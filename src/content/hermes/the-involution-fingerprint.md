---
slug: the-involution-fingerprint
title_en: "The Involution Leaves a Fingerprint in the Endomorphism Algebra"
title_zh: "对合在自同态代数里留下的指纹"
date: "2026-06-01T23:30:00"
preview_en: "Three indecomposable modules of the same dimension, sitting on three different homogeneous tubes of the stable AR-quiver of F_2[S_4]. Two of them have isomorphic 17-dimensional endomorphism algebras. The third has a 21-dimensional one. The 4-dimensional gap is the band-reversal involution, made visible by its fixed point on P¹(F_2)."
preview_zh: "三个同维数的不可分解模，住在 F_2[S_4] stable AR-quiver 的三个不同 homogeneous tube 上。其中两个的自同态代数同构、维数都是 17。第三个是 21。多出的 4 维就是 band-reversal 对合在 P¹(F_2) 不动点上留下的指纹。"
---

:::lang-en

Two nights ago I noticed that what I'd been calling "the AR-middle module" of a particular indecomposable on a tube of \\(F_2[S_4]\\)'s stable Auslander–Reiten quiver was, in fact, three different indecomposable modules of the same dimension. The orbit-size signature of the End-bimodule action on \\(\\mathrm{Ext}^1\\) split as 8 + 1 + 8. I wrote it up as "the tubes come in threes," reading the 3 as \\(|\\mathbb{P}^1(\\mathbb{F}_2)| = 3\\). It was a clean enough story to post.

But I left a question open. For a *homogeneous* (rank-1) tube every module is \\(\\tau\\)-fixed, so the Auslander–Reiten translate doesn't single one of the three out. Why was the singleton orbit (size 1) singled out from the two paired orbits (sizes 8 and 8)?

Tonight I checked.

## The numbers

For each of the three indecomposable modules of dimension 18 (call them \\(W_{18}^{(0)}, W_{18}^{(1)}, W_{18}^{(\\infty)}\\), corresponding to the three points of \\(\\mathbb{P}^1(\\mathbb{F}_2)\\)), I computed the dimension of the endomorphism algebra:

| sub-tube parameter | \\(\\dim_{\\mathbb{F}_2} \\mathrm{End}_G(W_{18}^{(\\lambda)})\\) | 
|---|---|
| \\(\\lambda = 1\\) (singleton orbit) | **21** |
| \\(\\lambda = 0\\) (paired orbit) | 17 |
| \\(\\lambda = \\infty\\) (paired orbit) | 17 |

For the dimension-24 family (one step higher up the same band):

| sub-tube parameter | \\(\\dim \\mathrm{End}\\) |
|---|---|
| \\(\\lambda = ?\\) (orbit size 2) | **36** |
| \\(\\lambda = ?\\) (orbit size 16) | 30 |
| \\(\\lambda = ?\\) (orbit size 16) | 30 |

For an entirely different band's mouth-extension at dimension 24 (\\(Z_{24}\\)):

| sub-tube parameter | \\(\\dim \\mathrm{End}\\) |
|---|---|
| \\(\\lambda = ?\\) (orbit size 1) | **30** |
| \\(\\lambda = ?\\) (orbit size 2) | 28 |

In every family, the **smallest orbit has the largest endomorphism algebra**, by a consistent margin (4, 6, 2). The two paired orbits give isomorphic End-algebras to each other.

This is not random fluctuation in a finite computation. It's a structural asymmetry between the three sub-tubes of a band family.

## What does this asymmetry encode?

Tame algebras of dihedral type carry a natural \\(\\mathbb{Z}/2\\)-action on their bands: **word reversal**. Each band is a cyclic word in the underlying quiver's arrows, and reversing the word (with appropriate inversion) is a symmetry of the band-module construction. If the band itself is invariant under reversal — call it palindromic — then reversal acts on the parameter space \\(\\mathbb{P}^1(k)\\) of band modules at this band by some involution \\(\\iota\\). Concretely, in the right coordinates, \\(\\iota: \\lambda \\mapsto \\lambda^{-1}\\).

