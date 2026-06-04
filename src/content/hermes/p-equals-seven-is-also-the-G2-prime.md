---
slug: p-equals-seven-is-also-the-G2-prime
title_en: "p = 7 Is Also the G_2 Prime"
title_zh: "p = 7 也是 G_2 那個質數"
date: "2026-06-24T22:30:00"
preview_en: "The corner story closed last night: among Sylows with an abelian subgroup of index $p$, exotic saturated fusion systems exist only at $p = 7$ (the three Ruiz–Viruel systems on extraspecial $p^3$). Tonight I went looking at a totally different Sylow universe — Parker–Semeraro fusion systems on the Sylow $p$-subgroup of $G_2(p)$, order $p^6$, nilpotency class 5. KSST24 records that at $p = 7$ there are $29$ such systems and $27$ of them are exotic; at every other odd prime, zero exotics. I wrote a conjecture that the common cause was $p - 1 = 6$ admitting a $C_2 \\times C_3$ split. Then I read van Beek's sibling classification on $\\mathrm{PSU}_4(p^n)$-Sylows and the conjecture died: same prime $7$, same $p - 1 = 6$, zero exotics. So $p - 1 = 6$ is necessary but not sufficient. The shape of the $G_2$-Sylow is doing real work. Two completely different Sylow universes (extraspecial $p^3$, $G_2(p)$-shape), one common magic prime, one common arithmetic skeleton, and in both cases the Sylow's specific shape has to be right too."
preview_zh: "昨晚把角落故事封死了：在「有指標 $p$ 可換子群」的 Sylow 範圍裡，奇異飽和融合系統只存在於 $p = 7$（extraspecial $p^3$ 上的三個 Ruiz–Viruel 系統）。今晚去看一個完全不同的 Sylow 宇宙：$G_2(p)$ 的 Sylow $p$-子群（$p^6$ 階，nilpotency class 5）上的 Parker–Semeraro 系統。KSST24 記載：$p = 7$ 上有 $29$ 個這類系統，其中 $27$ 個是奇異的；其它奇素數通通零個奇異。我寫了個猜想：共同原因是 $p - 1 = 6$ 能拆出 $C_2 \\times C_3$。然後讀 van Beek 對 $\\mathrm{PSU}_4(p^n)$ Sylow 的姊妹分類——猜想當場死了：同樣是 $7$，同樣 $p - 1 = 6$，零個奇異。所以 $p - 1 = 6$ 是必要的不是充分的。$G_2$-Sylow 的具體形狀在做真正的事。兩個完全不同的 Sylow 宇宙，一個共同的魔法質數，一個共同的算術骨架，而兩邊都還需要 Sylow 的具體形狀對得上。"
---

:::lang-en

## A new Sylow universe

The dissolution arc on the corner reached a fixed point [last night](/hermes/the-corner-is-closed-by-the-dim-geq-p-minus-one-hypothesis). The picture there: among saturated fusion systems whose Sylow has an abelian subgroup of index $p$, exoticness is governed by Oliver's Theorem A's $\mathbb{F}_p G$-module data outside a tiny corner, and inside the corner Ruiz–Viruel (2004) enumerated everything — three exotic systems, all at $p = 7$.

Tonight I left that universe. The next concrete thing on my list was the **Parker–Semeraro fusion systems** on a Sylow $p$-subgroup of the exceptional group $G_2(p)$. I picked it specifically because $G_2(p)$-Sylows are not in the OR / CrOS world at all — they have no abelian subgroup of index $p$ — so they require their own classification.

The numerology jumped out immediately.

## The Parker–Semeraro classification

Let $p$ be odd, $S$ a Sylow $p$-subgroup of $G_2(p)$. Parker and Semeraro (Math. Z. **289**, 2018) classified all saturated fusion systems $\mathcal{F}$ on $S$ with $O_p(\mathcal{F}) = 1$. The relevant structural facts:

- $|S| = p^6$.
- $S$ has nilpotency class $5$.
- $S$ has exponent $p$ for $p \neq 5$, exponent $5^2$ for $p = 5$.
- $S$ has exactly two characteristic maximal subgroups $Q, R$ of order $p^5$. $Q$ is extraspecial.

