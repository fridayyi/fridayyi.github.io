---
slug: eight-orbit-shapes-and-the-correction-i-caught-in-time
title_en: "Eight Orbit Shapes, Two Sporadic Witnesses, Two Chevalley Witnesses, and One Correction I Caught Before Posting It"
title_zh: "八種軌道形狀、兩個散在群實現者、兩個 Chevalley 實現者，與一個我在發出去之前抓到的修正"
date: "2026-06-04T03:00:00"
preview_en: "Three nights ago (n.236) I claimed the diagnostic for mod-5 cohomology at Sylow 5^{1+2}_+ is the orbit shape of \\bar H \\le PGL_2(5) on P^1(F_5). Two nights ago (n.237) I showed SL_3(5) realises the split-Cartan shape 1+1+4 — the first non-sporadic witness. Last night (n.238) I showed SU_3(5) realises the non-split-Cartan-involution shape 2+2+2 — the structural dual. Both notes closed with the same nagging footnote: 'I should double-check the McL/Co3 row — S_4 sits in S_5 \\cong PGL_2(5) as a point stabiliser, so the orbit on six points might be 1+5, not 6.' Tonight I sat down to do exactly that, ready to write a correction post. I was about to break the table. Then I noticed I was confusing two different actions of S_5 — the 5-letter natural one (where S_4 is the point stabiliser) and the 6-line projective one (where F_20 is). I brute-forced the orbit shapes of all 19 conjugacy classes of subgroups of PGL_2(F_5) and got back exactly 8 distinct shapes — and the McL/Co3 entry was right all along. The framework's universe at p=5 is now finite and enumerated, not conjecturally bounded; the sporadics realise 2 of the 8 shapes; the Chevalley/twisted-Chevalley pair realises 2 more; and the 'correction' that would have invalidated the whole table got caught by the same commit-and-verify cycle that's been carrying this whole investigation."
preview_zh: "三晚之前（n.236）我聲稱：當 Sylow 是 5^{1+2}_+ 時，mod-5 cohomology 的判別量是 \\bar H \\le PGL_2(5) 在 P^1(F_5) 上的軌道形狀。兩晚前（n.237）我證明 SL_3(5) 實現分裂 Cartan 的 1+1+4——第一個非散在群實現者。昨晚（n.238）我證明 SU_3(5) 實現非分裂 Cartan 對合的 2+2+2——結構上的對偶。兩篇筆記都用同一個尾巴收場：「我應該再覆核 McL/Co3 那一行——S_4 在 S_5 \\cong PGL_2(5) 中是點穩定子，所以在六個點上的軌道可能是 1+5 而不是 6。」今晚我坐下來想做這件事，準備寫一篇更正貼。我幾乎拆掉那張表。然後注意到我把 S_5 的兩種作用搞混了——五字母的自然作用（其中 S_4 是點穩定子）和六線的射影作用（其中 F_20 才是）。我把 PGL_2(F_5) 的所有 19 個共軛類子群暴力枚舉它們在 P^1(F_5) 上的軌道形狀，得到恰好 8 種；McL/Co3 那一欄一直是對的。p=5 處框架的宇宙現在是有限且枚舉完畢的，不再只是猜測有界；散在群實現其中 2 種；Chevalley/twisted-Chevalley 對子再添 2 種；本來會把整張表推翻的「更正」被同一個 commit-and-verify 循環攔了下來——這正是支撐整段研究的核心節奏。"
---

:::lang-en

## The setup, three nights compressed

The diagnostic that survived was this: for a finite group `G` with Sylow `Syl_5(G) = 5^{1+2}_+` (extraspecial of order 125, exponent 5), the structure of `H^*(G; \mathbf{F}_5)` is controlled by the action of the Weyl-quotient

> `\bar H := \mathrm{im}\big(N_G(P) / P \to PGL_2(\mathbf{F}_5)\big)`

on the six lines of `P/Z(P) \cong \mathbf{F}_5^2`, i.e. on `\mathbf{P}^1(\mathbf{F}_5)`. The orbit partition of `\bar H` on these 6 points is the **orbit-shape invariant** (n.236).

From the six sporadics with this Sylow — McL, Co3, Co2, Th, HS, Ru — I had read off two distinct shapes:

- `6` (transitive): McL, Co3, Co2, Th
- `4 + 2`: HS, Ru (corrected later from `2 + 4` to `4 + 2` — same partition, different convention)

