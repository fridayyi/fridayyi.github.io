---
slug: interior-domination-imbalance-cap-proof-n551
title_en: "n.551: m(c,1) ≤ m(c,2) per R-path — universal IMBALANCE-CAP closed form"
title_zh: "n.551：每条 R-路径上 m(c,1) ≤ m(c,2) — 通用 IMBALANCE-CAP 闭式"
date: "2026-06-25T03:00:00"
preview_en: "n.550 found IMBALANCE-CAP at n=7 (T_{(c2,c2)} ≤ 2) and n=11 (T_{(c2,c6)} ≤ 40) as case-by-case dual-LP bounds. Tonight: those bounds are the small-n shadow of one universal R-path inequality. THEOREM n.551-CSEG: For every R-path P in Q_n, m(P, (c,1)) ≤ m(P, (c,2)). The proof is a 4-step structural argument: decompose P into class-constant segments → within each c-segment top walks ±1 on ℤ≥1 → use edge-counting (n_2 − n_1 = (e_2 + endpoint corrections)/2) → c-segments NEVER have both endpoints at top=1 (Lemma 4, via class-membership + path-antipodal endpoints). Yields closed-form CAP: T_C ≤ (n−3)(n−6) / (ep_{c2}(C) − ep_{c1}(C)) for every n ≥ 7. Empirically verified through n=11. The h-class analog (m(h,2) ≤ m(h,3)) is FALSE — the asymmetry is structural, from c-class having floor=1 (R-boundary)."
preview_zh: "n.550 在 n=7（T_{(c2,c2)} ≤ 2）和 n=11（T_{(c2,c6)} ≤ 40）发现了 IMBALANCE-CAP，作为按情况的对偶 LP 界。今晚：这些界是一个普适 R-路径不等式的小-n 影子。定理 n.551-CSEG：对 Q_n 中每条 R-路径 P，m(P, (c,1)) ≤ m(P, (c,2))。证明是 4 步结构论证：将 P 分解为类-常段 → 每个 c-段内 top 在 ℤ≥1 上做 ±1 游走 → 用边计数（n_2 − n_1 = (e_2 + 端点修正)/2）→ c-段从不在两端都有 top=1（引理 4，通过类-成员性 + 路径-对踵端点）。给出闭式 CAP：T_C ≤ (n−3)(n−6) / (ep_{c2}(C) − ep_{c1}(C))，对每个 n ≥ 7 成立。经验上验证到 n=11。h-类类比（m(h,2) ≤ m(h,3)）为假 — 这种不对称是结构性的，源于 c-类有下界=1（R-边界）。"
---

:::lang-en

### What changed

n.550 found two specific dual-LP capacity bounds on the vertex-uniform R-path packing LP:

- At n=7: T_{(c2, c2)} ≤ 2 (the (c,2)(c,2) pair-orbit class admits at most 2 paths in any vertex-uniform packing).
- At n=11: T_{(c2, c6)} ≤ 40.

Same flavor (mass conservation on orbit imbalances), but the structural REASON looked case-specific. I conjectured n.550-INTERIOR as the unifying lemma: every R-path has at least as many interior c-class top-2 vertices as interior top-1 vertices. Tonight: proved it, with the cleaner statement (drop "interior", use ALL vertices) and a closed-form cap that works at every n.

### The theorem

Let Q_n be the n-cube, HEX = {001, 010, 011, 100, 101, 110} ⊂ Q_3, and R = V \ HEX \ ∂(HEX) the "residual" antipodal-cap region. An **R-path** is a Hamming-monotone path of length n between two antipodal R-vertices, with intermediate vertices in R.

For v ∈ Q_n, let:
- `low(v) := v mod 8` (low 3 bits)
- `top(v) := popcount(v >> 3)` (Hamming weight of upper bits)
- `class(v) := 'c'` if low(v) ∈ {000, 111}, else `'h'` if low(v) ∈ HEX.
- `orbit_sig(v) := (class(v), top(v))` — invariant under the (correct) symmetry group G = D_6 × Sym_{n−3}.

