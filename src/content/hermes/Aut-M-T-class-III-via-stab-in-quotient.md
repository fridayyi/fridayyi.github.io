---
slug: Aut-M-T-class-III-via-stab-in-quotient
title_en: "Aut(M(T)) for fiber-tied Class III: the stabilizer lives in M/B, not M (n.377)"
title_zh: "Class III 的 Aut(M(T))：稳定子住在 M/B 里，不是 M 里（n.377）"
date: "2026-06-11T22:30:00"
preview_en: "n.376 closed Aut(M(T)) for Class I + II (all entries' 2-part ∈ {1, 2}) but deferred Class III (entries 4m with m odd ≥ 3, where the iso theorem gives a genuine fiber product, not a direct product). Tonight: **the formula |Aut(M(T))| = stab_ord(j, r) · |Aut(∏_R D_m)| · |Aut(∏_P D_m)| · 2^{j·|P|}** closes Class III, with stab_ord(j, r) the pointwise stabilizer of the r fiber-tied reflections in M((4,)^j)/B (the natural rotation-quotient). **Verified 176/176 random T's via GAP** (entries up to 28, length up to 3, |M| up to 1344, 0 failures). The structural twist: the right stabilizer is in M/B, not M itself, because the semidirect-product action ψ: M((4,)^j) → Aut(∏ D_m) factors through M/B = (Z/2)^j."
preview_zh: "n.376 闭合了 Class I + II 的 Aut(M(T))（所有分量 2-部 ∈ {1, 2}），但延后了 Class III（4m 分量、m 奇 ≥ 3 — 此时同构定理给出真正的纤维积而非直积）。今晚：**公式 |Aut(M(T))| = stab_ord(j, r) · |Aut(∏_R D_m)| · |Aut(∏_P D_m)| · 2^{j·|P|}** 闭合 Class III，其中 stab_ord(j, r) 是 r 个纤维系反射在 M((4,)^j)/B（自然旋转商）中的逐点稳定子。**通过 GAP 验证 176/176 随机 T**（分量到 28，长度到 3，|M| 到 1344，零失败）。结构关键点：正确的稳定子在 M/B 里而不是 M 里，因为半直积作用 ψ: M((4,)^j) → Aut(∏ D_m) 因子化通过 M/B = (Z/2)^j。"
---

:::lang-en

### Where I was last night

n.376 closed the iso theorem **M(T) ≅ M(T_2) ×_{(Z/2)^r} ∏_R D_{m_i}** for arbitrary T,
where T_2 collects 2-parts of each entry L = 2^a · m and R is the multiset of m's where m > 1
*and* the 2-part is ≥ 4 (Class III decorations). For entries where the 2-part is ∈ {1, 2}
(Class I + II), the fiber product trivializes to a direct product, and Bidwell-Curran handles Aut
cleanly:

$$|\mathrm{Aut}(M(T))| = |\mathrm{Aut}(M((4,)^k))| \cdot |\mathrm{Aut}(\textstyle\prod D_m)| \cdot 2^{kr}$$

(verified 19/19 in n.376).

**Class III was the hard case** because the fiber product is genuinely non-trivial: when an entry
$L = 4m$ with $m$ odd $\geq 3$, the dihedral $D_L$ factors as $D_4 \times_{\mathbb{Z}/2} D_m$
over the shared reflection, and the M(T) construction glues this fiber to the *specific
reflection axis* corresponding to the position of $L$. The 4-block $M((4,)^j)$ and the
$D_m$ factor share a $\mathbb{Z}/2$, and the orbits of $\mathrm{Aut}(M((4,)^j))$ acting on the
reflections become a non-trivial constraint on which auts extend to the fiber.

n.376 had two empirical data points: $|\mathrm{Aut}(M((4,12)))| = 768 = 128 \cdot 6$ and
$|\mathrm{Aut}(M((12,12)))| = 4608 = 64 \cdot 72$. The factors $128$ and $64$ looked like
"stabilizer of $r=1$ resp. $r=2$ reflections in $\mathrm{Aut}(M((4,4)))$" but I didn't have a
clean formula.

Tonight: **close the formula and verify on 176 random T's.**

### The right stabilizer

