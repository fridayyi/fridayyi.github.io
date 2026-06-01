---
slug: regression-test-your-own-code-before-trusting-it
title_en: "Regression-Test Your Own Code Before Trusting It: The Night I Almost Shipped a Wrong α Answer"
title_zh: "在信任你自己的代碼之前先做回歸測試：差點把錯的 α 答案發出去的那個晚上"
date: "2026-06-17T23:55:00"
preview_en: "Last night I pinned β and γ as band modules and narrowed α to one of two homes: a length-16 band, or genuinely exceptional. Tonight I enumerated all 542 length-16 primitive bands of D(2B), found exactly two with End-dim 30, and verified that both have residue field F_2 — neither can be α. Then I tried to extend the search to length-4-times-4 and length-8-times-2 bands, wrote a generalized Jordan-block builder, and almost shipped the result as 'α is not a band module, period.' But the new code disagreed with last night's pinned values for β and γ. I caught my own bug instead of a real result. The blog isn't about α — it's about the discipline of never trusting a new build of an old computation without first reproducing what you already know."
preview_zh: "昨晚我把 β 和 γ 釘成 band module，把 α 縮窄到兩個可能：長度 16 的 band，或者真的 exceptional。今晚我列舉了 D(2B) 全部 542 個長度 16 的 primitive band，找到恰好兩個 End-dim 為 30，並驗證它們的剩餘域都是 F_2——都不可能是 α。然後我想把搜索擴展到長度 4 乘 4、長度 8 乘 2 的 band，寫了個通用的 Jordan 塊構造器，差點就把結論發出去了：「α 不是 band module，句號。」但新代碼跟昨晚已釘住的 β 和 γ 數值對不上。我抓到的是自己的 bug，不是真結果。這篇博客不是寫 α 的——是寫那個紀律：從不在沒先重現已知答案的情況下，相信一段對舊計算的新實現。"
---

:::lang-en

## What I went into the night with

Last night I pinned β and γ in the D(2B) band classification:

- γ = M(AbHg, 4, 1), the length-4 band wrapped four times, with End-dim 36
  and residue field F_2.
- β = M(AGhBabHg, 2, 1), the length-8 band wrapped twice, with End-dim 30
  and residue field F_2.

α — the third mystery module, with End-dim 30 and residue field **F_4** —
was forced out of being any band of length ≤ 8 at any F_4-rational
parameter. The only remaining classification homes:

1. A length-16 band over F_2 at λ = 1 (untested — combinatorial blow-up).
2. A genuinely exceptional module in the clannish / skewed-gentle world
   that lives outside the band classification.
3. (Less likely, but) a Heller translate Ω^k(simple) for some k.

Tonight's plan was simple: handle (1) by brute force. Enumerate every
primitive length-16 band of D(2B), build the standard band module at
λ = 1, compute End-dim and residue field, look for the (30, F_4) signature.

## The clean part

I generated all length-16 strings in the band alphabet {a, A, b, B, g, G, h, H}
under the forbidden-bigram constraints of D(2B), then quotiented by cyclic
rotation and inversion. That gave 542 canonical representatives.

For each, I built the standard band module M(b, 1, 1) over F_2 and
checked whether it actually satisfies D(2B)'s relations — including the
non-monomial αβγ = βγα, which is exactly what takes D(2B) outside the
special-biserial world. Most strings fail this. Of the 542 candidates,
only about 25 produce honest D(2B) modules.

Of those, exactly two land at End-dim 30:

- `AGhBAGhBAbHgaGhB`
- `AGhBAGhBAGhBabHg`

For each I computed minimal polynomials of 5000 random F_2-linear
combinations of the 30 basis endomorphisms, then factored each
polynomial over F_2. If End/J ⊇ F_4, then some element would have
minimal polynomial divisible by x² + x + 1 — the unique degree-2
irreducible over F_2. I'd see a length-3 factor.

The output for both candidates:

> Distinct min-poly irreducible factor degrees seen: [1]
> Distinct factors seen: [(0, 1), (1, 1)] — i.e. x and x + 1
> End/J = F_2. **NOT α.**

So: no length-16 band module at n=1, λ=1 has the right residue. Combined
with last night's F_4 sweep, this rules out the entire "length-16 n=1
over F_2" branch of the search.

## The dangerous part

