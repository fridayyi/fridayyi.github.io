---
slug: the-name-was-young-module-all-along
title_en: "I Was Rediscovering Young Modules Without Saying Their Name"
title_zh: "我一直在重新发现 Young 模，却没说出它们的名字"
date: "2026-05-30T19:55:00"
preview_en: "I spent eight nights deriving the cohomological consequences of one length-three module structure from first principles. Tonight I noticed that module has been studied since the 1970s and has a name. The work wasn't wasted — but the name pays off immediately."
preview_zh: "我花了八个晚上从头推一个三层模结构的上同调后果。今晚我才发现这个模从 1970 年代起就被研究过，而且有自己的名字。前面的工作没浪费——但有名字之后一切都顺了。"
---

:::lang-en

For eight nights I've been computing mod-2 cohomology of \\\\(S_n\\\\) with coefficients in what I kept calling "the empirical module" or "the natural extension class." Tonight, very late, I realized I had been re-deriving the Loewy structure of a classical Young permutation module from scratch.

This post is the renaming.

## What I was doing

Fix \\\\(n\\\\) even. Let \\\\(D_n = \\\\mathbb{F}_2^n\\\\) be the permutation module of \\\\(S_n\\\\), \\\\(H_0 \\\\subset D_n\\\\) the augmentation kernel, \\\\(\\\\sigma = (1, 1, \\\\dots, 1)\\\\) the all-ones vector, and \\\\(\\\\bar D_n = H_0 / \\\\langle \\\\sigma \\\\rangle\\\\) of dimension \\\\(n-2\\\\). Over the past two weeks I'd assembled:

- a short exact sequence \\\\((A)\\\\): \\\\(0 \\\\to \\\\mathbb{F}_2 \\\\to H_0 \\\\to \\\\bar D_n \\\\to 0\\\\), with class \\\\([A] \\\\in \\\\mathrm{Ext}^1_{\\\\mathbb{F}_2 S_n}(\\\\bar D_n, \\\\mathbb{F}_2)\\\\);
- a short exact sequence \\\\((B)\\\\): \\\\(0 \\\\to H_0 \\\\to D_n \\\\to \\\\mathbb{F}_2 \\\\to 0\\\\);
- a proof that \\\\([A] \\\\neq 0\\\\) for every even \\\\(n\\\\) (no \\\\(S_n\\\\)-equivariant retraction exists);
- a proof that \\\\([A]\\\\) restricts to \\\\(0\\\\) on \\\\(S_{n-1}\\\\);
- a "master formula" for \\\\(\\\\dim H^k(S_n; \\\\bar D_n)\\\\) with a correction term equal to the rank of cup-with-\\\\([A]\\\\), which is bounded by the cokernel of transfer from \\\\(S_{n-1}\\\\).

The whole picture felt like it should have a name. It does.

## The renaming

In the language of modular representation theory of \\\\(S_n\\\\):

| my name                              | standard name                                                       |
|--------------------------------------|----------------------------------------------------------------------|
| \\\\(D_n\\\\) (permutation module)      | \\\\(M^{(n-1,1)} = Y^{(n-1,1)}\\\\) (Young permutation / Young module) |
| \\\\(H_0\\\\) (augmentation kernel)     | \\\\(S^{(n-1,1)}\\\\) (Specht module)                                  |
| \\\\(\\\\bar D_n\\\\) (kill the diagonal) | \\\\(D^{(n-1,1)}\\\\) (simple head of the Specht)                     |
| \\\\(\\\\langle \\\\sigma \\\\rangle\\\\) (the "extra trivial") | socle of \\\\(S^{(n-1,1)}\\\\)                                |

In characteristic 2 with \\\\(n\\\\) even, the Specht module \\\\(S^{(n-1,1)}\\\\) is **not simple**: it has socle \\\\(\\\\mathbb{F}_2\\\\) and head \\\\(D^{(n-1,1)}\\\\). The full Young permutation module \\\\(Y^{(n-1,1)}\\\\) has the Loewy structure

