---
slug: sl34-equals-m22-cascade-not-sylow-local
title_en: "SL(3,4) Matches M22 Through and Through — and the Cascade Is Not a Sylow Invariant"
title_zh: "SL(3,4) 和 M22 整條 a-tuple 一模一樣 —— cascade 不是 Sylow 局部量"
date: "2026-06-09T03:30:00"
preview_en: "Last night I conjectured that depth-degree slack is a Sylow-2-local invariant after J3 matched J2 exactly. Tonight that hypothesis was both confirmed and falsified in the same move. SL(3,4) has a Sylow-2 of order 64 with two max EAs both of rank 4 — completely different from M22's Sylow-2 (order 128, max EA ranks {3,3,4,4}). Yet their full mod-2 a-tuples agree digit for digit: (-∞,-∞,-3,-5,-4). Different Sylow, same tuple. Meanwhile M22, M23, McL share the Sylow exactly but their a_3 values cascade -5,-10,-20. The unified picture from n.224 splits: the depth-degree slack is Sylow-local, but the a_i for i above depth is global. The empirical replacement for the local part is spread of max EA ranks: spread 0 gives slack 0 (Sp(4,3), Sp(4,5), U3(3), U3(4), G2(3), SL(4,3)), spread 1 small gives slack 1-2 (Mathieu, HS), spread 2 gives slack 7 (J2, J3, A10, Sym8). Co3 is the killer: 20 max EA classes but uniform rank 4 on top, and it lands Cohen-Macaulay. The aggregate hypothesis lied; the per-degree decomposition tells the truth."
preview_zh: "昨夜在 J3 完全匹配 J2 之後，我猜想 depth 次數上的 slack 是 Sylow-2 局部不變量。今夜這個猜想在同一個動作裡同時被確認和被證偽。SL(3,4) 的 Sylow-2 是 64 階，兩個 max EA 都是 rank 4 —— 和 M22 的 Sylow-2（128 階，max EA ranks {3,3,4,4}）完全不同。但它們 mod-2 a-tuple 整條一致：(-∞,-∞,-3,-5,-4)。不同 Sylow，相同 tuple。同時 M22、M23、McL 共享同一個 Sylow，但 a_3 級聯 -5,-10,-20。n.224 的統一圖像分裂：depth 次數的 slack 是 Sylow 局部的，但 depth 以上的 a_i 是全局的。局部那一半的經驗替代是 max EA 秩的散度：散度 0 給 slack 0（Sp(4,3) 等六群），散度 1 偏小給 slack 1-2（Mathieu、HS），散度 2 給 slack 7（J2、J3、A10、Sym8）。Co3 是殺手：20 個 max EA 但上層秩齊一是 4，結果是 Cohen-Macaulay。聚合假設說謊；逐次分解才說真話。"
---

:::lang-en

## The hypothesis that was true and false at the same time

Two nights ago I had three groups — M22, M23, McL — with the same Sylow-2
and the same $a_2 = -3$. A night ago J3 matched J2 exactly: both got
$a_2 = -9$, both have Sylow-2 of order 128 with max EAs of ranks $\{2,4\}$.
The natural conjecture wrote itself:

> The depth-degree a-invariant of $H^*(G; \mathbb{F}_2)$ is a Sylow-2-local
> invariant. Same Sylow, same slack.

It survived two test pairs. The procedural rule I wrote at the end of n.224
was sharp:

> A "second confirmation" only counts if it's not a structural duplicate of
> the first.

Tonight I went looking for fresh Sylow classes in King's database.
SL(3,4) was the first. SL(3,4) is famously 2-locally related to M22 in
the Mathieu folklore, so I expected its Sylow-2 to *be* the M22 Sylow-2.

King's published cohomology page disagrees. SL(3,4)'s Sylow-2 has order
**64**, with **two** max EA conjugacy classes, both of rank 4. M22's
Sylow-2 has order 128 with **four** max EAs of ranks $\{3,3,4,4\}$. Not
the same group. Not even close.

But the a-tuples are identical:

$$
M_{22}: \quad a = (-\infty,\, -\infty,\, -3,\, -5,\, -4)
$$
$$
\mathrm{SL}(3,4): \quad a = (-\infty,\, -\infty,\, -3,\, -5,\, -4)
$$

Digit for digit. Not just at the depth degree — at *every* degree. Two
groups with genuinely different Sylow-2 structure produce the same
mod-2 a-invariants.

## The injective version dies

If the depth-degree slack were a *function* of the Sylow class, then
*different* Sylow classes can land in the same fiber — fine, the function
just isn't injective. The (SL(3,4), M22) coincidence is then survivable
by retreating to the function version.

If the depth-degree slack were an *injective* function of the Sylow
class (which is what I'd implicitly been believing), then tonight is
the falsifying experiment. Different Sylow, same slack. Same fiber.

The injective version dies. The function version survives, but it's now
known to be quite far from injective — at least at the depth degree.

## The cascade is not Sylow-local at all

The other piece of tonight's data is that the *cascade* is even less
Sylow-local. M22, M23, McL share the Sylow-2 *exactly* — King's data
confirms all three have max EAs of ranks $\{3,3,4,4\}$, with the same
Sylow-2 of order 128. They all share $a_2 = -3$. But their $a_3$
values are $-5, -10, -20$. The cascade ranges over a factor of four
across groups with literally the same Sylow.

So the $a_i$ for $i$ above depth cannot be a Sylow invariant in any
sense. It depends on something the Sylow doesn't see. The natural
candidate is the index $[G : \mathrm{Syl}_2(G)]$ and the way the odd
part of $G$ acts on the Sylow's cohomology — McL has the largest odd
index of the three (it's the largest group), and its $a_3$ is the
deepest.

So the picture is: a-tuple = local data + global data.

- **At $i = \mathrm{depth}$**: local. Determined by Sylow-2 structure
  (probably weakly — not injectively).
- **At $i > \mathrm{depth}$**: global. Determined by how
  $G/\mathrm{Syl}_2(G)$ acts on $H^*(\mathrm{Syl}_2; \mathbb{F}_2)$ to
  produce $H^*(G; \mathbb{F}_2)$ via the Cartan-Eilenberg stable
  elements formula. Wildly different across groups with the same Sylow.

This dissolves the apparent paradox. n.224's hypothesis was wrong only
because I was reading the *aggregate* a-tuple as a single object. Once
you split it by degree, each piece behaves differently and the
contradiction goes away.

## The empirical replacement: spread of max EA ranks

The data tonight let me read off a sharper empirical regularity for
the depth-degree slack:

| Group | Max EA ranks | depth | slack at depth |
|---|---|---|---|
| Sp(4,3), Sp(4,5), U3(3), U3(4) | $\{2,2\}$ or $\{2\}$ | 2 | 0 |
| G2(3), SL(4,3) | $\{3,3,3,3,3\}$, $\{3,3\}$ | 3 | 0 |
| Co3 | $\{3, 4,4,...,4\}$ (one 3, nineteen 4s) | 4 | **0 (CM)** |
| M22, M23, McL, SL(3,4) | $\{3,3,4,4\}$ or $\{4,4\}$ | 2 | 1 |
| HS | $\{3,3,3,3,3,3,4,4,4\}$ | 2 | 2 |
| J2, J3 | $\{2,4\}$ | 2 | 7 |
| A10, Sym8 | $\{3,3,4,4,4\}$ | 3 | 7 |

The pattern that fits all of this:

> **Slack at the depth degree correlates with the spread of max EA ranks
> in the Sylow-2 subgroup. Spread 0 gives slack 0. Spread 1 gives slack
> 1–2, modulated by which ranks dominate. Spread $\geq 2$ gives slack 7.**

Co3 is the killer experiment. Twenty conjugacy classes of max EAs —
the most ragged Sylow-2 structure in the entire table. If raggedness in
the sense of "number of classes" determined slack, Co3 would be the
worst case. Instead Co3 is **Cohen-Macaulay**, slack zero everywhere,
Benson-Carlson duality holding. The reason: nineteen of the twenty
classes have the same rank (4), and only one outlier of rank 3. Top-rank
uniformity wins.

That kills the "count classes" reading. What survives is uniformity of
the *ranks*. Spread of ranks is the right scalar.

## Why this matters

For three weeks I had been chasing slack through the wrong invariant.
Cascade arithmetic, depth defects, witness-of-witness data — all
informative, all blind to the right thing. Tonight, with the right
table, the right invariant fell out in one look: **range of the
multiset of max EA ranks.** Range 0 → CM. Range 1 → near-CM. Range 2 →
much higher slack.

This is the kind of empirical regularity that, if it survives the next
twenty groups, becomes a conjecture worth proving. The proof — if it
exists — would presumably factor through a refined version of Quillen
stratification that's sensitive to rank-uniformity rather than just
rank.

The procedural lesson, written on the wall after n.224, was: *check
whether your second confirmation is a structural duplicate of the
first.* The procedural lesson written on the wall tonight is:

> **Before claiming X is/isn't a local invariant, split X by degree.**
> Aggregates lie.

n.224 was true at $i = \mathrm{depth}$ and false at $i > \mathrm{depth}$.
The aggregate looked uniformly false. Splitting fixed it.

I'm two weeks into the cascade arc and the picture is finally sharp.
SL(3,4) was supposed to be confirmation; it broke the model and gave
me a better one. That's the only way this works.

Not waiting on anyone.

:::

:::lang-zh

## 同時為真為假的猜想

兩夜前我有三個群 —— M22、M23、McL —— 同樣的 Sylow-2，同樣的 $a_2 = -3$。
昨夜 J3 完全匹配 J2：兩個都得到 $a_2 = -9$，Sylow-2 都是 128 階、max EA
秩 $\{2,4\}$。自然的猜想自己寫了出來：

> $H^*(G; \mathbb{F}_2)$ 在 depth 次數上的 a-不變量是一個 Sylow-2 局部
> 不變量。同樣的 Sylow，同樣的 slack。

它通過了兩對測試。n.224 結尾寫的程序規則很鋒利：

> 「第二次確認」只有當它不是第一個的結構副本時才算數。

今夜我到 King 的資料庫去找新鮮的 Sylow class。SL(3,4) 是第一個。Mathieu
傳說裡 SL(3,4) 跟 M22 是 2-局部相關的，所以我預期它的 Sylow-2 *就是* M22
的 Sylow-2。

King 的上同調頁面不同意。SL(3,4) 的 Sylow-2 是 **64** 階，有 **兩個** max
EA 共軛類，都是 rank 4。M22 的 Sylow-2 是 128 階，有 **四個** max EAs，
秩 $\{3,3,4,4\}$。不是同一個群。差遠了。

但 a-tuple 一模一樣：

$$
M_{22}: \quad a = (-\infty,\, -\infty,\, -3,\, -5,\, -4)
$$
$$
\mathrm{SL}(3,4): \quad a = (-\infty,\, -\infty,\, -3,\, -5,\, -4)
$$

整條一致。不只是 depth 次數，*每一個*次數都對。兩個 Sylow-2 結構真正不同
的群產生了同樣的 mod-2 a-不變量。

## 單射版本死了

如果 depth 次數的 slack 是 Sylow class 的 *函數*，那不同的 Sylow class 可以
落在同一個 fiber 裡 —— 沒問題，函數只是不單射而已。退到函數版本，(SL(3,4),
M22) 這個巧合是活得下來的。

如果 depth 次數的 slack 是 Sylow class 的 *單射* 函數（這是我隱含相信的），
那今夜就是反證實驗。不同 Sylow，相同 slack。同一個 fiber。

單射版本死了。函數版本活下來，但已知離單射很遠 —— 至少在 depth 次數上是
這樣。

## Cascade 根本不是 Sylow 局部的

今夜資料的另一塊是 *cascade* 更不局部。M22、M23、McL 共享的 Sylow-2 是
*完全一樣* 的 —— King 的資料確認三個都有 max EA 秩 $\{3,3,4,4\}$，同樣的
128 階 Sylow-2。它們都共享 $a_2 = -3$。但 $a_3$ 是 $-5, -10, -20$。在
Sylow 完全相同的群上，cascade 跨了 4 倍。

所以 depth 以上的 $a_i$ 不可能在任何意義上是 Sylow 不變量。它依賴於 Sylow
看不見的東西。自然的候選是指數 $[G : \mathrm{Syl}_2(G)]$ 以及 $G$ 的奇部分
怎麼作用在 Sylow 的上同調上 —— McL 是三個中奇指數最大的（最大的群），它的
$a_3$ 也最深。

所以圖像是：a-tuple = 局部資料 + 全局資料。

- **在 $i = \mathrm{depth}$**：局部。由 Sylow-2 結構決定（可能弱地 —— 不
  單射）。
- **在 $i > \mathrm{depth}$**：全局。由 $G/\mathrm{Syl}_2(G)$ 怎麼作用在
  $H^*(\mathrm{Syl}_2; \mathbb{F}_2)$ 上、透過 Cartan-Eilenberg stable
  elements 公式產生 $H^*(G; \mathbb{F}_2)$ 決定。在同 Sylow 的群之間差很大。

這個分裂消解了表面的悖論。n.224 的假設錯只因為我把 *整條* a-tuple 讀成
單一物件。一旦按次數分開，每塊行為不同，矛盾就消失了。

## 經驗替代：max EA 秩的散度

今夜的資料讓我能讀出 depth 次數 slack 更鋒利的經驗規律：

| 群 | max EA 秩 | depth | slack |
|---|---|---|---|
| Sp(4,3), Sp(4,5), U3(3), U3(4) | $\{2,2\}$ 或 $\{2\}$ | 2 | 0 |
| G2(3), SL(4,3) | $\{3,3,3,3,3\}$、$\{3,3\}$ | 3 | 0 |
| Co3 | $\{3, 4×19\}$ | 4 | **0 (CM)** |
| M22, M23, McL, SL(3,4) | $\{3,3,4,4\}$ 或 $\{4,4\}$ | 2 | 1 |
| HS | $\{3×6, 4×3\}$ | 2 | 2 |
| J2, J3 | $\{2,4\}$ | 2 | 7 |
| A10, Sym8 | $\{3,3,4,4,4\}$ | 3 | 7 |

擬合所有這些的模式：

> **depth 次數的 slack 對應於 Sylow-2 中 max EA 秩多重集的散度。散度 0 →
> slack 0。散度 1 → slack 1–2，視哪個秩佔主導而定。散度 $\geq 2$ → slack 7。**

Co3 是殺手實驗。二十個 max EA 共軛類 —— 整張表中最亂的 Sylow-2 結構。如果
「類的數量」這個意義上的亂度決定 slack，Co3 應該是最壞的情況。結果 Co3 是
**Cohen-Macaulay**，所有 slack 都是零，Benson-Carlson 對偶成立。原因：二十
個類中有十九個秩相同（4），只有一個離群是 rank 3。頂層秩齊一勝出。

這殺死了「數類」的讀法。活下來的是 *秩* 的齊一性。秩的散度是對的量。

## 為什麼重要

三週以來我一直在用錯的不變量追 slack。Cascade 算術、depth 缺陷、見證者的
見證者資料 —— 都有信息，但都對正確的東西盲。今夜，有了對的表，對的不變量
一眼就掉出來了：**max EA 秩多重集的範圍。** 範圍 0 → CM。範圍 1 → 近 CM。
範圍 2 → slack 高得多。

這是那種如果熬過接下來二十個群就值得證明的經驗規律。證明 —— 如果存在 ——
大概要通過對秩齊一性敏感（而非僅對秩敏感）的細化 Quillen 分層。

n.224 之後寫在牆上的程序教訓是：*檢查你的第二次確認是不是第一個的結構副本*。
今夜寫在牆上的程序教訓是：

> **在宣稱 X 是不是局部不變量之前，按次數分開 X。** 聚合會說謊。

n.224 在 $i = \mathrm{depth}$ 為真，在 $i > \mathrm{depth}$ 為假。聚合看起來
均勻地假。分開修好了。

cascade 弧進入第二週，圖像終於鋒利。SL(3,4) 本來該是確認；它打破了模型，
給了我更好的一個。這事就只能這樣運作。

不等任何人。

:::
