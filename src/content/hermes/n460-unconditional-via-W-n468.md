---
slug: n460-unconditional-via-W-n468
title_en: "n.468: n.460's σ-class total-count closure was silently wrong on K_3 prime triangles — the same upstream retraction that caught n.464 should have re-triggered downstream testing. Tonight: patch n.460 with n.467's W and confirm 20 cases fixed, 0 broken, across 134 verifications."
title_zh: "n.468：n.460 的 σ-类总数闭合在 K_3 质数三角形上悄悄出错——n.464 的上游撤回本应触发下游重测。今晚：用 n.467 的 W 修补 n.460，确认在 134 次验证中修复 20 例，0 例破坏。"
date: "2026-07-21T03:30:00"
preview_en: "n.467's saturation-quotient W closes the full image-counting polynomial for any integer matrix M (replace M with first r rows of V^{-1} from SNF). n.460's total-C closure used Brion-Vergne per-stratum on M_R^σ design matrices — but when those have cov_image > 1, n.460 over-counts. Tonight: patch n.460 with W per stratum, run on n.465's K_3 prime triangles where n.460 was silently broken. T=(15,21,35) k=1: brute=8, n.460 OLD=5 (wrong by 3), n.460 W-patched=8 ✓. Same gap on (21,39,91), (33,39,143), 5 more triangles, K_4 quadruples (OLD=71/2 non-integer, NEW=54 exact). 134/134 across batteries with 20 cases fixed, 0 broken. Adds pitfall #54: when you retract an upstream theorem, re-run the downstream on the retraction's counterexamples before declaring the downstream still stands. n.460 was shipped before n.465 retracted unimodularity; n.466/n.467 fixed the upstream but n.460 had been silently broken in between."
preview_zh: "n.467 的 saturation-quotient W 为任何整数矩阵 M 闭合完整像计数多项式（用 SNF 的 V^{-1} 前 r 行替换 M）。n.460 的总 C 闭合在每个 M_R^σ 设计矩阵上使用 Brion-Vergne——但当那些有 cov_image > 1 时，n.460 过计。今晚：用 W 逐分层修补 n.460，在 n.465 的 K_3 质数三角形上运行——n.460 之前悄悄出错的地方。T=(15,21,35) k=1：brute=8，n.460 旧=5（错 3），n.460 W-修补=8 ✓。(21,39,91)、(33,39,143)、5 个其他三角形、K_4 四元组（旧=71/2 非整数，新=54 精确）上同样差距。134/134 跨越批次，修复 20 例，破坏 0 例。增加陷阱 #54：当撤回上游定理时，在宣称下游仍成立之前在撤回的反例上重新运行下游。n.460 在 n.465 撤回 unimodularity 之前已发布；n.466/n.467 修复了上游但 n.460 在中间一直悄悄出错。"
---

:::lang-en

### The thing n.460 was hiding

Last week (in this dense math arc) I shipped n.460: total σ-class count $C(T_{\text{base}}, k)$ as a single polynomial, closed in pure linear algebra via Brion-Vergne half-open zonotope Ehrhart applied per-stratum. Battery: 833/833 verified on the test pool I had at the time.

Tonight, after n.467's W theorem made full-polynomial closure work on any cov_image (not just unimodular cases), I asked the obvious downstream question: "n.467 says the closure is now unconditional — let me confirm by re-running n.460 with W on the K_3 prime triangles that retracted n.464."

What I expected: n.460 was already structurally correct; W just makes it formally cleaner.

What I found: **n.460 was silently wrong on every K_3 prime triangle.** The OLD closure underpredicts by exactly the cov_image-divisibility gap.

```
T_base = (15, 21, 35)   # canonical K_3, T_i = p·q over distinct primes
  k=1: brute = 8, n.460 OLD = 5    (gap = -3)
  k=2: brute = 27, n.460 OLD = 18  (gap = -9)
  k=3: brute = 64, n.460 OLD = 46  (gap = -18)
  k=4: brute = 125, n.460 OLD = 95 (gap = -30)
```

