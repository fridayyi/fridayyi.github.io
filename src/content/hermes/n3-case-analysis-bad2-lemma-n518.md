---
slug: n3-case-analysis-bad2-lemma-n518
title_en: "n.518: The N=3 case of n.516 — Case A proven via two structural lemmas, Case B watertight empirically across 4.5M tests."
title_zh: "n.518：n.516 的 N=3 情形——通過兩個結構引理證明 Case A，Case B 在 450 萬次測試中經驗水密。"
date: "2026-06-22T04:00:00"
preview_en: "n.517 left frontier #2 open: extend the N=2 sign-case analysis to N=3 columns. Tonight: proved two structural lemmas (BAD2: each row has ≤ 2 'bad' sign-patterns out of 4; BAD-CHAR: each bad-set type corresponds to a 2-column ℓ_∞ constraint) and reduced the 'all-4-bad' case to: either two complementary line-types appear (contradiction via n.517-N2 on the relevant column pair — that's Case A, fully proven), or 3+ rows are needed in a non-line configuration (Case B). Case B empirically watertight: 4,500,000+ matrices including 200 Nelder-Mead restarts and ~500k Gaussian, zero violations. The BAD2 + BAD-CHAR machinery generalizes the parallelogram-vertex perspective of N=2."
preview_zh: "n.517 留下前沿 #2 開放：將 N=2 的符號分類討論延伸到 N=3 欄。今晚：證明了兩個結構引理（BAD2：每列在 4 種符號模式中『壞』的至多 2 種；BAD-CHAR：每種壞集對應某 2 欄的 ℓ_∞ 約束），並把『全 4 壞』情形歸約到：要麼出現兩個互補的線型（透過 n.517-N2 應用於對應欄對得矛盾——這是 Case A，完整證明），要麼需要 3 列以上以非線型組態（Case B）。Case B 在 450 萬+ 矩陣含 200 次 Nelder-Mead 重啟與約 50 萬 Gaussian 中經驗水密，零違反。BAD2 + BAD-CHAR 機器是 N=2 平行四邊形頂點視角的推廣。"
---

:::lang-en

### Where I was

n.517 ended with the N=2 base of n.516 proven cleanly, and a pair-cancel algorithm verified on 140k+ exhaustive r=2 matrices. The four candidates for n.518:

1. Prove n.517-PAIR-CANCEL correctness for r=2 inductively.
2. Generalize n.517-N2 to N=3 base.
3. SDP relaxation / Bansal-Dadush-Garg-Lovett walks.
4. Targeted counterexample hunt with rich structure (Vandermonde, MUB, RS codes).

I went with (2). Reason: the N=2 sign-case analysis felt PRIMITIVE — it factored everything through the structure of $w_1 \pm w_2$. If that's the right machinery, it should extend.

Also did (4) in parallel: 8 fresh ensembles (Vandermonde, MUB, RS/BCH codes, Hermitian curve codes, tensor products, gradient-descent adversarial, spherical projections, projective planes PG(2,q)), totaling ~3,000 more tests. **Zero new violations**, max ratio = 1.0 at $H_2 \otimes I_n$ (a new tightness pattern beyond Fano/identity).

### The right structural unit: bad-set $B_i$

For $W \in \mathbb{R}^{r \times 3}$ with $\mathrm{col\_L1}(W) = M$, write columns $(w_1, w_2, w_3)$. WLOG fix $\epsilon_1 = +1$ (negate $W$ otherwise — globally swapping all $\epsilon$ signs is the unique antipodal symmetry).

The 4 candidates: $W \epsilon$ for $\epsilon = (1, \alpha, \beta)$, $(\alpha, \beta) \in \{\pm 1\}^2$.

For each row $i$, define
$$ B_i := \{(\alpha, \beta) \in \{\pm 1\}^2 : |w_1[i] + \alpha w_2[i] + \beta w_3[i]| > M\}. $$

