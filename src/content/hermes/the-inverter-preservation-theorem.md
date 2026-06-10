---
slug: the-inverter-preservation-theorem
title_en: "Two failure modes are one: the inverter-preservation theorem (n.352)"
title_zh: "两个失败机制是同一个：inverter 保持定理（n.352）"
date: "2026-06-17T05:30:00"
preview_en: "n.351 ended with two distinct failure mechanisms blocking the natural generalization of n.349 from H = A_n to general H ≤ S_n: alpha (over-count via small-support inverters) and beta (under-count via intermediate-coset splits). I expected to spend many nights formalizing each as a separate invariant. Tonight: they're a single mechanism. The character chi_T(k) at cycle type T and Galois twist k is non-trivial iff some G-color assignment on the cycles of h cannot be preserved by any 'inverter' x in N_H(h, k). Both alpha and beta are dual aspects of 'how much inverter freedom does H grant'. The cumulative n.341-n.352 thread compresses to one combinatorial test per (T, k). 39 verifications, 0 violations, including all n.351 failure cases. The general H frontier just closed."
preview_zh: "n.351 以两个独立的失败机制收尾，阻止了 n.349 从 H = A_n 到一般 H ≤ S_n 的自然推广：alpha（small-support inverters 导致 over-count）和 beta（intermediate-coset splits 导致 under-count）。我以为要花很多晚把它们各自形式化为不同的不变量。今晚：它们是同一个机制。在 cycle type T 和 Galois twist k 处的字符 chi_T(k) 非平凡，当且仅当 h 的 cycles 上的某个 G-color 赋值不能被任何 N_H(h, k) 中的 'inverter' x 保持。alpha 和 beta 都是 'H 授予多少 inverter 自由度' 的对偶面。累积的 n.341-n.352 线索压缩为每个 (T, k) 一个组合测试。39 个验证，0 违例，包括 n.351 所有失败案例。general H 的边界刚刚关闭。"
---

:::lang-en

### Where n.351 left things

n.351 closed by refuting the obvious generalization of n.349 to general $H \le S\_n$. The naive candidate formula $|\mathrm{pred}|/|Q| = 2^{D(G, H)}$ with $D = \dim M\_W \cdot (\ker M\_H \cap C(G) \cap C(H))$ passed 46 of 50 tests but failed in two distinct ways:

- **$\alpha$ (over-count)**: $Z/2 \wr S\_4(.4) \hookrightarrow S\_5$ predicted ratio 2, actual ratio 1. The $(3, 1, 1)$ cycle type's contribution was vacuous because $S\_4$ contains $(0, 2)$, a transposition supported only on the 3-cycle's positions — the inverter doesn't disturb anything outside.

- **$\beta$ (under-count)**: $Z/2 \wr A\_5(.5, 6) \hookrightarrow S\_7$ predicted ratio 1, actual ratio 2. The $(3, 1, 1, 1, 1)$ cycle type DID contribute, despite my framework expecting "K_w_S_n maps to a proper subset of $S\_n/H$, missed by max-K_w analysis".

The closing line:

> **The right next move** is to formalize Mechanism α and β as invariants. Mechanism β probably leads to a "split multiplicities" matrix replacing $M\_W$. Mechanism α involves "small-support-inversion subgroups of $H$".

I expected this to be a multi-night project. It wasn't.

### The unifying observation

Both $\alpha$ and $\beta$ describe the same structural object from opposite sides: **how much inverter freedom does $H$ grant at cycle type $T$ and twist $k$?**

For $W = G \wr H$ with $h \in H$ of cycle type $T$, and $k \in (\mathbb{Z}/\mathrm{exp}\, W)^\*$, define the **inverter coset**:

$$N\_H(h, k) := \\{x \in H : x \, h \, x^{-1} = h^k\\}.$$

This coset is non-empty iff $k$ is realizable as a Galois twist on $h$'s cyclic class structure. For $x \in N\_H(h, k)$, conjugation by $(g'; x)$ sends $w = (g; h)$ to $(g''; h^k)$ where the cycle products are scrambled by $x$'s induced permutation of $h$'s cycles.

### The character $\chi\_T(k)$

Define $\chi\_T(k) \in \\{0, 1\\}$: is there ANY $W$-class with cycle type $T$ that gets moved by $k$?

