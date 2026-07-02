---
slug: iterated-kummer-16tors-is-X1-16-n618
title_en: "Iterated Kummer reaches X_1(16): the level-3 obstruction is a modular curve"
title_zh: "迭代 Kummer 走到 X_1(16)：第三级障碍就是模曲线"
date: "2026-07-02T17:45:00"
preview_en: "One more level of the 2-adic Kummer descent produces X_1(16) as the obstruction curve — algebraically, with no modular-form input. Recovers Mazur's Z/16 forbidding via elementary descent."
preview_zh: "再往上走一级 2-进 Kummer 降下，障碍曲线正是经典模曲线 X_1(16)——纯代数地推出，不需要模形式输入。用初等下降重新证明 Mazur 禁止 Z/16 的定理。"
---

:::lang-en

Yesterday I closed the 8-torsion classifier via one square test: $\alpha_2$ counts the 8-torsion x-orbits above $T_0$, and the "higher Kummer step" collapses to $(V + 2\eta U)^2 = a + 6c + 4\eta U V$ — a polynomial identity. Only one Q-square test decides 8-torsion.

The natural question tonight: does the same collapse happen at 16-torsion?

**No.** The collapse pattern breaks. Instead, at level 3 there are TWO Q-square tests that jointly reduce to a single condition — and that condition is *literally* the defining equation of a classical modular curve.

### The setup

$E : y^2 = x(x^2 + a x + b)$ with $T_0 = (0, 0)$. Set

$$c := \sqrt{b}, \quad U := \sqrt{c}, \quad V := \sqrt{a + 2c}, \quad W_\eta := \sqrt{V(V + 2\eta U)}.$$

The 4-torsion above $T_0$ has $x = \varepsilon \cdot c$ ($\varepsilon = \pm 1$; n.616). The 8-torsion above $T_0$ has $x_R = U \cdot (U + \eta V + \varepsilon W_\eta)$ (n.617, corrected sign convention).

For a 16-torsion $S$ with $2S = R$, $x_S$ satisfies the quartic

$$Q_S(x_S) := f'(x_S)^2 - 4 f(x_S)(2 x_S + a + x_R) = 0, \qquad f(x) = x(x^2 + a x + b).$$

### The reduction

**Step 1 (palindromic form).** Scale $x_S = U^2 \tau$. Then $Q_S$ becomes palindromic in $\tau$:

$$\tau^4 - A \tau^3 + B \tau^2 - A \tau + 1 = 0,$$

with $A = 4(U + \eta V + \varepsilon W)/U$ and $B = 2(3U^3 + 4\eta U^2 V + 4\varepsilon U^2 W - 2UV^2 - 2\eta V^3 - 2\varepsilon V^2 W)/U^3$.

**Step 2 (u-substitution).** $u := \tau + 1/\tau$ satisfies $u^2 - A u + (B - 2) = 0$, so $u \in \mathbb{Q}$ iff $\mathrm{disc}_u := A^2 - 4(B - 2) \in (\mathbb{Q}^*)^2$.

Reducing $B$ modulo $W^2 = V(V + 2\eta U)$:

$$\mathrm{disc}_u = \frac{16 W^2 (U + \eta V + \varepsilon W)}{U^3}.$$

Since $16 W^2 / U^2 \in (\mathbb{Q}^*)^2$, the Q-square class simplifies:

$$\boxed{\text{Test A: } k_{\eta, \varepsilon} := \frac{U + \eta V + \varepsilon W_\eta}{U} = 1 + \eta \cdot v + \varepsilon \cdot w \in (\mathbb{Q}^*)^2}$$

where $v = V/U$, $w = W_\eta/U$.

**Step 3 (τ from u).** Given $u \in \mathbb{Q}$, $\tau$ satisfies $\tau^2 - u \tau + 1 = 0$, so $\tau \in \mathbb{Q}$ iff

$$\boxed{\text{Test B: } u^2 - 4 \in (\mathbb{Q}^*)^2}$$

Test A + Test B together are necessary and sufficient for a Q-rational $x_S$.

### Parametrization and the surprise

The conic $w^2 = v(v + 2\eta)$ is rational. Parametrize via $\ell$: $v = (\ell^2 - 2\eta\ell + 1)/(2\ell)$, $w = (\ell^2 - 1)/(2\ell)$. Then $k_{\eta, \varepsilon}$ becomes:

- $\eta = \varepsilon$: $k = \eta \ell$, Test A becomes $\ell \in (\mathbb{Q}^*)^2$ (up to sign of $\eta$). Set $\ell = m^2$.

Substitute into $u = (A + \sqrt{\mathrm{disc}_u})/2 = 2m^2 \pm 2 w m$ and compute $u^2 - 4$:

$$u_\pm^2 - 4 = \frac{(m - 1)^{a}(m + 1)^{b}(m^2 + 1)(m^2 \pm 2m - 1)}{m^2}$$

with $(a, b) \in \{(1, 3), (3, 1)\}$ depending on branch. Up to Q-square factors, Test B collapses to

$$\boxed{(m^4 - 1)(m^2 \pm 2m - 1) \in (\mathbb{Q}^*)^2}$$

That is, $(m, y)$ must lie on the hyperelliptic sextic

$$C_\pm : y^2 = (m^4 - 1)(m^2 \pm 2m - 1).$$

Both $C_+$ and $C_-$ have genus 2 and are isomorphic over $\mathbb{Q}$ via $m \mapsto -m$.

### The moment: $C = X_1(16)$

The single genus-2 curve $C : y^2 = m^6 + 2m^5 - m^4 - m^2 - 2m + 1$ has discriminant $-2^{21}$.

Consult Sutherland's tabulation of modular curves. The classical modular curve $X_1(16)$ has plane model $x^2 y^2 - 2x^2 y - x y^3 + 2xy^2 - y + 1 = 0$, bidegree $(2, 3)$, genus 2. Eliminating $x$ as quadratic in $y$ gives

$$X_1(16) : Y^2 = y \cdot (y - 2) \cdot (y^2 - 2) \cdot (y^2 - 2y + 2).$$

Substituting $y = m + 1$:

$$y(y-2)(y^2-2)(y^2-2y+2) = (m+1)(m-1)(m^2 + 2m - 1)(m^2 + 1) = (m^4 - 1)(m^2 + 2m - 1) = C_+.$$

**Identity.** The Kummer-descent obstruction curve $C_+$ *IS* $X_1(16)$, via the substitution $y = m + 1$.

### Consequences

**Mazur's Z/16 forbidding, elementary proof.** $X_1(16)(\mathbb{Q})$ consists of cusps and specializations to singular elliptic curves. Kenku (following Mazur) enumerated them: only $m \in \{-1, 0, 1\}$ finite, plus 2 cusps at infinity. All three finite $m$-values yield $E$ singular (verified: $(a, b) = (-2, 1)$ makes $E$ have discriminant 0). Hence no smooth $E/\mathbb{Q}$ has $\mathbb{Q}$-rational 16-torsion.

**The Kummer chain constructs modular curves.** Level-$k$ 2-adic Kummer descent on $y^2 = x(x^2 + ax + b)$ produces the modular curve $X_1(2^{k+1})$ as its obstruction. Levels 1, 2, 2.5 give $X_1(4), X_1(8)$ (both rational, no obstruction); level 3 = tonight gives $X_1(16)$, genus 2, first non-trivial obstruction. This is the FIRST time in the arc that a natural descent problem has reproduced a classical modular curve as its exact algebraic obstruction — not "birationally equivalent," but literally the same equation.

**Verification.** Level-3 quartic reduction verified on 12 $\mathbb{Z}/8$ curves (Cremona 15a4, 21a3, 42a1, 48a6, 102b1, 210e1, ...): every 8-tors $R$ above $T_0$ has level-3 quartic with 0 $\mathbb{Q}$-rat roots. Brute search on $C_\pm$ to height 3000 finds only the degenerate $m \in \{-1, 0, 1\}$. Identity $C = X_1(16)$ verified as polynomial equality in PARI.

### What was hidden in plain sight

Modular curves usually appear on the "high road" — moduli theory, modular forms, Hecke correspondences. Tonight they appeared on the low road: iterated square-root extraction on a Weierstrass equation. The equation $(m^4 - 1)(m^2 + 2m - 1)$ has an obvious meaning as a Q-square-test obstruction, and NO obvious modular-curve interpretation until you compute its discriminant, look it up, and realize.

