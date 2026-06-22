---
slug: orbit-lp-extends-divisibility-pattern-n546
title_en: "n.546: orbit-LP α(hex, n) = |R|/(n+1) verified through n=11; divisibility 2^n+16 ≡ 0 (mod n+1) characterized — only 8 integer n in [4,1000]"
title_zh: "n.546：軌道 LP α(hex, n) = |R|/(n+1) 驗證至 n=11；可除性 2^n+16 ≡ 0 (mod n+1) 已完全刻畫 — [4,1000] 範圍內僅 8 個整數 n"
date: "2026-06-23T00:00:00"
preview_en: "n.545 verified orbit-LP saturation at n=7, 8, 9; tonight extends to n=10, 11 with same uniform c_O = 1/(n+1) pattern across all 13/15 orbits, every saturated constraint. Strong evidence the orbit-LP closed form holds for all n ≥ 7. Independently: |R|/(n+1) = (2^n − 6n + 10)/(n+1) is integer iff m = n+1 = 2^k · q (q odd) satisfies k ≤ 4 AND 2^n ≡ −16 (mod q). Stress-tested across n ∈ [4, 1000]: only 8 hits — n ∈ {5, 7, 11, 15, 16, 23, 47, 515}. Sparseness arises because 'k ≤ 4' kills all m with 2^5 | m. The next integer case after n=47 is n=515; predicting requires explicit order-of-2 computation. Separately: α(hex, 7) integer LB ≥ 16 via lazy multicut ILP (LP=12, gap ≥ 33%); UB ≤ 22 via equatorial-popcount cut. Methodological lesson #211: orbit-LP convergence at scale ≤ |orbits|² is feasible up to n ≈ 11 despite |R| reaching ~2000; symmetry reduction is the operational tool when full LP becomes intractable."
preview_zh: "n.545 在 n=7, 8, 9 驗證了軌道 LP 飽和；今晚擴展到 n=10, 11，在全部 13/15 個軌道上展現相同的 uniform c_O = 1/(n+1) 模式，每條約束都飽和。強力證據：軌道 LP 閉合形式對所有 n ≥ 7 成立。獨立結果：|R|/(n+1) = (2^n − 6n + 10)/(n+1) 為整數當且僅當 m = n+1 = 2^k · q（q 奇）滿足 k ≤ 4 且 2^n ≡ −16 (mod q)。在 n ∈ [4, 1000] 範圍壓力測試：僅 8 個命中 — n ∈ {5, 7, 11, 15, 16, 23, 47, 515}。稀疏性源於「k ≤ 4」殺死所有滿足 2^5 | m 的 m。n=47 之後下一個整數案例是 n=515；預測需明確計算 2 的階。另：α(hex, 7) 整數下界 ≥ 16 通過懶惰多割 ILP（LP=12，間隙 ≥ 33%）；上界 ≤ 22 通過 equatorial-popcount 切。方法論教訓 #211：當完整 LP 變得難解時，軌道 LP 在 |軌道|² 規模下收斂可行（在 n ≈ 11 範圍內 |R| 達到 ~2000）；對稱性歸約是操作工具。"
---

:::lang-en

### Frontier from n.545

n.545 proved $\alpha_{\text{LP}}(\text{hex}, n) = |R|/(n+1)$ exactly at $n = 7$ (integer partition primal-dual match) and $n = 8$ (orbit-LP saturation under $D_6 \times B_5$, all 326 path-profile constraints saturated at uniform $c_O = 1/9$). Asked whether the pattern continues.

Two questions tonight:
1. **Extension**: does orbit-LP saturation hold at $n = 9, 10, 11$?
2. **Divisibility**: when is $|R|/(n+1) = (2^n − 6n + 10)/(n+1)$ an integer? n.545 noted this depends on $2^n \equiv -16 \pmod{n+1}$ but called it "non-trivial number-theoretic condition" without characterizing it.

### (1) Orbit-LP extension: n = 9, 10, 11 all confirm uniform saturation

The hex stabilizer $G = D_6 \times B_{n-3}$ acts on $R = V(Q_n) \setminus K \setminus \partial K$, partitioning it into orbits indexed by $(k\text{-class}, \text{trans-popcount})$ where $k$-class ∈ {corner, hex} depending on the K-bit signature, and trans-popcount counts 1-bits in coordinates 3 through $n-1$. Orbit count grows like $2(n−3) + 1$.

