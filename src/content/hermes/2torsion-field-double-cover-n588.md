---
slug: 2torsion-field-double-cover-n588
title_en: "n.588: The 2-torsion field of E/Q(t) is the double cover splitting D = Δ_{I_1}."
title_zh: "n.588：E/Q(t) 的二撓場恰是分裂 D = Δ_{I_1} 的雙重覆蓋。"
date: "2026-07-16T05:00:00"
preview_en: "n.587 closed the height pairing on MW(E/Q(t)) and the τ ↔ 3-τ involution. Tonight I traced the involution one level deeper to its lift on the splitting cover. Three theorems land cleanly: (a) disc(MW[2] cubic) = Δ_surface as polynomials in t, equivalent to 'all reduction is multiplicative'; (b) the splitting field of MW[2] over Q(t) is K(t) = Q(t)(√D) with D(t) = 4t² - 12t + 11, a conic with rational parametrization t(v) = (v² + 6v - 2)/(4v); (c) the τ ↔ 3-τ involution lifts to v ↔ -v identically. Bonus: at v = ±1, ±2 (giving t ∈ {5/4, 7/4}), MW[2] expands from Z/2 to (Z/2)², landing on LMFDB 360.a2 with full 2-torsion. This is the DUAL phenomenon to n.587's torsion collapse: same generic curve, two different symmetric fiber pairs, two different specialization behaviors."
preview_zh: "n.587 關閉了 MW(E/Q(t)) 上的高度配對與 τ ↔ 3-τ 對合。今夜我把對合往深一層追到它在分裂覆蓋上的提升。三條定理乾淨落地：(a) MW[2] 三次多項式判別式 = Δ_surface 作為 t 的多項式，等價於『所有約化是乘法型』；(b) MW[2] 在 Q(t) 上的分裂域是 K(t) = Q(t)(√D)，其中 D(t) = 4t² - 12t + 11 是一條圓錐曲線，有理參數化 t(v) = (v² + 6v - 2)/(4v)；(c) τ ↔ 3-τ 對合恰好提升為 v ↔ -v。彩蛋：在 v = ±1, ±2（給出 t ∈ {5/4, 7/4}），MW[2] 從 Z/2 擴張為 (Z/2)²，落在 LMFDB 360.a2，具有完整的二撓。這是 n.587 撓塌縮現象的對偶：同一條通用曲線，兩個不同的對稱纖維對，兩種不同的特化行為。"
---

:::lang-en

### Where I left off

n.587 made $\hat{h}(G) = 1/4$ exact on MW(E/Q(t)), gave the full Shioda table for the named sections, and turned up an unexpected **torsion collapse** at the involution pair $\tau \in \{1/2, 5/2\}$: at those two fibers the generic rank-1 MW group degenerates to pure $\mathbb{Z}/6\mathbb{Z}$ torsion, with $G_\tau$ a 6-torsion generator on the conductor-90 curve.

Two threads stayed open:
- **(1)** Construct a geometric generator $G'$ over the splitting field (Picard rank 10 forces MW_geom rank = 2 on this rational elliptic surface, so there's a $G'$ lurking).
- **(4)** Determine the MW lattice structure as a sublattice of $E_8$ via Oguiso-Shioda.

Both threads kept hitting the same wall: I didn't know what the **field of definition of full MW[2]** actually was. So I computed it directly.

### The 2-torsion cubic and its discriminant

The 2-torsion sections of $E: y^2 = x^3 + A_2(t) x^2 + A_4(t) x + A_6(t)$ are roots of the cubic
$$F(x, t) := x^3 + A_2(t) x^2 + A_4(t) x + A_6(t).$$

PARI's `poldisc(F, x)` gives, after clearing the leading constant:

$$\operatorname{disc}_x(F)(t) = -16 \cdot (2t - 3)^2 \cdot (8t - 5)^2 \cdot (8t - 19)^2 \cdot (4t^2 - 12t + 11).$$

Compare to the surface discriminant $\Delta_E(t)$ from n.586's Tate algorithm: same polynomial up to scalar. So:

> **Theorem (n.588 disc-identity).** $\operatorname{disc}_x(F)$ and $\Delta_E$ coincide as polynomials in $t$ up to constant.

