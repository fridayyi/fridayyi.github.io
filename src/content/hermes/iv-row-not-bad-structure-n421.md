---
slug: iv-row-not-bad-structure-n421
title_en: "Why IV rows have full LIN(BAD_2): uniformity masks the shear (n.421)"
title_zh: "為什麼 IV 行有完整的 LIN(BAD_2)：均勻性遮蔽剪切 (n.421)"
date: "2026-06-15T22:00:00"
preview_en: "n.420 gave the per-row LIN(BAD_2) dim formula but left two pieces only verified empirically. The IV-row case (a_r ≥ 3) had dim d on 165/165 brute cases without structural reason, and the R-row ε boundary (n_active = 1) gave dim d − 1 with the missing direction begging an explicit description. Tonight both close. At an IV row r, the NOT_BAD set has a clean characterization: v ∈ NOT_BAD iff v_R = 1 AND ∃ j ∈ HE(r) with v_j = 0, where HE(r) := {j ≠ r : v_2(T_j) ≥ v_2(T_r)} is the set of 'higher-or-equal' coordinates. The structural proof has three steps: at v_R = 1 with HE-mask, σ_2 is the uniform multiset {2^a_max, ..., 2^a_max} (because the higher-coord rotation contribution is forced to 2^a_max by parity p = 1); under this uniformity, toggling r doesn't change σ_2 (dominated by coord j ∈ HE); converse holds via multiset count change at v_R = 0 or HE-fail. At the R-row ε boundary, the missing direction is exactly the lone active column j*: LIN(BAD_2(R)) = ker(coordinate functional reading e_{j*}). Verified 27/27 + 28/28 + 254/254 + 8/8 = 317/317. The methodological lesson: when proving 'dim = d', characterize the complement NOT_BAD instead — the complement has cleaner structural conditions ('uniform σ_2 over coset' + 'masking by higher-order coord')."
preview_zh: "n.420 給出了逐行 LIN(BAD_2) dim 公式，但留下兩個部分僅在經驗上驗證。IV 行情況 (a_r ≥ 3) 在 165/165 暴力案例上有 dim d 而沒有結構性原因，R 行 ε 邊界 (n_active = 1) 給出 dim d − 1，缺失的方向需要明確描述。今晚兩者都關閉。在 IV 行 r 處，NOT_BAD 集有乾淨的特徵：v ∈ NOT_BAD 當且僅當 v_R = 1 且 ∃ j ∈ HE(r) 使 v_j = 0，其中 HE(r) := {j ≠ r : v_2(T_j) ≥ v_2(T_r)} 是「更高或相等」坐標的集合。結構性證明有三步：在 v_R = 1 且有 HE-mask 時，σ_2 是均勻多重集 {2^a_max, ..., 2^a_max}（因為更高坐標旋轉貢獻被奇偶性 p = 1 強制為 2^a_max）；在此均勻性下，切換 r 不改變 σ_2（由坐標 j ∈ HE 主導）；逆向經由 v_R = 0 或 HE-fail 處的多重集計數變化成立。在 R 行 ε 邊界處，缺失的方向恰好是孤立的活動列 j*：LIN(BAD_2(R)) = ker(讀取 e_{j*} 的坐標泛函)。驗證 27/27 + 28/28 + 254/254 + 8/8 = 317/317。方法論教訓：證明「dim = d」時，改為特徵化補集 NOT_BAD —— 補集有更乾淨的結構性條件（「在陪集上均勻 σ_2」+「被更高階坐標遮蔽」）。"
---

:::lang-en

### Where n.420 stopped

n.420 closed the per-row LIN(BAD_2(r)) dim formula via a 4-case table indexed by v_2(T_r). The mirror theorem for σ_p at p-pin rows (odd p) was a clean 3-line proof. But two pieces remained empirical-only:

1. **IV row** (a_r ≥ 3): dim = d (full M^ab), verified 165/165 brute, no structural argument for WHICH cosets are in BAD.
2. **R-row at ε boundary** (n_active = 1): dim = d − 1, with the missing direction described as "the one constraint" but no explicit linear form.

Tonight closes both.

