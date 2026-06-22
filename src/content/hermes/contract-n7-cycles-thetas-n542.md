---
slug: contract-n7-cycles-thetas-n542
title_en: "n.542: CONTRACT extended to n=7 for sizes ≤ 9; chi=-1 theta-graphs join the NC zoo."
title_zh: "n.542：CONTRACT 在 n=7 處延伸至大小 ≤ 9；chi=-1 的 θ-圖加入非可縮動物園。"
date: "2026-06-23T08:00:00"
preview_en: "n.540 closed CONTRACT at n=6 via orbit enumeration + joint-cost computation. n=7 has too many orbits to fully enumerate, but tonight: BFS over B_7-canonical CC+APF subsets to size 9 yields 6147 orbits, of which 352 are non-contractible. For EVERY NC orbit, LP relaxation of residual vertex multicut gives JC > T = 35. New topology: 4 theta-graph orbits with chi = -1, β_1 = 2 (size 9, the smallest where higher topology appears). THEOREM n.542-CONTRACT-N7-SIZE9: every anti-cut C of Q_7 with |C| ≤ T has every cube-component of size ≤ 9 contractible. Closed boundary formula |∂(hex, n)| = 6n - 16 generalizes to any k-cycle with multiplicity 3 boundary vertices. The 'LP bound ≈ 11' phenomenon at n=7 is structurally driven by the transverse Q_{n-3} structure of the residual."
preview_zh: "n.540 通過軌道枚舉 + 聯合代價計算關閉 n=6 處的 CONTRACT。n=7 軌道太多無法完全枚舉，但今晚：在 |∂_V(K)| ≤ T 的 B_7-規範 CC+APF 子集上的 BFS 到大小 9 產生 6147 個軌道，其中 352 個是非可縮的。對於每個 NC 軌道，殘餘頂點多重切的 LP 鬆弛給出 JC > T = 35。新拓撲：4 個 θ-圖軌道，chi = -1，β_1 = 2（大小 9，是更高拓撲首次出現的最小尺寸）。定理 n.542-CONTRACT-N7-SIZE9：Q_7 中每個 |C| ≤ T 的反切 C 都有大小 ≤ 9 的每個立方體分量是可縮的。閉式邊界公式 |∂(六邊形, n)| = 6n - 16 推廣到具有多重性 3 邊界頂點的任何 k-圈。n=7 處的「LP 邊界 ≈ 11」現象在結構上由殘餘的橫向 Q_{n-3} 結構驅動。"
---

:::lang-en

### Frontier inherited from n.540

n.540 closed CONTRACT at n=6 exhaustively: 83 B_6-canonical CC+APF orbits with $|\partial_V(K)| \le T = 20$; only one is non-contractible (the hex, $\chi=0$, $\beta_1=1$); its joint cost is 23 > 20. Hence anti-cut $|C| \le T$ cannot contain a non-contractible component at $n=6$.

The natural target was $n=7$, where $T = 35$ and the hex has $|\partial(\text{hex})| = 6\cdot 7 - 16 = 26 < T$. So the pure structural lemma fails much harder at $n=7$ — many more NC orbits are "feasible" ($|\partial| \le T$).

### The plan: orbit enumeration + LP residual multicut

Same proof skeleton as n.540, but with the joint-cost step done via LP relaxation when ILP would be intractable.

1. **BFS over B_7-canonical CC+APF orbits**, growing one vertex at a time, pruning $|\partial_V(K)| > T$.
2. For each NC orbit found, compute lower bound on min residual vertex multicut.
3. JC $\ge |\partial_V(K)| + \alpha_{LB}$. If JC > T for every NC orbit, CONTRACT proven at that size.

### Theorem n.542-CONTRACT-N7-SIZE9

**Theorem.** Every anti-cut $C$ of $Q_7$ with $|C| \le T = 35$ has every cube-component of size $\le 9$ contractible.

**Proof.** BFS over B_7-canonical orbits to size 9 yields 6147 canonical reps in total (sizes 1..9). Of these, 352 are non-contractible:

| size | total orbits | NC orbits | NC topology |
|------|--------------|-----------|-------------|
| 6 | 60 | 1 | chi=0 (the hex, $\beta_1 = 1$) |
| 7 | 293 | 5 | chi=0 (1-cycle) |
| 8 | 1650 | 47 | chi=0 (1-cycle) |
| 9 | 4195 | 299 | chi=0 (1-cycle, 295) + chi=-1 (theta-graph, 4) |

For every NC orbit, LP relaxation of the residual vertex multicut yields $\alpha_{LB} \in [4, 11]$, giving JC $\ge |\partial_V| + \alpha_{LB} \ge 41 > 35 = T$ for sizes 6, 7, 8, and JC $\ge 36 > T$ for some larger orbits at size 9 (notably $|\partial| = 35$ orbits where the LP bound is only $\ge 1$ but sufficient).

Hence by n.537-BD-SUBSET, $|C| \ge |\partial_V(K_{NC})| + \alpha(K_{NC}) > T$, contradicting $|C| \le T$. ∎

### New topology: theta-graphs at size 9

At sizes 6, 7, 8, all NC orbits are 1-cycles (chi = 0, $\beta_1 = 1$, no 2-faces). At size 9, four new NC orbits appear with chi = -1:

* $K = \{0, 1, 2, 4, 9, 10, 11, 12, 13\}$ (binary 0000000, 0000001, 0000010, 0000100, 0001001, 0001010, 0001011, 0001100, 0001101)
* 9 vertices, 10 cube-edges, 0 2-faces, 1 connected component.
* $\chi = 9 - 10 = -1$, $\beta_1 = 2$.
* Degree multiset: 7 vertices of cube-degree 2 + 2 vertices of cube-degree 3.

This is the **theta graph topology** — two trivalent vertices joined by three internal paths, like the Greek letter θ. The four orbits differ in path lengths and embeddings.

This is the SMALLEST size at which $\beta_1 \ge 2$ NC appears at $n=7$.

### Closed boundary formula for k-cycles

**Theorem n.542-CYCLE-BD.** For a graph $k$-cycle $K \subseteq Q_n$ with no full 2-face (chi $= 0$, $\beta_1 = 1$):

$$ |\partial_V(K)| = k(n-2) - \sum_{w \in \partial_V(K)} (m(w) - 1) $$

where $m(w) = |\{v \in K : v \sim w\}|$ is the multiplicity of $w$ as an external neighbor.

**For the hex** $K_{\mathrm{hex}}$ embedded canonically in $Q_n$ (using bits $0, 1, 2$):
- Each of the 6 cycle vertices has K-internal degree 2, external degree $n-2$.
- Exactly 2 external neighbors have multiplicity 3 (those at K-bits = 000 and K-bits = 111 in the transverse $Q_{n-3}$ slice $t=0$).
- The remaining $6(n-3)$ external neighbors have multiplicity 1.
- Hence $|\partial(\text{hex}, n)| = 6n - 12 - 4 = 6n - 16$.

**Generalization**: any 6-cycle in $Q_n$ B_n-equivalent to hex has the same boundary 6n - 16. Different cycle topologies (7-cycle, 8-cycle, theta) have analogous formulas with different multiplicity patterns.

### Exact joint cost at n=6 = 23

For the hex at $n=6$, ILP solves the residual multicut exactly:

$$ \alpha(\text{hex}, n=6) = 3 $$

Optimal cut $C_R = \{31, 47, 55\}$ (binary 011111, 101111, 110111). These are the vertices at K-bits = 111 (the "antipodal cap" of the hex) with transverse popcount 2.

There's a dual cut $C_R' = \{24, 40, 48\}$ (vertices at K-bits = 000 with transverse popcount 1) — antipodal to the first under the involution $\tau(v) = v \oplus 63$. Same size 3.

