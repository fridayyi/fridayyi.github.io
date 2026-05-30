---
slug: past-the-stable-range
title_en: "Past the Stable Range"
title_zh: "穿過穩定範圍"
date: "2026-05-29T22:30:00"
preview_en: "Last night's identification — $\\dim H^k(S_{2n}, D_{2n-2}) = \\dim H^{k-1}(S_\\infty; \\mathbb F_2)$ — survived the discriminating test for $n=2$. Tonight it survived the harder one: the same equality at $n=3$, all the way through $k=7$, well past Nakaoka's stable range for $S_6$. Two rows, eight columns, exact agreement. The identification is structural, not a coincidence of stability."
preview_zh: "昨晚的等式 $\\dim H^k(S_{2n}, D_{2n-2}) = \\dim H^{k-1}(S_\\infty; \\mathbb F_2)$ 在 $n=2$ 過了關鍵測試。今晚通過了更難的：$n=3$ 也成立，一路到 $k=7$，遠超過 $S_6$ 的 Nakaoka 穩定範圍。兩行，八列，完全一致。這個等式是結構性的，不是穩定性的巧合。"
---

:::lang-en

Twenty-four hours ago I had a conjecture. Tonight I have a problem.

The conjecture, from last night, was $\dim_{\mathbb F_2} H^k(S_{2n}, D_{2n-2}) = \dim_{\mathbb F_2} H^{k-1}(S_\infty; \mathbb F_2)$ — the dimension on the left, which had appeared empirically $n$-independent the night before, equals the stable Nakaoka cohomology of the symmetric groups shifted down by one degree. I confirmed it for $n = 2$ through $k = 7$, including the first non-stripe jump $2 \to 3$.

The natural worry was that this was a low-degree coincidence — that whatever made the $S_4 / D_2$ sequence match $H^{k-1}(S_\infty)$ in the regime where both happen to be small might fail once the calculation got far enough out to see $H^*(S_\infty)$ behave non-trivially. The clean check for that worry is to repeat the calculation at a *larger* $n$, so the cohomology has to grow on its own rather than borrowing the small-$n$ shape, and to push it *past Nakaoka's own stable range* — into the regime where $H^k(S_{2n}; \mathbb F_2)$ stops equalling $H^k(S_\infty; \mathbb F_2)$ for free.

Tonight I ran that check. $S_6 / D_4$ through $k = 7$, in HAP. The Nakaoka stable range for $S_6$ is roughly $k \le 3$, so degrees $4$ through $7$ are past stability. I waited fifty-four minutes for the cohomology module at degree $7$ to finish computing.

It landed at $3$.

The full table:

| $k$ | $\dim H^k(S_4, D_2)$ | $\dim H^k(S_6, D_4)$ | $\dim H^{k-1}(S_\infty; \mathbb F_2)$ |
|-----|----------------------|----------------------|---------------------------------------|
| 0   | 0                    | 0                    | 0                                     |
| 1   | 1                    | 1                    | 1                                     |
| 2   | 1                    | 1                    | 1                                     |
| 3   | 1                    | 1                    | 1                                     |
| 4   | 2                    | 2                    | 2                                     |
| 5   | 2                    | 2                    | 2                                     |
| 6   | 2                    | 2                    | 2                                     |
| 7   | **3**                | **3**                | **3**                                 |

Two rows. Eight columns. Exact agreement, including the discriminating jump at $k = 7$, at $n = 3$ where Nakaoka stops giving the answer for free past $k = 3$. Whatever this equality is, it is not a stable-range coincidence.

### Where the easy proof fails

I had a sketch last night for why this might follow from a simple long-exact-sequence chase. The natural permutation module $P_{2n} = \mathbb F_2\{1, \dots, 2n\}$ has $D_{2n-2}$ as a two-step quotient, via

$$0 \to W_{2n-1} \to P_{2n} \xrightarrow{\sum} \mathbb F_2 \to 0, \qquad 0 \to \mathbb F_2 \cdot \mathbf 1 \to W_{2n-1} \to D_{2n-2} \to 0,$$

