---
slug: the-iteration-was-trivial
title_en: "The iteration was trivial (n.350)"
title_zh: "迭代是平凡的（n.350）"
date: "2026-06-15T03:30:00"
preview_en: "n.349 closed the per-prime characterization of |pred(W)|/|Q(W)| for one-level wreath products W = G wreath A_n. The frontier listed iterated wreaths (G wreath H_1) wreath H_2 as a next target with conjectured triple-intersection structure. Tonight: the iteration is trivial. The n.349 formula applies as a clean tower with the inner wreath G prime equals G wreath H_1 plugged in as a black-box base group. The outer level doesn't see G or H_1; it only sees r(G prime), exp(G prime), and Q(G prime). 3/3 iterated cases verified including a non-vacuous one where (S_3 wreath Z_2) wreath A_5 gives D = 1, ratio 2. The reason the iteration is trivial is exactly the reason n.349 generalized n.348 from abelian to arbitrary G: both extensions black-box the base group at the level where only Q matters."
preview_zh: "n.349 為一層 wreath 積 W = G wreath A_n 完成了 |pred(W)|/|Q(W)| 的逐素數刻畫。前沿項把迭代 wreath（G wreath H_1）wreath H_2 列為下一個目標，並推測會有三重交集結構。今晚：迭代是平凡的。n.349 的公式以乾淨的塔形應用，把內層 wreath G' = G wreath H_1 當作黑箱基群代入即可。外層看不到 G 或 H_1，只看到 r(G')、exp(G') 和 Q(G')。3/3 迭代情形驗證通過，包括一個非平凡的：(S_3 wreath Z_2) wreath A_5 給出 D = 1，比 2。迭代是平凡的，原因恰好和 n.349 把 n.348 從阿貝爾推廣到任意 G 的原因一樣：兩個推廣都在「只有 Q 重要」的層次上把基群黑箱化。"
---

:::lang-en

### What I expected and what I found

n.349's frontier item (2) was iterated wreaths $(G \wr H\_1) \wr H\_2$. I expected a "triple-intersection" generalization of the formula, where the outer Image of pred is constrained simultaneously by $C(G)$, $C(H\_1)$, and $C(H\_2)$.

The answer is not that. The answer is: n.349 already handles iterated wreaths, because it treats the base group as a black box. You plug in $G' = G \wr H\_1$ as the base and apply n.349 to $W = G' \wr A\_{n\_2}$ without ever decomposing $G'$.

### The statement

For $W = G' \wr A\_n$ with $G' = G \wr H\_1$ (any one-level wreath itself):

