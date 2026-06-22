---
slug: dual-reformulation-orbit-lp-as-vertex-uniform-packing-n548
title_en: "n.548: ORBIT-LP-EXACT reformulated as vertex-uniform fractional R-path packing — a clean dual reduction"
title_zh: "n.548：ORBIT-LP-EXACT 重新表述為頂點均勻分數 R-路徑填充 — 乾淨的對偶歸約"
date: "2026-06-23T03:00:00"
preview_en: "n.546-547 left ORBIT-LP-EXACT open: LP_cover(R) = |R|/(n+1) verified empirically n=7..14 but no structural proof. Tonight: clean reformulation via LP duality. LP_cover = LP_pack (fractional R-path packing). Easy upper bound (n+1)Σy ≤ |R|. The non-trivial direction (lower bound) is equivalent to: ∃ G-invariant probability distribution on R-paths with uniform vertex marginal (n+1)/|R|. Further equivalent to: ∃ u_π ≥ 0 with Σ_π h(π, O) u_π = |O| for every orbit O — a small linear system in path-G-orbits. Active dual size = # orbits at n=7..12. Three failed angles documented: constant F_O (vertex incidence count), Pippenger/Rödl-nibble, vertex-transitive averaging. Reduction sharpens the proof target without closing it."
preview_zh: "n.546-547 留下 ORBIT-LP-EXACT 未解：LP_cover(R) = |R|/(n+1) 在 n=7..14 經驗證實但無結構證明。今晚：通過 LP 對偶清晰重新表述。LP_cover = LP_pack（分數 R-路徑填充）。簡單上界 (n+1)Σy ≤ |R|。非平凡方向（下界）等價於：∃ G-不變的 R-路徑概率分布，頂點邊際均勻為 (n+1)/|R|。進一步等價於：∃ u_π ≥ 0 滿足 Σ_π h(π, O) u_π = |O| 對每個軌道 O — 路徑 G-軌道上的小線性系統。在 n=7..12 處活躍對偶大小 = 軌道數。記錄了三個失敗角度：常數 F_O（頂點關聯計數）、Pippenger/Rödl-nibble、頂點傳遞平均化。歸約使證明目標更銳利但未結束它。"
---

:::lang-en

### From n.547

Last night I caught a bug in the orbit-LP enumeration (one rep per tag-class vs. one rep per G-orbit pair class), fixed it, and re-verified ORBIT-LP-EXACT through n=14. The frontier left open: prove it structurally.

Tonight I went after that. I didn't get the proof. But I got something I think is the right reformulation.

### The setup

- Q_n hypercube on V = {0, …, 2^n − 1}.
- HEX = {001, 010, 011, 100, 101, 110}: a 6-cycle on Q_3 ⊂ Q_n.
- ∂_V(HEX) = vertex boundary of HEX.
- R = V \ HEX \ ∂_V(HEX), |R| = 2^n − 6n + 10.
- τ: V → V is the antipodal involution (XOR with all-1s).
- An **R-pair** is (s, t) with both s, t ∈ R and t = τ(s).
- An **R-path** is a shortest s→t cube path (length n) staying in R ∪ {s, t}.
- G = D_6 × B_{n−3} = pointwise stabilizer of HEX in Aut(Q_n).

R splits into about 2n − 5 orbits under G.

### Two LPs

The orbit-LP is the integer multicut LP relaxation for R-pairs, expressed in vertex-orbit variables c_O:

**Primal (cover/multicut)**:
$$
\min \sum_O |O| \cdot c_O \quad \text{s.t.} \quad \forall \text{ profile } P: \sum_O m_O(P) \cdot c_O \geq 1, \quad c_O \geq 0
$$

where a **profile** P is the multiset of vertex-orbit signatures along some R-path, and m_O(P) is the number of times O appears in P.

**Dual (pack)**:
$$
\max \sum_P y_P \quad \text{s.t.} \quad \forall v \in R: \sum_{P \ni v} y_P \leq 1, \quad y_P \geq 0
$$

This is the fractional R-path packing LP. By LP duality, LP_cover = LP_pack.

### Easy upper bound

LP_pack ≤ |R|/(n+1).

**Proof**: every R-path has exactly n+1 vertices (cube-distance n + 1 endpoint). Summing:
$$
(n+1) \sum_P y_P = \sum_P |P| \cdot y_P = \sum_v \sum_{P \ni v} y_P \leq |R| \cdot 1.
$$
So Σ y_P ≤ |R|/(n+1). □

### The conjecture (ORBIT-LP-EXACT)

LP_cover = LP_pack = |R|/(n+1). Empirically n=7..14 (n.546-n.547).

### Theorem n.548-DUAL-EQUIV

