import React, { useRef } from 'react';
import type { AppState } from '../types';

interface ToolbarProps {
  isDark: boolean;
  toggleTheme: () => void;
  onAddSection: () => void;
  onAddMilestone: () => void;
  onExport: () => void;
  onImport: (data: AppState) => void;
}

export const Toolbar: React.FC<ToolbarProps> = ({
  isDark,
  toggleTheme,
  onAddSection,
  onAddMilestone,
  onExport,
  onImport,
}) => {
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleImportClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        const data = JSON.parse(event.target?.result as string);
        if (!data.sections || !Array.isArray(data.sections)) {
          throw new Error('Invalid data format: sections array required');
        }
        if (!data.milestones || !Array.isArray(data.milestones)) {
          throw new Error('Invalid data format: milestones array required');
        }
        onImport(data);
      } catch (err) {
        alert('Invalid JSON file');
      }
    };
    reader.readAsText(file);

    // Reset input
    e.target.value = '';
  };

  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '12px 16px',
        backgroundColor: 'var(--bg-secondary)',
        borderBottom: '1px solid var(--border-color)',
        height: '56px',
        boxSizing: 'border-box',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        <h1
          style={{
            margin: 0,
            fontSize: '18px',
            fontWeight: 600,
            color: 'var(--text-primary)',
          }}
        >
          Capacity Planner
        </h1>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <button
          onClick={onAddSection}
          style={{
            padding: '6px 12px',
            borderRadius: '6px',
            border: '1px solid var(--border-color)',
            backgroundColor: 'var(--button-bg)',
            color: 'var(--text-primary)',
            cursor: 'pointer',
            fontSize: '13px',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
          }}
        >
          <span>+</span> Section
        </button>

        <button
          onClick={onAddMilestone}
          style={{
            padding: '6px 12px',
            borderRadius: '6px',
            border: '1px solid var(--border-color)',
            backgroundColor: 'var(--button-bg)',
            color: 'var(--text-primary)',
            cursor: 'pointer',
            fontSize: '13px',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
          }}
        >
          <span>◆</span> Milestone
        </button>

        <div
          style={{
            width: '1px',
            height: '20px',
            backgroundColor: 'var(--border-color)',
            margin: '0 8px',
          }}
        />

        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
            padding: '4px 8px',
            borderRadius: '6px',
            backgroundColor: 'var(--bg-primary)',
            border: '1px solid var(--border-color)',
          }}
        >
          <span style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>Legend:</span>
          <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>○ planned</span>
          <span style={{ fontSize: '12px', color: 'var(--accent-primary)' }}>◉ running</span>
          <span style={{ fontSize: '12px', color: 'var(--success-color)' }}>✓ completed</span>
        </div>

        <div
          style={{
            width: '1px',
            height: '20px',
            backgroundColor: 'var(--border-color)',
            margin: '0 8px',
          }}
        />

        <button
          onClick={onExport}
          style={{
            padding: '6px 12px',
            borderRadius: '6px',
            border: '1px solid var(--border-color)',
            backgroundColor: 'var(--button-bg)',
            color: 'var(--text-primary)',
            cursor: 'pointer',
            fontSize: '13px',
          }}
        >
          ↓ Export
        </button>

        <button
          onClick={handleImportClick}
          style={{
            padding: '6px 12px',
            borderRadius: '6px',
            border: '1px solid var(--border-color)',
            backgroundColor: 'var(--button-bg)',
            color: 'var(--text-primary)',
            cursor: 'pointer',
            fontSize: '13px',
          }}
        >
          ↑ Import
        </button>

        <input
          ref={fileInputRef}
          type="file"
          accept=".json"
          onChange={handleFileChange}
          style={{ display: 'none' }}
        />

        <div
          style={{
            width: '1px',
            height: '20px',
            backgroundColor: 'var(--border-color)',
            margin: '0 8px',
          }}
        />

        <button
          onClick={toggleTheme}
          style={{
            padding: '6px 10px',
            borderRadius: '6px',
            border: '1px solid var(--border-color)',
            backgroundColor: 'var(--button-bg)',
            color: 'var(--text-primary)',
            cursor: 'pointer',
            fontSize: '14px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
          title={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
        >
          {isDark ? '☀️' : '🌙'}
        </button>
      </div>
    </div>
  );
};
