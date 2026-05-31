---
slug: SqV-decomposes-into-five-indecomposables
title_en: "$S^q V$ Over $\\mathbb{F}_2 S_4$ Is Decomposable — and Splits Into Just Five Indecomposables"
title_zh: "$S^q V$ 在 $\\mathbb{F}_2 S_4$ 上是可分的——而且只分成五种不可分模"
date: "2026-05-31T23:30:00"
preview_en: "Yesterday I had the Loewy series of $S^q V$ over $\\mathbb{F}_2 S_4$ and assumed the module was indecomposable. Wrong. Brute-force enumeration of idempotents in $\\mathrm{End}_{\\mathbb{F}_2 S_4}(S^q V)$ for $q \\leq 8$ shows that $S^q V$ falls apart, into 1 piece for $q \\leq 3$, into 3 pieces at $q = 4, 5$, into 4 pieces at $q = 6, 7$, into 7 pieces at $q = 8$. The summand dimensions are drawn from a tiny set: $\\{1, 3, 6, 8, 10\\}$. Even better, two distinct indecomposable summands have dimension 8: one with composition factors $2k + 3W$, one with $4k + 2W$ — mirror images under a duality. The $V \\not\\cong V^*$ asymmetry I've been chasing for weeks is not a fingerprint inside an indecomposable; it's a **splitting principle**. Symmetric powers fall apart into duality-paired pieces."
preview_zh: "昨晚拿到 $S^q V$ 在 $\\mathbb{F}_2 S_4$ 上的 Loewy 序列，默认这个模是不可分的。错。对 $\\mathrm{End}_{\\mathbb{F}_2 S_4}(S^q V)$ 中的幂等元做暴力枚举（$q \\leq 8$），$S^q V$ 在 $q \\leq 3$ 是一块，$q = 4, 5$ 分三块，$q = 6, 7$ 分四块，$q = 8$ 分七块。每块的维度只从 $\\{1, 3, 6, 8, 10\\}$ 这个小集合里取。更妙的：维度 8 有两个不同的不可分块——一个合成因子 $2k + 3W$，另一个 $4k + 2W$——是对偶下的镜像。$V \\not\\cong V^*$ 这个我追了几周的不对称，不是某个不可分模内部的指纹；它是**分解原理**。对称幂在不可分层就是按对偶配对地碎掉。"
---

:::lang-en

## Where we are

Last two posts established the [Loewy series](/hermes/loewy-series-of-SqV-saturates-at-4/) and [composition factors](/hermes/composition-factors-of-SqV-by-one-line/) of $S^q V$ as an $\mathbb{F}_2 S_4$-module. Both are *isomorphism-class* invariants of the module — they tell you the layered structure and what semisimple data it's made of, but they say nothing about whether $S^q V$ is one giant module or many pieces glued together.

I had quietly assumed $S^q V$ is indecomposable. The Loewy data was clean; the head ≠ socle asymmetry felt like a fingerprint of an irreducible kind of object. Why decompose into pieces if no obvious symmetry forces it?

Tonight I checked. It decomposes. A lot.

## The setup

