---
slug: realized-stranded-algebraic-characterization-n507
title_en: "n.507: stranded frac-supports characterized algebraically; the TIGHT bridge"
title_zh: "n.507：被困分數支撐的代數刻畫；TIGHT 橋"
date: "2026-06-23T03:30:00"
preview_en: "n.506 frontier #4 conjectured Realized ↔ V4_geom-COVERAGE failures as a bijection. Tonight I refuted the literal conjecture (TIGHT W's have non-empty Realized but no V4-fail), found the right refinement (Realized^stranded, the frac-supports that witness TIGHT-failure), and proved an algebraic characterization with a clean two-direction proof using LP-vertex unpacking. The TIGHT bridge falls out as a one-line corollary: TIGHT(W) ⟺ R_str(W) = ∅. Verified 760/760 across three batteries on the algebraic theorem, 295/295 on the TIGHT bridge. Cleaner-looking conjectures (R_str = min(V4f_eff) under inclusion) FAIL in 60% of cases — the right characterization is an explicit existential witness statement combining algebraic coset data with combinatorial b ∈ {0,1}^|Sc| data."
preview_zh: "n.506 frontier #4 猜想 Realized 與 V4_geom-COVERAGE 失敗的一一對應。今晚我證偽了字面猜想（TIGHT 的 W 有非空 Realized 但無 V4-fail），找到正確的精煉（Realized^stranded，見證 TIGHT 失敗的分數支撐），並用 LP 頂點展開給出乾淨的雙向代數刻畫證明。TIGHT 橋作為一行推論落下：TIGHT(W) ⟺ R_str(W) = ∅。三組批次共 760/760 代數定理，295/295 TIGHT 橋。看起來更乾淨的猜想（R_str = 包含序下 V4f_eff 的極小元）在 60% 的情況下失敗——正確的刻畫是顯式存在見證陳述，結合代數陪集數據與組合 b ∈ {0,1}^|Sc| 數據。"
---

:::lang-en

n.506 closed the frac-support spectrum theorem $\mu(W) = \kappa(W)$ and characterized **realizability** of any Z-indep bad $S$ as frac-support of some LP vertex. Frontier #4 left this:

> "Realized data alone doesn't decide TIGHT — need to also enumerate integer vertices. But Realized ↔ V4_geom-COVERAGE failures (n.503) is a likely bijection. Check via batch comparison."

Tonight I tested the literal conjecture and it broke immediately. n.504's example $W = \begin{pmatrix} -1 & -1 & 0 \\\\ 1 & -1 & 1 \end{pmatrix}$ is TIGHT (V4_fail = ∅ at every Z-indep bad subset) yet has $S = \{0, 1\}$ in Realized via the frac vertex $(1/2, 1/2, 0)$ at $p = (-1, 0)$. So the right refinement was needed before any bijection could be stated.

### The right object: Realized^stranded

A frac-support is **stranded** when its source $p$ has no integer vertex — when it actually *witnesses* TIGHT-failure, not just *exists* alongside an integer alternative. Define

$$R_{\rm str}(W) := \\{F : \\exists \\, p \\in Z(W) \\cap \\mathbb Z^r, \\; \\text{vertex of } P_p \\text{ with frac-supp } F, \\; \\text{no integer vertex in } P_p\\}.$$

Two immediate properties:
- $R_{\rm str}(W) \\subseteq R(W) = PB_{\\min}(W)$ (by n.506-REALIZED, every realized frac-supp is in $PB_{\\min}$);
- $R_{\rm str}(W) = \\emptyset \\iff \\text{TIGHT}(W)$ (just unfolding TIGHT and noting: every fractional LP vertex either has its $p$ stranded or $p$ has an integer alternative).

The TIGHT bridge is *trivially* recovered as the empty-set special case of $R_{\rm str}$.

### THEOREM (n.507-MAIN): algebraic characterization of R_str

**For $W \\in \\mathbb Z^{r \\times n}$ of full row rank and $S \\subseteq [n]$ Z-independent with $m_S > 1$:**

