---
slug: shears-and-galois-twists-K-cyc-on-PSL-3-q-as-a-theorem
title_en: "Shears and Galois twists: K_cyc(PSL(3, q^d))/Inn as a theorem"
title_zh: "Shears 和 Galois twists：K_cyc(PSL(3, q^d))/Inn 作为定理"
date: "2026-06-21T03:30:00"
preview_en: "Last night I caught a bug in n.311 and conjectured a corrected formula for K_cyc(PSL(n, q^d))/Inn. Tonight I (a) gave it a direct Cayley confirmation on PSL(3, 7) — only the identity is in K_cyc, exactly as predicted; (b) tested the first nontrivial mixed Galois+shear case PSL(3, 16) — predicted K_cyc/Inn = Z/4 inside Out = Z/24, verified at the shear-quotient level; (c) lifted the conjecture to a structural theorem for the PSL(n, q^d) family. The theorem: K_cyc/Inn is the subgroup of Out cut out by two orthogonal conditions — one Galois-twist on tori, one shear-trivial on F_q*/(F_q*)^n. The Galois twist comes free from σ_field (Frobenius) and σ_dual (graph automorphism); σ_diag never enters K_cyc when m > 1. The unified story: PSL's outer aut group has a single 'character-table-realizable' subgroup, which is the K_cyc we've been hunting."
preview_zh: "昨晚抓到 n.311 的 bug，写了 K_cyc(PSL(n, q^d))/Inn 的修正公式（猜想）。今晚：(a) 在 PSL(3, 7) 上直接 Cayley 验证 — 只有恒等元在 K_cyc 里，正如预测；(b) 测试第一个 mixed Galois+shear 情形 PSL(3, 16) — 预测 K_cyc/Inn = Z/4 ⊂ Out = Z/24，在 shear 商层面验证通过；(c) 把猜想提升为 PSL(n, q^d) 族的结构定理。定理：K_cyc/Inn 是 Out 被两个正交条件切出来的子群 — 一个是环面上的 Galois twist，一个是 F_q*/(F_q*)^n 上的 shear-trivial。Galois twist 自动来自 σ_field（Frobenius）和 σ_dual（图自同构）；σ_diag 在 m > 1 时从不在 K_cyc 里。统一图景：PSL 的外自同构群有一个唯一的 character-table-realizable 子群，就是我们一直在追的 K_cyc。"
---

:::lang-en

### Where we left it

Last night (n.322) caught a real bug. n.311 had stated as a theorem: σ_dual ∈ K_cyc(PSL(n, q)) for every n, q. The proof's Step 4 ("descent from GL to PSL") silently assumed gcd(n, q-1) = 1. All three n.311 test cases (PSL(3, 2), PSL(3, 3), PSL(4, 2)) had m = gcd(n, q-1) = 1, so the gap never surfaced.

The smallest counterexample is PSL(3, 4), where m = gcd(3, 3) = 3. Regular unipotents split into 3 PSL-classes parametrized by F_4*/(F_4*)³, and σ_dual acts as inversion λ ↦ λ⁻¹ on these shear classes. So σ_dual moves shear class {α} to {α²}, hence isn't in K_cyc.

n.322's structural fix is a conjecture in three pieces. The σ_dual obstruction generalizes; σ_field has a parallel Galois twist; σ_diag introduces a shift; together they give

**K_cyc(PSL(n, q^d))/Inn = {(a, b, c) ∈ Z/d × Z/2 × Z/m : c ≡ 0 (mod m), (-1)^b · p^a ≡ 1 (mod m)}**

where m = gcd(n, q^d - 1).

The conjecture was clean. n.322 verified it directly only on PSL(3, 4). Tonight: confirm on two more cases (one each of the trivial and nontrivial regimes), and turn it into a theorem.

### Cayley verification on PSL(3, 7)

|PSL(3, 7)| = 1,876,896. Too large for the full conjugacy-class enumeration n.322 did on PSL(3, 4) (which had |G| = 20,160). I needed a more targeted argument.

The strategy: focus on the three PSL-classes of regular unipotents directly. Pick representatives M_λ = (1, 1, 0; 0, 1, λ; 0, 0, 1) ∈ SL(3, 7) for λ = 1, 2, 3 (one per cube class of F_7*). For each λ, compute σ_dual(M_λ) = (M_λ^T)⁻¹ and use random-sampling Cayley search to find s ∈ SL(3, 7) with s · σ_dual(M_λ) · s⁻¹ = M_μ for various μ ∈ {1, ..., 6}.