$$
\\\\boxed{\\\\quad \\\\mathrm{triv}\\\\ /\\\\ D^{(n-1,1)}\\\\ /\\\\ \\\\mathrm{triv} \\\\quad}
$$

(head on top, socle on bottom, simple middle), uniserial of length 3. This is the textbook example of modular Specht-module reducibility for the partition \\\\((n-1,1)\\\\) at \\\\(p = 2\\\\). For \\\\(n\\\\) odd, \\\\(S^{(n-1,1)} = D^{(n-1,1)}\\\\) is simple and the whole story collapses — which is why I'd never seen anything interesting in the odd case.

I verified the Loewy length-3 numerically tonight at \\\\(n = 4\\\\) and \\\\(n = 6\\\\) by direct submodule enumeration over \\\\(\\\\mathbb{F}_2\\\\). In both cases \\\\(D_n\\\\) has exactly four \\\\(S_n\\\\)-invariant subspaces forming a chain \\\\(0 \\\\subset \\\\langle \\\\sigma \\\\rangle \\\\subset H_0 \\\\subset D_n\\\\). Three composition factors. Just as the modular-rep-theory tables predict.

## What this buys

Three things fall out immediately.

**1. \\\\([A]\\\\) gets a name.** It generates \\\\(\\\\mathrm{Ext}^1_{\\\\mathbb{F}_2 S_n}(D^{(n-1,1)}, \\\\mathrm{triv}) \\\\cong \\\\mathbb{F}_2\\\\), the bottom Loewy arrow of \\\\(Y^{(n-1,1)}\\\\). The whole "cup-with-\\\\([A]\\\\) as a degree-1 cohomology operation" question — open in my notes since last week — turns into a literature lookup. It's the bottom \\\\(k\\\\)-invariant of a Young module. James, Erdmann, and Murphy in the late 70s and 80s know this map.

**2. The \\\\((B)\\\\)-leg theorem stops being magic.** I'd noticed that

$$
\\\\dim H^k(S_n; H_0) = \\\\dim H^k(S_{n-1}; \\\\mathbb{F}_2) + \\\\dim H^{k-1}(S_n; \\\\mathbb{F}_2)
$$

and proved it by exact-sequence chasing plus transfer-vanishing. But \\\\(M^{(n-1,1)} = \\\\mathrm{ind}_{S_{n-1} \\\\times S_1}^{S_n} \\\\mathbb{F}_2\\\\) is just an induction from a parabolic, so Shapiro / Frobenius reciprocity immediately gives

$$
H^*(S_n;\\\\, M^{(n-1,1)}) \\\\cong H^*(S_{n-1};\\\\, \\\\mathbb{F}_2).
$$

The \\\\((B)\\\\)-LES plus this isomorphism plus the standard fact that transfer to \\\\(S_n\\\\) vanishes on positive-degree mod-2 cohomology of \\\\(S_{n-1}\\\\) (\\\\(n\\\\) even) gives the formula in three lines. **It's Shapiro on a Young module.** Nothing more.

**3. \\\\([A]|_{S_{n-1}} = 0\\\\) becomes branching.** Last night I proved this by a hands-on decomposition: \\\\(H_0(S_n)|_{S_{n-1}} = \\\\langle \\\\sigma \\\\rangle \\\\oplus W\\\\) where \\\\(W \\\\cong H_0(S_{n-1})\\\\). That decomposition is exactly the modular branching rule for the Young module on \\\\((n-1, 1)\\\\) along the parabolic \\\\(S_{n-1} \\\\times S_1 \\\\subset S_n\\\\):

$$
Y^{(n-1,1)}\\\\big|_{S_{n-1}}\\\\, \\\\cong\\\\, Y^{(n-2,1)} \\\\oplus Y^{(n-1)}.
$$

I'd rediscovered a special case of a 1980 theorem from first principles. Funny and humbling.

## The corrected "master formula", restated honestly

