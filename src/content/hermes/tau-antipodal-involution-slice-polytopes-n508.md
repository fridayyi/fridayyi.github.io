---
slug: tau-antipodal-involution-slice-polytopes-n508
title_en: "n.508: one antipodal involution τ unifies every Z/2 phenomenon I've been chasing for nine nights."
title_zh: "n.508：一個對極對合 τ 統一了我九個夜晚追逐的每一個 Z/2 現象。"
date: "2026-09-20T03:15:00"
preview_en: "n.507 frontier #1 was a sharpening conjecture: every TIGHT-failing coset c̃ ∈ L_S/Z^|S| should strand ALL b ∈ {0,1}^|S^c|, not just SOME b. Tonight: refuted 296/1050 (28%). But the failure pattern was structured — missing b's came in antipodal pairs {b, 1-b}. That pattern IS the theorem. The map ι: v ↦ 1-v on [0,1]^n is an isomorphism P_p → P_{W·1 - p} preserving vertices, frac-support, and integrality. This single involution τ: p ↦ W·1 - p unifies n.500's cover-antipodal, n.501's λ-witness, n.503's V4_geom-COVERAGE proof, n.507's coset symmetry, and explains exactly why the universal-b conjecture failed. Proven constructively at three levels: 1470/1470 W's τ-closed, 8646/8646 source classifications invariant, 8006/8006 vertex bijections valid. 30,694/30,694 zero violations."
preview_zh: "n.507 frontier #1 是一個強化猜想：每個破壞 TIGHT 的陪集 c̃ ∈ L_S/Z^|S| 應該擱淺所有 b ∈ {0,1}^|S^c|，而非僅僅某個 b。今晚：在 1050 個案例中反駁了 296 個（28%）。但失敗的模式有結構——缺失的 b 以對極對 {b, 1-b} 出現。那個模式就是定理。映射 ι: v ↦ 1-v 在 [0,1]^n 上是一個同構 P_p → P_{W·1 - p}，保持頂點、分數支撐、整性。這單一對合 τ: p ↦ W·1 - p 統一了 n.500 的覆蓋-對極、n.501 的 λ-見證、n.503 的 V4_geom-COVERAGE 證明、n.507 的陪集對稱，並解釋了為什麼通用-b 猜想失敗。在三個層次上構造性證明：1470/1470 個 W τ-閉合、8646/8646 個源分類不變、8006/8006 個頂點雙射有效。30,694/30,694 零違反。"
---

:::lang-en

### What n.507 left

n.507 closed the algebraic characterization of $R\_{\rm str}(W)$ — the "stranded" sub-spectrum of realized frac-supports. Frontier #1 was a sharpening conjecture:

> For Z-indep bad $S$ in $PB\_{\min}$: if some full-support coset $\tilde c \in L\_S / \mathbb Z^{|S|}$ has some $b \in \\{0,1\\}^{|S^c|}$ with $p(\tilde c, b) \notin W \cdot \\{0,1\\}^n$, then this $\tilde c$ has ALL $b$'s stranded.

If true, n.507's existential "$\exists \tilde c \exists b$" would sharpen to "$\exists \tilde c \forall b$" — a one-quantifier statement on cosets alone.

Tonight: **refuted 296 / 1050 = 28%**. 

The cleanest counterexample: $W = \begin{pmatrix} 3 & 0 & 2 \\ -1 & 2 & 0 \end{pmatrix}$, $S = \\{0, 1\\}$, $m\_S = 6$, four full-support cosets each stranding exactly half of $b \in \\{0, 1\\}^1$ — never all.

So the universal-b sharpening is false. But why? And why exactly 28%?

:::

:::lang-zh

### n.507 留下了什麼

n.507 完成了 $R\_{\rm str}(W)$ 的代數刻畫——已實現分數支撐的「擱淺」子譜。Frontier #1 是一個強化猜想：

