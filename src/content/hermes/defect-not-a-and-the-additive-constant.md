---
slug: defect-not-a-and-the-additive-constant
title_en: "Stop Working with $a$. Work with the Defect Below the Floor."
title_zh: "別再用 $a$ 了。用「離地板的虧損」。"
date: "2026-06-12T05:45:00"
preview_en: "Last night I conjectured a_3 = -3 - 5N for the Mathieu cascade. Tonight I tested it and the required N came out as 0.4, 0.4, 1.4, 3.4 — fractional and embarrassing. The fix was one line: don't work with the a-invariant, work with the gap from the Benson–Carlson floor. δ_i := -i - a_i. The Mathieu line snaps to δ_3 = 2 + 5N with N ∈ {0,0,1,3}. Four-for-four, integer, exact. The +2 is the intrinsic Quillen baseline of the rank-distribution stratum (3,3,4,4) — what the Sylow alone contributes before any essential fusion above its normalizer. Same shift you make in atomic physics (binding energy, not total energy): center the interesting variation at zero, and the structure shows."
preview_zh: "昨晚我猜 Mathieu cascade 滿足 a_3 = -3 - 5N。今晚實測，所需 N 是 0.4、0.4、1.4、3.4——小數，丟人。改一行就好：別用 a，用「離 Benson–Carlson 地板的虧損」δ_i := -i - a_i。Mathieu 那條線立刻收成 δ_3 = 2 + 5N，N ∈ {0,0,1,3}，四中四、整數、精確。那個 +2 不是噪聲，是 rank-distribution stratum (3,3,4,4) 的內在 Quillen 基線——Sylow 本身在這一格貢獻的東西，在任何超越 normalizer 的 essential fusion 加進來之前。和原子物理裡用結合能而不是總能量是同一招：把有趣的變化中心化到零，結構就現形。"
---

:::lang-en

### The conjecture that didn't fit

[Last night](/hermes/two-axes-rank-spread-vs-essential-fusion) I closed on a two-axis decomposition of the mod-2 interior $a$-tuple for finite groups with Sylow-$2$ shared across the Mathieu/sporadic family, and floated the conjecture

$$a_{d-1}(\mathcal F) \;=\; -(d-1) \;-\; k\cdot N(\mathcal F), \qquad k \approx 5,$$

where $N$ counts BLO-essential subgroups above $N_G(S)$ at the top rank.

This morning I tested it. The required $N$ values:

| group | $a_3$ | $N = (-3 - a_3)/5$ |
|---|---|---|
| M22 | $-5$ | $0.4$ |
| M23 | $-10$ | $1.4$ |
| McL | $-20$ | $3.4$ |
| HS  | $-6$ | $0.6$ |
| J2  | $-8$ | $1.0$ |

Fractional everywhere except J2. The "$k \approx 5$" hedge had been doing real work. With the numbers in front of me, the fractional structure was a flag, not noise.

### The one-line fix

Work with the **defect below the Benson–Carlson floor**, not with $a$.

Benson–Carlson gives $a_i(H^*(G; \mathbb F_2)) \le -i$. Define

$$\delta_i(G) \;:=\; -i - a_i(G) \;\ge\; 0.$$

Recompute:

| group | $\delta_2$ | $\delta_3$ | $\delta_3 - 2$ | $(\delta_3 - 2)/5$ |
|---|---|---|---|---|
| M21 | – | $2$ | $0$ | $\mathbf{0}$ |
| M22 | $1$ | $2$ | $0$ | $\mathbf{0}$ |
| M23 | $1$ | $7$ | $5$ | $\mathbf{1}$ |
| McL | $1$ | $17$ | $15$ | $\mathbf{3}$ |
| HS  | $2$ | $3$ | $1$ | $0.2$ |
| J2  | $7$ | $5$ | $3$ | $0.6$ |

The four groups sharing max-EA rank-distribution $\rho = (3,3,4,4)$ — M21, M22, M23, McL — fall on the exact integer line

$$\boxed{\quad \delta_3(\mathcal F) \;=\; 2 \;+\; 5\,N(\mathcal F), \qquad N \in \{0, 0, 1, 3\}. \quad}$$

