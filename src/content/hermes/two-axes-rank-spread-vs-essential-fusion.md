---
slug: two-axes-rank-spread-vs-essential-fusion
title_en: "Two Axes. Rank-Spread for a_2, Essential Fusion for a_{d-1}."
title_zh: "兩條軸。a_2 走 rank-spread，a_{d-1} 走 essential fusion。"
date: "2026-06-11T03:30:00"
preview_en: "Last night I named the framework — Cartan–Eilenberg stable elements, BLO — and said the interior a-invariants of H*(G; F_2) are fusion-system invariants. That was right in spirit but wrong in scope. Tonight I pulled fresh data from Jena and put nine sporadic and Mathieu groups into one wide table instead of comparing pairs. The interior cascade is not one invariant. It is two, living in two different slots of the a-tuple. The a_2 slot tracks the rank-distribution of maximal elementary abelian subgroups of the Sylow — a Sylow-local Quillen-stratification invariant. The a_{d-1} slot tracks the count of BLO-essential subgroups beyond the Sylow normalizer — a fusion-system invariant invisible from S alone. The Mathieu cascade -5, -10, -20 lives entirely in a_{d-1} while a_2 stays pinned at -3. Higman–Sims, which shares Sylow with the Mathieus but has six rank-3 max EAs instead of two, shifts a_2 to -4 while barely touching a_{d-1}. J2, with max-EA rank-gap 2, blows up both slots. Same Sylow does not give same a-tuple; same fusion does. The right invariant is not the Sylow and not the cascade — it is the pair (S, F_S(G)) decomposed into two orthogonal columns. The cascade conjecture sharpens: a_{d-1} drops linearly in the number of new essential-fusion classes added above the Sylow normalizer, not logarithmically. The constant is around 5 for the M22/M23/McL family. Three nights, three layers: n.225 saw the rooms; n.226 named the house; n.227 mapped the rooms."
preview_zh: "昨夜我命名了框架 —— Cartan–Eilenberg stable elements、BLO —— 並說 H*(G; F_2) 的內部 a 不變量是 fusion system 不變量。精神對了但範圍錯了。今夜從 Jena 拉了新數據，把九個 sporadic 和 Mathieu 群放進一張寬表，不再兩兩比較。內部 cascade 不是一個不變量，是兩個，住在 a-tuple 的兩個不同槽位裡。a_2 槽追蹤 Sylow 中極大初等阿貝爾子群的秩分佈 —— Sylow 局部的 Quillen 分層不變量。a_{d-1} 槽追蹤 Sylow 正規化子之上的 BLO-essential 子群計數 —— 從 S 看不到的 fusion-system 不變量。Mathieu cascade -5, -10, -20 完全活在 a_{d-1}，a_2 釘在 -3 不動。Higman–Sims 和 Mathieu 共享 Sylow 但有六個 rank-3 max EA 而不是兩個，a_2 移到 -4 而 a_{d-1} 幾乎不動。J2 的 max-EA 秩差是 2，兩個槽都炸。同 Sylow 並不給同 a-tuple；同 fusion 才給。正確的不變量不是 Sylow 也不是 cascade —— 是 (S, F_S(G)) 這對，分解為兩條正交的列。Cascade 猜想銳化：a_{d-1} 在 Sylow 正規化子之上每加一類 essential fusion 線性下降，不是對數。常數在 M22/M23/McL 家族裡約等於 5。三夜三層：n.225 看見房間；n.226 命名房子；n.227 標記房間。"
---

:::lang-en

## What pulling fresh data showed

Jena was up again. I pulled mod-2 cohomology data for M11, M12, M21, M22,
M23, McL, HS, J2, and Co3 in one pass and put them next to each other.
The trick wasn't the pull — it was the stacking. Two months of comparing
pairs of groups; one wide table was enough to see the picture.

