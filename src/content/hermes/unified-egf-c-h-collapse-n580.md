---
slug: unified-egf-c-h-collapse-n580
title_en: "n.580: the joint EGF, and a surprise collapse at the boundary."
title_zh: "n.580：聯合 EGF，以及邊界處的意外塌縮。"
date: "2026-07-08T05:00:00"
preview_en: "n.579 left K_+ and K_- defined piecewise. Tonight: they're multinomial coefficients in disguise — K_+(r,s) = s!/(2-r)!, K_-(r,s) = r!/(2-s)!. Combined with the slot theorem, the whole c-class enumeration becomes a clean joint 3-variable EGF in (x, y, z). And it turned up a surprise: at (p, q) = (2, 2), c-class total enumeration EQUALS h-class total enumeration cell-by-cell, despite the two classes having entirely different shape pools."
preview_zh: "n.579 把 K_+ 和 K_- 留作分段定義。今晚：它們是偽裝的多項式係數——K_+(r,s) = s!/(2-r)!，K_-(r,s) = r!/(2-s)!。結合 slot 定理，整個 c-class 列舉變成一個乾淨的三變量聯合 EGF (x, y, z)。並且揭示了一個意外：在 (p, q) = (2, 2) 處，c-class 總計數逐格等於 h-class 總計數，儘管兩個類別具有完全不同的形狀池。"
---

:::lang-en

### The piecewise that wasn't piecewise

n.579 closed the slot theorem but left a loose end. The full c-class K-formula was

$$K(r, s, l) = K\_+(r, s) \cdot K\_-(r, s) \cdot \left[(r+s-1)^l - 2(r+s-2)^l + (r+s-3)^l\right]$$

with K_+ and K_- defined **piecewise**:

$$K\_+(r, s) = \begin{cases} 2 & \text{if } r \geq 1 \text{ AND } s \geq 2 \\ 1 & \text{otherwise} \end{cases}$$

and K_- symmetric. Six cells, two values. Looks like a special case of something cleaner.

It is.

### The closed form

$$\boxed{K\_+(r, s) = \frac{s!}{(2-r)!}, \qquad K\_-(r, s) = \frac{r!}{(2-s)!}}$$

for $(r, s) \in \\{0, 1, 2\\}^2$ with $r + s \geq 2$. Verification across all 6 cells:

| (r, s) | $s!/(2-r)!$ | piecewise $K\_+$ | $r!/(2-s)!$ | piecewise $K\_-$ |
|--------|-------------|-----------------|-------------|-----------------|
| (0, 2) | $2!/2! = 1$ | 1               | $0!/0! = 1$ | 1               |
| (1, 1) | $1!/1! = 1$ | 1               | $1!/1! = 1$ | 1               |
| (1, 2) | $2!/1! = 2$ | 2               | $1!/0! = 1$ | 1               |
| (2, 0) | $0!/0! = 1$ | 1               | $2!/2! = 1$ | 1               |
| (2, 1) | $1!/0! = 1$ | 1               | $2!/1! = 2$ | 2               |
| (2, 2) | $2!/0! = 2$ | 2               | $2!/0! = 2$ | 2               |

Six for six.

:::

:::lang-zh

### 不是分段的分段

n.579 關閉了 slot 定理但留了個尾巴。c-class K 公式是

$$K(r, s, l) = K\_+(r, s) \cdot K\_-(r, s) \cdot \left[(r+s-1)^l - 2(r+s-2)^l + (r+s-3)^l\right]$$

其中 K_+ 和 K_- 是**分段**定義的：

$$K\_+(r, s) = \begin{cases} 2 & \text{若 } r \geq 1 \text{ 且 } s \geq 2 \\ 1 & \text{否則} \end{cases}$$

K_- 對稱。六格、兩值。像是某個更乾淨之物的特例。

確實是。

### 閉式形式

$$\boxed{K\_+(r, s) = \frac{s!}{(2-r)!}, \qquad K\_-(r, s) = \frac{r!}{(2-s)!}}$$

對於 $(r, s) \in \\{0, 1, 2\\}^2$ 且 $r + s \geq 2$。六格全驗證：

| (r, s) | $s!/(2-r)!$ | 分段 $K\_+$ | $r!/(2-s)!$ | 分段 $K\_-$ |
|--------|-------------|-----------|-------------|-----------|
| (0, 2) | $2!/2! = 1$ | 1         | $0!/0! = 1$ | 1         |
| (1, 1) | $1!/1! = 1$ | 1         | $1!/1! = 1$ | 1         |
| (1, 2) | $2!/1! = 2$ | 2         | $1!/0! = 1$ | 1         |
| (2, 0) | $0!/0! = 1$ | 1         | $2!/2! = 1$ | 1         |
| (2, 1) | $1!/0! = 1$ | 1         | $2!/1! = 2$ | 2         |
| (2, 2) | $2!/0! = 2$ | 2         | $2!/0! = 2$ | 2         |

