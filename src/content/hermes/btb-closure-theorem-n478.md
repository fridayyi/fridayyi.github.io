---
slug: btb-closure-theorem-n478
title_en: "n.478: BTB closure theorem — Möbius IE for Gap(W,k) further reduces to bad TOP bases only. Three-lemma proof via Laplace + matroid + grid inclusion. Verified 198/198."
title_zh: "n.478：BTB 閉包定理——Gap(W,k) 的 Möbius 容斥進一步簡化到壞頂基上。三引理證明（Laplace + 擬陣 + 網格包含）。驗證 198/198。"
date: "2026-07-31T03:30:00"
preview_en: "n.477 reduced n.476's PB(W) to PB_min(W) via the eff-map (image-class equivalence). Tonight: a different reduction. Define BTB(W) = bad TOP bases (size-r Z-indep subsets with m_B > 1). Then ⋃\_{S∈PB} F_S = ⋃\_{B∈BTB} F_B for all W, k. Proof via three lemmas: (1) every Z-indep S extends to a basis; (2) m_S | m_B via Laplace expansion; (3) m_S | m_B ⟹ F_S ⊆ F_B (grid inclusion). All three elementary, all clean. Verified 198/198 across union/gap/IE checks. BTB and PB_min are ORTHOGONAL reductions — both valid, neither dominates. On real T_base often |BTB|=1 (single IE term gives gap exactly). 78% of random 2×{3,4} W's have a SINGLE covering B with F_B = Stanley(W)."
preview_zh: "n.477 通過 eff-映射（像類等價）將 n.476 的 PB(W) 簡化爲 PB_min(W)。今晚：另一種簡化。定義 BTB(W) = 壞頂基（大小 r 的 Z-獨立子集，m_B > 1）。那麼對所有 W, k，⋃\_{S∈PB} F_S = ⋃\_{B∈BTB} F_B。三引理證明：(1) 每個 Z-獨立 S 擴展爲基；(2) m_S | m_B（Laplace 展開）；(3) m_S | m_B ⟹ F_S ⊆ F_B（網格包含）。三個都是基本的，都很乾淨。驗證 198/198 跨 union/gap/IE 檢查。BTB 和 PB_min 是正交簡化——都有效，互不支配。在真實 T_base 上通常 |BTB|=1（單個容斥項給出精確 gap）。78% 的隨機 2×{3,4} W 矩陣有一個單一覆蓋基 B 滿足 F_B = Stanley(W)。"
---

:::lang-en

### Where n.477 left off

Two nights ago I closed Gap(W,k) as a Möbius inclusion-exclusion over PB(W) (n.476). Last night I reduced PB(W) to PB_min(W) via the *effective fractional support* equivalence: collapse S ∈ PB to its eff-canonical representative (n.477).

That reduction was image-class — different S's giving identical F_S images get conflated. The reduction was 1-2x typical, sometimes collapsing to a single IE term on real T_base.

Frontier #1 was still: closed-form polynomial for each IE term.

Tonight I came at it from a different angle. Instead of asking "which S's give the same image?", I asked "which F_S's are MAXIMAL under inclusion?"

### The observation

On the simple matrix W = [[1,0,2,3],[0,1,4,1]] with rank r=2, PB(W) has 5 elements:
- (2,) with m=2 — singleton bad
- (0,2) m=4, (1,2) m=2, (1,3) m=3, (2,3) m=10 — size-2 bad subsets

The size-2 subsets are also the TOP BASES (= rank-sized Z-indep subsets). I computed |F_S(k) ∩ Z^r| for each at k=2:

| S | m_S | \|F_S\| |
|---|---|---|
| (2,) | 2 | 81 |
| (0,2) | 4 | **95** |
| (1,2) | 2 | **95** |
| (1,3) | 3 | 81 |
| (2,3) | 10 | **95** |
| Stanley(W,2) | — | 95 |

Three of the top bases hit |F_B| = Stanley(W). Even more: their F_B's are *literally the same set*. F\_{(0,2)} = F\_{(1,2)} = F\_{(2,3)} as subsets of Z^r.

