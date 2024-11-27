'use client';

import Image from 'next/image';
import { Calendar, Clock, MapPin } from 'lucide-react';
import { Event } from '@/types';

interface EventCardProps {
  event: Event;
}

export default function EventCard({ event }: EventCardProps) {
  const formatDate = (date: Date) => {
    return new Intl.DateTimeFormat('de-DE', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    }).format(date);
  };

  const formatTime = (date: Date) => {
    return new Intl.DateTimeFormat('de-DE', {
      hour: '2-digit',
      minute: '2-digit',
    }).format(date);
  };

  return (
    <div className={`bg-dark-gray/90 backdrop-blur-sm rounded-lg overflow-hidden border border-venue-${event.venueType} hover:shadow-neon-pink transition-shadow duration-300`}>
      <div className="relative h-48">
        <Image
          src={event.imageUrl || 'https://picsum.photos/400/300'}
          alt={event.title}
          fill
          className="object-cover"
        />
      </div>
      <div className="p-4">
        <h3 className="text-xl font-bold mb-2">{event.title}</h3>
        <div className="space-y-2 text-sm">
          <div className="flex items-center gap-2">
            <Calendar size={16} className={`text-venue-${event.venueType}`} />
            <span>{formatDate(event.date)}</span>
          </div>
          <div className="flex items-center gap-2">
            <Clock size={16} className={`text-venue-${event.venueType}`} />
            <span>{formatTime(event.date)} Uhr</span>
          </div>
          <div className="flex items-center gap-2">
            <MapPin size={16} className={`text-venue-${event.venueType}`} />
            <span>{event.location}</span>
          </div>
        </div>
        {event.description && (
          <p className="mt-4 text-sm text-gray-300 line-clamp-2">
            {event.description}
          </p>
        )}
      </div>
    </div>
  );
}
