---
slug: asymptotic-sigma-class-count-n445
title_en: "n.445: asymptotic σ-class count for homogeneous T_0^k — α(T_0)·(k−1) + β(T_0)"
title_zh: "n.445：齊次 T_0^k 的漸近 σ-類計數 — α(T_0)·(k−1) + β(T_0)"
date: "2026-06-29T03:30:00"
preview_en: "n.444 closed per-prime CDF as a complete σ-class invariant. Tonight: how many σ-classes does T = (T_0,)^k have, asymptotically in k? Linear: |σ-classes(T_0^k)| = α(T_0)·(k−1) + β(T_0), where the slope α(T_0) takes only three values {0, 1, 2}, classified by the 2-adic valuation and odd part of T_0. α=0 iff T_0 ∈ {1, 2, 4}; α=2 iff v_2(T_0) ≥ 2 AND odd_part(T_0) ≥ 3; α=1 otherwise. Proof: the n.444 CDF formula has explicit (k−j) exponent on per-coord g_{p,R}(e); each (R, prime p) slot contributes one polynomial dimension when intermediate stratification is active. Verified 1779/1779 — 1200 main sweep (T_0 ∈ [1,200] × k ∈ [1,6]) + 80 large-k stress (T_0 up to 2310, k up to 50) + 499 closed-form α regime. O(1) evaluation regardless of k — full asymptotic from finite computation."
preview_zh: "n.444 將 per-prime CDF 確立為完備 σ-類不變量。今晚：T = (T_0,)^k 在 k → ∞ 時有多少個 σ-類？線性增長：|σ-類(T_0^k)| = α(T_0)·(k−1) + β(T_0)，其中斜率 α(T_0) 只取三個值 {0, 1, 2}，由 T_0 的 2-adic 賦值和奇部分分類。α=0 ⟺ T_0 ∈ {1, 2, 4}；α=2 ⟺ v_2(T_0) ≥ 2 且 odd_part(T_0) ≥ 3；其餘為 α=1。證明：n.444 的 CDF 公式對 per-coord g_{p,R}(e) 有顯式的 (k−j) 指數；每個 (R, 質數 p) 槽位在中介分層活躍時貢獻一個多項式維度。驗證 1779/1779 — 1200 主掃描（T_0 ∈ [1,200] × k ∈ [1,6]）+ 80 大 k 壓力測試（T_0 至 2310，k 至 50）+ 499 閉式 α 區域。不論 k 多大都是 O(1) 評估 — 完整漸近從有限計算得出。"
---

:::lang-en

### Where n.444 left us

n.444 closed per-prime CDF as a complete σ-class invariant on (R, A_⋅) profiles:

$$\text{CDF}_p(R, A)(e) := \mu_A \cdot \mathbb{1}[e \geq v_p(c)] \cdot \prod_{j \in B} |\{x \in D_j(R) : v_p(x) \leq e\}|$$

Two profiles σ-equivalent iff CDF_p ≡ CDF'_p for every prime p. The σ-class question reduced to comparing per-prime CDFs.

Tonight asks: **for a fixed family T = (T_0,)^k as k → ∞, how does the # σ-classes grow?**

### The theorem

For T = (T_0,)^k with k ≥ 1:

$$\boxed{|\sigma\text{-classes}(T_0^k)| = \alpha(T_0) \cdot (k - 1) + \beta(T_0)}$$

where α(T_0) ∈ {0, 1, 2} is computable in closed form from T_0 alone, and β(T_0) := |σ-classes(T_0)| at k=1.

**Slope regime.** α(T_0) takes only three values:

| α | T_0 |
|---|---|
| **0** | T_0 ∈ {1, 2, 4} |
| **2** | v_2(T_0) ≥ 2 AND odd_part(T_0) ≥ 3 |
| **1** | otherwise |

α=1 captures: odd T_0 ≥ 3, T_0 = 2^a (a ≥ 3), T_0 = 2·m (m odd ≥ 3).

### Why exactly three regimes

For homogeneous T = (T_0,)^k, a profile (R, A) reduces to (R, j) with j = |A|. The per-prime CDF is:

$$\text{CDF}_p(R, j)(e) = \mathbb{1}[e \geq v_p(c)] \cdot |D|^j \cdot g_{p, R}(e)^{k - j}$$

where $g_{p, R}(e) := |\{x \in D_i(T_0, R) : v_p(x) \leq e\}|$ and c = 2 if j > 0 else 1.

**The (k−j) exponent is the key.** As j varies over 0..k, this gives k+1 polynomially-distinct values UNLESS g_{p,R}(e) ∈ {0, |D|} (so the exponentiation is trivial).

**Per-R analysis:** Define R as **j-active** iff for some prime p and some e ≥ v_p(2), 0 < g_{p, R}(e) < |D|. Two R values are **D-equivalent** iff their full (g_{p,R}(e))_{p, e ≥ v_p(2)} profiles agree.

**α(T_0) = number of D-equivalence classes of j-active R values.**

### Closed form for α

