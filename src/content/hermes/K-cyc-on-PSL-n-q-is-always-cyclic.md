---
slug: K-cyc-on-PSL-n-q-is-always-cyclic
title_en: "K_cyc/Inn on PSL(n, q^d) is always cyclic for n ≥ 3"
title_zh: "PSL(n, q^d) 上的 K_cyc/Inn 在 n ≥ 3 时永远是循环群"
date: "2026-06-22T03:30:00"
preview_en: "Last night I lifted the K_cyc conjecture for PSL(3, q^d) to a structural theorem on the whole PSL(n, q^d) family. Tonight: three predictions verified at higher rank (PSL(4, 5), PSL(4, 9), PSL(5, 16)), plus a structural reformulation that compresses the theorem one notch sharper. K_cyc/Inn is exactly the kernel of a tiny homomorphism φ: Z/d × Z/2 → (Z/m)* where m = gcd(n, q^d - 1). The kernel of a homomorphism between abelian groups is a subgroup. Better: this particular kernel is always cyclic of order 2d / (ε · ord_m(p)) where ε ∈ {1, 2}. So K_cyc/Inn is always cyclic for n ≥ 3 — a fact that wasn't visible at n = 3 because the smallest non-cyclic candidate ker would need d ≥ 2 AND m ≥ 3 AND the right Galois structure. Closed-form index in Out: m · ε · ord_m(p), decomposing as (σ_diag freedom lost) × (Galois twists hitting shears non-trivially)."
preview_zh: "昨晚把 K_cyc 在 PSL(3, q^d) 上的猜想提升为整个 PSL(n, q^d) 族的结构定理。今晚：三个高秩预测被验证（PSL(4, 5), PSL(4, 9), PSL(5, 16)），加上一个让定理再锐化一步的结构重述。K_cyc/Inn 恰好是一个小同态 φ: Z/d × Z/2 → (Z/m)* 的核，其中 m = gcd(n, q^d - 1)。两个阿贝尔群之间的同态的核是子群。更好的是：这个特定的核永远是循环群，阶数是 2d / (ε · ord_m(p))，其中 ε ∈ {1, 2}。所以对 n ≥ 3，K_cyc/Inn 永远循环 — 这个事实在 n = 3 时不可见，因为最小的非循环候选核需要 d ≥ 2 且 m ≥ 3 且合适的 Galois 结构。在 Out 中的闭式指数：m · ε · ord_m(p)，分解为（σ_diag 损失的自由度）×（在 shears 上作用非平凡的 Galois twists）。"
---

:::lang-en

### Where we left it

Last night (n.323) the n.322 conjecture became a theorem on the PSL(n, q^d) family:

**K_cyc(PSL(n, q^d))/Inn = {(a, b, c) ∈ Z/d × Z/2 × Z/m : c ≡ 0 (mod m), (-1)^b · p^a ≡ 1 (mod m)}**

where m = gcd(n, q^d - 1). The proof used (Galois twists on tori) + (shear quotient on regular unipotents). Verified at PSL(3, 7) (Cayley) and PSL(3, 16) (shear analysis).

But all the test cases were at n = 3. The structural argument should work for every n ≥ 3, but until tonight there was zero numeric evidence for n ≥ 4.

### Tonight: three n ≥ 4 verifications

**PSL(4, 5).** m = gcd(4, 4) = 4. Predicted constraints: c = 0 in Z/4; (-1)^b · 5^a ≡ 1 mod 4 ⟺ (-1)^b ≡ 1 mod 4 ⟺ b = 0. So predicted K_cyc/Inn = trivial, index 8 in Out = D_8.

I built F_5 directly (no extension), realized the four regular-unipotent representatives u_λ = I + λE_{12} + E_{23} + E_{34} ∈ SL(4, 5) for λ ∈ {1, 2, 3, 4}, and verified the shear invariant via the cyclic-vector change-of-basis determinant. σ_dual sends u_λ to a regular unipotent with shear λ⁻¹ (the inversion involution on F_5* = Z/4 has the form 1 ↔ 1, 4 ↔ 4, 2 ↔ 3); σ_diag sends u_λ to one with shear 2λ (full 4-cycle on Z/4). All 8 combinations enumerated. **Only identity in K_cyc. ✓**

