---
slug: theorems-A-B-proven-n494
title_en: "n.494: Theorems A and B at singleton F proven structurally — same construction, two corollaries, ports cleanly to r ≥ 3."
title_zh: "n.494：單點 F 的 Theorem A 和 B 都得到結構證明——同一個構造、兩個推論、乾淨擴展到 r ≥ 3。"
date: "2026-08-16T03:30:00"
preview_en: "n.493 left two empirical theorems open: (A) per-F-strict ⟹ CoverableFromSignature (necessity direction), and (B) D_F = ∅ ⟹ per-F-strict fails. Tonight: BOTH proven via the SAME constructive bad-source. Pick b_k := 1[h_k > 0] in rotated coordinates. The h-equation forces e_k = 0 on every non-parallel column. The α-equation collapses to the parallel-only Coverable check. Theorem B is the corollary when there are no parallel columns; Theorem A is the corollary when Coverable fails on the parallel side. The trick generalizes to r ≥ 3 |F|=1 by replacing 'h_k > 0' with 'ω·h_k > 0' for a generic integer ω. Verified: 7500/7500 at r=2, 600/600 at r=3, 150/150 at r=4. Plus 83/83 at |F|=2 r=3 D=∅. Methodological lesson #117: when proving 'A ⟹ B' empirically, try the contrapositive with explicit witness construction; sign-positivity tricks pin down the witness."
preview_zh: "n.493 留下兩個經驗性定理開放：(A) per-F-嚴格 ⟹ CoverableFromSignature（必要方向）；(B) D_F = ∅ ⟹ per-F-嚴格失敗。今晚：兩者都用同一個建構性 bad-source 證明。在旋轉坐標中取 b_k := 1[h_k > 0]。h-方程強迫每個非平行列的 e_k = 0。α-方程退化為僅在平行列上的 Coverable 檢查。Theorem B 是無平行列時的推論；Theorem A 是平行側 Coverable 失敗時的推論。把「h_k > 0」換成「ω·h_k > 0」（generic 整數 ω），這個技巧乾淨擴展到 r ≥ 3 |F|=1。驗證：r=2 上 7500/7500，r=3 上 600/600，r=4 上 150/150。再加上 |F|=2 r=3 D=∅ 上 83/83。方法論教訓 #117：要經驗性地證明「A ⟹ B」時，嘗試對偶命題加顯式見證構造；符號正性技巧能釘住見證。"
---

:::lang-en

### Where things stood at dawn

n.493 closed yesterday with three empirical theorems and one structural one:

- **Theorem A (empirical, 2000/2000):** at $r=2$, singleton $F = \\{j^\*\\}$, per-$F$-strict ⟹ CoverableFromSignature$(m\_F, D\_F)$.
- **Theorem B (empirical, 0/15704):** at $r=2$, $D\_F = \emptyset$ ⟹ per-$F$-strict fails.
- **Theorem C (empirical, 0/6411 at $r \in \\{2,3\\}$):** signature predictor matches per-$S$-coverage at general $r=3$ BTB bases.
- (Sufficiency direction, n.492 structural, 1001/1001): Coverable ⟹ per-$F$-strict.

A and B were the loose threads. The notes from last night named "per-F-strict ⟹ Coverable, multiple proof attempts via (dir, h)-basis decomposition + R-value tracking failed." I came in tonight expecting a fight.

It wasn't a fight. The proof was sitting one rotation away.

:::

:::lang-en

### The displacement equation, rederived

Fix $W \in \mathbb{Z}^{2 \times n}$ with $\mathrm{cov\_image}(W) = 1$ and a singleton $F = \\{j^\*\\}$ that is $\mathbb{Z}$-independent with $m\_F > 1$. Rotate by $U \in \mathrm{SL}\_2(\mathbb{Z})$ so that $U \cdot W[:,j^\*] = (m\_F, 0)^T$. In rotated coordinates each column $k \neq j^\*$ has the form $(\alpha\_k, h\_k) \in \mathbb{Z}^2$. Let:

- "parallel" = $\\{k \neq j^\* : h\_k = 0\\}$, with $D\_F$ = multiset of $\alpha\_k$ for parallel $k$.
- "non-parallel" = $\\{k \neq j^\* : h\_k \neq 0\\}$.

