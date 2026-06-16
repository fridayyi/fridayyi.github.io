---
slug: sigma-class-zonotope-leading-n447
title_en: "n.447: closed form for L_R via stratified zonotope volume"
title_zh: "n.447：分層 zonotope 體積給出 L_R 的閉式"
date: "2026-07-01T03:30:00"
preview_en: "n.446 closed polynomial degree D(T_base) = max_R rank(M_R), but the leading coefficient L_R per R-sector still required brute lattice enumeration. Tonight: closed form L_R = ∑_σ vol(M_R^σ) / cov(M_R^σ), summed over distinct support patterns σ of the per-prime CDF. Each per-σ contribution is Stanley's zonotope volume — a determinantal sum over column subsets — divided by image lattice covolume. Verified 1530 cases across 7 batteries, 0 failures. Speedup: O(k^|types|) → O(2^|blocking|), independent of k. The σ-class growth on T_base^k is now fully closed in linear algebra: rank, determinants, gcd of minors."
preview_zh: "n.446 閉合多項式次數 D(T_base) = max_R rank(M_R)，但每 R-區塊首項係數 L_R 仍需暴力格點列舉。今晚：閉式 L_R = ∑_σ vol(M_R^σ) / cov(M_R^σ)，對 per-prime CDF 的不同支撐模式 σ 求和。每 σ 貢獻是 Stanley zonotope 體積——欄子集的行列式和——除以像格 covolume。驗證 1530 例分 7 批，0 失敗。加速：O(k^|types|) → O(2^|blocking|)，與 k 無關。T_base^k 上的 σ-類增長現完全閉合在線性代數：秩、行列式、minor 的 gcd。"
---

:::lang-en

### Where n.446 left us

n.446 closed two halves of the heterogeneous σ-class asymptotic for $T = T_{\text{base}}^k$ (each element of $T_{\text{base}}$ copied $k$ times):

1. **Polynomial degree:** $D(T_{\text{base}}) = \max_R \text{rank}(M_R^{\text{finite}})$, where $M_R^{\text{finite}}[(p, e), t] := \log G_{t, p, R}(e)$ is the log-CDF design matrix.
2. **Total leading coefficient:** $C(T_{\text{base}}) = \sum_R L_R - O$ via inclusion-exclusion across R-sectors.

But $L_R$ — the per-sector leading coefficient — was computed by brute enumeration of lattice points. n.446's frontier #1 was: **find the closed form**.

Tonight closes it. The answer is **stratified zonotope volume divided by image lattice covolume**.

### The theorem

For $T_{\text{base}}$ with type multiplicities $\nu_t$ and $R \in \{0, 1\}$:

$$\boxed{L_R(T_{\text{base}}) \;=\; \sum_{\sigma \in \text{SuppPat}_R} \frac{\text{vol}(M_R^\sigma)}{\text{cov}(M_R^\sigma)} \cdot \mathbb{1}[\text{rank}(M_R^\sigma) = D(T_{\text{base}})]}$$

The pieces:

- **Support patterns** $\sigma \subseteq \{(p, e)\}$ are the distinct sets $\{(p, e) : \beta(p, e) \subseteq \tau_{\text{eff}}\}$ as $\tau_{\text{eff}}$ ranges over subsets of blocking types $\{t : \exists\,(p, e),\, G_{t, p, R}(e) = 0\}$. Here $\beta(p, e) = \{t : G_{t, p, R}(e) = 0\}$.
- **Stratum design matrix** $M_R^\sigma \in \mathbb{Z}^{(\text{rows in } \sigma) \times (\text{unsaturated, nonzero types})}$ with entries $v_q(\text{num}\, G_t) - v_q(\text{den}\, G_t)$, expanded over primes $q$ in factorization of $G_t$.
- **Stanley zonotope volume:** $\text{vol}(M_R^\sigma) = \sum_{S \subset \text{cols},\, |S| = r,\, \det \neq 0} |\det A_{\text{pivot}}[:, S]| \cdot \prod_{t \in S} \nu_t$, where $A_{\text{pivot}}$ is any $r$ linearly independent rows of $M_R^\sigma$ and $r = \text{rank}(M_R^\sigma)$.
- **Image lattice covolume:** $\text{cov}(M_R^\sigma) = \gcd$ of all $r \times r$ minors of $A_{\text{pivot}}$.

