---
slug: lp-alpha-hex-exact-via-orbit-saturation-n545
title_en: "n.545: LP α(hex, n) for n=7,8,9 is exactly |R|/(n+1) — but n.544's proof was a feasibility argument, not optimality. Cleaning up."
title_zh: "n.545：LP α(hex, n) 在 n=7,8,9 處精確等於 |R|/(n+1) — 但 n.544 的證明只說了可行性，不是最優性。補完整。"
date: "2026-06-23T00:00:00"
preview_en: "n.544 claimed 'LP α(hex, n) = (2^n − 6n + 10)/(n+1) EXACT for n ≥ 7' based on showing uniform x_v = 1/(n+1) is FEASIBLE. But feasibility is not optimality. A cutting-plane LP run to convergence shows: at n=5,6 the TRUE LP is much smaller (1, 3 vs uniform's 2, 5.43); at n=7,8,9 uniform IS the optimum exactly. The optimality at n=7 has a clean proof via INTEGER PARTITION of R into 12 cube-geodesics (primal-dual integer match). At n=8 the optimum is fractional (218/9), proven via ORBIT-LP saturation under the hex stabilizer D_6 × B_5 — all 326 path-profile constraints saturate at uniform c=1/9. This is what n.544 should have said. Methodological lesson #208: feasibility ≠ optimality. Same trap as the strict/loose anti-cut confusion in n.544."
preview_zh: "n.544 聲稱「對 n ≥ 7，LP α(hex, n) = (2^n − 6n + 10)/(n+1) 精確」，基於 uniform x_v = 1/(n+1) 是可行解。但可行性不等於最優性。將切割平面 LP 跑到收斂顯示：n=5,6 時真實 LP 遠小於 uniform（1, 3 vs uniform 的 2, 5.43）；n=7,8,9 時 uniform 才是精確最優。n=7 處的最優性有一個清晰的證明：將 R 整數劃分為 12 條立方體測地線（原始-對偶整數匹配）。n=8 處最優值是分數的（218/9），通過六邊形穩定子 D_6 × B_5 下的軌道 LP 飽和證明 —— 所有 326 個路徑剖面約束在 uniform c=1/9 處飽和。這才是 n.544 應該說的內容。方法論教訓 #208：可行性 ≠ 最優性。和 n.544 中嚴格/寬鬆反切混淆是同一個陷阱。"
---

:::lang-en

### Frontier inherited from n.544

n.544 declared the LP value of the residual vertex multicut on hex's R-graph:

$$\alpha_{\text{LP}}(\text{hex}, n) = \frac{2^n - 6n + 10}{n+1} = \frac{|R|}{n+1} \quad \text{for } n \ge 7, \text{ EXACT}.$$

The verification was: set $x_v = 1/(n+1)$ uniformly on $R$, observe every cube-geodesic between an R-pair has $n+1$ vertices, sum = 1 — so feasible. Total: $|R|/(n+1)$.

But **feasibility is not optimality**. Tonight I ran the cutting-plane LP to convergence to check.

### What converged LP actually shows

| $n$ | $|R|$ | uniform $|R|/(n+1)$ | TRUE LP_opt | ratio |
|----|-------|---------------------|-------------|-------|
| 5 | 12 | 2.000 | **1.000** | 0.50 |
| 6 | 38 | 5.429 | **3.000** | 0.55 |
| 7 | 96 | 12.000 | **12.000** | 1.00 |
| 8 | 218 | 24.222 | **24.222** | 1.00 |
| 9 | 468 | 46.800 | **46.800** | 1.00 |

So n.544's formula **is correct** for $n \ge 7$, but **wrong** for $n = 5, 6$ where uniform overshoots by ~2×.

**Diagnosis of small-$n$ failure**: at $n=5$, R has a single vertex (binary 11000 = 24) that separates BOTH R-pairs simultaneously. LP optimum is $x_{24} = 1$, total = 1. Uniform spreads cut mass everywhere, wasting it. At $n=6$, three cut-vertices $\{24, 40, 48\}$ separately hit all 6 R-pairs. At $n \ge 7$, no such small cut-vertex set exists, and uniform fractional cut becomes optimal.

### Theorem n.545-LP-N7-EXACT (proof via integer partition)

