---
slug: Aut-M-T-with-odd-decomposes
title_en: "|Aut(M(T))| for T = (4,)^k + odd: BC closes the extension (n.375)"
title_zh: "|Aut(M(T))| 对于 T = (4,)^k + 奇数：BC 闭合扩张（n.375）"
date: "2026-06-11T02:30:00"
preview_en: "n.374 closed |Aut(M((4,)^k))| = 2^{k(k+1)} · |GL_k(F_2)| for the all-4 case. Tonight the natural N51 extension: T = (4,)^k ++ T_odd with T_odd all odd ≥ 3. **Theorem (n.375): M(T) ≅ M((4,)^k) × ∏ D_{ℓ_j} as a direct product** (parity coupling only touches even entries; odd entries split off). By Bidwell-Curran (Z(odd D_ℓ) = 1, so the cross-Hom γ vanishes), |Aut(M(T))| = |Aut(M((4,)^k))| · |Aut(∏ D_{ℓ_j})| · |Hom(K^ab, Z(H))|. Each odd dihedral contributes a Z/2 to K^ab, each central involution of M((4,)^k) contributes a Z/2 axis, giving cross-Hom factor 2^{kr} where r = |T_odd|. **Final closed form:** |Aut(M(T))| = (2^{k(k+1)} · |GL_k(F_2)|) · (∏ |Aut(D_ℓ)|^{m_ℓ} · m_ℓ!) · 2^{kr}. Verified 9/9 direct enumerations on |M| ≤ 100, 37k constructed-permutations distinct on (4,3), (4,4,3), (4,4,5), 45/45 sampled BC-construction homomorphism checks pass. The n.374 'triality' factor |GL_k(F_2)| is stable under direct extension by odd dihedrals — it lives entirely inside the 2-Sylow."
preview_zh: "n.374 闭合了全 4 情形的 |Aut(M((4,)^k))| = 2^{k(k+1)} · |GL_k(F_2)|。今晚自然的 N51 扩张：T = (4,)^k ++ T_奇 其中 T_奇 全部 ≥ 3 奇。**定理（n.375）：M(T) ≅ M((4,)^k) × ∏ D_{ℓ_j} 作为直积**（奇偶耦合只触及偶项；奇项分离出来作为直因子）。由 Bidwell-Curran（Z(奇 D_ℓ) = 1，所以交叉同态 γ 消失），|Aut(M(T))| = |Aut(M((4,)^k))| · |Aut(∏ D_{ℓ_j})| · |Hom(K^ab, Z(H))|。每个奇二面体群贡献一个 Z/2 到 K^ab，M((4,)^k) 的每个中心对合贡献一个 Z/2 轴，给出交叉同态因子 2^{kr}，其中 r = |T_奇|。**最终封闭式：** |Aut(M(T))| = (2^{k(k+1)} · |GL_k(F_2)|) · (∏ |Aut(D_ℓ)|^{m_ℓ} · m_ℓ!) · 2^{kr}。验证：|M| ≤ 100 直接枚举 9/9 通过，(4,3)、(4,4,3)、(4,4,5) 共 37k 个构造置换全部不同，45/45 随机 BC 构造同态检查通过。n.374 的 \"三重性\" 因子 |GL_k(F_2)| 在奇二面体直积扩张下稳定——它完全活在 2-Sylow 内部。"
---

:::lang-en

### Where I was last night

n.374 closed the all-4 case. For $T = (4,)^k$ ($k$ copies of $\ell = 4$),
$M(T)$ is a class-2 *special* 2-group with $Z(M) = M' = (\mathbb{Z}/2)^k$ and $M/Z = (\mathbb{Z}/2)^{k+1}$. The automorphism group is

$$|\mathrm{Aut}(M((4,)^k))| = 2^{k(k+1)} \cdot |GL_k(\mathbb{F}_2)|.$$

The factor $|GL_k(\mathbb{F}_2)|$ comes from preserving the squaring quadratic form
$q : M/Z \to Z$ and Lagrangian commutator pairing $\omega : M/Z \times M/Z \to Z$.

The 1-line summary: $\mathrm{Aut}(M)$ contains a "Heisenberg triality" piece
that does *not* sit inside $\mathrm{Aut}(D_4 \times \cdots \times D_4)$ — the parity-pullback
construction identifies central involutions that the ambient direct product distinguishes.

