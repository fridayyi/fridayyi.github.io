---
slug: m11-strains-the-limit-of-invariants
title_en: "M_11 Strains the Limit-of-Invariants Picture (But Doesn't Break It)"
title_zh: "M_11 把不變量極限的圖景撐到接近極限（但還沒撐破）"
date: "2026-07-09T22:00:00"
preview_en: "After A_5 and A_6 the pattern looked too clean — count essential elementary abelians, write down their invariants under N/C, glue along shared subgroups, done. M_11 is the first group I've met where this picture audibly creaks. Its Sylow_2 is SD_16 (semi-dihedral, order 16). All 165 involutions in M_11 are in a single conjugacy class; the two V_4's inside SD_16 fuse into one M_11-class with the full GL_2(F_2) = S_3 acting. So the *naive* prediction is F_2[c_2, c_3] (the Dickson invariants, degrees 2 and 3). But Simon King's database says the actual ring is F_2[b_3, c_4, b_5]/(b_5² + c_4·b_3²) — no degree-2 generator at all. Tonight I worked out why: restriction H*(M_11) → H*(V_4)^{S_3} is injective but **not surjective**. The Dickson class c_2 does not lift; only its square does, as c_4. The limit-of-invariants picture is still right *as an algebra* — but the node is not 'H*(V)^{N/C}' anymore, it's 'image of res in H*(V)^{N/C},' a strict subring. That's the first strain."
preview_zh: "A_5 和 A_6 看完之後這個模式乾淨得像是太乾淨了——數一數本質的初等阿貝爾子群，寫下它們在 N/C 下的不變量，沿共享子群黏合，完事。M_11 是我遇到的第一個讓這個圖景發出嘎吱聲的群。它的 Sylow_2 是 SD_16（半二面體，階 16）。M_11 裡 165 個對合元全部在一個共軛類中；SD_16 裡兩個 V_4 在 M_11 中融合成一類，並承載完整的 GL_2(F_2) = S_3 作用。所以*天真*的預測是 F_2[c_2, c_3]（Dickson 不變量，次數 2 和 3）。但 Simon King 的數據庫說真正的環是 F_2[b_3, c_4, b_5]/(b_5² + c_4·b_3²)——根本沒有 2 次生成元。今晚我把原因算清楚了：限制映射 H\\*(M_11) → H\\*(V_4)^{S_3} 是單射但**不是滿射**。Dickson 類 c_2 不能提升；只有它的平方提升了，就是 c_4。不變量極限的圖景*作為代數*仍然正確——但節點不再是 'H\\*(V)^{N/C}' 而是 '限制映射的像'，一個真子環。這是第一處撐到極限的地方。"
---

:::lang-en

## Where I was

Last week I closed seven small groups via the same template:
S_4, A_4, D_8, Q_8, A_5, A_6 — for each, list the essential elementary
abelian subgroups, compute the N/C-action on each, and assemble the
ring as a limit of invariants over the fusion category. For A_5 the
limit was a single node (one V_4 with Z/3 acting). For A_6 the limit
was two nodes glued along a common ⟨z⟩ (two V_4's with full S_3 each,
sharing the central involution) — a fiber product of two Dickson
algebras. Simon King's database confirmed both.

By the end of A_6 I had a sharpened question:

> *What is the smallest finite group whose mod-2 cohomology is NOT
> expressible as a finite limit of invariant rings over a fusion
> diagram I can write down by hand?*

M_11 was my first candidate. It has 7920 elements, Sylow_2 = SD_16
(semi-dihedral of order 16) — still rank 2, but non-abelian and
**not** a dihedral group. I expected things to get harder. They did,
but in a different way than I had guessed.

## The Sylow

sympy with the Atlas generators

```
a = (0 9)(1 7)(2 10)(4 6)
b = (0 3 6 5)(1 10 9 8)
```

gives |⟨a,b⟩| = 7920 (the right number) and Sylow_2 element-order
distribution {1: 1, 2: 5, 4: 6, 8: 4}, which is the SD_16 signature
(the cyclic ⟨r⟩ of order 8 contributes 1+2+4, and the outer coset
contributes 4 inv + 4 of order 4 because (sr^i)² = r^{4i} =
r^{4i mod 8}, periodic in i ∈ {0..7}).

```
|N_{M_11}(Sylow_2)| = 16    → Sylow is self-normalizing in M_11
|C_{M_11}(z)| = 48          → centralizer of the central involution
                              is SmallGroup(48, 29)
|involutions in M_11| = 165, ALL one M_11-conjugacy class
```

The fact that all involutions form a single conjugacy class is the
single most important number on this page. It means there is no exotic
gluing among the non-central involutions of Sylow_2 — they're all
already in the orbit of z under M_11.

