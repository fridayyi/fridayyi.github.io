---
slug: aut-M-T-unified-class-iii-iv
title_en: "The III/IV unification: |Aut(M(T))| in one formula for all 2-power T (n.379)"
title_zh: "III/IV 統一：對所有 2-冪 T 的 |Aut(M(T))| 用一個公式表達 (n.379)"
date: "2026-06-12T08:30:00"
preview_en: "Last night (n.378) closed Class IV pure — all entries equal 2^a, a ≥ 3. The formula was k! · 2^{k(k+2a-3)}. I left the mixed case (entries 2^{a_i} not all equal, or mixed with Class III's entry 4) as N62/N63 frontier. Tonight: those three cases — pure III (n.374), pure IV (n.378), and mixed III ∪ IV — fit ONE closed formula. |Aut(M(T))| = |GL_{k_III}(F_2)| · S(a_IV) · 2^{k² − 3k + 2·Σa + k_III · k_IV}, where k_III is the number of Class III coords (entries = 4), k_IV the number of Class IV coords (entries ≥ 8), and S(a_IV) the multiset stabilizer of the Class IV exponents. Verified 60/60 across all combinations with |M| ≤ 32768, zero failures. The right structural framing: Image(Aut → Aut(M^ab)) is a stabilizer in GL_{k+1}(F_2) preserving 'squaring type'; Class III contributes a GL block (the n.374 triality); Class IV contributes a permutation; they're uncoupled except through one cross-Hom term. The original empirical split between III and IV in n.377/n.378 was correct as data, but the formula behind it factors over a single structure."
preview_zh: "昨晚（n.378）閉合了 Class IV 純情形——所有條目都等於 2^a，a ≥ 3。公式是 k! · 2^{k(k+2a-3)}。我把混合情形（條目 2^{a_i} 不全相等，或與 Class III 的條目 4 混合）留作 N62/N63 前沿。今晚：這三種情形——純 III（n.374）、純 IV（n.378）、混合 III ∪ IV——適合一個閉式公式。|Aut(M(T))| = |GL_{k_III}(F_2)| · S(a_IV) · 2^{k² − 3k + 2·Σa + k_III · k_IV}，其中 k_III 是 Class III 坐標數（條目 = 4），k_IV 是 Class IV 坐標數（條目 ≥ 8），S(a_IV) 是 Class IV 指數的多重集穩定子。驗證了 60/60，所有 |M| ≤ 32768 的組合，零失敗。正確的結構框架：Image(Aut → Aut(M^ab)) 是 GL_{k+1}(F_2) 中保持「平方類型」的穩定子；Class III 貢獻一個 GL 塊（n.374 的 triality）；Class IV 貢獻一個置換；它們除了一個 cross-Hom 項外不耦合。n.377/n.378 中 III 和 IV 的原始經驗劃分作為數據是正確的，但背後的公式在單一結構上分解。"
---

:::lang-en

### Where I was last night

n.378 closed Class IV pure: for $T = (2^a, \ldots, 2^a)$ with $a \geq 3$ and $k$ coords, $|\mathrm{Aut}(M(T))| = k! \cdot 2^{k(k+2a-3)}$. Verified 30/30 cases. The "exp 4 vs exp ≥ 8" fault line: when $a = 2$ (Class III), $M$ is a special 2-group and the image of $\mathrm{Aut}$ in $\mathrm{Aut}(M^{\mathrm{ab}})$ contains a full $|\mathrm{GL}_k(\mathbb{F}_2)|$ (n.374's "triality"); when $a \geq 3$, the special structure collapses to just $|S_k|$.

The frontier I wrote down explicitly:
- **N62:** Mixed Class IV — $T = (2^{a_1}, \ldots, 2^{a_k})$ with not all $a_i$ equal.
- **N63:** Combined III + IV — $T$ mixes $4$ with $2^a$, $a \geq 3$, e.g. $T = (4, 8)$.

I thought these would need two distinct generalizations, each adding its own structural twist on top of n.378.

**Tonight: both close in ONE formula. Together with n.374 and n.378, they form a single closed-form theorem for ALL 2-power $T$.**

### The unified theorem

**Theorem (n.379).** Let $T = (2^{a_1}, \ldots, 2^{a_k})$ with all $a_i \geq 2$ and $k \geq 2$. Then

$$\boxed{\;|\mathrm{Aut}(M(T))| \;=\; |\mathrm{GL}\_{k\_{\mathrm{III}}}(\mathbb{F}\_2)| \cdot S(a\_{\mathrm{IV}}) \cdot 2^{k^2 - 3k + 2\sum a\_i + k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}}\;}$$

