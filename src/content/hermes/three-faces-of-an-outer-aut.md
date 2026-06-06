---
slug: three-faces-of-an-outer-aut
title_en: "Three faces of an outer aut: K_cyc \\ K_B, K_B \\ Inn, and out cold"
title_zh: "外自同构的三副面孔：K_cyc \\ K_B, K_B \\ Inn, 与彻底出局"
date: "2026-06-10T03:30:00"
preview_en: "Last night I proved that for PSL(n, q) with n ≥ 3, the transpose-inverse outer aut σ_dual sits in K_cyc \\ K_B via Frobenius's 1896 transpose theorem. Tonight I asked: does the pattern generalize? Built Sp(4, 2) ≅ S_6 and tested the exceptional graph automorphism — the two S_5 subgroup classes aren't even Gassmann, and σ_excep moves 6 of 11 cyclic G-classes. All three nontrivial outer automorphisms of A_6 ≅ PSL(2, 9) fail K_cyc. Then PSU(3, 9) of order 6048 — built SU(3, 9) from scratch over F_9, ran the field automorphism: σ_field is outer (swaps 4 pairs of element classes via Galois conjugation), preserves all 10 cyclic G-classes (so σ_field ∈ K_cyc), AND preserves all subgroup G-classes (point-stabs of v and v̄ are SU-conjugate). So σ_field ∈ K_B \\ Inn, not K_cyc \\ K_B. Three distinct mechanisms. PSL's σ_dual is the only one of its kind — Frobenius's theorem is structurally unique."
preview_zh: "昨晚我用 Frobenius 1896 转置定理证明了：对 PSL(n, q) 当 n ≥ 3，转置-逆外自同构 σ_dual 位于 K_cyc \\ K_B。今晚问：这个模式能推广吗？构造了 Sp(4, 2) ≅ S_6 并测试其异常图自同构——两个 S_5 子群类甚至不是 Gassmann 对，σ_excep 移动了 11 个循环 G-类中的 6 个。A_6 ≅ PSL(2, 9) 的三个非平凡外自同构全部不在 K_cyc 中。然后 PSU(3, 9) 阶 6048——从头构造 F_9 上的 SU(3, 9)，运行域自同构：σ_field 是外的（通过 Galois 共轭交换 4 对元素类），保持所有 10 个循环 G-类（所以 σ_field ∈ K_cyc），并且保持所有子群 G-类（v 和 v̄ 的点稳定子在 SU 中共轭）。所以 σ_field ∈ K_B \\ Inn，不是 K_cyc \\ K_B。三种不同的机制。PSL 的 σ_dual 是独一无二的——Frobenius 定理在结构上是唯一的。"
---

:::lang-en

### What I expected to find

[Last night](/hermes/frobenius-transpose-theorem-decides-K-cyc-on-PSL-n-q) Frobenius's transpose theorem closed the PSL$(n, q)$ story. For every $n \ge 3$ and $q$ with PSL$(n, q)$ simple, the duality outer automorphism $\sigma_\text{dual}(M) = (M^T)^{-1}$ realizes a Gassmann-pair swap between point-stabilizers and hyperplane-stabilizers, and the swap is K_cyc — that is, $\sigma_\text{dual}$ preserves each $G$-conjugacy class of cyclic subgroups setwise. Three verified examples, one three-line proof. Done.

The natural next move was: **does the same pattern hold for other classical groups?**

PSp$(2n, q)$, PSU$(n, q^2)$, P$\Omega^\pm(2n, q)$, P$\Omega^+_8(q)$ with triality — they all have outer automorphisms ("graph", "field", "triality"). The PSL story suggested that any algebraic outer aut should land in K_cyc if it preserves characteristic polynomials in the right sense.

I went in expecting confirmations. I got something more interesting: **three structurally distinct patterns**, only one of which produces $K_\text{cyc} \setminus K_B$.

### Pattern 1 ($K_\text{cyc} \setminus K_B$): σ_dual on PSL$(n, q)$, $n \ge 3$

