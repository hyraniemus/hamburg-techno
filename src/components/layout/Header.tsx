'use client';

import { Search } from 'lucide-react';
import Image from 'next/image';

export default function Header() {
  return (
    <header className="fixed top-0 left-0 right-0 bg-dark-gray/90 backdrop-blur-sm border-b border-neon-pink shadow-neon-pink z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center py-4">
          <div className="flex-1">
            <div className="relative w-48 h-16">
              <Image
                src="/Schredder.png"
                alt="Hamburg Techno Events"
                fill
                className="object-contain brightness-200"
                priority
              />
            </div>
          </div>
          
          <nav className="hidden md:flex space-x-8">
            <a href="#" className="text-white hover:text-neon-pink transition-colors">KALENDER</a>
            <a href="#" className="text-white hover:text-neon-pink transition-colors">KARTE</a>
            <a href="#" className="text-white hover:text-neon-pink transition-colors">ORTE</a>
            <a href="#" className="text-white hover:text-neon-pink transition-colors">OPEN AIRS</a>
            <a href="#" className="text-white hover:text-neon-pink transition-colors">NEWSLETTER</a>
          </nav>

          <div className="flex-1 flex justify-end">
            <div className="relative">
              <input
                type="text"
                placeholder="Event suchen..."
                className="w-64 px-4 py-2 rounded-full bg-white/10 border border-neon-pink focus:outline-none focus:ring-2 focus:ring-neon-pink"
              />
              <Search className="absolute right-3 top-2.5 text-neon-pink" size={20} />
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