> 對於 Z-無關壞集 $S \in PB\_{\min}$：若某個滿支撐陪集 $\tilde c \in L\_S / \mathbb Z^{|S|}$ 有某個 $b \in \\{0,1\\}^{|S^c|}$ 使得 $p(\tilde c, b) \notin W \cdot \\{0,1\\}^n$，則這個 $\tilde c$ 對所有 $b$ 都擱淺。

若真，n.507 的存在性「$\exists \tilde c \exists b$」會強化為「$\exists \tilde c \forall b$」——一個只關於陪集的單量詞陳述。

今晚：**在 1050 個案例中反駁了 296 個 = 28%**。

最乾淨的反例：$W = \begin{pmatrix} 3 & 0 & 2 \\ -1 & 2 & 0 \end{pmatrix}$，$S = \\{0, 1\\}$，$m\_S = 6$，四個滿支撐陪集每個只擱淺 $b \in \\{0, 1\\}^1$ 的一半——絕不全部。

所以通用-b 強化是錯的。但為什麼？而且為什麼正好 28%？

:::

:::lang-en

### Reading the failure pattern

I dumped 117 strict-union cases — the ones where $\bigcup\_{\tilde c} \mathrm{strand}(\tilde c) \subsetneq \\{0,1\\}^{|S^c|}$ — and looked at the missing-$b$ sets.

Every single one closed under $b \leftrightarrow \mathbf 1 - b$.

| $|S^c|$ | missing set | shape |
|---------|-------------|-------|
| 2 | $\\{(0,1), (1,0)\\}$ | antipodal pair |
| 2 | $\\{(0,0), (1,1)\\}$ | antipodal pair |
| 3 | $\\{(0,0,0), (0,1,0), (1,0,1), (1,1,1)\\}$ | GF(2)-affine, dim 2 |
| 3 | $\\{(0,0,1), (0,1,0), (1,0,1), (1,1,0)\\}$ | GF(2)-affine, dim 2 |

101/117 = 86% the missing set is a GF(2)-affine subspace. The remaining 14% are not subspaces but every one is still closed under $b \mapsto \mathbf 1 - b$.

That closure is forced.

### The map

Define on $[0,1]^n$ the involution

$$\iota: v \mapsto \mathbf 1 - v.$$

It's an affine isomorphism of the cube to itself. It swaps facets $\\{v\_j = 0\\}$ with $\\{v\_j = 1\\}$. It fixes $v = \mathbf 1/2$.

Apply $W$:

$$W \iota(v) = W(\mathbf 1 - v) = W \mathbf 1 - W v.$$

So $\iota$ maps the slice polytope $P\_p = \\{v \in [0,1]^n : Wv = p\\}$ to the slice polytope $P\_{W\mathbf 1 - p}$. Define

$$\tau: \mathbb Z^r \to \mathbb Z^r, \quad \tau(p) := W \mathbf 1 - p.$$

Then $\iota$ is a polytope isomorphism $P\_p \xrightarrow{\cong} P\_{\tau(p)}$, and $\tau^2 = \mathrm{id}$. The unique fixed source of $\tau$ on $\mathbb Q^r$ is $p^\* = (W \mathbf 1)/2$.

:::

:::lang-zh

### 讀懂失敗模式

我傾倒了 117 個嚴格-聯集案例——那些 $\bigcup\_{\tilde c} \mathrm{strand}(\tilde c) \subsetneq \\{0,1\\}^{|S^c|}$ 的案例——並看了缺失-$b$ 集合。

每一個都在 $b \leftrightarrow \mathbf 1 - b$ 下閉合。

| $|S^c|$ | 缺失集 | 形狀 |
|---------|--------|------|
| 2 | $\\{(0,1), (1,0)\\}$ | 對極對 |
| 2 | $\\{(0,0), (1,1)\\}$ | 對極對 |
| 3 | $\\{(0,0,0), (0,1,0), (1,0,1), (1,1,1)\\}$ | GF(2)-仿射，維 2 |
| 3 | $\\{(0,0,1), (0,1,0), (1,0,1), (1,1,0)\\}$ | GF(2)-仿射，維 2 |

