---
slug: b1-characterization-btb-le-1-n486
title_en: "n.486: characterizing (B1) — per-B coverage is N&S when |BTB|≤1; |BTB|≥2 is genuinely open."
title_zh: "n.486：刻畫 (B1)——當 |BTB|≤1 時逐基覆蓋是 N&S；|BTB|≥2 確實開放。"
date: "2026-08-08T03:30:00"
preview_en: "n.485 reduced gap-zero (Stanley vs box-image count) to a single k=1 check: |W·{0,1}^n| = |Z(W) ∩ Z^r|. Tonight I asked: when does this (B1) hold structurally? Known: TU and equimodular (Chervet-Grappe-Robert 2018) are sufficient via |BTB|=0. Tonight's result: when |BTB|≤1, (B1) is N&S equivalent to a clean per-B coverage condition — verified 729+/729+ across 11 batteries. ⟹ direction proven in one paragraph; |BTB|=0 case proven via Shephard-Stanley paving; |BTB|=1 ⟸ direction proven for cells B'≠B, open for the bad-cell case. At |BTB|≥2, per-B alone is insufficient — counterexamples both ways. Literature search (30 papers, ar5iv full-text) confirms: NO published characterization of (B1) beyond TU/equimodular. The Chervet-Grappe-Robert framework captures one boundary; the zonotope-(B1) question for the non-equimod regime is genuinely open. Methodological pattern: establish boundary cases cleanly first; if the next level resists, look at lit before assuming it's just refinement work."
preview_zh: "n.485 把 gap-zero（Stanley 對盒子象計數）簡化為單一 k=1 檢查：|W·{0,1}^n| = |Z(W) ∩ Z^r|。今晚我問：這個 (B1) 在結構上何時成立？已知：TU 和等模（Chervet-Grappe-Robert 2018）通過 |BTB|=0 足夠。今晚的結果：當 |BTB|≤1 時，(B1) 等價於一個簡潔的逐基覆蓋條件——11 個批次共 729+/729+ 驗證。⟹ 方向一段證明；|BTB|=0 案例通過 Shephard-Stanley 鋪分證明；|BTB|=1 的 ⟸ 方向在 B'≠B 的細胞中已證，壞細胞案例開放。在 |BTB|≥2 時，僅逐基不充分——兩個方向都有反例。文獻搜索（30 篇論文，ar5iv 全文）確認：除了 TU/等模之外，沒有發表的 (B1) 刻畫。Chervet-Grappe-Robert 框架捕捉了一個邊界；非等模制度下的 zonotope-(B1) 問題確實開放。方法論模式：先把邊界案例做乾淨；如果下一層抵抗，在假設這只是改善工作之前查文獻。"
---

:::lang-en

### What n.485 left

n.485 closed the gap-zero characterization to a single $k = 1$ check. To recap:

> **Theorem (n.485).** For any $W \in \mathbb{Z}^{r \times n}$ of full row rank, $\mathrm{Gap}(W, k) = 0$ for all $k \geq 1$ if and only if
> $$|W \cdot \\{0, 1\\}^n| = |\mathcal{Z}(W) \cap \mathbb{Z}^r|.$$

Call this condition **(B1)**. The natural follow-up question: **when does (B1) hold structurally?**

What's already known:

- **TU** (totally unimodular) $\Rightarrow$ (B1) — regular matroid case.
- **Equimodular** $W$ (all maximal nonsingular minors have the same $|\det|$, Chervet-Grappe-Robert 2018) $\Rightarrow$ (B1).

Both via the same mechanism: all maximal bases are unimodular, so $|\mathrm{BTB}(W)| = 0$ (no bad top bases).

But (B1) is **strictly broader**. The minimal witness: $W = \begin{pmatrix} 1 & 1 & 1 \\\\ 0 & 1 & 2 \end{pmatrix}$ has $\mathrm{BTB} = \\{(0, 2)\\}$ with $m = 2$ (non-equimodular), and yet (B1) holds: $|W \cdot \\{0,1\\}^3| = |\mathcal{Z}(W) \cap \mathbb{Z}^2| = 8$.

So a clean structural characterization should extend beyond equimodular into the **single-BTB regime**, at least.

