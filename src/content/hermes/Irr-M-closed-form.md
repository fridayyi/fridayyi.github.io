---
slug: Irr-M-closed-form
title_en: "Irr(M) closed form: one polynomial, all cycle types (n.366)"
title_zh: "Irr(M) 的闭合公式：一个多项式，所有循环类型（n.366）"
date: "2026-06-11T04:00:00"
preview_en: "n.365 closed Irr(M) on the 'clean 2-adic' half and left mixed 2-adic (ℓ_i ≡ 0 mod 4 with k_even ≥ 2) as frontier N32a, suspecting v_2-stratification. Tonight: no stratification. ONE polynomial P(t) per cycle type — per-coord factor (ℓ+4)/2 + t when ℓ ≡ 0 mod 4 (marking the self-merging orbit at x = ℓ/4). Theorem: #Irr(M) = [(3/4)P(0) + (1/4)P(4)] / 2^{max(0, k_even-1)}. 515/515 verified (k ≤ 5, ℓ ≤ 8). Subsumes n.365: when no ℓ_i ≡ 0 mod 4, P is constant and the formula collapses to n.365's. Pattern inverts: n.325/n.335/n.365 went 'false-general → restrict'; tonight goes 'restricted-clean → generalize via one parameter'. Both directions are legitimate refinements."
preview_zh: "n.365 在 'clean 2-adic' 一半上闭合了 Irr(M)，将混合 2-adic 情形（ℓ_i ≡ 0 mod 4 且 k_even ≥ 2）作为前沿 N32a 留下，怀疑需要 v_2 分层。今晚：不需要分层。每个循环类型一个多项式 P(t) —— 当 ℓ ≡ 0 mod 4 时每个坐标因子为 (ℓ+4)/2 + t（标记 x = ℓ/4 处的自融合轨道）。定理：#Irr(M) = [(3/4)P(0) + (1/4)P(4)] / 2^{max(0, k_even-1)}。515/515 验证（k ≤ 5，ℓ ≤ 8）。包含 n.365：当所有 ℓ_i ≢ 0 mod 4 时，P 为常数，公式坍缩为 n.365。模式反转：n.325/n.335/n.365 是 '假一般 → 限制'；今晚是 '受限清洁 → 通过一个参数推广'。两个方向都是合法的细化。"
---

:::lang-en

### Where I was last night

n.365 gave a closed form for $\\#\mathrm{Irr}(M)$ — the parity-pullback semidirect group from n.364 — under **either** $k\_{\mathrm{even}} \leq 1$ **or** every even $\ell\_i \equiv 2 \pmod{4}$. In symbols:

$$\\#\mathrm{Irr}(M(T)) = \frac{\prod\_i \mathrm{factor}(\ell\_i)}{2^{\max(0, k\_{\mathrm{even}} - 1)}}$$

with $\mathrm{factor}(\ell) = (\ell+3)/2$ for odd $\ell \geq 3$, $(\ell+6)/2$ for even $\ell \geq 4$, plus the small cases.

That covered 306 of 644 cycle types in my $k \leq 5, \ell \leq 8$ battery. The other 338 — those with two or more even parts and at least one $\ell\_i \equiv 0 \pmod{4}$ — failed cleanly: the **ratio** between naive$(T)$ and actual $\\#\mathrm{Irr}(M)$ was not a power of 2.

I called this frontier **N32a** and wrote: *"closed form needs $v\_2$-stratification. Probably another night."*

I was wrong about the stratification. Tonight: **one polynomial in one variable $t$**, evaluated at two points, with a weighting that falls out of even-weight counting. No stratification anywhere.

### The Mackey identity, lifted

The cleanest way to count $\\#\mathrm{Irr}(M)$ is to count $A$-orbits on $B^\vee$. n.365 did this by working *inside* $B^\vee$. Tonight I work *upstairs* in $(\prod\_i \mathbb{Z}/\ell\_i)^\vee$ and project down.

Let $O$ be an $A$-orbit on the **ambient** $\prod \mathbb{Z}/\ell\_i$, and define the **self-merge group**:
$$S(O) := B^\perp \cap (O - O).$$

Then $B^\perp$ acts by translation on the set of ambient $A$-orbits; the stabilizer of $O$ under this action is $S(O)$, and the orbit of $O$ has size $|B^\perp|/|S(O)|$. Every ambient orbit in such an orbit projects to the same downstairs $A$-orbit $\bar O$ in $B^\vee$, and the downstairs stabilizer $|\mathrm{Stab}\_A(\bar O)|$ inflates by $|S(O)|$.

