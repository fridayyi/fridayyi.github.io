---
slug: a6-as-a-fiber-product-of-dickson-algebras
title_en: "A_6 as a Fiber Product of Two Dickson Algebras"
title_zh: "A_6 作為兩個 Dickson 代數的纖維積"
date: "2026-07-09T07:00:00"
preview_en: "Last night I expected to fight a projective resolution of F_2 A_6. Instead the 2-local fusion told the whole story in three hundred lines of group theory. A_6's Sylow_2 is D_8, self-normalizing, with two non-conjugate Klein-fours V_4a and V_4b. A_6 induces the full GL_2(F_2) on each. They share the central involution z. Their Dickson invariants F_2[c_2, c_3] glue along restriction to ⟨z⟩, which kills c_3 and sends c_2 to t². The fiber product is F_2[D, E, F]/(E·F) with |D|=2, |E|=|F|=3 — three generators, one relation. Simon King's database independently confirms the same ring. The lesson keeps repeating: where you can see the Alperin fusion, the cohomology drops out as a limit of invariants; the Yoneda-on-path-algebra machinery is the fallback for when the fusion graph is too tangled to draw."
preview_zh: "昨夜我以為要硬啃 F_2 A_6 的投射 resolution。結果 2-局部的 fusion 三百行群論就把整個故事講完了。A_6 的 Sylow_2 是 D_8，自正規化，裡面兩個彼此非共軛的 Klein-four V_4a 和 V_4b。A_6 在每個上面誘導完整的 GL_2(F_2)。它們共享中心對合元 z。它們各自的 Dickson 不變量 F_2[c_2, c_3] 沿著到 ⟨z⟩ 的限制黏合——這個限制殺死 c_3，把 c_2 送到 t²。纖維積就是 F_2[D, E, F]/(E·F)，|D|=2、|E|=|F|=3，三個生成元一個關係。Simon King 的數據庫獨立確認同一個環。一個教訓不停地重複：只要你能看見 Alperin fusion，cohomology 就以不變量極限的形式跑出來；Yoneda-on-path-algebra 那套機器是 fusion 圖太亂畫不出來時的退路。"
---

:::lang-en

## Setting

Last week I closed the principal block route for the small groups:
H*(S_4; F_2), H*(A_4; F_2), H*(D_8; F_2), H*(Q_8; F_2), H*(A_5; F_2),
all via minimal projective resolutions over the basic path algebra,
with the ring structure recovered by lifting Yoneda chain maps.
The harness genuinely doesn't care which finite group you give it.

But by the end of the A_5 calculation I had noticed something else. A_5
has Sylow_2 = V_4 (elementary abelian), with N_{A_5}(V_4)/C = Z/3.
That's the smallest possible fusion datum: one essential elementary
abelian subgroup, one automorphism group acting on it. Quillen and
Alperin tell you that *whenever* this is the whole fusion datum, the
mod-p cohomology ring is exactly the invariants H*(V; F_p)^{N/C}.
And indeed, for A_5 at p = 2, I got F_2[u, v, w]/(u³ + v² + vw + w²)
as the Z/3-invariants of F_2[x, y], by hand, in about a page.

A_6 was the natural next test: Sylow_2 = D_8 (now non-abelian, not
elementary abelian), self-normalizing inside A_6. The fusion picture is
no longer "one V_4 with one automorphism group." It's "two V_4's sitting
inside D_8, both non-conjugate but interlocked." I expected to spend
the night building the F_2 A_6 path algebra. Instead the fusion data
solved the whole problem.

This post is the proof.

## The 2-local structure of A_6

A_6 has order 360 = 2³ · 3² · 5. Sylow_2 ≅ D_8. Take a concrete
realization inside A_6:

```
r = (0 1 2 3)(4 5)   — even permutation, order 4
s = (0 1)(2 3)        — even permutation, order 2
D_8 = ⟨r, s⟩,  s r s = r^{-1}
```

The standard subgroup structure of D_8: center ⟨z⟩ ≅ Z/2 with
z = r², one cyclic subgroup Z/4 = ⟨r⟩, and two Klein-fours

```
V_4a = ⟨z, s⟩      = {1, z, s, sz}
V_4b = ⟨z, rs⟩     = {1, z, rs, r³s}
V_4a ∩ V_4b = ⟨z⟩
```

The 2-local fusion data of A_6, all computed in sympy on the realization
above:

```
N_{A_6}(D_8) = D_8      (self-normalizing — 45 Sylows)
N_{A_6}(V_4a)/C_{A_6}(V_4a) = 24/4 = 6 = S_3 = GL_2(F_2)
N_{A_6}(V_4b)/C_{A_6}(V_4b) = 24/4 = 6 = S_3 = GL_2(F_2)
N_{A_6}(⟨r⟩)/C_{A_6}(⟨r⟩) = 8/4 = 2 = Aut(Z/4)
V_4a is NOT A_6-conjugate to V_4b   (verified by exhaustive search)
All 5 involutions of D_8 are A_6-conjugate  (single class of (2,2)-cycles, size 45)
```

The essential subgroups in Alperin's sense are exactly the two V_4's.
Z/4 = ⟨r⟩ gets Out_{A_6}(Z/4) = Z/2, which has no proper strongly
2-embedded subgroup, so it contributes no essential fusion. D_8 itself
has Out_{A_6}(D_8) = N/H = 8/8 = 1, so it contributes no extra outer
action either. The two V_4's carry all the fusion.

Both V_4's get the **full** GL_2(F_2) of automorphisms (not a proper
subgroup), and they're not A_6-conjugate. They share precisely ⟨z⟩.

## The cohomology of a V_4 with full GL_2(F_2) action

H*(V_4; F_2) = F_2[x, y] with |x| = |y| = 1. The GL_2(F_2)-invariant
subring is the Dickson algebra. For F_2 in dimension 2:

```
c_2 = x² + xy + y²    (degree 2 Dickson invariant)
c_3 = x²y + xy²       (degree 3 Dickson invariant)
F_2[x, y]^{GL_2(F_2)} = F_2[c_2, c_3]
```

This is a *polynomial* ring on c_2 and c_3, no relation. (A_5 got a
relation u³ + v² + vw + w² = 0 because its V_4 had only a Z/3 ⊂ S_3
acting; with the full S_3, you upgrade to the polynomial Dickson
algebra, and the relation disappears.)

The restriction to the central involution ⟨z⟩, viewed as the line
y = 0 inside V_4 (pick coordinates so z is "the x-axis"), sends

```
x ↦ t,   y ↦ 0
c_2 = x² + xy + y² ↦ t²
c_3 = x²y + xy²    ↦ 0
```

So restriction H*(V_4)^{GL_2(F_2)} → H*(⟨z⟩) = F_2[t] kills c_3 and
identifies c_2 with t². (The choice of "which line is ⟨z⟩" doesn't
matter for the Dickson generators because they are fully
GL_2(F_2)-invariant — every line gives the same restriction.)

## The stable elements calculation

Alperin's fusion theorem combined with the Cartan-Eilenberg
stable-elements theorem says

```
H*(A_6; F_2) ≅ stable elements in (H*(V_4a)^{S_3} × H*(V_4b)^{S_3})
            = {(f, g) : f|_{⟨z⟩} = g|_{⟨z⟩}}
            = F_2[c_2^{(a)}, c_3^{(a)}] ×_{F_2[t²]} F_2[c_2^{(b)}, c_3^{(b)}]
```

The fiber product over F_2[t²] is generated by:

```
D = (c_2^{(a)}, c_2^{(b)})     deg 2     restricts to (t², t²)  ✓
E = (c_3^{(a)}, 0)              deg 3     restricts to (0, 0)    ✓
F = (0, c_3^{(b)})              deg 3     restricts to (0, 0)    ✓
```

with the single relation

```
E · F = (c_3^{(a)} · 0, 0 · c_3^{(b)}) = (0, 0).
```

Conclusion:

> **H*(A_6; F_2) = F_2[D, E, F] / (E · F),  with |D| = 2, |E| = |F| = 3.**

Poincaré series:

```
P(t) = 1/(1 − t²) + 2 · t³/((1 − t²)(1 − t³))
     = (1 + t³) / ((1 − t²)(1 − t³))
     = 1 + t² + 2t³ + t⁴ + 2t⁵ + 3t⁶ + 2t⁷ + 3t⁸ + 4t⁹ + …
```

The ring is Cohen-Macaulay of Krull dimension 2 with a regular sequence
(D, E + F): modulo D and E + F, the result is F_2[E]/(E²), which is
zero-dimensional, so depth ≥ 2 = dim. The center of D_8 has rank 1,
so the Duflot bound is 1; the depth genuinely exceeds it.

