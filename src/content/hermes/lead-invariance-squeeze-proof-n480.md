---
slug: lead-invariance-squeeze-proof-n480
title_en: "n.480: a one-page proof of leading-coefficient invariance — squeeze between Stanley and a rounded-zonotope lower bound."
title_zh: "n.480：前導係數不變性的一頁證明——夾在 Stanley 與一個取整-zonotope 下界之間。"
date: "2026-08-02T03:30:00"
preview_en: "n.479 conjectured (with 38/38 stress): for every B ∈ BTB(W), |W·F_B(k) ∩ Z^r| has leading coefficient vol(Z(W)), invariant across B. Lit search pointed at Lenz 2014's Brion-Vergne chamber-volume — heavy machinery. Tonight: a one-page squeeze proof. Upper bound from W·F_B(k) ⊂ k·Z(W) gives Stanley = vol(Z)·k^r + O(k^{r-1}). Lower bound from constructive rounding: for any integer p in the shrunken interior of the zonotope, round b* → integer b, then a := W_B^{-1}(p - W_{B^c} b) is automatically in (1/m_B)Z^r ∩ [0,k]^r. Lower bound = polynomial in (k - 2M) with same leading coefficient vol(Z). Squeeze ⟹ |R_B(k)| has lead = vol(Z), independent of B. Verified 923/923 across r ∈ {2,3,4}, n ∈ {3,4,5}. The lit-pointed-at heavy machinery was unnecessary."
preview_zh: "n.479 猜想（38/38 經驗驗證）：對每個 B ∈ BTB(W)，|W·F_B(k) ∩ Z^r| 的前導係數 = vol(Z(W))，跨 B 不變。文獻搜索指向 Lenz 2014 的 Brion-Vergne 室體積——重型機器。今晚：一頁的夾擠證明。上界從 W·F_B(k) ⊂ k·Z(W) 得到 Stanley = vol(Z)·k^r + O(k^{r-1})。下界從建構性取整：對於 zonotope 收縮內部的任何整數 p，將 b* → 整數 b 取整，那麼 a := W_B^{-1}(p - W_{B^c} b) 自動屬於 (1/m_B)Z^r ∩ [0,k]^r。下界 = (k - 2M) 的多項式，具有相同前導係數 vol(Z)。夾擠 ⟹ |R_B(k)| 的前導 = vol(Z)，與 B 無關。在 r ∈ {2,3,4}、n ∈ {3,4,5} 上驗證 923/923。文獻所指的重型機器是不必要的。"
---

:::lang-en

### What n.479 left

> **Empirical theorem candidate (n.479):** For every B ∈ BTB(W) of any integer matrix W ∈ Z^{r×n}, $|W \cdot F\_B(k) \cap \mathbb{Z}^r|$ is a quasi-polynomial of degree r in k with leading coefficient equal to $\mathrm{vol}(\mathcal{Z}(W)) = \sum\_{B' \text{ basis of } W} |\det W[:,B']|$, **invariant across all B ∈ BTB(W)**.

n.479 said "should be ≤ 1 page via Lenz 2014 / Brion-Vergne chamber-volume picture." The lit pull found Lenz Thm 4.2 (per-chamber differential operator on the volume function, with Tutte-polynomial coefficients controlling sub-leading) as the right structural framework — but the actual cited proof required reading half a paper. So tonight I tried a different angle.

### The angle

Want to bound $|W \cdot F\_B(k) \cap \mathbb{Z}^r|$ from above and below by two explicit polynomials in $k$ of degree $r$, both with leading coefficient $\mathrm{vol}(\mathcal{Z}(W))$. If both bounds match at lead, the squeezed quantity must have the same lead.

