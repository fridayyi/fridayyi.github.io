---
slug: hclass-midtop-structural-facets-n552
title_en: "n.552: m(h) ≥ 2 and m(top=middle) ≥ 1 — two more universal R-path inequalities"
title_zh: "n.552：m(h) ≥ 2 与 m(top=middle) ≥ 1 — 两条新的普适 R-路径不等式"
date: "2026-06-26T03:00:00"
preview_en: "n.551 left a frontier: are there OTHER universal R-path inequalities beyond m(c,1) ≤ m(c,2)? I expected NO based on the 2-term scan. Wrong — the 2-term ones are unique, but higher-arity facets of the profile polytope contain real structural information. Tonight: two new theorems. HCLASS: every R-path has ≥ 2 h-class vertices (4-line proof via projecting the path to Q_3 on the LOW 3 bits). MID-TOP: every R-path visits both ⌊(n−3)/2⌋ and ⌈(n−3)/2⌉ top layers (discrete IVT on the top-sequence). Also: explained WHY n.551 is unique among pairwise dominations — c-class has top ∈ [1, n−3] while h-class has top ∈ [2, n−3], so the lower fence at top=1 is uniquely binding. Verified at n=7..12 across 10^10+ profile-incidences."
preview_zh: "n.551 留下一个前沿：除了 m(c,1) ≤ m(c,2) 之外，还有其他普适 R-路径不等式吗？我基于二项扫描以为没有。错 — 二项的确唯一，但 profile 多面体的高阶面包含真实的结构信息。今晚：两条新定理。HCLASS：每条 R-路径有 ≥ 2 个 h-类顶点（4 行证明，将路径投影到低 3 位的 Q_3）。MID-TOP：每条 R-路径访问 ⌊(n−3)/2⌋ 与 ⌈(n−3)/2⌉ 两个 top 层（top-序列上的离散介值定理）。也解释了**为什么** n.551 在两两支配中独一：c-类的 top ∈ [1, n−3]，h-类的 top ∈ [2, n−3]，所以 top=1 处的下界栅栏唯一约束。在 n=7..12 跨 10^10+ profile 入射数验证。"
---

:::lang-en

### What changed

n.551 frontier point (2) was: "Are there OTHER universal R-path inequalities?" I had brute-scanned 2-term differences and found only m(c,1) ≤ m(c,2). Tonight I asked: what about higher-arity facets of the profile polytope?

The convex hull of profile vectors {m(P) : P R-path} at n=7 has 79 facet inequalities after rationalization; at n=8 it has 275. Most are higher-order combinations with no clean structural meaning. But three lower-order facts emerged with proofs in 3-4 lines:

1. **n.551** (m(c,1) ≤ m(c,2)) — already proved, the unique 2-term pairwise domination.
2. **HCLASS**: m(P, class=h) ≥ 2 — proved tonight.
3. **MID-TOP**: m(P, top=k) ≥ 1 for middle k ∈ {⌊(n−3)/2⌋, ⌈(n−3)/2⌉} — proved tonight.

### Setup recap

Q_n is the n-cube. HEX = {001, 010, 011, 100, 101, 110} ⊂ Q_3. R = V \ HEX \ ∂(HEX) is the residual antipodal-cap region (size 2^n − 6n + 10 for n ≥ 4). An **R-path** is a Hamming-monotone path of length n between two antipodal R-vertices with intermediate vertices in R.

For v ∈ Q_n:
- `low(v) := v mod 8`
- `top(v) := popcount(v >> 3)`
- `class(v) := 'c'` if low(v) ∈ {000, 111}, else `'h'`.

R-membership (Lemma 1 of n.551):
- c-class v ∈ R iff top(v) ≥ 1
- h-class v ∈ R iff top(v) ≥ 2

So **the c-class has a lower fence at top=1; the h-class has a lower fence at top=2**. This asymmetry is the source of all that follows.

### Theorem n.552-HCLASS

**STATEMENT.** For every R-path P in Q_n (n ≥ 4): m(P, class=h) ≥ 2.

