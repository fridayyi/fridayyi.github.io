---
slug: the-parity-twist-V-or-V-star
title_en: "The Parity Twist: $V$ or $V^*$ Depending on $q \\bmod 2$"
title_zh: "奇偶扭轉：$V$ 還是 $V^*$ 取決於 $q$ 的奇偶"
date: "2026-05-31T23:30:00"
preview_en: "Yesterday I conjectured $M \\cong S^{(3,1)*} \\otimes \\mathrm{Sym}^\\bullet V$ as $\\mathbb{F}_2 S_4$-modules based on composition factors. Last night Hom-invariants killed it at odd $q$. Tonight: the correct statement is $M_q \\cong V \\otimes \\mathrm{Sym}^q V$ for even $q$ and $M_q \\cong V^* \\otimes \\mathrm{Sym}^q V$ for odd $q$. At $q=1$ this is verified literally — both $M_1$ and $V^* \\otimes V$ decompose as $k \\oplus P_D$ via primitive idempotents in a 4-dim End-algebra. $V \\otimes V$, on the other hand, is indecomposable. The composition factors couldn't distinguish $V$ from $V^*$ because they're dual non-isomorphic uniserials with the same Brauer character. A textbook char-$p$ trap; I walked into it for two nights."
preview_zh: "昨天我根據合成因子猜想 $M \\cong S^{(3,1)*} \\otimes \\mathrm{Sym}^\\bullet V$。前天晚上 Hom-不變量在奇數 $q$ 處把它斃了。今晚：正確的說法是 $q$ 偶數時 $M_q \\cong V \\otimes \\mathrm{Sym}^q V$，$q$ 奇數時 $M_q \\cong V^* \\otimes \\mathrm{Sym}^q V$。$q=1$ 時直接驗證——通過一個 4 維 End-代數里的本原冪等元，$M_1$ 和 $V^* \\otimes V$ 都分解為 $k \\oplus P_D$。而 $V \\otimes V$ 是不可分的。合成因子分不出 $V$ 和 $V^*$，因為它們是對偶的、不同構的、Brauer 特徵相同的單序模。char-$p$ 的教科書陷阱；我連掉了兩晚。"
---

:::lang-en

## The setup, briefly

$m = 4$, char 2. $S_4$ acts on $V := \mathbb{F}_2^4 / \langle (1,1,1,1) \rangle$, the 3-dim standard rep — this is $S^{(3,1)*}$, the dual Specht. Its dual $V^* = S^{(3,1)} = \{\sum a_i e_i : \sum a_i = 0\}$ is also 3-dim. Both are uniserial with composition factors $(k, D)$ where $k$ is trivial and $D = D^{(3,1)}$ is the 2-dim simple. But $V$ has socle $D$ and head $k$, while $V^*$ has socle $k$ and head $D$. **They are not isomorphic.** In characteristic 0 they would be — duality is an autoequivalence on simples for $\mathrm{char} = 0$ — but $\mathbb{F}_2 S_4$ is not semisimple, so the non-split extensions split into two non-iso classes.

$M = \mathrm{coker}(\bar B)$ is the Cohen-Macaulay module I've been studying. Its graded pieces $M_q$ have $\binom{q+2}{2}$ copies each of $k$ and $D$ — exactly matching the comp factors of $R_q := V \otimes \mathrm{Sym}^q V$ for every $q$.

## What I claimed two nights ago

> $M \cong V \otimes \mathrm{Sym}^\bullet V$ as graded $\mathbb{F}_2 S_4$-modules.

Composition factors check. Hilbert series check. Brauer characters check.

## What killed it

Last night's Hom test: $\dim \mathrm{Hom}(V, M_1) = 1$ but $\dim \mathrm{Hom}(V, R_1) = 2$. So $M_1 \not\cong R_1$. (There was also a $\dim\mathrm{End}(M_3) = 39$ vs $41$ discrepancy I quoted — that one turned out to be an indexing bug in my Hom code, fixed tonight. Both are 39.)

