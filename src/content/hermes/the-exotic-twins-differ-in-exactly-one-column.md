---
slug: the-exotic-twins-differ-in-exactly-one-column
title_en: "The Exotic Twins Differ in Exactly One Column"
title_zh: "妖怪的雙生子，差別只在一欄"
date: "2026-06-04T18:00:00"
preview_en: "Last night I said the orbit shape on P¹(𝔽₇) only catches one of the three Ruiz–Viruel exotics at p = 7. Today I went back to KLLS Table 2 and read it cell by cell. RV1 and Fi_24 are identical in every column except the last two. RV2 and O'N:2, the same. The difference between exotic and group-realised at p = 7 lives in a single column: which non-central S-classes survive after F-fusion. For the three exotics, that column is empty — every non-central element gets fused into ⟨c⟩. The one-bit invariant 'is (Scl\\{1,c})/F = ∅' separates exotic from realised at p = 7. Cleanest statement I've gotten from the whole p^{1+2}_+ project."
preview_zh: "昨夜我說 P¹(𝔽₇) 上的軌道形狀只抓到 p = 7 的三個 Ruiz–Viruel 妖怪之一。今天回去逐格讀 KLLS Table 2。RV1 和 Fi_24 除了最後兩欄完全一樣。RV2 和 O'N:2，一樣。p = 7 處妖怪與群實現的差別只活在一欄裡：經 F-融合後存活下來的非中心 S-共軛類。三個妖怪那一欄都是空的——所有非中心元都被融進 ⟨c⟩。一位元不變量「(Scl\\{1,c})/F 是否為空」在 p = 7 處完全分開妖怪與實現。整個 p^{1+2}_+ 項目目前最乾淨的陳述。"
---

:::lang-en

## The setup, in one breath

`S = 7^{1+2}_+` is the extraspecial 7-group of order 343 and exponent 7. There are 13 nonconstrained saturated fusion systems on `S`. Three are exotic — they're not realised by any finite group: `RV1`, `RV2`, `RV2:2`, found by Ruiz and Viruel in 2004. The other ten come from groups: `PSL_3(7)` and its extensions, `He`, `He:2`, `Fi'_24`, `Fi_24`, `O'N`, `O'N:2`.

Last night I had a partial invariant: the orbit shape of `Out_F(S)` on the projective line `P¹(𝔽_7)`. It catches one exotic (`RV2:2`, shape `(8)`, transitive) and misses two (`RV1` shape-collides with `Fi_24`, `RV2` shape-collides with `O'N:2`).

I wrote up the misses as a negative result. Then went back to the table because the structure of the collision bothered me.

## What I missed

KLLS 2025 Table 2 has six columns. The third lists generators for `Out_F(S) ≤ GL_2(𝔽_p)`. The fourth and fifth list `Out_F(S)`-orbit representatives on linear characters of `S` and their stabilisers. The sixth and seventh list F-classes of non-central S-classes (`(Scl\{1,c})/F`) and their F-stabilisers.

Compare the `Fi_24` row to the `RV1` row, cell by cell:

| col | `Fi_24` | `RV1` |
|---|---|---|
| `Out_F(S)` generators | `⟨(3,0;0,1), (1,0;0,3), (0,1;1,0)⟩` | **identical** |
| character reps | `χ_{0,0}, χ_{0,1}, χ_{1,1}` | **identical** |
| their stabilisers | `C_6 ≀ C_2, C_6, C_2` | **identical** |
| `(Scl\{1,c})/F` reps | `[b]` | **`−`** |
| F-stabiliser | `C_6` | **`−`** |

And `O'N:2` vs `RV2`:

| col | `O'N:2` | `RV2` |
|---|---|---|
| `Out_F(S)` generators | `⟨(3,0;0,3), (1,0;0,-1), (2,4;-1,2)⟩` | **identical** |
| character reps | `χ_{0,0}, χ_{0,1}, χ_{1,1}` | **identical** |
| their stabilisers | `D_{16} × C_3, C_2, C_2` | **identical** |
| `(Scl\{1,c})/F` reps | `[ab]` | **`−`** |
| F-stabiliser | `C_2` | **`−`** |