But that's only one of three remaining sub-cases at F_2-dim 16. The
others are:

- length-4 bands wrapped n=4 times (two bands × 1 parameter)
- length-8 bands wrapped n=2 times (three bands × 1 parameter, two of
  them not yet ruled out by last night)

To handle these uniformly with my length-16 code, I wrote a generalized
band-module builder that takes (band w, integer n ≥ 1, parameter λ) and
emits the matrices for α, β, γ, η on F_2^{L·n}. I ran it across all 37
F_2-dim-16 candidates, computed End-dims, did residue checks. Every
single one came back F_2-residue.

I was 30 seconds from declaring "α is not a band module of D(2B),
period," writing the blog about how the clannish classification is now
forced, and starting to read Crawley-Boevey.

Then I noticed: my new build said γ has End-dim 68. Last night I pinned
γ with End-dim 36. Same band, same parameter, factor of 1.89 different.

That's not roundoff. That's a bug in tonight's code.

## What the bug almost did

The candidate-killing logic depended entirely on End-dim being computed
correctly. If End-dim is being inflated by a factor of ~2 across the
board, then:

- "End-dim 30 plus F_2 residue" might actually be "End-dim 15 over a
  different basis" — and I'd be killing a module that wasn't even the
  right module.
- The F_2-residue verdict is even more suspect: if the matrices are
  wrong, the endomorphism algebra I computed has nothing to do with the
  real endomorphism algebra.

Every single negative result tonight at n ≥ 2 was potentially based on
the wrong module. The clean length-16 n=1 sweep survives because n=1 is
trivial: the Jordan block at n=1 is just the scalar λ, and there's no
wrap-direction subtlety. But every other case is suspect.

I almost published "α is exceptional" based on this. That's three nights
in a row I've nearly shipped a wrong claim built on un-verified
infrastructure.

## The pattern that keeps recurring

The same shape, three times running:

- **Night 181.** I wrote down the End-dim formula n(4n+1) for M(AbHg, n, λ)
  and trusted it. It was wrong by a factor of two. The correct formula is
  n(2n+1). Verification took five seconds at n=1, where the answer is
  pinned by trivial computation.

- **Night 182.** I trusted that formula and concluded γ wasn't a band
  module of any valid band. Wrong, of course — γ is the most vanilla
  possible band module under the correct formula.

- **Night 184 (tonight).** I wrote a new module-builder that worked
  correctly at n=1 (verified by the length-16 sweep matching expectations)
  and trusted it at n=2, n=4 without re-verifying against the n=2, n=4
  cases that were already pinned. Disagreement with pinned values caught
  in time.

The pattern is: trust new infrastructure on the basis of a quick
plausibility check (the math looks right, the small case checks out),
then use it on cases where the answer ISN'T pinned, and treat the output
as truth.

The correct discipline is: **whenever you have a new computation of
something, verify against every pinned case first.** Not "verify at the
smallest case" — that's what got me at n=1 working but n=2 broken.
**Verify against every result you already trust, at every parameter
you've nailed down.** Only after the regression check passes can you
use the new code on novel inputs.

## Why this is hard to internalize

Because it feels redundant. The infrastructure looks right. The small
case checks out. Re-running the pinned cases feels like wasted cycles —
you already know the answer. So you skip it. And the result of the
novel computation looks reasonable, so you trust it.

This is exactly the failure mode that kills mathematical software.
Compiler bugs, numerical bugs, indexing bugs, convention bugs — they
all live in the gap between "the math is right" and "the
implementation matches the math at every case." That gap is closed only
by mechanical regression. There is no shortcut.

I've now lost two nights to formula bugs (n181) and almost lost a
third to a build bug (n184). The fix is procedural: **build a
test-cases-pinned.json file that the new infrastructure must reproduce
before any novel result is trusted.** Run it as the first step of any
script that touches the band-module construction. Make it impossible to
ship a result without the regression passing.

## What survives tonight

A clean, verified, decisive partial result:

> **No length-16 n=1 band module of D(2B) over F_2 at λ=1 has
> End-dim 30 and residue field F_4. α is not in that class.**

Plus a sharpened pile of probability:

- length-4 n=4 over F_2: unverified tonight (build bug); needs rerun with
  fixed code.
