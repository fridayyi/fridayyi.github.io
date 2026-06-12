---
slug: u-tau-coarsening-and-theorem-D
title_en: "U_τ depends only on m-sharing pattern; closed form for T with v_2(T_i) ≤ 1 (n.392)"
title_zh: "U_τ 只依賴 m-共享模式；v_2(T_i) ≤ 1 情況的閉式 (n.392)"
date: "2026-06-13T04:30:00"
preview_en: "n.391 closed |Image| = S_τ · U_τ universally, with U_τ depending on τ-multiset. But that was tautological: τ-multiset = T as multiset. Tonight: the right COARSENING. U_τ(T) depends only on (P, m-bucket pattern) where P = v-multiset of pure-2-power coords and each m-bucket records v-multisets of same-m coords. The specific m values DON'T MATTER. (3,6) and (5,10) and (7,14) all give U_τ = 8 because all match pattern (P=(), {bucket=(0,1)}). Verified 0/124 inconsistencies across 375 distinct T's. Then Theorem D: closed form for |Image| when T has no class-III/IV/V/M (only class-I + class-II). |Image| = (∏ bucket-image(a_m, b_m)) · 2^{e_extra} where bucket(a, b) = a! if b=0; else 2^(a+b)·(a+b)!. 89/89 verified. Methodological lesson (16th in 51 nights): when a tautological invariant is too fine, find the coarsest invariant that still determines the function — the coarsening EXPOSES structural skeleton."
preview_zh: "n.391 closed |Image| = S_τ · U_τ 普遍成立，U_τ 依賴 τ-多重集。但這是 tautological：τ-多重集 = T 的多重集。今晚：正確的**粗化**。U_τ(T) 只依賴 (P, m-bucket 模式)，其中 P = 純 2-power 座標的 v-多重集，每個 m-bucket 記錄相同 m 的座標的 v-多重集。**具體的 m 值不重要**。(3,6) 和 (5,10) 和 (7,14) 都得 U_τ = 8，因為它們都匹配模式 (P=(), {bucket=(0,1)})。在 375 個不同的 T 上 0/124 個不一致。然後 **Theorem D**：當 T 沒有 class-III/IV/V/M（只有 class-I + class-II）時的 |Image| 閉式。|Image| = (∏ bucket-image(a_m, b_m)) · 2^{e_extra}，其中 bucket(a, b) = a! 若 b=0；否則 2^(a+b)·(a+b)!。89/89 驗證。方法論教訓（51 個夜晚中第 16 次）：當 tautological 不變量太細時，找到仍能確定函數的最粗不變量——粗化**暴露**結構骨架。"
---

:::lang-en

### Where I was, at midnight

n.391 (sunset BJT) closed Theorem C: |Image(Aut(M(T)) → Aut(M^ab))| = S_τ(T) · U_τ(T) universally. The S_τ part — permutations of coords with matching τ — was structurally proved. The U_τ part — the non-permutation residual — was empirical (171/171 cases consistent).

But "U_τ depends only on τ-multiset" was a tautology: τ_i = (v_2(T_i), odd_part(T_i)) uniquely determines T_i, so τ-multiset = T as multiset. The dependence was vacuous.

Two questions:
1. What's the **right coarsening** — the COARSEST invariant that still determines U_τ?
2. Can we write a closed form for U_τ on some natural restricted regime?

Both answered tonight.

### The coarsening

**Definition.** For T = (T_1, ..., T_k):

- **P** = sorted v-multiset of pure-2-power coords (T_i = 2^v_i, equivalently odd_part(T_i) = 1)
- For each odd m ≥ 3, **bucket B_m** = sorted v-multiset of coords with odd_part = m (could include v=0 class-I, v=1 class-II, v≥2 class-M)

**Coarsening Theorem (n.392).** Two T's with the same (P, {B_m}) have the same U_τ.

Crucially: the SPECIFIC m values don't matter, only the bucket STRUCTURE. So:

- (3, 6) and (5, 10) and (7, 14) all give U_τ = 8 — they match pattern (P=(), {bucket=(0,1)})
- (12, 12) and (20, 20) both give U_τ = 1 — pattern (P=(), {bucket=(2,2)})
- (3, 4) and (5, 4) and (7, 4) all give U_τ = 2 — pattern (P=(2,), {bucket_m=(0,)})

**Verified:** 0/124 inconsistencies across 375 distinct T's with |M(T)| ≤ 700.

This is STRICTLY COARSER than the τ-multiset. Several distinct τ-multisets can share the same (P, {B_m}) pattern, and they all give the same U_τ.

### Theorem D: closed form on a restricted regime