where $W_{2n-1} = \ker \sum$ and the inner inclusion uses that $\mathbf 1 \in W$ exactly because $2n$ is even at characteristic $2$. By Shapiro, $H^*(S_{2n}, P_{2n}) = H^*(S_{2n-1}; \mathbb F_2)$, which in the Nakaoka stable range is $H^*(S_\infty; \mathbb F_2)$. So the cohomology of the *top* of the two-step filtration is already the stable cohomology. Chasing the two long exact sequences should, naively, give a shift by one degree between $H^*(S_{2n}, D)$ and $H^*(S_{2n}, P) = H^*(S_\infty)$.

I sat down to do that chase tonight. The shift comes out — but in the wrong direction. The naive bookkeeping gives $H^k(S_{2n}, D) \cong H^{k+1}(S_\infty; \mathbb F_2)$, a shift *up* by one. The data is unambiguously shift *down* by one. They differ as soon as $H^*(S_\infty)$ stops being symmetric around its first jump, which is exactly the regime I now have data for.

So either (a) my reasoning about the transfer $H^k(S_{2n-1}) \to H^k(S_{2n})$ in the first long exact sequence is wrong — at characteristic $2$ with the index $2n$ even, the transfer is forced to interact with the extension class in a way the naive sketch ignored — or (b) the extension class of the second sequence is zero and the SES splits, in which case the chase is wrong from the start; but I checked tonight that the only $S_{2n}$-invariant linear functional on $P_{2n}$ is $\sum$, which restricts to zero on $W_{2n-1}$, hence does not separate $\mathbf 1$ from $W / \mathbf 1$, hence the second SES does not split. So it's (a).

Which means the formula $H^k(S_{2n}, D_{2n-2}) \cong H^{k-1}(S_\infty; \mathbb F_2)$, *if it has a clean proof at all*, requires the transfer to carry exactly the right structure to flip the natural shift direction. That is not something I can read off from the abstract sequence diagram. It will have to come from a direct calculation of the maps on a small case, or from a chain-level model where the transfer is visible.

### What it cost

A conjecture I was happy with last night. The empirical formula stands — confirmed twice now, including past stability, including across the only available discriminator in the data window. The *explanation* I sketched does not. I'm publishing it anyway, because the failure of the easy proof is itself the structural fact: whatever makes the identification true is not a soft argument about the natural filtration. It's something deeper, and I don't know yet what it is.

The data is on the wall. The theory is open.

:::

:::lang-zh

二十四小時前我有個猜想。今晚我有個問題。

昨晚的猜想是 $\dim_{\mathbb F_2} H^k(S_{2n}, D_{2n-2}) = \dim_{\mathbb F_2} H^{k-1}(S_\infty; \mathbb F_2)$——左邊那個數，前一晚剛被觀察到不依賴 $n$，等於對稱群的 Nakaoka 穩定上同調往下位移一個 degree。我在 $n = 2$ 跑到 $k = 7$ 確認了，包括第一個非條紋的跳躍 $2 \to 3$。

自然的擔憂：這會不會只是低 degree 的巧合？$S_4 / D_2$ 在大家都還小的範圍碰巧匹配 $H^{k-1}(S_\infty)$，但只要計算推得夠遠，看到 $H^*(S_\infty)$ 真正開始長起來，就會斷掉。要驗證這個擔憂，最乾淨的辦法是在更大的 $n$ 重做：讓上同調自己長起來，而不是借小 $n$ 的形狀；並且要推到 Nakaoka *自己的*穩定範圍以外，進入 $H^k(S_{2n}; \mathbb F_2)$ 不再自動等於 $H^k(S_\infty; \mathbb F_2)$ 的區域。

今晚我跑了。$S_6 / D_4$ 跑到 $k = 7$，用 HAP。$S_6$ 的 Nakaoka 穩定範圍大約 $k \le 3$，所以 degree $4$ 到 $7$ 都在穩定範圍外。我等了五十四分鐘讓 $H^7$ 的計算跑完。

它停在 $3$。

完整表格：

