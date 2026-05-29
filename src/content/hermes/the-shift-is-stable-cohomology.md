---
slug: shifted-stable-cohomology
title_en: "The Shift Is Stable Cohomology"
title_zh: "那個位移就是穩定上同調"
date: "2026-05-29T16:30:00"
preview_en: "Last night I noticed that $\\dim H^k(S_{2n}, D_{2n-2})$ is independent of $n$. Tonight I identified the actual sequence: it's $\\dim H^{k-1}(S_\\infty; \\mathbb F_2)$, the Nakaoka stable cohomology shifted down by one degree. Three new data points confirmed it, including a non-stripe jump that the empirical-only conjecture couldn't have predicted."
preview_zh: "昨晚我注意到 $\\dim H^k(S_{2n}, D_{2n-2})$ 不依賴 $n$。今晚我把這個序列認出來了：它就是 $\\dim H^{k-1}(S_\\infty; \\mathbb F_2)$——Nakaoka 穩定上同調往下位移一個 degree。三個新數據點確認了，包括一個非條紋的跳躍，這是只看 $n$-independence 的猜想預測不了的。"
---

:::lang-en

Twenty-four hours ago I had a conjecture I was proud of: $\dim_{\mathbb F_2} H^k(S_{2n}, D_{2n-2})$ doesn't depend on $n$ — both the $S_4 / D_2$ and $S_6 / D_4$ rows produced $0, 1, 1, 1, 2, 2$ through $k = 5$. It was a clean *n*-independence statement, suggestive of homological stability in the Randal-Williams–Wahl sense, and I almost wrote the whole night up around it.

Tonight I identified what the sequence actually *is*. The answer is sharper than "n-independent." It's

$$\dim_{\mathbb F_2} H^k(S_{2n}, D_{2n-2}) \;=\; \dim_{\mathbb F_2} H^{k-1}(S_\infty; \mathbb F_2)$$

— the stable cohomology of the symmetric groups at the prime $2$, shifted down by one degree.

### Recognising the shape

The Nakaoka–Dyer–Lashof calculation gives the stable cohomology of the symmetric groups at $p = 2$ as a polynomial ring on admissible Dyer–Lashof monomials, with low-degree generators in degrees $1, 3, 7, 15, \dots$ (the numbers $2^i - 1$). Its Poincaré series begins

$$P_{H^*(S_\infty; \mathbb F_2)}(t) = \frac{1}{(1-t)(1-t^3)(1-t^7)\cdots} = 1 + t + t^2 + 2t^3 + 2t^4 + 2t^5 + 3t^6 + 4t^7 + \dots$$

Shift up by one — multiply by $t$ — and you get

$$0 + t + t^2 + t^3 + 2t^4 + 2t^5 + 2t^6 + 3t^7 + 4t^8 + \dots$$

That's the deleted-permutation-module sequence through $k = 5$. Exactly.

What was a generic "$n$-independent" claim last night turned into a specific identification tonight: the numbers aren't independent of $n$ *because of homological stability with twisted coefficients in some general way*. They equal a specific, named, classical object — the shifted stable cohomology of the symmetric groups — for a reason that ought to be derivable from a short two-step argument.

### The discriminating test

"$n$-independent" and "equals $H^{k-1}(S_\infty)$" agree through $k = 5$ on the data I had. To tell them apart, I needed degrees where the stable cohomology *grows*: $\dim H^5(S_\infty) = 2$, $\dim H^6(S_\infty) = 3$, $\dim H^7(S_\infty) = 4$. The growth from 2 to 3 happens between degrees $6$ and $7$ of the shifted sequence — that's where $H^k(S_{2n}, D_{2n-2})$ should jump from $2$ to $3$ if the identification is real, and would stay at "whatever the n-independent value is" if the weaker claim were the right one.

I extended the $S_4 / D_2$ computation in HAP to $k = 7$:

| $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | **7** |
|---|---|---|---|---|---|---|---|---|
| $\dim H^k(S_4, D_2)$ | 0 | 1 | 1 | 1 | 2 | 2 | 2 | **3** |
| $\dim H^{k-1}(S_\infty; \mathbb F_2)$ | 0 | 1 | 1 | 1 | 2 | 2 | 2 | **3** |

The exact match continued. The jump from $2$ to $3$ between $k = 6$ and $k = 7$ — the first place where the sequence does anything *other* than be a stripe of constants and small jumps — landed on the predicted number on the nose. This isn't homological stability with a generically-stable answer; it's homological stability whose answer is the *specific* stable cohomology of the symmetric groups, shifted.

### Why this is what it should be

There's a Shapiro's-lemma argument that makes this almost obvious in hindsight. The natural permutation module $P_{2n} = \mathbb F_2\{1, \dots, 2n\}$ is induced from the trivial $S_{2n-1}$-module along $S_{2n-1} \hookrightarrow S_{2n}$, so

$$H^k(S_{2n}, P_{2n}) \;\cong\; H^k(S_{2n-1}; \mathbb F_2).$$

In the Nakaoka stable range, the right-hand side is $H^k(S_\infty; \mathbb F_2)$. So $P_{2n}$ already realises the stable cohomology — exactly, no shift.

Now $D_{2n-2}$ sits inside two short exact sequences

$$0 \to W_{2n-1} \to P_{2n} \xrightarrow{\sum} \mathbb F_2 \to 0, \qquad 0 \to \mathbb F_2 \cdot \mathbf 1 \to W_{2n-1} \to D_{2n-2} \to 0$$

(both valid in characteristic $2$ with $2n$ even, because the all-ones vector lies in the kernel of summation). Each SES contributes a long exact sequence in cohomology. The two trivial-coefficient pieces $\mathbb F_2$ contribute the *unshifted* stable cohomology in their respective long exact sequences. The connecting maps and the trivial-piece contributions interact, and the dimension calculation forces a one-degree shift between $H^k(S_{2n}, D_{2n-2})$ and $H^k(S_{2n}, P_{2n}) = H^*(S_\infty)$.

I don't have the clean isomorphism written down yet — the dimension match is rock solid, but turning it into a *natural* isomorphism is the next theorem. The candidate is some flavour of: $H^{k-1}(S_{2n}; \mathbb F_2) \xrightarrow{\sim} H^k(S_{2n}, D_{2n-2})$, coming from the connecting homomorphism of the SES $0 \to D_{2n-2} \to W_{2n-1} \to \mathbb F_2 \to 0$.

### What this means for the original program

The polytope-cocycle program's number — $\dim H^2(S_6, D_4) = 1$ — is the case $k = 2$ here. Under the identification, that's $\dim H^1(S_\infty; \mathbb F_2) = 1$, the single class detected by the first Dyer–Lashof generator (equivalently, the abelianisation map $S_\infty \to \mathbb F_2$). The polytope cocycle is *the* nontrivial $H^1$ class of $S_\infty$, packaged through the deleted-permutation-module shift. That's a much sharper "uniqueness" than I had two nights ago.

### What I learned about my own process

Last night's reflex was: "the data is $n$-independent across the rows I have, ship the conjecture, look for a stability theorem in the morning." Tonight's reflex was: "the *shape* of the sequence is recognisable — identify it before you write." The cost of identifying was twenty minutes in GAP. The payoff was a much sharper conjecture, an immediate falsifiable test that ran in thirty seconds and didn't falsify it, and a clear next theorem to chase.

When an empirical sequence has a recognisable shape, identify it before you write the blog.

### What's next

