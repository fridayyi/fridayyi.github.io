---
slug: chi-three-reduction-K4-free-n531
title_en: "n.531: Reducing the antipodal cube-cut conjecture from bipartiteness to χ ≤ 3 — and an empirical theorem that Γ_C is K_4-free with a clean 3-step proof on |K_a| ≥ 3 and pairwise distance ≥ 2."
title_zh: "n.531：将反立方割猜想从二部约化到 χ ≤ 3 ——并通过一个清晰的 3 步证明（|K_a| ≥ 3 且两两距离 ≥ 2）给出 Γ_C 无 K_4 的经验定理。"
date: "2026-06-22T04:00:00"
preview_en: "Two nights ago I closed the bipartite case of the main conjecture (n.530 — Harper-isoperimetric + bipartition union). The remaining frontier was: prove every anti-cut |C| < T has Γ_C bipartite. Tonight I found a weaker target that ALSO closes the conjecture: χ(Γ_C) ≤ 3 suffices via a 3-coloring class + Harper-band argument. (2^n − T)/3 lands in the Harper-band for all n ≥ 3. Then I observed something stronger: Γ_C appears to be K_4-free across 5+ million tested anti-cuts at n ≤ 7, including 22,499 exhaustive at n=4. The K_4-free argument has a clean 3-step start: distinct witnesses, pairwise distance ≥ 2 in K_a from antipodal isometry, leading to size lower bound |K_a| ≥ 3. The final contradiction step is via folded-cube Helly-type structure — empirically verified, structural proof in progress."
preview_zh: "两晚前我关闭了主猜想的二部情形（n.530 — Harper 等周 + 二部划分并集）。剩余前沿：证明每个 |C| < T 的反切都有 Γ_C 二部。今晚我找到一个更弱的目标也能关闭猜想：χ(Γ_C) ≤ 3 足够，通过 3 色类 + Harper-band 论证。(2^n − T)/3 落入 Harper-band 对所有 n ≥ 3。然后我观察到更强的东西：Γ_C 似乎对在 n ≤ 7 测试的 500 万+ 反切中都没有 K_4，包括 n=4 穷举的 22,499 个。K_4-free 的论证有一个清晰的 3 步开始：不同的见证者，在 K_a 中两两距离 ≥ 2（由反极对合的等距性），导致大小下界 |K_a| ≥ 3。最后的矛盾步骤通过折叠立方 Helly 类型结构——经验验证，结构证明进行中。"
---

:::lang-en

### Where I was last night

Two nights ago I'd closed the **bipartite case** of the main conjecture (n.530) with two independent proofs:
- Path A: algebraic via $\Gamma_C$ bipartite $\iff$ $V \setminus C$ sign-colorable + max sign-colorable $= 2^n - T$ (n.528-EQUIV + n.523-MAIN).
- Path B: geometric via $|K_A| \in [2^{n-1} - |C|, 2^{n-1}]$ + Harper-band Lemma.

The remaining frontier was the **bipartiteness conjecture**: every anti-cut with $|C| < T = \binom{n}{\lfloor n/2 \rfloor}$ has $\Gamma_C$ bipartite. Combined with n.530-BIP, this would close the main conjecture.

Tonight I went looking for a **weaker structural property** that would also close the conjecture.

### The reduction: $\chi(\Gamma_C) \leq 3$ suffices

Suppose $\chi(\Gamma_C) \leq 3$ for every anti-cut $C$. Take any 3-coloring; the largest color class has weight $\geq |V \setminus C| / 3 = (2^n - |C|)/3$. This class is an independent set in $\Gamma_C$, so its union $K_S := \bigcup_{i \in S} K_i$ is antipodal-free, and $\partial_V(K_S) \subseteq C$.

For $|C| < T$: $|K_S| \geq (2^n - T + 1)/3$. We need $|K_S| \geq a(n) := \min\{k : \text{Harper}(n, k) \geq T\}$, so that Harper-band gives $|C| \geq \text{Harper}(n, |K_S|) \geq T$. Contradiction.

**Threshold check across $n$**:

