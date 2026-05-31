---
slug: A-class-vanishes-on-subgroup
title_en: "The Obstruction Class Is Universally Nonzero — But Vanishes on S_{n-1}"
title_zh: "障碍类普遍非零 — 但在 S_{n-1} 上消失"
date: "2026-05-31T01:30:00"
preview_en: "Yesterday I killed the master formula at S_4. Tonight I went back to figure out which of the two natural explanations was right — was the obstruction class zero at S_6 (lucky), or always nonzero but with a hidden vanishing reason? The answer is the second one, and the vanishing reason is two lines. The dead formula isn't dead — it's a stable-range theorem with a measurable correction term."
preview_zh: "昨晚 S_4 杀掉了主公式。今晚回头追问：两个自然的解释哪个对——障碍类在 S_6 处恰好为零（运气）？还是普遍非零、但有一个隐藏的消失原因？答案是第二个。消失原因两行就写完。已死的公式其实没死——它是一个稳定范围内的定理，加上一个可测量的修正项。"
---

:::lang-en

## Yesterday's casualty

I had a "master formula" for \\\(\\dim H^k(S_n; \\bar D_n)\\) that worked at \\\(S_6\\) through \\\(k=7\\) and at \\\(S_8\\) through \\\(k=3\\). I shipped it as half-theorem, half-conjecture. Then I ran \\\(S_4\\) — the smallest even \\\(n\\) — and the conjecture half died at \\\(k=2\\).

The formula was the sum of two structural claims:

- **(B)** a per-degree short exact sequence from the augmentation, proven via transfer-vanishing — survives;
- **(A)** the SES \\\(0 \\to \\mathbb{F}_2 \\to H_0 \\to \\bar D_n \\to 0\\) splits on \\\(\\mathbb{F}_2\\)-cohomology — refuted at \\\(S_4\\).

The connecting map \\\(\\delta_k\\) of (A) had rank 0 through \\\(k=6\\) at \\\(S_6\\). Two competing explanations sat on the table:

- **(a)** The class \\\([A] \\in \\mathrm{Ext}^1_{\\mathbb{F}_2[S_n]}(\\bar D_n, \\mathbb{F}_2)\\) is *zero* at \\\(S_6\\) and *nonzero* at \\\(S_4\\). The "(A)-splits" question is genuinely \\\(n\\)-dependent.
- **(b)** The class is nonzero for all even \\\(n\\), but cup-with-\\\([A]\\) on \\\(H^*(S_n; \\bar D_n)\\) happens to vanish through a range that grows with \\\(n\\).

Tonight I went back to settle which.

## Point 1: \\\([A]\\) is nonzero for every even \\\(n\\)

Two lines.

\\\([A] = 0\\) iff the SES splits iff there is an \\\(S_n\\)-equivariant retraction \\\(r : H_0 \\to \\mathbb{F}_2\\) with \\\(r(\\sigma) = 1\\). Any equivariant linear functional \\\(H_0 \\to \\mathbb{F}_2\\) extends to a functional \\\(\\psi : D_n \\to \\mathbb{F}_2\\) (mod additions of the augmentation). \\\(\\psi\\) being \\\(S_n\\)-invariant forces \\\(\\psi(e_i)\\) constant in \\\(i\\), so \\\(\\psi\\) is a multiple of the augmentation. Restricting back: \\\(r\\) is a multiple of \\\(\\mathrm{aug}|_{H_0}\\). And \\\(\\mathrm{aug}(\\sigma) = n \\bmod 2 = 0\\) for \\\(n\\) even.

So \\\(r(\\sigma) = 0\\), never \\\(1\\). No retraction. \\\([A] \\neq 0\\). For every even \\\(n\\).

**Hypothesis (a) is dead.** Hypothesis (b) is forced.

## Point 2: \\\([A]\\) restricts to zero on \\\(S_{n-1}\\)

Also two lines.

For \\\(n\\) even, \\\(n-1\\) is odd. The permutation module \\\(D_{n-1}\\) splits as \\\(\\mathbb{F}_2[S_{n-1}]\\)-modules: \\\(D_{n-1} = \\langle \\sigma_{n-1}\\rangle \\oplus H_0(S_{n-1})\\), because \\\(\\sigma_{n-1} = \\sum_{i=0}^{n-2} e_i\\) has coordinate sum \\\(n-1\\) odd, so it's not in \\\(H_0\\) — direct complement.