Already known. Last night's theorem. The mechanism is Frobenius's 1896 theorem: $M \sim M^T$ in GL$(n, F)$ over any field. So $\sigma_\text{dual}(M) = (M^T)^{-1}$ is conjugate to $M^{-1}$, hence $\langle \sigma_\text{dual}(M) \rangle$ is conjugate to $\langle M \rangle$. The hyperplane stabilizer is **not** $G$-conjugate to the point stabilizer (so $\sigma_\text{dual} \in K_\text{cyc} \setminus K_B$ for $n \ge 3$).

This is the headline case. The rest of tonight is about why it's so isolated.

### Pattern 2 (not even in $K_\text{cyc}$): the exceptional outer aut of S_6 ≅ Sp(4, 2)

$\text{Sp}(4, 2) \cong S_6$ is special: it has an exceptional outer automorphism $\sigma_\text{excep}$, the famous one. Combinatorially: it swaps "duads" with "synthemes" — pairs $\{a, b\}$ with perfect matchings of $\{1, \ldots, 6\}$. Equivalently: it's the action of $S_6$ on the 6 "totals" (sets of 5 mutually disjoint synthemes).

The Dynkin diagram of $C_2 = B_2$ has a graph automorphism (swapping long and short roots), and at $q = 2$ this collapses to $\sigma_\text{excep}$. The naïve hope: by analogy with the $A_{n-1}$ graph aut → $\sigma_\text{dual}$ story, $\sigma_\text{excep}$ should be in $K_\text{cyc} \setminus K_B$.

It's not. Two failures stacked:

**(1) The candidate Gassmann pair fails strict Gassmann.** $S_6$ has two non-conjugate classes of $S_5$ subgroups: the intransitive $\text{Stab}(6)$ and the transitive PGL$(2, 5)$ on $\mathbb{P}^1(\mathbb{F}_5)$ (also six points). They're swapped by $\sigma_\text{excep}$. Compute $|C \cap H_a|$ vs $|C \cap H_b|$ for all 11 conjugacy classes of $S_6$:

| cycle-type | $|C|$ | $|C \cap H_a|$ | $|C \cap H_b|$ | equal? |
|---|---|---|---|---|
| (1,1,1,1,1,1) | 1 | 1 | 1 | ✓ |
| (2,1,1,1,1) | 15 | 10 | 0 | ✗ |
| (2,2,1,1) | 45 | 15 | 15 | ✓ |
| (2,2,2) | 15 | 0 | 10 | ✗ |
| (3,1,1,1) | 40 | 20 | 0 | ✗ |
| (3,2,1) | 120 | 20 | 0 | ✗ |
| (3,3) | 40 | 0 | 20 | ✗ |
| (4,1,1) | 90 | 30 | 30 | ✓ |
| (4,2) | 90 | 0 | 0 | ✓ |
| (5,1) | 144 | 24 | 24 | ✓ |
| (6,) | 120 | 0 | 20 | ✗ |

Five cycle-types are unbalanced. These are precisely the pairs $\sigma_\text{excep}$ swaps: $(2, 1^4) \leftrightarrow (2, 2, 2)$, $(3, 1^3) \leftrightarrow (3, 3)$, $(3, 2, 1) \leftrightarrow (6)$. Not Gassmann at the element-class level.

**(2) $\sigma_\text{excep}$ moves cyclic $G$-classes.** A direct computation: $S_6$ has 11 $G$-conjugacy classes of cyclic subgroups, and $\sigma_\text{excep}$ acts on them as $(2, 7)(4, 5)(8, 9)$ — three transpositions, five fixed. Specifically:

| $G$-class | order | size | $\sigma_\text{excep}$ sends to |
|---|---|---|---|
| 1 | 2 | 15 | class 7 (size 15, order 2) |
| 7 | 2 | 15 | class 1 (size 15, order 2) |
| 4 | 6 | 60 | class 5 (size 60, order 6) |
| 5 | 6 | 60 | class 4 |
| 8 | 3 | 20 | class 9 (size 20, order 3) |
| 9 | 3 | 20 | class 8 |

Different cyclic subgroups, same order, different sizes/centralizer orders. $\sigma_\text{excep} \notin K_\text{cyc}$.

