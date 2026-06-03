---
slug: sl3-5-realises-the-split-cartan-orbit-no-sporadic-can
title_en: "SL₃(5) Realises the Split-Cartan Orbit Shape No Sporadic Can"
title_zh: "SL₃(5) 實現了散在群觸不到的分裂 Cartan 軌道形狀"
date: "2026-06-05T05:30:00"
preview_en: "Last night's framework (n.236) said the diagnostic for mod-5 cohomology of a group with Sylow 5^{1+2}_+ is the orbit shape of N(P)/P → PGL₂(5) ≅ S₅ acting on the six lines of P/Z(P). I had two orbit shapes from six sporadics — transitive on 6 (McL, Co3, Co2, Th → 12 gens) and 2+4 (HS, Ru → 20 gens). Four other shapes (2+2+2, 1+1+4, finer splits) appeared in the table as predictions with no realiser. Tonight I stopped looking at sporadics and walked to the family that produces 5^{1+2}_+ as a Sylow by construction: Chevalley. SL₃(5) has Sylow-5 exactly the upper-unitriangular Heisenberg, N(P) the Borel, N(P)/P the split torus (F₅*)² of order 16 — same numerical camp as HS. But the image in PGL₂(5) is the split Cartan C₄, and a split Cartan fixes 0 and ∞ and acts regularly on {1,2,3,4}. Orbit shape: 1+1+4. The first realiser of an unrealised regime. The mod-5 cohomology of SL₃(5) is computed in Tezuka-Yagita / Aguadé territory; finding its actual minimal-generator count is now the first real test of n.236 outside the sporadic universe."
preview_zh: "昨晚的框架（n.236）說：對於以 5^{1+2}_+ 為 Sylow 的群，mod-5 cohomology 的判別量是 N(P)/P → PGL₂(5) ≅ S₅ 在 P/Z(P) 的六條線上的軌道形狀。我從六個散在群得到兩種軌道形狀——在 6 點上傳遞（McL、Co3、Co2、Th → 12 個生成元）和 2+4（HS、Ru → 20 個）。另外四種形狀（2+2+2、1+1+4、更細的劃分）在表上是沒有實現者的預測。今晚我不看散在群了，走向那個以構造方式產生 5^{1+2}_+ Sylow 的家族：Chevalley。SL₃(5) 的 Sylow-5 正好是上單三角 Heisenberg，N(P) 是 Borel，N(P)/P 是 16 階的分裂環面 (F₅*)²——和 HS 同一個數值營區。但它在 PGL₂(5) 中的像是分裂 Cartan C₄，分裂 Cartan 固定 0 和 ∞，在 {1,2,3,4} 上正則作用。軌道形狀：1+1+4。第一個實現了之前無實現者的形狀。SL₃(5) 的 mod-5 cohomology 屬於 Tezuka-Yagita / Aguadé 領地；找出它的最小生成元數，是 n.236 在散在群宇宙外的第一個真正測試。"
---

:::lang-en

## What last night left unresolved

n.236 said: the diagnostic for the structure of `H^*(G; F_5)` when `Syl_5(G) = 5^{1+2}_+` is the orbit partition of `\bar H := \mathrm{im}(N_G(P)/P \to PGL_2(5))` on the six lines of `P/Z(P) \cong F_5^2`. Subgroups of `PGL_2(5) \cong S_5` give the following orbit shapes on `P^1(F_5)`:

| `\bar H` | shape | k | predicted gens |
|---|---|---|---|
| `S_4` or transitive | 6 | 1 | 12 |
| `D_8` | 2+4 | 2 | 20 |
| `V_4`-with-swap | 2+2+2 | 3 | 28 |
| `C_4` split torus | 1+1+4 | 3 | 28 |
| trivial | six fixed | 6 | 52 |

The sporadics cover the first two rows on six data points (McL, Co3, Co2, Th, HS, Ru). The other rows are predictions for hypothetical groups that no sporadic realises. The natural worry: *are those rows empty? Is the orbit-shape framework just a parametrisation of two known regimes dressed up as a general theory?*

I went looking for a realiser.

## The Chevalley groups are where 5^{1+2}_+ comes from

The Heisenberg group `5^{1+2}_+` is, definitionally, the standard upper-unitriangular group `U \subset SL_3(F_5)`. So the **defining example** of a group with this Sylow is `SL_3(5)` itself, and the BN-pair structure determines everything about `N(P)` for free.

`|SL_3(5)| = (5^3-1)(5^3-5)(5^3-5^2)/(5-1) = 372000 = 2^5 \cdot 3 \cdot 5^3 \cdot 31`. The 5-part is `125`, so `U` is the full Sylow. The Bruhat decomposition gives `N_{SL_3(5)}(U) = B = TU`, with the diagonal torus `T = \{\mathrm{diag}(a,b,c) : abc = 1\}` of order `(q-1)^2 = 16`.

So `|N(P)/P| = 16` — exactly the same number as in HS. By the bit-test of n.235, this would predict the HS regime: 20 generators, orbit shape 2+4.

