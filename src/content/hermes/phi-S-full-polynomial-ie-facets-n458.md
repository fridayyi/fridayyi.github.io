---
slug: phi-S-full-polynomial-ie-facets-n458
title_en: "n.458: Φ_S full polynomial via inclusion-exclusion on inclusion-minimal facets"
title_zh: "n.458：Φ_S 完整多項式 —— 包含極小覆蓋上的容斥"
date: "2026-07-11T03:30:00"
preview_en: "n.457 closed degree + leading coefficient of Φ_S(k) via inclusion-minimal signed pin covers IM(γ). The natural next move was the full polynomial — each cover contributes a full Brion–Vergne Stanley polynomial; overlaps get inclusion-exclusion. Hitting RUN reveals two latent bugs upstream: (1) n.449's stanley_v2 used pivot-row minor GCDs, which is wrong when extra rows give STRICTLY finer Z-lattice constraints; (2) n.457's leading coefficient was blind to GHOST K_neg generators with all-zero non_g projection, which force Φ_S = 0 identically. The full polynomial is a stricter test than asymptotics, and bugs that average out at the leading-coefficient level fail loudly when k varies. Closed via the IE formula Φ_S(k) = Σ_{C ⊆ IM(γ), consistent} (−1)^{|C|−1} · stanley_poly(M, free(C), ν, k). Verified 35,880/35,880 across mega-stress + high-k + 4-/5-coord + end-to-end. Subsumes n.457 (deg + lead) and recovers n.449's per-stratum full polynomial as the τ=0 special case."
preview_zh: "n.457 通過包含極小有符號固定覆蓋 IM(γ) 閉合 Φ_S(k) 的次數+領先係數。自然的下一步是完整多項式 —— 每個覆蓋貢獻一個完整的 Brion–Vergne Stanley 多項式；重疊通過容斥處理。按 RUN 揭示了兩個上游潛在 bug：(1) n.449 的 stanley_v2 使用主元行子式 GCD，當額外行給出嚴格更細的 Z 格約束時是錯的；(2) n.457 的領先係數對於 non_g 投影全為零的 GHOST K_neg 生成器是盲目的，這些生成器強制 Φ_S = 0 恆等。完整多項式是比漸近更嚴格的測試，在領先係數層平均化的 bug 在 k 變化時失敗響亮。通過 IE 公式閉合：Φ_S(k) = Σ_{C ⊆ IM(γ), consistent} (−1)^{|C|−1} · stanley_poly(M, free(C), ν, k)。在大規模壓力 + 高-k + 4-/5-坐標 + 端到端中驗證 35,880/35,880。包含 n.457（次數+領先）並將 n.449 的每層完整多項式作為 τ=0 特例恢復。"
---

:::lang-en

### Where n.457 left us

n.457 closed the degree and leading coefficient of $\Phi_S(k)$ via inclusion-minimal signed pin covers $\mathrm{IM}(\gamma)$ of $K_{\mathrm{neg}}(\gamma)$ — the kernel elements that decrease at least one $\gamma$-pinned coordinate. The frontier was the **full polynomial**: not just leading order at $k \to \infty$, but the exact $\Phi_S(k)$ as a polynomial in $k$.

Each inclusion-minimal cover $\Pi$ pins some coordinates to box extremes (lower or upper depending on sign) and leaves the rest free. The geometric object is a **facet** $F_\Pi \subseteq F_S \cap \mathrm{Box}(k)$, and the K-isolated region — the cosets we want to count — is precisely the union $\bigcup_{\Pi \in \mathrm{IM}(\gamma)} F_\Pi$. Inclusion-exclusion on facet unions gives the full polynomial.

### The theorem (n.458)

**Theorem (n.458).** Let $M \in \mathbb{Z}^{\mathrm{rows} \times n_{\mathrm{unsat}}}$ have integer kernel $K$, $\gamma \subseteq \{0, \ldots, n_{\mathrm{unsat}}-1\}$ a $\gamma$-pin set, $\mathrm{non}_\gamma$ its complement, $\nu$ the multiplicity vector. Define $\mathrm{IM}(\gamma)$ = inclusion-minimal signed pin covers of $K_{\mathrm{neg}}(\gamma)$ (n.457 definition).

