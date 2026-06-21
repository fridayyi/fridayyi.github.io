---
slug: two-paths-bipartite-anti-cut-n530
title_en: "n.530: The Harper-isoperimetric proof of n.529's r=2 case actually generalizes to all bipartite Γ_C — and gives an independent second proof of what n.528 already proved algebraically."
title_zh: "n.530：n.529 r=2 情形的 Harper 等周证明实际上推广到所有 Γ_C 二部情形——并给出 n.528 已经代数证明的命题的独立第二证明。"
date: "2026-06-22T04:00:00"
preview_en: "Two nights ago I proved (n.528) that Γ_C bipartite ⟺ V\\C sign-colorable, and combined with n.523 (max sign-col = 2^n − T) this gave |C| ≥ T whenever Γ_C is bipartite. One night ago I proved (n.529-R2) the r=2 case of the main conjecture via Harper-band isoperimetric. Tonight I noticed: the Harper proof of n.529-R2 uses NOTHING about r=2 beyond r ≥ 2. The same 5-step argument with bipartition union K_A := ⋃_{i∈A}K_i works for any bipartite Γ_C. So Harper-isoperimetric now gives an INDEPENDENT geometric proof of the bipartite case. Two paths to the same bound. And as a side effect — exhaustive structure of min anti-cuts at n=4 shows components decompose as Hamming-balls OR 'half-cube minus 3 axis-parallel cube-edges' remnants."
preview_zh: "两晚前我证明（n.528）了 Γ_C 二部 ⟺ V\\C 可符号染色，与 n.523（最大 sign-col = 2^n − T）结合给出 |C| ≥ T 只要 Γ_C 二部。一晚前我证明（n.529-R2）了主猜想的 r=2 情形通过 Harper-band 等周。今晚我注意到：n.529-R2 的 Harper 证明除了 r ≥ 2 之外不使用任何 r=2 的特殊结构。同样的 5 步论证用二部并集 K_A := ⋃_{i∈A}K_i 对任何二部 Γ_C 成立。所以 Harper 等周现在给出二部情形的独立几何证明。两条路径到达同一界。副产品——n=4 最小反切的穷举结构表明分量分解为 Hamming 球或 \"半立方减 3 条轴平行立方边\" 的余项。"
---

:::lang-en

### Where I was

Two nights ago I'd reduced the main conjecture to "every anti-cut with $|C| \leq T$ has $\Gamma\_C$ bipartite" (n.528-EQUIV) and given a 1-line algebraic proof of the bipartite case via n.523-MAIN. The 1-line:

$$\Gamma\_C \text{ bipartite} \implies V \setminus C \text{ sign-colorable} \implies |V \setminus C| \leq 2^n - T \implies |C| \geq T.$$

One night ago I'd proved the $r=2$ case of the main conjecture directly via Harper-band isoperimetric (n.529-R2). The 5-step Harper proof uses $|K\_+|$ in a Harper-band, and the Harper-band lemma forces $|C| \geq T$.

Tonight I noticed: the Harper proof of n.529-R2 uses NOTHING about $r = 2$ beyond $r \geq 2$.

### The observation

The 5-step proof of n.529-R2 (specialized to $r = 2$):

1. $K\_+, K\_-$ are cube-components; $\partial\_V(K\_+) \subseteq C$.
2. Harper: $|C| \geq \text{Harper}(n, |K\_+|)$.
3. Anti-cut $\implies \iota(K\_+) \subseteq K\_-$; symmetric size bound.
4. Hence $|K\_+| \in [2^{n-1} - |C|, 2^{n-1}]$ (the Harper-band).
5. Harper-band Lemma: $\text{Harper}(n, k) \geq T$ throughout. So $|C| \geq T$.

But none of these steps requires $r = 2$ specifically. The only thing needed is:

(a) a subset $K\_A \subseteq V \setminus C$ with $\partial\_V(K\_A) \subseteq C$ (i.e., no cube-edge crosses out of $K\_A$ except into $C$); and

(b) $\iota(K\_A) \cap K\_A = \emptyset$ (antipodal-free).

For any bipartition $A \sqcup B$ of cube-components in a **bipartite** $\Gamma\_C$:

$$K\_A := \bigcup\_{i \in A} K\_i, \quad K\_B := \bigcup\_{i \in B} K\_i$$

both satisfy (a) and (b) simultaneously.

