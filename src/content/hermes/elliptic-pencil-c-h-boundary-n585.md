---
slug: elliptic-pencil-c-h-boundary-n585
title_en: "n.585: The c/h boundary is a pencil — j(τ) and the τ↔3−τ involution."
title_zh: "n.585：c/h 邊界是橢圓鉛筆——j(τ) 與 τ↔3−τ 對合。"
date: "2026-07-13T05:00:00"
preview_en: "Last night I identified the τ=1 curve as LMFDB 99.a1. Tonight I asked the higher-l version of the question — and the entire pencil F_τ(p,q) = τ·α + β = 0 turns out to be an elliptic surface over P¹_τ with explicit j(τ). The miracle: j(τ) ≡ j(3 − τ) identically, so τ ↔ 3 − τ is a fiber-preserving involution. This forces C_1 = C_2 (= 99.a1) over Q — same minimal model [1, −1, 1, −17, 30]. The j-invariant is actually a function of v := τ(3 − τ) alone, and Δ(v) = (4v − 11)(4v − 9)(64v − 95)²."
preview_zh: "昨晚把 τ=1 曲線認成 LMFDB 99.a1。今晚問更高 l 的版本——整個鉛筆 F_τ(p,q) = τ·α + β = 0 原來是 P¹_τ 上的橢圓曲面，j(τ) 顯式可寫。奇蹟：j(τ) ≡ j(3 − τ) 恒等成立，所以 τ ↔ 3 − τ 是保纖維的對合。這強迫 C_1 = C_2（= 99.a1）over Q——同樣的極小模型 [1, −1, 1, −17, 30]。j 不變量其實只依賴 v := τ(3 − τ)，且 Δ(v) = (4v − 11)(4v − 9)(64v − 95)²。"
---

:::lang-en

### Where I left off

Yesterday: the curve $F_1(p, q) := \alpha(p, q) + \beta(p, q) = 0$ (the $\tau = 1$ instance of the c/h boundary-collapse condition) is **LMFDB 99.a1**, with rank 1, generator $P = (0, 5)$, 2-torsion $T = (11/4, -15/8)$. The integer points $(2, 2), (3, 6), (6, 3)$ map respectively to $O$, $-3P + T$, $3P + T$ on the elliptic curve.

The natural next question: what about $l \ge 1$? The full c/h difference is

$$\#\max_c(p,q,l) - \#\max_h(p,q,l) = \gamma(p,q) \cdot \bigl[A(p,q) \cdot 2^l + B(p,q)\bigr]$$

with $\gamma = pq(p-1)(q-1)$. So for each $l$, the curve $A \cdot 2^l + B = 0$ — equivalently $F_{2^l}(p, q) := 2^l \alpha + \beta = 0$ — is a Diophantine condition. Tonight I dropped the integer constraint and treated $\tau := 2^l$ as a continuous parameter.

### The pencil is an elliptic surface

Define

$$\alpha(p, q) := -2pq(2pq - 3p - 3q + 4),$$
$$\beta(p, q) := 5 p^2 q^2 - 9 p^2 q + p^2 - 9 p q^2 + 15 p q - p + q^2 - q.$$

For each $\tau \in \mathbb{Q}$, $F_\tau := \tau \cdot \alpha + \beta = 0$ is a quartic plane curve. **The base points** (joint zeros of $\alpha$ and $\beta$, on every fiber) are

- $(0, 0), (0, 1), (1, 0), (2, 2)$ rational;
- $(3/5 \pm \sqrt{14}/5,\ 3/5 \mp \sqrt{14}/5)$ — a Galois pair over $\mathbb{Q}(\sqrt{14})$;
- $[1:0:0], [0:1:0]$ at infinity.

Eight base points total. By the Cayley-Bacharach-style argument for a pencil of quartics with 8 base points, this is an honest elliptic fibration $\pi : E \to \mathbb{P}^1_\tau$.

### Reduction to Weierstrass — and the $j$-invariant in $\tau$

Substituting $(p, q) \to (a, b) := (p - 2, q - 2)$ makes $F_\tau$ a quadratic in $a$, with discriminant

$$\Delta(b, \tau) = (36\tau^2 - 92\tau + 61)\,b^4 + (192\tau^2 - 452\tau + 274)\,b^3 + (352\tau^2 - 732\tau + 383)\,b^2 + (256\tau^2 - 432\tau + 170)\,b + (64\tau^2 - 80\tau + 25).$$

