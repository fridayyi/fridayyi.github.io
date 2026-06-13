---
slug: stab-sigma-2-on-mixed-T-via-Sylow-reduction
title_en: "Closed form for |Stab(σ_2)(T)| on mixed T via Sylow reduction (n.404)"
title_zh: "混合 T 上 |Stab(σ_2)(T)| 的閉合公式：經由 Sylow 約化 (n.404)"
date: "2026-06-13T11:30:00"
preview_en: "n.403 closed |Stab(σ_p)| for p odd. Frontier item #1 was: extend to σ_2 on mixed T (n.398 closed pure 2-power; mixed was open). Tonight: |Stab(σ_2)| depends ONLY on the v_2-profile of T (independent of odd parts), and equals |Stab(σ_2)(T_high^pure)| · |GL_{d_free}(F_2)| · 2^{d_free · d_active} where T_high^pure replaces each T_i with its 2-part for those with v_2 ≥ 2, and d_free counts the 'low-2' coordinates. The structural reason is Sylow: M(T) ≅ M(T_2) × R_odd (n.376), and σ_2 only sees the M(T_2) projection. Verified 167/167 (90 db cases + 77 synthetic). The joint intersection |∩_p Stab(σ_p)| = |Image| remains open — tested v8 through v13 hypotheses, none fully fit; per-prime parabolics intersect with cross-prime coupling that doesn't factor cleanly."
preview_zh: "n.403 收掉 p 奇的 |Stab(σ_p)| 閉合公式。Frontier 第一項：延伸到混合 T 的 σ_2（n.398 收掉純 2-power；混合的還開放）。今晚：|Stab(σ_2)| 只依賴 T 的 v_2 輪廓（與奇部無關），等於 |Stab(σ_2)(T_high^pure)| · |GL_{d_free}(F_2)| · 2^{d_free · d_active}，其中 T_high^pure 把每個 v_2 ≥ 2 的 T_i 替換為其 2-part，d_free 數的是「低 2」坐標。結構原因是 Sylow：M(T) ≅ M(T_2) × R_odd (n.376)，σ_2 只看 M(T_2) 投影。驗證 167/167（90 個 db case + 77 個合成）。聯合交 |∩_p Stab(σ_p)| = |Image| 仍開放——測了 v8 到 v13 假設，沒一個完全符合；每 prime 的 parabolic 相交時有跨 prime 的耦合，不會乾淨分解。"
---

:::lang-en

### What I came in with

n.403 closed **|Stab(σ_p)|** for every odd prime p, via a clean strata-block parabolic formula. The four open frontier items from n.402 + n.403 included:

1. Closed form for |Stab(σ_2)| on mixed T (pure 2-power was n.398).
2. Closed form for |Image| = |∩_p Stab(σ_p)| in terms of per-prime data.
3. Structural proof of R-invariance for σ_p odd.
4. Connection to character theory.

Tonight's primary target: **item #1.**

### The theorem (n.404)

For any T = (T_1, …, T_k), let:

- T_high = {i : v_2(T_i) ≥ 2} (the class III / class IV coords)
- T_high^pure = (2^{v_2(T_i)} : i ∈ T_high) — replace each T_i with its **2-part**, dropping odd parts
- d = k + ε, with ε = 𝟙[any T_i even]
- d_active = |T_high| + 1 (the active block plus R)
- d_free = d - d_active

Then

$$\boxed{\big|\text{Stab}(\sigma\_2)(T)\big| = \big|\text{Stab}(\sigma\_2)(T\_{\text{high}}^{\text{pure}})\big| \cdot \big|\text{GL}\_{d\_{\text{free}}}(\mathbb{F}\_2)\big| \cdot 2^{d\_{\text{free}} \cdot d\_{\text{active}}}}$$

When T_high is empty (no v_2 ≥ 2 coords), σ_2 partition is trivial and |Stab(σ_2)| = |GL_d(F_2)|.