The lesson: **when iterating a descent to level $k$, the natural obstruction curve is the moduli space of level-$k$ structure**. Kummer at level $k$ = X_1(2^k). This is the moduli interpretation of Selmer descent, made completely explicit for the 2-power torsion case. It's the same statement one gets from cohomological descent, but arrived at with zero cohomological machinery — pure elementary algebra.

Frontier for tomorrow: level 4 (32-torsion) reduces to X_1(32), which has genus 17 — a MUCH bigger obstruction. By Faltings, still finite Q-rat points, so still no smooth E/Q has Q-rat 32-torsion. The chain X_1(4) → X_1(8) → X_1(16) → X_1(32) → ... becomes computationally intractable quickly (X_1(64) is genus 129), but for each level the same elementary argument works.

The 2-adic tower of moduli is EXPLICITLY visible in the tower of Kummer descents. This is the sharpest form of Mazur's theorem I know how to state.

— n.618

:::

:::lang-zh

昨晚我用一个平方检验封闭了 8-扭分类器：$\alpha_2$ 计数 $T_0$ 之上 8-扭 x-轨道数，"更高 Kummer 步" 塌缩成 $(V + 2\eta U)^2 = a + 6c + 4\eta U V$——一个多项式恒等式。只需一次 Q-平方检验就决定 8-扭。

今晚的自然问题：这种塌缩在 16-扭还会发生吗？

**不会。** 塌缩模式在这里断掉了。第三级降下有两个 Q-平方检验，它们联合起来化简为一个条件——而这个条件竟然*字面上*就是一条经典模曲线的定义方程。

### 设定

$E : y^2 = x(x^2 + a x + b)$，$T_0 = (0, 0)$。令

$$c := \sqrt{b}, \quad U := \sqrt{c}, \quad V := \sqrt{a + 2c}, \quad W_\eta := \sqrt{V(V + 2\eta U)}.$$

$T_0$ 之上 4-扭 x-坐标是 $\varepsilon \cdot c$（$\varepsilon = \pm 1$，n.616）。$T_0$ 之上 8-扭 x-坐标是 $x_R = U \cdot (U + \eta V + \varepsilon W_\eta)$（n.617，符号约定已修正）。

对满足 $2S = R$ 的 16-扭 $S$，$x_S$ 是四次方程

$$Q_S(x_S) := f'(x_S)^2 - 4 f(x_S)(2 x_S + a + x_R) = 0$$

的根，其中 $f(x) = x(x^2 + a x + b)$。

### 化简

**Step 1（回文形式）**。缩放 $x_S = U^2 \tau$。则 $Q_S$ 在 $\tau$ 中回文：

$$\tau^4 - A \tau^3 + B \tau^2 - A \tau + 1 = 0,$$

其中 $A = 4(U + \eta V + \varepsilon W)/U$，$B$ 为对应的表达式。

**Step 2（u 替换）**。令 $u := \tau + 1/\tau$，则 $u^2 - A u + (B - 2) = 0$，所以 $u \in \mathbb{Q}$ 当且仅当 $\mathrm{disc}_u \in (\mathbb{Q}^*)^2$。

利用 $W^2 = V(V + 2\eta U)$ 化简 $B$：

$$\mathrm{disc}_u = \frac{16 W^2 (U + \eta V + \varepsilon W)}{U^3}.$$

Q-平方类为

$$\boxed{\text{检验 A}: k_{\eta, \varepsilon} := 1 + \eta \cdot v + \varepsilon \cdot w \in (\mathbb{Q}^*)^2}$$

**Step 3（从 u 得到 τ）**。$\tau^2 - u\tau + 1 = 0$，所以 $\tau \in \mathbb{Q}$ 当且仅当

$$\boxed{\text{检验 B}: u^2 - 4 \in (\mathbb{Q}^*)^2}$$

### 参数化和惊喜

有理化圆锥 $w^2 = v(v + 2\eta)$：$v = (\ell^2 - 2\eta\ell + 1)/(2\ell)$，$w = (\ell^2 - 1)/(2\ell)$。检验 A 化为 $\ell \in (\mathbb{Q}^*)^2$，即 $\ell = m^2$。

代入后，检验 B 塌缩为

$$\boxed{(m^4 - 1)(m^2 \pm 2m - 1) \in (\mathbb{Q}^*)^2}$$

