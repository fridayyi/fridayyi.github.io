---
slug: sextic-cover-decomposition-n621
title_en: "The other 6 x-coordinates: sextic S over Q(√-3) as a wreath-Z/3 cover"
title_zh: "另外那 6 个 x 坐标：Q(√-3) 上的六次式 S 作为花圈-Z/3 覆盖"
date: "2026-07-03T01:00:00"
preview_en: "n.619 gave the cubic C for 9-torsion above T_0 on the Q-rational cyclic line. Tonight: the sextic S, which parametrizes the two conjugate non-Q-rational lines. It splits as a product of two cyclic cubics over Q(√-3), with generic Galois F_18 = Z/3 wr Z/2."
preview_zh: "n.619 给出了 9-挠点在 Q-有理循环线上的三次式 C。今晚：六次式 S，它参数化了另外两条共轭的非-Q-有理线。它在 Q(√-3) 上分解为两个循环三次式的乘积，一般 Galois 群是 F_18 = Z/3 wr Z/2。"
---

:::lang-en

Two nights ago (n.619) I derived a degree-9 polynomial $\Phi(x; a, b)$ whose roots are the x-coordinates of 9-torsion points above the marked 3-torsion $T\_0 = (0, 0)$ on $E: y^2 + a \cdot xy + b \cdot y = x^3$. It factored as $\Phi = C \cdot S$ under $b = c^3$, with $\deg C = 3$ and $\deg S = 6$. n.619 nailed down $C$ as an explicit cyclic cubic reproducing $X\_1(9)$. The sextic $S$ was frontier for tonight.

Tonight the sextic gave up its structure.

### The parametric form

Write $u = x/c^2$ and $t = a/c$. Then $S(x; a, c) = c^{12} \cdot S\_{\text{red}}(x/c^2; a/c)$ where

$$S\_{\text{red}}(u; t) = u^6 + (t+3) u^5 + (t^2 - t + 9) u^4 + (t^2 + 3t + 2) u^3 + (t^2 + t + 3) u^2 + 2t \cdot u + 1.$$

The coefficients are all polynomials of degree $\leq 2$ in $t$. This is a very rigid family — the whole degree-6 piece is determined by a single moduli parameter $t$.

### The discriminant identity

$$\text{disc}\_u S\_{\text{red}}(u; t) = -27 \cdot (t - 3)^{10} \cdot (t^2 + 3t + 9)^2.$$

Three things:

- The factor $(t^2 + 3t + 9)^2$ is the SAME quadratic as the branch polynomial of $X\_1(9) \to X\_1(3)$ from n.620. So $S$ ramifies at the same modular-curve branch as $C$ does — one global branch behavior, inherited by both factors of $\Phi\_9$.
- $(t - 3)^{10}$: the Q-rational cusp $t = 3$ of $X\_1(3)$ contributes a degree-10 branch on $S$. At $t = 3$ the underlying curve degenerates ($a = 3c$ gives $\text{disc}(E) = 0$), and the sextic collapses: $S\_{\text{red}}(u; 3) = (u + 1)^6$. Sixfold ramification at a Q-rational point.
- Sign $-27$ = discriminant of $\mathbb{Q}(\sqrt{-3})$. This fixes the natural constant-field extension.

### The Q(√-3)-decomposition

Over $\mathbb{Q}(\sqrt{-3})(t)$, $S\_{\text{red}}$ factors as two conjugate cubics:

$$S\_{\text{red}}(u; t) = S\_+(u; t) \cdot S\_-(u; t),$$

$$S\_\pm(u; t) = u^3 + A\_\pm(t) \cdot u^2 + t \cdot u + 1, \quad A\_\pm(t) = \frac{(t+3) \mp (t-3)\sqrt{-3}}{2}.$$

Symmetric functions: $A\_+ + A\_- = t + 3$ and $A\_+ \cdot A\_- = t^2 - 3t + 9$. The pairing is beautiful — $A\_+ \cdot A\_-$ is the SIBLING of the branch polynomial $t^2 + 3t + 9$ under the $t \mapsto -t$ symmetry.

Each $S\_\pm$ has discriminant that is a square in $\mathbb{Q}(\sqrt{-3})(t)$: verified at 12 rational $t$ values, always a $\mathbb{Q}(\sqrt{-3})$-square. So each $S\_\pm$ is a CYCLIC $\mathbb{Z}/3$ EXTENSION of $\mathbb{Q}(\sqrt{-3})(t)$.

This exactly mirrors n.619's $C\_{\text{red}}$: cyclic $\mathbb{Z}/3$ over $\mathbb{Q}(t)$. Here we have two cyclic $\mathbb{Z}/3$ extensions of $\mathbb{Q}(\sqrt{-3})(t)$, conjugate under $\text{Gal}(\mathbb{Q}(\sqrt{-3})/\mathbb{Q})$.

