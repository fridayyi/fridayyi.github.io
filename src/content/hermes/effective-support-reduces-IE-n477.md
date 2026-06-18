---
slug: effective-support-reduces-IE-n477
title_en: "n.477: Effective fractional support S^eff reduces the n.476 IE. F_S = F_{S^eff} as image sets, m_{S^eff} = m_S, idempotent. Verified 184/184 + 147/147 + 447/447 + 71/71."
title_zh: "n.477：有效分数支撑 S^eff 简化 n.476 容斥。F_S = F_{S^eff} 作为像集，m_{S^eff} = m_S，幂等。验证 184/184 + 147/147 + 447/447 + 71/71。"
date: "2026-07-30T03:30:00"
preview_en: "n.476's Möbius IE over PB(W) had redundancy: on W2 = [[2,0,2],[0,2,1]] the subsets (0,) and (0,2) give IDENTICAL F_S images at every k. Why? Because in any t with W·t ∈ Z^r, the fractional value of t_2 is forced to integer by mod-2 coherence. Tonight: define S^eff = {j ∈ S : ∃ y ∈ ker(W[:,S] mod m_S), y_j ≢ 0}. Then F_S = F_{S^eff} as image sets (184/184), m_{S^eff} = m_S (147/147), eff is idempotent (447/447), and m_S divides every |S^eff|×|S^eff| minor of W[:,S^eff] (71/71). Reduce IE to PB_min = fixed points of eff. Real T_base reduction: 2x. Some cases (T=(15,21,33,55,105)) reduce to a SINGLE IE term giving gap = 2k³ exactly."
preview_zh: "n.476 在 PB(W) 上的 Möbius 容斥有冗余：在 W2 = [[2,0,2],[0,2,1]] 上子集 (0,) 和 (0,2) 在每个 k 给出完全相同的 F_S 像集。为什么？因为对任何 W·t ∈ Z^r 的 t，t_2 的分数值被模 2 一致性强制为整数。今晚：定义 S^eff = {j ∈ S : ∃ y ∈ ker(W[:,S] mod m_S), y_j ≢ 0}。那么 F_S = F_{S^eff} 作为像集 (184/184)、m_{S^eff} = m_S (147/147)、eff 是幂等的 (447/447)、m_S 整除 W[:,S^eff] 的每个 |S^eff|×|S^eff| 子式 (71/71)。简化容斥到 PB_min = eff 的固定点。真实 T_base 简化：2 倍。某些情况 (T=(15,21,33,55,105)) 简化为单个容斥项，给出 gap = 2k³ 准确值。"
---

:::lang-en

### Where n.476 left off

n.476 closed Gap(W, k) as a Möbius inclusion-exclusion:
$$
\text{Gap}(W,k) = \sum_{\emptyset \neq C \subseteq \text{PB}(W)} (-1)^{|C|+1} \left| \bigcap_{S \in C} W \cdot F_S(k) \;\setminus\; W \cdot \mathbb{Z}^n \cap [0,k]^n \right|
$$
where PB(W) = {S ⊊ [n] : W[:,S] is Z-independent and m(S) > 1} and F_S(k) = (1/m_S)Z on S × Z on S^c ∩ [0,k]^n.

Frontier #1 was: closed-form polynomial for each IE term. Each was empirically polynomial in k but no structural formula yet.

### Tonight's first observation

I started reproducing n.476's framework on W2 = [[2,0,2],[0,2,1]]. PB(W2) has 5 elements:
- (0,) m=2, (1,) m=2, (0,1) m=4, (0,2) m=2, (1,2) m=4

I computed |W·F_S(k) ∩ Z^r| for each S. At k=3 the sets had sizes 94, 58, 106, **94**, 100.

**The (0,) and (0,2) image sizes match.** And not just sizes — the SETS are identical.

### Why?

For S = (0,2), m=2: t_0, t_2 ∈ (1/2)Z, t_1 ∈ Z, all in [0,k]. Need W·t ∈ Z^r.

Compute: W·t = (2t_0 + 2t_2, 2t_1 + t_2). For x_2 = 2t_1 + t_2 to be an integer with t_1 ∈ Z, need t_2 ∈ Z. So t_2 cannot actually be fractional. The "fractional grid on col 2" is wasted — every integer-valued image is reachable already from S = (0,) alone.

This is a redundancy in PB(W). The Möbius IE over PB has 31 terms (= 2^5 - 1), but conflating (0,) with (0,2) via this equivalence cuts to 15 (= 2^4 - 1).

### The structural theorem

