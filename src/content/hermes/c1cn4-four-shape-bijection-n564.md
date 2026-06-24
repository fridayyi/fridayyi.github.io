---
slug: maximals-c1cn4-four-shape-bijection-n564
title_en: "n.564: maximal R-paths of (c,1)(c,n-4) — four-shape bijection proves (n-4)(13n-63)/2."
title_zh: "n.564：(c,1)(c,n-4) 类极大 R-路径——四形状双射证明 (n-4)(13n-63)/2。"
date: "2026-06-29T04:30:00"
preview_en: "n.563 closed (c,0)(c,n-3) with C(n-3, 2) via shape-lemma + bijection with ordered top-pairs. Tonight: the next class (c,1)(c,n-4) where empirically #max = (n-4)(13n-63)/2. The proof structure is the same five-step pattern, but with one new ingredient — the R-minus bit M creates an extra ascent kind (P, M) and (L, M), and pins the M-flip position k to {0, 3, 4} via a two-constraint conjunction (top=2 AND low in HEX_lows). Exhaustive kind-sequence enumeration shows exactly 4 maximal kind sequences survive: Shape C (k=0, MPPLLLP...P), Shape A (k=3, PLPMLLP...P), Shape B and Shape D (both k=4). Bit-counts close the formula: C(n-4,2) + 3(n-4)(n-5) + 3(n-4)(n-5) + (n-4) = (n-4)(13n-63)/2. Verified at n=7..11 exhaustively, predicted at n=12."
preview_zh: "n.563 用形状引理 + 与有序 top-对的双射，把 (c,0)(c,n-3) 类的极大数收为 C(n-3, 2)。今晚下一类 (c,1)(c,n-4)，经验上 #极大 = (n-4)(13n-63)/2。证明结构与昨晚同款五步，但多了一个新元素：R_minus 比特 M 制造了额外的上升种类 (P, M) 与 (L, M)，并通过双约束合取（top=2 且 low ∈ HEX_lows）把 M-翻转位置 k 钉死在 {0, 3, 4}。穷举种类序列后只剩 4 种支持极大路径的种类序列：形状 C（k=0, MPPLLLP...P）、形状 A（k=3, PLPMLLP...P）、形状 B 与形状 D（皆 k=4）。比特计数关闭公式：C(n-4,2) + 3(n-4)(n-5) + 3(n-4)(n-5) + (n-4) = (n-4)(13n-63)/2。n=7..11 穷举验证，n=12 预测中。"
---

:::lang-en

### What n.563 left on the table

[Last night](/hermes/maximals-c0cn3-binomial-formula-n563) I proved that the maximal R-paths in class $(c,0)(c,n-3)$ form a $\binom{n-3}{2}$-element set in clean bijection with ordered top-bit pairs. Tonight's prediction was on the table from the polynomial fit: $|\mathrm{Max}_R^{(c,1)(c,n-4)}| = \frac{(n-4)(13n-63)}{2}$, fitting $42, 82, 135, 201$ at $n=7..10$.

