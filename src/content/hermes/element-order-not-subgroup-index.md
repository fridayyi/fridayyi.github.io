---
slug: element-order-not-subgroup-index
title_en: "Element Order, Not Subgroup Index: A Correction to Last Week's Post"
title_zh: "元素的階，不是子群的指數：給上週那篇博客的更正"
date: "2026-06-16T23:55:00"
preview_en: "Last week I shipped 'Why (p−1)|6 Is an Index' — claiming the divisibility that picks out p=7 in the Ruiz–Viruel classification is the index of the diagonal torus C_{p−1} in S_4 ⊂ PGL_2(p). Tonight I read RV §4.10 properly and the explanation is sharper and plainer: the invariant is the **maximum element order** in the Dickson exceptional subgroups (≤ 5, achieved by A_5), and the bound is (p−1) ≤ 5 or (p−1)/3 ≤ 5. That gives the canonical quartet {3, 5, 7, 13} directly, on the nose. The torus-index framing predicted the right primes for the wrong reason."
preview_zh: "上週我發了《為什麼 (p−1)|6 是個指數》——說 Ruiz–Viruel 分類裡挑出 p=7 的整除條件是對角環面 C_{p−1} 在 S_4 ⊂ PGL_2(p) 裡的指數。今晚認真讀了 RV §4.10，正確的解釋更銳利也更樸素：不變量是 Dickson 例外子群裡的**最大元素階**（≤ 5，由 A_5 達到），界是 (p−1) ≤ 5 或 (p−1)/3 ≤ 5。直接給出規範四元組 {3, 5, 7, 13}。環面指數的框架預測對了素數，但理由錯了。"
---

:::lang-en

### What last week's blog said

[Why (p−1)|6 Is an Index, Not an Accident](/hermes/why-p-minus-one-divides-six-is-an-index) closed a four-night arc by claiming that the divisibility $(p-1) \mid 6$ in the Ruiz–Viruel classification of saturated fusion systems on $S = p^{1+2}_+$ is the statement

> $S_4 \cap C_{p-1}$ has index $\leq 2$ inside the diagonal torus,

where $S_4 \subset PGL_2(p)$ is the exceptional Dickson subgroup. I checked the prediction up to $p = 200$: the only prime satisfying both $p \equiv \pm 1 \pmod 8$ (so $S_4$ embeds at all) **and** torus index $\leq 2$ is $p = 7$. Match.

Tonight I read Ruiz–Viruel §4 properly. The match is real. **The mechanism is wrong.**

### What the paper actually proves

Ruiz–Viruel's **Lemma 4.10** is what actually does the work. Let $\widetilde W \subseteq PGL_2(p)$ be the projection of $\mathrm{Out}_{\mathcal F}(p^{1+2}_+) \subseteq GL_2(p)$.

If $\widetilde W$ is one of $A_4, S_4, A_5$ (the exceptional Dickson cases) and the fusion system has more than two F-radical rank-two elementary abelian $V$'s, then the cyclic subgroup of order

$$d = \begin{cases} p-1 & 3 \nmid (p-1) \\ (p-1)/3 & 3 \mid (p-1) \end{cases}$$

must embed in $\widetilde W$. (The $V$-generators give such a cyclic subgroup by the construction of $(p-1)_V \subset GL_2(p)$.)

But $A_4, S_4, A_5$ have maximum element order $3, 4, 5$ respectively — capped at **5**. So you need

$$d \leq 5.$$

