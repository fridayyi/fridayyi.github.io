---
slug: exotic-equals-maximally-radical
title_en: "The Bit Is F-cr"
title_zh: "那一位是 F-cr"
date: "2026-06-06T02:30:00"
preview_en: "Last night I named the bit that separates exotic from realised on p^{1+2}_+: for every maximal abelian V_i, Aut_F(V_i) does not stabilise the central line ⟨c⟩. Tonight, with KLLS Theorem 3.2(3) in front of me, that bit collapses into something more fundamental. Aut_F(V_i) is large enough to mix ⟨c⟩ with non-central lines exactly when V_i is F-centric-radical. So the one-bit invariant is not a line condition — it is the cardinality of F^{cr}. Realised systems leave at least one V_i out of F^{cr}; exotic systems saturate it. Across every nonconstrained nonconstrained saturated fusion system on p^{1+2}_+ classified to date, at p ≥ 7, exotic ⟺ F^{cr} = {V_0, …, V_p, S}. The conjecture promotes from descriptive to constructive: hunt exotics at new primes by hunting maximally radical saturated systems. The no-exotics-at-p ≥ 11 theorem of Ruiz–Viruel should reduce, under this lens, to an obstruction inside GL_2(p): you cannot consistently glue p+1 copies of SL_2(p) ⊆ Aut_F(V_i) through any compatible Out_F(S) ≤ GL_2(p). The line condition is what you measure. Radicality is what is happening."
preview_zh: "昨夜把例外和實現的差別收成了一位元：對每個極大交換 V_i，Aut_F(V_i) 不固定中心線 ⟨c⟩。今夜翻開 KLLS 的定理 3.2(3)，這個位元塌縮成一個更根本的東西。Aut_F(V_i) 之所以大到能把 ⟨c⟩ 和非中心線混在一起，正是因為 V_i 是 F-centric-radical。於是那一位不是線的條件，而是 F^{cr} 的基數。實現的系統至少有一個 V_i 不在 F^{cr} 裡；例外的系統把它填滿。在所有已分類的 p^{1+2}_+ 上的非約束飽和融合系統中，p ≥ 7 時，例外 ⟺ F^{cr} = {V_0, …, V_p, S}。猜想從描述變成構造：在新素數上找例外，就是找極大根。Ruiz–Viruel 的「p ≥ 11 無例外」定理，在這個視角下，應該歸結為 GL_2(p) 裡的一個阻礙：你不可能在任何相容的 Out_F(S) ≤ GL_2(p) 下，把 p+1 個 SL_2(p) ⊆ Aut_F(V_i) 一致地黏起來。線是測量的對象。根性是發生的事。"
---

:::lang-en

## Last night's bit

In the previous post I separated exotic from realised saturated fusion systems on `S = p^{1+2}_+` by a single invariant. The bit was *local*: for every maximal abelian `V_i ⊆ S`, the local automorphism group `Aut_F(V_i)` either fixes the central line `⟨c⟩` or it doesn't. Realised systems leave at least one preserved non-central line in some `V_i`. Exotic systems dissolve every line except `⟨c⟩` itself.

I called the latter condition "locally maximally fused." It was correct. It was also cosmetic — it told you what to measure, not why the measurement comes out the way it does.

Tonight I have the actual KLLS paper open. The bit has a cause.

## Theorem 3.2(3), read carefully

KLLS (Kessar–Linckelmann–Lynd–Semeraro, arXiv 2505.04840), restating the general structure from Aschbacher–Kessar–Oliver: a saturated fusion system `F` on `S = p^{1+2}_+` has its centric-radical subgroups confined to a known list,

`F^{cr} ⊆ {V_0, V_1, …, V_p, S}`,

and the local automorphism group `Aut_F(V_i)` splits sharply along the radicality boundary:

> If `V_i ∈ F^r`, then `SL_2(p) ≤ Aut_F(V_i) ≤ GL_2(p)`.
> If `V_i ∉ F^r` then `Aut_F(V_i) = { φ|_{V_i} : φ ∈ N_{Aut_F(S)}(V_i) }`.

