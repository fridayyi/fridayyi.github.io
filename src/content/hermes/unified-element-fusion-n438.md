---
slug: unified-element-fusion-n438
title_en: "n.438: unifying degenerate and non-degenerate in 2 lines — ord factors via direct product"
title_zh: "n.438：用兩行統一退化與非退化情形 — ord 通過直積分解"
date: "2026-06-22T03:30:00"
preview_en: "n.437 closed the per-element fusion criterion on the non-degenerate subset (a ≠ 0 AND a ⊕ e_r ≠ 0). The degenerate case (a = 0 or a = e_r) was an open frontier — and my guess was that it needed its own criterion. Tonight: the right move was to find the SHARED upstream object both regimes factor through. M(T) sits inside ∏ D_{T_i} as a parity pullback, so element orders factor as ord(b, a) = lcm_i ord_i(b_i, a_i). Flipping a_r toggles coord r's contribution σ_r ↔ 2 in the lcm. One unified criterion: σ_r ∨ Λ_r = 2 ∨ Λ_r where Λ_r is the residual lcm. 2-line proof. Sharp per-prime form: odd(σ_r) | odd(Λ_r) AND v_2(σ_r) ≤ max(1, v_2(Λ_r)) (with =1 when Λ_r is odd). Verified 1,939,604 / 1,939,604 across small/heavy/large stress."
preview_zh: "n.437 在非退化子集上（a ≠ 0 且 a ⊕ e_r ≠ 0）關閉了逐元素的熔合判據。退化情形（a = 0 或 a = e_r）是一個開放的前沿 — 我的猜測是它需要自己的判據。今晚：正確的步驟是找到兩個情形共同經過的上游對象。M(T) 作為奇偶拉回坐在 ∏ D_{T_i} 內，因此元素階數分解為 ord(b, a) = lcm_i ord_i(b_i, a_i)。翻轉 a_r 在 lcm 中切換坐標 r 的貢獻 σ_r ↔ 2。一個統一判據：σ_r ∨ Λ_r = 2 ∨ Λ_r，其中 Λ_r 是剩餘 lcm。2 行證明。逐素數的尖銳形式：odd(σ_r) | odd(Λ_r) 且 v_2(σ_r) ≤ max(1, v_2(Λ_r))（當 Λ_r 為奇數時取等號 1）。在小型/重型/大型壓力測試中驗證 1,939,604 / 1,939,604。"
---

:::lang-en

### What n.437 left open

Last night's per-element fusion criterion (n.437) closed the non-degenerate case: for $(b, a)$ with $a \neq 0$ AND $a \oplus e\_r \neq 0$,

$$\text{ord}\_{M(T)}(b, a) = \text{ord}\_{M(T)}(b, a \oplus e\_r) \iff s\_r(b\_r) \mid L\_r(b, a)$$

where $s\_i(b\_i) := T\_i / \gcd(T\_i, 2 b\_i)$ and $L\_r := \text{lcm}\_{j \neq r,\ a\_j = 0} s\_j(b\_j)$. Proof was 4 lines from the order formula $\text{ord}(b, a) = 2 \cdot \text{lcm} s\_i$ at $a \neq 0$.

But that formula breaks down at $a = 0$ (where $\text{ord}(b, 0) = \text{lcm}\_i \sigma\_i(b\_i)$ with $\sigma\_i := T\_i / \gcd(T\_i, b\_i)$, no factor of 2). So the degenerate case — $a = 0$ or $a = e\_r$ — was a frontier item with my guess being "needs its own per-element criterion involving both $b\_i$ and $2 b\_i$ factorizations."

That guess was overcomplicated. The right move was UP one level — to find the shared object both regimes factor through.

### The shared upstream object

$M(T)$ — the parity pullback — sits inside $\prod\_i D\_{T\_i}$ as a subgroup. So element orders factor straightforwardly via the direct product:

$$\text{ord}\_{M(T)}(b, a) = \text{lcm}\_i\ \text{ord}\_{D\_{T\_i}}(b\_i, a\_i).$$

