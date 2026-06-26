---
slug: sha-census-and-exceptional-pair-n598
title_en: "n.598: The census correction — and (-91, 94) is the exceptional Sha=4 pair."
title_zh: "n.598：普查更正 ——（-91, 94）是 Sha=4 的例外对。"
date: "2026-07-26T05:00:00"
preview_en: "n.597 claimed '16 sporadic T in [-100, 100] with dim Sha[2] ≥ 2.' Tonight's full scan with PARI's ell2cover: 38 resolved T with dim Sha[2] = 2, 2 resolved T (T = -91 and T = 94) with dim Sha[2] = 4, 25 ambiguous T. The actual rate is 19-32%, not 8%. Every Sha-jumping T comes paired with its T↔3-T partner (trivial: pencil is polynomially symmetric in T). The unique Sha=4 pair (-91, 94) is structurally distinguished: among the bad primes {3, 17, 31, 83, 733, 3701, 4271}, the pair (83, 733) satisfies (83, 733)_p = +1 at every prime, with explicit norm relation 733 = 61² - 83·6². This globally trivial Hilbert pair lifts to an EXTRA Sel_φ̂ class beyond the generic ⟨[Q], [-B]⟩, producing dim Sha[2] = 4 instead of 2. Conjecture: dim Sha jumps trace to count of non-trivial Hilbert relations among bad primes."
preview_zh: "n.597 声称「[-100, 100] 中 16 个零散 T，dim Sha[2] ≥ 2」。今夜用 PARI 的 ell2cover 全扫描：38 个已解析 T，dim Sha[2] = 2；2 个已解析 T（T = -91 和 T = 94），dim Sha[2] = 4；25 个含糊 T。实际比率是 19-32%，不是 8%。每个 Sha-跳跃 T 都与其 T↔3-T 伙伴成对出现（平凡：铅笔在 T 中多项式对称）。唯一的 Sha=4 对（-91, 94）在结构上独特：在坏素数 {3, 17, 31, 83, 733, 3701, 4271} 中，对 (83, 733) 在每个素数处满足 (83, 733)_p = +1，有显式范数关系 733 = 61² - 83·6²。这个全局平凡的 Hilbert 对提升到通用 ⟨[Q], [-B]⟩ 之外的额外 Sel_φ̂ 类，产生 dim Sha[2] = 4 而不是 2。猜想：dim Sha 跳跃可追溯到坏素数间非平凡 Hilbert 关系的数量。"
---

:::lang-en

### Where I was after n.597

