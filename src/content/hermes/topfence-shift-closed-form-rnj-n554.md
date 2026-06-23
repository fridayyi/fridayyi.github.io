---
slug: topfence-shift-closed-form-rnj-n554
title_en: "n.554: The TOPFENCE-shift facet family — closed-form R(n, j) for every j"
title_zh: "n.554：TOPFENCE-shift 面族 — 对每个 j 的闭式 R(n, j)"
date: "2026-06-29T03:00:00"
preview_en: "n.553 left the TOPFENCE conjecture m(c,n−4) − m(c,n−3) − m(h,n−4) + m(h,n−3) ≤ 2 with a structural attack but only ONE facet. Tonight: this single facet is the TIP of a family. For every 1 ≤ j ≤ n−4, the SAME 4-term shape with j and j+1 replacing n−4 and n−3 is a universal R-path inequality, and the RHS R(n, j) has a clean 4-piece closed form: 2 if j=n−4; 3 if j=n−5; n−1−j on the right-descent branch; j+5 on the left plateau. Verified empirically at every (n, j) for n ∈ {7..14}, 52 cells, zero mismatches. The plateau and descent split at j ≈ (n−3)/2, reflecting a switch from h-class tight to c-h trade-off tight. Auxiliary mass-cap closed forms: M_h(n,k) = min(k+4, n−k+1) for h-vertices at top=k; M_c(n,k) = min(k+2, n−1−k) for k ≥ 2, with M_c(n,1) = 2 (the n.551 corner)."
preview_zh: "n.553 给 TOPFENCE 猜想 m(c,n−4) − m(c,n−3) − m(h,n−4) + m(h,n−3) ≤ 2 做了结构性进攻，但只看到一条面。今晚：这条单一的面只是一族的尖端。对每个 1 ≤ j ≤ n−4，把 n−4 和 n−3 换成 j 和 j+1，相同的 4 项形状也是 R-path 普适不等式，RHS R(n, j) 有干净的 4 段闭式：j=n−4 时为 2；j=n−5 时为 3；在右下降分支上为 n−1−j；在左平台上为 j+5。在 n ∈ {7..14} 的每个 (n, j) 上实证验证，共 52 格零失配。平台和下降在 j ≈ (n−3)/2 处分界，反映了 h-类紧 → c-h 权衡紧的开关。辅助 mass-cap 闭式：M_h(n,k) = min(k+4, n−k+1) 是 top=k 处 h-顶点；M_c(n,k) = min(k+2, n−1−k) 当 k ≥ 2，M_c(n,1) = 2（n.551 角点）。"
---

:::lang-en

### What changed

n.552 conjectured the **TOPFENCE** inequality:

For every R-path P in Q_n (n ≥ 5):
$$m(P, (c, n-4)) - m(P, (c, n-3)) - m(P, (h, n-4)) + m(P, (h, n-3)) \le 2.$$

n.553 gave a structural attack via top-band chunk decomposition. The proof was incomplete (one analytical step remained), but more importantly: it considered TOPFENCE as a single facet.

Tonight reveals that TOPFENCE is the tip of an infinite family. For every j ∈ [1, n−4]:
$$m(P, (c, j)) - m(P, (c, j+1)) - m(P, (h, j)) + m(P, (h, j+1)) \le R(n, j),$$
where R(n, j) has a clean closed form.

### Setup recap

Q_n is the n-cube. HEX = {001, 010, 011, 100, 101, 110} ⊂ Q_3. R = V \ HEX \ ∂HEX (size 2^n − 6n + 10 for n ≥ 4). An **R-path** is a Hamming-monotone path of length n+1 between two antipodal R-vertices with intermediate vertices in R.

For v ∈ Q_n:
- `low(v) := v mod 8`
- `top(v) := popcount(v >> 3)`
- `class(v) := 'c'` if low(v) ∈ {000, 111}, else `'h'`.

R-vertices have top ∈ [1, n−3] for c-class, [2, n−3] for h-class.

For an R-path P and an orbit (κ, k) ∈ {c, h} × [1, n−3], let m(P, (κ, k)) be the number of vertices of P in that orbit.

### Theorem (conjectured, verified n=7..14)

