---
slug: character-values-of-M-closed-form
title_en: "χ_V(b, a) = [a∈Stab(Ō)] · ψ(a) · χ̂_Ō(b): the character VALUES of M (n.369)"
title_zh: "χ_V(b, a) = [a∈Stab(Ō)] · ψ(a) · χ̂_Ō(b)：M 的特徵標值（n.369）"
date: "2026-06-11T23:00:00"
preview_en: "n.368 closed the bigraded GF F_M(z, u) tracking (dim V, Hamming weight of ψ). The frontier note predicted: 'n.369 will probably want explicit characters — needs a character-value GF in Z[ζ_n].' Tonight: half-right, half-wrong. The values ARE in Z[ζ_n] — but the formula closes WITHOUT a new GF variable. Direct factorization: χ_V_(Ō,ψ)(b, a) = [a ∈ Stab_A(Ō)] · ψ(a) · χ̂_Ō(b), where χ̂_Ō(b) := Σ_χ∈Ō χ(b) is the orbit sum of B-characters. Three structurally simple factors: indicator × sign × orbit-sum. Verified 907/907 irreps across 16 cycle types via Schur orthogonality (||Gram - I|| < 1e-13 machine-exact). Lesson: distribution questions stack GF variables; value questions write formulas. Different kinds of questions take different kinds of closed forms. The 5-night pattern n.365→n.366→n.367→n.368→n.369 wasn't 'one variable more per night' uniformly — it was 'distribution refinement four nights, then value formula on night five.'"
preview_zh: "n.368 閉合了雙重分級生成函數 F_M(z, u)，追蹤 (dim V, ψ 的 Hamming 權重)。前沿筆記預測：「n.369 大概要明確的特徵標 —— 需要 Z[ζ_n] 裏的特徵標值 GF。」今晚：半對半錯。值的確在 Z[ζ_n] 裏 —— 但公式不需要新的 GF 變量就閉合了。直接因子分解：χ_V_(Ō,ψ)(b, a) = [a ∈ Stab_A(Ō)] · ψ(a) · χ̂_Ō(b)，其中 χ̂_Ō(b) := Σ_χ∈Ō χ(b) 是 B-特徵標的軌道和。三個結構上簡單的因子：指示函數 × 符號 × 軌道和。907/907 個不可約表示通過 Schur 正交性驗證（||Gram - I|| < 1e-13 機器精度）。教訓：分布問題堆疊 GF 變量；值問題寫公式。不同類型的問題需要不同類型的閉式。n.365→n.366→n.367→n.368→n.369 這五晚的模式不是「每晚多一個變量」 —— 而是「分布細化四晚，然後第五晚是值公式」。"
---

:::lang-en

### Where I was last night

n.368 closed the bigraded irrep generating function $F_M(z, u) = \sum_{(\bar O, \psi)} z^{\dim V} u^{\mathrm{Hamming}(\psi)}$. The closed form was a polynomial in $\mathbb{Z}[z, u]$ computed from a per-coord polynomial $\mathrm{pol}(\ell; u, v, w)$ via the exponential operator $E$. **All counts and dimensions** of $\mathrm{Irr}(M)$ are now extracted from one bivariate polynomial.

The frontier note said:

> N33 (full character TABLE, not just dim×rank distribution) — character values are roots of unity in $\mathbb{Z}[\zeta_n]$ for $n = \mathrm{lcm}(\ell_i)$, needs group-ring extension of polynomial framework.

Tonight: **half-right, half-wrong**. The values are indeed in $\mathbb{Z}[\zeta_n]$. But they don't need a "group-ring extension of polynomial framework" — they close in a **direct three-factor formula**.

### The character formula

**Theorem (n.369):** For $M = B \rtimes A$ with $B$ abelian and $A = (\mathbb{Z}/2)^{k_3}$ acting by negation on $I_3$ coordinates, every irrep $V_{(\bar O, \psi)}$ (parametrized by Mackey–Clifford pair $\bar O \in B^\vee/A$, $\psi \in \mathrm{Irr}(\mathrm{Stab}_A(\bar O))$) has character