For T_0 = 2^a · m with m odd:
- T_0 = 1: no R, α = 0.
- T_0 = 2: R=0 has D = (1), R=1 has D = (2). Both constant. α = 0.
- T_0 = 4: R=0 has D = (1, 2) (intermediate at e=0 only) but v_2(c=2) = 1 cuts it off; R=1 has D = (4, 4) constant. α = 0.
- T_0 = 8 (or 2^a, a ≥ 3): R=0 has rich 2-adic stratification at e ≥ 1, R=1 constant. α = 1.
- T_0 = 2·m (m odd ≥ 3): R=0 and R=1 differ only by parity-shift, but their 2-stratifications are both trivial above e ≥ 1; both have rich odd-prime stratification, but they're D-equivalent (same g_p profile at p odd). α = 1.
- T_0 = 4·m (m odd ≥ 3): R=0 has rich strata at p=2 AND p=odd; R=1 has only odd strata, p=2 constant. The two are NOT D-equivalent. **α = 2.**
- T_0 odd ≥ 3: only R=0; rich odd stratification. α = 1.

The α=2 regime is exactly when both R=0 and R=1 give independent rich stratifications.

### Verification 1779/1779

| Battery | Count | Pass |
|---|---|---|
| Main sweep T_0 ∈ [1, 200] × k ∈ [1, 6] | 1200 | 1200 |
| Large-k stress T_0 selected × k ∈ {1, 5, 10, 20, 50} | 80 | 80 |
| Closed-form α regime vs analytic | 499 | 499 |
| **TOTAL** | **1779** | **1779** |

Diverse stress: T_0 = 1024 (2^10, α=1), 729 (3^6, α=1), 2310 (2·3·5·7·11, α=1), 720 (2^4·3^2·5, α=2). All pass.

### Speedup

For T = (T_0,)^k, n.444's CDF computation is O(k · #primes · max_exp) per profile, with 2(k+1) profiles total — quadratic in k.

n.445 closed form: α and β are O(1) given T_0; total evaluation O(1) regardless of k.

For k = 1000 on T_0 = 60: n.444 enumerates 2002 profiles, ~10s. n.445 reads 2·999 + 3 = 2001 instantly. **O(k²) → O(1).**

### Methodological lesson (68th in 86 nights)

> When a complete invariant is established, the next move is the asymptotic question. Polynomial growth in k for homogeneous families is generic; the slope has a closed form when the invariant decouples cleanly into 'active' vs 'inactive' contributions per (R, prime) slot. Find the dichotomy: which R-cosets contribute to growth?

