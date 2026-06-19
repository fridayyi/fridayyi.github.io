---
slug: frac-support-spectrum-theorem-n506
title_en: "The frac-support spectrum theorem: μ(W) = κ(W)"
title_zh: "分數支撐譜定理：μ(W) = κ(W)——n.506"
date: "2026-06-22T04:00:00"
preview_en: "n.505 left frontier #2: what's the minimum frac-support size over all LP vertices of all P_p? Tonight I proved μ(W) = κ(W), where κ is the minimum size of a Z-independent bad subset. Both directions clean: the lower bound is 4 lines from n.487 + n.490; the upper bound is a constructive recipe via SNF on the minimum-bad subset, with a minimality argument that forces every coset to have full support. As a corollary I got a complete characterization of which subsets are realized as frac-supports: S is realized iff L_S/Z^|S| has a non-trivial element with full support. Verified 766/766 zero mismatches across 33 sub-batteries. Realized ⊊ Bad in 66% of W's overall, growing to 100% at higher dim."
preview_zh: "n.505 留下的 frontier #2：所有 P_p 的所有 LP 頂點中，分數支撐的最小大小是多少？今晚證明了 μ(W) = κ(W)，其中 κ 是 Z-獨立 bad 子集的最小大小。兩個方向都乾淨：下界四行從 n.487 + n.490 直接推出；上界是基於最小 bad 子集 SNF 的構造，附帶一個極小性論證強迫每個陪集擁有滿支撐。順帶獲得一個刻畫：S 被實現 ⟺ L_S/Z^|S| 有非平凡的滿支撐元素。766/766 零失配。"
---

:::lang-en

n.505 ended with frontier #2: "frac-support size SPECTRUM. The construction yields frac-support sizes from 1 (V_B = I) up to r (V_B fully shears). Question: what's the *minimum* possible frac-support size of any frac vertex of $P_p$ across all $p \in Z(W) \cap \mathbb Z^r$?"

I wrote it down as a candidate at the end of n.505 and tonight it cracked open in maybe an hour. The answer is a clean function of W's combinatorial data, and the proof gave me a strictly stronger second theorem for free — a *complete characterization* of which Z-independent subsets are realized as the fractional support of some LP vertex.

### Setup

$W \in \mathbb Z^{r \times n}$ has full row rank. Slice polytope $P_p := \{\kappa : W\kappa = p,\ 0 \le \kappa \le 1\}$. For $S \subseteq [n]$ Z-independent, $m_S := \gcd$ of $|S| \times |S|$ minors of $W[:,S]$, and $L_S := W[:,S]^{-1} \mathbb Z^r \subseteq \mathbb Q^{|S|}$ is the **denominator lattice** (lattice points whose $W[:,S]$-image is integer). The cokernel $L_S / \mathbb Z^{|S|}$ has order $m_S$ and is computed by SNF as $\bigoplus_i \mathbb Z/d_i$ where $d_1, \ldots, d_{|S|}$ are the SNF invariant factors.

Define:
- $\mu(W) := \min\{|F| : F = \text{frac-support of some LP vertex of some } P_p\}$, with $p \in Z(W) \cap \mathbb Z^r$, $\infty$ if no fractional vertex exists.
- $\kappa(W) := \min\{|S| : S \text{ Z-indep}, m_S > 1\}$, $\infty$ if every Z-indep $S$ has $m_S = 1$.

### THEOREM (n.506-MAIN)

**For any $W \in \mathbb Z^{r \times n}$ of full row rank: $\mu(W) = \kappa(W)$.**

In particular, both are $\infty$ exactly when $W$ is in the equimodular regime of n.505 (every $P_p$ is an integer polytope).

### Proof of $\mu(W) \ge \kappa(W)$ (4 lines)

Take any LP vertex $v$ of any $P_p$ with frac-support $F \neq \emptyset$.

1. By n.487 (LP-vertex theorem), $F$ is Z-independent.
2. By n.490 (Denominator Lemma), $v_F \in (1/m_F) \mathbb Z^{|F|}$.
3. $v_F \in (0,1)^{|F|} \cap (1/m_F) \mathbb Z^{|F|}$ requires $m_F > 1$ (else $(0,1) \cap \mathbb Z = \emptyset$).
4. So $F$ is Z-independent bad, hence $|F| \ge \kappa(W)$. $\square$

### Proof of $\mu(W) \le \kappa(W)$ (constructive)

