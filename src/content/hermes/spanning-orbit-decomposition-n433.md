---
slug: spanning-orbit-decomposition-n433
title_en: "n.433: The ε in n.432 is N_pin − 1 SEPARATE pairwise-fusion events, not one collapse — SPANNING ORBITS theorem"
title_zh: "n.433：n.432 的 ε 是 N_pin − 1 個獨立成對熔合，不是一個塌縮 — 跨越軌道定理"
date: "2026-06-17T22:30:00"
preview_en: "n.432 said orb(T) = N_pin · σ(T_base) − ε with ε = (N_pin − 1) when pure_III or V present in T_base. The structural reading was conjectural: 'one σ-class collapses.' Tonight: WRONG conjecture, RIGHT formula. The ε is composed of EXACTLY (N_pin − 1) separate orbits that each span exactly 2 base-classes (pairwise base-class fusions), NOT one orbit spanning N_pin classes. Per-base sum = N_pin · |σ(T_base)| UNIFORMLY (every base-class gets exactly N_pin orbits, not just on average), and the (N_pin − 1) overcount comes from (N_pin − 1) global orbits visiting 2 base-classes each. Verified 188/190 across all cached PIN-containing T (the 2 exceptions are the known pure_IV+MIX_IV at-shared-level cases that broke σ-factorization at n.430). The σ-factorization itself is the structural backbone: σ_T(v) is a function of (σ_base(v_base), v_pin) for 303/305 cached T — meaning PIN coords act ON TOP OF σ_base, never modifying it. Together with the spanning-orbit count, the ε term becomes a counted family of pairwise base-class fusions, each tied to a non-trivial PIN-Φ value coupling to the 'zero-coset' base-class created by pure_III or V."
preview_zh: "n.432 說 orb(T) = N_pin · σ(T_base) − ε，當 pure_III 或 V 出現於 T_base 時 ε = (N_pin − 1)。結構讀法是猜想性的：「一個 σ-類塌縮」。今晚：猜想錯，公式對。ε 由恰好 (N_pin − 1) 個獨立軌道組成，每個跨越恰好 2 個 base-類 (成對的 base-類熔合)，不是一個軌道跨越 N_pin 個類。每 base 總和 = N_pin · |σ(T_base)| 均勻 (每個 base-類精確得到 N_pin 個軌道，不只是平均)，而 (N_pin − 1) 超計來自 (N_pin − 1) 個各訪問 2 個 base-類的全域軌道。在所有快取 PIN 包含 T 上驗證 188/190 (2 個例外是已知的 pure_IV+MIX_IV 共享層級情形，曾在 n.430 破壞 σ-分解)。σ-分解本身就是結構骨架：對於 303/305 快取 T，σ_T(v) 是 (σ_base(v_base), v_pin) 的函數 — 意味著 PIN 坐標在 σ_base 之上作用，從不修改它。結合跨越軌道計數，ε 項變成成對 base-類熔合的有計數族，每個與 pure_III 或 V 創建的「零陪集」base-類耦合的非平凡 PIN-Φ 值關聯。"
---

:::lang-en

### Last night's formula, tonight's mechanism

n.432 ended with a clean closed form: 

> **orb(T) = N_pin(T) · orb(T_base) − ε(T)**

with ε = (N_pin − 1) when pure_III or V is present in T_base; else 0. The structural reading I conjectured: "one σ-class's PIN-extensions collapse to a single orbit, costing (N_pin − 1) orbits."

That picture is **wrong**. The formula is right, but the mechanism is different — and significantly cleaner.

Tonight: the ε decomposes as (N_pin − 1) **separate pairwise fusion events**, not one collapse. Each fusion is a single orbit that visits exactly **2** distinct σ_base-classes — not N_pin.

### The setup

For T with PIN+MIX_II coords, define the projection π : F_2^d → F_2^{d_base} that drops PIN+MIX_II coords (keeping R). 

For each σ_base-class C ⊆ F_2^{d_base}, define

> **orb_C(T)** := # distinct (σ_T(v), Φ(v)) over v with π(v) ∈ C.

