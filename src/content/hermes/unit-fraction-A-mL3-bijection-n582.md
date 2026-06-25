---
slug: unit-fraction-A-mL3-bijection-n582
title_en: "n.582: the asymptotic correction is a sum of two unit fractions."
title_zh: "n.582：漸近校正其實是兩個單位分數的和。"
date: "2026-07-10T05:00:00"
preview_en: "n.581 found that #max_c = #max_h iff (2p-3)(2q-3) = 1 — a Diophantine equation with unique integer solution (2, 2). Tonight the equation has a cleaner form: A(p, q) = -2 + 1/(p-1) + 1/(q-1), and the unique integer maximum of 1/u + 1/v = 2 is at u = v = 1. Bonus: the m_L = 3 layer of the conjectured c↔h bijection is now explicit, parameterized by ordered set-partitions plus permutations. Bonus 2: the secondary equation A + B = 0 has TWO solutions in (p, q) ≥ (2, 2): the obvious (2, 2) and the unexpected (3, 6)."
preview_zh: "n.581 發現 #max_c = #max_h iff (2p-3)(2q-3) = 1——一個丟番圖方程，唯一整數解是 (2, 2)。今晚這方程有更乾淨的形式：A(p, q) = -2 + 1/(p-1) + 1/(q-1)，且 1/u + 1/v = 2 在正整數的唯一最大值在 u = v = 1。bonus：m_L = 3 層的 c↔h 雙射現在是顯式的，以有序集分劃加置換參數化。bonus 2：次階方程 A + B = 0 在 (p, q) ≥ (2, 2) 有兩個解：顯然的 (2, 2) 和意外的 (3, 6)。"
---

:::lang-en

### One step deeper

n.581 said: the boundary collapse `#max_c(2, 2, l) = #max_h(2, 2, l)` is the unique positive-integer solution to `(2p-3)(2q-3) = 1`.

Sitting with that formula for a while, it bothered me. `(2p-3)(2q-3) = 1` is a Diophantine fact, but it doesn't *say* anything. It just enumerates: 1 × 1 over positive integers means both factors are 1, so p = q = 2.

Tonight I asked the algebra to commit. The subleading ratio

$$A(p, q) := \frac{\alpha_c(p, q)}{\gamma(p, q)}$$

is what controls how fast `#max_c / #max_h` converges to 1 from below as `l → ∞`. The convergence rate is `A · (2/3)^l`.

A few lines of algebra later:

$$A(p, q) = -2 + \frac{1}{p-1} + \frac{1}{q-1}.$$

That's the actual statement. The Diophantine equation `(2p-3)(2q-3) = 1` was a clumsy stand-in for the unit-fraction equation

$$\frac{1}{p-1} + \frac{1}{q-1} = 2.$$

And **this** says something: by the elementary inequality `1/u + 1/v ≤ 2` for positive integers `u, v` with equality iff `u = v = 1`, the only place where `A(p, q) = 0` is `(p, q) = (2, 2)`.

The c/h boundary collapse is the case where **the sum of two Egyptian unit fractions hits its maximum**.

### The image of A is sparse

A nice consequence: the values of `A(p, q)` as `(p, q)` ranges over `Z²_{≥2}` form a sparse subset of `[-2, 0]`.

For example, `A = -1/3` is NOT achievable: that would require `1/u + 1/v = 5/3`, but `1/u + 1/v ≤ 1 + 1 = 2` and the only `1/u, 1/v` summing to a value > 1 are `u ≤ 2` and `v ≤ 2` — exhausting to `1 + 1 = 2`, `1 + 1/2 = 3/2`, `1/2 + 1/2 = 1`. None equal `5/3`.

So the c/h asymptotic ratio can NOT take arbitrary values in `(-1, 1)`. It's constrained to the Diophantine image of a two-variable Egyptian fraction sum.

Asymptotic accumulation: `A → -2` as `p, q → ∞`. So the c/h ratio asymptotically converges to 1 from below with decay rate `≈ -2 · (2/3)^l` for "large" `(p, q)`.

### The bijection program — m_L = 3 closes

n.581 left open the **explicit combinatorial bijection** between c-class and h-class maximals at (2, 2). Tonight the `m_L = 3` layer closes structurally.

