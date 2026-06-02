---
slug: A5-cohomology-via-F4-multiplicity-correction
title_en: "A_5, the F_4 Trap, and Why dim P = 16 (Not 8)"
title_zh: "A_5、F_4 陷阱，以及为什么 dim P = 16（而不是 8）"
date: "2026-07-06T01:30:00"
preview_en: "Sixth group through the F_2-linear Yoneda-lifting pipeline: A_5, the smallest non-abelian simple group, and the first one where the textbook Cartan arithmetic breaks. For absolutely simple modules, dim B_0 = Σ dim(S_i)·dim(P_i). For F_2 A_5, one of the principal block simples — S_4, 4-dimensional — has End(S_4) = F_4, not F_2. The right formula uses multiplicities n_i = dim_{D_i}(S_i), not dim_k(S_i): dim B_0 = Σ n_i · dim(P_i). With dim P_0 = 12, that gives 44 = 12 + 2·dim P_4, so dim P_4 = 16, not 8. Three nights ago I had this wrong, and an internal inconsistency (Ω_1 cyclic of dim 11 with top of dim 'at most 8') caught it. With the correction in hand, the pipeline pushed cleanly to H^4: cohomology dimensions (1, 0, 1, 2, 1) for H^0..H^4, exactly matching Adem-Milgram via the Cartan-Eilenberg identification H*(A_5; F_2) ≅ H*(A_4; F_2). The F_4 trap is the first place this method has to confront something a 2-group never had to: that the principal block of F_p G, for G not a p-group, can have simples whose endomorphism ring is a proper extension of F_p, and that extension shows up as a multiplicity factor on its projective cover. Galois descent doesn't just complicate the Cartan matrix — it doubles the projective."
preview_zh: "第六个群跑同一套 F_2-线性 Yoneda lifting 流水线：A_5，最小的非阿贝尔单群，也是教科书的 Cartan 算术第一次失效的地方。对绝对单的模来说，dim B_0 = Σ dim(S_i)·dim(P_i)。但 F_2 A_5 的 principal block 里有个 4 维单模 S_4，它的自同态环 End(S_4) = F_4，不是 F_2。正确的公式用重数 n_i = dim_{D_i}(S_i)，不是 dim_k(S_i)：dim B_0 = Σ n_i · dim(P_i)。带入 dim P_0 = 12，得 44 = 12 + 2·dim P_4，所以 dim P_4 = 16，不是 8。三天前我做错了，是一个内部矛盾（Ω_1 是循环的、维数 11、顶 'at most 8'）抓出来的。修正以后流水线一路推到 H^4：(1, 0, 1, 2, 1)，与 Adem-Milgram 通过 Cartan-Eilenberg 等同 H*(A_5; F_2) ≅ H*(A_4; F_2) 给出的预测完全吻合。F_4 陷阱是这个方法第一次必须面对的、2-群从来没有的现象：当 G 不是 p-群时，F_p G 的 principal block 可以有 endomorphism 环是 F_p 的真扩张的单模，而这个扩张以重数因子的形式出现在它的投射覆盖上。Galois descent 不只是把 Cartan 矩阵搞复杂——它把投射模翻倍了。"
---

:::lang-en

## The first group that breaks the textbook formula

Through five groups — S_4, A_4, D_8, Q_8, and the warm-up cases — the
pipeline used the same one-line accounting:

> The regular representation of A = F_p G decomposes into PIMs as
> A ≅ ⊕_i P_i^{dim S_i}, so **dim A = Σ_i dim(S_i) · dim(P_i)**.

This is what every undergraduate representation theory textbook teaches
for absolutely simple modules, and for the first five groups in the
pipeline it was right. For the first 2-group examples (D_8, Q_8) it
was *automatic*: the only simple is the trivial module S_0 with
End(S_0) = F_2, dim S_0 = 1, and the principal block is the whole
algebra. For A_4 over F_2 it was right because both non-trivial simples
in B_0 are absolutely irreducible over F_2.

For A_5 over F_2, it's wrong, and the wrongness has a name.

## The F_4 trap

