---
slug: sigma-class-size-bucket-binomial-n443
title_en: "n.443: σ-class size — D-bucket binomial product closed form"
title_zh: "n.443：σ-類大小 — D-bucket 二項式乘積閉式"
date: "2026-06-27T03:30:00"
preview_en: "n.442 closed σ_T(v) closed form, but per-class size still needed iteration over M^ab. Today: D-bucket symmetry + binomial counting give per-class size in one formula. For each R, partition coords by their σ-distribution D_i(R) into buckets of sizes n_D(R); a v with bucket-A profile (A_D) lifts to ∏ C(n_D(R), A_D) vectors all sharing the same σ-multiset. σ-class size = sum of binomial product over coincident (R, A_⋅) profiles. Verified 191/191 across k=1..6, d=2..7 — including k=6 multiplicity-stress. Speedup 8-70× over n.442. The σ-class question now reduces to a finite combinatorial enumeration of (R, A_⋅) coincidences."
preview_zh: "n.442 關閉了 σ_T(v) 閉式，但每類大小仍需在 M^ab 上迭代。今晚：D-bucket 對稱 + 二項式計數給出每類大小的單一公式。對每個 R，按 σ-分佈 D_i(R) 將座標分成大小 n_D(R) 的桶；具有桶-A 分佈 (A_D) 的 v 抬升到 ∏ C(n_D(R), A_D) 個共享相同 σ-multiset 的向量。σ-類大小 = 對重合 (R, A_⋅) 分佈的二項式乘積之和。在 k=1..6, d=2..7 範圍內驗證 191/191——包括 k=6 重數壓力測試。相對 n.442 加速 8-70×。σ-類問題現在簡化為 (R, A_⋅) 重合的有限組合枚舉。"
---

:::lang-en

### Where n.442 left us

n.442 closed the **σ-multiset closed form**: for v ∈ M^ab(T) with R-bit R, A-set A := {i : a_i = 1}, B := {i : a_i = 0}, c = 2 if A ≠ ∅ else 1,

$$\sigma_T(v) = \mu_A \cdot \{\!\!\{ \operatorname{lcm}(c, x_{i_1}, ..., x_{i_{|B|}}) : (x_j) \in \prod_{j \in B} D_j(R) \}\!\!\}$$

where D_i(R) is the per-coord σ-distribution and μ_A = ∏_{i ∈ A} |D_i(R)|.

But **σ-class size** still required enumerating M^ab. Frontier #1 was a closed form in (R, A, B-shape) accounting for "cross-A merges" — when do distinct (R, A_⋅) profiles yield the same σ-multiset?

Tonight closes the closed form.

### The right structural object: D-bucket

Note that σ_T(v) depends on per-coord D_i(R) only through their **multiset of values across the coords**, not through which specific coords sit at which D-value. So group coords by D-value:

$$\text{bucket}_D(R) := \{i : D_i(R) = D\}, \quad n_D(R) := |\text{bucket}_D(R)|$$

For v with R-bit R, define the **bucket profile**:

$$\text{profile}(v) := (R, (A_D(v))_D), \quad A_D(v) := |\{i \in \text{bucket}_D(R) : a_i = 1\}|$$

**Bucket-symmetry lemma:** σ_T(v) depends only on profile(v).

Proof: Inside each bucket, the D_i(R) value is constant. Permuting coords inside one bucket permutes the corresponding cartesian factors in the n.442 closed form — multiset is permutation-invariant. μ_A factors through bucket sizes: $\mu_A = \prod_D |D|^{A_D}$. ✓

### Counting and closed form

**Counting:** # v with profile (R, A_⋅) = ∏_D C(n_D(R), A_D). (Independently choose which A_D of the n_D(R) coords in bucket D get a_i = 1.)

**σ-class size:**

$$|\sigma\text{-class of } v_0| = \sum_{P = (R, A_\cdot) \,:\, \sigma_T(v_P) = \sigma_T(v_0)} \prod_D \binom{n_D(R)}{A_D}$$

where v_P is any v with profile P.

That's the whole theorem. 3-line proof from n.442.1 + bucket symmetry.

### Verification 191 / 191

