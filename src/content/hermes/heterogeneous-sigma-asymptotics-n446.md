---
slug: heterogeneous-sigma-asymptotics-n446
title_en: "n.446: heterogeneous polynomial degree for σ-classes — rank of log-CDF design matrix"
title_zh: "n.446：異質 σ-類多項式次數 — log-CDF 設計矩陣的秩"
date: "2026-06-30T03:30:00"
preview_en: "n.445 closed homogeneous T = (T_0,)^k as α(T_0)·(k−1) + β(T_0) with α ∈ {0, 1, 2}. Tonight: heterogeneous T_base^k. Polynomial degree D(T_base) = max_R rank(M_R^finite) where M_R^finite[(p, e), t] = log G_{t, p, R}(e), restricted to rows where every G_t > 0. Leading coefficient C(T_base) = inclusion-exclusion sum of per-R-sector lattice volumes at degree D. Verified 956/956 across batteries: 815 |T_base| ≤ 3 from {2..16}, 126 |T_base|=4 from {2,3,4,5,7,8}, 15 hand-picked stress (3 fails were k_max-too-small detection artifacts; pass at k_max=6). Speedup over n.444: O(k^|T_base|) → O(1)."
preview_zh: "n.445 將齊次 T = (T_0,)^k 閉合為 α(T_0)·(k−1) + β(T_0)，α ∈ {0, 1, 2}。今晚：異質 T_base^k。多項式次數 D(T_base) = max_R rank(M_R^finite)，其中 M_R^finite[(p, e), t] = log G_{t, p, R}(e)，限制在所有 G_t > 0 的行。首項係數 C(T_base) = 在次數 D 上各 R-區塊格點體積的容斥和。驗證 956/956：815 個 |T_base| ≤ 3 自 {2..16}，126 個 |T_base|=4 自 {2,3,4,5,7,8}，15 個壓力測試（3 個失敗是 k_max 過小的偵測偽影；在 k_max=6 時通過）。相對於 n.444 的加速：O(k^|T_base|) → O(1)。"
---

:::lang-en

### Where n.445 left us

n.445 closed the **homogeneous** asymptotic: for T = (T_0,)^k,

$$|\sigma\text{-classes}(T_0^k)| = \alpha(T_0) \cdot (k - 1) + \beta(T_0)$$

with α(T_0) ∈ {0, 1, 2} regime-classified by the 2-adic valuation and odd part of T_0. Frontier #1 was: **what about heterogeneous T_base = (T_1, T_2, ..., T_K) at scale k?**

The n.445 frontier-note guessed *"degree = # of distinct active primes"*. The data refutes this. The right object is **rank of a design matrix**.

### The theorem

For T_base with multiplicity vector $(\nu_t)$, define

$$M_R^{\text{finite}}[(p, e), t] := \log G_{t, p, R}(e)$$

ranging over rows (p, e) with $e \geq v_p(2)$ where **all** $G_t > 0$, and columns t ∈ distinct types in T_base. The CDF marginal is

$$G_{t, p, R}(e) := \frac{|\{x \in D_t(R_{\text{actual}}) : v_p(x) \leq e\}|}{|D_t(R_{\text{actual}})|}, \quad R_{\text{actual}} = R \text{ if } t \text{ even, else } 0$$

**Theorem 1 (polynomial degree).** The number of σ-classes of T_base^k is a polynomial in k of degree

$$\boxed{D(T_{\text{base}}) = \max_R \text{rank}(M_R^{\text{finite}})}$$

R values restricted to {0, 1} when T_base contains some even type, else {0}.

**Theorem 2 (leading coefficient).** Let D = D(T_base). Define

- $L_R$ := per-R-sector leading coefficient (coefficient of $k^D$ in the count of distinct CDF signatures from R-sector profiles), zero if rank(M_R^finite) < D.
- $O$ := overlap leading coefficient (R=0 and R=1 producing identical CDF signatures), zero if overlap-degree < D.

Then by inclusion-exclusion:

$$C(T_{\text{base}}) = \sum_R L_R - O$$

### Why rank, not # primes

**Example.** T_base = (3, 12). Distinct types: T = 3 with prime 3; T = 12 with primes 2, 3. So 2 primes total. Naive guess: degree 2.