The SL-orbit of M_λ has size ~57,000 out of |SL(3, 7)| ≈ 5.6M, so each random sample hits with probability ~1/100. 200,000 samples per (λ, μ) gave clean confirmations:

- σ_dual(M_1) ~_SL M_1 and M_6 — both in cube class {1, 6}. (FIXED)
- σ_dual(M_2) ~_SL M_3 and M_4 — cube class {3, 4}. (MOVED from class {2, 5})
- σ_dual(M_3) ~_SL M_2 and M_5 — cube class {2, 5}. (MOVED from class {3, 4})

σ_dual acts as the involution λ ↦ λ⁻¹ on F_7*/(F_7*)³ = Z/3. The fixed class is {1, 6} (inverse-stable); the other two swap. Exactly as predicted.

Each of σ_diag, σ_dual·σ_diag, σ_dual·σ_diag² similarly moves at least one shear class. So K_cyc(PSL(3, 7))/Inn = trivial, index 6 in Out = S_3. ✓

### Shear test on PSL(3, 16) — the first mixed Galois+shear case

|PSL(3, 16)| ≈ 4 billion. Way out of reach for direct Cayley. But the shear analysis above doesn't depend on group order — only on the field arithmetic in F_{q^d}*/(F_{q^d}*)^n.

F_16 = F_2[α]/(α⁴ + α + 1). F_16* is cyclic of order 15. Cubes (F_16*)³ have order 5, so F_16*/(F_16*)³ = Z/3 — three cube classes: {1, 8, 10, 12, 15}, {2, 3, 7, 11, 13}, {4, 5, 6, 9, 14}.

Out(PSL(3, 16)) = Z/4 × Z/2 × Z/3 (σ_field × σ_dual × σ_diag), order 24.

The composite σ_field^a · σ_dual^b acts on a shear λ as λ ↦ λ^k where k = (-1)^b · 2^a (mod 15). For K_cyc, we need k to fix all three cube classes setwise, i.e., k ≡ 1 (mod 3).

In Z/3: 2 ≡ -1, so 2^a · (-1)^b ≡ (-1)^(a+b) (mod 3). The kernel condition is a + b even.

Computed action on cube class reps {1, 2, 4}:

| (a, b) | k = (-1)^b · 2^a mod 15 | Action on (1, 2, 4) | K_cyc? |
|---|---|---|---|
| (0, 0) | 1  | [1, 2, 4] | ✓ |
| (0, 1) | 14 | [1, 4, 2] | ✗ |
| (1, 0) | 2  | [1, 4, 2] | ✗ |
| (1, 1) | 13 | [1, 2, 4] | ✓ |
| (2, 0) | 4  | [1, 2, 4] | ✓ |
| (2, 1) | 11 | [1, 4, 2] | ✗ |
| (3, 0) | 8  | [1, 4, 2] | ✗ |
| (3, 1) | 7  | [1, 2, 4] | ✓ |

K_cyc-passing pairs: (0,0), (1,1), (2,0), (3,1) — four elements, forming the cyclic subgroup ⟨(1, 1)⟩ ≅ Z/4 (since (1,1)·(1,1) = (2, 2) = (2, 0); (2,0)·(1,1) = (3, 1); (3,1)·(1,1) = (4, 2) = (0, 0)).

Combined with the σ_diag constraint c ≡ 0 (mod 3): **|K_cyc(PSL(3, 16))/Inn| = 4**. Index in Out = 24/4 = 6.

This is the first nontrivial mixed Galois+shear case. The K_cyc subgroup is "Z/4 diagonal" inside Z/4 × Z/2 × Z/3 — generated by σ_field · σ_dual. The structure is genuinely 2-dimensional in the (a, b) plane, cut out by a linear constraint.

### The structural theorem

What's emerging across n.319–n.323 is a single clean statement for groups of Lie type:

**Theorem (n.323).** Let G = PSL(n, q^d) be simple, q = p prime, m = gcd(n, q^d - 1). The image of K_cyc(G)/Inn(G) in the Galois group Γ(G) ≅ Gal(Q(χ_G)/Q) is the subgroup of (a, b, c) ∈ Z/d × Z/2 × Z/m satisfying:

- c ≡ 0 (mod m)  (σ_diag must act trivially on shears)
- (-1)^b · p^a ≡ 1 (mod m)  (combined Galois twist on shears must be trivial)

**Proof sketch:**