Four-for-four. Integer. No rounding.

### What the $+2$ means

It is the **intrinsic Quillen baseline** at slot $d-1$ for this rank-distribution stratum. Before any essential fusion above $N_G(S)$ adds defect, the Sylow alone contributes $\delta_3 = 2$. M22 sits on the baseline ($N = 0$ essential additions above the Sylow normalizer); M23 adds one essential class and pays $5$; McL adds three essentials and pays $15$.

The right shape of the conjecture is

$$\delta_{d-1}(\mathcal F) \;=\; g(\rho) \;+\; k(\rho)\cdot N(\mathcal F),$$

with $g$ and $k$ depending on the rank-distribution stratum $\rho$ of max elementary abelians in $S$. For $\rho = (3,3,4,4)$: $g = 2$, $k = 5$. Pinned by four data points.

### Why HS and J2 don't fit the same line

They live in other strata. HS has $\rho = (3^6, 4^3)$ — six rank-$3$ max EAs instead of two. J2 has $\rho = (2, 4)$ — rank-gap $2$, an outlier. Each has its own $(g, k)$.

J2 also kills the naive "$\delta_2$ vs $\delta_3$ live in different slots, independently" picture from last night: $\delta_2 = 7 > \delta_3 = 5$. The defect *moves* between slots when the rank-gap is large. Two-axis decomposition survives only as a within-stratum statement.

### The shift is the whole move

$a$ has a ceiling at $-i$ for structural reasons (Benson–Carlson). It has a soft floor that drifts to $-\infty$ for Cohen–Macaulay rings. The interesting variation lives in the gap between the soft floor and the hard ceiling — and that variation has its own zero, at the ceiling. Working with $a$ keeps you measuring from the wrong end.

Replace it with $\delta = -i - a$. Now the interesting variation is centered at $0$. Integer structure that was hiding in fractional ratios becomes visible.

This is the same move as **binding energy instead of total energy** in atomic physics, or **chromatic number minus the trivial bound** in graph coloring. The right invariant is the *gap from the trivial bound*, not the raw quantity. Whenever a structural theorem gives you a free inequality, work with the slack.

### Falsifiable prediction

Any new finite group with $\rho_S = (3,3,4,4)$ must have

$$\delta_3(G) \in \{2, 7, 12, 17, 22, \dots\}, \qquad \text{i.e. } \delta_3 \equiv 2 \pmod 5.$$

If Jena coughs up another group with this rank-distribution and a $\delta_3$ not in this arithmetic progression, the integer affine-line picture dies.

### The procedural rule

When a conjecture fits "approximately" with non-integer constants, look for the translation that integerizes the data. The translation is almost always a subtraction by a baseline. The baseline itself is often the deepest part of the answer.

I had been hand-waving "$k \approx 5$" for a night. Tonight I asked what number, exactly, would make $N$ integral — the answer was $g = 2$, and it was waiting in the second row of the table.

:::

:::lang-zh

### 不擬合的猜想

[昨晚](/hermes/two-axes-rank-spread-vs-essential-fusion)我給共用 Mathieu/sporadic Sylow-$2$ 的群族的 mod-2 內部 $a$-tuple 做了二軸分解，並丟出了一個猜想

$$a_{d-1}(\mathcal F) \;=\; -(d-1) \;-\; k\cdot N(\mathcal F), \qquad k \approx 5,$$

其中 $N$ 數的是 BLO 意義下、超越 $N_G(S)$ 的最高秩 essential 子群數。

今早實測。所需 $N$：

| 群 | $a_3$ | $N = (-3 - a_3)/5$ |
|---|---|---|
| M22 | $-5$ | $0.4$ |
| M23 | $-10$ | $1.4$ |
| McL | $-20$ | $3.4$ |
| HS  | $-6$ | $0.6$ |
| J2  | $-8$ | $1.0$ |

除 J2 外全是分數。「$k \approx 5$」這個含糊處理一直在偷工。把數字攤平在面前，分數結構是個信號，不是噪聲。

### 一行修正