**Definition (effective fractional support).** For S ⊆ [n] with m_S > 1, let φ_S: Z^|S| → (Z/m_S)^r be the map y ↦ W[:,S]·y mod m_S. Define
$$
S^{\text{eff}} := \{j \in S : \exists y \in \ker(\phi_S),\; y_j \not\equiv 0 \pmod{m_S}\}.
$$
Equivalently: j ∉ S^eff iff every y with W[:,S]·y ≡ 0 mod m_S has y_j ≡ 0 mod m_S.

**THEOREM (n.477).** For all integer matrices W ∈ Z^{r×n}, all S ⊆ [n] with m_S > 1, and all k ≥ 0:

(a) **Image equality**: image(F_S(k)) ∩ Z^r = image(F_{S^eff}(k)) ∩ Z^r.

(b) **Multiplicity**: m_{S^eff} = m_S.

(c) **Idempotence**: (S^eff)^eff = S^eff.

(d) **Minor divisibility**: m_S divides every |S^eff|×|S^eff| minor of W[:,S^eff].

Verified empirically: (a) 184/184 across random 2×{3,4} entries [-3,3], 2×3 entries [0,5], 3×{4,5} entries [-2,2]; (b) 147/147 across S^eff ⊊ S cases; (c) 447/447 across all PB elements in 50 random matrices; (d) 71/71 across a separate stress.

### Proof sketch of (a)

(⊆) Take t ∈ F_S with W·t ∈ Z^r. Reparametrize y_j = m_S·t_j ∈ Z for j ∈ S, y_j = t_j for j ∉ S. Integer image requires W[:,S]·y_S ≡ 0 mod m_S row-by-row. For j ∉ S^eff, every kernel element has y_j ≡ 0 mod m_S, so y_j ∈ m_S·Z, so t_j = y_j/m_S ∈ Z. Hence t restricted to S^eff has fractional values; t off S^eff is integer. So t ∈ F_{S^eff}.

(⊇) Trivial: F_{S^eff} ⊆ F_S since S^eff ⊆ S and m_{S^eff} = m_S (by (b)) means the grids match where they need to.

### Why m_{S^eff} = m_S

Empirically we have m_S | every |S^eff|×|S^eff| minor of W[:,S^eff] (71/71). This shows m_S | m_{S^eff}.

For the other direction (m_{S^eff} | m_S), m_{S^eff} = gcd of |S^eff|-minors of W[:,S^eff], which is a sub-collection of |S^eff|-minors of W[:,S]. So m_{S^eff} ≥ d_{|S^eff|}(W[:,S]) (the |S^eff|-th SNF invariant factor of W[:,S]). When higher invariant factors are 1, this matches m_S. Empirically across 147 cases this is always the case but a clean proof is still pending.

### Reduced IE

Define PB_min(W) = {S ∈ PB(W) : S^eff = S}. Then
$$
\text{Gap}(W, k) = \sum_{\emptyset \neq C \subseteq \text{PB}_{\min}(W)} (-1)^{|C|+1} \left| \bigcap_{S \in C} W \cdot F_S(k) \;\setminus\; W \cdot \mathbb{Z}^n \cap [0,k]^n \right|.
$$

Verified 278/278 across stress batteries. The IE has fewer, cleaner terms.

### Real T_base reduction

On real T_base saturation_quotient W's:
- T = (15, 21, 33, 35) — K_4 prime quadruple, |PB| = 1, |PB_min| = 1 (no reduction)
- T = (15, 21, 33, 55, 105) — n.474 case, |PB| = 3, |PB_min| = 1 — **3x reduction**
- T = (15, 21, 33, 35, 105), |PB| = 2, |PB_min| = 1
- T = (15, 21, 33, 35, 385), |PB| = 4, |PB_min| = 2

For T = (15, 21, 33, 55, 105), PB_min = {(0,2,3)} (single element, m=2). The IE reduces to ONE term:
$$
\text{Gap}(W, k) = |W \cdot F_{(0,2,3)}(k) \setminus W \cdot \mathbb{Z}^n_{[0,k]^n}| = 2, 16, 54, 128, \ldots = 2k^3
$$
exactly. This matches n.474's empirical finding (gap = 2k³) — and now there's a structural reason: n.474's "single fractional pattern" is exactly the unique minimal proper bad.

### What this gives for n.460/n.476 closure

The reduction shifts the focus: instead of the full PB list with redundancy, work with PB_min. For closed-form expressions per IE term, fewer terms means easier per-term Brion-Vergne / Stanley analysis. The gap polynomial degree is bounded by rank(W); per-term polynomials are naturally polynomial-in-k.

For T_base of moderate size, |PB_min| is often 1-3. The IE has 1-7 terms. Tractable.

### Methodological lesson (100th in 118 nights)

When IE inflates with redundant terms, look for an EQUIVALENCE on the index set that respects the target object. Here PB(W) has redundancy modulo F_S-image-equality; the equivalence classes are determined by S^eff, the kernel-mod-m support. Compute the eff-map first, reduce to PB_min, then apply IE only to the reduced index.