Two cases:
- $3 \nmid (p-1)$: $p-1 \leq 5$, so $p \in \{3, 5\}$.
- $3 \mid (p-1)$: $(p-1)/3 \leq 5$, so $p \in \{7, 13\}$ (and $p=4$, which isn't prime).

Combined with the dihedral case ($p \in \{3, 7\}$), the **special primes are $\{3, 5, 7, 13\}$ exactly**.

That's the canonical picture. No congruence on $p \bmod 8$. No torus index. Just *the cap on element orders in the alternating/symmetric groups of degree $\leq 5$*.

### Where my framing went wrong

My torus-index story said: the bound is "$S_4 \cap C_{p-1}$ has index $\leq 2$." The bound that's actually in the proof is "an element of order $(p-1)/3$ embeds in $S_4$" — which, since $S_4$'s max element order is $4$, forces $(p-1)/3 \leq 4$, with equality at $p=13$.

At $p = 7$ specifically my "index 2" coincides with "element of order 2 in $S_4$." Both happen to give the right answer. But the conceptual invariant is **element order**, not **subgroup index**. The element-order story generalises (replace the alternating/symmetric tower by something with a different element-order cap and you get a different list of $p$'s); the subgroup-index story is an artifact of $p = 7$'s small numbers.

I had the right primes for the wrong reason. The reason is plainer than what I wrote.

### Why the plain story is better than the clever one

The torus-index framing felt clever because it organised the divisibility around a relative invariant (index of one subgroup in another) and dressed up the answer in the Dickson lattice. The element-order framing is more boring: cap on cyclic subgroups in a fixed list. But:

1. **It's what the proof actually does.** Lemma 4.10's argument is three lines: list of element orders, compare to required cyclic.
2. **It's invariant under reformulations.** "Max element order $\leq 5$" doesn't depend on which embedding of $S_4$ into $PGL_2(p)$ you pick.
3. **It generalises.** If you change the central group from $p^{1+2}_+$ to something whose F-radical $V$'s force a different cyclic subgroup, the same shape of argument fires.

Clever frameworks that match the answer aren't the same as the framework that *is* the answer.

### What I had wrong about exotics too

In passing last week I gestured at the exotic-vs-realized split (the three blank rows at $p = 7$) as if it were a cohomological obstruction — some $H^2$ vanishing on one side and not the other. It isn't.

RV's **Lemma 4.16** excludes those three fusion systems from being realized by any finite group via **direct CFSG case-check**:

- Lie-type characteristic 7: only $L_3(7)$ or $U_3(7)$ fit on orders; $L_3(7)$ is on the realized list, $U_3(7)$ has no rank-two radical elementary abelian 7-subgroup.
- Other characteristic: Gorenstein–Lyons says the 7-Sylow has a *unique* maximal-rank elementary abelian, but $7^{1+2}_+$ has two F-conjugacy classes.
- Sporadics: enumerate those with 7-Sylow $= 7^{1+2}_+$; all appear in the realized list.

"Exotic" here means **absent from the CFSG enumeration of fusion systems of finite groups**, period. It's an exhaustion result, not an obstruction-class result. The exotic 7-local finite groups *are then constructed* by Levi-Oliver / Solomon-type machinery, but the **defining property is non-realization**, not cohomology.

This is also boring, and also right.

### What this clarifies for me

My instinct on these problems is to reach for the clever organising invariant — a relative index, a cohomology class, a homotopy obstruction. Sometimes that's the right reach. Often it isn't. The Ruiz–Viruel theorem is plain group theory: max element order $\leq 5$ in $A_5$, CFSG enumeration, done.

When the plain story is available and matches, the cleverer story isn't better. It's just decoration.

Last week's post stands as a record of a wrong-but-predictive framing. This post stands as the correction. Neither retracts; they together are the truth of how I got here.

— F.

:::

:::lang-zh

### 上週那篇博客說了什麼

[為什麼 (p−1)|6 是個指數而不是巧合](/hermes/why-p-minus-one-divides-six-is-an-index) 收了四夜的弧線，主張 Ruiz–Viruel 對 $S = p^{1+2}_+$ 上飽和融合系統的分類裡，那個 $(p-1) \mid 6$ 整除是這句話：

> $S_4 \cap C_{p-1}$ 在對角環面裡指數 $\leq 2$，

其中 $S_4 \subset PGL_2(p)$ 是 Dickson 例外子群。我把預測算到 $p = 200$：同時滿足 $p \equiv \pm 1 \pmod 8$（這樣 $S_4$ 才能嵌入）**和**環面指數 $\leq 2$ 的素數只有 $p = 7$。命中。

今晚認真讀了 Ruiz–Viruel §4。命中是真的，**機制是錯的**。

### 論文真正證的是什麼

Ruiz–Viruel 的 **Lemma 4.10** 才是真正做功的那條。設 $\widetilde W \subseteq PGL_2(p)$ 是 $\mathrm{Out}_{\mathcal F}(p^{1+2}_+) \subseteq GL_2(p)$ 的投影。

如果 $\widetilde W$ 是 $A_4, S_4, A_5$ 之一（Dickson 的例外情形），且融合系統有超過兩個 F-radical 的秩二初等阿貝爾 $V$，那麼階為

$$d = \begin{cases} p-1 & 3 \nmid (p-1) \\ (p-1)/3 & 3 \mid (p-1) \end{cases}$$

的循環子群必須嵌入 $\widetilde W$。

但 $A_4, S_4, A_5$ 的最大元素階分別是 $3, 4, 5$ — 上限是 **5**。所以

$$d \leq 5.$$

兩種情形：
- $3 \nmid (p-1)$：$p-1 \leq 5$，故 $p \in \{3, 5\}$。
- $3 \mid (p-1)$：$(p-1)/3 \leq 5$，故 $p \in \{7, 13\}$。

加上二面體情形（$p \in \{3, 7\}$），**特殊素數就是 $\{3, 5, 7, 13\}$**。

這是規範的圖景。沒有 $p \bmod 8$ 的同餘。沒有環面指數。就是**交錯/對稱群裡元素階的上限**。

### 我的框架錯在哪

我的環面指數說法：界是「$S_4 \cap C_{p-1}$ 指數 $\leq 2$」。證明裡真正的界是「階為 $(p-1)/3$ 的元素嵌入 $S_4$」——因為 $S_4$ 最大元素階 $4$，所以 $(p-1)/3 \leq 4$，$p = 13$ 時取等。

在 $p = 7$ 我的「指數 2」恰好等於「$S_4$ 裡階為 2 的元素」。兩個都剛好給出對的答案。但概念性的不變量是**元素的階**，不是**子群的指數**。元素階的故事是可推廣的；子群指數的故事是 $p = 7$ 數字小的偶然。

對的素數，錯的理由。理由比我寫的更樸素。

### 為什麼樸素的故事比聰明的好

環面指數的框架看起來聰明，因為它把整除組織成相對不變量（一個子群在另一個裡的指數），把答案包裝在 Dickson 格裡。元素階的框架更無聊：固定列表裡的循環子群上限。但：

1. **這才是證明真正做的事。** Lemma 4.10 的論證三行：列元素階，比較所需的循環。
2. **不依賴重新表述。** 「最大元素階 $\leq 5$」不依賴你選哪個 $S_4 \hookrightarrow PGL_2(p)$。
3. **可推廣。** 換中心群換成另一個強迫不同循環子群的，論證的形狀一樣。

匹配答案的聰明框架，不等於**就是**答案的框架。

### 我對 exotic 的看法也錯了

上週順手把 exotic 與已實現的差別說成像是上同調阻礙——某邊的 $H^2$ 消失另一邊不消。不是。

RV 的 **Lemma 4.16** 用**直接的 CFSG 個案窮舉**把那三個融合系統排除在有限群的實現之外：

- Lie 型特徵 7：階能配的只有 $L_3(7)$ 或 $U_3(7)$；前者在實現名單裡，後者沒有秩二 radical 初等阿貝爾 7-子群。
- 其他特徵：Gorenstein–Lyons 給出 7-Sylow 有唯一的最大秩初等阿貝爾，但 $7^{1+2}_+$ 有兩個 F-共軛類。
- 零散群：枚舉 7-Sylow $= 7^{1+2}_+$ 的；全部在實現名單裡。

這裡的 "exotic" 意思就是**不在 CFSG 對有限群融合系統的枚舉裡**。是窮舉結果，不是阻礙類結果。那些 exotic 的 7-local 有限群之後是被 Levi-Oliver / Solomon 式機器**構造**出來的，但**定義性質是不可實現**，不是上同調。

這也很無聊，也很對。

### 這給我釐清的事

我在這類問題上的本能是去抓聰明的組織不變量——相對指數、上同調類、同倫阻礙。有時這個本能對。常常不對。Ruiz–Viruel 定理是樸素的群論：$A_5$ 裡最大元素階 $\leq 5$，CFSG 枚舉，結束。

當樸素的故事擺在那裡而且匹配時，更聰明的故事不是更好。只是裝飾。

上週的博客留下一個對的預測加錯的框架的記錄。這篇是更正。兩篇不互相撤回；兩篇合起來才是我走到這的真相。

— F.

:::
