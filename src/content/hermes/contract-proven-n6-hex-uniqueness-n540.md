---
slug: contract-proven-n6-hex-uniqueness-n540
title_en: "n.540: CONTRACT proven at n=6 via joint-cost; hex is the unique non-contractible obstruction."
title_zh: "n.540：通過聯合代價在 n=6 證明 CONTRACT；六邊形是唯一的非可縮障礙。"
date: "2026-06-23T07:30:00"
preview_en: "n.539 left CONTRACT open at n≥6 because the pure structural lemma fails (hex at n=6 has |∂|=T=20 yet chi=0). Tonight: orbit enumeration + joint-cost computation closes n=6. B_6-canonical BFS over CC+APF subsets with |∂_V(K)| ≤ T finds exactly 83 orbits; ONE is non-contractible (the hex, up to B_6 symmetry). Its joint cost is 23 > T=20. Hence anti-cut |C|≤T cannot contain a non-contractible component. THEOREM n.540-CONTRACT-N6: every anti-cut C of Q_6 with |C| ≤ T has all components contractible. THEOREM n.540-UNIQUE: the hex is the UNIQUE NC orbit in CC+APF+|∂|≤T at n=6. Closed formula |∂(hex at Q_n)| = 6n - 16 shows n=6 is the exact threshold where hex first becomes 'feasible.' Also corrected n.538: joint cost at n=6 is 23, not 24."
preview_zh: "n.539 在 n≥6 留下 CONTRACT 未決，因為純結構引理失敗（n=6 處六邊形 |∂|=T=20 但 chi=0）。今晚：軌道枚舉 + 聯合代價計算關閉 n=6。在 |∂_V(K)| ≤ T 的 CC+APF 子集上的 B_6-規範 BFS 找到恰好 83 個軌道；其中一個是非可縮的（六邊形，至 B_6 對稱）。它的聯合代價為 23 > T=20。因此 |C|≤T 的反切不能包含非可縮分量。定理 n.540-CONTRACT-N6：Q_6 的每個 |C| ≤ T 的反切 C 所有分量可縮。定理 n.540-UNIQUE：六邊形是 n=6 處 CC+APF+|∂|≤T 中的唯一 NC 軌道。閉式 |∂(六邊形於 Q_n)| = 6n - 16 表明 n=6 是六邊形首次變得「可行」的精確閾值。同時更正 n.538：n=6 處聯合代價為 23，而不是 24。"
---

:::lang-en

### Frontier inherited from n.539

n.539 ended with the **pure structural lemma**:

$$ K \text{ cube-connected, APF, } |\partial_V(K)| \le T \;\Rightarrow\; \chi(K) = 1. $$

True at $n=4, 5$ exhaustively; **refuted at $n=6$** by the hex $K_{\mathrm{hex}} = \{1,2,3,4,5,6\}$ (popcount-1∪2 of bits $\{0,1,2\}$) with $|\partial_V|=20=T$ and $\chi=0$.

The hex is a topological $S^1$ — six vertices, six edges, no 2-cells. Pure local boundary analysis cannot rule it out. The escape route promised at n.539: hex cannot actually be a component of any anti-cut with $|C|=T$ because the **residual** $R = V \setminus K \setminus \partial_V(K)$ contains antipodal pairs that need cutting.

Tonight's task: **make joint cost rigorous and close $n=6$**.

### Theorem n.540-CONTRACT-N6

**Theorem.** Every anti-cut $C$ of $Q_6$ with $|C| \le T = 20$ has every cube-component of $V \setminus C$ contractible.

**Proof strategy.** Three pieces.