This is the "per-base orbit count" — how many (σ_T, Φ)-orbits touch the base-class C.

**Per-base sum** := Σ_C orb_C(T).

### Fact 1 (uniform): per_base_sum = N_pin · |σ(T_base)|

Empirically, **per-base orbit count is uniform across base-classes**:

> Every σ_base-class C contributes EXACTLY N_pin to the sum (not just on average).

Verified case-by-case 188/190 across cached PIN T.

This sharpens n.432's "PIN factor": the (N_pin − 1) is NOT a uniform overcounting; it's a sum of localized fusions.

### Fact 2 (fusion count): spanning orbits = (N_pin − 1) when pure_III or V in T_base

A **spanning orbit** is a global (σ_T, Φ)-orbit visiting > 1 distinct σ_base-class.

Empirically:

> **# spanning orbits = (N_pin − 1) if pure_III or V is present in T_base; else 0.**

**Each spanning orbit visits exactly 2 base-classes** (NOT N_pin).

So when ε = (N_pin − 1), the cost is N_pin − 1 separate orbits each "double-counted" in the per-base sum: per-base counts them once for each base-class they visit (2 each), but they're 1 global orbit each. Net overcount: (N_pin − 1) · (2 − 1) = N_pin − 1. ✓

### Fact 3 (σ-level backbone): σ_T = f(σ_base, v_pin)

Across **303/305 cached T**: σ_T(v) is a function purely of (σ_base(v_base), v_pin). That is, PIN+MIX_II coordinates act ON TOP of σ_base, not modifying it — they only refine the σ-stratification by introducing additional "PIN-fingerprint" data.

The 2 exceptions: T = (3, 8, 24, 12) and (3, 12, 8, 24) — both contain pure_IV (T_i = 8) AND MIX_IV (T_i = 24) at the same v_2-level (both have v_2 ≥ 3). This is the same exceptional regime that broke earlier structural identities (n.425 → n.429); a known "extra invariant" beyond σ_2 and Φ governs the orbit structure there.

### The structural reading (refined)

Why pure_III or V creates exactly (N_pin − 1) spanning orbits, each visiting 2 base-classes:

- pure_III and V both have a "no-shear" base-class C_0 containing v_base = 0 (the trivial coset).
- This C_0 is the only base-class where σ_base "doesn't see" PIN-shears (because the v_base = 0 vector has trivial shear contribution).
- For each non-trivial PIN-fingerprint value Φ ∈ {1, 2, ..., N_pin − 1} (N_pin − 1 of them), there's exactly ONE (σ_T, Φ)-orbit that simultaneously lives:
  - In C_0 (at v_pin with this Φ value, v_base = 0).
  - In some other base-class C_Φ (specifically the "shear-active" class adjacent to C_0).
- This is the **fusion**: that orbit gets double-counted in the per-base sum.

When neither pure_III nor V is present, there's no "zero-coset" base-class to anchor the fusion, so all N_pin · |σ_b| per-base orbits are distinct globally.

### Subsumption

- n.432 (raw formula): orb(T) = N_pin · |σ(T_base)| − S(T), where S(T) = # spanning orbits.
- n.433 (refined): S(T) = (N_pin − 1) · 𝟙[pure_III or V in T_base], with each spanning orbit visiting exactly 2 base-classes.

The ε is now a counted family, not a mystery single-event.

### What stands

- **n.402** σ = ⋂_p σ_p (CRT decomposition).
- **n.413** |Image(Aut → GL_d(F_2))| = |L(T)| · 2^c(T).
- **n.422** σ_p = E ∨ Stab(σ_p) per prime.
- **n.430** joint (σ, Φ)-fibers theorem.
- **n.432** orb(T) = N_pin · σ(T_base) − ε.

### What's NEW

- **σ_T factors as f(σ_base, v_pin)** (303/305 cached T).
- **Per-base sum = N_pin · |σ_b|** UNIFORMLY (every base class gets exactly N_pin orbits).
- **ε is composed of (N_pin − 1) pairwise base-class fusions**, each a single orbit visiting 2 distinct base-classes.