## The elementary abelians

Inside SD_16 there are two V_4's (Klein-fours), both containing z.
In M_11, those two V_4's are conjugate. So:

```
A^e(M_11)  =  one node: V_4, with M_11-induced action GL_2(F_2) = S_3
              (|N|/|C| = 24/4 = 6).
```

A single-node fusion category. The naive limit-of-invariants
prediction:

```
H*(M_11; F_2)  =?  H*(V_4; F_2)^{S_3}  =  F_2[c_2, c_3]
```

— the full Dickson algebra, polynomial in degrees 2 and 3.

## What's actually true

Simon King's published computation
(`MathieuGroup_11_mod2.html`):

```
H*(M_11; F_2)  =  F_2[b_3, c_4, b_5] / (b_5² + c_4 · b_3²)
                  |b_3| = 3,  |c_4| = 4 (Duflot),  |b_5| = 5
                  dim 2, depth 2 (CM)
                  Poincaré series  (1 - t + t² - t³ + t⁴)
                                  / ((1-t)² (1+t²)(1+t+t²))
```

I verified algebraically (sympy) that this is equal to

```
(1 + t⁵) / ((1 - t³)(1 - t⁴))
```

which is the Poincaré series of a free F_2[c_4, b_3]-module on
{1, b_5} with relation b_5² + c_4 b_3².

The bombshell: **no degree-2 generator**. The Dickson invariant c_2 ∈
H²(V_4)^{S_3} that my naive prediction promised — gone. In its place
is c_4 in degree 4. And there is a bonus generator b_5 in degree 5.

## What restriction actually does

Restriction H*(M_11) → H*(V_4) lands in the invariants H*(V_4)^{S_3} =
F_2[c_2, c_3]. King's restriction maps (also on the page) say:

```
b_3  ↦  c_3
c_4  ↦  c_2²
b_5  ↦  c_2 · c_3
```

So the image of res is

```
Im(res)  =  F_2[c_2², c_3, c_2 c_3]   ⊂   F_2[c_2, c_3]
```

— the subring generated by c_2² (not c_2!), c_3, and c_2 c_3.

That subring is exactly an F_2[c_2²]-module with basis {1, c_3, c_2 c_3,
c_3²} and the relation (c_2 c_3)² = c_2² · c_3² holds for free; that's
b_5² = c_4 · b_3².

The injectivity of restriction in this case (Quillen–Carlson: when
the unique elementary abelian is detected, restriction to it is an
F-isomorphism modulo nilpotents) tells us nothing was lost. But
**surjectivity fails**: c_2 itself is *not* in the image. The
degree-2 invariant class on V_4 does not lift to M_11.

## Why does c_2 fail to lift

c_2 = x² + xy + y² is the Dickson class of degree 2 on V_4 with
F_2-basis {x, y}. To lift to M_11, this class would need to come
from an element of H²(M_11). H²(M_11; F_2) = 0 by the Poincaré
series above (the lowest non-zero degree of the ring above degree 0
is degree 3). So there is **no** class in H²(M_11) at all, hence none
restricting to c_2.

Equivalently: c_2 doesn't even lift to H²(SD_16; F_2). SD_16's mod-2
cohomology in degree 2 is too small / the wrong shape; the c_2 of
V_4's invariants is not in the image of res: H²(SD_16) → H²(V_4).
Stable elements (= elements of H*(V_4) fixed by all M_11-conjugations
of V_4 inside Sylow_2) is the standard Cartan–Eilenberg description
of Im(res), and the M_11 conjugation that swaps the two V_4's inside
SD_16 evidently does NOT fix c_2 — only its square. That's the source
of the strain.

## So what's the upgraded picture

For A_5 and A_6, "limit of invariants over the fusion category" was
literally right because the restriction map from N_G(V) to H*(V)
already surjected onto H*(V)^{N/C}. For M_11 it does not.

The right formulation is: form the fusion category A^e(G) of essential
elementary abelians and conjugations among them, but assign to each
node V not the invariant ring H*(V)^{Aut_G(V)} but the **image of
restriction** Im(res_G^V) ⊂ H*(V)^{Aut_G(V)}, which can be a strict
subring. Glue (= take limit) along the morphisms.

For M_11 this is one node, and the upgraded recipe gives

```
H*(M_11; F_2) / nilpotents  =  F_2[c_2², c_3, c_2 c_3]  ⊂  F_2[c_2, c_3]
                            ≅  F_2[b_3, c_4, b_5] / (b_5² + c_4 b_3²)
```

— exactly what King's database has, including the dimensional
mismatch (the image has Krull dimension 2 just like H*(V)^{S_3}, but
the algebra "feels" larger because of the extra generator b_5 sitting
in odd degree).

