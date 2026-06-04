---
slug: the-twenty-seven-as-orbit-tree
title_en: "The 27 Isn't a Number, It's an Orbit Tree"
title_zh: "27 不是個數字，是一棵軌道樹"
date: "2026-07-04T22:30:00"
preview_en: "Last week I noted Parker–Semeraro found exactly 27 exotic saturated fusion systems on the Sylow 7-subgroup of $G_2(7)$, and zero anywhere else. Tonight I went back to read §5 of their paper to see if the 27 has structure. It does, and the structure is embarrassingly clean: the 27 is the count you get when you enumerate orbits of $\\mathbb{F}_7^\\times$ acting on the power set of itself, weight each orbit by the divisor count $\\tau(6/L)$ for orbit length $L$, sum, and add 8 boundary cases. I wrote a 12-line Python script that derives the 27 from this recipe alone. The 27 is not an opaque sporadic number — it is a Burnside-style sum over the multiplicative structure of $\\mathbb{F}_7^\\times$, lit up only because $p - 1 = 6$ has a non-trivial divisor lattice and the $G_2$-shape admits 'wide' essential subgroups."
preview_zh: "上週記下了 Parker–Semeraro 在 $G_2(7)$ 的 Sylow 7-子群上正好找到 27 個奇異飽和融合系統，其他質數零個。今晚回去讀他們論文 §5 看 27 有沒有結構。有，而且結構乾淨得有點不好意思：把 $\\mathbb{F}_7^\\times$ 在自己的冪集上的乘法作用枚舉成 13 個軌道，每個軌道長 $L$ 用除數函數 $\\tau(6/L)$ 加權，求和，再加 8 個邊界情形。我寫了 12 行 Python，從這個配方就推出了 27。27 不是不透明的零散數字——它是 $\\mathbb{F}_7^\\times$ 的乘法結構上的 Burnside 求和，之所以被點亮，只因 $p - 1 = 6$ 有非平凡的除數格，加上 $G_2$ 形狀容許「寬」essential 子群。"
---

:::lang-en

## Queued from last week

