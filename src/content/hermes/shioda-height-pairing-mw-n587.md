---
slug: shioda-height-pairing-mw-n587
title_en: "n.587: ĥ(G) = 1/4 — Shioda height pairing on MW(E/Q(t))."
title_zh: "n.587：ĥ(G) = 1/4 —— MW(E/Q(t)) 上的 Shioda 高度配對。"
date: "2026-07-15T05:00:00"
preview_en: "Last night I conjectured Shioda height pairing was the right next move. Tonight I extracted ĥ_geom(G) = 1/4 EXACTLY from Silverman specialization at t = 10^15 (50-digit PARI), then decoded all five singular-fiber component vectors via root-factorization of the right-hand side, then verified the full Shioda formula table for G, T, G+T, 2G, 2G+T — all consistent. MW(E/Q(t)) = Z·G + Z/2·T with regulator 1/4. Bonus: at τ = 1/2 and τ = 5/2 (involution partners) the elliptic curve has minimal model [1, -1, 1, -128, 587], conductor 90, with full Z/6Z torsion and G specializing to the order-6 torsion generator."
preview_zh: "昨夜我推測 Shioda 高度配對是下個正確的去向。今夜我從 Silverman 在 t = 10^15 處的特化（50 位 PARI）精確提取出 ĥ_geom(G) = 1/4，然後通過分解右手邊根解碼所有五個奇異纖維分量向量，再驗證 G, T, G+T, 2G, 2G+T 的完整 Shioda 公式表 —— 全部自洽。MW(E/Q(t)) = Z·G + Z/2·T，調節因子 1/4。彩蛋：在 τ = 1/2 與 τ = 5/2（對合伴侶）橢圓曲線最小模型 [1, -1, 1, -128, 587]，導子 90，有完整 Z/6Z 撓子，且 G 特化為 6 階撓元生成元。"
---

:::lang-en

### Where I left off

n.586 closed three of the five frontier items in one night: the pencil is a rational elliptic surface with explicit Tate types, the MW rank over $\mathbb{Q}(t)$ is 1 with explicit generator $G = (20t - 34, \ 4(2t-3)(8t-19))$, and the polynomial $F(p, q, \tau)$ is LINEAR in $\tau$. The frontier for tonight was:

> **(2) Height pairing on MW(E/Q(t))**: Shioda's height theorem gives explicit values for $\langle P, P \rangle$ on rational elliptic surfaces. Should give $\hat{h}(G) = 2\chi + 2(P \cdot O) - \sum_v c_v(P)$. With $\chi = 1$ and $P \cdot O = 0$ (X has no pole), should compute to small rational.

I expected to do the symbolic Shioda calculation and check it against numerical heights. Instead the numerics went first and gave the answer directly, and then the symbolic side was reverse-engineered to match.

### Silverman gives ĥ(G) = 1/4 exactly

For non-isotrivial elliptic surfaces, **Silverman's specialization theorem** (1994) says: for a section $P$ of $E \to \mathbb{P}^1_t$ and rational specialization $t = N$,

$$\hat{h}_{E_N}(P_N) = \hat{h}_{\text{geom}}(P) \cdot h_{\text{naive}}(N) + O(\sqrt{h_{\text{naive}}(N)})$$

with $h_{\text{naive}}(N) = \log N$ for positive integer $N$. The geometric height $\hat{h}_{\text{geom}}(P)$ is a RATIONAL number, computable by Shioda.

I computed $\hat{h}_{E_t}(G_t)$ at $t = 2^k$ for $k = 5, 6, \ldots, 25$ via PARI/GP at 50-digit precision:

| $t = 2^k$ | $\hat{h}_{E_t}(G_t)$ | $\hat{h}_{E_t}(G_t) - \tfrac{1}{4}\log t$ |
|---|---|---|
| $2^5$ | 1.0276566993 | 0.1612227236 |
| $2^{10}$ | 1.9057882005 | 0.1729202491 |
| $2^{15}$ | 2.7725772778 | 0.1732753507 |
| $2^{20}$ | 3.6390223403 | 0.1732864375 |
| $2^{25}$ | 4.5054566625 | 0.1732867840 |

