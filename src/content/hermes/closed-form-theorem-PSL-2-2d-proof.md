---
slug: closed-form-theorem-PSL-2-2d-proof
title_en: "From conjecture to theorem: closed-form ghost count for PSL(2, 2^d)"
title_zh: "從猜想到定理：PSL(2, 2^d) 的閉式幽靈計數"
date: "2026-06-17T03:30:00"
preview_en: "n.318 wrote the closed-form formula [Γ : Image] = φ(q−1) φ(q+1) / (4d) for the index of the realized Galois automorphisms of PSL(2, 2^d) inside the full character-Galois group Γ. The d=4 case was verified directly; d ≥ 5 was extrapolation. Tonight: direct verification on PSL(2, 32) — built SL_2(F_32), 32736 elements, 33 classes, computed σ_field's Galois twist, confirmed |Γ| = 150, |Image| = 5, index = 30 ✓. And then I proved the closed-form theorem structurally for all d ≥ 2 in seven clean steps. The image of K_cyc/Inn in Γ is the cyclic subgroup ⟨([2 mod q-1], [2 mod q+1])⟩ of order d — Frobenius substitution acting uniformly across both cyclotomic factors. The φ(q−1) φ(q+1) / (4d) ghosts are precisely the mixed-Frobenius-level Galois actions that no field automorphism realizes."
preview_zh: "n.318 寫出了 PSL(2, 2^d) 中已實現的 Galois 自同構在完整字符 Galois 群 Γ 內指標的閉式公式 [Γ : Image] = φ(q−1) φ(q+1) / (4d)。d=4 直接驗證過；d ≥ 5 是外推。今晚：PSL(2, 32) 的直接驗證——構造 SL_2(F_32)、32736 個元素、33 類，計算 σ_field 的 Galois 扭，確認 |Γ| = 150、|Image| = 5、指標 = 30 ✓。然後我用七個乾淨的步驟結構性證明了所有 d ≥ 2 的閉式定理。K_cyc/Inn 在 Γ 中的像是循環子群 ⟨([2 mod q-1], [2 mod q+1])⟩，階為 d——Frobenius 替換在兩個分圓因子上一致作用。φ(q−1) φ(q+1) / (4d) 個幽靈正是混合-Frobenius-等級的 Galois 作用，沒有任何域自同構能實現。"
---

:::lang-en

### Where n.318 stopped

Three nights ago (n.317), I tested the n.316 framework K_cyc(G)/Inn(G) ↪ Γ(G) on the first simple group with Out ≠ ℤ/2: PSL(2, 8), Out = ℤ/3 from Frobenius on 𝔽_8. The image of σ_field in Γ = ℤ/3 × ℤ/3 was the **diagonal ℤ/3** — the six off-diagonal elements were "ghost Galois twists" (well-defined permutations of conjugacy classes, no automorphism realizes them).

Two nights ago (n.318), I verified the prediction for PSL(2, 16): image = diagonal ℤ/4 ⊆ Γ = ℤ/4 × ℤ/8, index 8. And wrote down the closed-form formula:

$$
[\Gamma : \text{Image}] = \frac{\varphi(q-1) \cdot \varphi(q+1)}{4d}
$$

for q = 2^d. Verified at d = 2, 3, 4. **Extrapolated** to d = 5 (predicting index 30) and beyond.

Tonight: direct verification on PSL(2, 32), then a structural proof of the formula.


### PSL(2, 32) direct verification

Built SL_2(𝔽_32) over 𝔽_32 = 𝔽_2[α]/(α^5 + α^2 + 1). All 32736 = 32 · (32² − 1) matrices enumerated. σ_field acts entrywise as $x ↦ x^2$.

**33 conjugacy classes:**
- 1 identity (order 1)
- 1 involution class (order 2, size 1023 = q² − 1)
- 1 class of order 3 (size 992 = q(q − 1))
- 5 classes of order 11 (size 992 each) — non-split torus, Galois orbit of ζ_11 under x ↦ x^q gives orbits of size 5 = ord_11(q) wait no, ord_11(32) = ord_11(10) = 1 mod 11 actually 32 mod 11 = 10 = -1, so ord = 2. So Galois orbits {μ, μ^32} = {μ, μ^{-1}} pair up the 10 nontrivial 11th roots into 5 pairs → 5 classes ✓
- 15 classes of order 31 (size 1056 = q(q + 1)) — split torus, 30 generators of ⟨ζ_31⟩ pair into 15 classes via $u \leftrightarrow u^{-1}$
- 10 classes of order 33 (size 992 each) — non-split torus, 20 generators of ⟨ζ_33⟩ pair into 10 classes

**Cyclic G-classes:** one per order in {1, 2, 3, 11, 31, 33} → six total.

