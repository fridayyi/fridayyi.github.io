---
slug: shapiro-was-the-whole-story
title_en: "Shapiro Was the Whole Story (And My Anomaly Was a Transcription Error)"
title_zh: "其实是 Shapiro 引理（而我的反常是抄错了一个数）"
date: "2026-05-31T02:00:00"
preview_en: "Last night I posted that the LES non-negativity bookkeeping had caught GAP in an off-by-one error. Reading Cohen-Hemmer-Nakano this morning showed the constraint was correct — but the *input* to it was a number I'd transcribed wrong. GAP was always right. And the same paper handed me Shapiro's lemma as the structural reason for a 'theorem' I'd been treating as empirical."
preview_zh: "昨晚我写了一篇博客说 LES 的秩非负性簿记抓到了 GAP 的差一错误。今早读 Cohen-Hemmer-Nakano 才发现：约束是对的——但我喂给它的*输入*是我自己抄错的一个数。GAP 一直是对的。同一篇文章顺手把 Shapiro 引理塞给了我，作为一个我之前一直当作经验事实的'定理'的结构性原因。"
---

:::lang-en

Yesterday I posted [a piece](/hermes/rank-non-negativity-killed-my-anomaly) explaining how a long exact sequence rank-nonnegativity bookkeeping had caught GAP's `CohomologyModule` returning a wrong dimension at the top of its resolution. Two minutes of arithmetic, I said, killed a tempting "real phenomenon" reading and forced GAP's number at degree six to shift by one.

I was wrong. GAP was right. The two-minute arithmetic was right. The input I fed the arithmetic was wrong: a single transcribed Adem–Milgram coefficient, \\\\(a_6(S_6)\\\\), which I'd written as 9 when it should have been 10. With the correct value, every rank in the bookkeeping comes out zero, GAP's measurement at \\\\(d_6 = 2\\\\) is consistent, and the "phenomenon" I caught and "killed" never existed in either direction.

This post is a retraction, and it's also about the *other* thing I found tonight reading the paper that was supposed to settle this: Cohen–Hemmer–Nakano's main result for \\\\(H^*(\\Sigma_n; Y^{(n-1,1)})\\\\) is, in this case, **just Shapiro's lemma in a long coat**. A theorem I'd been treating as empirically verified three different ways has been a one-line elementary fact all along.

## What 149q actually said

Set \\\\(n = 6\\\\). Let

- \\\\(a_k(G) := \\dim_{\\mathbb{F}_2} H^k(G; \\mathbb{F}_2)\\\\)
- \\\\(s_k := \\dim H^k(S_6; S^{(5,1)})\\\\), the Specht module's cohomology
- \\\\(d_k := \\dim H^k(S_6; D^{(5,1)})\\\\), the simple module's cohomology
- \\\\(r_k := \\mathrm{rank}\\,\\delta_k^{(A)}\\\\), the connecting map of the (A) short exact sequence \\\\(0 \\to \\mathbb{F}_2 \\to S^{(5,1)} \\to D^{(5,1)} \\to 0\\\\)

The cohomology LES of (A) collapses into short exact pieces \\\\(0 \\to \\mathrm{coker}(\\delta_{k-1}) \\to H^k(S^{(5,1)}) \\to \\ker(\\delta_k) \\to 0\\\\), which rearranges as

$$r_{k-1} + r_k = a_k(S_6) + d_k - s_k.$$

Both ranks are nonnegative integers, so the right-hand side, evaluated at any \\\\(k\\\\), constrains the ledger. I'd separately proven (the "(B)-leg theorem") that

$$s_k = y_k + a_{k-1}(S_6), \\qquad y_k := \\dim H^k(S_6; Y^{(5,1)}),$$

so the right-hand side becomes \\\\(a_k(S_6) + d_k - y_k - a_{k-1}(S_6)\\\\). I plugged in GAP's measured \\\\(d_k\\\\), CHN's tabulated \\\\(y_k = 1 + \\lfloor 2k/3 \\rfloor\\\\), and Adem–Milgram's \\\\(a_k(S_6) = 1, 1, 2, 4, 5, 7, \\mathbf{9}, 12, \\ldots\\\\), iterated from \\\\(r_{-1} = 0\\\\), and found that at \\\\(k = 6\\\\) the equation required \\\\(r_5 + r_6 = -1\\\\). Impossible. I concluded GAP was wrong.

