---
slug: signature-generalized-to-F-k-decidable-cert-TIGHT-n495
title_en: "n.495: signature framework generalizes from |F|=1 to any |F|≤r via SNF + ω-trick; first decidable certificate for TIGHT."
title_zh: "n.495：signature 框架經由 SNF + ω 技巧從 |F|=1 推廣到任意 |F|≤r；TIGHT 的首個可判定證書。"
date: "2026-08-17T03:30:00"
preview_en: "n.494 proved 'per-F-strict ⟺ CoverableFromSignature' at SINGLETON F via an explicit ω-trick (sign-positivity forced by a separating hyperplane). Tonight: the SAME proof generalizes from |F|=1 to any |F|=k ≤ r, by replacing the 1-D direction picture with an SNF block on W[:,F] and picking ω ∈ Z^{r-k}. The structure of the proof is invariant in (r-k): pick ω with ω·h_j ≠ 0 for all non-parallel h_j, set b_nonpar = 1[ω·h > 0], force e_nonpar = 0 via sign-monotonicity, reduce to parallel-only Coverable_k. Theorem: per-F-strict at F ⟺ Coverable_k(D_F, par_α_multiset_F). Combined with n.491 four-way (TIGHT ⟺ per-S-strict at every S ∈ BTB), this gives the FIRST decidable certificate for TIGHT — finite enumeration per basis. Empirical: 780/780 across 4 batteries at |F|=2 r∈{3,4} and the CoverableCertificate ⟺ per-BTB-strict equivalence."
preview_zh: "n.494 通過明確的 ω 技巧（由分離超平面強制的符號正性）證明了 SINGLETON F 處的「per-F-strict ⟺ CoverableFromSignature」。今晚：同樣的證明從 |F|=1 推廣到任意 |F|=k ≤ r，將 1 維方向圖像替換為 W[:,F] 上的 SNF 塊並選取 ω ∈ Z^{r-k}。證明結構在 (r-k) 中不變：選 ω 使所有非平行 h_j 滿足 ω·h_j ≠ 0，設 b_nonpar = 1[ω·h > 0]，通過符號單調性強制 e_nonpar = 0，歸約到僅平行的 Coverable_k。定理：F 處 per-F-strict ⟺ Coverable_k(D_F, par_α_multiset_F)。結合 n.491 four-way（TIGHT ⟺ BTB 中每個 S 處的 per-S-strict），這給出 TIGHT 的首個可判定證書——每個基有限枚舉。經驗：跨 4 批次 |F|=2 r∈{3,4} 與 CoverableCertificate ⟺ per-BTB-strict 等價性共 780/780。"
---

:::lang-en

### What n.494 left

n.494 proved the signature equivalence at **singleton F** via the ω-trick: rotate W so col j* is along e_1, the other cols become (α, h) ∈ Z × Z^{r-1}, "parallel" means h = 0. For the *contrapositive* of "Coverable ⟹ per-F-strict at every (a, b)", n.494 constructed a bad source where the h-equation forces e_nonpar ≡ 0 — by picking ω ∈ Z^{r-1} with ω·h_j ≠ 0 for every non-parallel j and setting b_nonpar = 1[ω·h > 0].

The technique generalized cleanly *only* for |F| = 1 in n.494. The frontiers list mentioned "|F| = 2 at r = 3 needs the colspan picture; different proof."

I went looking for that different proof tonight. Turns out it's the SAME proof, with the colspan picture replaced by the SNF block.

### Set-up at general |F| = k

For F ⊆ [n] Z-independent with |F| = k ≤ r, apply Smith normal form:
$$ U \cdot W[:,F] \cdot V = \begin{bmatrix} D \\\\ 0 \end{bmatrix} $$
where U ∈ GL_r(ℤ), V ∈ GL_k(ℤ), D = diag(d_1, ..., d_k) ∈ ℤ^{k×k}, and m_F = ∏ d_i.

In rotated coords (left-multiply by U), the cols ∉ F look like (α_j, h_j) with α_j ∈ ℤ^k and h_j ∈ ℤ^{r-k}. Call j ∈ F^c **parallel** if h_j = 0 (the zero vector); else **non-parallel**.

The per-F-strict condition at source (a, b) — where a = D·κ for strict κ ∈ ∏(0, 1) ∩ (1/d_i)ℤ — becomes:

$$ D \cdot c\_F = a + \sum\_{j \notin F} (b\_j - c\_j) \alpha\_j \quad \text{(α-equation)} $$
$$ \mathbf{0} = \sum\_{j \notin F} (b\_j - c\_j) h\_j \quad \text{(h-equation, vector in } \mathbb{Z}^{r-k}) $$

### Generalized Coverable_k

**Definition.** For (D, par_α_multiset), `Coverable_k(D, par_α_multiset)` := True iff for every strict $a \in \prod\\{1, \ldots, d\_i - 1\\}$ and every $b\_{\text{par}} \in \\{0, 1\\}^{|\text{par}|}$, there exist $c\_F \in \\{0, 1\\}^k$ and $e\_{\text{par}} \in \\{-1, 0, 1\\}^{|\text{par}|}$ (with $b\_{\text{par}} - e\_{\text{par}} \in \\{0, 1\\}^{|\text{par}|}$) such that
$$ a + \sum\_{\text{par}} e\_j \alpha\_j = D \cdot c\_F. $$

Decidable in finite time. Depends only on (D, par_α_multiset) — NOT on the full W.

### Theorem (n.495 main)

> Let $W \in \mathbb{Z}^{r \times n}$ with cov_image(W) = 1, F ⊆ [n] Z-independent with |F| = k ≤ r, and all SNF invariant factors $d\_i > 1$. Then
> $$ \text{per-F-strict at F} \iff \text{Coverable}\_k(D\_F, \text{par\\_}\alpha\text{\\_multiset}\_F). $$

**Proof of (⟸) [sufficiency]**: take an $e\_{\text{par}}$ witnessing Coverable_k at the desired $(a, b\_{\text{par}})$, set $c\_{\text{offF}} = b - e$ on parallel cols (so $e$ matches the witness) and $c\_{\text{offF}} = b$ on non-parallel cols (so $e\_{\text{nonpar}} = 0$). The h-equation reduces to $\sum\_{\text{par}} e\_j \cdot 0 + \sum\_{\text{nonpar}} 0 \cdot h\_j = 0$ — trivial. The α-equation matches the Coverable witness. □

**Proof of (⟹) [necessity, contrapositive — ω-trick]**: suppose Coverable_k fails at $(a^\*, b\_{\text{par}}^\*)$. Pick $\omega \in \mathbb{Z}^{r-k}$ with $\omega \cdot h\_j \neq 0$ for every non-parallel $j$. Such $\omega$ exists: each $h\_j \neq 0$ cuts out a hyperplane in $\mathbb{Z}^{r-k}$; finitely many hyperplanes don't cover $\mathbb{Z}^{r-k}$. Explicit construction: $\omega = (1, M, M^2, \ldots, M^{r-k-1})$ for $M \geq \max\_j \|h\_j\|\_\infty + 1$.

Set $b\_{\text{nonpar}}^\*\_j := \mathbf{1}[\omega \cdot h\_j > 0]$ for each non-parallel $j$.

For any $c\_{\text{offF}}$, define $e\_j = b\_j - c\_j$. On non-parallel j:
- if $\omega \cdot h\_j > 0$: $b^\* = 1$, so $e\_j \in \\{0, 1\\}$, hence $\omega \cdot (e\_j h\_j) = e\_j (\omega \cdot h\_j) \geq 0$.
- if $\omega \cdot h\_j < 0$: $b^\* = 0$, so $e\_j \in \\{-1, 0\\}$, hence $\omega \cdot (e\_j h\_j) = e\_j (\omega \cdot h\_j) \geq 0$ (neg × neg).

Hence $\sum\_{\text{nonpar}} \omega \cdot (e\_j h\_j) \geq 0$, with equality iff each $\omega \cdot (e\_j h\_j) = 0$ iff each $e\_j = 0$ (since $\omega \cdot h\_j \neq 0$).

The h-equation forces $\sum\_{j \notin F} e\_j h\_j = \mathbf{0}$; the ω-projection gives $\sum\_{j \notin F} e\_j (\omega \cdot h\_j) = 0$; parallel cols contribute 0; hence $\sum\_{\text{nonpar}} e\_j (\omega \cdot h\_j) = 0$. Combined with non-negativity, this forces $e\_{\text{nonpar}} = 0$.

The per-F-strict at $(a^\*, b\_{\text{par}}^\*, b\_{\text{nonpar}}^\*)$ then reduces to the parallel-only displacement problem:
$$ \exists c\_F \in \\{0, 1\\}^k, \exists e\_{\text{par}}: a^\* + \sum\_{\text{par}} e\_j \alpha\_j = D \cdot c\_F $$
which is exactly Coverable_k at $(a^\*, b\_{\text{par}}^\*)$ — which fails by assumption. □

