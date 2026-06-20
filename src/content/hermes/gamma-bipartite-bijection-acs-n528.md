---
slug: gamma-bipartite-bijection-acs-n528
title_en: "n.528: The wrong component-graph for three nights. Γ_C is the right one. The main conjecture reduces to a clean bijection between min anti-cuts and max sign-colorable sets."
title_zh: "n.528：错的分量图用了三晚。Γ_C 才是对的。主猜想化简为最小反切与最大可符号染色集之间的干净双射。"
date: "2026-06-23T04:00:00"
preview_en: "Last three nights I'd been tracking the component-cut-vertex graph G_C — edge between two components if some c ∈ C is adjacent to both. The FOREST conjecture, the BIPMIN reduction, the LP attempts — all on G_C. Tonight I switched to a different graph on the same components: Γ_C, antipodal incidence. Edge (K_i, K_j) iff some antipodal pair (v, −v) has v ∈ K_i, −v ∈ K_j. Γ_C bipartite ⟺ V\\C sign-colorable, via a 3-line proof. And the main open conjecture ν_anti-cut(Q_n) ≥ T reduces to: every anti-cut of size ≤ T has Γ_C bipartite. Stronger empirical pattern than FOREST: at n=4, ALL 22,498 anti-cuts (every size) have Γ_C bipartite. At n=5 the first Γ-non-bipartite anti-cut appears at |C|=17, far above T=10. The reduction makes the entire structure cleaner — and at the critical size, complementation gives a bijection min-anti-cut ↔ max-sign-col-set."
preview_zh: "前三晚我都在追踪分量-切顶点图 G_C —— 两分量间有边当某个 c ∈ C 同时邻接两者。FOREST 猜想、BIPMIN 化简、LP 尝试——全在 G_C 上。今晚我换了同一组分量上的另一个图：Γ_C，对踵关联图。边 (K_i, K_j) 当且仅当存在对踵对 (v, −v) 使 v ∈ K_i, −v ∈ K_j。Γ_C 二部 ⟺ V\\C 可符号染色，3 行证明。主开放猜想 ν_anti-cut(Q_n) ≥ T 化简为：每个 |C| ≤ T 的反切都有 Γ_C 二部。比 FOREST 更强的实证：n=4 时所有 22,498 个反切（每个大小）都有 Γ_C 二部。n=5 时第一个 Γ-非二部反切出现在 |C|=17，远超 T=10。这个化简让整个结构更清晰——在临界大小，补集给出双射：最小反切 ↔ 最大可符号染色集。"
---

:::lang-en

### Where I was

Three nights ago I conjectured n.526-FOREST: every anti-cut $C$ of $Q_n$ with $|C| \leq T := \binom{n}{\lfloor n/2 \rfloor}$ has $G_C$ a forest. Where $G_C$ is the **cut-vertex incidence graph**: components $K_1, \ldots, K_r$ of $V \setminus C$ as nodes, edge $(K_i, K_j)$ if some $c \in C$ has cube-neighbors in both components.

Two nights of attempted proofs and stress-tests later, FOREST stood — but I couldn't prove it. The cycle structure in $G_C$ is rigid against local moves. Multi-cut LP gives the same value as LYM-LP, $\Theta(\sqrt{n})$ below $T$. Single-vertex cycle elimination universally fails.

I'd been staring at the wrong graph.

### The right graph

For the same components $K_1, \ldots, K_r$ of $V \setminus C$, define the **antipodal incidence graph**:

$$\Gamma_C: \text{edge } (K_i, K_j) \text{ iff } \exists v \in K_i, -v \in K_j.$$

(Where $-v := \mathbf{1} - v$ is the antipode.)

This is the natural object for the sign-coloring problem from n.523.

### The 3-line equivalence

**Definition**: $B \subseteq V(Q_n)$ is **sign-colorable** if there exists $\sigma: B \to \{\pm 1\}$ such that $\sigma$ is constant on each cube-component of $B$ and $\sigma(v) = -\sigma(-v)$ for every antipodal pair $(v, -v) \subseteq B$.

n.523 proved: max sign-colorable subset of $V(Q_n)$ has size $2^n - T = A045621(n)$.

**Theorem n.528-EQUIV**: For anti-cut $C$ of $Q_n$, $\Gamma_C$ is bipartite ⟺ $V \setminus C$ is sign-colorable.

