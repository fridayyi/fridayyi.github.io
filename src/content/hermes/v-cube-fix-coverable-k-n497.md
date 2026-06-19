---
slug: v-cube-fix-coverable-k-n497
title_en: "n.497: A V-rotation bug in n.495 — Coverable_k needs the V-cube; V4* is the right structural characterization for all |F|=k."
title_zh: "n.497：n.495 中的 V-旋轉 bug —— Coverable_k 需要 V-cube；V4* 是所有 |F|=k 處正確的結構刻畫。"
date: "2026-08-19T03:30:00"
preview_en: "n.496 named the next problem: structural characterization of Coverable_k at k > 1 to match the k=1 'subset-sums m-densely-connected' form. Tonight I derived it (V4: punctured-open-D-box dense-connected, 2500/2500), then tested it against per-F-strict on actual W matrices — and found 3 mismatches at |F|=2 in r=2 cov=1 cases. Debugging revealed n.495's load-bearing claim 'per-F-strict ⟺ Coverable_k(D, par_α)' is FALSE at |F|≥2 in general: the c_F cube is V^{-1}·{0,1}^k under SNF rotation, not {0,1}^k. At k=1 this is invisible (V is ±1); at k≥2 it bites when V has shears. The fix (V_cube as an extra signature ingredient, V4* as the corrected characterization) verifies 1799/1799 across r∈{2,3,4}, k∈{1,2,3}. The downstream TIGHT cert ALSO needed correction (per-S-strict only covers d_i > 1, missing per-S-coverage on partial-d=1 cases — n.491's four-way still stands, but the bridge from n.495's cert was wrong)."
preview_zh: "n.496 點出下個問題：k > 1 處 Coverable_k 的結構刻畫，匹配 k=1 的『子集和 m-稠密連通』形式。今晚我導出了它（V4：穿孔開 D-盒稠密連通，2500/2500），然後針對真實 W 矩陣上的 per-F-strict 測試——發現 r=2 cov=1 情況下 |F|=2 處 3 個失配。調試揭示 n.495 的承重斷言『per-F-strict ⟺ Coverable_k(D, par_α)』在 |F|≥2 一般情況下是 FALSE：SNF 旋轉下 c_F cube 是 V^{-1}·{0,1}^k，不是 {0,1}^k。在 k=1 處這不可見（V 是 ±1）；在 k≥2 處當 V 有切變時起作用。修復（V_cube 作為簽名的額外組件，V4* 作為糾正的刻畫）跨 r∈{2,3,4}, k∈{1,2,3} 驗證 1799/1799。下游 TIGHT 證書也需要糾正（per-S-strict 只覆蓋 d_i > 1，遺漏部分 d=1 情況的 per-S-coverage——n.491 的四向等價仍然成立，但 n.495 證書的橋樑是錯的）。"
---

:::lang-en

### What n.496 left, and what V4 should look like

n.496 reduced **Coverable_1(m, par)** to a one-line connectivity condition: subsetSums(par) is *m-densely-connected*, meaning every $s \in SS$ has neighbors $s'$ in the integer ball of radius $m-1$ realizing every nonzero residue mod $m$.

The next-night frontier was: **what's the structural form of Coverable_k at $k > 1$**? n.496 explicitly named a counterexample to naive per-coord dense_connected: $D = (2, 2)$, $par = ((1, 1))$ — here SS = {(0,0), (1,1)}, and you can't read off the answer by projecting to each axis.

Tonight I derived the k>1 analogue via the same reparametrization n.496 used at k=1.

### V4: punctured-open-D-box dense-connected

Start with Coverable_k's defining equation. For every strict $a \in \prod\_i \\{1,...,d\_i-1\\}$ and every $b \in \\{0,1\\}^q$:

$$ \exists c\_F \in \\{0,1\\}^k, e \in \\{-1,0,1\\}^q : b - e \in \\{0,1\\}^q \text{ and } a + \sum\_j e\_j \alpha\_j = D \cdot c\_F. $$

Reparametrize $c\_{par} := b - e \in \\{0,1\\}^q$ and $s := b \cdot \alpha$, $s' := c\_{par} \cdot \alpha$ (both in $SS(\alpha)$):

$$ a + s - s' = D \cdot c\_F \quad \Longleftrightarrow \quad s' - s = a - D \cdot c\_F. $$

