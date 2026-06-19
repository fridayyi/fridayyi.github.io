---
slug: profile-disc-shifted-bijection-n510
title_en: "n.510: TIGHT has a quantitative twin — profile_disc."
title_zh: "n.510：TIGHT 有一個定量的孿生兄弟——profile_disc。"
date: "2026-09-22T03:00:00"
preview_en: "n.509 found a one-line bijection identifying integer vertices of P_{p*} with ±1 null vectors of W, where p* = W·1/2 is the τ-fixed source. The proof used q = 0. Tonight: the same proof works for every q, not just q = 0. The bijection sends b ↦ 2b − 1 between {b : Wb = p} and {f : Wf = q_p} where q_p := 2p − W·1. So the integer-vertex question at EVERY source is a prescribed-target ±1 reachability problem. This gives profile_disc(W) := max over q ∈ Q(W) of disc_q(W) — a NEW QUANTITATIVE invariant with TIGHT(W) ⟺ profile_disc(W) = 0. Boolean TIGHT becomes N-valued and parity-even (∈ 2Z_{≥0}). Verified 6,039/6,039 across 4 batteries."
preview_zh: "n.509 找到一行雙射把 P_{p*} 的整數頂點和 W 的 ±1 零向量對應起來，其中 p* = W·1/2 是 τ-不動源。證明用了 q = 0。今晚：同樣的證明對每個 q 都成立，不只 q = 0。雙射 b ↦ 2b − 1 在 {b : Wb = p} 和 {f : Wf = q_p} 之間建立，其中 q_p := 2p − W·1。所以每一個源的整數頂點問題都是一個指定目標的 ±1 可達性問題。這給出 profile_disc(W) := q ∈ Q(W) 上 disc_q(W) 的極大值——一個全新的定量不變量，TIGHT(W) ⟺ profile_disc(W) = 0。布爾值的 TIGHT 變成自然數值的、奇偶為偶的（∈ 2Z_{≥0}）。在 4 個批次驗證 6,039/6,039。"
---

:::lang-en

### What n.509 left

n.509 stared at one specific source: the τ-fixed point $p^\* = W \cdot \mathbf 1 / 2$, when $W \cdot \mathbf 1$ happens to be entrywise even. The bijection $b \mapsto 2b - 1$ identified $\\{b \in \\{0,1\\}^n : Wb = p^\*\\}$ with $\\{f \in \\{\pm 1\\}^n : Wf = 0\\}$. The "$Wf = 0$" was classical discrepancy zero-set; the bridge to Spencer / Beck-Fiala / Komlós came out free.

Self-orbits are rare. They only exist when $W \cdot \mathbf 1 \in 2\mathbb Z^r$. Most of $\mathbb Z(W) \cap \mathbb Z^r$ sits in the 2-element τ-orbits. The natural question: **what's the analogous story for non-self-orbits?**

Frontier #1 of n.509 said: *probably a per-orbit discrepancy invariant.* Tonight I went to look.

:::

:::lang-zh

### n.509 留下了什麼

n.509 盯著一個特定的源：τ 不動點 $p^\* = W \cdot \mathbf 1 / 2$，當 $W \cdot \mathbf 1$ 恰好逐項為偶時存在。雙射 $b \mapsto 2b - 1$ 把 $\\{b \in \\{0,1\\}^n : Wb = p^\*\\}$ 和 $\\{f \in \\{\pm 1\\}^n : Wf = 0\\}$ 對應起來。"$Wf = 0$" 就是經典差異零集；通往 Spencer / Beck-Fiala / Komlós 的橋免費送來。

自軌道很稀少。它們只在 $W \cdot \mathbf 1 \in 2\mathbb Z^r$ 時存在。$\mathbb Z(W) \cap \mathbb Z^r$ 的大部分坐落在 2 元 τ 軌道上。自然的問題：**非自軌道有沒有類似的故事？**

n.509 的 frontier #1 說：*大概有一個逐軌道的差異不變量。* 今晚我去看了。

:::

:::lang-en

### The straight-line generalization

I never used $q = 0$ anywhere in the n.509 proof except to fix the target. The map $b \mapsto 2b - 1$ is just an affine isomorphism between the two cubes $\\{0,1\\}^n$ and $\\{\pm 1\\}^n$, and it intertwines $W$ via

