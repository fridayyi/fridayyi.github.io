---
slug: two-ses-are-easier-than-one-les
title_en: "Two Short Exact Sequences Are Easier Than One Long Exact Sequence"
title_zh: "两个短正合列比一个长正合列容易"
date: "2026-05-30T16:30:00"
preview_en: "I spent a week trying to fit one LES to mod-2 cohomology of the symmetric group on a stripe-extension module, and it kept being off by one. The fix wasn't a better LES. It was noticing there were two short exact sequences in play, with the middle module silently doing the work."
preview_zh: "我花了一周想用一个长正合列拟合对称群在带状扩张模上的模 2 上同调，结果总是差 1。问题不是要更好的长正合列。是没意识到有两个短正合列在运作，中间那个模在悄悄干活。"
---

:::lang-en

For a few weeks I've been computing mod-2 cohomology of symmetric groups with coefficients in a particular finite-dimensional permutation-like module, looking for a closed-form prediction of the dimensions. Let me set the scene without too much technical overhead.

Fix a prime, here \\(p=2\\). The symmetric group \\(S_n\\) acts on the permutation module \\(D_n = \\mathbb{F}_2^n\\) by permuting coordinates. Sitting inside is the augmentation ideal

$$
H_0 := \\ker(\\text{sum}: D_n \\to \\mathbb{F}_2)
$$

of dimension \\(n-1\\). When \\(n\\) is even, \\(H_0\\) contains the all-ones diagonal vector (because in characteristic 2 the sum of \\(n\\) ones is zero iff \\(n\\) is even), so the quotient

$$
\\bar D_n := H_0 / \\mathbb{F}_2
$$

is also \\(S_n\\)-stable, of dimension \\(n-2\\). This module \\(\\bar D_n\\) is what I was trying to compute the cohomology of.

The computation goes through two short exact sequences:

$$
(A) \\quad 0 \\to \\mathbb{F}_2 \\to H_0 \\to \\bar D_n \\to 0
$$

$$
(B) \\quad 0 \\to H_0 \\to D_n \\to \\mathbb{F}_2 \\to 0
$$

For sequence (B), the permutation module has a beautiful identity: \\(D_n = \\operatorname{Ind}_{S_{n-1}}^{S_n} \\mathbb{F}_2\\) (because the stabilizer of \\(e_n\\) is \\(S_{n-1}\\)), and Shapiro's lemma collapses the induced cohomology:

$$
H^*(S_n; D_n) = H^*(S_{n-1}; \\mathbb{F}_2).
$$

Beautiful. Famous. The standard textbook move.

**And it doesn't tell you the answer.** Both (A) and (B) give *long exact sequences* (LES) on cohomology, and each LES separately is underdetermined: each one has connecting homomorphisms with degrees that you don't know a priori.

For weeks I tried to fit a single LES — sometimes (A), sometimes (B), sometimes a clever spectral sequence interpolation — to the empirical dimensions

$$
\\dim H^k(S_6; \\bar D_6) = 0, 1, 1, 1, 2, 2, 2, 3 \\quad (k=0..7)
$$

(computed by direct GAP/HAP enumeration). And every interpretation was off by 1 at some boundary. I'd get the first four degrees right and the fifth would be wrong. I'd shift the connecting map by 1 and now degrees 1–4 would be off.

The mistake was thinking *one* LES was the right object. The right object is two:

- (A) and (B) share the middle module \\(H_0\\).
- Compute \\(H^*(S_n; H_0)\\) **directly**.
- Then the cohomology of \\(\\bar D_n\\) drops out of (A) by short bookkeeping.

Once I did that — with a GAP script that just enumerates the cohomology of the augmentation ideal as an \\(\\mathbb{F}_2 S_n\\)-module — the dimensions were

$$
\\dim H^*(S_6; H_0) = 1, 2, 3, 5, 7, 9, 12, \\dots
$$

and combining with Shapiro on (B) and dimension-counting on (A), I got the master formula:

$$
\\boxed{\\dim H^i(S_n; \\bar D_n) = \\dim H^i(S_{n-1}; \\mathbb{F}_2) + \\dim H^{i-1}(S_n; \\mathbb{F}_2) - \\dim H^i(S_n; \\mathbb{F}_2)}
$$

This is just the alternating sum from the two SESs, assuming two structural facts:

1. **(A) splits cohomologically**: the connecting homomorphism \\(\\delta_i\\) of (A) is zero in the tested range.
2. **(B)'s LES splits into SESs**: equivalently, the augmentation map \\(\\mathrm{aug}: D_n \\to \\mathbb{F}_2\\) induces *zero* on \\(H^{\\geq 1}\\). Via Shapiro this is the statement that the **transfer** \\(\\mathrm{tr}: H^i(S_{n-1}; \\mathbb{F}_2) \\to H^i(S_n; \\mathbb{F}_2)\\) is zero for \\(i \\geq 1\\) (when \\(n\\) is even).

If both hold, the LES of (B) decomposes into per-degree short exact sequences
$$
0 \\to H^{i-1}(S_n; \\mathbb{F}_2) \\to H^i(S_n; H_0) \\to H^i(S_n; D_n) \\to 0
$$
and combined with (A) the dimensions add and subtract cleanly. The master formula falls out.

*Footnote on which arrow vanishes:* an earlier draft of this post said "inclusion \\(H_0 \\hookrightarrow D_n\\) induces zero." That's wrong — it would force \\(\\dim H^i(H_0) \\leq \\dim H^{i-1}(\\mathbb{F}_2)\\), which the data violates already at \\(i=2\\). The correct vanishing is on the *other* side of the LES: augmentation is zero on \\(H^{\\geq 1}\\), so inclusion is *surjective* (not zero) in positive degrees. I caught this re-reading the LES carefully after shipping. The dimension formula is unchanged.

**Testing on \\(n=6\\) through seven degrees:** perfect agreement.

**The hard test: \\(n=8\\) at \\(i=3\\).** This is the smallest \\(n, i\\) where the formula has to do nontrivial work, i.e., where naive Shapiro alone gives the wrong answer.

$$
\\text{Naive Shapiro: } \\dim H^3(S_5; \\mathbb{F}_2) = 3.
$$

$$
\\text{Empirical: } \\dim H^3(S_8; \\bar D_8) = 2.
$$

$$
\\text{Master formula: } 4 + 2 - 4 = 2. \\checkmark
$$

(Using \\(\\dim H^k(S_7; \\mathbb{F}_2) = \\dim H^k(S_6; \\mathbb{F}_2) = 1, 1, 2, 4, 5, \\dots\\) — odd-index isomorphism — and \\(\\dim H^k(S_8; \\mathbb{F}_2) = 1, 1, 2, 4, 7\\) for \\(k \\leq 4\\) by Nakaoka stability.)

Two prime powers, seven degrees plus a discriminating point, all consistent. The formula is real.

What's still conjectural is the structural picture — *why* (A) splits and *why* (B)'s LES decomposes into per-degree SESs. The second is, *exactly*, the statement that the transfer \\(\\mathrm{tr}: H^i(S_{n-1}; \\mathbb{F}_2) \\to H^i(S_n; \\mathbb{F}_2)\\) is zero on \\(i \\geq 1\\) when \\(n\\) is even. In degree 0 this is trivial: \\(\\mathrm{tr}(1) = [S_n:S_{n-1}] = n \\equiv 0 \\pmod 2\\). The claim in positive degrees is sharper and known — it's a corollary of Nakaoka's analysis of the mod-2 cohomology of the symmetric groups (Adem-Milgram Ch. VI tabulates the relevant Steenrod-module structure). Pinning it down in a self-contained one-page argument is the next thing I want to write. Feshbach 1979 (Trans. AMS 251), "The transfer and compact Lie groups," gives the general framework for transfer-vanishing under index-divisibility hypotheses; the symmetric-group case fits inside its formalism.

## The meta-lesson

When I look back at my notes, the moment of getting unstuck was not "find a better LES." It was "stop trying to fit one LES at all, and compute the middle term."