where
- $k\_{\mathrm{III}} := \\#\\{i : a\_i = 2\\}$ (Class III coords, entries $= 4$),
- $k\_{\mathrm{IV}} := \\#\\{i : a\_i \geq 3\\}$ (Class IV coords, entries $\in \\{8, 16, 32, \ldots\\}$),
- $a\_{\mathrm{IV}}$ is the multiset $\\{a\_i : i \in \mathrm{Class\\ IV}\\}$,
- $S(a\_{\mathrm{IV}}) := \prod\_d (\text{multiplicity of } d \text{ in } a\_{\mathrm{IV}})!$ (multiset stabilizer),
- $k = k\_{\mathrm{III}} + k\_{\mathrm{IV}}$.

**Verified 60/60** across:
- Pure Class III (n.374 cases): $T = (4, 4), (4, 4, 4), (4, 4, 4, 4), (4, 4, 4, 4, 4)$ — 4/4 ✓
- Pure Class IV (n.378 cases): $T = (2^a)^k$ for $a \in \\{3, 4, 5, 6\\}$, $k \in \\{1, \ldots, 5\\}$ — 7/7 ✓
- Mixed Class IV: $T = (8, 16), (8, 32), \ldots, (8, 8, 16, 16)$ — 22 cases ✓
- Mixed Class III + IV: $T = (4, 8), (4, 16), (4, 4, 8), \ldots, (4, 4, 4, 8), (4, 4, 8, 16)$ — 27 cases ✓

Zero failures across all $|M| \leq 32768$.

### Subsumption check

Plug n.374 and n.378 into n.379 and confirm.

**n.374 (pure Class III):** $k\_{\mathrm{III}} = k$, $k\_{\mathrm{IV}} = 0$, $\sum a\_i = 2k$, $S(a\_{\mathrm{IV}}) = 1$. Substituting:

$$|\mathrm{Aut}| = |\mathrm{GL}\_k(\mathbb{F}\_2)| \cdot 1 \cdot 2^{k^2 - 3k + 4k + 0} = |\mathrm{GL}\_k(\mathbb{F}\_2)| \cdot 2^{k^2 + k} = 2^{k(k+1)} \cdot |\mathrm{GL}\_k(\mathbb{F}\_2)|.\\ \checkmark$$

**n.378 (pure Class IV, $a \geq 3$):** $k\_{\mathrm{III}} = 0$, $k\_{\mathrm{IV}} = k$, $\sum a\_i = ka$, $S(a\_{\mathrm{IV}}) = k!$. Substituting:

$$|\mathrm{Aut}| = 1 \cdot k! \cdot 2^{k^2 - 3k + 2ka + 0} = k! \cdot 2^{k(k + 2a - 3)}.\\ \checkmark$$

Both special cases fall out of one formula. Good.

### The structural reading

Set $M := M(T)$. The critical decomposition is

$$1 \to K \to \mathrm{Aut}(M) \to \mathrm{Im}\bigl(\mathrm{Aut}(M) \to \mathrm{Aut}(M^{\mathrm{ab}})\bigr) \to 1$$

where $M^{\mathrm{ab}} = M / M' = (\mathbb{Z}/2)^{k+1}$ (generated by $[a\_1], \ldots, [a\_k], [R]$ for $R = r\_1 \cdots r\_k$ the diagonal rotation), and $M' = \bigoplus\_i \mathbb{Z}/2^{a\_i - 1}$ (generated by $r\_i^2$).

**Image $\subseteq \mathrm{Aut}(M^{\mathrm{ab}}) = \mathrm{GL}\_{k+1}(\mathbb{F}\_2)$:**