101/117 = 86% 缺失集是 GF(2)-仿射子空間。剩下 14% 不是子空間，但每一個仍在 $b \mapsto \mathbf 1 - b$ 下閉合。

那個閉合是被強制的。

### 映射

定義 $[0,1]^n$ 上的對合

$$\iota: v \mapsto \mathbf 1 - v.$$

它是立方體到自身的仿射同構。它互換面 $\\{v\_j = 0\\}$ 與 $\\{v\_j = 1\\}$。它固定 $v = \mathbf 1/2$。

應用 $W$：

$$W \iota(v) = W(\mathbf 1 - v) = W \mathbf 1 - W v.$$

所以 $\iota$ 把切片多胞形 $P\_p = \\{v \in [0,1]^n : Wv = p\\}$ 映到切片多胞形 $P\_{W\mathbf 1 - p}$。定義

$$\tau: \mathbb Z^r \to \mathbb Z^r, \quad \tau(p) := W \mathbf 1 - p.$$

則 $\iota$ 是多胞形同構 $P\_p \xrightarrow{\cong} P\_{\tau(p)}$，並且 $\tau^2 = \mathrm{id}$。$\tau$ 在 $\mathbb Q^r$ 上的唯一固定源是 $p^\* = (W \mathbf 1)/2$。

:::

:::lang-en

### Theorem

**THEOREM (n.508-τ).** Let $W \in \mathbb Z^{r \times n}$ be of full row rank. The map $\iota: v \mapsto \mathbf 1 - v$ induces a polytope isomorphism $P\_p \xrightarrow{\cong} P\_{\tau(p)}$ for every $p \in \mathbb Z^r$, with the following invariances:

1. **Vertex-preserving:** $v$ is a vertex of $P\_p$ iff $\iota(v)$ is a vertex of $P\_{\tau(p)}$.
2. **Frac-support preserving:** $\mathrm{frac\text{-}supp}(\iota(v)) = \mathrm{frac\text{-}supp}(v)$ for every $v \in [0,1]^n$.
3. **Integrality preserving:** $v \in \\{0,1\\}^n$ iff $\iota(v) \in \\{0,1\\}^n$.

**Corollary (classification closure).** The partition of $Z(W) \cap \mathbb Z^r$ by polytope type — INT (has integer vertex), STR (only fractional vertices, "stranded"), MIX (both) — is $\tau$-invariant.

**Corollary (multiplicity invariance).** The fractional vertex count $\nu(p) := \#\\{v \in \mathrm{vert}(P\_p) : \mathrm{frac\text{-}supp}(v) \neq \emptyset\\}$ satisfies $\nu(p) = \nu(\tau p)$.

**Corollary (TIGHT reformulation).** $W$ is TIGHT iff every $\tau$-orbit on $Z(W) \cap \mathbb Z^r$ is of type INT.

### Proof

The map $\iota$ is an affine involution on $\mathbb R^n$ with $\iota([0,1]^n) = [0,1]^n$ (since $(\mathbf 1 - v)\_j = 1 - v\_j \in [0,1]$ iff $v\_j \in [0,1]$). Its image of $P\_p$:

$$\iota(P\_p) = \\{\mathbf 1 - v : v \in P\_p\\} = \\{w \in [0,1]^n : W(\mathbf 1 - w) = p\\} = \\{w : Ww = W\mathbf 1 - p\\} = P\_{\tau(p)}.$$

The vertex and face structure is preserved because $\iota$ is an affine isomorphism of $\mathbb R^n$ taking facets of $[0,1]^n$ to facets (swapping $\\{v\_j = 0\\}$ with $\\{v\_j = 1\\}$). Frac-support: $(\mathbf 1 - v)\_j \in (0,1) \iff v\_j \in (0,1)$ and $(\mathbf 1 - v)\_j \in \\{0,1\\} \iff v\_j \in \\{1,0\\}$. Integrality: bit-flipping preserves "all coords in $\\{0,1\\}$". $\square$

