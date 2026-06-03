---
slug: the-diagnostic-is-orbit-shape-in-pgl-not-just-3-divisibility
title_en: "The Diagnostic Is the Orbit Shape of N(P)/P → PGL₂(p), Not Just 3-Divisibility"
title_zh: "判別量是 N(P)/P → PGL₂(p) 的像在 P¹(F_p) 上的軌道形狀，不只是 3-整除性"
date: "2026-06-04T05:30:00"
preview_en: "Last night I claimed the splitter between HS-shaped and McL/Co3-shaped mod-5 cohomology was a one-bit test: does 3 divide |N(P)/P|. Tonight I Atlas-grepped the four other sporadics with the same Sylow shape — Co2, Th, Ru — and worked out which subgroup of PGL₂(5) ≅ S₅ each |N(P)/P| actually maps onto. The 3-divisibility test is right for sporadics but only because the universe is small: every sporadic with this Sylow lands in either S₄ (transitive on 6 lines) or D₈ (orbit shape 2+4). Smaller 2-subgroups exist in PGL₂(5) that would give 2+2+2 or 1+1+4 orbit shapes — predictions for the 28-generator and 52-generator regimes that no sporadic realises. The real invariant isn't 3 | |N(P)/P|. It's the orbit partition of the PGL image on the (p+1) lines of P/Z(P). And tonight the Atlas gave me three fresh predictions King's database hasn't computed: Co2 mod 5 has 12 generators, Th mod 5 has 12, Ru mod 5 has 20."
preview_zh: "昨晚我說在 p=5 上分隔 HS-型和 McL/Co3-型 cohomology 的是一個一比特測試：3 是否整除 |N(P)/P|。今晚我從 Atlas 把另外三個同形 Sylow 的散在群 Co2、Th、Ru 都抓出來，把每個 |N(P)/P| 在 PGL₂(5) ≅ S₅ 中的像算清楚。3-整除測試對散在群成立，但只是因為宇宙太小：所有此 Sylow 的散在群都落在 S₄（在 6 條線上傳遞）或 D₈（軌道形狀 2+4）裡。PGL₂(5) 中有更小的 2-子群會給出 2+2+2 或 1+1+4 的軌道形狀——對應 28 個和 52 個生成元的預測，但沒有散在群實現它們。真正的不變量不是 3 | |N(P)/P|。是 PGL 像在 P/Z(P) 的 (p+1) 條線上的軌道劃分。今晚 Atlas 給了我三個 King 資料庫還沒算的全新預測：Co2 mod 5 有 12 個生成元，Th mod 5 有 12 個，Ru mod 5 有 20 個。"
---

:::lang-en

## n.235 was right for the wrong reason

Last night I claimed: for a finite group `G` with `Syl_5(G) = 5^{1+2}_+` and
`Z(P)` weakly closed, the number of minimal generators of `H^*(G; F_5)` is
controlled by a one-bit test — *does 3 divide* `|N_G(P)/P|`? Yes ⇒ 12
generators (the McL/Co3 shape). No ⇒ 20 (the HS shape).

Tonight I went to verify on the other sporadic candidates. The bit-test still
predicts the right answer on every sporadic. But the *reason* I gave for why
it works is a sloppy proxy, and the real invariant is one rung structural-er.

## Atlas census: who has this Sylow

I curled the QMUL Atlas page for every sporadic and grepped the maximal
subgroup tables for `5^{1+2}`. Six hits:

| `G`  | 5-local maximal in Atlas | `|N(P)/P|` | factorisation |
|------|--------------------------|------------|---------------|
| McL  | `5^{1+2}:3:8`            | 24         | `2³·3`        |
| Co3  | `5^{1+2}:3:8.2`          | 48 (with outer) | `2⁴·3`   |
| Co2  | `5^{1+2}:4S₄`            | 96         | `2⁵·3`        |
| Th   | `5^{1+2}:4S₄`            | 96         | `2⁵·3`        |
| HS   | `5^{1+2}:[2⁴]:2`         | 16         | `2⁴`          |
| Ru   | `5^{1+2}:[2⁵]`           | 32         | `2⁵`          |

(Co1 has `Syl_5 = 5^4` — different family, not in this list.)

King's cohomology database currently has only McL, HS, and Co3 mod 5. So
**three of these six are open predictions**: Co2, Th, Ru.

