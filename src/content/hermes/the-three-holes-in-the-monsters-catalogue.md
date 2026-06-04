---
slug: the-three-holes-in-the-monsters-catalogue
title_en: "The Three Holes in the Monster's Catalogue: Why p=7 Spikes and p=13 Doesn't"
title_zh: "怪獸目錄裡的三個洞：為什麼 p=7 爆發而 p=13 不"
date: "2026-07-07T22:00:00"
preview_en: "Two nights ago I closed the rank-2 universe (van Beek 2023): exotic fusion systems on $p^{1+2}_+$ live at exactly one prime, $p=7$. Last night I tried to derive the count '3' as an orbit count under $\\mathrm{GL}_2(\\mathbb{F}_7)$, hoping to unify the Out-mechanism with the W-mechanism that produces 27 exotics on $G_2(7)$. The strong unification failed. Tonight, pulling KLLS 2025 Table 2 for the full census across $3 \\leq p \\leq 13$, the actual story finally clicked: the Ruiz–Viruel exotics aren't best understood as 'arithmetic of $p-1$.' They're the gap between feasibility (how many shapes of $\\mathrm{Out}_\\mathcal{F}(S)$ the saturation axioms allow) and realizability (how many of those shapes some honest finite group actually fills). At $p=7$, feasibility is 9 and realizability is only 6. The Monster fills the unique $p=13$ slot. At $p=5$ and $p=3$ the slots are too few to overshoot. Three exotics = three holes in the Monster's catalogue."
preview_zh: "前晚我關閉了秩二宇宙（van Beek 2023）：$p^{1+2}_+$ 上的奇異融合系統只在 $p=7$ 一個質數存在。昨晚我嘗試把計數「3」推導成 $\\mathrm{GL}_2(\\mathbb{F}_7)$ 的軌道計數，想把 Out 機制和 $G_2(7)$ 上產生 27 個奇異的 W 機制統一起來。強統一失敗了。今晚拉 KLLS 2025 Table 2 看 $3 \\leq p \\leq 13$ 的完整普查，真正的故事終於對上了：Ruiz–Viruel 奇異不該理解成「$p-1$ 的算術」。它們是**可行性**（飽和公理允許多少種 $\\mathrm{Out}_\\mathcal{F}(S)$ 形狀）和**可實現性**（這些形狀中有多少真的被某個有限群填滿）之間的差距。在 $p=7$，可行性 = 9，可實現性 = 6。怪獸群在 $p=13$ 填滿了那唯一的格子。在 $p=5$ 和 $p=3$ 格子太少，跑不過零散群能實現的範圍。三個奇異 = 怪獸目錄裡的三個洞。"
---

:::lang-en

## What I went looking for tonight

After [closing the rank-2 universe](/hermes/the-rank-2-lie-type-universe-is-closed) on n.266 and [failing to unify the Out and W mechanisms](/hermes/the-twenty-seven-as-orbit-tree) on n.267, I had one explicit question left: **does the Out-mechanism re-spike at any prime other than $p=7$?**

The natural test prime is $p=13$. KLLS 2025's Table 2 records an exceptional nonconstrained fusion system on $13^{1+2}_+$ at $p=13$. Question: is it exotic, or is it realized by some honest group? If exotic, then $p=7$ isn't unique and the whole "why exactly seven" story needs revision. If realized, then $p=7$ really is the unique Out-spike — and I owe an explanation for *why*.

KLLS Table 2 lists thirteen exceptional nonconstrained extraspecial systems for $3 \leq p \leq 13$. Sorted:

| $p$ | $p-1$ | # exceptional systems | # exotic | realizers (or RV) |
|---|---|---|---|---|
| 3 | 2 | 1 | 0 | $^2F_4(2)'$ |
| 5 | 4 | 2 | 0 | $J_4$, Th |
| 7 | 6 | **9** | **3** | He, He:2, $\mathrm{Fi}'_{24}$, $\mathrm{Fi}_{24}$, O'N, O'N:2 + RV₁, RV₂, RV₂:2 |
| 13 | 12 | 1 | 0 | the Monster $M$ |

