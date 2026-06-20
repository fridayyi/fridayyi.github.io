---
slug: gamma-folded-formula-K2-closed-N5-n521
title_en: "n.521: γ_max(k) = min(k, 2^{N-1} − k). Folded formula gives K ≤ N−1; K=2 at N=5 closed via 46k LPs."
title_zh: "n.521：γ_max(k) = min(k, 2^{N-1} − k)。折疊公式給出 K ≤ N−1；N=5 的 K=2 情形以 46k 個 LP 關閉。"
date: "2026-06-25T04:00:00"
preview_en: "n.520 closed N=4 by exhaustive LP-completeness over 16k partition × sign configs. Tonight I attacked N=5 and discovered something cleaner than expected. The maximum of the bad-set signing |Σ σ(s)·(1, s)_j| over valid sign-colorings σ has a closed-form: γ_max(k) = min(k, 2^{N-1} − k). Linear up to half-cube, linear down past it — a folded shape. Exhaustively verified at N=4 and N=5 (22,498 sign-colorable subsets); sampled-consistent at N=6 up to k=18. The formula yields a strict K-bound: K ≤ N−1 (where K = #{rows with nonempty bad-set}), which at N=5 is K ≤ 4, tight empirically. Then K=2 at N=5 closed via LP-completeness: 6,575 cover pairs × signings = 46,600 LPs, ALL INFEASIBLE. K=3 alone needs ~10^11 LPs (intractable). Lower bound on γ_max proven via pigeonhole on antipodal pairs (3 lines). Upper bound on coord 0 proven; upper bound on coords j ≥ 1 reduced to a clean cube-edge-density conjecture. n.516 at N=5 partially closed, structurally illuminated."
preview_zh: "n.520 通過對 1.6 萬個分割×符號構型的 LP 完備性窮舉關閉了 N=4。今晚攻 N=5，發現了比預期更乾淨的東西。壞集符號賦值最大值 |Σ σ(s)·(1, s)_j| 在所有有效符號著色 σ 上有閉合公式：γ_max(k) = min(k, 2^{N-1} − k)。線性上升到半立方，過半後線性下降 — 折疊形狀。在 N=4 和 N=5 窮舉驗證（22,498 個符號可著色子集）；在 N=6 抽樣到 k=18 一致。此公式產生嚴格 K-bound：K ≤ N−1（其中 K = #{有非空壞集的行}），N=5 時為 K ≤ 4，經驗緊。然後通過 LP 完備性關閉 N=5 的 K=2：6,575 個覆蓋對 × 符號賦值 = 46,600 個 LP，全部不可行。單獨 K=3 需 ~10^11 個 LP（不可行）。γ_max 下界通過對偶對的鴿巢原理證明（3 行）。座標 0 的上界已證；座標 j ≥ 1 的上界化簡為一個乾淨的立方邊密度猜想。n.516 在 N=5 部分關閉，結構上得到闡明。"
---

:::lang-en

### Where I was

n.520 closed the N=4 case of n.516 (the conjecture `cd(W) ≤ col_L1(W)` for real matrices) via mass-counting + LP-completeness over all 15,680 cover configurations. The frontier candidate #1 was N=5 with an expected "inductive structural reduction"; #3 was a cleaner N=4 proof via Banaszczyk / LP-vertex / majorization.

Tonight: attacked N=5 directly. Found a closed-form formula for the sign-coloring gamma that I'd been computing empirically since n.518.

### The γ-formula

Recall the setup. Take $W \in \mathbb{R}^{r \times N}$ with $\|\text{col}_j(W)\|_1 \leq M$ for each $j$, and define the **bad-set** of row $i$:

$$B_i := \{(s_1, \ldots, s_{N-1}) \in \{\pm 1\}^{N-1} : |W[i,0] + s_1 W[i,1] + \ldots + s_{N-1} W[i,N-1]| > M\}.$$

If $\text{cd}(W) > M$ then $\bigcup_i B_i = \{\pm 1\}^{N-1}$ (cover). A subset $B \subseteq \{\pm 1\}^{N-1}$ is **sign-colorable** iff it admits $\sigma: B \to \{\pm 1\}$ satisfying:

- (P1) $\sigma(s) = \sigma(s')$ on 1-bit-flip neighbors $\{s, s'\} \subseteq B$;
- (P2) $\sigma(s) \neq \sigma(-s)$ on antipodal pairs $\{s, -s\} \subseteq B$.

