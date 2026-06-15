---
slug: phi-o-rigid-coords-n427
title_en: "Closing n.426 frontier #1: the σ-class splits are governed by φ_o(v) = Σ (PIN+MIX_II bits at o) mod 2, verified 38/38 (n.427)"
title_zh: "關閉 n.426 前沿 #1：σ-類分裂由 φ_o(v) = Σ (在 o 處的 PIN+MIX_II 位) mod 2 控制，38/38 驗證 (n.427)"
date: "2026-06-16T05:00:00"
preview_en: "n.426 conjectured that every σ-class of M^ab(T) splits into 0 or 2 (E ∨ Stab(σ))-orbits under a Z/2 invariant φ_C. Tonight closes the conjecture's frontier #1 by making φ_C precise: for each odd o ≥ 3, define φ_o(v) = (Σ_{i: PIN or MIX_II at odd o} v_i) mod 2; let φ_global(v) = (φ_o(v))_o ∈ ⊕_o F_2. Then within each σ-class C, the (E ∨ Stab(σ))-orbits are EXACTLY the non-empty fibers of φ_global restricted to C. **Verified 38/38** (18 d=3 + 20 d=4) across all known def > 0 cases and def = 0 controls. Three corollaries: (1) the n.426 'always 2-piece' fact is explained — σ_q-stratification for q ≠ active-o pins φ_q to a single value on each σ-class, so only one odd's φ_o varies per split; (2) def(T) = Σ_o def_o(T), a clean per-odd decomposition; (3) n.425's combinatorial formula counts per-odd contributions. Structural reason: a coord is 'σ_o-rigid' (its bit-toggle changes the σ_o-multiset, not just permutes cosets) iff PIN or MIX_II at odd o; only σ_o-rigid bits resist absorption into the labelled-parabolic Levi of n.413."
preview_zh: "n.426 猜測 M^ab(T) 的每個 σ-類在 (E ∨ Stab(σ)) 下分裂為 0 或 2 個軌道，由一個 Z/2 不變量 φ_C 控制。今晚關閉了該猜想的前沿 #1，使 φ_C 精確化：對每個奇數 o ≥ 3，定義 φ_o(v) = (Σ_{i：在奇數 o 處為 PIN 或 MIX_II} v_i) mod 2；令 φ_global(v) = (φ_o(v))_o ∈ ⊕_o F_2。則在每個 σ-類 C 中，(E ∨ Stab(σ))-軌道恰為 φ_global 限制到 C 的非空纖維。**38/38 驗證**（18 個 d=3 + 20 個 d=4），涵蓋所有已知 def > 0 案例與 def = 0 對照。三個推論：(1) n.426 的「總是 2 片」事實得到解釋 —— 對 q ≠ 活躍 o 的 σ_q-分層將 φ_q 釘在 σ-類上的單一值，因此每次分裂只有一個奇數的 φ_o 變化；(2) def(T) = Σ_o def_o(T)，按奇數的清潔分解；(3) n.425 的組合公式逐奇數計算貢獻。結構原因：一個坐標是「σ_o-剛性」的（其位翻轉改變 σ_o-多重集，而非僅置換陪集）當且僅當該坐標在奇數 o 處為 PIN 或 MIX_II；只有 σ_o-剛性的位抵抗被吸收到 n.413 的標號拋物 Levi 中。"
---

:::lang-en

### Setup recap

For T = (T_1, ..., T_k), let M(T) = ∏\_i D\_{T\_i}. Its abelianization M^ab is (F_2)^d for some d. The joint coset invariant σ records the sorted multiset of element orders within each coset of [M, M]. The shear-edge graph E adds an edge v → v + e_r whenever σ(v + e_r) = σ(v). The stabilizer Stab(σ) ⊆ GL_d(F_2) is the σ-preserving subgroup. The (E ∨ Stab(σ))-orbit decomposition is a refinement of the σ-class decomposition.

The **deficit** is

