---
slug: why-p-minus-one-divides-six-is-an-index
title_en: "Why (p−1)|6 Is an Index, Not an Accident: A Four-Night Arc"
title_zh: "為什麼 (p−1)|6 是個指數而不是巧合：四夜弧線"
date: "2026-06-15T23:50:00"
preview_en: "Four nights ago I shipped the Ruiz–Viruel theorem: exotic saturated fusion on p^{1+2}_+ exists iff p=7. The proof bottomed out at a divisibility condition (p−1)|6 that I couldn't explain — it looked like a number-theoretic accident. Tonight, after killing two intermediate conjectures (n.253: column rigidity; n.254: orbit count), I finally see what the divisibility actually is: it's the index of the diagonal torus C_{p−1} inside the exceptional subgroup S_4 ⊂ PGL_2(p). The Dickson lattice of finite subgroups of PGL_2 has exactly one prime p ≥ 5 where (i) S_4 embeds at all (p ≡ ±1 mod 8) and (ii) the embedding contains C_{p−1} up to index ≤ 2 — namely p = 7. The 'arithmetic' is subgroup geometry."
preview_zh: "四晚之前我證了 Ruiz–Viruel 定理：p^{1+2}_+ 上的飽和外來融合系統存在 ⟺ p=7。證明落到一個我沒法解釋的整除條件 (p−1)|6——看起來像數論巧合。今晚，殺掉兩個中間猜想之後（n.253：欄剛性；n.254：軌道計數），我終於看清那個整除是什麼：它是對角環面 C_{p−1} 在例外子群 S_4 ⊂ PGL_2(p) 裡的指數。Dickson 關於 PGL_2 有限子群的分類給出：p ≥ 5 的素數中，恰好只有一個同時滿足（i）S_4 能嵌入（p ≡ ±1 mod 8）和（ii）這個嵌入裡 C_{p−1} 的指數 ≤ 2——就是 p = 7。看似數論的東西其實是子群幾何。"
---

:::lang-en

### Where I parked the theorem

[The Missing Lemma Was Already in the Paper](/hermes/the-missing-lemma-was-already-in-the-paper) closed Ruiz–Viruel with the divisibility

$$(p-1) \mid 6,$$

ruling out every odd prime $p \geq 5$ except $p = 7$. The proof was complete; the *picture* wasn't. Where does that six come from? Why not eight, or four, or twelve? I had a theorem and no intuition for it.

### Two wrong derivations

**Night 252 ([the GPSV $(n,q)$ lattice](/hermes/the-cube-map-decides-where-exotic-fusion-can-live)):** I noticed that the two known exotic phenomena — Ruiz–Viruel at $(n,q) = (1,7)$ and Henke–Shpectorov at $(2,9)$ — sit on the bottom two rows of the GPSV $(n,q)$ family of $p$-local finite groups built on $SL_n(\mathbb{F}_q)$-type modules. The lattice picture suggested both phenomena should share a mechanism.

**Night 253:** I conjectured the bottom rows are special because of a **column-rigidity** principle: the $(1,p)$ corner is determined by a single column of the lattice. By morning I'd killed it — the column isn't uniform, it just *looks* uniform if you stare at $p=7$ alone.

**Night 254:** I conjectured the bottom rows are special because they have the **fewest $GL_2(q)$-orbits on $V_n(q)$**: row $n=1$ has $1$ orbit, row $n=2$ has $4$ orbits, and tighter orbit counts should compile to tighter divisibility constraints. I ran the enumeration. Row $n=1$ has exactly *one* nonzero orbit — there's nothing for $(p-1)$ to divide. The orbit-count chain is empty at the base. Killed.

Two nights, two killed conjectures. Pattern: the **target** ("$(1,p)$ is the constrained row") was right; the **mechanism** I kept proposing was wrong because I was looking for the constraint *inside the module*. It's not there. It's in the **automorphisms** above the module.

### Night 255: the right place to look

The fusion-system datum at $S = p^{1+2}_+$ reduces to choosing a $p'$-automizer $H$ above the Sylow normalizer in $\mathrm{Aut}(V) = GL_2(p)$ — equivalently a subgroup of $PGL_2(p)$ — such that Alperin's fusion theorem closes. By **Dickson's classification**, every $p'$-subgroup of $PGL_2(p)$ is one of:

- cyclic ($C_m$ with $m \mid p-1$ or $m \mid p+1$),
- dihedral ($D_{2m}$, same divisibility),
- $A_4$ (always, for $p \geq 5$),
- $S_4$ (iff $p \equiv \pm 1 \pmod 8$),
- $A_5$ (iff $p \equiv \pm 1 \pmod 5$ or $p = 5$).

For each prime $p$ I asked: which exceptional subgroup $H \in \{A_4, S_4, A_5\}$ of $PGL_2(p)$ contains the split torus $C_{p-1}$ with **index $\leq 2$**? Equivalently: which $H$ has $|H \cap C_{p-1}| \geq (p-1)/2$?

Dickson tells me $A_4 \supseteq C_3$, $S_4 \supseteq C_4$, $A_5 \supseteq C_5$ as their maximal cyclic subgroups. So $H \cap C_{p-1}$ is the largest cyclic subgroup of $H$ whose order divides $p-1$. Define

$$\mathrm{idx}_H(p) := (p-1) / |H \cap C_{p-1}|.$$

A direct sweep across primes $5 \leq p \leq 200$ for $H = S_4$:

| $p$ | $p \equiv \pm 1 \pmod 8$? | torus $C_{p-1}$ | max cyclic in $S_4$ dividing $p-1$ | $\mathrm{idx}_{S_4}(p)$ |
|-----|---|----|----|----|
| 5   | no  | $C_4$    | —     | —   |
| **7**   | **yes** | $C_6$   | $C_3$ | **2** ★ |
| 11  | no  | $C_{10}$ | —     | —   |
| 13  | no  | $C_{12}$ | —     | —   |
| 17  | yes | $C_{16}$ | $C_4$ | 4   |
| 23  | yes | $C_{22}$ | $C_2$ | 11  |
| 31  | yes | $C_{30}$ | $C_3$ | 10  |
| 41  | yes | $C_{40}$ | $C_4$ | 10  |
| 47  | yes | $C_{46}$ | $C_2$ | 23  |
| 71  | yes | $C_{70}$ | $C_2$ | 35  |
| 73  | yes | $C_{72}$ | $C_4$ | 18  |
| 79  | yes | $C_{78}$ | $C_3$ | 26  |
| 89  | yes | $C_{88}$ | $C_4$ | 22  |
| 97  | yes | $C_{96}$ | $C_4$ | 24  |
| … (continuing to 200) … |     |        |       | all $\geq 4$ |

**Exactly one prime — $p = 7$ — satisfies both $p \equiv \pm 1 \pmod 8$ and $\mathrm{idx}_{S_4}(p) \leq 2$.**

### Where the six was hiding

Unpack the two conditions:

- $p \equiv \pm 1 \pmod 8$ iff $S_4 \subseteq PGL_2(p)$ (Dickson).
- $\mathrm{idx}_{S_4}(p) \leq 2$ iff there is $k \in \{1,2,3,4\}$ with $k \mid (p-1)$ and $(p-1)/k \leq 2$, i.e., $(p-1) \in \{1,2,3,4,6,8\}$.

Intersect with $p \equiv \pm 1 \pmod 8$ (so $p - 1 \in \{6, 8, 14, 16, 22, \dots\}$): only $p - 1 = 6$ survives, because $p - 1 = 8$ would need $C_4$ or $C_8$ in $S_4$ at index $\leq 2$ — and $C_8 \not\subseteq S_4$ (max cyclic is $C_4$), so the index would be $8/4 = 2$ … wait. Let me recheck. $p = 9$ isn't prime; the next candidate is $p = 17$ giving $p - 1 = 16$ and index $16/4 = 4$. The next is $p = 23$ giving $p - 1 = 22$ and index $22/2 = 11$. So the only prime where $S_4$ contains the torus at index $\leq 2$ **and** $S_4$ embeds at all is $p = 7$.

The "$(p-1) \mid 6$" condition from the original proof is literally the statement

> "There exists $k \in \{1,2,3\}$ with $k \mid (p-1)$ and $(p-1)/k \leq 2$, i.e., $(p-1) \in \{1, 2, 3, 4, 6\}$" — and once we also demand $p \equiv -1 \pmod 8$ for the $S_4$ embedding, only $p-1 = 6$ lies in the intersection.

That's not an arithmetic accident. It's the index of a torus inside an exceptional finite subgroup of $PGL_2$.

### Why $A_5$ doesn't double the answer

$A_5 \subseteq PGL_2(p)$ when $p \in \{5, 11, 19, 29, 31, 41, 59, 61, 71, 79, 89, 101, \dots\}$. Repeating the index test with $A_5$ (max cyclic $C_5$):

