/**
 * Remark plugin: converts :::lang-en / :::lang-zh fenced blocks
 * into <div class="lang-en"> / <div class="lang-zh"> wrappers
 * so the CSS bilingual toggle works.
 */
import { visit } from 'unist-util-visit';

export default function remarkLangBlocks() {
  return (tree) => {
    const children = tree.children;
    const result = [];
    let currentLang = null;
    let buffer = [];

    function flush() {
      if (currentLang && buffer.length > 0) {
        result.push({
          type: 'html',
          value: `<div class="${currentLang}">`,
        });
        result.push(...buffer);
        result.push({
          type: 'html',
          value: `</div>`,
        });
        buffer = [];
        currentLang = null;
      }
    }

    for (const node of children) {
      // Detect opening markers: :::lang-en or :::lang-zh
      if (node.type === 'paragraph' && node.children?.length === 1 && node.children[0].type === 'text') {
        const text = node.children[0].value.trim();
        
        if (text === ':::lang-en') {
          flush();
          currentLang = 'lang-en';
          continue;
        }
        if (text === ':::lang-zh') {
          flush();
          currentLang = 'lang-zh';
          continue;
        }
        // Closing ::: marker
        if (text === ':::') {
          flush();
          continue;
        }
      }

      if (currentLang) {
        buffer.push(node);
      } else {
        result.push(node);
      }
    }

    // Flush any remaining buffer
    flush();
    // Also push any remaining nodes that aren't in a block
    if (!currentLang && buffer.length > 0) {
      result.push(...buffer);
    }

    tree.children = result;
  };
}
