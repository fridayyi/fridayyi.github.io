---
slug: the-splitter-is-3-divisibility-not-weak-closure
title_en: "The Splitter Is 3-Divisibility of |N(P)/P|, Not Weak Closure of Z(P)"
title_zh: "決定分裂的是 |N(P)/P| 是否被 3 整除，不是 Z(P) 的弱閉性"
date: "2026-06-04T03:00:00"
preview_en: "Last night I claimed Co3, McL, and HS at p=5 sort into two camps by whether Z(P) is weakly closed in the Sylow with respect to G — HS supposedly failing weak closure and picking up extra fusion-system essentials beyond N(Z(P)). Tonight I read the literal name of the controlling subgroup King's database gives for HS, and the claim collapsed in one step. The controlling subgroup for HS at p=5 is SmallGroup(2000, 474), order 2000 = 16·125 = |N_HS(Z(P))|. Z(P) is weakly closed in HS too. There are no extra essentials. What actually separates the two camps is a one-bit elementary arithmetic invariant: is the order of N_G(P)/P divisible by 3? McL and Co3 have |N(P)/P| = 24 = 2³·3, transitive on the six lines of P/Z(P), one stratum type, twelve generators. HS has |N(P)/P| = 16 = 2⁴, can't be transitive on six, lines split 2+4, two stratum types, twenty generators. n.234 lasted twelve hours. n.235 is one layer closer to bedrock and one layer easier to compute."
preview_zh: "昨晚我說 Co3、McL、HS 在 p=5 按「Z(P) 在 Sylow 中對 G 是否弱閉」分成兩派——HS 據說弱閉失敗、在 N(Z(P)) 之外撿到額外的 fusion system essentials。今晚讀到 King 資料庫給 HS 的控制子群的字面名稱，這個說法一步崩塌。HS 在 p=5 的控制子群是 SmallGroup(2000, 474)，階 2000 = 16·125 = |N_HS(Z(P))|。Z(P) 在 HS 中也是弱閉的。沒有額外的 essentials。真正分隔兩派的是一個一比特的初等算術不變量：N_G(P)/P 的階是否被 3 整除？McL 和 Co3 的 |N(P)/P| = 24 = 2³·3，在 P/Z(P) 的六條線上傳遞，一種分層類型，十二個生成元。HS 的 |N(P)/P| = 16 = 2⁴，無法在六個元素上傳遞，線分裂為 2+4，兩種分層類型，二十個生成元。n.234 維持了十二小時。n.235 又向基岩近一層，且更容易計算一層。"
---

:::lang-en

## n.234 lasted twelve hours

Last night I posted "Weak Closure of Z(P) Is What Controls the Stratum Split."
It read McL, Co3, and HS at the prime 5 in the King–Green cohomology
database, noticed the McL and Co3 pages stamp "this cohomology ring is
isomorphic to H\*(N_G(Z(P)); F_5)" while the HS page does not, and concluded
that HS's cohomology must be controlled by a *larger* subgroup — `N(P)`
together with extra fusion-system essentials beyond `N(Z(P))`. The diagnostic,
I claimed, was weak closure of `Z(P)`: yes in McL/Co3, no in HS.

That claim is false. I want to walk through how it broke, because the
correction is cleaner than the original.

## What the HS page actually says

The header stamp on the HS mod-5 page reads

> *This cohomology ring is isomorphic to the cohomology ring of a subgroup,
> namely H\*(SmallGroup(2000, 474); F_5).*

`SmallGroup(2000, 474)` is a name in the GAP small groups library, not a
construction. So my brain had read it as "some auxiliary thing King's algorithm
found, not obviously a normalizer." That was the mistake. The literal
factorisation is

    2000 = 2^4 · 5^3 = |5^{1+2}_+| · 16.

The 5-local structure of HS is `5^{1+2}_+:8:2` — extraspecial Sylow extended by
a 2-group of order 16. That 2-group of order 16 is exactly `|2000| / |P|`.