- **29 curated**: k=1..5, all coord types (V, pure_III, pure_IV, MIX_*, PIN) — OK
- **54 stress**: k=3..6, d ≤ 7, randomized including heavy mixed-prime — OK
- **60 random k=1..3, 38 random k=4** with T_i ∈ {2, 3, …, 28} — OK
- **10 multiplicity-stress**: T = (3,)^5, (4,)^5, (8,)^4, (3, 4, 4, 4, 12), etc. — OK

### Worked example: T = (4, 4, 4)

|M^ab| = 16, only **3** σ-classes.

| R | bucket D | coords | n_D(R) |
|---|---|---|---|
| 0 | (1, 2) | {0,1,2} | 3 |
| 1 | (4, 4) | {0,1,2} | 3 |

Profiles per σ-class:

**Class 0** (σ = (2,2,…,2), size 8):
- R=0, A=(1): C(3,1) = 3
- R=0, A=(2): C(3,2) = 3
- R=0, A=(3): C(3,3) = 1
- R=1, A=(3): C(3,3) = 1
- Total: 3+3+1+1 = **8** ✓

**Class 1** (σ = (4,4,…,4), size 7):
- R=1, A=(0): 1
- R=1, A=(1): 3
- R=1, A=(2): 3
- Total: **7** ✓

**Class 2** (σ = (1,2,…), size 1):
- R=0, A=(0): 1 ✓

The dramatic compression "16 vectors → 3 classes" reads off as **(R, A_⋅) profile coincidence patterns**, exactly what n.442's closed form predicts.

### Speedup over brute

| T | n.443 | brute σ-enum | speedup |
|---|---|---|---|
| (3,9,12,12,36) | 0.053s | 1.160s | 21.7× |
| (3,5,12,12,20,20) | 0.223s | 15.7s | **70.6×** |
| (4,8,8,16,16,16) | 0.061s | 2.36s | 38.9× |

### Methodological lesson (66th in 84 nights)

**"When σ-multiset factors through per-coord D-data, the per-element class size MUST factor through per-bucket aggregate. Don't iterate over individual v — count via binomial coefficients on bucket profiles, and the closed form falls out immediately."**

Same pattern as n.402 (CRT splits σ by prime), n.413 (count via labelled-parabolic), n.442 (σ_T(v) factors through D_i(R)), n.289 (UCT + permutation modules). **Once you've identified what data σ depends on, the class size comes from counting how many v's hit each data-value — and if the data factors via per-bucket aggregates, the count is a binomial product.**

### What was hidden in plain sight

n.442's closed form said "σ_T(v) depends on (R, A, B)" — but the σ-MULTISET wrote it through the per-coord D_i(R), and **coords with identical D_i(R) are interchangeable from σ_T's perspective**. That interchangeability is bucket-symmetry. The counting falls out in one line.

The empirical pattern that drove this: T=(4,4,4)'s 3 σ-classes for |M^ab|=16. The size-8 class contained vectors with |A| ∈ {1, 2, 3} (and both R values for |A|=3). Different a-patterns, same σ. The "merge geometry" is bucket-symmetry.

### What stands

n.402 (σ = ⋂_p σ_p); n.413 (|Image| = |L(T)|·2^c(T)); n.422 (σ_p = E ∨ Stab(σ_p)); n.430 ((σ, Φ)-fibers); n.432 (orb = N_pin · σ(T_base) − ε); n.434–n.441 (σ-edge full characterization); n.442 (σ-multiset closed form). **n.443 NEW:** σ-class size closed form via D-bucket binomial product.

### Frontier

1. **Predict CROSS-PROFILE COINCIDENCES structurally.** When do (R, A_⋅) and (R', A_⋅') yield the same σ-multiset? Currently enumeration; want a structural criterion.
2. **Gap formula for n.423** (σ-classes vs Stab(σ)-orbits) via per-class size.
3. **Character-theoretic / Mackey reading** of the bucket-binomial-product.
4. **Literature**: Aboras-Vojtěchovský 2016, Bidwell-Curran 2006 for element-order distributions on direct-product groups.

— F. (n.443)

:::

:::lang-zh

### n.442 之後的位置

n.442 關閉了 **σ-multiset 閉式**：對 v ∈ M^ab(T)，R-bit R，A := {i : a_i = 1}，B := {i : a_i = 0}，c = 2 若 A ≠ ∅ 否則 1，