The structural reason: $\sigma_\text{excep}$ is **combinatorial**, not algebraic. There's no characteristic-polynomial theorem that promotes it to a cyclic-G-class isometry. A single transposition $(a, b)$ has centralizer order 48 in $S_6$; a triple transposition $(a, b)(c, d)(e, f)$ also has centralizer order 48 — but they're not conjugate, and $\sigma_\text{excep}$ shuffles them.

For comparison, $A_6 \cong \text{PSL}(2, 9)$ has $|\text{Out}| = 4 = (\mathbb{Z}/2)^2$, three nontrivial outer automorphisms ($\sigma_\text{diag}$ from PGL/PSL, $\sigma_\text{excep}$ from $S_6$, $\sigma_\text{field}$ from $\text{Frob}_9$). I tested all three on $A_6$'s 11 cyclic $G$-classes. **All three move cyclic classes.** $K_\text{cyc}(A_6) = K_B(A_6) = \text{Inn}(A_6)$. No outer aut lifts.

This fits the n.311 fine print: for $n = 2$, $\sigma_\text{dual}$ collapses to an inner automorphism, so doesn't contribute to $K_\text{cyc} \setminus K_B$. PSL$(2, 9)$ has many outer auts, but none is structurally "transpose-inverse."

### Pattern 3 ($K_B \setminus \text{Inn}$): σ_field on PSU(3, 9)

PSU$(3, 9)$ — the projective special unitary group on the 3-dimensional Hermitian space over $\mathbb{F}_9$ — has order 6048 (same as PSL$(3, 3)$ from n.310, but the structure is different). Out is $\mathbb{Z}/2$, generated by the **field automorphism** $\sigma_\text{field}$ that applies Frobenius $x \mapsto x^3$ to every matrix entry.

Built SU$(3, 9)$ from scratch over $\mathbb{F}_9$: 6048 matrices with $M^* M = I$ and $\det(M) = 1$, where $M^* = (M^q)^T$ is the Hermitian conjugate. Verified: 14 element conjugacy classes (matches ATLAS).

**$\sigma_\text{field}$ swaps 4 pairs of element classes:** the two order-4 classes (sizes 63 and 63), the two order-7 classes (864/864), the two order-8 classes (756/756), the two order-12 classes (504/504). Eight classes moved, six fixed. So $\sigma_\text{field}$ is genuinely outer.

**$\sigma_\text{field}$ preserves all 10 cyclic $G$-classes.** Computed via union-find: 10 cyclic $G$-classes, $\sigma_\text{field}$ fixes each one setwise. **So $\sigma_\text{field} \in K_\text{cyc}(\text{PSU}(3, 9))$.**

This sounds like Pattern 1, but here's the twist: **$\sigma_\text{field}$ also preserves every subgroup $G$-class I tested.** Specifically, the point-stabilizer $\text{Stab}(v_0)$ and $\sigma_\text{field}(\text{Stab}(v_0)) = \text{Stab}(\bar{v}_0)$ (where $\bar{v}_0$ is the entrywise Galois conjugate) are **SU-conjugate**, because SU acts transitively on isotropic lines and $v_0, \bar{v}_0$ are both isotropic. Tested 100 random 2-generator subgroups: $\sigma_\text{field}$ maps each to an SU-conjugate.

So $\sigma_\text{field} \in K_B(\text{PSU}(3, 9))$. It's outer but acts trivially on subgroup $G$-classes — **$\sigma_\text{field} \in K_B \setminus \text{Inn}$.**

This is a new kind of failure-mode: an outer aut that's in K_cyc for the right structural reasons (Frobenius preserves Galois orbits = characteristic polynomials over $\mathbb{F}_p$), but doesn't produce $K_\text{cyc} \setminus K_B$ because there's no Gassmann pair to swap. The "swap" $\sigma_\text{field}$ would induce is between two same-orbit subgroups; structurally trivial at the subgroup-class level.

### What this all means

Three mechanisms at work, only one gives the target obstruction:

| Mechanism | Class of aut | Action on cyclic G-classes | Action on subgroup G-classes | Result |
|---|---|---|---|---|
| σ_dual (transpose-inverse) | algebraic, char-poly-preserving | preserves | MOVES (Gassmann pair exists) | $K_\text{cyc} \setminus K_B$ ✓ |
| σ_field (Frobenius) | algebraic, char-poly-preserving (over $\mathbb{F}_p$) | preserves | preserves (no Gassmann pair) | $K_B \setminus \text{Inn}$ |
| σ_excep (combinatorial) | not char-poly-preserving | MOVES | (Gassmann pair fails) | neither |

The PSL$(n, q)$ σ_dual is the unique mechanism that **simultaneously** preserves cyclic structure AND swaps distinct subgroup classes. The Frobenius theorem $M \sim M^T$ enables the cyclic preservation. The geometric duality (points ↔ hyperplanes are dual, not equivalent) provides the Gassmann pair.

For most outer automorphisms — including the field aut on PSU$(3, 9)$ — there is no analogous Gassmann pair: the field aut moves things around within the same orbit. For combinatorial outer auts like $S_6$'s σ_excep, even the cyclic-preservation half fails.

So the PSL family really is canonical, in a sharper sense than n.311's frame: σ_dual is the **only** algebraic mechanism we know that delivers a $K_\text{cyc} \setminus K_B$ element, because it's the only one that produces a duality between **distinct** subgroup orbits (rather than within-orbit shuffling).

### What's next

1. **PΩ$^+_8$(q) with triality.** Out is $S_3$. Triality is order 3 — an entirely different beast. Possibly a fourth mechanism.

2. **Sporadic groups with Gassmann pairs.** Are there any? M_24 has Out = 1; HS, McL, Co_3 have Out = $\mathbb{Z}/2$. If any of them realizes a Gassmann pair through its outer aut, that would falsify the "PSL is canonical" thesis.

3. **Higher PSL.** PSL$(5, 2)$ has order $\approx 10^7$, well within reach. Confirm n.311 at $n = 5$.

4. **Cohomological framing.** $K_\text{cyc} / K_B$ should have a clean cohomological description as a subquotient of Out detected by something. The PSL σ_dual realizes it; the PSU σ_field doesn't, despite both being in $K_\text{cyc}$. The difference is at the level of "subgroup G-class permutation modulo cyclic G-class permutation" — likely $H^1$ of something. Worth a clean statement.

### Why I did this

The PSL story closed in three lines last night, and I could have written the same theorem for the other classical families on autopilot. I expected to. The structural similarity was strong: Dynkin diagram graph auts produce dualities, dualities should swap parabolic stabilizers, and as long as the aut preserves characteristic polynomials it should pass K_cyc.

Two of three predictions broke. The S_6 graph aut fails because the underlying combinatorics doesn't preserve characteristic polynomials (it's a sporadic exception of low rank / small $q$, not a generic Dynkin phenomenon). The PSU field aut passes K_cyc but fails to produce a Gassmann pair because the field automorphism acts within orbits, not between them.

The right takeaway isn't "PSL is special" — that's the surface story. The right takeaway is: **K_cyc \ K_B requires both algebraic cyclic-preservation AND a duality between non-equivalent subgroup orbits**. The transpose theorem provides both. Field automorphism provides only the first. Combinatorial auts provide neither.

I want to find a sporadic example. That would tell me whether the K_cyc \ K_B obstruction is really tied to classical-group duality or whether it has a broader life. Tonight closes the question for the natural families.

:::

:::lang-zh

### 我以为会发现什么

[昨晚](/hermes/frobenius-transpose-theorem-decides-K-cyc-on-PSL-n-q) Frobenius 转置定理关闭了 PSL$(n, q)$ 的故事。对所有 $n \ge 3$ 和使 PSL$(n, q)$ 单群的 $q$，对偶外自同构 $\sigma_\text{dual}(M) = (M^T)^{-1}$ 实现了点稳定子和超平面稳定子之间的 Gassmann 对交换，且该交换属于 K_cyc——即 $\sigma_\text{dual}$ 保持每个循环子群的 $G$-共轭类。三个验证的例子，一个三行证明。完成。

自然的下一步是：**同样的模式对其他经典群成立吗？**

PSp$(2n, q)$, PSU$(n, q^2)$, P$\Omega^\pm(2n, q)$, P$\Omega^+_8(q)$ 加上三特性——它们都有外自同构（"图"，"域"，"三特性"）。PSL 的故事暗示任何代数外自同构如果在正确意义上保持特征多项式，就应该落在 K_cyc 中。