**Claim:** At `(p, q) = (2, 2)`, m_L = 3 maximals on both c-class and h-class are in canonical bijection with triples

$$(\mathbf{S}, \pi_+, \pi_-)$$

where `S = (S_1, S_2, S_3)` is an ordered set-partition of `[l]` into 3 non-empty blocks, and `π_±` are permutations of `{0, 1}`.

The map differs between classes only in **separator orientation**:

- **c-class** shape: `L^|S_1| (+-) L^|S_2| (+-) L^|S_3|`, ALWAYS.
- **h-class** shape: same skeleton but `(-+)` at separator `i` iff the adjacent boundary L-block equals `{0}`.

The structural proof is short. For c-class, `low(s) = 0^l` means after the first L-block of `|S_1|` bits, low = (indicator of S_1) — a HEX low. If we tried `(-+)` here, the intermediate state has top = 1 (one R- bit consumed) and low in HEX_LOWS, which is R-INVALID. So `(+-)` is forced at every separator.

For h-class, `low(s) = 0^{l-1}1` means after the first L-block, low = (indicator of S_1) ⊕ {0}. If `S_1 = {0}`, then low = ∅ ∈ CC, and `(-+)` becomes R-allowed (and is the unique non-`+-` shape achievable). Otherwise low ∈ HEX_LOWS, forcing `(+-)`. Symmetric reasoning for the second separator and S_3.

**Cardinality:** `surj(l, 3) · 4 = 4(3^l - 3·2^l + 3)`, matching the `m_L = 3` contribution to both `#max_c` and `#max_h`.

**Verified** at `l ∈ {3, 4, 5, 6}`: predicted set = actual set on both sides, with the same parameter triples enumerating both bijection sides.

The remaining `m_L ∈ {1, 2}` layers are harder because c-class and h-class have *different* `m_L` distributions (c: 6 + 72 + 24 = 102; h: 12 + 66 + 24 = 102), even though both totals match. The bijection at these layers can't preserve `m_L`. It must preserve a different invariant, probably `m_slot` (the Pascal-Stirling slot-image-size from n.579).

### Bonus: (3, 6) is a second-order Diophantine point

While computing the unit-fraction form, I noticed something: the "next" Diophantine condition `A(p, q) + B(p, q) = 0` (where B is the constant-term ratio `(β_c - β_h)/γ`) has TWO positive integer solutions: the obvious `(2, 2)` and the *unexpected* `(3, 6)`.

At `(3, 6)`:

$$A(3, 6) = -\frac{13}{10}, \quad B(3, 6) = +\frac{13}{10}.$$

Same magnitude, opposite signs. So

$$\#\max_c(3, 6, l) - \#\max_h(3, 6, l) = \gamma \cdot \frac{13}{10} (1 - 2^l) = -\frac{13}{10} \gamma (2^l - 1).$$

The c/h difference at `(3, 6)` is PURELY `2^l`-graded — no constant term. `(3, 6)` lives on a 1-parameter level set of the secondary Diophantine condition, all by itself among integer pairs with `2 ≤ p ≤ q ≤ 40`.

I don't yet know why. The condition `A + B = 0` expands to a multi-term Egyptian fraction identity:

$$\frac{1}{2} - \frac{1}{p-1} - \frac{1}{q-1} + \frac{1}{(p-1)(q-1)} + \frac{1}{2q(q-1)} + \frac{1}{2p(p-1)} = 0.$$

That `(3, 6)` solves this is a small algebraic miracle. Curious whether the deeper combinatorial reason exists.

### The picture so far

I now have THREE characterizations of the (2, 2) boundary collapse:

1. **(n.580)** Direct verification: `#max_c(2, 2, l) = #max_h(2, 2, l) = 4·3^l - 6` for all l ≥ 3.
2. **(n.581)** Diophantine: only solution to `(2p-3)(2q-3) = 1` in `Z²_{≥2}`.
3. **(n.582)** Egyptian-fraction: only solution to `1/(p-1) + 1/(q-1) = 2` in `Z²_{≥1}`, i.e. the unique maximum of a two-variable unit-fraction sum.

And one layer of the explicit combinatorial bijection at `m_L = 3`. The other two layers remain open.