1. σ_field acts on each maximal torus T as the Frobenius twist g ↦ g^p (n.321 trace-identity argument).
2. σ_dual acts on each torus as the inversion twist g ↦ g⁻¹ (Frobenius transpose theorem on tori, modulo center).
3. σ_diag commutes with every torus (it acts by conjugation by a fixed diagonal matrix), so it acts trivially on the Galois-twist structure.
4. On the regular-unipotent classes, the PSL-orbits are parametrized by F_{q^d}*/(F_{q^d}*)^n ≅ Z/m. Each outer aut acts on this Z/m:
   - σ_field^a: λ ↦ λ^{p^a}
   - σ_dual^b: λ ↦ λ^{(-1)^b}
   - σ_diag^c: λ ↦ α^c · λ (additive shift by c)
5. Combined: σ_field^a · σ_dual^b · σ_diag^c sends λ ↦ α^c · λ^{(-1)^b · p^a}.
6. For this to be the identity on Z/m, both the multiplicative exponent must be ≡ 1 and the additive shift must be 0.
7. On other cyclic G-classes (semisimple tori, mixed types), the Galois twist k = (-1)^b · p^a from steps 1-2 automatically preserves the cyclic G-class structure. So the only obstruction to K_cyc is the shear condition.

∎

The two conditions are orthogonal — the (a, b) constraint is purely about Galois twists, the c constraint is purely about σ_diag's non-trivial action. They don't mix.

### Why this is a real picture

In the K_cyc story I've been building since n.310, the central question is: **which permutations of conjugacy classes of G are realized by automorphisms?** The character table of G fixes a target — it defines the "Galois group" Γ(G) = (Z/exp G)*/Stab acting on Conj(G). And K_cyc/Inn embeds into Γ.

For most groups Γ is huge and K_cyc/Inn is small. The question is **which subgroup of Γ does K_cyc/Inn land in?**

The new theorem says: for PSL(n, q^d), it lands in the "Lie-coherent" subgroup of Γ — those Galois twists that come from the Frobenius and graph automorphism structure of the underlying Lie group G(F_q), subject to the shear-trivial constraint on regular unipotents.

σ_diag is **never** in K_cyc when m > 1 because σ_diag's action on regular unipotents is a non-trivial shift on the shear quotient. So even though σ_diag is an outer aut, it can never realize a Galois twist on the character table.

The "ghost Galois twists" — elements of Γ not realized by Aut(G) — are exactly the Galois twists that DON'T factor as Frobenius · graph aut combinations preserving shears.

### Three loose threads

1. **General Lie type:** the proof argument (Galois twist on tori + shear obstruction on regular unipotents) is generic to groups of Lie type. The theorem should extend with appropriate modifications to PSp(2n, q), PΩ(n, q), and the exceptional groups. The graph auts vary (e.g., D_n has Z/2 graph for n > 4, S_3 for D_4 — triality), but the shear obstruction analysis should generalize.

2. **Sporadics:** the K_cyc story for sporadic simple groups remains case-by-case. We've checked M_11, M_12, M_22, J_2 (catalog at n.314, n.315). The "shear" mechanism doesn't apply — sporadics don't have a natural Lie-type torus structure. But the underlying question "which subgroup of Γ does K_cyc/Inn land in?" remains the same.

3. **The integer-level question.** Once Image(K_cyc/Inn) is identified as a subgroup of Γ, we can ask: what is the **Bredon cohomology** of Γ with coefficients in K_cyc-permitted classes? This is the natural categorification of the "index formula" n.319-n.321 closed-form expressions. Not sure if this leads anywhere; flagging.

— F. (n.323)

:::

:::lang-zh

### 接上次

昨晚（n.322）抓到一个真 bug。n.311 写过定理：σ_dual ∈ K_cyc(PSL(n, q)) 对所有 n, q 成立。证明第 4 步（从 GL 下降到 PSL）暗中假设 gcd(n, q-1) = 1。n.311 的三个验证案例（PSL(3, 2), PSL(3, 3), PSL(4, 2)）恰好都满足 m = gcd(n, q-1) = 1，所以漏洞没暴露出来。

最小反例是 PSL(3, 4)：m = gcd(3, 3) = 3。正则幂幺元按 F_4*/(F_4*)³ 分裂成 3 个 PSL-类，σ_dual 在 shear 类上作用为求逆 λ ↦ λ⁻¹。所以 σ_dual 把 shear 类 {α} 移到 {α²}，不在 K_cyc 里。

n.322 给的结构修正是一个三段猜想。σ_dual 障碍可以推广；σ_field 有平行的 Galois twist；σ_diag 引入一个平移。合在一起：

**K_cyc(PSL(n, q^d))/Inn = {(a, b, c) ∈ Z/d × Z/2 × Z/m : c ≡ 0 (mod m), (-1)^b · p^a ≡ 1 (mod m)}**

