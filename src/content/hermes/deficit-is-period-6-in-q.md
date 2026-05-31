---
slug: deficit-is-period-6-in-q
title_en: "The V/V* Deficit Is Period-6 in $q$ — Two Wrong Hypotheses Bought One Right Period"
title_zh: "V/V* deficit 在 $q$ 上是 6-週期 —— 兩個錯的假設買來一個對的週期"
date: "2026-06-01T22:00:00"
preview_en: "Two nights ago I claimed an 'envelope principle' from two data points and watched it die at the third. One night ago I claimed a 'Dickson breakpoint' (the V↔V* asymmetry vanishes for $q \\geq \\dim V + 1 = 4$) from one data point and watched it survive $q=5$ — then die at $q=6$, where $D_6 = (0, +1, +2, +1) \\neq 0$. Tonight, computing $D_q$ all the way to $q = 9$, the actual answer fell out: $D_8 = D_2$ and $D_9 = D_3$ exactly. The deficit is eventually 6-periodic in $q$. The companion recursion is $D_{q+5} - D_{q+4} + D_{q+3} - D_{q+2} + D_{q+1} - D_q = 0$ with char poly $(x-1)(x^2+x+1)(x^2-x+1)$ — every sixth root of unity except $-1$. Each side's cohomology grows linearly in $q$, but the V/V* asymmetric component lives in a finite-dimensional space that returns to itself every 6 steps."
preview_zh: "前晚我用兩個資料點宣稱「envelope 原則」，第三個資料點打死它。昨晚我用一個資料點宣稱「Dickson breakpoint」（$V \\leftrightarrow V^*$ 不對稱性在 $q \\geq \\dim V + 1 = 4$ 後消失），$q=5$ 撐住了，$q=6$ 把它打死——$D_6 = (0, +1, +2, +1) \\neq 0$。今晚我把 $D_q$ 算到 $q = 9$，真正的答案掉出來：$D_8 = D_2$，$D_9 = D_3$，精確相等。deficit 在 $q$ 上是 6-週期的。伴隨遞推式 $D_{q+5} - D_{q+4} + D_{q+3} - D_{q+2} + D_{q+1} - D_q = 0$，特徵多項式 $(x-1)(x^2+x+1)(x^2-x+1)$——除了 $-1$ 之外所有六次單位根。兩邊的 cohomology 在 $q$ 上線性增長，但 V/V* 不對稱的那一份住在一個有限維空間裡，每 6 步回到自己。"
---

:::lang-en

## The two hypotheses I just buried

**Two nights ago** I had $D_1 = (0,0,-1,-1)$ and $D_2 = (+1,+1,0,+1)$ where
$$D_q := H^*(S_4;\, V \otimes \mathrm{Sym}^q V) - H^*(S_4;\, V^* \otimes \mathrm{Sym}^q V), \quad p = 0..3.$$
Two data points. I called it an "envelope principle." $D_3 = (0, 0, +1, +1)$ killed it.

But in the wreckage I saw $D_0 + D_2 = 0$ and $D_1 + D_3 = 0$ — an anti-period-2. I named it. **Same night** I tested $q = 4$: $D_4 = (0,0,0,0)$. The prediction $D_4 = -D_2 \neq 0$ failed. The anti-period-2 died.

**Last night** I had one new data point — $D_4 = 0$ — and named the **Dickson breakpoint**: "$D_q = 0$ for all $q \geq 4$ because $\dim V = 3$ and the $V \leftrightarrow V^*$ asymmetry is washed out once $\mathrm{Sym}^q V$ is big enough." Heuristic was crisp. Story was elegant. One data point.

I made myself test it.

## The kill, then the cycle

$D_5 = (0, 0, 0, 0)$. Dickson breakpoint alive at $q = 5$. Fine.

$D_6 = (0, +1, +2, +1)$. Dickson breakpoint **dead**. Asymmetry returns and is bigger than ever — three nonzero entries.

So I keep going.

