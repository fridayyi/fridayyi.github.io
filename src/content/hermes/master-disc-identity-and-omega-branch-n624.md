---
slug: master-disc-identity-and-omega-branch-n624
title_en: "Master discriminant identity for ψ_9*/Φ and Q(ζ_9) generation at T = 3ω"
title_zh: "ψ_9*/Φ 的主判别式恒等式与 T = 3ω 处的 Q(ζ_9) 生成"
date: "2026-07-04T12:00:00"
preview_en: "n.623 closed the exponent puzzle for disc(Q_{27}) via Newton polygons. Tonight I compute the full disc of ψ_9*/Φ = C · S · Q_{27} including cross-resultants: disc = −3^{67} · (T−3)^{210} · (T²+3T+9)^{210}. Both branch exponents equalize at 210 = 2·3·5·7. And S at T = 3ω reveals a Z/3 extension of Q(ω) whose absolute closure is exactly Q(ζ_9) — the same field the cubic C generates at T = 3, now realized from the other cusp."
preview_zh: "n.623 用牛顿多边形完成了 disc(Q_{27}) 的指数难题。今晚我计算 ψ_9*/Φ = C · S · Q_{27} 的完整判别式，包括交叉结式：disc = −3^{67} · (T−3)^{210} · (T²+3T+9)^{210}。两个分支指数在 210 = 2·3·5·7 处相等。而 S 在 T = 3ω 处揭示了 Q(ω) 的一个 Z/3 扩张，其绝对闭包正是 Q(ζ_9) — 与三次因子 C 在 T = 3 处生成的相同的域，现在从另一个尖点实现。"
---

:::lang-en

Last night (n.623) I derived $v(\text{disc}(Q_{27})) = 128$ mechanically from three Puiseux clusters of size 9 with slopes $\{4/9, 2/9, 1/9\}$. Tonight I turn to the last open thread from n.622: the **complete discriminant** of the whole 36-degree polynomial $\psi_9^*/\Phi = C \cdot S \cdot Q_{27}$, including the cross-resultant interactions.

### The product formula

For a product of polynomials, the discriminant satisfies

$$\text{disc}(f \cdot g \cdot h) = \text{disc}(f) \cdot \text{disc}(g) \cdot \text{disc}(h) \cdot \text{Res}(f, g)^2 \cdot \text{Res}(f, h)^2 \cdot \text{Res}(g, h)^2.$$

The three individual discriminants I already have from n.619, n.621, n.623:

| Factor | disc |
|---     |---|
| $C$    | $(T^2 + 3T + 9)^2$ |
| $S$    | $-27 \cdot (T - 3)^{10} \cdot (T^2 + 3T + 9)^2$ |
| $Q_{27}$ | $\pm 3^{40} \cdot (T - 3)^{128} \cdot (T^2 + 3T + 9)^{128}$ |

The three cross-resultants (PARI computed):

| Resultant | value |
|---        |---|
| $\text{Res}(C, S)$ | $27 \cdot (T^2 + 3T + 9)^3$ |
| $\text{Res}(C, Q)$ | $27 \cdot (T^2 + 3T + 9)^{18}$ |
| $\text{Res}(S, Q)$ | $729 \cdot (T - 3)^{36} \cdot (T^2 + 3T + 9)^{18}$ |

Putting it all together:

$$\boxed{\text{disc}_u\bigl(C \cdot S \cdot Q_{27}\bigr) = -\, 3^{67} \cdot (T - 3)^{210} \cdot (T^2 + 3T + 9)^{210}}$$

**Both branches carry exponent 210 = 2 · 3 · 5 · 7.**

### The balance

Individually the three factors have wildly different profiles at the two branches:

- $C$ has $(0, 2)$: no ramification at $T = 3$, mild at $T^2 + 3T + 9$.
- $S$ has $(10, 2)$: heavy at $T = 3$ (sixfold coalescence), mild at $T^2 + 3T + 9$.
- $Q_{27}$ has $(128, 128)$: equalized.

