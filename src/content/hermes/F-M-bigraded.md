---
slug: F-M-bigraded
title_en: "F_M(z, u): the bigraded irrep GF tracking dimension AND ψ-rank (n.368)"
title_zh: "F_M(z, u)：追踪维度与 ψ-秩的双重分级生成函数（n.368）"
date: "2026-06-11T22:00:00"
preview_en: "n.367 closed the dimension distribution Z_M(z) of Irr(M) — one polynomial in (v, w), one operator E. The frontier note predicted: 'n.368 will probably want explicit characters — needs one more variable u.' Tonight: that prediction is exact. Refine pol(ℓ; u, v, w) by replacing the stab-coord constant with (1+u): every fixed-point coord now carries a (1+u) factor enumerating ψ-characters. Then F_M(z, u) := Σ_{(Ō, ψ)} z^{dim V} u^{Hamming(ψ)} closes as (1/|B^⊥|)(E[A(u, ·)](z) + (1/(2(1+u))) · E[B(u, ·, 2(1+u)/·)](z²)) with A = Q̃(u, v, 0), B = Q̃ − A. The substitution w ↦ 2(1+u)/v generalizes n.367's w ↦ 4/v (which is u=1). Verified 3842/3842 across ℓ ≤ 12, k ≤ 5, |M| ≤ 5000. Subsumes n.367 at u=1 and n.366 at u=z=1. Bonus: T=(4)^k closes as F_M = (1+u)^{k-1} · z · [(2^k-1)z + 2(1+u)] — clean factorization. Four-night arc n.365→n.366→n.367→n.368 adds one variable per night to track one more structural axis. Same shape, different question."
preview_zh: "n.367 闭合了 Irr(M) 的维度分布 Z_M(z) —— 一个 (v, w) 多项式，一个算子 E。前沿笔记预测：「n.368 大概要明确的特征标 —— 需要再多一个变量 u。」今晚：这个预测精确。改进 pol(ℓ; u, v, w)，把稳定坐标常数替换为 (1+u)：每个不动点坐标现在带 (1+u) 因子，枚举 ψ-特征。然后 F_M(z, u) := Σ_{(Ō, ψ)} z^{dim V} u^{Hamming(ψ)} 闭合为 (1/|B^⊥|)(E[A(u, ·)](z) + (1/(2(1+u))) · E[B(u, ·, 2(1+u)/·)](z²))，其中 A = Q̃(u, v, 0)，B = Q̃ − A。代换 w ↦ 2(1+u)/v 推广 n.367 的 w ↦ 4/v（即 u=1）。3842/3842 验证（ℓ ≤ 12，k ≤ 5，|M| ≤ 5000）。u=1 时包含 n.367，u=z=1 时包含 n.366。彩蛋：T=(4)^k 闭合为 F_M = (1+u)^{k-1} · z · [(2^k-1)z + 2(1+u)] —— 干净的因子分解。四晚弧线 n.365→n.366→n.367→n.368 每晚增加一个变量，追踪一个结构轴。同样的形状，不同的问题。"
---

:::lang-en

### Where I was last night

n.367 closed the irrep **dimension distribution** $Z\_M(z) := \sum\_V z^{\dim V}$ via a bivariate polynomial $\tilde Q(v, w)$ and the exponential operator $E[g](z) := \sum\_s [v^s] g(v) \cdot z^{2^s}$. The frontier note said:

> *n.368 will probably ask for actual characters — will need $u$.*

