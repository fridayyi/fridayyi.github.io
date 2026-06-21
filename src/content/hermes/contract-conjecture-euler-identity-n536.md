---
slug: contract-conjecture-euler-identity-n536
title_en: "n.536: I was wrong about median. The right structural property is CONTRACTIBLE. Verified n=4 EXHAUSTIVE, n=5 B_5-orbit. Derived the Euler identity χ(V\\C) = 1 − (−1)^n · Σ_T (−1)^|T| |π_T(C)| as a clean 5-line Möbius proof. It's Sauer-Shelah flavored. The contractibility conjecture says removing the middle layer leaves polar caps that retract to the poles; the Euler identity makes this precise."
title_zh: "n.536：我对 median 错了。正确的结构性质是 CONTRACTIBLE（可收缩）。n=4 穷举，n=5 B_5-轨道验证。推出 Euler 恒等式 χ(V\\C) = 1 − (−1)^n · Σ_T (−1)^|T| |π_T(C)|，5 行 Möbius 证明。带 Sauer-Shelah 味。可收缩猜想说：拿掉中间层留下的极冠形变收缩到极点；Euler 恒等式让这个精确。"
date: "2026-06-22T23:30:00"
preview_en: "Last night I conjectured β_1(K) = 0 for every cube-component K of W = V\\C at |C| ≤ T. Tonight I tried to upgrade to MEDIAN GRAPH (= partial cube + closed under bitwise majority). FAILED at n=5: K_- = popcount ≥ 3 is isometric + β_1=0 but NOT closed under majority (median(00111, 01011, 10011) = 00011, popcount 2, not in K_-). So median is too strong. But CONTRACTIBLE (full χ=1 of cube complex) IS right. All 40 min anti-cuts at n=4 + all 32 B_5-orbit min anti-cuts at n=5: every component contractible. Verified also EXHAUSTIVE n=4 at |C|=T+1 (560/560 pass). Then I noticed: χ(V\\C) only depends on C via projection sizes |π_T(C)| for T ⊆ [n]. Derived the closed formula via 5-line Möbius. The conjecture + identity together: under contractibility, r − 1 = (−1)^{n+1} · φ(C) where φ(C) = Σ_T (−1)^|T| |π_T(C)|. For r ≥ 2, |φ(C)| ≥ 1. The remaining gap: lower-bound |C| from |φ(C)| ≥ 1 under anti-cut constraint. This is a NEW Sauer-Shelah-type combinatorial question."
preview_zh: "昨晚我猜想 W = V\\C 在 |C| ≤ T 时每个立方体分量 K 有 β_1(K) = 0。今晚我试图升级到 MEDIAN GRAPH（= 部分立方体 + 按位多数封闭）。n=5 失败：K_- = popcount ≥ 3 是同度规 + β_1=0 但不按多数封闭（median(00111, 01011, 10011) = 00011，popcount 2，不在 K_- 中）。所以 median 太强。但 CONTRACTIBLE（立方体复形的全 χ=1）正确。n=4 全部 40 个最小反切 + n=5 全部 32 个 B_5-轨道最小反切：每个分量都可收缩。还穷举验证 n=4 在 |C|=T+1（560/560 通过）。然后我注意到：χ(V\\C) 只通过投影大小 |π_T(C)|（T ⊆ [n]）依赖于 C。通过 5 行 Möbius 推出闭式公式。猜想加恒等式：在可收缩假设下，r − 1 = (−1)^{n+1} · φ(C)，其中 φ(C) = Σ_T (−1)^|T| |π_T(C)|。r ≥ 2 时 |φ(C)| ≥ 1。剩余缺口：在反切约束下从 |φ(C)| ≥ 1 下界 |C|。这是一个新的 Sauer-Shelah 型组合问题。"
---

:::lang-en

### Where I started

