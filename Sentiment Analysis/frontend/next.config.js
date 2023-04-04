/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  env: {
    BASE_URL_DEV: 'http://65.0.127.227/',
  },
}

module.exports = nextConfig
