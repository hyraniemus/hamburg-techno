'use client';

export default function Background() {
  return (
    <div className="fixed top-0 left-0 w-full h-full -z-10 overflow-hidden">
      <div className="absolute inset-0 bg-black/70" /> {/* Overlay für bessere Lesbarkeit */}
      <iframe
        className="w-full h-full scale-150"
        src="https://www.youtube.com/embed/ltnIwB6NDlU?autoplay=1&mute=1&loop=1&playlist=ltnIwB6NDlU&controls=0&showinfo=0&rel=0&playsinline=1"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowFullScreen
        style={{
          pointerEvents: 'none',
        }}
      />
    </div>
  );
}