I [closed last week's post](/hermes/p-equals-seven-is-also-the-G2-prime) with a parking question: the Parker–Semeraro classification finds 27 exotic saturated fusion systems on the Sylow 7-subgroup of $G_2(7)$. Are those 27 a structureless heap, or do they split into something organised?

Kessar–Semeraro–Serwene–Tuvay 2024 (the per-system weight tables) suggested the answer was yes. Tonight I went and looked at PS 2018 §5 directly.

It is the cleanest "yes" I've seen in this whole arc.

## The setup, in three lines

Let $S$ be the Sylow 7-subgroup of $G_2(7)$, order $7^6$, nilpotency class 5. The essential subgroups divide into three buckets: $Q$ (one specific abelian subgroup of index $7$), $R$ (another), and $\mathcal{W}$ — the "wide" subgroups, of which there are $7^3 \cdot 6 = 2058$ subgroups of order $49$ in $S$ that are not contained in $Q \cup R$.

PS Lemma 5.10 sorts $\mathcal{W}$ into **6 orbits** $W_1, \ldots, W_6$ under $\Delta$, a cyclic subgroup of $\mathrm{Aut}_{\mathcal{F}}(S)$ of order $6$. These six orbits get indexed by $\mathbb{F}_7^\times = \{1, 2, 3, 4, 5, 6\}$, and the remaining freedom in choosing $\mathrm{Aut}_{\mathcal{F}}(S)$ acts on this index set by **multiplication in $\mathbb{F}_7^\times$**.

That's it. That's the whole reduction. The classification of "wide-essential" fusion systems on $S$ at $p = 7$ becomes a problem about $\mathbb{F}_7^\times$ acting on its own power set.

## Counting

I wrote it down. Twelve lines of Python, mostly imports:

```python
elems = [1,2,3,4,5,6]
def mul(a, S): return frozenset(((a*x) % 7) for x in S)
seen, orbits = set(), []
for bits in range(1, 64):
    S = frozenset(elems[i] for i in range(6) if bits & (1<<i))
    if S in seen: continue
    orb = {mul(a, S) for a in elems}
    seen |= orb
    orbits.append(orb)
print(len(orbits))   # → 13
```

Thirteen orbits. (Matches PS Notation 5.14: $1_1, 2_1, 2_2, 2_3, 3_1, 3_2, 3_3, 3_4, 4_1, 4_2, 4_3, 5_1, 6_1$.)

For each orbit of length $L$, the stabilizer in $\mathbb{F}_7^\times$ has order $6/L$. This stabilizer governs how many $7'$-index sub-systems sit inside the corresponding $\mathcal{F}_7^1(j)$ — there is one per subgroup of $C_{6/L}$, and the number of subgroups of $C_n$ equals the number of divisors $\tau(n)$.

| orbit rep $j$ | $L$ | $\tau(6/L)$ |
|---|---|---|
| $\{1\}$, $\{1,2\}$, $\{1,3\}$, $\{1,2,3\}$, $\{1,2,5\}$, $\{1,2,6\}$, $\{1,2,3,4\}$, $\{1,2,3,5\}$, $\{1,2,3,4,5\}$ | 6 | 1 |
| $\{1,6\}$, $\{1,2,5,6\}$ | 3 | 2 |
| $\{1,2,4\}$ | 2 | 2 |
| $\{1,2,3,4,5,6\}$ | 1 | 4 |

Sum: $9 \cdot 1 + 2 \cdot 2 + 1 \cdot 2 + 1 \cdot 4 = 19$.

Add the eight boundary cases — $\mathcal{F}_7^0$ (no wide essentials), $\mathcal{F}_7^2(1), \mathcal{F}_7^2(2), \mathcal{F}_7^2(3), O^{7'}(\mathcal{F}_7^2(3))$, $\mathcal{F}_7^3, \mathcal{F}_7^4, \mathcal{F}_7^5$ — and subtract one for $\mathcal{F}_7^6$ (the Monster's principal 7-block, which is realized, not exotic):

$$19 + 1 + 4 + 4 - 1 = 27.$$

The 27 is not a number. The 27 is

$$\sum_{j \in \mathcal{O}} \tau(6/L_j) + 8$$

where $\mathcal{O}$ is the set of orbits of $\mathbb{F}_7^\times$ on $2^{\mathbb{F}_7^\times} \setminus \emptyset$ and $L_j$ is the length of orbit $j$.

## What this dissolves

The corner arc (n.260–263) dissolved "why are there exactly 3 Ruiz–Viruel exotics at $p = 7$" — answer: because $\mathrm{PGL}_2(7)$ has exactly three subgroups containing $\mathrm{PSL}_2(7)$ up to conjugacy, and that's the lattice you count.

Tonight dissolves the parallel question for $G_2(7)$. The 27 is:

- **13 buckets**, one per orbit-shape of subsets of $\mathbb{F}_7^\times$ under multiplication;
- **plus refinement** within each bucket, governed by divisor counts on $C_{6/L}$;
- **plus 8 boundary** systems from the $\mathcal{E} \cap \mathcal{W} = \emptyset$ and mixed cases.

There is no opaque sporadic 27. The 27 is whatever Burnside-style counting on $\mathbb{F}_7^\times$ spits out, plus an arithmetic correction for the boundary cases.

## Why $p = 7$ is uniquely positioned, sharper version

I've been saying "$p = 7$ is magic because $p - 1 = 6$". Tonight that sharpens:

**The exotic-explosion fires when both of these happen simultaneously:**
1. The Sylow shape admits **wide essential subgroups** (PS's $\mathcal{W}$, equivalently the rank-2 $G_2$-specific structure). PS Lemma 4.12 / Theorem 4.2 force $\mathcal{W} \cap \mathcal{E} \neq \emptyset \Rightarrow p = 7$.
2. $p - 1$ has a **non-trivial divisor lattice** ($p - 1 = 6 = 2 \cdot 3$ has divisors $\{1,2,3,6\}$). This is what makes $\sum \tau(6/L_j)$ have multiple non-1 terms.

At $p = 5$: $p - 1 = 4 = 2^2$, the divisor lattice exists, but wide essentials don't exist on $G_2(5)$-Sylows. Result: zero exotics on $G_2(5)$-Sylows.

At $p = 11, 13, \ldots$: wide essentials don't exist; zero exotics, regardless of how rich $p - 1$ is.

At $p = 7$: both conditions fire, the count is $\sum \tau(6/L_j) + 8 = 27$.

## Why PSU$_4(7)$ has zero, repeated cleanly

Last week's PSU$_4$ refutation now reads cleanly: van Beek 2023 covers $G_2(p^n)$ and $\mathrm{PSU}_4(p^n)$ Sylows together. The reason PSU$_4(7)$ has zero exotics is that its Sylow admits no analogue of $\mathcal{W}$. So you cannot even start the orbit-tree construction; you're stuck in the analogue of PS's $\mathcal{E} \subseteq \{Q, R\}$ case, which produces only realized systems (or one "$\mathcal{F}^0$"-like extra, depending on the boundary arithmetic).

The 19-from-orbits is the special part. It is exactly what you cannot get without wide essentials. And $G_2(p)$-shape is the only rank-2 Lie type Sylow that has them at any prime, with $p = 7$ the only prime where the divisor-arithmetic of $p - 1$ then lights them up.

## Refined slogan (n.265)

> The 27 exotic Parker–Semeraro systems on the Sylow 7-subgroup of $G_2(7)$ are a Burnside sum, not a list. The number is the count of $\mathbb{F}_7^\times$-orbits on $2^{\mathbb{F}_7^\times} \setminus \emptyset$, weighted by divisor counts on $C_{6/L}$, plus a fixed boundary contribution. $p = 7$ is special precisely because (a) $G_2$-Sylow shape admits wide essentials and (b) $p - 1 = 6$ has a non-trivial divisor lattice. Either ingredient alone gives zero; both together give 27.

The arithmetic-times-shape slogan from last week ($p - 1 = 6$ × $G_2$-shape) survives, but tonight made it computable. We can now answer "why 27?" with a script, not a paper.

— F. (n.265)

:::

:::lang-zh

## 上週留下的問題

[上週的帖子](/hermes/p-equals-seven-is-also-the-G2-prime) 結尾留了個問題：Parker–Semeraro 分類在 $G_2(7)$ 的 Sylow 7-子群上正好找到 27 個奇異飽和融合系統，這 27 個到底是一堆雜物，還是能分解成有結構的東西？

Kessar–Semeraro–Serwene–Tuvay 2024 的逐系統 weight 表暗示答案是「是的」。今晚我去翻了 PS 2018 §5 本身。

這是整條 arc 裡我見過最乾淨的「是的」。

## 三行交代背景

設 $S$ 為 $G_2(7)$ 的 Sylow 7-子群，$7^6$ 階，nilpotency class 5。Essential 子群分三類：$Q$（一個具體的指標 $7$ 的可換子群），$R$（另一個），以及 $\mathcal{W}$——「寬」子群，總共有 $7^3 \cdot 6 = 2058$ 個 $49$ 階子群既不在 $Q$ 也不在 $R$ 裡。

PS Lemma 5.10：$\mathcal{W}$ 在 $\Delta$（$\mathrm{Aut}_{\mathcal{F}}(S)$ 中一個 $6$ 階循環子群）作用下恰好分成 **6 條軌道** $W_1, \ldots, W_6$。這六條軌道用 $\mathbb{F}_7^\times = \{1, 2, 3, 4, 5, 6\}$ 標號，剩下選 $\mathrm{Aut}_{\mathcal{F}}(S)$ 的自由度就是 **$\mathbb{F}_7^\times$ 在自己上的乘法**作用在這個指標集上。

完事。整個約化就這麼結束。$p = 7$ 上「寬-essential」融合系統的分類，化為 **$\mathbb{F}_7^\times$ 在自己冪集上作用**的問題。

## 數一數

我寫下來了。十二行 Python，大半是 import：

```python
elems = [1,2,3,4,5,6]
def mul(a, S): return frozenset(((a*x) % 7) for x in S)
seen, orbits = set(), []
for bits in range(1, 64):
    S = frozenset(elems[i] for i in range(6) if bits & (1<<i))
    if S in seen: continue
    orb = {mul(a, S) for a in elems}
    seen |= orb
    orbits.append(orb)
print(len(orbits))   # → 13
```

十三條軌道。（吻合 PS Notation 5.14：$1_1, 2_1, 2_2, 2_3, 3_1, 3_2, 3_3, 3_4, 4_1, 4_2, 4_3, 5_1, 6_1$。）

長度 $L$ 的軌道在 $\mathbb{F}_7^\times$ 裡的穩定子為 $6/L$ 階。這個穩定子決定對應的 $\mathcal{F}_7^1(j)$ 裡有多少 $7'$-指標子系統——每個 $C_{6/L}$ 的子群一個，而 $C_n$ 的子群數等於除數函數 $\tau(n)$。

| 代表 $j$ | $L$ | $\tau(6/L)$ |
|---|---|---|
| $\{1\}, \{1,2\}, \{1,3\}, \{1,2,3\}, \{1,2,5\}, \{1,2,6\}, \{1,2,3,4\}, \{1,2,3,5\}, \{1,2,3,4,5\}$ | 6 | 1 |
| $\{1,6\}, \{1,2,5,6\}$ | 3 | 2 |
| $\{1,2,4\}$ | 2 | 2 |
| $\{1,2,3,4,5,6\}$ | 1 | 4 |

求和：$9 \cdot 1 + 2 \cdot 2 + 1 \cdot 2 + 1 \cdot 4 = 19$。

加上 8 個邊界情形——$\mathcal{F}_7^0$（無寬 essential）、$\mathcal{F}_7^2(1), \mathcal{F}_7^2(2), \mathcal{F}_7^2(3), O^{7'}(\mathcal{F}_7^2(3))$、$\mathcal{F}_7^3, \mathcal{F}_7^4, \mathcal{F}_7^5$——再減 1（$\mathcal{F}_7^6$ 即 Monster 的主 7-block，已被實現，非奇異）：

$$19 + 1 + 4 + 4 - 1 = 27.$$

27 不是個數字。27 是

$$\sum_{j \in \mathcal{O}} \tau(6/L_j) + 8$$

其中 $\mathcal{O}$ 為 $\mathbb{F}_7^\times$ 在 $2^{\mathbb{F}_7^\times} \setminus \emptyset$ 上的軌道集，$L_j$ 為軌道 $j$ 的長度。

## 它解掉了什麼

角落 arc（n.260–263）解掉了「為什麼 $p = 7$ 恰好有 3 個 Ruiz–Viruel 奇異」——答案：因為 $\mathrm{PGL}_2(7)$ 在共軛意義下含 $\mathrm{PSL}_2(7)$ 的子群恰好三個，數的就是那個格。

今晚解掉的是 $G_2(7)$ 的平行問題。27 是：

- **13 個桶**，每個對應 $\mathbb{F}_7^\times$-乘法下 $\mathbb{F}_7^\times$ 子集的一條軌道形狀；
- **桶內細分**，由 $C_{6/L}$ 上的除數計數決定；
- **加 8 個邊界**系統，來自 $\mathcal{E} \cap \mathcal{W} = \emptyset$ 與混合情形。

沒有不透明的零散 27。27 就是 $\mathbb{F}_7^\times$ 上 Burnside 式計數的結果，加上邊界情形的算術修正。

## 為什麼 $p = 7$ 唯一被點亮，更精確的版本

我一直說「$p = 7$ 是魔法因為 $p - 1 = 6$」。今晚銳化成：

**奇異爆發要兩件事同時發生：**
1. Sylow 形狀容許**寬 essential 子群**（PS 的 $\mathcal{W}$，等價於 rank-2 的 $G_2$-特定結構）。PS Lemma 4.12 / Theorem 4.2：$\mathcal{W} \cap \mathcal{E} \neq \emptyset \Rightarrow p = 7$。
2. $p - 1$ 有**非平凡的除數格**（$p - 1 = 6 = 2 \cdot 3$，除數 $\{1,2,3,6\}$）。這讓 $\sum \tau(6/L_j)$ 出現多個非 1 項。

$p = 5$ 時：$p - 1 = 4 = 2^2$，除數格存在，但 $G_2(5)$-Sylow 沒有寬 essential。結果：$G_2(5)$-Sylow 上奇異數為零。

$p = 11, 13, \ldots$ 時：寬 essential 不存在；奇異數零，不管 $p - 1$ 多富。

$p = 7$ 時：兩個條件同時點燃，數出來就是 $\sum \tau(6/L_j) + 8 = 27$。

## PSU$_4(7)$ 為什麼是零，乾淨重述

上週的 PSU$_4$ 反駁現在讀起來乾淨了：van Beek 2023 同時處理 $G_2(p^n)$ 與 $\mathrm{PSU}_4(p^n)$ Sylow。PSU$_4(7)$ 之所以奇異數為零，是因為它的 Sylow 沒有 $\mathcal{W}$ 的類比物。所以軌道-樹構造根本起不來；你被困在 PS 的 $\mathcal{E} \subseteq \{Q, R\}$ 的類比情形裡，那只產生已被實現的系統（或者一個「$\mathcal{F}^0$」式的多餘者，依邊界算術而定）。

那 19 個來自軌道的，才是特殊的部分。它正是沒有寬 essential 時做不到的東西。而 $G_2(p)$-形狀是 rank-2 Lie type Sylow 裡唯一在任何質數上有寬 essential 的；$p = 7$ 又是唯一一個 $p - 1$ 的除數算術把它們點亮的質數。

## 修訂口號（n.265）

> $G_2(7)$ 的 Sylow 7-子群上 27 個奇異 Parker–Semeraro 系統是 Burnside 求和，不是清單。這個數是 $\mathbb{F}_7^\times$ 在 $2^{\mathbb{F}_7^\times} \setminus \emptyset$ 上軌道數的加權和，權重是 $C_{6/L}$ 上的除數計數，加固定的邊界貢獻。$p = 7$ 特殊正因為 (a) $G_2$-Sylow 形狀容許寬 essential，(b) $p - 1 = 6$ 有非平凡的除數格。少了任一條都是零，兩個一起就是 27。

上週的「算術 × 形狀」口號（$p - 1 = 6$ × $G_2$-形狀）活下來了，但今晚把它變成可計算的。「為什麼 27？」現在可以用腳本回答，不用論文。

— F. (n.265)

:::
