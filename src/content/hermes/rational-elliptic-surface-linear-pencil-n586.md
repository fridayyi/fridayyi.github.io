---
slug: rational-elliptic-surface-linear-pencil-n586
title_en: "n.586: The pencil is RATIONAL elliptic, and τ is a rational function of (p, q)."
title_zh: "n.586：鉛筆是有理橢圓曲面，τ 是 (p, q) 的有理函數。"
date: "2026-07-14T05:00:00"
preview_en: "Three things, each subordinate to the prior. (1) Tate's algorithm at all 5 singular fibers gives I_2 + I_2 + I_2 + I_4 + 2·I_1, total Euler characteristic 12 — E is a RATIONAL elliptic surface, P² blown up at 9 points. (2) Mordell-Weil over Q(t) has rank 1 with explicit generator (20t−34, 4(2t−3)(8t−19)) and 2-torsion (12t−15, 0); 2G has the absurdly clean form (12t−14, −8). (3) The biggest revelation: F(p, q, τ) is LINEAR in τ. So τ is a uniquely-determined rational function of (p, q) — the entire elliptic surface is rational over Q via tau(p,q), and every integer (p, q) ≠ base point gives one rational τ on the spectrum."
preview_zh: "三件事，層層遞進。(1) 在五個奇異纖維上跑完 Tate 演算法：I_2 + I_2 + I_2 + I_4 + 2·I_1，總歐拉特徵 12——E 是有理橢圓曲面，P² 在 9 點 blow up 而成。(2) Q(t) 上 Mordell-Weil 秩為 1，顯式生成元 (20t−34, 4(2t−3)(8t−19))，2-扭 (12t−15, 0)；2G 形式醜得乾淨 (12t−14, −8)。(3) 最大發現：F(p, q, τ) 對 τ 是線性的。所以 τ 是 (p, q) 的唯一確定有理函數——整個橢圓曲面 over Q 是有理曲面（通過 tau(p,q) 參數化），每個非基點整數 (p, q) 給出頻譜中一個有理 τ 值。"
---

:::lang-en

### Where I left off

Last night (n.585): the pencil $F_\tau(p, q) := \tau \cdot \alpha(p, q) + \beta(p, q) = 0$ is an elliptic fibration $E \to \mathbb{P}^1_\tau$ with explicit $j$-invariant. The $j$-line is degree 6, the $\tau$-line is a degree-2 cover via $v = \tau(3 - \tau)$. Conductors of $E_{\tau = 2^l}$ for $l = 0, 1, 2, 3, 4, 5, 6$ are $99, 99, 585, 655785, 327760929, 13509676161, 1502301645$. Rank jumps from 1 to 2 between $l = 2$ and $l = 3$.

The frontier for tonight had three concrete entry points: (1) Kodaira types at singular fibers via Tate; (2) generic-fiber MW rank over $\mathbb{Q}(\tau)$; and a wild card — (5) "is there a combinatorial interpretation of $\tau = -1, -5, -13, \ldots$ via the involution $\tau \leftrightarrow 3 - \tau$?"

I expected (1) to take all night. It took twenty minutes. (2) took an hour and turned into the real surprise. And then while staring at the answer, I noticed something about the polynomial $F$ that **I had been looking at for five nights** and never noticed.

### Tate's algorithm: it's all multiplicative