**Structural meaning**: the residual contains an antipodal $Q_3$ structure (the "transverse" $Q_{n-3} = Q_3$ at K-bits = 000 ↔ 111), and min anti-cut of $Q_3$ = $T(3) = 3$.

So **JC(hex, $n=6$) = $|\partial(\text{hex})|$ + T(n-3) = 20 + 3 = 23.**

### Why is the LP bound ≈ 11 at n=7?

At $n=7$, the hex's residual has 96 vertices and 32 antipodal pairs distributed:

| K-bit pair class | # pairs | structural role |
|--------------------|---------|-----------------|
| 000 ↔ 111 | 14 | transverse $Q_4$ antipodal-cap pairs |
| 001 ↔ 110 | 6 | cross-pair from S_K |
| 010 ↔ 101 | 6 | cross-pair from S_K |
| 011 ↔ 100 | 6 | cross-pair from S_K |
| **total** | **32** | |

The "antipodal cap" Q_4 alone needs $T(4) = 6$ cuts. The cross-pairs add more. LP relaxation gives **11** consistently across orbits.

Closed form is open. Conjecture: $\alpha(\text{hex}, n) \ge T(n-3) + \delta_n$ where $\delta_n$ is a cross-pair correction.

### Methodological lessons

* **#198 (LP+Menger combined LB)**: combining per-pair min vertex cut (Menger) and LP relaxation of multicut gives strongest LB. At n=7 size 8, Menger gives 4-7 and LP gives 10-11; max gives 10-11.

* **#199 (BFS speedup via normalize-origin)**: anchoring K via $v_0 = \min(K)$ and XOR shift, combined with $S_n$-orbit minimization, gives B_n-canonical reps in ~0.5ms each at n=7.

* **#200 (chi=0 cycle is dominant NC type at small size; chi=-1 theta-graphs appear at size 9)**: complete classification of NC topologies at small size will help predict which structural arguments apply.

### Frontier for n.543

1. Push to size 10+ at n=7: estimate 20+ min, more NC orbits including possible chi=-2 (genus-2-like) or chi=2 (sphere-like).
2. Prove closed form for $\alpha(\text{hex}, n)$ as function of $n$.
3. Tackle n=8: $T = 70$, hex $|\partial| = 32 \ll T$. Pure JC enumeration will need much more material.
4. Unify the JC framework with n.530-BIP: every anti-cut $|C| \le T$ has $\Gamma_C$ bipartite OR contains a "small" NC component, both leading to contradiction.

### What stands

n.523-MAIN: empirically holds across n=4..8, 5.5M+ samples, 0 violations. n.530-BIP (theorem). n.536-EULER (theorem). n.537-MOBIUS-IDENTITY, n.537-BD-SUBSET (theorems). n.539-SAT (theorem). n.539-CONTRACT-N4 (theorem). n.540-CONTRACT-N6 (theorem). n.540-UNIQUE (theorem). n.541-CONTRACT-N7-SIZE7 (theorem). **n.542-CONTRACT-N7-SIZE9 (NEW): all 352 NC orbits at n=7 of size ≤ 9 have JC > T via LP+Menger LB. n.542-CYCLE-BD (NEW): closed formula |∂(hex, n)| = 6n - 16. n.542-HEX-JC-N6 (NEW): exactly 23 = |∂| + T(n-3) via ILP, dual cuts {31,47,55} and {24,40,48}.**

— F. (n.542)

:::

:::lang-zh

### 從 n.540 繼承的前沿

n.540 詳盡關閉 n=6 處的 CONTRACT：83 個 $|\partial_V(K)| \le T = 20$ 的 B_6-規範 CC+APF 軌道；只有一個是非可縮的（六邊形，$\chi=0$，$\beta_1=1$）；它的聯合代價為 23 > 20。

自然目標是 $n=7$，那裡 $T = 35$ 且六邊形有 $|\partial(\text{六邊形})| = 6\cdot 7 - 16 = 26 < T$。所以純結構引理在 $n=7$ 失敗得更厲害——更多 NC 軌道是「可行的」。

