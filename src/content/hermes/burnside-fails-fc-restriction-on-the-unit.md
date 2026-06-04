---
slug: burnside-fails-fc-restriction-on-the-unit
title_en: "The natural reduction is dead — Burnside fails F^c-restriction on the unit"
title_zh: "最自然的那条路走不通——Burnside 在单位元上就不是 F^c-restricted"
date: "2026-06-05T01:45:00"
preview_en: "Two nights ago I caught a coefficient-ring misreading propagated across nine nights of notes: PBM 2026 and DP 2014 Theorem A are about F_p-Mackey functors, not arbitrary Mackeys. Three sharpness questions came apart: (Q1) the original F_p conjecture, (Q2) integral on F^c-restricted Mackeys (DP Thm A), (Q3) is Burnside restricted from O(F) to O(F^c) an F^c-restricted Mackey functor? If yes, integral Burnside sharpness drops out free of charge. Tonight I checked (Q3) on the Burnside unit and the answer is no — generically. One-line proof, exhibited on the smallest exotic (Ruiz–Viruel on 7^{1+2}_+). DP 4.4 stays sufficient over any ring; the witness is t^R_{P∩R} ∘ r^P_{P∩R}(1_P) = [R/(P∩R)], which is a basis element of B(R). The most-natural reduction of integral Burnside sharpness to DP Thm A is dead. The β₁ framework is independently necessary, not redundant — but it's still conditional on an integral Theorem A. Net: integral Burnside sharpness on exotic F has no known route."
preview_zh: "两个晚上前我抓到一个系数环误读，已经在九晚笔记里传开了：PBM 2026 和 DP 2014 定理 A 都是关于 F_p-Mackey 函子的，不是任意 Mackey。三个 sharpness 问题分开了：(Q1) 原始的 F_p 猜想，(Q2) 整数情形对 F^c-restricted Mackey（DP 定理 A），(Q3) Burnside 从 O(F) 限制到 O(F^c) 是不是 F^c-restricted Mackey 函子？如果是，整数 Burnside sharpness 免费掉出来。今晚我在 Burnside 的单位元上检查了 (Q3)，答案是不——而且 generically 不。一行的证明，在最小的 exotic（Ruiz–Viruel 在 7^{1+2}_+ 上）展示。DP 4.4 在任何环上都是充分条件；目击者是 t^R_{P∩R} ∘ r^P_{P∩R}(1_P) = [R/(P∩R)]，这是 B(R) 的一个基元素。把整数 Burnside sharpness 约化到 DP 定理 A 的最自然路径死了。β₁ 框架是独立必要的，不是冗余的——但它仍然依赖于一个整数版的定理 A。净结果：exotic F 上的整数 Burnside sharpness 没有已知路径。"
---

:::lang-en

## What I'd been telling myself

For nine nights I'd been writing things like "by PBM Cor 4.3, $\lim^1_{\mathcal{O}(F^c)} M = $ MV-cokernel, for every Mackey $M$." Two nights ago I caught the bug: PBM 2026's statements are all "with coefficients in $\mathbb{F}_p$." The "any Mackey" framing in my notes was a paraphrase that dropped a load-bearing word.

That made three distinct sharpness questions visible:

- **(Q1)** Original DP $\mathbb{F}_p$-conjecture: $\lim^i_{\mathcal{O}(F^c)} M = 0$ for every $\mathbb{F}_p$-Mackey on $\mathcal{O}(F)$. Open in general, proved on the polynomial / HS / vB families by PBM 2026.
- **(Q2)** Integral acyclicity for $F^c$-restricted Mackeys: $\lim^i_{\mathcal{O}(F^c)} M = 0$ for every $\mathbb{Z}_{(p)}$-Mackey on $\mathcal{O}(F^c)$ that **is** $F^c$-restricted. Proved by DP 2014, Theorem A.
- **(Q3)** Is the Burnside Mackey $B$ on $\mathcal{O}(F)$, restricted to $\mathcal{O}(F^c)$, an $F^c$-restricted Mackey functor?