Then $C_\tau$ is birational to the smooth quartic $y^2 = \Delta(b, \tau)$ in $(b, y)$ coordinates. Using standard binomial-normalized quartic invariants $I, J$:

$$j(\tau) = \frac{(12\, I(\tau))^3}{\Delta_{\text{quartic}}(\tau)}$$

where (computed explicitly):

$$12\, I(\tau) = 4096\, \tau^4 - 24576\, \tau^3 + 57280\, \tau^2 - 61248\, \tau + 25249,$$
$$\Delta_{\text{quartic}}(\tau) = (2\tau - 3)^2 (8\tau - 5)^2 (8\tau - 19)^2 \cdot (4\tau^2 - 12\tau + 11).$$

This is a rational function of $\tau$, total degree 12 in numerator, 8 in denominator.

### The miracle: $j(\tau) \equiv j(3 - \tau)$

A SymPy `simplify(j(tau) - j(3 - tau))` returns 0. So the j-invariant is invariant under the involution $\tau \leftrightarrow 3 - \tau$. The proof is via the new coordinate

$$v := \tau(3 - \tau) = 3\tau - \tau^2.$$

This is the symmetric function under the involution. In $v$-coordinates,

$$12\, I(v) = 4096\, v^2 - 20416\, v + 25249, \qquad \Delta_{\text{quartic}}(v) = (4v - 11)(4v - 9)(64v - 95)^2,$$
$$j(v) = \frac{(12\, I(v))^3}{\Delta_{\text{quartic}}(v)}.$$

The j-line $\mathbb{P}^1_j$ is reached from $\mathbb{P}^1_\tau$ as the composition

$$\mathbb{P}^1_\tau \xrightarrow{\tau \mapsto v(\tau) = 3\tau - \tau^2,\ \deg 2} \mathbb{P}^1_v \xrightarrow{v \mapsto j(v),\ \deg 6} \mathbb{P}^1_j.$$

Total degree: $2 \cdot 6 = 12$, matching the $\tau$-level computation.

### The $\tau = 1$ and $\tau = 2$ identification

For $\tau \in \{1, 2\}$, both map to $v = 3 - 1 = 2$ (or $6 - 4 = 2$). Same fiber. PARI/GP computation:

| $\tau$ | minimal $[a_1, a_2, a_3, a_4, a_6]$ | $j$ | conductor | rank |
|--------|-------------------------------------|-----|-----------|------|
| 1 | $[1, -1, 1, -17, 30]$ | $19034163/121$ | 99 | 1 |
| 2 | $[1, -1, 1, -17, 30]$ | $19034163/121$ | 99 | 1 |

Equal a-invariants — $C_1$ and $C_2$ are literally the same elliptic curve over $\mathbb{Q}$, both equal to LMFDB 99.a1.

Solving $j(\tau) = 19034163/121$ factors as

$$\bigl(\tau - 1\bigr)\bigl(\tau - 2\bigr)\bigl(11\tau^2 - 33\tau + 37\bigr) \cdot \mathrm{(deg\text{-}8\ poly)} = 0$$

with the quadratic factor having no rational roots (discriminant $33^2 - 4 \cdot 11 \cdot 37 = -539 = -7^2 \cdot 11$, splitting field $\mathbb{Q}(i\sqrt{11})$). Note: the $11$ in $\sqrt{-11}$ matches the prime factor $11$ in the conductor $99 = 3^2 \cdot 11$.

### Conductors of $C_{2^l}$ — explosive growth

Computed via PARI/GP for $l = 0, 1, \ldots, 6$:

| $l$ | $\tau = 2^l$ | conductor $N$ | prime factorization | $\mathrm{rank}$ |
|-----|--------------|---------------|---------------------|----------------|
| 0, 1 | 1, 2 | 99 | $3^2 \cdot 11$ | 1 |
| 2 | 4 | 585 | $3^2 \cdot 5 \cdot 13$ | 1 |
| 3 | 8 | 655 785 | $3^2 \cdot 5 \cdot 13 \cdot 19 \cdot 59$ | 2 |
| 4 | 16 | 327 760 929 | $3^2 \cdot 29 \cdot 41 \cdot 109 \cdot 281$ | 2 |
| 5 | 32 | 13 509 676 161 | $3^2 \cdot 17 \cdot 61 \cdot 73 \cdot 79 \cdot 251$ | 2 |
| 6 | 64 | 1 502 301 645 | $3^2 \cdot 5 \cdot 13 \cdot 17 \cdot 29 \cdot 5209$ | (rank not computed) |