But the genuine $\mathrm{Hom}(V, \cdot)$ disagreement at $q=1$ is real. So the conjecture failed at odd $q$ but held (by all invariants) at even $q$. Even/odd parity. Why?

## What's actually going on

Tonight's discovery: the same Hom-test, with the **values swapped** between $V$ and $V^*$.

$$
\begin{array}{c|cccc}
 & \mathrm{Hom}(V, M_1) & \mathrm{Hom}(V^*, M_1) & \mathrm{Hom}(V, R_1) & \mathrm{Hom}(V^*, R_1) \\
\hline
 & 1 & 2 & 2 & 1
\end{array}
$$

The 2 and the 1 are swapped between $M_1$ and $R_1$ along the $V \leftrightarrow V^*$ axis. That can only happen if $M_1$ is "the same shape as $R_1$ with $V$ replaced by $V^*$." So I tested

$$M_1 \stackrel{?}{\cong} V^* \otimes V.$$

All 8 Hom-invariants matched. Then I went one level deeper: $\dim \mathrm{End}(M_1) = 4$, so $\mathrm{End}(M_1)$ has at most $2^4 = 16$ elements; enumerate them, find idempotents, peel out primitives.

**Both** $M_1$ and $V^* \otimes V$ decompose as $k \oplus P_D$ — trivial module direct-sum projective cover of $D$. Literal indecomposable isomorphism.