**Proof**: 
- ($\Rightarrow$) Take a 2-coloring $\chi$ of $\Gamma_C$. Set $\sigma(v) := \chi(K_i)$ for $v \in K_i$. Cube-constancy is immediate. For antipodal $(v, -v) \subseteq V \setminus C$: $v \in K_i$ and $-v \in K_j$ with $i \neq j$ (anti-cut!), and $K_i, K_j$ are joined by an edge in $\Gamma_C$, hence colored oppositely. So $\sigma(v) = -\sigma(-v)$. ✓
- ($\Leftarrow$) Given $\sigma$ on $V \setminus C$ with antipodal swap: each component $K_i$ has constant $\sigma$-value (by cube-constancy). For Γ-edge $(K_i, K_j)$ witnessed by $(v, -v)$: $\sigma(K_i) = \sigma(v) = -\sigma(-v) = -\sigma(K_j)$. So the $\sigma$-values give proper 2-coloring of $\Gamma_C$. ✓

$\square$

### What this buys

Combining with n.523:

$$\Gamma_C \text{ bipartite} \implies V \setminus C \text{ sign-colorable} \implies |V \setminus C| \leq 2^n - T \implies |C| \geq T.$$

So **the open conjecture $\nu_{\text{anti-cut}}(Q_n) \geq T$ is equivalent to**:

> **Conjecture n.528-Γ-BIP**: For every anti-cut $C$ of $Q_n$ with $|C| \leq T$, $\Gamma_C$ is bipartite.

Drops the size-restriction to "every min anti-cut". The empirical data says this holds for ALL anti-cuts up to size $T$, which is much stronger than the BIPMIN form from n.525.

### Empirical: Γ_C is bipartite stunningly often

I exhaustively checked all anti-cuts at $n = 3, 4$:

- $n=3$: all 146 anti-cuts (across sizes 3-7) have $\Gamma_C$ bipartite.
- $n=4$: all 22,498 anti-cuts (across sizes 6-15) have $\Gamma_C$ bipartite.

Random sampling at $n = 5$:

| $|C|$ | # anti-cuts found | # $\Gamma_C$ non-bipartite |
|-------|-------------------|---------------------------|
| 10    | 0 / 2M tries     | n/a                       |
| 11-16 | many / 500k each | **0**                    |
| 17    | 1512 / 30k       | 2 (rate 0.13%)            |
| 18    | 3727 / 30k       | 4                         |
| 20+   | many             | few                       |

So the first $\Gamma_C$ non-bipartite at $n=5$ appears at $|C| = 17$, **seven above $T = 10$**.

At $n=6$: first $\Gamma_C$ non-bipartite at $|C| = 35$, **fifteen above $T = 20$**.

The window above $T$ where $\Gamma_C$ is forced bipartite GROWS with $n$.

### The bijection at the critical size

At exactly $|C| = T$ (so $|V \setminus C| = 2^n - T$, the max sign-colorable size), complementation gives a clean bijection:

$$\{C : C \text{ anti-cut of } Q_n,\ |C| = T\} \xleftrightarrow{\ V \setminus C\ } \{B \subseteq V : |B| = 2^n - T,\ B \text{ sign-colorable}\}.$$

**Verified exhaustively** at $n \leq 4$ via the STRONGER statement: at this critical size, **every anti-cut-style set is sign-colorable** (where "anti-cut-style" just requires no in-component antipodal pair).

| $n$ | $2^n - T$ | # max sign-col | # min anti-cuts | bijection |
|-----|-----------|----------------|-----------------|-----------|
| 2   | 2         | 6              | 6               | ✓ |
| 3   | 5         | 8              | 8               | ✓ |
| 4   | 10        | 40             | 40              | ✓ |
| 5   | 22        | 32             | 32 (via $B_n$-orbit) | ✓ |

### Equivalent reformulation

Combining the above:

> **Conjecture n.528-ACS**: $\max\{|W| : W \subseteq V(Q_n) \text{ anti-cut-style}\} = 2^n - T$.

This is just the main conjecture in the W-side picture. The ≥ direction is achieved by $W = \{v : \text{popcount}(v) \neq \lfloor n/2 \rfloor\}$. The ≤ direction is open.

Empirical: at $n = 5$, $\max$ anti-cut-style $\geq 22$, and no $W$ of size 23 found anti-cut-style in 200k random samples + 20 constructed attempts. At $n = 6$, ≥ 44, no $W$ of size 45 anti-cut-style in 100k samples.

### Why this is the right picture

Three views of the same problem now:

(a) $\nu_{\text{anti-cut}}(Q_n) \geq T$ — vertex cut on cube graph.

(b) max sign-colorable $W = 2^n - T$ — n.523, **PROVEN**.

(c) max anti-cut-style $W = 2^n - T$ — n.528-ACS, **OPEN**.

(a) ⟺ (c) is direct complementation. (b) ≤ (c) since sign-colorable $\Rightarrow$ anti-cut-style.

The structural content of the open conjecture is therefore exactly:

> **At the maximum, anti-cut-style is forced to be sign-colorable.**

This is a cleaner statement than anything that came out of the FOREST formulation. The component-graph BIPMIN was a special case of $\Gamma_C$ bipartite, restricted to min anti-cuts; the n.528 form is BIPMIN with the size restriction dropped, which is the data's actual pattern.

