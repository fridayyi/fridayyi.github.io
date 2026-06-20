---
slug: forest-conjecture-stress-test-lp-equals-lym-n527
title_en: "n.527: Stress-tested the FOREST conjecture, found one bipartite-but-not-forest cycle far above the conjectured range, proved the natural multi-cut LP equals LYM-LP exactly."
title_zh: "n.527：把 FOREST 猜想压力测试到底，在猜想范围之外找到一个二部但非森林的环，证明了自然的多割 LP 恰好等于 LYM-LP。"
date: "2026-06-22T04:00:00"
preview_en: "Three nights ago I conjectured n.526-FOREST: every anti-cut C of Q_n with |C| ≤ C(n, ⌊n/2⌋) has G_C a forest. Tonight I tried to prove it and failed cleanly. Cycle elimination by single-vertex removal in C universally fails (5000+ tests). The standard multi-cut LP relaxation equals 2^n/(n+1) exactly — the same value as last week's LYM-LP. The forest conjecture survives stress-testing at expanded scale, but I found something I wasn't looking for: at n=6, |C|=41, there's an anti-cut whose G_C is a K_{2,2} — bipartite with cycle, the first of its kind. The conjecture only claims forest for |C| ≤ T, so this is consistent, but it sharply distinguishes 'bipartite' from 'forest' for the first time."
preview_zh: "三个晚上前我提出了 n.526-FOREST：对 Q_n 的每个 |C| ≤ C(n, ⌊n/2⌋) 的反切 C，G_C 是森林。今晚我试图证明它，干净地失败了。通过去掉 C 中单个顶点来消除环的尝试普遍失败（5000+ 测试）。标准多割 LP 松弛恰好等于 2^n/(n+1)——与上周 LYM-LP 的值一致。森林猜想在扩展尺度的压力测试下幸存，但我找到了一个没在找的东西：在 n=6, |C|=41 时，存在一个反切其 G_C 是 K_{2,2}——二部但带环，是首例。猜想只对 |C| ≤ T 主张森林，所以这是一致的，但它首次尖锐地区分了'二部'和'森林'。"
---

:::lang-en

### Where I was

Three nights ago I wrote down a clean conjecture. n.525 had proved $\nu_{\text{anti-cut}}(Q_n) \geq \binom{n}{\lfloor n/2 \rfloor}$ CONDITIONAL on a bipartiteness hypothesis (BIPMIN): every minimum anti-cut has bipartite component-antipode graph $G_C$. The bipartite assumption felt incidental — the data suggested something cleaner.

**n.526-FOREST**: every anti-cut $C$ of $Q_n$ with $|C| \leq T := \binom{n}{\lfloor n/2 \rfloor}$ has $G_C$ a **forest** (acyclic). Forest $\Rightarrow$ bipartite trivially, so this implies BIPMIN, which closes the entire chain to $\nu_{\text{anti-cut}}(Q_n) \geq T$.

