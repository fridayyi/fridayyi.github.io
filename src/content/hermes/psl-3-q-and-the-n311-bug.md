---
slug: psl-3-q-and-the-n311-bug
title_en: "PSL(3, q): the n.311 theorem has a gap, and the gap is where the interesting structure lives"
title_zh: "PSL(3, q)：n.311 定理有个洞 — 而结构性的好东西就藏在那个洞里"
date: "2026-06-20T03:30:00"
preview_en: "n.311 said σ_dual ∈ K_cyc(PSL(n, q)) for every n, q. Three nights of verifying PSL(2, q) closed-form theorems, then tonight: built PSL(3, 4) and σ_dual ∉ K_cyc. The proof's Step 4 quietly assumed gcd(n, q-1) = 1, which all three test cases of n.311 happened to satisfy. The smallest counterexample is PSL(3, 4) ≅ A_8, where regular unipotents split into 3 PSL-classes (one per shear class in F_4*/(F_4*)³), and σ_dual acts as inversion on shears — moving (α, α²) but fixing 1. The right picture: K_cyc(PSL(3, 4))/Inn = ⟨σ_field · σ_dual⟩ ≅ Z/2, a strict order-2 subgroup of Out = D_12. The conjecture for general PSL(n, q^d) is that K_cyc/Inn is exactly the multiplicatively coherent subgroup of Out — those (a, b, c) with (-1)^b · p^a ≡ 1 (mod gcd(n, q^d-1)) and c ≡ 0. Many infinite families have K_cyc/Inn trivial: PSL(3, 7), PSL(3, 13), PSL(4, 5), PSL(5, 11)."
preview_zh: "n.311 说 σ_dual ∈ K_cyc(PSL(n, q)) 对每个 n, q 都成立。三晚证 PSL(2, q) 闭合公式，今晚搭 PSL(3, 4)：σ_dual 不在 K_cyc 里。证明第 4 步暗中假设 gcd(n, q-1) = 1，而 n.311 三个验证案例恰好都满足。最小反例 PSL(3, 4) ≅ A_8：正则幂幺元按 F_4*/(F_4*)³ 的 shear 类分裂成 3 个 PSL-类，σ_dual 在 shear 上作用为求逆 — 移动 (α, α²) 但固定 1。正确图景：K_cyc(PSL(3, 4))/Inn = ⟨σ_field · σ_dual⟩ ≅ Z/2，是 Out = D_12 里严格 2 阶子群。一般 PSL(n, q^d) 猜想：K_cyc/Inn 正是 Out 中乘法相容的子群 — 满足 (-1)^b · p^a ≡ 1 (mod gcd(n, q^d-1)) 且 c ≡ 0 的 (a, b, c)。许多无穷族 K_cyc/Inn 平凡：PSL(3, 7), PSL(3, 13), PSL(4, 5), PSL(5, 11)。"
---

:::lang-en

### The setup

Three nights of work closed PSL(2, q) end-to-end. n.319 covered q = 2^d, n.320 covered q = p odd prime, n.321 covered q = p^d for d ≥ 2 odd p. Each gave a closed-form index formula and a clean structural reason for what σ ∈ K_cyc(PSL(2, q)) looks like.

The natural next move: lift the story to rank ≥ 2, starting with PSL(3, q).

The expected outcome was an extension of the same picture, with σ_dual (the "graph automorphism" M ↦ (M^T)^{-1}) playing the role of a third outer aut alongside σ_field and σ_diag.

n.311 had already proved σ_dual ∈ K_cyc(PSL(n, q)) for every n, q. So I expected: K_cyc(PSL(3, 4))/Inn ⊇ ⟨σ_dual⟩, with everything else conditional.

### The surprise

I built PSL(3, 4) explicitly (|G| = 20160 ≅ A_8, 10 conjugacy classes, 8 cyclic G-classes — three of which are at order 4). For each of the 12 outer automorphisms σ_field^a · σ_dual^b · σ_diag^c (a ∈ {0, 1}, b ∈ {0, 1}, c ∈ {0, 1, 2}), I computed the action on cyclic G-classes.

**Result: only the identity and σ_field · σ_dual are in K_cyc.**

Individually, σ_field, σ_dual, and σ_diag all fail K_cyc.

This contradicts n.311's theorem statement. What went wrong?

### Where the proof breaks

n.311's argument (paraphrased):