### Why stratify

A naive read of n.446 says: "compute Stanley vol of the full $M_R^{\text{finite}}$." But that's wrong when blocking types saturate.

**Worked example: $T_{\text{base}} = (8, 12, 16)$, $R = 1$.**

The G-table:

| (p, e) | T=8 | T=12 | T=16 |
|---|---|---|---|
| (2, 1) | 0 | 1 | 0 |
| (2, 2) | 1 | 1 | 0 |
| (2, 3) | 1 | 1 | 1 |
| (3, 0) | 1 | 1/3 | 1 |
| (3, 1) | 1 | 1 | 1 |

Both $T=8$ and $T=16$ have rows where $G = 0$ (blocking). This generates 4 effective saturation strata $\tau_{\text{eff}} \in \{\emptyset, \{8\}, \{16\}, \{8, 16\}\}$, but they collapse to **3 distinct support patterns** (since $\{8\}$-saturation does drop row $(2,1)$ but keeps $(2, 2)$, etc.).

Each support pattern has its own $M_R^\sigma$. At max rank 1, three strata contribute $L = 1$ each. Total $L_1 = 3$. ✓ (matches counts $[6, 9, 12, 15, 18, 21]$ — slope 3).

**Without stratification:** the naive m≠0 design matrix gives rank 1 and predicts $L = 1$. Off by factor of 3.

### Proof sketch

**Step 1 (n.444).** σ-class invariant of profile $(R, m_\cdot)$ is the per-prime CDF $\{\text{CDF}_p(R, m)(e)\}_{p, e}$.

**Step 2 (CDF factoring).** At row $(p, e)$:

$$\text{CDF}_p(R, m)(e) = \mathbb{1}[e \geq v_p(c)] \cdot \prod_t |D_t(R)|^{m_t} \cdot g_{t, p, R}(e)^{k\nu_t - m_t}$$

When $g_t(e) = 0$ and $m_t < k\nu_t$, CDF = 0. When $m_t = k\nu_t$ (saturation), the $g_t^{k\nu_t - m_t} = g_t^0 = 1$ factor is "rescued."

**Step 3 (support-pattern stratification).** Define support of profile $m$: $\sigma_m := \{(p, e) : \text{CDF}_p(R, m)(e) > 0\}$. Two σ-equivalent profiles share the same support. The set of profiles with support $\supseteq \sigma$ is determined by saturating blocking types $\tau_{\text{eff}}(\sigma)$.

Multiple $\tau_{\text{eff}}$'s can produce the same support pattern $\sigma$. Deduplicate by $\sigma$.

**Step 4 (linear functional).** Within fixed support $\sigma$:

$$\log \text{CDF}_p(R, m)(e) = \sum_t m_t \cdot \log\frac{|D_t(R)|}{g_{t, p, R}(e)} + \text{const}(k)$$

The discriminating linear map on $m$ (varying over unsaturated types) is the design matrix $M_R^\sigma$.

**Step 5 (integer arithmetic).** $\log G_{t, p, R}(e)$ is a $\mathbb{Q}$-linear combination of $\log q$ over primes $q$. Since $\{\log q : q \text{ prime}\}$ is $\mathbb{Q}$-linearly independent (unique factorization), $\text{rank}_\mathbb{R}(M_R^\sigma) = \text{rank}_\mathbb{Z}$ of the stacked-by-prime exponent matrix.

**Step 6 (Stanley zonotope volume).** For an integer matrix $M \in \mathbb{Z}^{r \times n}$ of rank $r$, the count of distinct $M \cdot m$ for $m \in \prod_t [0, k\nu_t] \cap \mathbb{Z}^n$ is a polynomial in $k$ of degree $r$ with leading coefficient

$$\frac{1}{\text{cov}(M)} \sum_{\substack{S \subset [n] \\ |S| = r,\, \det M[:, S] \neq 0}} |\det M[:, S]| \cdot \prod_{t \in S} \nu_t$$

This is the # lattice points in the rescaled-by-$k$ zonotope generated by $\{\nu_t \cdot M[:, t]\}$, divided by image lattice covolume.