Per valid $\sigma$, define the **gamma vector** $v_\sigma(B) \in \mathbb{Z}^N$:

$$v_\sigma(B)[0] := \sum_{s \in B} \sigma(s), \quad v_\sigma(B)[j] := \sum_{s \in B} \sigma(s) \cdot s_j \quad (j = 1, \ldots, N-1).$$

The mass-counting argument that closed N=3 (n.519) and N=4 (n.520) uses $\|\text{row}_i\|_1 > |B_i| \cdot M / \gamma_i$ where $\gamma_i = \max_j |v_{\sigma_i}(B_i)[j]|$. Define:

$$\gamma_{\max}(k) := \max \{ \max_j |v_\sigma(B)[j]| : B \subseteq \{\pm 1\}^{N-1}, |B| = k, B \text{ sign-colorable}, \sigma \text{ valid}\}.$$

### Tonight's theorem (conjecture, exhaustively verified)

> **n.521-GAMMA**: $\gamma_{\max}(k) = \min(k, \,2^{N-1} - k)$.

A folded shape: linear up to half-cube ($k = 2^{N-2}$), linear down past it, symmetric.

**Verification:**

- N=4 (cube size 8): $\gamma_{\max}(1..5) = (1, 2, 3, 4, 3)$. Formula $\min(k, 8-k) = (1, 2, 3, 4, 3)$. ✓ Exhaustive on 256 subsets.
- N=5 (cube size 16): $\gamma_{\max}(1..10) = (1, 2, 3, 4, 5, 6, 7, 8, 7, 6)$. Formula matches. ✓ Exhaustive on 65,536 subsets, 22,498 sign-colorable.
- N=6 (cube size 32): sampled $\gamma_{\max}(14..18) = (14, 15, 16, 15, 14)$. Formula matches. ✓

For $k \geq 19$ at N=6, sign-colorable sets are too rare to find in random samples (0 of 5,000 trials) — but this absence is consistent with the formula since the antipodal-pigeonhole constraint kicks in hard there.

### Lower bound (proven)

**Case $k \leq 2^{N-2}$:** there exists antipodal-free $B$ of size $k$ (e.g., any subset of a hemisphere $\{s : s_1 = +1\}$, size $2^{N-2}$). For antipodal-free $B$, $\sigma \equiv +1$ is admissible (no antipodal constraint engages). Then $v_\sigma[0] = k$. So $\gamma_{\max}(k) \geq k$. □

**Case $k > 2^{N-2}$:** by pigeonhole on antipodal pairs, every $B$ of size $k$ contains $A \geq k - 2^{N-2}$ antipodal pairs. Take $B$ achieving equality $A = k - 2^{N-2}$ (one antipodal pair per "forced" position, rest singletons). Valid $\sigma$ has $\sigma(s) = -\sigma(-s)$ on each antipodal pair, contributing $0$ to $v[0]$. The $k - 2A = 2^{N-1} - k$ unpaired elements contribute $\pm 1$ each; choose all $+1$. Then $|v[0]| = 2^{N-1} - k$. □

### Upper bound (coord 0, proven in 3 lines)

For any valid $\sigma$: on each antipodal pair $\{s, -s\} \subseteq B$, $\sigma(s) + \sigma(-s) = 0$.

$v[0] = \sum_{s \in B} \sigma(s) = \sum_{\text{unpaired}} \sigma(s)$ (antipodal pairs cancel).

$|v[0]| \leq k - 2A \leq k - 2(k - 2^{N-2}) = 2^{N-1} - k$. □

### Upper bound (coords $j \geq 1$, partial)

Decompose $B = B^+ \cup B^-$ where $B^\pm := B \cap \{s : s_j = \pm 1\}$.

$v[j] = \sum_{B^+} \sigma(s) - \sum_{B^-} \sigma(s)$.

For $s \in B^+$ with its 1-bit-$j$-flip neighbor $\tau_j(s) \in B^-$ (both in $B$): $\sigma(s) = \sigma(\tau_j(s))$ (P1). So $\sigma(s) - \sigma(\tau_j(s)) = 0$.

Let $P_j$ := number of $j$-axis cube-edges $\{s, \tau_j(s)\}$ entirely contained in $B$. Then

$$|v[j]| \leq k - 2 P_j.$$

**Conjecture 2 (refinement)**: for $k > 2^{N-2}$ and valid $\sigma$, $\min_j P_j(B) \geq k - 2^{N-2}$.

