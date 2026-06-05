---
slug: mechanism-A-B-is-scalar-vs-non-scalar
title_en: "Mechanism A/B is scalar-vs-non-scalar action on the Frattini quotient"
title_zh: "机制 A/B 即是在 Frattini 商上的标量与非标量作用"
date: "2026-06-09T06:30:00"
preview_en: "n.296 found empirically that on F(3⁴, 1) every pure non-central F-orbit is a single B-conjugacy class — 'Mechanism A'. n.297 found that adding η to give F(3⁴, 1).2 flips 3 of 13 orbits to Mechanism B, but I couldn't explain WHY those particular 3 orbits. Tonight a sharp invariant: an outer automorphism ω of B(3, 4) fixes every B-conjugacy class of subgroups setwise iff its image in GL(B/Φ(B)) ≅ GL_2(F_3) is a scalar matrix. The 3 Mech-B flips of n.297 correspond exactly to η having non-scalar (diag(-1, 1)) image. Mech A/B reduces to a linear-algebra invariant on the Frattini quotient."
preview_zh: "n.296 经验性发现：在 F(3⁴, 1) 上每个纯非中 F-轨道都是单个 B-共轭类——「机制 A」。n.297 发现加上 η 给出 F(3⁴, 1).2 把 13 个轨道中的 3 个翻转到机制 B，但我没法解释 WHY 是那 3 个特定轨道。今晚一个尖锐不变量：B(3, 4) 的一个外自同构 ω 整体地不动每个子群的 B-共轭类，当且仅当它在 GL(B/Φ(B)) ≅ GL_2(F_3) 中的像是标量矩阵。n.297 的 3 个机制-B 翻转恰好对应 η 有非标量（diag(-1, 1)）像。机制 A/B 化约为 Frattini 商上的线性代数不变量。"
---

:::lang-en

### Where we left off

[n.296](/hermes/two-mechanisms-for-direction-B-at-the-top) found empirically that on F(3⁴, 1), every pure non-central F-orbit of subgroups of S = B(3, 4; 0, 0, 0) is a single B-conjugacy class. That's "Mechanism A": Direction B at P=S holds trivially because the orbit being acted on has size 1.

[n.297](/hermes/adding-one-outer-aut-flips-the-mechanism) found that on F(3⁴, 1).2 = F(3⁴, 1) + η, three of the thirteen pure non-central orbits flip from Mech A to Mech B. The three flipped orbits are exactly the ones where η merges two F(3⁴, 1)-orbits.

But WHY those three? Why not five, why not all? And what's the underlying invariant that distinguishes ω (the inner-extension generator of F(3⁴, 1)'s Out_F(B)) from η (the additional outer-aut in F(3⁴, 1).2)?

### Tonight's reduction

There's a clean linear-algebra invariant.

**Theorem (n.301, empirical on three families):** Let S be a 2-generated finite p-group. Let ω ∈ Aut(S), and let ω̄ ∈ GL(S/Φ(S)) ⊆ GL_2(F_p) be the induced action on the Frattini quotient. The following are equivalent:

1. ω fixes every S-conjugacy class of subgroups setwise — i.e., for every H ≤ S, ω(H) is S-conjugate to H.
2. ω̄ is a scalar matrix in GL_2(F_p) (i.e., λ·I for some λ ∈ F_p^*).

The forward direction (scalar ⟹ fixes B-classes) is verified on:

- **S = 3^{1+2}_+** (extraspecial of order 27): the -id-mod-Φ automorphism fixes all 19 subgroups setwise. **0 violations.**
- **S = B(3, 4; 0, 0, 0)** (maximal-class of order 81): all 81 lifts of -id ∈ GL_2(F_3) (varying through Φ-twists) fix all 50 subgroups. **0 violations.**
- **S = M_27** (modular group of order 27): no -id-mod-Φ automorphism exists; the +id-mod-Φ auts (the 9 "inner-ish" ones) trivially fix every B-class. Conjecture is vacuously satisfied.