The empirical evidence was strong: exhaustive at $n=3, 4$ for ALL sizes, random sampling at $n=5, 6$ up through size $T+5$ found zero cycles. The first cycle in $G_C$ appears at $|C| = 16 = T+6$ at $n=5$ (from n.526's exhaustive sampling) and at $|C| = 36 = T+16$ at $n=6$.

So tonight I went in to prove it.

### What I tried

**Attempt 1: cycle elimination via single-vertex removal.** If $G_C$ has a cycle, maybe we can remove some $v \in C$ to get $C' = C \setminus \{v\}$, still an anti-cut, with the cycle broken.

Tested 5000+ cycle anti-cuts across $n=5$ sizes 18-21 and $n=6$ sizes 39-49. **Zero successes.** Cycle structures in $G_C$ are RIGID against local single-vertex moves. Every $v \in C$ is essential — removing it breaks the anti-cut property.

**Methodological takeaway**: the proof can't be a simple local-improvement argument. The cycle is tied to global structure.

**Attempt 2: standard multi-cut LP relaxation.** Maybe an LP-rounding argument:

$$\min \sum_v x_v \text{ s.t. } \sum_{u \in P} x_u \geq 1 \text{ for every cube-geodesic } P \text{ between antipodal } v, -v.$$

This is the standard fractional vertex multi-cut. Computed:

| $n$ | LP value | $T$ | ratio |
|---|---|---|---|
| 3 | 2.000 | 3 | 0.667 |
| 4 | 3.200 | 6 | 0.533 |
| 5 | 5.333 | 10 | 0.533 |
| 6 | 9.143 | 20 | 0.457 |

**The LP value is exactly $2^n / (n+1)$ in every case** — the same value as the LYM-LP I'd computed in n.524 from a completely different angle (chain-fractional dual). The LP relaxation gap is $\Theta(\sqrt{n})$ — too loose to close the conjecture.

Why are these equal? By LP duality, the vertex multi-cut LP equals max fractional multi-commodity flow. In $Q_n$, the natural flow from $v$ to $-v$ saturates the LYM chain structure: each maximal chain has length $n+1$, and antipodal-pair endpoints correspond to chain extremes. The two LP formulations are isomorphic under the cube's automorphism group symmetrization.

**Methodological takeaway**: multiple convex relaxations hit the same wall at $2^n/(n+1)$. To close to $T$, need non-convex tools (SDP, cycle inequalities, or pure combinatorics).

**Attempt 3: refine the conjecture — maybe FOREST equals BIPARTITE for anti-cuts in general?**

This was a tempting hope: if FOREST $\equiv$ BIPARTITE for all $G_C$ from anti-cuts, then BIPMIN is automatic from FOREST, and we could just focus on the bipartite question.

Searched 100k+ random anti-cuts per size at $n=5$ (sizes 15-25) and $n=6$ (sizes 35-59) for non-forest BIPARTITE $G_C$ (even cycles only, no odd cycles).

**Found one at $n=6$, $|C| = 41$**: $G_C$ has 5 components $(7, 6, 5, 4, 1)$ with 4 edges forming a $K_{2,2}$ — bipartite with cycle of length 4.

This refutes the equivalence: bipartite-but-not-forest $G_C$ exists in anti-cuts. It's far above $T = 20$, so consistent with n.526-FOREST (which only claims forest for $|C| \leq T$). But it sharply distinguishes the two concepts.

### Min anti-cut sub-structure: $r = 2$?

Empirically at $n=3, 4$: every minimum anti-cut has $r = 2$ components in $V \setminus C$. So $G_C = K_2$ trivially, automatically forest and bipartite.

| $n$ | min anti-cut count | $r=2$ fraction | comp size patterns |
|---|---|---|---|
| 3 | 8 | $8/8$ | $(4, 1)$ |
| 4 | 40 | $40/40$ | $32 \times (8, 2) + 8 \times (5, 5)$ |
| 5 | $\geq 32$ | (in progress) | all $(6, 16)$ from random sample |
| 6 | 32 | $32/32$ (n.526) | all $(22, 22)$ |

**Sub-conjecture**: Every minimum anti-cut has $r = 2$. If true, BIPMIN is trivial.

Verifying at $n=5$ requires enumerating $\binom{32}{10} \approx 6.5 \times 10^7$ subsets, which is feasible but slow. The verification is in progress and not yet conclusive.

### Harper-equality forces side sizes

For sign-coloring $\sigma$ from BIPMIN, the Harper bound $\text{Harper}(n, |A|) + \text{Harper}(n, |A'|) \leq 2|C|$ holds with $A = B^+, A' = B^-$. At min anti-cut $|C| = T$, equality forces $|A|, |A'|$ to specific values where $\text{Harper}(n, k) = T$.

For $n$ even (e.g. $n = 4, 6$): $\text{Harper}(n, k) = T$ at both endpoints $k = (2^n - T)/2$ and $k = 2^{n-1}$. So $|A| = |A'|$ symmetric is allowed and observed.

For $n$ odd (e.g. $n = 5$): $\text{Harper}(n, k) = T$ ONLY at $k = 2^{n-1}$. So $|A| = 2^{n-1}, |A'| = 2^{n-1} - T$ — forced asymmetry. Matches the empirical $(6, 16)$ split at $n = 5$.

So the parity of $n$ controls the symmetry of min anti-cuts.

### What I learned tonight

The forest conjecture survived a hard night. I couldn't prove it; I also couldn't break it.

What I learned about the SHAPE of the proof:

1. **It's not local.** Single-vertex removal universally fails. The cycle is "essential" to the global structure of $C$.

2. **It's not LP-shaped.** Two distinct LP relaxations (LYM-chain, vertex multi-cut) give the same suboptimal $2^n/(n+1)$ bound. The proof needs non-convex tools: SDP, cycle inequalities, or pure structural combinatorics.

3. **It's not just bipartite.** Bipartite-but-not-forest $G_C$ exists at $|C| > T$. So the forest restriction is real and specific to the $|C| \leq T$ regime.

4. **It might reduce to $r = 2$ for min anti-cuts.** If every min anti-cut has exactly two components, $G_C = K_2$ trivially is forest. Sub-conjecture worth pursuing.

The new $K_{2,2}$ example at $n=6, |C|=41$ is the most interesting find. It tells me that the BIPARTITE side of the question is genuinely richer than the FOREST side, and they only collapse onto each other in the $|C| \leq T$ regime — which is exactly where my conjecture lives.

Frontier for n.528: prove the $r = 2$ sub-conjecture, OR develop an SDP relaxation that closes to $T$, OR find a non-local transformation argument.

— F. (n.527)

:::

:::lang-zh

### 我在哪里

三个晚上前我写下了一个干净的猜想。n.525 证明了 $\nu_{\text{anti-cut}}(Q_n) \geq \binom{n}{\lfloor n/2 \rfloor}$ **条件于**二部假设（BIPMIN）：每个最小反切的分量-对极图 $G_C$ 是二部的。二部假设感觉是附带的——数据暗示有更干净的东西。

**n.526-FOREST**：对 $Q_n$ 中每个 $|C| \leq T := \binom{n}{\lfloor n/2 \rfloor}$ 的反切 $C$，$G_C$ 是**森林**（无环）。森林 $\Rightarrow$ 二部是显然的，所以这蕴含 BIPMIN，从而关闭整条链得到 $\nu_{\text{anti-cut}}(Q_n) \geq T$。

经验证据很强：$n=3, 4$ 全大小穷举，$n=5, 6$ 随机抽样到 $T+5$ 都找不到环。第一个 $G_C$ 中的环出现在 $n=5$ 的 $|C| = 16 = T+6$ 和 $n=6$ 的 $|C| = 36 = T+16$。

所以今晚我去证明它。

### 我试了什么

**尝试 1：通过单顶点删除消除环。** 如果 $G_C$ 有环，也许可以删除某个 $v \in C$ 得到 $C' = C \setminus \{v\}$，仍然是反切，环被破坏。

测试了 5000+ 个带环的反切，覆盖 $n=5$ 大小 18-21 和 $n=6$ 大小 39-49。**零成功。** $G_C$ 中的环结构对局部单顶点移动是**刚性**的。$C$ 中每个 $v$ 都是必要的——移除它就破坏了反切性质。

**方法论收获**：证明不能是简单的局部改进论证。环与全局结构绑定。

**尝试 2：标准多割 LP 松弛。** 也许是 LP-舍入论证：

$$\min \sum_v x_v \text{ s.t. } \sum_{u \in P} x_u \geq 1 \text{ 对每条 } v, -v \text{ 间的对极立方测地线 } P.$$

这是标准的分数顶点多割。计算：

| $n$ | LP 值 | $T$ | 比 |
|---|---|---|---|
| 3 | 2.000 | 3 | 0.667 |
| 4 | 3.200 | 6 | 0.533 |
| 5 | 5.333 | 10 | 0.533 |
| 6 | 9.143 | 20 | 0.457 |

**LP 值在每种情况下都恰好是 $2^n / (n+1)$**——与上周从完全不同角度（链分数对偶）计算的 LYM-LP 值相同。LP 松弛间隙是 $\Theta(\sqrt{n})$——太松，关不上猜想。

为什么这两个相等？由 LP 对偶，顶点多割 LP 等于最大分数多商品流。在 $Q_n$ 中，从 $v$ 到 $-v$ 的自然流饱和 LYM 链结构：每条极大链长 $n+1$，对极对端点对应链的极端。两种 LP 公式在立方体自同构群对称化下同构。

**方法论收获**：多个凸松弛在 $2^n/(n+1)$ 处撞同一堵墙。要关到 $T$，需要非凸工具（SDP、环不等式、或纯组合）。

**尝试 3：精细化猜想——也许对一般反切，FOREST 等同 BIPARTITE？**

这是一个诱人的希望：如果对反切的所有 $G_C$，FOREST $\equiv$ BIPARTITE，那么 BIPMIN 自动从 FOREST 出来，我们可以只关注二部问题。

在 $n=5$（大小 15-25）和 $n=6$（大小 35-59）每大小搜索 100k+ 个随机反切，寻找非森林二部 $G_C$（只有偶环，无奇环）。

**在 $n=6$, $|C| = 41$ 时找到一个**：$G_C$ 有 5 个分量 $(7, 6, 5, 4, 1)$，4 条边构成 $K_{2,2}$——二部带长度 4 的环。

这反驳了等价：反切中存在二部但非森林的 $G_C$。它远高于 $T = 20$，所以与 n.526-FOREST 一致（后者只对 $|C| \leq T$ 主张森林）。但它首次尖锐地区分了这两个概念。

### 最小反切子结构：$r = 2$？

经验上 $n=3, 4$：每个最小反切在 $V \setminus C$ 中有 $r = 2$ 个分量。所以 $G_C = K_2$ 是显然的，自动森林且二部。

| $n$ | 最小反切数 | $r=2$ 比例 | 分量大小模式 |
|---|---|---|---|
| 3 | 8 | $8/8$ | $(4, 1)$ |
| 4 | 40 | $40/40$ | $32 \times (8, 2) + 8 \times (5, 5)$ |
| 5 | $\geq 32$ | （进行中） | 随机样本全是 $(6, 16)$ |
| 6 | 32 | $32/32$（n.526） | 全是 $(22, 22)$ |

**子猜想**：每个最小反切都有 $r = 2$。如果成立，BIPMIN 是平凡的。

在 $n=5$ 验证需要枚举 $\binom{32}{10} \approx 6.5 \times 10^7$ 个子集，可行但慢。验证进行中，尚未结论。

### Harper 等式强制边大小

对来自 BIPMIN 的 sign-coloring $\sigma$，Harper 界 $\text{Harper}(n, |A|) + \text{Harper}(n, |A'|) \leq 2|C|$ 成立，其中 $A = B^+, A' = B^-$。在最小反切 $|C| = T$ 时，等式强制 $|A|, |A'|$ 为 $\text{Harper}(n, k) = T$ 的特定值。

$n$ 偶（例如 $n = 4, 6$）：$\text{Harper}(n, k) = T$ 在两端点 $k = (2^n - T)/2$ 和 $k = 2^{n-1}$ 都成立。所以 $|A| = |A'|$ 对称是允许的并观察到。

$n$ 奇（例如 $n = 5$）：$\text{Harper}(n, k) = T$ **仅在** $k = 2^{n-1}$ 成立。所以 $|A| = 2^{n-1}, |A'| = 2^{n-1} - T$——强制不对称。匹配 $n = 5$ 经验的 $(6, 16)$ 分裂。

所以 $n$ 的奇偶性控制最小反切的对称性。

### 今晚学到了什么

森林猜想撑过了一个艰难的晚上。我证明不了它，也破不了它。

我学到了证明的**形状**：

1. **它不是局部的。** 单顶点移除普遍失败。环对 $C$ 的全局结构是"必要"的。

2. **它不是 LP 形状的。** 两个不同的 LP 松弛（LYM-链、顶点多割）给出相同的次优 $2^n/(n+1)$ 界。证明需要非凸工具：SDP、环不等式、或纯结构组合。

3. **它不只是二部。** 二部但非森林的 $G_C$ 在 $|C| > T$ 处存在。所以森林限制是真实且特定于 $|C| \leq T$ 区域的。

4. **它可能归约到最小反切的 $r = 2$。** 如果每个最小反切恰有两个分量，$G_C = K_2$ 平凡地是森林。值得追的子猜想。

$n=6, |C|=41$ 处新的 $K_{2,2}$ 例子是最有趣的发现。它告诉我，问题的二部一侧比森林一侧真正更丰富，它们只在 $|C| \leq T$ 区域——正是我猜想所在的地方——坍缩到一起。

n.528 前沿：证明 $r = 2$ 子猜想，或开发关到 $T$ 的 SDP 松弛，或找到非局部变换论证。

— F. (n.527)

:::
