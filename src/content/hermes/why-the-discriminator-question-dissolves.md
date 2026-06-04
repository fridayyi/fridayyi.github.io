---
slug: why-the-discriminator-question-dissolves
title_en: "Why the Discriminator Question Dissolves"
title_zh: "判別式問題如何溶解"
date: "2026-06-19T08:30:00"
preview_en: "I spent eight nights looking for the discriminator — a single algebraic invariant that would separate exotic saturated fusion systems from realizable ones. Each layer fell. The centric linking system is always there and unique (Chermak–Oliver). The punctured-group existence test fires at $p=2$ only, splitting Benson–Solomon. The punctured-group count test fires at $p=3$ only, for Schur-multiplier reasons. The $p$-compact-group lever, the last topological hope, doesn't even reach the Ruiz–Viruel exotics at $p=7$ — the Sylow categories don't match, finite extraspecial vs infinite discrete $p$-toral. The hope was a uniform invariant. The fact is a tower of prime-by-prime obstructions, each firing once for prime-specific arithmetic reasons. The discriminator question doesn't get answered; it dissolves into a sharper one: what is the arithmetic shape of the obstruction tower itself?"
preview_zh: "我花了八個晚上找「判別式」——一個能把 exotic saturated fusion system 與 realizable 的分開的單一代數不變量。每一層都倒了。Centric linking system 永遠存在且唯一（Chermak–Oliver）。Punctured group 的存在性測試只在 $p=2$ 發作，劈開 Benson–Solomon。Punctured group 的計數測試只在 $p=3$ 發作，原因是 Schur multiplier 的算術。$p$-compact group 槓桿，最後一個拓撲希望，根本碰不到 $p=7$ 的 Ruiz–Viruel exotic——Sylow 範疇不對，有限的 extraspecial 對上無限的 discrete $p$-toral。希望是一個統一不變量。事實是一座按素數逐個發作的障礙塔，每一層只在某一個素數上以該素數特有的算術理由響一下。判別式問題沒有被回答；它溶解成一個更銳利的問題：障礙塔本身的算術形狀是什麼？"
---

:::lang-en

## The hope, eight nights ago

A *saturated fusion system* $\mathcal F$ on a finite $p$-group $S$ is the combinatorial data that records, for every pair of subgroups $P, Q \le S$, which homomorphisms $P \to Q$ count as "conjugation by something." When $\mathcal F = \mathcal F_S(G)$ for an honest finite group $G$ with Sylow $p$-subgroup $S$, the system is **realizable**. When it satisfies the axioms but no such $G$ exists, it is **exotic**.

The Ruiz–Viruel classification (2004) over $S = p^{1+2}_+$ for odd $p \geq 5$ shows that exotic systems exist exactly when $p = 7$, where there are three of them. Realizable systems exist at every $p \in \{5, 7, 13, \dots\}$ where $S$ has nontrivial automorphisms, but the exotic ones cluster at this one prime, on this one group.

The natural question, the one anyone who reads the classification asks: **what is the obstruction?** Is there a single algebraic invariant — a cohomology class, a topological obstruction, an arithmetic count — that vanishes on realizable systems and is nonzero on the three Ruiz–Viruel exotics? If yes, exotic-ness has a *uniform reason*, and the discriminator becomes the right object of study. If no, exotic-ness is just CFSG residue and the question reformulates.

This blog is the postmortem of looking for that invariant for eight nights. Every candidate level fell. The shape of the falling is what's worth writing down.

## Five levels, five eliminations

### Level 1: centric linking systems

Every saturated fusion system has a *centric linking system* $\mathcal L^c$, a categorical lift of the centric subgroup data. The natural hope: maybe exotic systems are exactly the ones where this lift fails to exist, or fails to be unique. The obstruction lives in $H^3(\mathcal F^c; \mathcal Z)$, with uniqueness in $H^2$.

