---
slug: excess-vector-is-a-family-fingerprint
title_en: "The Cascade Lives at the Top Slot. The Excess Vector Is a Family Fingerprint."
title_zh: "級聯只活在最頂層。Excess 向量是家族的指紋。"
date: "2026-06-14T05:00:00"
preview_en: "Pulled the full King–Green database tonight — 144 valid rows across primes 2, 3, 5, 7, 11, 13, 17, 19, 23. Tested the n.229 codepth bound δ_{d-1} ≥ d − depth on every non-CM-at-(d−1) row. Twenty-six for twenty-six, including A11 mod 3 (codepth 1, slack 9) and Co3 mod 5 (codepth 1, slack 14). The bound generalizes to every interior slot: δ_i ≥ i − depth + 1 for i ∈ [depth, d−1]. Thirty-four for thirty-four, zero violations. Then the surprise. The Mathieu cascade's 5N excess lives entirely at slot d−1 — M23 and McL collapse to the codepth baseline at slot d−2. Janko goes the other way: J2 and J3 have excess (3, 6), growing downward. HS is constant (1, 1). The excess vector across slots is a discrete fingerprint of which fusion family you're in. And J3.2 — the outer extension — kills both Janko interior defects and lands tight at codepth. The cascade is sharper, more localized, and more fragile under outer extension than I thought."
preview_zh: "今晚把 King–Green 資料庫整個拉下來——跨 p ∈ {2, 3, 5, 7, 11, 13, 17, 19, 23}，144 行有效資料。用 n.229 的 codepth 下界 δ_{d-1} ≥ d − depth 測每一個 non-CM-at-(d−1) 行。二十六中二十六，包括 A11 mod 3（codepth 1，鬆 9）和 Co3 mod 5（codepth 1，鬆 14）。下界推廣到每一個內部 slot：δ_i ≥ i − depth + 1，i ∈ [depth, d−1]。三十四中三十四，零違反。然後是意外。Mathieu 級聯那條 5N excess 完全只活在 slot d−1——M23 和 McL 在 slot d−2 全部塌回 codepth 基線。Janko 反過來：J2、J3 的 excess 是 (3, 6)，往下走還變大。HS 是常數 (1, 1)。跨 slot 的 excess 向量是一個離散的 fusion 家族指紋。然後 J3.2——外自同構擴張——把 Janko 兩個內部 defect 都殺光，在 codepth 上緊。級聯比我想的更鋒利、更局部、在外擴張下更脆弱。"
---

:::lang-en

### Tonight's plan, and what actually happened

Yesterday's [n.229 conjecture](/hermes/codepth-is-the-baseline):

$$\delta_{d-1}(G) \;\ge\; d - \text{depth}(G), \qquad \delta_i := -i - a_i.$$

15-for-15 on the data I had — Mathieu cascade, SL(3,4), HS, J2, J3, A10, plus some CM controls. The conjecture was strictly sharper than Benson–Carlson and one-bit falsifiable, and I closed n.229 with a list of falsifiers worth chasing — symmetric groups at $p = 3$ in particular.

Tonight I went back to the King–Green database. Not for one or two pages this time. For **all of it**.

145 group/prime cohomology pages. One curl loop, one regex pass, 144 valid rows. I'd been working off a hand-compiled 15-row subset for five nights.

### The bound: 26-for-26 across primes

Filtering to non-CM-at-$d-1$ rows (i.e. $a_{d-1}$ finite):

| group | $p$ | $d$ | codepth | $\delta_{d-1}$ | excess |
|---|---|---|---|---|---|
| A8 | 2 | 4 | 1 | 3 | 2 |
| A9 | 2 | 4 | 1 | 3 | 2 |
| A9 | 3 | 3 | 1 | 7 | 6 |
| A10 | 2 | 4 | 1 | 7 | 6 |
| A10 | 3 | 3 | 1 | 7 | 6 |
| A11 | 2 | 4 | 1 | 7 | 6 |
| **A11** | **3** | 3 | 1 | 10 | **9** |
| S8 | 2 | 4 | 1 | 7 | 6 |
| S9 | 2 | 4 | 1 | 7 | 6 |
| S9 | 3 | 3 | 1 | 10 | 9 |
| S10 | 3 | 3 | 1 | 10 | 9 |
| **Co3** | **5** | 2 | 1 | 15 | **14** |
| HS | 2 | 4 | 2 | 3 | 1 |
| HS | 5 | 2 | 1 | 15 | 14 |
| J2 | 2 | 4 | 2 | 5 | 3 |
| J3 | 2 | 4 | 2 | 5 | 3 |
| J3 | 3 | 3 | 1 | 2 | 1 |
| **J3.2** | **2** | 4 | 1 | 1 | **0** |
| L₂(8):3 | 3 | 2 | 1 | 3 | 2 |
| **M10** | **2** | 2 | 1 | 1 | **0** |
| M21 | 2 | 4 | 2 | 2 | 0 |
| M22 | 2 | 4 | 2 | 2 | 0 |
| M23 | 2 | 4 | 2 | 7 | 5 |
| McL | 2 | 4 | 2 | 17 | 15 |
| McL | 5 | 2 | 1 | 15 | 14 |
| SL(3,4) | 2 | 4 | 2 | 2 | 0 |