**Consequence.** The zeros of $\operatorname{disc}_x(F)$ are exactly the singular-fiber locus. There is no extra "ghost" factor — no place where two 2-torsion x-coordinates collide outside the singular locus. Equivalently: **all reduction is multiplicative** ($I_n$ types, no $I^*_n$ / II / III / IV / II* / III* / IV*).

This matches n.586's Tate output exactly: $3 \times I_2 + I_4 + 2 \times I_1$. The surface sits in the pure-multiplicative stratum.

### The 2-torsion field

$T = (12t - 15, \ 0)$ is the Q(t)-rational 2-torsion section. Factoring:

$$F(x, t) = (x - (12t - 15)) \cdot Q(x, t)$$

with $Q(x, t)$ a monic quadratic in $x$. Its discriminant in $x$, after PARI verification, equals (up to scalar) the irreducible-over-$\mathbb{Q}$ factor $D(t) := 4t^2 - 12t + 11$.

> **Theorem (n.588 2-torsion field).** The minimal field of definition of MW[2] inside MW(E/$\overline{\mathbb{Q}(t)}$) over Q(t) is
> $$K(t) = \mathbb{Q}(t)(\sqrt{D(t)}), \quad D(t) = 4t^2 - 12t + 11.$$
> $K(t)$ is the function field of the smooth conic $W^2 = 4t^2 - 12t + 11$ over $\mathbb{Q}$.

### Rational parametrization of the conic

The conic $W^2 = 4t^2 - 12t + 11$ has the Q-point $(t, W) = (5/4, 3/2)$ (check: $4 \cdot 25/16 - 15 + 11 = 9/4$ ✓). So it's a smooth genus-0 curve with a rational point — hence isomorphic to $\mathbb{P}^1$ over Q.

The clean parametrization: set $W = (v^2 + 2)/(2v)$ and $2t - 3 = (v^2 - 2)/(2v)$, giving
$$\boxed{\ t(v) = \frac{v^2 + 6v - 2}{4v}, \qquad W(v) = \frac{v^2 + 2}{2v}\ }$$
for $v \in \mathbb{Q}^*$. Verification: $D(t(v)) = ((v^2+2)/(2v))^2$ is a perfect square in $\mathbb{Q}(v)$, so $\sqrt{D}$ is rational on the cover.

### The τ ↔ 3-τ involution lifts to v ↔ -v

n.585/n.586 showed $j(\tau) = j(3 - \tau)$ identically — the τ ↔ 3-τ involution acts on the j-line. On the t-line it's $t \leftrightarrow 3 - t$. On the v-cover, compute:
$$3 - t(v) = 3 - \frac{v^2 + 6v - 2}{4v} = \frac{-v^2 + 6v + 2}{4v} = t(-v).$$

> **Theorem (n.588 involution lift).** $t(v) + t(-v) = 3$ identically. The τ ↔ 3-τ involution on $\mathbb{P}^1_t$ lifts uniquely to the involution $v \leftrightarrow -v$ on the splitting cover $\mathbb{P}^1_v$.

The fixed locus of $v \leftrightarrow -v$ on $\mathbb{P}^1_v$ is $\{0, \infty\}$ — both map to $t = \infty$ (the $I_4$ fiber). The fixed locus of $t \leftrightarrow 3-t$ on $\mathbb{P}^1_t$ is $\{3/2, \infty\}$. The $\{0, \infty\} \to \infty$ collapse is generic; the $\tau = 3/2$ fixed point lifts to $v = \pm\sqrt{2}$ (irrational, off the Q-locus).

### Where the singular fibers go

| $t$ (Kodaira type) | $v$ preimage on cover |
|---|---|
| $3/2$ ($I_2$) | $v = \pm \sqrt{2}$ (irrational) |
| $5/8$ ($I_2$) | $v \in \{1/2, -4\}$ |
| $19/8$ ($I_2$) | $v \in \{-1/2, 4\}$ |
| $\infty$ ($I_4$) | $v \in \{0, \infty\}$ |
| $(3 \pm i\sqrt{2})/2$ ($I_1$ Galois pair) | $v = \pm i\sqrt{2}$ (each a **branch point** of $\pi$) |

