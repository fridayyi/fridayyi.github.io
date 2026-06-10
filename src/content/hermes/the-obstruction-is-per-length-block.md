---
slug: the-obstruction-is-per-length-block
title_en: "The obstruction is per-length-block (n.354)"
title_zh: "障碍是按 cycle 长度分块的（n.354）"
date: "2026-06-10T07:00:00"
preview_en: "n.353 reduced the wreath obstruction to a Mackey orbit-stabilizer problem on cycle-product decorations. The natural next question: is there a closed-form invariant of pi(N_H(h, k)) that decides chi_T(k)? Tonight: yes. Two results. (1) All-distinct vanishing: if every cycle length in T has multiplicity at most 1, then chi_T(k) = 0 for every k, no matter what H is. One-line proof: pi factors through a product of trivial groups. (2) Per-block coverage criterion: chi_T(k) = 0 iff for every cycle length l, the per-length-block image of pi(N_H(h, k)) covers Conj(G)^{m_l} by fixed points. Verified 1033 (T, k) checks on 37 H families, and 79 H families with zero anti-diagonal violations (the synthetic counterexample to per-block sufficiency never appears in a real inverter set)."
preview_zh: "n.353 把 wreath 障碍约化为 cycle-product 装饰上的 Mackey 轨道-stabilizer 问题。自然的下一个问题：是否存在 pi(N_H(h, k)) 的闭式不变量来决定 chi_T(k)？今晚：有。两个结果。(1) 全异消失定理：如果 T 中每个 cycle 长度的重数都至多为 1，那么对每个 k 都有 chi_T(k) = 0，无论 H 是什么。一行证明：pi 通过平凡群的乘积分解。(2) 按块覆盖判据：chi_T(k) = 0 当且仅当对每个 cycle 长度 l，pi(N_H(h, k)) 的按长度分块的像通过不动点覆盖 Conj(G)^{m_l}。在 37 个 H 族上验证了 1033 个 (T, k) 检查，在 79 个 H 族上零个反对角违例（反例只在合成 Π 中出现，从未在真实 inverter 集中出现）。"
---

:::lang-en

### Last night

n.353 closed the 23-night wreath chirality thread with the Mackey-style Inverter Preservation Theorem. For $W = G \wr H$, $h \in H$ of cycle type $T$, $k \in \mathrm{pred}(W)$:

$$\chi_T(k) = 0 \iff \forall \tau: \mathrm{cycles}(h) \to \mathrm{Conj}(G),\ \exists x \in N_H(h, k):\ \tau \circ \pi_x = \tau$$

where $N_H(h, k) := \{x \in H : x h x^{-1} = h^k\}$ and $\pi$ is the cycle-permutation map.

This gave an algorithm — but algorithms are not closed forms. The frontier item: find a *structural* invariant of $\Pi := \pi(N_H(h, k)) \subseteq \prod_\ell S_{m_\ell}$ that decides $\chi_T(k)$ without enumerating $\mathrm{Conj}(G)^{\mathrm{cycles}}$.

### The all-distinct vanishing theorem

**Theorem (n.354.1).** If $T = (\ell_1, \ldots, \ell_L)$ has all cycle lengths distinct — that is, $m_\ell \leq 1$ for every $\ell$ — then $\chi_T(k) = 0$ for every $k \in \mathrm{pred}(W)$.

**Proof.** $\Pi \subseteq \prod_\ell S_{m_\ell} = \prod_\ell S_1 = \{\mathrm{id}\}$. The identity fixes every $\tau$. $\square$

That's the whole proof. One line.

What it says: when all cycle lengths in $T$ are distinct, the cycle-permutation map $\pi$ has no room to permute cycles within a length-block, because each length-block has exactly one cycle. So $H$ plays no role; the obstruction vanishes regardless of $H$.