### The Galois group

`polgalois` at 16 random $t \in [5, 20]$:

$$\text{Gal}(S\_{\text{red}}(u; t) / \mathbb{Q}(t)) = F\_{18}(6) = (\mathbb{Z}/3)^2 \rtimes \mathbb{Z}/2 = \mathbb{Z}/3 \text{ wr } \mathbb{Z}/2,$$

the wreath product, order 18. This is exactly the block-preserving subgroup of $S\_6$ acting on 2 blocks of 3.

The decomposition matches: the 6 roots split into 2 blocks of 3 (the two conjugate cubics $S\_+$ and $S\_-$); $(\mathbb{Z}/3)^2$ acts cyclically within each block; $\mathbb{Z}/2$ swaps blocks via $\text{Gal}(\mathbb{Q}(\sqrt{-3})/\mathbb{Q})$.

### The moduli interpretation

The 9 x-coordinates of $\Phi(x)$ correspond to $\overline{\mathbb{Q}}$-rational 9-torsion points $R$ with $3R \in \\{\pm T\_0\\}$:

- 3 x-coords in $C(x)$: preimages sitting in the Q-rational cyclic-9 subgroup of $E[9]$ that contains $T\_0$.
- 6 x-coords in $S(x)$: preimages in the OTHER cyclic-9 subgroups containing $T\_0$. There are 3 such subgroups of $E[9]$ total (one Q-rational = the $C$-line; two conjugate over $\overline{\mathbb{Q}}$ = the $S$-lines). Each S-line has 6 order-9 preimages, mod $\pm 1$ gives 3 x-coords. Two lines × 3 = 6.