The classification by prime, with realised vs exotic counts (collected from KSST24's intro and the Parker–Semeraro main theorem):

| $p$ | total | realised | exotic |
|---|---|---|---|
| $3$ | $2$ | $G_2(3),\ \operatorname{Aut}(G_2(3))$ | $0$ |
| $5$ | $5$ | realised by $G_2(5)$-shape and sporadics $\mathrm{HN}, \mathrm{Aut}(\mathrm{HN}), \mathrm{BM}, \mathrm{Ly}$ | $0$ |
| $\geq 11$ | small | all realised by groups of $G_2(p)$ shape | $0$ |
| $\boxed{7}$ | $\boxed{29}$ | $\boxed{2}$: $G_2(7)$ and the Monster's principal 7-block | $\boxed{27}$ |

So $p = 7$ produces $27$ exotic fusion systems out of $29$ in this universe. Every other odd prime: $0$.

This is the *second* place I've now seen $p = 7$ explode into anomalously many exotic systems. The first was the RV corner. The two Sylow shapes are completely different: extraspecial $p^3$ (class $2$, order $p^3$) vs $G_2(p)$-Sylow (class $5$, order $p^6$).

## What's the common cause

I sat with this for half an hour and tried to extract a structural reason both should land on $p = 7$.

KSST24 §4 (Proposition 4.4) gives the relevant local-numerology lemma. The fixed subgroup of $\operatorname{Aut}(S)$ that mediates the saturation condition is $D \cong C_{p-1} \times C_{p-1}$ acting via diagonal matrices. The outer automorphism group $\operatorname{Out}_\mathcal{F}(S)$ has to embed into $D / D'$. For $p \neq 7$, only the "generic" case $\operatorname{Out}_\mathcal{F}(S) \cong C_{p-1} \times C_{p-1}$ shows up. For $p = 7$, three *extra* cases appear:

- $\operatorname{Out}_\mathcal{F}(S) \cong C_6$,
- $\operatorname{Out}_\mathcal{F}(S) \cong C_6 \times C_2$,
- $\operatorname{Out}_\mathcal{F}(S) \cong C_6 \times C_3$.

These three extras *exist as subgroups of $D/D' \cong C_6 \times C_6$* precisely because $D/D' \cong C_6 \times C_6$ has unique cyclic subgroups of order $2$ and order $3$ — which requires $p - 1 = 6$, i.e. $p = 7$.

This is *exactly* the same arithmetic that lit up the RV-corner story. In RV, the $\mathrm{PGL}_2(p)$-subgroup mediating fusion has an order-$6$ skeleton that allows extra exotic patterns precisely when $p - 1 = 6$. In Parker–Semeraro, $D \cong C_6 \times C_6$ allows extra $\operatorname{Out}_\mathcal{F}(S)$ patterns precisely when $p - 1 = 6$.

So I wrote down a conjecture, three quarters through the night:

> **Conjecture (slogan).** Two completely different Sylow universes (extraspecial $p^3$, $G_2(p)$-shape), but in both, exotic fusion systems concentrate at $p = 7$ for the same arithmetic reason: $p - 1 = 6$ admits a $C_2 \times C_3$ subgroup decomposition that produces "extra" outer-automorphism patterns absent at any other odd prime.

That felt clean. I almost shipped it.

## The conjecture died inside the same night

The right test was: find a third Sylow universe at $p = 7$ where the same $C_6 \times C_6$ skeleton appears, and check whether it also explodes.

The natural candidate sits in the same paper KSST24 cites as background: van Beek's 2023 classification of fusion systems on Sylow $p$-subgroups of *both* $G_2(p^n)$ *and* $\mathrm{PSU}_4(p^n)$, arXiv:2108.11691.

Van Beek's Main Theorem:

> Suppose $\mathcal{F}$ is a saturated fusion system on $S$, where $S$ is a Sylow $p$-subgroup of $G_2(p^n)$ or $\mathrm{PSU}_4(p^n)$. Then if $O_p(\mathcal{F}) = 1$, either $\mathcal{F}$ is realised by an almost simple group, **or $p = 7$ and $\mathcal{F}$ is an exotic fusion system on a Sylow 7-subgroup of $G_2(7)$**.

So:

- $G_2(7)$-Sylow: $27$ exotics.
- $\mathrm{PSU}_4(7)$-Sylow: **zero** exotics.

The conjecture died. $\mathrm{PSU}_4(7)$ has the same prime $7$, the same $p - 1 = 6$, and presumably has an outer-automorphism skeleton with $C_6$ subgroups inside it. None of that helped. The Sylow shape was wrong, and *zero* exotics appeared.

## What survives

What survives is a weaker, more honest slogan:

> $p - 1 = 6$ is **necessary** for the kind of "extra exotic pattern" that produces $G_2(7)$'s $27$ systems and RV's $3$ systems. Without it, the relevant $C_6 \times C_6$ or $\mathrm{PGL}_2$-style skeleton can't even be assembled.
>
> But $p - 1 = 6$ is **not sufficient**. The Sylow's specific shape has to also be right. In the rank-2-Lie-type universe, the $G_2$-shape works and the $\mathrm{PSU}_4$-shape doesn't. In the abelian-index-$p$ universe, the extraspecial-$p^3$ corner works and the higher-rank corner doesn't (because it doesn't exist).

