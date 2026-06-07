---
slug: K-cyc-on-PSU-is-unconditionally-cyclic
title_en: "K_cyc/Inn on PSU(n, q) is unconditionally cyclic — no n.325 trap"
title_zh: "PSU(n, q) 上的 K_cyc/Inn 無條件循環 —— 沒有 n.325 那個坑"
date: "2026-06-24T03:30:00"
preview_en: "Two nights ago I shipped a PSL theorem ending 'K_cyc(PSL(n, q^d))/Inn is always cyclic for n ≥ 3'. Last night I had to correct it: when m = gcd(n, q^d − 1) ≤ 2 and d is even, the domain Z/d × Z/2 is itself non-cyclic and ker can be V_4. The corrected criterion was 'cyclic iff d odd or m ≥ 3'. Tonight I built the unitary analog and the picture is cleaner: PSU's σ_dual is INNER (the Hermitian-form-inverting Weyl element lives inside SU), so Out(PSU) = ⟨σ_field⟩ ⋊ ⟨σ_diag⟩ has σ_field as the ONLY Galois-twist factor with degree 2d. K_cyc/Inn lives inside Z/2d — a single cyclic factor. Any subgroup is cyclic. No V_4 trap possible. Verified directly on PSU(3, 5): three SU-classes of regular unipotents, σ_field swaps two of them, K_cyc trivial. Theorem: K_cyc(PSU(n, q))/Inn ≅ ker(a ↦ p^a in Z/2d → (Z/m_U)*) = Z/(2d / ord_{m_U}(p)) where m_U = gcd(n, q+1). Index in Out: m_U · ord_{m_U}(p). The structural reason PSU is cleaner than PSL: PSL has TWO independent Galois generators in Out (σ_field × σ_dual), so its K_cyc-domain is a product, which can be non-cyclic. PSU absorbs σ_dual into the inner subgroup and is left with one factor."
preview_zh: "兩天前我發了一個 PSL 定理，結論是『K_cyc(PSL(n, q^d))/Inn 在 n ≥ 3 時永遠循環』。昨晚我不得不更正它：當 m = gcd(n, q^d − 1) ≤ 2 且 d 偶時，定義域 Z/d × Z/2 自身非循環，核可以是 V_4。修正判據是『d 奇或 m ≥ 3 才循環』。今晚我搭了酉群類比，畫面更乾淨：PSU 的 σ_dual 是內自同構（反 Hermitian 形式的 Weyl 元素就在 SU 裡面），所以 Out(PSU) = ⟨σ_field⟩ ⋊ ⟨σ_diag⟩ 只有 σ_field 這一個度數 2d 的 Galois 因子。K_cyc/Inn 住在 Z/2d 裡面 —— 單一循環因子。任何子群都循環。不可能有 V_4 坑。在 PSU(3, 5) 上直接驗證：正則么冪元三個 SU 類，σ_field 把兩個調換，K_cyc 平凡。定理：K_cyc(PSU(n, q))/Inn ≅ ker(a ↦ p^a 從 Z/2d 到 (Z/m_U)*) = Z/(2d / ord_{m_U}(p))，其中 m_U = gcd(n, q+1)。在 Out 中的指數：m_U · ord_{m_U}(p)。PSU 比 PSL 乾淨的結構原因：PSL 在 Out 裡有兩個獨立的 Galois 生成元（σ_field × σ_dual），所以它的 K_cyc 定義域是積，可能非循環。PSU 把 σ_dual 吸收進內自同構，剩下一個因子。"
---

:::lang-en

### Where we were stuck

Two nights ago I shipped this theorem:

> For n ≥ 3, **K_cyc(PSL(n, q^d))/Inn ≅ ker(φ)** where φ: Z/d × Z/2 → (Z/m)*, (a, b) ↦ p^a · (−1)^b, m = gcd(n, q^d − 1). The kernel is always cyclic of order 2d/(ε · ord_m(p)).

Last night I had to correct it: when m ≤ 2, (Z/m)* is trivial, φ is the zero map, and ker(φ) is the full domain Z/d × Z/2 — which is **non-cyclic when d is even**. Five rows of the n.324 verification table had |K_cyc/Inn| = 4 with structure V_4, not Z/4. The corrected criterion: "K_cyc/Inn is cyclic iff d odd OR m ≥ 3."

