'use client';

import { Calendar, Music } from 'lucide-react';
import Link from 'next/link';

export default function Sidebar() {
  return (
    <div className="fixed left-0 top-0 h-full w-64 bg-black bg-opacity-50 backdrop-blur-lg p-6 pt-24">
      <nav>
        <ul className="space-y-4">
          <li>
            <Link href="/?category=week" className="flex items-center text-gray-300 hover:text-white transition-colors">
              <Calendar className="w-5 h-5 mr-3" />
              Diese Woche
            </Link>
          </li>
          <li>
            <Link href="/?category=weekend" className="flex items-center text-gray-300 hover:text-white transition-colors">
              <Music className="w-5 h-5 mr-3" />
              Dieses Wochenende
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}
