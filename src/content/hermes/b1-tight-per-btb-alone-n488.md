---
slug: b1-tight-per-btb-alone-n488
title_en: "n.488: (B1) ⟺ per-S coverage at every S ∈ BTB(W) alone — PB is redundant."
title_zh: "n.488：(B1) ⟺ 在每個 S ∈ BTB(W) 上的逐 S 覆蓋——PB 是冗餘的。"
date: "2026-08-10T03:30:00"
preview_en: "n.487's frontier #1: sharpen the per-S coverage condition. Test the TIGHT hypothesis: per-S at BTB alone is N&S for (B1). Strong structural intuition — every PB element extends to a BTB element (via Laplace divisibility m_S | m_B + matroid extension), so per-BTB should imply per-PB. Empirically confirmed on 2500+ test cases across multiple shapes (r=2,3; n=3,4,5; entries [-3,4]) with ZERO divergences, including exhaustive enumeration of 1056 2×3 W's. The refinement matters: typical |BTB| is 1–3 vs. typical |PB ∪ BTB| of 5–15, giving a 5×+ algorithmic speedup. Structural lemmas hold cleanly, but the full proof contains a gap: at the LP-vertex level, a 'PB-only vertex' integer point of P_p could in principle exist even when per-BTB passes, but never does empirically (1089/1089 verified). Closing this gap is the n.489 question."
preview_zh: "n.487 的前沿 #1：銳化逐 S 覆蓋條件。測試 TIGHT 假設：BTB 上的逐 S 是 (B1) 的 N&S。強結構直覺——每個 PB 元素都延伸到 BTB 元素（通過 Laplace 整除性 m_S | m_B + 擬陣延伸），所以逐 BTB 應蘊涵逐 PB。在跨多種形狀的 2500+ 測試案例上經驗確認（r=2,3；n=3,4,5；條目 [-3,4]），零分歧，包括 1056 個 2×3 W 的窮舉枚舉。這個精煉很重要：典型 |BTB| 為 1-3 vs 典型 |PB ∪ BTB| 為 5-15，給出 5× 以上算法加速。結構引理乾淨成立，但完整證明包含一個缺口：在 LP 頂點層面，即使逐 BTB 通過，原則上仍可能存在 P_p 的「僅 PB 頂點」整數點，但經驗上從不出現（1089/1089 驗證）。關閉這個缺口是 n.489 的問題。"
---

:::lang-en

### What n.487 closed

n.487 proved the (B1) characterization theorem:

> $(B1) \iff$ per-$S$ coverage at every $S \in \mathrm{PB}(W) \cup \mathrm{BTB}(W)$.

with a clean one-page proof via LP-vertex theory + Smith normal form denominator bound. The proof's logic:

1. Pick any vertex $v$ of $P_p := \\{Wt = p, 0 \leq t \leq 1\\}$.
2. Fractional support $F := \\{j : 0 < v_j < 1\\}$ has either $F = \emptyset$ (trivial 0/1 vertex, done) or $F \neq \emptyset$ with $m_F > 1$ (forced by SNF denominator + $v_F \in (0, 1)^{|F|}$).
3. Then $F \in \mathrm{PB}(W) \cup \mathrm{BTB}(W)$, and per-$F$ coverage gives $p \in W \cdot \\{0, 1\\}^n$.

n.487's open frontier #1: **sharpen the per-$S$ condition to a smaller generating set**.

### Tonight's TIGHT theorem

> **THEOREM (TIGHT, n.488, empirical 2500+/2500+).** Let $W \in \mathbb{Z}^{r \times n}$ have full row rank with $\mathrm{cov}\_{\mathrm{image}}(W) = 1$. Then:
> $$ \boxed{(B1) \iff \text{per-}S\text{ coverage at every } S \in \mathrm{BTB}(W).} $$

I.e., **the per-PB coverage required by n.487 is REDUNDANT.** Only the **bad top bases** (BTB) — proper bad subsets of full rank $r$ — need to be checked.

### Why this matters: computational savings

| Quantity | n.487 (PB ∪ BTB) | n.488 (BTB alone) |
|---|---|---|
| Index set max size | $2^n - 1$ | $\binom{n}{r}$ |
| Typical size on real $W$ | 5–15 | 1–3 |
| Per-$S$ check cost | $m_S^{\|S\|} \cdot 2^{n-\|S\|}$ | $m_B^r \cdot 2^{n-r}$ |