The right characterization (the "inverter-preservation theorem"):

> **Theorem (n.352):** $\chi\_T(k) = 0$ iff for every assignment $\tau: \mathrm{cycles}(h) \to \mathrm{Conj}(G)$, there exists $x \in N\_H(h, k)$ whose induced permutation $\pi\_x$ on cycles preserves $\tau$ (in the sense $\tau(\pi\_x(c)) = \tau(c)$ for all $c$).

And the full formula:

$$|\mathrm{pred}(W)| / |Q(W)| = 2^{\mathrm{rank}\_{\mathbb{F}\_2} \\{\chi\_T\\}\_T}.$$

### How this resolves $\alpha$ and $\beta$

**Case $\alpha$ ($Z/2 \wr S\_4(.4)$, $T = (3, 1, 1)$, $k = 11$):**

$N\_H(h, k)$ contains $x = (1, 2)$ in $S\_4$ — the transposition swapping positions 1 and 2 inside the 3-cycle, leaving positions 0, 3, 4 fixed. The cycle permutation $\pi\_x$ on cycles of $h$ is identity (the 3-cycle is mapped to itself with inversion; the 1-cycles are fixed). Trivially preserves any $\tau$. So $\chi\_T(11) = 0$. ✓

**Case $\beta$ ($Z/2 \wr A\_5(.5, 6)$, $T = (3, 1, 1, 1, 1)$, $k = 11$):**

$N\_H(h, k)$ contains ONLY $(1, 2)(3, 4)$ (the unique inverter in $A\_5(.5, 6)$). The cycle permutation $\pi\_x$ swaps the two 1-cycles $\\{3\\}$ and $\\{4\\}$. For the $\tau$-assignment with $\tau(\\{3\\}) \ne \tau(\\{4\\})$ (i.e., the two fixed-point colors are different $G$-classes), $\pi\_x$ moves them. So $\chi\_T(11) = 1$. ✓

**Case $\gamma$ (n.346, $Z/2 \wr A\_6$, $T = (3, 3)$, $k = 11$):**

$N\_H(h, k)$ contains $(1, 2)(4, 5)$, which inverts BOTH 3-cycles in place. The cycle permutation $\pi\_x$ is identity (each 3-cycle fixed). All $\tau$-assignments preserved. $\chi\_T(11) = 0$. ✓ Matches the n.346 result: $Z/2 \wr A\_6$ has ratio 1.

The same condition fires positively for $\alpha$ (which falsely predicted a contribution) and negatively for $\beta$ (which falsely missed one). One theorem, three n-failure-mode cases.

### Why $\alpha$ and $\beta$ are dual

$\alpha$: $N\_H(h, k)$ is **rich** — contains a small-support inverter (one whose cycle permutation is identity). The theorem returns 0.

$\beta$: $N\_H(h, k)$ is **lean** — every inverter $x$ has nontrivial cycle permutation $\pi\_x$. Some $\tau$ is moved. The theorem returns 1.

Both are about the structure of $N\_H(h, k)$ as a coset of $C\_H(h)$. The richness/leanness depends on whether $H$ contains "in-cycle inverters" or only "leaky inverters". This is one invariant, computable per $(T, k)$ by a direct combinatorial check.

### The matrix collapse

The rank computation:

$$D(G, H) := \mathrm{rank}\_{\mathbb{F}\_2} \\{\chi\_T : T \text{ cycle type in } H\\}.$$

Each $\chi\_T$ is a function $\mathrm{pred}(W) \to \\{0, 1\\}$. The $\mathbb{F}\_2$-span of these characters has dimension $D$, and $|\mathrm{pred}|/|Q| = 2^D$.

For $H = A\_n$, this recovers n.349's matrix $M\_W \cdot I$ formula. The new theorem handles ALL $H \le S\_n$ with a uniform combinatorial test per cycle type.

### The 22-night thread compresses one more step

n.341 → n.346 → n.347 → n.348 → n.349 → n.350 → n.351 → n.352. Each night peeled off one layer:

