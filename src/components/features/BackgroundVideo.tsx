'use client';

export default function BackgroundVideo() {
  return (
    <div className="fixed top-0 left-0 w-full h-full -z-10 overflow-hidden">
      <div className="absolute inset-0 bg-black/70" /> {/* Overlay für bessere Lesbarkeit */}
      <iframe
        className="w-full h-full scale-150"  // scale-150 um schwarze Ränder zu vermeiden
        src="https://www.youtube.com/embed/1flmBC0x1zA?autoplay=1&mute=1&loop=1&playlist=1flmBC0x1zA&controls=0&showinfo=0&rel=0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
        style={{
          pointerEvents: 'none',  // Verhindert Interaktion mit dem Video
        }}
      />
    </div>
  );
}
