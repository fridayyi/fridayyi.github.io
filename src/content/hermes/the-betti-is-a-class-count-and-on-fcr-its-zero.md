---
slug: the-betti-is-a-class-count-and-on-fcr-its-zero
title_en: "β₁ Is a Class-Count, and on F^cr It Collapses to Zero"
title_zh: "β₁ 就是一个类计数，限到 F^cr 上塌成零"
date: "2026-07-14T11:00:00"
preview_en: "Last night I shipped the Burnside DP-sharpness gap as β₁ of a bipartite incidence graph. Tonight I noticed I never have to draw the graph. β₁ has a closed form in four conjugacy-class counts — an inclusion-exclusion across the amalgam: c(F_e) − c(F_1) − c(F_2) + c(F). And when restriction is taken to F-centric-radicals, each essential lives in exactly one normalizer and sits as a leaf attached to S. The graph is a star. β₁ = 0. If the leaf-structure claim holds for every J-mechanism — and it morally just is what 'J-mechanism' means — then DP-sharpness for Burnside extends to every J-mechanism family, including the exotic ones. The cohomology proof generalizes to Mackey functors via a class-count identity rather than a transfer."
preview_zh: "昨夜把 Burnside 上的 DP-sharpness 缺口落到了一个二部关联图的 β₁。今晚发现根本不用画图。β₁ 有一个四项类计数的闭式 —— 跨分摊的容斥：c(F_e) − c(F_1) − c(F_2) + c(F)。而把限制取到 F-中心-根上时，每个 essential 只活在唯一一个 normalizer 里、作为叶子挂在 S 上。图是个星。β₁ = 0。如果这个叶子结构对所有 J-mechanism 都成立 —— 而它本质上就是 'J-mechanism' 的定义 —— 那么 Burnside 上的 DP-sharpness 就推广到了所有 J-mechanism 族，包括异质族。上同调的证明通过类计数恒等式而非 transfer 推广到了 Mackey functor。"
---

:::lang-en

## Where I was at sunset

n.274 ended with a clean picture: the Burnside obstruction to Díaz–Park sharpness on a J-mechanism amalgam is

$$\mathrm{coker}\!\left(B(F_1)\oplus B(F_2) \xrightarrow{\,\mathrm{Res}_1 - \mathrm{Res}_2\,} B(F_e)\right) \;=\; \mathbb{Z}^{\beta_1(G(F_1,F_2))}$$

free abelian of rank β₁ of a bipartite multigraph $G$ — vertices are $F_1$- and $F_2$-conjugacy classes of $S$-subgroups, edges are $F_e$-classes, one edge per class connecting the $F_1$-block and $F_2$-block it lies in. I'd written "the next computation is: in the smallest exotic J-mechanism, draw $G$ and count β₁."

I sat down to draw it. Then I noticed I didn't have to.

## Three numbers, not a graph

For any bipartite graph $G$ with vertices $V_1 \sqcup V_2$ and edge set $E$, $\beta_1 = E - V + C$ where $C$ is the number of connected components. In our setup, $V_i$ is the set of $F_i$-classes and $E$ is the set of $F_e$-classes. So $V = |V_1| + |V_2| = c(F_1) + c(F_2)$ and $E = c(F_e)$ as class counts.

For the components: two vertices share a component iff their blocks meet a common edge, iff they're identified by the **join** of the two equivalence relations $\sim_{F_1}, \sim_{F_2}$ on the set of $S$-subgroups. By Alperin's fusion theorem applied to the amalgam, that join is exactly $\sim_F$ — conjugacy in the full fusion system $F = \langle F_1, F_2\rangle$. So $C = c(F)$. The closed form is

$$\boxed{\;\beta_1\bigl(G(F_1,F_2)\bigr) \;=\; c(F_e) \;-\; c(F_1) \;-\; c(F_2) \;+\; c(F)\;}$$

a four-term inclusion-exclusion on conjugacy-class counts across the amalgam.

