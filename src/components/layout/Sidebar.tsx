'use client';

import { Calendar, Music, Star, Menu, X } from 'lucide-react';
import Link from 'next/link';
import { useState } from 'react';

export default function Sidebar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      {/* Mobile Menu Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="fixed top-4 right-4 z-50 p-2 bg-black/50 rounded-lg md:hidden"
      >
        {isOpen ? (
          <X className="w-6 h-6 text-white" />
        ) : (
          <Menu className="w-6 h-6 text-white" />
        )}
      </button>

      {/* Sidebar */}
      <div className={`
        fixed top-0 left-0 h-full w-64 bg-black bg-opacity-50 backdrop-blur-lg p-6 pt-24
        transform transition-transform duration-300 ease-in-out
        md:translate-x-0
        ${isOpen ? 'translate-x-0' : '-translate-x-full'}
      `}>
        <nav>
          <ul className="space-y-4">
            <li>
              <Link 
                href="/?category=week" 
                className="flex items-center text-gray-300 hover:text-white transition-colors"
                onClick={() => setIsOpen(false)}
              >
                <Calendar className="w-5 h-5 mr-3" />
                Diese Woche
              </Link>
            </li>
            <li>
              <Link 
                href="/?category=weekend" 
                className="flex items-center text-gray-300 hover:text-white transition-colors"
                onClick={() => setIsOpen(false)}
              >
                <Music className="w-5 h-5 mr-3" />
                Dieses Wochenende
              </Link>
            </li>
            <li>
              <Link 
                href="/?category=upcoming" 
                className="flex items-center text-gray-300 hover:text-white transition-colors"
                onClick={() => setIsOpen(false)}
              >
                <Star className="w-5 h-5 mr-3" />
                Top DJs Next Month
              </Link>
            </li>
          </ul>
        </nav>
      </div>

      {/* Overlay for mobile */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-30 md:hidden"
          onClick={() => setIsOpen(false)}
        />
      )}
    </>
  );
}