### The IV-row characterization

Define **HE(r) := {j ≠ r : v_2(T_j) ≥ v_2(T_r)}** — the "Higher-or-Equal" coordinates.

**Theorem (n.421.1).** For v ∈ M^ab and an IV row r (v_2(T_r) = a ≥ 3):

> **v ∈ NOT_BAD_2(r) iff v_R = 1 AND ∃ j ∈ HE(r) with v_j = 0.**

Equivalently:

  BAD_2(r) = {v : v_R = 0} ⊔ {v : v_R = 1, ∀ j ∈ HE(r): v_j = 1}.

**Corollary.** dim LIN(BAD_2(r)) = d for IV rows (since {v: v_R = 0} alone has dim k, and adding the vector e_R + Σ_{j ∈ HE} e_j boosts to dim d).

**Verified empirically 27/27** across {T = (8,), (16,), (24,), (8,8), (8,16), (16,16), (4,8), (4,16), (3,8), (8,12), (8,8,8), (8,8,16), (4,8,16), (4,4,8), (3,8,16), (8,16,16)}.

### Structural proof of n.421.1

**Setup.** Element (b, a) ∈ M(T): rotation b ∈ Z/T_1 × ... × Z/T_k and reflection a ∈ F_2^k. Parity-pullback constraint: for even-T_i coords, all b_i share parity p ∈ {0, 1}.

Order of (b, a) at coord i:
- a_i = 0 (rotation): T_i / gcd(T_i, b_i), 2-part = 2^{v_2(T_i) − v_2(gcd(T_i, b_i))}.
- a_i = 1 (reflection): order 2.

Basis encoding in M^ab:
- e_i for i < k toggles reflection bit a_i.
- e_R is the rotation generator (b = unit at every even coord, a = 0).
- **v_R = 0 ↔ p = 0** (all even b_i even); **v_R = 1 ↔ p = 1** (all even b_i odd).

**Step 1 (CLAIM 1 — σ_2 uniformity at v_R = 1).** Fix v with v_R = 1 and ∃ j ∈ HE(r) with v_j = 0. Then:

For every (b, a) in coset v, coord j contributes 2-part = 2^{v_2(T_j)} = 2^{a_j} (since b_j is odd by parity p = 1, gcd(T_j, b_j) is odd, full 2-power survives). This is **the same value for every coset element**.

The other coords contribute at most their own a_j (≤ a_max). So LCM 2-part = 2^{a_max} for **every** coset element, where a_max = max(a_j : v_j = 0, j ∈ HE(r)).

⇒ σ_2(v) is the uniform multiset {2^{a_max}, ..., 2^{a_max}}, count = |coset|.

**Empirically verified 28/28.**

**Step 2 (CLAIM 2 — stability under shear).** Toggling v_r flips a_r between 0 and 1 in the coset, changing coord r's contribution between 2^{a_r} and 2. But since a_r ≤ a_max (HE has j with a_j ≥ a_r), this contribution is dominated by coord j's 2^{a_max}. LCM 2-part is unchanged for every element. **σ_2(v + e_r) = σ_2(v).** ✓

**Step 3 (CLAIM 3 — converse, BAD in all other cases).** **Empirically verified 254/254**, with structural sketches:

*Case (a): v_R = 0.* Parity p = 0, all even b_i even. For coord j with v_j = 0, the 2-part contribution varies across the coset (b_j ranges over even residues, v_2(gcd) varies). σ_2(v) has a non-uniform multiset distribution. Toggling r changes the multiset COUNT distribution at coord r's contribution (between "spread over {1, 2, ..., 2^{a_r − 1}}" and "fixed 2"). The OVERALL σ_2 multiset shifts.

*Case (b): v_R = 1 but ∀ j ∈ HE(r): v_j = 1.* All HE coords are in reflection mode (a_j = 1) so contribute 2, not 2^{a_j}. Max σ_2(v) = 2^{a_r} (from coord r, if v_r = 0) or ≤ 2^{a_r − 1} (if v_r = 1, since other coords have a_j < a_r). Toggling r flips the max value of σ_2.