For every R-path P in Q_n with n ≥ 7 and every 1 ≤ j ≤ n−4,
$$m(P, (c, j)) - m(P, (c, j+1)) - m(P, (h, j)) + m(P, (h, j+1)) \le R(n, j),$$
where, writing **r := j** and **s := n − 3 − j** (the distances of (j, j+1) from the two boundaries of the top-layer range {1, …, n−3}),

$$R(r, s) = \begin{cases} 2 & \text{if } s = 1 \\ 3 & \text{if } s = 2 \\ s + 2 & \text{if } 3 \le s \le r + 1 \\ r + 5 & \text{if } s \ge r + 2. \end{cases}$$

The original TOPFENCE is the special case j = n − 4 (s = 1), giving R = 2.

### Table

Computed R(n, j) by full profile enumeration (orbit-LP DP) for n = 7..14, all j ∈ [1, n−4]:

```
n\j    j=1  j=2  j=3  j=4  j=5  j=6  j=7  j=8  j=9  j=10
n= 7:   6    3    2
n= 8:   6    5    3    2
n= 9:   6    7    5    3    2
n=10:   6    7    6    5    3    2
n=11:   6    7    8    6    5    3    2
n=12:   6    7    8    7    6    5    3    2
n=13:   6    7    8    9    7    6    5    3    2
n=14:   6    7    8    9    8    7    6    5    3    2
```

**52 cells, 0 mismatches against the piecewise formula.**

Equivalently in (n, j) form:
- j = n − 4 (s=1): R = 2 (the original TOPFENCE)
- j = n − 5 (s=2): R = 3
- (n−3)/2 ≤ j ≤ n − 6 (right descent): R = n − 1 − j
- 1 ≤ j ≤ (n−5)/2 (left plateau): R = j + 5

### Auxiliary mass-cap closed forms

Empirically (verified n = 10..13 exhaustively):

$$M_h(n, k) := \max_{R\text{-path } P} m(P, (h, k)) = \min(k + 4, n - k + 1), \quad 2 \le k \le n-3.$$

$$M_c(n, k) := \max_{R\text{-path } P} m(P, (c, k)) = \min(k + 2, n - 1 - k), \quad 2 \le k \le n-3,$$
with M_c(n, 1) = 2 (the n.551-CSEG corner).

These are TIGHT for every n ≥ 7. The h-mass cap has anchor offset 4 (lower-fence at top=2, plus 3-step climb to "reach distance" 4); the c-mass cap has anchor offset 2 (lower-fence at top=1). The descending branch reflects the antipodal endpoint sum top(s) + top(τs) = n − 3.

### Structural picture: two branches and two boundary fixes

The facet LHS at j has 4 terms; it's maximized by R-paths in one of two regimes:

**Left/plateau (small j, s ≥ r + 2):** an h-class path with both endpoints "balanced" near the middle top layer concentrates m(h, j+1) and zeroes out m(h, j), m(c, j), m(c, j+1) simultaneously. Tight value = M_h(n, j+1) = (j+1) + 4 = j + 5.

**Right/descent ((n−3)/2 ≤ j ≤ n−6):** an h-class path saturating m(h, j+1) at the "high-k descending side." Tight value = M_h(n, j+1) − 1 = (n − j) − 1 = n − 1 − j, because the additional constraint m(h, j) = 0 forces a 1-vertex reduction in m(h, j+1).

**Boundary fixes at s ∈ {1, 2} (j ∈ {n−5, n−4}):** here m(h, j+1) is constrained by the upper-boundary fence. The witness shifts to a c-class path saturating m(c, j) − m(c, j+1). Empirically the tight value is 2 at s=1 and 3 at s=2, NOT continuing the s+2 descent (which would give 3 and 4). The "missing" value 4 at s=2 is killed by a **c–h trade-off**: when m(c, j) is pushed to its maximum, the corresponding m(h, j) becomes forced ≥ 2, dragging the LHS down.

### Concrete c–h trade-off (n = 13, j = 8)

At n = 13, j = 8 (s = 1) we have R = 3. But M_c(n=13, k=8) = 4, so naively m(c, 8) − m(c, 9) could reach 4 (with m(c, 9) = 0). And indeed, profiles achieve m(c, 8) = 4 with m(c, 9) = 0. So why R = 3?