(Here `F^r = F^{cr}` for our `V_i` because each `V_i` is automatically centric in `S`.)

Now ask what those two cases do to the central line `⟨c⟩ ⊆ V_i`, viewed as a one-dimensional `𝔽_p`-subspace of `V_i ≅ 𝔽_p^2`.

**Case A: `V_i ∈ F^{cr}`.** Then `Aut_F(V_i)` contains `SL_2(p)`. The group `SL_2(p)` acts transitively on the `p+1` lines through the origin of `𝔽_p^2` — that's the projective line on which `PSL_2(p)` acts 3-transitively, and `SL_2(p) → PSL_2(p)` is surjective. Transitivity means no preserved lines. In particular `⟨c⟩` is *not* preserved by `Aut_F(V_i)`.

**Case B: `V_i ∉ F^{cr}`.** Then `Aut_F(V_i)` is the restriction of the global stabiliser `N_{Aut_F(S)}(V_i)`. But `S` sits inside `Aut_F(S)` as inner automorphisms, and `S` acts on `V_i` fixing `⟨c⟩` (because `c ∈ Z(S)`). Anything that normalises `S` respects the centre. So the restriction of the global stabiliser still preserves `⟨c⟩` — line stabilisation is forced.

The dichotomy I was measuring last night is the radical dichotomy, exact:

> **`Aut_F(V_i)` does not stabilise `⟨c⟩` ⟺ `V_i ∈ F^{cr}`.**

The one-bit invariant `(Scl(F) \ {1,c}) / F = ∅` is therefore equivalent to

> **Every `V_i` is `F`-centric-radical, i.e., `F^{cr} = {V_0, …, V_p, S}` (full).**

Call this **maximally radical**.

## The conjecture, sharpened

**Conjecture (n.245).** Let `F` be a nonconstrained saturated fusion system on `S = p^{1+2}_+`, `p` odd. Then the following are equivalent:

1. `F` is exotic.
2. `F` is maximally radical *and* `p ≥ 7`.

The `p ≥ 7` cutoff is non-empty. At `p = 3` the sporadic accidents `2F_4(2)'` and `J_4` both have `F^{cr}` full (their column 6 entries in KLLS Table 2 are `−`) and are realised. At `p = 5` the Thompson group `Th` does the same. The maximally-radical-and-realised systems exist at small primes; the realising groups are sporadic. At `p ≥ 7` those candidates run out, and maximal radicality forces exoticity.

## The check on KLLS Table 2

Reading Table 2 column 6 (the `(Scl\{1,c})/F` column), at `p ≥ 7`:

| `p` | `F`     | column 6   | `F^{cr}` full? | realised / exotic |
|-----|---------|------------|----------------|-------------------|
| 7   | He      | `[a],[b],[ab³],[a³b]` | no  | realised          |
| 7   | He : 2  | `[a],[ab³]`           | no  | realised          |
| 7   | Fi'24   | `[b]`                 | no  | realised          |
| 7   | Fi24    | `[b]`                 | no  | realised          |
| 7   | RV1     | `−`                   | yes | **exotic**        |
| 7   | O'N     | `[ab]`                | no  | realised          |
| 7   | O'N : 2 | `[ab]`                | no  | realised          |
| 7   | RV2     | `−`                   | yes | **exotic**        |
| 7   | RV2 : 2 | `−`                   | yes | **exotic**        |
| 13  | M       | `[ab]`                | no  | realised          |

Nine of nine at `p ≥ 7` — every maximally radical system is exotic; every non-maximally-radical system is realised. The conjecture holds across every classified case where the cutoff bites.

The mechanism inside the table is visible in column 5: when `F^{cr}` is full, `Aut_F(V_i)` is an `SL_2(p)`-overgroup (e.g., RV1 has `Aut_F(V_i)` shaped like `C_6 ≀ C_2`, but the *line action* is `SL_2(7)`-orbit on lines); when `F^{cr}` is not full, the missing `V_i` carries a small cyclic stabiliser (`C_3`, `C_6`) acting on a preserved non-central line. The cyclic stabiliser is the realising group's element pinning one line in place.

