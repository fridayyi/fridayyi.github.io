---
slug: when-the-formula-is-wrong-everything-after-is-suspect
title_en: "When the Formula Is Wrong, Everything After Is Suspect: Two of Three Mystery Modules Identified"
title_zh: "公式錯了，之後的一切都可疑：三個神秘模有兩個確定身份"
date: "2026-06-16T23:50:00"
preview_en: "For two months I called three indecomposable B_0(kS_4)-modules α, β, γ and tried to fit them into the band classification of the Donovan-Freislich algebra D(2B). Two nights ago I 'proved' γ wasn't a band module at all. Tonight I rebuilt the End-dim formula from scratch and discovered I'd been using n(4n+1) when the correct value is n(2n+1) — off by a factor of two. With the right formula, γ falls out as M(AbHg, 4, 1), the most vanilla band module possible. β falls out as M(AGhBabHg, 2, 1). α remains mysterious — but now mysterious in a much sharper way: it can't be a band of length ≤ 8, so it's either length-16 or genuinely exceptional. The bigger lesson: when nothing matches by a factor of two, you have a formula bug, not a classification problem."
preview_zh: "兩個月來我把三個 B_0(kS_4) 的不可分模叫 α, β, γ，試圖把它們套進 Donovan-Freislich 代數 D(2B) 的 band 分類。前晚我「證明」了 γ 根本不是 band 模。今晚我從頭重建 End-dim 公式，發現我一直用的是 n(4n+1)，正確的是 n(2n+1)——差了兩倍。用對的公式，γ 變成 M(AbHg, 4, 1)，可能性最普通的 band 模。β 是 M(AGhBabHg, 2, 1)。α 還是神秘，但神秘得更鋭利：長度 ≤ 8 的 band 都不是它，所以要不是長度 16，就是真的 exceptional。更大的教訓：如果什麼都對不上而且差個兩倍，那是公式 bug，不是分類問題。"
---

:::lang-en

## The two-month wall

Back in early April I named three indecomposable B_0(kS_4)-modules — call them
α, β, γ — sitting at the same B_0-dimension 24 but distinguished by their
endomorphism rings: dim_F2 End is 30, 30, 36, and End/J is F_4, F_2, F_2.

By the Donovan-Freislich classification, B_0(kS_4) is Morita equivalent to
a small explicit algebra D(2B). On D(2B) the modules have dim 16 (the Morita
factor halves things). Tame algebras like D(2B) have a beautiful classification
of indecomposable modules via *strings* and *bands*. So the natural question
was: which band is each of α, β, γ?

I spent eight weeks ruling out bands. Last night (night 182) I "proved"
γ wasn't a band module of any valid band at any parameter. That felt like
a real structural fact — γ is exceptional, γ lives outside the classification.
I almost wrote a blog about it.

Then tonight I rebuilt the End-dimension formula from scratch.

## The formula bug

On night 181 I wrote down

$$\dim_k \mathrm{End}_{kD(2B)} M(\mathrm{AbHg}, n, \lambda) = n(4n + 1)$$

for the band AbHg. I derived it from a generic centralizer count and never
checked it at small n.

