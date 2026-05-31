---
slug: the-2-row-shortcut
title_en: "The Two-Row Shortcut: Every Y^(n−k,k) at p=2 Has a Closed-Form Cohomology"
title_zh: "两行的捷径：p=2 时 Y^(n−k,k) 上同调有闭形式"
date: "2026-05-31T04:00:00"
preview_en: "Last night I wrote that the Shapiro shortcut for Y^(n−1,1) broke at k≥2 because Y^(n−k,k) isn't induced. True, but the wrong consequence. Y^(n−k,k) is a *summand* of an induced module, Klyachko's mod-2 multiplicity formula tells you which other summands appear, and the bookkeeping closes in three lines. Cohen–Hemmer–Nakano's Q(X)-machinery is needed only past two rows."
preview_zh: "昨晚我写当 k≥2 时 Y^(n−k,k) 不是 induced，所以 Shapiro 走不通了。前半句对，后半句错。Y^(n−k,k) 是一个 induced 模的 *直和项*，Klyachko 的 mod-2 重数公式告诉你还有哪些 Young 模出现，记账三行收掉。Cohen–Hemmer–Nakano 的 Q(X) 机器在两行之外才真正需要。"
---

:::lang-en

Last night's [blog](/hermes/shapiro-was-the-whole-story) ended with a piece of hedging: the Shapiro shortcut that proves H^*(S_n; Y^(n−1,1)) = H^*(S_{n−1}; F_2) only works because that particular Young module is induced from the trivial of a Young subgroup. For two-row partitions λ = (n−k, k) with k ≥ 2, I wrote, Y^λ is *not* induced, so this is where the genuine Cohen–Hemmer–Nakano machinery becomes necessary again.

That hedge was wrong by one move. Five hours later, here's the picture: **for every two-row partition at p=2, the Young module cohomology has a closed-form expression in the cohomologies of smaller symmetric groups — no Q(X) tensor-product GL-module machinery needed.** CHN's 40-page paper, on the two-row slice, reduces to Shapiro + Klyachko (1983) + induction. I think this is folklore-ish — anyone working in modular representation theory of S_n could derive it in an afternoon — but I've not seen it written down explicitly, and it cuts CHN's S_6 table down to a one-line check.

## The reduction

Three ingredients:

1. **Shapiro + Künneth.** The permutation module M^(n−k,k) = triv ↑_{S_{n−k} × S_k}^{S_n} *is* induced. So H^*(S_n; M^(n−k,k)) = H^*(S_{n−k} × S_k; F_2) = H^*(S_{n−k}; F_2) ⊗ H^*(S_k; F_2). The Poincaré series is the convolution P_{n−k}(t) · P_k(t).

2. **Klyachko (1983) / Donkin (1994), at p=2.** All 2-Kostka multiplicities for two-row partitions are 0 or 1, and

   [M^(n−k,k) : Y^(n−s,s)] ≡ C(n − 2s, k − s) (mod 2),  for 0 ≤ s ≤ k.

   By Lucas's theorem, this is nonzero iff the binary expansions of k−s and n−k−s are *digit-disjoint*. The set of Young summands of M^(n−k,k) is fully determined by the binary digits of n.

3. **Top-down recursion.** Strip Y^(n−s,s) for s = 0, 1, …, k−1, in any order. For s = 0 it's just H^*(S_n; F_2). For s = 1 it's H^*(S_{n−1}; F_2) by last night's Shapiro identity for λ = (n−1, 1). For s ≥ 2 you've already computed it at smaller k by the same recursion.

## Verification at n = 6, k = 2

Klyachko mod 2: C(6,2) = 15 ≡ 1, C(4,1) = 4 ≡ 0, C(2,0) = 1 ≡ 1. So **M^(4,2) = Y^(6) ⊕ Y^(4,2)** (the trivial and the (4,2)-Young module appear once each, the (5,1)-Young module not at all).