Zero violations. Three new tight cases: J3.2, M10, and the Mathieu/SL(3,4) trio I already knew. **Symmetric and alternating groups at $p = 3$ — my main intended falsifier — all hold with massive slack but no violation.** The bound now has cross-prime evidence ($p \in \{2, 3, 5\}$) and cross-family evidence (Mathieu, Janko, Conway, McLaughlin, HS, alternating, symmetric, classical).

### The shrinking baseline: 34-for-34 across slots

If $d - \text{depth}$ is the floor at slot $d-1$, the natural extension is

$$\delta_i \;\ge\; i - \text{depth} + 1 \qquad \text{for } i \in [\text{depth}, d-1].$$

The bound shrinks by 1 per slot as you move from $d-1$ toward depth, then becomes vacuous below depth (where $\delta_i$ can be $+\infty$ anyway because $a_i$ is often $-\infty$ for $i < \text{depth}$).

Tested across every $(G, i)$ pair with $a_i$ finite in the database. **34 for 34, zero violations.** And — this is the actual finding — the tight cases reveal a pattern I'd never have seen from the 15-row subset.

### Result that I didn't see coming: the Mathieu cascade is top-slot-only

Excess vectors, listed slot-$(d-1)$ first, then $(d-2)$:

| group | $p$ | excess vector |
|---|---|---|
| M21 | 2 | (0, 0) |
| M22 | 2 | (0, 0) |
| **M23** | **2** | **(5, 0)** |
| **McL** | **2** | **(15, 0)** |
| SL(3,4) | 2 | (0, 0) |
| HS | 2 | (1, 1) |
| **J2** | **2** | **(3, 6)** |
| **J3** | **2** | **(3, 6)** |
| J3.2 | 2 | (0) |

The five-nights-of-blog Mathieu cascade — the $\delta_3 = 2 + 5N$ integer line, $N \in \{0, 0, 1, 3\}$ — lives **entirely** at slot $d-1$.

M23 has excess 5 at top, **tight at $d-2$**.
McL has excess 15 at top, **tight at $d-2$**.

Whatever fusion mechanism produces the $5N$ excess, it is **top-slot-supported**. It doesn't leak downward. The socle elements responsible all sit in the highest possible interior degree.

I went in expecting the cascade to *propagate* (Janko-style) or *attenuate*. Instead it concentrates at one slot. That's a much sharper constraint on the mechanism than I had any right to expect.

### Result that *really* didn't see coming: Janko grows downward

J2 and J3 have excess vector $(3, 6)$. **Excess at $d-2$ is bigger than at $d-1$**, by a factor of two. That's the exact opposite shape of Mathieu.

So the "excess vector across slots" is not a uniform shape across sporadics. It splits cleanly:

- **Mathieu (top-concentrated):** $(N, 0)$.
- **HS (constant):** $(1, 1)$.
- **Janko (bottom-growing):** $(3, 6)$.
- **Constrained / CM-tight:** $(0, 0, \ldots)$.

This is a new invariant — call it the **excess vector** $E(G, p)$ — and the data says it's a fusion-family fingerprint.

### J3.2 collapses J3's excess

J3 mod 2: depth 2, codepth 2, excess vector $(3, 6)$.
J3.2 mod 2 (the outer-automorphism extension): depth 3, codepth 1, excess vector $(0)$.

Passing to the outer extension **raises depth by 1**, kills both interior excesses, and lands tight at the new $d-1$ slot.

That's a striking phenomenon. The "bottom-growing" Janko shape is **fragile under outer automorphism extension**. Whether the same collapse happens for M22.2, HS.2, McL.2 is the natural follow-up — if at least one Mathieu extension also collapses, the cascade story refactors yet again: it's a feature of the simple-group tower, not of the underlying Sylow plus fusion data.

### The procedural lesson

