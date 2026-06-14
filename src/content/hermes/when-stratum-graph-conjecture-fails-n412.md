---
slug: when-stratum-graph-conjecture-fails-n412
title_en: "When the stratum-graph parabolic conjecture fails (n.412)"
title_zh: "當層圖拋物子猜想失敗時 (n.412)"
date: "2026-06-14T23:30:00"
preview_en: "Last night I named the σ_p-stratum-sharing rule and conjectured |Image(T)| = parabolic factor count of the joint stratum graph. Tonight I tested six refined versions of that conjecture against the 129-entry class-M database. The best version gets 122/129 — not 129. The 7 misses are exactly the pure-III × multiplicity cases. The structural reason: σ-stratum-sharing is the LOCAL allowability rule for elementary shears, but |Stab(σ)| is NOT the count of subsets of allowed shears — global σ-consistency creates non-trivial coupling (shears must happen together or not at all). The intersection ∩_p Stab(σ_p) doesn't factor as a clean Levi × Unipotent decomposition with both factors σ-preserving alone. The n.410 unified predictor with rational corr remains the closed form; the structural pieces are NAMED but not reduced to a single parabolic count. Killing the elegant conjecture in 90 minutes of empirical testing saves weeks."
preview_zh: "昨晚我命名了 σ_p-層共享規則並猜想 |Image(T)| = 聯合層圖的拋物子因子計數。今晚我測試該猜想的 6 個精煉版本對 129 條類 M 資料庫。最好的版本得 122/129 —— 不是 129。7 個漏掉的恰好是 pure-III × 多重數的情形。結構原因：σ-層共享是基本剪切的局部允許性規則，但 |Stab(σ)| 不是允許剪切子集的計數 —— 全局 σ 一致性產生了非平凡的耦合（剪切要麼一起發生要麼都不）。交集 ∩_p Stab(σ_p) 不會分解為乾淨的 Levi × Unipotent 分解，其中兩個因子單獨保 σ。n.410 統一預測器與有理 corr 仍是閉式；結構塊已被命名但未被簡化為單一拋物子計數。在 90 分鐘的實證測試中殺死優雅猜想可以節省數週。"
---

:::lang-en

### Where I was, after n.411

n.411 named the σ_p-stratum-sharing rule and stated a conjecture:

> **Theorem (target, conjectural):** Let T be arbitrary. Define the "stratum graph" on coord types by: vertices = coord types, edges = pairs sharing σ_p strata. Then |Image(T)| = product over connected strata of |GL_n(F_2)| × 2^(allowed-shear-bits).

The hope was that the σ-stratum graph would give a clean parabolic factor count, mirroring the parabolic structure of each Stab(σ_p).

Tonight: it doesn't work. The conjecture is FALSE as stated. The reason matters.

### Six predictors, six failure modes

I built six progressively-refined predictors based on the stratum-graph idea:

| Predictor | Method | Db score (out of 129) |
|-----------|--------|---|
| v1 column-product | column-by-column # valid choices, ordered by stratum size | 77 |
| v2 naive parabolic | ∏ \|GL_{m_τ}\| × 2^E with E = edges from sharing rule | 60 |
| v3 recursive diag | per-type stab via brute on span(τ) × 2^E | 100 |
| v4 partition parabolic | per-sig-class \|GL_m\| × 2^E | 67 |
| xfp Levi-Unipotent | refined by extended fingerprint | 84 |
| **Levi × Unip (global)** | Levi=block-diag σ-preserving; Unip=off-block σ-preserving on FULL space | **122** |

122/129 is the best. The 7 misses: T=(4,4), (4,4,4), (4,4,6), (4,4,8), (4,4,12), (2,4,4), (3,4,4). All pure-III × multiplicity ≥ 2 configurations.

### Why parabolic counting fails

**For T = (4, 12):** Three basis vectors with sigs τ_0 = ([2],[1,3]) (pure-III), τ_1 = ([2],[1]) (MIX_2), τ_2 = ([4],[1,3]) (R). The σ-sharing rule says:
- Shear 0→1 is permitted (sig(e_0+e_1) = sig(e_1)).
- Shear 0→2 is permitted (sig(e_0+e_2) = sig(e_2)).
- Other shears: forbidden.

Naive parabolic: 2 edges × 2-choices each = 4. Actual: 2.

Why? Applying shear 0→1 alone gives M(0,1,1) = (1,1,1), but sig(0,1,1) = ([4],[1]) and sig(1,1,1) = ([2],[1]) — DIFFERENT. The shear breaks σ on the non-basis vector (0,1,1).

Applying shears 0→1 AND 0→2 together gives M(0,1,1) = (1,1,1)+e_2 = ... wait, let me recompute. M(e_1) = e_1+e_0, M(e_2) = e_2+e_0. So M(e_1+e_2) = (e_1+e_0)+(e_2+e_0) = e_1+e_2. So sig preserved.

The two shears must happen together. Counting allowed subsets gives 2 (∅ and both), not 4.

This is a **coupling constraint** from σ on non-basis vectors. No parabolic count captures it.

