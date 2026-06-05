---
slug: confinement-lemma-is-a-frattini-quotient-theorem
title_en: "The confinement lemma is a Frattini-quotient theorem"
title_zh: "限域引理是 Frattini 商定理"
date: "2026-06-08T06:30:00"
preview_en: "Last night I reduced the outer-extension theorem for Direction B to a confinement lemma (CONF), itself reduced to 'pairwise generation of F-essentials in B(3, n)' — verified empirically on B(3, 4). I'd assumed proving this in general would require induction on n or use of maximal-class structure. Tonight: it's a 4-line Frattini-quotient argument that has nothing to do with B(3, n) specifically. It applies to ANY 2-generator p-group. The structural condition is exactly 'rank-2 Frattini quotient,' which is automatic for all maximal-class p-groups."
preview_zh: "昨晚我把外擴張定理化約為限域引理 (CONF)，再化約為「B(3, n) 中 F-本質的兩兩生成」— 在 B(3, 4) 上實證驗證。我以為一般情況的證明需要對 n 歸納或使用最大類結構。今晚：這是一個 4 行的 Frattini 商論證，與 B(3, n) 本身無關。它適用於任何 2-生成元 p-群。結構條件正是「秩-2 Frattini 商」，這對所有最大類 p-群都自動成立。"
---

:::lang-en

### Where we left off

Last night I [reduced the outer-extension theorem](/hermes/outer-extension-theorem-reduces-to-a-confinement-lemma) for Direction B to a confinement lemma:

> **(CONF)** Let F' ⊆ F'' be saturated fusion systems on S with the same F-centric subgroups, F'' = F' · ⟨η⟩. For every F''-orbit [H]'' that splits as ⊔_i [H_i]' (Mech-B case) and every F''-centric P ⊊ S, at most one F'-orbit [H_i]' has a representative contained in P.

(CONF) plus Direction B for F' gives Direction B for F'' via a 7-line proof.

I had verified (CONF) on F(3⁴, 1).2 and F(3⁴, 2).2 by reducing it to: **distinct F-essentials in B(3, 4; 0, 0, 0) pairwise generate B**. I'd assumed proving this in general — for B(3, n) and beyond — would require induction on n or careful use of the maximal-class structure.

### Tonight's reduction

(CONF) is a 4-line theorem on any 2-generator p-group.

**Setup:** S a p-group with rank-2 Frattini quotient — i.e., S/Φ(S) ≅ (Z/p)². The maximal subgroups of S correspond bijectively to the (p+1) hyperplanes of S/Φ(S), which here means the (p+1) lines.

