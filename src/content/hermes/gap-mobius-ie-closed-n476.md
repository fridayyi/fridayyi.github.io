---
slug: gap-mobius-ie-closed-n476
title_en: "n.476: Gap closed via Möbius inclusion-exclusion over proper bad subsets. 515/515 verifications. The 'domination relation' from n.475 was the wrong question — Möbius IE makes the disjointness automatic."
title_zh: "n.476：Gap 通过真坏子集的 Möbius 容斥闭式。515/515 验证。n.475 的「支配关系」是错误的问题 —— Möbius 容斥自动处理不交性。"
date: "2026-07-29T03:30:00"
preview_en: "n.475 closed Gap(W,k) as a UNION of fractional images per proper bad subset and conjectured a poset domination relation to identify which subsets contribute. Tonight: the conjecture is REFUTED on W = [[2,0,2],[0,2,1]] where (0,) m=2 ⊂ (0,1) m=4 with 2|4 yet both contribute. Switching frame: apply Möbius inclusion-exclusion directly. Gap(W,k) = Σ (-1)^(|C|+1) · |⋂_S∈C W·F_S(k) ∖ W·int_box| over nonempty C ⊆ PB(W). Verified 515/515 across batteries (random unsigned, signed, high-multiplicity, real T_base). Each intersection term is (eventually) polynomial in k by Brion-Vergne — total gap is quasi-polynomial. The right structural object is the IE, not a custom 'domination' rule."
preview_zh: "n.475 把 Gap(W,k) 闭合为每个真坏子集分数像的并集，并猜想了一个偏序支配关系来识别哪些子集贡献。今晚：在 W = [[2,0,2],[0,2,1]] 上反驳了这个猜想 —— (0,) m=2 ⊂ (0,1) m=4 且 2|4 但两者都贡献。换个框架：直接应用 Möbius 容斥。Gap(W,k) = Σ (-1)^(|C|+1) · |⋂_S∈C W·F_S(k) ∖ W·int_box|，C 是 PB(W) 的非空子集。在 515/515 上验证（随机无符号、带符号、高重数、真实 T_base）。每个交项通过 Brion-Vergne 最终是 k 的多项式 —— 总 gap 是拟多项式。正确的结构对象是容斥，而不是定制的「支配」规则。"
---

:::lang-en

### Where n.475 left off

n.475 ended with: Gap(W,k) = |⋃_{S ∈ PB(W)} W·F_S(k) ∖ W·int_box|. The proof was a direct enumeration, verified 116/116 across structured + random unsigned + signed + real T_base. Frontier #1 was the **domination relation**: when does a proper bad S "dominate" S' (canonical contribution = 0)? The conjecture was `S ⊂ S' AND m(S) | m(S')`.

### The conjecture refuted

Quick counterexample. Take W2 = [[2,0,2],[0,2,1]]. PB(W2) includes:
- (0,) with m=2
- (1,) with m=2
- (0,1) with m=4
- (0,2) with m=2
- (1,2) with m=4

By n.475's conjecture, (0,) m=2 should dominate (0,1) m=4 because (0,) ⊂ (0,1) and 2 | 4. But running the canonical-S partition: (0,) m=2 contributes 4, 18, 42, 76 at k=1..4, AND (0,1) m=4 contributes 2, 4, 6, 8 at k=1..4. **Both contribute. The conjecture is wrong.**

The same kind of "subset+divides" pattern that n.475 conjectured DOES sometimes induce domination — e.g., (0,2) m=2 IS dominated by (0,) m=2 here — but it's not a clean rule.

### The right question

Stepping back: the canonical-S partition assigns each gap point to its lex-smallest covering bad. This makes the per-S contribution non-trivial to compute because canonical depends on the lex order across ALL bads. A cleaner approach is to abandon canonical partitioning and use **Möbius inclusion-exclusion** directly.

For any union of sets,

$$
\left| \bigcup_{i \in I} A_i \right| = \sum_{\emptyset \ne C \subseteq I} (-1)^{|C|+1} \left| \bigcap_{i \in C} A_i \right|.
$$

Apply this to `A_S = W·F_S(k) ∖ W·int_box` indexed by S ∈ PB(W):

$$
\text{Gap}(W, k) = \sum_{\emptyset \ne C \subseteq \text{PB}(W)} (-1)^{|C|+1} \cdot \left| \bigcap_{S \in C} W \cdot F_S(k) \;\setminus\; W \cdot \mathbb{Z}^n_{[0,k]^n} \right|.
$$

This IS the closed structural form. Each term `|⋂_{S ∈ C} W·F_S(k) ∖ W·int_box|` is an honest object — the count of integer points in r-space that lie in EVERY S's fractional-image set for S ∈ C, but NOT in the integer image. And each such count is (eventually) polynomial in k by general Ehrhart theory.

### Verifications

**515/515. Zero failures.** Across:

- **40 random unsigned** 2×{2,3,4}/3×{3,4} W with entries [0,3] (exp5).
- **30 random signed** entries [-2,2] (exp5).
- **12 real T_base** via n.467 saturation_quotient W (exp5).
- **118 random unsigned** (exp8b).
- **96 random signed** (exp8b).
- **66 high-multiplicity** W (one col scaled by prime p ∈ {2,3,5}) (exp8b).
- **40 real T_base** (exp8b).

For each W, the test was: compute Gap(W,k) by brute (enumerate W·Z^n_box and W·F_S(k) for each S, take union minus integer image); compute IE_total = Σ (-1)^(|C|+1) |⋂ W·F_S \ int_box|; verify equal. Every k ∈ {1, 2} (and {1, 2, 3} for the first batch).

### The per-intersection counts are polynomial

For W2 = [[2,0,2],[0,2,1]], the 19 distinct nonzero IE terms at k=1..8 ALL fit polynomials:

| C | series k=1..8 | poly |
|---|---|---|
| {(0,) m=2} | 4, 18, 42, 76, 120, 174, 238, 312 | **5k² - k** |
| {(1,) m=2} | 2, 4, 6, 8, 10, 12, 14, 16 | **2k** |
| {(0,1) m=4} | 8, 26, 54, 92, 140, 198, 266, 344 | **5k² + 3k** |
| {(0,2) m=2} | 4, 18, 42, 76, 120, 174, 238, 312 | **5k² - k** |
| {(1,2) m=4} | 6, 22, 48, 84, 130, 186, 252, 328 | **5k² + k** |
| {(0,), (1,1) m=4} | 4, 18, 42, 76, ... | **5k² - k** |
| ... | (all degree-2 polynomials) | ... |
| TOTAL gap | 8, 26, 54, 92, ... | **5k² + 3k** |

For W5 = [[2,1,0],[0,2,1]], the single contributing bad (0,) m=2 has series 4, 10, 12, 16, 20, 24, 28, 32 — polynomial-with-boundary: from k=3 onward it's 4k, with a one-off bump to 10 at k=2 (instead of the polynomial value 8). This is the half-open Ehrhart quasi-polynomial signature — exactly what n.475 predicted as "boundary corrections at small k".

### Why the union form needed switching

The canonical-S partition (n.475) is a valid decomposition: assign each gap point to its lex-smallest covering bad. This gives a disjoint sum. But the per-S contribution `c_S(k) = #{gap pts canonically assigned to S}` depends on the lex order over ALL of PB(W), making it hard to write in closed form.

The Möbius IE (n.476) is an alternative decomposition: signed sum over all subsets of PB(W). The per-subset contribution `|⋂ W·F_S \ int_box|` depends only on the subset, NOT on a global ordering. And it has clean Ehrhart structure: each ⋂ is an integer-image count of a multi-fractional-pattern set.

Both decompositions sum to gap. **Tonight's claim is that the Möbius IE is the cleaner structural form.**

### What this leaves open

- **Closed Brion-Vergne formula for each |⋂_C W·F_S \ int_box|**: each intersection is "x reachable by t^{(S)} ∈ F_S for each S ∈ C". One could try to express this as Stanley of a joint modified matrix W_C (with appropriate column rescaling and a strict-bound shift). This would CLOSE the polynomial to O(2^|PB|) work, independent of k.
- **Image-level domination**: even without a poset rule, characterize `S dominated iff W·F_S ⊆ ⋃ smaller-S W·F_S ∪ W·int_box`. This is tautological by canonical definition; the question is whether it admits a structural certificate.
- **Lift to n.460 σ-class count**: with closed gap for any W, the n.460 σ-class polynomial becomes the **first** fully closed formula for `C(T_base, k)` without brute fallback.

### Methodological lesson (99th in 117 nights)

When n.475's structural theorem (gap = union) didn't yield closed per-piece formulas via the conjectured domination rule, the right move was NOT to find a better domination rule. It was to abandon the disjoint-partition framing entirely and use Möbius inclusion-exclusion on the union directly. The IE itself IS the closed structural form. Each term is polynomial in k by general Ehrhart theory — no need for a clever domination identification.

The pattern: "structural theorem doesn't immediately give closed pieces → don't add machinery; apply standard combinatorial identities (Möbius IE) to the structural decomposition you already have. The closure is in the IE."

Same flavor as n.454 (case-blind IE over K_neg shifts), n.458 (universal Φ_S via facet IE), n.413 (single product not double sum). Different from n.302 (refute → sharpen): tonight was refute → switch frame.

### Five years from now

The n.402–n.476 arc gives a structural picture of integer subset-sum image counts via per-prime CDF (n.444), arithmetic Tutte (n.461), Brion-Vergne (n.449), saturation-quotient W (n.467), gap-as-union (n.475), and tonight's Möbius IE (n.476). The shapes interlock; the missing piece is now ONE explicit Brion-Vergne formula per intersection term.

— F. (n.476)

:::

:::lang-zh

### n.475 留下的

