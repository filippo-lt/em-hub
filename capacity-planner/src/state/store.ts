import type { AppState, Section, Item, Milestone, ItemState } from '../types';
import { DEFAULT_PALETTE } from '../types';
import { getTodayDay } from '../utils/dates';
import { dateToDay } from '../utils/dates';

// Generate unique IDs
function generateId(): string {
  return Math.random().toString(36).substring(2, 9);
}

// Action Types
type Action =
  | { type: 'ADD_SECTION' }
  | { type: 'DELETE_SECTION'; payload: string }
  | { type: 'RENAME_SECTION'; payload: { id: string; name: string } }
  | { type: 'TOGGLE_SECTION_COLLAPSE'; payload: string }
  | { type: 'MOVE_SECTION_UP'; payload: string }
  | { type: 'MOVE_SECTION_DOWN'; payload: string }
  | { type: 'ADD_ITEM'; payload: string }
  | { type: 'DELETE_ITEM'; payload: { sectionId: string; itemId: string } }
  | { type: 'RENAME_ITEM'; payload: { sectionId: string; itemId: string; name: string } }
  | { type: 'SET_ITEM_COLOR'; payload: { sectionId: string; itemId: string; color: string } }
  | { type: 'CYCLE_ITEM_STATE'; payload: { sectionId: string; itemId: string } }
  | { type: 'SET_ITEM_STATE'; payload: { sectionId: string; itemId: string; state: ItemState } }
  | { type: 'MOVE_ITEM_ITEM_UP'; payload: { sectionId: string; itemId: string } }
  | { type: 'MOVE_ITEM_ITEM_DOWN'; payload: { sectionId: string; itemId: string } }
  | { type: 'UPDATE_ITEM_DATES'; payload: { sectionId: string; itemId: string; startDay: number; endDay: number } }
  | { type: 'ADD_MILESTONE'; payload: { day: number; label: string } }
  | { type: 'UPDATE_MILESTONE'; payload: { id: string; day: number; label: string } }
  | { type: 'DELETE_MILESTONE'; payload: string }
  | { type: 'IMPORT_DATA'; payload: AppState }
  | { type: 'RESET_STATE' };

// Initial State
function createInitialState(): AppState {
  const today = getTodayDay();

  return {
    sections: [
      {
        id: generateId(),
        name: 'Team Alpha',
        collapsed: false,
        items: [
          {
            id: generateId(),
            name: 'Project Planning',
            startDay: today - 10,
            endDay: today + 5,
            color: DEFAULT_PALETTE[0],
            state: 'running',
          },
          {
            id: generateId(),
            name: 'Design Phase',
            startDay: today + 5,
            endDay: today + 25,
            color: DEFAULT_PALETTE[1],
            state: 'planned',
          },
        ],
      },
      {
        id: generateId(),
        name: 'Team Beta',
        collapsed: false,
        items: [
          {
            id: generateId(),
            name: 'Backend Setup',
            startDay: today - 5,
            endDay: today + 10,
            color: DEFAULT_PALETTE[2],
            state: 'running',
          },
          {
            id: generateId(),
            name: 'API Development',
            startDay: today + 10,
            endDay: today + 40,
            color: DEFAULT_PALETTE[3],
            state: 'planned',
          },
        ],
      },
    ],
    milestones: [
      {
        id: generateId(),
        day: today + 30,
        label: 'Beta Launch',
      },
    ],
  };
}

// Helper functions for state transitions
function getNextState(currentState: ItemState): ItemState {
  const states: ItemState[] = ['planned', 'running', 'completed'];
  const currentIndex = states.indexOf(currentState);
  return states[(currentIndex + 1) % states.length];
}

function getNextColor(existingColors: string[]): string {
  const usedIndices = existingColors.map(color => DEFAULT_PALETTE.indexOf(color));
  for (let i = 0; i < DEFAULT_PALETTE.length; i++) {
    if (!usedIndices.includes(i)) {
      return DEFAULT_PALETTE[i];
    }
  }
  return DEFAULT_PALETTE[0];
}

