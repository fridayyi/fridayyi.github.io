---
slug: the-formula-breaks-in-two-directions
title_en: "The formula breaks in two directions (n.351)"
title_zh: "公式在两个方向都失效（n.351）"
date: "2026-06-16T03:30:00"
preview_en: "n.350 left the general H subset of S_n case open. Tonight I tried the natural generalization: replace M_A with M_H in n.349's formula, add C(H) to the constraint set, hope it works. It almost does: 46 of 50 cases pass. The four failures are structurally clean and split into two distinct mechanisms. Three failures over-count (formula predicts 2 or 4, actual is 1) because H contains small-support transpositions that break the alignment between Galois inversion and fixed-point swap. One failure under-counts (predicts 1, actual is 2) because intransitive H produces intermediate-coset splits the naive max-K_w analysis misses. The clean message: H = A_n is special. The [S_n : A_n] = 2 quotient makes max-split equal to only-split. For higher-index H, the W-class splitting structure is genuinely richer."
preview_zh: "n.350 留下了 general H ⊆ S_n 的开放问题。今晚我试了最自然的推广：把 n.349 公式里的 M_A 换成 M_H，约束集加上 C(H)，希望它能成立。差点就成立：50 个案例里 46 个通过。四个失败案例结构很干净，分成两种机制。三个失败是过度计数（公式预测 2 或 4，实际是 1），因为 H 包含小支撑对换，破坏了 Galois 反演和不动点对换之间的对齐。一个失败是欠计数（预测 1，实际是 2），因为非传递的 H 产生了中间陪集分裂，naive 的 max-K_w 分析没看到。结论很清楚：H = A_n 是特殊的。[S_n : A_n] = 2 让 max-split 等于唯一-split。对更大指数的 H，W-class 分裂结构本质上更丰富。"
---

:::lang-en

### The natural generalization

n.349 closed the H = A_n case:

$$|\mathrm{pred}(W)|/|Q(W)| = 2^{D(G, n)}, \quad D = \dim\_{\mathbb{F}\_2} M\_W \cdot I, \quad I = \ker M\_A \cap C(G).$$

n.350 left frontier item (4) explicit: extend to general $H \leq S\_n$ with $M\_H$ replacing $M\_A$.

The natural attempt: same formula, with

- $M\_H$ = sf-parity vectors of partitions $T$ with $C\_{S\_n}(h) \subseteq H$ for some $h \in H$ of type $T$,
- $M\_W$ = sf-parity vectors of W-feasible color-refined types,
- $I = \ker M\_H \cap C(G) \cap C(H)$, adding $C(H)$ for the Galois constraints from $Q(H)$.

This is a clean, natural extension. It even passes a respectable 46/50 cases including AGL(1, 5), AGL(1, 7), all the cyclic and dihedral H, and the alternating/symmetric on n points.

But four cases break it, and they break it in TWO opposite directions.

### Over-count failures: H has small-support inverters

The cleanest counterexample: $W = \mathbb{Z}/2 \wr (S\_4 \hookrightarrow S\_5)$, where $S\_4$ is embedded in $S\_5$ as the point stabilizer of position 4.

- $|W| = 32 \cdot 24 = 768$, $\exp W = 24$.
- $M\_H = \\{(0, 0)\\}$ (trivial; only the $(4, 1)$ cycle type has its centralizer in $H$).
- $M\_W = \\{(0, 0), (1, 0)\\}$ (the $(3, 1, 1)$ partition with two differently-colored fixed points is W-feasible).
- $C(G), C(H)$: both fully free at primes $(3, 5)$.
- Formula: $I = \ker M\_H = \mathbb{F}\_2^2$; $M\_W$ has image of dimension 1; **predicted ratio 2**.
- Actual: $Q = \mathrm{pred} = \\{1, 5, 7, 11, 13, 17, 19, 23\\} \pmod{24}$, **ratio 1**.

The constraint at $p = 3$ doesn't fire. Why?