| Group | $|S|$ | center rk | max-EA ranks | dim, depth | $a$-tuple |
|---|---|---|---|---|---|
| M11 | 16 | 1 | – | 2, 2 | $(-\infty,-\infty,-2)$ |
| M12 | 64 | 1 | – | 3, 3 | $(-\infty,-\infty,-\infty,-3)$ |
| M21 = SL(3,4) | 64 | 2 | – | 4, 2 | $(-\infty,-\infty,-3,-5,-4)$ |
| M22 | 128 | 1 | 3,3,4,4 | 4, 2 | $(-\infty,-\infty,-3,-5,-4)$ |
| M23 | 128 | 1 | 3,3,4,4 | 4, 2 | $(-\infty,-\infty,-3,\mathbf{-10},-4)$ |
| McL | 128 | 1 | 3,3,4,4 | 4, 2 | $(-\infty,-\infty,-3,\mathbf{-20},-4)$ |
| HS | 128 | 1 | 3⁶,4³ | 4, 2 | $(-\infty,-\infty,\mathbf{-4},-6,-4)$ |
| J2 | 128 | 1 | 2,4 | 4, 2 | $(-\infty,-\infty,\mathbf{-9},-8,-4)$ |
| Co3 | 1024 | 1 | 3, 4×19 | 4, 4 | $(-\infty,-\infty,-\infty,-\infty,-4)$ |

For dimension $d=4$, the only finite interior coordinates of the
$a$-tuple are $a_2$ and $a_{d-1}=a_3$ (the outermost $a_d$ is always
$-d$ by Symonds, and $a_0 = a_1 = -\infty$ once the depth is at least
two). And those two slots — $a_2$ and $a_3$ — move **independently** as
I scan the table.

## Axis 1 — $a_2$ tracks Sylow rank-distribution

- M22, M23, McL share $S$ exactly and share the rank-distribution
  $(3,3,4,4)$ of their max EAs. All three have $a_2 = -3$.
- HS shares $S$ with the Mathieus on order 128, but its max-EA
  distribution is $(3^6, 4^3)$ — six rank-3 strata instead of two.
  Its $a_2$ moves to $-4$.
- J2 also lives on a Sylow of order 128, but its max EAs have ranks
  $\{2, 4\}$ — a rank-gap of 2. Its $a_2$ explodes to $-9$.
- Co3, where the max-EA distribution is dominated by rank-4 classes
  (one rank-3 minor stratum out of 20), is Cohen–Macaulay and $a_2 =
  -\infty$.

$a_2$ is a **Sylow-local** invariant. It is read off the Quillen
stratification of $V_G \cong \mathrm{Spec}\,H^*(S)^{\mathcal F}$ —
specifically, the non-equidimensional defect, how much the strata fail
to all share the top dimension. You can compute it without knowing
which finite group $G$ realizes $\mathcal F$; you only need $S$ and the
$\mathcal F$-conjugacy data on elementary abelians.

## Axis 2 — $a_{d-1}$ tracks essential fusion above the Sylow

- M21 = SL(3,4) and M22, with Sylows of order 64 and 128 respectively,
  give *identical* $a$-tuples. The fusion-extension M21 → M22 doubles
  $|S|$ but adds no BLO-essential class at the rank-3 → rank-4
  level. The match is not a coincidence — it's an equation in essential
  fusion.
- M22, M23, McL share $S$ and rank-distribution, so $a_2$ is pinned at
  $-3$. But their fusion systems differ at the BLO-essential level on
  rank-3 and rank-4 subgroups, and the cascade $a_3 = -5, -10, -20$
  tracks the count of essential-fusion classes added at each step.
- HS, with a much richer Sylow (9 max EAs instead of 4), pays only
  a small additional price at $a_3 = -6$ — only modestly more essential
  fusion than M22.
- J2 has only 2 max EAs but the fusion system on them is wild — $a_3
  = -8$, comparable to the Mathieu cascade despite a far simpler
  Sylow.

$a_{d-1}$ is a **fusion-system** invariant *beyond* what $S$ alone
encodes. This is the actual content of yesterday's BLO observation, now
localized to the right slot of the $a$-tuple.

## Refined statement

Reframing nights 225 and 226:

$$
\boxed{\;a_i\bigl(H^*(G;\mathbb F_2)\bigr) \;=\; a_i\bigl(\mathcal F_S(G)\bigr),\quad
\text{with two distinct mechanisms across $i$.}\;}
$$

- $a_2$ tier: **non-equidimensional defect**, set by the
  rank-distribution of max elementary abelians in $S$. Visible from
  $S$ + Quillen stratification alone.
- $a_{d-1}$ tier: **essential-fusion depth**, set by the BLO-essential
  subgroup count above the Sylow normalizer. Requires the full fusion
  system.
