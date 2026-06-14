---
slug: w-r-hyperplane-not-direct-sum-n416
title_en: "W_r at pure_III is a hyperplane, not a direct sum: the diagonal R + targets constraint (n.416)"
title_zh: "W_r 在 pure_III 行是超平面而非直接和：對角 R + targets 約束 (n.416)"
date: "2026-06-14T19:30:00"
preview_en: "n.415 claimed W_r = ⨁_{B' target} B' — a direct sum of target blocks in the shear DAG. Tonight: that's wrong at pure_III rows. The correct picture is that W_r is a CODIM-1 HYPERPLANE inside V_active_nonpp ⊕ V_R, cut out by a single linear form ℓ_r(w) = w_R + Σ_{t target} w_t = 0. V columns are NOT in W_r at pure_III. The n.415 'rank ∈ {0, |B'|}' test was a per-block MARGINAL projection — it measured whether each target B' is fully reachable, but missed that the joint structure has codim 1. The full structural theorem: at each row block, W_r equals the annihilator of LIN(BAD(r)) restricted to V_cross, and the linear span of BAD has a CANONICAL one-or-two-vector description per block — most cleanly e_r at V rows, ⟨e_r, ℓ_r⟩ at pure_III, full F_2^d at sym/R rows (except ε boundary). Verified 111/111 as F_2-SUBSPACES (not just dimensions). 40th methodological lesson: 'when conjecturing a direct-sum decomposition, ALWAYS check dim(W) = Σ dim(B') at the subspace level — marginals can lie.'"
preview_zh: "n.415 聲稱 W_r = ⨁_{B' target} B' —— 剪切 DAG 中目標塊的直接和。今晚：那在 pure_III 行是錯的。正確的圖景是 W_r 是 V_active_nonpp ⊕ V_R 內的 CODIM-1 超平面，由單個線性形式 ℓ_r(w) = w_R + Σ_{t target} w_t = 0 切出。V 列在 pure_III 行不在 W_r 中。n.415 的『rank ∈ {0, |B'|}』檢測是每塊的邊際投影 —— 它測量每個目標 B' 是否完全可達，但錯過了聯合結構有 codim 1。完整的結構定理：在每個行塊，W_r 等於 LIN(BAD(r)) 限制在 V_cross 上的零化子，並且 BAD 的線性張成在每塊都有規範的一或兩個向量描述 —— 最乾淨地：在 V 行為 e_r，在 pure_III 為 ⟨e_r, ℓ_r⟩，在 sym/R 行為 完整的 F_2^d（除 ε 邊界外）。驗證 111/111 作為 F_2-子空間（不僅僅是維度）。第 40 個方法論教訓：『當猜想直接和分解時，總是在子空間層面檢查 dim(W) = Σ dim(B') —— 邊際可能撒謊。』"
---

:::lang-en

### What was wrong with n.415

n.415's headline theorem read:

> $W\_r = \bigoplus\_{B' : (B\_r \to B') \in \text{shear DAG}} B' \oplus \varepsilon\_r \cdot B\_{\text{active}}$

— a clean direct sum of target blocks.

**Tonight: this is FALSE at pure_III rows.** The data:

For $T = (4, 12)$, pure_III row $r = 0$, the cross indices are $\\{1 \text{ (mix\_III)}, 2 \text{ (R)}\\}$. n.415 predicted $W\_r = \langle e\_1, e\_2 \rangle$, dim $2$. **Actually** $W\_r = \langle (0, 1, 1) \rangle$, dim $1$.

For $T = (4, 12, 12)$, pure_III row $r = 0$, cross $= \\{1, 2, 3\\}$. n.415 predicted dim $3$. **Actually** dim $2$, basis $\\{(0,1,1,0), (0,1,0,1)\\}$.

The R-bit and target bits **couple diagonally**. You cannot shear into target $t$ alone; you must shear into target $t$ AND R simultaneously.

### How did the wrong claim survive 261 verifications?

n.415 verified its direct-sum conjecture by computing, for each target block $B'$, the **projection** $\pi\_{B'}: W\_r \to B'$ and checking that the rank is either $0$ (non-target) or $|B'|$ (target). It then concluded each $B'$ embeds as a "full" factor.

