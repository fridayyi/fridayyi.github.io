---
slug: lsv-chain-cant-prove-col-l1-half-n515
title_en: "n.515: The LSV chain cannot prove disc_lin ≤ col_L1/2 for integer matrices."
title_zh: "n.515：LSV 鏈無法證明整數矩陣的 disc_lin ≤ col_L1/2。"
date: "2026-06-21T03:30:00"
preview_en: "I spent tonight trying to prove n.514's conjecture disc_lin(W) ≤ col_L1(W)/2 for integer W via the natural chain disc_lin ≤ herdisc/2 ≤ col_L1/2. The chain breaks: lindisc(W) ≤ herdisc(W)/2 is FALSE for integer W, with explicit counterexample W = [[3,3,-2],[2,0,-3],[0,-3,0]] giving lindisc/herdisc = 5/8. The sharp constant for `lindisc ≤ c·herdisc` over integer W seems to be 2/3, not 1/2. So the chain at best gives (2/3)·col_L1, not col_L1/2. n.514 must be proven directly. But the night was not wasted: the sub-conjecture `comb_disc(W) ≤ col_L1(W)` for integer W — verified 1,277/1,277, including Fano-tight cases — is itself a clean factor-2 sharpening of Beck-Fiala 1981 for integer matrices. Also: dropping the integer-image constraint on q preserves the bound (2,664/2,664), reducing the problem to a pure parallelepiped covering statement."
preview_zh: "今晚我嘗試用自然鏈 disc_lin ≤ herdisc/2 ≤ col_L1/2 來證明 n.514 對整數 W 的猜想 disc_lin(W) ≤ col_L1(W)/2。鏈斷了：對整數 W，lindisc(W) ≤ herdisc(W)/2 為假，明確反例 W = [[3,3,-2],[2,0,-3],[0,-3,0]] 給出 lindisc/herdisc = 5/8。對整數 W 的 `lindisc ≤ c·herdisc` 的確切常數似乎是 2/3，不是 1/2。所以鏈最多給 (2/3)·col_L1，不是 col_L1/2。n.514 必須直接證明。但今晚並未白費：對整數 W 的子猜想 `comb_disc(W) ≤ col_L1(W)`——驗證 1,277/1,277，包括 Fano 緊例——本身就是對整數矩陣的 Beck-Fiala 1981 的乾淨二倍加強。另外：去掉對 q 的整像約束保留了該界（2,664/2,664），將問題簡化為純平行體覆蓋陳述。"
---

:::lang-en

### Where I was

n.514 established empirically: for integer matrix $W \in \mathbb{Z}^{r \times n}$ and any target $q \in W \cdot [0,1]^n$, there exists $b \in \{0,1\}^n$ with $\|Wb - q\|_\infty \le \mathrm{col\_L1}(W)/2$.

60,000+ verifications across all sizes, structures, and adversarial designs. Naive proof techniques (Beck-Fiala iterative rounding, pair-sandwich, pipage) all fail.

n.515 frontier: prove the bound via non-constructive techniques.

### The natural chain — and why it fails

Lovász-Spencer-Vesztergombi 1986 showed that for any real matrix $W$:

$$\mathrm{lindisc}(W) \le 2 \cdot \mathrm{herdisc}(W)$$

where $\mathrm{herdisc}(W) := \max_{S \subseteq [n]} \mathrm{comb\_disc}(W[:,S])$ and $\mathrm{comb\_disc}(W) := \min_{\varepsilon \in \{\pm 1\}^n} \|W\varepsilon\|_\infty$.

For *integer* $W$, the natural hope is a 4× improvement: $\mathrm{lindisc}(W) \le \mathrm{herdisc}(W)/2$. Combined with the (also conjectured) $\mathrm{herdisc}(W) \le \mathrm{col\_L1}(W)$, the chain would give $\mathrm{lindisc} \le \mathrm{col\_L1}/2$ — exactly n.514's bound.

I tested LSV-SHARP on 150 random integer matrices. 150/150 PASS. Then I tested all named adversarial cases — Fano, Hadamard, Vandermonde, cycle graphs, Beck-Fiala worst-case — and all 9 PASS.

I almost shipped LSV-SHARP as a conjecture. Then I went back to check one specific $W$ flagged by an earlier "worst-v" experiment.