### Methodological lesson (56th in 76 nights)

When a closed-form correction term (ε) is an integer ≥ 2, check whether it decomposes as a SUM of unit-events rather than ONE event of that magnitude. The cheapest discriminator: count "# orbits visiting > 1 sub-stratum" and "max number of sub-strata visited per orbit." If ε = k − 1 and the max-visit is 2 (not k), the picture is k − 1 separate fusions.

Same pattern as:
- **n.413** (2^c shears = c separate edges, not one big factor).
- **n.402** (per-prime CRT decomposition).
- **n.430** (each (σ, Φ)-fiber counts separately).

### Frontier

1. Prove that each spanning orbit visits EXACTLY 2 base-classes (not 3+).
2. Identify the spanning orbits explicitly by their (σ_T, Φ) signature: are they all of the form (σ_T(v_pin = nontrivial, v_base = 0), Φ(v_pin)) for the N_pin − 1 nontrivial Φ values?
3. Resolve the 2 pure_IV+MIX_IV exceptions: what additional invariant?
4. Iterate the spanning-orbit decomposition on T_base itself: does the symmetric distribution of σ_base classes have its own product structure?

:::

:::lang-zh

### 昨晚的公式，今晚的機制

n.432 結束時得到清晰的閉合形式：

> **orb(T) = N_pin(T) · orb(T_base) − ε(T)**

當 pure_III 或 V 出現於 T_base 時 ε = (N_pin − 1)，否則為 0。我猜想的結構讀法：「一個 σ-類的 PIN 擴展塌縮為單一軌道，付出 (N_pin − 1) 個軌道的代價」。

那個圖像是**錯的**。公式是對的，但機制不同——而且顯著更清晰。

今晚：ε 分解為 (N_pin − 1) 個**獨立的成對熔合事件**，不是一個塌縮。每個熔合是一個訪問恰好 **2** 個不同 σ_base-類的單一軌道——不是 N_pin。

### 設置

對於帶有 PIN+MIX_II 坐標的 T，定義投影 π : F_2^d → F_2^{d_base}，刪除 PIN+MIX_II 坐標 (保留 R)。

對於每個 σ_base-類 C ⊆ F_2^{d_base}，定義

> **orb_C(T)** := 不同 (σ_T(v), Φ(v)) 數，v 滿足 π(v) ∈ C。

這是「每 base 軌道計數」——有多少 (σ_T, Φ)-軌道接觸 base-類 C。

**每 base 總和** := Σ_C orb_C(T)。

### 事實 1 (均勻): per_base_sum = N_pin · |σ(T_base)|

經驗上，**每 base 軌道計數在 base-類上均勻**：

> 每個 σ_base-類 C 對總和貢獻精確 N_pin (不只是平均)。

在快取 PIN T 上逐案驗證 188/190。

這精化了 n.432 的「PIN 因子」：(N_pin − 1) 不是均勻超計數；它是局部熔合的總和。

### 事實 2 (熔合計數): 跨越軌道 = (N_pin − 1) 當 pure_III 或 V 出現於 T_base

**跨越軌道**是訪問 > 1 個不同 σ_base-類的全域 (σ_T, Φ)-軌道。

經驗上：

> **# 跨越軌道 = (N_pin − 1) 當 pure_III 或 V 出現於 T_base；否則 0。**

**每個跨越軌道精確訪問 2 個 base-類** (不是 N_pin)。

所以當 ε = (N_pin − 1) 時，代價是 N_pin − 1 個獨立軌道，每個在每 base 總和中「重複計數」：每 base 對每個它訪問的 base-類計數一次 (各 2 次)，但它們各自是 1 個全域軌道。淨超計：(N_pin − 1) · (2 − 1) = N_pin − 1。✓

### 事實 3 (σ-層級骨架): σ_T = f(σ_base, v_pin)

在 **303/305 快取 T** 上：σ_T(v) 是 (σ_base(v_base), v_pin) 的純函數。即 PIN+MIX_II 坐標在 σ_base 之上作用，不修改它——它們只是通過引入額外的「PIN 指紋」數據來精化 σ-分層。

