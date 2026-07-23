#!/usr/bin/env python3
"""
email-digest.py — build a visually rich, email-safe HTML GCP cost digest.

Part of the gcp-spend pipeline. Reads the published data in metrics/gcp-spend/
and emits an inline-styled (Gmail-safe) HTML digest + a plain-text alternative.
Consumed by the cloud "Monthly cost digest" scheduled task, which drops the
output into a Gmail draft. Pure stdlib; no external deps.

Usage: python3 email-digest.py <YYYY-MM> <gcp-spend-dir> <out.html>
  <target>.json   (REQUIRED)  per-app cost_eur + mau
  <prior>.json    (optional)  prior-month precise costs (else index.html history)
  <target>.html   (optional)  service-level detail + display names + not-reporting
  index.html      (optional)  6-month history table (prior-month fallback)
Writes <out.html> and <out>.txt. Missing optional inputs just drop that section.
"""
import sys, os, re, json, calendar
from datetime import date

MON = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
FULLMON = {i:calendar.month_name[i] for i in range(1,13)}

# ---- palette (inline; email-safe) ----
INK="#0b0b0b"; INK2="#52514e"; MUTED="#898781"; GRID="#e7e6e0"
BLUE="#2a78d6"; BLUEBG="#e9f1fc"; BLUESOFT="#f3f7fd"
UP="#c2603f"; DOWN="#2f7d5b"; CARD="#ffffff"; PLANE="#f4f4f2"; BORDER="#e2e1da"
CHIPBG="#eef3fb"; CHIPINK="#1c5cab"

def eur(x):
    return "€{:,.2f}".format(x)
def eur0(x):
    return "€{:,.0f}".format(x)

def prev_month(target):
    y,m = int(target[:4]), int(target[5:7])
    m-=1
    if m==0: y-=1; m=12
    return "{:04d}-{:02d}".format(y,m)

def load_json(path):
    try:
        with open(path) as f: return json.load(f)
    except Exception: return None

def parse_target_html(html):
    """Return (display_names{slug->name}, project_ids{slug->pid}, services{slug->[(name,amt)]}, not_reporting[(name,pid)])."""
    names={}; pids={}; services={}; notrep=[]
    if not html: return names,pids,services,notrep
    # panels: <h2>Name<span class="project-id">pid</span></h2> ... table with svc/amt rows
    for m in re.finditer(r'<h2>(.*?)<span class="project-id">(.*?)</span></h2>(.*?)</table>', html, re.S):
        name=re.sub(r'<[^>]+>','',m.group(1)).strip()
        pid=m.group(2).strip()
        body=m.group(3)
        svcs=[]
        for r in re.finditer(r'<td class="svc">(.*?)</td>\s*<td class="amt">\$?([\d,]+\.?\d*)</td>', body, re.S):
            sname=re.sub(r'<[^>]+>','',r.group(1)).strip()
            amt=float(r.group(2).replace(',',''))
            svcs.append((sname,amt))
        slug=pid  # key services by project id; we map later via pid->slug
        services[pid]=svcs
        names[pid]=name
        pids[name]=pid
    # not reporting
    mrep=re.search(r'Not yet reporting.*?<ul>(.*?)</ul>', html, re.S)
    if mrep:
        for li in re.finditer(r'<li>(.*?)<code>\((.*?)\)</code>', mrep.group(1), re.S):
            nm=re.sub(r'<[^>]+>','',li.group(1)).strip()
            pid=li.group(2).strip()
            notrep.append((nm,pid))
    return names,pids,services,notrep

def parse_history(index_html):
    """Return {display_name: {month_label: value_float}} and {'Total':{month:val}} from the 6-month table."""
    hist={}
    if not index_html: return hist, []
    mt=re.search(r'Last 6 months.*?<table class="history">(.*?)</table>', index_html, re.S)
    if not mt: return hist, []
    tbl=mt.group(1)
    # month header labels — keep only real month abbreviations (drop "App"/"Avg" etc.)
    valid=set(MON.values())
    heads=[h for h in re.findall(r'<th[^>]*>\s*([A-Z][a-z]{2})\s*</th>', tbl) if h in valid]
    # rows
    for row in re.finditer(r'<tr>(.*?)</tr>', tbl, re.S):
        rr=row.group(1)
        appm=re.search(r'class="app">(?:<span[^>]*></span>)?(.*?)</td>', rr, re.S)
        if not appm: continue
        name=re.sub(r'<[^>]+>','',appm.group(1)).strip()
        vals=re.findall(r'<td[^>]*>\$([\d,]+)</td>', rr)
        vals=[float(v.replace(',','')) for v in vals]
        if name and vals:
            hist[name]=dict(zip(heads, vals[:len(heads)]))
    # totals from tfoot
    tot={}
    ft=re.search(r'<tfoot>(.*?)</tfoot>', index_html, re.S)
    if ft:
        tvals=re.findall(r'\$([\d,]+)', ft.group(1))
        tvals=[float(v.replace(',','')) for v in tvals]
        tot=dict(zip(heads, tvals[:len(heads)]))
    return hist, tot, heads

