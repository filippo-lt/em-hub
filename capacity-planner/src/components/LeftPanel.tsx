import React, { forwardRef } from 'react';
import type { Section, Item, ItemState } from '../types';
import { SECTION_HEADER_HEIGHT, ROW_HEIGHT } from '../types';
import { getStateColor } from '../utils/colors';

interface LeftPanelProps {
  sections: Section[];
  dispatch: React.Dispatch<any>;
  onScroll?: React.UIEventHandler<HTMLDivElement>;
}

interface InlineEditProps {
  value: string;
  onSave: (value: string) => void;
  onCancel: () => void;
}

const InlineEdit: React.FC<InlineEditProps> = ({ value, onSave, onCancel }) => {
  const [editValue, setEditValue] = React.useState(value);
  const inputRef = React.useRef<HTMLInputElement>(null);

  React.useEffect(() => {
    inputRef.current?.focus();
    inputRef.current?.select();
  }, []);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      onSave(editValue);
    } else if (e.key === 'Escape') {
      onCancel();
    }
  };

  const handleBlur = () => {
    onSave(editValue);
  };

  return (
    <input
      ref={inputRef}
      type="text"
      value={editValue}
      onChange={(e) => setEditValue(e.target.value)}
      onKeyDown={handleKeyDown}
      onBlur={handleBlur}
      style={{
        width: '100%',
        padding: '2px 4px',
        borderRadius: '3px',
        border: '1px solid var(--accent-primary)',
        backgroundColor: 'var(--bg-primary)',
        color: 'var(--text-primary)',
        fontSize: '13px',
        boxSizing: 'border-box',
      }}
    />
  );
};

interface SectionRowProps {
  section: Section;
  dispatch: React.Dispatch<any>;
}

const SectionRow: React.FC<SectionRowProps> = ({ section, dispatch }) => {
  const [isEditing, setIsEditing] = React.useState(false);

  return (
    <div
      style={{
        height: SECTION_HEADER_HEIGHT,
        display: 'flex',
        alignItems: 'center',
        padding: '0 12px',
        backgroundColor: 'var(--bg-secondary)',
        borderBottom: '1px solid var(--border-color)',
        boxSizing: 'border-box',
      }}
    >
      <button
        onClick={() => dispatch({ type: 'TOGGLE_SECTION_COLLAPSE', payload: section.id })}
        style={{
          width: '20px',
          height: '20px',
          border: 'none',
          backgroundColor: 'transparent',
          cursor: 'pointer',
          fontSize: '12px',
          color: 'var(--text-secondary)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: 0,
        }}
      >
        {section.collapsed ? '▶' : '▼'}
      </button>

      <div
        style={{
          flex: 1,
          marginLeft: '8px',
          fontWeight: 600,
          fontSize: '14px',
          color: 'var(--text-primary)',
        }}
        onDoubleClick={() => setIsEditing(true)}
      >
        {isEditing ? (
          <InlineEdit
            value={section.name}
            onSave={(value) => {
              dispatch({ type: 'RENAME_SECTION', payload: { id: section.id, name: value } });
              setIsEditing(false);
            }}
            onCancel={() => setIsEditing(false)}
          />
        ) : (
          section.name
        )}
      </div>

      <div style={{ display: 'flex', gap: '2px' }}>
        <button
          onClick={() => dispatch({ type: 'ADD_ITEM', payload: section.id })}
          style={{
            width: '22px',
            height: '22px',
            border: 'none',
            backgroundColor: 'transparent',
            cursor: 'pointer',
            fontSize: '13px',
            color: 'var(--accent-primary)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: 0,
            borderRadius: '3px',
          }}
          title="Add item"
        >
          +
        </button>
        <button
          onClick={() => dispatch({ type: 'MOVE_SECTION_UP', payload: section.id })}
          style={{
            width: '22px',
            height: '22px',
            border: 'none',
            backgroundColor: 'transparent',
            cursor: 'pointer',
            fontSize: '11px',
            color: 'var(--text-muted)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: 0,
            borderRadius: '3px',
          }}
          title="Move up"
        >
          ↑
        </button>
        <button
          onClick={() => dispatch({ type: 'MOVE_SECTION_DOWN', payload: section.id })}
          style={{
            width: '22px',
            height: '22px',
            border: 'none',
            backgroundColor: 'transparent',
            cursor: 'pointer',
            fontSize: '11px',
            color: 'var(--text-muted)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: 0,
            borderRadius: '3px',
          }}
          title="Move down"
        >
          ↓
        </button>
        <button
          onClick={() => dispatch({ type: 'DELETE_SECTION', payload: section.id })}
          style={{
            width: '22px',
            height: '22px',
            border: 'none',
            backgroundColor: 'transparent',
            cursor: 'pointer',
            fontSize: '13px',
            color: 'var(--danger-color)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: 0,
            borderRadius: '3px',
          }}
          title="Delete section"
        >
          ×
        </button>
      </div>
    </div>
  );
};

interface ItemRowProps {
  item: Item;
  sectionId: string;
  dispatch: React.Dispatch<any>;
}

const getStateIcon = (state: ItemState): string => {
  switch (state) {
    case 'planned':
      return '○';
    case 'running':
      return '◉';
    case 'completed':
      return '✓';
  }
};

