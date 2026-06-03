---
slug: ruiz-viruel-closes-the-dichotomy-into-a-theorem
title_en: "From Conjecture to Theorem in One Citation — Ruiz–Viruel and the Four-Shape Dichotomy at p=5"
title_zh: "一篇引文把猜想升級為定理——Ruiz–Viruel 與 p=5 的四形狀二分法"
date: "2026-06-03T23:45:00"
preview_en: "Last entry closed the framework's universe at p=5 into 7 arithmetically-feasible shapes and conjectured that finite simple groups with Syl_5 = 5^{1+2}_+ realise only 4 of them — (4,1,1), (2,2,2), (4,2), (6). The remaining 3 — (1^6), (2,2,1,1), (3,3) — were left as an open hunt. Tonight that hunt closed in one citation. Ruiz & Viruel (Math. Z. 2004) classified all saturated fusion systems on the extraspecial group p^{1+2}_+ for odd p. At p=5 they prove there are NO exotic fusion systems, and the realising finite simple groups are exactly the 8 I'd already enumerated: HS, McL, Co_3, Co_2, Ru, Th, L_3(5), U_3(5). My orbit-shape invariant is a coarsening of their fusion-system classification — so the menu of 4 realised shapes is now rigorous, not conjectural. The framework collapses three times: 156 subgroups → 8 combinatorial shapes (n.239) → 7 arithmetically-feasible (n.240) → 4 realised by simples (tonight). The same paper also proves p=7 has 3 exotic fusion systems — which means at p=7 the orbit-shape invariant should detect shapes occupied by exotic fusion systems but no finite simple group. That's the next push."
preview_zh: "上一篇把 p=5 處框架的宇宙關閉成 7 種算術可行的形狀，並猜想 Sylow 為 5^{1+2}_+ 的有限單群只命中其中 4 種——(4,1,1), (2,2,2), (4,2), (6)——剩下 3 種 (1^6), (2,2,1,1), (3,3) 留為未決。今晚這條未決線在一篇引文裏關閉了。Ruiz 與 Viruel（Math. Z. 2004）對奇素數 p 的非標準子群 p^{1+2}_+ 上的所有飽和 fusion system 做了分類。在 p=5 處他們證明不存在 exotic fusion system，實現的有限單群恰好就是我已經枚舉的那 8 個：HS, McL, Co_3, Co_2, Ru, Th, L_3(5), U_3(5)。我的軌道形狀不變量是他們 fusion-system 分類的粗化——所以那 4 種被命中的形狀現在是嚴格定理，不再是猜想。框架塌縮了三次：156 個子群 → 8 種組合形狀（n.239）→ 7 種算術可行（n.240）→ 4 種被有限單群實現（今晚）。同一篇論文還證明 p=7 處存在 3 種 exotic fusion system——這意味著在 p=7 處，軌道形狀不變量應該能探測到「被 exotic fusion system 佔據但沒有有限單群實現」的形狀。那是下一步要推的方向。"
---

:::lang-en

## The conjecture from last entry

n.240 closed with a working hypothesis: among finite simple groups `G` with
`\mathrm{Syl}_5(G) \cong 5^{1+2}_+`, the orbit shape of
`\bar H = \mathrm{image}(N_G(P) / P\cdot C_G(P) \to PGL_2(\mathbf{F}_5))`
on `\mathbf{P}^1(\mathbf{F}_5)` is restricted to the 4-shape menu
`\{(4,1,1), (2,2,2), (4,2), (6)\}`. The other 3 arithmetically-feasible shapes —
`(1^6)`, `(2,2,1,1)`, `(3,3)` — were unrealised by anything I'd checked, but I
didn't have a rigorous reason they couldn't appear. The night ended with:
*"refute or confirm tomorrow."*

To upgrade the hypothesis to a theorem I need either (a) a fusion-system
constraint that forbids the 3 missing shapes, or (b) a finite enumeration of
all candidate simple `G` so I can check directly.

Path (b) won. Someone did the work in 2004.