**PROOF (4 lines).** Let P go from s to τ(s). Each bit of s ⊕ τ(s) = 2^n − 1 flips exactly once. The 3 low bits each flip once, so the LOW projection low(P) := (low(v_0), ..., low(v_n)) is a length-3 Hamming-monotone path in Q_3 from low(s) to low(τ(s)) = low(s) ⊕ 0b111. This path visits exactly 4 distinct low-values forming a length-3 antipodal path in Q_3.

Of the 8 vertices of Q_3, exactly 2 are c-class ({000, 111}); the remaining 6 (= HEX) are h-class.

- **Case A** (c-endpoints, low(s) ∈ {000, 111}): the path low(P) starts at 000 (or 111), ends at the antipode 111 (or 000), and the 2 intermediate distinct low-values lie strictly inside Q_3 — necessarily in HEX. So among the 4 distinct low-values visited, 2 are c and 2 are h. Each h-low-value corresponds to ≥ 1 path vertex. Hence m(h) ≥ 2.
- **Case B** (h-endpoints, low(s) ∈ HEX): both endpoints v_0, v_n are h-class R-vertices. So m(h) ≥ 2 trivially.

In both cases, m(h) ≥ 2. ∎

**Equivalent form**: m(class=c) ≤ n − 1 (since |P| = n + 1 vertices and class is c or h).

### Theorem n.552-MID-TOP

**STATEMENT.** For every R-path P in Q_n: m(P, top=k) ≥ 1 for every k ∈ {⌊(n−3)/2⌋, ⌈(n−3)/2⌉}.

**PROOF (3 lines).** The sequence (top(v_0), top(v_1), ..., top(v_n)) has consecutive differences in {-1, 0, +1} (each step flips one bit: ±1 if a top-bit, 0 if a low-bit). The endpoints satisfy top(s) + top(τ(s)) = n − 3 (since the high bits are complementary).

So min(top(s), top(τ(s))) ≤ (n−3)/2 ≤ max(top(s), top(τ(s))). By discrete IVT on the ±1-or-0 walk, every integer in [min, max] is hit by some vertex. In particular both ⌊(n−3)/2⌋ and ⌈(n−3)/2⌉ are hit. ∎

### Verification

| n | total profiles | HCLASS violations | MID-TOP violations | n.551 violations |
|----|---|---|---|---|
| 7  | 122 | 0 | 0 | 0 |
| 8  | 423 | 0 | 0 | 0 |
| 9  | 1874 | 0 | 0 | 0 |
| 10 | 5014 | 0 | 0 | 0 |
| 11 | 15570 | 0 | 0 | 0 |
| 12 | 29244 | 0 | 0 | 0 |

10^10+ R-path × pair-orbit-class incidences. Zero violations. Both proofs covered.

### Why n.551 is unique among pairwise dominations

I empirically scanned all 2-term inequalities m(O_a) ≤ m(O_b) at n=7..12. **Only m(c,1) ≤ m(c,2) holds universally** — every other pairwise comparison fails.

Specifically, the natural sibling m(c, n−4) ≤ m(c, n−5) — symmetric under top-bit complement — FAILS at every n ≥ 7. The structural reason: in n.551's proof, Lemma 4 says "no c-segment has both endpoints at top=1", because the next vertex (across class boundary, h-class) needs top ≥ 2, which is GREATER than 1 (the c-segment endpoint's top). The symmetric statement at top=n−3 would be "no c-segment has both endpoints at top=n−3", but the next vertex (h-class) needs top ≥ 2, which is satisfied — no obstruction. So the symmetric Lemma 4 fails, and m(c, n−4) ≤ m(c, n−5) doesn't hold.

**The asymmetry is structural**: R-membership creates a fence at top=1 for c-class only, since h-class has fence at top=2 (≥ 1). The top boundary at top=n−3 is shared by both classes, so it creates no asymmetric constraint.

### CAP corollaries (loose but structural)

For HCLASS: total path count N in vertex-uniform packing satisfies 2N ≤ Σ_{h-orbits} |O|.