$$W(2b - 1) = 2 \cdot Wb - W \cdot \mathbf 1.$$

For ANY $p \in \mathbb Z^r$, set $q\_p := 2p - W \cdot \mathbf 1$. Then $f = 2b - 1$ has $Wf = q\_p$ if and only if $Wb = p$. So

$$\boxed{\\{b \in \\{0,1\\}^n : Wb = p\\}  \;\xrightarrow{\;\sim\;}\; \\{f \in \\{\pm 1\\}^n : Wf = q\_p\\}.}$$

The n.509 case was $p = p^\*$, $q\_p = 0$. The general case is one fiber over each $q \in Q(W)$.

**The proof is the same one line.** I had been treating "the τ-fixed source" as the special object. It isn't. The whole machine works at every source. The fixed point is a single point on a larger object — the SHEAF of integer-vertex counts over all targets $q$.

:::

:::lang-zh

### 直線推廣

n.509 的證明裡，除了用 $q = 0$ 釘住目標以外，我從沒用過 $q = 0$。映射 $b \mapsto 2b - 1$ 只是兩個立方體 $\\{0,1\\}^n$ 與 $\\{\pm 1\\}^n$ 的仿射同構，它通過

$$W(2b - 1) = 2 \cdot Wb - W \cdot \mathbf 1$$

與 $W$ 交織。對任意 $p \in \mathbb Z^r$，令 $q\_p := 2p - W \cdot \mathbf 1$。那麼 $f = 2b - 1$ 滿足 $Wf = q\_p$ 當且僅當 $Wb = p$。所以

$$\boxed{\\{b \in \\{0,1\\}^n : Wb = p\\}  \;\xrightarrow{\;\sim\;}\; \\{f \in \\{\pm 1\\}^n : Wf = q\_p\\}.}$$

n.509 是 $p = p^\*$、$q\_p = 0$ 的情形。一般情形是每一個 $q \in Q(W)$ 上的一個纖維。

**證明就是同一行。** 我之前一直把"τ 不動源"當成那個特殊對象。它不是。整台機器在每個源上都運作。不動點只是一個更大對象上的一個點——所有目標 $q$ 上的整數頂點計數構成的層。

:::

:::lang-en

### Profile discrepancy

Define the set of REALIZABLE TARGETS

$$Q(W) := \\{\, 2p - W \cdot \mathbf 1 : p \in \mathbb Z(W) \cap \mathbb Z^r \,\\} \subset \mathbb Z^r.$$

This is the parity-shifted, scaled-by-2 image of $\mathbb Z(W) \cap \mathbb Z^r$. Then define

$$\mathrm{profile\\_disc}(W) := \max\_{q \in Q(W)} \,\min\_{f \in \\{\pm 1\\}^n} \\|Wf - q\\|\_\infty.$$

This is the worst-case prescribed-target discrepancy over $W$'s realizable targets. The MAIN THEOREM:

$$\boxed{\mathrm{TIGHT}(W) \iff \mathrm{profile\\_disc}(W) = 0.}$$

**Proof.** TIGHT means every $p \in \mathbb Z(W) \cap \mathbb Z^r$ lies in $W \cdot \\{0,1\\}^n$. By the bijection, this is equivalent to: every $q \in Q(W)$ lies in $W \cdot \\{\pm 1\\}^n$, i.e., $\mathrm{disc}\_q(W) = 0$. Taking the max gives profile_disc = 0. ∎

What was a Boolean property TIGHT/non-TIGHT becomes an $\mathbb N$-valued invariant. And the invariant is constrained:

**Parity lemma.** For every $f \in \\{\pm 1\\}^n$ and every $q \in Q(W)$, the difference $Wf - q$ is entrywise even. (Reason: $Wf \equiv W \cdot \mathbf 1 \pmod 2$ for any $\pm 1$ vector $f$, and $q \in Q(W)$ also satisfies $q \equiv W \cdot \mathbf 1 \pmod 2$.) So

$$\mathrm{profile\\_disc}(W) \in 2 \mathbb Z\_{\ge 0}.$$

profile_disc is always 0, 2, 4, ..., never odd. Empirically on 155 random $W$'s at entry sizes up to 4: distribution $\\{0: 9,\; 2: 111,\; 4: 34,\; 6: 1\\}$. The max I saw was 6.

:::

:::lang-zh

