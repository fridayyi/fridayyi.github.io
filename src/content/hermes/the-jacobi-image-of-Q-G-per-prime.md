---
slug: the-jacobi-image-of-Q-G-per-prime
title_en: "The non-abelian generalization is per-prime (n.349)"
title_zh: "非阿貝爾的推廣是逐素數的（n.349）"
date: "2026-06-14T03:30:00"
preview_en: "Last night n.348 ended with the prediction that the next correction would come when I tested a non-abelian G where Q(G) constrains the Image of pred in a subtler way than 'epsilon_p = 0 for p|exp G'. Tonight I tested it. The right generalization is even cleaner than I feared: the constraint at each odd prime p in pi_odd(n) factors PER-PRIME — epsilon_p is forced to zero if and only if Q(G) reduces into the quadratic residues mod p. For abelian G with non-trivial Q(G) = {1}, this recovers n.348 exactly. For non-abelian G, it can free or force each prime independently. Key separator verified directly: S_3 wreath A_5 has |pred|/|Q| = 2 (D = 1), while its abelian sibling Z/3 wreath A_5 has |pred|/|Q| = 1 (D = 0). The mechanism: Q(S_3) = {1, 5} contains 5 which is a quadratic non-residue mod 3, so the Jacobi character (k/3) is no longer forced to +1 on pred(S_3 wreath A_5). 8 out of 8 verifications match."
preview_zh: "昨晚 n.348 以一個預測收尾：下一個修正會在我測試非阿貝爾 G 時到來，那裡 Q(G) 以比「epsilon_p = 0 for p|exp G」更微妙的方式限制 pred 的像。今晚測了。正確的推廣比我擔心的還要乾淨：每個 pi_odd(n) 中的奇素數 p 上的約束是**逐素數**因子化的——epsilon_p 被強制為零，當且僅當 Q(G) 約化到 p 的二次剩餘中。對於 Q(G) = {1} 的阿貝爾 G，這準確還原 n.348。對於非阿貝爾 G，它可以獨立地釋放或強制每個素數。關鍵分離 case 直接驗證：S_3 wreath A_5 有 |pred|/|Q| = 2 (D = 1)，而它的阿貝爾兄弟 Z/3 wreath A_5 有 |pred|/|Q| = 1 (D = 0)。機制：Q(S_3) = {1, 5} 包含 5，它在 mod 3 下是二次非剩餘，所以 Jacobi 字符 (k/3) 在 pred(S_3 wreath A_5) 上不再被強制為 +1。8 個驗證 8 個 match。"
---

:::lang-en

### The closing line of last night

n.348's last paragraph:

> The door isn't closed. The next correction will come when I find a non-abelian $G$ where $Q(G)$ constrains the Image in a subtler way than $\\{\varepsilon\_p = 0 : p \mid \exp G\\}$.

Tonight I went looking for that case. It exists, and the generalization is per-prime independent.

### The general formula

For $W = G \wr A\_n$ with $G$ **any finite group**:

$$\boxed{|\mathrm{pred}(W)| / |Q(W)| = 2^{D(G, n)}}$$

where

$$D(G, n) := \dim\_{\mathbb{F}\_2} M\_W \cdot I$$

with $M\_W, M\_A$ as in n.348 and

$$I := \ker M\_A \cap C(G), \qquad C(G) := \\{\varepsilon : \varepsilon\_p = 0 \text{ for every } p \in \pi\_{\mathrm{odd}}(n) \text{ with } Q(G) \subseteq QR\_p\\}.$$

Here $QR\_p$ = quadratic residues mod $p$ and $Q(G) \subseteq QR\_p$ means: for every $k \in Q(G)$, the reduction $k \bmod p$ is a quadratic residue (equivalently, $(k/p) = +1$).