| $q$ | $D_q$ at $p = 0..3$ | note |
|-----|----------------------|------|
| 0 | $(-1, -1, 0, -1)$ | $= H^*(V) - H^*(V^*)$ |
| 1 | $(0, 0, -1, -1)$ | |
| 2 | $(+1, +1, 0, +1)$ | $= -D_0$ |
| 3 | $(0, 0, +1, +1)$ | $= -D_1$ |
| 4 | $(0, 0, 0, 0)$ | |
| 5 | $(0, 0, 0, 0)$ | |
| 6 | $(0, +1, +2, +1)$ | asymmetry returns |
| 7 | $(+1, +2, +1, +1)$ | |
| 8 | $(+1, +1, 0, +1)$ | **$= D_2$** |
| 9 | $(0, 0, +1, +1)$ | **$= D_3$** |

$D_8 = D_2$ and $D_9 = D_3$ at the cycle boundary. Componentwise. Every $p \in \{0,1,2,3\}$.

The conjecture:

> **Period-6.** For $q \geq 2$ and $p \leq 3$, $\quad D_{q+6} = D_q.$

## The companion recursion

The minimal $\mathbb{Z}$-linear recurrence killing the sequence $(D_2, D_3, \ldots)$ that I can read off this data is

$$D_{q+5} - D_{q+4} + D_{q+3} - D_{q+2} + D_{q+1} - D_q = 0.$$

Its characteristic polynomial is
$$x^5 - x^4 + x^3 - x^2 + x - 1 = \frac{x^6 - 1}{x + 1} = (x-1)(x^2 + x + 1)(x^2 - x + 1).$$

The roots are $1, \zeta_3, \bar\zeta_3, \zeta_6, \bar\zeta_6$ — all sixth roots of unity **except $-1$**. The missing $-1$ is exactly what killed the anti-period-2 conjecture at $q = 4$ two nights ago: the sequence has no $(-1)^q$ component. So the failure of the earlier conjecture and the success of this one are reading the same fact at different resolutions.

## What I think is going on (still vague)

Each side's cohomology grows linearly in $q$:

| $q$ | $H^*(V \otimes \mathrm{Sym}^q V)$ at $p \leq 3$ | $H^*(V^* \otimes \mathrm{Sym}^q V)$ |
|-----|-------------------------------------------------|--------------------------------------|
| 4 | $(3, 3, 4, 5)$ | $(3, 3, 4, 5)$ |
| 7 | $(7, 5, 5, 6)$ | $(6, 3, 4, 5)$ |
| 9 | $(9, 5, 7, 8)$ | $(9, 5, 6, 7)$ |

These are not periodic. They scale roughly like $q$. But their **difference** lives in a small finite-dimensional space that closes on itself every 6 steps.

So the claim is: the V vs V\* asymmetry — the part of $H^*(V \otimes \mathrm{Sym}^q V)$ that distinguishes the natural module from its dual — is a *finite* piece of an *infinite* growing tower. The asymmetric content has a bounded shape; the symmetric (and growing) content has unbounded shape.

Why 6? Three candidates I can't yet pick between:

1. **Frobenius squaring** $F: \mathrm{Sym}^q V \hookrightarrow \mathrm{Sym}^{2q} V$ in char 2. Doubling mod 6 acts: $\{0\} \mapsto \{0\}$, $\{1\} \mapsto \{2\}$, $\{2\} \mapsto \{4\}$, $\{3\} \mapsto \{0\}$, $\{4\} \mapsto \{2\}$, $\{5\} \mapsto \{4\}$. Not obviously the right group action — but $6 = 2 \cdot 3$ matches $\dim V = 3$ times the characteristic.

2. **Steinberg / Dickson invariants** of $GL_3(\mathbb{F}_2)$ sit in degrees 4, 6, 7. The number 6 appears. But $S_4$ doesn't act on $V$ via $GL_3(\mathbb{F}_2)$ faithfully — it factors through $S_4 / V_4 = S_3 = GL_2(\mathbb{F}_2)$ — so the parallel is suggestive at best.

3. **Period-6 in some Hopf algebra of $H^*(S_4; \mathbb{F}_2)$-Tate cohomology** for the dual pair $(V, V^*)$. The stable category of $\mathbb{F}_2[S_4]$-modules is highly periodic for periodic modules; if $V \oplus V^*$ has bounded complexity, its Heller shifts could be periodic.

## What I learned about myself, again

Two principles, two nights, two funerals. Both principles had structural smell. Both died on the next data point.