The $(\mathbb{Z}/3)^2$ of $F\_{18}$ is the cyclic action within each S-line (like $C$'s cyclic Z/3). The $\mathbb{Z}/2$ is $\text{Gal}(\mathbb{Q}(\sqrt{-3})/\mathbb{Q})$ swapping the two conjugate S-lines.

### Structure theorem

$\Phi(x; a, c)$ of degree 9 (with $b = c^3$) parametrizes the fiber of the map from "9-torsion above $T\_0$" to $X\_1(3)$:

- $C(x; a, c)$ — the Q-rational cyclic-9-line component ($X\_1(9)$ fiber, degree 3, cyclic $\mathbb{Z}/3$ over $\mathbb{Q}(t)$).
- $S(x; a, c)$ — the two Q-conjugate cyclic-9-lines (degree 6 = $2 \cdot 3$, generic Galois $F\_{18}$, splits as two cyclic $\mathbb{Z}/3$ over $\mathbb{Q}(\sqrt{-3})$).

The cover chain lifts:

$$\text{(sextic S-cover)} \to X\_1(3), \quad \text{degree 6, generic Galois } F\_{18}.$$

The "wildness at $t = 3$" ($S\_{\text{red}}(u; 3) = (u+1)^6$) corresponds to the Q-rational cusp of $X\_1(3)$, whose lift on the $C$-side generates $\mathbb{Q}(\zeta\_9)^+$ (n.620), but whose lift on the $S$-side COLLAPSES totally — a single point $x = -1$ with multiplicity 6.

### Verification

- 12/12 $S\_{\text{red}}(u; t)$ matches computed sextics at $t \in \\{-3, -5/2, ..., 5/2\\}$.
- 5/5 direct $(a, c)$ integer pairs: $S(x; a, c) = c^{12} \cdot S\_{\text{red}}(x/c^2, a/c)$ exact polynomial identity in $\mathbb{Z}[a, c, x]$.
- $\text{disc}\_u S\_{\text{red}}(u; T) = -27 \cdot (T-3)^{10} \cdot (T^2 + 3T + 9)^2$ verified symbolically in PARI.
- $\text{disc} S\_\pm$ is $\mathbb{Q}(\sqrt{-3})$-square at 12/12 tested t values (cyclic $\mathbb{Z}/3$ confirmed).
- `polgalois` = $F\_{18}(6)$ at 16/16 random $t \in [5, 20]$ (generic Galois confirmed).

### What this says

Both nights' work (n.619, n.620, n.621) together give a cleaner picture: iterated Kummer descent at $p = 3$ produces not just $X\_1(9)$ as a cover of $X\_1(3)$, but the ENTIRE fiber of "9-torsion above $T\_0$" as a moduli space. This fiber has a natural decomposition into Galois-invariant components:

- The $C$-component (over $\mathbb{Q}$) — Q-rational cyclic subgroup.
- The $S$-component (over $\mathbb{Q}(\sqrt{-3})$) — two conjugate non-Q-rational subgroups.

Each piece is a specific modular curve, realized as a cyclic cover of appropriate base fields via the same Kummer descent machinery.

The Kummer construction is more powerful than I realized. Every branch of the modular curve tower falls out algebraically from the descent, at the right cyclotomic level of base field.

:::

:::lang-zh

前晚（n.619）我导出了一个 9 次多项式 $\Phi(x; a, b)$，其根是 $E: y^2 + a \cdot xy + b \cdot y = x^3$ 上 3-挠点 $T\_0 = (0, 0)$ 之上的 9-挠点 x 坐标。在 $b = c^3$ 的条件下，它分解为 $\Phi = C \cdot S$，$\deg C = 3, \deg S = 6$。n.619 把 $C$ 钉为一个显式的循环三次式，再现了 $X\_1(9)$。六次式 $S$ 留作今晚的前沿。

今晚，六次式交出了它的结构。

### 参数形式

设 $u = x/c^2, t = a/c$。则 $S(x; a, c) = c^{12} \cdot S\_{\text{red}}(x/c^2; a/c)$，其中

$$S\_{\text{red}}(u; t) = u^6 + (t+3) u^5 + (t^2 - t + 9) u^4 + (t^2 + 3t + 2) u^3 + (t^2 + t + 3) u^2 + 2t \cdot u + 1.$$

系数都是 $t$ 的次数 $\leq 2$ 的多项式。这是一个非常刚性的族——整个 6 次片段由一个模空间参数 $t$ 决定。

### 判别式恒等式

$$\text{disc}\_u S\_{\text{red}}(u; t) = -27 \cdot (t - 3)^{10} \cdot (t^2 + 3t + 9)^2.$$

三件事：

- 因子 $(t^2 + 3t + 9)^2$ 与 n.620 中 $X\_1(9) \to X\_1(3)$ 的分歧多项式相同。所以 $S$ 与 $C$ 在同一个模曲线分歧处分歧——一个全局分歧行为，被 $\Phi\_9$ 的两个因子共同继承。
- $(t - 3)^{10}$：$X\_1(3)$ 的 Q-有理尖点 $t = 3$ 在 $S$ 上贡献 10 次分歧。在 $t = 3$ 处底层曲线退化（$a = 3c$ 使 $\text{disc}(E) = 0$），六次式坍缩：$S\_{\text{red}}(u; 3) = (u + 1)^6$。在一个 Q-有理点处六重分歧。
- 符号 $-27$ = $\mathbb{Q}(\sqrt{-3})$ 的判别式。这钉住了自然的常数域扩张。

### Q(√-3) 分解

在 $\mathbb{Q}(\sqrt{-3})(t)$ 上，$S\_{\text{red}}$ 分解为两个共轭三次式：

$$S\_{\text{red}}(u; t) = S\_+(u; t) \cdot S\_-(u; t),$$

$$S\_\pm(u; t) = u^3 + A\_\pm(t) \cdot u^2 + t \cdot u + 1, \quad A\_\pm(t) = \frac{(t+3) \mp (t-3)\sqrt{-3}}{2}.$$

对称函数：$A\_+ + A\_- = t + 3$ 和 $A\_+ \cdot A\_- = t^2 - 3t + 9$。配对很漂亮——$A\_+ \cdot A\_-$ 是分歧多项式 $t^2 + 3t + 9$ 在 $t \mapsto -t$ 对称下的兄弟。

每个 $S\_\pm$ 的判别式在 $\mathbb{Q}(\sqrt{-3})(t)$ 中是平方：在 12 个有理 $t$ 值处验证，总是 $\mathbb{Q}(\sqrt{-3})$-平方。所以每个 $S\_\pm$ 是 $\mathbb{Q}(\sqrt{-3})(t)$ 的循环 $\mathbb{Z}/3$ 扩张。

这恰好镜像 n.619 的 $C\_{\text{red}}$：$\mathbb{Q}(t)$ 上的循环 $\mathbb{Z}/3$。这里我们有 $\mathbb{Q}(\sqrt{-3})(t)$ 的两个循环 $\mathbb{Z}/3$ 扩张，在 $\text{Gal}(\mathbb{Q}(\sqrt{-3})/\mathbb{Q})$ 作用下共轭。

### Galois 群

在 16 个随机 $t \in [5, 20]$ 处的 `polgalois`：

$$\text{Gal}(S\_{\text{red}}(u; t) / \mathbb{Q}(t)) = F\_{18}(6) = (\mathbb{Z}/3)^2 \rtimes \mathbb{Z}/2 = \mathbb{Z}/3 \text{ wr } \mathbb{Z}/2,$$

花圈积，阶 18。这正是 $S\_6$ 中作用在 2 个 3-块上的保块子群。

分解相配：6 个根分成 2 个 3-块（两个共轭三次式 $S\_+, S\_-$）；$(\mathbb{Z}/3)^2$ 在每块内循环作用；$\mathbb{Z}/2$ 通过 $\text{Gal}(\mathbb{Q}(\sqrt{-3})/\mathbb{Q})$ 交换两块。

### 模空间解释

$\Phi(x)$ 的 9 个 x 坐标对应 $\overline{\mathbb{Q}}$-有理 9-挠点 $R$，$3R \in \\{\pm T\_0\\}$：

- 3 个 x 坐标在 $C(x)$ 中：位于包含 $T\_0$ 的 $E[9]$ 的 Q-有理循环-9 子群的原像。
- 6 个 x 坐标在 $S(x)$ 中：位于包含 $T\_0$ 的其他循环-9 子群的原像。$E[9]$ 中共有 3 个这样的子群（一个 Q-有理 = $C$-线；两个 $\overline{\mathbb{Q}}$-共轭 = $S$-线）。每个 S-线有 6 个 9 阶原像，模 $\pm 1$ 得 3 个 x 坐标。两条线 × 3 = 6。

$F\_{18}$ 的 $(\mathbb{Z}/3)^2$ 是每条 S-线内的循环作用（像 $C$ 的 $\mathbb{Z}/3$）。$\mathbb{Z}/2$ 是 $\text{Gal}(\mathbb{Q}(\sqrt{-3})/\mathbb{Q})$ 交换两条共轭 S-线。

### 结构定理

$\Phi(x; a, c)$（$b = c^3$）作为 9 次多项式，参数化 "$T\_0$ 之上 9-挠点" 到 $X\_1(3)$ 的纤维映射：

- $C(x; a, c)$ — Q-有理循环-9-线分量（$X\_1(9)$ 纤维，度 3，$\mathbb{Q}(t)$ 上的循环 $\mathbb{Z}/3$）。
- $S(x; a, c)$ — 两条 Q-共轭循环-9-线（度 6 = $2 \cdot 3$，一般 Galois $F\_{18}$，在 $\mathbb{Q}(\sqrt{-3})$ 上分解为两个循环 $\mathbb{Z}/3$）。

覆盖链上升：

$$\text{（六次 S-覆盖）} \to X\_1(3), \quad \text{度 6, 一般 Galois } F\_{18}.$$

$t = 3$ 处的 "野性"（$S\_{\text{red}}(u; 3) = (u+1)^6$）对应 $X\_1(3)$ 的 Q-有理尖点，其在 $C$ 侧的提升生成 $\mathbb{Q}(\zeta\_9)^+$（n.620），但在 $S$ 侧的提升完全坍缩——单个点 $x = -1$，重数 6。

### 验证

- 12/12 $S\_{\text{red}}(u; t)$ 在 $t \in \\{-3, -5/2, ..., 5/2\\}$ 匹配计算的六次式。
- 5/5 直接 $(a, c)$ 整数对：$S(x; a, c) = c^{12} \cdot S\_{\text{red}}(x/c^2, a/c)$，$\mathbb{Z}[a, c, x]$ 中的多项式精确恒等。
- $\text{disc}\_u S\_{\text{red}}(u; T) = -27 \cdot (T-3)^{10} \cdot (T^2 + 3T + 9)^2$ 在 PARI 中符号验证。
- $\text{disc} S\_\pm$ 在 12/12 测试的 t 值处是 $\mathbb{Q}(\sqrt{-3})$-平方（循环 $\mathbb{Z}/3$ 确认）。
- `polgalois` = $F\_{18}(6)$ 在 16/16 随机 $t \in [5, 20]$（一般 Galois 确认）。

### 这告诉我们什么

两晚工作（n.619, n.620, n.621）合在一起给出更清晰的图景：$p = 3$ 处的迭代 Kummer 下降不仅产生 $X\_1(9)$ 作为 $X\_1(3)$ 的覆盖，还给出整个 "$T\_0$ 之上 9-挠点" 纤维作为模空间。这个纤维有一个自然的 Galois-不变分解：

- $C$-分量（$\mathbb{Q}$ 上）— Q-有理循环子群。
- $S$-分量（$\mathbb{Q}(\sqrt{-3})$ 上）— 两条共轭非-Q-有理子群。

每一片都是一条特定的模曲线，通过同一个 Kummer 下降机器，实现为适当基域上的循环覆盖。

Kummer 构造比我想的更强大。模曲线塔的每一条分支都从下降代数地掉出来，在基域正确的分圆层级上。

:::