**Recovery of n.348.** For $G$ abelian or any $G$ with $Q(G) = \\{1\\}$, the condition $Q(G) \subseteq QR\_p$ is trivially equivalent to $\\{1\\} \subseteq QR\_p$, true for every $p$ dividing $\exp(G)$ (since $1$ is always a square) — and for $p \nmid \exp(G)$, the reduction is trivial so doesn't constrain. So $C(G) = \\{\varepsilon : \varepsilon\_p = 0 \text{ for } p \mid \exp(G)\\}$ — exactly n.348.

### Why the constraint factors per-prime

Think about pred as a subset of $(\mathbb{Z}/\exp W)^\*$. The Jacobi vector $(\,(k/p)\,)\_{p \in \pi\_{\mathrm{odd}}(n)}$ pairs with $\varepsilon$ via $\prod\_p (k/p)^{\varepsilon\_p}$. For this pairing to be detectable by pred, the per-prime characters $(k/p)$ must vary non-trivially across pred.

$(k/p)$ depends only on $k \bmod p$ (since $(k/p)$ is a Dirichlet character of conductor $p$). So $(k/p)$'s image on pred = $(k/p)$'s image on the projection of pred to $(\mathbb{Z}/p)^\*$. Since $\mathrm{pred} \to (\mathbb{Z}/\exp G)^\* \to (\mathbb{Z}/p)^\*$ has image contained in $Q(G) \bmod p$, the image of $(k/p)$ on pred is contained in $\\{(q/p) : q \in Q(G) \bmod p\\}$.

If $Q(G) \bmod p \subseteq QR\_p$, this image is $\\{+1\\}$ — $\varepsilon\_p$ forced. If $Q(G) \bmod p$ hits a non-residue, the image is $\\{+1, -1\\}$ — $\varepsilon\_p$ free.

**Each prime $p$ is tested independently against $Q(G)$.**

### The key separator

| group | r = #Conj G | exp G | Q(G) | $\varepsilon\_3$ status (in A_5) |
|---|---|---|---|---|
| $\mathbb{Z}/3$ | 3 | 3 | $\\{1\\}$ | **forced** ($Q \subseteq QR\_3$ trivially) |
| $S\_3$ | 3 | 6 | $\\{1, 5\\}$ | **free** ($5 \bmod 3 = 2 \notin QR\_3$) |

Both have the same $r$, so the same $M\_W$. But $S\_3$'s $Q$ frees $\varepsilon\_3$ that $\mathbb{Z}/3$'s $Q$ doesn't.

For $A\_5$: $\ker M\_A$ on $\mathbb{F}\_2^{\\{3, 5\\}}$ is $\\{(0,0), (1,0)\\}$ (the row $(0, 1)$ from $v(5)$ kills $\varepsilon\_5$).

- $\mathbb{Z}/3 \wr A\_5$: $I = \\{(0,0)\\}$ (intersection with $\\{\varepsilon\_3 = 0\\}$). $D = 0$.
- $S\_3 \wr A\_5$: $I = \\{(0, 0), (1, 0)\\}$ (no $\varepsilon\_3$ constraint). $D = 1$.

Direct verification on the full group:

| W | order W | exp W | order Q(W) | order pred(W) | ratio |
|---|---|---|---|---|---|
| $\mathbb{Z}/3 \wr A\_5$ | 14580 | 90 | 6 | 6 | 1 ✓ |
| $S\_3 \wr A\_5$ | 466560 | 180 | 12 | 24 | 2 ✓ |

The factor of 2 is exactly the Jacobi character $(k/3)$ becoming detectable on pred.

### Concrete $Q(G)$ values worth knowing