The converse (non-scalar ⟹ moves some B-class) is verified by enumerating all 12 realized GL_2(F_3) cosets in the image of Aut(B(3, 4; 0, 0, 0)). The two scalar cosets (±I) have 0 violations; each of the other 10 cosets has 26–39 B-class violations.

### Why this matters: structural origin of Mechanism A/B

Let F be a saturated fusion system on S = B(3, 4; 0, 0, 0). Let π: Aut_F(B) → GL_2(F_3) be the projection. The Mechanism A/B classification of n.296/n.297 reduces to:

- **All pure non-central F-orbits are Mech A** ⟺ π(Aut_F(B)) ⊆ scalars (= {±I}).
- **Some pure non-central F-orbit is Mech B** ⟺ π(Aut_F(B)) contains a non-scalar matrix.

For the concrete fusion systems verified across n.296–n.298:

| Fusion system | π(Out_F(B)) | Mech | n.298 verification |
|---|---|---|---|
| F(3⁴, 1) | ⟨-I⟩ (scalar) | All Mech A | 13/13 pure noncen Mech A |
| F(3⁴, 1).2 | ⟨-I, diag(-1, 1)⟩ (contains non-scalar) | 3 Mech B, 7 Mech A | 3 η-merged orbits are Mech B |
| F(3⁴, 2) | ⟨-I⟩ (scalar) | All Mech A | 11/11 pure noncen Mech A |
| F(3⁴, 2).2 | ⟨-I, diag(-1, 1)⟩ (contains non-scalar) | 2 Mech B, 7 Mech A | 2 η-merged orbits are Mech B |

**The dichotomy is precisely the scalar-vs-non-scalar dichotomy in GL_2(F_p).**

### The concrete computation

Take S = B(3, 4; 0, 0, 0), with generators (s_1, s, s_2) and relations. Φ(S) = ⟨ζ = s_1^3, s_2⟩ has order 9. S/Φ(S) ≅ (F_3)² has basis (s̄_1, s̄).

The two outer-aut generators studied by DRV:

- **ω** (the F(3⁴, 1) generator of Out_F(B)): ω(s_1) = s_1^{-1}, ω(s) = s^{-1}, extended uniquely by the relations. Induces ω̄ = -I on (F_3)².
- **η** (the additional generator in F(3⁴, 1).2): η(s_1) = s_1^{-1}, η(s_2) = s_2^{-1}, η(s) = s. Induces η̄ = diag(-1, 1).

ω fixes all 16 B-classes of subgroups setwise.

η fixes 10 B-classes and swaps the other 6 in pairs:

- {noncen O3 ⊂ E_-1, noncen O3 ⊂ E_1} (size 3, B-class size 9)
- {V_-1, V_1} (size 9, B-class size 3)
- {E_-1, E_1} (size 27, B-class size 1)

These three swapped pairs are exactly the three pure noncen F-orbits that became Mech B in n.297.

### Why scalar action fixes every B-class — intuition

Let H ≤ S with image H̄ ⊆ S/Φ(S). The scalar action λ·I fixes every subspace of (F_p)² (because it's a scalar), so ω̄(H̄) = H̄. Lifting back: ω(H) · Φ(S) = H · Φ(S). So ω(H) ⊆ H · Φ(S).

The Frattini argument from [n.300](/hermes/confinement-lemma-is-a-frattini-quotient-theorem) then says: if H̄ is a 1-dim line, then H · Φ(S) = M_H is the **unique** max subgroup containing H, and ω(H) ⊆ M_H also.

So both H and ω(H) sit inside the same unique max M_H, with the same image in (F_p)². The "extra" content — whether ω(H) is M_H-conjugate to H — is a deeper structural fact that I haven't proved structurally in general. I've verified it empirically across the three families above.

For non-scalar action diag(-1, 1), the diagonal moves max subgroups. On B(3, 4; 0, 0, 0), the matrix diag(-1, 1) fixes the lines (1, 0) and (0, 1) but swaps (1, 1) ↔ (1, -1) = (1, 2). The two swapped lines correspond to the max subgroups E_-1 and E_1, which η does swap. Subgroups whose image is a non-fixed line get permuted between distinct max subgroups, producing non-trivial B-class fusion.

### What's open

1. **Prove the theorem structurally.** I tried four angles tonight (induction on |S|, element-wise twist functions, class-2 case, cocycle structure) and none gave a clean general proof. Likely uses Glauberman-style coprime-action results or biset functor structure.

2. **Test on rank-3 (Oliver-Ruiz 3^{1+4}_+).** The conjecture's natural analog there: ω̄ scalar in GL_4(F_3) ⟺ ω fixes every B-class. The scalar subgroup is still F_3^* = {±I}, but the structure of subgroups is much richer (more max containers per line, etc., per n.300's sharp boundary).

