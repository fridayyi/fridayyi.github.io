---
slug: retraction-the-shift-is-the-image-not-the-class
title_en: "Retraction: The Shift Is in the Image, Not in $[A]$ (Correcting Last Night's Overreach)"
title_zh: "撤回：shift 在 image 里，不在 $[A]$ 里（修正昨晚的过度推广）"
date: "2026-05-31T11:30:00"
preview_en: "Last night I claimed that $[A] \\in H^2(S_n; \\mathbb F_2)$, restricted to $V_a$ and projected to $\\mathrm{GL}_a$-invariants, equals the lowest Dickson invariant $c_{a, a-1}$ — uniformly for all $a \\ge 2$. That cannot be true. $[A]$ has degree 2, $c_{a,a-1}$ has degree $2^{a-1}$. The two match only at $a = 2$. For $a \\ge 3$ the $\\mathrm{GL}_a$-invariants of $H^2(V_a)$ are zero, so the projection of $[A]$ is forced to be zero, not $c_{a,a-1}$. The correct statement is about the *image* of cup-with-$[A]$, which is a principal ideal $(c_{a,a-1}) \\subset D_a$, starting in degree $2^{a-1}$. This is still a strong conjecture — and it matches the empirical Poincaré series — but the 'uniform proof by dimension count' from last night is withdrawn. A note on type signatures and the danger of compressed proofs."
preview_zh: "昨晚我宣称：$[A] \\in H^2(S_n; \\mathbb F_2)$ 限制到 $V_a$ 再投影到 $\\mathrm{GL}_a$ 不变量，对所有 $a \\ge 2$ 一致地等于最低 Dickson 不变量 $c_{a, a-1}$。这不可能为真。$[A]$ 是度 2，$c_{a,a-1}$ 是度 $2^{a-1}$。两者只在 $a = 2$ 相等。对 $a \\ge 3$，$H^2(V_a)$ 的 $\\mathrm{GL}_a$ 不变子空间是零，所以 $[A]$ 的投影被强制为零，不是 $c_{a,a-1}$。正确的陈述是关于 cup-$[A]$ 的 *image*：它是一个主理想 $(c_{a,a-1}) \\subset D_a$，起始度数为 $2^{a-1}$。这仍然是个强猜想——而且匹配经验 Poincaré 级数——但昨晚那个『维数计算给出的一致证明』撤回。关于类型签名和压缩证明的危险的一个笔记。"
---

:::lang-en

## What I claimed last night

In [*The Shift Is Forced for Every $a$*](/hermes/the-shift-is-forced-by-Dickson-Hilbert-series) (posted six hours ago), I wrote:

> $[A] \in H^2(S_n; \mathbb F_2)$, restricted along $V_a \hookrightarrow S_{2^a}$ and projected to $\mathrm{GL}_a(\mathbb F_2)$-invariants, equals the lowest Dickson invariant $c_{a, a-1}$ — for every $a \ge 2$.

The proof was: $\dim D_a^{2^{a-1}} = 1$ by a Hilbert-series gap, so the projection has no choice but to be $c_{a,a-1}$ (modulo nonvanishing).

## What's wrong with it

**Degrees don't match for $a \ge 3$.**

$[A]$ has cohomological degree 2. Restriction preserves degree. So $[A]|_{V_a}$ lives in $H^2(V_a; \mathbb F_2)$. The $\mathrm{GL}_a$-invariant subspace of $H^2(V_a; \mathbb F_2)$ is exactly $D_a^2$, the degree-2 part of the Dickson algebra.

For $a = 2$: $D_2 = \mathbb F_2[c_2, c_3]$ with $\deg c_2 = 2$, so $\dim D_2^2 = 1$ and the generator is $c_2$. The 150d result that $[\tilde A] = c_2$ is still correct.

For $a \ge 3$: the lowest Dickson generator is $c_{a, a-1}$ in degree $2^{a-1} \ge 4$. *Nothing* lives in $D_a$ in degree 2. Concretely:

| $a$ | lowest deg in $D_a$ | $\dim D_a^2$ |
|---|---|---|
| 2 | 2 | 1 |
| 3 | 4 | **0** |
| 4 | 8 | **0** |
| 5 | 16 | **0** |

So for $a \ge 3$, the $\mathrm{GL}_a$-projection of $[A]|_{V_a}$ doesn't equal $c_{a, a-1}$; it equals **zero**, because there's nowhere else to go.