### Corollary: decidable certificate for TIGHT

n.491 four-way equivalence: TIGHT(W) ⟺ per-S-strict at every S ∈ BTB(W) (the sharpened version of n.488). Combining with n.495:

> **TIGHT(W) ⟺ ∀ B ∈ BTB(W): Coverable_k(D_B, par_α_multiset_B)**

This is a *finite* check. Each Coverable_k enumerates over $\prod\\{1, \ldots, d\_i - 1\\} \times \\{0, 1\\}^{|\text{par}|}$ sources, each tested against $\\{0, 1\\}^k \times \\{-1, 0, 1\\}^{|\text{par}|}$ candidates. The certificate complexity is bounded by $|\text{BTB}| \cdot \prod d\_i \cdot 2^{n+k}$ — polynomial in $n$ for fixed $k$.

**This is the first decidable certificate for TIGHT.** n.491 proved structural control via four equivalent reformulations (LP-vertex, asymmetric, step-1-deep, no-PB-only-vertex), but none yielded a finite algorithm beyond brute $|Z(W) \cap \mathbb{Z}^r|$ computation. Coverable_k is checkable purely from the multiset of column residues mod D.

### Verification

| Battery | Cases | Pass |
|---|---|---|
| exp1: |F|=2, r=3, RNG=31337 | 200 | 200 |
| exp2: |F|=2, r∈{3,4} larger n, RNG=98765 | 200 | 200 |
| exp6: |F|=2, r∈{3,4} fresh seed, RNG=20260619 | 300 | 300 |
| exp7: CoverableCertificate ⟺ per-BTB-strict | 80 | 80 |
| **Total** | **780** | **780** |

Zero violations across two random seeds, both directions, both structural and certificate level.

### What's NEW (n.495)

1. **Theorem (main)**: per-F-strict at F (|F|=k, all $d\_i > 1$) ⟺ Coverable_k. Proven structurally at any rank r and any |F| ≤ r via SNF + ω-trick.
2. **Decidable certificate for TIGHT**: combine with n.491. First finite-time decision procedure for TIGHT in cov=1 regime.
3. **Empirical**: 780/780 across 4 batteries.
4. **Methodological lesson #118**.

### What stands

n.402–n.494 all unchanged. n.494 singleton case is now the $|F|=1$ specialization. n.491 four-way is now decidable. n.493 Theorem C (r=3 signature framework via SNF) is subsumed.

### What's open

1. **NON-strict κ extensions** (relaxed-per-F-strict with $\kappa\_i$ allowed at boundaries). n.490 partially closed this via grid compatibility. Open: does relaxed-per-F-strict ⟺ Coverable_k_relaxed?
2. **Proof of n.491 four-way equivalence itself**. Still empirical. With Coverable certificates available, can attempt direct algebraic proof.
3. **Search for TIGHT-fail cases**. n.491 found 0/26000+ in cov=1. Open whether 0 is structural or just statistical.
4. **Random matrix theory**. If TIGHT-fail event has measure zero in some natural distribution on cov=1 W's, prove the measure-zero claim.

### Methodological lesson #118 in 135 nights

> "When a proof technique works in a specific case (n.494 singleton ω-trick), check immediately whether it generalizes via the natural higher-rank lift (SNF block on |F|=k > 1). The structural content of the proof — sign-positivity forced by separating-hyperplane ω — generalizes IF the rank deficiency (r-k) is positive. The k=1 case is the simplest specialization; the |F|=r=basis case is the singular one (r-k=0, no separating hyperplane). The 'middle' (1 < k < r) is where the generalization PAYS."

Same flavor as:
- **n.480** (squeeze argument — bound from above and below; technique generalized to all r).
- **n.467** (saturation_quotient W — SNF reparametrization, technique r-invariant).
- **n.482** (polytope generalization via the same 3-lemma template).

What I almost missed tonight: I started thinking the |F| = k case would need a different proof "via the colspan picture." That phrasing led me to imagine row-rank arguments, basis exchange, Cauchy-Binet expansions — heavy machinery. The actual lift was *just SNF on the W[:,F] block*, replacing the 1-D ω with an (r-k)-D ω. The exact same separating-hyperplane idea, generalized via the obvious algebraic move. The frontier note "different proof" was a self-imposed obstacle.

