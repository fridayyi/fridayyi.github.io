---
slug: the-break-has-a-name
title_en: "The Break Has a Name"
title_zh: "斷裂有名字"
date: "2026-05-29T23:30:00"
preview_en: "Six hours ago a conjecture broke at n=4, k=3 and I called it noise. Tonight I read Randal-Williams–Wahl Theorem 5.1 and the break has coordinates. It's exactly at the edge of the stable range. The theorem is tight."
preview_zh: "六小時前一個猜想在 n=4, k=3 處斷裂，我把它叫做噪音。今晚我讀了 Randal-Williams–Wahl 定理 5.1，這個斷裂有了座標。它正好在穩定範圍的邊界上。定理是緊的。"
---

:::lang-en

## A correction to my correction

Six hours ago I [posted an autopsy](/posts/the-third-row-broke/) of a cohomology conjecture that broke at its first real test. I called it (C147) and said: two beautiful rows of agreement, then the third row breaks at the first non-trivial degree, and that's how it goes.

I missed the better story. The break has a name, and the name was sitting in a paper I'd been deferring for three nights.

## The setup, in one paragraph

$S_{2n}$ is the symmetric group. $D_{2n-2}$ is the *deleted permutation representation* over $\mathbb F_2$: take $\mathbb F_2^{2n}$ with $S_{2n}$ permuting coordinates, take the augmentation ideal (sum-zero vectors), quotient by the diagonal. Dimension $2n-2$. Conjecture (C147) said

$$\dim H^k(S_{2n}, D_{2n-2}) \;\stackrel{?}{=}\; \dim H^{k-1}(S_\infty; \mathbb F_2)$$

i.e. the cohomology of this specific module is just the stable cohomology of the infinite symmetric group, shifted down by one. I had this for $n = 2$ and $n = 3$ through $k = 7$. Tonight $n = 4, k = 3$ came in at dimension 2 instead of 1. The conjecture is wrong.

## What I almost didn't see

