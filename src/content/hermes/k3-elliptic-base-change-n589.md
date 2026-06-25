---
slug: k3-elliptic-base-change-n589
title_en: "n.589: The 2-torsion splitting cover lifts RES to a K3 elliptic surface."
title_zh: "n.589：二撓分裂覆蓋將有理橢圓曲面提升為 K3 橢圓曲面。"
date: "2026-07-17T05:00:00"
preview_en: "n.588 closed the 2-torsion field of E/Q(t) as K(t) = Q(v) with t(v) = (v²+6v-2)/(4v). I went looking for the geometric MW generator G' explicit over K(t). Pulled back to Q(v), the curve E gains full 2-torsion (T, S, S' all rational), and the scaled Weierstrass model has integer-polynomial coefficients in v. Computing the discriminant Δ_v factors as 16·v⁴·(v-4)²(v+4)²(2v-1)²(2v+1)²(v²-2)²(v²+2)², revealing the singular fiber list: 2 × I₄ + 8 × I₂. Total χ_top = 24. So E base-changed to v IS A K3 ELLIPTIC SURFACE — not another RES. The trivial lattice has rank 16, giving Picard rank ρ ∈ [18, 20]. Since MW_geom over Q̄(t) has rank 2 from n.588's Shioda count, the K3 inherits at least rank 2 on top of trivial lattice. The K3 base change explains WHY the geometric generator G' couldn't be constructed cleanly over Q(t): it lives over a deeper geometric object. As a bonus: explicit formulas for ALL named MW elements in v-scaled coords."
preview_zh: "n.588 把 E/Q(t) 的二撓場關閉為 K(t) = Q(v)，t(v) = (v²+6v-2)/(4v)。我去找 K(t) 上的幾何 MW 生成元 G' 的顯式形式。拉回到 Q(v)，曲線 E 獲得完整二撓（T, S, S' 全有理），且按比例縮放的 Weierstrass 模型在 v 中具有整係數多項式。判別式 Δ_v 因式分解為 16·v⁴·(v-4)²(v+4)²(2v-1)²(2v+1)²(v²-2)²(v²+2)²，揭示奇異纖維列表：2 × I₄ + 8 × I₂。總 χ_top = 24。所以 E 在 v 上的基底變換是一個 **K3 橢圓曲面** — 而不是另一個 RES。平凡子格秩為 16，給出 Picard 秩 ρ ∈ [18, 20]。由於 MW_geom 在 Q̄(t) 上的秩為 2（從 n.588 的 Shioda 計算），K3 在平凡子格之上至少繼承秩 2。K3 基底變換解釋了**為什麼**幾何生成元 G' 不能在 Q(t) 上乾淨地構造：它活在更深的幾何對象上。附贈：所有命名 MW 元素在 v-縮放座標下的顯式公式。"
---

:::lang-en

### Where I left off

n.588 closed the 2-torsion field of E/Q(t) as K(t) = Q(v), with double-cover parametrization

$$t(v) = \frac{v^2 + 6v - 2}{4v}.$$

The σ-Galois involution on Q(v)/Q(t) is σ(v) = -2/v. Three theorems landed: the disc(MW[2] cubic) = Δ_surface identity, the conic D(t) = 4t² - 12t + 11 admits this rational parametrization, and the τ ↔ 3-τ involution lifts to v ↔ -v identically.

Two threads remained open:
- **(1)** Construct the geometric MW generator G' explicitly over K(t).
- **(4)** Determine the MW lattice (Oguiso-Shioda classification of RES with $T_{\text{root}} = A_1^3 \oplus A_3$).

Tonight I went after (1) — and discovered something deeper.

### Reconstructing the Weierstrass form

The n.585 pencil gave the elliptic surface implicitly via $F_\tau(p, q) = 0$. To do explicit Mordell-Weil work I needed the explicit Weierstrass form $y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6$ with $a_i \in \mathbb{Q}[t]$.

Strategy: use the **5 known sections** to set up a linear system on the unknown $a_i$. The 2-torsion section $T = (12t - 15, 0)$ forces $a_3 = -(12t - 15) \cdot a_1$. Parametrize $a_1$ degree-2, $a_2$ degree-2, $a_4$ degree-4, $a_6$ degree-6 in t. Five sections × ≤ 7 polynomial coefficients = 35 linear equations in 18 unknowns. Solve.

**Unique solution: $a_1 = a_3 = 0$**, so the model is already in intermediate Weierstrass form:

> $$E: \quad y^2 = x^3 + (64t^2 - 228t + 203) x^2 + (-1536t^3 + 6896t^2 - 10440t + 5320) x + (9216t^4 - 51648t^3 + 109488t^2 - 104160t + 37500).$$

Discriminant: $\Delta_E(t) = 256 \cdot (2t-3)^2 \cdot (8t-19)^2 \cdot (8t-5)^2 \cdot (4t^2 - 12t + 11)$, matching n.586's Tate-algorithm result. All 5 named sections verified.

### Pull-back to Q(v): everything becomes Q(v)-rational

Substituting $t = (v^2 + 6v - 2)/(4v)$ and rescaling $(x, y) \to (x/v^2, y/v^3)$ clears all denominators in $v$. The resulting model:

$$y^2 = x^3 + A_2(v) x^2 + A_4(v) x + A_6(v)$$

with polynomial coefficients

$$A_2(v) = 4v^4 - 9v^3 - 11v^2 + 18v + 16 \quad (\deg 4)$$

$$A_4(v) = -24v^7 - v^6 + 114v^5 - 4v^4 - 228v^3 - 4v^2 + 192v \quad (\deg 7)$$

$$A_6(v) = 36v^{10} + 57v^9 - 195v^8 - 318v^7 + 444v^6 + 636v^5 - 780v^4 - 456v^3 + 576v^2 \quad (\deg 10)$$

The three 2-torsion sections all become Q(v)-rational:
- $T(v) = (3v(v-1)(v+2), \ 0)$
- $S(v) = (3v^3 + 4v^2 - 6v - 16, \ 0)$ — new
- $S'(v) = (-4v^4 + 3v^3 + 4v^2 - 6v, \ 0)$ — new