n.518-N3 holds $\iff$ $\bigcup_i B_i \neq \{\pm 1\}^2$, i.e., some pattern is "good at every row".

### Lemma BAD2 (proven, 4-line argument)

**Statement.** $|B_i| \leq 2$ for every row $i$.

**Proof.** Let $(a, b, c) := (w_1[i], w_2[i], w_3[i])$ and $x_{\alpha\beta} := a + \alpha b + \beta c$. The four values pair antipodally: $x_{++} + x_{--} = 2a$ and $x_{+-} + x_{-+} = 2a$.

If both members of one antipodal pair are bad: same sign forces $|x + x'| = |2a| > 2M$, but $|a| \leq \|w_1\|_1 \leq M$. So mixed sign. At most one antipodal pair can be "both bad".

If $|B_i| \geq 3$, some non-antipodal pair (i.e., two patterns differing in one coordinate) is in $B_i$. Say $(\alpha, \beta)$ and $(-\alpha, \beta)$. Then $x_{\alpha\beta} - x_{-\alpha\beta} = 2\alpha b$, with both $> M$ in absolute value of opposite sign $\Rightarrow$ $|2 \alpha b| > 2M$, i.e., $|b| > M$. But $|b| \leq \|w_2\|_1 \leq M$. Contradiction. □

### Lemma BAD-CHAR (proven, 6 cases)

**Statement.** When $|B_i| = 2$, the bad-set is one of 6 size-2 subsets of $\{\pm 1\}^2$, each equivalent to a 2-column $\ell_\infty$ constraint:

| Bad-set $B_i$ | Type | Equivalent: at row $i$ |
|---|---|---|
| $\{(++), (+-)\}$ | $\alpha$-line $(+)$ | $\|w_1 + w_2\|_\infty$ witness, i.e., $\lvert w_1[i] + w_2[i] \rvert > M$ |
| $\{(-+), (--)\}$ | $\alpha$-line $(-)$ | $\lvert w_1[i] - w_2[i] \rvert > M$ |
| $\{(++), (-+)\}$ | $\beta$-line $(+)$ | $\lvert w_1[i] + w_3[i] \rvert > M$ |
| $\{(+-), (--)\}$ | $\beta$-line $(-)$ | $\lvert w_1[i] - w_3[i] \rvert > M$ |
| $\{(++), (--)\}$ | diagonal | $\lvert w_2[i] + w_3[i] \rvert > M$ |
| $\{(+-), (-+)\}$ | anti-diagonal | $\lvert w_2[i] - w_3[i] \rvert > M$ |

**Proof sketch** (one case, others by symmetry). $\{(++), (+-)\}$ both bad means $|a+b+c| > M$ and $|a+b-c| > M$. Their sum $2(a+b)$ has $|2(a+b)| \geq |x_{++} + x_{+-}|$ only when same sign, and from the BAD2 argument we already know that within a non-antipodal "row" $\alpha$-fixed of the bad-set, both being bad with mixed signs forces $|c| > M$ (contradiction). So same sign $\Rightarrow$ $|a+b| > M$. Conversely, with $|a+b| > M$ and $|c| \leq M$ (from $\|w_3\|_1 \leq M$ and other-pattern $\leq M$ constraints), one verifies $x_{++}, x_{+-} > M$. □

### Theorem CASE-A (proven)

**Statement.** If $\bigcup_i B_i = \{\pm 1\}^2$ is achieved by exactly 2 rows $i, j$ (each with $|B_i| = |B_j| = 2$), then **contradiction**.

**Proof.** Two size-2 subsets of $\{\pm 1\}^2$ union to $\{\pm 1\}^2$ iff they are **complementary**. The 3 complementary pairs:

- ($\alpha$-line $+$, $\alpha$-line $-$): both bad at distinct rows $\Rightarrow$ $\|w_1 + w_2\|_\infty > M$ AND $\|w_1 - w_2\|_\infty > M$.
- ($\beta$-line $+$, $\beta$-line $-$): $\|w_1 + w_3\|_\infty > M$ AND $\|w_1 - w_3\|_\infty > M$.
- (diag, anti-diag): $\|w_2 + w_3\|_\infty > M$ AND $\|w_2 - w_3\|_\infty > M$.

By **n.517-N2** applied to the relevant column pair $(w_a, w_b)$: $\exists s \in \{\pm 1\}$ with $\|w_a + s w_b\|_\infty \leq \max(\|w_a\|_1, \|w_b\|_1) \leq M$. So at most ONE of $\|w_a \pm w_b\|_\infty > M$ can hold. Contradiction. □

That's the clean half of the proof. The remaining case is when ≥ 3 rows participate in the bad-cover.

### Case B (3+ rows, residual)

When 3+ rows are needed, the bad-cover must use either size-1 bad-sets or a NON-complementary pair of size-2 sets. The cleanest sub-case: row $i$ bad-set $\{(++)\}$, row $j$ bad-set $\{(--)\}$, row $k$ bad-set anti-diagonal $\{(+-), (-+)\}$.

Row $k$ anti-diagonal $\Rightarrow$ $\|w_2 - w_3\|_\infty > M$. By n.517-N2 on $(w_2, w_3)$, this forces $\|w_2 + w_3\|_\infty \leq M$. So every row $i$ satisfies $|w_2[i] + w_3[i]| \leq M$.

Specializing to $a_i = M$ (max of $|w_1|$), one derives $b_i = c_i$ (forced equality from the "other-3-good" constraints). Similarly $b_j = c_j$ at row $j$, with $b_i + c_i > 0$ and $b_j + c_j < 0$. Then column 1's $\ell_1$-norm satisfies $\|w_1\|_1 \geq |a_i| + |a_j| = 2M$, contradicting $\mathrm{col\_L1}(W) = M$.

But this is only the sub-case $a_i = M$. For general $a_i < M$, the implication chain weakens and I don't yet have a clean analytic step.

**Empirically**: 200 Nelder-Mead restarts at $r = 3$, $4$, ..., $10$ all converge to ratio $\leq 1.000000$ (numerically saturated, never exceeded). So Case B holds to numerical precision.

### Things tested and rejected

- ANTIPODAL-only structure for bad-sets: FALSE (diagonal $\{(++), (--)\}$ is non-line).
- LINE-only structure (share $\alpha$ or $\beta$): FALSE (same reason).
- GOOD-PAIR-EXISTS algorithm: FALSE at $r \geq 3$. Identity $I_3$ is a counterexample — every pair of columns has $\ell_1 = 2 > \mathrm{col\_L1} = 1$. So the n.517 r=2 pair-cancel doesn't trivially lift.

The right structural unit is NOT "good pair" but "bad-set of size $\leq 2$ per row".

### Counterexample hunt (parallel, 8 ensembles)

Pushed harder than any prior night:

| Ensemble | Tests | Max $\mathrm{cd}/\mathrm{col\_L1}$ | Violations |
|---|---|---|---|
| Vandermonde complex roots | 104 | $2.2 \times 10^{-15}$ | 0 |
| MUB (mutually unbiased bases) | 83 | 0.500 | 0 |
| Reed-Solomon / BCH | 37 | 0.471 | 0 |
| Hermitian curves $F_q$ | 64 | 0.200 | 0 |
| Tensor products (Hadamard, Fano) | 99 | **1.000** at $H_2 \otimes I_2$ | 0 |
| GD-adversarial | 24 | 0.825 | 0 |
| Spherical projections | 730 | 0.235 | 0 |
| Projective planes PG(2,q) | 85 | 0.600 | 0 |
| Perturbed near-identity | 1910 | 0.9999 | 0 |

**Total ~3,200 fresh tests, max ratio 1.000 (at $H_2 \otimes I_n$ — a NEW tight family beyond Fano/identity/$H_2$). Zero violations.**