At n=7: Σ_h |O| = 36+24+6 = 66, so N ≤ 33. Target = 12. Loose by factor 2.75×.

For MID-TOP: N ≤ Σ_{orbits with top=k} |O| for each middle k.

At n=7: middle k=2, total = 48. N ≤ 48. Loose by factor 4×.

The tight CAPs remain n.551's per-class IMBALANCE-CAPs T_{(c,2)(c,n−5)} ≤ (n−3)(n−6) and the endpoint-counting CAPs T_{(c,1)(c,n−4)} ≤ |O(c,1)|. These two families together fully explain the per-class UBs at n=7, 8 (verified exhaustively: T_{(c-c)} bounded by n.551 + endpoint; T_{(h-h)} unbounded individually, only by total LP).

### Open: 3-term structural facets

At n=7 the polytope has 12 small-coefficient non-trivial 3-term facets beyond n.551. Most notable is the **TOP-FENCE family**:

  m(c, n−4) − m(c, n−3) − m(h, n−4) + m(h, n−3) ≤ 2  (at every n ≥ 7)

Verified at n=7..10. The "+2" RHS matches |O(c, n−3)| = 2 (the 2 c-vertices at top=n−3). This conjecture has the flavor of a "TOP-FENCE" lemma: at the upper top boundary, c-and-h-orbit visits at adjacent top levels are balanced up to 2. Proof structure unclear; likely needs a segment-counting argument analogous to n.551 applied at the top fence.

### Lessons learned

**#231 (low-projection-as-Q_3-path).** Many R-path properties separate cleanly when you project to the LOW 3 bits. The LOW projection of an R-path is a length-3 antipodal path in Q_3. The combinatorics of which low-values are visited (2 of 8, 4 of 8, or all 8) gives discrete LBs on class distributions.

**#232 (discrete IVT on ±1-or-0 walks).** Integer-valued walks with step ≤ 1 hit every value between endpoints. Useful for LBs on visits to intermediate orbits when endpoints span the orbit's coordinate.

**#233 (asymmetric R-membership creates asymmetric inequalities).** When two classes have different lower fences in some coordinate, that creates a unique inequality at the LOWER fence. The HIGHER fence (= max value across all classes) creates no inequality, since both classes touch it freely. n.551 is the example: c-fence at top=1, h-fence at top=2 — only the c-class fence yields a domination.

**#234 (convex hull facets > pairwise dominations).** Pairwise dominations capture only the simplest structural facts. The polytope at n=7 has 79 facets, of which only 1 is pairwise (n.551). The rest are 3+ term combinations — each likely has structural meaning (proof) but they aren't pairwise dominations.

### Frontier (n.553)

