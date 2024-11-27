import Header from '@/components/layout/Header';
import Sidebar from '@/components/layout/Sidebar';
import EventGrid from '@/components/features/EventGrid';
import Background from '@/components/features/Background';
import { Event } from '@/types';
import { getToday, addDays } from '@/utils/dates';

// Mock data with current dates
const today = getToday();
const mockEvents: Event[] = [
  // Diese Woche
  {
    id: '1',
    title: 'Techno Night @ PAL',
    date: today,
    location: 'PAL Hamburg',
    description: 'Eine Nacht voller Techno mit den besten DJs der Stadt.',
    venueType: 'teal',
    imageUrl: '/images/schreddeer1.jpg',
    category: 'week'
  },
  {
    id: '2',
    title: 'Underground Vibes',
    date: addDays(today, 1),
    location: 'Waagenbau',
    description: 'Deep House und Techno im legendären Waagenbau.',
    venueType: 'blue',
    imageUrl: '/images/schreddeer1.jpg',
    category: 'week'
  },
  {
    id: '3',
    title: 'Hafenklang Rave',
    date: addDays(today, 2),
    location: 'Hafenklang',
    description: 'Industrieller Techno in historischer Location.',
    venueType: 'orange',
    imageUrl: '/images/schreddeer1.jpg',
    category: 'week'
  },
  // Dieses Wochenende
  {
    id: '4',
    title: 'Übel & Gefährlich',
    date: addDays(today, 5),
    location: 'U&G Hamburg',
    description: 'Techno und Electro im Bunker.',
    venueType: 'green',
    imageUrl: '/images/schreddeer1.jpg',
    category: 'weekend'
  },
  {
    id: '5',
    title: 'Terrassen Techno',
    date: addDays(today, 5),
    location: 'Uebel & Gefährlich',
    description: 'Open Air Techno auf der Terrasse mit Blick über Hamburg.',
    venueType: 'purple',
    imageUrl: '/images/schreddeer1.jpg',
    category: 'weekend'
  },
  {
    id: '6',
    title: 'Waterfront Beats',
    date: addDays(today, 6),
    location: 'Hamburger Hafen',
    description: 'Techno am Wasser mit internationalen DJs.',
    venueType: 'yellow',
    imageUrl: '/images/schreddeer1.jpg',
    category: 'weekend'
  },
  {
    id: '7',
    title: 'Warehouse Session',
    date: addDays(today, 6),
    location: 'PAL Hamburg',
    description: 'Raw Techno in industrieller Atmosphäre.',
    venueType: 'teal',
    imageUrl: '/images/schreddeer1.jpg',
    category: 'weekend'
  },
  // Kommende Top-DJs
  {
    id: '8',
    title: 'ARTBAT Exclusive',
    date: addDays(today, 30),
    location: 'PAL Hamburg',
    description: 'Das ukrainische Duo ARTBAT präsentiert melodischen Techno der Extraklasse.',
    venueType: 'red',
    imageUrl: '/images/schreddeer1.jpg',
    category: 'upcoming',
    dj: 'ARTBAT'
  },
  {
    id: '9',
    title: 'Charlotte de Witte',
    date: addDays(today, 35),
    location: 'Uebel & Gefährlich',
    description: 'Die Queen des Dark Techno kommt nach Hamburg!',
    venueType: 'purple',
    imageUrl: '/images/schreddeer1.jpg',
    category: 'upcoming',
    dj: 'Charlotte de Witte'
  },
  {
    id: '10',
    title: 'Boris Brejcha präsentiert FCKNG SERIOUS',
    date: addDays(today, 40),
    location: 'Große Freiheit 36',
    description: 'High-Tech Minimal vom maskierten Meister.',
    venueType: 'blue',
    imageUrl: '/images/schreddeer1.jpg',
    category: 'upcoming',
    dj: 'Boris Brejcha'
  }
];

export default function Home() {
  return (
    <div className="min-h-screen">
      <Background />
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