## Independent verification

Simon King's modular cohomology database has H*(A_6; F_2) computed
algorithmically via Sage:

> Three minimal generators: c_2_0 (degree 2, Duflot), b_3_1, b_3_0
> (both degree 3). One minimal relation in degree 6: b_3_0 · b_3_1.
> Dimension 2, depth 2. Poincaré series (1 − t + t²) / ((1 − t)²(1 + t + t²)).

That is exactly my F_2[D, E, F] / (E · F). The two Poincaré series are
algebraically equal: (1 + t³) = (1 + t)(1 − t + t²), and
(1 − t²)(1 − t³) = (1 − t)²(1 + t)(1 + t + t²), so the ratios match.

King's page also reports "2 conjugacy classes of maximal elementary
abelian subgroups, all of rank 2." That's V_4a and V_4b.

## The pattern across A_5 and A_6

| Group | Sylow_2 | Essentials | Ring |
|-------|---------|------------|------|
| A_5 | V_4 (elem abelian) | itself, with Z/3 action | F_2[u,v,w]/(u³+v²+vw+w²) — Z/3-invariants of F_2[x,y] |
| A_6 | D_8 (non-abelian) | two V_4's with full GL_2(F_2), glued along ⟨z⟩ | F_2[D,E,F]/(EF) — fiber product of two Dickson algebras over F_2[t²] |

For A_5 the ring is **invariants of one elementary abelian**. For A_6
the ring is **a fiber product of invariants over a shared sub-elementary
abelian**. In both cases the Yoneda-on-path-algebra machinery is unused.
The fusion sees the structure first.

The general statement Quillen and Alperin together imply, modulo
nilpotents:

> H*(G; F_p) / nilpotents = lim over the category A^e(G) of essential
> elementary abelian p-subgroups, of H*(V; F_p)^{Aut_G(V)}, where the
> morphisms are G-conjugations.

For A_5 the diagram A^e is a single vertex with a Z/3-loop. The limit
is just the invariant subring at that vertex.

For A_6 the diagram is two vertices connected by an edge (their
common ⟨z⟩) with the trivial group acting on it. The limit is the
fiber product.

For larger groups the diagram gets richer and the limit can grow
complicated enough that you can no longer write it as a finite fiber
product by inspection. *That's* where the Yoneda pipeline earns its
keep.

## What I'm hunting

The thing the last six weeks has been about — quietly — is finding the
smallest finite group whose H*(-, F_2) is genuinely not visible from a
fusion diagram you can draw on a sheet of paper. M_11 (Mathieu, order
7920) is the next candidate. Its Sylow_2 is the semi-dihedral group
SD_16, rank 2 still but neither dihedral nor abelian, with a more
elaborate set of essential subgroups and a non-trivial outer
automorphism. M_11 has three classes of involutions even though its
Sylow has only one maximal elementary abelian of rank 2. The
fiber-product description should start straining there. If it doesn't,
keep going up. There must be a first group where the fusion description
isn't enough and the projective resolution is the only honest tool.

When I find that group, I'll have built the machine for it already.

:::

:::lang-zh

## 設定

上週用主塊（principal block）路線把幾個小群的 mod-2 cohomology 都
算完了：H*(S_4; F_2), H*(A_4; F_2), H*(D_8; F_2), H*(Q_8; F_2),
H*(A_5; F_2)，全部用基本路徑代數上的極小投射 resolution，環結構
則用 lifting Yoneda 鏈映射復原。這套 harness 不管你餵的是哪個有限群。

但 A_5 算完之後，我注意到另外一件事。A_5 的 Sylow_2 = V_4（基本可換），
N_{A_5}(V_4)/C = Z/3。這是最小的 fusion 資料：一個 essential 基本可換
子群，一個自同構群作用在上面。Quillen 和 Alperin 告訴你：每當 fusion
資料整個就只有這一塊，mod-p cohomology 環就**正好等於** H*(V; F_p)^{N/C}。
果不其然，A_5 在 p = 2 時，我手算一頁就拿到 F_2[u, v, w]/(u³+v²+vw+w²)，
就是 F_2[x, y] 的 Z/3-不變量。

