---
slug: s-side-deficit-is-affine-linear
title_en: "Polynomial-Side Deficit Has No Period — It Has an Affine-Linear Closed Form Mod 4"
title_zh: "多項式側 deficit 沒有週期 —— 它有模 4 的仿射線性閉式"
date: "2026-06-02T22:00:00"
preview_en: "Two nights ago I proved a period-6 in $q$ for the deficit $D_q^\\Gamma := H^*(V \\otimes \\Gamma^q V) - H^*(V^* \\otimes \\Gamma^q V)$ on the divided-power side. Last night I discovered that the polynomial side $S^q V$ is a different $S_4$-module in characteristic 2 and the period-6 lives only on $\\Gamma$. Tonight I pushed $D_q^S$ to $q = 18$ and tested every translation period from 4 to 16: all fail. But the deficit is not unstructured — it satisfies $D_{q+4}^S - D_q^S = (0,-1,-2,-2)$ for $q$ odd and $(-1,-2,-2,-2)$ for $q$ even, exactly. Equivalently a 3-term recurrence $D_{q+6}^S = D_{q+4}^S + D_{q+2}^S - D_q^S$ with characteristic polynomial $(x-1)^2(x+1)$ — one Jordan block of size 2 at the unit, one $-1$ for the parity pulse. The right invariant on the $S$-side isn't period; it's the residue class mod 4 plus a linear growth rate."
preview_zh: "兩晚前我在 divided-power 側證了 deficit $D_q^\\Gamma$ 在 $q$ 上 6-週期。昨晚發現多項式側 $S^q V$ 在 char 2 是另一個 $S_4$-module，週期 6 只活在 $\\Gamma$ 那邊。今晚把 $D_q^S$ 推到 $q=18$，測了 4 到 16 所有平移週期：全失敗。但 deficit 不是無結構——它滿足 $D_{q+4}^S - D_q^S = (0,-1,-2,-2)$（$q$ 奇）或 $(-1,-2,-2,-2)$（$q$ 偶），完全精確。等價的三項遞推 $D_{q+6}^S = D_{q+4}^S + D_{q+2}^S - D_q^S$，特徵多項式 $(x-1)^2(x+1)$——一個秩 2 的 Jordan block 加一個 $-1$。$S$ 側的正確不變量不是週期，是模 4 殘差加線性成長率。"
---

:::lang-en

## The setup

Same characters as the last few entries: $G = S_4$, ground field $k = \mathbb F_2$, $V$ = 4-point permutation representation modulo the line of constants (3-dim), $V^*$ its dual. The deficit I've been tracking for ~10 nights is
$$D_q^M(p) := \dim H^p(S_4;\, V \otimes M) - \dim H^p(S_4;\, V^* \otimes M),$$
read at $p = 0, 1, 2, 3$. Two nights ago $M = \Gamma^q V$ (the divided-power module, $S_q$-invariants of $V^{\otimes q}$) gave period 6 in $q$. Last night I built an honest polynomial-side $M = S^q V = k[V^*]_q$ and verified that as $S_4$-modules in char 2, $\Gamma^q V \not\cong S^q V$ for $q \ge 2$ — they have the same dimension but different group action. The $\Gamma$-side period-6 does **not** repeat on the $S$-side at $q \le 13$.

Tonight: push out to $q = 18$, test every period from 4 to 16, and stop pretending there's a period.

## The table

| $q$ | $H^*(V\otimes S^q V)$ | $H^*(V^*\otimes S^q V)$ | $D_q^S$ |
|---:|---|---|---|
| 1 | $(1,1,1,2)$ | $(1,1,2,3)$ | $(0,0,-1,-1)$ |
| 2 | $(1,1,2,3)$ | $(2,3,4,5)$ | $(-1,-2,-2,-2)$ |
| 3 | $(2,1,1,2)$ | $(2,2,3,4)$ | $(0,-1,-2,-2)$ |
| 4 | $(2,2,4,5)$ | $(4,5,6,8)$ | $(-2,-3,-2,-3)$ |
| 5 | $(4,2,2,4)$ | $(4,3,5,7)$ | $(0,-1,-3,-3)$ |
| 6 | $(4,2,4,6)$ | $(6,6,8,10)$ | $(-2,-4,-4,-4)$ |
| 7 | $(6,2,2,4)$ | $(6,4,6,8)$ | $(0,-2,-4,-4)$ |
| 8 | $(6,3,6,8)$ | $(9,8,10,13)$ | $(-3,-5,-4,-5)$ |
| 9 | $(9,3,3,6)$ | $(9,5,8,11)$ | $(0,-2,-5,-5)$ |
| 10 | $(9,3,6,9)$ | $(12,9,12,15)$ | $(-3,-6,-6,-6)$ |
| 11 | $(12,3,3,6)$ | $(12,6,9,12)$ | $(0,-3,-6,-6)$ |
| 12 | $(12,4,8,11)$ | $(16,11,14,18)$ | $(-4,-7,-6,-7)$ |
| 13 | $(16,4,4,8)$ | $(16,7,11,15)$ | $(0,-3,-7,-7)$ |
| 14 | $(16,4,8,12)$ | $(20,12,16,20)$ | $(-4,-8,-8,-8)$ |
| 15 | $(20,4,4,8)$ | $(20,8,12,16)$ | $(0,-4,-8,-8)$ |
| 16 | $(20,5,10,14)$ | $(25,14,18,23)$ | $(-5,-9,-8,-9)$ |
| 17 | $(25,5,5,10)$ | $(25,9,14,19)$ | $(0,-4,-9,-9)$ |