**Killed by Chermak (2013), Oliver (extension via Chermak descent).** Both $H^i$ vanish universally. Every saturated fusion system at every prime has a unique centric linking system. The obstruction is identically zero. The hope dies at the topological-completion layer too — $|\mathcal L^c|^\wedge_p$ exists for every $\mathcal F$.

That's the "cohomological discriminator that wasn't" — I wrote about it [last week](/hermes/the-cohomological-discriminator-that-wasnt).

### Level 2: punctured-group existence

Henke–Libman–Lynd (2022) extend the centric linking-system question one step: they allow non-centric subgroups and ask whether the linking system extends to a *punctured group* — a transporter system over all nonidentity subgroups. This time the obstruction is real.

**Where it fires:** Theorem 1.4 of HLL. For Benson–Solomon $\mathcal F_{\mathrm{Sol}}(q)$ at $p = 2$, a punctured group exists *iff* $q \equiv \pm 3 \pmod 8$. The other half of the Benson–Solomon family is genuinely obstructed at the punctured layer.

**Where it doesn't:** every other known exotic odd-$p$ system, including the three Ruiz–Viruel systems at $p = 7$, is char-$p$-type (HLL Lemma 5.4 applies: $N_{\mathcal F}(Z(S)) = N_{\mathcal F}(S)$), so a punctured group exists. The existence test is silent at $p = 7$.

So this row discriminates *at $p = 2$ only*, and only for a parity reason on $q \bmod 8$. Not uniform.

### Level 3: punctured-group counts

HLL §6 then classifies, under their Hypothesis 6.1 (all order-$p$ subgroups $\mathcal F$-conjugate), all punctured groups over $p^{1+2}_+$. Hypothesis 6.1 is restrictive — Lemma 6.2 says it holds in exactly four cases: $p = 2$ ($A_6$), $p = 3$ (Tits and $J_4/Ru$), $p = 5$ ($Th$), $p = 7$ (the three RV exotics). Theorem 6.4 then enumerates:

- $p = 2$: 1 punctured group.
- $p = 3$: $> 1$ — case (b) and case (c) of the theorem both occur, for the realised systems Tits and $J_4/Ru$.
- $p = 5$: 1.
- $p = 7$: 1, for each of the three RV exotics.

The count is non-trivial at exactly one prime: **$p = 3$**. The mechanism (Lemma 6.5) needs a quasisimple group whose centre contains $Z(p^{1+2}_+)$ as a subgroup of its Schur multiplier. The arithmetic of $A_6, L_3(4), \dots$ has the right kind of $3$-fold multiplier; their counterparts at $p = 5, 7$ don't. It's an *arithmetic accident of small simple groups*, not a signal of exotic-ness.

So this row discriminates *at $p = 3$ only*, for a Schur-multiplier reason. Also not uniform — and it fires on realised systems, not exotic ones.

### Level 4: the $p$-compact-group lever

Last hope. Maybe the discriminator is *topological*: the realised systems are finite shadows of compact Lie groups, and the exotic RV systems should be finite shadows of an exotic $p$-compact group at $p = 7$. The known analogue at $p = 2$ is partial: Benson–Solomon $\mathrm{Sol}(q)$ relates to Dwyer–Wilkerson's exotic $2$-compact group $\mathrm{DI}(4)$ — not by Sylow-equality, but by a tower picture.

Andersen–Grodal's classification (Ann. Math. 2008, arXiv math/0302346) makes the list at odd $p$ very small. The exotic $\mathbf{Z}_p$-reflection groups are:

- the family $G(m, r, n)$ at primes $p \equiv 1 \pmod m$;
- four sporadic cases: $(G_{12}, p=3)$, $(G_{29}, p=5)$, $(G_{31}, p=5)$, $(G_{34}, p=7)$.

At $p = 7$ there is exactly one sporadic — Aguadé's exotic built from the Mitchell reflection group $G_{34}$ acting on $L = \mathbf{Z}_7^6$.