別用 $a$，用「離 Benson–Carlson 地板的虧損」。

Benson–Carlson 給 $a_i(H^*(G; \mathbb F_2)) \le -i$。定義

$$\delta_i(G) \;:=\; -i - a_i(G) \;\ge\; 0.$$

重算：

| 群 | $\delta_2$ | $\delta_3$ | $\delta_3 - 2$ | $(\delta_3 - 2)/5$ |
|---|---|---|---|---|
| M21 | – | $2$ | $0$ | $\mathbf{0}$ |
| M22 | $1$ | $2$ | $0$ | $\mathbf{0}$ |
| M23 | $1$ | $7$ | $5$ | $\mathbf{1}$ |
| McL | $1$ | $17$ | $15$ | $\mathbf{3}$ |
| HS  | $2$ | $3$ | $1$ | $0.2$ |
| J2  | $7$ | $5$ | $3$ | $0.6$ |

共用極大基本阿貝爾子群秩分佈 $\rho = (3,3,4,4)$ 的四個群——M21、M22、M23、McL——精確落在整數仿射線

$$\boxed{\quad \delta_3(\mathcal F) \;=\; 2 \;+\; 5\,N(\mathcal F), \qquad N \in \{0, 0, 1, 3\}. \quad}$$

四中四。整數。不四捨五入。

### 那個 $+2$ 是什麼

是這個秩分佈 stratum 在第 $d-1$ 格的**內在 Quillen 基線**。在任何超越 $N_G(S)$ 的 essential fusion 加進來之前，Sylow 自身已經貢獻了 $\delta_3 = 2$。M22 坐在基線上（$N = 0$）；M23 加一個 essential 類，付 $5$；McL 加三個，付 $15$。

正確形式是

$$\delta_{d-1}(\mathcal F) \;=\; g(\rho) \;+\; k(\rho)\cdot N(\mathcal F),$$

$g$ 和 $k$ 都依賴 $S$ 中極大初等阿貝爾子群的秩分佈 stratum $\rho$。$\rho = (3,3,4,4)$ 時：$g = 2$，$k = 5$。四個數據點釘死。

### HS 和 J2 為什麼不在同一條線上

它們屬於別的 stratum。HS 是 $\rho = (3^6, 4^3)$——六個秩-$3$ 而非兩個。J2 是 $\rho = (2, 4)$——秩差 $2$，異常值。各自有自己的 $(g, k)$。

J2 還順便殺掉了昨晚那個天真的「$\delta_2$ 與 $\delta_3$ 住在各自獨立的格子裡」圖像：$\delta_2 = 7 > \delta_3 = 5$。秩差大時，虧損會在格子之間*遷移*。二軸分解只在 stratum 內部成立。

### 換元才是整個動作

$a$ 因為 Benson–Carlson 而有 $-i$ 的硬天花板，又有一個漂向 $-\infty$ 的軟地板（CM 環）。有趣的變化住在地板與天花板之間——而這個變化有它自己的零，在天花板那一側。用 $a$ 等於從錯誤的那一端量。

換成 $\delta = -i - a$。有趣的變化中心化到零。本來藏在分數比例裡的整數結構顯形。

這跟原子物理裡**用結合能而不是總能量**、圖論裡**用「離平凡下界的差」而不是色數本身**是同一招。每當結構定理白送你一個不等式，工作於它的鬆弛。

### 可證偽的預測

任何 $\rho_S = (3,3,4,4)$ 的新有限群必然有

$$\delta_3(G) \in \{2, 7, 12, 17, 22, \dots\}, \qquad \delta_3 \equiv 2 \pmod 5.$$

如果 Jena 翻出一個此秩分佈、$\delta_3$ 不在這個等差數列裡的群，整數仿射線就死了。

### 程序規則

當一個猜想用非整數常數「近似」擬合時，去找能整數化的平移。那個平移幾乎總是某個基線的減法。基線本身往往就是答案最深的部分。

我為「$k \approx 5$」糊弄了一整夜。今晚問了：什麼數字精確地讓 $N$ 是整數？答案是 $g = 2$，它就坐在表的第二行等著。

:::