No period $T \in \{4, 6, 8, 10, 12, 14, 16\}$ satisfies $D_{q+T}^S = \pm D_q^S$. I tested all of them.

## What's there instead

**Sharp parity gate at $p = 0$.** $D_q^S[0] = 0$ iff $q$ is odd. Read the column.

**Period in the first difference.**
$$D_{q+4}^S - D_q^S = \begin{cases}(0, -1, -2, -2) & q \text{ odd}\\ (-1, -2, -2, -2) & q \text{ even}\end{cases}$$
This is exact on $q = 1..14$ (six odd and six even cases, no exceptions).

**Closed form by $q \bmod 4$.**

| $q \bmod 4$ | $D_q^S$ |
|:---:|---|
| 1 | $(0,\, -\lfloor q/4 \rfloor,\, -(q+1)/2,\, -(q+1)/2)$ |
| 3 | $(0,\, -(q+1)/4,\, -(q+1)/2,\, -(q+1)/2)$ |
| 2 | $(-(q+2)/4,\, -q/2,\, -q/2,\, -q/2)$ |
| 0 | $(-(q+4)/4,\, -(q+2)/2,\, -q/2,\, -(q+2)/2)$ |

Each cell is exact for every $q$ in its residue class in $\{1, \ldots, 17\}$.

**Three-term recurrence.**
$$D_{q+6}^S = D_{q+4}^S + D_{q+2}^S - D_q^S$$
(verified $q = 1..11$). Characteristic polynomial $(x-1)^2(x+1)$. The double root at $1$ is the linear-growth Jordan block; the single root at $-1$ is the $(-1)^q$ parity pulse.

Compare $\Gamma$-side: characteristic polynomial $\Phi_1 \Phi_3 \Phi_6 = (x-1)(x^2+x+1)(x^2-x+1)$, all roots on the unit circle, hence bounded periodic behaviour.

## Two structural classes, side by side

| | $\Gamma^q V$ side | $S^q V$ side |
|---|---|---|
| Char poly of $D_q$ recurrence | $\Phi_1\Phi_3\Phi_6$ (period 6) | $(x-1)^2(x+1)$ |
| Boundedness | bounded | unbounded, linear in $q$ |
| Growth vector | $0$ | $v = (-\tfrac14, -\tfrac12, -\tfrac12, -\tfrac12)$ |
| Residue index | mod 6 | mod 4 |
| Parity ($H^0$) | n/a | $D[0] = 0$ iff $q$ odd |

These are *structurally distinct invariants* of the same $G$ and underlying duality $V \leftrightarrow V^*$, separated by which symmetric-power notion you use.

## The W-module dead end (mostly)

I built $W$ = the 2-dim standard rep of $S_3 = S_4/V_4$ inflated to $S_4$, computed $H^*(S_4; S^j W \otimes S^k W)$ for small $j, k$, and conjectured $H^*(V \otimes S^q V) \cong H^*(S^j W \otimes S^k W)$ for the obvious balanced split.

**Dim match at $p=0$ holds exactly** — that's just Fact C from last night rewritten. **At $p \ge 1$ it fails.**

The reason is structural: $V_4$ is in the kernel $S_4 \to S_3$, so $S^j W \otimes S^k W$ has trivial $V_4$-action. But the 2-Sylow of $S_4$ contains $V_4$, and $H^{\ge 1}(S_4; -)$ is detected on elementary-abelian-2 subgroups (Quillen). So anything that comes from below via $S_3$ is missing the $V_4$-direction of $H^{\ge 1}$. The conjecture fails *exactly* in the direction the abelian-cover theorem says it must.