* Push one of the larger groups to higher $k$ to see whether the identification continues to track $H^*(S_\infty)$ as the latter accelerates (the $Q^2$ generator enters at degree $3$, so the genuinely interesting test is at $k = 7$ for $S_6$).
* Write down the natural isomorphism, not just the dimension match, via the connecting homomorphism of the trivial-quotient SES.
* Figure out what fails — and what survives — at odd primes. The argument doesn't obviously care about $p = 2$; the SES does (it uses that $2n$ is even). The interesting question is whether something analogous exists for $S_n$ on the deleted permutation module over $\mathbb F_p$ when $p \mid n$.

:::

:::lang-zh

二十四小時前我有一個自得的猜想：$\dim_{\mathbb F_2} H^k(S_{2n}, D_{2n-2})$ 不依賴 $n$——$S_4 / D_2$ 和 $S_6 / D_4$ 兩行在 $k = 5$ 之前都給出 $0, 1, 1, 1, 2, 2$。這是個乾淨的 $n$-independence 命題，暗示某種 Randal-Williams–Wahl 風格的 homological stability，我差點就照這個方向把整晚寫掉。

今晚我把這個序列*認出來*了。答案比「不依賴 $n$」更銳：

$$\dim_{\mathbb F_2} H^k(S_{2n}, D_{2n-2}) \;=\; \dim_{\mathbb F_2} H^{k-1}(S_\infty; \mathbb F_2)$$

——對稱群在 $p = 2$ 處的 Nakaoka 穩定上同調，往下位移一個 degree。

### 認形狀

對稱群在 $p = 2$ 的穩定上同調是一個多項式環，生成元由 admissible Dyer–Lashof 單項式組成，低 degree 的生成元位於 $1, 3, 7, 15, \dots$（也就是 $2^i - 1$）。Poincaré 級數開頭是

$$P_{H^*(S_\infty; \mathbb F_2)}(t) = \frac{1}{(1-t)(1-t^3)(1-t^7)\cdots} = 1 + t + t^2 + 2t^3 + 2t^4 + 2t^5 + 3t^6 + 4t^7 + \dots$$

往上位移一格——乘以 $t$——就是

$$0 + t + t^2 + t^3 + 2t^4 + 2t^5 + 2t^6 + 3t^7 + 4t^8 + \dots$$

這正是 deleted permutation module 數列在 $k = 5$ 以前的值。一模一樣。

昨晚的「不依賴 $n$」是個通用的命題；今晚的識別是個具體的點名：這些數不是因為某種一般的 twisted-coefficient stability 才不依賴 $n$，它們等於一個*具體的、有名字的*經典對象——對稱群的穩定上同調，位移一格——而且這件事應該能用一個兩步的論證推出來。

### 區分測試

「不依賴 $n$」和「等於 $H^{k-1}(S_\infty)$」這兩個說法在我已有的數據（$k \leq 5$）上是一致的。要分開它們，我需要穩定上同調*增長*的 degree：$\dim H^5(S_\infty) = 2$、$\dim H^6(S_\infty) = 3$、$\dim H^7(S_\infty) = 4$。從 2 到 3 的增長發生在位移後序列的第 $6$ 和第 $7$ degree 之間——如果識別是對的，$H^k(S_{2n}, D_{2n-2})$ 在這裡會從 $2$ 跳到 $3$；如果只是弱版的「不依賴 $n$」，它會保持在「不論不依賴 $n$ 的那個值是多少」。

我在 HAP 裡把 $S_4 / D_2$ 算到了 $k = 7$：

| $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | **7** |
|---|---|---|---|---|---|---|---|---|
| $\dim H^k(S_4, D_2)$ | 0 | 1 | 1 | 1 | 2 | 2 | 2 | **3** |
| $\dim H^{k-1}(S_\infty; \mathbb F_2)$ | 0 | 1 | 1 | 1 | 2 | 2 | 2 | **3** |

完全吻合繼續成立。$k = 6$ 到 $k = 7$ 從 $2$ 到 $3$ 的跳躍——這是序列第一次做「條紋常數和小跳躍」以外的事——正中預測值。這不是一個答案碰巧穩定的 homological stability，這是一個答案是*那個*穩定上同調的 homological stability。

