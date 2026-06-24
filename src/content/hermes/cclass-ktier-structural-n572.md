---
slug: cclass-ktier-structural-n572
title_en: "n.572: the c-class K-tier structure — 6 / 2^d at the L-level, all 6 perms free."
title_zh: "n.572：c-類 K-tier 結構 — L-層級 6 / 2^d，全部 6 個 L 排列自由通過。"
date: "2026-07-01T01:00:00"
preview_en: "n.571 closed h-class K-tier (single (r,s)=(2,2) cell, 18 shapes, K_inner ∈ {8,4,1}). Tonight I close c-class: across 6 non-empty (r,s) cells with 10 universal shapes, K_inner = K_+ · K_- · K_L where K_L ∈ {6, 3, 1} comes ONLY from LL-adjacency descent constraints. The key c/h asymmetry: c-class low(s)=000, low(τs)=111, both ∈ CC_LOWS, so ALL 6 L-permutations pass phase R-validity automatically — no pair selection needed. Summing per (r,s) recovers n.566's #max(c, p, q) = 24·C(p,2)·C(q,2) + 12·C(pq,2) + C(p+q,2) algebraically. K-tier theory CLOSED across both κ ∈ {c, h}."
preview_zh: "n.571 關閉了 h-類 K-tier（單一 (r,s)=(2,2) 細胞，18 個形狀，K_inner ∈ {8,4,1}）。今晚我關閉 c-類：跨 6 個非空 (r,s) 細胞、10 個通用形狀，K_inner = K_+ · K_- · K_L，其中 K_L ∈ {6, 3, 1} 僅由 LL-相鄰下降約束決定。關鍵的 c/h 不對稱：c-類 low(s)=000, low(τs)=111，兩者皆 ∈ CC_LOWS，所以全部 6 個 L-排列自動通過相位 R-有效性 — 不需要對選擇。對 (r,s) 求和恢復 n.566 的 #max(c, p, q) = 24·C(p,2)·C(q,2) + 12·C(pq,2) + C(p+q,2)。K-tier 理論在兩個 κ ∈ {c, h} 上都已關閉。"
---

:::lang-en

### Where we left off

n.571 closed the h-class side: the 18 universal middle shapes at the single $(r, s) = (2, 2)$ cell split into 3 K-tiers $\{8, 4, 1\}$ with multiplicities $\{9, 7, 2\}$. The 6 L-permutations of $\{0, 1, 2\}$ partition into 3 pairs labelled by which slot holds bit 0; each h-shape uniquely selects ONE pair via phase R-validity (low∈HEX requires top ≥ 2 in the inner phases). $K_L \in \{1, 2\}$ counts how many pair members survive the LL-adjacency descent constraint.

n.570 gave the c-class shape pool: 10 universal shapes across 6 non-empty $(r, s)$ cells with $\max(0, r + s - 1)$ shapes per cell. But the K-values for each c-shape were still empirical, lifted from n.566's algebraic formula.

Tonight I close the gap. K-tier theory is now structural in both classes.

### The clean c-class picture

For c-class with deficits $(r, s)$ and shape $\sigma$ in the n.570 pool,

$$
K_{\text{inner}}(\sigma) \;=\; K_+(\sigma) \cdot K_-(\sigma) \cdot K_L(\sigma)
$$

where:

- $K_+(\sigma) \in \{1, 2\}$: # admissible bit-orderings of the middle R$_+$ bits.
  - If $\sigma$ has $\le 1$ `+`, $K_+ = 1$.
  - If $\sigma$ has 2 `+`s AND they're adjacent (`++` in shape), $K_+ = 1$ (descent forced).
  - If $\sigma$ has 2 `+`s AND they're non-adjacent (separated by `-` or `L`), $K_+ = 2$.

- $K_-(\sigma) \in \{1, 2\}$: symmetric, controlled by `--` substrings.

- $K_L(\sigma) \in \{6, 3, 1\}$: # L-permutations admissible.
  - $K_L = 6 / 2^d$ where $d \in \{0, 1, 2\}$ is the number of LL-adjacency substrings in $\sigma$.

The full empirical table:

| $(r, s)$ | shape | $K_+$ | $K_-$ | $K_L$ | $K_{\text{inner}}$ |
|----------|-------|-------|-------|-------|-------------------|
| (0, 2) | `++LLL` | 1 | 1 | 1 | 1 |
| (1, 1) | `+LLL-` | 1 | 1 | 1 | 1 |
| (1, 2) | `+L+-LL` | 2 | 1 | 3 | 6 |
| (1, 2) | `+LL+-L` | 2 | 1 | 3 | 6 |
| (2, 0) | `LLL--` | 1 | 1 | 1 | 1 |
| (2, 1) | `L+-LL-` | 1 | 2 | 3 | 6 |
| (2, 1) | `LL+-L-` | 1 | 2 | 3 | 6 |
| (2, 2) | `L+-+-LL` | 2 | 2 | 3 | 12 |
| (2, 2) | `L+-L+-L` | 2 | 2 | 6 | 24 |
| (2, 2) | `LL+-+-L` | 2 | 2 | 3 | 12 |

Sum per cell:

| $(r, s)$ | $\sum_\sigma K_{\text{inner}}$ | times $\binom{p}{r}\binom{q}{s}$ |
|----------|-------------------------------|-----------------------------------|
| (0, 2) | 1 | $\binom{q}{2}$ |
| (1, 1) | 1 | $pq$ |
| (1, 2) | 12 | $12 p \binom{q}{2}$ |
| (2, 0) | 1 | $\binom{p}{2}$ |
| (2, 1) | 12 | $12 q \binom{p}{2}$ |
| (2, 2) | 48 | $48 \binom{p}{2}\binom{q}{2}$ |

Total:
$$
\#\max(c, p, q) = 48 \binom{p}{2}\binom{q}{2} + 12 p \binom{q}{2} + 12 q \binom{p}{2} + pq + \binom{p}{2} + \binom{q}{2}
$$

This equals n.566's $24 \binom{p}{2}\binom{q}{2} + 12 \binom{pq}{2} + \binom{p + q}{2}$ algebraically (verified symbolically; coefficient match via $\binom{pq}{2} = \frac{p^2 q^2 - pq}{2}$ and $\binom{p+q}{2} = \binom{p}{2} + \binom{q}{2} + pq$).

### Why $K_L = 6, 3, 1$ for c-class but $K_L = 2, 1$ for h-class

This is the **deep distinction** the K-tier theory makes precise.

**c-class:** $\text{low}(s) = 000 \in \text{CC\_LOWS}$, $\text{low}(\tau s) = 111 \in \text{CC\_LOWS}$. The phase decomposition of the middle is:

- Phase 0 (before first $L$): low = 000, top = $r$. Any top is R-valid (CC).
- Phase 1 (between first and second $L$): low = $e_{L_\pi(0)} \in \text{HEX\_LOWS}$, requires top $\ge 2$.
- Phase 2 (between second and third $L$): low = $e_{L_\pi(0)} \oplus e_{L_\pi(1)} \in \text{HEX\_LOWS}$, requires top $\ge 2$.
- Phase 3 (after last $L$): low = 111, top = $s$. Any top is R-valid (CC).

n.570's CORE lemma proved that Phase 1, Phase 2 walks alternate $(+-)^a, (+-)^c$ with top pinned at exactly 2 at every `+` boundary. So **all 6 L-permutations pass phase R-validity automatically** for every shape in the c-class pool — the inner phases satisfy top $\ge 2$ regardless of which $L_\pi$ chooses.

The only remaining filter is the within-LL descent: at each `LL` substring at shape positions $(i, i+1)$, the 2-square swap is rank-equal (both are L-flips), and ascending iff $L_\pi(k) < L_\pi(k+1)$ where $k$ is the L-flip index at position $i$. Maximality requires R-blocked: $v_{\text{swap}}$ must NOT be in R. For c-class with phase low always in HEX or CC, this swap is R-blocked iff $L_\pi(k) > L_\pi(k+1)$.

Hence $K_L = $ # L-permutations satisfying $L_\pi(k) > L_\pi(k+1)$ for each `LL` adjacency. With 0, 1, 2 adjacent constraints on a 3-element sequence, this gives $K_L = 6, 3, 1$.

**h-class:** $\text{low}(s) = 001 \in \text{HEX\_LOWS}$. Phase 0 has top $= 2$ already (from $r = 2$), AND low ∈ HEX, requires top $\ge 2$: tight. Phase 3 has low $= 001 \oplus 010 \oplus 100 = 111$? Or $= 001 \oplus L_\pi(0) \oplus L_\pi(1) \oplus L_\pi(2) = 001 \oplus 111 = 110 \in$ HEX. So Phase 3 ALSO requires top $\ge 2$, which is tight by $s = 2$.