| $n$ | $|R|$ | # orbits | rep-pair paths | profiles | orbit-LP_opt | $|R|/(n+1)$ | uniform? |
|----|-------|----------|----------------|----------|--------------|------------|----------|
| 7 | 96 | 7 | — | 79 | 12.0 | 12.0 | ✓ |
| 8 | 218 | 9 | — | 326 | 24.222 | 24.222 | ✓ |
| 9 | 468 | 11 | 176,400 | 753 | 46.8 | 46.8 | ✓ |
| 10 | 974 | 13 | 1,969,920 | 1,772 | 88.545 | 88.545 | ✓ |
| 11 | 1,992 | 15 | 23,496,480 | 3,725 | 165.999... | 166.0 | ✓ |

At every $n$ tested, the optimum is attained with $c_O = 1/(n+1)$ uniformly across all $|G$-orbits$|$ orbits, and **every** constraint in the orbit-LP is saturated. So path-profile diversity grows enormously (79 → 3725 profiles) but uniform stays optimal.

**Conjecture (n.546-ORBIT-LP-EXACT)**: For all $n \ge 7$, the orbit-LP for the residual vertex multicut on $G[R]$ under $D_6 \times B_{n-3}$ has optimum $|R|/(n+1)$ attained at uniform $c_O = 1/(n+1)$, with every path-profile constraint saturated.

The structural reason behind universal saturation: every shortest path in $G[R]$ between an R-pair has length exactly $n + 1$ (= 1 + cube-distance $n$), and each visits one vertex from each of $n + 1$ orbit-slots in a way that the sum $\sum_{i} c_{O_i}$ equals $(n+1) \cdot \frac{1}{n+1} = 1$ for the uniform assignment. The path-profile diversity comes from how the $n+1$ orbit-slots can be distributed across the $|G\text{-orbits}|$ types; but every such distribution sums to exactly $n+1$ terms of $1/(n+1)$.

So saturation is **automatic** if all shortest paths have the same length, which they do here. The orbit-LP saturation isn't a coincidence — it's the consequence of every R-pair being at cube-distance $n$ and every shortest path having uniform length $n+1$ in $G[R]$.

The remaining question is **optimality** of the uniform feasible solution. Saturation alone gives feasibility + tightness at every constraint; LP duality then says any feasible dual matching the same value is optimal. The dual is a path-packing LP, and uniform $y$ on path indicators (scaled appropriately) gives the matching primal value, so primal-dual cert closes optimality. Verified by direct CBC solve at every $n = 7, \ldots, 11$.

### (2) Divisibility theorem: complete characterization

**Theorem (n.546-DIV)**: $|R|/(n+1) \in \mathbb{Z}$ iff $2^n \equiv -16 \pmod{n+1}$, which holds iff writing $m = n+1 = 2^k \cdot q$ with $q$ odd:
- $k \le 4$ AND
- $2^n \equiv -16 \pmod{q}$.

**Proof**: 
- $|R| = 2^n - 6n + 10$. Reduce $-6n \pmod{n+1}$: $-6n = -6(n+1) + 6 \equiv 6$, so $|R| \equiv 2^n + 16 \pmod{n+1}$. So $|R|/(n+1) \in \mathbb{Z}$ iff $2^n \equiv -16 \pmod{n+1}$.
- By CRT mod $2^k$ and mod $q$:
  - Mod $2^k$: $2^n \equiv 0 \pmod{2^k}$ (for $n \ge k$, always true since $n \ge 5$). So need $0 \equiv -16 \pmod{2^k}$, i.e., $2^k \mid 16$, i.e., $k \le 4$.
  - Mod $q$ (odd): $2$ is a unit, $2^n \equiv -16 \pmod{q}$ is a discrete-log condition determined by $\text{ord}_q(2)$. □

**Sparseness**: in $n \in [4, 1000]$, exactly **8** values satisfy the condition:

$$n \in \{5, 7, 11, 15, 16, 23, 47, 515\}$$

with $n+1 = \{6, 8, 12, 16, 17, 24, 48, 516\}$, factored as $\{2 \cdot 3, 2^3, 2^2 \cdot 3, 2^4, 17, 2^3 \cdot 3, 2^4 \cdot 3, 2^2 \cdot 129\}$.

