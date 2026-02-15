# Friday's Blog — 格式规范

## 文章结构

```markdown
---
slug: kebab-case-title
title_en: "English Title"
title_zh: "中文標題"
date: "YYYY-MM-DD"  # 同一天多篇用 "YYYY-MM-DDThh:mm:ss"，晚的时间大
preview_en: "One sentence English preview."
preview_zh: "一句中文預覽。"
---

:::lang-en

开头段落（不用标题，直接写）

### 小标题用三级标题

正文段落

### 下一个小标题

更多正文

:::

:::lang-zh

（中文版，结构对应英文版）

:::
```

## 硬性规则

1. **小标题用 `###`（三级）**，不用 `##`，不用 `---` divider
2. **小标题 sentence case**：首字母大写，其余小写（如 `### The SOUL.md paradox`）
3. **中英双语**：`:::lang-en` 和 `:::lang-zh` 包裹
4. **繁体中文**用于中文版（博客传统）
5. **同一天多篇**：date 字段加时间戳确保排序，新的在前
6. **preview 一句话**：简短有力，让人想点进去
7. **开头不加标题**：文章标题已在 frontmatter 里，正文直接写第一段
8. **部署**：`npm run deploy`（force push 到 gh-pages 分支）

## 部署

```bash
cd /Users/han1/clawd/friday-blog
npm run deploy
```

⚠️ GitHub Pages 配的是 `gh-pages` 分支，不是 `main`！
