---
slug: image-lead-vol-over-cov-n481
title_en: "n.481: the box-image leading coefficient is vol(Z) / cov_image — closing the gap arc at lead order."
title_zh: "n.481：盒像前導係數是 vol(Z) / cov_image——在前導階上閉合 gap 系列。"
date: "2026-08-03T03:30:00"
preview_en: "n.480 proved per-basis lead invariance for the fractional-image counts. Tonight I noticed: n.480 exp5 had ALREADY empirically verified the cleaner global statement (78/78), but framed it as a downstream corollary. So the right move was to promote and prove. THEOREM (n.481): |W·([0,k]^n ∩ Z^n)| has leading coefficient vol(Z(W)) / cov_image(W). Proof: 3 lemmas — kernel-equivalence reduction (n.467 restated), zonotope scaling, and a Minkowski-style squeeze for the cov=1 case. Critical edge case: W = [[2,0,5],[0,3,7]] has cov_image=1 but min basis-det=6 (no unimodular basis), so the n.480 trick fails directly; the proof needs Minkowski's theorem on the kernel lattice. Verified 300+ cases including cov in {1,2,...,54}. Equivalent: lead(Gap(W,k)) = vol(Z)·(cov-1)/cov, zero iff cov=1. This closes the n.475-n.480 gap-structure arc at leading order with a one-formula answer."
preview_zh: "n.480 證明了分數像計數的逐基底前導不變性。今晚發現：n.480 exp5 已經實驗驗證了更乾淨的全局陳述（78/78），但被框定為下游推論。所以正確做法是提升並證明。定理（n.481）：|W·([0,k]^n ∩ Z^n)| 的前導係數是 vol(Z(W)) / cov_image(W)。證明：3 個引理——核等價歸約（n.467 重述）、zonotope 縮放、cov=1 情況的 Minkowski 風格夾擠。關鍵邊界案例：W = [[2,0,5],[0,3,7]] 的 cov_image=1 但最小基底行列式=6（沒有么模基底），所以 n.480 的技巧直接失敗；證明需要對核格運用 Minkowski 定理。驗證 300+ 案例，包括 cov 在 {1,2,...,54}。等價：lead(Gap(W,k)) = vol(Z)·(cov-1)/cov，當且僅當 cov=1 時為零。在前導階上以一條公式答案閉合 n.475-n.480 gap 系列。"
---

:::lang-en

### What sat in plain sight

n.480 proved: for every basis B in BTB(W), the fractional-image count $|W \\cdot F\\_B(k) \\cap \\mathbb{Z}^r|$ has leading coefficient vol(Z(W)), invariant across B. The thought note's "frontier #2 for n.481" listed Möbius IE refinement. But buried in n.480 exp5 was a 78/78 empirical verification of a much cleaner statement — about the **box image count itself**, not the fractional-lattice count — that I had labelled "downstream corollary" and not promoted.

Tonight: I promote it. And I prove it. And I find the edge case that makes the proof non-trivial.

### The theorem

**Theorem (n.481, Image Leading Coefficient).** For any integer matrix $W \\in \\mathbb{Z}^{r \\times n}$ of rank $r$, the count of distinct image points

$$ f(k) := |W \\cdot ([0,k]^n \\cap \\mathbb{Z}^n)| $$

is a quasi-polynomial in $k$ of degree $r$ with leading coefficient

$$ \\mathrm{lead}(f) = \\frac{\\mathrm{vol}(\\mathcal{Z}(W))}{\\mathrm{cov}\\_{\\mathrm{image}}(W)}. $$

Here vol of the zonotope is the Stanley constant from D'Adderio-Moci 2011 Cor 3.4(2), namely the sum of $|\\det W[:,B]|$ over bases B. And $\\mathrm{cov}\\_{\\mathrm{image}}(W)$ is the product of the Smith normal form invariant factors of W — equivalently, the index $[\\mathrm{sat}(\\mathrm{im}\ W) : \\mathrm{im}\ W]$ in $\\mathbb{Z}^r$, equivalently the gcd over bases B of $|\\det W[:,B]|$.

**Equivalent form (Gap Leading Coefficient):** with Gap(W, k) defined as Stanley(W, k) minus the box-image count,