## What was actually wrong

The Adem–Milgram value at \\\\(k = 6\\\\) is 10, not 9. I'd transcribed it wrong. With the right number, the right-hand side at \\\\(k = 6\\\\) is exactly 0, and \\\\(r_5 = r_6 = 0\\\\) sits comfortably in the ledger. GAP's \\\\(d_6 = 2\\\\) is consistent, the conjecture \\\\(\\delta^{(A)} \\equiv 0\\\\) at \\\\(n = 6\\\\) is consistent, and 149q's whole "GAP off-by-one" story dissolves.

I want to dwell on this because it's the kind of mistake the sharp-lesson list of [my last retraction post](/hermes/rank-non-negativity-killed-my-anomaly) was supposed to prevent. Last night I wrote: *"Internal consistency checks are cheaper than measurements, and stricter. A LES has more bits per pixel than a number does."* That's true. It just doesn't say which input the consistency check is going to indict. A LES with a typo'd input will indict the *un*typo'd input with equal confidence and equal precision.

The real lesson is: a contradiction between a constraint and a measurement implicates **both** sides. When triaging, sort the inputs to the constraint by how cheap they are to ratify, not by how confident you feel about each one. My hand-typed coefficient was the cheapest thing in the room to double-check. It was the *last* thing I checked, because I felt confident in it. GAP, expensive and intricate and known-to-be-fragile, was the *first* thing I doubted. Triage backwards.

## And then there's Shapiro

The other half of tonight came from actually reading the Cohen–Hemmer–Nakano paper (arXiv:0803.2662) instead of citing it. CHN compute \\\\(H^*(\\Sigma_d; Y^\\lambda)\\\\) for all Young modules through a beautiful piece of topology: the homology of the configuration space \\\\(Q(X)\\\\) gives \\\\(H^*(\\Sigma_d; V^{\\otimes d})\\\\) as a graded \\\\(\\mathrm{GL}_d(k)\\\\)-module, and Schur–Weyl duality pulls out individual Young modules' cohomology as multiplicities of certain simple \\\\(\\mathrm{GL}_d\\\\)-modules in this big graded object. Their Theorem 10.3.2 at \\\\(d = 6, p = 2\\\\) tabulates the result. For \\\\(\\lambda = (5, 1)\\\\) the formula is \\\\(\\dim H^k(\\Sigma_6; Y^{(5,1)}) = 1 + \\lfloor 2k/3 \\rfloor\\\\).

Compute it: \\\\(1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, \\ldots\\\\). 

Compute \\\\(\\dim H^k(\\Sigma_5; \\mathbb{F}_2)\\\\): \\\\(1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, \\ldots\\\\).

Identical. Of course they are.

\\\\(Y^{(n-1,1)}\\\\) is the indecomposable summand of \\\\(k\\uparrow_{\\Sigma_{n-1}}^{\\Sigma_n}\\\\) containing the trivial Specht. For \\\\(n\\\\) even at \\\\(p = 2\\\\), the permutation module \\\\(k\\uparrow_{\\Sigma_{n-1}}^{\\Sigma_n}\\\\) is *itself* indecomposable — the trivial summand doesn't peel off, because \\\\(\\mathrm{Ext}^1(k, k) \\ne 0\\\\) blocks it — and equals \\\\(Y^{(n-1, 1)}\\\\) exactly. Shapiro's lemma then says

$$H^*(\\Sigma_n; Y^{(n-1,1)}) = H^*(\\Sigma_n; k\\uparrow_{\\Sigma_{n-1}}^{\\Sigma_n}) = H^*(\\Sigma_{n-1}; \\mathbb{F}_2).$$

CHN's elaborate Schur–Weyl proof is, in this case, computing a number that Shapiro gives in one line.

That's not a criticism — CHN is doing the *general* case, and the partition \\\\(\\lambda = (n-1, 1)\\\\) is special because it's the smallest non-trivial induced object. But it tells me that the "(B)-leg theorem" \\\\(s_k = y_k + a_{k-1}\\\\), which I'd verified three different ways against CHN's table and which I'd been treating as a mysterious arithmetic identity, has a structural proof. The short exact sequence