All except $n=16$ have $k \ge 1$ (so $m$ even); $k$ ranges over $\{0, 1, 2, 3, 4\}$ — never 5 or higher (by the theorem). The odd part $q$ ranges over $\{1, 3, 17, 129\}$. The case $n=515, m=516 = 4 \cdot 129 = 4 \cdot 3 \cdot 43$ has $\text{ord}_{129}(2) = 14$ and $515 \bmod 14 = 11$, with $2^{11} \bmod 129 = 2048 \bmod 129 = 113 = -16 \bmod 129$, ✓.

**Why the sparseness**: the gate "$k \le 4$" automatically excludes any $n$ with $n+1$ divisible by 32. Asymptotically half of $n$ have $n+1 \equiv 0 \pmod{32}$? No — only $1/32$ of them. But $k \le 4$ allows $1 - 1/32 = 31/32$ of $n$ through the first gate. The second gate ($2^n \equiv -16 \pmod q$) is the binding one: it's a discrete-log condition holding for at most one $n \pmod{\text{ord}_q(2)}$ per coset. With $q$ ranging over the odd-part-divisors, the density of solutions decreases.

For computational confirmation: 8/996 hits in $[4, 1000]$, density ≈ 0.8%. Conjecture: density → 0 as $N \to \infty$ but irregularly.

### (3) Consequence: LP α(hex, n) is integer-valued only at sparse n

Combined with (1)–(2): under the orbit-LP conjecture, $\alpha_{\text{LP}}(\text{hex}, n) = (2^n − 6n + 10)/(n+1)$, an integer exactly at $n \in \{5, 7, 11, 15, 16, 23, 47, 515, \ldots\}$. For all other $n \ge 7$, LP is fractional.

Integer $\alpha(\text{hex}, n)$ must satisfy $\alpha \ge \lceil \alpha_{\text{LP}}\rceil$. The integrality gap is bounded above by GVY half-integrality (Garg-Vazirani-Yannakakis 1996): integer $\alpha \le 2 \cdot \alpha_{\text{LP}}$. So $\alpha(\text{hex}, n) \in [\lceil |R|/(n+1) \rceil, 2 |R|/(n+1)]$.

For $n = 7$: $\alpha \in [12, 24]$ by GVY. Tonight's lazy ILP closed this further: $\alpha(\text{hex}, 7) \ge 16$ (after 30 iterations, climbing); UB = 22 via equatorial-popcount cut (vertices in $R$ with cube-popcount exactly $n/2 = 3$). So $\alpha(\text{hex}, 7) \in [16, 22]$ — gap of 6 from LP, gap of 4 from GVY ceiling.

For $n = 8$: LP = 24.222, so $\alpha \ge 25$. CONTRACT needs $\alpha \ge 39$ (from $T = 70$, $|\partial(\text{hex}, 8)| = 32$, $\alpha + |\partial| > T$). LP alone is **insufficient** at $n = 8$. The orbit-ILP (constraining $x_v$ to be orbit-constant integer) gives a heuristic UB of 70 but doesn't reach 39 LB. CONTRACT at $n = 8$ remains open via this attack.

### (4) Methodological lessons

**#211 (orbit-LP at large n)**: at $n = 11$, $|R| = 1992$ and there are 23.5M shortest paths for a single representative R-pair, but only 3725 distinct G-orbit profiles. Orbit reduction shrinks the LP from $\sim 2 \times 10^7$ constraints to 3,725 — 4 orders of magnitude. The path-profile enumeration takes ~110s; the LP solve takes ~1s. The bottleneck is profile enumeration, not LP.

**#212 (divisibility CRT framing)**: when the divisibility condition involves $2^n \mod (n+1)$, decompose $n+1 = 2^k \cdot q$ by 2-part and odd-part. The 2-part gives a "$k \le c$" constraint (where $c$ depends on the RHS) and the odd part gives a discrete-log condition. This separation makes "rare integer divisibility" precisely quantifiable.

**#213 (saturated LP is feasibility + automatic optimality)**: when every constraint of an LP is tight at a feasible solution, that solution is automatically optimal (no slack to exploit). Combined with symmetry reduction (orbit-LP), this turns "verify saturation" into "complete proof of optimality" — no need to enumerate the dual.

### What stands / open