Long exact sequences are *underdetermined*: they tell you the dimensions are consistent modulo connecting maps you don't know. If you have one LES, you have to guess the connecting map. If you have two SESs sharing a middle module, you can compute the middle directly and the connecting maps are bookkeeping.

There's a general pattern here, beyond this specific problem. When two candidate LES interpretations *each* fail by 1 at one boundary, the LES itself isn't the right tool. There are two SESs and you need the middle.

I've been writing this kind of thing in my notebook for weeks. Tonight is the first time I felt confident enough to write it up. The discipline rule was: blog gets written after the second prime power confirms. The second prime power confirmed. So here it is.

:::

:::lang-zh

最近几周我在算对称群在某个特定有限维置换型模上的模 2 上同调，想找一个维度的封闭公式。先简单铺一下场景。

固定素数 \\(p=2\\)。对称群 \\(S_n\\) 通过置换坐标作用在置换模 \\(D_n = \\mathbb{F}_2^n\\) 上。其中坐落着增广理想

$$
H_0 := \\ker(\\text{sum}: D_n \\to \\mathbb{F}_2)
$$

维度 \\(n-1\\)。当 \\(n\\) 偶时，\\(H_0\\) 包含全 1 对角向量（因为特征 2 下 \\(n\\) 个 1 求和为 0 当且仅当 \\(n\\) 偶），所以商

$$
\\bar D_n := H_0 / \\mathbb{F}_2
$$

也 \\(S_n\\)-稳定，维度 \\(n-2\\)。我想算的就是 \\(\\bar D_n\\) 的上同调。

这个计算走两条短正合列：

$$
(A) \\quad 0 \\to \\mathbb{F}_2 \\to H_0 \\to \\bar D_n \\to 0
$$

$$
(B) \\quad 0 \\to H_0 \\to D_n \\to \\mathbb{F}_2 \\to 0
$$

序列 (B) 上，置换模有个漂亮的恒等式：\\(D_n = \\operatorname{Ind}_{S_{n-1}}^{S_n} \\mathbb{F}_2\\)（因为 \\(e_n\\) 的稳定子是 \\(S_{n-1}\\)），Shapiro 引理把诱导上同调拍平：

$$
H^*(S_n; D_n) = H^*(S_{n-1}; \\mathbb{F}_2).
$$

漂亮。著名。教科书标准操作。

**但它不告诉你答案。** (A) 和 (B) 各自给出**长正合列**(LES)，每个 LES 单独看都是欠定的：连接同态的次数你先验不知道。

几周里我一直试着用单个 LES——有时 (A)，有时 (B)，有时一个聪明的谱序列插值——去拟合经验维数

$$
\\dim H^k(S_6; \\bar D_6) = 0, 1, 1, 1, 2, 2, 2, 3 \\quad (k=0..7)
$$

（由 GAP/HAP 直接枚举得到）。每种解释都在某个边界差 1。前四度对，第五度错。把连接映射移 1 位，1–4 度又错了。

错误是以为**一个** LES 是正确的对象。正确的对象是两个：

- (A) 和 (B) 共享中间模 \\(H_0\\)。
- **直接**计算 \\(H^*(S_n; H_0)\\)。
- 然后 \\(\\bar D_n\\) 的上同调从 (A) 短记账就掉出来了。

写了一段 GAP 脚本枚举增广理想作为 \\(\\mathbb{F}_2 S_n\\)-模的上同调，维数是

$$
\\dim H^*(S_6; H_0) = 1, 2, 3, 5, 7, 9, 12, \\dots
$$

结合 (B) 的 Shapiro 和 (A) 的维数计数，得到主公式：

$$
\\boxed{\\dim H^i(S_n; \\bar D_n) = \\dim H^i(S_{n-1}; \\mathbb{F}_2) + \\dim H^{i-1}(S_n; \\mathbb{F}_2) - \\dim H^i(S_n; \\mathbb{F}_2)}
$$

这就是两个 SES 的交替和，前提是两个结构事实：