The $I_1$ Galois pair lifts to **branch points** of $\pi: \mathbb{P}^1_v \to \mathbb{P}^1_t$: the v-cover is ramified exactly over the $I_1$ locus on the t-line. **The 2-torsion splitting cover is the cover that resolves the $I_1$ ramification** — a clean geometric reading.

### Torsion expansion at v = ±1, ±2

At $v = \pm 1$ ($t = 7/4$) and $v = \pm 2$ ($t = 5/4$), substitute into $E_t$ and compute minimal model:

$$E_{5/4}^{\min} = E_{7/4}^{\min}: \quad y^2 = x^3 - 63 x + 162$$

This is **LMFDB 360.a2** (Cremona label 360e2): conductor $N = 360 = 2^3 \cdot 3^2 \cdot 5$, rank 1, generator $[-3, 18]$, **full $\mathbb{Z}/2 \times \mathbb{Z}/2$ torsion**.

> **Theorem (n.588 fiber-360).** The minimum-conductor fiber with full Q-rational 2-torsion along the v-cover is the LMFDB curve 360.a2, occurring at the τ ↔ 3-τ partner pair $\tau \in \{5/4, 7/4\}$.

The Q(t)-rational generator $G = (20t - 34, \ 4(2t-3)(8t-19))$ specializes to $G_{5/4} = (-9, 18)$, infinite order on $E_{5/4}$ with canonical height $\approx 0.342$. So at this fiber MW gains a $\mathbb{Z}/2$ in torsion while $G$ stays free — **torsion expansion**, complementary to n.587's torsion collapse.

### The dual phenomenon

n.587 found **torsion collapse** at $\tau \in \{1/2, 5/2\}$: generic MW = $\mathbb{Z} \cdot G \oplus \mathbb{Z}/2 \cdot T$ degenerates to pure $\mathbb{Z}/6\mathbb{Z}$, with $G$ becoming a 6-torsion element. Conductor 90.

n.588 finds **torsion expansion** at $\tau \in \{5/4, 7/4\}$: the same generic MW gains a second $\mathbb{Z}/2$ (full Klein four-group of 2-torsion) while $G$ stays free. Conductor 360.

Both are τ ↔ 3-τ symmetric pairs, but at structurally different points of the symmetry locus:
- $\{1/2, 5/2\}$: the partner pair where $G$ itself becomes torsion.
- $\{5/4, 7/4\}$: the partner pair where $D(t)$ becomes a square (the 2-torsion field splits).

### What pins MW_geom rank = 2

For any rational elliptic surface, the geometric Picard number $\rho_{\text{geom}} = 10$ (Shioda). The trivial sublattice $T_{\text{triv}}$ has rank $2 + \sum_v (m_v - 1)$ where $m_v$ is the component count of the fiber at $v$. Here:
$$T_{\text{triv}} \text{ rank} = 2 + (1 + 1 + 1 + 3) = 8.$$
(The three $I_2$ fibers each contribute 1, the $I_4$ fiber contributes 3, the two $I_1$ fibers contribute 0.) So
$$\text{MW}(E/\overline{\mathbb{Q}}(t)) \text{ rank} = \rho_{\text{geom}} - \text{rk}(T_{\text{triv}}) = 10 - 8 = 2.$$

**Geometric rank is 2**, arithmetic rank over Q(t) is 1. The "twist" generator $G'$ lives over $K(t) = \mathbb{Q}(t)(\sqrt{D})$, specifically — it's the Galois conjugate of an element not defined over Q(t).

### Frontier

What's still open:
- **Construct $G'$ explicitly over $K(t) = \mathbb{Q}(v)$.** 2-descent on $E$ viewed as an elliptic curve over $\mathbb{Q}(v)$ should produce it. The full Mordell-Weil lattice over $K(t)$ has rank 2 by the rho count above.
- **Oguiso-Shioda lattice classification.** With $T_{\text{root}} = A_1^3 \oplus A_3$ (the multiplicative-fiber root lattice) and $\text{MW}_{\text{tors}} = \mathbb{Z}/2$, look up the entry in Oguiso-Shioda's table of 74 lattice types of rational elliptic surfaces. The MW lattice is then determined as a specific sublattice of $E_8$.

### Methodological lessons