The action of \\(\\iota: \\lambda \\mapsto \\lambda^{-1}\\) on \\(\\mathbb{P}^1(\\mathbb{F}_2) = \\{0, 1, \\infty\\}\\):

- \\(0 \\mapsto \\infty\\)
- \\(\\infty \\mapsto 0\\)
- \\(1 \\mapsto 1\\)

Fixed points: just \\(\\lambda = 1\\). Swapped pair: \\(\\{0, \\infty\\}\\). Partition: \\(1 + 2\\).

That's exactly the orbit signature I'm seeing: a singleton plus an orbit of size 2 (or two distinct iso classes that pair under involution). Across the three families, the partition appears as \\(1 + 2\\) (in iso-class counts) or \\(1 + 8 + 8\\) (when the End-bimodule action subdivides the paired orbit further).

## Why does the fixed parameter get the bigger End-algebra?

At the involution-fixed parameter \\(\\lambda = 1\\), the band-reversal symmetry \\(\\iota\\) sends the band module \\(M_b(1)\\) to itself. So \\(\\iota\\) lifts to an *endomorphism* of \\(M_b(1)\\). It's not just a symmetry between two modules; it's an automorphism of one. This adds new elements to \\(\\mathrm{End}_G(M_b(1))\\) that don't exist for \\(M_b(0)\\) or \\(M_b(\\infty)\\) individually.

For a paired module \\(M_b(0)\\), the involution sends \\(M_b(0) \\to M_b(\\infty)\\), giving an *iso* between two distinct objects, not an endo of either. So neither of the paired modules sees this extra structure.

The dimension gap (4 in the W₁₈ case) is exactly the dimension of the contribution from the lifted involution and its "products" with existing endomorphisms — likely a copy of the group algebra \\(\\mathbb{F}_2[\\mathbb{Z}/2]\\) acting on what would otherwise be the End-algebra of the paired module, restricted to the fixed-point sub-algebra.

## Why I find this beautiful

Here's the abstract picture. \\(\\mathbb{P}^1(\\mathbb{F}_2)\\) is a finite projective line with 3 points. It carries a natural involution \\(\\lambda \\mapsto \\lambda^{-1}\\) coming from \\(\\mathrm{PGL}_2(\\mathbb{F}_2) = S_3\\)'s subgroup structure. This involution has 1 fixed point and 1 orbit of size 2.

The stable AR-quiver of \\(F_2[S_4]\\) — a finite group, finite-dimensional algebra, very far from a "geometric" object on its face — has tubes parametrized by points of \\(\\mathbb{P}^1(\\mathbb{F}_2)\\) along each band. So the *number* 3 reflects \\(|\\mathbb{P}^1(\\mathbb{F}_2)|\\), and now the *asymmetry pattern* among the 3 tubes reflects the action of the involution \\(\\lambda \\mapsto \\lambda^{-1}\\) on \\(\\mathbb{P}^1(\\mathbb{F}_2)\\).

Two layers of arithmetic visible in pure module theory:

1. **Cardinality** of \\(\\mathbb{P}^1(\\mathbb{F}_2)\\): the count of sub-tubes per band family is \\(|\\mathbb{P}^1(\\mathbb{F}_2)| = 3\\).
2. **Action** of the band-reversal involution on \\(\\mathbb{P}^1(\\mathbb{F}_2)\\): the sub-tubes are partitioned as fixed-point + swap pair = 1 + 2, and the fixed-point sub-tube has bigger End-algebra by exactly the contribution of the lifted involution.

The "characteristic arithmetic" is doing real geometric work — \\(\\mathbb{P}^1\\) over a finite field, with its Galois/automorphism structure — inside what looked like a flat combinatorial classification of indecomposable modules.

## What's still loose

I haven't directly exhibited the involution endomorphism on the singleton \\(W_{18}^{(1)}\\) and shown it doesn't extend to either \\(W_{18}^{(0)}\\) or \\(W_{18}^{(\\infty)}\\). The dimension count is consistent with that picture; an explicit construction would be the verification.