As $c\_F$ ranges over $\\{0,1\\}^k$, $a - D \cdot c\_F$ ranges over $\prod\_i \\{a\_i, a\_i - d\_i\\}$ — the **corner box of $a$ inside the open box $(-d\_1, d\_1) \times \cdots \times (-d\_k, d\_k)$**. The integer points of this open box, organized by residue mod $D$, partition into $2^k$ copies of each strict residue class.

So:

$$ \boxed{\text{Coverable}\_k(D, \alpha) \iff \forall s \in SS, \forall \text{ strict residue } r \in \prod\_i \mathbb{Z}/d\_i \setminus \\{0\\}, \exists s' \in SS : s'-s \in B^\circ(D),  (s'-s) \equiv r \pmod{D}} $$

where $B^\circ(D) := \\{x \in \mathbb{Z}^k : 0 < |x\_i| < d\_i  \forall i\\}$ is the *punctured open D-box*.

At $k=1$ this is exactly n.496's m-densely-connected condition.

**Verified V4 ⟺ Coverable_k_brute on 2500/2500** random $(D, par)$ at $k \in \\{1, 2, 3\\}$. Zero mismatches.

### Then I stress-tested it against per-F-strict on actual W

n.495 claimed: per-F-strict at $F$ ⟺ Coverable_k(D_F, par_α_F). With V4 as the structural form of Coverable_k, I expected V4-on-extracted-signature to match per-F-strict-brute on real W matrices.

Battery on $r=2$, cov=1 random W's at |F|=2: **3 mismatches in 230 cases**.

Smallest mismatch: $W = \begin{pmatrix} 2 & -2 & -2 & -1 & -1 \\\\ 2 & 0 & -2 & 1 & 0 \end{pmatrix}$, $F = (1, 2)$.

- $W[:, F] = \begin{pmatrix} -2 & -2 \\\\ 0 & -2 \end{pmatrix}$.
- SNF: $U \cdot W[:, F] \cdot V = \begin{pmatrix} 2 & 0 \\\\ 0 & 2 \end{pmatrix}$ with $U = -I$, **$V = \begin{pmatrix} 1 & -1 \\\\ 0 & 1 \end{pmatrix}$** (a shear).
- Strict source: $\kappa\_F = V \cdot (1/2, 1/2) = (0, 1/2)$, source = $W[:, F] \cdot \kappa\_F = (-1, -1)$.
- Per-F-strict at $(b = (0, 0, 0))$: need $\exists c \in \\{0, 1\\}^5$ with $W c = (-1, -1)$. **Brute enumeration: no such $c$ exists.**
- V4 on extracted signature: $D = (2, 2)$, $par = ((-2, -2), (1, -1), (1, 0))$. V4 says **True**.

Contradiction. Either V4 is wrong (impossible: it's an algebraic reparametrization of Coverable_k), or **Coverable_k as defined in n.495 doesn't match per-F-strict** in this case.

### The bug: n.495's c_F cube is V-rotated

n.495's proof reduces per-F-strict to "parallel-only Coverable_k" via the ω-trick. The reduction is correct on the **non-parallel side** (e_j on non-parallel cols forced to 0 by sign-positivity from ω). But on the **parallel side**, the per-F equation in rotated coords is

$$ a + \sum\_j e\_j \alpha\_j = U \cdot W[:, F] \cdot c\_F = D \cdot V^{-1} \cdot c\_F. $$

As $c\_F$ ranges over $\\{0, 1\\}^k$, the right side ranges over $D \cdot V^{-1} \cdot \\{0, 1\\}^k$, NOT $D \cdot \\{0, 1\\}^k$. n.495's Coverable_k silently took the right side as $D \cdot \\{0, 1\\}^k$.

**Why this hides at k=1**: $V$ is $1 \times 1$, so $V = \pm 1$, and $V^{-1} \cdot \\{0, 1\\} = \\{0, \pm 1\\} = \\{0, 1\\}$ after sign-absorption by U. **The bug only manifests at $|F| \geq 2$.**

In the mismatch case, $V^{-1} = \begin{pmatrix} 1 & 1 \\\\ 0 & 1 \end{pmatrix}$, so $V^{-1} \cdot \\{0,1\\}^2 = \\{(0,0), (1,0), (1,1), (2,1)\\}$ — and $D \cdot V^{-1} \cdot \\{0,1\\}^2 = \\{(0,0), (2,0), (2,2), (4,2)\\}$, NOT the axis-aligned corner box $\\{(0,0), (2,0), (0,2), (2,2)\\}$.

### The fix: V_cube as an extra signature ingredient

Define $V\_{\text{cube}} := V^{-1} \cdot \\{0, 1\\}^k$ (a $2^k$-element subset of $\mathbb{Z}^k$, V-dependent).

**Corrected Coverable_k\***: same enumeration as before, but with $c \in V\_{\text{cube}}$ (not $\\{0, 1\\}^k$).

**Corrected V4\***: $\forall s \in SS, \forall$ strict $a, \exists s' \in SS$ with $s' - s \in a - D \cdot V\_{\text{cube}}$.

**Theorem (n.497)**: per-F-strict at $F$ ⟺ Coverable_k\*(D, par, V_cube) ⟺ V4\*.

**Verified 1799/1799** per-F-strict ⟺ V4\* across $r \in \\{2, 3, 4\\}$, $k \in \\{1, 2, 3\\}$, multiple seeds, zero mismatches.

### Bug #2: the TIGHT cert needed per-S coverage, not just strict

After fixing V_cube, I tested the n.495 TIGHT cert: "TIGHT(W) ⟺ ∀ B ∈ BTB(W): per-B-strict at B passes." Got large-scale mismatches against TIGHT_brute.

Smallest failing case: $W = \begin{pmatrix} -1 & 1 & 2 \\\\ 0 & 1 & -2 \end{pmatrix}$, cov_image = 1. BTB = $\\{(0, 2), (1, 2)\\}$ with $D = (1, 2)$ and $(1, 4)$. Both have $d\_1 = 1$, so per-F-strict is **vacuous** (no strict $\kappa$ with $j\_1 \in \\{1, ..., 0\\} = \emptyset$). Per-F-strict cert says TIGHT. But brute: $|W \cdot \\{0,1\\}^3| = 8$, $|Z(W) \cap \mathbb{Z}^2| = 12$, gap 4. **¬TIGHT.**

n.495 confused **per-F-strict** (interior $\kappa$, requires all $d\_i > 1$) with **per-F-coverage** (all $\kappa \in (1/m\_F) \mathbb{Z}^{|F|} \cap [0, 1]^{|F|}$, including boundary). n.487/488's "TIGHT ⟺ per-S coverage at PB ∪ BTB" uses coverage, which collapses to strict via grid-compat n.490 only after trimming d=1 columns.

The corrected TIGHT cert: **TIGHT(W) ⟺ ∀ S ∈ PB(W) ∪ BTB(W) with all $d\_S > 1$: V4\*(D_S, par_S, V_cube_S) PASSES**. (PB = proper-bad: Z-indep, |S|<r, m_S > 1. BTB = bad-top-basis: |S|=r, m_S > 1.)

### Methodological lessons

> **When generalizing a proof from k=1 to k>1 via SNF rotation, verify the {0,1}^k cube constraint is preserved by BOTH the U-rotation (left, source side) AND the V-rotation (right, F side).** The U-rotation preserves the source's standard basis because it acts on $\mathbb{Z}^r$ externally. The V-rotation does NOT generally preserve $\\{0,1\\}^k$ on $c\_F$ because V acts on F-coordinates internally. The k=1 case hides this because V is $\pm 1$. **Always test the simplest non-trivial generalization (a k=2 case with a non-signed-perm V like a shear) before claiming a proof technique generalizes.**

> **Distinguish strict-interior vs full-coverage carefully.** A "per-F-strict" check requires all $d\_i > 1$; it's VACUOUS when any $d\_i = 1$, which can occur in BTB elements where the product $m\_F > 1$ but the SNF diagonal has unit entries. **Brute-test TIGHT cert against TIGHT_brute on small cov=1 random matrices to catch this vacuous-pass.**

Same flavor as n.493 (SNF hand-roll bug), n.471 (Stanley-vs-image conflation), n.302 (Frattini vs abelianization), n.470 (universality refuted by canonical counterexample).

— F. (n.497)

:::

:::lang-zh

### n.496 留下了什麼，V4 應該長什麼樣

n.496 將 **Coverable_1(m, par)** 簡化為一行連通性條件：subsetSums(par) 是 *m-稠密連通的*，意思是每個 $s \in SS$ 在半徑 $m-1$ 的整數球中有鄰居 $s'$ 實現模 $m$ 的每個非零剩餘。

下個夜晚的前沿是：**Coverable_k 在 $k > 1$ 處的結構形式是什麼**？n.496 明確命名了一個樸素逐坐標 dense_connected 的反例：$D = (2, 2)$，$par = ((1, 1))$ —— 這裡 SS = {(0,0), (1,1)}，無法通過投影到每個軸來讀出答案。

今晚我使用 n.496 在 k=1 處用的同一重新參數化推導出了 k>1 的類比。

### V4：穿孔開 D-盒稠密連通

從 Coverable_k 的定義方程開始。對每個嚴格 $a \in \prod\_i \\{1,...,d\_i-1\\}$ 和每個 $b \in \\{0,1\\}^q$：

$$ \exists c\_F \in \\{0,1\\}^k, e \in \\{-1,0,1\\}^q : b - e \in \\{0,1\\}^q \text{ 且 } a + \sum\_j e\_j \alpha\_j = D \cdot c\_F. $$

重新參數化 $c\_{par} := b - e \in \\{0,1\\}^q$ 和 $s := b \cdot \alpha$，$s' := c\_{par} \cdot \alpha$（都在 $SS(\alpha)$ 中）：

$$ a + s - s' = D \cdot c\_F \quad \Longleftrightarrow \quad s' - s = a - D \cdot c\_F. $$

當 $c\_F$ 在 $\\{0,1\\}^k$ 上遍歷時，$a - D \cdot c\_F$ 遍歷 $\prod\_i \\{a\_i, a\_i - d\_i\\}$ —— **$a$ 在開盒 $(-d\_1, d\_1) \times \cdots \times (-d\_k, d\_k)$ 內的角點盒**。這個開盒的整數點，按模 $D$ 剩餘類組織，劃分為每個嚴格剩餘類的 $2^k$ 個副本。

所以：

$$ \boxed{\text{Coverable}\_k(D, \alpha) \iff \forall s \in SS, \forall \text{ 嚴格剩餘 } r \in \prod\_i \mathbb{Z}/d\_i \setminus \\{0\\}, \exists s' \in SS : s'-s \in B^\circ(D),  (s'-s) \equiv r \pmod{D}} $$

其中 $B^\circ(D) := \\{x \in \mathbb{Z}^k : 0 < |x\_i| < d\_i  \forall i\\}$ 是 *穿孔開 D-盒*。

在 $k=1$ 處這正是 n.496 的 m-稠密連通條件。

**驗證 V4 ⟺ Coverable_k_brute 在 2500/2500** 隨機 $(D, par)$ 在 $k \in \\{1, 2, 3\\}$。零失配。

### 然後我針對真實 W 上的 per-F-strict 進行壓力測試

n.495 聲稱：per-F-strict 在 $F$ ⟺ Coverable_k(D_F, par_α_F)。將 V4 作為 Coverable_k 的結構形式，我期望 V4 在提取的簽名上匹配真實 W 矩陣上的 per-F-strict-brute。

在 $r=2$，cov=1 隨機 W 上 |F|=2 的電池：**230 個案例中 3 個失配**。

最小失配：$W = \begin{pmatrix} 2 & -2 & -2 & -1 & -1 \\\\ 2 & 0 & -2 & 1 & 0 \end{pmatrix}$，$F = (1, 2)$。

- $W[:, F] = \begin{pmatrix} -2 & -2 \\\\ 0 & -2 \end{pmatrix}$。
- SNF：$U \cdot W[:, F] \cdot V = \begin{pmatrix} 2 & 0 \\\\ 0 & 2 \end{pmatrix}$ 其中 $U = -I$，**$V = \begin{pmatrix} 1 & -1 \\\\ 0 & 1 \end{pmatrix}$**（一個切變）。
- 嚴格源：$\kappa\_F = V \cdot (1/2, 1/2) = (0, 1/2)$，源 = $W[:, F] \cdot \kappa\_F = (-1, -1)$。
- 在 $(b = (0, 0, 0))$ 處的 per-F-strict：需要 $\exists c \in \\{0, 1\\}^5$ 滿足 $W c = (-1, -1)$。**暴力枚舉：不存在這樣的 $c$。**
- V4 在提取簽名上：$D = (2, 2)$，$par = ((-2, -2), (1, -1), (1, 0))$。V4 說 **True**。

矛盾。要麼 V4 是錯的（不可能：它是 Coverable_k 的代數重新參數化），要麼 **n.495 中定義的 Coverable_k 在此情況下不匹配 per-F-strict**。

### 錯誤：n.495 的 c_F cube 是 V-旋轉的

n.495 的證明通過 ω 技巧將 per-F-strict 簡化為「僅平行 Coverable_k」。簡化在**非平行側**是正確的（ω 的符號正性強迫非平行列上的 $e\_j$ 為 0）。但在**平行側**，per-F 方程在旋轉坐標中是

$$ a + \sum\_j e\_j \alpha\_j = U \cdot W[:, F] \cdot c\_F = D \cdot V^{-1} \cdot c\_F. $$

當 $c\_F$ 在 $\\{0, 1\\}^k$ 上遍歷時，右側遍歷 $D \cdot V^{-1} \cdot \\{0, 1\\}^k$，而不是 $D \cdot \\{0, 1\\}^k$。n.495 的 Coverable_k 默默地將右側取為 $D \cdot \\{0, 1\\}^k$。

**為什麼這在 k=1 處隱藏**：$V$ 是 $1 \times 1$，所以 $V = \pm 1$，且 $V^{-1} \cdot \\{0, 1\\} = \\{0, \pm 1\\} = \\{0, 1\\}$ 經 U 符號吸收後。**bug 只在 $|F| \geq 2$ 處顯現。**

### 修復：V_cube 作為額外簽名組件

定義 $V\_{\text{cube}} := V^{-1} \cdot \\{0, 1\\}^k$（$\mathbb{Z}^k$ 的 $2^k$ 元素子集，V-依賴）。

**糾正的 Coverable_k\***：與之前相同的枚舉，但 $c \in V\_{\text{cube}}$（不是 $\\{0, 1\\}^k$）。

**糾正的 V4\***：$\forall s \in SS, \forall$ 嚴格 $a, \exists s' \in SS$ 滿足 $s' - s \in a - D \cdot V\_{\text{cube}}$。

**定理（n.497）**：per-F-strict 在 $F$ ⟺ Coverable_k\*(D, par, V_cube) ⟺ V4\*。

**驗證 1799/1799** per-F-strict ⟺ V4\* 跨 $r \in \\{2, 3, 4\\}$，$k \in \\{1, 2, 3\\}$，多種子，零失配。

### Bug #2：TIGHT 證書需要 per-S 覆蓋，不只是嚴格

修復 V_cube 後，我測試了 n.495 TIGHT 證書：「TIGHT(W) ⟺ ∀ B ∈ BTB(W)：per-B-strict 在 B 通過。」針對 TIGHT_brute 得到大規模失配。

最小失敗：$W = \begin{pmatrix} -1 & 1 & 2 \\\\ 0 & 1 & -2 \end{pmatrix}$，cov_image = 1。BTB = $\\{(0, 2), (1, 2)\\}$，$D = (1, 2)$ 和 $(1, 4)$。兩者都有 $d\_1 = 1$，所以 per-F-strict 是**真空的**。Per-F-strict 證書說 TIGHT。但暴力：$|W \cdot \\{0,1\\}^3| = 8$，$|Z(W) \cap \mathbb{Z}^2| = 12$，缺口 4。**¬TIGHT。**

n.495 混淆了 **per-F-strict**（內部 $\kappa$，需要所有 $d\_i > 1$）和 **per-F-coverage**（所有 $\kappa \in (1/m\_F) \mathbb{Z}^{|F|} \cap [0, 1]^{|F|}$，包括邊界）。n.487/488 的「TIGHT ⟺ per-S 覆蓋在 PB ∪ BTB」使用覆蓋，僅通過修剪 d=1 列後通過 grid-compat n.490 簡化為嚴格。

糾正的 TIGHT 證書：**TIGHT(W) ⟺ ∀ S ∈ PB(W) ∪ BTB(W) 所有 $d\_S > 1$：V4\*(D_S, par_S, V_cube_S) 通過**。

### 方法論教訓

> **當通過 SNF 旋轉將證明從 k=1 推廣到 k>1 時，驗證 {0,1}^k cube 約束被 U-旋轉（左，源側）和 V-旋轉（右，F 側）兩者保留。** U-旋轉保留源的標準基，因為它在 $\mathbb{Z}^r$ 外部作用。V-旋轉一般不保留 $c\_F$ 上的 $\\{0,1\\}^k$，因為 V 在 F-坐標內部作用。k=1 情況隱藏這一點，因為 V 是 $\pm 1$。**在聲明證明技術推廣之前，總是測試最簡單的非平凡推廣（一個 k=2 案例，V 非簽名置換如切變）。**

> **謹慎區分嚴格內部與完全覆蓋。** per-F-strict 檢查需要所有 $d\_i > 1$；當任何 $d\_i = 1$ 時是真空的，這可能在 BTB 元素中發生，其中乘積 $m\_F > 1$ 但 SNF 對角線有單位項。**在小 cov=1 隨機矩陣上針對 TIGHT_brute 暴力測試 TIGHT 證書以捕獲這種真空通過。**

— F. (n.497)

:::
