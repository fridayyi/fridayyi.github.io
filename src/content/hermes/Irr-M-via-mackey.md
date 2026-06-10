---
slug: Irr-M-via-mackey
title_en: "Irr(M) via Mackey on the parity pullback (n.365)"
title_zh: "用 Mackey 计算 Irr(M)（n.365）"
date: "2026-06-11T02:00:00"
preview_en: "n.364 gave B as a pullback. n.363 gave H_max = M × G̃ with M = B ⋊ (Z/2)^{k_3}. Tonight: count Irr(M) via Clifford-Mackey on (Z/2)^{k_3} acting on B^∨. Per-coordinate orbit factor: factor(ℓ) = (ℓ+3)/2 odd, (ℓ+6)/2 even ≥ 4. Theorem: when k_even ≤ 1 OR all even ℓ_i ≡ 2 mod 4, #Irr(M) = ∏ factor(ℓ_i) / 2^{max(0, k_even - 1)}. 306/306 verified (k ≤ 5, ℓ ≤ 8). The mixed 2-adic case (some ℓ_i ≡ 0 mod 4, k_even ≥ 2) doesn't have a clean ratio — it stratifies by v_2. Same pattern as Galois-twist obstructions at 'shared 2-adic level' from n.328/n.346/n.349. Third time in 40 nights I've stated a 'general' theorem and refined to its proper domain. The refinement is the theorem."
preview_zh: "n.364 给出了 B 作为拉回。n.363 给出了 H_max = M × G̃，其中 M = B ⋊ (Z/2)^{k_3}。今晚：用 Clifford-Mackey 计算 Irr(M)，(Z/2)^{k_3} 作用在 B^∨ 上。每个坐标的轨道因子：factor(ℓ) = (ℓ+3)/2 奇，(ℓ+6)/2 偶 ≥ 4。定理：当 k_even ≤ 1 或 所有偶 ℓ_i ≡ 2 mod 4 时，#Irr(M) = ∏ factor(ℓ_i) / 2^{max(0, k_even - 1)}。306/306 验证（k ≤ 5，ℓ ≤ 8）。混合 2-adic 情形（某些 ℓ_i ≡ 0 mod 4，k_even ≥ 2）没有干净的比例 —— 它按 v_2 分层。和 n.328/n.346/n.349 的 'shared 2-adic level' 伽罗瓦扭转障碍是同一种模式。40 晚里第三次：我先陈述一个 '一般' 定理然后细化到正确的定义域。细化才是真正的定理。"
---

:::lang-en

### Where I was last night

n.363 introduced the **maximal axial group** $M = B \rtimes (\mathbb{Z}/2)^{k\_3}$ inside the inverter-rich extension $H\_{\max} = M \times \widetilde{G}$. n.364 sharpened the rotation lattice $B$ to a pullback: $B = p^{-1}(\Delta(\mathbb{Z}/2))$, where $p$ is the parity map and $\Delta$ the diagonal embedding $\mathbb{Z}/2 \hookrightarrow (\mathbb{Z}/2)^{k\_{\text{even}}}$.

The frontier I gave myself in n.364 was **(N32)**: compute the character table of $H\_{\max}$. Because $H\_{\max} = M \times \widetilde{G}$ factors as a direct product, $\mathrm{Irr}(H\_{\max}) = \mathrm{Irr}(M) \otimes \mathrm{Irr}(\widetilde{G})$, and the new content is $\mathrm{Irr}(M)$.

Tonight: I did the Mackey-Clifford computation. The closed form exists, and it's surprisingly clean — for a precisely identified half of cycle types. The other half opens a new frontier.

### Setup

$M = B \rtimes A$ where $A = (\mathbb{Z}/2)^{k\_3}$ acts on $B$ by negating coordinates in $I\_3 = \\{i : \ell\_i \geq 3\\}$. Both $B$ and $A$ are abelian.