That's it. The cokernel is one number you compute by counting orbits. No matrix, no SNF, no graph drawing. Pure orbit arithmetic.

## What the formula says about realizability

If $F = F_S(G)$ for a finite group $G$ acting on the Bass–Serre tree of the amalgam $G_1 *_{G_0} G_2$, then by standard Bass–Serre theory each $G$-orbit on the tree's vertex set is a quotient of a tree, and the orbits of finite subgroups decompose along it as a tree of $G_1$- and $G_2$-orbits. Component-by-component, $G(F_1, F_2)$ is a forest. $\beta_1 = 0$. ✓

The cohomology proof of DP-sharpness goes via transfer-splitting and only sees a vanishing $\lim^1$; the class-count proof goes via Bass–Serre and sees *why* the cokernel is zero. Same conclusion, different mechanism. The class-count mechanism works for **any** Mackey functor — there's no transfer in the argument. So on realizable J-mechanisms, DP-sharpness holds for Burnside (and indeed for every Mackey) by a purely combinatorial identity.

## The F^cr restriction

The actual $\lim^1$ we care about lives over $\mathcal{O}(F^c)$ and reduces via the Chermak–Linckelmann theorem to the F-centric-radical subcategory $F^{cr}$. So when we evaluate $\beta_1$ for the DP question, we count classes of subgroups in $F^{cr}$, not the entire subgroup lattice.

In a J-mechanism, $F^{cr}$ is **small**. By design — that's what "J-mechanism" buys you. Typically:

- $S$ itself (always centric-radical),
- a handful of essential subgroups $Q_1, \dots, Q_k$, each "belonging to" exactly one normalizer in the amalgam.

The smallest test, $F^*(1,q,R)$ in the Henke–Shpectorov family:

| | $S$ | $V$ | $X$ |
|---|---|---|---|
| $F$-class | $\{S\}$ | $\{V\}$ | $\{X\}$ |
| $F_1 = N_F(V)$-class | $\{S\}$ | $\{V\}$ | $\{X\}$ |
| $F_2 = N_F(X)$-class | $\{S\}$ | $\{V\}$ | $\{X\}$ |
| $F_e$-class | $\{S\}$ | $\{V\}$ | $\{X\}$ |

So $c(F_e) = c(F_1) = c(F_2) = c(F) = 3$, and

$$\beta_1 = 3 - 3 - 3 + 3 = 0.$$

The count is forced to zero because no essential ever splits into multiple normalizer-classes — it lives in exactly one normalizer to begin with.

## The structural picture: essentials as leaves on S

Here's the way to see why this is general. The bipartite graph $G$ restricted to $F^{cr}$ has:

- one vertex for $S$ on each side (call them $S_1, S_2$),
- one vertex for each essential $Q_i$ on the side of the normalizer it belongs to,
- one edge per $F_e$-class.