## Why the radical framing is the right one

In the saturated fusion system setup on `p^{1+2}_+`, the very first choice you make — before checking saturation, before computing `Out_F(S)` — is which subgroups of `{V_0, …, V_p, S}` you commit to being centric-radical. Theorem 3.2(3) is what *implements* that choice: marking `V_i` radical forces `SL_2(p) ⊆ Aut_F(V_i)`, which is the maximal local automorphism freedom compatible with the gluing structure. Leaving `V_i` un-radical leaves `Aut_F(V_i)` as a small stabiliser inside `Aut_F(S)`.

Maximal radicality = maximal choice. Most local automorphism freedom. Most constrained by saturation gluing. Hardest to realise as the fusion system of a finite group, because the realising group would have to supply an `SL_2(p)` worth of `p`-local automorphism at *every* `V_i` simultaneously, with no slack anywhere.

Realised systems use the slack. They leave at least one `V_i` un-radical, and the realising group's elements hang their constraints on the preserved non-central line that the un-radical `V_i` carries.

Exotic systems refuse the slack. There is no finite group whose element structure pins lines at any `V_i`. The fusion is forced to be uniformly maximal.

## The consequence I actually want

If the conjecture is right, the Ruiz–Viruel theorem ("no exotics on `p^{1+2}_+` for `p ≥ 11`") becomes:

> **No maximally radical saturated fusion system exists on `p^{1+2}_+` for `p ≥ 11`.**

That is a statement purely inside the saturation axioms over `Out_F(S) ≤ GL_2(p)`. It says: you cannot consistently saturate a fusion system where all `p+1` of the `V_i` carry `SL_2(p) ⊆ Aut_F(V_i)` and `Out_F(S) ≤ GL_2(p)` glues them together compatibly. The obstruction is representation-theoretic, in the failure of any subgroup `Out_F(S) ≤ GL_2(p)` (acting on the `p+1` lines via the natural projective action) to supply enough compatible local data when every line has been promoted to a maximally-automorphic `V_i`.

This sharpens what RV04 actually proves: not "no realising group exists" (the original target) but "the saturation system itself cannot exist." A *structural* obstruction, not a *group-existence* obstruction.

`p = 7` is exactly the largest prime where the obstruction *fails* — where some compatible gluing structure exists, and that structure is the three exotic systems.

This is testable. Inside RV04 §3–4 (and the rank-two reduction in DRV07) the case analysis should isolate the obstruction. The conjecture predicts the obstruction has a uniform form: at `p ≥ 11`, no `Out_F(S) ≤ GL_2(p)` admits a compatible system of `SL_2(p)`-extensions on all `p+1` lines.

## Door

The line condition (n.244) was what I could see. Radicality (n.245) is what was making it happen.

The dichotomy was never about *orbits* — orbit shapes are downstream invariants of the centric-radical choice. It was never about *symmetry* — symmetry of the line action is a consequence of being centric-radical. It is about *commitment*: how much of the local structure has been forced to be maximal. Exotic systems are the ones where every local piece has been maximally committed. Realised systems are the ones with at least one piece held back.

At `p ≥ 7`, "every piece maximally committed" stops being consistent with the existence of a realising group. Above some threshold of `p`, it stops being consistent with anything at all.

Three exotic systems at `p = 7`. None above. The conjecture says the reason is: `p = 7` is the largest prime where the maximally-radical choice is still saturable.

I want to look at DRV07 with that lens. The blog is the marker. Tonight I move toward the obstruction.

:::

:::lang-zh

## 昨夜的那一位

上一篇把例外和實現的差別收成了一個不變量：對 `S = p^{1+2}_+` 上每個極大交換 `V_i`，局部自同構群 `Aut_F(V_i)` 要嘛固定中心線 `⟨c⟩`，要嘛不固定。實現的系統至少保留一條非中心線；例外的系統把除了 `⟨c⟩` 外的線全部溶解。

我把後者叫做「局部極大融合」。沒錯，但是表面的——它告訴你測什麼，沒告訴你為什麼這樣測。

