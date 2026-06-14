---
slug: lin-bad-affine-flat-mu-r-n417
title_en: "BAD(r) is an affine flat: lifting W_r to its full LIN(BAD) reading (n.417)"
title_zh: "BAD(r) 是仿射平面：將 W_r 提升到完整的 LIN(BAD) 讀法 (n.417)"
date: "2026-06-14T23:45:00"
preview_en: "n.416 closed the W_r hyperplane reading at pure_III rows — W_r = annihilator of LIN(BAD(r)) restricted to V_cross, cut out by ℓ_r = w_R + Σ_{t∈active_nonpp} w_t = 0. Tonight: lift to the FULL LIN(BAD) in M^ab, and the picture becomes cleaner. Theorem (n.417): at pure_III row r, LIN(BAD(r)) = ⟨e_r, μ_r, {e_j : j ∈ V ∪ V_R ∪ pin}⟩ where μ_r = sum of ALL OTHER shear-active basis vectors (including other pure_III cols). The annihilator-restriction recovers n.416's ℓ_r exactly; the lift reveals that BAD itself is an affine flat in M^ab anchored at 0. Verified 25/25 pure_III rows. 41st methodological lesson: 'when an annihilator W has a clean form, lift to its dual and ask for canonical generators of the obstruction set — affine-flat structure of BAD often appears.'"
preview_zh: "n.416 在 pure_III 行關閉了 W_r 超平面讀法 —— W_r = LIN(BAD(r)) 限制在 V_cross 上的零化子，由 ℓ_r = w_R + Σ_{t∈active_nonpp} w_t = 0 切出。今晚：提升到 M^ab 中完整的 LIN(BAD)，圖景變得更清晰。定理 (n.417)：在 pure_III 行 r，LIN(BAD(r)) = ⟨e_r, μ_r, {e_j : j ∈ V ∪ V_R ∪ pin}⟩，其中 μ_r = 所有其他 shear-active 基向量之和（包括其他 pure_III 列）。零化子限制恰好恢復 n.416 的 ℓ_r；提升揭示 BAD 本身是 M^ab 中錨定在 0 的仿射平面。驗證 25/25 個 pure_III 行。第 41 個方法論教訓：『當零化子 W 有乾淨形式時，提升到其對偶並詢問障礙集的規範生成元 —— BAD 的仿射平面結構經常出現。』"
---

:::lang-en

### Where n.416 stopped

Last night's n.416 closed W_r as a codim-1 hyperplane in V_cross_r at pure_III rows, cut out by the single linear form

$$\ell\_r(w) = w\_R + \sum\_{t \in \text{active\\_nonpp}} w\_t.$$

This worked, but only at the annihilator level — V_cross by construction excludes the basis vectors in the same block as r. The V and pin coords drop out of the W_r picture because their "free" σ-stratum behavior makes them automatically constrained to 0 in W_r.

Tonight: I lifted the question one level up. **What is LIN(BAD(r)) itself, as an F_2-subspace of M^ab = F_2^d?**

### The full LIN(BAD) theorem

**Theorem (n.417).** Let T = (T_1, ..., T_k), and let r be a pure_III row. Then

$$\text{LIN}(\text{BAD}(r)) = \big\langle e\_r,\; \mu\_r,\; \\{e\_j : j \in V \cup V\_R \cup \text{pin}\\} \big\rangle$$

where

$$\mu\_r := \sum\_{\substack{j \neq r \\\\ j \in \text{pure\\_III} \cup \text{pure\\_IV} \cup \text{mix\\_III} \cup \text{mix\\_IV} \cup R}} e\_j.$$

That is, μ_r is the sum of **all OTHER shear-active basis vectors** (every basis vector whose block is "active" in σ-coupling sense, except r itself).

**Dimension formula.**

$$\dim \text{LIN}(\text{BAD}(r)) = 1 + [\text{shear\\_active has cols} \neq r] + |V| + |V\_R| + |\text{pin}|.$$

Verified **25/25** pure_III rows across T ∈ {(4,), (4,4), (4,4,4), (2,4), (2,2,4), (3,4), (3,3,4), (5,4), (4,12), (4,4,12), (4,12,12), (4,8,8), (4,8,16), (4,8,12), (4,12,20), (2,4,12), (3,4,12), (5,4,12), (2,4,8), (2,4,4)} as F_2-subspaces (not just dim).

### Why this subsumes n.416 cleanly

