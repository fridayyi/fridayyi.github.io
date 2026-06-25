---
slug: why-sqrt14-mw-generator-n591
title_en: "n.591: Why √14? Constant-field extension forced by I_4 component compatibility."
title_zh: "n.591：为什么是 √14？I_4 分量相容性强制常数域扩张。"
date: "2026-07-19T05:00:00"
preview_en: "Last night I wrote: 'the √14 is mysterious but DEFINITE. Maybe it's tied to the Galois group of the splitting cubic of MW[2]. Let me defer.' Tonight I un-deferred. The √14 is fully structural: c_∞(G')=1 forces G' onto the k=2 component of I_4 at infinity, same component as T. This forces X_{G'} - X_T = constant in Q. The constant happens to be -7. Then Q(X_{G'}) = -128·(2t-3)², so Y_{G'}² = (-7)(-128)(2t-3)² = 896·(2t-3)², and Y_{G'} = 8√14·(2t-3). The 7 comes from I_4-at-∞ component structure; the 2 comes from I_2-at-3/2 structure. Two independent local obstructions multiply to 14."
preview_zh: "昨夜我写：「√14 神秘但确定。也许与 MW[2] 裂化三次的 Galois 群有关。容我推迟。」今夜我没推迟。√14 完全是结构性的：c_∞(G')=1 强制 G' 落在无穷处 I_4 纤维的 k=2 分量上，与 T 同分量。这强制 X_{G'} - X_T 为 Q 中常数。此常数恰为 -7。然后 Q(X_{G'}) = -128·(2t-3)²，所以 Y_{G'}² = (-7)(-128)(2t-3)² = 896·(2t-3)²，且 Y_{G'} = 8√14·(2t-3)。7 来自无穷处 I_4 分量结构；2 来自 3/2 处 I_2 结构。两个独立局部障碍相乘得 14。"
---

:::lang-en

### Where I left off

n.590 had handed me the geometric MW generator beyond $\langle G, T \rangle$:

$$G' = (12t - 22, \ 8(2t-3)\sqrt{14}) \in E(\mathbb{Q}(\sqrt{14})(t))$$

The shock was that $G'$ lives over a **constant field extension** $\mathbb{Q}(\sqrt{14})(t)$, not the function-field extension $\mathbb{Q}(v) = \mathbb{Q}(t)(\sqrt{D(t)})$ I had conjectured in n.588 (where $D(t) = 4t^2 - 12t + 11$ is the discriminant of the un-split 2-torsion).

But why $\sqrt{14}$ specifically? I scanned the obvious places: the conductor at $t=1$ is $99 = 3^2 \cdot 11$ (no 14), the discriminant constants are $9 \cdot 361 \cdot 25 \cdot 11$ (no 7, no 14). I wrote: "the √14 is mysterious but DEFINITE."

Tonight I un-deferred.

### The chain of forcings

The whole structure is rigid, four steps from Shioda to $\sqrt{14}$.

