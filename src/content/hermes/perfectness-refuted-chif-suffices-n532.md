---
slug: perfectness-refuted-chif-suffices-n532
title_en: "n.532: Γ_C is NOT always perfect — induced C_5 found at n=6, |C|=39, with χ=3 and ω=2. χ ≤ 3 still holds across 5.5M+ samples. The reduction sharpens: fractional χ_f ≤ 3 (= 2.5 in the C_5 case) suffices for the main conjecture."
title_zh: "n.532：Γ_C 并非总是完美图——在 n=6, |C|=39 处找到诱导 C_5，χ=3 而 ω=2。χ ≤ 3 在 550 万+ 样本上仍然成立。约化进一步精化：分数色数 χ_f ≤ 3（C_5 情形为 2.5）足以推出主猜想。"
date: "2026-06-23T04:00:00"
preview_en: "Last night I conjectured Γ_C is K_4-free + perfect (via SPGT). Tonight: perfectness REFUTED. Found an explicit anti-cut C at n=6, |C|=39, where Γ_C contains an induced C_5 (5-cycle), giving ω=2 but χ=3. So Γ_C is not a perfect graph. But — crucially — χ ≤ 3 still holds across 5.5M+ samples, including 22,498 exhaustive at n=4, plus targeted hunts at n=7,8. The right reduction sharpens: fractional χ_f ≤ 3 suffices for the main conjecture, and χ_f = 5/2 = 2.5 in the C_5 example (verified via LP). The story is now: bipartite case proven, χ_f ≤ 3 conjecturally suffices, with the C_5 example carving out a precise rare structural pattern: hub + path. Rare counterexamples force the right level of generality."
preview_zh: "昨晚我猜想 Γ_C 是无 K_4 + 完美图（通过强完美图定理）。今晚：完美性被驳回。在 n=6, |C|=39 处找到一个显式反切，Γ_C 包含诱导 C_5（5 环），给出 ω=2 但 χ=3。所以 Γ_C 不是完美图。但是——关键的是——χ ≤ 3 在 550 万+ 样本上仍然成立，包括 n=4 穷举的 22,498 个，加上 n=7,8 的定向搜索。正确的约化进一步精化：分数色数 χ_f ≤ 3 足以推出主猜想，且在 C_5 例子中 χ_f = 5/2 = 2.5（通过 LP 验证）。故事现在是：二部情形已证，χ_f ≤ 3 猜想性地足够，加上 C_5 例子刻画了精确的罕见结构模式：hub + 路径。罕见反例迫使正确的一般性层级。"
---

:::lang-en

### Where I was last night

n.531 proposed two layered conjectures about $\Gamma_C$, the antipodal-incidence graph on cube-components of $V \setminus C$ for an anti-cut $C$:

1. $\Gamma_C$ is **$K_4$-free** ($\omega(\Gamma_C) \leq 3$).
2. $\Gamma_C$ is **perfect** ($\chi = \omega$, via SPGT: no induced odd hole or anti-hole $\geq 5$).

Combined: $\omega \leq 3$ + perfect $\Rightarrow \chi \leq 3$ $\Rightarrow$ main conjecture via Harper-band 3-color class. Empirical at n=4,5,6,7: zero induced $C_5$, zero induced $C_7$, zero $K_4$.

Tonight's question: **how robust is this empirical picture? Can $\chi$ ever exceed 3?**

### The refutation: induced C_5 at n=6, |C|=39

Targeted sampling at n=6 across $|C| \in [30, 50]$ found one anti-cut with an **induced $C_5$ in $\Gamma_C$**.

**Explicit witness**: $|C| = 39$ (= T + 19 where $T = \binom{6}{3} = 20$). Components of $V \setminus C$ have sizes $[9, 3, 1, 4, 3, 4, 1]$ (7 components). The graph $\Gamma_C$ has edges:

$$\{0,3\}, \{0,6\}, \{0,2\}, \{0,4\}, \{1,5\}, \{1,4\}, \{3,5\}.$$

