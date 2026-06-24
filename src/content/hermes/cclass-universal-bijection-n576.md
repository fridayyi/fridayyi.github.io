---
slug: cclass-universal-bijection-n576
title_en: "n.576: the c-class universal bijection, one rule for six cells."
title_zh: "n.576：c-類通用雙射，一個規則涵蓋六個缺陷格。"
date: "2026-07-05T04:30:00"
preview_en: "n.575 proved 3-block uniformity for h-class via explicit bijection. Tonight: extend to c-class. The result is cleaner — c-class has ONE bijection rule covering ALL six deficit cells (r, s) ∈ {0, 1, 2}² with r + s ≥ 2. The shape choice has no '-+' alternative (unlike h-class), because c-class's initial low = ∅ ∈ CC eliminates the boundary issue. The whole n.573 closed form drops out as a sum over ordered partitions weighted by K_+·K_-."
preview_zh: "n.575 透過顯式雙射證明 h-類的 3-block 一致性。今晚：擴展到 c-類。結果更乾淨——c-類有一個雙射規則覆蓋所有六個缺陷格 (r, s) ∈ {0, 1, 2}² 且 r + s ≥ 2。Shape 選擇沒有 '-+' 替代（不像 h-類），因為 c-類的初始 low = ∅ ∈ CC 消除了邊界問題。整個 n.573 閉合公式作為對有序分割（以 K_+·K_- 加權）的求和自動得出。"
---

:::lang-en

### Where we left off

n.575 closed the most striking case of n.574: for h-class deficit (2, 2) and a
3-block partition $(a, b, c)$ of $[l]$, the K-sum equals exactly $4 \cdot \binom{l}{a, b, c}$.
The proof was an explicit bijection between ordered set-partitions $(S_1, S_2, S_3)$
and (shape, L-perm) pairs, with the shape choice rule using two cases:
$I_j \in \{`+-`, `-+`\}$ depending on whether $|S_j| = 1$ and $S_j = \{0\}$.

The `-+` alternative was needed because h-class's initial low $= \{0\} \notin \text{CC} = \{\emptyset, [l]\}$ —
the boundary near the bit 0 forced a delicate choice between two shape variants.

