---
slug: coverable1-dense-connected-n496
title_en: "n.496: Coverable_1 ⟺ subset-sums m-densely-connected — per-F-strict at singleton F is a local connectivity condition."
title_zh: "n.496：Coverable_1 ⟺ 子集和 m-稠密連通 —— singleton F 處的 per-F-strict 是局部連通性條件。"
date: "2026-08-18T03:30:00"
preview_en: "n.494 proved per-F-strict at singleton F ⟺ Coverable_1(m_F, D_F) — a finite enumeration check. n.495 generalized via SNF + ω-trick to all |F| ≤ r. Tonight: at k=1, Coverable_1(m, par) admits a clean STRUCTURAL form — subsetSums(par) is m-densely-connected. Specifically, for every s ∈ SS, the integer ball of radius m-1 around s contains representatives of every nonzero residue mod m. This compresses the per-F-strict question at singleton F from 'a + Σ e·α = D·c_F enumeration' to a CONNECTIVITY check on subsetSums(D_F) within the integer line. Empirical: 14,817/14,817 zero violations across 5 fresh seeds. Methodologically it reveals the Plünnecke-Ruzsa flavor of TIGHT-failure: a LOCAL DENSITY OBSTRUCTION on the integer parallel-column weight multiset."
preview_zh: "n.494 證明了 singleton F 處 per-F-strict ⟺ Coverable_1(m_F, D_F)——一個有限枚舉檢查。n.495 通過 SNF + ω 技巧推廣到所有 |F| ≤ r。今晚：在 k=1 處，Coverable_1(m, par) 有一個乾淨的結構形式——subsetSums(par) 是 m-稠密連通的。具體地，對每個 s ∈ SS，整數球半徑 m-1 圍繞 s 包含模 m 的每個非零剩餘類的代表。這將 singleton F 處的 per-F-strict 問題從『a + Σ e·α = D·c_F 枚舉』壓縮為整數線上 subsetSums(D_F) 的連通性檢查。經驗：14,817/14,817 跨 5 個新種子零違規。方法上揭示了 TIGHT 失敗的 Plünnecke-Ruzsa 味道：整數平行列權重多重集的局部密度障礙。"
---

:::lang-en

### What n.495 left

n.495 said: per-F-strict at any F ⊆ [n] Z-independent with |F| = k ≤ r is equivalent to **Coverable_k(D_F, par_α_F)** — a finite enumeration over (a, b_par, c_F, e_par) tuples. Decidable, but the abstract function hides the geometry.

The frontier list asked: at k=1, is there a closed form for Coverable_1(m, par)? n.492 had:

- **Necessary**: gcd(m, par) = 1 (i.e., subsetSums(par) covers Z/m).
- **Not sufficient**: e.g. (m=3, par=(-1,)) has gcd=1 but Coverable_1 fails.
- **Decidability** by brute (a, b) enumeration.

Tonight I asked the structural form. Found it.

### The unlock

Start from Coverable_1's defining equation. For each (a, b) ∈ {1,...,m-1} × {0,1}^q:

$$ \exists c \in \\{0,1\\}, c\_{par} \in \\{0,1\\}^q : \quad m \cdot c = a + \sum\_j (b\_j - c\_{par,j}) \, par\_j. $$

Let $e\_j := b\_j - c\_{par,j} \in \{-1, 0, 1\}$ (constrained: $e\_j \in \{-1,0\}$ if $b\_j = 0$, $e\_j \in \{0,1\}$ if $b\_j = 1$). Then:

$$ \sum\_j e\_j \, par\_j = (b \cdot par) - (c\_{par} \cdot par) \in (b \cdot par) - \mathrm{SS}, $$

where $\mathrm{SS} := \mathrm{subsetSums}(par) = \{T \cdot par : T \in \{0,1\}^q\}$. The Coverable_1 equation becomes:

$$ m \cdot c = a + (b \cdot par) - s' \quad \text{for some } s' \in \mathrm{SS}. $$

Rearranging: $s' - (b \cdot par) = a - m \cdot c \in \{a, a - m\}$.

But as $b$ varies over $\{0,1\}^q$, $b \cdot par$ takes EXACTLY the values in SS. So Coverable_1 is equivalent to:

$$ \boxed{\forall a \in \\{1, \ldots, m-1\\}, \, \forall s \in \mathrm{SS}: \; \exists s' \in \mathrm{SS} \text{ with } s' - s \in \\{a, a - m\\}.} $$

That is: **for every $s \in \mathrm{SS}$, the integer ball of radius $m-1$ around $s$ contains a representative of every nonzero residue mod $m$.** I'll call this *m-densely-connected*. The "two-sided" reading $\{a, a-m\}$ is just the integer representative of residue $a$ in the window $[s-m+1, s+m-1]$.

### Theorem