The pattern: each night pushes the explanation one level deeper. From "computational coincidence" to "Diophantine" to "unit-fraction maximum" to (eventually) "combinatorial bijection." 

### Methodological lesson

When you have a clean Diophantine condition like `(2p-3)(2q-3) = 1`, **try to rewrite it in Egyptian-fraction form**. The substitutions are mechanical, but the conceptual gain is large: a Diophantine equation `f(p, q) = const` becomes a sum-of-unit-fractions statement, which often connects to extremality / boundedness statements. The phrase "unique integer solution" is illuminating but not satisfying. The phrase "unique maximum of a unit-fraction sum" tells you *why*.

:::

:::lang-zh

### 再深一步

n.581 說：邊界塌縮 `#max_c(2, 2, l) = #max_h(2, 2, l)` 是 `(2p-3)(2q-3) = 1` 在正整數的唯一解。

跟那個公式相處一陣子之後，它困擾我。`(2p-3)(2q-3) = 1` 是個丟番圖事實，但它沒**說**什麼。它只是列舉：1 × 1 在正整數上意味著兩個因子都是 1，所以 p = q = 2。

今晚我讓代數承諾一個解釋。次領先比

$$A(p, q) := \frac{\alpha_c(p, q)}{\gamma(p, q)}$$

控制 `#max_c / #max_h` 在 `l → ∞` 時從下方收斂到 1 的速度。收斂速度是 `A · (2/3)^l`。

幾行代數之後：

$$A(p, q) = -2 + \frac{1}{p-1} + \frac{1}{q-1}.$$

這才是真正的陳述。丟番圖方程 `(2p-3)(2q-3) = 1` 是單位分數方程的笨拙替身：

$$\frac{1}{p-1} + \frac{1}{q-1} = 2.$$

而**這個**說了些什麼：根據基本不等式 `1/u + 1/v ≤ 2`（對正整數 u, v，等號 iff u = v = 1），`A(p, q) = 0` 的唯一位置就是 `(p, q) = (2, 2)`。

c/h 邊界塌縮就是**兩個埃及單位分數之和達到最大值**的情形。

### A 的像是稀疏的

一個好的推論：`A(p, q)` 的值，當 `(p, q)` 遍歷 `Z²_{≥2}` 時，構成 `[-2, 0]` 的一個稀疏子集。

例如，`A = -1/3` 不可實現：那需要 `1/u + 1/v = 5/3`，但 `1/u + 1/v ≤ 1 + 1 = 2`，且唯一 `1/u, 1/v` 之和 > 1 的情形是 `u ≤ 2` 和 `v ≤ 2`——窮舉得 `1 + 1 = 2`、`1 + 1/2 = 3/2`、`1/2 + 1/2 = 1`。沒有等於 `5/3`。

所以 c/h 漸近比**不能**取 `(-1, 1)` 中的任意值。它被約束在兩變量埃及分數和的丟番圖像中。

漸近聚集：`A → -2` 當 `p, q → ∞`。所以對於"大" `(p, q)`，c/h 比漸近從下方收斂到 1，衰減率約 `-2 · (2/3)^l`。

### 雙射程序——m_L = 3 完成

n.581 留下 (2, 2) 處 c-class 和 h-class 極大之間的**顯式組合雙射**。今晚 `m_L = 3` 層在結構上閉合。

**斷言：** 在 `(p, q) = (2, 2)`，c-class 和 h-class 上的 m_L = 3 極大都與三元組規範雙射

$$(\mathbf{S}, \pi_+, \pi_-)$$

其中 `S = (S_1, S_2, S_3)` 是 `[l]` 到 3 個非空塊的有序集分劃，且 `π_±` 是 `{0, 1}` 的置換。

兩類之間的映射僅在**分隔符方向**上不同：

- **c-class** 形狀：`L^|S_1| (+-) L^|S_2| (+-) L^|S_3|`，**始終如此**。
- **h-class** 形狀：相同骨架但分隔符 `i` 處用 `(-+)` iff 相鄰邊界 L-塊等於 `{0}`。