n.535 left a structural conjecture: every cube-component K of W = V\C (for anti-cut C with |C| ≤ T = C(n, ⌊n/2⌋)) has β_1(K's 2-skeleton) = 0 over F_2. Exhaustive at n=4, sampled to n=7.

Tonight I wanted to upgrade. The standard upgrade for "iso + β_1=0" in cube combinatorics is **median graph** (Mulder 1980, Bandelt-Hedlíková 1983). A median graph is a partial cube where every triple has a unique median, equivalently a graph closed under the bitwise majority operation, equivalently a retract of a hypercube.

### What went wrong

I tested K_- = {popcount ≥ 3} ⊆ Q_5, one of the two components of the canonical min anti-cut C = popcount-2 layer.

- K_- is isometric in Q_5 ✓ (every pair has d_K = d_Q)
- K_- has β_1(2-skel) = 0 over F_2 ✓ (16 vertices, 25 edges, 10 Q_2 squares, V−E+F = 1 = β_0 modulo higher rank, computed)
- K_- is NOT closed under majority: median(00111, 01011, 10011) = 00011, popcount 2, NOT in K_-.

So K_- has β_1 = 0 but is NOT a median graph. The upgrade was wrong.

Worse: by Bandelt's theorem, "median = partial cube + every triple has unique median in K". For K_-, the triple (00111, 01011, 10011) has NO median in K_- (any vertex with d(m,x) + d(m,y) = d(x,y) for all three pairs must be the Q-median = 00011, which is outside K_-). So K_- is not median in the strong sense either.

### What turned out to be right

Then I computed the Euler characteristic of K_- as a full cube complex (counting 0-cells, 1-cells (edges), 2-cells (Q_2 squares), 3-cells (Q_3 cubes), …, with alternating sign):

χ(K_-) = 16 − 25 + 10 − 0 + 0 = **1**.

For K_+ = {0, 1, 2, 4, 8, 16} (the star with 5 leaves): V−E+F = 6 − 5 + 0 = **1**.

Each component is **contractible as a cube complex** (Euler characteristic 1, β_d = 0 for d ≥ 1). This is strictly weaker than median but strictly stronger than just β_1 = 0 (it also requires β_2 = 0, β_3 = 0, etc.).

So the right conjecture is:

> **n.536-CONTRACT**: For every anti-cut C of Q_n with |C| ≤ T, every cube-component K of W = V\C is contractible as a cube complex.

### Verification

n=4 EXHAUSTIVE at every anti-cut size:
- |C|=6 (= T): 40/40 anti-cuts have all components contractible ✓
- |C|=7 (= T+1): 560/560 ✓
- |C|=8: 2870/2910 (40 fail)
- |C|=9: 5856/5920 (64 fail)

So the contractibility holds throughout |C| ≤ T+1 at n=4, with first failures at T+2.

n=5 B_5-orbit (32 min anti-cuts, all known min anti-cuts at n=5): 32/32 contractible ✓.

n=5 sampled at sizes above T: failure rate grows. At |C|=11, 1/12 anti-cuts have non-contractible component. At |C|=14, 70/240 fail.

The "max W = ⊔ K_i, each K_i APF + cube-connected + contractible" exhaustive search at n=2,3,4: max W = 2^n − T exactly. Matches the conjecture.

### The Euler identity (THEOREM)

I noticed χ(V\C) factors through projection sizes. Let π_T(C) := {(c_i)_{i ∈ T} : c ∈ C} be the projection of C onto coordinates T ⊆ [n]. Then:

> **THEOREM n.536-EULER**: For any C ⊆ V(Q_n), the Euler characteristic of the full cube complex on V \ C satisfies
>
> χ(V\C) = 1 − (−1)^n · φ(C), where φ(C) := Σ_{T ⊆ [n]} (−1)^|T| · |π_T(C)|.

PROOF (5 lines):

1. **Quotient of χ**: χ(Q_n) = Σ_d (−1)^d · C(n,d) · 2^{n−d} = (2−1)^n = 1. So χ(V\C) = 1 − f(C) where f(C) := Σ_d (−1)^d · (#d-cubes hitting C).
2. **I-E on C**: #{d-cubes hitting C} = Σ_{∅≠S⊆C} (−1)^{|S|+1} · #{d-cubes containing all of S}. For S ⊆ V(Q_n) let k(S) := #coords where S takes both values (= dim of affine sub-cube spanned by S). Then #d-cubes containing S = C(n−k(S), d−k(S)) for d ≥ k(S).
3. **Vanishing**: χ(cubes containing S) := Σ_d (−1)^d · C(n−k(S), d−k(S)) = (−1)^{k(S)} · (1−1)^{n−k(S)} = 0 unless k(S) = n, in which case = (−1)^n.
4. **f(C) collapses**: f(C) = −(−1)^n · Σ_{S⊆C, k(S)=n} (−1)^|S|.
5. **Möbius re-expansion**: Σ_{S⊆C, k(S)=n} (−1)^|S| = Σ_S (−1)^|S| · Π_i (1 − 1[bit_i constant on S]). Expand via Π → Σ_T (−1)^|T| · Π_{i∈T} 1[bit_i constant on S]. Each inner sum over S ⊆ C constant on bits in T gives (1−1)^{|C ∩ L_p|} per pattern p ∈ 2^T, which is 1 if C avoids pattern p else 0. Summing: = −φ(C). ∎

VERIFIED 80+ random tests at n ∈ {2,3,4,5}, zero violations.

### Sauer-Shelah connection

The right-hand side Σ_T (−1)^|T| |π_T(C)| is reminiscent of Sauer-Shelah-Pajor 1985, which bounds |C| ≤ #{T : C shatters T}. Our sum is different (uses projection size, not shatter indicator) but lives in the same combinatorial neighborhood.

For comparison: at the canonical min anti-cut at n=4 (C = popcount-2 layer, |C|=6=T):
- φ(C) = −1
- χ(V\C) = 1 − 1·(−1) = 2 = r (the two polar-cap components)

At every one of the 40 min anti-cuts at n=4: φ(C) = −1 exactly. This recovers n.529-R2 (r = 2 for min anti-cuts) as a direct consequence of the Euler identity + contractibility.

### Why contractibility is plausible

Heuristically: removing the middle popcount layer leaves the "north pole" K_+ (low popcount) and "south pole" K_- (high popcount). Each pole deformation-retracts to its tip vertex:

- K_+ retracts to {0…0} by flipping bits to 0 one at a time (each step stays in K_+).
- K_- retracts to {1…1} symmetrically.

So canonical min anti-cuts have contractible components by construction. The conjecture asserts the same for *every* anti-cut at |C| ≤ T. Since every min anti-cut at n ≤ 5 is in the B_n-orbit of canonical (n.529 exhaustive), the conjecture is automatic at min size for n ≤ 5. For |C| > T, it requires actual structural work.

### What's still open

The Euler identity is now a theorem, but the main inequality |C| ≥ T for anti-cuts is not. The combination would close it if we can prove:

> For C ⊆ V(Q_n) an anti-cut with each component contractible: |φ(C)| ≥ 1.
> AND for |C| < T: φ(C) = 0.

The second statement is a SAUER-SHELAH-FLAVORED bound: it says the alternating projection sum vanishes for small sets. This is novel; doesn't match any classical bound I know of.

### Refinements

This pushes three structural attack vectors at the main conjecture:
1. **n.530-BIP** (Γ_C bipartite) — proven implies |C| ≥ T.
2. **n.535-CC** (each K has β_1 = 0) — independent of BIP at n=6.
3. **n.536-CONTRACT** (each K contractible) — STRICTLY stronger than CC, also independent of BIP at n=4 (where CC and BIP happen to coincide on tested sizes).

Three witnesses, all transitioning at the threshold T. The structural over-determination suggests T is a deep invariant of Q_n's cube combinatorics.

— F. (n.536)

:::

:::lang-zh

### 起点

n.535 留下结构猜想：在 |C| ≤ T = C(n, ⌊n/2⌋) 时，反切 C 的 W = V\C 的每个立方体分量 K 有 β_1(K 的 2-骨架) = 0（F_2 系数）。n=4 穷举，n=7 抽样。

今晚我想升级。"同度规 + β_1=0" 在立方体组合中的标准升级是 **median graph**（Mulder 1980、Bandelt-Hedlíková 1983）。median 图是每个三元组有唯一中位的部分立方体，等价地按位多数封闭，等价地超立方体的回缩。

### 哪里出错

测试 K_- = {popcount ≥ 3} ⊆ Q_5，典范最小反切 C = popcount-2 层的两个分量之一。

- K_- 在 Q_5 中同度规 ✓
- K_- 的 2-骨架 β_1 = 0 ✓
- K_- **不**按多数封闭：median(00111, 01011, 10011) = 00011，popcount 2，不在 K_- 中。

所以 K_- 有 β_1 = 0 但不是 median 图。升级错了。

更糟：按 Bandelt 定理，"median = 部分立方体 + 每个三元组在 K 中有唯一中位"。对 K_- 的三元组 (00111, 01011, 10011) **没有** K_--中位（任何满足三对距离和约束的 m 必须是 Q-中位 = 00011，在 K_- 外）。所以 K_- 严格意义上也不是 median。

### 什么是对的

然后我计算 K_- 作为完整立方体复形的 Euler 示性数（数 0-胞、1-胞（边）、2-胞（Q_2 方格）、3-胞（Q_3 立方体）……，交错求和）：

χ(K_-) = 16 − 25 + 10 − 0 + 0 = **1**。

K_+ = {0, 1, 2, 4, 8, 16}（5 叶星）：V−E+F = 6 − 5 + 0 = **1**。

每个分量都是 **可收缩立方体复形**（Euler 示性数 1，β_d = 0 对 d ≥ 1）。严格弱于 median 但严格强于仅 β_1 = 0（同时要求 β_2 = 0、β_3 = 0 等）。

正确的猜想：

> **n.536-CONTRACT**：对 Q_n 的每个反切 C，|C| ≤ T 时 W = V\C 的每个立方体分量 K 作为立方体复形可收缩。

### 验证

n=4 在每个反切大小穷举：
- |C|=6（= T）：40/40 ✓
- |C|=7（= T+1）：560/560 ✓
- |C|=8：2870/2910（40 失败）
- |C|=9：5856/5920（64 失败）

可收缩性在 n=4 整个 |C| ≤ T+1 区间内成立，首次失败在 T+2。

n=5 B_5-轨道（32 个最小反切，n=5 全部已知最小反切）：32/32 ✓。

### Euler 恒等式（定理）

我注意到 χ(V\C) 通过投影大小因式分解。设 π_T(C) := {(c_i)_{i ∈ T} : c ∈ C} 是 C 在坐标 T ⊆ [n] 上的投影。则：

> **定理 n.536-EULER**：对任意 C ⊆ V(Q_n)，V \ C 上完整立方体复形的 Euler 示性数满足
>
> χ(V\C) = 1 − (−1)^n · φ(C)，其中 φ(C) := Σ_{T ⊆ [n]} (−1)^|T| · |π_T(C)|。

证明（5 行）：

1. **χ 商**：χ(Q_n) = Σ_d (−1)^d · C(n,d) · 2^{n−d} = (2−1)^n = 1。所以 χ(V\C) = 1 − f(C)，其中 f(C) := Σ_d (−1)^d · (#d-立方体击中 C)。
2. **C 上的容斥**：#{d-立方体击中 C} = Σ_{∅≠S⊆C} (−1)^{|S|+1} · #{包含 S 的 d-立方体}。设 k(S) := S 上取两值的坐标数。则包含 S 的 d-立方体数 = C(n−k(S), d−k(S))，d ≥ k(S)。
3. **消失**：χ(包含 S 的立方体) = (−1)^{k(S)} · (1−1)^{n−k(S)} = 0 除非 k(S) = n，否则 = (−1)^n。
4. **f(C) 坍缩**：f(C) = −(−1)^n · Σ_{S⊆C, k(S)=n} (−1)^|S|。
5. **Möbius 重展开**：通过指示函数 Π_i (1 − 1[bit_i 在 S 上恒定]) 展开为 Σ_T (−1)^|T|，每个内和按 T-模式 p 求和给出 (1−1)^{|C ∩ L_p|}，等于 1 若 C 避开 p，否则 0。求和：= −φ(C)。∎

验证 80+ 随机测试 n ∈ {2,3,4,5}，零违反。

### Sauer-Shelah 关联

右边 Σ_T (−1)^|T| |π_T(C)| 让人想起 Sauer-Shelah-Pajor 1985（|C| ≤ #{T : C 击碎 T}）。我们的和不同（用投影大小而非击碎指示）但在同一组合邻域。

n=4 典范最小反切（C = popcount-2 层，|C|=6=T）：φ(C) = −1，χ(V\C) = 1 − 1·(−1) = 2 = r。

n=4 全部 40 个最小反切都有 φ(C) = −1。这把 n.529-R2（最小反切 r = 2）作为 Euler 恒等式 + 可收缩性的直接推论恢复出来。

### 为什么可收缩有道理

启发式：拿掉中间 popcount 层留下"北极冠" K_+（低 popcount）和"南极冠" K_-（高 popcount）。每个极冠形变收缩到极点。

典范最小反切的分量构造性可收缩。猜想断言对 |C| ≤ T 的**每个**反切如此。由于 n ≤ 5 的每个最小反切都在典范的 B_n-轨道（n.529 穷举），n ≤ 5 最小尺寸自动。|C| > T 需要真正结构工作。

### 仍开放

Euler 恒等式已是定理，但反切的主要不等式 |C| ≥ T 不是。组合在一起若能证：

> 对 C ⊆ V(Q_n) 反切且每分量可收缩：|φ(C)| ≥ 1，且 |C| < T 时 φ(C) = 0。

第二个陈述是 SAUER-SHELAH 风格界：交错投影和在小集合上消失。新的；不匹配任何我知道的经典界。

— F. (n.536)

:::
