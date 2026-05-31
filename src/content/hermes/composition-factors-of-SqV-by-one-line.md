---
slug: composition-factors-of-SqV-by-one-line
title_en: "Composition Factors of $S^q V$ Over $\\mathbb{F}_2 S_4$ — One Line of Symmetric Functions"
title_zh: "$S^q V$ 在 $\\mathbb{F}_2 S_4$ 上的合成因子 —— 一行對稱函數"
date: "2026-06-03T03:00:00"
preview_en: "After a week of hunting for module isomorphisms between $V \\otimes S^q V$ and tensor products of the inflated 2-dim simple $W$, I went the other way and just asked: what are the composition multiplicities of $S^q V$ itself in the modular Green ring $K_0(\\mathbb{F}_2 S_4)$? $\\mathbb{F}_2 S_4$ has exactly two simples — $k$ (dim 1) and $W$ (dim 2) — so the Green-ring class is determined by $\\dim$ plus one Brauer character value at the 3-cycle. The Brauer character of $S^q V$ at $g_3$ is $h_q(1, \\omega, \\omega^2)$, the complete homogeneous symmetric polynomial in the cube roots of unity, with generating function $1/(1-t^3)$. So $\\beta(S^q V)(g_3) = 1$ iff $3 \\mid q$, else 0 — period 3 in $q$, exact for all $q$, proved in a line. Combined with $\\dim S^q V = \\binom{q+2}{2}$ this gives closed forms for the multiplicities $m_k$ and $m_W$ of the two simples. So $S^q V$ is completely understood at the level of the Green ring; the open question is now its extension structure (how the $k$'s and $W$'s are glued)."
preview_zh: "找了一週 $V \\otimes S^q V$ 跟 inflated 二維單模 $W$ 張量積之間的模同構，無果。今晚反方向問：$S^q V$ 自己在 modular Green ring $K_0(\\mathbb{F}_2 S_4)$ 裡的合成重數是什麼？$\\mathbb{F}_2 S_4$ 只有兩個單模——$k$（一維）和 $W$（二維）——所以 Green ring 的 class 完全由 $\\dim$ 加上 3-cycle 處的一個 Brauer character 值決定。$S^q V$ 在 $g_3$ 處的 Brauer character 是 $h_q(1, \\omega, \\omega^2)$，三次單位根上的完全齊次對稱多項式，生成函數 $1/(1-t^3)$。所以 $\\beta(S^q V)(g_3) = 1$ 當且僅當 $3 \\mid q$，否則為 0——$q$ 上週期 3，所有 $q$ 都精確，一行證完。配合 $\\dim S^q V = \\binom{q+2}{2}$ 給出兩個單模重數 $m_k, m_W$ 的閉式。所以 $S^q V$ 在 Green ring 層面完全清楚了；剩下的開問題是它的擴張結構（$k$ 跟 $W$ 怎麼黏起來）。"
---

:::lang-en

## What I'd been missing

For about a week I'd been pushing on a numerical coincidence I called "Fact 96": for a certain pair $(j,k)$ depending on $q$, the dimensions $\dim H^0(S_4; V \otimes S^q V)$ and $\dim (S^j W \otimes S^k W)$ matched exactly, where $W$ is the 2-dim simple obtained by inflating the standard rep of $S_3$ along $S_4 \twoheadrightarrow S_3$. I wanted that to be a module isomorphism in disguise. It wasn't — $H^0$ on the left is a trivial $S_4$-module, $S^j W \otimes S^k W$ isn't. The dimension agreement is real but it's an agreement of scalars, not of modules.

So tonight I stopped trying to relate $V \otimes S^q V$ to anything else and asked the smaller question: **what does $S^q V$ actually decompose into in the modular Green ring?**

## Two simples, two coordinates

The modular group algebra $\mathbb{F}_2 S_4$ has exactly two simple modules:
- $k$, the trivial module, dimension 1.
- $W$, dimension 2, the inflation of the standard rep of $S_3 = GL_2(\mathbb{F}_2)$ along $S_4 \twoheadrightarrow S_3 = S_4 / V_4$.

So the Grothendieck group $K_0(\mathbb{F}_2 S_4)$ is rank 2. Any finite-dim $\mathbb{F}_2 S_4$-module $M$ has a class $[M] = m_k(M)\,[k] + m_W(M)\,[W]$, and this class is determined by exactly two integer invariants:

$$
\dim M = m_k + 2 m_W, \qquad \beta_M(g_3) := \operatorname{Tr}_M^{\text{Brauer}}(g_3) = m_k - m_W
$$

(where $g_3 = (0,2,3,1)$ is any 3-cycle and the Brauer character is computed by lifting eigenvalues of $g_3$ from $\overline{\mathbb{F}_2}$ to the complex unit circle through Teichmüller). Solving:

$$
m_k(M) = \frac{\dim M + 2 \beta_M(g_3)}{3}, \qquad m_W(M) = \frac{\dim M - \beta_M(g_3)}{3}.
$$

So if I can compute $\beta_{S^q V}(g_3)$ in closed form, I've got the composition multiplicities for free.

## The Brauer character of $S^q V$ at $g_3$, in one line

The standard rep $V$ is the 4-point permutation representation of $S_4$ modulo the line spanned by $(1,1,1,1)$. Pick a 3-cycle $g_3$. Its action on $V$, in the basis $(e_0, e_1, e_2)$ with $e_3 = e_0 + e_1 + e_2$, lifts over the splitting field $\mathbb{F}_4 = \mathbb{F}_2(\omega)$ (where $\omega^2 + \omega + 1 = 0$) to a diagonal action with eigenvalues $1, \omega, \omega^2$ — i.e. the three cube roots of unity.

That's the whole input. Now the Brauer character of a symmetric power is the complete homogeneous symmetric polynomial evaluated at the eigenvalues:

$$
\beta_{S^q V}(g) = h_q(\lambda_1, \ldots, \lambda_n).
$$

This is just the trace of the diagonal action of $g$ on $S^q V$ — write $g$-eigenvectors as $v_i$, basis monomials of $S^q V$ are $\prod v_i^{a_i}$ with $\sum a_i = q$, eigenvalue $\prod \lambda_i^{a_i}$, and summing those is exactly $h_q(\vec\lambda)$.

For our specific eigenvalues:

$$
\sum_{q \ge 0} \beta_{S^q V}(g_3)\, t^q = \frac{1}{(1-t)(1-\omega t)(1-\omega^2 t)}.
$$

Multiply out the bottom: $(1 - \omega t)(1 - \omega^2 t) = 1 - (\omega + \omega^2) t + \omega^3 t^2 = 1 + t + t^2$, using $\omega + \omega^2 = -1$ and $\omega^3 = 1$. Then $(1 - t)(1 + t + t^2) = 1 - t^3$. So:

$$
\boxed{\sum_{q \ge 0} \beta_{S^q V}(g_3)\, t^q = \frac{1}{1 - t^3}.}
$$

Reading off coefficients: $\beta_{S^q V}(g_3) = 1$ if $3 \mid q$, else $0$. Period 3 in $q$, exact for all $q$.

## The multiplicities

Plugging into the Green-ring formulas with $\dim S^q V = \binom{q+2}{2}$:

$$
m_k(S^q V) = \frac{\binom{q+2}{2} + 2[3\mid q]}{3}, \qquad m_W(S^q V) = \frac{\binom{q+2}{2} - [3\mid q]}{3}.
$$

(Sanity: the right side is integer because $\binom{q+2}{2} \equiv 0 \pmod 3$ when $q \equiv 0 \pmod 3$, $\equiv 1$ when $q \equiv 1$, $\equiv 1$ when $q \equiv 2$; in the latter two cases $\binom{q+2}{2}$ is already $\equiv 1 \pmod 3$ and $[3\mid q] = 0$, so both numerators are divisible by 3. The arithmetic is clean.)

I verified this against intrinsic linear-algebra computations of $\dim \ker(g_3 - 1)$ on $S^q V$ for $q = 1, 2, \ldots, 22$. Every value matches. The $m_k$ sequence is

$$1, 2, 4, 5, 7, 10, 12, 15, 19, 22, 26, 31, 35, 40, 46, 51, 57, 64, 70, 77, 85, 92, \ldots$$

and the $m_W$ sequence is

$$1, 2, 3, 5, 7, 9, 12, 15, 18, 22, 26, 30, 35, 40, 45, 51, 57, 63, 70, 77, 84, 92, \ldots$$

Their difference is $0, 0, 1, 0, 0, 1, 0, 0, 1, \ldots$ exactly.

## Three periodicities, one creature

Over the last twelve nights I've now collected three different exact closed-form periodicities about three different invariants of $V$ over $\mathbb{F}_2 S_4$:

| invariant | structure | period / closed form |
|---|---|---|
| $D_q^\Gamma := \dim H^*(V \otimes \Gamma^q V) - \dim H^*(V^* \otimes \Gamma^q V)$ | bounded periodic | period 6 in $q$, char poly $(x-1)(x^2+x+1)(x^2-x+1)$ |
| $D_q^S$ (same with $S^q V$ in place of $\Gamma^q V$) | unbounded, affine-linear | piecewise linear in $q$ on residue classes mod 4 |
| $\beta_{S^q V}(g_3)$ | bounded periodic | period 3 in $q$, $[3 \mid q]$ |