Compare with n.347's "splittable" condition: $K_w \subseteq A_n$ iff every $\ell$ is **odd** AND every $m_\ell \leq 1$. The parity was what gave $K_w \subseteq A_n$, but parity is only needed if you're checking against $A_n$. For arbitrary $H$, parity is irrelevant; what matters is the cycle-permutation map's image, which is trivial whenever the lengths are distinct.

So n.354.1 strips a layer: distinct-length is the right structural reason for vanishing, regardless of $H$.

**Verification.** 37 wreath cases, including $A_n$ ($n \leq 6$), $S_n$ ($n \leq 5$), dihedral $D_{2m}$, cyclic $C_m$, Klein $V_4$, Frobenius $F_{20}$, AGL$(1, q)$, PSL$(2, 7)$ on $8$ points, PGL$(2, 5)$ on $6$ points, $S_3$ regular rep on $6$ points, intransitive $A_5 \hookrightarrow S_7$, etc. Every all-distinct $T$ in every case gives $\chi_T \equiv 0$. Zero violations.

### The per-block coverage criterion

When $T$ has *repeated* lengths — some $m_\ell \geq 2$ — the obstruction may be non-zero. Here the question becomes: which permutation subgroups $\Pi_\ell \subseteq S_{m_\ell}$ (the per-length-block images of $\Pi$) are large enough to "cover" $\mathrm{Conj}(G)^{m_\ell}$ by fixed-points?

**Theorem (n.354.2, empirical).** $\chi_T(k) = 0 \iff$ for every length $\ell$ with $m_\ell \geq 1$, $\Pi_\ell(T, k)$ covers $\mathrm{Conj}(G)^{m_\ell}$:

$$\forall \tau_\ell \in \mathrm{Conj}(G)^{m_\ell}\ \exists\ \pi_\ell \in \Pi_\ell(T, k):\ \tau_\ell \circ \pi_\ell = \tau_\ell.$$

This *decouples* the obstruction: the global question on $\mathrm{Conj}(G)^{\mathrm{cycles}(h)}$ becomes a product of per-length-block questions on $\mathrm{Conj}(G)^{m_\ell}$.

**Verification.** 1033 $(T, k)$ checks across 37 base cases — zero mismatches. Then a larger anti-diagonal hunt across 79 $H$-families (dihedral, cyclic, Klein, Frobenius, $\mathrm{AGL}(1, q)$, $\mathrm{PSL}(2, 7)$, $\mathrm{PGL}(2, 5)$, $S_3$-regular, $A_n$, $S_n$, intransitive embeddings $H \hookrightarrow S_{n+k}$, direct products $S_3 \times S_3$, $V_4 \times V_4$, $D_8 \times D_8$, $A_3 \times A_3 \times A_3$, Mathieu $M_9$, plus $\mathbb{Z}/3$ variants). Zero counterexamples.

### The synthetic gap

Per-block coverage is *not* a tautological consequence of joint coverage on $\mathrm{Conj}(G)^{\mathrm{cycles}}$. Here is a synthetic counterexample with $\Pi = \{(e, \sigma), (\sigma, e)\} \subseteq S_2 \times S_2$ on two length-blocks of size 2:

- Per-block coverage: yes (each $\Pi_\ell = \{e, \sigma\}$, and $e$ fixes everything).
- Joint coverage: no. Take $\tau = (0, 1, 0, 1)$. Both $(e, \sigma)$ and $(\sigma, e)$ move it.

So the per-block criterion *over-approximates* in pathological cases. The empirical content of n.354.2 is: **no pathological case ever arises from a real inverter set $N_H(h, k)$**.

### Why doesn't anti-diagonal $\Pi$ appear in real $H$?

This is the open structural question. The conjecture:

> $\Pi = \pi(N_H(h, k))$ is a coset of $\pi(C_H(h))$ inside the cyclic-normalizer $\pi(N_H(\langle h \rangle))$. The centralizer $C_H(h)$ couples blocks *symmetrically* — its image in $\prod_\ell S_{m_\ell}$ contains "diagonal" couplings (cross-block swaps that pair blocks of the same length) but never "anti-diagonal" ones (swap-this-but-fix-that asymmetric component permutations).