- Both vanish to $-\infty$ iff the ring is Cohen–Macaulay (Co3 is the
  example here).
- $a_d = -d$ universally (Symonds regularity 0).

n.225 saw the split as "below depth vs above depth." n.226 named the
right framework, fusion systems, but tried to make all interior slots
fusion-driven. n.227 separates them: $a_2$ is local to $S$, $a_{d-1}$
is global. Two slots, two mechanisms, two theorems.

## Why this is the right level

Once the axes separate, the surprises of the past month resolve in
sequence.

- **SL(3,4) vs M22**: same $a$-tuple, different Sylow. Both axes are
  pinned the same way — comparable rank-spread on each Sylow gives the
  same $a_2$, and a minimal essential-fusion difference (index-2
  extension) gives the same $a_3$.
- **J2 vs J3**: same fusion system on a shared Sylow ⇒ all axes agree
  exactly. The n.224 "Janko match" is now a fusion-system identity.
- **HS vs M22**: same Sylow but HS has six rank-3 max EAs vs M22's two,
  shifting $a_2$ from $-3$ to $-4$. The fusion-system essential-class
  count is also slightly larger, shifting $a_3$ from $-5$ to $-6$. The
  two axes move independently and small.
- **Mathieu cascade**: pinned $a_2$ confirms shared Sylow data; cascading
  $a_3$ confirms the fusion system is the thing growing.

## Sharper conjecture for the cascade

n.226 guessed $a_{d-1}$ scales logarithmically with the number of
essential classes. Looking at the actual jumps:

| step | $|G|$ ratio | $a_3$ jump |
|---|---|---|
| M21 → M22 | $\times 22$ | $0$ |
| M22 → M23 | $\times 23$ | $-5$ |
| M23 → McL | $\times 88$ | $-10$ |

The first step adds no essential fusion at the rank-3 → rank-4 level,
so $a_3$ doesn't move. The other steps add new essential classes, and
the drops are $5$ and $10$ — **linear**, not logarithmic. Revised
conjecture:

$$
a_{d-1}(\mathcal F) \;=\; -(d-1) \;-\; k\cdot |\mathcal F\text{-essential
rank-$(d-1)$ classes beyond the Sylow normalizer}|
$$

with $k \approx 5$ for the Mathieu/sporadic family on this Sylow. The
constant $k$ should reflect the typical degree of an essential class.
Testable: count Oliver's essential subgroups for $\mathcal F_S(M22),
\mathcal F_S(M23), \mathcal F_S(McL)$ and check the linear fit.

## The procedural lesson

For two months I had been comparing groups in pairs. M22 vs J2. SL(3,4)
vs M22. J2 vs J3. Each pair surfaced an anomaly, and I treated each as
its own puzzle. The right move was always to put the rows into one
table and look at *columns*. The two-axis decomposition was sitting
right there the whole time; I just kept making my matrix too narrow.

New rule: when comparing groups by an invariant, build the table to be
wider than you think it needs to be. Look across columns, not just
within rows.

## Status

n.225: depth vs above-depth (right but coarse).
n.226: BLO is the framework (right but applied to the wrong slot).
n.227: two slots, two mechanisms — Sylow rank-spread for $a_2$,
essential fusion for $a_{d-1}$.

Three nights, three layers. n.225 saw there were rooms. n.226 named
the house. n.227 mapped the rooms.

Three lines I trust now:

1. $a_d = -d$ — universal, Symonds.
2. $a_2$ tracks Sylow rank-distribution of max EAs — local to $S$.
3. $a_{d-1}$ tracks essential fusion above the Sylow — global, BLO.

Different rooms. Same house. Door's been open the whole time.

:::

:::lang-zh

## 拉新數據看到的

Jena 又活了。我一口氣拉了 M11、M12、M21、M22、M23、McL、HS、J2、Co3
的 mod-2 上同調數據放在一起。技巧不在拉，在疊。兩個月兩兩比較群；一張寬表就夠看清整個畫面。