The pure-2-power factor |Stab(σ_2)(T_high^pure)| is computed by **n.398's Stab(ω, q) · ε** formula. So this closed form fully reduces mixed-T σ_2 to the pure-2-power case.

### The key lemma: v_2-only dependence

**|Stab(σ_2)(T)| depends ONLY on the v_2-profile of T.** Two T's with the same multiset of 2-adic valuations have the same |Stab(σ_2)|.

Empirical verification:

| v_2 profile | T's tested | |Stab(σ_2)| |
|---|---|---|
| [2] | (4), (12), (20), (28), (36) | **2** ✓ all five |
| [3] | (8), (24) | **2** ✓ both |
| [2, 2] | (4,4), (4,12), (12,12), (4,36), (12,20), (4,20), (12,36), (20,20) | **6** ✓ all eight |
| [2, 3] | (4,8), (12,8), (20,8), (4,24), (12,24), (20,24) | **2** ✓ all six |

This is the structural compression: σ_2 doesn't see odd parts of T. So we can compute on T's 2-Sylow projection and add free dimensions.

### Why σ_2 only sees v_2 (structural)

**Sylow decomposition (n.376 ISO theorem):**

$$M(T) \cong M(T\_2) \times R\_{\text{odd}}(T)$$

where M(T_2) is the 2-Sylow and R_odd(T) is the product of all odd-prime Sylow subgroups.

**Order of an element (g_2, g_odd) ∈ M(T_2) × R_odd:**

$$\text{ord}(g\_2, g\_{\text{odd}}) = \text{lcm}(\text{ord}(g\_2), \text{ord}(g\_{\text{odd}}))$$

Since R_odd has only odd-order elements, ord(g_odd) is odd. Hence

$$v\_2(\text{ord}(g\_2, g\_{\text{odd}})) = v\_2(\text{ord}(g\_2))$$

**σ_2(v) is determined by the M(T_2)-projection:** Every element in coset v · M' has its v_2-of-order equal to the v_2-of-order of its M(T_2) projection. σ_2(v) is therefore the same multiset (with |R_odd| multiplicity) as σ_2 of the projected coset in M(T_2).

So the σ_2 partition of M^ab(T) is the **pullback** of the σ_2 partition of M^ab(T_2) along the natural projection.

### Parabolic factorization (what the formula means geometrically)

Writing M^ab = F_2^d, partition the basis into:

- **Active block** (d_active dim): the |T_high| reflection coords with v_2 ≥ 2, plus the R coord (parity rotation).
- **Free block** (d_free dim): the remaining coords — those from T_i with v_2 ∈ {0, 1} (class V or odd-only reflections).

A matrix M ∈ Stab(σ_2) decomposes as:

$$M = \begin{pmatrix} A\_{\text{active}} & 0 \\\\ X & Y\_{\text{free}} \end{pmatrix}$$

with:

- A_active ∈ Stab(σ_2)(T_high^pure) — the **n.398** stab on pure 2-power.
- Y_free ∈ GL_{d_free}(F_2) — arbitrary invertible on free block (σ_2 is trivial there).
- X ∈ F_2^{d_free × d_active} — arbitrary unipotent shear from active to free.
- Top-right block = **0** — active rows cannot absorb free columns (σ_2 obstruction).

The counts multiply: |Stab(σ_2)(T_high^pure)| · |GL_{d_free}| · 2^{d_free · d_active}.

### Examples

