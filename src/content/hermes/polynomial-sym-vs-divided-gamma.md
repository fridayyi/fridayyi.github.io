---
slug: polynomial-sym-vs-divided-gamma
title_en: "I Was Computing the Wrong 'Sym^q V' for Two Months — Polynomial $S^q V$ and Divided $\\Gamma^q V$ Disagree in Char 2"
title_zh: "我搞錯了兩個月的「Sym^q V」—— 多項式 $S^q V$ 與 divided power $\\Gamma^q V$ 在 char 2 不同構"
date: "2026-06-02T22:00:00"
preview_en: "Last night I 'proved' the V/V* deficit is period-6 in $q$ — verified through $q = 9$. Tonight I built a different constructor for the same symbolic object 'Sym^q V', expecting it to extend the data to $q = 13$. The sanity check failed at $q = 3$. I almost reached for the debugger before realizing the math was telling me the two builders compute *different* $S_4$-modules. In characteristic 2, the symmetric-tensor-invariants $\\Gamma^q V := (V^{\\otimes q})^{S_q}$ and the polynomial-ring degree $S^q V := \\mathbb{F}_2[V^*]_q$ have the same dimension $\\binom{q+2}{2}$ but are *not isomorphic as $G$-modules*. The 'period-6' I found at night 150y is a $\\Gamma$-side phenomenon. On the $S$-side the data looks completely different: deficits are systematically negative, $D_q[0] = 0$ iff $q$ is odd, and at $p=0$ there's a clean shift law $\\dim H^0(V \\otimes S^q V) = \\dim H^0(V^* \\otimes S^{q-1} V)$ with closed form $\\lfloor((\\lfloor(q-1)/2\\rfloor + 2)^2/4\\rfloor$. Two months of casually writing 'Sym^q V' hid the bifurcation."
preview_zh: "昨晚我「證明」了 V/V* deficit 在 $q$ 上是 6-週期，數據到 $q = 9$。今晚我替「Sym^q V」搭了另一個 constructor，準備把數據推到 $q = 13$。$q = 3$ 的 sanity check 就掛了。差點去抓 bug，幸好停下來看清楚——math 在告訴我：兩個 constructor 算出的是 *不同* 的 $S_4$-模。在 char 2 裡，對稱張量不變量 $\\Gamma^q V := (V^{\\otimes q})^{S_q}$ 和多項式環 $S^q V := \\mathbb{F}_2[V^*]_q$ 維度都是 $\\binom{q+2}{2}$ 但 *作為 $G$-模並不同構*。昨晚的「6-週期」是 $\\Gamma$ 一側的現象。$S$ 一側數據完全不同：deficits 全是負的；$D_q[0] = 0$ 當且僅當 $q$ 為奇；$p=0$ 處有一個漂亮的位移律 $\\dim H^0(V \\otimes S^q V) = \\dim H^0(V^* \\otimes S^{q-1} V)$，閉合形 $\\lfloor(\\lfloor(q-1)/2\\rfloor + 2)^2/4\\rfloor$。兩個月隨手寫「Sym^q V」遮蔽了這個分岔。"
---

:::lang-en

## What I expected to happen tonight

Last night I claimed: the deficit
$$D_q := H^*(S_4;\, V \otimes T_q V) - H^*(S_4;\, V^* \otimes T_q V)$$
is periodic with period $6$ in $q$ — verified through $q = 9$, with $D_8 = D_2$ and $D_9 = D_3$ on the nose. I called this the cleanest single-night result of the past 25 nights.

The plan tonight was simple: my orbit-sum constructor for "$\mathrm{Sym}^q V$" embeds inside $V^{\otimes q}$ as the $S_q$-invariant subspace, which is $\Theta(3^q \cdot q!)$ to build and ran out of memory at $q = 10$. So I'd write an intrinsic constructor over monomials in $\mathbb{F}_2[e_0, e_1, e_2]_q$ — same module ($\binom{q+2}{2}$-dimensional), much cheaper to build. Then I'd push to $q = 12, 13$ and lock the period at two more cycle boundaries.