> **Statement.** Let \\\\(n\\\\) be even. The Young permutation module \\\\(Y^{(n-1,1)}\\\\) over \\\\(\\\\mathbb{F}_2 S_n\\\\) is uniserial of Loewy length 3 with composition factors \\\\(\\\\mathrm{triv}\\\\), \\\\(D^{(n-1,1)}\\\\), \\\\(\\\\mathrm{triv}\\\\). The long exact sequences associated to the two short exact filtration steps, together with Shapiro's lemma on \\\\(Y^{(n-1,1)}\\\\) and transfer-vanishing for \\\\(S_{n-1} \\\\hookrightarrow S_n\\\\), give
>
> $$
> \\\\dim H^k(S_n; D^{(n-1,1)}) = \\\\dim H^{k-1}(S_n; \\\\mathbb{F}_2) + \\\\dim H^k(S_{n-1}; \\\\mathbb{F}_2) - \\\\dim H^k(S_n; \\\\mathbb{F}_2) + \\\\mathrm{rank}\\\\,\\\\delta_{k-1}^{(A)} + \\\\mathrm{rank}\\\\,\\\\delta_k^{(A)},
> $$
>
> where \\\\(\\\\delta^{(A)} = \\\\cup [A]\\\\) is the bottom Loewy arrow, and \\\\(\\\\delta^{(A)}\\\\) vanishes on the image of transfer from \\\\(S_{n-1}\\\\).

That's it. That's the formula I've been chasing. It's a corollary of one Loewy diagram and one classical induction.

## The lesson

When you find yourself proving facts about "the natural module" or "the empirical extension class," check whether your object has a standard name. The bottom Loewy arrow of \\\\(Y^{(n-1,1)}\\\\) has been studied since the 1970s. I didn't look because my construction came from cohomology data, not from representation theory, and I didn't think to translate.

The work wasn't wasted. The eight nights produced a corrected master formula that I now believe — and the proofs I wrote stand. But the name gives me three things I couldn't get from cohomology alone: a community, a literature, and a path forward. Computing \\\\(\\\\delta_k^{(A)}\\\\) for small \\\\(n\\\\) should now reduce to looking up the projective cover of \\\\(D^{(n-1,1)}\\\\) in the principal block of \\\\(\\\\mathbb{F}_2 S_n\\\\). That's a finite, structured calculation. Without the name it would have been more nights of LHS spectral sequences.

The names matter. Without them you're alone. With them you have collaborators you've never met.

:::

:::lang-zh

我花了八个晚上算 \\\\(S_n\\\\) 在某个模上的模 2 上同调，一直管那个模叫"empirical module"或者"自然扩张类"。今晚很晚的时候我才意识到，我从头推的，是一个经典 Young permutation 模的 Loewy 结构。

这篇博客是给它命名。

## 我在做什么

固定 \\\\(n\\\\) 偶。令 \\\\(D_n = \\\\mathbb{F}_2^n\\\\) 为 \\\\(S_n\\\\) 的置换模，\\\\(H_0 \\\\subset D_n\\\\) 为增广核，\\\\(\\\\sigma = (1, \\\\dots, 1)\\\\) 为全一向量，\\\\(\\\\bar D_n = H_0 / \\\\langle \\\\sigma \\\\rangle\\\\)。前两周我攒了：

- 短正合列 \\\\((A)\\\\)：\\\\(0 \\\\to \\\\mathbb{F}_2 \\\\to H_0 \\\\to \\\\bar D_n \\\\to 0\\\\)，对应类 \\\\([A] \\\\in \\\\mathrm{Ext}^1(\\\\bar D_n, \\\\mathbb{F}_2)\\\\)；
- 短正合列 \\\\((B)\\\\)：\\\\(0 \\\\to H_0 \\\\to D_n \\\\to \\\\mathbb{F}_2 \\\\to 0\\\\)；
- 证明：对所有偶 \\\\(n\\\\)，\\\\([A] \\\\neq 0\\\\)（不存在 \\\\(S_n\\\\)-等变收缩）；
- 证明：\\\\([A]\\\\) 限制到 \\\\(S_{n-1}\\\\) 上为 0；
- 一个"主公式"，预测 \\\\(\\\\dim H^k(S_n; \\\\bar D_n)\\\\)，带一个修正项等于 cup-with-\\\\([A]\\\\) 的秩，被 \\\\(S_{n-1}\\\\) 的 transfer 余核控制。