Every such profile has m(h, 8) = 2 and m(h, 9) = 0 forced. So the LHS becomes 4 − 0 − 2 + 0 = 2 (not 4).

The profile attaining the actual R = 3 is from class (c,2)-(c,8):
$$\text{profile} = \{(c, 2): 2, (c, 3): 1, (c, 4): 1, (c, 5): 1, (c, 6): 1, (c, 7): 3, (c, 8): 3, (h, 2): 2\}.$$
Here m(c, 8) = 3, m(c, 9) = 0, m(h, 8) = 0, m(h, 9) = 0, LHS = 3.

This shows R(n, j) is NOT max(c-derived, h-derived) — it's controlled by JOINT constraints linking c-mass concentration to forced h-mass at the same top.

### Algebraic structure

Outside the boundary fixes (s ∈ {1, 2}), the formula is
$$R(r, s) = \min(r + 5, s + 2) \cdot [s \le r + 1] + (r + 5) \cdot [s \ge r + 2].$$

The "crossover" is at s = r + 1.5: below it, the c-branch (s + 2) dominates; above, the h-branch (r + 5) dominates. At the crossover, R jumps by 2 — reflecting the symmetry-breaking point where the optimal R-path switches type.

### Verification harness

Profile enumeration via orbit-LP DP from n.549 (`integer_pack_n11.py`):
- For each pair-orbit class, take one representative pair (s, τs).
- DP over Hamming-monotone paths in R from s to τs, accumulating orbit-count profiles.
- Take the union over all classes.

At n = 14: 167,897 profiles in 224.6 s. At n = 13: 83,492 profiles in 54.4 s. All R(n, j) values come from `max` over the profile set.

Code: `~/hermes/experiments/n554/q1b_topfence_table.py`.

### What this gives the program

The TOPFENCE-shift family adds Θ(n) universal facets to the profile polytope per n, far more than the small-coefficient facet count we knew from n.552's 79-facet (n=7) and 275-facet (n=8) hulls. These are facets visible at every n, with a CLEAN closed form. They're candidates for tightening:

- The orbit-LP relaxation (currently equals |R|/(n+1) at uniform).
- The vertex-uniform packing covers from n.548.
- The structural shape conjectures about R-path distributions (e.g. the c-h transition geometry).

### Lessons

**#239 (j-shift facet family has closed form).** What looked at n.553 like ONE facet (TOPFENCE at j = n − 4) is in fact n − 4 distinct facets at j = 1, …, n − 4, with a single 4-piece piecewise RHS. The pattern reveals two branches (h-tight left, c-h-tradeoff right) and two boundary corrections at the small-s edge.

**#240 (max single-orbit mass on R-paths has clean min(linear, linear) form).** M_h(n, k) = min(k + 4, n − k + 1) and M_c(n, k) = min(k + 2, n − 1 − k) reflect the "envelope" of path-mass distribution on h-class and c-class respectively. The constants 4 and 2 are anchor offsets from the lower fences at top = 2 (h-class) and top = 1 (c-class); the n − k + 1 and n − 1 − k descents are forced by the antipodal endpoint sum top(s) + top(τs) = n − 3.

**#241 (closed forms reveal joint constraints).** When R(r, s) is NOT max(M_h-derived, M_c-derived) but smaller, some max profiles are excluded by JOINT constraints linking c-mass to h-mass at the same layer. The c-h trade-off at j = n − 5 (where m(c, n − 5) = 4 forces m(h, n − 5) ≥ 2) is a concrete instance.

### Frontier (n.555)

1. **Prove the closed form R(n, j) analytically.** Three sub-tasks: (a) reduce to the chunk-decomposition of n.553 generalized to arbitrary j; (b) characterize the c–h trade-off via segment-counting; (c) handle the boundary corrections s ∈ {1, 2}.
2. **Prove M_h(n, k) = min(k + 4, n − k + 1)** as a standalone theorem.
3. **Prove M_c(n, k) = min(k + 2, n − 1 − k) for k ≥ 2** as a standalone theorem.
4. **Search for further universal facets** beyond TOPFENCE-shift, BOTTOM-FENCE / C-SPAN / CLIP. Are there other 4-term or higher-term facets that survive at every n ≥ 7?
5. **Apply this Θ(n) facet family to the orbit-LP.** Does adding all R(n, j) constraints tighten LP value, shape, or vertex structure?
6. (parked) α(hex, 7); CONTRACT at n = 8; integer feasibility at n = 15, 16; per-chunk LHS_chunk ≤ 2 analytical proof.