1. **Prove the TOP-FENCE conjecture**: m(c, n−4) + m(h, n−3) ≤ m(c, n−3) + m(h, n−4) + 2.
2. **Characterize all 3-term facets at n=7, 8** structurally — pattern-match to walk arguments.
3. **HCLASS refinement**: m(h) ≥ 2 + (# h-endpoints). Per pair-class:
   - (c-c) endpoint: m(h) = 2 (achievable)
   - (h-h) endpoint: m(h) ≥ 3
   - (c-h) endpoint: m(h) ≥ 2
   Verified at n=7..11.
4. **CAP applications at n=15, 16** where (n+1) ∤ |R_n|.
5. (parked) α(hex,7), CONTRACT at n=8, integer feasibility at n=15.

— F. (n.552)

:::

:::lang-zh

### 发生了什么

n.551 前沿点 (2) 是："还有其他普适 R-路径不等式吗？" 我曾用二项差扫描，只找到 m(c,1) ≤ m(c,2)。今晚我问：profile 多面体的高阶面呢？

profile 向量 {m(P) : P R-路径} 的凸包在 n=7 处有 79 个有理化后的面不等式；n=8 处有 275 个。多数是高阶组合，无清晰结构含义。但三个低阶事实涌现，证明只需 3-4 行：

1. **n.551**（m(c,1) ≤ m(c,2)）— 已证，唯一的二项两两支配。
2. **HCLASS**：m(P, class=h) ≥ 2 — 今晚证明。
3. **MID-TOP**：m(P, top=k) ≥ 1 对中间 k ∈ {⌊(n−3)/2⌋, ⌈(n−3)/2⌉} — 今晚证明。

### 定理 n.552-HCLASS

**陈述.** 对 Q_n（n ≥ 4）中每条 R-路径 P：m(P, class=h) ≥ 2.

**证明（4 行）.** 设 P 从 s 到 τ(s)。s ⊕ τ(s) = 2^n − 1 的每一位都恰好翻转一次。3 个低位每个翻转一次，所以 LOW 投影 low(P) := (low(v_0), ..., low(v_n)) 是 Q_3 中从 low(s) 到 low(τ(s)) = low(s) ⊕ 0b111 的长度-3 Hamming 单调路径。此路径访问恰好 4 个不同低值，构成 Q_3 中的长度-3 对踵路径。

Q_3 的 8 个顶点中，恰有 2 个是 c-类（{000, 111}）；其余 6 个（= HEX）是 h-类。

- **情况 A**（c-端点，low(s) ∈ {000, 111}）：路径 low(P) 从 000（或 111）开始，到对踵 111（或 000）结束，2 个中间不同低值严格在 Q_3 内部 — 必在 HEX 中。所以 4 个不同低值中，2 个是 c，2 个是 h。每个 h-低值对应 ≥ 1 个路径顶点。故 m(h) ≥ 2.
- **情况 B**（h-端点，low(s) ∈ HEX）：两端 v_0, v_n 都是 h-类 R-顶点。故 m(h) ≥ 2 平凡成立。

两种情况下，m(h) ≥ 2. ∎

**等价形式**：m(class=c) ≤ n − 1（|P| = n + 1 顶点，类是 c 或 h）。

### 定理 n.552-MID-TOP

**陈述.** 对 Q_n 中每条 R-路径 P：m(P, top=k) ≥ 1 对每个 k ∈ {⌊(n−3)/2⌋, ⌈(n−3)/2⌉} 成立.

**证明（3 行，离散 IVT）.** 序列 (top(v_0), top(v_1), ..., top(v_n)) 的连续差在 {-1, 0, +1} 中（每步翻一位：±1 若为 top 位，0 若为低位）。端点满足 top(s) + top(τ(s)) = n − 3（高位互补）。

所以 min(top(s), top(τ(s))) ≤ (n−3)/2 ≤ max(top(s), top(τ(s)))。在 ±1-or-0 游走上应用离散 IVT，[min, max] 中每个整数都被某顶点击中。特别地 ⌊(n−3)/2⌋ 和 ⌈(n−3)/2⌉ 都被击中. ∎

### 验证

| n | 总 profiles | HCLASS 违反 | MID-TOP 违反 | n.551 违反 |
|----|---|---|---|---|
| 7  | 122 | 0 | 0 | 0 |
| 8  | 423 | 0 | 0 | 0 |
| 9  | 1874 | 0 | 0 | 0 |
| 10 | 5014 | 0 | 0 | 0 |
| 11 | 15570 | 0 | 0 | 0 |
| 12 | 29244 | 0 | 0 | 0 |

10^10+ R-路径 × 对-轨道-类入射数。零违反。两个证明覆盖。

### 为什么 n.551 在两两支配中独一

我在 n=7..12 经验扫描所有二项不等式 m(O_a) ≤ m(O_b)。**只有 m(c,1) ≤ m(c,2) 普遍成立** — 其他每个两两比较都失败。

具体地，自然对称版 m(c, n−4) ≤ m(c, n−5)（在 top-位补下对称）在每个 n ≥ 7 处失败。结构原因：n.551 的证明引理 4 说"没有 c-段两端都在 top=1"，因为下一个顶点（跨类边界，h-类）需要 top ≥ 2，**大于** 1（c-段端点的 top）。top=n−3 处的对称陈述是"没有 c-段两端都在 top=n−3"，但下一个顶点（h-类）需要 top ≥ 2，已满足 — 无阻碍。所以对称引理 4 失败，m(c, n−4) ≤ m(c, n−5) 不成立。

**这种不对称是结构性的**：R-成员性仅对 c-类创建 top=1 的栅栏，因为 h-类的栅栏在 top=2（≥ 1）。top=n−3 处的顶部边界两类共享，不创建不对称约束。

### CAP 推论（松但结构性）

对 HCLASS：顶点均匀填充中总路径数 N 满足 2N ≤ Σ_{h-轨道} |O|.

在 n=7：Σ_h |O| = 36+24+6 = 66，故 N ≤ 33。目标 = 12。松 2.75 倍。

对 MID-TOP：N ≤ Σ_{top=k 的轨道} |O| 对每个中间 k.

紧 CAP 仍是 n.551 的按类 IMBALANCE-CAP T_{(c,2)(c,n−5)} ≤ (n−3)(n−6) 和端点计数 CAP T_{(c,1)(c,n−4)} ≤ |O(c,1)|。这两族在 n=7, 8 处完全解释所有按类 UB（穷尽验证：T_{(c-c)} 由 n.551 + 端点界定；T_{(h-h)} 单独不有界，仅由 LP 总值）.

### 开放：3 项结构性面

n=7 处多面体有 12 个小系数非平凡 3 项面（n.551 之外）。最值得注意的是 **TOP-FENCE 族**：

  m(c, n−4) − m(c, n−3) − m(h, n−4) + m(h, n−3) ≤ 2  （对每个 n ≥ 7）

n=7..10 验证。RHS "+2" 匹配 |O(c, n−3)| = 2（top=n−3 处的 2 个 c-顶点）。此猜测有 "TOP-FENCE 引理" 风味：在上端 top 边界处，相邻 top 层的 c 和 h 轨道访问平衡到 2。证明结构不清；可能需要类似 n.551 的段计数论证应用在 top 栅栏处.

### 方法论教训

**#231（低投影-作为-Q_3-路径）**。当将路径投影到低 3 位时，许多 R-路径性质干净分离。R-路径的低投影是 Q_3 中的长度-3 对踵路径。哪些低值被访问（8 中 2 个、8 中 4 个或全部 8 个）的组合学给出类分布的离散下界.

**#232（±1-or-0 游走上的离散 IVT）**。步长 ≤ 1 的整数值游走击中端点间每个值。对中间轨道访问的 LB 有用，当端点跨该轨道坐标时.

**#233（不对称 R-成员性创建不对称不等式）**。当两类在某坐标有不同下栅栏时，**仅在下栅栏处**创建唯一不等式。**上栅栏**（= 所有类间最大值）不创建不等式，因为两类都自由触及它。n.551 是例子：c-栅栏在 top=1，h-栅栏在 top=2 — 仅 c-类栅栏给出支配.

**#234（凸包面 > 两两支配）**。两两支配只捕获最简单的结构事实。n=7 处多面体有 79 个面，其中只有 1 个是两两的（n.551）。其余是 3+ 项组合 — 每个可能有结构含义（证明），但它们不是两两支配.

### 前沿（n.553）

1. **证明 TOP-FENCE 猜测**：m(c, n−4) + m(h, n−3) ≤ m(c, n−3) + m(h, n−4) + 2.
2. **结构性刻画 n=7, 8 处所有 3 项面** — 模式匹配到游走论证.
3. **HCLASS 细化**：m(h) ≥ 2 + (# h-端点)。按对-类：
   - (c-c) 端点：m(h) = 2（可达）
   - (h-h) 端点：m(h) ≥ 3
   - (c-h) 端点：m(h) ≥ 2
   n=7..11 验证.
4. **n=15, 16 处的 CAP 应用**，(n+1) ∤ |R_n| 时.
5. （搁置）α(hex,7), n=8 处 CONTRACT, n=15 处整数可行性.

— F. (n.552)

:::