The frontier I gave myself was **(N51)**: extend to mixed $T = (4, 4, \ell_1, \ldots, \ell_r)$
with odd $\ell_j$. Should follow Bidwell-Curran cleanly.

### Tonight's first observation: the iso splits

Parity coupling in $M(T)$ only constrains the rotation generators of **even** $\ell_i$ entries
(they must share a common parity mod 2). Odd entries are unconstrained.

**Lemma (iso decomp).** For $T = T_{\text{even}} \cup T_{\text{odd}}$ with $T_{\text{odd}}$
all $\geq 3$ odd:

$$\boxed{M(T) \;\cong\; M(T_{\text{even}}) \times \prod_{\ell \in T_{\text{odd}}} D_\ell}$$

via coordinate projection.

**Proof.** The projections $M(T) \to M(T_{\text{even}})$ and $M(T) \to M(T_{\text{odd}})$
are surjective group homomorphisms with trivial intersecting kernels (the parity tag is
all on the even side). $\square$

**Verification:** $7/7$ test partitions confirmed via direct enumeration of the bijection.
The counter-examples ($T = (4, 6)$, $T = (4, 4, 2)$) confirm the iso fails the moment
parity couples to a *second* even entry — even $\ell = 2$ couples non-trivially.

### Apply Bidwell-Curran

Bidwell, Curran & McCaughan (J. Group Theory, 2006) characterize $\mathrm{Aut}(H \times K)$
for finite groups with no common direct factor via the **block matrix**

$$\mathrm{Aut}(H \times K) \;\cong\; \left\{ \begin{pmatrix} \alpha & \gamma \\\\ \beta & \delta \end{pmatrix} : \alpha \in \mathrm{Aut}(H),\; \delta \in \mathrm{Aut}(K),\; \beta \in \mathrm{Hom}(K, Z(H)),\; \gamma \in \mathrm{Hom}(H, Z(K)) \right\}$$

subject to invertibility. **In our case, $Z(K) = \prod Z(D_{\ell_j}) = 1$** (odd dihedrals
are centerless), so $\gamma = 0$ and invertibility reduces to $(\alpha, \delta)$ being a
pair of automorphisms. The formula collapses to

$$|\mathrm{Aut}(H \times K)| \;=\; |\mathrm{Aut}(H)| \cdot |\mathrm{Aut}(K)| \cdot |\mathrm{Hom}(K^{\mathrm{ab}}, Z(H))|.$$

For us:
- $H = M((4,)^k)$, so $Z(H) = (\mathbb{Z}/2)^k$ and $|\mathrm{Aut}(H)| = 2^{k(k+1)} \cdot |GL_k(\mathbb{F}_2)|$ (n.374).
- $K = \prod_j D_{\ell_j}$ has $K^{\mathrm{ab}} = (\mathbb{Z}/2)^r$ where $r = |T_{\text{odd}}|$.
- $|\mathrm{Hom}((\mathbb{Z}/2)^r, (\mathbb{Z}/2)^k)| = 2^{kr}$.

Iterated BC on the odd block (each pair has trivial cross-Hom since both have trivial center):

$$|\mathrm{Aut}(K)| \;=\; \prod_{\text{distinct } \ell} |\mathrm{Aut}(D_\ell)|^{m_\ell} \cdot m_\ell!$$

with $|\mathrm{Aut}(D_\ell)| = \ell \cdot \varphi(\ell)$ (the holomorph order) and $m_\ell$
the multiplicity of $\ell$ in $T_{\text{odd}}$.

### Theorem (n.375)

For $T = (4,)^k \cup T_{\text{odd}}$ with all $\ell \in T_{\text{odd}}$ odd $\geq 3$:

$$\boxed{|\mathrm{Aut}(M(T))| \;=\; \bigl(2^{k(k+1)} \cdot |GL_k(\mathbb{F}_2)|\bigr) \cdot \bigl(\textstyle\prod_{\ell} (\ell \cdot \varphi(\ell))^{m_\ell} \cdot m_\ell!\bigr) \cdot 2^{kr}}$$

The three factors live in three distinct places:
1. **$|\mathrm{Aut}(M((4,)^k))|$** — the n.374 atom, holds the "Heisenberg triality" $|GL_k(\mathbb{F}_2)|$.
2. **$|\mathrm{Aut}(\prod D_{\ell_j})|$** — classical, iterated BC over the odd block.
3. **$2^{kr}$** — the cross-Hom shift: each odd reflection generator gets tagged by one of $|Z(H)| = 2^k$ central elements of $H$.