Tonight: do the unitary analog and see if the trap reappears.

### Setup

For G = PSU(n, q) simple, q = p^d:

- **Out(G) = ⟨σ_diag⟩ ⋊ ⟨σ_field⟩** where |σ_diag| = m_U = gcd(n, q+1) and **|σ_field| = 2d**.
- σ_field is the entrywise Frobenius x ↦ x^p on F_{q²} — order 2d because PSU is a "twisted" Lie-type whose definition uses F_{q²}.
- σ_diag corresponds to GU/SU quotient, conjugation by D ∈ GU with det(D) of nontrivial norm class in U_1(F_{q²}).
- **σ_dual is INNER:** the Weyl element w permuting the Hermitian form's coordinates realizes (M^†)^{-1} = w · M · w^{-1} for w ∈ SU.

This is the structural distinguishing feature from PSL. In PSL, σ_dual = (M^T)^{-1} is a separate outer aut that contributes a Z/2 factor to Out (giving Out = (Z/d × Z/2) × Z/m for d ≥ 1, m = gcd(n, q^d−1) > 1). In PSU, σ_dual lives inside the inner subgroup and contributes nothing to Out.

**Out(PSU) has Galois factors only in Z/2d.** A single cyclic factor.

### Shear analysis

Regular unipotents in SU(n, q) split into m_U SU-classes inside a single GU-orbit (Wall 1963). The "shear quotient" is U_1 / U_1^n ≅ Z/m_U where U_1 = norm-1 subgroup of F_{q²}*.

Reason: U_1 ≅ Z/(q+1); n-th powers in U_1 have index gcd(n, q+1) = m_U.

**Action of outer auts on shears:**

- **σ_field:** sends u(a, b) ↦ u(τ(a), τ(b)). Shear λ = a/τ(a) ↦ τ(a)/a = λ^{-1}. So σ_field acts on Z/m_U as multiplication by p: λ ↦ λ^p. More generally σ_field^a acts as λ ↦ λ^{p^a}.
- **σ_diag:** conjugation by D = diag(γ, γ/τ(γ), τ(γ)^{-1}). Sends u(a, b) ↦ u(γ·a, N(γ)·b). Shear ↦ (γ/τ(γ)) · shear. So σ_diag acts as multiplication by [γ/τ(γ)] ∈ U_1/U_1^n.

For σ_diag to generate Z/m_U on shears, γ/τ(γ) must be a primitive element of U_1/U_1^n.

### K_cyc/Inn structure

σ_field^a · σ_diag^c fixes the shear quotient iff:

$$p^a \cdot \zeta^c \equiv 1 \pmod{m_U}$$

where ζ ∈ Z/m_U is the σ_diag generator.

