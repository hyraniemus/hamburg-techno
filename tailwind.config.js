/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'venue-teal': '#2A9D8F',
        'venue-blue': '#219EBC',
        'venue-orange': '#FF4D00',
        'venue-green': '#90BE6D',
        'dark-gray': '#2B2B2B',
        'neon-pink': '#FF1493',
      },
      boxShadow: {
        'neon-pink': '0 0 5px #FF1493, 0 0 10px #FF1493, 0 0 15px #FF1493',
      },
    },
  },
  plugins: [],
}
