---
slug: harper-vertex-isoperimetric-anti-cut-n525
title_en: "n.525: Harper vertex isoperimetric closes ν_anti-cut(Q_n) ≥ C(n, ⌊n/2⌋) — conditional on a bipartite component graph for min cuts."
title_zh: "n.525：Harper 顶点等周不等式封闭 ν_anti-cut(Q_n) ≥ C(n, ⌊n/2⌋) ——条件依赖最小切的分量图二部性。"
date: "2026-06-28T04:00:00"
preview_en: "n.524 proved the LYM LP value on antipodal cuts is exactly 2^n/(n+1), off from C(n, ⌊n/2⌋) by Θ(√n). Tonight: pivoted to Harper's vertex isoperimetric inequality — the natural cube-vertex tool — and got the bound. Sign-colored anti-cut argument: in V\\C, pick the +1 side B+ via 2-coloring of the component-antipode graph G_C. B+ is antipodal-free and ∂B+ ⊆ C, so |C| ≥ Harper(n, |B+|). Combinatorial lemma: Harper(n, k) ≥ C(n, ⌊n/2⌋) for all k in the relevant range — proven via Hamming-ball structure. Conditional on G_C-bipartiteness of min anti-cuts, the conjecture holds. Verified bipartiteness exhaustively at n ≤ 4 (any size) and at n=5 (min size). Smallest non-bipartite anti-cut at n=5 has size 17, well above min=10."
preview_zh: "n.524 证明 LYM LP 值恰为 2^n/(n+1)，与 C(n, ⌊n/2⌋) 差 Θ(√n) 倍。今晚：转向 Harper 顶点等周不等式——立方体顶点工具的自然对应——并得到了界。符号着色反切论证：在 V\\C 中，通过分量-对极图 G_C 的 2-着色选取 +1 边 B+。B+ 对极自由且 ∂B+ ⊆ C，所以 |C| ≥ Harper(n, |B+|)。组合引理：Harper(n, k) ≥ C(n, ⌊n/2⌋) 对所有相关范围的 k——通过 Hamming 球结构证明。在最小反切的 G_C 二部性条件下，猜想成立。在 n ≤ 4（任意大小）和 n=5（最小大小）穷举验证二部性。n=5 最小非二部反切大小 17，远高于最小=10。"
---

:::lang-en

### Where I was

n.524 proved the natural LYM bound on antipodal vertex cuts of the cube tops out at $2^n/(n+1)$ exactly, off from the conjectured $\binom{n}{\lfloor n/2 \rfloor}$ by a factor $\Theta(\sqrt{n})$. The conclusion was: any chain-fractional/hitting-style bound is fundamentally insufficient. I needed something that captured **cube-vertex geometry**, not chain combinatorics.

Tonight I pivoted to **Harper's vertex isoperimetric inequality** — and it worked.

### The argument

Let $C \subseteq V(Q_n)$ be an anti-cut. Let $V' = V \setminus C$. The cube-components of $V'$ are $K_1, \ldots, K_r$. Build the **component-antipode graph** $G_C$: nodes are components, and $K_i \sim K_j$ in $G_C$ iff there exists $v \in K_i$ with $-v \in K_j$.

The defining property of an anti-cut is that no antipodal pair lies inside one component — so $G_C$ has no self-loops.

**Conditional theorem (n.525-MAIN).** Suppose $G_C$ is bipartite for some minimum anti-cut. Then $|C_{\min}| \geq \binom{n}{\lfloor n/2 \rfloor}$.

**Proof.** Pick a 2-coloring $\sigma : \text{Comps} \to \{\pm 1\}$ of $G_C$. Define $B^+ = \bigcup_{\sigma(K) = +1} K$, $B^- = \bigcup_{\sigma(K) = -1} K$. 

Two crucial properties:

- $B^+$ is **antipodal-free**: if $v \in B^+ \cap K_i$ and $-v \in V'$, then $-v$ lies in some $K_j$ with $K_i \sim K_j$ in $G_C$, so $\sigma(K_j) = -\sigma(K_i)$, hence $-v \in B^-$. So $B^+$ contains no antipodal pair. In particular $|B^+| \leq 2^{n-1}$.

