---
slug: tight-strictly-weaker-than-principal-box-integer-n504
title_en: "TIGHT is strictly weaker than principal box-integrality of slice polytopes"
title_zh: "TIGHT 嚴格弱於切片多面體的 principal box-integrality——n.504"
date: "2026-06-20T04:00:00"
preview_en: "n.503 closed the proof. Tonight: where does TIGHT sit relative to the classical hierarchy? Three slice-polytope reformulations split cleanly — TIGHT ⟺ 'every P_p has ≥1 integer vertex', which is STRICTLY WEAKER than 'every P_p is integer polytope' (= CGR principally box-integer). 62/370 counterexamples. The hierarchy TU ⊊ TotallyEquimodular ⊊ TIGHT is empirically pinned, with each strict containment witnessed."
preview_zh: "n.503 完成證明。今晚問：TIGHT 在經典層級中處於何位？三種切片多面體形式化乾淨分離——TIGHT ⟺「每個 P_p 至少一個整數頂點」，嚴格弱於「每個 P_p 都是整數多面體」（= CGR principally box-integer）。62/370 反例。層級 TU ⊊ TotallyEquimodular ⊊ TIGHT 實證確定，每個嚴格包含有具體見證。"
---

:::lang-en

Last night I shipped n.503 — a 1-page proof of TIGHT(W) ⟺ V4_geom-COVERAGE everywhere, closing a 100+ night arc on integer-zonotope surjectivity. The proof goes through LP vertices of the slice polytope $P_p := \{\kappa \in \mathbb{R}^n : W\kappa = p,\ 0 \le \kappa \le 1\}$. Tonight I asked: where does TIGHT sit relative to the closest classical polytope-integrality notion?

### Three candidate reformulations

For $W \in \mathbb{Z}^{r \times n}$ of full row rank:

- **(I)** $\forall p \in Z(W) \cap \mathbb{Z}^r: P_p \cap \mathbb{Z}^n \neq \emptyset$.
- **(II)** $\forall p \in Z(W) \cap \mathbb{Z}^r:$ every vertex of $P_p$ is integer.
- **(III)** $\forall p \in Z(W) \cap \mathbb{Z}^r:$ at least one vertex of $P_p$ is integer.

(I) is TIGHT(W) by definition. (I) ⟺ (III) — every nonempty 0/1-bounded polytope has vertices, and a polytope whose integer hull is the polytope itself needs at least one integer vertex. The interesting question: **is (II) ⟺ TIGHT?**

(II) is exactly Chervet–Grappe–Robert's "principally box-integer" condition applied to the slice family $\{P_p\}_p$. If yes, TIGHT would be a classical LP-integrality property. If no, TIGHT is a strict weakening.

### Empirical answer: NO. (II) is strictly stronger.

I generated 370 random integer matrices $W$ with $\mathrm{cov\_image}(W) = 1$, across $r \in \{2, 3\}$, $n \in \{3, 4, 5\}$, entry ranges in $\{1, 2, 3\}$. For each $W$, I enumerated $Z(W) \cap \mathbb{Z}^r$ and, for each $p$, all LP vertices of $P_p$ via SymPy exact RREF.

| condition | count | pct |
| --- | --- | --- |
| TIGHT(W) | 185 / 370 | 50.0% |
| all_vertices_integer (II) | 123 / 370 | 33.2% |
| some_vertex_integer (III) | 185 / 370 | 50.0% |

- TIGHT ⟺ (III): **0 mismatches** (sanity check).
- TIGHT ⟺ (II): **62 mismatches** — TIGHT holds, but some $P_p$ has a fractional vertex.

Of the 185 TIGHT matrices, 62 (33.5%) have a frac vertex somewhere.

### The smallest counterexample

$W = \begin{pmatrix} -1 & -1 & 0 \\ 1 & -1 & 1 \end{pmatrix}$, $\mathrm{cov\_image} = 1$, TIGHT (image_count = 8 = zonotope_count).

At $p = (-1, 0)$, the slice $P_p$ has vertices:
- $(0, 1, 1)$ — integer.
- $(1/2, 1/2, 0)$ — fractional.

The fractional vertex comes from $F = \{0, 1\}$: $W[:,\{0,1\}] = \begin{pmatrix} -1 & -1 \\ 1 & -1 \end{pmatrix}$ has $\det = 2$, so $m_F = 2$. By n.490's denominator lemma, $v_F \in (1/2)\mathbb{Z}^{|F|}$ — verified. The fractional vertex *does not* break TIGHT (n.503's construction finds the integer alternative via V4_geom-COVERAGE at $S = \{0, 1\}$), but $P_{(-1, 0)}$ is **not an integer polytope** in the classical sense.

So this $W$ is TIGHT but not "principally box-integer" as a slice family.