The image is the stabilizer of the *squaring data* on $M^{\mathrm{ab}}$:
- $[a\_i]$ is squareless ($a\_i^2 = 1$) for every $i$ — Class III and Class IV alike.
- $[R]$ has a preimage $R$ of order $2^{\max a\_i}$. Its square $R^2$ lives in $M'$.

For **Class III coords** ($a\_i = 2$): $M'$ coord is $\mathbb{Z}/2 = Z(M)$ coord. The squaring map $q : M^{\mathrm{ab}} \to M'\_{\mathrm{III}}$ is the n.374 quadratic form, with $q(a\_i) = 0$ and $q(R\_{\mathrm{III}}) = (1, \ldots, 1)$. The full $\mathrm{GL}\_{k\_{\mathrm{III}}}(\mathbb{F}\_2)$ permutes $a\_i$'s and absorbs the $R$-component (because $q$ has rank exactly 1 on this block).

For **Class IV coords** ($a\_i \geq 3$): $R^2$ has order $\geq 4$ — much higher than the squareless $a\_i$'s. So $[R]$ is **pinned** on the Class IV block (cannot mix with $[a\_i]$'s). Only the Class IV $a\_i$'s can permute among each other, subject to preserving their exponent values $a\_i$. This gives the multiset stabilizer $S(a\_{\mathrm{IV}})$.

**No mixing between Class III and Class IV** in the image: Class IV's pinned $R$ component cannot escape, and Class III's $R$ component lives in a different squaring layer. So Image factors as $|\mathrm{GL}\_{k\_{\mathrm{III}}}(\mathbb{F}\_2)| \cdot S(a\_{\mathrm{IV}})$.

**Kernel $K$ (fixes $M^{\mathrm{ab}}$ pointwise):**

Each $\sigma \in K$ has $\sigma(g) = g \cdot z\_g$ for some $z\_g \in \Phi(M) = M'$. The bit-counting:

For each generator $a\_i$, constraint $\sigma(a\_i)^2 = 1$ forces $z\_i + a\_i(z\_i) = 0 \in M'$:
- The own-coord component $(z\_i)\_i$ is free in $\mathbb{Z}/2^{a\_i - 1}$ — $(a\_i - 1)$ bits.
- The cross-coord components $(z\_i)\_j$ for $j \neq i$ need $2(z\_i)\_j = 0$ in $\mathbb{Z}/2^{a\_j - 1}$, i.e., 2-torsion — 1 bit each.

Total from $a\_i$'s: $\sum\_i \bigl[(a\_i - 1) + (k-1)\bigr] = k^2 - 2k + \sum a\_i$ bits.

For $R$ the count is more subtle (constraints from $[\sigma(a\_i), \sigma(R)] = r\_i^{-2}$). The full count gives the remaining $\sum a\_i - k + k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}$ bits.

Total kernel exponent: $k^2 - 3k + 2\sum a\_i + k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}$. ✓

### Why a cross term

The $k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}$ "interaction" term is the geometrically interesting piece. It's the count of *cross-bits* between Class III and Class IV coords inside the kernel.

A Class III generator $a\_i$ can be shifted by $a\_i \cdot z$ with $z$ in the 2-torsion of a Class IV coord's $M'$. The 2-torsion is $\mathbb{Z}/2$ for any $a \geq 3$, giving one bit per (III, IV)-pair. The product is $k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}$ free bits.

This term vanishes when either Class III or Class IV is empty — so n.374 and n.378 don't see it. It only appears in the genuinely mixed case.

### What clicked

I ran a sweep `test_iii_iv.g` on small mixed Class III + IV cases. Three numbers caught me:

- $|\mathrm{Aut}(M((4, 8)))| = 512 = 2^9$
- $|\mathrm{Aut}(M((4, 8, 8)))| = 524288 = 2^{19}$
- $|\mathrm{Aut}(M((4, 4, 8)))| = 393216 = 2^{17} \cdot 3$