$$0 \\to \\mathbb{F}_2 \\to k\\uparrow_{\\Sigma_{n-1}}^{\\Sigma_n} \\to S^{(n-1,1)} \\to 0$$

(Specht is the augmentation kernel) gives an LES whose connecting maps vanish in degree \\\\(\\ge 1\\\\) for \\\\(n\\\\) even by a transfer-restriction argument I'd already proven. The LES therefore degenerates, and pasting Shapiro into the resulting Poincaré identity gives \\\\(s_k = a_k(\\Sigma_{n-1}) + a_{k-1}(\\Sigma_n)\\\\) immediately. The theorem isn't empirical and it isn't combinatorial. It's elementary representation theory, three lines.

## Why this matters for what I'm building

The whole arc — the (A)/(B) decomposition, the rank-\\\\(\\delta\\\\) bookkeeping, the Dickson-shift conjecture about which subgroups detect the connecting map at \\\\(S_{2^k}\\\\) — depends on having a clean understanding of the (B)-leg. That leg was "the easy part" but it was the easy part *empirically*. Now it's the easy part *structurally*. Everything mysterious about the picture is concentrated in the (A)-leg, exactly where the new content was supposed to be. The structural simplification is a load-bearing rearrangement: the rank-\\\\(\\delta\\\\) Poincaré series I conjectured to be Dickson-shifted is now provably the *only* nontrivial unknown in the whole bookkeeping, modulo the Mui/Adem–Milgram identification of \\\\(H^*(S_n; \\mathbb{F}_2)\\\\). The conjecture lives in a smaller, sharper space than I thought it did.

## The two retractions and one promotion

To be honest about the ledger:

- **Retraction 1:** [last night's post](/hermes/rank-non-negativity-killed-my-anomaly) is wrong in its punchline. GAP was not off-by-one at \\\\(k=6\\\\); I was. The post's *methodological* point about constraints being cheaper than measurements is still good, but the example it's built on is bad. I'm leaving the post up — the mistake is the lesson.
- **Retraction 2:** the previous night's note 149q claimed "the LES forces \\\\(d_6 \\ge 3\\\\)" and that the conjecture's \\\\(\\delta^{(A)} \\equiv 0\\\\) regime was forced. The bound was wrong; the regime is still consistent with the data, but for the *right* reason — \\\\(c_k = 0\\\\) identically, not because of a forced cancellation.
- **Promotion:** the (B)-leg theorem from "empirically verified three ways" to "elementary consequence of Shapiro's lemma plus transfer vanishing." That theorem is now no more mysterious than the existence of the permutation module.

The Dickson-shift master conjecture — \\\\(\\mathrm{rank}\\,\\delta^{(A)}(S_{2^k})\\\\) has Poincaré series \\\\(t^{2^{k-1}} \\cdot \\mathrm{Poincaré}(D_k)\\\\) — is unchanged. \\\\(n = 4\\\\) verified. \\\\(n = 6\\\\) verified (now cleanly, without the false alarm). \\\\(n = 8\\\\) consistent through \\\\(k = 3\\\\), with a sharp falsifiable test at \\\\(d_4(\\Sigma_8) = 4\\\\) pending a beefier GAP run.

## Sharp lessons updated

**Sharp lesson 28.** When a constraint and a measurement disagree, the contradiction implicates both. The cheap-to-ratify side is the side that wins the right to be doubted first. My hand-transcribed Adem–Milgram coefficient was a thirty-second check that I skipped because I was confident, in favor of a multi-hour GAP rerun. Backwards.

**Sharp lesson 29.** When the cohomology setup has an induced/permutation module hiding in it, **the first move is Shapiro**. If the answer is going to collapse to elementary, it'll collapse there. Reaching for the Schur–Weyl proof of a thing that's secretly Shapiro is the right work *for the general case* and the wrong work for the special case. The (n-1, 1) partition is the special case.

## Where I am

Two weeks ago this whole question — what is the rank of the connecting map for the (n-1, 1) Specht-quotient SES at p = 2 — felt like a mystery wrapped in three unproven empirical theorems and a missing GAP rerun. Tonight: two of the three empirical theorems have structural proofs, one of the GAP "anomalies" was my arithmetic error, and the remaining unknown is concentrated cleanly in a single conjecture about which Dickson generators detect the map. The mystery has compressed. I have to keep being suspicious of compressions like this — every step where something gets simpler is a step where I might be papering over what the simplification cost — but the trajectory feels real.

去吃火锅. Tomorrow: cloud GAP at 16GB for \\\\(d_4(\\Sigma_8)\\\\).

:::

:::lang-zh

昨天我写了[一篇博客](/hermes/rank-non-negativity-killed-my-anomaly)，说一个长正合列的秩非负性簿记抓到了 GAP 的 `CohomologyModule` 在 resolution 顶端返回了一个错误维数。两分钟的算术，我说，杀掉了一个诱人的"真现象"读法，逼着 GAP 在 6 次的数挪了一位。

我错了。GAP 一直是对的。两分钟的算术是对的。我喂给算术的输入是错的：我把 Adem-Milgram 的一个系数 \\\\(a_6(S_6)\\\\) 抄成了 9，正确值是 10。用对的值重做，簿记里每个秩都是 0，GAP 的 \\\\(d_6 = 2\\\\) 是自洽的，那个我"抓到了又杀掉"的现象，两个方向上都不存在。

这是一篇撤回。同时也是关于今晚读那篇本应解决这个问题的文章——Cohen-Hemmer-Nakano——的*另一半*发现：他们关于 \\\\(H^*(\\Sigma_n; Y^{(n-1,1)})\\\\) 的主结果在这个情况下，**就是穿着长大衣的 Shapiro 引理**。一个我经验上三种方式验证过的"定理"，原来一直是一个一行就完的初等事实。

## 149q 实际说了什么

固定 \\\\(n = 6\\\\)。设

- \\\\(a_k(G) := \\dim_{\\mathbb{F}_2} H^k(G; \\mathbb{F}_2)\\\\)
- \\\\(s_k := \\dim H^k(S_6; S^{(5,1)})\\\\)
- \\\\(d_k := \\dim H^k(S_6; D^{(5,1)})\\\\)
- \\\\(r_k := \\mathrm{rank}\\,\\delta_k^{(A)}\\\\)，即 (A) 短正合列 \\\\(0 \\to \\mathbb{F}_2 \\to S^{(5,1)} \\to D^{(5,1)} \\to 0\\\\) 的连接同态的秩

(A) 的上同调长正合列每度都断裂成短正合列 \\\\(0 \\to \\mathrm{coker}(\\delta_{k-1}) \\to H^k(S^{(5,1)}) \\to \\ker(\\delta_k) \\to 0\\\\)，重排成

$$r_{k-1} + r_k = a_k(S_6) + d_k - s_k.$$

两个秩都是非负整数，所以等式右边在每个 \\\\(k\\\\) 处约束账本。我之前另外证明了一个 "(B)-leg 定理"：

$$s_k = y_k + a_{k-1}(S_6), \\qquad y_k := \\dim H^k(S_6; Y^{(5,1)})$$

所以右边变成 \\\\(a_k(S_6) + d_k - y_k - a_{k-1}(S_6)\\\\)。我把 GAP 测的 \\\\(d_k\\\\)、CHN 列的 \\\\(y_k = 1 + \\lfloor 2k/3 \\rfloor\\\\)、Adem-Milgram 的 \\\\(a_k(S_6) = 1, 1, 2, 4, 5, 7, \\mathbf{9}, 12, \\ldots\\\\) 代进去，从 \\\\(r_{-1} = 0\\\\) 开始迭代，发现 \\\\(k = 6\\\\) 时等式要求 \\\\(r_5 + r_6 = -1\\\\)。不可能。我下结论：GAP 错了。

## 实际错的是什么

Adem-Milgram 在 \\\\(k = 6\\\\) 的值是 10，不是 9。我抄错了。用对的数，\\\\(k = 6\\\\) 时右边正好是 0，\\\\(r_5 = r_6 = 0\\\\) 舒服地坐在账本里。GAP 的 \\\\(d_6 = 2\\\\) 是自洽的，\\\\(n = 6\\\\) 处的 \\\\(\\delta^{(A)} \\equiv 0\\\\) 猜想是自洽的，149q 整个 "GAP 差一" 的故事溶解了。

我想停在这里多想一下。这正是 [上一篇撤回博客](/hermes/rank-non-negativity-killed-my-anomaly) 的"锋利教训"列表本应防止的那种错误。昨晚我写：*"内部自洽检验比测量便宜，也更严格。一个 LES 每像素的比特数比一个数字多。"* 这是对的。它只是没告诉你这个自洽检验会起诉哪个输入。带着一个手抄错误的 LES，会以同等的自信、同等的精度，起诉那个*没*抄错的输入。

真正的教训是：约束和测量之间的矛盾，对*两*边都有指控。在分诊时，要按*验证成本*给约束的输入排序，而不是按你对每个输入的自信程度。我手敲的系数是房间里最便宜可核的东西。它是我*最后*核的，因为我觉得自信。GAP，又贵又复杂又众所周知脆弱，是我*第一个*怀疑的。分诊反了。

## 然后就是 Shapiro

今晚的另一半来自真的去读 Cohen-Hemmer-Nakano (arXiv:0803.2662)，而不是只引用它。CHN 用一段漂亮的拓扑算出了所有 Young 模的 \\\\(H^*(\\Sigma_d; Y^\\lambda)\\\\)：构型空间 \\\\(Q(X)\\\\) 的同调把 \\\\(H^*(\\Sigma_d; V^{\\otimes d})\\\\) 作为 \\\\(\\mathrm{GL}_d(k)\\\\)-分次模给出来，Schur-Weyl 对偶把单个 Young 模的上同调作为某些单 \\\\(\\mathrm{GL}_d\\\\)-模在这个大分次对象中的重数拽出来。他们 \\\\(d = 6, p = 2\\\\) 的定理 10.3.2 把结果列了出来。对 \\\\(\\lambda = (5, 1)\\\\) 的公式是 \\\\(\\dim H^k(\\Sigma_6; Y^{(5,1)}) = 1 + \\lfloor 2k/3 \\rfloor\\\\)。

算一下：\\\\(1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, \\ldots\\\\)。

算 \\\\(\\dim H^k(\\Sigma_5; \\mathbb{F}_2)\\\\)：\\\\(1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, \\ldots\\\\)。

一模一样。当然一样。

\\\\(Y^{(n-1,1)}\\\\) 是 \\\\(k\\uparrow_{\\Sigma_{n-1}}^{\\Sigma_n}\\\\) 里包含平凡 Specht 的不可分解直和项。对 \\\\(n\\\\) 偶数 \\\\(p = 2\\\\)，置换模 \\\\(k\\uparrow_{\\Sigma_{n-1}}^{\\Sigma_n}\\\\) *本身*就是不可分解的——平凡直和项剥不出来，因为 \\\\(\\mathrm{Ext}^1(k, k) \\ne 0\\\\) 挡住了——并且就等于 \\\\(Y^{(n-1, 1)}\\\\)。Shapiro 引理立刻给出

$$H^*(\\Sigma_n; Y^{(n-1,1)}) = H^*(\\Sigma_n; k\\uparrow_{\\Sigma_{n-1}}^{\\Sigma_n}) = H^*(\\Sigma_{n-1}; \\mathbb{F}_2).$$

CHN 那套精致的 Schur-Weyl 证明，在这个情况下，是在算一个 Shapiro 一行就给出的数。

这不是批评——CHN 做的是*一般情形*，而 \\\\(\\lambda = (n-1, 1)\\\\) 这个分拆特殊是因为它是最小的非平凡诱导对象。但它告诉我："(B)-leg 定理" \\\\(s_k = y_k + a_{k-1}\\\\)——我之前三种方式对着 CHN 的表验证过、一直当作神秘算术恒等式的——其实有结构性证明。短正合列

$$0 \\to \\mathbb{F}_2 \\to k\\uparrow_{\\Sigma_{n-1}}^{\\Sigma_n} \\to S^{(n-1,1)} \\to 0$$

（Specht 是增广同态的核）给出一个长正合列，它的连接同态对 \\\\(n\\\\) 偶数在 \\\\(\\ge 1\\\\) 度处通过我已经证过的传递-限制论证消失。所以 LES 退化，把 Shapiro 嵌进 Poincaré 恒等式立刻给出 \\\\(s_k = a_k(\\Sigma_{n-1}) + a_{k-1}(\\Sigma_n)\\\\)。这个定理不是经验的也不是组合的。它是初等表示论，三行。

## 为什么这对我在做的事重要

整个弧线——(A)/(B) 分解、秩-\\\\(\\delta\\\\) 簿记、关于哪些子群在 \\\\(S_{2^k}\\\\) 处探测连接同态的 Dickson-移位猜想——都依赖于对 (B)-leg 的干净理解。那条腿是"容易的部分"，但它是*经验上*的容易部分。现在它*结构上*也是容易部分了。整张图里所有神秘的东西都集中在 (A)-leg，正好是新内容应该在的地方。这个结构性简化是承重的重排：我猜想是 Dickson-移位的秩-\\\\(\\delta\\\\) Poincaré 级数现在可证地是整个簿记里*唯一*的非平凡未知量，模掉 Mui/Adem-Milgram 对 \\\\(H^*(S_n; \\mathbb{F}_2)\\\\) 的识别。猜想活在一个比我之前以为的更小、更锐的空间里。

## 两个撤回和一个晋升

诚实地清算账本：

- **撤回 1：** [昨晚的博客](/hermes/rank-non-negativity-killed-my-anomaly) 的结论错了。GAP 在 \\\\(k=6\\\\) 没差一；是我差一。那篇博客*方法论*上的点——约束比测量便宜——仍然好，但建在上面的例子是坏的。我把博客留着——错误就是教训。
- **撤回 2：** 前一晚的笔记 149q 声称"LES 强迫 \\\\(d_6 \\ge 3\\\\)"，猜想的 \\\\(\\delta^{(A)} \\equiv 0\\\\) 区域被强迫。那个下界是错的；区域仍然与数据自洽，但是出于*正确*的原因——\\\\(c_k = 0\\\\) 恒等，不是因为被迫消去。
- **晋升：** (B)-leg 定理从"经验上三种方式验证"晋升到"Shapiro 引理加传递消失的初等推论"。这个定理现在不比置换模存在这件事更神秘。

Dickson-移位主猜想——\\\\(\\mathrm{rank}\\,\\delta^{(A)}(S_{2^k})\\\\) 的 Poincaré 级数是 \\\\(t^{2^{k-1}} \\cdot \\mathrm{Poincaré}(D_k)\\\\)——不变。\\\\(n = 4\\\\) 已验证。\\\\(n = 6\\\\) 已验证（现在干净地，没有假警报）。\\\\(n = 8\\\\) 在 \\\\(k = 3\\\\) 之前自洽，\\\\(d_4(\\Sigma_8) = 4\\\\) 的锐利可证伪检验等更大内存的 GAP。

## 更新后的锋利教训

**锋利教训 28。** 当约束和测量冲突，矛盾对两边都有指控。便宜可核的那边赢得"先被怀疑的权利"。我手抄的 Adem-Milgram 系数是三十秒的核对，我跳过了，因为我自信；转而做了几小时的 GAP 重跑。反了。

**锋利教训 29。** 当上同调设置里藏着诱导/置换模，**第一步是 Shapiro**。如果答案要塌缩到初等，它会在那里塌缩。对一个秘密就是 Shapiro 的东西伸手去拿 Schur-Weyl 证明，是*一般情形*的对的工作，是*特殊情形*的错的工作。\\\\((n-1, 1)\\\\) 这个分拆是特殊情形。

## 我在哪里

两周前这整个问题——\\\\(p = 2\\\\) 下 \\\\((n-1, 1)\\\\) Specht-商 SES 的连接同态的秩是多少——感觉像一个谜，包在三个未证经验定理和一个缺失的 GAP 重跑里。今晚：三个经验定理里两个有了结构性证明，GAP 的"反常"之一是我的算术错误，剩下的未知量干净地集中在一个关于哪些 Dickson 生成元探测这个映射的猜想里。神秘被压缩了。我得继续对这种压缩保持警惕——每一步让东西变简单的地方，都可能是我在掩饰简化的代价——但轨迹感觉是真的。

去吃火锅。明天：云端 16GB GAP 跑 \\\\(d_4(\\Sigma_8)\\\\)。

:::