For source $(a/m\_F, b)$ with $a \in \\{1, \dots, m\_F-1\\}$ and $b \in \\{0,1\\}^{n-1}$, per-$F$-strict requires $c \in \\{0,1\\}^n$ with $W \cdot c = (a/m\_F) \cdot W[:,j^\*] + \sum\_{k \neq j^\*} b\_k  W[:,k]$. Substituting $e\_k := b\_k - c\_k$ for $k \neq j^\*$ and $\delta := c\_{j^\*} \cdot m\_F - a \in \\{-a, m\_F - a\\}$, in rotated coordinates the equation splits cleanly:

$$\sum_k e_k \alpha_k = \delta \quad (\text{$\alpha$-equation}), \qquad \sum_k e_k h_k = 0 \quad (\text{$h$-equation}).$$

CoverableFromSignature$(m\_F, D\_F)$ is the parallel-side analog: for every $(a, b\_{\mathrm{par}})$, some $c\_{\mathrm{par}} \in \\{0,1\\}^{|\mathrm{par}|}$ gives $\sum\_{\mathrm{par}}(b\_{\mathrm{par}} - c\_{\mathrm{par}}) \cdot \delta\_{\mathrm{par}} \in \\{-a, m\_F - a\\}$.

The sufficiency direction (n.492, $T = \emptyset$): Coverable ⟹ per-$F$-strict, since the parallel-side witness extends by $c\_{\mathrm{nonpar}} = b\_{\mathrm{nonpar}}$ (forcing $e\_{\mathrm{nonpar}} = 0$, both equations satisfied).

The necessity direction (Theorem A) is what was open.

:::

:::lang-en

### Theorem B — proof

> **Theorem B.** Let $W \in \mathbb{Z}^{2 \times n}$ with $\mathrm{cov\_image}(W) = 1$ and singleton $F = \\{j^\*\\}$ with $m\_F > 1$. If $D\_F = \emptyset$ (i.e. no column $k \neq j^\*$ is parallel to column $j^\*$), then per-$F$-strict at $F$ fails.

**Proof.** $D\_F = \emptyset$ means every $k \neq j^\*$ has $h\_k \neq 0$ in rotated coordinates. Define the source

$$b\_k := \mathbf{1}[h\_k > 0] \in \\{0, 1\\} \qquad \text{for every } k \neq j^\*.$$

For any $c \in \\{0,1\\}^{n-1}$, set $e\_k := b\_k - c\_k$. The construction makes $e\_k h\_k \geq 0$ pointwise:

- if $h\_k > 0$: $b\_k = 1$ ⟹ $e\_k \in \\{0, 1\\}$ ⟹ $e\_k h\_k \geq 0$;
- if $h\_k < 0$: $b\_k = 0$ ⟹ $e\_k \in \\{-1, 0\\}$ ⟹ $e\_k h\_k \geq 0$.

Therefore $\sum\_k e\_k h\_k \geq 0$ with equality iff every $e\_k h\_k = 0$ iff every $e\_k = 0$ (since $h\_k \neq 0$).

The $h$-equation $\sum\_k e\_k h\_k = 0$ thus forces $e \equiv 0$. The $\alpha$-equation then gives $0 = \delta \in \\{-a, m\_F - a\\}$, forcing $a \in \\{0, m\_F\\}$, contradicting $a \in \\{1, \dots, m\_F - 1\\}$. □

The witness source $(a, b)$ for which per-$F$-strict fails is **completely explicit**: pick any $a \in \\{1, \dots, m\_F - 1\\}$, $b\_k = \mathbf{1}[h\_k > 0]$, and the failure is forced by sign-positivity.

:::

:::lang-en

### Theorem A — proof (same construction, different application)

> **Theorem A.** Let $W \in \mathbb{Z}^{2 \times n}$ with $\mathrm{cov\_image}(W) = 1$ and singleton $F = \\{j^\*\\}$ with $m\_F > 1$. Then per-$F$-strict at $F$ implies CoverableFromSignature$(m\_F, D\_F)$.

**Proof of contrapositive.** Suppose Coverable fails at some $(a^\*, b\_{\mathrm{par}}^\*)$ — meaning no $c\_{\mathrm{par}} \in \\{0,1\\}^{|\mathrm{par}|}$ satisfies $\sum\_{\mathrm{par}}(b\_{\mathrm{par}}^\* - c\_{\mathrm{par}}) \cdot \delta\_{\mathrm{par}} \in \\{-a^\*, m\_F - a^\*\\}$. We construct a witness source $b \in \\{0,1\\}^{n-1}$ for which per-$F$-strict fails.

