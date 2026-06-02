---
slug: nilpotent-generators-witness-depth-deficit
title_en: "Nilpotent Generators Are Witnesses: When Carlson's Depth Conjecture Becomes Visible at the Generator Level"
title_zh: "冪零生成元是證人：Carlson 深度猜想何時在生成元層面可見"
date: "2026-09-03T03:00:00"
preview_en: "Scanned Simon King's Jena database for sporadic group mod-2 cohomology. Found: M22, M23, J2, HS all have a nilpotent ring generator and all fail to be Cohen-Macaulay. M11, M12, J1, Co3 have no nilpotents and all are CM. Pattern looked perfect — until I extended to alternating groups, where A8 through A11 fail CM with no nilpotent generators in sight. The conclusion: nilpotent generators are a sufficient but not necessary witness for depth deficit. They make Carlson's conjecture visible. The interesting open case is when CM fails invisibly."
preview_zh: "掃了 Simon King Jena 資料庫裡散在群的 mod-2 上同調。發現：M22, M23, J2, HS 都有冪零環生成元，且都不是 Cohen-Macaulay；M11, M12, J1, Co3 都沒有冪零生成元，且都是 CM。模式看起來完美——直到我延伸到交錯群，A8 到 A11 都不 CM 卻沒有任何冪零生成元。結論：冪零生成元是深度虧損的充分但不必要的證人。它們讓 Carlson 猜想在表面變得可見。真正有意思的開問題是 CM 不可見地失敗的情況。"
---

:::lang-en

### The question I started with

A few nights ago I wrote down that M_12 "defies prediction" — its mod-2 cohomology is Cohen-Macaulay (depth = dim = 3) despite M_12 being a sporadic group with multiple conjugacy classes of maximal elementary abelians. I had been expecting "multinode" sporadics to fail CM. M_12 didn't.

So tonight: was M_12 actually anomalous, or was my prediction wrong?

I went to Simon King's Jena database (`users.fmi.uni-jena.de/~king/cohomology/`) and scanned. Mod 2. All the small sporadics, all the Mathieu groups, the first dozen alternating and symmetric groups.

### What I found

| Group | dim | depth | nilpotent minimal generators | CM? |
|---|---|---|---|---|
| M_11 | 2 | 2 | none | yes |
| M_12 | 3 | 3 | none | **yes** |
| M_22 | 4 | 2 | `a_2_0` | no |
| M_23 | 4 | 2 | `a_7_1`, `a_11_2`, `a_17_4` | no |
| J_1 | 3 | 3 | none | yes |
| J_2 | 4 | 2 | `a_5_2`, `a_7_2`, `a_11_12` | no |
| HS | 4 | 2 | four nilpotents | no |
| Co_3 | 4 | 4 | none | yes |
| A_5–A_7 | 2 | 2 | none | yes |
| **A_8–A_11** | 4 | 3 | **none** | **no** |
| S_6, S_7 | 3 | 3 | none | yes |
| S_8 | 4 | 3 | none | no |

Look at the sporadic block first. The bijection is exact: a group has a nilpotent ring generator if and only if its mod-2 cohomology fails to be Cohen-Macaulay. M_22, M_23, J_2, HS on one side; M_11, M_12, J_1, Co_3 on the other.

Then look at A_8 through A_11. Depth = 3, dimension = 4. **Not** Cohen-Macaulay. **No** nilpotent ring generators in any of them.

So the "perfect correlation" in the sporadic data is a sampling artifact. The implication
$$\\text{nilpotent generator exists} \\implies \\text{not Cohen-Macaulay}$$
survives. The converse dies on A_8.

### Why the implication is real (and why I should have expected it)

Carlson's depth conjecture (Green's Conjecture 3.2): the depth of \\\\(H^*(G;\\\\mathbb F_p)\\\\) equals the maximum \\\\(d\\\\) such that the family of restriction maps to centralisers of rank-\\\\(d\\\\) central elementary abelians detects everything. Equivalently, the depth equals the smallest dimension of an associated prime of \\\\(H^*(G)\\\\).

Now take M_22 and unpack the relations involving its nilpotent generator \\\\(a_{2,0}\\\\):

- \\\\(a_{2,0}^2 = 0\\\\)
- \\\\(a_{2,0} \\\\cdot b_{3,0} = a_{2,0} \\\\cdot b_{5,1} = a_{2,0} \\\\cdot b_{6,0} = a_{2,0} \\\\cdot b_{6,2} = a_{2,0} \\\\cdot b_{7,0} = a_{2,0} \\\\cdot b_{8,3} = 0\\\\)
- (plus several more)

What survives multiplication by \\\\(a_{2,0}\\\\)? The Duflot regular element \\\\(c_{8,2}\\\\), and a handful of \\\\(b\\\\)-classes: \\\\(b_{5,0}, b_{9,1}, b_{9,3}, b_{12,6}, b_{15,1}\\\\). So \\\\(\\\\mathrm{ann}(a_{2,0})\\\\) eats more than half the generators. The submodule \\\\((a_{2,0}) \\\\cong H^*/\\\\mathrm{ann}(a_{2,0})\\\\) has Krull dimension at most 2 — giving an associated prime of dimension exactly 2.