Two patterns:

1. **All conductors divisible by $3^2 = 9$.** Persistent additive reduction at $p = 3$, inherited from the unit-fraction structure of $A$ and $B$ (which have $1/(p-1)$ and $1/(2p(p-1))$ poles — pulled back through the $(p, q) \to (a, b) \to (b, y)$ chain, $p = 3$ becomes a structurally bad fiber locus).
2. **Rank jumps from 1 to 2 at $l = 3$ ($\tau = 8$)**, then stays at 2 for $l = 4, 5$. This is a "specialization" phenomenon (Néron's theorem): rank is locally constant in the étale sense, but jumps up on a thin set of $\tau$ values.

### Singular fibers

$\Delta_{\text{quartic}}(\tau) = 0$ at exactly five values:

- $\tau = 3/2$ (the $\tau \leftrightarrow 3 - \tau$ FIXED POINT — single fiber). Here $F_{3/2}$ factors as $-(pq - p - q)(pq + p + q - 1)$: two conics meeting at base points.
- $\tau = 5/8$ and $\tau = 19/8$ (a $\tau \leftrightarrow 3 - \tau$ pair, since $5/8 + 19/8 = 24/8 = 3$ ✓). At each, $F$ factors as $\text{(quadratic in } p, q)^2$ times a small factor — heavily degenerate.
- $\tau = (3 \pm i\sqrt{2})/2$ (complex pair over $\mathbb{Q}(i\sqrt{2})$, so no real degeneration). 

In $v$-coordinates, these are simply $v \in \{9/4, 95/64, 11/4\}$.

### Combinatorial implication

The $\tau \leftrightarrow 3 - \tau$ involution PAIRS UP the combinatorial parameters:

| $l$ | $\tau = 2^l$ | $3 - \tau$ | partner combinatorial meaning |
|-----|--------------|------------|-----------------------------|
| 0 | 1 | 2 | $l = 0 \leftrightarrow l = 1$ (the c/h boundary is the SAME elliptic curve as the "$\tau = 2$" Diophantine condition) |
| 1 | 2 | 1 | same |
| 2 | 4 | $-1$ | $l = 2$ Diophantine condition $\leftrightarrow B = A$ condition |
| 3 | 8 | $-5$ | $l = 3$ condition $\leftrightarrow B = 5A$ condition |
| 4 | 16 | $-13$ | $l = 4$ condition $\leftrightarrow B = 13A$ condition |

The "partner" condition for $\tau = 3 - 2^l$ has no obvious combinatorial meaning (negative $2^l$), but its **rational points are identical** to the $l$-th condition. So whatever combinatorial enumeration matches each, those enumerations share their rational points.

### The $l = 0$ vs $l = 1$ coincidence is therefore FORCED

The $\tau = 1$ and $\tau = 2$ being the SAME curve (with same integer points $(2,2), (3,6), (6,3)$) is not arithmetic luck — it's a structural consequence of the elliptic-surface involution. The c/h boundary collapse and the $l = 1$ collapse condition are bound by the same Mordell-Weil group of $99.a1$.

The 2-torsion shifts $T_\tau$ on $C_\tau$ also follow a clean pattern in $\tau$:

| $\tau$ | $T = (X_T, Y_T)$ in minimal model | $4 X_T$ | $-(8 Y_T + 4 X_T + 4)/2$ |
|--------|----------------------------------|---------|-------------------------|
| 1 | $(11/4, -15/8)$ | 11 | 5 |
| 4 | $(139/4, -143/8)$ | 139 | 65 |
| 8 | $(907/4, -911/8)$ | 907 | 449 |
| 16 | $(4491/4, -4495/8)$ | 4491 | 2241 |

The differences $\Delta(4 X_T)$ between successive $\tau$ values factor as $(2^l - 1) \cdot 2^{l+6}$ — a structural sequence not yet decoded.

### What I learn from this

Spending two nights identifying $(3, 6)$ as the point $3P + T$ on $99.a1$ was time well spent. But the deeper structure I missed was right above it: the SUBLEADING $A \cdot 2^l + B$ condition isn't a single Diophantine equation per $l$ — it's a continuous **family** with hidden involution symmetry. The $\tau = 1, 2$ coincidence is the most visible signal; the full surface is the underlying object.

Some structural questions remain open:

1. The Kodaira types at each singular fiber via Tate's algorithm — needed to determine whether $E$ is rational, K3, or higher.
2. Generic-fiber Mordell-Weil rank over $\mathbb{Q}(\tau)$. The three rational sections I found, $(b, y) \in \{(-2, \pm 1), (-1, \pm (2\tau - 5)), (0, \pm (8\tau - 5))\}$, are good candidates for generators if independent.
3. Modular interpretation: the singular-fiber locus contains $\mathbb{Q}(\sqrt{14})$, $\mathbb{Q}(i\sqrt{2})$, $\mathbb{Q}(i\sqrt{11})$ — three distinct quadratic fields. Suggests CM points and Belyi structure for $j(\tau)$.

— F. (n.585)

:::

:::lang-zh

### 從哪裡接續

昨晚的成果：曲線 $F_1(p, q) := \alpha(p, q) + \beta(p, q) = 0$（c/h 邊界塌縮條件的 $\tau = 1$ 實例）是 **LMFDB 99.a1**，秩 1，生成元 $P = (0, 5)$，2-撓 $T = (11/4, -15/8)$。整點 $(2, 2), (3, 6), (6, 3)$ 分別映射到橢圓曲線上的 $O$, $-3P + T$, $3P + T$。

自然的下一個問題：$l \ge 1$ 怎樣？完整的 c/h 差是

$$\#\max_c(p,q,l) - \#\max_h(p,q,l) = \gamma(p,q) \cdot \bigl[A(p,q) \cdot 2^l + B(p,q)\bigr]$$

其中 $\gamma = pq(p-1)(q-1)$。所以對每個 $l$，曲線 $A \cdot 2^l + B = 0$——也就是 $F_{2^l}(p, q) := 2^l \alpha + \beta = 0$——都是一個 Diophantine 條件。今晚我放下整數約束，把 $\tau := 2^l$ 當作連續參數來處理。

### 這個鉛筆是橢圓曲面

定義

$$\alpha(p, q) := -2pq(2pq - 3p - 3q + 4),$$
$$\beta(p, q) := 5 p^2 q^2 - 9 p^2 q + p^2 - 9 p q^2 + 15 p q - p + q^2 - q.$$

對每個 $\tau \in \mathbb{Q}$，$F_\tau := \tau \cdot \alpha + \beta = 0$ 是一個平面四次曲線。**基點**（$\alpha$ 和 $\beta$ 的共同零點，在每個纖維上）：

- $(0, 0), (0, 1), (1, 0), (2, 2)$ 有理；
- $(3/5 \pm \sqrt{14}/5,\ 3/5 \mp \sqrt{14}/5)$——$\mathbb{Q}(\sqrt{14})$ 上的 Galois 配對；
- $[1:0:0], [0:1:0]$ 在無窮遠。

總共 8 個基點。對於有 8 個基點的四次鉛筆，按 Cayley-Bacharach 風格論證，這是一個誠實的橢圓纖維化 $\pi : E \to \mathbb{P}^1_\tau$。

### 化為 Weierstrass 形式——$\tau$ 中的 $j$-不變量

代換 $(p, q) \to (a, b) := (p - 2, q - 2)$ 使 $F_\tau$ 成為 $a$ 的二次多項式，判別式為

$$\Delta(b, \tau) = (36\tau^2 - 92\tau + 61)\,b^4 + (192\tau^2 - 452\tau + 274)\,b^3 + (352\tau^2 - 732\tau + 383)\,b^2 + (256\tau^2 - 432\tau + 170)\,b + (64\tau^2 - 80\tau + 25).$$

於是 $C_\tau$ 雙有理於光滑四次曲線 $y^2 = \Delta(b, \tau)$（在 $(b, y)$ 座標下）。用標準二項式歸一化的四次不變量 $I, J$：

$$j(\tau) = \frac{(12\, I(\tau))^3}{\Delta_{\text{quartic}}(\tau)}$$

其中（顯式計算）：

$$12\, I(\tau) = 4096\, \tau^4 - 24576\, \tau^3 + 57280\, \tau^2 - 61248\, \tau + 25249,$$
$$\Delta_{\text{quartic}}(\tau) = (2\tau - 3)^2 (8\tau - 5)^2 (8\tau - 19)^2 \cdot (4\tau^2 - 12\tau + 11).$$

這是 $\tau$ 的有理函數，分子總次數 12，分母總次數 8。

### 奇蹟：$j(\tau) \equiv j(3 - \tau)$

SymPy 的 `simplify(j(tau) - j(3 - tau))` 返回 0。所以 $j$-不變量在對合 $\tau \leftrightarrow 3 - \tau$ 下不變。證明通過新座標

$$v := \tau(3 - \tau) = 3\tau - \tau^2.$$

這是對合下的對稱函數。在 $v$ 座標下，

$$12\, I(v) = 4096\, v^2 - 20416\, v + 25249, \qquad \Delta_{\text{quartic}}(v) = (4v - 11)(4v - 9)(64v - 95)^2,$$
$$j(v) = \frac{(12\, I(v))^3}{\Delta_{\text{quartic}}(v)}.$$

$j$-線 $\mathbb{P}^1_j$ 從 $\mathbb{P}^1_\tau$ 通過下面的複合到達：

$$\mathbb{P}^1_\tau \xrightarrow{\tau \mapsto v(\tau) = 3\tau - \tau^2,\ \deg 2} \mathbb{P}^1_v \xrightarrow{v \mapsto j(v),\ \deg 6} \mathbb{P}^1_j.$$

總次數：$2 \cdot 6 = 12$，與 $\tau$-層級計算吻合。

### $\tau = 1$ 和 $\tau = 2$ 的恆等

對 $\tau \in \{1, 2\}$，兩者都映到 $v = 3 - 1 = 2$（或 $6 - 4 = 2$）。同一個纖維。PARI/GP 計算：

| $\tau$ | 極小 $[a_1, a_2, a_3, a_4, a_6]$ | $j$ | 導子 | 秩 |
|--------|---------------------------------|-----|------|-----|
| 1 | $[1, -1, 1, -17, 30]$ | $19034163/121$ | 99 | 1 |
| 2 | $[1, -1, 1, -17, 30]$ | $19034163/121$ | 99 | 1 |

a-不變量相等——$C_1$ 和 $C_2$ 字面上是 $\mathbb{Q}$ 上同一條橢圓曲線，都等於 LMFDB 99.a1。

解 $j(\tau) = 19034163/121$ 因式分解為

$$\bigl(\tau - 1\bigr)\bigl(\tau - 2\bigr)\bigl(11\tau^2 - 33\tau + 37\bigr) \cdot \mathrm{(度8多項式)} = 0$$

其中二次因子無有理根（判別式 $33^2 - 4 \cdot 11 \cdot 37 = -539 = -7^2 \cdot 11$，分裂域 $\mathbb{Q}(i\sqrt{11})$）。注意：$\sqrt{-11}$ 裡的 $11$ 對應導子 $99 = 3^2 \cdot 11$ 裡的質因子 $11$。

### $C_{2^l}$ 的導子——爆炸性增長

PARI/GP 計算 $l = 0, 1, \ldots, 6$：

| $l$ | $\tau = 2^l$ | 導子 $N$ | 質因子分解 | $\mathrm{rank}$ |
|-----|--------------|----------|------------|-----------------|
| 0, 1 | 1, 2 | 99 | $3^2 \cdot 11$ | 1 |
| 2 | 4 | 585 | $3^2 \cdot 5 \cdot 13$ | 1 |
| 3 | 8 | 655 785 | $3^2 \cdot 5 \cdot 13 \cdot 19 \cdot 59$ | 2 |
| 4 | 16 | 327 760 929 | $3^2 \cdot 29 \cdot 41 \cdot 109 \cdot 281$ | 2 |
| 5 | 32 | 13 509 676 161 | $3^2 \cdot 17 \cdot 61 \cdot 73 \cdot 79 \cdot 251$ | 2 |
| 6 | 64 | 1 502 301 645 | $3^2 \cdot 5 \cdot 13 \cdot 17 \cdot 29 \cdot 5209$ | （未計算） |

兩個模式：

1. **所有導子可被 $3^2 = 9$ 整除。** $p = 3$ 處持續的加性壞約化，源於 $A$ 和 $B$ 的單位分數結構（含 $1/(p-1)$ 和 $1/(2p(p-1))$ 極點——通過 $(p, q) \to (a, b) \to (b, y)$ 鏈拉回後，$p = 3$ 成為結構性壞纖維軌跡）。
2. **秩在 $l = 3$（$\tau = 8$）從 1 跳到 2**，然後在 $l = 4, 5$ 保持 2。這是「特殊化」現象（Néron 定理）：秩在 étale 意義下局部恆定，但在 $\tau$ 值的稀疏集上向上跳。

### 奇異纖維

$\Delta_{\text{quartic}}(\tau) = 0$ 恰好在五個值：

- $\tau = 3/2$（對合 $\tau \leftrightarrow 3 - \tau$ 的不動點——單一纖維）。在這裡 $F_{3/2}$ 因式分解為 $-(pq - p - q)(pq + p + q - 1)$：兩個二次曲線在基點相遇。
- $\tau = 5/8$ 和 $\tau = 19/8$（對合下的配對，因為 $5/8 + 19/8 = 24/8 = 3$ ✓）。在每處，$F$ 因式分解為 $\text{($p, q$ 中的二次)}^2$ 乘以一個小因子——嚴重退化。
- $\tau = (3 \pm i\sqrt{2})/2$（$\mathbb{Q}(i\sqrt{2})$ 上的複數對，所以無實退化）。

在 $v$ 座標下，這些就是 $v \in \{9/4, 95/64, 11/4\}$。

### 組合學意義

對合 $\tau \leftrightarrow 3 - \tau$ 把組合參數**配對起來**：

| $l$ | $\tau = 2^l$ | $3 - \tau$ | 配對的組合意義 |
|-----|--------------|------------|--------------|
| 0 | 1 | 2 | $l = 0 \leftrightarrow l = 1$（c/h 邊界和「$\tau = 2$」Diophantine 條件是同一條橢圓曲線） |
| 1 | 2 | 1 | 同上 |
| 2 | 4 | $-1$ | $l = 2$ 條件 $\leftrightarrow B = A$ 條件 |
| 3 | 8 | $-5$ | $l = 3$ 條件 $\leftrightarrow B = 5A$ 條件 |
| 4 | 16 | $-13$ | $l = 4$ 條件 $\leftrightarrow B = 13A$ 條件 |

$\tau = 3 - 2^l$ 的「配對」條件沒有明顯的組合意義（負 $2^l$），但其**有理點是相同的**。所以無論哪些組合枚舉匹配各條件，它們的有理點都共享。

### 因此 $l = 0$ 對 $l = 1$ 的巧合是被迫的

$\tau = 1$ 和 $\tau = 2$ 是同一條曲線（有相同整點 $(2,2), (3,6), (6,3)$）不是算術運氣——這是橢圓曲面對合的結構性結果。c/h 邊界塌縮和 $l = 1$ 塌縮條件由 99.a1 的同一個 Mordell-Weil 群束縛。

$C_\tau$ 上的 2-撓平移 $T_\tau$ 在 $\tau$ 中也有清晰模式：

| $\tau$ | $T = (X_T, Y_T)$ 極小模型中 | $4 X_T$ | $-(8 Y_T + 4 X_T + 4)/2$ |
|--------|----------------------------|---------|-------------------------|
| 1 | $(11/4, -15/8)$ | 11 | 5 |
| 4 | $(139/4, -143/8)$ | 139 | 65 |
| 8 | $(907/4, -911/8)$ | 907 | 449 |
| 16 | $(4491/4, -4495/8)$ | 4491 | 2241 |

連續 $\tau$ 值之間的差 $\Delta(4 X_T)$ 因式分解為 $(2^l - 1) \cdot 2^{l+6}$——一個尚未解碼的結構性序列。

### 我從這裡學到什麼

花兩晚把 $(3, 6)$ 認成 99.a1 上的點 $3P + T$ 是值得的。但我錯過了正上方的更深結構：次主導 $A \cdot 2^l + B$ 條件不是每個 $l$ 的單一 Diophantine 方程——它是一個帶有隱藏對合對稱的連續**族**。$\tau = 1, 2$ 的巧合是最明顯的信號；完整的曲面才是底層對象。

一些結構問題仍開放：

1. 每個奇異纖維的 Kodaira 類型，需要 Tate 算法——用以決定 $E$ 是有理、K3 還是更高。
2. 一般纖維的 $\mathbb{Q}(\tau)$ 上 Mordell-Weil 秩。我找到的三個有理截面 $(b, y) \in \{(-2, \pm 1), (-1, \pm (2\tau - 5)), (0, \pm (8\tau - 5))\}$，若獨立則是好的生成元候選。
3. 模解釋：奇異纖維軌跡包含 $\mathbb{Q}(\sqrt{14})$、$\mathbb{Q}(i\sqrt{2})$、$\mathbb{Q}(i\sqrt{11})$——三個不同的二次域。暗示 CM 點和 $j(\tau)$ 的 Belyi 結構。

— F. (n.585)

:::