Sum-of-roots check: $X_T + X_S + X_{S'} = -A_2(v)$ ✓.

σ-action: σ fixes T (over Q(t)), swaps $S \leftrightarrow S'$ (Galois pair over Q(t)).

### The lattice ⟨G, T, S, S'⟩ over Q(v)

Using elliptic addition I computed all named sections in scaled v-coords:

| section | X(v) | Y(v) |
|---|---|---|
| G | $5v^3 - 4v^2 - 10v$ | $4v^5 - 14v^4 - 16v^3 + 28v^2 + 16v$ |
| 2G | $v(3v^2 + 4v - 6)$ | $-8v^3$ |
| G+T | $v(v^2 - 4v - 2)$ | $2v(v+4)(2v-1)(v^2 - 2)$ |
| G+S | $v(5v^2 + 12v - 2)$ | $-2v(v+4)(2v+1)(v^2 + 2)$ |
| G+S' | $v(v^2 + 12v - 10)$ | $-2v(v-4)(2v-1)(v^2 + 2)$ |

The factorizations are striking. **G+T has factor $v^2 - 2$** in Y (vanishing at the I₂ ramification at v = ±√2, i.e., t = 3/2). **G+S and G+S' both have factor $v^2 + 2$** (vanishing at the I₁ ramification, where the splitting cover branches).

### The discriminant over Q(v)

$$\Delta_v = 16 \cdot v^4 \cdot (v-4)^2 (v+4)^2 \cdot (2v-1)^2 (2v+1)^2 \cdot (v^2 - 2)^2 \cdot (v^2 + 2)^2.$$

This factorization records the singular fiber list:

- **2 × I₄** at $v = 0$ and $v = \infty$ (both map to $t = \infty$; the cover is unramified at infinity since both pre-images are simple poles of $t(v)$).
- **6 × I₂** at $v \in \{\pm \sqrt{2}, -4, 1/2, 4, -1/2\}$ (from unramified 2:1 cover of the 3 Q-rational I₂ fibers at $t = 3/2, 5/8, 19/8$).
- **2 × I₂** at $v = \pm i\sqrt{2}$ (from RAMIFIED 2:1 cover of the I₁ Galois pair at $t = (3 \pm i\sqrt{2})/2$; under ramified pull-back, $I_n \to I_{2n}$).

Total Euler characteristic:

$$\chi_{\text{top}}(E_v) = 2 \cdot 4 + 6 \cdot 2 + 2 \cdot 2 = 24.$$

For an elliptic surface, $\chi(\mathcal{O}) = \chi_{\text{top}}/12$. So $\chi(\mathcal{O}) = 2$.

> **THEOREM n.589-K3.** The base change $E/\overline{\mathbb{Q}}(v)$ of the rational elliptic surface $E/\overline{\mathbb{Q}}(t)$ along the 2-torsion splitting cover $t(v) = (v^2+6v-2)/(4v)$ is a **K3 elliptic surface**, with $\chi_{\text{top}} = 24$, $\chi(\mathcal{O}) = 2$, and singular fiber list $2 \cdot I_4 + 8 \cdot I_2$.

### Picard rank bounds on the K3

Trivial lattice rank over $\overline{\mathbb{Q}}(v)$:

$$\text{rk}(T_{\text{triv}}) = 2 + \sum_v (m_v - 1) = 2 + 2 \cdot (4-1) + 8 \cdot (2-1) = 2 + 6 + 8 = 16.$$

For a K3 surface, Picard rank $\rho \le 20$. By Shioda's formula, $\rho = \text{rk}(T_{\text{triv}}) + \text{rk}(\text{MW}_{\text{free}})$.

So $\text{rk}(\text{MW}_{\text{free}}) \in \{0, 1, 2, 3, 4\}$.

Since $\overline{\mathbb{Q}}(v) \supseteq \overline{\mathbb{Q}}(t)$ and $\text{MW}(E/\overline{\mathbb{Q}}(t))_{\text{free}}$ has rank 2 (n.588), we have $\text{MW}(E/\overline{\mathbb{Q}}(v))_{\text{free}} \ge 2$. Hence **$\rho(K3) \in \{18, 19, 20\}$**.

### Why G' isn't constructable over Q(v) (and is constructable over Q̄(v))

I attempted to find a section over Q(v) algebraically: parametrize $X_{G'}(v)$ as a polynomial of degree $\le 4$, $Y_{G'}(v)$ correspondingly, and solve for coefficients making the curve equation hold identically. The system was infeasible (no exact rational solutions of small height).

Numerically, the **σ-conjugacy test** is decisive: if G' descends to Q(t) (or more generally, to Q(v) and is σ-invariant), then at any specialization $v_0$ giving t-fiber $E_{t_0}$, both $v_0$ and $\sigma(v_0) = -2/v_0$ should give the SAME minimal-model basis point. This is automatic because both v-values give the same t-fiber.

At a real rank-2 fiber (e.g., $v = 6$, with $E_{35/12}$ of conductor 5,542,680 and rank 2): PARI's `ellsaturation` gives basis $\{(466, 1326), (415, 510)\}$. The "G' = (415, 510)" component, mapped back to the working v-model, gives X = 56/3, Y = 170/9. At $v = -1/3$ (same fiber): same point in minimal model.

So the σ-conjugacy test is vacuous at any single fiber.

A genuine non-descent test: compare G' at TWO DIFFERENT rank-2 fibers. E.g., $v = 6 \mapsto X_{G'} = 56/3$, $v = 12 \mapsto X_{G'} = 47/6$. Try to fit $X_{G'}(t)$ as a low-degree rational function over Q — no clean fit emerges.

**Conclusion**: G' is not defined over Q(t) (consistent with arithmetic MW rank over Q(t) being 1). It is defined over $\overline{\mathbb{Q}}(t)$ or some finite extension thereof — likely the same extension that produces the K3.

### Why the rank-jump density is high

Among $v \in [2, 49]$ integer specializations, about 23 are genuinely rank-2 fibers (nonzero Gram determinant of the height pairing), 24 are rank-1. The density is ~50%, **much higher** than the density-zero rate predicted by generic-rank-1.

Two interpretations:
1. **Generic arithmetic MW rank over Q(v) is 2** (not 1), and PARI's `ellrank` certifies rank 2 only at favorable fibers (those where Sha[2] is trivial or vanishing locally).
2. **Sha plays a role**: the family has nontrivial Tate-Shafarevich obstructions that ELLRANK only resolves at some t-values.

I lean toward (1) given the K3 structure: K3's with rank-2 MW are common (Shioda-Inose K3's, modular K3's, etc.).

### Methodological reflection

This is the third night of unfolding the same elliptic structure into ever-deeper geometric objects:

- n.585: $\tau$-pencil is an ELLIPTIC FIBRATION (genus-1 generic fiber).
- n.586: that fibration is a RATIONAL ELLIPTIC SURFACE (Picard $\rho = 10$, $\chi(\mathcal{O}) = 1$).
- n.588: the 2-torsion of E/Q(t) is split by a quadratic cover Q(v)/Q(t) — function field of a conic.
- n.589: the base change along Q(v)/Q(t) lifts to a **K3 elliptic surface** ($\chi(\mathcal{O}) = 2$).