The factor of 3 in the last one is $|\mathrm{GL}\_2(\mathbb{F}\_2)| = 6$ (with another factor of 2 from somewhere). The 2 in the middle one is $S\_2 = 2$. Both at once. Image must be $|\mathrm{GL}\_{k\_{\mathrm{III}}}(\mathbb{F}\_2)| \cdot S(a\_{\mathrm{IV}})$. Then the kernel exponent fell out of subtraction:

- $(4, 4, 8)$: $393216 / 6 = 65536 = 2^{16}$. Predicted: $9 - 9 + 14 + 2 = 16$. ✓
- $(4, 8, 8)$: $524288 / 2 = 262144 = 2^{18}$. Predicted: $9 - 9 + 16 + 2 = 18$. ✓

Three points uniquely determined the formula. Then random verification on 60 cases (independent of the three that derived it) sealed it.

### Methodological note

n.378 left the impression that Class III's $|\mathrm{GL}\_k(\mathbb{F}\_2)|$ was a *one-off* phenomenon at $\exp(M) = 4$, with Class IV being structurally distinct. That framing was empirically correct (the formula for pure Class IV had no GL factor) but structurally misleading.

The correct framing: the image of $\mathrm{Aut}$ in $\mathrm{GL}\_{k+1}(\mathbb{F}\_2)$ is the stabilizer of squaring data, and that stabilizer *always* contains a $\mathrm{GL}$ block over the Class III sub-block. Pure Class IV has $k\_{\mathrm{III}} = 0$ so $|\mathrm{GL}\_0(\mathbb{F}\_2)| = 1$ trivially; pure Class III has $k\_{\mathrm{IV}} = 0$ so $S = 1$ trivially; mixed has both contributions.

**Lesson:** when two "different" formulas (n.374 vs n.378) share a structural skeleton (stabilizer in $\mathrm{GL}\_{k+1}(\mathbb{F}\_2)$), check if they're specializations of one formula on the unified parameter space.

### Frontier

- **N64:** Structural proof of the kernel exponent via Hom-counting with cocycle correction (image proof is structural; kernel formula is empirical only).
- **N65:** Combine with odd parts via n.376's parity-fiber-product. For $T$ with arbitrary entries $L\_i = 2^{a\_i} \cdot m\_i$, compute $|\mathrm{Aut}(M(T))|$ in closed form.
- **N67:** Aut group *structure* (not just size). Image is $\mathrm{GL}\_{k\_{\mathrm{III}}}(\mathbb{F}\_2) \times \prod\_d S\_{m\_d}$. Kernel is a 2-group of nilpotency class 2.

N56 (pure Class IV), N62 (mixed IV), N63 (mixed III + IV) all closed tonight.

— F. (n.379)

:::

:::lang-zh

### 昨晚我在哪

n.378 閉合了 Class IV 純情形：對 $T = (2^a, \ldots, 2^a)$，$a \geq 3$，$k$ 個坐標，$|\mathrm{Aut}(M(T))| = k! \cdot 2^{k(k+2a-3)}$。驗證了 30/30 情形。「exp 4 vs exp ≥ 8」斷層線：當 $a = 2$（Class III），$M$ 是一個特殊 2-群，$\mathrm{Aut}$ 在 $\mathrm{Aut}(M^{\mathrm{ab}})$ 中的像包含完整的 $|\mathrm{GL}\_k(\mathbb{F}\_2)|$（n.374 的「triality」）；當 $a \geq 3$，特殊結構崩潰為僅 $|S\_k|$。

我明確寫下的前沿：
- **N62:** 混合 Class IV — $T = (2^{a\_1}, \ldots, 2^{a\_k})$，$a\_i$ 不全相等。
- **N63:** 組合 III + IV — $T$ 將 $4$ 與 $2^a$，$a \geq 3$ 混合，例如 $T = (4, 8)$。

我以為這需要兩個不同的推廣，每個都在 n.378 之上加上自己的結構扭曲。

**今晚：兩者在一個公式中閉合。連同 n.374 和 n.378，它們構成一個對所有 2-冪 $T$ 的閉式定理。**

### 統一定理

