import React, { useReducer, useRef, useCallback, useEffect, useState } from 'react';
import { reducer, createInitialState } from '../state/store';
import { useTheme } from '../hooks/useTheme';
import { Toolbar } from './Toolbar';
import { LeftPanel } from './LeftPanel';
import { RightPanel } from './RightPanel';
import { MilestoneModal } from './MilestoneModal';
import type { AppState, Milestone } from '../types';
import { DAY_WIDTH } from '../types';
import { getTodayDay, getTimelineStart } from '../utils/dates';

export const App: React.FC = () => {
  const [state, dispatch] = useReducer(reducer, createInitialState());
  const { isDark, toggleTheme } = useTheme();

  const leftPanelRef = useRef<HTMLDivElement>(null);
  const rightPanelRef = useRef<HTMLDivElement>(null);
  const isSyncing = useRef(false);

  // Scroll sync
  const handleLeftScroll = useCallback(() => {
    if (isSyncing.current || !leftPanelRef.current || !rightPanelRef.current) return;
    isSyncing.current = true;
    requestAnimationFrame(() => {
      rightPanelRef.current!.scrollTop = leftPanelRef.current!.scrollTop;
      isSyncing.current = false;
    });
  }, []);

  const handleRightScroll = useCallback(() => {
    if (isSyncing.current || !leftPanelRef.current || !rightPanelRef.current) return;
    isSyncing.current = true;
    requestAnimationFrame(() => {
      leftPanelRef.current!.scrollTop = rightPanelRef.current!.scrollTop;
      isSyncing.current = false;
    });
  }, []);

  // Center on today on mount
  useEffect(() => {
    const rightPanel = rightPanelRef.current;
    if (!rightPanel) return;

    const timelineStart = getTimelineStart();
    const todayDay = getTodayDay();
    const todayOffset = (todayDay - timelineStart) * DAY_WIDTH;
    const containerWidth = rightPanel.clientWidth;

    // Center today in the viewport
    rightPanel.scrollLeft = todayOffset - containerWidth / 2 + DAY_WIDTH / 2;
  }, []);

  // Milestone modal state
  const [milestoneModalOpen, setMilestoneModalOpen] = useState(false);
  const [editingMilestone, setEditingMilestone] = useState<Milestone | null>(null);

  const handleAddMilestone = () => {
    setEditingMilestone(null);
    setMilestoneModalOpen(true);
  };

  const handleEditMilestone = (milestone: Milestone) => {
    setEditingMilestone(milestone);
    setMilestoneModalOpen(true);
  };

  const handleSaveMilestone = (day: number, label: string) => {
    if (editingMilestone) {
      dispatch({
        type: 'UPDATE_MILESTONE',
        payload: { id: editingMilestone.id, day, label },
      });
    } else {
      dispatch({
        type: 'ADD_MILESTONE',
        payload: { day, label },
      });
    }
  };

  const handleDeleteMilestone = () => {
    if (editingMilestone) {
      dispatch({ type: 'DELETE_MILESTONE', payload: editingMilestone.id });
      setMilestoneModalOpen(false);
      setEditingMilestone(null);
    }
  };

  // Export
  const handleExport = () => {
    const data: AppState = {
      sections: state.sections,
      milestones: state.milestones,
    };
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'capacity-plan.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  // Import
  const handleImport = (data: AppState) => {
    dispatch({ type: 'IMPORT_DATA', payload: data });
  };

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        height: '100vh',
        overflow: 'hidden',
        fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        backgroundColor: 'var(--bg-primary)',
        color: 'var(--text-primary)',
      }}
    >
      <Toolbar
        isDark={isDark}
        toggleTheme={toggleTheme}
        onAddSection={() => dispatch({ type: 'ADD_SECTION' })}
        onAddMilestone={handleAddMilestone}
        onExport={handleExport}
        onImport={handleImport}
      />

      <div style={{ display: 'flex', flex: 1, overflow: 'hidden' }}>
        <LeftPanel
          ref={leftPanelRef}
          onScroll={handleLeftScroll}
          sections={state.sections}
          dispatch={dispatch}
        />
        <RightPanel
          ref={rightPanelRef}
          onScroll={handleRightScroll}
          sections={state.sections}
          milestones={state.milestones}
          dispatch={dispatch}
          onMilestoneClick={handleEditMilestone}
        />
      </div>

      <MilestoneModal
        isOpen={milestoneModalOpen}
        onClose={() => {
          setMilestoneModalOpen(false);
          setEditingMilestone(null);
        }}
        onSave={handleSaveMilestone}
        onDelete={editingMilestone ? handleDeleteMilestone : undefined}
        initialDay={editingMilestone?.day}
        initialLabel={editingMilestone?.label}
        isEditing={!!editingMilestone}
      />
    </div>
  );
};