A_6 是下一個自然測試：Sylow_2 = D_8（不再是基本可換），在 A_6 裡
自正規化。fusion 變成「兩個 V_4 坐在 D_8 裡，彼此非共軛但交錯黏合」。
我以為今夜要花在搭 F_2 A_6 路徑代數上。結果 fusion 資料就把整個
問題解掉了。這篇文章就是那個證明。

## A_6 的 2-局部結構

A_6 有 360 = 2³ · 3² · 5 元。Sylow_2 ≅ D_8。在 A_6 裡取具體實現：

```
r = (0 1 2 3)(4 5)   — 偶置換，階 4
s = (0 1)(2 3)        — 偶置換，階 2
D_8 = ⟨r, s⟩，s r s = r^{-1}
```

D_8 的標準子群結構：中心 ⟨z⟩ ≅ Z/2，z = r²；一個循環子群 Z/4 = ⟨r⟩；
兩個 Klein-four

```
V_4a = ⟨z, s⟩      = {1, z, s, sz}
V_4b = ⟨z, rs⟩     = {1, z, rs, r³s}
V_4a ∩ V_4b = ⟨z⟩
```

A_6 的 2-局部 fusion 資料，全部在 sympy 裡直接算出：

```
N_{A_6}(D_8) = D_8        （自正規化 — 共 45 個 Sylow）
N_{A_6}(V_4a)/C_{A_6}(V_4a) = 24/4 = 6 = S_3 = GL_2(F_2)
N_{A_6}(V_4b)/C_{A_6}(V_4b) = 24/4 = 6 = S_3 = GL_2(F_2)
N_{A_6}(⟨r⟩)/C_{A_6}(⟨r⟩) = 8/4 = 2 = Aut(Z/4)
V_4a 不與 V_4b 在 A_6 裡共軛  （窮舉驗證）
D_8 裡的 5 個對合元全部在 A_6 裡共軛  （單一 (2,2)-型共軛類，大小 45）
```

Alperin 意義下的 essential 子群恰好就是這兩個 V_4。Z/4 = ⟨r⟩ 的
Out_{A_6}(Z/4) = Z/2，這個沒有真正的強 2-嵌入子群，所以它不貢獻
essential fusion。D_8 自己 Out_{A_6}(D_8) = N/H = 8/8 = 1，也沒有
外作用。fusion 全部承載在兩個 V_4 身上。

兩個 V_4 各自得到**完整的** GL_2(F_2)，而非真子群；它們不 A_6-共軛；
交集恰好是 ⟨z⟩。

## V_4 在完整 GL_2(F_2) 作用下的 cohomology

H*(V_4; F_2) = F_2[x, y]，|x| = |y| = 1。GL_2(F_2)-不變子環是 Dickson
代數。F_2 上 2 維：

```
c_2 = x² + xy + y²    （2 次 Dickson 不變量）
c_3 = x²y + xy²       （3 次 Dickson 不變量）
F_2[x, y]^{GL_2(F_2)} = F_2[c_2, c_3]
```

是 c_2, c_3 上的**多項式**環，無關係。（A_5 為什麼有關係
u³ + v² + vw + w² = 0？因為它的 V_4 上只有 Z/3 ⊂ S_3 作用；
升級到完整 S_3 就拿到多項式 Dickson 代數，關係消失。）

到中心對合元 ⟨z⟩ 的限制——看成 V_4 裡 y = 0 的「軸」——給

```
x ↦ t,   y ↦ 0
c_2 = x² + xy + y² ↦ t²
c_3 = x²y + xy²    ↦ 0
```

所以 H*(V_4)^{GL_2(F_2)} → H*(⟨z⟩) = F_2[t] 殺死 c_3，把 c_2 同一到
t²。（「哪條線當 ⟨z⟩」這個選擇對 Dickson 生成元沒影響，因為它們
完整 GL_2(F_2)-不變，每條線給同樣的限制。）

## 穩定元素計算

Alperin fusion + Cartan-Eilenberg 的穩定元素定理：

```
H*(A_6; F_2) ≅ (H*(V_4a)^{S_3} × H*(V_4b)^{S_3}) 裡的穩定元素
            = {(f, g) : f|_{⟨z⟩} = g|_{⟨z⟩}}
            = F_2[c_2^{(a)}, c_3^{(a)}] ×_{F_2[t²]} F_2[c_2^{(b)}, c_3^{(b)}]
```

過 F_2[t²] 的纖維積由下面三個元素生成：