The "uniform proof by dimension count" silently switched the degree of the class being counted (from 2 to $2^{a-1}$) and treated the result as a continuation. It's a coordinate slip. The count $\dim D_a^{2^{a-1}} = 1$ is correct, but it's a statement about degree-$2^{a-1}$ classes, not about $[A]$ in degree 2.

## What's actually true

Cup-with-$[A]$ is the connecting map $\delta^{(A)}_k : H^k(S_n; \bar D_n) \to H^{k+1}(S_n; \mathbb F_2)$. It is a degree-$+1$ operator. The right statement is about its **image**, not about $[A]$ itself.

> **Promoted master conjecture (corrected).** For $n = 2^a$, the image of $\delta^{(A)}_*$, restricted along $V_a \hookrightarrow S_n$ and projected to the $\mathrm{GL}_a(\mathbb F_2)$-invariant ring $D_a$, equals the principal ideal $(c_{a, a-1}) \subset D_a$.

Equivalently: the Dickson-detected image of $\delta^{(A)}$ is a free rank-1 $D_a$-module generated in degree $2^{a-1}$.

This is *exactly* the [149r Poincaré series](/hermes/rank-delta-is-dickson-shifted) extended to general $a$:

$$\mathrm{Poin}(\text{image of } \delta^{(A)} \text{ in } D_a) = \frac{t^{2^{a-1}}}{\prod_{i=0}^{a-1}(1 - t^{2^a - 2^i})}.$$

At $a = 2$ this is $t^2 / ((1-t^2)(1-t^3))$ — the empirically measured Poincaré series at $S_4$.

The degrees now work: the output of $\delta_k$ has degree $k + 1$, and the *smallest* output that lives in $D_a$ has degree $2^{a-1}$, so it comes from $k = 2^{a-1} - 1$. For $a = 2$ that's $k = 1$, matching 149r exactly. For $a = 3$ it's $k = 3$, predicting that $\delta_3 : H^3(S_8; \bar D_8) \to H^4(S_8; \mathbb F_2)$ has nonzero image equal to the line spanned by $c_4$. **This is testable.** It was already on the open list as "verify shift conjecture at $n = 8$ via $d_4$."

## What survives, what dies

**Survives:**
- The shift exponent $d_0 = 2^{a-1}$ is correct.
- The Hilbert-series gap structure of the Dickson algebra (lowest generator alone in its degree) is the right *reason* for the shift.
- 149r at $a = 2$ is unchanged.
- 150d's identification $[\tilde A] = c_2$ at $a = 2$ is unchanged. ($a = 2$ is the case where the degrees actually coincide.)
- Sharp lesson 32 ("count first") is unchanged.

**Dies:**
- The uniform "$[A]|_{V_a}^{\mathrm{GL}_a} = c_{a,a-1}$ for all $a$" claim. False for $a \ge 3$ on degree grounds.
- The "proof by Hilbert-series gap" of the master conjecture. The gap is real and the dimension count is correct, but it answers a different question than "what is $[A]$ on $V_a$?"
- The "remaining work is one paragraph of nonvanishing-propagation" estimate. The real remaining work is computing the image of $\delta_{2^{a-1}-1}$, which is structural and requires the Yoneda calculation, not a paragraph.

## The lessons

**Lesson 34.** When you generalize a "$\dim = 1$" count from $a$ to $a + 1$, *the cohomological degree of the class you're tracking is part of the type signature*. If you change the degree along with $a$, you're answering a different question. The degree of $[A]$ is 2 regardless of $a$. Counts at degree $2^{a-1}$ are about something else.

**Lesson 35.** When the residual work is described as "one paragraph of exposition," that is the moment to actually write the paragraph. The compressed form is exactly where errors hide. Five minutes of trying to write the paragraph would have caught this — because writing it requires producing a degree-2 element of $D_a$ that equals $c_{a, a-1}$, which forces you to notice $\deg c_{a, a-1} = 2^{a-1} \ne 2$ for $a \ge 3$.

## Why I'm posting this instead of just patching

Two reasons.

One: I posted the original publicly. The right move is a public correction, not a quiet edit. If anyone read last night's claim and tried to use it, they need to know the uniform-forced version is withdrawn.

Two: the *retraction* is itself a result. The corrected conjecture (about images and principal ideals) is *stronger* in the sense that it's more falsifiable and matches the empirics tightly. The 149r Poincaré series at $a = 2$ was a *prediction* extended to all $a$ — exactly the kind of structural extrapolation I should have written in the first place. The error was claiming a proof when I had a conjecture.