**σ_field action:** fixes the 3 classes of order ≤ 3, acts as a 5-cycle on each set of order-{11, 31, 33} classes (since 𝔽_32 has Galois group ℤ/5 over 𝔽_2). σ_field preserves all 6 cyclic G-classes setwise → **σ_field ∈ K_cyc** ✓

### K_O and Stab per cyclic G-class

For each cyclic G-class of order $n$, compute K_O = $\\{k \\in (ℤ/n)^* : \\sigma_{\\text{field}}(g) \\sim_G g^k\\}$ and Stab = $\\{k : g^k \\sim_G g\\}$:

| $n$ | K_O | Stab |
|---:|---|---|
| 2 | {1} | {1} |
| 3 | {1, 2} | {1, 2} |
| 11 | {2, 9} | {1, 10} |
| 31 | {2, 29} | {1, 30} |
| 33 | {2, 31} | {1, 32} |

Each Stab is exactly $\\langle -1 \\rangle$, each K_O is $\\{2, -2\\}$ (= $\\langle -1 \\rangle \\cdot 2$). Same shape across all $n$.


### Globally: Γ and Image

$\\exp(G) = \\text{lcm}(2, 3, 11, 31, 33) = 2046 = 2 \\cdot 3 \\cdot 11 \\cdot 31$.

$|(ℤ/2046)^*| = \\varphi(2046) = 1 \\cdot 2 \\cdot 10 \\cdot 30 = 600$.

Combine Stab globally: $k$ such that $k \\bmod n \\in \\text{Stab}[n]$ for every $n$. Direct enumeration over $\\{k \\in [0, 2046) : \\gcd(k, 2046) = 1\\}$ gives **|Stab| = 4**, namely $\\{1, 991, 1055, 2045\\}$. Identifying via CRT:
- $1 \\equiv (1, 1, 1, 1)$ mod $(2, 3, 11, 31)$
- $991 \\equiv (1, 1, 1, -1)$
- $1055 \\equiv (1, 1, -1, 1)$  
- $2045 \\equiv (1, 1, -1, -1)$ — i.e., the trivial element of $(ℤ/2)^* = 1$ times $\\langle -1 \\rangle$ on each of the 11-, 31-, and constant-on-3 components.

**Wait —** Stab on $(ℤ/3)^*$ is the entire group $\\{1, 2\\}$, not $\\{1\\}$. So the 3-component of Stab is $\\langle -1 \\rangle = \\{1, 2\\}$, but $-1 \\equiv 2$ so this contributes 2 elements. But the global enumeration above shows only 4 Stab elements, which means... the constraint is consistent and the 3-component is "absorbed": every Stab element has $k \\equiv 1$ or $2$ mod 3. Indeed all four global Stab elements split: $\\{1, 1055\\}$ have $k \\equiv 1 \\bmod 3$, $\\{991, 2045\\}$ have $k \\equiv 2 \\bmod 3$. ✓

Combine K_O globally: **|K_O global| = 4**, $\\{959, 1021, 1025, 1087\\}$ — exactly one Stab-coset.

$|Γ| = \\varphi(2046) / |\\text{Stab}| = 600 / 4 = \\mathbf{150}$.

The representative $k = 959 \\equiv (1, 2, 2, 29) \\equiv (1, -1, 2, -2)$ mod $(2, 3, 11, 31)$. Hmm — let me check: $\\sigma_{\\text{field}}$ should give $k \\equiv 2$ uniformly on every component. $959 \\bmod 11 = 959 - 87 \\cdot 11 = 959 - 957 = 2$ ✓. $959 \\bmod 31 = 959 - 30 \\cdot 31 = 959 - 930 = 29 = -2$ — modulo Stab's $-1$ at the 31-component, this is the same Stab-coset as $k = 2$. ✓

**Order of [959] in Γ:** smallest $j > 0$ with $959^j \\in \\text{Stab}$. Computed: **5 = d** ✓.

**Index $[Γ : \\text{Image}] = 150 / 5 = \\mathbf{30}$.** 

Closed-form prediction: $\\varphi(31) \\cdot \\varphi(33) / (4 \\cdot 5) = 30 \\cdot 20 / 20 = 30$. ✓ **MATCH.**


### The closed-form theorem (proof)

**Theorem (n.319).** Let $G = \\text{PSL}(2, q)$, $q = 2^d$, $d \\geq 2$. Let $\\Gamma(G)$ be the subgroup of $\\text{Sym}(\\text{Conj}\\, G)$ generated by power maps $[g] \\mapsto [g^k]$ for $k \\in (ℤ/\\exp G)^*$, equivalently $\\text{Gal}(ℚ(\\chi_G)/ℚ)$ via Brauer's permutation lemma. Let $\\text{Image}$ be the image of $K_{\\text{cyc}}(G)/\\text{Inn}(G) \\hookrightarrow \\Gamma(G)$.

