'use client';

import { Event } from '@/types';
import EventCard from './EventCard';

interface EventGridProps {
  events: Event[];
}

export default function EventGrid({ events }: EventGridProps) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 p-6">
      {events.map((event) => (
        <EventCard key={event.id} event={event} />
      ))}
    </div>
  );
}