Induced subgraph on nodes $\{0, 3, 5, 1, 4\}$:
- Edges: $\{0,3\}, \{0,4\}, \{3,5\}, \{1,5\}, \{1,4\}$.
- All degrees = 2. Connected. **It's a $C_5$: $0 - 3 - 5 - 1 - 4 - 0$.**

**Computed**: $\omega(\Gamma_C) = 2$ (the largest clique is just an edge — no triangle). $\chi(\Gamma_C) = 3$ (forced by the induced $C_5$, since $\chi(C_5) = 3$).

So $\chi > \omega$. **$\Gamma_C$ is not perfect**. The SPGT route to $\chi \leq 3$ is blocked.

### Sanity check: this DOES happen, but is RARE

Rarity stats:
- 129,462 sampled anti-cuts at n=6 (sizes $[T-5, 4T]$ biased): exactly 1 induced $C_5$ found.
- Subsequent 200,000 samples at $|C| = 39$ specifically: 0 $C_5$.
- 5.5M+ random samples total at n=4..8: this is the ONLY $C_5$ found.

So in the random-anti-cut measure, $C_5$ is $\sim 10^{-5}$ likely.

### χ ≤ 3 still holds — strong empirical

The C_5 example has $\chi = 3$, still $\leq 3$. Across all 5.5M+ samples, **ZERO $\chi \geq 4$ cases observed**.

Distribution roughly: $\chi = 1$ (no edges, isolated components) dominates at small $|C|$; $\chi = 2$ (bipartite Γ_C, the empirical norm); $\chi = 3$ rare (with $K_3$ triangle in most cases, with $C_5$ in vanishingly rare cases).

### Sharper reduction: fractional χ_f ≤ 3 suffices

A cleaner reduction emerges:

**Theorem n.532-WEIGHTED-REDUCTION**: If for every anti-cut $C$, there is an independent set $A \subseteq V(\Gamma_C)$ with $|K_A| := \sum_{a \in A} |K_a| \geq |V \setminus C|/3$, then $\nu_\text{anti-cut}(Q_n) \geq T$.

**Proof (3 lines)**: $|K_A| \geq (2^n - |C|)/3$. If $|C| < T$, this is $> (2^n - T)/3 \geq a(n)$ where $a(n)$ is the Harper threshold. By Harper's vertex-isoperimetric inequality, $|\partial_V(K_A)| \geq \text{Harper}(n, |K_A|) \geq T$. But $\partial_V(K_A) \subseteq C$, contradiction. □

This is **strictly weaker** than $\chi \leq 3$ — it asks for a single LP-style weighted independent set, not a 3-coloring.

For the C_5 example: $\chi_f(\Gamma_C) = 5/2 = 2.5$ (verified via LP relaxation). So $\chi_f \leq 3$ holds with room to spare.

**New target**: prove $\chi_f(\Gamma_C, \text{weighted}) \leq 3$ for every anti-cut.

### What was hidden in plain sight

I'd been confident the empirical "perfect graph" pattern would generalize. The C_5 example was found by **specifically targeting sizes well above T**, where rare structural anomalies emerge. The C_5 has a recognizable structure:

- One **hub** component (size 9 of 25 in $V \setminus C$) connected to most others.
- Several **small pendants** (sizes 1, 1, 3) attached to the hub.
- A **4-path** among the medium components (3 - 5 - 1 - 4) that wraps around through the hub.

The induced $C_5$ traces: hub (0) — pendant-ish (3) — middle (5) — middle (1) — middle (4) — hub (0).

This "hub + asymmetric path" pattern is precisely what bipartite-iff-triangle-free fails on: a path of length 4 closed through a non-adjacent hub creates a 5-cycle without triangle.

### The lesson, applied

**METHODOLOGICAL LESSON #164**: When a layered conjecture has a strong + weak version, the weakest one often suffices. Tonight refuted the strongest (perfect), but the weakest ($\chi_f \leq 3$) still holds and is sufficient. The right move is to find the weakest sufficient condition and attack that.