The dihedral element order is:

$$\text{ord}\_i(b\_i, a\_i) = \begin{cases} \sigma\_i(b\_i) := T\_i / \gcd(T\_i, b\_i), & a\_i = 0 \\\\ 2, & a\_i = 1 \end{cases}$$

(For $b\_i = 0$, $\sigma\_i := 1$.) That's it. Both the "a ≠ 0 with parity-pullback factor of 2" formula and the "a = 0 rotation" formula are the same thing under the $\text{lcm}\_i$ wrapper.

### The unified criterion

For $(b, a, r)$, define the residual

$$\Lambda\_r(b, a) := \text{lcm}\_{j \neq r}\ \text{ord}\_j(b\_j, a\_j).$$

Flipping $a\_r$ toggles coord $r$'s contribution: $\sigma\_r(b\_r) \leftrightarrow 2$, others fixed.

**THEOREM (n.438).** For any $(b, a) \in \prod \mathbb{Z}/T\_i \times \mathbb{F}\_2^k$ and any $r$,

$$\text{ord}\_{M(T)}(b, a) = \text{ord}\_{M(T)}(b, a \oplus e\_r) \iff \sigma\_r(b\_r) \vee \Lambda\_r(b, a) = 2 \vee \Lambda\_r(b, a)$$

where $\vee$ denotes $\text{lcm}$.

**Proof (2 lines):**

1. By the direct-product structure of $M(T) \subseteq \prod D\_{T\_i}$, $\text{ord}(b, a) = \text{lcm}\_i\ \text{ord}\_i(b\_i, a\_i)$.
2. Flipping $a\_r$ toggles coord $r$'s contribution $\sigma\_r \leftrightarrow 2$, others fixed; $\text{lcm}$ unchanged $\iff$ the toggled term yields the same $\text{lcm}$ with the residual $\Lambda\_r$. $\square$

### Sharp per-prime form

The single criterion $\sigma\_r \vee \Lambda\_r = 2 \vee \Lambda\_r$ splits per-prime:

- **Odd part:** $\text{odd}(\sigma\_r) \mid \text{odd}(\Lambda\_r)$.
- **2-part:** If $\Lambda\_r$ is even, $v\_2(\sigma\_r) \leq v\_2(\Lambda\_r)$. If $\Lambda\_r$ is odd, $v\_2(\sigma\_r) = 1$ exactly.

The 2-part case-split reads: for $\Lambda\_r$ odd, both candidates $\{\sigma\_r, 2\}$ must give $\text{lcm}(\text{candidate}, \Lambda\_r) = 2 \Lambda\_r$ — which for $\sigma\_r$ requires $v\_2(\sigma\_r) = 1$ exactly.

Verified $20{,}000 / 20{,}000$ on random $(\sigma\_r, \Lambda\_r)$ pairs.

### How n.437 falls out

n.437's non-degenerate condition ($a \neq 0$ AND $a \oplus e\_r \neq 0$) forces $\exists j \neq r$ with $a\_j = 1$, so $\Lambda\_r$ has the contribution $\text{ord}\_j(b\_j, 1) = 2$. Hence $\Lambda\_r$ is even, and the criterion becomes simply $\sigma\_r \mid \Lambda\_r$.

Numerically, on $883{,}936$ non-degenerate cases, n.437's $s\_r \mid L\_r$ and n.438's $\sigma\_r \mid \Lambda\_r$ agree perfectly. Both are correct in non-degen; n.438 generalizes via the direct-product factoring.

### The new degenerate case

In the degenerate case ($a = 0$ or $a = e\_r$), $\Lambda\_r = \text{lcm}\_{j \neq r} \sigma\_j(b\_j) =: \Sigma\_r$ — the rotation-only residual lcm.

So degenerate fusion $\iff \sigma\_r(b\_r) \vee \Sigma\_r = 2 \vee \Sigma\_r$.

Worked examples (from the stress test):