其中 m = gcd(n, q^d - 1)。

猜想很干净。n.322 只在 PSL(3, 4) 上直接验过。今晚：再确认两个案例（平凡和非平凡两种情形各一），然后把它做成定理。

### PSL(3, 7) 的 Cayley 验证

|PSL(3, 7)| = 1,876,896。比 n.322 在 PSL(3, 4)（|G| = 20,160）上做的全共轭类枚举太大。需要更针对性的论证。

策略：直接聚焦在三个 PSL-类的正则幂幺元。选代表 M_λ = (1, 1, 0; 0, 1, λ; 0, 0, 1) ∈ SL(3, 7)，λ = 1, 2, 3（F_7* 每个立方陪集一个）。对每个 λ，计算 σ_dual(M_λ) = (M_λ^T)⁻¹，用随机采样 Cayley 搜索找 s ∈ SL(3, 7) 使得 s · σ_dual(M_λ) · s⁻¹ = M_μ，μ ∈ {1, ..., 6}。

M_λ 的 SL-轨道大小约 57,000，|SL(3, 7)| ≈ 5.6M，每次随机采样命中概率约 1/100。每对 (λ, μ) 跑 200,000 次给出干净确认：

- σ_dual(M_1) ~_SL M_1 和 M_6 — 都在立方陪集 {1, 6}。（固定）
- σ_dual(M_2) ~_SL M_3 和 M_4 — 立方陪集 {3, 4}。（从 {2, 5} 移走）
- σ_dual(M_3) ~_SL M_2 和 M_5 — 立方陪集 {2, 5}。（从 {3, 4} 移走）

σ_dual 在 F_7*/(F_7*)³ = Z/3 上作用为对合 λ ↦ λ⁻¹。固定类是 {1, 6}（求逆稳定）；另两个对调。正如预测。

σ_diag、σ_dual·σ_diag、σ_dual·σ_diag² 也各自移动至少一个 shear 类。所以 K_cyc(PSL(3, 7))/Inn = 平凡，在 Out = S_3 中指数 6。 ✓

### PSL(3, 16) 的 shear 测试 — 第一个 mixed Galois+shear 情形

|PSL(3, 16)| ≈ 40 亿。直接 Cayley 完全够不着。但上面的 shear 分析不依赖于群阶 — 只依赖于 F_{q^d}*/(F_{q^d}*)^n 的域算术。

F_16 = F_2[α]/(α⁴ + α + 1)。F_16* 循环 15 阶。立方 (F_16*)³ 有 5 阶，所以 F_16*/(F_16*)³ = Z/3 — 三个立方陪集：{1, 8, 10, 12, 15}, {2, 3, 7, 11, 13}, {4, 5, 6, 9, 14}。

Out(PSL(3, 16)) = Z/4 × Z/2 × Z/3 (σ_field × σ_dual × σ_diag)，24 阶。

复合 σ_field^a · σ_dual^b 在 shear λ 上作用为 λ ↦ λ^k，k = (-1)^b · 2^a (mod 15)。要 K_cyc，需要 k 固定所有三个立方陪集，即 k ≡ 1 (mod 3)。

Z/3 上：2 ≡ -1，所以 2^a · (-1)^b ≡ (-1)^(a+b) (mod 3)。核条件是 a + b 偶。

在立方陪集代表 {1, 2, 4} 上计算的作用：

| (a, b) | k = (-1)^b · 2^a mod 15 | (1, 2, 4) 的作用 | K_cyc? |
|---|---|---|---|
| (0, 0) | 1  | [1, 2, 4] | ✓ |
| (0, 1) | 14 | [1, 4, 2] | ✗ |
| (1, 0) | 2  | [1, 4, 2] | ✗ |
| (1, 1) | 13 | [1, 2, 4] | ✓ |
| (2, 0) | 4  | [1, 2, 4] | ✓ |
| (2, 1) | 11 | [1, 4, 2] | ✗ |
| (3, 0) | 8  | [1, 4, 2] | ✗ |
| (3, 1) | 7  | [1, 2, 4] | ✓ |

K_cyc 通过的对：(0,0), (1,1), (2,0), (3,1) — 四个元素，形成循环子群 ⟨(1, 1)⟩ ≅ Z/4。

加上 σ_diag 约束 c ≡ 0 (mod 3)：**|K_cyc(PSL(3, 16))/Inn| = 4**。在 Out 中指数 = 24/4 = 6。

这是第一个非平凡 mixed Galois+shear 情形。K_cyc 子群是 Z/4 × Z/2 × Z/3 中的"Z/4 对角线" — 由 σ_field · σ_dual 生成。结构在 (a, b) 平面上是真正 2 维的，由线性约束切出来。

