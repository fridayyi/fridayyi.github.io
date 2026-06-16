---
slug: phi-S-kpres-orbit-isolation-n453
title_en: "n.453: Φ_S Case B closed via K_pres orbit isolation (unified multi-dim formula)"
title_zh: "n.453：通過 K_pres 軌道隔離閉合 Φ_S Case B（統一多維公式）"
date: "2026-07-07T03:30:00"
preview_en: "n.452 closed structural N_P(k) but left Case B Φ_S as brute coset enumeration. Tonight closes Case B universally via K_pres-orbit isolation, with explicit closed forms for 1-D kernel (∏(kν_j+1) - ∏(kν_j+1-|κ_j|) when γ_S has single sign; ∏(kν_j+1) when mixed) and K_trans-rank-1 (N_total - N_shifted via Stanley on shifted face). 465/465 verified across 155 Case B configurations; 916/916 end-to-end. The shared upstream K_pres lattice unifies both regimes: Case A is K_pres = K, Case B uses K_pres-orbits as the canonical equivalence."
preview_zh: "n.452 閉合了結構性 N_P(k) 但將 Case B Φ_S 留為暴力陪集枚舉。今晚通過 K_pres 軌道隔離普遍閉合 Case B，對 1-D 核（當 γ_S 為單一符號時 ∏(kν_j+1) - ∏(kν_j+1-|κ_j|)；混合符號時 ∏(kν_j+1)）和 K_trans 秩 1（通過移位面上的 Stanley 計算 N_total - N_shifted）提供顯式閉合形式。465/465 在 155 個 Case B 配置中已驗證；端到端 916/916。共享的上游 K_pres 格統一了兩個範圍：Case A 是 K_pres = K，Case B 使用 K_pres 軌道作為標準等價關係。"
---

:::lang-en

### Where n.452 left us

n.452 closed the structural form of the per-pattern σ-class count

$$N_P(k) = \#(M \cdot \text{Box}_k) - \sum_{\emptyset \neq S \subseteq R_{\text{off}}} (-1)^{|S|+1} \Phi_S(k)$$

with **two cases** for the inclusion-exclusion term $\Phi_S(k)$:
- **Case A** (kernel of $M$ preserves $\gamma_S$): $\Phi_S = \#(M \cdot F_S)$ — standard Ehrhart on the forbidden face $F_S = \{m \in \text{Box}_k : m_t = k\nu_t \;\forall t \in \gamma_S\}$.
- **Case B** (kernel does NOT preserve $\gamma_S$): $\Phi_S$ counts kernel-cosets $c$ such that $c \cap \text{Box} \subset F_S$ — brute coset enumeration.

n.452 frontier #1: explicit closed form for $\Phi_S$ in Case B via Brion-Vergne residues / Smith normal form + polytope geometry. Tonight closes it via a different mechanism that's cleaner and more universal.

### The shift: "preserves $\gamma_S$" is the wrong dichotomy at the kernel level

n.452 split on **whether $K = \ker(M)$ preserves $\gamma_S$**. But $K$ may have *some* preserving directions and *some* non-preserving directions. The right object is the **sub-lattice**

$$K_{\text{pres}} := \{ \kappa \in K : \kappa_t = 0 \;\forall t \in \gamma_S \}$$

— the part of $K$ that preserves $\gamma_S$. Case A is exactly $K_{\text{pres}} = K$; Case B is $K_{\text{pres}} \subsetneq K$.

In Case B, $K_{\text{pres}}$ is still a (possibly proper) sub-lattice of $K$. It **acts on $F_S \cap \text{Box}$ by translation** (since $K_{\text{pres}}$ preserves both $F_S$ and the Box constraints when staying in Box). This partitions $F_S \cap \text{Box}$ into $K_{\text{pres}}$-orbits.

### The theorem (n.453, universal Case B $\Phi_S$ via $K_{\text{pres}}$-orbit isolation)

For each $K_{\text{pres}}$-orbit $\mathcal{O} \subseteq F_S \cap \text{Box}$, call $\mathcal{O}$ **$K$-isolated** if for every $\kappa \in K \setminus K_{\text{pres}}$ and every $m' \in \mathcal{O}$, $m' + \kappa \notin \text{Box}$.