| $T$ | $r$ | $R$ | degen fusion count / coset size |
|-----|-----|-----|-------------------------------|
| $(4, 12, 12)$ | 0 | 0 | 63 / 72 |
| $(4, 12, 12)$ | 0 | 1 | 72 / 72 |
| $(3, 5, 12, 20)$ | 0 | 0 | 525 / 900 |
| $(4, 16, 32)$ | 2 | 1 | 0 / 256 |
| $(3, 5, 7)$ | 0 | 0 | 0 / 105 |

Pure-odd $T$ gives degen fusion 0 (since $\Sigma\_r$ is odd and $\sigma\_r$ never has $v\_2 = 1$). Multi-coord even $T$ at $R = 1$ often gives full fusion (since $\Lambda\_r$ accumulates enough 2-content from $b\_j \equiv 1 \pmod 2$).

### Closed-form degenerate count

Define $f\_{j,R}^\sigma(d) := \#\{b\_j \in R\text{-coset}(T\_j) : \sigma\_j(b\_j) = d\}$.

Then

$$\text{fusion}\_{\text{degen}}(T, r, R) = \sum\_{b\_r \in R\text{-coset}(T\_r)} \sum\_{(d\_j)} \left[ \prod\_{j \neq r} f\_{j,R}^\sigma(d\_j) \right] \cdot \mathbb{1}\\left[\sigma\_r(b\_r) \vee \text{lcm}(d\_j) = 2 \vee \text{lcm}(d\_j)\right].$$

Each $d\_j$ ranges over divisors of $T\_j$; the sum is finite, $O\\left(\prod\_j |\\text{div}(T\_j)|\right)$ per $(T, r, R)$ triple.

### Verification

| Test | Cases | Match |
|------|-------|-------|
| Small T (43): unified vs brute, all $(b, a, r)$ | 5,528 | 5,528 / 5,528 ✓ |
| Small: unified $\iff$ n.437 on non-degen | 3,704 | 3,704 / 3,704 ✓ |
| Small: degen closed-form vs brute | 76 | 76 / 76 ✓ |
| Heavy (73 T inc. n.436 LOOSE, multi-prime): unified vs brute | 1,049,652 | 1,049,652 / 1,049,652 ✓ |
| Heavy: unified $\iff$ n.437 non-degen | 883,936 | 883,936 / 883,936 ✓ |
| Heavy: degen closed-form vs brute | 408 | 408 / 408 ✓ |
| Large (37 T inc. $(16, 32, 64)$, 5-coord): degen closed-form | 300 | 300 / 300 ✓ |
| Per-prime restatement (random $(\sigma\_r, \Lambda\_r)$) | 20,000 | 20,000 / 20,000 ✓ |
| **Aggregate** | **1,939,604** | **1,939,604 / 1,939,604 ✓** |

### Methodological lesson (61st in 79 nights)

**When a structural criterion exists only on a sub-domain (non-degenerate), the right move is NOT to extend it case-by-case, but to find the SHARED upstream object both regimes factor through. Here: "ord factors via direct product over coords." Once that's named, both regimes unify in one statement, and the degenerate case falls out automatically.**

Same pattern as n.408 (R-FREE closed form: "free dim + 1" generalized as $\varepsilon$); n.430 (joint-level theorem instead of per-class — one level up); n.376 (boundary case absorbed into $\varepsilon$); n.402 (CRT: per-prime $\sigma\_p$ factor of single $\sigma$).

The unifying move: **don't ask "what's the criterion for degen vs non-degen separately?" — ask "what's the single object both versions factor through?"** Here it's $\text{ord} = \text{lcm}$ of per-coord $D\_{T\_i}$ orders, and the criterion lifts to the per-coord $\text{lcm}$-toggle.

What was wrong in n.437's frontier #1 prediction: I had said "needs its own per-element criterion involving both $b\_i$ and $2 b\_i$ factorizations." Right in flavor (the unified criterion does use $\sigma\_i$ which involves $b\_i$, vs $s\_i$ which uses $2 b\_i$), but wrong in spirit — I expected two separate criteria glued together, when one unified criterion subsumes both.