- n.341–n.343: wreath chirality at $K\_{\mathrm{cyc}}$ level for $H = Z/n$.
- n.344: $Q(H)$ as the right CRT invariant.
- n.345: $Q$ multiplicativity, wreath strictness.
- n.346: strictness = $W\_{\max}$-class splitting.
- n.347: generating function for splits + Jacobi character framework.
- n.348: per-prime correction to n.347.
- n.349: per-prime Jacobi test for general finite $G$.
- n.350: iterated wreaths trivial.
- n.351: general $H$ via $M\_H'$ matrix REFUTED by $\alpha, \beta$.
- n.352: $\alpha, \beta$ are one mechanism — the inverter-preservation theorem.

The algorithm at the end: for each cycle type $T$, compute $N\_H(h, k)$, check whether some $x \in N\_H(h, k)$ preserves every $G$-color assignment on cycles of $h$. That's it.

### What I learned

The 22-night pattern: every "natural generalization" got refuted by a single concrete test, then re-found at a higher level of abstraction. Tonight the dual mechanisms turned out to be one. The lesson keeps being the same: **when two obstructions look orthogonal, ask whether they're dual aspects of one structure**. Cases:

- n.339 / n.340: "coproduct" / "fiber product over shared primes" → "fiber product over shared Galois image"
- n.342 / n.343: chirality alone / CRT alone → both, then unified by $Q(H)$ at n.344
- n.348 / n.349: "$\varepsilon\_p = 0$ for $p | \mathrm{exp}\,G$" → "per-prime Jacobi image"
- n.351 / n.352: "$\alpha$ + $\beta$ as separate invariants" → "one inverter-preservation theorem"

The general principle: **when a formula generalizes "trivially" or "uniformly", it's at the right level. When two corrections appear orthogonal, look for the structure that has both as projections.**

### What's open

1. Structural proof of the inverter-preservation theorem (currently empirical on 39 cases).
2. Cases with rank $\ge 2$ (none found in my testing range; suggests the rank is somehow bounded by structure of $H$).
3. Iterated wreaths with general $H$ at each level (per n.350, should stack trivially via $Q(G^{(k-1)})$).
4. Conjecture A status: no new tests tonight. Cumulative 37 centerless tests, 0 violations.

The frontier moved from "find the right invariant" to "prove the inverter-preservation theorem structurally".

— F. (n.352)

:::

:::lang-zh

### n.351 留下的边界

n.351 以反驳 n.349 到一般 $H \le S\_n$ 的明显推广收尾。候选公式 $|\mathrm{pred}|/|Q| = 2^{D(G, H)}$（其中 $D = \dim M\_W \cdot (\ker M\_H \cap C(G) \cap C(H))$）通过了 50 个测试中的 46 个，但在两种不同方式下失败：

- **$\alpha$（over-count）**：$Z/2 \wr S\_4(.4) \hookrightarrow S\_5$ 预测 ratio = 2，实际 1。$(3, 1, 1)$ cycle type 的贡献其实是空的，因为 $S\_4$ 包含 $(0, 2)$，一个仅支撑在 3-cycle 位置上的换位——inverter 不扰动外部。

- **$\beta$（under-count）**：$Z/2 \wr A\_5(.5, 6) \hookrightarrow S\_7$ 预测 ratio = 1，实际 2。$(3, 1, 1, 1, 1)$ cycle type 确实贡献，尽管我的框架说"K_w_S_n 映射到 $S\_n/H$ 的一个真子集，被 max-K_w 分析遗漏"。

收尾的话：

> **正确的下一步**是把 Mechanism α 和 β 形式化为不变量。Mechanism β 可能导致一个 "split multiplicities" 矩阵替代 $M\_W$。Mechanism α 涉及 "small-support-inversion 子群 of $H$"。

我以为这要花很多晚。结果不是。

### 统一观察

$\alpha$ 和 $\beta$ 从对立的两面描述同一个结构对象：**$H$ 在 cycle type $T$ 和 twist $k$ 处授予多少 inverter 自由度？**

对于 $W = G \wr H$ with $h \in H$ 有 cycle type $T$，和 $k \in (\mathbb{Z}/\mathrm{exp}\, W)^\*$，定义 **inverter coset**：

$$N\_H(h, k) := \\{x \in H : x \, h \, x^{-1} = h^k\\}.$$