const ItemRow: React.FC<ItemRowProps> = ({ item, sectionId, dispatch }) => {
  const [isEditing, setIsEditing] = React.useState(false);
  const displayColor = getStateColor(item.color, item.state);

  return (
    <div
      style={{
        height: ROW_HEIGHT,
        display: 'flex',
        alignItems: 'center',
        padding: '0 12px',
        backgroundColor: 'var(--bg-primary)',
        borderBottom: '1px solid var(--border-color)',
        boxSizing: 'border-box',
      }}
    >
      <div
        style={{
          width: '10px',
          height: '10px',
          borderRadius: '50%',
          backgroundColor: displayColor,
          marginRight: '8px',
          flexShrink: 0,
        }}
      />

      <div
        style={{
          flex: 1,
          fontSize: '13px',
          color: 'var(--text-primary)',
          overflow: 'hidden',
          textOverflow: 'ellipsis',
          whiteSpace: 'nowrap',
        }}
        onDoubleClick={() => setIsEditing(true)}
      >
        {isEditing ? (
          <InlineEdit
            value={item.name}
            onSave={(value) => {
              dispatch({
                type: 'RENAME_ITEM',
                payload: { sectionId, itemId: item.id, name: value },
              });
              setIsEditing(false);
            }}
            onCancel={() => setIsEditing(false)}
          />
        ) : (
          item.name
        )}
      </div>

      <button
        onClick={() => dispatch({ type: 'CYCLE_ITEM_STATE', payload: { sectionId, itemId: item.id } })}
        style={{
          width: '22px',
          height: '22px',
          border: 'none',
          backgroundColor: 'transparent',
          cursor: 'pointer',
          fontSize: '12px',
          color: item.state === 'running' ? 'var(--accent-primary)' : item.state === 'completed' ? 'var(--success-color)' : 'var(--text-muted)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: 0,
          borderRadius: '3px',
        }}
        title={`State: ${item.state}`}
      >
        {getStateIcon(item.state)}
      </button>

      <input
        type="color"
        value={item.color}
        onChange={(e) =>
          dispatch({
            type: 'SET_ITEM_COLOR',
            payload: { sectionId, itemId: item.id, color: e.target.value },
          })
        }
        style={{
          width: '24px',
          height: '20px',
          padding: 0,
          border: 'none',
          backgroundColor: 'transparent',
          cursor: 'pointer',
          marginLeft: '4px',
        }}
        title="Change color"
      />

      <button
        onClick={() => dispatch({ type: 'MOVE_ITEM_ITEM_UP', payload: { sectionId, itemId: item.id } })}
        style={{
          width: '20px',
          height: '20px',
          border: 'none',
          backgroundColor: 'transparent',
          cursor: 'pointer',
          fontSize: '10px',
          color: 'var(--text-muted)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: 0,
          borderRadius: '3px',
        }}
        title="Move up"
      >
        ↑
      </button>

      <button
        onClick={() => dispatch({ type: 'MOVE_ITEM_ITEM_DOWN', payload: { sectionId, itemId: item.id } })}
        style={{
          width: '20px',
          height: '20px',
          border: 'none',
          backgroundColor: 'transparent',
          cursor: 'pointer',
          fontSize: '10px',
          color: 'var(--text-muted)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: 0,
          borderRadius: '3px',
        }}
        title="Move down"
      >
        ↓
      </button>

      <button
        onClick={() => dispatch({ type: 'DELETE_ITEM', payload: { sectionId, itemId: item.id } })}
        style={{
          width: '20px',
          height: '20px',
          border: 'none',
          backgroundColor: 'transparent',
          cursor: 'pointer',
          fontSize: '14px',
          color: 'var(--danger-color)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: 0,
          borderRadius: '3px',
        }}
        title="Delete item"
      >
        ×
      </button>
    </div>
  );
};

export const LeftPanel = forwardRef<HTMLDivElement, LeftPanelProps>(
  ({ sections, dispatch, onScroll }, ref) => {
    return (
      <div
        ref={ref}
        onScroll={onScroll}
        style={{
          width: '280px',
          minWidth: '280px',
          backgroundColor: 'var(--bg-primary)',
          borderRight: '1px solid var(--border-color)',
          overflowY: 'auto',
          overflowX: 'hidden',
        }}
      >
        {/* Header */}
        <div
          style={{
            height: '60px',
            display: 'flex',
            alignItems: 'center',
            padding: '0 12px',
            backgroundColor: 'var(--bg-secondary)',
            borderBottom: '1px solid var(--border-color)',
            fontWeight: 600,
            fontSize: '13px',
            color: 'var(--text-secondary)',
            boxSizing: 'border-box',
            position: 'sticky',
            top: 0,
            zIndex: 10,
          }}
        >
          TEAM / TASKS
        </div>

        {/* Content */}
        <div>
          {sections.map((section) => (
            <React.Fragment key={section.id}>
              <SectionRow section={section} dispatch={dispatch} />
              {!section.collapsed &&
                section.items.map((item) => (
                  <ItemRow
                    key={item.id}
                    item={item}
                    sectionId={section.id}
                    dispatch={dispatch}
                  />
                ))}
            </React.Fragment>
          ))}
        </div>
      </div>
    );
  }
);

LeftPanel.displayName = 'LeftPanel';