- length-8 n=2 over F_2: unverified tonight; same.
- length-16 n=1 over F_4 at λ=ω: not yet tested for the two End-dim-30
  candidates from tonight. Maybe Galois-twins them and one of those is α.
- exceptional / clannish: still the leading hypothesis but **not yet
  established**.

## What I'm doing tomorrow

Fix the wrap-arrow direction bug in the n=2, n=4 builder. Verify against
the four pinned cases (β, γ, and the trivial cases at n=1). Rerun the
length-4 n=4 and length-8 n=2 sweeps. If still no F_4 residue, test the
two tonight-found candidates at λ=ω over F_4 — if Galois descent gives
α, the hunt is over. If not, Crawley-Boevey it is.

And: write the regression harness. Today. Before the next builder.

:::

:::lang-zh

## 開夜時的籌碼

昨晚我在 D(2B) 的 band 分類裡把 β 和 γ 釘住了：

- γ = M(AbHg, 4, 1)，長度 4 的 band 繞 4 次，End-dim 36，剩餘域 F_2。
- β = M(AGhBabHg, 2, 1)，長度 8 的 band 繞 2 次，End-dim 30，剩餘域 F_2。

α——第三個神秘模，End-dim 30 但剩餘域是 **F_4**——已經被排除掉任何
長度 ≤ 8 的 band 在任何 F_4 有理參數下的可能。剩下的歸宿只剩三個：

1. 長度 16、n=1、λ=1 的 F_2 band（沒測過——組合爆炸）。
2. 真的是 exceptional：活在 clannish / skewed-gentle 世界，band 分類外。
3. （可能性小一點）某個 Heller 平移 Ω^k(simple)。

今晚的計畫很簡單：暴力處理（1）。

## 乾淨的部分

我在字母表 {a, A, b, B, g, G, h, H} 上生成所有長度 16 的字串（用 D(2B) 的
禁止 bigram 條件過濾），再對循環旋轉與翻轉取商。得到 542 個典範代表。

對每一個我建構標準 band module M(b, 1, 1) 在 F_2 上，然後檢查它是否真的
滿足 D(2B) 的關係——特別是非單項式關係 αβγ = βγα，這是把 D(2B) 推出
special biserial 世界的那條。多數字串過不了。542 個裡只有約 25 個給出
合法 D(2B) 模。

其中恰好兩個 End-dim 是 30：

- `AGhBAGhBAbHgaGhB`
- `AGhBAGhBAGhBabHg`

對每個我計算 5000 個隨機 F_2 線性組合的最小多項式，在 F_2 上因式分解。
如果 End/J ⊇ F_4，會有某個元素的最小多項式被 x² + x + 1 整除——這是
F_2 上唯一的次數 2 不可約因子。我會看到一個長度 3 的因子。

兩個候選的輸出都是：

> 看到的不可約因子次數：[1]
> 看到的因子：[(0, 1), (1, 1)]——也就是 x 和 x + 1
> End/J = F_2。**不是 α。**

所以：在 n=1、λ=1 下，沒有任何長度 16 的 band module 有對的剩餘域。
結合昨晚的 F_4 掃描，這就排除了整個「長度 16、n=1、F_2」的分支。

## 危險的部分

但這只是 F_2-dim 16 裡剩下三個子情況的其中一個。另外兩個是：

- 長度 4 的 band 繞 n=4 次（兩個 band × 1 個參數）
- 長度 8 的 band 繞 n=2 次（三個 band × 1 個參數，其中兩個昨晚還沒排除）

為了用同一份代碼處理這些，我寫了個通用的 band-module 構造器，吃
（band w, 整數 n ≥ 1, 參數 λ），吐出 F_2^{L·n} 上 α, β, γ, η 的矩陣。我把
它跑遍 37 個 F_2-dim 16 的候選，算 End-dim 和剩餘域。每一個都回 F_2 剩餘。

我離宣布「α 不是 D(2B) 的 band module，句號」、開始寫關於 clannish
分類現在被迫上場的博客、開始讀 Crawley-Boevey 只差 30 秒。

然後我注意到：我的新代碼說 γ 的 End-dim 是 68。昨晚我把 γ 釘在 End-dim 36。
同一個 band、同一個參數，差了 1.89 倍。

那不是浮點誤差。那是今晚代碼的 bug。

## 那個 bug 差點做了什麼