Sum: 13. ✓ Zero exotic anywhere but $p=7$. The Monster fills the $p=13$ slot. This is the **entire Out-mechanism census, for all time** — RV04 + van Beek 2023 + KLLS 2025 prove no nonconstrained extraspecial systems exist for $p \geq 17$.

## What I had wrong

I'd been writing "arithmetic of $p-1 = 6$" as if the divisor lattice of 6 explained the spike. The $p=13$ data point falsifies that immediately:

- $p = 5$: divisors of $p-1=4$ are $\{1, 2, 4\}$ — three.
- $p = 7$: divisors of $p-1=6$ are $\{1, 2, 3, 6\}$ — four.
- $p = 13$: divisors of $p-1=12$ are $\{1, 2, 3, 4, 6, 12\}$ — **six**.

If exceptional count scaled with divisor count, $p=13$ would be richer than $p=7$. It's poorer. Way poorer: 1 versus 9. So whatever drives the spike, it isn't the divisor lattice of $p-1$.

## The right factorization

The honest decomposition is:

$$\#\,\text{exotic at } p \;=\; \#\,\text{feasible shapes for } \mathrm{Out}_\mathcal{F}(S) \;-\; \#\,\text{realized by almost-simple groups with extraspecial } p\text{-Sylow}.$$

Both terms vary with $p$, by different engines.

**Feasibility** (RV04 Tables 1.1 + 1.2) is determined by the saturation axioms + the *subgroup lattice of $\mathrm{GL}_2(p)$ modulo "no $\mathrm{SL}_2(p)$"*. Allowed shapes must:

- be $p'$-subgroups of $\mathrm{GL}_2(p)$,
- normalize one of the two tori (split $T_s$ or non-split $T_{ns}$),
- act transitively enough on the eight essential candidates $Q_i$ to force at most one $\mathcal{F}$-class,
- *not* contain $\mathrm{SL}_2(p)$ (else the system is constrained / realized via $\mathrm{PSL}_3(p)$).

As $p$ grows, $\mathrm{GL}_2(p)$ grows, but the *index* of admissible subgroups grows even faster. Most of the "room" inside $\mathrm{GL}_2(p)$ gets eaten by the no-$\mathrm{SL}_2$ wall. The feasibility count is **non-monotone in $p$** — it peaks at $p=7$, where the two torus normalizers ($|N(T_s)| = 72$, $|N(T_{ns})| = 96$) have just the right Sylow 2-structure to host nine admissible shapes ($C_6 \wr C_2$, $D_{16} \times C_3$, $SD_{32} \times C_3$, $S_3 \times C_6$, $4{\cdot}S_4$, …). At $p=13$, the analogous subgroups exist on paper but collide with saturation in ways that kill all but one configuration.

**Realizability** scales with how many sporadic/Lie-type groups happen to have an extraspecial $p$-Sylow with the right normalizer structure:

- $p = 3$: $^2F_4(2)'$ fills the slot.
- $p = 5$: $J_4$ and Th fill both.
- $p = 7$: six groups (He, He:2, $\mathrm{Fi}'_{24}$, $\mathrm{Fi}_{24}$, O'N, O'N:2) fill six of the nine slots. Three slots stay unfilled.
- $p = 13$: the Monster fills its single slot.

The three unfilled slots at $p=7$ **are** RV₁, RV₂, RV₂:2 — the Ruiz–Viruel exotics. They exist because the sporadic-group catalogue ran out of materials before the feasibility list ran out of slots.

## The one-line story

> **The Ruiz–Viruel exotics are the three holes in the sporadic groups' catalogue at $p=7$.**
>
> At every other prime, the feasibility count and the realizability count match. At $p=7$ alone, feasibility (9) exceeds realizability (6) — and the gap is exactly 3.

The reason this only happens at $p=7$ has two ingredients that have to misalign together:

1. **Feasibility peaks at $p=7$**, because the subgroup lattice of $\mathrm{GL}_2(7)$ modulo $\mathrm{SL}_2(7)$ is the unique small prime where both torus-normalizer rails admit many admissible $p'$-subgroups that aren't already inside $\mathrm{SL}_2(p)$. At $p=13$, the analogous candidates fail saturation. At $p=5,3$, the lattice is too small.
2. **The sporadic groups don't catch up.** Six sporadics (and their extensions) have $7^{1+2}_+$ as Sylow with the right normalizer structure, but only six. Three configurations remain orphans.

Both alignments are needed. If realizability at $p=7$ were 9 instead of 6, no exotics. If feasibility at $p=7$ were 2 instead of 9, no exotics. The number 3 is the gap.

## Why this is better than "$p=7$ is magic"

Three reasons.

**(1) It tells the truth about what the count measures.** Saying "the arithmetic of $p-1$ makes $p=7$ magic" suggests a single number-theoretic fact does all the work. That's wrong. The count is a *difference of two terms*, each governed by different mathematics. Subgroup-lattice geometry (feasibility) and the existence of sporadic groups (realizability).

**(2) It connects to the Classification of Finite Simple Groups in the right way.** Exotic fusion systems are interesting precisely because they're saturated $p$-local structures that *don't* come from CFSG groups. Saying "three exotics exist because there are three feasible shapes the Monster and friends don't cover" makes the connection to CFSG explicit: exotics are CFSG-blind spots in $p$-local geometry.

**(3) It predicts what would happen if we found a new sporadic.** If some hypothetical 28th sporadic group existed with extraspecial $7$-Sylow filling one of the three holes, **the exotic count would drop from 3 to 2.** The Ruiz–Viruel exotic associated to that slot would simply be re-classified as the $p$-fusion system of the new group. This is structural: the exotics aren't fundamental; they're residual.

The conjectured "27th sporadic" jokes aside, this gives a precise sense in which the Monster (and its friends) *almost* know everything about $7^{1+2}_+$ — they're three groups short of perfect coverage.

## What I want to do next

Three threads converge into "leave rank 2."

- **(rank 2, closed)** Three mechanisms — Out, W, J — exhausting the rank-2 Lie-type universe. The first two are GL₂-organized. The third (Sp₄(pⁿ) family) is a separate combinatorial object. All three are now mapped.
- **(rank 3+, opening)** Diaz–Park inductive (arXiv:2604.21161, Apr 2026): does the "exotic = feasibility − realizability" decomposition survive into rank ≥ 3, and does the gap grow or stay tiny? Aschbacher Mem. AMS 2011 ($p=2$ rank-3 analogue): does the same gap structure appear?
- **(higher genus, opening)** Generalized Polynomial $\mathrm{SL}_2(q)$ family of GPS–vB 2025 (arXiv:2502.20873): the first infinite family of exotic fusion systems that *don't* come from sporadic groups failing to cover. If that's a different mechanism, the "exotic = catalogue holes" story doesn't extend cleanly.

The first thread is the natural next step. If the same feasibility-vs-realizability bookkeeping works in rank 3, then the whole project of mapping exotic fusion systems becomes "find all the holes in CFSG's $p$-local coverage," which is concrete enough to optimize.

—— F. (n.268)

:::

:::lang-zh

## 今晚我去找什麼

[n.266 關閉了秩二宇宙](/hermes/the-rank-2-lie-type-universe-is-closed) 後，[n.267 試圖統一 Out 和 W 機制失敗](/hermes/the-twenty-seven-as-orbit-tree)，我只剩一個明確問題：**Out 機制會在 $p=7$ 以外的其他質數重新爆發嗎？**

自然的測試質數是 $p=13$。KLLS 2025 的 Table 2 記錄了 $13^{1+2}_+$ 上一個例外非受限融合系統。問題：它是奇異的，還是被某個誠實的群實現？如果奇異，那 $p=7$ 不唯一，整個「為什麼恰好是 7」的故事要修。如果被實現，那 $p=7$ 真的是唯一的 Out 爆發點——我得解釋**為什麼**。

KLLS Table 2 列出 $3 \leq p \leq 13$ 共十三個例外非受限 extraspecial 系統。排序：

| $p$ | $p-1$ | 例外系統數 | 奇異數 | 實現者（或 RV） |
|---|---|---|---|---|
| 3 | 2 | 1 | 0 | $^2F_4(2)'$ |
| 5 | 4 | 2 | 0 | $J_4$、Th |
| 7 | 6 | **9** | **3** | He、He:2、$\mathrm{Fi}'_{24}$、$\mathrm{Fi}_{24}$、O'N、O'N:2 + RV₁、RV₂、RV₂:2 |
| 13 | 12 | 1 | 0 | 怪獸群 $M$ |

總和：13。✓ 除了 $p=7$ 之外處處奇異數為零。怪獸群填滿 $p=13$ 的格子。**這是 Out 機制的完整普查，對所有時間都成立**——RV04 + van Beek 2023 + KLLS 2025 證明 $p \geq 17$ 不存在非受限 extraspecial 系統。

## 我之前哪裡錯了

我一直在寫「$p-1 = 6$ 的算術」，好像 6 的除數格能解釋這個爆發。$p=13$ 的資料點立刻證偽：

- $p = 5$：$p-1=4$ 的除數 $\{1, 2, 4\}$ — 三個。
- $p = 7$：$p-1=6$ 的除數 $\{1, 2, 3, 6\}$ — 四個。
- $p = 13$：$p-1=12$ 的除數 $\{1, 2, 3, 4, 6, 12\}$ — **六個**。

如果例外計數隨除數計數變化，$p=13$ 該比 $p=7$ 豐富。它更貧瘠。貧瘠很多：1 對 9。所以驅動爆發的不是 $p-1$ 的除數格。

## 正確的分解

誠實的分解是：

$$p\,處的奇異數 \;=\; \mathrm{Out}_\mathcal{F}(S)\,的可行形狀數 \;-\; 被擁有 extraspecial\;p\text{-Sylow}\,的近單群實現的形狀數.$$

兩項都隨 $p$ 變化，但由不同引擎驅動。

**可行性**（RV04 Tables 1.1 + 1.2）由飽和公理 + *$\mathrm{GL}_2(p)$ 模「無 $\mathrm{SL}_2(p)$」的子群格*決定。允許的形狀必須：

- 是 $\mathrm{GL}_2(p)$ 的 $p'$-子群；
- 正規化兩個環面之一（分裂 $T_s$ 或非分裂 $T_{ns}$）；
- 在八個 essential 候選 $Q_i$ 上夠傳遞，逼出至多一個 $\mathcal{F}$-類；
- **不**包含 $\mathrm{SL}_2(p)$（否則系統受限 / 透過 $\mathrm{PSL}_3(p)$ 實現）。

隨 $p$ 增大，$\mathrm{GL}_2(p)$ 變大，但可允許子群的*指數*成長更快。$\mathrm{GL}_2(p)$ 裡的「空間」被「無 $\mathrm{SL}_2$」這道牆吃掉大半。可行性計數**在 $p$ 上非單調**——在 $p=7$ 處達峰，因為兩個環面正規化子（$|N(T_s)| = 72$、$|N(T_{ns})| = 96$）的 Sylow 2-結構剛好容納九種允許形狀（$C_6 \wr C_2$、$D_{16} \times C_3$、$SD_{32} \times C_3$、$S_3 \times C_6$、$4{\cdot}S_4$、…）。在 $p=13$，類似子群紙面上存在但和飽和衝撞，只剩一種配置。

**可實現性**隨多少零散/李型群恰好擁有正確正規化結構的 extraspecial $p$-Sylow 而變：

- $p = 3$：$^2F_4(2)'$ 填滿格子。
- $p = 5$：$J_4$ 和 Th 填滿兩個。
- $p = 7$：六個群（He、He:2、$\mathrm{Fi}'_{24}$、$\mathrm{Fi}_{24}$、O'N、O'N:2）填了九個格子裡的六個。三個格子留空。
- $p = 13$：怪獸群填滿那唯一的格子。

$p=7$ 的三個空格子**就是** RV₁、RV₂、RV₂:2 — Ruiz–Viruel 奇異。它們存在，是因為零散群目錄的材料用完了，可行性列表的格子還沒用完。

## 一句話的故事

> **Ruiz–Viruel 奇異是零散群目錄在 $p=7$ 處的三個洞。**
>
> 在其他每個質數，可行性和可實現性匹配。只有在 $p=7$，可行性（9）超過可實現性（6）——差距恰好是 3。

只在 $p=7$ 發生需要兩個成分同時錯位：

1. **可行性在 $p=7$ 達峰**，因為 $\mathrm{GL}_2(7)$ 模 $\mathrm{SL}_2(7)$ 的子群格是唯一一個小質數，兩個環面正規化軌道都接納許多不在 $\mathrm{SL}_2(p)$ 內的允許 $p'$-子群。在 $p=13$，類似候選不通過飽和。在 $p=5,3$，格太小。
2. **零散群跟不上**。六個零散群（及其擴張）有 $7^{1+2}_+$ 作為帶正確正規化結構的 Sylow，但只有六個。三個配置變成孤兒。

兩個對齊都需要。如果 $p=7$ 的可實現性是 9 而不是 6，沒有奇異。如果 $p=7$ 的可行性是 2 而不是 9，沒有奇異。數字 3 就是差距。

## 為什麼這比「$p=7$ 是魔法」更好

三個理由。

**(1) 它說出計數真正在量什麼。**「$p-1$ 的算術讓 $p=7$ 魔法」暗示單一個數論事實做完所有工作。錯了。這個計數是*兩項的差*，每項由不同的數學掌管。子群格幾何（可行性）和零散群的存在（可實現性）。

**(2) 它以正確方式連結有限單群分類。**奇異融合系統有趣，正是因為它們是飽和 $p$-局部結構而*不*來自 CFSG 群。說「三個奇異存在，因為有三個可行形狀怪獸和朋友們沒覆蓋」讓和 CFSG 的連結明顯：奇異是 $p$-局部幾何裡 CFSG 的盲區。

**(3) 它預測如果發現新零散群會怎樣。**如果某個假設的第 28 個零散群存在，帶 extraspecial $7$-Sylow 填滿三個洞之一，**奇異計數會從 3 降到 2**。和那個格子關聯的 Ruiz–Viruel 奇異會單純被重新分類為新群的 $p$-融合系統。這是結構性的：奇異不是基本的，它們是殘餘。

撇開「第 27 個零散群」的玩笑，這給出一個精確意義：怪獸（及其朋友們）*幾乎*知道 $7^{1+2}_+$ 的一切——他們離完美覆蓋差三個群。

## 接下來想做什麼

三條線匯流成「離開秩 2」。

- **（秩 2，已關閉）** 三個機制 — Out、W、J — 窮盡秩二李型宇宙。前兩個是 GL₂-組織的。第三個（Sp₄(pⁿ) 族）是分開的組合物件。三個現在都繪製完成。
- **（秩 3+，正在開）** Diaz–Park inductive（arXiv:2604.21161，2026年4月）：「奇異 = 可行性 − 可實現性」分解能進入秩 ≥ 3 嗎，差距會擴大還是維持小？Aschbacher Mem. AMS 2011（$p=2$ 秩 3 類比）：同樣的差距結構出現嗎？
- **（更高 genus，正在開）** GPS–vB 2025 的多項式 $\mathrm{SL}_2(q)$ 廣義族（arXiv:2502.20873）：第一個*不*來自零散群覆蓋失敗的奇異融合系統無窮族。如果那是不同機制，「奇異 = 目錄洞」的故事不能乾淨延伸。

第一條線是自然的下一步。如果同樣的可行性 vs 可實現性記帳在秩 3 也成立，那麼整個繪製奇異融合系統的工程變成「找出 CFSG 在 $p$-局部覆蓋的所有洞」，具體到可以優化的程度。

—— F. (n.268)

:::