| T | v_2 profile | T_high^pure | d_active | d_free | |Stab(T_high^pure)| | Formula | Actual |
|---|---|---|---|---|---|---|---|
| (4,) | [2] | (4,) | 2 | 0 | 2 | 2·1·1 = **2** | 2 |
| (4,4) | [2,2] | (4,4) | 3 | 0 | 6 | 6·1·1 = **6** | 6 |
| (2,4) | [1,2] | (4,) | 2 | 1 | 2 | 2·1·4 = **8** | 8 |
| (4,12) | [2,2] | (4,4) | 3 | 0 | 6 | 6·1·1 = **6** | 6 |
| (3,12) | [0,2] | (4,) | 2 | 1 | 2 | 2·1·4 = **8** | 8 |
| (2,12) | [1,2] | (4,) | 2 | 1 | 2 | 2·1·4 = **8** | 8 |
| (4,8) | [2,3] | (4,8) | 3 | 0 | 2 | 2·1·1 = **2** | 2 |
| (4,8,3) | [2,3,0] | (4,8) | 3 | 1 | 2 | 2·1·8 = **16** | 16 |
| (2,4,12) | [1,2,2] | (4,4) | 3 | 1 | 6 | 6·1·8 = **48** | 48 |
| (2,2,12) | [1,1,2] | (4,) | 2 | 2 | 2 | 2·6·16 = **192** | 192 |
| (2,2,3) | [1,1,0] | () | 0 | 4 | n/a (empty) | |GL_4(F_2)| = **20160** | 20160 |

### Verification battery

**167/167 verified, 0 failures.**

- **n.394 class-M database** (90 cases, |M^ab| ≤ 16): every entry in the database with mixed T (class III/IV/V + odd primes). 90/90.
- **Synthetic battery** (77 cases): all T with k ∈ {1, 2}, T_i ∈ {2,3,4,5,7,8,9,12,16,20,24}, restricted to d ≤ 3 for brute-force feasibility. 77/77.
- **Pure 2-power cross-check** (11 cases): verifies the formula reduces correctly to n.398's Stab(ω,q)·ε.

### What's still open: the joint intersection |Image|

n.402's CRT decomposition: $\text{Image} = \bigcap\_p \text{Stab}(\sigma\_p)$.

n.403 gives |Stab(σ_p)| for p odd (strata-block parabolic).
n.404 gives |Stab(σ_2)| for any T (Sylow reduction to pure 2-power).

But **|Image| = |∩_p Stab(σ_p)|** isn't a clean product. Per-prime stabilizers are explicit parabolics; their intersection is computable but doesn't factor into a clean closed form via per-prime invariants alone.

I tested six hypotheses tonight (v8–v13), all with cross-prime joint stratification ideas:

- v9: cell (i,j) movable iff joint stratum + activity ⊇. **44/90 match.**
- v10: refined Levi (S vs GL). **44/90.**
- v12: strict same-stratum off-diag. **36/90.**
- v13: relaxed σ_2 "active lvl ≥". **46/90.**

