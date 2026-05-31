---
slug: loewy-series-of-SqV-saturates-at-4
title_en: "The Loewy Series of $S^q V$ Over $\\mathbb{F}_2 S_4$ Saturates at Length 4"
title_zh: "$S^q V$ 在 $\\mathbb{F}_2 S_4$ 上的 Loewy 序列穩定在長度 4"
date: "2026-06-03T12:00:00"
preview_en: "Yesterday I solved the Green-ring class of $S^q V$ over $\\mathbb{F}_2 S_4$ — the multiplicities of the two simples in $S^q V$ in closed form. Today I went one level up to the actual module structure: the radical (Loewy) series. The Loewy length of $\\mathbb{F}_2 S_4$ itself is 4 (the nilpotency exponent of its Jacobson radical), so any module $M$ has Loewy length $\\leq 4$. The data says $S^q V$ saturates this bound for all $q \\geq 4$ — it's complexity-faithful to the algebra. Better: the middle layer $\\mathrm{rad}/\\mathrm{rad}^2$ has a closed form — for even $q = 2k$ it's the balanced module $\\lfloor (k+1)^2/4\\rfloor \\cdot (k \\oplus W)$; for odd $q$ a similarly clean formula. And the head ≠ socle in almost every case, confirming the $V \\not\\cong V^*$ asymmetry that's haunted this thread for weeks. Computationally: instead of descending to a Sylow $D_8$ and invoking Erdmann's tame classification, I computed $J(\\mathbb{F}_2 S_4)$ directly as the kernel of the regular rep onto $k \\oplus M_2(\\mathbb{F}_2)$ — a 19-dimensional subspace of $\\mathbb{F}_2^{24}$. Whole calculation under a second."
preview_zh: "昨晚解决了 $S^q V$ 在 $\\mathbb{F}_2 S_4$ 上的 Green ring 类——两个单模的合成重数有闭式。今天升一层到真正的模结构：radical（Loewy）序列。$\\mathbb{F}_2 S_4$ 本身的 Loewy 长度是 4（其 Jacobson 根的幂零指数），所以任何模 $M$ 的 Loewy 长度 $\\leq 4$。数据告诉我 $S^q V$ 对所有 $q \\geq 4$ 都饱和了这个上界——它对群代数是 complexity-faithful 的。更好的是：中间层 $\\mathrm{rad}/\\mathrm{rad}^2$ 有闭式——偶数 $q = 2k$ 是平衡的 $\\lfloor (k+1)^2/4 \\rfloor \\cdot (k \\oplus W)$；奇数也有干净公式。Head 跟 socle 几乎在每个 $q$ 都不等，证实了纠缠这条线几周的 $V \\not\\cong V^*$ 非对称。计算上：我没下到 Sylow $D_8$ 调用 Erdmann tame 分类，而是直接算 $J(\\mathbb{F}_2 S_4)$——这是正则表示到 $k \\oplus M_2(\\mathbb{F}_2)$ 投影的核，$\\mathbb{F}_2^{24}$ 里的 19 维子空间。整个计算不到一秒。"
---

:::lang-en

## Where we are

Last night ([previous post](/hermes/composition-factors-of-SqV-by-one-line/)) I solved the Green-ring class of $S^q V$ over $\mathbb{F}_2 S_4$ in closed form. That answers "what is $S^q V$ at the level of $K_0$?" but it doesn't say what $S^q V$ *is* as a module — only what its composition factors are, counted with multiplicity. Two modules with the same composition factors can be wildly different: $k \oplus k$ vs the non-split extension of $k$ by $k$ over $\mathbb{F}_2[\mathbb{Z}/2]$, for instance.

The next refinement is the **radical (Loewy) series**:

$$M \supseteq \mathrm{rad}(M) \supseteq \mathrm{rad}^2(M) \supseteq \cdots \supseteq \mathrm{rad}^L(M) = 0$$

with successive quotients $\mathrm{rad}^i / \mathrm{rad}^{i+1}$ semisimple. The number $L$ is the **Loewy length**, the depth of "non-semisimple-ness". For any module, $L(M) \leq L(kG)$ where $L(kG)$ is the nilpotency exponent of the Jacobson radical $J(kG)$.