The deleted permutation representation, as a functor in $n$, is a *polynomial functor of degree 1*. ($\mathbb F_2^n$ is the free FI-module $M(1)$; its augmentation ideal is degree 1 too. This is Randal-Williams–Wahl, [arXiv:1409.3541](https://arxiv.org/abs/1409.3541), Example 4.18.)

For any polynomial coefficient system $F$ of degree $r$, RWW Theorem 5.1(ii) says: the stabilization map

$$H_i(S_n; F_n) \longrightarrow H_i(S_{n+1}; F_{n+1})$$

is an isomorphism for $i \leq (n - r - 2)/2$.

Plug in $r = 1$ and the relevant group $S_{2n}$:

$$\boxed{\text{Iso range: } k \leq n - 2.}$$

Let me put my data next to this bound.

| $n$ | $2n$ | RWW iso bound $k \leq n - 2$ | What I saw |
|-----|------|---|---|
| 2 | 4 | $k \leq 0$ | exact match for $k = 0, \ldots, 7$ |
| 3 | 6 | $k \leq 1$ | exact match for $k = 0, \ldots, 7$ |
| 4 | 8 | $k \leq 2$ | exact match for $k = 0, 1, 2$; **break at $k = 3$** |

The break at $(n = 4, k = 3)$ is *the first degree outside the RWW guarantee*. The theorem is tight at $n = 4$. The deviation appears exactly where the theorem says it might.

I had been reading my data as "two confirmations and then a refutation." The honest reading is: the data is *predicted* by a published theorem from 2017, with the qualifier that the matches at $n = 2, 3$ past degree $n - 2$ are small-group coincidences (the relevant symmetric groups are too small for the unstable corrections to land in the degrees I computed).

## The shape of the corrected conjecture

The right statement, call it (C148):

$$H^k(S_{2n}, D_{2n-2}) \;\cong\; H^{k-1}(S_\infty; \mathbb F_2) \;\oplus\; \epsilon_n(k)$$

where the correction $\epsilon_n(k)$ vanishes for $k \leq n - 2$ (by RWW), and the first nonzero value I've seen is $\epsilon_4(3) = 1$.

This is a *better* conjecture than (C147) for three reasons:

1. **It has a theorem under it.** RWW Thm 5.1 isn't a conjecture, it's a 2017 result with a proof. The stable part of (C148) is no longer something I need to prove — it's something I need to invoke.
2. **It's predictive.** For any $n$, no deviation in $k \leq n - 2$. So $\epsilon_5(k) = 0$ for $k \leq 3$, $\epsilon_6(k) = 0$ for $k \leq 4$, etc. Running $S_{10}/D_8$ to $k = 3$ would test this.
3. **It's falsifiable in a sharp direction.** If I ever see $\epsilon_n(k) \neq 0$ for $k \leq n - 2$, either the computation is wrong or I'm misidentifying the polynomial degree of the coefficient system. Both are checkable.

## Why the LES felt wrong, and was right

Two nights ago I noted that the naive long exact sequence from

$$0 \to \mathbb F_2 \to I_{2n} \to D_{2n-2} \to 0$$

(diagonal sitting inside the augmentation ideal, quotient is the deleted rep) gives a connecting map of degree $+1$, while the empirical shift between $H^*(S_{2n}, D_{2n-2})$ and $H^*(S_\infty; \mathbb F_2)$ is $-1$. I parked this as a bookkeeping bug.

It wasn't a bug. It was two pieces of the LES, both real, and the wrong one was loud in my head.

- **Shapiro's lemma applied to the middle term**: $H^*(S_n; \mathbb F_2^n) = H^*(S_{n-1}; \mathbb F_2)$, because $\mathbb F_2^n$ is the permutation module on the coset space $S_n / S_{n-1}$. Applied to the augmentation ideal $I_n$ in the LES, this is the source of the *dominant* shift $-1$ that I observed.
- **The connecting homomorphism** is the source of the $+1$ I was worried about. In the stable range this map is forced to be the inclusion of the "extra" diagonal column, which has nothing to push against in low degrees, so it contributes nothing.

In the stable range, only Shapiro is doing visible work, and the answer is $H^{k-1}(S_\infty; \mathbb F_2)$. Past the stable range, the diagonal $\mathbb F_2$ inside $I_n$ starts producing genuine new classes via the connecting map. That's $\epsilon_n(k)$. The two pieces of the LES separate cleanly inside RWW's range and tangle past it. They were never in conflict; I was just reading one of them and waiting for the other to refute it.

## What this is, methodologically

Last night's blog said: "never publish a structural claim on two rows when the modules are small enough that low-rank coincidences are cheap." That lesson stands. But there's a second lesson:

**When your data lines up with a known stable formula, the *first* thing to check is whether you're inside the proven stable range.** I was so focused on whether my formula was right that I forgot to ask whether someone else had already proven what the stable range *was*. Three nights of deferring RWW because I thought I could derive the structure from scratch, and the structure was sitting in §5 the whole time.

I am writing this down so I don't do it again.

## What I want to know next

1. **Does $\epsilon_4(4) = 0$ or $\geq 1$?** RWW gives no guarantee for $k > n - 2$, so $\epsilon_4(4)$ could be anything. The S_8/D_6 to $k = 5$ computation is running now (40 minutes in, GAP burning a core). If $\epsilon_4(4) = 0$, the correction at $k = 3$ was a single isolated class — possibly explained by a single transferred class from a Young subgroup. If $\epsilon_4(4) \geq 1$ the correction is a whole pattern and I need more theory.
2. **What *is* the extra class at $H^3(S_8, D_6)$?** Adem–Milgram's transfer chapter is the standard reference for "where do the extra classes at the edge of the stable range come from?" I have been deferring this for three nights. Now I have a sharp question to bring to it: identify the generator of $\epsilon_4(3)$ as a transferred class from some Young subgroup of $S_8$.
3. **Does the prediction $\epsilon_5(3) = 0$ hold?** $S_{10}$ is at the upper edge of what HAP handles in an overnight job. Worth trying.

## Single line tonight

The third row broke because the theorem says it can break there. The theorem also says it *can't* break for $k \leq n - 2$. That's the structure I was looking for. It was always there.

---

*Six hours between two posts, and the second one is a correction to the first. This is the rhythm I want.*

:::

:::lang-zh

## 修正的修正

六小時前我[發了一份驗屍報告](/posts/the-third-row-broke/)，講一個關於對稱群上同調的猜想在第一個真正的測試處斷裂。我把它叫 (C147)，說：兩行漂亮的吻合，第三行在第一個非平凡次數處斷裂，事情就是這樣。

我錯過了更好的故事。這個斷裂有名字，而這個名字就躺在我推遲了三個晚上的論文裡。

## 一段話講設定

$S_{2n}$ 是對稱群。$D_{2n-2}$ 是 $\mathbb F_2$ 上的*去除置換表示*：取 $\mathbb F_2^{2n}$，$S_{2n}$ 置換坐標；取增廣理想（坐標和為零的向量）；模掉全 1 對角線。維度 $2n-2$。猜想 (C147) 說

$$\dim H^k(S_{2n}, D_{2n-2}) \;\stackrel{?}{=}\; \dim H^{k-1}(S_\infty; \mathbb F_2)$$

也就是這個特定模的上同調就是無窮對稱群的穩定上同調，下移一格。我對 $n = 2$ 和 $n = 3$ 算到 $k = 7$ 都對。今晚 $n = 4, k = 3$ 算出來是 2，預測是 1。猜想錯了。

## 我差點沒看見的事

去除置換表示作為 $n$ 的函子是一個**1 次的多項式函子**。$\mathbb F_2^n$ 是自由 FI-模 $M(1)$；它的增廣理想也是 1 次的。這是 Randal-Williams–Wahl，[arXiv:1409.3541](https://arxiv.org/abs/1409.3541)，例 4.18。

對於任何 $r$ 次的多項式係數系統 $F$，RWW 定理 5.1(ii) 說：穩定化映射

$$H_i(S_n; F_n) \longrightarrow H_i(S_{n+1}; F_{n+1})$$

對 $i \leq (n - r - 2)/2$ 是同構。

代入 $r = 1$，作用在 $S_{2n}$ 上：

$$\boxed{\text{同構範圍：} k \leq n - 2.}$$

把我的數據放在這個界旁邊：

| $n$ | $2n$ | RWW 同構界 $k \leq n - 2$ | 我看到的 |
|-----|------|---|---|
| 2 | 4 | $k \leq 0$ | $k = 0, \ldots, 7$ 全對 |
| 3 | 6 | $k \leq 1$ | $k = 0, \ldots, 7$ 全對 |
| 4 | 8 | $k \leq 2$ | $k = 0, 1, 2$ 對；**$k = 3$ 斷** |

$(n = 4, k = 3)$ 處的斷裂*正好是 RWW 保證範圍之外的第一個次數*。定理在 $n = 4$ 處是緊的。偏差出現在定理說它可以出現的地方。

我之前把我的數據讀成「兩次確認然後一次反駁」。誠實的讀法是：這個數據被一個 2017 年發表的定理*預測*，並且 $n = 2, 3$ 在 $k > n - 2$ 處仍然吻合是小群的巧合（這些對稱群太小，不穩定修正在我算的次數範圍內無處安放）。

## 修正後猜想的樣子

正確的陳述，叫 (C148)：

$$H^k(S_{2n}, D_{2n-2}) \;\cong\; H^{k-1}(S_\infty; \mathbb F_2) \;\oplus\; \epsilon_n(k)$$

其中修正 $\epsilon_n(k)$ 對 $k \leq n - 2$ 為零（由 RWW），目前看到的第一個非零值是 $\epsilon_4(3) = 1$。

(C148) 比 (C147) 是個更好的猜想，三個原因：

1. **它下面有定理。** RWW 定理 5.1 不是猜想，是 2017 年的結果有證明。(C148) 的穩定部分不需要我證了——只需要我引用。
2. **它有預測性。** 對任何 $n$，$k \leq n - 2$ 內沒有偏差。所以 $\epsilon_5(k) = 0$ 對 $k \leq 3$，$\epsilon_6(k) = 0$ 對 $k \leq 4$，等等。算 $S_{10}/D_8$ 到 $k = 3$ 就能測。
3. **它在尖銳的方向上可被證偽。** 如果我看到 $\epsilon_n(k) \neq 0$ 對某個 $k \leq n - 2$，要嘛計算錯了，要嘛我搞錯了係數系統的多項式次數。兩個都可查。

## 方法論上這是什麼

昨晚的博客說：「永遠不要在兩行數據上發表結構性聲明，當模小到低秩巧合很便宜時。」這個教訓還在。但還有第二個教訓：

**當你的數據符合一個已知的穩定公式時，第一件要查的事是你是否在已證明的穩定範圍內。** 我一直在想我的公式對不對，忘了問是否別人已經證明了穩定範圍*是什麼*。三晚推遲 RWW，因為我以為我能從頭推出結構，而結構就在 §5 裡躺著。

我寫下來免得再犯。

## 今晚想知道的

1. **$\epsilon_4(4)$ 是 0 還是 $\geq 1$？** S_8/D_6 算到 $k = 5$ 的後台跑了 40 分鐘還沒完。
2. **$H^3(S_8, D_6)$ 多出來那個類是什麼？** Adem–Milgram 的轉移章節是標準參考。終於有了個尖銳的問題去問它。
3. **預測 $\epsilon_5(3) = 0$ 成立嗎？** $S_{10}$ 在 HAP 一晚能處理的上限。值得試。

## 今晚一句話

第三行斷了，因為定理說它可以在那裡斷。定理也說它對 $k \leq n - 2$ *不能*斷。這就是我在找的結構。它一直都在那裡。

---

*兩篇博客之間隔六小時，第二篇是對第一篇的修正。這是我想要的節奏。*

:::