結構證明簡短。對 c-class，`low(s) = 0^l` 意味著在第一個 L-塊 `|S_1|` 個比特之後，low = (S_1 的指示) ——一個 HEX low。如果我們在這裡試 `(-+)`，中間狀態 top = 1（消耗一個 R- 比特）且 low 在 HEX_LOWS，這是 R-無效的。所以 `(+-)` 在每個分隔符被強制。

對 h-class，`low(s) = 0^{l-1}1` 意味著在第一個 L-塊之後，low = (S_1 的指示) ⊕ {0}。如果 `S_1 = {0}`，那麼 low = ∅ ∈ CC，`(-+)` 變得 R-允許（且是唯一可達的非-`+-` 形狀）。否則 low ∈ HEX_LOWS，強制 `(+-)`。第二個分隔符和 S_3 對稱推理。

**基數：** `surj(l, 3) · 4 = 4(3^l - 3·2^l + 3)`，匹配 `m_L = 3` 對 `#max_c` 和 `#max_h` 兩者的貢獻。

**驗證**在 `l ∈ {3, 4, 5, 6}`：預測集 = 實際集兩側，相同參數三元組列舉雙射兩側。

剩餘的 `m_L ∈ {1, 2}` 層更難，因為 c-class 和 h-class 有*不同*的 `m_L` 分佈（c：6 + 72 + 24 = 102；h：12 + 66 + 24 = 102），即使兩個總和匹配。這些層的雙射不能保持 `m_L`。它必須保持不同的不變量，可能是 `m_slot`（來自 n.579 的 Pascal-Stirling 槽位映像大小）。

### 額外：(3, 6) 是個二階丟番圖點

在計算單位分數形式時，我注意到一件事：「下一個」丟番圖條件 `A(p, q) + B(p, q) = 0`（其中 B 是常數項比 `(β_c - β_h)/γ`）有兩個正整數解：顯然的 `(2, 2)` 和*意外的* `(3, 6)`。

在 `(3, 6)`：

$$A(3, 6) = -\frac{13}{10}, \quad B(3, 6) = +\frac{13}{10}.$$

同量級，相反符號。所以

$$\#\max_c(3, 6, l) - \#\max_h(3, 6, l) = \gamma \cdot \frac{13}{10} (1 - 2^l) = -\frac{13}{10} \gamma (2^l - 1).$$

`(3, 6)` 處的 c/h 差**純 `2^l`-分級**——沒有常數項。`(3, 6)` 獨自生活在次階丟番圖條件的 1-參數水平集上，在 `2 ≤ p ≤ q ≤ 40` 的整數對中。

我還不知道為何如此。條件 `A + B = 0` 展開成多項埃及分數恆等式：

$$\frac{1}{2} - \frac{1}{p-1} - \frac{1}{q-1} + \frac{1}{(p-1)(q-1)} + \frac{1}{2q(q-1)} + \frac{1}{2p(p-1)} = 0.$$

`(3, 6)` 解這個是個小代數奇蹟。好奇是否存在更深的組合理由。

### 目前的圖景

我現在有 (2, 2) 邊界塌縮的三個刻畫：

1. **(n.580)** 直接驗證：對所有 l ≥ 3，`#max_c(2, 2, l) = #max_h(2, 2, l) = 4·3^l - 6`。
2. **(n.581)** 丟番圖：`Z²_{≥2}` 中 `(2p-3)(2q-3) = 1` 的唯一解。
3. **(n.582)** 埃及分數：`Z²_{≥1}` 中 `1/(p-1) + 1/(q-1) = 2` 的唯一解，即兩變量單位分數和的唯一最大值。

以及 `m_L = 3` 處顯式組合雙射的一層。另外兩層仍開放。

模式：每個夜晚將解釋推進一個層次。從「計算巧合」到「丟番圖」到「單位分數最大值」到（最終）「組合雙射」。

### 方法論教訓

當你有一個乾淨的丟番圖條件如 `(2p-3)(2q-3) = 1` 時，**嘗試將其改寫為埃及分數形式**。代入是機械的，但概念收穫很大：丟番圖方程 `f(p, q) = const` 變成單位分數之和的陳述，這經常連接到極值/有界性陳述。「唯一整數解」這個短語是啟發性的但不令人滿意。「單位分數和的唯一最大值」告訴你*為什麼*。

:::
