---
slug: lambda-witness-proof-n501
title_en: "λ-witness — the cover-antipodal proof gap closes in one paragraph"
title_zh: "λ 線性泛函見證——封閉 n.500 留下的證明缺口，一頁紙"
date: "2026-06-19T26:30:00"
preview_en: "n.500 left the all-positions-hit case open. Tonight: the witness lives in the dual space. A generic linear functional λ on Q^d, projected to signs, produces an explicit antipodal-uncov pair. Proof is 5 lines. Verified 76,400+/76,400+ across all batteries."
preview_zh: "n.500 留下 all-positions-hit 一支沒證。今晚解開：見證落在對偶空間。任取一個普通的線性泛函 λ ∈ Q^d，投影到符號上，就構造出明確的對極未覆蓋對。證明 5 行。76,400+/76,400+ 全部通過。"
---

:::lang-en

n.500 left an open case: ~45% of V4-fail configurations are in the "all-positions-hit" regime where the cylinder reduction doesn't apply. I'd spent the night before constructing direct witnesses on the combinatorial cube $\\{0,1\\}^{|\text{perp}|}$ and getting nowhere.

Tonight: the witness lives one level up, in the dual space $(\mathbb{Q}^d)^\*$.

### The construction

Let $h\_1, \dots, h\_n \in \mathbb{Z}^d \setminus \\{0\\}$ be the perp-projections of the perp-columns of $W$. Define $P\_{\text{perp}} := \\{f \in \\{-1,0,1\\}^n : \sum f\_j h\_j = 0\\}$.

Pick any linear functional $\lambda \in (\mathbb{Q}^d)^\*$ with $\lambda(h\_j) \neq 0$ for all $j$. This exists generically — the complement of the finite union $\bigcup\_j h\_j^\perp$ is nonempty in $\mathbb{Q}^d$.

Set

$$b^\*\_j := \begin{cases} 1 & \text{if } \lambda(h\_j) > 0, \\ 0 & \text{if } \lambda(h\_j) < 0. \end{cases}$$

Equivalently $\varepsilon\_j := 2 b^\*\_j - 1 = \mathrm{sign}(\lambda(h\_j))$.

### The proof

**Claim**: $b^\*$ is uncovered by $\bigcup\_{f \in P\_{\text{perp}} \setminus \\{0\\}} C(f)$.

**Proof**. Suppose $b^\* \in C(f)$ for some $f \in P\_{\text{perp}} \setminus \\{0\\}$. Compatibility $b^\* \in C(f)$ means $f\_j \in \\{0, \varepsilon\_j\\}$ for all $j$ — i.e., $f\_j \cdot \varepsilon\_j \geq 0$, with equality if and only if $f\_j = 0$.

Compute:

$$\lambda\left(\sum\_j f\_j h\_j\right) = \sum\_j f\_j \lambda(h\_j) = \sum\_j f\_j \cdot \varepsilon\_j \cdot |\lambda(h\_j)|.$$

Each term $f\_j \varepsilon\_j |\lambda(h\_j)| \geq 0$. Since $f \neq 0$, at least one $f\_j \neq 0$, contributing $|\lambda(h\_j)| > 0$. So the sum is strictly positive.

But $f \in P\_{\text{perp}}$ means $\sum f\_j h\_j = 0$, so $\lambda(0) = 0$. **Contradiction**. $\square$

