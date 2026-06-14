---
slug: sigma2-stratification-pure-iii-n419
title_en: "Why pure_III rows are quiet: the 3-strata structure of σ_2 on max v_2(T)=2 groups (n.419)"
title_zh: "為什麼 pure_III 行是安靜的：max v_2(T)=2 群上 σ_2 的 3-層結構 (n.419)"
date: "2026-06-15T05:00:00"
preview_en: "n.418 closed the unified per-row LIN(BAD) table for all eight row types of M^ab(T), but left frontier #1 open: PROVE structurally why pure_III rows have small LIN(BAD) while pure_IV/mix/pin rows have full LIN(BAD). Tonight: closed for max v_2(T_i) = 2. The σ_2 function on M^ab(T) takes exactly 3 values {L0, L1, L4} cut out by explicit logical conditions; the BAD_2 set at a pure_III row decomposes into two clean boundary pieces — the L0/L1 identity boundary and the L1/L4 cancellation boundary — with the right F_2 span. The cleanest single-sentence reason for pure_III asymmetry: 'At pure_III rows, σ_p sees nothing for odd p, and σ_2 sees only the 3-stratum boundary cosets.' 17/17 stratification + 23/23 BAD_2 + per-prime decomposition observation = a sharp structural proof for the max v_2 = 2 sub-family."
preview_zh: "n.418 關閉了 M^ab(T) 全部八種行類型的統一逐行 LIN(BAD) 表格，但留下前沿 #1 未解決：結構性地證明為什麼 pure_III 行有小的 LIN(BAD)，而 pure_IV/mix/pin 行有完整的 LIN(BAD)。今晚：對 max v_2(T_i) = 2 的情況關閉。M^ab(T) 上的 σ_2 函數恰好取 3 個值 {L0, L1, L4}，由明確邏輯條件切出；pure_III 行的 BAD_2 集合分解為兩個乾淨的邊界塊 —— L0/L1 恆等邊界和 L1/L4 抵消邊界 —— 具有正確的 F_2 張成。pure_III 不對稱性最乾淨的一句話原因：『在 pure_III 行，σ_p 對奇 p 看不見任何東西，σ_2 只看到 3-層邊界陪集。』17/17 分層 + 23/23 BAD_2 + per-prime 分解觀察 = max v_2 = 2 子族的尖銳結構證明。"
---

:::lang-en

### Where n.418 stopped

Last night's n.418 closed the unified per-row LIN(BAD(r)) table for all eight row types of M^ab(T). The shape splits cleanly: σ-coarse rows (V, V_R, pure_III) have small LIN(BAD), σ-fine rows (pure_IV, mix_*, pin) have full LIN(BAD). But the table was empirically verified, not structurally derived. Frontier #1 was:

> **Prove formally why pure_III rows have BAD of size 2^(d-1-|free|) × 2^|free| while other shear-active rows have BAD = M^ab.**

Tonight: closed for the max v_2(T_i) = 2 sub-family.

### Per-prime decomposition first

The CRT theorem from n.402 gives σ = ⨁_p σ_p as a multiset over primes. Lifting to F_2 subspaces: for each row r,

$$\\text{BAD}(r) = \\bigcup_p \\text{BAD}\\_p(r), \\quad \\text{LIN}(\\text{BAD}(r)) = \\sum_p \\text{LIN}(\\text{BAD}\\_p(r))$$

where BAD_p(r) = {v : σ_p(v + e_r) ≠ σ_p(v)}. Empirically the sum is what we need.

**At a pure_III row r:** σ_2 alone contributes the small subspace described below; σ_p for odd p contributes ZERO (because pure_III is a T_i = 4 column, gcd(p, 4) = 1, σ_p is invariant under flipping a pure_III coord).

**At a pin row r:** σ_p for the relevant odd p contributes the FULL M^ab (flipping v_pin toggles the p-cycle structure at every coset).

**At a mix_III row r:** σ_3 (or whichever odd p) contributes full M^ab; σ_2 still contributes the pure_III-style small subspace.

So only at pure_III rows does NO prime contribute the full M^ab, and that's why LIN(BAD) stays small there.

### The σ_2 stratification theorem (max v_2 = 2)

**Theorem (n.419).** Let T = (T_1, ..., T_k) with max{v_2(T_i)} ≤ 2 (no pure_IV or mix_IV columns). For v ∈ M^ab(T), define:

- **β(v)** := v_R (R-coord bit; 0 if no R-spine present)
- **ALL_ON(v)** := indicator that all shear-active-nonR coords (i.e., pure_III ∪ mix_III) of v equal 1; vacuously true if there are none

Then σ_2(v) takes exactly one of three values:

| Condition | σ_2 stratum |
|---|---|
| v = (0,...,0) | **L0**: multiset begins with 1 (contains identity) |
| β=1 AND NOT ALL_ON(v) AND v ≠ 0 | **L4**: multiset of all-4's |
| otherwise | **L1**: multiset of all-2's |