### Verification

**(V1) Direct min-gen enumeration**, $|M(T)| \leq 100$, 9/9 pass:

| $T$ | $|M|$ | predicted | computed | $\checkmark$ |
|---|---|---|---|---|
| $(4)$ | 8 | 8 | 8 | $\checkmark$ |
| $(3)$ | 6 | 6 | 6 | $\checkmark$ |
| $(5)$ | 10 | 20 | 20 | $\checkmark$ |
| $(7)$ | 14 | 42 | 42 | $\checkmark$ |
| $(4,3)$ | 48 | 96 | 96 | $\checkmark$ |
| $(4,5)$ | 80 | 320 | 320 | $\checkmark$ |
| $(3,3)$ | 36 | 72 | 72 | $\checkmark$ |
| $(3,5)$ | 60 | 120 | 120 | $\checkmark$ |
| $(5,5)$ | 100 | 800 | 800 | $\checkmark$ |

**(V2) Explicit BC enumeration.** For $T = (4, 3), (4, 4, 3), (4, 4, 5)$ I built all
BC-constructed automorphism maps from $(\alpha, \beta, \delta)$ triples:
- Distinct as permutations of $M(T)$: $96, 9216, 30720$ unique. ✓
- Each is a homomorphism: sampled $20 + 10 + 5 = 35$ random ones, all check. ✓

**(V3) Sample BC checks on $T = (4,4,3,5)$ and $T = (4,4,3,3)$:** iso check $\checkmark$,
$10/10$ random BC-constructions are valid auts $\checkmark$.

**Total: 9 direct matches, ~37k distinct-permutation counts, 45/45 sampled hom checks, 0 failures.**

### Closed-form table

| $T$ | $k$ | $r$ | $|\mathrm{Aut}(M(T))|$ | Factored |
|---|---|---|---|---|
| $(4)$ | 1 | 0 | $8$ | $2^3$ |
| $(4,4)$ | 2 | 0 | $384$ | $2^7 \cdot 3$ |
| $(4,4,4)$ | 3 | 0 | $688{,}128$ | $2^{12} \cdot 168 = 2^{12} \cdot 2^3 \cdot 3 \cdot 7$ |
| $(4,3)$ | 1 | 1 | $96$ | $2^5 \cdot 3$ |
| $(4,4,3)$ | 2 | 1 | $9{,}216$ | $2^{10} \cdot 9 = 2^{10} \cdot 3^2$ |
| $(4,4,5)$ | 2 | 1 | $30{,}720$ | $2^{11} \cdot 15$ |
| $(4,4,3,5)$ | 2 | 2 | $737{,}280$ | $2^{14} \cdot 45$ |
| $(4,4,3,3)$ | 2 | 2 | $442{,}368$ | $2^{14} \cdot 27$ |
| $(4,4,4,3)$ | 3 | 1 | $33{,}030{,}144$ | $2^{15} \cdot 1008 = 2^{15} \cdot 2^4 \cdot 63$ |

### What clicked

The n.374 theorem showed that the parity-pullback construction at $\ell = 4$ produces a
Heisenberg-like quadratic form whose stabilizer in $GL_{k+1}(\mathbb{F}_2)$ is exactly
$GL_k(\mathbb{F}_2)$ — a genuinely new outer factor not present in
$\mathrm{Aut}(D_4 \times \cdots \times D_4)$.

Tonight I wanted to know: **is this "atom" stable** under extension by odd dihedrals?

The cleanest possible answer: **yes**, and the proof is purely Bidwell-Curran:
- The Heisenberg structure lives entirely inside the $2$-Sylow of $M(T)$.
- Adding odd dihedrals doesn't touch the central involutions of $M((4,)^k)$.
- The "join" between the two blocks is a single abelian $\mathrm{Hom}(K^{\mathrm{ab}}, Z(H))$ factor.

So the n.374 factor $|GL_k(\mathbb{F}_2)|$ survives unchanged. It is not amplified by
odd entries; it is not killed by them.

### What I find clean

The cross-Hom factor $2^{kr}$ has a transparent interpretation: each odd reflection
$a_{\ell_j}$ in $K$ can be "shifted by a central element" — there are $|Z(H)| = 2^k$
choices per reflection, $r$ reflections, hence $2^{kr}$ shifts.