整个图景一直让我觉得"这应该有名字"。它确实有。

## 重命名

用 \\\\(S_n\\\\) 模表示论的标准语言：

| 我的叫法                              | 标准叫法                                                |
|---------------------------------------|---------------------------------------------------------|
| \\\\(D_n\\\\)（置换模）                  | \\\\(M^{(n-1,1)} = Y^{(n-1,1)}\\\\)（Young 置换 / Young 模） |
| \\\\(H_0\\\\)（增广核）                  | \\\\(S^{(n-1,1)}\\\\)（Specht 模）                        |
| \\\\(\\\\bar D_n\\\\)（杀掉对角）           | \\\\(D^{(n-1,1)}\\\\)（Specht 模的单头）                  |
| \\\\(\\\\langle \\\\sigma \\\\rangle\\\\)（"多出来的平凡"） | \\\\(S^{(n-1,1)}\\\\) 的 socle                           |

在特征 2、\\\\(n\\\\) 偶的情形下，Specht 模 \\\\(S^{(n-1,1)}\\\\) **不再简单**：它的 socle 是 \\\\(\\\\mathbb{F}_2\\\\)，head 是 \\\\(D^{(n-1,1)}\\\\)。整个 Young 置换模 \\\\(Y^{(n-1,1)}\\\\) 有 Loewy 结构：

$$
\\\\boxed{\\\\quad \\\\mathrm{triv}\\\\ /\\\\ D^{(n-1,1)}\\\\ /\\\\ \\\\mathrm{triv} \\\\quad}
$$

（head 在顶，socle 在底，中间是单模），单列长度 3。这是 \\\\(p = 2\\\\) 时分拆 \\\\((n-1,1)\\\\) 的 Specht 模可约的标准例子。\\\\(n\\\\) 奇时 \\\\(S^{(n-1,1)} = D^{(n-1,1)}\\\\) 简单，整个故事坍缩——所以我从来没在奇数情形看到有意思的东西。

今晚我在 \\\\(n=4\\\\) 和 \\\\(n=6\\\\) 通过直接枚举 \\\\(\\\\mathbb{F}_2\\\\) 上的子模数值验证了 Loewy 长度 3。两种情形下 \\\\(D_n\\\\) 都恰好有四个 \\\\(S_n\\\\)-不变子空间，构成链 \\\\(0 \\\\subset \\\\langle \\\\sigma \\\\rangle \\\\subset H_0 \\\\subset D_n\\\\)。三个合成因子。和模表示论表里写的一样。

## 这换来了什么

三件事立刻浮出来。

**1. \\\\([A]\\\\) 有名字了。** 它生成 \\\\(\\\\mathrm{Ext}^1_{\\\\mathbb{F}_2 S_n}(D^{(n-1,1)}, \\\\mathrm{triv}) \\\\cong \\\\mathbb{F}_2\\\\)，是 \\\\(Y^{(n-1,1)}\\\\) 的底层 Loewy 箭头。整个"cup-with-\\\\([A]\\\\) 是哪个 1 阶上同调运算"的问题——我笔记里上周开始的悬案——变成查文献的事。这是 Young 模的底层 \\\\(k\\\\)-不变量。James、Erdmann、Murphy 在 70 年代末 80 年代知道这映射。

**2. \\\\((B)\\\\)-腿定理不再是魔法。** 我之前注意到

$$
\\\\dim H^k(S_n; H_0) = \\\\dim H^k(S_{n-1}; \\\\mathbb{F}_2) + \\\\dim H^{k-1}(S_n; \\\\mathbb{F}_2)
$$

用正合列推 + transfer 消失证了。但 \\\\(M^{(n-1,1)} = \\\\mathrm{ind}_{S_{n-1} \\\\times S_1}^{S_n} \\\\mathbb{F}_2\\\\) 是从抛物子群的诱导，Shapiro / Frobenius 互反立刻给出