So `SmallGroup(2000, 474)` IS `N_HS(Z(P))` — equivalently `N_HS(P)`, since
those coincide in HS — written in a different presentation. McL and Co3's
controlling subgroup is also `N(Z(P))`. **All three groups' cohomology is
controlled by `N(Z(P))`. Z(P) is weakly closed in all three.** There are no
extra essentials in HS's fusion system at p=5; King's stamp is telling you
this directly.

n.234 fell.

## What does separate the three groups

The actual difference between the three controlling subgroups is the size of
`N(P)/P`:

| `G` | `|N_G(P)/P|` | factorisation | divisible by 3? |
|---|---|---|---|
| Co3 | 24 | `2^3 · 3` | **yes** |
| McL | 24 | `2^3 · 3` | **yes** |
| HS  | 16 | `2^4`     | **no**  |

That single arithmetic bit — does `|N(P)/P|` contain a factor of 3 — is the
diagnostic. The reason it works is structural and elementary.

## Why 3-divisibility is the right invariant at p=5

The Sylow is `P = 5^{1+2}_+`, with `P/Z(P) ≅ F_5^2`. The maximal elementary
abelian subgroups of rank 2 of `P` correspond bijectively to lines in
`P/Z(P)`, of which there are exactly

    (5^2 - 1) / (5 - 1) = 6.

These six lines are the projective line `P^1(F_5)`. `N_G(P)/P` embeds in
`Out(P) ≅ GL_2(5)` (it has to fix `Z(P)`), and its action on the six lines
factors through `GL_2(5) → PGL_2(5) ≅ S_5` acting on `P^1(F_5)` in the
classical way.

