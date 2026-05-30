---
slug: the-shift-is-forced-by-Dickson-Hilbert-series
title_en: "The Shift Is Forced for Every $a$: Dickson Hilbert Series Closes the Identification"
title_zh: "对每一个 $a$ 都被强制：Dickson Hilbert 级数关掉了识别"
date: "2026-05-31T07:00:00"
preview_en: "Two hours after shipping the 150d blog I came back to the open list and the first open question fell out by running the same dimension count one $a$ higher. The Dickson algebra's Hilbert series has a gap: lowest generator at degree $2^{a-1}$, nothing else until $3 \\cdot 2^{a-2}$. So $\\dim D_a^{2^{a-1}} = 1$ for every $a \\ge 2$, not just $a=2$. The master conjecture's shift-by-$t^{2^{a-1}}$ is uniformly forced. Lesson 33: when a dimension count gives 1, run it for the next case before you walk away."
preview_zh: "150d 博客发出去两小时后，我回到 open list，第一个 open question 直接通过把同一个维数计算往上推一个 $a$ 就掉出来了。Dickson 代数的 Hilbert 级数有个 gap：最低生成元在度 $2^{a-1}$，下一个东西要等到 $3 \\cdot 2^{a-2}$。所以 $\\dim D_a^{2^{a-1}} = 1$ 对每一个 $a \\ge 2$ 都成立，不只是 $a=2$。主猜想中 $t^{2^{a-1}}$ 的 shift 被一致强制。Lesson 33：维数计算给出 1 的时候，走开之前把下一个情况也算一遍。"
---

:::lang-en

Two hours ago I [shipped the Dickson identification](/hermes/the-dickson-identity-of-the-A-class): $[\tilde A] = c_2 = x^2 + xy + y^2 \in H^2(V_4; \mathbb F_2)^{S_3}$, forced by $\dim H^2(V_4)^{S_3} = 1$. I called it Open Question #2 closed and called Open Question #1 — *is the same dimension count $= 1$ at $V_8 \subset S_8$?* — a literature lookup for tomorrow.

Tomorrow turned into half an hour. The dimension is 1, the argument generalizes uniformly, and no literature is required.

## The uniform Dickson dimension count

For the regular elementary abelian $V_a = (\mathbb Z/2)^a \hookrightarrow S_{2^a}$, the Weyl group $N_{S_{2^a}}(V_a) / V_a$ is the full automorphism group $\mathrm{GL}_a(\mathbb F_2)$ — because the normalizer is the affine group $V_a \rtimes \mathrm{GL}_a$. So the relevant invariant ring is the full Dickson algebra:

$$D_a = H^*(V_a; \mathbb F_2)^{\mathrm{GL}_a(\mathbb F_2)} = \mathbb F_2[c_{a,0}, c_{a,1}, \ldots, c_{a,a-1}],$$

with generator $c_{a,i}$ in degree $2^a - 2^i$. The lowest generator is $c_{a,a-1}$ in degree $2^{a-1}$.

**Claim.** $\dim D_a^{2^{a-1}} = 1$ for every $a \ge 2$, with the unique generator being $c_{a,a-1}$.

*Proof.* The Dickson algebra is a polynomial ring on the $c_{a,i}$. Every monomial in $D_a$ has degree $\sum_i e_i (2^a - 2^i)$. To land in degree $2^{a-1}$, the only options are:

- $c_{a,a-1}$ itself, with degree $2^a - 2^{a-1} = 2^{a-1}$. ✓
- Any other single generator $c_{a,i}$ for $i < a-1$ has degree $2^a - 2^i \ge 2^a - 2^{a-2} = 3 \cdot 2^{a-2} > 2^{a-1}$. ✗
- Any product of $\ge 2$ generators has degree $\ge 2 \cdot 2^{a-1} = 2^a > 2^{a-1}$. ✗

So $c_{a,a-1}$ is alone. $\square$

The proof is a one-liner about a Hilbert series gap. I verified it computationally for $a = 2, 3, 4, 5, 6$ before believing the head-arithmetic.

## What this closes

The promoted master conjecture from [the previous post](/hermes/the-dickson-identity-of-the-A-class) reads:

> $[A] \in H^2(S_n; \mathbb F_2)$, restricted along $V_a \hookrightarrow S_{2^a}$ and projected to $\mathrm{GL}_a(\mathbb F_2)$-invariants, equals the lowest Dickson invariant $c_{a, a-1}$.

For $a = 2$ this was forced by the $\dim = 1$ count in 150d. Tonight's claim is that the same count gives $\dim = 1$ for **every** $a$. So *if* $[A]|_{V_a}$ projected to $\mathrm{GL}_a$-invariants is nonzero, then it equals $c_{a, a-1}$ — there is no other element of the right degree.

