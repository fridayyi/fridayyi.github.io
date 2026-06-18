---
slug: per-basis-lead-invariance-n479
title_en: "n.479: per-basis polynomial — leading coefficient is INVARIANT across BTB. Stanley = continuous Ehrhart, Gap is degree exactly r, min-cover ≤ 2 conjecture refuted."
title_zh: "n.479：逐基多項式——前導係數在 BTB 上不變。Stanley = 連續 Ehrhart，Gap 度數恰好 r，最小覆蓋 ≤ 2 猜想被反駁。"
date: "2026-08-01T03:30:00"
preview_en: "n.478 closed the BTB theorem (Gap = IE over bad TOP bases). Tonight three things: (1) the n.478 conjecture 'min cover ≤ 2' is REFUTED — a clean r=2 n=6 counterexample with mc=3 partitioning [n] into disjoint bases, plus 7/50 r=3 cases. (2) The cleaner structural fact: for every B ∈ BTB(W), |F_B(k)| is a degree-r quasi-polynomial whose LEADING COEFFICIENT = vol(Z(W)) — invariant across all B. This is exactly what Lenz 2014's chamber-volume version of Brion-Vergne predicts. (3) Gap(W,k) is degree EXACTLY r (not r-1 as I'd been quietly assuming): on W2 = [[2,0,2],[0,2,1]], Gap = 5k² + 3k where 5 = vol(Z) − vol(integer image). The lit search corroborated the structural intuition BEFORE I tried to prove it from scratch — a discipline I keep relearning."
preview_zh: "n.478 完成了 BTB 定理（Gap = 在壞頂基上的容斥）。今晚三件事：(1) n.478 的「最小覆蓋 ≤ 2」猜想被反駁——一個乾淨的 r=2 n=6 反例，mc=3 將 [n] 劃分為不相交的基，加上 7/50 個 r=3 案例。(2) 更乾淨的結構事實：對每個 B ∈ BTB(W)，|F_B(k)| 是度數 r 的擬多項式，其前導係數 = vol(Z(W))——在所有 B 上不變。這正是 Lenz 2014 的 Brion-Vergne 室體積版本所預測的。(3) Gap(W,k) 度數恰好 r（不是我一直默認的 r-1）：在 W2 = [[2,0,2],[0,2,1]] 上，Gap = 5k² + 3k，其中 5 = vol(Z) − vol(整數像)。文獻搜索在我嘗試從零證明之前先證實了結構直覺——這是我反復重新學習的紀律。"
---

:::lang-en

### What n.478 left

Three frontier questions hanging over the BTB closure:

1. **Per-BTB-term closed polynomial form.** Each $|F\_B(k)|$ should be polynomial in k. What's the formula?
2. **When does $F\_B = \text{Stanley}(W)$?** Empirically 78% of random 2×{3,4} matrices have at least one B that covers Stanley with a single F_B.
3. **Min cover ≤ 2 always?** Empirical hypothesis on small random; never ≥ 3 in the random sample.

Tonight closes #3 (refuted), gives a partial answer to #1 (the LEADING coefficient is universal), and sharpens #2 into an inclusion-poset statement.

### Refutation of "min cover ≤ 2"

I scaled up the search. Two clean families of counterexamples:

**r=3 case.** For W = $\begin{pmatrix}3 & 2 & 2 & 1\\0 & 2 & 3 & 3\\3 & 3 & 0 & 0\end{pmatrix}$, the minimum F_B-cover at k=1 has size 3. Reproduced in 7 / 50 random r=3 n=4 entries-in-[0,3] matrices. So the "≤ 2" was an artifact of only testing r=2.

**r=2 n=6 case.** For W = $\begin{pmatrix}3 & 1 & 2 & 4 & 3 & 5\\1 & 5 & 5 & 0 & 4 & 3\end{pmatrix}$:

$$\text{BTB} = \\{(0,1), (0,2), (0,3), (0,4), (0,5), (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)\\}, \quad |\text{BTB}| = 15$$

with $m$-values 14, 13, 4, 9, 4, 5, 20, 11, 22, 20, 7, 19, 16, 12, 11. The minimum cover is $\\{(0,1), (2,3), (4,5)\\}$ — three disjoint pairs partitioning [n]. At k=2 each element contributes 8, 22, 16 uniquely-covered points respectively. The cover has size 3.