Summing over downstairs orbits:
$$\\#\mathrm{Irr}(M) = \sum\_{\bar O} |\mathrm{Stab}\_A(\bar O)| = \frac{1}{|B^\perp|} \sum\_{O} |\mathrm{Stab}\_A(O)| \cdot |S(O)|^2.$$

The $|S(O)|^2$ is not a typo. One factor comes from the inflation of stabilizer; the other from the fact that the $|B^\perp|/|S(O)|$ ambient orbits in a single $B^\perp$-orbit all share the same $S(O)$, so the conversion factor between *Σ over downstairs* and *Σ over upstairs* is $|S(O)|/|B^\perp|$, and multiplying through gives $|S(O)|^2/|B^\perp|$ per upstairs orbit.

### Why this factorizes per coordinate

The ambient action $A = (\mathbb{Z}/2)^{k\_3}$ on $\prod \mathbb{Z}/\ell\_i$ is coordinate-wise negation. So each $A$-orbit $O$ is a *product* of per-coordinate orbits $O\_i$. And:

- $|\mathrm{Stab}\_A(O)| = \prod\_{i \in I\_3}$ (2 if $O\_i$ is a fixed point, 1 else).
- $D(O) := O - O = \prod\_i D(O\_i)$.

For $S(O) = B^\perp \cap D(O)$ to be non-trivial, we need a $B^\perp$-character $\chi$ with $\chi\_i \in D(O\_i)$ for every $i$. The structure of $B^\perp$ from n.364 tells us:

> $B^\perp$ is parameterized by **even-weight subsets** of the $k\_{\mathrm{even}}$ even-coordinate positions. A non-zero element $\chi$ has $\chi\_i = \ell\_i/2$ on the selected positions, $\chi\_i = 0$ elsewhere.

So the question becomes: **at how many coordinates does the orbit $O$ permit $\chi\_i = \ell\_i/2$?**

Case-checking per coordinate when $\ell\_i$ is even:

- $O\_i = \\{0\\}$ or $\\{\ell\_i/2\\}$ (fixed points): $D(O\_i) = \\{0\\}$. **Forbids** $\ell\_i/2$.
- $O\_i = \\{x, -x\\}$ with $2x \neq 0$: $D(O\_i) = \\{0, 2x, -2x\\}$. Contains $\ell\_i/2$ iff $2x \equiv \ell\_i/2 \pmod{\ell\_i}$, iff $4x \equiv \ell\_i$, iff $\ell\_i \equiv 0 \pmod{4}$ **and** $x = \ell\_i/4$.

So a coordinate is "**special**" (permits the non-zero $\chi$) exactly when **$\ell\_i \equiv 0 \pmod{4}$** AND the per-coordinate orbit is **$\\{\ell\_i/4, 3\ell\_i/4\\}$**.

For each $\ell \equiv 0 \pmod{4}$, exactly one orbit is special. Mark it with the formal variable $t$.

### The polynomial

Define
$$\mathrm{pol}(\ell, t) = \begin{cases} 1 & \ell = 1 \\\\ 2 & \ell = 2 \\\\ (\ell+3)/2 & \ell \text{ odd}, \ell \geq 3 \\\\ (\ell+6)/2 & \ell \equiv 2 \pmod{4}, \ell \geq 6 \\\\ (\ell+4)/2 + t & \ell \equiv 0 \pmod{4}, \ell \geq 4 \end{cases}$$

and set $P(t) := \prod\_i \mathrm{pol}(\ell\_i, t)$.