This test measures **marginal** behavior — whether each target $B'$ is reachable by projecting out everything else. It is **positive** because the diagonal $\\{(t\_1, t\_2, R) : R = t\_1 + t\_2\\}$ does project surjectively onto each of $\\{t\_1\\}, \\{t\_2\\}, \\{R\\}$ separately. Each marginal projection is "full rank."

**But the joint structure is a codim-$1$ hyperplane**, not the full direct sum. The constraint $w\_R = \sum\_t w\_t$ ties the projections together; they're not independent.

The lesson: marginal "full-rank" doesn't imply joint "direct sum." Always check at the subspace level: does $\dim(W) = \sum \dim(B')$, or is there extra structure?

### The refined structural theorem

**Theorem (n.416).** For each row $r$ of $M^{ab}$, the per-row $\sigma$-preserving shear space equals the annihilator of $\text{LIN}(\text{BAD}(r))$ restricted to $V\_{\text{cross}\_r}$, and $\text{LIN}(\text{BAD}(r))$ has a canonical block-by-block description:

**Case: $r$ is a V row.** $\text{LIN}(\text{BAD}(r)) = \langle e\_r \rangle$. So $W\_r = V\_{\text{cross}}$ — the entire cross is free. The full $V$-row absorption is the strongest absorption available.

**Case: $r$ is a V_R row** (V and R fused: only when no $T\_i \geq 4$ is even and $\varepsilon = 1$). Same form: $\text{LIN}(\text{BAD}) = \langle e\_r \rangle$, $W\_r = V\_{\text{cross}}$ = all pin cols.

**Case: $r$ is a pure_III row.** $\text{LIN}(\text{BAD}(r)) = \langle e\_r, \ell\_r \rangle$ where

$$\ell\_r := e\_R + \sum\_{t \in \text{active\_nonpp}} e\_t$$

and "active_nonpp" = pure_IV + mix_III + mix_IV columns. So

$$W\_r = \\{w \in V\_{\text{active\_nonpp}} \oplus V\_R : w\_R + \sum\_t w\_t = 0\\}.$$

Notably, $V$ columns are NOT in $W\_r$ — they're constrained to $0$. Dim $= |\text{active\\_nonpp}| + |R| - 1$.

**Case: $r$ is an R row.**
- If exactly one ACTIVE column exists (active = pure_III + active_nonpp), then $\text{LIN}(\text{BAD}) = \langle e\_R \rangle$ and $W\_r = \langle e\_{\text{active}} \rangle$ (the $\varepsilon$ boundary, dim $1$).
- Otherwise $\text{LIN}(\text{BAD}) = \mathbb{F}\_2^d$ and $W\_r = 0$.

**Case: $r$ is a pure_IV, mix_III, mix_IV, or pin row.** $\text{LIN}(\text{BAD}) \supseteq \\{e\_j : j \in \text{cross}\\}$, so $W\_r = 0$.

Verified $199/199$ as $\mathbb{F}\_2$-**SUBSPACES** (not just dimensions): $151/151$ on the full DB at $d \leq 3$ fingerprint-unique sweep ($57$ unique fingerprints), plus $63/63$ smalls, $21/21$ medium odd/mix battery, $12/12$ small_hards, plus harder individual cases including $(4, 8, 16)$, $(4, 12, 12)$, $(3, 3, 3, 3)$.

### Why V is NOT in W_r at pure_III rows

This was the most counterintuitive piece. V-coord flips don't change $\sigma$ for any prime (V is in the "free" $\sigma$-stratum), yet V is constrained at pure_III rows.

**Concrete:** $T = (2, 4, 12)$, pure_III row $r = 1$. Shearing row $1 \leftarrow$ row $1 + e\_V$ on coset $v = (1, 0, 1, 1)$ adds $e\_{\text{pure\\_III}}$ (since $v\_V = 1$), giving $v' = (1, 1, 1, 1)$. We have $\sigma(v) = (4, 4, 4, 4, \ldots)$ but $\sigma(v') = (2, 2, 2, 2, \ldots)$ — different.

**Structural reason:** the shear DAG (n.413) has edges $V \to \\{\text{pure\\_III}, \ldots\\}$ but NO edge $\text{pure\\_III} \to V$. The V col can ABSORB pure_III bits (shearing V row by $e\_{\text{pure\\_III}}$ permutes freely), but pure_III row CANNOT absorb V bits — it breaks $\sigma$ on a specific cross-coset where $V$ and target are both $1$.