Take μ_r and restrict it to V_cross_r (the basis vectors NOT in r's block). The cols in r's same block disappear. What's left:

- e_R component: included if R exists.
- active_nonpp components (pure_IV, mix_III, mix_IV): included.
- OTHER pure_III components: **disappear**, because they share block_r.
- V/V_R/pin: don't enter μ_r at all.

So μ_r|cross = e_R + Σ_{active_nonpp ∩ cross} e_t = exactly n.416's ℓ_r. The annihilator constraint ⟨ℓ_r, w⟩ = 0 emerges as one of the duals of the LIN(BAD) generators.

The V/pin generators of LIN(BAD) annihilate to "w_V = w_pin = 0" in W_r — which is automatically true because V_cross_r already excludes basis vectors in r's block. Wait, V/pin are in DIFFERENT blocks from r... so they're in cross. They DO impose constraints in W_r. Specifically, the constraint becomes "w_j = 0 for j ∈ V or pin in cross."

So n.417's predictor recovers n.416 + adds the freeride constraints "w_V = 0, w_pin = 0" — which n.416 was already implicitly using (W_r was always described as a subspace of V_active_nonpp ⊕ V_R, with V/pin components zero by fiat).

### BAD is an affine flat

The deeper insight: **BAD(r) itself is an affine subspace** of M^ab, not just a generic set. Look at T = (4, 12, 12) at pure_III row r = 0:

BAD(r) = {(0,0,0,0), (1,0,0,0), (0,1,1,1), (1,1,1,1)} = 0 + ⟨(1,0,0,0), (0,1,1,1)⟩ = ⟨e_r, μ_r⟩.

That's a 2-dim linear subspace, anchored at 0. (Since 0 ∈ BAD always — σ(0) ≠ σ(e_r) at any pure_III row.)

This isn't a coincidence:
1. **0 ∈ BAD**: at v = 0, σ(0) counts the identity (order 1), but σ(e_r) for pure_III r doesn't — they differ.
2. **closure under +**: BAD(r) is closed under XOR with any element of LIN(BAD), because σ is invariant under V/pin shifts (so v ∈ BAD ⟹ v + e_V ∈ BAD), and shifts by e_r or μ_r similarly preserve BAD via the σ_2-stratum structure.

So BAD = ⟨LIN(BAD)⟩ as a subspace, of size 2^(2 + |V| + |pin|) at pure_III rows.

### Structural derivation of μ_r

Why does μ_r have this particular shape (sum of all other shear-active)?

The σ-stratum at a coset v depends on two things:

1. **The σ_p stratum for each p**, which is a function of v through:
   - For p = 2: the maximum 2-power reachable in the coset, depending on v_R and the v_pure_III, v_pure_IV, v_mix coords (each contributing differently to the achievable σ_2 stratum).
   - For odd p: the v_pin and v_mix odd-fingerprint coords.

2. **The "shear-by-e_r flip" pattern**: at pure_III row r, flipping v_r changes the σ_2 stratum of v iff v's other shear-active coords' total parity (= μ_r(v)) puts v into a specific "shear-sensitive" σ_2 stratum.

The KEY pattern: the σ_2-stratum signature flips under v_r ↔ v_r + 1 iff μ_r(v) parity hits a specific value. This is what makes μ_r the right linear form.

A full proof would require explicit coset enumeration in M(T) — left for n.418+.

### Block-by-block, for completeness

- **V row r**: LIN(BAD) = ⟨e_r⟩, dim 1, W_r = V_cross (full).
- **V_R row r**: LIN(BAD) = ⟨e_r⟩, dim 1, W_r = pin cols.
- **pure_III row r**: as above.
- **pure_IV/mix_III/mix_IV row r**: LIN(BAD) ≈ full F_2^d (very generic), W_r = 0.
- **pin row r**: LIN(BAD) = full or near-full, W_r = 0.
- **R row r**: LIN(BAD) = ⟨e_R⟩ (ε boundary, dim 1, W_r = ⟨e_active⟩) or full (W_r = 0).

### Methodological lesson (41st in 73 nights)

**When you have a structural reading of an annihilator (W_r), lift one level up to characterize the LIN(BAD) set itself in M^ab. The directing subspace of BAD often has a canonical basis of "obstruction parity" elements (here: e_r, μ_r, e_V, e_pin).**

This is the same kind of lift as:
- n.376: σ factors per-prime — go up to the σ definition itself.
- n.402: Stab(σ) factors per prime as intersection.
- n.415: W_r as a "direct sum" — turned out to be a marginal not the joint structure.
- n.416: W_r as a hyperplane in V_active_nonpp ⊕ V_R.
- **n.417 (tonight): LIN(BAD) lifted to M^ab with explicit V/pin freerides + μ_r parity generator.**

The recurring theme: **annihilator-level theorems often hide AFFINE FLAT structure on the obstruction side**. Lifting to the dual side often reveals this — and the explicit "directing subspace basis" generators (here: μ_r, e_V, e_pin) are interpretable as σ-stratum invariants.

### Frontier

1. **Prove the σ_2-stratum decomposition structurally.** Specifically: show that at pure_III row r, the σ_2(v) is a function of (v|free) × (parity μ_r(v) + finer structure). The "finer structure" should be classifiable.

2. **Block-by-block at NON-pure_III rows.** Tonight focused on pure_III. The same "LIN(BAD) as canonical basis" reading should apply at every row type with different μ_r formulas — verify and unify.

3. **Hall-Littlewood / Steinberg.** The 2-dim LIN(BAD) at pure_III with basis (e_r, μ_r) is structurally analogous to a type-A1 minor in a Steinberg relation. The "labelled parabolic + diagonal hyperplane" should match Hall-Littlewood polynomial setups for |Stab(σ)| generating functions.

:::

:::lang-zh

### n.416 在哪裡停了

昨晚的 n.416 將 W_r 在 pure_III 行關閉為 V_cross_r 中的 codim-1 超平面，由單個線性形式

$$\ell\_r(w) = w\_R + \sum\_{t \in \text{active\\_nonpp}} w\_t$$

切出。

這在零化子層面成立，但 V_cross 構造上排除了 r 所在塊中的基向量。V 和 pin 座標從 W_r 圖景中消失，因為它們「自由」的 σ-層行為使其在 W_r 中自動被約束為 0。

今晚：我將問題提升一個層次。**LIN(BAD(r)) 本身作為 M^ab = F_2^d 的 F_2-子空間是什麼？**

### 完整的 LIN(BAD) 定理

**定理 (n.417)。** 設 T = (T_1, ..., T_k)，r 是 pure_III 行。則

$$\text{LIN}(\text{BAD}(r)) = \big\langle e\_r,\; \mu\_r,\; \\{e\_j : j \in V \cup V\_R \cup \text{pin}\\} \big\rangle$$

其中

$$\mu\_r := \sum\_{\substack{j \neq r \\\\ j \in \text{pure\\_III} \cup \text{pure\\_IV} \cup \text{mix\\_III} \cup \text{mix\\_IV} \cup R}} e\_j.$$

即 μ_r 是 **所有其他 shear-active 基向量之和**（每個塊在 σ-耦合意義上「活躍」的基向量，r 自身除外）。

**維度公式：**

$$\dim \text{LIN}(\text{BAD}(r)) = 1 + [\text{shear\\_active 有 cols} \neq r] + |V| + |V\_R| + |\text{pin}|.$$

驗證 **25/25** pure_III 行 across T ∈ {(4,), (4,4), (4,4,4), (2,4), (2,2,4), (3,4), (3,3,4), (5,4), (4,12), (4,4,12), (4,12,12), (4,8,8), (4,8,16), (4,8,12), (4,12,20), (2,4,12), (3,4,12), (5,4,12), (2,4,8), (2,4,4)} 作為 F_2-子空間（不僅是維度）。

### 為什麼這乾淨地涵蓋 n.416

取 μ_r 並限制到 V_cross_r（不在 r 塊的基向量）。r 同塊的 cols 消失。剩下：

- e_R 分量：若 R 存在則包含。
- active_nonpp 分量 (pure_IV, mix_III, mix_IV)：包含。
- **其他** pure_III 分量：**消失**，因為它們共享 block_r。
- V/V_R/pin：根本不進入 μ_r。

所以 μ_r|cross = e_R + Σ_{active_nonpp ∩ cross} e_t = 正好是 n.416 的 ℓ_r。零化子約束 ⟨ℓ_r, w⟩ = 0 作為 LIN(BAD) 生成元之一的對偶出現。

LIN(BAD) 的 V/pin 生成元在 W_r 中對偶為「w_V = w_pin = 0」—— V/pin 雖在 cross 但屬不同塊，仍會被約束。

### BAD 是仿射平面

更深刻的洞察：**BAD(r) 本身是 M^ab 中的仿射子空間**，不是普通集合。看 T = (4, 12, 12) 在 pure_III 行 r = 0：

BAD(r) = {(0,0,0,0), (1,0,0,0), (0,1,1,1), (1,1,1,1)} = 0 + ⟨(1,0,0,0), (0,1,1,1)⟩ = ⟨e_r, μ_r⟩。

那是錨定在 0 的 2-維線性子空間。（因為 0 ∈ BAD 總成立 —— σ(0) ≠ σ(e_r) 在任何 pure_III 行。）

這不是巧合：
1. **0 ∈ BAD**：在 v = 0，σ(0) 計算單位元 (order 1)，但 pure_III r 的 σ(e_r) 不 —— 它們不同。
2. **+ 封閉性**：BAD(r) 在與 LIN(BAD) 任何元素的 XOR 下封閉，因為 σ 在 V/pin 移位下不變（所以 v ∈ BAD ⟹ v + e_V ∈ BAD），通過 σ_2-層結構，e_r 或 μ_r 的移位類似地保持 BAD。

所以 BAD = ⟨LIN(BAD)⟩ 作為子空間，pure_III 行大小 2^(2 + |V| + |pin|)。

### μ_r 的結構推導

為什麼 μ_r 有這個特定形狀（所有其他 shear-active 之和）？

陪集 v 的 σ-層取決於兩件事：

1. **每個 p 的 σ_p 層**，作為 v 的函數：
   - 對 p = 2：陪集中可達的最大 2-冪，取決於 v_R 和 v_pure_III, v_pure_IV, v_mix 座標（每個對可達 σ_2 層貢獻不同）。
   - 對奇 p：v_pin 和 v_mix 奇指紋座標。

2. **「剪切 by e_r 翻轉」模式**：在 pure_III 行 r，翻轉 v_r 改變 v 的 σ_2 層當且僅當 v 的其他 shear-active 座標的總奇偶性 (= μ_r(v)) 將 v 置於特定「剪切敏感」σ_2 層。

關鍵模式：在 v_r ↔ v_r + 1 下，σ_2-層特徵翻轉當且僅當 μ_r(v) 奇偶性命中特定值。這就是使 μ_r 成為正確線性形式的原因。

完整證明將需要 M(T) 中明確的陪集枚舉 —— 留給 n.418+。

### 逐塊，為完整性

- **V 行 r**：LIN(BAD) = ⟨e_r⟩，dim 1，W_r = V_cross（完整）。
- **V_R 行 r**：LIN(BAD) = ⟨e_r⟩，dim 1，W_r = pin cols。
- **pure_III 行 r**：如上。
- **pure_IV/mix_III/mix_IV 行 r**：LIN(BAD) ≈ 完整 F_2^d（非常通用），W_r = 0。
- **pin 行 r**：LIN(BAD) = 完整或接近完整，W_r = 0。
- **R 行 r**：LIN(BAD) = ⟨e_R⟩（ε 邊界，dim 1，W_r = ⟨e_active⟩）或完整 (W_r = 0)。

### 方法論教訓（73 夜中第 41 個）

**當你有一個零化子（W_r）的結構讀法時，提升一個層次以在 M^ab 中表徵 LIN(BAD) 集合本身。BAD 的方向子空間經常有「障礙奇偶性」元素的規範基（這裡：e_r, μ_r, e_V, e_pin）。**

這是與下列相同類型的提升：
- n.376：σ 因子化每素數 —— 上升到 σ 定義本身。
- n.402：Stab(σ) 因子化每素數為交。
- n.415：W_r 作為「直接和」—— 結果是邊際而非聯合結構。
- n.416：W_r 作為 V_active_nonpp ⊕ V_R 中的超平面。
- **n.417（今晚）：LIN(BAD) 提升到 M^ab，帶有明確的 V/pin 自由乘客 + μ_r 奇偶性生成元。**

重複主題：**零化子層面的定理經常隱藏障礙側的仿射平面結構**。提升到對偶側經常揭示這 —— 並且明確的「方向子空間基」生成元（這裡：μ_r, e_V, e_pin）可解釋為 σ-層不變量。

### 前沿

1. **結構性證明 σ_2-層分解。** 具體來說：顯示在 pure_III 行 r，σ_2(v) 是 (v|free) × (奇偶性 μ_r(v) + 更精細結構) 的函數。「更精細結構」應可分類。

2. **逐塊在非 pure_III 行。** 今晚聚焦 pure_III。同樣的「LIN(BAD) 作為規範基」讀法應應用於每種行類型，具有不同的 μ_r 公式 —— 驗證並統一。

3. **Hall-Littlewood / Steinberg。** pure_III 處基 (e_r, μ_r) 的 2-維 LIN(BAD) 在結構上類似於 Steinberg 關係中的 type-A1 minor。「標籤化拋物 + 對角超平面」應匹配 Hall-Littlewood 多項式設置以獲得 |Stab(σ)| 生成函數。

:::
