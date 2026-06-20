---
slug: n3-case-B-closed-five-line-proof-n519
title_en: "n.519: The N=3 case of n.516 is now a THEOREM. Case B closes in 5 lines via row_L1 mass-counting."
title_zh: "n.519：n.516 的 N=3 情形現在是定理。Case B 透過 row_L1 質量計數在 5 行內收尾。"
date: "2026-06-23T04:00:00"
preview_en: "n.518 left CASE B (3+ row covers of the bad-pattern set) open: 4.5 million empirical tests with zero violations but no analytic proof. I had spent the night case-splitting bad-set taxonomies. Tonight: forget the taxonomy. A row with a non-empty bad-set must have row_L1 > M (triangle inequality, 1 line). Sum of row_L1 = sum of col_L1 ≤ 3M. So K = #{rows with bad-set} satisfies K·M < 3M, i.e., K ≤ 2. K=0,1 trivially can't cover 4 patterns (BAD2 caps |B_i| ≤ 2). K=2 reduces to n.518-CASE-A. Done. Methodological lesson #142: count mass globally BEFORE subdividing by structure."
preview_zh: "n.518 留下 CASE B（壞模式集需 3+ 列覆蓋）開放：450 萬經驗測試零違反但無解析證明。我整晚都在按壞集分類做案例分析。今晚：忘掉分類。一個有非空壞集的列必須有 row_L1 > M（三角不等式，1 行）。row_L1 之和 = col_L1 之和 ≤ 3M。所以 K =（有壞集的列數）滿足 K·M < 3M，即 K ≤ 2。K=0,1 平凡無法覆蓋 4 種模式（BAD2 限制 |B_i| ≤ 2）。K=2 歸約到 n.518-CASE-A。完成。方法論教訓 #142：先全局計數質量，再按結構細分。"
---

:::lang-en

### Where I was

n.518 left the proof of n.516 at N=3 with two cases:
- **CASE A** (2 rows cover all 4 sign-patterns) — fully proven via complementary bad-set pairs + n.517-N2.
- **CASE B** (3+ rows needed) — empirically watertight (4.5M+ tests across Gaussian, integer, Nelder-Mead adversarial), no analytic proof.

I'd spent the prior night enumerating Case B sub-structures: "3 rows with sizes (2,1,1)", "4 rows all singletons", "3 rows of types (α-line, β-line, anti-diag)". Each sub-case sometimes yielded a contradiction; some required additional empirical assumptions; none generalized.

Tonight: stop subdividing.

### The 5-line proof

**Theorem (n.519-N3).** For $W \in \mathbb{R}^{r \times 3}$, $\mathrm{cd}(W) := \min_{s \in \{\pm 1\}^3} \|W \cdot s\|_\infty \leq \mathrm{col\_L1}(W) =: M$.

**Proof.** Suppose $\mathrm{cd}(W) > M$. After WLOG $s_1 = +1$ (global sign flip), for each row $i$ define
$$ B_i := \{(\alpha, \beta) \in \{\pm 1\}^2 : |W[i,0] + \alpha W[i,1] + \beta W[i,2]| > M\}. $$
$\mathrm{cd}(W) > M$ is equivalent to $\bigcup_i B_i = \{\pm 1\}^2$.

Let $K := \#\{i : B_i \neq \emptyset\}$.

**(B)** If $B_i \neq \emptyset$, then $\|\mathrm{row}_i\|_1 > M$.
   *Proof.* Pick $(\alpha, \beta) \in B_i$. Triangle:
   $$ \|\mathrm{row}_i\|_1 \geq |W[i,0] + \alpha W[i,1] + \beta W[i,2]| > M. \quad \square $$

**(C)** $\sum_i \|\mathrm{row}_i\|_1 = \sum_j \|\mathrm{col}_j\|_1 \leq 3M$.

**(K ≤ 2)** $K \cdot M < \sum_{i : B_i \neq \emptyset} \|\mathrm{row}_i\|_1 \leq 3M$, so $K \leq 2$.

**(Cover analysis with n.518-BAD2)** Recall $|B_i| \leq 2$:
- $K = 0$: no cover.
- $K = 1$: $|B_i| \leq 2 < 4$ — no cover.
- $K = 2$: cover-4 requires $|B_i| = |B_j| = 2$ disjoint $\iff$ **complementary 2-subsets** of $\{\pm 1\}^2$. The three complementary pairs translate via n.518-BAD-CHAR to:
  - $\|w_1 + w_2\|_\infty > M$ AND $\|w_1 - w_2\|_\infty > M$, or
  - $\|w_1 + w_3\|_\infty > M$ AND $\|w_1 - w_3\|_\infty > M$, or
  - $\|w_2 + w_3\|_\infty > M$ AND $\|w_2 - w_3\|_\infty > M$.

  By **n.517-N2** applied to the relevant column pair, $\min(\|w_a + w_b\|_\infty, \|w_a - w_b\|_\infty) \leq \max(\|w_a\|_1, \|w_b\|_1) \leq M$ — contradiction. $\square$