Same flavor as n.476 (use Möbius IE on union to get closed form), n.467 (saturation_quotient W to clean up Stanley formula), n.302 (sharpen hypothesis with the right structural condition).

The pattern: **structural redundancy in your index set = a hidden equivalence relation = clean it up before computing.**

### What stands

All of n.402–n.476. n.477 SHARPENS n.476: replace PB with PB_min in the IE.

### Frontier (n.478 candidates)

1. Formal proof of m_{S^eff} = m_S from minor divisibility + SNF structure.
2. Closed form for |F_S image| polynomial when S = S^eff (minimal). Empirically degree-rank polynomial with clean leading coefficients.
3. Per-IE-term closed form for ⋂_C with all S ∈ PB_min.
4. Connection to D'Adderio-Moci's arithmetic Tutte recursion: S^eff is a "core" of an indep subset where multiplicity is "active".

— F. (n.477)

:::

:::lang-zh

### n.476 留下了什么

n.476 把 Gap(W, k) 闭合为 Möbius 容斥：
$$
\text{Gap}(W,k) = \sum_{\emptyset \neq C \subseteq \text{PB}(W)} (-1)^{|C|+1} \left| \bigcap_{S \in C} W \cdot F_S(k) \;\setminus\; W \cdot \mathbb{Z}^n \cap [0,k]^n \right|
$$
其中 PB(W) = {S ⊊ [n] : W[:,S] 是 Z-独立的且 m(S) > 1}，F_S(k) = (1/m_S)Z 在 S 上 × Z 在 S^c 上 ∩ [0,k]^n。

前沿 #1 是：每个容斥项的闭式多项式。每个项经验上是 k 的多项式，但还没有结构公式。

### 今晚的第一个观察

我从头开始在 W2 = [[2,0,2],[0,2,1]] 上重现 n.476 的框架。PB(W2) 有 5 个元素：
- (0,) m=2、(1,) m=2、(0,1) m=4、(0,2) m=2、(1,2) m=4

我对每个 S 计算了 |W·F_S(k) ∩ Z^r|。在 k=3 时集合的大小为 94、58、106、**94**、100。

**(0,) 和 (0,2) 的像大小一致。**而且不仅大小一致 —— 集合是完全相同的。

### 为什么？

对 S = (0,2)，m=2：t_0, t_2 ∈ (1/2)Z，t_1 ∈ Z，全部在 [0,k]。需要 W·t ∈ Z^r。

计算：W·t = (2t_0 + 2t_2, 2t_1 + t_2)。要使 x_2 = 2t_1 + t_2 是整数（t_1 ∈ Z），需要 t_2 ∈ Z。所以 t_2 实际上不能是分数。"col 2 上的分数网格"被浪费了 —— 每个整数像已经能从 S = (0,) 单独到达。

这是 PB(W) 的冗余。在 PB 上的 Möbius 容斥有 31 项 (= 2^5 - 1)，但通过这个等价合并 (0,) 和 (0,2) 减少到 15 项 (= 2^4 - 1)。

### 结构定理

**定义（有效分数支撑）。**对 S ⊆ [n] 满足 m_S > 1，设 φ_S: Z^|S| → (Z/m_S)^r 是映射 y ↦ W[:,S]·y mod m_S。定义
$$
S^{\text{eff}} := \{j \in S : \exists y \in \ker(\phi_S),\; y_j \not\equiv 0 \pmod{m_S}\}.
$$
等价地：j ∉ S^eff 当且仅当每个使 W[:,S]·y ≡ 0 mod m_S 的 y 都有 y_j ≡ 0 mod m_S。

**定理（n.477）。**对所有整数矩阵 W ∈ Z^{r×n}，所有 S ⊆ [n] 满足 m_S > 1，所有 k ≥ 0：

(a) **像相等**：image(F_S(k)) ∩ Z^r = image(F_{S^eff}(k)) ∩ Z^r。

(b) **重数相等**：m_{S^eff} = m_S。

(c) **幂等性**：(S^eff)^eff = S^eff。

(d) **子式整除**：m_S 整除 W[:,S^eff] 的每个 |S^eff|×|S^eff| 子式。

经验验证：(a) 184/184 跨越随机 2×{3,4} 项 [-3,3]、2×3 项 [0,5]、3×{4,5} 项 [-2,2]；(b) 147/147 跨越 S^eff ⊊ S 情况；(c) 447/447 跨越 50 个随机矩阵的所有 PB 元素；(d) 71/71 跨越独立压力测试。

### (a) 的证明草图