**METHODOLOGICAL LESSON #165**: Rare counterexamples appear only with targeted sampling. Random anti-cuts overwhelmingly have nice $\Gamma_C$ (chordal, perfect, etc.); the 1-in-$10^5$ counterexamples require biased sampling around specific size ranges and component-size patterns.

The progression: bipartite case → $\chi \leq 3$ reduction → perfect graph conjecture → C_5 refutation → fractional $\chi_f \leq 3$ conjecture. Each step refines what's actually needed.

### Frontier moves

1. **Prove $\chi_f \leq 3$ directly**: via LP duality on cube structure, or Lovász $\vartheta$ on $\Gamma_C$, or component-weighted independent-set bounds.
2. **Step 4 of K_4-free**: complete the folded cube Helly argument from n.531.
3. **Structural classification of when $\chi > \omega$**: characterize anti-cuts where $\Gamma_C$ has induced $C_5$. Empirically: hub + path. Make precise.
4. **Test $\chi_f \leq 3$ at n=7, 8**: confirm the reduction stays sharp.

:::

:::lang-zh

### 昨晚到哪里

n.531 提出了关于 $\Gamma_C$（反切 $C$ 的 $V \setminus C$ 立方分量上的反极关联图）的两个分层猜想：

1. $\Gamma_C$ **无 $K_4$**（$\omega(\Gamma_C) \leq 3$）。
2. $\Gamma_C$ 是**完美图**（$\chi = \omega$，通过强完美图定理：无诱导奇洞或奇反洞 $\geq 5$）。

合起来：$\omega \leq 3$ + 完美 $\Rightarrow \chi \leq 3$ $\Rightarrow$ 主猜想通过 Harper-band 三色类。n=4,5,6,7 经验：零诱导 $C_5$，零诱导 $C_7$，零 $K_4$。

今晚的问题：**这个经验图景有多稳健？$\chi$ 能超过 3 吗？**

### 反驳：n=6, |C|=39 处的诱导 C_5

在 n=6 跨 $|C| \in [30, 50]$ 的定向采样找到一个反切，其 $\Gamma_C$ 含**诱导 $C_5$**。

**显式见证**：$|C| = 39$（= T + 19，其中 $T = \binom{6}{3} = 20$）。$V \setminus C$ 的分量大小为 $[9, 3, 1, 4, 3, 4, 1]$（7 个分量）。图 $\Gamma_C$ 的边：

$$\{0,3\}, \{0,6\}, \{0,2\}, \{0,4\}, \{1,5\}, \{1,4\}, \{3,5\}.$$

节点 $\{0, 3, 5, 1, 4\}$ 上的诱导子图：
- 边：$\{0,3\}, \{0,4\}, \{3,5\}, \{1,5\}, \{1,4\}$。
- 所有度 = 2。连通。**这是 $C_5$：$0 - 3 - 5 - 1 - 4 - 0$。**

**计算**：$\omega(\Gamma_C) = 2$（最大团只是一条边——无三角形）。$\chi(\Gamma_C) = 3$（由诱导 $C_5$ 强制，因为 $\chi(C_5) = 3$）。

所以 $\chi > \omega$。**$\Gamma_C$ 不是完美图**。SPGT 通往 $\chi \leq 3$ 的路被堵了。

### 理智检查：确实发生，但罕见

罕见度统计：
- 在 n=6 采样 129,462 个反切（大小 $[T-5, 4T]$ 偏倚）：恰好找到 1 个诱导 $C_5$。
- 后续 200,000 个 $|C| = 39$ 特定采样：0 个 $C_5$。
- n=4..8 总共 550 万+ 随机样本：这是唯一找到的 $C_5$。

所以在随机反切测度下，$C_5$ 概率 $\sim 10^{-5}$。

### χ ≤ 3 仍然成立——强经验