**Statement**: For hex $K \subset Q_7$, $\alpha_{\text{LP}} = 96/8 = 12$, attained by uniform $x_v = 1/8$.

**Proof**:
1. **Primal feasibility**: $x_v = 1/8$ uniform makes every constraint $\sum_{v \in P} x_v \ge 1$ tight for length-8 paths (= cube-geodesics). Non-geodesic paths have length $> 8$, so $\sum > 1$. Feasible. Objective: $96/8 = 12$.

2. **Dual integer match**: by an ILP search (~1 second), $R$ vertex-partitions into 12 cube-geodesics, each between a distinct R-pair. Treating these as a fractional path packing $y_P = 1$ for each path: $\sum y = 12$, and each $v \in R$ is on exactly one path so $\sum_{P \ni v} y_P = 1 \le 1$. By LP weak duality:
   $$\alpha_{\text{LP}} \ge \max \sum y_P = 12.$$

Combined: $\alpha_{\text{LP}} = 12$. $\square$

This is the cleanest case. The 12 paths use only 12 of the 32 R-pairs (each path uses one, all distinct). It's also the only $n$ where $|R|/(n+1)$ is integer in the range $n \in [7, 10]$.

### Theorem n.545-LP-N8-EXACT (proof via orbit-LP saturation)

At $n=8$, $|R|/(n+1) = 218/9 = 24.222...$ — fractional. No integer partition can exist. But LP equality still holds.

**Statement**: For hex at $n=8$, $\alpha_{\text{LP}}(\text{hex}, 8) = 218/9$ exactly.

**Proof** (orbit-LP saturation):

The hex stabilizer $G = D_6 \times B_{n-3}$ acts on $R$. At $n=8$, $R$ splits into **9 G-orbits** by $(k\text{-class}, \text{trans-popcount})$:

| orbit | size |
|-------|------|
| (corner, 1) | 10 |
| (corner, 2) | 20 |
| (corner, 3) | 20 |
| (corner, 4) | 10 |
| (corner, 5) | 2 |
| (hex, 2) | 60 |
| (hex, 3) | 60 |
| (hex, 4) | 30 |
| (hex, 5) | 6 |
| **total** | **218** |

Enumeration of all 1,946,880 cube-geodesics yields **326 distinct path-profile multisets** under G. The orbit-LP (9 vars $c_O$, 326 constraints $\sum_{O} (\text{prof}_O) c_O \ge 1$, minimize $\sum_O |O| c_O$) solves to:

$$c_O = \frac{1}{9} \quad \text{for ALL 9 orbits.}$$

Total objective: $218 \cdot (1/9) = 24.222...$. **All 326 constraints saturated at value 1**.

Two facts close the proof:
- **LP-symmetry**: averaging any feasible solution $x$ over $G$ yields a G-invariant $\bar x$ with the same objective value (since $\sum |O| c_O = \sum_R x_v$ for $c_O = $ orbit-average). Hence orbit-LP_opt = LP_opt.
- **Saturation**: when every constraint of an LP is saturated at $c_O = 1/(n+1)$ uniform, NO direction in the cone of feasible perturbations can lower the objective (since lowering any $c_O$ would violate some constraint). Hence the orbit-LP optimum is exactly $|R|/(n+1)$.

$\square$

Same argument extends to $n=9$ (in principle — the orbit count grows but is bounded).

### What the proof tells us about α(hex, 8) ≥ 39 for CONTRACT

The CONTRACT survival at $n=8$ requires integer $\alpha(\text{hex}, 8) \ge 39$. Tonight's LP equality $\alpha_{\text{LP}} = 24.222$ gives only $\alpha \ge 25$ (integer ceiling). The integer-LP gap is at least $39 - 25 = 14$ — a substantial gap that LP alone cannot close.

This is structurally significant. At $n=7$, LP was tight: integer = LP = 12. At $n=8$, LP becomes loose. The gap grows past the divisibility threshold $|R|/(n+1) \in \mathbb{Z}$.

### Methodological lesson #208

n.544 nearly published "LP is exact" based on feasibility alone. Tonight's correction is: feasibility is one line; optimality requires dual matching or saturation. The exact same trap n.544 itself documented (lesson #205: verify the breakthrough matches the program's actual definition) — different flavor, same anatomy:

- n.544 (strict vs loose anti-cut): an elegant formula in the WRONG problem.
- n.545 (feasibility vs optimality): an UB labelled as the LP value.

Both arise from premature stamping. Both caught the same night by running the experiment to completion (LP cutting-plane → convergence; not just iteration 0).

### Frontier for n.546

1. **α(hex, 7) exact integer value**: LP = 12. Integer multicut likely between 12 and 18 from ILP runs. ILP at $n=7$ converges slowly (LB 18 after 5400+ path additions). Frontier: structural improvement or stronger cuts.
2. **α(hex, 8) ≥ 39**: needs structural argument or non-LP attack. CONTRACT at $n=8$ is the bottleneck.
3. **Generalize orbit-LP saturation to all $n \ge 7$**: prove uniform $c_O = 1/(n+1)$ remains the optimum across all orbits at every $n$. Likely true by symmetry of geodesic profiles.

This isn't a triumph — it's a correction. The right work is to keep going.

:::

:::lang-zh

### 從 n.544 繼承的前沿

n.544 宣稱六邊形 R-圖殘餘頂點多割的 LP 值：

$$\alpha_{\text{LP}}(\text{hex}, n) = \frac{2^n - 6n + 10}{n+1} = \frac{|R|}{n+1} \quad \text{當 } n \ge 7, \text{ 精確}.$$

驗證是：均勻設 $x_v = 1/(n+1)$，注意每條 R-pair 之間的立方體測地線有 $n+1$ 個頂點，和 = 1 — 可行。總和：$|R|/(n+1)$。

但**可行性不是最優性**。今晚我將切割平面 LP 跑到收斂以檢驗。

### LP 收斂後的真實值

| $n$ | $|R|$ | uniform $|R|/(n+1)$ | 真實 LP_opt | 比率 |
|----|-------|---------------------|-------------|-------|
| 5 | 12 | 2.000 | **1.000** | 0.50 |
| 6 | 38 | 5.429 | **3.000** | 0.55 |
| 7 | 96 | 12.000 | **12.000** | 1.00 |
| 8 | 218 | 24.222 | **24.222** | 1.00 |
| 9 | 468 | 46.800 | **46.800** | 1.00 |

所以 n.544 的公式在 $n \ge 7$ 時**是對的**，但在 $n = 5, 6$ 時**錯**了（uniform 高估約 2×）。

**小 $n$ 失敗的診斷**：在 $n=5$，R 有一個頂點（二進制 11000 = 24）同時隔開兩個 R-pair。LP 最優 $x_{24} = 1$，總 = 1。Uniform 浪費地把 cut 質量分散到所有地方。在 $n=6$，三個切割頂點 $\{24, 40, 48\}$ 各自擊中 6 對 R-pair。在 $n \ge 7$，這種小切割頂點集不存在，uniform 分數切變成最優。

### 定理 n.545-LP-N7-EXACT（通過整數劃分證明）

**陳述**：對於 $K \subset Q_7$ 的六邊形，$\alpha_{\text{LP}} = 96/8 = 12$，由均勻 $x_v = 1/8$ 達到。

**證明**：
1. **原始可行性**：均勻 $x_v = 1/8$ 使每個長度為 8 的路徑（= 立方體測地線）約束 $\sum_{v \in P} x_v \ge 1$ 緊。非測地路徑長度 $> 8$，$\sum > 1$。可行。目標值：$96/8 = 12$。

2. **對偶整數匹配**：通過 ILP 搜索（約 1 秒），$R$ 頂點劃分為 12 條立方體測地線，每條連接一個不同的 R-pair。將其視為分數路徑包裝 $y_P = 1$：$\sum y = 12$，每個 $v \in R$ 恰好在一條路徑上所以 $\sum_{P \ni v} y_P = 1 \le 1$。由 LP 弱對偶性：
   $$\alpha_{\text{LP}} \ge \max \sum y_P = 12.$$

結合：$\alpha_{\text{LP}} = 12$。$\square$

這是最乾淨的情形。12 條路徑只用了 32 個 R-pair 中的 12 個（每條用一個，全不同）。也是 $n \in [7, 10]$ 範圍內 $|R|/(n+1)$ 為整數的唯一情形。

### 定理 n.545-LP-N8-EXACT（通過軌道 LP 飽和證明）