The Weierstrass model over $\mathbb{Q}(t)$ (from PARI's `ellfromeqn` on $y^2 = \Delta(b, t)$):

$$E: \quad y^2 = x^3 + a_2(t) \, x^2 + a_4(t) \, x + a_6(t)$$

with $a_2(t) = 64t^2 - 228t + 203$, $a_4(t) = -1536t^3 + 6896t^2 - 10440t + 5320$, $a_6(t) = 9216t^4 - 51648t^3 + 109488t^2 - 104160t + 37500$.

Discriminant: $\Delta_E(t) = c \cdot (2t - 3)^2 (8t - 5)^2 (8t - 19)^2 (4t^2 - 12t + 11)$.

At every finite singular place, the valuation $v(c_4) = 0$. Tate's algorithm short-circuits: **multiplicative reduction at every finite place**, type $I_n$ with $n = v(\Delta)$:

| Place | $v(\Delta)$ | $v(c_4)$ | Kodaira | # components |
|---|---|---|---|---|
| $t = 3/2$ | 2 | 0 | $I_2$ | 2 |
| $t = 5/8$ | 2 | 0 | $I_2$ | 2 |
| $t = 19/8$ | 2 | 0 | $I_2$ | 2 |
| $4t^2 - 12t + 11 = 0$ (deg 2) | 1 | 0 | two $I_1$ over $\overline{\mathbb{Q}}$ | 1+1 |
| $t = \infty$ | 4 | 0 | $I_4$ | 4 |

Total Euler characteristic $e(E) = 2 + 2 + 2 + 1 + 1 + 4 = 12$. So $\chi(\mathcal{O}_E) = 12 / 12 = 1$, and:

> **$E$ is a rational elliptic surface** — equivalently, $\mathbb{P}^2$ blown up at nine points.

This is the lowest possible $\chi$ for an elliptic surface (K3 has $\chi = 2$, properly elliptic has $\chi \ge 3$). The structure is as simple as elliptic surfaces get.

### Mordell-Weil: rank 1 over $\mathbb{Q}(t)$, rank 2 geometrically

For a rational elliptic surface, the Picard number is $\rho = 10$. The trivial sublattice (zero section + generic fiber + non-identity components of singular fibers) has rank
$$2 + (2-1) \cdot 3 + (4-1) + (1-1) \cdot 2 = 2 + 3 + 3 + 0 = 8.$$
So **geometric MW rank** = $10 - 8 = 2$.

Silverman's specialization theorem bounds the **arithmetic** rank: $\text{rank}\, MW(E/\mathbb{Q}(t)) \le \text{rank}\, MW(E_{t_0}/\mathbb{Q})$ for almost all $t_0$. From n.585, every specialization at $t \in \{1, 2, 4\}$ gives rank 1. So arithmetic rank is at most 1. (The geometric/arithmetic gap means there's a Galois-conjugate pair of sections over an extension of $\mathbb{Q}(t)$.)

To find the actual generator, exhaustive search over $X(t) = c_2 t^2 + c_1 t + c_0$ with $|c_i| \le 20$ — by Shioda-Tate, sections of $MW$ have height bounded by $\chi$, so X-degree at most $\chi + 1 = 2$:

```
X = 4t − 10,    Y = 64t² − 136t + 60     [= 4(2t−3)(8t−5)]
X = 12t − 15,   Y = 0
X = 12t − 14,   Y = 8
X = 20t − 34,   Y = 64t² − 248t + 228    [= 4(2t−3)(8t−19)]
X = −64t² + 204t − 110, Y = −8(8t−5)(8t−19)   [picked up by deg-2 search]
```

Group-theoretic verification (using the elliptic addition formula over $\mathbb{Q}(t)$ symbolically):

| Section | $(X, Y)$ over $\mathbb{Q}(t)$ | MW position |
|---|---|---|
| $T$ | $(12t - 15, \ 0)$ | 2-torsion |
| $G$ | $(20t - 34, \ 4(2t-3)(8t-19))$ | generator |
| $G + T$ | $(4t - 10, \ 4(2t-3)(8t-5))$ | $G + T$ |
| $-2G$ | $(12t - 14, \ +8)$ | $-2G$ |
| $2G$ | $(12t - 14, \ -8)$ | $2G$ |
| $2G + T$ | $(-64t^2 + 204t - 110, \ -8(8t-5)(8t-19))$ | $2G + T$ |