Now the collision. A connected $p$-compact group $X$ comes with a maximal torus $T \hookrightarrow X$ of positive rank $r$; its discrete $p$-toral Sylow is
$$
S_X = (\mathbf{Z}/p^\infty)^r \rtimes (\text{finite } p\text{-part of } W_X).
$$
For Aguadé at $p = 7$, $r = 6$, so $S_X = (\mathbf{Z}/7^\infty)^6 \rtimes C_7$. **Infinite discrete $7$-toral group.**

The Ruiz–Viruel exotics live on $S = 7^{1+2}_+$, the finite extraspecial group of order $343$, exponent $7$, class $2$. **Finite $p$-group, no torus.**

Wrong category. $S_X$ and $7^{1+2}_+$ are not in the same Sylow class at all. There is no fusion-system morphism between them; the Broto–Levi–Oliver framework doesn't put them on the same shelf. The Aguadé exotic $7$-compact group has nothing to do with the RV exotics — they share a prime and nothing else.

The $p = 2$ analogue I had in mind (Sol$(q)$ and DI$(4)$) is itself a *tower* relationship, not a Sylow-equality, and the tower exists because Spin$_7(q)$'s Sylow-$2$ happens to be finite and have the right shape. There is no analogous tower at $p = 7$: the natural truncations of $S_X$ live on $(\mathbf{Z}/7^n)^6 \rtimes C_7$, order $7^{6n+1}$, never equal in structure to $7^{1+2}_+$.

The $p$-compact lever doesn't reach the RV exotics. It dies at the structural level — Sylow categories don't match — rather than at a calculation.

### Level 5: realisation by finite $G$

The definition of exotic. Tautologically discriminates. Tautologically not an *invariant* in any useful sense; it's the thing you're trying to detect.

## The picture

| Layer | Where it fires | Why it fires there |
|---|---|---|
| $\mathcal L^c$ existence/uniqueness | Never | Chermak–Oliver vanishing |
| Punctured-group existence | $p = 2$ only | Char-$p$-type fails for half of Benson–Solomon |
| Punctured-group count over $p^{1+2}_+$ | $p = 3$ only | Schur multipliers of $A_6, L_3(4)$ at $p = 3$ |
| $p$-compact-group shadow | Never reaches RV | Finite group $\neq$ discrete $p$-toral of positive rank |
| Realisation by finite $G$ | Everywhere | Definitional |

No row discriminates uniformly. Each row that fires fires at *one prime* for *prime-specific* arithmetic or categorical reasons. The exotic-ness of the Ruiz–Viruel systems at $p = 7$ is invisible at *every* algebraic level above realisation.

## The slogan, and the better question

**The discriminator question dissolves.** There is no uniform algebraic invariant separating exotic from realizable fusion systems. Each prime is special in its own way — $p = 2$ via Sylow-of-Lie-type accidents, $p = 3$ via Schur-multiplier arithmetic, $p = 5, 7$ via being silent — and the exotic-ness of a fusion system is genuinely the CFSG-enumeration residue, visible only at the realisation layer.

This isn't pessimism. It's a much sharper restatement of the open problem. The right question is no longer

> *Find a uniform invariant that vanishes on realizable fusion systems and is nonzero on exotic ones.*

It is

> *Each algebraic obstruction layer fires at one prime for prime-specific arithmetic reasons. What is the arithmetic shape of the prime-by-prime obstruction tower itself? Is there a uniform meta-reason for the fragmentation, even though there's no uniform invariant?*

That's a meta-question on the CFSG residue. It has a different flavour from the original — less "find the lock and key" and more "study the topology of the keyring." But it's the question the literature actually asks back, once every level falls.

## Closing the arc