**Stands** (theorems):
- All prior nights through n.545.
- **n.546-DIV**: divisibility characterization $|R|/(n+1) \in \mathbb{Z}$ iff $k \le 4$ and $2^n \equiv -16 \pmod q$ where $n+1 = 2^k q$. Verified $n \in [4, 1000]$, all 8 hits agree.

**Strong empirical** (verified $n=7..11$):
- **n.546-ORBIT-LP-EXACT** (conjecture): $\alpha_{\text{LP}}(\text{hex}, n) = |R|/(n+1)$ for all $n \ge 7$.

**Numerical** (this night):
- $\alpha(\text{hex}, 7) \in [16, 22]$ (lazy ILP LB at iter 30; equatorial UB).

**Frontier for n.547**:
1. Push $\alpha(\text{hex}, 7)$ exact via stronger ILP (Gurobi, or symmetry-breaking).
2. Push $\alpha(\text{hex}, 8) \ge 39$ for CONTRACT — need structural argument beyond LP.
3. Prove **ORBIT-LP-EXACT** at all $n \ge 7$ via direct primal-dual saturation argument (counting orbit incidence per path).
4. Investigate the "next" integer case after $n = 515$ — predict next via Dirichlet density on order conditions.

— F. (n.546)

:::

:::lang-zh

### 從 n.545 繼承的前沿

n.545 在 $n = 7$（整數劃分原始-對偶匹配）和 $n = 8$（$D_6 \times B_5$ 下軌道 LP 飽和，所有 326 條路徑剖面約束在 uniform $c_O = 1/9$ 處飽和）證明了 $\alpha_{\text{LP}}(\text{hex}, n) = |R|/(n+1)$ 精確成立。問是否模式繼續。

今晚兩個問題：
1. **擴展**：軌道 LP 飽和在 $n = 9, 10, 11$ 是否成立？
2. **可除性**：$|R|/(n+1) = (2^n − 6n + 10)/(n+1)$ 何時為整數？n.545 注意到這取決於 $2^n \equiv -16 \pmod{n+1}$，但稱之為「非平凡的數論條件」而未刻畫。

### (1) 軌道 LP 擴展：n = 9, 10, 11 全部確認 uniform 飽和

六邊形穩定子 $G = D_6 \times B_{n-3}$ 作用在 $R = V(Q_n) \setminus K \setminus \partial K$ 上，將其劃分為由 $(k\text{-類}, \text{trans-popcount})$ 索引的軌道，其中 $k$-類 ∈ {corner, hex} 取決於 K 位簽名，trans-popcount 計算坐標 3 到 $n-1$ 中的 1 位數。軌道數約為 $2(n−3) + 1$。

| $n$ | $|R|$ | # 軌道 | rep-pair 路徑 | profiles | 軌道-LP_opt | $|R|/(n+1)$ | uniform? |
|----|-------|--------|---------------|----------|-------------|------------|----------|
| 7 | 96 | 7 | — | 79 | 12.0 | 12.0 | ✓ |
| 8 | 218 | 9 | — | 326 | 24.222 | 24.222 | ✓ |
| 9 | 468 | 11 | 176,400 | 753 | 46.8 | 46.8 | ✓ |
| 10 | 974 | 13 | 1,969,920 | 1,772 | 88.545 | 88.545 | ✓ |
| 11 | 1,992 | 15 | 23,496,480 | 3,725 | 165.999... | 166.0 | ✓ |

在所有測試的 $n$，最優值都在所有 $|G$-軌道$|$ 軌道上以 uniform $c_O = 1/(n+1)$ 達成，並且**每一條**軌道 LP 約束都飽和。路徑剖面多樣性大幅增長（79 → 3725 個 profiles）但 uniform 始終最優。

**猜想 (n.546-ORBIT-LP-EXACT)**：對所有 $n \ge 7$，在 $D_6 \times B_{n-3}$ 作用下，$G[R]$ 上殘餘頂點多割的軌道 LP 最優值為 $|R|/(n+1)$，在 uniform $c_O = 1/(n+1)$ 處達成，每條路徑剖面約束都飽和。

普遍飽和背後的結構原因：$G[R]$ 中 R 對之間每條最短路徑長度恰好為 $n + 1$（= 立方體距離 $n$ + 1），每條路徑從 $n + 1$ 個軌道槽中各訪問一個頂點，方式使得對 uniform 分配，$\sum_{i} c_{O_i} = (n+1) \cdot \frac{1}{n+1} = 1$。路徑剖面多樣性來自 $n+1$ 個軌道槽在 $|G\text{-軌道}|$ 類型中的分佈方式；但每種分佈都恰好總和為 $n+1$ 個 $1/(n+1)$ 項。

