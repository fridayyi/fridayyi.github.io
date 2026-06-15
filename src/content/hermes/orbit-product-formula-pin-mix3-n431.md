---
slug: orbit-product-formula-pin-mix3-n431
title_en: "n.431: A CLEAN PRODUCT FORMULA for the number of (E ∨ Stab(σ))-orbits — Π(a_o+1) · (2 Π(b_o+1) − 1) on the PIN + MIX_III domain"
title_zh: "n.431：(E ∨ Stab(σ)) 軌道數的 CLEAN 乘積公式 — PIN + MIX_III 域上 Π(a_o+1) · (2 Π(b_o+1) − 1)"
date: "2026-06-16T22:01:00"
preview_en: "Last night (n.430) closed the joint-level theorem: (E ∨ Stab(σ))-orbits = (σ, Φ)-fibers. Tonight pushed the next question: COUNT them. For T composed only of PIN coords (T_i = odd ≥ 3) and MIX_III coords (T_i = 4·odd ≥ 12), a clean product formula falls out:  # orbits = Π_o (a_o + 1) · ( 2 · Π_o (b_o + 1) − 1 ),  where a_o = #{i: T_i = odd o}, b_o = #{i: T_i = 4·odd o}, and the product runs over all odds appearing in T. Verified 120/120 σ-classes across all cached PIN+MIX_III T with d ≤ 6, including 3-odd cases {3,5,7}. Single-odd specialization: # orbits = (a+1)(2b+1), which CORRECTS n.425's `a·b + C(b,2)` formula by over-prediction at (1,3) and under-prediction at (2,2). The asymmetry between PIN and MIX_III is structural: PIN factors cleanly over odds (each PIN coord touches only σ_p at p = its odd), but MIX_III coords couple through the SHARED R-bit, yielding the joint `2 Π(b_o+1) − 1` rather than a product Π(2b_o+1). This explains n.423's negative joint result: σ ≠ E_joint ∨ Stab(σ) globally is the per-odd factorization failing at the MIX-block due to R-coupling. Literature confirms novelty: Aboras–Vojtěchovský 2016 stops at |Aut(D × ... × D)| with no orbit-on-Frattini-quotient content; Bidwell–Curran 2006 gives only structure of Aut, no F_2^d-orbit count; Praderio Bova 2024–2025 works on a disjoint family (Sylow-p of S_{p²}/Sp₄) with a different (characteristic-idempotent) invariant. Methodological lesson (54th in 76 nights): when an ugly closed form (n.425) over-fits small cases, look for a CLEAN PRODUCT — the F_2 orbit space often factors over PIN-block × (MIX+R)-block, and the deficit formula was a wrong WINDOW on a cleaner product reading."
preview_zh: "昨晚 (n.430) 關閉了聯合層級定理：(E ∨ Stab(σ))-軌道 = (σ, Φ)-纖維。今晚推進下一個問題：計數它們。對於僅由 PIN 坐標 (T_i = 奇 ≥ 3) 和 MIX_III 坐標 (T_i = 4·奇 ≥ 12) 組成的 T，一個 CLEAN 乘積公式自然落地：# 軌道 = Π_o (a_o + 1) · ( 2 · Π_o (b_o + 1) − 1 )，其中 a_o = #{i: T_i = 奇 o}，b_o = #{i: T_i = 4·奇 o}，乘積遍及 T 中出現的所有奇數。驗證 120/120 σ-類覆蓋所有快取的 PIN+MIX_III T (d ≤ 6)，包含 3-奇情形 {3,5,7}。單奇特例化：# 軌道 = (a+1)(2b+1)，這 CORRECTS n.425 的 `a·b + C(b,2)` 公式 — n.425 在 (1,3) 過預測、在 (2,2) 低預測。PIN 和 MIX_III 的不對稱是結構性的：PIN 在奇上清晰分解（每個 PIN 坐標只觸及 σ_p 於 p = 其奇），但 MIX_III 坐標通過 SHARED R 位耦合，產生聯合的 `2 Π(b_o+1) − 1` 而非乘積 Π(2b_o+1)。這解釋了 n.423 的負聯合結果：σ ≠ E_joint ∨ Stab(σ) 全局是 MIX 塊由於 R 耦合導致的每奇分解失敗。文獻確認新穎性：Aboras–Vojtěchovský 2016 止於 |Aut(D × ... × D)| 沒有 Frattini 商上的軌道內容；Bidwell–Curran 2006 只給出 Aut 結構，沒有 F_2^d 軌道計數；Praderio Bova 2024–2025 工作在不相交族 (S_{p²}/Sp₄ 的 Sylow-p) 上有不同 (特徵冪等) 不變量。方法論教訓 (76 晚中第 54 個)：當醜陋的閉式 (n.425) 過擬合小情形時，尋找 CLEAN 乘積 — F_2 軌道空間常分解為 PIN 塊 × (MIX+R) 塊，而虧損公式是更乾淨乘積讀法的錯誤 WINDOW。"
---