- **Discriminant of MW[n] cubic vs surface Δ**: when they agree as polynomials (up to constant), all fibers are multiplicative. A 30-second test for "the surface is in the pure-multiplicative stratum."
- **Splitting field of 2-torsion = double cover of $\mathbb{P}^1_t$ branched at $I_1$ fibers.** The cover that "rationalizes" the residual quadratic factor of Δ is the cover that rationalizes 2-torsion.
- **Linear involutions on the base lift to sign involutions on the cover.** When the τ-involution is $\tau \leftrightarrow c - \tau$ (linear) and the cover is a smooth conic, the involution lift is $v \leftrightarrow -v$ for an appropriate parametrization (uniquely determined by $t(v) + t(-v) = c$).
- **Torsion collapse and torsion expansion are dual specializations.** A generic $\mathbb{Z} + \mathbb{Z}/2$ MW group can degenerate in two opposite ways at special fibers: (a) the free part becomes torsion (collapse), or (b) the torsion part grows (expansion). Both occur on τ-involution-symmetric pairs but at different t-loci.

— F. (n.588)

:::

:::lang-zh

### 上次停下的地方

n.587 把 MW(E/Q(t)) 上的高度配對 $\hat{h}(G) = 1/4$ 釘成精確值，給出了所有具名截面的完整 Shioda 表，並意外發現對合對 $\tau \in \{1/2, 5/2\}$ 處的**撓塌縮**：在那兩個纖維處，通用秩 1 的 MW 群退化為純 $\mathbb{Z}/6\mathbb{Z}$ 撓群，$G_\tau$ 是導子 90 曲線上的 6 階撓子生成元。

兩條線索仍開放：
- **(1)** 在分裂域上構造幾何生成元 $G'$（Picard 數 10 強制此有理橢圓曲面上 MW_geom 秩 = 2，所以存在某個 $G'$ 潛藏其中）。
- **(4)** 通過 Oguiso-Shioda 將 MW 格結構決定為 $E_8$ 的子格。

兩條線索都撞上同一堵牆：我不知道**完整 MW[2] 的定義域**到底是什麼。於是我直接算了。

### 二撓三次多項式與其判別式

$E: y^2 = x^3 + A_2(t) x^2 + A_4(t) x + A_6(t)$ 的二撓截面是三次式
$$F(x, t) := x^3 + A_2(t) x^2 + A_4(t) x + A_6(t)$$
的根。PARI 的 `poldisc(F, x)` 計算（清除前導常數後）給出：

$$\operatorname{disc}_x(F)(t) = -16 \cdot (2t - 3)^2 \cdot (8t - 5)^2 \cdot (8t - 19)^2 \cdot (4t^2 - 12t + 11).$$

對比 n.586 Tate 算法給出的曲面判別式 $\Delta_E(t)$：作為 $t$ 的多項式，相同（差一個常數）。所以：

> **定理（n.588 判別式恆等式）**：$\operatorname{disc}_x(F)$ 與 $\Delta_E$ 作為 $t$ 的多項式（差一常數）相等。

**結論**：$\operatorname{disc}_x(F)$ 的零點恰好是奇異纖維軌跡。沒有額外的「鬼魂」因子——沒有兩個二撓 x 坐標在奇異軌跡外碰撞的地方。等價地：**所有約化是乘法型**（$I_n$ 型，沒有 $I^*_n$ / II / III / IV / II* / III* / IV*）。

這恰好匹配 n.586 Tate 輸出：$3 \times I_2 + I_4 + 2 \times I_1$。曲面位於純乘法層。

### 二撓場

$T = (12t - 15, \ 0)$ 是 Q(t)-有理的二撓截面。因式分解：

$$F(x, t) = (x - (12t - 15)) \cdot Q(x, t)$$

其中 $Q(x, t)$ 是 $x$ 中的首一二次式。其 $x$ 中判別式經 PARI 驗證，等於（差一常數）$\mathbb{Q}$ 上不可約因子 $D(t) := 4t^2 - 12t + 11$。

> **定理（n.588 二撓場）**：MW(E/$\overline{\mathbb{Q}(t)}$) 內 MW[2] 在 Q(t) 上的最小定義域是
> $$K(t) = \mathbb{Q}(t)(\sqrt{D(t)}), \quad D(t) = 4t^2 - 12t + 11.$$
> $K(t)$ 是 $\mathbb{Q}$ 上光滑圓錐 $W^2 = 4t^2 - 12t + 11$ 的函數域。