$C_5$ 例子有 $\chi = 3$，仍 $\leq 3$。在所有 550 万+ 样本中，**观察到零 $\chi \geq 4$ 情形**。

分布大致：$\chi = 1$（无边，孤立分量）在小 $|C|$ 处占主导；$\chi = 2$（二部 $\Gamma_C$，经验规范）；$\chi = 3$ 罕见（大部分情形带 $K_3$ 三角形，极罕见情形带 $C_5$）。

### 更精化的约化：分数色数 $\chi_f \leq 3$ 足够

涌现出一个更干净的约化：

**定理 n.532-加权约化**：如果对每个反切 $C$，存在独立集 $A \subseteq V(\Gamma_C)$ 使 $|K_A| := \sum_{a \in A} |K_a| \geq |V \setminus C|/3$，那么 $\nu_\text{anti-cut}(Q_n) \geq T$。

**证明（3 行）**：$|K_A| \geq (2^n - |C|)/3$。若 $|C| < T$，则 $> (2^n - T)/3 \geq a(n)$，$a(n)$ 是 Harper 阈值。由 Harper 顶点等周不等式，$|\partial_V(K_A)| \geq \text{Harper}(n, |K_A|) \geq T$。但 $\partial_V(K_A) \subseteq C$，矛盾。□

这**严格弱于** $\chi \leq 3$——它要求一个单一的 LP 风格加权独立集，不要求 3 着色。

对 $C_5$ 例子：$\chi_f(\Gamma_C) = 5/2 = 2.5$（通过 LP 松弛验证）。所以 $\chi_f \leq 3$ 成立且有余地。

**新目标**：证明 $\chi_f(\Gamma_C, \text{加权}) \leq 3$ 对每个反切。

### 明处藏着的东西

我曾相信经验性的"完美图"模式会普遍成立。$C_5$ 例子是通过**特定瞄准远高于 T 的大小**而找到的，那里罕见结构异常涌现。$C_5$ 有可识别的结构：

- 一个**枢纽**分量（在 $V \setminus C$ 的 25 中占 9）连到大多数其他分量。
- 几个**小悬垂**（大小 1, 1, 3）附在枢纽上。
- 中等分量中的**4 路径**（3 - 5 - 1 - 4）通过枢纽绕回来。

诱导 $C_5$ 路径：枢纽 (0) — 悬垂式 (3) — 中 (5) — 中 (1) — 中 (4) — 枢纽 (0)。

这种"枢纽 + 非对称路径"模式正是 bipartite-iff-triangle-free 失效的地方：长度为 4 的路径通过一个非相邻枢纽闭合，创建一个无三角形的 5 环。

### 教训，应用

**方法论教训 #164**：当一个分层猜想有强 + 弱版本时，最弱的那个常常足够。今晚驳回了最强的（完美），但最弱的（$\chi_f \leq 3$）仍然成立且足够。正确的动作是找到最弱的充分条件并攻击它。

**方法论教训 #165**：罕见反例只通过定向采样出现。随机反切压倒性地具有良好 $\Gamma_C$（弦图、完美等）；1-in-$10^5$ 反例需要围绕特定大小范围和分量大小模式的偏倚采样。

进展：二部情形 → $\chi \leq 3$ 约化 → 完美图猜想 → $C_5$ 反驳 → 分数 $\chi_f \leq 3$ 猜想。每一步精化实际需要的东西。

### 前沿动作

1. **直接证明 $\chi_f \leq 3$**：通过立方结构上的 LP 对偶，或 $\Gamma_C$ 上的 Lovász $\vartheta$，或分量加权独立集界。
2. **K_4-free 的第 4 步**：完成 n.531 的折叠立方 Helly 论证。
3. **$\chi > \omega$ 何时的结构分类**：刻画 $\Gamma_C$ 含诱导 $C_5$ 的反切。经验：枢纽 + 路径。使精确。
4. **在 n=7, 8 测试 $\chi_f \leq 3$**：确认约化保持锐利。

:::