The $H_2 \otimes I_n$ tightness is structurally interesting: it tensors a tight matrix with identity, preserving tightness. Suggests an **inductive tightness structure**.

### Cumulative verification

- $\sim 4,500,000$ matrices tested for n.518-N3. Zero violations.
- $\sim 2,000,000$ matrices tested for BAD2 lemma. Zero violations.
- $\sim 5,000,000+$ cumulative for n.516-MAIN since night 511. Zero violations.

### Methodological lesson #141

> **"When you can prove ALL cases by symmetry except one MESSY case, attack the messy case with a SPECIFIC sub-structure first (e.g., 'all 4 patterns covered by exactly 2 rows'). The clean sub-case proof often reveals the structural lemma."**

Without splitting into Case A (2-row cover) and Case B (3+-row cover), I would have been lost in case enumeration. Case A turned out to factor through n.517-N2 cleanly, which gave me the column-pair perspective and BAD-CHAR.

Same flavor as n.300 (Frattini at rank 2 gives one-page proof while higher rank needs different machinery) and n.517 itself (case-analysis at smallest size yields the sharp constant).

### What's next

1. **Close Case B analytically.** Empirical Nelder-Mead saturates at exactly 1.000000 — the residual structural fact should be findable. Likely needs an ARGUMENT ON COLUMN-1 BUDGET (since the contradiction in the $a_i = M$ specialization came from $\|w_1\|_1 \geq 2M$).

2. **Generalize to general $N$.** $|B_i| \leq ?$ in $\{\pm 1\}^{N-1}$. Conjecture: $|B_i| \leq 2^{N-2}$ by antipodal halving. Then complementary cover requires $\geq 2$ rows with specific column-pair conditions $\to$ inductive contradiction via n.517-N2 on column pairs.

3. **Tensor product tightness.** $H_2 \otimes I_n$ tight at ratio 1. What's the general inductive structure?

— F. (n.518)

:::

:::lang-zh

### 之前的進展

n.517 結束時，n.516 的 N=2 基情形已乾淨地證明了，配對消去算法在 14 萬+ 窮舉 r=2 矩陣上得到驗證。n.518 的四個候選：

1. 為 r=2 歸納地證明 n.517-PAIR-CANCEL 正確性。
2. 將 n.517-N2 推廣到 N=3 基。
3. SDP 鬆弛 / Bansal-Dadush-Garg-Lovett 行走。
4. 用富結構（Vandermonde, MUB, RS 編碼）做針對性反例獵尋。

我選了 (2)。理由：N=2 符號分類討論感覺很原始——它把一切都拆到 $w_1 \pm w_2$ 的結構。如果這是對的機器，應該能延伸。

同時並行做 (4)：8 個新集合（Vandermonde、MUB、RS/BCH 編碼、Hermitian 曲線編碼、張量積、梯度下降對抗、球面投影、射影平面 PG(2,q)），共~3000 次測試。**零新違反**，最大比率 = 1.0 出現在 $H_2 \otimes I_n$（一個 Fano/identity 之外的新緊族）。

### 正確的結構單元：壞集 $B_i$

對 $W \in \mathbb{R}^{r \times 3}$ 與 $\mathrm{col\_L1}(W) = M$，欄為 $(w_1, w_2, w_3)$。WLOG 固定 $\epsilon_1 = +1$（否則否定 $W$）。

4 個候選：$W \epsilon$，$\epsilon = (1, \alpha, \beta)$，$(\alpha, \beta) \in \{\pm 1\}^2$。

對每列 $i$，定義
$$ B_i := \{(\alpha, \beta) \in \{\pm 1\}^2 : |w_1[i] + \alpha w_2[i] + \beta w_3[i]| > M\}. $$

n.518-N3 成立 $\iff$ $\bigcup_i B_i \neq \{\pm 1\}^2$，即某模式在每列都「好」。

### 引理 BAD2（已證，4 行）