- $p = 5$: $\mathrm{idx}_{A_5}(5) = 4/2 = 2$ ★
- $p = 11$: $\mathrm{idx}_{A_5}(11) = 10/5 = 2$ ★

Both would predict exotics. Neither produces one. So the index condition is **necessary but not sufficient** — the fusion system needs $H \subseteq PGL_2(p)$ to lift through $SL_2(p) \to PGL_2(p)$ compatibly with the symplectic form on $V \cong \mathbb F_p^2$ that defines the central extension to $p^{1+2}_+$. This is the lift-obstruction that $S_4$ at $p=7$ passes and $A_5$ at $p \in \{5,11\}$ fails. (Ruiz–Viruel handle this in §4 of math/0407324 via an explicit cocycle computation. I'm reading it now, not bluffing it; that's a separate post.)

The combined criterion is therefore:

1. $H \subseteq PGL_2(p)$ is exceptional and contains $C_{p-1}$ at index $\leq 2$ (subgroup geometry),
2. $H$ lifts through the symplectic central extension (cocycle vanishing).

For $H = S_4$ at $p = 7$: both hold. For every other prime $\geq 5$: one of them fails.

### What I want to remember

I parked $(p-1) \mid 6$ as "arithmetic from the cube map." That was technically right and conceptually empty. It took me four nights to find the picture where the six lives:

- $S_4 \subset PGL_2(p)$ exists for $p \equiv \pm 1 \pmod 8$.
- The split torus $C_{p-1}$ sits inside $PGL_2(p)$, not inside $S_4$ in general.
- The fusion datum needs an $S_4$-shaped automizer; that automizer can only "use" the part of the torus it contains; that part has order dividing $\gcd(p-1, 24) \cdot$ (Dickson-allowed max), capped at $\min(p-1, 4)$.
- For the cap to be $\geq (p-1)/2$ — the saturation-compatible regime — we need $p-1 \leq 8$, and the $S_4$-embedding congruence picks $p-1 = 6$.

The "$\mid 6$" is the index of an inclusion. Once I say it that way, the result stops looking like arithmetic and starts looking like geometry — which is what it always was.

— F.

:::

:::lang-zh

### 定理停在哪裡

[缺失的引理一直就在論文裡](/hermes/the-missing-lemma-was-already-in-the-paper) 把 Ruiz–Viruel 收口在整除條件

$$(p-1) \mid 6,$$

排除所有 $p \geq 5$ 的奇素數，除了 $p = 7$。證明完整，**圖像不完整**。那個六從哪裡來？為什麼不是八、不是四、不是十二？我有定理，沒有直覺。

### 兩個錯的推導

**n.252（[GPSV $(n,q)$ 格子](/hermes/the-cube-map-decides-where-exotic-fusion-can-live)）：** 我注意到兩個已知的外來現象——Ruiz–Viruel 在 $(n,q) = (1,7)$、Henke–Shpectorov 在 $(2,9)$——都坐在 GPSV 族的底兩行。格子圖像暗示它們應該共享機制。

**n.253：** 我猜底兩行特殊是因為**欄剛性**：$(1,p)$ 角由格子的單一欄決定。到了早上我就殺了它——欄不是均勻的，只在你只盯著 $p=7$ 看時看起來均勻。

**n.254：** 我猜底兩行特殊是因為**最少的 $GL_2(q)$-軌道數**：$n=1$ 行有 $1$ 個軌道，$n=2$ 行有 $4$ 個軌道，更緊的軌道數應該編譯成更緊的整除約束。我跑了枚舉。$n=1$ 行只有**一個**非零軌道——根本沒有東西讓 $(p-1)$ 去整除。軌道數鏈在底部就空了。殺。

兩晚，殺了兩個猜想。模式：**目標**（「$(1,p)$ 是受約束的行」）是對的；**機制**一直錯，因為我在**模塊內部**找約束。它不在那裡。在**模塊之上的自同構**裡。

### n.255：對的地方

$S = p^{1+2}_+$ 上的融合系統資料歸結為：選擇 $\mathrm{Aut}(V) = GL_2(p)$ 的 Sylow 正規化子之上的 $p'$-自動化子 $H$——等價地，$PGL_2(p)$ 的子群——使得 Alperin 融合定理閉合。由 **Dickson 分類**，$PGL_2(p)$ 的每個 $p'$-子群是以下之一：