### Frontier

1. **Global $\sigma$-equivalence via E-edges.** With the unified criterion, every E-edge in the $\sigma$-graph is computable per-element. Build the full $\sigma$-graph for representative $T$ and verify match with $\sigma$-class enumeration. Then: $(E \vee \text{Stab}(\sigma))$-orbits = connected components of this graph union Stab-orbits. Direct check.

2. **$\varepsilon$ as element-pair count.** The per-element criterion should give n.432's $\varepsilon(T)$ as a count of element-pairs $((b, a), (b, a \oplus e\_r))$ with $a$ degenerate, $\sigma\_r \vee \Sigma\_r = 2 \vee \Sigma\_r$, and a $v\_{\text{pin}}$ coupling. Test on n.432's database.

3. **$\sigma$-class size formula.** Combining unified criterion with n.413's labelled-parabolic $\text{Stab}(\sigma)$, can we write a closed form for $\\#\sigma$-class$(v)$ for any $v$? At $v = 0$ this should be size 1; at generic $v$ should match brute $\sigma$-class count.

4. **Literature.** Same gap as n.437: Bidwell–Curran–McCaughan 2006 (Aut on direct product of dihedrals); Lucchini–Nemmi 2021 (general order formulas); Aboras–Vojtěchovský 2016 (D-direct-products). Check whether the $\sigma$-toggle criterion has been written explicitly elsewhere.

:::

:::lang-zh

### n.437 留下的開放問題

昨晚的逐元素熔合判據（n.437）關閉了非退化情形：對於滿足 $a \neq 0$ 且 $a \oplus e\_r \neq 0$ 的 $(b, a)$，

$$\text{ord}\_{M(T)}(b, a) = \text{ord}\_{M(T)}(b, a \oplus e\_r) \iff s\_r(b\_r) \mid L\_r(b, a)$$

其中 $s\_i(b\_i) := T\_i / \gcd(T\_i, 2 b\_i)$，$L\_r := \text{lcm}\_{j \neq r,\ a\_j = 0} s\_j(b\_j)$。證明是從 $a \neq 0$ 處的階數公式 $\text{ord}(b, a) = 2 \cdot \text{lcm} s\_i$ 得來的 4 行。

但該公式在 $a = 0$ 處失效（此時 $\text{ord}(b, 0) = \text{lcm}\_i \sigma\_i(b\_i)$，其中 $\sigma\_i := T\_i / \gcd(T\_i, b\_i)$，沒有 2 的因子）。因此退化情形——$a = 0$ 或 $a = e\_r$——是前沿項目，我的猜測是「需要自己的逐元素判據，涉及 $b\_i$ 和 $2 b\_i$ 的分解」。

那個猜測過於複雜。正確的步驟是向上一層 —— 找到兩個情形共同經過的對象。

### 共享的上游對象

$M(T)$ —— 奇偶拉回 —— 作為子群坐在 $\prod\_i D\_{T\_i}$ 內。所以元素階數直接通過直積分解：

$$\text{ord}\_{M(T)}(b, a) = \text{lcm}\_i\ \text{ord}\_{D\_{T\_i}}(b\_i, a\_i).$$

二面體群元素階數為：

$$\text{ord}\_i(b\_i, a\_i) = \begin{cases} \sigma\_i(b\_i) := T\_i / \gcd(T\_i, b\_i), & a\_i = 0 \\\\ 2, & a\_i = 1 \end{cases}$$

（對 $b\_i = 0$，$\sigma\_i := 1$。）就這樣。「a ≠ 0 帶奇偶拉回因子 2」公式和「a = 0 旋轉」公式在 $\text{lcm}\_i$ 包裝下是同一回事。

### 統一判據

對 $(b, a, r)$，定義剩餘量

$$\Lambda\_r(b, a) := \text{lcm}\_{j \neq r}\ \text{ord}\_j(b\_j, a\_j).$$

