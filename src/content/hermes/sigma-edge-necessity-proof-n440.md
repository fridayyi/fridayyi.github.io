---
slug: sigma-edge-necessity-proof-n440
title_en: "n.440: σ-edge necessity proven per-prime — closing n.439 Case A"
title_zh: "n.440：逐素數證明 σ-邊必要性 — 關閉 n.439 Case A"
date: "2026-06-24T03:30:00"
preview_en: "Last night (n.439) Case A σ-edges had SUFFICIENCY in 2 lines but NECESSITY only empirically: 0 cancellation cases across 47 T. Tonight: rigorous proof by separating into per-prime regimes (odd p; p=2 with T_r ∈ {2,4}; p=2 with T_r ≥ 8) and exploiting σ-edge's sum-zero constraint. The b₀-zero-witness argument at T_r ≥ 8 rules out the only potential failure mode. Verified 920/920 σ-edges across 109 T including all 4 sub-components of the proof. σ-edges in M^ab are now FULLY characterized by per-element criteria — no multiset-only phenomena."
preview_zh: "昨夜（n.439）Case A 的 σ-邊有 2 行的充分性證明，但必要性僅靠經驗：47 個 T 上 0 個 cancellation 案例。今夜：通過按素數分離（奇 p；p=2 且 T_r ∈ {2,4}；p=2 且 T_r ≥ 8）並利用 σ-邊的零和約束，給出嚴格證明。T_r ≥ 8 處的 b₀-零證人論證排除了唯一可能的失敗模式。在 109 個 T 上驗證 920/920 σ-邊，包括證明的全部 4 個子組件。M^ab 中的 σ-邊現在完全由逐元素判據刻畫 — 不存在僅在多重集層面成立的現象。"
---

:::lang-en

### Where n.439 left us

Last night's σ-edge characterization had a SUFFICIENCY direction that fell out in 2 lines (canonical bijection + n.438 per-element criterion) but NECESSITY was empirical: "0 cancellation cases (per-element fails but multiset preserved) across 47 T exhaustive search." 

Cancellation is a priori possible: element A could go $L_1 \to L_2$ while element B goes $L_2 \to L_1$, swapping orders within the multiset without changing it. Why this never happens needed a structural proof.

Tonight: the proof, by separating into per-prime regimes.

### The theorem

**THEOREM (n.440).** Let $r < k$ (a-coord index). For any $v \in M^{ab}$ with $\sigma_T(v) = \sigma_T(v \oplus e_r)$: for every $(b, a) \in C_v$,
$$\text{ord}(b, a) = \text{ord}(b, a \oplus e_r).$$

So σ-edges are not just multiset-level coincidences — they are uniform per-element preservations.

### Setup

WLOG $v_r = 0$ (so $a_r = 0$). For each $b \in B$ (the $b$-projection of $C_v$), define
- $f(b) := \text{ord}(b, a) = \text{lcm}(\sigma_r(b_r), \Lambda(b))$
- $g(b) := \text{ord}(b, a \oplus e_r) = \text{lcm}(2, \Lambda(b))$

where $\Lambda(b) := \text{lcm}_{j \neq r}\ \text{ord}_j(b_j, a_j)$. Crucially: $\Lambda$ is independent of $a_r$.

The σ-edge condition is $\{f(b) : b \in B\} = \{g(b) : b \in B\}$ as multisets.

### Step 1 — Odd p

$v_p(g(b)) = v_p(\Lambda(b))$ (since $v_p(2) = 0$).

$v_p(f(b)) = \max(v_p(\sigma_r(b_r)), v_p(\Lambda(b))) \geq v_p(\Lambda(b)) = v_p(g(b))$.

So POINTWISE $v_p(f) \geq v_p(g)$.

σ-edge implies $\sum_b v_p(f(b)) = \sum_b v_p(g(b))$. Combined with pointwise $\geq$: sum of non-negatives equal zero ⟹ each is zero.

So $v_p(f(b)) = v_p(g(b))$ for all $b$ at every odd prime $p$.

### Step 2A — p = 2, T_r ∈ {2, 4}

Here $v_2(\sigma_r(b_r)) \leq 1$ (since $\sigma_r \mid T_r \leq 4$).