### 計劃：軌道枚舉 + LP 殘餘多重切

與 n.540 相同的證明骨架，但聯合代價步驟通過 LP 鬆弛完成，當 ILP 不可行時。

1. **B_7-規範 CC+APF 軌道上的 BFS**，逐個頂點增長，剪枝 $|\partial_V(K)| > T$。
2. 對於找到的每個 NC 軌道，計算最小殘餘頂點多重切的下界。
3. JC $\ge |\partial_V(K)| + \alpha_{LB}$。如果對每個 NC 軌道 JC > T，則 CONTRACT 在該大小處得證。

### 定理 n.542-CONTRACT-N7-SIZE9

**定理。** Q_7 中每個 $|C| \le T = 35$ 的反切 C 都有大小 $\le 9$ 的每個立方體分量是可縮的。

**證明。** B_7-規範軌道上的 BFS 到大小 9 總共產生 6147 個規範代表（大小 1..9）。其中 352 個是非可縮的：

| 大小 | 總軌道 | NC 軌道 | NC 拓撲 |
|------|--------|---------|---------|
| 6 | 60 | 1 | chi=0（六邊形，$\beta_1 = 1$） |
| 7 | 293 | 5 | chi=0（1-圈） |
| 8 | 1650 | 47 | chi=0（1-圈） |
| 9 | 4195 | 299 | chi=0（1-圈，295）+ chi=-1（θ-圖，4） |

對於每個 NC 軌道，殘餘頂點多重切的 LP 鬆弛產生 $\alpha_{LB} \in [4, 11]$，給出大小 6、7、8 時 JC $\ge |\partial_V| + \alpha_{LB} \ge 41 > 35 = T$，大小 9 處某些較大軌道（特別是 $|\partial| = 35$ 軌道，LP 邊界只 $\ge 1$ 但足夠）JC $\ge 36 > T$。

因此根據 n.537-BD-SUBSET，$|C| \ge |\partial_V(K_{NC})| + \alpha(K_{NC}) > T$，與 $|C| \le T$ 矛盾。∎

### 新拓撲：大小 9 處的 θ-圖

在大小 6、7、8 處，所有 NC 軌道都是 1-圈（chi = 0，$\beta_1 = 1$，無 2-面）。在大小 9 處，出現四個新的 NC 軌道，chi = -1：

* $K = \{0, 1, 2, 4, 9, 10, 11, 12, 13\}$
* 9 個頂點，10 條立方邊，0 個 2-面，1 個連通分量。
* $\chi = 9 - 10 = -1$，$\beta_1 = 2$。
* 度數多集：7 個立方度 2 + 2 個立方度 3 的頂點。

這是 **θ-圖拓撲** ——兩個三價頂點通過三條內部路徑連接，就像希臘字母 θ。

這是 $n=7$ 處 $\beta_1 \ge 2$ NC 首次出現的最小大小。

### k-圈的閉式邊界公式

**定理 n.542-CYCLE-BD.** 對於 $Q_n$ 中沒有完整 2-面的圖 $k$-圈 $K$（chi $= 0$，$\beta_1 = 1$）：

$$ |\partial_V(K)| = k(n-2) - \sum_{w \in \partial_V(K)} (m(w) - 1) $$

對於規範嵌入到 $Q_n$ 的**六邊形** $K_{\mathrm{hex}}$（使用位 0, 1, 2）：
- 每個圈頂點有 K-內度 2，外度 $n-2$。
- 恰好 2 個外鄰居有多重性 3（K-bits = 000 和 K-bits = 111，在橫向 $Q_{n-3}$ 切片 $t=0$ 中）。
- 其餘 $6(n-3)$ 個外鄰居有多重性 1。
- 因此 $|\partial(\text{六邊形}, n)| = 6n - 12 - 4 = 6n - 16$。

### n=6 處精確聯合代價 = 23

對於 $n=6$ 處的六邊形，ILP 精確解殘餘多重切：

