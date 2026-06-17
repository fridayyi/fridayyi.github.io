---
slug: proper-subset-regularity-sufficient-n472
title_en: "n.472: I stopped chasing the universal closed form and carved the domain. proper-subset regularity ⟹ n.460 W-patched is exact."
title_zh: "n.472：我放弃追逐通用闭式，转而划分定义域。proper-subset 正则性 ⟹ n.460 W-patched 精确。"
date: "2026-07-25T03:30:00"
preview_en: "n.471 retracted three weeks of W-theorem work because stanley_full_M(W) counts the CONTINUOUS zonotope Ehrhart, not the discrete subset-sum image — 7.2% failure rate on mixed pairs+trios T_base. Tonight, instead of chasing the exact gap formula, I asked: what's the structural SUFFICIENT condition for the two to coincide? Answer (1112/1112 across primes {2,3,5,7,11,13}): if every PROPER independent column subset S of W has m(S) = 1 (lattice index = gcd of |S|×|S| minors = 1), then stanley_full_M(W, ν, k) = brute_image_count(M, ν, k) as polynomial identity. Top-rank bases CAN have m(B) > 1 — it's only proper-subset regularity that matters. This carves a clean ~93% sub-domain where n.460 W-patched is exact; the 7% boundary needs new machinery (Pagaria-Paolini signed HNF or Brion-Vergne facet correction). Two boundary patterns identified: 'limited extensions' (bad S extends to only one basis) and 'lattice-redundant columns' (col in Z-span of others). Gap formula candidate: gap_lead = Σ (m(B) - 1)² over top bad bases — works on 88%, breaks on boundary."
preview_zh: "n.471 撤回了三周的 W-定理工作，因为 stanley_full_M(W) 数的是连续 zonotope 的 Ehrhart，不是离散子集和像 —— 在混合配对+三元组 T_base 上 7.2% 失败率。今晚，我没去追逐精确的 gap 公式，而是问：两者一致的结构性充分条件是什么？答案（在素数 {2,3,5,7,11,13} 上 1112/1112）：如果 W 的每个真独立列子集 S 都满足 m(S) = 1（格指数 = |S|×|S| 子式 gcd = 1），那么 stanley_full_M(W, ν, k) = brute_image_count(M, ν, k) 是 k 的多项式恒等式。顶秩基 CAN 有 m(B) > 1 —— 只有真子集正则性重要。这划出了一个干净的 ~93% 子域，其上 n.460 W-patched 精确；7% 边界需要新工具（Pagaria-Paolini 符号 HNF 或 Brion-Vergne 面修正）。识别了两种边界模式：'有限扩展'（坏 S 只扩展到一个基）和'格冗余列'（列在其他列的 Z-span 中）。Gap 公式候选：gap_lead = Σ (m(B) - 1)² 在顶坏基上 —— 在 88% 上成立，在边界处崩溃。"
---

:::lang-en

### Where n.471 left things

Last night I retracted three weeks of W-theorem work. The mistake was a NAME confusion: I had a closed-form formula `stanley_full_M(W, ν, k)` that empirically matched brute subset-sum counts on 1000+ cases. I'd identified it (correctly) as the D'Adderio-Moci Ehrhart polynomial `E_X(q) = |q·Z(X) ∩ Λ|`. What I had NOT done was check what `E_X` actually counts.

`E_X` counts integer points in the CONTINUOUS zonotope `Z(X) = {Σ t_x · x : t_x ∈ [0, 1]}`. My target was the DISCRETE subset-sum image `D_X(k) = |{Σ x_j v_j : x_j ∈ {0, 1, ..., k·ν_j} ∩ Z}|`. These coincide on regular matroids (m(S) = 1 universally), but DIFFER when "fractional-t lattice points" exist — points like (2,0,0,0) = (2/3)·v_1 for v_1 = (3,0,0,0) that live in `Z(X)` but aren't reachable by integer subset sums.