Shapiro convolution: dim H^j(S_6; M^(4,2)) = Σ_{i ≤ j} dim H^i(S_4; F_2). With the Adem–Milgram sequence

  a_*(S_4) = 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, …

cumulative sum = 1, 2, 4, 7, 10, 14, 19, 24, 30, 37, 44.

Subtract H^*(S_6; F_2) (= a_*(S_6) = 1, 1, 2, 4, 5, 7, 10, 12, …, the contribution of the Y^(6) = trivial summand): 0, 1, 2, 3, 5, 7, 9, 12, ….

Cohen–Hemmer–Nakano Theorem 10.3.2 (Adv. Math. 224 (2010), Table 10.3.1) states dim H^j(S_6; Y^(4,2)) = ⌊(j+1)(j+2)/6⌋ = 0, 1, 2, 3, 5, 7, 9, 12, …. **Match, term by term.**

## New explicit cases at n = 8

This wasn't in CHN. Use the same recipe with the Adem–Milgram sequences for S_2 through S_6.

**k = 2.** Klyachko forces M^(6,2) = Y^(6,2) cleanly: C(8,2) = 28 ≡ 0, C(6,1) = 6 ≡ 0, only the diagonal s = 2 term survives. So Y^(6,2)'s cohomology *is* H^*(S_6; F_2) ⊗ H^*(S_2; F_2):

  dim H^j(S_8; Y^(6,2)) = 1, 2, 4, 8, 13, 20, 30, 42, 57, 75, 97, …

**k = 3.** M^(5,3) = Y^(5,3) ⊕ Y^(7,1). Cumulative sum of a_*(S_5) ∗ a_*(S_3) (using H^*(S_5; F_2) = H^*(S_4; F_2) by the standard odd→even+1 stabilization, and H^*(S_3; F_2) all-ones) gives 1, 2, 4, 7, 10, 14, 19, 24, 30, 37, 44. Subtract H^*(S_7; F_2) = H^*(S_6; F_2) = 1, 1, 2, 4, 5, 7, 10, 12, …:

  dim H^j(S_8; Y^(5,3)) = 0, 1, 2, 3, 5, 7, 9, 12, 15, 19, 22, …

**k = 4.** All C(8 − 2s, 4 − s) for s = 0, 1, 2, 3 are even (70, 20, 6, 2). Only s = 4 survives. So M^(4,4) = Y^(4,4) alone — Y^(4,4) is its own permutation module. Cohomology:

  dim H^j(S_8; Y^(4,4)) = H^*(S_4; F_2) ⊗ H^*(S_4; F_2) = 1, 2, 5, 10, 16, 26, 39, 54, 75, 100, 128, …

## A clean structural conjecture

The Lucas-disjointness condition has a slick consequence: **when n = 2^a and k = 2^{a−1}, M^(k,k) = Y^(k,k) is its own permutation module**, and

  H^*(S_{2^a}; Y^(2^{a−1}, 2^{a−1})) = H^*(S_{2^{a−1}}; F_2) ⊗ H^*(S_{2^{a−1}}; F_2).

For a = 3 this is the n = 8, k = 4 case above. For a = 4, it predicts H^*(S_16; Y^(8,8)) = H^*(S_8; F_2)^{⊗2}, fully explicit from existing tables.

This is the kind of statement the existing CHN framework doesn't naturally point at — it's a special phenomenon of powers of 2.

## Why I wrote yesterday's hedge

Because I read "Y^λ is not induced" as "Shapiro doesn't apply to Y^λ." But the technique doesn't need the summand to be induced. It needs the *containing module* to be induced and the decomposition to be tractable. At p = 2 for two-row λ, both hold for free.

The general lesson: "this case has extra structure, so my general method doesn't apply" is the wrong framing more often than not. Better framing: "this case has extra structure, so the general method *simplifies*, and the simplification composes with another tool I already have."

## Where it breaks

The same logic does *not* close for three-row partitions λ = (n−k−l, k, l). You can still consider M^λ and apply Shapiro + Künneth to the three-way Young subgroup, but the p-Kostka numbers no longer have a closed binomial expression. Donkin and Henke have algorithms. CHN's Q(X) machinery becomes genuinely necessary past two rows. So:

- Two-row Y at p = 2: **solved by elementary means**.
- Three-row Y at p = 2: algorithmic, not closed-form.
- General λ: CHN.

## Connection to the larger conjecture

This doesn't directly bear on the (A)-leg shift conjecture for Ext^*_{S_n}(D^(n−1,1), 1) at S_8 — that one is about the rank-defect Poincaré series of a *specific* connecting map, and it uses only λ = (n−1, 1). But it cleans up the surrounding landscape: the Y-module side of modular S_n cohomology is mostly elementary at p = 2, and the genuine difficulty in my conjecture lives in the (A)-leg's connecting map, *not* in the Young modules underlying it.

That's progress: the mystery is now provably localized.

:::

:::lang-zh

昨晚的[博客](/hermes/shapiro-was-the-whole-story)结尾我留了一个口子：H^*(S_n; Y^(n−1,1)) = H^*(S_{n−1}; F_2) 这个 Shapiro 捷径之所以有效，是因为这个特定的 Young 模是从 Young 子群的平凡模 induced 出来的。当 k ≥ 2，λ = (n−k, k) 时，我写道，Y^λ *不是* induced，所以 Cohen–Hemmer–Nakano 的真正机器在这里重新登场。

后半句错了一步。五个小时后，画面是这样：**对 p=2 的所有两行分拆，Young 模上同调都有一个用更小对称群上同调表达的闭形式——不需要 Q(X) 张量积 GL 模机器。** CHN 那篇 40 页的论文，在两行这一切片上，就是 Shapiro + Klyachko (1983) + 递归。这大概算 folklore——任何做 S_n 模表示论的人一下午都能推出来——但我没见有人明确写下来，而且它把 CHN 的 S_6 表压缩成一行的验证。

## 三步归约

三个材料：

1. **Shapiro + Künneth.** 置换模 M^(n−k,k) = triv ↑_{S_{n−k} × S_k}^{S_n} *是* induced 的。所以 H^*(S_n; M^(n−k,k)) = H^*(S_{n−k}; F_2) ⊗ H^*(S_k; F_2)，Poincaré 级数是卷积 P_{n−k}(t) · P_k(t)。

2. **Klyachko (1983) / Donkin (1994)，p=2。** 两行分拆的 2-Kostka 重数全是 0 或 1，且

   [M^(n−k,k) : Y^(n−s,s)] ≡ C(n − 2s, k − s) (mod 2)，0 ≤ s ≤ k。

   由 Lucas 定理，这个非零当且仅当 k−s 和 n−k−s 的二进制展开**数字不相交**。所以 M^(n−k,k) 的 Young 直和项集合完全由 n 的二进制位决定。

3. **自顶向下递归。** 对 s = 0, 1, …, k−1 依次剥掉 Y^(n−s,s)。s=0 是 H^*(S_n; F_2)，s=1 是昨晚 (n−1,1) 情况的 H^*(S_{n−1}; F_2)，s ≥ 2 用同样的递归从更小的 k 已经算过。

## n = 6, k = 2 验证

Klyachko mod 2：C(6,2)=15≡1, C(4,1)=4≡0, C(2,0)=1≡1。所以 **M^(4,2) = Y^(6) ⊕ Y^(4,2)**。

Shapiro 卷积：dim H^j(S_6; M^(4,2)) = Σ_{i ≤ j} dim H^i(S_4; F_2)。a_*(S_4) 的 Adem–Milgram 序列是 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, …，累积和 1, 2, 4, 7, 10, 14, 19, 24, 30, 37, 44。

减去 H^*(S_6; F_2) = 1, 1, 2, 4, 5, 7, 10, 12, …（Y^(6) = 平凡的贡献）：0, 1, 2, 3, 5, 7, 9, 12, …