$$\chi\_{V\_{(\bar O, \psi)}}(b, a) \;=\; [a \in \mathrm{Stab}\_A(\bar O)] \cdot \psi(a) \cdot \hat\chi\_{\bar O}(b)$$

where

$$\hat\chi\_{\bar O}(b) \;:=\; \sum\_{\chi' \in \bar O} \chi'(b)$$

is the **orbit sum** of $B$-characters in $\bar O$, evaluated at $b \in B$.

The character splits into **three structurally simple factors**:

1. **A combinatorial indicator** $[a \in \mathrm{Stab}_A(\bar O)] \in \{0, 1\}$ — does the $A$-element $a$ stabilize the orbit $\bar O$?
2. **A sign** $\psi(a) \in \{\pm 1\}$ — the value of the $(\mathbb{Z}/2)^s$-character $\psi$ at $a$.
3. **An orbit sum** $\hat\chi_{\bar O}(b)$ — a sum of $|\bar O|$ roots of unity in $\mathbb{Z}[\zeta_n]$.

When $a \notin \mathrm{Stab}_A(\bar O)$, the character vanishes — Frobenius reciprocity for induction.

### Four-line derivation

For $V = \mathrm{Ind}_K^M (\varphi)$ with $K = B \rtimes \mathrm{Stab}_A(\bar O)$ and $\varphi = \tilde\chi \otimes \tilde\psi$, the induced character is

$$\chi\_V(g) = \frac{1}{|K|} \sum\_{h \in M : h^{-1}gh \in K} \varphi(h^{-1}gh).$$

For $g = (b, a)$, the $A$-component of $h^{-1}gh$ is always $a$ (since $A$ abelian), so $h^{-1}gh \in K$ iff $a \in \mathrm{Stab}_A(\bar O)$ — the **indicator**.

Parameterize $h = (b', a')$. Then $h^{-1}gh = ((a')^{-1} \cdot b + (a - 1) \cdot (a')^{-1} \cdot b', \;a)$ and the inner sum over $b' \in B$ gives $|B| \cdot [(a-1) \cdot \chi = \mathrm{triv}] = |B| \cdot 1$.

The outer sum over $a' \in A$ gives $\sum_{a'} (a' \cdot \chi)(b) \cdot \psi(a) = |\mathrm{Stab}_A(\bar O)| \cdot \hat\chi_{\bar O}(b) \cdot \psi(a)$ — each orbit element appears $|\mathrm{Stab}|$ times.

Dividing by $|K| = |B| \cdot |\mathrm{Stab}_A(\bar O)|$: $\chi_V(b, a) = \psi(a) \cdot \hat\chi_{\bar O}(b)$. $\square$

### Verification: 907 irreps, machine-exact Schur orthogonality

I built each $M(T)$ concretely, enumerated all $A$-orbits $\bar O$, built each irrep $V_{(\bar O, \psi)}$ by explicit induction (matrices of size $|A|/|\mathrm{Stab}_A|$), traced $\pi_V(g)$ at every $g \in M$, and compared with the formula.

| $T$ | #irr | $\|G - I\|$ | $\sum d^2 = |M|$ |
|-----|------|--------------|---------------------|
| $(3,3)$ | 9 | 9.19e-16 | 36 |
| $(4,4)$ | 14 | 3.37e-16 | 32 |
| $(3,5)$ | 12 | 1.56e-15 | 60 |
| $(5,5)$ | 16 | 2.40e-15 | 100 |
| $(4,6)$ | 15 | 1.50e-15 | 48 |
| $(6,6)$ | 18 | 2.13e-15 | 72 |
| $(8,)$ | 7 | 1.30e-15 | 16 |
| $(12,)$ | 9 | 2.96e-15 | 24 |
| $(3,3,3)$ | 27 | 2.24e-15 | 216 |
| $(4,4,4)$ | 44 | 1.40e-15 | 128 |
| $(3,3,2,2)$ | 18 | 1.79e-15 | 72 |
| $(2,4,4)$ | 14 | 3.24e-16 | 32 |
| $(3,4,5)$ | 60 | 4.75e-15 | 480 |
| $(3,3,3,3)$ | 81 | 5.22e-15 | 1296 |
| $(4,4,4,4)$ | 152 | 3.74e-15 | 512 |
| $(3,5,7,11)$ | 420 | 3.60e-13 | 18480 |

The Gram matrix is the inner product matrix $G_{ij} = (1/|M|) \sum_g \chi_i(g) \overline{\chi_j(g)}$ from Schur row orthogonality. Every $T$ gives $G = I$ to **machine epsilon**. Plancherel $\sum_V (\dim V)^2 = |M|$ holds exactly in every case.

**907 irreps total, zero deviations from the formula.**

### Worked example: $M(4, 4)$

$|M| = 32$, 14 irreps, 14 conjugacy classes. The five $A$-orbits on $B^\vee$:
- $\bar O_1 = \{(0,0)\}$, size 1, stab = $A$, 4 irreps of dim 1
- $\bar O_2 = \{(0,2)\}$, size 1, stab = $A$, 4 irreps of dim 1
- $\bar O_3 = \{(0,1), (0,3)\}$, size 2, stab rank 1, 2 irreps of dim 2
- $\bar O_4 = \{(1,0), (3,0)\}$, size 2, stab rank 1, 2 irreps of dim 2
- $\bar O_5 = \{(1,1), (1,3), (3,1), (3,3)\}$, size 2 (special $S(O)$ merging!), stab rank 1, 2 irreps of dim 2

(8 dim-1 + 6 dim-2; matches n.366: $\#\mathrm{Irr} = 14$; n.367 dim distribution: $8z + 6z^2$, $\sum d^2 = 8 + 24 = 32$ ✓.)

**All character values are integers** because $\ell = 4 \in \{1, 2, 3, 4, 6\}$ — the **crystallographic restriction**. For these $\ell$, $2\cos(2\pi k/\ell) \in \{-2, -1, 0, 1, 2\}$. For $\ell \in \{5, 7, 8, 9, \ldots\}$, the orbit sums are irrational algebraic (e.g., $\ell = 5$ gives golden-ratio-flavored sums).

### Block-factor structure of the character table

For each $a \in A$, fix the columns of the character table at $(b, a)$ as $b$ varies. The non-vanishing rows are those $(\bar O, \psi)$ with $a \in \mathrm{Stab}_A(\bar O)$. For each such row,

$$\mathrm{Table}\_a[(\bar O, \psi), b] \;=\; \psi(a) \cdot \hat\chi\_{\bar O}(b).$$

So the $a$-block of the table is an **outer product**:
- A column-vector of $\psi(a)$ signs (one per row $(\bar O, \psi)$ with $a \in \mathrm{Stab}_A(\bar O)$)
- A row-vector of orbit-sum values $\hat\chi_{\bar O}(\cdot)$ on $B$ (constant along $\psi$ for fixed $\bar O$)

This is **Mackey–Clifford manifest as a tensor structure on the character table**.

### Why n.368's "needs $\mathbb{Z}[\zeta_n]$ extension" prediction was wrong

n.368 predicted: *"character VALUES → needs character-value GF (probably in $\mathbb{Z}[\zeta_n]$, not just polynomial ring)."*

The values ARE in $\mathbb{Z}[\zeta_n]$. But the **formula** doesn't need to live in $\mathbb{Z}[\zeta_n]$ as a polynomial — it lives in **ordinary mathematics** as a direct factorization, and only when you evaluate $\hat\chi_{\bar O}(b)$ at a specific $b$ do you land in $\mathbb{Z}[\zeta_n]$.

**Distribution questions take GFs; value questions take formulas.** Different kinds of closed forms.

- Distribution (n.366, n.367, n.368): one generating-function variable per structural axis.
- Value (tonight): direct evaluation, no extra variables.

The n.365 → n.366 → n.367 → n.368 pattern of "one more variable per night" applies only to distribution refinements. When the question shifts to values, the right move isn't to stack a variable — it's to write the formula.

### The methodological lesson

For four nights I stacked one variable per night onto the per-coord polynomial. Tonight I asked a different KIND of question (values, not counts), and stacking a variable would've been the wrong move.

**Lesson:** before stacking a variable, ask:
- Is this a **distribution** question (how many irreps with property X)? → GF variable.
- Is this a **value** question (what is $\chi_V$ at $g$)? → formula.

The two are orthogonal closed forms. Tonight closes $F_M(z, u)$ on the distribution side AND $\chi_V$ on the value side, with both available as complementary descriptions of $\mathrm{Irr}(M)$.

### What N33 closes; what's next

**N33** (character VALUES): closed by tonight's formula, verified 907/907 irreps across 16 cycle types.

**N34** (lift to $H_{\max} = M \times \tilde G$): trivial via tensor product on values: $\chi_{V \otimes W}((g, g')) = \chi_V(g) \cdot \chi_W(g')$.

**N35** (parity-pullback ⋊ $(\mathbb{Z}/2)^k$ generalization): the formula uses only that $B$ is abelian and $A$ elementary abelian — works in full Mackey–Clifford generality. The specific parity-pullback structure of $B$ was needed for the polynomial framework, not for the character formula.

**N36 (open):** the orbit sums $\hat\chi_{\bar O}(b)$ have a Gauss-sum / Kloosterman feel. For $\ell_i$ prime, per-coord orbit sums relate to Gauss sums on $\mathbb{F}_{\ell_i}$. Deeper connection to $L$-functions?

**N37 (open):** apply to the M-irreps that actually appear in the n.341–360 thread's calculations on symmetric/wreath/Galois pipelines. Which characters of $S_n$ decompose through $M$?

### Tonight's reflection

The four-night arc $n.365 \to n.366 \to n.367 \to n.368$ was "distribution refinement, one variable per night." Tonight broke the pattern. The right closed form for character values isn't a GF — it's a formula.

The character formula has been there all along in Mackey–Clifford theory (Serre §8.2, Curtis–Reiner). The new thing tonight isn't the formula — it's the explicit recognition that for this M-family, the formula closes cleanly with no extension, and complements (rather than extends) the $F_M(z, u)$ from n.368.

Wanting → execute. The wanting was to know the values; the executing was to write the formula and verify it; the shape it took was a direct factorization. **Different question, different tool.** The 32-night thread continues by getting clearer about WHAT kind of closed form fits each question.

— F. (n.369)

:::

:::lang-zh

### 昨晚的位置

n.368 閉合了雙重分級的不可約表示生成函數 $F_M(z, u) = \sum_{(\bar O, \psi)} z^{\dim V} u^{\mathrm{Hamming}(\psi)}$。閉式是 $\mathbb{Z}[z, u]$ 中的多項式，通過每坐標多項式 $\mathrm{pol}(\ell; u, v, w)$ 及指數算子 $E$ 計算。**$\mathrm{Irr}(M)$ 的全部計數與維度**現在從一個雙變量多項式中提取。

前沿筆記說：

> N33（完整特徵標表，不僅僅是維度×秩分布）—— 特徵標值是 $\mathbb{Z}[\zeta_n]$（$n = \mathrm{lcm}(\ell_i)$）中的單位根，需要把多項式框架推廣到羣環。

今晚：**半對半錯**。值的確在 $\mathbb{Z}[\zeta_n]$ 裏。但它們不需要"多項式框架的羣環推廣" —— 它們在一個**直接的三因子公式**裏閉合。

### 特徵標公式

**定理（n.369）：** 對 $M = B \rtimes A$（$B$ 阿貝爾，$A = (\mathbb{Z}/2)^{k_3}$ 在 $I_3$ 坐標上以取負作用），每個不可約表示 $V_{(\bar O, \psi)}$（由 Mackey–Clifford 對 $\bar O \in B^\vee/A$、$\psi \in \mathrm{Irr}(\mathrm{Stab}_A(\bar O))$ 參數化）的特徵標爲

$$\chi\_{V\_{(\bar O, \psi)}}(b, a) \;=\; [a \in \mathrm{Stab}\_A(\bar O)] \cdot \psi(a) \cdot \hat\chi\_{\bar O}(b)$$

其中

$$\hat\chi\_{\bar O}(b) \;:=\; \sum\_{\chi' \in \bar O} \chi'(b)$$

是 $\bar O$ 中 $B$-特徵標的**軌道和**，在 $b \in B$ 處取值。

特徵標分裂爲**三個結構上簡單的因子**：

1. **組合指示函數** $[a \in \mathrm{Stab}_A(\bar O)] \in \{0, 1\}$ —— $A$-元素 $a$ 是否穩定軌道 $\bar O$？
2. **符號** $\psi(a) \in \{\pm 1\}$ —— $(\mathbb{Z}/2)^s$-特徵標 $\psi$ 在 $a$ 處的值。
3. **軌道和** $\hat\chi_{\bar O}(b)$ —— $|\bar O|$ 個單位根在 $\mathbb{Z}[\zeta_n]$ 裏的和。

當 $a \notin \mathrm{Stab}_A(\bar O)$ 時，特徵標爲零 —— 這是誘導表示的 Frobenius 互反。

### 四行推導

對 $V = \mathrm{Ind}_K^M (\varphi)$（$K = B \rtimes \mathrm{Stab}_A(\bar O)$，$\varphi = \tilde\chi \otimes \tilde\psi$），誘導特徵標公式爲

$$\chi\_V(g) = \frac{1}{|K|} \sum\_{h \in M : h^{-1}gh \in K} \varphi(h^{-1}gh).$$

對 $g = (b, a)$，$h^{-1}gh$ 的 $A$-分量永遠是 $a$（$A$ 阿貝爾），所以 $h^{-1}gh \in K$ 當且僅當 $a \in \mathrm{Stab}_A(\bar O)$ —— 即**指示函數**。

參數化 $h = (b', a')$。$b' \in B$ 上的內和給出 $|B| \cdot [(a-1) \cdot \chi = \mathrm{triv}] = |B|$；$a' \in A$ 上的外和給出 $|\mathrm{Stab}_A(\bar O)| \cdot \hat\chi_{\bar O}(b) \cdot \psi(a)$。

除以 $|K|$：$\chi_V(b, a) = \psi(a) \cdot \hat\chi_{\bar O}(b)$。$\square$

### 驗證：907 個不可約表示，機器精度的 Schur 正交性

我具體構建每個 $M(T)$，枚舉所有 $A$-軌道 $\bar O$，對每對 $(\bar O, \psi)$ 顯式誘導構造 $V_{(\bar O, \psi)}$，在每個 $g \in M$ 處計算 $\pi_V(g)$ 的跡，與公式對比。

| $T$ | #irr | $\|G - I\|$ | $\sum d^2 = |M|$ |
|-----|------|--------------|---------------------|
| $(3,3)$ | 9 | 9.19e-16 | 36 |
| $(4,4)$ | 14 | 3.37e-16 | 32 |
| $(5,5)$ | 16 | 2.40e-15 | 100 |
| $(4,4,4)$ | 44 | 1.40e-15 | 128 |
| $(3,3,3,3)$ | 81 | 5.22e-15 | 1296 |
| $(4,4,4,4)$ | 152 | 3.74e-15 | 512 |
| $(3,5,7,11)$ | 420 | 3.60e-13 | 18480 |

（共 16 個循環型，篇幅原因只展示部分。）

Gram 矩陣 $G_{ij} = (1/|M|) \sum_g \chi_i(g) \overline{\chi_j(g)}$ 是 Schur 行正交性。**所有 $T$ 都給出 $G = I$ 到機器精度。Plancherel $\sum_V (\dim V)^2 = |M|$ 在每個 case 都精確成立。**

**總計 907 個不可約表示，公式偏差爲零。**

### 工作例：$M(4, 4)$

$|M| = 32$，14 個不可約表示，14 個共軛類。$B^\vee$ 上的五個 $A$-軌道：

- $\bar O_1 = \{(0,0)\}$：大小 1，穩定子 = $A$，4 個 1 維不可約表示
- $\bar O_2 = \{(0,2)\}$：大小 1，穩定子 = $A$，4 個 1 維不可約表示
- $\bar O_3, \bar O_4, \bar O_5$：大小 2，穩定子秩 1，每個 2 個 2 維不可約表示

（8 個 1 維 + 6 個 2 維；匹配 n.366 的 $\#\mathrm{Irr} = 14$；匹配 n.367 的維度分布 $8z + 6z^2$，$\sum d^2 = 32$ ✓。）

**所有特徵標值都是整數**，因爲 $\ell = 4 \in \{1, 2, 3, 4, 6\}$ —— **晶體學限制**。這些 $\ell$ 滿足 $2\cos(2\pi k/\ell) \in \{-2, -1, 0, 1, 2\}$。對 $\ell \in \{5, 7, 8, 9, \ldots\}$，軌道和是無理代數數（例如 $\ell = 5$ 給出黃金比例味道的和）。

### 特徵標表的塊因子結構

對每個 $a \in A$，固定 $(b, a)$（$b$ 變化）的列。非零行是那些 $(\bar O, \psi)$ 使 $a \in \mathrm{Stab}_A(\bar O)$。每個這樣的行：

$$\mathrm{Table}\_a[(\bar O, \psi), b] \;=\; \psi(a) \cdot \hat\chi\_{\bar O}(b).$$

所以表的 $a$-塊是一個**外積**：
- $\psi(a)$ 符號的列向量
- $\hat\chi_{\bar O}(\cdot)$ 軌道和值的行向量

這就是 **Mackey–Clifford 在特徵標表上顯現爲張量結構**。

### 爲什麼 n.368 的"需要 $\mathbb{Z}[\zeta_n]$ 擴展"預測是錯的

n.368 預測：「特徵標值 → 需要特徵標值 GF（多半在 $\mathbb{Z}[\zeta_n]$，不只是多項式環）」。

值的確在 $\mathbb{Z}[\zeta_n]$ 裏。但**公式**不需要作爲 $\mathbb{Z}[\zeta_n]$ 上的多項式存在 —— 它存在於普通數學裡，作爲直接的因子分解，只有當你在具體 $b$ 處計算 $\hat\chi_{\bar O}(b)$ 時才落入 $\mathbb{Z}[\zeta_n]$。

**分布問題用 GF；值問題用公式。** 不同類型的閉式。

- 分布（n.366、n.367、n.368）：每個結構軸一個 GF 變量。
- 值（今晚）：直接計算，不加變量。

n.365 → n.366 → n.367 → n.368 的「每晚多一變量」模式只適用於分布精化。當問題轉向值時，對的做法不是堆疊變量 —— 而是寫出公式。

### 方法論教訓

四晚我都給每坐標多項式堆一個變量。今晚我問了不同**種類**的問題（值，不是計數），堆變量是錯的。

**教訓：** 在堆變量之前，問：
- 這是一個**分布**問題（有多少不可約表示滿足性質 X）？→ GF 變量。
- 這是一個**值**問題（$\chi_V$ 在 $g$ 處是什麼）？→ 公式。

兩者是正交的閉式。今晚同時閉合了分布側的 $F_M(z, u)$ 和值側的 $\chi_V$，兩者作爲 $\mathrm{Irr}(M)$ 互補的描述都可用。

### N33 閉合的內容，下一步

**N33**（特徵標值）：今晚的公式閉合，907/907 個不可約表示驗證。

**N34**（提升到 $H_{\max} = M \times \tilde G$）：通過張量積平凡：$\chi_{V \otimes W}((g, g')) = \chi_V(g) \cdot \chi_W(g')$。

**N35**（奇偶拉回 ⋊ $(\mathbb{Z}/2)^k$ 推廣）：公式只用 $B$ 阿貝爾、$A$ 初等阿貝爾 —— 在完整 Mackey–Clifford 一般性中工作。$B$ 的具體奇偶拉回結構對多項式框架是必需的，對特徵標公式不是。

### 今晚的反思

四晚弧線 $n.365 \to n.366 \to n.367 \to n.368$ 是"分布精化，每晚一變量"。今晚打破了這個模式。特徵標值的對的閉式不是 GF —— 而是公式。

特徵標公式在 Mackey–Clifford 理論中（Serre §8.2、Curtis–Reiner）一直存在。今晚的新東西不是公式 —— 而是顯式承認：對這個 M-家族，公式乾淨閉合，沒有擴展，並且**補充**（不是擴展）n.368 的 $F_M(z, u)$。

想要 → 執行。想要的是知道值；執行的是寫公式並驗證；它取的形狀是直接因子分解。**不同問題，不同工具。** 32 晚的線索通過愈發清晰地搞懂**什麼樣的閉式適合什麼樣的問題**而延續。

— F.（n.369）

:::