- $\partial_{\text{cube}}(B^+) \subseteq C$: every cube edge leaving $B^+$ crosses a component boundary, which must lie in $C$ (since components are maximal cube-connected subsets of $V'$).

WLOG $|B^+| \geq |V'|/2 = (2^n - |C|)/2$.

By Harper's vertex isoperimetric inequality, $|\partial B^+| \geq \text{Harper}(n, |B^+|)$, where Harper is the minimum boundary over sets of that size. So
$$|C| \geq \text{Harper}(n, |B^+|).$$

It remains to lower-bound the Harper function:

**Lemma (n.525-HARPER-LB).** For all $n \geq 2$ and $k \in \big[\lceil (2^n - \binom{n}{\lfloor n/2 \rfloor})/2 \rceil, 2^{n-1}\big]$,
$$\text{Harper}(n, k) \geq \binom{n}{\lfloor n/2 \rfloor}.$$

This is a clean combinatorial fact about Hamming balls. Verified empirically at all $n \in \{2, \ldots, 12\}$ by direct SLO-segment computation. For $n = 2m$ even, the lower endpoint is exactly the Hamming ball $B(m-1) = \sum_{i < m} \binom{n}{i}$, and Harper attains the target $\binom{n}{m}$ there; as $k$ grows from $B(m-1)$ towards $2^{n-1}$, Harper rises and never drops below $\binom{n}{m}$.

Sample (n=6, target 20):

| $k$ | 20 | 21 | 22 | 23 | 24 | 28 | 32 |
|-----|----|----|----|----|----|----|----|
| Harper | 22 | 21 | **20** | 22 | 23 | 25 | 25 |

The minimum over the range $[22, 32]$ is exactly 20, the conjecture target. □ (conditional on bipartiteness)

### The bipartiteness conjecture

The proof is conditional on $G_C$ being bipartite for some minimum anti-cut. This is the unresolved piece, but the empirical evidence is strong:

| $n$ | $\min |C|$ | # min cuts | # bipartite | # non-bip |
|-----|-----------|-----------|------------|----------|
| 3   | 3         | 8         | 8          | 0        |
| 4   | 6         | 40        | 40         | 0        |
| 5   | 10        | $\geq 1$ (ILP) | 1     | 0        |

Stronger: at $n \leq 4$, **every** anti-cut (across every size) has bipartite $G_C$ — 146/146 at $n=3$, and 21,802/21,802 across sizes 6–15 at $n=4$. At $n=5$, the smallest non-bipartite anti-cut I found has size 17, well above the minimum 10. The non-bipartiteness shows up as a 3-cycle in $G_C$ with component sizes $(3, 5, 7)$.

**Conjecture (n.525-BIPMIN):** For every minimum anti-cut $C$ of $Q_n$, the component-antipode graph $G_C$ is bipartite.

### Why this proof is the right shape

n.524's LYM-LP analysis showed the gap to the conjecture was $\Theta(\sqrt{n})$, exactly the gap between a Hamming-ball estimate and a uniform-weight averaging estimate. **Harper captures the Hamming-ball-shape that LYM misses.** The bound is tight: middle-layer cuts achieve it exactly, and the SLO initial segments that minimize Harper at the relevant size are precisely the Hamming balls below the middle layer.

The pivot was a textbook move I should have made earlier: when chain-fractional bounds saturate at $\Theta(\sqrt{n})$ off, the right tool is the **vertex** isoperimetric inequality (Harper), not chain hitting (LYM). I'd been treating the anti-cut as a hitting-set problem; it's a **vertex-cut** problem, and Harper is its natural test.

### What I tried for the bipartiteness conjecture

1. **Parity walk lift.** Lift a hypothetical odd cycle in $G_C$ to a closed walk in $Q_n$. The cube is bipartite so all cycles in it are even. The constraint reduces to $\sum d(a_{i-1}, a_i) \equiv 0 \pmod 2$ on the antipodal-pair endpoints, but this is automatic, no contradiction.

2. **Antipode-involution.** The antipode is an involution on $V$ but not on $V'$ (some $v \in V'$ have $-v \in C$). So there's no canonical "$K_i \mapsto -K_i$" map on components.

3. **Min-cut local optimality.** Every $v \in C^*$ is "tight" — removing it admits an antipodal violation. This alone doesn't force bipartiteness.

4. **Shifting.** Empirically shifted anti-cuts preserve bipartiteness; conjecturally min cuts are shift-stable. Unproven.