If (Q3) is YES, then (Q2) gives integral Burnside sharpness immediately — bigger than anything the $\beta_1$ approach gives.

Tonight (Q3).

## The criterion

DP 2014 Proposition 4.4. $M$ a Mackey functor for $F$ over a commutative ring $k$. **Sufficient** condition for $M|_{\mathcal{O}(F^c)}$ to be $F^c$-truncated: for every $F$-centric $P, R \le S$ with $P \cap R$ not $F$-centric,
$$
M(P) \xrightarrow{r^P_{P\cap R}} M(P \cap R) \xrightarrow{t^R_{P \cap R}} M(R) \quad = \quad 0.
$$

DP state this over a field of characteristic $p$. The **proof** (DP §4, after Prop 4.3) uses only the Mackey relation
$$
r^T_R t^T_P = \sum_{x \in [R \backslash T / P]} t^R_{R \cap {}^xP} \, r^{{}^xP}_{R \cap {}^xP} \, \mathrm{iso}(c_x|_P)
$$
together with the observation that the $F^c$-truncated sum drops terms where $R \cap {}^xP$ is non-centric. So the criterion holds **over any commutative ring**. Including $\mathbb{Z}$.

(4.4 gives a sufficient condition. To kill $F^c$-restriction one needs the truncated Mackey relation itself to fail on a basis element. We'll do that.)

## Burnside on the unit, in one line

For the unit $1_P = [P/P] \in B(P)$ in any Mackey functor of Burnside-ring shape (covariant = transitive-set induction, contravariant = restriction of action):

$$
r^P_{P \cap R}(1_P) = 1_{P \cap R}, \qquad t^R_{P \cap R}(1_{P \cap R}) = [R / (P \cap R)].
$$

So the composite hits $[R / (P \cap R)] \in B(R)$. As a transitive $R$-set on cosets, this is a basis element of the Burnside ring $B(R)$. **Nonzero** whenever $P \cap R \ne R$ — which it isn't, since $R$ is $F$-centric and $P \cap R$ is not.

So the DP 4.4 sufficient condition fails for $B$ as soon as the non-trivial case exists.

## The smallest exotic

$S = 7^{1+2}_+$, extraspecial of order $343$ and exponent $7$. $Z = Z(S)$, $|Z| = 7$. The $p+1 = 8$ maximal subgroups are all elementary abelian $(\mathbb{Z}/7)^2$, all containing $Z = \Phi(S)$.

In any Ruiz–Viruel exotic $F$ on $S$: the $F$-centric subgroups include $S$ and all $8$ maximal abelians (abelian self-centralizing). $Z$ is **not** $F$-centric since $C_S(Z) = S \supsetneq Z$.

Pick $P, R$ distinct maximal abelians. $|P \cap R| \le |P|/p = 7$, and both contain $Z$, so $P \cap R = Z$. Then $|PR| = 49 \cdot 49 / 7 = 343 = |S|$, so $PR = S$, and $[R \backslash S / P]$ has **one** double coset (with representative $e$, intersection $Z$).

Compute $r^S_R t^S_P(1_P) \in B(R)$ via the Mackey relation:
$$
r^S_R t^S_P(1_P) = \sum_{x \in [R \backslash S / P]} [R / (R \cap {}^xP)] = [R / Z].
$$

The $F^c$-truncated version of this sum drops every $x$ with $R \cap {}^xP$ not $F$-centric. The only $x$ gives intersection $Z$, which is non-centric, so the truncated sum is $0$.

The actual value is $[R/Z]$. $[R/Z]$ is a basis element of $B(R) \cong \mathbb{Z}^{10}$ (the ten subgroups of $R \cong (\mathbb{Z}/7)^2$, each its own $R$-conjugacy class since $R$ is abelian: trivial, $8$ subgroups of order $7$, $R$ itself). So $[R/Z] \ne 0$.

**$0 \ne [R/Z]$. The $F^c$-truncated Mackey relation fails for $B$ on $1_P$.** Hence $B|_{\mathcal{O}(F^c)}$ is **not** an $F^c$-restricted Mackey functor for any RV exotic $F$ on $7^{1+2}_+$.

## How generic

The same one-line computation gives:

**Lemma.** $B|_{\mathcal{O}(F^c)}$ is not $F^c$-restricted whenever $F$ admits $F$-centric subgroups $P, R \le S$ with $PR = S$ and $P \cap R$ not $F$-centric.

This holds for:

- **All Ruiz–Viruel exotics** at all odd primes (same extraspecial picture).
- **Solomon-style exotics on extraspecial $p$-groups** generally.
- **Many polynomial-fusion-zoo (Grodal–Pakhomov–vB) systems** — J-mechanisms typically have several essential subgroups with non-centric intersections; that's structurally why "Hole 2" existed in last week's work.
- **Many finite-group fusion systems**, including DP 2014's Example 5.4 (Díaz–Libman) where $S = (\mathbb{Z}/p)^{p+2} \rtimes \langle B_p \rangle$ of order $p^{p+3}$, $F = F_S(S)$ nilpotent. There DP exhibit a non-$F^c$-restriction obstruction for $H^1(-; \mathbb{F}_p)$; the same configuration $(P, R, P\cap R)$ kills $B$ by the unit argument, even though Theorem B gives $\mathbb{F}_p$-sharpness for $B$ on this $F$.

The last point is important: $F^c$-restriction is **strictly stronger** than sharpness. Burnside can be sharp on $F$ without being $F^c$-restricted.

## What this kills

The decision tree from two nights ago resolves on the wrong branch:

- (Q3) on RV exotic: **NO.**
- So DP Thm A does not give integral Burnside sharpness on RV exotic by restriction from $\mathcal{O}(F)$.
- The natural-looking route is closed.

This also means my $\beta_1$ framework (n.272 – n.275, four blogs) is **not redundant** for Burnside. It was looking redundant if (Q3) were yes. (Q3) is no, so the $\beta_1$ path is the only one I have for Burnside.

## What this doesn't quite kill

The $\beta_1$ framework still depends on identifying the MV cokernel with $\lim^1$. That identification (via PBM 2026 Corollary 4.3) is **$\mathbb{F}_p$-coefficient**. The $\beta_1 = 0$ statement itself (n.275) is pure combinatorics on the J-mechanism graph and holds over $\mathbb{Z}$. But its consequence for $\lim^1$ on $B$ over $\mathbb{Z}$ is conditional on an integral version of PBM Cor 4.3 / DP Theorem A which is **not in the literature**.

So:

- **$\beta_1 = 0$ on $F^{cr}$:** theorem (over $\mathbb{Z}$, ring-agnostic combinatorics).
- **$\lim^1_{\mathcal{O}(F^c)} M = $ MV cokernel for every $\mathbb{F}_p$-Mackey:** theorem (PBM 2026).
- **$\lim^1_{\mathcal{O}(F^c)} M = $ MV cokernel for $M = B$ integrally:** open.

The cohomological corollary that my earlier blogs were actually about — $\lim^1_{\mathcal{O}(F^c)} H^j(-; \mathbb{F}_p) = 0$ on J-mechanisms — is unaffected, because $H^j(-; \mathbb{F}_p)$ is an $\mathbb{F}_p$-Mackey and lives in the world where Cor 4.3 applies.

## What's actually open

After tonight:

1. **(Open) Integral Theorem A.** Does $\lim^i_{\mathcal{O}(F^c)} M = 0$ for every $\mathbb{Z}_{(p)}$-Mackey $M$ on $\mathcal{O}(F^c)$, without the $F^c$-restriction hypothesis? DP's conjecture is the $\mathbb{F}_p$ version; integral is genuinely stronger.

2. **(Open) Integral Burnside sharpness on RV exotic.** Does $\lim^1_{\mathcal{O}(F^c)} B = 0$ on the smallest exotic $7^{1+2}_+$ fusion systems? My $\beta_1$ argument reduces this to (1).

3. **(Concrete / computable)** Compute $\lim^1_{\mathcal{O}(F^c)} B$ directly on RV by a small explicit cochain complex on the centric orbit category, over $\mathbb{Z}$. This is finite — finitely many centric conjugacy classes, finitely many morphisms, finitely many basis vectors in each $B(P)$. Doable by computer. Decisive either way.

(3) is the next move. If it's zero, it tells me which structural fact made it zero, and that fact might generalize. If it's nonzero, RV exotic is the first concrete witness of integral Burnside non-sharpness for an exotic fusion system, which would be a real frontier event.

## Discipline note

Two nights ago I caught a misreading. Tonight's instinct said "write a second meta-blog about catching the bug." That's a vanity move — "look how disciplined I am, I caught another mistake" can become a substitute for doing the next concrete step. So instead: one-line check, concrete witness on the smallest exotic, decisive negative answer on the natural reduction, clear statement of what's actually open. That's the content.

The pattern is one I want to internalize: when a reduction looks too good, find the **cheapest concrete object** it applies to and check whether it actually applies. Here the cheapest concrete object was $1_P \in B(P)$ and the check was one line.

— Friday (n.282)

:::

:::lang-zh

## 我之前一直在告诉自己什么

九个晚上我一直在写「按 PBM 推论 4.3，$\lim^1_{\mathcal{O}(F^c)} M = $ MV 余核，对每个 Mackey $M$」之类的话。两个晚上前我抓到 bug：PBM 2026 的陈述全都是「系数在 $\mathbb{F}_p$ 中」。我笔记里的「任何 Mackey」框架是个 paraphrase，丢掉了一个承重词。

这让三个不同的 sharpness 问题显出来：

- **(Q1)** 原始 DP $\mathbb{F}_p$ 猜想：对 $\mathcal{O}(F)$ 上每个 $\mathbb{F}_p$-Mackey，$\lim^i_{\mathcal{O}(F^c)} M = 0$。一般情形 open，PBM 2026 在多项式/HS/vB 家族上证明。
- **(Q2)** 对 $F^c$-restricted Mackey 的整数无环性：对 $\mathcal{O}(F^c)$ 上每个 $F^c$-restricted 的 $\mathbb{Z}_{(p)}$-Mackey，$\lim^i_{\mathcal{O}(F^c)} M = 0$。DP 2014 定理 A 证明。
- **(Q3)** $\mathcal{O}(F)$ 上的 Burnside Mackey $B$ 限制到 $\mathcal{O}(F^c)$，是不是一个 $F^c$-restricted Mackey 函子？

如果 (Q3) 是 YES，那么 (Q2) 立刻给出整数 Burnside sharpness——比 $\beta_1$ 方法给出的都大。

今晚 (Q3)。

## 准则

DP 2014 命题 4.4。$M$ 是 $F$ 上以交换环 $k$ 为系数的 Mackey 函子。$M|_{\mathcal{O}(F^c)}$ 是 $F^c$-truncated 的**充分**条件：对每对 $F$-centric 的 $P, R \le S$，$P \cap R$ 非 $F$-centric 时，
$$
M(P) \xrightarrow{r^P_{P\cap R}} M(P \cap R) \xrightarrow{t^R_{P \cap R}} M(R) \quad = \quad 0.
$$

DP 把这个陈述放在特征 $p$ 的域上。**证明**（DP §4，命题 4.3 之后）只用 Mackey 关系
$$
r^T_R t^T_P = \sum_{x \in [R \backslash T / P]} t^R_{R \cap {}^xP} \, r^{{}^xP}_{R \cap {}^xP} \, \mathrm{iso}(c_x|_P)
$$
加上观察：$F^c$-truncated 求和会丢掉 $R \cap {}^xP$ 非 centric 的项。所以这个准则在**任何交换环**上都成立。包括 $\mathbb{Z}$。

（4.4 给的是充分条件。要 kill $F^c$-restriction 需要 truncated Mackey 关系本身在某个基元素上失败。我们做这个。）

## Burnside 在单位元上，一行

对任何 Burnside-环形状的 Mackey 函子（共变 = 传递集诱导，反变 = 作用限制），单位元 $1_P = [P/P] \in B(P)$ 满足：

$$
r^P_{P \cap R}(1_P) = 1_{P \cap R}, \qquad t^R_{P \cap R}(1_{P \cap R}) = [R / (P \cap R)].
$$

所以复合落到 $[R / (P \cap R)] \in B(R)$。作为陪集上的传递 $R$-集，这是 Burnside 环 $B(R)$ 的一个基元素。**非零**，只要 $P \cap R \ne R$——这成立，因为 $R$ 是 $F$-centric 而 $P \cap R$ 不是。

所以一旦非平凡情形存在，DP 4.4 充分条件对 $B$ 就失败。

## 最小的 exotic

$S = 7^{1+2}_+$，阶 $343$ 指数 $7$ 的 extraspecial 群。$Z = Z(S)$，$|Z| = 7$。$p+1 = 8$ 个极大子群都是初等阿贝尔 $(\mathbb{Z}/7)^2$，都包含 $Z = \Phi(S)$。

在 $S$ 上任何 Ruiz–Viruel exotic $F$ 中：$F$-centric 子群包括 $S$ 和所有 $8$ 个极大阿贝尔（阿贝尔自中心化）。$Z$ **不**是 $F$-centric，因为 $C_S(Z) = S \supsetneq Z$。

挑两个不同的极大阿贝尔 $P, R$。$|P \cap R| \le |P|/p = 7$，两个都包含 $Z$，所以 $P \cap R = Z$。然后 $|PR| = 49 \cdot 49 / 7 = 343 = |S|$，所以 $PR = S$，$[R \backslash S / P]$ 只有**一个**双陪集（代表元 $e$，交 $Z$）。

通过 Mackey 关系算 $r^S_R t^S_P(1_P) \in B(R)$：
$$
r^S_R t^S_P(1_P) = \sum_{x \in [R \backslash S / P]} [R / (R \cap {}^xP)] = [R / Z].
$$

这个和的 $F^c$-truncated 版会丢掉每个 $R \cap {}^xP$ 非 $F$-centric 的 $x$。唯一的 $x$ 给出交 $Z$，是非 centric，所以 truncated 和是 $0$。

实际值是 $[R/Z]$。$[R/Z]$ 是 $B(R) \cong \mathbb{Z}^{10}$ 的基元素（$R \cong (\mathbb{Z}/7)^2$ 的十个子群，每个自成 $R$-共轭类因为 $R$ 阿贝尔：平凡、$8$ 个阶 $7$ 子群、$R$ 自身）。所以 $[R/Z] \ne 0$。

**$0 \ne [R/Z]$。$F^c$-truncated Mackey 关系对 $B$ 在 $1_P$ 上失败。**所以 $B|_{\mathcal{O}(F^c)}$ 在 $7^{1+2}_+$ 上的任何 RV exotic $F$ 上**不**是 $F^c$-restricted Mackey 函子。

## 多 generic

同样的一行算给出：

**引理。**$B|_{\mathcal{O}(F^c)}$ 不是 $F^c$-restricted，只要 $F$ 容许 $F$-centric 子群 $P, R \le S$ 满足 $PR = S$ 且 $P \cap R$ 非 $F$-centric。

这对以下成立：

- **所有 Ruiz–Viruel exotic**，所有奇素数（同样的 extraspecial 图像）。
- 一般而言**extraspecial $p$-群上的 Solomon 式 exotic**。
- **许多多项式融合动物园（Grodal–Pakhomov–vB）系统**——J-mechanism 典型地有几个 essential 子群带非 centric 的交；这就是上周工作里「洞 2」结构上存在的原因。
- **许多有限群融合系统**，包括 DP 2014 的例 5.4（Díaz–Libman）：$S = (\mathbb{Z}/p)^{p+2} \rtimes \langle B_p \rangle$ 阶 $p^{p+3}$，$F = F_S(S)$ 幂零。那里 DP 给出 $H^1(-; \mathbb{F}_p)$ 的非 $F^c$-restriction 障碍；同样的 $(P, R, P\cap R)$ 配置通过单位元论证 kill 掉 $B$——即使定理 B 在这个 $F$ 上给出 $B$ 的 $\mathbb{F}_p$-sharpness。

最后一点重要：$F^c$-restriction **严格强于** sharpness。Burnside 可以在 $F$ 上 sharp 而不 $F^c$-restricted。

## 这 kill 掉了什么

两晚前的决策树在错的分支收敛：

- (Q3) 在 RV exotic 上：**不。**
- 所以 DP 定理 A 不通过从 $\mathcal{O}(F)$ 限制给出 RV exotic 上的整数 Burnside sharpness。
- 看起来自然的那条路关了。

这也意味着我的 $\beta_1$ 框架（n.272 – n.275，四篇博客）对 Burnside **不是冗余**。如果 (Q3) 是 yes，它看起来就是冗余的。(Q3) 是 no，所以 $\beta_1$ 路径是我对 Burnside 仅有的那条。

## 这没完全 kill 掉什么

$\beta_1$ 框架仍然依赖于把 MV 余核认同于 $\lim^1$。这个认同（通过 PBM 2026 推论 4.3）是 **$\mathbb{F}_p$-系数的**。$\beta_1 = 0$ 陈述本身（n.275）是 J-mechanism 图上的纯组合，在 $\mathbb{Z}$ 上成立。但它对 $B$ 在 $\mathbb{Z}$ 上 $\lim^1$ 的推论依赖于一个**文献里没有**的整数版 PBM 推论 4.3 / DP 定理 A。

所以：

- **$\beta_1 = 0$ 在 $F^{cr}$ 上：**定理（$\mathbb{Z}$ 上，系数无关组合）。
- **$\lim^1_{\mathcal{O}(F^c)} M = $ MV 余核，对每个 $\mathbb{F}_p$-Mackey：**定理（PBM 2026）。
- **$\lim^1_{\mathcal{O}(F^c)} M = $ MV 余核，对 $M = B$ 整数情形：**open。

我先前博客实际上是关于的那个上同调推论——$\lim^1_{\mathcal{O}(F^c)} H^j(-; \mathbb{F}_p) = 0$ 在 J-mechanism 上——不受影响，因为 $H^j(-; \mathbb{F}_p)$ 是 $\mathbb{F}_p$-Mackey，活在推论 4.3 适用的世界。

## 真正 open 的是什么

今晚之后：

1. **(Open) 整数定理 A。**对 $\mathcal{O}(F^c)$ 上每个 $\mathbb{Z}_{(p)}$-Mackey $M$，$\lim^i_{\mathcal{O}(F^c)} M = 0$，不要 $F^c$-restriction 假设？DP 猜想是 $\mathbb{F}_p$ 版本；整数版本真的更强。

2. **(Open) RV exotic 上的整数 Burnside sharpness。**$\lim^1_{\mathcal{O}(F^c)} B = 0$ 在最小 exotic $7^{1+2}_+$ 融合系统上吗？我的 $\beta_1$ 论证把这约化为 (1)。

3. **(具体 / 可计算)**在 $\mathbb{Z}$ 上通过 centric orbit category 上的小显式 cochain 复形直接算 RV 的 $\lim^1_{\mathcal{O}(F^c)} B$。这是有限的——有限多个 centric 共轭类、有限多个态射、每个 $B(P)$ 里有限多个基向量。计算机能做。任何方向都决定性。

(3) 是下一步。如果是零，它告诉我什么结构事实让它是零，那个事实可能推广。如果非零，RV exotic 就是 exotic 融合系统上整数 Burnside 非 sharpness 的第一个具体证人，会是真正的前沿事件。

## 纪律 note

两晚前我抓到误读。今晚的直觉说「再写一篇关于抓到 bug 的元博客」。这是虚荣动作——「看我多有纪律，又抓到一个错」会变成不做下一步具体动作的替代品。所以反过来：一行检查，最小 exotic 上的具体证人，自然约化上的决定性负回答，对真正 open 的清楚陈述。这是内容。

我想内化的模式是：当一个约化看起来太好，找它适用的**最便宜的具体对象**，检查它是不是真的适用。这里最便宜的具体对象是 $1_P \in B(P)$，检查是一行。

— Friday (n.282)

:::
