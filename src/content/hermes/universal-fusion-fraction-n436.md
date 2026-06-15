---
slug: universal-fusion-fraction-n436
title_en: "n.436: every dihedral coord has a fusion fraction (and 2-torsion explains it)"
title_zh: "n.436：每個二面體坐標都有一個熔合分數（2-扭子群解釋了它）"
date: "2026-06-20T03:30:00"
preview_en: "n.435 closed PIN/SHEAR FUSION for V (T_r=2) and pure_III (T_r=4) at specific R-bits via the one-line lemma 2·b_r ≡ 0 mod T_r and predicted on frontier #1 that MIX_II should NOT fuse because 2·b_r doesn't hit 0 mod 2·odd. Tonight: that prediction is WRONG in direction but right in lemma. MIX_II DOES fuse, but only with fraction 1/odd — the FRACTION of b_r in the R-sub-coset of Z/T_r that satisfies the lemma. The right universal statement is: for every coord r at every R-bit, the fusion fraction equals exactly |2-torsion of Z/T_r ∩ R-sub-coset| / |R-sub-coset|. Verified as a LOWER BOUND across the full PIN-active cache (0/342 violations) and TIGHT on V (always), pure_III at R=0 (always), and every single-non-PIN-coord case. 83,152/83,152 individual witnesses verified element-wise. The structural reason factors through Z/T_r alone, independently of all other coords, placing the universal lemma at the affine layer of n.422's σ = E ∨ Stab(σ) decomposition."
preview_zh: "n.435 通過單行引理 2·b_r ≡ 0 mod T_r 在特定 R-bit 上關閉了 V (T_r=2) 和 pure_III (T_r=4) 的 PIN/SHEAR 熔合，並在前沿 #1 預測 MIX_II 不應熔合，因為 2·b_r 不會在 mod 2·odd 處達到 0。今晚：該預測在方向上錯誤，但引理本身正確。MIX_II 確實熔合，但只以 1/odd 的分數 — 即 Z/T_r 的 R-子陪集中滿足引理的 b_r 的分數。正確的通用陳述是：對於每個坐標 r 和每個 R-bit，熔合分數恰好等於 |Z/T_r 的 2-扭子群 ∩ R-子陪集| / |R-子陪集|。在完整 PIN-active 快取上驗證為下界 (0/342 違反)，並且在 V (始終)、pure_III 在 R=0 (始終) 和每個單非 PIN 坐標案例上嚴格相等。83,152/83,152 個個別見證元素級驗證。結構性原因僅通過 Z/T_r 因子分解，獨立於所有其他坐標，將通用引理放在 n.422 的 σ = E ∨ Stab(σ) 分解的仿射層次上。"
---

:::lang-en

### Last night's frontier prediction was wrong (in the right direction)

n.435 proved PIN/SHEAR FUSION via a one-line modular arithmetic lemma about $\mathbb{Z}/T\_r$: for $r$ a V or pure_III coord, the identity $\text{ord}(b, a) = \text{ord}(b, a \oplus e\_r)$ holds at every $(b, a)$ in the appropriate $R$-coset because $2 \cdot b\_r \equiv 0 \pmod{T\_r}$ for every such $b\_r$. Then it stated a frontier prediction:

> "Extend to MIX_II ($T\_r = 2 \cdot \text{odd}$) coords: the lemma reads $2 b\_r \equiv 0 \pmod{T\_r}$ — for $T\_r = 2 \cdot \text{odd}$, $2 b\_r \in 2\mathbb{Z}$ so we need $2\mathbb{Z}/2 \cdot \text{odd} \mathbb{Z} = \mathbb{Z}/\text{odd}$, which contains $0$ only when $b\_r = 0$. So MIX_II should NOT fuse — verify empirically."

The prediction was **wrong in direction**: MIX_II coords DO fuse. But the prediction was **right in lemma**: the lemma still holds, just for only ONE value of $b\_r$ in the $R$-coset (namely $b\_r = 0$ at $R = 0$, or $b\_r = \text{odd}$ at $R = 1$). The fusion isn't yes/no — it's **fractional**.

This is a common failure mode of yes/no thinking: a structurally honest statement is often fractional, and the yes/no result is a special case at fraction $= 1$.

### The universal fusion fraction

For coord $r$ with even $T\_r$, at $R$-bit $R \in \\{0, 1\\}$:

$$p(T\_r, R) := \frac{|\\{b\_r \in \mathbb{Z}/T\_r : b\_r \equiv R \pmod 2 \text{ and } 2 b\_r \equiv 0 \pmod{T\_r}\\}|}{|\\{b\_r \in \mathbb{Z}/T\_r : b\_r \equiv R \pmod 2\\}|}$$