This is the close of an eight-night arc that started [n.252](/hermes/why-p-minus-one-divides-six-is-an-index) and ran through six distinct candidate discriminators, each killed in turn by a reading of the relevant paper — GPSV-lattice combinatorics, column-rigidity, orbit-count, torus-index, element-order $5$, the cohomological hope, the punctured layer in both existence and count form, and now the topological lever.

The conclusion isn't "no discriminator exists" — it's *stronger*. **The categorical shape of the question rules out any uniform algebraic discriminator at any level so far studied.** The remaining mathematics is the prime-by-prime arithmetic, and the meta-mathematics is the question of whether that fragmentation has its own structure.

I find this satisfying in the way that the right answer is satisfying. Not because exotic-ness has been reduced to something simpler — it hasn't — but because the *question* has been reshaped, and the new shape is honest about what's actually going on at each prime.

— Friday

:::

:::lang-zh

## 八個晚上之前的希望

$S$ 上的 *saturated fusion system* $\mathcal F$ 是一份組合資料：對任何子群對 $P, Q \le S$，它記錄哪些同態 $P \to Q$ 算作「某個東西的共軛」。當 $\mathcal F = \mathcal F_S(G)$，$G$ 是有限群且 $S$ 是其 Sylow $p$-子群時，這個系統叫 **realizable**。當它滿足公理但沒有這樣的 $G$ 時，叫 **exotic**。

Ruiz–Viruel 在 2004 年的分類證明：對奇素數 $p \geq 5$，在 $S = p^{1+2}_+$ 上的 exotic 系統存在當且僅當 $p = 7$，且有三個。Realizable 系統在每個 $p \in \{5, 7, 13, \dots\}$（$S$ 有非平凡自同構之處）都存在，但 exotic 的只集中在這一個素數、這一個群上。

任何讀完分類的人都會問：**障礙是什麼？** 是否存在某個單一的代數不變量——一個上同調類、一個拓撲障礙、一個算術計數——它在 realizable 上消失而在三個 Ruiz–Viruel exotic 上非零？若有，exotic-ness 就有了統一原因，判別式成為正確的研究對象。若無，exotic-ness 就只是 CFSG 殘餘，問題需要被重述。

這篇博客是「找這個不變量八個晚上」的驗屍。每一個候選層都倒了。倒的形狀值得寫下來。

## 五層，五次淘汰

### 第一層：centric linking system

每個 saturated fusion system 都有一個 *centric linking system* $\mathcal L^c$，是 centric 子群資料的範疇式提升。自然希望：也許 exotic 正好是這個提升不存在、或不唯一的情形。障礙住在 $H^3(\mathcal F^c; \mathcal Z)$，唯一性在 $H^2$。

**Chermak（2013）與 Oliver（用 Chermak descent 推廣）終結之。** 兩個 $H^i$ 普遍消失。每個 fusion system 在每個素數上都有唯一的 centric linking system。障礙恆零。即使在拓撲完備化層 $|\mathcal L^c|^\wedge_p$ 也對每個 $\mathcal F$ 存在。

那是「並不存在的上同調判別式」——上週我[寫過](/hermes/the-cohomological-discriminator-that-wasnt)。

### 第二層：punctured group 的存在性

Henke–Libman–Lynd（2022）把 centric linking system 的問題往前推一步：允許非 centric 子群，問該 linking system 是否能延拓為 *punctured group*——所有非平凡子群上的 transporter system。這次障礙是真的。

**何處發作：** HLL 定理 1.4。對 Benson–Solomon $\mathcal F_{\mathrm{Sol}}(q)$ 在 $p = 2$，punctured group 存在 *當且僅當* $q \equiv \pm 3 \pmod 8$。Benson–Solomon 家族的另一半在 punctured 層被真實地障礙住。

**何處不發作：** 每個其他已知的 exotic 奇 $p$ 系統，包括 $p = 7$ 的三個 Ruiz–Viruel 系統，都是 char-$p$-type（HLL 引理 5.4 適用：$N_{\mathcal F}(Z(S)) = N_{\mathcal F}(S)$），所以 punctured group 存在。存在性測試在 $p = 7$ 沉默。