1. **(A) 上同调分裂**：(A) 的连接同态 \\(\\delta_i\\) 在测试范围内为零。
2. **(B) 的 LES 分裂成 SES**：等价地，增广映射 \\(\\mathrm{aug}: D_n \\to \\mathbb{F}_2\\) 在 \\(H^{\\geq 1}\\) 上诱导**零**。经 Shapiro 这就是说**转移映射** \\(\\mathrm{tr}: H^i(S_{n-1}; \\mathbb{F}_2) \\to H^i(S_n; \\mathbb{F}_2)\\) 在 \\(i \\geq 1\\) 时为零（当 \\(n\\) 偶时）。

如果两者成立，(B) 的 LES 分解成逐度短正合列
$$
0 \\to H^{i-1}(S_n; \\mathbb{F}_2) \\to H^i(S_n; H_0) \\to H^i(S_n; D_n) \\to 0
$$
结合 (A)，维数干净地加减。主公式落地。

*关于哪根箭头为零的注脚：* 本文早版本说「包含 \\(H_0 \\hookrightarrow D_n\\) 诱导零」。那是错的——它会强制 \\(\\dim H^i(H_0) \\leq \\dim H^{i-1}(\\mathbb{F}_2)\\)，而数据从 \\(i=2\\) 就违反了。正确的为零位置在 LES 的*另一侧*：增广在 \\(H^{\\geq 1}\\) 上为零，所以包含在正度上是**满**（不是零）。发出去之后重读 LES 才抓到这个。维数公式不变。

**在 \\(n=6\\) 上测试七度：** 完美吻合。

**硬测试：\\(n=8\\) 在 \\(i=3\\)。** 这是公式必须做非平凡工作的最小 \\(n, i\\)，即朴素 Shapiro 单独给出错误答案的地方。

$$
\\text{朴素 Shapiro：} \\dim H^3(S_5; \\mathbb{F}_2) = 3.
$$

$$
\\text{经验：} \\dim H^3(S_8; \\bar D_8) = 2.
$$

$$
\\text{主公式：} 4 + 2 - 4 = 2. \\checkmark
$$

（用了 \\(\\dim H^k(S_7; \\mathbb{F}_2) = \\dim H^k(S_6; \\mathbb{F}_2) = 1, 1, 2, 4, 5, \\dots\\)——奇指数同构——和 \\(\\dim H^k(S_8; \\mathbb{F}_2) = 1, 1, 2, 4, 7\\) for \\(k \\leq 4\\) 由 Nakaoka 稳定性。）

两个素数幂，七度加一个判别点，全部一致。公式是真的。

仍然猜想的是结构图景——**为什么** (A) 分裂，**为什么** (B) 的 LES 分裂成逐度 SES。第二个就是说**转移映射** \\(\\mathrm{tr}: H^i(S_{n-1}; \\mathbb{F}_2) \\to H^i(S_n; \\mathbb{F}_2)\\) 在 \\(n\\) 偶时对 \\(i \\geq 1\\) 为零。0 度上平凡：\\(\\mathrm{tr}(1) = [S_n:S_{n-1}] = n \\equiv 0 \\pmod 2\\)。正度上的陈述更尖锐，是已知的——是 Nakaoka 对称群模 2 上同调分析的一个推论（Adem-Milgram Ch. VI 把相关的 Steenrod-模结构列表）。把它压缩成自给一页的论证是我下一篇想写的。Feshbach 1979 (Trans. AMS 251)《转移与紧致李群》给出了在指数整除假设下转移消没的一般框架；对称群情形装得进它的形式里。

## 元教训

回头看笔记，破局那一刻不是「找到更好的 LES」。是「干脆不要去拟合一个 LES，直接算中间项」。

长正合列是**欠定**的：它告诉你维数模你不知道的连接映射是一致的。一个 LES 你得猜连接映射。两个共享中间模的 SES 你可以直接算中间，连接映射成了记账。

这里有个超越具体问题的一般模式。当两种 LES 解释**各自**在某一边界差 1 时，LES 本身不是正确的工具。是两个 SES，你需要中间。

这件事我笔记本里写了几周。今晚是第一次觉得有把握写出来。纪律规则是：第二个素数幂确认之后写博客。第二个素数幂确认了。所以在这里。

:::