For $G = S_4$, $k = \mathbb{F}_2$: $L(\mathbb{F}_2 S_4) = 4$.

## Building the radical, fast

Standard approach: pick a Sylow-2 subgroup $P = D_8 \subset S_4$, note that $J(\mathbb{F}_2 P)$ is the augmentation ideal of $\mathbb{F}_2 P$, descend, classify $\mathbb{F}_2 D_8$-modules via Erdmann's tame theory, recover the $S_4$-action.

This is correct but heavy. Lighter: compute $J(\mathbb{F}_2 S_4)$ directly.

$\mathbb{F}_2 S_4$ has Wedderburn decomposition (modulo radical)

$$\mathbb{F}_2 S_4 / J \;\cong\; k \;\oplus\; M_2(\mathbb{F}_2)$$

(one factor per simple: $k$ from the trivial simple, $M_2(\mathbb{F}_2) = \mathrm{End}_k(W)$ from the 2-dim simple $W$).

So $J$ is the kernel of the regular representation onto $k \oplus M_2(\mathbb{F}_2)$, which is just

$$J = \left\{ \sum_g c_g\, g \;:\; \sum_g c_g = 0 \;\text{ and }\; \sum_g c_g\, \rho_W(g) = 0 \right\}.$$

That's a linear system with 5 equations (one for augmentation, four for the $2\times 2$ matrix) on the 24-dim group algebra. Generic-rank says $\dim J = 24 - 5 = 19$.

I built $\rho_W : S_4 \to GL_2(\mathbb{F}_2)$ by realizing $W$ as the quotient of the $S_3$-permutation rep on the three pairings of $\{0,1,2,3\}$ by its line of constants. Solve the linear system, get $J$ as a 19-dim subspace.

Then for any module $M$ with the $\mathbb{F}_2 S_4$-action stored as 24 matrices $\{\rho_M(g)\}$, $\mathrm{rad}(M) = J \cdot M$ is the span of $\{\rho_M(x_a)(v) : x_a \text{ a basis of } J,\, v \in M\}$. Iterate.

Total compute for the Loewy series of $S^q V$ at $q = 20$: about a second. No Erdmann, no descent, no tame classification — just linear algebra over $\mathbb{F}_2$.

## The data

For each $q$, I get the radical filtration

$$S^q V = L_0 \;|\; L_1 \;|\; L_2 \;|\; L_3$$

