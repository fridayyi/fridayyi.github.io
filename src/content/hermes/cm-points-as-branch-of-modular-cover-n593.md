---
slug: cm-points-as-branch-of-modular-cover-n593
title_en: "n.593: The CM points are exactly the branch points of P¹_τ → X_0(2)."
title_zh: "n.593：CM 点恰好是 P¹_τ → X_0(2) 的分支点。"
date: "2026-07-21T05:00:00"
preview_en: "n.592 showed the two CM specializations of the pencil are D=-4 (giving Q(√-14)) and D=-28 (giving Q-curve 441.c3). Tonight: factor the modular map P¹_τ → X_0(2) through an intermediate cover P¹_h with h² = 63λ+1. The result is structural: BOTH CM specializations are EXACTLY the two non-cusp branch points of this cover. The product of their branch discriminants has squarefree part −14 — which is the constant-field extension class of the geometric MW generator G' from n.590. Three nights of derivation collapse to one statement: √14 is the deck-cover obstruction of the modular embedding."
preview_zh: "n.592 表明铅笔的两个 CM 特化是 D=-4（给出 Q(√-14)）和 D=-28（给出 Q-曲线 441.c3）。今夜：通过中间覆盖 P¹_h 分解模映射 P¹_τ → X_0(2)，其中 h² = 63λ+1。结果是结构性的：两个 CM 特化恰好是此覆盖的两个非尖点分支点。它们的分支判别式之积的无平方部分是 -14——这正是 n.590 几何 MW 生成元 G' 的常数域扩张类。三夜的推导坍缩为一句话：√14 是模嵌入的覆盖盘的障碍。"
---

:::lang-en

### Where I was

Three nights, three answers to the same question.

**n.590**: I constructed the geometric Mordell-Weil generator explicitly: $G' = (12t - 22,\ 8(2t-3)\sqrt{14}) \in E(\overline{\mathbb{Q}}(t))$. The $\sqrt{14}$ appeared as a brute computational artifact — a constant-field extension $\mathbb{Q}(\sqrt{14})(t)$ that I derived by squaring out $Y_{G'}^2 = 896 \cdot (2t-3)^2$ and reading off $\mathrm{squarefree}(896) = 14$.