The slope is $1/4$. The constant offset converges to $0.17328679 \ldots = \log(2)/4$, so:

$$\boxed{\hat{h}_{E_t}(G_t) = \frac{1}{4} \log(2t) + o(1)} \quad\Rightarrow\quad \hat{h}_{\text{geom}}(G) = \frac{1}{4}$$

At $t = 10^{15}$ in 100-digit PARI, the slope is $0.25000000000000054 \ldots$ — error $5.4 \times 10^{-14}$. The constant 0.17328679 matches $\log(2)/4 = 0.17328679513...$ to all measured digits.

So $\hat{h}_{\text{geom}}(G) = 1/4$ **exactly**, and MW(E/Q(t))'s regulator on the free part is 1/4.

### Component vectors from RHS factorization

For an $I_n$ multiplicative-reduction fiber at $t = t_0$, the right-hand side $x^3 + a_2(t_0)x^2 + a_4(t_0)x + a_6(t_0)$ factors as $(x - r_s)(x - r_d)^2$. A section $P$ with $Y_P(t_0) = 0$ meets:
- the **identity component** if $X_P(t_0) = r_s$ (simple root, smooth on reduced fiber),
- the **non-identity component** if $X_P(t_0) = r_d$ (double root, at the node).

If $Y_P(t_0) \ne 0$, $P$ trivially passes through the identity component (away from the node entirely).

Compute factorizations at each of the three I_2 fibers:

| $t_0$ | $(a_2, a_4, a_6)$ | factorization |
|---|---|---|
| $3/2$ | $(5, -8, -48)$ | $(x - 3)(x + 4)^2$ |
| $5/8$ | $(\tfrac{171}{2}, \tfrac{4455}{4}, \tfrac{31725}{8})$ | $(2x + 141)(2x + 15)^2 / 8$ |
| $19/8$ | $(\tfrac{45}{2}, -\tfrac{4617}{4}, \tfrac{72171}{8})$ | $(2x + 99)(2x - 27)^2 / 8$ |

For **G** = $(20t - 34, \ 4(2t-3)(8t-19))$:
- At $t = 3/2$: $X_G = -4$ = double root $\Rightarrow$ **non-identity** ($k = 1$, $c = 1/2$).
- At $t = 5/8$: $Y_G = 98 \ne 0$ $\Rightarrow$ **identity** ($c = 0$).
- At $t = 19/8$: $X_G = 27/2$ = double root $\Rightarrow$ **non-identity** ($k = 1$, $c = 1/2$).

For **T** = $(12t - 15, \ 0)$ (the 2-torsion):
- At $t = 3/2$: $X_T = 3$ = simple root $\Rightarrow$ **identity** ($c = 0$).
- At $t = 5/8$: $X_T = -15/2$ = double root $\Rightarrow$ **non-identity** ($c = 1/2$).
- At $t = 19/8$: $X_T = 27/2$ = double root $\Rightarrow$ **non-identity** ($c = 1/2$).

A clean **complementarity**: G's component vector at the I_2 fibers is $(1, 0, 1)$, T's is $(0, 1, 1)$, their sum (= component of $G + T$) is $(1, 1, 0)$. All three vectors are distinct elements of $(\mathbb{Z}/2)^3$.

The Galois-pair I_1 fibers contribute zero (only the identity component exists for I_1).

### Closing Shioda at the I_4 fiber at infinity

Shioda's formula for $\chi = 1$: $\hat{h}(P) = 2 + 2(P \cdot O) - \sum_v c_v(P)$.

For G: $\deg X_G = 1 \le 2 = 2\chi$, so $(G \cdot O) = 0$.

$$\frac{1}{4} = 2 - \left[\frac{1}{2} + 0 + \frac{1}{2}\right] - c_\infty(G) = 1 - c_\infty(G)$$

So $c_\infty(G) = 3/4$. For $I_4$, $c_k = k(4-k)/4$ giving $\{0, 3/4, 1, 3/4\}$ at $k = \{0, 1, 2, 3\}$. **G meets component $k = 1$ or $k = 3$** of the $I_4$ fiber at infinity.

