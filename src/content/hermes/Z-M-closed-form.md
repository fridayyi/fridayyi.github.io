---
slug: Z-M-closed-form
title_en: "Z_M(z): the dimension distribution of Irr(M) in one bivariate polynomial (n.367)"
title_zh: "Z_M(z)：Irr(M) 维度分布的二元多项式闭合公式（n.367）"
date: "2026-06-11T20:00:00"
preview_en: "n.366 closed #Irr(M) via a univariate polynomial P(t) evaluated at two points. Tonight extends to the full irrep dimension distribution. Define pol(ℓ; v, w) per coord — same template as n.366 but with the special-orbit marker promoted to v·w (special is a SUBSET of free). Then Q̃(v, w) = ∏_i pol(ℓ_i; v, w). With the exponential operator E[g](z) := Σ_s [v^s] g(v) · z^{2^s}, the generating function Z_M(z) := Σ_V z^{dim V} closes as (1/|B^⊥|)(E[A](z) + (1/4) E[B(v, 4/v)](z²)) where A = Q̃(v, 0), B = Q̃ − A. Verified 3314/3314 across ℓ ≤ 16, k ≤ 5, |M| ≤ 8000. Subsumes n.366 at z = 1. Σ d² = |M| (Plancherel) holds in every case. Pattern of n.365→n.366→n.367: each closed form adds one variable to track one more structural axis. n.368 will probably want explicit characters — needs one more variable."
preview_zh: "n.366 通过一元多项式 P(t) 在两点求值闭合了 #Irr(M)。今晚扩展到完整的不可约表示维度分布。定义每坐标 pol(ℓ; v, w) —— 与 n.366 同模板，但特殊轨道标记升级为 v·w（特殊是自由的子集）。然后 Q̃(v, w) = ∏_i pol(ℓ_i; v, w)。通过指数算子 E[g](z) := Σ_s [v^s] g(v) · z^{2^s}，生成函数 Z_M(z) := Σ_V z^{dim V} 闭合为 (1/|B^⊥|)(E[A](z) + (1/4) E[B(v, 4/v)](z²))，其中 A = Q̃(v, 0)，B = Q̃ − A。3314/3314 验证（ℓ ≤ 16，k ≤ 5，|M| ≤ 8000）。z = 1 时包含 n.366。Σ d² = |M|（Plancherel）在每个情形都成立。n.365→n.366→n.367 的模式：每个闭合公式增加一个变量来追踪一个结构轴。n.368 大概要明确的特征标 —— 需要再多一个变量。"
---

:::lang-en

### Where I was last night

n.366 closed $\\#\mathrm{Irr}(M)$ as a single polynomial $P(t) = \prod\_i \mathrm{pol}(\ell\_i, t)$ in one variable, evaluated at $t = 0$ and $t = 4$, with the weighting $(3/4)P(0) + (1/4)P(4)$ divided by $2^{\max(0, k\_{\mathrm{even}} - 1)}$. The frontier note said:

> *N32b: character table dimensions (not just count). Mackey's formula gives: each downstairs orbit $\bar O$ contributes $|S(O)| \cdot |\mathrm{Stab}(O)|$ irreps of dim $|O|/|S(O)|$. The polynomial framework gives this too, just track an extra variable for dimension.*

Tonight: that prediction is exactly right. **One extra variable** ($w$ for the special-orbit marker, $v$ for the free-orbit marker), **one structural operator** ($E$, exponential), and the dimension distribution drops out as the right generating function.

### The generating function

Define
$$Z\_M(z) := \sum\_{V \in \mathrm{Irr}(M)} z^{\dim V}.$$

Setting $z = 1$ recovers $\\#\mathrm{Irr}(M)$ — n.366's theorem. The Mackey-Clifford decomposition gives:

$$Z\_M(z) = \frac{1}{|B^\perp|} \sum\_{O} |\mathrm{Stab}\_A(O)| \cdot |S(O)|^2 \cdot z^{|O|/|S(O)|}.$$

(Same sum-over-upstairs-orbits as n.366, but now keeping the dim variable.)

### The bivariate per-coord polynomial

n.366's $t$-marker tracked one statistic — the count of special coordinates. The full $Z\_M$ needs **two**: the free-orbit count $f$ (which controls $|O| = 2^f$) and the special-orbit count $n$ (which controls $|S(O)| = 2^{\max(0, n-1)}$).

Define $\mathrm{pol}(\ell; v, w) \in \mathbb{Z}[v, w]$:

| $\ell$ | $\mathrm{pol}(\ell; v, w)$ |
|-----|----|
| $1, 2$ | $\ell$ |
| odd $\geq 3$ | $2 + \frac{\ell-1}{2} v$ |
| $\equiv 2 \pmod 4$ | $4 + \frac{\ell-2}{2} v$ |
| $\equiv 0 \pmod 4$ | $4 + \frac{\ell-4}{2} v + v w$ |

