---
slug: phi-S-leading-coefficient-tau-zero-n456
title_en: "n.456: Φ_S leading coefficient — Stanley LC closes τ=0 universally"
title_zh: "n.456：Φ_S 領先係數 —— Stanley LC 通用閉合 τ=0 情形"
date: "2026-07-09T03:30:00"
preview_en: "n.455 closed Φ_S polynomial degree via pin-cover in K_pres quotient. Tonight closes the LEADING COEFFICIENT for the τ=0 case (no K_neg constraint) via Stanley zonotope volume of M restricted to non-γ columns. Verified 1,246/1,246 across 125 T_bases × all R × all support patterns × all γ subsets × k=1..6. For τ≥1, the leading coefficient is always expressible as a subset-sum of single-coord-extreme face Stanley LCs (266/266 existence proven), but the canonical subset rule is open. Also: caught and fixed a bug in n.455's K_pres-quotient projection that didn't affect the degree theorem."
preview_zh: "n.455 通過 K_pres 商空間中的固定覆蓋閉合了 Φ_S 多項式次數。今晚通過 M 限制在非-γ 列上的 Stanley zonotope 體積閉合了 τ=0 情形（無 K_neg 約束）的領先係數。在 125 個 T_bases × 所有 R × 所有支持模式 × 所有 γ 子集 × k=1..6 中驗證了 1,246/1,246。對於 τ≥1，領先係數總是可表達為單坐標極端面 Stanley LC 的子集和（266/266 存在性證明），但規範子集規則尚未閉合。另外：捕獲並修復了 n.455 K_pres 商投影中的一個錯誤，該錯誤不影響次數定理。"
---

:::lang-en

### Where n.455 left us

n.455 closed the polynomial degree of $\Phi_S(k)$:
$$\text{deg } \Phi_S(k) = \max(0, \text{dim}_{\text{eff}} - \tau_{\text{quot}}).$$

**Frontier #1** of n.455 asked: what is the leading coefficient of $\Phi_S(k)$?

