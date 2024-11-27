'use client';

import { Search } from 'lucide-react';
import Image from 'next/image';

export default function Header() {
  return (
    <header className="fixed top-0 left-0 right-0 h-20 bg-black bg-opacity-50 backdrop-blur-lg z-40 flex items-center px-4 md:px-6">
      <h1 className="text-2xl md:text-3xl font-bold text-white">
        Hamburg Techno Events
      </h1>
    </header>
  );
}