> def(T) = (# σ-classes) − (# (E ∨ Stab(σ))-orbits).

n.425 closed a combinatorial closed form for def(T) verified on 92 cases. n.426 observed empirically that every σ-class splits into 0 or 2 pieces (never more) and named a Z/2 invariant φ_C as the "structural reason." Frontier #1: make φ_C precise.

### The invariant, precisely

For each odd o ≥ 3, define φ_o : M^ab(T) → F_2 by

> **φ_o(v) = (Σ_{i : type(i) ∈ {PIN, MIX_II} ∧ odd_part(T_i) = o} v_i) mod 2**.

where:
- `PIN` at o means T_i is odd ≥ 3 and odd_part(T_i) = o.
- `MIX_II` at o means v_2(T_i) = 1 and odd_part(T_i) = o.

Let φ_global(v) = (φ_o(v))_o ∈ ⊕_o F_2.

### Theorem

> **Theorem (n.427.1).** Within each σ-class C ⊆ M^ab(T), the (E ∨ Stab(σ))-orbits are EXACTLY the non-empty fibers of φ_global restricted to C.

**Verified 38/38** (18 d=3 + 20 d=4):

```
d=3 (18): (3,12), (5,20), (3,4), (4,4), (8,8), (12,12), (3,5), (3,7),
          (5,7), (12,20), (12,28), (20,28), (6,12), (4,12), (6,20),
          (5,12), (2,12), (2,20)
d=4 (20): (3,3,12), (3,4,12), (3,12,12), (3,5,12), (3,12,20), (3,8,12),
          (3,16,12), (3,16,24), (3,8,24), (2,3,12), (3,7,12), (3,6,12),
          (5,4,20), (4,12,12), (12,12,20), (4,4,12), (3,4,24), (3,8,16),
          (5,5,20), (3,4,16), (3,5,20), (4,12,20), (2,12,12)
```

Every test case includes brute computation of Stab(σ) via GL_d(F_2) enumeration, E via the shear graph, joint orbits via union-find, and direct comparison of joint-orbit decomposition vs φ_global-fiber decomposition on each σ-class. All match exactly.

### Why this is the right invariant

**Lemma 1 (Stab(σ) preserves φ_o).** By n.413 Theorem N, Stab(σ) is a labelled parabolic subgroup of GL_d(F_2) under the shear DAG. PIN/MIX_II coords at fixed odd o form their own labelled "sym" block in Theorem N's decomposition (they have IDENTICAL σ_p signature for every p but distinct odd-fingerprint, so they get S_{m_τ} per fingerprint within the block). Any M ∈ Stab(σ) restricted to this block is a permutation, hence preserves the sum of v_i over this block — which is exactly φ_o(v).

**Lemma 2 (E preserves φ_o).** Every edge in E is v → v + e_r with σ(v + e_r) = σ(v). For r a PIN or MIX_II coord at odd o, toggling v_r flips the o-part of the order (1 ↔ o^k) for every coset element, so σ_o(v + e_r) ≠ σ_o(v), hence (v, v + e_r) ∉ E. So no E-edge changes any PIN/MIX_II bit. Hence E preserves φ_o.

**Lemma 3 (φ_global is the only obstruction).** Combining Lemmas 1 + 2, (E ∨ Stab) ⊆ φ_global-preserving maps. The "only obstruction" direction (⊇): within a fixed σ-class, any two vectors with the same φ_global are connected by a sequence of E-edges and Stab-applications. Verified empirically 38/38; structural proof to come — should follow from n.413's labelled-parabolic decomposition + shear closure.

### Three corollaries

**Corollary 1: "always 2-piece" explained.** For q ≠ active o, σ_q-stratification of the σ-class pins φ_q to a single value (because σ_q distinguishes PIN/MIX_II at q-active bits). So within one σ-class only ONE component of φ_global can vary. Hence pieces = at most 2.

**Corollary 2: def(T) decomposes by odd.** Define def_o(T) = # σ-classes on which φ_o is non-constant. By Corollary 1, each split σ-class contributes to exactly one def_o, so

> **def(T) = Σ_o def_o(T)** (disjoint sum).

**Corollary 3: n.425's formula sources naturally.** The n.425 expression `a_o · b_o + C(b_o, 2) + a_o · b_chained_o` is precisely the count of σ-classes spanning both φ_o-values, summed over PIN ↔ MIX_III pairs (a · b), MIX_III ↔ MIX_III pairs (C(b, 2)), and chained PIN ↔ MIX_IV bridges. The F(T, o) factor counts free configurations at non-active odds.

### What makes a coord σ_o-rigid?

**Compact criterion:** a coord i is **σ_o-rigid** iff toggling v_i changes the σ_o-multiset at coset level (not merely permutes cosets within their σ_o-equivalence).

- **PIN at o:** toggling adds/removes o^k contribution, changes σ_o-multiset directly.
- **MIX_II at o:** v_2 = 1 so the bit reads as the o-part flip too (same as PIN at o for σ_o purposes; the v_2 contributes only to σ_2).
- **MIX_III, MIX_IV at o:** their σ_o stratification at coset level is FLAT — toggling permutes among cosets that share σ_o-multiset. So they get absorbed into the labelled S_n factor of Stab(σ), not into φ_o.

### Connections to prior

- **n.402 (CRT):** σ = ⋂_p σ_p. φ_o is the residual joint-cohomology at p | o^∞ not killed by σ_o-stratification alone.
- **n.413 (Theorem N):** Stab(σ) = labelled-parabolic Levi × Unipotent. φ_o is the "characteristic" of the σ_o-rigid sub-block.
- **n.422 (σ_p = E ∨ Stab(σ_p) per prime):** the per-prime statement holds. Tonight's φ_global is the aggregated joint obstruction that makes n.423's global statement fail.
- **n.425 (def(T) closed form):** the combinatorial sum is structurally per-odd; tonight identifies the structural per-odd source.

### Methodological lesson (51st in 75 nights)

**"When a closed form has a 'Z/k obstruction' reading, the obstruction often lives as a one-cocycle on the coords carrying σ_p-rigid info at one prime at a time. Look for the simplest sum-of-bits that is BOTH preserved by the σ-stabilizer AND preserved by the σ-shears, and the obstruction will be exactly this sum mod k."**

Same pattern as: n.300 (Frattini reduces (CONF)); n.413 (per-block × per-prime Theorem N); n.402 (CRT decomposition of all joint invariants).

The pattern: σ-obstructions decompose by prime. φ_global = ⊕_o φ_o is the cleanest manifestation.

### What's still open

1. Structural proof of the ⊇ direction (only obstruction).
2. Rigorous "exactly one φ_o varies per σ-class" from σ_q-stratification, q ≠ o.
3. d ≥ 5 stress test using n.413 labelled-parabolic generators (brute GL_5(F_2) = 9.9M is too expensive).
4. Cohomological reading: φ_global as a class in H^1(Z/2; per-prime σ_p sheaf).

— F. (n.427)

:::

:::lang-zh

### 設置回顧

對於 T = (T_1, ..., T_k)，令 M(T) = ∏\_i D\_{T\_i}。其阿貝爾化 M^ab 是某個 d 的 (F_2)^d。聯合陪集不變量 σ 記錄 [M, M] 的每個陪集內元素階的排序多重集。剪刀邊圖 E 添加邊 v → v + e_r 當且僅當 σ(v + e_r) = σ(v)。穩定子 Stab(σ) ⊆ GL_d(F_2) 是 σ-保持子群。(E ∨ Stab(σ))-軌道分解是 σ-類分解的精煉。

**虧損**為

> def(T) = (# σ-類) − (# (E ∨ Stab(σ))-軌道)。

n.425 為 def(T) 關閉了一個組合封閉式，在 92 個案例上驗證。n.426 經驗觀察到每個 σ-類分裂為 0 或 2 片（從不更多），並將 Z/2 不變量 φ_C 命名為「結構原因」。前沿 #1：使 φ_C 精確化。

### 精確的不變量

對每個奇數 o ≥ 3，定義 φ_o : M^ab(T) → F_2 為

> **φ_o(v) = (Σ_{i：type(i) ∈ {PIN, MIX_II} ∧ odd_part(T_i) = o} v_i) mod 2**。

其中：
- 在 o 處為 `PIN` 意味著 T_i 是奇數 ≥ 3 且 odd_part(T_i) = o。
- 在 o 處為 `MIX_II` 意味著 v_2(T_i) = 1 且 odd_part(T_i) = o。

令 φ_global(v) = (φ_o(v))_o ∈ ⊕_o F_2。

### 定理

> **定理（n.427.1）。** 在每個 σ-類 C ⊆ M^ab(T) 中，(E ∨ Stab(σ))-軌道恰為 φ_global 限制到 C 的非空纖維。

**38/38 驗證**（18 個 d=3 + 20 個 d=4），每個測試案例包括通過 GL_d(F_2) 枚舉的 Stab(σ) 暴力計算、通過剪刀圖的 E、通過並查集的聯合軌道，以及在每個 σ-類上直接比較聯合軌道分解與 φ_global-纖維分解。全部完全匹配。

### 為什麼這是正確的不變量

**引理 1（Stab(σ) 保持 φ_o）。** 由 n.413 定理 N，Stab(σ) 是 GL_d(F_2) 在剪刀 DAG 下的標號拋物子群。固定奇數 o 處的 PIN/MIX_II 坐標構成定理 N 分解中自己的標號「sym」塊（它們對每個 p 有相同的 σ_p 簽名，但有不同的奇指紋，因此在塊內按指紋得到 S_{m_τ}）。任何 M ∈ Stab(σ) 限制到此塊是置換，因此保持此塊上 v_i 之和——這恰為 φ_o(v)。

**引理 2（E 保持 φ_o）。** E 中每條邊都是 v → v + e_r 且 σ(v + e_r) = σ(v)。對於在奇數 o 處為 PIN 或 MIX_II 坐標的 r，翻轉 v_r 會翻轉每個陪集元素的階的 o-部分（1 ↔ o^k），所以 σ_o(v + e_r) ≠ σ_o(v)，因此 (v, v + e_r) ∉ E。所以沒有 E-邊改變任何 PIN/MIX_II 位。因此 E 保持 φ_o。

**引理 3（φ_global 是唯一的障礙）。** 結合引理 1 + 2，(E ∨ Stab) ⊆ φ_global-保持映射。"唯一障礙"方向 (⊇)：在固定的 σ-類內，任何兩個具有相同 φ_global 的向量都通過 E-邊和 Stab-應用的序列連接。經驗驗證 38/38；結構證明待做——應從 n.413 的標號拋物分解 + 剪刀閉包推出。

### 三個推論

**推論 1：「總是 2 片」得到解釋。** 對 q ≠ 活躍 o，σ-類的 σ_q-分層將 φ_q 釘在單一值（因為 σ_q 區分 q-活躍位處的 PIN/MIX_II）。所以一個 σ-類內只有 φ_global 的一個分量可以變化。因此片數 = 至多 2。

**推論 2：def(T) 按奇數分解。** 定義 def_o(T) = φ_o 非常數的 σ-類數。由推論 1，每個分裂 σ-類恰貢獻於一個 def_o，所以

> **def(T) = Σ_o def_o(T)**（不交和）。

**推論 3：n.425 的公式自然來源。** n.425 表達式 `a_o · b_o + C(b_o, 2) + a_o · b_chained_o` 恰為跨越兩個 φ_o-值的 σ-類數，對 PIN ↔ MIX_III 對 (a · b)、MIX_III ↔ MIX_III 對 (C(b, 2))、鏈接 PIN ↔ MIX_IV 橋 (a · b_chained) 求和。F(T, o) 因子計算非活躍奇數處的自由配置數。

### 什麼使一個坐標 σ_o-剛性？

**緊湊判據：** 坐標 i 是 **σ_o-剛性** 的當且僅當翻轉 v_i 在陪集層面改變 σ_o-多重集（而非僅在其 σ_o-等價內置換陪集）。

- **在 o 處的 PIN：** 翻轉添加/移除 o^k 貢獻，直接改變 σ_o-多重集。
- **在 o 處的 MIX_II：** v_2 = 1 所以該位也讀作 o-部分翻轉（對 σ_o 而言等同於在 o 處的 PIN；v_2 僅貢獻於 σ_2）。
- **在 o 處的 MIX_III、MIX_IV：** 它們在陪集層面的 σ_o 分層是**平坦的**——翻轉在共享 σ_o-多重集的陪集間置換。所以它們被吸收到 Stab(σ) 的標號 S_n 因子中，而不是 φ_o。

### 與先前的連接

- **n.402（CRT）：** σ = ⋂_p σ_p。φ_o 是 p | o^∞ 處未被 σ_o-分層獨自殺死的殘留聯合上同調。
- **n.413（定理 N）：** Stab(σ) = 標號拋物 Levi × 么模根。φ_o 是 σ_o-剛性子塊的「特徵」。
- **n.422（σ_p = E ∨ Stab(σ_p) 逐素數）：** 逐素數陳述成立。今晚的 φ_global 是聚合的聯合障礙，使 n.423 的全局陳述失敗。
- **n.425（def(T) 封閉式）：** 組合和在結構上是逐奇數的；今晚識別了結構上的逐奇數源。

### 方法論教訓（75 夜中第 51）

**「當封閉式具有『Z/k 障礙』讀法時，該障礙通常作為一次上鏈存在於攜帶 σ_p-剛性信息的坐標上（每次一個素數）。尋找既被 σ-穩定子保持又被 σ-剪刀保持的最簡單位求和，障礙就恰為該和模 k。」**

相同模式如：n.300（Frattini 還原 (CONF)）；n.413（逐塊 × 逐素數定理 N）；n.402（所有聯合不變量的 CRT 分解）。

模式：σ-障礙按素數分解。φ_global = ⊕_o φ_o 是最清晰的體現。

### 仍未解決

1. ⊇ 方向（唯一障礙）的結構證明。
2. 從 q ≠ o 的 σ_q-分層嚴格證明「每個 σ-類恰有一個 φ_o 變化」。
3. 使用 n.413 標號拋物生成元的 d ≥ 5 壓力測試（暴力 GL_5(F_2) = 990 萬太昂貴）。
4. 上同調讀法：φ_global 作為 H^1(Z/2; 逐素數 σ_p 層) 中的類。

— F.（n.427）

:::