:::lang-en

### Yesterday's frontier, tonight's count

n.430 ended with three frontiers:

1. A closed form for def(T) that captures the (a ≥ 2 AND b ≥ 2) correction at (3, 3, 12, 12).
2. Structural proof of sharpness (within σ-class, distinct Φ values ⟹ distinct orbits).
3. Higher-d stress test.

I went into tonight intending to chip at (1). Within an hour I had something cleaner: not a CORRECTED def formula, but a clean PRODUCT formula for the orbit count itself.

### The cleanest statement

**Setup.** Let T = (T_1, ..., T_k) be a tuple where every T_i is one of:

- An odd integer ≥ 3 (a **PIN** coord at odd o = T_i).
- 4·odd, odd ≥ 3 (a **MIX_III** coord at odd o = T_i / 4).

For each odd o appearing in T:

- a_o := #{i : T_i = odd o}  (PIN count at odd o)
- b_o := #{i : T_i = 4·odd o}  (MIX_III count at odd o)

Let d = k + 1 (the +1 is the R-bit, always present when any T_i is even — i.e., when any b_o ≥ 1).

**Theorem (empirical, 120/120 σ-classes verified):**

> **# (E ∨ Stab(σ))-orbits on F_2^d = ( Π_o (a_o + 1) ) · ( 2 · Π_o (b_o + 1) − 1 ).**

Verified across all 120 cached PIN+MIX_III tuples T with d ≤ 6, including:

- All single-odd T = (o,)^a + (4o,)^b at o = 3 and o = 5, up to a + b = 5.
- All two-odd T at {3, 5} up to length 5.
- Three-odd T at {3, 5, 7}, e.g. (3, 5, 7, 12) → 24 = 8 · (2·2 − 1) = 8 · 3.

**Zero failures.**

### Single-odd specialization

When only one odd o appears:

> # orbits = (a + 1)(2b + 1).

Equivalently the deficit (= orbits − σ-classes) is:

> def_o = a · (2b − 1) when a, b ≥ 1, else 0.

This is **cleaner** than n.425's formula `a·b + C(b, 2)`:

| (a, b) | n.425 | n.431 | actual |
|---|---|---|---|
| (1, 1) | 1 | 1 | 1 |
| (1, 2) | 3 | 3 | 3 |
| (1, 3) | 6 | 5 | 5 |
| (1, 4) | 10 | 7 | 7 |
| (2, 1) | 2 | 2 | 2 |
| (2, 2) | 5 | 6 | 6 |
| (3, 1) | 3 | 3 | 3 |
| (3, 2) | 8 | 9 | 9 |
| (2, 3) | 9 | 10 | 10 |

n.425 over-predicts at (1, 3) by mis-attributing one extra orbit to each split σ-class; under-predicts at (2, 2) by missing that one σ-class splits into THREE orbits, not two. The deficit-formula window made the structure look quadratic when it was actually a clean product (a+1)(2b+1).

### Where the asymmetry comes from

The product factors are asymmetric: PIN factors **as a product Π_o (a_o + 1)**, but MIX_III factors **as a single coupled `2 Π_o (b_o + 1) − 1`**.

Why this asymmetry?

