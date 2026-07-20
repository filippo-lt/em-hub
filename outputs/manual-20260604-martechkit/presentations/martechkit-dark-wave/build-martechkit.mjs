import fs from "node:fs/promises";
import path from "node:path";
import { Canvas } from "/Users/ftosetto/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/node_modules/skia-canvas/lib/index.mjs";
import {
  Presentation,
  PresentationFile,
  connector,
  image,
  layers,
  shape,
  text,
} from "/Users/ftosetto/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";

const ROOT = "/Users/ftosetto/Projects/em-hub/outputs/manual-20260604-martechkit/presentations/martechkit-dark-wave";
const OUT = path.join(ROOT, "output");
const PREVIEW = path.join(ROOT, "preview");
const QA = path.join(ROOT, "qa");
const ASSETS = path.join(ROOT, "assets");
const WAVE_PATH = path.join(ASSETS, "mau-wave.png");
const WIDTH = 1280;
const HEIGHT = 720;

const C = {
  black: "#030403",
  panel: "#1F1E1E",
  panel2: "#252525",
  panel3: "#2F3828",
  green: "#D5F8B9",
  green2: "#B6D9A1",
  muted: "#A9ACA1",
  white: "#F7F6F1",
  line: "#B9D7A4",
  amber: "#C6893E",
  coral: "#E98D65",
  red: "#F06D5F",
  blue: "#8FBEEA",
  purple: "#AEA6F4",
};

const font = "Aptos";
const mono = "Aptos Mono";

function pos(x, y) {
  return { left: x, top: y };
}

function txt(value, x, y, w, h, size, color = C.white, extra = {}) {
  return text(value, {
    position: pos(x, y),
    width: w,
    height: h,
    style: {
      typeface: extra.mono ? mono : font,
      fontSize: size,
      color,
      fill: "none",
      bold: Boolean(extra.bold),
      alignment: extra.align ?? "left",
    },
  });
}

function border(line) {
  if (!line || line === "none") return undefined;
  if (typeof line !== "string") return line;
  const match = /^([\d.]+)px\s+(.+)$/.exec(line.trim());
  if (match) return { width: Number(match[1]), fill: match[2] };
  return { width: 1, fill: line };
}

function box(x, y, w, h, fill = C.panel2, line = undefined, radius = 18) {
  return shape({
    position: pos(x, y),
    width: w,
    height: h,
    fill,
    line: border(line),
    borderRadius: radius,
  });
}

function pill(label, x, y, w, fill, color = C.white) {
  return layers({ position: pos(x, y), width: w, height: 34 }, [
    box(0, 0, w, 34, fill, `1px ${fill}`, 14),
    txt(label, 0, 7, w, 18, 14, color, { align: "center", bold: true }),
  ]);
}

function line(x1, y1, x2, y2, color = C.line, width = 1.2, head = undefined) {
  return connector({
    from: { left: x1, top: y1 },
    to: { left: x2, top: y2 },
    line: { fill: color, width },
    head,
  });
}

function bg({ title, presenter = "", section = "" } = {}) {
  return [
    box(0, 0, WIDTH, HEIGHT, C.black, "none", 0),
    box(50, 54, 1180, 612, "#20201F", "1px #2E312B", 30),
    ...wave(520, 80, 650, 450, 0.62),
    txt(section || "MartechKit", 88, 80, 320, 22, 15, C.green, { bold: true }),
    txt(presenter, 1040, 80, 150, 22, 13, C.muted, { align: "right" }),
    title ? txt(title, 92, 126, 820, 70, 34, C.white, { bold: false }) : null,
  ].filter(Boolean);
}

function wave(x, y, w, h, opacityScale = 1) {
  return [
    box(x + 130, y + 26, w - 150, h - 80, "#2B3726", undefined, 28),
    box(x + 70, y + 168, w - 70, 56, "#3C4E31", undefined, 24),
    box(x + 270, y + 282, w - 310, 42, "#475C38", undefined, 20),
  ];
}