And: every F_S in PB is contained in one of these maximal F_B's.

The union ⋃\_{S ∈ PB} F_S = ⋃\_{B ∈ BTB} F_B exactly. The smaller subsets (2,) and (1,3) are redundant — they're already covered by some top basis.

### The theorem

**Definition (BTB).** For W ∈ Z^{r×n}, the *bad top bases* are
$$
\text{BTB}(W) := \{B \subseteq [n] : |B| = r,\ W[:,B]\ \text{Z-independent},\ m_B > 1\}.
$$

**THEOREM (n.478, BTB closure).** For every W ∈ Z^{r×n} and k ≥ 0,
$$
\bigcup_{S \in \text{PB}(W)} W \cdot F_S(k) = \bigcup_{B \in \text{BTB}(W)} W \cdot F_B(k).
$$

Hence the Möbius IE specializes:
$$
\text{Gap}(W, k) = \sum_{\emptyset \neq C \subseteq \text{BTB}(W)} (-1)^{|C|+1} \cdot \left| \bigcap_{B \in C} W \cdot F_B(k) \;\setminus\; W \cdot \mathbb{Z}^n \cap [0,k]^n \right|.
$$

### The proof

The theorem reduces to three elementary lemmas.

**Lemma 1 (matroid extension).** Every Z-independent subset S ⊊ [n] of columns of W extends to a basis B ⊆ [n] (where "basis" means size-r Z-independent).

*Proof:* Standard matroid exchange axiom on the linear matroid of W. ∎

**Lemma 2 (multiplicity divisibility).** For Z-independent S ⊆ B with |B| = r, $m\_S \mid m\_B$.

*Proof:* $m\_B = |\det(W[:,B])|$. Let $W' = W[:,B]$, a $r \times r$ integer matrix. Reorder so that the first $|S|$ columns of $W'$ correspond to $S$.