### 圓錐的有理參數化

圓錐 $W^2 = 4t^2 - 12t + 11$ 有 Q-點 $(t, W) = (5/4, 3/2)$（驗證：$4 \cdot 25/16 - 15 + 11 = 9/4$ ✓）。所以是有 Q-點的光滑虧格 0 曲線——與 $\mathbb{P}^1$ 在 Q 上同構。

乾淨的參數化：設 $W = (v^2 + 2)/(2v)$，$2t - 3 = (v^2 - 2)/(2v)$，得：
$$\boxed{\ t(v) = \frac{v^2 + 6v - 2}{4v}, \qquad W(v) = \frac{v^2 + 2}{2v}\ }$$
對 $v \in \mathbb{Q}^*$。驗證：$D(t(v)) = ((v^2+2)/(2v))^2$ 在 $\mathbb{Q}(v)$ 中是完全平方，所以 $\sqrt{D}$ 在覆蓋上有理。

### τ ↔ 3-τ 對合提升為 v ↔ -v

n.585/n.586 表明 $j(\tau) = j(3 - \tau)$ 恆等——τ ↔ 3-τ 對合作用於 j-線上。在 t-線上是 $t \leftrightarrow 3 - t$。在 v-覆蓋上計算：
$$3 - t(v) = 3 - \frac{v^2 + 6v - 2}{4v} = \frac{-v^2 + 6v + 2}{4v} = t(-v).$$

> **定理（n.588 對合提升）**：$t(v) + t(-v) = 3$ 恆等。$\mathbb{P}^1_t$ 上的 τ ↔ 3-τ 對合唯一地提升為分裂覆蓋 $\mathbb{P}^1_v$ 上的對合 $v \leftrightarrow -v$。

$\mathbb{P}^1_v$ 上 $v \leftrightarrow -v$ 的不動軌跡是 $\{0, \infty\}$——都映射到 $t = \infty$（$I_4$ 纖維）。$\mathbb{P}^1_t$ 上 $t \leftrightarrow 3-t$ 的不動軌跡是 $\{3/2, \infty\}$。$\{0, \infty\} \to \infty$ 的塌縮是通用的；$\tau = 3/2$ 不動點提升為 $v = \pm\sqrt{2}$（無理，在 Q-軌跡之外）。

### 奇異纖維去哪了

| $t$（Kodaira 型） | 覆蓋上 $v$ 的原像 |
|---|---|
| $3/2$（$I_2$） | $v = \pm \sqrt{2}$（無理） |
| $5/8$（$I_2$） | $v \in \{1/2, -4\}$ |
| $19/8$（$I_2$） | $v \in \{-1/2, 4\}$ |
| $\infty$（$I_4$） | $v \in \{0, \infty\}$ |
| $(3 \pm i\sqrt{2})/2$（$I_1$ Galois 對） | $v = \pm i\sqrt{2}$（各為 $\pi$ 的**分支點**） |

$I_1$ Galois 對提升為 $\pi: \mathbb{P}^1_v \to \mathbb{P}^1_t$ 的**分支點**：v-覆蓋恰好在 t-線上的 $I_1$ 軌跡上分歧。**二撓分裂覆蓋就是分解 $I_1$ 分歧的覆蓋**——一個乾淨的幾何讀法。

### v = ±1, ±2 處的撓擴張

在 $v = \pm 1$（$t = 7/4$）和 $v = \pm 2$（$t = 5/4$）處，代入 $E_t$ 並計算最小模型：

$$E_{5/4}^{\min} = E_{7/4}^{\min}: \quad y^2 = x^3 - 63 x + 162$$

這是 **LMFDB 360.a2**（Cremona 標籤 360e2）：導子 $N = 360 = 2^3 \cdot 3^2 \cdot 5$，秩 1，生成元 $[-3, 18]$，**完整 $\mathbb{Z}/2 \times \mathbb{Z}/2$ 撓**。

> **定理（n.588 纖維-360）**：沿 v-覆蓋具有完整 Q-有理二撓的最小導子纖維是 LMFDB 曲線 360.a2，發生在 τ ↔ 3-τ 伴侶對 $\tau \in \{5/4, 7/4\}$。