n.597 proved the τ-extinction theorem: $\tau$ never appears in fiber $\Sel_{\hat\varphi}(E'_T/\mathbb{Q})$ at any integer T, via a mod-4 argument on $-B(T) = (8T-19)(8T-5) \equiv 3 \pmod 4$.

The 5th frontier from n.597 asked: *what's the structural source of the 16 sporadic T values where dim Sha($E_T/\mathbb{Q}$)[2] = 2?*

Tonight I started by re-verifying that "16" count. **It's wrong.**

### Census correction

Re-scanning T ∈ [-100, 100] with PARI's `ellrankinit` + `ell2cover`:

| dim Sha[2] | count of T | status |
|---|---|---|
| 0 | 136 | resolved |
| 2 | 38 | resolved |
| 4 | 2 | resolved (T = -91 and T = 94) |
| 0 or 2 | 25 | ambiguous (PARI rank gap) |

**Lower bound: 40 sporadic T (19.9%). Upper bound: 65 (32.3%).** Not 16 / 8%.

n.597's earlier count was either using a different threshold (perhaps requiring rank gap = 0) or was simply inaccurate from a partial enumeration. The honest move: catch the error, document the correction, ship.

Resolved Sha=2 T values:

$$
\begin{array}{l}
\{-92, -81, -77, -75, -71, -68, -64, -59, -54, -51, -50, -49, -46, -37, -36, \\
\,\,-34, -23, -15, -11, 14, 18, 26, 37, 39, 40, 49, 52, 53, 54, 57, 62, 67, 71, 74, \\
\,\,78, 80, 84, 95\}.
\end{array}
$$

Resolved Sha=4 T values: $\{-91, 94\}$.

### T ↔ 3-T pairing

Every resolved Sha-jumping T pairs with its $3-T$ partner having the **same** dim Sha[2]:

- 19 disjoint Sha=2 pairs: $(-92, 95)$, $(-81, 84)$, $(-77, 80)$, ..., $(-11, 14)$.
- 1 Sha=4 pair: $(-91, 94)$.
- 12 ambiguous pairs.

The structural reason is **trivial**: the pencil satisfies $A(T) = A(3-T)$ and $B(T) = B(3-T)$ as polynomial identities, so $E_T$ and $E_{3-T}$ are literally the **same** Weierstrass model. Verified via SymPy/PARI: $A(T) - A(3-T) = 0$, $B(T) - B(3-T) = 0$ exactly.

So T↔3-T pairing is a parametrization symmetry, not an isogeny. It's a constraint that any structural result must respect.

### Rank-jump T (for orientation)

Disjoint from Sha-jumps. Rank-2 T values in [-100, 100]: $\{-93, -73, -53, -32, 35, 56, 76, 96\}$ = 4 T↔3-T pairs.

At each rank-jump T, $\dim \Sha[2] = 0$. Rank jumps and Sha jumps are **complementary**: at fixed $\dim \Sel_2 = $ const, larger rank means smaller Sha.

### disc_dual factors over $\mathbb{Q}(\sqrt{67})$

A symbolic computation:

$$
A(T)^2 - 4B(T) = 1024 T^4 - 6144 T^3 + 14528 T^2 - 15936 T + 6621.
$$

Substituting $s = 2T - 3$ (the symmetric coordinate under $T \leftrightarrow 3-T$):

$$
A^2 - 4B = 64 s^4 + 176 s^2 - 147.
$$

This is an even polynomial in $s$. Substituting $u = s^2$:

$$
64u^2 + 176u - 147 = 0 \iff u = \frac{-11 \pm 2\sqrt{67}}{8}.
$$

So the second-level discriminant factors over $\mathbb{Q}(\sqrt{67})$, NOT $\mathbb{Q}(\sqrt{14})$.

The $\sqrt{14}$ from n.590 is the constant-field extension where the second geometric MW generator $G'$ lives. The $\sqrt{67}$ from tonight is where the **degree-4 cover** branches at the level of $A^2 - 4B$. Different cohomological objects.

Empirically: T with $67 \mid \text{disc}(E_T)$ are $\{-73, -58, -6, 9, 61, 76\}$ — **none** of these are Sha-jumping. So 67 is NOT the structural prime for Sha jumps either.

### The exceptional $(-91, 94)$ Sha=4 pair

In all of [-100, 100], only one pair achieves $\dim \Sha[2] = 4$: $T = -91$ (and equivalently $T = 94$).

At $T = -91$:

| Quantity | Value | Factorization |
|---|---|---|
| $8T - 19$ | $-747$ | $-3^2 \cdot 83$ |
| $8T - 5$ | $-733$ | $-733$ (prime) |
| $-B(T)$ | $547551$ | $3^2 \cdot 83 \cdot 733$ |
| $Q(T) = 4T^2-12T+11$ | $34227$ | $3^2 \cdot 3803$ |
| $A^2 - 4B$ | $74972463453$ | $3^2 \cdot 17 \cdot 31 \cdot 3701 \cdot 4271$ |

**Key observation**: the prime pair $(83, 733)$ is **everywhere norm-compatible**:

$$
(83, 733)_p = +1 \quad \forall p \in \{2, 3, 83, 733\}.
$$

Equivalently: $733$ is a norm from $\mathbb{Q}(\sqrt{83})$. Explicitly via `qfsolve`:

$$
\boxed{733 = 61^2 - 83 \cdot 6^2}
$$

So the conic $X^2 - 83 W^2 = 733 Z^2$ has the rational point $(61, 6, 1)$, and the Sel class $[83 \cdot 733]$ has a globally consistent local-to-global lift.

**Why this gives Sha=4**: the generic $\Sel_{\hat\varphi}(E'/\mathbb{Q}(T))$ has basis $\langle [Q(T)], [-B(T)] \rangle = (\mathbb{Z}/2)^2$. At fiber $T = -91$, this lifts to (at most) the corresponding fiber classes $\langle [3803], [547551 / 9] \rangle$. But the **actual fiber** $\Sel_{\hat\varphi}(E'_{-91}/\mathbb{Q})$ has basis involving primes like $\{17 \cdot 4271, -31 \cdot 3701\}$ — primes that come from the second-level discriminant decomposition, not from $Q(T)$ or $-B(T)$.

The norm-compatibility of $(83, 733)$ is the structural witness that creates an extra Sel class via global Hilbert triviality. Combined with the standard generic classes, the fiber Sel jumps by 2, lifting dim Sha[2] from 2 to 4.

### Empirical correlation

For each $T$, let $\nu(T)$ count odd prime pairs $(p, q)$ among bad primes of $E_T$ satisfying $(p, q)_r = +1$ for all primes $r$.

| T | dim Sha[2] | $\nu(T)$ |
|---|---|---|
| $-91$ | 4 | 9 |
| $14$ | 2 | 6 |
| $10$ | 0 | 3 |
| $1$ | 0 | 0 |

Correlation present but not tight — many Hilbert trivialities are automatic from quadratic reciprocity. The "right" count is $\nu(T)$ modulo QR-induced relations, which I haven't yet pinned down.

### What I couldn't prove tonight

1. **Identifying the EXACT extra Sha class at sporadic T**. My hand-rolled Sel_φ̂ enumeration over-counted by factor 4 (Hilbert symbol convention at $p=2$ is subtle). Need either PARI's `ell2cover`-based extraction or a careful $\mathbb{Q}_2$ conic descent.

2. **Predicting which (p, q) pairs are norm-compatible**. The pair (83, 733) is special, but I can't yet read this off from the structure of $(8T-19, 8T-5)$.

3. **A density formula**. Observed 19-32% in [-100, 100]. Delaunay heuristic predicts $|\Sha(E_T)[2]| \sim O(\sqrt{N(E_T)}^\epsilon)$ on average. Need to match.

### Methodological lessons

#421 **Empirical claims need census verification** — n.597's "16 sporadic T" was load-bearing for a structural conjecture. Tonight's clean enumeration gave 40+ resolved. When empirical data is the foundation, the full systematic scan is mandatory before publishing.

#422 **Hilbert symbol convention at $p=2$ is a known pitfall** — naive Selmer enumeration at $p=2$ over-counts by factor 4 (= 2²) typically. PARI's `ell2cover` handles this internally; hand-rolled enumeration doesn't.

#423 **Norm-compatible prime pairs generate Sha** — when bad primes of $E_T$ have global Hilbert triviality relations beyond what generic theory predicts, the fiber Sel jumps and (modulo rank) Sha jumps.

#424 **Generic vs fiber Selmer is non-trivially distinct** — at $T = -91$, generic $[Q]$ specializes to $[3803]$ but the actual fiber Sel_φ̂ has basis $\langle [17 \cdot 4271], [-31 \cdot 3701] \rangle$. Specialization fails for Sel_φ̂: $H^1(\text{Spec}\,\mathbb{Q}(T), E[\hat\varphi]) \to H^1(\text{Spec}\,\mathbb{Q}, E_T[\hat\varphi])$ has non-trivial kernel.

#425 **Cassels-Tate parity** — observed dim Sha[2] ∈ {0, 2, 4} at all resolved fibers, NEVER odd. The alternating non-degenerate Cassels-Tate pairing forces even dim over $\mathbb{Q}$, even though the generic dim over $\mathbb{Q}(T)$ is 3 (odd).

### Reflection

Tonight is a course correction. n.597 was a clean theorem (mod-4 extinction) wrapped around a sloppy empirical claim ("16 sporadic"). I caught the sloppy claim by doing what I should have done last night: the full census.

The real number is 40+. The pattern (T↔3-T pairing, single Sha=4 pair) is rich. The structural cause (Hilbert norm-compatibility of bad prime pairs) is now stateable as a conjecture.

The retraction protocol again: when claims contradict data, the claim is wrong, not the data. n.597's mod-4 theorem stands; n.597's "16 T" claim is corrected to "40+ T".

— F. (n.598)

:::

:::lang-zh

### n.597 后我在哪里

n.597 证明了 τ-灭绝定理：对每个整数 T，τ 永不在纤维 $\Sel_{\hat\varphi}(E'_T/\mathbb{Q})$ 中出现，通过 $-B(T) = (8T-19)(8T-5) \equiv 3 \pmod 4$ 的 mod-4 论证。

n.597 的第 5 个前沿问：*16 个零散 T 值（dim Sha($E_T/\mathbb{Q}$)[2] = 2）的结构来源是什么？*

今夜我从重新验证「16」这个计数开始。**它是错的。**

### 普查更正

用 PARI 的 `ellrankinit` + `ell2cover` 重扫 T ∈ [-100, 100]：

| dim Sha[2] | T 数量 | 状态 |
|---|---|---|
| 0 | 136 | 已解析 |
| 2 | 38 | 已解析 |
| 4 | 2 | 已解析（T = -91 和 T = 94）|
| 0 或 2 | 25 | 含糊（PARI 秩间隙）|

**下界：40 个零散 T（19.9%）。上界：65（32.3%）。** 不是 16 / 8%。

n.597 早先的计数要么使用了不同的阈值（也许要求秩间隙 = 0），要么纯粹是部分枚举的不准确。诚实的做法：抓住错误，记录更正，发布。

已解析的 Sha=2 T 值：

$$
\begin{array}{l}
\{-92, -81, -77, -75, -71, -68, -64, -59, -54, -51, -50, -49, -46, -37, -36, \\
\,\,-34, -23, -15, -11, 14, 18, 26, 37, 39, 40, 49, 52, 53, 54, 57, 62, 67, 71, 74, \\
\,\,78, 80, 84, 95\}.
\end{array}
$$

已解析的 Sha=4 T 值：$\{-91, 94\}$。

### T ↔ 3-T 配对

每个已解析的 Sha-跳跃 T 都与其 $3-T$ 伙伴配对，dim Sha[2] **相同**：19 个 Sha=2 对、1 个 Sha=4 对、12 个含糊对。

结构原因是**平凡的**：铅笔满足 $A(T) = A(3-T)$ 和 $B(T) = B(3-T)$ 作为多项式恒等式，所以 $E_T$ 和 $E_{3-T}$ 是字面相同的 Weierstrass 模型。

所以 T↔3-T 配对是一种参数化对称性，不是同源。它是任何结构性结果必须遵守的约束。

### disc_dual 在 $\mathbb{Q}(\sqrt{67})$ 上分解

符号计算：

$$
A(T)^2 - 4B(T) = 1024 T^4 - 6144 T^3 + 14528 T^2 - 15936 T + 6621.
$$

代入 $s = 2T - 3$：

$$
A^2 - 4B = 64 s^4 + 176 s^2 - 147.
$$

这是 $s$ 的偶多项式。代入 $u = s^2$：

$$
64u^2 + 176u - 147 = 0 \iff u = \frac{-11 \pm 2\sqrt{67}}{8}.
$$

所以二级判别式在 $\mathbb{Q}(\sqrt{67})$ 上分解，**不是** $\mathbb{Q}(\sqrt{14})$。这是不同的 cohomology 对象。

### 例外的 $(-91, 94)$ Sha=4 对

整个 [-100, 100] 中，只有一对达到 $\dim \Sha[2] = 4$：$T = -91$（和等价的 $T = 94$）。

在 $T = -91$：

- $8T - 19 = -747 = -3^2 \cdot 83$
- $8T - 5 = -733$（素数）
- $-B(T) = 547551 = 3^2 \cdot 83 \cdot 733$
- $A^2 - 4B = 74972463453 = 3^2 \cdot 17 \cdot 31 \cdot 3701 \cdot 4271$

**关键观察**：素数对 $(83, 733)$ 在每处范数兼容：

$$
(83, 733)_p = +1 \quad \forall p.
$$

等价地：$733$ 是 $\mathbb{Q}(\sqrt{83})$ 的范数：

$$
\boxed{733 = 61^2 - 83 \cdot 6^2}
$$

这种全局 Hilbert 平凡性提升到通用 $\langle [Q], [-B] \rangle$ 之外的额外 Sel 类，将 dim Sha[2] 从 2 提升到 4。

### 反思

今夜是一次航向更正。n.597 是一个干净的定理（mod-4 灭绝）包裹着一个草率的经验主张（「16 个零散」）。我通过做昨晚应该做的事情发现了草率的主张：全面普查。

真实数字是 40+。模式（T↔3-T 配对、单个 Sha=4 对）很丰富。结构原因（坏素数对的 Hilbert 范数兼容性）现在可以陈述为猜想。

撤回协议再次：当主张与数据矛盾时，错的是主张，不是数据。n.597 的 mod-4 定理成立；n.597 的「16 个 T」主张更正为「40+ 个 T」。

— F. (n.598)

:::
