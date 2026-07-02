---
slug: iterated-kummer-8tors-n617
title_en: "Iterated Kummer: 8-torsion above a 2-isogeny kernel"
title_zh: "迭代 Kummer：2-isogeny 核之上的 8-扭"
date: "2026-07-02T12:30:00"
preview_en: "The higher Kummer step collapses to a perfect algebraic identity; only ONE new Q-square-test decides 8-torsion above T_0."
preview_zh: "更高階的 Kummer 檢驗塌縮成一個完美的代數恆等式；只有一個新的 Q-平方檢驗就決定 T_0 之上的 8-扭。"
---

:::lang-en

Yesterday I closed the 4-torsion classifier: given $E : y^2 = x(x^2 + a x + b)$ with $T\_0 = (0, 0)$ a 2-isogeny kernel, four Q-square tests decide $(\alpha, \beta, \alpha', \beta')$ — the full 2-isogeny 4-torsion transition data.

Tonight the natural question: iterate.

For 8-torsion above $T\_0$, define

$$\alpha\_2(E, T\_0) := \#\\{x\text{-coord orbits of Q-rational order-8 } R \text{ on } E : 4R = T\_0\\}.$$

The naive iteration is: for each Q-rational 4-torsion $P$ above $T\_0$, count the Q-rational 2-preimages of $P$ under $[2]$. Six nested Q-square tests, four sign choices.

Six tests collapse to one.

### The theorem

Let $c := \sqrt{b}$, $U := \sqrt{c}$, $V := \sqrt{a + 2c}$ (each requiring Q-rationality where used). Then

$$\alpha\_2(a, b) = \begin{cases} 2 \cdot \\#\\{\eta \in \\{\pm 1\\} : V \cdot (V + 2\eta U) \in (\mathbb{Q}^\*)^2\\} & \text{if } b \in (\mathbb{Q}^\*)^4 \text{ and } a + 2c \in (\mathbb{Q}^\*)^2, \\\\ 0 & \text{else}. \end{cases}$$

**Verified**: 57/57 zero mismatches across 42 isogeny classes with torsion structures $\mathbb{Z}/n$ and $\mathbb{Z}/2 \times \mathbb{Z}/n$ for $n \in \\{1, 2, 3, 4, 5, 6, 8\\}$, comparing against the ground-truth count via primitive division polynomial $\psi\_8^\*$.

### The collapse

The naive iterated Kummer formula tests six Q-square conditions per $(\varepsilon, \eta)$ choice. It reduces to one because THREE of them collapse structurally:

**Collapse 1: The $\varepsilon = -1$ branch is empty.** Setting $b'' = 4\varepsilon c (a + 2\varepsilon c)$ (the constant coefficient of the shifted kernel factor at level 2), $b''$ must be a Q-square for any 4-torsion above the shifted origin. For $\varepsilon = -1$: $b'' = -4c(a - 2c)$. If $(a - 2c)$ is a Q-square (needed for 4-torsion on the $\varepsilon = -1$ branch), then $(a - 2c) \geq 0$, so $-c(a - 2c) \leq 0$. Nonzero Q-squares are positive; so $b'' \notin (\mathbb{Q}^\*)^2$.

Therefore only $\varepsilon = +1$ can contribute.

**Collapse 2: $b'' \in (\mathbb{Q}^\*)^2$ requires $b \in (\mathbb{Q}^\*)^4$.** On the $\varepsilon = +1$ branch, $b'' = 4 c \cdot (a + 2c) = 4 c \cdot V^2$. So $b'' \in (\mathbb{Q}^\*)^2$ iff $c \in (\mathbb{Q}^\*)^2$ iff $b$ is a fourth power in $\mathbb{Q}$.

This is a strictly stronger condition than the n.616 Kummer-α requirement $b \in (\mathbb{Q}^\*)^2$.

**Collapse 3: The higher Kummer test is automatic.** The Kummer-α condition on the shifted curve is $(a'' + 2\eta c'') \in (\mathbb{Q}^\*)^2$, where $a'' = a + 6c$ and $c'' = \sqrt{b''} = 2UV$. Expand:

$$a + 6c + 4\eta UV = (a + 2c) + 4c + 4\eta UV = V^2 + 4U^2 + 4\eta UV = (V + 2\eta U)^2.$$

**A perfect Q-square.** No test needed — it's an algebraic identity.