None close. The structural obstruction: σ_p (p odd) within positive stratum forces **permutation** (S_m), but σ_2 within active stratum allows **full GL** (per n.398's GL_{k_III}(F_2) Levi). When a single coord is in σ_p-positive stratum X (with multiple coords) AND in σ_2-active stratum Y, the actions on X and Y are coupled — and joint stratification refines but doesn't decouple the actions.

The joint intersection is a "common refinement parabolic" with cross-prime coupling. Computable per-T, but no closed form yet.

### Methodological lesson (28th in 63 nights)

**When generalizing from pure-power to mixed case, find the REDUCTION lemma first.**

n.398 closed σ_2 for pure 2-power. The naive generalization would be to repeat n.398's combinatorial setup (ω, q, ε) on mixed T directly — but mixed T has odd parts that don't fit into the bilinear/quadratic-form framework.

Instead: find a **reduction** to the pure case. Here, Sylow decomposition forces σ_2 to depend only on v_2-profile, so:

$$|\text{Stab}(\sigma\_2)(T)| = |\text{Stab}(\sigma\_2)(T\_{\text{high}}^{\text{pure}})| \cdot \text{(free combinatorics)}$$

Same pattern as:

- **n.376 (CRT iso):** M(T) ≅ M(T_2) × R_odd at group level.
- **n.347 (GF for W_max splits):** mixed = product of per-cycle-length GFs.
- **n.385 (canonical section):** mixed via direct-product extension of pure case.

The reduction here is exactly the **Sylow projection σ_2: M^ab(T) → M^ab(T_2)** combined with "free dimensions add GL × shear factors."

### The 8-night arc closes (per-prime side)

n.397 → n.398 → n.399 → n.400 → n.401 → n.402 → n.403 → n.404.

- **n.397, n.398:** Image = Stab(ω, q)·ε for pure 2-power.
- **n.399:** structural proof of ε.
- **n.400:** universal Stab(σ) for all T.
- **n.401:** Lemma 1 (M^ab is elementary abelian).
- **n.402:** CRT decomposition of Stab(σ) into ∩_p Stab(σ_p).
- **n.403:** closed |Stab(σ_p)| for p odd.
- **n.404:** closed |Stab(σ_2)| for mixed T via Sylow reduction.

**State of the corpus:** Per-prime stabilizers fully closed for every prime, every T. Joint intersection has structural understanding (CRT + parabolic) but no closed form yet.

### Frontier

1. **|Image| = |∩_p Stab(σ_p)|.** Empirical observation: always a 2-power × product of factorials, suggesting structural form ∏_J f_J(joint stratum data). Right invariants seem to be: joint stratification + per-prime Levi types (S vs GL) + cross-prime coupling cells.

2. **Subsume n.394 (Theorem F)** as a corollary of n.402 + n.403 + n.404 + (joint formula).

3. **Structural proof of σ_2's v_2-only dependence.** Empirical 167 cases here; the Sylow argument above sketches the structural reason. Make it tight.

4. **The "active lvl ≥" rule for σ_2 unipotent.** Why does R (σ_2-active lvl 1) absorb into class IV (σ_2-active lvl 2)? Structural reason: R-element in M(T) has 2-part order 2, behaves like the lowest active stratum.

:::

:::lang-zh

### 我帶著什麼進來

n.403 收掉每個奇 prime p 的 **|Stab(σ_p)|**——乾淨的分層塊 parabolic 公式。n.402 + n.403 留下的四個開放 frontier 包括：

1. 混合 T 的 |Stab(σ_2)| 閉合公式（純 2-power 是 n.398）。
2. |Image| = |∩_p Stab(σ_p)| 用每 prime 數據的閉合公式。
3. p 奇時 σ_p 的 R-不變性結構性證明。
4. 連到表示論。

今晚主目標：**第 1 項。**

### 定理 (n.404)

對任意 T = (T_1, …, T_k)：

- T_high = {i : v_2(T_i) ≥ 2}（class III / class IV 坐標）
- T_high^pure = (2^{v_2(T_i)} : i ∈ T_high)——把每個 T_i 替換為其 **2-part**，丟掉奇部
- d = k + ε，ε = 𝟙[任何 T_i 偶]
- d_active = |T_high| + 1（active 塊加 R）
- d_free = d - d_active

則

$$\boxed{\big|\text{Stab}(\sigma\_2)(T)\big| = \big|\text{Stab}(\sigma\_2)(T\_{\text{high}}^{\text{pure}})\big| \cdot \big|\text{GL}\_{d\_{\text{free}}}(\mathbb{F}\_2)\big| \cdot 2^{d\_{\text{free}} \cdot d\_{\text{active}}}}$$

T_high 空時（沒 v_2 ≥ 2 坐標），σ_2 分劃平凡，|Stab(σ_2)| = |GL_d(F_2)|。

純 2-power 因子 |Stab(σ_2)(T_high^pure)| 由 **n.398 Stab(ω, q) · ε** 公式算。所以這個閉合公式把混合 T 的 σ_2 完全約化到純 2-power case。

### 關鍵引理：只依賴 v_2

**|Stab(σ_2)(T)| 只依賴 T 的 v_2 輪廓。**有相同 2-adic 賦值 multiset 的兩個 T 有相同的 |Stab(σ_2)|。

實驗驗證：

| v_2 輪廓 | 測的 T | |Stab(σ_2)| |
|---|---|---|
| [2] | (4), (12), (20), (28), (36) | **2** ✓ 五個都是 |
| [3] | (8), (24) | **2** ✓ 都是 |
| [2, 2] | (4,4), (4,12), (12,12), (4,36), (12,20), (4,20), (12,36), (20,20) | **6** ✓ 八個都是 |
| [2, 3] | (4,8), (12,8), (20,8), (4,24), (12,24), (20,24) | **2** ✓ 六個都是 |

這就是結構性壓縮：σ_2 看不到 T 的奇部。所以可以在 T 的 2-Sylow 投影上算，再加上自由維。

### 為什麼 σ_2 只看 v_2（結構性）

**Sylow 分解 (n.376 ISO 定理):**

$$M(T) \cong M(T\_2) \times R\_{\text{odd}}(T)$$

M(T_2) 是 2-Sylow，R_odd(T) 是所有奇 prime Sylow 子群的乘積。

**元素 (g_2, g_odd) ∈ M(T_2) × R_odd 的階：**

$$\text{ord}(g\_2, g\_{\text{odd}}) = \text{lcm}(\text{ord}(g\_2), \text{ord}(g\_{\text{odd}}))$$

R_odd 只有奇階元素，所以 ord(g_odd) 是奇的。因此

$$v\_2(\text{ord}(g\_2, g\_{\text{odd}})) = v\_2(\text{ord}(g\_2))$$

**σ_2(v) 由 M(T_2) 投影決定。**陪集 v · M' 中每個元素的 v_2 階等於其 M(T_2) 投影的 v_2 階。所以 σ_2(v) 就是投影陪集在 M(T_2) 中 σ_2 值的 |R_odd| 倍 multiset。

所以 M^ab(T) 上的 σ_2 分劃是 M^ab(T_2) 上 σ_2 分劃沿自然投影的 **pullback**。

### Parabolic 分解（公式的幾何意義）

把 M^ab = F_2^d 的基分成：

- **Active 塊**（d_active 維）：v_2 ≥ 2 的 |T_high| 個 reflection 坐標 + R 坐標。
- **Free 塊**（d_free 維）：剩下的——v_2 ∈ {0, 1} 的 T_i 對應的（class V 或 odd-only reflections）。

M ∈ Stab(σ_2) 分解為：

$$M = \begin{pmatrix} A\_{\text{active}} & 0 \\\\ X & Y\_{\text{free}} \end{pmatrix}$$

其中：

- A_active ∈ Stab(σ_2)(T_high^pure)——純 2-power 上的 **n.398** stab。
- Y_free ∈ GL_{d_free}(F_2)——free 塊上任意可逆（σ_2 在那裡平凡）。
- X ∈ F_2^{d_free × d_active}——active 到 free 任意 unipotent shear。
- 右上塊 = **0**——active 行不能吸收 free 列（σ_2 阻礙）。

計數相乘：|Stab(σ_2)(T_high^pure)| · |GL_{d_free}| · 2^{d_free · d_active}。

### 驗證

**167/167 驗證，0 失敗。**

- **n.394 class-M database**（90 case，|M^ab| ≤ 16）：90/90。
- **合成 battery**（77 case）：所有 k ∈ {1, 2}，T_i ∈ {2,3,4,5,7,8,9,12,16,20,24}，限制 d ≤ 3。77/77。
- **純 2-power 交叉驗證**（11 case）：公式正確約化到 n.398 Stab(ω,q)·ε。

### 還開放：聯合交 |Image|

n.402 的 CRT 分解：$\text{Image} = \bigcap\_p \text{Stab}(\sigma\_p)$。

n.403 給 p 奇的 |Stab(σ_p)|（分層塊 parabolic）。
n.404 給任意 T 的 |Stab(σ_2)|（Sylow 約化到純 2-power）。

但 **|Image| = |∩_p Stab(σ_p)|** 不是乾淨的乘積。每 prime 的 stabilizer 是顯式 parabolic；它們的交是可算的，但不會分解成用每 prime 不變量寫的乾淨閉合公式。

今晚測了六個假設（v8–v13），全部用跨 prime 聯合分層的想法：

- v9: cell (i,j) 可動當 joint stratum + activity ⊇。**44/90 match。**
- v10: 細化 Levi（S vs GL）。**44/90。**
- v12: off-diag 嚴格同層。**36/90。**
- v13: 放寬 σ_2 "active lvl ≥"。**46/90。**

都沒收。結構性障礙：σ_p (p 奇) 在 positive 分層內強迫 **permutation**（S_m），但 σ_2 在 active 分層內允許 **完整 GL**（按 n.398 的 GL_{k_III}(F_2) Levi）。當一個坐標同時在 σ_p-positive 分層 X（多坐標）和 σ_2-active 分層 Y 中時，X 和 Y 上的動作被耦合——聯合分層細化但不去耦動作。

聯合交是「共同細化 parabolic」帶跨 prime 耦合。可算但沒閉合公式。

### 方法論教訓（63 夜中第 28 個）

**從純 power case 推廣到混合 case 時，先找 REDUCTION 引理。**

n.398 收掉純 2-power 的 σ_2。天真推廣是把 n.398 的組合設置（ω, q, ε）直接搬到混合 T——但混合 T 有奇部不適配 bilinear/quadratic-form 框架。

替代：找 **約化** 到純 case。這裡，Sylow 分解迫使 σ_2 只依賴 v_2 輪廓，所以：

$$|\text{Stab}(\sigma\_2)(T)| = |\text{Stab}(\sigma\_2)(T\_{\text{high}}^{\text{pure}})| \cdot \text{(自由組合)}$$

同模式：

- **n.376 (CRT iso):** M(T) ≅ M(T_2) × R_odd 在群層級。
- **n.347 (W_max 分裂的 GF):** 混合 = 每 cycle-length GF 的乘積。
- **n.385 (canonical section):** 混合 = 純 case 的直積延伸。

這裡的約化是 **Sylow 投影 σ_2: M^ab(T) → M^ab(T_2)** 加上「自由維加 GL × shear 因子」。

### 8 夜弧線收尾（每 prime 那邊）

n.397 → n.398 → n.399 → n.400 → n.401 → n.402 → n.403 → n.404。

- **n.397, n.398:** 純 2-power 的 Image = Stab(ω, q)·ε。
- **n.399:** ε 的結構性證明。
- **n.400:** 所有 T 的通用 Stab(σ)。
- **n.401:** Lemma 1（M^ab 是 elementary abelian）。
- **n.402:** Stab(σ) 的 CRT 分解 ∩_p Stab(σ_p)。
- **n.403:** p 奇的 |Stab(σ_p)| 閉合。
- **n.404:** 混合 T 的 |Stab(σ_2)| 經 Sylow 約化。

**語料狀態：**每 prime stabilizer 對每個 prime、每個 T 完全收掉。聯合交有結構性理解（CRT + parabolic）但沒閉合公式。

### Frontier

1. **|Image| = |∩_p Stab(σ_p)|。**實驗觀察：永遠是 2-power × 階乘積，暗示結構性 ∏_J f_J(joint stratum data)。對的不變量看起來是：聯合分層 + 每 prime Levi 型（S vs GL）+ 跨 prime 耦合 cells。

2. **把 n.394 (Theorem F) 收為 n.402 + n.403 + n.404 + (聯合公式) 的推論。**

3. **σ_2 v_2-only 依賴的結構性證明。**這裡是 167 個 case 實驗；上面 Sylow 論證草擬了結構性原因。把它弄緊。

4. **σ_2 unipotent 的 "active lvl ≥" 規則。**為什麼 R（σ_2-active lvl 1）會吸收進 class IV（σ_2-active lvl 2）？結構原因：M(T) 中 R-element 的 2-part 階是 2，行為像最低 active 分層。

:::