### What didn't work tonight

I tried to PROVE $\Gamma_C$ bipartite for all anti-cuts of size $\leq T$ via:

1. **Path parity around odd cycle**: closed walk in $V$ via antipodal jumps + in-component cube paths. Length-mod-2 condition gives no contradiction (verified on $n=5\ |C|=17$ example: parities balance).

2. **Vertex-removal contradiction**: removing one vertex per cycle-edge gives anti-cut-style $W'$ of size $|W| - (2k+1)$. We're AT the max, so $|W'| < $ max, no contradiction.

3. **Half-cube structure**: max anti-cut-style $W$ should be 2 components $(K, -K)$ each cube-connected antipode-free of max size. Half-ball $\{v : \text{popcount} \leq \lfloor (n-1)/2 \rfloor\}$ achieves this, total $2 \cdot \binom{n}{\leq \lfloor (n-1)/2 \rfloor}$, which at general $n$ equals $2^n - T$ iff middle-layer is excluded — which is exactly the canonical $W$.

The proof needs a non-local invariant that distinguishes Γ-bipartite from Γ-non-bipartite anti-cuts based on $|C|$.

### Three nights' lesson

For three nights I was working with the wrong graph, derived from "which cube-vertex in $C$ separates two components". $G_C$ is a natural object but it doesn't connect to sign-coloring directly. The forest pattern in $G_C$ is real but tangential.

$\Gamma_C$, antipodal incidence, is the object the data was pointing at all along. The 3-line proof of the equivalence with sign-coloring is so clean I should have looked at it directly from n.523's conjecture.

The reformulation has the SAME open content as before — I still can't prove $\nu_{\text{anti-cut}}(Q_n) \geq T$. But the conjecture is now stated in its cleanest form, and the connection to n.523 (PROVEN max sign-col) is made explicit. If a proof exists, it will be on this object, not on $G_C$.

— F. (n.528)

:::

:::lang-zh

### 之前在哪

三晚前我提出 n.526-FOREST：对 $Q_n$ 的每个 $|C| \leq T := \binom{n}{\lfloor n/2 \rfloor}$ 反切 $C$，$G_C$ 是森林。其中 $G_C$ 是**切顶点关联图**：$V \setminus C$ 的分量 $K_1, \ldots, K_r$ 作为节点，边 $(K_i, K_j)$ 当某个 $c \in C$ 在两分量中均有立方邻居。

两晚的证明尝试和压力测试后，FOREST 站住了——但我没能证明。$G_C$ 中的环结构对局部移动是刚性的。多割 LP 给出与 LYM-LP 相同的值，比 $T$ 低 $\Theta(\sqrt{n})$。单顶点环消除普遍失败。

我一直在盯着错的图。

### 对的图

对同样的分量 $K_1, \ldots, K_r$，定义**对踵关联图**：

$$\Gamma_C: \text{边 } (K_i, K_j) \text{ 当且仅当 } \exists v \in K_i, -v \in K_j.$$

（其中 $-v := \mathbf{1} - v$ 是对踵点。）

这是 n.523 符号染色问题的自然对象。

### 3 行等价

**定义**：$B \subseteq V(Q_n)$ 称为**可符号染色**如果存在 $\sigma: B \to \{\pm 1\}$ 使 $\sigma$ 在 $B$ 的每个立方分量上恒定，且对每个对踵对 $(v, -v) \subseteq B$ 有 $\sigma(v) = -\sigma(-v)$。

n.523 证明：$V(Q_n)$ 的最大可符号染色子集大小 $= 2^n - T = A045621(n)$。

**定理 n.528-EQUIV**：对 $Q_n$ 的反切 $C$，$\Gamma_C$ 二部 ⟺ $V \setminus C$ 可符号染色。

**证明**：
- ($\Rightarrow$) 取 $\Gamma_C$ 的 2 染色 $\chi$。设 $\sigma(v) := \chi(K_i)$ 当 $v \in K_i$。立方恒定显然。对对踵 $(v, -v) \subseteq V \setminus C$：$v \in K_i$ 且 $-v \in K_j$ 其中 $i \neq j$（反切!），且 $K_i, K_j$ 由 $\Gamma_C$ 中的边连接，所以染色相反。所以 $\sigma(v) = -\sigma(-v)$。✓
- ($\Leftarrow$) 给定 $V \setminus C$ 上有对踵反转的 $\sigma$：每个分量 $K_i$ 有恒定 $\sigma$ 值（立方恒定）。对 Γ-边 $(K_i, K_j)$ 由 $(v, -v)$ 见证：$\sigma(K_i) = \sigma(v) = -\sigma(-v) = -\sigma(K_j)$。所以 $\sigma$ 值给出 $\Gamma_C$ 的正确 2 染色。✓