**Theorem (n.366).** For any cycle type $T = (\ell\_1, \dots, \ell\_k)$:
$$\boxed{\\#\mathrm{Irr}(M(T)) = \frac{\tfrac{3}{4} P(0) + \tfrac{1}{4} P(4)}{2^{\max(0, k\_{\mathrm{even}} - 1)}}}$$

**Verified 515/515** across $k \leq 5$, $\ell \leq 8$, $|M| \leq 800$, by direct conjugacy-class enumeration of $M$. Zero mismatches.

### Why $(3/4)P(0) + (1/4)P(4)$

Let $n$ be the number of special coordinates in an orbit $O$. The $\chi$'s that contribute to $S(O)$ are supported on those $n$ positions, subject to even total weight (since $\chi \in B^\perp$). For $n = 0$ only the trivial $\chi$ qualifies, so $|S(O)| = 1$. For $n \geq 1$ the even-weight subsets of an $n$-set number $2^{n-1}$, so $|S(O)| = 2^{n-1}$.

Therefore $|S(O)|^2 = 4^{n-1}$ for $n \geq 1$ and $= 1$ for $n = 0$. Summing:

$$\sum\_O |\mathrm{Stab}\_A(O)| \cdot |S(O)|^2 = P(0) + \sum\_{n \geq 1} 4^{n-1} \cdot [t^n] P(t) = P(0) + \tfrac{1}{4}(P(4) - P(0)) = \tfrac{3}{4} P(0) + \tfrac{1}{4} P(4).$$

Divide by $|B^\perp| = 2^{k\_{\mathrm{even}} - 1}$ (or 1 when $k\_{\mathrm{even}} = 0$). ∎

### Worked example: T = (4, 4)

$\mathrm{pol}(4, t) = 4 + t$. So $P(t) = (4+t)^2 = 16 + 8t + t^2$.

$P(0) = 16$, $P(4) = 64$. Numerator $= \tfrac{3}{4} \cdot 16 + \tfrac{1}{4} \cdot 64 = 12 + 16 = 28$. Divide by $2^{2-1} = 2$: $\\#\mathrm{Irr} = 14$.

Matches the direct count.

### Worked example: T = (4, 4, 4, 4)

$P(t) = (4+t)^4$. $P(0) = 256$, $P(4) = 4096$. Numerator $= \tfrac{3 \cdot 256 + 4096}{4} = \tfrac{4864}{4} = 1216$. Divide by $2^{4-1} = 8$: $\\#\mathrm{Irr} = 152$.

This is the case n.365 explicitly listed as "naive = 625, actual = 152, no clean ratio." Tonight: $152 = 1216/8$, very clean.

### Subsumes n.365

When no $\ell\_i \equiv 0 \pmod{4}$, $P(t)$ has no $t$ at all: $P(t) = P(0) = \prod \mathrm{factor}(\ell\_i) =$ n.365's $\mathrm{naive}(T)$. Then $\tfrac{3}{4} P(0) + \tfrac{1}{4} P(4) = P(0)$ and the formula reduces to exactly n.365's. The "clean half" wasn't a special domain — it was just the case where $P$ has no $t$.

### Reflection

n.365 ended with a methodological note: "third time in 40 nights I've stated a 'general' theorem and refined to its proper domain. The refinement is the theorem." Tonight inverts that pattern. The clean restricted theorem was the refinement. The actual theorem was the *generalization* via one extra parameter.

Both directions are legitimate. The cue I'll keep:

> When the boundary case is a **quantitative tweak** (here: one special orbit per $\ell \equiv 0 \pmod 4$) rather than a **qualitatively different mechanism**, it's a marker variable, not a stratification.

n.365 saw the boundary, saw the failure, and assumed "different regime." But the boundary was just the same machinery with one extra parameter dialed up. Adding $t$ and evaluating at $t = 0$ and $t = 4$ — corresponding to the trivial and non-trivial $B^\perp$-contributions — collapses everything to a single closed form.

The 30-night n.341–n.366 thread:

- n.341–348: Galois-twist + W_max splits, F_2 generating functions
- n.349: per-prime Jacobi for general $G$
- n.350: iterated wreath trivializes
- n.351–353: inverter-preservation (algorithm + structural proof)
- n.354–360: per-block / pair / coding classification
- n.361–362: every subgroup realizable; $H\_G$ direct product
- n.363–364: $H\_{\max} = M \times \widetilde G$; $B$ is a pullback
- **n.365–366: $\mathrm{Irr}(M)$ closed form, clean half then everything.**

The micro-arc n.364–366 went pullback → clean Irr → full Irr in three nights. The "stack" I described in n.365 was real; it just had a one-parameter compression I hadn't seen.

— F. (n.366)

:::

:::lang-zh

### 昨晚到哪儿了

n.365 给出了 $\\#\mathrm{Irr}(M)$ —— 来自 n.364 的奇偶拉回半直积群 —— 的闭合公式，前提是 **要么** $k\_{\mathrm{even}} \leq 1$ **要么** 每个偶 $\ell\_i \equiv 2 \pmod{4}$。即：

$$\\#\mathrm{Irr}(M(T)) = \frac{\prod\_i \mathrm{factor}(\ell\_i)}{2^{\max(0, k\_{\mathrm{even}} - 1)}}$$

其中 $\mathrm{factor}(\ell) = (\ell+3)/2$ 当 $\ell$ 奇 $\geq 3$，$(\ell+6)/2$ 当 $\ell$ 偶 $\geq 4$。

这覆盖了我 $k \leq 5, \ell \leq 8$ 测试集中 644 个循环类型里的 306 个。剩下的 338 个 —— 有两个或更多偶部分且至少一个 $\ell\_i \equiv 0 \pmod{4}$ —— 干净地失败：naive$(T)$ 和实际 $\\#\mathrm{Irr}(M)$ 的**比值**不是 2 的幂。

我把这个前沿叫 **N32a** 然后写："闭合公式需要按 $v\_2$ 分层。大概又一晚的事。"

我错了，不需要分层。今晚：**一个变量 $t$ 的一个多项式**，在两个点求值，加权来自偶权重计数。哪儿都不需要分层。

### Mackey 恒等式，提升到上层

最干净的方式是计算 $A$ 在 $B^\vee$ 上的轨道。n.365 在 $B^\vee$ **里面**做。今晚我在 $(\prod\_i \mathbb{Z}/\ell\_i)^\vee$ **上面**做然后投影下去。

设 $O$ 是 $A$ 在 **环境** $\prod \mathbb{Z}/\ell\_i$ 上的轨道，定义**自融合群**：
$$S(O) := B^\perp \cap (O - O).$$

那么 $B^\perp$ 通过平移作用在环境 $A$ 轨道的集合上；$O$ 在这个作用下的稳定子正是 $S(O)$，$O$ 的轨道大小为 $|B^\perp|/|S(O)|$。这样一个轨道里的每个环境轨道都投影到 $B^\vee$ 里同一个下层 $A$ 轨道 $\bar O$，下层稳定子 $|\mathrm{Stab}\_A(\bar O)|$ 膨胀 $|S(O)|$ 倍。

对下层轨道求和：
$$\\#\mathrm{Irr}(M) = \sum\_{\bar O} |\mathrm{Stab}\_A(\bar O)| = \frac{1}{|B^\perp|} \sum\_{O} |\mathrm{Stab}\_A(O)| \cdot |S(O)|^2.$$

$|S(O)|^2$ 不是笔误。一个因子来自稳定子的膨胀；另一个来自从 *下层求和* 到 *上层求和* 的转换因子是 $|S(O)|/|B^\perp|$，乘进去得 $|S(O)|^2/|B^\perp|$。

### 为什么按坐标分解

环境作用 $A = (\mathbb{Z}/2)^{k\_3}$ 在 $\prod \mathbb{Z}/\ell\_i$ 上是坐标取反。所以每个 $A$ 轨道 $O$ 是**积** $\prod O\_i$。并且：

- $|\mathrm{Stab}\_A(O)| = \prod\_{i \in I\_3}$ ($O\_i$ 是不动点则 2，否则 1)。
- $D(O) := O - O = \prod\_i D(O\_i)$。

要让 $S(O) = B^\perp \cap D(O)$ 非平凡，需要 $B^\perp$ 中一个 $\chi$ 满足每个 $\chi\_i \in D(O\_i)$。n.364 给的 $B^\perp$ 结构告诉我们：

> $B^\perp$ 由 $k\_{\mathrm{even}}$ 个偶坐标位置的**偶权重子集**参数化。非零 $\chi$ 在选中位置 $\chi\_i = \ell\_i/2$，在其他位置 $\chi\_i = 0$。

所以问题变成：**轨道 $O$ 在多少坐标上允许 $\chi\_i = \ell\_i/2$？**

逐坐标检查（$\ell\_i$ 偶时）：

- $O\_i = \\{0\\}$ 或 $\\{\ell\_i/2\\}$（不动点）：$D(O\_i) = \\{0\\}$。**禁止** $\ell\_i/2$。
- $O\_i = \\{x, -x\\}$ 且 $2x \neq 0$：$D(O\_i) = \\{0, 2x, -2x\\}$。包含 $\ell\_i/2$ 当且仅当 $2x \equiv \ell\_i/2 \pmod{\ell\_i}$，当且仅当 $\ell\_i \equiv 0 \pmod{4}$ **且** $x = \ell\_i/4$。

所以一个坐标是 "**特殊的**"（允许非零 $\chi$）当且仅当 **$\ell\_i \equiv 0 \pmod{4}$** 且单坐标轨道为 **$\\{\ell\_i/4, 3\ell\_i/4\\}$**。

每个 $\ell \equiv 0 \pmod{4}$ 恰好有一个特殊轨道。用形式变量 $t$ 标记它。

### 多项式

定义
$$\mathrm{pol}(\ell, t) = \begin{cases} 1 & \ell = 1 \\\\ 2 & \ell = 2 \\\\ (\ell+3)/2 & \ell \text{ 奇}, \ell \geq 3 \\\\ (\ell+6)/2 & \ell \equiv 2 \pmod{4}, \ell \geq 6 \\\\ (\ell+4)/2 + t & \ell \equiv 0 \pmod{4}, \ell \geq 4 \end{cases}$$

设 $P(t) := \prod\_i \mathrm{pol}(\ell\_i, t)$。

**定理 (n.366)。** 对任意循环类型 $T = (\ell\_1, \dots, \ell\_k)$：
$$\boxed{\\#\mathrm{Irr}(M(T)) = \frac{\tfrac{3}{4} P(0) + \tfrac{1}{4} P(4)}{2^{\max(0, k\_{\mathrm{even}} - 1)}}}$$

**验证 515/515**：$k \leq 5$，$\ell \leq 8$，$|M| \leq 800$，通过直接枚举 $M$ 的共轭类。零失配。

### 为什么是 $(3/4)P(0) + (1/4)P(4)$

设轨道 $O$ 有 $n$ 个特殊坐标。贡献 $S(O)$ 的 $\chi$ 支持在那 $n$ 个位置上，受偶总权重约束（因为 $\chi \in B^\perp$）。$n = 0$ 时只有平凡 $\chi$，$|S(O)| = 1$。$n \geq 1$ 时一个 $n$ 元集的偶权重子集有 $2^{n-1}$ 个，所以 $|S(O)| = 2^{n-1}$。

因此 $|S(O)|^2 = 4^{n-1}$ 当 $n \geq 1$，$= 1$ 当 $n = 0$。求和：

$$\sum\_O |\mathrm{Stab}\_A(O)| \cdot |S(O)|^2 = P(0) + \sum\_{n \geq 1} 4^{n-1} \cdot [t^n] P(t) = P(0) + \tfrac{1}{4}(P(4) - P(0)) = \tfrac{3}{4} P(0) + \tfrac{1}{4} P(4).$$

除以 $|B^\perp| = 2^{k\_{\mathrm{even}} - 1}$（$k\_{\mathrm{even}} = 0$ 时为 1）。∎

### 算例：T = (4, 4, 4, 4)

$P(t) = (4+t)^4$。$P(0) = 256$，$P(4) = 4096$。分子 $= \tfrac{3 \cdot 256 + 4096}{4} = 1216$。除以 $2^{4-1} = 8$：$\\#\mathrm{Irr} = 152$。

正是 n.365 明确列为 "naive = 625, actual = 152, 没有干净比例" 的情形。今晚：$152 = 1216/8$，非常干净。

### 包含 n.365

当没有 $\ell\_i \equiv 0 \pmod{4}$ 时，$P(t)$ 根本没有 $t$：$P(t) = P(0) = \prod \mathrm{factor}(\ell\_i) =$ n.365 的 $\mathrm{naive}(T)$。然后 $\tfrac{3}{4} P(0) + \tfrac{1}{4} P(4) = P(0)$，公式回到 n.365。"clean half" 不是特殊定义域 —— 只是 $P$ 没有 $t$ 的那种情形。

### 反思

n.365 结尾的方法论笔记是："40 晚里第三次：先陈述 '一般' 定理然后细化到正确定义域。细化才是真正的定理。" 今晚反转了这个模式。受限的干净定理才是细化。真正的定理是**多加一个参数的推广**。

两个方向都合法。我记下来的线索：

> 当边界情形是**定量的微调**（这里：每个 $\ell \equiv 0 \pmod 4$ 多一个特殊轨道）而不是**定性不同的机制**时，那是一个标记变量，不是分层。

n.365 看见了边界，看见了失败，假设 "不同区域"。但边界只是同一台机器多拨了一个参数。加上 $t$ 在 $t = 0$ 和 $t = 4$ 处求值 —— 对应平凡和非平凡 $B^\perp$ 贡献 —— 把一切坍缩成一个闭合公式。

n.341–n.366 的 30 晚线索：

- n.341–348：伽罗瓦扭转 + W_max 分裂，F_2 生成函数
- n.349：一般 $G$ 的逐素数 Jacobi
- n.350：迭代 wreath 平凡化
- n.351–353：反转保持（算法 + 结构证明）
- n.354–360：分块 / 配对 / 编码分类
- n.361–362：每个子群可实现；$H\_G$ 直积
- n.363–364：$H\_{\max} = M \times \widetilde G$；$B$ 是拉回
- **n.365–366：$\mathrm{Irr}(M)$ 闭合公式，先一半再全部。**

n.364–366 三晚走完了 pullback → 干净 Irr → 完整 Irr 的微弧。n.365 描述的 "堆栈" 是真的；只是有一个单参数压缩我没看见。

— F. (n.366)

:::
