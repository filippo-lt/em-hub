import type { ItemState } from '../types';

export interface HSL {
  h: number;
  s: number;
  l: number;
}

export function hexToHsl(hex: string): HSL {
  let r = 0;
  let g = 0;
  let b = 0;

  if (hex.length === 4) {
    r = parseInt('0x' + hex[1] + hex[1], 16);
    g = parseInt('0x' + hex[2] + hex[2], 16);
    b = parseInt('0x' + hex[3] + hex[3], 16);
  } else if (hex.length === 7) {
    r = parseInt('0x' + hex[1] + hex[2], 16);
    g = parseInt('0x' + hex[3] + hex[4], 16);
    b = parseInt('0x' + hex[5] + hex[6], 16);
  }

  r /= 255;
  g /= 255;
  b /= 255;

  const max = Math.max(r, g, b);
  const min = Math.min(r, g, b);
  let h = 0;
  let s = 0;
  const l = (max + min) / 2;

  if (max !== min) {
    const d = max - min;
    s = l > 0.5 ? d / (2 - max - min) : d / (max + min);

    switch (max) {
      case r:
        h = (g - b) / d + (g < b ? 6 : 0);
        break;
      case g:
        h = (b - r) / d + 2;
        break;
      case b:
        h = (r - g) / d + 4;
        break;
    }
    h /= 6;
  }

  return {
    h: h * 360,
    s: s * 100,
    l: l * 100,
  };
}

export function hslToHex({ h, s, l }: HSL): string {
  s /= 100;
  l /= 100;

  const c = (1 - Math.abs(2 * l - 1)) * s;
  const x = c * (1 - Math.abs(((h / 60) % 2) - 1));
  const m = l - c / 2;

  let r = 0;
  let g = 0;
  let b = 0;

  if (h >= 0 && h < 60) {
    r = c;
    g = x;
  } else if (h >= 60 && h < 120) {
    r = x;
    g = c;
  } else if (h >= 120 && h < 180) {
    g = c;
    b = x;
  } else if (h >= 180 && h < 240) {
    g = x;
    b = c;
  } else if (h >= 240 && h < 300) {
    r = x;
    b = c;
  } else if (h >= 300 && h < 360) {
    r = c;
    b = x;
  }

  r = Math.round((r + m) * 255);
  g = Math.round((g + m) * 255);
  b = Math.round((b + m) * 255);

  const toHex = (n: number) => n.toString(16).padStart(2, '0');
  return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
}

export function getStateColor(baseColor: string, state: ItemState): string {
  const hsl = hexToHsl(baseColor);

  switch (state) {
    case 'planned':
      return hslToHex({
        h: hsl.h,
        s: hsl.s * 0.28,
        l: Math.min(hsl.l * 1.22, 88),
      });
    case 'completed':
      return hslToHex({
        h: hsl.h,
        s: hsl.s * 0.55,
        l: hsl.l * 0.62,
      });
    case 'running':
    default:
      return baseColor;
  }
}

export function getNextColorIndex(currentIndex: number, paletteLength: number): number {
  return (currentIndex + 1) % paletteLength;
}