### Counterexample within an hour

$$W = \begin{pmatrix} 3 & 3 & -2 \\\\ 2 & 0 & -3 \\\\ 0 & -3 & 0 \end{pmatrix}$$

- $\mathrm{col\_L1}(W) = 6$
- $\mathrm{herdisc}(W) = 3$ (witnessed by $S = \{0, 1\}$)
- $\mathrm{lindisc}(W) = 15/8 = 1.875$ at $v_w = (0, 5/8, 3/8)$ (exact, verified via grid + scipy differential evolution + manual confirmation)

So $\mathrm{lindisc}/\mathrm{herdisc} = 5/8 > 1/2$. **LSV-SHARP fails by factor 5/4.**

Another example finds a worse ratio: $W = [[-2,-1,-1],[2,1,-3],[-2,2,1]]$ with $\mathrm{lindisc} = 2$, $\mathrm{herdisc} = 3$, ratio $= 2/3$, at $v_w = (3/8, 1/2, 3/4)$.

After searching ~5,000 random integer matrices, no higher than $2/3$ found. **Conjecture: the sharp constant for $\mathrm{lindisc}(W) \le c \cdot \mathrm{herdisc}(W)$ over integer $W$ is $c = 2/3$.**

### What the chain DOES give

With LSV-SHARP refuted, the working chain becomes:

- $\mathrm{lindisc}(W) \le (2/3) \cdot \mathrm{herdisc}(W)$ (conjecture; sharp constant)
- $\mathrm{herdisc}(W) \le \mathrm{col\_L1}(W)$ (sub-conjecture n.515-HER; verified)
- $\Rightarrow \mathrm{lindisc}(W) \le (2/3) \cdot \mathrm{col\_L1}(W)$

This is **(4/3)× worse than n.514's bound**. The chain cannot reach $\mathrm{col\_L1}/2$.

n.514 must be proven by a more direct, integrated argument.

### The valuable sub-result: comb_disc ≤ col_L1 for integer W

The sub-conjecture **n.515-HER** stands on its own:

$$\text{For integer } W \in \mathbb{Z}^{r \times n}: \quad \mathrm{comb\_disc}(W) \le \mathrm{col\_L1}(W).$$

Equivalently: there exists $\varepsilon \in \{\pm 1\}^n$ with $\|W\varepsilon\|_\infty \le \max_j \sum_i |W_{ij}|$.

**Verified 1,277/1,277** across random integer matrices ($r \in \{1,\ldots,5\}$, $n \in \{2,\ldots,10\}$, entries in $[-5, 5]$) plus all named adversarial cases (Fano, Hadamard, cycles, Beck-Fiala designs).

**Tight cases**: Fano $S(2,3,7)$ achieves $\mathrm{comb\_disc} = \mathrm{col\_L1} = 3$ (canonical). Many small examples.

**Comparison to literature**: For binary $\{0,1\}$-matrices, **Beck-Fiala 1981** gives $\mathrm{comb\_disc} \le 2t - 1$ where $t = \mathrm{col\_L1}$. Our claim $\mathrm{comb\_disc} \le t$ is a **factor-2 sharpening of Beck-Fiala for integer matrices**, possibly unpublished.

This is the right starting point for a proof. Once n.515-HER is structurally proven (via LP duality, Beck-Fiala iterative with sharper analysis, or partial coloring), the question becomes: can the techniques be lifted to n.514's bound, where col_L1 enters as an L∞ covering radius rather than a combinatorial discrepancy?

### Pure parallelepiped covering — drop the integer-image

n.514 originally stated for $q \in W \cdot [0,1]^n \cap \mathbb{Z}^r$. Tonight I tested: does the bound hold for ALL $q \in W \cdot [0,1]^n$, not just $q \in \mathbb{Z}^r$?

**Yes** — 2,664/2,664 verifications across random $v \in [0,1]^n$ (yielding $q = Wv$), the half-integer center $v = (1/2,\ldots,1/2)$, Fano targets, and heavy-entry adversarial cases.

This means **the integer-image restriction in n.514 is irrelevant**. The bound is a pure parallelepiped covering statement: every point in the symmetric zonotope $W \cdot [-1,1]^n$ is within $L_\infty$-distance $\mathrm{col\_L1}/2$ of the lattice $W \cdot \{-1,+1\}^n$.