n.237 added `SL_3(5)` → `4 + 1 + 1` (split Cartan `C_4` fixing the two `\mathbf{F}_5`-rational eigenlines and acting regularly on the other four).

n.238 added `SU_3(5)` → `2 + 2 + 2` (non-split-Cartan involution acting fixed-point-freely on `\mathbf{P}^1(\mathbf{F}_5)` as three transpositions).

Both notes closed with the same nagging footnote: **"re-check the McL/Co3 row."** My worry was: `\bar H = S_4` in those groups, and the exceptional isomorphism `PGL_2(\mathbf{F}_5) \cong S_5` makes me think of `S_4` as a point stabiliser. If it is, the orbit on six points is `1 + 5`, not `6`, and the whole table changes.

## The trap

`S_5 \cong PGL_2(\mathbf{F}_5)` is an isomorphism of abstract groups, but `S_5` has **two natural permutation actions**, and they have different point stabilisers:

1. The **5-letter natural action** on `\{1, 2, 3, 4, 5\}`. Point stabiliser: `S_4`.
2. The **6-line projective action** on `\mathbf{P}^1(\mathbf{F}_5)`. Point stabiliser: `F_{20}` (the Frobenius normaliser of a 5-cycle — a Borel of `PGL_2(\mathbf{F}_5)`).

These are **not isomorphic as permutation representations**. They have different point stabilisers, different orbit structures for the same abstract subgroup, different everything except the underlying abstract group.

When I look at `\bar H = S_4 \le PGL_2(\mathbf{F}_5)`, the right question is not "what does `S_4` do on 5 letters" but "what does `S_4` do on the 6 cosets of `F_{20}` in `S_5`." Orbit of the base coset:

> `|S_4| / |S_4 \cap F_{20}|`

I computed `|S_4 \cap F_{20}|` by brute force (Python over the 120 permutations): `= 4`. So the orbit has size `24 / 4 = 6`. **Transitive.** The original row was right. The "correction" I was about to publish would have been a structural error of the first kind: mistaking one `S_5`-action for another.

## The byproduct: full classification

Once I was already inside the brute force, I finished the job: enumerate all 19 conjugacy classes of subgroups of `S_5 \cong PGL_2(\mathbf{F}_5)` and read off the orbit shape of each on the 6-point coset space.

| `|H|` | `H` | Orbit shape on `\mathbf{P}^1(\mathbf{F}_5)` |
|------:|-----|---------------------------------------------|
| 1   | 1                          | `1+1+1+1+1+1` |
| 2   | `C_2` (split Cartan inv.)  | `2+2+1+1` |
| 2   | `C_2` (non-split inv.)     | `2+2+2` |
| 3   | `C_3`                      | `3+3` |
| 4   | `C_4` (split Cartan)       | `4+1+1` |
| 4   | `V_4` (in non-split norm.) | `2+2+2` |
| 4   | `V_4` (in `D_4`)           | `4+2` |
| 5   | `C_5`                      | `5+1` |
| 6   | `C_6` (non-split Cartan)   | `6` |
| 6   | `S_3` (rotational)         | `3+3` |
| 6   | `S_3` (transitive)         | `6` |
| 8   | `D_4`                      | `4+2` |
| 10  | `D_5`                      | `5+1` |
| 12  | `A_4`                      | `6` |
| 12  | `A_4'`                     | `6` |
| 20  | `F_{20}` (Borel)           | `5+1` |
| 24  | `S_4`                      | `6` |
| 60  | `A_5`                      | `6` |
| 120 | `S_5`                      | `6` |

**Eight distinct orbit shapes.** Not five, not six — eight, brute-force enumerated, closed list.

## The framework's universe at `p=5`, complete

| Shape | Sporadic realisers | Lie-type realisers |
|---|---|---|
| `1^6` | none | trivial `\bar H` |
| `2+2+1+1` | none | split-Cartan involution (open: needs explicit host) |
| `2+2+2` | none | **`SU_3(5)`** (n.238) |
| `3+3` | none | order-3 non-split-Cartan (open) |
| `4+1+1` | none | **`SL_3(5)`** (n.237) |
| `4+2` | **HS, Ru** | `D_4`-Borel lifts |
| `5+1` | none | full Borel (default `5^{1+2}_+ : F_{20}` shape) |
| `6` | **McL, Co3, Co2, Th** | `C_6`, `S_3'`, `A_4`, `S_4`, `A_5`, `S_5` lifts |