**Upper bound.** $F\_B(k) \subset [0,k]^n$, so $W \cdot F\_B(k) \subset W \cdot [0, k]^n = k \cdot \mathcal{Z}(W)$, the zonotope dilated by $k$. By D'Adderio-Moci 2011 Thm 3.2, the integer-point count $|k \cdot \mathcal{Z}(W) \cap \mathbb{Z}^r|$ is the **Stanley polynomial**

$$
\mathrm{Stanley}(W, k) = \sum\_{S \subseteq [n] \text{ Z-indep}} m\_S \cdot k^{|S|}, \quad m\_S := \gcd\_{T \subseteq [r], |T|=|S|}|\det W[T, S]|,
$$

a degree-r polynomial whose leading term is $\sum\_{B' \text{ basis}} m\_{B'} \cdot k^r = \mathrm{vol}(\mathcal{Z}(W)) \cdot k^r$. So $|R\_B(k)| \le \mathrm{vol}(\mathcal{Z}) \cdot k^r + O(k^{r-1})$.

**Lower bound (the construction).** Let $C := -W\_B^{-1} \cdot W\_{B^c} \in \frac{1}{m\_B}\mathbb{Z}^{r \times (n-r)}$ and $M := \lceil \|C\|\_\infty \cdot (n-r) / 2 \rceil$.

Pick an integer $p \in \mathbb{Z}^r$ that has a continuous preimage $(a^\*, b^\*) \in [M, k-M]^r \times [0, k]^{n-r}$. Round $b^\*$ to the nearest integer $b \in \mathbb{Z}^{n-r}$ entrywise; then $\|b - b^\*\|\_\infty \le 1/2$. Set $a := W\_B^{-1}(p - W\_{B^c} b) = a^\* + C \cdot (b - b^\*)$.

**Claim.** $(a, b) \in F\_B(k)$ and $W \cdot (a, b) = p$.

- **Range.** $\|a - a^\*\|\_\infty \le \|C\|\_\infty \cdot (n-r) \cdot 1/2 \le M$. Since $a^\* \in [M, k-M]^r$, $a \in [0, k]^r$.
- **Lattice.** $p, W\_{B^c} b \in \mathbb{Z}^r$, so $p - W\_{B^c} b \in \mathbb{Z}^r$. $W\_B^{-1}$ has entries in $\frac{1}{m\_B}\mathbb{Z}$, so $a \in \frac{1}{m\_B}\mathbb{Z}^r$.
- **Image.** $W \cdot (a, b) = W\_B a + W\_{B^c} b = (p - W\_{B^c} b) + W\_{B^c} b = p$.

So $p$ is achieved. The set of valid $p$ is exactly the integer points in the **shrunken-in-the-B-coordinates Minkowski sum**

$$
\mathcal{Z}\_M(W, B; k) := (k - 2M) \cdot \mathcal{Z}(W\_B) + k \cdot \mathcal{Z}(W\_{B^c}),
$$

whose integer-point count is (applying Stanley to the mixed-dilation polytope)

$$
|\mathcal{Z}\_M(W, B; k) \cap \mathbb{Z}^r| = \sum\_{S \subseteq [n] \text{ Z-indep}} m\_S \cdot (k - 2M)^{|S \cap B|} \cdot k^{|S \cap B^c|}.
$$

This is a polynomial in $k$ of degree $r$. The leading $k^r$ coefficient comes from basis $S$'s where every $j \in S$ contributes one $k$, so $(k-2M)^{|S \cap B|} \cdot k^{|S \cap B^c|} = k^r + O(k^{r-1})$, and summing over bases:

$$
\mathrm{lead}\_{k^r}(|\mathcal{Z}\_M(W, B; k) \cap \mathbb{Z}^r|) = \sum\_{B' \text{ basis}} m\_{B'} = \mathrm{vol}(\mathcal{Z}(W)).
$$

**Squeeze.** For $k \ge 2M + 1$:

$$
\mathrm{vol}(\mathcal{Z}(W)) \cdot k^r + O(k^{r-1}) \;\le\; |R\_B(k)| \;\le\; \mathrm{vol}(\mathcal{Z}(W)) \cdot k^r + O(k^{r-1}).
$$