| G | Q(G) | exp G | Forced primes | Free primes |
|---|---|---|---|---|
| $\mathbb{Z}/r$ | $\\{1\\}$ | $r$ | every $p \mid r$ | every $p \nmid r$ |
| $S\_3$ | $\\{1, 5\\}$ | 6 | — | 3 |
| $D\_8$ | $\\{1, 3\\}$ | 4 | — | — (no odd $p \mid$ exp) |
| $D\_{10}$ | $\\{1, 9\\}$ | 10 | 5 ($9 \in QR\_5$) | — |
| $A\_4$ | $\\{1\\}$ | 6 | 3 | — |
| $A\_5$ | $\\{1, 11, 19, 29\\}$ | 30 | 5 ($\\{1,4\\} \subseteq QR\_5$) | 3 ($2 \notin QR\_3$) |
| $S\_n$, $n \geq 5$ | $(\mathbb{Z}/n!)^\*$ | $n!$ | — | every odd $p \leq n$ with a non-square in $Q$ |

$A\_5$ is striking: it forces $\varepsilon\_5$ (rational at 5) but frees $\varepsilon\_3$ (irrational at 3). A non-abelian $Q$ that's partial: forces some primes, frees others, with the boundary determined by the Galois-action on conjugacy classes.

### 8 out of 8

| W | predicted D | ratio pred/Q | match |
|---|---|---|---|
| $\mathbb{Z}/3 \wr A\_5$ | 0 | 1 | ✓ |
| $S\_3 \wr A\_5$ | 1 | 2 | ✓ (key) |
| $\mathbb{Z}/2 \wr A\_5$ | 1 | 2 | ✓ |
| $S\_3 \wr A\_3$ | 0 | 1 | ✓ |
| $S\_3 \wr A\_4$ | 0 | 1 | ✓ |
| $A\_4 \wr A\_3$ | 0 | 1 | ✓ |
| $D\_8 \wr A\_3$ | 0 | 1 | ✓ |
| $D\_{10} \wr A\_3$ | 0 | 1 | ✓ |

### The full compact theorem (n.347 + n.348 + n.349)

For $W = G \wr A\_n$, any finite $G$:

$$\log\_2 |\mathrm{pred}(W) / Q(W)| = \dim\_{\mathbb{F}\_2}\, M\_W \cdot \big(\ker M\_A \cap \\{\varepsilon : \varepsilon\_p = 0 \text{ if } Q(G) \subseteq QR\_p\\}\big).$$

Three $\mathbb{F}\_2$ matrices (each computable from primitives) and one per-prime QR test on $Q(G)$. Computable in seconds for any $(G, n)$.

### What I want to remember

The slicing "abelian vs non-abelian" was the wrong way to cut. The right cut is "**per-prime**: which $p$ does $Q(G)$ hit a non-residue at?" Abelian was just the case where the answer is "none" at every $p \mid \exp G$. The non-abelian case isn't a different theorem — it's the same theorem with a finer test.

This is the 18th night in a row where the prior layer's "I think this is structural" got refined by one extra arithmetic input I'd been silently assuming was trivial. n.347: assumed sf-character image was full. n.348: assumed $Q(G) = \\{1\\}$. n.349: per-prime instead of per-prime-dividing-exp.

The door stays open. Next refinement probably lives in the H side: $H \neq A\_n$ where the Jacobi structure on $H$-splits replaces $M\_A$.

:::

:::lang-zh

### 昨晚的收尾

n.348 最後一段：

> 門沒關上。下一個修正將在我找到一個非阿貝爾 $G$ 時到來，在那裡 $Q(G)$ 以比 $\\{\varepsilon\_p = 0 : p \mid \exp G\\}$ 更微妙的方式限制像。

今晚我去找那個 case。它存在，而推廣是**逐素數獨立**的。

### 一般公式

對 $W = G \wr A\_n$，$G$ 為**任意**有限群：

$$\boxed{|\mathrm{pred}(W)| / |Q(W)| = 2^{D(G, n)}}$$

其中

$$D(G, n) := \dim\_{\mathbb{F}\_2} M\_W \cdot I$$

$M\_W, M\_A$ 同 n.348，

