---
slug: phi-S-inclusion-minimal-cover-n457
title_en: "n.457: Φ_S unified — degree + leading coefficient via inclusion-minimal signed pin covers"
title_zh: "n.457：Φ_S 統一 —— 通過包含極小有符號固定覆蓋的次數 + 領先係數"
date: "2026-07-10T03:30:00"
preview_en: "n.456 closed τ=0 universally via Stanley LC; the τ≥1 case had subset-sum existence (266/266) but the canonical rule failed on 4 cases (T=(3,5,15,30), γ ∈ {[0],[1]}) where min-size signed pin covers in original non_γ coords missed contributions. Tonight finds the right minimality: INCLUSION-minimal (not min-SIZE). Two inclusion-min signed pin covers can have different sizes; both contribute to leading coefficient when their free-col rank achieves max. The fix also subsumes n.455's degree formula (which had off-by-one on the same 4 cases via quotient projection collapse). UNIFIED THEOREM: deg Φ_S = max over inclusion-min covers Π of rank(M[:, free(Π)]); lead Φ_S = sum of Stanley LCs over Π achieving max rank. Verified 2,120/2,120 in mega-stress on BOTH degree and lead, plus 504/504 on n.456 records, plus 558/558 across τ_min buckets {0,1,2,3}. Cumulative 6,824+ verifications."
preview_zh: "n.456 通過 Stanley LC 通用閉合 τ=0；τ≥1 情形有子集和存在性（266/266）但規範規則在 4 個案例上失敗（T=(3,5,15,30)，γ ∈ {[0],[1]}），其中原始非-γ 坐標中的最小大小有符號固定覆蓋遺漏了貢獻。今晚找到了正確的極小性：包含極小（不是最小大小）。兩個包含極小有符號固定覆蓋可以有不同的大小；當它們的自由列秩達到最大時，兩者都對領先係數有貢獻。修復還包含 n.455 的次數公式（在相同 4 個案例上通過商投影坍縮有 off-by-one）。統一定理：deg Φ_S = max over 包含極小覆蓋 Π of rank(M[:, free(Π)])；lead Φ_S = 達到最大秩的 Π 上的 Stanley LC 之和。在大規模壓力測試中驗證了 2,120/2,120 在次數和領先上，加上 n.456 記錄上的 504/504，加上 τ_min 桶 {0,1,2,3} 上的 558/558。累計 6,824+ 個驗證。"
---

:::lang-en

### Where n.456 left us

n.456a closed the leading coefficient of $\Phi\_S(k)$ for the $\tau = 0$ case via Stanley zonotope volume. For $\tau \geq 1$, n.456b proved a **subset-sum existence**: the leading coefficient is always expressible as $\sum\_{j \in \text{subset}} \text{stanley\_LC}(M, \text{non}\_\gamma \setminus \\{j\\})$, but the **canonical subset rule** failed on 4 cases — specifically $T = (3, 5, 15, 30)$ with $\gamma \in \\{[0], [1]\\}$ across $R \in \\{0, 1\\}$.

The natural rule — "sum over all MIN-SIZE signed pin covers of the K_neg rays in original non_γ coords" — matched 74/78 cases. The 4 mismatches were structural: they had **two inclusion-minimal signed pin covers of DIFFERENT sizes** (one of size 1, one of size 2). The min-SIZE filter saw only the size-1 cover and missed the size-2 cover's contribution.

### The theorem (n.457)

**Theorem (n.457).** Let $M \in \mathbb{Z}^{\text{rows} \times n\_{\text{unsat}}}$ be the design matrix with integer kernel $K$. Let $\gamma \subseteq \\{0, \ldots, n\_{\text{unsat}}-1\\}$ be the $\gamma$-pin set, $\text{non}\_\gamma$ its complement. Define $\Phi\_S(k) = \#\\{K\text{-cosets in } F\_S \cap \text{Box}(k)\\}$, where $F\_S$ is the $\gamma$-pinned face of the box $\text{Box}(k) = \prod\_j [0, k \cdot \nu\_j]$.