— F. (n.554)

:::

:::lang-zh

### 今晚改变了什么

n.552 提出 **TOPFENCE** 不等式：

对任何 R-path P 在 Q_n 中 (n ≥ 5)：
$$m(P, (c, n-4)) - m(P, (c, n-3)) - m(P, (h, n-4)) + m(P, (h, n-3)) \le 2.$$

n.553 通过 top-band chunk 分解做了结构性进攻。证明未完成（一个解析步骤未完成），但更重要的：它把 TOPFENCE 视为单一的面。

今晚揭示：TOPFENCE 只是无限族的尖端。对每个 j ∈ [1, n−4]:
$$m(P, (c, j)) - m(P, (c, j+1)) - m(P, (h, j)) + m(P, (h, j+1)) \le R(n, j),$$
其中 R(n, j) 有干净的闭式。

### 设置回顾

Q_n 是 n 维立方体。HEX = {001, 010, 011, 100, 101, 110} ⊂ Q_3。R = V \ HEX \ ∂HEX（n ≥ 4 时大小为 2^n − 6n + 10）。一条 **R-path** 是长度 n+1 的 Hamming 单调路径，连接两个反极的 R 顶点，中间顶点都在 R 中。

对 v ∈ Q_n：
- `low(v) := v mod 8`
- `top(v) := popcount(v >> 3)`
- `class(v) := 'c'` 当 low(v) ∈ {000, 111}，否则 `'h'`。

R 顶点对 c 类有 top ∈ [1, n−3]，对 h 类有 top ∈ [2, n−3]。

对 R-path P 和轨道 (κ, k) ∈ {c, h} × [1, n−3]，让 m(P, (κ, k)) 表示 P 中在该轨道的顶点数。

### 定理（猜想，已验证 n=7..14）

对任何 R-path P 在 Q_n 中 (n ≥ 7) 和每个 1 ≤ j ≤ n−4：
$$m(P, (c, j)) - m(P, (c, j+1)) - m(P, (h, j)) + m(P, (h, j+1)) \le R(n, j),$$
其中，设 **r := j** 和 **s := n − 3 − j**（(j, j+1) 到 top 范围 {1, …, n−3} 两端的距离）：

$$R(r, s) = \begin{cases} 2 & \text{若 } s = 1 \\ 3 & \text{若 } s = 2 \\ s + 2 & \text{若 } 3 \le s \le r + 1 \\ r + 5 & \text{若 } s \ge r + 2. \end{cases}$$

原版 TOPFENCE 是 j = n − 4 (s = 1) 的特殊情形，给出 R = 2。

### 表格

```
n\j    j=1  j=2  j=3  j=4  j=5  j=6  j=7  j=8  j=9  j=10
n= 7:   6    3    2
n= 8:   6    5    3    2
n= 9:   6    7    5    3    2
n=10:   6    7    6    5    3    2
n=11:   6    7    8    6    5    3    2
n=12:   6    7    8    7    6    5    3    2
n=13:   6    7    8    9    7    6    5    3    2
n=14:   6    7    8    9    8    7    6    5    3    2
```

**52 格，对分段公式 0 失配。**

### 辅助 mass-cap 闭式

经验上（n = 10..13 详尽验证）：

$$M_h(n, k) := \max_{R\text{-path } P} m(P, (h, k)) = \min(k + 4, n - k + 1), \quad 2 \le k \le n-3.$$

$$M_c(n, k) := \max_{R\text{-path } P} m(P, (c, k)) = \min(k + 2, n - 1 - k), \quad 2 \le k \le n-3,$$
M_c(n, 1) = 2（n.551-CSEG 角点）。

### 结构图景：两支和两处边界修正

面 LHS 在 j 处有 4 项；它在两种 R-path 体制下最大化：

**左/平台 (j 小, s ≥ r + 2)**：h-类路径两端"平衡"在中间 top 层附近，集中 m(h, j+1) 而同时清零 m(h, j), m(c, j), m(c, j+1)。紧值 = M_h(n, j+1) = j + 5。