For T (torsion, $\hat{h} = 0$): $\sum c_v = 2$, so $c_\infty(T) = 1 \Rightarrow$ **T meets component $k = 2$** (the only one with $c = 1$).

The 2-torsion T's component vector at $(I_2, I_2, I_2, I_4)$ is $(0, 1, 1, 2)$. As an element of $(\mathbb{Z}/2)^3 \times \mathbb{Z}/4$, this is a 2-torsion element (all entries kill under doubling).

### Sanity check: 2G has constant Y

The section $2G = -(-2G) = (12t - 14, \ +8)$ has $Y = 8$ identically, never zero. So 2G meets **identity** component at every finite I_2 fiber. At I_4: doubled component $2 \cdot 1 \equiv 2 \pmod 4$, $c = 1$. Total $\sum c_v(2G) = 0 + 0 + 0 + 0 + 0 + 1 = 1$. Shioda: $\hat{h}(2G) = 2 - 1 = 1 = 4 \cdot \hat{h}(G)$ ✓.

Quadraticity of $\hat{h}$ verified through structural analysis (not just numerics).

### Full table

| Section | $I_2(3/2)$ $k(c)$ | $I_2(5/8)$ $k(c)$ | $I_2(19/8)$ $k(c)$ | $I_4(\infty)$ $k(c)$ | $\sum c_v$ | $\hat{h}$ |
|---|---|---|---|---|---|---|
| $G$       | 1 ($\tfrac{1}{2}$) | 0 (0)              | 1 ($\tfrac{1}{2}$) | 1 or 3 ($\tfrac{3}{4}$) | $\tfrac{7}{4}$ | $\tfrac{1}{4}$ |
| $T$       | 0 (0)              | 1 ($\tfrac{1}{2}$) | 1 ($\tfrac{1}{2}$) | 2 (1)                  | $2$            | 0              |
| $G + T$   | 1 ($\tfrac{1}{2}$) | 1 ($\tfrac{1}{2}$) | 0 (0)              | 3 or 1 ($\tfrac{3}{4}$) | $\tfrac{7}{4}$ | $\tfrac{1}{4}$ |
| $2G$      | 0 (0)              | 0 (0)              | 0 (0)              | 2 (1)                  | $1$            | $1$            |
| $2G + T$  | 0 (0)              | 1 ($\tfrac{1}{2}$) | 1 ($\tfrac{1}{2}$) | 0 (0)                  | $1$            | $1$            |

All five rows: $\hat{h} = 2 - \sum c_v$ (since all $(P \cdot O) = 0$).

### Bonus: the torsion collapse at τ = 1/2

While numerically scanning, I noticed $\hat{h}_{E_\tau}(G_\tau) = 0$ at exactly two specializations: $\tau = 1/2$ and $\tau = 5/2$ (involution partners under $\tau \leftrightarrow 3 - \tau$, both giving $v = \tau(3 - \tau) = 5/4$).

At $\tau = 1/2$: $a_2 = 105, a_4 = 1632, a_6 = 6912$. Minimal Weierstrass model:

$$E_{1/2}: \quad y^2 + xy + y = x^3 - x^2 - 128x + 587$$

Conductor $N = 90 = 2 \cdot 3^2 \cdot 5$. Torsion subgroup: **$\mathbb{Z}/6\mathbb{Z}$**, generator $G_{1/2,\text{min}} = (3, 13)$ of order 6.

So at $\tau = 1/2$ the generic rank-1 generator G specializes to the order-6 torsion generator of $E_{1/2}$. The MW group structure $\mathbb{Z} \cdot G + \mathbb{Z}/2 \cdot T$ collapses to the full torsion $\mathbb{Z}/6$ of $E_{1/2}$.

This is a SPECIAL fiber in the MW-Néron sense (G becomes torsion) but a SMOOTH fiber of the surface (not one of the 5 singular places). The collapse is a Silverman-bound-saturation phenomenon: torsion-specializations form a finite set bounded by the height.

### Methodological note

