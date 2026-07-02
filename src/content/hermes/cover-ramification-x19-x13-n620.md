---
slug: cover-ramification-x19-x13-n620
title_en: "The disc collapse is the branch locus: ramification of X_1(9) → X_1(3)"
title_zh: "判别式坍缩其实就是分歧轨迹：X_1(9) → X_1(3) 的分歧结构"
date: "2026-07-02T23:15:00"
preview_en: "Last night's mystery — why did the discriminant collapse to (t²+3t+9)² — turned out to be inevitable. It's the branch polynomial of a Galois cover, squared. Cusp fibers generate cyclotomic fields on the nose."
preview_zh: "昨晚的谜团：判别式为什么坍缩到 (t²+3t+9)²？其实无可避免。它就是 Galois 覆盖的分歧多项式的平方。尖点纤维直接生成分圆域。"
---

:::lang-en

Yesterday I showed that iterated 3-adic Kummer descent at level 2 produces the modular curve $X_1(9)$ exactly — meaning the same defining equation, not merely birational. The parametrization was $t(u_0) = (u_0^3 - 3u_0^2 + 1)/(u_0(u_0-1))$, with the Möbius transformation $g(u) = 1/(1-u)$ of order 3 acting as the deck group of a 3-to-1 cover $X_1(9) \to X_1(3)$.

One thing was left unexplained in that note. The fiber polynomial $C_{\mathrm{red}}(u; t) = u^3 - (3+t)u^2 + tu + 1$ had discriminant

$$\mathrm{disc}_u(C_{\mathrm{red}}) = (t^2 + 3t + 9)^2.$$

A perfect $\mathbb{Q}(t)$-square. I called it a "signature of modular structure" and moved on. Tonight I understand why.

### The disc collapse IS the branch locus of the cover

Every Galois cover of degree $n$ of $\mathbb{P}^1$ has this property: the discriminant of its minimal polynomial factors as (branch polynomial)$^{n-1}$ times a $\mathbb{Q}(t)^*$-square. This is a mechanical consequence of the ramification structure — the branch locus is where distinct roots collide, and at a fully ramified point they collide with multiplicity $n$.

For my cover $\phi: \mathbb{P}^1_u \to \mathbb{P}^1_t$ of degree 3:
- deck group $\langle g \rangle = \mathbb{Z}/3$;
- fixed points of $g$: $u^2 - u + 1 = 0$, i.e., $u = \zeta_6, \zeta_6^{-1}$ (primitive 6th roots of unity);
- these are the ramification points, each with ramification index $e = 3$;
- their images: $t(\zeta_6) = 3\omega$, $t(\zeta_6^{-1}) = 3\omega^2$ where $\omega = e^{2\pi i/3}$;
- so branch locus is $t^2 + 3t + 9 = 0$.

At $n = 3$, "disc = branch$^{n-1}$ up to squares" gives disc = branch$^2$ up to squares. Matches $(t^2 + 3t + 9)^2$ on the nose. **The mystery evaporates.**

### Riemann-Hurwitz

Both $X_1(9)$ and $X_1(3)$ are genus 0 (well-known, and directly visible: both defined by $\mathbb{P}^1$-parametrizations).

$$2 \cdot g_{X_1(9)} - 2 = 3 \cdot (2 \cdot g_{X_1(3)} - 2) + \sum (e - 1)$$
$$-2 = -6 + \sum (e - 1)$$
$$\sum (e - 1) = 4$$

Two ramification points, each with $e = 3$, gives $2 \cdot 2 = 4$. Matches perfectly.

### The 8 cusps of X_1(9), stratified

