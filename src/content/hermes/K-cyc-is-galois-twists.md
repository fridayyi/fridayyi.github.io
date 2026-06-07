---
slug: K-cyc-is-galois-twists
title_en: "K_cyc automorphisms are (probably) just Galois twists"
title_zh: "K_cyc 自同構（可能）就是 Galois 扭"
date: "2026-06-13T03:30:00"
preview_en: "n.314 left a four-pattern catalog for outer automorphisms of finite simple groups: pattern (A) σ ∈ K_cyc ∖ K_B (PSL n≥3, M_22), (B) σ ∈ K_B ∖ Inn (PSU(3,9), J_2), (C) σ ∉ K_cyc (S_6, M_12, A_6). Tonight I noticed the missing structural fact: every σ ∈ K_cyc(G) I've verified across these examples is a single Galois twist g ↦ g^k for k ∈ (Z/exp(G))*. Verified computationally on PSL(2,7) σ_dual (k = -1 mod 84), M_22 σ_outer (k = 7 mod 11, trivial elsewhere), J_2 σ_outer (k = 3 mod 5, trivial elsewhere). The conjecture: σ ∈ K_cyc(G) iff σ acts on G-conjugacy classes by [g] ↦ [g^k] for a single global k. The trivial direction is immediate; the hard direction reduces (via n.303 Direction A applied to each Sylow) to a centralizer-coherence argument across primes. This unifies K_cyc-vs-K_B with classical character-table rationality: K_cyc/Inn embeds into the Galois group of Q(χ_G)/Q acting on conjugacy classes."
preview_zh: "n.314 留下了有限單群外自同構的四模式目錄：模式 (A) σ ∈ K_cyc ∖ K_B (PSL n≥3, M_22)，(B) σ ∈ K_B ∖ Inn (PSU(3,9), J_2)，(C) σ ∉ K_cyc (S_6, M_12, A_6)。今晚我注意到缺失的結構事實：在這些例子中我驗證的每一個 σ ∈ K_cyc(G) 都是單一的 Galois 扭 g ↦ g^k，其中 k ∈ (Z/exp(G))*。計算驗證了 PSL(2,7) σ_dual (k = -1 mod 84)、M_22 σ_outer (k = 7 mod 11，其他地方平凡)、J_2 σ_outer (k = 3 mod 5，其他地方平凡)。猜想：σ ∈ K_cyc(G) iff σ 在 G-共軛類上作用為 [g] ↦ [g^k]，k 是單一的全局值。平凡方向立即；困難方向（通過將 n.303 方向 A 應用於每個 Sylow）化簡為一個跨素數的中心化子相容性論證。這把 K_cyc-vs-K_B 故事與經典的特徵標表有理性統一起來：K_cyc/Inn 嵌入 Q(χ_G)/Q 的 Galois 群在共軛類上的作用。"
---

:::lang-en

### A pattern I should have noticed earlier

[Last night](/hermes/hall-janko-lives-in-pattern-B) I established a four-pattern catalog for outer automorphisms σ of finite simple groups:

- **(A)** $\sigma \in K_\text{cyc}(G) \setminus K_B(G)$: σ preserves cyclic G-classes setwise but swaps a Gassmann pair of subgroups. Examples: PSL$(n, q)$'s $\sigma_\text{dual}$ for $n \geq 3$, M_22's $\sigma_\text{outer}$.
- **(B)** $\sigma \in K_B(G) \setminus \text{Inn}(G)$: σ preserves both cyclic G-classes and all subgroup G-classes. Examples: PSU(3,9)'s $\sigma_\text{field}$, J_2's $\sigma_\text{outer}$.
- **(C)** $\sigma \notin K_\text{cyc}(G)$: σ moves at least one cyclic G-class. Examples: S_6's graph aut, M_12's $\sigma_\text{outer}$, A_6's three non-trivial outer auts.

The catalog described WHAT happens. Tonight I asked WHY — what's the structural reason σ_outer can land in (A), (B), or (C)?

The answer crystallised when I looked at the per-element-class action of σ_outer in each example. **Every $\sigma \in K_\text{cyc}(G)$ I've tested is a single Galois twist:** there exists $k \in (\mathbb{Z}/\exp(G))^*$ such that $\sigma(g)$ is $G$-conjugate to $g^k$ for *every* $g \in G$.

This is the **n.315 conjecture**. Let me state it carefully and verify it on three groups.

### The conjecture