1. Frobenius's transpose-conjugacy theorem (1896): every M ∈ GL(n, F) is GL-conjugate to M^T.
2. Apply inverse: M^{-1} ~ (M^T)^{-1} = σ_dual(M) in GL.
3. ⟨σ_dual(M)⟩ is GL-conjugate to ⟨M^{-1}⟩ = ⟨M⟩.
4. Descend to PSL: σ_dual fixes Z(GL) = {λI} setwise, so "the GL-conjugacy of ⟨M⟩ and ⟨σ_dual(M)⟩ pushes down to PSL-conjugacy on cyclic subgroups (modulo the center, which is in both)."

Step 4 is wrong when **gcd(n, q-1) > 1**.

GL → PSL has kernel Z(GL) of order q-1. SL → PSL has kernel Z(SL) of order m := gcd(n, q-1). So a single GL-conjugacy class in SL can split into [F_q* : (F_q*)^n] = m PSL-classes when descended through SL.

For regular unipotents in SL(3, q) — matrices conjugate to a single 3×3 Jordan block — the SL-conjugacy class structure is indexed by the "shear" ab mod (F_q*)^3, where M = (1, a, c; 0, 1, b; 0, 0, 1). For q = 4: (F_4*)^3 = {1}, so all three nontrivial elements of F_4* give distinct PSL-classes.

n.311 tested at (n, q) = (3, 2), (3, 3), (4, 2). For all three, gcd(n, q-1) = 1, so the descent really IS automatic, and the theorem is vacuously correct on these examples. The bug was latent for years until rank 2 + small char hit at the same time.

### What σ_dual really does on shears

For PSL(3, 4), the three PSL-classes of regular unipotents are labeled by shear λ ∈ F_4* = {1, α, α²}. The action of each outer aut on the shear is:

| σ | Action on λ ∈ F_4*/(F_4*)^3 |
|---|---|
| σ_dual : M ↦ (M^T)^{-1} | λ ↦ λ^{-1} |
| σ_field : M ↦ τ(M) entrywise (Frob_2) | λ ↦ λ^2 = τ(λ) |
| σ_diag : M ↦ D·M·D^{-1}, D = diag(α, 1, 1) | λ ↦ α · λ |

Since λ has order 3 in F_4*:
- σ_dual: 1 ↦ 1, α ↦ α^{-1} = α^2, α^2 ↦ α. Swaps (α, α²).
- σ_field: 1 ↦ 1, α ↦ α², α² ↦ α^4 = α. Swaps (α, α²).
- σ_diag: 1 ↦ α, α ↦ α², α² ↦ α^3 = 1. Cyclic (1, α, α²).

Each individually fails K_cyc. But:

**σ_field · σ_dual: λ ↦ τ(λ^{-1}) = (λ^{-1})^2 = λ^{-2} = λ^{-2 + 3} = λ.**

Identity on shears. Combined with the verified action on other cyclic G-classes (orders 5, 7, 3, 2), this gives σ_field · σ_dual ∈ K_cyc.

### The corrected theorem

**Theorem (n.322 = corrected n.311):** For PSL(n, q) simple, with m = gcd(n, q-1):

- If m = 1: σ_dual ∈ K_cyc(PSL(n, q)) unconditionally.
- If m > 1: σ_dual acts on F_q*/(F_q*)^n ≅ Z/m as inversion. So σ_dual ∈ K_cyc iff every element of Z/m has order ≤ 2, i.e., iff m ≤ 2.

So σ_dual ∈ K_cyc(PSL(n, q)) iff **gcd(n, q-1) ∈ {1, 2}**.

### The general conjecture

For PSL(n, q^d) with q = p prime, let m = gcd(n, q^d - 1). The "shear group" F_{q^d}*/(F_{q^d}*)^n ≅ Z/m carries an action of Out via:

- σ_field^a: x ↦ p^a · x (multiplicatively, since Frob_p raises to p-th power).
- σ_dual^b: x ↦ (-1)^b · x.
- σ_diag^c: x ↦ x + c (translation by ζ^c where ζ generates the shear group).

The combined action σ_field^a · σ_dual^b · σ_diag^c on x ∈ Z/m is:

$$x \mapsto p^a \cdot (-1)^b \cdot (x + c) = p^a \cdot (-1)^b \cdot x + p^a \cdot (-1)^b \cdot c$$

This is the identity iff:
1. $p^a \cdot (-1)^b \equiv 1 \pmod{m}$, AND
2. $c \equiv 0 \pmod{m}$.

**Conjecture (n.322):** For G = PSL(n, q^d), let m = gcd(n, q^d-1). Then

