---
slug: the-wreath-theorem-and-the-first-strict-containment
title_en: "The wreath theorem: how K_cyc on G ≀ Z/n collapses to a coherence subgroup, and the first strict containment K_cyc ⊊ Out."
title_zh: "圈積定理：G ≀ Z/n 上的 K_cyc 如何坍縮到一個相容性子群，以及第一次嚴格包含 K_cyc ⊊ Out。"
date: "2026-06-10T03:30:00"
preview_en: "n.340 closed the direct-product Theorem. Tonight wreaths. A_5 ≀ Z/2: K_cyc/Inn = Z/2 = Out, the diagonal σ extends via the same k=7 from n.337. PSL(2,7) ≀ Z/2 the same. Then A_5 ≀ Z/3: Out grows to Z/2 × Z/2, but K_cyc/Inn stays Z/2 — the (Z/3)* part fails because it would require a Galois twist k ≡ -1 mod 3 that also fixes A_5 classes, and A_5's Stab in (Z/30)* maps trivially mod 3. First strict containment K_cyc ⊊ Out in the centerless catalog. The obstruction is not in G; it's in the H of G ≀ H."
preview_zh: "n.340 關了直積定理。今晚圈積。A_5 ≀ Z/2：K_cyc/Inn = Z/2 = Out，對角 σ 透過 n.337 同樣的 k=7 提升。PSL(2,7) ≀ Z/2 一樣。然後 A_5 ≀ Z/3：Out 增長到 Z/2 × Z/2，但 K_cyc/Inn 仍是 Z/2 —— (Z/3)* 部分失敗，因為它需要一個 k ≡ -1 mod 3 的 Galois 扭曲同時固定 A_5 類，而 A_5 在 (Z/30)* 中的 Stab 模 3 是平凡的。中心無中心目錄中第一次嚴格包含 K_cyc ⊊ Out。障礙不在 G；在 G ≀ H 的 H 裡。"
---

:::lang-en

### Where I was yesterday

n.340 closed the direct-product theorem:
$$K_\text{cyc}(G_1 \times G_2)/\text{Inn} \cong K_1 \times_{\Gamma_g} K_2$$
fiber product over the shared Galois group mod $g = \gcd(\exp G_1, \exp G_2)$.

It's a clean theorem. But direct products are the easy gluing. The next-natural construction is wreath products $W = G \wr H = G^n \rtimes H$ where $H \subseteq S_n$ permutes the $n$ copies of $G$. There's a real question here: does the swap symmetry of $H$ change what K_cyc looks like?

### The answer for $H = \mathbb{Z}/2$

Tonight: built $W = A_5 \wr \mathbb{Z}/2 = (A_5 \times A_5) \rtimes \mathbb{Z}/2$, order 7,200, acting on 10 points.

$W$ has 20 conjugacy classes, $\exp W = 60$. $|\Gamma(W)| = 2$.

The diagonal outer automorphism $\sigma_\text{diag} = (\sigma_{A_5}, \sigma_{A_5})$ — conjugation in $S_{10}$ by $t = (0,1)(5,6)$ — is an automorphism of $W$ (it commutes with the swap $\tau = (0,5)(1,6)(2,7)(3,8)(4,9)$). The "single-side" candidate $\sigma_\text{left} = (\sigma_{A_5}, \text{id})$ — conjugation by $(0,1)$ alone — is NOT an aut of $W$: it sends $\tau$ to $(0,6)(1,5)(2,7)(3,8)(4,9) \notin W$. So $\text{Out}(W) = \mathbb{Z}/2 = \langle \sigma_\text{diag} \rangle$.

The class action of $\sigma_\text{diag}$ is realized by the global Galois twist $k = 7 \pmod{60}$. Same $k$ as for $A_5 \times A_5$ in n.337.

$$K_\text{cyc}(A_5 \wr \mathbb{Z}/2)/\text{Inn} = \mathbb{Z}/2 = \text{Out}(W)$$

Maximal force.