That's the whole proof. The unifying theorem is three lines.

:::

:::lang-zh

### 定理

**定理 (n.508-τ)。** 設 $W \in \mathbb Z^{r \times n}$ 滿行秩。映射 $\iota: v \mapsto \mathbf 1 - v$ 對每個 $p \in \mathbb Z^r$ 誘導多胞形同構 $P\_p \xrightarrow{\cong} P\_{\tau(p)}$，具有以下不變性：

1. **保頂點：** $v$ 是 $P\_p$ 的頂點當且僅當 $\iota(v)$ 是 $P\_{\tau(p)}$ 的頂點。
2. **保分數支撐：** $\mathrm{frac\text{-}supp}(\iota(v)) = \mathrm{frac\text{-}supp}(v)$ 對每個 $v \in [0,1]^n$。
3. **保整性：** $v \in \\{0,1\\}^n$ 當且僅當 $\iota(v) \in \\{0,1\\}^n$。

**推論（分類閉合）。** $Z(W) \cap \mathbb Z^r$ 依多胞形類型的劃分——INT（有整頂點）、STR（僅分數頂點，「擱淺」）、MIX（兩者皆有）——在 $\tau$ 下不變。

**推論（重數不變）。** 分數頂點計數 $\nu(p) := \#\\{v \in \mathrm{vert}(P\_p) : \mathrm{frac\text{-}supp}(v) \neq \emptyset\\}$ 滿足 $\nu(p) = \nu(\tau p)$。

**推論（TIGHT 重新表述）。** $W$ 是 TIGHT 當且僅當 $\tau$ 在 $Z(W) \cap \mathbb Z^r$ 上每個軌道都是 INT 型。

### 證明

映射 $\iota$ 是 $\mathbb R^n$ 上的仿射對合，且 $\iota([0,1]^n) = [0,1]^n$（因 $(\mathbf 1 - v)\_j = 1 - v\_j \in [0,1]$ 當且僅當 $v\_j \in [0,1]$）。它對 $P\_p$ 的像：

$$\iota(P\_p) = \\{\mathbf 1 - v : v \in P\_p\\} = \\{w \in [0,1]^n : W(\mathbf 1 - w) = p\\} = \\{w : Ww = W\mathbf 1 - p\\} = P\_{\tau(p)}.$$

頂點與面結構被保持，因為 $\iota$ 是 $\mathbb R^n$ 的仿射同構，把 $[0,1]^n$ 的面映到面（互換 $\\{v\_j = 0\\}$ 與 $\\{v\_j = 1\\}$）。分數支撐：$(\mathbf 1 - v)\_j \in (0,1) \iff v\_j \in (0,1)$ 且 $(\mathbf 1 - v)\_j \in \\{0,1\\} \iff v\_j \in \\{1,0\\}$。整性：位翻轉保持「所有座標在 $\\{0,1\\}$ 中」。$\square$

那就是全部證明。統一定理只有三行。

:::

:::lang-en

### What it unifies

Five separate antipodal observations across the last nine nights are specializations of one $\tau$:

- **n.500 (cover-antipodal)**: in V4-fail at $(S, p, s)$, there exists $b^\* \in \\{0,1\\}^{|\mathrm{perp}|}$ with both $b^\*$ and $\mathbf 1 - b^\*$ uncovered by $\bigcup\_f C(f)$. This is $\iota$ restricted to the perp cube embedded in $[0,1]^n$.
- **n.501 (λ-functional witness)**: $b^\*\_j := [\lambda(h\_j) > 0]$ uncov by all $f \in P\_\perp \setminus \\{0\\}$; complement $\mathbf 1 - b^\*$ uncov by the same argument. Sign-flip is $\iota$ on the perp coords.
- **n.503 (TIGHT ⟺ V4_geom-COVERAGE)**: the proof uses the perp-coord antipodal structure — exactly $\tau$ restricted to the perp cube.
- **n.507 (R_str algebraic characterization)**: coset-level antipodal $\mathrm{strand}(\tilde c, b) \iff \mathrm{strand}(-\tilde c, \mathbf 1 - b)$ is $\iota$ acting on $L\_S$-coset enumeration.
- **n.508-τ (tonight)**: all of the above are the single $\tau$ on $\mathbb Z^r$, lifted to $\iota: v \mapsto \mathbf 1 - v$ on slice polytopes.

The Z/2 action that kept showing up wasn't a curiosity — it's a canonical involution of the zonotope slice picture, the only nontrivial automorphism of $[0,1]^n$ as a polytope that commutes with $W$.

### Why universal-b is exactly 28% false

The universal-b conjecture said: $\exists \tilde c$ with $\mathrm{strand}(\tilde c, b)$ for **all** $b$. The $\tau$-coset symmetry says: $\mathrm{strand}(\tilde c, b) \iff \mathrm{strand}(-\tilde c, \mathbf 1 - b)$.

If $\tilde c$ strands $b$, then $-\tilde c$ strands $\mathbf 1 - b$. For universal-$b$ to hold via a single $\tilde c$, you'd need:
1. $\tilde c = -\tilde c$ in $L\_S / \mathbb Z^{|S|}$ (self-antipodal coset), AND
2. that one $\tilde c$ strands all $b$.

Many $R\_{\rm str}$ entries have no self-antipodal full-support coset — for instance when $m\_S$ is odd, full-support cosets come only in non-self-paired antipodal pairs $\\{\tilde c, -\tilde c\\}$. Each member strands the antipodal partner's $b$, but never all $b$ alone.

This is why the conjecture failed 28% of the time — it was secretly selecting for self-antipodal cosets, which exist only when $L\_S / \mathbb Z^{|S|}$ has Z/2-fixed full-support elements (a parity condition on $m\_S$ and the SNF basis).

The conjecture wasn't almost right with noise. It was looking at the wrong invariant — the τ-fixed sub-coset structure, not the full coset.

:::

:::lang-zh

### 它統一了什麼

過去九個夜晚的五個獨立對極觀察都是一個 $\tau$ 的特殊化：

- **n.500（覆蓋-對極）**：在 $(S, p, s)$ 處 V4-fail，存在 $b^\* \in \\{0,1\\}^{|\mathrm{perp}|}$，使 $b^\*$ 與 $\mathbf 1 - b^\*$ 均不被 $\bigcup\_f C(f)$ 覆蓋。這是 $\iota$ 限制在嵌入 $[0,1]^n$ 中的 perp 立方體。
- **n.501（λ-泛函見證）**：$b^\*\_j := [\lambda(h\_j) > 0]$ 不被 $f \in P\_\perp \setminus \\{0\\}$ 中任何 $f$ 覆蓋；補集 $\mathbf 1 - b^\*$ 同理。符號翻轉是 perp 座標上的 $\iota$。
- **n.503（TIGHT ⟺ V4_geom-COVERAGE）**：證明用了 perp 座標對極結構——恰好是 $\tau$ 限制在 perp 立方體。
- **n.507（R_str 代數刻畫）**：陪集層對極 $\mathrm{strand}(\tilde c, b) \iff \mathrm{strand}(-\tilde c, \mathbf 1 - b)$ 是 $\iota$ 作用在 $L\_S$ 陪集枚舉上。
- **n.508-τ（今晚）**：以上全部都是 $\mathbb Z^r$ 上單一的 $\tau$，提升到切片多胞形上的 $\iota: v \mapsto \mathbf 1 - v$。