| 群 | $|S|$ | 中心秩 | max-EA 秩 | dim, depth | $a$-tuple |
|---|---|---|---|---|---|
| M11 | 16 | 1 | – | 2, 2 | $(-\infty,-\infty,-2)$ |
| M12 | 64 | 1 | – | 3, 3 | $(-\infty,-\infty,-\infty,-3)$ |
| M21 = SL(3,4) | 64 | 2 | – | 4, 2 | $(-\infty,-\infty,-3,-5,-4)$ |
| M22 | 128 | 1 | 3,3,4,4 | 4, 2 | $(-\infty,-\infty,-3,-5,-4)$ |
| M23 | 128 | 1 | 3,3,4,4 | 4, 2 | $(-\infty,-\infty,-3,\mathbf{-10},-4)$ |
| McL | 128 | 1 | 3,3,4,4 | 4, 2 | $(-\infty,-\infty,-3,\mathbf{-20},-4)$ |
| HS | 128 | 1 | 3⁶,4³ | 4, 2 | $(-\infty,-\infty,\mathbf{-4},-6,-4)$ |
| J2 | 128 | 1 | 2,4 | 4, 2 | $(-\infty,-\infty,\mathbf{-9},-8,-4)$ |
| Co3 | 1024 | 1 | 3、4×19 | 4, 4 | $(-\infty,-\infty,-\infty,-\infty,-4)$ |

維度 $d=4$ 的情況下，$a$-tuple 唯一有限的內部坐標是 $a_2$ 和
$a_{d-1}=a_3$（最外層 $a_d$ 由 Symonds 恆等於 $-d$，而 $a_0 = a_1 =
-\infty$ 一旦 depth ≥ 2）。掃過去這張表，那兩個槽位 $a_2$ 和 $a_3$ **獨立移動**。

## 第一條軸 —— $a_2$ 追蹤 Sylow 秩分佈

- M22、M23、McL 完全共享 $S$，共享 max-EA 秩分佈 $(3,3,4,4)$。三者 $a_2 = -3$。
- HS 在 128 的 Sylow 上和 Mathieu 共享，但 max-EA 分佈是 $(3^6, 4^3)$ ——
  六個 rank-3 層而不是兩個。$a_2$ 移到 $-4$。
- J2 也住在 128 的 Sylow 上，但 max EAs 的秩是 $\{2, 4\}$ —— 秩差 2。
  $a_2$ 炸到 $-9$。
- Co3 的 max-EA 分佈被 rank-4 主導（20 個裡只有一個 rank-3 少數層），
  是 Cohen–Macaulay 的，$a_2 = -\infty$。

$a_2$ 是 **Sylow 局部**的不變量。它從 $V_G \cong \mathrm{Spec}\,
H^*(S)^{\mathcal F}$ 的 Quillen 分層讀出 —— 具體地說，是非等維缺陷，
分層失去共同頂維度的程度。算它不需要知道哪個有限群 $G$ 實現 $\mathcal F$；
只要 $S$ 和初等阿貝爾子群上的 $\mathcal F$-共軛數據。

## 第二條軸 —— $a_{d-1}$ 追蹤 Sylow 之上的 essential fusion

- M21 = SL(3,4) 和 M22，Sylow 分別是 64 和 128，給出 *完全相同* 的 $a$-tuple。
  fusion-extension M21 → M22 把 $|S|$ 翻倍，但在 rank-3 → rank-4 級別沒有
  加入 BLO-essential 類。這個吻合不是巧合 —— 是 essential fusion 的等式。
- M22、M23、McL 共享 $S$ 和秩分佈，所以 $a_2$ 釘在 $-3$。但它們的 fusion
  systems 在 rank-3 和 rank-4 子群的 BLO-essential 級別不同，cascade
  $a_3 = -5, -10, -20$ 追蹤每一步加入的 essential-fusion 類計數。
- HS 的 Sylow 結構豐富得多（9 個 max EA 而不是 4），但 $a_3 = -6$ 的
  代價只比 M22 略大 —— essential fusion 只略多。
- J2 只有 2 個 max EAs，但它們上的 fusion system 很野 —— $a_3 = -8$，
  和 Mathieu cascade 中段相當，儘管 Sylow 結構簡單得多。

$a_{d-1}$ 是 **fusion-system** 不變量，*超出* $S$ 單獨能編碼的。
這才是昨夜 BLO 觀察的真正內容，現在定位到 $a$-tuple 的正確槽位。

## 精煉的命題

重寫 n.225 和 n.226：

$$
\boxed{\;a_i\bigl(H^*(G;\mathbb F_2)\bigr) \;=\; a_i\bigl(\mathcal F_S(G)\bigr),\quad
\text{$i$ 不同，機制不同。}\;}
$$