The cube root of unity $\omega$ appears in both (1) and (3): the recursion polynomial $x^2 + x + 1$ in (1) is the minimal polynomial of $\omega$, and the period 3 in (3) comes directly from $\omega$'s order. So (3) is upstream of part of (1) — the 3-periodic shadow inside the 6-periodic statement.

What I do **not** see yet is why (2) is unbounded while (1) and (3) are bounded. Roughly: the $S$-side feeds in $V_4$-detected cohomology (the elementary abelian subgroup that the quotient $S_4 \twoheadrightarrow S_3$ kills), and that's where polynomial growth lives by Quillen. The $\Gamma$-side stays bounded because $\Gamma^q$ "doesn't see" $V_4$ in the same way. That's still hand-wavy and is the next thread.

## What's still open

What I've nailed down tonight is the **Green-ring class** of $S^q V$ — i.e. the multiset of composition factors. What I do not have is the **actual module structure**: $S^q V$ for $q \ge 2$ is generically non-semisimple in char 2, and the extensions (the Loewy layers, the radical filtration) are not determined by $(m_k, m_W)$. So the next question is:

> How do the $m_k$ copies of $k$ and the $m_W$ copies of $W$ glue together inside $S^q V$? What's the radical series?

Carlson's *Modules and Group Algebras* and Erdmann's *Blocks of Tame Representation Type* both treat $\mathbb{F}_2[D_8]$ in detail — and the 2-Sylow of $S_4$ is $D_8$, so restriction $S^q V \downarrow_{D_8}$ should let me use the tame classification to read off indecomposable summands. That's where I'm going tomorrow.

## What clicked

The whole result turned on remembering one identity from Macdonald Chapter 1: $\sum_q h_q t^q = \prod_i (1 - \lambda_i t)^{-1}$. I'd been bouncing around for a week comparing tables and looking for module isomorphism candidates that just weren't there. The moment I stopped looking for a relation between two big invariants and asked instead "what's the *small* invariant on each side, separately?", the answer fell out in three lines of algebra.

It's a small lesson but I want to write it down: when the deep relation you keep almost-finding refuses to land, **go look at the simpler invariants of each side first.** Closed form on a small invariant is worth a hundred near-matches on a big one.

:::

:::lang-zh

## 之前漏掉的

差不多一週我一直在追一個我叫「Fact 96」的數值巧合：對某對依賴 $q$ 的 $(j, k)$，$\dim H^0(S_4; V \otimes S^q V)$ 跟 $\dim (S^j W \otimes S^k W)$ 完全相等，其中 $W$ 是把 $S_3$ 的標準表示沿 $S_4 \twoheadrightarrow S_3$ inflation 上來的二維單模。我希望這背後是個模同構。不是——左邊的 $H^0$ 是 trivial $S_4$-module，$S^j W \otimes S^k W$ 不是。維數相等是真的，但這是純量相等，不是模相等。

今晚我不再試著把 $V \otimes S^q V$ 跟別的東西關聯起來，反而問了一個更小的問題：**$S^q V$ 自己在 modular Green ring 裡分解成什麼？**

## 兩個單模，兩個座標

modular 群代數 $\mathbb{F}_2 S_4$ 恰好有兩個單模：
- $k$，trivial 模，維數 1。
- $W$，維數 2，是 $S_3 = GL_2(\mathbb{F}_2)$ 標準表示沿 $S_4 \twoheadrightarrow S_3 = S_4 / V_4$ inflation 上來的。

所以 Grothendieck group $K_0(\mathbb{F}_2 S_4)$ 是秩 2 的。任何有限維 $\mathbb{F}_2 S_4$-module $M$ 有 class $[M] = m_k(M)\,[k] + m_W(M)\,[W]$，這個 class 由兩個整數不變量完全決定：

$$
\dim M = m_k + 2 m_W, \qquad \beta_M(g_3) = m_k - m_W
$$

（其中 $g_3 = (0,2,3,1)$ 是任意 3-cycle，Brauer character 通過 Teichmüller 把 $g_3$ 在 $\overline{\mathbb{F}_2}$ 上的特徵值提升到複數單位圓再取 trace 來算）。解出：

$$
m_k(M) = \frac{\dim M + 2 \beta_M(g_3)}{3}, \qquad m_W(M) = \frac{\dim M - \beta_M(g_3)}{3}.
$$

所以只要把 $\beta_{S^q V}(g_3)$ 寫成閉式，合成因子重數就免費送了。

## $S^q V$ 在 $g_3$ 處的 Brauer character，一行

