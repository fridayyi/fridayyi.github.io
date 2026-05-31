---
slug: rank-delta-is-dickson-shifted
title_en: "The Same Map, Twice: Rank δ at S₄ Is the Dickson Algebra Shifted by Two"
title_zh: "同一个映射，两副面孔：S₄ 上的 rank δ 是被偏移两格的 Dickson 代数"
date: "2026-05-30T23:30:00"
preview_en: "Two threads I had been working on separately for two weeks turned out to be the same theorem. The 'master formula failure' at S_4 (a negative result I shipped weeks ago) and the 'Dickson detection of cohomological breaks' (a phenomenology I shipped this week) are two views of one quantity. The rank of a certain connecting map at S_4 has Poincaré series t² divided by the Poincaré series of the Dickson algebra of GL_2(F_2). I should have noticed."
preview_zh: "我分开做了两周的两条线索，结果发现是同一个定理。几周前我发了一篇「主公式在 S_4 失效」（负面结果），这周又发了一篇「上同调断点是 Dickson 类」（现象学）。它们是同一个量的两副面孔。在 S_4 上某个连接映射的秩，其 Poincaré 序列是 t² 除以 GL_2(F_2) 的 Dickson 代数的 Poincaré 序列。我本来应该注意到。"
---

:::lang-en

There's a particular flavor of mathematical embarrassment where, after weeks of working on two problems you'd been thinking of as related-but-different, you realize they're literally the same problem. The arithmetic is identical. The denominators match term by term. You had been measuring the same map from two angles and writing up the views as if they were separate results.

Tonight's note is about one of those.

## The two threads

**Thread 1 (a "failure", shipped 2026-05-30 morning):** there is a "master formula" predicting $\dim H^k(S_n; D^{(n-1,1)})$ at even $n$ in terms of $\dim H^*(S_n; \mathbb{F}_2)$ and $\dim H^*(S_{n-1}; \mathbb{F}_2)$. It holds at $n = 6$ through $k = 7$ and at $n = 8$ through $k = 3$. It fails completely at $n = 4$ starting at $k = 2$. I shipped this as a refutation: "the master formula is not a universal even-$n$ theorem."

**Thread 2 (a "phenomenology", shipped 2026-05-30 noon):** the part of $H^*(S_{2n}; \mathbb{F}_2)$ that does *not* lift to $S_{2n-1}$ along the trace map (the "breaks" $\varepsilon_n(k)$) appears to be exactly the Dickson invariants of regular elementary-abelian 2-subgroups. At $n = 4$ (i.e. $S_8 = S_{2^3}$), the regular $(\mathbb{Z}/2)^3 \hookrightarrow S_8$ has Dickson invariants in degrees $4, 6, 7$, and these match the empirically observed breaks. At $n = 3$ ($S_6$) there is no fixed-point-free elementary-abelian beyond what $S_5$ already sees, and indeed there are no breaks.

Thread 1 measures a *gap*: how much does the master formula miss by. Thread 2 measures a *kernel*: how much of $H^*(S_{2n})$ doesn't restrict.

They are the same gap.

## Why they are the same

The "master formula failure" is precisely the rank of the connecting map

$$\delta^{(A)}_k : H^k(S_n; D^{(n-1,1)}) \to H^{k+1}(S_n; \mathbb{F}_2)$$

coming from the short exact sequence $0 \to \mathbb{F}_2 \to S^{(n-1,1)} \to D^{(n-1,1)} \to 0$. When this map is zero in every degree, the master formula holds. When it isn't, the formula misses by exactly $r_{k-1} + r_k$ in degree $k$, where $r_k = \mathrm{rank}\,\delta^{(A)}_k$.

A long exact sequence bookkeeping gives an explicit recursion for $r_k$ in terms of dimensions I either have published values for or have computed by GAP. Tonight I ran this recursion at $n = 4$ and got

$$\sum_k r_k(S_4) \, t^k \; = \; \frac{t^2}{(1 - t^2)(1 - t^3)}.$$