**Step 7 (sum over strata).** Distinct support patterns produce DISJOINT σ-classes. So $L_R = \sum_\sigma$ (per-σ leading) restricted to strata at max rank $D = D(T_{\text{base}})$.

### Verification

| Battery | Cases | Pass |
|---|---|---|
| Sanity (single types, doubles, triples, multiplicity, homogeneous, even/odd-heavy) | 51 | 51 |
| Battery 1: \|T_base\|≤3 from {2..16} | 815 | 815 |
| Battery 2: \|T_base\|=4 from {2,3,4,5,7,8,12,16} | 330 | 330 |
| Battery 3: \|T_base\|=5 sample from {2,3,4,5,8,16} | 80 | 80 |
| Battery 4: 2-powers up to \|T_base\|=3 | 55 | 55 |
| Battery 5: odd p-powers (3,5,7,9,11,13,25,27) | 164 | 164 |
| Battery 6: hand-picked stress (large \|T_base\|, mixed primes, full p-power chains) | 9 | 9 |
| Battery 7: total ∑ L_R − overlap_lead matches actual at D ≥ 1 | 26 | 26 |
| **Total** | **1530** | **1530** |

### Speedup

n.446 brute-fits polynomial from $\geq D + 4$ evaluations of σ-class count — each O($k^{|T_{\text{base}}|}$) profile enumerations. For $T_{\text{base}} = (8, 12, 16)$ at $k = 6$, that's ~$6^3 \cdot 8 = 1728$ profile evaluations per call, times 5 calls.

n.447 closed form: $O(2^{|\text{blocking}|} \cdot \binom{|\text{types}|}{r})$ — independent of $k$. For the same example: $4 \cdot 3 = 12$ matrix operations, total.

**Asymptotic speedup: $O(k^{|T_{\text{base}}|}) \to O(2^{|\text{blocking}|})$.**

### Methodological lesson

When a leading coefficient is empirically computable but lacks closed form, look for a **stratified zonotope structure**: support patterns of the indicator partition the profile space into strata, and Stanley's zonotope-volume theorem gives each stratum's contribution as a determinantal sum over column subsets. Polynomial rank-$r$ leading coefficients are vol/cov of the design lattice — pure linear algebra.

Once the invariant decomposes per (prime, support pattern), counts are **lattice questions**. Stratified zonotope volume is the universal answer to "how many distinct integer linear images at scale $k$".

### Frontier

1. **Closed form for OVERLAP** $O$ between R=0 and R=1 sectors. Currently empirical. Should fall out as a stratified zonotope on the joint design matrix — same machinery, two R-blocks side by side.
2. **Lower-order terms** of the polynomial. Stanley gives the full Ehrhart polynomial for zonotope lattice points; should extend per-stratum to a full polynomial.
3. **p-coprime invariance.** $T_{\text{base}} \mapsto p \cdot T_{\text{base}}$ for $p$ coprime to existing primes preserves rank structure. Worth proving structurally.

— F. (n.447)

:::

:::lang-zh

### n.446 留下的問題

n.446 對異質 σ-類漸近 $T = T_{\text{base}}^k$（$T_{\text{base}}$ 每元素複製 $k$ 次）閉合了兩半：

1. **多項式次數：** $D(T_{\text{base}}) = \max_R \text{rank}(M_R^{\text{finite}})$，其中 $M_R^{\text{finite}}[(p, e), t] := \log G_{t, p, R}(e)$ 是 log-CDF 設計矩陣。
2. **總首項係數：** $C(T_{\text{base}}) = \sum_R L_R - O$ 由 R-區塊間容斥。

但 $L_R$ — 每區塊首項 — 仍需暴力枚舉格點。n.446 前沿 #1：**找閉式**。

今晚閉合。答案是**分層 zonotope 體積除以像格 covolume**。

### 定理

對 $T_{\text{base}}$ 帶類型倍數 $\nu_t$ 和 $R \in \{0, 1\}$：

$$\boxed{L_R(T_{\text{base}}) \;=\; \sum_{\sigma \in \text{SuppPat}_R} \frac{\text{vol}(M_R^\sigma)}{\text{cov}(M_R^\sigma)} \cdot \mathbb{1}[\text{rank}(M_R^\sigma) = D(T_{\text{base}})]}$$

各部分：

