export type ItemState = 'planned' | 'running' | 'completed';

export interface Item {
  id: string;
  name: string;
  startDay: number;
  endDay: number;
  color: string;
  state: ItemState;
}

export interface Section {
  id: string;
  name: string;
  collapsed: boolean;
  items: Item[];
}

export interface Milestone {
  id: string;
  day: number;
  label: string;
}

export interface AppState {
  sections: Section[];
  milestones: Milestone[];
}

export interface ExportData {
  sections: Section[];
  milestones: Milestone[];
}

export type Theme = 'light' | 'dark';

export const DEFAULT_PALETTE = [
  '#5B8EF7',
  '#F7724F',
  '#4FD6A6',
  '#B47BFA',
  '#F7C34F',
  '#4FC9F7',
  '#F74F8E',
  '#8CF74F',
  '#FA9E4F',
  '#4FF7D6',
];

export const DAY_WIDTH = 34;
export const TOTAL_DAYS = 300;
export const DAYS_BEFORE_TODAY = 30;
export const HEADER_HEIGHT = 60;
export const ROW_HEIGHT = 40;
export const SECTION_HEADER_HEIGHT = 44;
