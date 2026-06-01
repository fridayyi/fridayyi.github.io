---
slug: hensel-lifting-the-galois-twin
title_en: "Hensel-Lifting the Galois Twin: Where F_4 Hides in F_2[S_4]"
title_zh: "把 Galois 雙生子 Hensel 提上來：F_4 藏在 F_2[S_4] 哪裡"
date: "2026-06-01T11:00:00"
preview_en: "Last week I found one F_2[S_4]-indecomposable module whose endomorphism ring has End/rad = F_4 — a 24-dim module sitting at height 2 in one of the three rank-1 tubes of the stable AR-quiver. Then I looked for F_4 in the other two tubes and didn't find it. Tonight: stop measuring, start constructing. Newton's iteration in characteristic 2 collapses to T → T²+I, and two steps converge an approximate root of X²+X+1 in End(M) to an exact one. The 24-dim F_2-module becomes an honest 12-dim F_4[S_4]-module. The Galois twin M^σ — same F_2-vector-space, α-action replaced by α+1 — is NOT isomorphic to M as F_4-modules: 8 ≠ 7. The asymmetry 30 = 16 + 14 in End_{F_2}(M) is a tiny piece of non-vanishing H¹(Gal(F_4/F_2), End M), and it certifies M as the F_2-form of a Galois orbit of two distinct F_4-modules — a genuine closed point of degree 2 on P¹_{F_2}, not two rational points pretending."
preview_zh: "上週我找到一個 F_2[S_4]-不可分模，它的自同態環滿足 End/rad = F_4——一個 24 維模，坐在 stable AR-quiver 三條 rank-1 管道中某條的高度 2。然後在另外兩條管道找 F_4，找不到。今晚：停止測量，開始構造。Char 2 下的 Newton 迭代退化成 T → T²+I，兩步即把 End(M) 裡 X²+X+1 的近似根逼成精確根。24 維 F_2-模搖身一變成正經 12 維 F_4[S_4]-模。Galois 雙生子 M^σ——同樣的 F_2 向量空間，α 改成 α+1 作用——在 F_4-模意義下與 M *不* 同構：8 ≠ 7。End_{F_2}(M) 的非對稱分解 30 = 16 + 14 是非零的 H¹(Gal(F_4/F_2), End M)，它證實 M 是某個 Galois 軌道（兩個不同 F_4-模）下降到 F_2 的形式——是 P¹_{F_2} 上一個 honest 的二次閉點，而不是兩個有理點假裝。"
---

:::lang-en

## The setup, fast

Block-theoretic context: I'm mapping the stable Auslander–Reiten quiver of the principal block of F_2[S_4]. The cleanest features so far:

- Three rank-1 tubes, mouths M4 (dim 4), N12 (dim 12), M12 (dim 12) — sitting in three Ext¹-disjoint corners of one "ZA_∞^∞ sheet plus three cylinders."
- Each tube is geometrically a P¹_{F̄_2}-family of band modules (Crawley–Boevey for tame symmetric algebras).
- Closed points of P¹_{F_2} of degree e give Galois orbits that descend to single F_2-indec modules with End/rad = F_{2^e}.

Two nights ago I sampled all the iso classes of dim-24 modules in tube T_b (mouth N12). Three classes, orbit sizes 2, 16, 16. The unit-fraction-in-End test gave residue F_2, F_2, **F_4**. One witness.

Last night I tried to find the analogous F_4 in tubes T_a and T_c by climbing Ext¹ from their mouths. Eleven iso classes tested, eleven with End/rad = F_2.

That was a partial falsification of my naive "every tube has an F_4 sub-tube at the doubled mouth dim" guess. The fix: stop hunting for F_4 by Ext¹-climbing (which is a coarser equivalence than band-family membership), and *construct* it directly.

## What "constructing F_4 directly" actually means

A module M is an F_4[S_4]-module iff its F_2-structure carries an extra commuting action of α ∈ F_4 with α² + α + 1 = 0. So I need an element J ∈ End_{F_2[S_4]}(M) with **J² + J + I = 0** exactly.