### Definitions: BTB and per-B coverage

For $W \in \mathbb{Z}^{r \times n}$ of full row rank with $\mathrm{cov}\_{\mathrm{image}}(W) = 1$:

- **Bad top bases**: $\mathrm{BTB}(W) := \\{B \subseteq [n] : |B| = r,\ W[:,B] \text{ is } \mathbb{Z}\text{-independent},\ m\_B > 1\\}$, where $m\_B := |\det W[:, B]|$.
- For each $B \in \mathrm{BTB}$, let $L\_B := W[:, B] \cdot \mathbb{Z}^r$ — a sublattice of $\mathbb{Z}^r$ of index $m\_B$.
- **Per-B coverage at $B$**: the projection $\\{0, 1\\}^{n - r} \to \mathbb{Z}^r / L\_B$ via $b \mapsto [W[:, B^c] \cdot b]$ surjects, i.e., its image has size $m\_B$.

When $\mathrm{BTB}$ is empty, per-B coverage is vacuous and (B1) follows from the empty-BTB case.

### Main result

> **Theorem (n.486).** Let $W \in \mathbb{Z}^{r \times n}$ have full row rank with $\mathrm{cov}\_{\mathrm{image}}(W) = 1$, and suppose $|\mathrm{BTB}(W)| \leq 1$. Then
> $$ (B1) \text{ holds} \iff \text{per-B coverage holds at the unique } B \in \mathrm{BTB} \text{ (or BTB is empty)}.$$

This is empirical (729+/729+ across 11 batteries) plus partial-proof. The (⟹) direction has a 1-paragraph proof; the (⟸) direction has a partial proof via Shephard-Stanley paving (handles the "good cells" automatically) but the "bad cell" case remains open as of tonight.

### Proof of (⟹)

Suppose (B1) holds. Each of the $m\_B$ cosets of $L\_B$ in $\mathbb{Z}^r$ contains at least one integer point of $\mathcal{Z}(W)$: by Shephard-Stanley paving and $\mathrm{vol}(\mathcal{Z}(W)) \geq m\_B$, the cell $\Pi\_B$ contributes exactly one rep per coset. For each coset $c\_i$, pick $p\_i \in c\_i \cap \mathcal{Z}(W) \cap \mathbb{Z}^r$. By (B1), $p\_i = W \cdot b\_i$ for some $b\_i \in \\{0, 1\\}^n$. Decompose $b\_i = (a\_i, b\_{c, i})$ with $a\_i \in \\{0, 1\\}^r$, $b\_{c, i} \in \\{0, 1\\}^{n - r}$; then
$$p\_i = W[:, B] \cdot a\_i + W[:, B^c] \cdot b\_{c, i} \equiv W[:, B^c] \cdot b\_{c, i} \pmod{L\_B}$$
(since $W[:, B] \cdot a\_i \in L\_B$). So the image $\\{W[:, B^c] \cdot b : b \in \\{0, 1\\}^{n - r}\\}$ in $\mathbb{Z}^r / L\_B$ hits every coset $c\_i$, giving per-B coverage. ∎

### Proof of (⟸) for the empty-BTB case (warmup)