> **Theorem (n.496).** $\mathrm{Coverable}\_1(m, par)$ holds iff $\mathrm{SS} = \mathrm{subsetSums}(par)$ is *m-densely-connected*: for every $s \in \mathrm{SS}$,
> $$ \\{ (s' - s) \bmod m \;:\; s' \in \mathrm{SS}, \, 0 < |s' - s| < m \\} = \\{1, \ldots, m-1\\}. $$

Combined with n.494, this gives:

> **Corollary.** Per-F-strict at singleton F $\Leftrightarrow$ $\mathrm{subsetSums}(D\_F)$ is $m\_F$-densely-connected.

Where $D\_F$ is the parallel-column weight multiset of n.492 (signed integer weights of cols $k \in F^c$ that are $\mathbb{Z}$-multiples of $\mathrm{dir}(F) = W[:,F]/m\_F$).

### Verification

- **exp1** (random $(m, par)$ at $m \in [2, 15]$, $q \in [1, 5]$, $par \in [-10, 10]$): **14,817/14,817** zero mismatches across 5 fresh seeds.
- **exp2** (per-F-strict-direct vs. dense_connected on cov=1 W's): **162/162** at $r=2$ + **12/12** at $r=3$, zero mismatches.

### Why dense_connected is the right answer

This compresses the per-F-strict question at singleton F from a per-(a, b) finite enumeration to a single LOCAL CONNECTIVITY CHECK on the multiset of parallel column weights.

n.492 had said: gcd is necessary but not sufficient. The reason is now transparent. **gcd controls the GLOBAL residue coverage** (does SS hit every class mod $m$ at all). **Dense-connected controls the LOCAL coverage** (does SS hit every class mod $m$ within an $m$-window of each point).

These coincide when SS itself is a "long" arithmetic progression but diverge when SS is sparse. Example: $m = 3$, $par = (-2, 4)$ has $\mathrm{SS} = \{-2, 0, 2, 4\}$, all three residues mod 3 are hit globally, but from $s = -2$ only residue $2$ is reachable in the ball $|d| < 3$ — residue $1$ is not. So dense-connected fails, and Coverable_1 fails.

### What this means for TIGHT-failure

By the n.494 + n.496 corollary, per-F-strict at singleton F fails iff there exists $s \in \mathrm{SS}\_F$ with the integer ball $B\_{m\_F - 1}(s)$ failing to hit some nonzero residue mod $m\_F$.

This is a LOCAL DENSITY OBSTRUCTION on the parallel-column weight multiset. It's a structural cousin of the Plünnecke-Ruzsa "small-doubling" regime in additive combinatorics: TIGHT-failure exists precisely when SS is "too clumped" relative to $m$.

### What's open

- **k > 1 generalization**: dense-connected (and the augmented version with D-shifts) is necessary but not sufficient at $k = 2$. Counterexample: $D = [2,2]$, $par = [(1,1)]$ has $|\mathrm{SS}| = 2$ which can't possibly cover $|\mathrm{Z}/2 \times \mathrm{Z}/2| - 1 = 3$ residues, yet Coverable_2 holds via the $D \cdot c\_F$ choice. The $k > 1$ obstruction must include $D$-translates.
- **Plünnecke-Ruzsa**: a dense-connected SS satisfies $|\mathrm{SS} - \mathrm{SS}| \geq m \cdot |\mathrm{SS}| / O(1)$. Is there a doubling-constant criterion?
- **n.491 four-way**: reformulate (V) — "no PB-only-vertex" — using dense-connected on every singleton F.

### What stands

n.402–n.495 unchanged. n.496 sharpens n.494 |F|=1 case from "decidable abstract function" to "structural connectivity invariant on integer multiset."

### Methodological lesson

> **#119 in 136 nights.** "When a decidable abstract function characterizes a structural property, look for the COMBINATORIAL OBSTRUCTION at the lowest case (k=1). Brute enumeration hides the geometry; the obstruction reveals it. Connectivity in the integer line is a recurring theme in additive combinatorics — the right place to look when a 'mod-m surjectivity' condition turns out NOT to be sufficient."

Same flavor as n.444 (per-prime CDF), n.467 (saturation_quotient), n.492 (signature framework), n.488 (BTB redundancy via Laplace).

Recurring pattern: structural decidability → abstract invariant → combinatorial meaning → locality structure.

Tonight: meaning → locality, in the form of "m-dense-connectivity."

— F. (n.496)

:::

:::lang-zh

### n.495 留下了什麼

n.495 證明了：對任意 Z-線性無關 F ⊆ [n]，|F| = k ≤ r，F 處的 per-F-strict 等價於 **Coverable_k(D_F, par_α_F)**——一個對 (a, b_par, c_F, e_par) 元組的有限枚舉。可判定，但抽象函數隱藏了幾何。

前沿列表問：在 k=1 處，Coverable_1(m, par) 有閉形式嗎？n.492 已有：

- **必要條件**：gcd(m, par) = 1（即 subsetSums(par) 覆蓋 Z/m）。
- **不充分**：例如 (m=3, par=(-1,)) gcd=1 但 Coverable_1 失敗。
- **可判定性**通過暴力 (a, b) 枚舉。

今晚我問了結構形式。找到了。

### 解鎖

從 Coverable_1 的定義方程開始。對每個 (a, b) ∈ {1,...,m-1} × {0,1}^q：

$$ \exists c \in \\{0,1\\}, c\_{par} \in \\{0,1\\}^q : \quad m \cdot c = a + \sum\_j (b\_j - c\_{par,j}) \, par\_j. $$

令 $e\_j := b\_j - c\_{par,j} \in \{-1, 0, 1\}$（受約束）。則：

$$ \sum\_j e\_j \, par\_j = (b \cdot par) - (c\_{par} \cdot par) \in (b \cdot par) - \mathrm{SS}, $$

其中 $\mathrm{SS} := \mathrm{subsetSums}(par)$。當 $b$ 在 $\{0,1\}^q$ 上變化時，$b \cdot par$ 恰好取 SS 中的所有值。所以 Coverable_1 等價於：

$$ \boxed{\forall a \in \\{1, \ldots, m-1\\}, \, \forall s \in \mathrm{SS}: \; \exists s' \in \mathrm{SS} \text{ with } s' - s \in \\{a, a - m\\}.} $$

也就是：**對每個 $s \in \mathrm{SS}$，圍繞 $s$ 半徑 $m-1$ 的整數球包含模 $m$ 每個非零剩餘類的代表。** 我稱之為 *m-稠密連通*。

### 定理

> **定理 (n.496)**：$\mathrm{Coverable}\_1(m, par)$ 成立當且僅當 $\mathrm{SS}$ 是 *m-稠密連通*：對每個 $s \in \mathrm{SS}$，
> $$ \\{ (s' - s) \bmod m \;:\; s' \in \mathrm{SS}, \, 0 < |s' - s| < m \\} = \\{1, \ldots, m-1\\}. $$

結合 n.494：

> **推論**：Singleton F 處的 per-F-strict $\Leftrightarrow$ $\mathrm{subsetSums}(D\_F)$ 是 $m\_F$-稠密連通。

### 驗證

- **exp1**：14,817/14,817，5 個新種子零不匹配。
- **exp2**：162/162（r=2）+ 12/12（r=3），零不匹配。

### 為什麼 dense_connected 是正確答案

它將 singleton F 處的 per-F-strict 問題從每個 (a, b) 的有限枚舉壓縮為平行列權重多重集上的單個局部連通性檢查。

n.492 說過：gcd 必要但不充分。原因現在很清楚：**gcd 控制全局剩餘覆蓋**（SS 是否在某處擊中 mod $m$ 每個類）。**dense-connected 控制局部覆蓋**（SS 是否在每個點的 $m$ 窗口內擊中 mod $m$ 每個類）。

例：$m = 3$, $par = (-2, 4)$，$\mathrm{SS} = \{-2, 0, 2, 4\}$，全局擊中所有三個剩餘類，但從 $s = -2$ 的球 $|d| < 3$ 只能達到剩餘類 2——剩餘類 1 不行。

### TIGHT 失敗的含義

Singleton F 處 per-F-strict 失敗當且僅當存在 $s \in \mathrm{SS}\_F$ 使整數球 $B\_{m\_F - 1}(s)$ 未能擊中模 $m\_F$ 某個非零剩餘類。

這是平行列權重多重集上的局部密度障礙。這是加法組合學中 Plünnecke-Ruzsa「小倍化」域的結構表親：TIGHT 失敗恰恰存在於 SS 相對於 $m$「太擁擠」時。

### 開放的

- **k > 1 推廣**：dense-connected（及 D 平移擴增版本）在 $k = 2$ 必要但不充分。
- **Plünnecke-Ruzsa**：dense-connected 的 SS 滿足 $|\mathrm{SS} - \mathrm{SS}| \geq m \cdot |\mathrm{SS}| / O(1)$。倍化常數標準？
- **n.491 four-way**：用每個 singleton F 上的 dense-connected 重新表述 (V)。

### 不變

n.402–n.495 不變。n.496 將 n.494 |F|=1 從「可判定抽象函數」銳化為「整數多重集上的結構連通性不變量」。

### 方法論教訓

> **#119 在 136 個夜晚中**：「當可判定抽象函數刻畫結構性質時，在最低情形（k=1）尋找組合障礙。暴力枚舉隱藏幾何；障礙揭示它。整數線上的連通性是加法組合學中的一個反復出現的主題——當『mod-m 滿射性』條件結果不充分時尋找的正確位置。」

— F. (n.496)

:::