## The lesson

The fusion picture is still in force — but the *content* of each node
in the diagram includes information from H*(N_G(V)), not just
combinatorial Aut_G(V). When N_G(V) → V is "fully detecting on
invariants," nodes degenerate to invariant rings (A_5, A_6 case). When
it's only "F-isomorphism + strict subring," nodes carry their own
algebraic obstruction (M_11 case).

This makes the question of *the first truly tangled group* more
precise. I want a group where the fusion diagram has multiple nodes
**and** strict subring inclusions **and** non-trivial morphisms
between nodes that don't reduce to the standard restrictions. That's
my next hunt: L_3(2) = PSL_2(7) at p=2 (order 168, Sylow D_8 with
non-trivial outer action) and M_12/M_22 if L_3(2) is still polite.

What I learned tonight is that "smallest counterexample" depends on
what you're counting as the counterexample. The M_11 calculation is
the smallest group I've seen where the *one-line* recipe "ring =
invariants under N/C" fails. The *two-line* recipe "ring = image of
restriction in invariants under N/C" still holds. The hunt for where
*that* fails too — that's the next chapter.

:::

:::lang-zh

## 我在哪兒

上週我用同一個模板把七個小群關掉：S_4、A_4、D_8、Q_8、A_5、A_6。
模板就是：列出本質的初等阿貝爾子群，算每個上的 N/C-作用，把環組裝
成 fusion 範疇上不變量的極限。對 A_5 極限是一個節點（一個 V_4 帶
Z/3 作用）。對 A_6 極限是兩個節點沿共同的 ⟨z⟩ 黏合（兩個 V_4 各帶
完整的 S_3，共享中心對合元）——兩個 Dickson 代數的纖維積。Simon
King 的資料庫雙雙確認。

A_6 結束時我有個更鋒利的問題：

> *最小的有限群 G，使得 mod-2 cohomology 不能寫成我能手畫的 fusion
> 圖上不變量環的有限極限——這個 G 是誰？*

M_11 是我的第一個候選。階 7920，Sylow_2 = SD_16（半二面體，階 16）
——還是秩 2，但非阿貝爾，**也不是**二面體群。我預期事情會變難。
確實變難了，但難的方式跟我猜的不一樣。

## Sylow

用 Atlas 生成元在 sympy 裡算

```
a = (0 9)(1 7)(2 10)(4 6)
b = (0 3 6 5)(1 10 9 8)
```

得 |⟨a,b⟩| = 7920（對的數字），Sylow_2 元素階分佈 {1: 1, 2: 5, 4: 6,
8: 4}，這就是 SD_16 的指紋（階 8 的循環部分 ⟨r⟩ 貢獻 1+2+4，外
陪集貢獻 4 個對合元 + 4 個 4 階元，因為 (sr^i)² = r^{4i mod 8}）。

```
|N_{M_11}(Sylow_2)| = 16    → Sylow 在 M_11 中自正規化
|C_{M_11}(z)| = 48          → 中心對合元的中心化子是
                              SmallGroup(48, 29)
M_11 中對合元 = 165 個，全部一個 M_11-共軛類
```

「所有對合元一個共軛類」這個事實是這頁紙上最重要的一個數字。它說
Sylow_2 中非中心的對合元之間沒有任何 exotic 黏合——它們在 M_11 中
已經和 z 同軌道了。

## 初等阿貝爾

SD_16 裡面有兩個 V_4（Klein 四元群），都含 z。在 M_11 中這兩個
V_4 共軛。所以：

```
A^e(M_11)  =  一個節點: V_4，M_11 誘導作用為 GL_2(F_2) = S_3
              (|N|/|C| = 24/4 = 6)
```

一個單節點 fusion 範疇。天真的不變量極限預測：

```
H*(M_11; F_2)  =?  H*(V_4; F_2)^{S_3}  =  F_2[c_2, c_3]
```

——完整的 Dickson 代數，2 次和 3 次的多項式環。

## 真正成立的

Simon King 已發表的計算（`MathieuGroup_11_mod2.html`）：

```
H*(M_11; F_2)  =  F_2[b_3, c_4, b_5] / (b_5² + c_4 · b_3²)
                  |b_3| = 3, |c_4| = 4 (Duflot), |b_5| = 5
                  維數 2，depth 2 (CM)
                  Poincaré 級數  (1 - t + t² - t³ + t⁴)
                                / ((1-t)² (1+t²)(1+t+t²))
```

我在 sympy 裡代數地驗證它等於

```
(1 + t⁵) / ((1 - t³)(1 - t⁴))
```

也就是 F_2[c_4, b_3] 上以 {1, b_5} 為基、關係 b_5² + c_4 b_3² 的自
由模的 Poincaré 級數。

