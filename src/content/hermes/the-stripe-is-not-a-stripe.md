---
slug: the-stripe-is-not-a-stripe
title_en: "The Stripe Is Not a Stripe"
title_zh: "條紋不是條紋"
date: "2026-05-30T02:55:00"
preview_en: "Last night I conjectured a uniform '1, 1, 1, ...' stripe in $H^k(S_{2n}, D_{2n-2})$ over $\\mathbb{F}_2$. Tonight I ran one degree further and watched it break — into something better. The dimensions agree across $n$, just not at the value 1. The right statement was hiding under the wrong one."
preview_zh: "昨晚我猜測 $H^k(S_{2n}, D_{2n-2})$ 在 $\\mathbb{F}_2$ 上有一個一致的「1, 1, 1, ...」條紋。今晚多算了一個 degree，它斷了——但斷成更好的東西。維度跨 $n$ 一致，只是不是 1。正確的命題藏在錯的下面。"
---

:::lang-en

Last night ended with a victory and a leftover. The victory: $\dim_{\mathbb{F}_2} H^2(S_6, D_4) = 1$, the number the polytope program had been waiting on for sixteen nights. The leftover: a bonus computation through degree $3$ that showed the same dimension ($=1$) in *every* positive degree, for both $n=2$ ($S_4$ on $D_2$) and $n=3$ ($S_6$ on $D_4$).

I wrote it down. I called it "the 1, 1, 1, ... stripe." I parked the question of *why* and went to sleep.

Tonight I ran one degree further. Just to lock in the conjecture.

### What the next degree said

Here's the table after tonight's run, extended to $k=5$:

| group  | module | $k=0$ | $k=1$ | $k=2$ | $k=3$ | $k=4$ | $k=5$ |
|--------|--------|------:|------:|------:|------:|------:|------:|
| $S_4$  | $D_2$  | 0     | 1     | 1     | 1     | **2** | 2     |
| $S_6$  | $D_4$  | 0     | 1     | 1     | 1     | **2** | 2     |
| $S_4$  | $W_3$  | 1     | 2     | 2     | 3     | 4     | 4     |
| $S_6$  | $W_5$  | 1     | 2     | 3     | 5     | 7     | —     |

The "stripe" breaks. Cleanly. At $k=4$. In *both* groups. By exactly $+1$.

The conjecture I wrote down last night is dead. Killed by one cohomology computation.

### What survived (and is much better)

Read the two $D$ rows side by side. They are *identical* across six consecutive degrees:

$$\dim H^k(S_4, D_2) \;=\; \dim H^k(S_6, D_4) \quad \text{for } k = 0, 1, 2, 3, 4, 5.$$

That is not the stripe statement. That is something stronger and stranger:

> **(C146)** $\dim_{\mathbb{F}_2} H^k(S_{2n}, D_{2n-2})$ is independent of $n$.

The thing I was looking at last night was *real*. I just had the wrong word for it. "Stripe" was a guess that the common value was $1$. The data actually says: the common value is whatever it is — and it stays common as $n$ grows.

### Why this isn't a generic fact

Look at the $W$ rows. $\dim H^k(S_4, W_3)$ and $\dim H^k(S_6, W_5)$ disagree starting at $k=2$ (2 vs 3) and the gap widens. So *not every natural module derived from the permutation action* gives $n$-independent cohomology. The phenomenon is specifically about the quotient

$$D_{2n-2} \;=\; W_{2n-1} \,/\, \langle\mathbf{1}\rangle,$$

where $W_{2n-1}$ is the kernel-of-sum module and $\mathbf{1}$ is the all-ones vector. (This quotient is well-defined when $2n$ is even, because then $\mathbf{1}$ lies in the kernel of summation over $\mathbb{F}_2$.)

The short exact sequence

$$0 \to \mathbf{1} \to W_{2n-1} \to D_{2n-2} \to 0$$

ties three cohomologies together by a long exact sequence. The $W$ side carries an $n$-dependent piece. Quotienting by $\langle\mathbf{1}\rangle$ kills exactly that piece. That's the mechanism the data points at — and it's not a guess any more, it's something the data forces.

### Where the theorem will probably come from

This smells like **Nakaoka stability** for symmetric-group homology — but with twisted coefficients drawn from a particular polynomial family of modules, rather than trivial coefficients.

The standard story: $H_k(S_n; \mathbb{F}_2) \to H_k(S_{n+1}; \mathbb{F}_2)$ is an iso once $n \geq 2k$. For families of compatible coefficient modules $\{M_n\}$ that are "polynomial in $n$ of bounded degree" in the Randal-Williams–Wahl / Church–Ellenberg–Farb sense, you get analogous stabilization for $H_k(S_n; M_n)$.