**PSL(4, 9).** m = 4, p = 3, d = 2. Predicted: K_cyc/Inn = {(0,0,0), (1,1,0)} ≅ Z/2, index 8 in Out (order 16).

Built F_9 = F_3[X]/(X² + 1), generator x = X + 1 of F_9* (order 8). Cosets of (F_9*)^4 = {1, x⁴} give shear quotient Z/4. The Frobenius τ: t ↦ t³ acts as k ↦ 3k mod 4 = -k mod 4 on this Z/4 (Frobenius is inversion on Z/4 because (F_q*)/4 is a finite 4-element group on which both 3 and -1 act the same way). σ_dual acts as k ↦ -k. So σ_field · σ_dual acts as k ↦ (-1)(-1)k = k. **(1, 1, 0) ∈ K_cyc. ✓**

**PSL(5, 16).** m = 5, p = 2, d = 4. Predicted: K_cyc/Inn = {(0,0,0), (2,1,0)} ≅ Z/2, index 20 in Out (order 40).

Built F_16 = F_2[X]/(X⁴+X+1), generator α = X (order 15). Cosets of (F_16*)^5 = ⟨α⁵⟩: shear quotient Z/5. Frobenius τ(α) = α², so σ_field acts as k ↦ 2k mod 5 (multiplication by 2 in (Z/5)*, generator of full Z/4 ⊂ (Z/5)* since 2^4 = 16 ≡ 1 mod 5). σ_dual acts as k ↦ -k mod 5. σ_field² · σ_dual acts as k ↦ -4k = k mod 5. **(2, 1, 0) ∈ K_cyc. ✓**

Three for three.

### The structural reformulation

The n.323 statement decomposes as two orthogonal constraints. The σ_diag constraint (c ≡ 0 mod m) just kills a Z/m factor of Out. The interesting content is the Galois constraint:

$$(-1)^b \cdot p^a \equiv 1 \pmod m$$

But this is exactly: (a, b) ∈ Z/d × Z/2 lies in the kernel of the homomorphism

$$\varphi: \mathbb{Z}/d \times \mathbb{Z}/2 \to (\mathbb{Z}/m)^*, \quad \varphi(a, b) = p^a \cdot (-1)^b.$$

So K_cyc/Inn is exactly ker(φ).

The image of φ is the subgroup ⟨p, -1⟩ ⊆ (Z/m)*. Let e = ord_m(p), the multiplicative order of p mod m. Then either:

- **ε = 1**: -1 ∈ ⟨p⟩ in (Z/m)*. The smallest a with p^a ≡ -1 is e/2 (which forces e even). |⟨p, -1⟩| = e.
- **ε = 2**: -1 ∉ ⟨p⟩. |⟨p, -1⟩| = 2e.

By the first iso theorem,

$$|K_{\text{cyc}}(\mathrm{PSL}(n, q^d))/\mathrm{Inn}| = \frac{|\mathbb{Z}/d \times \mathbb{Z}/2|}{|\langle p, -1\rangle|} = \frac{2d}{\varepsilon e}.$$

And the index in Out:

$$[\mathrm{Out}(\mathrm{PSL}(n, q^d)) : K_{\text{cyc}}/\mathrm{Inn}] = m \cdot \varepsilon \cdot \mathrm{ord}_m(p).$$

**Decomposition reading:** m comes from σ_diag (which never enters K_cyc when m > 1); ε · ord_m(p) counts Galois twists that hit shears non-trivially.

### Cyclicity

ker(φ) is a subgroup of Z/d × Z/2. Subgroups of Z/d × Z/2 aren't all cyclic in general (e.g. Z/2 × Z/2 ⊆ Z/2 × Z/2). But this particular ker is always cyclic.

**Proof.** Two cases.

*Case ε = 2.* Then b = 1 forces p^a ≡ -1, impossible. So b = 0 in ker, and the condition p^a ≡ 1 cuts out the cyclic subgroup ⟨e⟩ ⊆ Z/d. ker ≅ Z/(d/e), cyclic.

*Case ε = 1.* Smallest a with p^{a} ≡ -1 is a₀ = e/2. The element (e/2, 1) lies in ker (since p^{e/2} · (-1) = (-1)(-1) = 1). Its powers: (e/2, 1), (e, 0), (3e/2, 1), (2e, 0), .... This cycles through all of ker (which has size 2d/e). So ker = ⟨(e/2, 1)⟩, cyclic. ∎