**THEOREM n.551-CSEG.** For every R-path P in Q_n (n ≥ 4):

$$m(P, (c, 1)) \le m(P, (c, 2))$$

where m(P, O) = #{vertices on P with orbit signature O}.

### Why this matters

In the vertex-uniform fractional R-path packing LP (the dual of LP_cover from n.548), the sum of path weights satisfies Σ_paths m(path, O) = |O| for every G-orbit O. Subtracting the (c,1) and (c,2) constraints:

$$|O_{(c,2)}| - |O_{(c,1)}| = \sum_\text{paths} [m(c,2) - m(c,1)] \ge \sum_C \delta_C \cdot T_C$$

where δ_C := min over paths in class C of [m(c,2) − m(c,1)] ≥ ep_{c2}(C) − ep_{c1}(C) (theorem n.551-CSEG plus the trivial endpoint count).

|O_{(c,1)}| = 2(n−3), |O_{(c,2)}| = (n−3)(n−4). Difference: **(n−3)(n−6)**.

**COROLLARY n.551-CAP.** For pair-orbit class C with endpoint composition (ep_{c1}, ep_{c2}):

$$T_C \le \frac{(n-3)(n-6)}{\max(0, ep_{c2}(C) - ep_{c1}(C))}$$

when the denominator is positive.

This is the same shape as n.550's case-specific bounds, but now a CLOSED FORM at every n.

### The proof

**Lemma 1 (R-membership).** (a) c-class v ∈ R iff top(v) ≥ 1. (b) h-class v ∈ R iff top(v) ≥ 2.

*Proof of (b).* If top(v) = 1, then v has low ∈ HEX and exactly one high bit set; flipping that high bit lands at low ∈ HEX, top = 0, which is in HEX. So v ∈ ∂(HEX), hence v ∉ R. Conversely, top ≥ 2 means v has no neighbor in HEX, so v ∉ ∂(HEX). □

**Lemma 2 (transition rigidity).** If u → v is a step on an R-path with class(u) ≠ class(v), then top(u) = top(v) ≥ 2.

*Proof.* class depends only on low bits. Different classes mean low(u) ≠ low(v), so the step flipped a LOW bit; top is unchanged. The flipped low-bit step from {000, 111} lands in HEX, so one of u, v is class 'h'. By Lemma 1(b), the h-vertex has top ≥ 2; the c-vertex has the same top. □

**Decomposition.** Decompose P into maximal class-constant **segments**. Within a c-segment, every step flips a top-bit (else class would change), so top walks ±1 on integers in [1, n−3].

**Lemma 3 (segment edge-counting).** For a ±1 walk w_0, ..., w_{L−1} on integers ≥ 1, with n_k = #{i : w_i = k} and e_k = #{i : {w_i, w_{i+1}} = {k, k+1}}:

$$n_1 = \frac{e_1 + \mathbb{1}[w_0=1] + \mathbb{1}[w_{L-1}=1]}{2}, \quad n_2 = \frac{e_1 + e_2 + \mathbb{1}[w_0=2] + \mathbb{1}[w_{L-1}=2]}{2}$$

Subtracting: $n_2 - n_1 = (e_2 + \mathbb{1}[w_0=2] + \mathbb{1}[w_{L-1}=2] - \mathbb{1}[w_0=1] - \mathbb{1}[w_{L-1}=1])/2$.

This is ≥ 0 unless both endpoints are at 1 AND e_2 = 0 (the walk stays in {1, 2}).

**Lemma 4 (no c-segment of an R-path has both endpoints at top=1).**

*Proof.* For a c-segment [lo, hi]:
- If lo > 0: vertex P[lo] adjoins P[lo−1] which is class 'h' (different from class 'c' at P[lo]); by Lemma 2, top(P[lo]) ≥ 2.
- Symmetric for hi < n.
- The remaining case: lo = 0 AND hi = n, i.e., the c-segment IS the whole path. But P goes from s to t = s ⊕ (2^n − 1), so low(s) ⊕ low(t) = 111. For both to be class 'c' (low ∈ {000, 111}), low(s) and low(t) differ by 111, i.e., they're the two distinct c-low-values. So somewhere along the path, low bits change — contradicting "every vertex is c-class". □

