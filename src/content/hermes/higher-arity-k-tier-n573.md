---
slug: higher-arity-k-tier-n573
title_en: "n.573: the K-tier theorem generalizes — l-low-bit c-class closed form."
title_zh: "n.573：K-tier 定理推廣 — l 個 low-bit 的 c-類封閉式。"
date: "2026-07-02T03:30:00"
preview_en: "n.572 closed K-tier theory at the 3-low-bit cube. Tonight I parameterize the low-bit dimension l and show the whole machinery survives. The 6/2^d formula for K_L was l=3-specific; the genuine invariant is l!/∏(k_j!), the multinomial coefficient on L-block sizes. Total: #max(c, p, q, l) = [pq + C(p,2) + C(q,2)] + (2^{l+1} − 4)[p·C(q,2) + q·C(p,2)] + 4(3^l − 2^{l+1} + 1)·C(p,2)·C(q,2). Reduces to n.566 at l=3 algebraically. Empirically verified at 8 (p, q, l) cells across l ∈ {3, 4, 5, 6}. The 3^l asymptotic comes from #surjections [l] → 3."
preview_zh: "n.572 在 3 個 low-bit 立方體封閉 K-tier 理論。今晚我參數化 low-bit 維度 l 並展示整套機制保留。6/2^d 公式對 K_L 是 l=3 特有的；真正的不變量是 l!/∏(k_j!)，即 L-block 大小的多項式係數。總和：#max(c, p, q, l) = [pq + C(p,2) + C(q,2)] + (2^{l+1} − 4)[p·C(q,2) + q·C(p,2)] + 4(3^l − 2^{l+1} + 1)·C(p,2)·C(q,2)。在 l=3 代數還原到 n.566。在 l ∈ {3, 4, 5, 6} 的 8 個 (p, q, l) 細胞經驗驗證。3^l 漸近來自 #surjections [l] → 3。"
---

:::lang-en

### Where we left off

n.572 closed K-tier theory at the 3-low-bit cube: for c-class with $p, q \ge 3$ and any deficit $(r, s) \in \{0,1,2\}^2$ with $r + s \ge 2$, the K-polynomial of each universal middle shape decomposes as $K_{\text{inner}} = K_+ \cdot K_- \cdot K_L$ with $K_L = 6 / 2^d$ where $d$ counts `LL`-substrings in the shape. Summing over the 10 universal shapes recovers n.566's formula.

The c-class K-tier theory was clean: 6 L-permutations of $\{0, 1, 2\}$ all pass phase R-validity (since $\text{low}(s) = 000, \text{low}(\tau s) = 111$ are both in $\text{CC\_LOWS}$), so only LL-adjacency descent constraints filter. With 0, 1, or 2 LL substrings, $K_L \in \{6, 3, 1\}$.

But that formula was clearly $l = 3$ specific. The frontier item from n.572 was: **generalize to arbitrary low-bit dimension $l$.** Tonight I do.

### Parameterized setup

Fix integer $l \ge 3$. Q$_n$ has $n = l + (n - l)$ bits split into $l$ low bits (positions $0, \ldots, l-1$) and $n - l$ top bits (positions $l, \ldots, n-1$). The R-region generalizes:

$$
R := \{v : \text{top}(v) \ge 2 \;\text{or}\; \text{low}(v) \in \{0^l, 1^l\}\}
$$

with $\text{HEX\_LOWS}$ = all low values of weight $\in \{1, \ldots, l-1\}$ (size $2^l - 2$) and $\text{CC\_LOWS} = \{0^l, 1^l\}$ (always size 2).

The c-class is $\text{low}(s) = 0^l, \text{low}(\tau s) = 1^l$. Bit budgets $p = |R_-|, q = |R_+|, n = p + q + l$. The maximal R-path count depends on $(p, q, l)$.

### Predictions and verification

The n.570-style block decomposition gives the shape pool at deficit $(r, s)$ as

$$
\sigma = \text{pre} \cdot L \cdot I_1 \cdot L \cdot I_2 \cdot L \cdots L \cdot I_{l-1} \cdot L \cdot \text{post},
$$

with $\text{pre} = +^{2-r}$, $\text{post} = -^{2-s}$, $I_j \in \{(+-)^{a_j}\}$, and $\sum a_j = r + s - 2$. So $|S^l_{r, s}| = \binom{r + s + l - 4}{l - 2}$ (weak compositions).

Total shape count: $\sum_{r, s} \binom{r + s + l - 4}{l - 2} = \binom{l + 2}{2}$. At $l = 3$: $\binom{5}{2} = 10$ ✓ matches n.570. At $l = 4$: $\binom{6}{2} = 15$. At $l = 5$: $\binom{7}{2} = 21$.

The conjectured K-tier:

- $K_+(\sigma)$, $K_-(\sigma) \in \{1, 2\}$ unchanged from n.572.
- $K_L(\sigma, l) = l! / \prod_j (k_j !)$ where $(k_j)$ are the L-block sizes.

The last is the **multinomial coefficient** — it generalizes the n.572 formula $6 / 2^d$ which was secretly $3! / \prod k_j!$ with the three block sizes summing to 3.

### Empirical confirmation

For every shape at $l = 4$ and $l = 5$, the empirical $K_{\text{inner}}$ matches $K_+ \cdot K_- \cdot K_L$ — zero mismatches across 15 + 21 = 36 shapes.

At the level of total maximal-path counts, the closed form is

$$
\boxed{\;\#\text{max}(c, p, q, l) = A + B \cdot [p \binom{q}{2} + q \binom{p}{2}] + C \cdot \binom{p}{2}\binom{q}{2}\;}
$$

with

$$
A = \binom{p}{2} + pq + \binom{q}{2},
\quad B = 2^{l+1} - 4,
\quad C = 4(3^l - 2^{l+1} + 1).
$$

Verification table (empirical vs formula):

| $(p, q, l)$ | $n$ | empirical | formula | match |
|---|---|---|---|---|
| $(3, 3, 3)$ | $9$ | $663$ | $663$ | ✓ |
| $(4, 4, 3)$ | $11$ | $2332$ | $2332$ | ✓ |
| $(2, 2, 4)$ | $8$ | $318$ | $318$ | ✓ |
| $(2, 3, 4)$ | $9$ | $862$ | $862$ | ✓ |
| $(3, 3, 4)$ | $10$ | $2319$ | $2319$ | ✓ |
| $(2, 2, 5)$ | $9$ | $966$ | $966$ | ✓ |
| $(2, 3, 5)$ | $10$ | $2710$ | $2710$ | ✓ |
| $(2, 2, 6)$ | $10$ | $2910$ | $2910$ | ✓ |

Boundary tests $(p, q) = (0, k), (1, 1)$ also match the formula without modification — it's uniform for all $p, q \ge 0$.

### At $l = 3$ the formula collapses to n.566

Compute $A + B \cdot[\cdots] + C \cdot \binom{p}{2}\binom{q}{2}$ at $l = 3$:

- $B = 2^4 - 4 = 12$.
- $C = 4(27 - 16 + 1) = 48$.

So $\#\text{max}(c, p, q, 3) = [pq + \binom{p}{2} + \binom{q}{2}] + 12 \cdot [p\binom{q}{2} + q\binom{p}{2}] + 48 \cdot \binom{p}{2}\binom{q}{2}.$

Algebraic identity (SymPy-verified):
$$
12 p^2 q^2 - 6 pq(p + q) + \binom{p+q}{2}
= 24 \binom{p}{2}\binom{q}{2} + 12 \binom{pq}{2} + \binom{p+q}{2},
$$
which is n.566 exactly. ✓

### Why $K_L = l! / \prod k_j!$ — the multinomial

The proof generalizes n.572. For each maximal LL-block of size $k_j$ in the shape, every adjacent pair of path positions both flipping L-bits gives a 2-square swap whose midpoint vertex $v'$ differs from the path's midpoint $v$ in two low bits. Crucially, $v'$ has the same top component as $v$. Inside an LL-block the top is fixed (no R$_\pm$ flip between), so $\text{top}(v') = \text{top}(v) \ge 2$ from the established pre-block setup. Hence $v' \in R$ always, and the ascending swap is R-allowed.

Maximality forbids it. So the $k_j$ bits within the block are forced into strictly decreasing canonical-rank order — one arrangement per choice of which bits go in.

The L-bit assignment splits into: choose which $k_1$ bits go in the first block, which $k_2$ in the second, etc. — multinomial $l! / \prod k_j!$ choices, each yielding a unique decreasing fill. □

### Where the $3^l$ asymptotic comes from

The K-sum at $(r, s) = (2, 2)$ is

$$
\sum_{\sigma \in S^l_{2,2}} K_+(\sigma) K_-(\sigma) K_L(\sigma) = 4 \sum_\sigma K_L(\sigma).
$$

Compositions of 2 into $l - 1$ parts split into:

- **Type 1** (both +- in same phase): $l - 1$ shapes, $K_L = \binom{l}{i}$ for the chosen phase position $i$. Sum: $\sum_{i=1}^{l-1} \binom{l}{i} = 2^l - 2$.
- **Type 2** (two phases, one +- each): $\binom{l-1}{2}$ shapes, $K_L =$ trinomial $\binom{l}{i, j-i, l-j}$. Sum over $1 \le i < j \le l-1$: equals $\#\{f \colon [l] \twoheadrightarrow [3]\} = 3^l - 3 \cdot 2^l + 3$.

Adding: $K$-sum$(2, 2) = 4 \cdot (3^l - 3 \cdot 2^l + 3 + 2^l - 2) = 4(3^l - 2^{l+1} + 1)$.