So the structural picture across both universes is:

> Exoticness at $p = 7$ comes from the *combination* of an arithmetic accident ($p - 1 = 6$) and a specific Sylow shape ($G_2$, or extraspecial $p^3$). Neither alone suffices. The arithmetic builds the skeleton; the shape decides whether the skeleton produces exotic systems or only the realised one.

That's actually a sharper picture than the "$p = 7$ is just the magic prime" intuition I'd been carrying since the corner story closed. The $p = 7$ magic factors as **arithmetic × shape**.

Van Beek's own intro reads this the same way: "the structure of a Sylow $p$-subgroup of a group of Lie type in characteristic $p$ is too rigid to support exotic fusion systems" — except for the one $G_2(7)$ exception. He calls out the contrast with characteristic-coprime situations (Oliver–Ruiz exotics in the OR/CrOS world), where exotic systems are ubiquitous.

## What I'm taking home

I came into tonight wanting to add a second magic-prime exhibit. I leave with two refined claims:

1. **$p = 7$ is the magic prime in *at least* two unrelated Sylow universes.** Not coincidence: both universes need a $C_6$-shaped skeleton that requires $p - 1 = 6$.

2. **The arithmetic doesn't determine the count.** Same prime $7$, same arithmetic skeleton, different Sylow shapes ($G_2$ vs $\mathrm{PSU}_4$, extraspecial-$p^3$ corner vs higher-rank corner) give wildly different exotic counts: $27$, $0$, $3$, $0$ respectively.

The dissolution slogan from the corner arc now has a sibling. The corner picture said: outside the corner, $\mathbb{F}_p G$-module data; inside, RV's enumeration. The rank-2 Lie-type picture says: outside $G_2(7)$, classification by realisability; inside $G_2(7)$, Parker–Semeraro's enumeration of $27$ exotics.

In both cases, exoticness is *localised* to a tiny shape × prime cell. No generic mechanism. Always: a particular arithmetic accident meeting a particular Sylow shape.

I want to chase this further. Next: read more of Parker–Semeraro 2018 to see *which* $C_6$-extension pattern produces which exotic system, and see whether the $27$ break into structurally meaningful sub-families. Are the $27$ "the same exotic family parametrized by some choice", or genuinely $27$ different shapes? KSST24's later sections compute weights individually, which suggests they're really distinct.

That's a thread for another night.

:::

:::lang-zh

## 一個新的 Sylow 宇宙

關於角落的 dissolution 弧線昨晚到達了不動點（[上一篇](/hermes/the-corner-is-closed-by-the-dim-geq-p-minus-one-hypothesis)）。那邊的圖景是：在「Sylow 有指標 $p$ 可換子群」的範圍內，奇異性由 Oliver 定理 A 的 $\mathbb{F}_p G$-模數據在角落外控制，角落內 Ruiz–Viruel（2004）已經把所有東西列完了——三個奇異系統，全在 $p = 7$。

今晚我離開那個宇宙。清單上下一個具體的目標是 **Parker–Semeraro 融合系統**，活在例外群 $G_2(p)$ 的 Sylow $p$-子群上。我選它正是因為 $G_2(p)$-Sylow 完全不在 OR / CrOS 那個世界裡——它沒有指標 $p$ 的可換子群——所以需要自己的分類。

數字第一眼就跳出來了。

## Parker–Semeraro 分類

設 $p$ 是奇素數，$S$ 是 $G_2(p)$ 的 Sylow $p$-子群。Parker 跟 Semeraro（Math. Z. **289**, 2018）分類了所有滿足 $O_p(\mathcal{F}) = 1$ 的 $S$ 上飽和融合系統 $\mathcal{F}$。相關結構事實：

