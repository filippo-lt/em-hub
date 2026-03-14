import React, { forwardRef, useRef, useEffect } from 'react';
import type { Section, Item, Milestone } from '../types';
import { DAY_WIDTH, TOTAL_DAYS, ROW_HEIGHT, SECTION_HEADER_HEIGHT } from '../types';
import { getTimelineStart, getTodayDay, isWeekend, getMonthLabel, getDayOfMonth, formatDuration } from '../utils/dates';
import { getStateColor } from '../utils/colors';
import { snapToDay } from '../utils/dates';

interface RightPanelProps {
  sections: Section[];
  milestones: Milestone[];
  dispatch: React.Dispatch<any>;
  onMilestoneClick: (milestone: Milestone) => void;
  onScroll?: React.UIEventHandler<HTMLDivElement>;
}

interface ItemBarProps {
  item: Item;
  sectionId: string;
  timelineStart: number;
  dispatch: React.Dispatch<any>;
}

const ItemBar: React.FC<ItemBarProps> = ({ item, sectionId, timelineStart, dispatch }) => {
  const barRef = useRef<HTMLDivElement>(null);
  const [isDragging, setIsDragging] = React.useState(false);
  const [isResizingLeft, setIsResizingLeft] = React.useState(false);
  const [isResizingRight, setIsResizingRight] = React.useState(false);
  const dragStartX = useRef(0);
  const originalStartDay = useRef(item.startDay);
  const originalEndDay = useRef(item.endDay);

  const startOffset = item.startDay - timelineStart;
  const duration = item.endDay - item.startDay;

  const displayColor = getStateColor(item.color, item.state);

  const handleMouseDown = (e: React.MouseEvent, mode: 'move' | 'resize-left' | 'resize-right') => {
    e.stopPropagation();
    dragStartX.current = e.clientX;
    originalStartDay.current = item.startDay;
    originalEndDay.current = item.endDay;

    if (mode === 'move') {
      setIsDragging(true);
    } else if (mode === 'resize-left') {
      setIsResizingLeft(true);
    } else if (mode === 'resize-right') {
      setIsResizingRight(true);
    }
  };

  useEffect(() => {
    if (!isDragging && !isResizingLeft && !isResizingRight) return;

    const handleMouseMove = (e: MouseEvent) => {
      const deltaX = e.clientX - dragStartX.current;
      const dayDelta = snapToDay(deltaX, DAY_WIDTH);

      if (isDragging) {
        const newStartDay = originalStartDay.current + dayDelta;
        const newEndDay = originalEndDay.current + dayDelta;

        dispatch({
          type: 'UPDATE_ITEM_DATES',
          payload: {
            sectionId,
            itemId: item.id,
            startDay: newStartDay,
            endDay: newEndDay,
          },
        });
      } else if (isResizingLeft) {
        const newStartDay = originalStartDay.current + dayDelta;
        // Ensure minimum 1 day duration
        if (newStartDay < originalEndDay.current - 1) {
          dispatch({
            type: 'UPDATE_ITEM_DATES',
            payload: {
              sectionId,
              itemId: item.id,
              startDay: newStartDay,
              endDay: originalEndDay.current,
            },
          });
        }
      } else if (isResizingRight) {
        const newEndDay = originalEndDay.current + dayDelta;
        // Ensure minimum 1 day duration
        if (newEndDay > originalStartDay.current + 1) {
          dispatch({
            type: 'UPDATE_ITEM_DATES',
            payload: {
              sectionId,
              itemId: item.id,
              startDay: originalStartDay.current,
              endDay: newEndDay,
            },
          });
        }
      }
    };

    const handleMouseUp = () => {
      setIsDragging(false);
      setIsResizingLeft(false);
      setIsResizingRight(false);
    };

    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, [isDragging, isResizingLeft, isResizingRight, dispatch, sectionId, item.id]);

  const barWidth = duration * DAY_WIDTH;
  const showDuration = barWidth > 60;
  const showName = barWidth > 80;

  return (
    <div
      ref={barRef}
      onMouseDown={(e) => handleMouseDown(e, 'move')}
      style={{
        position: 'absolute',
        left: startOffset * DAY_WIDTH,
        width: barWidth,
        height: '28px',
        backgroundColor: displayColor,
        borderRadius: '4px',
        display: 'flex',
        alignItems: 'center',
        padding: '0 8px',
        boxSizing: 'border-box',
        cursor: isDragging ? 'grabbing' : 'grab',
        userSelect: 'none',
        overflow: 'hidden',
      }}
    >
      {/* Resize handle - left */}
      <div
        onMouseDown={(e) => handleMouseDown(e, 'resize-left')}
        style={{
          position: 'absolute',
          left: 0,
          top: 0,
          width: '5px',
          height: '100%',
          cursor: 'col-resize',
          backgroundColor: 'rgba(0,0,0,0.2)',
        }}
      />

      {/* Content */}
      <span
        style={{
          fontSize: '12px',
          color: 'white',
          fontWeight: 500,
          overflow: 'hidden',
          textOverflow: 'ellipsis',
          whiteSpace: 'nowrap',
          flex: 1,
          textShadow: '0 1px 2px rgba(0,0,0,0.3)',
          display: showName ? 'block' : 'none',
        }}
      >
        {item.name}
      </span>

      {showDuration && (
        <span
          style={{
            fontSize: '11px',
            color: 'rgba(255,255,255,0.9)',
            marginLeft: '4px',
            textShadow: '0 1px 2px rgba(0,0,0,0.3)',
          }}
        >
          {formatDuration(duration)}
        </span>
      )}

      {/* Resize handle - right */}
      <div
        onMouseDown={(e) => handleMouseDown(e, 'resize-right')}
        style={{
          position: 'absolute',
          right: 0,
          top: 0,
          width: '5px',
          height: '100%',
          cursor: 'col-resize',
          backgroundColor: 'rgba(0,0,0,0.2)',
        }}
      />
    </div>
  );
};

interface MilestoneMarkerProps {
  milestone: Milestone;
  timelineStart: number;
  onClick: () => void;
}

const MilestoneMarker: React.FC<MilestoneMarkerProps> = ({ milestone, timelineStart, onClick }) => {
  const offset = milestone.day - timelineStart;

  return (
    <div
      onClick={onClick}
      style={{
        position: 'absolute',
        left: offset * DAY_WIDTH + DAY_WIDTH / 2,
        top: 0,
        bottom: 0,
        width: '2px',
        backgroundColor: 'var(--milestone-line)',
        cursor: 'pointer',
        zIndex: 5,
      }}
    >
      <div
        style={{
          position: 'absolute',
          top: '8px',
          left: '50%',
          transform: 'translateX(-50%)',
          backgroundColor: 'var(--milestone-bg)',
          color: 'var(--milestone-line)',
          padding: '2px 8px',
          borderRadius: '4px',
          fontSize: '11px',
          fontWeight: 600,
          whiteSpace: 'nowrap',
          border: '1px solid var(--milestone-line)',
          boxShadow: 'var(--shadow-sm)',
        }}
      >
        ◆ {milestone.label}
      </div>
    </div>
  );
};

const TodayMarker: React.FC<{ timelineStart: number }> = ({
  timelineStart,
}) => {
  const todayDay = getTodayDay();
  const offset = todayDay - timelineStart;

  return (
    <div
      style={{
        position: 'absolute',
        left: offset * DAY_WIDTH + DAY_WIDTH / 2,
        top: 0,
        bottom: 0,
        width: '2px',
        backgroundColor: 'var(--grid-line-today)',
        zIndex: 4,
        pointerEvents: 'none',
      }}
    >
      <div
        style={{
          position: 'absolute',
          top: '8px',
          left: '50%',
          transform: 'translateX(-50%)',
          backgroundColor: 'var(--accent-primary)',
          color: 'white',
          padding: '2px 8px',
          borderRadius: '4px',
          fontSize: '10px',
          fontWeight: 700,
          textTransform: 'uppercase',
          letterSpacing: '0.5px',
        }}
      >
        TODAY
      </div>
    </div>
  );
};

export const RightPanel = forwardRef<HTMLDivElement, RightPanelProps>(
  ({ sections, milestones, dispatch, onMilestoneClick, onScroll }, ref) => {
    const timelineStart = getTimelineStart();
    const todayDay = getTodayDay();

    // Calculate total height
    let calculatedHeight = 0;
    sections.forEach((section) => {
      calculatedHeight += SECTION_HEADER_HEIGHT;
      if (!section.collapsed) {
        calculatedHeight += section.items.length * ROW_HEIGHT;
      }
    });
    // Ensure minimum height
    const totalHeight = Math.max(calculatedHeight, 200);

    // Generate timeline data
    const days: { day: number; isWeekend: boolean; isToday: boolean }[] = [];
    for (let i = 0; i < TOTAL_DAYS; i++) {
      const day = timelineStart + i;
      days.push({
        day,
        isWeekend: isWeekend(day),
        isToday: day === todayDay,
      });
    }

    // Group days by month for header
    const months: { label: string; startDay: number; dayCount: number }[] = [];
    let currentMonth: { label: string; startDay: number; dayCount: number } | null = null;

    days.forEach((dayInfo, index) => {
      const monthLabel = getMonthLabel(dayInfo.day);
      if (!currentMonth || currentMonth.label !== monthLabel) {
        if (currentMonth) {
          months.push(currentMonth);
        }
        currentMonth = { label: monthLabel, startDay: index, dayCount: 1 };
      } else {
        currentMonth.dayCount++;
      }
    });
    if (currentMonth) {
      months.push(currentMonth);
    }

    return (
      <div
        ref={ref}
        onScroll={onScroll}
        style={{
          flex: 1,
          backgroundColor: 'var(--bg-primary)',
          overflow: 'auto',
          position: 'relative',
        }}
      >
        <div style={{ minWidth: TOTAL_DAYS * DAY_WIDTH, position: 'relative' }}>
          {/* Sticky Header */}
          <div
            style={{
              position: 'sticky',
              top: 0,
              zIndex: 20,
              backgroundColor: 'var(--bg-secondary)',
            }}
          >
            {/* Month Row */}
            <div style={{ display: 'flex', height: '30px', borderBottom: '1px solid var(--border-color)' }}>
              {months.map((month, index) => (
                <div
                  key={index}
                  style={{
                    width: month.dayCount * DAY_WIDTH,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    borderRight: '1px solid var(--border-color)',
                    fontSize: '12px',
                    fontWeight: 600,
                    color: 'var(--text-secondary)',
                    boxSizing: 'border-box',
                  }}
                >
                  {month.label}
                </div>
              ))}
            </div>

            {/* Day Row */}
            <div style={{ display: 'flex', height: '30px', borderBottom: '1px solid var(--border-color)' }}>
              {days.map((dayInfo, index) => (
                <div
                  key={index}
                  style={{
                    width: DAY_WIDTH,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    borderRight: '1px solid var(--border-color)',
                    fontSize: '11px',
                    fontWeight: dayInfo.isToday ? 700 : 400,
                    color: dayInfo.isToday ? 'var(--accent-primary)' : 'var(--text-muted)',
                    backgroundColor: dayInfo.isToday ? 'var(--bg-today)' : 'transparent',
                    boxSizing: 'border-box',
                  }}
                >
                  {getDayOfMonth(dayInfo.day)}
                </div>
              ))}
            </div>
          </div>

          {/* Grid and Content */}
          <div style={{ position: 'relative', height: totalHeight || 200 }}>
            {/* Grid Lines */}
            <div style={{ display: 'flex', position: 'absolute', top: 0, left: 0, right: 0, bottom: 0 }}>
              {days.map((dayInfo, index) => (
                <div
                  key={index}
                  style={{
                    width: DAY_WIDTH,
                    borderRight: '1px solid var(--grid-line)',
                    backgroundColor: dayInfo.isWeekend ? 'var(--bg-weekend)' : 'transparent',
                    boxSizing: 'border-box',
                  }}
                />
              ))}
            </div>

            {/* Today Marker */}
            <TodayMarker timelineStart={timelineStart} />

            {/* Milestones */}
            {milestones.map((milestone) => (
              <MilestoneMarker
                key={milestone.id}
                milestone={milestone}
                timelineStart={timelineStart}
                onClick={() => onMilestoneClick(milestone)}
              />
            ))}

            {/* Section Rows */}
            <div style={{ position: 'relative' }}>
              {sections.reduce(
                (acc, section) => {
                  const { elements, offset } = acc;

                  // Section header row
                  elements.push(
                    <div
                      key={`section-${section.id}`}
                      style={{
                        height: SECTION_HEADER_HEIGHT,
                        borderBottom: '1px solid var(--border-color)',
                        boxSizing: 'border-box',
                      }}
                    />
                  );

                  if (!section.collapsed) {
                    section.items.forEach((item) => {
                      elements.push(
                        <div
                          key={`item-${item.id}`}
                          style={{
                            height: ROW_HEIGHT,
                            borderBottom: '1px solid var(--border-color)',
                            position: 'relative',
                            boxSizing: 'border-box',
                          }}
                        >
                          <ItemBar
                            item={item}
                            sectionId={section.id}
                            timelineStart={timelineStart}
                            dispatch={dispatch}
                          />
                        </div>
                      );
                    });
                  }

                  return { elements, offset: offset + (section.collapsed ? SECTION_HEADER_HEIGHT : SECTION_HEADER_HEIGHT + section.items.length * ROW_HEIGHT) };
                },
                { elements: [] as React.ReactNode[], offset: 0 }
              ).elements}
            </div>
          </div>
        </div>
      </div>
    );
  }
);

RightPanel.displayName = 'RightPanel';