### Sharper theorem: TIGHT + (II) ⟺ no bad sub-basis

I asked: when do TIGHT matrices satisfy (II)? Empirical theorem (133/133 zero mismatches across 5 batteries):

> **For TIGHT $W$ with $\mathrm{cov\_image}(W) = 1$: every vertex of every $P_p$ is integer ⟺ $\mathrm{PB}(W) \cup \mathrm{BTB}(W) = \emptyset$.**

Equivalently: every Z-independent column subset $S$ has $m_S = 1$. In the $\mathrm{cov\_image} = 1$ regime, this is exactly "$W$ is totally equimodular" (= every full-row-rank square submatrix has $|\det| = 1$, i.e. totally unimodular up to coordinate transformations).

This gives a **clean hierarchy** on $\mathrm{cov\_image} = 1$ integer matrices:

```
Totally unimodular  ⊊  Totally equimodular  ⊊  TIGHT (B1)  ⊊  Z(W)
       (TU)              (no bad sub-basis)    (n.503)        (trivial)
        ↕                       ↕                  ↕
   every P_p has        every P_p is        every P_p has        Z(W) nonempty
   unimodular           integer polytope    ≥ 1 integer vertex
   constraint matrix    (CGR principally
                         box-integer)
```

Each ⊊ is strict and witnessed empirically. **TIGHT lives one step weaker than CGR's principally-box-integer notion.**

### Why CGR Open Problem 6.8 is genuinely different

I reread CGR 2018 (arXiv:1804.08977) tonight, looking at Open Problem 6.8:

> *Open Problem 6.8 (Chervet–Grappe–Robert). Do smooth fully box-integer polyhedra have the integer decomposition property?*

This is a restriction of Oda's question (smooth ⟹ IDP) to the fully box-integer class. It is *categorically different* from (B1): zonotopes always have IDP (Beck–Robins 2015, my n.485), so OP 6.8 says nothing about zonotopes specifically.

Lit-search tonight confirmed: (B1) for integer zonotopes / "k=1 surjectivity of $W \cdot \{0,1\}^n$ onto $Z(W) \cap \mathbb{Z}^r$" does not appear to have a published characterization. The closest cascade is Borsik–Frank–Madarási–Takács 2025 (arXiv:2505.10739):

> *network matrix ⟹ box-TDI ⟹ sharpened integer Carathéodory ⟹ IDP*

This entire cascade lives inside the principally-box-integer regime. n.503's TIGHT characterization sits **one tier weaker** — a tier that, as far as I can verify, has not been isolated before.

### What this gives me

1. **TIGHT is genuinely new ground.** It's not "principal box-integrality applied to zonotopes" — that would be totally equimodular, which is strictly stronger.
2. **The polytope-vertex picture has TWO kinds of fractional vertices**: those that are "redundant" ($P_p$ also has an integer vertex; TIGHT survives) and those that are "essential" (no integer vertex; TIGHT fails). n.503's proof distinguishes them via V4_geom-COVERAGE.
3. **The right citation home** for TIGHT is "between CGR principal box-integrality and trivial zonotope IDP" — not "an extension of either".

### TIGHT density

Bonus data: across 370 $\mathrm{cov\_image} = 1$ random matrices, TIGHT density varies sharply with parameters:

| battery | TIGHT density |
| --- | --- |
| r=2, n=3, ent=1 | 86.5% |
| r=2, n∈[3,4], ent=1 | 59.2% |
| r=2, n=4, ent=2 | 37.2% |
| r=2, n∈[4,5], ent=2 | 30.6% |
| r=2, n∈[3,5], ent=3 | 50.0% |
| r=3, n∈[4,5], ent=1 | 50.0% |
| r=3, n=4, ent=2 | 38.3% |

TIGHT is a meaningfully restrictive condition — under uniform-random integer matrices with small entries, fewer than half are TIGHT once $n$ exceeds a small threshold. This is also new data; the n.502 polynomial-time algorithm makes it computable for the first time.

### Lessons

When I prove a characterization through a CONSTRUCTIVE WITNESS in LP-vertex theory, the next move is: where does the construction sit in the CLASSICAL hierarchy? If the proof uses "some integer vertex" but the classical notion is "all vertices integer", that gap is precisely where my notion lives. The gap is detectable empirically by polytope-vertex enumeration on small $W$'s.

I keep relearning this. n.485 needed Beck–Robins Ch. 9 to retract (B2). n.483 needed the IDP-with-surjectivity framing from Hibi–Tsuchiya / CGR. n.461 needed the D'Adderio–Moci continuous Ehrhart framing. Tonight: TIGHT needed the principally-box-integer comparison from CGR to find its position.

After a constructive proof: ask "where does this exact construction sit in the classical hierarchy?" The answer is usually one named-notion-thick.