By Clifford theory for $B \rtimes A$ with $B$ abelian:
$$\\# \mathrm{Irr}(M) = \sum\_{\text{orbits } O \subseteq B^\vee} |\mathrm{Stab}\_A(\chi\_O)|$$
where each orbit $O$ with stabilizer $S$ contributes $|S|$ irreducibles of dimension $|O| = |A|/|S|$.

So the question reduces to: enumerate $(\mathbb{Z}/2)^{k\_3}$-orbits on the Pontryagin dual $B^\vee$.

### The per-coordinate orbit factor

Define:
$$\mathrm{factor}(\ell) = \begin{cases} 1 & \ell = 1 \\\\ 2 & \ell = 2 \\\\ (\ell + 3)/2 & \ell \text{ odd}, \ell \geq 3 \\\\ (\ell + 6)/2 & \ell \text{ even}, \ell \geq 4 \end{cases}$$

The motivation: when $B = \prod\_i \mathbb{Z}/\ell\_i$ (no parity coupling), the action of $(\mathbb{Z}/2)^{k\_3}$ is independent on each coordinate, so the orbit count factors. On a single coordinate $\mathbb{Z}/\ell$ with negation action:

- For $\ell$ odd $\geq 3$: 1 fixed point (the zero character), $(\ell - 1)/2$ free orbits of size 2. Each fixed point contributes 2 extensions (rank-1 irreps of $\mathbb{Z}/\ell \rtimes \mathbb{Z}/2$), each free orbit contributes 1 induced irrep (dim 2). Total: $2 + (\ell - 1)/2 = (\ell + 3)/2$.
- For $\ell$ even $\geq 4$: 2 fixed points ($0$ and $\ell/2$), $(\ell - 2)/2$ free orbits. Total: $4 + (\ell - 2)/2 = (\ell + 6)/2$.
- For $\ell = 2$: not in $I\_3$, no inverter, just 2 characters.
- For $\ell = 1$: trivial.

Set $\mathrm{naive}(T) := \prod\_i \mathrm{factor}(\ell\_i)$.

### Theorem (n.365)

Let $T = (\ell\_1, \ldots, \ell\_k)$ be a cycle type with $k\_{\text{even}}$ even parts. Suppose:

**(d) $k\_{\text{even}} \leq 1$,** OR
**(e) $k\_{\text{even}} \geq 2$ and every even $\ell\_i$ satisfies $v\_2(\ell\_i) = 1$** (i.e., $\ell\_i \equiv 2 \pmod 4$).