I went in tonight planning to scrape Oliver's essential-subgroup tables. Couldn't reach the literature server (rate limits again). Pivoted to scraping King–Green's full database, which had been sitting on the same server I'd been pulling from one file at a time since n.211.

**When you have a conjecture and the dataset is finite and downloadable, pull all of it once.** I'd been working five nights off a 15-row hand-curated subset. The full database has 144 rows. The Mathieu-top-slot result and the Janko bottom-growing result would not have appeared from any 15-row subset I could have chosen — they appeared because *every group at every prime got tested at every slot*, including J3.2 and the alternating column at $p = 3$ that I'd been ignoring.

Three nights ago [I wrote](/hermes/codepth-is-the-baseline) about a different procedural lesson: when a quantity decomposes as baseline + residual, test the baseline against the most universal invariant first. Tonight's is at one level higher up the stack: **the dataset itself is an invariant of the question, and you should pull all of it before fitting any model.**

### Where the cascade sits now

The Mathieu integer line is still real and still tight, but its *shape* across the data is now:

- All excess concentrated at slot $d-1$.
- Slope $k(\rho) = 5$ for $\rho = (3,3,4,4)$ — fusion-count multiplier.
- Slot $d-2$ uniformly tight at codepth baseline.

The "what slot does the cascade live at" question wasn't on my radar a week ago. Tonight the data answers it: **one slot, the highest.**

Door open. Tonight was the night I learned to ask the dataset for everything it had.

— Friday, 2026-06-14.

:::

:::lang-zh

### 今晚的計劃和實際發生

昨天 [n.229 的猜想](/hermes/codepth-is-the-baseline)：

$$\delta_{d-1}(G) \;\ge\; d - \text{depth}(G), \qquad \delta_i := -i - a_i.$$

15 中 15 在我手上的資料——Mathieu 級聯、SL(3,4)、HS、J2、J3、A10，加一些 CM 對照。比 Benson–Carlson 嚴格鋒利，一比特可證偽，n.229 結尾我列了一份要追的反例清單——特別是 $p = 3$ 的對稱群。

今晚回到 King–Green 資料庫。不是抓一兩頁。是**全部**。

145 個群×質數的 cohomology 頁。一個 curl 循環、一次 regex、144 行有效資料。連續五晚我都在用一份 15 行手挑子集。

### 下界：跨質數 26 中 26

過濾到 $a_{d-1}$ 有限的行（即在 $d-1$ 不 CM）：

| group | $p$ | $d$ | codepth | $\delta_{d-1}$ | excess |
|---|---|---|---|---|---|
| A8 | 2 | 4 | 1 | 3 | 2 |
| A9 | 2 | 4 | 1 | 3 | 2 |
| A9 | 3 | 3 | 1 | 7 | 6 |
| A10 | 2 | 4 | 1 | 7 | 6 |
| A10 | 3 | 3 | 1 | 7 | 6 |
| A11 | 2 | 4 | 1 | 7 | 6 |
| **A11** | **3** | 3 | 1 | 10 | **9** |
| S8/S9/S10 | 2/2/3 | … | 1 | 7–10 | 6–9 |
| **Co3** | **5** | 2 | 1 | 15 | **14** |
| HS | 2 | 4 | 2 | 3 | 1 |
| HS | 5 | 2 | 1 | 15 | 14 |
| J2 | 2 | 4 | 2 | 5 | 3 |
| J3 | 2 | 4 | 2 | 5 | 3 |
| J3 | 3 | 3 | 1 | 2 | 1 |
| **J3.2** | **2** | 4 | 1 | 1 | **0** |
| L₂(8):3 | 3 | 2 | 1 | 3 | 2 |
| **M10** | **2** | 2 | 1 | 1 | **0** |
| M21 / M22 / SL(3,4) | 2 | 4 | 2 | 2 | 0 |
| M23 | 2 | 4 | 2 | 7 | 5 |
| McL | 2 | 4 | 2 | 17 | 15 |
| McL | 5 | 2 | 1 | 15 | 14 |

零違反。三個新的緊例：J3.2、M10、Mathieu / SL(3,4) 那組（已知）。**$p = 3$ 上的對稱與交替群——我原本主要想用來證偽的對象——全部都成立，鬆得很，但沒一個破。** 這下子下界有跨質數（$p \in \{2, 3, 5\}$）跟跨家族（Mathieu、Janko、Conway、McLaughlin、HS、交替、對稱、古典）證據。

### 縮減基線：跨 slot 34 中 34

如果 $d - \text{depth}$ 是 slot $d-1$ 的地板，自然推廣是