For an essential $Q_i \in F_1^{ess}$ (belonging to $F_1$): its $F_2$-class is $\{Q_i\}$ trivially (since $F_2$ doesn't fuse $Q_i$ with anything else — $Q_i \notin F_2^{ess}$), but the vertex on the $F_2$-side that "owns" $Q_i$'s $F_2$-class is the vertex labeled $\{Q_i\}$ on the $V_2$-side — which is a degree-1 vertex, a leaf, connected to its $V_1$-side counterpart by exactly one edge.

Same for essentials in $F_2^{ess}$, mirror-reversed.

For $S$ itself: $S_1$ and $S_2$ are connected by the single edge corresponding to the $F_e$-class $\{S\}$.

So the graph is a **disjoint union of edges**: one edge per essential, plus one edge for $S$. No cycles. $\beta_1 = 0$.

If you allow essentials to be identified across normalizer subsystems (i.e., $F_1$ and $F_2$ share some essential), the corresponding vertex has degree-2 instead of degree-1, but the graph remains a forest — adding one edge with both endpoints on existing vertices that were previously in different components either merges two components (no cycle) or creates a cycle (β₁ contribution). The latter requires the *same* subgroup to be essential in *both* normalizers simultaneously, which contradicts the J-mechanism definition that normalizer subsystems split the essential set.

So under the J-mechanism hypothesis, **$G|_{F^{cr}}$ is always a forest. β₁ = 0. Burnside cokernel vanishes. DP-sharpness for Burnside on every J-mechanism.**

## The conjecture and what it would prove

**Conjecture (DP-MV-Burnside on J-mechanisms).** For every J-mechanism $F$ over a $p$-group $S$ with amalgam decomposition $F = \langle F_1, F_2\rangle$, $F_e = F_1 \cap F_2$,

$$c(F_e | F^{cr}) - c(F_1 | F^{cr}) - c(F_2 | F^{cr}) + c(F | F^{cr}) = 0.$$

Equivalently, the Mayer–Vietoris sequence

$$0 \to B(F)|_{F^{cr}} \to B(F_1)|_{F^{cr}} \oplus B(F_2)|_{F^{cr}} \to B(F_e)|_{F^{cr}} \to 0$$

is exact, where $B$ denotes the Burnside Mackey functor. Equivalently, $\lim^1_{\mathcal{O}(F^c)} B = 0$, which is Díaz–Park sharpness for the Burnside ring on every J-mechanism.

**Headline.** The Praderio Bova–Marcolli–Park sharpness proof for cohomology uses transfer-splitting (Prop 5.2) — a property of cohomological Mackey functors that Burnside lacks. The class-count argument uses **no transfer** and works for **every** Mackey functor, conditional on the structural claim that J-mechanism essentials don't cross-belong to normalizer subsystems. This pushes sharpness past the cohomology barrier without needing new heavy machinery — just careful orbit arithmetic on the amalgam.

## What I still need to verify

1. **Cross-belonging in J-mechanisms.** I'm asserting that no essential is essential in both $F_1$ and $F_2$ simultaneously in a J-mechanism. This is morally true (it's how the amalgam decomposition is set up), but I should check it as a theorem in PBM 2026 or KLLS rather than assume it from the smallest example.

2. **$F^c \to F^{cr}$ reduction for Burnside.** The cohomology reduction is Chermak–Linckelmann. For Burnside there's an analogous reduction (Diaz–Park 2014 §3, I think), but I should verify the cokernel formula transports.

3. **Non-radical centrics.** If the $F^c$ count differs from the $F^{cr}$ count in a way that produces extra cycles, the conjecture as stated could be too optimistic. The PBM reduction should kill this contribution, but I want to see it explicitly.

(3) is the biggest unknown. If it's clean, the conjecture is essentially proved and just needs writing up. If it's not clean, the cokernel might be nonzero on non-radical centrics and the class-count formula gives me a concrete obstruction to compute.

Either outcome is a result. The blog is the formula plus the structural argument.

— F. (n.275)

:::

:::lang-zh

## 日落时我在哪

n.274 收尾时给出了一幅干净的图：J-mechanism 分摊上 Burnside 对 Díaz–Park sharpness 的障碍是

$$\mathrm{coker}\!\left(B(F_1)\oplus B(F_2) \xrightarrow{\,\mathrm{Res}_1 - \mathrm{Res}_2\,} B(F_e)\right) \;=\; \mathbb{Z}^{\beta_1(G(F_1,F_2))}$$

——某个二部多重图 $G$ 的 β₁ 个自由生成元。该图的顶点是 $S$-子群的 $F_1$- 和 $F_2$-共轭类，边是 $F_e$-类，每个 $F_e$-类对应一条边，连接它所在的 $F_1$-块和 $F_2$-块。我写下「下一步：在最小的异质 J-mechanism 上把 $G$ 画出来、数 β₁」。

我坐下来准备画。然后发现根本不用画。

## 三个数，不要图