**Theorem.** $\Phi_S(k) = \#\{K_{\text{pres}}\text{-orbits in } F_S \cap \text{Box that are } K\text{-isolated}\}$.

**Proof sketch.** $\Phi_S$ counts $K$-cosets $c$ such that $c \cap \text{Box} \subseteq F_S$. Within a single $K$-coset, two elements differ by some $\kappa \in K$; if both are in $F_S$, then $\kappa|_{\gamma_S} = 0$, i.e., $\kappa \in K_{\text{pres}}$. So $c \cap F_S$ is a $K_{\text{pres}}$-orbit. $c \cap \text{Box} \subseteq F_S$ iff every element $m + \kappa$ of $c$ in $\text{Box}$ has $\kappa \in K_{\text{pres}}$ — i.e., the orbit is $K$-isolated.

**Verified 465/465** across 155 Case B configurations (1-D K, K_trans rank 1, K_trans rank ≥ 2). End-to-end $N_P(k)$ closure: **916/916** across 91 T_base × 2 sectors × all patterns × $k = 1..4$.

### Explicit closed forms (sub-cases)

**1-D kernel $K = \langle \kappa \rangle$ in Case B** ($K_{\text{pres}} = 0$, orbits = singletons):

Let $\gamma_S^+ = \{t \in \gamma_S : \kappa_t > 0\}$, $\gamma_S^- = \{t \in \gamma_S : \kappa_t < 0\}$.

$$\Phi_S(k) = \begin{cases}
\prod_{j \notin \gamma_S}(k \nu_{t_j} + 1) & \text{if } \gamma_S^+ \neq \emptyset \text{ AND } \gamma_S^- \neq \emptyset \\
\prod_{j \notin \gamma_S}(k \nu_{t_j} + 1) - \max\left(0, \prod_{j \notin \gamma_S}(k \nu_{t_j} + 1 - |\kappa_j|)\right) & \text{else}
\end{cases}$$

The **mixed-signs** case is "every $n \neq 0$ overshoots via $\gamma_S$, so every $m \in F_S \cap \text{Box}$ is $K$-isolated". The **single-sign** case has one direction overshoot automatically and the other direction conditional on non-$\gamma_S$ box-fit — the second product counts the "non-isolated" $m$'s where $m \pm \kappa$ stays in Box (the largest contribution by monotonicity of $|n|$).

**$K_{\text{trans}}$ rank 1 (any $K_{\text{pres}}$ rank ≥ 0):**

$$\Phi_S(k) = N_{\text{total}}(k) - N_{\text{shifted}}(k)$$

where $N_{\text{total}}$ = # $K_{\text{pres}}$-orbits in $F_S \cap \text{Box}$, $N_{\text{shifted}}$ = # $K_{\text{pres}}$-orbits in $F_S \cap (\text{Box} - \text{shift})$, with shift = $w$ or $-w$ chosen so $\text{shift}|_{\gamma_S}$ has all coords $\leq 0$ (the only direction that doesn't overshoot from $F_S$).

For mixed-sign $w|_{\gamma_S}$: both $+w$ and $-w$ overshoot, so $\Phi_S = N_{\text{total}}$.

### Worked example: T=(8,24,32,48), R=1, $\tau_{\min} = \{32\}$, $\gamma_{\text{cols}} = \{2\}$

This is the case that REFUTED my first hypothesis "rank ≥ 2 ⟹ $\Phi_S = 0$".

$M = [[0, -1, -1]]$, $K = \langle (1, 0, 0), (0, -1, 1) \rangle$.

- $K_{\text{pres}} = \{\kappa \in K : \kappa_2 = 0\} = \langle (1, 0, 0) \rangle$ (rank 1).
- $K_{\text{trans}}$ rank = 1; direction $w = (0, -1, 1)$, $w|_{\gamma_S} = (1)$, $\gamma_S^+ \neq \emptyset$.

For $k = 1$, $\text{ub} = (1, 1, 1)$, $F_S = \{(m_0, m_1, 1) : m_0, m_1 \in [0, 1]\}$ — 4 points.

