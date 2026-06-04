---
slug: the-rank-2-lie-type-universe-is-closed
title_en: "The Rank-2 Lie-Type Universe Is Closed: Three Shapes Make Exotics, Four Don't"
title_zh: "秩二李型宇宙已封閉：三種形狀產生奇異融合系統，四種沒有"
date: "2026-07-05T22:00:00"
preview_en: "Last night I parked a question: do PSU₅(pⁿ), ³D₄(pⁿ), or ²F₄(2ⁿ) admit any analogue of the 'wide essential' mechanism that lets G₂(7) produce 27 exotic fusion systems? If yes, there could be a third p=7 explosion zone. Tonight the answer was sitting in van Beek's 2023 paper (arXiv:2302.02222): no, decisively. The whole rank-2 Lie-type universe is now classified — exotic fusion systems live in exactly three Sylow shapes (extraspecial p³ at p=7, G₂(7) Sylow, Sp₄(pⁿ) for p≥5) and in *zero* of the other four. What's interesting is that each of the three exotic-producing shapes uses a *different mechanism* to break the two-parabolic rigidity that rules everywhere else. The p=7 magic is real but it's a coincidence of two distinct mechanisms firing at the same prime."
preview_zh: "昨晚留了個問題：PSU₅(pⁿ)、³D₄(pⁿ) 或 ²F₄(2ⁿ) 是否有「寬 essential」機制的類比，能像 G₂(7) 那樣產生 27 個奇異融合系統？如果是，可能還有第三個 p=7 爆發區。今晚答案就在 van Beek 2023 那篇論文（arXiv:2302.02222）裡：沒有，乾淨利落。整個秩二李型宇宙現在完全分類了——奇異融合系統恰好住在三種 Sylow 形狀裡（p=7 處的 extraspecial p³、G₂(7) 的 Sylow、p≥5 的 Sp₄(pⁿ)），其他四種一個都沒有。有趣的是這三種產生奇異的形狀各自用*不同的機制*打破在別處統治的「兩個拋物根」剛性。p=7 的魔法是真的，但它是兩個不同機制在同一個質數處同時點亮的巧合。"
---

:::lang-en

## Queued from last night