Then $\\text{Image}$ is cyclic of order $d$, generated by the Frobenius substitution $\\zeta \\mapsto \\zeta^2$ acting uniformly on every cyclotomic factor of $ℚ(\\chi_G)$, and:

$$
[\\Gamma(G) : \\text{Image}] = \\frac{\\varphi(q-1) \\cdot \\varphi(q+1)}{4d}.
$$

**Proof.**

**(1) Structure of $\\exp(G)$.** Element orders of PSL(2, $2^d$) are: 1 (identity), 2 (involutions), $n \\mid q - 1$ (split torus), or $n \\mid q + 1$ (non-split torus). For $q$ even, $q-1$ and $q+1$ are odd and differ by 2, so $\\gcd(q-1, q+1) = \\gcd(q-1, 2) = 1$. Hence $\\exp(G) = 2(q-1)(q+1)$ with the three factors pairwise coprime, and:

$$
(ℤ/\\exp G)^* \\;\\cong\\; (ℤ/2)^* \\times (ℤ/(q-1))^* \\times (ℤ/(q+1))^* \\;=\\; 1 \\times (ℤ/(q-1))^* \\times (ℤ/(q+1))^*.
$$

**(2) Cyclic G-classes.** For each divisor $n$ of $q-1$ (resp. $q+1$), there is exactly one cyclic G-class of order $n$: split torus is cyclic of order $q-1$ (resp. non-split is cyclic of order $q+1$), all maximal split (resp. non-split) tori are G-conjugate, and the Weyl group $\\langle w \\rangle = \\langle u \\leftrightarrow u^{-1} \\rangle$ acts.

**(3) Stab and K_O at each $n$.** For $g$ a generator of order $n$ (in either torus), $g^k \\sim_G g$ iff $k \\equiv \\pm 1 \\pmod{n}$ (since within a fixed torus only the Weyl element $w$ produces nontrivial conjugation, sending $g \\mapsto g^{-1}$). So **Stab[$n$] = $\\langle -1 \\rangle \\subset (ℤ/n)^*$**.

σ_field acts on the torus generator by $u \\mapsto u^2$, so $\\sigma_{\\text{field}}(g) = g^2$ up to G-conjugacy. **K_O[$n$] = $\\langle -1 \\rangle \\cdot \\{2\\} = \\{2, -2\\} \\bmod n$.**

**(4) Globally via CRT.** $(ℤ/(q-1))^* \\times (ℤ/(q+1))^*$ embeds into $(ℤ/\\exp G)^*$. Stab globally = $\\langle -1 \\bmod (q-1) \\rangle \\times \\langle -1 \\bmod (q+1) \\rangle$ (the trivial $(ℤ/2)^*$ factor contributes nothing). Order $2 \\times 2 = \\mathbf{4}$.

**(5) $|\\Gamma|$.** $|\\Gamma| = \\varphi(\\exp G) / |\\text{Stab}| = \\varphi(q-1) \\cdot \\varphi(q+1) / 4$.

**(6) Order of Image.** Image is generated by $([2 \\bmod q-1], [2 \\bmod q+1]) \\in \\Gamma_{q-1} \\times \\Gamma_{q+1}$ where $\\Gamma_m := (ℤ/m)^* / \\langle -1 \\rangle$. Compute orders:

- In $\\Gamma_{q-1}$: $2^d = q \\equiv 1 \\pmod{q-1}$, so $\\text{ord}(2) \\mid d$ in $(ℤ/(q-1))^*$. The element $-1$ is in $\\langle 2 \\rangle$ iff $2^j \\equiv -1$ for some $j$, iff $2^j + 1 \\equiv 0 \\pmod{q-1}$ with $1 \\leq j \\leq d-1$. For $d \\geq 3$: $2^j + 1 \\leq 2^{d-1} + 1 < 2^d - 1 = q-1$, so no such $j$ exists. Hence $\\text{ord}([2] \\text{ in } \\Gamma_{q-1}) = d$ for $d \\geq 3$. (For $d = 2$: $2 \\equiv -1 \\pmod{3}$, so $[2] = [1]$ in $\\Gamma_3$, order 1.)
- In $\\Gamma_{q+1}$: $2^d = q \\equiv -1 \\pmod{q+1}$, so $2^d \\in \\langle -1 \\rangle$ but $2^j \\not\\equiv \\pm 1$ for $j < d$ (since $2^j < q+1$ and $2^j \\neq 1$ trivially, and $2^j = q$ requires $j = d$). Hence $\\text{ord}([2] \\text{ in } \\Gamma_{q+1}) = d$ for all $d \\geq 2$.

So $\\text{ord}(\\text{Image}) = \\text{lcm}(d', d) = d$ where $d' \\in \\{1, d\\}$.

**(7) Index.** $[\\Gamma : \\text{Image}] = |\\Gamma| / d = \\varphi(q-1) \\varphi(q+1) / (4d)$. $\\blacksquare$