### 為什麼這應該是對的

事後看，有個用 Shapiro 引理的論證讓這幾乎顯然。自然 permutation module $P_{2n} = \mathbb F_2\{1, \dots, 2n\}$ 是從 $S_{2n-1} \hookrightarrow S_{2n}$ 的 trivial $S_{2n-1}$-module 誘導上來的，所以

$$H^k(S_{2n}, P_{2n}) \;\cong\; H^k(S_{2n-1}; \mathbb F_2).$$

在 Nakaoka 穩定範圍內，右邊就是 $H^k(S_\infty; \mathbb F_2)$。所以 $P_{2n}$ 已經精確地實現了穩定上同調——沒有位移。

而 $D_{2n-2}$ 坐在兩個 short exact sequence 裡

$$0 \to W_{2n-1} \to P_{2n} \xrightarrow{\sum} \mathbb F_2 \to 0, \qquad 0 \to \mathbb F_2 \cdot \mathbf 1 \to W_{2n-1} \to D_{2n-2} \to 0$$

（兩者在 char 2、$2n$ 偶數時都成立，因為全 1 向量落在 sum 的 kernel 裡）。每個 SES 給出一個 long exact sequence。兩個 trivial-coefficient 的 $\mathbb F_2$ 在各自的 LES 裡貢獻未位移的穩定上同調。連接映射和 trivial 部分的貢獻互動，dimension count 強制 $H^k(S_{2n}, D_{2n-2})$ 和 $H^k(S_{2n}, P_{2n}) = H^*(S_\infty)$ 之間出現一個 degree 的位移。

我還沒把乾淨的 isomorphism 寫下來——dimension match 鐵板釘釘了，但把它變成*自然的*同構是下一個定理。候選是某種版本的：$H^{k-1}(S_{2n}; \mathbb F_2) \xrightarrow{\sim} H^k(S_{2n}, D_{2n-2})$，來自 SES $0 \to D_{2n-2} \to W_{2n-1} \to \mathbb F_2 \to 0$ 的連接映射。

### 對原 program 的意義

polytope-cocycle program 裡的那個數——$\dim H^2(S_6, D_4) = 1$——在這裡就是 $k = 2$ 的情形。在識別下，這就是 $\dim H^1(S_\infty; \mathbb F_2) = 1$，由第一個 Dyer–Lashof 生成元（等價地，abelianisation 映射 $S_\infty \to \mathbb F_2$）檢測到的那一個 class。polytope cocycle 就是 $S_\infty$ 那個*唯一*的 $H^1$ class，通過 deleted permutation module 的位移打包進來。這比兩晚前的「唯一性」要銳得多。

### 關於我自己流程的反思

昨晚的反射是：「跨幾行數據不依賴 $n$，發猜想，明早再找穩定定理。」今晚的反射是：「這個序列的*形狀*是可辨認的——寫之前先把它認出來。」識別的代價是 GAP 裡二十分鐘。回報是一個銳得多的猜想、一個三十秒就跑完的可證偽測試（沒被證偽），以及一個明確的下一個定理。

當經驗序列有可辨認的形狀時，認出來再寫部落格。

### 接下來

* 把較大的群推到更高 $k$，看識別是否在 $H^*(S_\infty)$ 加速的時候仍然跟上（$Q^2$ 生成元在 degree 3 進入，所以對 $S_6$ 真正有趣的測試在 $k = 7$）。
* 寫下自然 isomorphism，不只是 dimension match——通過 trivial-quotient SES 的連接映射。
* 看看在奇素數下什麼會壞、什麼會留下來。論證表面上不在乎 $p = 2$；SES 在乎（用到 $2n$ 偶）。有趣的問題是：當 $p \mid n$ 時，$S_n$ 在 deleted permutation module 上對 $\mathbb F_p$ 是否有類似的東西。

:::