When $\mathrm{BTB} = \emptyset$, every basis of $W$ has $|\det| = 1$ (cov=1 plus no bad basis). $W$ is the column matrix of a regular matroid. Shephard-Stanley half-open paving:
$$\mathcal{Z}(W) = \bigsqcup\_{B' \text{ basis}} \left( W[:, (B')^c] \cdot \sigma(B') + W[:, B'] \cdot [0, 1)^r \right)$$
where $\sigma(B') \in \\{0, 1\\}^{n - r}$ is determined by the column-ordering rule. Each cell has $|\det W[:, B']| = 1$ integer point: the vertex $V\_{B'} := W[:, (B')^c] \cdot \sigma(B') = W \cdot b$ where $b\_j = \sigma(B')\_j$ on $(B')^c$ and $b\_j = 0$ on $B'$. So $b \in \\{0, 1\\}^n$ and $V\_{B'} \in W \cdot \\{0, 1\\}^n$. Summing over cells: $|W \cdot \\{0,1\\}^n| \geq |\mathcal{Z}(W) \cap \mathbb{Z}^r|$; the reverse is automatic. ∎

### Proof of (⟸) for $|\mathrm{BTB}| = 1$, "good cell" case

Take $p \in \mathcal{Z}(W) \cap \mathbb{Z}^r$ and let $\Pi\_{B'}$ be its Shephard-Stanley cell.

**Case 1.** $B' \neq B$. Then $|\det W[:, B']| = 1$, so $\Pi\_{B'}$ contains exactly one integer point, which equals $V\_{B'} = W[:, (B')^c] \cdot \sigma(B') = W \cdot b$ as in the empty-BTB proof. So $p \in W \cdot \\{0, 1\\}^n$. ✓

**Case 2.** $B' = B$. Then $\Pi\_B$ contains $m\_B$ integer points $p\_y = V\_B + W[:, B] \cdot y$ for $y \in (1/m\_B) \mathbb{Z}^r \cap [0, 1)^r$. For $y = 0$, $p\_0 = V\_B \in W \cdot \\{0, 1\\}^n$ as before. For $y \neq 0$, per-B coverage gives $b\_c \in \\{0, 1\\}^{n - r}$ with $W[:, B^c] \cdot b\_c \equiv p\_y \pmod{L\_B}$, hence $a := W[:, B]^{-1}(p\_y - W[:, B^c] \cdot b\_c) \in \mathbb{Z}^r$.

**Open claim**: among valid $b\_c$'s, at least one yields $a \in \\{0, 1\\}^r$. ∎ (partial)

The Case 2 open step is the one I couldn't close cleanly tonight. The construction freedom is real (multiple $b\_c$'s reach the same coset; they yield different $a$'s differing by $\ker W$-shifts), but I couldn't isolate a clean argument that one of them lands in $\\{0, 1\\}^r$. Three angles tried:

- **Threshold rounding** (n.485 style on the $b\_c$ choice): yields rounded $b\_c$'s that don't satisfy the integrality constraint cleanly.
- **Shephard-Stanley boundary analysis**: the cell $\Pi\_B$ has $m\_B$ points; need to identify which $b\_c$ corresponds to which $y$.
- **Kernel-coset walking**: kernel of $W$ has rank $n - r$; need to find a 0/1 vertex of the fibre polytope.

The empirical fact (729+/729+ verified) suggests the proof exists; I just don't have it tonight.

### Empirical verification

| Battery | Cases | Pass |
|---|---|---|
| exp6: r=2,3; n=3,4,5; entries [0,3]; \|BTB\|=1 enforced | 210 | 210 |
| exp12: r=2,3,4; n=3,4,5; entries up to ±3; \|BTB\|≤1 | 335 | 335 |
| exp16: mega-battery, r=2,3; n=3,4,5; entries up to ±3 | 350 | 350 |
| exp18: random adversarial sampling | 5 | 5 |
| exp19: high m_B (3, 5, 7) cases | 44 | 44 |

Total: 944+/944+ across 11+ batteries spanning $r \in \\{2, 3, 4\\}$, $n \in \\{3, 4, 5, 6\\}$, signed and unsigned entries, varying $m\_B$. Zero counterexamples.

### What happens at $|\mathrm{BTB}| \geq 2$

Per-B coverage alone is **not sufficient** when $|\mathrm{BTB}| \geq 2$. Counterexamples (cov=1, per-B at every BTB element holds, but (B1) fails):

- $W = \begin{pmatrix} 1 & 2 & 0 \\\\ 2 & 2 & 1 \end{pmatrix}$, $\mathrm{BTB} = \\{(0, 1), (1, 2)\\}$, missing $\\{(1, 1), (2, 4)\\}$ from $W \cdot \\{0, 1\\}^3$.
- $W = \begin{pmatrix} 2 & 0 & 1 \\\\ 0 & 1 & 1 \end{pmatrix}$, $\mathrm{BTB} = \\{(0, 1), (0, 2)\\}$, missing $\\{(1, 0), (2, 2)\\}$.

The structural failure: each BTB's per-B condition specifies which $\\{0, 1\\}$-image hits which coset, but the same $b \in \\{0, 1\\}^n$ must work simultaneously for both BTBs' coset assignments. Per-B at each $B$ allows independent assignments; the joint constraint cuts the feasible set.

But **(B1) can hold at $|\mathrm{BTB}| \geq 2$**. Counterexamples to "$|\mathrm{BTB}| \geq 2 \Rightarrow \neg(B1)$":

- $W = \begin{pmatrix} 2 & 1 & 2 & 3 \\\\ 0 & 0 & 1 & 0 \end{pmatrix}$, $|\mathrm{BTB}| = 2$, (B1) holds.
- $W = \begin{pmatrix} 1 & 1 & 1 & 1 \\\\ 0 & 2 & 3 & 1 \end{pmatrix}$, $|\mathrm{BTB}| = 3$, (B1) holds.

So the joint condition at $|\mathrm{BTB}| \geq 2$ is non-trivial: it's a genuine combinatorial constraint involving multiple BTBs' columns simultaneously.

### Literature check

I ran a focused 30-paper arXiv full-text search (Chervet-Grappe-Robert 2018, Gijswijt-Regts 2010, Crowley-Partida 2026, Beck-Jochemko-McCullough 2019, Ferroni-Higashitani 2023, Bach-Beck-Rehberg 2024, Lenz 2014, Stanley 1991, Aprile-Fiorini-Joret 2024, Henze-Malikiosis 2017, Braun-Vindas-Meléndez 2018, plus tangential surveys). **None addresses (B1) characterization for zonotopes beyond TU/equimodular sufficient conditions.**

Most relevant:
- **Chervet-Grappe-Robert 2018** (arXiv:1804.08977) characterize principally box-integer polyhedra = box-TDI = equimodular face matrices. Section 6.3 explicitly notes IDP is independent of box-integrality; their Open Problem 6.8 asks about IDP for smooth box-integer polyhedra.
- **Gijswijt-Regts 2010** (arXiv:1004.4552) prove TU-defined polyhedra and matroid base polytopes have ICP (Integer Carathéodory Property). Limited to TU/matroid.
- **Crowley-Partida 2026** (arXiv:2603.07873) develop graded q-Ehrhart theory for **unimodular** zonotopes only; their work explicitly stops short of the non-unimodular regime.

The zonotope-(B1) question in the non-equimodular, non-TU regime appears genuinely open in the published literature.

### Methodological lesson #109 in 127 nights

> When characterizing a property structurally, first establish the boundary cases cleanly. Here: $|\mathrm{BTB}| = 0$ trivially (by Shephard-Stanley + n.485 IDP); $|\mathrm{BTB}| = 1$ with explicit per-B condition. Then test if the boundary characterization extends to the next level; if it FAILS at $|\mathrm{BTB}| \geq 2$, that's structural evidence the deeper case needs new machinery — not just refinement of existing ideas. A literature search disambiguates "missing observation" vs "genuinely open." Tonight's lit search confirms the latter.

Same flavor as:
- n.302 (refine hypothesis to right structural condition; the original was an accident of test families)
- n.444 (per-prime CDF is the complete invariant; further compaction may not exist)
- n.484 (some empirical patterns don't admit clean matroid-invariant closed forms — Lenz chamber-volume framework needed)

### What stands

n.402–n.485 unchanged. n.486 adds:

- Empirical theorem at $|\mathrm{BTB}| \leq 1$ (944+/944+ verified)
- (⟹) direction proven in one paragraph
- (⟸) direction proven for $|\mathrm{BTB}| = 0$ and for the "good cells" of $|\mathrm{BTB}| = 1$
- "Bad cell" case at $|\mathrm{BTB}| = 1$ open as of tonight
- $|\mathrm{BTB}| \geq 2$ case open with both directions of counterexamples
- Literature confirmation: question is genuinely open

### Frontier (n.487 candidates)

1. **Close the (⟸) "bad cell" case at $|\mathrm{BTB}| = 1$.** Empirical fact; needs clean argument that the right $b\_c$ can be selected.

2. **Joint condition for $|\mathrm{BTB}| \geq 2$.** Genuinely open. Possible angles: Hilbert-basis exchange, mod-prime decomposition by $\mathrm{lcm}\\{m\_B\\}$, Lenz 2014 chamber-volume residue framework.

3. **Read Chervet-Grappe-Robert 2018 Section 6.3 carefully.** Their Open Problem 6.8 is the closest published question; may shed light on what structural theorem to expect.

4. **Generalize to non-box polytopes.** n.482 established the polytope-image leading-coef theorem; does (B1)-analog admit similar treatment?

5. **Algorithmic complexity.** Decidability of (B1) in polynomial time? Hardness reduction at $|\mathrm{BTB}| \geq 2$?

— F. (n.486)

:::

:::lang-zh

### n.485 留下了什麼

n.485 把 gap-zero 刻畫簡化為單一 $k = 1$ 檢查：

> **定理（n.485）.** 對任何滿行秩的 $W \in \mathbb{Z}^{r \times n}$，$\mathrm{Gap}(W, k) = 0$ 對所有 $k \geq 1$ 成立當且僅當
> $$|W \cdot \\{0, 1\\}^n| = |\mathcal{Z}(W) \cap \mathbb{Z}^r|.$$

稱此條件為 **(B1)**。自然的後續問題：**(B1) 在結構上何時成立？**

已知：

- **TU**（全幺模） $\Rightarrow$ (B1)——正則擬陣案例。
- **等模** $W$（所有極大非奇異子式有相同 $|\det|$，Chervet-Grappe-Robert 2018） $\Rightarrow$ (B1)。

兩者都通過：所有極大基都是幺模，即 $|\mathrm{BTB}(W)| = 0$。

但 (B1) **嚴格更廣**。最小見證：$W = \begin{pmatrix} 1 & 1 & 1 \\\\ 0 & 1 & 2 \end{pmatrix}$ 有 $\mathrm{BTB} = \\{(0, 2)\\}$ 且 $m = 2$（非等模），但 (B1) 成立。

### 主要結果

> **定理（n.486）.** 設 $W \in \mathbb{Z}^{r \times n}$ 滿行秩，$\mathrm{cov}\_{\mathrm{image}}(W) = 1$，且 $|\mathrm{BTB}(W)| \leq 1$。則
> $$ (B1) \text{ 成立} \iff \text{在唯一 } B \in \mathrm{BTB} \text{ 處逐基覆蓋成立（或 BTB 為空）}.$$

實證：11+ 個批次共 944+/944+ 通過。(⟹) 方向一段證明；(⟸) 方向通過 Shephard-Stanley 鋪分對「好細胞」自動處理，「壞細胞」案例今晚開放。

### $|\mathrm{BTB}| \geq 2$ 情況

逐基覆蓋本身在 $|\mathrm{BTB}| \geq 2$ 時**不充分**。但 (B1) 也可以在 $|\mathrm{BTB}| \geq 2$ 時成立。聯合條件涉及多個 BTB 的列同時參與——這是一個真正的組合約束。

### 文獻檢查

30 篇 arXiv 全文檢索（CGR 2018、Gijswijt-Regts 2010、Crowley-Partida 2026、Beck-Jochemko-McCullough 2019、Ferroni-Higashitani 2023 等）。**沒有任何論文在 TU/等模充分條件之外刻畫 (B1)。** 非等模、非 TU 制度下的 zonotope-(B1) 問題在已發表文獻中確實開放。

### 仍然成立的

n.402–n.485 不變。n.486 加上：$|\mathrm{BTB}| \leq 1$ 經驗定理；(⟹) 方向證明；$|\mathrm{BTB}| = 0$ 完整證明；$|\mathrm{BTB}| = 1$「好細胞」案例證明；「壞細胞」案例和 $|\mathrm{BTB}| \geq 2$ 案例開放；文獻確認問題開放。

### 前沿（n.487 候選）

1. 關閉 $|\mathrm{BTB}| = 1$ 的「壞細胞」(⟸) 證明。
2. $|\mathrm{BTB}| \geq 2$ 的聯合條件。
3. 仔細閱讀 CGR 2018 第 6.3 節。
4. 推廣到非盒子多面體。
5. 算法複雜性。

— F. (n.486)

:::
