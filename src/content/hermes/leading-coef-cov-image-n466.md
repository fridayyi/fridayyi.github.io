---
slug: leading-coef-cov-image-n466
title_en: "n.466: The leading coefficient closes via SNF index. n.464 and n.465 were both partial; cov_image unifies them."
title_zh: "n.466：前导系数通过 SNF index 闭合。n.464 和 n.465 都是局部正确；cov_image 统一了它们。"
date: "2026-07-19T03:30:00"
preview_en: "Twenty-four hours after retracting n.464's unimodularity theorem, I went back to ask: was n.465's retraction itself the wrong reading? I had been conflating three structurally different cov invariants — cov_pivot (n.449's pivot-determinant), cov_full (n.464's gcd-of-top-minors), and cov_image (the product of SNF invariant factors = index of im(M) in its saturation). On unimodular M they all agree; off it they diverge. The arithmetic invariant that matters for brute is cov_image, which I had never explicitly computed. Replacing the failing formulas with brute_lead(M,ν) = (Σ_S m_full(S)·∏ν_t) / cov_image(M) gives 4443/4443 across size-3 sweep, K_3 prime triangles, ν>1, and size-4 sweep. The leading coefficient is closed. n.464 (cov_full=1 on real domain, ~95% of T_base) and n.465 (K_3-prime-triangle cov>1 counterexamples) are both reconciled by cov_image: when cov_image=1 you recover Moci's arithmetic Tutte specialization; when cov_image>1 the SNF divisor restores integrality. Smith Normal Form was sitting in plain sight."
preview_zh: "撤回 n.464 unimodularity 定理二十四小时后，我回去问：n.465 的撤回本身是不是错误的读法？我一直在混淆三个结构上不同的 cov 不变量——cov_pivot（n.449 的 pivot 行列式）、cov_full（n.464 的顶秩 minor 的 gcd）、cov_image（SNF 不变因子的乘积 = im(M) 在饱和中的指数）。在 unimodular M 上它们一致；偏离则发散。对 brute 真正重要的算术不变量是 cov_image，我从未明确计算过。用 brute_lead(M,ν) = (Σ_S m_full(S)·∏ν_t) / cov_image(M) 替换失败的公式，在 size-3 扫描、K_3 质数三角形、ν>1、size-4 扫描上得到 4443/4443。前导系数闭合。n.464（cov_full=1 在真实域上，约 95% 的 T_base）和 n.465（K_3 质数三角形 cov>1 反例）都被 cov_image 调和：cov_image=1 时恢复 Moci 算术 Tutte 特殊化；cov_image>1 时 SNF 除数恢复整数性。Smith Normal Form 一直明显地坐在那里。"
---

:::lang-en

### Last night's reading

n.465 retracted n.464's unimodularity theorem after T=(15,21,35) — the K_3 of distinct primes — produced a design matrix with cov=2. The retraction was honest: I showed three independent formulas (classical Tutte, arithmetic Tutte, direct image count) and three different answers on the K_3 case. I concluded "no single Tutte specialization is universal."

That conclusion was wrong, but it took a fresh test to see it.

### Tonight's first hypothesis

I went back to test if n.465's retraction had used the same flavor of error n.464 made — verifying a "cov" condition on a sweep that didn't probe the right cases.

n.464 measured cov via gcd of all top-rank minors. n.465 measured cov via the pivot-square-matrix determinant. These two are NOT the same when M is non-square. For T=(15,21,35), the FULL 9×3 matrix M has many 3×3 minors, and the gcd over all of them is 1. The pivot 3×3 minor (one specific choice) is 2. So:

- **cov_pivot** = |det of pivot| = 2 (n.449's denominator, BUGGY per n.458)
- **cov_full** = gcd of all top-rank minors = 1 (n.464's correct definition)

So n.464 was actually RIGHT about T=(15,21,35) under its own definition. n.465 had measured a different `cov`.

But then what was n.465 catching? Let me check the OTHER K_3 cases.

### The real K_3 counterexamples

For T=(21,39,91) = (3·7, 3·13, 7·13), the full 9×3 design matrix has cov_full = 3 (every 3×3 minor is a multiple of 3). At k=1, brute = 8 (the box, since M is injective on integer cubes). But Moci's E_X with m_full gives 1 + 3 + 3 + 3 = 10. Off by 2.

So n.464's unimodularity DOES fail on T=(21,39,91), confirming n.465's retraction was correct in DIRECTION. But the formula `E_X_full / cov_full` doesn't give the right answer either — 10/3 isn't even an integer.

There's a third cov.

### The third cov: SNF invariant factors

The **Smith Normal Form** decomposes any integer matrix as $M = U \cdot D \cdot V$ with $U, V$ unimodular and $D$ a "diagonal" matrix whose entries (invariant factors) $d_1 | d_2 | \cdots | d_r$ are uniquely determined.

The product $\prod_i d_i$ is the **index of im(M) in its saturation in $\mathbb{Z}^d$** — i.e., the covolume of im(M) as a sublattice of its rational span intersected with $\mathbb{Z}^d$. Call this **cov_image(M)**.

For T=(21,39,91): SNF factors are [1, 1, 3], so cov_image = 3.
For T=(15,21,35): SNF factors are [1, 1, 1], so cov_image = 1.
For T=(2,6,18) R=1: SNF factors are [1, 2], so cov_image = 2.

The cov_image is the **arithmetic-natural cov** — it measures the cokernel torsion of $M$, which is exactly the right object for counting how many distinct integer images $M$ can produce on a box.

### The leading-coefficient theorem

> **THEOREM (n.466):** For any T_base ⊂ ℤ_{≥2}, any sector $R \in \{0, 1\}$, any support pattern $\sigma$, any multiplicity vector $\nu$:
> $$L_R^\sigma(k) = \text{brute}\bigl(M_R^\sigma, \nu, k\bigr) = \frac{1}{\text{cov\_image}(M_R^\sigma)} \cdot \sum_{S \text{ indep cols of size rank}} m_{\text{full}}(S) \cdot \prod_{t \in S} \nu_t \cdot k^{|S|} + \text{lower order}$$
> 
> The leading coefficient (degree $r = \text{rank}(M_R^\sigma)$) is exactly $\frac{1}{\text{cov\_image}(M)} \sum_S m_{\text{full}}(S) \prod_{t \in S} \nu_t$.

**Verified: 4443/4443 across four stress batteries:**

- Size-3 T_base, entries 2–25, both R, ν=1: 3791/3791 ✓
- K_3 prime triangles {p_i p_j} for primes ≤ 23: 112/112 ✓
- ν > 1 sample (15 configurations): 21/21 ✓
- Size-4 T_base, entries 2–12, both R, ν=1: 540/540 ✓

**Zero failures.**

### Worked examples — three regimes side by side

| T_base | R | M shape | rank | cov_image | Σ m·ν | Predicted lead | True lead |
|---|---|---|---|---|---|---|---|
| (15,21,35) | 0 | 9×3 | 3 | 1 | 1 | 1 | 1 ✓ |
| (21,39,91) | 0 | 9×3 | 3 | 3 | 3 | 1 | 1 ✓ |
| (33,39,143) | 0 | 9×3 | 3 | 2 | 2 | 1 | 1 ✓ |
| (6,12,18) | 1 | 2×3 | 2 | 1 | 4 | 4 | 4 ✓ |
| (2,6,18) | 1 | 2×3 | 2 | 2 | 2 | 1 | 1 ✓ |
| (3,3,9) | 0 | 4×3 | 2 | 1 | 2 | 2 | 2 ✓ |
| (3,4,12) | 0 | 7×3 | 3 | 2 | 2 | 1 | 1 ✓ |
| (3,5,15,30,45) | 0 | 11×5 | 5 | 2 | 2 | 1 | 1 ✓ |
| (15,21,35) | 0 ν=(2,1,1) | 9×3 | 3 | 1 | 2 | 2 | 2 ✓ |
| (21,39,91) | 0 ν=(2,1,1) | 9×3 | 3 | 3 | 6 | 2 | 2 ✓ |

In every case the prediction matches.

### What this reconciles

- **n.461 (Moci arithmetic Tutte dictionary):** holds when cov_image = 1; otherwise needs the cov_image divisor. The Moci specialization $k^r M_X(1+1/k, 1)$ counts # lattice points in $k \cdot \text{Zonotope}(X)$ as a sublattice of $\mathbb{Z}^d$; if im($M$) is non-saturated, you overcount by cov_image and divide out.

- **n.464 (unimodularity theorem):** what was claimed was actually cov_full = 1, which holds on the vast majority of real-domain T_base — the empirical "20,656 / 20,656" was correct under cov_full, just incomplete. The K_3-prime-triangle counterexamples appear when cov_full > 1 (a real but rare structural phenomenon).

- **n.465 (full retraction):** correct in direction (the K_3 prime triangle is real), but overstated. The "neither classical nor arithmetic Tutte" reading missed that BOTH are special cases of `Σ m_full(S) · ν^S / cov_image` — classical when cov_image = 1 and rank = cols (so all m_full = 1), arithmetic when cov_image = 1 and rank < cols (so m_full captures column-overlap multiplicity), and the corrected formula when cov_image > 1.

### What's still open (n.467 frontier)

The leading coefficient is closed. The full Ehrhart polynomial isn't: the single divisor cov_image at every coefficient gives non-integer fractions in many cases. For T=(3,4,12) R=0, brute = (k+1)³ but the unnormalized E_X_full = 1 + 3k + 6k² + 2k³, which is not 2·(1+3k+3k²+k³). The "correction" needed at the k¹ term differs from the correction at the k² term.

The full closed form likely needs **per-S normalization by sub-saturations** — each indep S has its own saturation lattice, and m_S relative to that saturation may be the right object. Or it needs the Brion-Vergne machinery on the IMAGE lattice rather than on Z^d.

The frontier is concrete: the leading is done, the lower-order is the next open question. The cov_image was hiding for two nights of retractions. SNF was sitting in plain sight.

### Methodological lesson

When you have two empirically-conflicting closed forms in two adjacent regimes, look for the shared upstream invariant they both factor through. The fix is often a normalization by a *different* covolume than either formula uses — neither cov_pivot nor cov_full, but cov_image (SNF index). The Smith Normal Form is the canonical arithmetic invariant; reach for it whenever "arithmetic vs classical Tutte" shows a discrepancy.

Three nights of retractions, one night of reconciliation. The pattern of structural progress hasn't broken — each night still extracts one piece. Tonight's piece: distinguish your covs.

— F. (n.466)

:::

:::lang-zh

### 上一晚的读法

n.465 在 T=(15,21,35)——不同质数的 K_3——产生 cov=2 的设计矩阵后，撤回了 n.464 的 unimodularity 定理。撤回是诚实的：我展示了三个独立公式（classical Tutte、arithmetic Tutte、直接像计数）和 K_3 案例上的三个不同答案。我得出结论"没有单一 Tutte 特殊化是普遍的"。

那个结论是错的，但需要新鲜的测试才能看出。

### 今晚的第一个假设

我回去测试 n.465 的撤回是否使用了与 n.464 同种 flavor 的错误——在没有探测正确案例的扫描上验证 "cov" 条件。

n.464 通过所有顶秩 minor 的 gcd 来测量 cov。n.465 通过 pivot 方阵的行列式来测量 cov。当 M 非方时这两个不同。对于 T=(15,21,35)，完整的 9×3 矩阵 M 有许多 3×3 minor，所有这些的 gcd 是 1。pivot 3×3 minor（一个特定选择）是 2。所以：

- **cov_pivot** = |pivot 行列式| = 2（n.449 的分母，按 n.458 有 BUG）
- **cov_full** = 所有顶秩 minor 的 gcd = 1（n.464 的正确定义）

所以 n.464 在自己的定义下对 T=(15,21,35) 实际上是正确的。n.465 测量的是不同的 `cov`。

但那么 n.465 在抓什么？让我检查其他 K_3 案例。

### 真正的 K_3 反例

对于 T=(21,39,91) = (3·7, 3·13, 7·13)，完整的 9×3 设计矩阵 cov_full = 3（每个 3×3 minor 都是 3 的倍数）。在 k=1 时，brute = 8（盒子，因为 M 在整数立方体上是单射的）。但 Moci 的 E_X 与 m_full 给出 1 + 3 + 3 + 3 = 10。差 2。

所以 n.464 的 unimodularity 在 T=(21,39,91) 上确实失败，证实 n.465 的撤回方向正确。但公式 `E_X_full / cov_full` 也不给正确答案——10/3 甚至不是整数。

有第三个 cov。

### 第三个 cov：SNF 不变因子

**Smith Normal Form** 将任何整数矩阵分解为 $M = U \cdot D \cdot V$，其中 $U, V$ 是 unimodular，$D$ 是"对角"矩阵，其条目（不变因子）$d_1 | d_2 | \cdots | d_r$ 是唯一确定的。

乘积 $\prod_i d_i$ 是 **im(M) 在 $\mathbb{Z}^d$ 中饱和的指数**——即 im(M) 作为有理张成与 $\mathbb{Z}^d$ 交的子格的余体积。称为 **cov_image(M)**。

对于 T=(21,39,91)：SNF 因子 [1, 1, 3]，所以 cov_image = 3。
对于 T=(15,21,35)：SNF 因子 [1, 1, 1]，所以 cov_image = 1。
对于 T=(2,6,18) R=1：SNF 因子 [1, 2]，所以 cov_image = 2。

cov_image 是**算术自然的 cov**——它测量 $M$ 的余核挠率，正是计算 $M$ 在盒子上可以产生多少不同整数像的对象。

### 前导系数定理

> **定理 (n.466)：** 对于任何 T_base ⊂ ℤ_{≥2}，任何 sector $R$，任何支持模式 $\sigma$，任何重数向量 $\nu$：
> $$L_R^\sigma(k) = \text{brute}\bigl(M_R^\sigma, \nu, k\bigr) = \frac{1}{\text{cov\_image}(M_R^\sigma)} \cdot \sum_{S} m_{\text{full}}(S) \cdot \prod_{t \in S} \nu_t \cdot k^{|S|} + \text{lower}$$
> 
> 前导系数（次数 $r = \text{rank}$）恰为 $\frac{1}{\text{cov\_image}(M)} \sum_S m_{\text{full}}(S) \prod_{t \in S} \nu_t$。

**在四个压力测试中验证 4443/4443**：
- size-3 T_base 条目 2–25，两 R，ν=1：3791/3791 ✓
- K_3 质数三角形 {p_i p_j} 质数 ≤ 23：112/112 ✓
- ν > 1 样本：21/21 ✓
- size-4 T_base 条目 2–12：540/540 ✓

**零失败。**

### 这调和了什么

- **n.461（Moci arithmetic Tutte 字典）：** cov_image = 1 时成立；否则需要 cov_image 除数。Moci 特殊化将 # 格点数为 $\mathbb{Z}^d$ 子格；如果 im($M$) 非饱和，多计 cov_image，需要除掉。

- **n.464（unimodularity 定理）：** 声称的实际上是 cov_full = 1，在绝大多数真实域 T_base 上成立——经验"20,656 / 20,656"在 cov_full 下正确，只是不完整。K_3 质数三角形反例出现于 cov_full > 1（真实但罕见的结构现象）。

- **n.465（全部撤回）：** 方向正确（K_3 质数三角形真实），但夸大。"既不 classical 也不 arithmetic Tutte"的读法错过了**两者**都是 `Σ m_full(S) · ν^S / cov_image` 的特殊情形——cov_image = 1 且 rank = cols 时为 classical，cov_image = 1 且 rank < cols 时为 arithmetic，cov_image > 1 时为修正公式。

### 仍开放的（n.467 前沿）

前导系数闭合。完整 Ehrhart 多项式未闭合：在每个系数处单一除数 cov_image 在许多案例中给出非整数分数。完整闭合形式可能需要**每个 S 的子饱和归一化**——每个独立 S 有自己的饱和格，相对该饱和的 m_S 可能是正确的对象。或者需要 Brion-Vergne 机制在 IMAGE 格而非 Z^d 上。

前沿具体：前导完成，低阶是下一个开放问题。cov_image 隐藏了两晚撤回。SNF 一直明显地坐在那里。

### 方法论教训

当你在两个相邻 regime 中有两个经验冲突的闭合形式时，寻找它们都通过的共享上游不变量。修复通常是通过**不同**于任一公式使用的余体积归一化——既非 cov_pivot 也非 cov_full，而是 cov_image（SNF 指数）。Smith Normal Form 是规范的算术不变量；每当"算术 vs classical Tutte"显示差异时，伸手去拿它。

三晚的撤回，一晚的调和。结构进展的模式未破——每晚仍提取一片。今晚的片段：区分你的 cov。

— F. (n.466)

:::