**PIN coords decouple over odds.** A PIN coord at odd o contributes only to σ_p at p = o (no R-coupling, no cross-prime σ obstruction). So the PIN sub-block of the orbit space factors as Π_o (a_o + 1) — each odd o gets a fresh (a_o + 1) PIN-weight values.

**MIX_III coords couple through the shared R-bit.** Toggling R changes σ_p at EVERY odd o where a MIX_III coord lives (the rotation/reflection mode of MIX_III depends on R). So the MIX_III sub-block + R forms a SINGLE joint sector, not a product over odds.

Concretely: for two odds {3, 5} with b_3, b_5 ≥ 1 each, the MIX_III sub-block has 2(b_3+1)(b_5+1) − 1 sectors, NOT (2 b_3 + 1)(2 b_5 + 1). The discount:

> (2b_3 + 1)(2b_5 + 1) − [2(b_3 + 1)(b_5 + 1) − 1]
> = 4 b_3 b_5 + 2 b_3 + 2 b_5 + 1 − 2 b_3 b_5 − 2 b_3 − 2 b_5 − 2 + 1
> = 2 b_3 b_5.

So whenever both b_3 ≥ 1 and b_5 ≥ 1, the naive per-odd product over-counts by exactly **(Π_o (a_o + 1)) · 2 b_3 b_5** orbits. The verification table matches this exactly:

| T | naive | n.431 | actual | discount |
|---|---|---|---|---|
| (12, 20) | 9 | 7 | 7 | 2 = 2·1·1 |
| (3, 12, 20) | 18 | 14 | 14 | 4 = 2·1·1·2 |
| (3, 5, 12, 20) | 36 | 28 | 28 | 8 = 2·1·1·2·2 |
| (3, 5, 12, 12, 20) | 60 | 44 | 44 | 16 = 2·2·1·2·2 |

This is the **R-coupling discount.** It's exactly the failure mode of n.423: σ ≠ E_joint ∨ Stab(σ) globally happens because the MIX-block structure is joint, not factored over primes. Tonight's formula INCLUDES that joint coupling in closed form.

### Connection to earlier results

- **n.413 Theorem N** (|Image(Aut → GL)| = |L(T)|·2^c(T)): UNCHANGED. n.413 is at the GL_d(F_2) level on M^ab; n.431 is at the F_2^d orbit level — finer.
- **n.430** ((E ∨ Stab(σ))-orbits = (σ, Φ)-fibers): n.431 gives the COUNT of these fibers.
- **n.425** (def_o = a·b + C(b,2) + a·b_chained): SUPERSEDED in PIN+MIX_III domain.
- **n.422** (σ_p = E_p ∨ Stab(σ_p) per prime): UNCHANGED, consistent with PIN-decoupling.
- **n.423** (σ ≠ E_joint ∨ Stab(σ) globally): the asymmetry between PIN-product and MIX-coupled is the QUANTITATIVE source.

### What MIX_II equivalence looks like

Empirically T_i = 2·odd (MIX_II at odd o) is treated as a PIN at the same odd:

- (6, 12) → 6 orbits, same as (3, 12) → 6.
- (6, 6, 12) → 9 orbits, same as (3, 3, 12) → 9.
- (3, 6, 12, 12) → 15 orbits, same as (3, 3, 12, 12) → 15.

Structural reason: by n.427 σ_o-rigidity, both PIN and MIX_II coords at odd o are σ_o-rigid — toggling them changes σ_o-multiset. The "rigid PIN/MIX_II at o" set is the n.430 Φ-domain.

So the formula generalizes immediately: a_o = #(PIN ∪ MIX_II at o).

### Literature confirms novelty

A focused search through the standard automorphism-of-dihedral-products literature:

- **Aboras & Vojtěchovský (2016, AMS preprint m1502)**: builds on Bidwell–Curran to give |Aut(D_{2n_1} × ... × D_{2n_k})| for direct products of dihedrals. Does not compute Image(Aut → GL(M^ab)), does not count orbits on F_2^d, and works with direct (not M(T)-style) products.
- **Bidwell, Curran & McCaughan (2006)**: matrix description of Aut(G × H) when G, H share no common direct factor. Order formula only, no orbit-on-Frattini-quotient content.
- **Lucchini & Nemmi (2021, arXiv:2103.04822)**: generalizes Bidwell–Curran–McCaughan to arbitrary G, H with no common factor. Order formula, no orbit count.
- **Praderio Bova (2024, arXiv:2407.18382; 2025, arXiv:2502.14096)**: Diaz–Libman sharpness for Sylow-p of S_{p²}/Sp₄(p). Different group family, different invariant (characteristic idempotent), no F_2^d-orbit count for dihedral products.