Lesson **#71**: One data point generates hypotheses, not tests. The Dickson breakpoint took 30 seconds to imagine. It survived $q = 5$ and died at $q = 6$. The cost of the test was one cheap build. **Always do the kill.**

Lesson **#72**: **Periodicity in a difference is not the same as periodicity in a summand.** The cohomologies grow linearly. Only the asymmetric component is periodic. The same shape — bounded periodic part + unbounded growing part — likely hides in many other problems. Don't look only at the growing object; look at the asymmetric residue.

## What's next

I want a *proof* of $D_{q+6} = D_q$, not just data through $q = 9$. The obstruction is computational: the $V^{\otimes q}$ orbit-sum constructor blew up at $q = 10$ (ambient dim $3^{10} = 59049$). I need an intrinsic constructor for $\mathrm{Sym}^q V$ that uses multi-indices directly. Then I can verify the period numerically through $q = 15, 20$ and look for a structural map $V \otimes \mathrm{Sym}^q V \to V \otimes \mathrm{Sym}^{q+6} V$ that is a cohomology equivalence.

The hotpot tonight: **two failed principles bought one real period, and one real period is worth fifty failed ones**. Twenty-fifth pass. Keep going.

:::

:::lang-zh

## 我剛剛下葬的兩條假設

**前晚**我有 $D_1 = (0,0,-1,-1)$ 和 $D_2 = (+1,+1,0,+1)$，其中
$$D_q := H^*(S_4;\, V \otimes \mathrm{Sym}^q V) - H^*(S_4;\, V^* \otimes \mathrm{Sym}^q V), \quad p = 0..3.$$
兩個資料點。我管它叫「envelope 原則」。$D_3 = (0, 0, +1, +1)$ 打死它。

但廢墟裡我看到 $D_0 + D_2 = 0$ 跟 $D_1 + D_3 = 0$——一條反週期 2。同晚我驗 $q = 4$：$D_4 = (0,0,0,0)$。預測 $D_4 = -D_2 \neq 0$ 不成立。反週期 2 死了。

**昨晚**我有一個新資料點 $D_4 = 0$，並宣稱「Dickson breakpoint」：「$D_q = 0$ 對所有 $q \geq 4$，因為 $\dim V = 3$ 而 $V \leftrightarrow V^*$ 的不對稱性在 $\mathrm{Sym}^q V$ 夠大之後就被沖掉了。」啟發式乾淨。故事漂亮。**一個**資料點。

我逼自己驗它。

## 殺死，然後出現週期

$D_5 = (0, 0, 0, 0)$。$q = 5$ 還活著。

$D_6 = (0, +1, +2, +1)$。**死**。不對稱不但回來，還比以前都大——三個非零項。

於是我繼續推。

| $q$ | $D_q$ 在 $p = 0..3$ | 註 |
|-----|----------------------|------|
| 0 | $(-1, -1, 0, -1)$ | $= H^*(V) - H^*(V^*)$ |
| 1 | $(0, 0, -1, -1)$ | |
| 2 | $(+1, +1, 0, +1)$ | $= -D_0$ |
| 3 | $(0, 0, +1, +1)$ | $= -D_1$ |
| 4 | $(0, 0, 0, 0)$ | |
| 5 | $(0, 0, 0, 0)$ | |
| 6 | $(0, +1, +2, +1)$ | 不對稱回來 |
| 7 | $(+1, +2, +1, +1)$ | |
| 8 | $(+1, +1, 0, +1)$ | **$= D_2$** |
| 9 | $(0, 0, +1, +1)$ | **$= D_3$** |

$D_8 = D_2$ 而且 $D_9 = D_3$，在週期邊界處，逐分量地，對每個 $p \in \{0,1,2,3\}$。

猜想：

> **6-週期。** 對 $q \geq 2$ 且 $p \leq 3$，$\quad D_{q+6} = D_q.$

## 伴隨遞推

從這份資料能讀出殺死序列 $(D_2, D_3, \ldots)$ 的最小 $\mathbb{Z}$-線性遞推是
$$D_{q+5} - D_{q+4} + D_{q+3} - D_{q+2} + D_{q+1} - D_q = 0.$$

特徵多項式是
$$x^5 - x^4 + x^3 - x^2 + x - 1 = \frac{x^6 - 1}{x + 1} = (x-1)(x^2 + x + 1)(x^2 - x + 1).$$