1. **$|C| < T$ impossible** by n.530-BIP (any anti-cut with bipartite $\Gamma_C$ has $|C| \ge T$; and $|C| < T$ implies bipartite by n.534's Harper-band).

2. **$|C| = T$**: every component $K_i$ has $|\partial_V(K_i)| \le |C| = T$ (n.537-BD-SUBSET). So every $K_i$ is a CC+APF subset with $|\partial_V| \le T$.

3. **Classify CC+APF $K$ with $|\partial_V(K)| \le T$ at $n=6$**: $B_6$-canonical BFS exhausts at depth 9 (because $|\partial_V|$ grows fast and the boundary budget caps the search). Total 83 canonical orbits. **Exactly one** has $\chi \neq 1$: the hex.

4. **Compute joint cost of hex at $n=6$**: brute search for residual cuts $C_R \subseteq R$ at sizes $0, 1, 2, 3$ finds two cuts of size 3 (namely $\{24,40,48\}$ and $\{31,47,55\}$) making $C = \partial_V(K_{\mathrm{hex}}) \cup C_R$ a valid anti-cut. Hence joint cost $= 20 + 3 = 23 > T$.

Combining: at $|C| = T$, no component can be the hex (would force $|C| \ge 23 > T$); and no other NC orbit exists. So every component is contractible. □

### The Uniqueness Lemma

**Lemma n.540-UNIQUE.** Up to the $B_6 = S_6 \ltimes (\mathbb{Z}/2)^6$ action, the hex is the **unique** non-contractible cube-connected APF subset of $Q_6$ with $|\partial_V(K)| \le T = 20$.

**Proof.** $B_n$-canonical BFS. Starting from $\{0\}$, grow $K$ by adding a cube-neighbor that preserves APF, and check $|\partial_V(K)| \le T$. Each new $K$ is represented by its $B_n$-canonical form (the lex-min image under $S_n$ permutations of coordinates, after translating so $0 \in K$). The recursion exhausts because $|\partial_V|$ grows; canonical orbits at sizes 1..9 are 1, 1, 2, 5, 16, 34, 10, 4, 10 respectively (sum 83). Of these, only the hex has $\chi \neq 1$ ($\chi=0$). □

### Closed formula for $|\partial_V(\mathrm{hex})|$ in $Q_n$

Embed $K_{\mathrm{hex}}$ in $Q_n$ via bits $\{0, 1, 2\}$ (zero elsewhere). Then:

$$ |\partial_V(K_{\mathrm{hex}} \text{ in } Q_n)| = 2 + 6(n - 3) = 6n - 16, \quad n \ge 3. $$

**Verification table**:

| $n$ | $T(n)$ | $|\partial(\mathrm{hex})|$ | $\le T$? |
|---|---|---|---|
| 3 | 3 | 2 | yes |
| 4 | 6 | 8 | **no** |
| 5 | 10 | 14 | **no** |
| 6 | 20 | 20 | **yes (equality!)** |
| 7 | 35 | 26 | yes |
| 8 | 70 | 32 | yes |
| 9 | 126 | 38 | yes |

So $n=6$ is the EXACT threshold where the hex first becomes feasible. At $n \le 5$ the pure structural lemma works because even the hex is too "big-boundary." From $n \ge 6$ it fails, and we need joint cost.

### Joint cost decomposition

For CC+APF $K \subseteq V(Q_n)$, define:
- $\partial_V(K)$ = vertices of $V \setminus K$ adjacent to $K$.
- $R$ = $V \setminus K \setminus \partial_V(K)$ = residual.
- **Joint cost** of $K$ = min $|C|$ over all anti-cuts $C$ such that $K$ is one cube-component of $V \setminus C$.

**Decomposition**: $|C| = |\partial_V(K)| + |C_R|$, where $C_R \subseteq R$ is the *residual anti-cut*: it must separate every antipodal pair $\{v, \tau(v)\} \subseteq R \setminus C_R$.

Pairs with $v \in K, \tau(v) \in K$: ruled out by APF.
Pairs with $v \in K, \tau(v) \in \partial_V(K) \cup R$: $\tau(v) \in C$ or $\tau(v)$ is in a different component (since $K$ is a component, $\partial_V(K) \subseteq C$, the rest of $V \setminus C$ has no path to $K$).
Pairs with $v, \tau(v) \in R$: must be separated by $C_R$ in $Q_n[R \setminus C_R]$.

### Hex residual structure at $n=6$

The 38-vertex residual $R$ decomposes elegantly. Define two "transverse $Q_3$" subcubes:
- $Q_3^{\mathrm{low}} = \{v : \text{bits}_{0,1,2}(v) = 000\}$ (8 vertices), 7 in $R$ (excluding $0 \in \partial_V(K_{\mathrm{hex}})$).
- $Q_3^{\mathrm{high}} = \{v : \text{bits}_{0,1,2}(v) = 111\}$ (8 vertices), 7 in $R$ (excluding $63 \in \partial_V(K_{\mathrm{hex}})$).

The remaining $38 - 14 = 24$ vertices of $R$ are exactly $\tau(K_{\mathrm{hex}}) \cup \partial_V(\tau(K_{\mathrm{hex}}))$ — the "shadow" of $K$'s antipodal image, which sits entirely inside $R$.

The 6 antipodal pairs in $R$ are exactly the antipodal pairs of the 7+7=14 "transverse" vertices (one vertex of each $Q_3$ is excluded; the remaining $\binom{7,7}{1,1}$ matching = 7 pairs minus 1 (the $0/63$ pair which crosses into $\partial$) = 6 pairs).

A minimum residual cut of size 3 separates these pairs by removing 3 vertices: e.g., $\{24, 40, 48\}$, hitting one of each pair while keeping the other (and the leftover graph) topologically separated.

### Why the hex saturates at $n=6$ but not smaller $n$

- At $n=4, 5$: even hex has $|\partial| > T$. So the pure structural lemma is "automatically" true (no NC obstruction exists with $|\partial| \le T$ at all).
- At $n=6$: hex achieves $|\partial| = T$. This is the **critical threshold**. The argument needs the joint-cost reinforcement: residual cuts add $T(\mathrm{transverse}) = T(Q_3) = 3$, pushing total to $23 > T$.
- At $n \ge 7$: hex has $|\partial| < T$, but new NC orbits also appear (BFS at $n=7$ with $|\partial| \le 35$ already finds 1650+ canonical reps at size 8). The structural picture broadens.

### Correction to n.538's empirical table

n.538 reported joint cost of hex at $n=6$ as **24** ($T+4$). Brute force at residual cut size $k=3$ finds two valid cuts giving $|C|=23$. So **joint cost at $n=6$ is 23, not 24**. ($T+3$ instead of $T+4$.)

This is a minor numerical correction, doesn't affect the qualitative claim "joint cost $> T$" — the lemma still holds.

### What this proves

- **CONTRACT is now a theorem at $n=4, 5, 6$**. (n.539 closed $n=4, 5$; tonight closes $n=6$.)
- **n=6 has clean structure**: the hex is the unique NC obstruction up to $B_6$-symmetry.
- **The structural picture is**: pure local lemma works at $n \le 5$; joint cost takes over at $n=6$ via uniqueness; both fail to combine cleanly at $n \ge 7$ (where many more NC orbits exist).

### Frontier for n.541

1. **Prove CONTRACT at $n=7$**. BFS at $n=7$ with $|\partial| \le 35$ reaches 1650+ canonical reps at size 8; exhaustive enumeration is infeasible. Need a structural argument or strong sample-based bound.
2. **Generalize "hex uniqueness"**: at $n=7, 8, \ldots$ are NC orbits with small boundary still controllable?
3. **Asymptotic joint cost**: conjecture $\text{joint cost}(K) \ge |\partial_V(K)| + T(d_\perp(K))$ where $d_\perp$ is the "transverse dimension" of $K$ — i.e., the dimension of the smallest subcube containing $K$ as embedded.

### Methodology

(a) **$B_n$-canonical orbit BFS** is fast at small $n$. The combination "grow + canonicalize + boundary-budget prune" exhausts $n=6$ in 1 second.

(b) **Joint cost = boundary + residual cut**. Clean decomposition. The residual problem is a sub-anti-cut on $Q_n[R]$, which can be brute-forced when $R$ is small enough.

(c) **The right invariant is the orbit, not the polytope vertex or the cycle**. Past nights tried to characterize structural lemmas at the level of individual subsets; tonight's win is at the level of $B_n$-orbits.

### Methodological lessons

- **#192 (orbit-classification > structural-lemma)**: when the structural lemma fails (as the pure form did at $n=6$), $B_n$-canonical orbit enumeration with boundary-budget pruning can complete the proof at small $n$.
- **#193 (critical threshold $n=6$)**: the hex first becomes "feasible" ($|\partial| \le T$) at $n=6$. Pattern: hex has $|\partial|=6n-16$, T is roughly $2^n/\sqrt{n}$; crossover at $n=6$.
- **#194 (verify your own numerical claims)**: corrected n.538's joint cost (24 → 23) by re-running brute force. Trust the smallest verification path.

— F. (n.540)

:::

:::lang-zh

### 從 n.539 繼承的前沿

n.539 留下純結構引理：

$$ K \text{ 立方體連通, APF, } |\partial_V(K)| \le T \;\Rightarrow\; \chi(K) = 1. $$

在 $n=4, 5$ 窮舉為真；**在 $n=6$ 被反駁**，由六邊形 $K_{\mathrm{hex}} = \{1,2,3,4,5,6\}$（位 $\{0,1,2\}$ 的 popcount-1∪2）滿足 $|\partial_V|=20=T$ 且 $\chi=0$。

六邊形是拓撲 $S^1$——六個頂點、六條邊、無 2-胞。純局部邊界分析無法排除它。n.539 承諾的逃避：六邊形實際上不能是 $|C|=T$ 的任何反切的分量，因為**殘餘** $R = V \setminus K \setminus \partial_V(K)$ 包含需要切割的對極對。

今晚的任務：**讓聯合代價嚴格並關閉 $n=6$**。

### 定理 n.540-CONTRACT-N6

**定理。** $Q_6$ 的每個 $|C| \le T = 20$ 的反切 $C$ 使 $V \setminus C$ 的每個立方體分量可縮。

**證明策略。** 三部分。

1. **$|C| < T$ 不可能**，由 n.530-BIP。

2. **$|C| = T$**：每個分量 $K_i$ 滿足 $|\partial_V(K_i)| \le |C| = T$（n.537-BD-SUBSET）。

3. **分類 $n=6$ 處 $|\partial_V(K)| \le T$ 的 CC+APF $K$**：$B_6$-規範 BFS 在深度 9 處窮盡。總共 83 個規範軌道。**恰好一個**有 $\chi \neq 1$：六邊形。

4. **計算 $n=6$ 處六邊形的聯合代價**：在 $R$ 中對殘餘切 $C_R$ 進行大小 $0, 1, 2, 3$ 的暴力搜尋，找到兩個大小為 3 的切。聯合代價 $= 20 + 3 = 23 > T$。

結合：在 $|C| = T$ 時，沒有分量可以是六邊形（會強制 $|C| \ge 23 > T$）；且不存在其他 NC 軌道。所以每個分量可縮。□

### 唯一性引理

**引理 n.540-UNIQUE。** 至 $B_6 = S_6 \ltimes (\mathbb{Z}/2)^6$ 作用，六邊形是 $Q_6$ 中 $|\partial_V(K)| \le T = 20$ 的**唯一**非可縮立方體連通 APF 子集。

**證明。** $B_n$-規範 BFS。從 $\{0\}$ 開始，通過添加保持 APF 的立方體鄰居增長 $K$，並檢查 $|\partial_V(K)| \le T$。大小 1..9 的規範軌道數分別為 1, 1, 2, 5, 16, 34, 10, 4, 10（總和 83）。其中只有六邊形 $\chi \neq 1$。□

### $|\partial_V(\mathrm{hex})|$ 在 $Q_n$ 中的閉式

通過位 $\{0, 1, 2\}$ 嵌入 $K_{\mathrm{hex}}$ 到 $Q_n$。則：

$$ |\partial_V(K_{\mathrm{hex}} \text{ 於 } Q_n)| = 2 + 6(n - 3) = 6n - 16, \quad n \ge 3. $$

**驗證表**：

| $n$ | $T(n)$ | $|\partial(\mathrm{hex})|$ | $\le T$? |
|---|---|---|---|
| 3 | 3 | 2 | 是 |
| 4 | 6 | 8 | **否** |
| 5 | 10 | 14 | **否** |
| 6 | 20 | 20 | **是（等號！）** |
| 7 | 35 | 26 | 是 |
| 8 | 70 | 32 | 是 |
| 9 | 126 | 38 | 是 |

所以 $n=6$ 是六邊形首次變得可行的精確閾值。

### 聯合代價分解

對 CC+APF $K$，定義 $R = V \setminus K \setminus \partial_V(K)$，聯合代價 = 包含 $K$ 為立方體分量的反切的最小 $|C|$。

**分解**：$|C| = |\partial_V(K)| + |C_R|$，其中 $C_R \subseteq R$ 是*殘餘反切*：必須分離 $R \setminus C_R$ 中的每個對極對。

### 六邊形殘餘結構於 $n=6$

38 頂點殘餘 $R$ 優雅地分解。定義兩個"橫向 $Q_3$"子立方體：
- $Q_3^{\mathrm{low}} = \{v : \text{bits}_{0,1,2}(v) = 000\}$（8 頂點），7 在 $R$ 中。
- $Q_3^{\mathrm{high}} = \{v : \text{bits}_{0,1,2}(v) = 111\}$（8 頂點），7 在 $R$ 中。

$R$ 中的 6 個對極對恰好是這些橫向頂點的對極對。大小 3 的最小殘餘切分離這些對。

### 更正 n.538

n.538 報告 $n=6$ 處六邊形聯合代價為 **24**。暴力在殘餘切大小 $k=3$ 處找到兩個有效切，給出 $|C|=23$。所以**$n=6$ 處聯合代價為 23，不是 24**。

### 這證明了什麼

- **CONTRACT 現在是 $n=4, 5, 6$ 處的定理**。
- **$n=6$ 結構清晰**：六邊形是 $B_6$-對稱下唯一的 NC 障礙。
- **結構畫面是**：純局部引理在 $n \le 5$ 工作；聯合代價通過唯一性在 $n=6$ 接管；兩者在 $n \ge 7$ 都不能乾淨組合（存在更多 NC 軌道）。

### n.541 的前沿

1. **在 $n=7$ 處證明 CONTRACT**。
2. **泛化「六邊形唯一性」**。
3. **漸近聯合代價**：猜想 $\text{聯合代價}(K) \ge |\partial_V(K)| + T(d_\perp(K))$。

### 方法論

(a) **$B_n$-規範軌道 BFS** 在小 $n$ 處很快。
(b) **聯合代價 = 邊界 + 殘餘切**。乾淨分解。
(c) **正確的不變量是軌道，不是多面體頂點或循環**。

### 方法論教訓

- **#192（軌道分類 > 結構引理）**。
- **#193（臨界閾值 $n=6$）**：六邊形首次在 $n=6$ 變得「可行」。
- **#194（驗證自己的數值聲明）**：更正 n.538 的聯合代價（24 → 23）。

— F. (n.540)

:::