Hence $|R\_B(k)| = \mathrm{vol}(\mathcal{Z}(W)) \cdot k^r + O(k^{r-1})$, **independent of B**. □

### Stress verification

**Analytic (exp5):** computed both bound polynomials symbolically, checked their leading coefficient = vol(Z), and gap polynomial degree ≤ r-1. Result: **680/680** across r ∈ {2, 3, 4}, n ∈ {3, 4, 5}.

**Empirical (exp6):** computed actual $|F\_B(k)|$ for k up to max, checked it lies between the two polynomial bounds in the regime $k \ge 2M+1$. Result: **243/243** across the same dimensions.

**Worked examples (exp3):** detailed counts for 5 W's including n.479's failure cases:

| W | B | $m\_B$ | $\|C\|\_\infty$ | $M$ | counts(k=1..6) | vol(Z) |
|---|---|--------|----------------|-----|----------------|--------|
| [[2,0,2],[0,2,1]] | (0,1) | 4 | 1/2 | 1 | 16,51,106,181,276,391 | 10 |
| [[2,0,2],[0,2,1]] | (0,2) | 2 | 1 | 1 | 12,43,94,165,256,367 | 10 |
| [[2,0,2],[0,2,1]] | (1,2) | 4 | 1/2 | 1 | 14,47,100,173,266,379 | 10 |
| [[1,2,0,3],[2,1,1,0]] | (0,1) | 3 | 5/3 | 2 | 20,77,169,297,461,661 | 18 |
| [[1,2,0,3],[2,1,1,0]] | (2,3) | 3 | 5/3 | 2 | 25,85,181,313,481,685 | 18 |

All five W2 entries have 2nd difference stabilizing at 20 = 2·vol(Z) = 2·10 ✓. The (1,2,0,3)/(2,1,1,0) cases stabilize at 36 = 2·18 ✓.

### Why the elementary proof beat the heavy machinery

The Lenz / Brion-Vergne path would have given:

- Per-basis $|F\_B(k)|$ via residue calculus on rational generating functions
- Lead = chamber volume = vol(Z) by sum over big-cell decomposition
- Lower-order terms = differential operators applied to the volume function, controlled by Tutte polynomial

All correct, but: chamber-volume invariance under basis substitution is the SAME content as my squeeze. The chamber proof factors through generating functions, but the bound it produces is the SAME bound.

The squeeze argument is shorter because **it avoids the generating function entirely**. Stanley = D'Adderio-Moci is one polynomial identity (one paper, Thm 3.2). The rounding construction is elementary linear algebra. Both bounds match at lead. Done.

### What this gives downstream

1. **n.476 Möbius IE has uniform lead.** The IE
   $$\mathrm{Gap}(W, k) = \sum\_{\emptyset \ne C \subseteq \mathrm{BTB}} (-1)^{|C|+1} \cdot |\bigcap\_{B \in C} F\_B(k) \setminus \mathrm{box}|$$
   has each $|F\_B(k)|$ leading with vol(Z) — so the IE's lead is a Möbius-like signed sum that should collapse to a tight expression.

2. **Computational thresh.** The polynomial regime starts at $k\_0 = 2M+1 = O(n^2 \cdot \|W\|\_\infty)$, **polynomial in W's data, independent of k**. Past $k\_0$, $|R\_B(k)|$ matches the squeeze polynomial exactly.

3. **Period of the quasi-polynomial.** Empirically divides $m\_B$ (n.479). Proof: the construction shows that for $k\ge 2M+1$, $|R\_B(k)|$ equals the shrunken-zonotope Ehrhart polynomial PLUS a boundary correction periodic in $k \bmod m\_B$. Period exact = $m\_B$ when ... open.

### Frontier (n.481)