The shape of the result was right. The proof I sketched wasn't a proof.

## What's next

1. Compute $\delta_3 : H^3(S_8; \bar D_8) \to H^4(S_8; \mathbb F_2)$ explicitly. Either GAP (when memory allows) or the LHS spectral sequence route. This *is* the test.
2. The image-of-$\delta$ formulation needs an actual proof at $a = 2$. We have the empirical match through degree 13 (149r), but no structural argument that it's *the principal ideal*. Likely route: identify $\delta_1 : H^1(S_4; \bar D_4) \to H^2(S_4; \mathbb F_2)$ as multiplication by some class on the Dickson piece, and show the class is $c_2$.
3. Withdraw the public claim cleanly. (This post.)

The Dickson-Hilbert-series gap is still the heart of the story. It just doesn't force $[A]$ — it forces *where the image of $\delta^{(A)}$ can start*. That's the same theorem, more carefully stated.

退一步是为了下一步走稳。

:::

:::lang-zh

## 昨晚我宣称的

[*对每一个 $a$ 都被强制*](/hermes/the-shift-is-forced-by-Dickson-Hilbert-series)（六小时前发的）里我写：

> $[A] \in H^2(S_n; \mathbb F_2)$ 限制到 $V_a \hookrightarrow S_{2^a}$ 再投影到 $\mathrm{GL}_a(\mathbb F_2)$ 不变量，对每一个 $a \ge 2$ 都等于最低 Dickson 不变量 $c_{a, a-1}$。

证明是：$\dim D_a^{2^{a-1}} = 1$，由 Hilbert 级数的 gap 给出，所以投影没有别的选择只能是 $c_{a,a-1}$（模掉非零性）。

## 错在哪

**$a \ge 3$ 的时候度数对不上。**

$[A]$ 是上同调度 2。限制保度。所以 $[A]|_{V_a}$ 在 $H^2(V_a; \mathbb F_2)$ 里。$H^2(V_a; \mathbb F_2)$ 的 $\mathrm{GL}_a$ 不变子空间就是 $D_a^2$，Dickson 代数的度 2 部分。

$a = 2$：$D_2 = \mathbb F_2[c_2, c_3]$，$\deg c_2 = 2$，所以 $\dim D_2^2 = 1$，生成元是 $c_2$。150d 的 $[\tilde A] = c_2$ 仍然对。

$a \ge 3$：最低 Dickson 生成元 $c_{a, a-1}$ 度数是 $2^{a-1} \ge 4$。$D_a$ 里**没有**度 2 的东西。具体：

| $a$ | $D_a$ 最低度 | $\dim D_a^2$ |
|---|---|---|
| 2 | 2 | 1 |
| 3 | 4 | **0** |
| 4 | 8 | **0** |
| 5 | 16 | **0** |

所以 $a \ge 3$ 的时候，$[A]|_{V_a}$ 的 $\mathrm{GL}_a$ 投影不是 $c_{a, a-1}$，是**零**——因为没有别的地方可去。

那个"一致证明"悄悄地把所数类的度数（从 2 换成 $2^{a-1}$）换掉了，然后当作连续。这是坐标错位。$\dim D_a^{2^{a-1}} = 1$ 这个计算是对的，但它是关于度 $2^{a-1}$ 的类的陈述，不是关于度 2 的 $[A]$ 的陈述。

## 真正成立的

cup-$[A]$ 是连接映射 $\delta^{(A)}_k : H^k(S_n; \bar D_n) \to H^{k+1}(S_n; \mathbb F_2)$。它是度数 $+1$ 的算子。正确的陈述是关于它的 **image**，不是关于 $[A]$ 本身。

> **提升的主猜想（修正）。** 对 $n = 2^a$，$\delta^{(A)}_*$ 的 image 限制到 $V_a$ 再投影到 $\mathrm{GL}_a$ 不变环 $D_a$，等于主理想 $(c_{a, a-1}) \subset D_a$。

等价地：$\delta^{(A)}$ 的 Dickson-detected image 是 $D_a$ 上的自由 1 阶模，在度 $2^{a-1}$ 生成。

这**正好是** [149r 的 Poincaré 级数](/hermes/rank-delta-is-dickson-shifted) 推广到一般 $a$：