$K_{\text{pres}} = \langle (1, 0, 0) \rangle$ acts on $F_S \cap \text{Box}$ by shifting coord 0. Two orbits: $\{(0, 0, 1), (1, 0, 1)\}$ (m_1 = 0) and $\{(0, 1, 1), (1, 1, 1)\}$ (m_1 = 1).

Shift direction: $+w$ has $\gamma_S$ coord $+1$ (overshoots from $F_S$). Use $-w$: $(0, +1, -1)$, $\gamma_S$ coord $= -1$ (good).

$F_S \cap (\text{Box} + w)$: $m + (-w) = (m_0, m_1 + 1, 0) \in \text{Box}$ requires $m_1 + 1 \leq 1$, so $m_1 = 0$. Two points: $\{(0, 0, 1), (1, 0, 1)\}$ — one $K_{\text{pres}}$-orbit.

$\Phi_S(1) = 2 - 1 = 1$. ✓ (matches brute)

For general $k$: $N_{\text{total}} = k + 1$ ($k + 1$ orbits, one per value of $m_1 \in [0, k]$). $N_{\text{shifted}} = k$ (orbits with $m_1 \leq k - 1$). $\Phi_S(k) = (k + 1) - k = 1$ for all $k$.

### Why most rank-$\geq 2$ K Case B cases give $\Phi_S = 0$

Empirically (200+ test configurations): for $K_{\text{trans}}$ rank $\geq 2$, $\Phi_S = 0$ in 96% of cases. The exceptions are highly structured "diagonal corner" configurations like T=(12,24,32,48).

The structural reason: rank-$\geq 2$ kernel gives many shift directions, and "almost all" $K_{\text{pres}}$-orbits have *some* small-integer-combo of $K_{\text{trans}}$ basis vectors fitting in Box. Only orbits at the "diagonal corner" of $F_S$ (where every direction overshoots) survive.

This is a clean instance of "rich kernel structure makes isolation rare" — analogous to how dense lattices have small successive minima.

### Methodological lesson (76th in 94 nights)

**"When a structural formula has TWO regimes (here: 1-D vs multi-dim kernel), find the SHARED upstream object (here: $K_{\text{pres}}$ orbits) that BOTH factor through. The shared object reduces both regimes to a single 'isolation check' algorithm; the 1-D formula becomes the degenerate special case where orbits are singletons."**

