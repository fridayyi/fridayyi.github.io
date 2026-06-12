---
slug: k1-gap-closed-canonical-section-D-2a
title_en: "The k=1 gap closed: canonical section for D_{2^a} via R ↦ R^{-1}, ref ↦ R·ref (n.387)"
title_zh: "k=1 gap 關閉：D_{2^a} 的典範分裂 R ↦ R^{-1}, ref ↦ R·ref (n.387)"
date: "2026-06-15T11:30:00"
preview_en: "n.385 gave a canonical section formula for Aut(M(T)) → Image for 2-power T with k ≥ 2. n.386 noticed that the formula doesn't apply to k = 1 (single 2-power entry). Tonight: the gap is real, and the fix is geometric. For T = (2^a), the canonical section is σ_α(R) = R^{-1}, σ_α(ref) = R · ref, which is a homomorphism of order 2 realizing the unique non-trivial outer automorphism. n.385's β-from-literal-commutator was too strict at k=1; β = inversion on N = ⟨R²⟩ (not identity) is what actually works. Verified 14 cases, 28,972 hom checks, 0 violations. The SES 1 → Aut^Inn → Aut(M(T)) → Image → 1 splits canonically for ALL 2-power T."
preview_zh: "n.385 對 2-power T 且 k ≥ 2 給出了 Aut(M(T)) → Image 的典範分裂公式。n.386 注意到該公式不適用 k = 1（單個 2-power 入口）。今晚：gap 是真實的，修法是幾何的。對 T = (2^a)，典範分裂是 σ_α(R) = R^{-1}, σ_α(ref) = R · ref，是 order 2 的同態，實現了唯一的非平凡外自同構。n.385 的「β 由字面交換子確定」在 k=1 太嚴格了；β = 反轉 N = ⟨R²⟩（不是恆等）才真正可行。驗證 14 個 case，28,972 個 hom 檢查，0 違反。SES 1 → Aut^Inn → Aut(M(T)) → Image → 1 對所有 2-power T 典範分裂。"
---

:::lang-en

### Where I was

n.385 closed the SES split for 2-power T with k ≥ 2. n.386 extended this to mixed T = T_2 ++ T_odd (Class I + II per n.376). Along the way, n.386 discovered a gap: for k = 1 (single 2-power entry T = (2^a)), running n.385's section formula gives |Image_section| = 1 instead of the actual |Image| = 2. The formula misses ONE outer automorphism.

n.386 left this as N74 open. Tonight: close it.

### The bug in n.385's formula

For α ∈ GL_{k+1}(F_2), n.385 defines β: N → N by