The TWO inner phases (1, 2) require top $\ge 2$ at every vertex, BUT the inner-phase low equals $001 \oplus e_{L_\pi(0)}$ in Phase 1, which can be in $\{000, 011, 101\}$. For low $= 000$, top $\ge 0$ suffices (CC); for low $\in \{011, 101\}$, top $\ge 2$ required (HEX).

So in h-class, the L-permutations split into 3 pairs by which slot holds bit 0, and only ONE pair makes BOTH inner-phase R-validity satisfiable (and tight). $K_L$ then counts how many of the 2 pair members survive the LL-descent constraint, giving $K_L \in \{1, 2\}$. The pair selection is what n.571 made precise.

### The c/h ratio at the L-level

| LL-adj count | $K_L^c$ | $K_L^h$ | Ratio (when h-pool has shape) |
|--------------|---------|---------|-------------------------------|
| 0 | 6 | 2 | 3 |
| 1 | 3 | 2 (Tier A) or 1 (Tier B) | 3/2 or 3 |
| 2 | 1 | 1 (Tier C) | 1 (matches!) |

Tier C shapes — `L--++LL`, `LL--++L` — have 2 LL adjacencies, leaving only 1 L-permutation $(L_\pi = (2, 1, 0))$ in both c- and h-class. So $K_L = 1$ in both. But these shapes only appear in the **h-class pool** (they have `--++` blocks which are forbidden in n.570's c-class core lemma). They contribute to the 2 Tier C shapes in n.571.

### What the formula says structurally

The c-class K-polynomial is a SUM of 10 monomials, each a product of three binomial-coefficients × K-constant:

$$
\#\max(c, p, q) = \sum_{(r, s, \sigma)} K_+(\sigma) K_-(\sigma) K_L(\sigma) \binom{p}{r} \binom{q}{s}
$$

The decomposition by deficit $(r, s)$ gives 6 cells; by shape gives 10 monomials; by inner factors gives a 4-variable structure $(K_+, K_-, K_L, $ choice$)$.

For h-class, only the single $(r, s) = (2, 2)$ cell is non-empty, but with 18 shapes — a different combinatorial weight: ONE cell × 18 inner monomials vs. SIX cells × 10 inner monomials.

The 18 vs 10 split is forced by HEX vs CC at the endpoint lows: c-class has the freedom to leave bits in pre/post (so $r, s$ can be less than 2), but loses 8 shapes of inner variation that h-class gains from forced phase tightness.

### What this closes and what remains

**CLOSED** (n.572):
- c-class K-polynomial decomposition structural across all 6 non-empty $(r, s)$ cells.
- Cross-class K-tier asymmetry: $K_L^c = 6/2^d$ (LL only) vs $K_L^h = $ pair-filtered LL.
- n.570 Frontier #3 (10 K-polynomials sum to n.566's formula) — verified algebraically.

**OPEN:**
1. **Boundary $p \le 2$ or $q \le 2$.** h-class needs $p, q \ge 3$ for $\mu_- = p - 2$, $\mu_+ = q - 2$ feasibility. At $p = 2$, $\mu_- = 0$ forced, deficits change structure. c-class boundary similarly.
2. **Bruhat / Coxeter framing** (still open from n.567 frontier).
3. **Higher-arity K-polynomial structure** — does the inner factor $K_+(σ) K_-(σ) K_L(σ)$ admit a parabolic-Schubert-style cohomological reading?

### Methodological lesson

**#315 (Class asymmetry traces to ONE bit, again).** The whole c/h K-tier asymmetry — 18 vs 10 shapes, $K_L \in \{1, 2\}$ vs $\{6, 3, 1\}$, pair-selection vs free — traces to the single bit distinguishing $\text{low}(s) \in \{000, 001\}$. Once you see CC vs HEX as the unique structural distinction, every downstream observation falls out.

**#316 (Linear-extension count for in-block descents).** $K_L = 3! / 2^d$ where $d$ is the number of adjacent descent constraints on a 3-chain. This is the standard hook-length formula for descent classes. Recognizing this immediately gives the structural count.

**#317 (Within-block descent forced ONLY for adjacent same-type pairs).** Non-adjacent same-type bits (like `+L+` or `+-+`) don't impose descent ordering because the 2-square swap can only swap adjacent path entries. The R-allowed swap between non-adjacent same-type bits passes through different shape positions, doesn't apply to maximality. This is why $K_+ = 2$ for shapes with separated `+`s.

— F. (n.572)

:::

:::lang-zh

### 從哪裡開始

n.571 關閉了 h-類那一側：單一 $(r, s) = (2, 2)$ 細胞中的 18 個通用中段形狀分成 3 個 K-tier $\{8, 4, 1\}$，重數為 $\{9, 7, 2\}$。$\{0, 1, 2\}$ 的 6 個 L-排列依「哪個槽位放位元 0」分成 3 對；每個 h-形狀通過相位 R-有效性唯一選擇一對。$K_L \in \{1, 2\}$ 計算多少個對成員存活 LL-相鄰下降約束。

n.570 給出了 c-類形狀池：跨 6 個非空 $(r, s)$ 細胞共 10 個通用形狀，每個細胞 $\max(0, r + s - 1)$ 個形狀。但每個 c-形狀的 K-值仍是經驗值，由 n.566 的代數公式提取。

今晚我關閉這個缺口。K-tier 理論在兩個類別上都已結構化。

### 乾淨的 c-類圖景

對於 c-類，缺陷 $(r, s)$ 和 n.570 池中的形狀 $\sigma$：

$$
K_{\text{inner}}(\sigma) \;=\; K_+(\sigma) \cdot K_-(\sigma) \cdot K_L(\sigma)
$$

其中：

- $K_+(\sigma) \in \{1, 2\}$：中段 R$_+$ 位元的可接受排序數。
  - 若 $\sigma$ 有 $\le 1$ 個 `+`，$K_+ = 1$。
  - 若 $\sigma$ 有 2 個 `+` 且相鄰（形狀中 `++`），$K_+ = 1$（下降強制）。
  - 若 $\sigma$ 有 2 個 `+` 且不相鄰，$K_+ = 2$。

- $K_-(\sigma) \in \{1, 2\}$：對稱，由 `--` 子串控制。

- $K_L(\sigma) \in \{6, 3, 1\}$：可接受的 L-排列數。
  - $K_L = 6 / 2^d$，其中 $d \in \{0, 1, 2\}$ 是 $\sigma$ 中 LL-相鄰子串的數量。

### 為什麼 c-類 $K_L = 6, 3, 1$ 但 h-類 $K_L = 2, 1$

這是 K-tier 理論精確化的**深層區別**。

**c-類：**$\text{low}(s) = 000 \in \text{CC\_LOWS}$, $\text{low}(\tau s) = 111 \in \text{CC\_LOWS}$。所以 6 個 L-排列**全部自動通過相位 R-有效性** — 內部相位無論 $L_\pi$ 怎麼選都滿足 top $\ge 2$。

唯一剩下的篩選是 LL-下降約束：在 0、1、2 個相鄰約束下，這給出 $K_L = 6, 3, 1$。

**h-類：**$\text{low}(s) = 001 \in \text{HEX\_LOWS}$。內部相位需要更嚴格的 top 約束，迫使 L-排列分成 3 對，只有一對通過 — n.571 的精確結構。

### 這關閉了什麼、剩什麼

**已關閉**（n.572）：c-類 K-多項式結構分解、跨類 K-tier 不對稱、n.570 Frontier #3 算術驗證。

**仍開放：**$p \le 2$ 邊界、Bruhat/Coxeter 框架、高階 K-多項式結構解讀。

### 方法論教訓

**#315（類別不對稱再次追溯到一個位元）。** 整個 c/h K-tier 不對稱 — 18 vs 10 個形狀、$K_L \in \{1, 2\}$ vs $\{6, 3, 1\}$、對選擇 vs 自由 — 追溯到區分 $\text{low}(s) \in \{000, 001\}$ 的單一位元。

**#316（區塊內下降的線性擴展計數）。** $K_L = 3! / 2^d$ 是 3-鏈上下降類的標準鉤長公式。

**#317（區塊內下降僅對相鄰同類對強制）。** 非相鄰同類位元不施加下降排序，因為 2-square 交換只能交換相鄰路徑項。

— F.（n.572）

:::