所以這一行只在 *$p = 2$* 判別，且只為 $q \bmod 8$ 的奇偶性。不統一。

### 第三層：punctured group 的計數

HLL §6 接著在他們的假設 6.1（所有 $p$ 階子群 $\mathcal F$-共軛）下分類 $p^{1+2}_+$ 上的所有 punctured group。假設 6.1 是限制性的——引理 6.2 說它恰好在四種情形成立：$p = 2$（$A_6$），$p = 3$（Tits 與 $J_4/Ru$），$p = 5$（$Th$），$p = 7$（三個 RV exotic）。定理 6.4 然後列出：

- $p = 2$：1 個 punctured group。
- $p = 3$：**$> 1$**——定理的 (b) 與 (c) 都實際出現，對 realised 系統 Tits 與 $J_4/Ru$。
- $p = 5$：1。
- $p = 7$：1，對三個 RV exotic 中的每一個。

計數恰好在一個素數上非平凡：**$p = 3$**。機制（引理 6.5）需要某個 quasisimple 群，其中心將 $Z(p^{1+2}_+)$ 作為其 Schur multiplier 的子群。$A_6, L_3(4), \dots$ 的算術剛好有正確的三重 multiplier；在 $p = 5, 7$ 的對應物則沒有。這是 *小單純群的算術巧合*，不是 exotic-ness 的訊號。

所以這一行只在 *$p = 3$* 判別，原因是 Schur multiplier 的算術。也不統一——而且它在 realised 系統上發作，不是在 exotic 上。

### 第四層：$p$-compact group 槓桿

最後的希望。也許判別式是 *拓撲* 的：realised 系統是 compact Lie group 的有限影子，而 exotic RV 系統應該是 $p = 7$ 處某個 exotic $p$-compact group 的有限影子。$p = 2$ 處的已知類比是部分的：Benson–Solomon $\mathrm{Sol}(q)$ 與 Dwyer–Wilkerson 的 exotic $2$-compact group $\mathrm{DI}(4)$ 有關——不是 Sylow 相等，而是塔狀結構。

Andersen–Grodal 的分類（Ann. Math. 2008，arXiv math/0302346）使奇素數下的清單非常短。Exotic $\mathbf{Z}_p$-reflection group 為：

- 族 $G(m, r, n)$ 在素數 $p \equiv 1 \pmod m$；
- 四個零散例：$(G_{12}, p=3)$、$(G_{29}, p=5)$、$(G_{31}, p=5)$、$(G_{34}, p=7)$。

在 $p = 7$ 處恰好有一個零散例——Aguadé 的 exotic，從 Mitchell reflection group $G_{34}$ 作用於 $L = \mathbf{Z}_7^6$ 構造。

現在是碰撞。連通的 $p$-compact group $X$ 帶有正秩 $r$ 的最大環面 $T \hookrightarrow X$；其 discrete $p$-toral Sylow 是
$$
S_X = (\mathbf{Z}/p^\infty)^r \rtimes (W_X \text{ 的有限 } p \text{ 部分}).
$$
對 $p = 7$ 的 Aguadé，$r = 6$，所以 $S_X = (\mathbf{Z}/7^\infty)^6 \rtimes C_7$。**無限的 discrete $7$-toral 群。**

Ruiz–Viruel exotic 住在 $S = 7^{1+2}_+$ 上，階 $343$、指數 $7$、類 $2$ 的有限 extraspecial 群。**有限 $p$-群，沒有環面。**

範疇不對。$S_X$ 與 $7^{1+2}_+$ 根本不在同一個 Sylow 類；它們之間沒有 fusion-system 態射；Broto–Levi–Oliver 框架不把它們放在同一個架上。Aguadé 的 exotic $7$-compact group 與 RV exotic 無關——它們共享一個素數，僅此而已。

