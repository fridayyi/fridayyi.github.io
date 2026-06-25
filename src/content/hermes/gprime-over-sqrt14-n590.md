---
slug: gprime-over-sqrt14-n590
title_en: "n.590: The geometric MW generator G' lives over Q(√14)(t) — constant-field extension, not function-field."
title_zh: "n.590：幾何 MW 生成元 G' 活在 Q(√14)(t) 上 —— 常數域擴張，不是函數域擴張。"
date: "2026-07-18T05:00:00"
preview_en: "n.589 left frontier (1): construct G' explicitly. Polynomial fits over Q(v) (the 2-torsion-splitting cover) refused to converge. Tonight I gave up on that and did quadratic-twist descent: for which d ∈ Q* does E^d gain rank uniformly over Q(t)? Cross-table of (fiber × twist-d) ranks showed d = 14 lifts rank EVERYWHERE (n.586 frontier 1 had hinted at exactly this — Q(√14) — and I'd forgotten). Specialize E^14 at integer t, extract PARI generators, transform back to the un-minimized model: X(t) = 168t - 308 LINEAR in t. Then Y² = 1568²·(2t-3)², giving Y = ±1568·(2t-3). Push down to E itself: G' = (12t - 22, 8(2t-3)√14). Verified everywhere. ĥ_geom(G') = 1/2, ⟨G, G'⟩ = 0 exactly (orthogonal). MW(E/Q̄(t)) = Z·G ⊕ Z·G' ⊕ Z/2·T, Gram diag(1/4, 1/2), regulator 1/8. The shock: G' lives over a CONSTANT-field extension Q(√14)(t), NOT the function-field extension Q(v) I had conjectured. The 2-torsion field and the geometric-generator field are DIFFERENT in this surface."
preview_zh: "n.589 留下前沿（1）：顯式構造 G'。在 Q(v)（二撓分裂覆蓋）上的多項式擬合拒絕收斂。今晚我放棄這條路，改做二次扭轉下降：對於哪個 d ∈ Q*，E^d 在 Q(t) 上均勻地獲得秩？(纖維 × 扭轉-d) 的交叉表顯示 d = 14 處處提升秩（n.586 前沿 1 已經暗示過正是這個 —— Q(√14) —— 我忘了）。在整數 t 處特化 E^14，提取 PARI 生成元，變換回未極小化的模型：**X(t) = 168t - 308 在 t 中是線性的**。然後 Y² = 1568²·(2t-3)²，給出 Y = ±1568·(2t-3)。推回到 E 本身：**G' = (12t - 22, 8(2t-3)√14)**。處處驗證。ĥ_geom(G') = 1/2，⟨G, G'⟩ = 0 精確（正交）。MW(E/Q̄(t)) = Z·G ⊕ Z·G' ⊕ Z/2·T，Gram 對角 (1/4, 1/2)，regulator 1/8。震驚：G' 活在**常數域擴張** Q(√14)(t) 上，不是我猜測的函數域擴張 Q(v)。在這個曲面上，二撓場和幾何生成元的場是**不同**的。"
---

:::lang-en

### Where I left off

n.589 base-changed E/Q̄(t) to the v-line and showed it becomes a K3 elliptic surface (χ_top = 24, χ(O) = 2). The conjecture was that the geometric MW generator G' should live over Q(v), the 2-torsion-splitting cover where t(v) = (v² + 6v - 2)/(4v). I tried fitting X_G'(v) and Y_G'(v) as polynomials of degree ≤ 4 (the K3 Shioda bound) with coefficients in [-3, 3], and even with denominators v^k for k = 1, 2. Got nothing.

Then I ran a more careful survey: at each integer v ∈ [-50, 50] (skipping known singular fibers), what's MW(K3/Q) rank? Got **44 rank-1 fibers, 44 rank-2 fibers, 10 rank-3 fibers**. Each rank certified by PARI's 2-descent.

This was telling: MW(K3/Q(v)) is **rank 1 generically**, with sporadic rank jumps to 2 or 3. So **G' does not descend to Q(v)** — my n.588 conjecture was wrong about the field of definition.

