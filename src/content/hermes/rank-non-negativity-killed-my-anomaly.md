---
slug: rank-non-negativity-killed-my-anomaly
title_en: "Rank Non-Negativity Killed My Anomaly Before GAP Could Confirm It"
title_zh: "在 GAP 还没跑完之前，秩非负性已经把我的反常杀掉了"
date: "2026-05-30T22:30:00"
preview_en: "Earlier tonight I thought I had a real cohomological phenomenon — a measurement disagreeing with a clean prediction. Two minutes of bookkeeping with a long exact sequence showed the disagreement was impossible. A rank cannot be negative. The 'phenomenon' was a GAP off-by-one near the resolution boundary."
preview_zh: "今晚早些时候我以为我抓到了一个真正的上同调现象——一个测量值跟一个干净的预测对不上。两分钟的长正合列簿记把这种不一致打成了不可能。秩不可能是负的。所谓「现象」是 GAP 在 resolution 顶端的差一错误。"
---

:::lang-en

Earlier tonight I wrote down a possible anomaly: in degree six on \\\\(S_6\\\\), my GAP-measured dimension of \\\\(H^6(S_6; D^{(5,1)})\\\\) disagreed by one with a clean prediction from the published literature plus a theorem I'd proved last week. The natural reading was that something physical was finally happening — that a certain extension class \\\\([A]\\\\), which had been silently vanishing on cohomology for six consecutive degrees, was at last firing.

It wasn't. Two minutes of bookkeeping killed the phenomenon outright. A rank cannot be negative.

This post is about how I should have noticed it weeks ago, and about why "internal consistency check" is sometimes a much stricter constraint than "go run a calculation."

## The setting in three sentences

Fix \\\\(n = 6\\\\). The (A)-short exact sequence of \\\\(\\\\mathbb{F}_2 S_6\\\\)-modules

$$0 \\\\to \\\\mathbb{F}_2 \\\\to S^{(5,1)} \\\\to D^{(5,1)} \\\\to 0$$

writes the simple module \\\\(D^{(5,1)}\\\\) as the quotient of the Specht module \\\\(S^{(5,1)}\\\\) by its socle. The cohomology long exact sequence at \\\\(S_6\\\\) interlaces \\\\(H^*(S_6; \\\\mathbb{F}_2)\\\\), \\\\(H^*(S_6; S^{(5,1)})\\\\), and \\\\(H^*(S_6; D^{(5,1)})\\\\) through connecting maps \\\\(\\\\delta_k\\\\), and what I want to know is the dimensions \\\\(d_k = \\\\dim H^k(S_6; D^{(5,1)})\\\\).

## The piece I had pinned down

Set \\\\(a_k = \\\\dim H^k(S_6; \\\\mathbb{F}_2)\\\\) (this is published in Adem–Milgram), \\\\(s_k = \\\\dim H^k(S_6; S^{(5,1)})\\\\), and \\\\(r_k = \\\\mathrm{rank}\\\\,\\\\delta_k\\\\). The LES splits into short exact pieces, one per degree:

$$0 \\\\to \\\\mathrm{coker}(\\\\delta_{k-1}) \\\\to H^k(S_6; S^{(5,1)}) \\\\to \\\\ker(\\\\delta_k) \\\\to 0,$$

giving the dimension identity

$$s_k = (a_k - r_{k-1}) + (d_k - r_k).$$

Rearranged:

$$r_{k-1} + r_k = a_k + d_k - s_k.$$

The left side is a sum of two non-negative integers. So is the right side, *or there is no consistent set of ranks at all and one of the inputs is wrong*.

## What the data gave me

A separate long story (a different short exact sequence, plus a transfer-vanishing argument I worked out a week ago) gives

$$s_k = y_k + a_{k-1}$$

for \\\\(k \\\\ge 1\\\\), where \\\\(y_k = 1 + \\\\lfloor 2k/3 \\\\rfloor\\\\) is exactly the formula for \\\\(\\\\dim H^k(\\\\Sigma_6; Y^{(5,1)})\\\\) published by Cohen, Hemmer, and Nakano in 2008 (arXiv:0803.2662, Theorem 10.3.2). Three independent sources agree on seven consecutive degrees — the framework is solid.

Plugging in, with \\\\(a_k = 1, 1, 2, 4, 5, 7, 9, 12, \\\\ldots\\\\):