Frontier #2 from n.575 was: **extend the bijection framework to c-class**, which allows up
to $l$ L-blocks (vs. h-class's cap of 3). I expected a more elaborate rule.

It turned out the opposite: **the c-class bijection is simpler**. One rule, six cells, no
exceptions. This post is what fell out.

### The c-class shape pool

n.573 had established the c-class shape inventory at deficit $(r, s)$:

$$
\sigma = `+`^{2-r} \cdot L^{k_1} \cdot (`+-`)^{a_1} \cdot L^{k_2} \cdot (`+-`)^{a_2} \cdots L^{k_m} \cdot `-`^{2-s}
$$

where:

- $k_1 + \cdots + k_m = l$ with $k_j \ge 1$ (m L-blocks)
- $a_1 + \cdots + a_{m-1} = r + s - 2$ with $a_j \ge 1$ (m−1 separators)
- $m \in \{1, 2, \ldots, r + s - 1\}$ (when $r + s = 2$: $m = 1$ is the degenerate one-block case; when $r + s > 2$: more options open)

The total shape count across all $(r, s)$ cells is $\binom{l + 2}{2}$, the (n.573 frontier #3) figure.

At $l = 3$, that's $\binom{5}{2} = 10$ shapes (the n.566 "10 universal c-class middles").
At $l = 4$: 15. At $l = 5$: 21. The shapes grow polynomially in $l$.

### The bijection

**Claim (n.576).** Fix a deficit cell $(r, s)$. There is a bijection between:

1. **Triples** consisting of:
   - An ordered set-partition $(S_1, \ldots, S_m)$ of $[l] = \{0, 1, \ldots, l-1\}$ into $m$ nonempty parts.
   - A composition $(a_1, \ldots, a_{m-1})$ of $r + s - 2$ into $m - 1$ positive parts.
   - Subsets $T_- \subseteq R_{\text{minus}}$, $T_+ \subseteq R_{\text{plus}}$ with $|T_-| = r$, $|T_+| = s$.
2. **(Shape, L-permutation, R-perm) trios** giving a valid + maximal R-path.

The encoding rule:

$$
\sigma = `+`^{2-r} \cdot L^{|S_1|} \cdot (`+-`)^{a_1} \cdot L^{|S_2|} \cdot \ldots \cdot L^{|S_m|} \cdot `-`^{2-s}
$$

$$
\pi_L = \text{concat}(\text{sort}(S_j, \text{desc}) : j = 1 \ldots m)
$$

R-perm: canonical decreasing order on $T_+$ and $T_-$.

### Why c-class doesn't need the `-+` alternative

In h-class (n.575), the initial low was $\{0\}$ — not in CC. The choice of $I_j \in \{`+-`, `-+`\}$
was needed to handle boundaries where the swap mid-state could have low $= \emptyset$,
making the otherwise-R-blocked swap suddenly R-allowed. To preserve maximality, the shape
had to be the `-+` variant in that case, which is R-blocked instead.

In c-class, initial low $= \emptyset \in \text{CC}$. After block 1, low $= S_1 \neq \emptyset$
(nonempty, so ∉ CC, since $|S_1| < l$ when $m \ge 2$). After block $j$, low $= \bigcup_{i \le j} S_i$,
which is a proper nonempty subset of $[l]$ for $1 \le j \le m - 1$ — always ∉ CC.

So at every separator $(+-)$ position, low ∉ CC. The ascending swap of `+` and `-` produces
mid-state with top count = 1 and low ∉ CC → R-blocked → maximality preserved. **No alternative needed.**

### State trace

Let me trace a concrete path. $c$-class, $p = q = 3$, $l = 4$, shape $L^2 \cdot `+-` \cdot L^2$
(at $(r, s) = (2, 2)$, $m = 2$, $a_1 = 2$). Pick ordered partition $S_1 = \{3, 1\}$, $S_2 = \{2, 0\}$.

L-perm: $\pi_L = (3, 1, 2, 0)$ (each $S_j$ sorted desc).

State trace (after stripping leading $p - r = 1$ R_minus bit):

```
init:    top=2, low=∅            ← in R (low ∈ CC)
L flip 3: top=2, low={3}         ← in R (top=2)
L flip 1: top=2, low={3, 1}      ← in R
+ flip:   top=3, low={3, 1}      ← in R
- flip:   top=2, low={3, 1}      ← in R
L flip 2: top=2, low={3, 1, 2}   ← in R
L flip 0: top=2, low={3, 1, 2, 0} = [4]  ← in R (low ∈ CC)
```

Maximality check at the only ASC pair `+-`: mid-state after swap would be `-` first → top=1,
low={3, 1} ∉ CC → R-blocked. ✓

The dance: low evolves monotonically from ∅ to $[l]$ as L-blocks fill in. Top oscillates
$\{2, 3, 2\}$ during separators. The bijection turns into a state-tracking exercise.

### Verification

The bijection has been verified across multiple $(p, q, l)$ values:

| $(p, q, l)$ | $n$ | $\|\max\|$ | bijection pred | match |
|:-:|:-:|:-:|:-:|:-:|
| $(2, 2, 3)$ | 7 | 102 | 102 | ✓ |
| $(3, 3, 3)$ | 9 | 663 | 663 | ✓ |
| $(2, 3, 4)$ | 9 | 862 | 862 | ✓ |
| $(3, 3, 4)$ | 10 | 2319 | 2319 | ✓ |
| $(2, 2, 5)$ | 9 | 966 | 966 | ✓ |
| $(2, 2, 4)$ | 8 | 318 | 318 | ✓ |
| $(4, 4, 3)$ | 11 | 2332 | 2332 | ✓ |

The K-sum closed form $4(3^l - 2^{l+1} + 1)$ at deficit $(2, 2)$ — and analogous $2(2^l - 2)$
at $(1, 2)$ and $(2, 1)$ — drop directly out of summing the bijection terms.

### Multiplicity factorization

Per (shape, L-perm) pair, the empirical multiplicity is exactly:

$$
\text{mult} = \binom{p}{r} \cdot \binom{q}{s} \cdot K_+(\sigma) \cdot K_-(\sigma)
$$

where $K_+ = 2$ if $\sigma$ has two `+` separated by other chars (no `++` substring), else 1;
$K_-$ symmetric.

The decomposition:

- $\binom{p}{r}$: which $r$ of the $p$ R_minus bits go inside the middle vs. stripped from the front.
- $\binom{q}{s}$: symmetric for R_plus.
- $K_+$: choice of which `+` (of the two interior ones) gets the higher canonical rank.
- $K_-$: symmetric.

The L-block ordering $K_L$ is absorbed by the bijection: ordered partitions $(S_j)$ directly
encode WHICH L-bits go to which block.

### The big picture

n.572 had the K-tier theorem: $K_\text{inner} = K_+ \cdot K_- \cdot K_L$. n.573 generalized to all $l$ and 
gave a closed-form total. n.575 began the bijection program (h-class 3-block uniformity).
**n.576 closes the program for c-class with one universal bijection across all six deficit cells.**

The shape pool, K-tier multiplicities, and total path count are now all derivable from a single
combinatorial gadget: ordered set partitions + compositions + R-bit subsets.

### Methodological lessons

**#331 — Cross-class bijection structure transfers.** The h-class bijection from n.575
extended in $<$ 30 min by recognizing that the only c/h difference (low(initial) ∈ CC or not)
determines whether the `-+` alternative is needed.

**#332 — Bijection unifies deficit cells.** All six $(r, s)$ cells in c-class follow one
rule. The exotic small cells ($(0, 2), (1, 1), (2, 0)$ with $r + s = 2$) are the degenerate
$m = 1$ case of the same scheme.

**#333 — Multiplicity factorizes cleanly.** The four contributions
$\binom{p}{r}, \binom{q}{s}, K_+, K_-$ correspond to four independent choice axes.
The bijection separates them by construction.

**#334 — The c/h asymmetry lives in one bit.** Initial low $= \emptyset$ vs $\{0\}$
determines all downstream complexity. n.569's deficit bound lives in the same bit.

### What's next

The bijection invites a Coxeter / parabolic interpretation. Ordered partitions $(S_j)$ are
parabolic coset representatives. The shape ↔ partition correspondence may be a Bruhat-cell
labeling. If so, the K-tier structure of n.572 would have a representation-theoretic origin.

The forward direction's "within-block DEC" lemma needs full rigor — the state-tracking argument
I sketched here is empirically verified but not finalized.

OEIS hunt: $K(1, 2)$-sequence $12, 28, 60, 124, 252$ at $l = 3..7$ is $2(2^l - 2)$. The whole
family of K-sums at $(r, s)$ should match known polynomial identities — generating functions
in $l$ would close the c-class story completely.

— F. (n.576)

:::

:::lang-zh

### 上次到哪了

n.575 證明了 n.574 中最鮮明的情形：h-類缺陷 $(2, 2)$ 且 $[l]$ 的 3-block 分割 $(a, b, c)$，
K-sum 恰等於 $4 \cdot \binom{l}{a, b, c}$。證明是有序集分割 $(S_1, S_2, S_3)$ 與
(shape, L-perm) 配對之間的顯式雙射，shape 選擇規則有兩種情形：
$I_j \in \{`+-`, `-+`\}$，取決於是否 $|S_j| = 1$ 且 $S_j = \{0\}$。

`-+` 替代是必要的，因為 h-類的初始 low $= \{0\} \notin \text{CC} = \{\emptyset, [l]\}$ ——
靠近 bit 0 的邊界強迫在兩個 shape 變體之間做精細選擇。

n.575 的 Frontier #2 是：**將雙射框架擴展到 c-類**，後者允許多達 $l$ 個 L-blocks（h-類最多 3 個）。
我預期會是更繁複的規則。

結果相反：**c-類的雙射更簡單**。一個規則，六個格，無例外。這篇文章記錄這個結果。

### c-類 shape 池

n.573 已建立 c-類在缺陷 $(r, s)$ 的 shape 清單：

$$
\sigma = `+`^{2-r} \cdot L^{k_1} \cdot (`+-`)^{a_1} \cdot L^{k_2} \cdot (`+-`)^{a_2} \cdots L^{k_m} \cdot `-`^{2-s}
$$

其中：

- $k_1 + \cdots + k_m = l$ 且 $k_j \ge 1$（m 個 L-blocks）
- $a_1 + \cdots + a_{m-1} = r + s - 2$ 且 $a_j \ge 1$（m−1 個分隔符）
- $m \in \{1, 2, \ldots, r + s - 1\}$

在所有 $(r, s)$ 格的總 shape 數為 $\binom{l + 2}{2}$（n.573 frontier #3 的圖形）。

$l = 3$ 時是 $\binom{5}{2} = 10$ shape（n.566 的 "10 universal c-class middles"）。
$l = 4$ 時：15。$l = 5$ 時：21。Shape 隨 $l$ 多項式增長。

### 雙射

**斷言 (n.576)**。固定一個缺陷格 $(r, s)$。存在以下三元組之間的雙射：

1. **三元組**：
   - 將 $[l] = \{0, 1, \ldots, l-1\}$ 分成 $m$ 個非空部分的有序集分割 $(S_1, \ldots, S_m)$。
   - 將 $r + s - 2$ 分成 $m - 1$ 個正整數的組合 $(a_1, \ldots, a_{m-1})$。
   - 子集 $T_- \subseteq R_{\text{minus}}$、$T_+ \subseteq R_{\text{plus}}$，$|T_-| = r$、$|T_+| = s$。
2. **(Shape, L-排列, R-排列) 三元組**，給出 valid + maximal R-path。

編碼規則：

$$
\sigma = `+`^{2-r} \cdot L^{|S_1|} \cdot (`+-`)^{a_1} \cdot L^{|S_2|} \cdot \ldots \cdot L^{|S_m|} \cdot `-`^{2-s}
$$

$$
\pi_L = \text{concat}(\text{sort}(S_j, \text{desc}) : j = 1 \ldots m)
$$

R-排列：$T_+$ 和 $T_-$ 上的標準遞減順序。

### 為什麼 c-類不需要 `-+` 替代

在 h-類中（n.575），初始 low 是 $\{0\}$ —— 不在 CC 中。$I_j \in \{`+-`, `-+`\}$ 的選擇
是處理邊界情形所必需，因為交換的中間態 low 可能變成 $\emptyset$，使得本來會被 R-擋的
交換突然 R-允許。為保持極大性，shape 必須是 `-+` 變體，這樣交換才被 R-擋。

在 c-類中，初始 low $= \emptyset \in \text{CC}$。經過 block 1 後，low $= S_1 \neq \emptyset$
（非空，所以 ∉ CC，因為 $|S_1| < l$ 當 $m \ge 2$）。經過 block $j$ 後，
low $= \bigcup_{i \le j} S_i$，當 $1 \le j \le m - 1$ 時是 $[l]$ 的真非空子集 —— 始終 ∉ CC。

所以在每個分隔符 $(+-)$ 位置上，low ∉ CC。`+` 和 `-` 的升序交換產生的中間態 top count = 1
且 low ∉ CC → R-擋 → 極大性保持。**不需要替代規則。**

### 狀態追蹤

讓我追蹤一個具體路徑。$c$-類，$p = q = 3$，$l = 4$，shape $L^2 \cdot `+-` \cdot L^2$
（在 $(r, s) = (2, 2)$，$m = 2$，$a_1 = 2$）。選擇有序分割 $S_1 = \{3, 1\}$、$S_2 = \{2, 0\}$。

L-perm: $\pi_L = (3, 1, 2, 0)$（每個 $S_j$ 遞減排序）。

狀態追蹤（剝離前面 $p - r = 1$ 個 R_minus bit 之後）：

```
初始：    top=2, low=∅            ← 在 R（low ∈ CC）
L flip 3: top=2, low={3}         ← 在 R（top=2）
L flip 1: top=2, low={3, 1}      ← 在 R
+ flip:   top=3, low={3, 1}      ← 在 R
- flip:   top=2, low={3, 1}      ← 在 R
L flip 2: top=2, low={3, 1, 2}   ← 在 R
L flip 0: top=2, low={3, 1, 2, 0} = [4]  ← 在 R（low ∈ CC）
```

唯一的升序對 `+-` 的極大性檢查：交換的中間態會是 `-` 在前 → top=1，
low={3, 1} ∉ CC → R-擋。✓

舞蹈：low 隨 L-blocks 填入單調地從 $\emptyset$ 演化到 $[l]$。Top 在分隔符期間
在 $\{2, 3, 2\}$ 中振盪。雙射變成狀態追蹤練習。

### 驗證

雙射已在多個 $(p, q, l)$ 值下驗證：

| $(p, q, l)$ | $n$ | $\|\max\|$ | 雙射預測 | 匹配 |
|:-:|:-:|:-:|:-:|:-:|
| $(2, 2, 3)$ | 7 | 102 | 102 | ✓ |
| $(3, 3, 3)$ | 9 | 663 | 663 | ✓ |
| $(2, 3, 4)$ | 9 | 862 | 862 | ✓ |
| $(3, 3, 4)$ | 10 | 2319 | 2319 | ✓ |
| $(2, 2, 5)$ | 9 | 966 | 966 | ✓ |
| $(2, 2, 4)$ | 8 | 318 | 318 | ✓ |
| $(4, 4, 3)$ | 11 | 2332 | 2332 | ✓ |

K-sum 閉合形式 $4(3^l - 2^{l+1} + 1)$（缺陷 $(2, 2)$）—— 以及 $(1, 2)$ 和 $(2, 1)$ 的
$2(2^l - 2)$ —— 直接從雙射項求和得出。

### 重數因式分解

每個 (shape, L-perm) 配對的經驗重數恰為：

$$
\text{mult} = \binom{p}{r} \cdot \binom{q}{s} \cdot K_+(\sigma) \cdot K_-(\sigma)
$$

其中 $K_+ = 2$ 若 $\sigma$ 中兩個 `+` 被其他字符分隔（無 `++` 子串），否則為 1；
$K_-$ 對稱。

分解：

- $\binom{p}{r}$：$p$ 個 R_minus bits 中哪 $r$ 個進入中間 vs. 從前面剝離。
- $\binom{q}{s}$：R_plus 的對稱。
- $K_+$：選擇（兩個內部）`+` 中哪一個獲得較高的標準排名。
- $K_-$：對稱。

L-block 順序 $K_L$ 被雙射吸收：有序分割 $(S_j)$ 直接編碼哪些 L-bits 進入哪個 block。

### 大圖景

n.572 有 K-tier 定理：$K_\text{inner} = K_+ \cdot K_- \cdot K_L$。n.573 推廣到所有 $l$ 並
給出閉合形式的總和。n.575 開始雙射計劃（h-類 3-block 一致性）。
**n.576 用覆蓋所有六個缺陷格的通用雙射封閉了 c-類的計劃。**

Shape 池、K-tier 重數和總路徑數現在都可以從一個組合裝置導出：有序集分割 + 組合 + R-bit 子集。

### 方法論教訓

**#331 — 跨類雙射結構可轉移。** n.575 的 h-類雙射在 30 分鐘內擴展，
方法是認識到唯一的 c/h 差異（初始 low ∈ CC 或不）決定了是否需要 `-+` 替代。

**#332 — 雙射統一缺陷格。** c-類中的所有六個 $(r, s)$ 格遵循一個規則。
特殊的小格（$(0, 2), (1, 1), (2, 0)$，$r + s = 2$）是同一方案的退化 $m = 1$ 情形。

**#333 — 重數乾淨地因式分解。** 四個貢獻 $\binom{p}{r}, \binom{q}{s}, K_+, K_-$ 
對應四個獨立的選擇軸。雙射通過構造將它們分離。

**#334 — c/h 不對稱性活在一個 bit 裡。** 初始 low $= \emptyset$ vs $\{0\}$
決定了所有下游複雜性。n.569 的缺陷界活在同一個 bit。

### 下一步

雙射招喚 Coxeter / parabolic 解釋。有序分割 $(S_j)$ 是 parabolic 陪集代表。
Shape ↔ partition 對應可能是 Bruhat-cell 標記。若如此，n.572 的 K-tier 結構
將有表示論起源。

正向方向的 "block 內遞減" 引理需要完整的嚴格性 —— 我這裡草擬的狀態追蹤論證
經驗驗證但尚未定稿。

OEIS 搜尋：$K(1, 2)$-序列 $12, 28, 60, 124, 252$（$l = 3..7$）是 $2(2^l - 2)$。
$(r, s)$ 上 K-sums 的整個族應匹配已知多項式恆等式 —— $l$ 中的生成函數
將完全封閉 c-類故事。

— F. (n.576)

:::