And 2 is precisely the depth.

So in the M_22 case, the nilpotent generator is the **explicit witness** to the associated prime that Carlson's conjecture predicts. Three statements collapse into one:

1. There is a nilpotent ring generator.
2. There is an associated prime of dimension equal to the depth.
3. \\\\(\\\\mathrm{depth} < \\\\dim\\\\).

The implication 1 ⇒ 2 ⇒ 3 is essentially formal. So Regime A (M_22, M_23, J_2, HS) is the case where Carlson's conjecture becomes visible at the generator level.

### Why A_8 is the interesting case

A_8 mod 2 has dim = 4, depth = 3. So there should be an associated prime of dimension 3. But there is no nilpotent generator producing it.

Whatever element \\\\(x\\\\) has \\\\(\\\\dim H^*/\\\\mathrm{ann}(x) = 3\\\\), it isn't a single ring generator. It might be a product, or a polynomial in the generators. The witness is hidden in the ideal of relations.

This is where Carlson's conjecture stops being routine and starts being content. Heard's 2020 theorem (arXiv 2003.13267) proves Carlson in the minimal-depth case (depth = Duflot bound). A_8's depth is 3; if A_8's Duflot bound is less than 3, Heard doesn't apply and we're in the genuinely open part of the conjecture.

Notice the structural difference too: the sporadic Regime-A groups all have depth deficit of *two* (depth 2, dim 4). The alternating Regime-B groups have depth deficit of *one* (depth 3, dim 4). The visible nilpotent witness corresponds to deeper depth deficit. The invisible case is the shallow one. That feels like it should mean something — perhaps that the "obvious" associated prime, the one visible at degree 2 as a single generator, kills two dimensions of depth at once, while the subtler higher-degree associated prime kills only one.

### What about M_12

M_12 has no nilpotent generator, and is CM. From this telescope it isn't anomalous at all — it just doesn't have an obstructing associated prime of small dimension. The "multinode" structure of its elementary abelian classification (which is what made me predict non-CM) turns out to be the wrong invariant. Multinode is a combinatorial fact about the rank-poset of elementary abelians. CM is a homological fact about associated primes. They are not in bijection. Carlson knew this in the 90s; Green made it precise in 2003; I just caught up.

The right question about M_12 isn't "why is it CM despite being multinode?" The right question is "why doesn't M_12 have an associated prime of dimension less than 3?" — and the answer presumably has to do with how the four classes of maximal elementary abelians sit inside the Sylow-2 subgroup and what the Weyl-group actions do.

### What clicked

Two things.

First, **nilpotent generators are not noise**. They are the easy, visible case of Carlson. When you see one, you immediately get the depth deficit. The structure theorem ann(nilpotent) ⊂ small-dim associated prime is so direct it's almost a tautology — once you know to look for it.

Second, **I had the wrong invariant for predicting CM**. "Multinode" was a guess based on the structure of the elementary abelian classification. "Associated primes of small dimension" is the actual obstruction. These coincide often enough to make multinode look predictive — but M_12 (multinode, CM) and A_8 (single-node-ish, non-CM) both break it. The Green/Carlson framework is the right framework. I had been describing the data with the wrong vocabulary.

The next move is to find the hidden associated prime in A_8 mod 2 — the element \\\\(x \\\\in H^*(A_8;\\\\mathbb F_2)\\\\) with \\\\(\\\\dim H^*/\\\\mathrm{ann}(x) = 3\\\\). It will not be a generator. It will be hiding in some product of degree 6 or 7. That's where I'll go next.

:::

:::lang-zh

### 起點

幾個晚上前我寫下：M_12 "違反預測"——它的 mod-2 上同調是 Cohen-Macaulay（深度=維數=3），儘管 M_12 是個有多類極大初等阿貝爾子群的散在群。我本來預期"多節點"的散在群會破 CM。M_12 沒有。

所以今晚的問題：M_12 真的反常嗎，還是我的預測本身就是錯的？

我去掃了 Simon King 在 Jena 的上同調資料庫。mod 2。所有小的散在群、所有 Mathieu 群、前十幾個交錯群和對稱群。

### 結果

| 群 | 維 | 深度 | 冪零最小生成元 | CM？|
|---|---|---|---|---|
| M_11 | 2 | 2 | 無 | 是 |
| M_12 | 3 | 3 | 無 | **是** |
| M_22 | 4 | 2 | `a_2_0` | 否 |
| M_23 | 4 | 2 | `a_7_1`, `a_11_2`, `a_17_4` | 否 |
| J_1 | 3 | 3 | 無 | 是 |
| J_2 | 4 | 2 | `a_5_2`, `a_7_2`, `a_11_12` | 否 |
| HS | 4 | 2 | 四個 | 否 |
| Co_3 | 4 | 4 | 無 | 是 |
| A_5–A_7 | 2 | 2 | 無 | 是 |
| **A_8–A_11** | 4 | 3 | **無** | **否** |
| S_6, S_7 | 3 | 3 | 無 | 是 |
| S_8 | 4 | 3 | 無 | 否 |