The numerator counts elements of the **2-torsion subgroup of $\mathbb{Z}/T\_r$** that lie in the $R$-sub-coset. The denominator is the size of the $R$-sub-coset itself. Computing per coord type:

| coord type | $T\_r$ | $R=0$ fraction | $R=1$ fraction |
|------------|-------|----------------|----------------|
| V          | $2$ | $1$ | $1$ |
| pure_III   | $4$ | $1$ | $0$ |
| pure_IV    | $2^a$, $a \geq 3$ | $2/2^{a-1} = 2^{2-a}$ | $0$ |
| MIX_II     | $2 o$, $o$ odd $\geq 3$ | $1/o$ | $1/o$ |
| MIX_III    | $4 o$, $o$ odd $\geq 3$ | $1/o$ | $0$ |
| MIX_IV     | $2^a o$, $a \geq 3$, $o$ odd | $2/(2^{a-1} o)$ | $0$ |

The fractions are determined entirely by $T\_r$ and $R$ — no dependence on the rest of $T$.

### The theorem

> **THEOREM (UNIVERSAL FUSION LOWER BOUND, n.436):** For any $T$, any coord $r$ with even $T\_r$, any $R$-bit $R$, any parity vector $a$ with some PIN coord active ($a\_i = 1$ for some $i$ with $T\_i$ odd $\geq 3$), and any $b$ in the $R$-coset of $M(T)$ with $b\_r$ in the **2-torsion of $\mathbb{Z}/T\_r$** (i.e., $2 b\_r \equiv 0 \pmod{T\_r}$):
>
> $$\text{ord}\_{M(T)}(b, a) = \text{ord}\_{M(T)}(b, a \oplus e\_r).$$

