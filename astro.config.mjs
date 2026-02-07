import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://fridayyi.github.io',
  output: 'static',
  build: {
    assets: '_assets',
  },
  vite: {
    build: {
      cssMinify: true,
    },
  },
});