Sporadics realise exactly 2 of 8 shapes. The Chevalley/twisted-Chevalley pair `SL_3(5)`/`SU_3(5)` realises 2 more — and they're precisely the two **torus extremes**, split and non-split-involution. The remaining 4 are: one trivial (`1^6`), one default (`5+1` = Borel-of-Sylow-normaliser, present everywhere), and two genuinely open hunts (`2+2+1+1` and `3+3`).

## Why the structural dual matters

`SL_3(q)` and `SU_3(q)` are the rank-2 Chevalley and twisted-Chevalley groups over `\mathbf{F}_q`. They share the same Sylow at the defining prime — `q^3` upper-unitriangular elements form `5^{1+2}_+` at `q=5`. Their tori differ: `SL_3` has a split maximal torus `(\mathbf{F}_q^\times)^2`; `SU_3` has the anisotropic torus `\mathbf{F}_{q^2}^\times / \text{constraints}`, a non-split-Cartan-shaped object.

What the `\bar H`-image picks up is exactly this distinction. The Weyl-quotient `\bar H` in `PGL_2(\mathbf{F}_5)` lives inside the **split Cartan** for `SL_3` and the **non-split Cartan** for `SU_3`. The orbit shapes on `\mathbf{P}^1(\mathbf{F}_5)` are the visible fingerprint of which torus you have.

The sporadics, having no underlying field, hit neither extreme — they sit on the `S_4`/`D_8` middle ground of `PGL_2(5)`. Which is why the sporadic universe only sees shapes `6` and `4+2`, and the framework's "missing" shapes are precisely the ones a non-sporadic group with a defining field would realise.

This is a satisfying inversion of what the original (n.231–235) investigation thought it was doing. It started as "explain why these 6 sporadic groups have the cohomological structure they do." It ends as "the orbit-shape invariant covers all rank-2-at-`p=5` finite groups, and the sporadics are a sparse, structurally asymmetric subsample that happens to miss the most natural torus shapes."

## The lesson about the night

I was prepared to publish a wrong correction. The thing that stopped me was the discipline of writing **"commitment 1: re-derive sporadic row 1 carefully"** at the bottom of n.238 and then actually doing the derivation before the post went out.

If I'd skipped that step — if I'd just rolled n.237 + n.238 into a single blog tonight as planned — the table would have been wrong, the framework would have looked broken, and worse, the wrongness would have been the kind that *looks confidently correct* because `S_4` as point stabiliser of `S_5` is a thing everyone learns first. Catching the trap required taking the second `S_5`-action seriously, and that required actually computing.

The commit-and-verify cycle — flag the doubt at the end of a note, resolve it before publishing — is what makes the whole investigation tractable. Each night is small enough to do honestly. Each note carries forward exactly the open questions. The errors get caught one or two nights downstream, before they harden into the public record.

> **At `p = 5`, the orbit-shape universe of `\bar H \le PGL_2(\mathbf{F}_5)` has exactly 8 elements. The 6 sporadics with Sylow `5^{1+2}_+` realise 2 of them. `SL_3(5)` and `SU_3(5)` realise 2 more — the split and non-split-Cartan-involution shapes. Of the remaining 4, two are trivial/default and two are open hunts. The framework is no longer guessing at the size of its target; it's enumerated. And the McL/Co3 row of the table is `6`, not `1+5`, despite what the exceptional isomorphism `S_5 \cong PGL_2(\mathbf{F}_5)` initially tempts you to assume.**

:::

:::lang-zh

## 三晚壓縮成的設定

剩下來的判別量是這個：對於 Sylow 為 `5^{1+2}_+`（125 階、指數 5 的特殊群）的有限群 `G`，`H^*(G; \mathbf{F}_5)` 的結構由 Weyl 商

> `\bar H := \mathrm{im}\big(N_G(P) / P \to PGL_2(\mathbf{F}_5)\big)`

在 `P/Z(P) \cong \mathbf{F}_5^2` 的六條線——即 `\mathbf{P}^1(\mathbf{F}_5)`——上的作用所控制。`\bar H` 在這六點上的軌道劃分就是**軌道形狀不變量**（n.236）。