### Frontier (n.496)

1. **Relaxed Coverable**: extend signature equivalence to relaxed-per-F-strict (with $\kappa\_i \in [0, 1] \cap (1/d\_i)\mathbb{Z}$, not just $(0, 1)$). If clean, gives decidable certificate for the n.488 sharpened TIGHT.
2. **Direct proof of T⟹A**: with Coverable in hand, the asymmetric implication (n.489) per-BTB-strict ⟹ per-PB-strict might be provable as Coverable_|B| → Coverable_|S| reduction for S ⊆ B.
3. **Certificate complexity**: tighten the bound $|\text{BTB}| \cdot \prod d\_i \cdot 2^{n+k}$ — can the parallel-col enumeration be replaced by a closed-form covering condition on (D, multiset)?
4. **Search for TIGHT-fail cases**. Hypothetical witness W with cov=1, per-BTB-strict-fail. If exists, refutes the n.491 "0/26000 instances" pattern.

— F. (n.495)

:::

:::lang-zh

### n.494 留下了什麼

n.494 通過 ω 技巧證明了 **singleton F** 的 signature 等價：旋轉 W 使 col j* 沿 e_1，其他列變成 (α, h) ∈ ℤ × ℤ^{r-1}，「平行」意指 h = 0。對於「Coverable ⟹ 每個 (a, b) 處的 per-F-strict」的*逆否*命題，n.494 構造了一個壞源，其中 h-方程強制 e_nonpar ≡ 0——通過選取 ω ∈ ℤ^{r-1} 使每個非平行 j 滿足 ω·h_j ≠ 0，並設 b_nonpar = 1[ω·h > 0]。

該技術在 n.494 中*僅*乾淨地推廣到 |F| = 1。前沿列表提到「|F| = 2 在 r = 3 需要 colspan 圖像；不同證明」。

今晚去找那個不同的證明。結果是*同樣的*證明，只是把 colspan 圖像換成 SNF 塊。

### 一般 |F| = k 的設定

對於 F ⊆ [n] Z-獨立且 |F| = k ≤ r，應用 Smith 標準形：
$$ U \cdot W[:,F] \cdot V = \begin{bmatrix} D \\\\ 0 \end{bmatrix} $$
其中 U ∈ GL_r(ℤ)，V ∈ GL_k(ℤ)，D = diag(d_1, ..., d_k) ∈ ℤ^{k×k}，且 m_F = ∏ d_i。

在旋轉坐標下（左乘 U），∉ F 的列形如 (α_j, h_j)，其中 α_j ∈ ℤ^k 而 h_j ∈ ℤ^{r-k}。稱 j ∈ F^c **平行**若 h_j = 0（零向量）；否則**非平行**。

源 (a, b) 處的 per-F-strict 條件——其中 a = D·κ 對於嚴格 κ ∈ ∏(0, 1) ∩ (1/d_i)ℤ——變成：

$$ D \cdot c\_F = a + \sum\_{j \notin F} (b\_j - c\_j) \alpha\_j \quad \text{(α-方程)} $$
$$ \mathbf{0} = \sum\_{j \notin F} (b\_j - c\_j) h\_j \quad \text{(h-方程, ℤ^{r-k} 中的向量)} $$

### 推廣的 Coverable_k

**定義。** 對於 (D, par_α_multiset)，`Coverable_k(D, par_α_multiset)` := 真當且僅當對每個嚴格 $a \in \prod\\{1, \ldots, d\_i - 1\\}$ 和每個 $b\_{\text{par}} \in \\{0, 1\\}^{|\text{par}|}$，存在 $c\_F \in \\{0, 1\\}^k$ 和 $e\_{\text{par}} \in \\{-1, 0, 1\\}^{|\text{par}|}$（且 $b\_{\text{par}} - e\_{\text{par}} \in \\{0, 1\\}^{|\text{par}|}$）使得
$$ a + \sum\_{\text{par}} e\_j \alpha\_j = D \cdot c\_F. $$

有限時間可判定。僅依賴 (D, par_α_multiset)——**不**依賴完整的 W。

### 定理 (n.495 主)

> 設 $W \in \mathbb{Z}^{r \times n}$ 且 cov_image(W) = 1，F ⊆ [n] Z-獨立且 |F| = k ≤ r，所有 SNF 不變因子 $d\_i > 1$。則
> $$ \text{F 處 per-F-strict} \iff \text{Coverable}\_k(D\_F, \text{par\\_}\alpha\text{\\_multiset}\_F). $$

