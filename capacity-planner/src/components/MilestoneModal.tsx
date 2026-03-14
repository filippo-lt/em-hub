import React, { useState, useEffect } from 'react';
import { dateToDay, dayToDate } from '../utils/dates';

interface MilestoneModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSave: (day: number, label: string) => void;
  onDelete?: () => void;
  initialDay?: number;
  initialLabel?: string;
  isEditing?: boolean;
}

export const MilestoneModal: React.FC<MilestoneModalProps> = ({
  isOpen,
  onClose,
  onSave,
  onDelete,
  initialDay,
  initialLabel = '',
  isEditing = false,
}) => {
  const [date, setDate] = useState('');
  const [label, setLabel] = useState('');

  useEffect(() => {
    if (isOpen) {
      if (initialDay !== undefined) {
        const d = dayToDate(initialDay);
        setDate(d.toISOString().split('T')[0]);
      } else {
        setDate(new Date().toISOString().split('T')[0]);
      }
      setLabel(initialLabel);
    }
  }, [isOpen, initialDay, initialLabel]);

  const handleSave = () => {
    if (!date || !label.trim()) return;
    const day = dateToDay(new Date(date));
    onSave(day, label.trim());
    onClose();
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSave();
    } else if (e.key === 'Escape') {
      onClose();
    }
  };

  if (!isOpen) return null;

  return (
    <div
      onClick={onClose}
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'var(--modal-overlay)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 1000,
      }}
    >
      <div
        onClick={(e) => e.stopPropagation()}
        style={{
          backgroundColor: 'var(--bg-primary)',
          borderRadius: '8px',
          padding: '24px',
          minWidth: '320px',
          boxShadow: 'var(--shadow-md)',
        }}
      >
        <h2
          style={{
            margin: '0 0 16px 0',
            fontSize: '18px',
            color: 'var(--text-primary)',
          }}
        >
          {isEditing ? 'Edit Milestone' : 'Add Milestone'}
        </h2>

        <div style={{ marginBottom: '16px' }}>
          <label
            style={{
              display: 'block',
              marginBottom: '4px',
              fontSize: '13px',
              color: 'var(--text-secondary)',
            }}
          >
            Date
          </label>
          <input
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            onKeyDown={handleKeyDown}
            style={{
              width: '100%',
              padding: '8px 12px',
              borderRadius: '6px',
              border: '1px solid var(--border-color)',
              backgroundColor: 'var(--bg-secondary)',
              color: 'var(--text-primary)',
              fontSize: '14px',
              boxSizing: 'border-box',
            }}
          />
        </div>

        <div style={{ marginBottom: '24px' }}>
          <label
            style={{
              display: 'block',
              marginBottom: '4px',
              fontSize: '13px',
              color: 'var(--text-secondary)',
            }}
          >
            Label
          </label>
          <input
            type="text"
            value={label}
            onChange={(e) => setLabel(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Milestone name"
            autoFocus
            style={{
              width: '100%',
              padding: '8px 12px',
              borderRadius: '6px',
              border: '1px solid var(--border-color)',
              backgroundColor: 'var(--bg-secondary)',
              color: 'var(--text-primary)',
              fontSize: '14px',
              boxSizing: 'border-box',
            }}
          />
        </div>

        <div style={{ display: 'flex', gap: '8px', justifyContent: 'flex-end' }}>
          {isEditing && onDelete && (
            <button
              onClick={onDelete}
              style={{
                padding: '8px 16px',
                borderRadius: '6px',
                border: 'none',
                backgroundColor: 'var(--danger-color)',
                color: 'white',
                cursor: 'pointer',
                fontSize: '14px',
                marginRight: 'auto',
              }}
            >
              Delete
            </button>
          )}

          <button
            onClick={onClose}
            style={{
              padding: '8px 16px',
              borderRadius: '6px',
              border: '1px solid var(--border-color)',
              backgroundColor: 'var(--button-bg)',
              color: 'var(--text-primary)',
              cursor: 'pointer',
              fontSize: '14px',
            }}
          >
            Cancel
          </button>

          <button
            onClick={handleSave}
            disabled={!date || !label.trim()}
            style={{
              padding: '8px 16px',
              borderRadius: '6px',
              border: 'none',
              backgroundColor: 'var(--accent-primary)',
              color: 'white',
              cursor: !date || !label.trim() ? 'not-allowed' : 'pointer',
              fontSize: '14px',
              opacity: !date || !label.trim() ? 0.5 : 1,
            }}
          >
            {isEditing ? 'Save' : 'Add Milestone'}
          </button>
        </div>
      </div>
    </div>
  );
};
