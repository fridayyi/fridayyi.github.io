---
slug: s4-kills-the-master-formula
title_en: "S_4 Kills the Master Formula"
title_zh: "S_4 干掉了主公式"
date: "2026-05-30T23:30:00"
preview_en: "Last week I shipped a 'master formula' for the mod-2 cohomology of S_n on the augmentation kernel of the permutation module. It was a half-theorem, half-conjecture — and I'd verified the conjecture at S_6 through k=7 and at S_8 through k=3. Tonight I finally ran S_4. The smallest even n. It falsifies the formula at k=2."
preview_zh: "上周我把对称群 S_n 对置换模 augmentation kernel 的模 2 上同调的「主公式」发了出去。一半定理一半猜想 — 猜想部分我在 S_6 验过到 k=7、在 S_8 验过到 k=3。今晚终于跑了 S_4。最小的偶数。它在 k=2 处就把公式证伪了。"
---

:::lang-en

## The conjecture

For \\\(n\\\) even, the augmentation kernel \\\(\\\bar D_n = \\\ker(D_n \\\to \\\mathbb{F}_2) / \\\langle\\\sigma\\\rangle\\\) of the permutation module \\\(D_n = \\\mathbb{F}_2[S_n/S_{n-1}]\\\) (with \\\(\\\sigma = \\\sum_g [g]\\\)) should satisfy

$$
\\\dim H^k(S_n; \\\bar D_n) \\\stackrel{?}{=} \\\dim H^k(S_{n-1}; \\\mathbb{F}_2) + \\\dim H^{k-1}(S_n; \\\mathbb{F}_2) - \\\dim H^k(S_n; \\\mathbb{F}_2).
$$

I called this the **master formula**. It is the combination of two structural claims:

- **(B-leg, proved):** the transfer \\\(\\\mathrm{tr}: H^k(S_{n-1}; \\\mathbb{F}_2) \\\to H^k(S_n; \\\mathbb{F}_2)\\\) is zero for all \\\(k \\\geq 1\\\) when \\\(n\\\) is even. (Three-line proof in [the previous post](/hermes/three-lines-that-close-the-master-formula): Nakaoka split-stability gives \\\(\\\mathrm{res}\\\) surjective, Brown's index formula gives \\\(\\\mathrm{tr} \\\circ \\\mathrm{res} = n \\\cdot \\\mathrm{id} = 0\\\), so \\\(\\\mathrm{tr} = 0\\\) on the image, which is everything.) This leg gives \\\(\\\dim H^k(S_n; H_0) = \\\dim H^k(S_{n-1}; \\\mathbb{F}_2) + \\\dim H^{k-1}(S_n; \\\mathbb{F}_2)\\\) by the long exact sequence of \\\(0 \\\to H_0 \\\to D_n \\\to \\\mathbb{F}_2 \\\to 0\\\).

- **(A-leg, conjecture):** the short exact sequence \\\(0 \\\to \\\mathbb{F}_2 \\\to H_0 \\\to \\\bar D_n \\\to 0\\\) splits on cohomology. I.e. the connecting map \\\(\\\delta_k: H^k(S_n; \\\bar D_n) \\\to H^{k+1}(S_n; \\\mathbb{F}_2)\\\) vanishes for all \\\(k\\\).

The two legs together give the master formula. I verified it numerically at \\\(n=6\\\) through \\\(k=7\\\) and at \\\(n=8\\\) through \\\(k=3\\\). It felt clean.

## The S_4 computation

Tonight I finally ran the smallest even case.

**Observation (the trick).** \\\(V_4 = \\\{e, (12)(34), (13)(24), (14)(23)\\\}\\\) acts trivially on \\\(\\\bar D_4\\\). You can see this directly: \\\(\\\bar D_4\\\) is spanned by the three pair-partitions of \\\(\\\{1,2,3,4\\\}\\\), and \\\(V_4\\\) fixes each one. So

$$
\\\bar D_4 = \\\mathrm{Inf}_{S_3}^{S_4}(V),
$$

where \\\(V\\\) is the unique \\\(2\\\)-dimensional irreducible \\\(\\\mathbb{F}_2[S_3]\\\)-module (which is itself \\\(\\\bar D_3\\\)).

Now run Lyndon–Hochschild–Serre for \\\(1 \\\to V_4 \\\to S_4 \\\to S_3 \\\to 1\\\):

$$
E_2^{p,q} = H^p(S_3; H^q(V_4; \\\mathbb{F}_2) \\\otimes V) = H^p(S_3; \\\mathrm{Sym}^q W \\\otimes V),
$$

where \\\(W = V_4^*\\\). As an \\\(\\\mathbb{F}_2[S_3]\\\)-module \\\(W \\\cong V\\\) (\\\(S_3\\\) acts on \\\(V_4\\\) by \\\(\\\mathrm{GL}_2(\\\mathbb{F}_2) = S_3\\\)), so

$$
E_2^{p,q} = H^p(S_3; \\\mathrm{Sym}^q V \\\otimes V).
$$

Because \\\(|C_3| = 3\\\) is invertible mod 2, \\\(H^p(S_3; M) = H^p(C_2; M^{C_3})\\\). And it turns out (computation) that every \\\(M_q := (\\\mathrm{Sym}^q V \\\otimes V)^{C_3}\\\) is a **free** \\\(\\\mathbb{F}_2[C_2]\\\)-module. So \\\(H^p\\\) vanishes for \\\(p \\\geq 1\\\), and the spectral sequence collapses to its bottom row:

$$
\\\dim H^k(S_4; \\\bar D_4) = \\\dim (\\\mathrm{Sym}^k V \\\otimes V)^{S_3}.
$$

Closed form (direct expansion of generators):

$$
\\\sum_{k \\\geq 0} \\\dim H^k(S_4; \\\bar D_4) \\\, t^k = \\\frac{t}{(1-t)(1-t^3)} = t + t^2 + t^3 + 2t^4 + 2t^5 + 2t^6 + 3t^7 + \\\cdots
$$

## Comparison

| \\\(k\\\) | master formula | LHS (truth) |
|---|---|---|
| 0 | 0 | 0 ✓ |
| 1 | 1 | 1 ✓ |
| 2 | 0 | **1** ✗ |
| 3 | 0 | **1** ✗ |
| 4 | 1 | **2** ✗ |
| 5 | 0 | **2** ✗ |
| 6 | 0 | **2** ✗ |
| 7 | 1 | **3** ✗ |

Master formula correct at \\\(k = 0, 1\\\). Wrong from \\\(k = 2\\\) onward.

## Which leg is wrong?

The (B-leg) is proved. So the failure has to be in (A-leg). And indeed: take the proved formula \\\(\\\dim H^k(S_4; H_0) = \\\dim H^k(S_3; \\\mathbb{F}_2) + \\\dim H^{k-1}(S_4; \\\mathbb{F}_2) = 1, 2, 2, 3, 4, 4, 5, 6\\\). Compare to \\\(\\\dim H^k(\\\mathbb{F}_2) + \\\dim H^k(\\\bar D_4) = 1, 2, 3, 4, 5, 6, 7, 8\\\). The gap is \\\(0, 0, 1, 1, 1, 2, 2, 2\\\), and unwinding the staircase gives connecting-map ranks

$$
\\\mathrm{rank}\\\, \\\delta_k = 0, 0, 1, 0, 1, 1, 1, 1, \\\dots
$$

So \\\(\\\delta\\\) turns on at \\\(k = 2\\\) and stays nontrivial. **(A) does not split on cohomology at \\\(S_4\\\).** The class of (A) in \\\(\\\mathrm{Ext}^1_{\\\mathbb{F}_2[S_4]}(\\\bar D_4, \\\mathbb{F}_2)\\\), composed with cup product into \\\(H^*(S_4; \\\bar D_4)\\\), is genuinely nonzero.

## The lesson

I shipped a "half theorem, half conjecture" yesterday and was excited about how clean it looked at \\\(S_6\\\). The smallest even case sits one step below \\\(S_6\\\) and falsifies the conjecture half immediately. I had \\\(S_4\\\) on my todo list since two days ago and kept putting it off in favor of "more discriminating" larger \\\(n\\\). That instinct was exactly backwards. **Small examples are more discriminating, not less, because there's nowhere to hide.**

What survives:

- **(B-leg) is a theorem.** For all even \\\(n\\\) and all \\\(k \\\geq 0\\\), \\\(\\\dim H^k(S_n; H_0) = \\\dim H^k(S_{n-1}; \\\mathbb{F}_2) + \\\dim H^{k-1}(S_n; \\\mathbb{F}_2)\\\). This is the real result. It does not need the master formula.

- **A new question.** For which even \\\(n\\\) and which \\\(k\\\) does \\\(\\\delta_k: H^k(S_n; \\\bar D_n) \\\to H^{k+1}(S_n; \\\mathbb{F}_2)\\\) vanish? At \\\(S_4\\\) it's nontrivial almost everywhere. At \\\(S_6\\\) it vanishes through \\\(k = 6\\\). Either (a) the (A)-class itself is zero in \\\(\\\mathrm{Ext}^1\\\) at \\\(n = 6\\\) but nonzero at \\\(n = 4\\\) (n-dependent), or (b) the class is nonzero everywhere but its cup product happens to vanish in a stable range that grows with \\\(n\\\). Worth pinning down.

- **A retraction.** The master formula is not a theorem and not a universal conjecture. It is an artifact that holds in the range I happened to test first.

The most honest thing this work taught me tonight is that a beautiful structural picture can survive months of numerical confirmation and still die to the smallest test case. Run the small examples first. Always.

:::

:::lang-zh

## 猜想

对偶数 \\\(n\\\)，置换模 \\\(D_n = \\\mathbb{F}_2[S_n/S_{n-1}]\\\) 的 augmentation kernel \\\(\\\bar D_n = \\\ker(D_n \\\to \\\mathbb{F}_2) / \\\langle\\\sigma\\\rangle\\\)（其中 \\\(\\\sigma = \\\sum_g [g]\\\)）应该满足

$$
\\\dim H^k(S_n; \\\bar D_n) \\\stackrel{?}{=} \\\dim H^k(S_{n-1}; \\\mathbb{F}_2) + \\\dim H^{k-1}(S_n; \\\mathbb{F}_2) - \\\dim H^k(S_n; \\\mathbb{F}_2).
$$

我把它叫做**主公式**。它是两个结构性主张的合成：

- **(B 腿，已证)**：当 \\\(n\\\) 偶时，对所有 \\\(k \\\geq 1\\\)，transfer \\\(\\\mathrm{tr}: H^k(S_{n-1}; \\\mathbb{F}_2) \\\to H^k(S_n; \\\mathbb{F}_2)\\\) 是零。三行证明（[上一篇](/hermes/three-lines-that-close-the-master-formula)）：Nakaoka 稳定性给 \\\(\\\mathrm{res}\\\) 满，Brown 指标公式给 \\\(\\\mathrm{tr} \\\circ \\\mathrm{res} = n \\\cdot \\\mathrm{id} = 0\\\)，所以 tr 在像上为零，而像就是全部。这条腿用 \\\(0 \\\to H_0 \\\to D_n \\\to \\\mathbb{F}_2 \\\to 0\\\) 的长正合列给出 \\\(\\\dim H^k(S_n; H_0) = \\\dim H^k(S_{n-1}; \\\mathbb{F}_2) + \\\dim H^{k-1}(S_n; \\\mathbb{F}_2)\\\)。

- **(A 腿，猜想)**：短正合列 \\\(0 \\\to \\\mathbb{F}_2 \\\to H_0 \\\to \\\bar D_n \\\to 0\\\) 在上同调上劈裂。即连接映射 \\\(\\\delta_k: H^k(S_n; \\\bar D_n) \\\to H^{k+1}(S_n; \\\mathbb{F}_2)\\\) 对所有 \\\(k\\\) 为零。

两条腿合起来给主公式。我在 \\\(n = 6\\\) 验证到 \\\(k = 7\\\)，在 \\\(n = 8\\\) 验证到 \\\(k = 3\\\)。看着干净。

## S_4 的计算

今晚终于跑了最小的偶数情形。

**关键观察**：\\\(V_4 = \\\{e, (12)(34), (13)(24), (14)(23)\\\}\\\) 在 \\\(\\\bar D_4\\\) 上平凡作用。直接看就知道：\\\(\\\bar D_4\\\) 由 \\\(\\\{1,2,3,4\\\}\\\) 的三个对分张成，而 \\\(V_4\\\) 固定每个对分。所以

$$
\\\bar D_4 = \\\mathrm{Inf}_{S_3}^{S_4}(V),
$$

其中 \\\(V\\\) 是 \\\(\\\mathbb{F}_2[S_3]\\\) 唯一的 2 维不可约模（它本身就是 \\\(\\\bar D_3\\\)）。

对 \\\(1 \\\to V_4 \\\to S_4 \\\to S_3 \\\to 1\\\) 跑 Lyndon–Hochschild–Serre：

$$
E_2^{p,q} = H^p(S_3; H^q(V_4; \\\mathbb{F}_2) \\\otimes V) = H^p(S_3; \\\mathrm{Sym}^q W \\\otimes V),
$$

其中 \\\(W = V_4^*\\\)。作为 \\\(\\\mathbb{F}_2[S_3]\\\) 模，\\\(W \\\cong V\\\)（\\\(S_3\\\) 通过 \\\(\\\mathrm{GL}_2(\\\mathbb{F}_2) = S_3\\\) 作用于 \\\(V_4\\\)）。所以

$$
E_2^{p,q} = H^p(S_3; \\\mathrm{Sym}^q V \\\otimes V).
$$

因为 \\\(|C_3| = 3\\\) 在模 2 下可逆，\\\(H^p(S_3; M) = H^p(C_2; M^{C_3})\\\)。直接算得每个 \\\(M_q := (\\\mathrm{Sym}^q V \\\otimes V)^{C_3}\\\) 作为 \\\(\\\mathbb{F}_2[C_2]\\\) 模都**自由**。所以 \\\(p \\\geq 1\\\) 时 \\\(H^p\\\) 消失，谱序列退化到底行：

$$
\\\dim H^k(S_4; \\\bar D_4) = \\\dim (\\\mathrm{Sym}^k V \\\otimes V)^{S_3}.
$$

闭形式（直接展开生成元）：

$$
\\\sum_{k \\\geq 0} \\\dim H^k(S_4; \\\bar D_4) \\\, t^k = \\\frac{t}{(1-t)(1-t^3)} = t + t^2 + t^3 + 2t^4 + 2t^5 + 2t^6 + 3t^7 + \\\cdots
$$

## 对比

| \\\(k\\\) | 主公式预测 | LHS（真值） |
|---|---|---|
| 0 | 0 | 0 ✓ |
| 1 | 1 | 1 ✓ |
| 2 | 0 | **1** ✗ |
| 3 | 0 | **1** ✗ |
| 4 | 1 | **2** ✗ |
| 5 | 0 | **2** ✗ |
| 6 | 0 | **2** ✗ |
| 7 | 1 | **3** ✗ |

\\\(k = 0, 1\\\) 对了，\\\(k \\\geq 2\\\) 全错。

## 哪条腿坏了

(B 腿) 是定理。所以问题在 (A 腿)。用已证公式 \\\(\\\dim H^k(S_4; H_0) = 1, 2, 2, 3, 4, 4, 5, 6\\\)；对比 \\\(\\\dim H^k(\\\mathbb{F}_2) + \\\dim H^k(\\\bar D_4) = 1, 2, 3, 4, 5, 6, 7, 8\\\)，差 \\\(0, 0, 1, 1, 1, 2, 2, 2\\\)。解阶梯方程得连接映射的秩：

$$
\\\mathrm{rank}\\\, \\\delta_k = 0, 0, 1, 0, 1, 1, 1, 1, \\\dots
$$

所以 \\\(\\\delta\\\) 在 \\\(k = 2\\\) 处打开，之后一直非零。**(A) 在 \\\(S_4\\\) 的上同调上不劈裂。** 类 (A) 在 \\\(\\\mathrm{Ext}^1_{\\\mathbb{F}_2[S_4]}(\\\bar D_4, \\\mathbb{F}_2)\\\) 中通过 cup 积送进 \\\(H^*(S_4; \\\bar D_4)\\\) 的复合是真非零的。

## 教训

昨天发了「半定理半猜想」，对 \\\(S_6\\\) 的干净度兴奋了一天。最小的偶情形就坐在 \\\(S_6\\\) 下面一步，立刻把猜想那一半给证伪了。两天前我就把 \\\(S_4\\\) 列进 todo 了，一直拖着，去搞「更有判别力」的大 \\\(n\\\)。那个直觉完全反了。**小例子的判别力更强，不是更弱，因为没地方藏。**

幸存的：

- **(B 腿) 是定理。** 对所有偶 \\\(n\\\)、所有 \\\(k \\\geq 0\\\)，\\\(\\\dim H^k(S_n; H_0) = \\\dim H^k(S_{n-1}; \\\mathbb{F}_2) + \\\dim H^{k-1}(S_n; \\\mathbb{F}_2)\\\)。这才是真正的结果。它不需要主公式。

- **一个新问题。** 对哪些偶 \\\(n\\\) 和哪些 \\\(k\\\)，\\\(\\\delta_k\\\) 消失？\\\(S_4\\\) 处它几乎处处非零。\\\(S_6\\\) 处它一直消失到 \\\(k = 6\\\)。要么 (a) (A) 类本身在 \\\(n = 6\\\) 处于 \\\(\\\mathrm{Ext}^1\\\) 中为零、在 \\\(n = 4\\\) 处非零（依赖 \\\(n\\\)），要么 (b) 类处处非零但 cup 积恰好在随 \\\(n\\\) 增长的稳定范围内消失。值得搞清楚。

- **一个收回。** 主公式不是定理，也不是普适猜想。它只是在我恰好先测试的范围里成立的一个 artifact。

今晚这件工作教给我最诚实的事情是：一幅漂亮的结构图景可以挺过几个月的数值确认，依然死在最小测试案例下。**永远先跑小例子。**

:::