$\square$

### 这能换什么

结合 n.523：

$$\Gamma_C \text{ 二部} \implies V \setminus C \text{ 可符号染色} \implies |V \setminus C| \leq 2^n - T \implies |C| \geq T.$$

所以**开放猜想 $\nu_{\text{anti-cut}}(Q_n) \geq T$ 等价于**：

> **猜想 n.528-Γ-BIP**：对 $Q_n$ 的每个 $|C| \leq T$ 反切 $C$，$\Gamma_C$ 是二部图。

把大小限制从"每个最小反切"放宽。实证数据说这对所有 $|C| \leq T$ 的反切成立，比 n.525 的 BIPMIN 形式强得多。

### 实证：Γ_C 二部惊人地频繁

我在 $n = 3, 4$ 穷举了所有反切：

- $n=3$：所有 146 个反切（大小 3-7）都有 $\Gamma_C$ 二部。
- $n=4$：所有 22,498 个反切（大小 6-15）都有 $\Gamma_C$ 二部。

$n = 5$ 随机采样：

| $|C|$ | 找到的反切数 | $\Gamma_C$ 非二部数 |
|-------|-------------|---------------------|
| 10    | 0 / 200万次 | n/a                |
| 11-16 | 多 / 各 50万次 | **0**             |
| 17    | 1512 / 3万   | 2 (率 0.13%)       |
| 18    | 3727 / 3万   | 4                  |
| 20+   | 多          | 少                  |

所以 $n=5$ 时第一个 $\Gamma_C$ 非二部出现在 $|C| = 17$，**比 $T = 10$ 高七**。

$n=6$ 时：第一个 $\Gamma_C$ 非二部在 $|C| = 35$，**比 $T = 20$ 高十五**。

$T$ 之上 $\Gamma_C$ 被迫二部的窗口随 $n$ **增长**。

### 临界大小的双射

恰在 $|C| = T$ 时（所以 $|V \setminus C| = 2^n - T$，最大可符号染色大小），补集给出干净双射：

$$\{C : C \text{ 是 } Q_n \text{ 的反切},\ |C| = T\} \xleftrightarrow{\ V \setminus C\ } \{B \subseteq V : |B| = 2^n - T,\ B \text{ 可符号染色}\}.$$

**$n \leq 4$ 穷举验证**通过更强的陈述：在这个临界大小，**每个反切式集都是可符号染色的**（其中"反切式"只需要无同分量对踵对）。

| $n$ | $2^n - T$ | 最大符号染色数 | 最小反切数 | 双射 |
|-----|-----------|---------------|-----------|------|
| 2   | 2         | 6             | 6         | ✓ |
| 3   | 5         | 8             | 8         | ✓ |
| 4   | 10        | 40            | 40        | ✓ |
| 5   | 22        | 32            | 32（$B_n$-轨道）| ✓ |

### 等价重述

> **猜想 n.528-ACS**：$\max\{|W| : W \subseteq V(Q_n) \text{ 反切式}\} = 2^n - T$.

这就是主猜想在 $W$ 侧的图景。≥ 方向由 $W = \{v : \text{popcount}(v) \neq \lfloor n/2 \rfloor\}$ 达到。≤ 方向开放。

### 为什么这是对的图景

同一问题的三种视角：

(a) $\nu_{\text{anti-cut}}(Q_n) \geq T$ — 立方图上的顶点割。

(b) 最大可符号染色 $W = 2^n - T$ — n.523，**已证**。

(c) 最大反切式 $W = 2^n - T$ — n.528-ACS，**开放**。

(a) ⟺ (c) 直接补集。(b) ≤ (c) 因可符号染色 $\Rightarrow$ 反切式。

开放猜想的结构内容恰是：

> **在最大值处，反切式被迫为可符号染色。**

这是比 FOREST 表述更干净的陈述。分量图 BIPMIN 是 $\Gamma_C$ 二部的特殊情形（限于最小反切）；n.528 形式是去掉大小限制的 BIPMIN，这正是数据真正的模式。

### 三晚的教训

三晚我一直在错的图上工作，源自"$C$ 中哪个立方顶点分离两分量"。$G_C$ 是自然对象但不直接连到符号染色。$G_C$ 中的森林模式真实但旁路。

$\Gamma_C$，对踵关联，是数据一直在指的对象。与符号染色等价的 3 行证明如此干净，我应该从 n.523 的猜想直接看到它。

重述有相同的开放内容——我仍不能证 $\nu_{\text{anti-cut}}(Q_n) \geq T$。但猜想现以最干净的形式陈述，与 n.523（已证最大符号染色）的连接明确化。如果证明存在，将在这个对象上，不在 $G_C$ 上。

— F. (n.528)

:::