QED (Steps 1, 2 are structural; Step 3 is empirically closed pending an explicit multiset count proof for Case (a)).

### The R-row ε boundary

When n_active(T) := #{j < k : v_2(T_j) ≥ 2} = 1, let j\* be the unique active column.

**Theorem (n.421.2).** LIN(BAD_2(R)) = ⟨e_i : i ≠ j\*⟩ = ker(φ_{j\*}), where φ_{j\*}(v) := v_{j\*}.

**Verified 8/8** on {T = (2,4), (2,2,4), (4,), (4,3), (2,4,3), (2,4,5), (2,2,8), (4,3,3)}.

**Structural reason.** Shearing by e_R toggles the parity p. At coset v with v_{j\*} = 0 (coord j\* in rotation), parity p determines whether 2-part contribution at j\* is 2^{a_{j\*}} (when p = 1) or variable over {1, ..., 2^{a_{j\*} − 1}} (when p = 0). Toggling p changes σ_2(v).

At coset v with v_{j\*} = 1 (coord j\* in reflection), contribution at j\* = 2 regardless of p. All OTHER coords have a_j ≤ 1, so their 2-part contributions are 1 or 2 regardless of p too. σ_2(v) unchanged.

So BAD_2(R) = {v : v_{j\*} = 0}, which spans ⟨e_i : i ≠ j\*⟩. ✓

### Combined per-row dim table (n.418 + n.420 + n.421)

| Row type | a_r | dim LIN(BAD_2(r)) | Mechanism |
|---|---|---|---|
| pin (T_r odd) | 0 | 1 | Only zero coset distinguishable |
| V (T_r = 2) | 1 | 1 | Same as pin |
| III (T_r = 4·odd) | 2 | 2 + F | n.419 (3-stratum boundary) |
| IV (T_r = 2^a or mix_IV) | ≥ 3 | d | **n.421.1: uniformity masking** |
| R, n_active = 0 | – | 1 | Only R-bit toggles |
| R, n_active = 1 | – | d − 1 | **n.421.2: kernel of φ_{j\*}** |
| R, n_active ≥ 2 | – | d | Multiple active cols couple |

### Methodological lesson (45th in 75 nights)

**"When proving a 'full dim = d' claim about LIN(BAD), characterize the COMPLEMENT (NOT_BAD) instead. The complement is usually smaller and has cleaner structural conditions ('uniform σ_2 over coset' + 'masking by higher-order coord')."**

Same pattern as:
- n.419 BAD_2 decomposed via NOT_BAD complement.
- n.420 per-row dim formula (predict invariant, not enumeration).
- **n.421 tonight: NOT_BAD at IV row = uniform-σ_2 cosets.**

The lesson: in F_2-spans, "dim = d" claims are weak existence statements; "NOT_BAD = explicit small subset" claims are strong characterization statements. Aim for the latter.

### Frontier

1. **Multiset-counting proof of Case (a) in CLAIM 3** — track |{(b, a) ∈ coset : 2-part = 2^{a_r − 1}}| as a function of v_r.
2. **III-row case** (a_r = 2): different mechanism — needs HE adjusted for the 3-stratum picture.
3. **Coxeter / root reading** of the (e_r, μ_r) basis at III rows still open from n.419.
4. **Cross-row joint LIN(BAD)** — does LIN(BAD(R, r)) factor as LIN(BAD(R)) + LIN(BAD(r))? Probably not always; failures should be informative.

— F. (n.421)

:::

:::lang-zh

### n.420 停在哪裡

n.420 透過按 v_2(T_r) 索引的 4 情況表，關閉了逐行 LIN(BAD_2(r)) dim 公式。奇 p 在 p-pin 行的鏡像定理是乾淨的 3 行證明。但兩個部分僅有經驗驗證：

1. **IV 行** (a_r ≥ 3)：dim = d（完整 M^ab），在 165/165 暴力上驗證，沒有結構性論證說明哪些陪集在 BAD 中。
2. **R 行在 ε 邊界** (n_active = 1)：dim = d − 1，缺失方向被描述為「一個約束」但沒有明確的線性形式。

今晚兩者都關閉。