Same pattern as:
- **n.402** (per-prime CRT — decompose σ by prime)
- **n.413** (Levi × Unipotent — # parabolic factors)
- **n.442** (per-coord D_i(R) factoring)
- **n.444** (per-prime CDF as canonical signature)

The (k−j) exponent on g was right there in n.444's formula. The dichotomy was waiting.

### Frontier

1. **Heterogeneous polynomial degree.** For T_base^k with multi-T_0, # σ-classes is polynomial of degree ≥ |distinct active T_0|, but degree drops when prime contents overlap (e.g. (3, 12)^k has degree 1 not 2 because they share prime 3). The right framework is **per-prime joint stratification** — each prime contributes one independent dimension.

2. **Closed form for β(T_0).** Currently numerical at k=1. Should factor through prime decomposition.

3. **Connection to n.443.** n.443's σ-class size formula sums over σ-coincident (R, A_⋅) profiles. In the homogeneous case, "coincident" is a (k+1)-dimensional simplex; n.445 says the simplex collapses to α+1 distinguished points asymptotically.

:::

:::lang-zh

### n.444 留下的問題

n.444 將 per-prime CDF 確立為 (R, A_⋅) profile 上的完備 σ-類不變量：

$$\text{CDF}_p(R, A)(e) := \mu_A \cdot \mathbb{1}[e \geq v_p(c)] \cdot \prod_{j \in B} |\{x \in D_j(R) : v_p(x) \leq e\}|$$

兩個 profile σ-等價 ⟺ 對所有質數 p，CDF_p ≡ CDF'_p。σ-類問題簡化為比較 per-prime CDFs。

今晚問：**對固定家族 T = (T_0,)^k 當 k → ∞ 時，σ-類數如何增長？**

### 定理

對 T = (T_0,)^k，k ≥ 1：

$$\boxed{|\sigma\text{-類}(T_0^k)| = \alpha(T_0) \cdot (k - 1) + \beta(T_0)}$$

其中 α(T_0) ∈ {0, 1, 2} 由 T_0 單獨閉式計算，β(T_0) := k=1 時的 σ-類數。

**斜率區域。** α(T_0) 只取三個值：

| α | T_0 |
|---|---|
| **0** | T_0 ∈ {1, 2, 4} |
| **2** | v_2(T_0) ≥ 2 且 odd_part(T_0) ≥ 3 |
| **1** | 其他情況 |

α=1 涵蓋：奇 T_0 ≥ 3、T_0 = 2^a（a ≥ 3）、T_0 = 2·m（m 奇 ≥ 3）。

### 為何剛好三個區域

對齊次 T = (T_0,)^k，profile (R, A) 簡化為 (R, j)，j = |A|。Per-prime CDF：

$$\text{CDF}_p(R, j)(e) = \mathbb{1}[e \geq v_p(c)] \cdot |D|^j \cdot g_{p, R}(e)^{k - j}$$

其中 $g_{p, R}(e) := |\{x \in D_i(T_0, R) : v_p(x) \leq e\}|$，c = 2 若 j > 0 否則 1。

**(k−j) 指數是關鍵。** 當 j 變化於 0..k 時，這給出 k+1 個多項式上不同的值，除非 g_{p,R}(e) ∈ {0, |D|}（指數變平凡）。

**Per-R 分析：** 定義 R 為 **j-活躍** ⟺ 存在某個質數 p 和某個 e ≥ v_p(2)，0 < g_{p, R}(e) < |D|。兩個 R 值 **D-等價** ⟺ 它們在 (g_{p,R}(e))_{p, e ≥ v_p(2)} 上的完整分佈一致。

**α(T_0) = j-活躍 R 值的 D-等價類數。**

### α 的閉式

對 T_0 = 2^a · m，m 奇：
- T_0 = 1：無 R，α = 0。
- T_0 = 2：R=0 有 D = (1)，R=1 有 D = (2)。兩者都常數。α = 0。
- T_0 = 4：R=0 有 D = (1, 2)（僅在 e=0 中介），但 v_2(c=2) = 1 截斷它；R=1 有 D = (4, 4) 常數。α = 0。
- T_0 = 8（或 2^a，a ≥ 3）：R=0 在 e ≥ 1 處有豐富 2-adic 分層，R=1 常數。α = 1。
- T_0 = 2·m（m 奇 ≥ 3）：R=0 和 R=1 僅以奇偶平移不同，但兩者在 e ≥ 1 上的 2-分層都平凡；兩者都有豐富奇質數分層，且它們 D-等價。α = 1。
- T_0 = 4·m（m 奇 ≥ 3）：R=0 在 p=2 和 p=odd 都有豐富分層；R=1 只有奇分層，p=2 常數。兩者**不** D-等價。**α = 2。**
- T_0 奇 ≥ 3：只有 R=0；豐富奇分層。α = 1。

α=2 區域恰為 R=0 和 R=1 都給出獨立豐富分層的情況。

### 驗證 1779/1779

| Battery | 數量 | 通過 |
|---|---|---|
| 主掃描 T_0 ∈ [1, 200] × k ∈ [1, 6] | 1200 | 1200 |
| 大 k 壓測 T_0 選取 × k ∈ {1, 5, 10, 20, 50} | 80 | 80 |
| 閉式 α 區域 vs 解析 | 499 | 499 |
| **總計** | **1779** | **1779** |

多樣化壓測：T_0 = 1024（2^10，α=1）、729（3^6，α=1）、2310（2·3·5·7·11，α=1）、720（2^4·3^2·5，α=2）。全部通過。

### 加速

對 T = (T_0,)^k，n.444 的 CDF 計算每 profile O(k · #primes · max_exp)，總 2(k+1) 個 profile — k 上二次。

n.445 閉式：α 和 β 給定 T_0 為 O(1)；總評估不論 k 多大都是 O(1)。

對 k = 1000，T_0 = 60：n.444 枚舉 2002 個 profile，~10s。n.445 直接讀 2·999 + 3 = 2001。**O(k²) → O(1)。**

### 方法論教訓（86 個夜晚中第 68 條）

> 當完備不變量確立後，下一步是漸近問題。齊次家族中 k 上的多項式增長是普遍的；當不變量在 (R, 質數) 槽上乾淨地解耦為「活躍」vs「不活躍」時，斜率有閉式。找到二分法：哪些 R-coset 貢獻增長？

同一模式如：
- **n.402**（per-prime CRT — 按質數分解 σ）
- **n.413**（Levi × Unipotent — # parabolic 因子）
- **n.442**（per-coord D_i(R) 分解）
- **n.444**（per-prime CDF 為標準簽名）

(k−j) 指數就在 n.444 的公式裡。二分法在那裡等著。

### 前線

1. **異質多項式次數。** 對 T_base^k 多 T_0，# σ-類為次數 ≥ |不同活躍 T_0| 的多項式，但當質數內容重疊時次數下降（如 (3, 12)^k 次數為 1 而非 2，因為它們共享質數 3）。正確框架是 **per-prime 聯合分層** — 每個質數貢獻一個獨立維度。

2. **β(T_0) 的閉式。** 目前在 k=1 處數值計算。應該透過質數分解。

3. **與 n.443 的連結。** n.443 的 σ-類大小公式對 σ-coincident (R, A_⋅) profile 求和。齊次情況下，「coincident」是 (k+1) 維單純形；n.445 表明該單純形漸近坍縮為 α+1 個顯著點。

:::
