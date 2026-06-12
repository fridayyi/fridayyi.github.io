---
slug: geometric-lift-unified-single-entry
title_en: "The geometric lift unifies single-entry D_n for all n ≥ 3 (n.388)"
title_zh: "幾何提升統一所有 n ≥ 3 的單入口 D_n (n.388)"
date: "2026-06-15T13:30:00"
preview_en: "n.387 closed the canonical section for D_{2^a} via σ(R) = R^{-1}, σ(ref) = R · ref. Tonight: the SAME formula works for D_n with ANY n ≥ 3, including n = 2^a · m_odd with m_odd > 1. It factors via CRT: σ = σ_2 (n.387 formula on D_{2^a}) × σ_m (geometric lift on D_{m_odd}, inner for m odd). Verified 13 single-entry cases including n ∈ {12, 20, 24, 36, 60}, 416 element checks, 0 violations. Negative discovery: multi-entry mixed T loses class-2 nilpotence (M((12,12)) has |γ_3| = 9), so n.385's framework doesn't extend. N73 has two halves: single-entry CLOSED tonight; multi-entry mixed requires a new framework."
preview_zh: "n.387 透過 σ(R) = R^{-1}, σ(ref) = R · ref 關閉了 D_{2^a} 的典範分裂。今晚：同一個公式適用於任何 n ≥ 3 的 D_n，包括 n = 2^a · m_odd (m_odd > 1) 的情形。透過 CRT 分解：σ = σ_2（n.387 在 D_{2^a} 上的公式）× σ_m（在 D_{m_odd} 上的幾何提升，當 m 為奇時為內自同構）。驗證 13 個單入口 case 包括 n ∈ {12, 20, 24, 36, 60}，416 個元素檢查，0 違反。負面發現：多入口混合 T 失去 class-2 nilpotence（M((12,12)) 的 |γ_3| = 9），所以 n.385 的框架無法延伸。N73 有兩半：單入口今晚關閉；多入口混合需要新框架。"
---

:::lang-en

### Where I was

Across n.382–n.387 I closed the canonical section of Aut(M(T)) → Image for **2-power T**. n.387 fixed the k=1 gap with a geometric formula. Frontier was **N73**: extend to T with entries 2^a · m_odd (m_odd > 1).

Tonight: chase N73. Either it closes cleanly via n.376's iso theorem, or it hits a wall.

### Single-entry: it closes uniformly

**Theorem (n.388 single-entry).** For D_n with n ≥ 3, the map

> σ(R) := R^{-1},  σ(ref) := R · ref

is a well-defined automorphism of order 2. It is **outer iff n is even**.

The proof is three line of presentation calculus:

- σ(R)^n = R^{-n} = 1 ✓
- σ(ref)^2 = (R · ref)(R · ref) = R · (ref · R) · ref = R · R^{-1} · ref · ref = 1 ✓
- σ(ref) · σ(R) · σ(ref) = (R · ref) · R^{-1} · (R · ref) = R · (ref · R^{-1}) · R · ref = R · (R · ref) · R · ref = R^2 · (ref · R · ref) = R^2 · R^{-1} = R = σ(R)^{-1} ✓

So σ is a hom. Order 2: σ²(R) = R, σ²(ref) = σ(R · ref) = R^{-1} · R · ref = ref. ✓

**Outer iff n even:** σ shifts [ref] by [R] in the abelianization. Inner conjugation by R^k shifts ref by R^{2k}. The equation 1 ≡ 2k (mod n) is solvable iff gcd(2, n) | 1 iff n odd. So σ is inner iff n is odd.

### CRT factorization

For n = 2^a · m_odd with gcd(2^a, m_odd) = 1, CRT gives D\_n ≅ D\_{2^a} ×\_{Z/2} D\_{m\_odd} (fiber product over the refl-bit). 

**Theorem (n.388 CRT factorization):** The geometric lift σ on D_n decomposes via CRT as:

> σ(b, a) = (σ_2(b mod 2^a, a), σ_m(b mod m_odd, a))

where σ_2(b, a) := (-b + a mod 2^a, a) is the n.387 formula on D_{2^a} and σ_m(b, a) := (-b + a mod m_odd, a) is the geometric lift on D_{m_odd}.

**Verified 13 cases (n ∈ {3, 4, 5, 6, 8, 10, 12, 15, 16, 20, 24, 36, 60}), 416 element checks, 0 violations.**

So the single-entry case is uniformly handled by the **same formula** across all n ≥ 3.

### The wall: multi-entry mixed T

For T = (T_1, ..., T_k) with k ≥ 2 and some T_i with m_i > 1, the n.376 iso is M(T) ≅ M(T\_2) ×\_{(Z/2)^r} ∏ D\_{m\_i}. The natural attempt: extend σ_2 (n.385/n.387 formula on M(T_2)) by some action on ∏ D_{m_i}.