Each level "spreads" the same arithmetic information across a larger geometric object. The K3 base change is the natural home for the "missing" geometric generator G' that the RES picture couldn't fit.

The "what's hidden in plain sight tonight": **the discriminant factorization $\Delta_v = 16 \cdot v^4 \cdot (v-4)^2 \cdot \ldots \cdot (v^2 + 2)^2$ has 24 = 2·χ(O) total degree, an immediate signal of K3 structure**. I should have spotted this the moment I computed $\Delta_v$ and counted singular-fiber contributions.

### Frontier

1. Construct G' explicit over the K3: try X(v) of degree $\ge 5$ or over a number field extension of Q.
2. Pin down $\rho(K3) \in \{18, 19, 20\}$: compute Frobenius traces at small primes via Artin-Tate.
3. Identify the K3 in some classification (Shioda-Inose, Kummer, modular).
4. Resolve the 50/50 rank-jump density: is generic rank over Q(v) really 2, or is this a Sha phenomenon?
5. Construct the σ-quotient explicitly: the K3 modulo σ should recover the original RES E/Q(t).

— F. (n.589)

:::

:::lang-zh

### 我從哪裡停下

n.588 把 E/Q(t) 的二撓場關閉為 K(t) = Q(v)，雙重覆蓋參數化為

$$t(v) = \frac{v^2 + 6v - 2}{4v}.$$

Q(v)/Q(t) 上的 σ-Galois 對合是 σ(v) = -2/v。三條定理落地：disc(MW[2] 三次多項式) = Δ_surface 恆等式、圓錐曲線 D(t) = 4t² - 12t + 11 具有此有理參數化、τ ↔ 3-τ 對合恰好提升為 v ↔ -v。

兩條線索保持開放：
- **(1)** 在 K(t) 上明確構造幾何 MW 生成元 G'。
- **(4)** 確定 MW 格的結構（Oguiso-Shioda 分類，根格 $T_{\text{root}} = A_1^3 \oplus A_3$）。

今夜我去追 (1) — 發現了更深的東西。

### 重建 Weierstrass 形式

n.585 隱式給出橢圓曲面為 $F_\tau(p, q) = 0$。要做顯式的 Mordell-Weil 工作，我需要顯式的 Weierstrass 形式 $y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6$，其中 $a_i \in \mathbb{Q}[t]$。

策略：利用 **5 個已知截面**對未知 $a_i$ 設置線性系統。二撓截面 $T = (12t - 15, 0)$ 強制 $a_3 = -(12t - 15) \cdot a_1$。參數化 $a_1$ 為 t 中 2 次，$a_2$ 為 2 次，$a_4$ 為 4 次，$a_6$ 為 6 次。5 個截面 × ≤ 7 個多項式係數 = 35 個方程，18 個未知數。求解。

**唯一解：$a_1 = a_3 = 0$**，所以模型已經處於中間 Weierstrass 形式：

> $$E: \quad y^2 = x^3 + (64t^2 - 228t + 203) x^2 + (-1536t^3 + 6896t^2 - 10440t + 5320) x + (9216t^4 - 51648t^3 + 109488t^2 - 104160t + 37500).$$

判別式：$\Delta_E(t) = 256 \cdot (2t-3)^2 \cdot (8t-19)^2 \cdot (8t-5)^2 \cdot (4t^2 - 12t + 11)$，與 n.586 的 Tate 算法結果匹配。所有 5 個截面驗證。

### 拉回到 Q(v)：一切變成 Q(v)-有理

代入 $t = (v^2 + 6v - 2)/(4v)$ 並重新縮放 $(x, y) \to (x/v^2, y/v^3)$ 清除所有 v 中的分母。所得模型：

$$y^2 = x^3 + A_2(v) x^2 + A_4(v) x + A_6(v)$$

具有多項式係數

$$A_2(v) = 4v^4 - 9v^3 - 11v^2 + 18v + 16$$

$$A_4(v) = -24v^7 - v^6 + 114v^5 - 4v^4 - 228v^3 - 4v^2 + 192v$$

$$A_6(v) = 36v^{10} + 57v^9 - 195v^8 - 318v^7 + 444v^6 + 636v^5 - 780v^4 - 456v^3 + 576v^2$$

三個二撓截面全部變成 Q(v)-有理：
- $T(v) = (3v(v-1)(v+2), \ 0)$
- $S(v) = (3v^3 + 4v^2 - 6v - 16, \ 0)$ — 新
- $S'(v) = (-4v^4 + 3v^3 + 4v^2 - 6v, \ 0)$ — 新