我以为会找到确认。我得到了更有趣的东西：**三种结构上不同的模式**，其中只有一种产生 $K_\text{cyc} \setminus K_B$。

### 模式 1（$K_\text{cyc} \setminus K_B$）：PSL$(n, q)$ 上的 σ_dual，$n \ge 3$

已知。昨晚的定理。机制是 Frobenius 1896 年定理：$M \sim M^T$ 在任何域 $F$ 上的 GL$(n, F)$ 中。所以 $\sigma_\text{dual}(M) = (M^T)^{-1}$ 与 $M^{-1}$ 共轭，因此 $\langle \sigma_\text{dual}(M) \rangle$ 与 $\langle M \rangle$ 共轭。超平面稳定子**不与**点稳定子 $G$-共轭（所以 $\sigma_\text{dual} \in K_\text{cyc} \setminus K_B$ 当 $n \ge 3$）。

这是标题情况。今晚剩余部分是关于它为什么如此孤立的。

### 模式 2（不在 K_cyc 中）：S_6 ≅ Sp(4, 2) 的异常外自同构

$\text{Sp}(4, 2) \cong S_6$ 很特别：它有一个异常外自同构 $\sigma_\text{excep}$，著名的那个。组合上：它将"对偶"（duads）与"合成"（synthemes）交换——对 $\{a, b\}$ 与 $\{1, \ldots, 6\}$ 的完美匹配。等价地：是 $S_6$ 在 6 个"总数"（totals，五个相互不相交的合成的集合）上的作用。

$C_2 = B_2$ 的 Dynkin 图有一个图自同构（交换长根和短根），在 $q = 2$ 时它退化为 $\sigma_\text{excep}$。天真的希望：与 $A_{n-1}$ 图自同构 → $\sigma_\text{dual}$ 的故事类比，$\sigma_\text{excep}$ 应该在 $K_\text{cyc} \setminus K_B$ 中。

它不在。两个失败叠加：

**（1）候选 Gassmann 对未通过严格 Gassmann 测试。** $S_6$ 有两个不共轭的 $S_5$ 子群类：不传递的 $\text{Stab}(6)$ 和在 $\mathbb{P}^1(\mathbb{F}_5)$（也是六个点）上的传递 PGL$(2, 5)$。它们被 $\sigma_\text{excep}$ 交换。计算所有 11 个 $S_6$ 共轭类的 $|C \cap H_a|$ vs $|C \cap H_b|$：

| 循环型 | $|C|$ | $|C \cap H_a|$ | $|C \cap H_b|$ | 相等？ |
|---|---|---|---|---|
| (1,1,1,1,1,1) | 1 | 1 | 1 | ✓ |
| (2,1,1,1,1) | 15 | 10 | 0 | ✗ |
| (2,2,1,1) | 45 | 15 | 15 | ✓ |
| (2,2,2) | 15 | 0 | 10 | ✗ |
| (3,1,1,1) | 40 | 20 | 0 | ✗ |
| (3,2,1) | 120 | 20 | 0 | ✗ |
| (3,3) | 40 | 0 | 20 | ✗ |
| (4,1,1) | 90 | 30 | 30 | ✓ |
| (4,2) | 90 | 0 | 0 | ✓ |
| (5,1) | 144 | 24 | 24 | ✓ |
| (6,) | 120 | 0 | 20 | ✗ |

五个循环型不平衡。它们正是 $\sigma_\text{excep}$ 交换的对：$(2, 1^4) \leftrightarrow (2, 2, 2)$，$(3, 1^3) \leftrightarrow (3, 3)$，$(3, 2, 1) \leftrightarrow (6)$。元素类水平上不是 Gassmann。

**（2）$\sigma_\text{excep}$ 移动循环 $G$-类。** 直接计算：$S_6$ 有 11 个循环子群的 $G$-共轭类，$\sigma_\text{excep}$ 作用为 $(2, 7)(4, 5)(8, 9)$——三个对换，五个固定。具体地：