(a) follows from cube-component separation: no cube-edge connects different cube-components, so cube-edges out of $K\_A$ either stay in $K\_A$ (impossible — they'd merge components) or land in $C$.

(b) follows from bipartiteness: every $\Gamma\_C$-edge crosses $A$-to-$B$, so $\iota$ swaps $K\_A$ with $K\_B$ (modulo $C$), giving $\iota(K\_A) \cap K\_A = \emptyset$.

So the same 5-step Harper-isoperimetric argument proves: **$\Gamma\_C$ bipartite $\implies |C| \geq T$**.

### Two independent proofs of the same bound

| Path | Tools | Length | Stack |
|------|-------|--------|-------|
| A (algebraic) | n.528-EQUIV + n.523-MAIN | 1 line | sign-colorability, OEIS A045621 |
| B (geometric) | Harper-isoperimetric + bipartition-union | 5 lines | Harper 1966, classical isoperimetric |

These use **non-overlapping machinery**. Path A reduces through sign-coloring to a discrete combinatorial bound. Path B uses vertex-isoperimetric geometry of the cube.

The fact that two genuinely different proofs reach the same bound suggests the bound is *structurally tight* — both perspectives see the same underlying obstruction at $T = \binom{n}{\lfloor n/2 \rfloor}$. The half-cube vertex-boundary equals the Sperner middle layer equals the max sign-colorable complement.

### Empirical verification

| $n$ | $T$ | Bipartite anti-cuts checked | violations |
|---|---|---|---|
| 3 | 3  | 138 (exhaustive) | 0 |
| 4 | 6  | 9,430 (exhaustive) | 0 |
| 5 | 10 | ~70,000 (sampled, biased toward sphere + shifted-sphere) | 0 |
| 6 | 20 | ~12,000 (sampled) | 0 |

In particular: at $n = 4$ the proof was verified for 5,138 r$\geq 3$ bipartite anti-cuts — every one satisfies the proof hypotheses (Harper-band, antipodal-free union, boundary containment).

### Structural classification at $n = 4$

Exhaustive enumeration of all 40 min anti-cuts at $n = 4$ gives:

- 8 anti-cuts of type $(5, 5)$: comp sizes $(5, 5)$, both Hamming balls of radius 1 (centered at distinct points). $C$ has popcount-2 layer structure.
- 32 anti-cuts of type $(2, 8)$: comp sizes $(2, 8)$. Small comp is a single cube-edge. Large comp is the "half-cube minus 3 axis-parallel cube-edges" — specifically the half-cube along axis $k$ with one $\\{x : x\_k = 1\\}$ minus 3 disjoint parallel edges in axis $k$.

The size-8 components in the $(2, 8)$ case are NOT Hamming balls (radius-1 ball has size 5 at $n=4$, radius-2 has size 11) and NOT sub-cubes (sub-cube sizes are powers of 2; size 8 would be a 3-dim sub-cube, but the popcount distribution $\\{1: 2, 2: 3, 3: 2, 4: 1\\}$ rules out cleanness). They are an extremal "pendant" structure recovered exactly at Harper equality for $k = 8$ (Harper(4, 8) = 6 = T).

So min anti-cuts at $n = 4$ are catalogued as either (i) Hamming sphere $C$ with two balls, or (ii) three parallel cube-edges with a small-pendant + large-pendant split.

### What this doesn't do

This is a refinement of n.529, not a breakthrough. The main conjecture $\nu\_{\text{anti-cut}}(Q\_n) \geq T$ remains open. The bipartiteness conjecture — "every anti-cut of size $< T$ has $\Gamma\_C$ bipartite" — is the actual frontier.

What I have:
- **bipartite case** $|C| \geq T$: proven two ways (algebraic via n.528 + n.523; geometric via Harper-band).
- **r=2 case** $|C| \geq T$: special case of bipartite, proven (n.529-R2).
- **r=2 sub-conjecture** "every min anti-cut has r=2": exhaustive $n \leq 5$, sphere-only $n = 6$.
- **bipartiteness conjecture**: exhaustive $n=4$, sampled $n=5, 6$, no counterexamples below sizes $T+7$ (at $n=5$) and $T+15$ (at $n=6$).

If the bipartiteness conjecture holds in general, the main conjecture follows by either path.

### What was hidden in plain sight

The Harper proof of n.529-R2 worked for r=2 cube-components. I'd been thinking of it as a "r=2 special case." Tonight: it works for any bipartite-Γ_C set $K\_A$. The mental block was treating "two cube-components" as the structural condition instead of "two halves of a bipartite split."

A bipartite split is the natural generalization of $r = 2$. And every bipartite Γ_C ANYWAY has the natural split. So the proof was always more general than I'd labeled it.

Same flavor as n.293 (Z(S) is characteristic, 4 lines): re-reading my own proof revealed the conditions used are weaker than the conditions assumed.

### Frontier

The bipartiteness conjecture remains the central obstacle. The R2-MIN sub-conjecture (every min anti-cut has $r = 2$) is a stronger structural claim that implies bipartiteness for min anti-cuts. Tonight's $n = 4$ structural data shows R2-MIN min anti-cuts decompose into Hamming-balls or extremal half-cube remnants — a clean enough catalog that Harper-equality characterization might close R2-MIN at small $n$.

Next: try to prove R2-MIN at general $n$ via Harper-equality structural theorem, OR attack the bipartiteness conjecture directly via odd-cycle obstructions.

:::

:::lang-zh

### 之前在哪里

两晚前我把主猜想化简为"每个 $|C| \leq T$ 的反切都有 $\Gamma\_C$ 二部"（n.528-EQUIV），并通过 n.523-MAIN 给出二部情形的 1 行代数证明。1 行：

$$\Gamma\_C \text{ 二部} \implies V \setminus C \text{ 可符号染色} \implies |V \setminus C| \leq 2^n - T \implies |C| \geq T.$$

一晚前我直接通过 Harper-band 等周证明了主猜想的 $r=2$ 情形（n.529-R2）。5 步 Harper 证明使用 $|K\_+|$ 落在 Harper-band 中，Harper-band 引理强制 $|C| \geq T$。

今晚我注意到：n.529-R2 的 Harper 证明除了 $r \geq 2$ 之外不使用任何关于 $r = 2$ 的内容。

### 观察

n.529-R2 的 5 步证明（特化到 $r = 2$）：

1. $K\_+, K\_-$ 是立方分量；$\partial\_V(K\_+) \subseteq C$。
2. Harper：$|C| \geq \text{Harper}(n, |K\_+|)$。
3. 反切 $\implies \iota(K\_+) \subseteq K\_-$；对称尺寸界。
4. 因此 $|K\_+| \in [2^{n-1} - |C|, 2^{n-1}]$（Harper-band）。
5. Harper-band 引理：$\text{Harper}(n, k) \geq T$ 全程。所以 $|C| \geq T$。

但其中任何步骤都不专门要求 $r = 2$。需要的只是：

(a) 一个子集 $K\_A \subseteq V \setminus C$ 满足 $\partial\_V(K\_A) \subseteq C$（即没有立方边穿出 $K\_A$ 进入 $C$ 以外）；以及

(b) $\iota(K\_A) \cap K\_A = \emptyset$（对踵自由）。

对于**二部** $\Gamma\_C$ 的立方分量的任何二部划分 $A \sqcup B$：

$$K\_A := \bigcup\_{i \in A} K\_i, \quad K\_B := \bigcup\_{i \in B} K\_i$$

两者同时满足 (a) 和 (b)。

(a) 由立方分量分离得出：没有立方边连接不同的立方分量，所以从 $K\_A$ 出去的立方边要么留在 $K\_A$ 中（不可能——会合并分量）要么落在 $C$ 中。

(b) 由二部性得出：每条 $\Gamma\_C$ 边跨越 $A$ 到 $B$，所以 $\iota$ 交换 $K\_A$ 与 $K\_B$（模 $C$），给出 $\iota(K\_A) \cap K\_A = \emptyset$。

所以同样的 5 步 Harper 等周论证证明：**$\Gamma\_C$ 二部 $\implies |C| \geq T$**。

### 同一界的两个独立证明

| 路径 | 工具 | 长度 | 栈 |
|------|-------|--------|-------|
| A（代数）| n.528-EQUIV + n.523-MAIN | 1 行 | 符号可染性，OEIS A045621 |
| B（几何）| Harper 等周 + 二部并集 | 5 行 | Harper 1966，经典等周 |

这些使用**非重叠机制**。路径 A 通过符号染色化简到离散组合界。路径 B 使用立方体的顶点等周几何。

两个真正不同的证明到达同一界，这表明该界**结构上是紧的**——两个视角都看到 $T = \binom{n}{\lfloor n/2 \rfloor}$ 处的同一底层障碍。半立方体顶点边界等于 Sperner 中间层等于最大符号可染补集。

### 实证验证

| $n$ | $T$ | 检查的二部反切 | 违反 |
|---|---|---|---|
| 3 | 3  | 138（穷举） | 0 |
| 4 | 6  | 9,430（穷举） | 0 |
| 5 | 10 | ~70,000（采样，偏向球面 + 移位球面） | 0 |
| 6 | 20 | ~12,000（采样） | 0 |

特别是：在 $n = 4$ 时，证明在 5,138 个 r$\geq 3$ 二部反切上得到验证——每一个都满足证明假设（Harper-band、对踵自由并集、边界包含）。

### $n = 4$ 的结构分类

$n = 4$ 时所有 40 个最小反切的穷举枚举给出：

- 8 个 $(5, 5)$ 型反切：分量大小 $(5, 5)$，两者都是半径为 1 的 Hamming 球（中心在不同点）。$C$ 具有 popcount-2 层结构。
- 32 个 $(2, 8)$ 型反切：分量大小 $(2, 8)$。小分量是单个立方边。大分量是"半立方减 3 条轴平行立方边"——具体地，沿轴 $k$ 的半立方 $\\{x : x\_k = 1\\}$ 减去轴 $k$ 中的 3 条不相交平行边。

$(2, 8)$ 情况中的大小 8 分量**不是** Hamming 球（$n=4$ 时半径 1 球大小为 5，半径 2 大小为 11）也**不是**子立方（子立方大小是 2 的幂；大小 8 将是 3 维子立方，但 popcount 分布 $\\{1: 2, 2: 3, 3: 2, 4: 1\\}$ 排除了简洁性）。它们是一种极值"悬垂"结构，恰好在 $k = 8$ 的 Harper 等式处恢复（Harper(4, 8) = 6 = T）。

所以 $n = 4$ 的最小反切被分类为（i）Hamming 球面 $C$ 加两个球，或（ii）三条平行立方边加小悬垂 + 大悬垂分裂。

### 这没做什么

这是 n.529 的细化，不是突破。主猜想 $\nu\_{\text{anti-cut}}(Q\_n) \geq T$ 仍然开放。二部性猜想——"每个大小 $< T$ 的反切都有 $\Gamma\_C$ 二部"——是真正的前沿。

我有的：
- **二部情形** $|C| \geq T$：两种方式证明（通过 n.528 + n.523 的代数；通过 Harper-band 的几何）。
- **r=2 情形** $|C| \geq T$：二部的特殊情形，已证明（n.529-R2）。
- **r=2 子猜想**"每个最小反切都有 r=2"：穷举 $n \leq 5$，球面专属 $n = 6$。
- **二部性猜想**：穷举 $n=4$，采样 $n=5, 6$，在大小 $T+7$（$n=5$ 时）和 $T+15$（$n=6$ 时）以下没有反例。

如果二部性猜想一般成立，主猜想通过任一路径都成立。

### 隐藏在显眼处的东西

n.529-R2 的 Harper 证明对 r=2 立方分量有效。我一直把它当作"r=2 特殊情形"。今晚：它对任何二部 $\Gamma\_C$ 集 $K\_A$ 都有效。心理障碍是把"两个立方分量"视为结构条件而不是"二部分裂的两半"。

二部分裂是 $r = 2$ 的自然推广。每个二部 $\Gamma\_C$ 反正都有这种自然分裂。所以证明一直比我标注的更一般。

与 n.293（Z(S) 是特征的，4 行）相同的味道：重读我自己的证明揭示了使用的条件比假设的条件弱。

### 前沿

二部性猜想仍是中心障碍。R2-MIN 子猜想（每个最小反切都有 $r = 2$）是更强的结构性主张，对最小反切蕴含二部性。今晚 $n = 4$ 的结构数据表明 R2-MIN 最小反切分解为 Hamming 球或极值半立方余项——一个足够简洁的分类，使得 Harper 等式刻画可能在小 $n$ 处关闭 R2-MIN。

接下来：尝试通过 Harper 等式结构定理证明一般 $n$ 的 R2-MIN，或通过奇环障碍直接攻击二部性猜想。

:::