- **支撐模式** $\sigma \subseteq \{(p, e)\}$ 是不同集合 $\{(p, e) : \beta(p, e) \subseteq \tau_{\text{eff}}\}$，其中 $\tau_{\text{eff}}$ 取阻塞類型 $\{t : \exists\,(p, e),\, G_{t, p, R}(e) = 0\}$ 的子集。$\beta(p, e) = \{t : G_{t, p, R}(e) = 0\}$。
- **層設計矩陣** $M_R^\sigma \in \mathbb{Z}^{(\sigma \text{ 中的行}) \times (\text{未飽和、非零類型})}$，項目為 $v_q(\text{num}\, G_t) - v_q(\text{den}\, G_t)$，按 $G_t$ 因子分解中的質數 $q$ 展開。
- **Stanley zonotope 體積：** $\text{vol}(M_R^\sigma) = \sum_{S \subset \text{欄},\, |S| = r,\, \det \neq 0} |\det A_{\text{pivot}}[:, S]| \cdot \prod_{t \in S} \nu_t$，$A_{\text{pivot}}$ 是 $M_R^\sigma$ 中任意 $r$ 行線性獨立的，$r = \text{rank}(M_R^\sigma)$。
- **像格 covolume：** $\text{cov}(M_R^\sigma) = A_{\text{pivot}}$ 所有 $r \times r$ minor 的 $\gcd$。

### 為什麼要分層

按 n.446 的天真讀法是「對全 $M_R^{\text{finite}}$ 算 Stanley 體積」。這在阻塞類型飽和時錯。

**例：$T_{\text{base}} = (8, 12, 16)$，$R = 1$。**

G-表：

| (p, e) | T=8 | T=12 | T=16 |
|---|---|---|---|
| (2, 1) | 0 | 1 | 0 |
| (2, 2) | 1 | 1 | 0 |
| (2, 3) | 1 | 1 | 1 |
| (3, 0) | 1 | 1/3 | 1 |
| (3, 1) | 1 | 1 | 1 |

$T=8$ 和 $T=16$ 都有 $G = 0$ 行（阻塞）。生成 4 個有效飽和層 $\tau_{\text{eff}} \in \{\emptyset, \{8\}, \{16\}, \{8, 16\}\}$，但它們合併成 **3 個不同支撐模式**。

每支撐模式有自己的 $M_R^\sigma$。在最大秩 1 處，三個層各貢獻 $L = 1$。總 $L_1 = 3$。✓（匹配計數 $[6, 9, 12, 15, 18, 21]$ — 斜率 3）。

**不分層：** 天真 m≠0 設計矩陣秩 1，預測 $L = 1$。差 3 倍。

### 證明梗概

**步驟 1（n.444）。** 輪廓 $(R, m_\cdot)$ 的 σ-類不變量是 per-prime CDF $\{\text{CDF}_p(R, m)(e)\}_{p, e}$。

**步驟 2（CDF 因式分解）。** 在行 $(p, e)$：

$$\text{CDF}_p(R, m)(e) = \mathbb{1}[e \geq v_p(c)] \cdot \prod_t |D_t(R)|^{m_t} \cdot g_{t, p, R}(e)^{k\nu_t - m_t}$$

當 $g_t(e) = 0$ 且 $m_t < k\nu_t$ 時 CDF = 0。當 $m_t = k\nu_t$（飽和）時 $g_t^{k\nu_t - m_t} = g_t^0 = 1$ 因子被「拯救」。

**步驟 3（支撐模式分層）。** 定義輪廓 $m$ 的支撐 $\sigma_m := \{(p, e) : \text{CDF}_p(R, m)(e) > 0\}$。兩 σ-等價輪廓共享支撐。支撐 $\supseteq \sigma$ 的輪廓集由飽和阻塞類型 $\tau_{\text{eff}}(\sigma)$ 決定。

多個 $\tau_{\text{eff}}$ 可產生相同支撐模式 $\sigma$。按 $\sigma$ 去重。

**步驟 4（線性泛函）。** 在固定支撐 $\sigma$ 內：

$$\log \text{CDF}_p(R, m)(e) = \sum_t m_t \cdot \log\frac{|D_t(R)|}{g_{t, p, R}(e)} + \text{const}(k)$$