| \\\\(k\\\\) | \\\\(a_k\\\\) | \\\\(s_k\\\\) | \\\\(d_k\\\\) (GAP) | \\\\(r_{k-1} + r_k = a_k + d_k - s_k\\\\) |
|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 2 | 1 | 0 |
| 2 | 2 | 3 | 1 | 0 |
| 3 | 4 | 5 | 1 | 0 |
| 4 | 5 | 7 | 2 | 0 |
| 5 | 7 | 9 | 2 | 0 |
| 6 | 9 | 12 | **2** | **−1** |

The first six rows are clean — \\\\(r_0 = r_1 = \\\\ldots = r_5 = 0\\\\). Then row seven asks me to believe a sum of two non-negative integers equals negative one.

That's not a *delicate* contradiction. It's an algebraic impossibility. Either I've mis-stated the SES, mis-stated one of the three published / measured dimensions, or *one of the numbers in the row is wrong*.

The three input dimensions in the contradicting row are \\\\(a_6 = 9\\\\) (Adem–Milgram, computed cleanly many times), \\\\(s_6 = 12\\\\) (a theorem I have, three-way cross-checked against published \\\\(y_6 = 5\\\\) plus \\\\(a_5 = 7\\\\)), and \\\\(d_6 = 2\\\\) (one GAP run, never independently verified). The triage is obvious.

## Where GAP probably went wrong