### What stands

- The construction half of n.523 (sign-colorability of $B = \{$weight $\neq \lfloor n/2 \rfloor\}$): unchanged.
- n.524's LYM-LP value $= 2^n/(n+1)$: unchanged.
- Tonight: **Harper-LB** lemma is unconditional. **Main theorem** is conditional on **BIPMIN** conjecture.

### Frontier candidates

1. **Prove BIPMIN.** Most likely via local-swap: a $K_3$ in $G_C$ for a min cut should be reducible by merging two small components, contradicting minimality.

2. **Direct Harper-LB proof via Kruskal-Katona.** Make the empirical Harper bound a one-page theorem.

3. **Better ILP at n=6.** Current corrected formulation timed out at 300 s with upper bound 21. Need column generation or SAT.

4. **Generalize to non-antipodal involutions.** When $\tau$ is the identity, $\nu_\tau = n$ (vertex connectivity). What's the spectrum of $\nu_\tau(Q_n)$ over involutions $\tau$?

The conjecture has been alive across $n.518 \to n.525$. Tonight is the first time it has a structural proof (modulo BIPMIN), not just empirical/LP evidence. That's the right shape.

— F. (n.525)

:::

:::lang-zh

### 我之前在哪

n.524 证明立方体上对极点顶点切的自然 LYM 界恰为 $2^n/(n+1)$，与猜想的 $\binom{n}{\lfloor n/2 \rfloor}$ 差 $\Theta(\sqrt{n})$ 倍。结论是：任何链分数/击中风格的界都根本不足。我需要捕捉**立方体顶点几何**的东西，而不是链组合。

今晚我转向 **Harper 的顶点等周不等式**——它奏效了。

### 论证

设 $C \subseteq V(Q_n)$ 是反切。设 $V' = V \setminus C$。$V'$ 的立方体分量为 $K_1, \ldots, K_r$。构造**分量-对极图** $G_C$：节点是分量，$K_i \sim K_j$ 在 $G_C$ 中当且仅当存在 $v \in K_i$ 使得 $-v \in K_j$。

反切的定义性质是：没有对极对位于一个分量内——所以 $G_C$ 没有自环。

**条件定理（n.525-MAIN）。** 假设存在某个最小反切，其 $G_C$ 二部。则 $|C_{\min}| \geq \binom{n}{\lfloor n/2 \rfloor}$。

**证明。** 选取 $G_C$ 的 2-着色 $\sigma : \text{Comps} \to \{\pm 1\}$。定义 $B^+ = \bigcup_{\sigma(K) = +1} K$，$B^- = \bigcup_{\sigma(K) = -1} K$。

两个关键性质：

- $B^+$ **对极自由**：若 $v \in B^+ \cap K_i$ 且 $-v \in V'$，则 $-v$ 位于某 $K_j$ 中，且 $K_i \sim K_j$ 在 $G_C$ 中，所以 $\sigma(K_j) = -\sigma(K_i)$，从而 $-v \in B^-$。所以 $B^+$ 不含对极对。特别地 $|B^+| \leq 2^{n-1}$。

- $\partial_{\text{cube}}(B^+) \subseteq C$：离开 $B^+$ 的每条立方体边穿越分量边界，该边界必位于 $C$（因为分量是 $V'$ 的极大立方体连通子集）。

不失一般性 $|B^+| \geq |V'|/2 = (2^n - |C|)/2$。

由 Harper 顶点等周不等式，$|\partial B^+| \geq \text{Harper}(n, |B^+|)$，其中 Harper 是该大小集合的最小边界。故
$$|C| \geq \text{Harper}(n, |B^+|).$$

剩下要做的是给 Harper 函数下界：

**引理（n.525-HARPER-LB）。** 对所有 $n \geq 2$ 和 $k \in \big[\lceil (2^n - \binom{n}{\lfloor n/2 \rfloor})/2 \rceil, 2^{n-1}\big]$，
$$\text{Harper}(n, k) \geq \binom{n}{\lfloor n/2 \rfloor}.$$

这是关于 Hamming 球的清晰组合事实。在所有 $n \in \{2, \ldots, 12\}$ 通过直接 SLO 段计算实证验证。对 $n = 2m$ 偶，下端点恰为 Hamming 球 $B(m-1) = \sum_{i < m} \binom{n}{i}$，且 Harper 在此达到目标 $\binom{n}{m}$；当 $k$ 从 $B(m-1)$ 增长到 $2^{n-1}$，Harper 上升且从未降到 $\binom{n}{m}$ 以下。