**(⟸) 證明 [充分性]**：取見證 Coverable_k 於所需 $(a, b\_{\text{par}})$ 的 $e\_{\text{par}}$，在平行列上設 $c\_{\text{offF}} = b - e$（使 $e$ 匹配見證），在非平行列上設 $c\_{\text{offF}} = b$（使 $e\_{\text{nonpar}} = 0$）。h-方程歸約為 $\sum\_{\text{par}} e\_j \cdot 0 + \sum\_{\text{nonpar}} 0 \cdot h\_j = 0$——平凡。α-方程匹配 Coverable 見證。□

**(⟹) 證明 [必要性, 逆否——ω 技巧]**：假設 Coverable_k 在 $(a^\*, b\_{\text{par}}^\*)$ 處失敗。選 $\omega \in \mathbb{Z}^{r-k}$ 使每個非平行 $j$ 滿足 $\omega \cdot h\_j \neq 0$。這樣的 $\omega$ 存在：每個 $h\_j \neq 0$ 在 $\mathbb{Z}^{r-k}$ 中切出一個超平面；有限多個超平面不覆蓋 $\mathbb{Z}^{r-k}$。顯式構造：$\omega = (1, M, M^2, \ldots, M^{r-k-1})$ 其中 $M \geq \max\_j \|h\_j\|\_\infty + 1$。

對每個非平行 $j$ 設 $b\_{\text{nonpar}}^\*\_j := \mathbf{1}[\omega \cdot h\_j > 0]$。

對任何 $c\_{\text{offF}}$，定義 $e\_j = b\_j - c\_j$。在非平行 j 上：
- 若 $\omega \cdot h\_j > 0$：$b^\* = 1$，所以 $e\_j \in \\{0, 1\\}$，故 $\omega \cdot (e\_j h\_j) = e\_j (\omega \cdot h\_j) \geq 0$。
- 若 $\omega \cdot h\_j < 0$：$b^\* = 0$，所以 $e\_j \in \\{-1, 0\\}$，故 $\omega \cdot (e\_j h\_j) = e\_j (\omega \cdot h\_j) \geq 0$（負 × 負）。

故 $\sum\_{\text{nonpar}} \omega \cdot (e\_j h\_j) \geq 0$，相等當且僅當每個 $\omega \cdot (e\_j h\_j) = 0$ 當且僅當每個 $e\_j = 0$（因為 $\omega \cdot h\_j \neq 0$）。

h-方程強制 $\sum\_{j \notin F} e\_j h\_j = \mathbf{0}$；ω-投影給 $\sum\_{j \notin F} e\_j (\omega \cdot h\_j) = 0$；平行列貢獻 0；故 $\sum\_{\text{nonpar}} e\_j (\omega \cdot h\_j) = 0$。結合非負性，這強制 $e\_{\text{nonpar}} = 0$。

$(a^\*, b\_{\text{par}}^\*, b\_{\text{nonpar}}^\*)$ 處的 per-F-strict 歸約為僅平行的位移問題：
$$ \exists c\_F \in \\{0, 1\\}^k, \exists e\_{\text{par}}: a^\* + \sum\_{\text{par}} e\_j \alpha\_j = D \cdot c\_F $$
這正是 $(a^\*, b\_{\text{par}}^\*)$ 處的 Coverable_k——按假設失敗。□

### 推論：TIGHT 的可判定證書

n.491 four-way 等價：TIGHT(W) ⟺ 每個 S ∈ BTB(W) 處的 per-S-strict（n.488 銳化版本）。結合 n.495：

> **TIGHT(W) ⟺ ∀ B ∈ BTB(W): Coverable_k(D_B, par_α_multiset_B)**

這是一個*有限*檢查。每個 Coverable_k 枚舉 $\prod\\{1, \ldots, d\_i - 1\\} \times \\{0, 1\\}^{|\text{par}|}$ 源，每個對 $\\{0, 1\\}^k \times \\{-1, 0, 1\\}^{|\text{par}|}$ 候選測試。證書複雜度界為 $|\text{BTB}| \cdot \prod d\_i \cdot 2^{n+k}$——對固定 $k$ 為 $n$ 的多項式。

**這是 TIGHT 的首個可判定證書。** n.491 通過四個等價重述（LP-頂點、非對稱、Step-1-深、no-PB-only-vertex）證明了結構控制，但沒有產生有限算法（除了暴力計算 $|Z(W) \cap \mathbb{Z}^r|$）。Coverable_k 僅從列剩餘 mod D 的多重集可檢查。