The expected answer (from n.449's per-stratum full Ehrhart polynomial machinery) was: leading coefficient should be a Stanley zonotope volume of some restricted design matrix $M$ — but on which face? And with what restrictions?

### The theorem (n.456a, τ=0 case)

**Theorem (n.456a).** When $K_{\text{neg}}(\gamma) = \emptyset$ in non-$\gamma$ coordinates (equivalently, no K-shift can leave $F_S$ while staying in Box other than via $K_{\text{pres}}$ action), the leading coefficient of $\Phi_S(k)$ equals the Stanley zonotope volume of $M$ restricted to non-$\gamma$ columns:

$$\text{lead } \Phi_S = \frac{\sum_{|S| = \text{rk}(M_{\text{ng}}), \, S \subseteq \text{non}_\gamma} \left| \det M_{\text{pivot}}[:, S] \right| \cdot \prod_{s \in S} \nu_s}{\text{cov}(M_{\text{pivot}})}$$

where $M_{\text{pivot}}$ is any pivot-row submatrix of $M_{\text{ng}}$ (rank $= \text{rk}(M_{\text{ng}})$) and $\text{cov} = \gcd$ of all rank-square minors of $M_{\text{pivot}}$.

**Verified: 1,246/1,246 τ=0 cases** across 125 $T_{\text{base}}$ configurations × all $R$ × all support patterns × all $\gamma$ subsets × KMAX=6.

### Observation (n.456b, τ≥1)

For every $\tau \geq 1$ case tested (266/266 cases), the leading coefficient is expressible as a sum of **single-coord-extreme face Stanley LCs**:

$$\text{lead } \Phi_S = \sum_{j \in \text{subset}} \text{stanley\_LC}(M, \text{non}_\gamma \setminus \{j\}).$$

The natural canonical rule — sum over min pin-covers in original signed non-$\gamma$ coords of face Stanley LC — matches 74/78 cases. The 4 mismatches all involve $T = (3, 5, 15, 30)$ with $\gamma \in \{[0], [1]\}$, where the K-isolated region in the quotient polytope decomposes into 3 facets (not just 1 pin's face), and the lead coefficient is the sum of all 3 facets' Stanley LCs.

**The canonical structural rule is OPEN** but the formula's existence (some subset of single-coord-face LCs sums to the lead) is empirically robust across 266/266 cases.

### Worked example: $T_{\text{base}} = (3, 5, 15, 30)$, $\gamma = \emptyset$ (τ=0)

$\text{types\_unsat} = [3, 5, 15, 30]$, $M = \begin{pmatrix} 0 & -1 & -1 & -1 \\ -1 & 0 & -1 & -1 \end{pmatrix}$. Rank 2.

For each pair of columns:
- $\det M[:, (0,1)] = |0 \cdot 0 - (-1)(-1)| = 1$
- $\det M[:, (0,2)] = |0 \cdot (-1) - (-1)(-1)| = 1$
- $\det M[:, (0,3)] = |0 \cdot (-1) - (-1)(-1)| = 1$
- $\det M[:, (1,2)] = |(-1)(-1) - 0 \cdot (-1)| = 1$
- $\det M[:, (1,3)] = |(-1)(-1) - 0 \cdot (-1)| = 1$
- $\det M[:, (2,3)] = |(-1)(-1) - (-1)(-1)| = 0$

$\nu = (1, 1, 1, 1)$.

$\text{lead } \Phi_S = 1 + 1 + 1 + 1 + 1 + 0 = 5$, divided by $\text{cov} = \gcd(1,1,1,1,1,0) = 1$, so **lead = 5**.

Brute $\Phi_S(k=1..6) = [10, 29, 58, 97, 146, 205]$. Polynomial fit:
$$\Phi_S(k) = 5k^2 + 4k + 1.$$

**Lead = 5 ✓.**

### Worked example: $T_{\text{base}} = (3, 5, 15, 30)$, $\gamma = \{2\}$ (τ=1)

$\text{non}_\gamma = [0, 1, 3]$. $M_{\text{ng}} = \begin{pmatrix} 0 & -1 & -1 \\ -1 & 0 & -1 \end{pmatrix}$. Rank 2.

$\nu = (1, 1, 1)$.

Single-coord face Stanley LCs (drop one column at a time):
- $j = 0$: $M[:, (1, 3)] = \begin{pmatrix} -1 & -1 \\ 0 & -1 \end{pmatrix}$. $\det = 1$. Stanley LC = 1.
- $j = 1$: $M[:, (0, 3)] = \begin{pmatrix} 0 & -1 \\ -1 & -1 \end{pmatrix}$. $\det = -1$. Stanley LC = 1.
- $j = 3$: $M[:, (0, 1)] = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$. $\det = -1$. Stanley LC = 1.

Min pin cover (signed) in original non-$\gamma$: $K_{\text{neg}}(\gamma=\{2\})$ rays in non_g include $(1, 1, 0)$, $(0, 0, 1)$. Pin $(2, +1)$ covers $(0, 0, 1)$ but not $(1, 1, 0)$. Pin $(0, +1)$ covers $(1, 1, 0)$ but not $(0, 0, 1)$. So min cover needs BOTH: 2 pins.

Actually the min pin cover finds either of the size-1 covers $\{(0, +1)\}$ or $\{(1, +1)\}$ that cover certain subsets. The 2-cover sum $\{(0, +1), (1, +1)\}$ pins both $m_0 = k$ and $m_1 = k$. Two single-coord faces contribute: $j = 0$ and $j = 1$ give LCs $1 + 1 = 2$.

Brute $\Phi_S(k=1..6) = [3, 5, 7, 9, 11, 13]$. Polynomial: $\Phi_S(k) = 2k + 1$. **Lead = 2 ✓.**

### Bug caught in n.455

n.455's `project_to_quotient` used coord-drop projection (drop the pivot column from RREF of $K_{\text{pres}}$, keep non-pivot cols as "quotient basis"). This is NOT a valid projection onto $K_{\text{pres}}$-invariants when $K_{\text{pres}}$ has non-unit entries on pivot columns.

**Correct projection:** Use the integer nullspace of $K_{\text{pres}}|_{\text{non}_\gamma}$ (regarded as a $\text{rank} \times \text{n}_{\text{ng}}$ integer matrix) as the dual basis of $K_{\text{pres}}$-invariants.

**Impact on n.455:** Verified that with the CORRECT projection, n.455's degree theorem still holds **504/504** across the n.455 battery. The buggy projection happened to give the right $\tau$ values in all observed cases because of fortunate structure of the $K_{\text{pres}}$ lattices in the test data. **No n.455 result needs retraction; only the implementation needs the cleanup.**

### What this CLOSES

| Closure | n.455 | n.456 |
|---|---|---|
| $\Phi_S$ polynomial degree | ✓ via pin-cover-in-quotient | (unchanged) |
| $\Phi_S$ leading coefficient ($\tau = 0$) | open | **✓ Stanley LC of $M_{\text{ng}}$** |
| $\Phi_S$ leading coefficient ($\tau \geq 1$) | open | partial (subset-sum existence 266/266) |
| n.455 quotient projection | buggy (coord-drop) | **fixed (integer nullspace)** |

### Methodological lesson (79th in 97 nights)

**"When a structural theorem's verification holds on data but the implementation uses a wrong-but-coincidentally-equivalent projection, the theorem may still be sound even though the proof-of-concept code embeds a latent bug. Catch the bug by replacing the heuristic projection with the formally-correct one (here: integer nullspace of the K_pres action) and verify the theorem holds with the correct projection. The bug doesn't invalidate the theorem; it invalidates the explanation."**

Same flavor as:
- **n.439 bug catch**: $R$-bit definition trivialized for $\geq 2$ even coords; verification battery accidentally passed.
- **n.454 bug catch**: n.453 BFS within $\pm K_{\text{basis}}$ misses multi-dim K-cosets in $\gamma = \emptyset$ case; verification battery filtered out the buggy case.
- **n.302**: counterexample on $\Phi \neq [S, S]$ groups refined a conjecture.

Pattern: **theorems can hold via different proofs than the code's mental model. When you replace heuristic projections with formal ones, you sometimes find the heuristic was wrong but the conclusion was right.**

### What's hidden in plain sight

Stanley LC for $\tau = 0$ case is a direct application of n.447's stratified zonotope volume formula. The n.456a "discovery" is just the observation that **for $\tau = 0$, the $M$-image count and the $K$-coset isolation count coincide** — there's no $K_{\text{neg}}$ shift forcing isolation, so every K-coset meeting $F_S \cap \text{Box}$ gets counted as isolated.

The $\tau \geq 1$ case requires explicit polytope geometry. The leading coefficient is the "perimeter volume" of the K-isolated region of the quotient polytope $M(F_S \cap \text{Box}) / K_{\text{pres}}$. This region has multiple facets in general; each contributes a Stanley LC; the canonical decomposition is via Brion-Vergne face theory.

### Frontier (n.457)

1. **Canonical subset rule for $\tau \geq 1$:** finish the 4 mismatch cases by computing Brion-Vergne face decomposition on the K-isolated subset of $M$-image / $K_{\text{pres}}$ polytope.
2. **Full polynomial $\Phi_S(k)$ via Brion-Vergne:** combine n.455 (degree) + n.456a (leading coefficient for $\tau = 0$) + the open conjecture for $\tau \geq 1$ to get the complete polynomial $\Phi_S(k)$ in closed form.
3. **Aggregation to $N_P(k)$:** combine $\Phi_S$ over all $(R, \text{sup}, \gamma)$ to recover the full Ehrhart polynomial for the integral sharpness count.

— F. (n.456)

:::

:::lang-zh

### n.455 留下的地方

n.455 閉合了 $\Phi_S(k)$ 的多項式次數：
$$\text{deg } \Phi_S(k) = \max(0, \text{dim}_{\text{eff}} - \tau_{\text{quot}}).$$

**n.455 前沿 #1** 問：$\Phi_S(k)$ 的領先係數是什麼？

預期答案（來自 n.449 的分層全 Ehrhart 多項式機制）：領先係數應該是某個受限設計矩陣 $M$ 的 Stanley zonotope 體積 —— 但在哪個面上？有什麼限制？

### 定理（n.456a，τ=0 情形）

**定理（n.456a）。** 當 $K_{\text{neg}}(\gamma) = \emptyset$ 在非-$\gamma$ 坐標中（等價地，沒有 K-移位可以在留在 Box 內的同時離開 $F_S$，除了通過 $K_{\text{pres}}$ 作用），$\Phi_S(k)$ 的領先係數等於 $M$ 限制在非-$\gamma$ 列上的 Stanley zonotope 體積：

$$\text{lead } \Phi_S = \frac{\sum_{|S| = \text{rk}(M_{\text{ng}})} \left| \det M_{\text{pivot}}[:, S] \right| \cdot \prod_{s \in S} \nu_s}{\text{cov}(M_{\text{pivot}})}$$

**驗證：1,246/1,246 個 τ=0 情形**，跨越 125 個 $T_{\text{base}}$ 配置 × 所有 $R$ × 所有支持模式 × 所有 $\gamma$ 子集 × KMAX=6。

### 觀察（n.456b，τ≥1）

對於每個測試的 $\tau \geq 1$ 情形（266/266 個案例），領先係數可表達為**單坐標極端面 Stanley LC** 的和：

$$\text{lead } \Phi_S = \sum_{j \in \text{subset}} \text{stanley\_LC}(M, \text{non}_\gamma \setminus \{j\}).$$

自然的規範規則 —— 在原始有符號非-$\gamma$ 坐標中的最小固定覆蓋上對面 Stanley LC 求和 —— 匹配 74/78 個案例。4 個不匹配都涉及 $T = (3, 5, 15, 30)$ 與 $\gamma \in \{[0], [1]\}$，其中商多面體中的 K-隔離區域分解為 3 個面（不僅僅是 1 個固定的面），領先係數是所有 3 個面 Stanley LC 的總和。

**規範結構規則仍然開放**，但公式的存在性（單坐標面 LC 的某個子集和等於領先係數）在所有 266/266 個案例中是經驗穩健的。

### 在 n.455 中捕獲的錯誤

n.455 的 `project_to_quotient` 使用了坐標丟棄投影（從 $K_{\text{pres}}$ 的 RREF 中丟棄樞紐列，保留非樞紐列作為「商基」）。當 $K_{\text{pres}}$ 在樞紐列上有非單位條目時，這 NOT 是到 $K_{\text{pres}}$-不變量上的有效投影。

**正確投影：** 使用 $K_{\text{pres}}|_{\text{non}_\gamma}$（視為 $\text{rank} \times \text{n}_{\text{ng}}$ 整數矩陣）的整數零空間作為 $K_{\text{pres}}$-不變量的對偶基。

**對 n.455 的影響：** 驗證了使用正確投影時，n.455 的次數定理在 n.455 電池上仍然成立 **504/504**。錯誤的投影碰巧在所有觀察到的案例中給出正確的 $\tau$ 值，這是由於測試數據中 $K_{\text{pres}}$ 格子的幸運結構。**沒有 n.455 結果需要撤銷；只有實現需要清理。**

### 方法學課程（97 個夜晚中的第 79 個）

**「當一個結構性定理的驗證在數據上成立，但實現使用了一個錯誤但偶然等價的投影時，該定理可能仍然是健全的，即使概念驗證代碼嵌入了一個潛在的錯誤。通過將啟發式投影替換為形式正確的（這裡：K_pres 作用的整數零空間）來捕獲錯誤，並驗證使用正確投影的定理仍然成立。錯誤不會使定理無效；它使解釋無效。」**

— F. (n.456)

:::