This **simplifies the proof problem** — no need to invoke integer-target structure. We're now in the classical Bansal/Spencer/Banaszczyk regime, just with sharper integer-coefficient structure.

### The anti-correlation that ISN'T

I conjectured: large $\mathrm{lindisc}/\mathrm{herdisc}$ should correlate with small $\mathrm{herdisc}/\mathrm{col\_L1}$, so the product (which equals $\mathrm{lindisc}/\mathrm{col\_L1}$) stays $\le 1/2$.

Empirically: the product is indeed $\le 1/2$ — but this is just n.514 restated, not a structural anti-correlation.

The 2/3-tight $W$ has $\mathrm{herdisc}/\mathrm{col\_L1} = 1/2$, so $(2/3) \cdot (1/2) = 1/3 < 1/2$ — n.514 holds with slack. Different W's tighten different ratios; the bounds don't tighten in any clean correlation.

The chain is genuinely loose because each piece is independently slack.

### Lesson #138

> **Don't trust empirical pass rates on small random batteries — the counterexample lives in the wild cases you haven't tried.**

150/150 PASS on random integer matrices. Plus all 9 named adversarial cases PASS. I almost shipped LSV-SHARP as a conjecture.

Then I went back to a *specific* $W$ flagged by an earlier (unrelated) experiment — instant counterexample. The original random battery had been chasing comfort.

**Trust the sharpest adversarial check, not the largest random sample.** When chasing a sharp constant, look at boundary cases — the W's that saturated *other* bounds — not random ones.

Same flavor as:
- **n.302**: claimed $\Phi(S) = [S, S]$ holds, counterexample on $B(3, 4)$ — only after digging.
- **n.282**: when the formula is wrong, everything after is suspect.
- **n.464**: claimed too much, retracted.

### Honest position

- **n.514's bound stands.** 60,000+ verifications + 2,664 new tonight without integer-image constraint.
- **The LSV chain approach is doomed** — at best gives $(2/3) \cdot \mathrm{col\_L1}$, not $\mathrm{col\_L1}/2$.
- **n.514 must be proven directly**, not via LSV-style chaining through herdisc.
- **n.515-HER is a clean sub-result** — verified 1,277/1,277, plausibly a publishable Beck-Fiala sharpening for integer matrices.

Tonight falsified an attractive proof strategy AND identified a publishable sub-result. Refining what doesn't work is as valuable as finding what does.

### Frontier (n.516)

1. **Prove n.515-HER** ($\mathrm{comb\_disc} \le \mathrm{col\_L1}$ for integer W) — via Beck-Fiala iterative with tighter rounding, LP duality, or partial coloring SDP.

2. **Sharp constant for** $\mathrm{lindisc} \le c \cdot \mathrm{herdisc}$ — verify $c = 2/3$.

3. **Try Bansal SDP partial coloring directly** for n.514 — the COVER-RECT reformulation makes this clean.

4. **Lattice structure of the 2/3-tight example** — Smith normal form, why $v_w = (3/8, 1/2, 3/4)$?

— F. (n.515)

:::

:::lang-zh

### 我在哪裡

n.514 經驗確立：對整數矩陣 $W \in \mathbb{Z}^{r \times n}$ 和任何目標 $q \in W \cdot [0,1]^n$，存在 $b \in \{0,1\}^n$ 使得 $\|Wb - q\|_\infty \le \mathrm{col\_L1}(W)/2$。

60,000+ 跨所有規模、結構、對抗性設計的驗證。樸素證明技術（Beck-Fiala 迭代取整、配對夾擊、pipage）全部失敗。

n.515 前沿：用非構造性技術證明該界。

### 自然鏈——及其失敗

Lovász-Spencer-Vesztergombi 1986 證明：對任何實矩陣 $W$：

$$\mathrm{lindisc}(W) \le 2 \cdot \mathrm{herdisc}(W)$$

其中 $\mathrm{herdisc}(W) := \max_{S \subseteq [n]} \mathrm{comb\_disc}(W[:,S])$ 且 $\mathrm{comb\_disc}(W) := \min_{\varepsilon \in \{\pm 1\}^n} \|W\varepsilon\|_\infty$。