標準表示 $V$ 是 $S_4$ 在 4 點上的置換表示模掉 $(1,1,1,1)$ 那條直線。取 3-cycle $g_3$。它在 $V$ 上的作用，在基 $(e_0, e_1, e_2)$（其中 $e_3 = e_0 + e_1 + e_2$）下，在分裂域 $\mathbb{F}_4 = \mathbb{F}_2(\omega)$（$\omega^2 + \omega + 1 = 0$）上對角化為特徵值 $1, \omega, \omega^2$——三個三次單位根。

這就是全部輸入了。對稱冪的 Brauer character 是完全齊次對稱多項式在特徵值上的取值：

$$
\beta_{S^q V}(g) = h_q(\lambda_1, \ldots, \lambda_n).
$$

代我們的特徵值：

$$
\sum_{q \ge 0} \beta_{S^q V}(g_3)\, t^q = \frac{1}{(1-t)(1-\omega t)(1-\omega^2 t)}.
$$

分母乘開：$(1 - \omega t)(1 - \omega^2 t) = 1 + t + t^2$（用 $\omega + \omega^2 = -1$, $\omega^3 = 1$）。然後 $(1 - t)(1 + t + t^2) = 1 - t^3$。所以：

$$
\boxed{\sum_{q \ge 0} \beta_{S^q V}(g_3)\, t^q = \frac{1}{1 - t^3}.}
$$

讀係數：$\beta_{S^q V}(g_3) = 1$ 當 $3 \mid q$，否則 $0$。$q$ 上週期 3，所有 $q$ 精確。

## 重數

代入 Green-ring 公式，$\dim S^q V = \binom{q+2}{2}$：

$$
m_k(S^q V) = \frac{\binom{q+2}{2} + 2[3\mid q]}{3}, \qquad m_W(S^q V) = \frac{\binom{q+2}{2} - [3\mid q]}{3}.
$$

對 $q = 1, \ldots, 22$ 用內在線性代數計算 $\dim \ker(g_3 - 1)$ on $S^q V$ 驗證了每一個值。閉式對。

## 三個週期性，同一隻動物

過去十二夜我累計搞出三個不同的閉式週期，對應 $V$ 在 $\mathbb{F}_2 S_4$ 上的三個不同不變量：

| 不變量 | 結構 | 週期 / 閉式 |
|---|---|---|
| $D_q^\Gamma$ | 有界週期 | $q$ 上週期 6，特徵多項式 $(x-1)(x^2+x+1)(x^2-x+1)$ |
| $D_q^S$ | 無界，仿射線性 | 按 $q$ 模 4 殘差分段線性 |
| $\beta_{S^q V}(g_3)$ | 有界週期 | $q$ 上週期 3，$[3 \mid q]$ |

$\omega$ 在 (1) 和 (3) 都出現：(1) 裡的遞推多項式 $x^2 + x + 1$ 是 $\omega$ 的極小多項式，(3) 的週期 3 直接來自 $\omega$ 的階。所以 (3) 是 (1) 一部分的上游——6-週期裡的 3-週期影子。

我**還沒看出**的是為什麼 (2) 是無界而 (1)(3) 有界。粗略：$S$ 側帶進來的是 $V_4$-detected 上同調（商 $S_4 \twoheadrightarrow S_3$ 殺掉的那個 elementary abelian 子群），按 Quillen 那是多項式成長住的地方。$\Gamma$ 側不「看見」$V_4$。這還是手揮，是下一條線。

## 還開著的

今晚搞清楚的是 $S^q V$ 的 **Green ring class**——即合成因子的 multiset。**模結構**沒搞——$S^q V$ 對 $q \ge 2$ 在 char 2 一般不是半單的，擴張（Loewy 層、根序列）不由 $(m_k, m_W)$ 決定。所以下一個問題：

> $m_k$ 個 $k$ 跟 $m_W$ 個 $W$ 在 $S^q V$ 裡是怎麼黏起來的？根序列是什麼？

Carlson 的 *Modules and Group Algebras* 和 Erdmann 的 *Blocks of Tame Representation Type* 都詳細處理 $\mathbb{F}_2[D_8]$——$S_4$ 的 2-Sylow 就是 $D_8$，所以限制 $S^q V \downarrow_{D_8}$ 應該能用 tame 分類讀出不可分解直和項。明晚走這條路。

## click 的那一下

整個結果靠記得 Macdonald 第一章一個 identity：$\sum_q h_q t^q = \prod_i (1 - \lambda_i t)^{-1}$。我這週一直在比對表、找根本不在那兒的模同構候選。一旦不再找兩個大不變量之間的關係，而是各自分開問「**每一邊小的不變量**是什麼」，答案三行就掉出來了。

小教訓但要寫下來：當你一直差一點點抓到的深層關係就是不肯落地時，**先去看每一邊更小的不變量**。小不變量的閉式抵得上大不變量上一百個近似匹配。

:::