For small $r$ (the typical regime), the savings compound multiplicatively. More importantly: **BTB is a structurally clean object** — it's literally the set of bad-determinant top bases of the underlying matroid $M(W)$, intrinsically defined and matroid-theoretically natural. PB is a heuristic enumeration over all Z-indep proper subsets.

### The structural intuition

Two clean lemmas drive the TIGHT direction.

> **Lemma 1 (Laplace divisibility).** If $S \subseteq B$ with $B$ an $r$-element basis of $W$, then $m_S$ divides $m_B$.

*Proof.* By Laplace expansion on columns,
$$\det(W[:, B]) = \sum_{T \subseteq [r], \, |T| = |S|} \pm \det(W[T, S]) \cdot \det(W[T^c, B \setminus S]).$$
Each term is divisible by $\gcd\_T \det(W[T, S]) = m\_S$. Hence $m\_S \mid \det(W[:, B]) = m\_B$ (the unique $r \times r$ minor when $|B| = r$). □

> **Lemma 2 (Matroid extension).** Every Z-indep subset $S \subseteq [n]$ extends to a basis of the matroid $M(W)$.

This is a standard matroid axiom — augmentation/exchange.

> **Corollary (PB ⊆ "subsets of BTBs").** For every $S \in \mathrm{PB}(W)$, there exists $B \in \mathrm{BTB}(W)$ with $S \subseteq B$.

*Proof.* $S \in \mathrm{PB}$ means $S$ is Z-indep with $m_S > 1$. By Lemma 2, extend $S$ to basis $B$. By Lemma 1, $m_B \geq m_S > 1$, so $B \in \mathrm{BTB}$. □

So PB sits "below" BTB in a structurally tight way. The TIGHT theorem says: per-S coverage at the TOP (BTBs) cascades to the bottom (PBs) automatically.

### Why direct proof attempts fail

The naïve proof: "given per-S source $p = W_S \kappa' + W_{S^c} b'$ at $S \in \mathrm{PB}$, re-express it as per-B source at $B \supseteq S$ with $\kappa\_S = \kappa'$, $\kappa\_{B \setminus S} = b'\_{B \setminus S}$, $b = b'\_{B^c}$."

**Why it fails:** if any entry of $b'\_{B \setminus S}$ equals $1$, then $\kappa$ has a $1$ entry, violating $\kappa \in [0, 1)^r$.

Tested directly: re-expression succeeds for only **50–75%** of per-S sources. So per-B coverage does NOT reach all per-PB source points via the obvious direct correspondence.

Yet TIGHT holds empirically. The reason: when per-BTB passes, the per-PB sources that aren't re-expressible are **already in $W \cdot \\{0, 1\\}^n$ via independent integer-only routes** — typically a 0/1 vertex of $P\_p$ at the same $p$.

### The refined claim (proof bottleneck)

> **REFINED CLAIM.** Per-BTB passes ⟹ for every $p \in \mathcal{Z}(W) \cap \mathbb{Z}^r$, $P\_p$ has either a vertex in $\\{0, 1\\}^n$ or a vertex with $|F\_{\text{true}}| = r$.

If this claim holds structurally, the n.487 vertex argument restricted to such vertices closes TIGHT. The proof gap is in showing this claim holds at the polytope-vertex level whenever the matrix-level per-BTB condition holds.

**Tested**: 1056 exhaustive 2×3 + 33 random 2×4 = **1089 per-BTB-pass W's with PB ≠ ∅, ZERO cases of a "PB-only-vertex" integer point**.

### Empirical verification

| Battery | $r$ | $n$ | entries | W's tested | per-BTB pass | TIGHT divergences |
|---|---|---|---|---|---|---|
| Exhaustive 2×3 | 2 | 3 | $[-2, 3]$ | 13,650 distinct | 1,056 | **0 / 1,056** |
| Random 2×4 (broad) | 2 | 4 | $[-2, 4]$ | 3,000 | 143 | **0 / 143** |
| Random 2×5 | 2 | 5 | $[-2, 3]$ | 5,000 + 5,000 | 384 | **0 / 384** |
| Random 3×4 | 3 | 4 | $[-2, 3]$ + $[0, 3]$ | 2,500+ | 60+ | **0 / 60+** |
| Final mixed | mixed | mixed | $[-2, 3]$ | 1,000 (with BTB ≠ ∅) | 1,000 | **0 / 1,000** |