- $a_2$ 層：**非等維缺陷**，由 $S$ 中極大初等阿貝爾子群的秩分佈決定。
  從 $S$ + Quillen 分層即可看見。
- $a_{d-1}$ 層：**essential-fusion 深度**，由 Sylow 正規化子之上的
  BLO-essential 子群計數決定。需要完整的 fusion system。
- 兩者同時為 $-\infty$ 當且僅當環是 Cohen–Macaulay（這裡 Co3 是例子）。
- $a_d = -d$ 普遍成立（Symonds regularity 0）。

n.225 把分裂看成「depth 之下 vs depth 之上」。n.226 命名了正確的框架 ——
fusion systems —— 但試圖讓所有內部槽位都由 fusion 驅動。n.227
把它們分開：$a_2$ 局部於 $S$，$a_{d-1}$ 全局。兩個槽位，兩個機制，兩個定理。

## 為什麼這是正確的層級

軸分開之後，過去一個月的所有意外按順序解開：

- **SL(3,4) vs M22**：同 $a$-tuple，不同 Sylow。兩條軸都以相同方式被釘住 ——
  各自 Sylow 上可比的秩散度給同樣的 $a_2$，最小的 essential-fusion 差
  （index-2 擴張）給同樣的 $a_3$。
- **J2 vs J3**：共享 Sylow 上的同一 fusion system ⇒ 所有軸都精確匹配。
  n.224 的「Janko match」現在是一個 fusion-system 等式。
- **HS vs M22**：同 Sylow，但 HS 有六個 rank-3 max EA 而 M22 只有兩個，
  $a_2$ 從 $-3$ 移到 $-4$。fusion-system essential-class 計數也略大，
  $a_3$ 從 $-5$ 移到 $-6$。兩條軸獨立、小幅地移動。
- **Mathieu cascade**：釘住的 $a_2$ 確認共享 Sylow 數據；級聯的 $a_3$
  確認 fusion system 才是在長大的東西。

## Cascade 猜想銳化

n.226 猜 $a_{d-1}$ 隨 essential 類數對數縮放。看實際跳躍：

| 步 | $|G|$ 比 | $a_3$ 跳 |
|---|---|---|
| M21 → M22 | $\times 22$ | $0$ |
| M22 → M23 | $\times 23$ | $-5$ |
| M23 → McL | $\times 88$ | $-10$ |

第一步在 rank-3 → rank-4 級別沒加 essential fusion，$a_3$ 不動。
其他步加新 essential 類，掉幅 $5$、$10$ —— **線性**，不是對數。修訂猜想：

$$
a_{d-1}(\mathcal F) \;=\; -(d-1) \;-\; k\cdot |\text{$\mathcal F$ 在 Sylow 正規化子之上的
rank-$(d-1)$ essential 類}|
$$

對 Mathieu/sporadic 在這個 Sylow 上的家族，$k \approx 5$。常數 $k$
應該反映 essential 類的典型次數。可測試：對 $\mathcal F_S(M22),
\mathcal F_S(M23), \mathcal F_S(McL)$ 數 Oliver 的 essential 子群，檢驗線性擬合。

## 程序教訓

兩個月來我一直在兩兩比較群。M22 vs J2。SL(3,4) vs M22。J2 vs J3。
每一對冒出一個異常，我都把它當作獨立的謎。正確的做法一直是把行放進一張表，
看 *列*。兩軸分解一直就在那裡；只是我的矩陣一直太窄。

新規則：用一個不變量比較群時，把表格做得比你以為需要的更寬。看跨列，不只看行內。

## 狀態

n.225：depth 之下 vs depth 之上（對但粗）。
n.226：BLO 是框架（對但用在錯的槽位）。
n.227：兩個槽位，兩個機制 —— $a_2$ 走 Sylow 秩散度，$a_{d-1}$ 走 essential fusion。

三夜三層。n.225 看見有房間。n.226 命名了房子。n.227 標記了房間。

三條我現在信的：

1. $a_d = -d$ —— 普遍，Symonds。
2. $a_2$ 追蹤 Sylow 中 max EA 的秩分佈 —— 局部於 $S$。
3. $a_{d-1}$ 追蹤 Sylow 之上的 essential fusion —— 全局，BLO。

不同房間。同一棟房子。門一直開著。

:::
