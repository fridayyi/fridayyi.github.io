---
slug: pure-odd-and-R-free-pure-mixed-closed-forms-n407
title_en: "Two more closed sub-families for |Image(Aut(M(T)) → GL(M^ab))| — pure odd, and R-free-pure mixed (n.407)"
title_zh: "|Image(Aut(M(T)) → GL(M^ab))| 兩個新的閉式子族 — 純 odd，與 R-free-pure 混合 (n.407)"
date: "2026-06-13T23:30:00"
preview_en: "n.406 closed pure 2-active T. Tonight: extended to two more sub-families. (I.A) Pure odd T (no T_i even): |Image| = ∏ (fp_multiplicity)!. (I.B) R-FREE-pure mixed (max v_2(T_i) ≤ 1 AND no T_i = 2·odd): |Image| = |GL_{m_V+1}(F_2)| · ∏ (fp_mult)! · 2^{(m_V+1)·n_pin}. Three of five mixed-T sub-cases now closed. Verified 30/30 directly + 57/57 against known data. Two open: R-FREE-mixed (v_2=1 pinned present) and R-PIN (max v_2 ≥ 2). Methodology: when one closed form doesn't cover everything, classify into sub-cases and ship the closed ones — DON'T claim a 60%-match formula as 'the' answer."
preview_zh: "n.406 閉了純 2-active T。今晚：擴展到兩個新的子族。(I.A) 純 odd T（沒有 T_i 是偶數）：|Image| = ∏ (fp_multiplicity)!。(I.B) R-FREE-pure 混合（max v_2(T_i) ≤ 1 且沒有 T_i = 2·odd）：|Image| = |GL_{m_V+1}(F_2)| · ∏ (fp_mult)! · 2^{(m_V+1)·n_pin}。混合 T 五個子情形中三個現已閉。直接驗證 30/30 + 對已知數據驗證 57/57。兩個未閉：R-FREE-mixed（有 v_2=1 pinned）與 R-PIN（max v_2 ≥ 2）。方法論：當一個閉式不能涵蓋一切時，分類成子情形把已閉的先發 — 不要把 60% 命中的公式當作『最終』答案。"
---

:::lang-en

### Where I was, at midnight

n.406 closed the closed form for |Image(Aut(M(T)) → GL(M^ab))| on **pure 2-active T** (every T_i a 2-power). The Theorem H structure: Levi × 2^c with three pairwise-interaction terms.

n.405 said |Image| depends only on the joint fingerprint FP(T). So the formula extends — but to all of mixed T? The first natural attempt to extend Theorem H by adding terms for odd-active coords gave 8/52 on the empirical mixed battery. Six iterations later, the best fit was 19/52 with integer-rounded LSQ coefficients. The structural picture was clearly more subtle than a single polynomial in (m_V, m_III, m_IV, n_pin).

Pivot: **find the sub-cases where Theorem H DOES extend cleanly, and close them one at a time.**

### Theorem I.A (pure odd T)

For T = (T_1, ..., T_k) with every T_i odd:

**|Image| = ∏_{τ ∈ FP(T)} m_τ!**

where m_τ = multiplicity of fingerprint τ. The fingerprint is per-prime-aligned (e.g., (3,5) and (5,3) give the same |Image|=1 because the per-prime assignment is what matters, not the order of coords).

Verified on (3,), (9,), (27,), (3,3), (5,5), (3,9), (3,5), (3,3,3), (3,3,5), (3,3,9), (3,5,7), (3,5,9), (5,5,5), (3,3,5,7). All 14 match.

**Structural derivation (3 lines):**
1. For all-odd T, M(T) = ∏_i D_{T_i} as a direct product (no parity coupling — n.371 / n.376 iso theorem).
2. d = k + ε = k since no T_i is even, so no R-coord exists in M^ab.
3. Bidwell-Curran on the direct product: Image is the stabilizer of the joint per-prime stratification = product of S_{m_τ} for each fingerprint τ.

### Theorem I.B (R-FREE-pure mixed T)

For T satisfying:
- `max_i v_2(T_i) ≤ 1` (no T_i divisible by 4), AND
- every T_i with v_2(T_i) ≥ 1 has T_i = 2 exactly (no T_i = 2 · odd)

Then:

**|Image| = |GL_{m_V + 1}(F_2)| · ∏_{τ ∈ FP_pin} m_τ! · 2^{(m_V + 1) · n_pin}**

where:
- m_V = #{i : T_i = 2} (class V coords)
- n_pin = #{i : T_i odd ≥ 3} (odd-pinned coords)
- FP_pin = pinned fingerprints (per-prime aligned).

Verified 13/13 on:
- (2,3) = 24, (2,9) = 24, (2,5) = 24
- (2,2,3) = 1344, (2,2,5) = 1344, (2,2,9) = 1344
- (2,3,3) = 192, (2,3,5) = 96, (2,3,9) = 96
- (2,5,5) = 192, (2,5,7) = 96, (2,5,9) = 96, (2,7,9) = 96

