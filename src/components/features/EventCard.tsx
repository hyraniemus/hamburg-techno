'use client';

import { Event } from '@/types';
import { Calendar, MapPin, Star } from 'lucide-react';
import Image from 'next/image';

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
      <div className="relative h-40 sm:h-48 overflow-hidden group">
        <Image
          src={event.imageUrl}
          alt={event.title}
          width={400}
          height={300}
          className="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700"
          priority
        />
        <div className="absolute inset-0 bg-black/30 group-hover:bg-black/20 transition-all duration-700" />
        <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent h-24" />
        {event.dj && (
          <div className="absolute top-2 right-2 bg-black/80 px-2 sm:px-3 py-1 rounded-full flex items-center">
            <Star className="w-3 h-3 sm:w-4 sm:h-4 mr-1 sm:mr-2 text-yellow-400" />
            <span className="text-yellow-400 font-semibold text-sm sm:text-base">{event.dj}</span>
          </div>
        )}
      </div>
      <div className="p-3 sm:p-4">
        <h3 className="text-lg sm:text-xl font-bold mb-2 text-white">{event.title}</h3>
        <div className="flex items-center mb-2 text-gray-300 text-sm sm:text-base">
          <Calendar className="w-4 h-4 mr-2" />
          <span>{dateFormatter.format(event.date)}</span>
        </div>
        <div className="flex items-center text-gray-300 text-sm sm:text-base">
          <MapPin className="w-4 h-4 mr-2" />
          <span>{event.location}</span>
        </div>
        {event.description && (
          <p className="mt-2 text-xs sm:text-sm text-gray-400">{event.description}</p>
        )}
      </div>
    </div>
  );
}