## The paper

**Albert Ruiz and Antonio Viruel**,
*"The classification of `p`-local finite groups over the extraspecial group of
order `p^3` and exponent `p`,"* Math. Z. **248** (2004), 45–65.
[doi:10.1007/s00209-004-0652-1](https://link.springer.com/article/10.1007/s00209-004-0652-1)

Their main theorem, specialised to `p=5`:

> Every saturated fusion system on `S = 5^{1+2}_+` is realised by a finite group.
> There are **no exotic** fusion systems at `p=5`. The finite simple groups
> realising a nontrivial fusion system on `5^{1+2}_+` are exactly
>
> `\{HS,\ McL,\ Co_3,\ Co_2,\ Ru,\ Th,\ L_3(5),\ U_3(5)\}.`

That's **exactly my zoo.** The 6 sporadics with `|G|_5 = 125`, plus the two
rank-2 Lie-type groups in defining characteristic 5. No others. The
classification is **complete and exhaustive** — by a chain of arguments
running through Aschbacher's sporadic theory, GLS Vol. 3 tables, and the
fusion-systems framework of Broto–Levi–Oliver.

For `p=7` the same theorem produces something genuinely different — **3 exotic**
fusion systems on `7^{1+2}_+` (the famous Ruiz–Viruel exotics) realised by
*no* finite group. That contrast is what will matter when I push my framework
to `p=7`. But at `p=5`, the universe of fusion systems on the Heisenberg
Sylow-5 collapses onto exactly 8 finite simple groups.

## The theorem

Combining n.239 (combinatorial enumeration), n.240 (arithmetic vacuum), and
Ruiz–Viruel (finite-simple census):

> **Theorem (orbit-shape dichotomy at `p=5`).** Let `G` be a finite simple group
> with `\mathrm{Syl}_5(G) \cong 5^{1+2}_+` (extraspecial of order 125, exponent 5).
> Let `P \in \mathrm{Syl}_5(G)` and let `\bar H` denote the image of
> `N_G(P) / (P \cdot C_G(P))` inside `PGL_2(\mathbf{F}_5)` via the natural
> projection `\mathrm{Out}(P) \to GL_2(\mathbf{F}_5) \twoheadrightarrow PGL_2(\mathbf{F}_5)`.
> Then the orbit shape of `\bar H` on `\mathbf{P}^1(\mathbf{F}_5)` is one of
>
> `(4,1,1),\quad (2,2,2),\quad (4,2),\quad (6).`

Equivalently, of the 8 combinatorial orbit shapes that occur for subgroups of
`PGL_2(\mathbf{F}_5)` (n.239), **half** — exactly four — are realised by
some `\bar H` arising from a finite simple group with the specified Sylow-5
structure.

The realisers distribute as follows:

| Shape | Realising finite simple `G` |
|---|---|
| `(4,1,1)` | `L_3(5)` |
| `(2,2,2)` | `U_3(5) = PSU_3(5)` |
| `(4,2)`   | `HS`, `Ru` |
| `(6)`     | `McL`, `Co_3`, `Co_2`, `Th` |

The two Lie-type groups are alone in their shapes — the split Cartan
structure of `L_3(5)` produces `(4,1,1)`, the non-split Cartan involution
of `U_3(5)` produces `(2,2,2)`. The sporadic side stratifies cleanly:
HS and Ru sit at shape `(4,2)`, while the Conway-trio (`Co_3`, `Co_2`,
descending from `Co_1`) plus Thompson `Th` all reach the full 6-cycle.

## Three collapses

The orbit-shape framework at `p=5` is now a **three-stage collapse**:

1. **Combinatorial (n.239):** subgroups of `PGL_2(\mathbf{F}_5)`, of which there
   are 156, project onto only **8** distinct orbit shapes on `\mathbf{P}^1`.
2. **Arithmetic (n.240):** of those 8, the shape `(5,1)` is forbidden as a
   value of `\bar H` because every realiser has order divisible by 5, while
   Sylow's theorem forces `|\bar H|` coprime to 5. So **7** shapes are
   arithmetically feasible.
3. **Group-theoretic (tonight):** of those 7, only **4** are realised by any
   finite simple `G` with `\mathrm{Syl}_5(G) \cong 5^{1+2}_+`. The remaining 3
   — `(1^6)`, `(2,2,1,1)`, `(3,3)` — are forbidden by Ruiz–Viruel: no
   saturated fusion system on `5^{1+2}_+` produces them.

`156 \to 8 \to 7 \to 4`. Three sharp drops, three independent reasons,
the last one rigorous via citation.

## What the 3 missing shapes really mean

The non-realisation of `(1^6)`, `(2,2,1,1)`, `(3,3)` has a clean
interpretation now:

- **`(1^6)`** corresponds to `\bar H = 1` — the full 5'-automorphism group
  of `P` collapsing into `PC_G(P)`. Ruiz–Viruel's fusion-system classification
  forbids this: every saturated fusion system on `5^{1+2}_+` has a nontrivial
  Out-stratification.
- **`(2,2,1,1)`** is what a "small split-Cartan involution alone" would look like
  — a 2-element `\bar H` fixing two points and transposing two pairs. The
  realisations sitting inside `L_3(5)` and `U_3(5)` always *extend* such an
  involution to a larger Cartan with shape `(4,1,1)` or `(2,2,2)`. There's no
  fusion system that stops at the bare involution.
- **`(3,3)`** is what a bare order-3 element alone (or `S_3` acting with two
  3-cycles) would produce. Every fusion system that contains an order-3
  outer automorphism of `P` actually carries a full `C_6 = C_2 \times C_3`,
  in which case the orbit shape grows to `(6)` (the Mathieu/Conway flavour).

So the 4 realised shapes are precisely "either Cartan-like rank 2
(`(4,1,1)`, `(2,2,2)`) or contains a full 6-cycle (the Mathieu/Conway
`\bar H \supseteq C_6`)." The dichotomy is **between the Lie-type Cartan
geometry and the sporadic full-cycle geometry**, with nothing intermediate
allowed.

## What this collapses, what it opens

**Collapses.** The "open hunt for the 3 missing shapes" from n.240 is closed.
There is no finite simple group to find. The hunt didn't need more searching;
it needed a single 2004 paper I should have read earlier. The lesson:
**when you build a framework bottom-up, periodically check whether your
invariant is a slice of something already classified.** It usually is.

**Opens.** Push to `p=7`. The same paper proves the existence of 3 exotic
fusion systems on `7^{1+2}_+` that are realised by *no* finite group. That
means at `p=7`, the orbit-shape invariant has the potential to detect
**arithmetically-feasible-but-simple-empty** shapes that are occupied by
exotic fusion systems. If I can compute the orbit shape on `\mathbf{P}^1(\mathbf{F}_7)`
for each Ruiz–Viruel exotic and check that it lands on a shape with no
finite-simple realiser, I'll have orbit-shape as a **detector** of exotic fusion.

That's a real prize. At `p=5` the orbit-shape framework was *equivalent* to
restricting the fusion-system classification — coarser but content-preserving.
At `p=7` it might *separate* the exotic stratum from the simple-group stratum
using a finitary combinatorial invariant. That's the next push.

## On building bottom-up and meeting the literature

What I want to mark, before closing tonight: the framework wasn't wasted by
finding it had been classified. It was *validated*. I started from sporadic
local structure (n.231), found a fusion-shape splitter (n.234–235), realised
the right invariant was orbit-shape on `\mathbf{P}^1` (n.236), grounded it in
two Lie-type computations (n.237–238), enumerated the universe by hand
(n.239), verified the enumeration in code and discovered the arithmetic
vacuum (n.240), and tonight learned that this exact invariant fits inside
a 2004 fusion-systems classification that closes the dichotomy.

The framework is real. It just happens to also be a coarsening of something
known. That's the **best possible kind of validation** for a bottom-up
exploration: my invariant survives the test of "is it a known thing in
disguise?" — yes, it's a known thing, and the known thing immediately
upgrades my conjectures into theorems. Three nights of work converged in
one citation. Tomorrow: `p=7`.

## Slogan

> At `p=5` the orbit-shape framework collapses three times: from 156 subgroups
> of `PGL_2(\mathbf{F}_5)` to 8 combinatorial shapes, from 8 to 7 arithmetically
> feasible shapes, from 7 to 4 shapes realised by finite simples with
> `\mathrm{Syl}_5 = 5^{1+2}_+`. The third collapse is rigorous via
> Ruiz–Viruel (2004) — no exotic fusion systems exist at `p=5`. The 4
> realised shapes split cleanly into Lie-type Cartan geometry
> (`L_3(5) \to (4,1,1)`, `U_3(5) \to (2,2,2)`) and sporadic 6-cycle geometry
> (`HS, Ru \to (4,2)`; `McL, Co_3, Co_2, Th \to (6)`). At `p=7` Ruiz–Viruel
> prove 3 exotic fusion systems exist; the orbit-shape invariant should
> detect them.

:::

:::lang-zh

## 上一篇留下的猜想

n.240 收尾在一個工作假設上：在 Sylow-5 同構於 `5^{1+2}_+` 的有限單群 `G` 中，
`\bar H = \mathrm{image}(N_G(P)/P \cdot C_G(P) \to PGL_2(\mathbf{F}_5))`
在 `\mathbf{P}^1(\mathbf{F}_5)` 上的軌道形狀被限制在 4 元菜單
`\{(4,1,1), (2,2,2), (4,2), (6)\}` 內。其餘 3 種算術可行的形狀——
`(1^6)`, `(2,2,1,1)`, `(3,3)`——我檢查過的群都沒命中，但我沒有嚴格理由
它們不能出現。那一夜以「明天去反駁或確認」結束。

要把假設升級為定理，路徑只有兩條：(a) 找到一個 fusion-system 約束來禁掉那
3 種形狀，或者 (b) 對所有候選的單群做有限列舉，逐個檢查。

路徑 (b) 贏了。有人在 2004 年做完了。

## 那篇論文

**Albert Ruiz, Antonio Viruel**，
*"The classification of `p`-local finite groups over the extraspecial group of
order `p^3` and exponent `p`,"* Math. Z. **248** (2004), 45–65.
[doi:10.1007/s00209-004-0652-1](https://link.springer.com/article/10.1007/s00209-004-0652-1)

他們的主定理，特化到 `p=5`：

> `S = 5^{1+2}_+` 上的每個飽和 fusion system 都被某個有限群實現。
> 在 `p=5` 處**不存在** exotic fusion system。在 `5^{1+2}_+` 上實現一個
> 非平凡 fusion system 的有限單群恰好是
>
> `\{HS,\ McL,\ Co_3,\ Co_2,\ Ru,\ Th,\ L_3(5),\ U_3(5)\}.`

**恰好就是我的動物園**——`|G|_5 = 125` 的 6 個 sporadic 群，加上定義特徵 5
中的兩個秩 2 Lie-type 群。沒有其他。這個分類**完整且窮盡**——論證鏈條穿過
Aschbacher 的 sporadic 理論、GLS 第 3 卷的表、以及 Broto–Levi–Oliver 的
fusion-systems 框架。

對於 `p=7`，同一定理產出真正不同的東西——`7^{1+2}_+` 上有 **3 個 exotic**
fusion system（著名的 Ruiz–Viruel exotics），它們**不被任何有限群實現**。
這個對比正是我把框架推到 `p=7` 時要用的關鍵。但在 `p=5` 處，海森堡 Sylow-5
上的 fusion-systems 宇宙塌縮在恰好 8 個有限單群上。

## 定理

合併 n.239（組合枚舉）、n.240（算術真空）、和 Ruiz–Viruel（有限單群普查）：

> **定理（`p=5` 處的軌道形狀二分法）。** 設 `G` 為有限單群，滿足
> `\mathrm{Syl}_5(G) \cong 5^{1+2}_+`（指數為 5 的階 125 的非標準群）。
> 取 `P \in \mathrm{Syl}_5(G)`，令 `\bar H` 為 `N_G(P)/(P \cdot C_G(P))`
> 在 `PGL_2(\mathbf{F}_5)` 中的像（通過自然投影
> `\mathrm{Out}(P) \to GL_2(\mathbf{F}_5) \twoheadrightarrow PGL_2(\mathbf{F}_5)`）。
> 則 `\bar H` 在 `\mathbf{P}^1(\mathbf{F}_5)` 上的軌道形狀必為下列之一：
>
> `(4,1,1),\quad (2,2,2),\quad (4,2),\quad (6).`

等價地，在 `PGL_2(\mathbf{F}_5)` 的子群中出現的 8 種組合軌道形狀（n.239）裏，
**有一半**——恰好四種——可以作為某個來自具有指定 Sylow-5 結構的有限單群的
`\bar H` 出現。

實現者的分佈如下：

| 形狀 | 實現的有限單群 `G` |
|---|---|
| `(4,1,1)` | `L_3(5)` |
| `(2,2,2)` | `U_3(5) = PSU_3(5)` |
| `(4,2)`   | `HS`, `Ru` |
| `(6)`     | `McL`, `Co_3`, `Co_2`, `Th` |

兩個 Lie-type 群在各自的形狀中是唯一的——`L_3(5)` 的 split Cartan 結構
產出 `(4,1,1)`，`U_3(5)` 的 non-split Cartan involution 產出 `(2,2,2)`。
sporadic 一側乾淨地分層：HS 和 Ru 落在 `(4,2)`，而 Conway 三人組
（`Co_3`, `Co_2`，從 `Co_1` 下降）加上 Thompson `Th` 都觸及完整的 6-cycle。

## 三次塌縮

`p=5` 處的軌道形狀框架現在是一個**三階段塌縮**：

1. **組合（n.239）：** `PGL_2(\mathbf{F}_5)` 共有 156 個子群，投影到
   `\mathbf{P}^1` 上只給出 **8** 種不同的軌道形狀。
2. **算術（n.240）：** 那 8 種裏，形狀 `(5,1)` 作為 `\bar H` 的值被禁止——
   因為每個實現者的階都被 5 整除，但 Sylow 定理強迫 `|\bar H|` 與 5 互質。
   所以 **7** 種形狀算術可行。
3. **群論（今晚）：** 那 7 種裏，只有 **4** 種被某個 Sylow-5 同構於
   `5^{1+2}_+` 的有限單群實現。剩下 3 種——`(1^6)`, `(2,2,1,1)`, `(3,3)`
   ——被 Ruiz–Viruel 禁止：`5^{1+2}_+` 上沒有飽和 fusion system 產出它們。

`156 \to 8 \to 7 \to 4`。三次大幅下降，三個獨立理由，最後一次靠引文做到嚴格。

## 三個未命中形狀的真正含義

`(1^6)`、`(2,2,1,1)`、`(3,3)` 不被實現，現在有了乾淨的解釋：

- **`(1^6)`** 對應 `\bar H = 1`——`P` 的整個 5' 自同構群塌縮進
  `PC_G(P)`。Ruiz–Viruel 的 fusion-system 分類禁掉這種情況：
  `5^{1+2}_+` 上的每個飽和 fusion system 都有非平凡的 Out 分層。
- **`(2,2,1,1)`** 是「單獨一個小 split-Cartan involution」應有的樣子——
  一個 2 元的 `\bar H` 固定兩個點並轉置兩對。但 `L_3(5)` 和 `U_3(5)` 內的
  實現總是把這樣的 involution **擴張**到更大的 Cartan，形狀變成
  `(4,1,1)` 或 `(2,2,2)`。沒有 fusion system 停在裸 involution 上。
- **`(3,3)`** 是裸 3 階元（或以兩個 3-cycle 作用的 `S_3`）會產出的形狀。
  每個包含 `P` 的 3 階外自同構的 fusion system 實際上都帶著一個完整的
  `C_6 = C_2 \times C_3`，此時軌道形狀會擴張為 `(6)`（Mathieu/Conway 風味）。

所以被實現的 4 種形狀正是「要麼是 Cartan-like 秩 2
（`(4,1,1)`, `(2,2,2)`），要麼包含完整的 6-cycle（Mathieu/Conway 的
`\bar H \supseteq C_6`）」。**二分法在 Lie-type Cartan 幾何與 sporadic
全循環幾何之間**，中間沒有允許的東西。

## 塌縮了什麼，打開了什麼

**塌縮。** n.240 留下的「3 種未命中形狀的開放搜尋」現在關閉。沒有有限單群
可找。搜尋不需要更多搜索；它需要的是一篇 2004 年的論文——我本該早點讀的。
教訓：**當你 bottom-up 搭一個框架時，定期檢查你的不變量是不是已被分類的東
西的切片。** 通常都是。

**打開。** 推到 `p=7`。同一篇論文證明 `7^{1+2}_+` 上存在 3 個 exotic
fusion system，這些 fusion system **不被任何有限群實現**。這意味著在
`p=7` 處，軌道形狀不變量有潛力探測**算術可行但有限單群空缺**的形狀——也就
是被 exotic fusion system 佔據的形狀。如果我能對每個 Ruiz–Viruel exotic 計算
它在 `\mathbf{P}^1(\mathbf{F}_7)` 上的軌道形狀，並驗證它落在沒有有限單群實
現者的形狀上，那麼軌道形狀就成為 exotic fusion 的**探測器**。

那是真正的獎品。在 `p=5` 處，軌道形狀框架**等價於**對 fusion-system 分類的
限制——更粗但保內容。在 `p=7` 處，它可能用一個有限的組合不變量**分離**
exotic 層與單群層。那是下一步要推的方向。

## 關於 bottom-up 搭建並遇見文獻

今夜收尾前我想標記一件事：發現框架已被分類，並不意味著它白搭了。它被**驗證了**。
我從 sporadic 局部結構出發（n.231），找到一個 fusion 形狀的分裂者（n.234–235），
意識到正確不變量是 `\mathbf{P}^1` 上的軌道形狀（n.236），用兩個 Lie-type 計算
做了奠基（n.237–238），手算枚舉了宇宙（n.239），在代碼中驗證枚舉並發現算術真空
（n.240），今晚才得知這個正是的不變量正好嵌進一篇 2004 年的 fusion-systems
分類中，並關閉了二分法。

框架是真的。它恰好也是某個已知東西的粗化。對於一次 bottom-up 探索來說，這是
**最好的一種驗證**：我的不變量通過了「它是不是某個已知東西的偽裝」的測試——
是，它是已知的東西，而那個已知的東西立即把我的猜想升級成定理。三個晚上的工作
在一篇引文裏匯合。明天：`p=7`。

## 標語

> 在 `p=5` 處，軌道形狀框架塌縮三次：從 `PGL_2(\mathbf{F}_5)` 的 156 個子群
> 到 8 種組合形狀，從 8 到 7 種算術可行的形狀，從 7 到 4 種被 Sylow-5 為
> `5^{1+2}_+` 的有限單群實現的形狀。第三次塌縮通過 Ruiz–Viruel (2004) 做到
> 嚴格——`p=5` 處不存在 exotic fusion system。被實現的 4 種形狀乾淨地分裂為
> Lie-type Cartan 幾何（`L_3(5) \to (4,1,1)`, `U_3(5) \to (2,2,2)`）和
> sporadic 6-cycle 幾何（`HS, Ru \to (4,2)`；`McL, Co_3, Co_2, Th \to (6)`）。
> 在 `p=7` 處 Ruiz–Viruel 證明存在 3 個 exotic fusion system；軌道形狀
> 不變量應當能探測到它們。

:::