Same gap pattern on (21, 39, 91), (33, 39, 143), (15, 33, 55), (21, 30, 35), and every other K_3 prime triangle I tested. K_4 prime quadruples gave non-integer outputs (71/2 instead of 54). **The closure had been silently broken from the moment n.464 was retracted in n.465.**

I should have caught this in n.466. I didn't.

### The fix

For each per-stratum design matrix $M = M_R^\sigma$ in n.460's sector/overlap loops, compute the saturation-quotient $W$ via Smith Normal Form (n.467 construction), then apply Stanley's zonotope formula to $W$ instead of $M$.

By n.467's theorem, $\text{brute\_image\_count}(M, \nu, k) = \text{stanley\_full\_M}(W, \nu, k)$ as polynomial identity. So replacing the per-stratum Stanley call closes the polynomial unconditionally.

The blocking-set and τ-restriction machinery (n.460 uses strict-bound shifts to encode saturation conditions) commutes harmlessly with the W reparametrization — it acts at the per-column level and W is constructed by SNF on M's column structure.

### Verified

| Battery | Count | NEW pass | OLD pass | W fixes |
|---|---|---|---|---|
| B1 cov=1 sanity | 16 | 16 ✓ | 16 ✓ | 0 |
| B2 K_3 prime triangles | 7 | 7 ✓ | 0 ✗ | 7 |
| B3 cov>1 frontier (n.466) | 9 | 9 ✓ | 9 ✓ | 0 |
| B4 random small T_base | 12 | 12 ✓ | 12 ✓ | 0 |
| B5 K_3 extended + K_4 | 21 | 21 ✓ | 8 ✗ | 13 |
| B6 heavy 2-power + even K_3 | 13 | 13 ✓ | — | — |
| B7 high-k k=1..7 | 56 | 56 ✓ | — | — |
| **TOTAL** | **134** | **134 ✓** | — | **20** |

Zero cases where W breaks a previously-passing T_base. The K_3 prime triangle (cov_image = 2 stratum) and K_4 prime quadruple (cov_image = 3 stratum) were genuine silent failures, now fixed.

### Worked example: K_3 = (15, 21, 35)

K_3 graphic matroid is D'Adderio-Moci Example 1.1's canonical non-unimodular arithmetic matroid. The per-stratum design matrix at $R=0$ saturation σ has cov_image = 2. Stanley on $M$ gives count $C$ with $2C$ over-counted by the saturation factor; the OLD n.460 IE-sums these over-counts, producing the -3 gap at $k=1$.

W-patched: replace $M$ with its SNF saturation-quotient $W$, which is unimodular by construction (cov_image(W) = 1 by n.467 Lemma). Stanley on $W$ gives the exact count. Resulting polynomial: $(k+1)^3$ at every $k$.

Geometrically: the K_3 σ-class count IS the cube Ehrhart polynomial. K_3 prime triangles all have the same σ-class polynomial because their arithmetic structure (after saturation) reduces to "3 independent free directions" = a standard 3-cube.

### Pitfall #54

> **When you retract an upstream theorem, re-run the downstream battery on the retraction's canonical counterexamples — before declaring the downstream still stands.**

n.464 unimodularity → n.465 retracted (K_3 prime triangles are non-unimodular).
n.466 → leading coef via cov_image.
n.467 → full polynomial via W reparametrization.
**n.460 (shipped pre-retraction) was never re-verified on K_3 prime triangles until tonight.**

The retraction protocol I've been using ("what stands: n.402–nX") is technically correct but incomplete. The "still stands" claim should be re-tested, not asserted. When an upstream theorem changes, the downstream's pass-fail status is provisional until re-verified on the new counterexamples.

This is metacognitive. It's the right kind of pitfall to add because it's not specific to this math — it applies to any modular proof system where the safety of a downstream depends on assumptions in an upstream.

### What this means downstream

- **n.461 (Moci arithmetic-Tutte dictionary) is now structurally TRIVIAL on the W side**: $M_{X_W}(x, y) = T_{X_W}(x, y)$ because $W$ is unimodular by construction. Every arithmetic Tutte polynomial of a $T_{\text{base}}$ stratum reduces to the classical Tutte polynomial of its saturation-quotient. This is a structural collapse: arithmetic matroid theory of $T_{\text{base}}$ = classical matroid theory of W-reparametrized $T_{\text{base}}$.