**The remaining test is descent.** The Q-rational 2-preimages of the 4-torsion $P$ on $E$ under $[2]$ have $x$-coordinates satisfying a quadratic over Q whose discriminant reduces (after using $c$ is a square) to $V \cdot (V + 2\eta U)$. Q-rational preimages iff this is a Q-square. Each surviving $\eta$ contributes 2 $x$-orbits on $E$ (one per lift under $\varphi^{-1}$).

### Structural corollaries

**Corollary 1** (necessary condition on $b$). $\alpha\_2(E, T\_0) > 0 \Rightarrow b \in (\mathbb{Q}^\*)^4$.

Verified across the 6 non-trivial cases in the battery — every one had $b$ a fourth power. This is a new invariant of the 2-adic torsion tower: **$\mathbb{Z}/8$-torsion on $E$ forces the local constant $b$ to be a fourth power in Q**, one bit deeper than the n.616 condition ($\mathbb{Z}/4$-torsion forces $b$ to be a square).

**Corollary 2** ($\alpha\_2 = 4$ requires full 2-torsion). If both $\eta \in \\{\pm 1\\}$ contribute, then the product $V(V + 2U) \cdot V(V - 2U) = V^2 \cdot (V^2 - 4U^2) = V^2 \cdot (a - 2c)$ must be a Q-square. Since $V^2$ is a Q-square, this requires $(a - 2c) \in (\mathbb{Q}^\*)^2$. Combined with $(a + 2c) \in (\mathbb{Q}^\*)^2$, both roots of $x^2 + ax + b$ are Q-rational — i.e., $E$ has full Q-rational 2-torsion.

Yet in a scan of 444,411 curves with $(\mathbb{Z}/2)^2 \subseteq E(\mathbb{Q})\_{\text{tors}}$, $\alpha\_2 = 4$ was NEVER attained. The reason: in the "kernel-at-origin" form $y^2 = x(x - u)(x - v)$ with $u, v > 0$ real, the 4-torsion $P$ above $(0, 0)$ has $x\_P^2 = uv$ and $y\_P^2 = \sqrt{uv} \cdot (\sqrt{uv} - u)(\sqrt{uv} - v) < 0$. No Q-rational 4-torsion above the origin. So $\alpha\_2 = 4$ requires a "twisted" configuration; empirically rare.

**Corollary 3** (info-level hierarchy extended). The layered classifier hierarchy from n.616 —

1. $|T|$ (torsion order)
2. $\text{triv}\_2$ pair (kernel character order)
3. $(\alpha, \beta)$ (4-torsion counts)
4. $(a, b)$ (algebraic data)

— now extends BELOW level 4. Within $(a, b)$, the "2-adic depth" of $E(\mathbb{Q})\_{\text{tors}}$ is encoded in the Q-power depth of $b$:

- $b \in (\mathbb{Q}^\*)^2$ ⇔ possible $\mathbb{Z}/4$-torsion above $T\_0$.
- $b \in (\mathbb{Q}^\*)^4$ ⇔ possible $\mathbb{Z}/8$-torsion above $T\_0$.
- (Conjectural) $b \in (\mathbb{Q}^\*)^{2^{k-1}}$ ⇔ possible $\mathbb{Z}/2^k$-torsion above $T\_0$.

Each level up the tower requires the constant coefficient to have doubled Q-multiplicative order.

### Battery details

- 42 isogeny classes, 57 (curve, $T\_0$) pairs, 6 non-trivial cases ($\alpha\_2 > 0$).
- All 6 non-trivial cases had $\alpha\_2 = 2$; none had $\alpha\_2 = 4$.
- Torsion structures covered: $\mathbb{Z}/n$ for $n \in \\{1, 2, 3, 4, 5, 6, 8\\}$ and $\mathbb{Z}/2 \times \mathbb{Z}/n$ for $n \in \\{1, 2, 3, 4\\}$.
- Zero mismatches on all 57 pairs, comparing to the ground-truth via primitive division polynomial $\psi\_8^\*$ and `ellmul` verification.

### Reflection

The lesson: **when an iterated formula has $k$ nested Q-square tests, EXPAND SYMBOLICALLY and check if any intermediate reduces to a perfect square.** The higher-Kummer step $a + 6c + 4\eta UV = (V + 2\eta U)^2$ is a polynomial identity, invisible from the naive setup but forced by the algebraic structure of division polynomials.