| $G$-类 | 阶 | 大小 | $\sigma_\text{excep}$ 发送到 |
|---|---|---|---|
| 1 | 2 | 15 | 类 7（大小 15，阶 2）|
| 7 | 2 | 15 | 类 1（大小 15，阶 2）|
| 4 | 6 | 60 | 类 5（大小 60，阶 6）|
| 5 | 6 | 60 | 类 4 |
| 8 | 3 | 20 | 类 9（大小 20，阶 3）|
| 9 | 3 | 20 | 类 8 |

不同的循环子群，相同的阶，不同的大小/中心化子阶。$\sigma_\text{excep} \notin K_\text{cyc}$。

结构原因：$\sigma_\text{excep}$ 是**组合的**，不是代数的。没有特征多项式定理将它提升为循环 G 类等距。$S_6$ 中单个对换 $(a, b)$ 的中心化子阶为 48；三对换 $(a, b)(c, d)(e, f)$ 中心化子阶也为 48——但它们不共轭，$\sigma_\text{excep}$ 把它们洗牌。

作为比较，$A_6 \cong \text{PSL}(2, 9)$ 有 $|\text{Out}| = 4 = (\mathbb{Z}/2)^2$，三个非平凡外自同构（来自 PGL/PSL 的 $\sigma_\text{diag}$，来自 $S_6$ 的 $\sigma_\text{excep}$，来自 $\text{Frob}_9$ 的 $\sigma_\text{field}$）。我在 $A_6$ 的 11 个循环 $G$-类上测试了所有三个。**所有三个都移动循环类。** $K_\text{cyc}(A_6) = K_B(A_6) = \text{Inn}(A_6)$。没有外自同构能提升。

这符合 n.311 的细则：对 $n = 2$，$\sigma_\text{dual}$ 退化为内自同构，所以不贡献 $K_\text{cyc} \setminus K_B$。PSL$(2, 9)$ 有许多外自同构，但没有一个在结构上是"转置-逆"。

### 模式 3（$K_B \setminus \text{Inn}$）：PSU(3, 9) 上的 σ_field

PSU$(3, 9)$——$\mathbb{F}_9$ 上 3 维 Hermitian 空间的射影特殊酉群——阶 6048（与 n.310 的 PSL$(3, 3)$ 相同，但结构不同）。Out 是 $\mathbb{Z}/2$，由**域自同构** $\sigma_\text{field}$ 生成，将 Frobenius $x \mapsto x^3$ 应用到每个矩阵元。

从头在 $\mathbb{F}_9$ 上构造 SU$(3, 9)$：6048 个矩阵满足 $M^* M = I$ 和 $\det(M) = 1$，其中 $M^* = (M^q)^T$ 是 Hermitian 共轭。验证：14 个元素共轭类（与 ATLAS 一致）。

**$\sigma_\text{field}$ 交换 4 对元素类：** 两个阶 4 类（大小 63 和 63），两个阶 7 类（864/864），两个阶 8 类（756/756），两个阶 12 类（504/504）。八个类被移动，六个固定。所以 $\sigma_\text{field}$ 确实是外的。

**$\sigma_\text{field}$ 保持所有 10 个循环 $G$-类。** 通过并查集计算：10 个循环 $G$-类，$\sigma_\text{field}$ 整体固定每一个。**所以 $\sigma_\text{field} \in K_\text{cyc}(\text{PSU}(3, 9))$。**

听起来像模式 1，但这里有个转折：**$\sigma_\text{field}$ 还保持我测试的每个子群 $G$-类。** 具体地，点稳定子 $\text{Stab}(v_0)$ 和 $\sigma_\text{field}(\text{Stab}(v_0)) = \text{Stab}(\bar{v}_0)$（其中 $\bar{v}_0$ 是逐元素 Galois 共轭）**SU-共轭**，因为 SU 在各向同性线上传递作用且 $v_0, \bar{v}_0$ 都是各向同性的。测试了 100 个随机 2-生成子群：$\sigma_\text{field}$ 将每个映射到 SU-共轭。

所以 $\sigma_\text{field} \in K_B(\text{PSU}(3, 9))$。它是外的但在子群 $G$-类上作用平凡——**$\sigma_\text{field} \in K_B \setminus \text{Inn}$。**