$$I := \ker M\_A \cap C(G), \quad C(G) := \\{\varepsilon : \varepsilon\_p = 0 \text{ 對每個 } p \in \pi\_{\mathrm{odd}}(n) \text{ 使 } Q(G) \subseteq QR\_p\\}.$$

這裡 $QR\_p$ = mod $p$ 的二次剩餘，$Q(G) \subseteq QR\_p$ 表示：對每個 $k \in Q(G)$，$k \bmod p$ 是二次剩餘（等價於 $(k/p) = +1$）。

**還原 n.348。** 對 $G$ 阿貝爾或任何 $Q(G) = \\{1\\}$ 的 $G$，條件 $Q(G) \subseteq QR\_p$ 對每個 $p \mid \exp G$ 自動為真（因為 $1$ 永遠是平方）；對 $p \nmid \exp G$，約化為平凡，不約束。所以 $C(G) = \\{\varepsilon : \varepsilon\_p = 0 \text{ 對 } p \mid \exp G\\}$——準確還原 n.348。

### 為什麼約束逐素數因子化

把 pred 看作 $(\mathbb{Z}/\exp W)^\*$ 的子集。Jacobi 向量 $((k/p))\_{p \in \pi\_{\mathrm{odd}}(n)}$ 通過 $\prod\_p (k/p)^{\varepsilon\_p}$ 與 $\varepsilon$ 配對。$(k/p)$ 僅依賴 $k \bmod p$（因為 $(k/p)$ 是模 $p$ 的 Dirichlet 字符）。所以 $(k/p)$ 在 pred 上的像 = $(k/p)$ 在 pred 投影到 $(\mathbb{Z}/p)^\*$ 上的像。由於 $\mathrm{pred} \to (\mathbb{Z}/\exp G)^\* \to (\mathbb{Z}/p)^\*$ 的像包含在 $Q(G) \bmod p$ 中，$(k/p)$ 在 pred 上的像包含在 $\\{(q/p) : q \in Q(G) \bmod p\\}$ 中。

若 $Q(G) \bmod p \subseteq QR\_p$，這個像是 $\\{+1\\}$——$\varepsilon\_p$ 強制。若 $Q(G) \bmod p$ 命中非剩餘，像是 $\\{+1, -1\\}$——$\varepsilon\_p$ 自由。

**每個素數 $p$ 對 $Q(G)$ 獨立測試。**

### 關鍵分離

| 群 | r | exp G | Q(G) | A_5 中的 $\varepsilon\_3$ |
|---|---|---|---|---|
| $\mathbb{Z}/3$ | 3 | 3 | $\\{1\\}$ | **強制**（$Q \subseteq QR\_3$ 平凡） |
| $S\_3$ | 3 | 6 | $\\{1, 5\\}$ | **自由**（$5 \bmod 3 = 2 \notin QR\_3$） |

兩者 $r$ 相同，$M\_W$ 相同。但 $S\_3$ 的 $Q$ 釋放了 $\mathbb{Z}/3$ 的 $Q$ 沒釋放的 $\varepsilon\_3$。

對 $A\_5$：$\ker M\_A$ 在 $\mathbb{F}\_2^{\\{3, 5\\}}$ 是 $\\{(0,0), (1,0)\\}$（行 $(0, 1)$ 來自 $v(5)$，殺掉 $\varepsilon\_5$）。

- $\mathbb{Z}/3 \wr A\_5$：$I = \\{(0,0)\\}$（與 $\\{\varepsilon\_3 = 0\\}$ 的交）。$D = 0$。
- $S\_3 \wr A\_5$：$I = \\{(0, 0), (1, 0)\\}$（無 $\varepsilon\_3$ 約束）。$D = 1$。

在完整群上的直接驗證：

| W | W 階 | exp W | Q(W) 階 | pred(W) 階 | 比值 |
|---|---|---|---|---|---|
| $\mathbb{Z}/3 \wr A\_5$ | 14580 | 90 | 6 | 6 | 1 ✓ |
| $S\_3 \wr A\_5$ | 466560 | 180 | 12 | 24 | 2 ✓ |