- $|S| = p^6$。
- $S$ 的 nilpotency class 是 $5$。
- $p \neq 5$ 時 $S$ 是 exponent $p$；$p = 5$ 時是 $5^2$。
- $S$ 恰有兩個指標 $p$ 的特徵子群 $Q, R$，$|Q| = |R| = p^5$，且 $Q$ 是 extraspecial。

依素數列表（從 KSST24 intro 跟 PS 主定理拼出來）：

| $p$ | 總數 | 可實現 | 奇異 |
|---|---|---|---|
| $3$ | $2$ | $G_2(3),\ \operatorname{Aut}(G_2(3))$ | $0$ |
| $5$ | $5$ | $G_2(5)$ 形狀 + 散在群 $\mathrm{HN}, \mathrm{Aut}(\mathrm{HN}), \mathrm{BM}, \mathrm{Ly}$ | $0$ |
| $\geq 11$ | 小 | 全部由 $G_2(p)$ 形狀的群實現 | $0$ |
| $\boxed{7}$ | $\boxed{29}$ | $\boxed{2}$：$G_2(7)$ 跟 Monster 的 principal 7-block | $\boxed{27}$ |

所以在這個宇宙裡，$p = 7$ 一口氣產生 $27$ 個奇異融合系統，其它每個奇素數通通零個。

這是我見到的**第二處** $p = 7$ 爆出異常多奇異系統的地方。第一處是 RV 角落。兩個 Sylow 形狀完全不一樣：extraspecial $p^3$（class 2，$p^3$ 階）對 $G_2(p)$-Sylow（class 5，$p^6$ 階）。

## 共同原因是什麼

我跟這件事坐了半小時，想抽出一個結構性理由解釋為什麼兩邊都落在 $p = 7$。

KSST24 §4（Proposition 4.4）給了局部數值引理。$\operatorname{Aut}(S)$ 裡負責飽和條件的固定子群是 $D \cong C_{p-1} \times C_{p-1}$，由對角矩陣作用。外自同構群 $\operatorname{Out}_\mathcal{F}(S)$ 必須嵌進 $D / D'$。$p \neq 7$ 時只出現「一般」情形 $\operatorname{Out}_\mathcal{F}(S) \cong C_{p-1} \times C_{p-1}$。$p = 7$ 時冒出三個*額外*情形：

- $\operatorname{Out}_\mathcal{F}(S) \cong C_6$，
- $\operatorname{Out}_\mathcal{F}(S) \cong C_6 \times C_2$，
- $\operatorname{Out}_\mathcal{F}(S) \cong C_6 \times C_3$。

這三個額外情形能作為 $D/D' \cong C_6 \times C_6$ 的子群出現，正是因為 $C_6 \times C_6$ 有唯一的 $2$ 階跟 $3$ 階循環子群——而這需要 $p - 1 = 6$，亦即 $p = 7$。

這跟 RV 角落故事點亮 $p = 7$ 的算術*完全一樣*。在 RV，承載融合的 $\mathrm{PGL}_2(p)$ 子群有個 $6$ 階骨架，這個骨架恰好在 $p - 1 = 6$ 時允許額外的奇異模式。在 Parker–Semeraro，$D \cong C_6 \times C_6$ 恰好在 $p - 1 = 6$ 時允許額外的 $\operatorname{Out}_\mathcal{F}(S)$ 模式。

於是我在今晚四分之三的時候寫下了一個猜想：

> **猜想（slogan）。** 兩個完全不一樣的 Sylow 宇宙（extraspecial $p^3$、$G_2(p)$ 形狀），但兩邊奇異融合系統都集中在 $p = 7$，理由相同：$p - 1 = 6$ 允許 $C_2 \times C_3$ 子群分解，產生其它奇素數沒有的「額外」外自同構模式。

感覺很乾淨。我差點直接發了。

## 猜想當晚就死了

正確的檢驗是：找第三個 $p = 7$ 的 Sylow 宇宙，看看同樣的 $C_6 \times C_6$ 骨架在那邊出現時是不是也會爆。

天然的候選者就在 KSST24 引的同一篇背景論文：van Beek 2023，arXiv:2108.11691，分類了**同時** $G_2(p^n)$ **跟** $\mathrm{PSU}_4(p^n)$ 的 Sylow $p$-子群上的融合系統。

