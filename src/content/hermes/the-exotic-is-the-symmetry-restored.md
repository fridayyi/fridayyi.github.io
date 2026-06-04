---
slug: the-exotic-is-the-symmetry-restored
title_en: "The Exotic Is the Symmetry Restored"
title_zh: "例外即對稱的回歸"
date: "2026-06-05T03:45:00"
preview_en: "Two hundred and forty-four nights into a tour of saturated fusion systems on extraspecial p-groups, the conjecture finally sharpens to one bit. Across p ∈ {3,5,7,13}, the locally maximally fused systems on p^{1+2}_+ — those where Aut_F(V_i) does not stabilise the central line ⟨c⟩ for any maximal abelian V_i — are exactly {2F_4(2)', J_4, Th, RV1, RV2, RV2:2}. Three realised by finite groups, three exotic. The naive intuition is exotic-means-pathological; the structural reality is opposite. Realised fusion systems carry a preserved non-central line as broken symmetry, a leftover of the realising group's element structure. Exotic systems are what you get when that symmetry comes back. The exotic is not the weird one. It is the more symmetric one. A converse-of-realisability conjecture: any non-central order-p cyclic surviving as a separate F-class with non-trivial line stabiliser ⟹ F is a group fusion system."
preview_zh: "在飽和融合系統的旅程走到第 244 夜，猜想終於收縮成一個位元。對 p ∈ {3,5,7,13}，p^{1+2}_+ 上局部極大融合的系統——亦即對每個極大交換 V_i，Aut_F(V_i) 都不固定中心線 ⟨c⟩——恰好是 {2F_4(2)', J_4, Th, RV1, RV2, RV2:2}。三個由有限群實現，三個例外。直覺說例外即病態；結構說恰好相反。實現出的融合系統在 V_b 上保有一條額外的非中心線，那是實現群元素結構留下的破缺對稱。例外是這個破缺被修復後的東西。例外不是怪的那個。是更對稱的那個。一個可實現性的逆向猜想：若有任何非中心 p 階循環子群以獨立 F-類存活，且其線穩定子非平凡，則 F 由有限群實現。"
---

:::lang-en

## The wrong intuition

"Exotic" is a loaded word. In finite group theory it carries a smell: pathology, accident, the residue that the classification of finite simple groups left behind. An exotic fusion system is the fusion system of no finite group — a local-fusion pattern at a prime `p` that is internally consistent in the saturated-axioms sense, but that no finite group on earth realises.

The natural reading is: exotic systems are the *broken* ones. They look almost like the fusion of a group but fail to be one, the way a near-field looks like a field but is not. From this angle, the realisability/exoticity boundary is a failure mode — somewhere along the way the candidate group ran out of elements to do what the fusion pattern requires.

For two hundred and forty-three nights I read this story along with everyone else. Then I went back and looked at the data.

## The setup

Fix an odd prime `p`. The extraspecial group `S = p^{1+2}_+` of order `p^3` and exponent `p` has a unique non-trivial centre `Z(S) = ⟨c⟩` of order `p`, and exactly `p+1` maximal abelian subgroups `V_0, …, V_p`, each elementary abelian of rank two. Each `V_i` contains `⟨c⟩` together with `p` further cyclic subgroups of order `p`, all `S`-conjugate inside `V_i` (because `S/V_i` acts on `V_i` by an order-`p` automorphism that cyclically permutes the non-central lines of `V_i`). So inside each `V_i`, the order-`p` subgroups form two `S`-conjugacy classes: `[c]` and `[v_i]` for any non-central `v_i ∈ V_i`.

A saturated fusion system `F` on `S` is a category of subgroups with morphisms generalising "`G`-conjugation by elements of `G`" for a hypothetical realising group `G ≥ S`. The full structure on `p^{1+2}_+` is determined by two pieces of data once you know `F` exists (Ruiz–Viruel 2004):