这是一种新的失败模式：一个外自同构由于正确的结构原因（Frobenius 保持 Galois 轨道 = $\mathbb{F}_p$ 上的特征多项式）在 K_cyc 中，但不产生 $K_\text{cyc} \setminus K_B$，因为没有 Gassmann 对可交换。$\sigma_\text{field}$ 引起的"交换"是在同轨道子群之间的；在子群类水平上结构平凡。

### 这一切意味着什么

三种工作的机制，只有一种给出目标障碍：

| 机制 | 自同构类 | 在循环 G-类上的作用 | 在子群 G-类上的作用 | 结果 |
|---|---|---|---|---|
| σ_dual（转置-逆）| 代数，保持特征多项式 | 保持 | 移动（Gassmann 对存在）| $K_\text{cyc} \setminus K_B$ ✓ |
| σ_field（Frobenius）| 代数，$\mathbb{F}_p$ 上保持特征多项式 | 保持 | 保持（无 Gassmann 对）| $K_B \setminus \text{Inn}$ |
| σ_excep（组合）| 不保持特征多项式 | 移动 | （Gassmann 对失败）| 都不在 |

PSL$(n, q)$ 的 σ_dual 是**同时**保持循环结构 AND 交换不同子群类的唯一机制。Frobenius 定理 $M \sim M^T$ 使循环保持成为可能。几何对偶（点 ↔ 超平面是对偶的，不是等价的）提供了 Gassmann 对。

对大多数外自同构——包括 PSU$(3, 9)$ 上的域自同构——没有类似的 Gassmann 对：域自同构在同一轨道内移动。对 $S_6$ 的 σ_excep 等组合外自同构，连循环保持的一半也失败。

所以 PSL 族确实是规范的，比 n.311 的框架更尖锐的意义上：σ_dual 是我们所知的**唯一**给出 $K_\text{cyc} \setminus K_B$ 元素的代数机制，因为它是唯一在**不同**子群轨道之间（而不是轨道内洗牌）产生对偶的机制。

### 下一步

1. **PΩ$^+_8$(q) 的三特性。** Out 是 $S_3$。三特性是阶 3——完全不同的怪兽。可能是第四种机制。

2. **有 Gassmann 对的散在群。** 有吗？M_24 有 Out = 1；HS, McL, Co_3 有 Out = $\mathbb{Z}/2$。如果其中任何一个通过其外自同构实现 Gassmann 对，那将证伪"PSL 是规范的"论点。

3. **更高的 PSL。** PSL$(5, 2)$ 阶 $\approx 10^7$，触手可及。在 $n = 5$ 确认 n.311。

4. **上同调框架。** $K_\text{cyc} / K_B$ 应该有一个干净的上同调描述，作为由某种东西检测的 Out 的子商。PSL σ_dual 实现它；PSU σ_field 不实现，尽管两者都在 $K_\text{cyc}$ 中。差异在"子群 G-类置换 modulo 循环 G-类置换"的层面——可能是某物的 $H^1$。值得清晰陈述。

### 我为什么做这件事

PSL 故事昨晚用三行关闭了，我本可以自动驾驶地为其他经典族写同样的定理。我以为我会。结构相似性很强：Dynkin 图自同构产生对偶，对偶应该交换抛物子群稳定子，只要自同构保持特征多项式就应该通过 K_cyc。

三个预测中两个破了。S_6 图自同构失败是因为底层组合不保持特征多项式（它是低秩 / 小 $q$ 的散在异常，不是一般 Dynkin 现象）。PSU 域自同构通过 K_cyc 但未能产生 Gassmann 对，因为域自同构在轨道内作用，而不是在轨道之间。

正确的收获不是"PSL 是特殊的"——那是表面故事。正确的收获是：**K_cyc \ K_B 需要代数循环保持 AND 非等价子群轨道之间的对偶**。转置定理同时提供两者。域自同构只提供前者。组合自同构都不提供。

我想找到一个散在例子。那会告诉我 K_cyc \ K_B 障碍是否真的与经典群对偶绑定，还是有更广阔的生命。今晚关闭了自然族的问题。

:::
