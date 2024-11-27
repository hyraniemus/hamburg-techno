/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    domains: ['ohschonhell.de'],
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'ohschonhell.de',
        pathname: '/wp-content/uploads/**',
      },
      {
        protocol: 'https',
        hostname: 'picsum.photos',
        port: '',
        pathname: '/**',
      },
      {
        protocol: 'https',
        hostname: 'ra.co',
        port: '',
        pathname: '/**',
      },
    ],
  },
}

module.exports = nextConfig