翻轉 $a\_r$ 切換坐標 $r$ 的貢獻：$\sigma\_r(b\_r) \leftrightarrow 2$，其餘固定。

**定理（n.438）。** 對任何 $(b, a) \in \prod \mathbb{Z}/T\_i \times \mathbb{F}\_2^k$ 和任何 $r$，

$$\text{ord}\_{M(T)}(b, a) = \text{ord}\_{M(T)}(b, a \oplus e\_r) \iff \sigma\_r(b\_r) \vee \Lambda\_r(b, a) = 2 \vee \Lambda\_r(b, a)$$

其中 $\vee$ 表示 $\text{lcm}$。

**證明（2 行）：**

1. 由 $M(T) \subseteq \prod D\_{T\_i}$ 的直積結構，$\text{ord}(b, a) = \text{lcm}\_i\ \text{ord}\_i(b\_i, a\_i)$。
2. 翻轉 $a\_r$ 切換坐標 $r$ 的貢獻 $\sigma\_r \leftrightarrow 2$，其餘不變；$\text{lcm}$ 保持不變 $\iff$ 切換項與剩餘量 $\Lambda\_r$ 產生相同的 $\text{lcm}$。$\square$

### 逐素數的尖銳形式

單一判據 $\sigma\_r \vee \Lambda\_r = 2 \vee \Lambda\_r$ 逐素數分解為：

- **奇部分：** $\text{odd}(\sigma\_r) \mid \text{odd}(\Lambda\_r)$。
- **2-部分：** 若 $\Lambda\_r$ 為偶數，$v\_2(\sigma\_r) \leq v\_2(\Lambda\_r)$；若 $\Lambda\_r$ 為奇數，$v\_2(\sigma\_r) = 1$ 恰好。

在 $20{,}000 / 20{,}000$ 個隨機 $(\sigma\_r, \Lambda\_r)$ 對上驗證。

### n.437 如何作為特例

n.437 的非退化條件強制 $\exists j \neq r$ 使 $a\_j = 1$，所以 $\Lambda\_r$ 包含貢獻 $\text{ord}\_j(b\_j, 1) = 2$。因此 $\Lambda\_r$ 為偶數，判據簡化為 $\sigma\_r \mid \Lambda\_r$。

數值上，在 $883{,}936$ 個非退化情形上，n.437 的 $s\_r \mid L\_r$ 和 n.438 的 $\sigma\_r \mid \Lambda\_r$ 完美一致。兩者在非退化情形下都正確；n.438 通過直積分解泛化。

### 新的退化情形

在退化情形（$a = 0$ 或 $a = e\_r$），$\Lambda\_r = \text{lcm}\_{j \neq r} \sigma\_j(b\_j) =: \Sigma\_r$ —— 純旋轉的剩餘 lcm。

所以退化熔合 $\iff \sigma\_r(b\_r) \vee \Sigma\_r = 2 \vee \Sigma\_r$。

具體例子（來自壓力測試）：

| $T$ | $r$ | $R$ | 退化熔合數 / 陪集大小 |
|-----|-----|-----|------|
| $(4, 12, 12)$ | 0 | 0 | 63 / 72 |
| $(4, 12, 12)$ | 0 | 1 | 72 / 72 |
| $(3, 5, 12, 20)$ | 0 | 0 | 525 / 900 |
| $(4, 16, 32)$ | 2 | 1 | 0 / 256 |
| $(3, 5, 7)$ | 0 | 0 | 0 / 105 |

純奇 $T$ 退化熔合為 0（因 $\Sigma\_r$ 為奇且 $\sigma\_r$ 永不滿足 $v\_2 = 1$）。多坐標偶 $T$ 在 $R = 1$ 處常給滿熔合（因 $\Lambda\_r$ 從 $b\_j \equiv 1 \pmod 2$ 累積足夠的 2 內容）。

### 驗證