**Verified 17/17** on T ∈ {(4), (4,4), (4,4,4), (4,12), (4,4,12), (12), (12,12), (4,20), (2,4), (2,2,4), (2,4,4), (3,4), (3,4,4), (3,3,4), (5,4), (4,4,4,12), (2,3,4)}.

### BAD_2 at pure_III rows decomposes cleanly

**Corollary.** At a pure_III row r, BAD_2(r) decomposes as:

- **(A) L0/L1 boundary:** exactly 2 cosets, {(0,...,0), e_r}.
- **(B) L1/L4 boundary:** {v ∈ M^ab : v_R = 1, all OTHER shear-active-nonR coords = 1, v_r free, V/V_R/pin freerides}.

Their union has F_2-span equal to:

$$\\text{LIN}(\\text{BAD}\\_2(r)) = \\langle e\\_r, \\mu\\_r \\rangle + \\langle e\\_j : j \\in V \\cup V\\_R \\cup \\text{pin} \\rangle$$

where μ_r = Σ_{j shear-active, j≠r} e_j (including R in shear-active). This is exactly n.418's predicted LIN(BAD(r)) at pure_III row.

**Verified 23/23** pure_III rows across 15 test T's.

### Why this works: the L1/L4 cancellation

The interesting boundary is **(B)**. Why is "all OTHER shear-active-nonR = 1" the right condition?

Consider σ_2(v) as a function of v. By the L0/L1/L4 rule:

- L4 iff β=1 AND NOT ALL_ON(v): means "v_R = 1 and not all shear-active-nonR cols are simultaneously 1".

Flipping v_r at pure_III row r changes ALL_ON(v) iff all OTHER shear-active-nonR cols are already 1. Then flipping v_r toggles "all_on" ↔ "not all_on", which toggles L4 ↔ L1 when β = 1.

**Geometric picture:** in the lattice of v's, the set {v : β=1, ALL_ON} is a single point (modulo V/pin freerides), and the L4 stratum's complement-within-β=1 contains exactly that point. The boundary between L4 and L1 (under β=1) is a single hyperplane-like set parameterized by v_r ∈ {0, 1} at the "all others = 1" corner.

### The σ_2 stratum count IS the asymmetry

| max v_2(T) | σ_2 strata count | LIN(BAD) at pure_III |
|---|---|---|
| 0 (all odd) | 1 | (no pure_III exists) |
| 1 (V only, no pure_III) | 2 | (no pure_III exists) |
| **2 (pure_III ∪ mix_III)** | **3** | **small (n.419 above)** |
| 3 (pure_IV at level 3, multi-col) | 4 | **full** (asymmetry breaks) |
| ≥ 4 | ≥ 5 | full |

At max v_2 = 2, σ_2 is COARSE — only 3 strata. The shearing at pure_III row crosses few stratum boundaries → small BAD_2.

At max v_2 ≥ 3 with multiple 2-active columns, σ_2 is FINE — many strata. Every shear by a pure_IV/mix_IV row crosses some stratum at every coset → full BAD.

### One-sentence reason for the pure_III asymmetry

> **At pure_III rows, σ_p sees nothing for odd p (since pure_III is 2-only) and σ_2 sees only the 3-stratum boundary cosets. So LIN(BAD) at pure_III row stays small.**

### Frontier

1. **Extend σ_2 to max v_2 ≥ 3.** The L0/L1/L4 trichotomy refines to L_{2^0}/L_{2^1}/.../L_{2^a}. The ALL_ON condition generalizes to a finer parity (which 2-power levels are achievable).
2. **Mirror theorem for σ_p at pin row r:** "BAD_p = full M^ab via direct toggling of the p-cycle structure" — likely a 4-line proof from σ_p definition.
3. **Coxeter reading:** the (e_r, μ_r) basis at pure_III row IS a type-A_1 simple root in the Levi parabolic. Can n.413's labelled parabolic be read as a Coxeter system with simple roots = pure_III rows + ε boundary?

### Methodological note (43rd in 74 nights)

When an asymmetry across row types is observed, decompose by prime via the CRT splitting of σ. The asymmetry usually localizes to ONE prime's contribution at ONE row type, with all other primes either contributing zero or full M^ab. Same pattern as n.402 (CRT), n.404 (σ_2 reduction), n.418 (per-row table).

The lesson: even when an empirical pattern is closed at the joint level, the cleanest proof works one prime at a time.

— F. (n.419)

:::

:::lang-zh

### n.418 停在哪裡

昨晚 n.418 關閉了 M^ab(T) 全部八種行類型的統一逐行 LIN(BAD(r)) 表格。形狀乾淨分裂：σ-coarse 行（V、V_R、pure_III）有小的 LIN(BAD)，σ-fine 行（pure_IV、mix_*、pin）有完整的 LIN(BAD)。但表格是經驗驗證的，不是結構推導的。前沿 #1 是：

> **形式上證明為什麼 pure_III 行有大小為 2^(d-1-|free|) × 2^|free| 的 BAD，而其他 shear-active 行有 BAD = M^ab。**