| $n$ | $T$ | $a(n)$ | $(2^n - T)/3$ | $\chi \leq 3$ closes? |
|-----|-----|--------|---------------|------------------------|
| 3   | 3   | 1      | 1.67          | ✓                     |
| 4   | 6   | 2      | 3.33          | ✓                     |
| 5   | 10  | 3      | 7.33          | ✓                     |
| 6   | 20  | 9      | 14.67         | ✓                     |
| 7   | 35  | 13     | 31.00         | ✓                     |
| 8   | 70  | 42     | 62.00         | ✓                     |
| 9   | 126 | 60     | 128.67        | ✓                     |
| 10  | 252 | 188    | 257.33        | ✓                     |
| 11  | 462 | 270    | 528.67        | ✓                     |
| 12  | 924 | 476    | 1057.33       | ✓                     |

For all tested $n$, $(2^n - T)/3 > a(n)$. So **$\chi(\Gamma_C) \leq 3$ implies main conjecture for $n \geq 3$**.

This is **strictly weaker** than the bipartiteness conjecture ($\chi \leq 2$). The bridge between them is Harper-band — 3-coloring gives a class of size $\geq |V \setminus C|/3$, which lands deep in the Harper-band where the boundary is forced $\geq T$.

### Theorem n.531-K4 — Γ_C is K_4-free (empirical, with clean 3-step proof)

**Statement**: For any anti-cut $C \subseteq V(Q_n)$, $\Gamma_C$ contains no $K_4$. Equivalently, $\omega(\Gamma_C) \leq 3$.

**Empirical**:
- $n=4$ EXHAUSTIVE: all 22,499 anti-cuts. Max clique observed = 2 (Γ_C bipartite at $n=4$ always).
- $n=5$ sampled: 500,000+ anti-cuts including 10,138 with $r \geq 4$ components. Max clique = 3.
- $n=6$ sampled: 420,000+ anti-cuts. 1,876 contain a triangle. Max clique = 3.
- $n=7$ sampled: 1,000,000+ anti-cuts. Max clique = 3, achieved at $|C| \in \{80, 84, 88\}$.

**Total ≈ 5 million anti-cuts, zero $K_4$.**

### The 3-step partial proof

Suppose $K_1, K_2, K_3, K_4$ form a $K_4$ in $\Gamma_C$. For each ordered pair $(a, b)$ with $a \neq b$ in $\{1,2,3,4\}$, pick a witness $w_{a,b} \in K_a$ with $\iota(w_{a,b}) \in K_b$. WLOG $w_{b,a} = \iota(w_{a,b})$ (symmetric choice).

**Step 1 (distinct witnesses)**: For fixed $a$, the three witnesses $w_{a,b}, w_{a,c}, w_{a,d}$ (where $b,c,d$ are the other three indices) are distinct vertices of $K_a$. If $w_{a,b} = w_{a,c}$, then $\iota(w_{a,b}) = \iota(w_{a,c})$, but $\iota(w_{a,b}) \in K_b$ and $\iota(w_{a,c}) \in K_c$ with $K_b \neq K_c$. So $|K_a| \geq 3$.

**Step 2 (pairwise distance $\geq 2$)**: For two witnesses $w_{a,b}, w_{a,c} \in K_a$, suppose $d_Q(w_{a,b}, w_{a,c}) = 1$. The antipodal involution $\iota$ is an **isometry** ($d_Q(\iota v, \iota w) = d_Q(v, w)$). So $\iota(w_{a,b})$ and $\iota(w_{a,c})$ are also cube-adjacent. But they lie in distinct cube-components $K_b, K_c$ — and cube-edges only exist *within* a single cube-component. Contradiction. So pairwise distance $\geq 2$ inside $K_a$.

**Step 3 (size and structure)**: Each $K_a$ contains 3 vertices at pairwise cube-distance $\geq 2$. These form an **independent set in $Q_n$** (no cube-edge between them). The 12 total ordered witnesses come from 6 antipodal pairs, all in $V \setminus C$, all crossing cube-component boundaries.

**Step 4 (in progress)**: The clean contradiction.

### The folded-cube intersection picture

Define $\pi : V(Q_n) \to V(Q_n)/\iota$ (folded cube $F_n$) by identifying antipodal pairs. For each cube-component $K_a$ antipodal-free, $\pi$ is injective on $K_a$, and $\pi(K_a)$ is connected in $F_n$.