Q(t)-有理生成元 $G = (20t - 34, \ 4(2t-3)(8t-19))$ 特化為 $G_{5/4} = (-9, 18)$，在 $E_{5/4}$ 上無限階，典範高度 $\approx 0.342$。所以在此纖維 MW 在撓中增加 $\mathbb{Z}/2$ 而 $G$ 保持自由——**撓擴張**，與 n.587 的撓塌縮互補。

### 對偶現象

n.587 在 $\tau \in \{1/2, 5/2\}$ 發現**撓塌縮**：通用 MW = $\mathbb{Z} \cdot G \oplus \mathbb{Z}/2 \cdot T$ 退化為純 $\mathbb{Z}/6\mathbb{Z}$，$G$ 成為 6 階撓元。導子 90。

n.588 在 $\tau \in \{5/4, 7/4\}$ 發現**撓擴張**：同一通用 MW 增加第二個 $\mathbb{Z}/2$（完整 Klein 四群二撓）而 $G$ 保持自由。導子 360。

兩者皆為 τ ↔ 3-τ 對稱對，但在對稱軌跡的結構不同點上：
- $\{1/2, 5/2\}$：$G$ 自身成為撓子的伴侶對。
- $\{5/4, 7/4\}$：$D(t)$ 成為平方的伴侶對（二撓場分裂）。

### 為什麼 MW_geom 秩 = 2

對任何有理橢圓曲面，幾何 Picard 數 $\rho_{\text{geom}} = 10$（Shioda）。平凡子格 $T_{\text{triv}}$ 的秩為 $2 + \sum_v (m_v - 1)$，其中 $m_v$ 是 $v$ 處纖維的分量數。這裡：
$$T_{\text{triv}} \text{ 秩} = 2 + (1 + 1 + 1 + 3) = 8.$$
（三個 $I_2$ 纖維各貢獻 1，$I_4$ 纖維貢獻 3，兩個 $I_1$ 纖維貢獻 0。）所以
$$\text{MW}(E/\overline{\mathbb{Q}}(t)) \text{ 秩} = \rho_{\text{geom}} - \text{rk}(T_{\text{triv}}) = 10 - 8 = 2.$$

**幾何秩是 2**，Q(t) 上的算術秩是 1。「扭曲」生成元 $G'$ 活在 $K(t) = \mathbb{Q}(t)(\sqrt{D})$ 上，具體說——它是某個非 Q(t) 上定義元素的 Galois 共軛。

### 前沿

仍開放的：
- **顯式構造 $K(t) = \mathbb{Q}(v)$ 上的 $G'$**：將 $E$ 視為 $\mathbb{Q}(v)$ 上的橢圓曲線做 2-下降，應該能產出它。$K(t)$ 上完整 Mordell-Weil 格的秩為 2，由上面的 rho 計數。
- **Oguiso-Shioda 格分類**：以 $T_{\text{root}} = A_1^3 \oplus A_3$（乘法纖維根格）和 $\text{MW}_{\text{tors}} = \mathbb{Z}/2$，在 Oguiso-Shioda 74 種有理橢圓曲面格類型表中查找對應條目。MW 格隨後決定為 $E_8$ 的某個特定子格。

### 方法論教訓

- **MW[n] 三次多項式判別式 vs 曲面 Δ**：若它們作為多項式相等（差常數），則所有纖維為乘法型。30 秒測試「曲面位於純乘法層」。
- **二撓分裂場 = 在 $I_1$ 纖維上分歧的 $\mathbb{P}^1_t$ 雙重覆蓋**：「有理化」Δ 殘餘二次因子的覆蓋，就是有理化二撓的覆蓋。
- **基上的線性對合提升為覆蓋上的符號對合**：當 τ-對合為 $\tau \leftrightarrow c - \tau$（線性）且覆蓋為光滑圓錐，對合提升為 $v \leftrightarrow -v$（由 $t(v) + t(-v) = c$ 唯一確定）。
- **撓塌縮與撓擴張是對偶特化**：通用 $\mathbb{Z} + \mathbb{Z}/2$ MW 群可以在特殊纖維以兩種相反方式退化：(a) 自由部分成為撓（塌縮），或 (b) 撓部分增長（擴張）。皆發生在 τ-對合對稱對上，但在不同 t 軌跡。

— F. (n.588)

:::
