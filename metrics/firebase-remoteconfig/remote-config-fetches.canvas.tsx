
import {
  Callout,
  Card,
  CardBody,
  CardHeader,
  Grid,
  H1,
  H2,
  Link,
  Pill,
  Row,
  Stack,
  Stat,
  Table,
  Text,
  mergeStyle,
  useCanvasState,
  useHostTheme,
} from 'cursor/canvas';

type FetchRow = {
  friendly_name: string;
  project_id: string;
  env: 'dev' | 'prod';
  avg_daily: number | null;
  peak_daily: number | null;
  peak_day: string | null;
  peak_pct: number | null;
  trend: string;
  trend_kind: 'up' | 'down' | 'flat' | 'none';
  status_tier: 'billable' | 'watch' | 'ok' | 'na';
  status_label: string;
  est_monthly_cost: number | null;
  warn: boolean;
  mau: number | null;
  fetches_per_user_per_day: number | null;
  error: string | null;
};

type Snapshot = {
  share_title: string;
  generated_at: string;
  days: number;
  trend_label: string;
  daily_free: number;
  has_amplitude: boolean;
  rows: FetchRow[];
};

type EnvTab = 'prod' | 'dev';


const snapshot: Snapshot = {
  "share_title": "Utilities \u2014 Remote Config fetch usage",
  "generated_at": "2026-07-20T15:50:49.190888+00:00",
  "days": 30,
  "trend_label": "7d vs prior 7d",
  "daily_free": 100000,
  "has_amplitude": true,
  "rows": [
    {
      "friendly_name": "AI Cleaner Android",
      "project_id": "aicleaner-android-prod",
      "env": "prod",
      "avg_daily": 1091181,
      "peak_daily": 1239385,
      "peak_day": "2026-06-30",
      "peak_pct": 1239.385,
      "trend": "Down 21%",
      "trend_kind": "down",
      "status_tier": "billable",
      "status_label": "Billable \u2014 12.4\u00d7 over free tier",
      "est_monthly_cost": 178.412634,
      "est_daily_cost_peak": 6.83631,
      "warn": true,
      "mau": 1521886,
      "fetches_per_user_per_day": 0.72,
      "error": null
    },
    {
      "friendly_name": "iMote",
      "project_id": "imote-prod",
      "env": "prod",
      "avg_daily": 319794,
      "peak_daily": 371002,
      "peak_day": "2026-07-05",
      "peak_pct": 371.002,
      "trend": "Down 8%",
      "trend_kind": "down",
      "status_tier": "billable",
      "status_label": "Billable \u2014 3.7\u00d7 over free tier",
      "est_monthly_cost": 39.56292,
      "est_daily_cost_peak": 1.626012,
      "warn": true,
      "mau": 915891,
      "fetches_per_user_per_day": 0.35,
      "error": null
    },
    {
      "friendly_name": "AI Cleaner",
      "project_id": "ai-cleaner-prod",
      "env": "prod",
      "avg_daily": 60663,
      "peak_daily": 66203,
      "peak_day": "2026-06-21",
      "peak_pct": 66.203,
      "trend": "Flat",
      "trend_kind": "flat",
      "status_tier": "watch",
      "status_label": "~66% of free tier \u2014 watch",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": true,
      "mau": 480377,
      "fetches_per_user_per_day": 0.13,
      "error": null
    },
    {
      "friendly_name": "Video Up",
      "project_id": "video-up-video-editor",
      "env": "prod",
      "avg_daily": 33741,
      "peak_daily": 38732,
      "peak_day": "2026-06-20",
      "peak_pct": 38.732,
      "trend": "Flat",
      "trend_kind": "flat",
      "status_tier": "watch",
      "status_label": "~39% of free tier \u2014 watch",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": true,
      "mau": 273469,
      "fetches_per_user_per_day": 0.12,
      "error": null
    },
    {
      "friendly_name": "ChatUltra",
      "project_id": "chatai2-32311",
      "env": "prod",
      "avg_daily": 27101,
      "peak_daily": 30842,
      "peak_day": "2026-07-18",
      "peak_pct": 30.842000000000002,
      "trend": "Up 7%",
      "trend_kind": "up",
      "status_tier": "watch",
      "status_label": "~31% of free tier \u2014 watch",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": true,
      "mau": 364192,
      "fetches_per_user_per_day": 0.07,
      "error": null
    },
    {
      "friendly_name": "Tattooist",
      "project_id": "tattooist-prod",
      "env": "prod",
      "avg_daily": 25201,
      "peak_daily": 42738,
      "peak_day": "2026-07-14",
      "peak_pct": 42.738,
      "trend": "Up 46%",
      "trend_kind": "up",
      "status_tier": "watch",
      "status_label": "~43% of free tier \u2014 watch",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": true,
      "mau": 168403,
      "fetches_per_user_per_day": 0.15,
      "error": null
    },
    {
      "friendly_name": "Music Player",
      "project_id": "mesut-music-player",
      "env": "prod",
      "avg_daily": 17481,
      "peak_daily": 19278,
      "peak_day": "2026-06-20",
      "peak_pct": 19.278000000000002,
      "trend": "Flat",
      "trend_kind": "flat",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "AI Design",
      "project_id": "aihomedesign-prod",
      "env": "prod",
      "avg_daily": 4345,
      "peak_daily": 5277,
      "peak_day": "2026-07-13",
      "peak_pct": 5.277,
      "trend": "Flat",
      "trend_kind": "flat",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": 53902,
      "fetches_per_user_per_day": 0.08,
      "error": null
    },
    {
      "friendly_name": "Ereasy",
      "project_id": "ereasy-maetch",
      "env": "prod",
      "avg_daily": 4309,
      "peak_daily": 5307,
      "peak_day": "2026-06-21",
      "peak_pct": 5.3069999999999995,
      "trend": "Down 10%",
      "trend_kind": "down",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "PDF Editor",
      "project_id": "main-pdf-editor",
      "env": "prod",
      "avg_daily": 3200,
      "peak_daily": 9390,
      "peak_day": "2026-07-09",
      "peak_pct": 9.39,
      "trend": "Down 35%",
      "trend_kind": "down",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "Photo Up",
      "project_id": "photo-up-prod",
      "env": "prod",
      "avg_daily": 2824,
      "peak_daily": 3651,
      "peak_day": "2026-06-20",
      "peak_pct": 3.6510000000000002,
      "trend": "Flat",
      "trend_kind": "flat",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "SpamSafe",
      "project_id": "spamsafe-prod",
      "env": "prod",
      "avg_daily": 392,
      "peak_daily": 600,
      "peak_day": "2026-06-21",
      "peak_pct": 0.6,
      "trend": "Flat",
      "trend_kind": "flat",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "Mirage",
      "project_id": "mirageai-prod",
      "env": "prod",
      "avg_daily": 157,
      "peak_daily": 184,
      "peak_day": "2026-07-04",
      "peak_pct": 0.184,
      "trend": "Flat",
      "trend_kind": "flat",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "ScreenMirroring",
      "project_id": "screenmirroring-prod",
      "env": "prod",
      "avg_daily": 124,
      "peak_daily": 174,
      "peak_day": "2026-07-02",
      "peak_pct": 0.174,
      "trend": "Down 23%",
      "trend_kind": "down",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": 1544,
      "fetches_per_user_per_day": 0.08,
      "error": null
    },
    {
      "friendly_name": "iMote",
      "project_id": "imote-dev",
      "env": "dev",
      "avg_daily": 122,
      "peak_daily": 501,
      "peak_day": "2026-07-08",
      "peak_pct": 0.501,
      "trend": "Up 111%",
      "trend_kind": "up",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "Goya",
      "project_id": "goyaai-prod",
      "env": "prod",
      "avg_daily": 103,
      "peak_daily": 138,
      "peak_day": "2026-06-26",
      "peak_pct": 0.13799999999999998,
      "trend": "Down 17%",
      "trend_kind": "down",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "SpamSafe",
      "project_id": "spamsafe-dev",
      "env": "dev",
      "avg_daily": 98,
      "peak_daily": 303,
      "peak_day": "2026-07-09",
      "peak_pct": 0.303,
      "trend": "Down 76%",
      "trend_kind": "down",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "Step Counter",
      "project_id": "stepcounter-mau-prod",
      "env": "prod",
      "avg_daily": 77,
      "peak_daily": 124,
      "peak_day": "2026-07-17",
      "peak_pct": 0.124,
      "trend": "Up 38%",
      "trend_kind": "up",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "AI Cleaner",
      "project_id": "ai-cleaner-dev",
      "env": "dev",
      "avg_daily": 60,
      "peak_daily": 89,
      "peak_day": "2026-07-19",
      "peak_pct": 0.089,
      "trend": "Up 34%",
      "trend_kind": "up",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "AI Design",
      "project_id": "aihomedesign-dev",
      "env": "dev",
      "avg_daily": 59,
      "peak_daily": 139,
      "peak_day": "2026-07-14",
      "peak_pct": 0.13899999999999998,
      "trend": "Down 17%",
      "trend_kind": "down",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "Photo Up",
      "project_id": "photo-up-dev",
      "env": "dev",
      "avg_daily": 47,
      "peak_daily": 130,
      "peak_day": "2026-07-19",
      "peak_pct": 0.13,
      "trend": "Up 13%",
      "trend_kind": "up",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "Video Up",
      "project_id": "video-up-video-editor-dev",
      "env": "dev",
      "avg_daily": 36,
      "peak_daily": 92,
      "peak_day": "2026-07-01",
      "peak_pct": 0.092,
      "trend": "Up 13%",
      "trend_kind": "up",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "FaceAI",
      "project_id": "faceai-prod",
      "env": "prod",
      "avg_daily": 24,
      "peak_daily": 38,
      "peak_day": "2026-06-28",
      "peak_pct": 0.038,
      "trend": "Up 10%",
      "trend_kind": "up",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": 279,
      "fetches_per_user_per_day": 0.09,
      "error": null
    },
    {
      "friendly_name": "Ereasy",
      "project_id": "ereasy-dev",
      "env": "dev",
      "avg_daily": 23,
      "peak_daily": 65,
      "peak_day": "2026-07-01",
      "peak_pct": 0.065,
      "trend": "Up 37%",
      "trend_kind": "up",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "AI Cleaner Android",
      "project_id": "aicleaner-android-dev",
      "env": "dev",
      "avg_daily": 21,
      "peak_daily": 41,
      "peak_day": "2026-07-15",
      "peak_pct": 0.041,
      "trend": "Down 10%",
      "trend_kind": "down",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "FaceAI",
      "project_id": "faceai-dev",
      "env": "dev",
      "avg_daily": 14,
      "peak_daily": 41,
      "peak_day": "2026-07-01",
      "peak_pct": 0.041,
      "trend": "Up 22%",
      "trend_kind": "up",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "Step Counter",
      "project_id": "stepcounter-mau-dev",
      "env": "dev",
      "avg_daily": 12,
      "peak_daily": 40,
      "peak_day": "2026-07-16",
      "peak_pct": 0.04,
      "trend": "Up 212%",
      "trend_kind": "up",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "Music Player",
      "project_id": "mp3-music-player-dev",
      "env": "dev",
      "avg_daily": 3,
      "peak_daily": 6,
      "peak_day": "2026-07-02",
      "peak_pct": 0.006,
      "trend": "Up 20%",
      "trend_kind": "up",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "PDF Editor",
      "project_id": "pdf-editor-converter-dev",
      "env": "dev",
      "avg_daily": 2,
      "peak_daily": 2,
      "peak_day": "2026-06-22",
      "peak_pct": 0.002,
      "trend": "Flat",
      "trend_kind": "flat",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "ScreenMirroring",
      "project_id": "screenmirroring-dev",
      "env": "dev",
      "avg_daily": 1,
      "peak_daily": 1,
      "peak_day": "2026-07-02",
      "peak_pct": 0.001,
      "trend": "Flat",
      "trend_kind": "flat",
      "status_tier": "ok",
      "status_label": "under free tier",
      "est_monthly_cost": 0.0,
      "est_daily_cost_peak": 0.0,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    },
    {
      "friendly_name": "TruthSeeker",
      "project_id": "ai-truthseeker-prod",
      "env": "prod",
      "avg_daily": null,
      "peak_daily": null,
      "peak_day": null,
      "peak_pct": null,
      "trend": "\u2014",
      "trend_kind": "none",
      "status_tier": "na",
      "status_label": "\u2014",
      "est_monthly_cost": null,
      "est_daily_cost_peak": null,
      "warn": false,
      "mau": null,
      "fetches_per_user_per_day": null,
      "error": null
    }
  ]
};


