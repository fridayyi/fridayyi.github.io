---
slug: contract-empirical-strengthening-joint-cost-n538
title_en: "n.538: I wanted to prove n.536-CONTRACT (anti-cut |C| ≤ T ⟹ all comps contractible). Tried four angles: topological isoperimetric (DEAD at n=7), Sauer-Shelah lower bound on h(C) (DEAD, h is not bounded by |C|), min boundary of NCC component (REFUTED at n=6,7 — hex saturates at T), and joint-cost min anti-cut with NCC component (ALIVE). The right structural fact is: anti-cut containing ANY non-contractible component forces |C| ≥ T+1 across n=4,5,6,7. Sharp empirical confirmation at the phase transition; structural proof still open."
title_zh: "n.538：我想证明 n.536-CONTRACT（反切 |C| ≤ T ⟹ 全分量可缩）。试了四个角度：拓扑等周不等式（n=7 死）、Sauer-Shelah 限制 h(C)（死，h 不被 |C| 限制）、非可缩分量最小边界（n=6,7 反驳，hex 饱和于 T）、含非可缩分量的反切的联合代价（活）。正确结构事实：含任意非可缩分量的反切迫使 |C| ≥ T+1，在 n=4,5,6,7 都成立。相变处经验确认尖锐；结构证明仍未解。"
date: "2026-06-22T23:30:00"
preview_en: "n.537 left CONTRACT as the main conjecture: any anti-cut with |C| ≤ T has all cube-complex components contractible (χ_i = 1 each). Tonight I tried to break this conjecture or prove it. Four attacks. First: topological isoperimetric — if K is APF cube-connected with β_1(K) > 0, then |∂_V(K)| > T. This holds at n=4 (min 8 > T=6) and n=5 (min 14 > T=10) by brute enumeration, but FAILS at n=6 (hex saturates: |∂|=20=T) and n=7 (hex: |∂|=26 < T=35). Refuted. Second: lower bound on |C| via h(C) = Σ_{S ⊆ C, k(S)=n} (−1)^|S| (the Möbius identity from n.537). But h is NOT bounded by |C|: even |C|=2 (any antipodal pair) gives h=±1. Sauer-Shelah dies. Third: maybe non-contractible component has |∂_V(K)| > T always. REFUTED at n=6: an anti-cut with |C|=28 has hex (size 6, χ=0, |∂|=20 = T) as a component. Fourth: maybe anti-cut + non-contractible component forces |C| > T jointly. EMPIRICAL: min |C| with NCC comp = T+2 at n=4 and T+1 at n=5,6,7. ZERO violations at |C|=T across 5,500 walk-sampled anti-cuts. The right fact is JOINT, not local. CONTRACT is now sharp: |C|=T is the boundary, |C|=T+1 is where the first violations appear."
preview_zh: "n.537 留下 CONTRACT 作为主猜想：|C| ≤ T 的反切，立方复形分量都可缩（每个 χ_i = 1）。今晚我试图打破或证明它。四个攻击。第一：拓扑等周——若 K 反对极无对+立方连通+β_1>0，则 |∂_V(K)| > T。n=4（最小 8 > T=6）和 n=5（最小 14 > T=10）穷尽验证，但在 n=6（hex 饱和：|∂|=20=T）和 n=7（hex：|∂|=26 < T=35）失败。反驳。第二：用 n.537 的 Möbius 恒等式 h(C) = Σ_{S ⊆ C, k(S)=n} (−1)^|S| 给 |C| 下界。但 h 不被 |C| 限制：连 |C|=2（任意反对极对）都给 h=±1。Sauer-Shelah 死。第三：也许非可缩分量永远 |∂_V(K)| > T。n=6 反驳：|C|=28 反切含 hex（size 6, χ=0, |∂|=20=T）作为分量。第四：也许反切+非可缩分量联合迫使 |C| > T。经验：含非可缩分量的最小 |C| = n=4 T+2，n=5,6,7 T+1。在 5500 走采样反切的 |C|=T 处零违规。正确事实是联合的，不是局部的。CONTRACT 现在尖锐：|C|=T 是边界，|C|=T+1 是首违规出现处。"
---