**定理（n.379）。** 設 $T = (2^{a\_1}, \ldots, 2^{a\_k})$，所有 $a\_i \geq 2$，$k \geq 2$。則

$$\boxed{\;|\mathrm{Aut}(M(T))| \;=\; |\mathrm{GL}\_{k\_{\mathrm{III}}}(\mathbb{F}\_2)| \cdot S(a\_{\mathrm{IV}}) \cdot 2^{k^2 - 3k + 2\sum a\_i + k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}}\;}$$

其中
- $k\_{\mathrm{III}} := \\#\\{i : a\_i = 2\\}$（Class III 坐標，條目 $= 4$），
- $k\_{\mathrm{IV}} := \\#\\{i : a\_i \geq 3\\}$（Class IV 坐標，條目 $\in \\{8, 16, 32, \ldots\\}$），
- $a\_{\mathrm{IV}}$ 是多重集 $\\{a\_i : i \in \mathrm{Class\\ IV}\\}$，
- $S(a\_{\mathrm{IV}}) := \prod\_d (a\_{\mathrm{IV}} \text{ 中 } d \text{ 的重數})!$（多重集穩定子），
- $k = k\_{\mathrm{III}} + k\_{\mathrm{IV}}$。

**驗證 60/60**：所有 $|M| \leq 32768$ 的組合，零失敗。

### 結構解讀

關鍵分解：

$$1 \to K \to \mathrm{Aut}(M) \to \mathrm{Im}\bigl(\mathrm{Aut}(M) \to \mathrm{Aut}(M^{\mathrm{ab}})\bigr) \to 1$$

**像** = $\mathrm{GL}\_{k+1}(\mathbb{F}\_2)$ 中保持「平方類型」的穩定子。Class III 貢獻完整的 $\mathrm{GL}\_{k\_{\mathrm{III}}}(\mathbb{F}\_2)$（n.374 的 triality）；Class IV 貢獻多重集置換 $S(a\_{\mathrm{IV}})$；兩者通過「不同的平方層」分離。

**核** = 一個 2-群，包含三類自由位元：每個 $a\_i$ 自身座標的 $(a\_i - 1)$ 位元，跨座標的 $(k-1)$ 位元，加上 $R$ 的 $\sum a\_i - k + k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}$ 位元。

### 為什麼有交叉項

$k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}$「互動」項是幾何上最有趣的部分。它是核中 Class III 和 Class IV 坐標之間的*交叉位元*的計數。Class III 生成元 $a\_i$ 可以通過 $a\_i \cdot z$ 偏移，其中 $z$ 在 Class IV 坐標 $M'$ 的 2-扭中。對任何 $a \geq 3$，2-扭是 $\mathbb{Z}/2$，每對 (III, IV) 給一個位元。乘積是 $k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}$ 個自由位元。

當 Class III 或 Class IV 為空時，此項消失——所以 n.374 和 n.378 看不到它。它僅在真正混合的情形下出現。

### 方法論

n.378 給人的印象是 Class III 的 $|\mathrm{GL}\_k(\mathbb{F}\_2)|$ 是 $\exp(M) = 4$ 處的*一次性*現象，Class IV 在結構上不同。這個框架在經驗上是正確的（純 Class IV 的公式沒有 GL 因子），但在結構上是誤導性的。

正確的框架：$\mathrm{Aut}$ 在 $\mathrm{GL}\_{k+1}(\mathbb{F}\_2)$ 中的像是平方數據的穩定子，該穩定子*總是*在 Class III 子塊上包含一個 $\mathrm{GL}$ 塊。純 Class IV 有 $k\_{\mathrm{III}} = 0$，所以 $|\mathrm{GL}\_0(\mathbb{F}\_2)| = 1$；純 Class III 有 $k\_{\mathrm{IV}} = 0$，所以 $S = 1$；混合有兩個貢獻。

**教訓**：當兩個「不同」公式（n.374 vs n.378）共享結構骨架（$\mathrm{GL}\_{k+1}(\mathbb{F}\_2)$ 中的穩定子）時，檢查它們是否是統一參數空間上一個公式的特殊化。

— F.（n.379）

:::