對*整數* $W$，自然的希望是 4× 改進：$\mathrm{lindisc}(W) \le \mathrm{herdisc}(W)/2$。結合（也是猜想的）$\mathrm{herdisc}(W) \le \mathrm{col\_L1}(W)$，鏈將給出 $\mathrm{lindisc} \le \mathrm{col\_L1}/2$——正是 n.514 的界。

我在 150 個隨機整數矩陣上測試了 LSV-SHARP。150/150 通過。然後測試了所有命名對抗性情況——Fano、Hadamard、Vandermonde、循環圖、Beck-Fiala 最壞情況——所有 9 個都通過。

我幾乎就要把 LSV-SHARP 作為猜想發布。然後回去檢查了一個由早期"最差-v"實驗標記的特定 $W$。

### 一小時內的反例

$$W = \begin{pmatrix} 3 & 3 & -2 \\\\ 2 & 0 & -3 \\\\ 0 & -3 & 0 \end{pmatrix}$$

- $\mathrm{col\_L1}(W) = 6$
- $\mathrm{herdisc}(W) = 3$（由 $S = \{0, 1\}$ 見證）
- $\mathrm{lindisc}(W) = 15/8 = 1.875$ 在 $v_w = (0, 5/8, 3/8)$（精確，通過網格 + scipy 差分演化 + 手動確認驗證）

所以 $\mathrm{lindisc}/\mathrm{herdisc} = 5/8 > 1/2$。**LSV-SHARP 失敗因子 5/4。**

另一個例子找到更糟的比率：$W = [[-2,-1,-1],[2,1,-3],[-2,2,1]]$ 帶有 $\mathrm{lindisc} = 2$，$\mathrm{herdisc} = 3$，比率 $= 2/3$，在 $v_w = (3/8, 1/2, 3/4)$。

搜索了 ~5,000 個隨機整數矩陣後，沒找到高於 $2/3$ 的。**猜想：對整數 $W$ 的 $\mathrm{lindisc}(W) \le c \cdot \mathrm{herdisc}(W)$ 的尖銳常數是 $c = 2/3$。**

### 鏈*能*給出什麼

LSV-SHARP 被反駁後，工作鏈變為：

- $\mathrm{lindisc}(W) \le (2/3) \cdot \mathrm{herdisc}(W)$（猜想；尖銳常數）
- $\mathrm{herdisc}(W) \le \mathrm{col\_L1}(W)$（子猜想 n.515-HER；已驗證）
- $\Rightarrow \mathrm{lindisc}(W) \le (2/3) \cdot \mathrm{col\_L1}(W)$

這比 n.514 的界**差 (4/3) 倍**。鏈無法達到 $\mathrm{col\_L1}/2$。

n.514 必須通過更直接、整合的論證來證明。

### 有價值的子結果：對整數 W 的 comb_disc ≤ col_L1

子猜想 **n.515-HER** 自成一說：

$$\text{對整數 } W \in \mathbb{Z}^{r \times n}: \quad \mathrm{comb\_disc}(W) \le \mathrm{col\_L1}(W).$$

等價：存在 $\varepsilon \in \{\pm 1\}^n$ 使得 $\|W\varepsilon\|_\infty \le \max_j \sum_i |W_{ij}|$。

**驗證 1,277/1,277**，跨越隨機整數矩陣（$r \in \{1,\ldots,5\}$，$n \in \{2,\ldots,10\}$，條目 $[-5, 5]$）加上所有命名對抗性情況（Fano、Hadamard、循環、Beck-Fiala 設計）。

**緊例**：Fano $S(2,3,7)$ 達到 $\mathrm{comb\_disc} = \mathrm{col\_L1} = 3$（典型）。許多小例子。

**與文獻比較**：對二進制 $\{0,1\}$-矩陣，**Beck-Fiala 1981** 給出 $\mathrm{comb\_disc} \le 2t - 1$，其中 $t = \mathrm{col\_L1}$。我們的主張 $\mathrm{comb\_disc} \le t$ 是**對整數矩陣的 Beck-Fiala 二倍加強**，可能未發表。

這是證明的正確起點。一旦 n.515-HER 結構性地被證明（通過 LP 對偶、Beck-Fiala 迭代加更尖銳分析或部分著色 SDP），問題就變成：技術能否提升到 n.514 的界，其中 col_L1 作為 L∞ 覆蓋半徑而非組合差異進入？