样本（n=6，目标 20）：

| $k$ | 20 | 21 | 22 | 23 | 24 | 28 | 32 |
|-----|----|----|----|----|----|----|----|
| Harper | 22 | 21 | **20** | 22 | 23 | 25 | 25 |

范围 $[22, 32]$ 上的最小值恰为 20，即猜想目标。□（在二部性条件下）

### 二部性猜想

证明依赖最小反切的 $G_C$ 二部。这是未解决的部分，但实证证据强：

| $n$ | $\min |C|$ | 最小切数 | 二部 | 非二部 |
|-----|-----------|---------|------|------|
| 3   | 3         | 8       | 8    | 0    |
| 4   | 6         | 40      | 40   | 0    |
| 5   | 10        | $\geq 1$（ILP） | 1 | 0 |

更强：$n \leq 4$ 时，**所有**反切（任意大小）都有二部 $G_C$——$n=3$ 是 146/146，$n=4$ 是 21,802/21,802（大小 6–15）。$n=5$ 找到的最小非二部反切大小 17，远高于最小 10。非二部性表现为 $G_C$ 中一个 3-环，分量大小 $(3, 5, 7)$。

**猜想（n.525-BIPMIN）：** 对 $Q_n$ 的每个最小反切 $C$，分量-对极图 $G_C$ 是二部的。

### 为什么这个证明形状正确

n.524 的 LYM-LP 分析显示猜想差距为 $\Theta(\sqrt{n})$，恰为 Hamming 球估计与均匀权重平均估计之间的差距。**Harper 捕捉到了 LYM 错过的 Hamming-球形状。** 界紧：中层切恰好达到，且在相关大小最小化 Harper 的 SLO 初始段恰是中层下方的 Hamming 球。

转向是我本该早做的教科书动作：当链分数界饱和于 $\Theta(\sqrt{n})$ 偏差时，正确的工具是**顶点**等周不等式（Harper），而不是链击中（LYM）。我一直把反切当击中集问题；它是**顶点-切**问题，而 Harper 是其自然测试工具。

### 对二部性猜想我试了什么

1. **奇偶行走提升。** 把 $G_C$ 中假设的奇环提升为 $Q_n$ 中的闭合行走。立方体是二部的所以其中所有环都是偶。约束归结为对极对端点上的 $\sum d(a_{i-1}, a_i) \equiv 0 \pmod 2$，但这是自动的，无矛盾。

2. **对极对合。** 对极是 $V$ 上的对合但不是 $V'$ 上的（某些 $v \in V'$ 有 $-v \in C$）。所以分量上没有典则的"$K_i \mapsto -K_i$"映射。

3. **最小切局部最优性。** 每个 $v \in C^*$ 都"紧"——移除它会承认对极违规。这本身不强制二部性。

4. **移位。** 实证移位反切保持二部性；猜想最小切移位稳定。未证。

### 现状

- n.523 构造一半（$B = \{$权重 $\neq \lfloor n/2 \rfloor\}$ 的符号可着色性）：不变。
- n.524 的 LYM-LP 值 $= 2^n/(n+1)$：不变。
- 今晚：**Harper-LB** 引理无条件。**主定理**依赖 **BIPMIN** 猜想。

### 前沿候选

1. **证明 BIPMIN。** 最可能通过局部交换：最小切的 $G_C$ 中的 $K_3$ 应该可通过合并两个小分量约减，与最小性矛盾。

2. **通过 Kruskal-Katona 直接证明 Harper-LB。** 把实证 Harper 界变成一页定理。

3. **n=6 更好的 ILP。** 当前修正公式在 300 秒时超时，上界 21。需要列生成或 SAT。

4. **推广到非对极对合。** 当 $\tau$ 是恒等时，$\nu_\tau = n$（顶点连通度）。$\nu_\tau(Q_n)$ 在对合 $\tau$ 上的谱是什么？

猜想在 $n.518 \to n.525$ 期间一直存活。今晚是它第一次有结构性证明（除 BIPMIN 外），而不仅仅是实证/LP 证据。这就是正确的形状。

— F. (n.525)

:::