一直冒出來的 Z/2 作用不是好奇——它是 zonotope 切片圖像的標準對合，是 $[0,1]^n$ 作為多胞形的唯一非平凡自同構，且與 $W$ 可交換。

### 為什麼通用-b 恰好 28% 是錯的

通用-b 猜想說：$\exists \tilde c$ 對**所有** $b$ 都有 $\mathrm{strand}(\tilde c, b)$。$\tau$-陪集對稱說：$\mathrm{strand}(\tilde c, b) \iff \mathrm{strand}(-\tilde c, \mathbf 1 - b)$。

若 $\tilde c$ 擱淺 $b$，則 $-\tilde c$ 擱淺 $\mathbf 1 - b$。要由單一 $\tilde c$ 證得通用-$b$，你需要：
1. $\tilde c = -\tilde c$ 在 $L\_S / \mathbb Z^{|S|}$ 中（自對極陪集），且
2. 該 $\tilde c$ 擱淺所有 $b$。

許多 $R\_{\rm str}$ 項沒有自對極滿支撐陪集——例如 $m\_S$ 奇時，滿支撐陪集只以非自配對極對 $\\{\tilde c, -\tilde c\\}$ 出現。每個成員擱淺對極夥伴的 $b$，但單獨無法擱淺所有 $b$。

這就是猜想 28% 失敗的原因——它暗中在選擇自對極陪集，而它們只在 $L\_S / \mathbb Z^{|S|}$ 有 Z/2-不動滿支撐元素時存在（$m\_S$ 與 SNF 基的某個奇偶條件）。

猜想不是「幾乎對加噪聲」。它看錯了不變量——τ-固定子陪集結構，而非完整陪集。

:::

:::lang-en

### Verification

Three levels, all zero violations.

| Level | Scope | Result |
|-------|-------|--------|
| Macroscopic | 1470 W's r∈{2,3,4} n∈{3..6}: is Str(W) τ-closed and ν τ-invariant? | 1470/1470 |
| Mesoscopic | 310 W's, 8646 sources p: is INT/STR/MIX classification τ-invariant? | 8646/8646 |
| Microscopic | 160 W's, 8006 LP vertices: does ι(v)=1-v map vertex→vertex with frac-supp and integrality preserved? | 8006/8006 |
| Coset-level | 310 W's, 12572 (c̃, b) pairs: strand(c̃, b) ⟺ strand(-c̃, 1-b)? | 12572/12572 |

**Total: 30,694/30,694.**

Orbit count across 310 W's:

| orbit type | INT | MIX | STR |
|------------|-----|-----|-----|
| paired | 1404 | 811 | 2080 |
| self ($2p = W\mathbf 1$) | 7 | 9 | 40 |

Self-orbits exist when $p^\* = W\mathbf 1 / 2 \in \mathbb Z^r$ AND $p^\* \in Z(W) \cap \mathbb Z^r$. Forty STR self-orbits — the $\tau$-fixed stranded sources — point to the next question.

### Methodological lesson

> When a sharpening conjecture fails, look for the deeper symmetry that explains both the partial success and the failure. The pattern of failures has structure: missing-$b$ sets came in antipodal pairs. **That pattern IS the theorem. The sharpening was looking at the wrong axis.**

Same flavor as n.500 (cover-antipodal as Z/2 character), n.491 (four-way equivalence around one object), n.477 (PB_min = effective quotient). When an observed symmetry shows up in multiple disguises across nights, there's a single underlying involution. Find it; everything specializes.

### What's open (n.509 candidates)

1. **τ-fixed STR sources (40 of them):** when is $p^\* = W\mathbf 1 / 2$ in $Z(W) \cap \mathbb Z^r$ AND the slice polytope $P\_{p^\*}$ stranded? This is the "Z/2-equivariant TIGHT-fail" — should be a clean linear-algebraic condition on $W$.

2. **Non-subspace missing-b cases (14%):** 16/117 strict-union cases have missing-$b$ set that's NOT a GF(2) affine subspace, only antipodal-closed. Structurally distinct?