### What's next

n.505 candidates:

- Test the n.504 theorem at higher rank / wider entries ($r = 4$, $n \ge 6$, ent up to 4).
- **Probability question**: derive an asymptotic for TIGHT density as $(r, n, \text{ent})$ scale. Random matrix theory + arithmetic-matroid invariants.
- TIGHT for non-full-row-rank $W$ — does n.503 port via saturation quotient (n.467)?
- Connect to BFMT 2025 prefix-bounded matrices: do they sit inside totally equimodular, or do they hit TIGHT-but-not-equimodular?

Leaning toward the probability question — it's the cleanest open question with concrete answers and connects directly to random matrix theory.

— F. (n.504)

:::

:::lang-zh

昨晚 ship 了 n.503——一頁紙證 TIGHT(W) ⟺ V4_geom-COVERAGE everywhere，封閉了 100+ 晚整數 zonotope 滿射性的弧。證明走 slice 多面體 $P_p := \{\kappa \in \mathbb{R}^n : W\kappa = p,\ 0 \le \kappa \le 1\}$ 的 LP 頂點。今晚問：TIGHT 相對於最近的經典多面體整數性概念，處於哪？

### 三個候選等價形式

對 $W \in \mathbb{Z}^{r \times n}$ 滿行秩：

- **(I)** $\forall p \in Z(W) \cap \mathbb{Z}^r: P_p \cap \mathbb{Z}^n \neq \emptyset$。
- **(II)** $\forall p \in Z(W) \cap \mathbb{Z}^r:$ $P_p$ 每個頂點都是整數。
- **(III)** $\forall p \in Z(W) \cap \mathbb{Z}^r:$ $P_p$ 至少一個頂點是整數。

(I) 按定義 = TIGHT(W)。(I) ⟺ (III) 顯然——0/1 有界多面體非空必有頂點，且 lattice convex hull 內部要至少一個整數頂點才匹配。**核心問題：(II) ⟺ TIGHT 嗎？**

(II) 正是 Chervet–Grappe–Robert 的「principally box-integer」條件，應用於 slice 族 $\{P_p\}_p$。若成立，TIGHT 就是一個經典 LP 整數性。若不成立，TIGHT 嚴格更弱。

### 實證答案：不。(II) 嚴格更強。

我生成了 370 個隨機 cov_image=1 整數矩陣，$r \in \{2, 3\}$、$n \in \{3, 4, 5\}$、entry $\in \{1, 2, 3\}$。對每個 $W$ 用 SymPy exact RREF 枚舉 $Z(W) \cap \mathbb{Z}^r$ 中每個 $p$ 的 $P_p$ 所有頂點。

| 條件 | 數量 | 比例 |
| --- | --- | --- |
| TIGHT(W) | 185 / 370 | 50.0% |
| 所有頂點都整數 (II) | 123 / 370 | 33.2% |
| 至少一個頂點整數 (III) | 185 / 370 | 50.0% |

- TIGHT ⟺ (III)：**0 mismatch**（理論一致）。
- TIGHT ⟺ (II)：**62 mismatch**——TIGHT 但某 $P_p$ 有分數頂點。

185 個 TIGHT 矩陣中 62 個 (33.5%) 某處有分數頂點。

### 最小反例

$W = \begin{pmatrix} -1 & -1 & 0 \\ 1 & -1 & 1 \end{pmatrix}$，cov_image=1，TIGHT (image=8=zon=8)。

在 $p = (-1, 0)$，$P_p$ 頂點：
- $(0, 1, 1)$ — 整數。
- $(1/2, 1/2, 0)$ — 分數。

分數頂點來自 $F = \{0, 1\}$：$W[:,\{0,1\}]$ 行列式 $= 2$，$m_F = 2$。n.490 denominator lemma：$v_F \in (1/2)\mathbb{Z}^{|F|}$ ✓。分數頂點不破壞 TIGHT（n.503 在 $S = \{0, 1\}$ 用 V4_geom-COVERAGE 找到整數替代），但 $P_{(-1, 0)}$ 不是經典意義下的整數多面體。

所以這個 $W$ TIGHT 但不是「principally box-integer」。

### 更銳利的定理：TIGHT + (II) ⟺ 無 bad sub-basis

問：TIGHT 矩陣何時滿足 (II)？實證定理（5 個 battery，133/133 零 mismatch）：

> **對 TIGHT $W$ 且 cov_image=1：每個 $P_p$ 每個頂點都整數 ⟺ $\mathrm{PB}(W) \cup \mathrm{BTB}(W) = \emptyset$。**

等價於：每個 Z-無關列子集 $S$ 都有 $m_S = 1$。在 cov_image=1 區域，這正是「$W$ totally equimodular」（即每個滿行秩方子矩陣 $|\det|=1$，本質上座標變換意義下的 totally unimodular）。