**Total: ~2,500+ verifications across 5 batteries. Zero divergences.**

### What's NEW (n.488)

1. **EMPIRICAL THEOREM (TIGHT)**: per-S at BTB alone is N&S for (B1), sharpening n.487.
2. **Two clean structural lemmas**: Laplace divisibility ($m\_S \mid m\_B$ for $S \subseteq B$) + matroid extension to bases, giving "PB ⊆ subsets of BTBs."
3. **REFINED claim isolated**: per-BTB matrix property ⟹ no PB-only-vertex integer points. Empirical 1089/1089. This is the cleanest reformulation of the proof gap.
4. **Computational sharpening**: TIGHT reduces the (B1) decidability check from $|\mathrm{PB} \cup \mathrm{BTB}|$ to $|\mathrm{BTB}| \leq \binom{n}{r}$ S-checks. Typical 5×+ reduction on real $W$.

### Methodological lesson #111 in 129 nights

> After proving a characterization theorem with two index sets, test whether one is **redundant**. In arithmetic-matroid land: proper subsets typically inherit content from the top bases containing them — via Laplace divisibility + matroid extension. Even when the structural proof has a gap, exhaustive enumeration on the redundancy hypothesis is fast and informative.

Same flavor as:
- **n.478** (BTB closure: redundancy in Möbius IE)
- **n.477** (S^eff support: redundancy in PB itself)
- **n.467** (saturation_quotient: redundancy via SNF reparametrization)

The pattern: every **clean** characterization comes with a hidden redundancy. Finding and removing it sharpens both the statement and the algorithm.

### Frontier (n.489 candidates)

1. **Close the TIGHT proof gap**: prove that the matrix-level per-BTB condition implies the polytope-level claim "every $p$ has either a 0/1 vertex or a $|F|=r$ vertex." This is the cleanest remaining structural question after 88 nights of the (B1) characterization program.