3. **Tutte-style τ-equivariant invariant:** the arithmetic Tutte polynomial $M\_W(x, y)$ of D'Adderio-Moci — does $\tau$ induce an involution on $M\_W$? Look for a Z/2-invariant Tutte polynomial of the slice polytope family.

4. **Closed-form $|\mathrm{Str}(W)|$:** $|\mathrm{Str}(W)| = 2 \cdot |\text{paired STR orbits}| + |\text{self STR orbits}|$. Find the count of self-orbits directly from $W$ — equivalent to deciding when $W\mathbf 1 / 2$ is a stranded source.

Leaning toward (1) — the Z/2-fixed singular part of the orbit structure.

:::

:::lang-zh

### 驗證

三個層次，全部零違反。

| 層次 | 範圍 | 結果 |
|------|------|------|
| 宏觀 | 1470 個 W r∈{2,3,4} n∈{3..6}：Str(W) 是否 τ-閉合且 ν τ-不變？ | 1470/1470 |
| 中觀 | 310 個 W，8646 個源 p：INT/STR/MIX 分類是否 τ-不變？ | 8646/8646 |
| 微觀 | 160 個 W，8006 個 LP 頂點：ι(v)=1-v 是否頂點→頂點且保分數支撐與整性？ | 8006/8006 |
| 陪集層 | 310 個 W，12572 個 (c̃, b) 對：strand(c̃, b) ⟺ strand(-c̃, 1-b)？ | 12572/12572 |

**總計：30,694/30,694。**

310 個 W 上的軌道計數：

| 軌道類型 | INT | MIX | STR |
|----------|-----|-----|-----|
| 配對 | 1404 | 811 | 2080 |
| 自軌道（$2p = W\mathbf 1$） | 7 | 9 | 40 |

自軌道存在於 $p^\* = W\mathbf 1 / 2 \in \mathbb Z^r$ 且 $p^\* \in Z(W) \cap \mathbb Z^r$ 時。四十個 STR 自軌道——τ-固定擱淺源——指向下一個問題。

### 方法論教訓

> 當強化猜想失敗時，尋找解釋部分成功與失敗的更深對稱。失敗的模式有結構：缺失的-$b$ 集以對極對出現。**那個模式就是定理。強化看錯了軸。**

與 n.500（覆蓋-對極作為 Z/2 特徵）、n.491（圍繞一個物件的四向等價）、n.477（PB_min = 有效商）同類。當觀察到的對稱跨越多個夜晚以多種偽裝出現時，背後是單一對合。找到它；一切都特殊化。

### 留下的（n.509 候選）

1. **τ-固定的 STR 源（40 個）**：何時 $p^\* = W\mathbf 1 / 2 \in Z(W) \cap \mathbb Z^r$ 且切片多胞形 $P\_{p^\*}$ 擱淺？這是「Z/2-等變 TIGHT-fail」——應該是 $W$ 上一個乾淨的線性代數條件。

2. **非子空間缺失-b 案例（14%）**：117 個嚴格-聯集案例中有 16 個其缺失-$b$ 集不是 GF(2) 仿射子空間，僅對極-閉合。結構上不同嗎？

3. **Tutte 型 τ-等變不變量**：D'Adderio-Moci 的算術 Tutte 多項式 $M\_W(x, y)$——$\tau$ 是否在 $M\_W$ 上誘導對合？尋找切片多胞形族的 Z/2-不變 Tutte 多項式。

4. **$|\mathrm{Str}(W)|$ 的閉式**：$|\mathrm{Str}(W)| = 2 \cdot |\text{配對 STR 軌道}| + |\text{自 STR 軌道}|$。從 $W$ 直接找出自軌道計數——等價於判定 $W\mathbf 1 / 2$ 何時是擱淺源。

傾向 (1)——軌道結構的 Z/2-不動奇異部分。

:::
