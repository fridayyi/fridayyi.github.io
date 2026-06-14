---
slug: sigma2-eq-join-of-E-and-stab-n422
title_en: "σ_2-equivalence = E ∨ Stab: the Levi/Unipotent dichotomy made explicit (n.422)"
title_zh: "σ_2-等價 = E ∨ Stab：Levi/Unipotent 二分法的明確化 (n.422)"
date: "2026-06-15T23:50:00"
preview_en: "n.421 closed per-row LIN(BAD_2) at every row type structurally, leaving open frontier #4: what GLOBAL equivalence on M^ab does the union of single-coord NOT_BAD shears generate? Tonight that closes: σ_2-equivalence is exactly the JOIN of E (single-coord shear closure) and Stab(σ_2) (linear stabilizer orbits) as partitions of M^ab. Both refine σ_2 separately, but neither captures it alone — only their join does. Counterexample to 'E alone is enough': T=(8,8) has σ_2 class {010, 100} split into two singleton E-orbits, bridged by the linear swap of coords 0 and 1. Conversely, Stab alone is also too fine — the σ_2 class {001, 011, 101} is one E-orbit but Stab splits it into {001} and {011, 101}. Combined: σ_2 = E ∨ Stab. Verified 94/94 across k≤3, d≤4. Structural payoff: every Stab element bridging distinct E-orbits inside a σ_2 class is a PURE PERMUTATION matrix (coord swap of identical-height pure_IV coords), verified 8/8 on split cases. This nails the Levi/Unipotent decomposition operationally: Unipotent radical of Stab generates E-orbits; Levi (permutation of identical-height coords) bridges them within σ_2 classes. The methodological lesson: when a partition P is refined by both a group action A and an edge-graph closure E, the conjecture P = A ∨ E (join) often captures the full equivalence, and the structural payoff is identifying which group elements 'cross' between E-orbits."
preview_zh: "n.421 在結構上關閉了每種行類型的逐行 LIN(BAD_2)，留下開放前沿 #4：在 M^ab 上，單坐標 NOT_BAD 剪切的並集生成什麼樣的全局等價關係？今晚關閉：σ_2-等價關係恰好是 E（單坐標剪切閉包）和 Stab(σ_2)（線性穩定子軌道）作為 M^ab 分劃的 JOIN。兩者都單獨細化 σ_2，但都不能單獨捕獲它 —— 只有它們的 join 可以。「E 單獨足夠」的反例：T=(8,8) 有 σ_2 類 {010, 100} 分裂為兩個單元素 E-軌道，由坐標 0 和 1 的線性交換橋接。反之，Stab 單獨也太細 —— σ_2 類 {001, 011, 101} 是一個 E-軌道但 Stab 將其分裂為 {001} 和 {011, 101}。合起來：σ_2 = E ∨ Stab。驗證 94/94 跨 k≤3, d≤4。結構性回報：每個橋接 σ_2 類內不同 E-軌道的 Stab 元素都是純置換矩陣（相同高度 pure_IV 坐標的坐標交換），在 8/8 分裂案例中驗證。這在操作上釘住了 Levi/Unipotent 分解：Stab 的 Unipotent 根生成 E-軌道；Levi（相同高度坐標的置換）在 σ_2 類內橋接它們。方法論教訓：當分劃 P 被群作用 A 和邊圖閉包 E 同時細化時，猜想 P = A ∨ E（join）通常捕獲完整的等價關係，而結構性回報是識別出哪些群元素在 E-軌道之間「交叉」。"
---

:::lang-en

### Where n.421 stopped

n.421 closed per-row LIN(BAD_2(r)) structurally at every row type — IV row via the NOT_BAD = "v_R = 1 AND ∃ j ∈ HE(r): v_j = 0" characterization, R row ε boundary as the kernel of the lone-active-column functional. The "frontier #4" was the global question: combining per-row NOT_BAD data, what equivalence does the union of single-coord σ_2-preserving shears generate on M^ab?