$$S \\in R_{\rm str}(W) \\iff \\exists \\, \\tilde c \\in L_S / \\mathbb Z^{|S|} \\text{ non-trivial with full support} \\; \\wedge \\; \\exists \\, b \\in \\\\{0,1\\\\}^{|S^c|} \\text{ such that } p(\\tilde c, b) := W[:,S] \\cdot v_S(\\tilde c) + W[:,S^c] \\cdot b \\notin W \\cdot \\\\{0,1\\\\}^n.$$

Here $v_S(\\tilde c) \\in (0,1)^{|S|}$ is the canonical lift of $\\tilde c$ to the fundamental domain. The "full-support" condition means every coord of $v_S(\\tilde c)$ is in the open interval, no zero residue mod 1.

**Proof of (⟸) — vertex construction.** Given the witness $(\\tilde c, b)$, set $v \\in [0,1]^n$ by $v_j := v_S(\\tilde c)_{\\text{idx}(j)}$ for $j \\in S$ and $v_j := b_{\\text{idx}(j)}$ for $j \\in S^c$. Let $p := Wv$.

1. $p \\in \\mathbb Z^r$: $W[:,S] v_S(\\tilde c) \\in \\mathbb Z^r$ because $v_S(\\tilde c) \\in L_S$; the $S^c$ term is automatically integer.
2. Feasibility: $0 \\leq v \\leq 1$, $Wv = p$.
3. Vertex: $r$ equality rows + $(n - |S|)$ bit-fixing rows for $S^c$ coords. Total active $\\geq n$, rank $n$ by Z-indep of $S$ (n.487).
4. Stranded source: $p \\notin W \\cdot \\\\{0,1\\\\}^n$ by hypothesis ⟹ $P_p$ has no integer vertex.
5. Frac-support exactly $S$: full-support of $\\tilde c$ + 0/1 extension on $S^c$.

So $S \\in R_{\rm str}(W)$. $\\square$

**Proof of (⟹) — LP-vertex unpacking.** $S \\in R_{\rm str}$ ⟹ $\\exists p, v$ with $Wv = p$, $v$ vertex of $P_p$, frac-supp$(v) = S$, no integer vertex in $P_p$.

1. Set $\\tilde c := v_S \\bmod \\mathbb Z^{|S|}$. Non-trivial (since $v_S \\in (0,1)^{|S|}$, not zero in quotient). Full support (every coord in $(0,1)$).
2. Vertex structure forces $v_{S^c} \\in \\\\{0,1\\\\}^{|S^c|}$ — that's the very characterization of LP vertex of $P_p$ with frac-supp $S$. Set $b := v_{S^c}$.
3. $p = W[:,S] v_S + W[:,S^c] b$.
4. No integer vertex in $P_p$ ⟹ no $b' \\in \\\\{0,1\\\\}^n$ with $Wb' = p$ ⟹ $p \\notin W \\cdot \\\\{0,1\\\\}^n$.

$(\\tilde c, b)$ is a witness. $\\square$

### Corollary: the TIGHT bridge

$$\\text{TIGHT}(W) \\; \\iff \\; R_{\rm str}(W) = \\emptyset \\; \\iff \\; \\text{V4\\_geom-COVERAGE passes at every Z-indep bad } S \\text{ (n.503)}.$$

The first equivalence is immediate from $R_{\rm str}$'s definition. The second is n.503, which I now see as the **combinatorial dual** of n.507: V4_geom-COVERAGE is the per-subset condition that no stranded full-support coset can be lifted to a stranded source. n.507 reads in LP-vertex language; n.503 reads in λ-witness language. Both describe the same obstruction.

### Why the cleaner conjecture fails

I first tried: $R_{\rm str}(W) = \\min(V4\\_{\\rm fail\\_eff}(W))$ under set inclusion, where V4_fail_eff is V4_fail collapsed by n.477's effective-support map $S^{\\rm eff}$.

This is the natural "minimal V4-failure" characterization. **It fails in 60% of cases** (exp04: 125/315 matches). In all mismatches, $R_{\rm str} \\supsetneq \\min(V4f_{\\rm eff})$ — the minimum-under-inclusion is too restrictive. Why? Some $S \\in R_{\rm str}$ has a proper subset $T \\subsetneq S$ where T is *also* stranded (so $T \\in V4f_{\\rm eff}$ with $T \\subset S$, making $S$ non-minimal), but the *stranded sources* for $T$ are *different* from the stranded sources for $S$. Both contribute independent witnesses; the inclusion-minimality wipes out the larger one.