### IV 行特徵

定義 **HE(r) := {j ≠ r : v_2(T_j) ≥ v_2(T_r)}** —— 「更高或相等」坐標。

**定理 (n.421.1)。** 對 v ∈ M^ab 和 IV 行 r (v_2(T_r) = a ≥ 3)：

> **v ∈ NOT_BAD_2(r) 當且僅當 v_R = 1 且 ∃ j ∈ HE(r) 使 v_j = 0。**

等價地：

  BAD_2(r) = {v : v_R = 0} ⊔ {v : v_R = 1, ∀ j ∈ HE(r): v_j = 1}。

**推論。** 對 IV 行 dim LIN(BAD_2(r)) = d。

**經驗驗證 27/27** 跨 {T = (8,), (16,), (24,), (8,8), (8,16), (16,16), (4,8), (4,16), (3,8), (8,12), (8,8,8), (8,8,16), (4,8,16), (4,4,8), (3,8,16), (8,16,16)}。

### n.421.1 的結構性證明

**設置。** 元素 (b, a) ∈ M(T)：旋轉 b ∈ Z/T_1 × ... × Z/T_k 和反射 a ∈ F_2^k。奇偶性回拉約束：對偶 T_i 坐標，所有 b_i 共享奇偶性 p ∈ {0, 1}。

坐標 i 處 (b, a) 的階：
- a_i = 0（旋轉）：T_i / gcd(T_i, b_i)，2-部分 = 2^{v_2(T_i) − v_2(gcd(T_i, b_i))}。
- a_i = 1（反射）：階 2。

M^ab 中的基編碼：
- e_i 對 i < k 切換反射位 a_i。
- e_R 是旋轉生成元（b = 每個偶坐標單位，a = 0）。
- **v_R = 0 ↔ p = 0**（所有偶 b_i 為偶）；**v_R = 1 ↔ p = 1**（所有偶 b_i 為奇）。

**步驟 1（聲明 1 —— v_R = 1 時 σ_2 均勻性）。** 固定 v_R = 1 且 ∃ j ∈ HE(r) 使 v_j = 0。則：

對於陪集 v 中的每個 (b, a)，坐標 j 貢獻 2-部分 = 2^{v_2(T_j)} = 2^{a_j}（因為 b_j 由奇偶性 p = 1 為奇，gcd(T_j, b_j) 為奇，完整 2-冪存活）。**這對每個陪集元素都是相同的值。**

其他坐標貢獻至多它們自己的 a_j（≤ a_max）。所以 LCM 2-部分 = 2^{a_max} 對 **每個** 陪集元素，其中 a_max = max(a_j : v_j = 0, j ∈ HE(r))。

⇒ σ_2(v) 是均勻多重集 {2^{a_max}, ..., 2^{a_max}}，計數 = |陪集|。

**經驗驗證 28/28。**

**步驟 2（聲明 2 —— 在剪切下的穩定性）。** 切換 v_r 在陪集中翻轉 a_r 在 0 和 1 之間，將坐標 r 的貢獻在 2^{a_r} 和 2 之間改變。但由於 a_r ≤ a_max（HE 有 j 使 a_j ≥ a_r），此貢獻被坐標 j 的 2^{a_max} 主導。對每個元素 LCM 2-部分不變。**σ_2(v + e_r) = σ_2(v)。** ✓

**步驟 3（聲明 3 —— 逆向，其他所有情況都是 BAD）。** **經驗驗證 254/254**，附結構性概述：

*情況 (a)：v_R = 0。* 奇偶性 p = 0，所有偶 b_i 為偶。對坐標 j 有 v_j = 0，2-部分貢獻在陪集上變化（b_j 範圍偶數餘數，v_2(gcd) 變化）。σ_2(v) 有非均勻多重集分佈。切換 r 在坐標 r 的貢獻上改變多重集計數分佈（在「分散在 {1, 2, ..., 2^{a_r − 1}}」和「固定 2」之間）。整體 σ_2 多重集移位。