function mascot(x, y, s = 2.4, color = C.white) {
  return txt("MAU", x, y, 12 * s, 4 * s, Math.max(9, s * 3), color, { bold: true, mono: true });
}

function appIcon(x, y, label, fill = C.coral) {
  return layers({ position: pos(x, y), width: 82, height: 78 }, [
    box(12, 0, 58, 58, fill, `1px ${fill}`, 14),
    shape({ position: pos(28, 16), width: 26, height: 26, fill: C.white, borderRadius: 12 }),
    txt(label, 0, 64, 82, 14, 10.5, C.muted, { align: "center" }),
  ]);
}

function vendorBox(label, x, y, color, w = 118) {
  return layers({ position: pos(x, y), width: w, height: 42 }, [
    box(0, 0, w, 42, "#161716", `1px ${color}`, 12),
    txt(label, 0, 12, w, 16, 13, color, { align: "center", bold: true }),
  ]);
}

function statCallout(label, x, y, w, accent = C.green) {
  return layers({ position: pos(x, y), width: w, height: 62 }, [
    box(0, 0, w, 62, "#151615", `1px ${accent}`, 16),
    txt(label, 18, 18, w - 36, 22, 17, accent, { bold: true, align: "center" }),
  ]);
}

const slides = [
  {
    title: "",
    presenter: "Filippo + Victor",
    nodes: [
      ...bg({ presenter: "15-20 min", section: "" }),
      txt("MartechKit", 92, 170, 650, 88, 58, C.white),
      txt("One SDK for all our Martech", 94, 264, 620, 42, 28, C.green),
      txt("Unified Amplitude, RevenueCat and AppsFlyer across the portfolio", 96, 326, 640, 34, 20, C.muted),
      pill("Amplitude", 96, 406, 132, "#152B3F", C.blue),
      pill("RevenueCat", 244, 406, 146, "#29234A", C.purple),
      pill("AppsFlyer", 406, 406, 128, "#3A2917", "#F2C879"),
      pill("+ more", 550, 406, 104, "#2C3027", C.green2),
      txt("Filippo Tosetto · Engineering Manager", 96, 548, 360, 22, 15, C.white),
      txt("Victor Jalencas · Staff Engineer", 96, 574, 360, 22, 15, C.muted),
    ],
  },
  {
    title: "Same integration, wired N times",
    presenter: "Filippo",
    nodes: [
      ...bg({ title: "Same integration, wired N times", presenter: "Filippo" }),
      txt("Every app wires the same vendors from scratch. Different code, different versions, different event names.", 96, 194, 760, 44, 19, C.muted),
      ...["Photo Up", "Face AI", "Tattooist", "AI Design", "iMote", "Mirror"].flatMap((name, i) => {
        const x = 102 + i * 170;
        return [
          appIcon(x, 278, name),
          line(x + 41, 334, x + 41, 370, C.coral, 1),
          vendorBox("Amplitude", x - 18, 374, C.blue),
          vendorBox("RevenueCat", x - 18, 424, C.purple),
          vendorBox("AppsFlyer", x - 18, 474, "#F0BC68"),
        ];
      }),
      statCallout("6 apps x 3 vendors = 18 implementations to maintain", 318, 570, 640, C.coral),
    ],
  },
  {
    title: "What that costs us",
    presenter: "Filippo",
    nodes: [
      ...bg({ title: "What that costs us", presenter: "Filippo" }),
      txt("The duplication is not just wasteful. It breaks data quality and slows every Martech change.", 96, 194, 820, 42, 19, C.muted),
      ...[
        ["Mis-tracked events", "No reliable cross-app product analysis.", C.red],
        ["Martech bottlenecked", "Every experiment waits on per-app engineering.", C.amber],
        ["Cognitive load", "Every developer learns every vendor SDK.", C.green],
      ].flatMap(([head, body, color], i) => {
        const x = 108 + i * 360;
        return [
          box(x, 284, 310, 204, "#171817", `1px ${color}`, 22),
          shape({ position: pos(x + 28, 314), width: 46, height: 46, fill: "#111211", line: border(`1px ${color}`), borderRadius: 14 }),
          txt("!", x + 28, 320, 46, 32, 25, color, { align: "center", bold: true }),
          txt(head, x + 28, 384, 254, 28, 22, C.white, { bold: true }),
          txt(body, x + 28, 424, 246, 54, 17, C.muted),
        ];
      }),
      statCallout("The biggest cost lands on the data: inconsistent events mean inconsistent decisions", 210, 548, 860, C.green),
    ],
  },
  {
    title: "One library, single point of implementation",
    presenter: "Filippo -> Victor",
    nodes: [
      ...bg({ title: "One library, single point of implementation", presenter: "Filippo -> Victor" }),
      txt("The shift: apps integrate MartechKit once. Vendor changes ship as a version bump.", 96, 194, 840, 42, 19, C.muted),
      txt("Before", 138, 258, 420, 28, 18, C.coral, { bold: true, align: "center" }),
      txt("With MartechKit", 724, 258, 420, 28, 18, C.green, { bold: true, align: "center" }),
      ...[0, 1, 2].flatMap((i) => {
        const y = 316 + i * 76;
        return [appIcon(126, y, `App ${i + 1}`), line(206, y + 24, 446, 320, C.coral, 0.8), line(206, y + 24, 446, 396, C.coral, 0.8), line(206, y + 24, 446, 472, C.coral, 0.8)];
      }),
      vendorBox("Amplitude", 446, 316, C.blue, 140),
      vendorBox("RevenueCat", 446, 392, C.purple, 140),
      vendorBox("AppsFlyer", 446, 468, "#F0BC68", 140),
      ...[0, 1, 2].flatMap((i) => {
        const y = 316 + i * 76;
        return [appIcon(704, y, `App ${i + 1}`), line(784, y + 24, 908, 430, C.green, 1.2)];
      }),
      box(886, 380, 168, 98, "#1C2C1A", `1px ${C.green}`, 22),
      txt("MartechKit", 886, 410, 168, 28, 23, C.green, { align: "center", bold: true }),
      line(1054, 430, 1142, 340, C.green, 1.2),
      line(1054, 430, 1142, 430, C.green, 1.2),
      line(1054, 430, 1142, 520, C.green, 1.2),
      vendorBox("Amplitude", 1100, 316, C.blue, 140),
      vendorBox("RevenueCat", 1100, 406, C.purple, 140),
      vendorBox("AppsFlyer", 1100, 496, "#F0BC68", 140),
      txt("Handoff: Victor, how it actually works.", 96, 590, 780, 24, 18, C.green),
    ],
  },
  {
    title: "One clean API, vendors hidden inside",
    presenter: "Victor",
    nodes: [
      ...bg({ title: "One clean API, vendors hidden inside", presenter: "Victor" }),
      txt("MartechKit is a facade. App code calls one stable API; vendor specifics stay inside the library.", 96, 194, 860, 42, 19, C.muted),
      box(232, 270, 816, 82, "#311E18", `1px ${C.coral}`, 22),
      txt("App code: track(event)   identify(user)   entitlement()", 232, 296, 816, 28, 23, C.white, { align: "center", mono: true }),
      line(640, 352, 640, 414, C.green, 1.6),
      box(282, 414, 716, 102, "#1D321A", `1px ${C.green}`, 26),
      txt("MartechKit facade", 282, 442, 716, 34, 30, C.green, { align: "center", bold: true }),
      txt("one API in -> many vendor calls out", 282, 482, 716, 22, 16, C.muted, { align: "center" }),
      line(640, 516, 324, 574, C.green, 1.3),
      line(640, 516, 520, 574, C.green, 1.3),
      line(640, 516, 718, 574, C.green, 1.3),
      line(640, 516, 914, 574, C.green, 1.3),
      vendorBox("Amplitude", 256, 574, C.blue, 140),
      vendorBox("RevenueCat", 452, 574, C.purple, 140),
      vendorBox("AppsFlyer", 648, 574, "#F0BC68", 140),
      vendorBox("+ more", 844, 574, C.green2, 140),
    ],
  },
  {
    title: "Same event, same schema, everywhere",
    presenter: "Victor",
    nodes: [
      ...bg({ title: "Same event, same schema, everywhere", presenter: "Victor" }),
      txt("The unlock is the shared event dictionary: event names and schemas defined once, enforced by the library.", 96, 194, 900, 42, 19, C.muted),
      txt("Before", 144, 276, 400, 26, 18, C.coral, { bold: true, align: "center" }),
      box(116, 314, 430, 196, "#171817", `1px ${C.coral}`, 22),
      ...["buy_success", "purchase_done", "checkout_ok"].map((evt, i) => pill(evt, 178, 346 + i * 48, 220, "#2B1B17", C.coral)),
      txt("Three apps, one concept, three names", 144, 532, 360, 22, 15, C.muted, { align: "center" }),
      line(568, 412, 708, 412, C.green, 2, "triangle"),
      txt("With MartechKit", 748, 276, 400, 26, 18, C.green, { bold: true, align: "center" }),
      box(742, 314, 420, 196, "#1D321A", `1px ${C.green}`, 22),
      txt("SHARED EVENT DICTIONARY", 742, 342, 420, 22, 15, C.green, { bold: true, align: "center" }),
      ...["purchase_completed", "screen_viewed", "feature_used"].map((evt, i) => pill(evt, 838, 374 + i * 38, 230, "#111711", C.green)),
      txt("One schema -> analytics that actually compare", 746, 532, 414, 22, 15, C.muted, { align: "center" }),
      statCallout("Enforced in code, not remembered from a doc", 354, 586, 572, C.green),
    ],
  },
  {
    title: "From portfolio-wide tickets to a version bump",
    presenter: "Victor",
    nodes: [
      ...bg({ title: "From portfolio-wide tickets to a version bump", presenter: "Victor" }),
      txt("Integrate the library once. After that, Martech changes propagate as dependency updates.", 96, 194, 880, 42, 19, C.muted),
      txt("Integrate once", 132, 270, 260, 24, 18, C.green, { bold: true }),
      appIcon(132, 320, "App"),
      line(222, 350, 382, 350, C.green, 1.6, "triangle"),
      box(382, 306, 318, 88, "#1D321A", `1px ${C.green}`, 22),
      txt("Add MartechKit + config", 382, 336, 318, 28, 23, C.green, { align: "center", bold: true }),
      line(700, 350, 834, 350, C.green, 1.6, "triangle"),
      pill("Done", 834, 333, 112, "#1D321A", C.green),
      txt("Then every change is a version bump", 132, 454, 420, 24, 18, "#F0BC68", { bold: true }),
      box(132, 498, 430, 74, "#312615", `1px ${C.amber}`, 20),
      txt("MartechKit v1.1", 156, 516, 176, 22, 19, "#F0BC68", { bold: true, mono: true }),
      txt("new vendor · SDK update · new event", 156, 544, 330, 18, 14, C.muted),
      ...[0, 1, 2, 3, 4, 5].flatMap((i) => {
        const x = 664 + (i % 3) * 140;
        const y = 472 + Math.floor(i / 3) * 74;
        return [line(562, 535, x + 24, y + 24, C.amber, 0.8), appIcon(x, y, `v1.1`)];
      }),
    ],
  },
  {
    title: "Live on iOS, validated in 3 pilots",
    presenter: "Victor -> Filippo",
    nodes: [
      ...bg({ title: "Live on iOS, validated in 3 pilots", presenter: "Victor -> Filippo" }),
      txt("MartechKit is not a proposal. v1.0 is live on native iOS and has been validated in three pilot apps.", 96, 194, 920, 42, 19, C.muted),
      box(168, 278, 944, 96, "#1D321A", `1px ${C.green}`, 26),
      pill("Live", 210, 309, 110, "#D5F8B9", "#142013"),
      txt("MartechKit v1.0 - native iOS", 348, 304, 580, 34, 30, C.green, { bold: true }),
      txt("Validated in 3 pilot apps", 348, 340, 420, 20, 16, C.muted),
      ...[
        ["ScreenMirroring", 220],
        ["FaceAI", 510],
        ["Tattooist", 800],
      ].flatMap(([name, x]) => [
        box(x, 430, 230, 132, "#171817", `1px ${C.green}`, 22),
        appIcon(x + 72, 456, name, C.green2),
        pill("Live", x + 69, 526, 92, "#1D321A", C.green),
      ]),
      txt("Victor: integration effort, what surfaced early, and how the event dictionary held across real apps.", 164, 596, 880, 24, 18, C.green),
    ],
  },
  {
    title: "The road to full coverage",
    presenter: "Filippo",
    nodes: [
      ...bg({ title: "The road to full coverage", presenter: "Filippo" }),
      txt("iOS rollout now; Android and Flutter in parallel. Once those land, the whole portfolio is covered.", 96, 194, 900, 42, 19, C.muted),
      ...[
        ["1", "iOS portfolio rollout", "In progress", C.green],
        ["2", "Android library", "End of month target", "#F0BC68"],
        ["3", "Flutter library", "Follows swiftly after", "#F0BC68"],
      ].flatMap(([num, name, state, color], i) => {
        const y = 286 + i * 92;
        return [
          box(150, y, 680, 62, "#171817", `1px ${color}`, 18),
          shape({ position: pos(174, y + 14), width: 34, height: 34, fill: color, borderRadius: 17 }),
          txt(num, 174, y + 20, 34, 14, 15, C.black, { align: "center", bold: true }),
          txt(name, 230, y + 18, 310, 20, 20, C.white, { bold: true }),
          txt(state, 560, y + 21, 210, 18, 15, color, { align: "right" }),
          line(830, y + 31, 946, 424, color, 0.9),
        ];
      }),
      box(938, 380, 206, 88, "#1D321A", `1px ${C.green}`, 22),
      txt("Full portfolio coverage", 958, 406, 166, 28, 22, C.green, { align: "center", bold: true }),
      txt("One shared-components platform", 246, 568, 780, 20, 15, C.muted, { align: "center" }),
      ...["Parapet", "AI Gateway", "TVFoundationSDK", "MartechKit"].map((name, i) =>
        pill(name, 250 + i * 205, 600, name === "TVFoundationSDK" ? 174 : 150, name === "MartechKit" ? "#D5F8B9" : "#171817", name === "MartechKit" ? C.black : C.muted)
      ),
    ],
  },
  {
    title: "",
    presenter: "Filippo",
    nodes: [
      ...bg({ presenter: "Q&A", section: "" }),
      txt("Thank you", 96, 180, 560, 72, 54, C.white),
      txt("Questions?", 98, 262, 420, 42, 30, C.green),
      box(96, 388, 740, 110, "#171817", `1px ${C.green}`, 22),
      txt("Victor Jalencas", 126, 418, 200, 24, 21, C.green, { bold: true }),
      txt("designed and built MartechKit end-to-end, including the three pilot integrations.", 330, 421, 450, 24, 17, C.muted),
      box(96, 522, 740, 78, "#171817", `1px ${C.amber}`, 22),
      txt("David Sanchez & team", 126, 548, 240, 22, 19, "#F0BC68", { bold: true }),
      txt("shaped the initiative and the context behind it.", 372, 551, 360, 22, 17, C.muted),
      txt("MAU", 1030, 500, 180, 48, 30, C.green, { bold: true, mono: true }),
    ],
  },
];