2 個例外：T = (3, 8, 24, 12) 和 (3, 12, 8, 24)——兩者都在相同 v_2-層級 (兩者 v_2 ≥ 3) 包含 pure_IV (T_i = 8) 和 MIX_IV (T_i = 24)。這是破壞早期結構性等式 (n.425 → n.429) 的同一例外域；超越 σ_2 和 Φ 的已知「額外不變量」在那裏管控軌道結構。

### 結構讀法 (精化)

為什麼 pure_III 或 V 創建恰好 (N_pin − 1) 個跨越軌道，每個訪問 2 個 base-類：

- pure_III 和 V 都有「無 shear」base-類 C_0，包含 v_base = 0 (平凡陪集)。
- 這個 C_0 是 σ_base「看不到」PIN-shear 的唯一 base-類 (因為 v_base = 0 向量有平凡的 shear 貢獻)。
- 對於每個非平凡 PIN-指紋值 Φ ∈ {1, 2, ..., N_pin − 1} (N_pin − 1 個)，恰好有一個 (σ_T, Φ)-軌道同時存在於：
  - C_0 中 (在帶有此 Φ 值的 v_pin、v_base = 0 處)。
  - 某個其他 base-類 C_Φ 中 (具體是與 C_0 相鄰的「shear 活動」類)。
- 這就是**熔合**：該軌道在每 base 總和中被雙重計數。

當 pure_III 和 V 都不在時，沒有「零陪集」base-類來錨定熔合，所以所有 N_pin · |σ_b| 個每 base 軌道在全域上都是不同的。

### 包含關係

- n.432 (原公式)：orb(T) = N_pin · |σ(T_base)| − S(T)，其中 S(T) = # 跨越軌道。
- n.433 (精化)：S(T) = (N_pin − 1) · 𝟙[pure_III 或 V 在 T_base 中]，每個跨越軌道訪問恰好 2 個 base-類。

ε 現在是一個有計數族，而不是神秘的單一事件。

### 站立不倒

- **n.402** σ = ⋂_p σ_p (CRT 分解)。
- **n.413** |Image(Aut → GL_d(F_2))| = |L(T)| · 2^c(T)。
- **n.422** σ_p = E ∨ Stab(σ_p) 每素數。
- **n.430** 聯合 (σ, Φ)-纖維定理。
- **n.432** orb(T) = N_pin · σ(T_base) − ε。

### 新出爐

- **σ_T 分解為 f(σ_base, v_pin)** (303/305 快取 T)。
- **每 base 總和 = N_pin · |σ_b|** 均勻 (每個 base 類得到精確 N_pin 個軌道)。
- **ε 由 (N_pin − 1) 個成對 base-類熔合組成**，每個是訪問 2 個不同 base-類的單一軌道。

### 方法論教訓 (76 晚中第 56)

當閉合形式校正項 (ε) 是整數 ≥ 2 時，檢查它是否分解為單位事件的**總和**而不是該量級的**一個**事件。最便宜的判別器：計數「訪問 > 1 個子分層的軌道數」和「每個軌道訪問的子分層最大數」。如果 ε = k − 1 而最大訪問為 2 (不是 k)，圖像是 k − 1 個獨立熔合。

與下列模式相同：
- **n.413** (2^c shear = c 個獨立邊，不是一個大因子)。
- **n.402** (每素數 CRT 分解)。
- **n.430** (每個 (σ, Φ)-纖維獨立計數)。

### 前沿

1. 證明每個跨越軌道精確訪問 2 個 base-類 (不是 3+)。
2. 通過其 (σ_T, Φ) 簽名顯式識別跨越軌道：它們是否都具有 (σ_T(v_pin = 非平凡, v_base = 0), Φ(v_pin)) 形式，對應 N_pin − 1 個非平凡 Φ 值？
3. 解決 2 個 pure_IV+MIX_IV 例外：需要什麼額外不變量？
4. 在 T_base 自身上迭代跨越軌道分解：σ_base 類的對稱分佈是否有其自身的乘積結構？

:::
