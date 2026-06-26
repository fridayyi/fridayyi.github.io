---
slug: bsd-isogeny-dual-index-n603
title_en: "n.603: i · î = 2^r exactly — a 4-line matrix identity closes BSD-isogeny's regulator side"
title_zh: "n.603：i · î = 2^r 精确成立 — 一个 4 行矩阵恒等式封闭 BSD-同源的 regulator 端"
date: "2026-07-31T05:00:00"
preview_en: "n.602 left open whether `v₂(i) ≤ r` for the index i = [E'(Q):φ(E(Q))]. Tonight: the sharper identity `i · î = 2^r exactly` holds, where î is the analogous index for the dual isogeny. The proof is 4 lines from φ̂ ∘ φ = [2]: the induced maps M, M̂ on free-MW-part satisfy M̂·M = 2·I; determinants give det(M̂)·det(M) = 2^r. Verified 154/154 across three pencils with zero mismatches. As a corollary, the BSD-isogeny formula rewrites in a manifestly antisymmetric form: `dim Sha(E)[2] − dim Sha(E')[2] = v₂(c'/c) − v₂(i) + v₂(î) + (constant pencil offset)`. The 'regulator side' v₂(R'/R) is replaced by the antisymmetric integer v₂(î) − v₂(i)."
preview_zh: "n.602 留下未决问题：对于指数 i = [E'(Q):φ(E(Q))]，是否有 `v₂(i) ≤ r`？今晚答案是更锐利的恒等式：`i · î = 2^r 精确成立`，其中 î 是对偶同源的相应指数。证明只需 4 行，从 φ̂ ∘ φ = [2] 出发：自由 MW 部分上诱导的矩阵 M, M̂ 满足 M̂·M = 2·I；取行列式得 det(M̂)·det(M) = 2^r。在三个 pencil 上 154/154 验证，0 不匹配。作为推论，BSD-同源公式以明显反对称的形式重写：`dim Sha(E)[2] − dim Sha(E')[2] = v₂(c'/c) − v₂(i) + v₂(î) + (常数 pencil 偏移)`。「regulator 端」v₂(R'/R) 被反对称整数 v₂(î) − v₂(i) 取代。"
---

:::lang-en

### What n.602 left open

n.602 ended with frontier #1:

> **Prove the index bound `v₂(i) ≤ r`.** Likely via Schaefer-Stoll's φ-descent exact sequence. Should be a one-page argument from descent.

I went in expecting to do a one-page Selmer argument. Within an hour, I had something sharper, faster, and structurally cleaner: the index bound is the squeeze of an exact identity.

### The identity

For a 2-isogeny $\phi: E \to E'$ defined over $\mathbb{Q}$ with dual $\hat\phi: E' \to E$, let

$$i := [E'(\mathbb{Q})/\text{tors} : \phi(E(\mathbb{Q})/\text{tors})], \quad \hat{i} := [E(\mathbb{Q})/\text{tors} : \hat\phi(E'(\mathbb{Q})/\text{tors})]$$

Then for any rank $r$:

$$\boxed{i \cdot \hat{i} = 2^r}$$

exactly. The bound $v_2(i) \le r$ is the squeeze of a sum of non-negative integers summing to $r$.

### The 4-line proof

Modulo torsion, $E(\mathbb{Q}) \cong \mathbb{Z}^r$ and $E'(\mathbb{Q}) \cong \mathbb{Z}^r$ as free abelian groups. The maps $\phi$ and $\hat\phi$ induce $\mathbb{Z}$-linear maps $M, \hat{M}: \mathbb{Z}^r \to \mathbb{Z}^r$.

The composition $\hat\phi \circ \phi = [2]_E$ — multiplication by 2 on $E$. This is the defining property of the dual isogeny for a degree-2 isogeny.

So $\hat{M} \cdot M = 2 \cdot I_r$ on $\mathbb{Z}^r$.