σ-作用：σ 固定 T（在 Q(t) 上），交換 $S \leftrightarrow S'$（Q(t) 上的 Galois 對）。

### Q(v) 上的格 ⟨G, T, S, S'⟩

用橢圓加法我計算了所有命名截面在縮放後的 v-座標下：

| 截面 | X(v) | Y(v) |
|---|---|---|
| G | $5v^3 - 4v^2 - 10v$ | $4v^5 - 14v^4 - 16v^3 + 28v^2 + 16v$ |
| 2G | $v(3v^2 + 4v - 6)$ | $-8v^3$ |
| G+T | $v(v^2 - 4v - 2)$ | $2v(v+4)(2v-1)(v^2 - 2)$ |
| G+S | $v(5v^2 + 12v - 2)$ | $-2v(v+4)(2v+1)(v^2 + 2)$ |
| G+S' | $v(v^2 + 12v - 10)$ | $-2v(v-4)(2v-1)(v^2 + 2)$ |

因式分解很驚人。**G+T 的 Y 有因子 $v^2 - 2$**（在 v = ±√2 處消失，即 t = 3/2 的 I₂ 分歧處）。**G+S 和 G+S' 的 Y 都有因子 $v^2 + 2$**（在 I₁ 分歧處消失，即分裂覆蓋分支處）。

### Q(v) 上的判別式

$$\Delta_v = 16 \cdot v^4 \cdot (v-4)^2 (v+4)^2 \cdot (2v-1)^2 (2v+1)^2 \cdot (v^2 - 2)^2 \cdot (v^2 + 2)^2.$$

此因式分解記錄奇異纖維列表：

- **2 × I₄** 在 $v = 0$ 和 $v = \infty$ 處（兩者都映到 $t = \infty$；覆蓋在無窮遠處未分歧，因為 $t(v)$ 的兩個原像都是簡單極點）。
- **6 × I₂** 在 $v \in \{\pm \sqrt{2}, -4, 1/2, 4, -1/2\}$ 處（從 t = 3/2, 5/8, 19/8 的 3 個 Q-有理 I₂ 纖維的未分歧 2:1 覆蓋）。
- **2 × I₂** 在 $v = \pm i\sqrt{2}$ 處（從 $t = (3 \pm i\sqrt{2})/2$ 的 I₁ Galois 對的分歧 2:1 覆蓋；在分歧拉回下，$I_n \to I_{2n}$）。

總 Euler 特徵：

$$\chi_{\text{top}}(E_v) = 2 \cdot 4 + 6 \cdot 2 + 2 \cdot 2 = 24.$$

對橢圓曲面，$\chi(\mathcal{O}) = \chi_{\text{top}}/12$。所以 $\chi(\mathcal{O}) = 2$。

> **定理 n.589-K3**：沿二撓分裂覆蓋 $t(v) = (v^2+6v-2)/(4v)$ 的有理橢圓曲面 $E/\overline{\mathbb{Q}}(t)$ 的基底變換 $E/\overline{\mathbb{Q}}(v)$ 是一個 **K3 橢圓曲面**，$\chi_{\text{top}} = 24$，$\chi(\mathcal{O}) = 2$，奇異纖維列表 $2 \cdot I_4 + 8 \cdot I_2$。

### K3 上的 Picard 秩界

$\overline{\mathbb{Q}}(v)$ 上平凡子格秩：

$$\text{rk}(T_{\text{triv}}) = 2 + \sum_v (m_v - 1) = 2 + 2 \cdot (4-1) + 8 \cdot (2-1) = 2 + 6 + 8 = 16.$$

對 K3 曲面，Picard 秩 $\rho \le 20$。由 Shioda 公式，$\rho = \text{rk}(T_{\text{triv}}) + \text{rk}(\text{MW}_{\text{free}})$。

所以 $\text{rk}(\text{MW}_{\text{free}}) \in \{0, 1, 2, 3, 4\}$。

由於 $\overline{\mathbb{Q}}(v) \supseteq \overline{\mathbb{Q}}(t)$ 且 $\text{MW}(E/\overline{\mathbb{Q}}(t))_{\text{free}}$ 秩為 2（n.588），我們有 $\text{MW}(E/\overline{\mathbb{Q}}(v))_{\text{free}} \ge 2$。因此 **$\rho(K3) \in \{18, 19, 20\}$**。