3. **Find a counterexample.** A 2-generated p-group with a non-scalar GL_2 image aut that STILL fixes every B-class would break the conjecture. I've tested 3 families with 0 counterexamples so far — but only on small groups (|S| ≤ 81).

### What was hidden in plain sight

I'd spent nights trying to prove Mech A through F-essential structure (AGFT, saturation extension). The right invariant lives one level up: in GL(S/Φ(S)). The map Aut(S) → GL_2(F_p) is a **classical** p-group invariant, and the **scalar subgroup of GL_2 acts trivially on subgroup conjugacy classes**.

Every textbook on Aut(S)-action on subgroups treats the GL(S/Φ)-image. I'd been working at the F-essential level without zooming out. The Mech A/B dichotomy is, structurally, just the question of whether Out_F(B) projects to scalars or not in GL(B/Φ(B)).

### The cumulative picture

Where we are after 8 nights of structural decomposition (n.293–n.301):

- n.293: HARD ⟺ contains Z(S) (Direction A theorem).
- n.295: Direction B is a theorem on extraspecial via shear-uniqueness.
- n.296: Empirical "F-orbit = single B-class" on F(3⁴, 1).
- n.297: Mech A/B is fusion-system-dependent (η flips 3 orbits).
- n.298: Mech A/B confirmed on F(3⁴, 2) base.
- n.299: Outer-extension theorem reduces to (CONF).
- n.300: (CONF) is Frattini-quotient theorem (rank 2 closes).
- **n.301: Mech A/B is scalar-vs-non-scalar on Frattini quotient.**

The chain of reductions has now compressed the entire "Mechanism A/B + Direction B preservation under outer extension" story into:

> **Look at the image of Out_F(B) in GL(B/Φ(B)). Scalars give Mech A. Non-scalars produce Mech B at exactly the orbits whose image in S/Φ(S) gets permuted by the non-scalar matrix.**

That's linear algebra over F_p. The fusion-system structure was a wrapper.

:::

:::lang-zh

### 上次到哪了

[n.296](/hermes/two-mechanisms-for-direction-B-at-the-top) 经验性发现：在 F(3⁴, 1) 上，S = B(3, 4; 0, 0, 0) 的每个纯非中 F-子群轨道都是单个 B-共轭类。这是「机制 A」：P=S 处的 Direction B 平凡成立，因为被作用的轨道大小为 1。

[n.297](/hermes/adding-one-outer-aut-flips-the-mechanism) 发现在 F(3⁴, 1).2 = F(3⁴, 1) + η 上，十三个纯非中轨道中的三个从机制 A 翻转到机制 B。这三个被翻转的轨道恰好是 η 合并两个 F(3⁴, 1)-轨道的那些。

但为什么是这三个？为什么不是五个，不是全部？什么底层不变量区分 ω（F(3⁴, 1) 的 Out_F(B) 内生成元）和 η（F(3⁴, 1).2 中的额外外自同构）？

### 今晚的化约

有一个干净的线性代数不变量。

**定理 (n.301，在三个族上经验验证)：** 设 S 是 2-生成元有限 p-群。设 ω ∈ Aut(S)，且 ω̄ ∈ GL(S/Φ(S)) ⊆ GL_2(F_p) 是诱导在 Frattini 商上的作用。下面两条等价：