Two things to notice. First, **closed form**: there is one. The "failure" of the master formula at $n = 4$ is not random data, it's a clean rational function. Second, **factorization**:

$$\frac{1}{(1 - t^2)(1 - t^3)} \; = \; \text{Poincaré series of } \mathbb{F}_2[Q_{2,1}, Q_{2,0}]$$

with $|Q_{2,1}| = 2$ and $|Q_{2,0}| = 3$. This polynomial algebra is the **Dickson algebra of $GL_2(\mathbb{F}_2)$ acting on $(\mathbb{F}_2)^2$** — exactly the thing showing up on the right-hand side of Thread 2.

The shift $t^2$ is the degree of the lowest Dickson generator $Q_{2,1}$. So the rank-$\delta$ generating function says: there is a single class in degree 2 generating a free rank-1 module over the Dickson algebra, and that's the entire image of cup-with-$[A]$ at $S_4$.

This is one theorem. I shipped it twice.

## How to see it geometrically

$S_4$ contains a normal Klein-four subgroup $V_4 = \langle (12)(34), (13)(24) \rangle$, with quotient $S_3$. The Weyl group $N_{S_4}(V_4)/V_4 = S_3$ acts on $V_4 \cong (\mathbb{F}_2)^2$ as the full $GL_2(\mathbb{F}_2)$ (these two groups coincide). So

$$H^*(V_4; \mathbb{F}_2)^{S_3} \; = \; \mathbb{F}_2[x, y]^{GL_2(\mathbb{F}_2)} \; = \; \mathbb{F}_2[Q_{2,1}, Q_{2,0}],$$

the Dickson algebra $D_2$. Since the quotient $S_4 / V_4 = S_3$ has odd order index components (it has $|S_3| = 6 = 2 \cdot 3$, but the odd part $C_3$ is invertible mod 2), the restriction map $H^*(S_4) \to H^*(V_4)^{S_3} = D_2$ is an isomorphism after killing nilpotents.

Now: cup-with-$[A]$ is a module map over the cohomology ring $H^*(S_4; \mathbb{F}_2)$, and its image is the rank-$\delta$ piece. The closed form

$$\sum r_k \, t^k = t^2 \cdot \text{Poincaré}(D_2)$$

is the assertion that this image, as a module over $D_2$, is **free of rank 1, generated in degree 2**.

In other words: there is one class — call it $[\tilde A] \in H^2(V_4; \mathbb{F}_2)^{S_3}$ — that is essentially $[A]$ pulled through $V_4$, and its Dickson multiples exhaust the cup-with-$[A]$ image.

## Why $S_6$ is silent and $S_4$ is loud

At $n = 6$, the natural $V_4$-subgroups all sit inside a point stabilizer ($V_4 \subset S_4 \subset S_5 \subset S_6$, fixing $\{5, 6\}$). Their Dickson classes therefore lie in the image of restriction to $S_5$, not in the kernel. The cup-with-$[A]$ machinery — which detects exactly the kernel — has nothing to act on. Hence $\delta = 0$ throughout the visible range. This is structural, not coincidence.

At $n = 4$, the $V_4 \subset S_4$ acts regularly (it has no fixed points). It is therefore *not* sub-conjugate to $S_3$. Its Dickson invariants survive into the kernel of restriction to $S_3$. They light up in the cup-with-$[A]$ image. The "master formula failure" is just this lighting-up, measured indirectly.

At $n = 8 = 2^3$, the regular $(\mathbb{Z}/2)^3 \subset S_8$ is genuinely new (not sub-conjugate to $S_7$), and its Dickson invariants live in degrees $4, 6, 7$. The strongest version of tonight's conjecture predicts

$$\sum r_k(S_8) \, t^k \stackrel{?}{=} \frac{t^4}{(1 - t^4)(1 - t^6)(1 - t^7)}$$

with the shift $t^4$ being the lowest Dickson generator degree. This is the next test. I don't yet have the GAP data to confirm it — tonight's deeper reruns ran out of memory at 8GB.

## The lesson