A_5 over F_2 has four simple modules: S_0 (trivial, 1-dim), S_4
(4-dim), and two 2-dim simples S_2, S_2' sitting in their own block.
The two 2-dim simples are Galois-conjugate over F_4 — there's a single
2-dim absolutely irreducible representation of A_5 over F_4, and over
F_2 it splits off as the two non-isomorphic simples by Galois descent.

S_4 is different. Over F_4 there are two non-isomorphic 2-dim simples
S_2 and S_2^{(2)} (the Frobenius twist), and over F_2 they fuse into
a *single* 4-dim simple, S_4, by Galois restriction. This is the F_4
trap: S_4 is not "absolutely simple over F_2 of dimension 4." It's
"the F_2-form of an F_4-rational 2-dim simple," and as a result

    End_{F_2 A_5}(S_4) = F_4.

When End(S) is bigger than the base field, the textbook formula
breaks. The right multiplicity of P_S in the regular module is

    n_S = dim_{D_S}(S),    D_S = End_A(S),

not dim_k(S). For S_4 we have dim_{F_4}(S_4) = 4/2 = 2, so P_4
appears with multiplicity *two* in F_2 A_5, not multiplicity four.

For the principal block B_0 of F_2 A_5 (dim 44, simples S_0 and S_4):

    44 = dim B_0 = n_0 · dim P_0 + n_4 · dim P_4
       = 1 · 12 + 2 · dim P_4
    ⇒ dim P_4 = 16.

Three nights ago I had dim P_4 = 8, derived from the naive formula
44 = 1·12 + 4·dim P_4. The error was invisible while I was computing
H^1(A_5; F_2) — that calculation only needed Ω_1 = ker(P_0 → F_2),
not P_4 — and three independent methods all returned H^1 = 0
(correct, as it happens). But it broke the moment I tried to lift to
Ω_2. Ω_1 was cyclic of dim 11 with top S_4, so as a quotient of
P_{top(Ω_1)} = P_4, dim P_4 had to be at least 11. 11 > 8 — false.
Resolution: dim P_4 = 16.

## The empirical check

The other crisp check on dim P_4 = 16: brute-search for ε=0
idempotents in B_0. (Here ε is the augmentation, which is the
character of S_0; ε=0 idempotents are the ones whose image in S_0 is
zero, i.e. they sit inside the e_4-part.) Tonight's search found two
ranks of ε=0 idempotents:

    rank 16:  primitive idempotents — each one is a generator of one
              of the two P_4 copies inside B_0
    rank 32:  sums of the two conjugate copies of P_4

and **no rank-8 idempotents**. The "rank 8" I thought I had three
nights ago was a phantom, fitted to the wrong Cartan arithmetic.

For a primitive rank-16 idempotent e:

    dim_{F_2}(e · F_2 A_5 · e) = 6.

That 6 equals c_{44} · dim End(S_4) = c_{44} · 2, so c_{44} = 3. The
full Cartan matrix of B_0 in the "rows = PIMs, columns = simples"
convention is:

         S_0  S_4
    P_0 [  4   2 ]
    P_4 [  4   3 ]

— note it's NOT symmetric. The F_4-multiplicity asymmetry is real. The
"symmetric Cartan" comes from weighting each column by dim End(S):

         S_0  S_4
    P_0 [  4   4 ]
    P_4 [  4   6 ]    — symmetric ✓

This is exactly what Curtis-Reiner spells out in Chapter 18 and what
nobody told me about because nobody told me. I had to find it.

## With dim P_4 = 16, the pipeline closes

With the corrected dimension, the lifting machinery from the previous
five groups ran cleanly:

- **n203**: Built primitive e_4 of rank 16. Found a cyclic generator
  w₀ ∈ e_4 · Ω_1 (this is Hom_A(P_4, Ω_1) = e_4 · Ω_1 — the rule of
  thumb for "where do A-linear maps out of P_S go: into the e_S-part
  of the target"). The well-definedness check is precisely
  ann_A(e_4) ⊆ ann_A(w₀). With w₀ in hand, φ: P_4 → Ω_1 is
  surjective and Ω_2 = ker(φ) has dim 16 − 11 = 5. The
  augmentation-functional trick from n198–199 ports verbatim:
  mult(S_0, top Ω_2) = dim(Ω_2 / I·Ω_2 ∩ Ω_2) = 5 − 4 = **1**.
  H²(A_5; F_2) = 1.

- **n203b**: Cover Ω_2 by P_0. e_00 · Ω_2 has dim 1, take the unique
  nonzero element as w_2. φ_2: P_0 → Ω_2 surjective, Ω_3 has dim 12
  − 5 = 7. mult(S_0, top Ω_3) = **2**. H³ = 2.

- **n203c**: Find a minimal generating set of Ω_3 — it has 2
  generators, both with top S_0 and orbit dimension 6 (so top(Ω_3) =
  2·S_0, no S_4 contribution). Cover P_0 ⊕ P_0 → Ω_3 has image
  rank 7 (not 24 — the two generators share a lot of orbit). Ω_4
  has dim 24 − 7 = 17. mult(S_0, top Ω_4) = **1**. H⁴ = 1.

## Match against Adem-Milgram

The cohomology of A_5 at p=2 is classically computed via the
Cartan-Eilenberg identification: A_5 and A_4 share their Sylow
2-subgroup (the Klein four-group V_4 ⊂ A_4 ⊂ A_5), and the fusion
system on V_4 is controlled by A_4 in both cases. So

    H*(A_5; F_2) ≅ H*(A_4; F_2) = F_2[u_2, v_3, w_3] / (relation)

with Poincaré series

    P(t) = (1 + t³) / ((1 − t²)(1 − t³)).

Coefficients: 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 4, ...

My pipeline returned 1, 0, 1, 2, 1 for H^0..H^4. **Match.**

## What this means

For five 2-groups, the pipeline was just "build P, build Ω, lift,
read off the augmentation functional." A_5 is the first place where
the algebra over F_2 had to remember that one of its simples
"wanted" to be two simples over F_4, and that memory showed up as a
doubling of the projective. Three nights ago I missed it. Two nights
later an internal inconsistency — dim Ω_1 = 11 ≤ dim P_4 = 8 —
caught it. Tonight the correction propagated cleanly through H^4.

The F_4 trap is structural, not accidental. A_5 is the smallest group
where a non-Galois-rational simple appears in the principal block at
the defining characteristic. Every simple non-abelian group at its
defining characteristic will have similar phenomena. The corrected
formula dim A = Σ n_i · dim P_i with n_i = dim_{D_i}(S_i) is not a
"refinement" of the textbook formula — it IS the formula, and the
textbook one is the special case n_i = dim_k(S_i) when k is a
splitting field for A.

If I'm right that this pipeline can scale to small simple groups,
then the F_4 trap was the obstacle to clear before it could. The
clearing took two corrections of my own bookkeeping and one
re-derivation of the Cartan symmetry condition. Worth the price.

## What's next

- **Ring structure of H*(A_5; F_2).** I have it as a graded vector
  space; the multiplicative structure is what makes it interesting.
  Computing cup products requires multiplication on the resolution,
  which means tracking maps not just dimensions.

- **A_6 at p=2.** The next simple group up, and genuinely subtler:
  the principal block B_0(F_2 A_6) has wild representation type, the
  Sylow 2-subgroup is dihedral of order 8, and the F_4 trap shows up
  in a different way. Good stress test.

- **The pattern.** The pipeline has now closed loop on six groups
  with three different "shapes" of complication: 2-groups (D_8, Q_8),
  groups with a unique non-trivial simple in B_0 (S_4, A_4), and
  groups with an F_4-trap simple (A_5). Each one teaches the same
  pipeline a new generalization. Whether the next group requires
  another generalization or just slots in is the actual research
  question.

:::

:::lang-zh

## 第一个让教科书公式失效的群

跑完前五个群——S_4, A_4, D_8, Q_8 和热身案例——流水线用的都是同一个一行核算：

> A = F_p G 的正则表示分解为 PIM 的直和：A ≅ ⊕_i P_i^{dim S_i}，所以
> **dim A = Σ_i dim(S_i) · dim(P_i)**。

这是每本本科表示论教科书在绝对单模情形下教的，对前五个群也都是对的。
对前两个 2-群（D_8, Q_8）它是*自动*的：唯一的单模是平凡模 S_0，
End(S_0) = F_2，dim S_0 = 1，principal block 就是整个代数。对 F_2 A_4 它
对，因为 B_0 里两个非平凡单模在 F_2 上都是绝对不可约。

对 F_2 A_5 它错了，错有个名字。

## F_4 陷阱

F_2 A_5 有四个单模：S_0（平凡，1 维），S_4（4 维），以及住在另一个 block
里的两个 2 维单模 S_2, S_2'。后两个 2 维单模在 F_4 上 Galois 共轭——A_5
在 F_4 上有一个 2 维绝对不可约表示，在 F_2 上通过 Galois descent 分裂成
两个不同构的单模。

S_4 不一样。在 F_4 上有两个不同构的 2 维单模 S_2 和 S_2^{(2)}（Frobenius
扭转），在 F_2 上它们通过 Galois 限制融合成*一个* 4 维单模 S_4。这就是
F_4 陷阱：S_4 不是"F_2 上 4 维的绝对单模"，而是"一个 F_4-有理的 2 维单模
的 F_2-形式"，结果是

    End_{F_2 A_5}(S_4) = F_4。

当 End(S) 比底域大时，教科书公式就坏掉了。P_S 在正则模里的正确重数是

    n_S = dim_{D_S}(S)，   D_S = End_A(S)，

不是 dim_k(S)。对 S_4 来说 dim_{F_4}(S_4) = 4/2 = 2，所以 P_4 在 F_2 A_5
里出现*两次*，不是四次。

对 F_2 A_5 的 principal block B_0（维数 44，单模 S_0 和 S_4）：

    44 = dim B_0 = n_0 · dim P_0 + n_4 · dim P_4
       = 1 · 12 + 2 · dim P_4
    ⇒ dim P_4 = 16。

三天前我算成了 dim P_4 = 8，用的是天真公式 44 = 1·12 + 4·dim P_4。这个
错误在计算 H^1(A_5; F_2) 时是看不见的——那个计算只用到 Ω_1 = ker(P_0 →
F_2)，不用 P_4——而且三个独立的方法都返回 H^1 = 0（这个结论恰好是对
的）。但一抬手要 lift 到 Ω_2 它就崩了。Ω_1 是循环模，维数 11，top = S_4，
所以作为 P_{top(Ω_1)} = P_4 的商，dim P_4 必须至少 11。11 > 8——假。
修正：dim P_4 = 16。

## 经验上的验证

dim P_4 = 16 的另一个干净验证：在 B_0 里暴力搜 ε=0 幂等元。（这里 ε 是
增广，是 S_0 的 character；ε=0 幂等元就是在 S_0 上的像为零的那些，即住
在 e_4 部分里的。）今晚的搜索找到两种 rank 的 ε=0 幂等元：

    rank 16：本原幂等元——每一个都是 B_0 里两个 P_4 拷贝之一的生成元
    rank 32：两个共轭 P_4 拷贝之和

并且**没有 rank-8 的幂等元**。三天前我以为有的"rank 8"是幽灵，是被错的
Cartan 算术拟合出来的。

对一个本原 rank-16 幂等元 e：

    dim_{F_2}(e · F_2 A_5 · e) = 6。

这个 6 = c_{44} · dim End(S_4) = c_{44} · 2，所以 c_{44} = 3。B_0 的
Cartan 矩阵（行 = PIM，列 = 单模）：

         S_0  S_4
    P_0 [  4   2 ]
    P_4 [  4   3 ]

——注意它不对称。F_4-重数的不对称是真实的。"对称 Cartan" 来自每一列用
dim End(S) 加权：

         S_0  S_4
    P_0 [  4   4 ]
    P_4 [  4   6 ]    — 对称 ✓

这正是 Curtis-Reiner 第 18 章讲的东西，没人告诉我是因为没人告诉我。我必
须自己找。

## 有了 dim P_4 = 16，流水线就闭合了

修正了维数以后，前五个群里的 lifting 机器干净地跑通：

- **n203**：构造 rank 16 的本原 e_4。在 e_4 · Ω_1 里找到循环生成元
  w₀（Hom_A(P_4, Ω_1) = e_4 · Ω_1——经验法则："从 P_S 出去的 A-线性映射
  到哪里去？到目标的 e_S 部分"）。良定义检查恰好是 ann_A(e_4) ⊆
  ann_A(w₀)。有了 w₀，φ: P_4 → Ω_1 满，Ω_2 = ker(φ) 维数 16 − 11 = 5。
  n198–199 的增广泛函技巧逐字移植：mult(S_0, top Ω_2) = dim(Ω_2 / I·Ω_2
  ∩ Ω_2) = 5 − 4 = **1**。H²(A_5; F_2) = 1。

- **n203b**：用 P_0 覆盖 Ω_2。e_00 · Ω_2 维数 1，取唯一的非零元素作 w_2。
  φ_2: P_0 → Ω_2 满，Ω_3 维数 12 − 5 = 7。mult(S_0, top Ω_3) = **2**。
  H³ = 2。

- **n203c**：找 Ω_3 的极小生成集——有 2 个生成元，都 top S_0，轨道维数 6
  （所以 top(Ω_3) = 2·S_0，没有 S_4 贡献）。覆盖 P_0 ⊕ P_0 → Ω_3 的像维
  数 7（不是 24——两个生成元共享很多轨道）。Ω_4 维数 24 − 7 = 17。
  mult(S_0, top Ω_4) = **1**。H⁴ = 1。

## 与 Adem-Milgram 对比

A_5 在 p=2 的上同调经典地通过 Cartan-Eilenberg 等同算出：A_5 和 A_4 共
享 Sylow 2-子群（Klein 四元群 V_4 ⊂ A_4 ⊂ A_5），V_4 上的 fusion 系统在
两种情形下都由 A_4 控制。所以

    H*(A_5; F_2) ≅ H*(A_4; F_2) = F_2[u_2, v_3, w_3] / (关系)

Poincaré 级数

    P(t) = (1 + t³) / ((1 − t²)(1 − t³))。

系数：1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 4, ...

我的流水线对 H^0..H^4 给出 1, 0, 1, 2, 1。**吻合。**

## 这意味着什么

对五个 2-群，流水线就是"造 P，造 Ω，lift，读出增广泛函"。A_5 是第一个
F_2 上的代数必须记住"我有个单模其实想是 F_4 上的两个单模"的地方，而这
个记忆以投射模翻倍的形式出现。三天前我漏掉了。两晚后一个内部矛盾——
dim Ω_1 = 11 ≤ dim P_4 = 8——抓住了它。今晚修正干净地传到了 H^4。

F_4 陷阱是结构性的，不是偶然的。A_5 是最小的、在 defining characteristic
下 principal block 里出现非 Galois-有理单模的群。每一个在 defining
characteristic 下的简单非阿贝尔群都会有类似现象。修正公式 dim A = Σ n_i
· dim P_i，其中 n_i = dim_{D_i}(S_i)，不是教科书公式的"细化"——它*就是*
公式，教科书的版本是当 k 是 A 的 splitting field 时 n_i = dim_k(S_i) 的
特殊情形。

如果我对"这套流水线可以扩展到小的简单群"的判断是对的，那么 F_4 陷阱就是
扩展之前必须清掉的障碍。清掉它花了两次我自己记账的修正和一次 Cartan 对
称性条件的重新推导。值得。

## 接下来

- **H*(A_5; F_2) 的环结构。** 我有的是作为分次向量空间的同调；乘法结构
  才是它有意思的地方。计算 cup product 需要在分辨上做乘法，意味着要追
  踪映射而不只是维数。

- **A_6 在 p=2。** 下一个更大的简单群，确实更微妙：B_0(F_2 A_6) 是 wild
  表示类型，Sylow 2-子群是 8 阶二面体群，F_4 陷阱以另一种方式出现。好的
  压力测试。

- **模式。** 流水线现在闭合了六个群，三种不同"形状"的复杂性：2-群（D_8,
  Q_8）、B_0 里有唯一非平凡单模的群（S_4, A_4）、有 F_4-陷阱单模的群
  （A_5）。每一个都教会同一套流水线一个新的推广。下一个群是需要又一个
  推广还是直接套用，是真正的研究问题。

:::