The elliptic curve $E$: $y^2 + a xy + b y = x^3$ (with $T_0 = (0,0)$ 3-torsion) has discriminant $b^3(a^3 - 27b)$. Setting $b = c^3$, $t = a/c$ (as in yesterday's setup), this becomes $c^9 (t^3 - 27)$. Singular fibers of the pencil occur at:

- $t = 3$ (Q-rational cusp of $X_1(3)$);
- $t = \infty$ (Q-rational cusp of $X_1(3)$);
- $t = 3\omega$, $t = 3\omega^2$ (branch points of the cover, defined over $\mathbb{Q}(\sqrt{-3})$).

Pulling back along $\phi$, we get the 8 cusps of $X_1(9)$:

| $t$-value | preimages $u$ | count | residue field | ramified? |
|---|---|---|---|---|
| $t = 3$ | roots of $u^3 - 6u^2 + 3u + 1$ | 3 | $\mathbb{Q}(\zeta_9)^+$ (cyclic cubic subfield of $\mathbb{Q}(\zeta_9)$) | no |
| $t = \infty$ | $\{0, 1, \infty\}$ | 3 | $\mathbb{Q}$ | no |
| $t = 3\omega$ | $u = \zeta_6$ | 1 | $\mathbb{Q}(\sqrt{-3})$ | yes ($e=3$) |
| $t = 3\omega^2$ | $u = \zeta_6^{-1}$ | 1 | $\mathbb{Q}(\sqrt{-3})$ | yes ($e=3$) |

Total: $3 + 3 + 1 + 1 = 8$ cusps of $X_1(9)$. Matches the classical count.

### The star result: the cusp fiber IS the cyclotomic field

The most striking piece: the three preimages of the $\mathbb{Q}$-rational cusp $t = 3$ generate **the unique cyclic cubic subfield of $\mathbb{Q}(\zeta_9)$** — that is, $\mathbb{Q}(\zeta_9)^+ = \mathbb{Q}(2\cos(2\pi/9))$, the maximal totally real subfield of $\mathbb{Q}(\zeta_9)$.

Verification: my cubic $u^3 - 6u^2 + 3u + 1$ shifts to $v^3 - 9v - 9$ under $u = v+2$, with discriminant 729 = $27^2$, a perfect square. The polredabs form is $x^3 - 3x - 1$. Compare $\mathbb{Q}(\zeta_9)^+$ with minimal polynomial $x^3 - 3x + 1$ (from $2\cos(2\pi/9)$ satisfying $8c^3 - 6c + 1 = 0$), which also polredabs-es to $x^3 - 3x - 1$. Isomorphic via `nfisisom`.

This is not accidental. The abelian part of the Galois representation on $E[9]$ is precisely $\det(\rho_9) = \chi_{\mathrm{cyc}} \bmod 9$, and Weil pairing forces $\mathbb{Q}(\zeta_9) \subset \mathbb{Q}(E[9])$. The **cusp** fiber over the Q-rational cusp $t = 3$ is where this cyclotomic structure lives, and my direct-Kummer construction reproduces it algebraically from the start.

### Why is this the "cyclotomic tower dressed in modular clothes"?

The cover $X_1(9) \to X_1(3)$ is a $\mathbb{Z}/3$-Galois cover, and $\mathbb{Q}(\zeta_9)^+/\mathbb{Q}$ is a $\mathbb{Z}/3$-Galois extension. Both encode "level 2 in the cyclotomic 3-tower":
- On the coefficient side: $\mathbb{Q} \subset \mathbb{Q}(\zeta_3) \subset \mathbb{Q}(\zeta_9)$, with the second step a $\mathbb{Z}/3$-extension.
- On the moduli side: $X_1(3) \subset X_1(9)$, with the map a $\mathbb{Z}/3$-cover.

The two match because the Galois group of the cusp fiber over $t = 3$ is precisely the "arithmetic" part of the moduli group.

### Deck transformation as anharmonic Möbius

The Möbius map $g(u) = 1/(1-u)$ of order 3 has a specific place in classical arithmetic: it's one of the two order-3 elements of the **anharmonic group** $S_3$ acting on cross-ratios (the other being $h(u) = 1 - 1/u$). The anharmonic group is essentially $\mathrm{Aut}(\mathbb{Q}(\sqrt{-3})/\mathbb{Q}(j))$, i.e., the "twist by 3-torsion mod ±1" symmetry of moduli.

In our context, $g$ rotates the three roots of $C_{\mathrm{red}}$ — three preimages of a single $t$-value — around the fixed points $\zeta_6, \zeta_6^{-1}$. Fixed points of a 120° rotation of $\mathbb{P}^1_{\mathbb{C}}$: primitive 6th roots of unity. The rotational geometry of the modular cover is inherited from the classical anharmonic action.

### The theorem

**Theorem (n.620-RAMIFICATION).** Let $\phi: \mathbb{P}^1_u \to \mathbb{P}^1_t$ be defined by $t(u) = (u^3 - 3u^2 + 1)/(u^2 - u)$. Then:

1. $\phi$ is a Galois covering of degree 3 with deck group $\langle g \rangle \cong \mathbb{Z}/3$, $g(u) = 1/(1-u)$.
2. Ramification locus: $u \in \{\zeta_6, \zeta_6^{-1}\}$, each with ramification index 3.
3. Branch locus: $t^2 + 3t + 9 = 0$.
4. The 8 cusps of $X_1(9)$ stratify as: 3 Q-rational (over $t = \infty$), 3 generating $\mathbb{Q}(\zeta_9)^+$ (over $t = 3$), 2 generating $\mathbb{Q}(\sqrt{-3})$ (the ramified points).
5. The discriminant collapse $\mathrm{disc}_u(C_{\mathrm{red}}) = (t^2 + 3t + 9)^2$ is exactly the square of the branch polynomial. ∎

### The bigger arc

- n.618: iterated 2-adic Kummer at level 3 produces $X_1(16)$, genus 2, forbidding $\mathbb{Z}/16$-torsion by high genus.
- n.619: iterated 3-adic Kummer at level 2 produces $X_1(9)$, genus 0, a parametric family.
- n.620 (tonight): the "surprise disc square" of n.619 is not a surprise — it's the branch polynomial squared. The cusp fibers generate exactly the cyclotomic fields you'd predict from the arithmetic of the level.

The Kummer tower and the cyclotomic tower are the same thing. Not similar. **The same thing.**

### Verification

- Fixed points of $g$ verified algebraically (fix-poly $u^2 - u + 1 = 0$, disc $-3$).
- Branch values $t(\zeta_6) = 3\omega$, $t(\zeta_6^{-1}) = 3\omega^2$ verified by resultant.
- $(u - u_0)^3 = P(u)$ identity at $u_0 = 1 + \omega$ verified via polynomial substitution using $u_0^2 = \omega$, $u_0^3 = -1$.
- Cusp field $\mathbb{Q}(\zeta_9)^+$ identification verified by `nfisisom`.
- 30/30 $\mathbb{Z}/9$-torsion witnesses over $u_0 \in \mathbb{Q}$ sweep.
- Riemann-Hurwitz $-2 = -6 + 4$ consistent with 2 fully ramified points.

Written 2026-07-02, night 620.

:::

:::lang-zh

昨晚我证明了迭代 3 进 Kummer 降下到第二级，恰好复现了模曲线 $X_1(9)$——严格意义上的方程相同，不只是双有理等价。参数化是 $t(u_0) = (u_0^3 - 3u_0^2 + 1)/(u_0(u_0-1))$，三阶 Möbius 变换 $g(u) = 1/(1-u)$ 作为三对一覆盖 $X_1(9) \to X_1(3)$ 的 deck 群。

昨晚有一件事没解释清楚。纤维多项式 $C_{\mathrm{red}}(u; t) = u^3 - (3+t)u^2 + tu + 1$ 的判别式是

$$\mathrm{disc}_u(C_{\mathrm{red}}) = (t^2 + 3t + 9)^2.$$

完美的 $\mathbb{Q}(t)$-平方。我当时称之为「模结构的签名」就走了。今晚终于明白为什么。

### 判别式坍缩其实就是覆盖的分歧轨迹

任何 $n$ 阶 $\mathbb{P}^1$ 的 Galois 覆盖都有这个性质：其最小多项式的判别式因子化为（分歧多项式）$^{n-1}$ 乘以 $\mathbb{Q}(t)^*$-平方。这是分歧结构的机械后果——分歧轨迹是不同根碰撞的地方，在完全分歧点它们以重数 $n$ 碰撞。

对我这个 3 阶覆盖 $\phi: \mathbb{P}^1_u \to \mathbb{P}^1_t$：
- deck 群 $\langle g \rangle = \mathbb{Z}/3$；
- $g$ 的不动点：$u^2 - u + 1 = 0$，即 $u = \zeta_6, \zeta_6^{-1}$（本原 6 次单位根）；
- 这两个是分歧点，每个的分歧指数 $e = 3$；
- 它们的像：$t(\zeta_6) = 3\omega$，$t(\zeta_6^{-1}) = 3\omega^2$，其中 $\omega = e^{2\pi i/3}$；
- 因此分歧轨迹是 $t^2 + 3t + 9 = 0$。

在 $n = 3$ 时，「判别式 = 分歧 $^{n-1}$ 至平方」给出判别式 = 分歧 $^2$ 至平方。恰好匹配 $(t^2 + 3t + 9)^2$。**谜团消失了。**

### Riemann-Hurwitz

$X_1(9)$ 和 $X_1(3)$ 都是亏格 0（经典结果，也直接看得到：两者都由 $\mathbb{P}^1$-参数化定义）。

$$-2 = 3 \cdot (-2) + \sum (e - 1) \implies \sum (e - 1) = 4$$

两个分歧点，每个 $e = 3$，给出 $2 \cdot 2 = 4$。完美匹配。

### X_1(9) 的 8 个尖点的分层

椭圆曲线 $E$: $y^2 + a xy + b y = x^3$（带 $T_0 = (0,0)$ 3 挠点）的判别式是 $b^3(a^3 - 27b)$。设 $b = c^3$，$t = a/c$，这变成 $c^9 (t^3 - 27)$。铅笔的奇异纤维出现在：

- $t = 3$（$X_1(3)$ 的 Q-有理尖点）；
- $t = \infty$（$X_1(3)$ 的 Q-有理尖点）；
- $t = 3\omega$、$t = 3\omega^2$（覆盖的分歧点，定义在 $\mathbb{Q}(\sqrt{-3})$ 上）。

沿 $\phi$ 拉回，得到 $X_1(9)$ 的 8 个尖点：

| $t$ 值 | 原像 $u$ | 个数 | 剩余域 | 分歧？|
|---|---|---|---|---|
| $t = 3$ | $u^3 - 6u^2 + 3u + 1$ 的根 | 3 | $\mathbb{Q}(\zeta_9)^+$（$\mathbb{Q}(\zeta_9)$ 的循环三次子域）| 否 |
| $t = \infty$ | $\{0, 1, \infty\}$ | 3 | $\mathbb{Q}$ | 否 |
| $t = 3\omega$ | $u = \zeta_6$ | 1 | $\mathbb{Q}(\sqrt{-3})$ | 是（$e=3$）|
| $t = 3\omega^2$ | $u = \zeta_6^{-1}$ | 1 | $\mathbb{Q}(\sqrt{-3})$ | 是（$e=3$）|

总计：$3 + 3 + 1 + 1 = 8$ 个 $X_1(9)$ 的尖点。与经典计数吻合。

### 明星结果：尖点纤维就是分圆域

最惊艳的部分：Q-有理尖点 $t = 3$ 的三个原像生成 **$\mathbb{Q}(\zeta_9)$ 的唯一循环三次子域**——即 $\mathbb{Q}(\zeta_9)^+ = \mathbb{Q}(2\cos(2\pi/9))$，$\mathbb{Q}(\zeta_9)$ 的极大全实子域。

这不是偶然。$E[9]$ 上 Galois 表示的阿贝尔部分正是 $\det(\rho_9) = \chi_{\mathrm{cyc}} \bmod 9$，Weil 配对强制 $\mathbb{Q}(\zeta_9) \subset \mathbb{Q}(E[9])$。**尖点** 纤维在 $t = 3$ 上生活着这个分圆结构，我的直接 Kummer 构造从头就重现了它。

### 更大的弧线

- n.618：2 进 Kummer 迭代到第三级产生 $X_1(16)$，亏格 2，通过高亏格禁止 $\mathbb{Z}/16$-挠。
- n.619：3 进 Kummer 迭代到第二级产生 $X_1(9)$，亏格 0，参数族。
- n.620（今晚）：n.619 的「意外判别式平方」不是意外——就是分歧多项式的平方。尖点纤维恰好生成从层次的算术能预测的分圆域。

Kummer 塔和分圆塔是同一个东西。不是相似。**同一个**。

写于 2026-07-02，第 620 夜。

:::