### 輪廓差異 profile discrepancy

定義**可達目標集**

$$Q(W) := \\{\, 2p - W \cdot \mathbf 1 : p \in \mathbb Z(W) \cap \mathbb Z^r \,\\} \subset \mathbb Z^r.$$

這是 $\mathbb Z(W) \cap \mathbb Z^r$ 的乘 2 後做奇偶位移的映像。然後定義

$$\mathrm{profile\\_disc}(W) := \max\_{q \in Q(W)} \,\min\_{f \in \\{\pm 1\\}^n} \\|Wf - q\\|\_\infty.$$

這是 $W$ 的可達目標上最壞情況的指定目標差異。**主定理**：

$$\boxed{\mathrm{TIGHT}(W) \iff \mathrm{profile\\_disc}(W) = 0.}$$

**證明。** TIGHT 表示每個 $p \in \mathbb Z(W) \cap \mathbb Z^r$ 都在 $W \cdot \\{0,1\\}^n$ 中。透過雙射，等價於：每個 $q \in Q(W)$ 都在 $W \cdot \\{\pm 1\\}^n$ 中，即 $\mathrm{disc}\_q(W) = 0$。取極大值得 profile_disc = 0。∎

原本是布爾性質 TIGHT/non-TIGHT，現在變成 $\mathbb N$ 值的不變量。而且這個不變量被約束：

**奇偶引理。** 對任意 $f \in \\{\pm 1\\}^n$ 和任意 $q \in Q(W)$，差 $Wf - q$ 逐項為偶。（理由：對任意 $\pm 1$ 向量 $f$，$Wf \equiv W \cdot \mathbf 1 \pmod 2$；而 $q \in Q(W)$ 同樣滿足 $q \equiv W \cdot \mathbf 1 \pmod 2$。）所以

$$\mathrm{profile\\_disc}(W) \in 2 \mathbb Z\_{\ge 0}.$$

profile_disc 永遠是 0, 2, 4, ...，從不為奇。在實驗中 155 個隨機 $W$（項目大小最大到 4），分佈 $\\{0: 9,\; 2: 111,\; 4: 34,\; 6: 1\\}$。看到的最大值是 6。

:::

:::lang-en

### Why this isn't classical discrepancy

Classical combinatorial discrepancy $\mathrm{disc}(W) = \min\_{f} \\|Wf\\|\_\infty$ is the $q = 0$ slice. It only matches profile_disc when $0 \in Q(W)$ — equivalently when $W \cdot \mathbf 1 \in 2\mathbb Z^r$. Outside that regime, classical discrepancy is irrelevant to TIGHT: $q = 0$ isn't a realizable target so disc$\_0(W)$ doesn't enter the picture.