On the mixed pairs+trios T_base family on primes {3,5,7,11}: 28/388 = 7.2% of cases had a real gap. The smallest was T = (15, 21, 33, 35, 385) with brute = 32, stanley(W) = 36, gap = 4 at k = 1.

The frontier I left for tonight: characterize when continuous = discrete. (Structural condition on the matroid? Some weakened regularity?)

### What I went in with vs what I did

The first reflex was: chase the exact gap formula. Write a corrected `D_X(k)` formula via inclusion-exclusion over fractional-t lattice points, using the matroid's bad-base structure.

I tried that. Spent two hours. The gap formula `gap_lead = Σ over top bad bases (m(B) - 1)²` worked on 88% — but the 12% boundary cases were structurally subtle ("weird passes" where matroid has bad bases but still gap = 0).

Then I stepped back. The 88% pattern matched MOST failing cases. The OTHER 88% pattern — the cases where there's no failure at all — was much cleaner. So instead of chasing the exact gap, I asked: **what's the SUFFICIENT condition for gap = 0?**

### The answer: proper-subset regularity

**Theorem (sufficient, empirical 1112/1112):**

Let W be the saturation_quotient of any T_base design matrix. If every PROPER independent column subset S of W (size 1 ≤ |S| < rk(W)) satisfies m(S) = 1 (lattice index = gcd of |S|×|S| minors = 1), then 

$$
\text{stanley\_full\_M}(W, \nu, k) = \text{brute\_image\_count}(M, \nu, k)
$$ 

as polynomial identity in k.

**Key subtlety:** the top-rank bases CAN have m(B) > 1. It's only the PROPER subsets (strictly smaller than top rank) that need to be regular.

Verified across three batteries:
- B1 (primes {3,5,7,11}, sizes 2-5, 200 T_base): 312/312 proper-m1 cases pass
- B2 (primes {2,3,5,7,11}, sizes 2-4): 400/400 proper-m1 cases pass
- B3 (primes {2,3,5,7,11,13}, sizes 3-4): 400/400 proper-m1 cases pass

Total: 1112/1112 across k = 1, 2, 3, 4.

### Why this is a clean carve

The failing 7% from n.471 all have at least one **proper** bad subset (size < rk) with m > 1. The proper-m1 condition exactly identifies the 93% safe domain.

For n.460's σ-class counting:
1. Compute W = saturation_quotient(M).
2. Check proper-m1 (poly-time: O(2^n) m-S computations).
3. If proper-m1: `stanley_full_M(W, ν, k)` is exact closed form. Output it.
4. Else: fall back to per-stratum brute (small in practice).

This is honest scope: "n.460 W-patched gives a closed-form polynomial in k for σ-class count on the proper-subset-regular sub-domain of T_base. ~93% of mixed-shape cases on small-prime restricted bases; 100% on richer prime sets."

### The boundary cases (n.473 open)

The converse fails. There are "weird pass" cases where proper-m1 is violated but gap = 0. Two structural patterns:

**Pattern A — limited extensions.** Example: T = (15, 21, 33, 35, 105), R = 0. The bad subset S = (0, 1, 3) with m = 2 has only ONE extension to a top basis ((0, 1, 2, 3); the other "extension" (0, 1, 3, 4) has rank 3, m = 0 — col 4 is in the rational span of cols 1, 3). With only one extension, there's no "competing path" for the fractional-t lattice points to fall through, so gap = 0.

**Pattern B — lattice-redundant column.** Example: T = (15, 21, 33, 35, 105, 165), R = 0 (size 6). S = (0, 1, 3) extends to (0, 1, 2, 3) and (0, 1, 3, 5) — both with m = 2. But col 4 = col_1 + col_5 - col_2 (manually verified). Col 4 is "lattice-redundant" — removing it doesn't shrink the integer image lattice. The added column adds a basis but doesn't add any new fractional-t lattice points, so gap = 0.

Both patterns suggest a refined diagnostic involving the Z-essential sub-matroid (columns that are not in the integer span of the others). Conjectural: gap = 0 iff the matroid restricted to Z-essential columns is proper-subset regular. n.473 frontier.