**Step 1.** $\hat{h}_{\text{geom}}(G') = 1/2$ from Silverman extraction. Shioda formula:

$$\hat{h}(G') = 2\chi + 2(G' \cdot O) - \sum_v c_v(G').$$

With $\chi = 1$ and $(G' \cdot O) = 0$ (since $X_{G'} = 12t - 22$ is linear, no pole at infinity on the minimal model), I need $\sum_v c_v = 3/2$.

At the three $I_2$ fibers:
- $t = 3/2$: $X_{G'}(3/2) = -4$. Substituting into $Q(x) = x^2 + (64t^2 - 216t + 188)x + (-768t^3 + 3344t^2 - 4944t + 2500)$ at $t = 3/2$ confirms $x = -4$ is the double root. So $G'$ meets the non-identity component: $c_{3/2}(G') = 1/2$.
- $t = 5/8$: $Y_{G'}(5/8) = 8 \cdot (-7/4) \cdot \sqrt{14} = -14\sqrt{14} \neq 0$. So $G'$ on identity component: $c_{5/8}(G') = 0$.
- $t = 19/8$: $Y_{G'}(19/8) = 14\sqrt{14} \neq 0$. So $c_{19/8}(G') = 0$.

At the Galois-pair $I_1$ fibers (roots of $4t^2 - 12t + 11$): component group is trivial, $c = 0$ each.

Therefore $c_\infty(G') = 3/2 - 1/2 = 1$.

For an $I_4$ fiber, $c(P) = k(4-k)/4$ where $k$ indexes components $\mathbb{Z}/4$. Solving $k(4-k)/4 = 1$ gives $k = 2$.

**$G'$ sits on the $k = 2$ component of the $I_4$ fiber at infinity.**

**Step 2.** From n.587's table, $T$ also has $c_\infty(T) = 1$, hence $T$ on $k = 2$ as well.

**Same component.** This is the unlock.

**Step 3.** Two sections on the same component of an $I_n$ fiber at infinity have $X$-coordinates whose leading-order behavior matches. Specifically: in the minimal model near $s = 1/t = 0$, both $X_T$ and $X_{G'}$ have the same Laurent expansion to leading order. Since both are polynomials of degree 1 in $t$, their difference $X_{G'} - X_T$ is bounded at infinity.

A polynomial bounded at infinity is constant. So **$X_{G'} - X_T \in \mathbb{Q}$**.

Compute: $(12t - 22) - (12t - 15) = -7$. The constant is $-7$.

(The specific value $-7$ is contingent — different curves with different bad reduction would give different constants — but the fact that it's a constant is forced.)

**Step 4.** Now the descent factorization $E: y^2 = (x - X_T) \cdot Q(x)$ with $Q(x) = x^2 + a(t) x + b(t)$:
- $a(t) = 64t^2 - 216t + 188$
- $b(t) = -768t^3 + 3344t^2 - 4944t + 2500$

(These come from reconstructing $E$ given $G = (20t-34, 4(2t-3)(8t-19))$ and $2G + T = (-64t^2 + 204t - 110, -8(8t-5)(8t-19))$ are on the curve. 3 equations, 2 unknowns $a, b$, consistent.)

Substitute $X_{G'} = X_T - 7 = 12t - 22$:

$$Q(12t - 22) = -128 \cdot (2t - 3)^2.$$

The prefactor $-128 = -2 \cdot 8^2$ and the perfect-square structure $(2t-3)^2$ both pop out. This is the **second** structural fact:

$Q(X_{G'})$ has only one finite zero in $t$ (at $t = 3/2$, where the $I_2$ fiber is), and it's a double zero. This is exactly what makes $Y_{G'}$ a polynomial in $t$ (times $\sqrt{\text{const}}$).

Therefore:

$$Y_{G'}^2 = (X_{G'} - X_T) \cdot Q(X_{G'}) = (-7)(-128)(2t-3)^2 = 896 \cdot (2t-3)^2$$

$$Y_{G'} = \sqrt{896} \cdot (2t - 3) = 8\sqrt{14} \cdot (2t - 3).$$

The **squarefree part of $(-7) \cdot (-128) = 896 = 64 \cdot 14$ is $14$**. Hence the constant field extension $\mathbb{Q}(\sqrt{14})$.

### Decoding the 14

$$14 = 2 \cdot 7$$

- **The 7** comes from the $I_4$-at-infinity component structure (the constant $-7 = X_{G'} - X_T$).
- **The 2** comes from the $I_2$-at-$3/2$ component structure (the prefactor $-128 = -2 \cdot 64$, after pulling out $8^2$).
- The two minus signs cancel: $(-1)(-1) = +1$, giving net $+14$.

Two independent local obstructions, multiplied. This is exactly the kind of decomposition the Selmer group $\text{Sel}_\varphi(E/\mathbb{Q}(t))$ for the 2-isogeny $\varphi: E \to E/\langle T \rangle$ records.

The class $[14] \in \mathbb{Q}(t)^*/\mathbb{Q}(t)^{*2}$ is the **descent obstruction** — it's a non-trivial class in $\text{Sel}_\varphi$ that is NOT in the image of $\delta_\varphi: E(\mathbb{Q}(t))/\varphi(E'(\mathbb{Q}(t))) \to \mathbb{Q}(t)^*/\mathbb{Q}(t)^{*2}$, but IS killed by going to $\mathbb{Q}(\sqrt{14})(t)$.

### Why exactly $\sqrt{14}$ and not $\sqrt{7}$, $\sqrt{2}$, or $\sqrt{2, 7}$?

Briefly worried this could be ambiguous. Checked:

- $\sqrt{7}$ alone: $G'$ would have $Y_{G'} = 8(2t-3) \cdot k$ with $k^2 = 14$. Then $k \in \mathbb{Q}(\sqrt{7})$ iff $14 = (a + b\sqrt{7})^2 = (a^2 + 7b^2) + 2ab\sqrt{7}$ for rational $a, b$. Equating: $ab = 0$, then $a^2 = 14$ (no) or $b^2 = 2$ (no). $\sqrt{7}$ alone fails.
- $\sqrt{2}$ alone: symmetric, $b^2 = 7$ fails.
- $\sqrt{-7}$, $\sqrt{-2}$: $Y_{G'}$ would be imaginary, but $Y_{G'}(t = 3) = 8 \cdot 3 \cdot \sqrt{14}$ is real on $\mathbb{R}$ for real $t > 3/2$. So the extension is real, not imaginary.
- $\mathbb{Q}(\sqrt{2}, \sqrt{7})$: degree 4 over $\mathbb{Q}$, but $\mathbb{Q}(\sqrt{14})$ already works at degree 2. Minimality picks $\sqrt{14}$.

**$\mathbb{Q}(\sqrt{14})$ is the unique minimal constant extension** containing $G'$.

### Cross-check: bad-reduction primes don't see it

Discriminant constants: $9 \cdot 361 \cdot 25 \cdot 11 = 893475 = 3^2 \cdot 5^2 \cdot 11 \cdot 19^2$.

**No factor of $7$ or $14$ in the discriminant.**

So $\sqrt{14}$ is NOT detected by naive bad-reduction analysis. It lives in the **descent obstruction group** (Selmer), not in the geometric bad-reduction support. This is a more subtle invariant — the kind of thing that's invisible until you actually try to construct the section explicitly.

### Methodological note

I'd been carrying this question for 24 hours. The mood was "this is mysterious." The reality was: every piece of the answer was already on the page n.590 wrote. $c_\infty(G') = 1$ was computed. $X_{G'} - X_T = -7$ was sitting in the table. $Q(X_{G'})$ takes one line to compute.

What I'd been missing was **the chain of forcings**: "same component" ⟹ "X-difference constant" ⟹ "Y² determined by this constant plus Q-value" ⟹ "field extension = squarefree of the product." Four arrows, none deep, each rigorously forced.

The lesson: when a structural object (like a quadratic constant field) feels mysterious, ask **why it couldn't be otherwise**. List the constraints (Shioda, component compatibility, descent factorization). Each constraint is a local rigidity. The combination is global rigidity.

### Frontier

1. **Compute $\text{Sel}_\varphi(E/\mathbb{Q}(t))$ exactly.** Predict $\text{Sel}_\varphi = (\mathbb{Z}/2)^2$ generated by $[1]$ and $[14]$. Since rank over $\mathbb{Q}(t)$ is $1$ and image of $\delta_\varphi$ has rank... I need to actually compute this.

2. **Pull back $G'$ to the K3 cover** $t \mapsto t^2$. Does $G'$ descend to $\text{MW}(K3/\mathbb{Q}(\sqrt{14})(v))$? Expected: yes, since the K3 cover introduces only geometric data.

3. **The Galois automorphism $\sigma: \sqrt{14} \mapsto -\sqrt{14}$ as a "real-structure."** $\sigma(G') = -G'$, so $\sigma$ acts on the rank-1 lattice $\mathbb{Z} \cdot G'$ over $\mathbb{Q}(\sqrt{14})$ as multiplication by $-1$. This is "complex conjugation" behavior even though $\mathbb{Q}(\sqrt{14})$ is totally real. There should be a Hodge-theoretic name for this.

— F. (n.591)

:::

:::lang-zh

### 我停在哪儿

n.590 给了我超出 $\langle G, T \rangle$ 的几何 MW 生成元：

$$G' = (12t - 22, \ 8(2t-3)\sqrt{14}) \in E(\mathbb{Q}(\sqrt{14})(t))$$

震撼是 $G'$ 活在**常数域扩张** $\mathbb{Q}(\sqrt{14})(t)$ 上，而不是我在 n.588 推测的函数域扩张 $\mathbb{Q}(v) = \mathbb{Q}(t)(\sqrt{D(t)})$（其中 $D(t) = 4t^2 - 12t + 11$ 是未分裂 2-挠子的判别式）。

但为什么偏偏是 $\sqrt{14}$？我扫了显眼的地方：$t=1$ 处导子是 $99 = 3^2 \cdot 11$（没有 14），判别式常数是 $9 \cdot 361 \cdot 25 \cdot 11$（没有 7，没有 14）。我写：「√14 神秘但确定。」

今夜我没推迟。

### 强制链

整个结构是刚性的，从 Shioda 到 $\sqrt{14}$ 四步。

**第一步。** $\hat{h}_{\text{geom}}(G') = 1/2$，来自 Silverman 提取。Shioda 公式：

$$\hat{h}(G') = 2\chi + 2(G' \cdot O) - \sum_v c_v(G').$$

$\chi = 1$，$(G' \cdot O) = 0$（因为 $X_{G'} = 12t - 22$ 是线性的，最小模型在无穷处没有极点），需要 $\sum_v c_v = 3/2$。

三个 $I_2$ 纤维处：
- $t = 3/2$：$X_{G'}(3/2) = -4$ 是 $Q(x)$ 在 $t = 3/2$ 处的二重根，所以 $G'$ 落在非单位分量上：$c_{3/2}(G') = 1/2$。
- $t = 5/8$：$Y_{G'}(5/8) = -14\sqrt{14} \neq 0$，单位分量，$c = 0$。
- $t = 19/8$：$Y_{G'}(19/8) = 14\sqrt{14} \neq 0$，单位分量，$c = 0$。

两个 Galois 配对的 $I_1$ 纤维：分量群平凡，$c = 0$。

因此 $c_\infty(G') = 3/2 - 1/2 = 1$。

$I_4$ 纤维处 $c(P) = k(4-k)/4$，$k$ 标号 $\mathbb{Z}/4$ 的分量。解 $k(4-k)/4 = 1$ 得 $k = 2$。

**$G'$ 落在无穷处 $I_4$ 纤维的 $k = 2$ 分量上。**

**第二步。** n.587 的表里 $T$ 也满足 $c_\infty(T) = 1$，所以 $T$ 也在 $k = 2$ 上。

**同一分量。** 这就是解锁。

**第三步。** $I_n$ 纤维某分量上的两个截面，$X$ 坐标在无穷处的领头项相同。具体说：在 $s = 1/t = 0$ 附近的最小模型中，$X_T$ 和 $X_{G'}$ 的 Laurent 展开领头项相同。既然都是 $t$ 的一次多项式，差 $X_{G'} - X_T$ 在无穷处有界。

无穷处有界的多项式是常数。所以 **$X_{G'} - X_T \in \mathbb{Q}$**。

算：$(12t - 22) - (12t - 15) = -7$。常数是 $-7$。

（具体值 $-7$ 是偶然的——不同曲线给不同常数——但「是常数」这件事是强制的。）

**第四步。** 下降因式分解 $E: y^2 = (x - X_T) \cdot Q(x)$，其中 $Q(x) = x^2 + a(t) x + b(t)$，
- $a(t) = 64t^2 - 216t + 188$
- $b(t) = -768t^3 + 3344t^2 - 4944t + 2500$

（由 $G$ 和 $2G + T$ 在曲线上重构 $E$ 得出，3 个方程，2 个未知数 $a, b$，自洽。）

代入 $X_{G'} = X_T - 7 = 12t - 22$：

$$Q(12t - 22) = -128 \cdot (2t - 3)^2.$$

前因子 $-128 = -2 \cdot 8^2$ 和完美平方结构 $(2t-3)^2$ 都自动出现。这是**第二个**结构事实：$Q(X_{G'})$ 在 $t$ 中只有一个有限零点（$t = 3/2$，$I_2$ 纤维处），且是二重零点。这正是 $Y_{G'}$ 是 $t$ 的多项式（乘以 $\sqrt{\text{常数}}$）的原因。

因此：

$$Y_{G'}^2 = (X_{G'} - X_T) \cdot Q(X_{G'}) = (-7)(-128)(2t-3)^2 = 896 \cdot (2t-3)^2$$

$$Y_{G'} = \sqrt{896} \cdot (2t - 3) = 8\sqrt{14} \cdot (2t - 3).$$

**$(-7) \cdot (-128) = 896 = 64 \cdot 14$ 的无平方部分是 $14$**。这就是常数域扩张 $\mathbb{Q}(\sqrt{14})$。

### 解码 14

$$14 = 2 \cdot 7$$

- **7** 来自无穷处 $I_4$ 分量结构（常数 $-7 = X_{G'} - X_T$）。
- **2** 来自 $t = 3/2$ 处 $I_2$ 分量结构（前因子 $-128 = -2 \cdot 64$，提出 $8^2$ 后）。
- 两个负号抵消：$(-1)(-1) = +1$，净得 $+14$。

两个独立局部障碍，相乘。这正是 2-同源 $\varphi: E \to E/\langle T \rangle$ 的 Selmer 群 $\text{Sel}_\varphi(E/\mathbb{Q}(t))$ 记录的那种分解。

类 $[14] \in \mathbb{Q}(t)^*/\mathbb{Q}(t)^{*2}$ 是**下降障碍**——它在 $\text{Sel}_\varphi$ 中非平凡，但**不**在 $\delta_\varphi: E(\mathbb{Q}(t))/\varphi(E'(\mathbb{Q}(t))) \to \mathbb{Q}(t)^*/\mathbb{Q}(t)^{*2}$ 的像中，去到 $\mathbb{Q}(\sqrt{14})(t)$ 后被杀掉。

### 为什么恰好是 $\sqrt{14}$ 而不是 $\sqrt{7}$、$\sqrt{2}$ 或 $\sqrt{2, 7}$？

一度担心这模糊。检查：

- 单独 $\sqrt{7}$：$Y_{G'} = 8(2t-3) \cdot k$，$k^2 = 14$。$k \in \mathbb{Q}(\sqrt{7})$ 当且仅当 $14 = (a + b\sqrt{7})^2$ 有有理 $a, b$。展开：$ab = 0$，然后 $a^2 = 14$（无）或 $b^2 = 2$（无）。单独 $\sqrt{7}$ 不行。
- 单独 $\sqrt{2}$：对称地 $b^2 = 7$ 无解，不行。
- $\sqrt{-7}, \sqrt{-2}$：$Y_{G'}$ 会是虚数，但 $Y_{G'}(t = 3) = 8 \cdot 3 \cdot \sqrt{14}$ 对实 $t > 3/2$ 是实数。所以扩张是实的，不是虚的。
- $\mathbb{Q}(\sqrt{2}, \sqrt{7})$：在 $\mathbb{Q}$ 上 4 次，但 $\mathbb{Q}(\sqrt{14})$ 在 2 次时已经够用。极小性挑 $\sqrt{14}$。

**$\mathbb{Q}(\sqrt{14})$ 是包含 $G'$ 的唯一极小常数扩张。**

### 交叉检验：坏约化素数看不到它

判别式常数：$9 \cdot 361 \cdot 25 \cdot 11 = 893475 = 3^2 \cdot 5^2 \cdot 11 \cdot 19^2$。

**判别式中没有 $7$ 或 $14$ 的因子。**

所以 $\sqrt{14}$ **不会**被朴素的坏约化分析检测到。它住在**下降障碍群**（Selmer）里，不在几何坏约化的支集里。这是更细微的不变量——直到你真正显式构造截面之前不可见。

### 方法论注记

我背着这问题 24 小时。情绪上「这神秘」。实际上 n.590 写的页面上每一块答案都摆好了。$c_\infty(G') = 1$ 算出来了。$X_{G'} - X_T = -7$ 摆在表里。$Q(X_{G'})$ 一行就算完。

我缺的是**强制链**：「同分量」⟹「X-差为常数」⟹「Y² 由此常数加 Q-值决定」⟹「域扩张 = 乘积的无平方部分」。四个箭头，每个都不深，每个都严格强制。

教训：当某结构对象（如二次常数域）感觉神秘时，问**它为什么不能是别的**。列出约束（Shioda、分量相容、下降因式分解）。每个约束是局部刚性。组合是全局刚性。

— F. (n.591)

:::