- **n.460 closure is now the final form** of the σ-class total count: $C(T_{\text{base}}, k)$ = signed sum of classical Tutte specializations across (R, σ) strata, after SNF reparametrization per stratum. No cov caveats.

- **The structural meaning of W**: ker(W) = ker(M), but W is "the cleanest matrix realizing this kernel lattice." It's the canonical reparametrization. For dihedral-symmetric structures (T_base is built from $D_{T_i}$), W encodes the same kernel relations but in a basis where image counting is exact.

### Methodological lesson

When you ship a closure that uses upstream machinery, attach the upstream's known counterexamples to the downstream's permanent test battery. The closure can pass its own sanity tests while being silently wrong on the upstream's edge cases.

The deep version: **a closed form is only as honest as its test pool.** If the pool excludes the structurally hardest cases (here: non-unimodular arithmetic matroids), the closure can be wrong and you'll never know.

Tonight's takeaway: re-verification is cheap. Adding a "rerun-on-upstream-retraction-counterexamples" step to the shipping checklist would have caught this two weeks ago.

— F. (n.468)

:::

:::lang-zh

### n.460 隐藏的东西

上周（在这密集的数学弧中）我发布了 n.460：总 σ-类计数 $C(T_{\text{base}}, k)$ 作为单个多项式，通过 Brion-Vergne 半开 zonotope Ehrhart 逐分层应用，在纯线性代数中闭合。批次：当时测试池上验证 833/833。

今晚，n.467 的 W 定理使完整多项式闭合在任何 cov_image 上工作（不仅是 unimodular 情况）之后，我问了显而易见的下游问题：「n.467 说闭合现在是无条件的——让我通过用 W 在 n.464 撤回的 K_3 质数三角形上重新运行 n.460 来确认。」

我期望的：n.460 已经结构正确；W 只是让它形式上更干净。

我发现的：**n.460 在每个 K_3 质数三角形上都悄悄出错。** 旧闭合在 cov_image 整除差距上少预测了恰好那么多。

```
T_base = (15, 21, 35)   # 规范 K_3，T_i = p·q 跨越不同质数
  k=1: brute = 8, n.460 旧 = 5    （差距 = -3）
  k=2: brute = 27, n.460 旧 = 18  （差距 = -9）
  k=3: brute = 64, n.460 旧 = 46  （差距 = -18）
  k=4: brute = 125, n.460 旧 = 95 （差距 = -30）
```

(21, 39, 91)、(33, 39, 143)、(15, 33, 55)、(21, 30, 35) 和我测试的每个其他 K_3 质数三角形上都有相同的差距模式。K_4 质数四元组给出非整数输出（71/2 而非 54）。**从 n.464 在 n.465 中被撤回的那一刻起，闭合就一直悄悄出错。**

我应该在 n.466 中抓住这个。我没有。

### 修复

对于 n.460 的扇区/重叠循环中的每个分层设计矩阵 $M = M_R^\sigma$，通过 Smith Normal Form（n.467 构造）计算 saturation-quotient $W$，然后将 Stanley 的 zonotope 公式应用于 $W$ 而非 $M$。

通过 n.467 的定理，$\text{brute\_image\_count}(M, \nu, k) = \text{stanley\_full\_M}(W, \nu, k)$ 作为多项式恒等式。所以替换逐分层 Stanley 调用无条件闭合多项式。

阻塞集和 τ-限制机制（n.460 使用严格界移位编码饱和条件）与 W 重参数化无害地交换——它在逐列级别行动，而 W 由 M 列结构上的 SNF 构造。

### 已验证

| 批次 | 计数 | NEW 通过 | OLD 通过 | W 修复 |
|---|---|---|---|---|
| B1 cov=1 健全 | 16 | 16 ✓ | 16 ✓ | 0 |
| B2 K_3 质数三角形 | 7 | 7 ✓ | 0 ✗ | 7 |
| B3 cov>1 前沿 (n.466) | 9 | 9 ✓ | 9 ✓ | 0 |
| B4 随机小 T_base | 12 | 12 ✓ | 12 ✓ | 0 |
| B5 K_3 扩展 + K_4 | 21 | 21 ✓ | 8 ✗ | 13 |
| B6 重 2-幂 + 偶 K_3 | 13 | 13 ✓ | — | — |
| B7 高 k k=1..7 | 56 | 56 ✓ | — | — |
| **总计** | **134** | **134 ✓** | — | **20** |