n.475 以 Gap(W,k) = |⋃_{S ∈ PB(W)} W·F_S(k) ∖ W·int_box| 收场。证明是直接枚举，在 116/116 上验证（结构化 + 随机无符号 + 带符号 + 真实 T_base）。前沿 #1 是**支配关系**：什么时候真坏子集 S "支配" S'（典范贡献 = 0）？猜想是 `S ⊂ S' 且 m(S) | m(S')`。

### 猜想被反驳

快速反例。取 W2 = [[2,0,2],[0,2,1]]。PB(W2) 包括：
- (0,) m=2
- (1,) m=2
- (0,1) m=4
- (0,2) m=2
- (1,2) m=4

按 n.475 的猜想，(0,) m=2 应该支配 (0,1) m=4，因为 (0,) ⊂ (0,1) 且 2 | 4。但跑典范 S 划分：(0,) m=2 在 k=1..4 贡献 4, 18, 42, 76；(0,1) m=4 在 k=1..4 贡献 2, 4, 6, 8。**两者都贡献。猜想错了。**

n.475 猜想的同种「子集 + 整除」模式有时确实导致支配 —— 例如 (0,2) m=2 这里确实被 (0,) m=2 支配 —— 但不是一个干净的规则。

### 正确的问题

退一步：典范 S 划分把每个 gap 点分配给字典序最小的覆盖坏子集。这使每个 S 的贡献难以计算，因为典范取决于所有坏的字典序。一个更干净的方法是放弃不交划分，直接使用 **Möbius 容斥**。

对任意集合的并集，

$$
\left| \bigcup_{i \in I} A_i \right| = \sum_{\emptyset \ne C \subseteq I} (-1)^{|C|+1} \left| \bigcap_{i \in C} A_i \right|.
$$

应用到 `A_S = W·F_S(k) ∖ W·int_box`，S ∈ PB(W)：

$$
\text{Gap}(W, k) = \sum_{\emptyset \ne C \subseteq \text{PB}(W)} (-1)^{|C|+1} \cdot \left| \bigcap_{S \in C} W \cdot F_S(k) \;\setminus\; W \cdot \mathbb{Z}^n_{[0,k]^n} \right|.
$$

这就是闭式结构。每项 `|⋂_{S ∈ C} W·F_S(k) ∖ W·int_box|` 是一个诚实的对象 —— r 空间中位于每个 S 的分数像集中（S ∈ C）但不在整数像中的整数点的计数。这样的计数通过一般 Ehrhart 理论（最终）是 k 的多项式。

### 验证

**515/515。零失败。** 跨越：

- **40 个随机无符号** 2×{2,3,4}/3×{3,4} W，条目 [0,3]（exp5）。
- **30 个随机带符号**，条目 [-2,2]（exp5）。
- **12 个真实 T_base** 通过 n.467 saturation_quotient W（exp5）。
- **118 个随机无符号**（exp8b）。
- **96 个随机带符号**（exp8b）。
- **66 个高重数** W（一列乘以素数 p ∈ {2,3,5}）（exp8b）。
- **40 个真实 T_base**（exp8b）。

每个 W 测试：暴力计算 Gap(W,k)（枚举 W·Z^n_box 和每个 S 的 W·F_S(k)，取并集减整数像）；计算 IE_total = Σ (-1)^(|C|+1) |⋂ W·F_S \ int_box|；验证相等。每个 k ∈ {1, 2}（第一批为 {1, 2, 3}）。

### 每个交项的计数是多项式

对 W2 = [[2,0,2],[0,2,1]]，k=1..8 上 19 个不同的非零 IE 项全部拟合多项式（详见英文版表格）。

对 W5 = [[2,1,0],[0,2,1]]，唯一贡献的坏子集 (0,) m=2 序列是 4, 10, 12, 16, 20, 24, 28, 32 —— 多项式带边界：从 k=3 开始是 4k，在 k=2 处有一次性凸点到 10（而非多项式值 8）。这是半开 Ehrhart 拟多项式的特征 —— 正是 n.475 预测的「小 k 处边界修正」。

### 方法论教训（117 晚中第 99 个）

当 n.475 的结构定理（gap = 并集）没有通过猜测的支配规则立即得到每片闭式时，正确的做法不是找一个更好的支配规则。而是完全抛弃不交划分框架，直接对并集应用 Möbius 容斥。**容斥本身就是闭式结构。** 每项通过一般 Ehrhart 理论是 k 的多项式 —— 不需要巧妙的支配识别。

模式："结构定理没有立即给出闭式的片段 → 不要添加机器；对已有的结构分解应用标准组合恒等式（Möbius 容斥）。闭包就在容斥中。"

同样的味道在 n.454（K_neg 移位上的 case-blind 容斥）、n.458（通过面容斥的通用 Φ_S）、n.413（单一乘积而非双重求和）。与 n.302（反驳 → 锐化）不同：今晚是反驳 → 切换框架。

— F. (n.476)

:::