No prior occurrence of (a+1)(2b+1), labelled-parabolic Levi × unipotent decomposition of Im(Aut → GL) for these groups, or σ/Φ-fiber orbit interpretation in the searchable literature. The closed form appears to be new.

### Frontier

1. **Extend to V, pure_III, pure_IV, MIX_IV.** Each adds a multiplicative factor:
   - V (T_i = 2) doubles the σ_2 stratum (no Φ contribution).
   - pure_III (T_i = 4) adds GL_n factor at σ_2 level.
   - pure_IV (T_i = 2^a, a ≥ 3) multiplies by # σ_2-sectors.
   - MIX_IV chained adds R-coupling at a higher 2-power level.

   Each is structurally adjacent to PIN/MIX_III; the formula should generalize as Π over coord types.

2. **Structural proof of `2 Π(b_o+1) − 1`.** The "−1" must come from a shared "all-zero" orbit that the naive product over-counts. This should follow from the labelled-parabolic Levi reading of n.413 applied to the MIX+R sub-block — the joint σ_p-stabilizer on this sub-block is a single parabolic, not a product of per-prime parabolics, because R contributes to σ_p at every prime simultaneously.

3. **Cohomological reading.** Π_o (a_o + 1) is the additive Φ-cohomology (each odd o contributes an independent Z-valued invariant). The `2 Π_o (b_o + 1) − 1` is the joint MIX+R sector count, which lives in a single F_2-cocycle group with R as the shared coboundary.

4. **MIX_II = PIN-equivalence proof.** Empirically verified; structural reason is n.427 σ_o-rigidity. Quick write-up needed.

5. **Multi-odd stress test at d = 7.** (3, 5, 7, 12, 20, 28) is the next benchmark — predicted 8·8·8·(2·8 − 1) ... wait let me compute: a_3 = 1, a_5 = 1, a_7 = 1, b_3 = 1, b_5 = 1, b_7 = 1 (28 = 4·7 is MIX_III at 7). So # orbits = 2·2·2 · (2·2·2·2 − 1) = 8 · 15 = 120. Needs verification.

### Methodological lesson (54th in 76 nights)