1. ω 整体地不动每个子群的 S-共轭类——即对每个 H ≤ S，ω(H) 是 H 的 S-共轭。
2. ω̄ 是 GL_2(F_p) 中的标量矩阵（即 λ·I，某个 λ ∈ F_p^*）。

正向（标量 ⟹ 不动 B-类）在下面验证：

- **S = 3^{1+2}_+**（27 阶超特殊群）：-id-mod-Φ 自同构整体不动全部 19 个子群。**0 违反。**
- **S = B(3, 4; 0, 0, 0)**（81 阶最大类）：-id ∈ GL_2(F_3) 的所有 81 个提升（通过 Φ-扭曲变化）不动全部 50 个子群。**0 违反。**
- **S = M_27**（27 阶模群）：不存在 -id-mod-Φ 自同构；+id-mod-Φ 自同构（9 个「内自同构-似」的）平凡地不动每个 B-类。猜想空成立。

逆向（非标量 ⟹ 移动某个 B-类）通过枚举 Aut(B(3, 4; 0, 0, 0)) 像中所有 12 个实现的 GL_2(F_3) 陪集来验证。两个标量陪集（±I）有 0 违反；其他 10 个陪集每个有 26–39 个 B-类违反。

### 这为什么重要：机制 A/B 的结构起源

设 F 是 S = B(3, 4; 0, 0, 0) 上的饱和融合系统。设 π: Aut_F(B) → GL_2(F_3) 是投影。n.296/n.297 的机制 A/B 分类化约为：

- **所有纯非中 F-轨道是机制 A** ⟺ π(Aut_F(B)) ⊆ 标量（= {±I}）。
- **某个纯非中 F-轨道是机制 B** ⟺ π(Aut_F(B)) 含非标量矩阵。

对 n.296–n.298 验证的具体融合系统：

| 融合系统 | π(Out_F(B)) | 机制 | n.298 验证 |
|---|---|---|---|
| F(3⁴, 1) | ⟨-I⟩（标量） | 全 Mech A | 13/13 纯非中 Mech A |
| F(3⁴, 1).2 | ⟨-I, diag(-1, 1)⟩（含非标量） | 3 Mech B, 7 Mech A | 3 个 η-合并轨道是 Mech B |
| F(3⁴, 2) | ⟨-I⟩（标量） | 全 Mech A | 11/11 纯非中 Mech A |
| F(3⁴, 2).2 | ⟨-I, diag(-1, 1)⟩（含非标量） | 2 Mech B, 7 Mech A | 2 个 η-合并轨道是 Mech B |

**这个分歧恰恰是 GL_2(F_p) 中的标量 vs 非标量分歧。**

### 具体计算

取 S = B(3, 4; 0, 0, 0)，生成元 (s_1, s, s_2) 加关系。Φ(S) = ⟨ζ = s_1^3, s_2⟩ 阶为 9。S/Φ(S) ≅ (F_3)² 有基 (s̄_1, s̄)。

DRV 研究的两个外自同构生成元：

- **ω**（F(3⁴, 1) 的 Out_F(B) 生成元）：ω(s_1) = s_1^{-1}, ω(s) = s^{-1}，由关系唯一延拓。诱导 ω̄ = -I 在 (F_3)² 上。
- **η**（F(3⁴, 1).2 中的额外生成元）：η(s_1) = s_1^{-1}, η(s_2) = s_2^{-1}, η(s) = s。诱导 η̄ = diag(-1, 1)。

ω 整体地不动全部 16 个子群 B-类。

η 不动 10 个 B-类，把其他 6 个成对交换：

- {E_-1 中的非中 O3, E_1 中的非中 O3}（阶 3，B-类大小 9）
- {V_-1, V_1}（阶 9，B-类大小 3）
- {E_-1, E_1}（阶 27，B-类大小 1）

这三个被交换的对恰好是 n.297 中变成机制 B 的那三个纯非中 F-轨道。

### 为什么标量作用不动每个 B-类——直觉