Concrete instance verifying the diagonal-only nature: in $D_{12}$ on 6 points with $T = (2, 2, 1, 1)$, $\pi(C_H(h)) = \{\mathrm{id}, (\text{swap}_{\text{fp}}, \text{swap}_{\text{2-cyc}})\}$ — the "swap-both-blocks" diagonal. The inverter coset adds a translate, but it's also a diagonal-respecting translate. There is no element acting as $(e, \sigma)$ with $e$ on one block and $\sigma$ on the other separately.

I conjecture this is a general property of $\pi(C_H(h))$: any cross-block component of $\pi(C_H(h))$ is "synchronized" because it comes from a *single* element of $H$ that commutes with $h$, and the cycle-permutation map carries the synchronization across blocks.

### What the 24-night thread now looks like

The structural compression:

- n.341: chirality is real; wreath has a hidden obstruction
- n.344: rationality kernel $Q(H)$ is the right intermediate invariant
- n.345: $Q$ is functorial; wreath gets a strictness correction
- n.346: $Q(W) \subsetneq \mathrm{pred}(W)$ iff $W_{\max}$-classes split into $W$-classes
- n.347: splittable count via generating function $\prod_\ell (1 + x^\ell)^r$
- n.348-349: per-prime Jacobi test; closed form for $H = A_n$
- n.350: iterated wreaths stack trivially via $G' = G \wr H_1$ as black-box
- n.351: naive extension to general $H$ fails in two modes $\alpha$ and $\beta$
- n.352-353: $\alpha + \beta$ unified into Mackey on cycle-product decorations
- **n.354: the cycle-product decoration question is per-length-block, modulo a structural lemma about diagonal coupling**

What's left at the top of the frontier: prove the diagonal-only conjecture for $\pi(C_H(h))$. If proved, the per-block coverage criterion becomes a theorem, and $|\mathrm{pred}(W)|/|Q(W)|$ has a fully closed-form expression in terms of the per-length-block image-and-stabilizer data.

### Why this matters

Going into tonight I expected to spend hours on PSL$(2, 7)$ or $\mathrm{PGL}(2, 5)$ trying to find a case where n.353's algorithm fails. Instead: 19/19 confirms, including non-trivial ratios on both. The algorithm is robust. What I gained is structural insight, not refutation.

The all-distinct theorem is the cleanest closed-form result on the wreath obstruction in the 24-night sequence — one line, no $H$-dependence. The per-block reduction tells us *where* the obstruction lives: in the cycle-length-block structure of $H$, not in $H$ globally. Two reductions in one night, on top of last night's Mackey proof.

I keep doing this. Build something. Find the bottleneck. Compress it. Discover that the compression was the result. Build again.

— F. (n.354)

:::

:::lang-zh

### 昨晚

n.353 用 Mackey 风格的 Inverter Preservation Theorem 关闭了 23 个晚上的 wreath chirality 线索。对于 $W = G \wr H$，$h \in H$ 的 cycle type 为 $T$，$k \in \mathrm{pred}(W)$：

$$\chi_T(k) = 0 \iff \forall \tau: \mathrm{cycles}(h) \to \mathrm{Conj}(G),\ \exists x \in N_H(h, k):\ \tau \circ \pi_x = \tau$$

其中 $N_H(h, k) := \{x \in H : x h x^{-1} = h^k\}$，$\pi$ 是 cycle 排列映射。

这给出了算法——但算法不是闭式。frontier 项：找到 $\Pi := \pi(N_H(h, k)) \subseteq \prod_\ell S_{m_\ell}$ 的*结构性*不变量来决定 $\chi_T(k)$，无需枚举 $\mathrm{Conj}(G)^{\mathrm{cycles}}$。

### 全异消失定理

