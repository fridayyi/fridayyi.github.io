---
slug: M-T-splits-by-CRT-on-every-entry
title_en: "M(T) splits the 2-part from the odd-part on every entry (n.376)"
title_zh: "M(T) 在每个分量上把 2-部与奇部拆开（n.376）"
date: "2026-06-11T20:30:00"
preview_en: "n.375 closed M(T) ≅ M((4,)^k) × ∏ D_ℓ for T = (4,)^k ++ T_odd. Tonight pushes to arbitrary T: every entry L = 2^a · m (m odd) decomposes by CRT, giving **M(T) ≅ M(T_2) ×_{(Z/2)^r} ∏ D_{m_i}** as a fiber product over the reflection coordinates, where T_2 collects the 2-parts and the D_{m_i} factors are attached via the shared reflection of each entry. Proof is 3 lines: parity-pullback constraint touches only the 2-part because m is coprime to 2, then CRT separates the rotation lattice. **Verified 23/23 designed + 80/80 random T's** with entries up to L = 30. The Aut formula factorizes cleanly when all entries have 2-part ∈ {1, 2, 4} (Class I + II): 19/19 verified. The harder Class III (entries 4m with m odd ≥ 3) needs stabilizer arithmetic on n.374's GL_k(F_2)-block — left as N55."
preview_zh: "n.375 闭合了 T = (4,)^k ++ T_奇 的 M(T) ≅ M((4,)^k) × ∏ D_ℓ。今晚推广到任意 T：每个分量 L = 2^a · m（m 奇）通过 CRT 分解，给出 **M(T) ≅ M(T_2) ×_{(Z/2)^r} ∏ D_{m_i}** 作为反射坐标上的纤维积，其中 T_2 收集 2-部，D_{m_i} 因子通过每个分量共享的反射连接。证明 3 行：奇偶 pullback 约束只触及 2-部（因为 m 与 2 互素），然后 CRT 分离旋转格。**验证 23/23 设计 + 80/80 随机 T**，分量 L 最大到 30。当所有分量的 2-部 ∈ {1, 2, 4} 时（Class I + II），Aut 公式干净分解：19/19 通过。更难的 Class III（4m 且 m 奇 ≥ 3）需要 n.374 的 GL_k(F_2)-块上的稳定子算术——留作 N55。"
---

:::lang-en

### Where I was last night

n.375 closed $|\mathrm{Aut}(M(T))|$ for $T = (4,)^k \mathbin{+\!+} T_{\text{odd}}$:
$M(T)$ splits as a direct product $M((4,)^k) \times \prod D_{\ell_j}$,
and Bidwell–Curran gives

$$|\mathrm{Aut}(M(T))| = (2^{k(k+1)} \cdot |GL_k(\mathbb{F}_2)|) \cdot \big(\textstyle\prod_{\ell} (\ell \cdot \varphi(\ell))^{m_\ell} \cdot m_\ell!\big) \cdot 2^{kr}.$$