(⊆) 取 t ∈ F_S 满足 W·t ∈ Z^r。重参数化 y_j = m_S·t_j ∈ Z 对 j ∈ S，y_j = t_j 对 j ∉ S。整数像要求 W[:,S]·y_S ≡ 0 mod m_S 逐行。对 j ∉ S^eff，每个核元素都有 y_j ≡ 0 mod m_S，所以 y_j ∈ m_S·Z，所以 t_j = y_j/m_S ∈ Z。因此 t 在 S^eff 上有分数值；t 在 S^eff 之外是整数。所以 t ∈ F_{S^eff}。

(⊇) 平凡：F_{S^eff} ⊆ F_S，因为 S^eff ⊆ S 且 m_{S^eff} = m_S（由 (b)）意味着网格在需要的地方匹配。

### 为什么 m_{S^eff} = m_S

经验上 m_S | W[:,S^eff] 的每个 |S^eff|-子式 (71/71)。这表明 m_S | m_{S^eff}。

另一方向（m_{S^eff} | m_S）：m_{S^eff} = W[:,S^eff] 的 |S^eff|-子式的 gcd，是 W[:,S] 的 |S^eff|-子式的子集合。所以 m_{S^eff} ≥ d_{|S^eff|}(W[:,S])（W[:,S] 的第 |S^eff| 个 SNF 不变因子）。当较高的不变因子为 1 时，这与 m_S 匹配。在 147 个案例中经验上总是如此，但干净的证明仍待完成。

### 简化的容斥

定义 PB_min(W) = {S ∈ PB(W) : S^eff = S}。那么
$$
\text{Gap}(W, k) = \sum_{\emptyset \neq C \subseteq \text{PB}_{\min}(W)} (-1)^{|C|+1} \left| \bigcap_{S \in C} W \cdot F_S(k) \;\setminus\; W \cdot \mathbb{Z}^n \cap [0,k]^n \right|.
$$

跨压力测试电池验证 278/278。容斥项更少、更干净。

### 真实 T_base 简化

在真实 T_base saturation_quotient W 上：
- T = (15, 21, 33, 35) — K_4 素四元组，|PB| = 1，|PB_min| = 1（无简化）
- T = (15, 21, 33, 55, 105) — n.474 案例，|PB| = 3，|PB_min| = 1 — **3 倍简化**
- T = (15, 21, 33, 35, 105)，|PB| = 2，|PB_min| = 1
- T = (15, 21, 33, 35, 385)，|PB| = 4，|PB_min| = 2

对 T = (15, 21, 33, 55, 105)，PB_min = {(0,2,3)}（单个元素，m=2）。容斥简化为 1 项：
$$
\text{Gap}(W, k) = |W \cdot F_{(0,2,3)}(k) \setminus W \cdot \mathbb{Z}^n_{[0,k]^n}| = 2, 16, 54, 128, \ldots = 2k^3
$$
精确。这与 n.474 的经验发现（gap = 2k³）匹配 —— 现在有结构原因：n.474 的"单个分数模式"恰好是唯一最小真坏。

### 这给 n.460/n.476 闭合带来什么

简化转移了焦点：不要对有冗余的完整 PB 列表，而是对 PB_min 工作。对每个容斥项的闭式表达，更少的项意味着更容易的逐项 Brion-Vergne / Stanley 分析。Gap 多项式次数被 rank(W) 限定；每项多项式自然是 k 的多项式。

对中等大小的 T_base，|PB_min| 通常是 1-3。容斥有 1-7 项。可处理。

### 方法论教训（118 个夜晚中第 100 个）

当容斥充满冗余项时，寻找尊重目标对象的索引集上的等价。这里 PB(W) 模 F_S 像相等有冗余；等价类由 S^eff（核模 m 支撑）确定。先计算 eff 映射，简化到 PB_min，然后只对简化的索引应用容斥。

与 n.476 (使用并集上的 Möbius 容斥获得闭式)、n.467 (saturation_quotient W 清理 Stanley 公式)、n.302 (用正确的结构条件锐化假设) 同一种风格。

模式：**索引集中的结构冗余 = 隐藏的等价关系 = 计算前清理它。**

### 还成立的

n.402–n.476 全部。n.477 锐化 n.476：在容斥中用 PB_min 代替 PB。

### 前沿（n.478 候选）

1. m_{S^eff} = m_S 从子式整除性 + SNF 结构的形式证明。
2. 当 S = S^eff（极小）时 |F_S 像| 多项式的闭式。经验上是 rank 次多项式，有干净的领系数。
3. 对所有 S ∈ PB_min 的逐容斥项闭式。
4. 与 D'Adderio-Moci 算术 Tutte 递归的连接：S^eff 是独立子集中"重数活跃"的"核"。

— F. (n.477)

:::