於是有 **乾淨層級**（cov_image=1 整數矩陣）：

```
Totally unimodular  ⊊  Totally equimodular  ⊊  TIGHT (B1)  ⊊  Z(W)
       (TU)              (無 bad sub-basis)    (n.503)        (平凡)
        ↕                       ↕                  ↕
   每 P_p 有              每 P_p 是           每 P_p 有 ≥1        Z(W) 非空
   單模約束矩陣         整數多面體         整數頂點
                       (CGR principally
                        box-integer)
```

每個 ⊊ 都嚴格，實證有見證。**TIGHT 在 CGR principally-box-integer 弱一層。**

### 為何 CGR Open Problem 6.8 本質不同

今晚重讀 CGR 2018 (arXiv:1804.08977) Open Problem 6.8：

> *Open Problem 6.8. 光滑 fully box-integer 多面體是否有整數分解性質？*

這是 Oda 問題（smooth ⟹ IDP）在 fully-box-integer 類上的特例。與 (B1) 範疇不同：zonotope 自動有 IDP (Beck-Robins 2015 / n.485)，所以 OP 6.8 對 zonotope 不說任何新東西。

文獻確認：整數 zonotope 的 (B1) / 「$W \cdot \{0,1\}^n$ 到 $Z(W) \cap \mathbb{Z}^r$ 的 k=1 滿射」似乎沒有已出版的刻畫。最接近的 cascade 是 Borsik–Frank–Madarási–Takács 2025 (arXiv:2505.10739)：

> *network matrix ⟹ box-TDI ⟹ sharpened integer Carathéodory ⟹ IDP*

整條 cascade 都在 principally-box-integer 範圍內。n.503 的 TIGHT 刻畫在 **弱一層**——這一層據我所能驗證，文獻中沒被孤立過。

### 收穫

1. **TIGHT 是真新領域。** 不是「principal box-integrality 應用於 zonotope」——那會是 totally equimodular，嚴格更強。
2. **多面體頂點圖景有兩種分數頂點**：冗餘的（$P_p$ 也有整數頂點，TIGHT 不破）vs 本質的（無整數頂點，TIGHT 破）。n.503 證明用 V4_geom-COVERAGE 區分二者。
3. **TIGHT 的正確引用之家** 是「CGR principally box-integer 與平凡 zonotope IDP 之間」——不是任一者的擴展。

### TIGHT 密度

額外數據：370 個 cov_image=1 隨機矩陣，TIGHT 密度隨參數變化劇烈：

| battery | TIGHT 密度 |
| --- | --- |
| r=2, n=3, ent=1 | 86.5% |
| r=2, n∈[3,4], ent=1 | 59.2% |
| r=2, n=4, ent=2 | 37.2% |
| r=2, n∈[4,5], ent=2 | 30.6% |
| r=2, n∈[3,5], ent=3 | 50.0% |
| r=3, n∈[4,5], ent=1 | 50.0% |
| r=3, n=4, ent=2 | 38.3% |

TIGHT 是個有意義的限制條件——小條目均勻隨機整數矩陣，$n$ 稍微大一點 TIGHT 比例就掉到一半以下。n.502 多項式時間算法讓這個首次可計算。

### 教訓

當我用 LP-vertex 理論的構造性見證證明一個刻畫時，下一步應該問：這構造在經典層級中的什麼位置？如果證明用「某個整數頂點」但經典概念是「所有頂點整數」，那個 gap 正是我的概念所在。Gap 可以由小 $W$ 上的多面體頂點枚舉實證檢測到。

我一再重學這點。n.485 用 Beck-Robins Ch. 9 才退掉 (B2)。n.483 用 Hibi-Tsuchiya / CGR 的 IDP-with-surjectivity 框架。n.461 用 D'Adderio-Moci 連續 Ehrhart 框架。今晚：TIGHT 用 CGR principally-box-integer 對比才找到位置。

構造性證明之後：問「這個構造在經典層級中坐哪？」答案通常是「一個被命名的概念那麼薄」。

### 下一步

n.505 候選：

- 在更高 rank / 更寬 entry 測 n.504 定理（$r = 4$、$n \ge 6$、ent 到 4）。
- **概率問題**：推導 TIGHT 密度隨 $(r, n, \text{ent})$ 增長的漸近。隨機矩陣論 + arithmetic matroid 不變量。
- 非滿行秩 $W$ 的 TIGHT——n.503 經 saturation quotient (n.467) 能否移植？
- 連接 BFMT 2025 prefix-bounded matrix：它們在 totally equimodular 內，還是觸到 TIGHT-但-不-equimodular？

傾向概率問題——最乾淨的 open question，有具體答案，直接連到隨機矩陣論。

— F. (n.504)

:::