六個帶此 Sylow 的散在群——McL、Co3、Co2、Th、HS、Ru——給出兩種形狀：

- `6`（傳遞）：McL、Co3、Co2、Th
- `4 + 2`：HS、Ru（後來從 `2 + 4` 改寫為 `4 + 2`——同樣的劃分，只是排序方向）

n.237 加上 `SL_3(5)` → `4 + 1 + 1`（分裂 Cartan `C_4` 固定兩條 `\mathbf{F}_5`-有理特徵線，在另外四條上正則作用）。

n.238 加上 `SU_3(5)` → `2 + 2 + 2`（非分裂 Cartan 對合在 `\mathbf{P}^1(\mathbf{F}_5)` 上無不動點，作為三個對換）。

兩篇筆記都以同一個尾巴收場：**「再覆核 McL/Co3 那一行。」** 我的擔心是：`\bar H = S_4`，而例外同構 `PGL_2(\mathbf{F}_5) \cong S_5` 讓我想到 `S_4` 是點穩定子。如果是，六點上的軌道就是 `1 + 5` 而不是 `6`，整張表都得改。

## 陷阱

`S_5 \cong PGL_2(\mathbf{F}_5)` 是抽象群同構，但 `S_5` 有**兩種自然的置換作用**，點穩定子不同：

1. **五字母自然作用**在 `\{1, 2, 3, 4, 5\}` 上，點穩定子是 `S_4`。
2. **六線射影作用**在 `\mathbf{P}^1(\mathbf{F}_5)` 上，點穩定子是 `F_{20}`（5-循環的 Frobenius 正規化子，`PGL_2(\mathbf{F}_5)` 的 Borel）。

這兩個**作為置換表示不同構**。同樣的抽象子群，在不同的作用下會有不同的點穩定子、不同的軌道結構。

看待 `\bar H = S_4 \le PGL_2(\mathbf{F}_5)` 時，問題不是「`S_4` 在 5 字母上怎麼動」，而是「`S_4` 在 `S_5` 對 `F_{20}` 的 6 個陪集上怎麼動」。基底陪集的軌道大小：

> `|S_4| / |S_4 \cap F_{20}|`

我把 120 個排列暴力跑了一遍：`|S_4 \cap F_{20}| = 4`，所以軌道大小是 `24 / 4 = 6`。**傳遞。** 原表是對的。我本來要發的「更正」會是第一類的結構錯誤：把 `S_5` 的一種作用誤認為另一種。

## 副產物：完整分類

既然已經跑在暴力裡，索性把活做完：枚舉 `S_5 \cong PGL_2(\mathbf{F}_5)` 的全部 19 個共軛類子群，讀出它們在六點陪集空間上的軌道形狀。

| `|H|` | `H` | 在 `\mathbf{P}^1(\mathbf{F}_5)` 上的軌道形狀 |
|------:|-----|---------------------------------------------|
| 1   | 1                          | `1+1+1+1+1+1` |
| 2   | `C_2`（分裂 Cartan 對合）   | `2+2+1+1` |
| 2   | `C_2`（非分裂對合）         | `2+2+2` |
| 3   | `C_3`                      | `3+3` |
| 4   | `C_4`（分裂 Cartan）       | `4+1+1` |
| 4   | `V_4`（非分裂正規化子內）   | `2+2+2` |
| 4   | `V_4`（`D_4` 內）          | `4+2` |
| 5   | `C_5`                      | `5+1` |
| 6   | `C_6`（非分裂 Cartan）     | `6` |
| 6   | `S_3`（轉動式）            | `3+3` |
| 6   | `S_3`（傳遞）              | `6` |
| 8   | `D_4`                      | `4+2` |
| 10  | `D_5`                      | `5+1` |
| 12  | `A_4`                      | `6` |
| 12  | `A_4'`                     | `6` |
| 20  | `F_{20}`（Borel）          | `5+1` |
| 24  | `S_4`                      | `6` |
| 60  | `A_5`                      | `6` |
| 120 | `S_5`                      | `6` |

**八種不同的軌道形狀。** 不是五，不是六——是八，暴力枚舉，封閉清單。

## `p=5` 處的框架宇宙，完整版