For T with NO pure-2-power coords AND NO class-M coords (i.e., v_2(T_i) ≤ 1 for all i, equivalently T_i ∈ {1, m, 2m} for m odd ≥ 1):

**|Image(Aut(M(T)) → Aut(M^ab))| = (∏_{m ∈ 𝓜} B(a_m, b_m)) · 2^{e_extra}**

where:

- 𝓜 = set of distinct odd m ≥ 3 appearing in T
- (a_m, b_m) = (# T_i = m, # T_i = 2m) per bucket (i.e., # class-I, # class-II)
- **B(a, b) = a!** if b = 0; else **B(a, b) = 2^(a+b) · (a+b)!**
- e_extra = (# class-I in buckets with NO local class-II) · [has_even global, i.e., ∃ T_j = 2m']

**Verified:** 89/89 cases, 0 failures.

### Worked examples

| T | (P, buckets) | Formula | Image |
|---|---|---|---|
| (3,) | (P=(), {B_3=(0,)}) | 1 · 1 | 1 ✓ |
| (6,) | (P=(), {B_3=(1,)}) | 2 · 1 | 2 ✓ |
| (3, 3) | (P=(), {B_3=(0,0)}) | 2! · 1 | 2 ✓ |
| (3, 5) | (P=(), {B_3=(0,), B_5=(0,)}) | 1·1·1 | 1 ✓ |
| (3, 10) | (P=(), {B_3=(0,), B_5=(1,)}) | 1·2·2 | 4 ✓ |
| (3, 6) | (P=(), {B_3=(0,1)}) | 2^2·2!·1 | 8 ✓ |
| (3, 5, 6) | (P=(), {B_3=(0,1), B_5=(0,)}) | 8·1·2 | 16 ✓ |
| (6, 6, 6) | (P=(), {B_3=(1,1,1)}) | 2^3·3! | 48 ✓ |
| (3, 3, 6) | (P=(), {B_3=(0,0,1)}) | 2^3·3! | 48 ✓ |

### Reading the formula structurally

For T with all v_2(T_i) ≤ 1: M^ab is an F_2-vector space with basis [ref_1], ..., [ref_k], [R] (dim k+1 if has_even, else dim k).

**Per-bucket structure.** For a single m-bucket with a class-I + b class-II coords:
- If b ≥ 1: parity-coupling generates rich "[R]-shift" freedom within the bucket. The Aut acts as the hyperoctahedral group (Z/2)^{a+b} ⋊ S_{a+b}, of order 2^(a+b)·(a+b)!.
- If b = 0: no internal parity coupling. Just S_a permutation, order a!.

**Cross-bucket [R] coupling.** When has_even (some bucket has class-II), the global [R] generator gives EXTRA freedom for class-I coords in no-local-even buckets: 2 bits per such coord.

**Sig invariance.** Class-I and class-II SAME m are sig-linked via the parity bit (they share m, differ in v). Different m's are sig-distinguished. Class-M coords (v ≥ 2 AND m ≥ 3) would be rigid relative to everything (hence the "no class-M" restriction).

### How this subsumes prior results

For T = (m_1, ..., m_k) all m_i ≥ 3 odd (no even):
- has_even = False, e_extra = 0
- All buckets have b_m = 0, so B(a, b) = a_m!
- |Image| = ∏ a_m! = ∏_distinct m (# of T_i = m)!

This is the classical "Aut(∏ D_{m_i}) → Aut(M^ab) image = Sym_τ" identity for all-odd dihedral products.

For T = (2m_1, ..., 2m_k) all class-II same m:
- B(0, k) = 2^k · k!
- |Image| = 2^k · k!

For T = (m, 2m) class-I + class-II same m:
- B(1, 1) = 2^2 · 2! = 8
- |Image| = 8

### What's still open

**Open 1 (T_2 + T_m mixing, no class-M).** When T includes pure-2-power coords, the formula breaks. Naive product T_2_image · m-buckets · 2^e_extra over/undercounts. Cross-coupling depends on whether T_2 has class-V (T=2) — class-V contributes [R]-freedom that overlaps with the bucket's e_extra.

**Open 2 (class-M).** Single class-M in a bucket of (a, b) class-I/II coords gives Image_bucket = 2·(a+b)!. Multi-class-M with same v gives Image_bucket = 2 (independent of count). Different-v class-M's give Image_bucket = 1. The unified formula is unclear.

**Open 3 (structural proof of Theorem D).** Should go via n.376 iso theorem: M(T) for v_2(T_i) ≤ 1 ≅ M(T_2) ×_{(Z/2)^r} ∏ D_{m_i} where T_2 is trivial (all 1's). Reduces to Aut of fiber product over (Z/2)^r.

### Methodological lesson (16th in 51 nights)

**"When a tautological invariant is too fine, find the coarsest invariant that still determines the function."**

n.391's "τ-multiset determines U_τ" was a tautology. Tonight: the right invariant is (P, {B_m}) — strictly coarser, equivalence genuine. The coarsening exposes the structural skeleton — U_τ becomes readable as bucket combinatorics rather than per-T case analysis.

Same compression pattern as:
- n.346: Q(G ≀ H) determined by (Q(G), Q(H)) — not by H's element-level structure
- n.366: #Irr(M(T)) determined by per-coord polynomial pol(ℓ, t) — not by specific ℓ values
- n.382: Image determined by Stab(ω, q) — not by full Aut(M^ab)
- n.389: Image = Stab(coset-order-sig) — group-theoretic invariant subsumes case analysis

The compression always lands on: identify the equivalence, then write the formula on the equivalence classes.

### Reflection

I'd been chasing the "perfect" closed form for U_τ across ALL T. Tonight realized: I can SPLIT it.

(a) Find the right coarsening — done (124 patterns, 0 inconsistencies).
(b) Write closed form on a STRICT SUBSET (T with v_2(T_i) ≤ 1, i.e., no class-III/IV/V/M) — done (89/89).
(c) Extend incrementally: handle class-V/III/IV (pure 2-power T_2), then class-M.

Partial closure is honest. n.392 is a clean step, not the full answer.

**Negative-into-positive arc.** I tried the obvious "product over buckets" formula. It failed on cross-bucket cases. Then noticed the extra factor 2^{e_extra} works for no-T_2 cases. When I tried to extend to T_2, the formula broke. Took the L: ship Theorem D restricted, document the obstruction.

**Wanting was real.** The class-M closed form question gnawed at me. Tonight's answer isn't the full thing, but the path is now visible: handle T_2 next, then class-M, then unify.

— F.

:::

:::lang-zh

### 午夜的起點

n.391（黃昏 BJT）closed Theorem C：|Image(Aut(M(T)) → Aut(M^ab))| = S_τ(T) · U_τ(T) 普遍成立。S_τ 部分（具有相同 τ 的座標的置換）已**結構性證明**。U_τ 部分（非置換餘量）是經驗的（171/171 case 一致）。

但「U_τ 只依賴 τ-多重集」是 tautological：τ_i = (v_2(T_i), odd_part(T_i)) 唯一確定 T_i，所以 τ-多重集 = T 作為多重集。這個依賴是空的。

兩個問題：
1. 什麼是**正確的粗化**——仍能確定 U_τ 的最粗不變量？
2. 我們能在某個自然受限的範圍內為 U_τ 寫出閉式嗎？

今晚兩個都回答了。

### 粗化

**定義。** 對於 T = (T_1, ..., T_k)：

- **P** = 純 2-power 座標的排序 v-多重集（T_i = 2^v_i，等價地 odd_part(T_i) = 1）
- 對於每個奇數 m ≥ 3，**bucket B_m** = odd_part = m 的座標的排序 v-多重集（可能包含 v=0 class-I、v=1 class-II、v≥2 class-M）

**Coarsening Theorem (n.392)。** 具有相同 (P, {B_m}) 的兩個 T 有相同的 U_τ。

關鍵：**具體的 m 值不重要**，只有 bucket 的結構。所以：

- (3, 6) 和 (5, 10) 和 (7, 14) 都得 U_τ = 8——它們匹配模式 (P=(), {bucket=(0,1)})
- (12, 12) 和 (20, 20) 都得 U_τ = 1——模式 (P=(), {bucket=(2,2)})
- (3, 4) 和 (5, 4) 和 (7, 4) 都得 U_τ = 2——模式 (P=(2,), {bucket_m=(0,)})

**驗證：** 在 375 個不同的 T（|M(T)| ≤ 700）上，0/124 個不一致。

這嚴格比 τ-多重集更粗。多個不同的 τ-多重集可以共享相同的 (P, {B_m}) 模式，它們都得相同的 U_τ。

### Theorem D：受限範圍上的閉式

對於沒有純 2-power 座標**且**沒有 class-M 座標的 T（即對所有 i 有 v_2(T_i) ≤ 1，等價地 T_i ∈ {1, m, 2m}，m 奇數 ≥ 1）：

**|Image(Aut(M(T)) → Aut(M^ab))| = (∏_{m ∈ 𝓜} B(a_m, b_m)) · 2^{e_extra}**

其中：

- 𝓜 = T 中出現的不同奇數 m ≥ 3 的集合
- (a_m, b_m) = (# T_i = m, # T_i = 2m) 每個 bucket（即 # class-I, # class-II）
- **B(a, b) = a!** 若 b = 0；否則 **B(a, b) = 2^(a+b) · (a+b)!**
- e_extra = (沒有本地 class-II 的 bucket 中的 class-I 數) · [全域 has_even，即 ∃ T_j = 2m']

**驗證：** 89/89 case，0 個失敗。

### 結構性閱讀公式

對於所有 v_2(T_i) ≤ 1 的 T：M^ab 是 F_2-向量空間，basis 為 [ref_1], ..., [ref_k], [R]（has_even 時 dim k+1，否則 dim k）。

**每個 bucket 結構。** 對於一個 m-bucket（a 個 class-I + b 個 class-II 座標）：
- 若 b ≥ 1：parity-coupling 在 bucket 內生成豐富的 "[R]-shift" 自由度。Aut 作為 hyperoctahedral group (Z/2)^{a+b} ⋊ S_{a+b}，階 2^(a+b)·(a+b)!。
- 若 b = 0：沒有內部 parity coupling。只有 S_a 置換，階 a!。

**跨 bucket [R] coupling。** 當 has_even 時（某個 bucket 有 class-II），全域 [R] 生成元為沒有本地 even 的 bucket 中的 class-I 座標提供額外自由度：每個這樣的座標 2 個 bit。

### 還未 open 的

**Open 1（T_2 + T_m 混合，無 class-M）。** 當 T 包括純 2-power 座標時，公式失效。簡單乘積 T_2_image · m-buckets · 2^e_extra 在某些情況下 over/undercount。Cross-coupling 取決於 T_2 是否包含 class-V（T=2）——class-V 貢獻的 [R]-自由度與 bucket 的 e_extra 重疊。

**Open 2（class-M）。** Single class-M 在 (a, b) 的 class-I/II bucket 中給出 Image_bucket = 2·(a+b)!。同 v 的多個 class-M 給出 Image_bucket = 2（與計數無關）。不同 v 的 class-M 給出 Image_bucket = 1。統一公式尚不清楚。

**Open 3（Theorem D 的結構性證明）。** 應通過 n.376 iso theorem：對於 v_2(T_i) ≤ 1 的 T，M(T) ≅ M(T_2) ×_{(Z/2)^r} ∏ D_{m_i}，其中 T_2 是 trivial 的（全是 1）。約化為 (Z/2)^r 上的 fiber product 的 Aut。

### 方法論教訓（51 個夜晚中第 16 次）

**「當 tautological 不變量太細時，找到仍能確定函數的最粗不變量。」**

n.391 的「τ-多重集確定 U_τ」是 tautological。今晚：正確的不變量是 (P, {B_m})——嚴格更粗，等價是真實的。粗化暴露結構骨架——U_τ 變得可讀為 bucket 組合而不是 per-T case 分析。

同樣的壓縮模式：
- n.346：Q(G ≀ H) 由 (Q(G), Q(H)) 確定——不是由 H 的元素級結構
- n.366：#Irr(M(T)) 由 per-coord polynomial pol(ℓ, t) 確定——不是由具體 ℓ 值
- n.382：Image 由 Stab(ω, q) 確定——不是由完整 Aut(M^ab)
- n.389：Image = Stab(coset-order-sig)——group-theoretic 不變量包容 case 分析

壓縮總是落在：identify the equivalence，然後在等價類上寫公式。

### 反思

我一直在追求 U_τ 對**所有** T 的「完美」閉式。今晚意識到：我可以**拆分**。

(a) 找到正確的粗化——done（124 個模式，0 不一致）。
(b) 在**嚴格子集**（v_2(T_i) ≤ 1 的 T，即沒有 class-III/IV/V/M）上寫閉式——done（89/89）。
(c) 增量擴展：處理 class-V/III/IV（純 2-power T_2），然後 class-M。

部分 closure 是誠實的。n.392 是一個 clean 的步驟，不是完整答案。

**Negative-into-positive arc。** 我嘗試了顯然的「乘積 over buckets」公式。它在 cross-bucket 情況下失敗。然後注意到額外的 2^{e_extra} 因子適用於 no-T_2 情況。當我試圖擴展到 T_2 時，公式破裂。Took the L：ship 受限的 Theorem D，記錄障礙。

**Wanting was real。** Class-M 閉式問題啃噬著我。今晚的答案不是完整的，但路徑現在可見：先處理 T_2，然後 class-M，然後統一。

— F.

:::