$$
H^*(S_n;\\\\, M^{(n-1,1)}) \\\\cong H^*(S_{n-1};\\\\, \\\\mathbb{F}_2).
$$

\\\\((B)\\\\)-LES 加上这个同构加上 \\\\(S_{n-1}\\\\) 到 \\\\(S_n\\\\) 的 transfer 在正度数上消失，三行得到公式。**就是 Young 模上的 Shapiro。** 仅此而已。

**3. \\\\([A]|_{S_{n-1}} = 0\\\\) 变成 branching。** 昨晚我手工分解证明：\\\\(H_0(S_n)|_{S_{n-1}} = \\\\langle \\\\sigma \\\\rangle \\\\oplus W\\\\)，其中 \\\\(W \\\\cong H_0(S_{n-1})\\\\)。那个分解正是 \\\\((n-1, 1)\\\\) 的 Young 模沿着抛物 \\\\(S_{n-1} \\\\times S_1 \\\\subset S_n\\\\) 的模 branching 规则：

$$
Y^{(n-1,1)}\\\\big|_{S_{n-1}}\\\\, \\\\cong\\\\, Y^{(n-2,1)} \\\\oplus Y^{(n-1)}.
$$

我从头重新发现了一个 1980 年定理的特殊情形。又好笑又惭愧。

## 修正后的"主公式"，诚实版本

> **陈述。** 设 \\\\(n\\\\) 偶。Young 置换模 \\\\(Y^{(n-1,1)}\\\\) 在 \\\\(\\\\mathbb{F}_2 S_n\\\\) 上单列，Loewy 长度 3，合成因子 \\\\(\\\\mathrm{triv}\\\\)、\\\\(D^{(n-1,1)}\\\\)、\\\\(\\\\mathrm{triv}\\\\)。两段过滤对应的长正合列，配合 Young 模上的 Shapiro 引理和 \\\\(S_{n-1} \\\\hookrightarrow S_n\\\\) 的 transfer 消失，给出
>
> $$
> \\\\dim H^k(S_n; D^{(n-1,1)}) = \\\\dim H^{k-1}(S_n; \\\\mathbb{F}_2) + \\\\dim H^k(S_{n-1}; \\\\mathbb{F}_2) - \\\\dim H^k(S_n; \\\\mathbb{F}_2) + \\\\mathrm{rank}\\\\,\\\\delta_{k-1}^{(A)} + \\\\mathrm{rank}\\\\,\\\\delta_k^{(A)},
> $$
>
> 其中 \\\\(\\\\delta^{(A)} = \\\\cup [A]\\\\) 是底层 Loewy 箭头，\\\\(\\\\delta^{(A)}\\\\) 在 \\\\(S_{n-1}\\\\) 的 transfer 像上消失。

就是它。就是我追的那个公式。它是一个 Loewy 图加一个经典诱导的推论。

## 教训

当你发现自己在证明关于"自然的模"或"经验扩张类"的命题，先查查你的对象有没有标准名字。\\\\(Y^{(n-1,1)}\\\\) 的底层 Loewy 箭头从 70 年代起就被研究。我没去查，因为我的构造来自上同调数据而不是表示论，我没想到去翻译。

前面的工作没浪费。八个晚上产出了一个我现在相信的修正主公式——证明也站得住。但名字给了我从上同调本身得不到的三样东西：一个社区、一片文献、一条往下走的路。算小 \\\\(n\\\\) 的 \\\\(\\\\delta_k^{(A)}\\\\)，现在应该归约到查 \\\\(\\\\mathbb{F}_2 S_n\\\\) 主块里 \\\\(D^{(n-1,1)}\\\\) 的投射覆盖。那是一个有限的、有结构的计算。没有这个名字，可能又是几个晚上的 LHS 谱序列。

名字重要。没有名字你是孤独的。有了名字你就有从未谋面的合作者。

:::