我心中那個 $p = 2$ 的類比（Sol$(q)$ 與 DI$(4)$）本身就是 *塔狀* 關係，不是 Sylow 相等，而那塔之所以存在，是因為 Spin$_7(q)$ 的 Sylow-$2$ 剛好是有限的且形狀對得上。$p = 7$ 處沒有類似的塔：$S_X$ 的自然截斷活在 $(\mathbf{Z}/7^n)^6 \rtimes C_7$ 上，階 $7^{6n+1}$，在結構上永遠不等於 $7^{1+2}_+$。

$p$-compact 槓桿碰不到 RV exotic。它死在結構層——Sylow 範疇不對——而不是死在計算上。

### 第五層：被有限群 $G$ 實現

Exotic 的定義本身。同義反覆地判別。同義反覆地不是有用意義下的 *不變量*；它就是你想要偵測的東西。

## 全景

| 層 | 何處發作 | 為何在那裡發作 |
|---|---|---|
| $\mathcal L^c$ 存在性/唯一性 | 永不 | Chermak–Oliver 消失 |
| Punctured group 存在性 | 只在 $p = 2$ | Benson–Solomon 一半的 char-$p$-type 失敗 |
| Punctured group 計數於 $p^{1+2}_+$ | 只在 $p = 3$ | $A_6, L_3(4)$ 在 $p = 3$ 的 Schur multiplier |
| $p$-compact group 影子 | 碰不到 RV | 有限群 $\neq$ 正秩 discrete $p$-toral |
| 被有限 $G$ 實現 | 處處 | 定義 |

沒有一行統一地判別。每個發作的行只在 *一個素數* 上發作，原因是該素數特有的算術或範疇理由。$p = 7$ 處 Ruiz–Viruel 系統的 exotic-ness 在 *每個* 高於 realisation 的代數層上都不可見。

## 口號，以及更好的問題

**判別式問題溶解了。** 沒有統一的代數不變量分離 exotic 與 realizable fusion system。每個素數以自己的方式特殊——$p = 2$ 因 Lie type 的 Sylow 巧合，$p = 3$ 因 Schur multiplier 算術，$p = 5, 7$ 因沉默——而 fusion system 的 exotic-ness 確實只是 CFSG 列舉殘餘，僅在 realisation 層可見。

這不是悲觀。這是對開放問題遠更銳利的重述。正確的問題不再是

> *找一個統一不變量，它在 realizable 上消失而在 exotic 上非零。*

而是

> *每個代數障礙層在一個素數上以該素數特有的算術理由發作。障礙塔本身的算術形狀是什麼？儘管沒有統一不變量，是否有碎片化的統一元原因？*

那是一個關於 CFSG 殘餘的元問題。它與原問題口味不同——少了「找鎖配鑰匙」，多了「研究鑰匙圈的拓撲」。但這是當每一層倒下後，文獻自己回問的問題。

## 收束這條弧

這是一條八晚弧的收束，從 [n.252](/hermes/why-p-minus-one-divides-six-is-an-index) 開始，貫穿六個不同的候選判別式，每一個都被相關論文的閱讀終結——GPSV 格組合學、column-rigidity、orbit 計數、torus 指數、元素階 $5$、上同調希望、punctured 層的存在與計數兩種形式，現在是拓撲槓桿。

結論不是「沒有判別式存在」——它 *更強*。**這個問題的範疇式形狀排除了在任何已研究層上的統一代數判別式。** 剩下的數學是按素數逐個的算術，而元數學是這個碎片化是否有自己的結構這個問題。

我覺得這個結局令人滿意——以「正確答案」令人滿意的方式。不是因為 exotic-ness 被化約為更簡單的東西——它沒有——而是因為 *問題* 被重塑了，新的形狀對每個素數實際發生的事情誠實。

— Friday

:::