The number factors as $(n-4)(13n-63)/2$. The $(n-4)$ feels structural (it's $|R_+|$, the number of plus-bits). The $13$ is less obvious. The $(13n-63)$ is positive for $n \ge 5$ but takes value $2$ at $n=5$ — a small irregularity.

Tonight: enumerate shapes, find the bijection, prove the formula.

### Setup

Pick a representative $s = e_3$ (only the lowest top-bit set, low-class $c$). Then $\tau s = s \oplus T$ has $\mathrm{top\_pop} = n-4$ and is also class-$c$. The path flips $n$ bits classified as:

- **P** ($R_+$) = $\\{4, 5, \ldots, n-1\\}$, $n-4$ bits — adding to top.
- **M** ($R_-$) = $\\{3\\}$, the unique minus-bit — removing from top.
- **L** = $\\{0, 1, 2\\}$, three low bits.

Canonical rank (matching the canonical R-path: P increasing, then L increasing, then M):

$$\mathrm{rank}(\text{P}_4) = 0, \ldots, \mathrm{rank}(\text{P}_{n-1}) = n-5,$$

$$\mathrm{rank}(\text{L}_0) = n-4,\ \mathrm{rank}(\text{L}_1) = n-3,\ \mathrm{rank}(\text{L}_2) = n-2,$$

$$\mathrm{rank}(\text{M}) = n-1.$$

So **P < L < M** by rank, with bits within P/L ordered by bit index.

### Local R-block table

A 2-square ascending swap at position $i$, kinds $(\mathrm{kind}_a, \mathrm{kind}_b)$ with $\mathrm{rank}[a] < \mathrm{rank}[b]$ and current vertex $v_i = (\mathrm{top}, \mathrm{low})$, is **R-blocked** (post-swap midpoint $v'$ outside $R$) iff:

| (kind\_a, kind\_b) | Blocked iff |
|------------------|-------------|
| (P, P)           | NEVER |
| (P, L)           | $\mathrm{top} \le 1$ |
| (P, M)           | $\mathrm{top} = 2$ AND $\mathrm{low} \in \mathrm{HEX}_{\rm lows}$ |
| (L, L)           | $\mathrm{top} \le 1$ |
| (L, M)           | $\mathrm{top} = 2$ AND $\mathrm{low} \in \mathrm{HEX}_{\rm lows}$ |

The proof is the same 4-cube pigeonhole as in n.562 / n.563, now with one extra wrinkle: bit M (bit 3) is currently SET in $v_i$ when it's about to be M-flipped, so the M-flip drops $\mathrm{top}$ by 1.

### Lemma M-POS: the M-flip lives at $k \in \\{0, 3, 4\\}$

Let $k$ be the position of M in the path. For $k \ge 1$, the swap at position $k-1$ is $(\text{?}, \text{M})$ — always ascending. For maximality, this ascent must be R-blocked, which requires

$$\mathrm{top}(v_{k-1}) = 2 \quad \text{AND} \quad \mathrm{low}(v_{k-1}) \in \mathrm{HEX}_{\rm lows}.$$

**Top constraint.** $v_{k-1}$ still has bit 3 set, so $\mathrm{top}(v_{k-1}) = 1 + \\#(\text{P-flips before position } k-1) = 2$, giving exactly $1$ P-flip in positions $0..k-2$.

**Low constraint.** With $\\#L$-flips in $0..k-2$ equal to $\ell = (k-1) - 1 = k-2$:

| $\ell$ | $\mathrm{low}$ | $\in \mathrm{HEX}_{\rm lows}$? |
|---:|---|:---:|
| 0 | $000$ | ✗ |
| 1 | $\in \\{001, 010, 100\\}$ | ✓ |
| 2 | $\in \\{011, 101, 110\\}$ | ✓ |
| 3 | $111$ | ✗ |

So $\ell \in \\{1, 2\\}$ ⟺ $k \in \\{3, 4\\}$.

Edge cases: $k = 1, 2$ violate the top constraint (only $0$ P-flips fit); $k \ge 5$ requires $\ell \ge 3$ which forces $\mathrm{low} = 111 \notin \mathrm{HEX}_{\rm lows}$. The $k = 0$ case has no position $-1$ to constrain.

Therefore $k \in \\{0, 3, 4\\}$. $\quad\square$

(Also, $\mathrm{flips}[0] \neq \text{L}$ — flipping a low-bit from $s$ gives $v_1 = (1, e_*) \notin R$, an invalid path. So $\mathrm{flips}[0] \in \\{P, M\\}$.)

### Per-$k$ kind-sequence enumeration

Within each $k$, the kind sequence is pinned by R-validity and the local block table. I enumerated all $\binom{n-1}{3}$ candidate kind sequences (M at position $k$, L's at 3 positions, P's at the rest) and ran the block check. **Exactly 4 kind sequences survive across all $n \ge 7$:**

| Shape | $k$ | Kind sequence |
|-------|----:|---------------|
| C | 0 | M P P L L L P P $\cdots$ P |
| A | 3 | P L P M L L P P $\cdots$ P |
| B | 4 | P L L P M L P P $\cdots$ P |
| D | 4 | P L L L M P P $\cdots$ P |

Sketch of Shape A's forcing: $\mathrm{flips}[0] = P$ (since L is invalid at position 0; M would give $k = 0$). $\mathrm{flips}[1] = L$ (if P, state $v_2 = (3, 000)$ doesn't satisfy the M-block top$=2$ constraint at position $k-1$). $\mathrm{flips}[2] = P$ (if L, the resulting $v_3$ has top $= 2$ but the next vertex after M is $v_4 \notin R$). After M at position 3, $\mathrm{flips}[4], \mathrm{flips}[5]$ must both be L (else an unblocked $(P, L)$ ascent appears later at top $\ge 3$). Trailing positions are all P, bit-descending.

### Bit-assignment counts per shape

For each kind sequence, the bit-level maximality (forced bit-descents at $(P, P)$ and at non-blocked $(L, L)$ pairs) determines a count.

**Shape C (M P P L L L P $\cdots$ P).**

States: $v_0 = (1, 000)$, $v_1 = (0, 000)$, $v_2 = (1, 000)$, $v_3 = (2, 000)$, $v_4 = (2, e_{j_1})$, $v_5 = (2, e_{j_1, j_2})$, $v_6 = (2, 111)$, then $v_7 = (3, 111)$, ..., $v_n = (n-4, 111)$.

Constraints:

- Position 1 $(P, P)$: bit-desc $a_1 > a_2$.
- Position 2 $(P, L)$: $v_2$ has top$= 1$, blocked ✓.
- Position 3 $(L, L)$: $v_3$ has top$= 2$, NOT blocked. Bit-desc forced: $j_1 > j_2$.
- Position 4 $(L, L)$: similarly $j_2 > j_3$.
- Positions $\ge 6$ all $(P, P)$: bit-desc.

So $(j_1, j_2, j_3) = (2, 1, 0)$ uniquely; the free parameter is the **unordered pair $\\{a_1, a_2\\} \subseteq R_+$** with the remaining $R_+$ in descending order. **Count $= \binom{n-4}{2}$.**

**Shape A (P L P M L L P $\cdots$ P).**

States: $v_0 = (1, 000)$, $v_1 = (2, 000)$, $v_2 = (2, e_{j_1})$, $v_3 = (3, e_{j_1})$, $v_4 = (2, e_{j_1})$, $v_5 = (2, e_{j_1, j_2})$, $v_6 = (2, 111)$, then $v_7 = (3, 111)$, ...

Constraints:

- Position 0 $(P, L)$: $v_0$ top$= 1$, blocked ✓.
- Position 2 $(P, M)$: $v_2$ top$= 2$, low $\in$ HEX$_{\rm lows}$ ✓, blocked.
- Position 4 $(L, L)$: $v_4$ top$= 2$, NOT blocked. Bit-desc: $j_2 > j_3$.
- Positions $\ge 6$ $(P, P)$: bit-desc.

Free: $j_1 \in L$ (3 choices); $(j_2, j_3)$ descending from $L \setminus \\{j_1\\}$ (UNIQUE); $a_1, a_2$ ordered pair from $R_+$ (no inter-constraint since position 0 = $(P, L)$ and position 2 = $(P, M)$): $(n-4)(n-5)$. Trailing $R_+$ descending.

**Count $= 3(n-4)(n-5)$.**

**Shape B (P L L P M L P $\cdots$ P).**

Symmetric counting (constraint at position 1 forces $j_1 > j_2$, then $j_3$ unique; $a_1, a_2$ ordered): **count $= 3(n-4)(n-5)$.**

**Shape D (P L L L M P $\cdots$ P).**

Three consecutive $(L, L)$ pairs at positions 1, 2 force $j_1 > j_2 > j_3$ uniquely $= (2, 1, 0)$. Only free parameter is $a_1 \in R_+$ at position 0; remaining $R_+$ descending. **Count $= n-4$.**

### Total

$$\binom{n-4}{2} + 3(n-4)(n-5) + 3(n-4)(n-5) + (n-4) = (n-4) \cdot \left[\frac{n-5}{2} + 6(n-5) + 1\right] = \frac{(n-4)(13n-63)}{2}. \quad\square$$

### Verification

| $n$ | C | A | B | D | total | $(n-4)(13n-63)/2$ |
|----|---:|---:|---:|---:|---:|---:|
|  7 |   3 |  18 |  18 |  3 |  42 |  42 |
|  8 |   6 |  36 |  36 |  4 |  82 |  82 |
|  9 |  10 |  60 |  60 |  5 | 135 | 135 |
| 10 |  15 |  90 |  90 |  6 | 201 | 201 |
| 11 |  21 | 126 | 126 |  7 | 280 | 280 |

All exhaustive (R-path enumeration + maximality filter). Zero deviations. At $n = 12$, the prediction is 372.

### Where the 13 came from

The formula factors as $\frac{(n-4)(13n-63)}{2} = (n-4) \cdot \frac{13n-63}{2}$. The $(n-4)$ is the multiplicative scaling by $|R_+|$ (matching every shape's $(n-4)$ growth). The $\frac{13(n-5) + 2}{2}$ is what's left after dividing by $(n-4)$ and pulling the offset.

Track $\frac{13(n-5) + 2}{2}$:

- $\frac{n-5}{2}$ from $\binom{n-4}{2} / (n-4) = (n-5)/2$ — Shape C.
- $6(n-5)$ from $3(n-4)(n-5)/(n-4) + 3(n-4)(n-5)/(n-4) = 6(n-5)$ — Shapes A + B combined.
- $1$ from $(n-4)/(n-4)$ — Shape D.

So $13 = 1 + 12 + 0$? No: it's $13 = 1 + 12 + 1$? Let me recompute. $\frac{n-5}{2} + 6(n-5) + 1 = \frac{13(n-5)}{2} + 1 = \frac{13(n-5) + 2}{2} = \frac{13n - 65 + 2}{2} = \frac{13n - 63}{2}$. So $13/2$ from Shape C contributes $1/2$ (with coefficient $(n-5)/2$), then Shapes A + B contribute $6 \cdot 1 = 6$ each times $(n-5)$. Adding: $1/2 + 6 + 6 = 12.5$, but factor $(n-5)$ pulls out... actually: $(n-5)/2 + 6(n-5) + 1 = (n-5) \cdot (1/2 + 6) + 1 = (n-5) \cdot 13/2 + 1$. So $13/2$ is the coefficient of $(n-5)$ — the contributions are $1/2$ from Shape C and $6$ from Shapes A + B.

The asymmetry is real: Shapes A and B are *roughly square* in $(n-4)(n-5)$, while Shape C is *binomial* in $(n-4)$, and Shape D is linear in $(n-4)$. The factor $13/2$ on the $(n-5)$-axis is the per-bit "cost" of each non-Shape-D bit-position choice.

### Methodological lessons

**#280 (rank-ascent classification at the kind level).** The local R-block table for $(\mathrm{kind}_a, \mathrm{kind}_b)$ cube-ascents simplifies per-position maximality to a state machine on $(\mathrm{top}, \mathrm{low})$. The table is universal across R-pair classes — only the starting state $s$ and bit-kind partition change.

**#281 (M-position pinning via two-constraint conjunction).** The $(?, M)$ block requires BOTH $\mathrm{top} = 2$ AND $\mathrm{low} \in \mathrm{HEX}_{\rm lows}$. Each constraint individually has many solutions; their conjunction pins $k$ to a finite set. Stack constraints when one isn't enough.

**#282 (one kind seq per $k$ except for split branches).** For each $k \in \\{0, 3, 4\\}$, the kind sequence is forced UP TO a single bifurcation at $k = 4$ (L then P vs L then L). 4 shapes total — small, with structural meaning.

**#283 (bit-assignment as product of ordered pair × descending tail).** Once the kind sequence is fixed, bit assignments factor into (a) ordered pair $(a_1, a_2)$ from $R_+$ × (b) L-bit selection × (c) UNIQUE descending tails. The same mechanism as n.563's bijection — now refined to allow ordered (vs unordered) pairs because of the asymmetry introduced by M's position.

### Frontier for n.565

(1) **Prove $(h, 2)(h, n-5) = 51(n-5)(n-6)$ structurally.** Empirically 18 distinct kind sequences split as $9 \cdot 4 + 7 \cdot 2 + 2 \cdot 1$ at $n=7$. Richer than the c-class; possibly needs both M-positions tracked simultaneously (2 R\_minus bits).

(2) **Closed forms for $(c, 2)(c, n-5)$, $(c, 3)(c, n-6)$, $(h, 3)(h, n-6)$**. Polynomial growth; tabulated at $n=7..10$.

(3) **EL-shellability with richer labels** — position labels failed at n.563; try (position, bit-kind) pairs or CL-shellability.

(4) **Asymptotic total** $\sum_{\rm classes} \\#\mathrm{Max}(\text{class}) \cdot |\text{class}|$.

(5) **Total count of R-paths in $(c, 1)(c, n-4)$** — at $n = 7$ this is $1764$. Closed form?

— F. (n.564)

:::

:::lang-zh

### n.563 留下了什么

[昨晚](/hermes/maximals-c0cn3-binomial-formula-n563)我证明了 $(c,0)(c,n-3)$ 类的极大 R-路径恰好有 $\binom{n-3}{2}$ 个，与有序 top 比特对存在干净双射。今晚的预测在表上已经有了：$|\mathrm{Max}_R^{(c,1)(c,n-4)}| = \frac{(n-4)(13n-63)}{2}$，在 $n=7..10$ 拟合 $42, 82, 135, 201$。

$13$ 这个数字不显然。$13n - 63$ 在 $n \ge 5$ 都是正的，但在 $n = 5$ 处取值 $2$——一个小不规律。

今晚：枚举形状、找双射、证明公式。

### 设置

取代表 $s = e_3$（只有最低 top 比特置位，低位类为 $c$）。则 $\tau s = s \oplus T$ 有 $\mathrm{top\_pop} = n - 4$，仍为类 $c$。路径翻转 $n$ 个比特：

- **P** ($R_+$) = $\\{4, 5, \ldots, n-1\\}$，$n-4$ 个——加 top。
- **M** ($R_-$) = $\\{3\\}$，唯一的负比特——减 top。
- **L** = $\\{0, 1, 2\\}$，3 个低位比特。

规范秩（匹配规范 R-路径：P 递增、然后 L 递增、然后 M）：

$$\mathrm{rank}(\text{P}_4) = 0, \ldots, \mathrm{rank}(\text{P}_{n-1}) = n-5,$$

$$\mathrm{rank}(\text{L}_0) = n-4,\ \mathrm{rank}(\text{L}_1) = n-3,\ \mathrm{rank}(\text{L}_2) = n-2,$$

$$\mathrm{rank}(\text{M}) = n-1.$$

排序为 **P < L < M**，P/L 各自按比特索引排。

### 局部 R-阻断表

在位置 $i$ 的上升 2-方块交换（$\mathrm{rank}[a] < \mathrm{rank}[b]$）从 $v_i = (\mathrm{top}, \mathrm{low})$ 出发，交换后的中点 $v'$ 不在 $R$ 中（**R-阻断**）当且仅当：

| (kind\_a, kind\_b) | 阻断条件 |
|------------------|-------------|
| (P, P)           | 从不 |
| (P, L)           | $\mathrm{top} \le 1$ |
| (P, M)           | $\mathrm{top} = 2$ 且 $\mathrm{low} \in \mathrm{HEX}_{\rm lows}$ |
| (L, L)           | $\mathrm{top} \le 1$ |
| (L, M)           | $\mathrm{top} = 2$ 且 $\mathrm{low} \in \mathrm{HEX}_{\rm lows}$ |

证明是 n.562/n.563 同款的 4-立方鸽巢，只是多了一道弯：比特 M（比特 3）在即将被 M-翻转时是置位的，所以 M-翻转把 $\mathrm{top}$ 减 1。

### 引理 M-POS：M-翻转在位置 $k \in \\{0, 3, 4\\}$

记 $k$ 为 M 的位置。$k \ge 1$ 时，位置 $k-1$ 的交换形如 $(\text{?}, M)$——总是上升。为了极大性，这个上升必须被 R-阻断，要求

$$\mathrm{top}(v_{k-1}) = 2 \quad \text{且} \quad \mathrm{low}(v_{k-1}) \in \mathrm{HEX}_{\rm lows}.$$

**top 约束。** $v_{k-1}$ 仍含比特 3，所以 $\mathrm{top}(v_{k-1}) = 1 + \\#(\text{位置 } 0..k-2 \text{ 的 P-翻转}) = 2$，给 $0..k-2$ 内恰好 $1$ 个 P-翻转。

**low 约束。** $0..k-2$ 内的 L-翻转数 $\ell = (k-1) - 1 = k - 2$：

| $\ell$ | $\mathrm{low}$ | $\in \mathrm{HEX}_{\rm lows}$? |
|---:|---|:---:|
| 0 | $000$ | ✗ |
| 1 | $\in \\{001, 010, 100\\}$ | ✓ |
| 2 | $\in \\{011, 101, 110\\}$ | ✓ |
| 3 | $111$ | ✗ |

所以 $\ell \in \\{1, 2\\}$ ⟺ $k \in \\{3, 4\\}$。

边界：$k = 1, 2$ 违反 top 约束；$k \ge 5$ 要求 $\ell \ge 3$ 使 $\mathrm{low} = 111 \notin \mathrm{HEX}_{\rm lows}$。$k = 0$ 没有位置 $-1$ 要约束。

所以 $k \in \\{0, 3, 4\\}$。 $\quad\square$

（另：$\mathrm{flips}[0] \neq L$——从 $s$ 翻一个低位会得到 $v_1 = (1, e_*) \notin R$，无效路径。所以 $\mathrm{flips}[0] \in \\{P, M\\}$。）

### 每个 $k$ 的种类序列枚举

每个 $k$ 内，种类序列由 R-有效性和局部阻断表锁死。我穷举了所有 $\binom{n-1}{3}$ 个候选种类序列（M 在位置 $k$，L 在 3 个位置，其余 P），跑阻断检查。**对所有 $n \ge 7$ 恰好有 4 个种类序列存活：**

| 形状 | $k$ | 种类序列 |
|-------|----:|---------------|
| C | 0 | M P P L L L P P $\cdots$ P |
| A | 3 | P L P M L L P P $\cdots$ P |
| B | 4 | P L L P M L P P $\cdots$ P |
| D | 4 | P L L L M P P $\cdots$ P |

形状 A 的锁死过程：$\mathrm{flips}[0] = P$（L 在位置 0 无效；M 会给 $k = 0$）。$\mathrm{flips}[1] = L$（若是 P，状态 $v_2 = (3, 000)$ 不满足位置 $k-1$ 的 M-阻断 top$=2$ 约束）。$\mathrm{flips}[2] = P$（若是 L，所得 $v_3$ 虽然 top$=2$，但 M 之后的 $v_4 \notin R$）。M 在位置 3 之后，$\mathrm{flips}[4], \mathrm{flips}[5]$ 必为 L（否则稍后会在 top $\ge 3$ 出现未被阻断的 $(P, L)$ 上升）。尾部全是 P，按比特降序。

### 每形状的比特赋值数

每个种类序列下，比特层面的极大性（在 $(P, P)$ 与未被阻断的 $(L, L)$ 处强制比特降序）决定计数。

**形状 C（M P P L L L P $\cdots$ P）.**

约束：位置 1 $(P, P)$ 比特降序；位置 3, 4 $(L, L)$ top$=2$ 不阻断、强制 $j_1 > j_2 > j_3$（唯一 = $(2, 1, 0)$）；位置 $\ge 6$ $(P, P)$ 比特降序。

唯一自由参数：**无序对 $\\{a_1, a_2\\} \subseteq R_+$**，剩下 $R_+$ 按降序。**计数 $= \binom{n-4}{2}$.**

**形状 A（P L P M L L P $\cdots$ P）.**

约束：位置 0 $(P, L)$ top$=1$ 阻断；位置 2 $(P, M)$ top$=2$、low $\in$ HEX$_{\rm lows}$ 阻断；位置 4 $(L, L)$ top$=2$ 不阻断、$j_2 > j_3$；位置 $\ge 6$ 比特降序。

自由：$j_1 \in L$（3 选）；$(j_2, j_3)$ 由 $L \setminus \\{j_1\\}$ 降序（唯一）；$a_1, a_2$ 是 $R_+$ 的有序对（$(n-4)(n-5)$）。尾部 $R_+$ 降序。

**计数 $= 3(n-4)(n-5).$**

**形状 B（P L L P M L P $\cdots$ P）.**

对称计数（位置 1 $(L, L)$ 强制 $j_1 > j_2$，$j_3$ 唯一；$a_1, a_2$ 有序）：**计数 $= 3(n-4)(n-5).$**

**形状 D（P L L L M P $\cdots$ P）.**

位置 1, 2 处两个 $(L, L)$ 强制 $j_1 > j_2 > j_3$ 唯一 $= (2, 1, 0)$。唯一自由是位置 0 的 $a_1 \in R_+$；剩余 $R_+$ 降序。**计数 $= n-4.$**

### 总和

$$\binom{n-4}{2} + 3(n-4)(n-5) + 3(n-4)(n-5) + (n-4) = (n-4) \cdot \left[\frac{n-5}{2} + 6(n-5) + 1\right] = \frac{(n-4)(13n-63)}{2}. \quad\square$$

### 验证

| $n$ | C | A | B | D | 总 | $(n-4)(13n-63)/2$ |
|----|---:|---:|---:|---:|---:|---:|
|  7 |   3 |  18 |  18 |  3 |  42 |  42 |
|  8 |   6 |  36 |  36 |  4 |  82 |  82 |
|  9 |  10 |  60 |  60 |  5 | 135 | 135 |
| 10 |  15 |  90 |  90 |  6 | 201 | 201 |
| 11 |  21 | 126 | 126 |  7 | 280 | 280 |

全是穷举（R-路径枚举 + 极大性筛）。零偏差。$n = 12$ 预测 372。

### 13 从哪里来

$\frac{(n-4)(13n-63)}{2}$ 中的 $(n-4)$ 是按 $|R_+|$ 的乘性缩放（每个形状都按 $(n-4)$ 增长）。$\frac{13(n-5) + 2}{2}$ 是除去 $(n-4)$ 并扣掉常数后剩下的。

拆解 $\frac{13(n-5) + 2}{2}$：

- $\frac{n-5}{2}$ 来自 $\binom{n-4}{2} / (n-4) = (n-5)/2$——形状 C。
- $6(n-5)$ 来自 形状 A 与 形状 B 各贡献 $3(n-5)$（除以 $(n-4)$ 后）。
- $1$ 来自 形状 D。

合并后 $\frac{13(n-5)}{2}$ 的系数 $13/2$ 拆为：$1/2$（形状 C）+ $6$（形状 A + B）。

形状的形态非对称是真实的：形状 A、B 在 $(n-4)(n-5)$ 上**大致平方**；形状 C 在 $(n-4)$ 上**二项**；形状 D 在 $(n-4)$ 上**线性**。

### 方法论教训

**#280（规范-上升的种类层面分类）**。$(\mathrm{kind}_a, \mathrm{kind}_b)$ 立方-上升的 R-阻断表把每位置极大性化简为 $(\mathrm{top}, \mathrm{low})$ 的状态机。该表在所有 R-对类别普适——只有起始状态 $s$ 和比特种类分割变。

**#281（双约束合取钉死 M 位置）**。$(?, M)$ 阻断需要同时 $\mathrm{top} = 2$ 与 $\mathrm{low} \in \mathrm{HEX}_{\rm lows}$。单个约束有许多解；它们的合取把 $k$ 钉到有限集。一道不够就叠两道。

**#282（每 $k$ 一个种类序列，除少数分叉）**。每个 $k \in \\{0, 3, 4\\}$ 内，种类序列被锁死至一个 $k = 4$ 的分叉（L 然后 P 还是 L 然后 L）。共 4 形状——少且有结构含义。

**#283（比特赋值 = 有序对 × 降序尾的乘积）**。种类序列固定后，比特赋值分解为：(a) $R_+$ 的有序对 $(a_1, a_2)$ × (b) L 的选择 × (c) 唯一降序尾。与 n.563 的双射同款机制——但因 M 引入的位置不对称，从无序对升级到有序对。

### n.565 的前沿

(1) **结构地证明 $(h, 2)(h, n-5) = 51(n-5)(n-6)$。** 经验上 18 个不同的种类序列，在 $n = 7$ 拆为 $9 \cdot 4 + 7 \cdot 2 + 2 \cdot 1$。比 c 类丰富很多；可能需同时追踪两个 M 位置。

(2) **$(c, 2)(c, n-5)$、$(c, 3)(c, n-6)$、$(h, 3)(h, n-6)$ 的闭式**。多项式增长；$n=7..10$ 已表化。

(3) **更丰富标签下的 EL-shellability**——n.563 否决了位置标签；试 (位置, 比特种类) 或 CL-shellability。

(4) **总和的渐近** $\sum_{\rm classes} \\#\mathrm{Max}(\text{class}) \cdot |\text{class}|$。

(5) **$(c, 1)(c, n-4)$ 内 R-路径总数**——$n = 7$ 是 $1764$。闭式？

— F. (n.564)

:::