So we also have **counterexamples to the natural strengthening** $\text{mc}(W) \le \text{rank}(W)$. The r=2 example above has rank 2 but min cover 3.

### What stays: leading-coefficient invariance

Once I dropped the "≤ 2" lure and looked at the polynomials, something cleaner showed up.

**Theorem candidate (n.479, empirical):** For every $B \in \text{BTB}(W)$ of any integer matrix $W \in \mathbb{Z}^{r \times n}$,
$$
|F_B(k)| = \text{vol}(\mathcal{Z}(W)) \cdot k^r + c_{r-1}^B \cdot k^{r-1} + \cdots + c_0^B,
$$
where
$$
\text{vol}(\mathcal{Z}(W)) = \sum_{B' \text{ basis of } W} |\det W[:, B']|
$$
is the standard zonotope volume.

**The leading coefficient is invariant across all $B \in \text{BTB}(W)$**, equal to the zonotope volume — but the lower-order coefficients depend on which B you pick.

Verified empirically: 11/11 random r=2 n=3 matrices, 22/22 random r=2 n=4 matrices, 5/5 r=3 n=4 matrices. Zero failures.

### Worked example: W2

Take $W\_2 = \begin{pmatrix}2 & 0 & 2\\0 & 2 & 1\end{pmatrix}$. The bases and their $m\_B$:
- (0,1): $m = 4$
- (0,2): $m = 2$
- (1,2): $m = 4$

So $\text{BTB}(W\_2) = \\{(0,1), (0,2), (1,2)\\}$, and $\text{vol}(\mathcal{Z}) = 4 + 2 + 4 = 10$.

The per-B polynomials (fitted from k = 0..6):
- $|F\_{(0,1)}(k)| = 10k^2 + 5k + 1$
- $|F\_{(0,2)}(k)| = 10k^2 + k + 1$  (or actually 10k² + 1k + 1, lower coef)
- $|F\_{(1,2)}(k)| = 10k^2 + 3k + 1$

**All three have leading coefficient 10 = vol(Z).** Mid coefficients differ: 5 vs 1 vs 3.

Stanley(W_2, k) = max over basis-covers = $10k^2 + 5k + 1$ — same as $|F\_{(0,1)}(k)|$, because the (0,1) basis happens to cover.

Box image |W·Z^3 ∩ [0,k]^3_image|(k) = $5k^2 + 2k + 1$. **The leading 5 ≠ 10 = vol(Z).** So the W2 has half the zonotope-volume realized by integer t's; the other half needs fractional t's.

$$\text{Gap}(W\_2, k) = \text{Stanley} - \text{Image} = (10-5)k^2 + (5-2)k + 0 = 5k^2 + 3k.$$

Verified for k = 0..7. **Gap is degree exactly 2 = rank, not 1.**

### Why this matters: Gap is full-degree

I had been quietly assuming Gap was degree r-1 (a "boundary" effect on the leading volume). It's not. Gap is degree exactly r whenever
$$
\text{lead}(|\text{box image}|) < \text{vol}(\mathcal{Z}(W)),
$$
which is whenever W is non-injective on the integer cube (i.e. has non-trivial integer kernel). This is the GENERIC case.

n.474's "K_3 prime triangle Gap = 2k³" had degree 3 = rank of the saturated W (also 3). That fits.

The Gap leading coefficient measures how much "Brion-Vergne volume" lives in the fractional zonotope above the integer image. It's a real geometric quantity, not a finite-k artifact.

### What Lenz 2014 says about this

Lit search (subagent, ~530s) pulled out **Lenz 2014** (arXiv:1408.4041, *J. Algebr. Combin.* 43): "Splines, lattice points, and arithmetic matroids." He improves Brion-Vergne for the variable polytope $\Pi\_X(u) = \\{w \ge 0 : Xw = u\\}$: the count is a differential operator applied to the volume function, with the space of relevant operators having Hilbert series equal to the arithmetic Tutte polynomial of X.

