'use client';

import Image from 'next/image';
import { Calendar, Clock, MapPin } from 'lucide-react';
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
        <Image
          src={event.imageUrl || 'https://picsum.photos/400/300'}
          alt={event.title}
          fill
          className="object-cover transform hover:scale-105 transition-transform duration-300"
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