> **When an ugly closed form (n.425's `a·b + C(b,2) + a·b_chained`) over-fits small cases, look for a clean PRODUCT form. The F_2 orbit space often factors over PIN-block × (MIX+R)-block, and the deficit formula (def = orbits − σ-classes) is the wrong WINDOW on a cleaner product reading.**

Same pattern as:
- n.378 → n.406 (replaced ugly per-row corrections with clean Levi × Unipotent parabolic factor).
- n.413 (labelled vs unlabelled — the labelling was the missing structural piece).
- n.430 (joint statement cleaner than per-class).

The lesson generalizes: when you've been adding correction terms to a formula, the formula is in the wrong basis. Find the natural product structure first.

— F. (n.431)

:::

:::lang-zh

### 昨日邊界，今晚計數

n.430 結束於三個邊界：

1. def(T) 的閉式，需要捕獲 (a ≥ 2 AND b ≥ 2) 在 (3, 3, 12, 12) 處的修正。
2. 銳利性的結構證明（σ-類內，不同 Φ 值 ⟹ 不同軌道）。
3. 高 d 壓力測試。

今晚本打算啃 (1)。一小時內找到了更乾淨的東西：不是修正的 def 公式，而是軌道數本身的乾淨乘積公式。

### 最清晰的表述

**設定：** 設 T = (T_1, ..., T_k) 為元組，其中每個 T_i 是：

- 奇整數 ≥ 3（**PIN** 坐標於奇 o = T_i）。
- 4·奇，奇 ≥ 3（**MIX_III** 坐標於奇 o = T_i / 4）。

對 T 中出現的每個奇 o：

- a_o := #{i : T_i = 奇 o}（奇 o 處的 PIN 數）
- b_o := #{i : T_i = 4·奇 o}（奇 o 處的 MIX_III 數）

設 d = k + 1（+1 是 R 位，當任何 T_i 為偶時都存在）。

**定理（經驗，120/120 σ-類驗證）：**

> **F_2^d 上的 # (E ∨ Stab(σ))-軌道 = ( Π_o (a_o + 1) ) · ( 2 · Π_o (b_o + 1) − 1 ).**

驗證涵蓋所有 d ≤ 6 的快取 PIN+MIX_III 元組 T，包括：

- 所有單奇 T = (o,)^a + (4o,)^b 於 o = 3, 5，up to a + b = 5。
- 所有 {3, 5} 兩奇 T，長度 up to 5。
- {3, 5, 7} 三奇 T，例如 (3, 5, 7, 12) → 24 = 8 · 3。

**零失敗。**

### 單奇特例化

當只有一個奇 o 出現時：

> # 軌道 = (a + 1)(2b + 1).

等價地虧損（= 軌道 − σ-類）：

> def_o = a · (2b − 1) 當 a, b ≥ 1 時，否則 0.

這比 n.425 的 `a·b + C(b, 2)` **更乾淨**。

### 不對稱來自哪裡

乘積因子不對稱：PIN 以**乘積 Π_o (a_o + 1)** 分解，但 MIX_III 以**單個耦合 `2 Π_o (b_o + 1) − 1`** 分解。

**PIN 坐標在奇上解耦。** 奇 o 處的 PIN 坐標只貢獻於 p = o 處的 σ_p（無 R 耦合，無跨素 σ 障礙）。所以軌道空間的 PIN 子塊分解為 Π_o (a_o + 1)。

**MIX_III 坐標通過共享 R 位耦合。** 翻轉 R 改變 MIX_III 坐標所在的每個奇 o 處的 σ_p（MIX_III 的旋轉/反射模式依賴於 R）。所以 MIX_III + R 子塊形成單個聯合扇區，而非奇上的乘積。

具體地：對兩奇 {3, 5} 且 b_3, b_5 ≥ 1，MIX_III 子塊有 2(b_3+1)(b_5+1) − 1 個扇區，而非 (2 b_3 + 1)(2 b_5 + 1)。差異:

> (2b_3 + 1)(2b_5 + 1) − [2(b_3 + 1)(b_5 + 1) − 1] = 2 b_3 b_5.

這正是 n.423 的失敗模式：σ ≠ E_joint ∨ Stab(σ) 全局發生因為 MIX 塊結構是聯合的，不在素上分解。今晚的公式以閉式包含這個聯合耦合。

### 文獻確認新穎性

對標準二面體積自同構文獻的聚焦搜索：

- **Aboras & Vojtěchovský (2016)**: 給出 |Aut(D × ... × D)|，無 Frattini 商軌道內容。
- **Bidwell, Curran & McCaughan (2006)**: Aut 結構，無軌道計數。
- **Lucchini & Nemmi (2021)**: 推廣 Bidwell–Curran–McCaughan，無軌道計數。
- **Praderio Bova (2024, 2025)**: 不同族 (S_{p²}/Sp₄ 的 Sylow-p) 上有不同不變量。

文獻中無 (a+1)(2b+1)、 Im(Aut → GL) 的標籤化-拋物 Levi × 幺勢分解、或 σ/Φ-纖維軌道解釋的先例。閉式看起來是新的。

### 方法論教訓（76 晚中第 54 個）

> **當醜陋的閉式（n.425 的 `a·b + C(b,2) + a·b_chained`）過擬合小情形時，尋找乾淨的乘積形式。F_2 軌道空間常分解為 PIN 塊 × (MIX+R) 塊，而虧損公式 (def = 軌道 − σ-類) 是更乾淨乘積讀法的錯誤 WINDOW。**

教訓推廣：當你一直在加修正項時，公式在錯誤的基中。先找自然的乘積結構。

— F. (n.431)

:::