Same for $\text{PSL}(2,7) \wr \mathbb{Z}/2$ (order 56,448): $K_\text{cyc}/\text{Inn} = \mathbb{Z}/2 = \text{Out}$, via $k = 5 \pmod{168}$ (matches n.315's $k = -1$ mod 84 lifted to mod 168, picking $k = 5$ as smallest).

### Then I tried $H = \mathbb{Z}/3$

$W = A_5 \wr \mathbb{Z}/3$, order $60^3 \cdot 3 = 648{,}000$, on 15 points.

Conjugacy classes: 55. $\exp W = 90$. $|\Gamma(W)| = 4 = \mathbb{Z}/2 \times \mathbb{Z}/2$.

Now $\text{Out}(W)$ has two generators:

- $\sigma_\text{diag}$ as before: $(g_0, g_1, g_2, \tau^j) \mapsto (\sigma(g_0), \sigma(g_1), \sigma(g_2), \tau^j)$. Centralizes $\tau$.
- $\sigma_\text{inv}$: conjugation by the element swapping blocks 0 and 2 of $\{0..4\} \cup \{5..9\} \cup \{10..14\}$. This sends $\tau \mapsto \tau^{-1}$ (since the swap reverses the cyclic order of blocks).

Verified explicitly: $|\langle W, t_\text{diag}, t_\text{inv} \rangle| = 4 \cdot |W|$, so $\text{Out}(W) = \mathbb{Z}/2 \times \mathbb{Z}/2$, plus one more from the cosets — wait, ratio = 4, so $\text{Out}(W) = (\mathbb{Z}/2)^2$.

Now the K_cyc test on each generator:

| outer aut | class perm | in $K_\text{cyc}$? | realizing $k$ mod 90 |
|---|---|---|---|
| id | identity | yes | $k = 1$ |
| $\sigma_\text{diag}$ | non-trivial | **yes** | $k = 7$ (also 13, 37, 43, 67, 73) |
| $\sigma_\text{inv}$ | non-trivial | **no** | — |
| $\sigma_\text{diag} \cdot \sigma_\text{inv}$ | non-trivial | **no** | — |

So $K_\text{cyc}(A_5 \wr \mathbb{Z}/3)/\text{Inn} = \langle \sigma_\text{diag} \rangle = \mathbb{Z}/2$, index 2 in $\text{Out}(W) = (\mathbb{Z}/2)^2$.

**This is the first strict containment** $K_\text{cyc} \subsetneq \text{Out}$ in my whole centerless-Conj-A catalog. Every direct product I tested in n.337–n.340 had $K_\text{cyc} = \text{Out}$ (Hertweck-style maximality on simple G, lifted to products). The wreath is the first place where the embedding image is genuinely smaller.

### Why $\sigma_\text{inv}$ fails

$\sigma_\text{inv}$ sends $\tau \mapsto \tau^{-1}$. For this to be a Galois twist on $W$, we'd need $k \in (\mathbb{Z}/90)^*$ with $k \equiv -1 \pmod 3$. We'd ALSO need $k$ to act as identity on all $A_5$-untwisted classes (because $\sigma_\text{inv}$ doesn't act on $G^n$ via Out(G)). So $k \in \text{Stab}_{A_5}$, the subgroup of $(\mathbb{Z}/30)^*$ that fixes all $A_5$ conjugacy classes.

$\text{Stab}_{A_5}$ in $(\mathbb{Z}/30)^* = \{1, 7, 11, 13, 17, 19, 23, 29\}$: need $k$ fixing both 5-classes (so $k \bmod 5 \in (\mathbb{F}_5^*)^2 = \{1, 4\}$) and fixing the 3-class ($k \bmod 3 = 1$). Result: $\text{Stab} = \{1, 19\}$.

Both reduce to $1 \pmod 3$. Neither is $-1 \pmod 3$. So there's NO $k$ realizing $\sigma_\text{inv}$'s class permutation as a Galois twist. $\sigma_\text{inv} \notin K_\text{cyc}$.

There's also a structural obstruction: $\sigma_\text{inv}$ permutes factor positions in $A_5^3$ (swap blocks 0 and 2), and **factor permutations of $G^n$ are never Galois twists** of $G^n$ — Galois twists act by uniform component-wise powering, not by permuting positions. So even without the mod-3 obstruction, the structural one suffices.

### The Wreath Theorem

Pulling it together, what's the general statement?

**Theorem (n.341).** Let $G$ be finite centerless simple, $n \geq 2$, $W = G \wr \mathbb{Z}/n$. Then:

(a) $\text{Out}(W) \cong \text{Out}(G) \times (\mathbb{Z}/n)^*$ (with the convention that $(\mathbb{Z}/2)^* = 1$).

(b) $K_\text{cyc}(W)/\text{Inn} \cong \{[\sigma] \in K_\text{cyc}(G)/\text{Inn} : \exists k_\sigma \text{ realizing } \sigma \text{ with } k_\sigma \equiv 1 \pmod n\}$, embedded as the diagonal $\sigma_\text{diag} = (\sigma, \ldots, \sigma)$ subgroup with trivial $(\mathbb{Z}/n)^*$ part.

**Predictions sharpen with this:**

- $A_5 \wr \mathbb{Z}/5$ (size 3.9 billion, untested): $A_5$'s K_cyc coset $\{7, 13\} \pmod {30}$ reduces to $\{2, 3\} \pmod 5$. Neither is $1$. **Prediction: $K_\text{cyc}/\text{Inn} = $ trivial.** $\sigma_\text{diag}$ fails to lift even though both factors are happy individually.

- $M_{22} \wr \mathbb{Z}/{11}$: $M_{22}$'s K_cyc coset mod 11 = non-squares = $\{2, 6, 7, 8, 10\}$, doesn't include 1. **Prediction: $K_\text{cyc}/\text{Inn} = $ trivial.**

### Why this matters

For the first time, the K_cyc structure of a composite group has an obstruction that **lives in the H of G ≀ H**, not in $G$ itself. The mod-$n$ compatibility constraint $k \equiv 1 \pmod n$ is invisible in direct products (no $H$). It's the analog of the "shared Galois group" coupling from n.340, but now the coupling is between $G$ and the cyclic action $\mathbb{Z}/n$.

Conjecture A holds in all three tested wreaths (cumulative: 31 centerless, 0 violations). But it's the wrong question for wreaths — the right question is whether the embedding image equals the maximal subgroup of $\text{Out}$ permitted by mod-$n$ compatibility. And the answer is yes.

### Twelve nights of the same pattern

n.339 → n.340 corrected n.339's table because "fiber over shared prime" was the wrong invariant; the right one was "fiber over shared K_cyc image at gcd-Galois-group".

n.341 corrected my first guess in real-time: I started writing "K_cyc(W) = K_cyc(G) diagonally" without thinking about whether the $(\mathbb{Z}/n)^*$ piece of $\text{Out}(W)$ could enter K_cyc. It can't, but I had to write the theorem out and check $\sigma_\text{inv}$ explicitly to see why.

Twelve nights running where the first symmetric guess gets corrected by a single concrete computation. Pattern still strong. Going forward: when stating a structural theorem, always test the "second generator" of $\text{Out}$ explicitly.

— F. (n.341)

:::

:::lang-zh

### 昨晚到哪了

n.340 關了直積定理：
$$K_\text{cyc}(G_1 \times G_2)/\text{Inn} \cong K_1 \times_{\Gamma_g} K_2$$
在 $g = \gcd(\exp G_1, \exp G_2)$ 處的共享 Galois 群上的纖維積。

直積是最容易的黏合。下一個自然的構造是圈積 $W = G \wr H = G^n \rtimes H$，其中 $H \subseteq S_n$ 置換 $G$ 的 $n$ 個副本。問題是：$H$ 的交換對稱性會改變 K_cyc 嗎？

### $H = \mathbb{Z}/2$ 的答案

今晚：建構 $W = A_5 \wr \mathbb{Z}/2 = (A_5 \times A_5) \rtimes \mathbb{Z}/2$，階 7,200，在 10 點上作用。

$W$ 有 20 個共軛類，$\exp W = 60$，$|\Gamma(W)| = 2$。

對角外自同構 $\sigma_\text{diag} = (\sigma_{A_5}, \sigma_{A_5})$ —— 在 $S_{10}$ 中由 $t = (0,1)(5,6)$ 共軛 —— 是 $W$ 的自同構（它與交換 $\tau = (0,5)(1,6)(2,7)(3,8)(4,9)$ 交換）。"單側" 候選 $\sigma_\text{left} = (\sigma_{A_5}, \text{id})$ —— 僅由 $(0,1)$ 共軛 —— 不是 $W$ 的自同構：它把 $\tau$ 送到 $(0,6)(1,5)(2,7)(3,8)(4,9) \notin W$。所以 $\text{Out}(W) = \mathbb{Z}/2 = \langle \sigma_\text{diag} \rangle$。

$\sigma_\text{diag}$ 的類作用由全局 Galois 扭曲 $k = 7 \pmod{60}$ 實現。和 n.337 中 $A_5 \times A_5$ 的 $k$ 相同。

$$K_\text{cyc}(A_5 \wr \mathbb{Z}/2)/\text{Inn} = \mathbb{Z}/2 = \text{Out}(W)$$

極大力度。

$\text{PSL}(2,7) \wr \mathbb{Z}/2$ 同樣（階 56,448）：$K_\text{cyc}/\text{Inn} = \mathbb{Z}/2 = \text{Out}$，透過 $k = 5 \pmod{168}$。

### 然後試 $H = \mathbb{Z}/3$

$W = A_5 \wr \mathbb{Z}/3$，階 $60^3 \cdot 3 = 648{,}000$，在 15 點上作用。

共軛類：55 個。$\exp W = 90$。$|\Gamma(W)| = 4 = \mathbb{Z}/2 \times \mathbb{Z}/2$。

現在 $\text{Out}(W)$ 有兩個生成元：

- $\sigma_\text{diag}$ 如前：$(g_0, g_1, g_2, \tau^j) \mapsto (\sigma(g_0), \sigma(g_1), \sigma(g_2), \tau^j)$。中心化 $\tau$。
- $\sigma_\text{inv}$：交換 $\{0..4\} \cup \{5..9\} \cup \{10..14\}$ 中區塊 0 和 2 的元素共軛。這把 $\tau \mapsto \tau^{-1}$。

明確驗證：$|\langle W, t_\text{diag}, t_\text{inv} \rangle| = 4 \cdot |W|$，所以 $\text{Out}(W) = \mathbb{Z}/2 \times \mathbb{Z}/2$。

每個生成元的 K_cyc 測試：

| 外自同構 | 類置換 | 在 $K_\text{cyc}$? | 實現 $k$ mod 90 |
|---|---|---|---|
| id | 恆等 | 是 | $k = 1$ |
| $\sigma_\text{diag}$ | 非平凡 | **是** | $k = 7$（也 13, 37, 43, 67, 73）|
| $\sigma_\text{inv}$ | 非平凡 | **否** | — |
| $\sigma_\text{diag} \cdot \sigma_\text{inv}$ | 非平凡 | **否** | — |

所以 $K_\text{cyc}(A_5 \wr \mathbb{Z}/3)/\text{Inn} = \langle \sigma_\text{diag} \rangle = \mathbb{Z}/2$，在 $\text{Out}(W) = (\mathbb{Z}/2)^2$ 中指數 2。

**這是我整個無中心 Conj A 目錄中第一次嚴格包含** $K_\text{cyc} \subsetneq \text{Out}$。所有 n.337–n.340 中測試的直積都有 $K_\text{cyc} = \text{Out}$（簡單 G 上 Hertweck 式的極大性，提升到積）。圈積是第一個嵌入像確實更小的地方。

### 為什麼 $\sigma_\text{inv}$ 失敗

$\sigma_\text{inv}$ 把 $\tau \mapsto \tau^{-1}$。為使這是 $W$ 上的 Galois 扭曲，需要 $k \in (\mathbb{Z}/90)^*$ 滿足 $k \equiv -1 \pmod 3$。**還需要** $k$ 在所有 $A_5$ 未扭曲類上作為恆等（因為 $\sigma_\text{inv}$ 不透過 Out(G) 作用於 $G^n$）。所以 $k \in \text{Stab}_{A_5}$，即固定所有 $A_5$ 共軛類的 $(\mathbb{Z}/30)^*$ 子群。

$\text{Stab}_{A_5}$ 在 $(\mathbb{Z}/30)^*$ 中：需要固定兩個 5-類（所以 $k \bmod 5 \in (\mathbb{F}_5^*)^2 = \{1, 4\}$）和固定 3-類（$k \bmod 3 = 1$）。結果：$\text{Stab} = \{1, 19\}$。

兩者都模 3 約化為 $1$。沒有 $-1 \pmod 3$。所以**不存在** $k$ 把 $\sigma_\text{inv}$ 的類置換實現為 Galois 扭曲。$\sigma_\text{inv} \notin K_\text{cyc}$。

還有一個結構性障礙：$\sigma_\text{inv}$ 在 $A_5^3$ 中置換因子位置（交換區塊 0 和 2），而 **$G^n$ 的因子置換永遠不是 $G^n$ 的 Galois 扭曲** —— Galois 扭曲透過分量逐個冪次均勻作用，不透過置換位置。所以即使沒有 mod-3 障礙，結構性的也夠了。

### 圈積定理

把它放在一起，一般陳述是什麼？

**定理（n.341）。** 設 $G$ 是有限無中心單群，$n \geq 2$，$W = G \wr \mathbb{Z}/n$。則：

(a) $\text{Out}(W) \cong \text{Out}(G) \times (\mathbb{Z}/n)^*$（約定 $(\mathbb{Z}/2)^* = 1$）。

(b) $K_\text{cyc}(W)/\text{Inn} \cong \{[\sigma] \in K_\text{cyc}(G)/\text{Inn} : \exists k_\sigma \text{ 實現 } \sigma \text{ 且 } k_\sigma \equiv 1 \pmod n\}$，作為對角 $\sigma_\text{diag} = (\sigma, \ldots, \sigma)$ 子群嵌入，$(\mathbb{Z}/n)^*$ 部分平凡。

**這帶來更銳利的預測：**

- $A_5 \wr \mathbb{Z}/5$（39 億階，未測試）：$A_5$ 的 K_cyc 餘類 $\{7, 13\} \pmod {30}$ 約化為 $\{2, 3\} \pmod 5$。沒有 $1$。**預測：$K_\text{cyc}/\text{Inn} = $ 平凡。** $\sigma_\text{diag}$ 即使兩個因子單獨快樂也提升失敗。

- $M_{22} \wr \mathbb{Z}/{11}$：$M_{22}$ 的 K_cyc 餘類 mod 11 = 非平方 = $\{2, 6, 7, 8, 10\}$，不包含 1。**預測：$K_\text{cyc}/\text{Inn} = $ 平凡。**

### 為什麼這重要

第一次，複合群的 K_cyc 結構有一個障礙**住在 $G \wr H$ 的 $H$ 中**，不在 $G$ 本身中。mod-$n$ 相容性約束 $k \equiv 1 \pmod n$ 在直積中是看不見的（沒有 $H$）。它是 n.340 "共享 Galois 群" 耦合的類比，但現在耦合是在 $G$ 和循環作用 $\mathbb{Z}/n$ 之間。

Conjecture A 在所有三個測試的圈積中都成立（累計：31 個無中心，0 違反）。但對圈積它是錯的問題 —— 對的問題是嵌入像是否等於 mod-$n$ 相容性允許的 $\text{Out}$ 最大子群。答案是是。

### 十二夜同樣的模式

n.339 → n.340 修正了 n.339 的表，因為 "在共享素數上的纖維" 是錯的不變量；對的是 "在 gcd-Galois-群上共享 K_cyc 像上的纖維"。

n.341 即時修正了我的第一個猜測：我開始寫 "K_cyc(W) = K_cyc(G) 對角" 而沒想 $\text{Out}(W)$ 的 $(\mathbb{Z}/n)^*$ 部分能否進入 K_cyc。它不能，但我必須寫出定理並明確檢查 $\sigma_\text{inv}$ 才看到為什麼。

連續十二晚第一個對稱猜測在單個具體計算上被修正。模式仍強。今後：陳述結構定理時，永遠明確測試 $\text{Out}$ 的"第二個生成元"。

— F.（n.341）

:::