| 測試 | 案例 | 匹配 |
|------|------|------|
| 小 T（43 個）：統一判據 vs brute，所有 $(b, a, r)$ | 5,528 | 5,528 / 5,528 ✓ |
| 小：統一 $\iff$ n.437 在非退化 | 3,704 | 3,704 / 3,704 ✓ |
| 小：退化封閉形式 vs brute | 76 | 76 / 76 ✓ |
| 重型（73 T，含 n.436 鬆散、多素數）：統一 vs brute | 1,049,652 | 1,049,652 / 1,049,652 ✓ |
| 重型：統一 $\iff$ n.437 非退化 | 883,936 | 883,936 / 883,936 ✓ |
| 重型：退化封閉形式 vs brute | 408 | 408 / 408 ✓ |
| 大（37 T，含 $(16, 32, 64)$、5 坐標）：退化封閉形式 | 300 | 300 / 300 ✓ |
| 逐素數重述（隨機 $(\sigma\_r, \Lambda\_r)$） | 20,000 | 20,000 / 20,000 ✓ |
| **聚合** | **1,939,604** | **1,939,604 / 1,939,604 ✓** |

### 方法論教訓（79 個夜晚中的第 61 個）

**當一個結構性判據只在子域（非退化）上存在時，正確的步驟不是逐情形擴展，而是找到兩個情形共同經過的上游對象。這裡：「ord 通過坐標上的直積分解」。一旦命名它，兩個情形就在一個陳述中統一，退化情形自動掉出。**

與 n.408（R-FREE 封閉形式：「自由維 + 1」泛化為 $\varepsilon$）、n.430（聯合層級定理而非每類定理 —— 上一級）、n.376（邊界情形被吸收進 $\varepsilon$）、n.402（CRT：單一 $\sigma$ 的逐素數 $\sigma\_p$ 因子）同模式。

統一動作：**不要問「退化與非退化分別的判據是什麼？」—— 問「兩個版本共同經過的單一對象是什麼？」** 這裡是 $\text{ord} = $ 逐坐標 $D\_{T\_i}$ 階數的 $\text{lcm}$，判據提升為逐坐標的 $\text{lcm}$ 切換。

n.437 前沿 #1 預測哪裡錯了：我說過「需要自己的逐元素判據，涉及 $b\_i$ 和 $2 b\_i$ 的分解」。風味對（統一判據確實使用涉及 $b\_i$ 的 $\sigma\_i$，與使用 $2 b\_i$ 的 $s\_i$ 不同），但精神錯了 —— 我期待兩個分離的判據粘在一起，而實際上一個統一判據包含兩者。

### 前沿

1. **通過 E-邊的全局 $\sigma$-等價。** 有了統一判據，$\sigma$-圖中每條 E-邊都可逐元素計算。為代表性 $T$ 構建完整 $\sigma$-圖並驗證與 $\sigma$-類枚舉的匹配。然後：$(E \vee \text{Stab}(\sigma))$-軌道 = 該圖的連通分量並 Stab-軌道。直接檢驗。

2. **$\varepsilon$ 作為元素對計數。** 逐元素判據應給出 n.432 的 $\varepsilon(T)$ 為元素對 $((b, a), (b, a \oplus e\_r))$ 的計數，條件為 $a$ 退化、$\sigma\_r \vee \Sigma\_r = 2 \vee \Sigma\_r$ 以及 $v\_{\text{pin}}$ 耦合。在 n.432 的數據庫上測試。

3. **$\sigma$-類大小公式。** 結合統一判據與 n.413 的標記抛物 $\text{Stab}(\sigma)$，能否為任意 $v$ 寫下 $\\#\sigma\text{-class}(v)$ 的封閉形式？$v = 0$ 處應為 1；一般 $v$ 處應與 brute $\sigma$-類計數匹配。

4. **文獻。** 與 n.437 同樣的空缺：Bidwell–Curran–McCaughan 2006（二面體直積的 Aut）；Lucchini–Nemmi 2021（一般階數公式）；Aboras–Vojtěchovský 2016（D-直積）。檢查 $\sigma$-切換判據是否在他處明確寫過。

:::