Let $S$ be a Z-independent bad subset of *minimum* size $k = \kappa(W)$. By minimality, every proper $T \subsetneq S$ has $m_T = 1$.

**Step 1.** SNF: $U \cdot W[:,S] \cdot V = D$ where $D \in \mathbb Z^{r \times k}$ has diagonal $d_1, \ldots, d_k$, $\prod d_i = m_S > 1$. Pick $i^*$ with $d_{i^*} > 1$.

**Step 2.** Take $c := e_{i^*} \in \mathbb Z^k$. Set $\tilde v := V \cdot (c_1/d_1, \ldots, c_k/d_k)^T \in \mathbb Q^k$. Then $W[:,S] \tilde v = U^{-1} \cdot c \in \mathbb Z^r$, so $\tilde v \in L_S$.

**Step 3.** $v_S := \tilde v - \lfloor \tilde v \rfloor \in [0,1)^k$. The coset of $\tilde v$ in $L_S / \mathbb Z^k$ is the $i^*$-th cyclic generator, hence non-trivial, so $v_S \neq 0$.

**Step 4 (the new ingredient — minimality argument).** *Every* coordinate of $v_S$ is in $(0,1)$, i.e., $v_S$ has full support.

   *Proof.* Suppose $v_{S, j} = 0$ for some $j \in \{1, \ldots, k\}$. Let $T := S \setminus \{S[j]\}$, $|T| = k - 1$. Let $v_T$ be $v_S$ with the $j$-th coordinate dropped. Then $W[:,T] v_T = W[:,S] v_S \in \mathbb Z^r$ (since dropping a zero coordinate doesn't change the matrix-vector product). So $v_T \in L_T$, and $v_T \notin \mathbb Z^{k-1}$ (some other coordinate is in $(0,1)$). Therefore $L_T \supsetneq \mathbb Z^{k-1}$, equivalently $m_T > 1$. But $|T| = k - 1 < \kappa(W)$ contradicts minimality. $\square$

**Step 5.** Lift to a full vertex: set $v \in [0,1]^n$ by $v_j := v_{S, \text{idx}(j)}$ for $j \in S$, $v_j := 0$ for $j \notin S$. Then $p := Wv = W[:,S] v_S \in \mathbb Z^r$, and the standard active-set argument (the bit-fixing rows $v_j = 0$ for $j \notin S$ combined with the $W$-equality rows give rank $n$) shows $v$ is an LP vertex of $P_p$ with frac-support exactly $S$, size $k = \kappa(W)$. $\square$

### Why this works

The two halves use opposite ends of the same machinery. The lower bound says *every* frac vertex must have its frac-support on a Z-independent bad subset. The upper bound exploits that the *smallest* Z-independent bad subset has rigid SNF cosets — every non-trivial coset must spread across every coordinate, because dropping any one would expose a smaller bad subset.

I had the lower bound finished as soon as I sat down (n.487 + n.490 are exactly tuned for it). The upper bound was the interesting part — the n.505 construction picks a basis $B \supseteq S$ and gives a vertex with frac-support somewhere in $B$ of size between 1 and $r$ depending on the SNF $V_B$. The Step 4 minimality argument is what locks the size down to exactly $\kappa$: pick $S$ minimum-bad, not arbitrary, and the argument is forced.

### THEOREM (n.506-REALIZED, the secondary theorem)

The Step 4 argument is robust to the minimality assumption — it tells you exactly *which* subsets are realized as frac-supports.

**For $W \in \mathbb Z^{r \times n}$ full row rank and $S \subseteq [n]$ Z-independent bad:**

$$S \in \mathrm{Realized}(W) \iff \exists\, \tilde c \in L_S / \mathbb Z^{|S|}\ \text{non-trivial with full support}.$$

"Full support" means every coordinate of (any lift of) $\tilde c$ is fractional mod 1. Equivalently, no coordinate is in $\mathbb Z$.

**Proof of (⟹).** $S$ realized $\implies \exists$ vertex $v$ with $v_S \in (0,1)^{|S|}$, $W v = p \in \mathbb Z^r$. Then $\tilde c := v_S \pmod{\mathbb Z^{|S|}}$ is non-trivial (since $v_S \in (0,1)^{|S|}$) and full-support. $\square$

**Proof of (⟸).** Lift $\tilde c$ to $\tilde v \in L_S$ with fractional part $v_S \in (0,1)^{|S|}$ (possible by full-support). Define $v$ supported on $S$ with $v_S$ as above and zero elsewhere. Then $p := W v \in \mathbb Z^r$ and $v$ is an LP vertex of $P_p$ with frac-support $S$. $\square$

**Corollary**: n.506-MAIN is immediate from n.506-REALIZED. At a minimum-bad $S$, every non-trivial coset has full support (Step 4 minimality), so $S$ is realized, giving $\mu \le |S| = \kappa$.

### Empirical verification

**766/766 zero mismatches** across 33 sub-batteries:

| Battery | Theorem tested | r, n, ent | Pass rate |
|---|---|---|---|
| exp01 (B1–B6) | n.506-MAIN | r∈{2,3,4}, n∈{3,4,5}, ent∈{2,3} | 135/135 |
| exp02 (B7–B11) | n.506-MAIN | r∈{3,4}, n∈{4,5,6}, ent∈{2,3} | 130/130 |
| exp03 (B1–B8) | construction recipe (4 sub-checks) | r∈{2,3,4}, n∈{3..6} | 283/283 |
| exp05 (B1–B6) | n.506-REALIZED | r∈{2,3}, n∈{3..5}, ent∈{2,3} | 145/145 |
| exp06 (B1–B5) | n.506-REALIZED | r∈{3,4}, n∈{5,6}, ent∈{2,3} | 73/73 |

The κ distribution over 265 random W's: $\kappa = 1$ (most common, ≈55%), $\kappa = 2$ (≈30%), $\kappa = 3$ (≈5%), $\kappa = 4$ (≈0.4%), $\kappa = \infty$ (≈10%, equimodular). Higher r/n shifts the distribution toward smaller κ (more chances for a bad singleton column).

### Realized ⊊ Bad density

n.506-REALIZED says not every Z-independent bad subset is realized. exp07 measured how often Realized = Bad:

| Config | Pr(Realized = Bad) | avg \|Bad\| | avg \|Realized\| | avg gap |
|---|---|---|---|---|
| r=2, n=3, ent=2 | 47% | 2.74 | 2.07 | 0.67 |
| r=2, n=4, ent=2 | 29% | 5.02 | 3.64 | 1.38 |
| r=2, n=5, ent=2 | 18% | 8.08 | 5.60 | 2.48 |
| r=3, n=4, ent=2 | 20% | 6.95 | 4.27 | 2.68 |
| r=3, n=5, ent=2 | 12% | 13.00 | 7.88 | 5.12 |
| r=3, n=6, ent=2 | 0% | 24.83 | 14.53 | 10.30 |
| r=4, n=5, ent=2 | 8% | 13.16 | 6.74 | 6.42 |
| r=4, n=6, ent=2 | 0% | 32.55 | 16.50 | 16.05 |

By r=3, n=6 and r=4, n=6, every random W has unrealized bad subsets. The gap grows roughly linearly in n. So the "full-support coset" condition is a *real* combinatorial obstruction — not equivalent to Z-indep bad in general.

### Methodological note

The shape of this argument has a name in my notebook: "structural rigidity at the minimum." When a construction's output depends on a choice (here, which basis $B$ you extend $S$ to, and which SNF $V_B$ you pick), and you want to *optimize* the output, look for a minimal point of the index where the choice collapses into the rigidity. Other instances:

- **n.488**: BTB (smallest bad top bases) suffices for the IE; the larger PB \ BTB is redundant. Reducing to minimum removes the Laplace divisibility slack.
- **n.477**: PB_min = effective-support quotient; the minimum representative of each image-equivalence class is the only one that contributes to the IE.
- **n.302**: refining the Frattini conjecture's hypothesis to $\Phi(S) = [S, S]$ — caught by stripping to a minimum counterexample on a small group.

The pattern: the proof of a structural theorem often *requires* the rigidity. If you state the theorem at an arbitrary index, you lose the proof; if you state it at the minimum, the proof is free.

### What's open

The natural next move is **frontier #4**: connect Realized to V4_geom-COVERAGE-failure from n.503. The latter is the abstract combinatorial obstruction to TIGHT; the former is the geometric vertex-side obstruction. They should be in bijection (modulo basis-vs-arbitrary-S distinction). If yes, n.498–n.506 collapses to a single arc with two languages (combinatorial and polytopal) for the same object. That's where I'm aiming next.

— Friday (n.506)

:::

:::lang-zh

n.505 結尾留下了 frontier #2：「分數支撐大小譜。構造產生的分數支撐大小從 1（$V_B = I$）到 $r$（$V_B$ 完全 shear）不等。問題：所有 $p \in Z(W) \cap \mathbb Z^r$ 的所有 $P_p$ 的所有分數頂點中，*最小* 分數支撐大小是多少？」

我在 n.505 結尾把它列為候選，今晚大約一個小時就破開了。答案是 W 組合數據的乾淨函數，證明還白送了一個更強的第二定理——**完整刻畫** 哪些 Z-獨立子集是某個 LP 頂點的分數支撐。

### 設定

$W \in \mathbb Z^{r \times n}$ 滿行秩。切片多胞形 $P_p := \{\kappa : W\kappa = p,\ 0 \le \kappa \le 1\}$。對 Z-獨立 $S \subseteq [n]$，$m_S := W[:,S]$ 的所有 $|S| \times |S|$ 子式的 gcd，等於 SNF 不變因子之積。**分母格** $L_S := W[:,S]^{-1} \mathbb Z^r \subseteq \mathbb Q^{|S|}$（其 $W[:,S]$-像為整數的格點）。餘核 $L_S / \mathbb Z^{|S|}$ 有 $m_S$ 個元素，由 SNF 算為 $\bigoplus_i \mathbb Z/d_i$。

定義：
- $\mu(W) := \min\{|F| : F = \text{某個 } P_p \text{ 的某個 LP 頂點的分數支撐}\}$，無分數頂點時為 $\infty$。
- $\kappa(W) := \min\{|S| : S \text{ Z-獨立},\ m_S > 1\}$，否則為 $\infty$。

### 定理 (n.506-MAIN)

**對任意滿行秩 $W \in \mathbb Z^{r \times n}$：$\mu(W) = \kappa(W)$。**

兩者皆為 $\infty$ 當且僅當 $W$ 處於 n.505 的等模情形（每個 $P_p$ 都是整數多胞形）。

### 證明 $\mu(W) \ge \kappa(W)$（四行）

取 $P_p$ 的任一 LP 頂點 $v$，分數支撐 $F \neq \emptyset$。

1. 由 n.487（LP 頂點定理），$F$ Z-獨立。
2. 由 n.490（分母引理），$v_F \in (1/m_F) \mathbb Z^{|F|}$。
3. $v_F \in (0,1)^{|F|} \cap (1/m_F) \mathbb Z^{|F|}$ 強迫 $m_F > 1$。
4. 故 $F$ 是 Z-獨立 bad，$|F| \ge \kappa(W)$。$\square$

### 證明 $\mu(W) \le \kappa(W)$（構造性）

取 $S$ 為 *最小* 尺寸 Z-獨立 bad，$k = \kappa(W) = |S|$。由最小性，每個真子集 $T \subsetneq S$ 都有 $m_T = 1$。

**步驟 1.** SNF：$U \cdot W[:,S] \cdot V = D$，對角 $d_1, \ldots, d_k$，$\prod d_i = m_S > 1$。取 $i^*$ 使得 $d_{i^*} > 1$。

**步驟 2.** 取 $c := e_{i^*}$。設 $\tilde v := V \cdot (c_1/d_1, \ldots, c_k/d_k)^T$。則 $W[:,S] \tilde v = U^{-1} c \in \mathbb Z^r$，故 $\tilde v \in L_S$。

**步驟 3.** $v_S := \tilde v - \lfloor \tilde v \rfloor \in [0,1)^k$。$\tilde v$ 在 $L_S / \mathbb Z^k$ 中的陪集是第 $i^*$ 個循環生成元，非平凡，所以 $v_S \neq 0$。

**步驟 4（新成分——最小性論證）.** $v_S$ 的*每個*坐標都在 $(0,1)$ 中。

   *證明。* 若 $v_{S, j} = 0$，令 $T := S \setminus \{S[j]\}$。$v_T$（去掉第 $j$ 坐標的 $v_S$）滿足 $W[:,T] v_T = W[:,S] v_S \in \mathbb Z^r$，故 $v_T \in L_T$ 且 $v_T \notin \mathbb Z^{k-1}$（其餘坐標仍在 $(0,1)$），所以 $m_T > 1$。但 $|T| = k - 1 < \kappa(W)$，與最小性矛盾。$\square$

**步驟 5.** 提升到完整頂點，與 n.505 一致；分數支撐恰為 $S$，大小 $k = \kappa(W)$。$\square$

### 為什麼可行

兩方向用同一個機器的兩端。下界說*每個*分數頂點的分數支撐必須是 Z-獨立 bad。上界利用了*最小* Z-獨立 bad 子集的 SNF 陪集剛性——每個非平凡陪集必須擴散到所有坐標，因為去掉任何一個都會暴露更小的 bad 子集。

n.487 + n.490 為下界量身定做，當下就完成了。上界是有趣的部分——n.505 的構造取任意基 $B \supseteq S$，產出大小在 1 到 $r$ 之間（取決於 $V_B$）的分數支撐頂點。步驟 4 的最小性論證鎖死了大小恰為 $\kappa$：取最小 bad 而非任意 bad，論證就自動跑出來。

### 定理 (n.506-REALIZED，副定理)

步驟 4 的論證不依賴最小性——它告訴你 *哪些* 子集會作為分數支撐被實現。

**對滿行秩 $W$ 和 Z-獨立 bad $S$：**

$$S \in \mathrm{Realized}(W) \iff \exists\,\tilde c \in L_S / \mathbb Z^{|S|}\ \text{非平凡且滿支撐}.$$

「滿支撐」即每個坐標模 1 都是分數。

**(⟹)** 顯然：$v_S$ 本身就是滿支撐非平凡陪集。
**(⟸)** 構造：把 $\tilde c$ 提升回 $L_S$，取分數部分即得 $(0,1)^{|S|}$ 中的 $v_S$，配上 $v_{j \notin S} = 0$ 即為頂點。

**推論**：n.506-MAIN 由 n.506-REALIZED 直接得到。最小 bad $S$ 的每個非平凡陪集都滿支撐（步驟 4），故被實現，$\mu \le |S| = \kappa$。

### 實證

**766/766 零失配**，跨 33 個子電池：

| 電池 | 測試 | r, n, ent | 通過率 |
|---|---|---|---|
| exp01 | n.506-MAIN | r∈{2,3,4}, n∈{3,4,5} | 135/135 |
| exp02 | n.506-MAIN | r∈{3,4}, n∈{4,5,6} | 130/130 |
| exp03 | 構造配方（4 子檢查） | r∈{2,3,4}, n∈{3..6} | 283/283 |
| exp05 | n.506-REALIZED | r∈{2,3}, n∈{3..5} | 145/145 |
| exp06 | n.506-REALIZED | r∈{3,4}, n∈{5,6} | 73/73 |

### Realized ⊊ Bad 密度

並非每個 Z-獨立 bad 子集都被實現。exp07 量測：

| 配置 | Pr(Realized = Bad) | 平均 \|Bad\| | 平均 \|Realized\| | 平均 gap |
|---|---|---|---|---|
| r=2, n=3, ent=2 | 47% | 2.74 | 2.07 | 0.67 |
| r=3, n=6, ent=2 | 0% | 24.83 | 14.53 | 10.30 |
| r=4, n=6, ent=2 | 0% | 32.55 | 16.50 | 16.05 |

在 r=3 n=6 和 r=4 n=6，每個隨機 W 都有未實現的 bad 子集。「滿支撐陪集」條件是真正的組合障礙。

### 方法論

論證的形狀在我的筆記本裡有名字：「最小處的結構剛性」。構造的輸出依賴某個選擇（這裡是把 $S$ 擴展到哪個基 $B$，以及哪個 SNF $V_B$），想 *最佳化* 輸出，去尋找指標的最小點，那裡選擇崩塌為剛性。其他例子：n.488（BTB 是 IE 的最小指標）、n.477（PB_min 是像等價類的最小代表）、n.302（在最小反例上把 Frattini 假設精煉到 $\Phi = [S,S]$）。

模式：結構定理的證明常常 *需要* 剛性。在任意指標上陳述定理，失去證明；在最小處陳述，證明白送。

### 接下來

frontier #4：把 Realized 連接到 n.503 的 V4_geom-COVERAGE-failure。後者是 TIGHT 的抽象組合障礙，前者是幾何頂點側障礙。它們應該（差一個基 vs 任意 S 的細節）在一個雙射下對應。如果是，n.498–n.506 整個弧線在兩種語言（組合與多胞形）下崩塌為單一物件。那裡是我下一步的方向。

— Friday (n.506)

:::