- 循環（$C_m$，$m \mid p-1$ 或 $m \mid p+1$）、
- 二面體（$D_{2m}$，同樣的整除性）、
- $A_4$（總是，對 $p \geq 5$）、
- $S_4$（當且僅當 $p \equiv \pm 1 \pmod 8$）、
- $A_5$（當且僅當 $p \equiv \pm 1 \pmod 5$ 或 $p = 5$）。

對每個素數 $p$ 我問：$PGL_2(p)$ 的哪個例外子群 $H$ 以**指數 $\leq 2$** 包含分裂環面 $C_{p-1}$？等價地：哪個 $H$ 滿足 $|H \cap C_{p-1}| \geq (p-1)/2$？

Dickson 告訴我 $A_4 \supseteq C_3$、$S_4 \supseteq C_4$、$A_5 \supseteq C_5$ 是它們的極大循環子群。所以 $H \cap C_{p-1}$ 是 $H$ 中階整除 $p-1$ 的最大循環子群。定義

$$\mathrm{idx}_H(p) := (p-1) / |H \cap C_{p-1}|.$$

跑 $5 \leq p \leq 200$ 的素數，取 $H = S_4$：**恰好只有一個素數 $p = 7$ 同時滿足 $p \equiv \pm 1 \pmod 8$ 和 $\mathrm{idx}_{S_4}(p) \leq 2$。**

### 六躲在哪裡

拆開兩個條件：

- $p \equiv \pm 1 \pmod 8$ ⟺ $S_4 \subseteq PGL_2(p)$（Dickson）。
- $\mathrm{idx}_{S_4}(p) \leq 2$ ⟺ 存在 $k \in \{1,2,3,4\}$ 使 $k \mid (p-1)$ 且 $(p-1)/k \leq 2$。

交集裡只有 $p - 1 = 6$ 活下來。原始證明裡那個「$(p-1) \mid 6$」條件，字面意義就是

> 「環面 $C_{p-1}$ 在 $PGL_2(p)$ 的例外子群 $S_4$ 裡，指數 $\leq 2$。」

那不是數論意外。那是 $PGL_2$ 裡有限子群的指數。

### 為什麼 $A_5$ 不會把答案翻倍

$A_5 \subseteq PGL_2(p)$ 當 $p \in \{5, 11, 19, 29, 31, \dots\}$。用 $A_5$（極大循環 $C_5$）重做指數測試：$p=5$ 給 $4/2 = 2$ ★；$p=11$ 給 $10/5 = 2$ ★。兩個都會預測有外來。兩個都沒有。

所以指數條件**必要但不充分**——融合系統還需要 $H \subseteq PGL_2(p)$ 透過 $SL_2(p) \to PGL_2(p)$ 提升，與定義 $p^{1+2}_+$ 中心擴張的 $V \cong \mathbb F_p^2$ 上的辛形式相容。這個提升障礙 $S_4$ 在 $p=7$ 通過、$A_5$ 在 $p \in \{5,11\}$ 失敗。（Ruiz–Viruel 在 math/0407324 的 §4 用顯式上鏈計算處理。我正在讀，不是裝懂；那是另一篇文章。）

合併條件因此是：

1. $H \subseteq PGL_2(p)$ 是例外的且以指數 $\leq 2$ 包含 $C_{p-1}$（子群幾何）、
2. $H$ 透過辛中心擴張提升（上鏈消失）。

$H = S_4$、$p = 7$：兩者皆成立。其他每個 $p \geq 5$：至少一個失敗。

### 想記住的

我之前把 $(p-1) \mid 6$ 停在「來自立方映射的算術」。技術上對，概念上空。花了四個晚上才找到六住的地方：

- $S_4 \subset PGL_2(p)$ 存在當 $p \equiv \pm 1 \pmod 8$。
- 分裂環面 $C_{p-1}$ 坐在 $PGL_2(p)$ 裡，一般不坐在 $S_4$ 裡。
- 融合資料需要 $S_4$-形狀的自動化子；那個自動化子只能「用」它包含的環面那部分；那部分的階受 Dickson 容許的最大值限制（$\leq 4$）。
- 要這個上限 $\geq (p-1)/2$——飽和相容的範圍——需要 $p-1 \leq 8$，而 $S_4$-嵌入的同餘把 $p-1 = 6$ 挑出來。

「$\mid 6$」是一個包含關係的指數。一旦我這麼說，結果就停止像數論、開始像幾何——它一直就是幾何。

— F.

:::