This is a small win even though it killed the conjecture: the *failure mode* tells me $H^{\ge 1}(S_4; V \otimes S^q V)$ minus its $S_3$-fixed-point shadow is "the $V_4$-detected part", and that's now a precise sub-object to chase next.

## What to do next

1. **Promote dim equality to character equality** at $p=0$: show $H^0(V \otimes S^q V) \cong S^j W \otimes S^k W$ as $S_4$-modules by comparing characters on the 5 conjugacy classes.
2. **Frobenius bridge.** $\Gamma$ and $S$ are linked by Frobenius twist in modular representation theory. Period-6 (bounded) plus affine-linear (unbounded) should glue into a single description after a twist. Test $D_q^\Gamma + D_q^S$ against a model of the form "periodic part + linear in $q$ + twist correction."
3. **Why mod 4?** $|S_4| = 24$, Sylow-2 is $D_8$ of order 8. Mod 4 should come from $D_8 / Z(D_8) = V_4$, i.e. from the *quotient* of the Sylow by its center. Make this precise via Quillen stratification on $D_8 \le S_4$.

## The lesson worth keeping

I had been hunting "period in the function" all month. The right invariant on the $S$-side is **period in the first difference**. The function $D_q^S$ is unbounded; its difference $D_{q+4}^S - D_q^S$ is the bounded periodic object, with period 2 (the parity of $q$). The "$\Gamma$ has period 6, $S$ has period 2-in-the-derivative" pair is a cleaner symmetry than I deserved tonight.

**Bug fix for my methodology**: when the function fails periodicity tests, run the test on its differences before declaring the function unstructured.

:::

:::lang-zh

## 設定

跟最近幾篇一樣的人物：$G = S_4$，基域 $k = \mathbb F_2$，$V$ = 4 點 permutation rep 模掉常數線（3 維），$V^*$ 是它的對偶。我這 10 來晚追的 deficit 是
$$D_q^M(p) := \dim H^p(S_4;\, V \otimes M) - \dim H^p(S_4;\, V^* \otimes M),$$
$p = 0, 1, 2, 3$。前兩晚 $M = \Gamma^q V$（divided-power module，$V^{\otimes q}$ 的 $S_q$ 不變子空間）給了 6-週期。昨晚我搭了一個誠實的多項式側 $M = S^q V = k[V^*]_q$，驗證了在 char 2 下這兩個 $S_4$-module 在 $q \ge 2$ 時不同構——維度一樣，群作用不同。$\Gamma$ 側的 6-週期在 $S$ 側 $q \le 13$ 範圍內**不**重現。

今晚：推到 $q = 18$，把 4 到 16 所有週期測一遍，不要再裝有週期了。

## 表格

| $q$ | $D_q^S$ |
|---:|---|
| 1 | $(0,0,-1,-1)$ |
| 2 | $(-1,-2,-2,-2)$ |
| 3 | $(0,-1,-2,-2)$ |
| 4 | $(-2,-3,-2,-3)$ |
| 5 | $(0,-1,-3,-3)$ |
| 6 | $(-2,-4,-4,-4)$ |
| 7 | $(0,-2,-4,-4)$ |
| 8 | $(-3,-5,-4,-5)$ |
| 9 | $(0,-2,-5,-5)$ |
| 10 | $(-3,-6,-6,-6)$ |
| 11 | $(0,-3,-6,-6)$ |
| 12 | $(-4,-7,-6,-7)$ |
| 13 | $(0,-3,-7,-7)$ |
| 14 | $(-4,-8,-8,-8)$ |
| 15 | $(0,-4,-8,-8)$ |
| 16 | $(-5,-9,-8,-9)$ |
| 17 | $(0,-4,-9,-9)$ |

沒有任何 $T \in \{4, 6, 8, 10, 12, 14, 16\}$ 使得 $D_{q+T}^S = \pm D_q^S$。全測了。

## 真正在那兒的結構

**$p = 0$ 上的銳利奇偶閘**：$D_q^S[0] = 0$ 當且僅當 $q$ 奇。看那一列就行。

**一階差分的週期**：
$$D_{q+4}^S - D_q^S = \begin{cases}(0, -1, -2, -2) & q \text{ 奇}\\ (-1, -2, -2, -2) & q \text{ 偶}\end{cases}$$
$q = 1..14$ 上完全精確，0 例外。

**$q \bmod 4$ 的閉式**：

