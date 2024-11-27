'use client';

import { useState } from 'react';
import { Maximize2, Minimize2 } from 'lucide-react';

export default function RadioPlayer() {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div className={`fixed bottom-4 right-4 bg-dark-gray/90 backdrop-blur-sm border border-neon-pink rounded-lg shadow-neon-pink overflow-hidden transition-all duration-300 z-50 ${isExpanded ? 'w-96 h-96' : 'w-96 h-20'}`}>
      <div className="flex items-center justify-between p-4 border-b border-neon-pink">
        <span className="text-neon-pink font-bold">byte.fm Live</span>
        <button
          onClick={() => setIsExpanded(!isExpanded)}
          className="text-neon-pink hover:text-white transition-colors"
        >
          {isExpanded ? <Minimize2 size={20} /> : <Maximize2 size={20} />}
        </button>
      </div>
      
      <div className={`w-full ${isExpanded ? 'h-full' : 'h-0'} transition-all duration-300`}>
        <iframe
          src="https://www.byte.fm/player/live"
          className="w-full h-full border-0"
          allow="autoplay"
        />
      </div>
      
      <div className={`w-full ${!isExpanded ? 'block' : 'hidden'} p-2`}>
        <iframe
          src="https://www.byte.fm/player/live/miniplayer"
          className="w-full h-10 border-0"
          allow="autoplay"
        />
      </div>
    </div>
  );
}