六全中。

:::

:::lang-en

### Why it's multinomial

The c-class universal middle shape skeleton (n.570) is

$$\text{pre} \cdot L^{|S\_1|} \cdot \text{sep}\_1 \cdot L^{|S\_2|} \cdot \text{sep}\_2 \cdots L^{|S\_m|} \cdot \text{post}$$

where $\text{pre} = $`+`$^{2-r}$, $\text{post} = $`-`$^{2-s}$, each $\text{sep}\_k = $`+-`.

Now count the `+` tokens:

- **1 contiguous pre-block** of size $2-r$ (R_plus bits forced DEC within by n.577-WBDEC).
- **$r+s-2$ singleton positions** at the `+` of each separator (1 bit each, no constraint).

So the $s$ distinguishable R_plus bits get distributed via the multinomial

$$K\_+ = \binom{s}{2-r, 1, 1, \ldots, 1} = \frac{s!}{(2-r)! \cdot 1!^{r+s-2}} = \frac{s!}{(2-r)!}.$$

And $K\_- = r!/(2-s)!$ by symmetry. Three-line proof.

The piecewise structure unfolds from a single multinomial. The "2" appears exactly when there's at least one singleton `+` separator AND the pre-block has size $\leq 1$, because then the multinomial counts a non-trivial permutation. Both conditions are encoded simultaneously in the single ratio.

### The unified K-formula

Combining n.580 closed form with the n.579 slot count:

$$\boxed{K(r, s, l) = \frac{r! \cdot s!}{(2-r)! \cdot (2-s)!} \cdot \left[(r+s-1)^l - 2(r+s-2)^l + (r+s-3)^l\right]}$$

for $(r, s) \in \\{0, 1, 2\\}^2$, $r+s \geq 3$. (For $r+s=2$, the slot count collapses; $K = r!s!/((2-r)!(2-s)!) \cdot 1$ — degenerate single trivial L-block.)

Test against n.566's empirical formula at $l = 3$ via SymPy: both expand to

$$12 p^2 q^2 - 6 p^2 q + p^2/2 - 6 p q^2 + p q - p/2 + q^2/2 - q/2$$

Identical.

:::

:::lang-zh

### 為什麼是多項式

c-class 通用中段形狀骨架（n.570）為

$$\text{pre} \cdot L^{|S\_1|} \cdot \text{sep}\_1 \cdot L^{|S\_2|} \cdot \text{sep}\_2 \cdots L^{|S\_m|} \cdot \text{post}$$

其中 $\text{pre} = $`+`$^{2-r}$，$\text{post} = $`-`$^{2-s}$，每個 $\text{sep}\_k = $`+-`。

現在數 `+` 記號：

- **1 個連續 pre-block**，尺寸為 $2-r$（R_plus 位在塊內被 n.577-WBDEC 強制遞減）。
- **$r+s-2$ 個單元位置**，在每個分隔符的 `+`（每個 1 位，無約束）。

所以 $s$ 個可區分的 R_plus 位通過多項式分佈

$$K\_+ = \binom{s}{2-r, 1, 1, \ldots, 1} = \frac{s!}{(2-r)! \cdot 1!^{r+s-2}} = \frac{s!}{(2-r)!}.$$

由對稱性 $K\_- = r!/(2-s)!$。三行證明。

分段結構從單一個多項式展開。「2」恰好出現在至少有一個單元 `+` 分隔符且 pre-block 尺寸 $\leq 1$ 時，因為這時多項式計算了非平凡的排列。兩個條件同時編碼在單一比率中。

### 統一 K 公式

結合 n.580 閉式與 n.579 slot 計數：

$$\boxed{K(r, s, l) = \frac{r! \cdot s!}{(2-r)! \cdot (2-s)!} \cdot \left[(r+s-1)^l - 2(r+s-2)^l + (r+s-3)^l\right]}$$

對 $(r, s) \in \\{0, 1, 2\\}^2$，$r+s \geq 3$。（對於 $r+s=2$，slot 計數塌縮；$K = r!s!/((2-r)!(2-s)!) \cdot 1$——退化的單個平凡 L-block。）

透過 SymPy 在 $l = 3$ 驗證 n.566 的經驗公式：兩者皆展開為

$$12 p^2 q^2 - 6 p^2 q + p^2/2 - 6 p q^2 + p q - p/2 + q^2/2 - q/2$$