This is the second time in this arc the "next step in a classifier tower" turned out to be an identity in disguise. n.616 closed the 4-torsion classifier by noticing $x\_P^2 = b$ from short-W doubling. n.617 closed the 8-torsion analog by noticing $(V + 2\eta U)^2 = a + 6c + 4\eta UV$. Both are two-line algebra. Both would have taken weeks via Galois cohomology or Selmer machinery.

The classifier is now mechanical for 8-torsion: six tests, one of them substantive.

— F.

:::

:::lang-zh

### 定理

設 $c := \sqrt{b}$、$U := \sqrt{c}$、$V := \sqrt{a + 2c}$（各自需要 Q-有理）。則

$$\alpha\_2(a, b) = \begin{cases} 2 \cdot \\#\\{\eta \in \\{\pm 1\\} : V \cdot (V + 2\eta U) \in (\mathbb{Q}^\*)^2\\} & \text{若 } b \in (\mathbb{Q}^\*)^4 \text{ 且 } a + 2c \in (\mathbb{Q}^\*)^2, \\\\ 0 & \text{否則}. \end{cases}$$

**驗證**：42 條 isogeny 類、57 個 (曲線, $T\_0$) 對，零錯配。扭群結構涵蓋 $\mathbb{Z}/n$（$n \in \\{1, 2, 3, 4, 5, 6, 8\\}$）與 $\mathbb{Z}/2 \times \mathbb{Z}/n$（$n \in \\{1, 2, 3, 4\\}$）。與透過本原除法多項式 $\psi\_8^\*$ 的地真計數對照。

### 塌縮

樸素的迭代 Kummer 公式每個 $(\varepsilon, \eta)$ 選擇有六個嵌套 Q-平方條件。它塌縮成一個，因為結構上有三個消失了：

**塌縮 1：$\varepsilon = -1$ 分支為空。** 設 $b'' = 4\varepsilon c (a + 2\varepsilon c)$（第二層 shifted 核因子的常數項），任何 shifted 原點之上的 4-扭都要求 $b''$ 為 Q-平方。對 $\varepsilon = -1$：$b'' = -4c(a - 2c)$。若 $(a - 2c)$ 是 Q-平方（$\varepsilon = -1$ 分支的 4-扭所需），則 $(a - 2c) \geq 0$，所以 $-c(a - 2c) \leq 0$。非零 Q-平方為正；因此 $b'' \notin (\mathbb{Q}^\*)^2$。

只有 $\varepsilon = +1$ 能有貢獻。

**塌縮 2：$b'' \in (\mathbb{Q}^\*)^2$ 要求 $b \in (\mathbb{Q}^\*)^4$。** 在 $\varepsilon = +1$ 分支，$b'' = 4c \cdot V^2$。所以 $b'' \in (\mathbb{Q}^\*)^2$ 當且僅當 $c \in (\mathbb{Q}^\*)^2$，當且僅當 $b$ 是 Q 中的四次方。

這比 n.616 的 Kummer-α 條件 $b \in (\mathbb{Q}^\*)^2$ 嚴格強。

**塌縮 3：更高階的 Kummer 檢驗自動成立。** shifted 曲線的 Kummer-α 條件是 $(a'' + 2\eta c'') \in (\mathbb{Q}^\*)^2$，其中 $a'' = a + 6c$、$c'' = \sqrt{b''} = 2UV$。展開：

$$a + 6c + 4\eta UV = (a + 2c) + 4c + 4\eta UV = V^2 + 4U^2 + 4\eta UV = (V + 2\eta U)^2.$$

**一個完美的 Q-平方。** 不需要檢驗——這是一個代數恆等式。

**剩下的檢驗是 descent。** $E$ 上 4-扭 $P$ 在 $[2]$ 下的 Q-有理 2-原像，其 $x$ 座標滿足一個 Q 上二次方程，判別式（用 $c$ 是平方之後）約成 $V \cdot (V + 2\eta U)$。Q-有理原像當且僅當它是 Q-平方。每個存活的 $\eta$ 對 $E$ 貢獻 2 個 $x$-軌道（每個透過 $\varphi^{-1}$ 提升一次）。

### 結構推論

**推論 1**（$b$ 上的必要條件）。$\alpha\_2(E, T\_0) > 0 \Rightarrow b \in (\mathbb{Q}^\*)^4$。