const PRICING_URL = 'https://firebase.google.com/docs/remote-config/pricing';

function fmt(n: number | null | undefined): string {
  if (n == null) return '—';
  return n.toLocaleString('en-US');
}

function fmtUsd(n: number | null | undefined): string {
  if (n == null) return '—';
  return `$${n.toFixed(2)}`;
}

function sortRows(rows: FetchRow[]): FetchRow[] {
  return [...rows].sort((a, b) => {
    const aAvg = a.avg_daily ?? -1;
    const bAvg = b.avg_daily ?? -1;
    if (bAvg !== aAvg) return bAvg - aAvg;
    return a.friendly_name.localeCompare(b.friendly_name);
  });
}

function rowTone(r: FetchRow) {
  if (r.error || r.avg_daily == null) return 'neutral' as const;
  if (r.status_tier === 'billable') return 'danger' as const;
  if (r.status_tier === 'watch') return 'warning' as const;
  return 'success' as const;
}

function statusTone(tier: FetchRow['status_tier']) {
  if (tier === 'billable') return 'warning' as const;
  if (tier === 'watch') return 'warning' as const;
  if (tier === 'ok') return 'success' as const;
  return 'neutral' as const;
}

function trendPill(trend: string, kind: FetchRow['trend_kind'], projectId: string) {
  if (kind === 'none') return trend;
  const tone = kind === 'up' ? 'warning' : kind === 'down' ? 'success' : 'neutral';
  return (
    <Pill key={`trend-${projectId}`} tone={tone} size="small" active={kind !== 'flat'}>
      {trend}
    </Pill>
  );
}

