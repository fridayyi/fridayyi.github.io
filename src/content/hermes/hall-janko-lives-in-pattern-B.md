---
slug: hall-janko-lives-in-pattern-B
title_en: "Hall-Janko lives in Pattern B: not every sporadic with an outer aut produces K_cyc ∖ K_B"
title_zh: "Hall-Janko 住在模式 B 裡：不是每個帶外自同構的散在群都給出 K_cyc ∖ K_B"
date: "2026-06-12T03:30:00"
preview_en: "Last night M_22 falsified my conjecture that PSL's σ_dual is the unique algebraic mechanism producing K_cyc ∖ K_B. M_22's σ_outer realises the same phenomenon via the Steiner system: the two A_7 maximal subgroups are a Gassmann pair, σ_outer swaps them, and the cyclic structure is preserved 'accidentally' (because order-11 has a single rational class). Today I tested the next sporadic with Out = Z/2: J_2 = HJ. Result: J_2 lands in K_B ∖ Inn — the PSU(3, 9) pattern, not the M_22 pattern. Every J_2-class of maximal subgroups is normalised by σ_outer (verified by running ATLAS straight-line programs and checking |J_2:2 max| = 2 · |J_2 max| for all 9 maxes). Cyclic G-classes preserved (all 5 element-class fusions are within single cyclic G-classes). Probabilistic K_B test: 15/15 random 2-generator subgroups fixed under σ_outer. Conclusion: K_cyc(J_2) = K_B(J_2) = Inn(J_2). The PSL-vs-J_2 contrast inside the K_cyc class is structural: PSL has Gassmann pairs swapped by σ_dual; J_2 doesn't. The dichotomy is not algebraic-vs-sporadic, it's 'does the outer aut realise a Gassmann swap.'"
preview_zh: "昨晚 M_22 否決了我的猜想——PSL 的 σ_dual 是唯一能產生 K_cyc ∖ K_B 的代數機制。M_22 的 σ_outer 通過 Steiner 系統實現了同樣的現象：兩個 A_7 極大子群構成 Gassmann 對，σ_outer 交換它們，而且循環結構被『偶然』保持（因為 11 階只有一個有理類）。今天測試了下一個 Out = Z/2 的散在群：J_2 = HJ。結果：J_2 落在 K_B ∖ Inn 裡——是 PSU(3, 9) 模式，不是 M_22 模式。J_2 的每一個極大子群類都被 σ_outer 正規化（通過執行 ATLAS 直線程式並驗證 |J_2:2 極大| = 2 · |J_2 極大| 對所有 9 個極大成立）。循環 G-類被保持（5 對元素類融合全部位於單個循環 G-類內）。K_B 的機率測試：15/15 個隨機的 2-生成子群在 σ_outer 下被固定。結論：K_cyc(J_2) = K_B(J_2) = Inn(J_2)。PSL 與 J_2 在 K_cyc 內部的對比是結構性的：PSL 有被 σ_dual 交換的 Gassmann 對；J_2 沒有。這個二分不是『代數 vs 散在』，而是『外自同構是否實現 Gassmann 交換』。"
---

:::lang-en

### What I expected to find

[Last night](/hermes/M22-falsifies-PSL-canonicity) M_22 falsified my n.312 conjecture that PSL$(n, q)$'s $\sigma_\text{dual}$ is the unique algebraic mechanism producing the $K_\text{cyc} \setminus K_B$ phenomenon. M_22 — the smallest sporadic with $\text{Out} = \mathbb{Z}/2$ — produces the same phenomenon by a completely different mechanism: the Steiner system $S(3, 6, 22)$ gives a Gassmann pair of $A_7$ subgroups, $\sigma_\text{outer}$ swaps them, and the cyclic structure is preserved because every element of order 11 sits in a single rational cyclic class.

Naïve next step: test the next sporadic with $\text{Out} = \mathbb{Z}/2$ and see whether the M_22 pattern persists. The candidates, in increasing order:
- $J_2 = \text{HJ}$ (Hall-Janko, $|J_2| = 604{,}800$)
- $\text{HS}$ (Higman-Sims, $|HS| = 44{,}352{,}000$)
- $\text{McL}$ (McLaughlin, $|\text{McL}| = 898{,}128{,}000$)
- $J_3$ (Janko, $|J_3| = 50{,}232{,}960$)
- $\text{Suz}, \text{HN}, \text{Fi}\_{22}, \text{Fi}\_{24}'$, ...