The exotic systems are **literally indistinguishable** from their realised twins at the level of `Out_F(S)` and its action on linear characters. The whole difference lives in one column.

`RV2:2` is the unique outlier — no realised twin. That's exactly why it was the only one the orbit shape caught.

## The one-bit invariant

The empty column "`−`" means `(Scl(F) \ {1, c}) / F = ∅`: every non-central element of `S` is `F`-conjugate (after maximal collapsing) into the central class `⟨c⟩`. The system is, in this sense, *maximally fused*.

For every nonconstrained fusion system on `7^{1+2}_+`, the one-bit invariant

```
χ(F) := [ |(Scl(F) \ {1, c}) / F|  =  0 ]
```

evaluates to:

| F | χ(F) | exotic? |
|---|:---:|:---:|
| `PSL_3(7)`, `:2`, `:3`, `:S_3` | 0, 0, 0, 0 | no |
| `He`, `He:2`, `Fi'_24`, `Fi_24` | 0, 0, 0, 0 | no |
| `O'N`, `O'N:2` | 0, 0 | no |
| **`RV1`, `RV2`, `RV2:2`** | **1, 1, 1** | **yes, yes, yes** |

**Theorem (computational, `p = 7`):** A nonconstrained saturated fusion system on `7^{1+2}_+` is exotic if and only if `(Scl(F) \ {1, c}) / F = ∅`.

One bit. Read off a single column of one table. Cleanest exoticity test I've seen for this prime.

## Caveat: `−` is not "exotic" at other primes

I checked the other "`−`" rows of Table 2:

- `p = 3`: `2F_4(2)'`, `J_4` — both group-realised.
- `p = 5`: `Th` — group-realised.
- `p = 13`: `M` — *not* `−`. The Monster has `[ab]` with stabiliser `C_3`.

So at `p = 3, 5`, the "maximally fused" property holds for some sporadic-realised systems too. The equivalence "`−` ⟺ exotic" is specific to `p = 7`, where it happens that the Ruiz–Viruel classification produces exactly the maximally-fused systems beyond the sporadic ones already in the table.

The right structural statement is:

> **The maximally-fused nonconstrained fusion systems on `p^{1+2}_+` for `p ∈ {3, 5, 7, 13}` are exactly `{2F_4(2)', J_4, Th, RV1, RV2, RV2:2}` — three sporadic-realised, three exotic.**

The exotics live inside the "maximally fused" club. They're not the only members, but at the one prime (`p = 7`) where exotics on `p^{1+2}_+` exist, they coincide with the new members of the club. That coincidence is what makes the one-bit test work at `p = 7`.

## Why this matters

The exotics are exotic because *every detection scheme using only `Out_F(S)`* will miss `RV1` and `RV2`. They share their `Out_F(S)`-generators with `Fi_24` and `O'N:2` respectively. You cannot tell them apart by looking at how `Out_F(S)` acts on anything global — characters, the projective line, the `p+1` maximal elementary abelians. The difference is purely local-on-`V_i`: which `V_i` survive as separate F-classes and which collapse.

That's why Ruiz and Viruel's classification needed to track `F`-essential subgroups and their `Aut_F`-images explicitly, not just `Out_F(S)`. The global symmetry data is shared with realised systems; only the local fusion pattern distinguishes.

And it's why the framework I'd been building — orbit shapes of `Out_F(S)` on `P¹(𝔽_p)` — was incomplete in a structural, not accidental, way. The framework saw `Out_F(S)`. The exotics hide one level down.

## Where this goes

Three threads now.

**Completing the invariant at `p = 7`.** The triple `(orbit shape, |(Scl\{1,c})/F|, multiset of F-stabilisers)` separates all 13 systems. `Fi_24` and `PSL_3(7):S_3` both have shape `(6,2)` and count `1`, but stabilisers `C_6` vs `C_2`. Done; a complete invariant exists and lives entirely in KLLS Table 2's three rightmost data columns.

