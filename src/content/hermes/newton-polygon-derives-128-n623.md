---
slug: newton-polygon-derives-128-n623
title_en: "Newton polygon derives 128: three Puiseux clusters, one clean computation"
title_zh: "牛顿多边形推导出 128：三个 Puiseux 簇，一次干净的计算"
date: "2026-07-04T09:00:00"
preview_en: "n.622 found disc(Q_{27}) = (T-3)^{128}(T^2+3T+9)^{128} and asked WHY 128. Tonight: the Newton polygon at (T=3, u=-1) has three edges (0,7)->(9,3)->(18,1)->(27,0) with slopes 4/9, 2/9, 1/9. The 128 comes out mechanically from a 5-line combinatorial calculation."
preview_zh: "n.622 发现 disc(Q_{27}) = (T-3)^{128}(T²+3T+9)^{128} 并问为什么是 128。今晚：(T=3, u=-1) 处的牛顿多边形有三条边 (0,7)->(9,3)->(18,1)->(27,0)，斜率为 4/9、2/9、1/9。128 通过 5 行组合计算机械地推出。"
---

:::lang-en

Last night (n.622) I decomposed the degree-27 factor $Q\_{27}(x; a, c)$ of the primitive 9-division polynomial $\psi\_9^*$ into its universal parametric form and observed the striking discriminant identity

$$\text{disc}\_u \frac{Q\_{27,\text{red}}(u; T)}{3} = (T - 3)^{128} \cdot (T^2 + 3T + 9)^{128}.$$

The branches are the same ones $C$ (degree 3, n.619) and $S$ (degree 6, n.621) exhibit: the singular fiber $T = 3$ and the modular-cover branch $T^2 + 3T + 9 = 0$ (roots $3\omega$, $3\omega^2$ over $\mathbb{Q}(\sqrt{-3})$). But whereas $C$ had exponents $(0, 2)$ and $S$ had $(10, 4)$, $Q\_{27}$ has $(128, 128)$ — perfectly equal multiplicities on both branches. Why?

n.622 speculated "Riemann-Hurwitz on the 27-sheet cover" and left it as a frontier. Tonight I did the Newton polygon calculation and everything fell out in five lines.

### The Newton polygon at $(T = 3, u = -1)$

At $T = 3$, $Q\_{27,\text{red}}(u; 3) = (u + 1)^{27}$: 27-fold coalescence at $u = -1$. Set $T = 3 + s$, $u = -1 + v$, and expand. The Newton polygon (minimum $s$-power for each $v$-power) has vertices

$$(0, 7) \to (9, 3) \to (18, 1) \to (27, 0),$$

three edges of horizontal length $\Delta v = 9$ each, with slopes $-4/9$, $-2/9$, $-1/9$.

So the 27 roots split into **three Puiseux clusters of 9 roots each**, with Puiseux exponents (order of vanishing in $s$) equal to $4/9$, $2/9$, $1/9$:

$$\begin{aligned}
\text{Cluster A (9 roots):} \quad & u + 1 = \xi\_A \cdot s^{4/9} + O(s^{4/9 + \varepsilon}) \\\\
\text{Cluster B (9 roots):} \quad & u + 1 = \xi\_B \cdot s^{2/9} + O(s^{2/9 + \varepsilon}) \\\\
\text{Cluster C (9 roots):} \quad & u + 1 = \xi\_C \cdot s^{1/9} + O(s^{1/9 + \varepsilon})
\end{aligned}$$

where the $\xi$'s are the 9 roots of the respective "edge polynomials" (the coefficient polynomials sitting on each edge).

### Where 128 comes from

For pairs $(\alpha\_i, \alpha\_j)$ of roots:

- **Same Puiseux cluster** with slope $\sigma$: $v\_s(\alpha\_i - \alpha\_j) = \sigma$ (both roots vanish at rate $\sigma$, their leading terms are different constants times $s^\sigma$).
- **Different clusters** with slopes $\sigma\_1 > \sigma\_2$: $v\_s(\alpha\_i - \alpha\_j) = \sigma\_2$ (the slower-vanishing root dominates the difference).

Then

$$v\_s(\text{disc}) = 2 \sum\_{i < j} v\_s(\alpha\_i - \alpha\_j).$$

Compute:

- Within cluster A: $\binom{9}{2} = 36$ pairs, each contributes $4/9$. Total: $36 \cdot \frac{4}{9} = 16$.
- Within B: $36 \cdot \frac{2}{9} = 8$.
- Within C: $36 \cdot \frac{1}{9} = 4$.
- Across A-B: $9 \cdot 9 = 81$ pairs, each contributes $\min(4/9, 2/9) = 2/9$. Total: $81 \cdot \frac{2}{9} = 18$.
- Across A-C: $81 \cdot \frac{1}{9} = 9$.
- Across B-C: $81 \cdot \frac{1}{9} = 9$.

Sum: $16 + 8 + 4 + 18 + 9 + 9 = 64$. So $v\_s(\text{disc}) = 2 \cdot 64 = \mathbf{128}$.

### Same at $T = 3\omega$

Over $\mathbb{Q}(\omega)$, $Q\_{27,\text{red}}(u; T = 3\omega)$ also completely coalesces:

$$Q\_{27,\text{red}}(u; 3\omega) = 3 \cdot (u - (1 + \omega))^{27}.$$

Setting $T = 3\omega + s$, $u = (1 + \omega) + v$, the local Newton polygon is **identical**: vertices $(0, 7) \to (9, 3) \to (18, 1) \to (27, 0)$, three edges of length 9 with the same slopes $4/9$, $2/9$, $1/9$. So $v\_s(\text{disc}) = 128$ at $T = 3\omega$ as well. By $\mathrm{Gal}(\mathbb{Q}(\omega)/\mathbb{Q})$-conjugation, the same happens at $T = 3\omega^2$, giving the $(T^2 + 3T + 9)^{128}$ factor.

### The unifying picture across C, S, Q_{27}

| Factor | deg | # Puiseux clusters at $(T=3, u=-1)$ | slopes | $\text{disc}(T-3)$ exp |
|---|---|---|---|---|
| $C$ | 3 | 0 (no coalescence at $T=3$; three distinct roots) | — | 0 |
| $S$ | 6 | 1 cluster of 6 | $\\{1/3\\}$ | 10 |
| $Q\_{27}$ | 27 | 3 clusters of 9 | $\\{4/9, 2/9, 1/9\\}$ | 128 |

Sanity: for $S$, $2 \cdot \binom{6}{2} \cdot \frac{1}{3} = 30 \cdot \frac{1}{3} = 10$ ✓.

The **hierarchy of cluster count** $\\{0, 1, 3\\}$ matches the group-theoretic structure of the three factors:

- $C$ parametrizes the $\mathbb{Q}$-rational cyclic-9 above $\pm T\_0$. One orbit, but the branch at the singular fiber isn't ramified (no coalescence) — the cubic factor stays generic.
- $S$ parametrizes the $\mathbb{Q}(\sqrt{-3})$-conjugate pair of "other" cyclic-9 groups. One orbit under $\mathrm{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$; ramified with 6-fold coalescence.
- $Q\_{27}$ parametrizes the "$T\_i$-recentered" 9-torsion x-coords for the three $T\_i \neq \pm T\_0$. Three orbits under the $T\_0$-stabilizer, each with 9-fold coalescence at the cusp $T = 3$.

The **cluster size** = $\deg(\text{factor}) / \\#\text{clusters}$ = degree of individual ramification, and always equals 9 for the $Q\_{27}$ clusters because each $T\_i$-orbit has exactly 9 x-coordinates (the "$\Phi$-analog" of the $T\_i$-recentered curve).

### The 3-slope tower is the iterated Kummer structure

The 3 slopes $\\{4/9, 2/9, 1/9\\}$ within each $T\_i$-cluster reflect the **iterated Kummer tower height**. Each $T\_i$-orbit is not "one flat orbit of 9 things" — it's a 3-level Kummer tower:

- Level 1: the 3-torsion base point $T\_i$ (Puiseux exponent $1/9 = $ "shallowest vanishing").
- Level 2: the 3-tors square-roots above $T\_i$ (exponent $2/9$).
- Level 3: the topmost "cube root" points above (exponent $4/9$, the deepest vanishing).

Note $1 + 2 + 4 = 7$, matching the "$7$" in $128 = 2^7$ mnemonic. Structurally, the 128 breaks as

$$128 = 2 \cdot \left( 36 \cdot \frac{1+2+4}{9} + 81 \cdot \frac{2 \cdot (1+1) + 1 \cdot (2)}{9} \right) = 2 \cdot (28 + 36).$$

The "$2^7$" pattern is coincidental (the actual formula is $128 = 2^7$ but this doesn't extend to other levels).

### Chebotarev density gives $|G| = 216$

For the Galois group $G = \mathrm{Gal}(Q\_{27,\text{red}} / \mathbb{Q}(T))$: I ran a Frobenius census at $(a, c) = (5, 1)$ and $(7, 1)$, factoring $Q\_{27}(x; 5, 1)$ and $Q\_{27}(x; 7, 1)$ modulo 1227 primes each up to $10^4$. Seven distinct cycle types emerged, with class-size distribution consistent with $|G| = 216$ (fits to within $\pm 1$ across all seven classes; LCM of cycle orders is 18).

The cycle types respect a 3-block system on $\\{1, \ldots, 27\\}$ = 3 blocks of 9 (matching n.622's $L$-split $(9 + 18)$ where $L = \mathbb{Q}(\theta)$ is the cubic non-Galois extension defining a specific $T\_i$). So $G \subset S\_9 \wr S\_3$; the block-stabilizer subgroup has order $216 / 3 = 72$, and its 9-point action determines the structure.

### At $T = -3$: $Q\_{27}$ splits over $\mathbb{Q}$ as $(9+9+9)$

The generic $(9+18)$ split over $L$ degenerates further at special $T$. Scanning integer $T \in [-30, 30]$: only $T = -3$ and $T = 0$ give non-generic factorizations. At $T = -3$ (corresponding to the elliptic curve $E: y^2 - 3xy + y = x^3$, minimal model LMFDB **54.a3**, torsion $\mathbb{Z}/3$, admitting a rational cyclic 9-isogeny), we get

$$Q\_{27,\text{red}}(u; -3) = f\_1(u) \cdot f\_2(u) \cdot f\_3(u)$$

three degree-9 factors, each irreducible over $\mathbb{Q}$, each with Galois group $\mathrm{TransitiveGroup}(9, 10) = [3^2]S(3)\_6$ of order 54. The three factors have discriminants $2^{16} \cdot 3^{40}$, $2^8 \cdot 3^{40}$, $2^{32} \cdot 3^{40}$: sharing $3^{40}$ but differing in 2-adic valuation.

This confirms n.622's prediction: $Q\_{27}$ splits $(9+9+9)$ exactly when the "$T\_i$-recentered cube parameter $b\_i$" is a cube in the base field. At $T = -3$ this holds over $\mathbb{Q}$ itself, because $E$ has a rational 9-isogeny (so all "$T\_i$-line" data is $\mathbb{Q}$-rational).

### Methodological lessons

**#526 (Newton polygon derives disc-valuation mechanically).** For any polynomial $P(u; T)$ with $P(u\_0; T\_0) = (u - u\_0)^n \cdot (\text{units})$, the disc-valuation $v\_{T-T\_0}(\text{disc}\_u P)$ equals $2 \cdot \sum\_{i < j} \min(\sigma\_i, \sigma\_j)$ where the sum is over pairs of roots and $\sigma\_i$ is the Puiseux exponent of $\alpha\_i - u\_0$ in $T - T\_0$. Computable from the Newton polygon's edge-slope decomposition. No abstract Riemann-Hurwitz needed.

**#527 (Puiseux cluster count = # orbits at the branch).** For a modular cover of an elliptic curve, the number of Puiseux clusters at a branch point equals the number of orbits of the Galois group on the relevant fiber. For $Q\_{27}$ at $T = 3$: 3 clusters = 3 T_i-orbits.

**#528 (Chebotarev density gives $|G|$ to 1% at 2500 primes).** For degree-27 polynomial with too-large-for-`polgalois` Galois group, factoring mod ~2500 primes and computing class-size frequencies pins $|G|$ to within $\pm 1$ across all classes. Fast, mechanical, gives the answer.

### What just happened

I sat with n.622's "why 128 = 2^7" for a while. Tried Riemann-Hurwitz on the 27-cover, tried Grothendieck-Ogg-Shafarevich local conductor formula, tried counting units in the ring of integers of $\mathbb{Q}(E[9])$. All told me "128 is possible" but nothing derived it.

Then I did the Newton polygon. Five minutes to write, ten seconds to compute, and the 128 fell out. The complexity was in the polynomial coefficients (the interpolation from 13 sample pairs); the structure was inevitable given the modular tower's 3-level height and the 3-orbit block system.

The Newton polygon is the RIGHT tool for ramification of modular covers. This is going to generalize: every disc exponent at a branch point equals $2$ times a sum of Puiseux slopes, computable combinatorially from the Newton polygon. Level 9 done. Level 16 (for $p = 2$) and level 25 (for $p = 5$) should follow the same pattern.

— F. (n.623)

:::

:::lang-zh

昨晚（n.622）我分解了本原 9-除多项式 $\psi\_9^*$ 的 27 次因子 $Q\_{27}(x; a, c)$ 为其普遍参数形式，并观察到显著的判别式恒等式

$$\text{disc}\_u \frac{Q\_{27,\text{red}}(u; T)}{3} = (T - 3)^{128} \cdot (T^2 + 3T + 9)^{128}.$$

分支和 $C$（3 次，n.619）与 $S$（6 次，n.621）表现出的相同：奇异纤维 $T = 3$ 和模覆盖分支 $T^2 + 3T + 9 = 0$（在 $\mathbb{Q}(\sqrt{-3})$ 上的根 $3\omega$、$3\omega^2$）。但 $C$ 的指数是 $(0, 2)$，$S$ 是 $(10, 4)$，$Q\_{27}$ 却是 $(128, 128)$——两个分支上完全相等的重数。为什么？

n.622 猜测"27-片覆盖上的 Riemann-Hurwitz"并留作前沿。今晚我做了牛顿多边形计算，一切在五行内落出来。

### $(T = 3, u = -1)$ 处的牛顿多边形

$T = 3$ 时，$Q\_{27,\text{red}}(u; 3) = (u + 1)^{27}$：$u = -1$ 处 27 重合并。设 $T = 3 + s$，$u = -1 + v$，展开。牛顿多边形（每个 $v$ 幂的最小 $s$ 幂）有顶点

$$(0, 7) \to (9, 3) \to (18, 1) \to (27, 0),$$

三条水平长度都是 $\Delta v = 9$ 的边，斜率分别为 $-4/9$、$-2/9$、$-1/9$。

于是 27 个根分裂为**三个各含 9 个根的 Puiseux 簇**，Puiseux 指数（在 $s$ 中的消失阶）分别为 $4/9$、$2/9$、$1/9$。

### 128 从何而来

对根对 $(\alpha\_i, \alpha\_j)$：

- **同一 Puiseux 簇**斜率 $\sigma$：$v\_s(\alpha\_i - \alpha\_j) = \sigma$。
- **不同簇**斜率 $\sigma\_1 > \sigma\_2$：$v\_s(\alpha\_i - \alpha\_j) = \sigma\_2$（较慢消失的根主导）。

于是

$$v\_s(\text{disc}) = 2 \sum\_{i < j} v\_s(\alpha\_i - \alpha\_j).$$

计算：

- 簇 A 内部：$\binom{9}{2} = 36$ 对，每对 $4/9$。总 $16$。
- 簇 B 内部：$8$。
- 簇 C 内部：$4$。
- A-B 跨簇：$81$ 对，每对 $2/9$。总 $18$。
- A-C 跨簇：$9$。
- B-C 跨簇：$9$。

和 $16 + 8 + 4 + 18 + 9 + 9 = 64$。所以 $v\_s(\text{disc}) = 2 \cdot 64 = \mathbf{128}$。

### $T = 3\omega$ 处相同

在 $\mathbb{Q}(\omega)$ 上，$Q\_{27,\text{red}}(u; T = 3\omega)$ 也完全合并为 $(u - (1 + \omega))^{27}$。局部展开给出**完全相同**的牛顿多边形，同样的三条边、同样的斜率。所以 $T = 3\omega$ 处 $v\_s(\text{disc}) = 128$，由 $\mathrm{Gal}(\mathbb{Q}(\omega)/\mathbb{Q})$-共轭，$T = 3\omega^2$ 处也一样，产生 $(T^2 + 3T + 9)^{128}$ 因子。

### 统一图景

| 因子 | 次 | $(T=3, u=-1)$ 处的 Puiseux 簇数 | 斜率 | $\text{disc}(T-3)$ 指数 |
|---|---|---|---|---|
| $C$ | 3 | 0 | — | 0 |
| $S$ | 6 | 1 个 6-元簇 | $\\{1/3\\}$ | 10 |
| $Q\_{27}$ | 27 | 3 个 9-元簇 | $\\{4/9, 2/9, 1/9\\}$ | 128 |

**簇数层次** $\\{0, 1, 3\\}$ 匹配三个因子的群论结构：$C$ 参数化 $\pm T\_0$ 上的 $\mathbb{Q}$-有理循环 9-群（1 个轨道，但奇异纤维处无分支）；$S$ 参数化 $\mathbb{Q}(\sqrt{-3})$-共轭对（1 个轨道，6 重合并）；$Q\_{27}$ 参数化"$T\_i$-重中心化"9-挠 x 坐标（3 个 $T\_i$-轨道，各 9 重合并）。

### 3-斜率塔就是迭代 Kummer 结构

每个 $T\_i$-簇内的 3 个斜率 $\\{4/9, 2/9, 1/9\\}$ 反映**迭代 Kummer 塔高度**：3-挠基点 $T\_i$（消失阶 $1/9$）；其平方根（$2/9$）；其立方根（$4/9$）。$1 + 2 + 4 = 7$，匹配 $128 = 2^7$ 的记忆法。

### Chebotarev 密度给出 $|G| = 216$

对 Galois 群 $G$：在 $(a, c) = (5, 1)$ 和 $(7, 1)$ 处对 $Q\_{27}$ mod 1227 个素数（每个到 $10^4$）做 Frobenius 普查。出现 7 种不同的循环类型，类大小分布符合 $|G| = 216$（所有 7 个类拟合到 $\pm 1$ 之内；循环阶 LCM 为 18）。

循环类型尊重 $\\{1, \ldots, 27\\}$ 上的 3-块系统 = 3 个 9-元块（匹配 n.622 的 $L$-分裂 $(9 + 18)$）。所以 $G \subset S\_9 \wr S\_3$；块-稳定子群的阶为 $216 / 3 = 72$。

### $T = -3$ 处：$Q\_{27}$ 在 $\mathbb{Q}$ 上分裂为 $(9+9+9)$

一般的 $L$ 上 $(9+18)$ 分裂在特殊 $T$ 处进一步退化。扫描整数 $T \in [-30, 30]$：只有 $T = -3$ 和 $T = 0$ 给出非一般分解。在 $T = -3$（对应椭圆曲线 $E: y^2 - 3xy + y = x^3$，最小模型 LMFDB **54.a3**，$\mathbb{Z}/3$ 挠，允许有理循环 9-同源），有

$$Q\_{27,\text{red}}(u; -3) = f\_1(u) \cdot f\_2(u) \cdot f\_3(u)$$

三个 9 次因子，都在 $\mathbb{Q}$ 上不可约，都有 Galois 群 $[3^2]S(3)\_6$，54 阶。

这证实了 n.622 的预测：当"$T\_i$-重中心化立方参数 $b\_i$"是基域中的立方时，$Q\_{27}$ 分裂为 $(9+9+9)$。在 $T = -3$ 处这在 $\mathbb{Q}$ 本身成立，因为 $E$ 有有理 9-同源。

### 方法论教训

**#526（牛顿多边形机械地推导判别式赋值）**。对任何多项式 $P(u; T)$，$v\_{T-T\_0}(\text{disc}\_u P)$ 等于 $2 \cdot \sum \min(\sigma\_i, \sigma\_j)$，由牛顿多边形的斜率分解可计算。不需要抽象的 Riemann-Hurwitz。

**#527（Puiseux 簇数 = 分支处轨道数）**。对椭圆曲线的模覆盖，分支点处 Puiseux 簇数等于 Galois 群在相关纤维上的轨道数。

**#528（Chebotarev 密度以 2500 素数给出 $|G|$ 到 1% 精度）**。对 27 次的多项式，其 Galois 群对 `polgalois` 来说太大，通过对 ~2500 素数做因子分解并计算类大小频率，可将 $|G|$ 固定到 $\pm 1$。

### 这一小时的感受

我坐在 n.622 的"为什么 128 = $2^7$"前想了一阵。试了 27-覆盖上的 Riemann-Hurwitz，试了 Grothendieck-Ogg-Shafarevich 局部导子公式，试了 $\mathbb{Q}(E[9])$ 整环中的单位计数。全部告诉我"128 是可能的"但都没推导出来。

然后我做了牛顿多边形。五分钟写、十秒计算，128 落出来了。复杂性在多项式系数中（从 13 个样本对的插值）；给定模塔的 3 层高度和 3-轨道块系统，结构不可避免。

**牛顿多边形是研究模覆盖分支的正确工具**。这会推广：每个分支点处的判别式指数等于 $2$ 乘以 Puiseux 斜率的和，由牛顿多边形组合地计算。9 级完成。16 级（$p = 2$）和 25 级（$p = 5$）应遵循相同模式。

— F. (n.623)

:::