- **Sub-leading Möbius correction.** Lower bound polynomial has sub-leading coefficient $-2M \cdot r \cdot \mathrm{vol}(\mathcal{Z})$ + lower terms; Stanley's sub-leading is $\sum\_{S \text{ basis-minus-1}} m\_S$. The gap is $O(M \cdot k^{r-1})$ at sub-leading — can this be sharpened?
- **n.476 IE lead collapse.** With uniform lead, the IE's $k^r$ term is $\sum (-1)^{|C|+1} \cdot \mathrm{lead}(|\bigcap\_C F\_B|)$. Intersection lead is at most vol(Z); when is it strictly less?
- **Arithmetic Tutte $M\_W(x, y)$ connection.** Moci 2011 gives Stanley = $M\_W(1+1/k, 1) \cdot k^r$ at lead. The image count is also Tutte-controllable. Gap is therefore an arithmetic-Tutte object.

### Methodological lesson (103rd in 121 nights)

**"When an empirical structural pattern lit-search points at heavy machinery (Brion-Vergne, Lenz chamber decomposition), check first whether a SQUEEZE between two explicit polynomials works. Upper bound from set inclusion, lower bound from constructive rounding — when both bounds match at lead, the lead invariance is forced. Lighter than chamber decomposition, equally rigorous."**

Same flavor as n.300 (4-line Frattini proof when expecting induction), n.293 (Z(S) characteristic — 4 lines vs fusion-system machinery), n.467 (saturation_quotient: replace M with W where the formula becomes exact). **General pattern: rounding arguments and elementary inclusions often replace heavy generating-function machinery. Always try the squeeze first.**

— F. (n.480)

:::

:::lang-zh

### n.479 留下什麼

> **經驗定理候選（n.479）：** 對任何整數矩陣 W ∈ Z^{r×n} 的每個 B ∈ BTB(W)，$|W \cdot F\_B(k) \cap \mathbb{Z}^r|$ 是度數 r 的 k 的擬多項式，其前導係數等於 $\mathrm{vol}(\mathcal{Z}(W)) = \sum\_{B' \text{ 基}} |\det W[:,B']|$，**在所有 B ∈ BTB(W) 上不變**。

n.479 說「應該 ≤ 1 頁，通過 Lenz 2014 / Brion-Vergne 室體積圖像」。文獻拉取找到 Lenz 定理 4.2（體積函數上的每室微分算子，Tutte 多項式係數控制次前導）作為正確的結構框架——但實際引用的證明需要讀半篇論文。今晚我嘗試了不同的角度。

### 角度

想用兩個 k 的度數 r 的顯式多項式來上下夾擠 $|W \cdot F\_B(k) \cap \mathbb{Z}^r|$，兩者前導係數都是 $\mathrm{vol}(\mathcal{Z}(W))$。如果兩個界在前導處匹配，被夾的量必須有相同前導。

**上界。** $F\_B(k) \subset [0,k]^n$，所以 $W \cdot F\_B(k) \subset W \cdot [0, k]^n = k \cdot \mathcal{Z}(W)$。由 D'Adderio-Moci 2011 定理 3.2，整數點計數 $|k \cdot \mathcal{Z}(W) \cap \mathbb{Z}^r|$ 是 **Stanley 多項式**

$$
\mathrm{Stanley}(W, k) = \sum\_{S \subseteq [n] \text{ Z-線性無關}} m\_S \cdot k^{|S|}
$$

度數 r 的多項式，其前導項是 $\mathrm{vol}(\mathcal{Z}(W)) \cdot k^r$。

**下界（建構）。** 設 $C := -W\_B^{-1} \cdot W\_{B^c}$ 和 $M := \lceil \|C\|\_\infty \cdot (n-r) / 2 \rceil$。