async function build() {
  await fs.mkdir(OUT, { recursive: true });
  await fs.mkdir(PREVIEW, { recursive: true });
  await fs.mkdir(QA, { recursive: true });
  await fs.mkdir(ASSETS, { recursive: true });
  await writeWaveAsset();

  const deck = Presentation.create();
  const selectedSlides = slides.slice(0, process.env.SLIDE_LIMIT ? Number(process.env.SLIDE_LIMIT) : slides.length);
  selectedSlides.forEach((cfg, idx) => {
    const slide = deck.slides.add({ width: WIDTH, height: HEIGHT });
    const nodes = process.env.ELEMENT_LIMIT && idx === 0 ? cfg.nodes.slice(0, Number(process.env.ELEMENT_LIMIT)) : cfg.nodes;
    slide.compose(layers({ width: WIDTH, height: HEIGHT }, nodes));
    slide.speakerNotes.setText?.(`Slide ${idx + 1}: ${cfg.presenter}`);
  });

  const bad = findBadNumber(deck.toProto(), "deck");
  if (bad) {
    throw new Error(`Bad numeric value before export at ${bad}`);
  }

  const pptx = await PresentationFile.exportPptx(deck);
  await fs.writeFile(path.join(OUT, "martechkit-dark-wave.pptx"), pptx.data);

  if (!process.env.SKIP_PREVIEW) {
    const layoutSummaries = [];
    for (const [idx, slide] of deck.slides.items.entries()) {
      const png = await slide.export({ format: "png", scale: 1 });
      await fs.writeFile(path.join(PREVIEW, `slide-${String(idx + 1).padStart(2, "0")}.png`), await blobBytes(png));
      const layout = await slide.export({ format: "layout" });
      layoutSummaries.push({ slide: idx + 1, layout });
    }
    await fs.writeFile(path.join(QA, "layout.json"), JSON.stringify(layoutSummaries, null, 2));
  }
  await fs.writeFile(path.join(QA, "source-notes.txt"), "Source: presentations/MartechKit/MartechKit-presentation.md\nVisual reference: user-provided mau.io screenshot from 2026-06-04.\n");
}

