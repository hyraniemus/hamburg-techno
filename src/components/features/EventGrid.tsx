'use client';

import { Event } from '@/types';
import EventCard from './EventCard';
import { useSearchParams } from 'next/navigation';

interface EventGridProps {
  events: Event[];
}

export default function EventGrid({ events }: EventGridProps) {
  const searchParams = useSearchParams();
  const category = searchParams.get('category');

  const filteredEvents = category
    ? events.filter(event => event.category === category)
    : events;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 p-6">
      {filteredEvents.map((event) => (
        <EventCard key={event.id} event={event} />
      ))}
    </div>
  );
}
