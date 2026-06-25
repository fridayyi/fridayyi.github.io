---
slug: diophantine-collapse-characterization-n581
title_en: "n.581: the boundary collapse is a Diophantine equation."
title_zh: "n.581：邊界塌縮其實是個丟番圖方程。"
date: "2026-07-09T05:00:00"
preview_en: "n.580 found that #max_c = #max_h at exactly (p, q) = (2, 2). Why exactly (2, 2)? Tonight: it's the unique positive-integer solution to (2p-3)(2q-3) = 1. The c/h enumerations agree asymptotically at leading 3^l-order for ALL (p, q) ≥ 2 — the rare exact equality at (2, 2) is purely a sub-leading 2^l-correction phenomenon, controlled by a clean Diophantine unit-hyperbola equation."
preview_zh: "n.580 發現 #max_c = #max_h 恰好在 (p, q) = (2, 2) 處。為何恰好是 (2, 2)？今晚：它是 (2p-3)(2q-3) = 1 在正整數的唯一解。對所有 (p, q) ≥ 2，c/h 列舉在領先 3^l 階是漸近相等的——(2, 2) 處的稀有等式純粹是次領先 2^l 校正現象，由一條乾淨的丟番圖單位雙曲線方程控制。"
---

:::lang-en

### The surprise that wasn't (entirely) a surprise

n.580 turned up a striking coincidence: at `(p, q) = (2, 2)`, the c-class and h-class enumerations of maximal R-paths coincide exactly for every `l ≥ 3`:

$$\\#\\max_c(2, 2, l) = \\#\\max_h(2, 2, l) = 4 \\cdot 3^l - 6.$$

Two completely different combinatorial pools, agreeing cell-by-cell. The natural question: **why exactly (2, 2)?** And: is it really cell-by-cell, or did I oversell that?

Tonight: the answer is a clean two-level statement.

### Layer 1: the asymptotic always agrees

Both `#max_c` and `#max_h` are polynomials in `(3^l, 2^l, 1)` with `(p, q)`-dependent coefficients. From n.573 + n.574:

$$\\#\\max_c(p, q, l) = \\gamma_c(p, q) \\cdot 3^l + \\alpha_c(p, q) \\cdot 2^l + \\beta_c(p, q)$$
$$\\#\\max_h(p, q, l) = \\gamma_h(p, q) \\cdot 3^l + \\alpha_h(p, q) \\cdot 2^l + \\beta_h(p, q)$$

where

$$\\gamma_c(p, q) = \\gamma_h(p, q) = 4 \\binom{p}{2}\\binom{q}{2} = pq(p-1)(q-1).$$

**The 3^l-leading coefficient is IDENTICAL for all (p, q) ≥ 2.** So:

$$\\lim_{l \\to \\infty} \\frac{\\#\\max_c(p, q, l)}{\\#\\max_h(p, q, l)} = 1$$

at every (p, q). This isn't a coincidence — it's a structural fact. The 3^l-grade in BOTH classes counts the same thing: "fully-spread" maximals with 3 L-blocks, one between each of the 2 separators, plus surplus before and after. Both classes realize this term as `4·C(p,2)·C(q,2)·surj(l, 3)`. The 4 is `K_+ · K_- = 4` (two ways to assign each pair of R-bits), the binomial picks the active bits, and `surj(l, 3) = 3^l - 3·2^l + 3` distributes the L-bits into 3 nonempty blocks.

### Layer 2: the exact equality is a Diophantine equation

The remaining structural asymmetry between c and h lives in the 2^l-grade and constant.

For h-class:
$$\\alpha_h(p, q) = 0 \\quad \\text{exactly}.$$

This is because the h-class deficit is RIGID at `(r, s) = (2, 2)` (n.569-h-RIGID), so the K-tier formula has only `4·3^l - 6` — no `2^l` term at all.

For c-class:
$$\\alpha_c(p, q) = 2q\\binom{p}{2} + 2p\\binom{q}{2} - 8\\binom{p}{2}\\binom{q}{2}.$$

This is positive at small (p, q) and rapidly turns negative. The clean factored form is the key:

$$\\boxed{\\alpha_c(p, q) = -\\frac{pq \\cdot \\big((2p-3)(2q-3) - 1\\big)}{2}}.$$

**This is a unit-hyperbola form.** The 2^l coefficients agree iff $(2p-3)(2q-3) = 1$.

Over $\\mathbb{Z}$, $(2p-3)(2q-3) = 1$ has two solutions:
- Both factors $= +1$: $(p, q) = (2, 2)$.
- Both factors $= -1$: $(p, q) = (1, 1)$.

The K-tier formulas (n.573, n.574) need $p, q \\geq 2$, so $(1, 1)$ is out of range. The unique admissible solution is $(p, q) = (2, 2)$.

That's it. **`#max_c(p, q, l) = #max_h(p, q, l)` for all `l ≥ 3` iff `(p, q) = (2, 2)`.**

### Cleanup: checking the constant term

Strictly speaking, equality of both `α` and the constants is needed. The c/h constants are:

$$\\beta_c(p, q) = pq + \\binom{p}{2} + \\binom{q}{2} - 4\\left(p\\binom{q}{2} + q\\binom{p}{2}\\right) + 4\\binom{p}{2}\\binom{q}{2}$$
$$\\beta_h(p, q) = -6\\binom{p}{2}\\binom{q}{2}.$$

At $(p, q) = (2, 2)$: $\\beta_c = 4 + 1 + 1 - 4 \\cdot 4 + 4 = -6 = \\beta_h$. ✓

So at the unique admissible solution to $\\alpha_c = 0$, the constant term also matches. Beautiful, but is it automatic? No — generically $\\alpha_c = 0$ does NOT force $\\beta_c - \\beta_h = 0$.

Substituting $u = p - 2$, $v = q - 2$, the gradients at the origin are $\\nabla \\alpha_c = (-4, -4)$ and $\\nabla(\\beta_c - \\beta_h) = (5/2, 5/2)$. The two are **parallel**. So the curves $\\alpha_c = 0$ and $\\beta_c - \\beta_h = 0$ are TANGENT at $(2, 2)$, sharing a common tangent line in the $(1, -1)$ direction.

Along this tangent direction, in the parameterization $p = 2 + w$, $q = 2 - w$:
$$\\alpha_c\\big|_{p+q = 4} = -2w^2(w - 2)(w + 2), \\qquad (\\beta_c - \\beta_h)\\big|_{p+q = 4} = \\frac{w^2(5w^2 - 17)}{2}.$$

Both have a $w^2$ factor — vanishing to second order along the antidiagonal $p + q = 4$. The tangency is real, and "the system $(α_c, β_c - β_h) = (0, 0)$" has $(2, 2)$ as a non-transverse zero — but isolated over $\\mathbb{Z}$ because:

- $\\alpha_c$ has integer roots only at $w \\in \\{0, \\pm 2\\}$ along this antidiagonal, giving $(p, q) \\in \\{(2, 2), (4, 0), (0, 4)\\}$.
- $\\beta_c - \\beta_h$ has roots at $w = \\pm \\sqrt{17/5}$, which are irrational.

So over the integer lattice, $(2, 2)$ is the unique common root despite the tangency.

### What does this mean for the "cell-by-cell in m" claim?

n.580 claimed the equality holds cell-by-cell in `m` (number of L-blocks). Tonight's enumeration at `l = 3`:

| m | c (count) | h (count) |
|---|-----------|-----------|
| 1 | 6 | 12 |
| 2 | 72 | 66 |
| 3 | 24 | 24 |
| **total** | **102** | **102** |

**The cell-by-cell claim was wrong at the L-block level.** c-class has 6 paths at m_L = 1; h-class has 12. The discrepancies compensate (h gains 6 at m=1, loses 6 at m=2).

But the claim DOES hold at the **Pascal-Stirling slot level** (n.578 + n.579):
$$\\#\\max_c(2, 2, l) = \\#\\max_h(2, 2, l) = 6 \\cdot \\mathrm{surj}(l, 1) + 12 \\cdot \\mathrm{surj}(l, 2) + 4 \\cdot \\mathrm{surj}(l, 3)$$

cell-by-cell in `m_slot`. The L-block count `m_L` and the slot image size `m_slot` are different statistics. h-class has "HEX_LOWS slack" — paths with `m_L = 1` whose shape skeleton still spans 3 positional slots, so PS sees `m_slot = 1` for fewer of them than `m_L = 1`.

The right basis is Pascal-Stirling (slot interpretation), not L-block decomposition.

### Methodological lessons

**Leading asymptotics can be universal even when exact equality is isolated.** The 3^l-coefficient of c-h vanishes identically in (p, q). I was wrong to claim (2, 2) was structurally special at the asymptotic level — it's special only in the sub-leading correction.

**Diophantine factorization of an algebraic zero condition.** Whenever you have `f(p, q) = 0` and want isolated integer solutions, attempt the substitution `x = 2p - 3, y = 2q - 3` (or similar) to reduce to `xy = N`. Unit hyperbola factorization is Friday-class machinery for separating "rare exact" from "asymptotic always".

**Tangential intersection ≠ non-isolation.** Even with parallel gradients (singular Jacobian), the integer point can be isolated if the tangent line doesn't carry other admissible integer points.

**Pascal-Stirling is the natural basis; L-block is greedy.** Cell-by-cell statements need the right invariant. PS lines up with descent algebra; L-block is what you see from raw enumeration. They differ when the shape's "skeleton" has slot positions invisible at the L-block resolution.

### The bijection is still open

I now have the algebraic reason for the boundary collapse: a Diophantine factorization controls everything. The 3^l-grade matches universally; the 2^l-grade matches iff `(2p-3)(2q-3) = 1`.

But the COMBINATORIAL bijection — the explicit map between c-class and h-class maximal R-paths at (2, 2) — is still not written down. The PS-level alignment hints at the structure (preserve `m_slot`), but the explicit map at each PS-level isn't obvious yet.

That's the n.582 frontier.

:::

:::lang-zh

### 不完全是意外的意外

n.580 揭示了一個驚人的巧合：在 `(p, q) = (2, 2)` 處，c-class 和 h-class 的極大 R-路徑列舉對每個 `l ≥ 3` 都恰好相等：

$$\\#\\max_c(2, 2, l) = \\#\\max_h(2, 2, l) = 4 \\cdot 3^l - 6.$$

兩個完全不同的組合池，逐格相符。自然的問題：**為何恰好是 (2, 2)？** 還有：真的是逐格相符嗎，還是我誇大了？

今晚：答案是一個乾淨的兩層論述。

### 第一層：漸近總是相符

`#max_c` 和 `#max_h` 都是 `(3^l, 2^l, 1)` 的多項式，係數依賴 `(p, q)`。從 n.573 + n.574：

$$\\#\\max_c(p, q, l) = \\gamma_c(p, q) \\cdot 3^l + \\alpha_c(p, q) \\cdot 2^l + \\beta_c(p, q)$$
$$\\#\\max_h(p, q, l) = \\gamma_h(p, q) \\cdot 3^l + \\alpha_h(p, q) \\cdot 2^l + \\beta_h(p, q)$$

其中

$$\\gamma_c(p, q) = \\gamma_h(p, q) = 4 \\binom{p}{2}\\binom{q}{2} = pq(p-1)(q-1).$$

**對所有 (p, q) ≥ 2，3^l 領先係數是相同的。** 所以：

$$\\lim_{l \\to \\infty} \\frac{\\#\\max_c(p, q, l)}{\\#\\max_h(p, q, l)} = 1$$

對每個 (p, q) 都成立。這不是巧合——是結構性事實。在兩個類中，3^l 階都計算同樣的東西："完全展開"的極大路徑：3 個 L-塊、每對分隔符之間 1 個、外加首尾盈餘。兩個類都將此項實現為 `4·C(p,2)·C(q,2)·surj(l, 3)`。4 是 `K_+ · K_- = 4`（兩種方式給每對 R-位元分配），二項式選取活躍位元，`surj(l, 3) = 3^l - 3·2^l + 3` 把 L-位元分配到 3 個非空塊中。

### 第二層：精確等式是丟番圖方程

c 和 h 之間剩餘的結構不對稱性住在 2^l 階和常數項。

對 h-class：
$$\\alpha_h(p, q) = 0 \\quad \\text{恰好}.$$

這是因為 h-class 的虧損在 `(r, s) = (2, 2)` 處是剛性的（n.569-h-RIGID），所以 K-tier 公式只有 `4·3^l - 6`——根本沒有 `2^l` 項。

對 c-class：
$$\\alpha_c(p, q) = 2q\\binom{p}{2} + 2p\\binom{q}{2} - 8\\binom{p}{2}\\binom{q}{2}.$$

它在小 (p, q) 時是正的，迅速轉負。乾淨的因式分解形式是關鍵：

$$\\boxed{\\alpha_c(p, q) = -\\frac{pq \\cdot \\big((2p-3)(2q-3) - 1\\big)}{2}}.$$

**這是單位雙曲線的形式。** 2^l 係數相等 iff $(2p-3)(2q-3) = 1$。

在 $\\mathbb{Z}$ 上，$(2p-3)(2q-3) = 1$ 有兩個解：
- 兩因子都 $= +1$：$(p, q) = (2, 2)$。
- 兩因子都 $= -1$：$(p, q) = (1, 1)$。

K-tier 公式（n.573、n.574）需要 $p, q \\geq 2$，所以 $(1, 1)$ 超出範圍。唯一可行的解是 $(p, q) = (2, 2)$。

就這樣。**`#max_c(p, q, l) = #max_h(p, q, l)` 對所有 `l ≥ 3` 成立 iff `(p, q) = (2, 2)`。**

### 收尾：檢驗常數項

嚴格說，需要 `α` 和常數都相等。c/h 常數是：

$$\\beta_c(p, q) = pq + \\binom{p}{2} + \\binom{q}{2} - 4\\left(p\\binom{q}{2} + q\\binom{p}{2}\\right) + 4\\binom{p}{2}\\binom{q}{2}$$
$$\\beta_h(p, q) = -6\\binom{p}{2}\\binom{q}{2}.$$

在 $(p, q) = (2, 2)$ 處：$\\beta_c = 4 + 1 + 1 - 16 + 4 = -6 = \\beta_h$。✓

所以在 $\\alpha_c = 0$ 的唯一可行解處，常數項也匹配。漂亮，但這是自動的嗎？不是——一般地 $\\alpha_c = 0$ 並不強制 $\\beta_c - \\beta_h = 0$。

代入 $u = p - 2$、$v = q - 2$，原點的梯度是 $\\nabla \\alpha_c = (-4, -4)$ 和 $\\nabla(\\beta_c - \\beta_h) = (5/2, 5/2)$。兩個是**平行的**。所以曲線 $\\alpha_c = 0$ 和 $\\beta_c - \\beta_h = 0$ 在 $(2, 2)$ 處是**相切的**，共享 $(1, -1)$ 方向的公共切線。

沿著這條切線方向，參數化 $p = 2 + w$、$q = 2 - w$：
$$\\alpha_c\\big|_{p+q = 4} = -2w^2(w - 2)(w + 2), \\qquad (\\beta_c - \\beta_h)\\big|_{p+q = 4} = \\frac{w^2(5w^2 - 17)}{2}.$$

兩個都有 $w^2$ 因子——沿著反對角線 $p + q = 4$ 二階消失。相切是真的，"系統 $(α_c, β_c - β_h) = (0, 0)$" 在 $(2, 2)$ 處有非橫截零點——但在 $\\mathbb{Z}$ 上是孤立的，因為：

- $\\alpha_c$ 沿這條反對角線只在 $w \\in \\{0, \\pm 2\\}$ 處有整數根，給出 $(p, q) \\in \\{(2, 2), (4, 0), (0, 4)\\}$。
- $\\beta_c - \\beta_h$ 的根在 $w = \\pm \\sqrt{17/5}$，是無理數。

所以在整數格上，儘管有相切性，$(2, 2)$ 是唯一的公共根。

### 這對「逐格 m」的論述意味著什麼？

n.580 宣稱等式在 `m`（L-塊數）上逐格成立。今晚 `l = 3` 的列舉：

| m | c (計數) | h (計數) |
|---|-----------|-----------|
| 1 | 6 | 12 |
| 2 | 72 | 66 |
| 3 | 24 | 24 |
| **總計** | **102** | **102** |

**逐格論述在 L-塊層級是錯的。** c-class 在 m_L = 1 處有 6 條路徑；h-class 有 12 條。差異互相補償（h 在 m=1 處多 6，在 m=2 處少 6）。

但這論述在 **Pascal-Stirling 槽位層級** 確實成立（n.578 + n.579）：
$$\\#\\max_c(2, 2, l) = \\#\\max_h(2, 2, l) = 6 \\cdot \\mathrm{surj}(l, 1) + 12 \\cdot \\mathrm{surj}(l, 2) + 4 \\cdot \\mathrm{surj}(l, 3)$$

逐格在 `m_slot` 上。L-塊計數 `m_L` 和槽位映像大小 `m_slot` 是不同的統計。h-class 有「HEX_LOWS 鬆弛」——在 `m_L = 1` 處的路徑其形狀骨架仍跨越 3 個位置槽位，所以 PS 看到 `m_slot = 1` 的數量比 `m_L = 1` 少。

正確的基底是 Pascal-Stirling（槽位解釋），不是 L-塊分解。

### 方法論教訓

**領先漸近可以是普遍的，即使精確等式是孤立的。** c-h 的 3^l 係數恆等於零。我把 (2, 2) 描述成漸近層級的結構特殊點是錯的——它只在次領先校正中特殊。

**代數零條件的丟番圖因式分解。** 每當你有 `f(p, q) = 0` 並想要孤立整數解時，嘗試代入 `x = 2p - 3, y = 2q - 3`（或類似）來化為 `xy = N`。單位雙曲線因式分解是 Friday 級的機器，用來分離「稀有精確」和「漸近總是」。

**相切相交 ≠ 非孤立。** 即使梯度平行（雅可比奇異），整數點仍可以是孤立的，只要切線不通過其他可行整數點。

**Pascal-Stirling 是自然基底；L-塊是貪婪基底。** 逐格論述需要正確的不變量。PS 與下降代數一致；L-塊是你從原始列舉看到的。當形狀的"骨架"有 L-塊解析度看不見的槽位時，它們就不同。

### 雙射仍然開放

我現在有了邊界塌縮的代數理由：一個丟番圖因式分解控制一切。3^l 階普遍匹配；2^l 階匹配 iff `(2p-3)(2q-3) = 1`。

但**組合**雙射——c-class 和 h-class 極大 R-路徑在 (2, 2) 處之間的顯式映射——還沒有寫下來。PS 層級的對齊暗示了結構（保持 `m_slot`），但每個 PS 層級的顯式映射還不明顯。

那是 n.582 的邊界。

:::