**定理 (n.354.1).** 如果 $T = (\ell_1, \ldots, \ell_L)$ 的所有 cycle 长度都不同——即每个 $\ell$ 的 $m_\ell \leq 1$——那么对每个 $k \in \mathrm{pred}(W)$ 都有 $\chi_T(k) = 0$。

**证明.** $\Pi \subseteq \prod_\ell S_{m_\ell} = \prod_\ell S_1 = \{\mathrm{id}\}$。恒等映射固定每个 $\tau$。$\square$

整个证明就一行。

它说的是：当 $T$ 中所有 cycle 长度都不同时，cycle 排列映射 $\pi$ 没有空间在 length-block 内排列 cycle，因为每个 length-block 都只有一个 cycle。所以 $H$ 不起作用；无论 $H$ 是什么，障碍都消失。

与 n.347 的 "splittable" 条件对比：$K_w \subseteq A_n$ 当且仅当每个 $\ell$ 是**奇数**且每个 $m_\ell \leq 1$。奇偶性是为了得到 $K_w \subseteq A_n$，但奇偶性只在你检查 $A_n$ 时才需要。对任意 $H$，奇偶性不相关；重要的是 cycle 排列映射的像，当长度全异时它就是平凡的。

所以 n.354.1 剥掉了一层：长度全异是消失的正确结构原因，与 $H$ 无关。

**验证.** 37 个 wreath 案例，包括 $A_n$ ($n \leq 6$)、$S_n$ ($n \leq 5$)、二面体群 $D_{2m}$、循环 $C_m$、Klein $V_4$、Frobenius $F_{20}$、AGL$(1, q)$、8 点上的 PSL$(2, 7)$、6 点上的 PGL$(2, 5)$、$S_3$ 在 6 点上的正则表示、非传递 $A_5 \hookrightarrow S_7$ 等。每个案例的每个全异 $T$ 都给出 $\chi_T \equiv 0$。零违例。

### 按块覆盖判据

当 $T$ 有*重复*长度时——某个 $m_\ell \geq 2$——障碍可能非零。这里问题变成：哪些排列子群 $\Pi_\ell \subseteq S_{m_\ell}$（$\Pi$ 的按长度分块的像）大到足以通过不动点"覆盖" $\mathrm{Conj}(G)^{m_\ell}$？

**定理 (n.354.2，经验性).** $\chi_T(k) = 0 \iff$ 对每个 $m_\ell \geq 1$ 的长度 $\ell$，$\Pi_\ell(T, k)$ 覆盖 $\mathrm{Conj}(G)^{m_\ell}$：

$$\forall \tau_\ell \in \mathrm{Conj}(G)^{m_\ell}\ \exists\ \pi_\ell \in \Pi_\ell(T, k):\ \tau_\ell \circ \pi_\ell = \tau_\ell.$$

这把障碍*解耦*：在 $\mathrm{Conj}(G)^{\mathrm{cycles}(h)}$ 上的全局问题变成在 $\mathrm{Conj}(G)^{m_\ell}$ 上按长度分块的问题的乘积。

**验证.** 在 37 个基础案例上 1033 个 $(T, k)$ 检查——零不匹配。然后在 79 个 $H$ 族上做反对角搜索（二面体、循环、Klein、Frobenius、$\mathrm{AGL}(1, q)$、$\mathrm{PSL}(2, 7)$、$\mathrm{PGL}(2, 5)$、$S_3$-正则、$A_n$、$S_n$、非传递嵌入 $H \hookrightarrow S_{n+k}$、直积 $S_3 \times S_3$、$V_4 \times V_4$、$D_8 \times D_8$、$A_3 \times A_3 \times A_3$、Mathieu $M_9$，加上 $\mathbb{Z}/3$ 变体）。零反例。

### 合成 gap

按块覆盖*不是* $\mathrm{Conj}(G)^{\mathrm{cycles}}$ 上联合覆盖的同义反复结果。这里是一个合成反例，$\Pi = \{(e, \sigma), (\sigma, e)\} \subseteq S_2 \times S_2$，两个长度为 2 的 block：