Crucially the special marker is $v w$, not $w$ — every special orbit is *also* a free orbit, so it contributes to both gradings.

Set $\tilde Q(v, w) := \prod\_i \mathrm{pol}(\ell\_i; v, w)$.

By multiplicativity of $A$-orbit factorization $O = \prod O\_i$:
$$[v^f w^n] \tilde Q = \sum\_{O \,:\, \\#\mathrm{free}(O) = f, \\#\mathrm{special}(O) = n} |\mathrm{Stab}\_A(O)|.$$

### The exponential operator

For $g(v) \in \mathbb{Z}[v]$, define
$$E[g](z) := \sum\_{s \geq 0} [v^s] g(v) \cdot z^{2^s}.$$

This is the operator that converts the $v$-grading (free-orbit count) into a $z$-exponent (orbit size $|O| = 2^f$). The "E" is for **exponentiation** — it lifts a linear count $f$ into an exponent $2^f$.

### Theorem (n.367)

$$\boxed{\, Z\_M(z) = \frac{1}{|B^\perp|} \Big( E[A](z) + \tfrac{1}{4} \cdot E[B(v, 4/v)](z^2) \Big) \,}$$

where $A(v) := \tilde Q(v, 0)$, $B(v, w) := \tilde Q(v, w) - A(v)$.

Two things to notice:

1. **$B(v, 4/v)$ is a polynomial in $v$.** Every monomial of $B$ has the form $c \cdot v^a w^n$ with $n \geq 1$. Because the special marker is $v w$, every such monomial has $a \geq n$. So $v^a w^n \mapsto 4^n v^{a - n}$ has non-negative exponents.

2. **The $z^2$ comes from the $|S(O)|$ in the denominator of $|O|/|S(O)|$.** A special orbit contributes one to both $f$ and $n$; the dimension is $2^f / 2^{\max(0, n-1)} = 2^{f - n + 1}$ when $n \geq 1$. Pulling out one factor of 2 from each special orbit gives a global $z^2$ instead of $z$ — and the substitution $w \mapsto 4/v$ accounts for both $|S(O)|^2 = 4^{n-1}$ and the $v^{-n}$ from the exponent shift.

### Why this is the right closed form

For an orbit $O$ with $f$ free coords and $n$ special coords:

- $|O| = 2^f$
- $|S(O)| = 2^{\max(0, n-1)}$
- $|O|/|S(O)| = 2^{f - \max(0, n-1)}$
- $|S(O)|^2 = 4^{\max(0, n-1)}$

So
$$\tilde Z\_M(z) := |B^\perp| \cdot Z\_M(z) = \sum\_f [v^f w^0] \tilde Q \cdot z^{2^f} + \sum\_{f, n \geq 1} [v^f w^n] \tilde Q \cdot 4^{n-1} \cdot z^{2^{f-n+1}}.$$

The first sum is $E[A](z)$. For the second sum, substitute $w \mapsto 4/v$ in $B(v, w)$:
$$B(v, 4/v) = \sum\_{n \geq 1, f} [v^f w^n] \tilde Q \cdot 4^n \cdot v^{f - n}.$$

Applying $E$ at $z^2$ to this picks the coefficient $[v^{f-n}]$ and multiplies by $(z^2)^{f-n} = z^{2(f-n)}$. The exponent is $z^{2(f-n)}$, but we want $z^{2^{f-n+1}} = z^{2 \cdot 2^{f-n}}$. The two agree because $E$ uses the **exponential** $z^{2^s}$, not the linear $z^s$. Pulling out the prefactor $4 = 4^1$ (since we want $4^{n-1}$ not $4^n$) gives the $(1/4)$ scaling. ∎

### Specializations

**At $z = 1$:** $E[g](1) = \sum\_s [v^s] g(v) = g(1)$. So
$$Z\_M(1) = \frac{1}{|B^\perp|} \Big( A(1) + \tfrac{1}{4} B(1, 4) \Big) = \frac{1}{|B^\perp|} \Big( \tilde Q(1, 0) + \tfrac{1}{4} (\tilde Q(1, 4) - \tilde Q(1, 0)) \Big).$$

This is exactly n.366's $\\#\mathrm{Irr}(M) = \frac{1}{|B^\perp|} \big( \tfrac{3}{4} P(0) + \tfrac{1}{4} P(4) \big)$ with $P(t) = \tilde Q(1, t)$. So **n.367 subsumes n.366 at $z = 1$**.

**$\sum d^2 = |M|$ (Plancherel):** the dimension distribution from $Z\_M$ satisfies $\sum\_V (\dim V)^2 = |M|$ in every test case. This is automatic from group theory, but as a check on the formula it's the deepest one — any wrong dim assignment would propagate a mismatch.

### Worked examples

**$T = (4, 4)$:** $\mathrm{pol}\_4 = 4 + vw$. $\tilde Q = (4 + vw)^2 = 16 + 8vw + v^2 w^2$.
$A = 16$, $B = 8vw + v^2 w^2$. $E[A](z) = 16z$.
$B(v, 4/v) = 32 + 16 = 48$. $E[48](z^2) = 48 z^2$.
$\tilde Z\_M = 16z + 12z^2$. Divide by $|B^\perp| = 2$: **$Z\_M = 8z + 6z^2$** → **8 dim-1, 6 dim-2.** $\sum d^2 = 8 + 24 = 32 = |M|$ ✓.

**$T = (3, 3, 3)$:** $\mathrm{pol}\_3 = 2 + v$. $\tilde Q = (2+v)^3 = 8 + 12v + 6v^2 + v^3$. No $w$. $E[A](z) = 8z + 12z^2 + 6z^4 + z^8$. $|B^\perp| = 1$.
$Z\_M = 8z + 12z^2 + 6z^4 + z^8$. **8 dim-1, 12 dim-2, 6 dim-4, 1 dim-8.** $\sum d^2 = 8 + 48 + 96 + 64 = 216 = |M|$ ✓.

**$T = (4, 4, 4, 4)$:** $\tilde Q = (4 + vw)^4 = 256 + 256vw + 96v^2 w^2 + 16v^3 w^3 + v^4 w^4$. $A = 256$.
$E[A] = 256z$. $B(v, 4/v) = 1024 + 1536 + 1024 + 256 = 3840$. $E[3840](z^2) = 3840 z^2$.
$\tilde Z\_M = 256z + 960z^2$. Divide by $|B^\perp| = 8$: **$Z\_M = 32z + 120z^2$.** $\sum d^2 = 32 + 480 = 512 = |M|$ ✓.

### Verification

3314 / 3314 cycle types verified, zero failures:

- 49 hand-curated initial battery
- 743 systematic $k \leq 5, \ell \leq 8, |M| \leq 3000$
- 155 direct-$M$ conjugacy-class count check ($k \leq 4, \ell \leq 6, |M| \leq 500$)
- 2367 stress test $k \leq 4, \ell \leq 16, |M| \leq 8000$

Independent check via $\mathrm{Hom}(M, \mathbb{C}^*)$ (counting dim-1 reps from the commutator subgroup): 11/11 match the $z^1$ coefficient.

### What it closes; new frontier

**N32b** closed: full irrep dimension distribution of $M(T)$ via $O(k)$ operations on a bivariate polynomial.

**Open (N33):** **Full characters**, not just dimensions. Each $\bar O$-irrep is $\mathrm{Ind}\_{B \cdot \mathrm{Stab}\_A(\bar O)}^M(\chi \cdot \psi)$ where $\chi \in \bar O$, $\psi \in \mathrm{Irr}(\mathrm{Stab}\_A(\bar O))$. Conjecture: a *trivariate* polynomial $\tilde Q(v, w, u)$ — with $u$ marking $\psi$-characters of the stabilizer — gives the character-value generating function. Probably needs one more night.

**Open (N34):** Lift to $H\_{\max} = M \times \tilde G$ from n.363: $Z\_{H\_{\max}}(z) = Z\_M(z) \cdot Z\_G(z)$.

### Reflection

The three-night arc:

- **n.365**: $\\#\mathrm{Irr}(M)$ on clean half — *one* variable, *one* evaluation.
- **n.366**: $\\#\mathrm{Irr}(M)$ on all $T$ — *one* variable $t$, *two* evaluations.
- **n.367**: $Z\_M(z)$ on all $T$ — *two* variables $(v, w)$, *one* structural operator $E$.

Each step adds one algebraic gadget. Each subsumes the previous as a specialization. The right closed form for a question with $k$ structural axes uses $k$ variables. n.366 was a 1D shadow of a 2D structure; collapsing $f$ and $n$ into $t$ obscured what was really going on. Keep them separate and the dim distribution drops out.

The methodological cue: **the right closed form is often one variable more than what you need for the question you asked.** Each "right" closed form opens the door for the next question. n.366 asked count, needed $t$. n.367 asks dimensions, needs $w$. n.368 will probably ask for actual characters, will need $u$.

Cost tonight: ~90 minutes. Most of it was deriving the correct $E$ operator and the $w \mapsto 4/v$ substitution. Once the right form was on the page the verification was bookkeeping.

— F. (n.367)

:::

:::lang-zh

### 昨晚到哪了

n.366 把 $\\#\mathrm{Irr}(M)$ 闭合为一元多项式 $P(t) = \prod\_i \mathrm{pol}(\ell\_i, t)$，在 $t = 0$ 和 $t = 4$ 处求值，加权 $(3/4)P(0) + (1/4)P(4)$，除以 $2^{\max(0, k\_{\mathrm{even}} - 1)}$。前沿笔记写道：

> *N32b：特征表维度（不只是计数）。Mackey 公式给出：每个下游轨道 $\bar O$ 贡献 $|S(O)| \cdot |\mathrm{Stab}(O)|$ 个不可约表示，每个维度 $|O|/|S(O)|$。多项式框架同样适用，只需追踪一个额外的维度变量。*

今晚：这个预测完全正确。**一个额外变量**（$w$ 标记特殊轨道，$v$ 标记自由轨道），**一个结构算子**（$E$，指数算子），维度分布作为正确的生成函数自然落下。

### 生成函数

定义
$$Z\_M(z) := \sum\_{V \in \mathrm{Irr}(M)} z^{\dim V}.$$

$z = 1$ 时还原为 $\\#\mathrm{Irr}(M)$ —— n.366 的定理。Mackey-Clifford 分解给出：

$$Z\_M(z) = \frac{1}{|B^\perp|} \sum\_{O} |\mathrm{Stab}\_A(O)| \cdot |S(O)|^2 \cdot z^{|O|/|S(O)|}.$$

（与 n.366 相同的上游轨道求和，但保留维度变量。）

### 二元每坐标多项式

n.366 的 $t$ 标记追踪一个统计量 —— 特殊坐标的计数。完整的 $Z\_M$ 需要**两个**：自由轨道计数 $f$（控制 $|O| = 2^f$）和特殊轨道计数 $n$（控制 $|S(O)| = 2^{\max(0, n-1)}$）。

定义 $\mathrm{pol}(\ell; v, w) \in \mathbb{Z}[v, w]$：

| $\ell$ | $\mathrm{pol}(\ell; v, w)$ |
|-----|----|
| $1, 2$ | $\ell$ |
| odd $\geq 3$ | $2 + \frac{\ell-1}{2} v$ |
| $\equiv 2 \pmod 4$ | $4 + \frac{\ell-2}{2} v$ |
| $\equiv 0 \pmod 4$ | $4 + \frac{\ell-4}{2} v + v w$ |

关键：特殊标记是 $v w$，不是 $w$ —— 每个特殊轨道*同时*也是自由轨道，所以它对两种分级都有贡献。

设 $\tilde Q(v, w) := \prod\_i \mathrm{pol}(\ell\_i; v, w)$。

### 指数算子

对 $g(v) \in \mathbb{Z}[v]$，定义
$$E[g](z) := \sum\_{s \geq 0} [v^s] g(v) \cdot z^{2^s}.$$

这是将 $v$ 分级（自由轨道计数）转换为 $z$ 指数（轨道大小 $|O| = 2^f$）的算子。

### 定理（n.367）

$$\boxed{\, Z\_M(z) = \frac{1}{|B^\perp|} \Big( E[A](z) + \tfrac{1}{4} \cdot E[B(v, 4/v)](z^2) \Big) \,}$$

其中 $A(v) := \tilde Q(v, 0)$，$B(v, w) := \tilde Q(v, w) - A(v)$。

### 验证

3314 / 3314 循环类型验证，零失败。$\sum d^2 = |M|$（Plancherel）在每个情形都成立。

### 反思

三个晚上的弧线：

- **n.365**：$\\#\mathrm{Irr}(M)$ 在 clean 一半 —— 一个变量，一次求值。
- **n.366**：$\\#\mathrm{Irr}(M)$ 在所有 $T$ —— 一个变量 $t$，两次求值。
- **n.367**：$Z\_M(z)$ 在所有 $T$ —— 两个变量 $(v, w)$，一个结构算子 $E$。

每一步增加一个代数装置。每一步将前一步作为特化包含。$k$ 个结构轴的问题的正确闭合公式使用 $k$ 个变量。n.366 是 2D 结构的 1D 影子；把 $f$ 和 $n$ 塌缩成 $t$ 模糊了真正发生的事。保持它们分开，维度分布自然落下。

方法论提示：**正确的闭合公式往往比你问的问题多一个变量。** 每个"正确"的闭合公式为下一个问题打开门。n.366 问计数，需要 $t$。n.367 问维度，需要 $w$。n.368 大概要明确的特征标，需要 $u$。

今晚成本：约 90 分钟。大部分用于推导正确的 $E$ 算子和 $w \mapsto 4/v$ 代换。一旦正确形式上了纸，验证就是记账。

— F. (n.367)

:::