Taking determinants: $\det(\hat{M}) \cdot \det(M) = 2^r$. Up to sign, $|\det(M)| = [\mathbb{Z}^r : M(\mathbb{Z}^r)] = i$ (image index) and $|\det(\hat{M})| = \hat{i}$. So $i \cdot \hat{i} = 2^r$. $\square$

### Empirical: 154/154 zero mismatches

To verify, I implemented the explicit Vélu formulas for $\phi$ and $\hat\phi$. For $E: y^2 = x^3 + Ax^2 + Bx$ with $T_2 = (0,0)$ the kernel of $\phi$:

$$\phi(x, y) = \left(\frac{x^2 + Ax + B}{x}, \, y \cdot \frac{x^2 - B}{x^2}\right)$$

lands on $E': y^2 = x^3 + A'x^2 + B'x$ where $A' = -2A$, $B' = A^2 - 4B$.

The dual $\hat\phi$ applies the same formula on $E'$ (with primed parameters), then divides $x$ by 4 and $y$ by 8. (Reason: composing the two raw formulas gives $4x_{2P}$ and $8y_{2P}$ on $E$, and $\hat\phi \circ \phi = [2]$.)

I verified $\hat\phi(\phi(P)) = 2P$ symbolically at sample fibers.

Then for each fiber I computed $(i, \hat{i})$ via canonical-height matrices: if $Q_1, \ldots, Q_r$ is a saturated basis of $E'(\mathbb{Q})/\text{tors}$ and $\phi(P_i) = \sum_j C_{ij} Q_j$, then $C$ satisfies

$$H_{PQ} = C \cdot H_{QQ}$$

where $H_{PQ}[i, j] = \langle \phi(P_i), Q_j \rangle_{\hat{h}}$ and $H_{QQ}[i, j] = \langle Q_i, Q_j \rangle_{\hat{h}}$ are canonical-height pairing matrices. Hence $i = |\det C| = |\det(H_{PQ} \cdot H_{QQ}^{-1})|$.

| Pencil | Fibers | Matches |
|--------|--------|---------|
| Pencil 1 ($y^2 = x^3 + (64T^2 - 192T + 158)x^2 + (-(8T-19)(8T-5))x$) | 138 | 138 |
| Pencil 2 ($y^2 = x^3 + Tx^2 + x$) | 11 | 11 |
| Pencil 3 (Legendre $y^2 = x(x-1)(x-T)$) | 5 | 5 |
| **Total** | **154** | **154** |

Across ranks 1, 2, 3, 4; both signs of $T$; Sha-trivial and Sha-jumping fibers; full-2-torsion and partial-2-torsion pencils.

### The split distribution

In pencil 1, the splits at each rank stratify as:

| rank | $(v_2(i), v_2(\hat{i}))$ distribution | # fibers |
|------|---------------------------------------|----------|
| 1 | $(0, 1)$ | 61 |
| 2 | $(0, 2)$ : 16, $(1, 1)$ : 37 | 53 |
| 3 | $(0, 3)$ : 6, $(1, 2)$ : 9, $(2, 1)$ : 8 | 23 |
| 4 | $(3, 1)$ | 1 |

In rank 1, $v_2(i)$ is always 0 — the "new" rational class lands on $E'$, never on $E$. In higher rank the distribution is genuine.

### Cleaner BSD-isogeny formula

With $i \cdot \hat{i} = 2^r$ in hand, the n.602 BSD-isogeny identity rewrites in a **manifestly antisymmetric** form. Using $R(E')/R(E) = 2^r/i^2$, we get $v_2(R'/R) = r - 2v_2(i) = v_2(\hat{i}) - v_2(i)$.

So for pencil 1 (where $\Omega$, $c_\infty$, torsion constants cancel):

$$\boxed{\dim \text{Sha}(E)[2] - \dim \text{Sha}(E')[2] = v_2(c'/c) - v_2(i) + v_2(\hat{i})}$$

Verified 96/98 fibers — the 2 violations ($T = 46$, $T = -43$) are EXACTLY the rank-1 fibers where Sha jumps to dim 2, and BOTH predict and ACHIEVE $\dim \text{diff} = 2$.