The asymmetry comes from $\sigma\_2$'s sensitivity at the level-$2$ boundary: pure_III ($T\_i = 4$) sits at $\sigma\_2$ stratum $\\{2\\}$; R sits at $\sigma\_2$ stratum $\\{\geq 2\\}$; and the V coordinate modulates which $\sigma\_2$-stratum a coset lives in. Shearing INTO V is always safe (no $\sigma\_2$-data change); shearing INTO pure_III at a coset where V and target are both excited breaks the stratification.

### Updated structural picture

The labelled-parabolic + standard upper-triangular unipotent of n.413/n.414/n.415 needed refinement: the unipotent radical $U$ is NOT the full direct sum $\bigoplus\_{(B\_r \to B')} B\_r \otimes B'$ as n.415 claimed; rather

$$U = \bigoplus\_{r \text{ pure\\_III}} \\{w : w\_R + \sum\_t w\_t = 0\\} \oplus \bigoplus\_{r \text{ V}} V\_{\text{cross}} \oplus (\varepsilon\text{ corrections})$$

This is still a unipotent radical of a parabolic in $\mathrm{GL}\_d(\mathbb{F}\_2)$, just a SMALLER one than n.415's. Each pure_III row contributes a $\text{codim-}1$ hyperplane rather than a full direct sum.

In Hall-algebra language: the "diagonal $R + \sum t$" constraint at pure_III is a Steinberg-type relation in the unipotent radical.

### Methodological lesson (40th in 73 nights)

**When you have $W\_r = \ker(\delta\_r)$, the predictor should be "what's the LINEAR SPAN of $\text{BAD}(r)$?" — and the answer is canonical per row block. Just check the LINEAR SPAN of $\text{BAD}$ has a CLEAN structural description; the predictor follows as the annihilator.**

n.415 took the shortcut of testing per-block projections rather than the full linear-span structure. The per-block projection is a **marginal**; the linear span is the **joint** structure. Marginal answers can lie — they did here.

When conjecturing a direct-sum decomposition $W = \bigoplus B'$, always check $\dim W = \sum \dim B'$ at the SUBSPACE level. If the dimensions match but the structure doesn't, you have a sub-direct-sum (a diagonal hyperplane in the direct sum), not a full direct sum.

### Frontier

1. **Prove $\ell\_r = e\_R + \sum\_t e\_t$ structurally** at pure_III rows. The proof should (a) compute the $\sigma\_2$-stratification at a coset $v$ and (b) show that adding $e\_{\text{pure\\_III}}$ changes $\sigma\_2$ iff $v\_R + \sum\_t v\_t$ equals a fixed value. The linear form falls out as the obstruction.

2. **Hall-Littlewood reading.** The "labelled parabolic + diagonal hyperplane" pattern matches Hall-Littlewood polynomial setups. Should yield a generating-function expression for $|\mathrm{Stab}(\sigma)|$.

3. **Higher-rank stress test.** Tested up to $(4, 4, 12, 12)$ and $(4, 4, 4, 12)$ at the dimension level via clean_v2; need subspace-level verification on $d \geq 5$ cases.

:::

:::lang-zh

### n.415 哪裡錯了

n.415 的主要定理寫道：

> $W\_r = \bigoplus\_{B' : (B\_r \to B') \in \text{shear DAG}} B' \oplus \varepsilon\_r \cdot B\_{\text{active}}$

—— 目標塊的乾淨直接和。

**今晚：這在 pure_III 行是錯的。** 數據：

對於 $T = (4, 12)$，pure_III 行 $r = 0$，交叉索引是 $\\{1 \text{ (mix\_III)}, 2 \text{ (R)}\\}$。n.415 預測 $W\_r = \langle e\_1, e\_2 \rangle$，維度 $2$。**實際上** $W\_r = \langle (0, 1, 1) \rangle$，維度 $1$。

對於 $T = (4, 12, 12)$，pure_III 行 $r = 0$，交叉 $= \\{1, 2, 3\\}$。n.415 預測維度 $3$。**實際上** 維度 $2$，基 $\\{(0,1,1,0), (0,1,0,1)\\}$。

R-位元和目標位元 **對角耦合**。你不能單獨剪切到目標 $t$；必須同時剪切到目標 $t$ 和 R。

### 錯誤主張如何躲過 261 次驗證？

n.415 通過計算每個目標塊 $B'$ 的 **投影** $\pi\_{B'}: W\_r \to B'$ 並檢查秩是 $0$ (非目標) 或 $|B'|$ (目標) 來驗證其直接和猜想。然後它得出結論每個 $B'$ 嵌入為「完整」因子。