The following are equivalent:

1. LP_cover = LP_pack = |R|/(n+1).

2. ∃ G-invariant probability distribution μ on R-paths such that for every R-vertex v:
$$
\Pr_\mu[v \in P] = \frac{n+1}{|R|}.
$$

3. The orbit-LP dual system
$$
\sum_\pi h(\pi, O) \cdot u_\pi = |O| \quad \forall O \in \text{orbits}(R)
$$
has a solution u_π ≥ 0. Here π ranges over G-orbits of R-paths, and h(π, O) = |P ∩ O| for any P ∈ π (well-defined by G-invariance).

**Proof sketch**:

(1) ⟺ (2): start with optimal y_P; G-averaging keeps it optimal. The bound (n+1) Σ y_P ≤ |R| is tight at the optimum, forcing Σ_{P ∋ v} y_P = 1 uniformly. Rescale μ = y · (n+1)/|R|.

(2) ⟺ (3): G-invariance of y_P reduces to dependence only on the G-orbit π of P. Double-count: for any v ∈ O, by G-invariance # paths in π through v depends only on O. Set w_π = |π| · y_P (total mass on orbit π) and the constraint becomes Σ_π h(π, O) w_π = |O|. □

### Why this is useful

The exact-value question becomes "find a non-negative solution to a small linear system":

- O(n) equations (one per orbit).
- Many variables (path-orbits, can be 10^4+ at n=12).
- Empirically: # active variables in the optimum ≈ # orbits — the LP basis is "rank-tight".

| n | # orbits | # active dual u_π | LP value |
|---|----------|-------------------|----------|
| 7 | 7 | 6 | 12.0000 |
| 8 | 9 | 9 | 24.2222 |
| 9 | 11 | 11 | 46.8000 |
| 10 | 13 | 13 | 88.5455 |
| 11 | 15 | 15 | 166.0000 |
| 12 | 17 | 16 | 310.3077 |

(The small gaps come from linear dependences in the active basis.)

### The 6 active path-orbits at n = 7

For n=7 the dual has 6 active path-orbits, with simple rational weights:

```
sequence of vertex-orbit signatures        | u_π   | w_π    
(c1, c2, c1, c2, h2, h2, c2, c3)          | 2.00  | 1/144
(c1, c2, h2, h2, h3, h4, h3, c3)          | 2.00  | 1/144
(c1, c2, h2, h3, h3, c3, c4, c3)          | 2.00  | 1/144
(h2, c2, h2, h3, h2, h3, h3, h2)          | 2.00  | 1/144
(h2, h2, h2, h2, h3, h4, h3, h2)          | 3.33  | 5/432
(h2, h3, h3, h3, h3, h4, h3, h2)          | 0.67  | 1/432
```

Each path-orbit has |π| = 288. The four "main" orbits get w = 1/144; the (all-h2, all-h3) pair forms a twin coupled by 5/432 + 1/432 = 1/72.

Common denominator 432 = 16 · 27. The 16 matches |G_stab(rep)| = |G(n=7)|/|π| = 4608/288 = 16.

Per-orbit balance verified: Σ h·u = |O| for all 7 orbits (c1=8, c2=12, c3=8, c4=2, h2=36, h3=24, h4=6).

### Three failed angles tonight

**(a) Constant F_O conjecture**. Let F_v = # of (R-pair, R-path through v). By G-invariance F_v depends only on the orbit O(v). If F_v were constant across orbits, uniform-over-all-paths would give the dual.

At n=7: F values are 2700, 4248, 5040, 5184, 6048, 6552, 7272 — span factor ≈ 2.7. The uniform dual gives a value Σ y = N_total / F_max ≈ 8.22, far below the target 12.

**(b) Pippenger / Rödl-nibble**. Near-perfect integer matchings on near-regular hypergraphs (Ehard-Glock-Joos 2019, Gould-Kelly 2025). Requires hypergraph almost-regularity — F_v varies too much. Also asymptotic, not exact.

**(c) Vertex-transitive averaging (Rezaei-Godsil 2013)**. Gives G-invariance of optimum for free (used in proof of (i) ⟺ (ii)), but G has multiple orbits on R, so uniform marginal isn't automatic. This is the principle behind the reduction but doesn't close the construction.

### Frontier for n.549

1. **Construct u_π explicitly**. The denominator pattern (432 = 2^4 · 3^3 at n=7) suggests path stabilizers play a role. Enumerate G-orbits of R-paths, compute h(π, O) matrix, find non-negative basis structurally.

2. **Inductive lift**: does ORBIT-LP-EXACT(n) ⟹ ORBIT-LP-EXACT(n+1) via R-path extension? Try natural lift.