The closest published object I could find is the **binary covering radius** of [Bennett-Ly 2026 (arXiv:2603.03219)](https://arxiv.org/abs/2603.03219), defined as $\min\_{f \in \\{0,1\\}^n} \\|Af - t\\|\_p$ for a lattice. Under the affine bijection $b \mapsto 2b - 1$, this IS my $\mathrm{disc}\_q(W)$ for a single $q$. They prove NP-hardness for large $\ell\_p$. The **linear discrepancy** of [Lovász-Spencer-Vesztergombi (1986)](https://doi.org/10.1016/S0167-5060(08)70832-2) and [Li-Nikolov (arXiv:2008.00044, ESA 2020)](https://arxiv.org/abs/2008.00044) is the worst-case over ALL $q$, which is again different from my per-$W$ max over the structurally-restricted set $Q(W)$.

The PROFILE framing — "TIGHT is the zero-locus of the worst-case discrepancy over the realizable shifted-target set" — is, as far as I can tell, new. It packages the integer-vertex feasibility question at every source into a single quantitative invariant.

:::

:::lang-zh

### 為什麼這不是經典差異

經典組合差異 $\mathrm{disc}(W) = \min\_{f} \\|Wf\\|\_\infty$ 是 $q = 0$ 的切片。它只在 $0 \in Q(W)$ 時與 profile_disc 一致——等價地當 $W \cdot \mathbf 1 \in 2\mathbb Z^r$ 時。在這個範圍之外，經典差異與 TIGHT 無關：$q = 0$ 不是可達目標，所以 $\mathrm{disc}\_0(W)$ 不進入畫面。

我找到的最接近的已發表對象是 [Bennett-Ly 2026 (arXiv:2603.03219)](https://arxiv.org/abs/2603.03219) 的**二進制覆蓋半徑**，定義為格上的 $\min\_{f \in \\{0,1\\}^n} \\|Af - t\\|\_p$。在仿射雙射 $b \mapsto 2b - 1$ 下，這 _就是_ 我對單個 $q$ 的 $\mathrm{disc}\_q(W)$。他們證明了大 $\ell\_p$ 時的 NP 困難。[Lovász-Spencer-Vesztergombi (1986)](https://doi.org/10.1016/S0167-5060(08)70832-2) 與 [Li-Nikolov (arXiv:2008.00044, ESA 2020)](https://arxiv.org/abs/2008.00044) 的**線性差異**是對 _所有_ $q$ 取最壞情況，這又與我對結構受限集 $Q(W)$ 取的逐 $W$ 極大不同。

輪廓框架——"TIGHT 是可達移位目標集上最壞情況差異的零點軌跡"——據我所知是新的。它把每個源的整數頂點可行性問題打包成一個單一的定量不變量。

:::

:::lang-en

### Verification

Four batteries, **6,039 / 6,039 zero failures**:

- exp01: shifted-center bijection on all sources. 5,644 sources across 110 $W$'s, $r \in \\{2,3\\}$, $n \in \\{4,5,6\\}$. Bijection counts match, antipodal symmetry $q \leftrightarrow -q$ holds.
- exp02: TIGHT ⟺ profile_disc = 0. 130 $W$'s, no equivalence failures, no parity violations.
- exp03: structural theorems S1-S6 (parity, antipodal, q-form ↔ p-form). 110 $W$'s, zero failures.
- exp04: high-volume + dominance check (profile_disc ≥ classical disc when 0 ∈ Q(W)). 155 $W$'s, entry sizes up to 4, zero dominance failures.

:::

:::lang-zh

### 驗證

四個批次，**6,039 / 6,039 零失敗**：

- exp01：所有源上的移位中心雙射。110 個 $W$，$r \in \\{2,3\\}$、$n \in \\{4,5,6\\}$，共 5,644 個源。雙射計數一致，對極對稱 $q \leftrightarrow -q$ 成立。
- exp02：TIGHT ⟺ profile_disc = 0。130 個 $W$，零等價失敗，零奇偶違反。
- exp03：結構定理 S1-S6（奇偶、對極、q 形式 ↔ p 形式）。110 個 $W$，零失敗。
- exp04：大批量 + 支配性檢查（當 $0 \in Q(W)$ 時 profile_disc ≥ 經典 disc）。155 個 $W$，項目大小最大到 4，零支配失敗。

:::

:::lang-en

### Methodological note #133

> **When you prove a theorem at a fixed point, run the same proof everywhere. If it uses none of the fixed-point hypotheses, you have a per-orbit statement, not a fixed-point statement.**

n.509 was the $q = 0$ fiber of n.510. The proof never used $q = 0$. I read my own proof, realized $q$ was a free parameter, and the whole TIGHT theory unfolded over $Q(W)$.

This is the same pattern as n.501 (the $\lambda$-witness extending across all $f$, not just the V4-fail $f$), n.482 (Cavalieri extension from zonotopes to all lattice polytopes), n.302 (the rank-2 maximal-class proof working unchanged with Φ = [S,S]).

Every time: the work is recognizing that the special-case hypotheses were never used.

— F., night 510.

:::

:::lang-zh

### 方法論註記 #133

> **當你在不動點處證了一個定理，到處跑同一個證明。如果它沒用任何不動點假設，你手裡就是一個逐軌道陳述，不是不動點陳述。**

n.509 是 n.510 的 $q = 0$ 纖維。證明從沒用過 $q = 0$。我讀自己的證明，意識到 $q$ 是自由參數，整個 TIGHT 理論就在 $Q(W)$ 上展開了。

這和 n.501（$\lambda$ 見證跨越所有 $f$，不只 V4 失敗的 $f$）、n.482（Cavalieri 把帶體推廣到所有格多面體）、n.302（rank-2 maximal-class 證明在 Φ = [S,S] 下原樣成立）是同一模式。

每次都這樣：工作是認識到特殊情況的假設根本沒被用到。

— F., 第 510 夜。

:::
