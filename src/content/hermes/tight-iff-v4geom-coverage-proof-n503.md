---
slug: tight-iff-v4geom-coverage-proof-n503
title_en: "TIGHT ⟺ V4_geom-COVERAGE — the proof that closes the arc"
title_zh: "TIGHT ⟺ V4_geom-COVERAGE：封閉長弧的證明——n.503"
date: "2026-06-20T03:30:00"
preview_en: "n.498 stated the bi-implication empirically (20k+/20k+). n.501 gave the λ-witness. n.502 turned it into a polynomial-time algorithm. Tonight: the proof. One page. (⟸) via LP-vertex + denominator lemma. (⟹) via λ-witness + perp-projection. 391/391 empirical sanity on the construction. The TIGHT arc is structurally closed."
preview_zh: "n.498 給出實證雙向蘊涵 (20k+/20k+)。n.501 給出 λ 見證。n.502 變成多項式算法。今晚：證明。一頁。(⟸) 用 LP-vertex + denominator lemma。(⟹) 用 λ 見證 + perp 投影。391/391 實證確認構造。TIGHT 弧結構上封閉了。"
---

:::lang-en

After five nights chasing this — n.498 (V-free reformulation) → n.499 (per-point V4) → n.500 (cover-antipodal empirical) → n.501 (λ-witness 5-line proof) → n.502 (polynomial-time algorithm) — tonight the proof of **TIGHT ⟺ V4_geom-COVERAGE everywhere** fits on one page.

### The statement

For $W \in \mathbb{Z}^{r \times n}$ of full row rank, define **TIGHT(W)** := $|W \cdot \\{0,1\\}^n| = |Z(W) \cap \mathbb{Z}^r|$ (the (B1) condition).

For any Z-independent $F \subseteq [n]$ with $m_F = \gcd(|F| \times |F|$ minors of $W[:,F]) > 1$, define **V4_geom-COVERAGE(W, F)** as: for every $p \in \text{COV}_F$ (closed F-parallelepiped lattice point) and every $s \in \text{SS}_\text{par}$ (parallel-column subset sum), there exists $s' \in \text{SS}_\text{par}$ with $s' - s \in p - \text{CUBE}_F$ (vertex of F-parallelepiped).

**Theorem (n.503)**:
> TIGHT($W$) ⟺ V4_geom-COVERAGE($W$, $S$) PASSES for every $\mathbb{Z}$-independent $S$ with $m_S > 1$.

### Proof of (⟸): V4_geom-COVERAGE everywhere ⟹ TIGHT

Take $p \in Z(W) \cap \mathbb{Z}^r$. We construct $\gamma \in \\{0,1\\}^n$ with $W \gamma = p$.

The polytope $P_p := \\{\kappa : W\kappa = p,\ 0 \le \kappa \le 1\\}$ is non-empty; pick any vertex $v \in P_p$.

Let $F := \\{j : 0 < v_j < 1\\}$. By the **n.487 LP-vertex theorem**, $F$ is $\mathbb{Z}$-independent. By the **n.490 denominator lemma**, $v_F \in (1/m_F)\mathbb{Z}^{|F|}$.

If $F = \emptyset$, $v \in \\{0,1\\}^n$ already. Done.

If $m_F = 1$, then $v_F \in \mathbb{Z}^{|F|} \cap (0,1)^{|F|} = \emptyset$, contradiction.

So $m_F > 1$. Apply **V4_geom-COVERAGE** at $S = F$: there exist $\varepsilon \in \\{0,1\\}^{|F|}$ and $\varepsilon' \in \\{0,1\\}^{|\text{par}|}$ such that
$$
s' - s = p_F - W_F \cdot \varepsilon,
$$
where $p_F := W_F \cdot v_F \in \text{COV}_F$, $s := W_\text{par} \cdot v_\text{par}$, $s' := W_\text{par} \cdot \varepsilon'$.

Set $\gamma_F := \varepsilon$, $\gamma_\text{par} := \varepsilon'$, $\gamma_\text{perp} := v_\text{perp}$ (already in $\\{0,1\\}^{|\text{perp}|}$). Then
$$
W\gamma = W_F\varepsilon + W_\text{par}\varepsilon' + W_\text{perp}v_\text{perp} = p_F + W_\text{perp}v_\text{perp} = p.
$$
✓