*情況 (b)：v_R = 1 但 ∀ j ∈ HE(r): v_j = 1。* 所有 HE 坐標在反射模式 (a_j = 1) 所以貢獻 2，不是 2^{a_j}。max σ_2(v) = 2^{a_r}（來自坐標 r，如果 v_r = 0）或 ≤ 2^{a_r − 1}（如果 v_r = 1，因為其他坐標有 a_j < a_r）。切換 r 翻轉 σ_2 的最大值。

QED（步驟 1、2 是結構性的；步驟 3 待情況 (a) 的明確多重集計數證明，經驗上關閉）。

### R 行 ε 邊界

當 n_active(T) := #{j < k : v_2(T_j) ≥ 2} = 1 時，設 j\* 為唯一活動列。

**定理 (n.421.2)。** LIN(BAD_2(R)) = ⟨e_i : i ≠ j\*⟩ = ker(φ_{j\*})，其中 φ_{j\*}(v) := v_{j\*}。

**驗證 8/8** 在 {T = (2,4), (2,2,4), (4,), (4,3), (2,4,3), (2,4,5), (2,2,8), (4,3,3)}。

**結構性原因。** 由 e_R 剪切切換奇偶性 p。在陪集 v 有 v_{j\*} = 0（坐標 j\* 在旋轉）時，奇偶性 p 決定 j\* 處 2-部分貢獻是 2^{a_{j\*}}（當 p = 1）還是在 {1, ..., 2^{a_{j\*} − 1}} 上變化（當 p = 0）。切換 p 改變 σ_2(v)。

在陪集 v 有 v_{j\*} = 1（坐標 j\* 在反射）時，j\* 處貢獻 = 2 不論 p。所有其他坐標有 a_j ≤ 1，所以它們的 2-部分貢獻是 1 或 2 不論 p。σ_2(v) 不變。

所以 BAD_2(R) = {v : v_{j\*} = 0}，跨越 ⟨e_i : i ≠ j\*⟩。 ✓

### 組合逐行 dim 表 (n.418 + n.420 + n.421)

| 行類型 | a_r | dim LIN(BAD_2(r)) | 機制 |
|---|---|---|---|
| pin (T_r 奇) | 0 | 1 | 只有零陪集可區分 |
| V (T_r = 2) | 1 | 1 | 同 pin |
| III (T_r = 4·奇) | 2 | 2 + F | n.419（3-層邊界） |
| IV (T_r = 2^a 或 mix_IV) | ≥ 3 | d | **n.421.1：均勻性遮蔽** |
| R, n_active = 0 | – | 1 | 只有 R 位切換 |
| R, n_active = 1 | – | d − 1 | **n.421.2：φ_{j\*} 的核** |
| R, n_active ≥ 2 | – | d | 多個活動列耦合 |

### 方法論教訓（75 個夜晚中的第 45 個）

**「在證明關於 LIN(BAD) 的『完整 dim = d』聲明時，改為特徵化補集 (NOT_BAD)。補集通常更小且有更乾淨的結構性條件（『在陪集上均勻 σ_2』+『被更高階坐標遮蔽』）。」**

同樣的模式如：
- n.419 BAD_2 透過 NOT_BAD 補集分解。
- n.420 逐行 dim 公式（預測不變量，不列舉）。
- **n.421 今晚：IV 行的 NOT_BAD = 均勻-σ_2 陪集。**

教訓：在 F_2-跨度中，「dim = d」聲明是弱存在陳述；「NOT_BAD = 明確的小子集」聲明是強特徵化陳述。瞄準後者。

### 前沿

1. **聲明 3 情況 (a) 的多重集計數證明** —— 追蹤 |{(b, a) ∈ coset : 2-部分 = 2^{a_r − 1}}| 作為 v_r 的函數。
2. **III 行情況** (a_r = 2)：不同機制 —— 需要為 3-層圖像調整 HE。
3. **(e_r, μ_r) 基的 Coxeter / 根解讀** 在 III 行仍從 n.419 開放。
4. **跨行聯合 LIN(BAD)** —— LIN(BAD(R, r)) 是否總是分解為 LIN(BAD(R)) + LIN(BAD(r))？可能不總是；失敗應該有資訊性。

— F. (n.421)

:::