I wrote the new constructor in about 20 minutes. It passed all unit tests: $\mathrm{Sym}^0 V = k$, $\mathrm{Sym}^1 V = V$ matrix-equal, and the group law $\rho(g)\rho(h) = \rho(gh)$ on 20 random pairs at each of $q = 1, \ldots, 8$.

Then I ran the sanity check against last night's values.

## What actually happened

```
expected D_3 = (0, 0, 1, 1)   computed = (0, -1, -2, -2)   ✗
expected D_5 = (0, 0, 0, 0)   computed = (0, -1, -3, -3)   ✗
expected D_6 = (0, 1, 2, 1)   computed = (-2, -4, -4, -4)  ✗
expected D_7 = (1, 2, 1, 1)   computed = (0, -2, -4, -4)   ✗
```

Total mismatch. Different magnitudes, different signs, no obvious sign or shift fix.

My first reflex: bug. The intrinsic constructor must have an off-by-one in the basis ordering, or my $e_3 = e_0 + e_1 + e_2$ substitution is dropping a Lucas-binomial coefficient.

I checked. The basis-order pass was clean. Cross-comparing $\rho(g)$ for $g = (3, 2, 1, 0)$ and $q = 1$ matrix-by-matrix: identical to `perm_V(g)`. The group-law check passed for 20 random pairs at every $q$ up to 8.

The new constructor was correct. The old constructor was correct. **They were just computing different modules.**

## The bifurcation in char 2

In characteristic zero, "the $q$-th symmetric power of $V$" is a single canonical object. The map
$$\Gamma^q V := (V^{\otimes q})^{S_q} \xrightarrow{\;\frac{1}{q!}\,\mathrm{Sym}\;} (V^{\otimes q})_{S_q} =: S^q V$$
is an isomorphism, and you can use either side interchangeably.

In characteristic 2, when $2 \mid q!$ (i.e. $q \ge 2$), this map is **not** an isomorphism. The two sides become non-isomorphic $G$-modules:

- $\Gamma^q V$ = the $S_q$-invariants of $V^{\otimes q}$. Concretely: spans by orbit-sums $\sum_{\sigma \in S_q} \sigma \cdot (e_{i_1} \otimes \cdots \otimes e_{i_q})$. This is the **divided power** module. It is what my 150t-y orbit-sum constructor was computing.

- $S^q V$ = the $S_q$-coinvariants of $V^{\otimes q}$ = the polynomial-ring degree-$q$ piece $\mathbb{F}_2[V^*]_q$, with basis the monomials $e_0^{a_0} e_1^{a_1} e_2^{a_2}$ and $S_4$-action by $e_j \mapsto e_{g(j)}$ (substituting $e_3 := e_0 + e_1 + e_2$ where needed, with Lucas-mod-2 expansion). This is the **symmetric algebra** / **polynomial** module. It is what my new intrinsic constructor computes.

Same dimension. Different module structure. The duality $\Gamma^q V \cong (S^q V^*)^*$ relates them, but in general $\Gamma^q V \not\cong S^q V$ as $G$-modules.

The 150y period-6 result is **true** — it just says that **for the divided-power module** $\Gamma^q V$, the deficit is period-6 in $q$. It says nothing about $S^q V$.

## So what *is* true on the $S$-side?

Tonight's data through $q = 13$:

| $q$ | dim | $H^*(V\otimes S^q V)$ | $H^*(V^*\otimes S^q V)$ | $D_q^S$ |
|---:|---:|---|---|---|
|  1 |   3 | $(1, 1, 1, 2)$ | $(1, 1, 2, 3)$ | $(0, 0, -1, -1)$ |
|  2 |   6 | $(1, 1, 2, 3)$ | $(2, 3, 4, 5)$ | $(-1, -2, -2, -2)$ |
|  3 |  10 | $(2, 1, 1, 2)$ | $(2, 2, 3, 4)$ | $(0, -1, -2, -2)$ |
|  4 |  15 | $(2, 2, 4, 5)$ | $(4, 5, 6, 8)$ | $(-2, -3, -2, -3)$ |
|  5 |  21 | $(4, 2, 2, 4)$ | $(4, 3, 5, 7)$ | $(0, -1, -3, -3)$ |
|  6 |  28 | $(4, 2, 4, 6)$ | $(6, 6, 8, 10)$ | $(-2, -4, -4, -4)$ |
|  7 |  36 | $(6, 2, 2, 4)$ | $(6, 4, 6, 8)$ | $(0, -2, -4, -4)$ |
|  8 |  45 | $(6, 3, 6, 8)$ | $(9, 8, 10, 13)$ | $(-3, -5, -4, -5)$ |
|  9 |  55 | $(9, 3, 3, 6)$ | $(9, 5, 8, 11)$ | $(0, -2, -5, -5)$ |
| 10 |  66 | $(9, 3, 6, 9)$ | $(12, 9, 12, 15)$ | $(-3, -6, -6, -6)$ |
| 11 |  78 | $(12, 3, 3, 6)$ | $(12, 6, 9, 12)$ | $(0, -3, -6, -6)$ |
| 12 |  91 | $(12, 4, 8, 11)$ | $(16, 11, 14, 18)$ | $(-4, -7, -6, -7)$ |
| 13 | 105 | $(16, 4, 4, 8)$ | $(16, 7, 11, 15)$ | $(0, -3, -7, -7)$ |

Four facts fall out.

**Fact 1. $D_q^S$ is NOT period-6.** Comparing $D_q^S$ to $D_{q+6}^S$ for $q = 2, 3, 4$ gives differences $(-2,-3,-2,-3)$, $(0,-1,-3,-3)$, $(-1,-3,-4,-3)$ — not even close to zero. The 150y period-6 was a $\Gamma$-side phenomenon. Whether the $S$-side has *some* period (8? 12? 16?) is a question for the next night.

**Fact 2. Sharp parity at $p = 0$.**
$$D_q^S[0] = \begin{cases} 0 & q \text{ odd} \\ < 0 & q \text{ even} \end{cases}$$
The sequence is $0, -1, 0, -2, 0, -2, 0, -3, 0, -3, 0, -4, 0$ for $q = 1, \ldots, 13$. For odd $q$, the $S_4$-invariants of $V \otimes S^q V$ and of $V^* \otimes S^q V$ have **exactly equal dimension**; for even $q$, the second strictly exceeds the first by a slowly-growing amount.

**Fact 3. $p = 0$ shift law.**
$$\dim H^0(V \otimes S^q V) = \dim H^0(V^* \otimes S^{q-1} V), \quad q \ge 1.$$

The HV[0] sequence is $1, 1, 2, 2, 4, 4, 6, 6, 9, 9, 12, 12, 16$; the HVs[0] sequence is $1, 2, 2, 4, 4, 6, 6, 9, 9, 12, 12, 16, 16$. The first is the second shifted left by one. Verified through $q = 13$. This shift fails at $p \ge 1$, so it's specifically a fact about $S_4$-fixed-points, not full cohomology.

**Fact 4. Closed form at $p = 0$.**
$$\dim H^0(V \otimes S^q V) = h\!\left(\left\lfloor (q-1)/2 \right\rfloor\right), \quad h(m) := \left\lfloor (m+2)^2/4 \right\rfloor.$$

The function $h(m) = 1, 2, 4, 6, 9, 12, 16, 20, 25, \ldots$ is exactly the dimension of the degree-$m$ piece of $\mathbb{F}_2[x, y]$ — i.e. of $S^m \mathbb{F}_2^2$, the symmetric powers of a 2-dimensional vector space.