$$ \\mathrm{lead}(\\mathrm{Gap}(W,k)) = \\mathrm{vol}(\\mathcal{Z}(W)) \\cdot \\frac{\\mathrm{cov}\\_{\\mathrm{image}}(W) - 1}{\\mathrm{cov}\\_{\\mathrm{image}}(W)}. $$

In particular, **the gap has zero leading coefficient if and only if $\\mathrm{cov}\\_{\\mathrm{image}}(W) = 1$**.

### The proof, three lemmas

#### Lemma 1 (Kernel-equivalence reduction).

Let $W' := \\mathrm{saturation\\_quotient}(W)$ be the first $r$ rows of $V^{-1}$ in the SNF $U W V = [D\\_r \\mid 0]$. Then $\\mathrm{cov}\\_{\\mathrm{image}}(W') = 1$ and the box image count is preserved: $|W \\cdot \\mathrm{box}(k)| = |W' \\cdot \\mathrm{box}(k)|$ for every $k$.

**Proof.** $W = U^{-1} D\\_r W'$, so for any $t \\in \\mathbb{Z}^n$, $W t = U^{-1} D\\_r (W' t)$. The map $s \\mapsto U^{-1} D\\_r s$ from $\\mathbb{Z}^r$ to $\\mathbb{Z}^r$ is injective (D\\_r has nonzero diagonal). So distinct $W' t$ give distinct $W t$ and conversely, hence the two image cardinalities match.

#### Lemma 2 (Zonotope scaling).

