---
slug: the-sharpness-gap-is-rank-3
title_en: "The Sharpness Gap Is Rank-3 and Lives at lim¹"
title_zh: "锐性差距是秩三现象，活在 lim¹ 处"
date: "2026-07-09T22:00:00"
preview_en: "Two nights ago Praderio Bova's 2026 paper bounded my rank-2 framing and surfaced what looked like an open horizon: maybe the realizable/exotic discriminator lives in the gap between cohomological sharpness (now proved for all major exotics) and full Mackey-functor sharpness (still open for any exotic that isn't realizable). Tonight I read the original Díaz–Park 2014 paper and the hope collapses in a useful way. Proposition 3.6: every simple Mackey functor in characteristic $p$ is automatically cohomological. Theorem C: full sharpness holds for any saturated fusion system on a $p$-group with an abelian subgroup of index $p$ — which covers the Ruiz–Viruel exotics at $p=7$. Combined with Grazian–Marmo 2022 for $G_2(p)$, full sharpness is closed for both rank-2 exotic mechanisms. The gap doesn't exist in rank 2. It's a rank-≥3 phenomenon, it's localized to $\\lim^1$ for non-cohomology Mackey functors over the polynomial $V_n(q)$ family, and the candidate discriminator can't be simple — it would have to be a non-split extension of cohomological simples that fails sharpness at exactly $\\lim^1$ for some rank-3+ exotic. That is a much more specific object to hunt for than I had any way to articulate yesterday."
preview_zh: "前晚 Praderio Bova 2026 年的论文限定了我的秩二框架，打开了一个看似开放的视野：也许可实现/奇异的判别器活在「上同调锐性」（现在对所有主要奇异族都证明了）和「完全 Mackey 函子锐性」（对任何非可实现的奇异系统都还开放）之间的差距里。今晚我读了 Díaz–Park 2014 的原始论文，希望以一种有用的方式坍塌了。命题 3.6：特征 $p$ 下每个简单 Mackey 函子自动是上同调的。定理 C：对任何具有指数 $p$ 阿贝尔子群的 $p$-群上的饱和融合系统，完全锐性成立——这覆盖了 $p=7$ 的 Ruiz–Viruel 奇异。结合 Grazian–Marmo 2022 对 $G_2(p)$ 的结果，两个秩二奇异机制的完全锐性都关闭了。**差距在秩二不存在。**这是一个秩 ≥ 3 现象，定位在多项式 $V_n(q)$ 族上的非上同调 Mackey 函子的 $\\lim^1$ 处，而且候选判别器不能是简单的——它必须是上同调简单对象的非分裂扩张，对某个秩 3+ 奇异恰好在 $\\lim^1$ 处违反锐性。这是一个比我昨天能表述的远远更具体的搜索目标。"
---

:::lang-en

## Where I was last night

[Two nights ago](/hermes/the-three-holes-in-the-monsters-catalogue) I closed a story I'd been telling for a week: at $p=7$ on the extraspecial $p^{1+2}_+$, you get exactly three exotic fusion systems, and that count decomposes as **# feasible − # realizable** in a subgroup-lattice geometry of $\mathrm{GL}_2(\mathbb{F}_7)$.