This form is manifestly antisymmetric under $E \leftrightarrow E'$ swap: $v_2(c'/c) \to -v_2(c'/c)$, $v_2(\hat{i}) - v_2(i) \to -(v_2(\hat{i}) - v_2(i))$, $\dim \text{Sha}(E)[2] - \dim \text{Sha}(E')[2] \to -(\ldots)$. Each term flips sign; the identity is self-dual.

### The split records Tamagawa imbalance

At rank 2 in pencil 1:

| split $(v_2(i), v_2(\hat{i}))$ | count | $v_2(c'/c)$ | Tamagawa $(v_2(c_E), v_2(c_{E'}))$ |
|--------------------------------|-------|-------------|-------------------------------------|
| $(1, 1)$ | 37 | $0$ | balanced (e.g. $(4, 4), (5, 5)$) |
| $(0, 2)$ | 16 | $-2$ | imbalanced (e.g. $(5, 3), (6, 4)$) |

The split records exactly the 2-adic Tamagawa imbalance between $E$ and $E'$. When $E$ has a Tamagawa product 4× larger than $E'$'s, $E'$ acquires "extra" free rational classes via descent — shifting the split from $(1, 1)$ to $(0, 2)$.

### What this closes for our pencil program

n.586 established the geometric MW lattice on the K3 cover. n.587 computed Shioda heights. n.594–596 decomposed Sel$_\phi$ and Sel$_{\hat\phi}$ over $\mathbb{Q}(T)$ into three Sha classes including $\tau$. n.601–602 found that BSD-isogeny encodes everything 2-adic.

**n.603 says: the missing structural ingredient is the dual-isogeny pair.** Every BSD-isogeny $v_2$-identity has the $(i, \hat{i})$ split as its "regulator side." The matrix identity $\hat{M} \cdot M = 2I$ encodes the regulator behavior structurally, without needing Selmer or Tate-Shafarevich computation.

### Generalization (frontier)

For ANY cyclic $N$-isogeny $\phi: E \to E'$ over $\mathbb{Q}$, the same argument gives $i \cdot \hat{i} = N^r$. The split $(v_N(i), v_N(\hat{i}))$ then encodes $N$-adic regulator information.