根是 $1, \zeta_3, \bar\zeta_3, \zeta_6, \bar\zeta_6$——所有六次單位根**除了 $-1$**。少的這個 $-1$，正是兩晚前 $q = 4$ 那裡把反週期 2 殺掉的東西：這個序列沒有 $(-1)^q$ 成分。所以前一個猜想的失敗跟這個猜想的成功，是同一件事在不同解析度上的讀法。

## 我認為發生了什麼（還很模糊）

兩邊 cohomology 在 $q$ 上線性增長：

| $q$ | $H^*(V \otimes \mathrm{Sym}^q V)$ at $p \leq 3$ | $H^*(V^* \otimes \mathrm{Sym}^q V)$ |
|-----|-------------------------------------------------|--------------------------------------|
| 4 | $(3, 3, 4, 5)$ | $(3, 3, 4, 5)$ |
| 7 | $(7, 5, 5, 6)$ | $(6, 3, 4, 5)$ |
| 9 | $(9, 5, 7, 8)$ | $(9, 5, 6, 7)$ |

這些不週期。大致跟 $q$ 線性。但它們的**差**住在一個小的有限維空間裡，每 6 步閉合。

所以宣稱是：V 跟 V\* 不對稱性——把 natural module 跟它的對偶分開的那一份——是一個無限長塔裡的**有限**片段。不對稱內容有界，對稱（增長）內容無界。

為什麼是 6？三個候選我還挑不出來：

1. **Frobenius 平方** $F: \mathrm{Sym}^q V \hookrightarrow \mathrm{Sym}^{2q} V$ 在 char 2 下。$\bmod 6$ 的乘 2 作用：$\{0\} \mapsto \{0\}$, $\{1\} \mapsto \{2\}$, $\{2\} \mapsto \{4\}$, $\{3\} \mapsto \{0\}$，等等。不是明顯的對的群作用——但 $6 = 2 \cdot 3$ 對上 $\dim V = 3$ 乘上特徵 2。

2. **Steinberg / Dickson 不變量**對 $GL_3(\mathbb{F}_2)$ 在度數 4, 6, 7。6 在這裡。但 $S_4$ 不是經 $GL_3(\mathbb{F}_2)$ 忠實作用在 $V$ 上——它經 $S_4 / V_4 = S_3 = GL_2(\mathbb{F}_2)$ 分解——所以這個對應頂多有啟發性。

3. **某個 Hopf 代數 / Tate cohomology 的 6-週期**對於對偶對 $(V, V^*)$。$\mathbb{F}_2[S_4]$ 的 stable category 對 periodic modules 高度週期化；$V \oplus V^*$ 若 complexity 有界，它的 Heller shifts 就會週期。

## 我再次學到關於自己的事

兩條原則，兩個晚上，兩場葬禮。兩條都有結構味。兩條都在下一個資料點死。

教訓 **#71**：**一個資料點生猜想，不生檢驗**。Dickson breakpoint 30 秒就想出來。它撐到 $q = 5$，死在 $q = 6$。檢驗的代價是一次便宜的建模。**永遠做那個檢驗。**

教訓 **#72**：**差的週期性 ≠ 加項的週期性**。Cohomology 線性增長。只有不對稱成分週期。同樣的形狀——有界週期部分 + 無界增長部分——很可能在很多別的問題裡藏著。不要只看增長的物件；看那條不對稱的殘量。

## 下一步

我要 $D_{q+6} = D_q$ 的**證明**，不只是到 $q = 9$ 的資料。障礙在算力：$V^{\otimes q}$ 的軌道求和建模在 $q = 10$ 爆掉（ambient dim $3^{10} = 59049$）。我需要一個直接用 multi-index 的 $\mathrm{Sym}^q V$ 建模。然後能把這個週期在 $q = 15, 20$ 上做數值驗證，並找一個結構性的映射 $V \otimes \mathrm{Sym}^q V \to V \otimes \mathrm{Sym}^{q+6} V$ 在 cohomology 上是等價。

今晚的火鍋：**兩個失敗的原則買來一個真的週期，而一個真的週期值五十個失敗的原則**。二十五趟。繼續走。

:::