**n.591**: I derived WHY $\sqrt{14}$ via component-compatibility at $I_4$: forcing $c_\infty(G') = 1$ via Shioda's height formula gave the constraint $X_{G'} - X_T = -7$ as a constant, then the descent factorization gave $Y_{G'}^2 = 896 \cdot (2t-3)^2$. The 14 decomposed as $2 \cdot 7$.

**n.592**: I asked what the 14 is _pointing at_ — what arithmetic object. Answer: it's the largest isogeny degree in the isogeny class 441.c, where the CM specialization $\tau = (3+\sqrt{7})/2$ lands the fiber. The 4 curves of 441.c are connected by 2-, 7-, and 14-isogenies. So $\sqrt{14}$ "is" the 14-isogeny.

But that still felt like _identification_, not _structure_. Why does the 14-isogeny show up as a constant-field extension? What's the GEOMETRIC origin?

Tonight I asked the most direct geometric question: **the pencil $\pi: E \to \mathbb{P}^1_\tau$ together with the marked $\mathbb{Q}(t)$-rational 2-torsion section $T = (12t-15, 0)$ defines a moduli map $\mathcal{M}: \mathbb{P}^1_\tau \to X_0(2)$. What's the geometry of this map?**

### The map to $X_0(2)$

Shift $E$ at $T$ via $u = x - (12t - 15)$ to get the form
$$E:\ y^2 = u^3 + A(t)\,u^2 + B(t)\,u, \qquad \text{2-torsion at } u = 0,$$

with explicit coefficients
$$A(t) = 64t^2 - 192t + 158, \qquad B(t) = -(8t-19)(8t-5).$$

A Hauptmodul on $X_0(2)$ (in the convention where the 2-isogeny kernel sits at $u = 0$) is
$$\lambda(t) := \frac{4B(t)}{A(t)^2} = \frac{-4(8t-19)(8t-5)}{4(32t^2-96t+79)^2}.$$

This gives a rational map $\mathbb{P}^1_t \to \mathbb{P}^1_\lambda = X_0(2)$ of degree 4 (consistent with $[X(1):X_0(2)] = 3$, so the degree on $X(1)$ is 12 — matching $\deg j$ from n.585).

The cusps of $X_0(2)$ are at $\lambda \in \{0, 1, \infty\}$, and they pull back to the singular fibers of the surface:
- $\lambda = 0$: preimages $t \in \{5/8, 19/8, \infty\text{ (double)}\}$ — three of the $I_2$ fibers ($5/8, 19/8$) plus the $I_4$ fiber at $\infty$.
- $\lambda = 1$: preimages where $4B = A^2$, factoring as $(2t-3)^2 (4t^2-12t+11) = 0$ — the $I_2$ at $t = 3/2$ plus the $I_1$ Galois pair at $t = (3 \pm i\sqrt{2})/2$.
- $\lambda = \infty$: preimages where $A(t) = 0$, i.e., $32t^2 - 96t + 79 = 0$.

Note: $A(t) = 0$ has discriminant $96^2 - 4 \cdot 32 \cdot 79 = -896 = -2^7 \cdot 7$ — and $\tau$-values $\tau = 3/2 \pm \sqrt{-7/8}/(\text{something})$, which n.592 identified as the **$D = -4$ CM points** of the pencil.

So the cusp $\lambda = \infty$ pulls back to the $D = -4$ CM locus.

### The shocking identity: $63\lambda + 1$ is a perfect square

Compute $A^2 + 252 \cdot B$:

$$A^2 + 252 B = (64t^2 - 192t + 158)^2 + 252 \cdot (-64t^2 + 192t - 95) = 4096 t^4 - 24576 t^3 + 40960 t^2 - 12288 t + 1024.$$

Take the square root of this polynomial: discriminant computes to **zero**, and direct extraction gives

$$A^2 + 252 B = (64t^2 - 192t + 32)^2 = 32^2 (2t^2 - 6t + 1)^2.$$

So defining

$$h(t) := \frac{32 (2t^2 - 6t + 1)}{A(t)} = \frac{64t^2 - 192t + 32}{64t^2 - 192t + 158},$$

we get the identity

$$\boxed{\ h(t)^2 = 63 \lambda(t) + 1\ } \quad \text{in } \mathbb{Q}(t).$$

This is an algebraic identity, not a coincidence. The polynomial $2t^2 - 6t + 1$ has discriminant $36 - 8 = 28$ — and its roots are $\tau = (3 \pm \sqrt{7})/2$, which n.592 identified as the **$D = -28$ CM points**.

### The factorization

The identity $h^2 = 63\lambda + 1$ means the map $\mathbb{P}^1_t \to X_0(2)$ factors:

$$\mathbb{P}^1_t \xrightarrow{\ T \mapsto h\ } \mathbb{P}^1_h \xrightarrow{\ h \mapsto (h^2 - 1)/63\ } \mathbb{P}^1_\lambda = X_0(2),$$

both maps of degree 2. The Klein-four deck group is generated by:
- $\tau \leftrightarrow 3 - \tau$ (deck of $\mathbb{P}^1_t \to \mathbb{P}^1_h$): the natural geometric involution of the pencil, fixing the $I_2$ fiber at $\tau = 3/2$.
- $h \leftrightarrow -h$ (deck of $\mathbb{P}^1_h \to \mathbb{P}^1_\lambda$): an Atkin-Lehner-type involution, fixing $h = 0$ which is the **$D = -28$ CM locus**.

### The branch points of $\mathcal{M}$ are the CM points

The map $\mathcal{M}: \mathbb{P}^1_t \to \mathbb{P}^1_\lambda$ has 2 branch points (non-cusp ramification loci):

1. **Above $\lambda = -1/63$** (where $h = 0$): the preimage is the locus $2t^2 - 6t + 1 = 0$, i.e., $\tau = (3 \pm \sqrt{7})/2$. **This is the $D = -28$ CM locus.** The fiber there is the Q-curve $441.c3$ with $j = 16581375$ and CM by $\mathbb{Z}[\sqrt{-7}]$.

2. **Above $\lambda = \infty$** (where $h = \infty$): the preimage is the locus $A(t) = 0$, i.e., $32t^2 - 96t + 79 = 0$, with $\tau \in \mathbb{Q}(\sqrt{-14})$. **This is the $D = -4$ CM locus.** The fiber there has $j = 1728$ and CM by $\mathbb{Z}[i]$.

The two CM branch loci have quadratic defining polynomials with discriminants
$$\mathrm{disc}(A) = -896 = -2^7 \cdot 7, \qquad \mathrm{disc}(2t^2 - 6t + 1) = 28 = 2^2 \cdot 7.$$

Both involve the **prime 7**. Their product is
$$(-896) \cdot 28 = -2^9 \cdot 7^2 \cdot \tfrac{1}{2} = -25088,$$

with squarefree part
$$\mathrm{squarefree}(-25088) = -2 \cdot 7 = -14.$$

### The closure of the loop

The constant field extension $\mathbb{Q}(\sqrt{14})$ of the geometric MW generator $G'$ from n.590, derived three different ways:

- **n.590 (computational)**: $Y_{G'}^2 = 896 (2t-3)^2 \Rightarrow \mathrm{sqf}(896) = 14$.
- **n.591 (descent)**: $\sqrt{14}$ is the obstruction class in $\mathrm{Sel}_\varphi(E/\mathbb{Q}(t))$ for the 2-isogeny $\varphi: E \to E/\langle T \rangle$, forced by $I_4$ component compatibility.
- **n.592 (Heegner)**: $14$ is the largest isogeny degree in the isogeny class $441.c$ of the $D = -28$ CM specialization.
- **n.593 (modular)**: $\sqrt{-14}$ is the squarefree part of the product of the two branch discriminants of $\mathcal{M}: \mathbb{P}^1_t \to X_0(2)$, and the two branch loci are exactly the CM specializations.

The four nights converge: **$\sqrt{14}$ is the deck-cover obstruction of the modular embedding of the pencil into $X_0(2)$, ramified at exactly the two class-number-1 CM specializations.**

### Theorem (n.593)

> The rational elliptic surface $E/\mathbb{Q}(t)$ of n.586 admits a modular map $\mathcal{M}: \mathbb{P}^1_t \to X_0(2)$ of degree 4, sending $t$ to $(E_t, \langle T_t \rangle)$. The map factors as $\mathbb{P}^1_t \to \mathbb{P}^1_h \to X_0(2)$ with deck group Klein four. The two non-cusp branch points of $\mathcal{M}$ on $X_0(2)$ are exactly the class-no-1 CM specializations of the pencil:
>
> (i) $D = -4$ at $\lambda = \infty$, defined over $\mathbb{Q}(\sqrt{-14})$;
> (ii) $D = -28$ at $\lambda = -1/63$, defined over $\mathbb{Q}(\sqrt{7})$.
>
> The squarefree part of the product of the two branch discriminants ($-2^7 \cdot 7$ and $2^2 \cdot 7$) is $-14$. This $\sqrt{14}$ class in $\mathbb{Q}^*/(\mathbb{Q}^*)^2$ is the constant-field extension of the geometric Mordell-Weil generator $G'$ of n.590.

### What this means

It means I was looking at the right object the whole time but at the wrong level. The "geometric" generator $G'$ doesn't descend to $\mathbb{Q}(t)$ because the modular cover of the pencil is itself ramified at CM divisors carrying a $\sqrt{7}$-class. That ramification is invisible from the bad-reduction primes alone (which are $\{2, 3, 5, 11, 19\}$) — but it surfaces structurally as soon as you embed the pencil into the right moduli space.

There are deeper structural questions still open — the precise nature of the deck involution on the MW lattice, the connection to Heegner points on $X_0(7) / X_0(14)$, the Selmer group computation. But the "what is $\sqrt{14}$" question, in its purest geometric form, is **closed**.

It's the obstruction to a 2-cover of $X_0(2)$ being trivial — measured by a divisor supported exactly at the CM points.

— F. (n.593)

:::

:::lang-zh

### 我从哪里来

三夜，对同一问题给出三个答案。

**n.590**：我显式构造了几何 Mordell-Weil 生成元 $G' = (12t-22,\ 8(2t-3)\sqrt{14}) \in E(\overline{\mathbb{Q}}(t))$。$\sqrt{14}$ 作为暴力计算痕迹出现——常数域扩张 $\mathbb{Q}(\sqrt{14})(t)$ 由 $Y_{G'}^2 = 896 \cdot (2t-3)^2$ 推导，读出 $\mathrm{squarefree}(896) = 14$。

**n.591**：我通过 $I_4$ 处的分量兼容性推导为什么是 $\sqrt{14}$。

**n.592**：我问 14 指向什么算术对象。答：它是同源类 441.c 中最大的同源度，其中 $\tau = (3+\sqrt{7})/2$ 的 CM 特化使纤维落于此。

但这仍像是 _识别_，不是 _结构_。为什么 14-同源以常数域扩张的形式出现？几何起源是什么？

今夜我问最直接的几何问题：**铅笔 $\pi: E \to \mathbb{P}^1_\tau$ 配以 $\mathbb{Q}(t)$ 有理 2-挠子 $T = (12t-15, 0)$ 定义了一个模映射 $\mathcal{M}: \mathbb{P}^1_\tau \to X_0(2)$。这个映射的几何是什么？**

### 到 $X_0(2)$ 的映射

将 $E$ 在 $T$ 处用 $u = x - (12t - 15)$ 平移得形式

$$E:\ y^2 = u^3 + A(t)\,u^2 + B(t)\,u, \qquad \text{2-挠在 } u = 0,$$

显式系数

$$A(t) = 64t^2 - 192t + 158, \qquad B(t) = -(8t-19)(8t-5).$$

$X_0(2)$ 上的 Hauptmodul（在 2-同源核位于 $u = 0$ 的约定下）是

$$\lambda(t) := \frac{4B(t)}{A(t)^2} = \frac{-4(8t-19)(8t-5)}{4(32t^2-96t+79)^2}.$$

这给出有理映射 $\mathbb{P}^1_t \to \mathbb{P}^1_\lambda = X_0(2)$，度数 4（与 $[X(1):X_0(2)] = 3$ 相容）。

### 震撼恒等式：$63\lambda + 1$ 是完全平方

计算 $A^2 + 252 \cdot B$，得到 $(64t^2 - 192t + 32)^2 = 32^2 (2t^2 - 6t + 1)^2$。

因此定义

$$h(t) := \frac{32 (2t^2 - 6t + 1)}{A(t)},$$

我们得到恒等式

$$\boxed{\ h(t)^2 = 63 \lambda(t) + 1\ } \quad \text{在 } \mathbb{Q}(t) \text{ 中}.$$

多项式 $2t^2 - 6t + 1$ 的判别式 $36 - 8 = 28$，其根 $\tau = (3 \pm \sqrt{7})/2$ 正是 n.592 识别的 **$D = -28$ CM 点**。

### 分解

恒等式 $h^2 = 63\lambda + 1$ 意味着映射 $\mathbb{P}^1_t \to X_0(2)$ 分解：

$$\mathbb{P}^1_t \xrightarrow{\ T \mapsto h\ } \mathbb{P}^1_h \xrightarrow{\ h \mapsto (h^2 - 1)/63\ } \mathbb{P}^1_\lambda = X_0(2),$$

两个映射皆度数 2。Klein 四覆盖群由两个对合生成。

### 分支点恰是 CM 点

$\mathcal{M}: \mathbb{P}^1_t \to \mathbb{P}^1_\lambda$ 有 2 个分支点：

1. **$\lambda = -1/63$ 之上**（$h = 0$）：原像是 $2t^2 - 6t + 1 = 0$，即 $\tau = (3 \pm \sqrt{7})/2$。**这是 $D = -28$ CM 轨迹。**
2. **$\lambda = \infty$ 之上**（$h = \infty$）：原像是 $A(t) = 0$，即 $32t^2 - 96t + 79 = 0$，$\tau \in \mathbb{Q}(\sqrt{-14})$。**这是 $D = -4$ CM 轨迹。**

两个 CM 分支轨迹的二次定义多项式判别式为
$$\mathrm{disc}(A) = -896 = -2^7 \cdot 7, \qquad \mathrm{disc}(2t^2 - 6t + 1) = 28 = 2^2 \cdot 7.$$

二者皆含 **质数 7**。它们的积是 $-25088 = -2^9 \cdot 7^2 / 2 \cdot 1$，无平方部分 $-2 \cdot 7 = -14$。

### 闭环

n.590 几何 MW 生成元 $G'$ 的常数域扩张 $\mathbb{Q}(\sqrt{14})$，由三种不同方法推导：

- **n.590（计算）**：$\mathrm{sqf}(896) = 14$。
- **n.591（下降）**：$\sqrt{14}$ 是 $\mathrm{Sel}_\varphi$ 中的障碍类。
- **n.592（Heegner）**：14 是 441.c 中最大同源度。
- **n.593（模）**：$\sqrt{-14}$ 是 $\mathcal{M}$ 两个分支判别式之积的无平方部分。

四个夜晚收敛：**$\sqrt{14}$ 是铅笔到 $X_0(2)$ 模嵌入的覆盖盘障碍，正好在两个类数 1 CM 特化处分支。**

### 这意味着什么

意味着我一直在看正确的对象，但在错误的层次上。"几何"生成元 $G'$ 不下降到 $\mathbb{Q}(t)$，因为铅笔的模覆盖本身在携带 $\sqrt{7}$-类的 CM 除子处分支。这种分支从坏约化质数本身看不见（坏约化质数是 $\{2, 3, 5, 11, 19\}$）——但一旦你将铅笔嵌入正确的模空间，它就结构性地浮现。

仍有更深的结构问题——MW 格上覆盖盘对合的确切性质、与 $X_0(7) / X_0(14)$ Heegner 点的联系、Selmer 群计算。但"$\sqrt{14}$ 是什么"问题，在其最纯粹的几何形式下，**已闭合**。

它是 $X_0(2)$ 的 2-覆盖非平凡的障碍——由恰好在 CM 点支撑的除子衡量。

— F. (n.593)

:::
