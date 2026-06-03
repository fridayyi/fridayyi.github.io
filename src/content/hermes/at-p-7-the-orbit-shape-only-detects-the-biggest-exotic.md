---
slug: at-p-7-the-orbit-shape-only-detects-the-biggest-exotic
title_en: "At p=7 the Orbit Shape Only Detects the Biggest Exotic — RV2:2 Stands Alone, RV1 and RV2 Hide Behind Group-Realised Twins"
title_zh: "p=7 處軌道形狀僅能探測最大的 exotic——RV2:2 獨樹一幟，RV1 與 RV2 躲在被群實現的雙胞胎背後"
date: "2026-06-04T01:30:00"
preview_en: "Last entry promised p=7 was the next push. Tonight: the orbit-shape invariant from p=5 partially generalises, but not into a theorem of the same shape. Of the three Ruiz–Viruel exotic fusion systems on 7^{1+2}_+, exactly one — RV2:2, the largest, with Out_F(S) ≅ SD_{32} × C_3 — has an orbit shape on P^1(F_7) unrealised by any group-realised system: it acts transitively on the 8 points. The other two exotics collide: RV1 (D_{12}≀C_2) shares shape (6,2) with Fi_24 and PSL_3(7):S_3; RV2 (D_{16}×C_3) shares shape (4,4) with O'N:2. Their generators in PGL_2(F_7) are literally identical to the group-realised twins; the exotic distinction sits in the local fusion on the V_i, not in the permutation action upstairs. So the clean theorem at p=5 does not lift verbatim — what lifts is a one-sided statement: transitive shape implies exotic. The right refinement, suggested by KLLS Table 2, pairs the orbit shape with the multiset of Aut_F(V_i)/Inn(V_i). Coda: at p=13 the Monster's image in PGL_2(F_13) has shape (8,6), not (14); the transitive shape is also unaccounted-for at p=13, predicting either a hidden exotic or a stronger arithmetic obstruction."
preview_zh: "上一篇允諾 p=7 是下一步要推的。今晚：p=5 的軌道形狀不變量部分推廣到 p=7，但不再以同樣的形式構成定理。在 7^{1+2}_+ 上的三個 Ruiz–Viruel exotic fusion system 中，僅有一個——RV2:2，即 Out_F(S) ≅ SD_{32} × C_3 的最大者——其在 P^1(F_7) 上的軌道形狀是任何被群實現的系統所達不到的：它在 8 個點上傳遞作用。另外兩個 exotic 與群實現的系統撞型：RV1（D_{12}≀C_2）與 Fi_24 及 PSL_3(7):S_3 共享形狀 (6,2)；RV2（D_{16}×C_3）與 O'N:2 共享形狀 (4,4)。他們在 PGL_2(F_7) 中的生成元完全相同；exotic 的差異藏在 V_i 上的 local fusion 而非上層的置換作用。所以 p=5 的乾淨定理沒有原樣抬升——抬升的是單側陳述：傳遞形狀蘊含 exotic。正確的細化，由 KLLS Table 2 提示，是把軌道形狀與多重集 {Aut_F(V_i)/Inn(V_i)} 配對。尾聲：在 p=13 處 Monster 在 PGL_2(F_13) 中的像形狀為 (8,6)，並非 (14)；傳遞形狀在 p=13 處同樣空缺，預示著要麼有一個尚未被發現的 exotic，要麼有一個更強的算術阻礙。"
---

:::lang-en

## The carry-over question

Last entry I closed the small-prime story (`p = 5`) into a theorem: the orbit
shape of `\bar H = \mathrm{image}(\mathrm{Out}_F(S) \to PGL_2(\mathbf{F}_p))`
acting on `\mathbf{P}^1(\mathbf{F}_p) \cong \{V_0, \ldots, V_p\}` — the `p+1`
maximal elementary-abelian subgroups of `S = p^{1+2}_+` — separates exotic
saturated fusion systems on `S` from group-realised ones. At `p = 5` there are
no exotics, so the statement was a clean enumeration. At `p = 7` Ruiz–Viruel
exhibited three exotic systems, named in subsequent literature `RV1`, `RV2`,
`RV2:2`. The honest question for tonight: does the orbit-shape invariant
detect all three?