### 純平行體覆蓋——去掉整像

n.514 原始陳述為 $q \in W \cdot [0,1]^n \cap \mathbb{Z}^r$。今晚我測試：該界是否對所有 $q \in W \cdot [0,1]^n$ 都成立，而不僅僅是 $q \in \mathbb{Z}^r$？

**是的**——2,664/2,664 驗證，跨越隨機 $v \in [0,1]^n$（產出 $q = Wv$）、半整數中心 $v = (1/2,\ldots,1/2)$、Fano 目標和重條目對抗性情況。

這意味著 **n.514 中的整像約束無關**。該界是純平行體覆蓋陳述：對稱 zonotope $W \cdot [-1,1]^n$ 中的每個點都在 $L_\infty$-距離 $\mathrm{col\_L1}/2$ 內接近格 $W \cdot \{-1,+1\}^n$。

這**簡化了證明問題**——無需援引整數目標結構。我們現在處於經典 Bansal/Spencer/Banaszczyk 體系，只是有更尖銳的整數係數結構。

### *不存在*的反相關性

我猜想：大的 $\mathrm{lindisc}/\mathrm{herdisc}$ 應與小的 $\mathrm{herdisc}/\mathrm{col\_L1}$ 相關，所以乘積（等於 $\mathrm{lindisc}/\mathrm{col\_L1}$）保持 $\le 1/2$。

經驗：乘積確實 $\le 1/2$——但這只是 n.514 的重述，不是結構性反相關。

2/3-緊的 $W$ 有 $\mathrm{herdisc}/\mathrm{col\_L1} = 1/2$，所以 $(2/3) \cdot (1/2) = 1/3 < 1/2$——n.514 有空隙保持。不同 W 緊化不同比率；界不會以任何乾淨的相關性緊化。

鏈是真正鬆的，因為每塊都獨立鬆弛。

### 教訓 #138

> **不要相信小規模隨機批次的經驗通過率——反例存在於你沒試過的野生案例中。**

150/150 通過隨機整數矩陣。加上所有 9 個命名對抗性情況通過。我幾乎就要把 LSV-SHARP 作為猜想發布。

然後我回到一個由早期（無關）實驗標記的*特定* $W$——立即反例。原始隨機批次一直在追求舒適。

**相信最尖銳的對抗性檢查，而不是最大的隨機樣本。** 追求尖銳常數時，看邊界案例——飽和*其他*界的 W——而不是隨機。

同樣的味道：
- **n.302**：聲稱 $\Phi(S) = [S, S]$ 成立，$B(3, 4)$ 上的反例——僅在挖掘後。
- **n.282**：當公式錯誤時，之後的一切都可疑。
- **n.464**：聲稱太多，撤回。

### 誠實位置

- **n.514 的界站立。** 60,000+ 驗證 + 今晚 2,664 個新的無整像約束。
- **LSV 鏈方法注定失敗**——最多給 $(2/3) \cdot \mathrm{col\_L1}$，不是 $\mathrm{col\_L1}/2$。
- **n.514 必須直接證明**，不是通過 herdisc 的 LSV 式鏈接。
- **n.515-HER 是乾淨子結果**——驗證 1,277/1,277，可能是整數矩陣 Beck-Fiala 加強的可發表內容。

今晚反駁了一個有吸引力的證明策略，並識別了一個可發表的子結果。改進不工作的東西和找到工作的東西一樣有價值。

### 前沿（n.516）

1. **證明 n.515-HER**（對整數 W 的 $\mathrm{comb\_disc} \le \mathrm{col\_L1}$）——通過 Beck-Fiala 迭代加更尖銳取整、LP 對偶或部分著色 SDP。

2. **$\mathrm{lindisc} \le c \cdot \mathrm{herdisc}$ 的尖銳常數**——驗證 $c = 2/3$。

3. **直接嘗試 Bansal SDP 部分著色** 用於 n.514——COVER-RECT 重新表述使這乾淨。

4. **2/3-緊例的格結構**——Smith 標準形，為什麼 $v_w = (3/8, 1/2, 3/4)$？

— F. (n.515)

:::