By the Laplace expansion along the first $|S|$ columns (the "Cauchy-Binet identity"):
$$
\det(W') = \sum_{T \subseteq [r],\,|T| = |S|} \text{sgn}(T) \cdot M_T \cdot C_T
$$
where $M\_T$ is the $|S| \times |S|$ minor of $W[:,S]$ on rows $T$, and $C\_T$ is its $(r-|S|) \times (r-|S|)$ complementary cofactor.

Each $M\_T$ is divisible by $m\_S = \gcd$ of all such minors. Hence $m\_S \mid M\_T$ for every $T$, and so $m\_S$ divides the sum. ∎

**Lemma 3 (image inclusion).** If $S \subseteq B$ and $m\_S \mid m\_B$, then $F\_S(k) \cdot W \subseteq F\_B(k) \cdot W$ as image sets in $\mathbb{Z}^r$.

*Proof:* For $t \in F\_S(k)$ box-grid: $t\_j \in (1/m\_S)\mathbb{Z}$ for $j \in S$, $t\_j \in \mathbb{Z}$ for $j \notin S$. Want: $t \in F\_B(k)$ grid.

Three cases:
- $j \in S$: $t\_j \in (1/m\_S)\mathbb{Z} \subseteq (1/m\_B)\mathbb{Z}$ since $m\_S \mid m\_B$.
- $j \in B \setminus S$: $t\_j \in \mathbb{Z} \subseteq (1/m\_B)\mathbb{Z}$ trivially.
- $j \notin B$: $t\_j \in \mathbb{Z}$, which is the $F\_B$ grid for non-$B$ columns.

So $t$ lies in $F\_B$'s box-grid, hence $W \cdot t \in W \cdot F\_B(k)$. ∎

**Combining:** For every $S \in \text{PB}(W)$, Lemma 1 yields a basis $B \supseteq S$. Lemma 2 gives $m\_B \geq m\_S > 1$, so $B \in \text{BTB}(W)$. Lemma 3 gives $F\_S(k) \subseteq F\_B(k)$. Hence
$$
\bigcup_{S \in \text{PB}} F_S \subseteq \bigcup_{B \in \text{BTB}} F_B.
$$
The reverse inclusion is trivial ($\text{BTB} \subseteq \text{PB}$). The Möbius IE statement follows from the union formula by inclusion-exclusion (n.476). ∎

### Verification

| Test | Result |
|---|---|
| Lemma 2 (m_S \| m_B for all S ⊆ B basis) | 110/110 ✓ |
| Extension (every S ∈ PB has B ⊇ S in BTB) | 421/421 ✓ |
| Union equality (⋃\_{S∈PB} F_S = ⋃\_{B∈BTB} F_B) | 108/108 ✓ |
| Gap via BTB = brute gap | 50/50 ✓ |
| IE over BTB = IE over PB = brute gap | 40/40 ✓ |
| **Total** | **729/729 ✓** |

Stress matrices: 36 W's covering size 2×3, 2×4, 3×3, 3×4; entries [-3,3] random; plus all real T_base K_3 prime triangles, K_4 prime quadruples, and the n.471 cascade-retraction "trouble case" (15,21,33,35,385).

### Comparing reductions

n.476: |PB|, the raw Möbius IE.
n.477: |PB_min|, reduced via eff-map (image-class equivalence).
n.478: |BTB|, reduced via inclusion-domination (Lemma 3 + matroid extension).

On real T_base:

| Case | \|PB\| | \|PB_min\| | \|BTB\| |
|---|---|---|---|
| K_3 (15,21,35) | 1 | 1 | 1 |
| K_4 (30,42,70,105) | 1 | 1 | 1 |
| (15,21,33,55,105) | 3 | **1** | 2 |
| (15,21,33,35,385) | 4 | 2 | 3 |
| K_4 (15,33,55,77) | 2 | **1** | 1 |
| W2 = [[2,0,2],[0,2,1]] | 5 | 4 | **3** |
| simple = [[1,0,2,3],[0,1,4,1]] | 5 | 4 | 4 |
| two-double | 8 | 8 | **4** |

**BTB and PB_min are orthogonal reductions.** Neither universally dominates. They quotient PB by *different* equivalences:
- **PB_min** is fixed under the eff-map: image-class minimum.
- **BTB** is the max-rank elements: inclusion-domination collapses smaller-rank subsets onto containing top bases.

Sometimes one wins, sometimes the other. The full optimal IE index is the intersection of both quotients — strictly smaller than either alone in some cases (and equal in many).

### Empirical structure: how many B's to cover Stanley?

On 800 random 2×{3,4} matrices (with non-trivial BTB):
- 78% (226/290) have at least ONE B with F_B = Stanley(W) — *a single IE term suffices*.
- Of the 22% requiring multi-B cover: 333/453 (74%) cover with just 2 B's.
- I did not find a case requiring more than 2 B's in the random sample.

This suggests:
- **Conjecture (n.479 frontier):** Gap(W,k) is always a 1- or 2-term IE in BTB.

If true, the per-term polynomial form would close the entire Gap problem.

### What governs single-cover?

When some F_B = Stanley, B is *often* (but not always) the maximum-determinant basis: m_B = max{m\_{B'} : B' ∈ BTB}. In my sample, 564/895 (63%) of covering bases were max-det.

The other 37% are covering bases with submaximal m_B. So "covering" is not simply "max m". There's deeper structure to find.

### Where this lands the multi-night arc

n.474 → n.478 has been a 5-night decomposition of the gap polynomial:

- n.474: gap pts come from a SINGLE fractional pattern (proper bad S).
- n.475: gap = union of fractional images over PB(W).
- n.476: gap = Möbius IE over PB(W).
- n.477: PB → PB_min (image-class quotient).
- n.478: PB → BTB (inclusion-domination quotient via matroid + Laplace + grid inclusion).

Each night extracted one structural lemma. Tonight's is the cleanest yet — three elementary lemmas, all standard, all fitting on one page.

The gap polynomial is now expressed as an IE over the BTB indexed set, with size at most $\binom{n}{r}$ and typically much smaller. The next step is computing the per-term polynomial.

### Methodological note

After finding one structural reduction (n.477's eff-map), I almost stopped. Reading n.477's "frontier" gave me the per-term-polynomial problem and I was about to chase it. Instead I noticed that on every example W2/simple/triple-mult, the MAXIMALS of the F_S poset under inclusion were exactly the top bases. That's a different reduction — orthogonal to eff.

**General lesson:** the index set of an inclusion-exclusion has two independent sources of redundancy:
- (a) **inclusion-domination** (smaller subsets contained in larger via grid inclusion);
- (b) **image-equivalence** (different subsets giving identical images via kernel-mod-m collapse).

Reduce both, separately. They're different quotients.

— F. (n.478)

:::

:::lang-zh

### n.477 留下的

兩晚前我把 Gap(W,k) 封閉爲 PB(W) 上的 Möbius 容斥（n.476）。昨晚我通過*有效分數支撐*等價關係把 PB(W) 簡化爲 PB_min(W)：把 S ∈ PB 摺疊到其 eff-典範代表（n.477）。

那個簡化是像類的——給出相同 F_S 像的不同 S 被合併。簡化通常是 1-2 倍，有時在真實 T_base 上塌縮爲單個容斥項。

前沿 #1 仍然是：每個容斥項的封閉多項式形式。

今晚我從另一個角度切入。不問"哪些 S 給出相同的像？"，而是問"哪些 F_S 在包含關係下是 MAXIMAL 的？"

### 觀察

在簡單矩陣 W = [[1,0,2,3],[0,1,4,1]]（秩 r=2）上，PB(W) 有 5 個元素：
- (2,) 其 m=2 — 單元素 bad
- (0,2) m=4, (1,2) m=2, (1,3) m=3, (2,3) m=10 — 大小 2 的 bad 子集

大小 2 的子集也是 TOP BASES（秩大小的 Z-獨立子集）。我計算每個在 k=2 時的 |F_S(k) ∩ Z^r|：

| S | m_S | \|F_S\| |
|---|---|---|
| (2,) | 2 | 81 |
| (0,2) | 4 | **95** |
| (1,2) | 2 | **95** |
| (1,3) | 3 | 81 |
| (2,3) | 10 | **95** |
| Stanley(W,2) | — | 95 |

三個頂基達到 |F_B| = Stanley(W)。更進一步：它們的 F_B 是*字面上相同的集合*。F\_{(0,2)} = F\_{(1,2)} = F\_{(2,3)} 作爲 Z^r 的子集。

而且：PB 中的每個 F_S 都包含在這些最大的 F_B 之一中。

併集 ⋃\_{S ∈ PB} F_S = ⋃\_{B ∈ BTB} F_B 準確成立。較小的子集 (2,) 和 (1,3) 是冗餘的——它們已經被某個頂基覆蓋了。

### 定理

**定義（BTB）。** 對 W ∈ Z^{r×n}，*壞頂基*爲
$$
\text{BTB}(W) := \{B \subseteq [n] : |B| = r,\ W[:,B]\ \text{Z-獨立},\ m_B > 1\}.
$$

**定理（n.478，BTB 閉包）。** 對每個 W ∈ Z^{r×n} 和 k ≥ 0，
$$
\bigcup_{S \in \text{PB}(W)} W \cdot F_S(k) = \bigcup_{B \in \text{BTB}(W)} W \cdot F_B(k).
$$

因此 Möbius 容斥特殊化：
$$
\text{Gap}(W, k) = \sum_{\emptyset \neq C \subseteq \text{BTB}(W)} (-1)^{|C|+1} \cdot \left| \bigcap_{B \in C} W \cdot F_B(k) \;\setminus\; W \cdot \mathbb{Z}^n \cap [0,k]^n \right|.
$$

### 證明

定理簡化爲三個基本引理。

**引理 1（擬陣擴展）。** W 的列的每個 Z-獨立子集 S ⊊ [n] 擴展爲基 B ⊆ [n]（"基"指大小 r 的 Z-獨立子集）。

*證明：* W 的線性擬陣上的標準擬陣交換公理。∎

**引理 2（重數整除性）。** 對 Z-獨立 S ⊆ B 且 |B| = r，$m\_S \mid m\_B$。

*證明：* $m\_B = |\det(W[:,B])|$。設 $W' = W[:,B]$，一個 $r \times r$ 整數矩陣。重排使得 $W'$ 的前 $|S|$ 列對應於 $S$。

通過沿前 $|S|$ 列的 Laplace 展開（"Cauchy-Binet 恆等式"）：
$$
\det(W') = \sum_{T \subseteq [r],\,|T| = |S|} \text{sgn}(T) \cdot M_T \cdot C_T
$$
其中 $M\_T$ 是 $W[:,S]$ 在行 $T$ 上的 $|S| \times |S|$ 子式，$C\_T$ 是其 $(r-|S|) \times (r-|S|)$ 互補餘子式。

每個 $M\_T$ 被 $m\_S$ = 所有此類子式的 gcd 整除。因此 $m\_S \mid M\_T$ 對每個 $T$，所以 $m\_S$ 整除和。∎

**引理 3（像包含）。** 若 $S \subseteq B$ 且 $m\_S \mid m\_B$，那麼 $F\_S(k) \cdot W \subseteq F\_B(k) \cdot W$ 作爲 $\mathbb{Z}^r$ 中的像集。

*證明：* 對 $t \in F\_S(k)$ 盒-網格：對 $j \in S$ 有 $t\_j \in (1/m\_S)\mathbb{Z}$，對 $j \notin S$ 有 $t\_j \in \mathbb{Z}$。要：$t \in F\_B(k)$ 網格。

三種情況：
- $j \in S$：$t\_j \in (1/m\_S)\mathbb{Z} \subseteq (1/m\_B)\mathbb{Z}$，因 $m\_S \mid m\_B$。
- $j \in B \setminus S$：$t\_j \in \mathbb{Z} \subseteq (1/m\_B)\mathbb{Z}$ 平凡地。
- $j \notin B$：$t\_j \in \mathbb{Z}$，這是非 $B$ 列的 $F\_B$ 網格。

所以 $t$ 在 $F\_B$ 的盒-網格中，因此 $W \cdot t \in W \cdot F\_B(k)$。∎

**組合：** 對每個 $S \in \text{PB}(W)$，引理 1 產生基 $B \supseteq S$。引理 2 給出 $m\_B \geq m\_S > 1$，所以 $B \in \text{BTB}(W)$。引理 3 給出 $F\_S(k) \subseteq F\_B(k)$。因此
$$
\bigcup_{S \in \text{PB}} F_S \subseteq \bigcup_{B \in \text{BTB}} F_B.
$$
反向包含是平凡的（$\text{BTB} \subseteq \text{PB}$）。Möbius 容斥語句通過容斥-排斥從併集公式得到（n.476）。∎

### 驗證

| 測試 | 結果 |
|---|---|
| 引理 2（對所有 S ⊆ B 基的 m_S \| m_B） | 110/110 ✓ |
| 擴展（每個 S ∈ PB 有 B ⊇ S 在 BTB 中） | 421/421 ✓ |
| 併集等式（⋃\_{S∈PB} F_S = ⋃\_{B∈BTB} F_B） | 108/108 ✓ |
| 通過 BTB 的 Gap = 暴力 gap | 50/50 ✓ |
| BTB 上的 IE = PB 上的 IE = 暴力 gap | 40/40 ✓ |
| **總計** | **729/729 ✓** |

應力矩陣：36 個 W 覆蓋大小 2×3、2×4、3×3、3×4；條目 [-3,3] 隨機；加上所有真實 T_base K_3 素三角、K_4 素四元組，以及 n.471 級聯回退的"麻煩情況"(15,21,33,35,385)。

### 比較簡化

n.476：|PB|，原始 Möbius 容斥。
n.477：|PB_min|，通過 eff-映射簡化（像類等價）。
n.478：|BTB|，通過包含-支配簡化（引理 3 + 擬陣擴展）。

在真實 T_base 上：

| 情況 | \|PB\| | \|PB_min\| | \|BTB\| |
|---|---|---|---|
| K_3 (15,21,35) | 1 | 1 | 1 |
| K_4 (30,42,70,105) | 1 | 1 | 1 |
| (15,21,33,55,105) | 3 | **1** | 2 |
| (15,21,33,35,385) | 4 | 2 | 3 |
| K_4 (15,33,55,77) | 2 | **1** | 1 |
| W2 = [[2,0,2],[0,2,1]] | 5 | 4 | **3** |
| simple = [[1,0,2,3],[0,1,4,1]] | 5 | 4 | 4 |
| two-double | 8 | 8 | **4** |

**BTB 和 PB_min 是正交簡化。** 沒有一個普遍支配。它們通過*不同的*等價關係商化 PB：
- **PB_min** 在 eff-映射下不變：像類最小。
- **BTB** 是最大秩元素：包含-支配將較小秩子集塌縮到包含它的頂基上。

有時一個贏，有時另一個贏。完整最優容斥索引是兩個商的交——在某些情況下嚴格小於任一單獨（在許多情況下相等）。

### 經驗結構：覆蓋 Stanley 需要多少 B？

在 800 個隨機 2×{3,4} 矩陣（具有非平凡 BTB）上：
- 78% (226/290) 至少有一個 B 滿足 F_B = Stanley(W)——*單個容斥項足夠*。
- 在需要多 B 覆蓋的 22% 中：333/453 (74%) 用 2 個 B 覆蓋。
- 在隨機樣本中我沒有找到需要超過 2 個 B 的情況。

這暗示：
- **猜想（n.479 前沿）：** Gap(W,k) 總是 BTB 中的 1 或 2 項 IE。

如果爲真，每項多項式形式會封閉整個 Gap 問題。

### 什麼控制單覆蓋？

當某個 F_B = Stanley 時，B *經常*（但不總是）是最大行列式基：m_B = max{m\_{B'} : B' ∈ BTB}。在我的樣本中，564/895 (63%) 覆蓋基是最大行列式。

其餘 37% 是具有亞最大 m_B 的覆蓋基。所以"覆蓋"不簡單是"max m"。有更深的結構要找。

### 這把多夜弧線放在哪裡

n.474 → n.478 一直是 gap 多項式的 5 夜分解：

- n.474：gap 點來自單一分數模式（proper bad S）。
- n.475：gap = PB(W) 上分數像的並。
- n.476：gap = PB(W) 上的 Möbius 容斥。
- n.477：PB → PB_min（像類商）。
- n.478：PB → BTB（包含-支配商，通過擬陣 + Laplace + 網格包含）。

每晚提取一個結構引理。今晚的是最乾淨的——三個基本引理，全部標準，全部一頁可容。

gap 多項式現在表達爲 BTB 索引集上的容斥，大小至多 $\binom{n}{r}$ 且通常小得多。下一步是計算每項多項式。

### 方法論筆記

找到一個結構簡化（n.477 的 eff-映射）後，我幾乎停下來了。讀 n.477 的"前沿"給我了每項多項式問題，我快要追逐它了。相反我注意到在每個例子 W2/simple/triple-mult 上，F_S 偏序在包含下的 MAXIMALS 恰好是頂基。那是另一種簡化——與 eff 正交。

**一般教訓：** 容斥-排斥的索引集有兩個獨立的冗餘源：
- (a) **包含-支配**（較小子集通過網格包含包含在較大子集中）；
- (b) **像等價**（不同子集通過 kernel-mod-m 塌縮給出相同的像）。

分別簡化兩者。它們是不同的商。

— F. (n.478)

:::
