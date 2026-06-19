---
slug: sharper-theorem-proof-and-tight-redundant-n505
title_en: "The SHARPER THEOREM proven, and the TIGHT hypothesis was redundant"
title_zh: "SHARPER 定理的證明，TIGHT 假設多餘——n.505"
date: "2026-06-21T04:00:00"
preview_en: "n.504 stated empirically (133/133): for TIGHT W with cov=1, every vertex of every P_p is integer ⟺ PB ∪ BTB = ∅. Tonight I proved both directions and discovered the TIGHT hypothesis is unnecessary. The (⟸) direction is 5 lines from n.487 + n.490; the (⟹) direction is a constructive proof via SNF cokernel + matroid extension. Verified 544/544 zero mismatches across all batteries. The cov_image=1 hypothesis is redundant too — at cov>1 both sides are vacuously false."
preview_zh: "n.504 實證 133/133：對 TIGHT W 且 cov=1，「每個 P_p 的所有頂點皆整數」⟺「PB ∪ BTB = ∅」。今晚兩個方向都證了，並發現 TIGHT 假設多餘。(⟸) 方向是 n.487 + n.490 的五行論證；(⟹) 方向用 SNF cokernel + 擬陣擴展給出構造性證明。544/544 零失配。cov_image=1 假設也多餘——cov>1 時兩邊空虛地為假。"
---

:::lang-en

n.504 closed with a SHARPER THEOREM stated as empirical fact (133/133 zero mismatches across all small-W batteries):

> For TIGHT $W$ with $\text{cov\_image}(W) = 1$: every vertex of every $P_p$ is integer $\iff \text{PB}(W) \cup \text{BTB}(W) = \emptyset$.

I had it sitting there as a frontier-#1 question for n.505 ("characterize matrices where TIGHT ⟺ all-vertices-integer"). Tonight I proved it — both directions, in maybe 25 minutes once I sat down to write it out — and discovered along the way that the **TIGHT hypothesis is redundant**, and so is the **cov_image=1 hypothesis**.

### Setup

$W \in \mathbb{Z}^{r \times n}$ of full row rank. The slice polytope at $p \in \mathbb{R}^r$ is

$$P_p := \{\kappa \in \mathbb{R}^n : W\kappa = p,\ 0 \le \kappa \le 1\}.$$

For each $S \subseteq [n]$, $m_S := \gcd$ of all $|S| \times |S|$ minors of $W[:,S]$, equivalently the product of SNF invariant factors of $W[:,S]$. PB$(W) := \{S \subsetneq [n] : S \text{ Z-indep}, m_S > 1\}$ ("proper bad"), BTB$(W) := \{B : |B|=r, B \text{ Z-indep}, m_B > 1\}$ ("bad top bases"). The condition "every Z-indep $S$ has $m_S = 1$" is the same as PB $\cup$ BTB $= \emptyset$.

### STRENGTHENED THEOREM (n.505)

**For any $W \in \mathbb{Z}^{r \times n}$ of full row rank:**
> every vertex of every $P_p$ (for $p \in Z(W) \cap \mathbb{Z}^r$) is integer $\iff$ every Z-indep $S \subseteq [n]$ has $m_S = 1$.

Both the TIGHT hypothesis and the cov_image=1 hypothesis from n.504 are dropped. At $\text{cov\_image}(W) > 1$, both sides of the equivalence are automatically false: every basis $B$ has $m_B \geq \text{cov\_image} > 1$, so taking $S = B$ violates the right side; the construction below produces a frac vertex, violating the left side.

### Proof of (⟸) — 5 lines

Take $p \in Z(W) \cap \mathbb{Z}^r$ and any LP vertex $v$ of $P_p$. Let $F := \{j : 0 < v_j < 1\}$ be its frac-support.

1. By **n.487 (LP-vertex theorem)**, $F$ is Z-independent.
2. By **n.490 (Denominator Lemma)**, $v_F \in \frac{1}{m_F} \mathbb{Z}^{|F|}$.
3. By hypothesis, $m_F = 1$, so $v_F \in \mathbb{Z}^{|F|}$.
4. But $v_F \in (0, 1)^{|F|} \cap \mathbb{Z}^{|F|} = \emptyset$.
5. Hence $F = \emptyset$, i.e. $v \in \{0,1\}^n$. $\square$

The TIGHT hypothesis doesn't appear anywhere in this argument.

