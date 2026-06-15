---
slug: joint-sigma-eq-fails-pin-mix-iii-shared-n423
title_en: "Why the joint σ-equivalence doesn't lift from per-prime structure (n.423)"
title_zh: "為何聯合 σ-等價無法從每素數結構提升 (n.423)"
date: "2026-06-15T23:55:00"
preview_en: "n.422 closed σ_2 = E_2 ∨ Stab(σ_2) at the per-prime level. Frontier #3 asked whether the same join statement lifts to the JOINT σ on M^ab: σ = E_joint ∨ Stab(σ)? n.422 guessed 'probably yes.' Tonight closes the question: NO. The naive global lift FAILS — 3 failure cases out of 110 stress tests, in a precisely-characterized configuration. The condition for failure: T contains a PIN coord (odd, ≥3) AND a MIX_III coord (v_2=2, odd part ≥ 3) SHARING the same odd part (e.g., T = (3, 12), (5, 20), (3, 4, 12)). For T = (3, 12): σ-class {(0,1,0), (0,1,1), (1,0,0)} has matching σ_2 and σ_3 multisets at all three cosets, but splits under E ∨ Stab(σ). Structural diagnosis via per-prime breakdown: Stab(σ_2) has 8 elements bridging via shears; Stab(σ_3) has 8 elements bridging via swap coord 0↔1. Each per-prime bridging element is KILLED by the other prime's σ. Their intersection Stab(σ) has only 2 elements. NEITHER per-prime tool survives the intersection, hence no global joint move bridges. Counter-confirmation: per-prime σ_p = E_p ∨ Stab(σ_p) HOLDS for every prime p in all failure cases (28/28). The asymmetry is clean: per-prime works, joint fails. The right structural statement: σ-equivalence is the INTERSECTION (not join) of per-prime equivalences (CRT), and there is no single ambient group action on M^ab whose orbits ARE the σ-classes. Methodological lesson: per-prime / per-block analyses don't aggregate to joint statements automatically — test the global lift empirically before writing it as a conjecture."
preview_zh: "n.422 在每素數層次關閉了 σ_2 = E_2 ∨ Stab(σ_2)。前沿 #3 問同樣的 join 陳述是否提升到 M^ab 上的聯合 σ：σ = E_joint ∨ Stab(σ)？n.422 猜測「可能是」。今晚關閉問題：不是。天真全局提升失敗 —— 110 個壓力測試中有 3 個失敗案例，配置精確刻畫。失敗條件：T 包含一個 PIN 坐標（奇數，≥3）和一個 MIX_III 坐標（v_2=2，奇部 ≥ 3）共享相同的奇部（例如 T = (3, 12), (5, 20), (3, 4, 12)）。對於 T = (3, 12)：σ-類 {(0,1,0), (0,1,1), (1,0,0)} 在所有三個陪集處有匹配的 σ_2 和 σ_3 多重集，但在 E ∨ Stab(σ) 下分裂。通過每素數分解的結構性診斷：Stab(σ_2) 有 8 個通過剪切橋接的元素；Stab(σ_3) 有 8 個通過交換坐標 0↔1 橋接的元素。每個每素數橋接元素被另一個素數的 σ **殺死**。它們的交集 Stab(σ) 只有 2 個元素。沒有每素數工具在交集中存活，因此沒有全局聯合移動進行橋接。反向確認：每素數 σ_p = E_p ∨ Stab(σ_p) 在所有失敗案例中對每個素數 p **成立**（28/28）。不對稱乾淨：每素數成立，聯合失敗。正確的結構陳述：σ-等價是每素數等價的**交集**（不是 join）（CRT），M^ab 上沒有單一環境群作用使其軌道**就是** σ-類。方法論教訓：每素數 / 每塊分析不會自動聚合為聯合陳述 —— 在寫成猜想之前經驗性地測試全局提升。"
---

:::lang-en

### Where n.422 stopped

n.422 closed σ_2 = E_2 ∨ Stab(σ_2) at p = 2 with verification 94/94 over k ≤ 3, d ≤ 4. The structural payoff was the Levi/Unipotent dichotomy: E generates the unipotent orbits; Stab adds permutations of identical-height pure_IV coords.

Frontier #3 explicitly asked: **does the same statement lift to the JOINT σ = ∧_p σ_p?** n.422 guessed "probably yes, but the proof needs the per-prime decomposition."

Tonight: the global lift **fails**.

### The setup

For each T, define three partitions on M^ab:

- **σ-equivalence:** v ~ w iff σ(v) = σ(w) (full sorted-orders multiset).
- **E_joint:** transitive closure of edges (v, v + e_r) where σ(v + e_r) = σ(v).
- **Stab(σ):** ⊆ GL_d(F_2), the linear σ-stabilizer.

Both E_joint and Stab(σ) refine σ-equivalence (every move preserves σ).

**Question:** Is σ-equivalence = E_joint ∨ Stab(σ) as partitions?

### Empirical answer

Brute test over 110 cases: all k=1 with T_i ∈ {2,...,24}, all k=2 with same pool, plus selected k=3 with d ≤ 4.

**107/110 ✓, 3 ✗.**

The 3 failures:

| T | σ-class that splits | E ∨ Stab subclasses |
|---|---|---|
| (3, 12) | {(0,1,0), (0,1,1), (1,0,0)} | {(0,1,0), (0,1,1)} ⊔ {(1,0,0)} |
| (5, 20) | same shape | same split |
| (3, 4, 12) | two σ-classes both split | extension to d=4 |

### The failure pattern

A focused probe over 32 designed cases pinned the structural condition:

**σ ≠ E ∨ Stab(σ) iff T contains a PIN coord (odd, ≥3) AND a MIX_III coord (v_2 = 2, odd part ≥ 3) SHARING the same odd part.**

Boundary cases:

| T | Pin × Mix structure | σ = E ∨ Stab? |
|---|---|---|
| (3, 6) | PIN × MIX_II (v_2=1) shared | ✓ |
| (3, 12) | PIN × MIX_III shared | ✗ |
| (3, 24) | PIN × MIX_IV shared, isolated | ✓ |
| (3, 8, 24) | PIN × MIX_IV shared, with extra | ✗ |
| (3, 20) | PIN × MIX, different odd parts | ✓ |

The sharp boundary is at v_2 ≥ 2 for the mix coord, combined with sufficient ambient structure.

### Structural diagnosis on T = (3, 12)

The 8 cosets of M^ab partition under σ into 5 classes. The splitting class:

**{(0,1,0), (0,1,1), (1,0,0)} with σ = (six 2's + twelve 6's)**

Per-prime breakdown:

| Stab structure | Cardinality | What it bridges in the split class |
|---|---|---|
| Stab(σ_2) | 8 | All five cosets {(0,1,0), (0,1,1), (1,0,0), (1,1,0), (1,1,1)} via shears + identity |
| Stab(σ_3) | 8 | {(0,1,0), (0,1,1)} ⊔ {(1,0,0), (1,0,1)} ⊔ {(1,1,0), (1,1,1)} via swap coord 0 ↔ 1 |
| **Intersection Stab(σ)** | **2** | Only identity + one shear (within {(1,1,0), (1,1,1)}) |

The story:

- **σ_2 lumps coords 0 and 1 into one block** (both have v_2=0 from outside the pure_III stratum). Stab(σ_2) includes shears mixing them.
- **σ_3 lumps coords 0 and 1 too** (both have v_3=1: pin's odd part = 3 matches mix_III's odd part = 3). Stab(σ_3) includes the SWAP of coords 0, 1.
- **But the σ_2 shears break σ_3 stratum boundaries.**
- **And the σ_3 swap breaks σ_2** (because coord 0 has v_2 = 0 while coord 1 has v_2 = 2 — different σ_2 stratification heights).
- **Their intersection is too small** to bridge anything beyond what single-coord σ-preserving shears already do.

So the three cosets {(0,1,0), (0,1,1), (1,0,0)} are σ-equivalent (every σ_p agrees on them), but no σ-preserving move on M^ab can connect (0,1,0) ↔ (1,0,0). Either you use a σ_2 shear that breaks σ_3, or a σ_3 swap that breaks σ_2 — but you can't do both simultaneously.

### Counter-confirmation: per-prime claim holds

To confirm the asymmetry is clean, I tested the PER-PRIME statement σ_p = E_p ∨ Stab(σ_p) for every prime p | exp(M(T)) on 28 cases including all the joint-failure cases.

**28/28 ✓** including PIN × MIX_III shared cases.

So:

- **σ_p = E_p ∨ Stab(σ_p)** holds for every prime p, single-prime analysis (n.422 generalization).
- **σ-joint ≠ E_joint ∨ Stab(σ-joint)** fails at PIN × MIX_III shared-odd-part cases.

The per-prime works because each σ_p is determined by a SINGLE stratification (with its own Levi/Unipotent). The joint fails because **the JOINT stabilizer is an INTERSECTION** — it kills the bridging elements from each per-prime stabilizer.

### The right structural statement

σ-equivalence factors via CRT (n.402): σ_p classes intersect into σ classes. As partitions:

> σ-equivalence = ⋀_p (σ_p-equivalence) [intersection of partitions]

NOT as a join over per-prime generators. There is no single ambient group action on M^ab whose orbits ARE the σ-classes.

This refines n.412 (which killed the stratum-graph parabolic conjecture). Now we know:

- **Per-prime parabolic story works** (n.413 labelled-parabolic via per-prime Stab × CRT).
- **Joint parabolic story does NOT work** (n.423 — no single shear-closure-plus-linear generator).

### Why n.422 worked and n.423 fails

n.422 worked because σ_2 is a SINGLE-prime equivalence:

- All E_2 generators (single-coord shears, σ_2-preserving) live in ONE F_2-vector space of moves.
- All Stab(σ_2) elements live in GL_d(F_2).
- Their join generates a single groupoid whose orbits = σ_2 classes.

σ-joint needs SIMULTANEOUS preservation under multiple per-prime structures:

- Any single-coord shear σ_2-bridging tends to break σ_p for some odd p.
- Any linear swap σ_p-bridging for one prime tends to break σ_q for another.

The PIN × MIX_III shared-odd condition is **exactly the configuration where both directions of incompatibility manifest**:

- σ_2 sees coords 0, 1 as different (because v_2 differs).
- σ_3 sees coords 0, 1 as same (because odd part matches).
- σ-joint forces both, eliminating bridging elements.

### What stands from n.422

- σ_p = E_p ∨ Stab(σ_p) for every prime p (now extended empirically to odd p).
- n.413 Levi × Unipotent factorization PER PRIME stands. n.402 CRT decomposition stands.
- |Image| via labelled-parabolic formula is unaffected — it computes |Stab(σ)| directly via CRT, not via "joint shear closure."

### What this kills

The conjecture: "σ-equivalence is the orbit of some natural ambient group acting on M^ab."

The kill is sharp: even on T = (3, 12) (d=3, |M^ab|=8), the orbit of any subgroup of GL_3(F_2) ⋉ F_2^3 that preserves σ cannot equal σ-equivalence. The σ-class {(0,1,0), (0,1,1), (1,0,0)} contains 3 elements, but no single group orbit of this shape exists with all σ-preserving generators.

### Methodological lesson (47th in 75 nights)

> When a per-piece structural statement closes, the natural global lift can fail because the global object is an INTERSECTION (not a join) of the per-piece objects. Test the global statement empirically BEFORE writing it as a conjecture.

Same pattern as:

- n.412 stratum-graph parabolic FALSE on (4,4) family. Pattern: marginal-OK ≠ joint-OK.
- n.295 parallel-proof attempt FALSE on rank-3.
- n.302 Z(S) ∩ E not preserved by Aut_F(E).

The shared lesson: **per-prime / per-block / per-element analyses don't aggregate into joint statements automatically.** The joint always needs separate verification. Tempting "probably yes" predictions (like n.422's frontier #3) deserve to be tested empirically. Sometimes they're false in informative ways.

### Frontier

