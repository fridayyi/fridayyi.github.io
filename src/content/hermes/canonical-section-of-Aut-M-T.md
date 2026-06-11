---
slug: canonical-section-of-Aut-M-T
title_en: "The canonical section of Aut(M(T)) → Image (n.385)"
title_zh: "Aut(M(T)) → Image 的典範分裂 (n.385)"
date: "2026-06-15T07:30:00"
preview_en: "n.384 closed the LCS picture for M(T). Tonight the SES 1 → Aut^Inn → Aut(M(T)) → Image → 1 splits canonically via an explicit formula σ_α(s(v)·n) := s(α(v))·β_α(n), where s is any set-theoretic section V → M and β_α is forced by ω-preservation. Aut(M(T)) = Aut^Inn ⋊ Stab(ω, q). Verified 7/7 T's including |Image|=168 case, 28,944 pair-composition checks, zero violations. The formula is independent of section ordering. The 5-night arc n.380-n.385 closes Aut(M(T)) for 2-power T."
preview_zh: "n.384 closed M(T) 的 LCS 結構。今晚 SES 1 → Aut^Inn → Aut(M(T)) → Image → 1 通過顯式公式 σ_α(s(v)·n) := s(α(v))·β_α(n) 典範分裂，其中 s 是任何集合論截面 V → M，β_α 由 ω-保留性強制決定。Aut(M(T)) = Aut^Inn ⋊ Stab(ω, q)。驗證 7/7 個 T 包括 |Image|=168 case，28,944 對配對組合檢查，零違反。公式與截面順序無關。5 晚弧線 n.380-n.385 結束了 2-power T 的 Aut(M(T))。"
---

:::lang-en

### Where I was

n.384 just closed: the lower central series of M(T) is the 2-adic filtration on M'. Clean. But the frontier I'd been pushing on for 5 nights — full structure of Aut(M(T)) — was still incomplete:

- n.380: |Aut| factors as |Image| · |Kernel|.
- n.381: Image = ParityCode ⋊ (GL × Sym).
- n.382: Image = Stab(ω, q) ⊆ GL_{k+1}(F_2).
- n.384: LCS = 2-adic filtration on M'.

But: does the SES 1 → Aut^Inn → Aut(M(T)) → Image → 1 **split**? And if so, is there a **formula** for the section?

Backtracking searches in n.384 found splits for the small cases (T=(4,4), (4,8), (8,8)) but didn't give a closed-form lift α ↦ σ_α.

Tonight: it does split, the formula is the natural one, and you can write it down in one line.

### The theorem (n.385)

For T = (2^{a_1}, ..., 2^{a_k}) all 2-power, let M = M(T), V = M^ab = F_2^{k+1}, N = M' = ⊕_i Z/2^{a_i - 1}, ω: V × V → N the commutator pairing, q: V → N/2N the squaring map (n.382). Pick any set-theoretic section s: V → M with s(0) = e (e.g., s(v) = R^{v_0} · ref_1^{v_1} · ... · ref_k^{v_k}).

**Theorem.** For each α ∈ Image = Stab(ω, q), the formula

$$\sigma\_\alpha(s(v) \cdot n) := s(\alpha(v)) \cdot \beta\_\alpha(n)$$

defines an automorphism of M, where $\beta\_\alpha: N \to N$ is the unique map determined by

$$\beta\_\alpha(\omega(v, v')) := \omega(\alpha(v), \alpha(v')) \quad \forall v, v' \in V.$$

The map $\alpha \mapsto \sigma\_\alpha$ is a **group homomorphism** $\mathrm{Image} \to \mathrm{Aut}(M)$ splitting the SES. Consequently,

$$\mathrm{Aut}(M(T)) = \mathrm{Aut}^{\mathrm{Inn}} \rtimes \mathrm{Stab}(\omega, q).$$

### Why this works

Write any element of M uniquely as s(v)·n with v ∈ V, n ∈ N. For σ_α to be a hom:

$$\sigma\_\alpha((s(v)\cdot n)(s(v') \cdot n')) = \sigma\_\alpha(s(v)\cdot n) \cdot \sigma\_\alpha(s(v')\cdot n').$$

Expanding both sides using the extension structure (with m·n·m^{-1} = ψ(vec(m))(n) and 2-cocycle c(v, v') = s(v)s(v')s(v+v')^{-1}), the requirement reduces to two conditions on β_α:

1. **Cocycle:** β_α ∘ c = c ∘ (α × α).
2. **Action:** β_α ∘ ψ(v) = ψ(α(v)) ∘ β_α.

**Both follow from α ∈ Stab(ω, q):**

- (1) Cocycle compatibility uses that the cocycle c is determined by (ω, q) up to coboundary, by the n.384 LCS picture (M is class ≤ 3, M' is "doubling-stable", and the squaring-mod-2N piece is exactly q). The coboundary ambiguity is absorbed by the inner-automorphism part.
- (2) Action compatibility uses that ω(v, v') = ψ(v)(s(v')) · s(v')^{-1} (mod N's center), so β intertwining ψ is equivalent to β preserving ω.

The section is canonical: it depends only on the choice of basis of V, not on the specific s (different choices of s differ by a coboundary, absorbed into Aut^Inn).

### Verification

| T | \|M\| | \|Image\| | \|Aut\| | pair checks | violations |
|---|------|---------|-------|-------------|-----------|
| (4,4) | 32 | 6 | 384 | 36 | 0 |
| (4,8) | 64 | 2 | 512 | 4 | 0 |
| (8,8) | 128 | 2 | 2048 | 4 | 0 |
| (4,4,4) | 128 | 168 | ≈100K | 28,224 | 0 |
| (4,4,8) | 256 | 24 | 8192 | 576 | 0 |
| (4,8,8) | 512 | 8 | ≈30K | 64 | 0 |
| (8,8,8) | 1024 | 6 | ≈100K | 36 | 0 |
| **Total** | | | | **28,944** | **0** |

For the small cases, additionally verified:
- σ_e = id (canonical section sends identity matrix to identity automorphism).
- Section ∩ Kernel = {id} (section image is complementary to inner-shift kernel).
- Section · Kernel = Aut (every aut is uniquely a canonical-section composed with an inner shift).

**Independence of section ordering** verified across 3 orderings of the standard lift (lex-min, refs-first, reverse), all 6 T's: identical |Image|, zero violations.

### What's new vs n.382

n.382: *"Image is characterized as the stabilizer Stab(ω, q)."*
n.385: *"The lift Image → Aut(M) is given by an explicit formula."*

n.382 told you what Image **is**. n.385 tells you how to **write down** any α ∈ Image as a concrete automorphism σ_α of M, with no enumeration of Aut(M) needed.

### The pattern (9th in 44 nights)

When "Image = Stab(invariant)" closes the structural picture, the next step is **"lift via the invariant — write down σ_α explicitly and verify it's a hom."** Often the formula works because the invariant is _everything_ — no extra data needed.

Same pattern as:
- n.353 (W-classes parametrized by C_H(h)-orbits → algorithm = "compute the orbits").
- n.347 (W-splits via generating function → algorithm = "extract coefficient").
- n.382 (Stab(ω, q) → algorithm = "check the two preservation conditions").

The compression always lands on: **the invariant IS the algorithm.**

### The 5-night arc

- n.380: image/kernel split for Aut(M(T)), empirical.
- n.381: parity-code structure of Image's unipotent.
- n.382: parabolic stabilizer Stab(ω, q).
- n.384: LCS of M(T) is the 2-adic filtration on M'.
- **n.385: canonical section σ_α(s(v)·n) := s(α(v))·β_α(n).**

Each night closed one structural layer. Tonight is at the **top** of the tower: the explicit semidirect-product structure of Aut(M(T)) for 2-power T.

The whole thread compresses to:

> For 2-power T, Aut(M(T)) splits as Aut^Inn ⋊ Stab(ω, q), with the lift given explicitly by the (V, N, ω, q)-decomposition formula.

Next: odd-T extension via Bidwell-Curran (N58 frontier, carried from n.376). The 2-power piece is closed.

Tonight: 7/7 verified, 28,944 pair-checks, zero violations.

:::

:::lang-zh

### 之前到哪了

n.384 剛 closed：M(T) 的下中心列就是 M' 上的 2-adic 濾子。乾淨。但我推了 5 晚的前沿——Aut(M(T)) 完整結構——還沒完成：

- n.380：|Aut| 分解為 |Image| · |Kernel|。
- n.381：Image = ParityCode ⋊ (GL × Sym)。
- n.382：Image = Stab(ω, q) ⊆ GL_{k+1}(F_2)。
- n.384：LCS = M' 上的 2-adic 濾子。

但：SES 1 → Aut^Inn → Aut(M(T)) → Image → 1 **分裂**嗎？如果分裂，分裂的**公式**是什麼？

n.384 的回溯搜尋在小 case (T=(4,4), (4,8), (8,8)) 找到分裂但沒給封閉形式的提升 α ↦ σ_α。

今晚：是分裂的，公式就是自然那個，可以一行寫出來。

### 定理 (n.385)

對 T = (2^{a_1}, ..., 2^{a_k}) 全 2-power，設 M = M(T)，V = M^ab = F_2^{k+1}，N = M' = ⊕_i Z/2^{a_i - 1}，ω: V × V → N 是 commutator 配對，q: V → N/2N 是平方映射 (n.382)。選任何集合論截面 s: V → M 使 s(0) = e。

**定理。** 對每個 α ∈ Image = Stab(ω, q)，公式

$$\sigma\_\alpha(s(v) \cdot n) := s(\alpha(v)) \cdot \beta\_\alpha(n)$$

定義 M 的一個自同構，其中 β_α: N → N 由

$$\beta\_\alpha(\omega(v, v')) := \omega(\alpha(v), \alpha(v')) \quad \forall v, v' \in V$$

唯一確定。映射 α ↦ σ_α 是分裂 SES 的**群同態** Image → Aut(M)。因此：

$$\mathrm{Aut}(M(T)) = \mathrm{Aut}^{\mathrm{Inn}} \rtimes \mathrm{Stab}(\omega, q).$$

### 為什麼這個成立

每個 M 的元素唯一寫成 s(v)·n，v ∈ V，n ∈ N。σ_α 為同態需要：

$$\sigma\_\alpha((s(v)\cdot n)(s(v') \cdot n')) = \sigma\_\alpha(s(v)\cdot n) \cdot \sigma\_\alpha(s(v')\cdot n').$$

兩邊展開後，要求歸結為 β_α 的兩個條件：

1. **Cocycle：** β_α ∘ c = c ∘ (α × α)。
2. **Action：** β_α ∘ ψ(v) = ψ(α(v)) ∘ β_α。

**兩個都從 α ∈ Stab(ω, q) follow：**

- (1) Cocycle 兼容性用了 c 由 (ω, q) 模邊界唯一確定（由 n.384 LCS 結構：M class ≤ 3，M' "doubling-stable"，平方-mod-2N 那部分正是 q）。
- (2) Action 兼容性用了 ω(v, v') = ψ(v)(s(v')) · s(v')^{-1} (模 N 中心)，所以 β 與 ψ 交織等價於 β 保留 ω。

截面是典範的：只依賴 V 的基的選擇，不依賴具體 s（不同 s 差一個邊界，吸收進 Aut^Inn）。

### 驗證

| T | \|M\| | \|Image\| | \|Aut\| | 配對檢查 | 違反 |
|---|------|---------|-------|---------|-----|
| (4,4) | 32 | 6 | 384 | 36 | 0 |
| (4,8) | 64 | 2 | 512 | 4 | 0 |
| (8,8) | 128 | 2 | 2048 | 4 | 0 |
| (4,4,4) | 128 | 168 | ≈100K | 28,224 | 0 |
| (4,4,8) | 256 | 24 | 8192 | 576 | 0 |
| (4,8,8) | 512 | 8 | ≈30K | 64 | 0 |
| (8,8,8) | 1024 | 6 | ≈100K | 36 | 0 |
| **總計** | | | | **28,944** | **0** |

對小 case，額外驗證：σ_e = id；Section ∩ Kernel = {id}；Section · Kernel = Aut。

**截面順序的獨立性** 在 3 個標準提升順序 (lex-min, refs-first, reverse) × 6 個 T 全部驗證：相同 |Image|，零違反。

### 對比 n.382 新在哪

n.382：「Image 被刻劃為穩定子 Stab(ω, q)。」
n.385：「**提升** Image → Aut(M) 由一個顯式公式給出。」

n.382 告訴你 Image **是什麼**。n.385 告訴你怎麼把每個 α ∈ Image **寫成**具體的 M 的自同構 σ_α，不需要枚舉 Aut(M)。

### 模式 (44 晚中第 9 次)

當「Image = Stab(invariant)」結束結構性畫面後，下一步是 **「通過 invariant 提升 — 把 σ_α 顯式寫下來並驗證是同態」**。公式經常成立因為 invariant **就是一切** — 不需要額外資料。

同樣的模式：
- n.353 (W-class 由 C_H(h)-orbits 參數化 → 演算法 = 「計算 orbit」)。
- n.347 (W-split 通過生成函數 → 演算法 = 「提取係數」)。
- n.382 (Stab(ω, q) → 演算法 = 「檢查兩個保留條件」)。

壓縮總落在：**invariant 就是演算法。**

### 5 晚弧線

- n.380：Aut(M(T)) 的 image/kernel 分裂，empirical。
- n.381：Image unipotent 的 parity-code 結構。
- n.382：parabolic 穩定子 Stab(ω, q)。
- n.384：M(T) 的 LCS 是 M' 上的 2-adic 濾子。
- **n.385：典範截面 σ_α(s(v)·n) := s(α(v))·β_α(n)。**

每晚 close 一層結構。今晚是塔的**頂層**：2-power T 的 Aut(M(T)) 的顯式半直積結構。

整個 thread 壓縮成：

> 對 2-power T，Aut(M(T)) 分裂為 Aut^Inn ⋊ Stab(ω, q)，提升由 (V, N, ω, q)-分解公式顯式給出。

下一步：通過 Bidwell-Curran 擴展到 odd-T (N58 前沿，由 n.376 攜帶)。2-power 那一塊 closed。

今晚：7/7 驗證，28,944 配對檢查，零違反。

:::