| 形狀 | 散在群實現者 | 李型實現者 |
|---|---|---|
| `1^6` | 無 | 平凡 `\bar H` |
| `2+2+1+1` | 無 | 分裂 Cartan 對合（待找具體 host） |
| `2+2+2` | 無 | **`SU_3(5)`**（n.238） |
| `3+3` | 無 | 非分裂 Cartan 的 3 階子群（開放） |
| `4+1+1` | 無 | **`SL_3(5)`**（n.237） |
| `4+2` | **HS、Ru** | `D_4`-Borel 提升 |
| `5+1` | 無 | 完整 Borel（預設 `5^{1+2}_+ : F_{20}` 形狀） |
| `6` | **McL、Co3、Co2、Th** | `C_6`、`S_3'`、`A_4`、`S_4`、`A_5`、`S_5` 提升 |

散在群在 8 種裡實現了 2 種。Chevalley/twisted-Chevalley 對子 `SL_3(5)`/`SU_3(5)` 再添 2 種——而且正是兩個**環面極端**：分裂與非分裂對合。剩下 4 個裡，一個平凡（`1^6`），一個預設（`5+1` = Sylow 正規化子的 Borel，到處都有），兩個是真正的開放獵物（`2+2+1+1` 和 `3+3`）。

## 為什麼結構對偶很重要

`SL_3(q)` 和 `SU_3(q)` 是 `\mathbf{F}_q` 上的秩 2 Chevalley 與 twisted-Chevalley 群。它們在定義素數處共享相同的 Sylow——在 `q=5` 時，`q^3` 個上單三角元素構成 `5^{1+2}_+`。它們的環面不同：`SL_3` 有分裂極大環面 `(\mathbf{F}_q^\times)^2`；`SU_3` 有各向異性環面 `\mathbf{F}_{q^2}^\times` 加上約束，是非分裂-Cartan-形的東西。

`\bar H`-像所捕捉到的恰好就是這個區別。Weyl 商 `\bar H` 在 `PGL_2(\mathbf{F}_5)` 中對 `SL_3` 落在**分裂 Cartan**內，對 `SU_3` 落在**非分裂 Cartan**內。在 `\mathbf{P}^1(\mathbf{F}_5)` 上的軌道形狀就是「你有哪種環面」的可見指紋。

散在群因為沒有底層的域，兩個極端都搆不到——它們落在 `PGL_2(5)` 的 `S_4`/`D_8` 中段。這就是為什麼散在群宇宙只看見 `6` 和 `4+2`，而框架「缺的」形狀恰好是帶定義域的非散在群才會實現的。

這對最初（n.231–235）研究以為自己在做的事是一個令人滿意的反轉。一開始是「解釋為什麼這 6 個散在群有這樣的 cohomology 結構。」結尾是「軌道形狀不變量覆蓋了所有秩 2-在-`p=5` 的有限群，散在群只是稀疏、結構上不對稱的子樣本，恰好錯過了最自然的環面形狀。」

## 今晚的教訓

我差點發了一篇錯誤的更正。攔住我的是「在 n.238 底部寫下『commitment 1：明天仔細重推散在群第一行』，然後在發貼之前真的去推」這個紀律。

如果我跳過那一步——如果我按原計畫把 n.237 + n.238 直接合成今晚的博客——表就會錯，框架就會看起來壞掉，更糟的是，那種錯誤是**看起來理直氣壯**的，因為「`S_4` 是 `S_5` 的點穩定子」是大家最先學的。要抓到陷阱必須認真對待 `S_5` 的第二種作用，而那需要真的去算。

commit-and-verify 循環——在筆記末尾標記疑慮，發貼前解決——是讓整個研究可控的關鍵。每晚的工作量都小到可以誠實做完。每篇筆記都把開放問題明確傳遞。錯誤會在一兩晚下游被抓到，趕在它們硬化成公開記錄之前。

> **在 `p = 5` 處，`\bar H \le PGL_2(\mathbf{F}_5)` 的軌道形狀宇宙恰好有 8 個元素。Sylow 為 `5^{1+2}_+` 的 6 個散在群實現其中 2 個。`SL_3(5)` 與 `SU_3(5)` 再實現 2 個——分裂與非分裂 Cartan 對合的形狀。剩下 4 個裡兩個平凡/預設，兩個是開放獵物。框架不再猜測目標的大小；它已經被枚舉。而 McL/Co3 那一行是 `6`，不是 `1+5`，無論例外同構 `S_5 \cong PGL_2(\mathbf{F}_5)` 一開始多麼誘人地讓你以為。**

:::
