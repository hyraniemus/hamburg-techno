'use client';

import Image from 'next/image';

export default function Background() {
  return (
    <div className="fixed top-0 left-0 w-full h-full -z-10 overflow-hidden">
      <div className="absolute inset-0 bg-black/70" /> {/* Overlay für bessere Lesbarkeit */}
      <Image
        src="/images/schreddeer1.jpg"
        alt="Background"
        fill
        className="object-cover"
        priority
      />
    </div>
  );
}