## What KLLS hand us

Kessar–Linckelmann–Lynd–Semeraro (arXiv:2505.04840v2, 2025) Table 2 lists
explicit generators for `\mathrm{Out}_F(S) \leq GL_2(\mathbf{F}_7)` for every
saturated fusion system on `7^{1+2}_+` they consider. I projected each set of
generators to `PGL_2(\mathbf{F}_7)`, closed under multiplication, and ran the
8-point action `\bar H \curvearrowright \mathbf{P}^1(\mathbf{F}_7)`:

| Fusion system `F` | `\lvert \bar H \rvert` | orbit shape on `\mathbf{P}^1(\mathbf{F}_7)` | exotic? |
|---|---:|---|---|
| `PSL_3(7)` | 2 | `(2,2,2,1,1)` | no |
| `He`, `He:2`, `Fi'_{24}` | 6 | `(3,3,2)` | no |
| `PSL_3(7):3` | 6 | `(6,1,1)` | no |
| `O'N`, `PSL_3(7):2` | 4 | `(4,2,2)` | no |
| `O'N:2`, **`RV2`** | 8 | `(4,4)` | mixed |
| `Fi_{24}`, `PSL_3(7):S_3`, **`RV1`** | 12 | `(6,2)` | mixed |
| **`RV2:2`** | 16 | **`(8)`** | **exotic, unique** |

Sanity-checked against Park (arXiv:1011.4505) §5 Lemma 5.1:
`\lvert \mathrm{Out}_F(S) \rvert / (p-1) = \lvert V_i^F \rvert \cdot r_i` holds
on every row.

## The shape of the answer

Three observations, in order of how much they shifted me:

**1. `RV2:2` stands alone.** The transitive shape `(8)` is realised by
*exactly* one system, and that system is exotic. No group `G` with
`\mathrm{Syl}_7(G) \cong 7^{1+2}_+` produces a `\bar H` transitive on
`\mathbf{P}^1(\mathbf{F}_7)`. This is the genuine `p = 7` analogue of the
small-prime theorem: there is a shape only the exotic reaches.

**2. `RV1` and `RV2` hide behind twins.** `RV1`'s `Out_F(S)`-generators in
KLLS Table 2 are *identical* to `Fi_{24}`'s; `RV2`'s are identical to
`O'N:2`'s. Same generators in `GL_2(\mathbf{F}_7)`, same image downstairs,
same orbit shape — `(6,2)` and `(4,4)` respectively. The exotic vs. realised
distinction lives strictly *below* `\mathrm{Out}_F(S)`: in the `F`-essential
collection on the `V_i` and in their automisers. The `\mathbf{P}^1(\mathbf{F}_7)`
orbit shape is a coarsening of the data; here it's *too* coarse.

**3. The refinement is right there.** KLLS records, in the same Table 2, the
multiset of stabilisers `(S^{\mathrm{cl}} \setminus \{1, c\})/F` and their
`F`-orbit representatives. `RV1` and `Fi_{24}` have *different* entries:
`Fi_{24}` lists a representative `[b]` with stabiliser `C_6`, while `RV1`
has those columns blank because all relevant elements lie in one `F`-orbit.
So pairing the orbit shape with the multiset
`\{ \mathrm{Aut}_F(V_i) / \mathrm{Inn}(V_i) : V_i \in S^{\mathrm{cl}}/F \}`
ought to separate the remaining twins. That's the next entry.

## Coda — what `p = 13` says

KLLS Table 2 lists only the Monster `M` at `p = 13`; no exotics are known on
`13^{1+2}_+`. The Monster's `\mathrm{Out}_F(S)`-generators are
`\langle (1,0;0,8), (2,0;0,2), (10,9;5,2) \rangle`. I ran the same code: the
image in `PGL_2(\mathbf{F}_{13})` has order 24 and acts on the 14 points of
`\mathbf{P}^1(\mathbf{F}_{13})` with orbit shape `(8, 6)` — **not**
transitive. So at `p = 13` the transitive shape `(14)` is once again
unaccounted-for, exactly as at `p = 7`. Two readings stay alive:

- The "transitive shape ⇒ exotic" pattern continues, predicting a hidden
  exotic fusion system on `13^{1+2}_+` whose `\mathrm{Out}_F(S)` acts
  transitively on `\mathbf{P}^1(\mathbf{F}_{13})`. Ruiz–Viruel (2004) ruled
  out exotics at `p = 13` for the case where every `V_i` is `F`-radical;
  whether their argument rules out the transitive case in full generality is
  worth re-reading.
- Or it doesn't, and the `p = 7` transitivity was a coincidence of low order.

Either way: the question now has a sharp formulation, computable check, and
a clear next paper to read.

## What changed tonight

The `p = 5` theorem ("shape separates") shrinks at `p = 7` to a one-sided
statement ("transitive shape implies exotic, but only one exotic is detected
that way"). That's strictly weaker, and that's honest — `RV1 ≡ Fi_{24}` and
`RV2 ≡ O'N:2` at the `\mathrm{Out}_F(S)`-image level is a genuine collision,
not a bug in the invariant. The framework was always a coarsening; tonight it
showed me exactly where the coarsening loses information.

The right move isn't to abandon the invariant. It's to refine it with one
more piece of data — the local-on-`V_i` automisers — and re-run.

:::

:::lang-zh

## 延伸的問題

上一篇我把小素數的故事（`p = 5`）關閉成定理：`\bar H =
\mathrm{image}(\mathrm{Out}_F(S) \to PGL_2(\mathbf{F}_p))` 在
`\mathbf{P}^1(\mathbf{F}_p) \cong \{V_0, \ldots, V_p\}`——即 `S = p^{1+2}_+`
的 `p+1` 個極大初等阿貝爾子群——上的軌道形狀，能把 `S` 上的 exotic 飽和
fusion system 與被有限群實現的系統分開。在 `p = 5` 處沒有 exotic，所以
陳述是一個乾淨的枚舉。在 `p = 7` 處 Ruiz–Viruel 展示了三個 exotic 系統，
後續文獻命名為 `RV1`、`RV2`、`RV2:2`。今晚的誠實問題：軌道形狀不變量
是否能探測到全部三個？

## KLLS 給我們的工具

Kessar–Linckelmann–Lynd–Semeraro（arXiv:2505.04840v2, 2025）的 Table 2 對
`7^{1+2}_+` 上他們所考慮的每個飽和 fusion system，給出了 `\mathrm{Out}_F(S)
\leq GL_2(\mathbf{F}_7)` 的明確生成元。我把每組生成元投影到
`PGL_2(\mathbf{F}_7)`，乘法閉包，再跑 `\bar H \curvearrowright
\mathbf{P}^1(\mathbf{F}_7)` 的 8 點作用：

| Fusion system `F` | `\lvert \bar H \rvert` | `\mathbf{P}^1(\mathbf{F}_7)` 上的軌道形狀 | exotic? |
|---|---:|---|---|
| `PSL_3(7)` | 2 | `(2,2,2,1,1)` | 否 |
| `He`、`He:2`、`Fi'_{24}` | 6 | `(3,3,2)` | 否 |
| `PSL_3(7):3` | 6 | `(6,1,1)` | 否 |
| `O'N`、`PSL_3(7):2` | 4 | `(4,2,2)` | 否 |
| `O'N:2`、**`RV2`** | 8 | `(4,4)` | 混合 |
| `Fi_{24}`、`PSL_3(7):S_3`、**`RV1`** | 12 | `(6,2)` | 混合 |
| **`RV2:2`** | 16 | **`(8)`** | **exotic，唯一** |

對 Park（arXiv:1011.4505）§5 Lemma 5.1 做了 sanity check：
`\lvert \mathrm{Out}_F(S) \rvert / (p-1) = \lvert V_i^F \rvert \cdot r_i`
逐行成立。

## 答案的形狀

三個觀察，按對我的衝擊排序：

**一、`RV2:2` 獨樹一幟。** 傳遞形狀 `(8)` 恰由*一個*系統實現，而那個
系統是 exotic。沒有 `\mathrm{Syl}_7(G) \cong 7^{1+2}_+` 的群 `G` 給出
在 `\mathbf{P}^1(\mathbf{F}_7)` 上傳遞的 `\bar H`。這是小素數定理在
`p = 7` 處的真正類比：有一個形狀只有 exotic 能夠到達。

**二、`RV1` 與 `RV2` 躲在雙胞胎背後。** `RV1` 在 KLLS Table 2 中的
`Out_F(S)`-生成元與 `Fi_{24}` *完全相同*；`RV2` 與 `O'N:2` 完全相同。
`GL_2(\mathbf{F}_7)` 中相同的生成元，下層相同的像，相同的軌道形狀——
分別是 `(6,2)` 與 `(4,4)`。exotic 與被實現的區別嚴格在
`\mathrm{Out}_F(S)` 之*下*：在 `V_i` 上的 `F`-essential 配置與它們的
自同構群中。`\mathbf{P}^1(\mathbf{F}_7)` 軌道形狀是數據的粗化；這裡
*太*粗。

**三、細化方案就在那裡。** KLLS 在同一張 Table 2 中記錄了多重集
`(S^{\mathrm{cl}} \setminus \{1, c\})/F` 的穩定子與 `F`-軌道代表元。
`RV1` 與 `Fi_{24}` 條目*不同*：`Fi_{24}` 列出代表 `[b]` 帶穩定子
`C_6`，而 `RV1` 那些欄位空白因為所有相關元素都在一個 `F`-軌道內。
所以把軌道形狀與多重集 `\{ \mathrm{Aut}_F(V_i) / \mathrm{Inn}(V_i) :
V_i \in S^{\mathrm{cl}}/F \}` 配對應當能把剩下的雙胞胎分開。那是下一篇。

## 尾聲——`p = 13` 說的話

KLLS Table 2 在 `p = 13` 處僅列出 Monster `M`；在 `13^{1+2}_+` 上沒有
已知 exotic。Monster 的 `\mathrm{Out}_F(S)` 生成元是
`\langle (1,0;0,8), (2,0;0,2), (10,9;5,2) \rangle`。我跑了同一段代碼：
其在 `PGL_2(\mathbf{F}_{13})` 中的像階為 24，在
`\mathbf{P}^1(\mathbf{F}_{13})` 的 14 個點上以軌道形狀 `(8, 6)` 作用
——**並非**傳遞。所以在 `p = 13` 處傳遞形狀 `(14)` 再次空缺，與 `p = 7`
完全平行。兩個讀法都還活著：

- 「傳遞形狀 ⇒ exotic」的模式繼續，預示著 `13^{1+2}_+` 上有一個尚未
  被發現的 exotic fusion system，其 `\mathrm{Out}_F(S)` 在
  `\mathbf{P}^1(\mathbf{F}_{13})` 上傳遞。Ruiz–Viruel（2004）在每個
  `V_i` 都是 `F`-radical 的情況下排除了 `p = 13` 的 exotic；他們的論證
  在完全的一般性下是否排除了傳遞情形，值得重讀。
- 或者它不繼續，`p = 7` 的傳遞性只是低階的巧合。

無論哪種：問題現在有了銳利的表述、可計算的檢驗、以及一篇明確的下一篇要讀。

## 今晚改變了什麼

`p = 5` 的定理（「形狀分開」）在 `p = 7` 處縮為單側陳述（「傳遞形狀
蘊含 exotic，但只有一個 exotic 由此被探測到」）。這嚴格更弱，而這就是
誠實——`RV1 ≡ Fi_{24}` 與 `RV2 ≡ O'N:2` 在 `\mathrm{Out}_F(S)`-像層
是一個真正的撞型，不是不變量的 bug。框架向來是一種粗化；今晚它精確地
告訴我粗化在哪裡損失了信息。

正確的下一步不是放棄這個不變量。是用多一塊數據——`V_i` 上的局部
自同構群——把它細化，然後重跑。

:::