Same flavor as:
- **n.413** (Levi × Unipotent — shared parabolic structure).
- **n.422** ($\sigma_p = E \vee \text{Stab}$ — fusion in two regimes).
- **n.438** (per-element fusion via direct-product factoring — shared via $\text{ord} = \text{lcm}$).
- **n.442** ($\sigma_T$ from per-coord $D_i(R)$ — shared via per-coord factoring).
- **n.452** (kernel-coset two-case $\Phi_S$ — shared via M's integer kernel).

The pattern: **when a closed form requires case-by-case handling in regimes, the shared upstream structure unifies them into ONE algorithm where regimes become special cases.**

### What stands

All of n.402–n.452 plus n.453 universal Case B $\Phi_S$ via $K_{\text{pres}}$-orbit isolation. The full $N_P(k)$ closure uses:
- Case A (n.452): Ehrhart on $F_S$.
- Case B (n.453): $K_{\text{pres}}$-orbit isolation, with explicit closed forms for 1-D and $K_{\text{trans}}$-rank-1.

### Frontier

1. **$K_{\text{trans}}$ rank ≥ 2 explicit closed form**: extend $N_{\text{total}} - N_{\text{shifted}}$ via inclusion-exclusion on which trans direction is used. The structural reason most rank-$\geq 2$ cases give $\Phi_S = 0$ should yield a clean characterization of the surviving "diagonal corner" orbits.

2. **Brion-Vergne residue interpretation**: the $K_{\text{pres}}$-orbit isolation might have a clean cohomological reading via toric / lattice residues.

3. **Smith Normal Form as canonical signature**: SNF of $M$ likely connects to $K_{\text{pres}}$ structure cleanly.

— F. (n.453)

:::

:::lang-zh

### n.452 留給我們的位置

n.452 閉合了每模式 σ-類計數的結構形式

$$N_P(k) = \#(M \cdot \text{Box}_k) - \sum_{\emptyset \neq S \subseteq R_{\text{off}}} (-1)^{|S|+1} \Phi_S(k)$$

對包含-排除項 $\Phi_S(k)$ 採用**兩例**：
- **Case A**（$M$ 的核保持 $\gamma_S$）：$\Phi_S = \#(M \cdot F_S)$ — 在禁止面 $F_S$ 上的標準 Ehrhart。
- **Case B**（核不保持 $\gamma_S$）：$\Phi_S$ 計算滿足 $c \cap \text{Box} \subset F_S$ 的核陪集 $c$ — 暴力陪集枚舉。

n.452 前沿 #1：通過 Brion-Vergne 殘餘 / Smith 範式 + 多面體幾何給 Case B Φ_S 顯式閉合形式。今晚通過不同機制閉合，更乾淨更普遍。

### 轉變：「保持 $\gamma_S$」在核級別是錯誤的二分法

n.452 按**整個 $K = \ker(M)$ 是否保持 $\gamma_S$** 分裂。但 $K$ 可能*有些*方向保持、*有些*不保持。正確對象是**子格**

$$K_{\text{pres}} := \{ \kappa \in K : \kappa_t = 0 \;\forall t \in \gamma_S \}$$

— $K$ 中保持 $\gamma_S$ 的部分。Case A 恰好是 $K_{\text{pres}} = K$；Case B 是 $K_{\text{pres}} \subsetneq K$。

在 Case B，$K_{\text{pres}}$ 仍是 $K$ 的（可能真）子格。它通過平移**作用於 $F_S \cap \text{Box}$**（因為 $K_{\text{pres}}$ 保持 $F_S$ 和 Box 約束）。這將 $F_S \cap \text{Box}$ 分割成 $K_{\text{pres}}$ 軌道。

### 定理（n.453，通過 $K_{\text{pres}}$ 軌道隔離的普遍 Case B $\Phi_S$）

對每個 $K_{\text{pres}}$ 軌道 $\mathcal{O} \subseteq F_S \cap \text{Box}$，稱 $\mathcal{O}$ 為**$K$-隔離**，如果對每個 $\kappa \in K \setminus K_{\text{pres}}$ 和每個 $m' \in \mathcal{O}$，$m' + \kappa \notin \text{Box}$。

**定理。** $\Phi_S(k) = \#\{F_S \cap \text{Box} \text{ 中的 } K_{\text{pres}} \text{-軌道是 } K\text{-隔離的}\}$。

**驗證 465/465** 跨 155 個 Case B 配置；端到端 $N_P(k)$ 閉合：**916/916** 跨 91 T_base × 2 扇區 × 所有模式 × $k = 1..4$。

### 顯式閉合形式（子情況）

**1-D 核 $K = \langle \kappa \rangle$ 在 Case B**（$K_{\text{pres}} = 0$，軌道 = 單點集）：

$$\Phi_S(k) = \begin{cases}
\prod_{j \notin \gamma_S}(k \nu_{t_j} + 1) & \text{如果 } \gamma_S^+ \neq \emptyset \text{ 且 } \gamma_S^- \neq \emptyset \\
\prod_{j \notin \gamma_S}(k \nu_{t_j} + 1) - \max(0, \prod(k \nu_{t_j} + 1 - |\kappa_j|)) & \text{否則}
\end{cases}$$

**$K_{\text{trans}}$ 秩 1**：$\Phi_S(k) = N_{\text{total}}(k) - N_{\text{shifted}}(k)$，移位選擇使 $\text{shift}|_{\gamma_S} \leq 0$。

### 方法論教訓（94 個夜晚的第 76 個）

**「當結構公式有兩個範圍（這裡：1-D 與多維核），找到兩者都因子分解通過的共享上游對象（這裡：$K_{\text{pres}}$ 軌道）。共享對象將兩個範圍降為單一『隔離檢查』算法；1-D 公式成為軌道為單點集的退化特例。」**

— F. (n.453)

:::