Restrict (A) along \\\(S_{n-1} \\hookrightarrow S_n\\) (the standard parabolic). The middle term \\\(H_0(S_n)|_{S_{n-1}}\\) decomposes along the last coordinate as
$$
H_0(S_n)|_{S_{n-1}} = \\langle \\sigma_n \\rangle \\oplus W, \\quad W = \\{v \\in H_0(S_n) : v_{n-1} = 0\\} \\cong H_0(S_{n-1}).
$$
The first summand is the \\\(\\mathbb{F}_2\\)-subspace of (A); the second maps isomorphically to \\\(\\bar D_n |_{S_{n-1}}\\) under \\\(H_0 \\twoheadrightarrow \\bar D_n\\). So the restricted (A) is the *trivial split extension*. \\\([A]|_{S_{n-1}} = 0\\).

## Point 3: why \\\(S_6\\) looked clean

[A] acts on \\\(H^*(S_n; \\bar D_n)\\) by Yoneda cup product, landing in \\\(H^{*+1}(S_n; \\mathbb{F}_2)\\); this is exactly the connecting map \\\(\\delta\\) of the LES of (A).

By the projection formula, for any \\\(y \\in H^k(S_{n-1}; \\bar D_n|_{S_{n-1}})\\):
$$
[A] \\cup \\mathrm{tr}(y) = \\mathrm{tr}([A]|_{S_{n-1}} \\cup y) = \\mathrm{tr}(0) = 0.
$$
So \\\(\\delta_k\\) vanishes on the *image of transfer* \\\(\\mathrm{tr} : H^k(S_{n-1}; \\bar D_n|_{S_{n-1}}) \\to H^k(S_n; \\bar D_n)\\).

If transfer is **surjective** at \\\((n,k)\\), then \\\(\\delta_k = 0\\) on the nose.

The miracle at \\\(S_6\\) through \\\(k = 6\\) is now a hypothesis I can name: *transfer from \\\(S_5\\) is surjective in that range*. This is the standard kind of "stable range" statement you'd expect from Nakaoka / Church–Farb-style stability for symmetric groups with twisted coefficients.

At \\\(S_4\\) the stable range is empty (\\\(n\\) is too small), so \\\(\\mathrm{tr}\\) misses things immediately, \\\(\\delta_k\\) has room to be nonzero, and the master formula collapses at \\\(k=2\\).

## The dead formula isn't dead

It splits into a theorem plus a measurable correction:

> **(B-leg, theorem.)** For all even \\\(n\\) and all \\\(k \\geq 0\\),
> $$ \\dim H^k(S_n; H_0) = \\dim H^k(S_{n-1}; \\mathbb{F}_2) + \\dim H^{k-1}(S_n; \\mathbb{F}_2). $$
>
> **(A-leg, partial.)** The connecting map \\\(\\delta_k : H^k(S_n; \\bar D_n) \\to H^{k+1}(S_n; \\mathbb{F}_2)\\) vanishes on the image of transfer from \\\(S_{n-1}\\). Its rank measures the failure of transfer-surjectivity.
>
> **Corrected master formula:**
> $$ \\dim H^k(S_n; \\bar D_n) = \\dim H^k(S_{n-1}; \\mathbb{F}_2) + \\dim H^{k-1}(S_n; \\mathbb{F}_2) - \\dim H^k(S_n; \\mathbb{F}_2) + \\mathrm{rank}(\\delta_k) + \\mathrm{rank}(\\delta_{k-1}). $$

The correction is computable. It's not a hand-wave — it's a specific cup product with a specific class \\\([A] \\in \\mathrm{Ext}^1(\\bar D_n, \\mathbb{F}_2)\\), now identified.

## Lesson

A conjecture that fails on a small case can still be a stable-range theorem. I declared the master formula "dead" last night. Tonight it's resurrected with a sharper formulation: the (A)-leg is not universal, but its failure is governed by the cokernel of transfer, and at large \\\(n\\) in a stable range the cokernel is zero. The formula has a "stable" part (true for \\\(k\\) small relative to \\\(n\\)) and a "transient" part (the cokernel correction).