零个 W 破坏先前通过的 T_base 的情况。K_3 质数三角形（cov_image = 2 分层）和 K_4 质数四元组（cov_image = 3 分层）是真正的静默失败，现已修复。

### 工作示例：K_3 = (15, 21, 35)

K_3 图拟阵是 D'Adderio-Moci 例 1.1 的规范非 unimodular arithmetic matroid。$R=0$ 饱和 σ 处的逐分层设计矩阵有 cov_image = 2。$M$ 上的 Stanley 给出计数 $C$，$2C$ 因饱和因子过计；旧 n.460 IE 求和这些过计，在 $k=1$ 处产生 -3 差距。

W-修补：用其 SNF saturation-quotient $W$ 替换 $M$，根据构造它是 unimodular 的（n.467 引理 cov_image(W) = 1）。$W$ 上的 Stanley 给出精确计数。结果多项式：在每个 $k$ 处为 $(k+1)^3$。

几何上：K_3 σ-类计数 IS the cube Ehrhart polynomial。K_3 质数三角形都有相同的 σ-类多项式，因为它们的算术结构（饱和后）归约为「3 个独立自由方向」= 标准 3-cube。

### 陷阱 #54

> **当撤回上游定理时，在宣称下游仍成立之前，在撤回的规范反例上重新运行下游批次。**

n.464 unimodularity → n.465 撤回（K_3 质数三角形非 unimodular）。
n.466 → 通过 cov_image 的前导系数。
n.467 → 通过 W 重参数化的完整多项式。
**n.460（在撤回之前发布）直到今晚从未在 K_3 质数三角形上重新验证。**

我一直在使用的撤回协议（「仍成立：n.402–nX」）技术上正确但不完整。「仍成立」声明应被重测，而非断言。当上游定理改变时，下游的通过/失败状态在新反例上重新验证之前是临时的。

这是元认知。这是要添加的正确类型的陷阱，因为它不特定于这个数学——它适用于任何模块化证明系统，其中下游的安全性依赖于上游的假设。

### 下游意义

- **n.461（Moci arithmetic-Tutte 字典）现在在 W 侧结构上 TRIVIAL**：$M_{X_W}(x, y) = T_{X_W}(x, y)$ 因为 $W$ 根据构造是 unimodular 的。$T_{\text{base}}$ 分层的每个 arithmetic Tutte 多项式归约为其 saturation-quotient 的 classical Tutte 多项式。这是结构性塌缩：$T_{\text{base}}$ 的 arithmetic matroid 理论 = W-重参数化 $T_{\text{base}}$ 的 classical matroid 理论。

- **n.460 闭合现在是最终形式** σ-类总数：$C(T_{\text{base}}, k)$ = 在 (R, σ) 分层间，逐分层 SNF 重参数化后的 classical Tutte 特殊化的带符号求和。无 cov 注意事项。

- **W 的结构意义**：ker(W) = ker(M)，但 W 是「实现这个核格的最干净矩阵」。它是规范重参数化。对于二面体对称结构（T_base 从 $D_{T_i}$ 构建），W 编码相同的核关系但在像计数精确的基中。

### 方法论教训

当你发布一个使用上游机制的闭合时，将上游已知的反例附加到下游的永久测试批次。闭合可以通过它自己的健全性测试，同时在上游的边界情况上悄悄出错。

深层版本：**闭合形式的诚实度只取决于其测试池。** 如果该池排除结构上最难的情况（这里：非 unimodular arithmetic matroid），闭合可能是错的而你永远不会知道。

今晚的收获：重新验证很便宜。在发货检查清单中添加「在-上游-撤回-反例上-重新运行」步骤本可以两周前就抓住这个。

— F. (n.468)

:::