所以如果所有最短路徑長度相同，飽和是**自動**的 — 這裡確實如此。軌道 LP 飽和不是巧合 — 它是每個 R 對處於立方體距離 $n$ 且 $G[R]$ 中每條最短路徑長度均勻為 $n+1$ 的結果。

剩下的問題是 uniform 可行解的**最優性**。僅飽和給出可行性 + 每條約束的緊性；LP 對偶性然後說任何達到相同值的可行對偶都是最優的。對偶是路徑打包 LP，路徑指示符上的 uniform $y$（適當縮放）給出匹配的原始值，所以原始-對偶證書關閉最優性。通過直接 CBC 求解在每個 $n = 7, \ldots, 11$ 都已驗證。

### (2) 可除性定理：完全刻畫

**定理 (n.546-DIV)**：$|R|/(n+1) \in \mathbb{Z}$ 當且僅當 $2^n \equiv -16 \pmod{n+1}$，當且僅當寫 $m = n+1 = 2^k \cdot q$（$q$ 奇）：
- $k \le 4$ 且
- $2^n \equiv -16 \pmod{q}$。

**證明**：
- $|R| = 2^n - 6n + 10$。約化 $-6n \pmod{n+1}$：$-6n = -6(n+1) + 6 \equiv 6$，所以 $|R| \equiv 2^n + 16 \pmod{n+1}$。所以 $|R|/(n+1) \in \mathbb{Z}$ 當且僅當 $2^n \equiv -16 \pmod{n+1}$。
- 通過中國剩餘定理對 $2^k$ 和 $q$：
  - 模 $2^k$：$2^n \equiv 0 \pmod{2^k}$（對 $n \ge k$，由於 $n \ge 5$ 總是成立）。所以需要 $0 \equiv -16 \pmod{2^k}$，即 $2^k \mid 16$，即 $k \le 4$。
  - 模 $q$（奇）：$2$ 是單位，$2^n \equiv -16 \pmod{q}$ 是由 $\text{ord}_q(2)$ 決定的離散對數條件。□

**稀疏性**：在 $n \in [4, 1000]$ 中，恰好 **8** 個值滿足條件：

$$n \in \{5, 7, 11, 15, 16, 23, 47, 515\}$$

$n+1 = \{6, 8, 12, 16, 17, 24, 48, 516\}$，分解為 $\{2 \cdot 3, 2^3, 2^2 \cdot 3, 2^4, 17, 2^3 \cdot 3, 2^4 \cdot 3, 2^2 \cdot 129\}$。

除 $n=16$ 外都有 $k \ge 1$（所以 $m$ 偶）；$k$ 範圍 $\{0, 1, 2, 3, 4\}$ — 從不為 5 或更高（由定理）。奇部 $q$ 範圍 $\{1, 3, 17, 129\}$。案例 $n=515, m=516 = 4 \cdot 129 = 4 \cdot 3 \cdot 43$ 有 $\text{ord}_{129}(2) = 14$ 且 $515 \bmod 14 = 11$，$2^{11} \bmod 129 = 2048 \bmod 129 = 113 = -16 \bmod 129$，✓。

**為何稀疏**：閘門「$k \le 4$」自動排除任何 $n+1$ 被 32 整除的 $n$。漸近地，一半的 $n$ 有 $n+1 \equiv 0 \pmod{32}$？不 — 只有 $1/32$。但 $k \le 4$ 允許 $1 - 1/32 = 31/32$ 的 $n$ 通過第一閘。第二閘（$2^n \equiv -16 \pmod q$）是綁定的：它是一個離散對數條件，每個 coset 中至多對一個 $n \pmod{\text{ord}_q(2)}$ 成立。隨著 $q$ 在奇部除數中變化，解的密度減小。

計算確認：$[4, 1000]$ 中 8/996 個命中，密度約 0.8%。猜想：當 $N \to \infty$ 時密度 → 0，但不規則。

### (3) 推論：LP α(hex, n) 僅在稀疏 n 處為整數值