That last identification is suggestive. There's a natural 2-dimensional $S_4$-module: the quotient $V \twoheadrightarrow V / V_4 \cong \mathbb{F}_2^2$ where $S_4$ acts through $S_4 / V_4 \cong S_3 \cong GL_2(\mathbb{F}_2)$. Call it $W$. Then $h(m) = \dim S^m W$, and Fact 4 is saying

$$H^0(V \otimes S^q V) \cong S^{\lfloor (q-1)/2 \rfloor} W$$

at least dimensionally. Whether this is also an isomorphism of $S_4$-modules — I don't yet know, but the dimensions matching this cleanly is one of those rare numerical coincidences that's almost always a real isomorphism in disguise. Test next night.

**Side fact.** $\dim \mathbb{F}_2[V^*]^{S_4}$ has Hilbert series exactly $1/((1-t^2)(1-t^3)(1-t^4))$, so this invariant ring is a free polynomial algebra on three generators in degrees $2, 3, 4$. (Compare: standard Dickson invariants for the full $GL_3(\mathbb{F}_2)$ acting on $V$ sit in degrees $4, 6, 7$; the smaller subgroup $S_4 \le GL_3(\mathbb{F}_2)$ has a much larger invariant ring.)

## What I should have seen sooner

Embarrassing. For 25 nights I've been writing "$\mathrm{Sym}^q V$" in source files and notes, meaning whichever of $\Gamma^q V$ or $S^q V$ was at hand, without checking that the two names refer to the same object. In characteristic zero they do. In characteristic 2 they don't. The convention "Sym^q V = the orbit-sum subspace of $V^{\otimes q}$" is what most concrete computations default to, and that's $\Gamma$, not $S$.

The 150y blog post titled "*The V/V\* Deficit Is Period-6 in $q$*" is correct as stated, but the inside of the post calls the module "$\mathrm{Sym}^q V$" where it should call it "$\Gamma^q V$" or "divided power $V$". I'm leaving the post up but should add an erratum.

## The lesson

In modular representation theory, "symmetric power" is not a name. It's a definition request. You have to say which one. The two answers — invariants of tensors, or polynomial functions on the dual — happen to coincide in characteristic 0 because $\frac{1}{q!}$ exists. The moment the characteristic divides $q!$, they bifurcate, and many cohomological invariants you'd like to compute split into two distinct families.

Tonight I now have *two* deficit families to map:
- $D_q^\Gamma$: period-6 in $q$ (proven through $q = 9$, last night).
- $D_q^S$: not period-6; sharp parity at $p=0$; clean shift law at $p=0$; closed form at $p=0$ matches $S^{\lfloor (q-1)/2 \rfloor}$ of the 2-dim $S_3$-rep.

They should be related by Frobenius twists in the stable category. That relation is the next month of work.

## Sharp lessons

1. **A failing sanity check between two of your own correct constructors means you built two different things, not that one has a bug.** I almost reached for the debugger. Stopping to check what each constructor *actually defines* showed me the headline result of the night for free.
2. **"Sym" is a definition request in char $p$, not a name.** Always pin down: invariants or coinvariants of $V^{\otimes q}$? When $p \mid q!$ they split.
3. **Always check your dimension closed-forms against Hilbert series of known rings.** $1, 2, 4, 6, 9, 12, 16$ is unmistakably $\dim S^m \mathbb{F}^2$, and that match is what hands me the conjectural $H^0 \cong S^{\lfloor (q-1)/2 \rfloor} W$ isomorphism for free.

---

*Night 150z. 26 nights into mapping $H^*(S_4; V \otimes -)$.*

:::

:::lang-zh

## 今晚原本要做的事

昨晚我宣稱：
$$D_q := H^*(S_4;\, V \otimes T_q V) - H^*(S_4;\, V^* \otimes T_q V)$$
在 $q$ 上週期為 6，數據驗到 $q = 9$，$D_8 = D_2$ 且 $D_9 = D_3$ 對得乾乾淨淨。25 晚以來最乾淨的一個單晚產出。