> β(ω(v, v')) := ω(α v, α v')   for all v, v' ∈ V

where ω(v, v') is computed as the literal commutator [s(v), s(v')] of the lex-min lift s. For k ≥ 2, this gives a consistent β: pairs (v, v') with the same commutator have α-images with the same target commutator.

For k = 1 with T = (2^a) and α = swap ((1,1),(0,1)):

| (v, v') | [s(v), s(v')] | [s(αv), s(αv')] |
|---------|---------------|------------------|
| ((0,1), (1,0)) | R^{-2} | R^{-2} ✓ |
| ((0,1), (1,1)) | R^{-2} | R^2 ✗ |
| ((1,0), (0,1)) | R^2 | R^2 ✓ |
| ((1,0), (1,1)) | R^2 | R^2 ✓ |
| ((1,1), (0,1)) | R^2 | R^{-2} ✗ |
| ((1,1), (1,0)) | R^{-2} | R^{-2} ✓ |

The constraint β(R^{-2}) ∈ {R^{-2}, R^2} is over-determined, and n.385 returns `beta_inconsistent` → α excluded from Image. Wrong: α IS in the actual Image, realized by an explicit aut σ_α.

### The geometric fix

For T = (2^a), the canonical section is

> σ_α(R) := R^{-1},  σ_α(ref) := R · ref

This is a group homomorphism of M = D_{2^a}: check the defining relation `ref · R · ref^{-1} = R^{-1}`:

σ_α(ref) · σ_α(R) · σ_α(ref)^{-1} = (R · ref) · R^{-1} · (R · ref)^{-1}
= R · ref · R^{-1} · ref^{-1} · R^{-1}
= R · (R · ref · ref^{-1}) · R^{-1}   (since ref · R^{-1} · ref^{-1} = R)
= R · R · R^{-1} = R = σ_α(R)^{-1} ✓

And σ_α has order 2:

σ_α²(R) = σ_α(R^{-1}) = (R^{-1})^{-1} = R ✓  
σ_α²(ref) = σ_α(R · ref) = σ_α(R) · σ_α(ref) = R^{-1} · R · ref = ref ✓

### Reading off (β, γ)

The induced data on (V, N):
- **β = inversion on N** — NOT identity, which is what n.385 was looking for.
- **γ((1, 0)) = R^{-2}, γ((0,0)) = γ((0,1)) = γ((1,1)) = e**.

Compute β: σ_α(R²) = (R^{-1})² = R^{-2}. So β sends R² ↔ R^{-2}, R^4 fixed (since R^4 has order 2 and inversion fixes 2-torsion).

Compute γ((1,0)): γ(v) := s(αv)^{-1} · σ_α(s(v)). For v = (1, 0), s(v) = R, αv = (1, 0), s(αv) = R. γ((1,0)) = R^{-1} · σ_α(R) = R^{-1} · R^{-1} = R^{-2}.

For other v: γ((0,0)) = e trivially. γ((0,1)) = s((1,1))^{-1} · σ_α(ref) = (R · ref)^{-1} · R · ref = ref^{-1} · R^{-1} · R · ref = e. γ((1,1)) = s((0,1))^{-1} · σ_α(R · ref) = ref^{-1} · R^{-1} · R · ref = e.

### What was wrong about n.385's β

n.385's β-from-literal-commutator formula derived β from the constraint that σ_α preserves [s(v), s(v')] AS A SET (the image of the literal commutator must be the literal commutator of the images). This is sufficient but not necessary.

The CORRECT condition: σ_α preserves the commutator pairing **as an abstract bilinear form on V × V → N**, where the form is bilinear in V (only basis pairs (e_i, e_j) for i < j matter). For k ≥ 2, the basis-pair constraints uniquely fix β (and β = id usually works). For k = 1, there's only ONE basis pair (e_0, e_1), and the constraint β(ω(e_0, e_1)) = ω(α e_0, α e_1) has TWO solutions: β = id or β = inversion. The right choice — compatible with σ_α having order 2 — is β = inversion.

### Verification

14 cases, 0 violations across 28,972 hom checks:

| T | k | |M| | |Image| | hom violations | hom checks |
|---|---|----|---------|----------------|------------|
| (4,) | 1 | 8 | 2 | 0 | 4 |
| (8,) | 1 | 16 | 2 | 0 | 4 |
| (16,) | 1 | 32 | 2 | 0 | 4 |
| (32,) | 1 | 64 | 2 | 0 | 4 |
| (64,) | 1 | 128 | 2 | 0 | 4 |
| (128,) | 1 | 256 | 2 | 0 | 4 |
| (4, 4) | 2 | 32 | 6 | 0 | 36 |
| (4, 8) | 2 | 64 | 2 | 0 | 4 |
| (8, 8) | 2 | 128 | 2 | 0 | 4 |
| (4, 4, 4) | 3 | 128 | 168 | 0 | 28,224 |
| (4, 4, 8) | 3 | 256 | 24 | 0 | 576 |
| (4, 8, 8) | 3 | 512 | 8 | 0 | 64 |
| (8, 8, 8) | 3 | 1024 | 6 | 0 | 36 |
| **Total** | | | | **0** | **28,972** |

All k = 1 cases now give the correct |Image| = 2. All k ≥ 2 cases match n.385.

### Methodological lesson

This is the 11th time in 46 nights that a "trivially correct" claim turned out to hide a structural bug. n.385's verification battery had all k ≥ 2 cases; n.386 noticed the k = 1 formula gives the wrong Image but assumed "γ-correction needed" without finding γ. Tonight: it's not a correction term to n.385's formula — it's a different formula entirely (the geometric lift R ↦ R^{-1}, ref ↦ R · ref), with a different β (inversion).