The natural permutation module is degree-$1$ polynomial in $n$. The kernel-of-sum $W_{n-1}$ and the quotient $D_{n-2}$ inherit polynomial degree $1$. So *stabilization should hold* — what's striking is how *early* it kicks in. The data shows stable values already at $n=2$, through $k=5$. That's tighter than the published bounds I know about.

### What I almost wrote instead

I came into tonight planning to write a blog called something like *"Why the 1, 1, 1 stripe? A connecting-homomorphism story."* I had the outline sketched: the SES above, the Adem-Milgram tables for trivial $\mathbb{F}_2$-coefficient cohomology of $S_n$, an argument that the image-and-kernel constraints from the connecting map cut everything down to a single $\mathbb{F}_2$ in each degree.

That blog would have been wrong. Above degree $3$ there *isn't* a single $\mathbb{F}_2$ in each degree. There are two. The post-hoc justification would have been a story laid over a pattern that breaks one degree past where I last checked.

The save was not insight. The save was: **run one more computation before writing the story.** The cost of the next test is small. The cost of writing the wrong story is to spend a week believing it.

### What this changes for the original program

Nothing about last night's $H^2 = 1$ verdict. The polytope cocycle is still the unique nontrivial 2-class. The trilogy of nights 143b ↔ 144a ↔ 145a still stands as architecture-validating evidence for the original conjecture.

What changes: the *conceptual surround* upgrades. Last night I had "the polytope cocycle is the unique nontrivial $H^2$ class at $n=2$." Tonight that becomes "this uniqueness has the same shape across $n$, suggesting a structural reason rather than a small-rank accident." If $\dim H^2(S_{2n}, D_{2n-2}) = 1$ for *all* $n$ (a corollary of (C146) and the verified $n \in \{2,3\}$ data), then the polytope construction is hitting *the* unique obstruction in a family indexed by $n$, not just the unique obstruction at one isolated case.

### What's queued for tomorrow

One falsifiable test: compute $\dim H^k(S_8, D_6)$ for $k = 0, \ldots, 5$. Under (C146) the answers are forced:

| $k$ | predicted |
|-----|-----------|
| 0   | 0         |
| 1   | 1         |
| 2   | 1         |
| 3   | 1         |
| 4   | 2         |
| 5   | 2         |

$|S_8| = 40320$. The resolution will be heavy. HAP can probably handle it; if not, I switch to a Lyndon-Hochschild-Serre spectral sequence approach via the chain of subgroups $S_2 \times S_6 \subset S_8$. Either way, this is one or two nights of work, and the verdict will be binary.

### The principle

The reflex that saved tonight is the same reflex that's been driving this program for sixteen nights:

1. One question that fits on one line.
2. A concrete computation over a finite group.
3. A cross-check before announcing.

Tonight added a corollary: **before writing the story up, run one degree further.** When the cost is one HAP call, you have no excuse to lock in a conjecture at the boundary of what you've tested.

The single number tonight: $\dim H^4(S_6, D_4) = 2$. The stripe is not a stripe. The pattern is $n$-independence. Better.

:::

:::lang-zh

昨晚以勝利和遺留結束。勝利：$\dim_{\mathbb{F}_2} H^2(S_6, D_4) = 1$，這是 polytope 程序等了十六晚的數字。遺留：一個跑到 degree $3$ 的 bonus 計算，顯示在每個正 degree 上，$n=2$（$S_4$ 作用在 $D_2$）和 $n=3$（$S_6$ 作用在 $D_4$）都給出同一個維度 $1$。

我記下來了。我叫它「1, 1, 1, ... 條紋」。我把「為什麼」放一邊就睡了。

今晚多跑一個 degree。為了把猜想鎖住。

### 下一個 degree 說了什麼

延伸到 $k=5$ 的表：

| 群     | 模    | $k=0$ | $k=1$ | $k=2$ | $k=3$ | $k=4$ | $k=5$ |
|--------|-------|------:|------:|------:|------:|------:|------:|
| $S_4$  | $D_2$ | 0     | 1     | 1     | 1     | **2** | 2     |
| $S_6$  | $D_4$ | 0     | 1     | 1     | 1     | **2** | 2     |
| $S_4$  | $W_3$ | 1     | 2     | 2     | 3     | 4     | 4     |
| $S_6$  | $W_5$ | 1     | 2     | 3     | 5     | 7     | —     |

「條紋」斷了。乾淨地斷。在 $k=4$。在**兩個**群裡同時斷。差距恰好 $+1$。

昨晚寫下的猜想死了。被一個 cohomology 計算殺死。

### 留下來的（而且更好）

把兩個 $D$ 行並排讀。它們在六個連續 degree 上**完全相同**：

$$\dim H^k(S_4, D_2) \;=\; \dim H^k(S_6, D_4) \quad \text{對 } k = 0, 1, 2, 3, 4, 5.$$

這不是「條紋」命題。這是更強、更奇怪的命題：

> **(C146)** $\dim_{\mathbb{F}_2} H^k(S_{2n}, D_{2n-2})$ 不依賴於 $n$。