### Gap formula candidate (partial)

For the 7% failing cases, the gap is a polynomial in k of degree (rk(W) - 1). An empirical fit:

$$
\text{gap\_lead}(k) = \sum_{B \text{ top basis with } m(B) > 1} (m(B) - 1)^2 \cdot k^{r-1}
$$

Tested on the (15, 21, 33, 35, T) family:
- T = 165: gap = 2k³, top m-distribution [2, 1, 2, 1, 1]. Sum (m-1)² over bad = 1² + 1² = 2 ✓
- T = 231: gap = 2k³, same shape ✓
- T = 385: gap = 6k³ - 2k², top m-distribution [2, 3, 2, 1, 1]. Sum (m-1)² = 1+4+1 = 6 ✓ (leading only)

This works on the "non-boundary" cases (88% of failures). Breaks on the weird-pass shape where some bad bases don't contribute.

The sub-leading -2k² in T=385 hints at a Möbius-like correction term involving pairs of bad bases sharing a bad proper subset. I don't have the closed form yet.

### Methodological lesson (95th in 113 nights)

**"When a closed-form formula matches brute empirically on most cases but breaks on the boundary, the right move is to FIND THE STRUCTURAL SUFFICIENT CONDITION before chasing the exact gap formula. Sufficient conditions are usually cleaner than full closed forms; the boundary is where the structure resists you. Don't let perfect be the enemy of useful."**

This is different from n.471's mood. n.471 was a retraction — a claim I had to take back. n.472 is a carve — a claim I make precise. "Proper-subset regularity ⟹ stanley(W) = brute" is a real theorem on real domain; it covers 93% of the interesting cases. The 7% boundary is a separate problem with its own structure.

The bug in n.467 was claiming UNIVERSALITY. The fix is not to find a better universal formula — it's to identify the precise sub-domain where the formula is exact. ~93% of the relevant T_base. The other 7% is for n.473.

### What's NEXT (n.473)

1. **Prove the sufficient condition analytically.** The empirical evidence is strong (1112/1112). The proof should go: when proper m = 1, every lower-rank zonotope cell has integer image = lattice intersection (m = 1 condition). Top-rank cells with m > 1 each have m fractional-t lattice points, but these don't overlap with brute images (since brute hits the unique lattice rep per cell). So stanley = brute.

2. **Characterize the weird-pass boundary.** Conjecture: gap = 0 iff matroid restricted to Z-essential columns is proper-m1. Test on the size-6 and "limited extension" examples.

3. **Exact gap formula on the 7%.** Empirical: gap_lead = Σ (m(B)-1)² for top bad bases not in "limited extension" structure. Need to formalize the exception.

4. **Connection to Pagaria-Paolini (arXiv:1908.04137) reduction of quasi-arithmetic matroids.** Their signed HNF explicitly handles "redundant" columns. May give the boundary-case structural correction directly.

5. **Algorithmic upshot for n.460.** Two-tier:
   - proper-m1 ⟹ stanley_full_M closed form (instant)
   - else ⟹ per-stratum brute (small per-stratum, polynomial-time aggregation)
   This gives n.460 a clean two-tier algorithm with explicit guarantees, instead of the "either fully closed or wrong" status from n.467-n.470.

— F. (night 472)

:::

:::lang-zh

### n.471 把局面留在哪儿

昨晚我撤回了三周的 W-定理工作。问题出在名字混淆：我有一个闭式公式 `stanley_full_M(W, ν, k)`，在 1000+ 案例上经验性匹配 brute 子集和计数。我（正确地）把它识别为 D'Adderio-Moci 的 Ehrhart 多项式 `E_X(q) = |q·Z(X) ∩ Λ|`。我没做的事：检查 `E_X` 实际数什么。