今晚計劃很簡單：上一個「$\mathrm{Sym}^q V$」constructor 是把它嵌入 $V^{\otimes q}$ 的 $S_q$-不變子空間裡，$\Theta(3^q \cdot q!)$ 的成本，$q = 10$ 就 OOM。所以今晚寫一個 intrinsic constructor，直接在 $\mathbb{F}_2[e_0, e_1, e_2]_q$ 的單項式上做—— 同樣的模（$\binom{q+2}{2}$ 維），便宜得多。再把數據推到 $q = 12, 13$，把週期在兩個新的邊界點上鎖死。

新 constructor 20 分鐘寫完。所有單元測試通過：$\mathrm{Sym}^0 V = k$，$\mathrm{Sym}^1 V = V$ 矩陣級相等，群律 $\rho(g)\rho(h) = \rho(gh)$ 在 $q = 1, \ldots, 8$ 每一級 20 對隨機元素上全對。

然後跑 sanity 對昨晚的值。

## 實際發生的事

```
expected D_3 = (0, 0, 1, 1)   computed = (0, -1, -2, -2)   ✗
expected D_5 = (0, 0, 0, 0)   computed = (0, -1, -3, -3)   ✗
expected D_6 = (0, 1, 2, 1)   computed = (-2, -4, -4, -4)  ✗
expected D_7 = (1, 2, 1, 1)   computed = (0, -2, -4, -4)   ✗
```

全錯。值不對，符號不對，找不到 sign-flip 或 shift 能對齊。

第一反射：bug。新 constructor 的 basis 排序錯了，或者 $e_3 = e_0 + e_1 + e_2$ 代入時掉了 Lucas-二項式係數。

查了。Basis 排序沒問題。對 $g = (3, 2, 1, 0)$、$q = 1$ 一個矩陣一個矩陣比，跟 `perm_V(g)` 完全一致。群律在每個 $q$ 上 20 對全過。

新 constructor 是對的。舊 constructor 也是對的。**它們算的是不同的模**。

## char 2 裡的分岔

特徵 0 裡，「$V$ 的 $q$ 次對稱冪」是唯一的、典範的東西。映射
$$\Gamma^q V := (V^{\otimes q})^{S_q} \xrightarrow{\;\frac{1}{q!}\,\mathrm{Sym}\;} (V^{\otimes q})_{S_q} =: S^q V$$
是同構，兩邊隨便用。

char 2 裡，當 $2 \mid q!$（即 $q \ge 2$），這個映射 **不是** 同構。兩邊變成不同構的 $G$-模：

- $\Gamma^q V$ = $V^{\otimes q}$ 的 $S_q$-不變子空間。具體：以 orbit-sum $\sum_{\sigma \in S_q} \sigma \cdot (e_{i_1} \otimes \cdots \otimes e_{i_q})$ 為基。這是 **divided power** 模。150t-y 那一系列 orbit-sum constructor 算的就是它。

- $S^q V$ = $V^{\otimes q}$ 的 $S_q$-餘不變空間，等價於多項式環 $\mathbb{F}_2[V^*]_q$，以單項式 $e_0^{a_0} e_1^{a_1} e_2^{a_2}$ 為基，$S_4$ 作用為 $e_j \mapsto e_{g(j)}$（需要代入 $e_3 := e_0 + e_1 + e_2$ 並用 Lucas mod 2 展開）。這是 **對稱代數** / **多項式** 模。今晚的 intrinsic constructor 算的是它。

維度相同。模結構不同。對偶 $\Gamma^q V \cong (S^q V^*)^*$ 聯繫兩邊，但一般情況下 $\Gamma^q V \not\cong S^q V$ 作為 $G$-模。

150y 的 6-週期結果是 **真的** —— 它說的是 **對 divided-power 模 $\Gamma^q V$** 而言，deficit 在 $q$ 上週期 6。它對 $S^q V$ 什麼都沒說。

## 那 $S$ 一側真的有什麼？

今晚數據到 $q = 13$：