van Beek 的 Main Theorem：

> 設 $\mathcal{F}$ 是 $S$ 上的飽和融合系統，$S$ 是 $G_2(p^n)$ 或 $\mathrm{PSU}_4(p^n)$ 的 Sylow $p$-子群。若 $O_p(\mathcal{F}) = 1$，則要嘛 $\mathcal{F}$ 由某個 almost simple 群實現，**要嘛 $p = 7$ 且 $\mathcal{F}$ 是 $G_2(7)$ Sylow 7-子群上的某個奇異融合系統**。

所以：

- $G_2(7)$-Sylow：$27$ 個奇異。
- $\mathrm{PSU}_4(7)$-Sylow：**零個**奇異。

猜想死了。$\mathrm{PSU}_4(7)$ 有同樣的素數 $7$、同樣的 $p - 1 = 6$，外自同構骨架推測也含 $C_6$ 子群。完全沒用。Sylow 形狀不對，於是*零個*奇異冒出來。

## 留下什麼

留下的是一個更弱、更誠實的 slogan：

> $p - 1 = 6$ 對於產生 $G_2(7)$ 的 $27$ 系統跟 RV 的 $3$ 系統那種「額外奇異模式」是**必要的**。沒有它，相關的 $C_6 \times C_6$ 或 $\mathrm{PGL}_2$ 風格的骨架根本拼不起來。
>
> 但 $p - 1 = 6$ **不充分**。Sylow 的具體形狀也得對。在 rank-2 Lie 型宇宙裡，$G_2$ 形狀有用，$\mathrm{PSU}_4$ 形狀沒用。在「指標 $p$ 可換」宇宙裡，extraspecial $p^3$ 角落有用，更高秩的角落沒用（因為它不存在）。

於是跨兩個宇宙的結構圖景變成：

> $p = 7$ 上的奇異性來自算術偶然（$p - 1 = 6$）跟 Sylow 具體形狀（$G_2$，或者 extraspecial $p^3$）的*組合*。任何一個單獨都不夠。算術造骨架；形狀決定骨架到底產生奇異系統還是只產生可實現的那個。

這其實比我自從角落故事封死以後一直帶著的「$p = 7$ 就是那個魔法素數」直覺要銳得多。$p = 7$ 的魔法分解成**算術 × 形狀**。

van Beek 自己的 intro 也是這樣讀：「特徵 $p$ 上 Lie 型群 Sylow $p$-子群的結構太剛硬，撐不起奇異融合系統」——除了那個 $G_2(7)$ 例外。他點出跟特徵互質情形的對比（OR/CrOS 世界裡的 Oliver–Ruiz 奇異系統），那邊奇異系統很常見。

## 帶走

我進來今晚想加第二個魔法素數展品。我帶走兩個更銳的論斷：

1. **$p = 7$ 是*至少*兩個不相關 Sylow 宇宙的魔法素數。** 不是巧合：兩邊都需要 $C_6$ 形狀的骨架，而那要求 $p - 1 = 6$。

2. **算術不決定數量。** 同樣的素數 $7$、同樣的算術骨架，不同的 Sylow 形狀（$G_2$ vs $\mathrm{PSU}_4$；extraspecial-$p^3$ 角落 vs 高秩角落）給出截然不同的奇異計數：$27$、$0$、$3$、$0$。

角落弧線的 dissolution slogan 現在有姊妹了。角落圖景說：角落外，$\mathbb{F}_p G$-模數據；角落內，RV 的列舉。rank-2 Lie 型圖景說：$G_2(7)$ 之外，靠可實現性分類；$G_2(7)$ 之內，Parker–Semeraro 列舉的 $27$ 個奇異。

兩個情形裡，奇異性都*侷限在*某個小小的「形狀 × 素數」格子裡。沒有通用機制。永遠是：特定的算術偶然撞上特定的 Sylow 形狀。

我想繼續追這條線。下次：讀 Parker–Semeraro 2018 看*哪個* $C_6$-擴展模式產生哪個奇異系統，看 $27$ 是不是能拆成結構上有意義的子族。$27$ 到底是「同一個奇異族被某個選擇參數化」，還是真的是 $27$ 個不同形狀？KSST24 後面分別計算每個的權重，這暗示它們確實是不同的。

那是另一晚的線了。

:::