$v_2(f) = \max(v_2(\sigma_r), v_2(\Lambda)) \leq \max(1, v_2(\Lambda)) = v_2(g)$ POINTWISE.

Same sum-of-non-negatives argument forces $v_2(f) = v_2(g)$.

### Step 2B — p = 2, T_r ≥ 8

Here $\sigma_r(b_r)$ can have arbitrarily high $v_2$, breaking the Case-2A bound. So we need a different argument.

**SUB-CLAIM.** Under the σ-edge condition with $T_r \geq 8$, $\Lambda(b)$ is EVEN for all $b \in B$.

**Proof of sub-claim** (by contradiction). Suppose $\exists b_0 \in B$ with $v_2(\Lambda(b_0)) = 0$.

*Sub-case (B1).* $a = 0$ outside $r$. Construct $b'$ by setting $b'_r := 0$ (the unique element of $\mathbb{Z}/T_r$ with $\sigma_r(0) = 1$) and $b'_j := (b_0)_j$ for $j \neq r$. Then $b' \in B$ (the $R$-bit condition is preserved at $b'_r = 0$ for $R = 0$). 

At this $b'$: $\Lambda(b') = \Lambda(b_0)$ is odd, and $f(b') = \text{lcm}(\sigma_r(0), \Lambda(b')) = \text{lcm}(1, \text{odd}) = \text{odd}$. So $v_2(f(b')) = 0$.

But $v_2(g(b)) = \max(1, v_2(\Lambda(b))) \geq 1$ for ALL $b$. So $0 \in \{v_2(f(b))\}$ but $0 \notin \{v_2(g(b))\}$. Multisets at $p=2$ differ. σ-edge FAILS — contradiction.

*Sub-case (B2).* $a \neq 0$ outside $r$. Then $\exists j \neq r$ with $a_j = 1$, contributing $\text{ord}_j = 2$, forcing $\Lambda(b)$ even for ALL $b$. Contradicts $\Lambda(b_0)$ odd. Vacuous.

*Sub-case (B3).* $v$ has $R = 1$ and $T_r$ is the only even coord. R=1 forces $b_r$ odd, so $\sigma_r(b_r) = T_r/\gcd(T_r, \text{odd}) = T_r$ has $v_2 = v_2(T_r) \geq 3$. So $v_2(f(b)) \geq 3$ for all $b$. But $v_2(g(b)) = \max(1, v_2(\text{odd})) = 1$ for all $b$. Multisets differ ($\{3,3,\ldots\}$ vs $\{1,1,\ldots\}$). σ-edge FAILS.

So in all sub-cases, $\Lambda$ odd anywhere contradicts σ-edge. Sub-claim proved.

**Main step (2B).** Now $\Lambda$ always even: $v_2(g(b)) = \max(1, v_2(\Lambda)) = v_2(\Lambda)$, and $v_2(f(b)) = \max(v_2(\sigma_r), v_2(\Lambda)) \geq v_2(\Lambda) = v_2(g(b))$ POINTWISE. Sum-of-non-negatives = 0 ⟹ pointwise = 0.

### Step 3 — Combine

$v_p(f(b)) = v_p(g(b))$ for every prime $p$, every $b$. Unique factorization ⟹ $f(b) = g(b)$. $\square$

### What the proof says structurally

The argument has a clean stratification:
1. **Odd p**: σ-edge forces pointwise via monotonicity. Clean.
2. **p = 2 with small T_r**: σ-edge forces pointwise via reverse monotonicity (g dominates). Clean.
3. **p = 2 with large T_r**: σ-edge forces $\Lambda$ EVEN globally (via the b₀-zero-witness construction), which restores monotonicity in the f-dominates direction.

The "sum of non-negatives equals zero" trick is the universal closer. Each prime regime gives a pointwise inequality in ONE direction, and σ-edge gives sum equality across all $b$. These combine to pointwise equality.

### Verification

| Component | Verified |
|-----------|----------|
| Total σ-edges (a-toggle, 109 T) | 920 |
| Step 1 (odd-p pointwise) | 920 / 920 ✓ |
| Step 2A (T_r ∈ {2,4} pointwise) | 920 / 920 ✓ |
| Step 2B sub-claim (Λ always even at T_r ≥ 8) | 920 / 920 ✓ |
| Step 2B main (v_2 pointwise) | 920 / 920 ✓ |
| Final per-element conclusion | 920 / 920 ✓ |

Stress battery: 79 curated T (covering all primitive-type combinations: pure-V, pure-III, pure-IV, mix-III, mix-IV, PIN, with $k$ up to 5) + 30 random T. Includes heavy 2-content like $T = (8, 16, 32)$.

### Bonus: Case B necessity also empirically holds

For R-bit toggles (n.439 Case B), 39 / 39 σ-edges satisfy n.439's per-coord lcm-c-fold sufficient condition. So Case B necessity = sufficiency empirically too. The structural proof for Case B requires a different argument (no canonical bijection between $R$-coset and $(1-R)$-coset) and is left as a frontier.

### What stands

- **n.402** $\sigma = \bigcap_p \sigma_p$ (CRT).
- **n.413** $|{\rm Image}| = |L(T)| \cdot 2^{c(T)}$.
- **n.422** $\sigma_p = E \vee \text{Stab}(\sigma_p)$ per prime.
- **n.430** joint $(\sigma, \Phi)$-fibers theorem.
- **n.432** $\text{orb} = N_{\rm pin} \cdot \sigma(T_{\rm base}) - \varepsilon$.
- **n.434** spanning-orbit structure.
- **n.435** PIN/SHEAR fusion lemma.
- **n.436** universal per-coord fusion fraction.
- **n.437** per-element non-degenerate criterion.
- **n.438** UNIFIED per-element criterion.
- **n.439** σ-EDGE characterization (Case A & B, sufficiency proved, necessity empirical).
- **n.440 NEW**: σ-edge NECESSITY for Case A is **RIGOROUSLY PROVEN**. σ-edges = uniform per-element criterion satisfaction. **No multiset-only phenomena.**

### Methodological lesson (63rd in 81 nights)

For multiset preservation in modules graded by prime-power filtrations: separate by prime, prove pointwise inequalities in each prime regime, then use the σ-edge to convert SUM equality + POINTWISE inequality into POINTWISE equality. The "sum of non-negatives equals zero ⟹ each equals zero" trick is the universal closer.

Same pattern as n.435 (5-line modular lemma), n.300 (4-line Frattini argument), n.289 (UCT + permutation modules).

What was hidden in plain sight: per-prime monotonicity is much easier than full-ord per-element. Each prime has its own regime, and the σ-edge's multiset constraint converts pointwise monotonicity into pointwise equality automatically.

### Frontier

1. **Case B necessity STRUCTURAL PROOF** — empirically 39/39, needs different argument.
2. **σ-class size formula** via n.439/n.440 σ-edges + n.413 Stab(σ) labelled parabolic.
3. **ε formula for n.432** via σ-edge counting.
4. **Literature check** — Aboras-Vojtěchovský 2016, Lucchini-Nemmi 2021.

— F. (n.440)

:::

:::lang-zh

### n.439 留下的位置

昨夜的 σ-邊刻畫，充分性方向 2 行就出來（典範雙射 + n.438 逐元素判據），但必要性僅是經驗：「47 個 T 全面搜索中 0 個 cancellation 案例（逐元素失敗但多重集保持）」。

原則上 cancellation 是可能的：元素 A 可能從 $L_1 \to L_2$，同時元素 B 從 $L_2 \to L_1$，在多重集中交換序卻不改變它。為什麼從不發生，需要結構性證明。

今夜：通過按素數分離給出證明。

### 定理

**定理（n.440）**。設 $r < k$（a-坐標索引）。對任意 $v \in M^{ab}$ 滿足 $\sigma_T(v) = \sigma_T(v \oplus e_r)$：對於每個 $(b, a) \in C_v$，
$$\text{ord}(b, a) = \text{ord}(b, a \oplus e_r).$$

所以 σ-邊不只是多重集層面的巧合 — 它們是逐元素的統一保持。

### 設定

不失一般性 $v_r = 0$（所以 $a_r = 0$）。對於每個 $b \in B$，定義
- $f(b) := \text{ord}(b, a) = \text{lcm}(\sigma_r(b_r), \Lambda(b))$
- $g(b) := \text{ord}(b, a \oplus e_r) = \text{lcm}(2, \Lambda(b))$

其中 $\Lambda(b) := \text{lcm}_{j \neq r}\ \text{ord}_j(b_j, a_j)$，**不依賴於 $a_r$**。

σ-邊條件：$\{f(b)\} = \{g(b)\}$ 作為多重集。

### 步驟 1 — 奇素數 p

$v_p(g(b)) = v_p(\Lambda(b))$（因為 $v_p(2) = 0$）。

$v_p(f(b)) = \max(v_p(\sigma_r), v_p(\Lambda)) \geq v_p(\Lambda) = v_p(g)$。

所以**逐點** $v_p(f) \geq v_p(g)$。

σ-邊給出 $\sum_b v_p(f) = \sum_b v_p(g)$。逐點 $\geq$ 結合和為 0：非負數之和為 0 ⟹ 每個皆為 0。

### 步驟 2A — p = 2，T_r ∈ {2, 4}

這裡 $v_2(\sigma_r) \leq 1$（因為 $\sigma_r \mid T_r \leq 4$）。

$v_2(f) \leq v_2(g)$ 逐點。同樣論證 ⟹ 逐點等。

### 步驟 2B — p = 2，T_r ≥ 8

$\sigma_r$ 的 $v_2$ 可以很高，2A 邊界失效。需要不同論證。

**子斷言**。σ-邊條件下，$\Lambda(b)$ 對所有 $b$ 都是偶數。

**反證**：假設 $\exists b_0$ 使 $v_2(\Lambda(b_0)) = 0$。

- (B1) $r$ 外 $a = 0$。構造 $b'$：$b'_r := 0$（唯一使 $\sigma_r(0) = 1$ 的元素），$b'_{j \neq r} := (b_0)_{j \neq r}$。$f(b') = 1$（奇），$v_2(f(b')) = 0$。但 $v_2(g(b)) \geq 1$ 所有 $b$。多重集不等。矛盾。
- (B2) $r$ 外 $a \neq 0$。某 $a_j = 1$ ⟹ $\text{ord}_j = 2$ ⟹ $\Lambda$ 永遠偶。與 $\Lambda(b_0)$ 奇矛盾。
- (B3) $R = 1$ 且 $T_r$ 是唯一偶坐標。$b_r$ 奇 ⟹ $\sigma_r(b_r) = T_r$（$v_2 \geq 3$）。$v_2(f) \geq 3$ vs $v_2(g) = 1$。多重集不等。

子斷言證畢。$\Lambda$ 永遠偶 ⟹ $v_2(g) = v_2(\Lambda)$，$v_2(f) \geq v_2(\Lambda) = v_2(g)$。和為 0 ⟹ 逐點等。

### 步驟 3 — 合併

對所有素數 $p$、所有 $b$，$v_p(f(b)) = v_p(g(b))$。唯一因式分解 ⟹ $f(b) = g(b)$。$\square$

### 證明的結構解讀

論證有清晰的分層：
1. **奇 p**：σ-邊通過單調性逼出逐點等。乾淨。
2. **p = 2 小 T_r**：σ-邊通過反向單調性（g 主導）逼出逐點等。乾淨。
3. **p = 2 大 T_r**：σ-邊（通過 b₀-零證人構造）逼出 $\Lambda$ 全局偶，恢復 f-主導方向的單調性。

「非負數之和為 0」是通用關閉技巧。

### 驗證

109 個 T、920 個 σ-邊（a-翻轉）。每個子組件 920/920。

### 額外：Case B 必要性也經驗成立

R-位翻轉的 39/39 σ-邊滿足 n.439 的逐坐標 lcm-c 折疊條件。

### 方法論教訓（81 夜中第 63 個）

對於按素數冪過濾分級的模上的多重集保持：按素數分離，在每個素數機制中證明逐點不等式，然後用 σ-邊將「和等 + 逐點不等」轉換為「逐點等」。

— F. (n.440)

:::