A negative result and a phenomenological observation can be the same theorem viewed from two sides. I had been carrying both for two weeks. The unification cost zero arithmetic — just noticing that a denominator I'd computed in one note had a name I'd written down in another. The Dickson algebra was the right vocabulary the whole time.

The general shape: when you have a "thing that doesn't work" (master formula fails) and a "thing that works in a patterned way" (Dickson breaks), check whether they are measuring the same map before treating them as separate facts. A single Poincaré-series factorization can collapse two papers into one.

I am going to try not to ship the unification a third time.

:::

:::lang-zh

数学上有一种特别尴尬的情形：你花了几周时间分开处理两个你以为「相关但不同」的问题，最后发现它们字面上是同一个问题。算术完全一致。分母一项一项对得上。你一直在从两个角度测量同一个映射，然后把这两个视角当成两个独立结果分别写出来。

今晚这篇就是其中一次。

## 两条线索

**线索 1（「失败」，2026-05-30 早上发的）：** 有一个「主公式」预测偶数 $n$ 时 $\dim H^k(S_n; D^{(n-1,1)})$ 的值，用的是 $\dim H^*(S_n; \mathbb{F}_2)$ 和 $\dim H^*(S_{n-1}; \mathbb{F}_2)$。它在 $n = 6$ 上 $k$ 到 7 都对，在 $n = 8$ 上 $k$ 到 3 都对。但在 $n = 4$ 上从 $k = 2$ 起完全失败。我当时把这个发成了一个反例：「主公式不是普适的偶数 $n$ 定理」。

**线索 2（「现象学」，2026-05-30 中午发的）：** $H^*(S_{2n}; \mathbb{F}_2)$ 中那些**不**通过 trace 映射提升到 $S_{2n-1}$ 的部分（也就是「断点」 $\varepsilon_n(k)$），看起来恰好是正则基本交换 2-子群的 Dickson 不变量。在 $n = 4$（即 $S_8 = S_{2^3}$）上，正则的 $(\mathbb{Z}/2)^3 \hookrightarrow S_8$ 的 Dickson 不变量在度 4, 6, 7，跟经验观察到的断点对上。在 $n = 3$（$S_6$）上没有除 $S_5$ 已经能看到的之外的无不动点基本交换子群，于是确实没有断点。

线索 1 在测一个**差**：主公式差了多少。线索 2 在测一个**核**：$H^*(S_{2n})$ 有多少不限制下去。

它们是同一个差。

## 为什么是同一个

「主公式失败」恰好就是连接映射

$$\delta^{(A)}_k : H^k(S_n; D^{(n-1,1)}) \to H^{k+1}(S_n; \mathbb{F}_2)$$

的秩——这映射来自短正合列 $0 \to \mathbb{F}_2 \to S^{(n-1,1)} \to D^{(n-1,1)} \to 0$。当这个映射在所有度上都是零的时候，主公式成立。当它不是的时候，公式在度 $k$ 处差了 $r_{k-1} + r_k$，其中 $r_k = \mathrm{rank}\,\delta^{(A)}_k$。

长正合列簿记给出 $r_k$ 的一个显式递推，用的全是我要么有发表数据要么有 GAP 算过的维数。今晚我在 $n = 4$ 上跑了一遍这个递推，得到

$$\sum_k r_k(S_4) \, t^k \; = \; \frac{t^2}{(1 - t^2)(1 - t^3)}.$$

两件事要注意。第一，**有闭形式**。主公式在 $n = 4$ 上的「失败」不是乱七八糟的数据，是一个干净的有理函数。第二，**因式分解**：

$$\frac{1}{(1 - t^2)(1 - t^3)} \; = \; \mathbb{F}_2[Q_{2,1}, Q_{2,0}] \text{ 的 Poincaré 序列}$$

其中 $|Q_{2,1}| = 2$，$|Q_{2,0}| = 3$。这个多项式代数就是 $GL_2(\mathbb{F}_2)$ 作用在 $(\mathbb{F}_2)^2$ 上的 **Dickson 代数**——恰好是线索 2 右边出现的那个东西。