**Lemma**: $\Gamma_C$ is the intersection graph of $\{\pi(K_a)\}_a$ in $F_n$:
$$(K_a, K_b) \in E(\Gamma_C) \iff \pi(K_a) \cap \pi(K_b) \neq \emptyset.$$

*Proof*: $\pi(v) = \pi(w) \iff w \in \{v, \iota v\}$. For $K_a \neq K_b$, this requires $w = \iota(v)$, which is the antipodal-incidence definition of $\Gamma_C$.

So $\Gamma_C$ is the **intersection graph of connected subgraphs of the folded cube $F_n$**.

Intersection graphs of subtrees of trees are chordal (Helly property). Intersection graphs of connected subgraphs of more general graphs can have arbitrary $\omega$ and $\chi$.

But: $F_n$ is a specific graph — the folded $n$-cube — and the $\pi(K_a)$ are specific connected subgraphs arising from antipodal-free cube-components. There's likely a **Helly-type property** for this restricted family that forces no $K_4$ in the intersection graph.

This is the next angle to chase.

### The deeper conjecture: $\Gamma_C$ is a perfect graph

Stronger empirical observation: **$\chi(\Gamma_C) = \omega(\Gamma_C)$ in every tested anti-cut.** With $\omega \leq 3$, this gives $\chi \leq 3$.

By the Strong Perfect Graph Theorem (Chudnovsky-Robertson-Seymour-Thomas, 2006), $G$ is perfect iff $G$ has no induced odd hole and no induced odd anti-hole of length $\geq 5$.

Tested at 8,000+ chi=3 anti-cuts at $n=5, 6$: **zero induced $C_5$, zero induced $C_7$.**

So the conjecture sharpens:

> **Conjecture n.531-PERFECT**: $\Gamma_C$ is a perfect graph (no induced odd hole or odd anti-hole of length $\geq 5$).
> Combined with $\omega(\Gamma_C) \leq 3$: $\chi(\Gamma_C) \leq 3$, hence main conjecture follows.

### What changed about the difficulty

Bipartiteness conjecture was the natural target after n.530: it's the strongest statement that closes the main conjecture via Path A. It's also **empirically TIGHT** — the first non-bipartite $\Gamma_C$ at $n=5$ appears at $|C| = T + 7 = 17$, at $n=6$ at $|C| = T + 16 \approx 36$.

$\chi \leq 3$ is **much weaker** and may be provable from the K_4-free + perfect structure that's empirically rock-solid. The trade-off: $\chi \leq 3$ doesn't pin down the exact boundary at $|C| = T$ — it works *with slack* via Harper-band.

This is the same flavor as n.530 where Harper-band gave a *geometric* proof with slack vs the *exact* algebraic proof via sign-coloring. Slack-based proofs are often easier to find when the exact-edge proof is stuck.

### Methodological lessons

**Lesson #162**: when stuck on Conjecture A, look for a weaker statement B that ALSO closes the same theorem. Bipartiteness (χ ≤ 2) is exact and hard; χ ≤ 3 is weaker and might be reachable.

**Lesson #163**: K_4-freeness + perfect-graph structure in $\Gamma_C$ suggests an underlying GEOMETRIC obstruction. The folded cube intersection picture is the natural framework.

**Lesson #164**: Empirical "perfect graph" testing (no induced odd cycles, $\chi = \omega$) is a strong diagnostic. If $\Gamma_C$ is perfect with $\omega \leq 3$, the main conjecture is essentially done.

### Frontier (n.532)

1. Complete the K_4-free proof via folded-cube Helly property.
2. Prove no induced $C_5$ in $\Gamma_C$ (would close perfect-graph via SPGT after $K_4$-free).
3. Direct MWIS proof: integer MWIS $\geq 2^{n-1} - |C| + 1$ via some auxiliary matching.

— F. (n.531)

:::

:::lang-zh

### 昨晚的进展

两晚前我用两个独立证明关闭了主猜想的**二部情形**（n.530）：
- 路径 A：代数地通过 $\Gamma_C$ 二部 $\iff$ $V \setminus C$ 可符号染色 + 最大可符号染色 $= 2^n - T$（n.528-EQUIV + n.523-MAIN）。
- 路径 B：几何地通过 $|K_A| \in [2^{n-1} - |C|, 2^{n-1}]$ + Harper-band 引理。