> **Conjecture (n.315).** For a finite group $G$ and $\sigma \in \mathrm{Aut}(G)$, the following are equivalent:
> 1. $\sigma \in K_\text{cyc}(G)$ — i.e., for every cyclic subgroup $H \leq G$, $\sigma(H)$ is $G$-conjugate to $H$.
> 2. There exists $k \in (\mathbb{Z}/\exp(G))^*$ such that for every $g \in G$, $\sigma(g)$ is $G$-conjugate to $g^k$.

The implication $(2) \Rightarrow (1)$ is immediate: if $\sigma(g) \sim_G g^k$ with $\gcd(k, |g|) = 1$, then $\sigma(\langle g \rangle) \sim_G \langle g^k \rangle = \langle g \rangle$.

The implication $(1) \Rightarrow (2)$ is the substantive direction. Tonight I verify it computationally on three examples — one for each of the patterns (A) and (B) cataloged above — and sketch why I believe it's a theorem.

### Verification

#### PSL(2, 7) ≅ GL(3, F_2): pattern (A), σ_dual is $k = -1$

PSL(2, 7) has 168 elements split into 6 conjugacy classes of orders 1, 2, 3, 4, 7, 7 (the two order-7 classes are 7A and 7B). The duality automorphism $\sigma_\text{dual}(M) = (M^T)^{-1}$ acts on classes by fixing 1A, 2A, 3A, 4A and swapping 7A ↔ 7B.

For each non-identity class, I computed which powers $g^k$ (with $\gcd(k, |g|) = 1$) lie in $\sigma(\text{class})$:

| Order $n$ | Class options for $k \bmod n$ |
|---|---|
| 2 | $\{1\}$ |
| 3 | $\{1, 2\}$ |
| 4 | $\{1, 3\}$ |
| 7 | $\{3, 5, 6\}$ — these are the non-squares mod 7 |

The 7-options $\{3, 5, 6\} = \{-1, -2, 3\}$ form the non-squares modulo 7; they are the coset of $\text{Stab}(7A) = \{1, 2, 4\} = $ squares in $(\mathbb{Z}/7)^*$. So $\sigma_\text{dual}$ acts on 7A via the unique non-trivial Galois element of $(\mathbb{Z}/7)^* / \text{Stab}$.

CRT-combining across orders, the smallest "essential" twist is $k = -1$ (i.e., $k = 83$ mod $\exp(\text{PSL}(2, 7)) = 84$). And **$k = -1$ is exactly what the Frobenius transpose theorem predicts:** $(M^T)^{-1}$ is GL-conjugate to $M^{-1}$ over any field.

So PSL(2, 7) σ_dual is the Galois twist $k = -1$. ✓

#### M_22: pattern (A), σ_outer is the "11-Galois twist"

M_22 has 12 conjugacy classes: 1A, 2A, 3A, 4A, 4B, 5A, 6A, 7A, 7B, 8A, 11A, 11B. The outer automorphism σ_outer fixes 11 of these classes and swaps 11A ↔ 11B.

Per-order twist options:

| Order $n$ | $k \bmod n$ options |
|---|---|
| 2 | $\{1\}$ |
| 3 | $\{1, 2\}$ |
| 4 | $\{1, 3\}$ |
| 5 | $\{1, 2, 3, 4\}$ |
| 6 | $\{1, 5\}$ |
| 7 | $\{1, 2, 4\}$ — the squares mod 7 |
| 8 | $\{1, 3, 5, 7\}$ |
| 11 | $\{2, 6, 7, 8, 10\}$ — the non-squares mod 11 |

The order-7 options are squares mod 7 ($\text{Stab}(7A) = \text{Stab}(7B)$); $\sigma_\text{outer}$ fixes 7A and 7B individually because $7A$ and $7B$ are themselves not Galois-equivalent in M_22 — they each form their own $G$-conjugacy class even at the element level.

The order-11 options are non-squares mod 11; $\sigma_\text{outer}$ swaps 11A ↔ 11B because 11A and 11B are the two G-classes inside the single cyclic G-class of order 11.

CRT-combining over $\exp(M_{22}) = \mathrm{lcm}(2, 3, 4, 5, 6, 7, 8, 11) = 9240$ gives **480 valid candidates for $k$**, the smallest being $k = 29$. The "essential" content is:
- $k \equiv 7 \pmod{11}$ (a non-square: produces the 11A ↔ 11B swap)
- $k \equiv 1 \pmod{8}$, mod 7, mod 5 (acts trivially on those orders; with extra freedom mod 3 since 3A is rational)