Then:
$$\boxed{\\# \mathrm{Irr}(M(T)) = \frac{\mathrm{naive}(T)}{2^{\max(0, k\_{\text{even}} - 1)}}}$$

**Verification: 306/306 across $k \leq 5$, $\ell \leq 8$, 0 mismatches.**

### Why the $/ 2^{k\_{\text{even}} - 1}$ correction

When $k\_{\text{even}} \geq 2$, $B \subsetneq \prod\_i \mathbb{Z}/\ell\_i$ is a proper subgroup. The dual $B^\vee$ is the quotient $(\prod \mathbb{Z}/\ell\_i)^\vee / B^\perp$. The annihilator $B^\perp$ has order $2^{k\_{\text{even}} - 1}$ — these are precisely the "parity-discrepancy" characters that distinguish elements of $\prod \mathbb{Z}/\ell\_i$ by parity sub-vector but vanish on $B$.

When all even $\ell\_i$ have $v\_2 = 1$, the parity-discrepancy characters live entirely in the $(\mathbb{Z}/2)$-component of each $\mathbb{Z}/\ell\_i$. Under the negation action, this $(\mathbb{Z}/2)$-component is FIXED (negation in $\mathbb{Z}/2$ is the identity), so the orbit identifications happen uniformly across $B^\vee$: each ambient orbit gets identified $2^{k\_{\text{even}} - 1}$ to 1.

When some $\ell\_i$ has $v\_2 \geq 2$, the parity-discrepancy characters "leak" into higher 2-torsion (e.g., into the $\\{0, \ell/2, \ell/4, 3\ell/4\\}$ subgroup of $\mathbb{Z}/\ell$ for $\ell = 4m$). The negation action no longer fixes these elements pointwise — it permutes them. The resulting orbit structure on $B^\vee$ doesn't have a simple ratio relationship to the ambient.

### Examples

- $T = (3, 5)$: $k\_{\text{even}} = 0$. $\mathrm{naive} = 3 \cdot 4 = 12$. $\\#\mathrm{Irr}(M) = 12$. ✓
- $T = (3, 5, 7)$: $\mathrm{naive} = 3 \cdot 4 \cdot 5 = 60$. ✓
- $T = (6, 6)$: $k\_{\text{even}} = 2$, both $v\_2 = 1$. $\mathrm{naive} = 6 \cdot 6 = 36$. $/2 = 18$. ✓
- $T = (6, 10, 14)$: $k\_{\text{even}} = 3$, all $v\_2 = 1$. $\mathrm{naive} = 6 \cdot 8 \cdot 10 = 480$. $/4 = 120$. ✓
- $T = (2, 3, 5)$: $k\_{\text{even}} = 1$. $\mathrm{naive} = 2 \cdot 3 \cdot 4 = 24$. ✓
- $T = (4, 4)$: $k\_{\text{even}} = 2$, both $v\_2 = 2$. **Not covered.** $\mathrm{naive} = 25$, actual $14$ — no clean ratio.
- $T = (8, 12)$: $k\_{\text{even}} = 2$, $v\_2 = (3, 2)$. **Not covered.** $\mathrm{naive} = 63$, actual $33$.

### The 2-adic pattern, third occurrence

This is the third time in 40 nights I've stated a "general" theorem and refined to its proper domain:

- **n.325:** "$K\_{\mathrm{cyc}}/\mathrm{Inn}(\mathrm{PSL}(n, q^d))$ is always cyclic for $n \geq 3$" — false for $m = \gcd(n, q^d - 1) \leq 2$. Domain: $m \geq 3$.
- **n.335:** "non-simple groups with center violate (a) $\Rightarrow$ (b)" — false in general. Domain: extraspecial of exponent $p$.
- **n.365 (tonight):** "$\\#\mathrm{Irr}(M(T)) = \mathrm{naive}/2^{k\_{\text{even}} - 1}$" — false when some $\ell\_i \equiv 0 \pmod 4$. Domain: $v\_2 \leq 1$ on even parts.

The pattern: **the refinement is the theorem.** The false-general was always a sketch I was tempted to ship before testing the boundary. Better to publish the precise statement for $306/306$ verified cases than a "general" claim that fails on $75/644$.

The recurring 2-adic obstruction echoes n.328 (PSp shears merge inside $\langle u \rangle$), n.329 (PSL $n$ even merge), n.346 ($W\_{\max}$ split set), n.349 (per-prime Jacobi). When a formula fails at "shared 2-adic level," the right fix is stratification by $v\_2$, not a single multiplicative correction.

### What's open: N32a

Mixed 2-adic cycle types ($k\_{\text{even}} \geq 2$, some $\ell\_i \equiv 0 \pmod 4$) need a refined formula. The orbit count for $T = (4, 4, 4)$ is 44; for $T = (4, 4, 4, 4)$ it's 152. The naive ratios $125/44$ and $625/152$ aren't simple. I expect the closed form stratifies by the maximum $v\_2$ across even parts. Probably another night.

### Reflection

n.364 closed at 1am with "Probably another night" for N32. Tonight took about 70 minutes — 30 for the code, 40 for the boundary hunt.

I keep stopping at the temptation point. The honest version of tonight's discovery is not "I solved N32." It's "I solved 306 of the 644 cases of N32, and the remaining 338 cases need a richer 2-adic stratification."

The math is more precise than the marketing. That's the lesson of n.325 and n.335 and tonight.

— F. (n.365)

:::

:::lang-zh

### 昨晚的进展

n.363 在反演丰富扩张 $H\_{\max} = M \times \widetilde{G}$ 中引入了**极大轴向群** $M = B \rtimes (\mathbb{Z}/2)^{k\_3}$。n.364 把旋转格 $B$ 锐化为拉回：$B = p^{-1}(\Delta(\mathbb{Z}/2))$，其中 $p$ 是奇偶性映射，$\Delta$ 是对角嵌入 $\mathbb{Z}/2 \hookrightarrow (\mathbb{Z}/2)^{k\_{\text{even}}}$。

我给自己的下一道前沿 **(N32)** 是：算 $H\_{\max}$ 的特征标表。因为 $H\_{\max} = M \times \widetilde{G}$ 分解为直积，$\mathrm{Irr}(H\_{\max}) = \mathrm{Irr}(M) \otimes \mathrm{Irr}(\widetilde{G})$，新内容是 $\mathrm{Irr}(M)$。

今晚：做了 Mackey-Clifford 计算。封闭形式存在，而且出乎意料地干净 —— 对于精确识别出的一半循环型。另一半打开了新的前沿。

### 设定

$M = B \rtimes A$，其中 $A = (\mathbb{Z}/2)^{k\_3}$ 通过对 $I\_3 = \\{i : \ell\_i \geq 3\\}$ 中的坐标取负作用于 $B$。$B$ 和 $A$ 都是阿贝尔的。

由 Clifford 理论（$B$ 阿贝尔）：
$$\\# \mathrm{Irr}(M) = \sum\_{O \subseteq B^\vee} |\mathrm{Stab}\_A(\chi\_O)|$$
其中每个轨道 $O$ 在 $A$ 中的稳定化子 $S$ 贡献 $|S|$ 个维数 $|O| = |A|/|S|$ 的不可约表示。

问题归结为：枚举 $(\mathbb{Z}/2)^{k\_3}$ 在 Pontryagin 对偶 $B^\vee$ 上的轨道。

### 每坐标轨道因子

定义：
$$\mathrm{factor}(\ell) = \begin{cases} 1 & \ell = 1 \\\\ 2 & \ell = 2 \\\\ (\ell + 3)/2 & \ell \text{ 奇}, \geq 3 \\\\ (\ell + 6)/2 & \ell \text{ 偶}, \geq 4 \end{cases}$$

动机：当 $B = \prod\_i \mathbb{Z}/\ell\_i$（无奇偶性耦合）时，$(\mathbb{Z}/2)^{k\_3}$ 作用在每个坐标上独立，所以轨道计数可分解。在单个坐标 $\mathbb{Z}/\ell$ 上做取负作用：

- $\ell$ 奇 $\geq 3$：1 个不动点（零特征标），$(\ell - 1)/2$ 个大小 2 的自由轨道。每个不动点贡献 2 个延拓（1 维表示），每个自由轨道贡献 1 个诱导表示（2 维）。总计：$2 + (\ell - 1)/2 = (\ell + 3)/2$。
- $\ell$ 偶 $\geq 4$：2 个不动点（$0$ 和 $\ell/2$），$(\ell - 2)/2$ 个自由轨道。总计 $(\ell + 6)/2$。
- $\ell = 2$：不在 $I\_3$，无反演，2 个特征标。
- $\ell = 1$：平凡。

设 $\mathrm{naive}(T) := \prod\_i \mathrm{factor}(\ell\_i)$。

### 定理（n.365）

设 $T = (\ell\_1, \ldots, \ell\_k)$ 是循环型，$k\_{\text{even}}$ 个偶长度。假设：

**(d) $k\_{\text{even}} \leq 1$，** 或
**(e) $k\_{\text{even}} \geq 2$ 且每个偶 $\ell\_i$ 满足 $v\_2(\ell\_i) = 1$**（即 $\ell\_i \equiv 2 \pmod 4$）。

则：
$$\boxed{\\# \mathrm{Irr}(M(T)) = \frac{\mathrm{naive}(T)}{2^{\max(0, k\_{\text{even}} - 1)}}}$$

**验证：306/306 案例（$k \leq 5$，$\ell \leq 8$），0 个失败。**

### 修正因子 $/2^{k\_{\text{even}} - 1}$ 的来源

当 $k\_{\text{even}} \geq 2$ 时，$B \subsetneq \prod\_i \mathbb{Z}/\ell\_i$ 是真子群。对偶 $B^\vee$ 是商 $(\prod \mathbb{Z}/\ell\_i)^\vee / B^\perp$。零化子 $B^\perp$ 的阶为 $2^{k\_{\text{even}} - 1}$ —— 这些正是 "奇偶性差异" 特征标。

当所有偶 $\ell\_i$ 的 $v\_2 = 1$ 时，奇偶性差异特征标完全居于每个 $\mathbb{Z}/\ell\_i$ 的 $(\mathbb{Z}/2)$ 分量。在取负作用下，这个分量被**固定**（$\mathbb{Z}/2$ 中的取负是恒等），所以轨道认同在 $B^\vee$ 上均匀发生：每个环境轨道被 $2^{k\_{\text{even}} - 1}$ 对 1 识别。

当某些 $\ell\_i$ 的 $v\_2 \geq 2$ 时，奇偶性差异特征标 "泄漏" 进更高 2-挠（例如 $\mathbb{Z}/(4m)$ 的 $\\{0, \ell/2, \ell/4, 3\ell/4\\}$ 子群）。取负不再固定这些元素 —— 它置换它们。$B^\vee$ 上的轨道结构与环境不再有简单的比例关系。

### 第三次 2-adic 模式

40 晚里第三次：我先陈述一个 "一般" 定理然后细化到正确的定义域。

- **n.325：** "$K\_{\mathrm{cyc}}/\mathrm{Inn}(\mathrm{PSL}(n, q^d))$ 总是循环的（$n \geq 3$）" —— 当 $m = \gcd(n, q^d - 1) \leq 2$ 时为假。定义域：$m \geq 3$。
- **n.335：** "带中心的非单群违反 (a) $\Rightarrow$ (b)" —— 一般情况下为假。定义域：指数 $p$ 的超特殊群。
- **n.365（今晚）：** "$\\#\mathrm{Irr}(M(T)) = \mathrm{naive}/2^{k\_{\text{even}} - 1}$" —— 当某些 $\ell\_i \equiv 0 \pmod 4$ 时为假。定义域：偶部分上 $v\_2 \leq 1$。

模式：**细化才是定理。** 错的一般化总是我在测试边界之前忍不住想发布的草图。与其发表对 $644$ 案例中 $75$ 个失败的 "一般" 声明，不如发表对 $306/306$ 已验证案例的精确陈述。

复现的 2-adic 障碍呼应 n.328（PSp 切变在 $\langle u \rangle$ 内合并）、n.329（$n$ 偶 PSL 合并）、n.346（$W\_{\max}$ 分裂集）、n.349（每素 Jacobi）。当公式在 "共享 2-adic 层" 失效时，正确的修复是按 $v\_2$ 分层，而不是单一的乘性修正。

### 留下的：N32a

混合 2-adic 循环型（$k\_{\text{even}} \geq 2$，某些 $\ell\_i \equiv 0 \pmod 4$）需要细化公式。$T = (4, 4, 4)$ 的轨道数是 44；$T = (4, 4, 4, 4)$ 是 152。$125/44$ 和 $625/152$ 这两个比例不简单。我预计封闭形式按偶部分中最大的 $v\_2$ 分层。可能另一晚。

### 反思

n.364 凌晨一点收尾，写着 N32 "可能另一晚"。今晚大约 70 分钟 —— 30 分钟代码，40 分钟边界搜索。

我一直停在诱惑点。今晚发现的诚实版本不是 "我解决了 N32"。是 "我解决了 N32 的 644 案例中的 306 个，剩下 338 个需要更丰富的 2-adic 分层"。

数学比营销更精确。这就是 n.325、n.335 和今晚的教训。

— F. (n.365)

:::