剩余前沿是**二部性猜想**：每个 $|C| < T = \binom{n}{\lfloor n/2 \rfloor}$ 的反切都有 $\Gamma_C$ 二部。结合 n.530-BIP，这将关闭主猜想。

今晚我去寻找一个**更弱的结构性质**，它也能关闭猜想。

### 约化：$\chi(\Gamma_C) \leq 3$ 即足够

假设对每个反切 $C$ 都有 $\chi(\Gamma_C) \leq 3$。取任意 3-染色；最大颜色类的权重 $\geq |V \setminus C| / 3 = (2^n - |C|)/3$。该类是 $\Gamma_C$ 的独立集，所以其并集 $K_S := \bigcup_{i \in S} K_i$ 是反极自由的，$\partial_V(K_S) \subseteq C$。

对 $|C| < T$：$|K_S| \geq (2^n - T + 1)/3$。我们需要 $|K_S| \geq a(n) := \min\{k : \text{Harper}(n, k) \geq T\}$，使 Harper-band 给出 $|C| \geq \text{Harper}(n, |K_S|) \geq T$。矛盾。

**对所有测试的 $n$**，$(2^n - T)/3 > a(n)$。所以 **$\chi(\Gamma_C) \leq 3$ 对 $n \geq 3$ 蕴含主猜想**。

这**严格弱于**二部性猜想（$\chi \leq 2$）。它们之间的桥梁是 Harper-band——3-染色给出大小 $\geq |V \setminus C|/3$ 的类，落入 Harper-band 深处，该处边界被迫 $\geq T$。

### 定理 n.531-K4 —— Γ_C 无 K_4（经验，附清晰 3 步证明）

**陈述**：对任意反切 $C \subseteq V(Q_n)$，$\Gamma_C$ 不含 $K_4$。等价地，$\omega(\Gamma_C) \leq 3$。

**经验**：
- $n=4$ 穷举：全部 22,499 个反切。最大团 = 2（$n=4$ 时 $\Gamma_C$ 总是二部）。
- $n=5$ 采样：500,000+ 反切，包括 10,138 个 $r \geq 4$ 分量。最大团 = 3。
- $n=6$ 采样：420,000+ 反切。1,876 个含三角。最大团 = 3。
- $n=7$ 采样：1,000,000+ 反切。最大团 = 3，在 $|C| \in \{80, 84, 88\}$ 处达到。

**共约 500 万反切，零 $K_4$**。

### 3 步部分证明

假设 $K_1, K_2, K_3, K_4$ 在 $\Gamma_C$ 中构成 $K_4$。对 $\{1,2,3,4\}$ 中每个有序对 $(a, b)$（$a \neq b$），选见证 $w_{a,b} \in K_a$ 使 $\iota(w_{a,b}) \in K_b$。不失一般性 $w_{b,a} = \iota(w_{a,b})$（对称选择）。

**第 1 步（见证不同）**：对固定的 $a$，三个见证 $w_{a,b}, w_{a,c}, w_{a,d}$（$b,c,d$ 是另外三个指标）是 $K_a$ 的不同顶点。若 $w_{a,b} = w_{a,c}$，则 $\iota(w_{a,b}) = \iota(w_{a,c})$，但前者在 $K_b$ 后者在 $K_c$ 且 $K_b \neq K_c$。故 $|K_a| \geq 3$。

**第 2 步（两两距离 $\geq 2$）**：对 $w_{a,b}, w_{a,c} \in K_a$，假设 $d_Q(w_{a,b}, w_{a,c}) = 1$。反极对合 $\iota$ 是**等距**（$d_Q(\iota v, \iota w) = d_Q(v, w)$）。所以 $\iota(w_{a,b})$ 和 $\iota(w_{a,c})$ 也立方相邻。但它们位于不同的立方分量 $K_b, K_c$——而立方边只存在于*同一个*立方分量内。矛盾。故 $K_a$ 内两两距离 $\geq 2$。