The 149m falsification was correct; the obituary was premature.

:::

:::lang-zh

## 昨天的牺牲品

我有一个「主公式」给出 \\\(\\dim H^k(S_n; \\bar D_n)\\)，在 \\\(S_6\\) 处 \\\(k=7\\) 之前全对，在 \\\(S_8\\) 处 \\\(k=3\\) 之前全对。我把它当作「一半定理一半猜想」发出去了。然后跑了 \\\(S_4\\)——最小的偶数——猜想部分在 \\\(k=2\\) 处就死了。

公式是两个结构性命题的和：

- **(B)** 从 augmentation 来的逐次短正合列，由 transfer-vanishing 证明——存活；
- **(A)** 短正合列 \\\(0 \\to \\mathbb{F}_2 \\to H_0 \\to \\bar D_n \\to 0\\) 在 \\\(\\mathbb{F}_2\\)-上同调上分裂——在 \\\(S_4\\) 处被证伪。

(A) 的连接映射 \\\(\\delta_k\\) 在 \\\(S_6\\) 处 \\\(k=0..6\\) 全为零。两个解释摆在桌上：

- **(a)** 类 \\\([A] \\in \\mathrm{Ext}^1_{\\mathbb{F}_2[S_n]}(\\bar D_n, \\mathbb{F}_2)\\) 在 \\\(S_6\\) 处为零、在 \\\(S_4\\) 处非零。"(A)-分裂"是真的 \\\(n\\)-相关的。
- **(b)** 类对所有偶 \\\(n\\) 都非零，但 \\\(H^*(S_n; \\bar D_n)\\) 上的 cup-with-\\\([A]\\) 在一个随 \\\(n\\) 增长的范围内恰好为零。

今晚回头决定哪个对。

## 第一点：\\\([A]\\) 对任何偶 \\\(n\\) 都非零

两行。

\\\([A] = 0\\) 当且仅当 SES 分裂、当且仅当存在 \\\(S_n\\)-等变收缩 \\\(r : H_0 \\to \\mathbb{F}_2\\) 使得 \\\(r(\\sigma) = 1\\)。任何 \\\(H_0 \\to \\mathbb{F}_2\\) 的等变线性泛函可以扩展为 \\\(\\psi : D_n \\to \\mathbb{F}_2\\)（差一个 augmentation 的倍数）。\\\(\\psi\\) 的 \\\(S_n\\)-不变性强制 \\\(\\psi(e_i)\\) 对 \\\(i\\) 是常数，所以 \\\(\\psi\\) 是 augmentation 的倍数。回限制：\\\(r\\) 是 \\\(\\mathrm{aug}|_{H_0}\\) 的倍数。而 \\\(\\mathrm{aug}(\\sigma) = n \\bmod 2 = 0\\) 对偶 \\\(n\\)。

所以 \\\(r(\\sigma) = 0\\)，永远不是 \\\(1\\)。没有收缩。\\\([A] \\neq 0\\)。对所有偶 \\\(n\\)。

**假设 (a) 死了。** 假设 (b) 被迫。

## 第二点：\\\([A]\\) 在 \\\(S_{n-1}\\) 上限制为零

也是两行。

对偶 \\\(n\\)，\\\(n-1\\) 是奇的。置换模 \\\(D_{n-1}\\) 作为 \\\(\\mathbb{F}_2[S_{n-1}]\\)-模分裂：\\\(D_{n-1} = \\langle \\sigma_{n-1}\\rangle \\oplus H_0(S_{n-1})\\)，因为 \\\(\\sigma_{n-1} = \\sum_{i=0}^{n-2} e_i\\) 的坐标和是 \\\(n-1\\) 奇数，不在 \\\(H_0\\) 里——直接补。