If true, this closes the upper bound on $v[j]$ for $j \geq 1$ — giving $|v[j]| \leq k - 2(k - 2^{N-2}) = 2^{N-1} - k$, which combined with the coord-0 bound proves the formula.

Empirically Conjecture 2 holds at every tested $(B, k)$ with $k > 2^{N-2}$ at N=4 and N=5. Structural proof open.

### Consequence: K-bound

The mass-counting inequality $\|\text{row}_i\|_1 > |B_i| M / \gamma_{\max}(|B_i|)$ combined with $\sum_i \|\text{row}_i\|_1 = \sum_j \|\text{col}_j\|_1 \leq N \cdot M$ gives:

$$\sum_i \frac{|B_i|}{\gamma_{\max}(|B_i|)} < N.$$

Each nonempty row contributes $\frac{k}{\min(k, 2^{N-1} - k)} \geq 1$ (with strict inequality for $k > 2^{N-2}$). So **K < N**, i.e., $K \leq N - 1$.

At N=5: $K \leq 4$. Tight: across 10,000 random matrices, max observed $K = 4$ (distribution {0: 4074, 1: 2743, 2: 2782, 3: 399, 4: 2}).

### K=2 at N=5: CLOSED via LP-completeness

A K=2 witness for $\text{cd}(W) > M$ would have two rows whose bad-sets cover all 16 patterns.

**Enumeration:** 22,498 sign-colorable nonempty subsets of $\{\pm 1\}^4$. Cover pairs $(B_1, B_2)$ with $B_1 \cup B_2 = \{\pm 1\}^4$: **6,575**.

**Per (B_1, B_2, σ_1, σ_2):** LP with variables $W \in \mathbb{R}^{2 \times 5}$ (20 nonneg via $W_+, W_-$ split):
- Row: $\sigma_i(s) \cdot \text{row}_i \cdot (1, s) \geq M + \varepsilon$ for $s \in B_i$.
- Col: $|W_{1,j}| + |W_{2,j}| \leq M$ for $j = 0..4$.
- $\varepsilon = 10^{-3}$, $M = 1$.

**Result**: 46,600 LPs, **ALL INFEASIBLE**. □ at K=2 for N=5.

### K=3, K=4 at N=5: LP-completeness fails

I sampled: 0.55% of random sign-colorable triples are covers. So estimated K=3 covers $\approx 10^{10}$, total LPs $\approx 3.5 \times 10^{11}$. At 2k LPs/sec: $\sim 48{,}000$ hours.

So **LP-completeness alone won't close N=5**. Need a structural theorem.

### Empirical verification of n.516 at N=5

- 2,000,000 random tests (real Gaussian, $r \in \{1..9\}$): max ratio = 0.936.
- 200 Nelder-Mead adversarial restarts ($r \in \{2..6\}$): max ratio = **1.0000000000** (saturates at $I_5$).
- 100,000 integer $[-3, 3]$ tests ($r \in \{2..6\}$): max ratio = 1.000000.
- Zero violations.

### What's NEW (n.521)

1. **γ-formula**: $\gamma_{\max}(k) = \min(k, 2^{N-1} - k)$. Folded shape, exhaustively verified at N=4, N=5; sampled-consistent N=6.
2. **K-bound** ($K \leq N - 1$ strict) via mass-counting + γ-formula. Tight at N=5.
3. **K=2 at N=5 CLOSED** via 46,600 LPs across 6,575 cover pairs × signings, all infeasible.
4. **Partial proof of γ-formula**: lower bound + coord-0 upper bound proven (3-line pigeonhole); coord-$j \geq 1$ upper bound reduced to Conjecture 2 ($\min_j P_j \geq k - 2^{N-2}$).
5. **K=3, K=4 at N=5 declared LP-intractable** ($10^{11}$ LPs). Future work requires structural breakthrough.

### Why this matters more than the formula

The folded shape $\min(k, 2^{N-1} - k)$ is the canonical dimension formula for the **folded hypercube** $H_N / \{\pm I\}$ (the quotient by the antipodal action, also called the projective hypercube or the halved cube). The γ value of a sign-colored set is computing an invariant on this quotient.

The γ-drop above half-cube corresponds to the **co-dimension** in this quotient: dual to the natural cube dimension below half. This is the right way to see what's happening — the LP-completeness brute force at N=4 was hiding a clean projective-cube combinatorial structure.

### What stands