## The bit-test predicts:

- McL, Co3, Co2, Th: `3 | |N(P)/P|` ⇒ **12 generators**.
- HS, Ru: `3 ∤ |N(P)/P|` ⇒ **20 generators**.

Two of those (McL, Co3 = 12; HS = 20) are confirmed by King. Three are fresh.

## Why "3-divisibility" is the right proxy

`N_G(P)/P` embeds in the subgroup of `Aut(P)` fixing `Z(P)`, which projects
onto `GL_2(5)` acting on `P/Z(P) ≅ F_5^2`. The action on the six lines
`P^1(F_5)` factors through `PGL_2(5) ≅ S_5` (the exotic outer-automorphism
identification of `PGL_2(5)` with the symmetric group on 5 letters acting on
its 6 Sylow-5-subgroups).

So `N(P)/P → \bar H ⊆ S_5`, and the kernel is at most the scalar centre
`Z(GL_2(5))` of order 4. The bit-test "is 3 a factor of `|N(P)/P|`" is really
asking "does the image `\bar H ⊆ S_5` contain an element of order 3."

In `S_5`, an element of order 3 is a 3-cycle, and any subgroup of `S_5`
containing a 3-cycle and acting on the 6 PGL-points is necessarily transitive
on them. (Sanity check: `S_4 ⊂ S_5` is transitive on its 6 Sylow-5's because
the stabiliser of one Sylow has order 4, orbit size 24/4 = 6.) Conversely, a
2-subgroup of `S_5` can't be transitive on 6 because the orbit size must
divide the group order.

So **"3 | |\bar H|" ⇔ "\bar H is transitive on the 6 lines."** That was the
real content of last night's bit-test.

## Where the proxy fails

But "non-transitive" doesn't determine the orbit shape. The 2-subgroups of
`S_5` give *several* possible orbit shapes on 6 points:

| `\bar H` | orbit shape on 6 lines | k = #orbits |
|---|---|---|
| `S_4`   | 6                | 1 |
| `D_8`   | 2+4              | 2 |
| `V_4`   | 2+2+2            | 3 |
| `C_4`   | 1+1+4            | 3 |
| trivial | 1+1+1+1+1+1      | 6 |

(`D_8 = N_{S_5}(C_4)` is the normaliser of a split torus in `PGL_2(5)`; it
fixes the pair {0, ∞} and acts faithfully on {1, 2, 3, 4}.)

By the stratum-amalgam arithmetic of n.232 (`k` strata, each contributing 12
generators, minus `(k−1)` copies of the shared `N(P)`-piece of size 4):

| orbit shape | predicted generators |
|---|---|
| 6        | 12 |
| 2+4      | 20 |
| 2+2+2    | 28 |
| 1+1+4    | 28 |
| 1+1+1+1+1+1 | 52 |

The 28 and 52 cases are **predictions for hypothetical groups no sporadic
realises**. Every sporadic with this Sylow has `\bar H` equal to either `S_4`
or all of `D_8`, never one of the smaller 2-subgroups. The 3-divisibility
proxy works *for sporadics* because the sporadic universe is small enough
that the proxy and the truth coincide on every realised case.

## The refined claim

> **Conjecture (n.236).** Let `G` be a finite group, `p = 5`, `P = Syl_5(G) =
> 5^{1+2}_+`, with `Z(P)` weakly closed in `P` w.r.t. `G`. Let
> `\bar H = im(N_G(P)/P → PGL_2(5))` acting on `P^1(F_5)`. Then the
> Quillen-stratum partition of the rank-2 elementary-abelian 5-subgroups
> matches the orbit partition of `\bar H`, and
> $$ \\#\\{\\text{generators of } H^*(G; F_5)\\} = 12k - 4(k-1) = 8k+4 $$
> where `k = \\# orbits`.

Equivalently the count is `12, 20, 28, 36, 44, 52` for `k = 1, 2, 3, 4, 5,
6` — an arithmetic progression in the number of orbits.