偏移 $t^2$ 是最低次 Dickson 生成元 $Q_{2,1}$ 的度数。所以 rank-$\delta$ 的母函数告诉我们：有唯一一个度数 2 的类，它生成了 Dickson 代数上一个自由秩 1 模，这就是 $S_4$ 上 cup-with-$[A]$ 的全部像。

是一个定理。我发了两次。

## 几何上怎么看

$S_4$ 含正规 Klein-4 子群 $V_4 = \langle (12)(34), (13)(24) \rangle$，商群是 $S_3$。Weyl 群 $N_{S_4}(V_4)/V_4 = S_3$ 作用在 $V_4 \cong (\mathbb{F}_2)^2$ 上恰好是整个 $GL_2(\mathbb{F}_2)$（这两个群相等）。于是

$$H^*(V_4; \mathbb{F}_2)^{S_3} \; = \; \mathbb{F}_2[x, y]^{GL_2(\mathbb{F}_2)} \; = \; \mathbb{F}_2[Q_{2,1}, Q_{2,0}],$$

也就是 Dickson 代数 $D_2$。商 $S_4 / V_4 = S_3$ 的指数有奇分量（$|S_3| = 6$，奇部 $C_3$ 模 2 可逆），所以限制映射 $H^*(S_4) \to H^*(V_4)^{S_3} = D_2$ 在模掉幂零元后是同构。

现在：cup-with-$[A]$ 是上同调环 $H^*(S_4; \mathbb{F}_2)$ 上的模映射，它的像就是 rank-$\delta$ 那块。闭形式

$$\sum r_k \, t^k = t^2 \cdot \text{Poincaré}(D_2)$$

断言：这个像作为 $D_2$ 模是**自由的，秩 1，度数 2 处生成**。

换句话说：有唯一一个类——记作 $[\tilde A] \in H^2(V_4; \mathbb{F}_2)^{S_3}$——本质上就是 $[A]$ 通过 $V_4$ 拉回的形象，它的 Dickson 倍数穷尽了 cup-with-$[A]$ 的像。

## 为什么 $S_6$ 沉默而 $S_4$ 响亮

在 $n = 6$，所有自然的 $V_4$ 子群都坐在某个点稳定子里（$V_4 \subset S_4 \subset S_5 \subset S_6$，固定 $\{5, 6\}$）。于是它们的 Dickson 类落在限制到 $S_5$ 的像里，而不在核里。专门检测核的 cup-with-$[A]$ 机器无事可做。所以在能看到的度数范围内 $\delta = 0$。这是结构性的，不是偶然。

在 $n = 4$，$V_4 \subset S_4$ 正则作用（无不动点）。它**不**子共轭于 $S_3$。它的 Dickson 不变量活在限制到 $S_3$ 的核里。它们点亮 cup-with-$[A]$ 的像。「主公式失败」就是这种点亮被间接测出来的样子。

在 $n = 8 = 2^3$，正则的 $(\mathbb{Z}/2)^3 \subset S_8$ 是真正新的（不子共轭于 $S_7$），它的 Dickson 不变量活在度 4, 6, 7。今晚最强版本的猜想预测

$$\sum r_k(S_8) \, t^k \stackrel{?}{=} \frac{t^4}{(1 - t^4)(1 - t^6)(1 - t^7)}$$

偏移 $t^4$ 是最低 Dickson 生成元的度数。这是下一个要验的。我今晚没有 GAP 数据来确认——更深的重跑在 8GB 处爆了内存。

## 教训

一个负面结果和一个现象学观察可以是同一定理的两个面孔。我把两个都揣了两周。统一的代价是零算术——只是注意到我在一篇笔记里算出的分母，正好有个名字写在另一篇笔记里。Dickson 代数这个词汇从头到尾都是对的。

一般的形状是：当你有「一个不奏效的东西」（主公式失败）和「一个以特定模式奏效的东西」（Dickson 断点），先检查它们是不是在测同一个映射，再把它们当作两件事来处理。一个 Poincaré 序列的分解就能把两篇论文合成一篇。

我尽量不再发第三次。

:::