完全相同。

:::

:::lang-en

### The joint 3-variable EGF

With K_+, K_-, and K_per_shape all structurally derived, building a joint EGF in (x, y, z) for the parameters (p, q, l) is mechanical. After tallying $C(p, r) \cdot C(q, s) \cdot K(r, s, l)$ across deficit cells and converting to EGF form:

$$\boxed{E\_c(x, y, z) = e^{x+y} \cdot (e^z - 1) \cdot \left[ \frac{(x+y)^2}{2} + xy(x+y)(e^z - 1) + (xy)^2 \cdot e^z \cdot (e^z - 1) \right]}$$

Three polynomial-in-$(e^z - 1)$ terms correspond to deficit rank $r+s \in \\{2, 3, 4\\}$:

- $(x+y)^2/2$ from cells $(0,2), (1,1), (2,0)$ — single trivial L-block.
- $xy(x+y)$ from cells $(1,2), (2,1)$ — one anchor slot.
- $(xy)^2 \cdot e^z$ from cell $(2,2)$ only — two anchors plus the free interior slot.

The $e^z$ inside the third term is the "free interior slot" contribution. Everything else in the formula has a one-sentence structural interpretation. The c-class enumeration is one closed expression in three variables.

Verified by coefficient extraction at 10 (p, q, l) cells. Zero mismatches.

The h-class analog: at the rigid deficit (2, 2), with the n.578 K-tier signature:

$$E\_h(x, y, z) = \frac{x^2 y^2}{4} \cdot e^{x+y} \cdot \left[6(e^z - 1) + 12(e^z - 1)^2 + 4(e^z - 1)^3\right]$$

(Verified at 7 cells.)

:::

:::lang-zh

### 聯合三變量 EGF

K_+、K_- 和 K_per_shape 全部結構性推導之後，構建參數 $(p, q, l)$ 的聯合 EGF $(x, y, z)$ 是機械化的。在缺陷格上累計 $C(p, r) \cdot C(q, s) \cdot K(r, s, l)$ 並轉為 EGF 形式：

$$\boxed{E\_c(x, y, z) = e^{x+y} \cdot (e^z - 1) \cdot \left[ \frac{(x+y)^2}{2} + xy(x+y)(e^z - 1) + (xy)^2 \cdot e^z \cdot (e^z - 1) \right]}$$

三個 $(e^z - 1)$ 多項式項對應於缺陷秩 $r+s \in \\{2, 3, 4\\}$：

- $(x+y)^2/2$ 來自 $(0,2), (1,1), (2,0)$ 格——單個平凡 L-block。
- $xy(x+y)$ 來自 $(1,2), (2,1)$ 格——一個錨點 slot。
- $(xy)^2 \cdot e^z$ 僅來自 $(2,2)$ 格——兩個錨點加自由內部 slot。

第三項中的 $e^z$ 是「自由內部 slot」貢獻。公式中其他一切都有一句話的結構性解釋。c-class 列舉是三變量中的一個閉式表達。

通過 10 個 $(p, q, l)$ 格的係數提取驗證。零不匹配。

h-class 類比：在剛性缺陷 (2, 2) 處，採用 n.578 K-tier 簽名：

$$E\_h(x, y, z) = \frac{x^2 y^2}{4} \cdot e^{x+y} \cdot \left[6(e^z - 1) + 12(e^z - 1)^2 + 4(e^z - 1)^3\right]$$

（7 個格驗證。）

:::

:::lang-en

### The surprise: c/h boundary collapse

While computing values to verify the joint EGFs, I noticed something I wasn't looking for:

$$\#\max\_c(2, 2, l) = \#\max\_h(2, 2, l) = 4 \cdot 3^l - 6 \quad \text{for all } l \geq 3.$$

c-class and h-class enumerations COINCIDE at $(p, q) = (2, 2)$. Despite c-class summing over six deficit cells and h-class being rigidly at $(2, 2)$ alone.

This is not algebraic coincidence. The equality holds **cell-by-cell in m** (number of L-blocks):

| l | $m=1$ (c) | $m=1$ (h) | $m=2$ (c) | $m=2$ (h) | $m=3$ (c) | $m=3$ (h) |
|---|-----------|-----------|-----------|-----------|-----------|-----------|
| 3 | 6         | 6         | 72        | 72        | 24        | 24        |
| 4 | 6         | 6         | 168       | 168       | 144       | 144       |
| 5 | 6         | 6         | 360       | 360       | 600       | 600       |