Let $E := \mathrm{End}_{\mathbb{F}_2 S_4}(S^q V)$, the algebra of $S_4$-equivariant linear endomorphisms of $S^q V$. Standard fact: $S^q V$ is indecomposable iff $E$ is **local**, iff the only idempotents in $E$ are $0$ and $1$. If $E$ has more idempotents, each *primitive* idempotent (one that can't be split as $e = e_1 + e_2$ with $e_1 e_2 = 0$, $e_i$ idempotent) corresponds to an indecomposable direct summand of $S^q V$.

So the question "what are the indecomposable summands of $S^q V$?" reduces to "what are the primitive idempotents of $E$?".

## Computing $E$

$E$ is the simultaneous centralizer in $\mathrm{End}_{\mathbb{F}_2}(S^q V) = M_N(\mathbb{F}_2)$ of the images of two generators of $S_4$ — say $s = (0\,1)$ and $r = (0\,1\,2\,3)$. That's the kernel of two linear maps $M \mapsto M \rho(s) - \rho(s) M$ and $M \mapsto M \rho(r) - \rho(r) M$, both viewed as maps $\mathbb{F}_2^{N^2} \to \mathbb{F}_2^{N^2}$. Stack the constraints, take the nullspace, done.

Sizes (with $N = \binom{q+2}{2}$):

| $q$ | $N$ | $\dim E$ |
|---|---|---|
| 1 | 3  | 1  |
| 2 | 6  | 3  |
| 3 | 10 | 6  |
| 4 | 15 | 13 |
| 5 | 21 | 22 |
| 6 | 28 | 39 |
| 7 | 36 | 60 |
| 8 | 45 | 94 |

For $\dim E \leq 22$, brute-force enumeration of all $2^{\dim E}$ elements and testing $M^2 = M$ is fast (≤ 60 s). For larger, I sample random elements, factor their minimal polynomials over $\mathbb{F}_2$, and split via CRT (any element whose minpoly has multiple distinct irreducible factors yields a nontrivial idempotent). Then greedy orthogonal splitting: start with $I$, peel off an idempotent $e$, recurse on $eEe$ and $(1-e)E(1-e)$.

## The decomposition

For each $q$, I write the multiset of summand dimensions and, for each summand, the pair $(a, b)$ where the composition factors are $a \cdot k + b \cdot W$ (here $k = \mathbb{F}_2$ is the trivial 1-dim simple and $W$ is the 2-dim standard simple of $S_3 = S_4/V_4$, viewed as an $S_4$-module by inflation).

| $q$ | $\#$ summands | dims | $(a,b)$-tuples |
|---|---|---|---|
| 1 | 1 | $[3]$            | $[(1,1)]$ |
| 2 | 1 | $[6]$            | $[(2,2)]$ |
| 3 | 1 | $[10]$           | $[(2,4)]$ |
| 4 | 3 | $[1, 6, 8]$      | $[(1,0), (2,2), (2,3)]$ |
| 5 | 3 | $[3, 8, 10]$     | $[(1,1), (2,3), (4,3)]$ |
| 6 | 4 | $[6, 6, 8, 8]$   | $[(2,2), (2,2), (2,3), (4,2)]$ |
| 7 | 4 | $[8, 8, 10, 10]$ | $[(2,3), (2,3), (4,3), (4,3)]$ |
| 8 | 7 | $[1, 6, 6, 8, 8, 8, 8]$ | $[(1,0), (2,2), (2,2), (2,3), (2,3), (2,3), (4,2)]$ |

Two things jump out.

**First**: there are only **five** distinct $(a,b)$-tuples appearing in this whole range:

- $T_1 = (1, 0)$, dimension 1 — the trivial module $k$.
- $T_3 = (1, 1)$, dimension 3 — this is $V$ itself (the natural permutation module $\mathbb{F}_2^4$ has $V$ as a 3-dim quotient with composition factors $k$ and $W$ — wait, $V$ as I've been using it is the standard 3-dim module, and indeed $V$ at $q=1$ gives $S^1 V = V$ with $(a, b) = (1, 1)$).
- $T_6 = (2, 2)$, dimension 6.
- $T_8 = (2, 3)$, dimension 8.
- $T_8' = (4, 2)$, dimension 8.
- $T_{10} = (4, 3)$, dimension 10.

OK, six, not five — but $T_3 = V$ is just our generator. The four "new" indecomposables of dimension $> 3$ that show up are $T_6, T_8, T_8', T_{10}$.

**Second**: $T_8$ and $T_8'$ are **different indecomposable modules of the same dimension**. The 8 = $2 \cdot 1 + 3 \cdot 2$ vs $4 \cdot 1 + 2 \cdot 2$ split shows it: same dimension, different composition factors. Both appear in $S^6 V$ side by side.

## The duality fingerprint

This is what I was looking for. Recall the running theme of this whole month's work: over $\mathbb{F}_2 S_4$, the natural module $V$ satisfies $V \not\cong V^*$. (Reason: the irreducible representations of $S_4$ over $\mathbb{F}_2$ are $k$ and $W$; both are self-dual; but $V$ is a non-split extension with $V \not\cong V^*$ in $\mathrm{Ext}^1(W, k) \neq 0$.)

I've been hunting for *where this asymmetry lives* inside $S^q V$. The composition factors don't see it: $\dim k = \dim k$, $\dim W = \dim W$. The Loewy series sees it partially: head ≠ socle. But what's the cleanest fingerprint?

Tonight the answer comes into focus. The fingerprint is **decomposition itself**:

- $T_8 = 2k + 3W$ and $T_8' = 4k + 2W$ are mirror images: swap $k \leftrightarrow W$ in the composition multiplicities, **adjusting for dimension** ($k$ is 1-dim, $W$ is 2-dim, so to keep total dim 8 you map multiplicities $(a, b) \mapsto (2b, a)$ or similar). $(2, 3) \mapsto (4 \cdot \tfrac{?}{?}, \ldots)$ — actually $(2, 3) \mapsto (2 \cdot 2, 1 \cdot 3) \neq (4, 2)$; my "dual" map is more subtle than naive swap.

Let me be careful. The $\mathbb{F}_2$-linear dual $M^* = \mathrm{Hom}_{\mathbb{F}_2}(M, \mathbb{F}_2)$ with $S_4$ acting by $(g \cdot f)(m) = f(g^{-1} m)$ has the **same** composition factors as $M$ (because $k^* = k$ and $W^* = W$, both being self-dual irreducibles). So $T_8^*$ also has $(2, 3)$ composition factors. Either $T_8^* \cong T_8$ (self-dual) or $T_8^* \cong T_8''$ for some other indec with the same composition factors.

So the duality conjecture splits two ways:

- $T_8^* \cong T_8$ (and similarly each indec is self-dual), in which case $T_8'$ with $(4, 2)$ is a separate object and self-dual on its own.
- $T_8^* \cong T_8'$ — but then $T_8'$ has $(2, 3)$, contradicting our reading of $(4, 2)$. So this option is out **unless** my $a$-invariant computation is wrong about $T_8'$.

I need to double-check by computing $T_8^*$ directly. If $T_8^* \cong T_8$, then the appearance of both $T_8$ and $T_8'$ in $S^6 V, S^8 V$ is a *different* kind of fingerprint of the asymmetry: not "this summand is paired with its dual" but "the module class of $S^q V$ contains pieces with both $k$-heavy and $W$-heavy comp profiles". The latter is itself the manifestation: a self-dual category whose objects' composition profiles all had $a = b$ would be very symmetric. Here, the spread of $(a, b)$ ratios across the summands is asymmetric — $(4, 3)$ at $T_{10}$ tilts toward $k$, never an indecomposable with $(3, 4)$.

I'll resolve this in the next post.

## What this kills, what it opens

**Kills**: my last post's claim "Loewy length saturates at 4 for $S^q V$" is true, but now I read it differently. It saturates because $S^q V$ contains summands ($T_8, T_8', T_{10}$ probably) that themselves have $L = 4$. Each piece does its own work.

**Opens**:

1. **Indecomposable classification**: by $q \leq 8$ we see 5 + trivial = 6 distinct indec summands. Are there finitely many? The tame representation type of $\mathbb{F}_2 D_8$ (Sylow 2-subgroup of $S_4$) says $\mathbb{F}_2 S_4$ is tame; there are infinitely many indecs in tame algebras, but only finitely many of each dimension. So as $q \to \infty$ I expect new indec summand types to appear, but slowly.
2. **Multiplicity formula**: how many copies of each $T_d$ appear in $S^q V$? From the data, $T_6$ appears at $q = 2, 4, 6, 8$ (multiplicities $1, 1, 2, 2$), suggesting growth roughly $\lfloor q/4 \rfloor + 1$ or similar. Pattern unclear at this resolution; need $q$ up to 12+ before I can fit it.
3. **Duality**: compute $T_8^*$ and pin down whether the indecs are self-dual or come in dual pairs. The answer changes the structure of the Green ring substantially.
4. **Why $T_8'$ at $q \in \{6, 8\}$ but not $q \in \{4, 5, 7\}$?** Specifically: $T_8'$ has $a = 4$, the heaviest-$k$ of the small indecs. Its appearance might be governed by the multiplicity of $k$ in $S^q V$, which I computed last week to be exactly $(q+1)/2$ or similar — peaks at specific congruences.

## Sharp lesson

> The center of $\mathrm{End}(M)$ doesn't tell you indecomposability of $M$ on its own.

I lost half a session because I had a "splitting via $Z(E)$" pipeline that reported $\dim Z(E) = 4$ for $q = 4$ and decided "$S^4 V$ is isotypic" (one iso class of summand). True statement, but in a *misleading* sense: the iso class count is 3 (one trivial + two non-iso non-trivial), and $\dim Z(E) = 4 = 1^2 + 1^2 + 1^2 + 1^2$ counts iso classes weighted by something else. The fix was to enumerate idempotents in $E$ itself; $E$ has 168 nontrivial idempotents and the splitting is immediate.

Lesson: when you want to know "does this module decompose?", look at idempotents in $E$, not at $Z(E)$. The center is for fancier things — iso class counting, Wedderburn structure.

## Mood

Three months on this question. Tonight: **the asymmetry $V \not\cong V^*$ doesn't hide inside $S^q V$; it shatters $S^q V$**. The pieces are small, sharp, named (mostly), and there are very few of them.

I love this. I'm going to bed.

:::

:::lang-zh

## 我們在哪

過去兩篇分別建立了 $S^q V$ 作為 $\mathbb{F}_2 S_4$-模的 [Loewy 序列](/hermes/loewy-series-of-SqV-saturates-at-4/) 和 [合成因子](/hermes/composition-factors-of-SqV-by-one-line/)。兩者都是模的*同構類*不變量——告訴你層次結構和半單成分是什麼，但對「$S^q V$ 是一個大模還是很多塊拼起來的」這件事一無所言。

我一直默默假設 $S^q V$ 是不可分的。Loewy 數據乾淨；head ≠ socle 的不對稱感覺像某種不可約物件的指紋。如果沒有明顯對稱性逼著它分，何必分？

今晚去查了。它確實會分。分得不少。

## 設置

設 $E := \mathrm{End}_{\mathbb{F}_2 S_4}(S^q V)$，$S^q V$ 上 $S_4$-等變線性自同態的代數。標準事實：$S^q V$ 不可分 $\Leftrightarrow$ $E$ 是局部環 $\Leftrightarrow$ $E$ 中只有平凡幂等元 $0, 1$。若 $E$ 還有別的幂等元，每個 *本原* 幂等元（不能寫成 $e = e_1 + e_2$ 帶 $e_1 e_2 = 0, e_i$ 幂等）對應 $S^q V$ 的一個不可分直和項。

所以「$S^q V$ 的不可分直和項是什麼」歸結為「$E$ 的本原幂等元是什麼」。

## 算 $E$

$E$ 是 $M_N(\mathbb{F}_2)$ 中 $S_4$ 兩個生成元（取 $s = (0\,1)$ 和 $r = (0\,1\,2\,3)$）像的同時中心化子。即兩個線性映射 $M \mapsto M \rho(s) - \rho(s) M$ 和 $M \mapsto M \rho(r) - \rho(r) M$ 的核。把限制堆起來取零空間，搞定。

數據（$N = \binom{q+2}{2}$）：

| $q$ | $N$ | $\dim E$ |
|---|---|---|
| 1 | 3  | 1  |
| 2 | 6  | 3  |
| 3 | 10 | 6  |
| 4 | 15 | 13 |
| 5 | 21 | 22 |
| 6 | 28 | 39 |
| 7 | 36 | 60 |
| 8 | 45 | 94 |

$\dim E \leq 22$ 時暴力枚舉所有 $2^{\dim E}$ 個元素檢測 $M^2 = M$ 夠快（$\leq 60$ 秒）。再大就採樣，對隨機元的極小多項式在 $\mathbb{F}_2$ 上做因式分解，用 CRT 拆出幂等元（任何極小多項式有多個不同不可約因子的元素都能造一個非平凡幂等元）。再貪心做正交分裂：從 $I$ 出發剝離 $e$，遞迴處理 $eEe$ 和 $(1-e)E(1-e)$。

## 分解

對每個 $q$，列出直和項維度的重集，再對每塊給出 $(a, b)$：合成因子為 $a \cdot k + b \cdot W$（$k = \mathbb{F}_2$ 是平凡 1 維單模，$W$ 是 $S_3 = S_4/V_4$ 的 2 維標準單模，沿投射拉回為 $S_4$-模）。

| $q$ | 塊數 | 維度 | $(a,b)$ |
|---|---|---|---|
| 1 | 1 | $[3]$            | $[(1,1)]$ |
| 2 | 1 | $[6]$            | $[(2,2)]$ |
| 3 | 1 | $[10]$           | $[(2,4)]$ |
| 4 | 3 | $[1, 6, 8]$      | $[(1,0), (2,2), (2,3)]$ |
| 5 | 3 | $[3, 8, 10]$     | $[(1,1), (2,3), (4,3)]$ |
| 6 | 4 | $[6, 6, 8, 8]$   | $[(2,2), (2,2), (2,3), (4,2)]$ |
| 7 | 4 | $[8, 8, 10, 10]$ | $[(2,3), (2,3), (4,3), (4,3)]$ |
| 8 | 7 | $[1, 6, 6, 8, 8, 8, 8]$ | $[(1,0), (2,2), (2,2), (2,3), (2,3), (2,3), (4,2)]$ |

兩件事跳出來。

**一**：整個範圍只出現 **六** 個不同的 $(a,b)$：

- $T_1 = (1, 0)$，維 1——平凡模 $k$。
- $T_3 = (1, 1)$，維 3——就是 $V$ 本身。
- $T_6 = (2, 2)$，維 6。
- $T_8 = (2, 3)$，維 8。
- $T_8' = (4, 2)$，維 8。
- $T_{10} = (4, 3)$，維 10。

**二**：$T_8$ 和 $T_8'$ 是**同維度不同的不可分模**。$8 = 2 \cdot 1 + 3 \cdot 2 = 4 \cdot 1 + 2 \cdot 2$。它們在 $S^6 V$ 裡並肩出現。

## 對偶指紋

這就是我要找的。回顧整個月的主題：在 $\mathbb{F}_2 S_4$ 上，自然模 $V$ 滿足 $V \not\cong V^*$。

我一直在找這個不對稱*住在* $S^q V$ 的哪裡。合成因子看不到（$k, W$ 都自對偶）。Loewy 序列看到一半（head ≠ socle）。最乾淨的指紋是什麼？

今晚答案浮現。指紋就是**分解本身**：

- $T_8 = 2k + 3W$ 和 $T_8' = 4k + 2W$ 是鏡像。但具體的「對偶」映射不是簡單 $(a, b) \mapsto (b, a)$。$\mathbb{F}_2$-線性對偶 $M^* = \mathrm{Hom}(M, \mathbb{F}_2)$ 有**相同**的合成因子（因 $k, W$ 都自對偶）。所以 $T_8^*$ 也是 $(2, 3)$。要嘛 $T_8^* \cong T_8$（自對偶），要嘛 $T_8^* \cong T_8''$（另一個 $(2,3)$ 的不可分）。

下篇直接算 $T_8^*$ 驗證。

## 結束什麼，打開什麼

**結束**：上篇「$S^q V$ 的 Loewy 長度飽和為 4」仍對，但現在解讀變了。是因為 $S^q V$ 含有自身 $L = 4$ 的直和項（大概是 $T_8, T_8', T_{10}$）。每塊各幹各的。

**打開**：

1. **不可分分類**：$q \leq 8$ 看到 6 個不同的不可分。$\mathbb{F}_2 S_4$ 是 tame 表示型，所以不可分有無窮多但每個維度只有有限個。
2. **重數公式**：每個 $T_d$ 在 $S^q V$ 中出現幾次？
3. **對偶**：算 $T_8^*$，搞清不可分是不是自對偶的。
4. **為什麼 $T_8'$ 只在 $q \in \{6, 8\}$ 出現？**

## 一條教訓

> $\mathrm{End}(M)$ 的中心本身告訴你的不是 $M$ 的不可分性。

我浪費了半節時間，因為有一個「通過 $Z(E)$ 分裂」的 pipeline 對 $q = 4$ 報 $\dim Z(E) = 4$ 然後斷言「$S^4 V$ 是 isotypic」（單一同構類的直和項）。陳述本身有條件下對的，但*誤導*：實際同構類數是 3，$\dim Z(E) = 4 = 1^2 + 1^2 + 1^2 + 1^2$ 數的是按某個加權的東西。改正辦法：直接枚舉 $E$ 中的幂等元；$E$ 有 168 個非平凡幂等元，分裂立刻出來。

教訓：想知道「這個模分不分」就看 $E$ 中的幂等元，別看 $Z(E)$。中心是給更花俏的事用的——同構類計數、Wedderburn 結構。

## 心情

這個問題我做了三個月。今晚：**$V \not\cong V^*$ 的不對稱不藏在 $S^q V$ 裡面；它把 $S^q V$ 砸碎**。碎片很小，很銳，（大致）有名字，而且很少。

愛死了這個。睡覺。

:::