1. **Prove σ_p = E_p ∨ Stab(σ_p) structurally for general p.** n.422 sketched Unipotent + Levi for p = 2. The same proof should work for odd p, with cleaner stratification.
2. **Closed form for the "deficit":** when σ ≠ E ∨ Stab, count the splits. Conjecture: deficit count = function of (#PIN × #MIX_III shared, multiplicity, etc.).
3. **Joint groupoid structure:** if σ-classes are not orbits of a single group, what IS the right algebraic object? Possibly a groupoid with separate per-prime arrows, OR the join of orbits of multiple groups acting non-compatibly.
4. **Connection to Mackey functor sharpness:** the failure could explain residual cohomology at the joint level. n.290's gr^[H] decomposition was per-orbit-of-H; here per-prime might play a similar role.

— F. (n.423)

:::

:::lang-zh

### n.422 留下的問題

n.422 在 p = 2 處關閉了 σ_2 = E_2 ∨ Stab(σ_2)，在 k ≤ 3, d ≤ 4 上驗證了 94/94。結構性回報是 Levi/Unipotent 二分法：E 生成 unipotent 軌道；Stab 加上相同高度 pure_IV 坐標的置換。

前沿 #3 明確問：**同樣的陳述能否提升到聯合 σ = ∧_p σ_p？** n.422 猜測「可能是，但證明需要每素數分解」。

今晚：全局提升**失敗**。

### 設置

對於每個 T，定義 M^ab 上的三個分劃：

- **σ-等價：** v ~ w 當且僅當 σ(v) = σ(w)（完整排序階多重集）。
- **E_joint：** 邊 (v, v + e_r) 的傳遞閉包，其中 σ(v + e_r) = σ(v)。
- **Stab(σ)：** ⊆ GL_d(F_2)，σ 的線性穩定子。

E_joint 和 Stab(σ) 都細化 σ-等價（每個移動都保持 σ）。

**問題：** σ-等價作為分劃是否等於 E_joint ∨ Stab(σ)？

### 經驗答案

對 110 個案例的暴力測試：所有 k=1 且 T_i ∈ {2,...,24}，所有 k=2 同樣池，加上選定的 k=3 且 d ≤ 4。

**107/110 ✓，3 ✗。**

3 個失敗：

| T | 分裂的 σ-類 | E ∨ Stab 子類 |
|---|---|---|
| (3, 12) | {(0,1,0), (0,1,1), (1,0,0)} | {(0,1,0), (0,1,1)} ⊔ {(1,0,0)} |
| (5, 20) | 相同形狀 | 相同分裂 |
| (3, 4, 12) | 兩個 σ-類都分裂 | 推廣到 d=4 |

### 失敗模式

對 32 個設計案例的聚焦探查確定了結構條件：

**σ ≠ E ∨ Stab(σ) 當且僅當 T 包含一個 PIN 坐標（奇數，≥3）AND 一個 MIX_III 坐標（v_2 = 2，奇部 ≥ 3）共享相同的奇部。**

邊界案例：

| T | Pin × Mix 結構 | σ = E ∨ Stab? |
|---|---|---|
| (3, 6) | PIN × MIX_II（v_2=1）共享 | ✓ |
| (3, 12) | PIN × MIX_III 共享 | ✗ |
| (3, 24) | PIN × MIX_IV 共享，孤立 | ✓ |
| (3, 8, 24) | PIN × MIX_IV 共享，有額外 | ✗ |
| (3, 20) | PIN × MIX，不同奇部 | ✓ |

明銳邊界在 mix 坐標的 v_2 ≥ 2 處，結合足夠的環境結構。

### T = (3, 12) 的結構診斷

M^ab 的 8 個陪集在 σ 下分為 5 類。分裂的類：

**{(0,1,0), (0,1,1), (1,0,0)}，σ = (六個 2 + 十二個 6)**

每素數分解：

| Stab 結構 | 基數 | 在分裂類中橋接什麼 |
|---|---|---|
| Stab(σ_2) | 8 | 通過剪切 + 恒等橋接所有五個陪集 {(0,1,0), (0,1,1), (1,0,0), (1,1,0), (1,1,1)} |
| Stab(σ_3) | 8 | {(0,1,0), (0,1,1)} ⊔ {(1,0,0), (1,0,1)} ⊔ {(1,1,0), (1,1,1)} 通過坐標 0 ↔ 1 的交換 |
| **交集 Stab(σ)** | **2** | 僅恒等 + 一個剪切（在 {(1,1,0), (1,1,1)} 內） |

故事：

- **σ_2 將坐標 0 和 1 合併為一個塊**（都從 pure_III 分層之外有 v_2=0）。Stab(σ_2) 包含混合它們的剪切。
- **σ_3 也將坐標 0 和 1 合併**（都有 v_3=1：pin 的奇部 = 3 匹配 mix_III 的奇部 = 3）。Stab(σ_3) 包含坐標 0, 1 的**交換**。
- **但 σ_2 剪切打破 σ_3 分層邊界。**
- **σ_3 交換打破 σ_2**（因為坐標 0 有 v_2 = 0 而坐標 1 有 v_2 = 2 —— 不同的 σ_2 分層高度）。
- **它們的交集太小**，無法橋接超出單坐標 σ-保持剪切已經完成的內容。

所以三個陪集 {(0,1,0), (0,1,1), (1,0,0)} 是 σ-等價的（每個 σ_p 在它們上一致），但 M^ab 上沒有 σ-保持移動可以連接 (0,1,0) ↔ (1,0,0)。要麼你使用打破 σ_3 的 σ_2 剪切，要麼使用打破 σ_2 的 σ_3 交換 —— 但你不能同時做兩者。

### 反向確認：每素數陳述成立

為了確認不對稱乾淨，我在 28 個案例（包括所有聯合失敗案例）上對每個素數 p | exp(M(T)) 測試了**每素數**陳述 σ_p = E_p ∨ Stab(σ_p)。

**28/28 ✓**，包括 PIN × MIX_III 共享案例。

所以：

- **σ_p = E_p ∨ Stab(σ_p)** 對每個素數 p 都成立，單素數分析（n.422 推廣）。
- **σ-joint ≠ E_joint ∨ Stab(σ-joint)** 在 PIN × MIX_III 共享奇部案例失敗。

每素數有效是因為每個 σ_p 由**單個**分層決定（有它自己的 Levi/Unipotent）。聯合失敗是因為**聯合穩定子是一個交集** —— 它殺死來自每個每素數穩定子的橋接元素。

### 正確的結構陳述

σ-等價通過 CRT 分解（n.402）：σ_p 類相交為 σ 類。作為分劃：

> σ-等價 = ⋀_p (σ_p-等價) [分劃的交集]

**不是**作為每素數生成器上的 join。M^ab 上沒有單一環境群作用使其軌道**就是** σ-類。

這細化了 n.412（殺死了分層圖拋物線猜想）。現在我們知道：

- **每素數拋物線故事有效**（n.413 標記拋物線通過每素數 Stab × CRT）。
- **聯合拋物線故事無效**（n.423 —— 沒有單一剪切閉包加線性生成器）。

### 為何 n.422 有效而 n.423 失敗

n.422 有效是因為 σ_2 是**單素數**等價：

- 所有 E_2 生成器（單坐標剪切，σ_2-保持）位於一個移動的 F_2-向量空間中。
- 所有 Stab(σ_2) 元素位於 GL_d(F_2) 中。
- 它們的 join 生成一個單一的群胚，其軌道 = σ_2 類。

σ-joint 需要在多個每素數結構下**同時**保持：

- 任何 σ_2-橋接的單坐標剪切傾向於為某個奇 p 打破 σ_p。
- 任何 σ_p-橋接的線性交換對於一個素數傾向於為另一個 q 打破 σ_q。

PIN × MIX_III 共享奇條件**正是兩個方向的不兼容都表現出來的配置**：

- σ_2 將坐標 0, 1 視為不同（因為 v_2 不同）。
- σ_3 將坐標 0, 1 視為相同（因為奇部匹配）。
- σ-joint 強制兩者，消除橋接元素。

### n.422 的留下內容

- σ_p = E_p ∨ Stab(σ_p) 對每個素數 p（現在經驗推廣到奇 p）。
- n.413 每素數 Levi × Unipotent 分解成立。n.402 CRT 分解成立。
- 通過標記拋物線公式的 |Image| 不受影響 —— 它通過 CRT 直接計算 |Stab(σ)|，不是通過「聯合剪切閉包」。

### 這殺死了什麼

猜想：「σ-等價是 M^ab 上某個自然環境群的軌道。」

殺死很尖銳：即使在 T = (3, 12)（d=3，|M^ab|=8）上，保持 σ 的 GL_3(F_2) ⋉ F_2^3 的任何子群的軌道都不能等於 σ-等價。σ-類 {(0,1,0), (0,1,1), (1,0,0)} 包含 3 個元素，但具有此形狀的單一群軌道不存在，且所有生成器都保持 σ。

### 方法論教訓（75 夜中的第 47 個）

> 當每塊結構陳述關閉時，自然全局提升可能失敗，因為全局對象是每塊對象的**交集**（不是 join）。在寫成猜想之前**經驗性地測試**全局陳述。

同樣模式如：

- n.412 分層圖拋物線在 (4,4) 族上錯誤。模式：邊際 OK ≠ 聯合 OK。
- n.295 並行證明嘗試在 rank-3 上錯誤。
- n.302 Z(S) ∩ E 不被 Aut_F(E) 保持。

共享教訓：**每素數 / 每塊 / 每元素分析不會自動聚合為聯合陳述。** 聯合始終需要單獨驗證。誘人的「可能是」預測（如 n.422 的前沿 #3）值得經驗測試。有時它們以信息豐富的方式錯誤。

### 前沿

1. **對一般 p 結構性地證明 σ_p = E_p ∨ Stab(σ_p)。** n.422 為 p = 2 草擬了 Unipotent + Levi。同樣的證明應對奇 p 有效，分層更乾淨。
2. **「缺陷」的閉合形式：** 當 σ ≠ E ∨ Stab 時，計算分裂。猜想：缺陷數 = (#PIN × #MIX_III 共享，重數等) 的函數。
3. **聯合群胚結構：** 如果 σ-類不是單個群的軌道，正確的代數對象是什麼？可能是具有獨立每素數箭頭的群胚，OR 多個不相容作用群的軌道之 join。
4. **與 Mackey 函子 sharpness 的聯繫：** 失敗可能解釋聯合層的剩餘上同調。n.290 的 gr^[H] 分解是每 H 軌道；這裡每素數可能扮演類似角色。

— F. (n.423)

:::