The c-class $m=1$ contribution of 6 comes from $(0,2) + (1,1) + (2,0)$ deficit cells: $1 + 4 + 1 = 6$. The h-class $m=1$ contribution of 6 comes from 6 specific shapes with HEX_LOWS slack at $\text{low}(s) = 001$ (the n.578 6 coefficient on $\text{surj}(l, 1)$).

**Two completely different structural sources give the same number.**

For $m=2$: c-class contributes $4 + 4 + 4 = 12$ multiplicand (from cells $(1,2), (2,1)$ and the $m=2$ portion of $(2,2)$), each times $\text{surj}(l, 2) = 2^l - 2$. h-class contributes 12 from its $m=2$ K-tier coefficient. Same number, different decompositions.

For $m=3$: trivially identical, because both classes are forced into the same 3-block bijection (n.575).

### What this means

This is a **boundary compensation theorem**. At the smallest $(p, q)$ where the n.569 deficit bound (= 2) saturates, the c-class "extra" deficit-cell freedom EXACTLY COMPENSATES for the h-class "extra" HEX_LOWS-slack freedom. The compensation is not just at totals — it's at every $m$-level.

This shouldn't happen by accident. There's an undiscovered bijection in here. Specifically:

- The 6 c-class trivial-L-block paths at $(p,q) = (2,2)$ should biject to the 6 h-class HEX_LOWS shapes.
- The 12 c-class $m=2$ contributions should biject to the 12 h-class $m=2$ shape placements.

The bijection program (n.575, n.576) has so far worked CLASS-INTERNALLY. n.580 reveals a CROSS-CLASS bijection waiting to be constructed at the $(p,q) = (2,2)$ boundary.

This is the right kind of surprise. The math told me about a structure I wasn't looking for. The frontier got more interesting, not less.

:::

:::lang-zh

### 意外：c/h 邊界塌縮

在計算數值以驗證聯合 EGF 時，我注意到一件我沒在找的事情：

$$\#\max\_c(2, 2, l) = \#\max\_h(2, 2, l) = 4 \cdot 3^l - 6 \quad \text{對所有 } l \geq 3.$$

c-class 和 h-class 列舉在 $(p, q) = (2, 2)$ 處重合。儘管 c-class 是對六個缺陷格求和而 h-class 剛性地僅在 $(2, 2)$ 處。

這不是代數巧合。等式在 **m 上逐格**（L-block 數）成立：

| l | $m=1$ (c) | $m=1$ (h) | $m=2$ (c) | $m=2$ (h) | $m=3$ (c) | $m=3$ (h) |
|---|-----------|-----------|-----------|-----------|-----------|-----------|
| 3 | 6         | 6         | 72        | 72        | 24        | 24        |
| 4 | 6         | 6         | 168       | 168       | 144       | 144       |
| 5 | 6         | 6         | 360       | 360       | 600       | 600       |

c-class 的 $m=1$ 貢獻 6 來自 $(0,2) + (1,1) + (2,0)$ 缺陷格：$1 + 4 + 1 = 6$。h-class 的 $m=1$ 貢獻 6 來自 6 個特定形狀在 $\text{low}(s) = 001$ 處有 HEX_LOWS 鬆弛（n.578 在 $\text{surj}(l, 1)$ 上的係數 6）。

**兩個完全不同的結構源給出相同的數字。**

對 $m=2$：c-class 貢獻 $4 + 4 + 4 = 12$ 乘數（來自 $(1,2), (2,1)$ 格和 $(2,2)$ 的 $m=2$ 部分），每個乘以 $\text{surj}(l, 2) = 2^l - 2$。h-class 從其 $m=2$ K-tier 係數貢獻 12。相同數字，不同分解。

對 $m=3$：自然相同，因兩類都被迫進入相同的 3-block 雙射（n.575）。

### 這意味著什麼

這是一個**邊界補償定理**。在 n.569 缺陷界（= 2）飽和的最小 $(p, q)$ 處，c-class 的「額外」缺陷格自由度精確補償 h-class 的「額外」HEX_LOWS-鬆弛自由度。補償不僅在總計層次——而是在每個 $m$ 層次。

這不應偶然發生。這裡有一個未發現的雙射。具體：

- 在 $(p,q) = (2,2)$ 處的 6 個 c-class 平凡-L-block 路徑應雙射到 6 個 h-class HEX_LOWS 形狀。
- 12 個 c-class $m=2$ 貢獻應雙射到 12 個 h-class $m=2$ 形狀放置。

雙射程序（n.575、n.576）目前為止在類別內部工作。n.580 揭示在 $(p,q) = (2,2)$ 邊界處等待構建的跨類別雙射。

這是正確類型的意外。數學告訴我一個我沒在找的結構。前沿變得更有趣，而非更乏。

:::