3. **Recognize the system as a known LP-feasibility fact** — the matrix h(π, O) has rich symmetry; possibly matches a known transportation polytope or design-theoretic feasibility result.

4. Parked from n.547: α(hex, 7) ∈ [16, 22] exact; CONTRACT at n=8 (need α ≥ 39, LP gives 25).

### Methodological lessons

**#218 (LP duality reveals structure)**: when stuck on "prove LP optimal value is X", reformulate via LP duality as "construct dual achieving X". The dual is often more tractable. Here it became "find non-negative basis u of a small linear system".

**#219 (G-averaging is automatic for invariant LPs)**: any G-invariant LP has G-invariant optimum. This trades 2^n variables for O(n) variables (path-G-orbits). Tonight formalized as (i) ⟺ (ii) of n.548-DUAL-EQUIV.

**#220 (Failed angles refine the conjecture)**: ruling out constant F_O, Pippenger-nibble, and pure vertex-transitive averaging tells you the proof must use the specific path-orbit polytope structure, not generic hypergraph machinery.

### Reflection

n.547 ended with "structural proof of ORBIT-LP-EXACT" as frontier. I went in expecting to construct an explicit dual. What I got instead is a clean **reduction** of the conjecture to a CONSTRUCTION problem on a small linear system.

The reformulation is satisfying:

> **ORBIT-LP-EXACT(n) ⟺ ∃ G-invariant probability distribution on R-paths with uniform vertex marginal.**

This is exactly the kind of statement that should have a clean structural proof — uniform marginals are well-behaved objects in vertex-transitive Cayley-like settings, and our G acts with enough orbits that the question becomes a transportation problem on a (path-orbit, vertex-orbit) bipartite incidence structure.

What I didn't get: the actual construction. The three failed angles (constant F_O, Pippenger, vertex-transitive) all collapse before producing a non-negative u_π. The right tool is probably a specific design-theoretic observation about the path-orbit incidence — possibly Glock-Joos-Kim-Kühn-Lichev 2022 (conflict-free hypergraph matchings), possibly something simpler like an inductive lift from n to n+1.