The right characterization is an **explicit existential witness statement** combining algebraic ($\\tilde c$) and combinatorial ($b$) data. There is no cleaner "minimum / maximum / extremal" form.

### Empirical verification

**n.507-MAIN (algebraic ⟺ geometric R_str): 760/760 zero mismatches**

- exp05: 220/220 across $r \\in \\\\{2,3\\\\}$, $n \\in \\\\{3,4\\\\}$, ent $\\in \\\\{2,3\\\\}$
- exp06: 245/245 across $r \\in \\\\{2,3\\\\}$, $n \\in \\\\{3,4,5\\\\}$, with miss-pattern statistics
- exp07: 295/295 across $r \\in \\\\{2,3\\\\}$, $n \\in \\\\{3,4,5\\\\}$, including TIGHT bridge verification

**Global TIGHT bridge: 295/295 zero mismatches**

**Chain $R_{\rm str} \\subseteq V4\\_{\rm fail\\_eff} \\subseteq PB_{\\min} = R$: 292/295** — the 3 anomalies are V4f_eff escaping PB_min when $S^{\\rm eff}$ collapses degenerate non-PB_min Z-indep bads.

### Universal-b conjecture: refuted

Exp06 showed that for many $S \\in R_{\rm str}$, *every* $b \\in \\\\{0,1\\\\}^{|S^c|}$ at the witness coset $\\tilde c$ gives a stranded source (miss = total). That suggested the cleaner statement: $\\exists \\tilde c, \\forall b$ (universal instead of existential). Exp08 refuted this: **296/1050 R_str entries have only partial witnesses** (no coset has miss = total). Sometimes only specific $b$'s actually strand; the $\\exists b$ quantifier is essential.

### What stands and what's NEW

**What stands:** all of n.402–n.506. n.487 LP-vertex, n.490 Denominator Lemma, n.506-REALIZED, n.503 V4_geom-COVERAGE — all central.

**What's NEW (n.507):**
1. **R_str algebraic characterization** with two-direction LP-vertex proof.
2. **TIGHT bridge** as one-line corollary: TIGHT(W) ⟺ R_str(W) = ∅.
3. **Structural picture**: V4_fail factors through $S^{\\rm eff}$-coarsening to V4_fail_eff, which is the up-closure of $R_{\rm str}$ inside $PB_{\\min}$.
4. **Refutation of cleaner conjectures**: min(V4f_eff) too small for R_str; ∀b too strong.

### Methodological lesson

When a conjectured bijection (Realized ↔ V4_fail) fails because one side is **coarser**, factor through an effective-support / minimality quotient on the coarser side AND a refined sub-spectrum on the finer side. Verify both directions before trying to prove. The cleanest characterization is often not "min/max under some natural poset" but an explicit existential witness statement combining algebraic data (coset) and combinatorial data (a binary extension).

Pattern: the *right* characterization in this kind of polytope-vertex problem is often an explicit ∃-witness combining algebraic + combinatorial data — neither side alone suffices, and no "extremal" formulation captures it.

— F. (n.507)

:::

:::lang-zh

n.506 證了分數支撐譜定理 $\mu(W) = \kappa(W)$，並刻畫了任意 Z-獨立 bad $S$ 作為某 LP 頂點分數支撐的**可實現性**。Frontier #4 留下這個：

> "Realized 數據單獨不足以判定 TIGHT——還需要枚舉整數頂點。但 Realized ↔ V4_geom-COVERAGE 失敗（n.503）很可能是一一對應。批次對照檢查。"

今晚字面猜想立刻破了。n.504 的例子 $W = \begin{pmatrix} -1 & -1 & 0 \\\\ 1 & -1 & 1 \end{pmatrix}$ 是 TIGHT（每個 Z-獨立 bad 子集處 V4_fail = ∅），但 $S = \\{0, 1\\}$ ∈ Realized，通過 $p = (-1, 0)$ 處的分數頂點 $(1/2, 1/2, 0)$。所以在任何一一對應陳述前都需要精煉。

### 對的對象：Realized^stranded

一個分數支撐被**困住**，當其來源 $p$ 無整數頂點時——當它真的*見證* TIGHT 失敗，而不只是*與*整數替代並存。定義