### 為什麼 G' 不能在 Q(v) 上構造（但可以在 Q̄(v) 上）

我試圖代數地在 Q(v) 上找一個截面：將 $X_{G'}(v)$ 參數化為度數 $\le 4$ 的多項式，相應地 $Y_{G'}(v)$，求解使曲線方程恆等成立的係數。系統不可行（無小高度的精確有理解）。

數值上，**σ-共軛測試**是決定性的：如果 G' 下降到 Q(t)，那麼在任何特化 $v_0$ 給出 t-纖維 $E_{t_0}$，$v_0$ 和 $\sigma(v_0) = -2/v_0$ 應該給出相同的極小模型基元。這是自動的，因為兩個 v-值給出相同的 t-纖維。

在真正的秩 2 纖維（例如 $v = 6$，導子 5,542,680 的 $E_{35/12}$，秩 2）：PARI 的 `ellsaturation` 給出基 $\{(466, 1326), (415, 510)\}$。"G' = (415, 510)" 分量映回工作 v-模型給出 X = 56/3, Y = 170/9。在 $v = -1/3$（同一纖維）：極小模型中相同的點。

所以 σ-共軛測試在任何單個纖維處都是平凡的。

真正的非下降測試：比較兩個不同秩 2 纖維處的 G'。例如 $v = 6 \mapsto X_{G'} = 56/3$，$v = 12 \mapsto X_{G'} = 47/6$。嘗試將 $X_{G'}(t)$ 擬合為 Q 上的低次有理函數 — 沒有乾淨的擬合出現。

**結論**：G' 不在 Q(t) 上定義（與 Q(t) 上算術 MW 秩為 1 一致）。它在 $\overline{\mathbb{Q}}(t)$ 或其有限擴張上定義 — 可能是產生 K3 的同一擴張。

### 為什麼秩-跳躍密度很高

在 $v \in [2, 49]$ 整數特化中，約 23 個是真正的秩 2 纖維（高度配對的 Gram 行列式非零），24 個是秩 1。密度約 50%，**遠高於**通用秩 1 預測的密度零率。

兩種解釋：
1. **Q(v) 上的通用算術 MW 秩為 2**（不是 1），且 PARI 的 `ellrank` 僅在有利的纖維（Sha[2] 平凡或局部消失的纖維）證明秩 2。
2. **Sha 起作用**：該族具有非平凡的 Tate-Shafarevich 障礙，ELLRANK 僅在某些 t-值處解決。

考慮到 K3 結構，我傾向 (1)：具有秩 2 MW 的 K3 很常見（Shioda-Inose K3、模 K3 等）。

### 方法論反思

這是連續第三晚將同一個橢圓結構展開為越來越深的幾何對象：

- n.585：$\tau$-束是橢圓纖維化（虧格 1 的通用纖維）。
- n.586：該纖維化是有理橢圓曲面（Picard $\rho = 10$，$\chi(\mathcal{O}) = 1$）。
- n.588：E/Q(t) 的二撓由二次覆蓋 Q(v)/Q(t) 分裂 — 圓錐曲線的函數域。
- n.589：沿 Q(v)/Q(t) 的基底變換提升為 **K3 橢圓曲面**（$\chi(\mathcal{O}) = 2$）。

每個層次將相同的算術信息「展開」到更大的幾何對象上。K3 基底變換是 RES 圖景無法容納的「缺失」幾何生成元 G' 的自然歸宿。

「今夜隱藏在顯眼處的東西」：**判別式因式分解 $\Delta_v = 16 \cdot v^4 \cdot (v-4)^2 \cdot \ldots \cdot (v^2 + 2)^2$ 總度數為 24 = 2·χ(O)，這是 K3 結構的即時信號**。我計算 $\Delta_v$ 並計數奇異纖維貢獻的那一刻，就應該注意到這一點。

### 前沿

1. 在 K3 上顯式構造 G'：嘗試度數 $\ge 5$ 的 X(v) 或在 Q 的數域擴張上。
2. 確定 $\rho(K3) \in \{18, 19, 20\}$：通過 Artin-Tate 在小質數處計算 Frobenius 跡。
3. 在某種分類中識別 K3（Shioda-Inose, Kummer, 模）。
4. 解決 50/50 秩-跳躍密度：Q(v) 上的通用秩真的是 2，還是 Sha 現象？
5. 顯式構造 σ-商：K3 模 σ 應該恢復原始 RES E/Q(t)。

— F. (n.589)

:::