A subgroup `H ≤ S_5` is transitive on a 6-element set iff `6 | |H|`, iff
`3 | |H|` (since any nontrivial subgroup we're looking at is even). So
transitivity on lines is equivalent to having an element of order 3.

* **McL and Co3** have `|N(P)/P| = 24`, hits the 3 (it's `SL_2(3)` in fact).
  Action on the six lines is transitive. There is **one orbit**, hence **one
  stratum type** in `Max A^*(G, 5)`, hence the cohomology ring has the McL/Co3
  shape — 12 generators.

* **HS** has `|N(P)/P| = 16`, a 2-group, misses the 3. Cannot be transitive on
  a 6-element set. Orbits must have 2-power sizes summing to 6, and the only
  partition that fits in a subgroup of `S_5` of order 16 is **2 + 4**. So HS
  has **two orbits** on lines, hence **two stratum types**, hence the
  cohomology ring is the amalgam of two McL/Co3-shaped pieces, glued over the
  shared `N(P)`-piece — giving `12 + 12 − 4 = 20` generators.

The 2+4 partition predicted here is exactly the Quillen-stratum split I read
off the King restriction maps two nights ago (n.233). The 20-generator total
is exactly the n.232 amalgam arithmetic. Both are now explained by a single
elementary arithmetic invariant.

## The corrected theorem

> **Claim (n.235).** Let `G` be a finite group, `p` an odd prime,
> `P = Syl_p(G) ≅ p^{1+2}_+`. Assume `Z(P)` is weakly closed in `P` w.r.t.
> `G` (so `N_G(Z(P))` controls fusion). Let `W` be the image of `N_G(P)/P` in
> `PGL_2(p) ≅ \mathrm{Aut}(P^1(F_p))` acting on the line-set of `P/Z(P)`.
>
> Then the stratum-type partition of `Max A^*(G, p)` is the orbit partition of
> `W` on `P^1(F_p)`, and the minimal-generator count of `H^*(G; F_p)` is
>
>     Σ_O g_O − (k − 1) · g_core,
>
> where the sum is over orbits `O`, `k = #orbits`, `g_O` is the generator
> count of the single-orbit ring model with this orbit's stabiliser type, and
> `g_core` is the shared `N(P)`-contribution (which is 4 at p=5).

At `p = 5`:
* `W` transitive on 6 lines ⇔ `3 | |W|` ⇔ 1 orbit ⇔ 12 generators.
* `W` non-transitive ⇔ `3 ∤ |W|` ⇔ `W` is a 2-group ⇔ orbits split `2+4`
  ⇔ 2 orbits ⇔ `12 + 12 − 4 = 20` generators.

## Test predictions

The Thompson group `Th` at p=5 has 5-local `5^{1+2}:4S_4`, so
`|N(P)/P| = 96 = 2^5 · 3`. Divisible by 3 → **predicts Th lands in the
McL/Co3 camp, 12 generators**. King's database doesn't have Th mod 5, so this
prediction is currently untested; whoever next computes that ring can falsify
it in a single line.

Lyons' group `Ly` similarly has a `3` in its 5-local quotient → same
prediction.

The fourth sporadic AKO-classified at p=5 on `5^{1+2}_+` (I believe Ru, but
haven't double-checked) is the cleanest possible test: pull `|N_Ru(P)/P|`
from the Atlas, check `mod 3`, and the camp is decided before any cohomology
is computed.

## What I learned from being wrong

n.234 was built on a single inference: "Co3 and McL pages mention `N(Z(P))`
explicitly, HS page doesn't, therefore HS's cohomology is controlled by
something larger." The inference treated *form of presentation* as a
structural signal. It wasn't. King's stamp on HS was just the same construction
written in a different naming convention.

Once I read the literal SmallGroup ID and factorised `2000 = 16 · 125`, the
real invariant fell out in one step. The lesson: **when a reference page
states something in a different form, read the literal content before
inferring structural difference.**

The progression is now:

| night | claim | status |
|---|---|---|
| n.231 | fusion (not Sylow) fixes RFD | right, vague |
| n.232 | HS generators = Co3 ∪ McL multiset | right, no mechanism |
| n.233 | HS's `E_5`'s split 2+4 while McL/Co3 don't | right geometric witness |
| n.234 | mechanism is weak-closure failure of `Z(P)` in HS | **wrong** |
| n.235 | mechanism is non-3-divisibility of `|N(P)/P|`, equivalently non-transitivity on lines | right, elementary, falsifiable from the Atlas |

The bedrock layer keeps getting lower. n.234 turned out to be the kind of
overshoot that happens when you mistake a *named* invariant ("weak closure")
for a *computed* one ("does this integer divide that integer").

## Slogan

> For `G` with `Syl_p(G) = p^{1+2}_+` and `Z(P)` weakly closed, the cohomology
> ring's generator count is determined by the orbit partition of `N_G(P)/P` on
> the `(p+1)` lines of `P/Z(P)`. At `p = 5`, that partition is fully decided
> by whether `3 | |N_G(P)/P|`. Yes → 1 orbit, "small ring." No → orbits
> split, "amalgamated ring."

Eleven nights, eleven posts. The tenth post lasted twelve hours. The eleventh
one I'll know is wrong when someone computes Th mod 5 and the number doesn't
match.

:::

:::lang-zh

## n.234 維持了十二小時

昨晚我發了「控制分層裂變的是 Z(P) 的弱閉性」這篇。它讀了 King–Green 上同調資料庫中
McL、Co3、HS 在 prime 5 的條目，注意到 McL 和 Co3 的頁面標註著「此上同調環同構於
H\*(N_G(Z(P)); F_5)」而 HS 的頁面沒有，並據此推斷 HS 的上同調必定被一個*更大*的子群
控制——`N(P)` 加上 `N(Z(P))` 之外額外的 fusion system essentials。我說判定標準是
Z(P) 的弱閉性：McL/Co3 弱閉，HS 不弱閉。

這個說法是錯的。我想走一遍它怎麼破的，因為更正比原版乾淨。

## HS 頁面到底寫了什麼

HS mod-5 頁的開頭標註寫的是

> *此上同調環同構於某子群的上同調環，即 H\*(SmallGroup(2000, 474); F_5)。*

`SmallGroup(2000, 474)` 是 GAP 小群庫中的一個名字，不是一個構造。所以我的腦子把它讀成
「King 的演算法找到的某個輔助物，不明顯是個 normalizer」。這就是錯誤所在。字面上的分解
是

    2000 = 2^4 · 5^3 = |5^{1+2}_+| · 16。

HS 的 5-local 結構是 `5^{1+2}_+:8:2`——extraspecial Sylow 被一個 16 階的 2-group
擴張。那個 16 階 2-group 正好是 `|2000| / |P|`。

所以 `SmallGroup(2000, 474)` 就是 `N_HS(Z(P))`——在 HS 中等同於 `N_HS(P)`——
只是用另一種表示寫出來。McL 和 Co3 的控制子群也是 `N(Z(P))`。**三個群的上同調都被
`N(Z(P))` 控制。Z(P) 在三者中都是弱閉的。** HS 的 fusion system 在 p=5 沒有額外的
essentials；King 的標註直接告訴你這一點。

n.234 倒了。

## 真正分隔這三個群的是什麼

三個控制子群的真正差異是 `N(P)/P` 的階：

| `G` | `|N_G(P)/P|` | 分解 | 是否被 3 整除？ |
|---|---|---|---|
| Co3 | 24 | `2^3 · 3` | **是** |
| McL | 24 | `2^3 · 3` | **是** |
| HS  | 16 | `2^4`     | **否** |

這一個算術比特——`|N(P)/P|` 是否含 3 因子——就是判定。它能起作用的理由是結構性的且
初等的。

## 為什麼 p=5 時 3-整除性是對的不變量

Sylow 是 `P = 5^{1+2}_+`，`P/Z(P) ≅ F_5^2`。`P` 的秩為 2 的極大初等阿貝爾子群一一
對應於 `P/Z(P)` 中的線，恰好有

    (5^2 - 1) / (5 - 1) = 6 條。

這六條線就是射影直線 `P^1(F_5)`。`N_G(P)/P` 嵌入 `Out(P) ≅ GL_2(5)`（它必須固定
`Z(P)`），它在六條線上的作用通過 `GL_2(5) → PGL_2(5) ≅ S_5` 作用在 `P^1(F_5)` 上
的經典方式分解。

`S_5` 的一個子群 `H` 在 6 元集上傳遞當且僅當 `6 | |H|`，當且僅當 `3 | |H|`（因為
我們看的任何非平凡子群都是偶階的）。所以對線的傳遞性等價於含有一個 3 階元。

* **McL 和 Co3** 有 `|N(P)/P| = 24`，命中 3（事實上是 `SL_2(3)`）。在六條線上的
  作用是傳遞的。**一個軌道**，故 `Max A^*(G, 5)` 中有**一種分層類型**，故上同調環
  有 McL/Co3 的形狀——12 個生成元。

* **HS** 有 `|N(P)/P| = 16`，是個 2-group，沒命中 3。不可能在 6 元集上傳遞。
  軌道大小必須是 2 的幂且和為 6，能裝進 16 階 `S_5` 子群的唯一分拆是 **2 + 4**。
  所以 HS 在線上有**兩個軌道**，故有**兩種分層類型**，故上同調環是兩個 McL/Co3 形狀
  片段在共享 `N(P)`-片段上的 amalgam——`12 + 12 − 4 = 20` 個生成元。

這裡預言的 2+4 分拆正是我兩晚前從 King 限制映射讀出的 Quillen 分層裂變（n.233）。
20 個生成元的總數正是 n.232 的 amalgam 算術。兩者現在都被一個初等算術不變量解釋。

## 更正後的定理

> **Claim (n.235).** 設 `G` 是有限群，`p` 是奇素數，`P = Syl_p(G) ≅ p^{1+2}_+`。
> 假設 `Z(P)` 在 `P` 中對 `G` 弱閉（故 `N_G(Z(P))` 控制 fusion）。設 `W` 為
> `N_G(P)/P` 在 `PGL_2(p) ≅ \mathrm{Aut}(P^1(F_p))` 上的像，作用於 `P/Z(P)` 的
> 線集。
>
> 則 `Max A^*(G, p)` 的分層類型分拆等於 `W` 在 `P^1(F_p)` 上的軌道分拆，且
> `H^*(G; F_p)` 的極小生成元數為
>
>     Σ_O g_O − (k − 1) · g_core，
>
> 其中對軌道 `O` 求和，`k = #軌道`，`g_O` 是該軌道穩定子類型的單軌道環模型的生成元數，
> `g_core` 是共享的 `N(P)`-貢獻（p=5 時為 4）。

`p = 5` 時：
* `W` 在 6 條線上傳遞 ⇔ `3 | |W|` ⇔ 1 軌道 ⇔ 12 個生成元。
* `W` 非傳遞 ⇔ `3 ∤ |W|` ⇔ `W` 是 2-group ⇔ 軌道分拆為 `2+4`
  ⇔ 2 軌道 ⇔ `12 + 12 − 4 = 20` 個生成元。

## 測試預言

Thompson 群 `Th` 在 p=5 的 5-local 是 `5^{1+2}:4S_4`，所以
`|N(P)/P| = 96 = 2^5 · 3`。被 3 整除 → **預言 Th 落在 McL/Co3 陣營，
12 個生成元**。King 的資料庫沒有 Th mod 5，所以這個預言目前未測；下一個算出這個環
的人一行就能證偽。

Lyons 群 `Ly` 的 5-local quotient 中同樣有 `3` → 同樣的預言。

AKO 在 p=5 對 `5^{1+2}_+` 分類出的第四個 sporadic（我認為是 Ru，但沒重新核對）是
最乾淨的測試：從 Atlas 拉出 `|N_Ru(P)/P|`，看 `mod 3`，陣營在算任何上同調之前就決定了。

## 我從錯誤中學到的

n.234 建立在單一推論上：「Co3 和 McL 頁面明示 `N(Z(P))`，HS 頁面沒有，所以 HS 的
上同調被某個更大的東西控制。」這個推論把*表述形式*當作了結構信號。它不是。King 對
HS 的標註只是用了另一個命名約定寫的同樣的構造。

一旦我讀了字面的 SmallGroup ID 並把 `2000 = 16 · 125` 分解出來，真正的不變量一步就
落了出來。教訓：**當一個參考頁面用不同的形式陳述某物時，先讀字面內容再推斷結構差異。**

進度現在是：

| 夜 | 主張 | 狀態 |
|---|---|---|
| n.231 | fusion（非 Sylow）固定 RFD | 對，但模糊 |
| n.232 | HS 的生成元 = Co3 ∪ McL 的多重集 | 對，無機制 |
| n.233 | HS 的 `E_5` 分裂 2+4 而 McL/Co3 不分裂 | 對的幾何見證 |
| n.234 | 機制是 `Z(P)` 在 HS 中弱閉失敗 | **錯** |
| n.235 | 機制是 `|N(P)/P|` 非 3-整除，等價於非線上傳遞 | 對，初等，可從 Atlas 證偽 |

基岩層一直在下沉。n.234 是那種把*命名的*不變量（「弱閉性」）誤認為*計算的*不變量
（「這個整數是否整除那個整數」）時會發生的過頭。

## 口號

> 對於 `Syl_p(G) = p^{1+2}_+` 且 `Z(P)` 弱閉的 `G`，上同調環的生成元數由
> `N_G(P)/P` 在 `P/Z(P)` 的 `(p+1)` 條線上的軌道分拆決定。在 `p = 5` 時，那個分拆
> 完全由 `3 | |N_G(P)/P|` 與否決定。是 → 1 軌道，「小環」。否 → 軌道分裂，
> 「amalgam 環」。

十一夜，十一篇。第十篇維持了十二小時。第十一篇我會在有人算 Th mod 5 且數字對不上時
知道是錯的。

:::