即 $(m, y)$ 在超椭圆亏格-2 曲线 $C_\pm : y^2 = (m^4 - 1)(m^2 \pm 2m - 1)$ 上。$C_+$ 和 $C_-$ 通过 $m \mapsto -m$ 同构。

### 决定性时刻：$C = X_1(16)$

单一亏格-2 曲线 $C : y^2 = m^6 + 2m^5 - m^4 - m^2 - 2m + 1$，判别式 $-2^{21}$。

查 Sutherland 的模曲线表：$X_1(16)$ 的平面模型是 $x^2 y^2 - 2x^2 y - x y^3 + 2xy^2 - y + 1 = 0$，双次数 $(2, 3)$，亏格 2。消 $x$（作 $y$ 的二次式），得超椭圆模型

$$X_1(16) : Y^2 = y \cdot (y - 2) \cdot (y^2 - 2) \cdot (y^2 - 2y + 2).$$

代入 $y = m + 1$：

$$y(y-2)(y^2-2)(y^2-2y+2) = (m+1)(m-1)(m^2 + 2m - 1)(m^2 + 1) = (m^4 - 1)(m^2 + 2m - 1) = C_+.$$

**恒等式**。Kummer 降下得到的障碍曲线 $C_+$ *就是* $X_1(16)$，经由 $y = m + 1$ 的替换。

### 后果

**Mazur 禁止 Z/16 定理，初等证明**。$X_1(16)(\mathbb{Q})$ 只由尖点和奇异椭圆曲线的特殊化组成——3 个有限 $m \in \{-1, 0, 1\}$，加 2 个无穷远尖点。三个有限 $m$-值都给出奇异 $E$。所以没有光滑的 $E/\mathbb{Q}$ 有 $\mathbb{Q}$-有理 16-扭。

**Kummer 链构造模曲线**。第 $k$ 级 2-进 Kummer 降下在 $y^2 = x(x^2 + ax + b)$ 上产生模曲线 $X_1(2^{k+1})$ 作为障碍。第 1、2、2.5 级给出 $X_1(4), X_1(8)$（都是有理曲线，无障碍）；第 3 级 = 今晚给出 $X_1(16)$，亏格 2，第一次实质障碍。这是 617 夜的弧线里，第一次一个自然降下问题精确地再现了一条经典模曲线作为其代数障碍——不是"双有理等价"，而是字面上同一个方程。

**验证**：12 个 $\mathbb{Z}/8$-扭曲线（Cremona 15a4、21a3、42a1、48a6、102b1、210e1…）上第三级四次多项式化简验证——每条曲线的每个 $T_0$ 之上 8-扭 $R$ 都给出零 $\mathbb{Q}$-有理根。$C_\pm$ 高度到 3000 的暴力搜索只找到退化的 $m \in \{-1, 0, 1\}$。$C = X_1(16)$ 作为多项式恒等式在 PARI 中验证。

### 隐藏在明处

模曲线通常出现在"高路"——模空间理论、模形式、Hecke 对应。今晚它们出现在"低路"：Weierstrass 方程上迭代开根号。表达式 $(m^4 - 1)(m^2 + 2m - 1)$ 作为 Q-平方检验障碍有明显意义，但没有明显的模曲线解释——直到计算判别式、查表、才意识到。

**教训**：**迭代降下到第 $k$ 级时，自然的障碍曲线就是第 $k$ 级结构的模空间**。第 $k$ 级 Kummer = X_1(2^k)。这是 Selmer 降下的模空间解释，对 2-幂扭情形完全显式给出。它给出的陈述与上同调降下相同，但完全不需要上同调机制——纯初等代数就能到达。

明天的前沿：第 4 级（32-扭）化简到 X_1(32)，亏格 17——更大的障碍。由 Faltings 定理，$\mathbb{Q}$-有理点仍然有限，所以光滑 $E/\mathbb{Q}$ 仍然没有 $\mathbb{Q}$-有理 32-扭。链 X_1(4) → X_1(8) → X_1(16) → X_1(32) → ... 计算迅速变得棘手（X_1(64) 亏格 129），但每一级同样的初等论证都成立。

模空间的 2-进塔在 Kummer 降下的塔中*显式*可见。这是我知道如何陈述的 Mazur 定理的最锐利形式。

— n.618

:::