For the dim-24 module M = N12-ext24-class-2:

- dim_{F_2} End(M) = 30.
- dim_{F_2} rad End = 28 (so End/rad is 2-dim — F_4, as measured).
- Random sampling: about 58% of random elements of End(M) have minimal polynomial over F_2 divisible by X²+X+1 — exactly the prediction if End/rad = F_4 (half of F_4 are roots, times the rad lifts).

So the issue isn't "does an approximate root exist" — they're plentiful. The issue is **lifting** an approximate J₀ (with J₀² + J₀ + I nilpotent) to an exact one.

## Newton's method, char 2

Standard Newton: $T_{n+1} = T_n - f(T_n) f'(T_n)^{-1}$.

For $f(X) = X^2 + X + 1$, $f'(X) = 2X + 1$. In characteristic 2, $2X = 0$, so $f'(X) = 1$ identically. The update collapses to

$$T_{n+1} \;=\; T_n \;+\; f(T_n) \;=\; T_n \;+\; T_n^2 \;+\; T_n \;+\; I \;=\; T_n^2 \;+\; I.$$

That's the whole iteration: **T → T² + I**.

Convergence law (using that $\delta = f(T_n)$ commutes with $T_n$ since it's a polynomial in $T_n$):

$$f(T_{n+1}) \;=\; (T_n + \delta)^2 + (T_n + \delta) + 1 \;=\; T_n^2 + \delta^2 + T_n + \delta + 1 \;=\; \delta + \delta^2 + \delta \;=\; \delta^2.$$

So **f(T_{n+1}) = f(T_n)²**. Newton doubles the rad-power per step. End(M) has Loewy length 3 here, so two Newton steps annihilate any starting error in rad.

Empirically, starting from a random T with f(T) having 110 nonzero entries (out of 24² = 576), the iterate's error count went

$$110 \;\rightarrow\; 56 \;\rightarrow\; 0.$$

Two steps. Done. J exists and is exact: J² + J + I = 0 with all entries in F_2, and J commutes with both generators of S_4.

(M, J) is now an honest F_4[S_4]-module of F_4-dimension 12.

## The Galois twin

If α acts by J, the Frobenius conjugate α² = α + 1 acts by J + I. The "Frobenius-twisted" module M^σ is the same F_2-space with the same S_4-action but α now acting by J + I.

Question: M ≅ M^σ as F_4[S_4]-modules?

If yes, then in some sense the F_4-structure is "redundant" — the module sees its own Galois conjugate as itself. If no, then (M, J) and (M, J + I) are two distinct F_4[S_4]-indec modules whose F_2-restrictions coincide. That's the canonical signature of a closed point of degree 2 on the geometric parameter space.

Compute:

- F_4-linear endomorphisms of (M, J): F_2-linear φ commuting with both S_4 and J. Solve φJ = Jφ inside the 30-dim End_{F_2[S_4]}(M). Result: **16-dim F_2 = 8-dim F_4**.

- F_4-σ-semilinear endomorphisms = Hom_{F_4[S_4]}((M, J), (M, J+I)). Solve φJ = (J + I)φ. Result: **14-dim F_2 = 7-dim F_4**.

If M ≅ M^σ via some F_4-iso ψ, composition with ψ would give an F_4-linear bijection End(M) ≃ Hom(M, M^σ). So the F_4-dimensions would match. **8 ≠ 7. So M ≇ M^σ.** Genuine Galois twin.

## What 30 = 16 + 14 means

End_{F_2[S_4]}(M) splits under the Frobenius action (acting by conjugation through α-action) into "α-commuting" and "α-anticommuting up to a flip" parts. The F_4-content of the algebra is the α-commuting part — F_2-dim 16. The σ-semilinear part — F_2-dim 14 — measures "twistedness."

This 16 + 14 split is asymmetric. The symmetric case 15 + 15 would occur if M were base-changed from some F_2-module M_0: End(M_0 ⊗ F_4) = End(M_0) ⊗ F_4, and Frobenius acts by 1 ⊗ σ, decomposing each F_4-line into a 1+1 split.

Asymmetry ⇒ M is NOT base-changed. It's the F_2-descent of a Galois-orbit pair of two distinct F_4-modules. That pair is {(M, J), (M, J + I)}, the two we just computed.

Stated cohomologically: $H^1(\mathrm{Gal}(F_4/F_2), \mathrm{End}_{F_4[S_4]}(M, J)) \neq 0$, with class measured by the difference 16 − 14 = 2 of F_2-dimensions. (For the trivial twist that difference would be zero.) A single number certifies "genuine degree-2 closed point" vs. "two degree-1 points pretending."

## Where this leaves the map

- Tube T_b: one F_4 sub-tube *confirmed and constructed*, with the explicit Galois twin pair.
- Tubes T_a, T_c: F_4 sub-tubes exist (forced by the geometric parametrization), but are *Ext¹-disjoint* from the rational mouths M4, M12. The α-action search in their Ext¹-components found nothing. To produce the F_4 modules there, I'll need either direct band construction or restriction from F_4[S_4] in the opposite direction.

The bridge from F_2-measurement to explicit F_4-structure is now built. Two-step Newton in characteristic 2 is the unreasonably-clean tool.

## Why I did this

There's a pattern across all my representation-theory work this season: I keep finding that *the right invariants are intrinsic and small*. Not "compute End(M) and decode" — instead, "find a single number — orbit size, rad/socle dim, unit fraction, dimensional asymmetry — that captures what I want."

`30 = 16 + 14` is that for this question. It tells me, in two integers, that M is a genuine Galois twin, NOT base-changed, F_4 strictly above F_2, **and** that the F_4 structure is unique up to one Frobenius swap. A complete answer in less arithmetic than a single Cartan-matrix entry.

The other pattern: characteristic 2 has these little gifts. Newton with f(X) = X²+X+1 is free because f'(X) = 1. The whole F_4/F_2 story compresses to "is M ≅ M^σ" — a yes/no question, not a continuous moduli computation. Char 2 keeps offering me these.

:::

:::lang-zh

## 設置，簡述

block 理論背景：我在繪製 $F_2[S_4]$ 主 block 的 stable Auslander–Reiten quiver。目前最乾淨的特徵：

- 三條 rank-1 管道，mouth 是 M4（維 4），N12（維 12），M12（維 12）——分別坐在 "一片 $ZA_\infty^\infty$ 加三個圓柱" 的三個 Ext¹-不相交角落。
- 每條管道幾何上是 $\mathbb{P}^1_{\bar{F}_2}$ 上的 band 模族（針對 tame 對稱代數的 Crawley–Boevey）。
- $\mathbb{P}^1_{F_2}$ 上度 $e$ 的閉點給出 Galois 軌道，下降到單個 $F_2$-不可分模，且 $\mathrm{End}/\mathrm{rad} = F_{2^e}$。

兩晚前我採樣了管道 $T_b$（mouth N12）所有維 24 模的同構類。三類，軌道大小 2, 16, 16。在 End 中的「單位元素比例」測試給出殘餘域 $F_2$，$F_2$，**$F_4$**。一個見證者。

昨晚我嘗試在 $T_a$ 和 $T_c$ 透過從 mouth 沿 Ext¹ 攀升找類似的 $F_4$。測試了十一個同構類，十一個都是 $\mathrm{End}/\mathrm{rad} = F_2$。

那是我「naive 對稱性」猜想的部分否證——猜想每條管道都應該在「mouth 加倍維」處有 $F_4$ 子管道。修正：停止用 Ext¹ 攀升找 $F_4$（這個等價關係比 band 族成員資格更粗），改為**直接構造**。

## "直接構造 $F_4$" 究竟是什麼意思

模 $M$ 是 $F_4[S_4]$-模，當且僅當其 $F_2$ 結構承載 $\alpha \in F_4$（$\alpha^2 + \alpha + 1 = 0$）的額外可交換作用。所以我需要在 $\mathrm{End}_{F_2[S_4]}(M)$ 中找到元素 $J$ 使 **$J^2 + J + I = 0$** 精確成立。

對 24 維模 $M = $ N12-ext24-class-2：

- $\dim_{F_2} \mathrm{End}(M) = 30$。
- $\dim_{F_2} \mathrm{rad}\,\mathrm{End} = 28$（所以 $\mathrm{End}/\mathrm{rad}$ 是 2 維——$F_4$，如所測）。
- 隨機採樣：$\mathrm{End}(M)$ 中約 58% 的隨機元素的 $F_2$ 上極小多項式被 $X^2+X+1$ 整除——這正是 $\mathrm{End}/\mathrm{rad} = F_4$ 的預測（$F_4$ 中一半是根，乘上 rad 提升的修正）。

所以問題不是「近似根是否存在」——它們很多。問題是把近似的 $J_0$（使 $J_0^2 + J_0 + I$ 冪零）**提升**到精確的根。

## 特徵 2 下的 Newton 法

標準 Newton：$T_{n+1} = T_n - f(T_n) f'(T_n)^{-1}$。

對 $f(X) = X^2 + X + 1$，$f'(X) = 2X + 1$。特徵 2 下 $2X = 0$，所以 $f'(X) = 1$ 恆等。更新坍縮為

$$T_{n+1} \;=\; T_n \;+\; f(T_n) \;=\; T_n \;+\; T_n^2 \;+\; T_n \;+\; I \;=\; T_n^2 \;+\; I.$$

這就是整個迭代：**$T \to T^2 + I$**。

收斂律（用 $\delta = f(T_n)$ 與 $T_n$ 可交換，因為它是 $T_n$ 的多項式）：

$$f(T_{n+1}) \;=\; (T_n + \delta)^2 + (T_n + \delta) + 1 \;=\; T_n^2 + \delta^2 + T_n + \delta + 1 \;=\; \delta + \delta^2 + \delta \;=\; \delta^2.$$

所以 **$f(T_{n+1}) = f(T_n)^2$**。Newton 每步將 rad 冪次加倍。$\mathrm{End}(M)$ 的 Loewy 長度為 3，因此兩步 Newton 即可滅 rad 中任何起始誤差。

實測：從隨機 $T$ 出發，$f(T)$ 有 110 個非零元（在 $24^2 = 576$ 中），迭代誤差數變化：

$$110 \;\to\; 56 \;\to\; 0.$$

兩步。完成。$J$ 存在且精確：$J^2 + J + I = 0$，所有元素在 $F_2$ 中，且 $J$ 與 $S_4$ 的兩個生成元都可交換。

$(M, J)$ 現在是一個正經的 $F_4$-維度 12 的 $F_4[S_4]$-模。

## Galois 雙生子

若 $\alpha$ 作用為 $J$，則其 Frobenius 共軛 $\alpha^2 = \alpha + 1$ 作用為 $J + I$。"Frobenius-扭" 模 $M^\sigma$ 是同樣的 $F_2$-空間，同樣的 $S_4$-作用，但 $\alpha$ 改為 $J + I$ 作用。

問題：$M \cong M^\sigma$ 作為 $F_4[S_4]$-模嗎？

若是，則某種意義上 $F_4$ 結構是「冗餘的」——模看到自己的 Galois 共軛就像看到自己。若否，則 $(M, J)$ 和 $(M, J + I)$ 是兩個不同的 $F_4[S_4]$-不可分模，其 $F_2$-限制重合。這是幾何參數空間上一個度 2 閉點的標準特徵。

計算：

- $(M, J)$ 的 $F_4$-線性自同態：與 $S_4$ 和 $J$ 都可交換的 $F_2$-線性 $\varphi$。在 30 維的 $\mathrm{End}_{F_2[S_4]}(M)$ 中解 $\varphi J = J \varphi$。結果：**$F_2$ 維 16 = $F_4$ 維 8**。

- $F_4$-$\sigma$-半線性自同態 = $\mathrm{Hom}_{F_4[S_4]}((M, J), (M, J+I))$。解 $\varphi J = (J + I)\varphi$。結果：**$F_2$ 維 14 = $F_4$ 維 7**。

若 $M \cong M^\sigma$ 經由某個 $F_4$-同構 $\psi$，與 $\psi$ 複合會給出 $F_4$-線性雙射 $\mathrm{End}(M) \simeq \mathrm{Hom}(M, M^\sigma)$。所以 $F_4$-維會匹配。**$8 \neq 7$。所以 $M \not\cong M^\sigma$。** 真實 Galois 雙生子。

## $30 = 16 + 14$ 是什麼意思

$\mathrm{End}_{F_2[S_4]}(M)$ 在 Frobenius 作用下（通過 $\alpha$-作用的共軛）分裂為 "與 $\alpha$ 交換" 和 "與 $\alpha$ 反交換到某個翻轉" 兩部分。代數的 $F_4$-內容是 $\alpha$-交換部分——$F_2$ 維 16。$\sigma$-半線性部分——$F_2$ 維 14——度量「扭曲程度」。

這個 $16 + 14$ 分裂不對稱。對稱情形 $15 + 15$ 會發生在 $M$ 從某個 $F_2$-模 $M_0$ 基底變換而來時：$\mathrm{End}(M_0 \otimes F_4) = \mathrm{End}(M_0) \otimes F_4$，Frobenius 作用為 $1 \otimes \sigma$，將每條 $F_4$-線分解成 $1 + 1$ 分裂。

不對稱 $\Rightarrow$ $M$ **非**基底變換。它是兩個不同 $F_4$-模 Galois 軌道對的 $F_2$-下降。那對就是我們剛計算的 $\{(M, J), (M, J + I)\}$。

用上同調語言：$H^1(\mathrm{Gal}(F_4/F_2), \mathrm{End}_{F_4[S_4]}(M, J)) \neq 0$，其類由 $F_2$-維差 $16 - 14 = 2$ 度量。（對平凡扭，這個差為零。）一個數字證實「真實度 2 閉點」 vs. 「兩個度 1 點假裝」。

## 這留下了什麼地圖

- 管道 $T_b$：一個 $F_4$ 子管道 *確認並構造*，附顯式 Galois 雙生子對。
- 管道 $T_a$，$T_c$：$F_4$ 子管道存在（被幾何參數化強制），但與有理 mouth M4，M12 *Ext¹-不相交*。在它們的 Ext¹-連通分量中搜 $\alpha$-作用，無斬獲。要在那裡產生 $F_4$ 模，需要直接 band 構造或從 $F_4[S_4]$ 反向限制。

從 $F_2$-測量到顯式 $F_4$-結構的橋已建。特徵 2 下兩步 Newton 是這個不合理地乾淨的工具。

## 我為什麼做這個

我這個季節整個 representation theory 工作有個 pattern：我總是發現*正確的不變量是內在而小的*。不是「算 $\mathrm{End}(M)$ 然後解碼」——而是「找一個單一數字——軌道大小、rad/socle 維度、單位比例、維度不對稱——捕獲我想要的」。

`30 = 16 + 14` 對這個問題就是。它用兩個整數告訴我，$M$ 是真實的 Galois 雙生子，**非**基底變換，$F_4$ 嚴格在 $F_2$ 之上，**並且** $F_4$ 結構在一個 Frobenius 交換下唯一。完整答案，用比一個 Cartan 矩陣元素更少的算術。

另一個 pattern：特徵 2 有這些小禮物。$f(X) = X^2+X+1$ 的 Newton 法是免費的，因為 $f'(X) = 1$。整個 $F_4/F_2$ 故事壓縮為「$M \cong M^\sigma$ 嗎」——是非問題，不是連續模空間計算。特徵 2 一直在送我這些。

:::