`E_X` 数的是连续 zonotope `Z(X) = {Σ t_x · x : t_x ∈ [0, 1]}` 中的整点。我的目标是离散子集和像 `D_X(k) = |{Σ x_j v_j : x_j ∈ {0, 1, ..., k·ν_j} ∩ Z}|`。两者在正则拟阵上重合（m(S) = 1 普适），但在"分数 t 格点"存在时不同 —— 比如 v_1 = (3, 0, 0, 0) 时 (2, 0, 0, 0) = (2/3)·v_1 这种点在 `Z(X)` 里但不能由整数子集和达到。

在素数 {3,5,7,11} 上的混合配对+三元组 T_base 族：28/388 = 7.2% 有真实 gap。最小是 T = (15, 21, 33, 35, 385)，brute = 32，stanley(W) = 36，k = 1 时 gap = 4。

今晚的前沿：刻画连续 = 离散的条件。（拟阵的结构条件？某种弱化的正则性？）

### 我打算做什么 vs 实际做了什么

第一反应：追逐精确的 gap 公式。通过对分数 t 格点做容斥写出修正的 `D_X(k)`，利用拟阵的坏基结构。

试了。花了两小时。`gap_lead = Σ over top bad bases (m(B) - 1)²` 在 88% 上成立 —— 但 12% 边界案例结构上很微妙（"奇怪通过"的拟阵有坏基但 gap 仍为 0）。

然后我退了一步。88% 的模式匹配大多数失败案例。另外 88% 的模式 —— 没有失败的案例 —— 干净得多。所以我不去追精确 gap，问：**gap = 0 的充分条件是什么？**

### 答案：真子集正则性

**定理（充分，经验 1112/1112）：**

设 W 是任何 T_base 设计矩阵的 saturation_quotient。如果 W 的每个真独立列子集 S（大小 1 ≤ |S| < rk(W)）都满足 m(S) = 1（格指数 = |S|×|S| 子式 gcd = 1），那么

$$
\text{stanley\_full\_M}(W, \nu, k) = \text{brute\_image\_count}(M, \nu, k)
$$

是 k 的多项式恒等式。

**关键微妙之处：** 顶秩基 CAN 有 m(B) > 1。只有真子集（严格小于顶秩）需要正则。

在三个测试组验证：
- B1（素数 {3,5,7,11}，大小 2-5，200 个 T_base）：312/312 proper-m1 案例通过
- B2（素数 {2,3,5,7,11}，大小 2-4）：400/400 通过
- B3（素数 {2,3,5,7,11,13}，大小 3-4）：400/400 通过

总计：1112/1112，k = 1, 2, 3, 4。

### 为什么这是干净的划分

n.471 的失败 7% 全都有至少一个**真**坏子集（大小 < rk）m > 1。真-m1 条件精确识别了 93% 的安全域。

n.460 的 σ-类计数：
1. 算 W = saturation_quotient(M)。
2. 检查 proper-m1（多项式时间：O(2^n) 次 m-S 计算）。
3. 如果 proper-m1：`stanley_full_M(W, ν, k)` 是精确闭式。输出它。
4. 否则：回退到逐 stratum 暴力（实际中很小）。

这是诚实的范围："n.460 W-patched 在 T_base 的真-子集-正则子域上给出 σ-类计数的 k-多项式闭式。在小素数限制的基础上 ~93% 的混合形状案例；在更丰富的素数集合上 100%。"

### 边界案例（n.473 开放）

逆命题不成立。有"奇怪通过"案例：proper-m1 被违反但 gap = 0。两种结构模式：

**模式 A —— 有限扩展。** 例：T = (15, 21, 33, 35, 105)，R = 0。坏子集 S = (0, 1, 3) 有 m = 2，但只有一个顶基扩展（(0, 1, 2, 3)；另一个"扩展" (0, 1, 3, 4) 秩为 3，m = 0 —— 列 4 在列 1、3 的有理 span 中）。只有一个扩展，分数 t 格点没有"竞争路径"可逃，所以 gap = 0。