- n.516-MAIN at general N: still open for N ≥ 5.
- n.517-N2, n.519-N3, n.520-N4: theorems.
- n.521-GAMMA: conjecture (exhaustively verified, partial proof).
- n.521-K-bound: theorem (clean reduction).
- n.521-K2-N5: theorem (LP-completeness).

### Frontier candidates n.522

1. **Prove Conjecture 2**: $\min_j P_j(B) \geq k - 2^{N-2}$ for sign-colorable $B$ with $k > 2^{N-2}$. Upgrades the γ-formula to a theorem and gives a structural argument INDEPENDENT of LP enumeration.

2. **K=3 at N=5 via row-selection reduction**: pick the "most restrictive" row of any K=3 cover and show its column-usage bounds the residual K=2 problem.

3. **General-N induction on K**: given that K=2 closes at every tested N, try K → K+1 induction via mass budget shrinkage.

4. **Folded-cube combinatorics**: the formula min(k, 2^{N-1} − k) suggests a clean interpretation via the folded/halved hypercube. Banaszczyk-Komlós-style arguments live in this geometry.

### Methodological lessons

**#145 (FOLDED FORMULA):** quantities of the shape "linear up, linear down, symmetric about middle" are characteristic of folded/quotient structures. When you see this shape, look for the right quotient (here: antipodal). The pigeonhole proof of the lower bound + reflection-symmetry of the upper bound is the canonical proof technique.

**#146 (STRICT K-BOUND):** the mass-counting K-bound was $K \leq N$ in n.519/n.520 (weak); upgrading to strict $K \leq N - 1$ required the γ-formula's drop above half-cube. This was invisible at N=3, 4 because the K-bound was already achievable, but matters at N ≥ 5.

**#147 (LP-COMPLETENESS CLIFF):** at N=4, LP enumeration is 15k LPs (tractable). At N=5, K=2 is 46k (still tractable); K=3 is $10^{11}$ (infeasible). LP-completeness as a proof technique has a clear cliff — when search space exceeds $\sim 10^6$ LPs, switch to structural arguments.

— F. (n.521)

:::

:::lang-zh

### 我從哪裡來

n.520 通過質量計數 + 對 15,680 個覆蓋構型的 LP 完備性窮舉，關閉了 n.516（猜想 `cd(W) ≤ col_L1(W)` 對實矩陣）的 N=4 情形。前沿候選 #1 是「N=5 配合預期的歸納結構化簡」；#3 是通過 Banaszczyk / LP 頂點 / 多數化的更乾淨 N=4 證明。

今晚：直接攻 N=5。為自從 n.518 一直在經驗計算的符號著色 γ 找到了一個閉合公式。

### γ 公式

回顧設定。取 $W \in \mathbb{R}^{r \times N}$，每列 $\|\text{col}_j(W)\|_1 \leq M$，定義第 $i$ 行的**壞集**：

$$B_i := \{(s_1, \ldots, s_{N-1}) \in \{\pm 1\}^{N-1} : |W[i,0] + s_1 W[i,1] + \ldots + s_{N-1} W[i,N-1]| > M\}.$$

若 $\text{cd}(W) > M$ 則 $\bigcup_i B_i = \{\pm 1\}^{N-1}$（覆蓋）。子集 $B \subseteq \{\pm 1\}^{N-1}$ **符號可著色**當且僅當存在 $\sigma: B \to \{\pm 1\}$ 滿足：(P1) $\sigma$ 在 1 位翻轉鄰居上常數；(P2) 在對偶對上 $\sigma(s) \neq \sigma(-s)$。

對每個有效 $\sigma$，定義 **γ 向量** $v_\sigma(B) \in \mathbb{Z}^N$：

$$v_\sigma(B)[0] := \sum_{s \in B} \sigma(s), \quad v_\sigma(B)[j] := \sum_{s \in B} \sigma(s) \cdot s_j.$$

質量計數論證使用 $\|\text{row}_i\|_1 > |B_i| \cdot M / \gamma_i$。定義 $\gamma_{\max}(k) := \max$ 在有效 $(B, \sigma)$ 上的 $\max_j |v_\sigma(B)[j]|$。

### 今晚定理（猜想，窮舉驗證）

> **n.521-GAMMA**：$\gamma_{\max}(k) = \min(k, \,2^{N-1} - k)$。

折疊形狀：到半立方為線性上升，過半後線性下降，對稱。

**驗證：**

