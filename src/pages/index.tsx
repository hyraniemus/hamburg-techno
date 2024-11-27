import Header from '@/components/layout/Header';
import Sidebar from '@/components/layout/Sidebar';
import EventGrid from '@/components/features/EventGrid';
import BackgroundVideo from '@/components/features/BackgroundVideo';
import { Event } from '@/types';
import { getToday, addDays } from '@/utils/dates';

// Mock data for development
const today = getToday();
const mockEvents: Event[] = [
  {
    id: '1',
    title: 'Techno Night @ PAL',
    date: today,
    location: 'PAL Hamburg',
    description: 'Eine Nacht voller Techno mit den besten DJs der Stadt.',
    venueType: 'teal',
  },
  {
    id: '2',
    title: 'Underground Vibes',
    date: addDays(today, 1),
    location: 'Waagenbau',
    description: 'Deep House und Techno im legendären Waagenbau.',
    venueType: 'blue',
  },
  {
    id: '3',
    title: 'Hafenklang Rave',
    date: addDays(today, 2),
    location: 'Hafenklang',
    description: 'Industrieller Techno in historischer Location.',
    venueType: 'orange',
  },
  {
    id: '4',
    title: 'Übel & Gefährlich',
    date: addDays(today, 3),
    location: 'U&G Hamburg',
    description: 'Techno und Electro im Bunker.',
    venueType: 'green',
  },
];

export default function Home() {
  return (
    <div className="min-h-screen">
      <BackgroundVideo />
      <Header />
      <div className="pt-20">
        <Sidebar />
        <main className="ml-64 p-6">
          <EventGrid events={mockEvents} />
        </main>
      </div>
    </div>
  );
}