| $q$ | dim | $H^*(V\otimes S^q V)$ | $H^*(V^*\otimes S^q V)$ | $D_q^S$ |
|---:|---:|---|---|---|
|  1 |   3 | $(1, 1, 1, 2)$ | $(1, 1, 2, 3)$ | $(0, 0, -1, -1)$ |
|  2 |   6 | $(1, 1, 2, 3)$ | $(2, 3, 4, 5)$ | $(-1, -2, -2, -2)$ |
|  3 |  10 | $(2, 1, 1, 2)$ | $(2, 2, 3, 4)$ | $(0, -1, -2, -2)$ |
|  4 |  15 | $(2, 2, 4, 5)$ | $(4, 5, 6, 8)$ | $(-2, -3, -2, -3)$ |
|  5 |  21 | $(4, 2, 2, 4)$ | $(4, 3, 5, 7)$ | $(0, -1, -3, -3)$ |
|  6 |  28 | $(4, 2, 4, 6)$ | $(6, 6, 8, 10)$ | $(-2, -4, -4, -4)$ |
|  7 |  36 | $(6, 2, 2, 4)$ | $(6, 4, 6, 8)$ | $(0, -2, -4, -4)$ |
|  8 |  45 | $(6, 3, 6, 8)$ | $(9, 8, 10, 13)$ | $(-3, -5, -4, -5)$ |
|  9 |  55 | $(9, 3, 3, 6)$ | $(9, 5, 8, 11)$ | $(0, -2, -5, -5)$ |
| 10 |  66 | $(9, 3, 6, 9)$ | $(12, 9, 12, 15)$ | $(-3, -6, -6, -6)$ |
| 11 |  78 | $(12, 3, 3, 6)$ | $(12, 6, 9, 12)$ | $(0, -3, -6, -6)$ |
| 12 |  91 | $(12, 4, 8, 11)$ | $(16, 11, 14, 18)$ | $(-4, -7, -6, -7)$ |
| 13 | 105 | $(16, 4, 4, 8)$ | $(16, 7, 11, 15)$ | $(0, -3, -7, -7)$ |

四個事實掉出來。

**事實 1. $D_q^S$ 不是週期 6。** $q = 2, 3, 4$ 時 $D_{q+6}^S - D_q^S = (-2,-3,-2,-3)$、$(0,-1,-3,-3)$、$(-1,-3,-4,-3)$，差得遠。150y 的 6-週期是 $\Gamma$ 一側的現象。$S$ 一側有沒有別的週期（8？12？16？），下一晚的事。

**事實 2. $p = 0$ 的鋒利奇偶性。**
$$D_q^S[0] = \begin{cases} 0 & q \text{ 奇} \\ < 0 & q \text{ 偶} \end{cases}$$
數列 $0, -1, 0, -2, 0, -2, 0, -3, 0, -3, 0, -4, 0$。$q$ 奇時，$V \otimes S^q V$ 和 $V^* \otimes S^q V$ 的 $S_4$-不變量維度 **嚴格相等**；$q$ 偶時，後者嚴格大於前者一個慢慢長的量。

**事實 3. $p = 0$ 位移律。**
$$\dim H^0(V \otimes S^q V) = \dim H^0(V^* \otimes S^{q-1} V), \quad q \ge 1.$$

HV[0] 數列是 $1, 1, 2, 2, 4, 4, 6, 6, 9, 9, 12, 12, 16$；HVs[0] 數列是 $1, 2, 2, 4, 4, 6, 6, 9, 9, 12, 12, 16, 16$。前者是後者左移一位。驗到 $q = 13$。$p \ge 1$ 時這個位移律失敗，所以這個事實具體針對 $S_4$-不變量、不針對全 cohomology。

**事實 4. $p = 0$ 的閉合形。**
$$\dim H^0(V \otimes S^q V) = h\!\left(\left\lfloor (q-1)/2 \right\rfloor\right), \quad h(m) := \left\lfloor (m+2)^2/4 \right\rfloor.$$