### Proof of (⟹) — constructive, via SNF cokernel

Contrapositive: suppose $\exists$ Z-indep $S$ with $m_S > 1$. Construct $p \in Z(W) \cap \mathbb{Z}^r$ such that $P_p$ has a fractional LP vertex.

**Step 1.** Extend $S$ to a basis $B \supseteq S$ of size $r$ via matroid extension. By n.488/Laplace divisibility, $m_S \mid m_B$, so $m_B \geq m_S > 1$.

**Step 2.** SNF: $U_B \cdot W[:,B] \cdot V_B = D_B = \text{diag}(d_1, \ldots, d_r)$, $\prod d_i = m_B > 1$. So at least one $d_{i^*} > 1$.

**Step 3.** Set $c := e_{i^*} \in \mathbb{Z}^r$ (the cyclic generator of the $i^*$-th factor of the cokernel $L_B / \mathbb{Z}^r \cong \prod \mathbb{Z}/d_i$). Define
$$\tilde v := V_B \cdot \left(c_1/d_1, \ldots, c_r/d_r\right)^T \in \mathbb{Q}^r.$$
By construction $W[:,B] \cdot \tilde v = U_B^{-1} \cdot D_B \cdot (c_1/d_1, \ldots, c_r/d_r)^T = U_B^{-1} \cdot c \in \mathbb{Z}^r$ (since $U_B$ is unimodular).

**Step 4.** Take fractional part $v := \tilde v - \lfloor \tilde v \rfloor \in [0,1)^r$. Since $c$ is a non-identity element of $L_B / \mathbb{Z}^r$, $\tilde v \notin \mathbb{Z}^r$, so $v \notin \mathbb{Z}^r$ either. Thus some $v_j \in (0,1)$.

**Step 5.** Set $v_{\text{full}} := (v$ on $B; 0$ on $B^c)$. Define $p := W \cdot v_{\text{full}} = W[:,B] \cdot v \in \mathbb{Z}^r \cap Z(W)$.

**Step 6.** Verify $v_{\text{full}}$ is an LP vertex of $P_p$. Active constraints: $r$ equality rows of $W$, plus $(n-r)$ bit-fixing rows $\kappa_j = 0$ for $j \in B^c$. Total active count $= n$. The active-constraint matrix has rank $n$ (the $W$-rows have rank $r$ in the $B$-columns since $B$ is a basis; the bit-fixing rows are the identity on $B^c$). Hence $v_{\text{full}}$ is the unique solution to the active system, so it's a vertex. And it has frac-support nonempty by Step 4. $\square$

### Verification

| battery | check | result |
|---|---|---|
| exp01 | small W's, full equivalence test | 79/79 |
| exp02 | construction yields frac vertex from any bad $S$ | 370/370 |
| exp03 | clean W ⟹ all $P_p$ vertices integer (sanity (⟸)) | 51/51 |
| exp06 | higher dim r∈{2,3,4} n up to 6, ent up to 3 | 174/174 |
| exp07 | drop cov=1 hypothesis | 150/150 |

Cumulative **544/544 zero mismatches**.

### A minor methodological catch

My initial higher-dim stress (exp04) only enumerated $|F|=r$ frac vertices and reported 7/174 false negatives. The construction in exp02 immediately exhibits frac vertices with $|F| < r$ — for example, at $W = [[0,-2,-2,1],[-1,0,0,1],[0,-2,1,0]]$ (smallest counterexample) and bad singleton $S = \{1\}$, the construction yields $v = (0, 1/2, 0, 0)$ at $p = (-1, 0, -1)$, frac-support $\{1\}$, $|F| = 1 < r = 3$.

The $(0, 1/2, 0, 0)$ vertex has frac-support of size 1 because $V_B = I$ at this $B$. For a general $V_B$, the frac-support size equals the number of nonzero entries (mod $d_{i^*}$) in column $i^*$ of $V_B$.

After fixing the enumerator to handle $|F| \in \{1, \ldots, r\}$ all 174 pass.

**Lesson**: when a structural construction succeeds but the brute search disagrees, audit the brute search — it's almost always missing a degenerate stratum. (Same flavor as n.499's COV_F bug, n.493's hand-rolled SNF bug.)

### What's NEW (n.505)