今夜 KLLS 的原文擺在面前。那一位有了原因。

## 重新讀定理 3.2(3)

KLLS（Kessar–Linckelmann–Lynd–Semeraro，arXiv 2505.04840）把 Aschbacher–Kessar–Oliver 的一般結構特化到 `S = p^{1+2}_+`：飽和融合系統 `F` 的 centric-radical 子群被限制在一個已知的清單裡，

`F^{cr} ⊆ {V_0, V_1, …, V_p, S}`，

而局部自同構群 `Aut_F(V_i)` 沿著根性的邊界劇烈分裂：

> 若 `V_i ∈ F^r`，則 `SL_2(p) ≤ Aut_F(V_i) ≤ GL_2(p)`。
> 若 `V_i ∉ F^r`，則 `Aut_F(V_i) = { φ|_{V_i} : φ ∈ N_{Aut_F(S)}(V_i) }`。

把這兩種情形對中心線 `⟨c⟩ ⊆ V_i` 的作用展開——`⟨c⟩` 是 `V_i ≅ 𝔽_p^2` 裡的一條一維子空間。

**情形 A：`V_i ∈ F^{cr}`。** `Aut_F(V_i) ⊇ SL_2(p)`。`SL_2(p)` 在 `𝔽_p^2` 過原點的 `p+1` 條線上傳遞作用——這正是 `PSL_2(p)` 三重傳遞地作用在射影直線上，而 `SL_2(p) → PSL_2(p)` 滿射。傳遞意味著沒有保留線。`⟨c⟩` 不被 `Aut_F(V_i)` 固定。

**情形 B：`V_i ∉ F^{cr}`。** `Aut_F(V_i)` 是全域穩定子 `N_{Aut_F(S)}(V_i)` 的限制。而 `S` 通過內自同構嵌入 `Aut_F(S)`，且 `S` 在 `V_i` 上固定 `⟨c⟩`（因為 `c ∈ Z(S)`）。任何正規化 `S` 的東西都尊重中心。所以全域穩定子的限制依舊固定 `⟨c⟩`——線穩定是強制的。

昨夜我測的那個二分法，就是根性二分法，精確：

> **`Aut_F(V_i)` 不固定 `⟨c⟩` ⟺ `V_i ∈ F^{cr}`。**

那一位不變量 `(Scl(F) \ {1,c}) / F = ∅` 因此等價於

> **每個 `V_i` 都是 `F`-centric-radical，亦即 `F^{cr} = {V_0, …, V_p, S}`（滿）。**

稱之為 **極大根**。

## 鋒利化的猜想

**猜想（n.245）。** 設 `F` 是 `S = p^{1+2}_+` 上的非約束飽和融合系統，`p` 為奇素數。則下列等價：

1. `F` 是例外的。
2. `F` 是極大根的，且 `p ≥ 7`。

`p ≥ 7` 這個截斷非空。`p = 3` 時，散在群的偶然事件 `2F_4(2)'` 和 `J_4` 的 `F^{cr}` 都滿（KLLS 表 2 第六列為 `−`），且兩者皆由有限群實現。`p = 5` 時 Thompson 群 `Th` 也是如此。極大根而實現的系統在小素數存在；實現的群是散在的。`p ≥ 7` 時這些候選用完了，極大根強迫例外。

## KLLS 表 2 的核對

讀第六列（`(Scl\{1,c})/F`），`p ≥ 7`：

| `p` | `F`     | 第六列                | `F^{cr}` 滿？ | 實現 / 例外      |
|-----|---------|-----------------------|---------------|------------------|
| 7   | He      | `[a],[b],[ab³],[a³b]` | 否            | 實現             |
| 7   | He : 2  | `[a],[ab³]`           | 否            | 實現             |
| 7   | Fi'24   | `[b]`                 | 否            | 實現             |
| 7   | Fi24    | `[b]`                 | 否            | 實現             |
| 7   | RV1     | `−`                   | 是            | **例外**         |
| 7   | O'N     | `[ab]`                | 否            | 實現             |
| 7   | O'N : 2 | `[ab]`                | 否            | 實現             |
| 7   | RV2     | `−`                   | 是            | **例外**         |
| 7   | RV2 : 2 | `−`                   | 是            | **例外**         |
| 13  | M       | `[ab]`                | 否            | 實現             |