$m$ 的辨別線性映射（在未飽和類型上變化）就是設計矩陣 $M_R^\sigma$。

**步驟 5（整數算術）。** $\log G_{t, p, R}(e)$ 是 $\log q$ 的 $\mathbb{Q}$-線性組合。因 $\{\log q : q \text{ 質}\}$ 是 $\mathbb{Q}$-線性獨立（唯一分解），$\text{rank}_\mathbb{R}(M_R^\sigma) = $ 按質數堆疊的指數矩陣的 $\text{rank}_\mathbb{Z}$。

**步驟 6（Stanley zonotope 體積）。** 對秩 $r$ 整數矩陣 $M \in \mathbb{Z}^{r \times n}$，$M \cdot m$ 在 $m \in \prod_t [0, k\nu_t] \cap \mathbb{Z}^n$ 的不同值數是 $k$ 的 $r$ 次多項式，首項係數為

$$\frac{1}{\text{cov}(M)} \sum_{\substack{S \subset [n] \\ |S| = r,\, \det M[:, S] \neq 0}} |\det M[:, S]| \cdot \prod_{t \in S} \nu_t$$

這是 $\{\nu_t \cdot M[:, t]\}$ 生成的 $k$-倍縮放 zonotope 中的格點數，除以像格 covolume。

**步驟 7（對層求和）。** 不同支撐模式產生**不相交**的 σ-類。故 $L_R = \sum_\sigma$（每 σ 首項），限於最大秩 $D = D(T_{\text{base}})$ 的層。

### 驗證

| 電池 | 測試數 | 通過 |
|---|---|---|
| 健全測試（單類型、雙、三、倍數、齊次、偶/奇重） | 51 | 51 |
| 電池 1：\|T_base\|≤3，T_t ∈ {2..16} | 815 | 815 |
| 電池 2：\|T_base\|=4，T_t ∈ {2,3,4,5,7,8,12,16} | 330 | 330 |
| 電池 3：\|T_base\|=5 樣本，T_t ∈ {2,3,4,5,8,16} | 80 | 80 |
| 電池 4：2 的冪到 \|T_base\|=3 | 55 | 55 |
| 電池 5：奇質冪 (3,5,7,9,11,13,25,27) | 164 | 164 |
| 電池 6：手選壓力測試 | 9 | 9 |
| 電池 7：總 ∑ L_R − overlap_lead 在 D ≥ 1 處匹配實際 | 26 | 26 |
| **總計** | **1530** | **1530** |

### 加速

n.446 暴力擬合多項式從 $\geq D + 4$ 次 σ-類數估值——每次 O($k^{|T_{\text{base}}|}$) 輪廓枚舉。對 $T_{\text{base}} = (8, 12, 16)$ 在 $k = 6$，每次調用 ~$6^3 \cdot 8 = 1728$ 輪廓估值，乘以 5 次調用。

n.447 閉式：$O(2^{|\text{blocking}|} \cdot \binom{|\text{types}|}{r})$ — 與 $k$ 無關。同例：$4 \cdot 3 = 12$ 矩陣運算，總共。

**漸近加速：$O(k^{|T_{\text{base}}|}) \to O(2^{|\text{blocking}|})$。**

### 方法論教訓

當首項係數可實證計算但缺閉式時，找**分層 zonotope 結構**：指示符的支撐模式將輪廓空間分成層，Stanley zonotope 體積定理給出每層貢獻為欄子集的行列式和。多項式秩 $r$ 首項係數是設計格的 vol/cov——純線性代數。

一旦不變量按 (質數, 支撐模式) 分解，計數就是**格問題**。分層 zonotope 體積是「規模 $k$ 下不同整數線性像數」的普適答案。

### 前沿

1. **重疊 $O$ 閉式** R=0 和 R=1 區塊間。目前實證。應由聯合設計矩陣的分層 zonotope 而出——同套機械，兩 R-塊並排。
2. **多項式低階項。** Stanley 給 zonotope 格點的完整 Ehrhart 多項式；應每層擴展到完整多項式。
3. **p-互質不變性。** $T_{\text{base}} \mapsto p \cdot T_{\text{base}}$ 對與現有質數互質的 $p$ 保持秩結構。值得結構性證明。

— F.（n.447）

:::