function statusCell(r: FetchRow) {
  if (r.error || r.avg_daily == null) return r.status_label;
  return (
    <Pill key={`status-${r.project_id}`} tone={statusTone(r.status_tier)} size="small" active={r.status_tier !== 'ok'}>
      {r.status_label}
    </Pill>
  );
}

function MetricCard({
  label,
  value,
  tone,
}: {
  label: string;
  value: string;
  tone?: 'danger' | 'success' | 'info';
}) {
  return (
    <Card>
      <CardBody style={{ padding: 14 }}>
        <Stat value={value} label={label} tone={tone} />
      </CardBody>
    </Card>
  );
}

function buildTableRows(envRows: FetchRow[], hasAmplitude: boolean) {
  const dash = '—';
  return envRows.map((r) => {
    const mauCell = hasAmplitude ? (r.mau != null ? fmt(r.mau) : dash) : null;
    const fpuCell = hasAmplitude
      ? r.fetches_per_user_per_day != null
        ? r.fetches_per_user_per_day.toFixed(2)
        : dash
      : null;
    if (r.error) {
      const row = [r.friendly_name, dash, dash, r.error, dash, dash];
      if (hasAmplitude) row.push(dash, dash);
      return row;
    }
    if (r.avg_daily == null) {
      const row = [r.friendly_name, dash, dash, 'no data', dash, dash];
      if (hasAmplitude) row.push(dash, dash);
      return row;
    }
    const row = [
      r.friendly_name,
      fmt(r.avg_daily),
      <Text key={`${r.project_id}-cost`} weight={r.status_tier === 'billable' ? 'semibold' : 'normal'}>
        {fmtUsd(r.est_monthly_cost)}
      </Text>,
      statusCell(r),
      fmt(r.peak_daily),
      trendPill(r.trend, r.trend_kind, r.project_id),
    ];
    if (hasAmplitude) row.push(mauCell, fpuCell);
    return row;
  });
}

