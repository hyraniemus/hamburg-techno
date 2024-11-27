'use client';

import { Calendar, MapPin } from 'lucide-react';
import { Event } from '@/types';

interface EventCardProps {
  event: Event;
}

export default function EventCard({ event }: EventCardProps) {
  const dateFormatter = new Intl.DateTimeFormat('de-DE', {
    weekday: 'long',
    month: 'long',
    day: 'numeric',
  });

  return (
    <div className={`rounded-lg overflow-hidden shadow-lg bg-opacity-80 bg-black hover:bg-opacity-90 transition-all border-l-4 border-${event.venueType}`}>
      <div className="relative h-48 overflow-hidden">
        <iframe
          className="w-full h-full scale-150"
          src="https://www.youtube.com/embed/ltnIwB6NDlU?autoplay=1&mute=1&loop=1&playlist=ltnIwB6NDlU&controls=0&showinfo=0&rel=0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
          style={{
            pointerEvents: 'none',
          }}
        />
        <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent h-24" />
      </div>
      <div className="p-4">
        <h3 className="text-xl font-bold mb-2 text-white">{event.title}</h3>
        <div className="flex items-center mb-2 text-gray-300">
          <Calendar className="w-4 h-4 mr-2" />
          <span>{dateFormatter.format(event.date)}</span>
        </div>
        <div className="flex items-center text-gray-300">
          <MapPin className="w-4 h-4 mr-2" />
          <span>{event.location}</span>
        </div>
        {event.description && (
          <p className="mt-2 text-sm text-gray-400">{event.description}</p>
        )}
      </div>
    </div>
  );
}