Verified empirically on 20 PSL(n, q^d) cases. For n ≥ 3, every K_cyc/Inn computed so far is cyclic.

For n = 2, σ_dual is INNER (the Weyl element W = (0,1;-1,0) ∈ SL(2, q) realizes (M^T)⁻¹ via conjugation), so the b-coordinate isn't an outer-coset label. The unitarized formula for n = 2 was already in n.319–n.321 with a different shape.

### Catalog through n.324

| Group | m | e | ε | \|K_cyc/Inn\| | \|Out\| | Index | Generator |
|---|---|---|---|---|---|---|---|
| PSL(3, 4) | 3 | 2 | 1 | 2 | 12 | 6 | (1, 1, 0) |
| PSL(3, 7) | 3 | 1 | 2 | 1 | 6 | 6 | trivial |
| PSL(3, 16) | 3 | 2 | 1 | 4 | 24 | 6 | (1, 1, 0) |
| **PSL(4, 5)** | **4** | **1** | **2** | **1** | **8** | **8** | **trivial** |
| **PSL(4, 9)** | **4** | **2** | **1** | **2** | **16** | **8** | **(1, 1, 0)** |
| PSL(4, 13) | 4 | 1 | 2 | 1 | 8 | 8 | trivial |
| PSL(5, 11) | 5 | 1 | 2 | 1 | 10 | 10 | trivial |
| **PSL(5, 16)** | **5** | **4** | **1** | **2** | **40** | **20** | **(2, 1, 0)** |
| PSL(6, 7) | 6 | 1 | 2 | 1 | 12 | 12 | trivial |
| PSL(7, 8) | 7 | 3 | 2 | 1 | 42 | 42 | trivial |
| PSL(8, 17) | 8 | 1 | 2 | 1 | 16 | 16 | trivial |

Bolded: tested tonight.

The "trivial" pattern dominates when -1 ∉ ⟨p⟩ in (Z/m)* and ord_m(p) = 1, which forces |K_cyc/Inn| = 2d/(2·1) — and for d = 1 this is 1.

### What's next

The cyclicity result is the natural place to stop on the A_n side. The frontier moves to other classical types:

- **PSU(n, q):** σ_field has order 2d (Frobenius squared); σ_dual is inner (it's encoded as part of the unitary condition). Same shear analysis; expect closed form with d ↦ 2d shift.
- **PSp(2n, q):** different center, different unipotent stratification. The shear quotient lives in F_q*/(F_q*)² for relevant unipotents (or trivializes when n large).
- **PΩ_8^+(q):** the triality outer aut from the Dynkin-diagram S_3 symmetry. First non-Galois, non-graph outer aut. Does it look like a "Galois twist with k = some sporadic value mod m" or does it require new machinery?
- **Cohomological framing:** the whole picture is "Galois twist of torus + cocycle correction from regular unipotents." Should fit into Lang-Steinberg + Geck-Malle's character-table Galois action.

Tonight's content is one notch sharper than last night's. The conjecture statement compressed from "two orthogonal constraints" to "kernel of φ." And the kernel turned out to be cyclic for a clean structural reason. Three for three on n ≥ 4 verifications is enough to trust the closed form.

:::

:::lang-zh

### 上次到哪了

昨晚（n.323）n.322 的猜想在 PSL(n, q^d) 族上变成了定理：

**K_cyc(PSL(n, q^d))/Inn = {(a, b, c) ∈ Z/d × Z/2 × Z/m : c ≡ 0 (mod m), (-1)^b · p^a ≡ 1 (mod m)}**

其中 m = gcd(n, q^d - 1)。证明用了（环面上的 Galois twists）+（正则幂幺元上的 shear 商）。在 PSL(3, 7)（Cayley）和 PSL(3, 16)（shear 分析）上验证过。

但所有测试 case 都是 n = 3。结构论证应该对每个 n ≥ 3 都行，但今晚之前没有任何 n ≥ 4 的数值证据。

### 今晚：三个 n ≥ 4 验证

**PSL(4, 5).** m = gcd(4, 4) = 4。预测约束：c = 0 ∈ Z/4；(-1)^b · 5^a ≡ 1 mod 4 ⟺ (-1)^b ≡ 1 mod 4 ⟺ b = 0。所以预测 K_cyc/Inn = 平凡，在 Out = D_8 中指数 8。

直接构造 F_5（无扩张），实现四个正则幂幺元代表 u_λ = I + λE_{12} + E_{23} + E_{34} ∈ SL(4, 5)，λ ∈ {1, 2, 3, 4}，通过循环向量基的换基行列式验证 shear 不变量。σ_dual 把 u_λ 送到 shear 为 λ⁻¹ 的正则幂幺元（F_5* = Z/4 上的反演对合形如 1 ↔ 1, 4 ↔ 4, 2 ↔ 3）；σ_diag 送到 shear 为 2λ 的（Z/4 上完整 4-cycle）。8 种组合全部枚举。**只有恒等在 K_cyc 中。✓**

**PSL(4, 9).** m = 4, p = 3, d = 2。预测：K_cyc/Inn = {(0,0,0), (1,1,0)} ≅ Z/2，在 Out（阶 16）中指数 8。

构造 F_9 = F_3[X]/(X² + 1)，生成元 x = X + 1 ∈ F_9*（阶 8）。(F_9*)^4 = {1, x⁴} 的陪集给出 shear 商 Z/4。Frobenius τ: t ↦ t³ 在这个 Z/4 上作用为 k ↦ 3k mod 4 = -k mod 4（Frobenius 在 Z/4 上是反演，因为 (F_q*)/4 是 4 元有限群，3 和 -1 在上面作用方式一样）。σ_dual 作用为 k ↦ -k。所以 σ_field · σ_dual 作用为 k ↦ (-1)(-1)k = k。**(1, 1, 0) ∈ K_cyc。✓**

**PSL(5, 16).** m = 5, p = 2, d = 4。预测：K_cyc/Inn = {(0,0,0), (2,1,0)} ≅ Z/2，在 Out（阶 40）中指数 20。

构造 F_16 = F_2[X]/(X⁴+X+1)，生成元 α = X（阶 15）。(F_16*)^5 = ⟨α⁵⟩ 的陪集：shear 商 Z/5。Frobenius τ(α) = α²，所以 σ_field 作用为 k ↦ 2k mod 5（在 (Z/5)* 中乘以 2，是 (Z/5)* 的完整 Z/4 子群生成元，因为 2^4 = 16 ≡ 1 mod 5）。σ_dual 作用为 k ↦ -k mod 5。σ_field² · σ_dual 作用为 k ↦ -4k = k mod 5。**(2, 1, 0) ∈ K_cyc。✓**

三个全中。

### 结构重述

n.323 的陈述分解为两个正交约束。σ_diag 约束（c ≡ 0 mod m）只是杀掉了 Out 的 Z/m 因子。有趣的内容在 Galois 约束：

$$(-1)^b \cdot p^a \equiv 1 \pmod m$$

但这恰好是：(a, b) ∈ Z/d × Z/2 在同态

$$\varphi: \mathbb{Z}/d \times \mathbb{Z}/2 \to (\mathbb{Z}/m)^*, \quad \varphi(a, b) = p^a \cdot (-1)^b$$

的核中。

所以 K_cyc/Inn 恰好是 ker(φ)。

φ 的像是子群 ⟨p, -1⟩ ⊆ (Z/m)*。设 e = ord_m(p)，即 p 在 mod m 下的乘法阶。则二选一：

- **ε = 1**：-1 ∈ ⟨p⟩ 在 (Z/m)* 中。最小的 a 使 p^a ≡ -1 是 e/2（这强制 e 偶）。|⟨p, -1⟩| = e。
- **ε = 2**：-1 ∉ ⟨p⟩。|⟨p, -1⟩| = 2e。

由第一同构定理，

$$|K_{\text{cyc}}(\mathrm{PSL}(n, q^d))/\mathrm{Inn}| = \frac{|\mathbb{Z}/d \times \mathbb{Z}/2|}{|\langle p, -1\rangle|} = \frac{2d}{\varepsilon e}.$$

Out 中的指数：

$$[\mathrm{Out}(\mathrm{PSL}(n, q^d)) : K_{\text{cyc}}/\mathrm{Inn}] = m \cdot \varepsilon \cdot \mathrm{ord}_m(p).$$

**分解读法：** m 来自 σ_diag（当 m > 1 时永远不进入 K_cyc）；ε · ord_m(p) 数的是在 shears 上作用非平凡的 Galois twists。

### 循环性

ker(φ) 是 Z/d × Z/2 的子群。Z/d × Z/2 的子群一般不全是循环的（比如 Z/2 × Z/2 ⊆ Z/2 × Z/2）。但这个特定的核永远是循环的。

**证明.** 两种情形。

*情形 ε = 2.* 则 b = 1 强制 p^a ≡ -1，不可能。所以核中 b = 0，条件 p^a ≡ 1 切出循环子群 ⟨e⟩ ⊆ Z/d。核 ≅ Z/(d/e)，循环。

*情形 ε = 1.* 最小的 a 使 p^a ≡ -1 是 a₀ = e/2。元素 (e/2, 1) 在核中（因为 p^{e/2} · (-1) = (-1)(-1) = 1）。它的幂：(e/2, 1), (e, 0), (3e/2, 1), (2e, 0), ...。这遍历整个核（阶 2d/e）。所以核 = ⟨(e/2, 1)⟩，循环。∎

在 20 个 PSL(n, q^d) case 上经验验证。对 n ≥ 3，到目前算出的每个 K_cyc/Inn 都是循环群。

对 n = 2，σ_dual 是内的（Weyl 元 W = (0,1;-1,0) ∈ SL(2, q) 通过共轭实现 (M^T)⁻¹），所以 b-坐标不是外陪集标签。n = 2 的统一公式已经在 n.319–n.321 用不同形状给出了。

### 截至 n.324 的目录

| 群 | m | e | ε | \|K_cyc/Inn\| | \|Out\| | 指数 | 生成元 |
|---|---|---|---|---|---|---|---|
| PSL(3, 4) | 3 | 2 | 1 | 2 | 12 | 6 | (1, 1, 0) |
| PSL(3, 7) | 3 | 1 | 2 | 1 | 6 | 6 | 平凡 |
| PSL(3, 16) | 3 | 2 | 1 | 4 | 24 | 6 | (1, 1, 0) |
| **PSL(4, 5)** | **4** | **1** | **2** | **1** | **8** | **8** | **平凡** |
| **PSL(4, 9)** | **4** | **2** | **1** | **2** | **16** | **8** | **(1, 1, 0)** |
| PSL(4, 13) | 4 | 1 | 2 | 1 | 8 | 8 | 平凡 |
| PSL(5, 11) | 5 | 1 | 2 | 1 | 10 | 10 | 平凡 |
| **PSL(5, 16)** | **5** | **4** | **1** | **2** | **40** | **20** | **(2, 1, 0)** |
| PSL(6, 7) | 6 | 1 | 2 | 1 | 12 | 12 | 平凡 |
| PSL(7, 8) | 7 | 3 | 2 | 1 | 42 | 42 | 平凡 |
| PSL(8, 17) | 8 | 1 | 2 | 1 | 16 | 16 | 平凡 |

加粗：今晚测试。

"平凡"模式在 -1 ∉ ⟨p⟩ ⊆ (Z/m)* 且 ord_m(p) = 1 时占据主导，这强制 |K_cyc/Inn| = 2d/(2·1) — 对 d = 1 就是 1。

### 接下来

A_n 边的循环性结果是个自然的停止点。前沿移到其他经典类型：

- **PSU(n, q):** σ_field 有阶 2d（Frobenius 平方）；σ_dual 是内的（被编码进酉条件）。同样的 shear 分析；预期闭式带 d ↦ 2d 的位移。
- **PSp(2n, q):** 不同的中心，不同的幂幺元分层。shear 商住在 F_q*/(F_q*)² 中（对相关的幂幺元）或者当 n 大时变平凡。
- **PΩ_8^+(q):** 来自 Dynkin 图 S_3 对称的 triality 外自同构。第一个非-Galois、非-graph 的外自同构。它看起来像"k 是 mod m 下某个零散值的 Galois twist"还是需要新的机器？
- **上同调框架：** 整个图景是"环面的 Galois twist + 正则幂幺元的 cocycle 修正"。应该套进 Lang-Steinberg + Geck-Malle 的特征标表 Galois 作用。

今晚的内容比昨晚锐化一档。猜想陈述从"两个正交约束"压缩成"φ 的核"。而核出于干净的结构原因是循环的。三个 n ≥ 4 验证全中足以信任闭式。

:::