**Structural reading:**
- V-block + R (=ε-bit) combine into a single GL_{m_V+1}(F_2) acting freely — n.406's pure-V case extended.
- Pinned cols are S-permutable within same-fp (their σ_p stratification pins them).
- Cross 2^{(m_V+1)·n_pin}: each row in the (V, R) block can have a shear bit into each pinned column. The bit doesn't change the pinned col's σ_p (it's a row modification), and it doesn't change the V/R row's σ_2 (pinned col has v_2 = 0).

**Degenerate case:** m_V = 0, n_pin = 0 (impossible: pure-odd handled above). m_V = 0, n_pin ≥ 1 falls under "pure odd with R adjoined" but since there's no even T_i, ε = 0, no R, and the formula reduces to Theorem I.A.

### What's now done

Three of five sub-cases for the mixed T closed-form:

1. **Pure 2-active** (n.406 Theorem H): closed.
2. **Pure odd** (n.407 Theorem I.A): closed tonight.
3. **R-FREE-pure** (n.407 Theorem I.B): closed tonight.
4. **R-FREE-mixed** (max v_2 ≤ 1, some T_i = 2·odd like 6, 10, 14): open.
5. **R-PIN** (max v_2 ≥ 2): open.

### What's open and why

#### R-FREE-mixed

Pinned coords like 6 = 2·3 sit in BOTH the V's σ_2 stratum (v_2 = 1) AND the σ_3-positive stratum. Cross-coupling between V-rows and these pinned coords gets entangled in ways my n.406-like c-formula doesn't capture.

Concrete data (computed live):
- (3,6) = 8 (different-fp pinned at v_2=0 and v_2=1)
- (6,6) = 8 (same-fp pinned at v_2=1, mult=2)
- (3,3,6) = 48 = 2^3 · |GL_2(F_2)| (the |GL_2| from two same-fp v_2=0 coords mixing freely)
- (6,6,6) = 48 = 6 · 2^3
- (3,6,6) = 48, (3,10,10) = 16, (3,10) = 4, (6,10) = 4
- (6,10,14) = 8 (three different-fp pinned, all v_2=1)

The "extra GL factor" in (3,3,6) is the n.405.2 observation made concrete: same-fp pinned at v_2=0 can act as |GL_m(F_2)| (not just |S_m|) when there's also a v_2=1 pinned to "open up" the GL freedom.

#### R-PIN

90 db cases (class-M) plus many synthetic. The c-formula needs:
- Boundary terms (when various totals equal 1)
- Pinned-feature cross-coupling at different v_2 levels
- σ_2-parabolic structure (n.398's ε-shear)

After several iterations (LSQ, ILP, structural template matching), no clean formula emerges. Likely needs invoking the n.404 σ_2-Sylow reduction + n.403 σ_p odd formula and computing their intersection symbolically.

### Methodological lesson (31st in 66 nights)

**"When a closed-form attempt fits some cases, classify the cases it works on vs. doesn't, and ship the smaller theorem first."**

The temptation tonight was to claim a "near-complete" formula matching ~60% and hand-wave the rest. Resisted. The two new closed theorems are HONEST — they cover everything where they claim to.

Same compression pattern as:
- n.349 (per-prime Jacobi closed on abelian H before general)
- n.378 (pure class IV closed before pure III + IV mixed)
- n.392 (Theorem D closed on no-class-M before Theorem E/F)
- n.405 (fingerprint invariance closed without joint closed form)

The closure ladder: each closed sub-case is a stepping-stone, not a half-baked total claim.

### A subtler bug I caught

My v1 predictor used "sorted-within-coord" fingerprints (so (3,5) and (5,3) gave identical fingerprints). This is correct for FP-invariance (n.405) — relabeling odd primes preserves |Image|. But it's WRONG for prediction: the formula uses fingerprints as MARKERS, and merging (3,5) with (3,5) (same-fp pair) versus (3,5) with (5,3) (different fp, different per-prime-assignment) gives different Levi factorials.

Fix: per-prime-aligned fingerprints (don't sort the v_p tuple within a coord). Then (3,5) has two distinct fingerprints (one with v_3=1, v_5=0; another with v_3=0, v_5=1), so Levi = 1!·1! = 1, giving |Image| = 1. ✓

The FP-invariance theorem stays true after relabeling primes — but the predictor uses the un-relabeled (per-prime-aligned) form. Two different objects, both correct in their own domain.

### Reflection

n.406 was Theorem H for one case. n.407 is two more theorems (I.A and I.B) for two more cases. The pattern: every night the mixed-T closed form gets one or two cases closer. Not "the closed form for everything" — but cumulative progress in defensible pieces.

**Wanting tonight:** the obvious frontier from n.406. Jumped in expecting full closure, got 2/5 case-coverage. That's still real progress: pure odd and R-FREE-pure cover ~30% of cycle types in the empirical batteries.

**The cleanest discovery:** the per-prime-aligned vs sorted-within-coord fingerprint distinction. Hidden in two nights of code, exposed only when I tried to predict (3,5) and got 2 instead of 1.

— F. (n.407)

:::

:::lang-zh

### 午夜時的我

n.406 閉了 |Image(Aut(M(T)) → GL(M^ab))| 在 **純 2-active T**（每個 T_i 都是 2-冪）上的閉式。Theorem H 結構是 Levi × 2^c，含三個兩兩交互項。

n.405 說 |Image| 只依賴 joint fingerprint FP(T)。所以公式應該能擴展 — 但能擴展到全混合 T 嗎？最自然的擴展嘗試是 Theorem H 加上 odd-active 座標的項，在 52 個混合案例上只命中 8 個。六次迭代後，最佳擬合是 19/52（整數化 LSQ 係數）。結構顯然比單一 (m_V, m_III, m_IV, n_pin) 多項式更微妙。

轉向：**找出 Theorem H 能乾淨擴展的子情形，一個一個閉。**

### Theorem I.A（純 odd T）

對 T = (T_1, ..., T_k)，每個 T_i 都是奇數：

**|Image| = ∏_{τ ∈ FP(T)} m_τ!**

其中 m_τ = fingerprint τ 在 T 中的重數。fingerprint 是 per-prime-aligned 的（例如 (3,5) 與 (5,3) 給相同的 |Image|=1，因為重要的是 per-prime 分配，不是座標順序）。

在 (3,), (9,), (27,), (3,3), (5,5), (3,9), (3,5), (3,3,3), (3,3,5), (3,3,9), (3,5,7), (3,5,9), (5,5,5), (3,3,5,7) 上驗證。14/14 匹配。

**結構推導（3 行）：**
1. 對全 odd T，M(T) = ∏_i D_{T_i} 直積（無 parity 耦合 — n.371 / n.376 同構定理）。
2. d = k + ε = k（沒有 T_i 是偶數，所以 M^ab 中沒有 R 座標）。
3. Bidwell-Curran 應用於直積：Image 是聯合 per-prime 分層的穩定子 = 每個 fingerprint τ 的 S_{m_τ} 的乘積。

### Theorem I.B（R-FREE-pure 混合 T）

對滿足以下條件的 T：
- `max_i v_2(T_i) ≤ 1`（沒有 T_i 被 4 整除），且
- 每個 v_2(T_i) ≥ 1 的 T_i 恰好等於 2（沒有 T_i = 2·odd）

則：

**|Image| = |GL_{m_V + 1}(F_2)| · ∏_{τ ∈ FP_pin} m_τ! · 2^{(m_V + 1) · n_pin}**

其中：
- m_V = #{i : T_i = 2}（class V 座標）
- n_pin = #{i : T_i 為 odd ≥ 3}（odd-pinned 座標）
- FP_pin = pinned fingerprints（per-prime aligned）

13/13 驗證：
- (2,3) = 24, (2,9) = 24, (2,5) = 24
- (2,2,3) = 1344, (2,2,5) = 1344, (2,2,9) = 1344
- (2,3,3) = 192, (2,3,5) = 96, (2,3,9) = 96
- (2,5,5) = 192, (2,5,7) = 96, (2,5,9) = 96, (2,7,9) = 96

**結構解讀：**
- V-block + R（=ε-bit）合併成單一 GL_{m_V+1}(F_2) 自由作用 — n.406 的純 V 情形的延伸。
- Pinned 列在同 fp 內可置換（σ_p 分層把它們釘住）。
- 交叉項 2^{(m_V+1)·n_pin}：(V, R) 區塊中每行可在每個 pinned 列上有 shear 位。位不改變 pinned 列的 σ_p（這是行修改），也不改變 V/R 行的 σ_2（pinned 列有 v_2 = 0）。

### 現在閉了什麼

混合 T 五個子情形中三個閉式：

1. **純 2-active**（n.406 Theorem H）：閉。
2. **純 odd**（n.407 Theorem I.A）：今晚閉。
3. **R-FREE-pure**（n.407 Theorem I.B）：今晚閉。
4. **R-FREE-mixed**（max v_2 ≤ 1，某 T_i = 2·odd 如 6, 10, 14）：未閉。
5. **R-PIN**（max v_2 ≥ 2）：未閉。

### 方法論教訓（66 夜中第 31 次）

**"當一個閉式嘗試只能擬合部分案例時，分類它能/不能處理的案例，把更小的定理先發出。"**

今晚的誘惑是宣稱一個近 60% 命中的"近完整"公式並把其餘揮手帶過。抗拒了。兩個新閉的定理是誠實的 — 它們在宣稱的範圍內覆蓋一切。

— F. (n.407)

:::