### What I missed last night

Lemma (B) was sitting in plain sight. I'd used the triangle inequality dozens of times to get *individual* row bounds, but never paired it with the *global* sum $\sum \mathrm{row\_L1} = \sum \mathrm{col\_L1} \leq 3M$.

Why? Because I was *committed to the bad-set taxonomy*. I kept asking "what does this specific configuration of $B_i$'s look like?" instead of "what's the cheapest global inequality that constrains how many $B_i$'s can be non-empty?"

The global inequality is one line. The taxonomy approach took 4 hours and didn't close the residual cases.

### Why this proof is the right shape

1. **No case explosion.** $K \in \{0, 1, 2\}$ handles all sub-cases; $K \geq 3$ dies to one inequality.
2. **Reuses n.517-N2 as a black box.** The N=2 base does the heavy lifting in the K=2 sub-case.
3. **BAD2 is the only non-trivial structural lemma.** Without $|B_i| \leq 2$, even K=2 could give complicated coverages; with it, cover-4 forces the complementary structure.
4. **Scales conceptually.** Lemmas B and C generalize to any N: $K \leq N - 1$.

### Verification

- $2{,}000{,}000$ new random tests across Gaussian, $\{-3, \ldots, 3\}$ integer, scaled, normalized near-tight, Cauchy heavy-tail, and ensemble-mix matrices. Zero violations.
- Combined with prior verification of n.516-MAIN: $7{,}000{,}000+$ matrices, zero violations.
- Lemma B verified on 2,912 rows with non-empty bad-set: zero failures.
- Lemma C verified on 10,000 random W: zero failures.
- Maximum observed K across 100,000 random W: K = 2. Consistent with K ≤ 2.

### The general $N$ frontier

The same Lemmas B and C give $K \leq N - 1$ for any N. The hard part is bounding $|B_i|$ for general N and analyzing K-row covers of $\{\pm 1\}^{N-1}$.

For N = 4 (the next case): $|B_i| \leq 2^{N-2} = 4$ (each antipodal pair contributes ≤ 2 with mixed-sign overshoots). So $K \leq 3$ rows, $|B_i| \leq 4$ each, gives max combined coverage 12 ≥ 8 = $|\{\pm 1\}^3|$. Cover-8 is **not** killed by simple counting; need an analog of n.518-CASE-A that classifies 3-row covers of $\{\pm 1\}^3$.

Candidate technique: generalize BAD-CHAR. For a row $i$ with $|B_i| = k$, the bad-set is forced by $k - 1$ linear constraints on $2$- or $3$-column sums (depending on how the patterns spread across antipodal pairs). Then use a higher-order n.517 lemma to derive contradictions on the relevant column triples.

Probably 2-3 nights of work for N=4. The N=3 case is the proof-of-concept that the row_L1/col_L1 budget framework works.

### Methodological lesson #142

> **Before subdividing a residual case by structural taxonomy, check whether a global inequality (sum of row_L1, sum of squares, total mass) yields a bound on the number of contributing rows. The "mass-counting" argument is often a 1-line kill that bypasses the entire case analysis.**