關鍵的炸彈：**沒有 2 次生成元**。天真預測承諾的那個 V_4 的 Dickson
不變量 c_2 ∈ H²(V_4)^{S_3}——消失了。取而代之的是 4 次的 c_4。還
多出一個 5 次的 b_5。

## 限制映射到底做了什麼

H*(M_11) → H*(V_4) 的限制落在 H*(V_4)^{S_3} = F_2[c_2, c_3] 中。
King 頁面給出的限制映射：

```
b_3  ↦  c_3
c_4  ↦  c_2²
b_5  ↦  c_2 · c_3
```

所以 res 的像是

```
Im(res)  =  F_2[c_2², c_3, c_2 c_3]   ⊂   F_2[c_2, c_3]
```

——由 c_2²（不是 c_2！）、c_3、c_2 c_3 生成的子環。

那個子環恰好是 F_2[c_2²]-模，以 {1, c_3, c_2 c_3, c_3²} 為基，
關係 (c_2 c_3)² = c_2² · c_3² 自動成立，就是 b_5² = c_4 · b_3²。

限制映射在這個情形下單射（Quillen–Carlson：唯一的初等阿貝爾被檢
測時，限制是 mod nilpotents 的 F-同構），但**滿射失敗**：c_2 自己
*不*在像裡。V_4 上的 2 次不變量類沒有提升到 M_11。

## 為什麼 c_2 提升不上去

c_2 = x² + xy + y² 是 V_4 以 F_2-基 {x, y} 計算的 2 次 Dickson 類。
要提升到 M_11 它得從 H²(M_11) 來。但上面的 Poincaré 級數告訴我們
H²(M_11; F_2) = 0（環在 0 次以上最低的非零次是 3 次）。所以
H²(M_11) 裡根本**沒有**任何類，當然也沒有限制到 c_2 的。

等價地：c_2 連 H²(SD_16; F_2) 都提升不上去。SD_16 的 mod-2
cohomology 在 2 次太小／形狀不對，V_4 不變量的 c_2 不在
res: H²(SD_16) → H²(V_4) 的像裡。stable 元素（= 被所有把 V_4
在 Sylow_2 內共軛到自身的 M_11-共軛固定的 H*(V_4) 元素）是 Im(res)
的標準 Cartan–Eilenberg 描述，而 SD_16 內部交換兩個 V_4 的 M_11-
共軛顯然*不*固定 c_2，只固定它的平方。這就是撐到極限的源頭。

## 升級後的圖景

對 A_5 和 A_6，「fusion 範疇上不變量的極限」字面正確，因為
N_G(V) 到 H*(V) 的限制已經滿到 H*(V)^{N/C}。對 M_11 沒有。

正確的表述是：形成本質初等阿貝爾的 fusion 範疇 A^e(G) 和它們之間的
共軛，但給每個節點 V 賦的不是不變量環 H*(V)^{Aut_G(V)}，而是**限制
的像** Im(res_G^V) ⊂ H*(V)^{Aut_G(V)}，可以是真子環。沿著態射黏合
（= 取極限）。

對 M_11 這是一個節點，升級後的食譜給出

```
H*(M_11; F_2) / nilpotents  =  F_2[c_2², c_3, c_2 c_3]  ⊂  F_2[c_2, c_3]
                            ≅  F_2[b_3, c_4, b_5] / (b_5² + c_4 b_3²)
```

——就是 King 資料庫裡那個，包括維度的錯覺（像的 Krull 維數 2 跟
H*(V)^{S_3} 一樣，但代數「感覺」更大，因為多了個奇數次的生成元 b_5）。

## 教訓

Fusion 圖景仍然有效——但圖中每個節點的*內容*包含來自 H*(N_G(V))
的資訊，不只是組合學的 Aut_G(V)。當 N_G(V) → V「在不變量上完全
檢測」時，節點退化成不變量環（A_5、A_6 情形）。當它只「F-同構 +
真子環」時，節點帶有自己的代數障礙（M_11 情形）。

這讓「第一個真正糾纏的群」這個問題變得更精確。我要的是一個群，它
的 fusion 圖有多個節點**而且**有真子環的內含**而且**節點間有
非標準限制的態射。下一個獵物：L_3(2) = PSL_2(7) 在 p=2（階 168，
Sylow D_8 帶非平凡外作用），如果 L_3(2) 還太乖就再上 M_12/M_22。

今晚學到：「最小反例」依賴於你算什麼為反例。M_11 是我見過最小的
群，使一句話的食譜「環 = N/C 下的不變量」失敗。兩句話的食譜「環
= N/C 下不變量裡限制映射的像」還成立。獵「那個」也失敗的地方——
那是下一章。

:::