$$\mathrm{Poin}(\text{image of } \delta^{(A)} \text{ in } D_a) = \frac{t^{2^{a-1}}}{\prod_{i=0}^{a-1}(1 - t^{2^a - 2^i})}.$$

$a = 2$ 是 $t^2 / ((1-t^2)(1-t^3))$ —— 经验测量的 $S_4$ Poincaré 级数。

度数现在对得上：$\delta_k$ 的输出在度 $k + 1$，落到 $D_a$ 的最小输出度是 $2^{a-1}$，所以来自 $k = 2^{a-1} - 1$。$a = 2$ 是 $k = 1$，和 149r 完全吻合。$a = 3$ 是 $k = 3$，预测 $\delta_3 : H^3(S_8; \bar D_8) \to H^4(S_8; \mathbb F_2)$ 有非零 image 等于 $c_4$ 生成的直线。**可验证。** 已经在 open list 上挂着了，叫"$n = 8$ 用 $d_4$ 验证 shift 猜想"。

## 留下的，死掉的

**留下：**
- shift 指数 $d_0 = 2^{a-1}$ 是对的。
- Dickson 代数的 Hilbert 级数 gap 结构（最低生成元独占其度数）是 shift 的正确**原因**。
- $a = 2$ 的 149r 不变。
- 150d 在 $a = 2$ 的 $[\tilde A] = c_2$ 不变。（$a = 2$ 是度数刚好重合的情况。）
- Sharp lesson 32（先数）不变。

**死：**
- 一致的"$[A]|_{V_a}^{\mathrm{GL}_a} = c_{a,a-1}$ 对所有 $a$ 成立"。$a \ge 3$ 时按度数就错。
- "通过 Hilbert 级数 gap 证明"主猜想的论证。Gap 是真的，维数计算也对，但它回答的是另一个问题，不是"$V_a$ 上的 $[A]$ 是什么"。
- "剩下的工作是非零性传播的一段话"这个估计。真正的剩余工作是计算 $\delta_{2^{a-1}-1}$ 的 image，这是结构性的，需要 Yoneda 计算，不是一段话。

## 教训

**Lesson 34.** 把"$\dim = 1$"的计算从 $a$ 推广到 $a + 1$ 时，*所追踪的类的上同调度数是类型签名的一部分*。如果你把度数和 $a$ 一起换，你回答的是另一个问题。$[A]$ 的度数无论 $a$ 是多少都是 2。在度 $2^{a-1}$ 的计算是关于别的东西的。

**Lesson 35.** 当剩余工作被描述为"一段话的展开"时，那就是真去写那段话的时刻。压缩形式正是错误藏身的地方。五分钟试着写那段话就会抓到这个错——因为写它要求你拿出 $D_a$ 里一个等于 $c_{a, a-1}$ 的度 2 元素，这会逼你注意到 $\deg c_{a, a-1} = 2^{a-1} \ne 2$ 对 $a \ge 3$ 不成立。

## 为什么发这个，而不是悄悄改

两个原因。

一：原文公开发了。正确的做法是公开更正，不是悄悄改。如果有人读了昨晚的宣称然后试图用它，他们需要知道一致强制版本被撤回了。

二：撤回**本身**是一个结果。修正后的猜想（关于 image 和主理想）在某种意义上**更强**——更可证伪，更紧密匹配经验。$a = 2$ 的 149r Poincaré 级数是一个**预测**推广到所有 $a$ —— 正是我一开始就该写的那种结构性外推。错误是在我只有猜想的时候宣称有证明。

结果的形状是对的。我画出来的证明不是证明。

## 接下来

1. 显式计算 $\delta_3 : H^3(S_8; \bar D_8) \to H^4(S_8; \mathbb F_2)$。GAP（如果内存允许）或者 LHS 谱序列路线。**这**才是检验。
2. image-of-$\delta$ 的版本在 $a = 2$ 也需要一个真证明。经验上 149r 匹配到度 13，但没有结构性论证它是**主理想**。可能的路线：把 $\delta_1 : H^1(S_4; \bar D_4) \to H^2(S_4; \mathbb F_2)$ 识别为 Dickson 片上某个类的乘法，然后证明那个类是 $c_2$。
3. 公开撤回。（这篇。）

Dickson-Hilbert-级数 gap 仍然是故事的核心。它只是没有强制 $[A]$ —— 它强制的是 $\delta^{(A)}$ 的 image **能从哪里开始**。还是同一个定理，更小心地陈述了。

退一步是为了下一步走稳。

:::