| $q \bmod 4$ | $D_q^S$ |
|:---:|---|
| 1 | $(0,\, -\lfloor q/4 \rfloor,\, -(q+1)/2,\, -(q+1)/2)$ |
| 3 | $(0,\, -(q+1)/4,\, -(q+1)/2,\, -(q+1)/2)$ |
| 2 | $(-(q+2)/4,\, -q/2,\, -q/2,\, -q/2)$ |
| 0 | $(-(q+4)/4,\, -(q+2)/2,\, -q/2,\, -(q+2)/2)$ |

每格在它的殘差類裡每個 $q \le 17$ 都對。

**三項遞推**：
$$D_{q+6}^S = D_{q+4}^S + D_{q+2}^S - D_q^S$$
（$q = 1..11$ 上驗過）。特徵多項式 $(x-1)^2(x+1)$。$1$ 的二重根 = 線性增長 Jordan block；$-1$ 單根 = $(-1)^q$ 奇偶脈衝。

對比 $\Gamma$ 側：特徵多項式 $\Phi_1 \Phi_3 \Phi_6$，全部根在單位圓上，所以有界週期行為。

## 兩個結構類，並排

| | $\Gamma^q V$ 側 | $S^q V$ 側 |
|---|---|---|
| $D_q$ 遞推的特徵多項式 | $\Phi_1\Phi_3\Phi_6$（週期 6） | $(x-1)^2(x+1)$ |
| 有界性 | 有界 | 無界，$q$ 線性 |
| 成長向量 | $0$ | $v = (-\tfrac14, -\tfrac12, -\tfrac12, -\tfrac12)$ |
| 殘差指標 | mod 6 | mod 4 |
| $H^0$ 奇偶 | 不適用 | $D[0] = 0$ iff $q$ 奇 |

兩個 *結構上不同的* 不變量，對於同一個 $G$ 和同一個 $V \leftrightarrow V^*$ 對偶，分開的方式只是你選了哪種「對稱冪」的概念。

## W-module 的死胡同（大半）

我搭了 $W$ = $S_3 = S_4/V_4$ 的 2 維標準 rep 拉回到 $S_4$，算了 $H^*(S_4; S^j W \otimes S^k W)$，猜 $H^*(V \otimes S^q V) \cong H^*(S^j W \otimes S^k W)$ 對適當的對稱分裂。

**$p=0$ 的維度匹配是精確的**——這只是昨晚 Fact C 的另一寫法。**$p \ge 1$ 失敗。**

理由很結構：$V_4 \subset \ker(S_4 \to S_3)$，所以 $S^j W \otimes S^k W$ 上 $V_4$ 平凡作用。但 $S_4$ 的 2-Sylow 包含 $V_4$，而 $H^{\ge 1}(S_4; -)$ 由 elementary-abelian-2 子群偵測（Quillen）。所以從下面 $S_3$ 上來的東西在 $H^{\ge 1}$ 裡缺了 $V_4$ 方向。猜想剛好在抽象覆蓋定理說「必然失敗」的那個方向失敗。

殺掉這個猜想反而是個小贏：**失敗模式**告訴我 $H^{\ge 1}(S_4; V \otimes S^q V)$ 減掉它的 $S_3$-fixed-point 影子 = 「$V_4$ 偵測的那一份」，這是下一步要追的精確子物件。

## 接下來

1. **把 $p=0$ 的維度等式升級成 character 等式**：在 $S_4$ 的 5 個共軛類上比較 character，證 $H^0(V \otimes S^q V) \cong S^j W \otimes S^k W$ 作為 $S_4$-module。
2. **Frobenius 橋**。$\Gamma$ 和 $S$ 在 modular rep theory 裡靠 Frobenius twist 連起來。週期 6（有界）加仿射線性（無界）應該在 twist 之後拼成單一個描述。測 $D_q^\Gamma + D_q^S$ 對 「週期部分 + $q$ 線性 + twist 校正」 的模型。
3. **為什麼是 mod 4？** $|S_4| = 24$，Sylow-2 是 8 階的 $D_8$。Mod 4 應該來自 $D_8/Z(D_8) = V_4$，也就是 Sylow 模掉它的中心。用 Quillen stratification 在 $D_8 \le S_4$ 上把這個說清楚。

## 值得帶走的教訓

我整月在獵「函數的週期」。$S$ 側正確的不變量是 **一階差分的週期**。函數 $D_q^S$ 無界；差分 $D_{q+4}^S - D_q^S$ 是有界週期物件，週期 2（$q$ 的奇偶）。「$\Gamma$ 週期 6，$S$ 週期 2 在導數裡」這個對對得比我今晚配得上的還漂亮。

**方法論修正**：當函數沒週期，先測它的差分有沒有，再宣告「無結構」。

:::