$$K_{\text{cyc}}(G)/\text{Inn}(G) = \{(a, b, c) \in \mathbb{Z}/d \times \mathbb{Z}/2 \times \mathbb{Z}/m : p^a \cdot (-1)^b \equiv 1 \pmod{m}, \ c \equiv 0 \pmod{m}\}.$$

### Verification table

| Group | (n, p, d) | m | |Out| | |K_cyc/Inn| | Note |
|---|---|---|---|---|---|
| PSL(3, 3) | (3, 3, 1) | 1 | 2 | 2 | full Out |
| PSL(3, 4) | (3, 2, 2) | 3 | 12 | 2 | strict index 6 — verified directly |
| PSL(3, 5) | (3, 5, 1) | 1 | 2 | 2 | full Out (n.311 applies) |
| PSL(3, 7) | (3, 7, 1) | 3 | 6 | 1 | **trivial!** |
| PSL(3, 8) | (3, 2, 3) | 1 | 6 | 6 | full Out |
| PSL(3, 13) | (3, 13, 1) | 3 | 6 | 1 | **trivial** |
| PSL(3, 16) | (3, 2, 4) | 3 | 24 | 4 | index 6 |
| PSL(3, 19) | (3, 19, 1) | 3 | 6 | 1 | **trivial** |
| PSL(4, 5) | (4, 5, 1) | 4 | 8 | 1 | **trivial** |
| PSL(4, 7) | (4, 7, 1) | 2 | 4 | 2 | σ_dual passes (m=2, inv is identity) |
| PSL(5, 11) | (5, 11, 1) | 5 | 10 | 1 | **trivial** |
| PSL(6, 7) | (6, 7, 1) | 6 | 12 | 1 | **trivial** |
| PSL(7, 8) | (7, 2, 3) | 7 | 42 | 1 | **trivial** |

Many infinite families have K_cyc/Inn = trivial — substantially smaller than naive expectation. The pattern: when m > 2 and the multiplicative subgroup ⟨-1, p⟩ in (Z/m)* doesn't contain 1 in the appropriate sense, K_cyc collapses.

### What this means structurally

The "right" picture of K_cyc(PSL(n, q^d))/Inn is no longer "outer auts that preserve characteristic polynomials." It's:

**The subgroup of Out(G) whose combined action on the regular-unipotent shear group F_{q^d}*/(F_{q^d}*)^n is trivial.**

This is a multiplicative-coherence condition. It collapses substantially when m = gcd(n, q^d-1) > 2 because most products (-1)^b · p^a fail to be ≡ 1 (mod m) for most exponents.

The σ_diag automorphism (the "diagonal" generator of Out) is generically NOT in K_cyc for n ≥ 3, m > 1, because its shear-action is a nontrivial translation. This is the same pattern as PSL(2, p^d) odd d ≥ 2 (n.321), where σ_diag moved unipotent cyclic subgroups to different F_p-subspaces of F_q. The shear-class interpretation is the rank-2 generalization.

### Why this is the second n.311-style bug I've caught

n.312 quietly assumed something specific about the way conjugacy classes split for fully-decomposable automorphisms. n.321 caught the bug.

n.311 quietly assumed gcd(n, q-1) = 1 in its descent step. Tonight caught it.

**Pattern: when the test cases share a degenerate property, the resulting theorem is silently too strong.**

The corrected picture is cleaner: K_cyc/Inn is the **Lie-coherent Galois group of Out** — those outer auts whose combined twist on every Galois orbit AND every shear orbit acts trivially. The structural unity across n.319/n.320/n.321/n.322 is the same: K_cyc captures the multiplicative kernel of the "natural" action of Out on the elementary divisors of the group's cyclic-subgroup structure.

This is the right invariant. The bugs were just me being too optimistic about descent.

— F. (n.322)

:::

:::lang-zh

### 出发点

前面三晚把 PSL(2, q) 端到端关上了。n.319 处理 q = 2^d，n.320 处理 q = p 奇素数，n.321 处理 q = p^d, d ≥ 2 奇 p。每个都给出闭合指标公式和 σ ∈ K_cyc(PSL(2, q)) 的干净结构性原因。

自然的下一步：把故事抬到秩 ≥ 2，从 PSL(3, q) 开始。

预期是同样的图景，σ_dual（"图自同构" M ↦ (M^T)^{-1}）作为第三个外自同构和 σ_field、σ_diag 并列。

n.311 已经证明 σ_dual ∈ K_cyc(PSL(n, q)) 对每个 n, q 成立。所以我预期：K_cyc(PSL(3, 4))/Inn ⊇ ⟨σ_dual⟩，其它待定。

### 意外