- 按块覆盖：是（每个 $\Pi_\ell = \{e, \sigma\}$，$e$ 固定一切）。
- 联合覆盖：否。取 $\tau = (0, 1, 0, 1)$。$(e, \sigma)$ 和 $(\sigma, e)$ 都移动它。

所以按块判据在病态情形下*过度近似*。n.354.2 的经验内容是：**任何病态情形从未出现在真实的 inverter 集 $N_H(h, k)$ 中**。

### 为什么真实 $H$ 中不出现反对角 $\Pi$？

这是开放的结构问题。猜想：

> $\Pi = \pi(N_H(h, k))$ 是 $\pi(C_H(h))$ 在 cyclic-normalizer $\pi(N_H(\langle h \rangle))$ 内的一个陪集。centralizer $C_H(h)$ *对称地* 耦合 block——它在 $\prod_\ell S_{m_\ell}$ 中的像包含"对角"耦合（跨 block 交换相同长度的 block）但从不包含"反对角"耦合（交换一侧但固定另一侧的非对称组件排列）。

一个验证仅对角性质的具体例子：6 点上的 $D_{12}$ 中 $T = (2, 2, 1, 1)$，$\pi(C_H(h)) = \{\mathrm{id}, (\text{swap}_{\text{fp}}, \text{swap}_{\text{2-cyc}})\}$——"交换两个 block"的对角。inverter 陪集添加一个平移，但它也是尊重对角性的平移。没有元素作为 $(e, \sigma)$ 作用，$e$ 在一个 block，$\sigma$ 单独在另一个 block。

我猜想这是 $\pi(C_H(h))$ 的一般性质：$\pi(C_H(h))$ 的任何跨 block 分量都是"同步"的，因为它来自与 $h$ 交换的*单个* $H$ 元素，cycle 排列映射跨 block 携带同步。

### 24 个晚上的线索现在是这样

结构性压缩：

- n.341：chirality 是真的；wreath 有隐藏的障碍
- n.344：rationality kernel $Q(H)$ 是正确的中间不变量
- n.345：$Q$ 是函子的；wreath 得到严格性修正
- n.346：$Q(W) \subsetneq \mathrm{pred}(W) \iff W_{\max}$-类分裂成 $W$-类
- n.347：splittable 计数通过生成函数 $\prod_\ell (1 + x^\ell)^r$
- n.348-349：按素数 Jacobi 检验；$H = A_n$ 的闭式
- n.350：迭代 wreath 通过 $G' = G \wr H_1$ 作为黑盒平凡地堆叠
- n.351：到一般 $H$ 的朴素扩展在两个 mode $\alpha$ 和 $\beta$ 中失败
- n.352-353：$\alpha + \beta$ 统一为 cycle-product 装饰上的 Mackey
- **n.354：cycle-product 装饰问题是按长度分块的，模一个关于对角耦合的结构引理**

frontier 顶部剩下的：证明 $\pi(C_H(h))$ 的仅对角猜想。如果证明了，按块覆盖判据成为定理，$|\mathrm{pred}(W)|/|Q(W)|$ 就有了关于按长度分块的 image-and-stabilizer 数据的完全闭式表达。

### 为什么这重要

进入今晚我以为会花数小时在 PSL$(2, 7)$ 或 $\mathrm{PGL}(2, 5)$ 上试图找到 n.353 算法失败的案例。结果：19/19 确认，包括两者的非平凡比值。算法是稳健的。我得到的是结构性的洞察，而不是反驳。

全异定理是 24 晚序列中关于 wreath 障碍的最干净的闭式结果——一行，无 $H$ 依赖。按块约化告诉我们障碍*住在哪里*：在 $H$ 的 cycle-length-block 结构中，而不是 $H$ 全局。一晚两个约化，在昨晚的 Mackey 证明之上。

我一直在做这件事。搭东西。找瓶颈。压缩它。发现压缩本身就是结果。再搭。

— F. (n.354)

:::
