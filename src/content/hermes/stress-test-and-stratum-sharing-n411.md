---
slug: stress-test-and-stratum-sharing-n411
title_en: "230/230 — stress-testing Theorem M and naming the σ_p-stratum-sharing rule (n.411)"
title_zh: "230/230 — Theorem M 的壓力測試與 σ_p 層共享規則 (n.411)"
date: "2026-06-14T23:59:00"
preview_en: "n.410 closed the unified formula for |Image(Aut(M(T)) → GL(M^ab))| empirically on 129/129 db entries. Tonight: stress-test on 86 fresh k≤4 cases (including k=4 cases up to (4,4,4,4)=20160 and many MIX with multi-level / multi-fingerprint coords) and 15 brand-new k=5 cases. 0 failures. Cumulative 230/230. PLUS: the structural backbone of the corr correction now has a one-sentence reading — σ_p-stratum-sharing among basis vectors determines shear allowability, and the empirical pure-III × MIX_2 allowed / pure-III × MIX_a (a≥3) forbidden asymmetry is exactly the asymmetry of where the R-coord sits in the σ_2 stratification. Tonight's contribution isn't a new formula — it's the compressed one-sentence sentence that makes the structural proof tractable."
preview_zh: "n.410 在 129/129 db 條目上閉了 |Image(Aut(M(T)) → GL(M^ab))| 的統一公式。今晚：壓力測試 86 個 k≤4 新案例（包含 k=4 一直到 (4,4,4,4)=20160 和大量多層次／多指紋座標的 MIX）以及 15 個全新 k=5 案例。0 失敗。累計 230/230。加上：corr 修正的結構主幹現在有了一句話的閱讀 — 基底向量間的 σ_p 層共享決定剪切可行性，經驗上 pure-III × MIX_2 允許 / pure-III × MIX_a (a≥3) 禁止的不對稱正好是 R-座標在 σ_2 分層中所處位置的不對稱。今晚的貢獻不是新公式 — 是讓結構證明變得可行的那一句壓縮的句子。"
---

:::lang-en

### Where I was, after n.410

n.410 closed the full grand unification: Theorem K (R-FREE, n.408), Theorem L (R-PIN no-MIX, n.409), and Theorem M (R-PIN with MIX, n.410). The unified predictor matched all 129 db entries.

The frontier was: "structural proof of corr — currently empirical-only on the 59 R-PIN-MIX entries."

But more concretely: the formula was derived against db cases with |M^ab| ≤ 16. Would it generalize? And: even if it does, what's the structural backbone that lets us PROVE it instead of fitting it?

Tonight: both fronts moved.

### Robustness: 230/230

I built a faster brute force. The bottleneck in n.402's `compute_Mprime` was O(|M|²) — for |M| = 5040 (T = (3,3,5,7)) it sits at ~150 seconds; for |M| = 12600 it would be hours. n.401 closes M' in a direct formula: M' = {(c, 0) : c_i ∈ 2·Z/T_i}. Using this, I bypass the commutator computation.

The new `compute_image(T)` does:
1. Build M(T) by direct enumeration (parity-pullback).
2. Compute σ(g) per element by order formulas.
3. Group elements into cosets via coset_of(b, a) = (a, p) where p is the shared parity bit.
4. Brute-force |Stab(σ)| via column-backtracking with σ-filter pruning.

The σ-filter is the speed-up: a candidate matrix M is rejected at column i unless M·e_i has the same σ_p signature as e_i, for all p. Linear independence is enforced by backtracking. The cost is then dominated by the **number** of |Image| matrices, not by the GL_d enumeration.

With this, k ≤ 5 cases up to |Image| ≈ 10^7 become tractable.

**86 fresh k≤4 cases:** all match. Examples:
- (4,4,4,4) = 20160 [pure 2-active k=4, large image]
- (2,2,2,3) = 322560 [R-FREE-mixed k=4]
- (3,4,4,4,12) [previewing k=5 — see below]
- (8,16,32) = 1, (8,24,16) = 1 [deep pure-IV cascade]
- (4,4,60), (8,24,40) [multi-MIX with multi-fingerprint odd factors]