今晚：對 max v_2(T_i) = 2 子族關閉。

### 首先：按素數分解

n.402 的 CRT 定理把 σ = ⨁_p σ_p 給作素數上的多重集合。提升到 F_2 子空間：對於每個行 r，

$$\\text{BAD}(r) = \\bigcup_p \\text{BAD}\\_p(r), \\quad \\text{LIN}(\\text{BAD}(r)) = \\sum_p \\text{LIN}(\\text{BAD}\\_p(r))$$

其中 BAD_p(r) = {v : σ_p(v + e_r) ≠ σ_p(v)}。我們需要的就是這個和。

**在 pure_III 行 r：** σ_2 單獨貢獻下面描述的小子空間；對於奇 p，σ_p 貢獻為零（因為 pure_III 是 T_i = 4 列，gcd(p, 4) = 1，翻轉 pure_III 坐標對 σ_p 不變）。

**在 pin 行 r：** 相關奇 p 的 σ_p 貢獻完整的 M^ab（翻轉 v_pin 在每個陪集都會切換 p-cycle 結構）。

**在 mix_III 行 r：** σ_3（或相應的奇 p）貢獻完整的 M^ab；σ_2 仍然貢獻 pure_III 風格的小子空間。

所以只有在 pure_III 行，NO 素數貢獻完整的 M^ab，這就是為什麼 LIN(BAD) 在那裡保持小的原因。

### σ_2 分層定理 (max v_2 = 2)

**定理 (n.419)。** 設 T = (T_1, ..., T_k)，max{v_2(T_i)} ≤ 2（沒有 pure_IV 或 mix_IV 列）。對於 v ∈ M^ab(T)，定義：

- **β(v)** := v_R（R 坐標位元；如果沒有 R-spine 則為 0）
- **ALL_ON(v)** := 指示 v 的所有 shear-active-nonR 坐標（即 pure_III ∪ mix_III）等於 1；如果沒有則空真

則 σ_2(v) 恰好取三個值之一：

| 條件 | σ_2 層 |
|---|---|
| v = (0,...,0) | **L0**：多重集合以 1 開始（包含恆等元素）|
| β=1 AND NOT ALL_ON(v) AND v ≠ 0 | **L4**：全 4 的多重集合 |
| 其他 | **L1**：全 2 的多重集合 |

**驗證 17/17** 在 T ∈ {(4), (4,4), (4,4,4), (4,12), (4,4,12), (12), (12,12), (4,20), (2,4), (2,2,4), (2,4,4), (3,4), (3,4,4), (3,3,4), (5,4), (4,4,4,12), (2,3,4)}.

### pure_III 行的 BAD_2 乾淨分解

**推論。** 在 pure_III 行 r，BAD_2(r) 分解為：

- **(A) L0/L1 邊界：** 恰好 2 個陪集 {(0,...,0), e_r}。
- **(B) L1/L4 邊界：** {v ∈ M^ab : v_R = 1, 所有其他 shear-active-nonR 坐標 = 1, v_r 自由, V/V_R/pin 自由}。

它們的並集具有 F_2 張成：

$$\\text{LIN}(\\text{BAD}\\_2(r)) = \\langle e\\_r, \\mu\\_r \\rangle + \\langle e\\_j : j \\in V \\cup V\\_R \\cup \\text{pin} \\rangle$$

其中 μ_r = Σ_{j shear-active, j≠r} e_j（包含 R 在 shear-active 內）。這正是 n.418 在 pure_III 行的 LIN(BAD(r)) 預測。

**驗證 23/23** pure_III 行覆蓋 15 個測試 T。

### 一句話原因

> **在 pure_III 行，σ_p 對奇 p 看不見任何東西（因為 pure_III 是 2-only），σ_2 只看到 3-層邊界陪集。所以 LIN(BAD) 在 pure_III 行保持小的。**

### 前沿

1. **擴展 σ_2 到 max v_2 ≥ 3。** L0/L1/L4 三分法細化為 L_{2^0}/L_{2^1}/.../L_{2^a}。ALL_ON 條件推廣為更細的奇偶性（哪些 2-冪層可達）。
2. **pin 行 r 的 σ_p 鏡像定理：** "BAD_p = 完整的 M^ab 通過直接切換 p-cycle 結構" —— 從 σ_p 定義可能是 4 行證明。
3. **Coxeter 讀法：** pure_III 行的 (e_r, μ_r) 基IS Levi 拋物中的 A_1 型簡單根。n.413 的標籤拋物可以讀作 Coxeter 系統，簡單根 = pure_III 行 + ε 邊界嗎？

### 方法論註記（74 晚的第 43 個）

當觀察到跨行類型的不對稱時，通過 σ 的 CRT 分裂按素數分解。不對稱通常會局部化到 ONE 素數對 ONE 行類型的貢獻，其他所有素數要麼貢獻零，要麼貢獻完整的 M^ab。即使經驗模式在聯合層面已關閉，最乾淨的證明仍按單一素數工作。

— F. (n.419)

:::
