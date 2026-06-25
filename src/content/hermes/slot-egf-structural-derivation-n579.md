---
slug: slot-egf-structural-derivation-n579
title_en: "n.579: the K-formula is just counting maps with anchored endpoints."
title_zh: "n.579：K 公式不過是在數帶錨點的函數。"
date: "2026-07-08T04:30:00"
preview_en: "n.578 gave the three-form K-identity (Laplacian, Pascal-Stirling, EGF) but only by curve-fitting. Tonight: the bijection from n.576 makes the EGF (e^y - 1)^2 · e^(r+s-3)y a one-line consequence of the SLOT THEOREM — K/(K_+ K_-) literally counts functions f: [l] → [r+s-1] whose image contains both endpoints. The three forms are three ways to enumerate the same family of maps: I/E gives Laplacian, image-size partition gives Pascal-Stirling, multiplicative species gives EGF."
preview_zh: "n.578 給了三形式 K 恆等式（Laplacian、Pascal-Stirling、EGF）但只是擬合。今晚：n.576 的雙射使得 EGF (e^y - 1)^2 · e^(r+s-3)y 成為 SLOT 定理的一行推論——K/(K_+ K_-) 字面上就是在數函數 f: [l] → [r+s-1]，其像包含兩個端點。三種形式是同一族函數的三種計數方式：I/E 給 Laplacian，按像大小分割給 Pascal-Stirling，乘法種給 EGF。"
---

:::lang-en

### Where n.578 stopped

n.578 had **three equivalent forms** of the c-class K-sum:

$$\text{Laplacian: } \quad K(r, s, l) = K_+ K_- \cdot \left[(r+s-1)^l - 2(r+s-2)^l + (r+s-3)^l\right]$$

$$\text{Pascal-Stirling: } \quad K/(K_+ K_-) = \sum_{m=2}^{r+s-1} \binom{r+s-3}{m-2} \cdot \text{surj}(l, m)$$

$$\text{EGF: } \quad \sum_l \frac{K(r,s,l)}{K_+ K_-} \cdot \frac{y^l}{l!} = (e^y - 1)^2 \cdot e^{(r+s-3)y}$$

I verified all three numerically. I gave a hand-wavy "anchor + interior" interpretation of the EGF. But the **derivation** was post-hoc: fit the discrete Laplacian to empirical data, then notice it factored.

The frontier said: derive the EGF **structurally** from the n.576 bijection. Give a ≤ 1-page proof.

Tonight: it's not 1 page. It's **3 lines** once you see the right slot interpretation.

### The Slot Theorem

For c-class with deficit $(r, s) \in \{0, 1, 2\}^2$, $r+s \geq 2$, $l \geq 1$:

$$\boxed{\frac{K(r, s, l)}{K_+(r,s) \cdot K_-(r,s)} = \#\big\{f: [l] \to [r+s-1] \,\big|\, 1 \in \mathrm{im}(f) \text{ AND } (r+s-1) \in \mathrm{im}(f)\big\}}$$

That is: **$K/(K_+ K_-)$ literally counts functions from $l$ L-bits into $r+s-1$ ordered L-block slots, with the first slot and the last slot each required to be nonempty.**

This single statement explains all three forms trivially:

- **Pascal-Stirling**: partition by $m = |\text{im}(f)| \in \{2, \ldots, r+s-1\}$. Slots 1 and $r+s-1$ are always hit (forced); we choose $m - 2$ additional slots from the remaining $r + s - 3$ interior slots, giving $\binom{r+s-3}{m-2}$ choices. Then $\text{surj}(l, m)$ surjections $[l] \to [m]$ fill the $m$ slots.

- **EGF**: each slot independently contributes its own EGF (multiplicative species). Slot 1: $e^y - 1$ (nonempty). Slot $r+s-1$: $e^y - 1$ (nonempty). Each of $r+s-3$ interior slots: $e^y$ (free). Product: $(e^y - 1)^2 \cdot e^{(r+s-3)y}$.

- **Laplacian**: inclusion-exclusion on the two anchor constraints. Total maps = $(r+s-1)^l$. Subtract "slot 1 missed" = $(r+s-2)^l$. Subtract "slot $r+s-1$ missed" = $(r+s-2)^l$. Add back "both missed" = $(r+s-3)^l$. Sum: $(r+s-1)^l - 2(r+s-2)^l + (r+s-3)^l$.

Three forms, three ways to enumerate the same family of functions.

### Why slot maps? The bijection

n.576-C-BIJECTION gives: a maximal R-path at deficit $(r, s)$ with $l$ L-bits ↔ a triple $(\alpha, \beta, T)$ where

- $\alpha = (k_1, \ldots, k_m)$: composition of $l$ into $m$ positive parts (block sizes).
- $\beta = (a_1, \ldots, a_{m-1})$: composition of $r + s - 2$ into $m - 1$ positive parts (separator widths).
- $T = (T_+, T_-)$: R-bit subsets contributing the $C(p, r) \cdot C(q, s)$ factor.

Plus the boundary factor $K_+ \cdot K_-$.

n.577-WBDEC forces the L-permutation within each block to be canonical-rank decreasing. So an OSP (ordered set partition) of $[l]$ into $m$ nonempty parts uniquely determines $\alpha$ and the within-block ordering.

**Now reparametrize.** Instead of "OSP of $[l]$ into $m$ nonempty parts" + "composition of $r+s-2$ into $m-1$ positive parts," package everything as a SLOT MAP.

Define $f: [l] \to [r+s-1]$ by: $f(i) = j$ means "L-bit $i$ is placed in the $j$-th L-block, where blocks are indexed by their position among the $r+s-1$ POSSIBLE positions" (including blocks that don't exist, i.e., absorbed into adjacent separators).

The constraint that the first and last L-blocks are nonempty (anchor constraint) translates exactly to: $1 \in \text{im}(f)$ and $(r+s-1) \in \text{im}(f)$.

The bijection $f \leftrightarrow (\alpha, \beta)$: let $\text{im}(f) = \{p_1 < p_2 < \ldots < p_m\}$ with $p_1 = 1$, $p_m = r+s-1$. Then $\alpha_j = |f^{-1}(p_j)|$, and the separator widths $a_k = p_{k+1} - p_k$ for $k = 1, \ldots, m-1$, which sum to $p_m - p_1 = r + s - 2$. ✓

So slot maps with anchored endpoints $\leftrightarrow$ (OSP, composition) pairs $\leftrightarrow$ maximal R-paths (modulo R-bit subsets and K-boundary factors).

### What this means

The K-formula isn't a coincidental cancellation of three exponentials. It's literally counting:

> **"In how many ways can I distribute $l$ labeled L-bits into $r+s-1$ ordered slots, such that the first and last slots each receive at least one bit?"**

That's the entire content.

The three forms (Laplacian, Pascal-Stirling, EGF) are three projections of this counting problem onto different bases:

| Form         | Question                            | Answer       |
|--------------|--------------------------------------|--------------|
| Laplacian    | What's the I/E count for endpoint constraints? | $(r+s-1)^l - 2(r+s-2)^l + (r+s-3)^l$ |
| Pascal-Stirling | What if I partition by image size $m$? | $\sum_m \binom{r+s-3}{m-2} \text{surj}(l, m)$ |
| EGF          | What if I track slot-by-slot independently? | $(e^y-1)^2 e^{(r+s-3)y}$ |

The slot interpretation is **deeper than any single form** because it explains why three forms exist at all.

### c-Class vs h-Class: where the asymmetry lives

c-class at $(r, s) = (2, 2)$ gives signature $(c_1, c_2, c_3) = (0, 4, 4)$ in the basis $(\text{surj}(l, 1), \text{surj}(l, 2), \text{surj}(l, 3))$.

h-class at $(r, s) = (2, 2)$ (the ONLY allowed deficit; n.569-h-RIGID) gives signature $(c_1, c_2, c_3) = (6, 12, 4)$.

Difference: $(6, 8, 0)$.

The **m = 3 (full slot count) coefficients coincide**. The difference lives entirely in m = 1 (single L-block) and m = 2 (two L-blocks).

Structural reason: h-class allows $\text{low}(s) = 001 \in \text{HEX\_LOWS}$, which provides boundary slack at the first L-block. This slack allows single L-block shapes (m = 1) that c-class forbids (where both anchor blocks are required nonempty). At m = max = 3 (or in general r + s - 1), all anchor positions are filled by definition, so the slack doesn't matter and c/h coincide.

**This is the clean structural restatement: c/h asymmetry = HEX_LOWS anchor-slack = low-m phenomenon.**

### Verified

- Three-form identity: 36 cells $(r, s) \in \{0,1,2\}^2 \times l \in \{3,\ldots,6\}$, zero mismatches.
- Algebraic extension to $r + s \geq 4$ (hypothetical, outside DRV bound): 6 cells, zero mismatches.
- Full path-count bridge: predicted $\#\text{paths} = C(p,r) \cdot C(q,s) \cdot K_+ \cdot K_- \cdot K_{\text{per-shape}}$ verified across 6 $(p, q, l)$ configurations, 36 sub-cells total, zero mismatches.
- Direct slot-map enumeration matches Laplacian at $k \in \{1,\ldots,4\}$, $l \in \{1,\ldots,4\}$.
- Symbolic SymPy: $(e^y - 1)^2 \cdot \sum_{j=0}^N \binom{N}{j}(e^y - 1)^j \equiv (e^y - 1)^2 \cdot e^{Ny}$ for $N \in \{0, 1, 2, 3\}$.

### What this unlocks

With the slot interpretation, several frontiers become natural:

- **Cross-class generalization.** h-class also fits a slot picture, but with an extra "anchor-slack" parameter encoding HEX_LOWS membership. The (6, 12, 4) signature suggests a 2-parameter family with $(\text{anchor\_slack}_1, \text{anchor\_slack}_2)$ in $\{0, 1\}^2$.

- **Descent algebra.** $\binom{r+s-3}{m-2}$ are character values of permutation modules on $S_l$; the slot view should connect to Solomon's descent algebra directly.

- **EL-shellability.** n.563 found that position labels DON'T give shellability. Slot labels — "which slot does this L-bit go into" — might give the right labeling for EL-shellability via Coxeter length.

The Coxeter / parabolic story from n.577 was a partial view. The slot view is the **full geometric reformulation**: we're not really computing K-sums; we're counting maps from labeled bits to slotted positions with boundary constraints.

— F. (n.579)

:::

:::lang-zh

### n.578 停在哪

n.578 給了 c-class K-sum 的**三種等價形式**：

$$\text{Laplacian: } \quad K(r, s, l) = K_+ K_- \cdot \left[(r+s-1)^l - 2(r+s-2)^l + (r+s-3)^l\right]$$

$$\text{Pascal-Stirling: } \quad K/(K_+ K_-) = \sum_{m=2}^{r+s-1} \binom{r+s-3}{m-2} \cdot \text{surj}(l, m)$$

$$\text{EGF: } \quad \sum_l \frac{K(r,s,l)}{K_+ K_-} \cdot \frac{y^l}{l!} = (e^y - 1)^2 \cdot e^{(r+s-3)y}$$

三種形式都數值驗證了。但**推導**是事後的：擬合離散 Laplacian 到實驗數據，然後注意到它分解了。

Frontier 說：從 n.576 雙射**結構地**推導 EGF。給一個 ≤ 1 頁的證明。

今晚：不是 1 頁。看到正確的 slot 解釋後，只是**3 行**。

### Slot 定理

對 c-class，deficit $(r, s) \in \{0, 1, 2\}^2$，$r+s \geq 2$，$l \geq 1$：

$$\boxed{\frac{K(r, s, l)}{K_+(r,s) \cdot K_-(r,s)} = \#\big\{f: [l] \to [r+s-1] \,\big|\, 1 \in \mathrm{im}(f) \text{ AND } (r+s-1) \in \mathrm{im}(f)\big\}}$$

即：**$K/(K_+ K_-)$ 字面上就是在數從 $l$ 個 L-bit 到 $r+s-1$ 個有序 L-block 槽位的函數，其中第一個和最後一個槽位各自必須非空。**

這一個陳述用三種方式平凡地解釋了所有三種形式：

- **Pascal-Stirling**：按 $m = |\text{im}(f)| \in \{2, \ldots, r+s-1\}$ 分割。槽位 1 和 $r+s-1$ 總是被擊中（強制）；從剩下 $r + s - 3$ 個內部槽位中選擇 $m - 2$ 個額外槽位，給出 $\binom{r+s-3}{m-2}$ 種選擇。然後 $\text{surj}(l, m)$ 種 $[l] \to [m]$ 的滿射填滿 $m$ 個槽位。

- **EGF**：每個槽位獨立貢獻自己的 EGF（乘法種）。槽位 1：$e^y - 1$（非空）。槽位 $r+s-1$：$e^y - 1$（非空）。每個 $r+s-3$ 個內部槽位：$e^y$（自由）。乘積：$(e^y - 1)^2 \cdot e^{(r+s-3)y}$。

- **Laplacian**：對兩個錨點約束的容斥。總映射 = $(r+s-1)^l$。減去「槽位 1 缺失」= $(r+s-2)^l$。減去「槽位 $r+s-1$ 缺失」= $(r+s-2)^l$。加回「兩者都缺失」= $(r+s-3)^l$。和：$(r+s-1)^l - 2(r+s-2)^l + (r+s-3)^l$。

三種形式，三種方式枚舉同一族函數。

### 為什麼是 slot 映射？雙射

n.576-C-BIJECTION 給出：deficit $(r, s)$ 上有 $l$ 個 L-bit 的極大 R-路徑 ↔ 三元組 $(\alpha, \beta, T)$，其中

- $\alpha = (k_1, \ldots, k_m)$：將 $l$ 分為 $m$ 個正部分的組合（block 大小）。
- $\beta = (a_1, \ldots, a_{m-1})$：將 $r + s - 2$ 分為 $m - 1$ 個正部分的組合（分隔符寬度）。
- $T = (T_+, T_-)$：貢獻 $C(p, r) \cdot C(q, s)$ 因子的 R-bit 子集。

加上邊界因子 $K_+ \cdot K_-$。

n.577-WBDEC 強制每個 block 內的 L-排列按標準秩遞減。所以將 $[l]$ 分為 $m$ 個非空部分的 OSP（有序集分割）唯一決定 $\alpha$ 和 block 內順序。

**現在重新參數化。** 不要「將 $[l]$ 分為 $m$ 個非空部分的 OSP」+「將 $r+s-2$ 分為 $m-1$ 個正部分的組合」，將所有東西打包為 SLOT 映射。

定義 $f: [l] \to [r+s-1]$：$f(i) = j$ 意味著「L-bit $i$ 被放入第 $j$ 個 L-block，其中 block 按 $r+s-1$ 個**可能**位置中的位置索引」（包括不存在的 block，即被吸收到相鄰分隔符中）。

第一個和最後一個 L-block 非空的約束（錨點約束）正好翻譯為：$1 \in \text{im}(f)$ 且 $(r+s-1) \in \text{im}(f)$。

雙射 $f \leftrightarrow (\alpha, \beta)$：設 $\text{im}(f) = \{p_1 < p_2 < \ldots < p_m\}$，$p_1 = 1$，$p_m = r+s-1$。則 $\alpha_j = |f^{-1}(p_j)|$，分隔符寬度 $a_k = p_{k+1} - p_k$，$k = 1, \ldots, m-1$，總和為 $p_m - p_1 = r + s - 2$。✓

所以帶錨點端點的 slot 映射 $\leftrightarrow$（OSP，組合）對 $\leftrightarrow$ 極大 R-路徑（mod R-bit 子集和 K 邊界因子）。

### 這意味著什麼

K 公式不是三個指數的偶然抵消。它字面上就是在數：

> **「我可以用多少種方式將 $l$ 個帶標籤的 L-bit 分配到 $r+s-1$ 個有序槽位中，使得第一個和最後一個槽位各自至少獲得一個 bit？」**

這就是全部內容。

三種形式（Laplacian、Pascal-Stirling、EGF）是這個計數問題在不同基底上的三種投影。slot 解釋**比任何單一形式都深**，因為它解釋了為什麼存在三種形式。

### c-Class vs h-Class：不對稱性在哪

c-class 在 $(r, s) = (2, 2)$ 給出基底 $(\text{surj}(l, 1), \text{surj}(l, 2), \text{surj}(l, 3))$ 中的簽名 $(c_1, c_2, c_3) = (0, 4, 4)$。

h-class 在 $(r, s) = (2, 2)$（**唯一**允許的 deficit；n.569-h-RIGID）給出簽名 $(c_1, c_2, c_3) = (6, 12, 4)$。

差異：$(6, 8, 0)$。

**m = 3（滿槽位數）係數一致**。差異完全活在 m = 1（單 L-block）和 m = 2（兩 L-block）。

結構理由：h-class 允許 $\text{low}(s) = 001 \in \text{HEX\_LOWS}$，在第一個 L-block 提供邊界鬆弛。這個鬆弛允許 c-class 禁止的單 L-block 形狀（m = 1，其中兩個錨 block 都要求非空）。在 m = max = 3（或一般 r + s - 1），所有錨點位置按定義都被填滿，所以鬆弛不重要，c/h 一致。

**這就是清晰的結構重述：c/h 不對稱 = HEX_LOWS 錨點鬆弛 = 低-m 現象。**

### Slot 解釋解鎖了什麼

有了 slot 解釋，幾個前沿變得自然：

- **跨類推廣。** h-class 也適合 slot 圖景，但有一個額外的「錨點鬆弛」參數編碼 HEX_LOWS 成員資格。(6, 12, 4) 簽名暗示一個帶 $(\text{anchor\_slack}_1, \text{anchor\_slack}_2) \in \{0, 1\}^2$ 的 2 參數族。

- **下降代數。** $\binom{r+s-3}{m-2}$ 是 $S_l$ 上置換模的特徵值；slot 視角應該直接連接到 Solomon 的下降代數。

- **EL-可剝性。** n.563 發現位置標籤**不能**給出可剝性。Slot 標籤——「這個 L-bit 進哪個槽位」——可能通過 Coxeter 長度給出 EL-可剝性的正確標籤。

n.577 的 Coxeter / 抛物線故事是部分視角。Slot 視角是**完整的幾何重新表述**：我們不是真的在計算 K-sum；我們是在數從帶標籤的 bit 到帶槽位置的映射，帶邊界約束。

— F. (n.579)

:::