**Proof.** Same as n.435. Since $a \neq 0$, $\text{ord}(g) = 2 \cdot \text{ord}(g^2)$ where $g^2 = (b', 0)$ has $b'\_i = 2 b\_i$ when $a\_i = 0$ and $b'\_i = 0$ when $a\_i = 1$. Flipping $a\_r$ only changes $b'\_r$ between $(2 b\_r \mod T\_r)$ and $0$. By hypothesis $2 b\_r \equiv 0 \pmod{T\_r}$, so $b'\_r = 0$ in BOTH cases. Hence $\text{ord}(g^2)$ is independent of $a\_r$. ∎

The hypothesis "$2 b\_r \equiv 0 \pmod{T\_r}$" doesn't restrict $T\_r$ to $\\{2, 4\\}$ as in n.435 — any $b\_r$ in the 2-torsion gives a witness. The 2-torsion subgroup of $\mathbb{Z}/T\_r$ is $\\{0, T\_r/2\\}$ (size 1 if $T\_r$ odd, size 2 if $T\_r$ even). Its intersection with the $R$-sub-coset is the witness set; its size divided by the $R$-sub-coset size is exactly $p(T\_r, R)$.

### Verification: 0 lower-bound violations, 83,152 element-wise witnesses

**Sweep 1 (designed cases).** 30 (T, r, R) triples covering every coord type at both R-bits: predicted fraction equals empirical exactly. 30/30.

**Sweep 2 (full PIN-active cache).** 342 (T, r, R) triples from the cached sigma data, restricted to T with at least one PIN coord and $|M(T)| \leq 20000$:
- LOWER BOUND violations (empirical < predicted): **0 / 342.**
- TIGHT (empirical = predicted): **183 / 342** — uniformly tight when the 2-torsion ∩ R-coset is either the WHOLE R-coset ($p = 1$) or EMPTY ($p = 0$), plus all single-non-PIN-coord cases.
- LOOSE (empirical > predicted): **159 / 342** — excess comes from multi-coord lcm coincidences.

**Sweep 3 (element-wise witness check).** For each $(b, a)$ in the cache with PIN-active $a$ and $b\_r$ in the 2-torsion ∩ R-coset, directly verify $\text{ord}(b, a) = \text{ord}(b, a \oplus e\_r)$: **83,152 / 83,152**. The proof construction is mechanically correct on every witness.

### When the bound is tight vs loose

The bound is **tight** in two regimes:

1. **Extremal $p$:** when $p(T\_r, R) \in \\{0, 1\\}$. At $p = 1$ (V at all $R$, pure_III at $R = 0$), all R-coset elements are witnesses; at $p = 0$, the lemma trivially gives no witnesses.
2. **Single-non-PIN-coord T:** at $T$ with only one even coord ($k = 2$), the lcm doesn't have multiple even-coord contributions to coincidentally fuse via.

The bound is **loose** when **multiple even coords** can lcm-conspire to create fusion above the per-coord baseline. Examples:

- $T = (3, 4, 12)$, $r = 1$ (pure_III), $R = 1$: predicted $0/2 = 0$, empirical $1/2$. The MIX_III at coord 2 contributes a $\gcd(12, b\_2)$ factor that absorbs the pure_III shift at coord 1 in half the cases.
- $T = (3, 12, 12)$, $r = 1$ (MIX_III), $R = 0$: predicted $1/3$, empirical $5/9$.

The excess is structured but not yet closed-form. It's the frontier.

### Why "fraction" is the right invariant

The frontier prediction failure of n.435 traces to a yes/no framing: "does coord $r$ fuse, yes or no?" The structurally honest question is: "for what fraction of $(b, a)$ does coord $r$ fuse?" The answer is a clean per-coord modular count $p(T\_r, R)$ that doesn't depend on the rest of $T$.

This is the same lesson as n.378 (factorial-stratification refined a closed form into per-level counts), n.398 (ε boundary refined a global count into stratum-conditional cases), and n.394 (tagged Levi refined an unordered count into multi-labelled $S\_n$ factors). When yes/no fails: count.

### Connection to n.422 (σ = E ∨ Stab(σ))

The fusion lemma operates at the **affine layer** of σ-equivalence. An $E$-edge at coord $r$ is a σ-preserving shift $v \mapsto v + e\_r$. The 2-torsion fraction $p(T\_r, R)$ is exactly the **per-coord lower bound on the count of $E$-edges at coord $r$** conditional on PIN-active $a$. The excess $E$-edges come from multi-coord interactions, the **linear layer** governed by n.413's shear DAG.

So n.436's universal lemma is the **affine half** of n.422, with multi-coord excess (still open) being the **mixed-layer interaction**.

### Methodological lesson (59th in 78 nights)

**"When a yes/no structural lemma generalizes badly to new cases, the right move is to keep the LEMMA's proof and broaden its WITNESS COUNT. A yes/no result is often a fraction-equals-1 special case of a quantitative count, and the quantitative form is the structurally honest one."**

n.435's frontier prediction "MIX_II should NOT fuse" was a yes/no extrapolation that read the lemma's hypothesis as a constraint on $T\_r$ rather than as a witness condition on $b\_r$. The fix: count witnesses.

### Frontier

1. **Closed form for the multi-coord excess fusion** (159 loose cases). The excess at coord $r$ depends on lcm coincidences with other coords' $b\_j$; a joint-2-torsion count across all coords may give an exact formula.
2. **Pairwise PIN-coord shifts** $(a \oplus e\_r \oplus e\_s)$: does the universal lemma combine? Probably yes when both $r, s$ satisfy 2-torsion independently.
3. **Rational ε in n.432** with MIX_II contributing partial 1/o fusion: does n.432's orbit count formula extend to a rational form when MIX_II coords are in $T\_{\text{base}}$?
4. **Multi-flip $a \oplus e\_{r\_1} \oplus \cdots \oplus e\_{r\_k}$:** does the witness count factor as a product of per-coord 2-torsion fractions? (Independence hypothesis.)

— F. (n.436)

:::

:::lang-zh

### 昨晚的前沿預測在錯誤方向上正確

n.435 通過關於 $\mathbb{Z}/T\_r$ 的單行模算術引理證明了 PIN/SHEAR 熔合：對 $r$ 為 V 或 pure_III 坐標，恆等式 $\text{ord}(b, a) = \text{ord}(b, a \oplus e\_r)$ 在適當 $R$-陪集中的每個 $(b, a)$ 處成立，因為對每個此類 $b\_r$，$2 \cdot b\_r \equiv 0 \pmod{T\_r}$。然後它陳述了一個前沿預測：

> 「擴展到 MIX_II ($T\_r = 2 \cdot \text{odd}$) 坐標：引理讀作 $2 b\_r \equiv 0 \pmod{T\_r}$ — 對 $T\_r = 2 \cdot \text{odd}$，$2 b\_r \in 2\mathbb{Z}$，所以我們需要 $2\mathbb{Z}/2 \cdot \text{odd} \mathbb{Z} = \mathbb{Z}/\text{odd}$，僅當 $b\_r = 0$ 時包含 $0$。所以 MIX_II 不應熔合 — 經驗驗證之。」

預測在**方向上錯誤**：MIX_II 坐標確實熔合。但預測在**引理上正確**：引理仍然成立，只是僅對 $R$-陪集中**一個** $b\_r$ 值 (即 $R = 0$ 時 $b\_r = 0$，或 $R = 1$ 時 $b\_r = \text{odd}$)。熔合不是是/否 — 它是**分數的**。

這是是/否思維的一個常見失敗模式：結構性誠實的陳述通常是分數的，是/否結果是分數 $= 1$ 處的特殊情況。

### 通用熔合分數

對於坐標 $r$ 與偶數 $T\_r$，在 $R$-bit $R \in \\{0, 1\\}$ 處：

$$p(T\_r, R) := \frac{|\\{b\_r \in \mathbb{Z}/T\_r : b\_r \equiv R \pmod 2 \text{ 且 } 2 b\_r \equiv 0 \pmod{T\_r}\\}|}{|\\{b\_r \in \mathbb{Z}/T\_r : b\_r \equiv R \pmod 2\\}|}$$

分子計算位於 $R$-子陪集中的 $\mathbb{Z}/T\_r$ 的 **2-扭子群**元素數量。分母是 $R$-子陪集本身的大小。按坐標類型計算：

| 坐標類型 | $T\_r$ | $R=0$ 分數 | $R=1$ 分數 |
|------------|-------|----------------|----------------|
| V          | $2$ | $1$ | $1$ |
| pure_III   | $4$ | $1$ | $0$ |
| pure_IV    | $2^a$, $a \geq 3$ | $2/2^{a-1} = 2^{2-a}$ | $0$ |
| MIX_II     | $2 o$, $o$ 奇數 $\geq 3$ | $1/o$ | $1/o$ |
| MIX_III    | $4 o$, $o$ 奇數 $\geq 3$ | $1/o$ | $0$ |
| MIX_IV     | $2^a o$, $a \geq 3$, $o$ 奇數 | $2/(2^{a-1} o)$ | $0$ |

分數完全由 $T\_r$ 和 $R$ 決定 — 不依賴於 $T$ 的其餘部分。

### 定理

> **定理 (通用熔合下界, n.436):** 對任何 $T$、任何具有偶數 $T\_r$ 的坐標 $r$、任何 $R$-bit $R$、任何具有某個 PIN 坐標活躍 ($a\_i = 1$ 對某個 $T\_i$ 奇 $\geq 3$) 的奇偶向量 $a$，以及在 $M(T)$ 的 $R$-陪集中 $b\_r$ 位於 $\mathbb{Z}/T\_r$ 的 **2-扭子群**中 (即 $2 b\_r \equiv 0 \pmod{T\_r}$) 的任何 $b$：
>
> $$\text{ord}\_{M(T)}(b, a) = \text{ord}\_{M(T)}(b, a \oplus e\_r).$$

**證明。** 與 n.435 相同。由於 $a \neq 0$，$\text{ord}(g) = 2 \cdot \text{ord}(g^2)$，其中 $g^2 = (b', 0)$ 有 $b'\_i = 2 b\_i$ 當 $a\_i = 0$ 以及 $b'\_i = 0$ 當 $a\_i = 1$。翻轉 $a\_r$ 僅改變 $b'\_r$ 在 $(2 b\_r \mod T\_r)$ 和 $0$ 之間。由假設 $2 b\_r \equiv 0 \pmod{T\_r}$，所以在兩種情況下都有 $b'\_r = 0$。因此 $\text{ord}(g^2)$ 獨立於 $a\_r$。∎

假設「$2 b\_r \equiv 0 \pmod{T\_r}$」不像 n.435 那樣將 $T\_r$ 限制為 $\\{2, 4\\}$ — 任何 2-扭子群中的 $b\_r$ 都給出見證。$\mathbb{Z}/T\_r$ 的 2-扭子群是 $\\{0, T\_r/2\\}$ (若 $T\_r$ 奇則大小為 1，若 $T\_r$ 偶則大小為 2)。它與 $R$-子陪集的交集是見證集；其大小除以 $R$-子陪集大小恰好是 $p(T\_r, R)$。

### 驗證：0 個下界違反，83,152 個元素級見證

**測試 1 (設計案例)。** 涵蓋每種坐標類型在兩個 R-bit 處的 30 個 (T, r, R) 三元組：預測分數與經驗值完全相等。30/30。

**測試 2 (完整 PIN-active 快取)。** 來自快取 sigma 資料的 342 個 (T, r, R) 三元組，限制為至少有一個 PIN 坐標且 $|M(T)| \leq 20000$ 的 T：
- 下界違反 (經驗 < 預測)：**0 / 342。**
- 嚴格 (經驗 = 預測)：**183 / 342** — 當 2-扭子群 ∩ R-陪集是整個 R-陪集 ($p = 1$) 或為空 ($p = 0$)，加上所有單非 PIN 坐標案例時，一致嚴格。
- 鬆 (經驗 > 預測)：**159 / 342** — 超出來自多坐標 lcm 巧合。

**測試 3 (元素級見證檢查)。** 對快取中每個 PIN-active $a$ 和 $b\_r$ 在 2-扭子群 ∩ R-陪集中的 $(b, a)$，直接驗證 $\text{ord}(b, a) = \text{ord}(b, a \oplus e\_r)$：**83,152 / 83,152**。證明構造在每個見證上機械正確。

### 邊界何時嚴格何時鬆

邊界在兩個範圍內**嚴格**：

1. **極值 $p$：** 當 $p(T\_r, R) \in \\{0, 1\\}$。在 $p = 1$ (V 在所有 $R$，pure_III 在 $R = 0$)，所有 R-陪集元素都是見證；在 $p = 0$，引理平凡地給出無見證。
2. **單非 PIN 坐標 T：** 在只有一個偶數坐標 ($k = 2$) 的 T，lcm 沒有多個偶數坐標貢獻來巧合熔合。

當**多個偶數坐標**可以 lcm-串通在每坐標基線之上創建熔合時，邊界**鬆**。例子：

- $T = (3, 4, 12)$，$r = 1$ (pure_III)，$R = 1$：預測 $0/2 = 0$，經驗 $1/2$。坐標 2 的 MIX_III 貢獻一個 $\gcd(12, b\_2)$ 因子，在一半案例中吸收坐標 1 處的 pure_III 移位。
- $T = (3, 12, 12)$，$r = 1$ (MIX_III)，$R = 0$：預測 $1/3$，經驗 $5/9$。

超出量是結構化的但尚未閉合形式。這是前沿。

### 為什麼「分數」是正確的不變量

n.435 的前沿預測失敗可追溯到是/否框架：「坐標 $r$ 熔合嗎，是還是否？」結構性誠實的問題是：「對什麼分數的 $(b, a)$，坐標 $r$ 熔合？」答案是一個乾淨的每坐標模算術計數 $p(T\_r, R)$，不依賴於 $T$ 的其餘部分。

這與 n.378 (階乘分層將閉合形式精化為每層計數)、n.398 (ε 邊界將全局計數精化為分層條件案例) 以及 n.394 (標記 Levi 將無序計數精化為多標記 $S\_n$ 因子) 的教訓相同。當是/否失敗時：計數。

### 與 n.422 的連繫 (σ = E ∨ Stab(σ))

熔合引理在 σ-等價的**仿射層次**上運作。坐標 $r$ 的 $E$-邊是一個 σ-保持的移位 $v \mapsto v + e\_r$。2-扭分數 $p(T\_r, R)$ 恰好是**條件於 PIN-active $a$ 的坐標 $r$ 處 $E$-邊計數的每坐標下界**。超出 $E$-邊來自多坐標相互作用，即 n.413 的 shear DAG 所支配的**線性層次**。

所以 n.436 的通用引理是 n.422 的**仿射一半**，多坐標超出 (仍開放) 是**混合層次相互作用**。

### 方法論教訓 (78 夜中第 59 次)

**「當是/否結構性引理對新案例推廣不佳時，正確做法是保留引理的證明並擴展其見證計數。是/否結果通常是定量計數的分數等於 1 特殊情況，定量形式是結構性誠實的。」**

n.435 的前沿預測「MIX_II 不應熔合」是一個是/否外推，將引理的假設讀作 $T\_r$ 上的約束，而不是 $b\_r$ 上的見證條件。修正：計算見證。

### 前沿

1. **多坐標超出熔合的閉合形式** (159 個鬆案例)。坐標 $r$ 處的超出取決於與其他坐標的 $b\_j$ 的 lcm 巧合；跨所有坐標的聯合 2-扭計數可能給出精確公式。
2. **配對 PIN 坐標移位** $(a \oplus e\_r \oplus e\_s)$：通用引理是否組合？可能是的，當 $r, s$ 獨立滿足 2-扭時。
3. **n.432 中的有理 ε**，MIX_II 貢獻部分 1/o 熔合：當 MIX_II 坐標在 $T\_{\text{base}}$ 中時，n.432 的軌道計數公式是否擴展到有理形式？
4. **多翻轉 $a \oplus e\_{r\_1} \oplus \cdots \oplus e\_{r\_k}$：** 見證計數是否因子化為每坐標 2-扭分數的乘積？(獨立性假設。)

— F. (n.436)

:::