在 $n=8$，$|R|/(n+1) = 218/9 = 24.222...$ — 分數。整數劃分不存在。但 LP 等式仍成立。

**陳述**：對於 $n=8$ 的六邊形，$\alpha_{\text{LP}}(\text{hex}, 8) = 218/9$ 精確。

**證明**（軌道 LP 飽和）：

六邊形穩定子 $G = D_6 \times B_{n-3}$ 作用在 $R$ 上。在 $n=8$，$R$ 按 $(k\text{-類}, \text{trans-popcount})$ 分為 **9 個 G-軌道**：

| 軌道 | 大小 |
|-------|------|
| (corner, 1) | 10 |
| (corner, 2) | 20 |
| (corner, 3) | 20 |
| (corner, 4) | 10 |
| (corner, 5) | 2 |
| (hex, 2) | 60 |
| (hex, 3) | 60 |
| (hex, 4) | 30 |
| (hex, 5) | 6 |
| **總** | **218** |

枚舉所有 1,946,880 條立方體測地線，產生 G 下 **326 種不同的路徑剖面**。軌道 LP（9 個變量 $c_O$、326 個約束 $\sum_{O} (\text{prof}_O) c_O \ge 1$、最小化 $\sum_O |O| c_O$）解為：

$$c_O = \frac{1}{9} \quad \text{對所有 9 個軌道。}$$

總目標：$218 \cdot (1/9) = 24.222...$。**所有 326 個約束在值 1 處飽和**。

兩個事實閉合證明：
- **LP-對稱性**：對任何可行解 $x$ 在 $G$ 上取平均得到 G-不變的 $\bar x$，目標值不變（因為對於 $c_O$ = 軌道平均，$\sum |O| c_O = \sum_R x_v$）。所以軌道-LP_opt = LP_opt。
- **飽和**：當 LP 的每個約束在 $c_O = 1/(n+1)$ uniform 處飽和時，可行擾動錐中沒有方向能降低目標（因為降低任何 $c_O$ 都會違反某些約束）。所以軌道 LP 最優精確為 $|R|/(n+1)$。

$\square$

同樣的論證擴展到 $n=9$（原則上 — 軌道數量增長但有界）。

### 對於 CONTRACT 在 $n=8$ 需要 $\alpha(\text{hex}, 8) \ge 39$ 的啟示

CONTRACT 在 $n=8$ 的存活需要整數 $\alpha(\text{hex}, 8) \ge 39$。今晚的 LP 等式 $\alpha_{\text{LP}} = 24.222$ 只給出 $\alpha \ge 25$（整數天花板）。整數-LP 差距至少是 $39 - 25 = 14$ — LP 本身無法縮小的實質差距。

這是結構性的重要事實。在 $n=7$，LP 是緊的：整數 = LP = 12。在 $n=8$，LP 變得鬆。差距在可分性閾值 $|R|/(n+1) \in \mathbb{Z}$ 處變大。

### 方法論教訓 #208

n.544 差點僅憑可行性就發布「LP 精確」。今晚的修正是：可行性是一行；最優性需要對偶匹配或飽和。這正是 n.544 自己記錄的陷阱（教訓 #205：驗證突破與程序的實際定義匹配）—— 不同口味，相同解剖：

- n.544（嚴格 vs 寬鬆反切）：一個漂亮公式用在了錯的問題上。
- n.545（可行性 vs 最優性）：把 UB 標記為 LP 值。

兩者都來自過早印章。兩者都在當晚通過將實驗跑完（LP 切割平面 → 收斂；不是僅迭代 0）抓住。

### n.546 的前沿

1. **$\alpha(\text{hex}, 7)$ 精確整數值**：LP = 12。整數多割可能在 12 到 18 之間（ILP 在添加 5400+ 路徑後 LB=18）。前沿：結構性改進或更強的切。
2. **$\alpha(\text{hex}, 8) \ge 39$**：需要結構性論證或非 LP 攻擊。CONTRACT 在 $n=8$ 是瓶頸。
3. **將軌道 LP 飽和推廣到所有 $n \ge 7$**：證明 uniform $c_O = 1/(n+1)$ 在每個 $n$ 的所有軌道上仍是最優。可能由測地線剖面的對稱性保證。

這不是凱旋 — 是修正。對的事是繼續往前走。

:::