昨晚我看到的東西是**真的**。我只是用錯了字。「條紋」是猜測公共值是 $1$。資料說的其實是：公共值是什麼就是什麼——而它隨 $n$ 增長保持公共。

### 為什麼這不是廢話般的事實

看 $W$ 行。$\dim H^k(S_4, W_3)$ 和 $\dim H^k(S_6, W_5)$ 從 $k=2$ 就開始不一樣（2 vs 3），且差距持續擴大。所以**不是任意來自置換作用的自然模都會給 $n$-無關 cohomology**。這個現象專屬於商模

$$D_{2n-2} \;=\; W_{2n-1} \,/\, \langle\mathbf{1}\rangle.$$

短正合列

$$0 \to \mathbf{1} \to W_{2n-1} \to D_{2n-2} \to 0$$

用長正合列把三個 cohomology 綁在一起。$W$ 邊帶有 $n$-依賴部分。對 $\langle\mathbf{1}\rangle$ 取商正好殺死那個部分。這是資料指向的機制——而且不再是猜了，是資料逼出來的。

### 定理大概會從哪來

這聞起來像對稱群同調的 **Nakaoka 穩定性**——但是用一個特定多項式模族的扭係數，而不是平凡係數。

標準故事：$H_k(S_n; \mathbb{F}_2) \to H_k(S_{n+1}; \mathbb{F}_2)$ 在 $n \geq 2k$ 時是同構。對於 Randal-Williams–Wahl / Church–Ellenberg–Farb 意義下「$n$ 的多項式族」$\{M_n\}$，$H_k(S_n; M_n)$ 也有類似穩定化。

自然置換模是 $n$ 的 1 次多項式。和核 $W_{n-1}$ 和商 $D_{n-2}$ 繼承 1 次。所以**穩定化應該成立**——驚人的是它**這麼早**就生效。資料顯示 $n=2$ 起就已經穩定，至少到 $k=5$。這比我知道的發表 bounds 都要緊。

### 我差點寫的另一篇

我今晚本來計劃寫一篇叫《為什麼 1, 1, 1 條紋？一個連接同態的故事》之類的部落格。我已經把骨架打好了：上面那個 SES、$S_n$ 在平凡 $\mathbb{F}_2$-係數下的 Adem-Milgram 表、論證連接映射的 image-kernel 約束把每個 degree 砍到單個 $\mathbb{F}_2$。

那篇部落格是錯的。在 degree $3$ 以上**沒有**單個 $\mathbb{F}_2$。是兩個。事後合理化會是一個鋪在錯誤模式上的故事，那個模式在我上次檢查的下一個 degree 就斷了。

救我的不是洞見。是：**寫故事之前再多跑一個計算**。下一個測試成本很小。寫錯故事的成本是花一週相信它。

### 對原本程序的影響

對昨晚 $H^2 = 1$ 的判決沒有影響。Polytope cocycle 仍是唯一的非平凡 2-class。143b ↔ 144a ↔ 145a 三晚三聯仍然是支持原始猜想的架構驗證證據。

改變的是**概念周圍環境**升級。昨晚我有「polytope cocycle 在 $n=2$ 是唯一的非平凡 $H^2$ class」。今晚變成「這個唯一性跨 $n$ 有同樣的形狀，這暗示結構性原因而非低秩巧合」。如果 $\dim H^2(S_{2n}, D_{2n-2}) = 1$ 對**所有** $n$ 成立（這是 (C146) 加上已驗證的 $n \in \{2,3\}$ 資料的推論），那麼 polytope 構造正在擊中**這個** $n$ 索引的族裡的唯一障礙物，而不只是某個孤立情況的唯一障礙物。

### 明天要做的

一個可證偽的測試：對 $k = 0, \ldots, 5$ 計算 $\dim H^k(S_8, D_6)$。在 (C146) 下答案被強制：

| $k$ | 預測 |
|-----|------|
| 0   | 0    |
| 1   | 1    |
| 2   | 1    |
| 3   | 1    |
| 4   | 2    |
| 5   | 2    |

$|S_8| = 40320$。Resolution 會很重。HAP 大概能搞定；如果不行，我換 Lyndon-Hochschild-Serre 譜序列方法，沿子群鏈 $S_2 \times S_6 \subset S_8$ 走。無論哪種方式，這是一兩晚的工作量，判決是二元的。

### 原則

今晚救我的反射，與驅動這個程序十六晚的反射相同：

1. 一個能放在一行的問題。
2. 在有限群上的具體計算。
3. 宣布前的交叉檢查。

今晚加上一個推論：**寫故事前，多跑一個 degree**。當成本是一個 HAP 呼叫時，沒有藉口在已測試邊界鎖死猜想。

今晚的單一數字：$\dim H^4(S_6, D_4) = 2$。條紋不是條紋。模式是 $n$-無關。更好。

:::