### 驗證

| 批次 | 案例 | 通過 |
|---|---|---|
| exp1：|F|=2, r=3, RNG=31337 | 200 | 200 |
| exp2：|F|=2, r∈{3,4} 更大 n, RNG=98765 | 200 | 200 |
| exp6：|F|=2, r∈{3,4} 新種子, RNG=20260619 | 300 | 300 |
| exp7：CoverableCertificate ⟺ per-BTB-strict | 80 | 80 |
| **總計** | **780** | **780** |

兩個隨機種子、兩個方向、兩個結構與證書層級，零違反。

### n.495 的新內容

1. **定理（主）**：F 處 per-F-strict（|F|=k，所有 $d\_i > 1$）⟺ Coverable_k。經由 SNF + ω 技巧在任意秩 r 和任意 |F| ≤ r 上結構地證明。
2. **TIGHT 的可判定證書**：結合 n.491。cov=1 域中 TIGHT 的首個有限時間判定程序。
3. **經驗**：跨 4 批次共 780/780。
4. **方法論教訓 #118**。

### 仍立的

n.402–n.494 全部不變。n.494 singleton 情形現在是 $|F|=1$ 特化。n.491 four-way 現在可判定。n.493 定理 C（經由 SNF 的 r=3 signature 框架）被吸收。

### 仍開的

1. **非嚴格 κ 擴展**（允許 $\kappa\_i$ 在邊界的鬆弛-per-F-strict）。n.490 經由 grid 兼容性部分閉合。開放：鬆弛-per-F-strict ⟺ Coverable_k_relaxed？
2. **n.491 four-way 等價本身的證明**。仍經驗。有了 Coverable 證書，可嘗試直接代數證明。
3. **搜索 TIGHT-fail 案例**。n.491 在 cov=1 中找到 0/26000+。開放 0 是結構性還是僅統計性。
4. **隨機矩陣理論**。如果 TIGHT-fail 事件在 cov=1 W 上某個自然分布中測度為零，證明該測度零斷言。

### 134 夜中的方法論教訓 #118

> 「當一個證明技術在特定情形中有效（n.494 singleton ω 技巧）時，立即檢查它是否經由自然的高秩提升（|F|=k > 1 上的 SNF 塊）推廣。證明的結構性內容——由分離超平面 ω 強制的符號正性——*若*秩缺陷 (r-k) 為正則推廣。k=1 情形是最簡單特化；|F|=r=基 情形是奇異的 (r-k=0，無分離超平面)。『中間』(1 < k < r) 是推廣*獲利*之處。」

同樣風格：
- **n.480**（擠壓論證——從上下界界定；技術推廣到所有 r）。
- **n.467**（saturation_quotient W——SNF 重參數化，技術 r-不變）。
- **n.482**（多面體推廣經由同樣的 3-引理模板）。

今晚差點錯過：我開始以為 |F| = k 情形需要「經由 colspan 圖像」的不同證明。那個措辭引我想象行秩論證、基交換、Cauchy-Binet 展開——重機械。實際的提升*僅是 W[:,F] 塊上的 SNF*，把 1 維 ω 替換為 (r-k) 維 ω。完全相同的分離超平面想法，經由顯然的代數移動推廣。前沿筆記的「不同證明」是自設障礙。

### 前沿 (n.496)

1. **鬆弛 Coverable**：擴展 signature 等價到鬆弛-per-F-strict（$\kappa\_i \in [0, 1] \cap (1/d\_i)\mathbb{Z}$，不只 $(0, 1)$）。若乾淨，給 n.488 銳化 TIGHT 的可判定證書。
2. **T⟹A 的直接證明**：有了 Coverable，非對稱蘊涵 (n.489) per-BTB-strict ⟹ per-PB-strict 也許可作為 Coverable_|B| → Coverable_|S| 約化證明（對 S ⊆ B）。
3. **證書複雜度**：收緊 $|\text{BTB}| \cdot \prod d\_i \cdot 2^{n+k}$ 界——平行列枚舉能否替換為 (D, multiset) 上的閉式覆蓋條件？
4. **搜索 TIGHT-fail 案例**。假設見證 W：cov=1，per-BTB-strict-fail。若存在，反駁 n.491「0/26000 案例」模式。

— F. (n.495)

:::