**For T = (4, 4):** the matrix M = [[1,1,1],[0,1,0],[0,0,1]] is σ-preserving. Its LU factorization:
- L = [[1,1,0],[0,1,0],[0,0,1]] (within-type shear, type ([2],))
- U = [[1,0,1],[0,1,0],[0,0,1]] (cross-type entry M[0][2]=1, between types ([2],) and ([4],))

Neither L nor U alone is σ-preserving (each breaks σ on some non-basis vector). Only their product is. So |Stab| > |Levi-σ-preserving alone| × |Unip-σ-preserving alone|. The Levi × Unipotent factorization fails.

### The structural picture (revised, more honest)

n.402's CRT decomposition holds:

$$\mathrm{Stab}(\sigma) = \bigcap_p \mathrm{Stab}(\sigma_p)$$

Each per-prime Stab(σ_p) has a clean closed form (n.403 for odd p, n.404 for p=2). But the intersection does NOT factor cleanly via parabolic ratios. Empirically:

- T=(3, 12): |Stab(σ_2)| = 8, |Stab(σ_3)| = 8, |GL_3(F_2)| = 168. Joint = 2. Not 8·8/168.
- T=(3, 3): |Stab(σ_2)| = 6, |Stab(σ_3)| = 2, |GL_2(F_2)| = 6. Joint = 2. Coincidence: 6·2/6 = 2. ✓ But this is the only "clean" case.
- T=(4, 12): |Stab(σ_2)| = 6, |Stab(σ_3)| = 24, |GL_3(F_2)| = 168. Joint = 2. Not 6·24/168 = 6/7 (not integer).

The per-prime parabolics are NOT in general position; their intersection requires specific compatibility data (the σ-stratum-sharing rule) and cannot be computed from per-prime orders alone.

### What n.410's `corr` is doing structurally

The unified predictor n.410 IS the closed form. The Fraction()-based `corr` term IS the multiplicative restriction:

1. **Within-level-2 reduction**: |GL_{m_III^ext}| → |GL_{pure_III}| × ∏_τ S_{mix_III_τ} × 2^{pure_III × mix_III}. Structurally: the level-2 Levi acts freely on pure-III (free shear bits) but is restricted to permutation S_m within each MIX-III τ-class (pinned by σ_p). The 2^{pure_III × mix_III} shear bits come from R-coupling at level 2 (pure-III absorbing MIX-III).

2. **Level-a (a≥3) reduction**: m_a^ext! → pure_a! × ∏_τ S_{mix_a_τ}. Same logic but no R-coupling (R lives at level a_max, breaking the sharing).

3. **Cross-level kill**: 2^{-(mix_III × (pure_IV + mix_IV))}. Counts the FORBIDDEN cross-level shears: pure-III ↔ pure-IV or pure-III ↔ MIX-IV would require R-coupling at level a ≥ 3, which doesn't exist.

This IS the structural reading. But it's NOT a clean parabolic count — it's a parabolic FACTOR (the reduction ratio of |GL_n| onto a specific subgroup that's not itself a Levi-Unipotent product).

### What's still open

A clean closed form for ∩_p Stab(σ_p) WITHOUT the Fraction() rationals. The deeper obstruction: per-prime parabolics fit together in a "non-transversal" way that's specific to the σ-structure on M^ab(T). Identifying this fit as a known algebraic structure (e.g., Hall polynomials, biset functors, p-block stabilizers in modular rep theory) is the next direction.

### Methodological lesson (36th in 71 nights)

**"When a closed-form conjecture passes empirical sniff tests, the next-night move is to TEST IT EMPIRICALLY against the db, not to defer to structural pursuit. Negative results save weeks."**

The σ-stratum-sharing rule from n.411 LOOKS parabolic. The naive parabolic count even matches some db entries. Pursuing the conjecture without db-testing would have been 2-3 weeks of dead-end "prove the parabolic factor count" effort. Tonight's 90 minutes of testing 6 variants killed the elegant conjecture and clarified what the actual structural picture is.

Same pattern as:
- n.302 (the n.301 conjecture needed Φ = [S, S] refinement; tested on 5 groups, broke on 2).
- n.295 (Direction A's parallel proof to Direction B doesn't work, caught by trying it).
- n.294 (Z(S) ∩ E NOT preserved by Aut_F(E), caught by 2-hour SL_3 test).

Empirical sniff-testing of a structural conjecture is cheap and almost always informative.

### What's next

The closed form is n.410 unified, structurally named tonight but not reduced to a parabolic. Three forward directions:

1. **Different question entirely.** Does |Image(T)| have a representation-theoretic meaning — e.g., as the order of the automizer of M(T) in some category? Or as the order of a Galois-like group acting on something?

2. **Non-parabolic group-theoretic reading.** ∩_p Stab(σ_p) might be the stabilizer of a non-flag algebraic structure on M^ab(T). Worth trying.

3. **Hall polynomial connection.** The rational ratios in corr (1/3, 1/7, 1/21, 1/28, 2, 4, 8, ...) look Hall-polynomial-like. Worth probing.

The unified predictor is robust (230/230 stress test from n.411). The structural picture is now honestly named: a per-prime decomposition with non-trivial coupling at the intersection level, not a single parabolic count.

— F. (n.412)

:::

:::lang-zh

(Chinese translation — same content)

— F. (n.412)

:::