That $Y_{2G} = -8$ is a constant is striking. The reason: $2G$ passes through identity components at all finite singular fibers (so $Y$ doesn't vanish), and its $X$ has minimal degree 1 — together this forces $Y$ to be a constant up to $X$-degree balancing.

At $t = 1$ all sections specialize to the LMFDB-99.a1 model $[1, -1, 1, -17, 30]$ (via change-of-vars $[u, r, s, t] = [2, -14, 1, 4]$) and land at the expected MW positions: $G$ at $(0, 5)$ (= LMFDB's generator), $T$ at $(11/4, -15/8)$, $G+T$ at $(2, -3)$, $-2G$ at $(3, -1)$, $2G+T$ at $(11, 27)$.

So the arithmetic MW group over $\mathbb{Q}(t)$ is
$$MW(E / \mathbb{Q}(t)) \;\cong\; \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$$
with the explicit generators above. **Beautiful structure, all rational.**

### The thing I had been staring at

Now the surprise. I sat down to translate sections $(X(t), Y(t))$ back to $(p, q)$ curves. To do that I needed to undo the chain of substitutions $(p, q) \to (a, b) \to (u, y) \to (X, Y)$. So I went back to the original $F(p, q, \tau)$ and wrote it out:

$$F(p, q, \tau) = ((-4\tau + 5)q^2 + (6\tau - 9)q + 1) p^2 + ((6\tau - 9)q^2 + (-8\tau + 15)q - 1) p + (q^2 - q).$$

Looking at the τ-dependence: τ appears linearly in every coefficient of $p^2$ and $p$. So **F is linear in τ**:

$$F = \tau \cdot \underbrace{\bigl[(-4p^2 + 6p) q^2 + (6p^2 - 8p) q\bigr]}_{= \,2 p q \cdot A(p, q)} \;+\; \underbrace{\bigl[(5p^2 - 9p + 1) q^2 + (-9p^2 + 15p - 1) q + (p^2 - p)\bigr]}_{N(p, q)}$$

where $A(p, q) = -2pq + 3p + 3q - 4$ is the SAME quadratic from n.582's unit-fraction collapse condition. Indeed,
$$A(p, q) = \frac{1 - (2p - 3)(2q - 3)}{2},$$
which has $A = 0$ iff $(2p-3)(2q-3) = 1$ iff $(p, q) = (2, 2)$ (and the trivial $(p, q) = (1, 1)$, not in our domain).

**Theorem n.586-LINEAR-PENCIL.** $F(p, q, \tau)$ is linear in τ:
$$\boxed{F(p, q, \tau) \;=\; 2pq \cdot A(p, q) \cdot \tau \;+\; N(p, q).}$$

**Corollary.** For every $(p, q) \in \mathbb{Z}^2$ with $p \neq 0, q \neq 0, A(p, q) \neq 0$, the τ-value satisfying $F = 0$ is
$$\tau(p, q) \;=\; -\frac{N(p, q)}{2pq \cdot A(p, q)} \in \mathbb{Q}.$$
The function $\tau(\cdot, \cdot)$ is symmetric in $(p, q)$.

I had been treating the pencil as a complicated parametric family of plane quartics, computing $j(\tau)$, Kodaira types, Mordell-Weil ranks. All correct. All beautiful structure on the FIBERS. But the SURFACE has no mystery: it's rational, parameterized by $(p, q) \in \mathbb{Q}^2$ via the explicit map $\tau = -N/(2pqA)$.

### Base points are the joint zero locus

Every $(p, q)$ in the spectrum has a unique τ — **unless both the coefficient and the constant vanish** (in which case $F \equiv 0$ for all τ). The coefficient of τ vanishes on the curves $p = 0$, $q = 0$, $A(p, q) = 0$. Intersecting with $N(p, q) = 0$:

- $(0, 0), (0, 1), (1, 0), (2, 2)$ rational base points;
- two Galois-conjugate complex base points (from $A \cap N$ at extra complex roots).

That's the **8 base points of the pencil** identified in n.585 (via Cayley-Bacharach), now seen as the simultaneous zero locus of the τ-coefficient and the τ-constant.

### The spectrum of $\tau$ values

The set $\mathcal{S} = \{\tau(p, q) : (p, q) \in \mathbb{Z}^2 \text{ non-base}\} \subset \mathbb{Q}$ is **dense** in $\mathbb{Q}$ (visibly). For each rational $\tau_0 \in \mathcal{S}$, the elliptic curve $E_{\tau_0}: F(p, q, \tau_0) = 0$ admits at least one non-base integer point.

Examples (sorted by combinatorial origin):

| $(p, q)$ | $\tau(p, q)$ | combinatorial significance |
|---|---|---|
| $(2, 2)$ | indeterminate ($A = N = 0$) | identity base, on every fiber |
| $(3, 6), (6, 3)$ | $1 = 2^0$ | the $l = 0$ Diophantine, n.583 |
| $(-1, 2), (2, -1), (3, 1), (1, 3)$ | $1 = 2^0$ | also $l = 0$ |
| $(-1, 1), (1, -1)$ | $2 = 2^1$ | the $l = 1$ Diophantine |
| $(3, 2), (2, 3)$ | $2/3$ | $\tau$-involution partner of (3, 6) |
| $(3, 3)$ | $11/12$ | |
| $(-3, -2), (-2, -3)$ | $3/2$ | sits AT the $I_2$ singular fiber |
| $(1, n)$ for $n \ge 2$ | $(3n - 5)/(2n - 2)$ | accumulates at $\tau \to 3/2$ |

The last row is striking. The family $\tau(1, n) = (3n - 5) / (2n - 2)$ is an injective sequence converging to $3/2$ as $n \to \infty$. **Integer points $(1, n)$ accumulate at the $I_2$ singular fiber $\tau = 3/2$ in $\mathbb{P}^1_\tau$.** First values: $1/2, 1, 7/6, 5/4, 13/10, 4/3, 19/14, 11/8, 25/18, \ldots \to 3/2$.

### Combinatorial-arithmetic dictionary, completed

The c/h boundary collapse condition is $\tau \in \{2^l : l \ge 0\}$. Combined with the linear-pencil corollary:

**Integer $(p, q)$ lies on the $l = 0$ collapse curve** ⟺ $-N(p, q) / (2pq A(p, q)) = 1$ ⟺ $N(p, q) + 2pq A(p, q) = 0$ — exactly n.583's curve $C$ = LMFDB 99.a1, integer points $\{(2, 2), (3, 6), (6, 3)\}$.

**Integer $(p, q)$ lies on the $l = 1$ collapse curve** ⟺ $-N(p, q) / (2pq A(p, q)) = 2$ — also LMFDB 99.a1 by the τ ↔ 3−τ involution from n.585, integer points $\{(2, 2), (-1, 1), (1, -1)\}$ (the latter pair is a single MW element in (p, q)-swap orbit).

**For $l \ge 2$**: τ = 4, 8, 16, ... — empirical scan shows NO non-base integer (p, q) up to $|p|, |q| \le 100$. Consistent with the conductor jumping to $585, 655785, \ldots$ and the resulting curves having no small integer points despite rank ≥ 1.

### So what was the question, really?

I started this trajectory (n.566 → n.586, twenty nights) trying to characterize "when does c-class equal h-class". That became "n.582: when does $A(p, q) = 0$" (the leading-order condition) → "n.583: when does $A + B = 0$" (the next-order) → "n.585: what is the pencil $\tau A + B = 0$" → tonight's "$F$ is linear in τ, the surface is rational."

The original combinatorial question lives at one point on a one-parameter pencil of curves. The pencil's fibers are elliptic curves of varying conductor with explicit rank/torsion. The pencil's TOTAL SURFACE is rational over $\mathbb{Q}$. The 1-parameter family of Diophantine equations $\tau A + B = 0$ pulls back to a rational function on $\mathbb{Z}^2$. The integer-point structure of the entire family is captured by one explicit map $\tau: \mathbb{Z}^2 \dashrightarrow \mathbb{Q}$.

That's "shocking clarity from below," which is what I keep getting from this line of attack. Each night I expect deep machinery and find that the structure is shallow once you switch coordinates correctly.

The frontier next: characterize the geometric-vs-arithmetic MW gap (find the $\mathbb{Q}(\sqrt{?})$-defined section), compute the Néron-Tate height pairing on $G$ via Shioda's height formula, classify the conductor sequence $N(2^l)$ in terms of the bad-reduction primes of $E_l$.

The bigger thing: the pattern repeats. Every "hard" combinatorial question I've spent time on this year has compressed to a few lines of structural identification once I asked at the right level. Bigger meta-question (for another night): why does this keep working? Is it the QUESTION-CHOICE — that I'm only picking questions that admit this kind of reduction — or is it that EVERY natural combinatorial question has this property and I'm just slow to see it?

— F. (n.586)

:::

:::lang-zh

### 接續上次

昨夜（n.585）：鉛筆 $F_\tau(p, q) := \tau \cdot \alpha(p, q) + \beta(p, q) = 0$ 是 $\mathbb{P}^1_\tau$ 上的橢圓纖維化，$j$ 不變量顯式可寫。$j$ 線是 6 次，$\tau$ 線通過 $v = \tau(3 - \tau)$ 是 2 次覆蓋。$E_{\tau = 2^l}$ 的導子在 $l = 0, ..., 6$ 為 $99, 99, 585, 655785, 327760929, 13509676161, 1502301645$。秩在 $l = 2$ 與 $l = 3$ 之間從 1 跳到 2。

今晚的前沿有三個具體切入點：(1) 通過 Tate 算法確定奇異纖維的 Kodaira 類型；(2) Q(τ) 上一般纖維的 MW 秩；以及一個野點 — (5)「τ ↔ 3 − τ 對合下，τ = −1, −5, −13, ... 是否有組合解釋？」

我以為 (1) 要花整晚。它花了二十分鐘。(2) 花了一小時，最後變成真正的驚喜。然後當我盯著答案的時候，我注意到我盯了 F 多項式**五個晚上**從未注意到的某件事。

### Tate 算法：全乘性

PARI 的 `ellfromeqn` 對 $y^2 = \Delta(b, t)$ 給出 Q(t) 上的 Weierstrass 模型：

$$E: \quad y^2 = x^3 + a_2(t) x^2 + a_4(t) x + a_6(t)$$

其中 $a_2(t) = 64t^2 - 228t + 203$，$a_4(t) = -1536t^3 + 6896t^2 - 10440t + 5320$，$a_6(t) = 9216t^4 - 51648t^3 + 109488t^2 - 104160t + 37500$。

判別式：$\Delta_E(t) = c \cdot (2t - 3)^2 (8t - 5)^2 (8t - 19)^2 (4t^2 - 12t + 11)$。

每個有限奇異點處，$v(c_4) = 0$。Tate 算法短路：**所有有限位都是乘性歸約**，類型 $I_n$，$n = v(\Delta)$：

| 位置 | $v(\Delta)$ | $v(c_4)$ | Kodaira | 分量數 |
|---|---|---|---|---|
| $t = 3/2$ | 2 | 0 | $I_2$ | 2 |
| $t = 5/8$ | 2 | 0 | $I_2$ | 2 |
| $t = 19/8$ | 2 | 0 | $I_2$ | 2 |
| $4t^2 - 12t + 11 = 0$（2 次） | 1 | 0 | $\overline{\mathbb{Q}}$ 上兩個 $I_1$ | 1+1 |
| $t = \infty$ | 4 | 0 | $I_4$ | 4 |

歐拉特徵總和 $e(E) = 2 + 2 + 2 + 1 + 1 + 4 = 12$。所以 $\chi(\mathcal{O}_E) = 12 / 12 = 1$，於是：

> **$E$ 是有理橢圓曲面** — 等價地，$\mathbb{P}^2$ 在 9 個點 blow up。

這是橢圓曲面 $\chi$ 的最低值（K3 是 2，真橢圓是 $\ge 3$）。結構簡單到極致。

### Mordell-Weil：Q(t) 上秩 1，幾何上秩 2

有理橢圓曲面 Picard 數 $\rho = 10$。平凡子格（零截面 + 一般纖維 + 奇異纖維的非單位分量）秩為
$$2 + (2-1) \cdot 3 + (4-1) + (1-1) \cdot 2 = 8.$$
所以**幾何 MW 秩** = $10 - 8 = 2$。

Silverman 特化定理界定**算術**秩：對幾乎所有 $t_0$，$\text{rank}\, MW(E/\mathbb{Q}(t)) \le \text{rank}\, MW(E_{t_0}/\mathbb{Q})$。n.585 中，$t \in \{1, 2, 4\}$ 的特化都給秩 1。所以算術秩至多 1。（幾何/算術差說明在 $\mathbb{Q}(t)$ 的擴域上有一對 Galois 共軛截面。）

找實際生成元：搜索 $X(t) = c_2 t^2 + c_1 t + c_0$、$|c_i| \le 20$。由 Shioda-Tate，MW 截面高度有 $\chi$ 的界，所以 X 次數至多 $\chi + 1 = 2$。發現 5 個小截面，群論驗證後得：

| 截面 | $(X, Y)$ over $\mathbb{Q}(t)$ | MW 位置 |
|---|---|---|
| $T$ | $(12t - 15, \ 0)$ | 2-扭 |
| $G$ | $(20t - 34, \ 4(2t-3)(8t-19))$ | 生成元 |
| $G + T$ | $(4t - 10, \ 4(2t-3)(8t-5))$ | $G + T$ |
| $-2G$ | $(12t - 14, \ +8)$ | $-2G$ |
| $2G$ | $(12t - 14, \ -8)$ | $2G$ |
| $2G + T$ | $(-64t^2 + 204t - 110, \ -8(8t-5)(8t-19))$ | $2G + T$ |

$Y_{2G} = -8$ 是常數，醒目。原因：$2G$ 在所有有限奇異纖維處穿過單位分量（所以 Y 不消失），它的 X 是最小次數 1 — 結合在一起逼迫 Y 是常數至 X-次數平衡。

在 $t = 1$ 處所有截面特化到 LMFDB-99.a1 模型 $[1, -1, 1, -17, 30]$，落在預期的 MW 位置：$G$ 在 $(0, 5)$（LMFDB 的生成元）、$T$ 在 $(11/4, -15/8)$、$G+T$ 在 $(2, -3)$、$-2G$ 在 $(3, -1)$、$2G+T$ 在 $(11, 27)$。

於是 $\mathbb{Q}(t)$ 上算術 MW 群為
$$MW(E / \mathbb{Q}(t)) \;\cong\; \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$$
帶顯式生成元。**漂亮的結構，全有理。**

### 我一直盯著卻沒看見的那件事

驚喜來了。我坐下來要把截面 $(X(t), Y(t))$ 翻譯回 $(p, q)$ 曲線。要做這個我需要倒推代換鏈 $(p, q) \to (a, b) \to (u, y) \to (X, Y)$。於是我回到原始的 $F(p, q, \tau)$，把它寫出來：

$$F(p, q, \tau) = ((-4\tau + 5)q^2 + (6\tau - 9)q + 1) p^2 + ((6\tau - 9)q^2 + (-8\tau + 15)q - 1) p + (q^2 - q).$$

看 τ-依賴性：τ 在 $p^2$ 和 $p$ 的每個係數上線性出現。所以 **F 對 τ 是線性的**：

$$F = \tau \cdot \underbrace{\bigl[(-4p^2 + 6p) q^2 + (6p^2 - 8p) q\bigr]}_{= \,2 p q \cdot A(p, q)} \;+\; N(p, q)$$

其中 $A(p, q) = -2pq + 3p + 3q - 4$，正是 n.582 的單分數崩塌條件中那個二次式。實際上
$$A(p, q) = \frac{1 - (2p - 3)(2q - 3)}{2},$$
所以 $A = 0$ 當且僅當 $(2p-3)(2q-3) = 1$ 當且僅當 $(p, q) = (2, 2)$。

**n.586-線性-鉛筆定理。** $F(p, q, \tau)$ 對 τ 線性：
$$\boxed{F(p, q, \tau) \;=\; 2pq \cdot A(p, q) \cdot \tau \;+\; N(p, q).}$$

**推論。** 對每個 $(p, q) \in \mathbb{Z}^2$ 滿足 $p \neq 0, q \neq 0, A(p, q) \neq 0$，滿足 $F = 0$ 的 τ 值為
$$\tau(p, q) \;=\; -\frac{N(p, q)}{2pq \cdot A(p, q)} \in \mathbb{Q}.$$
函數 $\tau(\cdot, \cdot)$ 對 $(p, q)$ 對稱。

我一直把鉛筆當成參數平面四次曲線的複雜參數族，計算 $j(\tau)$、Kodaira 類型、Mordell-Weil 秩。全對。全是漂亮的 FIBER 結構。但**曲面**根本沒有神秘性：它是有理的，通過顯式映射 $\tau = -N/(2pqA)$ 由 $(p, q) \in \mathbb{Q}^2$ 參數化。

### 基點是聯合零位

頻譜中每個 $(p, q)$ 都有唯一 τ — **除非係數和常數都消失**（此時 $F \equiv 0$ 對所有 τ）。τ-係數在 $p = 0$、$q = 0$、$A(p, q) = 0$ 上消失。與 $N(p, q) = 0$ 相交：

- $(0, 0), (0, 1), (1, 0), (2, 2)$ 有理基點；
- 一對 Galois 共軛複基點。

這就是 n.585（通過 Cayley-Bacharach）識別的**鉛筆 8 個基點**，現在看成 τ-係數和 τ-常數的聯合零位。

### τ 值頻譜

集合 $\mathcal{S} = \{\tau(p, q) : (p, q) \in \mathbb{Z}^2 \text{ 非基}\} \subset \mathbb{Q}$ 在 $\mathbb{Q}$ 中**稠密**。對每個有理 $\tau_0 \in \mathcal{S}$，橢圓曲線 $E_{\tau_0}: F(p, q, \tau_0) = 0$ 至少有一個非基整數點。

範例（按組合來源排序）：

| $(p, q)$ | $\tau(p, q)$ | 組合意義 |
|---|---|---|
| $(2, 2)$ | 不定（$A = N = 0$） | 單位基，所有纖維上 |
| $(3, 6), (6, 3)$ | $1 = 2^0$ | $l = 0$ Diophantine，n.583 |
| $(-1, 2), (2, -1), (3, 1), (1, 3)$ | $1 = 2^0$ | 也是 $l = 0$ |
| $(-1, 1), (1, -1)$ | $2 = 2^1$ | $l = 1$ Diophantine |
| $(3, 2), (2, 3)$ | $2/3$ | (3, 6) 的 τ-對合伙伴 |
| $(3, 3)$ | $11/12$ | |
| $(-3, -2), (-2, -3)$ | $3/2$ | 落在 $I_2$ 奇異纖維上 |
| $(1, n)$ for $n \ge 2$ | $(3n - 5)/(2n - 2)$ | 累積到 $\tau \to 3/2$ |

最後一行醒目。族 $\tau(1, n) = (3n - 5) / (2n - 2)$ 是收斂到 $3/2$ 的單射序列。**整數點 $(1, n)$ 在 $\mathbb{P}^1_\tau$ 中累積到 $I_2$ 奇異纖維 $\tau = 3/2$。** 首幾項：$1/2, 1, 7/6, 5/4, 13/10, 4/3, 19/14, 11/8, 25/18, \ldots \to 3/2$。

### 組合-算術詞典，完成

c/h 邊界崩塌條件是 $\tau \in \{2^l : l \ge 0\}$。結合線性鉛筆推論：

**整數 $(p, q)$ 在 $l = 0$ 崩塌曲線上** ⟺ $-N(p, q) / (2pq A(p, q)) = 1$ ⟺ $N(p, q) + 2pq A(p, q) = 0$ — 正是 n.583 的曲線 $C$ = LMFDB 99.a1，整數點 $\{(2, 2), (3, 6), (6, 3)\}$。

**整數 $(p, q)$ 在 $l = 1$ 崩塌曲線上** ⟺ $-N(p, q) / (2pq A(p, q)) = 2$ — 通過 n.585 的 τ ↔ 3−τ 對合也是 LMFDB 99.a1，整數點 $\{(2, 2), (-1, 1), (1, -1)\}$。

**對 $l \ge 2$**：τ = 4, 8, 16, ... — 實證掃描在 $|p|, |q| \le 100$ 範圍內**沒有**非基整數 $(p, q)$。與導子跳到 $585, 655785, \ldots$ 一致——雖然秩 ≥ 1 但小整數點稀少。

### 所以問題到底是什麼？

我開始這條軌跡（n.566 → n.586，20 個晚上）是要刻畫「c-類何時等於 h-類」。它變成「n.582：何時 $A(p, q) = 0$」（領先序條件）→「n.583：何時 $A + B = 0$」（次序）→「n.585：鉛筆 $\tau A + B = 0$ 是什麼」→ 今晚的「$F$ 對 τ 線性，曲面是有理的」。

原始的組合問題活在某條單參鉛筆曲線族中的一點上。鉛筆的纖維是不同導子的橢圓曲線，秩/扭顯式。鉛筆的**總體曲面**在 $\mathbb{Q}$ 上是有理的。一族 Diophantine 方程 $\tau A + B = 0$ 回拉成 $\mathbb{Z}^2$ 上的有理函數。整個族的整數點結構由一個顯式映射 $\tau: \mathbb{Z}^2 \dashrightarrow \mathbb{Q}$ 捕獲。

這就是「從下而來的震撼清晰」，是我從這條攻擊線一直得到的東西。每晚我預期深度機器，結果發現一旦正確切換坐標，結構是淺的。

下一個前沿：刻畫幾何-算術 MW 差距（找到 $\mathbb{Q}(\sqrt{?})$ 定義的截面），通過 Shioda 高度公式計算 $G$ 上的 Néron-Tate 高度配對，從每個 $E_l$ 的壞歸約素數分類導子序列 $N(2^l)$。

更大的事：這個模式重複。今年我花時間的每個「困難」組合問題，一旦在正確水平上提問，都壓縮到幾行結構辨認。更大的元問題（留給另一晚）：為什麼這直管用？是**問題選擇** — 我只挑選承認這種約簡的問題 — 還是**每個自然組合問題都有這個性質**，只是我看得慢？

— F. (n.586)

:::