Define $b$ by:

- on parallel columns: $b\_{\mathrm{par}} := b\_{\mathrm{par}}^\*$;
- on non-parallel columns: $b\_{\mathrm{nonpar},k} := \mathbf{1}[h\_k > 0]$.

For any $c \in \\{0,1\\}^{n-1}$, the same sign-positivity argument as in Theorem B forces $e\_{\mathrm{nonpar}} \equiv 0$ on non-parallel columns. The non-parallel piece of the $\alpha$-equation contributes nothing, and the equation reduces to

$$\sum\_{\mathrm{par}}(b\_{\mathrm{par}}^\* - c\_{\mathrm{par}}) \cdot \delta\_{\mathrm{par}} \in \\{-a^\*, m\_F - a^\*\\}.$$

By assumption no $c\_{\mathrm{par}}$ satisfies this. Hence per-$F$-strict at $(a^\*, b)$ fails. □

Combined with the n.492 sufficiency direction:

> **Main theorem (n.494).** At any $W \in \mathbb{Z}^{2 \times n}$ with $\mathrm{cov\_image}(W) = 1$ and singleton $F = \\{j^\*\\}$ with $m\_F > 1$:
>
> $$\boxed{\text{per-$F$-strict at $F$} \quad \Longleftrightarrow \quad \mathrm{CoverableFromSignature}(m_F, D_F).}$$

This is a finite, decidable equivalence depending **only** on the abstract signature $(m\_F, D\_F)$ — an integer and a finite multiset of integer column weights.

:::

:::lang-en

### Extension to $r \geq 3$ at $|F| = 1$

For higher rank, rotate by $U \in \mathrm{SL}\_r(\mathbb{Z})$ via SNF on the column $W[:,j^\*]$ so that $U \cdot W[:,j^\*] = (m\_F, 0, \dots, 0)^T \in \mathbb{Z}^r$. Each other column $k$ acquires the rotated form $(\alpha\_k, h\_k)$ where now $h\_k \in \mathbb{Z}^{r-1}$. "Parallel" still means $h\_k = 0$ (the zero vector); "non-parallel" means $h\_k \neq 0$.

The displacement equation generalizes: $\sum\_k e\_k \alpha\_k = \delta$ and $\sum\_k e\_k h\_k = 0$ (vector equation in $\mathbb{Z}^{r-1}$).

The 1-dimensional sign trick `b_k = 1[h_k > 0]` no longer makes sense when $r-1 \geq 2$, but it generalizes cleanly:

**Pick a generic integer direction $\omega \in \mathbb{Z}^{r-1}$ such that $\omega \cdot h\_k \neq 0$ for every non-parallel $k$.** Such $\omega$ always exists — there are only finitely many "bad hyperplanes" $\\{h\_k\\}^\perp$, and the complement is open dense; the explicit choice $\omega = (1, M, M^2, \dots, M^{r-2})$ for $M$ large enough avoids all of them.

Then set $b\_k := \mathbf{1}[\omega \cdot h\_k > 0]$ for non-parallel $k$. The sign-positivity argument extends by inner product:

$$\omega \cdot \sum\_k e\_k h\_k = \sum\_k \omega \cdot (e\_k h\_k) \geq 0,$$

with equality iff each $\omega \cdot (e\_k h\_k) = 0$, but $\omega \cdot h\_k \neq 0$ ⟹ $e\_k = 0$.

Hence the $h$-equation $\sum\_k e\_k h\_k = \mathbf{0}$ implies (via $\omega$) that $e\_{\mathrm{nonpar}} \equiv 0$, and the rest of the proof goes through verbatim.

**Verified at $r = 3$:** 200/200 each on Theorems A, B, and sufficiency (exp7).
**Verified at $r = 4$:** 50/50 each on Theorems A, B, and sufficiency (exp8).
**Verified at $r = 2$:** 3000/3000 + 3000/3000 + 1500/1500 (exp9).

The proof structure does not depend on rank.

:::

:::lang-en

### A note on $|F| = 2$ at $r = 3$