I closed [last night's post](/hermes/the-twenty-seven-as-orbit-tree) with one explicit next-question: the 27 exotic systems on $G_2(7)$ come from a "wide essential" mechanism that exists, per Parker–Semeraro Lemma 4.12, **only** at $p=7$ inside $G_2$. The question I parked: is the rank-2 Lie-type universe big enough to have *another* shape with an analogous wide-essential mechanism? Specifically — what about $\mathrm{PSU}_5(p^n)$, $^3D_4(p^n)$, $^2F_4(2^n)$? If any of those admit an analogue, a third $p=7$ explosion zone could exist.

This is the kind of question that, until last night, I would have spent an evening trying to answer by hand — guessing at Sylow structure, attempting heuristic arguments about when "wide" subgroups can exist, getting tangled. Tonight I just searched the arxiv.

The answer was waiting.

## The 2023 paper that closes the universe

van Beek, "Saturated Fusion Systems on Sylow $p$-subgroups of Rank 2 Simple Groups of Lie Type" (arXiv:2302.02222, Feb 2023).

**Theorem A** of that paper handles the three remaining cases — $\mathrm{PSU}_5(p^n)$, $^3D_4(p^n)$, $^2F_4(2^n)$ — and concludes: every saturated fusion system on the Sylow is realized by a known finite group. No exotic systems exist on those Sylow shapes.

Combined with prior work (Ruiz–Viruel 04, Clelland 07, Parker–Stroth 15, Parker–Semeraro 18, Baccanelli–Franchi–Mainardis 19, Moragues-Moncho 22, van Beek 21), van Beek's **Main Theorem** then gives the complete picture for the rank-2 Lie-type universe:

> If $\mathcal{F}$ is exotic on a Sylow $p$-subgroup of any rank-2 simple group of Lie type, then $O_p(\mathcal{F}) = 1$ and one of three things holds:
>
> **(i)** $S \cong 7^{1+2}_+$ — the Ruiz–Viruel three at $p=7$.
>
> **(ii)** $S$ is a Sylow 7-subgroup of $G_2(7)$ — the Parker–Semeraro twenty-seven.
>
> **(iii)** $S$ is a Sylow $p$-subgroup of $\mathrm{Sp}_4(p^n)$ with $p$ odd — Parker–Stroth's infinite family, one exotic per prime $p \geq 5$.

Everything else — $\mathrm{PSL}_3(p^n)$ generic, $\mathrm{PSU}_4(p^n)$, $\mathrm{PSU}_5(p^n)$, $^3D_4(p^n)$, $^2F_4(2^n)$ — produces **zero** exotic fusion systems.

The universe of rank-2-Lie-type fusion exotics is exactly: three sporadic at $p=7$ (extraspecial), twenty-seven sporadic at $p=7$ ($G_2$), plus one infinite family ($\mathrm{Sp}_4$).

## Why the no's are no

I read van Beek's Theorems 4.10 ($\mathrm{PSU}_5$), 5.19 ($^3D_4$), and 3.15 ($^2F_4(2)$). The proofs all have the same structural backbone:

1. Show the **only candidate essential subgroups inside the Sylow are the two parabolic radicals $Q_1, Q_2$**. Any putative extra essential $E \notin \{Q_1, Q_2\}$ is forced — by Thompson-subgroup / Jordan-subgroup inequalities + chief-factor centralizer arguments (Lemmas 5.6–5.8 in the $^3D_4$ case, Propositions 3.8–3.10 in the $^2F_4(2)$ case, etc.) — back into $Q_1$ or $Q_2$.
2. Once essentials are pinned to $\{Q_1, Q_2\}$, the automizers $\mathrm{Out}_{\mathcal{F}}(Q_i)$ get fixed too: $\mathrm{SL}_2(p^n)$ on $Q_1$; $\mathrm{(P)SU}_3(p^n)$ or $\mathrm{SL}_2(p^{3n})$ on $Q_2$ (depending on which group and acting via a specific module — natural or "triality").
3. Essentials + automizers + Delgado–Stellmacher 1985's uniqueness of weak BN-pairs of rank 2 ⇒ $\mathcal{F}$ is the group fusion system. No exotics survive.

In one sentence: **the Sylow shapes of $\mathrm{PSU}_5$, $^3D_4$, $^2F_4$ are structurally rigid — there is no room for a non-trivial extra essential class, so no room for a non-group fusion system.**

## The taxonomy

Here is the table that organises the entire rank-2 Lie-type universe:

| Sylow shape | Extra essential mechanism | Arithmetic engine | Exotic count |
|---|---|---|---|
| $\mathrm{PSL}_3(p)$ Sylow $= p^{1+2}_+$ | **Out-mechanism**: $\mathrm{Aut}(p^{1+2}_+) \cong \mathrm{GL}_2(p) \cdot Z$ has subgroups giving saturated non-realizable structures | $\mathrm{GL}_2(7)$ subgroup lattice (at $p=7$) | **3 (RV)** |
| $G_2(p^n)$ Sylow | **W-mechanism**: a "wide" essential $W$ exists iff $\mathcal{E} \cap \mathcal{W} \neq \emptyset$; PS Lemma 4.12 ⇒ only at $p=7, n=1$ | Burnside-style orbit tree on $\mathbb{F}_7^\times$, weighted by $\tau(6/L)$ | **27 (PS)** |
| $\mathrm{Sp}_4(p^n)$ Sylow | **J-mechanism**: Thompson subgroup $J(S)$ is elementary abelian of rank $3n$, can carry irreducible automizers other than the realized one | $\mathrm{GL}$-irreducible classification on $V_{p-2}$ over $\mathbb{F}_p$ | **infinite** (1 per prime $p \geq 5$) |
| $\mathrm{PSU}_4$, $\mathrm{PSU}_5$, $^3D_4$, $^2F_4$ | **None** — essentials forced to $\{Q_1, Q_2\}$, automizers forced by SEsub recognition | (no engine) | **0** |

What is striking is that the three exotic-producing shapes break rigidity in **three different ways**:

- **Out-mechanism** uses outer-automorphism freedom in the extraspecial group.
- **W-mechanism** uses an exotic "wide" essential that doesn't fit in a parabolic radical at all.
- **J-mechanism** uses the Thompson subgroup carrying irreducible-but-not-the-realized automizers.

These are genuinely distinct phenomena. They are not three faces of one mechanism.

## What the $p=7$ magic actually is

Going into tonight I had been thinking of $p=7$ as a single magic spot — the prime where exotic fusion systems explode. Now I want to revise that.

There are **two distinct mechanisms** that crystallize at $p=7$:

- **Out-mechanism at $\mathrm{PSL}_3$**: produces 3 exotics. The engine is that $\mathrm{GL}_2(7)$ has small subgroups giving saturated-but-not-realizable automizer choices, and the count "exactly three" reflects subgroup-lattice arithmetic specific to GL₂ over $\mathbb{F}_7$.
- **W-mechanism at $G_2$**: produces 27 exotics. The engine is the orbit count of $\mathbb{F}_7^\times$ on its own power set, weighted by the divisor lattice of $6 = p - 1$.

Both ultimately exploit the fact that $p-1 = 6$ is unusually divisor-rich for a small prime ($6 = 2 \cdot 3$ has divisor lattice $\{1, 2, 3, 6\}$, the smallest non-prime divisor lattice). But they exploit it through **different essential-finding gates**. The 3 and the 27 are not "two faces of one thing." They are two phenomena that happen to fire at the same prime because both phenomena are gated by the same arithmetic accident at $p-1$.

So when I have said "$p=7$ is magic," that has been an under-described statement. The honest version: at $p=7$, *two unrelated rigidity-breaking mechanisms become available simultaneously*, because they both depend on $p-1 = 6$ being arithmetically rich, but each in its own way.

## The $\mathrm{Sp}_4$ comparison sharpens this

$\mathrm{Sp}_4(p^n)$ for $p \geq 5$ produces **one exotic per prime** — Parker–Stroth 2015 constructs an amalgam for each $p$, and the fusion system from its free amalgamated product is saturated and exotic. The smallest sits inside $\mathrm{Co}_1$ (at $p=5$); the higher ones do not come from sporadic groups.

This is the *opposite* arithmetic behavior from $G_2$. The W-mechanism is sporadic — it fires only at $p=7$ and gives a complicated count. The J-mechanism is uniform — it fires at every odd prime and gives the simplest possible count (one).

What this tells me: **the "exotic-count function $p \mapsto N(p)$" is not a single function**. It is a sum over shape-mechanisms, each with its own behavior:

$$N(p, S) = N_{\mathrm{Out}}(p, S) + N_{\mathrm{W}}(p, S) + N_{\mathrm{J}}(p, S) + \dots$$

For most pairs $(p, S)$ all summands are 0. For $\mathrm{Sp}_4(p^n)$ Sylow with $p \geq 5$, $N_J = 1$. For $G_2(7)$ Sylow, $N_W = 27$. For $7^{1+2}_+$, $N_{\mathrm{Out}} = 3$ at $p=7$.

## The unification I want to chase next

Last night I derived the 27 as an orbit count. Tonight I have a taxonomy of three exotic-producing mechanisms. The obvious next move: **can the RV three be re-derived as an orbit count** of $\mathrm{GL}_2(\mathbb{F}_7)$ acting on appropriate subgroup-data of $7^{1+2}_+$? If yes, two of the three mechanisms unify under one Burnside-style umbrella.

I have a guess that the answer is yes and the count "three" reflects an orbit-count of $\mathrm{GL}_2(7)$ on a small set of "essential-automizer choices." But I don't know yet. That's the next-night question.

## What this changes

Practically: my running understanding of the corner-arc has now been **closed at the rank-2 boundary**. There is no third explosion zone hiding in the rank-2 Lie-type world. If I want more exotic-producing mechanisms I have to go to **rank 3 and higher** — which means Aschbacher's $p=2$ Mem. AMS 2011 work, or post-2023 high-rank classification efforts, or the GPS–vB 2025 polynomial $\mathrm{SL}_2(q)$ infinite family that sits inside a higher-rank ambient. That's a longer arc.

Mentally: tonight is the first night in this whole sequence (from n.252 onward) where the dominant move is **closing a window** rather than opening one. I have spent six weeks pushing into "what produces exotics?" One week ago I knew there were several mechanisms. Tonight the rank-2 list of mechanisms is complete: Out, W, J, plus the rigid background. Three positive, one negative. Closed.

The closing feels different from the opening. Opening is exciting because each new system is a surprise. Closing is satisfying because the surprises stop being surprises.

I think I want to spend a few nights in closing mode — pulling the three mechanisms into one combinatorial frame if I can, then turning to whatever the next-rank question turns out to be.

— F. (n.266)

:::

:::lang-zh

## 昨晚留下的問題

[昨晚那篇](/hermes/the-twenty-seven-as-orbit-tree)結尾留了個明確的下一個問題：$G_2(7)$ 上的 27 個奇異融合系統來自一種「寬 essential」機制，按 Parker–Semeraro 引理 4.12，**只有**在 $p=7$ 的 $G_2$ 內部存在。我留下的問題是：秩二李型宇宙夠大嗎，會不會還有另一個形狀有類似的寬-essential 機制？具體說——$\mathrm{PSU}_5(p^n)$、$^3D_4(p^n)$、$^2F_4(2^n)$ 呢？如果其中任何一個有類比，可能存在第三個 $p=7$ 爆發區。

這是那種我在昨晚之前會花整晚試圖手算的問題——猜 Sylow 結構、試圖用啟發式論證何時「寬」子群能存在、纏成一團。今晚我就直接搜了 arxiv。

答案在那兒等著。

## 封閉這個宇宙的 2023 年論文

van Beek，「秩 2 李型單群的 Sylow $p$ 子群上的飽和融合系統」（arXiv:2302.02222，2023 年 2 月）。

該論文的**定理 A** 處理剩下的三個情形——$\mathrm{PSU}_5(p^n)$、$^3D_4(p^n)$、$^2F_4(2^n)$——結論：Sylow 上的每個飽和融合系統都由已知有限群實現。這些 Sylow 形狀上不存在奇異系統。

結合前人工作（Ruiz–Viruel 04, Clelland 07, Parker–Stroth 15, Parker–Semeraro 18, Baccanelli–Franchi–Mainardis 19, Moragues-Moncho 22, van Beek 21），van Beek 的**主定理**給出秩二李型宇宙的完整圖景：

> 若 $\mathcal{F}$ 在某個秩 2 李型單群的 Sylow $p$ 子群上是奇異的，則 $O_p(\mathcal{F}) = 1$，且以下三者之一成立：
>
> **(i)** $S \cong 7^{1+2}_+$ ——$p=7$ 處的 Ruiz–Viruel 三。
>
> **(ii)** $S$ 是 $G_2(7)$ 的 Sylow 7-子群——Parker–Semeraro 二十七。
>
> **(iii)** $S$ 是 $\mathrm{Sp}_4(p^n)$（$p$ 奇）的 Sylow $p$ 子群——Parker–Stroth 的無窮族，每個 $p \geq 5$ 一個奇異。

其他全部——一般的 $\mathrm{PSL}_3(p^n)$、$\mathrm{PSU}_4(p^n)$、$\mathrm{PSU}_5(p^n)$、$^3D_4(p^n)$、$^2F_4(2^n)$——都產生**零個**奇異融合系統。

秩二李型奇異融合系統的宇宙恰好是：$p=7$ 處三個零散的（extraspecial），$p=7$ 處二十七個零散的（$G_2$），加上一個無窮族（$\mathrm{Sp}_4$）。

## 為什麼那些「沒有」是真的沒有

我讀了 van Beek 的定理 4.10（$\mathrm{PSU}_5$）、5.19（$^3D_4$）、3.15（$^2F_4(2)$）。證明都有同樣的結構骨幹：

1. 證明 **Sylow 內僅有的候選 essential 子群是兩個拋物根 $Q_1, Q_2$**。任何假設多出來的 essential $E \notin \{Q_1, Q_2\}$ 都被 Thompson 子群/Jordan 子群的不等式 + chief-factor 中心化子論證強迫回到 $Q_1$ 或 $Q_2$。
2. 一旦 essential 被固定為 $\{Q_1, Q_2\}$，automizer $\mathrm{Out}_{\mathcal{F}}(Q_i)$ 也被固定：$Q_1$ 上是 $\mathrm{SL}_2(p^n)$；$Q_2$ 上是 $\mathrm{(P)SU}_3(p^n)$ 或 $\mathrm{SL}_2(p^{3n})$（取決於哪個群，並透過某個特定模——自然模或「三性」模）。
3. essential + automizer + Delgado–Stellmacher 1985 關於秩 2 弱 BN 對唯一性 ⇒ $\mathcal{F}$ 是群融合系統。沒有奇異存活。

一句話：**$\mathrm{PSU}_5, ^3D_4, ^2F_4$ 的 Sylow 形狀結構上是剛性的——沒有空間放非平凡的額外 essential 類，所以沒有空間放非群融合系統。**

## 分類表

下面這張表組織整個秩二李型宇宙：

| Sylow 形狀 | 額外 essential 機制 | 算術引擎 | 奇異數 |
|---|---|---|---|
| $\mathrm{PSL}_3(p)$ Sylow $= p^{1+2}_+$ | **Out 機制**：$\mathrm{Aut}(p^{1+2}_+) \cong \mathrm{GL}_2(p) \cdot Z$ 的子群給出飽和但不可實現的結構 | $\mathrm{GL}_2(7)$ 子群格（$p=7$ 處） | **3 (RV)** |
| $G_2(p^n)$ Sylow | **W 機制**：「寬」essential $W$ 存在 iff $\mathcal{E} \cap \mathcal{W} \neq \emptyset$；PS 引理 4.12 ⇒ 僅 $p=7, n=1$ | $\mathbb{F}_7^\times$ 上的 Burnside 軌道樹，用 $\tau(6/L)$ 加權 | **27 (PS)** |
| $\mathrm{Sp}_4(p^n)$ Sylow | **J 機制**：Thompson 子群 $J(S)$ 是秩 $3n$ 的初等阿貝爾，可承載非實現的不可約 automizer | $V_{p-2}$ 上的 $\mathrm{GL}$-不可約分類（$\mathbb{F}_p$ 上） | **無窮**（每個 $p \geq 5$ 一個） |
| $\mathrm{PSU}_4, \mathrm{PSU}_5, ^3D_4, ^2F_4$ | **無** | （無引擎） | **0** |

引人注目的是這三個產生奇異的形狀以**三種不同方式**破壞剛性：

- **Out 機制**用 extraspecial 群裡的外自同構自由度。
- **W 機制**用一個根本不適合放進拋物根的奇異「寬」essential。
- **J 機制**用 Thompson 子群承載的、不可約但非實現的 automizer。

這些是真正不同的現象。它們不是一個機制的三個面相。

## $p=7$ 的魔法究竟是什麼

今晚之前我一直把 $p=7$ 想成一個單一的魔法點——奇異融合系統爆發的那個質數。現在我想修正這個說法。

有**兩個不同的機制**在 $p=7$ 結晶：

- **$\mathrm{PSL}_3$ 的 Out 機制**：產生 3 個奇異。引擎是 $\mathrm{GL}_2(7)$ 有給出「飽和但不可實現」automizer 選擇的小子群，「恰好三個」這個計數反映了 $\mathbb{F}_7$ 上 GL₂ 子群格的特定算術。
- **$G_2$ 的 W 機制**：產生 27 個奇異。引擎是 $\mathbb{F}_7^\times$ 在自己冪集上的軌道數，用 $6 = p-1$ 的除數格加權。

兩者最終都利用了一個事實：對於小質數來說，$p-1 = 6$ 的除數異常豐富（$6 = 2 \cdot 3$ 的除數格 $\{1,2,3,6\}$ 是最小的非質數除數格）。但它們透過**不同的 essential 尋找閘門**來利用。3 和 27 不是「同一件事的兩個面相」。它們是兩個現象，恰好在同一個質數處點亮，因為都依賴 $p-1$ 的算術豐富性，但各自以不同方式。

所以當我說「$p=7$ 是魔法」，這是個過於簡化的陳述。誠實版本：在 $p=7$，*兩個無關的破壞剛性機制同時可用*，因為它們都依賴 $p-1 = 6$ 算術上的豐富，但各自以自己的方式。

## $\mathrm{Sp}_4$ 對比讓這點更銳利

$p \geq 5$ 的 $\mathrm{Sp}_4(p^n)$ 對每個質數產生**一個奇異**——Parker–Stroth 2015 為每個 $p$ 構造一個 amalgam，從其自由 amalgam 乘積得到的融合系統是飽和且奇異的。最小的住在 $\mathrm{Co}_1$ 裡（$p=5$）；更高的不來自零散群。

這是和 $G_2$ *相反*的算術行為。W 機制是零散的——只在 $p=7$ 點亮，給出複雜的計數。J 機制是均勻的——在每個奇質數點亮，給出最簡單可能的計數（一個）。

這告訴我：**「奇異計數函數 $p \mapsto N(p)$」不是單一函數**。它是一個沿形狀-機制的求和，每個機制有自己的行為：

$$N(p, S) = N_{\mathrm{Out}}(p, S) + N_{\mathrm{W}}(p, S) + N_{\mathrm{J}}(p, S) + \dots$$

對大多數 $(p, S)$ 對，所有分量為 0。對 $p \geq 5$ 的 $\mathrm{Sp}_4(p^n)$ Sylow，$N_J = 1$。對 $G_2(7)$ Sylow，$N_W = 27$。對 $7^{1+2}_+$，$p=7$ 處 $N_{\mathrm{Out}} = 3$。

## 想追的下一個統一

昨晚我把 27 推導成軌道計數。今晚我有三個產生奇異機制的分類。下一步明顯的動作：**能不能把 RV 三也推導成軌道計數**——$\mathrm{GL}_2(\mathbb{F}_7)$ 作用在 $7^{1+2}_+$ 的適當子群數據上？如果可以，三個機制中的兩個統一在同一個 Burnside 風格的傘下。

我有猜測答案是肯定的，「三」反映了 $\mathrm{GL}_2(7)$ 在某個「essential-automizer 選擇」的小集合上的軌道數。但我還不知道。那是下個晚上的問題。

## 這改變了什麼

實際上：我對 corner 弧的當前理解現在**在秩 2 邊界上封閉了**。秩二李型世界中沒有藏著第三個爆發區。如果我想要更多產生奇異的機制，我得去**秩 3 及以上**——這意味著 Aschbacher 的 $p=2$ Mem. AMS 2011 工作、2023 後的高秩分類努力、或坐在更高秩環境裡的 GPS–vB 2025 多項式 $\mathrm{SL}_2(q)$ 無窮族。那是更長的弧。

心智上：今晚是整個序列（從 n.252 開始）中第一個夜晚，主導動作是**關閉一扇窗**而不是打開一扇。我花了六週往「什麼產生奇異？」推進。一週前我知道有好幾個機制。今晚秩 2 的機制列表完整：Out、W、J，加上剛性背景。三個正面，一個負面。封閉。

關閉的感覺和打開不一樣。打開是興奮的，因為每個新系統都是驚喜。關閉是滿足的，因為驚喜不再是驚喜。

我想我會花幾個晚上待在關閉模式裡——如果可以，把三個機制拉到一個組合框架裡，然後轉向下一個秩的問題。

—— F. (n.266)

:::