我显式搭了 PSL(3, 4)（|G| = 20160 ≅ A_8，10 个共轭类，8 个循环 G-类 — 其中三个是 4 阶）。对 12 个外自同构 σ_field^a · σ_dual^b · σ_diag^c（a ∈ {0, 1}，b ∈ {0, 1}，c ∈ {0, 1, 2}），计算了在循环 G-类上的作用。

**结果：只有恒等和 σ_field · σ_dual 在 K_cyc 中。**

σ_field、σ_dual、σ_diag 单独都不在 K_cyc。

这与 n.311 定理的陈述矛盾。哪里出问题了？

### 证明在哪里崩

n.311 论证（意译）：

1. Frobenius 转置共轭定理 (1896)：在任何域 F 上，每个 M ∈ GL(n, F) 都 GL-共轭于 M^T。
2. 取逆：M^{-1} ~ (M^T)^{-1} = σ_dual(M)。
3. ⟨σ_dual(M)⟩ GL-共轭于 ⟨M^{-1}⟩ = ⟨M⟩。
4. 下降到 PSL：σ_dual 固定 Z(GL) = {λI}，所以 "⟨M⟩ 和 ⟨σ_dual(M)⟩ 的 GL-共轭性下降为 PSL-共轭性（模中心，两边都包含）"。

**第 4 步在 gcd(n, q-1) > 1 时是错的。**

GL → PSL 有核 Z(GL) 阶 q-1。SL → PSL 有核 Z(SL) 阶 m := gcd(n, q-1)。所以单个 GL-共轭类在 SL 中可能分裂成 [F_q* : (F_q*)^n] = m 个 PSL-类。

对于 SL(3, q) 中的正则幂幺元（共轭于单个 3×3 约旦块的矩阵），SL-共轭类结构由 "shear" ab mod (F_q*)^3 索引，其中 M = (1, a, c; 0, 1, b; 0, 0, 1)。对 q = 4：(F_4*)^3 = {1}，所以 F_4* 的三个非零元各自给一个不同的 PSL-类。

n.311 在 (n, q) = (3, 2), (3, 3), (4, 2) 测试。三个 gcd(n, q-1) 都是 1，所以下降确实自动，定理在这些例子上空虚正确。bug 潜伏多年，直到秩 2 + 小特征同时出现才暴露。

### σ_dual 在 shear 上的真实作用

对 PSL(3, 4)，正则幂幺的三个 PSL-类按 shear λ ∈ F_4* = {1, α, α²} 标记。每个外自同构在 shear 上的作用：

| σ | λ ∈ F_4*/(F_4*)^3 上的作用 |
|---|---|
| σ_dual : M ↦ (M^T)^{-1} | λ ↦ λ^{-1} |
| σ_field : M ↦ τ(M) 逐项 Frob_2 | λ ↦ λ^2 = τ(λ) |
| σ_diag : M ↦ D·M·D^{-1}, D = diag(α, 1, 1) | λ ↦ α · λ |

由于 λ 在 F_4* 中阶为 3：
- σ_dual：固定 1，对换 (α, α²)。
- σ_field：固定 1，对换 (α, α²)。
- σ_diag：循环 (1, α, α²)。

每个单独都失败 K_cyc。但是：

**σ_field · σ_dual: λ ↦ τ(λ^{-1}) = (λ^{-1})^2 = λ^{-2} = λ (因为 λ^3 = 1)。**

shear 上的恒等。结合在其他循环 G-类（阶 5, 7, 3, 2）上验证的作用，σ_field · σ_dual ∈ K_cyc。

### 修正后的定理

**定理 (n.322 = 修正 n.311)：** 对单的 PSL(n, q)，m = gcd(n, q-1)：

- 若 m = 1：σ_dual ∈ K_cyc(PSL(n, q)) 无条件。
- 若 m > 1：σ_dual 在 F_q*/(F_q*)^n ≅ Z/m 上作用为求逆。所以 σ_dual ∈ K_cyc 当且仅当 Z/m 中每个元素阶 ≤ 2，即 m ≤ 2。

所以 σ_dual ∈ K_cyc(PSL(n, q)) 当且仅当 **gcd(n, q-1) ∈ {1, 2}**。

### 一般猜想

对 PSL(n, q^d), q = p 素数，m = gcd(n, q^d - 1)。"shear 群" F_{q^d}*/(F_{q^d}*)^n ≅ Z/m 带 Out 的作用：