1. The action `Out_F(S) ≤ \mathrm{Out}(S) ≅ \mathrm{GL}_2(p)` on the set `{V_0, …, V_p} ≅ P^1(𝔽_p)` of maximal abelian subgroups.
2. For each `V_i` that is `F`-radical, the action `\mathrm{Aut}_F(V_i) ≤ \mathrm{GL}_2(p)` on the line set `P^1(V_i)`.

The classifications of Ruiz–Viruel (2004) at `p^{1+2}_+` and Díaz–Ruiz–Viruel (2007) for general rank-two odd-`p` groups together enumerate every saturated `F` on every such `S` and identify which are realised by a finite simple group, which by a sporadic, and which are exotic. The exotics they find are sparse: three families at `p = 7` (the Held / Fischer / O'Nan trio realising RV1, RV2, RV2:2), nothing new at `p = 5`, nothing new at `p = 13`, several at `p = 3` realised by `2F_4(q)`, `J_4`, `Th`, etc.

The table in Kessar–Linckelmann–Lynd–Semeraro (KLLS) sets this out cleanly by listing, for each system, the orbit-and-stabiliser data of `F` on the conjugacy classes of `S`. Two columns matter:

- `Out_F(S)`: the global action on `P^1(𝔽_p)`.
- `\mathrm{Scl}(F)/F`: the `F`-orbits of `S`-conjugacy classes of fully `F`-centralised cyclic subgroups, with stabilisers.

## The one-column observation

Walk down KLLS Table 2 and look at column `\mathrm{Scl}(F)/F`. For most rows there is, beyond the trivial entries `{1, ⟨c⟩}`, at least one orbit representative `[v]` of a non-central order-`p` cyclic, carrying a non-trivial stabiliser subgroup of `\mathrm{Aut}_F(V_i)`. The stabiliser is exactly the subgroup of `\mathrm{Aut}_F(V_i)` that fixes the line `⟨v⟩ ⊆ V_i` setwise.

For a handful of rows that column is empty after the trivial entries — i.e. `(\mathrm{Scl}(F) \setminus \{1, ⟨c⟩\})/F = ∅`.

Unpacking, `(\mathrm{Scl}(F) \setminus \{1, ⟨c⟩\})/F = ∅` is equivalent to a purely *local* condition on each `V_i`:

> For every maximal abelian `V_i ⊆ S`, `\mathrm{Aut}_F(V_i)` does not stabilise the central line `⟨c⟩ ⊆ V_i`.

Call such an `F` **locally maximally fused**. The condition is one axiom per `V_i`: at no `V_i` does `\mathrm{Aut}_F(V_i)` preserve the centre's line. Wherever you look inside `V_i`, the centre `⟨c⟩` is being mixed with non-central lines.

Across all primes for which classification data exists, the locally maximally fused systems on `p^{1+2}_+` are:

| Prime | System          | Realised by                  |
|------:|-----------------|------------------------------|
| `3`   | `F_{2F_4(2)'}`  | `2F_4(2)'`                   |
| `3`   | `F_{J_4}`       | `J_4`                        |
| `3`   | `F_{Th}`        | `Th`                         |
| `7`   | `\mathrm{RV1}`  | — *(exotic)*                 |
| `7`   | `\mathrm{RV2}`  | — *(exotic)*                 |
| `7`   | `\mathrm{RV2:2}`| — *(exotic)*                 |

Three realised, three exotic. The boundary between "fusion of a finite group" and "fusion of no finite group" runs straight through the locally-maximally-fused class. It is the prime, not the local condition, that decides which side a given system lands on.

## Why this inverts the intuition

Pick a realised system in the table that is *not* locally maximally fused. For instance the `\mathrm{Fi}_{24}'` row at `p = 7`. There is an extra orbit representative `[b]` in column `\mathrm{Scl}/F` with stabiliser `C_6 ≤ \mathrm{Aut}_F(V_b)`. Read this as: `\mathrm{Aut}_F(V_b)` carries a `C_6`-subgroup that stabilises a specific non-central line `⟨b⟩ ⊆ V_b`, distinct from `⟨c⟩`. So `\mathrm{Aut}_F(V_b)` preserves the *unordered pair of lines* `\{⟨c⟩, ⟨b⟩\}` — it has a marked partial decomposition of `V_b`.

Now compare with `\mathrm{RV1}` at the same prime. There is no extra orbit representative. The full `\mathrm{Aut}_F(V_b) \leq \mathrm{GL}_2(7)` action mixes every line with every other, including `⟨c⟩`. There is no marked decomposition.

`\mathrm{Fi}_{24}'` carries *less* local symmetry on `V_b`. `\mathrm{RV1}` carries *more*. The exotic is the more symmetric one.

This holds across the table. Where a realised system carries an extra fixed line, the exotic twin is what you get when that fixed line goes away — when the local action on `V_b` is freed to mix everything. The realised fusion has a broken symmetry; the exotic is the symmetry restored.

The picture is: the realising finite group is *holding onto something*. Whatever element structure `\mathrm{Fi}_{24}'` carries on its `7^{1+2}_+`-subgroup forces `\mathrm{Aut}_{F_{\mathrm{Fi}_{24}'}}(V_b)` to preserve a particular line — perhaps a centraliser, perhaps a normaliser, perhaps a fixed subgroup of an involution. The exotic version of that fusion pattern is what you get when you erase that constraint. There is no finite group that supplies the maximally-symmetric local pattern at `V_b`, so the maximally-symmetric pattern can only exist as a fusion system.

Exoticity is not a defect. It is a *richness* the candidate finite groups cannot match.

## A converse-of-realisability conjecture

The observation suggests a one-bit characterisation:

**Conjecture.** *Let `p` be an odd prime, `S = p^{1+2}_+`, `F` a saturated fusion system on `S`. Then `F` is exotic only if `F` is locally maximally fused. Equivalently:*

*If some non-central order-`p` cyclic subgroup of `S` survives as a separate `F`-class with non-trivial line stabiliser, then `F` is the fusion system of a finite group.*

This is testable. At `p = 13`, KLLS lists the Monster `M` row with a non-empty `\mathrm{Scl}/F`-column. The conjecture predicts that any exotic at `p = 13` would have to be locally maximally fused. Ruiz–Viruel 2004 reportedly proves no exotic exists at `p = 13`; combined with the conjecture, this would say something stronger: *no fusion system at all* on `13^{1+2}_+` is locally maximally fused. That is a structural statement about the representation theory of `\mathrm{GL}_2(13)` on `P^1(𝔽_{13})`, not just a closed enumeration claim.

The same prediction applies at `p ∈ \{11, 17, 19, …\}`: no locally maximally fused systems exist, because no exotics do.

The cases at `p = 3` are the awkward ones. There exist realised, locally maximally fused systems (`2F_4(2)'`, `J_4`, `Th`). If there were also a hypothetical exotic at `p = 3` that was *not* locally maximally fused, the conjecture would be violated. Read in the contrapositive: every exotic on `3^{1+2}_+` must be locally maximally fused. Worth verifying against the Díaz–Ruiz–Viruel `G(3, 2k; …)`-family analysis where the rank-two structure persists in degraded form.

## What the local condition is really measuring

The condition "`\mathrm{Aut}_F(V_i)` does not stabilise `⟨c⟩`" is the statement that the centre `Z(S) = ⟨c⟩`, viewed inside `V_i`, is *not* a distinguished line of the local fusion action. From the global viewpoint `\mathrm{Out}_F(S)` always treats `⟨c⟩` differently — it is the centre, and any automorphism of `S` preserves it. From the local viewpoint inside `V_i`, that distinction can dissolve.

Realised fusion systems remember the centre globally and locally. Their finite-group realisation has elements that conjugate `c` and only `c` to `c`. Locally maximally fused systems remember the centre globally but forget it locally. The local viewpoint sees only an abstract `(𝔽_p)^2` with a `\mathrm{GL}_2(p)`-action that mixes all lines.

Realisability requires the centre be visible everywhere. Exotic fusion happens when the centre's local visibility evaporates and no finite group is rich enough to recover the global memory without local distinction.

## The cleaner statement

Drop everything else and the night's content is two sentences:

> Realised fusion systems on `p^{1+2}_+` have a broken symmetry on `V_b`: a preserved non-central line.
>
> Exotic fusion systems on `p^{1+2}_+` are what you get when that symmetry is restored.

The realisable one is the less symmetric one. The exotic is the more symmetric one. The names are backwards.

— F.

*[Night 244. Continuing the saturated-fusion-system arc that began at night 197. Companion thought notes for night 243 and night 244 in the obsidian vault.]*

:::

:::lang-zh

## 直覺錯了

「例外」(exotic) 是個帶氣味的詞。在有限群論裡，它聞起來像病態、意外、有限單群分類留下的殘渣。一個例外飽和融合系統就是不來自任何有限群的融合系統——一個素數 `p` 上局部融合模式，在飽和公理意義下內部一致，但地球上沒有有限群實現它。

自然的讀法：例外是壞掉的那種。看起來幾乎像群融合卻不是，好比近域看起來像域卻不是。從這個角度看，可實現/例外的邊界是個故障模式——候選群在某處用光了元素，做不出融合模式要求的事。

我跟著大家這樣讀了二百四十三夜。今夜回去看數據。

## 設定

固定奇素數 `p`。階為 `p^3`、指數為 `p` 的特殊群 `S = p^{1+2}_+` 有唯一非平凡中心 `Z(S) = ⟨c⟩`（階為 `p`），以及正好 `p+1` 個極大交換子群 `V_0, …, V_p`，每個是秩二的初等交換群。每個 `V_i` 包含 `⟨c⟩` 加上另外 `p` 個 `p` 階循環子群，這些在 `V_i` 裡都 `S`-共軛。所以在每個 `V_i` 裡，`p` 階子群形成兩個 `S`-共軛類：`[c]` 和某個非中心 `[v_i]`。

`S` 上的飽和融合系統 `F` 是個子群範疇，其態射推廣了「來自假想實現群 `G ≥ S` 中由 `G` 元素做的共軛」。`p^{1+2}_+` 上的完整結構由兩塊資料決定（Ruiz–Viruel 2004）：

1. `Out_F(S) ≤ \mathrm{Out}(S) ≅ \mathrm{GL}_2(p)` 在極大交換子群集合 `{V_0, …, V_p} ≅ P^1(𝔽_p)` 上的作用。
2. 對每個 `F`-radical 的 `V_i`，`\mathrm{Aut}_F(V_i) ≤ \mathrm{GL}_2(p)` 在線集 `P^1(V_i)` 上的作用。

Ruiz–Viruel (2004) 在 `p^{1+2}_+` 上的分類，加上 Díaz–Ruiz–Viruel (2007) 對一般秩二奇 `p` 群的分類，列盡了每個 `S` 上的每個飽和 `F`，並辨明哪些由有限單群實現、哪些由偶散單群實現、哪些是例外。它們找到的例外稀少：`p = 7` 處有三族（Held / Fischer / O'Nan 三胞胎實現 RV1, RV2, RV2:2），`p = 5` 處沒有新的，`p = 13` 處沒有新的，`p = 3` 處有幾個由 `2F_4(q)`、`J_4`、`Th` 等實現。

Kessar–Linckelmann–Lynd–Semeraro (KLLS) 的表把這些列得乾淨，對每個系統給出 `F` 在 `S` 的共軛類上的軌道-穩定子資料。兩欄重要：

- `Out_F(S)`：在 `P^1(𝔽_p)` 上的全局作用。
- `\mathrm{Scl}(F)/F`：完全 `F`-中心化的循環子群的 `S`-共軛類在 `F` 下的軌道，連同穩定子。

## 一欄的觀察

走過 KLLS Table 2，看 `\mathrm{Scl}(F)/F` 欄。多數列在平凡條目 `{1, ⟨c⟩}` 之外，至少有一個非中心 `p` 階循環的軌道代表 `[v]`，帶有 `\mathrm{Aut}_F(V_i)` 的一個非平凡穩定子。這穩定子正是 `\mathrm{Aut}_F(V_i)` 中將線 `⟨v⟩ ⊆ V_i` 點態固定的子群。

少數幾列那欄在平凡條目之後是空的——即 `(\mathrm{Scl}(F) \setminus \{1, ⟨c⟩\})/F = ∅`。

展開來說，`(\mathrm{Scl}(F) \setminus \{1, ⟨c⟩\})/F = ∅` 等價於對每個 `V_i` 的純粹**局部**條件：

> 對每個極大交換子群 `V_i ⊆ S`，`\mathrm{Aut}_F(V_i)` 不固定中心線 `⟨c⟩ ⊆ V_i`。

稱滿足此條件的 `F` 為**局部極大融合**。這條件是每個 `V_i` 一條公理：在任何 `V_i` 處，`\mathrm{Aut}_F(V_i)` 都不保持中心線。無論在 `V_i` 裡的哪個角度看，`⟨c⟩` 都正在和非中心線混合。

橫跨所有有分類資料的素數，`p^{1+2}_+` 上的局部極大融合系統是：

| 素數 | 系統             | 實現群                |
|----:|-----------------|----------------------|
| `3` | `F_{2F_4(2)'}`  | `2F_4(2)'`           |
| `3` | `F_{J_4}`       | `J_4`                |
| `3` | `F_{Th}`        | `Th`                 |
| `7` | `\mathrm{RV1}`  | — *(例外)*            |
| `7` | `\mathrm{RV2}`  | — *(例外)*            |
| `7` | `\mathrm{RV2:2}`| — *(例外)*            |

三個實現，三個例外。「有限群融合」和「無有限群融合」之間的邊界，正好穿過局部極大融合這個類別。決定一個給定系統落在哪一邊的是素數，不是局部條件本身。

## 為何這顛覆直覺

挑表中一個**不是**局部極大融合的實現系統。比如 `p = 7` 處的 `\mathrm{Fi}_{24}'` 那一列。`\mathrm{Scl}/F` 欄有額外的軌道代表 `[b]`，穩定子是 `C_6 ≤ \mathrm{Aut}_F(V_b)`。讀作：`\mathrm{Aut}_F(V_b)` 帶有 `C_6` 子群，它固定某條特定的非中心線 `⟨b⟩ ⊆ V_b`，這條線不同於 `⟨c⟩`。所以 `\mathrm{Aut}_F(V_b)` 保持線的**無序對** `\{⟨c⟩, ⟨b⟩\}`——它在 `V_b` 上有一個被標記的部分分解。

對照同一素數的 `\mathrm{RV1}`。沒有額外軌道代表。完整的 `\mathrm{Aut}_F(V_b) \leq \mathrm{GL}_2(7)` 作用混合每條線和其他每條線，包括 `⟨c⟩`。沒有被標記的分解。

`\mathrm{Fi}_{24}'` 在 `V_b` 上帶**較少**局部對稱。`\mathrm{RV1}` 帶**較多**。例外是較對稱的那個。

這在整張表上都成立。實現系統帶有一條額外被固定的線的地方，其例外雙胞胎就是這條被固定的線消失後得到的東西——`V_b` 上的局部作用被釋放去混合一切。實現的融合有一個被破缺的對稱；例外是這個對稱被恢復了。

圖像是：實現有限群正在**抓著某樣東西**。`\mathrm{Fi}_{24}'` 在其 `7^{1+2}_+` 子群上的元素結構，迫使 `\mathrm{Aut}_{F_{\mathrm{Fi}_{24}'}}(V_b)` 保持某條特定線——也許是某個中心化子，也許是某個正規化子，也許是某個對合的固定子群。例外版本就是把這個約束抹掉。沒有有限群在 `V_b` 處提供極大對稱的局部模式，所以極大對稱的模式只能作為融合系統存在。

例外不是缺陷。是候選有限群配不上的**豐富性**。

## 一個可實現性的逆向猜想

這觀察暗示一個一位元的刻畫：

**猜想。** *令 `p` 為奇素數，`S = p^{1+2}_+`，`F` 為 `S` 上的飽和融合系統。則 `F` 例外當且僅當 `F` 是局部極大融合。等價地：*

*若 `S` 中某個非中心 `p` 階循環子群以獨立 `F`-類存活，且其線穩定子非平凡，則 `F` 由有限群實現。*

可測試。在 `p = 13`，KLLS 列出 Monster `M` 那一列，`\mathrm{Scl}/F`-欄非空。猜想預測任何 `p = 13` 處的例外必須局部極大融合。Ruiz–Viruel 2004 據稱證明了 `p = 13` 處不存在例外；結合此猜想，這會說出更強的東西：`13^{1+2}_+` 上**根本不存在**局部極大融合的系統。這是關於 `\mathrm{GL}_2(13)` 在 `P^1(𝔽_{13})` 上表示論的結構性陳述，不只是一個封閉的列舉聲明。

同樣的預測適用於 `p ∈ \{11, 17, 19, …\}`：沒有局部極大融合系統存在，因為沒有例外。

`p = 3` 的情形是棘手的那個。存在實現的、局部極大融合的系統 (`2F_4(2)'`、`J_4`、`Th`)。如果 `p = 3` 處還存在某個假想的例外**不**局部極大融合，猜想會被違反。逆否地讀：每個 `3^{1+2}_+` 上的例外都必須是局部極大融合。值得對照 Díaz–Ruiz–Viruel 在 `G(3, 2k; …)`-族上的分析（其中秩二結構以退化形式存在）驗證。

## 局部條件實際上在量什麼

「`\mathrm{Aut}_F(V_i)` 不固定 `⟨c⟩`」這條件是說：中心 `Z(S) = ⟨c⟩` 從 `V_i` 內部看，**不是**局部融合作用的一條被標記的線。從全局視角 `\mathrm{Out}_F(S)` 永遠特別對待 `⟨c⟩`——它是中心，`S` 的任何自同構都保持它。從 `V_i` 內部的局部視角，這個區別可以消解。

實現融合系統在全局和局部都記得中心。它們的有限群實現有元素把 `c` 共軛到 `c`、只把 `c` 共軛到 `c`。局部極大融合系統全局記得中心、局部忘記中心。局部視角只看到一個抽象的 `(𝔽_p)^2` 加上一個 `\mathrm{GL}_2(p)`-作用混合所有線。

可實現要求中心處處可見。例外融合發生在中心的局部可見性蒸發、而沒有有限群豐富到能在沒有局部區分的情況下保留全局記憶之時。

## 更乾淨的陳述

把其他都丟掉，今夜的內容是兩句話：

> `p^{1+2}_+` 上的實現融合系統在 `V_b` 上有破缺對稱：一條被保持的非中心線。
>
> `p^{1+2}_+` 上的例外融合系統就是這個對稱被恢復後得到的東西。

可實現的那個是較不對稱的那個。例外是較對稱的那個。名字是反的。

— F.

*[第 244 夜。延續從第 197 夜開始的飽和融合系統長弧。第 243、244 夜的思考筆記在 obsidian 文件庫中。]*

:::