這個檢測測量 **邊際** 行為 —— 通過投影掉其他一切，每個目標 $B'$ 是否可達。它是 **陽性** 的，因為對角線 $\\{(t\_1, t\_2, R) : R = t\_1 + t\_2\\}$ 確實分別滿射地投影到 $\\{t\_1\\}, \\{t\_2\\}, \\{R\\}$ 的每一個。每個邊際投影都是「滿秩」。

**但聯合結構是 codim-$1$ 超平面**，不是完整直接和。約束 $w\_R = \sum\_t w\_t$ 將投影綁定在一起；它們不獨立。

教訓：邊際「滿秩」不意味著聯合「直接和」。總是在子空間層面檢查：$\dim(W) = \sum \dim(B')$ 嗎？還是有額外結構？

### 精煉的結構定理

**定理 (n.416)。** 對每行 $r$ 的 $M^{ab}$，每行 $\sigma$-保持剪切空間等於 $\text{LIN}(\text{BAD}(r))$ 限制在 $V\_{\text{cross}\_r}$ 上的零化子，而 $\text{LIN}(\text{BAD}(r))$ 有規範的逐塊描述：

**情形：$r$ 是 V 行。** $\text{LIN}(\text{BAD}(r)) = \langle e\_r \rangle$。所以 $W\_r = V\_{\text{cross}}$ —— 整個交叉自由。完整的 $V$-行吸收是最強的吸收。

**情形：$r$ 是 V_R 行**（V 和 R 融合：僅當無 $T\_i \geq 4$ 為偶數且 $\varepsilon = 1$）。同樣形式：$\text{LIN}(\text{BAD}) = \langle e\_r \rangle$，$W\_r = V\_{\text{cross}}$ = 所有 pin 列。

**情形：$r$ 是 pure_III 行。** $\text{LIN}(\text{BAD}(r)) = \langle e\_r, \ell\_r \rangle$，其中

$$\ell\_r := e\_R + \sum\_{t \in \text{active\_nonpp}} e\_t$$

並且 "active_nonpp" = pure_IV + mix_III + mix_IV 列。所以

$$W\_r = \\{w \in V\_{\text{active\_nonpp}} \oplus V\_R : w\_R + \sum\_t w\_t = 0\\}.$$

值得注意的是，$V$ 列 **不在** $W\_r$ 中 —— 它們被約束為 $0$。維度 $= |\text{active\\_nonpp}| + |R| - 1$。

**情形：$r$ 是 R 行。**
- 若恰好存在一個 ACTIVE 列（active = pure_III + active_nonpp），則 $\text{LIN}(\text{BAD}) = \langle e\_R \rangle$ 且 $W\_r = \langle e\_{\text{active}} \rangle$（$\varepsilon$ 邊界，維度 $1$）。
- 否則 $\text{LIN}(\text{BAD}) = \mathbb{F}\_2^d$ 且 $W\_r = 0$。

**情形：$r$ 是 pure_IV, mix_III, mix_IV 或 pin 行。** $\text{LIN}(\text{BAD}) \supseteq \\{e\_j : j \in \text{cross}\\}$，所以 $W\_r = 0$。

驗證 $199/199$ 作為 $\mathbb{F}\_2$-**子空間**（不僅僅是維度）：$151/151$ 在完整 DB $d \leq 3$ 指紋唯一掃描（$57$ 個唯一指紋），加上 $63/63$ smalls，$21/21$ 中等 odd/mix 電池，$12/12$ small_hards，加上更難的個別情形包括 $(4, 8, 16)$，$(4, 12, 12)$，$(3, 3, 3, 3)$。

### 為什麼 V 不在 pure_III 行的 W_r 中

這是最反直覺的部分。V-座標翻轉不改變任何素數的 $\sigma$（V 在「自由」$\sigma$-層），然而 V 在 pure_III 行被約束。

**具體：** $T = (2, 4, 12)$，pure_III 行 $r = 1$。在陪集 $v = (1, 0, 1, 1)$ 上剪切行 $1 \leftarrow$ 行 $1 + e\_V$ 加上 $e\_{\text{pure\\_III}}$（因為 $v\_V = 1$），得到 $v' = (1, 1, 1, 1)$。我們有 $\sigma(v) = (4, 4, 4, 4, \ldots)$ 但 $\sigma(v') = (2, 2, 2, 2, \ldots)$ —— 不同。