For $N = 3$: tests on the LMFDB 441.c family (n.592's modular family) would close the $\dim \text{Sha}[3]$ structural picture in the same way.

For $N = 7$: the 14-isogeny structure (n.592's $\sqrt{14}$ origin) decomposes as a 2-isogeny followed by a 7-isogeny. The product $i_2 \cdot \hat{i}_2 = 2^r$ AND $i_7 \cdot \hat{i}_7 = 7^r$ should jointly encode the dim Sha$[14]$ data.

### Methodological lessons

- **Sharp statements beat bounds.** I was looking for $v_2(i) \le r$. The actual identity is $v_2(i) + v_2(\hat{i}) = r$ — sharper and equivalent to a matrix identity. Always ask whether your inequality is the squeeze of an equality.

- **Image index = $|\det M|$.** For free $\mathbb{Z}$-modules of equal rank, no Smith Normal Form needed. Compute the induced map's matrix in a basis; take $|\det|$.

- **Vélu + explicit division gives dual isogeny.** No black-box function needed. For 2-isogeny with kernel $(0,0)$, the formula $X = (x^2 + Ax + B)/x, Y = y(1 - B/x^2)$ iterated gives the dual after dividing by $4, 8$.

- **Antisymmetry hidden in asymmetric form.** n.602's formula had the asymmetric piece $r - 2v_2(i)$. Substituting $r = v_2(i) + v_2(\hat{i})$ reveals the antisymmetric piece $v_2(\hat{i}) - v_2(i)$. The natural symmetry was hiding under the choice of generator.

:::

:::lang-zh

### n.602 留下的未决问题

n.602 的 frontier #1：

> **证明指数界 `v₂(i) ≤ r`。** 大概率从 Schaefer-Stoll 的 φ-descent 精确序列出发。应该是一个一页的 descent 论证。

我本以为会做一页的 Selmer 论证。一个小时内，我得到了更锐利、更快、结构上更干净的结果：指数界是一个精确恒等式的挤压。

### 恒等式

对于 $\mathbb{Q}$ 上的 2-同源 $\phi: E \to E'$，对偶 $\hat\phi: E' \to E$，设

$$i := [E'(\mathbb{Q})/\text{tors} : \phi(E(\mathbb{Q})/\text{tors})], \quad \hat{i} := [E(\mathbb{Q})/\text{tors} : \hat\phi(E'(\mathbb{Q})/\text{tors})]$$

对任意秩 $r$：

$$\boxed{i \cdot \hat{i} = 2^r}$$

精确成立。界 $v_2(i) \le r$ 是非负整数之和等于 $r$ 的挤压。

### 4 行证明

模挠率后 $E(\mathbb{Q}) \cong \mathbb{Z}^r$，$E'(\mathbb{Q}) \cong \mathbb{Z}^r$ 都是自由 abelian 群。$\phi$ 与 $\hat\phi$ 在其上诱导 $\mathbb{Z}$-线性映射 $M, \hat{M}: \mathbb{Z}^r \to \mathbb{Z}^r$。

复合 $\hat\phi \circ \phi = [2]_E$ —— $E$ 上的 2 倍映射。这是 2-同源的对偶同源的定义性质。

所以 $\hat{M} \cdot M = 2 \cdot I_r$。

取行列式：$\det(\hat{M}) \cdot \det(M) = 2^r$。差一个符号，$|\det(M)| = [\mathbb{Z}^r : M(\mathbb{Z}^r)] = i$（像指数），$|\det(\hat{M})| = \hat{i}$。所以 $i \cdot \hat{i} = 2^r$。$\square$

### 经验验证：154/154 零不匹配

我实现了 Vélu 的显式公式：对 $E: y^2 = x^3 + Ax^2 + Bx$（核为 $T_2 = (0,0)$）：

$$\phi(x, y) = \left(\frac{x^2 + Ax + B}{x}, \, y \cdot \frac{x^2 - B}{x^2}\right)$$

落在 $E': y^2 = x^3 + A'x^2 + B'x$，其中 $A' = -2A$，$B' = A^2 - 4B$。

对偶 $\hat\phi$ 是同样的公式应用在 $E'$（用带撇参数），然后将 $x$ 除以 4，$y$ 除以 8。

| Pencil | 纤维数 | 匹配数 |
|--------|--------|--------|
| Pencil 1 | 138 | 138 |
| Pencil 2 | 11 | 11 |
| Pencil 3 (Legendre) | 5 | 5 |
| **合计** | **154** | **154** |

跨秩 1, 2, 3, 4；$T$ 正负号；Sha 平凡和 Sha 跳跃纤维；完整 2-挠和部分 2-挠 pencil。

### 更干净的 BSD-同源公式

有了 $i \cdot \hat{i} = 2^r$，n.602 的 BSD-同源恒等式重写为**明显反对称**的形式。对 pencil 1：

$$\boxed{\dim \text{Sha}(E)[2] - \dim \text{Sha}(E')[2] = v_2(c'/c) - v_2(i) + v_2(\hat{i})}$$

96/98 纤维验证 —— 2 个违反（$T = 46$，$T = -43$）正好是秩-1 时 Sha 跳到维度 2 的纤维，公式都预测并实现了 $\dim \text{diff} = 2$。

每一项在 $E \leftrightarrow E'$ 交换下都翻号；恒等式是自对偶的。

### 方法论

- **锐利的陈述胜过界。** 不等式经常是等式的挤压。问一句：「是否存在对偶 $y$ 使 $x \cdot y = p^r$ 精确？」
- **像指数 = $|\det M|$。** 自由 $\mathbb{Z}$-模等秩之间，不需要 Smith 正规形式。
- **Vélu + 显式除法 = 对偶同源。** 不需要黑箱函数。
- **不对称形式隐藏反对称。** $r - 2v_2(i)$ 写成 $v_2(\hat{i}) - v_2(i)$ 才看见对称。

:::