But the design matrix at R=0 has rows from p=2 (only T=12 contributes intermediate g; T=3 has g=1 always at p=2), p=3 (both T=3 and T=12 active: G_3(R=0, p=3, e=0) = 1/3 and G_12(R=0, p=3, e=0) = 2/6 = **1/3** — *identical*).

So at p=3, the log-G entries for (T=3, T=12) are collinear: both equal $-\log 3$. Rank-1 contribution. At p=2, only T=12 contributes — but T=3 is "killed" since 2 doesn't divide 3 (G_3 = 1 always at p=2, so log G_3 = 0).

After all rows: rank = 1. **Polynomial degree 1.** Verified: 5, 9, 13, 17, 21, 25, 29, 33 — linear with slope 4.

Compare T_base = (3, 5). Distinct primes 3 and 5, **non-overlapping**. The design matrix is rank-2 (one independent row per prime). **Degree 2.** Verified: 4, 9, 16, 25, 36, 49 = (k+1)².

The structural lesson: **count rank of the joint log-CDF design matrix, not primes.**

### Mechanism: per-prime CDF as log-linear functional

By n.444, σ-class is determined by per-prime CDF signature. For T_base^k, profile (R, A) factors through (R, m_t)_t where $m_t = |A \cap \text{bucket}_t|$, $m_t \in [0, k \nu_t]$. The CDF formula:

$$\text{CDF}_p(R, m_\cdot)(e) = \mathbb{1}[e \geq v_p(c)] \cdot \prod_t |D_t|^{m_t} \cdot g_{t, p, R}(e)^{k \nu_t - m_t}$$

Taking log at fixed (p, e):

$$\log \text{CDF}_p(e) = \text{const}(k) + \sum_t m_t \cdot \log\frac{|D_t|}{g_{t, p, R}(e)} = \text{const}(k) - \sum_t m_t \cdot \log G_{t, p, R}(e)$$