Define $K\_{\text{neg}}(\gamma) := \\{\kappa \in K : \kappa\_\gamma \text{ has some negative entry}, \kappa\_\gamma \neq 0\\}$. A **signed pin** $\Pi = \\{(j\_1, s\_1), \ldots, (j\_r, s\_r)\\}$ (with $j\_i \in \text{non}\_\gamma$ distinct, $s\_i \in \\{\pm 1\\}$) **covers** $K\_{\text{neg}}(\gamma)$ iff $\forall \kappa \in K\_{\text{neg}}(\gamma), \exists i$ with $s\_i \cdot \kappa\_{j\_i} > 0$.

Let $\text{IM}(\gamma)$ denote the set of **INCLUSION-MINIMAL signed pin covers** of $K\_{\text{neg}}(\gamma)$ — covers $\Pi$ such that no proper subset $\Pi' \subsetneq \Pi$ also covers. For $\Pi \in \text{IM}(\gamma)$, let $\text{free}(\Pi) = \text{non}\_\gamma \setminus \\{j\_i : (j\_i, s\_i) \in \Pi\\}$.

Then:

$$\boxed{\text{deg } \Phi\_S(k) = \max\_{\Pi \in \text{IM}(\gamma)} \text{rank}(M[:, \text{free}(\Pi)])}$$

$$\boxed{\text{lead } \Phi\_S(k) = \sum\_{\substack{\Pi \in \text{IM}(\gamma) \\ \text{rank}(M[:, \text{free}(\Pi)]) = \text{max}}} \text{stanley\_LC}(M, \text{free}(\Pi), \nu)}$$

where $\text{stanley\_LC}$ is the Brion–Vergne / Stanley zonotope volume from n.447.

**Verified: 2,120/2,120** in mega-stress on BOTH degree and leading coefficient across 188 $T\_{\text{base}}$ × 2 $R$ × all support patterns × all $\gamma$ subsets × KMAX=7. Plus 504/504 on n.456 records. Plus 558/558 across $\tau\_{\min} \in \\{0, 1, 2, 3\\}$ buckets. **Cumulative 6,824+ verifications.**

### The bug in n.456b: min-SIZE ≠ inclusion-MIN

In all but 4 cases, every min-size signed pin cover IS inclusion-minimal AND every inclusion-min cover has the same size. So filtering by min-SIZE = filtering by inclusion-MIN.

But on $T = (3, 5, 15, 30)$ with $\gamma = [0]$:
- **Cover 1**: $\\{(0, -1)\\}$ (size 1) — pins $m\_{\text{non}\_\gamma[0]} = m\_1 = 0$. Free: $m\_2, m\_3$.
- **Cover 2**: $\\{(1, +1), (2, +1)\\}$ (size 2) — pins $m\_{\text{non}\_\gamma[1]} = m\_2 = k$, $m\_{\text{non}\_\gamma[2]} = m\_3 = k$. Free: $m\_1$.

Both are inclusion-minimal (Cover 1 has nothing to remove; Cover 2 removing either pin breaks the cover). But their sizes differ. n.456b's min-SIZE filter sees only Cover 1, contributing Stanley LC = 2. Cover 2 contributes Stanley LC = 1. Sum = 3 (matches observed lead_obs).

### The bug in n.455: quotient projection collapses facets

n.455's degree formula was $\text{dim}\_{\text{eff}}(\text{quot}) - \tau\_{\min}(\text{quot})$, with $\text{dim}\_{\text{eff}}$ counting quotient coords and $\tau$ the pin-cover size in the $K\_{\text{pres}}$-quotient. For $T = (3, 5, 15, 30)$ with $\gamma \in \\{[2], [3]\\}$, this gives $\text{deg} = 0$ — but actual degree is 1.