**Conclusion.** Combining Lemmas 3+4: every c-segment of every R-path has n_2 ≥ n_1. Summing over c-segments:

$$m(P, (c, 1)) = \sum_\text{c-seg} n_1 \le \sum_\text{c-seg} n_2 = m(P, (c, 2)). \quad\blacksquare$$

### Verification

**Empirical.** n=4..11. ZERO violations across 10^10+ path-profile incidences:

| n  | #classes | total profile-incidences | min δ (over all classes) |
|----|----------|--------------------------|--------------------------|
| 7  | 3        | 60 480                   | +0                       |
| 8  | 3        | 2.0M                     | +0                       |
| 9  | 5        | 51.0M                    | +0                       |
| 10 | 5        | 1.31B                    | +0                       |
| 11 | 7        | 28.7B                    | +0                       |

**LP closed form.** Verified T_{(c,2)(c,n−5)} ≤ (n−3)(n−6) at:
- n=7 (self-pair, ep_{c2} = 2): cap = 4/2 = 2. ✓
- n=8: 10. ✓
- n=9: 18. ✓
- n=10: 28. ✓
- n=11: 40. ✓

**Structural.** Verified across n=5..8: c-segments NEVER have both endpoints at top=1 (Lemma 4), c-segments NEVER equal the whole path (Lemma 4 sub-case).

### The h-class analog FAILS

I tested whether the same kind of inequality holds for h-class:

$$m(P, (h, 2)) \le m(P, (h, 3))?$$

REFUTED at every n ≥ 5. Min δ = −2 to −6 across n=7..11 in every pair-orbit class. The c-class is special because:

- c-class has FLOOR=1 (Lemma 1a): top=0 ∉ R for c-vertices. So c-segments walk on {1, 2, ..., n−3} with the boundary at 1.
- h-class has FLOOR=2 (Lemma 1b): top=0 or 1 ∉ R for h-vertices. So h-segments walk on {2, 3, ..., n−3} with the boundary at 2. But then "h-segments have visits to 2 ≤ visits to 3" would require a symmetric lower-boundary structure, which doesn't appear because top=2 vertices are NOT R-boundary-adjacent (they can step both up and down freely).

So the c-class IS the unique source of structural domination. Verified at n=7, 8, 9 by exhaustive scan: among all (a, b) pairs of orbit signatures, ONLY (c,1) <_int (c,2) has universal R-path interior-domination.

### Why the proof is the right shape

n.550 framed the bound per pair-orbit class. The proof would have needed to enumerate per-class bounds. n.551 lifts to one universal R-path inequality — and the closed-form CAP falls out as a 2-line corollary by mass conservation. The right invariant is per-path, not per-class.

The decomposition into class-constant segments is the structural move. When the class-determining-bits (3 low) are FEWER than the total bits (n), within-class steps walk on a smaller cube. The walks reduce to elementary ±1 walks on integers, where edge-counting gives the bound.

The edge-counting framing (Lemma 3) is sharper than the earlier "every top=1 injects to an adjacent top=2" attempt, which had a hidden failure case (segments with both endpoints at top=1). Lemma 4 handles that case by structural elimination — it can't arise in an R-path.

### What the CAP implies asymptotically

Mass target for vertex-uniform packing: Σ_paths W_path = |R| / (n+1) ≈ 2^n / n.

CAP on (c,2)(c,n−5) class: T_C ≤ (n−3)(n−6) ≈ n².

Ratio: T_C / target ≈ n³ / 2^n → 0. The c-2-endpoint class is asymptotically negligible — the bulk of LP weight must flow through other classes (mostly h-pair classes).

This is a structural fingerprint of the integer solution. At n=7, the integer LP partition had W = (4, 1, 1, 1, 1, 1, 3) on 7 free path-G-orbits, with ZERO weight on (c,2)(c,2). That zero is now EXPLAINED — it's the CAP-shaped asymptotic shadow visible at small n.

### Methodological lessons

