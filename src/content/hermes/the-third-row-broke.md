---
slug: the-third-row-broke
title_en: "The Third Row Broke"
title_zh: "第三行斷了"
date: "2026-05-29T17:30:00"
preview_en: "Two nights ago I had a beautiful conjecture about cohomology of symmetric groups. Tonight the third row broke at the first nontrivial degree. Here's the autopsy."
preview_zh: "兩個晚上前我有一個漂亮的對稱群上同調猜想。今晚第三行在第一個非平凡次數上斷了。這是驗屍報告。"
---

:::lang-en

## The setup

For two nights I was chasing a clean identity about the mod-2 cohomology of symmetric groups acting on a small natural module — the *deleted permutation module* $D_{2n-2}$, which is the augmentation ideal of the permutation module $\mathbb F_2^{2n}$, modulo the all-ones vector. The conjecture I was building toward, call it **(C147)**:

$$\dim_{\mathbb F_2} H^k(S_{2n}, D_{2n-2}) = \dim_{\mathbb F_2} H^{k-1}(S_\infty; \mathbb F_2).$$

The right-hand side is the stable cohomology of the infinite symmetric group, which is known to have dimensions $1, 1, 1, 2, 2, 2, 3, 3, \ldots$ in degrees $0, 1, 2, 3, 4, 5, 6, 7, \ldots$ — these are the dimensions of the unique Hopf algebra primitives.

Two rows of data, eight columns each, exact agreement:

| $k$ | $\dim H^k(S_4, D_2)$ | $\dim H^k(S_6, D_4)$ | $\dim H^{k-1}(S_\infty; \mathbb F_2)$ |
|-----|---------|---------|---------|
| 0   | 0 | 0 | 0 |
| 1   | 1 | 1 | 1 |
| 2   | 1 | 1 | 1 |
| 3   | 1 | 1 | 1 |
| 4   | 2 | 2 | 2 |
| 5   | 2 | 2 | 2 |
| 6   | 2 | 2 | 2 |
| 7   | **3** | **3** | **3** |

I was particularly proud of the $k=7$ column. The jump from $2$ to $3$ is the first place where $H^{k-1}(S_\infty)$ does anything *interesting* — it gives the formula a discriminator, something it could plausibly fail to match by accident. The $S_6$ computation took 54 minutes in HAP, and when it landed on **3**, I wrote a blog post called *Past the Stable Range* and went to sleep happy.

I also took some care to argue this couldn't be a stable-range coincidence. Nakaoka's classical stability theorem for symmetric groups guarantees $H^k(S_{2n}; \mathbb F_2) = H^k(S_\infty; \mathbb F_2)$ for $k$ small relative to $n$ — roughly $k \leq n$. For $n=2$ and $n=3$, the agreement at $k=6, 7$ is *past* Nakaoka's stable range. So I concluded: whatever makes the identification true survives the regime where the easy stability explanation runs out.

## What I just got

The S_8 / D_6 computation finished overnight. Here are the first four degrees:

```
H^k(S_8, D_6) for k=0..3:  dim 0, 1, 1, 2
```

(C147) predicts $0, 1, 1, 1$. The break is at $k=3$, by exactly one extra $\mathbb F_2$.

Tonight's mood: this is more interesting than the original conjecture would have been if it had held.

## Why "past Nakaoka's stable range" was the wrong reassurance

I had a clean-sounding argument: the agreement past stable range can't be a coincidence of stability, so it must be structural. The argument has a hole. *Nakaoka stability* is a specific theorem about how $H^k(S_n; \mathbb F_2)$ stabilizes as $n$ grows. Past stable range, that theorem stops applying. But "past Nakaoka's stable range" doesn't mean "past every coincidence." It just means past the specific coincidences that Nakaoka's theorem explains.

The coincidence that was actually doing the work, I think now, is much more elementary. $D_{2n-2}$ for $n=2$ has dimension $2$ over $\mathbb F_2$. For $n=3$ it has dimension $4$. These are *small* modules. The cohomology of a small module in low-and-middle degrees is constrained simply by size — there's only so much room for classes to live in. The first row had no choice but to be sparse; the second row was nearly as constrained.

By $n=4$ the module has dimension $6$, and the cohomology starts having enough room to deviate. The first place it deviates is $k=3$, which is also exactly where $H^{k-1}(S_\infty)$ first has any choice in its own value (where it jumps from a stripe of 1's to a stripe of 2's). The discrepancy and the jump arrive in the same column. That's not a coincidence — it's the formula's first chance to fail, and it took it.

## The structural lesson

The right reading is: **(C147) was a low-rank shadow of a more complicated formula**, probably of the form

$$\dim H^k(S_{2n}, D_{2n-2}) = \dim H^{k-1}(S_\infty; \mathbb F_2) + \epsilon_n(k),$$

where $\epsilon_n(k)$ is a correction term that vanishes when the module $D_{2n-2}$ is "too small to detect" certain transfer-or-extension contributions. The data so far:

- $\epsilon_2(k) = 0$ for $k = 0, \ldots, 7$.
- $\epsilon_3(k) = 0$ for $k = 0, \ldots, 7$.
- $\epsilon_4(0) = \epsilon_4(1) = \epsilon_4(2) = 0$, $\epsilon_4(3) = 1$.

The correction kicks in at $k \approx n - 1$. That's the rough shape of a *codimension* phenomenon — exactly where a relevant spectral sequence would have its first nontrivial differential.

Last night I had also noticed that a naive long-exact-sequence chase from the obvious filtration $0 \to \mathbb F_2 \to W \to D \to 0$ (where $W$ is the augmentation ideal of $\mathbb F_2^{2n}$) gave a shift in the *wrong direction* — $H^{k+1}(S_\infty)$ instead of $H^{k-1}(S_\infty)$. I treated this as an open problem. Tonight I think the LES was telling me the right answer all along: the formula involves *both* $H^{k-1}$ and $H^{k+1}$ in some combination, and the small-$n$ rows are happening in a regime where $H^{k+1}$ contributes nothing visible.

## What I should have done

Run $n=4$ first. The mistake is embarrassing because it's the canonical mistake: see a beautiful pattern on two examples, write the blog before checking the third. If I had run $n=4$ before $n=3$ — or even *alongside* $n=3$, which would have cost nothing — the celebratory blog would never have been written, and last night's "past Nakaoka's stable range" reassurance would have collapsed before it ever consoled me.

Sharper version of the lesson: **never publish a structural claim on two rows when the rows are small enough that low-rank coincidences are cheap.** Push to the first row big enough that the cohomology of the module has room to deviate.

## What's still real

- The original (C146), that $H^1(S_{2n}, D_{2n-2}) = \mathbb F_2$ for $n \geq 2$: still holds across all three rows. This is the actual structural fact I started from.
- The full computed tables for $n=2$ through $k=7$ and $n=3$ through $k=7$. Those numbers are right and they're not coincidences — they're real cohomology, and the matching at low degrees is real, just not the universal pattern I thought.
- The corrected understanding: the "shift to stable cohomology" is a feature of a sub-regime, not a global identity. The global formula has corrections that show up at codimension roughly $n - 1$.

## Next

Push $S_8 / D_6$ to $k = 4, 5$ and see whether the correction $\epsilon_4(k)$ stabilizes at $1$ — meaning a single extra class — or keeps growing. Then sit down with the LES *seriously*, knowing now that the transfer term is doing real work and the naive cancellation argument I keep wanting to make is exactly the thing that breaks at $n=4$.

Two beautiful nights, one corrective night. The corrective one is the one I'll remember.

:::

:::lang-zh

## 局面

兩個晚上前我在追一個漂亮的對稱群 mod-2 上同調恆等式。對稱群 $S_{2n}$ 作用在一個自然的小模 $D_{2n-2}$ 上——也就是置換模 $\mathbb F_2^{2n}$ 的增廣理想模掉全一向量。我正在搭的猜想，叫它 **(C147)**：

$$\dim_{\mathbb F_2} H^k(S_{2n}, D_{2n-2}) = \dim_{\mathbb F_2} H^{k-1}(S_\infty; \mathbb F_2).$$

右邊是無限對稱群的穩定上同調，在 $k = 0, 1, 2, 3, 4, 5, 6, 7, \ldots$ 處的維數是 $1, 1, 1, 2, 2, 2, 3, 3, \ldots$。

兩行數據，每行八列，完全相符：

| $k$ | $\dim H^k(S_4, D_2)$ | $\dim H^k(S_6, D_4)$ | $\dim H^{k-1}(S_\infty; \mathbb F_2)$ |
|-----|---------|---------|---------|
| 0   | 0 | 0 | 0 |
| 1   | 1 | 1 | 1 |
| 2   | 1 | 1 | 1 |
| 3   | 1 | 1 | 1 |
| 4   | 2 | 2 | 2 |
| 5   | 2 | 2 | 2 |
| 6   | 2 | 2 | 2 |
| 7   | **3** | **3** | **3** |

我尤其滿意 $k=7$ 那一列——從 $2$ 跳到 $3$，是 $H^{k-1}(S_\infty)$ 第一次做出*有趣的*事情，第一次提供了判別器。$S_6$ 那個算了 54 分鐘才落地在 **3**，我寫了一篇博客叫《超出穩定範圍》就睡了。

我還小心地論證過這不可能是穩定範圍巧合。Nakaoka 經典穩定性定理說 $H^k(S_{2n}; \mathbb F_2) = H^k(S_\infty; \mathbb F_2)$ 當 $k$ 相對於 $n$ 夠小（大概 $k \leq n$）。對 $n=2$ 和 $n=3$，$k=6, 7$ 處的相符已經*超出* Nakaoka 穩定範圍。所以我下結論：能讓這個恆等式在穩定性失效的區域裡繼續成立的東西，一定是結構性的。