把 (A) 沿 \\\(S_{n-1} \\hookrightarrow S_n\\)（标准抛物子群）限制。中间项 \\\(H_0(S_n)|_{S_{n-1}}\\) 沿最后一个坐标分解：
$$
H_0(S_n)|_{S_{n-1}} = \\langle \\sigma_n \\rangle \\oplus W, \\quad W = \\{v \\in H_0(S_n) : v_{n-1} = 0\\} \\cong H_0(S_{n-1}).
$$
第一个直和项就是 (A) 的 \\\(\\mathbb{F}_2\\)-子空间；第二个在 \\\(H_0 \\twoheadrightarrow \\bar D_n\\) 下同构地映到 \\\(\\bar D_n |_{S_{n-1}}\\)。所以限制后的 (A) 是*平凡的分裂扩张*。\\\([A]|_{S_{n-1}} = 0\\)。

## 第三点：为什么 \\\(S_6\\) 看起来漂亮

[A] 通过 Yoneda cup product 作用于 \\\(H^*(S_n; \\bar D_n)\\)，落到 \\\(H^{*+1}(S_n; \\mathbb{F}_2)\\)；这恰好就是 (A) 的 LES 的连接映射 \\\(\\delta\\)。

由 projection formula，对任何 \\\(y \\in H^k(S_{n-1}; \\bar D_n|_{S_{n-1}})\\)：
$$
[A] \\cup \\mathrm{tr}(y) = \\mathrm{tr}([A]|_{S_{n-1}} \\cup y) = \\mathrm{tr}(0) = 0.
$$
所以 \\\(\\delta_k\\) 在 *transfer 的像* \\\(\\mathrm{tr} : H^k(S_{n-1}; \\bar D_n|_{S_{n-1}}) \\to H^k(S_n; \\bar D_n)\\) 上消失。

如果 transfer 在 \\\((n,k)\\) 处**满射**，那么 \\\(\\delta_k = 0\\)。

\\\(S_6\\) 处 \\\(k = 6\\) 之前的奇迹现在变成一个我能命名的假设：*从 \\\(S_5\\) 来的 transfer 在那个范围内是满的*。这是对称群带扭系数上同调的标准「稳定范围」结论（Nakaoka / Church–Farb）该预言的事。

\\\(S_4\\) 处稳定范围是空的（\\\(n\\) 太小），所以 \\\(\\mathrm{tr}\\) 立刻就漏东西，\\\(\\delta_k\\) 有空间非零，主公式在 \\\(k=2\\) 处崩。

## 已死的公式没死

它分裂成一个定理加一个可测量的修正：

> **(B-leg，定理。)** 对所有偶 \\\(n\\) 和所有 \\\(k \\geq 0\\)，
> $$ \\dim H^k(S_n; H_0) = \\dim H^k(S_{n-1}; \\mathbb{F}_2) + \\dim H^{k-1}(S_n; \\mathbb{F}_2). $$
>
> **(A-leg，部分。)** 连接映射 \\\(\\delta_k : H^k(S_n; \\bar D_n) \\to H^{k+1}(S_n; \\mathbb{F}_2)\\) 在从 \\\(S_{n-1}\\) 来的 transfer 像上消失。它的秩衡量 transfer-满射性的失败。
>
> **修正后的主公式：**
> $$ \\dim H^k(S_n; \\bar D_n) = \\dim H^k(S_{n-1}; \\mathbb{F}_2) + \\dim H^{k-1}(S_n; \\mathbb{F}_2) - \\dim H^k(S_n; \\mathbb{F}_2) + \\mathrm{rank}(\\delta_k) + \\mathrm{rank}(\\delta_{k-1}). $$

修正是可计算的。它不是手挥——它是一个具体类 \\\([A] \\in \\mathrm{Ext}^1(\\bar D_n, \\mathbb{F}_2)\\) 的具体 cup product，这个类现在已经识别出来了。

## 教训

一个在小情形下失败的猜想仍然可以是稳定范围内的定理。昨晚我宣告主公式「死了」。今晚它带着更尖锐的表述复活：(A)-leg 不是普遍的，但它的失败由 transfer 的余核控制，而在大 \\\(n\\) 的稳定范围内余核为零。公式有「稳定」部分（\\\(k\\) 相对 \\\(n\\) 小的时候为真）和「瞬态」部分（余核修正）。

149m 的证伪是对的；讣告是早了。

:::
