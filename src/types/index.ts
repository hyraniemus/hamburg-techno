export type VenueType = 'teal' | 'blue' | 'orange' | 'green';

export interface Event {
  id: string;
  title: string;
  date: Date;
  location: string;
  description: string;
  venueType: VenueType;
  imageUrl: string;  // Neue Eigenschaft für Bilder
}

export interface Venue {
  id: string;
  name: string;
  type: VenueType;
  events: Event[];
}

export type ViewMode = 'grid' | 'list' | 'map';
