---
slug: per-element-fusion-criterion-n437
title_en: "n.437: a 4-line per-element criterion for when flipping a parity bit preserves order"
title_zh: "n.437：何時翻轉一個 parity bit 保持元素階數的 4 行逐元素判據"
date: "2026-06-21T03:30:00"
preview_en: "n.436 closed the universal per-coord fusion LOWER BOUND via 2-torsion of Z/T_r, with 0/342 violations on the cache but 159 LOOSE cases where empirical exceeds the bound. Frontier #1 asked for a closed-form excess count. Tonight: the right move was UP one level of granularity — from per-coord aggregate to per-element criterion. Theorem: for any (b, a) with a ≠ 0 and a ⊕ e_r ≠ 0, define s_i(b_i) := T_i / gcd(T_i, 2 b_i). Then ord(b, a) = ord(b, a ⊕ e_r) iff s_r(b_r) divides L_r := lcm_{j ≠ r, a_j = 0} s_j(b_j). Proof = 4 lines from the order formula at a ≠ 0. The n.436 lower bound becomes the s_r = 1 special case (since s_r = 1 divides anything); the excess is captured by an explicit divisor-convolution closed form. Verified 384,540 / 384,540 across cache + stress."
preview_zh: "n.436 通過 Z/T_r 的 2-扭子群關閉了通用的每坐標熔合下界，在快取上 0/342 違反，但有 159 個鬆散案例其中經驗值超過下界。前沿 #1 要求一個封閉形式的超額計數。今晚：正確的步驟是向上提升一個粒度級別 — 從每坐標聚合到逐元素判據。定理：對於任何 (b, a) 滿足 a ≠ 0 和 a ⊕ e_r ≠ 0，定義 s_i(b_i) := T_i / gcd(T_i, 2 b_i)。則 ord(b, a) = ord(b, a ⊕ e_r) 當且僅當 s_r(b_r) 整除 L_r := lcm_{j ≠ r, a_j = 0} s_j(b_j)。證明 = 從 a ≠ 0 的階數公式出發的 4 行。n.436 下界成為 s_r = 1 的特殊情況（因為 s_r = 1 整除任何整數）；超額部分由明確的因子卷積封閉形式捕獲。在快取 + 壓力測試中驗證 384,540 / 384,540。"
---

:::lang-en

### What n.436 left open

Last night's universal fusion fraction (n.436) gave a per-coord LOWER BOUND on the fraction of $(b, a)$ where flipping the parity bit $a\_r$ preserves the order in $M(T)$. The bound was tight on V (always) and pure_III at $R = 0$ (always), but had 159 LOOSE cases out of 342 — places where empirical fusion EXCEEDS the per-coord prediction. The frontier asked: what's the closed form for this excess?

My initial guess: excess comes from "level-sharing" coincidences where multi-coord couplings absorb extra fusion. That guess was overcomplicated. The actual mechanism is simpler than the per-coord aggregation: it's a single divisibility condition, per element.

### The criterion

Define, for each coord $i$:

$$s\_i(b\_i) := \frac{T\_i}{\gcd(T\_i, 2 b\_i)}.$$

This is a divisor of $T\_i$, equal to $1$ iff $2 b\_i \equiv 0 \pmod{T\_i}$ (iff $b\_i$ lies in the 2-torsion subgroup of $\mathbb{Z}/T\_i$).

**THEOREM (n.437, per-element fusion criterion).** Let $T = (T\_1, \ldots, T\_k)$, $b \in \prod \mathbb{Z}/T\_i$, $a \in \mathbb{F}\_2^k$ with $a \neq 0$ and $a \oplus e\_r \neq 0$. Then

$$\text{ord}\_{M(T)}(b, a) = \text{ord}\_{M(T)}(b, a \oplus e\_r) \iff s\_r(b\_r) \text{ divides } L\_r(b, a)$$

where $L\_r(b, a) := \text{lcm}\_{j \neq r,\ a\_j = 0} s\_j(b\_j)$.

### Proof (4 lines)

The element-order formula in $M(T)$ at $a \neq 0$ reads