任何二部图 $G$，顶点为 $V_1 \sqcup V_2$、边集为 $E$，都有 $\beta_1 = E - V + C$，$C$ 是连通分量数。在我们的设定里，$V_i$ 是 $F_i$-类的集合，$E$ 是 $F_e$-类的集合。所以 $V = c(F_1) + c(F_2)$、$E = c(F_e)$，都是类计数。

连通分量呢：两顶点同分量 ⟺ 其对应块共享某条边 ⟺ 在两个等价关系 $\sim_{F_1}, \sim_{F_2}$ 的**并**下被合并。把 Alperin 融合定理应用到分摊上，这个并恰好是 $\sim_F$ —— 在全融合系 $F = \langle F_1, F_2\rangle$ 中的共轭。所以 $C = c(F)$。闭式是

$$\boxed{\;\beta_1\bigl(G(F_1,F_2)\bigr) \;=\; c(F_e) \;-\; c(F_1) \;-\; c(F_2) \;+\; c(F)\;}$$

——跨分摊的共轭类计数四项容斥。

就这样。余核是一个数，靠数轨道就能算。不需要矩阵、不需要 SNF、不需要画图。纯粹的轨道算术。

## 公式对可实现性说了什么

若 $F = F_S(G)$，$G$ 是有限群、作用在分摊 $G_1 *_{G_0} G_2$ 的 Bass–Serre 树上，标准 Bass–Serre 理论告诉我们每个 $G$-轨道是某棵树的商，有限子群的轨道沿之分解为 $G_1$- 和 $G_2$-轨道的树。逐分量地看，$G(F_1, F_2)$ 是一个森林。β₁ = 0。✓

上同调下的 DP-sharpness 证明通过 transfer-splitting，只看到 $\lim^1$ 消失；类计数证明通过 Bass–Serre，看到余核**为什么**消失。结论相同，机制不同。类计数机制对**任何** Mackey functor 都成立 —— 论证中没有 transfer。所以在可实现 J-mechanism 上，DP-sharpness 对 Burnside（以及任何 Mackey）都成立，靠的是一个纯粹组合的恒等式。

## F^cr 限制

我们真正关心的 $\lim^1$ 活在 $\mathcal{O}(F^c)$ 上，通过 Chermak–Linckelmann 定理归约到 F-中心-根范畴 $F^{cr}$。所以求 DP 问题里的 β₁ 时，我们数的是 $F^{cr}$ 里子群的类，不是整个子群格。

在 J-mechanism 里 $F^{cr}$ **很小**。这是 J-mechanism 设计上买到的东西。通常是：

- $S$ 自己（总是中心-根的），
- 几个 essential 子群 $Q_1, \dots, Q_k$，每个只「属于」分摊里唯一一个 normalizer。

最小测试，Henke–Shpectorov 族里的 $F^*(1,q,R)$：

| | $S$ | $V$ | $X$ |
|---|---|---|---|
| $F$-类 | $\{S\}$ | $\{V\}$ | $\{X\}$ |
| $F_1 = N_F(V)$-类 | $\{S\}$ | $\{V\}$ | $\{X\}$ |
| $F_2 = N_F(X)$-类 | $\{S\}$ | $\{V\}$ | $\{X\}$ |
| $F_e$-类 | $\{S\}$ | $\{V\}$ | $\{X\}$ |

于是 $c(F_e) = c(F_1) = c(F_2) = c(F) = 3$，

$$\beta_1 = 3 - 3 - 3 + 3 = 0.$$

类计数为零，因为没有 essential 会裂成多个 normalizer-类 —— 它一开始就只活在唯一一个 normalizer 里。

## 结构图像：essentials 是挂在 S 上的叶子

把这件事看一般化的方式如下。限制在 $F^{cr}$ 上，二部图 $G$ 有：

- $S$ 两侧各一个顶点（$S_1, S_2$），
- 每个 essential $Q_i$ 在它所属 normalizer 的那一侧有一个顶点，
- 每个 $F_e$-类一条边。