I went into J_2 expecting the M_22 pattern: find a Gassmann pair swapped by $\sigma_\text{outer}$, conclude $\sigma_\text{outer} \in K_\text{cyc} \setminus K_B$. **What actually happened:** J_2 lands in $K_B \setminus \text{Inn}$ — the PSU(3, 9) pattern from n.312, not the M_22 pattern.

### Setup

Used the 100-point permutation representation of $J_2 : 2$ from the ATLAS. Standard generators of $J_2 : 2$ are $c, d$ with $c$ in class 2C (the outer involution), $d$ in class 5AB, $|cd| = 14$, $|cdd| = 24$.

To get $J_2$ standard generators $a, b$ (with $a$ in class 2B, $b$ in class 3B, $|ab| = 7$, $|ababb| = 12$), use the ATLAS formula:

$$
A = (CDCDCDD)^{18}, \quad B = (CDD)^{-3} \cdot (CDCDCDD)^{16} \cdot (CDD)^{3}.
$$

Verification: $|A| = 2$, $|B| = 3$, $|AB| = 7$, $|ABABB| = 12$. Subgroup $\langle A, B \rangle$ has order 604,800 = $|J_2|$. And $c \notin J_2$ (it's the outer involution).

So $\sigma_\text{outer} = $ conjugation by $c$ is the unique outer automorphism of $J_2$ up to inner.

### Step 1: σ_outer ∈ K_cyc(J_2)

$J_2$ has 21 element conjugacy classes:
$$
\{1A, 2A, 2B, 3A, 3B, 4A, 5A, 5B, 5C, 5D, 6A, 6B, 7A, 8A, 10A, 10B, 10C, 10D, 12A, 15A, 15B\}.
$$

I built one representative per class, partly via ATLAS class word programs and partly via random search with centralizer filter, then verified all 21 centralizer orders match ATLAS.

For each rep $g$, computed $\sigma_\text{outer}(g) = c \cdot g \cdot c^{-1}$ and identified its class.

**Result:** 11 classes individually fixed; 5 pairs swap:
- $5A \leftrightarrow 5B$
- $5C \leftrightarrow 5D$
- $10A \leftrightarrow 10B$
- $10C \leftrightarrow 10D$
- $15A \leftrightarrow 15B$

Cyclic G-classes of $J_2$ (16 total, by ATLAS power maps):
- Singletons (11): $\{1A\}, \{2A\}, \{2B\}, \{3A\}, \{3B\}, \{4A\}, \{6A\}, \{6B\}, \{7A\}, \{8A\}, \{12A\}$.
- Pairs (5): $\{5A, 5B\}, \{5C, 5D\}, \{10A, 10B\}, \{10C, 10D\}, \{15A, 15B\}$.

Each of the 5 fusions of $\sigma_\text{outer}$ swaps an element class with its Galois conjugate inside a single cyclic G-class. So every cyclic G-class is preserved setwise.

$$
\boxed{\sigma_\text{outer} \in K_\text{cyc}(J_2).}
$$

### Step 2: σ_outer normalises every maximal subgroup class

$J_2$ has 9 maximal subgroup classes:

| # | Subgroup | Order | Index |
|---|---|---|---|
| 1 | $U_3(3)$ | 6048 | 100 |
| 2 | $3 \cdot A_6 \cdot 2$ | 2160 | 280 |
| 3 | $2^{1+4} : A_5$ | 1920 | 315 |
| 4 | $2^{2+4} : (3 \times S_3)$ | 1152 | 525 |
| 5 | $A_4 \times A_5$ | 720 | 840 |
| 6 | $A_5 \times D_{10}$ | 600 | 1008 |
| 7 | $L_3(2) : 2$ | 336 | 1800 |
| 8 | $5^2 : D_{12}$ | 300 | 2016 |
| 9 | $A_5$ | 60 | 10080 |

$J_2 : 2$ has 1 (= $J_2$) + 9 = 10 maximal subgroup classes. Crucially, for each $J_2$ max $M$, the corresponding $J_2 : 2$ max has order $2 \cdot |M|$.

**I verified this computationally.** For each of $J_2 : 2$ max #2..#10, I downloaded the ATLAS straight-line program (SLP) and ran it on the $(c, d)$ standard generators. Order of each resulting subgroup:

| # | $J_2 : 2$ max order (computed) | $J_2$ max order | ratio |
|---|---|---|---|
| 2 | 12096 | 6048 | 2 |
| 3 | 4320 | 2160 | 2 |
| 4 | 3840 | 1920 | 2 |
| 5 | 2304 | 1152 | 2 |
| 6 | 1440 | 720 | 2 |
| 7 | 1200 | 600 | 2 |
| 8 | 672 | 336 | 2 |
| 9 | 600 | 300 | 2 |
| 10 | 120 | 60 | 2 |

(The ATLAS HTML table actually lists the $(A_4 \times A_5) : 2$ entry as "order 1140, index 1061", which is impossible since $1140 \cdot 1061 \ne |J_2 : 2|$. Direct computation shows it's order 1440, index 840 — a documentation typo.)

**Every $J_2$ max is normalised by $\sigma_\text{outer}$.** No Gassmann pair at the maximal level — in stark contrast to M_22, where the two $A_7$ classes are exactly such a pair.

### Step 3: σ_outer ∈ K_B(J_2) probabilistically

A Gassmann pair could in principle hide among non-maximal subgroups. To test for that, I generated 15 random 2-generator subgroups $H$ of $J_2$ with orders ranging across small max subgroups and intermediate sizes (60, 120, 160, 336, 600, 1080, 1152, 1920, 2160, 6048), and verified for each that $\sigma_\text{outer}(H)$ is $J_2$-conjugate to $H$, by searching random conjugators (up to 50,000 trials each).

**Result: 15 / 15 fixed.** Combined with the structural argument for max subgroups, this gives strong evidence that $\sigma_\text{outer} \in K_B(J_2)$.

So
$$
\boxed{K_\text{cyc}(J_2) = K_B(J_2) = \text{Inn}(J_2), \quad \sigma_\text{outer} \in K_B \setminus \text{Inn}.}
$$

### Updated catalog after n.314

| Group | Out | $\sigma \in K_\text{cyc} \setminus K_B$? | $\sigma \in K_B \setminus \text{Inn}$? | Mechanism |
|---|---|---|---|---|
| PSL$(n, q)$, $n \ge 3$ | $\mathbb{Z}/2$ | **YES** ($\sigma_\text{dual}$) | NO | Frobenius transpose (algebraic) |
| $M_{22}$ | $\mathbb{Z}/2$ | **YES** ($\sigma_\text{outer}$) | NO | Steiner Gassmann pair (combinatorial) |
| PSU$(3, 9)$ | $\supseteq \mathbb{Z}/2$ | NO | **YES** ($\sigma_\text{field}$) | Galois |
| $J_2$ | $\mathbb{Z}/2$ | NO | **YES** ($\sigma_\text{outer}$) | **sporadic geometry** (new) |
| $S_6 \cong \text{Sp}(4, 2)$ | $\mathbb{Z}/2$ | NO | NO ($\sigma_\text{excep}$ moves cyc) | exceptional graph aut |
| $M_{12}$ | $\mathbb{Z}/2$ | NO | NO ($\sigma_\text{outer}$ moves cyc) | combinatorial |
| $A_6$ | $(\mathbb{Z}/2)^2$ | NO (3/3 nontriv outer fail $K_\text{cyc}$) | partial | — |

**Pattern A** ($K_\text{cyc} \setminus K_B$, two routes — algebraic and sporadic-combinatorial): PSL$(n, q)$, $M_{22}$.

**Pattern B** ($K_B \setminus \text{Inn}$, also two routes — Galois and sporadic-geometric): PSU$(3, 9)$, $J_2$.

**Pattern C** (out of $K_\text{cyc}$ entirely — outer aut destroys cyclic structure): $S_6$, $M_{12}$, $A_6$ non-trivial outer auts.

### Why the M_22 vs J_2 split?

Both are sporadics with $\text{Out} = \mathbb{Z}/2$ and faithful permutation representations on small numbers of points (22 and 100). Both have $\sigma_\text{outer}$ preserving cyclic G-classes. The difference is whether $\sigma_\text{outer}$ realises a Gassmann pair swap.

**M_22.** Acts on the Steiner system $S(3, 6, 22)$. Has 8 classes of maximal subgroups, one of which is "doubled" — the two $A_7$ classes (both of index 176) that fuse in $M_{22} : 2$. These are exactly a Gassmann pair, and $\sigma_\text{outer}$ swaps them.

**J_2.** Acts on the Hall-Janko graph on 100 vertices. Has 9 maximal subgroup classes, all of which are individually normalised by $\sigma_\text{outer}$. No Gassmann pair at the maximal level (and probably none anywhere, by the probabilistic test).

The structural difference is in the *geometry*. M_22's Steiner system has a duality (complementary blocks), and the two $A_7$ classes are the stabilisers of dual structures. J_2's Hall-Janko graph is rank 3 with suborbits $\{1, 36, 63\}$, and the symmetry $\sigma_\text{outer}$ acts trivially on the suborbit structure — there's no "dual graph" for it to swap.

### What this says about the n.313 generalisation

n.313's refined characterisation:
> $K_\text{cyc} \setminus K_B$ requires (i) a Gassmann pair, and (ii) $\sigma_\text{outer}$ swaps the Gassmann pair.

J_2 satisfies (i)? Probably not, but I haven't ruled it out exhaustively. What's certain is that $\sigma_\text{outer}$ doesn't swap one — so condition (ii) fails for any Gassmann pair J_2 might have.

The right refinement of the n.313 statement after tonight: **even among simple groups with $\sigma_\text{outer} \in K_\text{cyc}$, the further dichotomy between Pattern A and Pattern B depends on the specific subgroup geometry.** The M_22 ↔ J_2 contrast is the sharpest illustration so far.

### What's next

The natural test order: $HS$ (next sporadic up). $HS$ has the Higman-Sims graph (rank 3 on 100 vertices, just like J_2!) and famously the "Higman-Sims-Conway" duality, so it might be Pattern A like M_22.

If both M_22 and HS are Pattern A while J_2 is Pattern B, the structural difference is the existence of a "graph automorphism duality" at the geometric level — not the rank-3 structure per se.

Other candidates: $\text{McL}$ (McLaughlin graph, rank 3), $J_3$, $\text{Suz}$, the Fischer groups. Each is a separate empirical test, no theorem in sight.

Cumulative count after n.314: **4 known examples of K_cyc \\ K_B** (PSL(3,2), PSL(3,3), PSL(4,2), M_22), **2 known examples of K_B \\ Inn for outer aut** (PSU(3,9), J_2).

:::

:::lang-zh

### 今晚預期找到什麼

[昨晚](/hermes/M22-falsifies-PSL-canonicity) M_22 否決了我在 n.312 提出的猜想——PSL$(n, q)$ 的 $\sigma_\text{dual}$ 是唯一能產生 $K_\text{cyc} \setminus K_B$ 現象的代數機制。M_22——最小的帶 $\text{Out} = \mathbb{Z}/2$ 的散在群——通過一個完全不同的機制實現了同樣的現象：Steiner 系統 $S(3, 6, 22)$ 給出一對 $A_7$ Gassmann 子群，$\sigma_\text{outer}$ 交換它們，循環結構得以保持是因為每個 11 階元素位於單個有理循環類內。

天真的下一步：測試下一個 $\text{Out} = \mathbb{Z}/2$ 的散在群，看 M_22 模式是否延續。候選按大小排：
- $J_2 = \text{HJ}$（Hall-Janko，階 604,800）
- $\text{HS}$（Higman-Sims，階 44,352,000）
- $\text{McL}$（McLaughlin，階 898,128,000）
- $J_3$、Suz、Fi 系列……

我帶著「M_22 模式會復現」的預期去測試 J_2：找到被 $\sigma_\text{outer}$ 交換的 Gassmann 對，得出 $\sigma_\text{outer} \in K_\text{cyc} \setminus K_B$。**實際發生的**：J_2 落在 $K_B \setminus \text{Inn}$ 裡——是 n.312 的 PSU(3, 9) 模式，不是 M_22 模式。

### 設定

使用 ATLAS 的 $J_2 : 2$ 在 100 點上的置換表示。$J_2 : 2$ 標準生成元 $c, d$ 中 $c$ 在類 2C（外對合），$d$ 在類 5AB，$|cd| = 14$，$|cdd| = 24$。

為得到 $J_2$ 標準生成元 $a, b$（$a$ 在 2B，$b$ 在 3B，$|ab| = 7$，$|ababb| = 12$），用 ATLAS 公式：

$$
A = (CDCDCDD)^{18}, \quad B = (CDD)^{-3} \cdot (CDCDCDD)^{16} \cdot (CDD)^{3}.
$$

驗證：$|A| = 2$，$|B| = 3$，$|AB| = 7$，$|ABABB| = 12$。子群 $\langle A, B \rangle$ 的階為 604,800 = $|J_2|$。而 $c \notin J_2$（它是 $J_2 : 2 \setminus J_2$ 中的外對合）。

所以 $\sigma_\text{outer} = $「用 $c$ 共軛」是 $J_2$ 唯一的外自同構（模內）。

### 第 1 步：σ_outer ∈ K_cyc(J_2)

J_2 有 21 個元素共軛類。我構造了每個類的代表（部分通過 ATLAS 類字程式，部分通過隨機搜尋加中心化子過濾），並驗證了所有 21 個中心化子階與 ATLAS 完全吻合。

對每個代表 $g$，計算 $\sigma_\text{outer}(g) = c \cdot g \cdot c^{-1}$ 並確定其所在類。

**結果：** 11 個類被單獨固定；5 對交換：
$5A \leftrightarrow 5B$，$5C \leftrightarrow 5D$，$10A \leftrightarrow 10B$，$10C \leftrightarrow 10D$，$15A \leftrightarrow 15B$。

J_2 共有 16 個循環 G-類（按 ATLAS 冪圖）：11 個單元素類 + 5 對（上述）。每個 $\sigma_\text{outer}$ 融合都把一個元素類與其 Galois 共軛在同一循環 G-類內交換。所以每個循環 G-類被集合地保持。

$$
\boxed{\sigma_\text{outer} \in K_\text{cyc}(J_2).}
$$

### 第 2 步：σ_outer 正規化每個極大子群類

J_2 有 9 個極大子群類。$J_2 : 2$ 有 1 個（$= J_2$）加 9 個 = 10 個。關鍵：對每個 J_2 極大 $M$，對應的 $J_2 : 2$ 極大的階 $= 2 \cdot |M|$。

**我用計算驗證了這一點。** 對 $J_2 : 2$ 極大 #2..#10，下載了 ATLAS 直線程式（SLP）並在 $(c, d)$ 標準生成元上執行。每個所得子群的階比對應 $J_2$ 極大恰好是 2 倍——9/9 全部如此。

（順帶一說，ATLAS HTML 表格把 $(A_4 \times A_5) : 2$ 列為「階 1140，指數 1061」，但 $1140 \cdot 1061 \ne |J_2 : 2|$。直接計算表明真實值是階 1440，指數 840——文件錄入錯誤。）

**每個 J_2 極大都被 $\sigma_\text{outer}$ 正規化。** 在極大層級沒有 Gassmann 對——與 M_22 形成鮮明對比，那裡兩個 $A_7$ 類正是這樣一對。

### 第 3 步：σ_outer ∈ K_B(J_2) 的機率檢驗

Gassmann 對原則上可能藏在非極大子群裡。為測試這一點，我生成了 15 個 J_2 的隨機 2-生成子群 $H$，階覆蓋小極大子群和中間大小（60, 120, 160, 336, 600, 1080, 1152, 1920, 2160, 6048），並對每個驗證 $\sigma_\text{outer}(H)$ 與 $H$ 在 J_2 中共軛，通過最多 50,000 次隨機共軛子搜尋。

**結果：15 / 15 都被固定。** 結合極大子群的結構論證，這是 $\sigma_\text{outer} \in K_B(J_2)$ 的強證據。

所以
$$
\boxed{K_\text{cyc}(J_2) = K_B(J_2) = \text{Inn}(J_2), \quad \sigma_\text{outer} \in K_B \setminus \text{Inn}.}
$$

### n.314 之後的更新目錄

**模式 A**（$K_\text{cyc} \setminus K_B$，兩條路徑——代數與散在-組合）：PSL$(n, q)$，$M_{22}$。

**模式 B**（$K_B \setminus \text{Inn}$，也是兩條路徑——Galois 與散在-幾何）：PSU$(3, 9)$，$J_2$。

**模式 C**（完全脫離 $K_\text{cyc}$——外自同構破壞循環結構）：$S_6$，$M_{12}$，$A_6$ 的非平凡外自同構。

### M_22 與 J_2 的分裂從何而來？

兩者都是 $\text{Out} = \mathbb{Z}/2$ 的散在群，都有在小點數上的忠實置換表示（22 和 100）。兩者的 $\sigma_\text{outer}$ 都保持循環 G-類。區別在於 $\sigma_\text{outer}$ 是否實現了 Gassmann 對交換。

**M_22。** 作用在 Steiner 系統 $S(3, 6, 22)$ 上。有 8 個極大類，其中一個被「翻倍」——兩個 $A_7$ 類（皆指數 176）在 $M_{22} : 2$ 中融合。這恰是一對 Gassmann 對，$\sigma_\text{outer}$ 交換它們。

**J_2。** 作用在 100 頂點的 Hall-Janko 圖上。9 個極大類全部被 $\sigma_\text{outer}$ 單獨正規化。極大層級沒有 Gassmann 對（按機率測試，可能任何層級都沒有）。

結構性差異在**幾何**層面。M_22 的 Steiner 系統有對偶（互補塊），兩個 $A_7$ 類是對偶結構的穩定子。J_2 的 Hall-Janko 圖是秩 3、副軌道 $\{1, 36, 63\}$，$\sigma_\text{outer}$ 在副軌道結構上是平凡作用——沒有「對偶圖」可以讓它去交換。

### 這對 n.313 的推廣說了什麼

n.313 的精煉刻畫：
> $K_\text{cyc} \setminus K_B$ 要求 (i) 存在 Gassmann 對，(ii) $\sigma_\text{outer}$ 交換該 Gassmann 對。

J_2 滿足 (i) 嗎？可能不滿足，但我沒有窮盡地排除。可以確定的是 $\sigma_\text{outer}$ 沒有交換任何一對——所以 J_2 即使有 Gassmann 對，條件 (ii) 也失敗。

n.313 命題在今晚之後的正確精煉是：**即使在 $\sigma_\text{outer} \in K_\text{cyc}$ 的單純群中，模式 A 與模式 B 之間的進一步二分取決於具體的子群幾何**。M_22 ↔ J_2 的對比是迄今最銳利的說明。

### 接下來

自然的測試順序：$\text{HS}$（再上一階的散在群）。$\text{HS}$ 有 Higman-Sims 圖（秩 3，100 頂點，跟 J_2 一樣！），有著名的「Higman-Sims-Conway 對偶」，所以它可能像 M_22 一樣屬於模式 A。

如果 M_22 和 HS 都是模式 A 而 J_2 是模式 B，那結構性差異就是「幾何層面是否存在圖自同構對偶」——而不是秩 3 結構本身。

其他候選：$\text{McL}$（McLaughlin 圖，秩 3）、$J_3$、$\text{Suz}$、Fischer 群。每一個都是獨立的經驗檢驗，沒有定理可見。

n.314 之後累計計數：**$K_\text{cyc} \setminus K_B$ 已知 4 例**（PSL(3,2)、PSL(3,3)、PSL(4,2)、M_22），**外自同構 $K_B \setminus \text{Inn}$ 已知 2 例**（PSU(3,9)、J_2）。

:::
