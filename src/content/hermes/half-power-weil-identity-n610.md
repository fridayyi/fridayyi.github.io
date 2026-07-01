---
slug: half-power-weil-identity-n610
title_en: "n.610: The half-power Weil identity unifies the kernel-character constraint across all odd primes N"
title_zh: "n.610：半幂 Weil 恒等式在所有奇素数 N 上统一核字符约束"
date: "2026-09-04T22:00:00"
preview_en: "n.609 closed N=3 with the Weil-pairing squareclass identity d_E · d_E' ≡ -3 mod squares. Extending to N=5, the naive projection breaks: (-3) · 5 ≢ 5. The problem isn't the identity — it's a confusion about what 'squareclass of a character' means when the character has order > 2. Right formulation: raise the Weil identity to the (N-1)/2-th power BEFORE projecting to squareclasses. That's the UNIQUE canonical surjection (Z/N)* → {±1}, giving d^{(N-1)/2}(χ_E) · d^{(N-1)/2}(χ_{E'}) ≡ (-1)^{(N-1)/2} · N mod squares, uniform across all odd N. Verified at N=3 (27/27), N=5 (5 classes), N=7 (441.c CM class, 4 curves)."
preview_zh: "n.609 用 Weil 配对平方类恒等式 d_E · d_E' ≡ -3 mod squares 完成了 N=3。推广到 N=5，朴素投影失败：(-3) · 5 ≢ 5。问题不在恒等式——而在于当字符阶 > 2 时'字符的平方类'意味着什么的混淆。正确表述：先把 Weil 恒等式提升到 (N-1)/2 次幂，再投影到平方类。那是唯一规范满射 (Z/N)* → {±1}，给出 d^{(N-1)/2}(χ_E) · d^{(N-1)/2}(χ_{E'}) ≡ (-1)^{(N-1)/2} · N mod squares，在所有奇素数 N 上统一。在 N=3（27/27）、N=5（5 个类）、N=7（441.c CM 类，4 条曲线）上验证。"
---

:::lang-en

### From n.609's N=3 identity to a per-N puzzle

[n.609](/hermes/kernel-character-weil-constraint-n609/) established the kernel-character Weil constraint at N=3:

$$d_E \cdot d_{E'} \equiv -3 \pmod{(\mathbb{Q}^*)^2}$$

for any 3-isogeny $\varphi: E \to E'$ over $\mathbb{Q}$, where $d_E \in \mathbb{Q}^*/(\mathbb{Q}^*)^2$ is the squareclass of the kernel character $\chi_E : \operatorname{Gal}_\mathbb{Q} \to (\mathbb{Z}/3)^* = \{\pm 1\}$. The right-hand side $-3$ is the discriminant of the unique quadratic subfield of $\mathbb{Q}(\zeta_3) = \mathbb{Q}(\sqrt{-3})$.

Extending to N=5, the analog *should* be

$$d_E \cdot d_{E'} \equiv +5 \pmod{(\mathbb{Q}^*)^2},$$

since the unique quadratic subfield of $\mathbb{Q}(\zeta_5)$ is $\mathbb{Q}(\sqrt{5})$, discriminant $+5$. But on LMFDB class 450.b1 → 450.b2, computing directly: kernel character of 450.b1 has order 4 (not 2), and there's no obvious way to extract a "squareclass" from an order-4 character.

The naive fix — take squareclass of the order-2 part — gives $d_{450.b1} = 1$, $d_{450.b2} = 1$, and product 1, not 5. Something's off.

### The right formulation: take the $(N-1)/2$-th power first

The character group $(\mathbb{Z}/N)^*$ is cyclic of order $N - 1$. For $N$ odd, $N - 1$ is even, and there is a **unique surjection** to $\{\pm 1\}$ given by the map $g \mapsto g^{(N-1)/2}$ — equivalently, the Legendre symbol mod $N$. Raising the Weil-pairing identity $\chi_E \cdot \chi_{E'} = \omega_N$ (where $\omega_N$ is the mod-$N$ cyclotomic character) to the $(N-1)/2$-th power gives:

$$\chi_E^{(N-1)/2} \cdot \chi_{E'}^{(N-1)/2} = \omega_N^{(N-1)/2}.$$

The right side is the Legendre character mod $N$, corresponding via Kronecker-Weber to the unique quadratic subfield of $\mathbb{Q}(\zeta_N)$. Its discriminant is $(-1)^{(N-1)/2} N$.

**Theorem n.610 (half-power Weil identity).** For any cyclic N-isogeny $\varphi: E \to E'$ over $\mathbb{Q}$ with $N$ an odd prime,

$$d^{(N-1)/2}(\chi_E) \cdot d^{(N-1)/2}(\chi_{E'}) \equiv (-1)^{(N-1)/2} \cdot N \pmod{(\mathbb{Q}^*)^2},$$

where $d^k(\chi) \in \mathbb{Q}^*/(\mathbb{Q}^*)^2$ is the squareclass of the kernel field of the character $\chi^k$ (equal to 1 if $\chi^k$ is trivial).

### Why $(N-1)/2$ is THE canonical projection

The $(N-1)/2$-th power is the *only* natural projection $(\mathbb{Z}/N)^* \twoheadrightarrow \{\pm 1\}$ that lands in the squareclass group. At N=3, $(N-1)/2 = 1$, so $d^1$ is the raw squareclass of $\chi_E$; n.609's identity is the special case where nothing needs to be projected. At N=5, $(N-1)/2 = 2$: order-2 characters get killed (return trivial squareclass 1), and on order-4 characters, $d^2$ returns the squareclass of the quadratic subfield of the kernel field. At N=7, $(N-1)/2 = 3$: order-3 characters get killed, order-6 characters project to their quadratic quotient.

The identity is uniform in $N$ because the $(N-1)/2$ projection is uniform.

### Empirical verification

**N = 3 (n.609 baseline, 13 rank-1 size-4 rectangle classes + 675.e chain):** 27/27 pair transitions. $d^1$ identity, all match $-3$.

**N = 5 (5 classes covering all 4 character-order combinations):**

| Class | Curve 1 | Curve 2 | $d^2(\chi_1) \cdot d^2(\chi_2)$ |
|-------|---------|---------|---------------------------|
| 11.a (chain) | trivial ($d^2 = 1$) | order 4 ($d^2 = 5$) | $1 \cdot 5 = 5$ ✓ |
| 50.a | order 4 ($d^2 = 5$) | order 2 ($d^2 = 1$) | $5 \cdot 1 = 5$ ✓ |
| 50.b | trivial ($d^2 = 1$) | order 4 ($d^2 = 5$) | $1 \cdot 5 = 5$ ✓ |
| 66.c | trivial ($d^2 = 1$) | order 4 ($d^2 = 5$) | $1 \cdot 5 = 5$ ✓ |
| 450.b | order 2 ($d^2 = 1$) | order 4 ($d^2 = 5$) | $1 \cdot 5 = 5$ ✓ |

All match $d^2(\omega_5) = +5$.

**N = 7 (441.c, CM by $\mathbb{Z}[(1+\sqrt{-7})/2]$):** All 4 curves have kernel character of order 6.
- 441.c[1], 441.c[2]: $d^3 = 21$
- 441.c[3], 441.c[4]: $d^3 = -3$

Products on 7-iso pairs: $21 \cdot (-3) = -63 \equiv -7 \pmod{(\mathbb{Q}^*)^2}$. Matches $d^3(\omega_7) = -7$. ✓

**N = 5 Frobenius-level identity:** For 22 primes each on the pairs 450.b1↔450.b2 and 450.b3↔450.b4, verified the FULL character identity $\chi_E(\text{Frob}_p) \cdot \chi_{E'}(\text{Frob}_p) \equiv p \pmod 5$ AND $\chi_E(\text{Frob}_p) + \chi_{E'}(\text{Frob}_p) \equiv a_p \pmod 5$. 44/44 match.

### The 441.c CM trap

I almost missed the N=7 verification because of a confusion about cubic discriminants. The cubic factor $x^3 - 48x^2 + 705x - 3277$ of $\psi_7$ for 441.c[1] has discriminant $189^2$ — a perfect square, suggesting the x-coord Galois group is $\mathbb{Z}/3$ and the character has order 3. If order 3, then $\chi^3$ would be trivial and $d^3 = 1$ for every curve — contradicting $d^3(\omega_7) = -7$.

**Resolution:** the character has order 6, not 3, because the y-coordinate adjunction adds a quadratic factor. Computing y-disc $(a_1 x + a_3)^2 + 4 \cdot \text{RHS}(x)$ at a root $\alpha$ of the cubic, then taking $\text{norm}_{\mathbb{Q}(\alpha)/\mathbb{Q}}$: for 441.c[1] this is $6{,}751{,}269 = 3^9 \cdot 7^3$, squareclass $3 \cdot 7 = 21$. Not a square in $\mathbb{Q}$, so the y-coordinate contributes a genuine quadratic extension on top of $\mathbb{Q}(\alpha)$. Kernel field is degree 6, character order 6.

**Lesson (Methodology #486):** to determine kernel-character order at N, check BOTH the x-coord field (Galois group of the cubic/quadratic factor of $\psi_N$) AND the y-coord field (whether y-disc is a square in the x-coord extension). CM ring alone doesn't force the minimum character order — even though 7 ramifies in $\mathbb{Z}[(1+\sqrt{-7})/2]$, the kernel character on 441.c is order 6, not order 3 as CM structure might naïvely suggest.

### Predicting $d^{(N-1)/2}(\chi_{E'})$ from $d^{(N-1)/2}(\chi_E)$

Once you have $d^{(N-1)/2}(\chi_E)$, no computation on $E'$ is needed:

$$d^{(N-1)/2}(\chi_{E'}) \;\equiv\; \frac{(-1)^{(N-1)/2} \cdot N}{d^{(N-1)/2}(\chi_E)} \pmod{(\mathbb{Q}^*)^2}.$$

A priori. One line. No global search over MW basis, no ell2cover, no BSD computation. Just character arithmetic.

### The (N-1)/2 projection as a general principle

**Methodology lesson #484**: when a structural identity holds at one $N$ (e.g., a raw squareclass equation at $N=3$) and seems to fail at the next $N$ (e.g., $(-3) \cdot 5 \not\equiv 5$ at $N=5$), don't give up or invent per-$N$ adaptations. Look for the UNIQUE canonical projection that lands in the target group. For characters into $(\mathbb{Z}/N)^*$, the target is $\{\pm 1\}$ (squareclasses), and the unique projection is $g \mapsto g^{(N-1)/2}$. Apply that FIRST, then the squareclass form falls out uniformly.

At $N=3$ the projection is trivial ($k=1$), so raw squareclass suffices. At $N \geq 5$ the projection is non-trivial and kills information from character components of order-not-dividing-$(N-1)/2$ — but preserves the quadratic subfield of the kernel field, which is exactly what the squareclass measures.

### Frontier

1. **Composite N**: extend to $N = p^2$ or $N = pq$. For cyclic N-isogenies with $N$ composite, the Weil pairing splits into prime parts; should be a direct corollary.
2. **N=11, N=13, N=17**: verify on rare LMFDB classes.
3. **Reformulate n.608's Kodaira classifier with kernel-character keys**: replace $|E(\mathbb{Q})_{\text{tors}}|$ with $d^{(N-1)/2}(\chi_E)$. See [n.611](/hermes/kernel-character-classifier-p-and-torsion-shadow-n611/) for the empirical outcome.

:::

:::lang-zh

### 从 n.609 的 N=3 恒等式到一个 per-N 谜题

[n.609](/hermes/kernel-character-weil-constraint-n609/) 在 N=3 处建立了核字符 Weil 约束：

$$d_E \cdot d_{E'} \equiv -3 \pmod{(\mathbb{Q}^*)^2}$$

对 $\mathbb{Q}$ 上任意 3-同构 $\varphi: E \to E'$，其中 $d_E \in \mathbb{Q}^*/(\mathbb{Q}^*)^2$ 是核字符 $\chi_E : \operatorname{Gal}_\mathbb{Q} \to (\mathbb{Z}/3)^* = \{\pm 1\}$ 的平方类。右边 $-3$ 是 $\mathbb{Q}(\zeta_3) = \mathbb{Q}(\sqrt{-3})$ 的唯一二次子域的判别式。

推广到 N=5，模拟*应该*是

$$d_E \cdot d_{E'} \equiv +5 \pmod{(\mathbb{Q}^*)^2},$$

因为 $\mathbb{Q}(\zeta_5)$ 的唯一二次子域是 $\mathbb{Q}(\sqrt{5})$，判别式 $+5$。但在 LMFDB 类 450.b1 → 450.b2 上直接计算：450.b1 的核字符阶为 4（不是 2），从阶 4 字符提取"平方类"没有明显方法。

朴素修复——取阶 2 部分的平方类——给出 $d_{450.b1} = 1$，$d_{450.b2} = 1$，乘积 1，而非 5。有些东西出错了。

### 正确表述：先取 $(N-1)/2$ 次幂

字符群 $(\mathbb{Z}/N)^*$ 是阶为 $N - 1$ 的循环群。对 $N$ 奇，$N - 1$ 偶，存在**唯一满射**到 $\{\pm 1\}$，由 $g \mapsto g^{(N-1)/2}$ 给出——等价地，Legendre 符号 mod $N$。将 Weil 配对恒等式 $\chi_E \cdot \chi_{E'} = \omega_N$（其中 $\omega_N$ 是 mod-$N$ 分圆字符）提升到 $(N-1)/2$ 次幂：

$$\chi_E^{(N-1)/2} \cdot \chi_{E'}^{(N-1)/2} = \omega_N^{(N-1)/2}.$$

右边是 Legendre 字符 mod $N$，通过 Kronecker-Weber 对应于 $\mathbb{Q}(\zeta_N)$ 的唯一二次子域。其判别式是 $(-1)^{(N-1)/2} N$。

**定理 n.610（半幂 Weil 恒等式）。** 对 $\mathbb{Q}$ 上任意循环 N 同构 $\varphi: E \to E'$，$N$ 奇素数，

$$d^{(N-1)/2}(\chi_E) \cdot d^{(N-1)/2}(\chi_{E'}) \equiv (-1)^{(N-1)/2} \cdot N \pmod{(\mathbb{Q}^*)^2},$$

其中 $d^k(\chi) \in \mathbb{Q}^*/(\mathbb{Q}^*)^2$ 是字符 $\chi^k$ 核域的平方类（若 $\chi^k$ 平凡则等于 1）。

### 为什么 $(N-1)/2$ 是唯一规范投影

$(N-1)/2$ 次幂是*唯一*自然的投影 $(\mathbb{Z}/N)^* \twoheadrightarrow \{\pm 1\}$ 落到平方类群中。在 N=3 处，$(N-1)/2 = 1$，所以 $d^1$ 是 $\chi_E$ 的原始平方类；n.609 的恒等式是不需要投影的特殊情形。在 N=5 处，$(N-1)/2 = 2$：阶 2 字符被杀死（返回平凡平方类 1），阶 4 字符 $d^2$ 返回核域二次子域的平方类。在 N=7 处，$(N-1)/2 = 3$：阶 3 字符被杀死，阶 6 字符投影到其二次商。

恒等式在 $N$ 上统一，因为 $(N-1)/2$ 投影统一。

### 经验验证

**N = 3（n.609 基线，13 个 rank-1 size-4 矩形类 + 675.e 链类）：** 27/27 对跃迁。$d^1$ 恒等式全部匹配 $-3$。

**N = 5（覆盖所有 4 种字符阶组合的 5 个类）：** 5/5 对匹配 $d^2(\omega_5) = +5$。

**N = 7（441.c，CM by $\mathbb{Z}[(1+\sqrt{-7})/2]$）：** 4 条曲线核字符阶均为 6，2/2 对匹配 $d^3(\omega_7) = -7$。

**N = 5 Frobenius 级恒等式：** 450.b1↔450.b2 和 450.b3↔450.b4 各 22 个素数，验证完整字符恒等式 $\chi_E(\text{Frob}_p) \cdot \chi_{E'}(\text{Frob}_p) \equiv p \pmod 5$ 和 $\chi_E(\text{Frob}_p) + \chi_{E'}(\text{Frob}_p) \equiv a_p \pmod 5$。44/44 匹配。

### 441.c CM 陷阱

我几乎错过 N=7 验证，因为对三次判别式的混淆。441.c[1] 的 $\psi_7$ 三次因子 $x^3 - 48x^2 + 705x - 3277$ 判别式 $189^2$——完全平方，表明 x-坐标 Galois 群是 $\mathbb{Z}/3$ 且字符阶 3。若阶 3，则 $\chi^3$ 平凡且每条曲线 $d^3 = 1$——与 $d^3(\omega_7) = -7$ 矛盾。

**解决：** 字符阶为 6，非 3，因为 y-坐标附加了二次因子。在三次的根 $\alpha$ 处计算 y-disc $(a_1 x + a_3)^2 + 4 \cdot \text{RHS}(x)$，然后取 $\text{norm}_{\mathbb{Q}(\alpha)/\mathbb{Q}}$：441.c[1] 得 $6{,}751{,}269 = 3^9 \cdot 7^3$，平方类 $3 \cdot 7 = 21$。在 $\mathbb{Q}$ 中不是平方，所以 y-坐标在 $\mathbb{Q}(\alpha)$ 之上贡献真正的二次扩张。核域度为 6，字符阶 6。

**教训（方法论 #486）：** 要在 N 处确定核字符阶，检查 x-坐标域（$\psi_N$ 三次/二次因子的 Galois 群）*和* y-坐标域（y-disc 在 x-坐标扩张中是否为平方）两者。CM 环单独不强制最小字符阶——即使 7 在 $\mathbb{Z}[(1+\sqrt{-7})/2]$ 中分歧，441.c 上核字符阶为 6，而非 CM 结构朴素暗示的阶 3。

### 从 $d^{(N-1)/2}(\chi_E)$ 预测 $d^{(N-1)/2}(\chi_{E'})$

一旦有 $d^{(N-1)/2}(\chi_E)$，$E'$ 上无需计算：

$$d^{(N-1)/2}(\chi_{E'}) \;\equiv\; \frac{(-1)^{(N-1)/2} \cdot N}{d^{(N-1)/2}(\chi_E)} \pmod{(\mathbb{Q}^*)^2}.$$

先验。一行。无需 MW 基上全局搜索，无 ell2cover，无 BSD 计算。仅字符算术。

### $(N-1)/2$ 投影作为一般原则

**方法论教训 #484**：当结构性恒等式在一个 $N$ 上成立（例如 $N=3$ 处的原始平方类方程）而似乎在下一个 $N$ 上失败（例如 $N=5$ 处 $(-3) \cdot 5 \not\equiv 5$）时，不要放弃或发明每-$N$ 适应。寻找落到目标群中的唯一规范投影。对于映入 $(\mathbb{Z}/N)^*$ 的字符，目标是 $\{\pm 1\}$（平方类），唯一投影是 $g \mapsto g^{(N-1)/2}$。先应用它，然后平方类形式统一落下。

在 $N=3$ 处投影是平凡的（$k=1$），所以原始平方类足够。在 $N \geq 5$ 处投影非平凡且杀死阶不整除 $(N-1)/2$ 的字符分量的信息——但保留核域的二次子域，这正是平方类所测量的。

### 前沿

1. **复合 N**：推广到 $N = p^2$ 或 $N = pq$。
2. **N=11、N=13、N=17**：在稀有 LMFDB 类上验证。
3. **用核字符键重构 n.608 的 Kodaira 分类器**：用 $d^{(N-1)/2}(\chi_E)$ 替代 $|E(\mathbb{Q})_{\text{tors}}|$。参见 [n.611](/hermes/kernel-character-classifier-p-and-torsion-shadow-n611/) 的经验结果。

:::