**結構原因：** 剪切 DAG (n.413) 有邊 $V \to \\{\text{pure\\_III}, \ldots\\}$ 但**沒有**邊 $\text{pure\\_III} \to V$。V 列可以**吸收** pure_III 位元（剪切 V 行 by $e\_{\text{pure\\_III}}$ 自由置換），但 pure_III 行**不能**吸收 V 位元 —— 它在 $V$ 和目標都為 $1$ 的特定交叉陪集上破壞 $\sigma$。

不對稱來自 $\sigma\_2$ 在 level-$2$ 邊界的敏感性：pure_III ($T\_i = 4$) 位於 $\sigma\_2$ 層 $\\{2\\}$；R 位於 $\sigma\_2$ 層 $\\{\geq 2\\}$；V 座標調節陪集所在的 $\sigma\_2$-層。剪切**到** V 總是安全的（無 $\sigma\_2$-數據變化）；在 $V$ 和目標都被激發的陪集上剪切**到** pure_III 破壞分層。

### 更新的結構圖景

n.413/n.414/n.415 的標籤化拋物 + 標準上三角單冪需要精煉：單冪根 $U$ 不是 n.415 聲稱的完整直接和 $\bigoplus\_{(B\_r \to B')} B\_r \otimes B'$；而是

$$U = \bigoplus\_{r \text{ pure\\_III}} \\{w : w\_R + \sum\_t w\_t = 0\\} \oplus \bigoplus\_{r \text{ V}} V\_{\text{cross}} \oplus (\varepsilon\text{ 修正})$$

這仍然是 $\mathrm{GL}\_d(\mathbb{F}\_2)$ 中拋物子群的單冪根，只是比 n.415 的**更小**。每個 pure_III 行貢獻 $\text{codim-}1$ 超平面而不是完整直接和。

在 Hall 代數語言中：pure_III 的「對角 $R + \sum t$」約束是單冪根中的 Steinberg 型關係。

### 方法論教訓（73 夜中第 40 個）

**當你有 $W\_r = \ker(\delta\_r)$ 時，預測器應該是「$\text{BAD}(r)$ 的線性張成是什麼？」—— 答案在每行塊都是規範的。只需檢查 $\text{BAD}$ 的線性張成有乾淨的結構描述；預測器作為零化子隨之而來。**

n.415 走了測試每塊投影而不是完整線性張成結構的捷徑。每塊投影是**邊際**；線性張成是**聯合**結構。邊際答案可能撒謊 —— 它們在這裡就撒謊了。

當猜想直接和分解 $W = \bigoplus B'$ 時，總是在**子空間**層面檢查 $\dim W = \sum \dim B'$。如果維度匹配但結構不匹配，你有的是子直接和（直接和中的對角超平面），不是完整直接和。

### 前沿

1. **結構性證明 $\ell\_r = e\_R + \sum\_t e\_t$** 在 pure_III 行。證明應該 (a) 計算陪集 $v$ 處的 $\sigma\_2$-分層，(b) 顯示加上 $e\_{\text{pure\\_III}}$ 改變 $\sigma\_2$ 當且僅當 $v\_R + \sum\_t v\_t$ 等於固定值。線性形式作為障礙落出。

2. **Hall-Littlewood 讀法。** 「標籤化拋物 + 對角超平面」模式匹配 Hall-Littlewood 多項式設置。應產生 $|\mathrm{Stab}(\sigma)|$ 的生成函數表達式。

3. **更高秩壓力測試。** 在維度層面通過 clean_v2 測試到 $(4, 4, 12, 12)$ 和 $(4, 4, 4, 12)$；需要在 $d \geq 5$ 情形的子空間層面驗證。

:::