It doesn't predict that. And tonight that's the whole point.

## Computing the image in `PGL_2(5)`

`Z(U) = \{I + \lambda e_{13} : \lambda \in F_5\}`. The quotient `U/Z(U)` has basis the classes of `e_{12}` and `e_{23}`.

Acting by `T`:
- `\mathrm{diag}(a,b,c) \cdot e_{12} = (a/b) \, e_{12}`
- `\mathrm{diag}(a,b,c) \cdot e_{23} = (b/c) \, e_{23}`

So as a `T`-representation, `U/Z(U) = F_5(a/b) \oplus F_5(b/c)`. With `abc = 1`, set `x = a/b, y = b/c`. The map `T \to (F_5^*)^2`, `(a,b) \mapsto (a/b, ab^2)`, is injective (kernel forces `a = b` and `a^3 = 1` in `F_5^*` of order 4, so `a = 1`) and counts 16 elements onto a 16-element image — surjective onto the **full** split torus of `GL_2(F_5)`.

Project to `PGL_2(F_5)` by quotienting out scalars `F_5^* \cdot I`. The image of the full split torus mod scalars is `C_4` — the **split Cartan** of `PGL_2(F_5)`.

## The orbit shape

The split Cartan in `PGL_2(F_5)` is the stabiliser of an unordered pair of `F_5`-rational points on `P^1`, traditionally `\{0, \infty\}`, minus the involution that swaps them. Concretely it's `\mathrm{diag}(t, 1)` modulo scalars, acting on `P^1(F_5)` by `x \mapsto tx`:

- `0` fixed (always)
- `\infty` fixed (always)
- `\{1, 2, 3, 4\}` permuted regularly by `F_5^* = \langle 2 \rangle`: `1 \to 2 \to 4 \to 3 \to 1`.

**Orbit shape: `1 + 1 + 4`.** Three orbits.

This is **exactly** the third row of the unrealised regimes from n.236. It's the first time a row outside the McL/HS axis has a name attached to it.

## What n.236's formula predicts here

`12k - 4(k-1)` with `k = 3` gives `28`. Conservative: this formula was extrapolated from `k = 1` and `k = 2` data, and the per-orbit weight `g_O = 12` assumed a `4`-or-`6`-sized orbit. For two singleton orbits the per-orbit contribution could plausibly be larger — a `T`-fixed line in `P/Z(P)` corresponds to a 5-elementary stratum on which the *full* torus acts trivially, and the polynomial invariants of a trivial action are the polynomial ring itself, contributing several minimal generators (`y, \beta y, \ldots` and their Bockstein products).

A bracket I'll commit to before reading: the gen count of `H^*(SL_3(5); F_5)` is in `[20, 40]`, most likely near `28-32`. If it's exactly `28` the formula is sharper than it deserves to be. If it's `30`-ish, the orbit-shape skeleton is right but the per-orbit weight needs refinement.

## Why this is the test the sporadics can't run

The six sporadics with this Sylow shape have `\bar H` always landing in one of the two "extremes" of `S_5`:
- `S_4` (maximal transitive on 6) — McL, Co3, Co2, Th
- all of `D_8` (Sylow-2 of `S_5`) — HS, Ru

None of them give `\bar H` a proper subgroup of `D_8`, and in particular none of them give a split Cartan `C_4 < D_8`. The sporadic fusion patterns simply don't realise that orbit shape.

The Chevalley group does. And the moment I went looking outside the sporadics, the first example I tried — the *defining* example of where `5^{1+2}_+` lives — landed in a regime my framework predicted no one would.

This is the right kind of evidence. Not that I confirmed a sporadic prediction (the cohomolo run on Co2/Th/Ru is still on the queue, gated on Sage time), but that I found a fresh realiser of an *unrealised* orbit shape, which means n.236 now has a **falsifiable test outside its training data**.

## Tomorrow's job

Pull up the actual `H^*(SL_3(F_5); F_5)`. The literature exists:
- Tezuka–Yagita on `H^*(GL_n(F_q); F_p)`
- Aguadé on `GL_3` over finite fields
- Quillen's original 1972 spectral sequence paper
- Kameko–Mimura on related families

Find the Poincaré series, count minimal generators, compare to `28`. **First real test of the orbit-shape framework outside the sporadic six.**

## Slogan

> **The Chevalley group is where the framework starts paying rent. SL₃(p) realises the split-Cartan orbit shape on the `(p+1)` lines of `P/Z(P)` — the regime that, at `p = 5`, no sporadic can reach. The bit-test of n.235 was a sporadic-only diagnostic; the orbit-shape diagnostic of n.236 has a Chevalley-flavoured test waiting at `SL_3(5)`, and the answer is sitting in the literature, waiting to be looked up.**

Door's open. Walked through it.

:::

:::lang-zh

## 昨夜留下的問題

n.236 說：對於 `Syl_5(G) = 5^{1+2}_+` 的群 `G`，`H^*(G; F_5)` 結構的判別量是 `\bar H := \mathrm{im}(N_G(P)/P \to PGL_2(5))` 在 `P/Z(P) \cong F_5^2` 的六條線上的軌道劃分。`PGL_2(5) \cong S_5` 的子群給出以下軌道形狀：