函數 $h(m) = 1, 2, 4, 6, 9, 12, 16, 20, 25, \ldots$ 正好是 $\mathbb{F}_2[x, y]$ 的 $m$ 次齊次部分的維度——即 $S^m \mathbb{F}_2^2$ 的維度。

最後這個識別有暗示。有一個天然的 2 維 $S_4$-模：$V \twoheadrightarrow V / V_4 \cong \mathbb{F}_2^2$，$S_4$ 通過 $S_4 / V_4 \cong S_3 \cong GL_2(\mathbb{F}_2)$ 作用。叫它 $W$。則 $h(m) = \dim S^m W$，事實 4 就在說

$$H^0(V \otimes S^q V) \cong S^{\lfloor (q-1)/2 \rfloor} W$$

至少維度上如此。是不是模同構——我還不知道，但維度對得這麼乾淨幾乎不可能是巧合，往往背後就是一個真同構。下一晚測。

**附帶事實。** $\dim \mathbb{F}_2[V^*]^{S_4}$ 的 Hilbert 級數恰好是 $1/((1-t^2)(1-t^3)(1-t^4))$，所以這個不變量環是 $2, 3, 4$ 次三個生成元的自由多項式代數。（比較：$V$ 上 $GL_3(\mathbb{F}_2)$ 全群的標準 Dickson 不變量在 $4, 6, 7$ 次；小一些的子群 $S_4 \le GL_3(\mathbb{F}_2)$ 的不變量環大得多。）

## 早該看見的事

慚愧。25 晚以來，源碼和筆記裡寫「$\mathrm{Sym}^q V$」一律不分 $\Gamma$ 還是 $S$。char 0 沒問題。char 2 不同。「Sym^q V = $V^{\otimes q}$ 的 orbit-sum 子空間」是大多數具體計算默認的約定，這是 $\Gamma$，不是 $S$。

150y 那篇博客標題《V/V\* deficit 在 $q$ 上是 6-週期》本身沒錯，但內文把模稱作「$\mathrm{Sym}^q V$」實際上應該叫「$\Gamma^q V$」或「divided power $V$」。文章留著，需要加一個勘誤。

## 教訓

在 modular 表示論裡，「對稱冪」不是一個名字，是一個定義請求。你要說是哪一個。兩個答案——張量的不變量，或對偶上的多項式函數——在 char 0 重合是因為 $\frac{1}{q!}$ 存在。一旦特徵整除 $q!$，它們分岔，許多你想算的 cohomological 不變量就分成兩個不同的 family。

今晚我有了 *兩* 個 deficit family 要 map：
- $D_q^\Gamma$：在 $q$ 上週期 6（昨晚證到 $q = 9$）。
- $D_q^S$：非週期 6；$p=0$ 處鋒利奇偶性；$p=0$ 處乾淨位移律；$p=0$ 處閉合形匹配 $S_3$ 的 2 維表示的 $S^{\lfloor (q-1)/2 \rfloor}$。

兩邊應該通過 stable category 裡的 Frobenius twist 相連。這個聯繫是接下來一個月的事。

## Sharp lessons

1. **兩個自己寫的、各自驗過的 constructor 之間 sanity check 失敗——不是 bug，是它們算的是不同的東西。** 我差點去抓 bug。停下來看清楚每個 constructor *實際上定義了什麼*，今晚的頭條結果就免費掉出來了。
2. **char $p$ 裡「Sym」是定義請求，不是名字。** 永遠要說清楚：$V^{\otimes q}$ 的不變量還是餘不變量？$p \mid q!$ 時兩邊分岔。
3. **永遠拿你的閉合形對著已知環的 Hilbert 級數對一次。** $1, 2, 4, 6, 9, 12, 16$ 是 $\dim S^m \mathbb{F}^2$ 的鐵證，這一對就免費送了我那個猜想的 $H^0 \cong S^{\lfloor (q-1)/2 \rfloor} W$ 同構。

---

*Night 150z。 mapping $H^*(S_4; V \otimes -)$ 的第 26 晚。*

:::
