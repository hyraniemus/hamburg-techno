export interface Event {
  id: string;
  title: string;
  date: Date;
  location: string;
  description?: string;
  imageUrl?: string;
  venueType: 'teal' | 'blue' | 'orange' | 'green';
}

export interface Venue {
  id: string;
  name: string;
  type: 'teal' | 'blue' | 'orange' | 'green';
  events: Event[];
}

export type ViewMode = 'grid' | 'list' | 'map';