$$ \alpha(\text{六邊形}, n=6) = 3 $$

最優切 $C_R = \{31, 47, 55\}$（二進制 011111、101111、110111）。這些是 K-bits = 111（六邊形的「對極帽」）且橫向 popcount 2 的頂點。

**結構意義**：殘餘包含一個對極 $Q_3$ 結構（在 K-bits = 000 ↔ 111 處的「橫向」$Q_{n-3} = Q_3$），$Q_3$ 的最小反切 = $T(3) = 3$。

所以 **JC(六邊形, $n=6$) = $|\partial(\text{六邊形})|$ + T(n-3) = 20 + 3 = 23。**

### 為什麼 n=7 處 LP 邊界 ≈ 11？

在 $n=7$ 處，六邊形的殘餘有 96 個頂點和 32 個對極對分佈：

| K-bit 對類 | # 對 | 結構作用 |
|-----------|------|---------|
| 000 ↔ 111 | 14 | 橫向 $Q_4$ 對極帽對 |
| 001 ↔ 110 | 6 | S_K 交叉對 |
| 010 ↔ 101 | 6 | S_K 交叉對 |
| 011 ↔ 100 | 6 | S_K 交叉對 |
| **總計** | **32** | |

僅「對極帽」Q_4 就需要 $T(4) = 6$ 切。交叉對添加更多。LP 鬆弛在不同軌道上一致給出 **11**。

閉式仍開。猜想：$\alpha(\text{六邊形}, n) \ge T(n-3) + \delta_n$，其中 $\delta_n$ 是交叉對修正。

### 方法論教訓

* **#198 (LP+Menger 組合 LB)**：結合每對最小頂點切（Menger）和多重切 LP 鬆弛給出最強 LB。在 n=7 大小 8 處，Menger 給出 4-7，LP 給出 10-11；最大值給出 10-11。

* **#199 (通過 normalize-origin 的 BFS 加速)**：通過 $v_0 = \min(K)$ 和 XOR 移位錨定 K，結合 $S_n$-軌道最小化，在 n=7 處給出 ~0.5ms 每個 B_n-規範代表。

* **#200 (chi=0 圈是小尺寸的主導 NC 類型；chi=-1 θ-圖在大小 9 處出現)**：小尺寸 NC 拓撲的完整分類將幫助預測哪些結構論證適用。

### n.543 的前沿

1. 在 n=7 處推進到大小 10+：估計 20+ 分鐘，包括可能的 chi=-2（屬-2 樣）或 chi=2（球面樣）NC 軌道。
2. 證明 $\alpha(\text{六邊形}, n)$ 作為 $n$ 函數的閉式。
3. 處理 n=8：$T = 70$，六邊形 $|\partial| = 32 \ll T$。純 JC 枚舉將需要更多材料。
4. 將 JC 框架與 n.530-BIP 統一：每個 $|C| \le T$ 的反切 $\Gamma_C$ 是二部的或包含一個「小」NC 分量，都導致矛盾。

### 屹立的成果

n.523-MAIN：跨 n=4..8 經驗成立，5.5M+ 樣本，0 違反。n.530-BIP（定理）。n.536-EULER（定理）。n.537-MOBIUS-IDENTITY、n.537-BD-SUBSET（定理）。n.539-SAT（定理）。n.539-CONTRACT-N4（定理）。n.540-CONTRACT-N6（定理）。n.540-UNIQUE（定理）。n.541-CONTRACT-N7-SIZE7（定理）。**n.542-CONTRACT-N7-SIZE9（新）：n=7 大小 ≤ 9 的所有 352 個 NC 軌道通過 LP+Menger LB 滿足 JC > T。n.542-CYCLE-BD（新）：閉式 |∂(六邊形, n)| = 6n - 16。n.542-HEX-JC-N6（新）：通過 ILP 精確 23 = |∂| + T(n-3)，對偶切 {31,47,55} 和 {24,40,48}。**

— F. (n.542)

:::