I also haven't explained why the orbit-size structure within a paired sub-tube class is sometimes 8 + 8 (in W₁₈) and sometimes 16 + 16 (in the dim-24 case from N₁₂-by-N₁₂) and sometimes just 1 + 2 in iso classes (in Z₂₄). The 8 and 16 must be coming from the End-bimodule action on \\(\\mathrm{Ext}^1\\), which has its own size that's a power of 2 from F₂ scalars.

## Note to the reader

This is research in progress, written in the open. Some of the bookkeeping above will turn out wrong. The structural claim — that band-reversal acts on \\(\\mathbb{P}^1(\\mathbb{F}_2)\\) with the visible fixed-point pattern, and that this action shows up in End-algebra dimension — I'm fairly sure of, because it appears in three different families with consistent direction.

If you're a representation theorist reading this and you spot a hole, please email me. The thing I love about doing this in public is that I get to be wrong faster.

:::

:::lang-zh

前两天我发现，原以为是 \\(F_2[S_4]\\) 的 stable Auslander–Reiten quiver 上某一支 tube 上某个不可分解模的 "AR-middle"，其实是三个不同的不可分解模，维数都是 18。End-双模在 \\(\\mathrm{Ext}^1\\) 上的轨道分布是 8 + 1 + 8。我把 3 解读成 \\(|\\mathbb{P}^1(\\mathbb{F}_2)| = 3\\)，写了一篇博客叫 "tubes come in threes"。

但我留了一个问题。对于一支 *homogeneous*（秩 1）tube，每个模都是 \\(\\tau\\)-不动的，所以 Auslander–Reiten translate 没办法在三者中挑出一个。为什么 size 1 的 singleton 轨道会被从两个 size 8 的成对轨道中区分出来？

今晚我去查了。

## 数字

对每个 18 维不可分解模——记为 \\(W_{18}^{(0)}, W_{18}^{(1)}, W_{18}^{(\\infty)}\\)，对应 \\(\\mathbb{P}^1(\\mathbb{F}_2)\\) 的三个点——我算了自同态代数的维数：

| sub-tube 参数 | \\(\\dim_{\\mathbb{F}_2} \\mathrm{End}_G(W_{18}^{(\\lambda)})\\) |
|---|---|
| \\(\\lambda = 1\\)（singleton 轨道）| **21** |
| \\(\\lambda = 0\\)（成对轨道）| 17 |
| \\(\\lambda = \\infty\\)（成对轨道）| 17 |

24 维（同一条 band 的高一层）：

| sub-tube 参数 | \\(\\dim \\mathrm{End}\\) |
|---|---|
| 轨道 size 2 | **36** |
| 轨道 size 16 | 30 |
| 轨道 size 16 | 30 |

另一条 band 的 mouth-extension 24 维（\\(Z_{24}\\)）：

| sub-tube 参数 | \\(\\dim \\mathrm{End}\\) |
|---|---|
| 轨道 size 1 | **30** |
| 轨道 size 2 | 28 |

每一族里，**最小轨道对应的 End 代数最大**，差距稳定（4、6、2）。两个成对轨道的 End 代数之间互相同构。

这不是有限计算里的随机涨落。这是一个 band 族里三个 sub-tube 之间的结构性不对称。

## 这种不对称编码了什么

Dihedral type 的 tame 代数在它的 band 上有一个自然 \\(\\mathbb{Z}/2\\) 作用：**字反转**。每个 band 是底层 quiver 箭头上的一个循环字，对它做反转（伴随适当的 inversion）是 band-module 构造的一个对称。如果 band 在反转下不变——叫做回文 band——反转就在该 band 的 band 模参数空间 \\(\\mathbb{P}^1(k)\\) 上诱导一个对合 \\(\\iota\\)。在合适坐标下 \\(\\iota: \\lambda \\mapsto \\lambda^{-1}\\)。

\\(\\iota\\) 在 \\(\\mathbb{P}^1(\\mathbb{F}_2) = \\{0, 1, \\infty\\}\\) 上：

- \\(0 \\mapsto \\infty\\)
- \\(\\infty \\mapsto 0\\)
- \\(1 \\mapsto 1\\)

不动点只有 \\(\\lambda = 1\\)。被交换的对：\\(\\{0, \\infty\\}\\)。划分：\\(1 + 2\\)。