def main():
    target=sys.argv[1]
    base=sys.argv[2]
    out=sys.argv[3]
    y,m=int(target[:4]),int(target[5:7])
    prior=prev_month(target)
    cur=load_json(os.path.join(base,f"{target}.json"))
    if not cur or "apps" not in cur:
        print("ERROR: missing "+os.path.join(base,f"{target}.json")); sys.exit(2)
    prior_json=load_json(os.path.join(base,f"{prior}.json"))
    thtml=None
    p=os.path.join(base,f"{target}.html")
    if os.path.exists(p): thtml=open(p,encoding="utf-8").read()
    ihtml=None
    p=os.path.join(base,"index.html")
    if os.path.exists(p): ihtml=open(p,encoding="utf-8").read()

    names,pids,services,notrep=parse_target_html(thtml)
    hist_res=parse_history(ihtml)
    if len(hist_res)==3: hist,tot_hist,heads=hist_res
    else: hist,tot_hist,heads={},{},[]

    def titleize(slug):
        return names_by_slug.get(slug) or slug.replace("_"," ").title()

    # map slug -> display name / project id via target.html panels.
    # Primary match: normalised display name (e.g. "Chat Ultra" -> "chatultra") == slug.
    # Fallbacks: project-id contains slug; else titleise the slug.
    pid_to_name=names  # pid->name
    norm=lambda s: re.sub(r'[^a-z0-9]','',s.lower())
    normname_to_pid={ norm(nm):pid for pid,nm in pid_to_name.items() }
    names_by_slug={}
    pid_by_slug={}
    for slug in cur["apps"].keys():
        best=None
        if slug in normname_to_pid:
            best=normname_to_pid[slug]
        else:
            for pid in pid_to_name:
                pl=pid.lower()
                if pl.startswith(slug) or slug in pl.replace("-","").replace("_",""):
                    best=pid; break
        if best:
            names_by_slug[slug]=pid_to_name[best]; pid_by_slug[slug]=best
        else:
            names_by_slug[slug]=slug.replace("_"," ").title(); pid_by_slug[slug]=""

    # assemble app rows (cost>0)
    apps=[]
    for slug,d in cur["apps"].items():
        c=d.get("cost_eur") or 0.0
        if c<=0: continue
        apps.append({"slug":slug,"name":names_by_slug[slug],"pid":pid_by_slug.get(slug,""),
                     "cost":c,"mau":d.get("mau")})
    apps.sort(key=lambda a:-a["cost"])
    total=sum(a["cost"] for a in apps)

    # prior lookups
    def prior_cost(app):
        if prior_json and "apps" in prior_json:
            pd=prior_json["apps"].get(app["slug"])
            if pd and pd.get("cost_eur") is not None:
                return pd["cost_eur"], True   # precise
        # fallback: history table, prior month column by name
        plabel=MON[int(prior[5:7])]
        h=hist.get(app["name"])
        if h and plabel in h:
            return h[plabel], False  # rounded
        return None, False

    if prior_json and "apps" in prior_json:
        prior_total=sum((v.get("cost_eur") or 0) for v in prior_json["apps"].values())
        prior_total_precise=True
    else:
        plabel=MON[int(prior[5:7])]
        prior_total=tot_hist.get(plabel)
        prior_total_precise=False

    # top service = single biggest service line across all apps
    top_service=None
    if services:
        allsvc=[]
        for slug in cur["apps"]:
            pid=pid_by_slug.get(slug,"")
            for sn,amt in services.get(pid,[]):
                allsvc.append((sn,amt))
        if allsvc:
            allsvc.sort(key=lambda x:-x[1])
            top_service=allsvc[0]

    # ---------- build HTML ----------
    W="680"
    def bar(pct, h=22, bg=BLUEBG, fg=BLUE, radius=6):
        pct=max(0.0,min(100.0,pct))
        return (f'<div style="background:{bg};border-radius:{radius}px;height:{h}px;line-height:{h}px;font-size:0;">'
                f'<div style="background:{fg};height:{h}px;width:{pct:.3f}%;border-radius:{radius}px;font-size:0;">&nbsp;</div></div>')

    cells=[]
    # KPI 1 total
    cells.append(("Total spend", eur0(total), "exact "+eur(total), INK))
    # KPI 2 MoM
    if prior_total:
        dt=total-prior_total; pct=dt/prior_total*100 if prior_total else 0
        arrow="▲" if dt>=0 else "▼"; col=UP if dt>=0 else DOWN
        sign="+" if dt>=0 else "−"
        cells.append(("vs "+MON[int(prior[5:7])], f'{arrow} {abs(pct):.1f}%', f'{sign}{eur(abs(dt))[1:]} €'.replace(" €",""), col))
        cells[-1]=("vs "+MON[int(prior[5:7])], f'<span style="color:{col}">{arrow} {abs(pct):.1f}%</span>', f'<span style="color:{col}">{sign}{eur(abs(dt))}</span>', INK)
    else:
        cells.append(("vs prior month", "—", "no prior data", INK))
    # KPI 3 largest app
    if apps:
        la=apps[0]; share=la["cost"]/total*100
        cells.append(("Largest app", la["name"], f'{share:.1f}% of spend', INK))
    # KPI 4 top service
    if top_service:
        cells.append(("Top service", top_service[0], f'{top_service[1]/total*100:.1f}% of org total', INK))
    else:
        cells.append(("Apps reporting", str(len(apps)), "with billed spend", INK))

    kpi_html='<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:separate;border-spacing:10px 0;"><tr>'
    for label,val,meta,col in cells:
        kpi_html+=(f'<td width="25%" valign="top" style="background:{CARD};border:1px solid {BORDER};border-radius:12px;padding:14px 14px;">'
                   f'<div style="font-size:11px;color:{MUTED};font-weight:600;text-transform:uppercase;letter-spacing:.04em;margin-bottom:6px;">{label}</div>'
                   f'<div style="font-size:20px;color:{col};font-weight:700;line-height:1.15;">{val}</div>'
                   f'<div style="font-size:12px;color:{INK2};margin-top:4px;">{meta}</div></td>')
    kpi_html+='</tr></table>'

    # MoM total bars
    mom_html=""
    if prior_total:
        mx=max(total,prior_total)
        pl=MON[int(prior[5:7])]; cl=MON[m]
        def momrow(lbl,val,pct,fg):
            return (f'<tr><td width="46" style="font-size:12px;color:{INK2};font-weight:600;padding:5px 0;">{lbl}</td>'
                    f'<td style="padding:5px 8px;">{bar(pct,22,BLUEBG,fg)}</td>'
                    f'<td width="92" align="right" style="font-size:13px;font-weight:600;color:{INK};font-family:monospace;">{eur0(val)}</td></tr>')
        mom_html=(f'<div style="background:{CARD};border:1px solid {BORDER};border-radius:12px;padding:18px 20px;margin-top:14px;">'
                  f'<div style="font-size:15px;font-weight:700;color:{INK};">Month over month — total spend</div>'
                  f'<div style="font-size:12.5px;color:{MUTED};margin:2px 0 12px;">{pl} → {cl} across all reporting apps.</div>'
                  f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">'
                  +momrow(pl,prior_total,prior_total/mx*100,"#9cc0ee")
                  +momrow(cl,total,total/mx*100,BLUE)
                  +'</table></div>')

    # Spend by app table
    rows=""
    for a in apps:
        share=a["cost"]/total*100
        barw=a["cost"]/apps[0]["cost"]*100
        pc,precise=prior_cost(a)
        if pc is None or pc<=0:
            dtxt=f'<span style="display:inline-block;background:{CHIPBG};color:{CHIPINK};font-size:10.5px;font-weight:700;padding:1px 7px;border-radius:20px;">NEW</span>'
            ptxt="—"; pcttxt="—"
        else:
            d=a["cost"]-pc; pct=d/pc*100
            arrow="▲" if d>=0 else "▼"; col=UP if d>=0 else DOWN; sg="+" if d>=0 else "−"
            dtxt=f'<span style="color:{col};font-weight:600;"><span style="font-size:10px;">{arrow}</span> {abs(d):,.2f}</span>'
            pcttxt=f'<span style="color:{col};font-weight:600;">{sg}{abs(pct):.1f}%</span>'
            ptxt=(eur(pc) if precise else "≈"+eur0(pc))
        rows+=(f'<tr>'
               f'<td style="padding:9px 0;border-bottom:1px solid #f1f0ec;font-size:13.5px;"><b>{a["name"]}</b> '
               f'<span style="color:{MUTED};font-size:11px;font-family:monospace;">{a["pid"]}</span></td>'
               f'<td width="120" style="padding:9px 0 9px 14px;border-bottom:1px solid #f1f0ec;">{bar(barw,9,"#eef1f5",BLUE,3)}</td>'
               f'<td align="right" style="padding:9px 0 9px 16px;border-bottom:1px solid #f1f0ec;font-size:13.5px;font-family:monospace;white-space:nowrap;">{eur(a["cost"])}</td>'
               f'<td align="right" style="padding:9px 0 9px 16px;border-bottom:1px solid #f1f0ec;font-size:13.5px;font-family:monospace;color:{INK2};white-space:nowrap;">{ptxt}</td>'
               f'<td align="right" style="padding:9px 0 9px 16px;border-bottom:1px solid #f1f0ec;font-size:13px;font-family:monospace;white-space:nowrap;">{dtxt}</td>'
               f'<td align="right" style="padding:9px 0 9px 16px;border-bottom:1px solid #f1f0ec;font-size:13px;font-family:monospace;white-space:nowrap;">{pcttxt}</td>'
               f'</tr>')
    prior_label=MON[int(prior[5:7])]
    apptbl=(f'<div style="background:{CARD};border:1px solid {BORDER};border-radius:12px;padding:18px 20px;margin-top:14px;">'
            f'<div style="font-size:15px;font-weight:700;color:{INK};">Spend by app</div>'
            f'<div style="font-size:12.5px;color:{MUTED};margin:2px 0 12px;">Sorted by {MON[m]} spend. Bar shows each app\'s share of the month.</div>'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">'
            f'<tr>'
            f'<th align="left" style="font-size:11px;color:{MUTED};font-weight:600;text-transform:uppercase;padding-bottom:8px;border-bottom:1px solid {GRID};">App</th>'
            f'<th align="left" style="font-size:11px;color:{MUTED};font-weight:600;text-transform:uppercase;padding:0 0 8px 14px;border-bottom:1px solid {GRID};">Share</th>'
            f'<th align="right" style="font-size:11px;color:{MUTED};font-weight:600;text-transform:uppercase;padding:0 0 8px 16px;border-bottom:1px solid {GRID};">{MON[m]}</th>'
            f'<th align="right" style="font-size:11px;color:{MUTED};font-weight:600;text-transform:uppercase;padding:0 0 8px 16px;border-bottom:1px solid {GRID};">{prior_label}</th>'
            f'<th align="right" style="font-size:11px;color:{MUTED};font-weight:600;text-transform:uppercase;padding:0 0 8px 16px;border-bottom:1px solid {GRID};">&#916;</th>'
            f'<th align="right" style="font-size:11px;color:{MUTED};font-weight:600;text-transform:uppercase;padding:0 0 8px 16px;border-bottom:1px solid {GRID};">&#916; %</th>'
            f'</tr>{rows}</table></div>')

    # Service breakdown top 3
    svc_html=""
    if services and apps:
        blocks=""
        for a in apps[:3]:
            pid=a["pid"]; svcs=services.get(pid,[])
            if not svcs: continue
            svcs=sorted(svcs,key=lambda x:-x[1])
            top=svcs[:4]; rest=svcs[4:]
            mx=top[0][1] if top else 1
            srows=""
            for sn,amt in top:
                srows+=(f'<tr><td style="font-size:12.5px;color:{INK2};padding:2px 0;">{sn}</td>'
                        f'<td align="right" width="90" style="font-size:12.5px;font-family:monospace;padding:2px 0;">{eur(amt)}</td>'
                        f'<td align="right" width="44" style="font-size:11px;color:{MUTED};font-family:monospace;padding:2px 0;">{amt/a["cost"]*100:.1f}%</td></tr>'
                        f'<tr><td colspan="3" style="padding:0 0 3px;">{bar(amt/mx*100,6,"#e4ebf4",BLUE,3)}</td></tr>')
            if rest:
                ro=sum(x[1] for x in rest)
                srows+=(f'<tr><td style="font-size:12.5px;color:{MUTED};font-style:italic;padding:2px 0;">Other {len(rest)} service{"s" if len(rest)!=1 else ""}</td>'
                        f'<td align="right" style="font-size:12.5px;font-family:monospace;color:{MUTED};padding:2px 0;">{eur(ro)}</td>'
                        f'<td align="right" style="font-size:11px;color:{MUTED};font-family:monospace;padding:2px 0;">{ro/a["cost"]*100:.1f}%</td></tr>')
            blocks+=(f'<div style="border:1px solid {GRID};border-radius:10px;padding:14px 16px;background:{BLUESOFT};margin-bottom:14px;">'
                     f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>'
                     f'<td style="font-size:13.5px;font-weight:700;color:{INK};">{a["name"]} <span style="color:{MUTED};font-size:11px;font-family:monospace;font-weight:400;">{a["pid"]}</span></td>'
                     f'<td align="right" style="font-size:14px;font-weight:700;font-family:monospace;">{eur(a["cost"])}</td></tr></table>'
                     f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:8px;">{srows}</table></div>')
        if blocks:
            svc_html=(f'<div style="background:{CARD};border:1px solid {BORDER};border-radius:12px;padding:18px 20px;margin-top:14px;">'
                      f'<div style="font-size:15px;font-weight:700;color:{INK};">Service breakdown — top {min(3,len(apps))} apps</div>'
                      f'<div style="font-size:12.5px;color:{MUTED};margin:2px 0 14px;">Where each leading app\'s spend actually goes.</div>'
                      f'{blocks}</div>')

    # Cost per MAU
    mau_rows=""
    eff=[a for a in apps if a.get("mau")]
    eff.sort(key=lambda a:a["cost"]/a["mau"])
    for a in eff:
        per=a["cost"]/a["mau"]*1000
        mau_rows+=(f'<tr>'
                   f'<td style="padding:9px 0;border-bottom:1px solid #f1f0ec;font-size:13.5px;"><b>{a["name"]}</b></td>'
                   f'<td align="right" style="padding:9px 0 9px 16px;border-bottom:1px solid #f1f0ec;font-size:13.5px;font-family:monospace;">{a["mau"]:,}</td>'
                   f'<td align="right" style="padding:9px 0 9px 16px;border-bottom:1px solid #f1f0ec;font-size:13.5px;font-family:monospace;">{eur(a["cost"])}</td>'
                   f'<td align="right" style="padding:9px 0 9px 16px;border-bottom:1px solid #f1f0ec;font-size:13.5px;font-family:monospace;">€{per:,.2f}</td></tr>')
    mau_html=""
    if mau_rows:
        mau_html=(f'<div style="background:{CARD};border:1px solid {BORDER};border-radius:12px;padding:18px 20px;margin-top:14px;">'
                  f'<div style="font-size:15px;font-weight:700;color:{INK};">Cost efficiency — spend per user</div>'
                  f'<div style="font-size:12.5px;color:{MUTED};margin:2px 0 12px;">{MON[m]} cost &#247; monthly active users, per 1,000 MAU. Sorted most efficient first. Apps without MAU are omitted.</div>'
                  f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">'
                  f'<tr>'
                  f'<th align="left" style="font-size:11px;color:{MUTED};font-weight:600;text-transform:uppercase;padding-bottom:8px;border-bottom:1px solid {GRID};">App</th>'
                  f'<th align="right" style="font-size:11px;color:{MUTED};font-weight:600;text-transform:uppercase;padding:0 0 8px 16px;border-bottom:1px solid {GRID};">MAU</th>'
                  f'<th align="right" style="font-size:11px;color:{MUTED};font-weight:600;text-transform:uppercase;padding:0 0 8px 16px;border-bottom:1px solid {GRID};">{MON[m]} cost</th>'
                  f'<th align="right" style="font-size:11px;color:{MUTED};font-weight:600;text-transform:uppercase;padding:0 0 8px 16px;border-bottom:1px solid {GRID};">&#8364; / 1k MAU</th>'
                  f'</tr>{mau_rows}</table>'
                  f'<div style="font-size:11.5px;color:{MUTED};margin-top:10px;">Note: GCP-only &#8364;/MAU is not directly comparable across apps — some route AI spend through GCP while others use a separate AI provider.</div>'
                  f'</div>')

    # Not reporting
    nr_html=""
    if notrep:
        items=", ".join(f'{nm} <span style="font-family:monospace;color:{MUTED};">({pid})</span>' for nm,pid in notrep)
        nr_html=(f'<div style="background:#fbf8ef;border:1px solid #ece0bd;border-radius:10px;padding:12px 16px;margin-top:14px;font-size:12.5px;color:{INK2};">'
                 f'<b style="color:{INK};">Not yet reporting.</b> Billing export not enabled — these appear automatically once their export tables come online: {items}.</div>')

    gen=cur.get("generated_at","")
    foot=(f'<div style="color:{MUTED};font-size:11.5px;text-align:center;margin-top:12px;">'
          f'Source: GCP billing export{" · generated "+gen if gen else ""} · figures in EUR, net of credits.</div>')

    prior_note=""
    if prior_total and not prior_total_precise:
        prior_note=(f'<div style="color:{MUTED};font-size:11px;text-align:center;margin-top:4px;">'
                    f'Prior-month figures (≈) are from the 12-month history dashboard; current month is exact.</div>')

    grad=f"background:{'#22588f'};background:linear-gradient(135deg,#1c3f66 0%,#2a78d6 100%);"
    masthead=(f'<div style="{grad}border-radius:14px;padding:24px 26px;">'
              f'<div style="font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#cfe0f3;font-weight:600;margin-bottom:6px;">Cloud Cost Digest</div>'
              f'<div style="font-size:25px;font-weight:700;color:#ffffff;">GCP Spend — {FULLMON[m]} {y}</div>'
              f'<div style="font-size:13px;color:#d7e4f4;margin-top:6px;">{len(apps)} apps reporting · net cost, credits applied · all figures EUR</div></div>')

    doc=(f'<!doctype html><html><head><meta charset="utf-8">'
         f'<meta name="viewport" content="width=device-width,initial-scale=1">'
         f'<title>GCP Spend Digest — {target}</title></head>'
         f'<body style="margin:0;padding:0;background:{PLANE};">'
         f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{PLANE};">'
         f'<tr><td align="center" style="padding:22px 12px 48px;">'
         f'<table role="presentation" width="{W}" cellpadding="0" cellspacing="0" style="width:{W}px;max-width:100%;'
         f'font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,Helvetica,Arial,sans-serif;color:{INK};">'
         f'<tr><td>{masthead}</td></tr>'
         f'<tr><td style="padding-top:14px;">{kpi_html}</td></tr>'
         f'<tr><td>{mom_html}</td></tr>'
         f'<tr><td>{apptbl}</td></tr>'
         f'<tr><td>{svc_html}</td></tr>'
         f'<tr><td>{mau_html}</td></tr>'
         f'<tr><td>{nr_html}</td></tr>'
         f'<tr><td>{foot}{prior_note}</td></tr>'
         f'</table></td></tr></table></body></html>')

    # ---- plain-text alternative ----
    tl=[f"GCP Spend — {FULLMON[m]} {y}", ""]
    if prior_total:
        dt=total-prior_total; pct=dt/prior_total*100 if prior_total else 0
        sign="+" if dt>=0 else "-"
        tl.append(f"Total: {eur(total)}  ({sign}{abs(pct):.1f}% / {sign}{eur(abs(dt))} vs {MON[int(prior[5:7])]})")
    else:
        tl.append(f"Total: {eur(total)}")
    if apps:
        tl.append(f"Largest app: {apps[0]['name']} ({apps[0]['cost']/total*100:.1f}% of spend)."
                  + (f" Top service: {top_service[0]} ({top_service[1]/total*100:.1f}% of org total)." if top_service else ""))
    tl+=["","Spend by app (month | delta vs prior):"]
    for a in apps:
        pc,_=prior_cost(a)
        if pc and pc>0:
            d=a["cost"]-pc; tl.append(f"  {a['name']:<18} {eur(a['cost']):>12}   {'+' if d>=0 else '-'}{abs(d/pc*100):.1f}%")
        else:
            tl.append(f"  {a['name']:<18} {eur(a['cost']):>12}   NEW")
    tl+=["","Full visual breakdown in the HTML version of this email.",
         f"Source: GCP billing export{' · generated '+gen if gen else ''} · figures in EUR, net of credits."]
    txt="\n".join(tl)

    with open(out,"w",encoding="utf-8") as f: f.write(doc)
    txt_path=os.path.splitext(out)[0]+".txt"
    with open(txt_path,"w",encoding="utf-8") as f: f.write(txt)
    print(f"Wrote {out} and {txt_path}: {len(apps)} apps, total {eur(total)}, prior_total={prior_total} precise={prior_total_precise}")

if __name__=="__main__":
    main()