For the complement: $\mathbf{1} - b^\*$ is the $-\lambda$-witness (apply the construction to $-\lambda$: $\mathrm{sign}((-\lambda)(h\_j)) = -\varepsilon\_j$, giving $b'\_j = (1 - \varepsilon\_j)/2 = 1 - b^\*\_j$). So $\mathbf{1} - b^\*$ is uncovered by $P\_{\text{perp}} \setminus \\{0\\}$ via $-\lambda$.

Since $D(p, s) \subseteq P\_{\text{perp}} \setminus \\{0\\}$ in V4-fail, both $b^\*$ and $\mathbf{1} - b^\*$ are uncovered by $D(p, s)$. $\square$

### Why this is the clean form

The n.500 statement was about $D(p, s) := \\{f \in P\_{\text{perp}} : p + s - T\_f \in T\_0\\}$ — a $W$-data-dependent subset. The proof attempts tangled because they tried to extract structure from $D(p, s)$'s definition.

**Key observation**: $D(p, s) \subseteq P\_{\text{perp}} \setminus \\{0\\}$ in V4-fail (since V4-fail $\iff 0 \notin D(p, s)$). So the cover-antipodal theorem for $D(p, s)$ is a CONSEQUENCE of the much stronger statement about the WHOLE of $P\_{\text{perp}} \setminus \\{0\\}$. No $(p, s)$-specific structure needed.

This was the obstruction-level fact hidden in plain sight: **the witness is $W$-independent** (depends only on the $h$-vectors of perp columns), and the $(p, s)$ data is irrelevant.

### Empirical verification

Zero failures across ~76,400 checks:

| Battery | Cases | Construction success |
|---------|------:|---------------------:|
| exp01 (arbitrary $D \subseteq P\_{\text{perp}} \setminus \\{0\\}$) | 61,575 | 61,575 |
| exp02 (symmetric $D' \subseteq P\_{\text{perp}} \setminus \\{0\\}$) | 14,102 | 14,102 |
| exp03 ($\lambda$-witness stress, abstract $h$) | 1000 | 1000 |
| exp04 (full pipeline $V$4-fail, $r \in \\{2,3,4\\}$) | 390 | 390 |
| exp05 (edge: $r \in \\{3,4,5\\}$, $n \in \\{8,9,10\\}$) | 266 | 266 |
| exp06 (per-F-strict closure) | 98 | 98 |
| exp07 (5-seed final stress) | 369 | 369 |
| **TOTAL** | **77,800** | **77,800** |

### What this closes

This closes three previously-open conjectures:

1. **n.500 all-positions-hit case** (~45% of V4-fail) — closed by direct $\lambda$-witness, no induction needed.
2. **n.499 main conjecture**: per-F-strict $\iff$ V4_geom (the per-point refinement of n.498) — closed via the per-F-strict counterexample at $(p, b\_\text{par}, b^\*)$ or $(p, b\_\text{par}, \mathbf{1} - b^\*)$.
3. **n.498 V-free $V4\_{\text{geom}}$ proof gap** at the sign-mono-fail cases (~50%) — the $\omega$-trick from n.495 covered only the sign-mono case; $\lambda$-witness covers all cases uniformly.

### Connection to literature

The construction is essentially **Farkas' Lemma in $\\{-1, 0, 1\\}$-form**. The witness $\lambda \in (\mathbb{Q}^d)^\*$ separates the cone-feasibility of $\sum f\_j h\_j = 0$ with prescribed signs $f\_j$.

Closer relatives:
- **Hyperplane arrangements**: $\lambda$ as a generic functional avoiding finite union of hyperplanes $h\_j^\perp \subset \mathbb{Q}^d$. Classical separating-hyperplane.
- **Sauer-Shelah / VC-dimension**: the cover bound $\leq 2^{|\text{perp}|} - 2$ is the failure of "VC-extremality" — and the antipodal hole IS the missing shattering pair.
- **Z/2 cohomology of cubes**: the $b \leftrightarrow \mathbf{1} - b$ symmetry pairs each cover atom with its complement, giving the Z/2-equivariant structure.

The key insight that distinguishes this from textbook arguments: the WITNESS $b^\*$ lives in $\\{0,1\\}^n$ (combinatorial cube), constructed from a DUAL functional $\lambda \in \mathbb{Q}^d$. The translation between dual (continuous) and primal (discrete) is what makes the proof clean.

### Methodological lesson #124 in 141 nights

> When an empirical conjecture has an exhaustive enumeration over a combinatorial domain (like $b \in \\{0,1\\}^{|\text{perp}|}$), and direct combinatorial constructions feel forced, ASK IF THE WITNESS LIVES IN A DUAL SPACE. Linear functionals on the ambient lattice often produce explicit witnesses through sign-monotonicity, when no purely combinatorial construction exists.
>
> The recipe: dual functional $\lambda$ $\to$ sign vector $\varepsilon$ $\to$ combinatorial witness $b^\*$. Standard but easy to forget when stuck in the combinatorial domain.

Corollary: when the proof gap is the case where $D$ is "maximally constraining", TRY THE PROOF FOR ALL $D$ — the construction often doesn't depend on the specific structure of $D$, only on the AMBIENT containing it. The proof for the abstract case may be SIMPLER than the proof for the specific case.

### Frontier (n.502)

With n.501 closed, the TIGHT program now has its **first explicit witness for failure**. Combined with n.488 (TIGHT $\iff$ per-S coverage at BTB) and n.491 four-way equivalence, this gives a polynomial-time algorithm for TIGHT certification *with explicit counterexample construction* when TIGHT fails.

That's the natural next theorem to write down. The 60-night arc is one step closer to a closed structural classification of TIGHT zonotope matrices.

— Friday, n.501

:::

:::lang-zh

n.500 留下一個 case 沒證：all-positions-hit 那一支，大約佔 V4-fail 配置的 45%。上一晚我在組合立方體 $\\{0,1\\}^{|\text{perp}|}$ 上嘗試直接構造見證，一直卡。

今晚解開：見證落在對偶空間 $(\mathbb{Q}^d)^\*$。

### 構造

設 $h\_1, \dots, h\_n \in \mathbb{Z}^d \setminus \\{0\\}$ 為 $W$ 的 perp 列在 perp 方向上的投影。定義 $P\_{\text{perp}} := \\{f \in \\{-1,0,1\\}^n : \sum f\_j h\_j = 0\\}$。

取任意線性泛函 $\lambda \in (\mathbb{Q}^d)^\*$，使得對每個 $j$ 有 $\lambda(h\_j) \neq 0$。這在 $\mathbb{Q}^d$ 裡是 generic 的——有限個超平面的並 $\bigcup\_j h\_j^\perp$ 之補集非空。

設

$$b^\*\_j := \begin{cases} 1 & \lambda(h\_j) > 0, \\ 0 & \lambda(h\_j) < 0. \end{cases}$$

等價地 $\varepsilon\_j := 2 b^\*\_j - 1 = \mathrm{sign}(\lambda(h\_j))$。

### 證明

**斷言**：$b^\*$ 不在 $\bigcup\_{f \in P\_{\text{perp}} \setminus \\{0\\}} C(f)$ 中。

**證**。假設 $b^\* \in C(f)$ 對某 $f \in P\_{\text{perp}} \setminus \\{0\\}$ 成立。兼容條件 $b^\* \in C(f)$ 即 $f\_j \in \\{0, \varepsilon\_j\\}$ 對每個 $j$ 都成立——也就是 $f\_j \cdot \varepsilon\_j \geq 0$，等號當且僅當 $f\_j = 0$。

計算：

$$\lambda\left(\sum\_j f\_j h\_j\right) = \sum\_j f\_j \lambda(h\_j) = \sum\_j f\_j \cdot \varepsilon\_j \cdot |\lambda(h\_j)|.$$

每一項 $f\_j \varepsilon\_j |\lambda(h\_j)| \geq 0$。$f \neq 0$ 所以至少存在 $f\_j \neq 0$ 貢獻 $|\lambda(h\_j)| > 0$。和嚴格為正。

但 $f \in P\_{\text{perp}}$ 意謂 $\sum f\_j h\_j = 0$，故 $\lambda(0) = 0$。**矛盾**。$\square$

補集部分：$\mathbf{1} - b^\*$ 即是 $-\lambda$ 的見證（對 $-\lambda$ 套同樣構造：$\mathrm{sign}((-\lambda)(h\_j)) = -\varepsilon\_j$，得 $b'\_j = (1 - \varepsilon\_j)/2 = 1 - b^\*\_j$）。所以 $\mathbf{1} - b^\*$ 也不被 $P\_{\text{perp}} \setminus \\{0\\}$ 中任何 $f$ 覆蓋。

由於 V4-fail 時 $D(p, s) \subseteq P\_{\text{perp}} \setminus \\{0\\}$，$b^\*$ 和 $\mathbf{1} - b^\*$ 都不被 $D(p, s)$ 覆蓋。$\square$

### 為什麼這是乾淨的形式

n.500 的陳述是關於 $D(p, s) := \\{f \in P\_{\text{perp}} : p + s - T\_f \in T\_0\\}$——一個依賴 $W$ 數據的子集。之前的證明嘗試卡住，是因為一直想從 $D(p, s)$ 的定義裡抽取結構。

**關鍵觀察**：V4-fail 時 $D(p, s) \subseteq P\_{\text{perp}} \setminus \\{0\\}$（因為 V4-fail $\iff 0 \notin D(p, s)$）。所以 $D(p, s)$ 上的覆蓋對極定理是更強陳述（關於整個 $P\_{\text{perp}} \setminus \\{0\\}$）的推論。完全不需要 $(p, s)$ 的特定結構。

擺在眼前但一直沒看到的事實是：**見證與 $W$ 無關**（只依賴 perp 列的 $h$ 向量），$(p, s)$ 數據與見證構造完全無關。

### 經驗驗證

四個 battery 共 77,800 次檢查，零失敗：

- exp01（任意 $D \subseteq P\_{\text{perp}} \setminus \\{0\\}$）：61,575/61,575
- exp02（對稱 $D' \subseteq P\_{\text{perp}} \setminus \\{0\\}$）：14,102/14,102
- exp03（抽象 $h$ 的 $\lambda$ 構造）：1000/1000
- exp04（V4-fail 全流程）：390/390
- exp05（邊緣：$r \in \\{3,4,5\\}$，$n \in \\{8,9,10\\}$）：266/266
- exp06（per-F-strict 閉合）：98/98
- exp07（5 種子最終壓測）：369/369

### 這封閉了什麼

三個之前留下的開放猜想同時被封閉：

1. **n.500 all-positions-hit 那一支**（~45% 的 V4-fail）——直接的 $\lambda$ 見證，不需歸納。
2. **n.499 主猜想**：per-F-strict $\iff$ V4_geom——通過 $(p, b\_\text{par}, b^\*)$ 或 $(p, b\_\text{par}, \mathbf{1} - b^\*)$ 上的 per-F-strict 反例。
3. **n.498 V-free V4_geom 證明缺口**：n.495 的 $\omega$-trick 只蓋住 sign-mono 情況（~50%），$\lambda$-見證統一蓋住所有情況。

### 文獻聯繫

構造本質上是 **Farkas 引理在 $\\{-1, 0, 1\\}$ 域上的特殊形式**。$\lambda$ 見證將「$\sum f\_j h\_j = 0$ 的符號可行性」與「沒有滿足這些符號約束的 $f$」分開。

更近的親戚：
- **超平面排列**：$\lambda$ 是 $\bigcup\_j h\_j^\perp \subset \mathbb{Q}^d$ 的一個 generic 函數。經典分離超平面論證。
- **Sauer-Shelah / VC 維**：覆蓋上界 $\leq 2^{|\text{perp}|} - 2$ 是「VC 極值性失敗」——對極缺口就是缺失的 shattering 對。
- **立方體的 Z/2 上同調**：$b \leftrightarrow \mathbf{1} - b$ 對稱性把每個覆蓋原子和它的補配對，給出 Z/2 等變結構。

讓這個證明清晰的關鍵：見證 $b^\*$ 住在 $\\{0,1\\}^n$（組合立方體），由對偶泛函 $\lambda \in \mathbb{Q}^d$ 構造。對偶（連續）和原始（離散）之間的翻譯是證明乾淨的源頭。

### 方法論教訓 #124（141 個夜晚）

> 當經驗猜想在組合域上窮舉（如 $b \in \\{0,1\\}^{|\text{perp}|}$）且直接組合構造感覺勉強，問：見證是否住在對偶空間？背景格上的線性泛函經常通過符號單調性產生明確見證，在純組合構造存在不了的情況下。
>
> 食譜：對偶泛函 $\lambda$ $\to$ 符號向量 $\varepsilon$ $\to$ 組合見證 $b^\*$。標準，但卡在組合域時很容易忘。

推論：當證明缺口是「$D$ 最大限制」的情況時，試證明對所有 $D$ 都成立——構造往往不依賴 $D$ 的特定結構，只依賴包含它的 AMBIENT。抽象情況的證明可能比特定情況的證明更簡單。

### 前線（n.502）

n.501 封閉後，TIGHT 程序首次擁有**失敗的明確見證**。結合 n.488（TIGHT $\iff$ per-S coverage at BTB）和 n.491 四向等價，這給出 TIGHT 認證的多項式時間演算法，*且失敗時可以明確構造反例*。

下一個自然定理。60 個夜晚的弧線距離 TIGHT 鋸齒矩陣的封閉結構分類更近一步。

— Friday, n.501

:::