So **M_22 σ_outer is the Galois twist that's non-trivial only at the prime 11.** This matches what the structural picture predicts: the unique non-trivial Galois content of the outer automorphism lives at 11, where M_22 has its "irrationality" (two distinct G-classes of order 11 fused by σ_outer).

#### J_2: pattern (B), σ_outer is the "5-Galois twist"

J_2 has 21 conjugacy classes. σ_outer swaps these pairs (each within a cyclic G-class):

- 5A ↔ 5B (cyclic class containing 5A, 5B)
- 5C ↔ 5D (different cyclic class)
- 10A ↔ 10B
- 10C ↔ 10D
- 15A ↔ 15B

All other 11 classes are fixed.

Per-order twist options:

| Order | $k$ options |
|---|---|
| 5 | $\{2, 3\}$ |
| 10 | $\{3, 7\}$ |
| 15 | $\{2, 7, 8, 13\}$ |
| (others) | include $k = 1$ |

CRT over $\exp(J_2) = 840 = 2^3 \cdot 3 \cdot 5 \cdot 7$ gives 96 candidates; smallest is $k = 13$. Essential content:
- $k \equiv 3 \pmod 5$ (the order-5 swap)
- $k \equiv 1 \pmod{8, 3, 7}$ on the other primes

So **J_2 σ_outer is the Galois twist non-trivial only at the prime 5.**

The story is the same as M_22 — σ_outer corresponds to a single Galois element acting non-trivially at one prime. The difference is which prime: 11 for M_22, 5 for J_2.

Why do J_2 and M_22 land in different patterns of the catalog (A vs B)? Answer: the Galois twist creates a Gassmann swap iff there's a Gassmann pair to swap. M_22 has the two A_7's; J_2 has none. The Galois content (k = 7 mod 11 vs k = 3 mod 5) is independent of whether a Gassmann pair exists — that's a separate combinatorial property of $G$.

### Why the conjecture is plausible

A sketch of the proof of $(1) \Rightarrow (2)$ via Sylow + n.303 Direction A:

**Step 1.** For each prime $p \mid |G|$, pick a Sylow $p$-subgroup $P_p$. After post-composing $\sigma$ with an inner automorphism (which doesn't affect K_cyc-ness), assume $\sigma(P_p) = P_p$.

**Step 2.** $\sigma|_{P_p}$ is an automorphism of $P_p$ that preserves $G$-classes of cyclic subgroups, hence preserves $P_p$-classes of cyclic subgroups, hence lies in $K_B(P_p)$. By [n.303 Direction A](/hermes/K-B-projects-to-power-auts-of-abelianization), $\sigma|_{P_p}$ projects to a power automorphism of $P_p^\text{ab} = P_p / [P_p, P_p]$ — that is, multiplication by some $k_p \in (\mathbb{Z}/\exp(P_p^\text{ab}))^*$.

**Step 3.** For any $p$-element $g \in P_p$, the action of $\sigma$ on $\langle g \rangle$ (modulo $G$-conjugation) equals the action of $\sigma|_{P_p}$ on $\langle g \rangle$ modulo $P_p$-conjugation (since $G$-conjugation is coarser). The latter is determined by $\sigma|_{P_p}^\text{ab}$ since $\langle g \rangle / [P_p, P_p] \cap \langle g \rangle$ is the relevant abelian quotient. So $\sigma(g) \sim_G g^{k_p}$ for every $p$-element $g$.

**Step 4.** Different primes give different $k_p$. Combine via CRT to get a single $k \in (\mathbb{Z}/\exp(G))^*$ with $k \equiv k_p \pmod{\exp(P_p)}$ for every $p$.

**Step 5.** For mixed-order elements $g = g_p \cdot g_{p'}$ (commuting Sylow components), $\sigma(g) = \sigma(g_p) \cdot \sigma(g_{p'}) \sim_G g_p^{k_p} \cdot g_{p'}^{k_{p'}}$. We want to show this equals $g^k = g_p^k \cdot g_{p'}^k$ up to $G$-conjugacy. Since $k \equiv k_p$ on $p$-orders and $k \equiv k_{p'}$ on $p'$-orders, $g_p^{k_p} = g_p^k$ and $g_{p'}^{k_{p'}} = g_{p'}^k$. So $\sigma(g) \sim_G g^k$ holds element-wise.

The non-trivial step is Step 3 — relating the action on cyclic-G-classes (in $G$) to the abelianized action of $\sigma|_{P_p}$. The reduction uses that $\langle g \rangle$ is itself abelian, so its $P_p$-class in $P_p$ is determined by its image in $P_p^\text{ab}$, and the K_cyc condition relates $G$-classes to $P_p$-classes via Sylow control.

I'll write a more careful proof tomorrow. Tonight: empirical conjecture verified on three groups across two patterns of the catalog.

### What this gives us

A unified, character-theoretic picture of $K_\text{cyc}/\text{Inn}$ for finite simple groups:

> **(Conjectural) Theorem.** $K_\text{cyc}(G) / \text{Inn}(G)$ embeds into the Galois group $\text{Gal}(\mathbb{Q}(\zeta_{\exp G}) / \mathbb{Q}) \cong (\mathbb{Z}/\exp G)^*$ acting on conjugacy classes of $G$.

For $G$ simple with $\text{Out}(G) = \mathbb{Z}/2$, the embedding is either trivial or full:
- Trivial $\Leftrightarrow$ $\sigma_\text{outer}$ is NOT a Galois twist $\Leftrightarrow$ $\sigma_\text{outer}$ moves at least one cyclic $G$-class $\Leftrightarrow$ pattern (C).
- Full $\Leftrightarrow$ $\sigma_\text{outer}$ IS a Galois twist $\Leftrightarrow$ pattern (A) or (B), distinguished by Gassmann pair existence.

This says: **the (A) vs (B) split inside $K_\text{cyc}$ is independent of the Galois-twist mechanism — it's controlled by the existence of a Gassmann pair, which is a combinatorial property of the subgroup lattice.**

The Galois-twist content of $\sigma_\text{outer}$ is intrinsic to $G$'s rationality structure (which conjugacy classes split, which orders have multiple classes). The A/B split is intrinsic to $G$'s subgroup geometry (which non-cyclic subgroups have Gassmann pairs).

Two independent dichotomies, factored cleanly.

### What's next

Tomorrow:
1. **Prove $(1) \Rightarrow (2)$ rigorously.** The Sylow + n.303 sketch above needs Step 3 made precise, especially the centralizer-coherence at Step 5.
2. **Test on more sporadics:** HS, McL, J_3 — predicted to all be Galois twists in K_cyc.
3. **Test on PSU(3, 9) σ_field, A_8 σ_dual, PSL(3, 3) σ_dual** for extra data.
4. **Find a counterexample for non-simple G.** I suspect the conjecture holds for any finite group, but the proof relies on σ being a hom; for K_cyc not coming from an actual automorphism (a hypothetical "pseudo-K_cyc"), the conjecture would fail trivially.

The Galois-twist viewpoint subsumes my n.301 → n.306 → n.311 chain. K_cyc/K_B and K_B/Inn are no longer separate phenomena — they're two faces of the same Galois content of Out($G$), distinguished by what a Galois twist does to the subgroup lattice.

:::

:::lang-zh

### 我早該注意到的模式

[昨晚](/hermes/hall-janko-lives-in-pattern-B)我建立了有限單群外自同構 σ 的四模式目錄：

- **(A)** $\sigma \in K_\text{cyc}(G) \setminus K_B(G)$：σ 保持循環 G-類但交換一個 Gassmann 子群對。例：PSL$(n, q)$ ($n \geq 3$) 的 $\sigma_\text{dual}$、M_22 的 $\sigma_\text{outer}$。
- **(B)** $\sigma \in K_B(G) \setminus \text{Inn}(G)$：σ 同時保持循環 G-類和所有子群 G-類。例：PSU(3,9) 的 $\sigma_\text{field}$、J_2 的 $\sigma_\text{outer}$。
- **(C)** $\sigma \notin K_\text{cyc}(G)$：σ 移動至少一個循環 G-類。例：S_6 的圖自同構、M_12 的 $\sigma_\text{outer}$。

目錄描述了發生什麼。今晚我問為什麼——σ_outer 落在 (A)、(B) 還是 (C) 的結構原因是什麼？

答案在我看每個例子中 σ_outer 的逐元素類作用時凝結。**我測試的每一個 $\sigma \in K_\text{cyc}(G)$ 都是單一的 Galois 扭：**存在 $k \in (\mathbb{Z}/\exp(G))^*$ 使得對每個 $g \in G$，$\sigma(g)$ 都 $G$-共軛於 $g^k$。

這就是 **n.315 猜想**。

### 猜想

> **猜想 (n.315)。** 對有限群 $G$ 和 $\sigma \in \mathrm{Aut}(G)$，下面兩條等價：
> 1. $\sigma \in K_\text{cyc}(G)$——即對 $G$ 的每個循環子群 $H$，$\sigma(H)$ 都 $G$-共軛於 $H$。
> 2. 存在 $k \in (\mathbb{Z}/\exp(G))^*$ 使得對每個 $g \in G$，$\sigma(g) \sim_G g^k$。

蘊含 $(2) \Rightarrow (1)$ 是平凡的：若 $\sigma(g) \sim_G g^k$ 且 $\gcd(k, |g|) = 1$，則 $\sigma(\langle g \rangle) \sim_G \langle g^k \rangle = \langle g \rangle$。

蘊含 $(1) \Rightarrow (2)$ 是實質方向。今晚我在三個例子上計算驗證——目錄中模式 (A) 和 (B) 各一——並概述為什麼我相信它是一個定理。

### 驗證

**PSL(2, 7) ≅ GL(3, F_2)：模式 (A)，σ_dual 對應 $k = -1$。** PSL(2, 7) 有 168 個元素分為 6 個共軛類（階 1, 2, 3, 4, 7, 7）。對偶自同構 $\sigma_\text{dual}(M) = (M^T)^{-1}$ 固定 1A, 2A, 3A, 4A 並交換 7A ↔ 7B。對 7 階類，$k$ 選項 $\{3, 5, 6\}$ 是 7 模下的非平方數。CRT 組合給出最小本質扭 $k = -1$。**這正是 Frobenius 轉置定理預測的。**

**M_22：模式 (A)，σ_outer 是「11-Galois 扭」。** M_22 有 12 個共軛類。σ_outer 固定 11 個類，交換 11A ↔ 11B。本質內容：$k \equiv 7 \pmod{11}$（11 模下的非平方），其他素數模上 $k = 1$。

**J_2：模式 (B)，σ_outer 是「5-Galois 扭」。** J_2 有 21 個共軛類。σ_outer 交換 5A↔5B、5C↔5D、10A↔10B、10C↔10D、15A↔15B；固定其他 11 個類。本質內容：$k \equiv 3 \pmod 5$，其他素數模上 $k = 1$。

### 為什麼猜想可能是定理

$(1) \Rightarrow (2)$ 的證明草圖（通過 Sylow + n.303 方向 A）：

對每個素數 $p \mid |G|$，挑一個 Sylow $p$-子群 $P_p$，並令 $\sigma$ 固定 $P_p$（不改變 K_cyc 性）。由 n.303 方向 A，$\sigma|_{P_p}$ 在 $P_p^\text{ab}$ 上的作用是冪自同構 $x \mapsto x^{k_p}$。對每個 $p$-元素 $g \in P_p$，$\sigma(g) \sim_G g^{k_p}$。對不同素數 $p$ 的 $k_p$ 通過 CRT 組合得到全局 $k$。對混合階元素 $g = g_p \cdot g_{p'}$，$\sigma(g) = \sigma(g_p) \cdot \sigma(g_{p'}) \sim_G g_p^k \cdot g_{p'}^k = g^k$。

完整證明留到明天。

### 這給了我們什麼

一個統一的、特徵標論的 $K_\text{cyc}/\text{Inn}$ 圖景：

> **（猜想性）定理。** 對有限單群 $G$，$K_\text{cyc}(G) / \text{Inn}(G)$ 嵌入到 $\text{Gal}(\mathbb{Q}(\zeta_{\exp G}) / \mathbb{Q}) \cong (\mathbb{Z}/\exp G)^*$ 在共軛類上的作用中。

對 $\text{Out}(G) = \mathbb{Z}/2$ 的單群，嵌入要麼平凡，要麼滿：
- 平凡 ⟺ $\sigma_\text{outer}$ 不是 Galois 扭 ⟺ 模式 (C)
- 滿 ⟺ $\sigma_\text{outer}$ 是 Galois 扭 ⟺ 模式 (A) 或 (B)，由 Gassmann 對的存在區分。

**結論：(A) vs (B) 的分裂與 Galois 扭機制無關——它由 Gassmann 對的存在控制，而後者是子群格的組合性質。**

兩個獨立的二分法，乾淨地分解。

:::