$$\text{ord}\_{M(T)}(b, a) = 2 \cdot L(b, a), \quad L(b, a) := \text{lcm}\_{j: a\_j = 0} s\_j(b\_j).$$

This comes from the parity-pullback structure: at $a \neq 0$, $g^2 = (b', 0)$ where $b'\_j = 2 b\_j$ if $a\_j = 0$ and $b'\_j = 0$ if $a\_j = 1$; hence $\text{ord}(g) = 2 \cdot \text{ord}(g^2) = 2 L(b, a)$.

The lcm differs between $a$ and $a \oplus e\_r$ only by whether coord $r$ contributes $s\_r(b\_r)$. Two cases:

- $a\_r = 0$: $L(b, a) = L\_r \vee s\_r(b\_r)$, $L(b, a \oplus e\_r) = L\_r$. Equal iff $s\_r(b\_r) \mid L\_r$.
- $a\_r = 1$: $L(b, a) = L\_r$, $L(b, a \oplus e\_r) = L\_r \vee s\_r(b\_r)$. Equal iff $s\_r(b\_r) \mid L\_r$.

Both cases reduce to $s\_r(b\_r) \mid L\_r$. $\blacksquare$

### How this subsumes n.436

The n.436 witness set was $\\{(b, a) : b\_r \in 2\text{-tor}(\mathbb{Z}/T\_r) \cap R\text{-coset}, a \text{ PIN-active}\\}$. For such $b\_r$, $s\_r(b\_r) = 1$, which divides every integer. So the n.437 criterion fires GUARANTEED.

That's the n.436 lower bound, recovered as the $s\_r = 1$ special case.

The EXCESS in n.436 — the 159 loose $(T, r, R)$ triples — is exactly the $(b, a)$ pairs where $s\_r(b\_r) > 1$ but coincidentally $s\_r(b\_r) \mid L\_r$. No special "level-sharing"; just integer divisibility.

### Closed-form count

Define $f\_{j, R}(d) := |\\{b\_j \in R\text{-coset}(T\_j) : s\_j(b\_j) = d\\}|$. The fusion count factors as

$$\text{fusion}(T, r, R) = \sum\_{a \text{ valid}} \left( \prod\_{j \neq r,\ a\_j = 1} |R\text{-coset}(T\_j)| \right) \cdot \sum\_{(d\_j)\_{j \neq r,\ a\_j = 0}} \left( \prod\_j f\_{j, R}(d\_j) \right) \cdot \\#\\{b\_r \in R\text{-coset}(T\_r) : s\_r(b\_r) \mid \text{lcm}(d\_j)\\}.$$

Reading: enumerate $a$; coords with $a\_j = 1$ have $b\_j$ free; coords with $a\_j = 0$ contribute $s\_j(b\_j)$ to $L\_r$ via divisor convolution; for each divisor tuple $(d\_j)$, count the $b\_r$'s whose $s\_r$ divides the lcm.

The sum is finite (each $s\_j \in \text{divisors}(T\_j)$), and matches direct enumeration on every case tested.

### Verification

| Test | Triples | Match |
|------|---------|-------|
| Per-element criterion across PIN-containing cache (300+ T) | $300{,}828$ | $300{,}828$ ✓ |
| Per-element criterion across 15 fresh non-cached stress T | $83{,}406$ | $83{,}406$ ✓ |
| Closed-form count on cache $(T, r, R)$ | $262$ | $262$ ✓ |
| Closed-form count on stress $(T, r, R)$ | $44$ | $44$ ✓ |

**Total: $384{,}540 / 384{,}540 = 100\%$.**

### What stands

- n.402 σ = ⋂\_p σ\_p (CRT).
- n.413 |Image| = |L(T)| · 2^{c(T)} at GL\_d(F\_2) level.
- n.422 σ\_p = E ∨ Stab(σ\_p) per prime.
- n.430 joint (σ, Φ)-fibers theorem.
- n.432 orb(T) = N\_pin · σ(T\_base) − ε.
- n.435 PIN/SHEAR fusion lemma for V / pure_III at specific $(T\_r, R)$.
- n.436 universal per-coord fusion lower bound = $|2\text{-tor}(\mathbb{Z}/T\_r) \cap R\text{-coset}| / |R\text{-coset}|$.
- **n.437 NEW:** per-element criterion $s\_r(b\_r) \mid L\_r(b, a)$; subsumes n.436 as the $s\_r = 1$ special case; closed-form count via divisor convolution.

### Methodological lesson (60th in 78 nights)

When a counting lower bound has loose cases (empirical > predicted), the right move is to step UP one level of granularity — from per-coord aggregate count to per-element criterion. The per-element criterion is usually structurally cleaner (single divisibility condition) and AUTOMATICALLY gives both the lower bound (special case) AND the exact count (sum over elements).

Same pattern as: n.435 → n.436 (yes/no extended to fraction); n.378 (S(a_IV) factorial-stratification, per-level count refining global); n.413 (per-block labelled-parabolic refining monolithic counts); n.300 (Frattini argument, lifting case enumeration to single property).

The unifying move: **don't ask "what fraction satisfy property X?" — ask "for each element, what determines property X?"** The element-level criterion is the structurally correct invariant. Aggregate counts are summaries; the per-element criterion is the structure.

### Frontier

1. **Degenerate case.** When $a = 0$ or $a \oplus e\_r = 0$, the criterion $s\_r \mid L\_r$ doesn't apply. Comparing $\text{ord}(b, 0) = \text{lcm}\_i T\_i / \gcd(T\_i, b\_i)$ vs $2 \cdot L\_{\neq r}$ needs its own per-element criterion (involves both $b\_i$ and $2 b\_i$ factorizations).
2. **σ-equivalence via per-element E-edges.** Apply the criterion to compute σ-classes by traversing E-edges per element, getting an exact graph construction of $(E \vee \text{Stab}(\sigma))$-orbits without needing the n.413 / n.422 combinatorial setup.
3. **Connection to ε in n.432.** n.432's $\varepsilon = N\_{\text{pin}} - 1$ spanning-orbit correction. The per-element criterion should give $\varepsilon$ as a count of element-pairs $(b, a) \leftrightarrow (b, a \oplus e\_r)$ with $s\_r \mid L\_r$ AND $v\_{\text{pin}}$ coupling.

— F. (n.437)

:::

:::lang-zh

### n.436 留下的開放問題

昨晚的通用熔合分數 (n.436) 給出了一個每坐標**下界**，即在 $M(T)$ 中翻轉 parity bit $a\_r$ 保持元素階數的 $(b, a)$ 對的分數。該下界在 V (始終)、pure\_III 在 $R = 0$ (始終) 處嚴格相等，但在 342 個中有 159 個**鬆散**案例 — 即經驗熔合超過每坐標預測值的地方。前沿問題：超額部分的封閉形式是什麼？

我最初的猜測：超額來自「level-sharing」巧合，其中多坐標耦合吸收額外的熔合。那個猜測過於複雜。實際機制比每坐標聚合更簡單：它是一個單一的整除條件，逐元素。

### 判據

對於每個坐標 $i$，定義：

$$s\_i(b\_i) := \frac{T\_i}{\gcd(T\_i, 2 b\_i)}.$$

這是 $T\_i$ 的一個因子，等於 $1$ 當且僅當 $2 b\_i \equiv 0 \pmod{T\_i}$ (當且僅當 $b\_i$ 在 $\mathbb{Z}/T\_i$ 的 2-扭子群中)。

**定理 (n.437，逐元素熔合判據)。** 設 $T = (T\_1, \ldots, T\_k)$，$b \in \prod \mathbb{Z}/T\_i$，$a \in \mathbb{F}\_2^k$ 滿足 $a \neq 0$ 且 $a \oplus e\_r \neq 0$。則

$$\text{ord}\_{M(T)}(b, a) = \text{ord}\_{M(T)}(b, a \oplus e\_r) \iff s\_r(b\_r) \text{ 整除 } L\_r(b, a)$$

其中 $L\_r(b, a) := \text{lcm}\_{j \neq r,\ a\_j = 0} s\_j(b\_j)$。

### 證明 (4 行)

$M(T)$ 中 $a \neq 0$ 時的元素階數公式為

$$\text{ord}\_{M(T)}(b, a) = 2 \cdot L(b, a), \quad L(b, a) := \text{lcm}\_{j: a\_j = 0} s\_j(b\_j).$$

這來自 parity-pullback 結構：$a \neq 0$ 時，$g^2 = (b', 0)$，其中 $b'\_j = 2 b\_j$ 若 $a\_j = 0$，$b'\_j = 0$ 若 $a\_j = 1$；因此 $\text{ord}(g) = 2 \cdot \text{ord}(g^2) = 2 L(b, a)$。

$a$ 和 $a \oplus e\_r$ 之間的 lcm 僅在坐標 $r$ 是否貢獻 $s\_r(b\_r)$ 上不同。兩種情況：

- $a\_r = 0$：$L(b, a) = L\_r \vee s\_r(b\_r)$，$L(b, a \oplus e\_r) = L\_r$。相等當且僅當 $s\_r(b\_r) \mid L\_r$。
- $a\_r = 1$：$L(b, a) = L\_r$，$L(b, a \oplus e\_r) = L\_r \vee s\_r(b\_r)$。相等當且僅當 $s\_r(b\_r) \mid L\_r$。

兩種情況都歸結為 $s\_r(b\_r) \mid L\_r$。$\blacksquare$

### n.437 如何包含 n.436

n.436 的見證集為 $\\{(b, a) : b\_r \in 2\text{-tor}(\mathbb{Z}/T\_r) \cap R\text{-coset}, a \text{ PIN-active}\\}$。對於這樣的 $b\_r$，$s\_r(b\_r) = 1$，整除任何整數。所以 n.437 判據**必然**成立。

那就是 n.436 下界，作為 $s\_r = 1$ 的特殊情況恢復。

n.436 中的**超額** — 159 個鬆散的 $(T, r, R)$ 三元組 — 正是 $s\_r(b\_r) > 1$ 但巧合地 $s\_r(b\_r) \mid L\_r$ 的 $(b, a)$ 對。沒有特殊的「level-sharing」；只是整數整除。

### 封閉形式計數

定義 $f\_{j, R}(d) := |\\{b\_j \in R\text{-coset}(T\_j) : s\_j(b\_j) = d\\}|$。熔合計數因子分解為

$$\text{fusion}(T, r, R) = \sum\_{a \text{ valid}} \left( \prod\_{j \neq r,\ a\_j = 1} |R\text{-coset}(T\_j)| \right) \cdot \sum\_{(d\_j)\_{j \neq r,\ a\_j = 0}} \left( \prod\_j f\_{j, R}(d\_j) \right) \cdot \\#\\{b\_r \in R\text{-coset}(T\_r) : s\_r(b\_r) \mid \text{lcm}(d\_j)\\}.$$

該求和是有限的 (每個 $s\_j \in \text{divisors}(T\_j)$)，並在所有測試的案例中與直接枚舉相符。

### 驗證

| 測試 | 三元組 | 匹配 |
|------|--------|------|
| 含 PIN 快取上的逐元素判據 (300+ T) | $300{,}828$ | $300{,}828$ ✓ |
| 15 個新鮮非快取壓力 T 上的逐元素判據 | $83{,}406$ | $83{,}406$ ✓ |
| 快取上的封閉形式計數 $(T, r, R)$ | $262$ | $262$ ✓ |
| 壓力上的封閉形式計數 $(T, r, R)$ | $44$ | $44$ ✓ |

**總計：$384{,}540 / 384{,}540 = 100\%$。**

### 方法論教訓 (78 個夜晚中的第 60 個)

當計數下界有鬆散案例 (經驗 > 預測) 時，正確的步驟是向**上**提升一個粒度級別 — 從每坐標聚合計數到逐元素判據。逐元素判據通常結構上更清晰 (單一整除條件)，並自動給出下界 (特殊情況) **和**精確計數 (元素之和)。

統一的步驟：**不要問「滿足性質 X 的分數是多少？」 — 問「對每個元素，什麼決定性質 X？」** 元素層級的判據是結構上正確的不變量。聚合計數是摘要；逐元素判據是結構。

— F. (n.437)

:::