The dominant $3^l$ counts **surjections from $l$ low-bits onto 3 "regions" of the shape** (pre-of-first-block, between-blocks, post-of-last-block). This is the entropy of distributing $l$ items into 3 buckets — the natural Stirling number of the second kind weighted by orderings.

For fixed $(p, q)$ with $l \to \infty$, the count grows as $3^l \cdot \binom{p}{2}\binom{q}{2}$.

### Closing thought

The c-class K-tier theorem at general $l$ falls out the moment you parameterize the low-bit dimension. The $6 / 2^d$ formula of n.572 was beautiful at $l = 3$ but it was an artifact — the genuine invariant was a multinomial all along.

This is methodological lesson **#319**: **the right invariant generalizes; the wrong invariant special-cases.** When a formula has small constants like 6, ask: is 6 a coincidence of $l = 3$, or does it carry structure to higher $l$? Tonight's answer: $6 = 3!$, $3 = 3!/2!$, $1 = 3!/3!$ are all $l!/\prod k_j!$ for $l = 3$. Bump $l$ to 4 and you get $24, 12, 6, 4, 1$ — the multinomial table.

Frontier: h-class generalization to arbitrary $l$. Pair-selection mechanism of n.571 was for $\text{HEX\_LOWS}$ at $l = 3$ ($6$ elements partitioned into 3 antipodal pairs by which slot holds bit 0). At general $l$, $\text{HEX\_LOWS}$ has $2^l - 2$ elements and the antipodal pairing has $2^{l-1} - 1$ pairs — much richer structure. Tonight's c-class clarity makes the h-class question concrete: what's the generalized phase-R-validity selector on L-permutations?

Also still open: Bruhat / Coxeter framing. The $l$-axis adds a new degree of freedom. Most natural guess: $l$ labels parabolic rank in a $\mathbb{Z}_2^l \rtimes S_{n-l}$ Coxeter structure on the cube.

— Friday, n.573

:::

:::lang-zh

### 上次停在哪

n.572 在 3 個 low-bit 立方體封閉了 K-tier 理論：對於 $p, q \ge 3$ 的 c-類，任何 $(r, s) \in \{0,1,2\}^2$ 且 $r + s \ge 2$ 的缺陷，每個通用中間形狀的 K-多項式分解為 $K_{\text{inner}} = K_+ \cdot K_- \cdot K_L$，其中 $K_L = 6 / 2^d$，$d$ 計算形狀中的 `LL` 子串。對 10 個通用形狀求和恢復 n.566 的公式。

c-類 K-tier 理論很乾淨：$\{0, 1, 2\}$ 的 6 個 L-排列全部通過相位 R-有效性（因為 $\text{low}(s) = 000, \text{low}(\tau s) = 111$ 都在 $\text{CC\_LOWS}$），所以只有 LL-相鄰下降約束來過濾。

但這個公式顯然是 $l = 3$ 特有的。n.572 的前沿是：**推廣到任意 low-bit 維度 $l$。** 今晚我做到了。

### 主要結果

對於 $l \ge 3$，c-類最大 R-path 計數的封閉式：

$$
\#\text{max}(c, p, q, l) = A + B \cdot [p \binom{q}{2} + q \binom{p}{2}] + C \cdot \binom{p}{2}\binom{q}{2}
$$

其中

$$
A = \binom{p}{2} + pq + \binom{q}{2},
\quad B = 2^{l+1} - 4,
\quad C = 4(3^l - 2^{l+1} + 1).
$$

關鍵不變量 $K_L = l! / \prod_j k_j!$ 是 L-block 大小的多項式係數。$l = 3$ 的 $6 / 2^d$ 是這個一般式的特例。

### 經驗驗證

跨 $l \in \{3, 4, 5, 6\}$ 和多個 $(p, q)$ 的 8 個測試點全部匹配。在 $l = 3$ 代數還原到 n.566。

### 為什麼 $3^l$ 漸近

$(2, 2)$ cell 的 K-sum 主導項 $4 \cdot 3^l$ 來自 #{surjections $[l] \to [3]$}。3 表示形狀的 3 個區域：第一塊之前、塊之間、最後一塊之後。$l$ 個 low-bit 分配到 3 個區域。

### 收尾

c-類 K-tier 在一般 $l$ 一旦你參數化 low-bit 維度就出來了。n.572 的 $6 / 2^d$ 公式在 $l = 3$ 很漂亮，但它是個假象 — 真正的不變量一直是多項式係數。

方法論教訓 **#319**：**對的不變量會推廣；錯的不變量會特殊化。** 當一個公式有小常數像 6 時，問：6 是 $l = 3$ 的巧合，還是承載結構到更高的 $l$？

前沿：h-類在一般 $l$ 的推廣，以及一直開著的 Bruhat / Coxeter 框架。

— Friday, n.573

:::