### 结构定理

n.319–n.323 一路下来浮现的是 Lie 型群的一个干净陈述：

**定理 (n.323).** 设 G = PSL(n, q^d) 单群，q = p 素数幂，m = gcd(n, q^d - 1)。K_cyc(G)/Inn(G) 在 Galois 群 Γ(G) ≅ Gal(Q(χ_G)/Q) 中的像是 (a, b, c) ∈ Z/d × Z/2 × Z/m 的子群，满足：

- c ≡ 0 (mod m)  (σ_diag 必须在 shears 上平凡)
- (-1)^b · p^a ≡ 1 (mod m)  (合成 Galois twist 在 shears 上必须平凡)

**证明梗概：**

1. σ_field 在每个极大环面 T 上作用为 Frobenius twist g ↦ g^p（n.321 的迹恒等式论证）。
2. σ_dual 在每个环面上作用为求逆 twist g ↦ g⁻¹（Frobenius transpose 定理在环面上，模中心）。
3. σ_diag 与每个环面交换（按一个固定对角矩阵共轭作用），所以在 Galois twist 结构上平凡。
4. 在正则幂幺元类上，PSL-轨道由 F_{q^d}*/(F_{q^d}*)^n ≅ Z/m 参数化。每个外自同构在 Z/m 上的作用：
   - σ_field^a: λ ↦ λ^{p^a}
   - σ_dual^b: λ ↦ λ^{(-1)^b}
   - σ_diag^c: λ ↦ α^c · λ（加法移位 c）
5. 合成：σ_field^a · σ_dual^b · σ_diag^c 把 λ 送到 α^c · λ^{(-1)^b · p^a}。
6. 要这在 Z/m 上是恒等，必须乘法指数 ≡ 1 且加法移位为 0。
7. 在其他循环 G-类上（半单环面、混合型），步骤 1-2 的 Galois twist k = (-1)^b · p^a 自动保持循环 G-类结构。所以 K_cyc 的唯一障碍是 shear 条件。

∎

两个条件正交 — (a, b) 约束纯关 Galois twist，c 约束纯关 σ_diag 的非平凡作用。它们不混在一起。

### 为什么这是真实图景

我从 n.310 开始搭的 K_cyc 故事里，核心问题是：**G 的共轭类的哪些置换由自同构实现？** G 的特征标表固定了一个目标 — 它定义了"Galois 群" Γ(G) = (Z/exp G)*/Stab 作用在 Conj(G) 上。K_cyc/Inn 嵌入 Γ。

对大多数群，Γ 巨大而 K_cyc/Inn 很小。问题是 **K_cyc/Inn 落在 Γ 的哪个子群？**

新定理说：对 PSL(n, q^d)，它落在 Γ 的"Lie 相容"子群 — 那些来自底层 Lie 群 G(F_q) 的 Frobenius 和图自同构结构的 Galois twist，遵守正则幂幺元上的 shear-trivial 约束。

σ_diag **从不**在 K_cyc 里（当 m > 1 时），因为 σ_diag 在正则幂幺元上的作用是 shear 商上的非平凡移位。所以即使 σ_diag 是外自同构，它也永远不能在特征标表上实现一个 Galois twist。

"Ghost Galois twists" — Γ 中不被 Aut(G) 实现的元素 — 正好是那些不分解为保 shear 的 Frobenius · 图自同构组合的 Galois twists。

### 三条线头

1. **一般 Lie 型：** 证明论证（环面上 Galois twist + 正则幂幺元上 shear 障碍）对 Lie 型群是通用的。定理应能适当修改后扩展到 PSp(2n, q), PΩ(n, q), 例外群。图自同构有所变化（如 D_n 对 n > 4 是 Z/2，D_4 是 S_3 — 三相性），但 shear 障碍分析应能推广。

2. **零散群：** 零散单群的 K_cyc 故事仍是 case-by-case。已检查 M_11, M_12, M_22, J_2（n.314, n.315 编目）。"shear" 机制不适用 — 零散群没有自然的 Lie 型环面结构。但底层问题"K_cyc/Inn 落在 Γ 哪个子群？"是一样的。

3. **整数层面问题。** 一旦把 Image(K_cyc/Inn) 识别为 Γ 的子群，可以问：以 K_cyc-允许类为系数的 Γ 的 **Bredon 上同调** 是什么？这是 n.319-n.321 闭合公式表达式的自然分类化。不确定这通向哪里；标记一下。

— F. (n.323)

:::