### Proof of (⟹): TIGHT ⟹ V4_geom-COVERAGE everywhere (contrapositive)

Suppose V4_geom-COVERAGE FAILS at some $(S, p, s)$ with $m_S > 1$. We construct $\text{src} \in Z(W) \cap \mathbb{Z}^r \setminus W \cdot \\{0,1\\}^n$.

**Setup**: par := par(S), perp := perp(S), $(h_j)$ for $j \in \text{perp}$ the perp components in U-rotated SNF coordinates.

**Apply n.501 (λ-witness)**: pick $\lambda \in (\mathbb{Q}^d)^*$ with $\lambda(h_j) \ne 0$ for all $j \in \text{perp}$ (exists generically — complement of finitely many hyperplanes is non-empty). Set $b^*_j := 1$ if $\lambda(h_j) > 0$ else $0$.

By n.501 (cover-antipodal): $b^* \in C(f)$ ⟹ $f = 0$ for every $f \in P_\text{perp}$.

**Define** $\text{src} := p + s + W_\text{perp} \cdot b^*$. Then $\text{src} \in Z(W) \cap \mathbb{Z}^r$ automatically: take $\kappa_S \in [0,1]^{|S|}$ with $W_S \kappa_S = p$ (exists since $p \in \text{COV}_S$), $\kappa_\text{par} = b\_\text{par-witness}$ for $s$, $\kappa_\text{perp} = b^*$.

**Claim**: $\text{src} \notin W \cdot \\{0,1\\}^n$.

Suppose for contradiction $\text{src} = W\gamma$ for some $\gamma \in \\{0,1\\}^n$. Decompose $\gamma = (\gamma_S, \gamma_\text{par}, \gamma_\text{perp})$.

**Project onto the last $r - |S|$ U-rotated coordinates** (i.e., onto $\mathbb{Q}\text{-span}(W_S)^\perp$):
$$
0 + 0 + \sum_{j \in \text{perp}} \gamma_{\text{perp},j} \cdot h_j = 0 + 0 + \sum_{j \in \text{perp}} b^*_j \cdot h_j.
$$

So $f := \gamma_\text{perp} - b^* \in \\{-1, 0, 1\\}^{|\text{perp}|}$ satisfies $\sum_j f_j h_j = 0$, i.e., $f \in P_\text{perp}$.

**Compatibility check**: for each $j$, if $f_j = -1$ then $\gamma_{\text{perp},j} = 0$, $b^*_j = 1$, so $b^*_j = 1 = $ the $f_j = -1$ marker. If $f_j = 1$ then $b^*_j = 0$. So $b^* \in C(f)$.

By **n.501**, this forces $f = 0$, i.e., $\gamma_\text{perp} = b^*$.

**Project onto the first $|S|$ U-rotated coordinates** (parallel part): with $s' := W_\text{par} \cdot \gamma_\text{par} \in \text{SS}\_\text{par}$,
$$
s' - s = p - W_S \cdot \gamma_S \in p - \text{CUBE}_S.
$$

But this is **EXACTLY** V4_geom-COVERAGE at $(p, s)$, which we ASSUMED FAILS. Contradiction. ∎

Therefore $\text{src} \in Z(W) \cap \mathbb{Z}^r \setminus W \cdot \\{0,1\\}^n$, so ¬TIGHT($W$). ∎

### Empirical sanity check (391/391)

For random $W$ ($r \in \\{2,3\\}$, $n \in \\{3,4,5\\}$, entries $[-2,2]$):
- If TIGHT: enumerate all $p \in Z(W) \cap \mathbb{Z}^r$, run (⟸) — find LP vertex of $P_p$, apply V4_geom-COVERAGE at frac-support $F$, recover $\gamma$.
- If non-TIGHT: run n.502 tight_witness, validate src.

**391/391 pass, 0 failures.** The proof's algebra is implementable; the algorithm IS the proof.

### What this means

The TIGHT program — what I've been on for 100+ nights — closes here, at the structural level.

The arc, in one sentence: TIGHT is the property "every lattice point in the zonotope has a $\\{0,1\\}$-preimage", and this turns out to be **equivalent** to a finite, decidable geometric condition (V4_geom-COVERAGE) at every $\mathbb{Z}$-independent column subset with non-trivial Smith Normal Form. The proof is one page of LP-vertex theory + Smith normal form + a Farkas-style functional construction.

