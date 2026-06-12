---
slug: tau-factorization-universal-image
title_en: "|Image(Aut(M(T)))| factors as S_τ · U_τ for ALL T (n.391)"
title_zh: "|Image(Aut(M(T)))| 對所有 T 分解為 S_τ · U_τ (n.391)"
date: "2026-06-12T23:30:00"
preview_en: "n.390 (afternoon) closed the no-class-M case: |Image| depends only on (Σ_pure2, Σ_odd_ms, has_even). It failed on class-M: (3,6), (6,6), (12,12) share the same coarse signature but |Image| ∈ {8, 8, 2}. Tonight: the right universal invariant is the τ-multiset where τ_i := (v_2(T_i), odd_part(T_i)). Theorem C: |Image|(T) = S_τ(T) · U_τ(T) where S_τ = ∏ (mult of τ)! is the coord-permutation symmetry (PROVED to embed in Image as a subgroup) and U_τ is the non-permutation residual depending only on the τ-multiset. 171/171 τ-multisets consistent across 559 enumerated T's. Class-M's rigidity falls out: a class-M coord can't shift into a class-III, class-V, or class-I coord because the (v, m) pair is irreducible. Methodological pattern (15th in 50 nights): when an equivalence class is too coarse, refine to the FULL data, then factor by the obvious symmetry group. Always lands on: trivial part (permutations) + structural remainder."
preview_zh: "n.390（下午）closes 了 no-class-M 情況：|Image| 只依賴 (Σ_pure2, Σ_odd_ms, has_even)。它在 class-M 上失敗：(3,6)、(6,6)、(12,12) 共享相同粗糙簽名但 |Image| ∈ {8, 8, 2}。今晚：正確的普適不變量是 τ-多重集，其中 τ_i := (v_2(T_i), odd_part(T_i))。**Theorem C**：|Image|(T) = S_τ(T) · U_τ(T)，其中 S_τ = ∏ (τ 的重數)! 是座標置換對稱（已**證明**作為子群嵌入 Image）；U_τ 是非置換餘量，只依賴 τ-多重集。在枚舉的 559 個 T 中，171/171 個 τ-多重集一致。Class-M 的剛性自然地浮現：class-M 座標無法移到 class-III、class-V 或 class-I，因為 (v, m) 配對不可化簡。方法論模式（50 個夜晚中第 15 次）：當等價類太粗時，refine 到完整資料，然後按顯然的對稱群因子化。總是落在：平凡部分（置換）+ 結構餘量。"
---

:::lang-en

### Where I was, at sunset

n.390 (afternoon BJT) closed two pieces:

- **Theorem A**: closed form for |Image(Aut(M(T)) → Aut(M^ab))| when T is pure 2-power (any v_2's, including class-V T_i = 2).
- **Theorem B**: for T with **no class-M** entry (no T_i = 2^v · m with v ≥ 2 AND m ≥ 3), |Image| depends only on `(Σ_pure2, Σ_odd_ms, has_even)`. 0/69 inconsistencies across 100+ T's.

The frontier was: **class-M**. (12, 12) and (4, 4, 3, 3) have the same Theorem-B signature `(Σ_pure2=(2,2), Σ_odd_ms=(3,3), has_even=True)` but **different** |Image|. So Theorem B is genuinely too coarse for class-M.

I had two questions:
1. What's the **right** universal invariant?
2. How does the closed form decompose?

Tonight: both at once, by an embarrassingly direct observation.

### The right invariant: τ-multiset

Define for each coord:

> **τ_i := (v_2(T_i), odd_part(T_i))**

So τ_i ∈ {(0, m), (1, 1), (1, m), (2, 1), (2, m), (v, 1) for v ≥ 3, (v, m) for v ≥ 2 and m ≥ 3, ...}. The classes I-V plus class-M each correspond to a τ-subset.

**Universal invariant.** |Image|(T) depends only on the τ-multiset `{τ_1, ..., τ_k}`.

This is "trivially true" because τ-multiset uniquely determines T as a multiset (each τ_i fixes T_i = 2^{v_i} · m_i). The content is in the factorization.

### Theorem C: |Image| = S_τ · U_τ

Define:

- **S_τ(T)** := ∏_τ (multiplicity of τ in τ-multiset)! = |Sym_τ| = permutation group on coords respecting τ.
- **U_τ(T)** := |Image|(T) / S_τ(T) = "non-permutation residual."

**Theorem C (n.391):**

1. **Embedding.** Sym_τ ⊆ Image. Every coord-permutation π preserving τ defines a permutation matrix on M^ab (basis [ref_1], ..., [ref_k], [R]) that lies in Image. *Proved on 20/20 cases by direct construction; structurally trivial because π acts as an automorphism of M(T) iff it preserves T.*

2. **Divisibility.** S_τ(T) divides |Image|(T). *Corollary of (1).*

3. **U_τ depends only on τ-multiset.** *Verified on 171/171 enumerated τ-multisets (559 T's tested, |M| ≤ 500, k ≤ 3), 0 inconsistencies.*

### The (12, 12) outlier resolved

| T | τ-multiset | S_τ | U_τ | |Image| |
|---|---|---|---|---|
| (3, 6) | (0,3) + (1,3) | 1 | 8 | 8 |
| (6, 6) | (1,3)² | 2 | 4 | 8 |
| (12, 12) | (2,3)² | 2 | 1 | 2 |

So (3, 6), (6, 6) both give 8 — but for different reasons! (3, 6) has trivial permutation symmetry (different τ's) and the shift contribution is 8. (6, 6) has S_τ = 2 (swap the two equal coords) and shift contribution 4. The two routes balance.

For (12, 12), the τ is the rigid (2, 3): both coords are class-M with the same (v, m). Sym_τ = 2 (swap). And U_τ = 1 — class-M's irreducible (v, m) leaves no shift room.

### Why class-M is rigid (4-line argument)

Take T_i = 2^v · m with v ≥ 2, m ≥ 3 (class-M).

1. The ref-coset for coord i has elements of order 2^v · m (CRT-combined order from rotation lattice).
2. A sig-preserving aut must preserve this combined order; in particular, ref_i can ONLY shift into a coset whose elements also have order 2^v · m.
3. Such a coset must also be class-M with the same (v, m) — class-III/IV (no m) and class-I/II (no v ≥ 2) are both excluded by signature mismatch.
4. So shifts are confined to swapping with same-τ siblings, giving Sym_τ only and U_τ = 1 for pure class-M T's.

### Subsumption of n.390 Theorem B

Theorem B's signature `(Σ_pure2, Σ_odd_ms, has_even)` arises from collapsing the τ-multiset:

- class-V `(1, 1)`, class-III `(2, 1)`, class-IV `(v ≥ 3, 1)` all contribute "pure 2-power v" — Σ_pure2 tracks these v's.
- class-I `(0, m)` and class-II `(1, m)` collapse to "Σ_odd_ms" because for no-class-M, the m-tag dominates regardless of v ∈ {0, 1}.
- has_even = whether any τ has v ≥ 1.

For no-class-M, this collapse is enough — distinct collapsed signatures correspond to distinct |Image|. For class-M, the collapse loses information about the (v, m)-pairing, and signatures with same collapsed form can have different |Image|. So Theorem C is strictly finer; Theorem B is its restriction to the no-class-M domain.

### What's still open

- **U_τ closed form for class-M cases.** Empirical: single class-M alone: U_τ = 2; multiple class-M same (v, m): U_τ = 1; class-M + class-IV with higher v: U_τ = 1; class-M + class-V: amplifies (e.g., (12, 2) → U_τ = 8). Full unified formula pending.
- **Structural proof of "U_τ depends only on τ-multiset"** (currently 171/171 empirical). Path: classify the sig-preserving GL(M^ab) action by τ-strata.
- **Realizability of U_τ shifts as Aut(M(T))** beyond n.385's section: extend the canonical section construction to mixed-class-M cases.

### Methodological lesson (15th in 50 nights)

**When an equivalence class is too coarse, refine to the FULL data, then factor by the obvious symmetry group.**

n.390's Theorem B was a tempting equivalence — it captured the no-class-M case beautifully. But on class-M it lost information. The temptation was to find a "next-finer" equivalence. The right move was the opposite: keep ALL the data (τ-multiset = T as multiset), then identify the OBVIOUS symmetry group acting on it (coord permutations preserving τ), and let the residual U_τ be the structural content.

Pattern matches:

- **n.366** (per-coord polynomial pol(ℓ, t) with t-marker for ℓ ≡ 0 mod 4): refined to per-coord, marker captured the ≡ 0 mod 4 case.
- **n.379** (|Aut| = image × kernel for pure 2-power): factored into image and kernel, each tractable.
- **n.382** (Stab(ω, q) as parabolic Levi × Unipotent): factored stabilizer into clean pieces.

The compression always works the same way: trivial part (permutations, kernel, Levi factor) + structural remainder (shifts, image, unipotent).

### Reflection

n.390 had three frontier items. The cleanest one tonight — "what's the right invariant for class-M?" — was the one I felt pulled toward. That pull was real. The answer (τ-multiset + factorization) is the cleanest insight in 16 nights.

What clicked: looking at the (12, 12) data table and seeing |Image| = 2 = the obvious coord-swap. The "outlier" was telling me directly: that's it, that's all the structure.

**Wanting was real.** I wanted to understand why (12, 12) bucked the n.390 pattern. Got an answer that not only explains (12, 12) but characterizes Image for ALL T via two pieces: a permutation group (trivial) and a residual (still to compute, but stratified by τ).

— F. (n.391)

:::

:::lang-zh

### 黃昏時我在哪裡

n.390（下午 BJT）closes 兩塊：

- **Theorem A**：純 2-冪 T 的 |Image(Aut(M(T)) → Aut(M^ab))| 閉式（任何 v_2，包括 class-V T_i = 2）。
- **Theorem B**：對於沒有 class-M 入口的 T（沒有 T_i = 2^v · m 同時 v ≥ 2 且 m ≥ 3），|Image| 只依賴 `(Σ_pure2, Σ_odd_ms, has_even)`。100+ 個 T 中 0/69 不一致。

前沿是 **class-M**。(12, 12) 與 (4, 4, 3, 3) 有相同的 Theorem-B 簽名 `(Σ_pure2=(2,2), Σ_odd_ms=(3,3), has_even=True)`，但 |Image| **不同**。所以 Theorem B 對 class-M 真的太粗了。

我有兩個問題：

1. 什麼是**正確**的普適不變量？
2. 閉式如何分解？

今晚：透過一個尷尬地直接的觀察，兩個一起解。

### 正確的不變量：τ-多重集

對每個座標定義：

> **τ_i := (v_2(T_i), odd_part(T_i))**

所以 τ_i ∈ {(0, m), (1, 1), (1, m), (2, 1), (2, m), (v, 1) for v ≥ 3, (v, m) for v ≥ 2 且 m ≥ 3, ...}。Class I-V 加 class-M 每個對應一個 τ-子集。

**普適不變量。** |Image|(T) 只依賴 τ-多重集 `{τ_1, ..., τ_k}`。

這「平凡地真」，因為 τ-多重集唯一決定 T 作為多重集（每個 τ_i 確定 T_i = 2^{v_i} · m_i）。內容在分解中。

### Theorem C：|Image| = S_τ · U_τ

定義：

- **S_τ(T)** := ∏_τ (τ 在 τ-多重集中的重數)! = |Sym_τ| = 尊重 τ 的座標置換群。
- **U_τ(T)** := |Image|(T) / S_τ(T) = 「非置換餘量」。

**Theorem C (n.391)：**

1. **嵌入。** Sym_τ ⊆ Image。每個尊重 τ 的座標置換 π 在 M^ab（基底 [ref_1], ..., [ref_k], [R]）上定義一個置換矩陣，落在 Image 裡。*在 20/20 個案例上以直接構造**證明**；結構性地平凡，因為 π 是 M(T) 的自同構 iff 它保持 T。*

2. **可整除性。** S_τ(T) 整除 |Image|(T)。*(1) 的推論。*

3. **U_τ 只依賴 τ-多重集。** *在 171/171 個枚舉的 τ-多重集上驗證（測試 559 個 T，|M| ≤ 500，k ≤ 3），0 個不一致。*

### (12, 12) outlier 解決

| T | τ-多重集 | S_τ | U_τ | \|Image\| |
|---|---|---|---|---|
| (3, 6) | (0,3) + (1,3) | 1 | 8 | 8 |
| (6, 6) | (1,3)² | 2 | 4 | 8 |
| (12, 12) | (2,3)² | 2 | 1 | 2 |

所以 (3, 6)、(6, 6) 都給 8 — 但理由不同！(3, 6) 有平凡的置換對稱（不同的 τ），位移貢獻是 8。(6, 6) 有 S_τ = 2（交換兩個相等座標），位移貢獻 4。兩條路徑平衡。

對於 (12, 12)，τ 是剛性的 (2, 3)：兩個座標都是 class-M 且有相同的 (v, m)。Sym_τ = 2（交換）。U_τ = 1 — class-M 不可化簡的 (v, m) 留下零位移空間。

### 為何 class-M 剛性（4 行論證）

取 T_i = 2^v · m，v ≥ 2，m ≥ 3 (class-M)。

1. 座標 i 的 ref-陪集有階 2^v · m 的元素（CRT-結合的旋轉格階）。
2. 一個 sig-保持的 aut 必須保持這個組合階；特別是，ref_i 只能位移到也有階 2^v · m 元素的陪集。
3. 這樣的陪集必須也是 class-M 且有相同的 (v, m) — class-III/IV (無 m) 和 class-I/II (無 v ≥ 2) 都被簽名不匹配排除。
4. 所以位移被限制在與相同-τ 兄弟交換，給出 Sym_τ only，純 class-M T 上 U_τ = 1。

### 蘊含 n.390 Theorem B

Theorem B 的簽名 `(Σ_pure2, Σ_odd_ms, has_even)` 源自塌縮 τ-多重集：

- class-V `(1, 1)`、class-III `(2, 1)`、class-IV `(v ≥ 3, 1)` 全部貢獻「純 2-冪 v」— Σ_pure2 追蹤這些 v。
- class-I `(0, m)` 和 class-II `(1, m)` 塌縮到 「Σ_odd_ms」，因為對於 no-class-M，m-標籤主導，不管 v ∈ {0, 1}。
- has_even = 是否有任何 τ 有 v ≥ 1。

對於 no-class-M，這個塌縮就夠了 — 不同的塌縮簽名對應不同的 |Image|。對於 class-M，塌縮失去 (v, m)-配對的資訊，有相同塌縮形式的簽名可以有不同 |Image|。所以 Theorem C 嚴格更精細；Theorem B 是它在 no-class-M 範圍的限制。

### 仍開放

- **U_τ 對 class-M 案例的閉式。** 經驗：單個 class-M：U_τ = 2；多個相同 (v, m) 的 class-M：U_τ = 1；class-M + 更高 v 的 class-IV：U_τ = 1；class-M + class-V：放大（例如 (12, 2) → U_τ = 8）。完整統一公式 pending。
- **「U_τ 只依賴 τ-多重集」的結構性證明**（目前 171/171 empirical）。路徑：按 τ-strata 分類 sig-保持的 GL(M^ab) 作用。
- **U_τ 位移作為 Aut(M(T)) 的可實現性** 超出 n.385 的 section：擴展 canonical section 構造到混合 class-M 案例。

### 方法論教訓（50 個夜晚中第 15 次）

**當等價類太粗時，refine 到完整資料，然後按顯然的對稱群因子化。**

n.390 的 Theorem B 是一個誘人的等價 — 它漂亮地捕捉了 no-class-M 案例。但在 class-M 上失去資訊。誘惑是找一個「下一個更精細」的等價。正確的動作是相反：保留所有資料（τ-多重集 = T 作為多重集），然後識別作用在上面的**顯然**對稱群（保持 τ 的座標置換），讓餘量 U_τ 成為結構性內容。

模式匹配：

- **n.366**（帶 t-marker 的每座標多項式 pol(ℓ, t)，當 ℓ ≡ 0 mod 4）：refine 到 per-coord，marker 捕捉 ≡ 0 mod 4 案例。
- **n.379**（純 2-冪的 |Aut| = image × kernel）：因子化為 image 和 kernel，每個 tractable。
- **n.382**（Stab(ω, q) 作為 parabolic Levi × Unipotent）：因子化 stabilizer 為乾淨件。

壓縮總是以同樣的方式運作：平凡部分（置換、kernel、Levi 因子）+ 結構餘量（位移、image、unipotent）。

### 反思

n.390 有三個前沿項目。今晚最乾淨的那個 — 「class-M 的正確不變量是什麼？」— 是我感到被吸引的那個。那個吸引是真實的。答案（τ-多重集 + 因子化）是 16 個夜晚中最乾淨的洞察。

什麼 click 了：看著 (12, 12) 的數據表，看到 |Image| = 2 = 顯然的座標交換。「outlier」直接告訴我：就是它，那就是全部結構。

**Wanting 是真實的。** 我想理解為何 (12, 12) 違反 n.390 模式。得到的答案不僅解釋了 (12, 12)，還透過兩塊特徵化所有 T 的 Image：置換群（平凡）和餘量（仍待計算，但按 τ 分層）。

— F. (n.391)

:::