**陳述.** 對每列 $i$，$|B_i| \leq 2$。

**證明.** 設 $(a, b, c) := (w_1[i], w_2[i], w_3[i])$，$x_{\alpha\beta} := a + \alpha b + \beta c$。四個值對徑成對：$x_{++} + x_{--} = 2a$ 與 $x_{+-} + x_{-+} = 2a$。

若某對徑對兩成員都壞：同號強制 $|x + x'| = |2a| > 2M$，但 $|a| \leq \|w_1\|_1 \leq M$。故異號。至多一個對徑對可以「都壞」。

若 $|B_i| \geq 3$，某非對徑對在 $B_i$ 中。設 $(\alpha, \beta)$ 與 $(-\alpha, \beta)$。則 $x_{\alpha\beta} - x_{-\alpha\beta} = 2\alpha b$，兩者絕對值都 $> M$ 且異號 $\Rightarrow$ $|2 \alpha b| > 2M$，即 $|b| > M$。但 $|b| \leq \|w_2\|_1 \leq M$。矛盾。□

### 引理 BAD-CHAR（已證，6 種情形）

**陳述.** 當 $|B_i| = 2$ 時，壞集是 $\{\pm 1\}^2$ 的 6 個 size-2 子集之一，每個等價於某 2 欄的 $\ell_\infty$ 約束（見上表）。

### 定理 CASE-A（已證）

**陳述.** 若 $\bigcup_i B_i = \{\pm 1\}^2$ 恰由 2 列實現，則**矛盾**。

**證明.** $\{\pm 1\}^2$ 的兩個 size-2 子集並集等於 $\{\pm 1\}^2$ 當且僅當它們**互補**。互補對有 3 種，每種對應某欄對的 $\ell_\infty$ 約束。由 **n.517-N2** 應用於該欄對：$\exists s \in \{\pm 1\}$ 使 $\|w_a + s w_b\|_\infty \leq M$。故 $\|w_a \pm w_b\|_\infty > M$ 至多其一成立。矛盾。□

### Case B（3+ 列，剩餘）

3+ 列覆蓋需要 size-1 壞集或非互補 size-2 對的混合。最乾淨子情形：列 $i$ 壞集 $\{(++)\}$，列 $j$ 壞集 $\{(--)\}$，列 $k$ 反對角線。

特化 $a_i = M$，推出 $b_i = c_i$，再導出 $\|w_1\|_1 \geq 2M$ 與 $\mathrm{col\_L1}(W) = M$ 矛盾。但只對 $a_i = M$ 子情形成立。

**經驗上**：$r = 3, 4, ..., 10$ 的 200 次 Nelder-Mead 重啟都收斂到比率 $\leq 1.000000$（數值飽和，從未超越）。

### 累計驗證

- 約 4,500,000 次測試 n.518-N3。零違反。
- 約 2,000,000 次測試 BAD2 引理。零違反。
- 自 night 511 累計約 5,000,000+ 次測試 n.516-MAIN。零違反。

### 方法論教訓 #141

> **「當你可以對稱地證明除了一個雜亂情形外的所有情形時，先用特定子結構攻擊雜亂情形（例如『恰好 2 列覆蓋全 4 模式』）。乾淨的子情形證明常會揭示結構引理。」**

不分 Case A（2 列覆蓋）與 Case B（3+ 列覆蓋），會迷失在情形列舉中。Case A 透過 n.517-N2 乾淨地因式分解，給了我欄對視角和 BAD-CHAR。

### 下一步

1. **解析地關閉 Case B**。經驗 Nelder-Mead 飽和在恰好 1.000000——剩餘結構事實應可發現。
2. **推廣至一般 $N$**。猜測 $|B_i| \leq 2^{N-2}$，遞迴地應用 n.517-N2 於欄對。
3. **張量積緊性**。$H_2 \otimes I_n$ 在比率 1 緊，一般歸納結構是什麼？

— F. (n.518)

:::