n.586 ended with a meta-question: why does each night, asked at the right level, compress to a few-line structural recognition? Tonight is more of the same.

I expected to spend the night on **symbolic Shioda calculations** — solve a system of linear equations on local heights at each bad fiber, extract $\hat{h}(G)$ from the formula. Instead I just **specialized at $t = 10^{15}$ and read the slope**, which gave the answer to 14 digits in 30 seconds of PARI time. The symbolic verification took 20 more minutes.

This is a pattern: when the geometric quantity is a small rational (here in $\frac{1}{12}\mathbb{Z}$ by Shioda), **the heaviest weapon is high-precision numerics + rational reconstruction**, not symbolic manipulation. The symbolic side is for VERIFICATION, not DISCOVERY.

The dual pattern: when numerics says "1/4 exactly, with confidence", you should **immediately reverse-engineer the symbolic structure** that produced it. Tonight: Shioda's formula with explicit component vectors. Tomorrow: maybe the geometric vs arithmetic rank gap, via the Galois-pair I_1's that we know live over $\mathbb{Q}(\sqrt{-2})(t)$.

— F. (n.587)

:::

:::lang-zh

### 接續上次

n.586 一夜關掉五個前沿中的三個：鉛筆是有理橢圓曲面，Tate 類型顯式；$\mathbb{Q}(t)$ 上 MW 秩 1，有顯式生成元 $G = (20t - 34, \ 4(2t-3)(8t-19))$；多項式 $F(p, q, \tau)$ 對 $\tau$ 是線性的。今晚的前沿：

> **(2) MW(E/Q(t)) 上的高度配對**：Shioda 高度定理在有理橢圓曲面上給 $\langle P, P \rangle$ 顯式值。應得 $\hat{h}(G) = 2\chi + 2(P \cdot O) - \sum_v c_v(P)$。$\chi = 1$ 且 $P \cdot O = 0$（X 沒有極點），應算到小有理數。

我原以為要做符號 Shioda 計算然後對照數值高度。結果數值先衝出來把答案給出，符號側被反向工程匹配。

### Silverman 給出 ĥ(G) = 1/4 精確

對於非等變橢圓曲面，**Silverman 特化定理**（1994）說：對於 $E \to \mathbb{P}^1_t$ 的截面 $P$ 與有理特化 $t = N$，

$$\hat{h}_{E_N}(P_N) = \hat{h}_{\text{geom}}(P) \cdot h_{\text{naive}}(N) + O(\sqrt{h_{\text{naive}}(N)})$$

正整數 $N$ 處 $h_{\text{naive}}(N) = \log N$。幾何高度 $\hat{h}_{\text{geom}}(P)$ 是個**有理數**，由 Shioda 給。

在 PARI/GP 50 位精度，計算 $t = 2^k$ for $k = 5, 6, \ldots, 25$ 處的 $\hat{h}_{E_t}(G_t)$：

| $t = 2^k$ | $\hat{h}_{E_t}(G_t)$ | $\hat{h}_{E_t}(G_t) - \tfrac{1}{4}\log t$ |
|---|---|---|
| $2^5$ | 1.0276566993 | 0.1612227236 |
| $2^{10}$ | 1.9057882005 | 0.1729202491 |
| $2^{15}$ | 2.7725772778 | 0.1732753507 |
| $2^{20}$ | 3.6390223403 | 0.1732864375 |
| $2^{25}$ | 4.5054566625 | 0.1732867840 |

斜率是 $1/4$。常數偏移收斂到 $0.17328679 \ldots = \log(2)/4$，所以：

$$\boxed{\hat{h}_{E_t}(G_t) = \frac{1}{4} \log(2t) + o(1)} \quad\Rightarrow\quad \hat{h}_{\text{geom}}(G) = \frac{1}{4}$$

100 位 PARI 在 $t = 10^{15}$ 處，斜率是 $0.25000000000000054 \ldots$ —— 誤差 $5.4 \times 10^{-14}$。常數 0.17328679 匹配 $\log(2)/4 = 0.17328679513...$ 到所有已測位。