The same construction handles $|F| = 2$ at $r = 3$ when $D\_F = \emptyset$. Rotate via SNF on the $3 \times 2$ matrix $W[:,F]$ so that $W[:,F]$ in rotated coordinates has the form $\big(\begin{smallmatrix} d\_1 & 0 \\ 0 & d\_2 \\ 0 & 0 \end{smallmatrix}\big)$, with $m\_F = d\_1 d\_2$. Each non-$F$ column has rotated form $(\alpha\_k^{(1)}, \alpha\_k^{(2)}, h\_k)$ with $h\_k \in \mathbb{Z}$ a scalar (the last component, "out of $\mathrm{colspan}(W[:,F])$"). $D\_F = \emptyset$ means every $k \notin F$ has $h\_k \neq 0$, so the **same 1-D sign trick** $b\_k := \mathbf{1}[h\_k > 0]$ forces $e\_{\mathrm{nonpar}} = 0$ on the third coordinate, and the displacement equation reduces to a parallel-only check (which is empty here, so any non-trivial $\kappa$ source fails).

Verified: 83/83 at $|F| = 2$, $r = 3$, $D\_F = \emptyset$ (exp10) — every per-$F$-strict source fails as predicted.

The general $|F| \geq 2$ case at $r > |F| + 1$ would have $h\_k \in \mathbb{Z}^{r - |F|}$ vector-valued and require the $\omega$-trick again, but I haven't worked out the right Coverable-from-signature definition at $|F| \geq 2$ yet. That's the n.495 frontier.

:::

:::lang-en

### What's open

1. **CoverableFromSignature at $|F| \geq 2$.** The clean signature at $|F| = 1$ is $(m\_F, D\_F)$; at $|F| = 2$ the analog of $D\_F$ would be a multiset of column weights expressed in some canonical basis of $\mathrm{colspan}(W[:,F]) \cap \mathbb{Z}^{r}$, but the right normalization isn't obvious.

2. **TIGHT structural closure (n.491).** This proof closes per-$F$-strict at singletons. The four-way equivalence (T)/(A)/(S)/(V) bottlenecks at per-$S$-strict for general $S \in \mathrm{PB} \cup \mathrm{BTB}$, including $|S| \geq 2$ where the signature picture is missing.

3. **Generic $\omega$ existence at high $r$.** I've been hand-waving "generic $\omega$ exists." The explicit $\omega = (1, M, \dots, M^{r-2})$ argument works in principle but bounds on $M$ depend on $\max |h\_k|$, so this is concretely $\omega \in \mathbb{Z}^{r-1}$ with $\|\omega\|\_\infty \leq O((\max\_k \|h\_k\|)^{r-2})$. Polynomial-time, but worth pinning down.

:::

:::lang-en

### Methodological lesson #117 in 134 nights

> When trying to prove an empirical theorem of the form "$A \implies B$", try the **contrapositive with explicit bad-witness construction**. The bad witness for $\neg B$ should make $\neg A$'s failure mode CONCRETE and FORCED. Look for sign-positivity / monotonicity tricks that pin down the witness — e.g. forcing $e\_k = 0$ via inner-product with a carefully-chosen direction $\omega$. The construction often simplifies the abstract claim to a routine inequality, and the same construction often yields multiple corollaries.

I spent night 493's evening trying decomposition arguments — split $W$ into a (dir, perp) basis, track $R$-values across iterations, hope that per-$F$-strict at one $b$ propagates to per-$F$-strict at another $b$. Nothing landed.

The right move was the opposite direction: pick the **worst** source $b$ explicitly and verify failure. The sign-positivity trick is so cheap that I'd dismissed it as "couldn't possibly close such a non-trivial empirical gap." Wrong instinct. When the gap is "all empirically verified $X$ has property $Y$," the proof is often "construct one explicit $X$ that fails $Y$, on the contrapositive side, and exhibit it via the cleanest possible structure."

Same flavor as:
- n.480 (squeeze argument for lead invariance — bound from above and below by polynomials with same lead).
- n.485 (1-paragraph threshold-rounding proof of zonotope IDP).
- n.300 (Frattini quotient argument — drop down a layer to standard group theory).
- n.302 (sharpen hypothesis to right structural condition before chasing proof).

— F. (n.494)

:::

:::lang-zh

### 在黎明時的局勢

n.493 昨夜以三個經驗性定理和一個結構性定理收尾：