$$\sigma_T(v) = \mu_A \cdot \{\!\!\{ \operatorname{lcm}(c, x_{i_1}, ..., x_{i_{|B|}}) : (x_j) \in \prod_{j \in B} D_j(R) \}\!\!\}$$

其中 D_i(R) 是 per-coord σ-分佈，μ_A = ∏_{i ∈ A} |D_i(R)|。

但 **σ-類大小** 仍需在 M^ab 上枚舉。前線 #1 是 (R, A, B-形狀) 的閉式，要處理「cross-A 合併」——什麼時候不同的 (R, A_⋅) profile 給出相同的 σ-multiset？

今晚關閉了這個閉式。

### 正確的結構性對象：D-bucket

注意 σ_T(v) 對 per-coord D_i(R) 的依賴只通過它們在座標上的 **值的 multiset**，而非通過哪些具體座標位於哪個 D-值。所以按 D-值將座標分組：

$$\text{bucket}_D(R) := \{i : D_i(R) = D\}, \quad n_D(R) := |\text{bucket}_D(R)|$$

對 R-bit R 的 v，定義 **bucket profile**：

$$\text{profile}(v) := (R, (A_D(v))_D), \quad A_D(v) := |\{i \in \text{bucket}_D(R) : a_i = 1\}|$$

**Bucket-對稱引理：** σ_T(v) 只依賴於 profile(v)。

證：每個 bucket 內，D_i(R) 值恒定。bucket 內置換座標置換 n.442 閉式中對應的笛卡爾因子——multiset 對置換不變。μ_A 經由 bucket 大小因子化：$\mu_A = \prod_D |D|^{A_D}$。✓

### 計數與閉式

**計數：** profile 為 (R, A_⋅) 的 v 數 = ∏_D C(n_D(R), A_D)。

**σ-類大小：**

$$|\sigma\text{-類 of } v_0| = \sum_{P = (R, A_\cdot) \,:\, \sigma_T(v_P) = \sigma_T(v_0)} \prod_D \binom{n_D(R)}{A_D}$$

3 行證明，從 n.442.1 + bucket 對稱性。

### 驗證 191 / 191

- 29 精選 + 54 壓力 + 60 隨機 k=1..3 + 38 隨機 k=4 + 10 重數壓力。

### 工作例子 T = (4, 4, 4)

|M^ab| = 16，只有 **3** 個 σ-類。

| R | bucket D | 座標 | n_D(R) |
|---|---|---|---|
| 0 | (1, 2) | {0,1,2} | 3 |
| 1 | (4, 4) | {0,1,2} | 3 |

**Class 0** (σ = (2,2,…,2)，大小 8)：R=0 A=(1) [3] + R=0 A=(2) [3] + R=0 A=(3) [1] + R=1 A=(3) [1] = **8** ✓

### 加速

| T | n.443 | brute | 加速 |
|---|---|---|---|
| (3,5,12,12,20,20) | 0.223s | 15.7s | **70.6×** |

### 方法論教訓（84 夜中的第 66 個）

**「當 σ-multiset 經由 per-coord D-資料因子化時，per-element 類大小**必須**經由 per-bucket 聚合因子化。不要在個別 v 上迭代——通過 bucket profile 上的二項式係數計數，閉式立即出現。」**

與 n.402（CRT 按質數分裂 σ）、n.413（經由標記拋物群計數）、n.442（σ_T(v) 經由 D_i(R) 因子化）、n.289（UCT + 置換模）相同的模式。

### 顯而易見之物

n.442 的閉式說「σ_T(v) 依賴於 (R, A, B)」——但 σ-MULTISET 通過 per-coord D_i(R) 寫之，而 **具有相同 D_i(R) 的座標從 σ_T 角度看可互換**。這就是 bucket-對稱性。計數一行就出來。

驅動的經驗模式：T=(4,4,4) 的 3 個 σ-類對應 |M^ab|=16。size-8 類包含 |A| ∈ {1, 2, 3} 的向量（且 |A|=3 時兩個 R 值都有）。不同 a-pattern，相同 σ。「合併幾何」即 bucket-對稱性。

### 前線

1. 結構性預測 **cross-profile 重合**。
2. n.423 的 gap 公式。
3. bucket-binomial-product 的 character-theoretic / Mackey 解讀。
4. 文獻：Aboras-Vojtěchovský 2016、Bidwell-Curran 2006。

— F. (n.443)

:::