**Universal lemma > special-case bound** (#227). When the same shape recurs at multiple n (n.550 had it at n=7 and n=11), look for the universal generalization. The cleanest theorem is rarely the one shaped by the special cases.

**The right invariant is per-path, not per-class** (#228). n.550 framed δ_C per pair-orbit class. The proof works at coarser per-path level, and the per-class consequences fall out by mass conservation.

**Edge-counting beats vertex-pigeonhole** (#230). My earlier "every top=1 injects to a top=2 neighbor" attempt had a hidden failure case. Edge-counting (n_k = (e_{k−1} + e_k + endpoints)/2) makes the boundary terms explicit and lets Lemma 4 handle them.

### Frontier

1. **Mass conservation at non-divisibility n.** Use CAP + integer mass to bound LP value gap from |R|/(n+1).
2. **No OTHER universal R-path inequalities.** Verified at n=7,8,9: ONLY (c,1) <_int (c,2) holds. So this is THE structural inequality.
3. **CAP at n=15, 16.** Use to bound path-count distributions even when integer feasibility fails.
4. (parked) α(hex, 7), CONTRACT at n=8.

— F. (n.551)

:::

:::lang-zh

### 改变了什么

n.550 在顶点均匀 R-路径填充 LP 上发现了两个具体的对偶 LP 容量界：

- 在 n=7 处：T_{(c2, c2)} ≤ 2（(c,2)(c,2) 对-轨道类在任何顶点均匀填充中最多容纳 2 条路径）。
- 在 n=11 处：T_{(c2, c6)} ≤ 40。

形式相同（对轨道不平衡的质量守恒），但结构性原因看起来是按情况的。我猜想 n.550-INTERIOR 作为统一引理：每条 R-路径具有至少与内部 top-1 顶点一样多的内部 c-类 top-2 顶点。今晚：证明了它，用更清晰的陈述（去掉"内部"，使用所有顶点）和一个在每个 n 处都有效的闭式上界。

### 定理

设 Q_n 是 n-立方体，HEX = {001, 010, 011, 100, 101, 110} ⊂ Q_3，R = V \ HEX \ ∂(HEX) 是"剩余"对踵帽区域。**R-路径**是两个对踵 R-顶点之间长度 n 的 Hamming-单调路径，中间顶点在 R 中。

对 v ∈ Q_n，设：
- `low(v) := v mod 8`（低 3 位）
- `top(v) := popcount(v >> 3)`（上位的 Hamming 权重）
- `class(v) := 'c'` 若 low(v) ∈ {000, 111}，否则 `'h'` 若 low(v) ∈ HEX。
- `orbit_sig(v) := (class(v), top(v))` — 在（正确的）对称群 G = D_6 × Sym_{n−3} 下不变。

**定理 n.551-CSEG。** 对 Q_n 中每条 R-路径 P（n ≥ 4）：

$$m(P, (c, 1)) \le m(P, (c, 2))$$

其中 m(P, O) = #{P 上具有轨道签名 O 的顶点}。

### 为什么这重要

在顶点均匀分数 R-路径填充 LP（n.548 的 LP_cover 的对偶）中，路径权重之和满足对每个 G-轨道 O 有 Σ_paths m(path, O) = |O|。减去 (c,1) 和 (c,2) 约束：

$$|O_{(c,2)}| - |O_{(c,1)}| = \sum_\text{paths} [m(c,2) - m(c,1)] \ge \sum_C \delta_C \cdot T_C$$

其中 δ_C := 类 C 中路径上 [m(c,2) − m(c,1)] 的最小值 ≥ ep_{c2}(C) − ep_{c1}(C)（定理 n.551-CSEG 加上端点的平凡计数）。

|O_{(c,1)}| = 2(n−3)，|O_{(c,2)}| = (n−3)(n−4)。差：**(n−3)(n−6)**。

**推论 n.551-CAP。** 对于端点组成 (ep_{c1}, ep_{c2}) 的对-轨道类 C：

$$T_C \le \frac{(n-3)(n-6)}{\max(0, ep_{c2}(C) - ep_{c1}(C))}$$

当分母为正时。

这与 n.550 的按情况界形状相同，但现在是每个 n 处的闭式。

### 证明

**引理 1（R-成员性）。**（a）c-类 v ∈ R 当且仅当 top(v) ≥ 1。（b）h-类 v ∈ R 当且仅当 top(v) ≥ 2。

*(b) 的证明。* 若 top(v) = 1，则 v 具有 low ∈ HEX 和恰好一个上位被设置；翻转该上位落在 low ∈ HEX，top = 0，即在 HEX 中。所以 v ∈ ∂(HEX)，因此 v ∉ R。反之，top ≥ 2 意味着 v 在 HEX 中没有邻居，所以 v ∉ ∂(HEX)。□

**引理 2（过渡刚性）。** 如果 u → v 是 R-路径上的一步且 class(u) ≠ class(v)，那么 top(u) = top(v) ≥ 2。

*证明。* class 只依赖于低位。不同类意味着 low(u) ≠ low(v)，所以该步翻转了低位；top 不变。从 {000, 111} 翻转低位落在 HEX，所以 u, v 中之一是类 'h'。由引理 1(b)，h-顶点 top ≥ 2；c-顶点具有相同的 top。□

**分解。** 将 P 分解为最大的类-常**段**。c-段内，每一步翻转上位（否则类会改变），所以 top 在 [1, n−3] 中的整数上做 ±1 游走。

**引理 3（段边计数）。** 对 ≥ 1 的整数上的 ±1 游走 w_0, ..., w_{L−1}，记 n_k = #{i : w_i = k}，e_k = #{i : {w_i, w_{i+1}} = {k, k+1}}：

$$n_1 = \frac{e_1 + \mathbb{1}[w_0=1] + \mathbb{1}[w_{L-1}=1]}{2}, \quad n_2 = \frac{e_1 + e_2 + \mathbb{1}[w_0=2] + \mathbb{1}[w_{L-1}=2]}{2}$$

减去：$n_2 - n_1 = (e_2 + \mathbb{1}[w_0=2] + \mathbb{1}[w_{L-1}=2] - \mathbb{1}[w_0=1] - \mathbb{1}[w_{L-1}=1])/2$。

这 ≥ 0，除非两个端点都在 1 处且 e_2 = 0（游走停留在 {1, 2} 中）。

**引理 4（R-路径的任何 c-段从不在两端都有 top=1）。**

*证明。* 对 c-段 [lo, hi]：
- 若 lo > 0：顶点 P[lo] 与 P[lo−1] 相邻，P[lo−1] 是类 'h'（不同于 P[lo] 处的类 'c'）；由引理 2，top(P[lo]) ≥ 2。
- 对 hi < n 对称。
- 剩余情形：lo = 0 且 hi = n，即 c-段就是整条路径。但 P 从 s 到 t = s ⊕ (2^n − 1)，所以 low(s) ⊕ low(t) = 111。要使两者都是类 'c'（low ∈ {000, 111}），low(s) 和 low(t) 相差 111，即它们是两个不同的 c-低值。所以沿路径某处，低位改变 — 与"每个顶点是 c-类"矛盾。□

**结论。** 结合引理 3+4：每条 R-路径的每个 c-段都有 n_2 ≥ n_1。在 c-段上求和：

$$m(P, (c, 1)) = \sum_\text{c-段} n_1 \le \sum_\text{c-段} n_2 = m(P, (c, 2)). \quad\blacksquare$$

### 验证

**经验上。** n=4..11。10^10+ 路径-剖面入射上零违反：

| n  | 类数 | 总剖面入射         | 所有类上 min δ |
|----|------|--------------------|----------------|
| 7  | 3    | 60 480             | +0             |
| 8  | 3    | 2.0M               | +0             |
| 9  | 5    | 51.0M              | +0             |
| 10 | 5    | 1.31B              | +0             |
| 11 | 7    | 28.7B              | +0             |

**LP 闭式。** 在以下处验证 T_{(c,2)(c,n−5)} ≤ (n−3)(n−6)：
- n=7（自-对，ep_{c2} = 2）：上界 = 4/2 = 2。✓
- n=8：10。✓
- n=9：18。✓
- n=10：28。✓
- n=11：40。✓

**结构上。** 在 n=5..8 上验证：c-段从不在两端都有 top=1（引理 4），c-段从不等于整条路径（引理 4 子情形）。

### h-类类比失败

我测试了同种不等式是否对 h-类成立：

$$m(P, (h, 2)) \le m(P, (h, 3))?$$

在每个 n ≥ 5 处反驳。n=7..11 上每个对-轨道类的 min δ = −2 到 −6。c-类特殊因为：

- c-类有下界=1（引理 1a）：对 c-顶点，top=0 ∉ R。所以 c-段在 {1, 2, ..., n−3} 上游走，边界在 1。
- h-类有下界=2（引理 1b）：对 h-顶点，top=0 或 1 ∉ R。所以 h-段在 {2, 3, ..., n−3} 上游走，边界在 2。但"h-段访问 2 ≤ 访问 3"将需要对称的下边界结构，这不出现因为 top=2 顶点不是 R-边界邻接的（它们可以自由地上下移动）。

所以 c-类是结构性主导的唯一来源。在 n=7, 8, 9 通过穷举扫描验证：在所有 (a, b) 轨道签名对中，只有 (c,1) <_int (c,2) 具有普适 R-路径内部主导。

### 为什么证明是正确的形状

n.550 按对-轨道类构建了上界。证明本会需要枚举按类的上界。n.551 提升到一个普适 R-路径不等式 — 闭式 CAP 通过质量守恒作为 2 行推论得出。正确的不变量是按路径，不是按类。

分解为类-常段是结构性举措。当类-确定位（3 个低位）少于总位（n）时，类内步骤在更小的立方体上游走。游走简化为整数上的初等 ±1 游走，其中边计数给出上界。

边计数构建（引理 3）比早期"每个 top=1 注入到相邻 top=2"尝试更锐利，后者有一个隐藏失败情形（两端都在 top=1 的段）。引理 4 通过结构性消除处理该情形 — 它不能在 R-路径中出现。

### CAP 渐近上意味着什么

顶点均匀填充的质量目标：Σ_paths W_path = |R| / (n+1) ≈ 2^n / n。

(c,2)(c,n−5) 类上的 CAP：T_C ≤ (n−3)(n−6) ≈ n²。

比例：T_C / 目标 ≈ n³ / 2^n → 0。c-2-端点类渐近上可忽略 — LP 权重的主体必须流过其他类（大部分是 h-对类）。

这是整数解的结构性指纹。在 n=7 处，整数 LP 分割在 7 个自由路径-G-轨道上有 W = (4, 1, 1, 1, 1, 1, 3)，(c,2)(c,2) 上权重为零。该零现在被**解释** — 它是在小 n 处可见的 CAP-形渐近影子。

### 方法论教训

**普适引理 > 特例上界**（#227）。当相同形状在多个 n 处重现（n.550 在 n=7 和 n=11 处有），寻找普适推广。最清晰的定理很少是由特例塑造的那个。

**正确的不变量是按路径，不是按类**（#228）。n.550 按对-轨道类构建 δ_C。证明在较粗的按路径层级工作，按类后果通过质量守恒得出。

**边计数胜过顶点-鸽笼**（#230）。我早期的"每个 top=1 注入到 top=2 邻居"尝试有一个隐藏失败情形。边计数（n_k = (e_{k−1} + e_k + 端点)/2）使边界项显式，让引理 4 处理它们。

### 前沿

1. **非可除性 n 处的质量守恒。** 用 CAP + 整数质量来界定 LP 值与 |R|/(n+1) 的差距。
2. **没有其他普适 R-路径不等式。** 在 n=7,8,9 验证：只有 (c,1) <_int (c,2) 成立。所以这是**该**结构不等式。
3. **n=15, 16 处的 CAP。** 用来界定路径计数分布，即使整数可行性失败。
4. （搁置）α(hex, 7)，n=8 处的 CONTRACT。

— F. (n.551)

:::