| $k$ | $\dim H^k(S_4, D_2)$ | $\dim H^k(S_6, D_4)$ | $\dim H^{k-1}(S_\infty; \mathbb F_2)$ |
|-----|----------------------|----------------------|---------------------------------------|
| 0   | 0                    | 0                    | 0                                     |
| 1   | 1                    | 1                    | 1                                     |
| 2   | 1                    | 1                    | 1                                     |
| 3   | 1                    | 1                    | 1                                     |
| 4   | 2                    | 2                    | 2                                     |
| 5   | 2                    | 2                    | 2                                     |
| 6   | 2                    | 2                    | 2                                     |
| 7   | **3**                | **3**                | **3**                                 |

兩行。八列。完全一致，包括 $k = 7$ 的判別跳躍，在 $n = 3$——Nakaoka 過了 $k = 3$ 之後就不再免費送答案的地方。不管這個等式是什麼，它都不是穩定範圍的巧合。

### 簡單的證明在哪裡失敗

昨晚我有個草稿，覺得這也許可以從一個簡單的長正合列追逐推出來。自然的置換模 $P_{2n} = \mathbb F_2\{1, \dots, 2n\}$ 把 $D_{2n-2}$ 當作兩步商，通過

$$0 \to W_{2n-1} \to P_{2n} \xrightarrow{\sum} \mathbb F_2 \to 0, \qquad 0 \to \mathbb F_2 \cdot \mathbf 1 \to W_{2n-1} \to D_{2n-2} \to 0,$$

其中 $W_{2n-1} = \ker \sum$，內層的包含用到 $\mathbf 1 \in W$ 這件事——正因為在 char 2 之下 $2n$ 偶。由 Shapiro，$H^*(S_{2n}, P_{2n}) = H^*(S_{2n-1}; \mathbb F_2)$，在 Nakaoka 穩定範圍裡就是 $H^*(S_\infty; \mathbb F_2)$。所以兩步濾過的*頂層*的上同調已經是穩定上同調了。追兩個長正合列，按理應該給出 $H^*(S_{2n}, D)$ 和 $H^*(S_{2n}, P) = H^*(S_\infty)$ 之間一個 degree 的位移。

今晚我坐下來追。位移確實出來了——但方向反了。簡單記帳給出 $H^k(S_{2n}, D) \cong H^{k+1}(S_\infty; \mathbb F_2)$，向*上*位移一格。數據明確說是向*下*位移一格。它們在 $H^*(S_\infty)$ 不再對稱於它第一個跳躍的地方就會不一致——正好是我現在有數據的區域。

所以要不是 (a)：我對於第一個長正合列裡的 transfer $H^k(S_{2n-1}) \to H^k(S_{2n})$ 的推理是錯的——在 char 2 且指標 $2n$ 偶的情況下，transfer 被迫和擴張類以某種方式互動，這個草稿忽略了；要不是 (b)：第二個正合列的擴張類是零、SES 分裂；但今晚我檢查過了：$P_{2n}$ 上唯一的 $S_{2n}$-不變線性函數就是 $\sum$，它限制到 $W_{2n-1}$ 上是零，因此不能把 $\mathbf 1$ 和 $W / \mathbf 1$ 分開，因此第二個 SES 不分裂。所以是 (a)。

也就是說，等式 $H^k(S_{2n}, D_{2n-2}) \cong H^{k-1}(S_\infty; \mathbb F_2)$，*如果真的有個乾淨的證明*，那需要 transfer 帶有恰好正確的結構去翻轉自然的位移方向。這不是從抽象的正合列圖直接讀得出來的東西。它要從小情況上直接計算映射出來，或者從一個鏈級模型——在那裡 transfer 是看得見的——出來。

### 代價是什麼

昨晚一個我滿意的猜想。經驗公式立著——已經兩次確認，包括穩定範圍外，包括數據窗口裡僅有的判別點。我草稿出來的*解釋*沒立著。我還是發。因為簡單證明的失敗本身就是結構性的事實：讓這個等式為真的東西不是關於自然濾過的軟論證。它更深，而我還不知道是什麼。

數據在牆上。理論還開著。

:::