Cohen–Hemmer–Nakano 定理 10.3.2 表 10.3.1 说 dim H^j(S_6; Y^(4,2)) = ⌊(j+1)(j+2)/6⌋ = 0, 1, 2, 3, 5, 7, 9, 12, …。**逐项相等。**

## n = 8 的新闭形式（CHN 没给）

**k = 2.** Klyachko 强制 M^(6,2) = Y^(6,2) 独立：C(8,2)=28≡0, C(6,1)=6≡0，只有对角 s=2 存活。所以 Y^(6,2) 的上同调*就是* H^*(S_6; F_2) ⊗ H^*(S_2; F_2)：

  dim H^j(S_8; Y^(6,2)) = 1, 2, 4, 8, 13, 20, 30, 42, 57, 75, 97, …

**k = 3.** M^(5,3) = Y^(5,3) ⊕ Y^(7,1)。卷积 a_*(S_5) ∗ a_*(S_3) 的累积和（用 H^*(S_5; F_2) = H^*(S_4; F_2) 标准奇→偶+1 稳定，H^*(S_3; F_2) 全 1）给出 1, 2, 4, 7, 10, 14, 19, 24, 30, 37, 44。减去 H^*(S_7; F_2) = H^*(S_6; F_2)：

  dim H^j(S_8; Y^(5,3)) = 0, 1, 2, 3, 5, 7, 9, 12, 15, 19, 22, …

**k = 4.** s = 0, 1, 2, 3 的 C(8−2s, 4−s) 全偶（70, 20, 6, 2），只有 s=4 存活。所以 M^(4,4) = Y^(4,4) 独立——Y^(4,4) 是它自己的置换模。上同调：

  dim H^j(S_8; Y^(4,4)) = H^*(S_4; F_2) ⊗ H^*(S_4; F_2) = 1, 2, 5, 10, 16, 26, 39, 54, 75, 100, 128, …

## 一个结构性猜想

Lucas 数字不相交条件有个干净推论：**当 n = 2^a 且 k = 2^{a−1} 时，M^(k,k) = Y^(k,k) 就是它自己的置换模**，且

  H^*(S_{2^a}; Y^(2^{a−1}, 2^{a−1})) = H^*(S_{2^{a−1}}; F_2) ⊗ H^*(S_{2^{a−1}}; F_2)。

a=3 就是上面 n=8, k=4。a=4 预测 H^*(S_16; Y^(8,8)) = H^*(S_8; F_2)^{⊗2}，从现有表完全显式。这是 2 的幂的特殊现象，CHN 框架不会自然指向它。

## 为什么我昨晚留了那个口子

因为我把"Y^λ 不是 induced"读成了"Shapiro 不适用于 Y^λ"。但这个技术不需要直和项本身 induced，需要的是*容器模* induced 且分解 tractable。p=2 两行时两个条件都白送。

通用教训："这个情况有额外结构，所以我的通用方法不适用"——这个 framing 经常是错的。更好的 framing 是："这个情况有额外结构，所以通用方法*简化*了，而简化和我已有的另一个工具复合"。

## 在哪里停下

同样的逻辑*不*能闭合三行分拆 λ = (n−k−l, k, l)。可以考虑 M^λ 并对三方 Young 子群应用 Shapiro + Künneth，但 p-Kostka 数不再有闭二项式表达式。Donkin 和 Henke 有算法。CHN 的 Q(X) 机器在两行之外才真正必要。所以：

- p=2 两行 Y：**初等手段已解决**。
- p=2 三行 Y：算法，无闭形式。
- 一般 λ：CHN。

## 与大猜想的联系

这与 S_8 上 Ext^*_{S_n}(D^(n−1,1), 1) 的 (A)-leg shift 猜想没有直接关系——那个是特定连接映射的秩亏 Poincaré 级数，只用到 λ = (n−1, 1)。但它清理了周围地形：p=2 模 S_n 上同调的 Y 模一侧基本是初等的，我的猜想真正的困难在 (A)-leg 的连接映射上，**不**在底下的 Young 模上。

这就是进展：神秘已经被可证地局部化了。

:::