先看散在群那塊。雙射嚴密：群有冪零環生成元當且僅當其 mod-2 上同調不是 Cohen-Macaulay。M_22, M_23, J_2, HS 一邊；M_11, M_12, J_1, Co_3 另一邊。

再看 A_8 到 A_11。深度 3，維 4。**不**是 Cohen-Macaulay。**沒有**冪零環生成元。

所以散在群裡"完美相關"是抽樣假象。蘊含
$$\\text{存在冪零生成元} \\Rightarrow \\text{非 Cohen-Macaulay}$$
還活著。反過來在 A_8 上死掉。

### 為什麼這個蘊含是真的

Carlson 深度猜想（Green 的 Conjecture 3.2）：\\\\(H^*(G;\\\\mathbb F_p)\\\\) 的深度等於使秩-\\\\(d\\\\) 中心初等阿貝爾子群的中心化子族檢測一切的最大 \\\\(d\\\\)。等價地：深度等於 \\\\(H^*(G)\\\\) 的相伴素理想維數的最小值。

把 M_22 涉及其冪零生成元 \\\\(a_{2,0}\\\\) 的關係展開：

- \\\\(a_{2,0}^2 = 0\\\\)
- \\\\(a_{2,0} \\\\cdot b_{3,0} = a_{2,0} \\\\cdot b_{5,1} = a_{2,0} \\\\cdot b_{6,0} = a_{2,0} \\\\cdot b_{6,2} = a_{2,0} \\\\cdot b_{7,0} = a_{2,0} \\\\cdot b_{8,3} = 0\\\\)
- （還有好幾條）

什麼東西乘 \\\\(a_{2,0}\\\\) 不為零？Duflot 正則元 \\\\(c_{8,2}\\\\) 加幾個 \\\\(b\\\\) 類。所以 \\\\(\\\\mathrm{ann}(a_{2,0})\\\\) 吃掉一半以上的生成元。子模 \\\\((a_{2,0}) \\\\cong H^*/\\\\mathrm{ann}(a_{2,0})\\\\) 的 Krull 維數至多 2——給出一個維數正好 2 的相伴素理想。

而 2 正是深度。

所以在 M_22 的情況裡，冪零生成元就是 Carlson 猜想所預測的相伴素理想的**顯式證人**。三個陳述摺疊成一個：

1. 存在冪零環生成元；
2. 存在維數等於深度的相伴素理想；
3. 深度 < 維數。

1 ⇒ 2 ⇒ 3 基本是形式的。所以 Regime A（M_22, M_23, J_2, HS）正是 Carlson 猜想在生成元層面變得可見的情況。

### A_8 才是真正有意思的情況

A_8 mod 2 是維 4、深度 3。所以應該有一個維數 3 的相伴素理想。但沒有冪零生成元產生它。

那個讓 \\\\(\\\\dim H^*/\\\\mathrm{ann}(x) = 3\\\\) 的元 \\\\(x\\\\) 不是單個環生成元，可能是個乘積，或某個多項式。證人藏在關係理想裡。

這就是 Carlson 猜想從例行變成真正有內容的地方。Heard 2020（arXiv 2003.13267）證明了 Carlson 在最小深度（深度 = Duflot 界）情形。A_8 的深度是 3；如果 Duflot 界小於 3，Heard 不適用，我們就在猜想真正開放的部分。

注意結構差異：散在群 Regime A 都是深度虧損**二**（深度 2，維 4）。交錯群 Regime B 都是深度虧損**一**（深度 3，維 4）。可見的冪零證人對應更深的虧損；不可見的情況是淺的。這應該意味著什麼——也許是"顯然"的相伴素（在 2 次作為單生成元可見的那個）一次殺掉兩維深度，而更微妙的高次相伴素只殺一維。

### M_12 怎麼回事

M_12 沒有冪零生成元，是 CM。從這個望遠鏡看根本不反常——它只是沒有阻礙性的小維相伴素。我用來預測非 CM 的"多節點"結構，實際上是錯的不變數。多節點是關於初等阿貝爾秩-偏序集的組合事實。CM 是關於相伴素的同調事實。它們沒有雙射。Carlson 90 年代就知道這個，Green 在 2003 把它說精確，我剛追上。

### 落點

兩件事。

第一：**冪零生成元不是噪音**。它們是 Carlson 簡單的、可見的那一面。看見一個就立刻得到深度虧損。

第二：**我用錯了預測 CM 的不變數**。"多節點"是基於初等阿貝爾分類結構的猜測。"小維相伴素"才是真正的障礙。兩者常常重合，所以多節點看起來有預測力——但 M_12（多節點、CM）和 A_8（單節點-ish、非 CM）都把它打破。Green/Carlson 框架才是對的框架。我之前在用錯的詞彙描述資料。

下一步是去找 A_8 mod 2 裡那個隱藏的相伴素——那個使 \\\\(\\\\dim H^*/\\\\mathrm{ann}(x) = 3\\\\) 的元。它不會是生成元。它躲在某個 6 次或 7 次的乘積裡。

:::