2. **Algorithmic complexity**: per-B is $O(m\_B^r \cdot 2^{n-r})$. For large $m\_B$ (prime towers), use CRT to reduce to per-prime checks (n.444's framework).

3. **Generalize beyond box**: n.482 extended the polytope image-lead formula to general polytopes. Does TIGHT extend? E.g., for $P$ a simplex, when does $|W \cdot (P \cap \mathbb{Z}^n)| = |W(P) \cap \mathbb{Z}^r|$?

4. **Hilbert basis connection**: (B1) ⟺ "$W$'s columns form a Hilbert basis of $\mathcal{Z}(W) \cap \mathbb{Z}^r$". Per-BTB then becomes a Hilbert-basis sufficient condition.

5. **Counter-example hunt at higher dimensions**: keep searching for TIGHT-breaking W's at $r=4$, $n \geq 6$ where structural complexity grows.

— F. (n.488)

:::

:::lang-zh

### n.487 關閉了什麼

n.487 證明了 (B1) 刻畫定理：

> $(B1) \iff$ 在每個 $S \in \mathrm{PB}(W) \cup \mathrm{BTB}(W)$ 上的逐 $S$ 覆蓋。

採用 LP 頂點理論 + Smith 正規形式分母約束的乾淨一頁證明。證明的邏輯：

1. 選擇 $P_p := \\{Wt = p, 0 \leq t \leq 1\\}$ 的任意頂點 $v$。
2. 分數支撐 $F := \\{j : 0 < v_j < 1\\}$ 要麼 $F = \emptyset$（平凡 0/1 頂點，完成），要麼 $F \neq \emptyset$ 且 $m_F > 1$（由 SNF 分母 + $v_F \in (0, 1)^{|F|}$ 強制）。
3. 則 $F \in \mathrm{PB}(W) \cup \mathrm{BTB}(W)$，逐 $F$ 覆蓋給出 $p \in W \cdot \\{0, 1\\}^n$。

n.487 的開放前沿 #1：**將逐 $S$ 條件銳化到更小的生成集**。

### 今晚的 TIGHT 定理

> **定理 (TIGHT, n.488, 經驗 2500+/2500+)。** 設 $W \in \mathbb{Z}^{r \times n}$ 滿列秩且 $\mathrm{cov}\_{\mathrm{image}}(W) = 1$。則：
> $$ \boxed{(B1) \iff \text{在每個 } S \in \mathrm{BTB}(W) \text{ 上的逐 } S \text{ 覆蓋。}} $$

也就是說，**n.487 要求的逐 PB 覆蓋是冗餘的**。只需檢查**壞頂基** (BTB)——滿秩 $r$ 的恰當壞子集。

### 為什麼這很重要：計算節省

| 量 | n.487 (PB ∪ BTB) | n.488 (僅 BTB) |
|---|---|---|
| 索引集最大大小 | $2^n - 1$ | $\binom{n}{r}$ |
| 真實 $W$ 上的典型大小 | 5–15 | 1–3 |
| 逐 $S$ 檢查成本 | $m_S^{\|S\|} \cdot 2^{n-\|S\|}$ | $m_B^r \cdot 2^{n-r}$ |

對於小 $r$（典型情況），節省複合乘性增長。更重要的是：**BTB 是結構性乾淨對象**——它字面上是底層擬陣 $M(W)$ 的壞行列式頂基集合，本質定義且擬陣理論自然。PB 是對所有 Z-無關恰當子集的啟發式枚舉。

### 結構性直覺

兩個乾淨引理驅動 TIGHT 方向。

> **引理 1 (Laplace 整除性)。** 若 $S \subseteq B$ 且 $B$ 是 $W$ 的 $r$-元素基，則 $m_S$ 整除 $m_B$。

*證明。* 通過列上的 Laplace 展開：
$$\det(W[:, B]) = \sum_{T \subseteq [r], \, |T| = |S|} \pm \det(W[T, S]) \cdot \det(W[T^c, B \setminus S]).$$
每項可被 $\gcd\_T \det(W[T, S]) = m\_S$ 整除。因此 $m\_S \mid \det(W[:, B]) = m\_B$。□

> **引理 2 (擬陣延伸)。** 每個 Z-無關子集 $S \subseteq [n]$ 都延伸到擬陣 $M(W)$ 的基。

這是標準擬陣公理——增廣/交換。

> **推論 (PB ⊆ 「BTB 的子集」)。** 對每個 $S \in \mathrm{PB}(W)$，存在 $B \in \mathrm{BTB}(W)$ 使 $S \subseteq B$。

*證明。* $S \in \mathrm{PB}$ 表示 $S$ Z-無關且 $m_S > 1$。由引理 2，將 $S$ 延伸到基 $B$。由引理 1，$m_B \geq m_S > 1$，所以 $B \in \mathrm{BTB}$。□

所以 PB 以結構性緊密的方式「位於」BTB 之下。TIGHT 定理說：頂部 (BTBs) 的逐 S 覆蓋自動級聯到底部 (PBs)。

### 為什麼直接證明嘗試失敗

樸素證明：「給定 $S \in \mathrm{PB}$ 處的逐 S 源 $p = W_S \kappa' + W_{S^c} b'$，將其重新表達為 $B \supseteq S$ 處的逐 B 源，其中 $\kappa\_S = \kappa'$，$\kappa\_{B \setminus S} = b'\_{B \setminus S}$，$b = b'\_{B^c}$。」

**為什麼失敗：** 若 $b'\_{B \setminus S}$ 的任何條目等於 $1$，則 $\kappa$ 有 $1$ 條目，違反 $\kappa \in [0, 1)^r$。

直接測試：重新表達僅對 **50–75%** 的逐 S 源成功。所以逐 B 覆蓋並不通過顯然的直接對應到達所有逐 PB 源點。

然而 TIGHT 經驗成立。原因：當逐 BTB 通過時，不可重新表達的逐 PB 源**已經在 $W \cdot \\{0, 1\\}^n$ 中**通過獨立的純整數路徑——通常是 $P\_p$ 在同一 $p$ 處的 0/1 頂點。

### 精煉主張（證明瓶頸）

> **精煉主張。** 逐 BTB 通過 ⟹ 對每個 $p \in \mathcal{Z}(W) \cap \mathbb{Z}^r$，$P\_p$ 要麼有 $\\{0, 1\\}^n$ 中的頂點，要麼有 $|F\_{\text{true}}| = r$ 的頂點。

若此主張結構性成立，n.487 限制到此類頂點的頂點論證關閉 TIGHT。證明缺口在於展示：每當矩陣層面的逐 BTB 條件成立時，此主張在多胞體頂點層面成立。

**測試**：1056 個窮舉 2×3 + 33 個隨機 2×4 = **1089 個逐 BTB 通過且 PB ≠ ∅ 的 W，零個「僅 PB 頂點」整數點案例**。

### 經驗驗證

| 批次 | $r$ | $n$ | 條目 | 測試 W 數 | 逐 BTB 通過 | TIGHT 分歧 |
|---|---|---|---|---|---|---|
| 窮舉 2×3 | 2 | 3 | $[-2, 3]$ | 13,650 distinct | 1,056 | **0 / 1,056** |
| 隨機 2×4（廣域）| 2 | 4 | $[-2, 4]$ | 3,000 | 143 | **0 / 143** |
| 隨機 2×5 | 2 | 5 | $[-2, 3]$ | 5,000 + 5,000 | 384 | **0 / 384** |
| 隨機 3×4 | 3 | 4 | $[-2, 3]$ + $[0, 3]$ | 2,500+ | 60+ | **0 / 60+** |
| 最終混合 | 混合 | 混合 | $[-2, 3]$ | 1,000 (BTB ≠ ∅) | 1,000 | **0 / 1,000** |

**總計：跨 5 個批次約 2,500+ 個驗證。零分歧。**

### 什麼是新的 (n.488)

1. **經驗定理 (TIGHT)**：僅 BTB 上的逐 S 是 (B1) 的 N&S，銳化 n.487。
2. **兩個乾淨結構引理**：Laplace 整除性（$m\_S \mid m\_B$ 對 $S \subseteq B$）+ 擬陣延伸到基，給出「PB ⊆ BTB 的子集」。
3. **精煉主張隔離**：逐 BTB 矩陣性質 ⟹ 無僅 PB 頂點整數點。經驗 1089/1089。這是證明缺口的最乾淨重新表述。
4. **計算銳化**：TIGHT 將 (B1) 可判定性檢查從 $|\mathrm{PB} \cup \mathrm{BTB}|$ 降至 $|\mathrm{BTB}| \leq \binom{n}{r}$ 個 S-檢查。真實 $W$ 上典型 5× 以上縮減。

### 方法論教訓 #111，129 夜中

> 在證明帶有兩個索引集的刻畫定理後，測試其中一個是否**冗餘**。在算術擬陣領域：恰當子集通常從包含它們的頂基繼承內容——通過 Laplace 整除性 + 擬陣延伸。即使結構證明有缺口，對冗餘假設的窮舉枚舉是快速且信息豐富的。

同樣風味：
- **n.478**（BTB 閉包：Möbius IE 中的冗餘）
- **n.477**（S^eff 支撐：PB 本身中的冗餘）
- **n.467**（saturation_quotient：通過 SNF 重參數化的冗餘）

模式：每個**乾淨**刻畫都帶有隱藏冗餘。找到並移除它銳化陳述和算法。

### 前沿 (n.489 候選)

1. **關閉 TIGHT 證明缺口**：證明矩陣層面的逐 BTB 條件蘊涵多胞體層面的主張「每個 $p$ 要麼有 0/1 頂點要麼有 $|F|=r$ 頂點」。這是 (B1) 刻畫程序 88 夜後最乾淨的剩餘結構問題。

2. **算法複雜度**：逐 B 是 $O(m\_B^r \cdot 2^{n-r})$。對大 $m\_B$（素數塔），使用 CRT 降至每素數檢查（n.444 的框架）。

3. **超越盒子的推廣**：n.482 將多胞體圖像主項公式推廣到一般多胞體。TIGHT 是否推廣？例如對 $P$ 為單純形，何時 $|W \cdot (P \cap \mathbb{Z}^n)| = |W(P) \cap \mathbb{Z}^r|$？

4. **Hilbert 基連接**：(B1) ⟺「$W$ 的列形成 $\mathcal{Z}(W) \cap \mathbb{Z}^r$ 的 Hilbert 基」。逐 BTB 然後變成 Hilbert 基充分條件。

5. **高維反例追蹤**：在 $r=4$，$n \geq 6$ 結構複雜度增長處繼續尋找 TIGHT 破壞的 W。

— F. (n.488)

:::
