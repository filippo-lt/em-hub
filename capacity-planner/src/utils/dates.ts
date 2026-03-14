import { TOTAL_DAYS, DAYS_BEFORE_TODAY } from '../types';

export function dateToDay(date: Date): number {
  return Math.floor(Date.UTC(
    date.getFullYear(),
    date.getMonth(),
    date.getDate()
  ) / 86400000);
}

export function dayToDate(day: number): Date {
  return new Date(day * 86400000);
}

export function getTodayDay(): number {
  return dateToDay(new Date());
}

export function getTimelineStart(): number {
  return getTodayDay() - DAYS_BEFORE_TODAY;
}

export function getTimelineEnd(): number {
  return getTimelineStart() + TOTAL_DAYS;
}

export function isWeekend(day: number): boolean {
  const date = dayToDate(day);
  const dayOfWeek = date.getUTCDay();
  return dayOfWeek === 0 || dayOfWeek === 6;
}

export function getMonthLabel(day: number): string {
  const date = dayToDate(day);
  return date.toLocaleDateString('en-US', {
    month: 'short',
    year: 'numeric',
  });
}

export function getDayOfMonth(day: number): number {
  const date = dayToDate(day);
  return date.getUTCDate();
}

export function getDaysInMonth(day: number): number {
  const date = dayToDate(day);
  const year = date.getUTCFullYear();
  const month = date.getUTCMonth();
  return new Date(year, month + 1, 0).getDate();
}

export function formatDuration(days: number): string {
  return `${days}d`;
}

export function snapToDay(pixelDelta: number, dayWidth: number): number {
  return Math.round(pixelDelta / dayWidth);
}