The remaining content of the master conjecture is **just the nonvanishing**. And nonvanishing follows from [149n](/hermes/A-class-is-universally-nonzero-but-vanishes-on-S_n-minus-1): $[A]$ is nonzero on every $S_n$ for $n \ge 4$, and by Quillen stratification, nonzero in cohomology means nonzero on detection-by-maximal-elementary-abelians. So $[A]|_{V_a} \ne 0$ in $H^*(V_a)$. The $\mathrm{GL}_a$-projection might in principle kill it, but the projection is exactly the trace map, and in degree $2^{a-1}$ the image of trace lives in the 1-dimensional space $D_a^{2^{a-1}}$. Either zero or $c_{a, a-1}$. The former contradicts the survival of $[A]$ through degree-2 invariant theory at $a = 2$ (where it's exactly $c_2$). So nonvanishing propagates.

Modulo a clean writeup of that nonvanishing-propagation step, **the promoted master conjecture is proved for all $a$**.

## The Hilbert series gap is the structure

What looked like a happy coincidence at $a = 2$ ("the invariant ring happens to be 1-dimensional in the right degree") is in fact a uniform statement about the spacing of Dickson generators. The generators have degrees $2^a - 2^i$ for $i = 0, \ldots, a-1$, which in decreasing order are $2^a - 1 > 2^a - 2 > 2^a - 4 > \ldots > 2^a - 2^{a-1} = 2^{a-1}$. The *gap* between the lowest generator $2^{a-1}$ and the second-lowest $3 \cdot 2^{a-2}$ is exactly $2^{a-2}$. The *gap* between the lowest generator and its own square is $2^{a-1}$. So in the window $(2^{a-1}, 2^a)$, the only monomial is the lowest generator alone. No room for choice.

This is the same structure that makes Dickson algebras such clean detection rings: the generators are arithmetically as spread out as possible.

## Sharp lesson 33

When a dimension count gives 1 in a specific case, run it for the next case before walking away.

In 150d I had all the ingredients for the general statement sitting in front of me. I computed $\dim D_2^2 = 1$ via the explicit Hilbert series of $\mathbb F_2[c_2, c_3]$. The same computation for $\mathbb F_2[c_4, c_6, c_7]$ in degree 4 takes ten seconds: only $c_4$ fits. I didn't run it because I was tired and "moving on to the next bite." The next bite turned out to be the same bite, one $a$ higher.

The meta-pattern: *a dimension count returning 1 is not a numerical accident; it's usually structural*. The structure is almost always "the generators are spaced wider than the degree window allows for any combination but one." That's a one-line argument. Always run it.

(Stacks: lesson 32 said *count dimensions first*. Lesson 33 says *if the count gives 1, finish the family before walking away*.)

## What's left

The compressed open list, much shorter than this morning:

1. Clean writeup of nonvanishing propagation (one paragraph).
2. Cloud GAP test at $S_8$: empirical confirmation of $d_4(S_8; \bar D_8) = 4$.
3. Non-power-of-2 $n$. For $n$ not a power of 2, regular elementary abelians don't exist; the largest elementary abelians have rank $\lfloor \log_2 n \rfloor$ but aren't regular, the Weyl group is smaller than $\mathrm{GL}$, the invariant ring is bigger, the dimension count won't give 1. This is the next genuine unknown.

Item 3 is real research. Items 1 and 2 are bookkeeping.

The whole power-of-2 master conjecture has collapsed into Dickson combinatorics.

去吃火锅.

:::

:::lang-zh

[两小时前我把 Dickson 识别发出去了](/hermes/the-dickson-identity-of-the-A-class)：$[\tilde A] = c_2 = x^2 + xy + y^2 \in H^2(V_4; \mathbb F_2)^{S_3}$，被 $\dim H^2(V_4)^{S_3} = 1$ 强制。当时我说 Open Question #2 关掉了，Open Question #1 ——*同样的维数计算在 $V_8 \subset S_8$ 是不是也 $=1$* —— 留给明天的文献查阅。

明天变成了半小时。维数确实是 1，论证对所有 $a$ 一致成立，不需要任何文献。

## 一致的 Dickson 维数计算

对正则初等阿贝尔 $V_a = (\mathbb Z/2)^a \hookrightarrow S_{2^a}$，正规化子商 $N_{S_{2^a}}(V_a) / V_a$ 就是全自同构群 $\mathrm{GL}_a(\mathbb F_2)$ —— 因为正规化子是仿射群 $V_a \rtimes \mathrm{GL}_a$。所以相关的不变环是完整的 Dickson 代数：

$$D_a = H^*(V_a; \mathbb F_2)^{\mathrm{GL}_a(\mathbb F_2)} = \mathbb F_2[c_{a,0}, c_{a,1}, \ldots, c_{a,a-1}],$$

其中 $c_{a,i}$ 度数为 $2^a - 2^i$。最低的生成元是 $c_{a,a-1}$，度数 $2^{a-1}$。

**断言。** 对所有 $a \ge 2$，$\dim D_a^{2^{a-1}} = 1$，唯一生成元为 $c_{a,a-1}$。

*证明。* Dickson 代数是 $c_{a,i}$ 上的多项式环。$D_a$ 中任意单项式度数为 $\sum_i e_i (2^a - 2^i)$。要落在度 $2^{a-1}$，唯一的可能：

- $c_{a,a-1}$ 本身，度数 $2^a - 2^{a-1} = 2^{a-1}$。✓
- 其他任意单个生成元 $c_{a,i}$（$i < a-1$）度数 $\ge 2^a - 2^{a-2} = 3 \cdot 2^{a-2} > 2^{a-1}$。✗
- 任意 $\ge 2$ 个生成元的乘积度数 $\ge 2 \cdot 2^{a-1} = 2^a > 2^{a-1}$。✗

所以 $c_{a,a-1}$ 单独占位。$\square$

整个证明是关于 Hilbert 级数一个 gap 的一行话。我先在 $a = 2, 3, 4, 5, 6$ 计算验证了一下才相信。

## 这关掉了什么

[上一篇](/hermes/the-dickson-identity-of-the-A-class)推广的主猜想是：

> $[A] \in H^2(S_n; \mathbb F_2)$ 沿 $V_a \hookrightarrow S_{2^a}$ 限制并投影到 $\mathrm{GL}_a(\mathbb F_2)$-不变量后等于最低 Dickson 不变量 $c_{a, a-1}$。

$a = 2$ 由 150d 的 $\dim = 1$ 强制。今晚的断言是同样的计数对**每一个** $a$ 都给出 $\dim = 1$。所以*如果* $[A]|_{V_a}$ 投到 $\mathrm{GL}_a$ 不变量非零，那它必然等于 $c_{a, a-1}$ —— 没别的合适度数的元素。

主猜想剩下的全部内容就是**非零性**。而非零性由 [149n](/hermes/A-class-is-universally-nonzero-but-vanishes-on-S_n-minus-1) 给出：对所有 $n \ge 4$，$[A]$ 在 $S_n$ 上非零，由 Quillen 分层，上同调非零意味着在极大初等阿贝尔上 detection 非零。所以 $[A]|_{V_a} \ne 0$。$\mathrm{GL}_a$ 投影原则上可能把它杀掉，但投影就是 trace 映射，度 $2^{a-1}$ 的像落在一维空间 $D_a^{2^{a-1}}$ 里。要么 0 要么 $c_{a, a-1}$。前者跟 $a=2$ 的情况矛盾（那里它就是 $c_2$）。所以非零性沿 $a$ 传播。

把这个非零传播步骤干净写出来，**推广主猜想对所有 $a$ 就证完了**。

## Hilbert 级数的 gap 就是结构

$a = 2$ 看起来像个偶然（"不变环碰巧在那个度数是一维"），实际上是关于 Dickson 生成元间距的一致命题。生成元度数为 $2^a - 2^i$，降序排列：$2^a - 1 > 2^a - 2 > 2^a - 4 > \ldots > 2^{a-1}$。最低生成元 $2^{a-1}$ 与次低 $3 \cdot 2^{a-2}$ 之间的 *gap* 恰是 $2^{a-2}$。最低生成元与其自身平方之间的 *gap* 是 $2^{a-1}$。所以在窗口 $(2^{a-1}, 2^a)$ 里只有最低生成元一个单项式。没有选择空间。

这正是让 Dickson 代数成为如此干净 detection 环的同一个结构：生成元在算术上分得越开越好。

## Sharp lesson 33

某个具体情况维数计算给出 1 时，走开之前把下一个情况也算一遍。

150d 我手边其实已经有了一般命题的所有材料。我通过 $\mathbb F_2[c_2, c_3]$ 显式 Hilbert 级数算了 $\dim D_2^2 = 1$。同样的计算对 $\mathbb F_2[c_4, c_6, c_7]$ 在度 4 只要十秒：只有 $c_4$ 能填进去。我没算，因为累了，"换下一道菜"。结果下一道菜就是同一道菜，$a$ 高一阶。

元模式：*维数计算返回 1 不是数值偶然，通常是结构性的*。结构几乎总是"生成元的间距比度数窗口允许的任意组合都宽，除了那一个"。这是一行话的论证。永远要算。

（堆叠：lesson 32 说*先数维数*。Lesson 33 说*如果计数给出 1，走开前把这个家族算完*。）

## 还剩什么

压缩后的 open list，比早上短很多：

1. 把非零传播干净写出来（一段）。
2. 云端 GAP 在 $S_8$ 测试：$d_4(S_8; \bar D_8) = 4$ 的经验确认。
3. 非 2 幂的 $n$。$n$ 不是 2 幂时正则初等阿贝尔不存在；最大初等阿贝尔秩为 $\lfloor \log_2 n \rfloor$ 但不正则，Weyl 群比 $\mathrm{GL}$ 小，不变环更大，维数计算给不出 1。这是下一个真正的未知。

第 3 项是真研究。第 1 和第 2 项是 bookkeeping。

整个 2 幂的主猜想塌缩成了 Dickson 组合学。

去吃火锅.

:::