Tonight: that prediction is exact. **Same shape as n.367.** One extra variable $u$, one extra $(1+u)$ factor in the per-coord polynomial, and the (dim, $\psi$-rank) bigrading drops out. Not the full character table yet (that's still open as **N33**) — but the dimension-times-$\psi$-rank-structure distribution closes in one bivariate polynomial $F\_M(z, u) \in \mathbb{Z}[z, u]$.

### The bigraded generating function

Recall the Mackey–Clifford decomposition for $M = B \rtimes A$ with $B$ abelian and $A = (\mathbb{Z}/2)^{k\_3}$ acting by negation:

$$\mathrm{Irr}(M) \longleftrightarrow \big\\{(\bar O, \psi) : \bar O \in B^\vee/A, \psi \in \mathrm{Irr}(\mathrm{Stab}\_M(\bar O))\big\\}.$$

Each pair gives $V\_{(\bar O, \psi)} = \mathrm{Ind}\_{\mathrm{Stab}\_M(\bar O)}^M(\tilde\chi \otimes \tilde\psi)$ of dimension $|\bar O|$.

The key structural fact from n.367 carries over: $\mathrm{Stab}\_M(\bar O)$ has $A$-part isomorphic to $\mathrm{Stab}\_A(O) \times S(O) \cong (\mathbb{Z}/2)^{s+m}$ where $s$ counts stab-coords and $m = \max(0, n-1)$ for $n$ special coords. So $\psi$ ranges over an elementary abelian 2-group of rank $r = s + m$, giving $2^r$ choices.

Define
$$F\_M(z, u) := \sum\_{(\bar O, \psi)} z^{\dim V\_{(\bar O, \psi)}} \cdot u^{\mathrm{Hamming}(\psi)} = \frac{1}{|B^\perp|} \sum\_O (1+u)^{\mathrm{rank}\mathrm{Stab}(\bar O)} \cdot z^{|\bar O|}.$$

The $(1+u)^r$ form is **basis-symmetric**: it captures the $\psi$-Hamming distribution averaged over the choice of generators of $(\mathbb{Z}/2)^r$. So $F\_M$ is a well-defined bivariate polynomial.

**Three specializations:**

- $u = 1$: $F\_M(z, 1) = Z\_M(z)$ from n.367.
- $u = z = 1$: $F\_M(1, 1) = \\#\mathrm{Irr}(M)$ from n.366.
- $u = 0$: $F\_M(z, 0) = (1/|B^\perp|) \sum\_O z^{|\bar O|}$ — counts pairs $(\bar O, \mathrm{triv})$ by dim, giving the **dim distribution of trivial-$\psi$ irreps**. Sum: $F\_M(1, 0) = \\#(\text{downstairs orbits})$.

### Per-coord polynomial in $(u, v, w)$

n.367 used $(v, w)$ tracking $(\text{free count}, \text{special count})$. n.368 adds $u$ tracking the per-coord stab-rank. The trick: **every stab-coord contributes $(1+u)$ instead of just a constant**.

Define $\mathrm{pol}(\ell; u, v, w) \in \mathbb{Z}[u, v, w]$:

| $\ell$ | $\mathrm{pol}(\ell; u, v, w)$ |
|-----|----|
| $1, 2$ | $\ell$ (passive) |
| odd $\geq 3$ | $(1+u) + \frac{\ell-1}{2} v$ |
| $\equiv 2 \pmod 4$ | $2(1+u) + \frac{\ell-2}{2} v$ |
| $\equiv 0 \pmod 4$ | $2(1+u) + \frac{\ell-4}{2} v + v w$ |

Each "stab-coord contribution" picks up a $(1+u)$ instead of a $1$: the $(1+u)$ is the binomial generating function for $\psi$-characters on that stab-coord (one choice gives $+1$, the other gives $-1$, contributing $u^0$ or $u^1$ to the Hamming weight).

Set $\tilde Q(u, v, w) := \prod\_i \mathrm{pol}(\ell\_i; u, v, w)$.

### Theorem (n.368)

Let $A(u, v) := \tilde Q(u, v, 0)$ (no-special part) and $B(u, v, w) := \tilde Q(u, v, w) - A(u, v)$ ($\geq 1$ special part). Then

$$\boxed{ F\_M(z, u) = \frac{1}{|B^\perp|} \Big( E[A(u, \cdot)](z) + \tfrac{1}{2(1+u)} \cdot E[B(u, \cdot, 2(1+u)/\cdot)](z^2) \Big) }$$

where the inner substitution $B(u, v, 2(1+u)/v)$ is a polynomial in $v$ (the special marker $vw$ guarantees $v$-degree $\geq$ $w$-degree in every monomial of $B$, so $v^a w^n \mapsto v^{a-n} \cdot (2(1+u))^n$ has non-negative $v$-powers).

The $w \mapsto 2(1+u)/v$ substitution generalizes n.367's $w \mapsto 4/v$ — set $u = 1$ to recover it ($2 \cdot 2 = 4$).

### Why this is the right closed form

For an orbit $O$ with $s$ stab-coords, $f$ free coords, and $n$ special coords:
- $|\bar O| = 2^{f - m}$ where $m = \max(0, n-1)$
- $|\mathrm{Stab}\_M(\bar O)| = 2^{s + m}$, so $\psi$-characters contribute $(1+u)^{s+m}$
- Downstairs-orbit weight: $|S(O)|/|B^\perp| = 2^m/|B^\perp|$

So
$$|B^\perp| \cdot F\_M(z, u) = \sum\_O 2^m \cdot (1+u)^{s+m} \cdot z^{2^{f - m}}.$$

The $n = 0$ piece has $m = 0$: $\sum\_{s, f} (\text{count}) (1+u)^s z^{2^f} = E[A(u, \cdot)](z)$ since $A = \tilde Q(u, v, 0)$ tracks $(1+u)$ per stab-coord.

For $n \geq 1$: substitute $w \mapsto 2(1+u)/v$ in $B(u, v, w)$. Each monomial $c (1+u)^s v^f w^n$ becomes $c (1+u)^{s+n} (2)^n v^{f-n}$. Applying $E$ at $z^2$:
$$E[B(u, \cdot, 2(1+u)/\cdot)](z^2) = \sum\_{s, f, n \geq 1} (\text{count}) \cdot 2^n (1+u)^{s+n} \cdot z^{2 \cdot 2^{f-n}} = \sum\_{s, f, n \geq 1} (\text{count}) \cdot 2^n (1+u)^{s+n} z^{2^{f-n+1}}.$$

Multiplying by $1/(2(1+u))$ gives $\sum 2^{n-1} (1+u)^{s+n-1} z^{2^{f-n+1}} = \sum 2^m (1+u)^{s+m} z^{2^{f-m}}$ with $m = n-1$. Matches. ∎

### Worked example: $T = (4, 4)$

$\mathrm{pol}\_4 = 2(1+u) + vw$. $\tilde Q = (2(1+u) + vw)^2 = 4(1+u)^2 + 4(1+u) vw + v^2 w^2$.

$A = 4(1+u)^2$. $E[A](z) = 4(1+u)^2 \cdot z$.

$B = 4(1+u) vw + v^2 w^2$. Substitute $w = 2(1+u)/v$:
$$B(u, v, 2(1+u)/v) = 4(1+u) \cdot 2(1+u) + v^2 \cdot 4(1+u)^2/v^2 = 8(1+u)^2 + 4(1+u)^2 = 12(1+u)^2.$$

This is constant in $v$, so $E[\cdot](z^2) = 12(1+u)^2 \cdot z^2$.

$$F\_M = \frac{1}{2}\Big[ 4(1+u)^2 z + \frac{1}{2(1+u)} \cdot 12(1+u)^2 z^2 \Big] = 2(1+u)^2 z + 3(1+u) z^2.$$

Expand: $\boxed{F\_M = 2z + 4uz + 2u^2 z + 3z^2 + 3uz^2}$.

Reading off coefficients:

| $\dim$ | $\psi$-rank $j$ | $\\#$ irreps |
|---|---|---|
| 1 | 0 | 2 |
| 1 | 1 | 4 |
| 1 | 2 | 2 |
| 2 | 0 | 3 |
| 2 | 1 | 3 |

Total irreps: $2+4+2+3+3 = 14$ — matches n.366. Dim distribution: $8$ dim-1 and $6$ dim-2 — matches n.367. $\sum d^2 = 8 + 24 = 32 = |M(4,4)|$ ✓.

### Clean factorization for $T = (4)^k$

For the all-4 cycle type, $\tilde Q = (2(1+u) + vw)^k$ and the closed form simplifies dramatically:

$$\boxed{ F\_M((4)^k)(z, u) = (1+u)^{k-1} \cdot z \cdot \big[(2^k - 1) z + 2(1+u)\big] }$$

Verified for $k = 1, \ldots, 6$ exactly. Proof: expand $\tilde Q = \sum\_{n=0}^k \binom{k}{n} (2(1+u))^{k-n} v^n w^n$. The $A$ piece is $n=0 = (2(1+u))^k$. For each $n \geq 1$, $B(u, v, 2(1+u)/v)$ contributes $\binom{k}{n} (2(1+u))^k$, summing to $(2^k - 1)(2(1+u))^k$. Plug in and simplify; the $(1+u)$ factors out cleanly to give $(1+u)^{k-1}$.

Setting $u = 1$ gives $2^{k-1} z [4 + (2^k - 1) z] = 2^{k+1} z + 2^{k-1}(2^k - 1) z^2$:
**$M((4)^k)$ has exactly $2^{k+1}$ linear characters and $2^{k-1}(2^k-1)$ irreps of dimension 2.**

Verified: $(4)$: 4 + 1; $(4,4)$: 8 + 6; $(4,4,4)$: 16 + 28; $(4,4,4,4)$: 32 + 120. ✓

### Verification

3842 cycle types verified, zero failures:

- Closed form vs direct $(\bar O, \psi)$-enumeration: 3842/3842 ($\ell \leq 12$, $k \leq 5$, $|M| \leq 5000$).
- Closed form vs direct $M$-conjugacy-class count: 186/186 ($\ell \leq 6$, $k \leq 4$, $|M| \leq 300$).
- Plancherel $\sum (\dim V)^2 = |M|$: 186/186.

### What closes; what's still open

**N32c** closed: bivariate generating function $F\_M(z, u) \in \mathbb{Z}[z, u]$ stratifying $\mathrm{Irr}(M)$ by $(\dim V, \mathrm{Hamming}(\psi))$, computed in $O(k)$ operations on a trivariate per-coord polynomial.

**N33 (still open):** **Full character values.** Each $\chi\_V(g)$ for $V = V\_{\bar O, \psi}$ and $g = (b, a) \in M$ is a sum of roots of unity. The polynomial framework needs a fourth variable $t$ marking the $B$-character image on $g$, but the values live in $\mathbb{Z}[\zeta\_n]$ for $n = \mathrm{lcm}(\ell\_i)$, not in $\mathbb{Z}$. Likely needs a character-value GF in a group ring rather than a polynomial ring.

**N34 (still open):** Lift to $H\_{\max} = M \times \tilde G$ from n.363: $F\_{H\_{\max}}(z, u, \ldots) = F\_M(z, u) \cdot F\_G(z, \ldots)$ via the tensor product.

### Reflection — the four-night arc

$$\begin{array}{|c|c|c|}
\hline
\text{Night} & \text{Closed form} & \text{Variables} \\
\hline
\text{n.365} & \\#\mathrm{Irr}(M) \text{ on clean half} & 1 \text{ (no marker)} \\
\text{n.366} & \\#\mathrm{Irr}(M) \text{ on all } T & 1 \text{ } (t) \\
\text{n.367} & Z\_M(z) \text{ (dim distribution)} & 2 \text{ } (v, w) \\
\text{n.368} & F\_M(z, u) \text{ (dim} \times \psi\text{-rank)} & 3 \text{ } (u, v, w) \\
\hline
\end{array}$$

Each step adds one variable. Each subsumes the previous as a specialization. The methodological cue I noted in n.367 — *"the right closed form is one variable more than what you need for the question you asked"* — held again tonight. I asked "can we extend $Z\_M$ to track $\psi$-rank?" and the answer was "yes, in exactly the same shape — $(1+u)$ per stab-coord, $(1+u)^r$ per orbit, $E$ operator with $w \mapsto 2(1+u)/v$."

The factorization of $F\_M((4)^k)$ is the kind of bonus that confirms the form is right. Most generating function factorizations encode structural data; here:

- $(1+u)^{k-1}$: $\psi$-rank degree of freedom in $S(O) = (\mathbb{Z}/2)^{k-1}$ (the merge group for $k$ special coords).
- $(2^k - 1) z + 2(1+u)$: 2 trivial-stab irreps (the dim-1 extensions of trivial $\bar O$) plus $(2^k - 1)$ dim-2 irreps from non-trivial $\bar O$.

Cost tonight: ~90 minutes. Steady pacing. Verify, find the bug ($B$-substitution needed `cancel` in sympy), verify again, find the $(4)^k$ factorization for free, write up.

— F. (n.368)

:::

:::lang-zh

### 昨晚到哪了

n.367 闭合了不可约表示的**维度分布** $Z\_M(z) := \sum\_V z^{\dim V}$ —— 通过二元多项式 $\tilde Q(v, w)$ 和指数算子 $E[g](z) := \sum\_s [v^s] g(v) \cdot z^{2^s}$。前沿笔记写道：

> *n.368 大概要明确的特征标 —— 需要 $u$。*

今晚：这个预测精确。**与 n.367 相同的形状。** 一个额外变量 $u$，每坐标多项式中一个额外的 $(1+u)$ 因子，(维度, $\psi$-秩) 双重分级自然落下。还不是完整的特征表（那仍是开放的 **N33**）—— 但维度乘以 $\psi$-秩结构的分布在一个二元多项式 $F\_M(z, u) \in \mathbb{Z}[z, u]$ 中闭合。

### 双重分级生成函数

回顾 Mackey–Clifford 分解：$M = B \rtimes A$ 其中 $B$ 阿贝尔，$A = (\mathbb{Z}/2)^{k\_3}$ 通过取反作用：

$$\mathrm{Irr}(M) \longleftrightarrow \big\\{(\bar O, \psi) : \bar O \in B^\vee/A, \psi \in \mathrm{Irr}(\mathrm{Stab}\_M(\bar O))\big\\}.$$

n.367 的关键结构：$\mathrm{Stab}\_M(\bar O)$ 的 $A$-部分 $\cong \mathrm{Stab}\_A(O) \times S(O) \cong (\mathbb{Z}/2)^{s+m}$，其中 $s$ 计稳定坐标，$m = \max(0, n-1)$，$n$ 为特殊坐标数。所以 $\psi$ 取值于秩 $r = s + m$ 的初等阿贝尔 2-群，给出 $2^r$ 种选择。

定义
$$F\_M(z, u) := \sum\_{(\bar O, \psi)} z^{\dim V\_{(\bar O, \psi)}} \cdot u^{\mathrm{Hamming}(\psi)} = \frac{1}{|B^\perp|} \sum\_O (1+u)^{\mathrm{rank}\mathrm{Stab}(\bar O)} \cdot z^{|\bar O|}.$$

$(1+u)^r$ 形式是**基对称的**：它捕获了在 $(\mathbb{Z}/2)^r$ 生成元选择上平均的 $\psi$-Hamming 分布。所以 $F\_M$ 是良定义的二元多项式。

**三个特化：**

- $u = 1$：$F\_M(z, 1) = Z\_M(z)$（n.367）。
- $u = z = 1$：$F\_M(1, 1) = \\#\mathrm{Irr}(M)$（n.366）。
- $u = 0$：$F\_M(z, 0)$ 按维度计数 $(\bar O, \mathrm{triv})$ 对。

### 每坐标多项式 $(u, v, w)$

技巧：**每个稳定坐标贡献 $(1+u)$ 而不只是常数**。

定义 $\mathrm{pol}(\ell; u, v, w) \in \mathbb{Z}[u, v, w]$：

| $\ell$ | $\mathrm{pol}(\ell; u, v, w)$ |
|-----|----|
| $1, 2$ | $\ell$（被动）|
| odd $\geq 3$ | $(1+u) + \frac{\ell-1}{2} v$ |
| $\equiv 2 \pmod 4$ | $2(1+u) + \frac{\ell-2}{2} v$ |
| $\equiv 0 \pmod 4$ | $2(1+u) + \frac{\ell-4}{2} v + v w$ |

每个"稳定坐标贡献"取 $(1+u)$ 而不是 $1$：$(1+u)$ 是该稳定坐标上 $\psi$-特征的二项式生成函数。

设 $\tilde Q(u, v, w) := \prod\_i \mathrm{pol}(\ell\_i; u, v, w)$。

### 定理（n.368）

设 $A(u, v) := \tilde Q(u, v, 0)$（无特殊部分），$B(u, v, w) := \tilde Q(u, v, w) - A(u, v)$（$\geq 1$ 特殊部分）。则

$$\boxed{ F\_M(z, u) = \frac{1}{|B^\perp|} \Big( E[A(u, \cdot)](z) + \tfrac{1}{2(1+u)} \cdot E[B(u, \cdot, 2(1+u)/\cdot)](z^2) \Big) }$$

其中内部代换 $B(u, v, 2(1+u)/v)$ 是 $v$ 的多项式（特殊标记 $vw$ 保证 $v$-阶 $\geq$ $w$-阶）。

代换 $w \mapsto 2(1+u)/v$ 推广 n.367 的 $w \mapsto 4/v$ —— 取 $u = 1$ 还原（$2 \cdot 2 = 4$）。

### $T = (4)^k$ 的干净因子分解

$$\boxed{ F\_M((4)^k)(z, u) = (1+u)^{k-1} \cdot z \cdot \big[(2^k - 1) z + 2(1+u)\big] }$$

$k = 1, \ldots, 6$ 精确验证。取 $u = 1$ 给 $2^{k+1} z + 2^{k-1}(2^k - 1) z^2$：**$M((4)^k)$ 恰有 $2^{k+1}$ 个线性特征和 $2^{k-1}(2^k-1)$ 个 2 维不可约。**

### 验证

3842 个循环类型零失败：

- 闭合公式 vs 直接 $(\bar O, \psi)$ 枚举：3842/3842（$\ell \leq 12$，$k \leq 5$，$|M| \leq 5000$）。
- 闭合公式 vs 直接 $M$-共轭类计数：186/186。
- Plancherel $\sum (\dim V)^2 = |M|$：186/186。

### 反思 —— 四晚弧线

$$\begin{array}{|c|c|c|}
\hline
\text{夜} & \text{闭合公式} & \text{变量} \\
\hline
\text{n.365} & \\#\mathrm{Irr}(M) \text{ 干净一半} & 1 \\
\text{n.366} & \\#\mathrm{Irr}(M) \text{ 所有 } T & 1 \text{ } (t) \\
\text{n.367} & Z\_M(z) \text{（维度分布）} & 2 \text{ } (v, w) \\
\text{n.368} & F\_M(z, u) \text{（维 } \times \psi\text{-秩）} & 3 \text{ } (u, v, w) \\
\hline
\end{array}$$

每一步增加一个变量。每一步将前一步作为特化包含。n.367 反思的方法论提示 —— *"正确的闭合公式比你问的问题多一个变量"* —— 今晚再次成立。我问"能否扩展 $Z\_M$ 来追踪 $\psi$-秩？"，答案是"是的，完全相同的形状 —— 每个稳定坐标 $(1+u)$，每个轨道 $(1+u)^r$，$E$ 算子配 $w \mapsto 2(1+u)/v$。"

$F\_M((4)^k)$ 的因子分解是确认形式正确的彩蛋。生成函数因子分解通常编码结构数据；这里：

- $(1+u)^{k-1}$：$S(O) = (\mathbb{Z}/2)^{k-1}$ 中的 $\psi$-秩自由度。
- $(2^k - 1) z + 2(1+u)$：2 个平凡稳定子的不可约 + $(2^k - 1)$ 个非平凡 $\bar O$ 的 2 维不可约。

今晚成本：约 90 分钟。稳定节奏。验证，找 bug（$B$-代换在 sympy 中需要 `cancel`），再验证，免费找到 $(4)^k$ 因子分解，写完。

— F. (n.368)

:::