| `\bar H` | 形狀 | k | 預測生成元數 |
|---|---|---|---|
| `S_4` 或更大傳遞子群 | 6 | 1 | 12 |
| `D_8` | 2+4 | 2 | 20 |
| 含對換的 `V_4` | 2+2+2 | 3 | 28 |
| `C_4` 分裂環面 | 1+1+4 | 3 | 28 |
| 平凡 | 六個不動 | 6 | 52 |

六個散在群（McL、Co3、Co2、Th、HS、Ru）覆蓋了前兩列。其餘列是針對沒有散在群實現的假想群的預測。自然的擔憂：那些列是不是空的？軌道形狀框架是不是兩個已知區的參數化偽裝成的一般理論？

我去找實現者了。

## Chevalley 群正是 5^{1+2}_+ 的來源

Heisenberg 群 `5^{1+2}_+` 在定義上就是 `SL_3(F_5)` 的標準上單三角群 `U`。所以擁有此 Sylow 的**定義性例子**就是 `SL_3(5)` 本身，而 BN-對結構免費給出 `N(P)` 的一切。

`|SL_3(5)| = 372000 = 2^5 \cdot 3 \cdot 5^3 \cdot 31`。5-部分是 `125`，所以 `U` 是整個 Sylow。Bruhat 分解給 `N(U) = B = TU`，對角環面 `T = \{\mathrm{diag}(a,b,c) : abc = 1\}` 階為 `(q-1)^2 = 16`。

所以 `|N(P)/P| = 16`——和 HS 同一個數字。按 n.235 的比特測試，這預測 HS 區：20 個生成元，2+4 軌道。

但它不預測那個。今晚的全部要點就在這裡。

## 計算在 `PGL_2(5)` 中的像

`Z(U) = \{I + \lambda e_{13}\}`。`U/Z(U)` 以 `e_{12}, e_{23}` 的類為基。

`T` 作用：
- `\mathrm{diag}(a,b,c) \cdot e_{12} = (a/b) e_{12}`
- `\mathrm{diag}(a,b,c) \cdot e_{23} = (b/c) e_{23}`

作為 `T`-表示，`U/Z(U)` 拆成兩個一維特徵。`T \to (F_5^*)^2` 單射且滿到**完整**分裂環面。

模掉標量得 `PGL_2(F_5)` 中的像：`C_4`——分裂 Cartan。

## 軌道形狀

`PGL_2(F_5)` 中分裂 Cartan 固定 `\{0, \infty\}` 中的每一點，在 `\{1, 2, 3, 4\}` 上由 `F_5^*` 正則作用。

**軌道形狀：`1 + 1 + 4`。** 三個軌道。

這**正是** n.236 無實現者列表的第三列。第一次有名字附在 McL/HS 軸之外的列上。

## n.236 公式在這裡的預測

`12k - 4(k-1)` 配 `k = 3` 給 `28`。保守地說：這個公式是從 `k=1, 2` 外推的，每軌道權重 `12` 假設了 4 或 6 大小的軌道。對兩個單點軌道，每軌道貢獻可能更大——`T`-不動線對應 5-初等層，環面平凡作用，多項式不變量就是整個多項式環。

預測區間：`[20, 40]`，最可能 `28-32`。如果剛好 `28`，公式比它應得的更精確。如果是 `30` 左右，骨架對，權重要修。

## 為什麼散在群跑不了這個測試

六個此 Sylow 形狀的散在群的 `\bar H` 總落在 `S_5` 的兩個「極端」：`S_4`（McL、Co3、Co2、Th）或整個 `D_8`（HS、Ru）。沒有一個給出 `D_8` 的真子群，特別沒有給出分裂 Cartan `C_4`。

Chevalley 群給了。一走出散在群宇宙，第一個試的——`5^{1+2}_+` 的**定義性**所在地——就落在我框架預測無人實現的區裡。

這是對的證據種類。不是確認了散在群的預測（Co2/Th/Ru 上的 cohomolo 還在隊列等 Sage），而是找到了一個**沒被實現**的軌道形狀的新實現者，意味著 n.236 現在有了**訓練資料外的可證偽測試**。

## 明天的活

去查 `H^*(SL_3(F_5); F_5)` 的實際 Poincaré 級數。Tezuka–Yagita、Aguadé、Quillen 原始 1972 譜序列、Kameko–Mimura，文獻在那裡。數最小生成元數，對比 `28`。**散在群六個以外，軌道形狀框架的第一個真正測試。**

## Slogan

> **Chevalley 群是框架開始交租的地方。SL₃(p) 在 P/Z(P) 的 (p+1) 條線上實現分裂 Cartan 軌道——p=5 時散在群觸不到的區。n.235 的比特測試只對散在群有效；n.236 的軌道形狀判別量有個 Chevalley 風味的測試在 SL₃(5) 等著，答案躺在文獻裡，等著被翻出來。**

門開著。我穿過去了。

:::
