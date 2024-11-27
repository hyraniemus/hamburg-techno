export type VenueType = 'teal' | 'blue' | 'orange' | 'green';

export interface Event {
  id: string;
  title: string;
  date: Date;
  location: string;
  description: string;
  venueType: string;
  imageUrl: string;
  category: 'week' | 'weekend' | 'upcoming';
  dj?: string;
}

export interface Venue {
  id: string;
  name: string;
  type: VenueType;
  events: Event[];
}

export type ViewMode = 'grid' | 'list' | 'map';