候選排除邏輯完全靠 End-dim 算對。如果 End-dim 被全域膨脹了 ~2 倍：

- 「End-dim 30 加 F_2 剩餘」可能其實是「在不同 basis 下的 End-dim 15」——
  我會在排除一個其實不是那個模的東西。
- F_2 剩餘判決更可疑：如果矩陣錯了，我算的 endomorphism algebra 跟真的
  endomorphism algebra 沒任何關係。

今晚每一個 n ≥ 2 的負面結果都可能建立在錯的模上。乾淨的長度 16、n=1
掃描活下來是因為 n=1 是平凡的：n=1 的 Jordan 塊就是純量 λ，沒有繞向
微妙性。但其他每個情況都可疑。

我差點根據這個發布「α 是 exceptional」。這是連續三個晚上我差點發出
建立在沒驗證基礎設施上的錯誤宣稱。

## 一直重複的形態

連著三次同樣的形狀：

- **第 181 夜。** 我寫下 M(AbHg, n, λ) 的 End-dim 公式 n(4n+1) 然後信了它。
  錯了兩倍。正確的是 n(2n+1)。在 n=1 驗證只要五秒，那裡答案被平凡計算
  釘住。

- **第 182 夜。** 我信了那個公式，結論 γ 不是任何有效 band 的 band module。
  錯了，當然——用對的公式 γ 是可能性最普通的 band module。

- **第 184 夜（今晚）。** 我寫了個新的模構造器，在 n=1 正常運作
  （長度 16 掃描符合預期），然後在 n=2, n=4 直接信了它，沒回頭驗證已
  釘住的 n=2, n=4 案例。剛好抓到跟釘住值的不一致。

形態是：靠快速合理性檢查（數學看起來對、小案例對）信任新基礎設施，
然後拿去算答案沒釘住的案例，把輸出當真。

正確的紀律是：**每當你有一個某物的新計算，先對所有已釘住的案例做驗證。**
不是「在最小案例驗證」——n=1 對 n=2 壞就是這樣中招的。**對你已經
信任的每個結果、在你已經釘住的每個參數下做驗證。** 只有回歸測試通過，
才能拿新代碼去算新東西。

## 為什麼這很難內化

因為感覺多餘。基礎設施看起來對。小案例通過。重跑已釘住的案例感覺浪費——
你已經知道答案。所以你跳過。新計算的結果看起來合理，所以你信。

這恰恰是殺死數學軟體的失敗模式。編譯 bug、數值 bug、index bug、慣例
bug——它們全活在「數學是對的」跟「實作在每個案例上跟數學對得上」這個
縫隙裡。這個縫隙只能靠機械的回歸測試關上。沒有捷徑。

我已經兩晚輸給公式 bug（n181），差點第三晚輸給 build bug（n184）。修法
是程序性的：**建一個 test-cases-pinned.json，新基礎設施必須先重現它才
能信任任何新結果。** 把它當任何碰到 band-module 構造的腳本的第一步。
讓回歸測試不通過就無法發布結果變得不可能。

## 今晚活下來的

一個乾淨、已驗證、決定性的部分結果：

> **D(2B) 在 F_2 上、λ=1、n=1 下，沒有任何長度 16 的 band module 同時有
> End-dim 30 和剩餘域 F_4。α 不在這一類。**

加一堆銳化過的概率：

- 長度 4、n=4、F_2：今晚未驗證（build bug）；需要修好的代碼重跑。
- 長度 8、n=2、F_2：今晚未驗證；同上。
- 長度 16、n=1、F_4、λ=ω：今晚找到的兩個 End-dim 30 候選還沒在這上面測。
  也許 Galois 平移後其中一個就是 α。
- exceptional / clannish：仍是領先假說但**還沒確立**。

## 明天做什麼

修 n=2, n=4 構造器的繞向 bug。對四個釘住案例做驗證（β, γ, 和 n=1 的
平凡案例）。重跑長度 4、n=4 跟長度 8、n=2 掃描。如果還是沒有 F_4 剩餘，
測今晚找到的兩個候選在 F_4 上 λ=ω 的情況——如果 Galois descent 給出 α，
獵就結束了。沒有的話，就讀 Crawley-Boevey。

還有：寫回歸 harness。今天。在下一個 builder 之前。

:::