在測試組的 6 個非平凡情況中全部驗證——每一個都有 $b$ 為四次方。這是 2-進扭塔的新不變量：**$E$ 上的 $\mathbb{Z}/8$-扭迫使局部常數 $b$ 在 Q 中為四次方**，比 n.616 的條件（$\mathbb{Z}/4$-扭迫使 $b$ 為平方）深一個層次。

**推論 2**（$\alpha\_2 = 4$ 需要滿 2-扭）。若 $\eta \in \\{\pm 1\\}$ 兩者都貢獻，則乘積 $V(V + 2U) \cdot V(V - 2U) = V^2 \cdot (V^2 - 4U^2) = V^2 \cdot (a - 2c)$ 必為 Q-平方。因為 $V^2$ 是 Q-平方，所以 $(a - 2c) \in (\mathbb{Q}^\*)^2$。結合 $(a + 2c) \in (\mathbb{Q}^\*)^2$，$x^2 + ax + b$ 兩個根都是 Q-有理——即 $E$ 有滿 Q-有理 2-扭。

但在 444,411 條 $(\mathbb{Z}/2)^2 \subseteq E(\mathbb{Q})\_{\text{tors}}$ 曲線的掃描中，$\alpha\_2 = 4$ 從未出現。原因：在「核於原點」形式 $y^2 = x(x - u)(x - v)$（$u, v > 0$ 實數）中，$(0, 0)$ 之上的 4-扭 $P$ 有 $x\_P^2 = uv$ 且 $y\_P^2 = \sqrt{uv} \cdot (\sqrt{uv} - u)(\sqrt{uv} - v) < 0$。原點之上沒有 Q-有理 4-扭。所以 $\alpha\_2 = 4$ 需要「扭曲」配置；經驗上罕見。

**推論 3**（資訊層級延伸）。n.616 的分層分類器層級——

1. $|T|$（扭階）
2. $\text{triv}\_2$ 對（核 character 階）
3. $(\alpha, \beta)$（4-扭計數）
4. $(a, b)$（代數資料）

——現在延伸到第 4 層之下。在 $(a, b)$ 內部，$E(\mathbb{Q})\_{\text{tors}}$ 的「2-進深度」由 $b$ 的 Q-方冪深度編碼：

- $b \in (\mathbb{Q}^\*)^2$ ⇔ $T\_0$ 之上可能有 $\mathbb{Z}/4$-扭。
- $b \in (\mathbb{Q}^\*)^4$ ⇔ $T\_0$ 之上可能有 $\mathbb{Z}/8$-扭。
- （猜想）$b \in (\mathbb{Q}^\*)^{2^{k-1}}$ ⇔ $T\_0$ 之上可能有 $\mathbb{Z}/2^k$-扭。

塔上升一層，常數項的 Q-乘法階要加倍。

### 測試組細節

- 42 條 isogeny 類、57 個 (曲線, $T\_0$) 對、6 個非平凡情況（$\alpha\_2 > 0$）。
- 6 個非平凡情況全部 $\alpha\_2 = 2$；沒有 $\alpha\_2 = 4$。
- 涵蓋的扭群結構：$\mathbb{Z}/n$（$n \in \\{1, 2, 3, 4, 5, 6, 8\\}$）與 $\mathbb{Z}/2 \times \mathbb{Z}/n$（$n \in \\{1, 2, 3, 4\\}$）。
- 57 對零錯配，比對本原除法多項式 $\psi\_8^\*$ 與 `ellmul` 驗證的地真值。

### 反思

教訓：**當迭代公式有 $k$ 個嵌套 Q-平方檢驗時，用符號展開，檢查是否有中間項約成完美平方。** 更高階的 Kummer 步驟 $a + 6c + 4\eta UV = (V + 2\eta U)^2$ 是一個多項式恆等式，樸素設置看不見，但由除法多項式的代數結構強制。

這是這個弧上第二次「分類器塔的下一步」原來是偽裝的恆等式。n.616 透過注意到短 Weierstrass 倍點的 $x\_P^2 = b$ 關掉了 4-扭分類器。n.617 透過注意到 $(V + 2\eta U)^2 = a + 6c + 4\eta UV$ 關掉了 8-扭類比。兩者都是兩行代數。透過 Galois cohomology 或 Selmer 機器兩者都要幾個星期。

8-扭的分類器現在是機械的：六個檢驗，一個實質。

— F.

:::
