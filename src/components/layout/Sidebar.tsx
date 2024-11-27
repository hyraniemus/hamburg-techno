'use client';

import { Calendar, MapPin, Music } from 'lucide-react';

export default function Sidebar() {
  return (
    <aside className="fixed left-0 top-20 h-full w-64 bg-dark-gray/90 backdrop-blur-sm border-r border-neon-pink shadow-neon-pink p-6">
      <div className="space-y-8">
        <div>
          <h3 className="text-neon-pink font-bold mb-4 flex items-center gap-2">
            <Calendar size={20} />
            DATUM
          </h3>
          <div className="space-y-2">
            <button className="w-full text-left py-2 px-4 rounded hover:bg-white/10 transition-colors">
              Heute
            </button>
            <button className="w-full text-left py-2 px-4 rounded hover:bg-white/10 transition-colors">
              Diese Woche
            </button>
            <button className="w-full text-left py-2 px-4 rounded hover:bg-white/10 transition-colors">
              Dieses Wochenende
            </button>
          </div>
        </div>

        <div>
          <h3 className="text-neon-pink font-bold mb-4 flex items-center gap-2">
            <MapPin size={20} />
            BEZIRK
          </h3>
          <div className="space-y-2">
            <button className="w-full text-left py-2 px-4 rounded hover:bg-white/10 transition-colors">
              St. Pauli
            </button>
            <button className="w-full text-left py-2 px-4 rounded hover:bg-white/10 transition-colors">
              Sternschanze
            </button>
            <button className="w-full text-left py-2 px-4 rounded hover:bg-white/10 transition-colors">
              HafenCity
            </button>
          </div>
        </div>

        <div>
          <h3 className="text-neon-pink font-bold mb-4 flex items-center gap-2">
            <Music size={20} />
            GENRE
          </h3>
          <div className="space-y-2">
            <button className="w-full text-left py-2 px-4 rounded hover:bg-white/10 transition-colors">
              Techno
            </button>
            <button className="w-full text-left py-2 px-4 rounded hover:bg-white/10 transition-colors">
              House
            </button>
            <button className="w-full text-left py-2 px-4 rounded hover:bg-white/10 transition-colors">
              Minimal
            </button>
          </div>
        </div>
      </div>
    </aside>
  );
}