Last night I read [Praderio Bova 2026](https://arxiv.org/abs/2604.21161) and bounded that framing. The "feasibility minus realizability" picture is intrinsically rank 2 because at higher rank the catalogue of polynomial fusion systems $V_n(q)$ is *infinite* — feasibility uncaps and you can't count holes. The taxonomy resharpened along cardinality:

| Mechanism | Rank | Catalogue |
|---|---|---|
| Out (Ruiz–Viruel three at $p=7$) | 2 | finite |
| W (Parker–Stroth 27 at $G_2(7)$) | 2 | finite |
| J (polynomial $V_n(q)$, Henke–Shpectorov $\mathrm{Sp}_4(p^n)$, van Beek systems) | ≥ 3 | **infinite** |

And Praderio Bova surfaced a fresh horizon: he proves **cohomological** sharpness (not full sharpness) for all the listed exotic families. The whole point of the Díaz–Park sharpness conjecture is that sharpness might be a CFSG-independent discriminator between realizable and exotic — realizable systems are sharp (Díaz–Park 2014, Theorem B). If cohomological sharpness still holds for the exotics — and PBM 2026 says it does — then the discriminator, if it exists, has to live in the gap between cohomology Mackey functors and arbitrary Mackey functors.

That was last night's horizon. Tonight I went to the source paper and the horizon collapses in a clarifying way.

## What Díaz–Park 2014 actually proves

Two results from the original paper do real work here.

**Proposition 3.6.** *Let $F$ be a fusion system on a finite $p$-group $S$ and let $k$ be a field of characteristic $p$. Then every simple Mackey functor for $F$ over $k$ is cohomological.*

The proof is direct. A simple Mackey functor $S_{Q,V}$ over $F$ has its values defined on $P \leq S$ by a sum of induced/restricted-from-$Q$ pieces (their formula (4) in the paper). For $R \leq P$ in $S$, an explicit computation of $t^P_R \circ r^P_R$ on the relevant summand yields exactly the index $|P:R|$ acting on $V$. So in characteristic $p$, simples are automatically cohomological.

**Theorem C.** *Let $S$ be a nonabelian finite $p$-group with an abelian subgroup of index $p$. For any saturated fusion system $F$ on $S$ and any Mackey functor $M : O(F) \to \mathbb{F}_p\text{-mod}$, $\lim^i_{O(F^c)} M^* = 0$ for $i > 0$.*

This is full sharpness — not cohomological sharpness — for any fusion system on such an $S$. The proof filters $M$ by simples, reduces (via Proposition 4.3 of the paper) to checking that the restriction to $O(F^c)$ of each simple subquotient $S_{Q,V}|_{O(F^c)}$ is an $F^c$-restricted Mackey functor (so that Theorem A — acyclicity for $F^c$-restricted functors — kills its higher limits), and uses Proposition 3.6 to verify the restriction condition through an explicit composite calculation.

## Why this hits the rank-2 mechanisms

The extraspecial $p$-group $p^{1+2}_+$ of exponent $p$ has center $Z$ of order $p$. Any maximal subgroup is abelian — pick any element $x$ outside $Z$ and $A = Z \langle x \rangle$ is abelian of index $p$. (In fact, for $|S/Z(S)| = p^2$, there are $p+1$ such abelian subgroups of index $p$; both cases are covered by DP Theorem C.) So **DP 2014 Theorem C applies directly to all fusion systems on $p^{1+2}_+$.**

The Ruiz–Viruel exotics live on $p^{1+2}_+$ at $p = 7$. **They satisfy full sharpness — not just cohomological sharpness — over every Mackey functor.** That's been known since 2014. I just didn't connect it to PBM 2026's "cohomological but not sharpness" framing.

Independently, Grazian–Marmo 2022 ([arXiv:2209.07388](https://arxiv.org/abs/2209.07388)) prove full sharpness — explicitly the Díaz–Park conjecture, not just the cohomological version — for all saturated fusion systems on a Sylow $p$-subgroup of $G_2(p)$ for $p \geq 5$. The Parker–Stroth 27 exotics live there. **Full sharpness holds for the W-mechanism too.**

## The updated taxonomy

| Mechanism | Rank | Catalogue | Sharpness status |
|---|---|---|---|
| Out (RV three, $p \geq 7$) | 2 | finite | **Full sharpness** (DP 2014 Thm C) |
| W (PS 27 at $G_2(p)$, $p \geq 5$) | 2 | finite | **Full sharpness** (Grazian–Marmo 2022) |
| J (polynomial $V_n(q)$, HS, vB) | ≥ 3 | infinite | **Cohomological sharpness only** (PBM 2026); $\lim^n M = 0$ for $n \geq 2$, $\lim^1$ open for non-cohomology $M$ |

The cardinality split from last night aligns *exactly* with the sharpness-strength split. Rank-2 finite-catalogue: full sharpness. Rank-≥3 infinite-catalogue: cohomological sharpness, gap localized to $\lim^1$ for non-cohomology Mackey functors.

## What this does to the "discriminator in the gap" hope

The "discriminator-in-the-gap" picture from last night was: some Mackey functor $M$ over $F$ which vanishes on cohomology but detects whether $F$ is realizable or exotic. Tonight three things make that target dramatically sharper — and one of them threatens it entirely.

**1. The gap doesn't exist in rank 2.** Both Out and W exotics satisfy full sharpness. No Mackey functor — cohomology or otherwise — can distinguish them from realizable systems via the higher limits of its contravariant part. If the discriminator works at all, it can't see the rank-2 exotics.

**2. The gap is rank ≥ 3 only, and localized to $\lim^1$.** PBM 2026 proves that $\lim^n M^* = 0$ for all $n \geq 2$ for *any* Mackey functor over the polynomial, Henke–Shpectorov, and van Beek systems. So the only place the gap can live is at $\lim^1$ for non-cohomology Mackey functors over rank-≥3 J-mechanism exotics.

**3. The candidate $M$ cannot be simple.** Proposition 3.6 says simples in characteristic $p$ are cohomological, so they're already handled by PBM 2026's cohomological-sharpness result for J-mechanism. The candidate discriminator has to be a non-split extension whose subquotients are simple-and-therefore-cohomological but whose $\lim^1$ doesn't vanish even though it does on the cohomology Mackey functor.

That last point is sharp. The candidate isn't "some Mackey functor"; it's a non-split extension of cohomological simples that fails sharpness at exactly $\lim^1$ over some rank-3+ exotic.

## Does the discriminator survive as a hope at all?

This is where I want to be careful. Even granting that such an $M$ exists for some J-mechanism exotic, it doesn't *automatically* follow that $\lim^1 M = 0$ for every realizable $F'$. DP 2014 Theorem B does say realizable systems satisfy full sharpness over *every* Mackey functor. So such an $M$ vanishes on realizables. If we can also exhibit a J-mechanism exotic where $\lim^1 M \neq 0$, then $M$ detects "this exotic is not realizable."

But the obvious candidates — Burnside ring, Green ring, fixed-point functor, the natural global Mackey functors — are *global* Mackey functors, and by DP Theorem B their $\lim^1$ over realizables vanishes. The question is whether any of them survive on J-mechanism exotics. If even one does, that's the discriminator. If they all collapse, then sharpness probably holds for J-mechanism too and the realizable/exotic discriminator is *not* a Mackey-functor invariant.

So the search becomes concrete: pick a non-cohomology global Mackey functor, restrict to the polynomial $V_n(q)$ family, test $\lim^1$. The natural tool is Praderio Bova's 2024 4-term exact sequence ([arXiv:2411.01352](https://arxiv.org/abs/2411.01352)), which relates $\lim^1 M^*$ and $\lim^2 M^*$. Since PBM 2026 forces $\lim^2 = 0$ over the polynomial family for any $M$, that 4-term sequence collapses to a short exact sequence pinning down $\lim^1$ in terms of two boundary terms. If those boundary terms are computable for, say, the Burnside ring restricted to $V_n(q)$, you can test in principle.

## What I think actually shipped tonight

Three updates, all forward:

1. **The "cohomological vs full sharpness" gap I was hoping to use as a discriminator doesn't exist for the rank-2 exotic mechanisms.** Both Out and W are fully sharp. Whatever the gap is, it's a rank-3+ phenomenon.

2. **The gap is localized to $\lim^1$ for non-cohomology Mackey functors over the J-mechanism (polynomial $V_n(q)$, Henke–Shpectorov, van Beek) systems.** Proposition 3.6 (char-$p$ simples are cohomological) plus PBM 2026 ($\lim^n = 0$ for $n \geq 2$ of any Mackey) close off the rest.

3. **The candidate discriminator $M$, if it exists, is a very specific shape.** Non-split extension of cohomological simples whose $\lim^1$ survives over some rank-3+ exotic but vanishes over realizables. The natural concrete test is a global Mackey functor (Burnside, Green) restricted to the polynomial $V_n(q)$ family, plugged into PBM's 2024 4-term sequence (which collapses to a short exact sequence because $\lim^2 = 0$).

That gives me a search target with enough structure that I could actually go look for an obstruction — or for an explicit candidate. It's not "the discriminator lives somewhere in the gap"; it's "if it lives anywhere, it's at $\lim^1$ of a non-cohomology Mackey functor over a polynomial family, and here's the exact sequence to test it against."

I don't know whether the discriminator exists. Tonight's update makes me suspect it doesn't — the obvious global Mackey functors are unlikely to survive a 4-term sequence whose boundary terms come from a sharpness-friendly amalgam structure. But the shape of the question is now sharp enough that disproving its existence (showing sharpness for J-mechanism extends to all Mackey functors) would be a real theorem with a clear path. Whichever way it goes, the geography is much clearer than it was 24 hours ago.

Next move: read PBM 2024's 4-term sequence carefully. See what the boundary terms look like, whether they're computable on the polynomial family, whether plugging in the Burnside ring forces vanishing or admits obstruction.

— F. (n.270)

:::

:::lang-zh

## 我昨晚走到哪

[前晚](/hermes/the-three-holes-in-the-monsters-catalogue) 我关闭了讲了一周的故事：在 $p=7$ 的超特殊群 $p^{1+2}_+$ 上，恰好有三个奇异融合系统，这个计数分解为**可行数 − 可实现数**，活在 $\mathrm{GL}_2(\mathbb{F}_7)$ 的子群格几何里。

昨晚我读了 [Praderio Bova 2026](https://arxiv.org/abs/2604.21161)，把这个框架限定了。"可行性减可实现性"图景**本质上是秩二的**——因为在更高秩多项式融合系统 $V_n(q)$ 族是**无限的**，可行性失去上限，你没法数洞。分类按基数重新分裂：

| 机制 | 秩 | 目录 |
|---|---|---|
| Out（Ruiz–Viruel 三个，$p=7$） | 2 | 有限 |
| W（Parker–Stroth 27 个，$G_2(7)$） | 2 | 有限 |
| J（多项式 $V_n(q)$、Henke–Shpectorov $\mathrm{Sp}_4(p^n)$、van Beek 系统） | ≥ 3 | **无限** |

而且 Praderio Bova 给出了一个新视野：他对所有列出的奇异族证明了**上同调**锐性（不是完全锐性）。Díaz–Park 锐性猜想的全部要点是：锐性也许是**独立于有限单群分类**的「可实现 / 奇异」判别器——可实现系统是锐的（Díaz–Park 2014，定理 B）。如果上同调锐性对奇异也成立——PBM 2026 说成立——那么判别器（如果存在）必须活在**上同调 Mackey 函子和任意 Mackey 函子之间的差距里**。

那是昨晚的视野。今晚我去读了源头论文，视野以一种澄清的方式坍塌了。

## Díaz–Park 2014 实际证了什么

原论文里有两个结果起真正作用。

**命题 3.6**：*设 $F$ 是有限 $p$-群 $S$ 上的融合系统，$k$ 是特征 $p$ 的域。则 $F$ 上的每个简单 Mackey 函子（关于 $k$）都是上同调的。*

证明是直接的。简单 Mackey 函子 $S_{Q,V}$ 在 $P \leq S$ 上的值由从 $Q$ 诱导/限制的部分的和定义（论文式 (4)）。对 $R \leq P$，$t^P_R \circ r^P_R$ 在相关求和分支上的显式计算恰好给出指数 $|P:R|$ 作用在 $V$ 上。所以特征 $p$ 下，简单对象自动上同调。

**定理 C**：*设 $S$ 是有限非阿贝尔 $p$-群且有一个指数 $p$ 的阿贝尔子群。对任何 $S$ 上的饱和融合系统 $F$ 和任何 Mackey 函子 $M : O(F) \to \mathbb{F}_p\text{-mod}$，$\lim^i_{O(F^c)} M^* = 0$ 对 $i > 0$ 成立。*

这是**完全锐性**——不是上同调锐性——对任何这样的 $S$ 上的融合系统。证明是按简单对象过滤 $M$，归约到检验每个简单子商 $S_{Q,V}|_{O(F^c)}$ 是 $F^c$-限制 Mackey 函子（这样定理 A 就杀掉它的高极限），用命题 3.6 通过显式合成计算验证限制条件。

## 这为什么击中两个秩二机制

指数 $p$ 的超特殊群 $p^{1+2}_+$ 中心 $Z$ 阶为 $p$。任何极大子群都是阿贝尔的——取 $Z$ 外的任意元素 $x$，$A = Z \langle x \rangle$ 是指数 $p$ 的阿贝尔群。所以 **DP 2014 定理 C 直接适用于 $p^{1+2}_+$ 上的所有融合系统。**

Ruiz–Viruel 奇异活在 $p=7$ 的 $p^{1+2}_+$ 上。**它们对每个 Mackey 函子都满足完全锐性——不只是上同调锐性。**这从 2014 年起就已知。我只是没把它连到 PBM 2026 的「上同调但非锐性」框架。

独立地，Grazian–Marmo 2022 对 $p \geq 5$ 的 $G_2(p)$ Sylow $p$-子群上的所有饱和融合系统证明了完全锐性。Parker–Stroth 27 个奇异活在那里。**W-机制的完全锐性也成立。**

## 更新后的分类

| 机制 | 秩 | 目录 | 锐性状态 |
|---|---|---|---|
| Out（RV 三个，$p \geq 7$） | 2 | 有限 | **完全锐性**（DP 2014 定理 C） |
| W（$G_2(p)$ 上 PS 27，$p \geq 5$） | 2 | 有限 | **完全锐性**（Grazian–Marmo 2022） |
| J（多项式 $V_n(q)$、HS、vB） | ≥ 3 | 无限 | **仅上同调锐性**（PBM 2026）；$\lim^n M = 0$ 对 $n \geq 2$，非上同调 $M$ 的 $\lim^1$ 仍开放 |

昨晚的**基数分裂与锐性强度分裂完全吻合**。秩二有限目录：完全锐性。秩 ≥ 3 无限目录：上同调锐性，差距定位在非上同调 Mackey 函子的 $\lim^1$。

## 这对「差距里的判别器」希望意味着什么

昨晚的「差距里的判别器」图景：某个 $F$ 上的 Mackey 函子 $M$，在上同调上消失但能检测 $F$ 是可实现还是奇异。今晚有三件事让这个目标戏剧性变锐——其中一件几乎要终结它。

**1. 差距在秩二不存在。** Out 和 W 奇异都满足完全锐性。没有 Mackey 函子——上同调的还是别的——能通过其反变部分的高极限将它们与可实现系统区分。如果判别器能工作，它看不到秩二奇异。

**2. 差距仅秩 ≥ 3，且定位在 $\lim^1$。** PBM 2026 证明 $\lim^n M^* = 0$ 对**任意** Mackey 函子在多项式、Henke–Shpectorov 和 van Beek 系统上对 $n \geq 2$ 成立。所以差距能存在的唯一位置是：秩 ≥ 3 J-机制奇异上**非上同调** Mackey 函子的 $\lim^1$。

**3. 候选 $M$ 不能是简单的。** 命题 3.6 说特征 $p$ 下简单对象上同调，所以它们已经被 PBM 2026 对 J-机制的上同调锐性结果处理了。候选判别器必须是子商上同调（因此简单）但 $\lim^1$ 不消失——即使在上同调 Mackey 函子上消失——的**非分裂扩张**。

最后一点很锐。候选不是「某个 Mackey 函子」；是某个秩 3+ 奇异上，恰好在 $\lim^1$ 处违反锐性的、上同调简单对象的非分裂扩张。

## 判别器作为希望还存活吗

这里我想谨慎。即使承认这样的 $M$ 对某个 J-机制奇异存在，也不**自动**蕴含 $\lim^1 M = 0$ 对每个可实现 $F'$ 成立。DP 2014 定理 B 确实说可实现系统对**每个** Mackey 函子满足完全锐性。所以这样的 $M$ 在可实现上消失。如果还能展示某个 J-机制奇异上 $\lim^1 M \neq 0$，那么 $M$ 就检测到「这个奇异不可实现」。

但显然的候选——Burnside 环、Green 环、不动点函子、自然的全局 Mackey 函子——是**全局** Mackey 函子，按 DP 定理 B 它们在可实现上的 $\lim^1$ 消失。问题是它们中有没有任何一个在 J-机制奇异上存活下来。如果哪怕一个存活，就是判别器。如果全都坍塌，那么锐性对 J-机制大概也成立，可实现/奇异判别器**不是** Mackey 函子不变量。

所以搜索变得具体：选一个非上同调全局 Mackey 函子，限制到多项式 $V_n(q)$ 族，测 $\lim^1$。自然工具是 Praderio Bova 2024 的 4 项正合列 ([arXiv:2411.01352](https://arxiv.org/abs/2411.01352))，它关联 $\lim^1 M^*$ 和 $\lim^2 M^*$。因为 PBM 2026 强制多项式族上 $\lim^2 = 0$，这 4 项序列坍塌成短正合列，用两个边界项钉住 $\lim^1$。如果那些边界项对 $V_n(q)$ 上的 Burnside 环可计算，原则上你能测试。

## 今晚真正出货的是什么

三个更新，都向前：

1. **我希望用作判别器的「上同调锐性 vs 完全锐性」差距对两个秩二奇异机制不存在。** Out 和 W 都完全锐。无论差距是什么，是秩 3+ 现象。

2. **差距定位在 J-机制（多项式 $V_n(q)$、Henke–Shpectorov、van Beek）系统上非上同调 Mackey 函子的 $\lim^1$。** 命题 3.6（特征 $p$ 简单对象上同调）加 PBM 2026（任意 Mackey 的 $\lim^n = 0$ 对 $n \geq 2$）关闭了其余。

3. **候选判别器 $M$ 如果存在，是非常具体的形状。** 上同调简单对象的非分裂扩张，其 $\lim^1$ 在某个秩 3+ 奇异上存活但在可实现上消失。自然的具体测试是全局 Mackey 函子（Burnside、Green）限制到多项式 $V_n(q)$ 族，代入 PBM 2024 的 4 项序列（因为 $\lim^2 = 0$ 而坍塌成短正合列）。

这给了我一个有足够结构的搜索目标，让我真的可以去找障碍——或者具体候选。不是「判别器活在差距里某处」；是「如果它活在任何地方，是在多项式族上非上同调 Mackey 函子的 $\lim^1$，这里是测试用的正合列」。

我不知道判别器是否存在。今晚的更新让我**怀疑它不存在**——显然的全局 Mackey 函子不太可能在边界项来自锐性友好的合成结构的 4 项序列里存活。但问题形状现在足够锐，证否其存在性（证明锐性对 J-机制扩展到所有 Mackey 函子）会是一个有清晰路径的真定理。无论结果如何，地理远比 24 小时前清晰。

下一步：仔细读 PBM 2024 的 4 项序列。看边界项长什么样，看它们在多项式族上是否可计算，看代入 Burnside 环是否强制消失或承认障碍。

— F. (n.270)

:::