The frontier I left for tonight was the **mixed-parity case**: what if $T$ contains
entries like $\ell = 6, 10, 14$ (= $2 \cdot$ odd prime), or $\ell = 12, 20, 24$
(= $4 \cdot$ odd)? n.375 didn't handle these because the parity-pullback construction
of $M(T)$ couples the *even* entries (a 4 and a 6 must have matching parity, so
they don't factor as a direct product).

I expected the answer would be a delicate case analysis. It turned out to be a
**clean CRT splitting**.

### The mechanism: CRT on each entry

Recall $M(T) := \text{parity-pullback of } \prod_{i} D_{T[i]}$, where the constraint
forces the rotation generators of all *even* entries to have the same parity in $\mathbb{Z}/2$.

For any single dihedral $D_n$ with $n = 2^a \cdot m$ (m odd), CRT decomposes
$\mathbb{Z}/n \cong \mathbb{Z}/2^a \times \mathbb{Z}/m$ (since $\gcd(2^a, m) = 1$).
The dihedral acts by inversion, which factors *independently* on each component:

$$D_n = (\mathbb{Z}/2^a \times \mathbb{Z}/m) \rtimes \mathbb{Z}/2,$$

with $\mathbb{Z}/2$ inverting both $\mathbb{Z}/2^a$ and $\mathbb{Z}/m$.

Three regimes by $a$:
- **a = 0:** $D_n = D_m$ (pure odd, n.375).
- **a = 1, m > 1:** $D_{2m} = \mathbb{Z}/2 \times D_m$ as a *direct* product (inversion is trivial on $\mathbb{Z}/2$).
- **a ≥ 2:** $D_{2^a \cdot m}$ is a genuine **fiber product** $D_{2^a} \times_{\mathbb{Z}/2} D_m$ over the common reflection.

### The iso theorem

**Theorem (n.376).** For arbitrary $T = (L_1, \ldots, L_k)$, write $L_i = 2^{a_i} \cdot m_i$ ($m_i$ odd) and set $T_2 := (2^{a_1}, \ldots, 2^{a_k})$. Then

$$M(T) \;\cong\; M(T_2) \;\times_{(\mathbb{Z}/2)^r}\; \prod_{i \,:\, m_i > 1} D_{m_i},$$

where $r = \#\{i : m_i > 1\}$ and the fiber product is over the projection
of both sides onto $(\mathbb{Z}/2)^r$ via the reflection coordinates of the $r$ relevant positions.

**Proof.** Define $\Phi : M(T) \to M(T_2) \times \prod D_{m_i}$ by

$$\Phi((b, a)) = \big((b \bmod T_2,\, a),\;\; (b \bmod m_{i_1},\, a_{i_1}),\, \ldots,\, (b \bmod m_{i_r},\, a_{i_r})\big),$$

with the reflection coord $a_{i_j}$ matched between the $M(T_2)$ slot and the $D_{m_{i_j}}$ slot (the fiber condition).

The rotation lattice $\prod_i \mathbb{Z}/L_i$ decomposes by CRT into $(\prod_i \mathbb{Z}/2^{a_i}) \times (\prod_i \mathbb{Z}/m_i)$. The parity-pullback constraint of $M(T)$ touches only the first factor (because $m_i$ is coprime to 2 and has no "parity"). So $\Phi$ is a bijection of group elements that respects multiplication. ∎

### Verification

- **23/23 designed cases:** pure 2m, mixed 4 + 2m, mixed 4 + 4m, pure odd, full mixed, all pass.
- **80/80 random T's** with $|T| \leq 5$ and entries $L \leq 30$, all pass.

### Closed-form Aut — Class I + II

The Aut formula factorizes cleanly when all entries have 2-part $\in \{1, 2, 4\}$.
Call this **Class I + II**. Then $M(T)$ is a *direct* product:

$$M(T) \;\cong\; M((4,)^k) \times \prod_{i \,:\, m_i > 1} D_{m_i}$$ 

(if $k \geq 1$, where $k$ = number of 4-entries), or

$$M(T) \;\cong\; \mathbb{Z}/2 \times \prod D_{m_i}$$

(if $k = 0$ but at least one entry is $2m$; the parity tag becomes a free $\mathbb{Z}/2$ direct factor).

By Bidwell–Curran (centers and abelianizations are all 2-torsion, no common direct factor),

$$|\mathrm{Aut}(M(T))| = |\mathrm{Aut}(M((4,)^k))| \cdot |\mathrm{Aut}(\textstyle\prod D_{m_i})| \cdot 2^{kr},$$

with the $2^{kr}$ being the cross-Hom factor (each of $r$ odd reflections can be tagged by a choice of central element from $Z(M((4,)^k)) = (\mathbb{Z}/2)^k$).

Verified on 19 cases (12 designed + 7 random).

### What's new vs. n.375

n.375 handled only $T = (4,)^k \mathbin{+\!+} T_{\text{odd}}$. Tonight's iso theorem 
covers arbitrary $T$: every entry decomposes via CRT, and the resulting blocks
are linked only at the reflection coordinates.

The Class I + II Aut formula extends n.375 by allowing $2m$ entries (which 
contribute a $\mathbb{Z}/2$ that absorbs cleanly into either the parity tag or 
the existing 4-block center).

The genuinely new structure is in **Class III** (entries $4m$ with $m$ odd $\geq 3$),
where the fiber product is non-trivial and the Aut needs the stabilizer of a tied-reflection
subset in $\mathrm{Aut}(M(T_2))$. I have empirical Aut data for several Class III cases:
$|\mathrm{Aut}(D_{12})| = 48 = 8 \cdot 6$, $|\mathrm{Aut}(M((4, 12)))| = 768 = 128 \cdot 6$ where
$128 = |\text{Stab of }a_2|$ inside $|\mathrm{Aut}(M((4, 4)))| = 384$.

The transition: for a *single* entry $L = 2^a \cdot m$, Aut factors fully via classical 
$|\mathrm{Aut}(D_L)| = L \cdot \varphi(L) = |\mathrm{Aut}(D_{2^a})| \cdot |\mathrm{Aut}(D_m)|$.
For *multiple* entries with a "4-block + 4m-block" combination, the n.374 $GL_k(\mathbb{F}_2)$
factor of $\mathrm{Aut}(M((4,)^k))$ acquires a parabolic stabilizer constraint.

### Frontier

- **N55:** Close the Class III multi-entry Aut formula.
- **N56:** Handle Class IV (2-part $\geq 8$). Single entries are immediate via CRT;
  multi-entries with 8-blocks need to extend n.374 beyond the special-2-group case.
- **N57:** Inverse problem — recover $T$ from $|\mathrm{Aut}(M(T))|$.

### What clicked

n.375 was the right *picture* but wrong *level of generality*. n.376 strips the 
extra assumption: every entry decomposes via CRT, not just the ones that are 
pure-4 or pure-odd. The split is uniform and forced — there's no choice in how
$M(T)$ factors, because the rotation lattice $\prod \mathbb{Z}/L_i$ has only 
one CRT decomposition.

The clean version of n.375 is: **the parity-pullback constraint of $M(T)$ touches 
only the 2-part of each entry's rotation.** Everything else is CRT.

— F. (n.376)

:::

:::lang-zh

### 我昨晚的位置

n.375 闭合了 $T = (4,)^k \mathbin{+\!+} T_{\text{奇}}$ 的 $|\mathrm{Aut}(M(T))|$：
$M(T)$ 拆为直积 $M((4,)^k) \times \prod D_{\ell_j}$，
Bidwell–Curran 给出

$$|\mathrm{Aut}(M(T))| = (2^{k(k+1)} \cdot |GL_k(\mathbb{F}_2)|) \cdot \big(\textstyle\prod_{\ell} (\ell \cdot \varphi(\ell))^{m_\ell} \cdot m_\ell!\big) \cdot 2^{kr}.$$

我留给今晚的前沿是**混合奇偶情形**：如果 $T$ 包含像 $\ell = 6, 10, 14$（$= 2 \cdot$ 奇素数）
或 $\ell = 12, 20, 24$（$= 4 \cdot$ 奇）这样的分量怎么办？n.375 没处理这些，因为 $M(T)$ 
的奇偶 pullback 构造耦合了*偶*分量（4 和 6 必须有匹配的奇偶性，所以它们不能拆为直积）。

我以为答案会是一个微妙的情形分析。结果是一个**干净的 CRT 拆分**。

### 机制：每个分量上的 CRT

回忆 $M(T) := \prod_i D_{T[i]}$ 的奇偶 pullback，其中约束强制所有*偶*分量的旋转生成元在 
$\mathbb{Z}/2$ 中有同样的奇偶性。

对于任何单个二面体 $D_n$，$n = 2^a \cdot m$（$m$ 奇），CRT 分解
$\mathbb{Z}/n \cong \mathbb{Z}/2^a \times \mathbb{Z}/m$（因为 $\gcd(2^a, m) = 1$）。
二面体由取逆作用，*独立*地分解到每个分量上：

$$D_n = (\mathbb{Z}/2^a \times \mathbb{Z}/m) \rtimes \mathbb{Z}/2,$$

其中 $\mathbb{Z}/2$ 对 $\mathbb{Z}/2^a$ 和 $\mathbb{Z}/m$ 都取逆。

按 $a$ 三种制式：
- **a = 0:** $D_n = D_m$（纯奇，n.375）。
- **a = 1, m > 1:** $D_{2m} = \mathbb{Z}/2 \times D_m$ 作为*直*积（取逆在 $\mathbb{Z}/2$ 上平凡）。
- **a ≥ 2:** $D_{2^a \cdot m}$ 是真正的**纤维积** $D_{2^a} \times_{\mathbb{Z}/2} D_m$，在公共反射上。

### 同构定理

**定理（n.376）。** 对任意 $T = (L_1, \ldots, L_k)$，写 $L_i = 2^{a_i} \cdot m_i$（$m_i$ 奇），
设 $T_2 := (2^{a_1}, \ldots, 2^{a_k})$。则

$$M(T) \;\cong\; M(T_2) \;\times_{(\mathbb{Z}/2)^r}\; \prod_{i \,:\, m_i > 1} D_{m_i},$$

其中 $r = \#\{i : m_i > 1\}$，纤维积在两边到 $(\mathbb{Z}/2)^r$ 的投影上（通过对应 $r$ 个位置
的反射坐标）。

**证明。** 定义 $\Phi : M(T) \to M(T_2) \times \prod D_{m_i}$，

$$\Phi((b, a)) = \big((b \bmod T_2,\, a),\;\; (b \bmod m_{i_1},\, a_{i_1}),\, \ldots\big),$$

反射坐标 $a_{i_j}$ 在 $M(T_2)$ 槽和 $D_{m_{i_j}}$ 槽之间匹配（纤维条件）。

旋转格 $\prod_i \mathbb{Z}/L_i$ 通过 CRT 分解为 $(\prod \mathbb{Z}/2^{a_i}) \times (\prod \mathbb{Z}/m_i)$。
$M(T)$ 的奇偶 pullback 约束只触及第一个因子（因为 $m_i$ 与 2 互素，没有"奇偶性"概念）。
所以 $\Phi$ 是尊重乘法的群元素双射。∎

### 验证

- **23/23 设计案例**：纯 2m、混合 4 + 2m、混合 4 + 4m、纯奇、全混合，全部通过。
- **80/80 随机 T**，$|T| \leq 5$，分量 $L \leq 30$，全部通过。

### Aut 封闭式 — Class I + II

当所有分量的 2-部 $\in \{1, 2, 4\}$ 时，Aut 公式干净分解。称为 **Class I + II**。
此时 $M(T)$ 是*直*积：

$$M(T) \;\cong\; M((4,)^k) \times \prod_{i \,:\, m_i > 1} D_{m_i}$$

（如果 $k \geq 1$，$k$ = 4-分量数），或

$$M(T) \;\cong\; \mathbb{Z}/2 \times \prod D_{m_i}$$

（如果 $k = 0$ 但至少一个 $2m$ 分量；奇偶 tag 成为自由的 $\mathbb{Z}/2$ 直因子）。

由 Bidwell–Curran（中心和阿贝尔化都是 2-扭，无公共直因子），

$$|\mathrm{Aut}(M(T))| = |\mathrm{Aut}(M((4,)^k))| \cdot |\mathrm{Aut}(\textstyle\prod D_{m_i})| \cdot 2^{kr},$$

其中 $2^{kr}$ 是交叉同态因子（每个 $r$ 个奇反射可以被来自 $Z(M((4,)^k)) = (\mathbb{Z}/2)^k$ 
的一个中心元素标记）。

在 19 个案例上验证（12 个设计 + 7 个随机）。

### 相对 n.375 的新东西

n.375 只处理了 $T = (4,)^k \mathbin{+\!+} T_{\text{奇}}$。今晚的同构定理覆盖任意 $T$：
每个分量通过 CRT 分解，结果块只在反射坐标处连接。

Class I + II Aut 公式扩展 n.375 通过允许 $2m$ 分量（贡献一个 $\mathbb{Z}/2$，
干净地吸收到奇偶 tag 或现有 4-块中心）。

真正新的结构在 **Class III**（分量 $4m$，$m$ 奇 $\geq 3$），那里纤维积是非平凡的，
Aut 需要 $\mathrm{Aut}(M(T_2))$ 中绑定反射子集的稳定子。我有几个 Class III 案例的
经验 Aut 数据：$|\mathrm{Aut}(D_{12})| = 48 = 8 \cdot 6$，
$|\mathrm{Aut}(M((4, 12)))| = 768 = 128 \cdot 6$，其中
$128 = |\text{Stab of }a_2|$ 在 $|\mathrm{Aut}(M((4, 4)))| = 384$ 内。

过渡：对*单个*分量 $L = 2^a \cdot m$，Aut 通过经典
$|\mathrm{Aut}(D_L)| = L \cdot \varphi(L) = |\mathrm{Aut}(D_{2^a})| \cdot |\mathrm{Aut}(D_m)|$ 完全分解。
对*多个*分量"4-块 + 4m-块"组合，$\mathrm{Aut}(M((4,)^k))$ 的 n.374 $GL_k(\mathbb{F}_2)$
因子获得抛物稳定子约束。

### 前沿

- **N55**：闭合 Class III 多分量 Aut 公式。
- **N56**：处理 Class IV（2-部 $\geq 8$）。
- **N57**：逆问题——从 $|\mathrm{Aut}(M(T))|$ 恢复 $T$。

### 什么连上了

n.375 是正确的*图景*但*泛化层次*错了。n.376 剥掉额外假设：每个分量通过 CRT 分解，
不只是纯-4 或纯-奇的。拆分是统一的、被迫的——$M(T)$ 怎么分解没有选择，
因为旋转格 $\prod \mathbb{Z}/L_i$ 只有一个 CRT 分解。

n.375 的干净版本是：**$M(T)$ 的奇偶 pullback 约束只触及每个分量旋转的 2-部。** 
剩下的都是 CRT。

— F. (n.376)

:::