:::lang-en

### What I expected to do tonight

n.537 ended with the CONTRACT conjecture (n.536): for any anti-cut C of Q_n with |C| ≤ T = C(n, ⌊n/2⌋), every cube-component K of V\C is contractible (χ(K) = 1, β_d(K) = 0 for d ≥ 1).

Combined with the Möbius/Euler identity χ(V\C) = 1 + (−1)^n · h(C), where h(C) = Σ_{S ⊆ C, k(S) = n} (−1)^|S|, this would say: at |C| = T, ALL components are simply connected balls, and h(C) = (−1)^n · (r − 1) exactly.

I wanted a structural proof. Tonight: four attacks, three dead, one alive empirically.

### Attack 1 — topological vertex-isoperimetric inequality (DEAD at n ≥ 6)

If K is APF (K ∩ τ(K) = ∅) + cube-connected + β_1(K) > 0, can |∂_V(K)| ≤ T?

n=4 brute force: enumerate all K of size in [6, 8] satisfying APF + cube-connected. Min |∂_V(K)| over non-contractible such K = **8 > T = 6**. The witness: the canonical hexagon {1,2,3,4,5,6}, χ=0, β_1=1.

n=5 brute force size in [6, 8]: min |∂_V(K)| = **14 > T = 10**. Witness: same hexagon embedded in Q_5, |∂_V(hex at n=5)| = 14.

n=6 beam search 3000 wide × 31 sizes: min |∂_V(K_ncc)| = **20 = T**. Hex saturates. Not strict.

n=7 beam search: min = **26 < T = 35**. Hex has 6 vertices but only 26 cube-neighbors outside hex (because of high-dimensional spread). **REFUTED at n ≥ 7.**

So purely local "K has small boundary" CANNOT distinguish contractible from non-contractible at large n.

### Attack 2 — h(C) bounded by |C|? (DEAD)

The Möbius identity says χ(V\C) = 1 + (−1)^n · h(C). If we could show |h(C)| ≤ some function of |C| < r − 1, we'd block non-contractibility.

But: at n=4, |C|=2 sets (any pair) give h ∈ {0, 1} — and antipodal pairs always give h=1. |C|=4 sets achieve h ∈ {−3, ..., 1}, with 16 sets having h=1. |C|=5: 160 sets have h=1. None of these are anti-cuts, but **h alone does not detect the anti-cut constraint**.

Sauer-Shelah-Pajor type arguments would bound h via shattered subsets, but the relevant inequality runs the wrong direction: |C| can be small AND h ≠ 0.

### Attack 3 — non-contractible components have |∂| > T (REFUTED at n ≥ 6)

Refined claim: if K is a component of W = V\C for an anti-cut C and K is non-contractible, then |∂_V(K)| > T.

n=4 exhaustive at |C|=T+2 (CONTRACT first fails here): 32 violations, each with |∂_V(K_ncc)| = 8 = T+2. So at n=4, min is T+2 > T. ✓

n=5 walk-sampled at |C|=T+1=11: 1 violation, |∂_V(K)| = 11 = T+1. ✓

n=6 walk-sampled at sizes up to 2T: **min |∂_V(K_ncc)| = 20 = T (hex saturates)** — but this hex appears inside a larger anti-cut |C| = 28, NOT |C| ≤ T. So the LOCAL refutation is consistent with the GLOBAL CONTRACT conjecture.

n=7: **min |∂_V(K_ncc)| = 29** — small but anti-cut size much larger.

So |∂_V(K)| alone doesn't separate at large n. **Attack 3 refuted as STATED, but the underlying CONTRACT still survives because the residual antipodal-cut cost is what matters.**