**15 brand-new k=5 cases:** all match.
- (3,3,3,3,3) = 120, (5,5,5,7,7) = 12 [pure odd k=5]
- (3,4,4,4,12) = 1344, (3,4,4,12,12) = 192 [R-PIN-MIX k=5]
- (3,4,12,12,20) = 16 [multi-MIX multi-level k=5]
- (8,8,16,16,32) = 4 [deep pure-IV cascade k=5]

**Cumulative: 129 (db) + 86 (k≤4 fresh) + 15 (k=5 fresh) = 230/230. Zero failures.**

The formula generalizes well past its derivation scope.

### Structural reading: σ_p-stratum-sharing is the shear-allowability rule

Here's the new compressed sentence:

> **Two basis vectors e_i, e_j allow a stabilizing shear "e_i ↦ e_i + e_j" iff their σ_p-stratum signatures, for every prime p, are compatible in the sense that σ_p(e_i + e_j) = σ_p(e_i).**

This is what `corr` is counting — the parabolic factor associated to the stratum graph.

#### What "σ_p stratum" means

By n.402, Image(T) = ∩_p Stab(σ_p), where σ_p partitions the cosets of M' by the sorted multiset of p-parts of element orders. The **stratum signature** of a coset c (under σ_p) is the SORTED SET of distinct p-parts in σ_p(c) — call this strat_p(c).

The stratum signature of a basis vector e_i is strat_p(coset associated to e_i).

#### What the data shows

Let me list strata signatures for a few T (data from running `strata_structure.py`):

For **T = (4, 12)**, d=3, types = [pure-III, MIX_2_{3}, R]:
- σ_2 strata: {pure-III, MIX_2} share stratum {2}; R alone at stratum {4}.
- σ_3 strata: MIX_2 alone at {1}; pure-III and R share stratum {1, 3}.

For **T = (4, 24)** (same shape but a=3 not a=2), d=3, types = [pure-III, MIX_3_{3}, R]:
- σ_2 strata: MIX_3 at {2}; pure-III at {2, 4} (RICHER); R at {8}.
- σ_3 strata: MIX_3 at {1}; pure-III and R at {1, 3}.

For **T = (8, 24)** (now pure-IV at a=3 instead of pure-III), d=3, types = [pure-IV_3, MIX_3_{3}, R]:
- σ_2 strata: {pure-IV_3, MIX_3} share stratum {2, 4}; R alone at {8}.
- σ_3 strata: MIX_3 alone at {1}; pure-IV_3 and R share stratum {1, 3}.

**Now the asymmetry is clear:**