async function blobBytes(value) {
  if (value?.data) return value.data;
  if (value?.arrayBuffer) return Buffer.from(await value.arrayBuffer());
  return value;
}

async function writeWaveAsset() {
  const canvas = new Canvas(900, 520);
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "#20201F";
  ctx.fillRect(0, 0, 900, 520);
  ctx.lineWidth = 1.1;
  for (let i = 0; i < 54; i += 1) {
    const t = i / 53;
    ctx.beginPath();
    const hue = i % 3 === 0 ? C.green : i % 3 === 1 ? C.green2 : "#D6B56C";
    ctx.strokeStyle = hue;
    ctx.globalAlpha = 0.34;
    for (let x = 0; x <= 900; x += 16) {
      const nx = x / 900;
      const y = 80 + t * 330 + Math.sin(nx * Math.PI * 3.2 + t * 4.8) * 72 + Math.sin(nx * Math.PI * 7.1) * 20;
      if (x === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();
  }
  ctx.globalAlpha = 1;
  await fs.writeFile(WAVE_PATH, await canvas.toBuffer("png"));
}

function findBadNumber(value, trail) {
  if (typeof value === "number" && !Number.isFinite(value)) return trail;
  if (!value || typeof value !== "object") return null;
  if (Array.isArray(value)) {
    for (let i = 0; i < value.length; i += 1) {
      const found = findBadNumber(value[i], `${trail}[${i}]`);
      if (found) return found;
    }
    return null;
  }
  for (const [key, child] of Object.entries(value)) {
    const found = findBadNumber(child, `${trail}.${key}`);
    if (found) return found;
  }
  return null;
}

build().catch((err) => {
  console.error(err);
  process.exit(1);
});