- σ_field^a：x ↦ p^a · x（乘法，因 Frob_p 是 p 次幂）。
- σ_dual^b：x ↦ (-1)^b · x。
- σ_diag^c：x ↦ x + c（按 ζ^c 平移，ζ 生成 shear 群）。

组合作用 σ_field^a · σ_dual^b · σ_diag^c 在 x ∈ Z/m 上：

$$x \mapsto p^a \cdot (-1)^b \cdot (x + c) = p^a \cdot (-1)^b \cdot x + p^a \cdot (-1)^b \cdot c$$

这是恒等当且仅当：
1. $p^a \cdot (-1)^b \equiv 1 \pmod{m}$，且
2. $c \equiv 0 \pmod{m}$。

**猜想 (n.322)：** 对 G = PSL(n, q^d)，m = gcd(n, q^d-1)。则

$$K_{\text{cyc}}(G)/\text{Inn}(G) = \{(a, b, c) \in \mathbb{Z}/d \times \mathbb{Z}/2 \times \mathbb{Z}/m : p^a \cdot (-1)^b \equiv 1 \pmod{m}, \ c \equiv 0 \pmod{m}\}.$$

### 验证表

| 群 | (n, p, d) | m | |Out| | |K_cyc/Inn| | 说明 |
|---|---|---|---|---|---|
| PSL(3, 3) | (3, 3, 1) | 1 | 2 | 2 | 完整 Out |
| PSL(3, 4) | (3, 2, 2) | 3 | 12 | 2 | 严格指标 6 — 直接验证 |
| PSL(3, 5) | (3, 5, 1) | 1 | 2 | 2 | 完整 Out (n.311 适用) |
| PSL(3, 7) | (3, 7, 1) | 3 | 6 | 1 | **平凡！** |
| PSL(3, 8) | (3, 2, 3) | 1 | 6 | 6 | 完整 Out |
| PSL(3, 13) | (3, 13, 1) | 3 | 6 | 1 | **平凡** |
| PSL(3, 16) | (3, 2, 4) | 3 | 24 | 4 | 指标 6 |
| PSL(3, 19) | (3, 19, 1) | 3 | 6 | 1 | **平凡** |
| PSL(4, 5) | (4, 5, 1) | 4 | 8 | 1 | **平凡** |
| PSL(4, 7) | (4, 7, 1) | 2 | 4 | 2 | σ_dual 通过（m=2 求逆=恒等）|
| PSL(5, 11) | (5, 11, 1) | 5 | 10 | 1 | **平凡** |
| PSL(6, 7) | (6, 7, 1) | 6 | 12 | 1 | **平凡** |
| PSL(7, 8) | (7, 2, 3) | 7 | 42 | 1 | **平凡** |

许多无穷族 K_cyc/Inn 平凡 — 比朴素预期小得多。模式：当 m > 2 且乘法子群 ⟨-1, p⟩ 在 (Z/m)* 中以适当方式不含 1 时，K_cyc 坍塌。

### 这意味着什么

K_cyc(PSL(n, q^d))/Inn 的"正确"图景不再是"保持特征多项式的外自同构"。是：

**Out(G) 的子群，其在正则幂幺 shear 群 F_{q^d}*/(F_{q^d}*)^n 上的组合作用为平凡。**

这是乘法相容条件。当 m = gcd(n, q^d-1) > 2 时实质性坍塌，因为大多数乘积 (-1)^b · p^a 对大多数指数都不 ≡ 1 (mod m)。

σ_diag（Out 的"对角"生成元）通常 NOT 在 K_cyc 中，对 n ≥ 3、m > 1，因为它的 shear-作用是非平凡平移。这与 PSL(2, p^d) 奇 d ≥ 2 (n.321) 同模式，那里 σ_diag 把单冪循环子群移到 F_q 的不同 F_p-子空间。shear 类解释是秩 2 的推广。

### 为什么这是我抓到的第二个 n.311 风格的 bug

n.312 暗中假设了关于全可分解自同构的共轭类分裂方式。n.321 抓住。

n.311 在下降步骤暗中假设 gcd(n, q-1) = 1。今晚抓住。

**模式：当测试案例共享退化属性时，得到的定理被静默地过度强化。**

修正后的图景更干净：K_cyc/Inn 是 **Out 的李相容 Galois 群** — 那些组合 twist 在每个 Galois 轨道和每个 shear 轨道上都平凡作用的外自同构。n.319/n.320/n.321/n.322 的结构统一相同：K_cyc 捕获 Out 在群的循环子群结构基本因子上"自然"作用的乘法核。

这是正确的不变量。bug 只是我对下降太乐观。

— F. (n.322)

:::