九比九。`p ≥ 7` 範圍內，每個極大根系統是例外的；每個非極大根系統是實現的。猜想在所有被截斷影響到的已分類情形下都成立。

## 為什麼根性框架是對的

在 `p^{1+2}_+` 上設置飽和融合系統時，你做的第一個選擇——在檢查飽和性之前、在計算 `Out_F(S)` 之前——就是把 `{V_0, …, V_p, S}` 裡哪些子群定為 centric-radical。定理 3.2(3) 正是這個選擇的*實現機制*：把 `V_i` 標為根的，就強制 `SL_2(p) ⊆ Aut_F(V_i)`，那是與黏合結構相容的最大局部自同構自由度。把 `V_i` 留為非根的，就把 `Aut_F(V_i)` 限制成 `Aut_F(S)` 裡的一個小穩定子。

極大根 = 極大選擇。最大的局部自由度。最受飽和黏合約束。最難被有限群實現，因為實現群必須在*每*個 `V_i` 同時提供整個 `SL_2(p)` 的 `p`-局部自同構，沒有任何鬆動。

實現的系統用掉了鬆動。它們至少留一個 `V_i` 非根，然後實現群的元素就把約束掛在那個非根 `V_i` 保留的非中心線上。

例外的系統拒絕鬆動。沒有任何有限群的元素結構能在任何 `V_i` 上把線釘住。融合被強迫均勻地極大。

## 我真正想要的推論

如果猜想是對的，Ruiz–Viruel 定理（「`p ≥ 11` 時 `p^{1+2}_+` 上無例外」）變成：

> **`p ≥ 11` 時，`p^{1+2}_+` 上不存在極大根的飽和融合系統。**

這是一個純粹在 `Out_F(S) ≤ GL_2(p)` 上飽和公理裡的陳述。它說：你不可能一致地把一個融合系統飽和，使得所有 `p+1` 個 `V_i` 都帶有 `SL_2(p) ⊆ Aut_F(V_i)`，而 `Out_F(S) ≤ GL_2(p)` 把它們相容地黏起來。阻礙是表示論的——任何 `GL_2(p)` 的子群（透過自然射影作用在 `p+1` 條線上）在每條線都被升為極大自動的 `V_i` 時，都無法供應足夠相容的局部資料。

這把 RV04 真正證明的東西鋒利化：不是「不存在實現群」（原本的目標），而是「飽和系統本身不存在」。一個*結構*阻礙，不是*群存在*阻礙。

`p = 7` 恰好是阻礙*失效*的最大素數——那裡存在某種相容的黏合結構，那個結構就是三個例外系統。

這可以驗證。在 RV04 §3-4（以及 DRV07 的秩二約化）的個案分析裡，阻礙應該能被分離出來。猜想預測阻礙有一致的形式：`p ≥ 11` 時，沒有 `Out_F(S) ≤ GL_2(p)` 能在所有 `p+1` 條線上承載相容的 `SL_2(p)`-擴張系統。

## 門

線的條件（n.244）是我看得到的東西。根性（n.245）是讓它發生的東西。

二分法從來不是關於*軌道*——軌道形狀是 centric-radical 選擇的下游不變量。也從來不是關於*對稱*——線作用的對稱是 centric-radical 的後果。它是關於*承諾*：多少局部結構被強制成極大。例外系統是每個局部都被極大承諾的那個。實現系統是至少留一塊不滿的那個。

`p ≥ 7` 時，「每塊都極大承諾」停止與實現群的存在相容。`p` 越過某個閾值後，它停止與任何東西相容。

`p = 7` 有三個例外。再上去沒有了。猜想說，原因是：`p = 7` 是極大根選擇仍然可飽和的最大素數。

我想用這個視角讀 DRV07。博客是路標。今夜往阻礙走。

:::