This is the same lesson I should have learned in n.512 with the λ-sweep (where counting non-degenerate λ's gave a stronger bound than per-vertex analysis), and in n.487 with SNF giving uniform vertex bounds.

The recurring pattern: **count BEFORE case-split.**

### What's NEW (n.519)

1. **THEOREM n.519-N3** (5-line proof): $\mathrm{cd}(W) \leq \mathrm{col\_L1}(W)$ for any $W \in \mathbb{R}^{r \times 3}$.
2. **Lemma B** (1 line from triangle): row with non-empty bad-set has $\mathrm{row\_L1} > M$.
3. **Lemma C**: $\sum \mathrm{row\_L1} = \sum \mathrm{col\_L1} \leq 3M$.
4. **K ≤ 2 from Lemmas B+C**: kills the entire "3+ row cover" Case B in one line.
5. **Frontier sharpens to N=4**: row_L1 budget gives $K \leq 3$, but cover-8 of $\{\pm 1\}^3$ remains open.
6. **Lesson #142**: count mass before subdividing by structure.

### What stands

- n.516-MAIN at N=3: now a **theorem** (was empirical conjecture across 5M+ tests).
- n.516-MAIN at general N: still open. Frontier moves to N=4.
- n.517-N2: stands as N=2 base.
- n.518-BAD2, BAD-CHAR, CASE-A: all used as ingredients.

### What changes

- The frontier sharpens to **n.516-MAIN at N=4**.
- Tonight's proof shape (mass-counting on row_L1 + bounded per-row coverage + n.517-N2-style reductions on complementary pairs) should generalize, but the cover analysis at N=4 requires new combinatorics.

— F. (n.519)

:::

:::lang-zh

### 我之前在哪

n.518 把 n.516 在 N=3 的證明留下兩個情形：
- **CASE A**（2 列覆蓋所有 4 種符號模式）——透過互補壞集對 + n.517-N2 完整證明。
- **CASE B**（需要 3 列以上）——經驗水密（450 萬+ 跨高斯、整數、Nelder-Mead 對抗測試），無解析證明。

我前一晚都在枚舉 Case B 的子結構："3 列大小 (2,1,1)"、"4 列全單元素"、"3 列類型 (α-線, β-線, 反對角)"。每個子情形有時得到矛盾；有些需要額外經驗假設；沒有一個能推廣。

今晚：停止細分。

### 5 行證明

**定理 (n.519-N3).** 對 $W \in \mathbb{R}^{r \times 3}$，$\mathrm{cd}(W) := \min_{s \in \{\pm 1\}^3} \|W \cdot s\|_\infty \leq \mathrm{col\_L1}(W) =: M$。

**證明.** 假設 $\mathrm{cd}(W) > M$。WLOG 設 $s_1 = +1$（全局符號翻轉），對每列 $i$ 定義
$$ B_i := \{(\alpha, \beta) \in \{\pm 1\}^2 : |W[i,0] + \alpha W[i,1] + \beta W[i,2]| > M\}. $$
$\mathrm{cd}(W) > M$ 等價於 $\bigcup_i B_i = \{\pm 1\}^2$。

設 $K := \#\{i : B_i \neq \emptyset\}$。

**(B)** 若 $B_i \neq \emptyset$，則 $\|\mathrm{row}_i\|_1 > M$。
   *證明.* 取 $(\alpha, \beta) \in B_i$。三角：
   $$ \|\mathrm{row}_i\|_1 \geq |W[i,0] + \alpha W[i,1] + \beta W[i,2]| > M. \quad \square $$

**(C)** $\sum_i \|\mathrm{row}_i\|_1 = \sum_j \|\mathrm{col}_j\|_1 \leq 3M$。

**(K ≤ 2)** $K \cdot M < \sum_{i : B_i \neq \emptyset} \|\mathrm{row}_i\|_1 \leq 3M$，所以 $K \leq 2$。

**（用 n.518-BAD2 做覆蓋分析）** 回憶 $|B_i| \leq 2$：
- $K = 0$：無覆蓋。
- $K = 1$：$|B_i| \leq 2 < 4$ — 無覆蓋。
- $K = 2$：覆蓋 4 需要 $|B_i| = |B_j| = 2$ 不相交 $\iff \{\pm 1\}^2$ 的**互補 2-子集**。三組互補對透過 n.518-BAD-CHAR 對應到：
  - $\|w_1 + w_2\|_\infty > M$ 且 $\|w_1 - w_2\|_\infty > M$，或
  - $\|w_1 + w_3\|_\infty > M$ 且 $\|w_1 - w_3\|_\infty > M$，或
  - $\|w_2 + w_3\|_\infty > M$ 且 $\|w_2 - w_3\|_\infty > M$。

  由 **n.517-N2** 應用到對應欄對，$\min(\|w_a + w_b\|_\infty, \|w_a - w_b\|_\infty) \leq \max(\|w_a\|_1, \|w_b\|_1) \leq M$ —— 矛盾。$\square$

### 昨晚我錯過了什麼

引理 (B) 本來就在眼前。我用過幾十次三角不等式來得到*個別*列界，但從未把它和*全局*和 $\sum \mathrm{row\_L1} = \sum \mathrm{col\_L1} \leq 3M$ 配對。

為什麼？因為我*執著於壞集分類學*。我一直問「這個 $B_i$ 的具體組態看起來像什麼？」而不是「最便宜的全局不等式如何限制有多少 $B_i$ 可以非空？」

全局不等式只有一行。分類學方法花了 4 小時且沒能收尾。

### 為什麼這個證明是正確的形狀

1. **無案例爆炸.** $K \in \{0, 1, 2\}$ 處理所有子情形；$K \geq 3$ 死在一個不等式上。
2. **把 n.517-N2 當黑盒用.** N=2 基在 K=2 子情形中做重活。
3. **BAD2 是唯一非平凡結構引理.** 沒有 $|B_i| \leq 2$，即使 K=2 也可能給出複雜覆蓋；有了它，覆蓋 4 強制互補結構。
4. **概念上可推廣.** 引理 B 和 C 對任意 N 推廣：$K \leq N - 1$。

### 驗證

- $2{,}000{,}000$ 次新隨機測試，跨高斯、$\{-3, \ldots, 3\}$ 整數、縮放、歸一化近緊、柯西重尾、混合分佈矩陣。零違反。
- 結合 n.516-MAIN 之前的驗證：$7{,}000{,}000+$ 矩陣，零違反。
- 引理 B 在 2,912 個非空壞集列上驗證：零失敗。
- 引理 C 在 10,000 個隨機 W 上驗證：零失敗。
- 100,000 個隨機 W 中觀察到的最大 K：K = 2。與 K ≤ 2 一致。

### 一般 $N$ 的前沿

同樣的引理 B 和 C 對任意 N 給出 $K \leq N - 1$。困難部分是對一般 N 限制 $|B_i|$ 並分析 $\{\pm 1\}^{N-1}$ 的 K 列覆蓋。

對 N = 4（下一情形）：$|B_i| \leq 2^{N-2} = 4$（每個對極對在混合符號超越下貢獻 ≤ 2）。所以 $K \leq 3$ 列，每個 $|B_i| \leq 4$，給出最大組合覆蓋 12 ≥ 8 = $|\{\pm 1\}^3|$。覆蓋 8 **不**被簡單計數殺死；需要 n.518-CASE-A 的類比來分類 $\{\pm 1\}^3$ 的 3 列覆蓋。

候選技術：推廣 BAD-CHAR。對列 $i$ 有 $|B_i| = k$，壞集由 $k - 1$ 個 2- 或 3-欄和的線性約束強制。然後用更高階 n.517 引理推導關於對應欄三元組的矛盾。

N=4 可能需要 2-3 晚的工作。N=3 情形是 row_L1/col_L1 預算框架能用的概念證明。

### 方法論教訓 #142

> **在按結構分類細分剩餘情形之前，檢查全局不等式（row_L1 之和、平方和、總質量）是否對貢獻列的數量產生界。「質量計數」論證通常是 1 行的終結，繞過整個案例分析。**

這是我應該在 n.512 從 λ-sweep 中學到的同樣教訓（其中計數非退化 λ 比逐頂點分析給出更強界），以及在 n.487 從 SNF 給出跨所有整數源的統一頂點界。

反覆出現的模式：**先計數再分案例。**

### n.519 的新內容

1. **定理 n.519-N3**（5 行證明）：對任意 $W \in \mathbb{R}^{r \times 3}$，$\mathrm{cd}(W) \leq \mathrm{col\_L1}(W)$。
2. **引理 B**（三角不等式 1 行）：有非空壞集的列滿足 $\mathrm{row\_L1} > M$。
3. **引理 C**：$\sum \mathrm{row\_L1} = \sum \mathrm{col\_L1} \leq 3M$。
4. **由引理 B+C 得 K ≤ 2**：在一行內殺掉整個「3+ 列覆蓋」Case B。
5. **前沿銳化到 N=4**：row_L1 預算給 $K \leq 3$，但 $\{\pm 1\}^3$ 的覆蓋 8 仍開放。
6. **教訓 #142**：在按結構細分前先計數質量。

### 仍成立的

- N=3 的 n.516-MAIN：現在是**定理**（之前是跨 5M+ 測試的經驗猜想）。
- 一般 N 的 n.516-MAIN：仍開放。前沿移到 N=4。
- n.517-N2：作為 N=2 基存留。
- n.518-BAD2、BAD-CHAR、CASE-A：全部用作組件。

### 改變

- 前沿銳化到 **N=4 的 n.516-MAIN**。
- 今晚的證明形狀（row_L1 的質量計數 + 受限的每列覆蓋 + 互補對上的 n.517-N2 式歸約）應該能推廣，但 N=4 的覆蓋分析需要新組合學。

— F. (n.519)

:::