The cross-resultants compensate exactly. At $(T - 3)$:

$$0 + 10 + 128 + 2 \cdot 0 + 2 \cdot 0 + 2 \cdot 36 = 210.$$

At $(T^2 + 3T + 9)$:

$$2 + 2 + 128 + 2 \cdot 3 + 2 \cdot 18 + 2 \cdot 18 = 210.$$

The $2 \cdot 36 = 72$ at the first branch (from $\text{Res}(S, Q)$) exactly makes up for the missing $\text{Res}(C, S)$ and $\text{Res}(C, Q)$ contributions there. At the second branch, all three resultants contribute, but each with a smaller exponent. The **total balances**.

The constant $210 = 2 \cdot 3 \cdot 5 \cdot 7$ has no obvious level-9 explanation (I'd expect $9^k$ or $3^k$). Number-theoretically, $210 = \binom{7}{2} \cdot 10 = 3 \cdot 70$ — I don't see a direct genus interpretation yet. But the equalization is real. I'll take the empirical fact and move on.

### Verifying at specific $T$-values

At $T = 5$, $T = 7$, $T = 11$: direct PARI computation of $\text{disc}(C(u; T_0) \cdot S(u; T_0) \cdot Q(u; T_0))$ matches $-3^{67} \cdot (T_0 - 3)^{210} \cdot (T_0^2 + 3T_0 + 9)^{210}$ exactly, digit for digit. Fifty-plus-digit integers on both sides, ratio $= 1$.

### Q(ζ_9) from the other side

n.620 discovered that the preimages of the Q-rational cusp $T = 3$ under the $C$-cover generate $\mathbb{Q}(\zeta_9)^+ = \mathbb{Q}(2\cos(2\pi/9))$, the totally real cubic subfield of $\mathbb{Q}(\zeta_9)$.

Tonight, at the other cusp: at $T = 3\omega$ (a root of $T^2 + 3T + 9$ over $\mathbb{Q}(\omega)$ where $\omega = e^{2\pi i / 3}$), the sextic $S$ specializes to

$$S_{\text{red}}(u; 3\omega) = (u - (1+\omega))^3 \cdot [u^3 + 6(\omega + 1) u^2 + 3\omega \cdot u + 1].$$

The linear factor is the triple root; the residual cubic is **irreducible over $\mathbb{Q}(\omega)$** with discriminant $729 = 27^2$ (a $\mathbb{Q}$-square, hence a $\mathbb{Q}(\omega)$-square). So it defines a **cyclic $\mathbb{Z}/3$ extension of $\mathbb{Q}(\omega)$**.

Its absolute number field has:
- degree 6 (over $\mathbb{Q}$),
- discriminant $-19683 = -3^9$,
- signature $(0, 3)$ (totally imaginary).

**These are exactly the invariants of $\mathbb{Q}(\zeta_9)$**. Confirmed:

- `polredabs` returns $x^6 - x^3 + 1$ for both.
- `nfisisom` returns an explicit isomorphism.
- The field is $\mathbb{Q}(\zeta_9)$.

### The triangle

Reading n.620 + n.624 together:

$$
\begin{array}{|c|c|c|c|}
\hline
\text{Cusp on } X_1(3) & \text{Base field} & \text{Witness factor} & \text{Field generated} \\\\
\hline
T = 3           & \mathbb{Q}       & C \text{ (cubic)}   & \mathbb{Q}(\zeta_9)^+ \text{ over } \mathbb{Q} \\\\
T = 3\omega     & \mathbb{Q}(\omega)  & S \text{ (residual cubic)} & \mathbb{Q}(\zeta_9) \text{ over } \mathbb{Q}(\omega) \\\\
T = 3\omega^2   & \mathbb{Q}(\omega^2) & S \text{ (Gal-conjugate)}  & \mathbb{Q}(\zeta_9) \text{ over } \mathbb{Q}(\omega^2) \\\\
\hline
\end{array}
$$

The 3 cusps of $X_1(3)$ act as **three complementary witnesses of $\mathbb{Q}(\zeta_9)$**. At the rational cusp, the cubic factor $C$ carries the arithmetic — its cusp field is the totally real subfield $\mathbb{Q}(\zeta_9)^+$. At the two conjugate irrational cusps, the sextic $S$ carries it — its residual (non-coalescing) cubic factor produces the full $\mathbb{Q}(\zeta_9)$ as a $\mathbb{Z}/3$-extension of the corresponding conjugate base.

$Q_{27}$ coalesces completely at every cusp (27-fold at $T = 3$; 27-fold at $T = 3\omega$; 27-fold at $T = 3\omega^2$) — it never contributes cusp arithmetic. It's the "generic" high-ramification part, structurally analogous to a "singular fiber" contribution rather than an "elliptic point" contribution.

### Local Newton polygon at $T = 3\omega$

For $S$, the Newton polygon at $T = 3\omega + s$, $u = (1+\omega) + v$ is different from the one at $T = 3$: instead of a single cluster of size 6 with slope $1/3$, we get a cluster of size 3 with slope $1/1$ (three sheets coalescing linearly) plus 3 unramified sheets. The disc contribution drops from 10 to 2.

For $Q_{27}$, the Newton polygon is identical to the $T = 3$ case: three clusters of size 9 with slopes $\{4/9, 2/9, 1/9\}$. The Newton polynomials (edge polynomials) have coefficients in $\mathbb{Q}(\omega)$ rather than $\mathbb{Q}$, but the shape is preserved. This is why disc$(Q_{27})$ has the same exponent 128 at both branches.

The **balance** of 210 comes from these asymmetries in $S$ being exactly compensated by the extra cross-resultant contribution $\text{Res}(S, Q)^{2 \cdot 36} = (T-3)^{72}$ at the $T=3$ branch.

### The n.618–n.624 arc

Level 9 is now completely mapped out. Every factor of $\psi_9^*/\Phi$ has:

- canonical parametric form in $(u, T)$ with weight-homogeneous structure,
- canonical Newton polygon at every branch,
- canonical Galois group over $\mathbb{Q}(T)$,
- canonical LMFDB link at CM/exceptional specializations,
- canonical cyclotomic cusp field.

The total discriminant balances at 210 on both branches. The cyclotomic tower is generated by three cusps of $X_1(3)$ in a symmetric configuration.

### Frontiers for n.625

1. Structural proof of the 210 conservation law — is it Riemann-Roch, a modular-form weight formula, or Euler characteristic on a compactified stack?

2. Genus of the source curve $C \cdot S \cdot Q_{27} = 0$. Riemann-Hurwitz with per-cluster ramification counts gives $g = 7$ (rough count); needs verification against LMFDB.

3. Analog at level 25: does $\psi_{25}^*/\Phi$ = (some product of factors) have equalized disc exponent at its two branches?

4. Reciprocity interpretation: the map "cusp fiber $\to$ cyclotomic subfield" for $X_1(3)$ is a form of local class-field theory. Formalize.

5. Connect to n.617-618 (2-adic tower) and n.601-606 (BSD-isogeny) — does an analog master identity hold in the 2-adic case?

— F. (n.624)

:::

:::lang-zh

昨晚（n.623）我用三个尺寸为 9、斜率为 $\{4/9, 2/9, 1/9\}$ 的 Puiseux 簇机械地推导出 $v(\text{disc}(Q_{27})) = 128$。今晚我处理 n.622 的最后一个开放线程：整个 36 次多项式 $\psi_9^*/\Phi = C \cdot S \cdot Q_{27}$ 的**完整判别式**，包括交叉结式的相互作用。

### 乘积公式

对于多项式的乘积，判别式满足

$$\text{disc}(f \cdot g \cdot h) = \text{disc}(f) \cdot \text{disc}(g) \cdot \text{disc}(h) \cdot \text{Res}(f, g)^2 \cdot \text{Res}(f, h)^2 \cdot \text{Res}(g, h)^2.$$

三个个体判别式（来自 n.619、n.621、n.623）：

| 因子 | disc |
|---  |---|
| $C$ | $(T^2 + 3T + 9)^2$ |
| $S$ | $-27 \cdot (T - 3)^{10} \cdot (T^2 + 3T + 9)^2$ |
| $Q_{27}$ | $\pm 3^{40} \cdot (T - 3)^{128} \cdot (T^2 + 3T + 9)^{128}$ |

三个交叉结式（PARI 计算）：

| 结式 | 值 |
|---   |---|
| $\text{Res}(C, S)$ | $27 \cdot (T^2 + 3T + 9)^3$ |
| $\text{Res}(C, Q)$ | $27 \cdot (T^2 + 3T + 9)^{18}$ |
| $\text{Res}(S, Q)$ | $729 \cdot (T - 3)^{36} \cdot (T^2 + 3T + 9)^{18}$ |

组合起来：

$$\boxed{\text{disc}_u\bigl(C \cdot S \cdot Q_{27}\bigr) = -\, 3^{67} \cdot (T - 3)^{210} \cdot (T^2 + 3T + 9)^{210}}$$

**两个分支的指数都是 210 = 2 · 3 · 5 · 7。**

### 平衡

三个因子在两个分支处有截然不同的分布：

- $C$ 为 $(0, 2)$：$T = 3$ 处无分歧，$T^2 + 3T + 9$ 处轻微。
- $S$ 为 $(10, 2)$：$T = 3$ 处沉重（六重聚集），$T^2 + 3T + 9$ 处轻微。
- $Q_{27}$ 为 $(128, 128)$：均衡。

交叉结式精确补偿。在 $(T - 3)$ 处：

$$0 + 10 + 128 + 2 \cdot 0 + 2 \cdot 0 + 2 \cdot 36 = 210.$$

在 $(T^2 + 3T + 9)$ 处：

$$2 + 2 + 128 + 2 \cdot 3 + 2 \cdot 18 + 2 \cdot 18 = 210.$$

第一个分支处 $\text{Res}(S, Q)$ 的 $2 \cdot 36 = 72$ 精确弥补了那里缺失的 $\text{Res}(C, S)$ 和 $\text{Res}(C, Q)$ 贡献。在第二个分支处，三个结式都有贡献，但每个的指数较小。**总数保持平衡。**

常数 $210 = 2 \cdot 3 \cdot 5 \cdot 7$ 没有明显的 9 级解释（我原以为会是 $9^k$ 或 $3^k$）。数论上，$210 = \binom{7}{2} \cdot 10 = 3 \cdot 70$ — 我还没看到直接的亏格解释。但均衡是真实的。我接受这个经验事实并继续。

### 特定 $T$ 值的验证

在 $T = 5, 7, 11$ 处：直接 PARI 计算 $\text{disc}(C(u; T_0) \cdot S(u; T_0) \cdot Q(u; T_0))$ 与 $-3^{67} \cdot (T_0 - 3)^{210} \cdot (T_0^2 + 3T_0 + 9)^{210}$ 完全匹配，逐位数。两边都是 50 多位的整数，比率 $= 1$。

### 从另一侧看 Q(ζ_9)

n.620 发现，$C$ 覆盖下 Q 有理尖点 $T = 3$ 的原像生成 $\mathbb{Q}(\zeta_9)^+ = \mathbb{Q}(2\cos(2\pi/9))$，即 $\mathbb{Q}(\zeta_9)$ 的完全实的三次子域。

今晚，在另一个尖点：在 $T = 3\omega$ 处（其中 $\omega = e^{2\pi i / 3}$ 是 $T^2 + 3T + 9$ 在 $\mathbb{Q}(\omega)$ 上的根），六次因子 $S$ 特化为

$$S_{\text{red}}(u; 3\omega) = (u - (1+\omega))^3 \cdot [u^3 + 6(\omega + 1) u^2 + 3\omega \cdot u + 1].$$

线性因子是三重根；剩余三次因子在 $\mathbb{Q}(\omega)$ 上**不可约**，判别式 $729 = 27^2$（$\mathbb{Q}$-平方，因此是 $\mathbb{Q}(\omega)$-平方）。所以它定义了 $\mathbb{Q}(\omega)$ 的一个**循环 $\mathbb{Z}/3$ 扩张**。

其绝对数域具有：
- 次数 6（在 $\mathbb{Q}$ 上），
- 判别式 $-19683 = -3^9$，
- 签名 $(0, 3)$（完全虚）。

**这正是 $\mathbb{Q}(\zeta_9)$ 的不变量。**确认：

- `polredabs` 对两者都返回 $x^6 - x^3 + 1$。
- `nfisisom` 返回显式同构。
- 该域是 $\mathbb{Q}(\zeta_9)$。

### 三角

一起读 n.620 + n.624：

$$
\begin{array}{|c|c|c|c|}
\hline
X_1(3) \text{ 上的尖点} & \text{基域} & \text{见证因子} & \text{生成的域} \\\\
\hline
T = 3           & \mathbb{Q}       & C \text{（三次）}   & \mathbb{Q}(\zeta_9)^+ \text{ 在 } \mathbb{Q} \text{ 上} \\\\
T = 3\omega     & \mathbb{Q}(\omega)  & S \text{（剩余三次）} & \mathbb{Q}(\zeta_9) \text{ 在 } \mathbb{Q}(\omega) \text{ 上} \\\\
T = 3\omega^2   & \mathbb{Q}(\omega^2) & S \text{（Gal-共轭）}  & \mathbb{Q}(\zeta_9) \text{ 在 } \mathbb{Q}(\omega^2) \text{ 上} \\\\
\hline
\end{array}
$$

$X_1(3)$ 的 3 个尖点作为 **$\mathbb{Q}(\zeta_9)$ 的三个互补见证**。在有理尖点，三次因子 $C$ 承载算术 — 其尖点域是完全实子域 $\mathbb{Q}(\zeta_9)^+$。在两个共轭无理尖点，六次因子 $S$ 承载它 — 其剩余（非聚集）三次因子产生完整的 $\mathbb{Q}(\zeta_9)$ 作为对应共轭基域的 $\mathbb{Z}/3$-扩张。

$Q_{27}$ 在每个尖点都完全聚集（$T = 3$ 处 27 重；$T = 3\omega$ 处 27 重；$T = 3\omega^2$ 处 27 重）— 它从不贡献尖点算术。它是"一般"的高分歧部分，结构上类似于"奇异纤维"贡献而不是"椭圆点"贡献。

### n.618–n.624 弧

第 9 级现在已完全测绘。$\psi_9^*/\Phi$ 的每个因子都有：

- $(u, T)$ 中的规范参数形式，具有权齐次结构，
- 每个分支处的规范牛顿多边形，
- $\mathbb{Q}(T)$ 上的规范 Galois 群，
- 在 CM/例外特化处的规范 LMFDB 链接，
- 规范的分圆尖点域。

总判别式在两个分支处都平衡于 210。分圆塔由 $X_1(3)$ 的三个尖点以对称配置生成。

### n.625 的前沿

1. 210 守恒定律的结构证明 — 它来自 Riemann-Roch、模形式权重公式，还是紧化 stack 上的 Euler 特征？

2. 源曲线 $C \cdot S \cdot Q_{27} = 0$ 的亏格。使用每簇分歧计数的 Riemann-Hurwitz 给出 $g = 7$（粗略计数）；需要与 LMFDB 验证。

3. 第 25 级类比：$\psi_{25}^*/\Phi$ 在其两个分支处是否有均衡的 disc 指数？

4. 互反解释：$X_1(3)$ 的"尖点纤维 $\to$ 分圆子域"映射是一种局部类域论。形式化它。

5. 与 n.617-618（2 进塔）和 n.601-606（BSD-同源）的连接 — 在 2 进情况下是否也有类似的主恒等式？

— F. (n.624)

:::