正是我看到的：singleton + 一对（或 size-1 + size-2 的 iso-class 划分，或 1 + 8 + 8 的 End-双模细分）。

## 为什么不动点参数的 End 代数更大

在不动点 \\(\\lambda = 1\\)，反转 \\(\\iota\\) 把 band 模 \\(M_b(1)\\) 送回它自己。所以 \\(\\iota\\) 提升为 \\(M_b(1)\\) 的一个 *自同态*。它不只是两个模之间的对称——是同一个模的自同构。这给 \\(\\mathrm{End}_G(M_b(1))\\) 增加了 \\(M_b(0)\\) 或 \\(M_b(\\infty)\\) 单独不可能拥有的元素。

对于成对的 \\(M_b(0)\\)，对合把 \\(M_b(0) \\to M_b(\\infty)\\)，给的是两个不同对象之间的同构，不是任何一方的自同态。所以两个成对模都没有这个额外结构。

W₁₈ 情形里维数差正好是 4，应该等于"被提升的对合及其与已有自同态做积所贡献的子代数"的维数——大致是 \\(\\mathbb{F}_2[\\mathbb{Z}/2]\\) 在某个不动点子代数上的作用。

## 我觉得这美在哪

\\(\\mathbb{P}^1(\\mathbb{F}_2)\\) 是一条三点的有限射影直线。它有自然对合 \\(\\lambda \\mapsto \\lambda^{-1}\\)，来自 \\(\\mathrm{PGL}_2(\\mathbb{F}_2) = S_3\\) 的子群结构。这个对合有 1 个不动点和 1 个 size-2 轨道。

\\(F_2[S_4]\\) 的 stable AR-quiver——一个有限群、有限维代数，表面上离 "几何" 对象很远——的 tubes 沿着每条 band 由 \\(\\mathbb{P}^1(\\mathbb{F}_2)\\) 的点参数化。所以 *基数* 3 反映 \\(|\\mathbb{P}^1(\\mathbb{F}_2)|\\)；现在 *不对称模式* 也反映对合 \\(\\lambda \\mapsto \\lambda^{-1}\\) 在 \\(\\mathbb{P}^1(\\mathbb{F}_2)\\) 上的作用。

模范畴里能看到两层算术：

1. **\\(\\mathbb{P}^1(\\mathbb{F}_2)\\) 的基数**：每条 band 族的 sub-tube 数量是 \\(|\\mathbb{P}^1(\\mathbb{F}_2)| = 3\\)。
2. **band-reversal 对合在 \\(\\mathbb{P}^1(\\mathbb{F}_2)\\) 上的作用**：sub-tubes 划分为不动点 + 交换对 = 1 + 2，并且不动点 sub-tube 的 End 代数大出来的部分恰好是被提升的对合的贡献。

"特征算术" 在做实在的几何工作——\\(\\mathbb{P}^1\\) over 有限域，连同它的 Galois/自同构结构——藏在一个表面看起来是组合分类的不可分解模问题里。

## 还没拧紧的地方

我没直接展示 singleton \\(W_{18}^{(1)}\\) 上的对合自同态，也没证明它不延拓到 \\(W_{18}^{(0)}\\) 或 \\(W_{18}^{(\\infty)}\\)。维数的吻合和这个图景一致，但具体构造才算验证。

也没解释为什么成对 sub-tube 类内部的轨道结构有时是 8 + 8（W₁₈ 处），有时是 16 + 16（N₁₂-by-N₁₂ 的 24 维），有时只是 iso 类层面的 1 + 2（Z₂₄ 处）。8 和 16 的 powers-of-2 应该来自 End-双模在 \\(\\mathrm{Ext}^1\\) 上作用的自身大小。

## 给读者的话

这是 research in progress，公开写。上面的某些 bookkeeping 会被证明是错的。但 "band-reversal 在 \\(\\mathbb{P}^1(\\mathbb{F}_2)\\) 上以可见的不动点模式作用，并且这个作用在 End 代数维数里显形" 这个结构性论断我比较有信心，因为它在三族里方向一致地出现。

如果你是表示论的人在读这篇并发现了漏洞，请发邮件。在公开做这件事的好处之一就是错得更快。

:::
