import { defineCollection, z } from 'astro:content';

const hermes = defineCollection({
  type: 'content',
  schema: z.object({
    title_en: z.string(),
    title_zh: z.string(),
    date: z.string(),
    preview_en: z.string(),
    preview_zh: z.string(),
  }),
});

const posts = defineCollection({
  type: 'content',
  schema: z.object({
    title_en: z.string(),
    title_zh: z.string(),
    date: z.string(),
    preview_en: z.string(),
    preview_zh: z.string(),
    author: z.string().optional(),
  }),
});

export const collections = { posts, hermes };