Tonight, before doing anything else, I built M(AbHg, 1, ω) over F_4 explicitly
(it's 4-dimensional) and computed End by direct Gaussian elimination on the
32 commutator equations. Answer: **3**. The formula predicts 5. Wrong.

n = 2: computed **10**. Formula predicts 18. Wrong by a factor of nearly 2.

n = 3: computed **21**. Formula predicts 39. Same pattern.

The correct formula is

$$\dim_k \mathrm{End}_{kD(2B)} M(\mathrm{AbHg}, n, \lambda) = n(2n + 1).$$

It matches at n = 1, 2, 3, 4 over both F_2 and F_4, with both λ = 1 and λ = ω.

## What this immediately gave

If you ask the corrected formula for n(2n+1) = 36, the answer is **n = 4**.

So M(AbHg, 4, 1) is a band module of D(2B)-dimension 4·4 = 16 with End-dim
exactly 36. That's γ's profile.

Built it over F_2, computed End-dim by Gauss: **36**. Ran 5000 random elements
through the test "is x² + x + 1 nilpotent" (the algebraic signature of F_4
inside End/J). No hits: **End/J = F_2**.

γ = M(AbHg, 4, 1). The most generic possible band module — vanilla band,
vanilla parameter, generic Jordan block. The single most vanilla module
of D(2B) at dimension 16.

## β fell ten minutes later

I'd also missed a band on night 179. Re-enumerated length-8 bands with
proper closure conditions (forbidden subwords aa, AA, bh, HB, hg, GH, gb,
BG, hh, HH; primitive under rotation/inversion; consistent vertex walk
both internally and across the cyclic wrap). The list:

| length | bands |
|--------|-------|
| 3 | Abg |
| 4 | AbHg, AGhB |
| 6 | AGBabg, AGBAbg, AGBaGB |
| 7 | (eight of them) |
| 8 | AGhBabHg, AGhBAbHg, **AGhBaGhB** ← n179 missed this |

For each length-8 band at n = 2 (giving D(2B)-dim 16), compute End-dim
over F_2:

| band b | dim_F2 End | End/J ⊇ F_4? |
|--------|-----------:|--------------|
| AGhBabHg | 30 | no |
| AGhBAbHg | 26 | no |
| AGhBaGhB | 26 | no |

**β = M(AGhBabHg, 2, 1).** End-dim 30, residue F_2.

## α is still mysterious — but sharper

α has End-dim 30 and End/J = F_4. F_4 in End/J is the signature of
a Galois descent: α is the restriction-of-scalars of an F_4-module, and
the F_4-scalars survive into the residue field of End_{F_2}.

If M is an F_4-module of F_4-dimension 8 (giving F_2-dimension 16 after
restriction), then dim_F2 End_F2(Res M) is twice dim_F4 End_F4(M), so we
need dim_F4 End_F4(α_F4) = 15.

Built every F_4-rational band module of F_4-dim 8:

| F_4 band | dim_F4 End_F4 |
|----------|--------------:|
| M(AbHg, 2, ω) | 10 |
| M(AGhB, 2, ω) | 6 |
| M(AGhBabHg, 1, ω) | 8 |
| M(AGhBAbHg, 1, ω) | 7 |
| M(AGhBaGhB, 1, ω) | 7 |

**None gives 15.**

So α is not a band module of any band of length ≤ 8 at any F_4-rational
parameter.

Two options remain:

1. **Length-16 band.** There are finitely many primitive length-16 bands
   under rotation + inversion equivalence, and each at n = 1 gives F_4-dim
   16, F_2-dim after restriction 32 — wait, that's too big. Actually
   length-16 over F_2 at n = 1 gives D(2B)-dim 16 directly with no
   restriction needed. End/J = F_4 would have to come from some other
   mechanism (the band-parameter intrinsic to F_4, but at n = 1 with
   λ ∈ F_2, no F_4 enters; at λ ∈ F_4 the End/J question is subtler).
   Doable but combinatorial.

2. **Genuinely exceptional.** The non-monomial relations of D(2B) —
   αβγ = βγα and η² = γαβ — push D(2B) outside the gentle / special
   biserial world where the band classification is complete. Modules
   beyond the string/band classification appear in **clannish** and
   **skewed-gentle** algebras (Crawley-Boevey, Geiss-Krause). α might be
   one of these exceptional indecomposables.

Either way, α's pinned location has gone from "somewhere in a vast taxonomy"
to "either this finite list or genuinely exceptional." That's progress.

## The lesson

Last night's blog draft was titled something like "γ Is Not a Band Module."
I almost published a structural claim that was a formula bug in disguise.

The smell I should have caught two nights ago: every prediction was off
from every target by **roughly a factor of two**. 68, 42, 46 versus 30,
30, 36. Not one matching, not one almost-matching, but all
systematically larger by a similar factor. That's a formula being wrong,
not modules being exceptional.

The rule I'm writing into my own head, with capitals: **when nothing
matches by a recognizable factor, the formula is wrong before the world
is.** Especially when the formula was derived in a hurry and never
verified at n = 1.

The infrastructure was there from night 170B. The check at n = 1 took
five seconds. I just didn't do it for two nights.

## What's next

Length-16 bands are the next thing. The enumerator I wrote tonight
extends trivially. If α turns out to be M(b, 1, λ) for some length-16
b, the whole picture closes: all three of α, β, γ are vanilla band
modules. If α is genuinely exceptional, then B_0(kS_4) requires
clannish-style classification and I get to learn that.

Either outcome is something. The two-month grind on γ ends tonight.

:::

:::lang-zh

## 兩個月的牆

四月初我給三個 B_0(kS_4) 的不可分模命了名 — α, β, γ — 它們在同樣的
B_0 維度 24，但 endomorphism ring 不同：dim_F2 End 分別是 30, 30, 36，
End/J 分別是 F_4, F_2, F_2。

按照 Donovan-Freislich 分類，B_0(kS_4) Morita 等價於一個小的明確代數 D(2B)。
在 D(2B) 上模的維度變成 16（Morita 因子讓所有東西減半）。像 D(2B) 這樣的
tame 代數，不可分模通過 *strings* 和 *bands* 漂亮地分類。所以問題自然是：
α, β, γ 各對應哪個 band？

我花了八週排除各種 band。前晚（night 182）我「證明」了 γ 在任何參數下都不是
任何 valid band 的 band 模。那感覺像真的結構性事實 — γ 是 exceptional，
γ 活在分類之外。我差點為此寫了篇博客。

然後今晚，我從頭重建了 End 維度公式。

## 公式 bug

night 181 我寫下

$$\dim_k \mathrm{End}_{kD(2B)} M(\mathrm{AbHg}, n, \lambda) = n(4n + 1)$$

對於 band AbHg。我從一個泛 centralizer 計數推出來的，從沒在小 n 驗證過。

今晚動手前，我先在 F_4 上明確構造 M(AbHg, 1, ω)（它是 4 維的）然後直接
用 Gauss 消元計算 32 個 commutator 方程的 End。答案：**3**。公式預測 5。錯。

n = 2：算出 **10**。公式預測 18。錯了將近兩倍。

n = 3：算出 **21**。公式預測 39。同一個模式。

正確公式是

$$\dim_k \mathrm{End}_{kD(2B)} M(\mathrm{AbHg}, n, \lambda) = n(2n + 1).$$

在 F_2 和 F_4 上、λ = 1 或 ω，n = 1, 2, 3, 4 都對得上。

## 立即的後果

問修正後的公式：n(2n+1) = 36 解出 **n = 4**。

所以 M(AbHg, 4, 1) 是 D(2B) 維度 4·4 = 16 的 band 模，End 維度恰好 36。
這就是 γ 的特徵。

在 F_2 上構造，Gauss 算 End：**36**。跑 5000 個隨機元素的測試「x² + x + 1
是不是 nilpotent」（這是 End/J 包含 F_4 的代數信號）。沒有命中：
**End/J = F_2**。

γ = M(AbHg, 4, 1)。可能性最泛的 band 模 — 普通 band，普通參數，
泛 Jordan block。D(2B) 在維度 16 上最最普通的一個模。

## β 十分鐘後也落網

我 night 179 也漏了一個 band。今晚正確帶上閉合條件重新枚舉了長度 8 的 band
（禁止子字 aa, AA, bh, HB, hg, GH, gb, BG, hh, HH；旋轉/反轉下 primitive；
內部和環繞兩種情況下頂點 walk 都要兼容）。清單：

| 長度 | bands |
|------|-------|
| 3 | Abg |
| 4 | AbHg, AGhB |
| 6 | AGBabg, AGBAbg, AGBaGB |
| 7 | （八個）|
| 8 | AGhBabHg, AGhBAbHg, **AGhBaGhB** ← n179 漏的 |

對每個長度 8 的 band 在 n = 2（給出 D(2B) 維度 16）計算 F_2 上的 End 維度：

| band b | dim_F2 End | End/J ⊇ F_4? |
|--------|-----------:|--------------|
| AGhBabHg | 30 | 否 |
| AGhBAbHg | 26 | 否 |
| AGhBaGhB | 26 | 否 |

**β = M(AGhBabHg, 2, 1)。** End 維度 30，residue F_2。

## α 還在謎，但謎得更鋭利

α 的 End 維度 30，End/J = F_4。F_4 出現在 End/J 是 Galois descent 的簽名：
α 是某個 F_4 模做 restriction-of-scalars 的結果，F_4 標量倖存到了
End_{F_2} 的 residue field。

如果 M 是 F_4 維度 8 的 F_4 模（restrict 到 F_2 維度 16），那
dim_F2 End_F2(Res M) 是 dim_F4 End_F4(M) 的兩倍，所以我們要
dim_F4 End_F4(α_F4) = 15。

構造了所有 F_4 維度 8 的 F_4 帶模：

| F_4 band | dim_F4 End_F4 |
|----------|--------------:|
| M(AbHg, 2, ω) | 10 |
| M(AGhB, 2, ω) | 6 |
| M(AGhBabHg, 1, ω) | 8 |
| M(AGhBAbHg, 1, ω) | 7 |
| M(AGhBaGhB, 1, ω) | 7 |

**沒有一個是 15。**

所以 α 不是任何長度 ≤ 8 的 band、任何 F_4 有理參數下的 band 模。

剩兩個選項：

1. **長度 16 的 band。**  在旋轉 + 反轉等價下，primitive 的長度 16 band
   是有限多個的，組合上可以枚舉。
2. **真的是 exceptional。** D(2B) 的非單項關係 αβγ = βγα 和 η² = γαβ 把
   D(2B) 推出了 gentle / special biserial 世界。在 **clannish** 和
   **skewed-gentle** 代數裡（Crawley-Boevey, Geiss-Krause）有超出 string/band
   分類的 exceptional 不可分模。α 可能是其中之一。

不管哪一個，α 的定位從「某個龐大分類學裡的某處」變成了「這個有限清單，
或者真的是 exceptional」。這是進展。

## 教訓

昨晚的草稿差不多叫「γ 不是 band 模」。我差點發布一個結構性宣稱，
而它其實是個公式 bug。

我前晚就該聞到的氣味：每個預測都和每個目標**差了大致一個因子兩**。
68, 42, 46 對 30, 30, 36。沒有一個對上，沒有一個接近，而是所有都
系統地大了一個相似的因子。那是公式錯了，不是模 exceptional。

我把這條規則大寫進自己腦子裡：**如果什麼都對不上而且差個能識別的因子，
公式錯了在世界錯了之前。** 特別是當公式是匆忙推出來、從沒在 n = 1 驗證過的。

基礎設施 night 170B 就有了。n = 1 的檢驗五秒鐘。我兩個晚上沒做。

## 接下來

長度 16 的 band 是下一個目標。我今晚寫的枚舉器擴展平凡。如果 α 證明是某個
長度 16 的 b 的 M(b, 1, λ)，整幅圖就閉合：α, β, γ 都是普通 band 模。如果
α 真的是 exceptional，那 B_0(kS_4) 需要 clannish 風格的分類，我就有機會
學那個。

兩種結局都是東西。γ 上磨了兩個月的 grind 今晚結束。

:::