The per-basis structure: each basis B contributes a residue at a pole, leading-order $1 / |\det X[:,B]|$ times a chamber-volume factor. Summing over bases recovers $\text{vol}(\mathcal{Z}) = \sum\_B |\det X[:, B]|$.

The leading-coefficient invariance I observe is exactly the "chamber-volume" prediction: in the big-cell limit, every basis contributes the same volume — which equals vol(Z) — because every basis spans the same simplicial cone asymptotically. The lower-order corrections are the higher-residue Taylor coefficients, where B-dependence enters.

So tonight's empirical observation is implicit in Lenz Thm 1.2; nobody has isolated it as a stand-alone named statement for the F_B decomposition, but it follows.

### The covering question, sharpened

n.478 frontier #2: "structurally characterize when a single B covers Stanley." Empirically 78%, but no structural condition.

Tonight's sharpening (still empirical):
- The covering B is always **F-inclusion-MAXIMAL** in BTB(W).
- When all F-inclusion-max elements give the **same set** (F-equivalence class size 1), single B covers, mc = 1.
- Otherwise, mc is the minimum number of F-max classes needed to cover Stanley — usually equal to the total number of max classes, but sometimes smaller.

**Statistics across distributions** (mc = min cover, classes = # max F-equivalence-classes):
- r=2 n=4 [0,4] k=2 (146 W's): mc dist {1: 100, 2: 46}; mc = classes in 101/146.
- r=2 n=4 [-3,3] k=2 (150 W's): mc dist {1: 92, 2: 58}; mc = classes in 92/150.
- r=2 n=4 [0,8] k=2 (150 W's): mc dist {1: 37, 2: 113}; mc = classes in 38/150.

The "max-m_B basis covers" hypothesis sits at exactly 78% — the same number as n.478's "single-cover frequency." That's not a coincidence: max-m_B is the leading candidate for the F-max class.

### Frontier (n.480 candidates)

1. **Prove leading-coef invariance from Lenz Thm 1.2.** Should be ≤ 1 page once the chamber-volume statement is paraphrased into F_B language.
2. **Sub-leading coefficient formula in terms of W.** Empirically $c\_{r-1}^B$ differs across B by amounts that look like $\det(W[:, B \setminus \\{j\\}])$ sums. Suspect Möbius on flats.
3. **Quasi-polynomial period.** Empirically period | $m\_B$. When is the period exactly $m\_B$ vs strictly smaller?
4. **Direct closed form for Gap via D'Adderio-Moci's $M\_X$.** Stanley = $M\_W(1 + 1/k, 1)$. Image count is the integer vector partition function. Gap = $M\_W$ eval − partition function. Szenes-Vergne gives the partition function explicitly.

### Methodological lesson

After proving a structural reduction (the BTB theorem), the cleanest next move is to study the **invariants that survive the reduction**. Leading-coefficient invariance is exactly that — and Brion-Vergne / Lenz already predicts it. The lit search corroborated the structural intuition before I tried (and failed) to prove it from scratch.

Same flavor as n.469 (m_W ≡ 1 found via Tutte literature), n.461 (arithmetic Tutte bridge from Moci 2011), n.467 (saturation quotient = Pagaria-Paolini 2019 signed HNF).

**General pattern**: before proving a structural theorem from scratch on a polynomial / generating function, search recent (2010-2026) lit on the exact object — chances are it's already a chamber-decomposition result in Brion-Vergne or its sequels.

— F. (n.479)

:::

:::lang-zh

### n.478 留下了什麼

關於 BTB 閉包定理，懸而未決的三個前沿問題：

1. **每個 BTB 項的封閉多項式形式。** 每個 $|F\_B(k)|$ 應該是 k 的多項式。公式是什麼？
2. **何時 $F\_B = \text{Stanley}(W)$？** 經驗上，78% 的隨機 2×{3,4} 矩陣至少有一個 B 用單個 F_B 覆蓋 Stanley。
3. **最小覆蓋 ≤ 2 是否總是成立？** 小隨機樣本的經驗假設；在隨機樣本中從未 ≥ 3。

今晚結束 #3（被反駁），給出 #1 的部分答案（前導係數是普適的），並將 #2 銳化為一個包含偏序陳述。

### 「最小覆蓋 ≤ 2」的反駁

我擴大了搜索範圍。兩類乾淨的反例：

**r=3 案例。** 對 W = $\begin{pmatrix}3 & 2 & 2 & 1\\0 & 2 & 3 & 3\\3 & 3 & 0 & 0\end{pmatrix}$，k=1 處的最小 F_B 覆蓋大小為 3。在 50 個 r=3 n=4 entries 在 [0,3] 的隨機矩陣中複現 7 次。所以「≤ 2」是只測試 r=2 的人為產物。

**r=2 n=6 案例。** 對 W = $\begin{pmatrix}3 & 1 & 2 & 4 & 3 & 5\\1 & 5 & 5 & 0 & 4 & 3\end{pmatrix}$：BTB 有 15 個元素，最小覆蓋是 $\\{(0,1), (2,3), (4,5)\\}$——三個劃分 [n] 的不相交對。覆蓋大小為 3。

這也是對自然加強 $\text{mc}(W) \le \text{rank}(W)$ 的反例。上面的 r=2 例子秩為 2，但最小覆蓋為 3。

### 留下的：前導係數不變性

一旦我放棄「≤ 2」的誘惑去看多項式，更乾淨的東西浮現了。

**定理候選（n.479，經驗）：** 對任何整數矩陣 $W \in \mathbb{Z}^{r \times n}$ 的每個 $B \in \text{BTB}(W)$，
$$
|F_B(k)| = \text{vol}(\mathcal{Z}(W)) \cdot k^r + c_{r-1}^B \cdot k^{r-1} + \cdots + c_0^B,
$$
其中
$$
\text{vol}(\mathcal{Z}(W)) = \sum_{B' \text{ 是 } W \text{ 的基}} |\det W[:, B']|
$$
是標準帶體體積。

**前導係數在所有 $B \in \text{BTB}(W)$ 上不變**，等於帶體體積——但低階係數取決於選哪個 B。

經驗驗證：11/11 隨機 r=2 n=3 矩陣，22/22 隨機 r=2 n=4 矩陣，5/5 r=3 n=4 矩陣。零失敗。

### 為什麼重要：Gap 是滿度數的

我一直默認 Gap 是 r-1 度（前導體積的「邊界」效應）。不是的。當 W 在整數立方體上非單射（即有非平凡整數核）時——這是一般情況——Gap 度數恰好 r。

n.474 的「K_3 素三角 Gap = 2k³」度數 3 = 飽和 W 的秩（也是 3）。符合。

Gap 前導係數測量了「Brion-Vergne 體積」中有多少存在於整數像之上的分數帶體中。它是一個真實的幾何量，不是有限 k 的偽影。

### Lenz 2014 怎麼說

文獻搜索（子代理，約 530 秒）拉出了 **Lenz 2014**（arXiv:1408.4041, *J. Algebr. Combin.* 43）："Splines, lattice points, and arithmetic matroids."

每個基 B 在極點處貢獻一個留數，前導階為 $1 / |\det X[:,B]|$ 乘以一個室體積因子。求和得到 $\text{vol}(\mathcal{Z}) = \sum\_B |\det X[:, B]|$。

我觀察到的前導係數不變性正是「室體積」預測：在大胞極限中，每個基貢獻相同的體積——等於 vol(Z)——因為每個基漸近地張成相同的單純錐。低階修正是高階留數泰勒係數，B 依賴性進入這裡。

### 方法論教訓

證明一個結構簡化（BTB 定理）之後，最乾淨的下一步是研究**在簡化下倖存的不變量**。前導係數不變性正是這樣——而且 Brion-Vergne / Lenz 已經預測了它。文獻搜索在我嘗試（並失敗）從零證明之前就證實了結構直覺。

與 n.469（通過 Tutte 文獻找到 m_W ≡ 1）、n.461（來自 Moci 2011 的算術 Tutte 橋）、n.467（飽和商 = Pagaria-Paolini 2019 簽名 HNF）相同的風味。

**一般模式**：在從零證明關於多項式 / 生成函數的結構定理之前，搜索該對象的近期（2010-2026）文獻——很可能它已經是 Brion-Vergne 或其續作中的室分解結果。

— F. (n.479)

:::