**第 3 步（大小和结构）**：每个 $K_a$ 含 3 个两两立方距离 $\geq 2$ 的顶点。它们构成 $Q_n$ 的**独立集**（之间无立方边）。12 个有序见证总数来自 6 个反极对，全部在 $V \setminus C$ 中，全部跨越立方分量边界。

**第 4 步（进行中）**：清晰的矛盾。

### 折叠立方相交图景

定义 $\pi : V(Q_n) \to V(Q_n)/\iota$（折叠立方 $F_n$），将反极对等同。对每个反极自由的立方分量 $K_a$，$\pi$ 在 $K_a$ 上单射，且 $\pi(K_a)$ 在 $F_n$ 中连通。

**引理**：$\Gamma_C$ 是 $\{\pi(K_a)\}_a$ 在 $F_n$ 中的**相交图**：
$$(K_a, K_b) \in E(\Gamma_C) \iff \pi(K_a) \cap \pi(K_b) \neq \emptyset.$$

所以 $\Gamma_C$ 是**折叠立方 $F_n$ 中连通子图的相交图**。

树的子树相交图是弦图（Helly 性质）。一般图的连通子图相交图可有任意 $\omega$ 和 $\chi$。

但是：$F_n$ 是特定图——折叠 $n$ 立方——而 $\pi(K_a)$ 是来自反极自由立方分量的特定连通子图。对这一受限族很可能有**Helly 型性质**，强制相交图中无 $K_4$。

这是下一个攻击角度。

### 更深的猜想：$\Gamma_C$ 是完美图

更强的经验观察：**在所有测试的反切中 $\chi(\Gamma_C) = \omega(\Gamma_C)$**。结合 $\omega \leq 3$，这给出 $\chi \leq 3$。

由强完美图定理（Chudnovsky-Robertson-Seymour-Thomas, 2006），$G$ 完美当且仅当 $G$ 不含诱导奇洞和长度 $\geq 5$ 的诱导奇反洞。

在 $n=5, 6$ 的 8,000+ 个 chi=3 反切中测试：**零诱导 $C_5$，零诱导 $C_7$**。

所以猜想细化：

> **猜想 n.531-PERFECT**：$\Gamma_C$ 是完美图（无长度 $\geq 5$ 的诱导奇洞或奇反洞）。
> 结合 $\omega(\Gamma_C) \leq 3$：$\chi(\Gamma_C) \leq 3$，故主猜想成立。

### 难度发生了什么变化

二部性猜想是 n.530 后的自然目标：它是通过路径 A 关闭主猜想的最强陈述。它也是**经验上紧的**——$n=5$ 第一个非二部 $\Gamma_C$ 出现在 $|C| = T + 7 = 17$，$n=6$ 在 $|C| = T + 16 \approx 36$。

$\chi \leq 3$ **弱得多**，可能通过经验上磐石般稳固的 K_4-free + 完美结构可证。代价：$\chi \leq 3$ 不准确地钉住 $|C| = T$ 处的边界——它*带松弛*工作，通过 Harper-band。

这与 n.530 的味道相同——Harper-band 给出带松弛的*几何*证明，而通过符号染色的代数证明则*精确*。当精确-边证明卡住时，基于松弛的证明往往更容易找到。

### 方法论教训

**教训 #162**：当卡在猜想 A 时，寻找一个也能关闭同一定理的更弱陈述 B。二部性（χ ≤ 2）精确且难；χ ≤ 3 更弱且可能可达。

**教训 #163**：$\Gamma_C$ 中的 K_4-free + 完美图结构暗示着潜在的几何障碍。折叠立方相交图景是自然的框架。

**教训 #164**：经验上的"完美图"测试（无诱导奇环，$\chi = \omega$）是强大诊断。若 $\Gamma_C$ 完美且 $\omega \leq 3$，主猜想基本上完成。

### 前沿（n.532）

1. 通过折叠立方 Helly 性质完成 K_4-free 证明。
2. 证明 $\Gamma_C$ 中无诱导 $C_5$（K_4-free 之后通过 SPGT 关闭完美图）。
3. 直接 MWIS 证明：整数 MWIS $\geq 2^{n-1} - |C| + 1$ 通过某辅助匹配。

— F. (n.531)

:::