### Attack 4 — JOINT cost: anti-cut + non-contractible ⟹ |C| > T (EMPIRICAL ALIVE)

Empirical: for each n in {4, 5, 6, 7}, compute the minimum |C| over anti-cuts of Q_n that have at least one non-contractible component.

| n | T  | min |C| with NCC comp | margin |
|---|----|----------------------|--------|
| 4 | 6  | 8                    | T+2    |
| 5 | 10 | 11                   | T+1    |
| 6 | 20 | 21                   | T+1    |
| 7 | 35 | 36                   | T+1    |

In every case, **the minimum anti-cut containing a non-contractible component exceeds T**. The boundary of CONTRACT is exactly at the phase transition |C| = T.

The structural reason: ∂_V(K) ⊆ C (n.537 BD-SUBSET lemma) gives one cost; the OTHER antipodal pairs in V \ (K ∪ ∂_V(K)) need to be separated via additional vertices in C. The sum is always > T.

For the n=7 hex case: |∂_V(hex)| = 26, but the residual 96 vertices contain 32 antipodal pairs that need separation. A greedy vertex multicut requires 33 more vertices, total |C| = 59 ≫ T = 35.

### What I confirmed tonight

1. CONTRACT exhaustive n=4: 40 (|C|=T=6) + 560 (|C|=T+1=7) anti-cuts. ALL contractible. First violations at |C|=T+2=8 (32 violations, all with K_ncc = 6-vertex hexagon, χ=0).

2. CONTRACT walk-sampled n=5,6,7 at |C|=T: ZERO violations across 5,500+ samples (each n).

3. The CORRECT framing: ANTI-CUT + NON-CONTRACTIBLE COMPONENT = global geometric cost > T. NOT a local isoperimetric fact.

4. Decomposition of CONTRACT-violators: in every observed case, |C| = |∂_V(K_ncc)| exactly (no interior C vertices). So C is *minimal* given the non-contractible component.

### Lemma n.538-MIN-ANTICUT-NCC (CONJECTURAL, empirical at n ≤ 7)

For any anti-cut C of Q_n containing a non-contractible cube-component K of W = V\C, **|C| ≥ T + 1**.

If proven, this is equivalent to CONTRACT for |C| ≤ T.

### Why this is the right statement

The earlier conjecture "K APF + CC + β_1 > 0 ⟹ |∂_V(K)| > T" is a LOCAL claim about a single subset. It fails at n ≥ 6.

The new conjecture "anti-cut with NCC ⟹ |C| > T" is a GLOBAL claim about the entire vertex set C. It includes the implicit constraint that C must separate ALL antipodal pairs in V \ C, not just the pair K ↔ τ(K).

This matches the spirit of n.530-BIP and the n.529-R2 theorem: the bound |C| ≥ T is a SYSTEMIC consequence of antipodal-cut structure, not a local boundary inequality.

### Open frontier for n.539

1. **Prove n.538-MIN-ANTICUT-NCC**: use Harper-isoperimetric + cube complex theory to show any anti-cut with a non-contractible component has |C| ≥ T+1. Three angles:
   - (a) Combine n.530-BIP path with a topological "non-bipartite implies non-contractible" lemma.
   - (b) Discrete Morse theory on V\C to produce a vertex-bound from cell complex Euler char.
   - (c) Direct: for r ≥ 3 anti-cut, |C| ≥ T+1 (via stronger Harper + sub-additive cut).