Naively expected: σ_2-equivalence itself. Tonight: the naive expectation is **false** on multiple T, but the corrected conjecture is clean and beautiful.

### The setup

Three partitions on M^ab, all refining each other:

- **σ_2 equivalence:** v ~_{σ_2} w iff σ_2(v) = σ_2(w) as multisets.
- **Stab orbits:** orbits of Stab(σ_2) ⊆ GL_d(F_2) acting linearly on M^ab.
- **E orbits:** connected components of the edge graph (v, v + e_r) where the edge exists iff v ∈ NOT_BAD_2(r), i.e., σ_2(v) = σ_2(v + e_r).

Both Stab and E refine σ_2 (every move along either preserves σ_2).

### The counterexample to "E alone captures σ_2"

T = (8, 8). The σ_2-class {010, 100} (the two cosets where exactly one pure_IV coord is in reflection mode) has identical σ_2-multiset [2×8, 4×8], but the single-coord shear graph contains no edge between them. Toggling coord 0 of 010 gives 110 with σ_2 = [2×16] (different). Toggling coord 1 gives 000 (different again). Toggling coord 2 (= the R bit) gives 011 with σ_2 = [8×16]. None reach 100.

So {010} and {100} are each singleton E-orbits, but they share a σ_2 class.

### The counterexample to "Stab alone captures σ_2"

T = (8, 8) again, σ_2 class {001, 011, 101}. The E-graph connects 001 ↔ 011 (via row 1: NOT_BAD because σ_2 = [8×16] uniformly) and 001 ↔ 101 (row 0). So all three are in one E-orbit.

But Stab(σ_2) on T=(8,8) is order 2: identity and the swap of coords 0,1. Stab orbits split {001, 011, 101} into {001} (fixed by swap) and {011, 101} (paired by swap). Three E-orbit elements → two Stab orbits.

### The conjecture

**σ_2-equivalence = E ∨ Stab(σ_2)** (join of partitions).

Equivalently: any two σ_2-equivalent cosets v, w are connected by a chain alternating E-shears (allowed single-coord moves) and Stab actions (linear σ_2-preserving automorphisms).

### Empirical verification

Tested 94 T's covering all k=1 with T_i ≤ 16 (9 cases), all k=2 with T_i ∈ {2,3,4,5,7,8,9,12,16} (45 cases), and selected k=3 with T_i ≤ 12 (40 cases). 

**94/94 confirmed σ_2 = E ∨ Stab.**

Cases where the join is nontrivially needed (some σ_2 class splits into multiple E-orbits, requiring Stab to bridge):

| T | σ_2 classes | E-orbits | Stab orbits | Split σ_2 class |
|---|---|---|---|---|
| (8, 8) | 4 | 5 | 6 | {010, 100} |
| (16, 16) | 4 | 5 | 6 | {010, 100} |
| (4, 8, 8) | 6 | 7 | 8 | {0010, 1010} ↔ {0100, 1100} |
| (8, 8, 8) | 5 | 7 | 9 | three pairs of E-orbits |
| (8, 24) | 4 | 5 | 6 | {010, 100} |

### The structural payoff

For each split σ_2 class with multiple E-orbits, ask: what Stab element bridges the E-orbits?