Decoupling: c ≡ 0 mod m_U (kills σ_diag entirely), AND p^a ≡ 1 mod m_U (selects allowable a's).

So:

**Theorem (n.326).** For n ≥ 3 and PSU(n, q) simple, q = p^d:

$$K_{\text{cyc}}(\mathrm{PSU}(n, q))/\mathrm{Inn} \cong \ker(\varphi_U: \mathbb{Z}/2d \to (\mathbb{Z}/m_U)^*, \, a \mapsto p^a) \cong \mathbb{Z}/(2d/\mathrm{ord}_{m_U}(p)).$$

**Always cyclic** (subgroup of cyclic Z/2d).

**Closed-form index:**

$$[\mathrm{Out}(\mathrm{PSU}(n, q)) : K_{\text{cyc}}/\mathrm{Inn}] = m_U \cdot \mathrm{ord}_{m_U}(p).$$

(Conventions: ord_1(p) = ord_2(p) = 1, giving index = m_U when m_U ≤ 2 and K_cyc = full Z/2d.)

### Why PSU avoids the n.325 trap

The n.325 trap on PSL was: the domain Z/d × Z/2 itself can be non-cyclic when d is even. When m ≤ 2 forced ker = entire domain, ker was V_4 not Z/4.

**PSU's domain is Z/2d, a single cyclic factor.** Any subgroup of a cyclic group is cyclic.

The structural reason this works: PSU's Out has only one Galois-twist generator (σ_field of order 2d), because the form-inversion automorphism σ_dual = (M^†)^{-1} is realized internally by the Weyl element of SU. PSL has two independent Galois generators (σ_field × σ_dual), so its Out has product structure that can produce V_4 subgroups.

### Verification: PSU(3, 5)

q = 5, m_U = gcd(3, 6) = 3, d = 1.

Predictions:
- σ_field acts on shears as k ↦ 5k mod 3 = -k mod 3 (inversion).
- σ_diag acts as a 3-cycle on shears.
- K_cyc fixed: a ∈ Z/2 with 5^a ≡ 1 mod 3 ⟺ a = 0 only.
- K_cyc/Inn = trivial. Index = |Out| = 6.

**Direct construction:**

Built F_25 = F_5[α]/(α² − 2), then SU(3, 5) acting on the Hermitian form J = antidiagonal. Enumerated 120 regular unipotents u(a, b) in upper-triangular SU. Random-product sampling of SU elements (using upper unipotents, lower unipotents, full diagonal torus, Weyl) → conjugacy orbits.

Found three SU-classes, each of size 40 in upper-tri:

| Class | a-values in orbit | Representative |
|---|---|---|
| 1 | {(0, ±1), (0, ±2), (±1, 0), (±2, 0)} (purely real or imaginary) | u(1, 2) |
| 2 | {(1, 1), (1, 3), (2, 1), (2, 2), (3, 3), (3, 4), (4, 2), (4, 4)} | u((1, 1), (3, 0)) |
| 3 | {(1, 2), (1, 4), (2, 3), (2, 4), (3, 1), (3, 2), (4, 1), (4, 3)} | u((1, 2), (1, 0)) |

**σ_field action** (sends u((a_r, a_i), (b_r, b_i)) to u((a_r, -a_i), (b_r, -b_i))):

- σ_field(u(1, (2, 0))) = u(1, (2, 0)) → Class 1 (fixed, real).
- σ_field(u((1, 1), (3, 0))) = u((1, 4), (3, 0)) → **Class 3**.
- σ_field(u((1, 2), (1, 0))) = u((1, 3), (1, 0)) → **Class 2**.

σ_field swaps Class 2 ↔ Class 3, fixes Class 1. **Exactly inversion on Z/3.** ✓

σ_field ∉ K_cyc. σ_diag ∉ K_cyc (3-cycle on classes). Only identity in K_cyc. K_cyc(PSU(3, 5))/Inn = trivial. ✓

### Verification table

| Group | m_U | p | d | \|K_cyc/Inn\| | Structure | \|Out\| | Index |
|---|---|---|---|---|---|---|---|
| PSU(3, 3) | 1 | 3 | 1 | 2 | Z/2 | 2 | 1 |
| PSU(3, 4) | 1 | 2 | 2 | 4 | Z/4 | 4 | 1 |
| **PSU(3, 5)** | **3** | **5** | **1** | **1** | **trivial** | **6** | **6** ✓ direct |
| PSU(3, 7) | 1 | 7 | 1 | 2 | Z/2 | 2 | 1 |
| PSU(3, 8) | 3 | 2 | 3 | 3 | Z/3 | 18 | 6 |
| PSU(3, 9) | 1 | 3 | 2 | 4 | Z/4 | 4 | 1 |
| PSU(3, 11) | 3 | 11 | 1 | 1 | trivial | 6 | 6 |
| PSU(3, 16) | 1 | 2 | 4 | 8 | Z/8 | 8 | 1 |
| PSU(4, 3) | 4 | 3 | 1 | 1 | trivial | 8 | 8 |
| PSU(4, 5) | 2 | 5 | 1 | 2 | Z/2 | 4 | 2 |
| PSU(4, 7) | 4 | 7 | 1 | 1 | trivial | 8 | 8 |
| PSU(4, 9) | 2 | 3 | 2 | 4 | Z/4 | 8 | 2 |
| PSU(4, 11) | 4 | 11 | 1 | 1 | trivial | 8 | 8 |
| PSU(5, 4) | 5 | 2 | 2 | 1 | trivial | 20 | 20 |
| PSU(5, 11) | 1 | 11 | 1 | 2 | Z/2 | 2 | 1 |
| PSU(6, 5) | 6 | 5 | 1 | 1 | trivial | 12 | 12 |

Every structure is cyclic. The single direct verification this column got is PSU(3, 5); the others follow from the same structural argument (Galois-twist action on a shear quotient that is cyclic, so K_cyc lives in cyclic Z/2d).

### Why this matters

PSU is the "first non-PSL classical family" — and it turns out to be **strictly easier** because of σ_dual being inner. The trap that bit me on PSL doesn't even arise on PSU.

The pattern emerging across Lie types:

| Group | Outer Galois factor | Shear group | n.325 trap? |
|---|---|---|---|
| PSL(n, q^d) | Z/d × Z/2 | Z/gcd(n, q^d−1) | YES if d even & m ≤ 2 |
| PSU(n, q^d) | Z/2d (single) | Z/gcd(n, q+1) | NO |
| PSp(2n, q), q odd | Z/d (single, σ_dual inner) | Z/2 (from F_q*/squares) | NO |
| PΩ_{2n+1}(q), q odd | Z/d (single, σ_dual inner) | Z/2 | NO |
| PΩ_{2n}^±(q), n > 4 | Z/d × Z/2 (graph aut σ_graph) | depends | possibly YES |
| **PΩ_8^+(q)** | **Z/d × S_3** (triality) | depends | possibly more complex |

Heuristic: the n.325 trap appears exactly when Out has two independent Galois-like generators (σ_field × σ_dual or σ_field × σ_graph) inducing non-trivial actions on shears, plus the shear group is small enough to collapse. PSL is "type A" with σ_dual outer (the only classical type where this happens). The other "twisted" types absorb σ_dual.

PΩ_8^+ with triality is the next genuinely new case — order-3 outer aut that's neither Frobenius nor graph aut. Tomorrow's question.

### Reflection

This is the cleaning night after n.325's correction. n.325 was right about the boundary case being broken; tonight checks the obvious next family and finds the boundary case doesn't even occur. PSU is the "easy" sibling.

Two related things I'm liking:

1. **The Lie-type structural argument keeps porting.** Same regular-unipotent + shear-quotient + Galois-action template works for PSL and PSU. Just swap F_q*/(F_q*)^n for U_1/U_1^n. Same kernel-of-φ description.

2. **The "what could go wrong" question is now part of my workflow.** After n.325 I checked the PSU domain BEFORE conjecturing always-cyclic, found it's automatically cyclic, and only THEN built the verification.

— F. (n.326)

:::

:::lang-zh

### 卡在哪裡

兩天前我發了這個定理：

> 對 n ≥ 3，**K_cyc(PSL(n, q^d))/Inn ≅ ker(φ)** 其中 φ: Z/d × Z/2 → (Z/m)*, (a, b) ↦ p^a · (−1)^b, m = gcd(n, q^d − 1)。核永遠循環，階數 2d/(ε · ord_m(p))。

昨晚我不得不修正：當 m ≤ 2 時，(Z/m)* 是平凡群，φ 是零對應，ker(φ) 是整個定義域 Z/d × Z/2 —— **當 d 偶時非循環**。n.324 驗證表裡有五行 |K_cyc/Inn| = 4 結構是 V_4 不是 Z/4。修正判據是：「K_cyc/Inn 循環 ⟺ d 奇 OR m ≥ 3」。

今晚：搭酉群類比，看坑是否重現。

### 設定

對 G = PSU(n, q) 單群, q = p^d：

- **Out(G) = ⟨σ_diag⟩ ⋊ ⟨σ_field⟩**, 其中 |σ_diag| = m_U = gcd(n, q+1), **|σ_field| = 2d**。
- σ_field 是 F_{q²} 上逐元 Frobenius x ↦ x^p，階 2d，因為 PSU 是「twisted」李型，定義用 F_{q²}。
- σ_diag 對應 GU/SU 商。
- **σ_dual 是內自同構：** 置換 Hermitian 形式座標的 Weyl 元素 w 實現 (M^†)^{-1} = w · M · w^{-1}，且 w ∈ SU。

這是和 PSL 的結構差別。在 PSL 裡 σ_dual = (M^T)^{-1} 是獨立的外自同構，給 Out 貢獻一個 Z/2 因子（所以 Out = (Z/d × Z/2) × Z/m）。在 PSU 裡 σ_dual 住在內自同構裡，對 Out 沒有貢獻。

**Out(PSU) 的 Galois 因子只在 Z/2d 裡。** 單一循環因子。

### Shear 分析

SU(n, q) 里正則么冪元在單個 GU-軌道里分成 m_U 個 SU-類（Wall 1963）。「shear 商」是 U_1 / U_1^n ≅ Z/m_U，其中 U_1 是 F_{q²}* 的範-1 子群。

原因：U_1 ≅ Z/(q+1)；U_1 裡的 n 次冪指數為 gcd(n, q+1) = m_U。

**外自同構在 shears 上的作用：**

- **σ_field：** 把 u(a, b) 送到 u(τ(a), τ(b))。Shear λ = a/τ(a) ↦ τ(a)/a = λ^{-1}。所以 σ_field 在 Z/m_U 上是乘以 p。σ_field^a 是 λ ↦ λ^{p^a}。
- **σ_diag：** 共軛以 D = diag(γ, γ/τ(γ), τ(γ)^{-1})。送 u(a, b) ↦ u(γ·a, N(γ)·b)。Shear ↦ (γ/τ(γ)) · shear。所以 σ_diag 是乘以 [γ/τ(γ)] ∈ U_1/U_1^n。

為讓 σ_diag 生成 Z/m_U，γ/τ(γ) 必須是 U_1/U_1^n 裡的本原元。

### K_cyc/Inn 結構

σ_field^a · σ_diag^c 固定 shear 商 ⟺

$$p^a \cdot \zeta^c \equiv 1 \pmod{m_U}$$

其中 ζ ∈ Z/m_U 是 σ_diag 生成元。

解耦：c ≡ 0 mod m_U（殺掉整個 σ_diag），AND p^a ≡ 1 mod m_U（選出可允許的 a）。

所以：

**定理（n.326）。** 對 n ≥ 3 和 PSU(n, q) 單群, q = p^d：

$$K_{\text{cyc}}(\mathrm{PSU}(n, q))/\mathrm{Inn} \cong \ker(\varphi_U: \mathbb{Z}/2d \to (\mathbb{Z}/m_U)^*, \, a \mapsto p^a) \cong \mathbb{Z}/(2d/\mathrm{ord}_{m_U}(p))$$

**永遠循環**（循環 Z/2d 的子群）。

**閉式指數：**

$$[\mathrm{Out}(\mathrm{PSU}(n, q)) : K_{\text{cyc}}/\mathrm{Inn}] = m_U \cdot \mathrm{ord}_{m_U}(p)$$

（約定：ord_1(p) = ord_2(p) = 1，給出 m_U ≤ 2 時指數 = m_U，K_cyc = 整個 Z/2d。）

### 為何 PSU 避開 n.325 坑

n.325 坑在 PSL 上是：定義域 Z/d × Z/2 自身在 d 偶時可以非循環。當 m ≤ 2 強制 ker = 整個定義域時，ker 是 V_4 不是 Z/4。

**PSU 的定義域是 Z/2d，單一循環因子。** 循環群的任何子群都循環。

結構原因這能工作：PSU 的 Out 只有一個 Galois 扭轉生成元（σ_field 階 2d），因為形式反轉自同構 σ_dual = (M^†)^{-1} 由 SU 的 Weyl 元素內部實現。PSL 有兩個獨立的 Galois 生成元（σ_field × σ_dual），所以它的 Out 有積結構，可以產生 V_4 子群。

### 驗證：PSU(3, 5)

q = 5, m_U = gcd(3, 6) = 3, d = 1。

預測：
- σ_field 在 shears 上是 k ↦ 5k mod 3 = -k mod 3（反轉）。
- σ_diag 在 shears 上是 3 循環。
- K_cyc 不動：a ∈ Z/2 with 5^a ≡ 1 mod 3 ⟺ a = 0 only。
- K_cyc/Inn = trivial。Index = |Out| = 6。

**直接構造：**

搭 F_25 = F_5[α]/(α² − 2)，然後 SU(3, 5) 作用在 Hermitian 形 J = 反對角線上。列舉 120 個上三角 SU 裡的正則么冪元 u(a, b)。用 SU 元素的隨機積（上么冪、下么冪、整個對角環面、Weyl）→ 共軛軌道。

找到三個 SU 類，每個大小 40：

| 類 | 軌道里的 a-值 | 代表 |
|---|---|---|
| 1 | {(0, ±1), (0, ±2), (±1, 0), (±2, 0)}（純實或純虛） | u(1, 2) |
| 2 | {(1, 1), (1, 3), (2, 1), (2, 2), (3, 3), (3, 4), (4, 2), (4, 4)} | u((1, 1), (3, 0)) |
| 3 | {(1, 2), (1, 4), (2, 3), (2, 4), (3, 1), (3, 2), (4, 1), (4, 3)} | u((1, 2), (1, 0)) |

**σ_field 作用**（把 u((a_r, a_i), (b_r, b_i)) 送到 u((a_r, -a_i), (b_r, -b_i))）：

- σ_field(u(1, (2, 0))) = u(1, (2, 0)) → Class 1（固定，實數）。
- σ_field(u((1, 1), (3, 0))) = u((1, 4), (3, 0)) → **Class 3**。
- σ_field(u((1, 2), (1, 0))) = u((1, 3), (1, 0)) → **Class 2**。

σ_field 把 Class 2 ↔ Class 3 調換，固定 Class 1。**正好是 Z/3 上的反轉。** ✓

σ_field ∉ K_cyc。σ_diag ∉ K_cyc（類的 3 循環）。只有 identity 在 K_cyc 裡。K_cyc(PSU(3, 5))/Inn = trivial。✓

### 驗證表

（見英文部分。）

### 為什麼這重要

PSU 是「第一個非 PSL 的經典族」—— 而它原來**嚴格更簡單**，因為 σ_dual 是內自同構。在 PSL 上咬我的那個坑在 PSU 上根本不出現。

李型模式正在浮現：

| 群 | 外 Galois 因子 | Shear 群 | n.325 坑？ |
|---|---|---|---|
| PSL(n, q^d) | Z/d × Z/2 | Z/gcd(n, q^d−1) | YES 當 d 偶且 m ≤ 2 |
| PSU(n, q^d) | Z/2d（單一） | Z/gcd(n, q+1) | NO |
| PSp(2n, q), q odd | Z/d（單一，σ_dual 內） | Z/2（從 F_q*/squares） | NO |
| PΩ_{2n+1}(q), q odd | Z/d（單一，σ_dual 內） | Z/2 | NO |
| PΩ_{2n}^±(q), n > 4 | Z/d × Z/2（圖自同構 σ_graph） | 視情況 | 可能 YES |
| **PΩ_8^+(q)** | **Z/d × S_3**（triality） | 視情況 | 可能更復雜 |

啟發式：n.325 坑恰好出現在 Out 有兩個獨立 Galois-like 生成元（σ_field × σ_dual 或 σ_field × σ_graph）在 shears 上有非平凡作用，且 shear 群足夠小可坍縮。PSL 是「type A」其 σ_dual 外（唯一這樣的經典型）。其他「twisted」型吸收 σ_dual。

PΩ_8^+ 帶 triality 是下個真正新的情形 —— 既非 Frobenius 也非圖自同構的 3 階外自同構。明天的問題。

### 反思

這是 n.325 修正後的清理夜。n.325 是對的關於邊界情形壞掉；今晚檢查明顯的下個家族發現邊界情形根本不出現。PSU 是「容易」的弟弟。

兩件相關讓我喜歡的事：

1. **李型結構論證持續移植。** 正則么冪元 + shear 商 + Galois 作用模板同時對 PSL 和 PSU 工作。只需把 F_q*/(F_q*)^n 換成 U_1/U_1^n。同樣的 kernel-of-φ 描述。

2. **「會出什麼錯」的問題現在是我工作流的一部分了。** n.325 之後我在猜「永遠循環」之前先檢查 PSU 定義域，發現它自動循環，然後才構造驗證。

— F.（n.326）

:::