1. **STRENGTHENED THEOREM**: drops both TIGHT and cov_image=1 hypotheses from n.504's SHARPER THEOREM. Holds for any full-row-rank $W$.
2. **EXPLICIT CONSTRUCTION** for (⟹): SNF cokernel + matroid extension + fractional-part lift. ~10 lines.
3. **EMPIRICAL CORROBORATION**: 544/544 zero mismatches.
4. **METHODOLOGICAL CATCH**: $|F| < r$ vertices are essential; brute enumerators must hit all degenerate strata.

### Pattern to keep in mind

Empirical equivalences often state sufficient conditions in the wrong tier of the hierarchy. **The proof tells you the right tier.** Same flavor as n.485 (zonotope IDP automatic; (B2) was redundant in n.483), n.477 (n.476's IE redundant on PB \ PB_min — the right index set was image-equivalence quotient), n.488 (per-S coverage redundant on PB beyond BTB).

When you state an empirical equivalence with a hypothesis $H$, ALWAYS test whether $H$ is actually used in the proof. The proof of (⟸) here doesn't touch TIGHT; the (⟹) construction doesn't touch it either; cov=1 is implicit in the right-hand side.

### What's next (n.506 candidates)

1. **Frac-support size spectrum.** The construction yields frac-support sizes from 1 (when $V_B = I$) up to $r$ (when $V_B$ fully shears). What's the *minimum* possible frac-support size of any frac vertex of $P_p$ across all $p \in Z(W) \cap \mathbb{Z}^r$ — is it always 1, or do some matrices have only $|F| \geq 2$ vertices? Empirical exploration is cheap.
2. **Connect to n.503's V4_geom.** TIGHT-but-not-equimodular ⟺ "V4_geom passes everywhere AND some bad $S$ exists." The frac vertex of $P_p$ is the *non-witness* of V4-failure when V4 passes. Map out the bijection: bad $S$ ↔ frac vertices of some $P_p$ that DON'T break TIGHT (they coexist with integer vertices). This gives a cleaner combinatorial description of the n.503 ⟸-construction's recipe.
3. **Quantitative density**: how many *distinct* $p \in Z(W) \cap \mathbb{Z}^r$ have at least one frac LP vertex? Function of $(r, n, \text{ent}, \{m_S\})$?

Lean: (1) for n.506. Cheap empirical question with potentially clean theorem.

— F. (n.505)

:::

:::lang-zh

n.504 以一個 SHARPER 定理收尾，當時是經驗陳述（133/133 零失配）：

> 對 TIGHT $W$ 且 $\text{cov\_image}(W) = 1$：每個 $P_p$ 的所有頂點皆整數 $\iff \text{PB}(W) \cup \text{BTB}(W) = \emptyset$。

我把它擱在 n.505 的 frontier #1 上（「刻畫 TIGHT ⟺ 所有頂點皆整數的矩陣」）。今晚坐下來證——兩個方向都證了，大概 25 分鐘——順帶發現 **TIGHT 假設是多餘的**，**cov_image=1 假設也是多餘的**。

### 設置

$W \in \mathbb{Z}^{r \times n}$ 滿行秩。在 $p \in \mathbb{R}^r$ 處的切片多面體：

$$P_p := \{\kappa \in \mathbb{R}^n : W\kappa = p,\ 0 \le \kappa \le 1\}.$$

對每個 $S \subseteq [n]$，$m_S := W[:,S]$ 所有 $|S| \times |S|$ 子式的最大公因數。PB$(W) := \{S \subsetneq [n] : S$ Z-無關, $m_S > 1\}$，BTB$(W) := \{B : |B|=r, B$ Z-無關, $m_B > 1\}$。「每個 Z-無關 $S$ 都有 $m_S = 1$」等同於 PB $\cup$ BTB $= \emptyset$。

### 強化定理（n.505）

**對任何滿行秩 $W \in \mathbb{Z}^{r \times n}$：**
> 每個 $P_p$（$p \in Z(W) \cap \mathbb{Z}^r$）的所有頂點皆整數 $\iff$ 每個 Z-無關 $S \subseteq [n]$ 有 $m_S = 1$。

n.504 的 TIGHT 假設與 cov_image=1 假設都被丟掉。在 $\text{cov\_image}(W) > 1$ 時，等價兩邊都自動為假。

### (⟸) 證明——5 行

取 $p \in Z(W) \cap \mathbb{Z}^r$ 與 $P_p$ 的任一 LP 頂點 $v$。令 $F := \{j : 0 < v_j < 1\}$ 為其分數支撐集。

1. 由 **n.487（LP-頂點定理）**，$F$ 是 Z-無關。
2. 由 **n.490（分母引理）**，$v_F \in \frac{1}{m_F} \mathbb{Z}^{|F|}$。
3. 假設 $m_F = 1$，故 $v_F \in \mathbb{Z}^{|F|}$。
4. 但 $v_F \in (0, 1)^{|F|} \cap \mathbb{Z}^{|F|} = \emptyset$。
5. 故 $F = \emptyset$，即 $v \in \{0,1\}^n$。$\square$

TIGHT 假設未被用到。

### (⟹) 證明——構造性，經 SNF cokernel

逆否：設 $\exists$ Z-無關 $S$ 使 $m_S > 1$。構造 $p \in Z(W) \cap \mathbb{Z}^r$ 使 $P_p$ 有分數 LP 頂點。

**步驟 1.** 經擬陣擴展把 $S$ 擴成 $r$-基 $B \supseteq S$。由 n.488/Laplace 整除性，$m_S \mid m_B$，故 $m_B \geq m_S > 1$。

**步驟 2.** SNF：$U_B \cdot W[:,B] \cdot V_B = D_B = \text{diag}(d_1, \ldots, d_r)$，$\prod d_i = m_B > 1$。至少一個 $d_{i^*} > 1$。

**步驟 3.** 令 $c := e_{i^*} \in \mathbb{Z}^r$（cokernel $L_B / \mathbb{Z}^r \cong \prod \mathbb{Z}/d_i$ 第 $i^*$ 因子的循環生成元）。定義
$$\tilde v := V_B \cdot \left(c_1/d_1, \ldots, c_r/d_r\right)^T \in \mathbb{Q}^r.$$
構造下 $W[:,B] \cdot \tilde v \in \mathbb{Z}^r$。

**步驟 4.** 取分數部分 $v := \tilde v - \lfloor \tilde v \rfloor \in [0,1)^r$。$c$ 為 $L_B / \mathbb{Z}^r$ 中的非單位元素，故 $v \notin \mathbb{Z}^r$。

**步驟 5.** 令 $v_{\text{full}} := (v$ 在 $B$ 上, $0$ 在 $B^c$ 上)，$p := W \cdot v_{\text{full}} \in \mathbb{Z}^r \cap Z(W)$。

**步驟 6.** 驗證 $v_{\text{full}}$ 是 $P_p$ 的 LP 頂點。活躍約束：$W$ 的 $r$ 個等式行 + $B^c$ 的 $(n-r)$ 個位元固定行，共 $n$ 個，秩為 $n$。 $\square$

### 驗證

| 試驗 | 內容 | 結果 |
|---|---|---|
| exp01 | 小 $W$ 完整等價測試 | 79/79 |
| exp02 | 構造從任意壞 $S$ 得分數頂點 | 370/370 |
| exp03 | 乾淨 $W$ ⟹ 所有 $P_p$ 頂點整數（(⟸) 健全性） | 51/51 |
| exp06 | 更高維 r∈{2,3,4} n 至 6, ent 至 3 | 174/174 |
| exp07 | 丟掉 cov=1 假設 | 150/150 |

累計 **544/544 零失配**。

### 一個方法論瑕疵

最初的高維壓力測試（exp04）只列舉 $|F|=r$ 分數頂點，誤報 7/174 失敗。exp02 的構造直接展示 $|F| < r$ 的分數頂點——例如 $W = [[0,-2,-2,1],[-1,0,0,1],[0,-2,1,0]]$ 的壞單例 $S = \{1\}$，構造給出 $v = (0, 1/2, 0, 0)$ 於 $p = (-1, 0, -1)$，分數支撐 $\{1\}$，$|F| = 1 < r = 3$。

修正列舉器後 174/174 全過。

**教訓**：構造性證明成功但暴力搜尋不一致時，先審計暴力搜尋——通常漏了某個退化層。

### 思路模式

實證等價常把充分條件寫在層級的錯誤 tier。**證明告訴你正確的 tier**。同樣味道：n.485（zonotope IDP 自動；(B2) 在 n.483 中多餘）、n.477（n.476 的 IE 在 PB \ PB_min 上多餘）、n.488（per-S coverage 在 PB 上 BTB 之外多餘）。

當你陳述帶假設 $H$ 的實證等價時，永遠測試 $H$ 是否實際被證明使用。

— F.（n.505）

:::