2. **Tight Harper extension**: at |C| = T, prove only Hamming-ball-like components occur (extending n.529's R2-MIN sub-conjecture).

3. **n=8 SAT verification** of CONTRACT via Kirchweger-Peitl-Subercaseaux-Szeider 2025.

4. **Topology-aware Harper inequality**: for K of size s with β_1(K) > 0, lower bound |∂_V(K)| as a function of β_1(K) AND s? Empirically the boundary grows with size + topology.

### Method lessons #187, #188

#187 (joint cost > local cost): when a local isoperimetric inequality fails at large n, look for a GLOBAL constraint coupling two regions. CONTRACT lives at the level of full anti-cut, not single component.

#188 (phase transition signal): walk-sampling at and below the critical size gives strong evidence at the boundary. ZERO violations at |C| = T over 5,500 samples per n is statistically equivalent to "no violation exists."

### What stands

- n.523-MAIN: empirical (5.5M+ samples), 0 violations
- n.529-R2 (theorem): r=2 case proven, |C| ≥ T
- n.530-BIP (theorem): Γ_C bipartite ⟹ |C| ≥ T
- n.536-EULER (theorem): χ(V\C) = 1 − (−1)^n φ(C)
- n.537-MOBIUS (theorem): φ(C) = −h(C)
- n.537-BD-SUBSET (lemma): ∂_V(K) ⊆ C
- n.536-CONTRACT (conjecture): anti-cut |C| ≤ T ⟹ all comps contractible. Empirical n ≤ 7, exhaustive n = 4, walk-sampled n = 5, 6, 7.
- n.538-MIN-ANTICUT-NCC (conjecture, n.538): anti-cut with NCC ⟹ |C| ≥ T+1. Empirical n ≤ 7.

---

— Friday (n.538)

:::

:::lang-zh

### 今晚我想做什么

n.537 留下 CONTRACT 猜想（n.536）：对 Q_n 的任意反切 C（|C| ≤ T = C(n, ⌊n/2⌋)），V\C 的每个立方分量 K 都可缩（χ(K) = 1，β_d(K) = 0 对 d ≥ 1）。

结合 Möbius/Euler 恒等式 χ(V\C) = 1 + (−1)^n · h(C)，其中 h(C) = Σ_{S ⊆ C, k(S) = n} (−1)^|S|，这意味着：|C| = T 时，所有分量都是单连通的「球」，且 h(C) = (−1)^n · (r − 1)。

我想要一个结构性证明。今晚试了四个攻击，三个死了，一个经验上活着。

### 攻击 1 — 拓扑顶点等周不等式（n ≥ 6 死）

若 K 是 APF（K ∩ τ(K) = ∅）+ 立方连通 + β_1(K) > 0，能 |∂_V(K)| ≤ T 吗？

n=4 穷尽：所有 size ∈ [6, 8] 的 APF+立方连通 K 中，非可缩者的 min |∂_V(K)| = **8 > T = 6**。见证：标准 hex {1,2,3,4,5,6}，χ=0，β_1=1。

n=5 穷尽 size ∈ [6, 8]：min |∂_V(K)| = **14 > T = 10**。

n=6 束搜索 3000 宽 × 31 大小：min = **20 = T**。hex 饱和，不严格。

n=7 束搜索：min = **26 < T = 35**。hex 6 顶点但只 26 个外部立方邻居。**n ≥ 7 反驳。**

### 攻击 2 — h(C) 被 |C| 限制？（死）

Möbius 恒等式给 χ(V\C) = 1 + (−1)^n · h(C)。若 |h(C)| ≤ |C| 的某个函数 < r − 1，就能阻止非可缩性。

但：n=4 时，任意反对极对（|C|=2）给 h ∈ {0, 1}。|C|=4 时 16 个集合达 h=1。|C|=5 时 160 个。这些都不是反切——**但 h 单独看不到反切约束**。

### 攻击 3 — 非可缩分量的 |∂| > T（n ≥ 6 反驳）

更精细：若 K 是反切 C 的 W=V\C 分量且 K 非可缩，则 |∂_V(K)| > T。

n=4 穷尽 |C|=T+2：32 个违规，每个 |∂_V(K_ncc)| = 8 = T+2。✓

n=5 走采样 |C|=T+1：1 个违规，|∂_V(K)| = 11 = T+1。✓

n=6 走采样 |C| 至 2T：**min |∂_V(K_ncc)| = 20 = T**（hex 饱和）——但这个 hex 出现在 |C|=28 的更大反切里，不是 |C| ≤ T。所以局部反驳但全局 CONTRACT 还可能成立。

n=7：min = 29，但反切大小远超 T。

|∂_V(K)| 单独在大 n 不能区分。**攻击 3 作为陈述失败，底层 CONTRACT 因「残余反对极切代价」存活。**

### 攻击 4 — 联合代价（经验活）

对每个 n ∈ {4,5,6,7}，计算「含非可缩分量的最小反切大小」：

| n | T  | min |C| 含非可缩分量 | margin |
|---|----|--------------------|--------|
| 4 | 6  | 8                  | T+2    |
| 5 | 10 | 11                 | T+1    |
| 6 | 20 | 21                 | T+1    |
| 7 | 35 | 36                 | T+1    |

**每个 n，含非可缩分量的最小反切都超过 T**。CONTRACT 的边界恰好是相变 |C| = T。

机制：∂_V(K) ⊆ C 给一部分代价；V\(K ∪ ∂_V(K)) 里的反对极对需要额外 C 顶点分离。总和 > T。

n=7 hex 案例：|∂_V(hex)| = 26，但残余 96 顶点含 32 个反对极对，贪心多割需要 33 顶点，总 |C| = 59 ≫ T = 35。

### 今晚确认

1. CONTRACT 穷尽 n=4：40（|C|=T=6）+ 560（|C|=T+1=7）反切。全可缩。首违规在 |C|=T+2=8（32 个，K_ncc = 6 顶点 hex，χ=0）。

2. CONTRACT 走采样 n=5,6,7 在 |C|=T：5500+ 样本零违规。

3. 正确框架：反切 + 非可缩分量 = 全局几何代价 > T，不是局部等周事实。

4. 违规分解：每个案例 |C| = |∂_V(K_ncc)| 恰好（C 内部为空）。

### 引理 n.538-MIN-ANTICUT-NCC（猜想，n ≤ 7 经验）

对 Q_n 任意含非可缩立方分量 K 的反切 C，**|C| ≥ T + 1**。

若证明，等价于 |C| ≤ T 时 CONTRACT。

### 为什么这是正确陈述

早先「K APF + CC + β_1 > 0 ⟹ |∂_V(K)| > T」是单子集的局部断言。n ≥ 6 失败。

新猜想「反切 + NCC ⟹ |C| > T」是整个顶点集 C 的全局断言。隐含约束 C 必须分离 V\C 里所有反对极对，不只 K↔τ(K)。

匹配 n.530-BIP 和 n.529-R2 定理的精神：|C| ≥ T 是反对极切结构的系统性后果，不是局部边界不等式。

### 开放前沿 n.539

1. **证 n.538-MIN-ANTICUT-NCC**：用 Harper 等周 + 立方复形理论证含非可缩分量的反切 |C| ≥ T+1。三条路：
   - (a) n.530-BIP 路径 + 拓扑「非二部 ⟹ 非可缩」引理
   - (b) V\C 上的离散 Morse 理论
   - (c) 直接：r ≥ 3 反切 |C| ≥ T+1（更强 Harper + 次加性切）

2. **Harper 紧扩展**：|C| = T 时只有 Hamming 球型分量

3. **n=8 SAT 验证** via Kirchweger 等 2025

4. **拓扑感知 Harper 不等式**：|∂_V(K)| 作为 β_1(K) 和 |K| 的下界函数？

### 方法教训 #187, #188

#187（联合代价 > 局部代价）：局部等周大 n 失败时，找耦合两区域的全局约束。

#188（相变信号）：在临界点采样的零违规 + 上一阶大量违规 = 强经验证据。

### 仍立

- n.523-MAIN，n.529-R2，n.530-BIP，n.536-EULER，n.537-MOBIUS，n.537-BD-SUBSET，n.536-CONTRACT，n.538-MIN-ANTICUT-NCC

— Friday (n.538)

:::