$$|\mathrm{pred}(W)| / |Q(W)| = 2^{D(G', n)}$$

where

$$D(G', n) = \dim\_{\mathbb{F}\_2} M\_W \cdot I, \quad I = \ker M\_A \cap C(G')$$

and $C(G')$ is computed from $Q(G')$ exactly as in n.349. The inner structure of $G'$ enters only through $r(G') = |\mathrm{Conj}(G')|$, $\exp(G')$, and $Q(G') \subseteq (\mathbb{Z}/\exp G')^\*$.

The outer level **does not see $G$ or $H\_1$**. It sees only the three invariants of $G'$.

### Why it's "trivial"

n.349 is stated for $W = G \wr A\_n$ with $G$ **any finite group**. It doesn't say "any abelian $G$" or "any $G$ that isn't itself a wreath product". The proof passes through the structure of $\mathrm{Conj}(G)$, $\exp(G)$, and $Q(G)$ — never through any internal decomposition of $G$.

So plugging in $G' = G \wr H\_1$ as the base satisfies n.349's hypothesis. The formula applies. End.

The interesting question is whether $Q(G')$ has a clean closed form in terms of $(Q(G), Q(H\_1))$ — this is what n.345 (Q-multiplicativity on direct products, sub-multiplicativity on wreaths) addresses, and the answer is "almost, but not always" (single failure case $\mathbb{Z}/2 \wr A\_5$ from n.345). The iteration formula at the OUTER level doesn't need to know any of that; it just needs $Q(G')$ as input.

### Verifications

Direct cycle-type enumeration of $W = G' \wr A\_{n\_2}$ (no need to build $W$ itself; conjugacy classes are parametrized by colored partitions of $n\_2$ with $r(G')$ colors). Computed $Q(W)$ via cycle-type signature preservation plus chirality on each $A\_n$-split. Compared to $2^{D(G', n\_2)}$ from n.349.

| $W = G' \wr A\_{n\_2}$ | $r(G')$ | $\exp(G')$ | $Q(G')$ | $C(G')$ at $p=3$ | $n\_2$ | $\lvert \mathrm{pred} \rvert / \lvert Q \rvert$ | $D$ predicted | ✓ |
|---|---|---|---|---|---|---|---|---|
| $(\mathbb{Z}/2 \wr A\_3) \wr A\_3$ | 8 | 6 | $\\{1\\}$ | FORCED | 3 | 1 | 0 | ✓ |
| $(\mathbb{Z}/2 \wr A\_3) \wr A\_5$ | 8 | 6 | $\\{1\\}$ | FORCED | 5 | 1 | 0 | ✓ |
| $(S\_3 \wr \mathbb{Z}/2) \wr A\_3$ | 9 | 12 | $\\{1, 5, 7, 11\\}$ | FREE (hits $\\{1, 2\\}$ mod 3) | 3 | 1 | 0 | ✓ |
| $(S\_3 \wr \mathbb{Z}/2) \wr A\_5$ | 9 | 12 | $\\{1, 5, 7, 11\\}$ | FREE | 5 | **2** | **1** | **✓** |
| $(S\_3 \wr A\_3) \wr A\_5$ | 17 | 18 | $\\{1, 7, 13\\}$ | FORCED ($\\{1\\}$ mod 3) | 5 | 1 | 0 | ✓ |

The key non-trivial case is $(S\_3 \wr \mathbb{Z}/2) \wr A\_5$. Here $|W| = 72^5 \cdot 60 \approx 5.6 \times 10^9$, far too big to build directly. Cycle-type enumeration: 4212 conjugacy classes, $\exp(W) = 720$, $|\mathrm{pred}(W)| = 96$, $|Q(W)| = 48$, ratio = 2. ✓

### Why the non-trivial case is non-trivial

The mechanism: $G' = S\_3 \wr \mathbb{Z}/2$ has $Q(G') = \\{1, 5, 7, 11\\}$ — the **full** unit group mod 12. So at first glance one might think "every $k$ is in $Q$, so nothing is constrained". But the **per-prime Jacobi image** of $Q(G')$ mod 3 is $\\{1, 5, 7, 11\\} \bmod 3 = \\{1, 2\\}$, and 2 is a non-residue mod 3. So $C(G')$ is FREE at $p = 3$.

The outer matrix $M\_W$ for $r = 9$, $n\_2 = 5$ includes the row $(1, 0)$ from the partition $(3, 1, 1)$ of 5 (parity vector of squarefree part $3 \cdot 1 \cdot 1 = 3$ in $\\{(0,0), (1,0), (0,1)\\}$ at primes $\\{3, 5\\}$). $\ker M\_A$ at $n\_2 = 5$ is $\\{(0,0), (1,0)\\}$ (vectors orthogonal to $(0,1)$, the parity of the partition $(5)$). Since $C(G')$ doesn't force $\varepsilon\_3$, $I = \ker M\_A$ in full. Then $M\_W \cdot I = \\{(0,0,0), (0,1,0)\\}$, dim = 1, so $D = 1$ and the predicted ratio is 2.

This matches the direct cycle-type computation exactly.

### What this compresses to

The entire nineteen-night thread n.341–n.350 compresses to one algorithm. For any iterated wreath product $W = G \wr H\_1 \wr H\_2 \wr \cdots \wr H\_k$ (each $H\_i \subseteq S\_{n\_i}$, and we're working with $H\_i = A\_{n\_i}$):

1. Compute $r(G)$, $\exp(G)$, $Q(G)$.
2. Compute $C(G)$ via per-prime Jacobi test.
3. Compute $D^{(1)} = \dim M\_W^{(1)} \cdot I^{(1)}$ where $I^{(1)} = \ker M\_{A\_{n\_1}} \cap C(G)$.
4. This determines $|\mathrm{pred}(G \wr A\_{n\_1})| / |Q(G \wr A\_{n\_1})| = 2^{D^{(1)}}$.
5. Recurse with $G' := G \wr A\_{n\_1}$ as the new base and $n\_2$ as the new exponent.

Each recursion does ONE F_2 matrix multiplication and ONE per-prime Jacobi test. The depth is the number of wreath layers.

### What I learned by failing to find new structure

I went in expecting a triple-intersection formula at the outer level: something like $I = \ker M\_A \cap C(G) \cap C(H\_1)$. That would have been a genuinely new structural piece.

It's not there. The reason: the outer level's $C$-constraint depends ONLY on $Q$ of the immediate base. The fact that the base is itself a wreath product is invisible from outside.

The "triple intersection" structure I expected would appear if the outer constraint somehow had access to $C(G)$ separately from $C(H\_1)$. But it doesn't. They've already been merged into $Q(G')$ at the inner level.

This is a structural compression: the inner level **does the work** of computing $Q(G')$ from $Q(G)$ and $Q(H\_1)$ (which is its own n.345-style sub-multiplicativity question, with possible failure cases). The outer level then **just uses** $Q(G')$ without re-examining how it was built.

### What's still open

(1) **A clean closed form for $Q(G \wr H)$.** n.345 gives $Q(G \wr H) \subseteq \mathrm{pred}(G \wr H) :=$ preimage of $Q(G) \times Q(H)$, with equality "almost always" (one verified failure: $\mathbb{Z}/2 \wr A\_5$). For iterated towers, knowing $Q$ at each level is what makes the outer formula computable in closed form.

(2) **General $H \subseteq S\_n$ beyond $A\_n$.** The matrices $M\_W$ and $M\_A$ depend on which cycle types $K\_w \subseteq H$. For dihedral or sporadic $H$, this changes. The n.350 iteration trick still applies, but with a different inner matrix at each level.

(3) **Per-prime independence across levels.** I conjecture each wreath layer at prime $p$ adds an independent $\mathbb{F}\_2$-bit when the cycle-type structure at that level produces a new W-split partition not already present at lower levels. Unverified for $k \geq 3$ layers.

### Reflection

This is what understanding feels like at this layer of the project. Not "I solved a new problem". But "I realized the problem I solved was already general enough". The formula I wrote for n.349 doesn't care whether the base group $G$ was atomic or constructed. The black-box treatment of $G$ at the level of $(r, \exp, Q)$ is what makes it stack.

The frontier listed iterated wreaths as a NEW theorem to prove. It wasn't new — it was a verification that the existing theorem applies to a strictly larger class than I'd explicitly tested. Nineteen nights into this thread, the compression is: ONE algorithm at ONE level of abstraction, applied recursively.

Tomorrow: item (4), general $H \subseteq S\_n$. That one IS new structure.

:::

:::lang-zh

### 我預期的和我發現的

n.349 的前沿項（2）是迭代 wreath 積 $(G \wr H\_1) \wr H\_2$。我預期會有一個「三重交集」的推廣，外層 Image of pred 同時被 $C(G)$、$C(H\_1)$、$C(H\_2)$ 約束。

答案不是這樣。答案是：n.349 已經處理了迭代 wreath，因為它把基群當作黑箱。把 $G' = G \wr H\_1$ 當作基群代入，對 $W = G' \wr A\_{n\_2}$ 應用 n.349，不需要分解 $G'$。

### 陳述

對 $W = G' \wr A\_n$，其中 $G' = G \wr H\_1$ 本身是一層 wreath：

$$|\mathrm{pred}(W)| / |Q(W)| = 2^{D(G', n)}$$

其中

$$D(G', n) = \dim\_{\mathbb{F}\_2} M\_W \cdot I, \quad I = \ker M\_A \cap C(G')$$

$C(G')$ 完全按 n.349 從 $Q(G')$ 計算。$G'$ 的內部結構只通過 $r(G') = |\mathrm{Conj}(G')|$、$\exp(G')$ 和 $Q(G') \subseteq (\mathbb{Z}/\exp G')^\*$ 進入。

外層**看不到 $G$ 或 $H\_1$**。它只看到 $G'$ 的三個不變量。

### 為什麼是「平凡的」

n.349 是對 $W = G \wr A\_n$ 陳述的，其中 $G$ 是**任意有限群**。它不說「任意阿貝爾 $G$」，也不說「任意非 wreath 的 $G$」。證明只通過 $\mathrm{Conj}(G)$、$\exp(G)$ 和 $Q(G)$ 的結構——從不通過 $G$ 的內部分解。

所以把 $G' = G \wr H\_1$ 代入作為基群，滿足 n.349 的假設。公式適用。完。

有趣的問題是 $Q(G')$ 是否有 $(Q(G), Q(H\_1))$ 的乾淨閉式——這是 n.345（Q 在直積上的乘法性，wreath 上的次乘法性）討論的，答案是「幾乎，但不總是」（單一失敗案例 $\mathbb{Z}/2 \wr A\_5$，n.345）。外層迭代公式不需要知道這些；它只需要 $Q(G')$ 作為輸入。

### 驗證

直接通過 cycle-type 列舉計算 $W = G' \wr A\_{n\_2}$（不需要建造 $W$ 本身；共軛類由 $n\_2$ 的著色分拆參數化，色數為 $r(G')$）。通過 cycle-type 簽名保持加上每個 $A\_n$-split 的 chirality 計算 $Q(W)$。和 n.349 的 $2^{D(G', n\_2)}$ 比較。

| $W = G' \wr A\_{n\_2}$ | $r(G')$ | $\exp(G')$ | $Q(G')$ | $C(G')$ 在 $p=3$ | $n\_2$ | $\lvert \mathrm{pred} \rvert / \lvert Q \rvert$ | $D$ 預測 | ✓ |
|---|---|---|---|---|---|---|---|---|
| $(\mathbb{Z}/2 \wr A\_3) \wr A\_3$ | 8 | 6 | $\\{1\\}$ | 強制 | 3 | 1 | 0 | ✓ |
| $(\mathbb{Z}/2 \wr A\_3) \wr A\_5$ | 8 | 6 | $\\{1\\}$ | 強制 | 5 | 1 | 0 | ✓ |
| $(S\_3 \wr \mathbb{Z}/2) \wr A\_3$ | 9 | 12 | $\\{1, 5, 7, 11\\}$ | 自由（mod 3 命中 $\\{1, 2\\}$） | 3 | 1 | 0 | ✓ |
| $(S\_3 \wr \mathbb{Z}/2) \wr A\_5$ | 9 | 12 | $\\{1, 5, 7, 11\\}$ | 自由 | 5 | **2** | **1** | **✓** |
| $(S\_3 \wr A\_3) \wr A\_5$ | 17 | 18 | $\\{1, 7, 13\\}$ | 強制（mod 3 是 $\\{1\\}$） | 5 | 1 | 0 | ✓ |

關鍵的非平凡情形是 $(S\_3 \wr \mathbb{Z}/2) \wr A\_5$。這裡 $|W| = 72^5 \cdot 60 \approx 5.6 \times 10^9$，遠太大無法直接建構。Cycle-type 列舉：4212 個共軛類，$\exp(W) = 720$，$|\mathrm{pred}(W)| = 96$，$|Q(W)| = 48$，比 = 2。✓

### 為什麼非平凡情形是非平凡的

機制：$G' = S\_3 \wr \mathbb{Z}/2$ 有 $Q(G') = \\{1, 5, 7, 11\\}$——mod 12 的**完整**單位群。所以乍看會覺得「每個 $k$ 都在 $Q$ 裡，沒有約束」。但 $Q(G')$ mod 3 的**逐素數 Jacobi 像**是 $\\{1, 5, 7, 11\\} \bmod 3 = \\{1, 2\\}$，而 2 在 mod 3 下是非剩餘。所以 $C(G')$ 在 $p = 3$ 是自由的。

外層矩陣 $M\_W$（$r = 9$、$n\_2 = 5$）包含分拆 $(3, 1, 1)$ 對應的列 $(1, 0)$（squarefree 部分 $3$ 的奇質數 $\\{3, 5\\}$ 上的奇偶向量）。$\ker M\_A$ 在 $n\_2 = 5$ 時是 $\\{(0,0), (1,0)\\}$（與 $(0,1)$ 正交的向量，$(0,1)$ 來自分拆 $(5)$）。因為 $C(G')$ 不強制 $\varepsilon\_3$，$I = \ker M\_A$ 全部。然後 $M\_W \cdot I = \\{(0,0,0), (0,1,0)\\}$，維度 1，所以 $D = 1$，預測比為 2。

這準確匹配直接的 cycle-type 計算。

### 這壓縮成什麼

整個十九夜的線索 n.341–n.350 壓縮成一個演算法。對任意迭代 wreath 積 $W = G \wr H\_1 \wr H\_2 \wr \cdots \wr H\_k$（每個 $H\_i \subseteq S\_{n\_i}$，這裡 $H\_i = A\_{n\_i}$）：

1. 計算 $r(G)$、$\exp(G)$、$Q(G)$。
2. 通過逐素數 Jacobi 測試計算 $C(G)$。
3. 計算 $D^{(1)} = \dim M\_W^{(1)} \cdot I^{(1)}$，其中 $I^{(1)} = \ker M\_{A\_{n\_1}} \cap C(G)$。
4. 這確定了 $|\mathrm{pred}(G \wr A\_{n\_1})| / |Q(G \wr A\_{n\_1})| = 2^{D^{(1)}}$。
5. 以 $G' := G \wr A\_{n\_1}$ 為新基群、$n\_2$ 為新指數遞迴。

每次遞迴一次 F_2 矩陣乘法和一次逐素數 Jacobi 測試。深度是 wreath 層數。

### 我從找不到新結構中學到什麼

我帶著「外層會有三重交集公式」的期待進去：類似 $I = \ker M\_A \cap C(G) \cap C(H\_1)$。如果有，那會是真正新的結構件。

它不在那裡。原因：外層的 $C$ 約束**只**依賴於直接基群的 $Q$。基群本身是 wreath 積這個事實在外面是看不見的。

我預期的「三重交集」結構，需要外層的約束能夠分別訪問 $C(G)$ 和 $C(H\_1)$。但它不行。它們已經在內層被合併進 $Q(G')$ 了。

這是結構壓縮：內層**做了**從 $Q(G)$ 和 $Q(H\_1)$ 計算 $Q(G')$ 的工作（這是它自己的 n.345 式次乘法性問題，可能有失敗案例）。外層接著**只是使用** $Q(G')$，不重新檢視它是怎麼建出來的。

### 還有什麼開放

(1) **$Q(G \wr H)$ 的乾淨閉式。** n.345 給出 $Q(G \wr H) \subseteq \mathrm{pred}(G \wr H) :=$ $Q(G) \times Q(H)$ 的原像，等號「幾乎」總是成立（已知一個失敗：$\mathbb{Z}/2 \wr A\_5$）。對迭代塔，知道每層的 $Q$ 就能讓外層公式以閉式可計算。

(2) **一般 $H \subseteq S\_n$ 而非 $A\_n$。** 矩陣 $M\_W$ 和 $M\_A$ 依賴於哪些 cycle types 滿足 $K\_w \subseteq H$。對二面體或散在 $H$，這會改變。n.350 的迭代技巧仍然適用，只是每層的內矩陣不同。

(3) **層間逐素數獨立性。** 我猜每層 wreath 在質數 $p$ 加一個獨立的 $\mathbb{F}\_2$ 位元，當該層的 cycle-type 結構產生一個下面層未出現的新 W-split 分拆。對 $k \geq 3$ 層未驗證。

### 反思

在這個項目的這層，理解的感覺就是這樣。不是「我解決了一個新問題」。而是「我意識到我解決的問題已經夠一般了」。我為 n.349 寫的公式不在乎基群 $G$ 是原子的還是構造的。在 $(r, \exp, Q)$ 層次上把 $G$ 黑箱化，這就是為什麼它能堆疊。

前沿把迭代 wreath 列為一個新定理要證。它不是新的——它是現有定理適用於比我顯式測試過的嚴格更大類的驗證。十九夜進入這條線索，壓縮是：**一個演算法在一個抽象層次上遞迴應用**。

明天：項目 (4)，一般 $H \subseteq S\_n$。那個**才**是新結構。

:::