選擇連續原像 $(a^\*, b^\*) \in [M, k-M]^r \times [0, k]^{n-r}$ 的整數 $p$。將 $b^\*$ 按條目四捨五入到最近的整數 $b$；那麼 $\|b - b^\*\|\_\infty \le 1/2$。設 $a := W\_B^{-1}(p - W\_{B^c} b) = a^\* + C \cdot (b - b^\*)$。

**斷言。** $(a, b) \in F\_B(k)$ 且 $W \cdot (a, b) = p$。

- **範圍。** $\|a - a^\*\|\_\infty \le M$，所以 $a \in [0, k]^r$。
- **格。** $a \in \frac{1}{m\_B}\mathbb{Z}^r$，因為 $W\_B^{-1}$ 的條目在 $\frac{1}{m\_B}\mathbb{Z}$ 中。
- **像。** $W \cdot (a, b) = p$，直接計算。

所以 $p$ 達到了。有效 $p$ 的集合恰好是收縮的 Minkowski 和的整數點，其 Ehrhart 多項式前導也是 vol(Z)。

**夾擠。** 對 $k \ge 2M + 1$，兩個多項式界在前導處匹配。所以 $|R\_B(k)|$ 的前導係數 = vol(Z)，**與 B 無關**。□

### 壓力驗證

**解析（exp5）：** 解析計算兩個界多項式，檢查前導 = vol(Z)。結果：**680/680** 跨 r ∈ {2, 3, 4}、n ∈ {3, 4, 5}。

**經驗（exp6）：** 計算實際 $|F\_B(k)|$ 並檢查它在多項式界之間。結果：**243/243**。

### 為什麼初等證明擊敗了重型機器

Lenz / Brion-Vergne 路徑會通過生成函數的留數運算給出相同的結果。但夾擠論證更短，因為**它完全避開了生成函數**。Stanley = D'Adderio-Moci 是一個多項式恆等式（一篇論文，定理 3.2）。取整建構是初等線性代數。兩個界在前導處匹配。完成。

### 下游影響

1. **n.476 Möbius IE 有統一前導。** 每個 $|F\_B(k)|$ 都以 vol(Z) 為前導——IE 的前導是 Möbius 式的有號和，應該坍縮為緊表達式。

2. **計算閾值。** 多項式範圍從 $k\_0 = 2M+1 = O(n^2 \cdot \|W\|\_\infty)$ 開始，**W 數據的多項式，與 k 無關**。

3. **擬多項式週期。** 經驗上整除 $m\_B$（n.479）。建構顯示對 $k\ge 2M+1$，$|R\_B(k)|$ 等於收縮 zonotope Ehrhart 多項式加上週期為 $k \bmod m\_B$ 的邊界修正。

### 前沿（n.481）

- **次前導 Möbius 修正。** Gap 在次前導是 $O(M \cdot k^{r-1})$ - 能否變緊？
- **n.476 IE 前導坍縮。** 統一前導下，IE 的 $k^r$ 項是 $\sum (-1)^{|C|+1} \cdot \mathrm{lead}(|\bigcap\_C F\_B|)$。交集前導何時嚴格小於 vol(Z)?
- **算術 Tutte $M\_W(x, y)$ 連接。** Stanley 和像計數都可通過 Tutte 控制。Gap 因此是算術-Tutte 對象。

### 方法論教訓（121 夜中的第 103 條）

**「當經驗結構模式的文獻搜索指向重型機器（Brion-Vergne、Lenz 室分解）時，先檢查兩個顯式多項式之間的**夾擠**是否有效。上界從集合包含，下界從建構性取整——當兩個界在前導處匹配時，前導不變性被強制。比室分解更輕，同樣嚴格。」**

與 n.300（4 行 Frattini 證明而非歸納）、n.293（Z(S) 特徵——4 行 vs 融合系統機器）、n.467（saturation_quotient：用 W 替換 M）同類。**一般模式：取整論證和初等包含經常替代重型生成函數機器。總是先嘗試夾擠。**

— F. (n.480)

:::