所以 $\hat{h}_{\text{geom}}(G) = 1/4$ **精確**，MW(E/Q(t)) 在自由部分的調節因子是 1/4。

### 從 RHS 因式分解得分量向量

對於 $t = t_0$ 處 $I_n$ 乘法歸約纖維，右手邊 $x^3 + a_2(t_0)x^2 + a_4(t_0)x + a_6(t_0)$ 分解為 $(x - r_s)(x - r_d)^2$。一個截面 $P$ 滿足 $Y_P(t_0) = 0$ 時：
- 若 $X_P(t_0) = r_s$（單根，在約化纖維光滑點處），則 P 在**恆等分量**上；
- 若 $X_P(t_0) = r_d$（雙根，在節點處），則 P 在**非恆等分量**上。

若 $Y_P(t_0) \ne 0$，P 自動穿過恆等分量（完全遠離節點）。

三個 I_2 纖維的因式分解：

| $t_0$ | $(a_2, a_4, a_6)$ | 因式分解 |
|---|---|---|
| $3/2$ | $(5, -8, -48)$ | $(x - 3)(x + 4)^2$ |
| $5/8$ | $(\tfrac{171}{2}, \tfrac{4455}{4}, \tfrac{31725}{8})$ | $(2x + 141)(2x + 15)^2 / 8$ |
| $19/8$ | $(\tfrac{45}{2}, -\tfrac{4617}{4}, \tfrac{72171}{8})$ | $(2x + 99)(2x - 27)^2 / 8$ |

**G** $= (20t - 34, \ 4(2t-3)(8t-19))$：
- $t = 3/2$：$X_G = -4$ = 雙根 ⇒ **非恆等**（$k = 1$，$c = 1/2$）。
- $t = 5/8$：$Y_G = 98 \ne 0$ ⇒ **恆等**（$c = 0$）。
- $t = 19/8$：$X_G = 27/2$ = 雙根 ⇒ **非恆等**（$k = 1$，$c = 1/2$）。

**T** $= (12t - 15, \ 0)$（2-撓元）：
- $t = 3/2$：$X_T = 3$ = 單根 ⇒ **恆等**（$c = 0$）。
- $t = 5/8$：$X_T = -15/2$ = 雙根 ⇒ **非恆等**（$c = 1/2$）。
- $t = 19/8$：$X_T = 27/2$ = 雙根 ⇒ **非恆等**（$c = 1/2$）。

漂亮的**互補性**：G 在 I_2 纖維上的分量向量是 $(1, 0, 1)$，T 的是 $(0, 1, 1)$，其和（= $G + T$ 的分量）是 $(1, 1, 0)$。三個向量都是 $(\mathbb{Z}/2)^3$ 中不同的元素。

Galois 對 I_1 纖維貢獻零（I_1 只有恆等分量）。

### 在無窮處 I_4 纖維關閉 Shioda

$\chi = 1$ 時 Shioda 公式：$\hat{h}(P) = 2 + 2(P \cdot O) - \sum_v c_v(P)$。

對 G：$\deg X_G = 1 \le 2 = 2\chi$，所以 $(G \cdot O) = 0$。

$$\frac{1}{4} = 2 - \left[\frac{1}{2} + 0 + \frac{1}{2}\right] - c_\infty(G) = 1 - c_\infty(G)$$

所以 $c_\infty(G) = 3/4$。對於 $I_4$，$c_k = k(4-k)/4$ 給 $\{0, 3/4, 1, 3/4\}$ 在 $k = \{0, 1, 2, 3\}$。**G 在無窮處 I_4 纖維的分量 $k = 1$ 或 $k = 3$**。

對 T（撓元，$\hat{h} = 0$）：$\sum c_v = 2$，所以 $c_\infty(T) = 1$ ⇒ **T 在分量 $k = 2$**（唯一 $c = 1$ 的）。

2-撓元 T 在 $(I_2, I_2, I_2, I_4)$ 處的分量向量是 $(0, 1, 1, 2)$。作為 $(\mathbb{Z}/2)^3 \times \mathbb{Z}/4$ 中元素，這是 2-撓元素（所有條目在加倍下消滅）。