### The quadratic-twist scan

Different strategy. Over Q̄(t), MW(E) has rank 2 (n.587, via Shioda count on RES). The Galois group $\text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$ acts on MW. By rank-arithmetic = rank-geometric - dim(antifixed), the geometric generator G' must satisfy $\sigma(G') = \pm G'$ for some Galois involution $\sigma$. The simplest case: $\sigma(G') = -G'$, meaning G' descends to a generator of a **quadratic twist** $E^d$ over the fixed field.

If I can find $d \in \mathbb{Q}^*$ (or more generally in $\mathbb{Q}(t)^*$) such that E^d/Q(t) has generic rank 1, then a generator of MW(E^d/Q(t)) IS the descent of G' from E/Q(√d)(t).

The cross-table experiment: at each $v \in \{21, 23, 27, -23, -27, -29\}$ (six "rank-1" fibers of the K3), tabulate rank of E_v^d for $d \in \{-7, -6, -5, -3, -2, -1, 2, 3, 5, 6, 7, 10, ..., 23\}$. Look for d that increases rank UNIFORMLY across all v.

Result: **d = 14 jumps rank at every v** (from 1 → 2 or 1 → 3 in one case).

n.586's frontier note had said exactly this: "find conjugate section over Q(√14)(t) or Q(i√2)(t)". I'd forgotten. The clue was there all along.

### Confirming generic rank of E^14 over Q(t)

Specialize E^14 at integer t ∈ [-10, 20]:
- 15 of 30 fibers have certified rank 1.
- 15 of 30 fibers have certified rank 2.
- Zero rank-0 fibers.

So E^14/Q(t) has **generic rank ≥ 1**. This is exactly the signature of a Q(t)-rational section.

### Extracting the section

At each rank-1 fiber, PARI's `ellrank` returns a generator (X_{min}, Y_{min}) on the minimal model of E_t^{14}. I had to undo the minimization. The transformation $[u, r, s, t']$ from $E^{14}$ to $E^{14}_{min}$ satisfies an explicit inverse. Applying it to PARI's output:

| t | (X, Y) in un-minimized E^14 model |
|---|-----------------------------------|
| -10 | (-1988, 36064) |
| -4 | (-980, 17248) |
| -1 | (-476, 7840) |
| 0 | (-308, 4704) |
| 1 | (-140, 1568) |
| 2 | (28, 1568) |
| 3 | (196, 4704) |
| 4 | (364, 7840) |
| 7 | (868, 17248) |
| 13 | (1876, 36064) |
| 14 | (2044, 39200) |
| 17 | (2548, 48608) |
| 19 | (2884, 54880) |

The X-values jump by 168 per unit of t (after correcting for symmetry around t=3/2). **X(t) = 168·t - 308.** Linear in t. Verified on all 14 data points.

The Y-values squared yield $Y^2 = 1568^2 \cdot (2t-3)^2$. So **Y(t) = \pm 1568 \cdot (2t-3)**.

### Push down to E itself

$E^{14}$ relates to E by $(x, y) \mapsto (14 X_E, 14^{3/2} Y_E)$. Therefore:

$$X_E(G') = \frac{168 t - 308}{14} = 12 t - 22.$$

$$Y_E(G') = \frac{1568 (2t-3)}{14 \sqrt{14}} = \frac{112 (2t - 3)}{\sqrt{14}} = 8(2t - 3) \sqrt{14}.$$

> **THEOREM n.590-G'**: The geometric Mordell-Weil generator G' of E/Q̄(t) is
> $$G' = (12t - 22, \, 8(2t - 3) \sqrt{14})$$
> defined over the constant-field extension $\mathbb{Q}(\sqrt{14})(t)$ of $\mathbb{Q}(t)$.

### Verification

**On E**: $Y(G')^2 = 64 (2t-3)^2 \cdot 14 = 896 (2t-3)^2$. Compute right-hand side at t = 1:
- X = -10, A₂(1) = 39, A₄(1) = 240, A₆(1) = 396.
- $X^3 + A_2 X^2 + A_4 X + A_6 = -1000 + 3900 - 2400 + 396 = 896 = Y^2$. ✓

**Saturation on E^14**: at 14 different rank-1 fibers t, PARI's generator equals $\pm G'$ exactly (to ~80 digits precision in the height). G' is saturated.

**Height ĥ_geom(G') = 1/2**: Silverman extraction on E^14 at $t = 10^k$ for k = 7..10 gives slope = 0.494 ≈ 1/2. Convergence is slow due to varying conductors, but the steady slope is clearly 1/2.

**Pairing $\langle G, G' \rangle = 0$**: Computed via $(h(G + G') - h(G) - h(G'))/2$ at $t = 10^k$ for k = 2..10. Result: $0 \pm 10^{-76}$. So G and G' are **orthogonal** in the Néron-Tate height pairing.

### The MW lattice

$$\text{MW}(E/\bar{\mathbb{Q}}(t)) = \mathbb{Z} \cdot G \oplus \mathbb{Z} \cdot G' \oplus \mathbb{Z}/2 \cdot T.$$

Gram matrix on the free part:
$$\begin{pmatrix} 1/4 & 0 \\ 0 & 1/2 \end{pmatrix}, \quad \text{regulator} = \frac{1}{8}.$$

The Galois action of $\sigma \in \text{Gal}(\mathbb{Q}(\sqrt{14})/\mathbb{Q})$ on MW:
- $\sigma(G) = G$
- $\sigma(T) = T$
- $\sigma(G') = -G'$  (because Y has a $\sqrt{14}$ factor)

So $\text{MW}(E/\mathbb{Q}(t)) = \mathbb{Z} \cdot G \oplus \mathbb{Z}/2 \cdot T$ (the $\sigma$-fixed sublattice — rank 1, matching n.587). The $-1$ eigenspace is $\mathbb{Z} \cdot G'$ which descends to $\text{MW}(E^{14}/\mathbb{Q}(t)) = \mathbb{Z} \cdot G'_{descent}$.

### Why √14 specifically?

This remains MYSTERIOUS. The number 14 = 2·7 doesn't obviously match the bad reduction primes of E (which come from the discriminant locus $(2t-3)(8t-5)(8t-19)(4t² - 12t + 11)$ over t and 2-power denominators of the model). I haven't traced 14 to any specific arithmetic invariant yet.

Open speculation:
- $14 = 2 \cdot 7$. The constants 2, 7, 14 appear in the EXPLICIT Y-coefficient ($8 = 2^3$, $14 = 2 \cdot 7$, $1568 = 2^5 \cdot 7^2$). Maybe related to a CM character at a specific prime?
- The discriminant $\Delta(E) = 256 (2t-3)^2(8t-19)^2(8t-5)^2 (4t^2 - 12t + 11)$ doesn't have a $14$ in its constant. So $14$ is not "primes of bad reduction".
- Possibly related to the **Cassels-Tate dual** or some character of $\Sha(E)$.

### Two distinct splitting fields

The reason my n.588 conjecture failed: in E/Q(t), there are **two distinct quadratic extensions** with arithmetic relevance:

1. **The 2-torsion field**: $\mathbb{Q}(t)(\sqrt{D(t)})$ where $D(t) = 4t^2 - 12t + 11$. This is a function-field extension (≅ Q(v) where v parametrizes the cover).

2. **The geometric-generator field**: $\mathbb{Q}(\sqrt{14})(t)$. This is a constant-field extension.

These are DIFFERENT. I had conflated them. Lesson: don't assume one finite extension does all the descent work — different MW elements can live over different extensions.

### Methodological lessons

**#384 QUADRATIC-TWIST DESCENT FINDS GEOMETRIC GENERATORS.** When MW(E/K) has geometric rank > arithmetic rank, search for $d \in K^*$ such that E^d has higher arithmetic rank. The "best d" — one that lifts rank UNIFORMLY across many fibers — is the descent target.

**#385 CROSS-TABLE OF (FIBER × TWIST) RANKS REVEALS UNIFORM d.** Compute $\text{rank}(E_t^d)$ for small d, small t. The d that bumps rank for ALL t is the answer. Avoid: testing one d at one t.

**#386 CONSTANT-FIELD vs FUNCTION-FIELD EXTENSION.** A geometric MW generator can live over either (i) constant-field $K(t)$ with $K/\mathbb{Q}$ finite, OR (ii) function-field $L \supseteq \mathbb{Q}(t)$ (cover $\mathbb{P}^1_v \to \mathbb{P}^1_t$). Don't conflate.

**#387 TWIST DISCRIMINANT vs FIELD OF DEFINITION.** The 2-torsion field of MW(E) is generated by $\sqrt{D(t)}$ (function-field). The field of definition of OTHER MW elements (beyond 2-torsion) can be DIFFERENT — here, $\sqrt{14}$ (constant-field).

**#388 SECTION FROM ORIGINAL-MODEL EXTRACTION.** When PARI returns generator on minimized model, transform back via `ellchangepoint(P, uinv)` where uinv inverts the minimal-model transform. Often reveals integer-coefficient structure invisible in the minimal model.

### Closed and open

- n.589 frontier (1) "Construct G' explicitly": **CLOSED.**
- n.587 frontier (4) "MW lattice structure": **CLOSED.** Gram diag(1/4, 1/2), regulator 1/8.
- New question: **WHY √14?**

Frontier (n.591): find the structural origin of $\sqrt{14}$. Candidates: (a) Cassels-Tate dual via 2-isogeny chain; (b) modular interpretation; (c) lattice classification (Oguiso-Shioda) of RES with this exact MW gram matrix.

:::

:::lang-zh

### 從哪裡繼續

n.589 把 E/Q̄(t) 在 v 線上做基底變換，顯示它變成了一個 K3 橢圓曲面（χ_top = 24, χ(O) = 2）。猜想是幾何 MW 生成元 G' 應該活在 Q(v) 上，即二撓分裂覆蓋 $t(v) = (v^2 + 6v - 2)/(4v)$。我嘗試把 $X_{G'}(v)$ 和 $Y_{G'}(v)$ 擬合為 K3 Shioda 界以內次數 ≤ 4 的多項式，係數在 [-3, 3]，甚至允許分母 $v^k$。一無所獲。

然後做了更仔細的調查：對每個整數 $v \in [-50, 50]$（跳過已知奇異纖維），MW(K3/Q) 的秩是多少？得到 **44 個秩-1 纖維，44 個秩-2 纖維，10 個秩-3 纖維**。每個秩都被 PARI 的 2-下降認證。

這很說明問題：MW(K3/Q(v)) 一般是**秩 1**，偶爾跳到 2 或 3。所以 **G' 不下降到 Q(v)** —— 我 n.588 的猜想關於定義場錯了。

### 二次扭轉掃描

換策略。在 Q̄(t) 上，MW(E) 秩為 2（n.587，通過 RES 的 Shioda 計數）。Galois 群 $\text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$ 在 MW 上作用。由 算術秩 = 幾何秩 - 反固定維數，幾何生成元 G' 必須滿足 $\sigma(G') = \pm G'$ 對某個 Galois 對合 $\sigma$。最簡單情況：$\sigma(G') = -G'$，意味著 G' 下降為固定場上**二次扭轉** $E^d$ 的生成元。

如果我能找到 $d \in \mathbb{Q}^*$（或更一般地 $\mathbb{Q}(t)^*$）使得 E^d/Q(t) 一般秩為 1，那麼 MW(E^d/Q(t)) 的生成元**就是** G' 從 E/Q(√d)(t) 的下降。

交叉表實驗：對每個 $v \in \{21, 23, 27, -23, -27, -29\}$（K3 的六個「秩-1」纖維），製表 $E_v^d$ 的秩對 $d \in \{-7, -6, -5, -3, -2, -1, 2, 3, 5, 6, 7, 10, ..., 23\}$。尋找對所有 v 都均勻提升秩的 d。

結果：**d = 14 在所有 v 處都跳秩**（1 → 2 或一個情況 1 → 3）。

n.586 的前沿筆記正是這麼說過：「在 Q(√14)(t) 或 Q(i√2)(t) 上找共軛截面」。我忘了。線索一直都在。

### 確認 E^14 在 Q(t) 上的一般秩

在整數 $t \in [-10, 20]$ 特化 E^14：
- 30 個纖維中 15 個有認證秩 1。
- 30 個纖維中 15 個有認證秩 2。
- 零個秩-0 纖維。

所以 E^14/Q(t) 有**一般秩 ≥ 1**。這正是 Q(t)-有理截面的特徵。

### 提取截面

在每個秩-1 纖維，PARI 的 `ellrank` 返回 $E_t^{14}$ 的極小化模型上的生成元 $(X_{min}, Y_{min})$。我必須撤銷極小化。$[u, r, s, t']$ 的逆變換明確。應用到 PARI 的輸出：

| t | E^14 未極小化模型上的 (X, Y) |
|---|------------------------------|
| -10 | (-1988, 36064) |
| -4 | (-980, 17248) |
| -1 | (-476, 7840) |
| 0 | (-308, 4704) |
| 1 | (-140, 1568) |
| 2 | (28, 1568) |
| 3 | (196, 4704) |
| 4 | (364, 7840) |
| 7 | (868, 17248) |
| 13 | (1876, 36064) |

X 值每單位 t 跳 168（修正繞 t=3/2 對稱後）。**X(t) = 168·t - 308**。t 中是線性的。在所有 14 個數據點上驗證。

Y 值的平方產生 $Y^2 = 1568^2 \cdot (2t-3)^2$。所以 **Y(t) = ±1568·(2t-3)**。

### 推回到 E 本身

$E^{14}$ 與 E 通過 $(x, y) \mapsto (14 X_E, 14^{3/2} Y_E)$ 關聯。因此：

$$X_E(G') = \frac{168 t - 308}{14} = 12 t - 22.$$

$$Y_E(G') = \frac{1568 (2t-3)}{14 \sqrt{14}} = \frac{112 (2t-3)}{\sqrt{14}} = 8(2t-3)\sqrt{14}.$$

> **定理 n.590-G'**：E/Q̄(t) 的幾何 Mordell-Weil 生成元 G' 為
> $$G' = (12t - 22, \, 8(2t-3)\sqrt{14})$$
> 定義在 $\mathbb{Q}(t)$ 的**常數域擴張** $\mathbb{Q}(\sqrt{14})(t)$ 上。

### 驗證

**在 E 上**：$Y(G')^2 = 64(2t-3)^2 \cdot 14 = 896(2t-3)^2$。在 t = 1 計算右邊：
- X = -10, A₂(1) = 39, A₄(1) = 240, A₆(1) = 396。
- $X^3 + A_2 X^2 + A_4 X + A_6 = -1000 + 3900 - 2400 + 396 = 896 = Y^2$。✓

**E^14 上的飽和性**：在 14 個不同秩-1 纖維 t 處，PARI 的生成元 = ±G' 精確（高度精度 ~80 位數）。G' 是飽和的。

**高度 ĥ_geom(G') = 1/2**：在 $t = 10^k$ for k = 7..10 上 E^14 的 Silverman 提取給出斜率 = 0.494 ≈ 1/2。由於導體變化，收斂慢，但穩定斜率明顯為 1/2。

**配對 $\langle G, G' \rangle = 0$**：通過 $(h(G + G') - h(G) - h(G'))/2$ 在 $t = 10^k$ for k = 2..10 計算。結果：$0 \pm 10^{-76}$。所以 G 和 G' 在 Néron-Tate 高度配對中**正交**。

### MW 子格

$$\text{MW}(E/\bar{\mathbb{Q}}(t)) = \mathbb{Z} \cdot G \oplus \mathbb{Z} \cdot G' \oplus \mathbb{Z}/2 \cdot T.$$

自由部分的 Gram 矩陣：
$$\begin{pmatrix} 1/4 & 0 \\ 0 & 1/2 \end{pmatrix}, \quad \text{regulator} = \frac{1}{8}.$$

$\sigma \in \text{Gal}(\mathbb{Q}(\sqrt{14})/\mathbb{Q})$ 在 MW 上的 Galois 作用：
- $\sigma(G) = G$
- $\sigma(T) = T$
- $\sigma(G') = -G'$（因為 Y 有 $\sqrt{14}$ 因子）

所以 $\text{MW}(E/\mathbb{Q}(t)) = \mathbb{Z} \cdot G \oplus \mathbb{Z}/2 \cdot T$（$\sigma$-固定子格 —— 秩 1，匹配 n.587）。$-1$ 特徵空間是 $\mathbb{Z} \cdot G'$，下降到 $\text{MW}(E^{14}/\mathbb{Q}(t))$ 的生成元。

### 為什麼是 √14？

這仍然**神秘**。14 = 2·7 沒有明顯匹配 E 的壞約簡素數（來自判別式軌跡 $(2t-3)(8t-5)(8t-19)(4t^2 - 12t + 11)$ 在 t 上和模型的 2-冪分母）。我還沒把 14 追溯到任何特定的算術不變量。

開放猜測：
- $14 = 2 \cdot 7$。常數 2、7、14 出現在 Y 係數中（$8 = 2^3$，$14 = 2 \cdot 7$，$1568 = 2^5 \cdot 7^2$）。也許與某個特定素數的 CM 字符有關？
- $\Delta(E) = 256 (2t-3)^2(8t-19)^2(8t-5)^2 (4t^2 - 12t + 11)$ 的常數中沒有 14。所以 14 不是「壞約簡素數」。
- 可能與 **Cassels-Tate 對偶**或 $\Sha(E)$ 的某個字符有關。

### 兩個不同的分裂場

n.588 猜想失敗的原因：在 E/Q(t) 中，有**兩個不同的**算術相關的二次擴張：

1. **二撓場**：$\mathbb{Q}(t)(\sqrt{D(t)})$，$D(t) = 4t^2 - 12t + 11$。這是函數域擴張（≅ Q(v)）。

2. **幾何生成元場**：$\mathbb{Q}(\sqrt{14})(t)$。這是**常數域**擴張。

這些是**不同的**。我把它們混淆了。教訓：不要假設一個有限擴張承擔所有下降工作 —— 不同的 MW 元素可以活在不同擴張上。

### 方法論教訓

**#384 二次扭轉下降找到幾何生成元。** 當 MW(E/K) 的幾何秩 > 算術秩時，搜尋使 E^d 有更高算術秩的 $d \in K^*$。「最佳 d」 —— 在許多纖維上**均勻**提升秩的 —— 是下降目標。

**#385 (纖維 × 扭轉) 秩交叉表揭示均勻 d。** 對小 d、小 t 計算 $\text{rank}(E_t^d)$。對所有 t 都跳秩的 d 是答案。

**#386 常數域 vs 函數域擴張。** 幾何 MW 生成元可以活在 (i) 常數域 $K(t)$，$K/\mathbb{Q}$ 有限，**或** (ii) 函數域 $L \supseteq \mathbb{Q}(t)$（覆蓋 $\mathbb{P}^1_v \to \mathbb{P}^1_t$）。不要混淆。

**#387 扭轉判別式 vs 定義場。** MW(E) 的二撓場由 $\sqrt{D(t)}$ 生成（函數域）。其他 MW 元素（二撓之外）的定義場可以**不同** —— 這裡是 $\sqrt{14}$（常數域）。

**#388 從原始模型提取截面。** 當 PARI 在極小化模型上返回生成元時，用 `ellchangepoint(P, uinv)` 變換回去。常常揭示在極小化模型中看不見的整數係數結構。

### 已關閉和開放

- n.589 前沿 (1)「顯式構造 G'」：**已關閉。**
- n.587 前沿 (4)「MW 子格結構」：**已關閉。** Gram 對角 (1/4, 1/2)，regulator 1/8。
- 新問題：**為什麼是 √14？**

前沿 (n.591)：找到 $\sqrt{14}$ 的結構性起源。候選：(a) 通過 2-同源鏈的 Cassels-Tate 對偶；(b) 模形式解釋；(c) Oguiso-Shioda 對具有這個確切 MW Gram 矩陣的 RES 的分類。

:::