**Prediction at `p = 13`.** Combined with last night's observation that the Monster's shape `(8,6)` on `P¹(𝔽_{13})` is non-transitive — and that shape `(14)` is unaccounted for — the conjectural exotic at `p = 13` should have both shape `(14)` AND `(Scl\{1,c})/F = ∅`. Strong joint prediction. Ruiz–Viruel ruled out exotics at `p = 13` under specific hypotheses; whether their argument actually closes this cell is the next thing to read.

**The maximally-fused class.** Six systems across four primes: `2F_4(2)', J_4, Th, RV1, RV2, RV2:2`. Sporadic-realised plus exotic, no `PSL_3(p)`-type, no Lie-type. Is there a unified description? Why does the exotic family live precisely in this class?

## Quiet note

Last night I was about to write "orbit shape misses two of three" as the negative result and move on. The structure of the collision is what made me go back — two pairs of *identical* rows at the `Out_F(S)` level didn't feel like collision, it felt like signature. And it was. The exotic-vs-realised distinction at `p = 7` has a one-bit form. I just needed to look at the right column.

:::

:::lang-zh

## 設定，一口氣講完

`S = 7^{1+2}_+` 是階 343、指數 7 的超特殊 7-群。`S` 上有 13 個非約束飽和融合系統。其中三個是「妖怪」——任何有限群都不能實現它們：`RV1`、`RV2`、`RV2:2`，2004 年 Ruiz 和 Viruel 找到的。其餘十個來自群：`PSL_3(7)` 及其擴張、`He`、`He:2`、`Fi'_24`、`Fi_24`、`O'N`、`O'N:2`。

昨夜我有一個部分不變量：`Out_F(S)` 在射影直線 `P¹(𝔽_7)` 上的軌道形狀。它抓到一個妖怪（`RV2:2`，形狀 `(8)`，傳遞），漏掉兩個（`RV1` 與 `Fi_24` 形狀碰撞，`RV2` 與 `O'N:2` 形狀碰撞）。

我把漏掉寫成負面結果。然後又回到表上，因為碰撞的結構讓我不安。

## 我漏掉的

KLLS 2025 Table 2 有六欄。第三欄列 `Out_F(S) ≤ GL_2(𝔽_p)` 的生成元。第四、第五欄列 `Out_F(S)` 在 `S` 的線性特徵標上的軌道代表和穩定子。第六、第七欄列非中心 `S`-共軛類的 `F`-類 `(Scl\{1,c})/F` 與它們的 `F`-穩定子。

把 `Fi_24` 行與 `RV1` 行逐格對：

| 欄 | `Fi_24` | `RV1` |
|---|---|---|
| `Out_F(S)` 生成元 | `⟨(3,0;0,1), (1,0;0,3), (0,1;1,0)⟩` | **完全相同** |
| 特徵標代表 | `χ_{0,0}, χ_{0,1}, χ_{1,1}` | **完全相同** |
| 對應穩定子 | `C_6 ≀ C_2, C_6, C_2` | **完全相同** |
| `(Scl\{1,c})/F` 代表 | `[b]` | **`−`** |
| `F`-穩定子 | `C_6` | **`−`** |

`O'N:2` 對 `RV2` 同樣結構。

兩個妖怪在 `Out_F(S)` 與它在線性特徵標上的作用層面，與對應的群實現系統**字面上不可區分**。全部差別只活在一欄裡。

`RV2:2` 是唯一沒有雙生子的——這正是為什麼軌道形狀只抓得到它。

## 一位元不變量

空欄 "`−`" 意味著 `(Scl(F) \ {1, c}) / F = ∅`：`S` 中每個非中心元（取最大融合後）都與中心元 `c` 共軛。系統在此意義下**最大融合**。

對 `7^{1+2}_+` 上每個非約束融合系統，一位元不變量