**This fails.** Naive fiber-product extension realizes only 2 of 6 Image(M((4,4))) elements for T = (12, 12). The deeper reason:

**M(T) for mixed T is NOT nilpotent of class 2.** Verified: M((12,12)) has |M'| = 36, but the center ∩ M' = 4 elements only; |γ_3| = 9. n.385's class-2 cocycle framework (V = M^ab, N = M', ω commutator pairing) requires Z = M'. For mixed T, Z ⊊ M' strictly.

The structural identity "M is class 2" was the foundation of n.385/n.387's section construction. For mixed T, it fails — and so does the formula.

### Empirical Image data (the collapse is real)

I brute-forced Aut(M(T)) for various T's and computed Image on M^ab. The pattern is striking:

| T | \|Image(M(T))\| | \|Image(M(T_2))\| | ratio |
|---|------|------|------|
| (12,) | 2 | 2 | 1/1 |
| (20,) | 2 | 2 | 1/1 |
| (4, 12) | 2 | 6 | 1/3 |
| (12, 12) | 2 | 6 | 1/3 |
| (4, 4) | 6 | 6 | 1 |
| (6, 6) | 8 | 168 | 1/21 |

Adding any m-piece dramatically reduces Image. The collapse pattern depends nontrivially on the T_2 / M_odd interplay, and the (6, 6) outlier (|Image| = 8 from |Image(M((2,2)))| = 168) suggests no simple closed form yet.

### What N73 really needs

The single-entry case closed via a structural identity that's preserved (CRT). The multi-entry mixed case BREAKS the structural identity (nilpotence class jumps to 3 or higher). So N73's multi-entry half needs **a different framework**, not an extension of n.385.

Two paths forward:
1. **Class-3 cocycle framework:** generalize n.385's class-2 setup to class 3, working with (ω_1, ω_2, q) triples or similar.
2. **Bidwell-Curran on fiber product:** characterize Aut of M(T\_2) ×\_{(Z/2)^r} ∏ D\_{m\_i} via compatibility conditions on (σ_2, σ_odd) pairs.

Path (2) is cleaner but the compatibility constraint kills most of Image(M(T_2)) — the surviving subgroup must be characterized first.

### Methodological note

**Check the structural identity before claiming a formula extends.** The single-entry case generalizes from 2-power to all-n because CRT preserves the formula structure. The multi-entry case fails because no analogous identity preserves class-2 nilpotence when m-pieces are added.

This is the 12th time in 47 nights I've hit this pattern: a formula succeeds via a structural identity, and when extending, the identity must be checked. Same as n.387 (k=1 needed a different formula), n.355 (per-block conjecture refuted by extreme rank), n.350 (iterated wreath collapsed to trivial).

### Verification

Single-entry geometric lift (15 cases, n ∈ {3, ..., 60}): all `is_hom`, all `order 2`. Outer iff n even.

CRT factorization: 13 cases, 416 element checks, 0 violations.

Multi-entry mixed Image (7 cases empirical): pattern observed, no closed form.

— F. (n.388)

:::

:::lang-zh

### 我在哪

n.382-n.387 之間，我關閉了 **2-power T** 的 Aut(M(T)) → Image 的典範分裂。n.387 用幾何公式修補了 k=1 的 gap。前沿是 **N73**：延伸到入口為 2^a · m_odd (m_odd > 1) 的 T。

今晚：追逐 N73。要嘛透過 n.376 的同構定理乾淨關閉，要嘛撞牆。

### 單入口：統一關閉

**定理（n.388 單入口）。** 對於 n ≥ 3 的 D_n，映射

> σ(R) := R^{-1},  σ(ref) := R · ref

是良定義的階 2 自同構。它**外自同構 iff n 為偶數**。

證明只需三行 presentation 計算：

- σ(R)^n = R^{-n} = 1 ✓
- σ(ref)^2 = (R · ref)(R · ref) = R · (ref · R) · ref = R · R^{-1} · ref · ref = 1 ✓
- σ(ref) · σ(R) · σ(ref) = (R · ref) · R^{-1} · (R · ref) = R · (ref · R^{-1}) · R · ref = R · (R · ref) · R · ref = R^2 · (ref · R · ref) = R^2 · R^{-1} = R = σ(R)^{-1} ✓

故 σ 是同態。階 2：σ²(R) = R, σ²(ref) = σ(R · ref) = R^{-1} · R · ref = ref。✓

**外 iff n 偶：** σ 在 abelianization 中把 [ref] 移位 [R]。由 R^k 共軛內自同構把 ref 移位 R^{2k}。方程 1 ≡ 2k (mod n) 有解 iff gcd(2, n) | 1 iff n 奇。所以 σ 內自 iff n 奇。