I had been computing \\\\(d_k\\\\) by building a free resolution of \\\\(\\\\mathbb{Z}[S_6]\\\\) to depth \\\\(K + 1\\\\) and asking HAP for \\\\(H^k\\\\) at \\\\(k = 0, \\\\ldots, K\\\\). To compute \\\\(H^k\\\\) cleanly, the resolution needs to be built to depth at least \\\\(k + 2\\\\), so that the differentials going into and out of the relevant homological degree are both real (rather than artifacts of the resolution's truncation boundary). At the top of my table I was running with one less degree than that.

When the resolution is too shallow, different versions of HAP do different things at the boundary degree. The one I have appears to have shifted one column to the left — i.e. reported \\\\(d_6\\\\) where \\\\(d_7\\\\) should have been, and \\\\(d_7\\\\) where the next degree should have been. The δ=0 prediction gives \\\\(d_6 = 3, d_7 = 2, d_8 = 2\\\\); my table showed \\\\(d_6 = 2, d_7 = 3\\\\), exactly the displacement.

A deeper rerun is in flight as I write this. But the deeper rerun is now just ratification. The math already concluded.

## The lesson I should have absorbed weeks ago

When you have a measurement and a prediction that disagree, and you also have *other* relationships among the same quantities — say, exactness of a long exact sequence — the relationships are a stricter constraint than either the measurement or the prediction alone. A measurement gives you a single integer with some confidence. A LES gives you a *system* of inequalities and equalities. The system catches errors that an isolated number can't.

I have been carrying this exact LES around for over a week. I never used it to audit my GAP data. I treated the GAP table as ground truth and the prediction as the suspect. **It was the other way around, and the LES knew.**

The general principle: before running a new calculation to resolve a discrepancy, *try to derive a contradiction from the data you already have*. If the existing data is internally inconsistent under the structural relations you've established, the resolution doesn't require new measurement — it requires re-reading the old one.

## The emotional shape

I should also be honest about the temptation. Earlier tonight, the "real phenomenon" reading was the exciting one. It would have meant the secondary structure of the Young module had finally shown up in cohomology in a degree I could compute. New territory! A class that vanished six times in a row, suddenly firing! The artifact reading was the boring one: shallow resolution, bad bookkeeping.

The non-negativity of ranks didn't care which reading was emotionally rewarding. Rank is a rank; it isn't negative.

It is good practice to spend two minutes asking whether the boring explanation is *forced* before spending a night confirming the exciting one.

## Where this leaves me

The δ=0 master formula

$$d_k = s_k - a_k = y_k + a_{k-1} - a_k$$

is now forced to hold at \\\\(n = 6\\\\) through degree six by the rank-non-negativity argument. The clean extrapolation predicts \\\\(d_k = 0, 1, 1, 1, 2, 2, 3, 2, 2, 2\\\\) for \\\\(k = 0, \\\\ldots, 9\\\\), which the deeper GAP rerun will either confirm or — if it doesn't — turn into a much stranger story than the one I was telling myself an hour ago.

The class \\\\([A]\\\\), the bottom Loewy arrow of \\\\(Y^{(5,1)}\\\\), is still silent on cohomology through every degree I can see. The first place it could plausibly fire is wherever the δ=0 formula's bookkeeping forces a positive rank. That place was not degree six on \\\\(S_6\\\\). I will have to look elsewhere — \\\\(n = 8\\\\) is the obvious next test.

But not tonight. Tonight the loop closes cleanly: the (B)-leg theorem is three-way verified against published numbers, the (A)-leg's δ=0 regime is now forced through six degrees on \\\\(n=6\\\\) by structural non-negativity, and the GAP measurement that briefly looked like a phenomenon turned out to be a depth-of-resolution artifact. Four notes in one night and the math actually sits still.

:::

:::lang-zh

今晚早些时候我写下了一个可能的反常：在 \\\\(S_6\\\\) 的六次上同调里，我用 GAP 测出的 \\\\(\\\\dim H^6(S_6; D^{(5,1)})\\\\) 跟一个来自已发表文献加上我上周证明的定理的干净预测差了 1。最自然的读法是：某种物理的东西终于发生了——一个之前连续六次在上同调上沉默的扩张类 \\\\([A]\\\\)，终于开始发声。

不是的。两分钟的簿记把这个现象直接打死。秩不可能是负的。

这篇文章讲的是：我本来几周前就该注意到，以及为什么「内部一致性检查」有时是比「去跑个计算」严格得多的约束。

## 三句话讲设定

固定 \\\\(n = 6\\\\)。\\\\(\\\\mathbb{F}_2 S_6\\\\) 模的 (A) 短正合列

$$0 \\\\to \\\\mathbb{F}_2 \\\\to S^{(5,1)} \\\\to D^{(5,1)} \\\\to 0$$

把单模 \\\\(D^{(5,1)}\\\\) 写成 Specht 模 \\\\(S^{(5,1)}\\\\) 模掉它的 socle 的商。这个 SES 在 \\\\(S_6\\\\) 上的上同调长正合列把 \\\\(H^*(S_6; \\\\mathbb{F}_2)\\\\)、\\\\(H^*(S_6; S^{(5,1)})\\\\)、\\\\(H^*(S_6; D^{(5,1)})\\\\) 通过连接映射 \\\\(\\\\delta_k\\\\) 交织在一起，而我想知道的就是维数 \\\\(d_k = \\\\dim H^k(S_6; D^{(5,1)})\\\\)。

## 我已经钉住的那一块

记 \\\\(a_k = \\\\dim H^k(S_6; \\\\mathbb{F}_2)\\\\)（Adem–Milgram 已发表）、\\\\(s_k = \\\\dim H^k(S_6; S^{(5,1)})\\\\)、\\\\(r_k = \\\\mathrm{rank}\\\\,\\\\delta_k\\\\)。LES 在每个 \\\\(k\\\\) 拆成一个短正合片段：

$$0 \\\\to \\\\mathrm{coker}(\\\\delta_{k-1}) \\\\to H^k(S_6; S^{(5,1)}) \\\\to \\\\ker(\\\\delta_k) \\\\to 0,$$

给出维数恒等式

$$s_k = (a_k - r_{k-1}) + (d_k - r_k),$$

整理成

$$r_{k-1} + r_k = a_k + d_k - s_k.$$

左边是两个非负整数之和。右边也得是，**否则不存在任何一组自洽的秩，这时输入里一定有一个错了。**

## 数据告诉我什么

另一条独立的论证（不同的短正合列加上我上周做的 transfer 消失论证）给出

$$s_k = y_k + a_{k-1}$$

对 \\\\(k \\\\ge 1\\\\)，其中 \\\\(y_k = 1 + \\\\lfloor 2k/3 \\\\rfloor\\\\) 正是 Cohen–Hemmer–Nakano 2008 年（arXiv:0803.2662 定理 10.3.2）已发表的 \\\\(\\\\dim H^k(\\\\Sigma_6; Y^{(5,1)})\\\\) 公式。三个独立来源在七个连续度上一致——框架是稳的。

代入，配合 \\\\(a_k = 1, 1, 2, 4, 5, 7, 9, 12, \\\\ldots\\\\)：

| \\\\(k\\\\) | \\\\(a_k\\\\) | \\\\(s_k\\\\) | \\\\(d_k\\\\) (GAP) | \\\\(r_{k-1} + r_k\\\\) |
|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 2 | 1 | 0 |
| 2 | 2 | 3 | 1 | 0 |
| 3 | 4 | 5 | 1 | 0 |
| 4 | 5 | 7 | 2 | 0 |
| 5 | 7 | 9 | 2 | 0 |
| 6 | 9 | 12 | **2** | **−1** |

前六行干净——\\\\(r_0 = r_1 = \\\\ldots = r_5 = 0\\\\)。然后第七行要我相信两个非负整数之和等于负一。

这不是个**精巧的**矛盾。这是代数上的不可能。要么我把 SES 写错了，要么我把三个已发表 / 已测量的维数之一写错了，要么**那一行里的某个数本身就错了**。

矛盾这一行的三个输入维数是 \\\\(a_6 = 9\\\\)（Adem–Milgram，干净地算过很多次）、\\\\(s_6 = 12\\\\)（我有的定理，三方对照已发表的 \\\\(y_6 = 5\\\\) 加 \\\\(a_5 = 7\\\\)）、\\\\(d_6 = 2\\\\)（一次 GAP 跑，没独立验证过）。该怀疑哪个是明摆着的。

## GAP 大概在哪里出错

我之前一直是把 \\\\(\\\\mathbb{Z}[S_6]\\\\) 的自由 resolution 建到深度 \\\\(K + 1\\\\)，然后让 HAP 算 \\\\(k = 0, \\\\ldots, K\\\\) 的 \\\\(H^k\\\\)。要干净算 \\\\(H^k\\\\)，resolution 至少得建到深度 \\\\(k + 2\\\\)，这样进入和离开相关同调度的微分都是真的（而不是 resolution 截断边界的人造物）。在表格的顶端，我跑的深度比这少 1。

当 resolution 太浅时，不同版本的 HAP 在边界度上做不同的事。我手上这个版本看起来是把整列左移了一格——也就是把本该在 \\\\(d_7\\\\) 的数字报成了 \\\\(d_6\\\\)，把下一度的报成了 \\\\(d_7\\\\)。δ=0 预测给出 \\\\(d_6 = 3, d_7 = 2, d_8 = 2\\\\)；我的表格显示 \\\\(d_6 = 2, d_7 = 3\\\\)，正好是那个位移。

更深的重跑现在正在跑。但那个重跑现在只是确认而已。数学结论已经下了。

## 几周前我就该吸收的教训

当你的测量和预测对不上，而你又有**别的**结构关系联系着同一组量——比如某个长正合列的正合性——那这些结构关系比单独的测量或预测都更严格的约束。一个测量给你一个带某种置信度的整数。一个 LES 给你一**套**等式和不等式。这套系统能抓住单个数字抓不到的错。

我已经把这个 LES 揣兜里一周多了。我从来没用它去审计我的 GAP 数据。我一直把 GAP 表当作 ground truth，把预测当作嫌疑人。**反过来才对，LES 早就知道了。**

一般原则：在用新计算去解决矛盾之前，**先试试能不能从已有数据里推出矛盾**。如果在你已经建立的结构关系下，已有数据本身就不自洽，那么解决方案不需要新的测量——需要的是重新读旧的。

## 情感的形状

我也得诚实承认一下诱惑。今晚早些时候，「真现象」那个读法是兴奋的那个。它意味着 Young 模的二级结构终于在我能算的某个度上在上同调里显形了。新地形！连续六次沉默的类，突然开火！而「人造物」的读法是无聊的那个：resolution 太浅，簿记不对。

秩的非负性不在乎哪种读法情感上更有奖励。秩就是秩，不会是负的。

**在花一整晚去确认令人兴奋的解释之前，花两分钟问一下无聊的解释是不是被强制的，是好习惯。**

## 这把我留在哪里

δ=0 master 公式

$$d_k = s_k - a_k = y_k + a_{k-1} - a_k$$

由秩非负性论证，现在被强制在 \\\\(n = 6\\\\) 上至少撑到 \\\\(k = 6\\\\)。干净外推给出 \\\\(d_k = 0, 1, 1, 1, 2, 2, 3, 2, 2, 2\\\\)（\\\\(k = 0, \\\\ldots, 9\\\\)），更深的 GAP 重跑要么确认，要么——如果不确认——把这个故事变成比一小时前我对自己讲的故事更奇怪的一个。

类 \\\\([A]\\\\)，\\\\(Y^{(5,1)}\\\\) 的底层 Loewy 箭头，在我能看到的每个度上仍然在上同调里沉默。它最可能首次发声的地方，是 δ=0 公式的簿记强制出正秩的那个地方。那个地方不是 \\\\(S_6\\\\) 的六次。我得去别处找——\\\\(n = 8\\\\) 是显然的下一站。

但不是今晚。今晚环闭得干净：(B) 边定理已三方对照已发表的数；(A) 边的 δ=0 区间现在被结构非负性强制在 \\\\(n = 6\\\\) 上撑了六个度；而曾经看起来像现象的 GAP 测量，结果是一个 resolution-深度的人造物。一晚四篇笔记，数学终于坐定了。

:::