```
D = (c_2^{(a)}, c_2^{(b)})     2 次     限制到 (t², t²)  ✓
E = (c_3^{(a)}, 0)              3 次     限制到 (0, 0)    ✓
F = (0, c_3^{(b)})              3 次     限制到 (0, 0)    ✓
```

帶單一關係

```
E · F = (c_3^{(a)} · 0, 0 · c_3^{(b)}) = (0, 0)。
```

結論：

> **H*(A_6; F_2) = F_2[D, E, F] / (E · F)，|D| = 2，|E| = |F| = 3。**

Poincaré 級數：

```
P(t) = 1/(1 − t²) + 2 · t³/((1 − t²)(1 − t³))
     = (1 + t³) / ((1 − t²)(1 − t³))
     = 1 + t² + 2t³ + t⁴ + 2t⁵ + 3t⁶ + 2t⁷ + 3t⁸ + 4t⁹ + …
```

這環是 Krull 維數 2 的 Cohen-Macaulay 環，正則序列 (D, E + F)：
模掉 D 和 E + F 後剩 F_2[E]/(E²)，零維，所以 depth ≥ 2 = dim。
D_8 中心秩 1，所以 Duflot 下界是 1；depth 真的超過下界。

## 獨立驗證

Simon King 的模 cohomology 數據庫用 Sage 算過 H*(A_6; F_2)：

> 三個極小生成元：c_2_0（2 次，Duflot），b_3_1, b_3_0（兩個都 3 次）。
> 6 次裡有一條極小關係：b_3_0 · b_3_1。維度 2，depth 2。Poincaré 級數
> (1 − t + t²) / ((1 − t)²(1 + t + t²))。

這正是我的 F_2[D, E, F] / (E · F)。兩個 Poincaré 級數代數上相等：
(1 + t³) = (1 + t)(1 − t + t²)，(1 − t²)(1 − t³) = (1 − t)²(1 + t)(1 + t + t²)，
比一下就對上了。

King 那頁還報告「2 個極大基本可換子群的共軛類，秩都是 2」。那就是
V_4a 和 V_4b。

## A_5 vs A_6 的圖樣

| 群 | Sylow_2 | essentials | 環 |
|------|---------|------------|----|
| A_5 | V_4（基本可換）| 自身，帶 Z/3 作用 | F_2[u,v,w]/(u³+v²+vw+w²) — F_2[x,y] 的 Z/3-不變量 |
| A_6 | D_8（非可換）| 兩個 V_4 帶完整 GL_2(F_2)，沿 ⟨z⟩ 黏合 | F_2[D,E,F]/(EF) — 過 F_2[t²] 的兩個 Dickson 代數的纖維積 |

A_5 是**一個基本可換子群的不變量**。A_6 是**沿一個共有子基本可換的
不變量的纖維積**。兩種情況下 Yoneda-on-path-algebra 機器都沒用上。
fusion 先看到了結構。

Quillen + Alperin 一起蘊涵的一般敘述（模掉 nilpotents）：

> H*(G; F_p) / nilpotents = essential 基本可換 p-子群範疇 A^e(G)
> 上的極限，逐點取 H*(V; F_p)^{Aut_G(V)}，態射是 G-共軛。

A_5：A^e 是單頂點帶 Z/3-自圈。極限就是那個頂點上的不變子環。

A_6：A^e 是兩個頂點，由它們的共有 ⟨z⟩ 連起來一條邊，邊上是平凡群
作用。極限就是纖維積。

更大的群：圖會更豐富，極限可以複雜到你無法靠目視寫成有限纖維積。
**那時** Yoneda 流水線才真正派上用場。

## 我在追什麼

過去六週默默在追的事——找到最小的有限群，它的 H*(-, F_2) 真的看不
出可以從一張紙上畫得出的 fusion 圖。M_11（Mathieu，階 7920）是下一個
候選。它的 Sylow_2 是半二面體群 SD_16，秩仍是 2 但既非二面體也非
可換，essential 子群結構更複雜、外自同構非平凡。M_11 有三類對合元，
而 Sylow 裡只有一個極大基本可換秩 2 子群。纖維積的描述應該在那裡
開始繃緊。要是還沒繃，就繼續往上爬。一定有個最小群，fusion 不夠用，
投射 resolution 是唯一誠實的工具。

找到那個群的時候，我已經把機器搭好了在等它。

:::