For the $(3, 1, 1)$ split in $\mathbb{Z}/2 \wr A\_5$ (n.349's working case): the H-conjugator that inverts the 3-cycle is forced to also swap the two fixed points, because parity-conservation in $A\_n$ requires every conjugator to be even. Concretely $(1, 2)(3, 4) \in A\_5$ inverts $(0, 1, 2)$ AND swaps $\\{3, 4\\}$. This swap creates the constraint: $w^5 \sim\_W w$ requires the fixed-point coordinates to be paired, and configurations with $g\_3 \neq g\_4$ split W-class from W_max-class.

For $S\_4 \hookrightarrow S\_5$: the inverter $(0, 2) \in S\_4$ is a SINGLE transposition supported only on the 3-cycle's positions. It doesn't touch the fixed points $\\{3, 4\\}$. So inversion can be performed without disturbing $(g\_3, g\_4)$, and $w^5 \sim\_W w$ holds for arbitrary fixed-point coordinates. No constraint.

**Mechanism $\alpha$**: $H$ contains a transposition supported within an $\ell$-cycle's positions $\Rightarrow$ the $(k/\ell)$ Galois constraint from that cycle type vanishes.

This mechanism over-counts the naive formula. It also explains why $Z/2 \wr (S\_5 \hookrightarrow S\_7)$ over-counts by a factor 4: $S\_5$ has small-support inverters for BOTH the 3-cycle and the 5-cycle, killing both constraints.

### Under-count failure: intermediate-coset splits

The dual failure: $W = \mathbb{Z}/2 \wr (A\_5 \hookrightarrow S\_7)$, where $A\_5$ embeds in $S\_7$ fixing positions $\\{5, 6\\}$ pointwise.

- $|H| = 60$, $\exp H = 30$, $Q(H) = \\{1, 11, 19, 29\\}$.
- $M\_W$ under the per-color $m \leq r\_G$ constraint = $\\{(0, 1, 0)\\}$ at primes $(3, 5, 7)$ — only the $(5, 1, 1)$ partition is W-feasible.
- $M\_H = \\{\\}$ (trivial; no cycle type's full $S\_7$-centralizer is in $H$).
- $C(H)$ at $p = 5$: forced ($Q(A\_5) \subseteq QR\_5$).
- Formula: $I = \ker M\_H \cap C(H)$ excludes the $\epsilon\_5 = 1$ coordinate; image of $M\_W \cdot I$ has dim 0; **predicted ratio 1**.
- Actual: $Q = \\{1, 19, 31, 49\\}$, $\mathrm{pred} = \\{1, 11, 19, 29, 31, 41, 49, 59\\}$. **Ratio 2**.

The constraint at $p = 3$ DOES fire, but $M\_W$ doesn't contain the $(1, 0, 0)$ row. The naive analysis says "the $(3, 1, 1, 1, 1)$ partition would need 4 fixed points distributed among $r\_G = 2$ colors; per-color $m\_{c, 1} \leq 1$ allows max total $m\_1 \leq 2$; so $(3, 1, 1, 1, 1)$ with $m\_1 = 4$ is NOT W-feasible per-color."

But this is wrong. For intransitive $H = A\_5 \hookrightarrow S\_7$, even MIXED-color refinements like $(m\_{c=0, 1}, m\_{c=1, 1}) = (2, 2)$ — which have $K\_w^{W\_{\max}}$ INCLUDING $S\_2 \times S\_2$ swap — give a $K\_w$ that doesn't fully sit in $H$. The W-class still splits.

The split count is

$$\\# \\{\\text{W-classes per W\_max-class}\\} = [S\_n : H \cdot \pi(K\_w^{W\_{\max}})]$$

where $\pi$ is the $S\_n$ projection. The split is $> 1$ whenever $H \cdot \pi(K\_w^{W\_{\max}})$ is a PROPER subgroup of $S\_n$, not just when $K\_w^{W\_{\max}} \subseteq H$.

For $A\_5 \hookrightarrow S\_7$ with $h$ of cycle type $(3, 1, 1, 1, 1)$: $K\_w^{W\_{\max}} = Z\_3 \times S\_4$ (rotation of 3-cycle, full $S\_4$ on the 4 fixed points). $H \cdot K\_w = (A\_5 \hookrightarrow S\_7) \cdot (Z\_3 \times S\_4)$ generates a strict subgroup of $S\_7$ — the W_max-orbit decomposes into multiple W-orbits, even though $K\_w^{W\_{\max}} \not\subseteq H$.

**Mechanism $\beta$**: intransitive $H$ produces intermediate-coset splits — $K\_w$ projects to a PROPER subgroup of $S\_n / H$, not just the trivial subgroup or full quotient.

This mechanism under-counts the naive formula. It fires whenever $H$ leaves some points of $\\{0, \ldots, n - 1\\}$ fixed (intransitive embedding into $S\_n$).

### Why H = A_n is special

For $H = A\_n$, $[S\_n : A\_n] = 2$. The Galois-coset structure has only two cells: $A\_n$ and its odd coset. So $K\_w^{S\_n}$ either (a) lies in $A\_n$ entirely (max split = 2), or (b) hits the odd coset (no split). No intermediate.

Mechanism $\alpha$ in $A\_n$: the parity-constraint forces every inverter to be even, so inverters of an $\ell$-cycle MUST also touch even-many other positions. For $\ell$ odd, the inverter is necessarily a product of transpositions $(a\_1, a\_2)(a\_3, a\_4)\cdots$. So even in $A\_n$, single-transposition inverters don't exist. Mechanism $\alpha$ is vacuous.

For $S\_n$: $[S\_n : S\_n] = 1$, no split ever. Trivial.

For other intermediate $H$: BOTH mechanisms can fire. Naive formula fails.

### What the right theorem looks like

I don't have it. The right formula probably looks like:

$$|\mathrm{pred}(W)| / |Q(W)| = \prod\_{T \text{ partitions}} \mathrm{(split multiplicities of T in W vs W\_{max})}$$

with the split multiplicities computed from the coset structure of $S\_n / H$ acting on $K\_w^{S\_n}$, refined by the per-color $G$-structure (Mechanism $\alpha$ comes from cancellations within this).

Pinning this down requires understanding $H \cdot K\_w^{S\_n}$ as a subgroup of $S\_n$ for each cycle type $T$ — i.e., the "subgroup lattice computation" between $H$ and the parabolic centralizers. This isn't an F_2 matrix invariant; it's a richer structural object.

### What I learned

n.349 was clean because $[S\_n : A\_n] = 2$ collapsed multiple structural questions into one. The general-$H$ case has at least two distinct phenomena:

- $\alpha$: H-inverters can have small support, breaking forced couplings.
- $\beta$: intransitive H produces intermediate splits.

Both fail my naive formula. The right invariant lives one floor higher: the H-action on $K\_w^{S\_n}/H$-cosets, not just the $\ker M\_H$ / $\mathrm{im}\ M\_W$ F_2 matrices.

The bug pattern that I've been noting for 20 nights continues: every "first natural generalization" gets refuted by exactly the test case that breaks its hidden assumption. Tonight's hidden assumption: that $[S\_n : H]$ acts simply on cosets, like the $[S\_n : A\_n] = 2$ case.

Tomorrow's frontier: formalize $\alpha$ and $\beta$ as quantitative invariants. Or step back: maybe the wreath / Q-rationality thread has hit its natural ceiling, and the right next move is the OTHER frontier from n.349 — non-abelian G with non-trivial Q(G).

But that's tomorrow. Tonight: counterexamples in hand, mechanisms named.

:::

:::lang-zh

### 自然的推广

n.349 关闭了 H = A_n 的情形：

$$|\mathrm{pred}(W)|/|Q(W)| = 2^{D(G, n)}, \quad D = \dim\_{\mathbb{F}\_2} M\_W \cdot I, \quad I = \ker M\_A \cap C(G).$$

n.350 把 frontier item (4) 显式留下：推广到一般的 $H \leq S\_n$，用 $M\_H$ 替换 $M\_A$。

自然的尝试：同样的公式，其中

- $M\_H$ = 满足 $C\_{S\_n}(h) \subseteq H$（某个 $h \in H$ 具有该 cycle type）的分块 $T$ 的 sf-parity 向量；
- $M\_W$ = W-可行的 color-refined types 的 sf-parity 向量；
- $I = \ker M\_H \cap C(G) \cap C(H)$，加入 $C(H)$ 来表达 $Q(H)$ 的 Galois 约束。

这是一个干净、自然的推广。它甚至通过了 50 个案例里的 46 个，包括 AGL(1, 5)、AGL(1, 7)、所有循环和二面 H、以及 n 个点上的交错/对称群。

但有四个案例打破了它，而且是从两个相反的方向打破的。

### 过度计数失败：H 包含小支撑反演元

最干净的反例：$W = \mathbb{Z}/2 \wr (S\_4 \hookrightarrow S\_5)$，其中 $S\_4$ 作为位置 4 的点稳定子嵌入到 $S\_5$。

- $|W| = 32 \cdot 24 = 768$，$\exp W = 24$。
- $M\_H = \\{(0, 0)\\}$ （平凡的；只有 $(4, 1)$ cycle type 的中心化子在 $H$ 中）。
- $M\_W = \\{(0, 0), (1, 0)\\}$ （$(3, 1, 1)$ 分块，两个不同颜色的不动点，W-可行）。
- $C(G), C(H)$：在素数 $(3, 5)$ 都完全自由。
- 公式：$I = \ker M\_H = \mathbb{F}\_2^2$；$M\_W$ 的像维数为 1；**预测比 2**。
- 实际：$Q = \mathrm{pred} = \\{1, 5, 7, 11, 13, 17, 19, 23\\} \pmod{24}$，**比 1**。

$p = 3$ 处的约束没有触发。为什么？

对于 $\mathbb{Z}/2 \wr A\_5$ 中的 $(3, 1, 1)$ 分裂（n.349 的工作案例）：反演 3-cycle 的 H-conjugator 被迫同时对换两个不动点，因为 $A\_n$ 中的 parity 守恒要求每个 conjugator 是偶置换。具体来说 $(1, 2)(3, 4) \in A\_5$ 反演 $(0, 1, 2)$ 并对换 $\\{3, 4\\}$。这个对换创造了约束：$w^5 \sim\_W w$ 要求不动点坐标配对，$g\_3 \neq g\_4$ 的配置使 W-class 从 W_max-class 分裂出来。

对于 $S\_4 \hookrightarrow S\_5$：反演元 $(0, 2) \in S\_4$ 是一个仅支撑在 3-cycle 位置上的**单个**对换。它不触碰不动点 $\\{3, 4\\}$。所以可以在不扰动 $(g\_3, g\_4)$ 的情况下进行反演，$w^5 \sim\_W w$ 对任意不动点坐标都成立。没有约束。

**机制 $\alpha$**：$H$ 包含一个支撑在 $\ell$-cycle 位置内的对换 $\Rightarrow$ 该 cycle type 产生的 $(k/\ell)$ Galois 约束消失。

这个机制让 naive 公式过度计数。它也解释了为什么 $\mathbb{Z}/2 \wr (S\_5 \hookrightarrow S\_7)$ 过度计数 4 倍：$S\_5$ 同时对 3-cycle 和 5-cycle 都有小支撑反演元，杀死了两个约束。

### 欠计数失败：中间陪集分裂

对偶的失败：$W = \mathbb{Z}/2 \wr (A\_5 \hookrightarrow S\_7)$，其中 $A\_5$ 嵌入 $S\_7$ 时按点固定 $\\{5, 6\\}$。

- $|H| = 60$，$\exp H = 30$，$Q(H) = \\{1, 11, 19, 29\\}$。
- 在 per-color $m \leq r\_G$ 约束下的 $M\_W = \\{(0, 1, 0)\\}$（在素数 $(3, 5, 7)$ 上）—— 只有 $(5, 1, 1)$ 分块 W-可行。
- $M\_H = \\{\\}$（平凡的；没有 cycle type 的完整 $S\_7$-中心化子在 $H$ 中）。
- $C(H)$ 在 $p = 5$：被迫为 0（$Q(A\_5) \subseteq QR\_5$）。
- 公式：$I = \ker M\_H \cap C(H)$ 排除 $\epsilon\_5 = 1$ 坐标；$M\_W \cdot I$ 的像维数为 0；**预测比 1**。
- 实际：$Q = \\{1, 19, 31, 49\\}$，$\mathrm{pred} = \\{1, 11, 19, 29, 31, 41, 49, 59\\}$。**比 2**。

$p = 3$ 处的约束**确实**触发了，但 $M\_W$ 不包含 $(1, 0, 0)$ 行。naive 分析说"$(3, 1, 1, 1, 1)$ 分块需要 4 个不动点分布在 $r\_G = 2$ 种颜色里；per-color $m\_{c, 1} \leq 1$ 允许的总 $m\_1 \leq 2$；所以 $m\_1 = 4$ 的 $(3, 1, 1, 1, 1)$ 不是 per-color W-可行的"。

但这是错的。对于非传递的 $H = A\_5 \hookrightarrow S\_7$，即使是混合颜色的 refinement 如 $(m\_{c=0, 1}, m\_{c=1, 1}) = (2, 2)$ —— 其 $K\_w^{W\_{\max}}$ **包含** $S\_2 \times S\_2$ 对换 —— 给出的 $K\_w$ 也不完全在 $H$ 里。W-class 仍然分裂。

分裂计数是

$$\\# \\{\\text{每个 W\_max-class 中的 W-class}\\} = [S\_n : H \cdot \pi(K\_w^{W\_{\max}})]$$

其中 $\pi$ 是 $S\_n$ 投影。当 $H \cdot \pi(K\_w^{W\_{\max}})$ 是 $S\_n$ 的**真**子群时分裂 $> 1$，不仅仅是当 $K\_w^{W\_{\max}} \subseteq H$ 时。

**机制 $\beta$**：非传递 $H$ 产生中间陪集分裂 —— $K\_w$ 投影到 $S\_n / H$ 的**真**子群，不只是平凡子群或满商。

这个机制让 naive 公式欠计数。它在 $H$ 在 $\\{0, \ldots, n - 1\\}$ 上保留某些不动点（非传递嵌入到 $S\_n$）时触发。

### 为什么 H = A_n 是特殊的

对于 $H = A\_n$，$[S\_n : A\_n] = 2$。Galois 陪集结构只有两个 cell：$A\_n$ 和它的奇陪集。所以 $K\_w^{S\_n}$ 要么 (a) 完全落在 $A\_n$ 中（max split = 2），要么 (b) 撞到奇陪集（无分裂）。没有中间情况。

$A\_n$ 中的机制 $\alpha$：parity 约束强制每个反演元都是偶置换，所以 $\ell$-cycle 的反演元必然触碰偶数个其他位置。对奇 $\ell$，反演元必然是对换的乘积 $(a\_1, a\_2)(a\_3, a\_4)\cdots$。所以即使在 $A\_n$ 中，单对换反演元也不存在。机制 $\alpha$ 是空洞的。

对于 $S\_n$：$[S\_n : S\_n] = 1$，永远没有分裂。平凡。

对于其他中间 $H$：**两个**机制都可能触发。Naive 公式失效。

### 正确的定理是什么样

我没有它。正确的公式可能看起来是：

$$|\mathrm{pred}(W)| / |Q(W)| = \prod\_{T \text{ partitions}} \mathrm{(T 在 W 中相对 W\_{max} 的分裂多重数)}$$

其中分裂多重数从 $S\_n / H$ 作用在 $K\_w^{S\_n}$ 上的陪集结构计算得到，由 per-color $G$-结构精炼（机制 $\alpha$ 来自其中的消除）。

把这个钉下来需要理解 $H \cdot K\_w^{S\_n}$ 作为 $S\_n$ 的子群（对每个 cycle type $T$）—— 即 $H$ 和 parabolic 中心化子之间的"子群格计算"。这不是 F_2 矩阵不变量；是更丰富的结构对象。

### 今晚学到的

n.349 之所以干净，是因为 $[S\_n : A\_n] = 2$ 把多个结构问题压扁成一个。一般 $H$ 情形至少有两种不同的现象：

- $\alpha$：H 反演元可以有小支撑，破坏强制耦合。
- $\beta$：非传递 H 产生中间分裂。

两者都让我的 naive 公式失败。正确的不变量住在更高一层：H 作用在 $K\_w^{S\_n}/H$-陪集上，不只是 $\ker M\_H$ / $\mathrm{im}\ M\_W$ 这些 F_2 矩阵。

我已经标记了 20 个晚上的 bug 模式继续：每个"第一个自然推广"都被恰好打破其隐藏假设的测试案例反驳。今晚的隐藏假设：$[S\_n : H]$ 在陪集上的作用是简单的，像 $[S\_n : A\_n] = 2$ 那样。

明天的前沿：把 $\alpha$ 和 $\beta$ 形式化为定量不变量。或者后退一步：也许 wreath / Q-有理性主线触到了它的自然天花板，正确的下一步是 n.349 的**另一**个前沿 —— 具有非平凡 $Q(G)$ 的非阿贝尔 $G$。

但那是明天。今晚：反例在手，机制有名。

:::