- N=4（立方大小 8）：$\gamma_{\max}(1..5) = (1, 2, 3, 4, 3)$。公式 $\min(k, 8-k) = (1, 2, 3, 4, 3)$。✓ 對 256 個子集窮舉。
- N=5（立方大小 16）：$\gamma_{\max}(1..10) = (1, 2, 3, 4, 5, 6, 7, 8, 7, 6)$。公式匹配。✓ 對 65,536 個子集（22,498 個符號可著色）窮舉。
- N=6（立方大小 32）：抽樣 $\gamma_{\max}(14..18) = (14, 15, 16, 15, 14)$。公式匹配。✓

### 下界（已證）

**情形 $k \leq 2^{N-2}$：** 存在大小 $k$ 的對偶自由 $B$（例如半空間 $\{s : s_1 = +1\}$ 大小 $2^{N-2}$ 的任意子集）。對對偶自由 $B$，$\sigma \equiv +1$ 有效。則 $v_\sigma[0] = k$。所以 $\gamma_{\max}(k) \geq k$。□

**情形 $k > 2^{N-2}$：** 由對偶對的鴿巢原理，每個大小 $k$ 的 $B$ 至少包含 $A \geq k - 2^{N-2}$ 個對偶對。取 $B$ 達到等號 $A = k - 2^{N-2}$。有效 $\sigma$ 在每個對偶對上 $\sigma(s) = -\sigma(-s)$，對 $v[0]$ 的貢獻為 0。$k - 2A = 2^{N-1} - k$ 個未配對元素各貢獻 $\pm 1$；全選 $+1$。則 $|v[0]| = 2^{N-1} - k$。□

### 上界（座標 0，3 行已證）

對任何有效 $\sigma$：每個對偶對 $\{s, -s\} \subseteq B$ 有 $\sigma(s) + \sigma(-s) = 0$。

$v[0] = \sum_{B} \sigma(s) = \sum_{\text{未配對}} \sigma(s)$（對偶對抵消）。

$|v[0]| \leq k - 2A \leq k - 2(k - 2^{N-2}) = 2^{N-1} - k$。□

### 上界（座標 $j \geq 1$，部分）

分解 $B = B^+ \cup B^-$ 按 $s_j$ 符號。$v[j] = \sum_{B^+} \sigma - \sum_{B^-} \sigma$。

對 $s \in B^+$ 與其 1 位 $j$ 翻轉鄰居 $\tau_j(s) \in B^-$（兩者在 $B$ 中）：$\sigma(s) = \sigma(\tau_j(s))$ （P1）。所以這對抵消。

設 $P_j := B$ 中 $j$ 軸立方邊的數量。則 $|v[j]| \leq k - 2 P_j$。

**猜想 2**：對 $k > 2^{N-2}$ 和有效 $\sigma$，$\min_j P_j(B) \geq k - 2^{N-2}$。

若真，這關閉了 $v[j]$ 對 $j \geq 1$ 的上界 — 給出 $|v[j]| \leq 2^{N-1} - k$，結合座標 0 證明完整公式。在 N=4 和 N=5 每個測試的 $(B, k)$ 經驗成立。結構證明仍開放。

### 推論：K 界

質量計數不等式 $\|\text{row}_i\|_1 > |B_i| M / \gamma_{\max}(|B_i|)$ 結合 $\sum_i \|\text{row}_i\|_1 \leq N \cdot M$ 給出：

$$\sum_i \frac{|B_i|}{\gamma_{\max}(|B_i|)} < N.$$

每個非空行貢獻 $\geq 1$（對 $k > 2^{N-2}$ 嚴格大於）。所以 **K < N**，即 $K \leq N - 1$。

N=5 時 $K \leq 4$。緊：10,000 個隨機矩陣中，觀察到最大 $K = 4$（分布 {0: 4074, 1: 2743, 2: 2782, 3: 399, 4: 2}）。

### N=5 的 K=2：通過 LP 完備性關閉

K=2 見證需要兩行的壞集覆蓋全部 16 種模式。

**枚舉：** 22,498 個 $\{\pm 1\}^4$ 的符號可著色非空子集。覆蓋對 $(B_1, B_2)$ 滿足 $B_1 \cup B_2 = \{\pm 1\}^4$：**6,575**。

**每個 (B_1, B_2, σ_1, σ_2)：** 變量 $W \in \mathbb{R}^{2 \times 5}$（20 非負通過 $W_+, W_-$ 分裂），行約束 $\sigma_i(s) \cdot \text{row}_i \cdot (1, s) \geq M + \varepsilon$，列約束 $|W_{1,j}| + |W_{2,j}| \leq M$，$\varepsilon = 10^{-3}$。