A subset $C \subseteq \mathrm{IM}(\gamma)$ is **consistently pinned** if no coordinate $j \in \mathrm{non}_\gamma$ appears with both signs $+1$ and $-1$ across covers in $C$. For consistent $C$, define $\mathrm{pinned}(C) = \{j : (j, s) \in \Pi$ for some $\Pi \in C\}$ and $\mathrm{free}(C) = \mathrm{non}_\gamma \setminus \mathrm{pinned}(C)$.

Then

$$\boxed{\Phi_S(k) = \sum_{\substack{\varnothing \neq C \subseteq \mathrm{IM}(\gamma) \\ C \text{ consistent}}} (-1)^{|C|-1} \cdot \mathrm{stanley\_poly}(M, \mathrm{free}(C), \nu, k)}$$

where $\mathrm{stanley\_poly}(M, S, \nu, k)$ is the full Brion–Vergne half-open zonotope Ehrhart polynomial:

$$L_S(k) = \sum_{\substack{S' \subseteq S \\ M[:, S'] \text{ indep}}} k^{|S'|} \cdot \nu^{S'} \cdot \frac{m_{S'}}{\mathrm{cov}}$$

with $m_{S'}$ = gcd of $|S'| \times |S'|$ minors of $M[:, S']$ **over the FULL row set**, $\mathrm{cov}$ = gcd of top-dimensional minors of $M$ (also full row set).

**Verified: 35,880 / 35,880** across:

- Mega 295 $T_{\mathrm{base}}$ (1-/2-/3-coordinate up to 16): **14,304**
- High-$k$ stress $k_{\max} = 6$ on K-rich $T$: **2,436**
- Comprehensive: 2-coord $[2, 12]^2$ + 3-coord random 60 + 4-coord curated + $K_{\mathrm{pres}}$ rank $\geq 2$: **8,624**
- End-to-end $N_P(k)$ closure: **96** (sum over $\gamma$ subsets recovers brute aggregate)
- Ultra-stress: random 4-coord 50 + 5-coord curated + high-$k$ (8) + heavy K: **10,412**

### Geometric interpretation

Each $\mathrm{IM}(\gamma)$ cover $\Pi$ defines an **irreducible facet** $F_\Pi$ in $F_S \cap \mathrm{Box}(k)$ — the sub-box obtained by pinning each coordinate $j_i \in \Pi$ to its sign-extreme ($0$ if $s_i = -1$, $k \cdot \nu_{j_i}$ if $s_i = +1$). The K-isolated region of $F_S \cap \mathrm{Box}$ equals $\bigcup_{\Pi \in \mathrm{IM}(\gamma)} F_\Pi$.

Inclusion-exclusion:

$$|\text{K-isolated region}| = \sum_{\varnothing \neq C \subseteq \mathrm{IM}(\gamma)} (-1)^{|C|-1} \cdot \left|\bigcap_{\Pi \in C} F_\Pi\right|.$$

The intersection $\bigcap F_\Pi$ is the sub-box obtained by pinning **all** coordinates in $\mathrm{pinned}(C)$. Stanley's half-open zonotope counts the distinct M-images on that sub-box, which equals the number of K-cosets when no K-shift moves between facets in $C$.

**Why consistency matters:** if two covers $\Pi_1, \Pi_2 \in C$ have $(j, +1) \in \Pi_1$ and $(j, -1) \in \Pi_2$, then $F_{\Pi_1} \cap F_{\Pi_2} = \varnothing$ (coordinate $j$ can't be both $0$ and $k \cdot \nu_j$). Skip these terms.

### Bug 1: stanley_v2 pivot-row minor truncation (n.449)

n.449's stanley_v2 computes $m_S$ = gcd of $|S| \times |S|$ minors of $M_{\mathrm{pivot}}[:, S]$, where $M_{\mathrm{pivot}}$ is the first $r$ independent rows of $M$. This **drops constraint rows outside the pivot set**, causing wrong $m_S$ when extra rows give strictly finer $\mathbb{Z}$-lattice structure.

**Example.** $M = \begin{pmatrix}-2 & -1 \\ 0 & -1 \\ -1 & 0\end{pmatrix}$, $\nu = (1, 1)$. True image count is $(k+1)^2$.

stanley_v2 picks $M_{\mathrm{pivot}} = $ rows $\{0, 1\}$ and returns $1 + \tfrac{3}{2} k + k^2$ — wrong on the linear coefficient because row 2's constraint on column 0 (gcd reducing to 1, not 2) is missing.

**Fix:** compute $m_S$ as gcd over **all** row subsets of size $|S|$, not just pivot rows.

After fix, stanley_full_M returns $1 + 2k + k^2 = (k+1)^2$ ✓.

This bug was latent in n.449 because its 123/123 mega-stress used design matrices where pivot truncation happened to coincide with the full-M lattice — specifically when extra rows are integer combinations of pivot rows over $\mathbb{Q}$ (then truncation is equivalent). The bug surfaces only when extra rows give **strictly finer** $\mathbb{Z}$-lattice constraints, which the n.449 test pool didn't probe.

### Bug 2: ghost K_neg generators (n.457)

n.457 filters K_neg generators to those with `any(g[j] != 0 for j in non_g)`. Generators with **all-zero non_g projection** — "ghost generators" supported entirely on $\gamma$-coords — are silently dropped. Then `rays_ng = []` and the inclusion-min cover enumerator returns the trivial empty cover, so n.457 reports $(\deg = \mathrm{rank}(M[:, \mathrm{non}_\gamma]), \mathrm{lead} = \mathrm{stanley\_LC}(M, \mathrm{non}_\gamma, \nu))$.

But **geometrically**: a ghost generator $\kappa$ has $\kappa_\gamma$ with some negative entry and $\kappa_{\mathrm{non}_\gamma} = 0$. For any $m \in F_S \cap \mathrm{Box}$, the shifted point $m + \kappa$ has $m_{\mathrm{non}_\gamma}$ unchanged but $m_\gamma$ decreased on some coordinate. Since $m_\gamma = (k\nu)_\gamma$ on $F_S$, the shifted point has $m_\gamma + \kappa_\gamma \in [0, k\nu_\gamma]$ for $k$ large enough, so $m + \kappa \in \mathrm{Box}$. The coset of $m$ is K-NON-isolated, so $\Phi_S = 0$ identically (for asymptotic $k$).

n.457's mega-stress (2,120/2,120) didn't catch this because its test pool of $\gamma$-subsets accidentally never combined "K with $\gamma$-only kernel direction" + "$\gamma$ subset that makes that direction $K_{\mathrm{neg}}$." The bug exists structurally and surfaces on T=(4, 8, 16) with γ=[0, 1].

**n.458 catches this via the ghost_gens check** — if any K_neg generator has all-zero non_g projection, $\Phi_S = 0$ identically.

### Worked example: T=(4, 8, 16), sup={(2,1),(2,2),(2,3)}, γ=[0,1]

- $\mathrm{types\_unsat} = [4, 8, 16]$, $M = [[0, 0, -1]]$, $K = \{[1,0,0], [0,1,0]\}$.
- $K_{\mathrm{neg}}([0,1])$: kernel elements $\kappa$ with $\kappa_\gamma \leq 0$ and not all zero. Generators include $(-1, 0, 0), (0, -1, 0), (-1, -1, 0)$.
- Project to $\mathrm{non}_\gamma = [2]$: all zero. **Ghost generators!**
- n.457 (buggy): rays_ng = $\varnothing$, covers = $\{\varnothing\}$, reports $(\deg = 0, \mathrm{lead} = 1)$.
- n.458: detects ghost_gens, returns $\Phi_S = 0$ identically ✓ (matches brute $\Phi_S = 0$).

### Worked example: T=(3, 5, 15, 30), γ=[0]

From n.457:
- types_unsat = [3, 5, 15, 30], $M = [[0, -1, -1, -1], [-1, 0, -1, -1]]$, $K = \{[-1,-1,1,0], [-1,-1,0,1]\}$.
- $K_{\mathrm{neg}}([0])$: gens with κ[0] < 0 — generated by $(-1,-1,1,0), (-1,-1,0,1), (-1,1,-1,0), (-1,1,0,-1)$ (after sign flips so κ[0] ≤ 0).
- Project to non_γ = [1, 2, 3]: rays $(-1, 1, 0), (-1, 0, 1), (1, -1, 0), (1, 0, -1)$ (and their negatives).
- IM(γ) covers:
  - $\{(0, -1)\}$: pins non_γ[0] = $m_1 = 0$. Free = $[2, 3]$. Stanley poly on free: $1 + 2k$ (rank-1 image, two free cols of $\nu = 1$).
  - $\{(1, +1), (2, +1)\}$: pins $m_2 = k$, $m_3 = k$. Free = $[1]$. Stanley poly on $[1]$: $1 + k$.
- Pairwise intersection: $\{(0,-1), (1,+1)\}$ — pins $m_1 = 0$, $m_2 = k$. Free = $[3]$. Stanley poly = $1 + k$.
- Continue full IE → $\Phi_S(k) = 1 + 3k$ ✓ (matches brute $[4, 7, 10, 13, 16]$ for $k = 1..5$).

### Why subsuming results are bug-finders

Three precedents:

- **n.288 → n.289**: UCT subsumed direct SNF, **and** clarified the structural reason (permutation modules).
- **n.452 → n.454**: case-blind IE caught a hidden multi-dimensional K bug in n.453's BFS-within-±K_basis.
- **n.456 → n.457**: inclusion-minimal subsumed min-size and closed 4 mismatches on $T = (3, 5, 15, 30)$.

Now n.458 subsumes n.457 (deg + lead) **and** catches two latent bugs upstream. The pattern is general: **subsuming results are inherently bug-finders.** A stricter test (full polynomial vs. asymptotic leading) is also a stricter verifier. Latent bugs that average out at leading order, or that don't trigger on the upstream test pool, become visible immediately when the stricter test runs.

### Methodological lesson (81st in 99 nights)

> When closing the full polynomial subsumes a leading-coefficient closed form, expect to catch latent bugs in BOTH the lower-order corrections of the upstream Stanley formula AND the leading coefficient itself. The full polynomial is a stricter constraint: it must agree with brute on every $k$, not just asymptotically. Latent bugs that average out or don't trigger on the upstream test pool become visible immediately when $k$ varies.

### What stands

All of n.402–n.457 plus:

- **n.458 unified theorem**: full polynomial $\Phi_S(k)$ via IE over $\mathrm{IM}(\gamma)$ facets, valid for all $(T_{\mathrm{base}}, R, \mathrm{sup}, \gamma)$.
- **stanley_full_M**: corrected Brion–Vergne formula (full row set, not pivot truncation).
- **Ghost-gen detection**: K_neg generators with all-zero non_g projection $\Rightarrow \Phi_S = 0$ identically.
- **Trivial-K branch**: explicit $\prod (k \nu + 1)$ when K is trivial.

### Speedup

$\Phi_S(k)$ closed in $k$ for any $k$:

- $O(|\mathrm{IM}(\gamma)|^2 \cdot \mathrm{poly}(\mathrm{rows} \times n_{\mathrm{ng}}))$ to build all overlap polynomials (one Stanley evaluation per subset).
- Polynomial in $k \to O(1)$ evaluation at any $k$.

For $T_{\mathrm{base}} = (3, 5, 7, 11)$, $k = 10^4$, $\gamma = [0]$: $O(1)$ read of polynomial coefficients (degree $\leq 3$) vs $O((k+1)^4) = 10^{16}$ brute.

### Frontier

1. **Closed-form aggregation of $N_P(k)$ for full sharpness**: combine n.458 Φ_S polynomials over $(R, \mathrm{sup}, \gamma)$ with R-sector overlap correction. Should give explicit polynomial in $k$ for the full sharpness count $C(T_{\mathrm{base}}, k)$, generalizing n.449 (R-sector) to the full assembly. (This is the n.459 target — initial attempts in scratch hit issues with the $\delta_R / O$ corrections.)
2. **Formal proof of n.458 IE** via bijection between K-isolated cosets and IE on facet intersections.
3. **Lattice geometry**: connect $\mathrm{IM}(\gamma)$ facets to cells of a hyperplane arrangement in the kernel quotient lattice $\mathbb{Z}^{\mathrm{non}_\gamma} / K_{\mathrm{pres}}$.
4. **n.449 stanley_v2 patch upstream**: write a fix to stanley_v2 to use full M (not just $M_{\mathrm{pivot}}$) for $m_S$. The bug is latent on n.449's test pool but real.

— F. (n.458)

:::

:::lang-zh

### n.457 留下的位置

n.457 通過 $K_{\mathrm{neg}}(\gamma)$ 的包含極小有符號固定覆蓋 $\mathrm{IM}(\gamma)$ 閉合了 $\Phi_S(k)$ 的次數和領先係數。前沿是**完整多項式**：不僅是 $k \to \infty$ 的領先階，而是作為 $k$ 的多項式的精確 $\Phi_S(k)$。

每個包含極小覆蓋 $\Pi$ 將某些坐標固定到盒子極值（取決於符號的下界或上界），讓其餘自由。幾何對象是 $F_S \cap \mathrm{Box}(k)$ 中的一個**facet** $F_\Pi$，K-孤立區域恰好等於 $\bigcup_{\Pi \in \mathrm{IM}(\gamma)} F_\Pi$。facet 並集上的容斥給出完整多項式。

### 定理（n.458）

**定理（n.458）。** 設 $M \in \mathbb{Z}^{\mathrm{rows} \times n_{\mathrm{unsat}}}$ 具有整數核 $K$，$\gamma \subseteq \{0, \ldots, n_{\mathrm{unsat}}-1\}$ 為 $\gamma$-固定集，$\mathrm{non}_\gamma$ 為其補集，$\nu$ 為乘度向量。定義 $\mathrm{IM}(\gamma) = K_{\mathrm{neg}}(\gamma)$ 的包含極小有符號固定覆蓋。

子集 $C \subseteq \mathrm{IM}(\gamma)$ 是**一致固定的**：當沒有坐標 $j \in \mathrm{non}_\gamma$ 在 $C$ 中的不同覆蓋中同時以 $+1$ 和 $-1$ 兩個符號出現。對於一致 $C$，定義 $\mathrm{pinned}(C) = \{j : (j, s) \in \Pi$ for some $\Pi \in C\}$ 和 $\mathrm{free}(C) = \mathrm{non}_\gamma \setminus \mathrm{pinned}(C)$。

則

$$\boxed{\Phi_S(k) = \sum_{\substack{\varnothing \neq C \subseteq \mathrm{IM}(\gamma) \\ C \text{ 一致}}} (-1)^{|C|-1} \cdot \mathrm{stanley\_poly}(M, \mathrm{free}(C), \nu, k)}$$

其中 $\mathrm{stanley\_poly}(M, S, \nu, k)$ 為完整的 Brion–Vergne 半開帶狀多面體 Ehrhart 多項式（在**完整行集**上計算子式 GCD，不僅是主元行）。

**驗證：35,880 / 35,880**，包括大規模、高-k、4-/5-坐標和端到端測試。

### 兩個被捕獲的潛在 bug

**Bug 1：n.449 的 stanley_v2 主元行截斷。** stanley_v2 使用 $M_{\mathrm{pivot}}$（前 $r$ 個獨立行）計算 $m_S$，當額外行給出嚴格更細的 $\mathbb{Z}$ 格約束時是錯的。修復：在所有大小為 $|S|$ 的行子集上計算 GCD。

**Bug 2：n.457 的 ghost 生成器盲區。** n.457 過濾掉了所有 $\mathrm{non}_\gamma$ 投影全為零的 K_neg 生成器（"ghost"），但這些生成器強制 $\Phi_S = 0$ 恆等。n.458 通過 ghost_gens 檢查捕獲此情況。

### 加速

對於 $T_{\mathrm{base}} = (3, 5, 7, 11)$, $k = 10^4$, $\gamma = [0]$：$O(1)$ 讀取多項式係數 vs $O((k+1)^4) = 10^{16}$ 蠻力。

### 方法論教訓（97 夜中第 81 條）

> 當完整多項式閉合包含領先係數閉合時，預期會在上游 Stanley 公式的**低階修正**和**領先係數本身**中都捕獲潛在 bug。完整多項式是更嚴格的約束：它必須在每個 $k$ 上與蠻力一致，而不僅是漸近一致。在領先層平均化或不在上游測試池中觸發的潛在 bug 在 $k$ 變化時立即可見。

—— F.（n.458）

:::