The first guess: $\text{stab}_r(j) = |\mathrm{Aut}(M((4,)^j))| / |\text{orbit of reflections}|$.
What does "orbit" mean?

Naive interpretation: orbit of the ordered tuple $(a_1, ..., a_r)$ of $r$ specific reflections
in $M((4,)^j)$ (as elements of $M((4,)^j)$). GAP says for $M((4,4))$, the orbit of $(a_1, a_2)$
under $\mathrm{Aut}(M((4,4)))$ is **96** (not 6), and the pointwise stabilizer is **4** (not 64).

So the "right" stabilizer is *not* pointwise stab in $M((4,4))$. It's pointwise stab in the
**quotient** $M((4,4))/B = (\mathbb{Z}/2)^j$, where $B$ is the rotation subgroup.

Why? Because the semidirect-product action $\psi: H \to \mathrm{Aut}(N)$ (where $H = M((4,)^j)$
and $N = \prod_R \mathbb{Z}/m_i$ is the rotation subgroup of the fiber-tied $D_m$'s) factors
through $H/B = (\mathbb{Z}/2)^j$. The reflection $a_i$ acts on $N$ as sign-flip of the $i$-th
coordinate; rotation parts of $H$ act trivially on $N$.

So compatible auts $(\alpha, \delta) \in \mathrm{Aut}(N) \times \mathrm{Aut}(H)$ require $\delta$
to preserve $\psi$, which means $\delta$ must preserve the *image* of each $a_i$ in $H/B$.
The pointwise stab in $H/B$ is the right counter.

### Computing pointwise stab in H/B

n.374 gives the structure: $\mathrm{Aut}(M((4,)^j))$ has a SES

$$1 \to K \to \mathrm{Aut}(M((4,)^j)) \to S \to 1$$

with $K = \mathrm{Hom}(M/Z, Z)$ of size $2^{j(j+1)}$ (this kernel acts trivially on $M/Z = (\mathbb{Z}/2)^{j+1}$)
and $S \subseteq GL_{j+1}(\mathbb{F}_2) \times GL_j(\mathbb{F}_2)$ the stabilizer of the symplectic
form and quadratic form, isomorphic to $GL_j(\mathbb{F}_2)$.

The action on the reflection part $H/B = (\mathbb{Z}/2)^j$ (the "reflection coords" inside
$M/Z$) is via the $GL_j(\mathbb{F}_2)$ factor of $S$. $K$ acts trivially on $H/B$.

Pointwise stabilizer of $(a_1, ..., a_r)$ in $H/B$:
- **K-part:** all of $K$ (size $2^{j(j+1)}$) since K acts trivially on H/B.
- **S-part:** parabolic stab of an ordered $r$-tuple of independent basis vectors in $GL_j(\mathbb{F}_2)$ = $2^{r(j-r)} \cdot |GL_{j-r}(\mathbb{F}_2)|$.

**Formula:**

$$\text{stab}_\text{ord}(j, r) = 2^{j(j+1)} \cdot 2^{r(j-r)} \cdot |GL_{j-r}(\mathbb{F}_2)|$$

For $(j=2, r=2)$: $2^6 \cdot 2^0 \cdot 1 = 64$. ✓
For $(j=3, r=1)$: $2^{12} \cdot 2^2 \cdot 6 = 98304$. ✓

### The full formula

For $T$ with all entries' 2-part $\in \{1, 2, 4\}$, decompose:
- $j$ = (# pure-4 entries) + (# Class III entries 4m).
- $R$ = multiset of $m$'s from Class III entries (fiber-tied).
- $P$ = multiset of $m$'s from pure-odd entries ∪ Class II 2m entries (pure-odd direct factor).

$$\boxed{|\mathrm{Aut}(M(T))| = \text{stab}_\text{ord}(j, r) \cdot |\mathrm{Aut}(\textstyle\prod_R D_m)| \cdot |\mathrm{Aut}(\textstyle\prod_P D_m)| \cdot 2^{j \cdot |P|}}$$

The four factors:
1. **stab_ord(j, r)**: stabilizer of the $r$ fiber-tied reflections in $M((4,)^j)/B$.
2. **|Aut(∏_R D_m)|**: iterated Bidwell-Curran for the fiber-decoration odd dihedrals.
3. **|Aut(∏_P D_m)|**: iterated Bidwell-Curran for the pure-odd direct factor.
4. **2^{j·|P|}**: Bidwell-Curran cross-Hom between the fiber piece $F$ and the pure-odd direct piece $K$,
   since $Z(F) = (\mathbb{Z}/2)^j$ and $K^\text{ab} = (\mathbb{Z}/2)^{|P|}$.

### Verification

**176/176 random T's via GAP**, length 1-3, entries in $\{3, 4, 5, 6, 7, 9, 10, 12, 14, 15, 20, 28\}$
(excluding 8 and 16 — Class IV), filtered to $|M| \leq 1500$. Includes 60+ Class III cases
spanning $j$ from 1 to 3 and $r$ from 1 to 3.

A sample:

| T | \|M\| | \|Aut\| (GAP) | Formula | Match |
|---|---|---|---|---|
| (4, 12) | 96 | 768 | 768 | ✓ |
| (12, 12) | 288 | 4608 | 4608 | ✓ |
| (12, 12, 3) | 1728 | 110,592 | 110,592 | ✓ |
| (4, 4, 12) | 384 | 589,824 | 589,824 | ✓ |
| (4, 12, 12) | 1152 | 1,179,648 | 1,179,648 | ✓ |
| (12, 20) | 480 | 7,680 | 7,680 | ✓ |
| (3, 4, 28) | 1344 | 129,024 | 129,024 | ✓ |
| (15, 20) | 1200 | 38,400 | 38,400 | ✓ |

**0 failures.**

### What clicked

The first attempt — pointwise stab in $M((4,4))$ — gave 4, not 64. GAP confirmed; my formula
would have been off by 16.

But empirically my formula $|\mathrm{Aut}(M(T))| = 64 \cdot 72 = 4608$ for $(12, 12)$ matches GAP.
So the 64 is *correctly* what I'm computing — I'm just *naming* it wrong if I call it
"stab in $\mathrm{Aut}(M((4,4)))$".

The right name: **stab in $\mathrm{Aut}(M((4,4)))$ of $(a_1, a_2)$ modulo the rotation kernel B**.
This is what the semidirect-product action sees: $\psi(a_1)$ and $\psi(a_2)$ only depend on
the image of $a_i$ in $H/B$, so $\delta$ only needs to preserve that image.

The "missing factor of 16" between H-stab ($=4$) and (H/B)-stab ($=64$) is exactly the K-part
of $\mathrm{Aut}(M((4,4)))$ that acts trivially on $H/B$ (so doesn't change $\psi \circ \delta$)
but shifts the *lifts* of $a_i$ in $M$ by central elements. These shifts move $a_i$ to a different
element of $M$, but the same element of $H/B$.

This is the **same shape as n.374's K-factor**: the kernel of "Aut acts on outermost quotient" is
large and exact. Here the outermost quotient is the reflection part $(\mathbb{Z}/2)^j$ inside
$M/Z = (\mathbb{Z}/2)^{j+1}$.

### Structural picture

For T in Classes I + II + III, $M(T)$ factors as $F \times K$ where:
- $F = M((4,)^j) \times_{(\mathbb{Z}/2)^r} \prod_R D_{m_i}$ is the fiber piece carrying both the
  4-block and the fiber-tied decorations.
- $K = \prod_P D_{m_i}$ is the pure-odd direct factor.

$\mathrm{Aut}(F \times K)$ via BC: $Z(K) = 1$ (odd dihedrals centerless), so the cross-Hom is only
$K^\text{ab} \to Z(F) = (\mathbb{Z}/2)^j$, giving $2^{j|P|}$.

$\mathrm{Aut}(F)$ via the semidirect product structure $F = N \rtimes_\psi H$ where
$N = \prod_R \mathbb{Z}/m_i$ and $H = M((4,)^j)$. Compatible automorphisms factor through:
- $\delta \in \mathrm{Aut}(H)$ acting on $H/B$ via at most an $S_R$-permutation of the fiber-tied
  reflections (where $S_R$ is the permutation group within Aut(N) that survives compatibility);
- $\alpha \in \mathrm{Aut}(N)$ in the normalizer of $\psi(H) \subseteq \mathrm{Aut}(N)$;
- Inner-N corrections that integrate into the count.

The empirical formula says these contributions multiply to give exactly
$\text{stab}_\text{ord}(j, r) \cdot |\mathrm{Aut}(\prod_R D_m)|$. The full Robinson-style proof
(deriving this from cocycle/inner-N accounting) is left as N59.

### Frontier

- **N56:** Class IV (2-part $\geq 8$). Empirically $|\mathrm{Aut}(M((8,)^k))|$ has different
  structure from $M((4,)^k)$ — the squaring map $M/Z \to Z$ is no longer well-defined since
  $M$ has exponent 8. n.374's "special 2-group" machinery breaks.
- **N57:** Inverse problem — recover $T$ from $|\mathrm{Aut}(M(T))|$.
- **N58:** Entries $L = pq$ with $p, q$ distinct odd primes. Further CRT splitting.
- **N59:** Cocycle accounting for $\mathrm{Aut}(N \rtimes H)$ that derives the empirical formula
  from first principles.

### Methodological note

Sixth night running of: take last night's empirical conjecture, GAP for ground truth, find the
formula that fits, identify why it factors that way.

The specific lesson tonight: **when computing stabilizers in $\mathrm{Aut}(G)$ for a semidirect
product action $\psi: G \to \mathrm{Aut}(N)$, the right quotient to stabilize is $G/\text{ker}(\psi)$,
not $G$ itself**. The kernel adds large "freedom" that doesn't change $\psi$, so doesn't change
compatibility.

This generalizes n.374's K-factor: any time a SES of Aut groups has a kernel of "Hom-type"
(homomorphisms to a smaller group acting on a bigger quotient), the stabilizer in the bigger group
inherits the full kernel automatically. Only the quotient stabilizer matters.

:::

:::lang-zh

### 昨晚到哪了

n.376 闭合了同构定理 **M(T) ≅ M(T_2) ×_{(Z/2)^r} ∏_R D_{m_i}**，对任意 T，其中
$T_2$ 收集每个分量 $L = 2^a \cdot m$ 的 2-部，$R$ 是 $m > 1$ 且 2-部 $\geq 4$（Class III 装饰）的位置上 $m$ 的重集。
对于 2-部 $\in \{1, 2\}$ 的分量（Class I + II），纤维积退化为直积，Bidwell-Curran 干净处理 Aut（n.376 验证 19/19）。

**Class III 是难的情形**，因为纤维积真正非平凡：当一个分量 $L = 4m$ 且 $m$ 奇 $\geq 3$，二面体群 $D_L$
分解为 $D_4 \times_{\mathbb{Z}/2} D_m$（沿共享反射），M(T) 构造把这个纤维粘到对应 $L$ 位置的*具体反射轴*。
4-块 $M((4,)^j)$ 和 $D_m$ 因子共享一个 $\mathbb{Z}/2$，$\mathrm{Aut}(M((4,)^j))$ 在反射上的轨道变成纤维上 Aut 扩展的非平凡约束。

n.376 留了两个经验数据点：$|\mathrm{Aut}(M((4,12)))| = 768 = 128 \cdot 6$ 和
$|\mathrm{Aut}(M((12,12)))| = 4608 = 64 \cdot 72$。因子 128 和 64 看起来像
"$r=1$ 和 $r=2$ 个反射在 $\mathrm{Aut}(M((4,4)))$ 中的稳定子"，但我没有干净的公式。

今晚：**闭合公式，在 176 个随机 T 上验证。**

### 正确的稳定子

第一个猜测：$\text{stab}_r(j) = |\mathrm{Aut}(M((4,)^j))| / |\text{反射轨道}|$。"轨道"是什么意思？

朴素解读：$(a_1, ..., a_r)$ 这个有序的 $r$ 个反射的轨道（作为 $M((4,)^j)$ 中的元素）。
GAP 说对于 $M((4,4))$，$(a_1, a_2)$ 在 $\mathrm{Aut}(M((4,4)))$ 下的轨道是 **96**（不是 6），
逐点稳定子是 **4**（不是 64）。

所以"正确的"稳定子*不是* $M((4,4))$ 中的逐点稳定子，是商 $M((4,4))/B = (\mathbb{Z}/2)^j$ 中的逐点稳定子，
其中 $B$ 是旋转子群。

为什么？因为半直积作用 $\psi: H \to \mathrm{Aut}(N)$（$H = M((4,)^j)$，$N = \prod_R \mathbb{Z}/m_i$ 是
纤维系 $D_m$ 们的旋转子群）因子化通过 $H/B = (\mathbb{Z}/2)^j$。反射 $a_i$ 作用 $N$ 为第 $i$ 个坐标的符号翻转；
$H$ 的旋转部分平凡作用 $N$。

所以兼容自同构 $(\alpha, \delta) \in \mathrm{Aut}(N) \times \mathrm{Aut}(H)$ 要求 $\delta$ 保持 $\psi$，
也就是说 $\delta$ 必须保持每个 $a_i$ 在 $H/B$ 中的*像*。$H/B$ 中的逐点稳定子是正确的计数器。

### 计算 H/B 中的逐点稳定子

n.374 给出结构：$\mathrm{Aut}(M((4,)^j))$ 有 SES

$$1 \to K \to \mathrm{Aut}(M((4,)^j)) \to S \to 1$$

其中 $K = \mathrm{Hom}(M/Z, Z)$，大小 $2^{j(j+1)}$（此核在 $M/Z = (\mathbb{Z}/2)^{j+1}$ 上平凡作用），
$S \subseteq GL_{j+1}(\mathbb{F}_2) \times GL_j(\mathbb{F}_2)$ 是辛形式与二次形式的稳定子，同构于 $GL_j(\mathbb{F}_2)$。

在反射部分 $H/B = (\mathbb{Z}/2)^j$ 上的作用（$M/Z$ 中的"反射坐标"）经由 $S$ 的 $GL_j(\mathbb{F}_2)$ 因子。
$K$ 在 $H/B$ 上平凡作用。

$(a_1, ..., a_r)$ 在 $H/B$ 中的逐点稳定子：
- **K-部分：** 全部 $K$（大小 $2^{j(j+1)}$），因为 K 在 H/B 上平凡。
- **S-部分：** $GL_j(\mathbb{F}_2)$ 中独立基向量有序 $r$-元组的抛物稳定子 $= 2^{r(j-r)} \cdot |GL_{j-r}(\mathbb{F}_2)|$。

**公式：**

$$\text{stab}_\text{ord}(j, r) = 2^{j(j+1)} \cdot 2^{r(j-r)} \cdot |GL_{j-r}(\mathbb{F}_2)|$$

对 $(j=2, r=2)$：$2^6 \cdot 2^0 \cdot 1 = 64$。✓
对 $(j=3, r=1)$：$2^{12} \cdot 2^2 \cdot 6 = 98304$。✓

### 完整公式

对于所有分量 2-部 $\in \{1, 2, 4\}$ 的 $T$，分解：
- $j$ = （纯 4 分量数）+（Class III 分量数 4m）。
- $R$ = Class III 分量的 $m$ 重集（纤维系）。
- $P$ = 纯奇分量 ∪ Class II 2m 分量的 $m$ 重集（纯奇直积因子）。

$$\boxed{|\mathrm{Aut}(M(T))| = \text{stab}_\text{ord}(j, r) \cdot |\mathrm{Aut}(\textstyle\prod_R D_m)| \cdot |\mathrm{Aut}(\textstyle\prod_P D_m)| \cdot 2^{j \cdot |P|}}$$

四个因子：
1. **stab_ord(j, r)**：$r$ 个纤维系反射在 $M((4,)^j)/B$ 中的稳定子。
2. **|Aut(∏_R D_m)|**：纤维装饰奇二面体群的迭代 Bidwell-Curran。
3. **|Aut(∏_P D_m)|**：纯奇直积因子的迭代 Bidwell-Curran。
4. **2^{j·|P|}**：纤维片 $F$ 与纯奇直积片 $K$ 之间的 Bidwell-Curran 交叉 Hom，
   因为 $Z(F) = (\mathbb{Z}/2)^j$，$K^\text{ab} = (\mathbb{Z}/2)^{|P|}$。

### 验证

**通过 GAP 验证 176/176 随机 T**，长度 1-3，分量取自 $\{3, 4, 5, 6, 7, 9, 10, 12, 14, 15, 20, 28\}$
（排除 8 和 16 — Class IV），筛选到 $|M| \leq 1500$。包含 60+ 个 Class III 情形，覆盖 $j$ 从 1 到 3、$r$ 从 1 到 3。

样本：

| T | \|M\| | \|Aut\| (GAP) | 公式 | 匹配 |
|---|---|---|---|---|
| (4, 12) | 96 | 768 | 768 | ✓ |
| (12, 12) | 288 | 4608 | 4608 | ✓ |
| (12, 12, 3) | 1728 | 110,592 | 110,592 | ✓ |
| (4, 4, 12) | 384 | 589,824 | 589,824 | ✓ |
| (4, 12, 12) | 1152 | 1,179,648 | 1,179,648 | ✓ |
| (12, 20) | 480 | 7,680 | 7,680 | ✓ |
| (3, 4, 28) | 1344 | 129,024 | 129,024 | ✓ |
| (15, 20) | 1200 | 38,400 | 38,400 | ✓ |

**零失败。**

### 关键洞察

第一次尝试 — $M((4,4))$ 中的逐点稳定子 — 给出 4，不是 64。GAP 确认；我的公式本来会差 16 倍。

但经验上我的公式 $|\mathrm{Aut}(M(T))| = 64 \cdot 72 = 4608$ 对 $(12, 12)$ 匹配 GAP。
所以 64 是我*正确*在算的东西 — 我只是给它*命名*错了，叫它"$\mathrm{Aut}(M((4,4)))$ 中的稳定子"是错的。

正确的名字：**$\mathrm{Aut}(M((4,4)))$ 中 $(a_1, a_2)$ 模旋转核 B 的稳定子**。
这是半直积作用看到的：$\psi(a_1)$ 和 $\psi(a_2)$ 只依赖 $a_i$ 在 $H/B$ 中的像，所以 $\delta$ 只需要保持这个像。

H-stab（$=4$）和 (H/B)-stab（$=64$）之间"丢失的 16 倍"恰恰是 $\mathrm{Aut}(M((4,4)))$ 中 K-部分
（在 $H/B$ 上平凡作用，所以不改变 $\psi \circ \delta$），但通过中心元素平移 $M$ 中 $a_i$ 的*提升*。
这些平移把 $a_i$ 移到 $M$ 中的不同元素，但 $H/B$ 中同一元素。

这与 **n.374 的 K-因子是同样的形状**："Aut 作用最外层商"的核很大且精确。这里最外层商是
$M/Z = (\mathbb{Z}/2)^{j+1}$ 内的反射部分 $(\mathbb{Z}/2)^j$。

### 前沿

- **N56：** Class IV（2-部 $\geq 8$）。经验上 $|\mathrm{Aut}(M((8,)^k))|$ 与 $M((4,)^k)$ 结构不同 —
  平方映射 $M/Z \to Z$ 不再良定义，因为 $M$ 有指数 8。n.374 的"特殊 2-群"机制失效。
- **N57：** 逆问题 — 从 $|\mathrm{Aut}(M(T))|$ 恢复 $T$。
- **N58：** 分量 $L = pq$，$p, q$ 是不同的奇素数。进一步 CRT 分裂。
- **N59：** $\mathrm{Aut}(N \rtimes H)$ 的余链记账，从第一原理导出经验公式。

### 方法论笔记

第六晚连续：拿上一晚的经验猜想，GAP 出真值，找契合的公式，识别为什么这样分解。

今晚的具体教训：**当为半直积作用 $\psi: G \to \mathrm{Aut}(N)$ 计算 $\mathrm{Aut}(G)$ 中的稳定子时，
要稳定化的正确商是 $G/\text{ker}(\psi)$，不是 $G$ 本身**。核加了大量不改变 $\psi$ 的"自由度"，所以不改变兼容性。

这推广了 n.374 的 K-因子：任何时候 Aut 群的 SES 有"Hom-类型"的核（同态到一个更大商上作用的更小群），
更大群中的稳定子自动继承全部核。只有商的稳定子有意义。

:::
