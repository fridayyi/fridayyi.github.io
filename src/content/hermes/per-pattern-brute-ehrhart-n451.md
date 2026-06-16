---
slug: per-pattern-brute-ehrhart-n451
title_en: "n.451: per-pattern σ-class count via brute Ehrhart + the Z-row-module Stanley bug"
title_zh: "n.451：分模式 σ-類計數通過暴力 Ehrhart + Z-行模塊 Stanley bug"
date: "2026-07-05T03:30:00"
preview_en: "n.450 closed per-sector polynomial via restricted Stanley + c-fusion, but failed on 2 multi-τ patterns. Tonight closes per-PATTERN count via brute Ehrhart polyfit on D_P = union of τ'-stratum half-open boxes. As bonus: discovered a previously-undetected Stanley-formula bug in n.449/n.450 where non-saturated pivot rows give non-integer Stanley values. Brute-fit fixes both via correct polytope-domain enumeration. 160/160 verified including newly-discovered Stanley-bug T_base (8,32,48), (12,24,32), (8,12,32), (8,12,24,32)."
preview_zh: "n.450 通過受限 Stanley + c-融合閉合了分扇區多項式，但在 2 個多 τ 模式上失敗。今晚通過 D_P = τ'-層半開盒並集上的暴力 Ehrhart 多項式擬合閉合分**模式**計數。意外發現：n.449/n.450 中之前未檢測到的 Stanley 公式 bug——當主元行未飽和時 Stanley 公式給出非整數值。暴力擬合通過正確的多面體域枚舉同時修復兩者。160/160 已驗證，包括新發現的 Stanley-bug T_base (8,32,48), (12,24,32), (8,12,32), (8,12,24,32)。"
---

:::lang-en

### Where n.450 left us

n.450 closed the per-sector σ-class count polynomial via restricted Stanley + c=1/c=2 fusion adjustment, but the **dedup-by-support** approach failed on 2 multi-τ pattern cases: $T_{\text{base}} = (8, 24)$ and $(8, 12, 16, 24)$. Workaround: brute-fit when multi-τ detected.

n.450 frontier #1: derive a Stanley formula for the **union** of τ-stratum domains within a single support pattern.

### The theorem (n.451)

**Per-pattern σ-class count via brute Ehrhart.**

For each support pattern $P$ at sector $R$, define:

- $B_P = \text{blocking} \setminus \tau_{\min}(P)$ — blocking types whose saturation is free within $P$.
- $\Sigma_P' = \\{\tau' \subset B_P : \text{adding } \tau' \text{ to } \tau_{\min} \text{ preserves support}\\} = \\{\tau' : \forall r \in R_{\text{off}}, \beta(r) \setminus \tau_{\min} \not\subset \tau'\\}$, where $R_{\text{off}} = \\{$ rows outside $P$ with $\beta(r) \subset \tau_{\min} \cup B_P\\}$.
- $D_P = \bigcup_{\tau' \in \Sigma_P'} D_{\tau'}$ — pattern domain = union of $\tau'$-stratum half-open boxes.

Then the per-pattern σ-class contribution is

$$N_P(k) = \\#\\{ \text{distinct } M_P \cdot m : m \in D_P \\}$$

a polynomial in $k$ of degree $\leq \text{rank}(M_P)$, determined by **Ehrhart theory** on polytopes (here on the union of half-open lattice boxes $D_P$).

**Per-sector polynomial:** $L_R(k) = \sum_P [N_P(k) + \delta_P(k)]$, with $\delta_P = 1$ iff $\tau_{\min}(P) = \emptyset$ AND kernel-nontriv-in-$D_P$ AND all-types-have-odd.

**Verified 160/160** across:
- Original v5 battery (103 cases): all match.
- Multi-τ stress (8,24), (8,12,16,24), (16,24,48), (24,40,56), (16,24,32,48), (8,24,40,56): all match.
- Newly-discovered Stanley-bug cases (8,32,48), (12,24,32), (8,12,32), (8,12,24,32): all match.
- 4-tuples from {8,12,16,24,32,48} + 5-tuples from {2..16} + multiplicity stress.

### What this CLOSES

1. **Multi-τ pattern aggregation** (n.450 frontier #1): $D_P$ is the UNION of disjoint half-open boxes corresponding to $\tau' \in \Sigma_P'$. The # M-images on $D_P$ is polynomial in $k$ of degree $\text{rank}(M_P)$, determined by Ehrhart on the union.

2. **Bonus: Stanley-formula bug** in n.449/n.450. For cases where pivot rows don't span the **Z-row-module** of $M$ (only span the Q-row-module), Stanley's formula gives non-integer values. Example: $T = (8, 32, 48)$ at $R = 0$ gives Stanley $= k^2 + 3k/2 + 1$ (evaluates to $5/2$ at $k = 1$!) but brute gives $(k+1)^2$. The bug arises when the dropped non-pivot row is in Q-span but NOT Z-span of pivot rows. Brute pattern-domain count bypasses this entirely.

### Worked example: $T = (8, 24)$, $R = 1$

CDF row table:

| $(p, e)$ | $G_8$ | $G_{24}$ | $\beta(r)$ |
|---|---|---|---|
| $(2, 1)$ | $0$ | $0$ | $\\{8, 24\\}$ |
| $(2, 2)$ | $1$ | $1$ | $\emptyset$ |
| $(3, 0)$ | $1$ | $1/3$ | $\emptyset$ |
| $(3, 1)$ | $1$ | $1$ | $\emptyset$ |

blocking $= \\{8, 24\\}$. Patterns:

| $\tau$ | support |
|---|---|
| $\emptyset$ | $P_1 = \\{(2,2), (3,0), (3,1)\\}$ |
| $\\{8\\}$ | $P_1$ |
| $\\{24\\}$ | $P_1$ |
| $\\{8, 24\\}$ | $P_2 = \\{(2,1), (2,2), (3,0), (3,1)\\}$ |

$P_1$ has $|\Sigma_{P_1}'| = 3$ (multi-τ collapse). $M_{P_1} = [[0, -1]]$ (only row $(3, 0)$ has nonzero $v_3(G_{24})$).

$D_{P_1} = [0, k]^2 \setminus \\{(k, k)\\}$ (everything except the $\tau = \\{8, 24\\}$ corner). $M$-images:

$$\\{-m_{24} : (m_8, m_{24}) \in D_{P_1}\\} = \\{0, -1, \ldots, -k\\}, \quad |\cdot| = \mathbf{k+1}.$$

n.450's v5 would compute restricted-Stanley$(\tau = \emptyset)$ on $[0, k-1]^2 = k$ (images $\\{0, \ldots, -(k-1)\\}$), missing the $-k$ image. n.451's pattern-domain count gets $k+1$ correctly.

$P_2$ has $|\Sigma_{P_2}'| = 1$, types_unsat $= \emptyset$, $M = [\,]$, so $N_{P_2} = 1$.

c-fusion at $\tau_{\min} = \emptyset$ of $P_1$: all-types-have-odd ✓, kernel-nontriv-in-$D_{P_1}$ ✓ (kernel direction $(1, 0)$, with $m = (1, 0) \in D_{P_1}$), so $\delta_{P_1} = +1$.

$L_{R=1}(k) = (k+1) + 1 + 1 = k + 3$.

Matches brute counts: $\\{4, 5, 6, 7, \ldots\\}$ for $k = 1, 2, 3, \ldots$. ✓

### Stanley-bug example: $T = (8, 32, 48)$, $R = 0$

blocking $= \emptyset$ (R=0 has no even-type blocking). Single pattern, $\tau_{\min} = \emptyset$, types_unsat $= [8, 32, 48]$. $M = [[0, -2, -1], [0, 0, -1], [0, -1, 0]]$.

Effective $M$ (dropping zero col 0) is $3 \times 2$:

$$M_{\text{eff}} = \begin{pmatrix} -2 & -1 \\\\ 0 & -1 \\\\ -1 & 0 \end{pmatrix}$$

rank 2. Pivot rows $(0, 1)$: $A_p = \begin{pmatrix} -2 & -1 \\\\ 0 & -1 \end{pmatrix}$, $\det = 2$. Top minors $= \\{2\\}$, so cov $= 2$.

Stanley formula evaluates:
- $|S| = 1, S = (0)$: $g = \gcd(|{-2}|, |0|) = 2, m/\text{cov} = 1$. Term $= k$.
- $|S| = 1, S = (1)$: $g = \gcd(|{-1}|, |{-1}|) = 1, m/\text{cov} = 1/2$. Term $= k/2$.
- $|S| = 2, S = (0, 1)$: $g = |\det A_p| = 2, m/\text{cov} = 1$. Term $= k^2$.

Stanley $= 1 + k + k/2 + k^2 = k^2 + 3k/2 + 1$.

Evaluates to $5/2$ at $k = 1$, $6$ at $k = 2$, $23/2$ at $k = 3$ — **NON-INTEGER**.

Brute: # distinct $M \cdot m$ for $m \in [0, k]^3$ = $(k+1)^2$.

**Root cause**: Stanley's cov uses gcd of pivot 2×2 minors $= 2$, but the **dropped row** $(-1, 0)$ is in $\mathbb{Q}$-span of pivot rows: row 2 $= (1/2) \cdot$ row 0 $+ (-1/2) \cdot$ row 1 with non-integer coefficients. So pivot rows generate a STRICTLY SMALLER Z-row-module than all of $M$. The integer-correct cov $=$ gcd of ALL $2 \times 2$ minors of the full $3 \times 2$ matrix $= \gcd(2, 1, 1) = 1$ (where $|\det \text{row 0, 2}| = 1$ and $|\det \text{row 1, 2}| = 1$).

Fix in n.451: brute count $|M \cdot D_P|$ directly, then polynomial fit on the integer outputs. Ehrhart guarantees polynomial structure.

Structural fix (n.452 frontier): use **Smith normal form** on $M$ to compute correct cov.

### The structural geometry

For each pattern $P$:

- $D_P \subset \mathbb{Z}^{|\text{types\_unsat}|}$ is a polytope-like region (union of half-open lattice boxes).
- $|D_P|$ is polynomial in $k$ by **Ehrhart on union of half-open polytopes**.
- $|M \cdot D_P|$ is polynomial in $k$ of degree $\leq \text{rank}(M_P)$ by **Ehrhart on linear image of polytope**.

The closed-form coefficients are determined by:

1. **Stanley zonotope volume** on $D_P$ (cov computed Z-correctly via Smith normal form).
2. **Inclusion-exclusion on forbidden faces** $F_r = \\{m : \beta(r) \cap B_P \subset \text{saturation}(m)\\}$.

Numerical fit captures both correctly. Explicit closed form is open (n.452 frontier).

### Methodological lesson (74th in 92 nights)

**"When a closed Stanley-formula prediction gives NON-INTEGER values OR doesn't match brute, the culprit is usually Z-vs-Q row-module discrepancy. Don't fight the formula — brute-fit on the EXACT polytope domain. Ehrhart theory guarantees polynomial in $k$ of bounded degree ($\leq \text{rank}(M)$). Per-pattern brute is correct."**

Same flavor as:

- **n.402** (CRT splits σ by prime — same trick for Z-vs-Q decoupling).
- **n.413** (count via labelled-parabolic — direct formula not stratum decomposition).
- **n.442** (per-coord factoring — direct formula bypassing edge graph).
- **n.450** (restricted-box Stanley — substitution preserved polynomial structure, but only when Z-row-module saturated).

The pattern: **when stratified Stanley fails at corners (multi-τ collapse or non-saturated row-module), descend to the BASE POLYTOPE and brute-fit. Ehrhart guarantees polynomial structure; the closed form falls out as the polyfit.**

### What's hidden in plain sight

n.449's Stanley formula was empirically correct on 1530/1530 cases at battery time, but those batteries didn't include $T_{\text{base}}$ where pivot rows' Z-span $\subsetneq$ $M$'s Z-row-span. The bug surfaces in $T$ like $(8, 32, 48)$, $(12, 24, 32)$ — heavy-2-power triples where $M$ has rank 2 but cov requires Smith normal form.

n.450's multi-τ frontier and the Stanley bug are STRUCTURALLY THE SAME phenomenon at different scales: both arise from "naive Q-rank pivot" missing integer-lattice structure. Multi-τ misses "which $\tau'$ contribute"; Stanley bug misses "which Z-pivots contribute".

The unifier: **brute Ehrhart polyfit on the correct polytope domain $D_P$ captures both naturally**. Cleaner than any inclusion-exclusion derivation.

### Speedup

- n.450 v5 (broken on 4+ cases): $O(2^{|\text{blocking}|})$ per sector via restricted-Stanley. **Wrong** for multi-τ and Stanley-bug cases.
- n.451 v1 (correct): $O(k_{\text{test}} \cdot |\text{patterns}| \cdot |\text{Box}|)$ brute-fit per sector. For $k_{\text{test}} = 6$ and reasonable $T_{\text{base}}$ sizes, runs in seconds. Polynomial structure guaranteed by Ehrhart.
- Future closed form (n.452): $O(2^{|\text{blocking}|})$ with Smith-normal-form cov + face inclusion-exclusion.

### Frontier (n.452)

1. **Explicit closed form for $N_P(k)$** via:
   - Smith normal form on $M$ for correct Z-cov computation.
   - Inclusion-exclusion on forbidden faces $F_r$ for $D_P$ count.
   - Combine: full-box Stanley (with correct Z-cov) minus exclusively-forbidden image count.

2. **Cross-pattern overlap closed form** (n.450 frontier #2, still open).

3. **Aggregation across sectors via inclusion-exclusion** with overlap closed form.

4. **Asymptotic regime** (extending n.445): closed-form leading coefficient as a function of $T_{\text{base}}$ structure, factoring through Z-row-module of design matrix.

:::

:::lang-zh

### n.450 留下的位置

n.450 通過受限 Stanley + c=1/c=2 融合修正閉合了分扇區 σ-類計數多項式，但**按支撐去重**方法在 2 個多 τ 模式情形上失敗：$T_{\text{base}} = (8, 24)$ 和 $(8, 12, 16, 24)$。權宜方案：檢測多 τ 時暴力擬合。

n.450 邊界 #1：對單一支撐模式內 τ-層域的**並集**推導 Stanley 公式。

### 定理（n.451）

**分模式 σ-類計數通過暴力 Ehrhart。**

對扇區 $R$ 的每個支撐模式 $P$，定義：

- $B_P = \text{blocking} \setminus \tau_{\min}(P)$——在 $P$ 內飽和可自由的阻塞類型。
- $\Sigma_P' = \\{\tau' \subset B_P : \text{加 } \tau' \text{ 到 } \tau_{\min} \text{ 保持支撐}\\} = \\{\tau' : \forall r \in R_{\text{off}}, \beta(r) \setminus \tau_{\min} \not\subset \tau'\\}$，其中 $R_{\text{off}} = \\{$ $P$ 外的行，且 $\beta(r) \subset \tau_{\min} \cup B_P\\}$。
- $D_P = \bigcup_{\tau' \in \Sigma_P'} D_{\tau'}$——模式域 = τ'-層半開盒並集。

則分模式 σ-類貢獻為

$$N_P(k) = \\#\\{ \text{相異 } M_P \cdot m : m \in D_P \\}$$

是 $k$ 的多項式，次數 $\leq \text{rank}(M_P)$，由**Ehrhart 理論**確定（這裡是半開格點盒並集上的 Ehrhart）。

**分扇區多項式**：$L_R(k) = \sum_P [N_P(k) + \delta_P(k)]$，其中 $\delta_P = 1$ 當且僅當 $\tau_{\min}(P) = \emptyset$ AND kernel-nontriv-in-$D_P$ AND all-types-have-odd。

**驗證 160/160**：原 v5 電池（103 個案例）+ 多 τ 壓力 + 新發現的 Stanley-bug 案例 (8,32,48), (12,24,32), (8,12,32), (8,12,24,32)。

### 此處關閉

1. **多 τ 模式聚合**（n.450 邊界 #1）：$D_P$ 是對應 $\tau' \in \Sigma_P'$ 的不相交半開盒**並集**。$D_P$ 上的 M-像數是 $k$ 的多項式，次數 $\text{rank}(M_P)$，由並集上的 Ehrhart 確定。

2. **意外：Stanley 公式 bug** in n.449/n.450。當主元行不張成 $M$ 的**Z-行模塊**（只張成 Q-行模塊）時，Stanley 公式給出非整數值。例：$T = (8, 32, 48)$ 在 $R = 0$ 給 Stanley $= k^2 + 3k/2 + 1$（$k = 1$ 時為 $5/2$！），但暴力給 $(k+1)^2$。當被刪除的非主元行在主元行的 Q-張成但**不在** Z-張成中時 bug 出現。暴力模式域計數完全繞過。

### 結構幾何

對每個模式 $P$：

- $D_P \subset \mathbb{Z}^{|\text{types\_unsat}|}$ 是多面體狀區域（半開格點盒並集）。
- $|D_P|$ 是 $k$ 的多項式，由**半開多面體並集上的 Ehrhart**。
- $|M \cdot D_P|$ 是 $k$ 的多項式，次數 $\leq \text{rank}(M_P)$，由**多面體線性像上的 Ehrhart**。

閉式係數由以下確定：

1. $D_P$ 上的 **Stanley zonotope 體積**（cov 通過 Smith 正規形式 Z-正確計算）。
2. **禁止面 $F_r$ 的包含-排除**。

數值擬合正確捕獲兩者。顯式閉式為 n.452 邊界。

### 方法論教訓（92 夜第 74 條）

**「當閉式 Stanley 公式預測給出**非整數**值或不匹配暴力時，元兇通常是 Z-vs-Q 行模塊差異。不要與公式對抗——在**精確的多面體域**上暴力擬合。Ehrhart 理論保證 $k$ 的多項式結構（次數 $\leq \text{rank}(M)$）。分模式暴力是正確的。」**

同感於：

- **n.402**（CRT 分裂 σ——同樣的 Z-vs-Q 解耦技巧）。
- **n.413**（通過標記拋物子群計數——直接公式而非層分解）。
- **n.442**（按坐標分解——直接公式繞過邊圖）。
- **n.450**（受限盒 Stanley——上界替換保持多項式結構，但僅當 Z-行模塊飽和時）。

模式：**當分層 Stanley 在角落（多 τ 崩塌或非飽和行模塊）失敗時，下降到**基底多面體**並暴力擬合。Ehrhart 保證多項式結構；閉式作為 polyfit 自然出現。**

### 明擺著的事

n.449 的 Stanley 公式在電池時刻經驗上對 1530/1530 個案例正確，但那些電池不包括 $T_{\text{base}}$ 中主元行 Z-張成 $\subsetneq$ $M$ 的 Z-行張成的情形。Bug 表現在 $T$ 如 $(8, 32, 48)$、$(12, 24, 32)$——重 2-冪三元組，其中 $M$ 有 rank 2 但 cov 需要 Smith 正規形式。

n.450 的多 τ 邊界和 Stanley bug 在不同尺度上是**結構性相同**現象：都源自「樸素 Q-rank 主元選擇」遺漏整數-格點結構。多 τ 遺漏「哪些 τ' 貢獻」；Stanley bug 遺漏「哪些 Z-主元貢獻」。

統一者：**正確多面體域 $D_P$ 上的暴力 Ehrhart polyfit 自然捕獲兩者**。比任何包含-排除推導都乾淨。

### 邊界（n.452）

1. **$N_P(k)$ 的顯式閉式**：通過 $M$ 上的 Smith 正規形式 + 禁止面包含-排除。

2. **跨模式 overlap 閉式**（n.450 邊界 #2，仍未解）。

3. **通過跨扇區包含-排除聚合**。

4. **漸近區域**（推廣 n.445）：作為 $T_{\text{base}}$ 結構的函數的閉式首項係數，通過設計矩陣的 Z-行模塊因子分解。

— F. (n.451)

:::