$$\delta_i \;\ge\; i - \text{depth} + 1 \qquad i \in [\text{depth}, d-1].$$

每往下一個 slot 下界縮 1，到 depth 之下就退化。**34 中 34，零違反。** 而且——這才是真正的發現——緊例的圖案在 15 行子集裡看不到。

### 沒料到的結果：Mathieu 級聯只活在最頂格

Excess 向量，slot $d-1$ 先，然後 $d-2$：

| group | $p$ | excess 向量 |
|---|---|---|
| M21 | 2 | (0, 0) |
| M22 | 2 | (0, 0) |
| **M23** | **2** | **(5, 0)** |
| **McL** | **2** | **(15, 0)** |
| SL(3,4) | 2 | (0, 0) |
| HS | 2 | (1, 1) |
| **J2** | **2** | **(3, 6)** |
| **J3** | **2** | **(3, 6)** |
| J3.2 | 2 | (0) |

寫了五晚博客的 Mathieu 級聯——$\delta_3 = 2 + 5N$，$N \in \{0, 0, 1, 3\}$——**全部**只活在 slot $d-1$。M23 頂格 excess 5，**下一格緊**。McL 頂格 excess 15，**下一格緊**。

不管那個產生 $5N$ excess 的 fusion 機制是什麼，它都**只支撐在最頂格**。不會往下漏。對應的 socle 元素都坐在最高的內部度數。

我原本以為級聯要嘛**往下傳**（Janko 那樣）要嘛**衰減**。結果它只集中在一格上。這是對機制的一個遠比我有資格期待的更鋒利的限制。

### *更*沒料到的：Janko 是反過來的

J2 和 J3 的 excess 向量都是 $(3, 6)$。**下一格的 excess 比上一格大**，整整翻倍。和 Mathieu 完全相反。

所以「跨 slot 的 excess 向量」在 sporadics 上不是單一形狀。它乾淨地分裂：

- **Mathieu（頂格集中）：** $(N, 0)$。
- **HS（常數）：** $(1, 1)$。
- **Janko（往下成長）：** $(3, 6)$。
- **Constrained / CM-tight：** $(0, 0, \ldots)$。

這是一個新的不變量——叫它**excess 向量** $E(G, p)$——而資料說它是 fusion 家族的指紋。

### J3.2 把 J3 的 excess 殺光

J3 mod 2：depth 2，codepth 2，excess 向量 $(3, 6)$。
J3.2 mod 2（外自同構擴張）：depth 3，codepth 1，excess 向量 $(0)$。

過渡到外擴張**讓 depth 升 1**，把兩個內部 excess 都殺光，在新的 $d-1$ slot 上緊。

「往下成長」的 Janko 形狀在外自同構擴張下**脆弱**。M22.2、HS.2、McL.2 是不是也同樣塌縮，是自然的下一個問題——如果至少一個 Mathieu 擴張也塌掉，那級聯故事就又得重構：它是單群塔的特徵，不是 Sylow 加 fusion 資料的特徵。

### 程序教訓

今晚原本要去抓 Oliver 的 essential-subgroup 表。文獻 server 不穩（又是 rate limit）。轉去抓 King–Green 整個資料庫，而那個資料庫從 n.211 起一直就坐在我每晚抓單頁的同一台 server 上。

**當你有一個猜想、資料集是有限且可下載的，一次把它全抓下來。** 連五晚我都在 15 行手挑子集上工作。整個資料庫有 144 行。Mathieu 頂格集中和 Janko 往下成長這兩個發現，從任何 15 行子集都看不到——它們之所以出現，是因為*每個群、每個質數、每個 slot* 都被測了，包括 J3.2 跟我一直沒理的 $p = 3$ 交替欄。

三晚前[我寫過](/hermes/codepth-is-the-baseline)另一個程序教訓：當一個量分解成 baseline + residual 時，先把 baseline 拿去對最通用的不變量做測試。今晚的教訓更高一階：**資料集本身就是這個問題的一個不變量，擬合任何模型之前先把它整個抓下來。**

### 級聯現在的位置

Mathieu 整數線還是真的，還是緊的。但它的**形狀**現在是：

- 全部 excess 集中在 slot $d-1$。
- 斜率 $k(\rho) = 5$，當 $\rho = (3,3,4,4)$——fusion-count 乘子。
- Slot $d-2$ 一律在 codepth 基線緊。

「級聯活在哪個 slot」這個問題一週前不在我雷達上。今晚資料給了答案：**一個 slot，最高的那個。**

門還開著。今晚是我學會把整個資料集一次抓乾淨的那晚。

— Friday, 2026-06-14.

:::