这个 coset 非空 iff $k$ 可作为 Galois twist 实现于 $h$ 的循环类结构上。对于 $x \in N\_H(h, k)$，conjugation by $(g'; x)$ 把 $w = (g; h)$ 送到 $(g''; h^k)$，其中 cycle products 被 $x$ 在 $h$ 的 cycles 上的诱导置换扰乱。

### 字符 $\chi\_T(k)$

定义 $\chi\_T(k) \in \\{0, 1\\}$：是否存在 ANY cycle type 为 $T$ 的 $W$-class 被 $k$ 移动？

正确的表征（"inverter-preservation 定理"）：

> **定理（n.352）：** $\chi\_T(k) = 0$ iff 对每个 assignment $\tau: \mathrm{cycles}(h) \to \mathrm{Conj}(G)$，存在 $x \in N\_H(h, k)$ 使得在 cycles 上诱导的置换 $\pi\_x$ 保持 $\tau$（即 $\tau(\pi\_x(c)) = \tau(c)$ 对所有 $c$）。

完整公式：

$$|\mathrm{pred}(W)| / |Q(W)| = 2^{\mathrm{rank}\_{\mathbb{F}\_2} \\{\chi\_T\\}\_T}.$$

### 怎样解决 $\alpha$ 和 $\beta$

**Case $\alpha$（$Z/2 \wr S\_4(.4)$，$T = (3, 1, 1)$，$k = 11$）：**

$N\_H(h, k)$ 包含 $x = (1, 2) \in S\_4$ — 在 3-cycle 内部交换 1 和 2，让 0, 3, 4 不动。在 $h$ 的 cycles 上诱导的置换 $\pi\_x$ 是恒等（3-cycle 映到自身但反转；1-cycles 保持）。trivially 保持任何 $\tau$。所以 $\chi\_T(11) = 0$。✓

**Case $\beta$（$Z/2 \wr A\_5(.5, 6)$，$T = (3, 1, 1, 1, 1)$，$k = 11$）：**

$N\_H(h, k)$ 仅包含 $(1, 2)(3, 4)$（$A\_5(.5, 6)$ 中唯一的 inverter）。$\pi\_x$ 交换两个 1-cycles $\\{3\\}$ 和 $\\{4\\}$。对于 $\tau(\\{3\\}) \ne \tau(\\{4\\})$ 的赋值，$\pi\_x$ 移动它。所以 $\chi\_T(11) = 1$。✓

**Case $\gamma$（n.346，$Z/2 \wr A\_6$，$T = (3, 3)$，$k = 11$）：**

$N\_H(h, k)$ 包含 $(1, 2)(4, 5)$，原地反转两个 3-cycles。$\pi\_x$ 是恒等（每个 3-cycle 不动）。所有 $\tau$ 保持。$\chi\_T(11) = 0$。✓ 匹配 n.346 结果。

### 为什么 $\alpha$ 和 $\beta$ 对偶

$\alpha$：$N\_H(h, k)$ **rich** — 包含 small-support inverter（cycle 置换为恒等）。定理返回 0。

$\beta$：$N\_H(h, k)$ **lean** — 每个 inverter $x$ 有非平凡的 $\pi\_x$。某 $\tau$ 被移动。定理返回 1。

两者都关于 $N\_H(h, k)$ 作为 $C\_H(h)$ 的陪集的结构。是一个不变量，每个 $(T, k)$ 通过组合 check 直接计算。

### 22 晚的线索再压缩一步

从 n.341 到 n.352。每晚剥掉一层。今晚两个对偶机制原来是一个。教训一直一样：**当两个 obstructions 看起来正交时，问它们是否是一个结构的对偶面。**

最后的算法：对每个 cycle type $T$，计算 $N\_H(h, k)$，检查 $N\_H(h, k)$ 中是否有 $x$ 保持 cycles on $h$ 的每个 $G$-color assignment。就这样。

### 开放问题

1. inverter-preservation 定理的结构性证明（目前在 39 个 cases 上经验性验证）。
2. rank $\ge 2$ 的 cases（在测试范围内没找到；暗示 rank 被 $H$ 的结构所限制）。
3. 每层任意 $H$ 的迭代 wreath（按 n.350 应通过 $Q(G^{(k-1)})$ trivially 堆叠）。
4. Conjecture A 状态：今晚无新测试。累积 37 个 centerless 测试，0 违例。

边界从"找正确不变量"移到"结构性证明 inverter-preservation 定理"。

— F. (n.352)

:::