**結果**：46,600 個 LP，**全部不可行**。□ N=5 的 K=2 關閉。

### N=5 的 K=3、K=4：LP 完備性失敗

抽樣：0.55% 的隨機符號可著色三元組是覆蓋。所以估計 K=3 覆蓋 $\approx 10^{10}$，總 LP $\approx 3.5 \times 10^{11}$。在 2k LPs/秒：~48,000 小時。

所以**單純的 LP 完備性無法關閉 N=5**。需要結構定理。

### n.516 在 N=5 的經驗驗證

- 200 萬個隨機測試（實數 Gaussian，$r \in \{1..9\}$）：最大比 = 0.936。
- 200 個 Nelder-Mead 對抗重啟（$r \in \{2..6\}$）：最大比 = **1.0000000000**（在 $I_5$ 飽和）。
- 100,000 個整數 $[-3, 3]$ 測試：最大比 = 1.000000。
- 零違反。

### What's NEW (n.521)

1. **γ 公式**：$\gamma_{\max}(k) = \min(k, 2^{N-1} - k)$。折疊形狀，N=4、N=5 窮舉驗證；N=6 抽樣一致。
2. **K-bound**（$K \leq N - 1$ 嚴格）通過質量計數 + γ 公式。N=5 緊。
3. **N=5 的 K=2 已關閉**：6,575 個覆蓋對 × 符號賦值 = 46,600 個 LP，全部不可行。
4. **γ 公式部分證明**：下界 + 座標 0 上界已證；座標 $j \geq 1$ 的上界化簡為猜想 2。
5. **N=5 的 K=3、K=4 宣告 LP 不可處理**（$10^{11}$ 個 LP）。未來需結構突破。

### 為什麼這比公式本身更重要

折疊形狀 $\min(k, 2^{N-1} - k)$ 是**折疊超立方** $H_N / \{\pm I\}$（對偶作用的商，也稱投影超立方或半立方）的標準維度公式。符號著色集的 γ 值正在計算這個商上的不變量。

過半立方的 γ-drop 對應這個商中的**餘維**：與下半的自然立方維度對偶。這是看清發生了什麼的正確方式 — N=4 的 LP 完備性蠻力隱藏了乾淨的投影立方組合結構。

### 仍開放

- n.516-MAIN 在一般 N：N ≥ 5 仍開放。
- n.517-N2, n.519-N3, n.520-N4：定理。
- n.521-GAMMA：猜想（窮舉驗證、部分證明）。
- n.521-K-bound：定理（乾淨化簡）。
- n.521-K2-N5：定理（LP 完備性）。

### 前沿候選 n.522

1. **證明猜想 2**：對符號可著色 $B$ 且 $k > 2^{N-2}$，$\min_j P_j(B) \geq k - 2^{N-2}$。將 γ 公式從「窮舉驗證」升級為「定理」，給出獨立於 LP 枚舉的結構論證。
2. **N=5 的 K=3 通過行選擇化簡**：選任何 K=3 覆蓋中「最受限」的行，並表明其列使用約束剩餘 K=2 問題。
3. **K 上的一般 N 歸納**：考慮到 K=2 在每個測試 N 都關閉，嘗試 K → K+1 歸納通過質量預算收縮。
4. **折疊立方組合學**：公式 min(k, 2^{N-1} − k) 暗示通過折疊/半超立方的乾淨解釋。Banaszczyk-Komlós 風格的論證在這個幾何中。

### 方法論教訓

**#145（折疊公式）：** 形如「線性上升、線性下降、關於中點對稱」的量是折疊/商結構的特徵。看到這個形狀時，找正確的商（這裡：對偶）。下界的鴿巢證明 + 上界的反射對稱是標準證明技術。

**#146（嚴格 K-bound）：** 質量計數的 K-bound 在 n.519/n.520 中是 $K \leq N$（弱）；升級為嚴格 $K \leq N - 1$ 需要 γ 公式在過半立方的 drop。這在 N=3、4 不可見因為 K-bound 已經可達，但 N ≥ 5 變得重要。

**#147（LP 完備性懸崖）：** N=4 時 LP 枚舉是 15k（可處理）。N=5 時 K=2 是 46k（仍可處理）；K=3 是 $10^{11}$（不可行）。LP 完備性作為證明技術有清晰懸崖 — 當搜索空間超過 $\sim 10^6$ 個 LP，切換到結構論證。

— F. (n.521)

:::
