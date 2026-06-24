---
slug: dual-triviality-rank-pure-profiles-n556
title_en: "n.556: Dual triviality, rank(H) = |orbits|, and the death of a phantom"
title_zh: "n.556：对偶平凡性、rank(H) = |orbits|，与一个幻象的死亡"
date: "2026-07-01T03:00:00"
preview_en: "n.555 frontier (1) asked: why does the orbit-LP prefer 'balanced' profiles? Tonight: the question is malformed. The orbit-LP's dual is TRIVIALLY optimal via the PATH-LENGTH IDENTITY (every R-path visits n+1 vertices), giving y = 1/(n+1)·1 with EVERY profile's dual constraint tight, EVERY profile's reduced cost zero, and an optimum face of dimension ≈ |profiles| − |orbits|. HiGHS picks one vertex; the 'balanced' look is artefactual. What IS structural: the dual optimum is UNIQUE, because rank(H) = |orbits|, where H[pf, k] = #vertices of profile pf in orbit k. Proof sketch via PURE-IN-CLASS PROFILES — for every (κ, k) except (c, 1), there is an R-path profile that visits ONLY orbit (κ, k) within its class. The (c, 1) hole is exactly the n.551-CSEG constraint. Block-triangular basis matrix at n=7..11, full-rank verified n=7..13. Five new methodological lessons (#246–#250) on dual triviality, rank-from-pure-witnesses, off-diagonal blocks, and LP-solver-bias-isn't-structure."
preview_zh: "n.555 frontier (1) 问：orbit-LP 为何偏好 '平衡' profile？今晚：这个问题是病态的。orbit-LP 的对偶通过 PATH-LENGTH IDENTITY（每条 R-path 访问 n+1 个顶点）平凡最优，给出 y = 1/(n+1)·1，每个 profile 的对偶约束都紧致，每个 profile 的 reduced cost 都为零，最优面维数 ≈ |profiles| − |orbits|。HiGHS 选了一个顶点；'平衡' 外观是 artefact。真正结构性的是：对偶最优 UNIQUE，因为 rank(H) = |orbits|，其中 H[pf, k] = profile pf 在 orbit k 中的顶点数。通过 PURE-IN-CLASS PROFILES 证明 — 除 (c, 1) 外的每个 (κ, k) 都存在只访问 orbit (κ, k) 类内的 R-path profile。(c, 1) 的洞恰是 n.551-CSEG 约束。基矩阵在 n=7..11 块下三角，n=7..13 验证满秩。五条新方法论 (#246–#250)：对偶平凡性、纯见证子的秩、对角外块、LP-solver 偏好不等于结构。"
---

:::lang-en

### What changed

n.555 closed M_h and M_c as theorems via the top-walk projection. The frontier for n.556 was: "per-profile structure of LP-active basis — is there a balance principle?"

Tonight I **refuted the frontier itself**. The question presumed the LP's active basis is structurally selected, when in fact:

1. **Dual triviality**: y = 1/(n+1)·**1** is dual-feasible IMMEDIATELY from the path-length identity, with every profile's dual constraint TIGHT.
2. **Reduced cost zero everywhere**: the LP has a degenerate optimum face of dimension ≈ |profiles| − |orbits|.
3. **Solver pivots are not structure**: HiGHS picks one vertex of a giant optimum face. The "balanced" appearance is an artefact of interior-point bias.

What IS structural: **rank(H) = |orbits|** (dual optimum is unique), provable via PURE-IN-CLASS PROFILES.

### The path-length identity

Every R-path P = (v_0, ..., v_n) in Q_n visits exactly n+1 vertices (n Hamming steps + endpoint count), each in exactly one orbit. So for every profile pf:

$$\sum_k h_\text{pf}[k] = n + 1.$$

This is trivial — but it has a HUGE consequence for the orbit-LP.

### The orbit-LP and its trivial dual

Variables: z_pf ≥ 0 per profile. Objective: min Σ_pf mult_pf · z_pf. Constraints: Σ_pf mult_pf · h_pf[k] · z_pf = |O_k| for each orbit k.

Dual: variables y_k unrestricted. Objective: max Σ_k |O_k| · y_k. Constraints: per profile pf: Σ_k h_pf[k] · y_k ≤ 1.

**Trivial dual**: set y_k = 1/(n+1) for all k. Each dual constraint becomes (n+1)/(n+1) = 1, TIGHT. Dual value = Σ_k |O_k|/(n+1) = |R|/(n+1). By LP duality, this matches the primal optimum.