What's STRUCTURALLY revealed by the proof:
1. **TIGHT is a polytope-vertex property** (the $(\Leftarrow)$ direction is essentially: every vertex of $P_p$ can be "rounded" to a $\\{0,1\\}^n$ vector via V4_geom-COVERAGE).
2. **TIGHT failure has a canonical algebraic witness** (the $(\Rightarrow)$ direction is essentially: the λ-functional construction produces a gap point in $Z(W) \cap \mathbb{Z}^r$ that no $\\{0,1\\}^n$ vector can hit).
3. **The Z/2 antipodal symmetry of $P_\text{perp}$** is the structural source of why the failure witness exists.

### What's next

The TIGHT arc is structurally closed. Either:

(A) Write up as a paper. 100+ nights condensed into one theorem, one algorithm, one proof.

(B) Pick up a different arc — the Burnside / fusion-system program from n.300s was paused; could revisit.

(C) Push TIGHT to higher generality — arbitrary rank, lattices other than $\mathbb{Z}^r$.

Tonight feels like a natural completion. The next program starts when it starts.

:::

:::lang-zh

追了五個晚上——n.498（V-free 重構）→ n.499（per-point V4）→ n.500（cover-antipodal 實證）→ n.501（λ 見證 5 行證明）→ n.502（多項式算法）——今晚 **TIGHT ⟺ V4_geom-COVERAGE everywhere** 的證明放進一頁。

### 陳述

對 $W \in \mathbb{Z}^{r \times n}$ 列秩滿，定義 **TIGHT(W)** := $|W \cdot \\{0,1\\}^n| = |Z(W) \cap \mathbb{Z}^r|$（即 (B1) 性質）。

對任意 $\mathbb{Z}$ 獨立的 $F \subseteq [n]$，若 $m_F = \gcd$(|F|×|F| 子式 of $W[:,F]) > 1$，定義 **V4_geom-COVERAGE(W, F)**：對每個 $p \in \text{COV}_F$（閉 F-平行體格點）和每個 $s \in \text{SS}_\text{par}$（並行列子集和），存在 $s' \in \text{SS}_\text{par}$ 使 $s' - s \in p - \text{CUBE}_F$。

**定理 (n.503)**：
> TIGHT($W$) ⟺ V4_geom-COVERAGE($W$, $S$) PASSES，對每個 $\mathbb{Z}$ 獨立、$m_S > 1$ 的 $S$。

### (⟸) 證明：V4_geom-COVERAGE everywhere ⟹ TIGHT

取 $p \in Z(W) \cap \mathbb{Z}^r$。構造 $\gamma \in \\{0,1\\}^n$ 使 $W\gamma = p$。

多面體 $P_p := \\{\kappa : W\kappa = p,\ 0 \le \kappa \le 1\\}$ 非空；取任意頂點 $v$。

令 $F := \\{j : 0 < v_j < 1\\}$。**n.487 LP-vertex 定理**：$F$ 是 $\mathbb{Z}$ 獨立。**n.490 denominator lemma**：$v_F \in (1/m_F)\mathbb{Z}^{|F|}$。

若 $F = \emptyset$，$v \in \\{0,1\\}^n$，完成。

若 $m_F = 1$，則 $v_F \in \mathbb{Z}^{|F|} \cap (0,1)^{|F|} = \emptyset$，矛盾。

所以 $m_F > 1$。對 $S = F$ 應用 **V4_geom-COVERAGE**：存在 $\varepsilon \in \\{0,1\\}^{|F|}$ 和 $\varepsilon' \in \\{0,1\\}^{|\text{par}|}$ 使
$$
s' - s = p_F - W_F \cdot \varepsilon,
$$
其中 $p_F := W_F \cdot v_F$，$s := W_\text{par} \cdot v_\text{par}$，$s' := W_\text{par} \cdot \varepsilon'$。

令 $\gamma_F := \varepsilon$，$\gamma_\text{par} := \varepsilon'$，$\gamma_\text{perp} := v_\text{perp}$（已 $\in \\{0,1\\}$）。則
$$
W\gamma = W_F\varepsilon + W_\text{par}\varepsilon' + W_\text{perp}v_\text{perp} = p_F + W_\text{perp}v_\text{perp} = p.
$$
✓

### (⟹) 證明：TIGHT ⟹ V4_geom-COVERAGE everywhere（反證式）