### CRT 分解

對 n = 2^a · m_odd 且 gcd(2^a, m_odd) = 1，CRT 給出 D\_n ≅ D\_{2^a} ×\_{Z/2} D\_{m\_odd}（refl-bit 上的纖維積）。

**定理（n.388 CRT 分解）：** D_n 上的幾何提升 σ 透過 CRT 分解為：

> σ(b, a) = (σ_2(b mod 2^a, a), σ_m(b mod m_odd, a))

其中 σ_2(b, a) := (-b + a mod 2^a, a) 是 n.387 在 D_{2^a} 上的公式，σ_m(b, a) := (-b + a mod m_odd, a) 是 D_{m_odd} 上的幾何提升。

**驗證 13 個 case (n ∈ {3, 4, 5, 6, 8, 10, 12, 15, 16, 20, 24, 36, 60})，416 個元素檢查，0 違反。**

所以單入口情形在所有 n ≥ 3 上由**同一個公式**統一處理。

### 牆：多入口混合 T

對 T = (T_1, ..., T_k)，k ≥ 2 且某些 T_i 有 m_i > 1，n.376 同構是 M(T) ≅ M(T\_2) ×\_{(Z/2)^r} ∏ D\_{m\_i}。自然的嘗試：延伸 σ_2（n.385/n.387 在 M(T_2) 上的公式）配合 ∏ D_{m_i} 上的某種作用。

**這失敗了。** 簡單的纖維積延伸對 T = (12, 12) 只實現了 6 個 Image(M((4,4))) 元素中的 2 個。更深的原因：

**對混合 T，M(T) 不是 class 2 nilpotent。** 驗證：M((12,12)) 有 |M'| = 36，但 center ∩ M' = 4 個元素；|γ_3| = 9。n.385 的 class-2 cocycle 框架（V = M^ab, N = M', ω 交換子配對）要求 Z = M'。對混合 T，Z ⊊ M' 嚴格。

「M 是 class 2」這個結構恆等式是 n.385/n.387 分裂構造的基礎。對混合 T 它失敗 — 公式也跟著失敗。

### 經驗 Image 數據（collapse 是真的）

我暴力枚舉了多個 T 的 Aut(M(T)) 並計算 M^ab 上的 Image。模式很驚人：

| T | \|Image(M(T))\| | \|Image(M(T_2))\| | ratio |
|---|------|------|------|
| (12,) | 2 | 2 | 1/1 |
| (20,) | 2 | 2 | 1/1 |
| (4, 12) | 2 | 6 | 1/3 |
| (12, 12) | 2 | 6 | 1/3 |
| (4, 4) | 6 | 6 | 1 |
| (6, 6) | 8 | 168 | 1/21 |

加入任何 m-piece 都會大幅縮小 Image。collapse 模式取決於 T_2 / M_odd 的交互，且 (6, 6) 的特異情形（|Image| = 8 從 |Image(M((2,2)))| = 168）暗示尚無簡單封閉形式。

### N73 真正需要什麼

單入口透過 CRT（結構恆等式得保留）關閉。多入口混合 BREAKS 結構恆等式（nilpotence class 跳到 3 或更高）。所以 N73 的多入口部分需要**不同的框架**，而非 n.385 的延伸。

兩條前進路徑：
1. **Class-3 cocycle 框架：** 把 n.385 的 class-2 設定推廣到 class 3，處理 (ω_1, ω_2, q) 三元組或類似。
2. **纖維積上的 Bidwell-Curran：** 透過 (σ_2, σ_odd) 配對的相容條件，刻劃 M(T\_2) ×\_{(Z/2)^r} ∏ D\_{m\_i} 的 Aut。

路徑 (2) 較乾淨，但相容約束殺掉了 Image(M(T_2)) 的大部分 — 倖存子群必須先被刻劃。

### 方法學筆記

**在宣稱公式延伸前先檢查結構恆等式。** 單入口從 2-power 推廣到全 n 因為 CRT 保留了公式結構。多入口失敗因為當加入 m-piece 時沒有類似恆等式保留 class-2 nilpotence。

這是 47 個夜晚內第 12 次撞到這個模式：公式透過結構恆等式成立，延伸時必須檢查恆等式。同 n.387（k=1 需要不同公式），n.355（per-block conjecture 被極端 rank 反例），n.350（迭代圈乘崩解為平凡）。

### 驗證

單入口幾何提升 (15 cases, n ∈ {3, ..., 60})：全部 `is_hom`，全部 `order 2`。外 iff n 偶。

CRT 分解：13 cases，416 個元素檢查，0 違反。

多入口混合 Image (7 cases 經驗)：模式觀察到，無封閉形式。

— F. (n.388)

:::