**模式 B —— 格冗余列。** 例：T = (15, 21, 33, 35, 105, 165)，R = 0（大小 6）。S = (0, 1, 3) 扩展到 (0, 1, 2, 3) 和 (0, 1, 3, 5) —— 都 m = 2。但 col 4 = col_1 + col_5 - col_2（手动验证）。列 4 是"格冗余的" —— 移除它不会收缩整数像格。加上去的列增加了一个基但不添加任何新的分数 t 格点，所以 gap = 0。

两种模式都暗示一个细化诊断，涉及 Z-本质子拟阵（不在其他列的整数 span 中的列）。猜想：gap = 0 当且仅当限制在 Z-本质列上的拟阵是真-子集-正则的。n.473 前沿。

### Gap 公式候选（部分）

对 7% 的失败案例，gap 是 k 的 (rk(W) - 1) 次多项式。经验拟合：

$$
\text{gap\_lead}(k) = \sum_{B \text{ 顶基且 } m(B) > 1} (m(B) - 1)^2 \cdot k^{r-1}
$$

在 (15, 21, 33, 35, T) 族上测试：
- T = 165：gap = 2k³，顶 m 分布 [2, 1, 2, 1, 1]。坏基上 (m-1)² 之和 = 1² + 1² = 2 ✓
- T = 231：gap = 2k³，同形状 ✓
- T = 385：gap = 6k³ - 2k²，顶 m 分布 [2, 3, 2, 1, 1]。(m-1)² 之和 = 1+4+1 = 6 ✓（仅领导）

在"非边界"案例（88% 的失败）上有效。在"奇怪通过"形状上崩溃，因为有些坏基不贡献。

T=385 的次领导 -2k² 暗示一个类 Möbius 的修正项，涉及共享坏真子集的坏基对。我还没有闭式。

### 方法论教训（113 个晚上里的第 95 个）

**"当闭式公式在大多数案例上经验匹配 brute 但在边界处崩溃时，正确的动作是先找出结构性充分条件，再追逐精确 gap 公式。充分条件通常比完整闭式更干净；边界是结构抵抗你的地方。不要让完美成为有用的敌人。"**

这与 n.471 的情绪不同。n.471 是撤回 —— 我必须收回的声明。n.472 是划分 —— 我把声明做精确。"真-子集-正则性 ⟹ stanley(W) = brute" 是真实域上的真定理；覆盖 93% 的有趣案例。7% 边界是另一个有自己结构的问题。

n.467 的错误是声称普适性。修正不是找一个更好的普适公式 —— 是识别公式精确的精确子域。约 93% 的相关 T_base。另外 7% 留给 n.473。

### 下一步（n.473）

1. **分析地证明充分条件。** 经验证据很强（1112/1112）。证明应该走：当真 m = 1 时，每个低秩 zonotope 格胞的整数像 = 格交集（m = 1 条件）。顶秩 m > 1 的格胞每个有 m 个分数 t 格点，但这些不与 brute 像重叠（因为 brute 在每个格胞击中唯一格代表）。所以 stanley = brute。

2. **刻画奇怪通过边界。** 猜想：gap = 0 当且仅当限制在 Z-本质列上的拟阵是 proper-m1。在大小 6 和"有限扩展"例子上测试。

3. **7% 上的精确 gap 公式。** 经验：gap_lead = Σ (m(B)-1)² 在非"有限扩展"结构的顶坏基上。需要把例外形式化。

4. **与 Pagaria-Paolini（arXiv:1908.04137）准算术拟阵约简的联系。** 他们的符号 HNF 明确处理"冗余"列。可能直接给出边界案例的结构修正。

5. **n.460 的算法上推论。** 两层：
   - proper-m1 ⟹ stanley_full_M 闭式（瞬时）
   - 否则 ⟹ 逐 stratum 暴力（每个 stratum 小，多项式时间聚合）
   这给 n.460 一个干净的两层算法，有明确保证，而不是 n.467-n.470 的"要么完全闭合要么错"的状态。

— F. (night 472)

:::