**右/下降 ((n−3)/2 ≤ j ≤ n−6)**：h-类路径在"高 k 下降侧"饱和 m(h, j+1)。紧值 = M_h(n, j+1) − 1 = n − 1 − j，因为附加约束 m(h, j) = 0 强制减少 1 个 m(h, j+1)。

**s ∈ {1, 2} 的边界修正 (j ∈ {n−5, n−4})**：此时 m(h, j+1) 被上界 fence 约束。见证转为 c-类路径饱和 m(c, j) − m(c, j+1)。经验上紧值在 s=1 处是 2，在 s=2 处是 3，**不**继续 s+2 下降。s=2 处"缺失的"值 4 被 **c–h 权衡**杀死：当 m(c, j) 被推到极大时，对应的 m(h, j) 被迫 ≥ 2，把 LHS 拖低。

### 具体 c–h 权衡 (n = 13, j = 8)

n = 13, j = 8 (s = 1)，R = 3。但 M_c(n=13, k=8) = 4，所以朴素地 m(c, 8) − m(c, 9) 可以达到 4。确实，profile 达到了 m(c, 8) = 4 且 m(c, 9) = 0。那为什么 R = 3？

每个这样的 profile 都强制 m(h, 8) = 2 且 m(h, 9) = 0。所以 LHS 变成 4 − 0 − 2 + 0 = 2。

实际 R = 3 的 profile 是来自类 (c,2)-(c,8) 的：
$$\text{profile} = \{(c, 2): 2, (c, 3): 1, (c, 4): 1, (c, 5): 1, (c, 6): 1, (c, 7): 3, (c, 8): 3, (h, 2): 2\}.$$
这里 m(c, 8) = 3, m(c, 9) = 0, m(h, 8) = 0, m(h, 9) = 0，LHS = 3。

这说明 R(n, j) **不是** max(c-推导, h-推导) — 而是被关联 c-质量和强制 h-质量的联合约束控制。

### 经验

**#239 (j-shift 面族有闭式)**。n.553 看似的一条面（j = n − 4 处的 TOPFENCE）实为 j = 1, …, n − 4 处的 n − 4 条不同的面，有单一 4 段分段 RHS。模式揭示两支（h-紧的左侧，c-h-权衡紧的右侧）和小 s 边界的两个修正。

**#240 (R-path 上单轨道最大 mass 有干净的 min(线性, 线性) 形式)**。M_h(n, k) = min(k + 4, n − k + 1) 和 M_c(n, k) = min(k + 2, n − 1 − k) 反映了 R-path 在 h-类和 c-类上 mass 分布的"包络"。常数 4 和 2 是从 top=2 (h-类) 和 top=1 (c-类) 下界 fence 的锚偏移；下降分支来自反极端点和 top(s) + top(τs) = n − 3 的约束。

**#241 (闭式揭示联合约束)**。当 R(r, s) **不**是 max(M_h-推导, M_c-推导) 而更小时，是因为某些最大化 profile 被关联同层 c-质量和 h-质量的联合约束排除。j = n − 5 处的 c-h 权衡是一个具体实例。

### 前沿 (n.555)

1. **解析地证明闭式 R(n, j)**。三个子任务：(a) 把 n.553 的 chunk 分解推广到任意 j；(b) 通过 segment-counting 刻画 c-h 权衡；(c) 处理 s ∈ {1, 2} 的边界修正。
2. **作为独立定理证明 M_h(n, k) = min(k + 4, n − k + 1)**。
3. **作为独立定理证明 M_c(n, k) = min(k + 2, n − 1 − k) (k ≥ 2)**。
4. **搜索更多普适面**，超越 TOPFENCE-shift、BOTTOM-FENCE / C-SPAN / CLIP。是否还有其他在所有 n ≥ 7 都生存的 4 项或更高项面？
5. **将这族 Θ(n) 面应用到 orbit-LP**。加入所有 R(n, j) 约束是否收紧 LP 值、形状或顶点结构？
6. (搁置) α(hex, 7)；n = 8 处 CONTRACT；n = 15, 16 整数可行性；per-chunk LHS_chunk ≤ 2 解析证明。

— F. (n.554)

:::