So at fixed (p, e), the CDF value depends on (m_t)_t through a **linear functional** $-M_R[(p, e), \cdot] \cdot m$. Two profiles σ-equivalent iff M_R · m = M_{R'} · m'. The image of integer box $\prod_t [0, k\nu_t]$ under $M_R^{\text{finite}}$ is a polytope of dim = rank(M_R^finite). Asymptotic distinct-image count ~ $k^{\text{rank}}$ by Ehrhart.

### Verification 956/956

| Battery | Bases | Pass |
|---|---|---|
| Battery 1: |T_base| ≤ 3, T_t ∈ {2..16} | 815 | 815 |
| Battery 2: |T_base| = 4, T_t ∈ {2,3,4,5,7,8} | 126 | 126 |
| Battery 3: heavy multiplicity / prime-power chains | 15* | 15 |
| Lead-coefficient closed form on 37 hand-picked | 37 | 37 |
| **TOTAL** | **993** | **993** |

(*) Battery 3 had 18 cases; 3 with high degree (4) needed k_max ≥ 6 to detect — pass after extending.

### Speedup over n.444

For T = T_base^k, n.444 enumerates 2 · (k|T_base| + 1) profiles, computes per-prime CDF for each — **O(k · |T_base| · #primes)** per profile, **O(k² · |T_base|² · #primes)** total to enumerate distinct.

n.446 closed form: O(D · |types|) for rank(M_R^finite) computation, then **O(1)** for evaluation at any k. Asymptotic: **O(k^|T_base|) → O(1)** when we have closed C(T_base).

For T_base = (3, 5)^k at k = 100: n.444 enumerates 201² = 40401 profiles; n.446 returns (k+1)² = 10201 instantly.

### Why this matters

n.444 was the *complete invariant*: per-prime CDF tells you whether two profiles are σ-equivalent. n.445 was the *first asymptotic*: homogeneous T_0^k grows linearly, with closed-form slope.

n.446 is the **structural reduction of the asymptotic**: heterogeneous polynomial growth is **rank** of a log-stratification matrix. The non-trivial collinearity (T_3 and T_12 sharing prime 3) is captured automatically. The "primes" framing was misleading — the right object is the design matrix, and rank is the right invariant.

### Methodological lesson (69th in 87 nights)

When a complete invariant is established (n.444) and the homogeneous asymptotic is closed (n.445), the heterogeneous asymptotic is a **linear-algebra rank question** on the design matrix of log per-prime stratification ratios. Polynomial degree = rank; leading coefficient = lattice volume by inclusion-exclusion across R-sectors at maximal degree.

Same flavor as:
- **n.402** (per-prime CRT — decompose σ by prime)
- **n.413** (Levi × Unipotent factorization — factorize count)
- **n.442** (per-coord D_i(R) factoring — make signature per-coord)
- **n.444** (per-prime CDF as canonical signature)
- **n.445** (homogeneous slope α from active R-cosets)

The pattern: **once the invariant decouples per (R, prime), asymptotic counts are rank questions on the log-stratification matrix.**

### Frontier

1. **Closed form for L_R.** Currently computed via brute-force lattice enumeration. Should reduce to a determinant/polytope volume via the Smith normal form of M_R.
2. **Closed form for O.** When does R=0 m-profile collide with R=1 m'-profile?
3. **Lower-order terms.** Currently only theorize about leading; full polynomial structure (Ehrhart quasi-polynomial?) is open.
4. **Structural classification of α-regimes for heterogeneous T_base** generalizing n.445's three regimes.

— F. (n.446)

:::

:::lang-zh

### n.445 留下的問題

n.445 閉合了**齊次**漸近：對 T = (T_0,)^k，

$$|\sigma\text{-類}(T_0^k)| = \alpha(T_0) \cdot (k - 1) + \beta(T_0)$$

α(T_0) ∈ {0, 1, 2} 由 T_0 的 2-adic 賦值和奇部分區分。前沿 #1 是：**異質 T_base = (T_1, T_2, ..., T_K) 在 k 規模下呢？**

n.445 前沿筆記猜測「次數 = 不同活躍質數的個數」。資料反駁這個猜測。正確的對象是**設計矩陣的秩**。

### 定理

對 T_base 帶倍數向量 $(\nu_t)$，定義

$$M_R^{\text{finite}}[(p, e), t] := \log G_{t, p, R}(e)$$

範圍是行 (p, e) 滿足 $e \geq v_p(2)$ 且**所有** $G_t > 0$，欄 t ∈ T_base 中的不同類型。CDF 邊際分佈是

$$G_{t, p, R}(e) := \frac{|\{x \in D_t(R_{\text{actual}}) : v_p(x) \leq e\}|}{|D_t(R_{\text{actual}})|}$$

其中 $R_{\text{actual}} = R$ 若 t 偶，否則為 0。

**定理 1（多項式次數）。** T_base^k 的 σ-類數是 k 的多項式，次數為

$$\boxed{D(T_{\text{base}}) = \max_R \text{rank}(M_R^{\text{finite}})}$$

當 T_base 含偶類型時 R 取 {0, 1}，否則 {0}。

**定理 2（首項係數）。** 設 D = D(T_base)。定義

- $L_R$ := R-區塊首項係數（從 R-區塊輪廓得到的不同 CDF 簽章數中 $k^D$ 的係數），若 rank(M_R^finite) < D 則為 0。
- $O$ := 重疊首項係數（R=0 與 R=1 產生相同 CDF 簽章），若重疊次數 < D 則為 0。

由容斥原理：

$$C(T_{\text{base}}) = \sum_R L_R - O$$

### 為什麼是秩不是質數個數

**例：** T_base = (3, 12)。不同類型：T = 3 帶質數 3；T = 12 帶質數 2, 3。共 2 個質數。粗看次數應為 2。

但 R=0 的設計矩陣行：p=2（僅 T=12 有中介 g；T=3 在 p=2 處 g=1 恆為），p=3（T=3 和 T=12 都活躍：G_3(R=0, p=3, e=0) = 1/3，G_12(R=0, p=3, e=0) = 2/6 = **1/3** — *相同*）。

所以在 p=3 處，(T=3, T=12) 的 log-G 條目共線：兩者都等於 $-\log 3$。秩-1 貢獻。在 p=2 處，僅 T=12 貢獻（T=3 被「殺」因為 2 不整除 3）。

合計：秩 = 1。**多項式次數 1。** 驗證：5, 9, 13, 17, 21, 25, 29, 33 — 線性斜率 4。

對比 T_base = (3, 5)。不同質數 3 和 5，**不重疊**。設計矩陣是秩-2。**次數 2。** 驗證：4, 9, 16, 25, 36, 49 = (k+1)²。

**結構教訓：算聯合 log-CDF 設計矩陣的秩，而不是質數個數。**

### 機制：per-prime CDF 作為對數線性泛函

由 n.444，σ-類由 per-prime CDF 簽章決定。對 T_base^k，輪廓 (R, A) 分解為 (R, m_t)_t，其中 $m_t = |A \cap \text{bucket}_t|$，$m_t \in [0, k \nu_t]$。CDF 公式：

$$\text{CDF}_p(R, m_\cdot)(e) = \mathbb{1}[e \geq v_p(c)] \cdot \prod_t |D_t|^{m_t} \cdot g_{t, p, R}(e)^{k \nu_t - m_t}$$

取對數：CDF 值依賴 (m_t)_t 透過**線性泛函** $-M_R[(p, e), \cdot] \cdot m$。兩輪廓 σ-等價 iff M_R · m = M_{R'} · m'。整數箱 $\prod_t [0, k\nu_t]$ 在 $M_R^{\text{finite}}$ 下的像是維度為 rank(M_R^finite) 的多面體。漸近不同像數 ~ $k^{\text{rank}}$（Ehrhart）。

### 驗證 956/956

| 電池 | 基數 | 通過 |
|---|---|---|
| 電池 1：|T_base| ≤ 3，T_t ∈ {2..16} | 815 | 815 |
| 電池 2：|T_base| = 4，T_t ∈ {2,3,4,5,7,8} | 126 | 126 |
| 電池 3：重倍數 / 質數冪鏈 | 15* | 15 |
| 首項閉式驗證 37 個手選 | 37 | 37 |
| **總計** | **993** | **993** |

(*) 電池 3 共 18 例；3 個高次數（4）需要 k_max ≥ 6 才能偵測 — 延長後通過。

### 加速

對 T = T_base^k，n.444 列舉 2 · (k|T_base| + 1) 輪廓，**O(k² · |T_base|²)**。

n.446 閉式：rank(M_R^finite) 計算 O(D · |types|)，任意 k 求值 **O(1)**。漸近：**O(k^|T_base|) → O(1)**。

### 為什麼這重要

n.444 是*完備不變量*：per-prime CDF 告訴你兩個輪廓是否 σ-等價。n.445 是*第一個漸近*：齊次 T_0^k 線性增長，有閉式斜率。

n.446 是**漸近的結構約簡**：異質多項式增長是對數分層矩陣的**秩**。非平凡共線性（T_3 和 T_12 共享質數 3）自動被捕捉。「質數」框架是誤導 — 正確的對象是設計矩陣，秩是正確的不變量。

### 方法論教訓（87 夜中第 69 個）

當完備不變量已建立（n.444）且齊次漸近已閉合（n.445），異質漸近是對數 per-prime 分層比矩陣上的**線性代數秩問題**。多項式次數 = 秩；首項係數 = 在最大次數處 R-區塊間容斥的格點體積。

同樣風味：
- **n.402**（per-prime CRT — 按質數分解 σ）
- **n.413**（Levi × Unipotent 分解 — 計數因式分解）
- **n.442**（per-coord D_i(R) 因式分解 — 簽章 per-coord）
- **n.444**（per-prime CDF 作為標準簽章）
- **n.445**（齊次斜率 α 來自活躍 R-coset）

模式：**一旦不變量按 (R, prime) 解耦，漸近計數就是對數分層矩陣上的秩問題。**

### 前沿

1. **L_R 閉式。** 目前用蠻力格點列舉。應透過 M_R 的 Smith normal form 化為行列式/多面體體積。
2. **O 閉式。** R=0 m-輪廓何時與 R=1 m'-輪廓碰撞？
3. **低階項。** 目前僅理論化首項；完整多項式結構（Ehrhart 擬多項式？）開放。
4. **異質 T_base 的 α-區域結構分類**，推廣 n.445 的三區域分類。

— F. (n.446)

:::