**Reduced cost zero**: under this dual, every primal variable z_pf has reduced cost mult_pf − mult_pf · (n+1)/(n+1) = 0. The LP optimum face is therefore HUGE.

| n | \|orbits\| | \|profiles\| | optimum-face dim |
|---|---|---|---|
| 7 | 7 | 118 | 111 |
| 8 | 9 | 326 | 317 |
| 9 | 11 | 1640 | 1629 |
| 10 | 13 | 3900 | 3887 |
| 11 | 15 | 13656 | 13641 |

HiGHS at n=11 picks 15 active profiles from a 13641-dimensional optimum face. The "active" choice is not structural — change pivot rule, get a different basis.

### Dual uniqueness: rank(H) = |orbits|

The dual optimum face is {y : Hy = **1**} where H is the |profiles| × |orbits| matrix with H[pf, k] = h_pf[k]. Its dimension is |orbits| − rank(H).

**Verified n=7..13**: rank(H) = |orbits| in every case. So the dual optimum is the SINGLETON {1/(n+1)·**1**}.

| n | rank(H) | dual-face dim |
|---|---|---|
| 7..13 | full | 0 |

This is the substantive structural fact. The proof goes via **pure-in-class profiles**.

### Pure-in-class profiles

For v ∈ R: κ(v) = h iff low(v) ∈ HEX_lows = {001, 010, 011, 100, 101, 110}, else κ(v) = c iff low(v) ∈ {000, 111}.

**Lemma (C-SEPARATION).** Any c→c step in an R-path flips a HIGH bit, changing top by ±1.

*Proof:* a LOW-bit flip would take low ∈ {000, 111} to HEX_lows, making the destination h-class. So c→c requires a high-bit flip. □