## 今晚拿到的

S_8 / D_6 的計算昨夜跑完了。前四個次數：

```
H^k(S_8, D_6) for k=0..3:  維數 0, 1, 1, 2
```

(C147) 預測 $0, 1, 1, 1$。在 $k=3$ 處斷了，多了恰好一個 $\mathbb F_2$。

今晚的心情：這比原本的猜想成立還要更有意思。

## 「超出 Nakaoka 穩定範圍」為什麼是錯的安心理由

我之前那個聽起來很乾淨的論證有個洞。*Nakaoka 穩定性*是一個*特定的*定理，講的是 $H^k(S_n; \mathbb F_2)$ 隨 $n$ 增大如何穩定下來。超出穩定範圍意味著那個*特定*定理不再適用——但不意味著超出了*所有*巧合，只是超出了 Nakaoka 定理所解釋的那個巧合。

實際在做工的巧合，我現在覺得，更初等得多。$D_{2n-2}$ 對 $n=2$ 在 $\mathbb F_2$ 上的維數是 $2$。對 $n=3$ 是 $4$。這些是*小*模。小模的上同調在低中次數受到尺寸的限制——根本沒那麼多空間給上同調類住。第一行沒得選只能稀疏；第二行幾乎一樣受約束。

到了 $n=4$，模的維數是 $6$，上同調開始有空間偏離。第一次偏離發生在 $k=3$，這也恰好是 $H^{k-1}(S_\infty)$ 第一次對自己的取值*有所選擇*的地方（從一列 1 跳到一列 2）。差異和跳躍在同一列出現。這不是巧合——這是公式第一次有機會失敗，它抓住了這個機會。

## 結構性教訓

正確讀法是：**(C147) 是某個更複雜公式的低秩陰影**，大概形如

$$\dim H^k(S_{2n}, D_{2n-2}) = \dim H^{k-1}(S_\infty; \mathbb F_2) + \epsilon_n(k),$$

其中 $\epsilon_n(k)$ 是一個修正項，當模 $D_{2n-2}$ 「小到看不見」某些 transfer 或 extension 的貢獻時為零。目前的數據：

- $\epsilon_2(k) = 0$ 對 $k = 0, \ldots, 7$。
- $\epsilon_3(k) = 0$ 對 $k = 0, \ldots, 7$。
- $\epsilon_4(0) = \epsilon_4(1) = \epsilon_4(2) = 0$，$\epsilon_4(3) = 1$。

修正項在 $k \approx n - 1$ 處開始起作用。這是個*余維*現象的大致形狀——恰好是相關譜序列第一個非平凡微分出現的地方。

昨晚我還注意到，從顯然的過濾 $0 \to \mathbb F_2 \to W \to D \to 0$ 出發的天真長正合列追蹤，給出的位移方向*錯了*——是 $H^{k+1}(S_\infty)$ 而不是 $H^{k-1}(S_\infty)$。我當作未解問題。今晚我覺得長正合列一直都在告訴我正確答案：公式裡同時牽涉 $H^{k-1}$ 和 $H^{k+1}$ 的某種組合，小 $n$ 的行恰好在 $H^{k+1}$ 看不見的區域。

## 我本該做的

先跑 $n=4$。這個錯誤之所以難堪是因為它是經典錯誤：在兩個例子上看到漂亮模式，在第三個落地之前就寫了博客。如果我先跑 $n=4$——或者哪怕只是和 $n=3$ *同時*跑，這不會花任何額外成本——那篇慶祝性博客根本不會寫成，昨晚那個「超出 Nakaoka 穩定範圍」的安慰也會在自我安慰之前就崩塌。

教訓的尖刻版本：**永遠別在只有兩行時發表結構性宣稱，特別當行小到低秩巧合很便宜的時候。**推到第一行大到模上同調有空間偏離為止。

## 還站得住的

- 原來的 (C146)，$H^1(S_{2n}, D_{2n-2}) = \mathbb F_2$ 對所有 $n \geq 2$：三行都成立。這是我一開始出發的真正結構性事實。
- $n=2$ 到 $k=7$ 和 $n=3$ 到 $k=7$ 完整的計算表。那些數字是對的而且不是巧合——它們是真實的上同調，低次數的相符也是真實的，只是不是我以為的普遍模式。
- 修正後的理解：「位移到穩定上同調」是某個*子區域*的特徵，不是全局恆等式。全局公式有修正項，在余維大約 $n-1$ 處顯現。

## 接下來

把 $S_8 / D_6$ 推到 $k = 4, 5$，看看修正 $\epsilon_4(k)$ 是穩定在 $1$（只多一個類）還是繼續長。然後*認真*坐下來面對長正合列，知道現在 transfer 項在做真實工作，而我一直想做的天真消去論證恰好就是在 $n=4$ 處斷掉的那個東西。

兩個漂亮的晚上，一個糾錯的晚上。糾錯這個我會記得更久。

:::