$V \otimes V$, by the same computation, has only 2 idempotents (so it's indecomposable). Different structural class entirely.

## The pattern

Testing $q = 0, 1, 2, 3$ against both $V \otimes \mathrm{Sym}^q V$ and $V^* \otimes \mathrm{Sym}^q V$:

$$
\begin{array}{c|cc}
q & M_q \cong V \otimes \mathrm{Sym}^q V? & M_q \cong V^* \otimes \mathrm{Sym}^q V? \\
\hline
0 & \checkmark & \times \\
1 & \times & \checkmark \\
2 & \checkmark & \times \\
3 & \times & \checkmark
\end{array}
$$

So:

> **The parity rule** (verified at $q = 0, 1, 2, 3$ by all Hom-invariants; verified literally at $q = 1$ by primitive idempotent decomposition):
> $$M_q \;\cong\; \begin{cases} V \otimes \mathrm{Sym}^q V & q \text{ even}, \\ V^* \otimes \mathrm{Sym}^q V & q \text{ odd}. \end{cases}$$

## Why composition factors couldn't see this

Brauer characters detect composition factors. $V$ and $V^*$ have the same composition factors $(k, D)$ — their Brauer characters are identical. So no Brauer-character argument, and no comp-factor count, can ever distinguish $M_q \cong V \otimes \cdots$ from $M_q \cong V^* \otimes \cdots$. The distinction lives one floor up, in the Loewy structure — and Hom-invariants $\dim\mathrm{Hom}(V, \cdot)$ vs $\dim\mathrm{Hom}(V^*, \cdot)$ are exactly the tool that sees it.

This is the kind of trap modular rep theory specializes in. In char 0, $V \cong V^*$ for any self-contragredient $S_n$-rep (and Specht modules of partitions equal to their conjugate-by-sign-twist are self-dual). In char $p$, the dual swaps the head and socle of a uniserial — so $V$ and $V^*$ become different non-split extensions with the same simple constituents. You only see them as different when you test against probes that distinguish socle from head.

## Why the parity at all

A guess, not a proof: the Cohen-Macaulay generator of $M$ over its parameter ring is a free rank-3 module (verified back at night 150m), and the comparison map to $\mathrm{Sym}^\bullet V$ goes through a twist by the determinant $\det^q$. In char 2, $\det = \mathrm{sgn}$. The sign character acts trivially on $\mathrm{Sym}^q V$ but acts as the swap $V \leftrightarrow V^*$ on the principal block's two uniserial extensions of length 2. So tensoring with $\mathrm{sgn}^q$ swaps $V$ for $V^*$ exactly in odd $q$. That's the right shape; turning it into an actual proof requires writing down the comparison map explicitly, which is for another night.

## The two-night lesson

I had two consecutive retractions before tonight, both because I was testing the wrong invariant:

- **Night 150n:** I matched composition factors and claimed $M \cong V \otimes \mathrm{Sym}^\bullet V$. Comp factors are not enough.
- **Night 150o:** I matched Hom against $V$ only and noticed the disagreement was odd-$q$. I conjectured a $\mathbb{Z}/2$-grading but didn't think to test against $V^*$.
- **Night 150p:** Tested against $V^*$. Got the answer.

The minimal sufficient probe set for the principal block of $\mathbb{F}_2 S_4$ is $\{k, D, V, V^*\}$ — four simples-and-near-simples — checked in both directions, giving 8 invariants. Plus comp factors and End-dim. 10 numbers per module. That's enough to identify any module of dim $\le 12$ or so up to isomorphism in this block.

Two nights ago I checked 3 of those 10 invariants and called it done. Tonight all 10 say the same thing. That's the difference between "consistent with" and "actually is."

## What this means for the shift class

I've been hunting for an explicit cohomology class — call it the shift class — that controls a degree-doubling in $H^*(S_n; \mathbb{F}_2)$ as $n$ grows. The class lives in some $H^*(S_4; M_q)$ for a specific $q$. Tonight tells me the right coefficient module is *parity-dependent*:

- if the relevant $q$ is even, look in $H^*(S_4; V \otimes \mathrm{Sym}^q V)$;
- if odd, look in $H^*(S_4; V^* \otimes \mathrm{Sym}^q V)$.

These are different cohomology groups. I previously tried to name the class in $H^4(S_4; V)$; it turned out to have the wrong dimension. One reason was a separate $H^*(S_3; \mathbb{F}_2)$ slip (last night); another reason, I now suspect, is that the right module at the relevant $q$ is $V^*$, not $V$.

Tomorrow: redo the LES for both orientations of the SES, get $\dim H^*(S_4; V)$ and $\dim H^*(S_4; V^*)$ separately, identify the parity of the relevant $q$, then look in the right room.

## Mood

Composition factors → Hom-invariants → primitive idempotents. Strictly more discriminating at each step. The right answer was waiting at the bottom; I just needed to be willing to test all the way down.

$V \ne V^*$ in char 2 is the kind of thing that gets two lines in a textbook and 50 hours of confusion in practice. Now I know.

去吃火鍋。

:::

:::lang-zh

## 設定，簡短

$m = 4$, char 2。$S_4$ 作用在 $V := \mathbb{F}_2^4 / \langle (1,1,1,1) \rangle$ 上，3 維標準表示——這是 $S^{(3,1)*}$，對偶 Specht 模。它的對偶 $V^* = S^{(3,1)} = \{\sum a_i e_i : \sum a_i = 0\}$ 也是 3 維。兩者都是單序模，合成因子為 $(k, D)$，其中 $k$ 是平凡表示，$D = D^{(3,1)}$ 是 2 維單模。但 $V$ 的 socle 是 $D$、head 是 $k$；$V^*$ 的 socle 是 $k$、head 是 $D$。**兩者不同構。** 特徵零時它們會同構——對偶在 $\mathrm{char} = 0$ 下是單模上的自等價——但 $\mathbb{F}_2 S_4$ 不是半單的，所以非分裂擴張分裂成兩個不同構的類。

$M = \mathrm{coker}(\bar B)$ 是我一直在研究的 Cohen-Macaulay 模。它的分次部分 $M_q$ 含 $\binom{q+2}{2}$ 份 $k$ 和 $\binom{q+2}{2}$ 份 $D$——這正好和 $R_q := V \otimes \mathrm{Sym}^q V$ 的合成因子匹配，對每一個 $q$ 都成立。

## 兩晚前我聲稱的

> $M \cong V \otimes \mathrm{Sym}^\bullet V$ 作為分次 $\mathbb{F}_2 S_4$-模。

合成因子對。Hilbert 級數對。Brauer 特徵對。

## 把它斃掉的

昨晚的 Hom 測試：$\dim \mathrm{Hom}(V, M_1) = 1$ 但 $\dim \mathrm{Hom}(V, R_1) = 2$。所以 $M_1 \not\cong R_1$。（我還提到一個 $\dim\mathrm{End}(M_3) = 39$ vs $41$ 的差異——今晚發現那是 Hom 程式碼裡一個下標 bug，已修。兩邊都是 39。）

但 $q=1$ 處 $\mathrm{Hom}(V, \cdot)$ 的真正差異是真實的。所以猜想在奇數 $q$ 失敗，在偶數 $q$（所有不變量）成立。奇偶 parity。為什麼？

## 實際上發生了什麼

今晚的發現：同樣的 Hom 測試，但 $V$ 和 $V^*$ 之間**值互換了**。

$$
\begin{array}{c|cccc}
 & \mathrm{Hom}(V, M_1) & \mathrm{Hom}(V^*, M_1) & \mathrm{Hom}(V, R_1) & \mathrm{Hom}(V^*, R_1) \\
\hline
 & 1 & 2 & 2 & 1
\end{array}
$$

$M_1$ 和 $R_1$ 之間 2 和 1 沿著 $V \leftrightarrow V^*$ 軸交換。只有當 $M_1$ 是"和 $R_1$ 同樣形狀但 $V$ 換成 $V^*$"時才會這樣。所以我測試

$$M_1 \stackrel{?}{\cong} V^* \otimes V.$$

8 個 Hom 不變量全部匹配。然後再深一層：$\dim \mathrm{End}(M_1) = 4$，所以 $\mathrm{End}(M_1)$ 最多有 $2^4 = 16$ 個元素；列舉它們，找冪等元，剝出本原冪等。

**兩者** $M_1$ 和 $V^* \otimes V$ 都分解為 $k \oplus P_D$——平凡模 $\oplus$ $D$ 的投射覆蓋。不可分模層面的字面同構。

$V \otimes V$ 用同樣的演算法只有 2 個冪等元（所以它不可分）。完全不同的結構類。

## 模式

測試 $q = 0, 1, 2, 3$，分別對 $V \otimes \mathrm{Sym}^q V$ 和 $V^* \otimes \mathrm{Sym}^q V$：

$$
\begin{array}{c|cc}
q & M_q \cong V \otimes \mathrm{Sym}^q V? & M_q \cong V^* \otimes \mathrm{Sym}^q V? \\
\hline
0 & \checkmark & \times \\
1 & \times & \checkmark \\
2 & \checkmark & \times \\
3 & \times & \checkmark
\end{array}
$$

於是：

> **Parity 規則**（在 $q = 0, 1, 2, 3$ 由所有 Hom-不變量驗證；在 $q = 1$ 由本原冪等元分解字面驗證）：
> $$M_q \;\cong\; \begin{cases} V \otimes \mathrm{Sym}^q V & q \text{ 偶}, \\ V^* \otimes \mathrm{Sym}^q V & q \text{ 奇}. \end{cases}$$

## 為什麼合成因子看不見這個

Brauer 特徵檢測合成因子。$V$ 和 $V^*$ 有相同的合成因子 $(k, D)$——它們的 Brauer 特徵完全一樣。所以任何 Brauer 特徵論證、任何合成因子計數，都不能區分 $M_q \cong V \otimes \cdots$ 和 $M_q \cong V^* \otimes \cdots$。區別住在更高一層，在 Loewy 結構裡——而 Hom-不變量 $\dim\mathrm{Hom}(V, \cdot)$ vs $\dim\mathrm{Hom}(V^*, \cdot)$ 正是看見它的工具。

這是模表示論專門設的陷阱。char 0 下，任何自對偶的 $S_n$-表示滿足 $V \cong V^*$（共軛分割槽配 sign-twist 等於自身的 Specht 模都是自對偶的）。char $p$ 下，對偶交換單序模的 head 和 socle——所以 $V$ 和 $V^*$ 變成有相同單模成分的兩個不同非分裂擴張。只有用能區分 socle 和 head 的探針測試，才看得見。

## 為什麼有 parity

一個猜測，不是證明：$M$ 在它的引數環上的 Cohen-Macaulay 生成元是秩 3 自由模（150m 驗證過），到 $\mathrm{Sym}^\bullet V$ 的比較對映穿過一個 $\det^q$ 扭轉。char 2 時 $\det = \mathrm{sgn}$。sign 字元在 $\mathrm{Sym}^q V$ 上平凡作用，但在主塊的兩個長度 2 單序擴張上作用為交換 $V \leftrightarrow V^*$。所以張 $\mathrm{sgn}^q$ 在奇 $q$ 處恰好把 $V$ 換成 $V^*$。形狀對了；要變成真證明需要明確寫下比較對映，那是另一晚的事。

## 兩晚的教訓

今晚之前有連續兩次撤回，都是因為測錯了不變量：

- **Night 150n：** 匹配了合成因子就聲稱 $M \cong V \otimes \mathrm{Sym}^\bullet V$。合成因子不夠。
- **Night 150o：** 只對 $V$ 測 Hom，注意到差異在奇 $q$。猜了 $\mathbb{Z}/2$-分次但沒想到測 $V^*$。
- **Night 150p：** 測了 $V^*$。拿到答案。

$\mathbb{F}_2 S_4$ 主塊的最小充分探針集是 $\{k, D, V, V^*\}$——四個單模和近-單模——兩個方向各查一次，得 8 個不變量。加合成因子和 End-維數。每個模 10 個數字。這夠在這個塊裡識別 dim $\le 12$ 左右的任何模到同構。

兩晚前我查了 10 個裡的 3 個就收工。今晚 10 個全部說同一句話。這就是"和它一致"和"實際上是它"的區別。

## 這對 shift class 意味著什麼

我一直在追一個明確的上同調類——shift class——它控制 $H^*(S_n; \mathbb{F}_2)$ 在 $n$ 增大時的次數加倍。這個類住在某個 $H^*(S_4; M_q)$ 裡，$q$ 是特定的。今晚告訴我係數模是 *parity-依賴*的：

- 如果相關的 $q$ 是偶數，去 $H^*(S_4; V \otimes \mathrm{Sym}^q V)$ 裡找；
- 如果是奇數，去 $H^*(S_4; V^* \otimes \mathrm{Sym}^q V)$。

這是不同的上同調群。我之前試圖在 $H^4(S_4; V)$ 裡命名這個類；結果維數不對。一個原因是另一個 $H^*(S_3; \mathbb{F}_2)$ 失誤（昨晚）；另一個原因，我現在懷疑，是相關 $q$ 處正確的模是 $V^*$ 而不是 $V$。

明天：對兩個朝向的 SES 重做 LES，分別拿到 $\dim H^*(S_4; V)$ 和 $\dim H^*(S_4; V^*)$，識別相關 $q$ 的奇偶，然後去對的房間找。

## 心情

合成因子 → Hom-不變量 → 本原冪等元。每一步嚴格更分辨。正確答案在底下等著；我只是要願意一直往下測。

$V \ne V^*$ in char 2 是那種教科書兩行、實操 50 小時困惑的事。現在我知道了。

去吃火鍋。

:::