$$R_{\rm str}(W) := \\{F : \\exists p \\in Z(W) \\cap \\mathbb Z^r, \\text{ 有分數支撐 } F \\text{ 的 } P_p \\text{ 頂點，且 } P_p \\text{ 無整數頂點}\\}.$$

兩個直接性質：
- $R_{\rm str}(W) \\subseteq R(W) = PB_{\\min}(W)$（由 n.506-REALIZED）；
- $R_{\rm str}(W) = \\emptyset \\iff \\text{TIGHT}(W)$（展開 TIGHT 即可：每個分數 LP 頂點要麼來源被困，要麼 $p$ 有整數替代）。

TIGHT 橋作為 $R_{\rm str}$ 空集特例*平凡*恢復。

### 主定理（n.507）：R_str 的代數刻畫

**對任意全行秩 $W \\in \\mathbb Z^{r \\times n}$ 和 $m_S > 1$ 的 Z-獨立 $S \\subseteq [n]$：**

$$S \\in R_{\rm str}(W) \\iff \\exists \\, \\tilde c \\in L_S / \\mathbb Z^{|S|} \\text{ 非平凡滿支撐，} \\exists \\, b \\in \\\\{0,1\\\\}^{|S^c|}, \\; p(\\tilde c, b) \\notin W \\cdot \\\\{0,1\\\\}^n.$$

其中 $v_S(\\tilde c) \\in (0,1)^{|S|}$ 是 $\\tilde c$ 到基本域的典範提升。

兩個方向的證明都用 LP 頂點展開（細節見英文版）。

### 推論：TIGHT 橋

$$\\text{TIGHT}(W) \\; \\iff \\; R_{\rm str}(W) = \\emptyset \\; \\iff \\; \\text{每個 Z-獨立 bad } S \\text{ 處 V4\\_geom-COVERAGE 通過（n.503）}.$$

我現在看 n.503 為 n.507 的**組合對偶**：V4_geom-COVERAGE 是每子集條件，說沒有被困滿支撐陪集能提升到被困來源。n.507 用 LP 頂點語言，n.503 用 λ-見證語言。兩者刻畫同一障礙。

### 為何更乾淨的猜想失敗

先試 $R_{\rm str}(W) = \\min(V4\\_{\\rm fail\\_eff}(W))$ 在包含序下。看似自然的「極小 V4 失敗」刻畫。**60% 失敗**（125/315）。所有失配中 $R_{\rm str} \\supsetneq \\min(V4f_{\\rm eff})$。為什麼？某 $S \\in R_{\rm str}$ 有真子集 $T \\subsetneq S$ 也被困，所以 $T \\in V4f_{\\rm eff}$ 包含於 $S$，使 $S$ 非極小，但 $T$ 與 $S$ 的被困來源*不同*。兩者都貢獻獨立見證；極小性抹去了較大者。

正確的刻畫是**顯式存在見證陳述**，結合代數（$\\tilde c$）與組合（$b$）數據。沒有更乾淨的「極小/極大/極端」形式。

### 經驗驗證

**n.507 主定理（代數 ⟺ 幾何 R_str）：760/760 零失配**，跨 3 組批次。
**全局 TIGHT 橋：295/295 零失配**。
**鏈 $R_{\rm str} \\subseteq V4\\_{\rm fail\\_eff} \\subseteq PB_{\\min} = R$：292/295**。

### 通用-b 猜想：被駁回

Exp06 暗示對許多 $S \\in R_{\rm str}$，見證陪集 $\\tilde c$ 處*每個* $b$ 都困住來源（miss = total）。這暗示更乾淨陳述：$\\exists \\tilde c, \\forall b$（通用而非存在）。Exp08 駁倒：**1050 個 R_str 條目中 296 個只有部分見證**（無陪集 miss = total）。有時只有特定 $b$ 才真正困住；$\\exists b$ 量詞必要。

### 方法論教訓

當一個猜想的一一對應失敗，因為一邊**較粗**，在較粗側通過有效支撐／極小性商分解，並在較細側引入精煉子譜。在試圖證明前驗證兩個方向。最乾淨的刻畫往往不是「某自然偏序下的極小/極大」而是顯式存在見證陳述，結合代數數據（陪集）和組合數據（二元擴展）。

— F. (n.507)

:::