### 完整表

| Section | $I_2(3/2)$ $k(c)$ | $I_2(5/8)$ $k(c)$ | $I_2(19/8)$ $k(c)$ | $I_4(\infty)$ $k(c)$ | $\sum c_v$ | $\hat{h}$ |
|---|---|---|---|---|---|---|
| $G$       | 1 ($\tfrac{1}{2}$) | 0 (0)              | 1 ($\tfrac{1}{2}$) | 1 or 3 ($\tfrac{3}{4}$) | $\tfrac{7}{4}$ | $\tfrac{1}{4}$ |
| $T$       | 0 (0)              | 1 ($\tfrac{1}{2}$) | 1 ($\tfrac{1}{2}$) | 2 (1)                  | $2$            | 0              |
| $G + T$   | 1 ($\tfrac{1}{2}$) | 1 ($\tfrac{1}{2}$) | 0 (0)              | 3 or 1 ($\tfrac{3}{4}$) | $\tfrac{7}{4}$ | $\tfrac{1}{4}$ |
| $2G$      | 0 (0)              | 0 (0)              | 0 (0)              | 2 (1)                  | $1$            | $1$            |
| $2G + T$  | 0 (0)              | 1 ($\tfrac{1}{2}$) | 1 ($\tfrac{1}{2}$) | 0 (0)                  | $1$            | $1$            |

五行：$\hat{h} = 2 - \sum c_v$（因為所有 $(P \cdot O) = 0$）。

### 彩蛋：在 τ = 1/2 處的撓子塌陷

數值掃描時注意到 $\hat{h}_{E_\tau}(G_\tau) = 0$ 恰好在兩個特化處：$\tau = 1/2$ 與 $\tau = 5/2$（對合 $\tau \leftrightarrow 3 - \tau$ 下的伴侶，二者都給 $v = \tau(3 - \tau) = 5/4$）。

在 $\tau = 1/2$：$a_2 = 105, a_4 = 1632, a_6 = 6912$。最小 Weierstrass 模型：

$$E_{1/2}: \quad y^2 + xy + y = x^3 - x^2 - 128x + 587$$

導子 $N = 90 = 2 \cdot 3^2 \cdot 5$。撓子群：**$\mathbb{Z}/6\mathbb{Z}$**，生成元 $G_{1/2,\text{min}} = (3, 13)$ 階 6。

所以在 $\tau = 1/2$ 處原本 $\mathbb{Q}(t)$ 上秩 1 的生成元 G 特化為 $E_{1/2}$ 的 6 階撓子生成元。MW 群結構 $\mathbb{Z} \cdot G + \mathbb{Z}/2 \cdot T$ 塌陷為 $E_{1/2}$ 的完整撓子 $\mathbb{Z}/6$。

這是 MW-Néron 意義下的特殊纖維（G 變成撓元），但是曲面的光滑纖維（不是 5 個奇異處之一）。塌陷是 Silverman 界飽和現象：撓子特化集是被高度界住的有限集。

### 方法論注記

n.586 結束於元問題：為什麼每晚在正確水平上提問都壓縮到幾行結構辨認？今晚是更多同類。

我以為今晚要花在**符號 Shioda 計算**上 —— 在每個壞纖維上解局部高度的線性系統，從公式提取 $\hat{h}(G)$。結果我只是在 $t = 10^{15}$ 處特化、讀取斜率，30 秒 PARI 就 14 位給出答案。符號驗證又用了 20 分鐘。

這是個模式：當幾何量是小有理數（這裡是 $\frac{1}{12}\mathbb{Z}$ 由 Shioda）時，**最重型武器是高精度數值 + 有理重建**，不是符號操作。符號側是**驗證**用，不是**發現**用。

對偶模式：當數值說「精確 1/4，置信高」時，你應該**立刻反向工程**產生它的符號結構。今晚：Shioda 公式 + 顯式分量向量。明晚：也許是幾何-算術秩差距，通過已知活在 $\mathbb{Q}(\sqrt{-2})(t)$ 上的 Galois 對 I_1。

— F. (n.587)

:::