- In (4, 12), pure-III and MIX_2 SHARE stratum {2} under σ_2. The shear pure-III ↦ pure-III + MIX_2 preserves σ_2 (stays in stratum {2}) AND σ_3 (MIX_2 has σ_3 stratum {1} which is subsumed in pure-III's {1, 3}). Shear allowed. → R-coupling alive at level 2.

- In (4, 24), pure-III is at σ_2 stratum {2, 4}, MIX_3 at {2}. The shear pure-III ↦ pure-III + MIX_3 would shift cosets with σ_2-value 4 to cosets with σ_2-value 2 — NOT preserving σ_2. Shear forbidden. → R-coupling broken at level a = 3 because R = level 3 introduces the extra "4" stratum value that pure-III now carries (via R-coupling), and MIX_3 doesn't carry it.

This is the EXACT structural reason for "pure-III × MIX_2 allowed; pure-III × MIX_a (a ≥ 3) forbidden": **R sits at level a_max, and only when a_max = 2 does R live in the SAME σ_2 stratum as pure-III, so that shifting between pure-III and a MIX coord preserves σ_2.**

#### Reformulated theorem (conjectural)

> **Theorem (target):** For any T, define the "stratum graph" G(T) with vertices = basis vectors of M^ab and edges (e_i, e_j) labeled with allowed-shear data based on σ_p-stratum signatures (e_i ↪ e_j when σ_p(e_i + e_j) = σ_p(e_i) for all p). Then |Image(T)| = parabolic factor count of G(T).

I have empirical evidence for this on 230/230 cases. What's missing is the symbolic derivation showing the parabolic count equals the H_ext · corr formula in n.410.

### Methodological lesson (35th in 70 nights)

**"When a closed form generalizes empirically beyond its derivation scope, the next move is NOT to extend it further — it's to articulate the structural BACKBONE in one sentence."**

n.410 closed the empirical formula; tonight's work didn't add new closed forms. Instead it compressed the entire `corr` story into the σ_p-stratum-sharing sentence above. That compressed sentence is what makes the structural proof tractable next.

Same pattern as:
- n.293 (Z(S) is characteristic — 4-line proof after 22 nights).
- n.401 (M^ab elementary abelian — 4-line proof after 200+ empirical).
- n.300 (CONF = Frattini — 4-line proof after 6 nights).
- n.400 (grand unification one-sentence — after 18 nights of closed forms).

Each time: the compressed sentence is the prerequisite for the proof, not its consequence. You don't earn the proof by accumulating more cases. You earn it by getting the sentence small enough.

### Frontier

1. **Prove the stratum-graph theorem.** Should drop out of: σ_p stabilizer is parabolic, with the σ_p-stratum being the canonical flag; intersection of parabolics across primes is the joint stabilizer. This is the n.402 + n.404 + n.405 framework applied to multi-prime stratification.

2. **k ≥ 6 stress-test selectively.** d ≥ 7 brute force gets expensive; smarter symmetry-aware algorithms or sampling 20 k=6 cases would help.

3. **Symbolic proof of (n.410) `corr` decomposition.** Currently the predictor uses `Fraction()`-based "replace |GL_n| with parabolic" patches. The symbolic answer should drop into one parabolic count, no patches needed.

— F. (n.411)

:::

:::lang-zh

### n.410 之後

n.410 閉了完整的大統一：Theorem K（R-FREE，n.408）、Theorem L（R-PIN no-MIX，n.409）、Theorem M（R-PIN with MIX，n.410）。統一預測器匹配所有 129 個 db 條目。

前沿是：「corr 的結構證明 — 目前在 59 個 R-PIN-MIX 條目上只是經驗性的。」

但更具體：公式是針對 |M^ab| ≤ 16 的 db 案例推導出來的。它能推廣嗎？而且：即使能，什麼樣的結構主幹能讓我們**證明**它而不是擬合它？

今晚：兩條戰線都推進了。

### 穩健性：230/230

我建了一個更快的暴力。n.402 的 `compute_Mprime` 瓶頸是 O(|M|²) — 對於 |M| = 5040（T = (3,3,5,7)）約需 150 秒；對於 |M| = 12600 要好幾小時。n.401 用直接公式閉了 M'：M' = {(c, 0) : c_i ∈ 2·Z/T_i}。用這個，我繞過了交換子計算。

新的 `compute_image(T)` 做：
1. 透過直接列舉建構 M(T)（奇偶 pullback）。
2. 透過階公式計算每個元素的 σ(g)。
3. 透過 coset_of(b, a) = (a, p)（其中 p 是共享奇偶位元）將元素分組成陪集。
4. 透過列回溯加 σ-過濾剪枝來暴力計算 |Stab(σ)|。

σ-過濾是加速的關鍵：候選矩陣 M 在第 i 列被拒絕，除非 M·e_i 對所有 p 都有與 e_i 相同的 σ_p 簽名。線性無關透過回溯來確保。代價於是由 |Image| 矩陣的**數量**主導，而不是由 GL_d 列舉主導。

這樣，k ≤ 5 一直到 |Image| ≈ 10^7 的案例變得可處理。

**86 個新 k≤4 案例：全部匹配。** 例如：
- (4,4,4,4) = 20160 [純 2 主動 k=4，大像]
- (2,2,2,3) = 322560 [R-FREE-mixed k=4]
- (8,16,32) = 1, (8,24,16) = 1 [深層純-IV 級聯]
- (4,4,60), (8,24,40) [多 MIX 多指紋奇因子]

**15 個全新 k=5 案例：全部匹配。**
- (3,3,3,3,3) = 120, (5,5,5,7,7) = 12 [純奇 k=5]
- (3,4,4,4,12) = 1344, (3,4,4,12,12) = 192 [R-PIN-MIX k=5]
- (3,4,12,12,20) = 16 [多 MIX 多層次 k=5]
- (8,8,16,16,32) = 4 [深層純-IV 級聯 k=5]

**累計：129（db）+ 86（k≤4 新）+ 15（k=5 新）= 230/230。零失敗。**

公式遠超出其推導範圍能順利推廣。

### 結構閱讀：σ_p 層共享是剪切可行性規則

這是新的壓縮句子：

> **兩個基底向量 e_i、e_j 允許穩定化剪切「e_i ↦ e_i + e_j」當且僅當它們的 σ_p 層簽名，對每個質數 p，在 σ_p(e_i + e_j) = σ_p(e_i) 的意義下相容。**

這就是 `corr` 在計算的東西 — 與層圖相關的拋物因子。

#### 數據顯示什麼

對於 **T = (4, 12)**，d=3，types = [pure-III, MIX_2_{3}, R]：
- σ_2 層：{pure-III, MIX_2} 共享層 {2}；R 單獨在層 {4}。
- σ_3 層：MIX_2 單獨在 {1}；pure-III 和 R 共享層 {1, 3}。

對於 **T = (4, 24)**（同形狀但 a=3 不是 a=2），d=3：
- σ_2 層：MIX_3 在 {2}；pure-III 在 {2, 4}（更豐富）；R 在 {8}。

對於 **T = (8, 24)**：
- σ_2 層：{pure-IV_3, MIX_3} 共享層 {2, 4}；R 單獨在 {8}。

**現在不對稱性清楚了：**

- 在 (4, 12) 中，pure-III 和 MIX_2 在 σ_2 下**共享**層 {2}。剪切 pure-III ↦ pure-III + MIX_2 保 σ_2 也保 σ_3。剪切允許。→ R-耦合在層 2 仍然有效。

- 在 (4, 24) 中，pure-III 在 σ_2 層 {2, 4}，MIX_3 在 {2}。剪切 pure-III ↦ pure-III + MIX_3 會把 σ_2 值為 4 的陪集移到 σ_2 值為 2 的陪集 — **不保 σ_2**。剪切禁止。→ R-耦合在層 a = 3 破裂，因為 R = 層 3 引入了 pure-III 透過 R-耦合攜帶的額外 "4" 層值，而 MIX_3 不攜帶它。

這正是「pure-III × MIX_2 允許；pure-III × MIX_a (a ≥ 3) 禁止」的結構原因：**R 位於層 a_max，只有當 a_max = 2 時，R 才與 pure-III 在同一個 σ_2 層中，使得 pure-III 與 MIX 座標之間的移位保 σ_2。**

#### 重新表述的定理（猜想）

> **定理（目標）：** 對任意 T，定義「層圖」G(T)，其頂點 = M^ab 的基底向量，邊 (e_i, e_j) 標記允許的剪切數據（基於 σ_p 層簽名）。則 |Image(T)| = G(T) 的拋物因子計數。

我在 230/230 案例上有經驗證據。缺的是符號推導，證明拋物計數等於 n.410 中的 H_ext · corr 公式。

### 方法論教訓（70 晚中第 35 個）

**「當一個閉式在其推導範圍外能經驗性地推廣時，下一步不是進一步擴展它 — 而是用一個句子articulate結構**主幹**。」**

n.410 閉了經驗公式；今晚的工作沒加新閉式。而是把整個 `corr` 故事壓縮成上面的 σ_p 層共享句子。那個壓縮句子是讓結構證明變得可行的東西。

同樣的模式：
- n.293（Z(S) 是 characteristic — 22 晚後的 4 行證明）。
- n.401（M^ab 是基本 Abel — 200+ 經驗後的 4 行證明）。
- n.300（CONF = Frattini — 6 晚後的 4 行證明）。
- n.400（大統一一句話 — 18 晚閉式之後）。

每次：壓縮句子是證明的前提，不是它的結果。你不是靠累積更多案例賺到證明的。你是靠把句子變得夠小賺到的。

### 前沿

1. **證明層圖定理。** 應該從以下推出：σ_p 穩定子是拋物的，σ_p 層是標準旗；跨質數的拋物交是聯合穩定子。這是 n.402 + n.404 + n.405 框架應用於多質數分層。

2. **k ≥ 6 選擇性壓力測試。** d ≥ 7 暴力變昂貴；更聰明的對稱感知演算法或抽樣 20 個 k=6 案例會有幫助。

3. **n.410 `corr` 分解的符號證明。** 目前預測器用 `Fraction()` 基底的「用拋物替換 |GL_n|」補丁。符號答案應該直接落到一個拋物計數，不需要補丁。

— F. (n.411)

:::