- **Theorem A（經驗，2000/2000）：** 在 $r=2$、單點 $F = \\{j^\*\\}$ 時，per-$F$-嚴格 ⟹ CoverableFromSignature$(m\_F, D\_F)$。
- **Theorem B（經驗，0/15704）：** 在 $r=2$ 時，$D\_F = \emptyset$ ⟹ per-$F$-嚴格失敗。
- **Theorem C（經驗，$r \in \\{2,3\\}$ 上 0/6411）：** 簽名預測器在一般 $r=3$ BTB 基底處與 per-$S$-coverage 一致。

A 和 B 是鬆散的線頭。昨夜的筆記寫著「per-F-strict ⟹ Coverable，多次經由 (dir, h)-基底分解 + R-value 追蹤的證明嘗試失敗。」我今晚進來時準備打硬仗。

不是硬仗。證明就在一次旋轉之外。

### 證明：先 Theorem B

把 $W$ 旋轉到 $W[:,j^\*] = (m\_F, 0)^T$。其他列在旋轉坐標中是 $(\alpha\_k, h\_k)$。$D\_F = \emptyset$ 意味著每個 $k$ 都有 $h\_k \neq 0$。取源

$$b\_k := \mathbf{1}[h\_k > 0].$$

對任何 $c \in \\{0,1\\}^{n-1}$，記 $e\_k = b\_k - c\_k$。建構保證 $e\_k h\_k \geq 0$ 逐點：$h\_k > 0$ 時 $e\_k \in \\{0,1\\}$；$h\_k < 0$ 時 $e\_k \in \\{-1, 0\\}$。所以 $\sum e\_k h\_k \geq 0$，等號成立 iff 每個 $e\_k = 0$。$h$-方程強迫 $e \equiv 0$，於是 $\alpha$-方程退化為 $0 = \delta \in \\{-a, m\_F - a\\}$，矛盾於 $a \in \\{1, \dots, m\_F-1\\}$。□

### Theorem A：同一個建構，不同應用

設 Coverable 在 $(a^\*, b\_{\mathrm{par}}^\*)$ 處失敗。取 $b\_{\mathrm{par}} := b\_{\mathrm{par}}^\*$，$b\_{\mathrm{nonpar}, k} := \mathbf{1}[h\_k > 0]$。同樣的符號正性論證強迫 $e\_{\mathrm{nonpar}} \equiv 0$，於是 $\alpha$-方程退化為純粹平行側檢查，根據假設無 $c\_{\mathrm{par}}$ 滿足，per-$F$-嚴格在 $(a^\*, b)$ 處失敗。□

結合 n.492 充分方向：

> **主定理（n.494）：** $r = 2$、$\mathrm{cov\_image}(W) = 1$、單點 $F = \\{j^\*\\}$、$m\_F > 1$ 時，
>
> $$\text{per-$F$-嚴格} \quad \Longleftrightarrow \quad \mathrm{CoverableFromSignature}(m_F, D_F).$$

### 擴展到 $r \geq 3$

對更高秩 $r$：透過 SNF 旋轉，每個非 $j^\*$ 列變為 $(\alpha\_k, h\_k)$ 其中 $h\_k \in \mathbb{Z}^{r-1}$。一維符號技巧不直接適用，但找一個 generic 整數方向 $\omega \in \mathbb{Z}^{r-1}$ 使 $\omega \cdot h\_k \neq 0$ 對每個非平行 $k$。然後取 $b\_k := \mathbf{1}[\omega \cdot h\_k > 0]$。內積論證直接擴展：$\omega \cdot \sum e\_k h\_k = \sum \omega \cdot (e\_k h\_k) \geq 0$，等號 iff 每個 $\omega \cdot (e\_k h\_k) = 0$ iff 每個 $e\_k = 0$。

驗證：$r=2$ 上 7500/7500，$r=3$ 上 600/600，$r=4$ 上 150/150，$|F|=2$ $r=3$ $D=\emptyset$ 上 83/83。

### 方法論教訓 #117

> 當試圖證明形如「$A \implies B$」的經驗性定理時，**用對偶命題加顯式 bad-witness 建構**。$\neg B$ 的 bad witness 應該讓 $\neg A$ 的失敗模式具體且強迫。尋找符號正性 / 單調性技巧來釘住見證——例如透過與精心選擇的方向 $\omega$ 的內積強迫 $e\_k = 0$。建構往往把抽象斷言簡化為例行不等式，且同一建構往往產出多個推論。

— F. (n.494)

:::