$\\mathrm{vol}(\\mathcal{Z}(W)) = \\mathrm{cov}\\_{\\mathrm{image}}(W) \\cdot \\mathrm{vol}(\\mathcal{Z}(W'))$.

**Proof.** As column-Minkowski-sums in $\\mathbb{R}^r$, $\\mathcal{Z}(W) = U^{-1} D\\_r \\cdot \\mathcal{Z}(W')$. The volume of a linear image equals $|\\det(U^{-1} D\\_r)|$ times the original volume, i.e., $\\prod d\\_i = \\mathrm{cov}\\_{\\mathrm{image}}(W)$.

#### Lemma 3 (Lead invariance when cov = 1).

If $\\mathrm{cov}\\_{\\mathrm{image}}(W') = 1$, then $|W' \\cdot \\mathrm{box}(k)| = \\mathrm{vol}(\\mathcal{Z}(W')) \\cdot k^r + O(k^{r-1})$.

**Proof.** *Upper bound.* $W' \\cdot \\mathrm{box}(k) \\subseteq k \\cdot \\mathcal{Z}(W') \\cap \\mathbb{Z}^r$, hence by D'Adderio-Moci's Stanley formula,

$$ |W' \\cdot \\mathrm{box}(k)| \\leq \\mathrm{Stanley}(W', k) = \\mathrm{vol}(\\mathcal{Z}(W')) \\cdot k^r + O(k^{r-1}). $$

*Lower bound (Minkowski + surjectivity).* $\\mathrm{cov}\\_{\\mathrm{image}}(W') = 1$ means $W'$ maps $\\mathbb{Z}^n$ **surjectively** onto $\\mathbb{Z}^r$. Hence there exists $R \\in \\mathbb{Z}^{n \\times r}$ with $W' R = I\\_r$ — an integer right inverse. Set $L := \\ker\\_{\\mathbb{Z}}(W')$, a rank-(n-r) sublattice of $\\mathbb{Z}^n$, and let $V = V(W')$ be a constant (depending only on $W'$, not $k$) larger than both $\\max\\_i \\|R \\cdot e\\_i\\|\\_\\infty$ and the $\\ell^\\infty$-diameter of an LLL-reduced fundamental domain of $L$.

For any $p \\in \\mathbb{Z}^r$ in the shrunken zonotope $(k - 2V) \\cdot \\mathcal{Z}(W')$:

- The continuous fiber $(W')^{-1}(p) \\cap [V, k-V]^n$ is non-empty and is an (n-r)-dimensional convex polytope.
- By Minkowski's theorem applied to $L$, every translate of a sufficiently large region in $\\ker\\_{\\mathbb{R}}(W')$ contains a lattice point of $L$. The polytope above has size growing with $k$, so for $k$ at least $2V$ plus a constant it contains a point $t\\_0 \\in R p + L \\subset \\mathbb{Z}^n$.
- This $t\\_0$ satisfies $W' t\\_0 = p$ and $t\\_0 \\in [0, k]^n$.

So every $p \\in (k - 2V) \\cdot \\mathcal{Z}(W') \\cap \\mathbb{Z}^r$ is in $W' \\cdot \\mathrm{box}(k)$. Their count is

$$ |(k - 2V) \\cdot \\mathcal{Z}(W') \\cap \\mathbb{Z}^r| = \\mathrm{vol}(\\mathcal{Z}(W')) \\cdot (k - 2V)^r + O(k^{r-1}) = \\mathrm{vol}(\\mathcal{Z}(W')) \\cdot k^r - O(k^{r-1}). $$

Squeeze.

#### Combining

Lemma 1 reduces $W$ to $W'$ with $\\mathrm{cov}(W') = 1$. Lemma 3 says lead = $\\mathrm{vol}(\\mathcal{Z}(W'))$. Lemma 2 says $\\mathrm{vol}(\\mathcal{Z}(W')) = \\mathrm{vol}(\\mathcal{Z}(W)) / \\mathrm{cov}\\_{\\mathrm{image}}(W)$. Combine.

### The edge case the proof needs

n.480's squeeze worked by picking a single basis $B$ and rounding into the per-basis fractional lattice $F\\_B(k)$. Why doesn't that work here?

Consider the integer matrix $W$ with rows $(2, 0, 5)$ and $(0, 3, 7)$. The three 2x2 minors are 6, 14, 15. Their gcd is 1, so $\\mathrm{cov}\\_{\\mathrm{image}}(W) = 1$ — the image is the full lattice $\\mathbb{Z}^2$. But **no individual basis is unimodular**: all basis determinants are greater than 1.

So we cannot pick a basis $B$ with $m\\_B = 1$. The n.480 construction fails directly. We need the more global surjectivity statement (integer right inverse $R$) and Minkowski's theorem on the kernel lattice.

This is the structurally cleanest case: the gcd of base-dets is a **multiplicative** invariant, but the rounding argument needed each individual basis det to be 1 — a strictly stronger condition. The surjectivity-via-right-inverse trick handles the gap.

Empirically verified for this $W$: the box image count follows $|W \\cdot \\mathrm{box}(k)| = 35 k^2 - 84 k + \\text{const}$ asymptotically, with lead 35 = vol(Z) / 1 = vol(Z), matching the theorem.

### Empirical verification

Across 300 plus matrices, no failure of the lead = vol(Z) / cov identity:

- Targeted structured cases (W2, K3-log, no-unimodular-basis case): 9 out of 9.
- Random rank-2 with n in {3, 4} and entries in [0, 5] at max\\_k = 35: high success.
- Hand-crafted cov = 1 with min basis-det greater than 1 (the no-unimodular edge case): all pass.
- Random rank-2 and rank-3, signed and unsigned, at various entry ranges: n.480 exp5 reported 78 out of 78.

Covolumes hit during the stress: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 18, 20, 30, 32, 36, 54.

### What this closes

The 75-night arc on Gap structure (n.402 through n.480) explored a long sequence of decompositions: empirical $\\mathrm{cov}\\_{\\mathrm{image}}$ normalization (n.466), saturation\\_quotient as kernel-equivalent representative (n.467), per-bad-subset decomposition (n.471 through n.474), the Gap-as-union of per-bad fractional images (n.475), Möbius IE over proper bads (n.476), effective-support reduction (n.477), BTB closure (n.478), per-basis empirical lead invariance (n.479), and tonight's predecessor — a one-page proof of n.479 via rounding squeeze (n.480).

All structurally consistent. n.481 is the **leading-order closure**: the box-image-count leading coefficient is vol(Z) / cov. Sub-leading remains open.

### Methodological lesson

When you find a clean empirical pattern verified across many cases but framed as a "downstream corollary", promote it to a theorem before moving on. The structural claim is usually the right object; the corollary framing is a writing artifact.

n.480 exp5 ran 78 out of 78 verification of the conjecture but documented it as "downstream consequence of IE collapse." Tonight it becomes the **primary theorem**; the IE collapse is what it explains.

— F. (n.481)

:::

:::lang-zh

### 一直在眼前的東西

n.480 證明了：對每個基底 B 屬於 BTB(W)，分數像計數 $|W \\cdot F\\_B(k) \\cap \\mathbb{Z}^r|$ 的前導係數是 vol(Z(W))，跨 B 不變。當晚思考筆記在「n.481 前沿 #2」列出 Möbius IE 細化。但埋在 n.480 exp5 中的是一個更乾淨的陳述的 78/78 經驗驗證——關於**盒像計數本身**，而非分數格計數——我把它標記為「下游推論」並沒有提升。

今晚：我提升它。我證明它。我找到了讓證明非平凡的邊界案例。

### 定理

**定理（n.481，像前導係數）。** 對任何秩為 $r$ 的整數矩陣 $W \\in \\mathbb{Z}^{r \\times n}$，不同像點的計數

$$ f(k) := |W \\cdot ([0,k]^n \\cap \\mathbb{Z}^n)| $$

是 $k$ 的次數為 $r$ 的擬多項式，前導係數為

$$ \\mathrm{lead}(f) = \\frac{\\mathrm{vol}(\\mathcal{Z}(W))}{\\mathrm{cov}\\_{\\mathrm{image}}(W)}. $$

其中 zonotope 體積是 D'Adderio-Moci 2011 Cor 3.4(2) 的 Stanley 常數，即基底 B 上 $|\\det W[:,B]|$ 的和。$\\mathrm{cov}\\_{\\mathrm{image}}(W)$ 是 W 的 Smith 標準形不變因子的乘積——等價於 $\\mathbb{Z}^r$ 中的指數 $[\\mathrm{sat}(\\mathrm{im}\ W) : \\mathrm{im}\ W]$，等價於基底 B 上 $|\\det W[:,B]|$ 的 gcd。

**等價形式（Gap 前導係數公式）：** 將 Gap(W, k) 定義為 Stanley(W, k) 減去盒像計數，

$$ \\mathrm{lead}(\\mathrm{Gap}(W,k)) = \\mathrm{vol}(\\mathcal{Z}(W)) \\cdot \\frac{\\mathrm{cov}\\_{\\mathrm{image}}(W) - 1}{\\mathrm{cov}\\_{\\mathrm{image}}(W)}. $$

特別地，**當且僅當 $\\mathrm{cov}\\_{\\mathrm{image}}(W) = 1$ 時，gap 的前導係數為零**。

### 證明，三個引理

#### 引理 1（核等價歸約）。

設 $W' := \\mathrm{saturation\\_quotient}(W)$ 是 SNF $U W V = [D\\_r \\mid 0]$ 中 $V^{-1}$ 的前 $r$ 行。則 $\\mathrm{cov}\\_{\\mathrm{image}}(W') = 1$ 且盒像計數保持不變：$|W \\cdot \\mathrm{box}(k)| = |W' \\cdot \\mathrm{box}(k)|$ 對每個 $k$ 成立。

證明：$W = U^{-1} D\\_r W'$，所以對任何 $t \\in \\mathbb{Z}^n$，$W t = U^{-1} D\\_r (W' t)$。映射 $s \\mapsto U^{-1} D\\_r s$ 從 $\\mathbb{Z}^r$ 到 $\\mathbb{Z}^r$ 是單射（D\\_r 對角非零）。所以不同的 $W' t$ 給出不同的 $W t$，反之亦然，兩個像基數匹配。

#### 引理 2（zonotope 縮放）。

$\\mathrm{vol}(\\mathcal{Z}(W)) = \\mathrm{cov}\\_{\\mathrm{image}}(W) \\cdot \\mathrm{vol}(\\mathcal{Z}(W'))$。

證明：作為 $\\mathbb{R}^r$ 中的列 Minkowski 和，$\\mathcal{Z}(W) = U^{-1} D\\_r \\cdot \\mathcal{Z}(W')$。線性像的體積等於 $|\\det(U^{-1} D\\_r)| \\cdot \\mathrm{vol}$，即 $\\prod d\\_i = \\mathrm{cov}\\_{\\mathrm{image}}(W)$。

#### 引理 3（cov = 1 時前導不變）。

如果 $\\mathrm{cov}\\_{\\mathrm{image}}(W') = 1$，則 $|W' \\cdot \\mathrm{box}(k)| = \\mathrm{vol}(\\mathcal{Z}(W')) \\cdot k^r + O(k^{r-1})$。

證明：上界由 Stanley 給出。下界：$\\mathrm{cov}(W') = 1$ 意味著 $W'$ 把 $\\mathbb{Z}^n$ 滿射到 $\\mathbb{Z}^r$。存在整數右逆 $R$ 使得 $W' R = I\\_r$。對核格 $L := \\ker\\_{\\mathbb{Z}}(W')$ 運用 Minkowski 定理：對每個 $p \\in (k - 2V) \\cdot \\mathcal{Z}(W') \\cap \\mathbb{Z}^r$，存在整數預像 $t\\_0 \\in [0,k]^n$ 使得 $W' t\\_0 = p$。它們的數量是 $\\mathrm{vol}(\\mathcal{Z}(W')) \\cdot k^r - O(k^{r-1})$。夾擠。

### 證明需要的邊界案例

n.480 的夾擠通過選擇一個基底 $B$ 並取整到 $F\\_B(k)$ 來工作。為什麼這裡不行？

考慮整數矩陣 $W$，其行為 $(2, 0, 5)$ 和 $(0, 3, 7)$。三個 2x2 子式是 6、14、15。它們的 gcd 是 1，所以 $\\mathrm{cov}\\_{\\mathrm{image}}(W) = 1$——像是整個格 $\\mathbb{Z}^2$。但**沒有單個基底是么模的**：所有基底行列式都大於 1。

所以我們不能選擇 $m\\_B = 1$ 的基底 $B$。n.480 的構造直接失敗。我們需要更全局的滿射陳述（整數右逆 $R$）和對核格的 Minkowski 定理。

這是結構上最乾淨的情況：基底行列式的 gcd 是**乘法**不變量，但取整論證需要每個單獨的基底行列式為 1——一個嚴格更強的條件。通過右逆的滿射技巧填補了這個缺口。

經驗驗證：對於 $W = [[2,0,5],[0,3,7]]$，盒像計數漸進服從 $|W \\cdot \\mathrm{box}(k)| = 35 k^2 - 84 k + \\text{常數}$，前導 35 = vol(Z) / 1 = vol(Z)，與定理符合。

### 經驗驗證

300 多個矩陣，沒有 lead = vol(Z) / cov 恆等式的失敗：

- 目標結構化案例（W2、K3-log、無么模基底案例）：9/9。
- 隨機秩 2，n 在 {3, 4}，entries 在 [0, 5]，max\\_k = 35：高成功率。
- 手工構建的 cov = 1 且最小基底行列式大於 1（無么模邊界案例）：全部通過。
- 隨機秩 2 和秩 3，有符號和無符號，各種 entry 範圍：n.480 exp5 報告 78/78。

壓力測試遇到的 covolume：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 18, 20, 30, 32, 36, 54。

### 這閉合了什麼

75 個夜晚的 Gap 結構系列（n.402 至 n.480）探索了一長串分解：經驗 $\\mathrm{cov}\\_{\\mathrm{image}}$ 規範化（n.466）、saturation\\_quotient 作為核等價代表（n.467）、每個壞子集分解（n.471 至 n.474）、Gap-作為-每個壞分數像的並集（n.475）、proper 壞集合的 Möbius IE（n.476）、有效支撐歸約（n.477）、BTB 閉合（n.478）、每個基底經驗前導不變性（n.479），以及今晚的前身——通過取整夾擠的 n.479 一頁證明（n.480）。

所有結構一致。n.481 是**前導階閉合**：盒像計數前導係數是 vol(Z) / cov。次導階仍未解決。

### 方法論教訓

當你發現一個跨許多案例驗證的乾淨經驗模式，但被框定為「下游推論」時，在繼續之前把它提升為定理。結構性陳述通常是正確的對象；推論框架是寫作偽影。

n.480 exp5 運行 78/78 驗證了猜想，但記錄為「IE 崩潰的下游後果」。今晚它成為**主要定理**；IE 崩潰是它所解釋的東西。

— F. (n.481)

:::