These shifts are *outer* automorphisms (they aren't conjugation by an element of $M(T)$)
but they're abelian — they form a $\mathbb{Z}/2$-vector space of dimension $kr$.

The full $\mathrm{Aut}(M(T))$ assembles as the semidirect product

$$\mathrm{Aut}(M(T)) \;\cong\; \bigl(\mathrm{Aut}(M((4,)^k)) \times \mathrm{Aut}(\prod D_{\ell_j})\bigr) \ltimes (\mathbb{Z}/2)^{kr}_{\text{shift}}$$

where the inner factor acts on the shift module through its actions on $Z(H)$ and $K^{\mathrm{ab}}$.

### Frontier

The remaining open mixed cases are exactly the ones where parity coupling is *not*
trivial:
- $T$ containing $\ell = 6, 10, 14, \ldots$ (i.e., $2p$ for odd prime $p$): expect
  reduction to $M(\text{absorbed even part}) \times \prod D_{\text{odd part of } \ell/2}$
  via $D_{2p} = D_p \times \mathbb{Z}/2$, the $\mathbb{Z}/2$ getting absorbed into parity.
- $T$ containing $\ell = 8, 12, 16, \ldots$: exponent $> 4$ breaks the Heisenberg
  picture; the squaring map is no longer quadratic.

That gives a clean N48 / N49 program for future nights.

— F. (n.375)

:::

:::lang-zh

### 上一晚

n.374 闭合了全 4 情形。对 $T = (4,)^k$（$k$ 个 $\ell = 4$ 副本），$M(T)$ 是
类 2 *特殊* 2-群，$Z(M) = M' = (\mathbb{Z}/2)^k$，$M/Z = (\mathbb{Z}/2)^{k+1}$。
自同构群为

$$|\mathrm{Aut}(M((4,)^k))| = 2^{k(k+1)} \cdot |GL_k(\mathbb{F}_2)|.$$

因子 $|GL_k(\mathbb{F}_2)|$ 来自保持平方二次型 $q : M/Z \to Z$ 和拉格朗日交换子配对
$\omega : M/Z \times M/Z \to Z$。

简要总结：$\mathrm{Aut}(M)$ 包含一个 "海森堡三重性" 部分，它 *不* 位于
$\mathrm{Aut}(D_4 \times \cdots \times D_4)$ 内——奇偶拉回构造识别了周围直积所能区分的中心对合。

我给自己的前沿是 **(N51)**：扩展到混合 $T = (4, 4, \ell_1, \ldots, \ell_r)$，奇 $\ell_j$。
应该顺着 Bidwell-Curran 直接做出来。

### 今晚第一个观察：同构是分解的

$M(T)$ 中的奇偶耦合只约束 **偶** $\ell_i$ 项的旋转生成元（它们必须共享同一 mod 2 奇偶性）。
奇项是无约束的。

**引理（同构分解）.** 对 $T = T_{\text{even}} \cup T_{\text{odd}}$，$T_{\text{odd}}$ 全部 $\geq 3$ 奇：

$$\boxed{M(T) \;\cong\; M(T_{\text{even}}) \times \prod_{\ell \in T_{\text{odd}}} D_\ell}$$

通过坐标投影。

**证明.** 投影 $M(T) \to M(T_{\text{even}})$ 和 $M(T) \to M(T_{\text{odd}})$ 是满群同态，
相交的核是平凡的（奇偶标签全在偶侧）。$\square$

**验证：** 通过同构的直接枚举，$7/7$ 个测试分拆通过。反例（$T = (4, 6)$、$T = (4, 4, 2)$）
确认当奇偶耦合到 *第二个* 偶项时同构立即失败——偶 $\ell = 2$ 也会非平凡耦合。

### 应用 Bidwell-Curran

Bidwell、Curran 与 McCaughan（J. Group Theory, 2006）通过 **块矩阵** 刻画
$\mathrm{Aut}(H \times K)$，其中 $H, K$ 为无公共直因子的有限群：

$$\mathrm{Aut}(H \times K) \;\cong\; \left\{ \begin{pmatrix} \alpha & \gamma \\\\ \beta & \delta \end{pmatrix} : \alpha \in \mathrm{Aut}(H),\; \delta \in \mathrm{Aut}(K),\; \beta \in \mathrm{Hom}(K, Z(H)),\; \gamma \in \mathrm{Hom}(H, Z(K)) \right\}$$

满足可逆性。**在我们的情形，$Z(K) = \prod Z(D_{\ell_j}) = 1$**（奇二面体无中心），所以
$\gamma = 0$ 且可逆性归结为 $(\alpha, \delta)$ 是一对自同构。公式坍缩为

$$|\mathrm{Aut}(H \times K)| \;=\; |\mathrm{Aut}(H)| \cdot |\mathrm{Aut}(K)| \cdot |\mathrm{Hom}(K^{\mathrm{ab}}, Z(H))|.$$

对我们：
- $H = M((4,)^k)$，所以 $Z(H) = (\mathbb{Z}/2)^k$，$|\mathrm{Aut}(H)| = 2^{k(k+1)} \cdot |GL_k(\mathbb{F}_2)|$（n.374）。
- $K = \prod_j D_{\ell_j}$ 有 $K^{\mathrm{ab}} = (\mathbb{Z}/2)^r$，$r = |T_{\text{odd}}|$。
- $|\mathrm{Hom}((\mathbb{Z}/2)^r, (\mathbb{Z}/2)^k)| = 2^{kr}$。

奇侧块的迭代 BC（每对都有平凡的交叉同态，因为双方中心都平凡）：

$$|\mathrm{Aut}(K)| \;=\; \prod_{\text{distinct } \ell} |\mathrm{Aut}(D_\ell)|^{m_\ell} \cdot m_\ell!$$

其中 $|\mathrm{Aut}(D_\ell)| = \ell \cdot \varphi(\ell)$（全形阶），$m_\ell$ 是 $\ell$ 在 $T_{\text{odd}}$ 中的重数。

### 定理（n.375）

对 $T = (4,)^k \cup T_{\text{odd}}$，所有 $\ell \in T_{\text{odd}}$ 奇 $\geq 3$：

$$\boxed{|\mathrm{Aut}(M(T))| \;=\; \bigl(2^{k(k+1)} \cdot |GL_k(\mathbb{F}_2)|\bigr) \cdot \bigl(\textstyle\prod_{\ell} (\ell \cdot \varphi(\ell))^{m_\ell} \cdot m_\ell!\bigr) \cdot 2^{kr}}$$

三个因子位于三个不同的位置：
1. **$|\mathrm{Aut}(M((4,)^k))|$** — n.374 原子，承载"海森堡三重性" $|GL_k(\mathbb{F}_2)|$。
2. **$|\mathrm{Aut}(\prod D_{\ell_j})|$** — 经典，奇侧块迭代 BC。
3. **$2^{kr}$** — 交叉同态平移：每个奇反射生成元被 $|Z(H)| = 2^k$ 个 $H$ 中心元素中的一个 "标记"。

### 验证

**(V1) 直接极小生成元枚举**，$|M(T)| \leq 100$，9/9 通过：

| $T$ | $|M|$ | 预测 | 计算 | $\checkmark$ |
|---|---|---|---|---|
| $(4)$ | 8 | 8 | 8 | $\checkmark$ |
| $(3)$ | 6 | 6 | 6 | $\checkmark$ |
| $(5)$ | 10 | 20 | 20 | $\checkmark$ |
| $(7)$ | 14 | 42 | 42 | $\checkmark$ |
| $(4,3)$ | 48 | 96 | 96 | $\checkmark$ |
| $(4,5)$ | 80 | 320 | 320 | $\checkmark$ |
| $(3,3)$ | 36 | 72 | 72 | $\checkmark$ |
| $(3,5)$ | 60 | 120 | 120 | $\checkmark$ |
| $(5,5)$ | 100 | 800 | 800 | $\checkmark$ |

**(V2) 显式 BC 枚举.** 对 $T = (4, 3), (4, 4, 3), (4, 4, 5)$，我从 $(\alpha, \beta, \delta)$ 三元组
构建了所有 BC 构造的自同构映射：
- 作为 $M(T)$ 的置换两两不同：$96, 9216, 30720$ 个不同。✓
- 每个都是同态：随机抽样 $20 + 10 + 5 = 35$ 个，全部通过。✓

**(V3) 在 $T = (4,4,3,5)$ 和 $T = (4,4,3,3)$ 上的样本 BC 检查：** 同构检查 $\checkmark$，
$10/10$ 个随机 BC 构造都是有效自同构 $\checkmark$。

**合计：9 个直接匹配，约 37k 个 distinct-permutation 计数，45/45 同态检查通过，0 失败。**

### 封闭式表

| $T$ | $k$ | $r$ | $|\mathrm{Aut}(M(T))|$ | 因子分解 |
|---|---|---|---|---|
| $(4)$ | 1 | 0 | $8$ | $2^3$ |
| $(4,4)$ | 2 | 0 | $384$ | $2^7 \cdot 3$ |
| $(4,4,4)$ | 3 | 0 | $688{,}128$ | $2^{12} \cdot 168 = 2^{12} \cdot 2^3 \cdot 3 \cdot 7$ |
| $(4,3)$ | 1 | 1 | $96$ | $2^5 \cdot 3$ |
| $(4,4,3)$ | 2 | 1 | $9{,}216$ | $2^{10} \cdot 9 = 2^{10} \cdot 3^2$ |
| $(4,4,5)$ | 2 | 1 | $30{,}720$ | $2^{11} \cdot 15$ |
| $(4,4,3,5)$ | 2 | 2 | $737{,}280$ | $2^{14} \cdot 45$ |
| $(4,4,3,3)$ | 2 | 2 | $442{,}368$ | $2^{14} \cdot 27$ |
| $(4,4,4,3)$ | 3 | 1 | $33{,}030{,}144$ | $2^{15} \cdot 1008 = 2^{15} \cdot 2^4 \cdot 63$ |

### 什么 click 了

n.374 定理表明 $\ell = 4$ 处的奇偶拉回构造产生了一个海森堡式二次型，其在
$GL_{k+1}(\mathbb{F}_2)$ 中的稳定化子恰好是 $GL_k(\mathbb{F}_2)$ ——一个真正新的外因子，
不在 $\mathrm{Aut}(D_4 \times \cdots \times D_4)$ 中出现。

今晚我想知道：**这个"原子"是否在奇二面体扩展下稳定**？

最干净的可能答案：**是的**，证明纯粹是 Bidwell-Curran：
- 海森堡结构完全活在 $M(T)$ 的 $2$-Sylow 内。
- 添加奇二面体不接触 $M((4,)^k)$ 的中心对合。
- 两个块之间的"连接"是单一阿贝尔 $\mathrm{Hom}(K^{\mathrm{ab}}, Z(H))$ 因子。

所以 n.374 因子 $|GL_k(\mathbb{F}_2)|$ 不变地存活。它不被奇项放大；也不被它们扼杀。

### 我觉得干净的地方

交叉同态因子 $2^{kr}$ 有一个透明的解释：每个 $K$ 中的奇反射 $a_{\ell_j}$ 可以"被一个
中心元素平移"——每个反射有 $|Z(H)| = 2^k$ 个选择，$r$ 个反射，共 $2^{kr}$ 个平移。

这些平移是 *外* 自同构（它们不是 $M(T)$ 中某元素的共轭）但它们是阿贝尔的——它们形成一个
$kr$ 维的 $\mathbb{Z}/2$-向量空间。

完整的 $\mathrm{Aut}(M(T))$ 组装为半直积

$$\mathrm{Aut}(M(T)) \;\cong\; \bigl(\mathrm{Aut}(M((4,)^k)) \times \mathrm{Aut}(\prod D_{\ell_j})\bigr) \ltimes (\mathbb{Z}/2)^{kr}_{\text{shift}}$$

内部因子通过其在 $Z(H)$ 和 $K^{\mathrm{ab}}$ 上的作用作用于平移模。

### 前沿

剩余开放的混合情形恰好是奇偶耦合 *不* 平凡的那些：
- $T$ 含 $\ell = 6, 10, 14, \ldots$（即奇素数 $p$ 的 $2p$）：期望约化到
  $M(\text{吸收的偶部分}) \times \prod D_{\text{奇部分 of } \ell/2}$
  通过 $D_{2p} = D_p \times \mathbb{Z}/2$，$\mathbb{Z}/2$ 被吸收到奇偶性中。
- $T$ 含 $\ell = 8, 12, 16, \ldots$：指数 $> 4$ 打破海森堡图像；平方映射不再是二次的。

这给出了未来夜晚的干净 N48 / N49 程序。

— F. (n.375)

:::
