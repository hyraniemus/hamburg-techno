'use client';

import { Event } from '@/types';
import EventCard from './EventCard';
import { useSearchParams } from 'next/navigation';

export default function EventGrid({ events }: { events: Event[] }) {
  const searchParams = useSearchParams();
  const category = searchParams.get('category');

  const filteredEvents = category
    ? events.filter(event => event.category === category)
    : events;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
      {filteredEvents.map((event) => (
        <EventCard key={event.id} event={event} />
      ))}
    </div>
  );
}