export default function RemoteConfigFetchesDashboard() {
  const theme = useHostTheme();
  const { share_title, generated_at, days, trend_label, daily_free, has_amplitude, rows: rawRows } = snapshot;
  const [tab, setTab] = useCanvasState<EnvTab>('envTab', 'prod');

  const prodRows = sortRows(rawRows.filter((r) => r.env === 'prod'));
  const devRows = sortRows(rawRows.filter((r) => r.env === 'dev'));
  const activeRows = tab === 'prod' ? prodRows : devRows;

  const blazeMonthly = prodRows.reduce((s, r) => s + (r.est_monthly_cost ?? 0), 0);
  const billableCount = prodRows.filter((r) => r.status_tier === 'billable').length;
  const generatedLabel = generated_at.slice(0, 16).replace('T', ' ');

  const headers = [
    'Project',
    `Avg fetches/day (last ${days}d)`,
    'Projected $/mo',
    'Status',
    'Peak/day',
    `Trend (${trend_label})`,
  ];
  const columnAlign: Array<'left' | 'right'> = ['left', 'right', 'right', 'left', 'right', 'left'];
  if (has_amplitude) {
    headers.push('MAU (latest month)', 'Fetches/user/day');
    columnAlign.push('right', 'right');
  }

  return (
    <div
      style={mergeStyle({
        background: theme.bg.editor,
        color: theme.text.primary,
        minHeight: '100%',
        padding: 24,
        maxWidth: 1180,
        margin: '0 auto',
      })}
    >
      <Stack gap={16}>
        <Stack gap={6}>
          <H1>{share_title}</H1>
          <Text tone="secondary" size="small">
            Generated {generatedLabel} UTC · {days}-day window · FetchRemoteConfig ·{' '}
            <Link href={PRICING_URL}>Blaze pricing</Link>
          </Text>
        </Stack>

        <Grid columns={3} gap={12}>
          <MetricCard
            label="Projected Blaze overage / month (prod)"
            value={fmtUsd(blazeMonthly)}
            tone={blazeMonthly > 0 ? 'danger' : 'success'}
          />
          <MetricCard
            label="Billable prod projects"
            value={String(billableCount)}
            tone={billableCount > 0 ? 'danger' : 'info'}
          />
          <MetricCard label="Free fetches / day" value={fmt(daily_free)} />
        </Grid>

        {blazeMonthly > 0 ? (
          <Callout tone="warning" title="Cost impact">
            Prod volume exceeds the daily free tier on at least one project. Orange trend chips mean fetches are rising.
          </Callout>
        ) : null}

        <H2>Cost impact — your apps</H2>

        <Card>
          <CardHeader
            trailing={
              <Row gap={6}>
                <Pill active={tab === 'prod'} onClick={() => setTab('prod')}>
                  Prod ({prodRows.length})
                </Pill>
                <Pill active={tab === 'dev'} onClick={() => setTab('dev')}>
                  Dev ({devRows.length})
                </Pill>
              </Row>
            }
          >
            {tab === 'prod' ? 'Production' : 'Development'}
          </CardHeader>
          <CardBody style={{ padding: 0 }}>
            <Table
              headers={headers}
              rows={buildTableRows(activeRows, has_amplitude)}
              columnAlign={columnAlign}
              striped
              stickyHeader
              framed={false}
              rowTone={activeRows.map((r) => rowTone(r))}
            />
          </CardBody>
        </Card>

        <Text tone="tertiary" size="small">
          Trend: orange = Up, green = Down, gray = Flat ({trend_label}).
          {has_amplitude
            ? ' Fetches/user/day = avg daily fetches ÷ MAU; ~1.0 is healthy, ≫1 suggests over-fetching.'
            : ''}
        </Text>
      </Stack>
    </div>
  );
}