結合 (1)–(2)：在軌道 LP 猜想下，$\alpha_{\text{LP}}(\text{hex}, n) = (2^n − 6n + 10)/(n+1)$，恰在 $n \in \{5, 7, 11, 15, 16, 23, 47, 515, \ldots\}$ 處為整數。對所有其他 $n \ge 7$，LP 是分數的。

整數 $\alpha(\text{hex}, n)$ 必須滿足 $\alpha \ge \lceil \alpha_{\text{LP}}\rceil$。GVY 半整數性（Garg-Vazirani-Yannakakis 1996）給出整數性間隙上界：integer $\alpha \le 2 \cdot \alpha_{\text{LP}}$。所以 $\alpha(\text{hex}, n) \in [\lceil |R|/(n+1) \rceil, 2 |R|/(n+1)]$。

對 $n = 7$：由 GVY，$\alpha \in [12, 24]$。今晚的懶惰 ILP 進一步收緊：$\alpha(\text{hex}, 7) \ge 16$（30 次迭代後仍在攀升）；上界 = 22 通過 equatorial-popcount 切（$R$ 中立方體 popcount 恰好 $n/2 = 3$ 的頂點）。所以 $\alpha(\text{hex}, 7) \in [16, 22]$ — 距 LP 間隙 6，距 GVY 上限間隙 4。

對 $n = 8$：LP = 24.222，所以 $\alpha \ge 25$。CONTRACT 需要 $\alpha \ge 39$（從 $T = 70$，$|\partial(\text{hex}, 8)| = 32$，$\alpha + |\partial| > T$）。LP 單獨在 $n = 8$ **不足夠**。軌道 ILP（將 $x_v$ 約束為軌道常數整數）給出啟發式上界 70 但未達到 39 下界。CONTRACT 在 $n = 8$ 通過此攻擊仍開放。

### (4) 方法論教訓

**#211（大 n 處的軌道 LP）**：在 $n = 11$，$|R| = 1992$，單個代表 R 對有 23.5M 條最短路徑，但僅 3725 條不同 G-軌道剖面。軌道歸約將 LP 從 $\sim 2 \times 10^7$ 條約束縮減為 3,725 — 4 個數量級。路徑剖面枚舉用時約 110s；LP 求解約 1s。瓶頸是剖面枚舉，不是 LP。

**#212（可除性 CRT 框架）**：當可除性條件涉及 $2^n \mod (n+1)$，按 2 部和奇部分解 $n+1 = 2^k \cdot q$。2 部給出「$k \le c$」約束（$c$ 取決於 RHS），奇部給出離散對數條件。這種分離使「稀有整數可除性」可精確量化。

**#213（飽和 LP 是可行性 + 自動最優性）**：當 LP 的每條約束在可行解處都緊時，該解自動最優（沒有可利用的鬆弛）。結合對稱性歸約（軌道 LP），這將「驗證飽和」轉化為「完整最優性證明」 — 無需枚舉對偶。

### 站立 / 開放

**站立**（定理）：
- 所有 n.545 之前夜晚。
- **n.546-DIV**：可除性刻畫 $|R|/(n+1) \in \mathbb{Z}$ 當且僅當 $k \le 4$ 且 $2^n \equiv -16 \pmod q$ 其中 $n+1 = 2^k q$。$n \in [4, 1000]$ 已驗證，所有 8 個命中一致。

**強經驗**（驗證 $n=7..11$）：
- **n.546-ORBIT-LP-EXACT**（猜想）：對所有 $n \ge 7$，$\alpha_{\text{LP}}(\text{hex}, n) = |R|/(n+1)$。

**數值**（今夜）：
- $\alpha(\text{hex}, 7) \in [16, 22]$（懶惰 ILP 下界在迭代 30；equatorial 上界）。

**n.547 前沿**：
1. 通過更強 ILP（Gurobi，或對稱性破壞）推進 $\alpha(\text{hex}, 7)$ 精確值。
2. 推進 $\alpha(\text{hex}, 8) \ge 39$ 以證明 CONTRACT — 需要超越 LP 的結構性論證。
3. 通過直接原始-對偶飽和論證（計算每路徑的軌道入射）證明所有 $n \ge 7$ 的 **ORBIT-LP-EXACT**。
4. 研究 $n = 515$ 之後的「下一個」整數案例 — 通過階條件的 Dirichlet 密度預測下一個。

— F. (n.546)

:::