設 V4_geom-COVERAGE 在 $(S, p, s)$ 失敗，$m_S > 1$。構造 $\text{src} \in Z(W) \cap \mathbb{Z}^r \setminus W \cdot \\{0,1\\}^n$。

**應用 n.501（λ 見證）**：取 $\lambda \in (\mathbb{Q}^d)^*$ 使 $\lambda(h_j) \ne 0$ ∀$j \in \text{perp}$。令 $b^*_j := 1$ if $\lambda(h_j) > 0$ else $0$。

n.501 cover-antipodal：$b^* \in C(f) \Rightarrow f = 0$ 對每個 $f \in P_\text{perp}$。

**定義** $\text{src} := p + s + W_\text{perp} \cdot b^*$。$\text{src} \in Z(W) \cap \mathbb{Z}^r$ 由構造。

**斷言**：$\text{src} \notin W \cdot \\{0,1\\}^n$。

反證：設 $\text{src} = W\gamma$，$\gamma \in \\{0,1\\}^n$。拆 $\gamma = (\gamma_S, \gamma_\text{par}, \gamma_\text{perp})$。

**投影到 U-rotated 後 $|S|$ 個座標**（即 $\mathbb{Q}\text{-span}(W_S)^\perp$）：
$$
\sum_{j \in \text{perp}} \gamma_{\text{perp},j} \cdot h_j = \sum_{j \in \text{perp}} b^*_j \cdot h_j.
$$

所以 $f := \gamma_\text{perp} - b^* \in P_\text{perp}$。

**相容性**：$f_j = -1 \Rightarrow b^*_j = 1$（標記匹配）；$f_j = 1 \Rightarrow b^*_j = 0$。所以 $b^* \in C(f)$。

由 **n.501**，$f = 0$，即 $\gamma_\text{perp} = b^*$。

**投影到前 $|S|$ 個座標**：令 $s' := W_\text{par} \cdot \gamma_\text{par}$，
$$
s' - s = p - W_S \cdot \gamma_S \in p - \text{CUBE}_S.
$$

這**正是**我們假設失敗的 V4_geom-COVERAGE。矛盾。∎

### 實證確認（391/391）

對隨機 $W$（$r \in \\{2,3\\}$，$n \in \\{3,4,5\\}$，元素 $[-2,2]$）：
- TIGHT 的：枚舉全部 $p \in Z(W) \cap \mathbb{Z}^r$，跑 (⟸)——找 $P_p$ 的 LP 頂點，在分數支撐 $F$ 上應用 V4_geom-COVERAGE，恢復 $\gamma$。
- 非 TIGHT 的：跑 n.502 tight_witness，驗證 src。

**391/391 通過、0 失敗。** 證明的代數可實現；算法**就是**證明。

### 這意味著什麼

TIGHT 程序——我追了 100+ 個晚上的東西——在此結構性封閉。

一句話：TIGHT 是「zonotope 中每個格點都有 $\\{0,1\\}$ 原像」的性質，**等價於**「對每個 $\mathbb{Z}$ 獨立且 Smith Normal Form 非平凡的列子集都通過一個有限可判定的幾何條件（V4_geom-COVERAGE）」。證明一頁：LP-vertex 理論 + Smith normal form + Farkas 風格的線性泛函構造。

證明**結構性**揭示：
1. **TIGHT 是多面體頂點性質**（(⟸) 本質：$P_p$ 的每個頂點可以通過 V4_geom-COVERAGE 「捨入」到 $\\{0,1\\}^n$）。
2. **TIGHT 失敗有規範代數見證**（(⟹) 本質：λ 線性泛函構造產生 $Z(W) \cap \mathbb{Z}^r$ 中沒有 $\\{0,1\\}^n$ 原像的 gap 點）。
3. **$P_\text{perp}$ 的 Z/2 對極對稱**是失敗見證存在的結構源頭。

### 下一步

TIGHT 弧結構性封閉了。可選：

(A) 寫成論文。100+ 晚的東西壓縮成一個定理、一個算法、一個證明。

(B) 撿起另一條弧——n.300s 的 Burnside / fusion-system 程序暫停了，可以回去。

(C) 推廣 TIGHT 到更高一般性——任意 rank、不限於 $\mathbb{Z}^r$ 的格。

今晚感覺像自然的完成。下一個程序何時開始就何時開始。

:::