// Reducer
function reducer(state: AppState, action: Action): AppState {
  switch (action.type) {
    case 'ADD_SECTION': {
      const newSection: Section = {
        id: generateId(),
        name: 'New Section',
        collapsed: false,
        items: [],
      };
      return { ...state, sections: [...state.sections, newSection] };
    }

    case 'DELETE_SECTION': {
      return { ...state, sections: state.sections.filter(s => s.id !== action.payload) };
    }

    case 'RENAME_SECTION': {
      return {
        ...state,
        sections: state.sections.map(s =>
          s.id === action.payload.id ? { ...s, name: action.payload.name } : s
        ),
      };
    }

    case 'TOGGLE_SECTION_COLLAPSE': {
      return {
        ...state,
        sections: state.sections.map(s =>
          s.id === action.payload ? { ...s, collapsed: !s.collapsed } : s
        ),
      };
    }

    case 'MOVE_SECTION_UP': {
      const index = state.sections.findIndex(s => s.id === action.payload);
      if (index <= 0) return state;
      const sections = [...state.sections];
      [sections[index - 1], sections[index]] = [sections[index], sections[index - 1]];
      return { ...state, sections };
    }

    case 'MOVE_SECTION_DOWN': {
      const index = state.sections.findIndex(s => s.id === action.payload);
      if (index >= state.sections.length - 1) return state;
      const sections = [...state.sections];
      [sections[index], sections[index + 1]] = [sections[index + 1], sections[index]];
      return { ...state, sections };
    }

    case 'ADD_ITEM': {
      const today = getTodayDay();
      const section = state.sections.find(s => s.id === action.payload);
      const existingColors = section?.items.map(i => i.color) || [];

      const newItem: Item = {
        id: generateId(),
        name: 'New Task',
        startDay: today,
        endDay: today + 7,
        color: getNextColor(existingColors),
        state: 'planned',
      };

      return {
        ...state,
        sections: state.sections.map(s =>
          s.id === action.payload ? { ...s, items: [...s.items, newItem] } : s
        ),
      };
    }

    case 'DELETE_ITEM': {
      return {
        ...state,
        sections: state.sections.map(s =>
          s.id === action.payload.sectionId
            ? { ...s, items: s.items.filter(i => i.id !== action.payload.itemId) }
            : s
        ),
      };
    }

    case 'RENAME_ITEM': {
      return {
        ...state,
        sections: state.sections.map(s =>
          s.id === action.payload.sectionId
            ? {
                ...s,
                items: s.items.map(i =>
                  i.id === action.payload.itemId ? { ...i, name: action.payload.name } : i
                ),
              }
            : s
        ),
      };
    }

    case 'SET_ITEM_COLOR': {
      return {
        ...state,
        sections: state.sections.map(s =>
          s.id === action.payload.sectionId
            ? {
                ...s,
                items: s.items.map(i =>
                  i.id === action.payload.itemId ? { ...i, color: action.payload.color } : i
                ),
              }
            : s
        ),
      };
    }

    case 'CYCLE_ITEM_STATE': {
      return {
        ...state,
        sections: state.sections.map(s =>
          s.id === action.payload.sectionId
            ? {
                ...s,
                items: s.items.map(i =>
                  i.id === action.payload.itemId ? { ...i, state: getNextState(i.state) } : i
                ),
              }
            : s
        ),
      };
    }

    case 'SET_ITEM_STATE': {
      return {
        ...state,
        sections: state.sections.map(s =>
          s.id === action.payload.sectionId
            ? {
                ...s,
                items: s.items.map(i =>
                  i.id === action.payload.itemId ? { ...i, state: action.payload.state } : i
                ),
              }
            : s
        ),
      };
    }

    case 'MOVE_ITEM_ITEM_UP': {
      const section = state.sections.find(s => s.id === action.payload.sectionId);
      if (!section) return state;
      const itemIndex = section.items.findIndex(i => i.id === action.payload.itemId);
      if (itemIndex <= 0) return state;

      const newItems = [...section.items];
      [newItems[itemIndex - 1], newItems[itemIndex]] = [newItems[itemIndex], newItems[itemIndex - 1]];

      return {
        ...state,
        sections: state.sections.map(s =>
          s.id === action.payload.sectionId ? { ...s, items: newItems } : s
        ),
      };
    }

    case 'MOVE_ITEM_ITEM_DOWN': {
      const section = state.sections.find(s => s.id === action.payload.sectionId);
      if (!section) return state;
      const itemIndex = section.items.findIndex(i => i.id === action.payload.itemId);
      if (itemIndex >= section.items.length - 1) return state;

      const newItems = [...section.items];
      [newItems[itemIndex], newItems[itemIndex + 1]] = [newItems[itemIndex + 1], newItems[itemIndex]];

      return {
        ...state,
        sections: state.sections.map(s =>
          s.id === action.payload.sectionId ? { ...s, items: newItems } : s
        ),
      };
    }

    case 'UPDATE_ITEM_DATES': {
      return {
        ...state,
        sections: state.sections.map(s =>
          s.id === action.payload.sectionId
            ? {
                ...s,
                items: s.items.map(i =>
                  i.id === action.payload.itemId
                    ? { ...i, startDay: action.payload.startDay, endDay: action.payload.endDay }
                    : i
                ),
              }
            : s
        ),
      };
    }

    case 'ADD_MILESTONE': {
      const newMilestone: Milestone = {
        id: generateId(),
        day: action.payload.day,
        label: action.payload.label,
      };
      return { ...state, milestones: [...state.milestones, newMilestone] };
    }

    case 'UPDATE_MILESTONE': {
      return {
        ...state,
        milestones: state.milestones.map(m =>
          m.id === action.payload.id
            ? { ...m, day: action.payload.day, label: action.payload.label }
            : m
        ),
      };
    }

    case 'DELETE_MILESTONE': {
      return { ...state, milestones: state.milestones.filter(m => m.id !== action.payload) };
    }

    case 'IMPORT_DATA': {
      return action.payload;
    }

    case 'RESET_STATE': {
      return createInitialState();
    }

    default:
      return state;
  }
}

// Export everything needed
export { reducer, createInitialState, generateId, getNextState, getNextColor, dateToDay };
export type { Action };