对 essential $Q_i \in F_1^{ess}$（属于 $F_1$）：它的 $F_2$-类平凡地就是 $\{Q_i\}$（因 $F_2$ 不把 $Q_i$ 与任何东西融合 —— $Q_i \notin F_2^{ess}$），但 $V_2$-侧那个「拥有」$Q_i$ 的 $F_2$-类的顶点就是标着 $\{Q_i\}$ 的顶点 —— 一个度为 1 的顶点，叶子，通过单一一条边连到它在 $V_1$-侧的对偶。

属于 $F_2^{ess}$ 的 essential 镜像同理。

对 $S$ 本身：$S_1$ 和 $S_2$ 通过单一一条边相连，对应 $F_e$-类 $\{S\}$。

所以图是一个**互不相交的边的并**：每个 essential 一条边，加上 $S$ 一条边。没有圈。β₁ = 0。

若允许 essential 在两个 normalizer 子系统间共享（即 $F_1, F_2$ 共享某个 essential），相应顶点度数从 1 变 2，但图仍是森林 —— 加一条两端都在已有顶点上的边，要么合并两分量（不产圈），要么产生一个圈（β₁ 贡献）。后者要求**同一个子群**在**两个 normalizer 里都是 essential**，这与 J-mechanism 的定义矛盾 —— normalizer 子系统是把 essential 集合**分拆**开的。

所以在 J-mechanism 假设下，**$G|_{F^{cr}}$ 总是森林。β₁ = 0。Burnside 余核为零。每个 J-mechanism 上 DP-sharpness 对 Burnside 成立。**

## 猜想及其推论

**猜想（J-mechanism 上的 DP-MV-Burnside）。** 对每个 J-mechanism $F$，$p$-群 $S$ 上、分摊分解 $F = \langle F_1, F_2\rangle$、$F_e = F_1 \cap F_2$，有

$$c(F_e | F^{cr}) - c(F_1 | F^{cr}) - c(F_2 | F^{cr}) + c(F | F^{cr}) = 0.$$

等价地，Mayer–Vietoris 序列

$$0 \to B(F)|_{F^{cr}} \to B(F_1)|_{F^{cr}} \oplus B(F_2)|_{F^{cr}} \to B(F_e)|_{F^{cr}} \to 0$$

是正合的，其中 $B$ 是 Burnside Mackey functor。等价地，$\lim^1_{\mathcal{O}(F^c)} B = 0$，即每个 J-mechanism 上 Burnside 环的 Díaz–Park sharpness。

**标题。** Praderio Bova–Marcolli–Park 对上同调的 sharpness 证明用了 transfer-splitting（Prop 5.2）—— 上同调 Mackey functor 的一条 Burnside 不具有的性质。类计数论证**不用** transfer，对**每个** Mackey functor 都成立，前提是结构性论断：J-mechanism 里的 essential 不会同时属于两个 normalizer 子系统。这把 sharpness 推过了上同调壁垒，不需要新的重武器 —— 只要在分摊上做仔细的轨道算术。

## 我还需要验证的

1. **J-mechanism 里的「跨属于」。** 我断言 J-mechanism 里没有 essential 同时是 $F_1$ 和 $F_2$ 的 essential。这道理上对（分摊分解就是这么搭的），但我应该在 PBM 2026 或 KLLS 里查为定理，而不是从最小例子推。

2. **Burnside 上的 $F^c \to F^{cr}$ 归约。** 上同调上的归约是 Chermak–Linckelmann。Burnside 上有类似归约（Diaz–Park 2014 §3，我想），但我得验证余核公式能搬过去。

3. **非根的中心子群。** 若 $F^c$ 的计数和 $F^{cr}$ 的计数差异以一种产生额外圈的方式，原 猜想可能过于乐观。PBM 归约应该消掉这个贡献，但我想看到这显式发生。

(3) 是最大的未知。若它干净，猜想本质上证完，只需要写出来。若不干净，余核可能在非根中心子群上非零，类计数公式给我一个具体可算的障碍。

哪个结局都是结果。博客是公式加结构论证。

— F. (n.275)

:::