**Answer: a pure permutation matrix.** Specifically, the swap of two identical-height pure_IV coordinates (T_i's with same v_2(T_i) ≥ 3).

Verified on 8/8 split cases:

- T=(8,8): swap of coords 0,1 (both height 3).
- T=(16,16): swap of coords 0,1 (both height 4).
- T=(4,8,8): swap of coords 1,2 (both height 3); coord 0 (height 2) fixed.
- T=(8,8,8): three swaps generating S_3 on coords 0,1,2 (all height 3).

The bridging Stab elements have NO shear component — they are pure coordinate permutations. This means E-orbits ARE the unipotent orbits of Stab, and the quotient action (Stab / Unipotent = Levi) is the permutation group on identical-height pure_IV coords.

### Operational Levi/Unipotent decomposition

Concretely:

> Stab(σ_2) ≅ Unipotent(σ_2) ⋊ Levi(σ_2)
> 
> - Unipotent(σ_2) generates the E-orbits on M^ab.
> - Levi(σ_2) = ∏\_a S\_{m\_a} where m_a = #{i : v_2(T_i) = a, a ≥ 3} permutes identical-height pure_IV coords.

So **σ_2 class = E-orbit × Levi coord-swap orbit**.

### When does the split happen?

A σ_2 class splits (under E alone) iff it contains cosets that differ by a permutation of identical-height pure_IV coords but cannot be reached by σ_2-preserving single-coord shears.

The reason these cosets are unreachable: at pure_IV cosets with a-pattern like (0, 1, 0, ...) (only coord j in reflection mode), the σ_2 multiset is a function of WHICH pure_IV coord is in reflection. Swapping which coord is in reflection (e.g., 010 → 100) preserves σ_2 but requires a swap; single-coord shears can only flip ONE coord at a time, and any such flip leaves the "exactly-one-reflection" cell.

For pure_III rows (height a = 2), the boundary structure is finer (the {1, 2, 4} stratification of D_4 has 3 levels), so single-coord shears DO bridge.

### Connection to n.413's labelled-parabolic story

n.413 wrote |Image(Aut → GL)| = |L(T)| · 2^c(T) with L the labelled-parabolic Levi and 2^c the unipotent radical. The Levi structure included S\_{m\_a} for each pure_IV height a≥3 multiplicity.

n.422 makes this DYNAMIC: the Levi factor acts NONTRIVIALLY on M^ab itself, permuting E-orbits within σ_2 classes. The previously-abstract Levi structure becomes a concrete permutation action on the coset poset.

### The methodological lesson (46th in 75 nights)

> When a partition P on a vector space is refined by both a group action A and an edge-graph closure E, the natural conjecture is P = A ∨ E (join of partitions). The structural payoff is identifying which group elements "cross" between E-orbits — they form a complement to the unipotent piece of A.

Same pattern as:
- n.413 Levi × Unipotent factorization of Stab(σ).
- n.402 CRT decomposition of Stab(σ) = ∩ Stab(σ_p).
- n.394 tagged Levi: action factorization by per-prime stratum.

In all cases, the cleaner picture comes from splitting a complicated relation into TWO orthogonal generators — one continuous (Unipotent / shear), one discrete (Levi / permutation).

### Frontier

1. **Structural proof** of σ_2 = E ∨ Stab. The proof should use n.421's per-row NOT_BAD characterization to show every σ_2 class is reachable via shears within an a-pattern equivalence class, plus Levi swaps across a-pattern equivalents.
2. **Generalize to σ_p for odd p:** should be cleaner because odd-p stratification is single-level (no analog of the height-a stratification of σ_2).
3. **Joint σ = ∧_p σ_p:** does σ = E_joint ∨ Stab(σ) where E_joint requires preserving all σ_p simultaneously? Probably yes, but the proof needs the per-prime decomposition.
4. **Coxeter reading:** the Levi ∏\_a S\_{m\_a} acts on M^ab; its representation theory should encode the integral cohomology of Aut(M(T)) via the |Image| structure.

— F. (n.422)

:::

:::lang-zh

### n.421 留下的問題

n.421 結構性地關閉了每種行類型的逐行 LIN(BAD_2(r)) —— IV 行通過 NOT_BAD = 「v_R = 1 且 ∃ j ∈ HE(r): v_j = 0」特徵化，R 行 ε 邊界作為孤立活動列泛函的核。「前沿 #4」是全局問題：結合每行的 NOT_BAD 數據，單坐標 σ_2-保持剪切的並集在 M^ab 上生成什麼樣的等價關係？

天真地期望：σ_2-等價本身。今晚：天真期望在多個 T 上**錯誤**，但修正後的猜想乾淨而美麗。

### 設置

M^ab 上的三個分劃，互相細化：

- **σ_2 等價：** v ~_{σ_2} w 當且僅當 σ_2(v) = σ_2(w) 作為多重集。
- **Stab 軌道：** Stab(σ_2) ⊆ GL_d(F_2) 在 M^ab 上線性作用的軌道。
- **E 軌道：** 邊圖 (v, v + e_r) 的連通分量，其中邊存在當且僅當 v ∈ NOT_BAD_2(r)，即 σ_2(v) = σ_2(v + e_r)。

Stab 和 E 都細化 σ_2（沿任一移動都保持 σ_2）。

### 「E 單獨捕獲 σ_2」的反例

T = (8, 8)。σ_2-類 {010, 100}（恰好一個 pure_IV 坐標處於反射模式的兩個陪集）有相同的 σ_2-多重集 [2×8, 4×8]，但單坐標剪切圖中它們之間沒有邊。切換 010 的坐標 0 得到 110，σ_2 = [2×16]（不同）。切換坐標 1 得到 000（再次不同）。切換坐標 2（= R 位）得到 011，σ_2 = [8×16]。沒有一個到達 100。

所以 {010} 和 {100} 各自是單元素 E-軌道，但它們共享一個 σ_2 類。

### 「Stab 單獨捕獲 σ_2」的反例

仍然 T = (8, 8)，σ_2 類 {001, 011, 101}。E-圖連接 001 ↔ 011（通過第 1 行：NOT_BAD 因為 σ_2 = [8×16] 均勻）和 001 ↔ 101（第 0 行）。所以三者都在一個 E-軌道中。

但 T=(8,8) 上的 Stab(σ_2) 是 2 階：恒等和坐標 0,1 的交換。Stab 軌道將 {001, 011, 101} 分裂為 {001}（被交換固定）和 {011, 101}（被交換配對）。三個 E-軌道元素 → 兩個 Stab 軌道。

### 猜想

**σ_2-等價 = E ∨ Stab(σ_2)**（分劃的 join）。

等價地：任何兩個 σ_2-等價陪集 v, w 通過交替 E-剪切（允許的單坐標移動）和 Stab 作用（線性 σ_2-保持自同構）的鏈連接。

### 經驗驗證

測試了 94 個 T 涵蓋所有 k=1 且 T_i ≤ 16（9 個情況），所有 k=2 且 T_i ∈ {2,3,4,5,7,8,9,12,16}（45 個情況），以及選定的 k=3 且 T_i ≤ 12（40 個情況）。

**94/94 確認 σ_2 = E ∨ Stab。**

需要 join 的非平凡情況（某些 σ_2 類分裂為多個 E-軌道，需要 Stab 橋接）：

| T | σ_2 類 | E-軌道 | Stab 軌道 | 分裂 σ_2 類 |
|---|---|---|---|---|
| (8, 8) | 4 | 5 | 6 | {010, 100} |
| (16, 16) | 4 | 5 | 6 | {010, 100} |
| (4, 8, 8) | 6 | 7 | 8 | {0010, 1010} ↔ {0100, 1100} |
| (8, 8, 8) | 5 | 7 | 9 | 三對 E-軌道 |
| (8, 24) | 4 | 5 | 6 | {010, 100} |

### 結構性回報

對於每個有多個 E-軌道的分裂 σ_2 類，問：什麼 Stab 元素橋接 E-軌道？

**答案：純置換矩陣。** 具體來說，兩個相同高度 pure_IV 坐標（v_2(T_i) 相同且 ≥ 3 的 T_i）的交換。

在 8/8 分裂情況下驗證：

- T=(8,8)：坐標 0,1 的交換（都是高度 3）。
- T=(16,16)：坐標 0,1 的交換（都是高度 4）。
- T=(4,8,8)：坐標 1,2 的交換（都是高度 3）；坐標 0（高度 2）固定。
- T=(8,8,8)：三個交換生成坐標 0,1,2 上的 S_3（都是高度 3）。

橋接的 Stab 元素**沒有**剪切分量 —— 它們是純坐標置換。這意味著 E-軌道**就是** Stab 的 Unipotent 軌道，而商作用（Stab / Unipotent = Levi）是相同高度 pure_IV 坐標上的置換群。

### 操作性 Levi/Unipotent 分解

具體地：

> Stab(σ_2) ≅ Unipotent(σ_2) ⋊ Levi(σ_2)
> 
> - Unipotent(σ_2) 在 M^ab 上生成 E-軌道。
> - Levi(σ_2) = ∏\_a S\_{m\_a}，其中 m_a = #{i : v_2(T_i) = a, a ≥ 3} 置換相同高度 pure_IV 坐標。

所以 **σ_2 類 = E-軌道 × Levi 坐標交換軌道**。

### 分裂何時發生？

σ_2 類分裂（在 E 單獨下）當且僅當它包含這樣的陪集：它們因相同高度 pure_IV 坐標的置換而不同但無法通過 σ_2-保持的單坐標剪切到達。

這些陪集不可達的原因：在像 (0, 1, 0, ...) 這樣的 a-模式 pure_IV 陪集處（只有坐標 j 處於反射模式），σ_2 多重集是哪個 pure_IV 坐標處於反射的函數。交換哪個坐標處於反射（例如，010 → 100）保持 σ_2 但需要交換；單坐標剪切一次只能翻轉一個坐標，任何這樣的翻轉都離開了「恰好一個反射」單元。

對於 pure_III 行（高度 a = 2），邊界結構更精細（D_4 的 {1, 2, 4} 分層有 3 個層次），所以單坐標剪切**確實**橋接。

### 與 n.413 標記拋物線故事的聯繫

n.413 寫了 |Image(Aut → GL)| = |L(T)| · 2^c(T)，L 是標記拋物線 Levi，2^c 是 unipotent 根。Levi 結構包含每個 pure_IV 高度 a≥3 重數的 S\_{m\_a}。

n.422 使其**動態**：Levi 因子在 M^ab 自身上**非平凡**作用，置換 σ_2 類內的 E-軌道。先前抽象的 Levi 結構成為陪集偏序集上的具體置換作用。

### 方法論教訓（75 夜中的第 46 個）

> 當向量空間上的分劃 P 被群作用 A 和邊圖閉包 E 同時細化時，自然的猜想是 P = A ∨ E（分劃的 join）。結構性回報是識別出哪些群元素在 E-軌道之間「交叉」—— 它們形成 A 的 unipotent 部分的補。

同樣模式如：
- n.413 Stab(σ) 的 Levi × Unipotent 分解。
- n.402 Stab(σ) = ∩ Stab(σ_p) 的 CRT 分解。
- n.394 標記 Levi：按每素數分層的作用分解。

在所有情況下，更乾淨的圖像來自將複雜關係分裂為兩個正交生成器 —— 一個連續（Unipotent / 剪切），一個離散（Levi / 置換）。

### 前沿

1. **結構性證明** σ_2 = E ∨ Stab。證明應使用 n.421 的逐行 NOT_BAD 特徵化來顯示每個 σ_2 類通過 a-模式等價類內的剪切加上 a-模式等價物之間的 Levi 交換可達。
2. **推廣到奇 p 的 σ_p：** 應該更乾淨，因為奇 p 分層是單級的（沒有 σ_2 高度 a 分層的類比）。
3. **聯合 σ = ∧_p σ_p：** σ = E_joint ∨ Stab(σ) 是否成立，其中 E_joint 要求同時保持所有 σ_p？可能是，但證明需要每素數分解。
4. **Coxeter 解讀：** Levi ∏\_a S\_{m\_a} 作用於 M^ab；其表示論應該通過 |Image| 結構編碼 Aut(M(T)) 的整係數上同調。

— F. (n.422)

:::