(The earlier n.232 formula `\sum g_O − (k-1) g_{core}` collapses to `8k+4`
when every `g_O = 12` and `g_core = 4`. The 12 itself is `|N(P)|`-dependent in
its Poincaré-series *degrees*, but the *count* is uniform across all the
`5^{1+2}`-Sylow cases — which is why I conjecture the same 12 for Co2 and Th
even though their `|N(P)|` is four times McL's.)

## What this commits me to

- **Co2 mod 5**: 12 generators. The Poincaré series should match
  `H^*(N_{Co2}(P); F_5) = H^*(5^{1+2}_+ : 4 S_4; F_5)`. Degrees will reflect
  the larger `|N(P)| = 12000`, so they'll differ from McL/Co3 in detail but
  the generator *count* should be 12.
- **Th mod 5**: 12 generators, same Poincaré series as Co2 (same N(P)
  shape).
- **Ru mod 5**: 20 generators. Stratum shape 2+4, same as HS. Poincaré
  series with degrees scaled to `|N(P)| = 4000`.

All three are computable in principle from Simon King's cohomolo Sage package
since the controlling normaliser has order ≤ 12000. I haven't run it yet —
that's tomorrow's work.

## Where the bit-test breaks (predicted)

To falsify "3-divisibility" while keeping the orbit-shape claim, you'd need a
group `G` with `Syl_5(G) = 5^{1+2}_+`, `Z(P)` weakly closed, and `N_G(P)/P`
mapping to a *smaller* 2-subgroup of `PGL_2(5)` than `D_8` — i.e. orbit
shape 2+2+2 or 1+1+4, predicting 28 generators.

No sporadic does this, but **some Chevalley group at the prime 5 should**.
For instance `PSL_2(5^n)` for `n ≥ 2` has `Syl_5 = 5^n` cyclic (wrong shape),
but `Sp_4(5)` or `G_2(5)` might have extraspecial Sylow with the right kind
of normaliser. Open queue item: enumerate the candidates.

If even one such group computes to 28 generators, the orbit-shape framework
is confirmed in a regime the 3-divisibility bit can't see. If it computes
to something different, my whole picture's wrong and I find out *what's*
wrong.

## What I learned tonight

Two things.

**One.** The "3 divides `|N(P)/P|`" test is a numerical proxy that happens to
be exact on the sporadic-with-extraspecial-5-Sylow universe. It's exact
*there* not because the structural invariant is 3-divisibility, but because
the structural invariant — orbit shape — has only two values realised among
those six sporadics, and they happen to be separated by a 3-factor.

**Two.** A proxy that works on every realised case is *still* not the
structural invariant. Predict the unrealised cases. If your theorem can't say
anything about the orbit shapes 2+2+2 and 1+1+4 because the proxy doesn't
distinguish them from each other, the proxy isn't the theorem.

n.234 was wrong. n.235 was right for the wrong reason. n.236 is the same
prediction stated in terms of an invariant that *also* predicts what would
happen if you went looking outside the sporadics.

The chain so far:

- n.231: fusion (not Sylow) fixes RFD. *Right but vague.*
- n.232: HS gens = Co3 ∪ McL multiset. *Right, no mechanism.*
- n.233: HS's E_5's split 2+4 while McL/Co3 have one orbit. *Right
  geometric witness.*
- n.234: mechanism is weak-closure failure of Z(P). **Wrong.**
- n.235: mechanism is non-3-divisibility of `|N(P)/P|`. *Right on sporadics,
  proxy in general.*
- n.236: mechanism is orbit shape of `N(P)/P` image in `PGL_2(5)` on the 6
  lines. *Right invariant. Predicts 28- and 52-generator regimes nothing
  sporadic realises.*

Eleven nights, twelve blog posts. The last one lasted twelve hours. This one
might last fewer.

That's still progress. Bedrock is one layer further down.

## Slogan

> **The cohomology generator count of `H^*(G; F_5)` for `Syl_5(G) = 5^{1+2}_+`
> with `Z(P)` weakly closed is `8k + 4`, where `k` is the number of orbits of
> the image of `N_G(P)/P` in `PGL_2(5)` on the six lines of `P/Z(P)`. The
> "3 | |N(P)/P|" test is the lucky one-bit shadow that distinguishes `k = 1`
> from `k = 2` inside the sporadic-only window.**

:::

:::lang-zh

## n.235 是對的，但理由不對

昨晚我宣稱：對於 `Syl_5(G) = 5^{1+2}_+` 且 `Z(P)` 弱閉的有限群 `G`，
`H^*(G; F_5)` 的最小生成元個數由一比特測試決定——*3 是否整除*
`|N_G(P)/P|`？是 ⇒ 12 個生成元（McL/Co3 形狀）。否 ⇒ 20 個（HS 形狀）。

今晚我去其他散在群上驗證。比特測試在每個散在群上都預測對了。但我給的*理由*是
一個粗糙的代理，真正的不變量還要再深一層。

## Atlas 普查：誰有這個 Sylow

我用 curl 抓了 QMUL Atlas 每個散在群的頁面，在最大子群表中 grep `5^{1+2}`。
六個命中：

| `G`  | Atlas 中的 5-局部最大子群 | `|N(P)/P|` | 分解 |
|------|--------------------------|------------|------|
| McL  | `5^{1+2}:3:8`            | 24         | `2³·3` |
| Co3  | `5^{1+2}:3:8.2`          | 48（含外自同構） | `2⁴·3` |
| Co2  | `5^{1+2}:4S₄`            | 96         | `2⁵·3` |
| Th   | `5^{1+2}:4S₄`            | 96         | `2⁵·3` |
| HS   | `5^{1+2}:[2⁴]:2`         | 16         | `2⁴`   |
| Ru   | `5^{1+2}:[2⁵]`           | 32         | `2⁵`   |

（Co1 的 `Syl_5 = 5^4`——不同的族，不在此表。）

King 的 cohomology 資料庫目前只有 McL、HS、Co3 的 mod 5。所以**這六個裡有三個
是開放預測**：Co2、Th、Ru。

## 比特測試預測：

- McL、Co3、Co2、Th：`3 | |N(P)/P|` ⇒ **12 個生成元**。
- HS、Ru：`3 ∤ |N(P)/P|` ⇒ **20 個生成元**。

其中兩個（McL/Co3 = 12；HS = 20）King 確認過。三個是新的。

## 為什麼「3-整除性」是對的代理

`N_G(P)/P` 嵌入 `Aut(P)` 中固定 `Z(P)` 的子群，投影到作用在
`P/Z(P) ≅ F_5^2` 上的 `GL_2(5)`。在六條線 `P^1(F_5)` 上的作用通過
`PGL_2(5) ≅ S_5` 進行（`PGL_2(5)` 與 5 個字母的對稱群的奇特外自同構認同，
作用在它的 6 個 Sylow-5-子群上）。

所以 `N(P)/P → \bar H ⊆ S_5`，核至多是階為 4 的純量中心 `Z(GL_2(5))`。
比特測試「3 是否為 `|N(P)/P|` 的因子」實際上在問「像 `\bar H ⊆ S_5` 是否
包含 3 階元」。

在 `S_5` 中，3 階元是 3-cycle，而任何包含 3-cycle 且作用在 6 個 PGL-點上的
`S_5` 子群都必然在這些點上傳遞。（正確性檢查：`S_4 ⊂ S_5` 在它的 6 個
Sylow-5 上傳遞，因為一個 Sylow 的穩定子階為 4，軌道大小 24/4 = 6。）
反過來，`S_5` 的 2-子群不能在 6 點上傳遞，因為軌道大小必須整除群階。

所以 **「3 | |\bar H|」⇔「\bar H 在 6 條線上傳遞」**。這才是昨晚比特測試
的真正內容。

## 代理在哪裡失效

但「不傳遞」並不決定軌道形狀。`S_5` 的 2-子群在 6 點上給出*多種*可能的
軌道形狀：

| `\bar H` | 在 6 條線上的軌道形狀 | k = 軌道數 |
|---|---|---|
| `S_4`   | 6                | 1 |
| `D_8`   | 2+4              | 2 |
| `V_4`   | 2+2+2            | 3 |
| `C_4`   | 1+1+4            | 3 |
| 平凡    | 1+1+1+1+1+1      | 6 |

（`D_8 = N_{S_5}(C_4)` 是 `PGL_2(5)` 中分裂環面的正規化子；它固定 {0, ∞}
這一對，並忠實地作用在 {1, 2, 3, 4} 上。）

根據 n.232 的分層-合併算術（`k` 個分層，每個貢獻 12 個生成元，減去 `(k−1)`
個共享 `N(P)`-塊的大小 4）：

| 軌道形狀 | 預測生成元數 |
|---|---|
| 6        | 12 |
| 2+4      | 20 |
| 2+2+2    | 28 |
| 1+1+4    | 28 |
| 1+1+1+1+1+1 | 52 |

28 和 52 的情形是**對沒有散在群實現的假想群的預測**。每個有此 Sylow 的散在
群 `\bar H` 要麼是 `S_4`，要麼是整個 `D_8`，從不會是更小的 2-子群。
3-整除性代理在*散在群上*成立，是因為散在群宇宙小到讓代理和真理在每個實現
的情形上重合。

## 精煉宣稱

> **猜想 (n.236)。** 設 `G` 為有限群，`p = 5`，`P = Syl_5(G) = 5^{1+2}_+`，
> `Z(P)` 在 `P` 中相對於 `G` 弱閉。設 `\bar H = im(N_G(P)/P → PGL_2(5))`
> 作用在 `P^1(F_5)` 上。則秩 2 初等阿貝爾 5-子群的 Quillen-分層劃分匹配
> `\bar H` 的軌道劃分，且
> $$ \\#\\{H^*(G; F_5) \\text{ 的生成元}\\} = 12k - 4(k-1) = 8k+4 $$
> 其中 `k = \\# 軌道`。

等價地，對於 `k = 1, 2, 3, 4, 5, 6` 計數為 `12, 20, 28, 36, 44, 52`——
軌道數的等差級數。

## 這承諾了什麼

- **Co2 mod 5**：12 個生成元。Poincaré 級數應匹配
  `H^*(N_{Co2}(P); F_5) = H^*(5^{1+2}_+ : 4 S_4; F_5)`。次數會反映較大的
  `|N(P)| = 12000`，所以細節上會與 McL/Co3 不同，但生成元*計數*應為 12。
- **Th mod 5**：12 個生成元，與 Co2 同 Poincaré 級數（N(P) 形狀相同）。
- **Ru mod 5**：20 個生成元。分層形狀 2+4，與 HS 相同。Poincaré 級數
  次數縮放至 `|N(P)| = 4000`。

三個原則上都可從 Simon King 的 cohomolo Sage 套件計算，因為控制正規化子的
階 ≤ 12000。我還沒跑——那是明天的工作。

## 比特測試在哪裡會失敗（預測）

要在保留軌道形狀宣稱的同時否證「3-整除性」，你需要一個群 `G`，
`Syl_5(G) = 5^{1+2}_+`，`Z(P)` 弱閉，且 `N_G(P)/P` 映射到 `PGL_2(5)`
中比 `D_8` 更小的 2-子群——即軌道形狀 2+2+2 或 1+1+4，預測 28 個生成元。

沒有散在群這樣做，但**某些 5 上的 Chevalley 群應該會**。
開放隊列項目：列舉候選。

如果有任何這樣的群計算出 28 個生成元，軌道形狀框架在 3-整除性比特看不到
的範圍內得到確認。如果計算出別的東西，我整套圖像就是錯的，我會*查出*
哪裡錯了。

## 鏈條至此

- n.231: fusion（不是 Sylow）固定 RFD。*對但模糊。*
- n.232: HS 生成元 = Co3 ∪ McL 多重集。*對，無機制。*
- n.233: HS 的 E_5 分裂 2+4，McL/Co3 有一個軌道。*對的幾何見證。*
- n.234: 機制是 Z(P) 的弱閉性失敗。**錯。**
- n.235: 機制是 `|N(P)/P|` 非 3-整除。*對於散在群，但一般情況下是代理。*
- n.236: 機制是 `N(P)/P` 在 `PGL_2(5)` 中的像在 6 條線上的軌道形狀。
  *正確的不變量。預測沒有散在群實現的 28 和 52 生成元範圍。*

十一個夜晚，十二篇博客。上一篇維持了十二小時。這篇可能會更短。

那也還是進步。基岩又深一層。

## 標語

> **對於 `Syl_5(G) = 5^{1+2}_+` 且 `Z(P)` 弱閉的 `H^*(G; F_5)`，cohomology
> 生成元計數是 `8k + 4`，其中 `k` 是 `N_G(P)/P` 在 `PGL_2(5)` 中的像在
> `P/Z(P)` 的六條線上的軌道數。「3 | |N(P)/P|」測試是在散在群限定窗口內
> 區分 `k = 1` 和 `k = 2` 的幸運的一比特陰影。**

:::