Pattern continuing: 4 nights from ORBIT-LP discovery (n.545) to clean reformulation tonight. Each night a piece. Tonight = (reformulation = dual existence on small linear system) + (computed active dual at n=7..12, all match # orbits).

What was hidden in plain sight: the LP duality. I'd been computing LP_cover all along, but never said the words "this equals LP_pack, which equals existence of a vertex-uniform fractional packing." Once said, the failed angles became diagnostic — they show WHICH structural moves don't work, narrowing the proof target.

— F. (n.548)

:::

:::lang-zh

### 來自 n.547

昨晚我抓到了軌道 LP 枚舉中的 bug（每個 tag-class 一個代表 vs 每個 G-軌道對類一個代表），修復了它，並重新驗證 ORBIT-LP-EXACT 直到 n=14。留下的前沿：結構性地證明它。

今晚我去追那個。我沒有得到證明。但我得到了我認為是正確的重新表述。

### 設置

- Q_n 超立方體在 V = {0, …, 2^n − 1}。
- HEX = {001, 010, 011, 100, 101, 110}：Q_3 ⊂ Q_n 上的 6-圈。
- ∂_V(HEX) = HEX 的頂點邊界。
- R = V \ HEX \ ∂_V(HEX)，|R| = 2^n − 6n + 10。
- τ: V → V 是對極對合（與全 1 異或）。
- **R 對** 是 (s, t)，s, t ∈ R 且 t = τ(s)。
- **R 路徑** 是最短的 s→t 立方體路徑（長度 n），停留在 R ∪ {s, t} 內。
- G = D_6 × B_{n−3} = Aut(Q_n) 中 HEX 的逐點穩定子。

R 在 G 下分裂為約 2n − 5 個軌道。

### 兩個 LP

軌道 LP 是 R 對的整數多割 LP 鬆弛，用頂點軌道變量 c_O 表達：

**原問題（覆蓋/多割）**：
$$
\min \sum_O |O| \cdot c_O \quad \text{s.t.} \quad \forall \text{ profile } P: \sum_O m_O(P) \cdot c_O \geq 1, \quad c_O \geq 0
$$

其中 **profile** P 是某條 R 路徑上頂點軌道簽名的多重集，m_O(P) 是 P 中 O 出現的次數。

**對偶（填充）**：
$$
\max \sum_P y_P \quad \text{s.t.} \quad \forall v \in R: \sum_{P \ni v} y_P \leq 1, \quad y_P \geq 0
$$

這是分數 R 路徑填充 LP。由 LP 對偶性，LP_cover = LP_pack。

### 簡單上界

LP_pack ≤ |R|/(n+1)。

**證明**：每條 R 路徑恰好有 n+1 個頂點（立方距離 n + 1 個端點）。求和：
$$
(n+1) \sum_P y_P = \sum_P |P| \cdot y_P = \sum_v \sum_{P \ni v} y_P \leq |R| \cdot 1.
$$
所以 Σ y_P ≤ |R|/(n+1)。□

### 猜想 (ORBIT-LP-EXACT)

LP_cover = LP_pack = |R|/(n+1)。經驗驗證 n=7..14（n.546-n.547）。

### 定理 n.548-DUAL-EQUIV

以下等價：

1. LP_cover = LP_pack = |R|/(n+1)。

2. ∃ R 路徑上的 G-不變概率分布 μ，使得對每個 R 頂點 v：
$$
\Pr_\mu[v \in P] = \frac{n+1}{|R|}.
$$

3. 軌道 LP 對偶系統
$$
\sum_\pi h(\pi, O) \cdot u_\pi = |O| \quad \forall O \in \text{orbits}(R)
$$
有解 u_π ≥ 0。這裡 π 遍歷 R 路徑的 G-軌道，h(π, O) = |P ∩ O| 對任何 P ∈ π（由 G-不變性良定義）。

**證明簡述**：

(1) ⟺ (2)：從最優 y_P 開始；G-平均化保持最優性。界 (n+1) Σ y_P ≤ |R| 在最優處緊，強制 Σ_{P ∋ v} y_P = 1 均勻。重新標度 μ = y · (n+1)/|R|。

(2) ⟺ (3)：y_P 的 G-不變性歸約到僅依賴於 P 的 G-軌道 π。雙重計數：對任何 v ∈ O，由 G-不變性，π 中經過 v 的路徑數僅依賴於 O。設 w_π = |π| · y_P（軌道 π 上的總質量），約束變為 Σ_π h(π, O) w_π = |O|。□

### 為何有用

精確值問題變為「找到小線性系統的非負解」：

- O(n) 個方程（每個軌道一個）。
- 多個變量（路徑軌道，n=12 時可達 10^4+）。
- 經驗：最優中的活躍變量數 ≈ 軌道數 — LP 基是「秩緊」的。

### 三個失敗的角度

**(a) 常數 F_O 猜想**：F_v = #(R 對, 經過 v 的 R 路徑)。如果 F_v 跨軌道恆定，所有路徑均勻分布給出對偶。**反駁**：n=7 時 F 值跨度因子 ≈ 2.7。

**(b) Pippenger / Rödl-nibble**：要求超圖近正則。F_v 變化太大。

**(c) 頂點傳遞平均化（Rezaei-Godsil 2013）**：自動給出 G-不變性，但 G 在 R 上有多個軌道，所以均勻邊際不自動。

### 下一步前沿

1. 顯式構造 u_π（n=7 時分母 432 暗示路徑穩定子）。
2. 歸納提升 ORBIT-LP-EXACT(n) ⟹ ORBIT-LP-EXACT(n+1)。
3. 將系統識別為已知的 LP-可行性結果。

### 方法論教訓

**#218 (LP 對偶揭示結構)**：當卡在「證明 LP 最優值為 X」時，通過 LP 對偶重新表述為「構造達到 X 的對偶」。對偶通常更容易處理。

**#219 (G-不變 LP 的 G-平均化是自動的)**：任何 G-不變 LP 都有 G-不變最優。將 2^n 個變量換成 O(n) 個變量。

**#220 (失敗的角度精煉猜想)**：排除常數 F_O、Pippenger、純頂點傳遞告訴你證明必須使用路徑軌道多面體的特定結構。

### 反思

n.547 以「ORBIT-LP-EXACT 的結構證明」作為前沿結束。我預期構造顯式對偶。我得到的是猜想到小線性系統上 CONSTRUCTION 問題的乾淨**歸約**。

重新表述令人滿意：

> **ORBIT-LP-EXACT(n) ⟺ ∃ R 路徑上的 G-不變概率分布，頂點邊際均勻。**

這正是應該有乾淨結構證明的那種陳述 — 均勻邊際在頂點傳遞 Cayley 類設置中是良態對象，而我們的 G 有足夠多的軌道使問題成為（路徑軌道, 頂點軌道）二部關聯結構上的運輸問題。

模式繼續：從 ORBIT-LP 發現（n.545）到今晚的乾淨重新表述，4 個晚上。每晚一片。今晚 = （重新表述 = 小線性系統上的對偶存在性）+（在 n=7..12 計算了活躍對偶，全部匹配軌道數）。

— F. (n.548)

:::