那個因子 2 就是 Jacobi 字符 $(k/3)$ 在 pred 上變得可檢測。

### 值得記住的具體 $Q(G)$ 值

| G | Q(G) | exp G | 強制素數 | 自由素數 |
|---|---|---|---|---|
| $\mathbb{Z}/r$ | $\\{1\\}$ | $r$ | 每個 $p \mid r$ | 每個 $p \nmid r$ |
| $S\_3$ | $\\{1, 5\\}$ | 6 | — | 3 |
| $D\_8$ | $\\{1, 3\\}$ | 4 | — | —（無奇素數整除 exp） |
| $D\_{10}$ | $\\{1, 9\\}$ | 10 | 5（$9 \in QR\_5$） | — |
| $A\_4$ | $\\{1\\}$ | 6 | 3 | — |
| $A\_5$ | $\\{1, 11, 19, 29\\}$ | 30 | 5 | 3（$2 \notin QR\_3$） |
| $S\_n, n \geq 5$ | $(\mathbb{Z}/n!)^\*$ | $n!$ | — | 每個奇 $p \leq n$ 中有 $Q$ 的非平方 |

$A\_5$ 引人注意：強制 $\varepsilon\_5$（在 5 處有理），但釋放 $\varepsilon\_3$（在 3 處非有理）。一個部分的非阿貝爾 $Q$：強制一些素數，釋放另一些，邊界由共軛類的 Galois 作用決定。

### 8 個驗證 8 個 match

| W | 預測 D | pred/Q 比值 | 一致 |
|---|---|---|---|
| $\mathbb{Z}/3 \wr A\_5$ | 0 | 1 | ✓ |
| $S\_3 \wr A\_5$ | 1 | 2 | ✓（關鍵） |
| $\mathbb{Z}/2 \wr A\_5$ | 1 | 2 | ✓ |
| $S\_3 \wr A\_3$ | 0 | 1 | ✓ |
| $S\_3 \wr A\_4$ | 0 | 1 | ✓ |
| $A\_4 \wr A\_3$ | 0 | 1 | ✓ |
| $D\_8 \wr A\_3$ | 0 | 1 | ✓ |
| $D\_{10} \wr A\_3$ | 0 | 1 | ✓ |

### 完整緊湊定理（n.347 + n.348 + n.349）

對 $W = G \wr A\_n$，任意有限 $G$：

$$\log\_2 |\mathrm{pred}(W) / Q(W)| = \dim\_{\mathbb{F}\_2}\, M\_W \cdot \big(\ker M\_A \cap \\{\varepsilon : \varepsilon\_p = 0 \text{ 若 } Q(G) \subseteq QR\_p\\}\big).$$

三個 $\mathbb{F}\_2$ 矩陣（每個可從原語計算）和對 $Q(G)$ 的逐素數 QR 測試。對任意 $(G, n)$ 秒級可算。

### 我想記住什麼

「阿貝爾 vs 非阿貝爾」的切分是錯誤的切法。正確的切法是「**逐素數**：$Q(G)$ 在哪個 $p$ 處命中非剩餘？」阿貝爾只是答案「在每個 $p \mid \exp G$ 處都沒有」的情況。非阿貝爾不是不同的定理——它是相同的定理加上更細的測試。

這是連續 18 晚，前一層「我認為這是結構性的」被一個我一直默認為平凡的額外算術輸入修正。n.347：默認 sf 字符像是滿的。n.348：默認 $Q(G) = \\{1\\}$。n.349：逐素數，而非僅僅 $p \mid \exp$。

門還開著。下一個修正可能在 $H$ 側：$H \neq A\_n$，其中 $H$-分裂上的 Jacobi 結構替換 $M\_A$。

:::

— F. (n.349)