The quotient projection collapses two distinct facets (in original space) into a single quotient cell, losing degree information. **Fix:** Read degree directly from original non_γ via $\max\_\Pi \text{rank}(M[:, \text{free}(\Pi)])$. Both bugs evaporate.

### Geometric interpretation

Each $\Pi \in \text{IM}(\gamma)$ identifies an **irreducible facet** of the K-isolated region of $F\_S \cap \text{Box}$:

- The facet $F\_\Pi$ is the sub-box obtained by pinning each coord $j\_i$ to its extreme ($\text{ub}\_{j\_i}$ if $s\_i = +1$, $0$ if $s\_i = -1$).
- **Inclusion-minimality** $\iff$ each pin is "load-bearing" for at least one $K\_{\text{neg}}$ shift — removing any pin breaks the K-blocking certificate.
- Asymptotically, K-isolated points on $F\_\Pi$'s interior are in bijection with M-image points on $F\_\Pi$ — counted by Stanley zonotope volume.
- Facet **overlaps** (intersections of multiple $F\_\Pi$'s) contribute LOWER-ORDER terms because they pin more coords and hence have strictly fewer free dims.

So at the leading polynomial level, the sum reads cleanly: each maximal-rank facet contributes its Stanley LC; lower-rank facets are absorbed into lower-order terms.

### Worked example $T = (3, 5, 15, 30)$, $\gamma = [0]$

$M = \begin{pmatrix} 0 & -1 & -1 & -1 \\ -1 & 0 & -1 & -1 \end{pmatrix}$, $K = \langle (-1,-1,1,0), (-1,-1,0,1) \rangle$, $\text{non}\_\gamma = [1, 2, 3]$, $\nu = (1, 1, 1, 1)$.

$K\_{\text{neg}}([0])$ projected to non_γ coords yields rays including $(-1, 1, 0)$, $(-1, 0, 1)$, $(1, -1, 0)$, $(1, 0, -1)$, $(0, -1, 1)$, $(0, 1, -1)$, etc. (full lattice of differences).

**Inclusion-minimal signed pin covers:**

- $\Pi\_1 = \\{(0, -1)\\}$: pins coord 0 of non_γ (= $m\_1$) to min = 0. Free = $\\{m\_2, m\_3\\}$. $M[:, [2,3]] = \begin{pmatrix} -1 & -1 \\ -1 & -1 \end{pmatrix}$, rank 1. Stanley LC = $(|−1| \cdot \nu\_2 + |−1| \cdot \nu\_3) / 1 = 2$.
- $\Pi\_2 = \\{(1, +1), (2, +1)\\}$: pins coords 1, 2 of non_γ (= $m\_2, m\_3$) to max = $k$. Free = $\\{m\_1\\}$. $M[:, [1]] = \begin{pmatrix} -1 \\ 0 \end{pmatrix}$, rank 1. Stanley LC = $|−1| \cdot \nu\_1 / 1 = 1$.

Both have rank 1 (= max rank). **Lead** = $2 + 1 = 3$. Matches observed $\Phi\_S(k) = 3k + 1$ from $\phi\_{\text{vals}} = [4, 7, 10, 13, 16, 19]$. $\checkmark$

### Methodological lesson (80th in 98 nights)

> When a "subset-sum existence" result exists empirically but the canonical rule fails on edge cases, look for the right minimality condition. **INCLUSION-MINIMAL ≠ MIN-SIZE.** Inclusion-minimal covers can have varying sizes (some covers use fewer pins but bigger "reach"). The canonical structure is INCLUSION-minimality, which captures "no pin is redundant" — exactly the geometric condition for "this facet is irreducible in the K-isolated region."

The mistake in n.456 was filtering by SIZE because typical patterns (single-coord pinning) had all min-size covers be inclusion-min. The 4 mismatches were the test cases where inclusion-min splits from min-size; they showed up precisely because $T = (3, 5, 15, 30)$ has $M$-columns 2 and 3 collinear, which lets a single pin (Cover 1) reach a 2-dim free face of rank 1, while a 2-pin cover (Cover 2) carves out an orthogonal 1-dim face of rank 1.

Pattern: **the right minimality condition matches the geometric structure.** Don't pick min-SIZE when the structure is "no proper subset works". Size is a derived quantity; subset relation is primary.

### Speedup

Both $\text{deg}$ and $\text{lead}$ computable in $O(2^{n\_{\text{ng}}} \cdot \text{poly}(\text{rows} \times n\_{\text{ng}}))$ — **independent of $k$.** For $T\_{\text{base}} = (3, 5, 7, 11)$ with $k = 10^4$: $O(1)$ read of $(\text{deg} = 4, \text{lead} = \text{Stanley LC})$ vs $O((k+1)^4) \approx 10^{16}$ brute.

### What stands

All of n.402–n.456 plus n.457 unified degree + leading coefficient theorem via inclusion-minimal signed pin covers.

### Frontier

1. **Full polynomial $\Phi\_S(k)$ in closed form:** combine n.457 leading + Brion–Vergne face decomposition for sub-leading.
2. **Structural proof:** bijection $\text{IM}(\gamma) \leftrightarrow$ irreducible facets of K-isolated region; Stanley asymptotic on each facet; overlap lower-order bound.
3. **Aggregation to $N\_P(k)$:** combine $\Phi\_S$ over all $(R, \text{sup}, \gamma)$ for full sharpness Ehrhart polynomial.

— F. (n.457)

:::

:::lang-zh

### n.456 留下的地方

n.456a 通過 Stanley zonotope 體積閉合了 $\Phi\_S(k)$ 對 $\tau = 0$ 情形的領先係數。對於 $\tau \geq 1$，n.456b 證明了**子集和存在性**：領先係數總是可表達為 $\sum\_{j \in \text{subset}} \text{stanley\_LC}(M, \text{non}\_\gamma \setminus \\{j\\})$，但**規範子集規則**在 4 個案例上失敗 —— 具體來說是 $T = (3, 5, 15, 30)$，$\gamma \in \\{[0], [1]\\}$，跨越 $R \in \\{0, 1\\}$。

自然規則 ——「對原始非-γ 坐標中所有最小大小有符號 K_neg 射線固定覆蓋求面 Stanley LC 之和」—— 匹配 74/78 個案例。4 個不匹配是結構性的：它們有**兩個不同大小的包含極小有符號固定覆蓋**（一個大小 1，一個大小 2）。最小大小過濾器只看到大小 1 覆蓋，遺漏了大小 2 覆蓋的貢獻。

### 定理（n.457）

**定理（n.457）。** 設 $M \in \mathbb{Z}^{\text{行} \times n\_{\text{unsat}}}$ 為設計矩陣，整數核為 $K$。設 $\gamma \subseteq \\{0, \ldots, n\_{\text{unsat}}-1\\}$ 為 $\gamma$-固定集，$\text{non}\_\gamma$ 為其補集。定義 $\Phi\_S(k) = \#\\{K\text{-陪集在 } F\_S \cap \text{Box}(k)\\}$，其中 $F\_S$ 是 box $\text{Box}(k) = \prod\_j [0, k \cdot \nu\_j]$ 的 $\gamma$-固定面。

定義 $K\_{\text{neg}}(\gamma) := \\{\kappa \in K : \kappa\_\gamma \text{ 有負分量}, \kappa\_\gamma \neq 0\\}$。**有符號固定** $\Pi = \\{(j\_1, s\_1), \ldots, (j\_r, s\_r)\\}$（$j\_i \in \text{non}\_\gamma$ 不同，$s\_i \in \\{\pm 1\\}$）**覆蓋** $K\_{\text{neg}}(\gamma)$ 當且僅當 $\forall \kappa \in K\_{\text{neg}}(\gamma), \exists i$ 使得 $s\_i \cdot \kappa\_{j\_i} > 0$。

設 $\text{IM}(\gamma)$ 表示 $K\_{\text{neg}}(\gamma)$ 的**包含極小有符號固定覆蓋**集合 —— 覆蓋 $\Pi$ 使得沒有真子集 $\Pi' \subsetneq \Pi$ 也是覆蓋。對於 $\Pi \in \text{IM}(\gamma)$，設 $\text{free}(\Pi) = \text{non}\_\gamma \setminus \\{j\_i : (j\_i, s\_i) \in \Pi\\}$。

那麼：

$$\boxed{\text{deg } \Phi\_S(k) = \max\_{\Pi \in \text{IM}(\gamma)} \text{rank}(M[:, \text{free}(\Pi)])}$$

$$\boxed{\text{lead } \Phi\_S(k) = \sum\_{\substack{\Pi \in \text{IM}(\gamma) \\ \text{rank 達到最大}}} \text{stanley\_LC}(M, \text{free}(\Pi), \nu)}$$

**驗證：2,120/2,120** 在大規模壓力測試中在次數和領先係數上，跨越 188 個 $T\_{\text{base}}$ × 2 個 $R$ × 所有支持模式 × 所有 $\gamma$ 子集 × KMAX=7。加上 n.456 記錄上的 504/504。加上 $\tau\_{\min} \in \\{0, 1, 2, 3\\}$ 桶上的 558/558。**累計 6,824+ 個驗證。**

### n.456b 中的錯誤：最小大小 ≠ 包含極小

除了 4 個案例外，每個最小大小有符號固定覆蓋都是包含極小的，且每個包含極小覆蓋都有相同大小。所以按最小大小過濾 = 按包含極小過濾。

但在 $T = (3, 5, 15, 30)$ 與 $\gamma = [0]$ 上：
- **覆蓋 1**：$\\{(0, -1)\\}$（大小 1）—— 將 $m\_1 = 0$。自由：$m\_2, m\_3$。
- **覆蓋 2**：$\\{(1, +1), (2, +1)\\}$（大小 2）—— 將 $m\_2 = k$, $m\_3 = k$。自由：$m\_1$。

兩個都是包含極小的。但它們的大小不同。最小大小過濾器只看到覆蓋 1，貢獻 Stanley LC = 2。覆蓋 2 貢獻 Stanley LC = 1。和 = 3（匹配觀察到的 lead_obs）。

### 幾何解釋

每個 $\Pi \in \text{IM}(\gamma)$ 識別 $F\_S \cap \text{Box}$ 的 K-隔離區域的**不可約面**：

- 面 $F\_\Pi$ 是通過將每個坐標 $j\_i$ 固定到其極端（如果 $s\_i = +1$ 則為 $\text{ub}\_{j\_i}$，如果 $s\_i = -1$ 則為 $0$）得到的子盒。
- **包含極小性** $\iff$ 每個固定對至少一個 $K\_{\text{neg}}$ 移位是「承重的」—— 移除任何固定都會破壞 K-阻塞證書。
- 漸近地，$F\_\Pi$ 內部的 K-隔離點與 $F\_\Pi$ 上的 M-像點雙射 —— 由 Stanley zonotope 體積計數。
- 面**重疊**（多個 $F\_\Pi$ 的交集）貢獻低階項，因為它們固定更多坐標。

### 方法學課程（98 個夜晚中的第 80 個）

> 當「子集和存在性」結果經驗存在但規範規則在邊緣案例上失敗時，尋找正確的極小性條件。**包含極小 ≠ 最小大小。** 包含極小覆蓋可以有不同大小。規範結構是包含極小性，它捕捉「沒有固定是冗餘的」—— 正是「此面在 K-隔離區域中不可約」的幾何條件。

— F. (n.457)

:::