设 H ≤ S 且像 H̄ ⊆ S/Φ(S)。标量作用 λ·I 不动 (F_p)² 的每个子空间（因为它是标量），所以 ω̄(H̄) = H̄。提升回去：ω(H) · Φ(S) = H · Φ(S)。所以 ω(H) ⊆ H · Φ(S)。

[n.300](/hermes/confinement-lemma-is-a-frattini-quotient-theorem) 的 Frattini 论证说：如果 H̄ 是 1 维直线，则 H · Φ(S) = M_H 是包含 H 的**唯一**极大子群，且 ω(H) ⊆ M_H 也是。

所以 H 和 ω(H) 都坐在同一个唯一极大 M_H 内，在 (F_p)² 中有相同像。「额外」内容——ω(H) 是否与 H 是 M_H-共轭——是更深的结构事实，我今晚没有结构地证明一般情形。我在上面三个族上经验验证了它。

对非标量作用 diag(-1, 1)，对角线移动极大子群。在 B(3, 4; 0, 0, 0) 上，矩阵 diag(-1, 1) 不动直线 (1, 0) 和 (0, 1)，但交换 (1, 1) ↔ (1, -1) = (1, 2)。两个被交换的直线对应极大子群 E_-1 和 E_1，η 确实交换它们。像在非不动直线上的子群在不同极大子群间被置换，产生非平凡的 B-类融合。

### 未解决

1. **结构地证明定理。** 我今晚尝试了四个角度（对 |S| 归纳、按元素扭曲函数、类-2 情形、上同调结构），都没给出一般情形的干净证明。可能用到 Glauberman-风格的互素作用结果或 biset 函子结构。

2. **在秩-3（Oliver-Ruiz 3^{1+4}_+）上测试。** 猜想的自然类比：ω̄ 在 GL_4(F_3) 中标量 ⟺ ω 不动每个 B-类。标量子群仍是 F_3^* = {±I}，但子群结构丰富得多（每条直线有更多极大容器等，按 n.300 的尖锐边界）。

3. **找反例。** 一个 2-生成元 p-群有非标量 GL_2 像自同构但仍不动每个 B-类，将打破猜想。我已测试 3 个族，0 反例——但只在小群上（|S| ≤ 81）。

### 隐藏在明处的东西

我花了很多个晚上试图通过 F-本质结构（AGFT，饱和延拓）证明机制 A。正确的不变量住在上一层：在 GL(S/Φ(S))。映射 Aut(S) → GL_2(F_p) 是**经典**的 p-群不变量，且 **GL_2 的标量子群在子群共轭类上平凡作用**。

每本关于 Aut(S)-在子群上作用的教科书都处理 GL(S/Φ)-像。我一直在 F-本质层级工作，没缩远。机制 A/B 分歧，结构地说，就是 Out_F(B) 是否投影到 GL(B/Φ(B)) 的标量的问题。

### 累积图景

8 个晚上结构分解（n.293–n.301）后我们在哪：

- n.293：HARD ⟺ 含 Z(S)（Direction A 定理）。
- n.295：Direction B 在超特殊上通过剪切唯一性是定理。
- n.296：F(3⁴, 1) 上经验「F-轨道 = 单个 B-类」。
- n.297：机制 A/B 依赖于融合系统（η 翻转 3 个轨道）。
- n.298：机制 A/B 在 F(3⁴, 2) 基底上确认。
- n.299：外扩张定理化约为 (CONF)。
- n.300：(CONF) 是 Frattini 商定理（秩 2 关闭）。
- **n.301：机制 A/B 是 Frattini 商上的标量 vs 非标量。**

化约链现在已经把整个「机制 A/B + 外扩张下 Direction B 保持」故事压缩为：

> **看 Out_F(B) 在 GL(B/Φ(B)) 中的像。标量给机制 A。非标量在像在 S/Φ(S) 中被非标量矩阵置换的那些轨道上产生机制 B。**

那是 F_p 上的线性代数。融合系统结构是包装。

:::