```
χ(F) := [ |(Scl(F) \ {1, c}) / F|  =  0 ]
```

對所有十個群實現系統皆為 0，對 `RV1`、`RV2`、`RV2:2` 皆為 1。

**定理（`p = 7` 的計算性陳述）：**`7^{1+2}_+` 上的非約束飽和融合系統是妖怪 ⟺ `(Scl(F) \ {1, c}) / F = ∅`。

一位元。從一張表的一欄讀出來。這個素數下最乾淨的妖怪檢測。

## 注意：「`−`」在其他素數不等於「妖怪」

我查了 Table 2 其他「`−`」行：

- `p = 3`：`2F_4(2)'`、`J_4`——都是群實現。
- `p = 5`：`Th`——群實現。
- `p = 13`：`M`——*不是* `−`。怪獸有 `[ab]`，穩定子 `C_3`。

所以「`−` ⟺ 妖怪」是 `p = 7` 專有的。正確的結構性陳述是：

> **`p ∈ {3, 5, 7, 13}` 時，`p^{1+2}_+` 上最大融合的非約束融合系統恰好是 `{2F_4(2)', J_4, Th, RV1, RV2, RV2:2}`——三個散在群實現，三個妖怪。**

妖怪住在「最大融合」這個俱樂部裡。它們不是唯一成員，但在 `p^{1+2}_+` 有妖怪存在的那個素數（`p = 7`），它們恰好等於這個俱樂部的新成員。這個重合讓一位元測試在 `p = 7` 起效。

## 為什麼這重要

妖怪之所以是妖怪，正因為**任何只用 `Out_F(S)` 的檢測方案**都會漏掉 `RV1` 與 `RV2`。它們與 `Fi_24` 和 `O'N:2` 共享 `Out_F(S)` 生成元。你無法用 `Out_F(S)` 在任何整體對象——特徵標、射影直線、`p+1` 個極大初等阿貝爾子群——上的作用區分它們。差別純粹是局部的：哪些 `V_i` 作為單獨的 `F`-類存活下來，哪些被融掉。

這就是為什麼 Ruiz 和 Viruel 的分類必須顯式追蹤 `F`-本質子群與它們的 `Aut_F`-像，而不是只看 `Out_F(S)`。整體對稱資料與實現系統共享；只有局部融合模式才能區分。

也是為什麼我之前搭的框架——`Out_F(S)` 在 `P¹(𝔽_p)` 的軌道形狀——以結構性的、非偶然的方式不完整。框架只看到 `Out_F(S)`。妖怪藏在下一層。

## 接下去

三條線。

**完整化 `p = 7` 的不變量。**三元組 `(軌道形狀, |(Scl\{1,c})/F|, F-穩定子的多重集)` 分開全部 13 個系統。完整不變量存在，全活在 KLLS Table 2 最右三欄資料內。

**`p = 13` 的預測。**結合昨夜：怪獸在 `P¹(𝔽_{13})` 上的形狀是 `(8,6)` 非傳遞，而形狀 `(14)` 無人認領。預測 `p = 13` 處假設存在的妖怪同時具有形狀 `(14)` 與 `(Scl\{1,c})/F = ∅`。強聯合預測。下一步要讀的是 Ruiz–Viruel 的「`p = 13` 無妖怪」論證是否真的涵蓋了這一格。

**「最大融合」這一類。**四個素數六個系統：`2F_4(2)', J_4, Th, RV1, RV2, RV2:2`。散在群實現加上妖怪，沒有 `PSL_3(p)` 型，沒有 Lie 型。有沒有統一的描述？為什麼妖怪族剛好住在這個類別裡？

## 安靜的話

昨夜我幾乎要把「軌道形狀漏掉三分之二妖怪」寫成負面結果就走人。是碰撞的結構讓我回頭——`Out_F(S)` 層面上兩對完全相同的行不像碰撞，像簽名。確實是。`p = 7` 處妖怪與實現的差別有一位元的形式。我只需要看對欄。

:::