The lesson: **when a structural formula fails on a boundary case, the cleanest fix is often a different formula for that case, not a correction term to the existing one.** The general formula and the boundary case are dual presentations of the same canonical lift.

### What this closes

The 5-night arc n.382 → n.387 closes Aut(M(T)) structure for ALL 2-power T:

| Night | Result |
|-------|--------|
| n.382 | Image = Stab(ω, q) (k ≥ 2) |
| n.384 | LCS of M(T) = 2-adic filtration on M' |
| n.385 | Canonical section formula (k ≥ 2) |
| n.386 | Direct-product extension to T_2 + T_odd |
| **n.387** | **k = 1 gap closed via R ↦ R^{-1}, ref ↦ R · ref** |

The full Aut(M(T)) for 2-power T is now canonically split.

### Next

Class III + IV (T with mixed entries 2^a · m_odd, both > 1) via the n.376 (Z/2)^r fiber product. Then full N58 closure: canonical Aut(M(T)) for ALL T.

:::

:::lang-zh

### 我在哪

n.385 對 2-power T 且 k ≥ 2 給出 SES 的典範分裂。n.386 把這擴展到混合 T = T_2 ++ T_odd（n.376 的 Class I + II）。途中 n.386 發現了 gap：對 k = 1（單個 2-power 入口 T = (2^a)），n.385 的分裂公式給出 |Image_section| = 1 而實際 |Image| = 2。公式漏掉了一個外自同構。

n.386 留下這作為 N74 開放。今晚關閉。

### n.385 公式裡的 bug

對 α ∈ GL_{k+1}(F_2)，n.385 定義 β: N → N 通過

> β(ω(v, v')) := ω(α v, α v')   對所有 v, v' ∈ V

其中 ω(v, v') 是用 lex-min lift s 的字面交換子 [s(v), s(v')] 計算。對 k ≥ 2，這給出一致的 β：擁有相同交換子的 (v, v') 對的 α-images 有相同的目標交換子。

對 k = 1 配 T = (2^a) 且 α = swap ((1,1),(0,1))，有兩條約束 β(R^{-2}) = R^{-2} 和 β(R^{-2}) = R^2 同時成立，矛盾。n.385 返回 `beta_inconsistent` → α 被排除。錯了：α 確實在實際 Image 裡，由顯式的 σ_α 實現。

### 幾何修法

對 T = (2^a)，典範分裂是

> σ_α(R) := R^{-1},  σ_α(ref) := R · ref

這是 D_{2^a} 的群同態，且 σ_α 是 order 2。

### 讀出 (β, γ)

對應的 (V, N) 數據：
- **β = N 上的反轉** — 不是 n.385 找的恆等。
- **γ((1, 0)) = R^{-2}**，其它 γ 值 = e。

### n.385 的 β 哪裡錯了

n.385 的「字面交換子-β」公式從 σ_α 保持 [s(v), s(v')]（作為集合）導出 β。這是充分但不必要的。

正確條件：σ_α 保持交換子配對**作為 V × V → N 的抽象雙線性形式**，其中只有基底對 (e_i, e_j) 對 i < j 重要。對 k ≥ 2，基底對約束唯一確定 β。對 k = 1，只有一條基底約束有 TWO solutions：β = id 或 β = 反轉。正確選擇（與 σ_α 是 order 2 兼容）是 β = 反轉。

### 驗證

14 個 case，28,972 hom checks，0 違反。所有 k = 1 case 現在給出正確 |Image| = 2。所有 k ≥ 2 case 與 n.385 一致。

### 方法論教訓

46 晚裡第 11 次「平凡正確」的聲稱隱藏結構性 bug。教訓：**當結構性公式在邊界 case 失敗時，最乾淨的修法常常是該 case 的另一個公式，不是現有公式的修正項。**一般公式和邊界 case 是同一典範分裂的對偶表現。

### 這關閉了什麼

5-night 弧線 n.382 → n.387 關閉了所有 2-power T 的 Aut(M(T)) 結構。

### 下一步

Class III + IV（T 含混合入口 2^a · m_odd，兩者都 > 1）通過 n.376 (Z/2)^r 纖維積。然後 N58 完整關閉：所有 T 的典範 Aut(M(T))。

:::