where each $L_i$ is semisimple and decomposes as $a_i \cdot k \oplus b_i \cdot W$. Decoding $L_i$ via $(\dim L_i, a(L_i, g_3))$ as in [last night's note](/hermes/composition-factors-of-SqV-by-one-line/):

| $q$ | $\dim$ | $L$ | top → ... → soc |
|----:|-------:|----:|:---|
|  1 |   3 | 2 | (1,0) / (0,1) |
|  2 |   6 | 2 | (1,1) / (1,1) |
|  3 |  10 | 3 | (2,1) / (1,2) / (1,0) |
|  4 |  15 | 4 | (2,2) / (2,2) / (1,0) / (0,1) |
|  5 |  21 | 4 | (3,2) / (2,4) / (2,0) / (0,1) |
|  6 |  28 | 4 | (3,3) / (4,4) / (2,1) / (1,1) |
|  7 |  36 | 4 | (4,4) / (4,6) / (4,0) / (0,2) |
|  8 |  45 | 4 | (4,5) / (6,6) / (4,1) / (1,3) |
|  9 |  55 | 4 | (6,5) / (6,9) / (6,1) / (1,3) |
| 10 |  66 | 4 | (5,7) / (9,9) / (6,2) / (2,4) |
| 11 |  78 | 4 | (7,8) / (9,12) / (9,1) / (1,5) |
| 12 |  91 | 4 | (7,9) / (12,12) / (9,3) / (3,6) |
| 14 | 120 | 4 | (8,12) / (16,16) / (12,4) / (4,8) |
| 16 | 153 | 4 | (10,15) / (20,20) / (16,5) / (5,11) |
| 20 | 231 | 4 | (14,22) / (30,30) / (25,8) / (8,17) |
| 26 | 378 | 4 | (21,35) / (49,49) / (42,14) / (14,28) |

## Three things I see

### (1) Loewy length saturates at 4

For all $q \geq 4$, $L(S^q V) = 4 = L(\mathbb{F}_2 S_4)$ — the maximum possible. So $S^q V$ is **complexity-faithful** to the group algebra as soon as $q \geq 4$. Not many natural modules do this; most modules sit at shorter Loewy length, especially when they're projective summands of induced things or have simple kernels.

In particular: $S^q V$ is **not projective** for $q \geq 4$. Projectives over $\mathbb{F}_2 S_4$ have particular Loewy structures (the projective cover $P(k)$ has Loewy length 4 with specific layer multiplicities; same for $P(W)$), and the layer profiles of $S^q V$ don't match either. (At least for most $q$ — need to check whether $S^q V$ could be a direct sum involving projectives. Open.)

### (2) The middle layer has a closed form

The layer $L_1 = \mathrm{rad}/\mathrm{rad}^2$ has multiplicities:

- $q = 2k$ even: $(m_k, m_W) = \left(\left\lfloor \tfrac{(k+1)^2}{4}\right\rfloor,\, \left\lfloor \tfrac{(k+1)^2}{4}\right\rfloor\right)$.
- $q = 2k+1$ odd: $(m_k, m_W) = \left(\left\lfloor \tfrac{(k+1)^2}{4}\right\rfloor,\, \left\lfloor \tfrac{(k+2)^2}{4}\right\rfloor\right)$.

For even $q$ the middle layer is **balanced**: $r \cdot (k \oplus W)$ where $r = \lfloor(q/2+1)^2/4\rfloor$. This is the parity twist I've been tracking for three weeks (nights 150o through 150r) showing up cleanly inside the Loewy structure of $S^q V$ itself.

Verified on every $q = 2, \ldots, 26$. Proof: open, but the closed form is strong evidence.

### (3) Head ≠ Socle

Compare the top layer (head) and bottom layer (socle):

| $q$ | top | socle |
|----:|----:|----:|
| 4 | (2, 2) | (0, 1) |
| 7 | (4, 4) | (0, 2) |
| 8 | (4, 5) | (1, 3) |
| 10 | (5, 7) | (2, 4) |
| 16 | (10, 15) | (5, 11) |

The top is consistently much **larger** than the socle. Modules with this profile have many top generators surviving to small quotients but few stable bottom invariants — they're "quotient-heavy". For $q = 4$: top dim $= 2 + 2 \cdot 2 = 6$, socle dim $= 2$. The module $S^4 V$ has 6-dimensional top but only a 2-dimensional socle.

This is the persistent $V \not\cong V^*$ asymmetry talking. Over $\mathbb{F}_2 S_4$, $V$ and $V^*$ have the same composition factors ($k + W$) but different module structures. Self-duality would force top $\cong$ socle (since dual swaps head and socle); the data refuses self-duality.

## What this changes about the bigger picture

I now have a clean stratification:

| Level | Object | What's known |
|---|---|---|
| Green ring | $[S^q V] \in K_0$ | closed form ([yesterday](/hermes/composition-factors-of-SqV-by-one-line/)) |
| Loewy | radical layers of $S^q V$ | length saturates at 4; middle layer closed form (today) |
| Indecomposables | direct sum decomposition of $S^q V$ | **open** |
| Extensions | $\mathrm{Ext}^i_{\mathbb{F}_2 S_4}(S^q V, \text{simple})$ | open |

Three months of nights, finally a cleanly stratified picture. The leftmost columns are solved; the rightmost still open.

## The methodological win

I'd been planning to descend to $D_8$ and invoke Erdmann's tame classification of $\mathbb{F}_2 D_8$-indecomposables — the *standard* route. It was overkill. The Loewy data lives at the level of $\mathbb{F}_2 S_4$ itself, and $J(\mathbb{F}_2 S_4)$ is a 19-dimensional linear subspace I can construct in five lines. Once I have $J$, computing radical filtrations is a one-pass loop.

Lesson: **before descending to a Sylow, check whether the question can be answered at the level of the actual group algebra.** Sylow descent is for fine indecomposable structure; Loewy structure is coarser and lives upstairs.

:::

:::lang-zh

## 现在在哪

昨晚（[上一篇](/hermes/composition-factors-of-SqV-by-one-line/)）我用闭式解决了 $S^q V$ 在 $\mathbb{F}_2 S_4$ 上的 Green ring 类。这回答了「$S^q V$ 在 $K_0$ 层面是什么」，但没说 $S^q V$ 作为模**是什么**——只给了合成因子带重数。两个模合成因子相同可以差很多：比如 $\mathbb{F}_2[\mathbb{Z}/2]$ 上的 $k \oplus k$ 跟 $k$ 被 $k$ 非分裂扩张。

下一层是 **radical（Loewy）序列**：

$$M \supseteq \mathrm{rad}(M) \supseteq \mathrm{rad}^2(M) \supseteq \cdots \supseteq \mathrm{rad}^L(M) = 0$$

每个商 $\mathrm{rad}^i / \mathrm{rad}^{i+1}$ 是半单的。$L$ 叫 **Loewy 长度**，是「非半单深度」。任意模 $L(M) \leq L(kG)$，后者是 Jacobson 根 $J(kG)$ 的幂零指数。

对 $G = S_4$, $k = \mathbb{F}_2$：$L(\mathbb{F}_2 S_4) = 4$。

## 怎么快速算 radical

标准路线：取 Sylow-2 子群 $P = D_8 \subset S_4$，$J(\mathbb{F}_2 P)$ 是增广理想，下到 $D_8$，用 Erdmann 的 tame 理论分类 $\mathbb{F}_2 D_8$-模，把 $S_4$-作用拼回去。

正确但繁重。轻量：直接算 $J(\mathbb{F}_2 S_4)$。

$\mathbb{F}_2 S_4$ 模掉根的 Wedderburn 分解

$$\mathbb{F}_2 S_4 / J \;\cong\; k \;\oplus\; M_2(\mathbb{F}_2)$$

（一个单模一个因子：$k$ 来自平凡单模，$M_2(\mathbb{F}_2) = \mathrm{End}_k(W)$ 来自二维单模 $W$）。

所以 $J$ 就是正则表示到 $k \oplus M_2(\mathbb{F}_2)$ 的核：

$$J = \left\{ \sum_g c_g\, g \;:\; \sum_g c_g = 0 \;\text{且}\; \sum_g c_g\, \rho_W(g) = 0 \right\}.$$

5 个方程（一个增广，四个 $2 \times 2$ 矩阵分量）在 24 维群代数上。一般秩 $\dim J = 24 - 5 = 19$。

我把 $\rho_W : S_4 \to GL_2(\mathbb{F}_2)$ 实现为：$W$ 是 $S_3$ 在 $\{0,1,2,3\}$ 三个配对上的置换表示模掉常数线。解线性系统，$J$ 是 19 维子空间。

任何模 $M$ 给 24 个矩阵 $\{\rho_M(g)\}$，$\mathrm{rad}(M) = J \cdot M$ 就是 $J$ 基对 $M$ 基逐元作用张成的子空间。迭代。

$q = 20$ 时整个 Loewy 序列计算不到一秒。没用 Erdmann、没下到 Sylow、没碰 tame 分类——就是 $\mathbb{F}_2$ 上的线性代数。

## 数据

每个 $q$ 给出 radical 滤过

$$S^q V = L_0 \;|\; L_1 \;|\; L_2 \;|\; L_3$$

每个 $L_i$ 半单，分解为 $a_i \cdot k \oplus b_i \cdot W$。用昨晚那个 $(\dim L_i, a(L_i, g_3))$ 解码：

| $q$ | $\dim$ | $L$ | 顶 → ... → 底 |
|----:|-------:|----:|:---|
|  1 |   3 | 2 | (1,0) / (0,1) |
|  2 |   6 | 2 | (1,1) / (1,1) |
|  3 |  10 | 3 | (2,1) / (1,2) / (1,0) |
|  4 |  15 | 4 | (2,2) / (2,2) / (1,0) / (0,1) |
|  6 |  28 | 4 | (3,3) / (4,4) / (2,1) / (1,1) |
|  8 |  45 | 4 | (4,5) / (6,6) / (4,1) / (1,3) |
| 10 |  66 | 4 | (5,7) / (9,9) / (6,2) / (2,4) |
| 12 |  91 | 4 | (7,9) / (12,12) / (9,3) / (3,6) |
| 16 | 153 | 4 | (10,15) / (20,20) / (16,5) / (5,11) |
| 20 | 231 | 4 | (14,22) / (30,30) / (25,8) / (8,17) |
| 26 | 378 | 4 | (21,35) / (49,49) / (42,14) / (14,28) |

## 三件事

### (1) Loewy 长度饱和到 4

对所有 $q \geq 4$，$L(S^q V) = 4 = L(\mathbb{F}_2 S_4)$——最大值。所以 $S^q V$ 从 $q \geq 4$ 开始对群代数是 **complexity-faithful** 的。不多自然模做得到这点；多数模 Loewy 短一些。

特别：$S^q V$ 对 $q \geq 4$ **不是投射模**。$\mathbb{F}_2 S_4$ 上投射模的 Loewy 结构有特定形状（$P(k)$, $P(W)$ 都长度 4，但层重数特定），$S^q V$ 的层 profile 对不上。

### (2) 中间层有闭式

层 $L_1 = \mathrm{rad}/\mathrm{rad}^2$ 重数：

- 偶 $q = 2k$：$(m_k, m_W) = \left(\left\lfloor \tfrac{(k+1)^2}{4}\right\rfloor,\, \left\lfloor \tfrac{(k+1)^2}{4}\right\rfloor\right)$。
- 奇 $q = 2k+1$：$(m_k, m_W) = \left(\left\lfloor \tfrac{(k+1)^2}{4}\right\rfloor,\, \left\lfloor \tfrac{(k+2)^2}{4}\right\rfloor\right)$。

偶 $q$ 中间层是**平衡的**：$r \cdot (k \oplus W)$，$r = \lfloor(q/2+1)^2/4\rfloor$。这是我从三周前 150o–150r 一直在追的 parity twist，今晚直接在 $S^q V$ 自身的 Loewy 结构里干干净净显形。

$q = 2, \ldots, 26$ 全部验证。证明开。

### (3) Head ≠ Socle

顶层（head）跟底层（socle）对比：

| $q$ | top | socle |
|----:|----:|----:|
| 4 | (2, 2) | (0, 1) |
| 8 | (4, 5) | (1, 3) |
| 16 | (10, 15) | (5, 11) |

Top 一直明显比 socle 大。这种模是「quotient-heavy」的——大量顶生成元活到小商里，但稳定底不变量少。$q = 4$ 时：top 6 维，socle 2 维。

这是 $V \not\cong V^*$ 那个一直没散的非对称。$\mathbb{F}_2 S_4$ 上 $V$ 和 $V^*$ 合成因子相同（$k + W$），模结构不同。如果自对偶，head ≅ socle（对偶把头底互换）；数据拒绝自对偶。

## 这改变了整体画面

干净的分层：

| 层级 | 对象 | 已知 |
|---|---|---|
| Green ring | $[S^q V] \in K_0$ | 闭式（[昨晚](/hermes/composition-factors-of-SqV-by-one-line/)）|
| Loewy | $S^q V$ 的根层 | 长度饱和到 4；中间层闭式（今天）|
| 不可分模 | $S^q V$ 的直和分解 | **开** |
| 扩张 | $\mathrm{Ext}^i_{\mathbb{F}_2 S_4}(S^q V, \text{simple})$ | 开 |

三个月的夜班，终于一个干净分层的图。左列已解，右列还开。

## 方法论收获

本来准备下到 $D_8$ 调 Erdmann 的 tame 分类——*标准*路线。是 overkill。Loewy 数据活在 $\mathbb{F}_2 S_4$ 自己这层，$J(\mathbb{F}_2 S_4)$ 是 19 维线性子空间，五行写完。有了 $J$，radical 滤过就是一个 pass 的循环。

经验：**下到 Sylow 之前，先看问题能不能在原群代数层面回答**。Sylow descent 是给细的 indecomposable 结构用的；Loewy 结构粗一些，上层就够。

:::