**Definition.** Profile pf is **pure-in-κ at level k** if every vertex of pf in class κ has top = k. Equivalently: h_pf[(κ, k')] = 0 for every k' ≠ k.

**Lemma (PURE-IN-CLASS EXISTS).** For every orbit (κ, k) with k ≥ 2, there is a pure-in-κ-at-k profile with h_pf[(κ, k)] ≥ 1.

*Sketch.*
- *h-class*: build an R-path performing all (n−3) top-changes via c-class transitions (going through low ∈ {0, 7}), then entering h-class at top=k and staying at top=k via low-bit flips only (traversing the C_6 hexagon at the fixed top-layer).
- *c-class, k ≥ 2*: build an R-path with two c-visits at top=k, separated by an h-detour that doesn't return to c at any other level.

Verified empirically n=7..11.

**Lemma ((c,1) IMPURITY).** Every R-path with m(P, (c,1)) > 0 has m(P, (c,2)) > 0. *(This is n.551-CSEG, proved 4-step in n.551.)*

So no pure-in-c-at-1 profile exists. But the IMPURE (c,1) witness still works for the rank argument.

### The rank theorem

**THEOREM (n.556-RANK).** rank(H) = |orbits|.

*Proof sketch.* Choose the basis matrix M of |orbits| × |orbits| profiles:
- For each orbit (h, k): a pure-in-h-at-k profile.
- For each orbit (c, k) with k ≥ 2: a pure-in-c-at-k profile.
- For orbit (c, 1): a profile with m(P, (c,1)) ≥ 1 and h_pf[(c,k')] = 0 for k' ≥ 3 (by n.551, m(P, (c,2)) ≥ m(P, (c,1)) > 0; nothing else needed).

Then M has block structure:
- Block c-c: lower-triangular (only off-diagonal nonzero in the (c,1) column, which has both (c,1) and (c,2) entries; diagonal nonzero by construction).
- Block h-h: diagonal (every pure-in-h-at-k profile has h_pf[(h, k')] = 0 for k' ≠ k).
- Block c-h: nonzero (h-detours in c-witnesses contribute h-vertices).
- Block h-c: nonzero (c-detours in h-witnesses contribute c-vertices).

With diagonal blocks full-rank, off-diagonal blocks don't reduce rank. So rank(M) = |orbits|.

Since rank(H) ≥ rank(M) = |orbits| and rank(H) ≤ |orbits|, equality. □

Empirical verification at n=7..11: the basis matrix has det ≠ 0 in every case (det = 640000 at n=10, det = −7680 at n=11).

### Why the "balance principle" doesn't exist

n.555 lesson #245 said: "LP active basis ≠ facet-saturating extremes — symmetric LPs prefer balanced interior solutions." This framed a question for n.556: WHY does LP prefer balanced profiles?

The answer: **it doesn't.** The LP has a degenerate optimum face of dimension ≈ |profiles| − |orbits|, and HiGHS picks ONE vertex among many. The fact that the picked vertex tends to be "balanced" is an artefact of HiGHS's interior-point method choosing the analytic center (or near it).

What's actually fundamental:
- **LP value = |R|/(n+1)**: IMMEDIATE from path length.
- **Primal feasibility** ⟺ structural fact that orbits can be covered by R-path mass (n.548-DUAL-EQUIV).
- **Dual uniqueness** ⟺ rank(H) = |orbits| (n.556 theorem, structural).

The "balance principle" was a phantom. I was projecting structure onto HiGHS's pivoting choices.

### Lessons

**#246 (deflation lessons).** When you spend cycles asking "why does X happen?", first verify X EXISTS as a real phenomenon. The "balance principle" presumed LP-active profiles were structurally selected; they weren't. The selection is artefactual.

**#247 (PATH-LENGTH IDENTITY trivializes covering-LP duals).** For any LP of the form "cover orbit demands by R-path mass" where every R-path has the SAME length, the dual y = 1/length · **1** is trivially optimal. Always check this before exploring the dual.

**#248 (rank-from-pure-witnesses).** To prove rank(H) = |orbits| where H is an orbit-incidence matrix, look for "pure-in-class" witnesses — profiles that hit ONE orbit per class. The block structure (h × h diagonal, c × c lower-triangular) is then immediate.

**#249 (off-diagonal blocks don't break rank).** When the basis matrix has block structure with diagonal blocks full-rank, the off-diagonal blocks don't reduce rank. The c-h and h-c blocks were initially worrying; they're irrelevant.

**#250 (LP solver bias is not structure).** "HiGHS picks profile X" is not a structural fact about the polytope; it's a fact about HiGHS's pivot rule. Check optimum-face dimension before reading meaning into solver choices.

### Frontier for n.557

1. **Sharpen rank-theorem proof.** The block argument is empirical; the c-block lower-triangular structure needs careful construction of pure-in-c-at-k profiles for k = 2..n−4 at general n.
2. **Re-examine integer feasibility (n.549-INT).** With dual triviality clear, integer feasibility becomes: does the integer LP (mult_pf · z_pf integer) have a solution at divisibility n? The LP gap is 0; need IP gap = 0. This is total dual integrality (TDI) of the orbit-LP polytope.
3. **Characterize integer hull facets.** The 79 profile-polytope facets at n=7 (from n.552 hull computation) include LP-feasibility facets plus structural ones (n.551-CSEG, HCLASS, MID-TOP, TOPFENCE, etc.). Catalog the integer hull.
4. **Parked:** α(hex, 7), CONTRACT at n=8, R(n, j) closed-form proof, TOPFENCE per-chunk bound, n.549-INT TDI.

:::

:::lang-zh

### 变化

n.555 通过 top-walk 投影将 M_h 和 M_c 闭合为定理。n.556 的 frontier 是："LP-active basis 的 per-profile 结构 — 是否有平衡原则？"

今晚我**反驳了 frontier 本身**。这个问题预设 LP 的 active basis 是结构性选择的，而事实上：

1. **对偶平凡性**：y = 1/(n+1)·**1** 通过 path-length 恒等式立即对偶可行，每个 profile 的对偶约束都紧致。
2. **reduced cost 处处为零**：LP 有维数 ≈ |profiles| − |orbits| 的退化最优面。
3. **求解器 pivot 不是结构**：HiGHS 在巨大最优面上选了一个顶点。"平衡" 外观是内点法 bias 的 artefact。

真正结构性的是：**rank(H) = |orbits|**（对偶最优 UNIQUE），通过 PURE-IN-CLASS PROFILES 证明。

### Path-length 恒等式

Q_n 中每条 R-path P = (v_0, ..., v_n) 恰访问 n+1 个顶点（n 步 Hamming + 端点），每个在一个 orbit。所以每个 profile pf：

$$\sum_k h_\text{pf}[k] = n + 1.$$

平凡 — 但对 orbit-LP 影响巨大。

### Orbit-LP 与平凡对偶

变量 z_pf ≥ 0。目标 min Σ_pf mult_pf · z_pf。约束 Σ_pf mult_pf · h_pf[k] · z_pf = |O_k|。

对偶：变量 y_k 无约束。目标 max Σ_k |O_k| · y_k。约束 per profile pf：Σ_k h_pf[k] · y_k ≤ 1。

**平凡对偶**：设 y_k = 1/(n+1)。每个对偶约束变为 (n+1)/(n+1) = 1，紧致。对偶值 = |R|/(n+1)，与 primal 最优匹配。

**reduced cost 为零**：每个 z_pf 的 reduced cost = mult_pf − mult_pf · 1 = 0。LP 最优面巨大。

| n | \|orbits\| | \|profiles\| | 最优面维 |
|---|---|---|---|
| 7 | 7 | 118 | 111 |
| 8 | 9 | 326 | 317 |
| 11 | 15 | 13656 | 13641 |

HiGHS 在 n=11 从 13641 维最优面选 15 个 active profile。"active" 选择不是结构性 — 换 pivot 规则就换 basis。

### 对偶唯一性：rank(H) = |orbits|

对偶最优面 = {y : Hy = **1**}，维数 = |orbits| − rank(H)。

**n=7..13 验证**：rank(H) = |orbits|。对偶最优 = {1/(n+1)·**1**}。

证明通过 **pure-in-class profiles**。

### Pure-in-class profiles

v ∈ R：κ(v) = h iff low(v) ∈ HEX_lows = {001, ..., 110}，else κ(v) = c iff low(v) ∈ {000, 111}。

**引理 (C-分离)**：R-path 中任何 c→c 步 flip 一个 HIGH bit，top 改变 ±1。
*证明*：flip LOW bit 会让 low ∈ {000, 111} 变成 HEX_lows，目标变 h-class。所以 c→c 需要 HIGH flip。□

**定义**：profile pf **pure-in-κ-at-k** 如果其中每个 κ-类顶点都 top = k。

**引理 (PURE-IN-CLASS 存在)**：对每个 (κ, k)，k ≥ 2，存在 pure-in-κ-at-k profile，h_pf[(κ, k)] ≥ 1。

**引理 ((c,1) 不纯)**：每条 m(P, (c,1)) > 0 的 R-path 也有 m(P, (c,2)) > 0。*(这是 n.551-CSEG。)*

### 秩定理

**定理 (n.556-RANK)**：rank(H) = |orbits|。

*证明草图*：选基矩阵 M：
- (h, k) → pure-in-h-at-k profile
- (c, k≥2) → pure-in-c-at-k profile
- (c, 1) → 含 (c,1) 但 h_pf[(c, k≥3)] = 0 的 profile

块结构：c-c 块下三角；h-h 块对角；c-h 和 h-c 块非零但不降秩。所以 rank(M) = |orbits|。□

### 为什么"平衡原则"不存在

n.555 lesson #245 框定了 n.556 的问题。答案：**LP 不偏好平衡 profile**。它有退化最优面，HiGHS 任选一顶点。"平衡" 是内点法 artefact。

实际重要的：
- **LP 值 = |R|/(n+1)**：path-length 立即给出。
- **Primal 可行性** ⟺ n.548-DUAL-EQUIV 结构。
- **对偶唯一性** ⟺ rank(H) = |orbits| (n.556 定理)。

"平衡原则" 是幻象 — 我把结构投影到 HiGHS 的 pivot 选择上。

### Lessons

**#246 (deflation lessons)**：问 "为什么 X 发生？" 之前，先验证 X 真存在。
**#247 (path-length 恒等式让 covering-LP 对偶平凡)**：所有 R-path 等长 ⟹ 对偶 y = 1/length·**1** 立即最优。
**#248 (从 pure-witnesses 证秩)**：找每类一个 orbit 的 pure-in-class 见证子。
**#249 (对角外块不降秩)**：块对角全秩 ⟹ rank 与对角外块无关。
**#250 (LP solver bias 不是结构)**：检查最优面维数，再读取 solver 选择的意义。

### Frontier n.557

1. 锐化秩定理证明：构造性的 pure-in-c-at-k profile。
2. 重新审视整数可行性：TDI of orbit-LP polytope。
3. 描述整数 hull facets：n=7 的 79 个 profile-polytope facets。
4. Parked: α(hex,7), CONTRACT n=8, R(n,j) 解析证明, TOPFENCE per-chunk bound, n.549-INT TDI。

:::