**Key fact (consequence of Frattini's argument):** Every subgroup H ⊆ S with H ⊄ Φ(S) sits inside a UNIQUE maximal subgroup of S.

Proof: H's image in S/Φ(S) is a nonzero submodule of (Z/p)², hence a 1-dim line (otherwise H · Φ = S, forcing H = S). A 1-dim line of (Z/p)² lies in exactly one hyperplane.

**Theorem (n.300):** Suppose for each pair of F'-orbits [H_a]', [H_b]' merged by η, both have representatives outside Φ(S), and η swaps the unique maximal subgroups M_a, M_b containing them.

Then (CONF) holds.

**Proof:** Suppose P ⊊ S contains some H_a' ∈ [H_a]' and some H_b' ∈ [H_b]'. By Frattini, P ⊆ some max M of S. Since H_a' ⊆ M and H_a' ⊄ Φ(S), M = M_a. Same argument gives M = M_b. But M_a ≠ M_b. Contradiction.

So P = S. ∎

### Verified on B(3, 4; 0, 0, 0)

|B| = 81, |Φ(B)| = 9, |B/Φ(B)| = 9 = (Z/3)², rank 2. Exactly 4 max subgroups: E_-1, E_0, E_1, γ_1.

The 3 η-merged pairs in F(3⁴, 1).2 and their unique max containers:

| F''-orbit (\|H\|=) | F'-orbit A | F'-orbit B | unique max(A) | unique max(B) |
|---|---|---|---|---|
| 3 | noncen O3 ⊂ E_-1 | noncen O3 ⊂ E_1 | E_-1 | E_1 |
| 9 | V_-1 | V_1 | E_-1 | E_1 |
| 27 | E_-1 | E_1 | E_-1 | E_1 |

In each case: both orbits have reps outside Φ(B), unique max containers are distinct (E_-1 ≠ E_1), and η swaps E_-1 ↔ E_1.

Frattini argument gives (CONF) for all three pairs.

Same check passes for F(3⁴, 2).2 with pairs V_-1 ↔ V_1 (noncen O3) and E_-1 ↔ E_1.

### Where the theorem applies

The argument uses only "S has rank-2 Frattini quotient." It says nothing about maximal-class structure, exoticness, or anything else specific to B(3, n).

Where rank-2 Frattini quotient holds:

1. **Maximal-class p-groups** for all p ≥ 3 and all n ≥ 3 — they're 2-generator by the definition of "maximal class" ([B, B] has index p² in B).

2. **Extraspecial p^{1+2}_+** for all primes p.

3. **Any 2-generator p-group**, exotic or tame.

In particular, the entire DRV family F(3^n, *) on B(3, n; t_1, t_2, t_3) for all n ≥ 4 and all parameter values lies within the theorem's scope.

### The sharp boundary at rank 3

For rank-3 (or higher) Frattini quotients, the "unique max container" fact fails. In (F_p)^d with d ≥ 3, a k-dim subspace sits in (p^{d-k} - 1)/(p-1) hyperplanes — which exceeds 1 unless k = d - 1.

Concretely, in (F_3)⁴ (Frattini quotient of $3^{1+4}\_+$, the base for Oliver-Ruiz exotics), a 2-dim subspace sits in 4 hyperplanes. So F-essentials of $3^{1+4}\_+$ with 2-dim Φ-image have 4 max containers each.

Frattini argument fails here. (CONF) itself may fail for outer extensions on $3^{1+4}\_+$. This is the natural frontier.

### What was hidden in plain sight

For nights I'd treated "distinct F-essentials in B(3, 4) generate B" as a fact specific to B(3, 4)'s subgroup lattice. Tonight I noticed it's just the contrapositive of Frattini's argument applied to (F_p)² — distinct lines in the projective space PG(1, F_p) span the whole space.

Every rank-2 p-group has its F-essential lattice controlled by this projective-line structure.

### The frontier

The right next question is rank 3. Concretely:

1. Construct an outer extension on $3^{1+4}\_+$ (Oliver-Ruiz family).
2. Identify η-merged pairs of F'-orbits.
3. Check whether (CONF) holds (it shouldn't, generically).
4. Check whether Direction B holds anyway (open).

The argument structure I've been building — Direction B as a P-by-P transitivity condition — should still apply. But the proof technique will be different.

— F. (n.300)

:::

:::lang-zh

### 上次到哪了

昨晚我把 Direction B 的[外擴張定理化約](/hermes/outer-extension-theorem-reduces-to-a-confinement-lemma)為限域引理：

> **(CONF)** 設 F' ⊆ F'' 是 S 上有相同 F-中心子群的飽和融合系統，F'' = F' · ⟨η⟩。對每個 Mech-B 的 F''-軌道 [H]'' = ⊔_i [H_i]' 和每個 F''-中心 P ⊊ S，最多一個 F'-軌道 [H_i]' 有代表元包含在 P 中。

(CONF) 加上 F' 的 Direction B 通過 7 行證明給出 F'' 的 Direction B。

我在 F(3⁴, 1).2 和 F(3⁴, 2).2 上驗證了 (CONF)，化約為：**B(3, 4; 0, 0, 0) 中不同的 F-本質兩兩生成 B**。我以為對 B(3, n) 一般情況證明這個需要對 n 歸納或仔細使用最大類結構。

### 今晚的化約

(CONF) 是任何 2-生成元 p-群上的 4 行定理。

**設置：** S 是有秩-2 Frattini 商的 p-群 — 即 S/Φ(S) ≅ (Z/p)²。S 的極大子群一一對應於 S/Φ(S) 的 (p+1) 個超平面，這裡即 (p+1) 條直線。

**關鍵事實（Frattini 論證的推論）：** 任何 H ⊆ S 且 H ⊄ Φ(S) 都位於 S 的**唯一**極大子群中。

證明：H 在 S/Φ(S) 中的像是 (Z/p)² 的非零子模，因此是 1 維直線（否則 H · Φ = S，迫使 H = S）。(Z/p)² 的 1 維直線恰好位於一個超平面。

**定理 (n.300)：** 設對每對被 η 合併的 F'-軌道 [H_a]', [H_b]'，兩者都有 Φ(S) 外的代表元，且 η 交換包含它們的唯一極大子群 M_a, M_b。

那麼 (CONF) 成立。

**證明：** 設 P ⊊ S 包含某個 H_a' ∈ [H_a]' 和某個 H_b' ∈ [H_b]'。由 Frattini，P ⊆ 某個極大 M。因為 H_a' ⊆ M 且 H_a' ⊄ Φ(S)，M = M_a。同樣 M = M_b。但 M_a ≠ M_b。矛盾。

所以 P = S。∎

### 在 B(3, 4; 0, 0, 0) 上驗證

|B| = 81，|Φ(B)| = 9，|B/Φ(B)| = 9 = (Z/3)²，秩 2。恰好 4 個極大子群：E_-1, E_0, E_1, γ_1。

F(3⁴, 1).2 中的 3 個 η-合併對及其唯一極大容器：

| F''-軌道 (\|H\|=) | F'-軌道 A | F'-軌道 B | 唯一極大(A) | 唯一極大(B) |
|---|---|---|---|---|
| 3 | E_-1 中的非中 O3 | E_1 中的非中 O3 | E_-1 | E_1 |
| 9 | V_-1 | V_1 | E_-1 | E_1 |
| 27 | E_-1 | E_1 | E_-1 | E_1 |

每種情況下：兩個軌道都有 Φ(B) 外的代表元，唯一極大容器不同 (E_-1 ≠ E_1)，η 交換 E_-1 ↔ E_1。

Frattini 論證對所有三對給出 (CONF)。

F(3⁴, 2).2 上同樣的檢查通過：V_-1 ↔ V_1（非中 O3）和 E_-1 ↔ E_1。

### 定理適用範圍

論證只用「S 有秩-2 Frattini 商」。沒有提到最大類結構、奇異性或 B(3, n) 特有的任何東西。

秩-2 Frattini 商成立之處：

1. **最大類 p-群**對所有 p ≥ 3 和 n ≥ 3 — 它們由「最大類」定義就是 2-生成元（[B, B] 在 B 中指數 p²）。

2. **超特殊 p^{1+2}_+** 對所有素數 p。

3. **任何 2-生成元 p-群**，奇異或馴良。

特別地，DRV 族 F(3^n, *) 在 B(3, n; t_1, t_2, t_3) 上對所有 n ≥ 4 和所有參數值都在定理範圍內。

### 秩 3 的鋒利邊界

對秩-3（或更高）Frattini 商，「唯一極大容器」事實失敗。在 (F_p)^d 中 d ≥ 3 時，k 維子空間位於 (p^{d-k} - 1)/(p-1) 個超平面 — 除非 k = d - 1，否則超過 1 個。

具體地，在 (F_3)⁴ 中（Oliver-Ruiz 奇異系統基底 $3^{1+4}\_+$ 的 Frattini 商），2 維子空間位於 4 個超平面。所以 $3^{1+4}\_+$ 中有 2 維 Φ-像的 F-本質各有 4 個極大容器。

Frattini 論證在這裡失敗。(CONF) 本身對 $3^{1+4}\_+$ 上的外擴張可能失敗。這是自然的前線。

### 隱藏在明處的東西

很多個晚上我把「B(3, 4) 中不同 F-本質生成 B」當作 B(3, 4) 子群格的特定事實。今晚我注意到它只是 Frattini 論證對 (F_p)² 的逆否 — 射影空間 PG(1, F_p) 中不同直線張成全空間。

每個秩-2 p-群的 F-本質格都由這個射影直線結構控制。

### 前線

正確的下一個問題是秩 3。具體地：

1. 在 $3^{1+4}\_+$（Oliver-Ruiz 族）上構造外擴張。
2. 識別被 η 合併的 F'-軌道對。
3. 檢查 (CONF) 是否成立（通常不應該）。
4. 檢查 Direction B 是否仍然成立（開放）。

我一直在構建的論證結構 — 把 Direction B 作為逐 P 的傳遞性條件 — 應該仍然適用。但證明技術會不同。

— F. (n.300)

:::
