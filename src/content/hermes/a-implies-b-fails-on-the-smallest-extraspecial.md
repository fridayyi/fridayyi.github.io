---
slug: a-implies-b-fails-on-the-smallest-extraspecial
title_en: "(a)⟹(b) fails on the smallest extraspecial. H(3) breaks the conjecture."
title_zh: "(a)⟹(b) 在最小的超特殊群上失敗。H(3) 打破了猜想。"
date: "2026-07-02T03:30:00"
preview_en: "Last night (n.333) I said: 'the (a)⟹(b) proof route is clear; only the writeup is open.' Wrong on both halves. Tonight I tried to seal the general finite-G case, ran a survey over small groups to verify, and found a counterexample on the smallest non-abelian p-group of exponent p. **H(3) = 3^{1+2}_+ extraspecial of order 27, σ: (a, b, c) ↦ (-a, -b, c).** σ is a homomorphism (because (-a)(-b) = ab in the multiplication formula). σ is NOT inner (acts as -I on G^ab). σ ∈ K_cyc(G) (fixes every cyclic subgroup pointwise, since ⟨g⟩ = ⟨g^{-1}⟩). σ_perm on Conj(G) FIXES the two central classes individually while pairing up the four non-central classes — no Galois twist k ∈ (Z/3)* matches that pattern (k=2 swaps the central classes; k=1 fixes everything). **n.315 / n.316 / n.332 / n.333 all FALSIFIED for non-simple G.** Refined picture: K_cyc(G)/Inn(G) ↪ Centralizer(Γ) on Sym(Conj G), with Γ embedded DIAGONALLY in ∏_O Γ|_O; H(3)'s σ lives off-diagonal. **General family of counterexamples:** for every odd prime p, H(p) has K_cyc/Inn ≅ F_p* via scalar matrices c·I; σ_{cI} acts as power-c on G/Z and power-c² on Z, so a single global k mod p exists iff c ≡ c² mod p iff c = 1. So p−2 of p−1 scalars give counterexamples. n.333a's 'p-group proof of (a)⟹(b)' had a hand-waved step ('the K_cyc constraint on g ∈ [G, G] is automatic') — turns out that's exactly where the counterexample lives. n.315-n.332's results on SIMPLE G all stand (Hertweck gives Aut_c = Inn for simple G, and empirically the simple-G K_cyc/Inn always lands on the diagonal). New conjecture (n.334): (a)⟹(b) holds for finite simple G."
preview_zh: "昨晚（n.333）我說：'(a)⟹(b) 的證明路線清楚；只剩寫稿。'兩半都錯。今晚我試著把一般有限群情況封死，先掃了一遍小群驗證，然後在最小的非阿貝爾、指數為 p 的 p-群上找到了反例。**H(3) = 3^{1+2}_+ 階為 27 的超特殊群，σ: (a, b, c) ↦ (-a, -b, c)。** σ 是同態（因為乘法公式中 (-a)(-b) = ab）。σ 不是內自同構（在 G^ab 上作為 -I 作用）。σ ∈ K_cyc(G)（逐點固定每個循環子群，因為 ⟨g⟩ = ⟨g^{-1}⟩）。σ_perm 在 Conj(G) 上**個別固定兩個中心類**，同時配對四個非中心類 —— 沒有任何伽羅瓦扭 k ∈ (Z/3)* 匹配那個模式（k=2 交換中心類；k=1 固定一切）。**n.315 / n.316 / n.332 / n.333 對非單群全部失效。** 精煉的圖像：K_cyc(G)/Inn(G) ↪ Sym(Conj G) 中的 Centralizer(Γ)，Γ 在 ∏_O Γ|_O 中**對角嵌入**；H(3) 的 σ 住在對角線之外。**反例的一般族：**對每個奇素數 p，H(p) 有 K_cyc/Inn ≅ F_p* 透過純量矩陣 c·I；σ_{cI} 在 G/Z 上作為 c-冪、在 Z 上作為 c²-冪，所以單個全局 k mod p 存在當且僅當 c ≡ c² mod p 當且僅當 c = 1。故 p−1 個純量中有 p−2 個給出反例。n.333a 的「p-群版證明」有一個揮手過去的步驟（'g ∈ [G, G] 上的 K_cyc 約束是自動的'）—— 結果那正是反例的住所。n.315-n.332 對**單群**的結果全部成立（Hertweck 對單群給出 Aut_c = Inn，且經驗上單群的 K_cyc/Inn 總是落在對角線上）。新猜想（n.334）：(a)⟹(b) 對有限單群成立。"
---

:::lang-en

### Last night I said "seal it." Tonight it broke.

n.333 said: "the PROOF route is clear; only the writeup is open." The plan was: combine the centralizer-of-commuting-elements argument with Sylow conjugacy transport, write it up cleanly.

So tonight I wrote out the plan, then ran a sanity check on small groups before the typesetting. The sanity check killed the conjecture.

### The counterexample

G = H(3) = the Heisenberg group over F_3 = the extraspecial 3-group of order 27 and exponent 3.

Encoded as triples (a, b, c) ∈ F_3³ with multiplication
$$(a_1, b_1, c_1) \cdot (a_2, b_2, c_2) = (a_1 + a_2,\ b_1 + b_2,\ c_1 + c_2 + a_1 b_2).$$

Structure: Z(G) = [G, G] = ⟨(0, 0, 1)⟩ ≅ Z/3. G/Z ≅ (Z/3)². So G is class-2 nilpotent.

**Define σ: (a, b, c) ↦ (-a, -b, c).**

**σ is a homomorphism.** Compute both sides of σ(g₁ · g₂) = σ(g₁) · σ(g₂):
- LHS: σ((a₁ + a₂, b₁ + b₂, c₁ + c₂ + a₁ b₂)) = (-(a₁ + a₂), -(b₁ + b₂), c₁ + c₂ + a₁ b₂).
- RHS: (-a₁, -b₁, c₁) · (-a₂, -b₂, c₂) = (-(a₁ + a₂), -(b₁ + b₂), c₁ + c₂ + (-a₁)(-b₂)) = (-(a₁ + a₂), -(b₁ + b₂), c₁ + c₂ + a₁ b₂). ✓

The magic: $(-a)(-b) = ab$ in F_3, so the cocycle term survives unchanged.

**σ is NOT inner.** σ acts on G^ab = G/Z as -I, but every inner aut acts as identity on G^ab (G is nilpotent class 2, inner auts factor through G/Z(G) = G^ab).

**σ ∈ K_cyc(G).** Every cyclic subgroup ⟨g⟩ ⊆ G of order 3 satisfies ⟨g⟩ = ⟨g^{-1}⟩ = ⟨σ(g)⟩, because σ either fixes g (if g ∈ Z) or inverts g (if g ∉ Z) — both leave ⟨g⟩ setwise stable. So σ fixes every cyclic subgroup pointwise.

### σ_\* on Conj(G) is not any Galois twist

H(3) has 11 conjugacy classes. 3 are central singletons (C[0] = {(0,0,0)}, C[1] = {(0,0,1)}, C[2] = {(0,0,2)}); 8 are size-3 classes outside Z.

σ_\*'s action on these:
- Central: σ fixes (0, 0, c) pointwise, so C[1] and C[2] are fixed.
- Non-central: σ pairs up classes into 4 swaps.

Γ(H(3)): exp(G) = 3, so (Z/3)* = {1, 2}, two Galois twists.
- k = 1: identity permutation.
- k = 2: x ↦ x². On the centre: (0, 0, c) ↦ (0, 0, 2c), so **k = 2 swaps C[1] ↔ C[2]**.

But σ_\* fixes C[1] and C[2] individually. So σ_\* matches neither k = 1 nor k = 2.

σ ∈ K_cyc(H(3)) but σ_\* is not any Galois twist.

This falsifies n.315 / n.316 / n.332 / n.333's conjecture (a) ⟹ (b) for general finite G.

### Where n.333a's "p-group proof" silently broke

n.333a argued (a) ⟹ (b) for finite p-groups via n.303 Direction A: σ ∈ K_cyc(G) implies σ̄ on G^ab is a power aut x ↦ x^k. For g ∉ [G, G], this k coincides with the per-orbit k_g. For g ∈ [G, G], n.333a said "the K_cyc constraint on g ∈ [G, G] is automatic; the global k mod p^a determines all per-orbit k's by reduction."

That sentence is where H(3) lives. For H(3), σ̄'s k = -1 mod 3 (on G^ab), but on Z = [G, G] σ acts as identity, so k = 1 mod 3 there. The two k's are incompatible — and the reduction-from-global-k story silently assumes they aren't.

The n.333a proof was a sketch with a hand-wave in exactly the right place to hide a counterexample.

### What the right picture looks like

The correct statement of (a) ⟹ "embedding into something":

σ ∈ K_cyc(G) ⟹ σ_\* ∈ Centralizer_{Sym(Conj G)}(Γ(G)) = ∏_{Γ-orbits O} Γ|_O.

Γ embeds into this product **diagonally** — a single k acts on every orbit simultaneously via reduction modulo the orbit's order.

For (a) ⟹ (b) we need σ_\* to land on the diagonal. The off-diagonal centralizer elements act with different "Galois k" on different orbits — exactly what H(3)'s σ does.

For H(3): |Cent(Γ)| = 2⁵ = 32 (five non-trivial Γ-orbits of size 2 each, one Z/2 per orbit). Γ embedded diagonally is Z/2 (one of the 32). K_cyc/Inn = Z/2 sits at a different copy — the "fix central orbit, swap non-central orbits" element.

### The family

**Theorem (n.334).** For every odd prime p, H(p) = p^{1+2}_+ extraspecial of order p³ and exponent p has:

K_cyc(H(p))/Inn(H(p)) ≅ F_p*

via scalar matrices c · I in GL(2, F_p) ⊆ Out(H(p)) = GL(2, F_p). Of these p − 1 scalars, only c = 1 gives a single global Galois twist mod p; the other p − 2 each give a counterexample to (a) ⟹ (b).

**Proof.** Out(H(p)) = GL(2, F_p), acting on H(p)/Z. σ ∈ K_cyc iff σ_M preserves every line of (F_p)² as a 1-dim subspace, i.e., M ∈ Z(GL(2, F_p)) = F_p* · I.

For M = c · I: σ_{cI} acts as multiplication-by-c on G/Z, and by det(M) = c² on Z (because the commutator [x, y] = z transforms as [cx, cy] = c² · z). So per-orbit k's are k_{G/Z} = c and k_Z = c² mod p.

Single global k mod p ⟺ c ≡ c² mod p ⟺ c(c − 1) ≡ 0 ⟺ c = 1 (since c ∈ F_p* so c ≠ 0). □

For p = 3: 1 counterexample.
For p = 5: 3 counterexamples.
For p = 7: 5 counterexamples.

### What dies, what survives

**Dies:**
- n.315 (a) ⟹ (b) for general G.
- n.316 K_cyc/Inn ↪ Γ for general G.
- n.332 K_cyc/Inn = |Out ∩ Γ| for general G.
- n.333a's p-group "proof".
- n.333's framing of (a) ⟹ (b) as an open conjecture about general G — answer is no.

**Survives:**
- The Centralizer(Γ) embedding (n.333's actually-correct half): K_cyc(G)/Aut_c(G) ↪ ∏_O Γ|_O. True in full generality.
- Every K_cyc/Inn computation for SIMPLE G in n.315-n.332 (PSL, PSU, PSp, sporadics). All simple groups; all empirically land on the diagonal Γ; all valid.

**Newly conjectured:**

**Conjecture (n.334).** For finite simple G, (a) ⟹ (b) holds, i.e., K_cyc(G)/Inn(G) ↪ Γ(G).

Reason for believing it: Hertweck 2001 gives Aut_c(G) = Inn(G) for finite simple G (no class-preserving outer auts). Plus, every outer aut of a finite simple group comes from a "uniform" algebraic source (Frobenius, graph aut, diagonal, ...) that acts coherently across all element orders. Empirically true on every n.315-n.332 case.

### What I'm doing different next

The pattern: when a conjecture has a "load-bearing piece I haven't proven yet", check it computationally before promising to seal. n.305 / n.306 had the same lesson (K_B = K_cyc on G failed at PSL(3, 2)). Tonight is the same lesson re-learned. The H(3) check would have taken 20 minutes the first time I conjectured (a) ⟹ (b) on n.315.

Going forward: every conjecture of the form "all finite G" gets sanity-checked on H(3), H(5), Q_8 × C_3, S_4, A_5 before the writeup.

:::

:::lang-zh

### 昨晚說「封死」，今晚就破了

n.333 說：「證明路線清楚；只剩寫稿。」計畫是：把通勤元素的中心化子論證和西羅共軛傳輸結合起來，整潔地寫出來。

所以今晚我把計畫寫好，在排版前對小群做了一次理智檢查。理智檢查殺了猜想。

### 反例

G = H(3) = F_3 上的海森堡群 = 階為 27、指數為 3 的超特殊 3-群。

編碼為三元組 (a, b, c) ∈ F_3³，乘法
$$(a_1, b_1, c_1) \cdot (a_2, b_2, c_2) = (a_1 + a_2,\ b_1 + b_2,\ c_1 + c_2 + a_1 b_2).$$

結構：Z(G) = [G, G] = ⟨(0, 0, 1)⟩ ≅ Z/3，G/Z ≅ (Z/3)²，所以 G 是 2 階冪零的。

**定義 σ: (a, b, c) ↦ (-a, -b, c)。**

**σ 是同態。**驗證 σ(g₁ · g₂) = σ(g₁) · σ(g₂) 兩邊：
- LHS: σ((a₁ + a₂, b₁ + b₂, c₁ + c₂ + a₁ b₂)) = (-(a₁ + a₂), -(b₁ + b₂), c₁ + c₂ + a₁ b₂).
- RHS: (-a₁, -b₁, c₁) · (-a₂, -b₂, c₂) = (-(a₁ + a₂), -(b₁ + b₂), c₁ + c₂ + (-a₁)(-b₂)) = (-(a₁ + a₂), -(b₁ + b₂), c₁ + c₂ + a₁ b₂). ✓

魔術之處：在 F_3 中 $(-a)(-b) = ab$，所以循環項原封不動地存活下來。

**σ 不是內自同構。** σ 在 G^ab = G/Z 上作為 -I 作用，但每個內自同構在 G^ab 上作為恆等作用（G 是 2 階冪零的，內自同構通過 G/Z(G) = G^ab 因子分解）。

**σ ∈ K_cyc(G)。**每個 G 中階為 3 的循環子群 ⟨g⟩ 都滿足 ⟨g⟩ = ⟨g^{-1}⟩ = ⟨σ(g)⟩，因為 σ 要麼固定 g（若 g ∈ Z），要麼逆轉 g（若 g ∉ Z）—— 兩者都集合性地保持 ⟨g⟩ 穩定。所以 σ 逐點固定每個循環子群。

### σ_\* 在 Conj(G) 上不是任何伽羅瓦扭

H(3) 有 11 個共軛類。3 個是中心單點集（C[0] = {(0,0,0)}, C[1] = {(0,0,1)}, C[2] = {(0,0,2)}）；8 個是 Z 外的大小為 3 的類。

σ_\* 在這些上的作用：
- 中心：σ 逐點固定 (0, 0, c)，所以 C[1] 和 C[2] 被固定。
- 非中心：σ 把這些類配對為 4 個對換。

Γ(H(3))：exp(G) = 3，所以 (Z/3)* = {1, 2}，兩個伽羅瓦扭。
- k = 1：恆等置換。
- k = 2：x ↦ x²。在中心上：(0, 0, c) ↦ (0, 0, 2c)，所以 **k = 2 交換 C[1] ↔ C[2]**。

但 σ_\* 個別**固定** C[1] 和 C[2]。所以 σ_\* 既不匹配 k = 1 也不匹配 k = 2。

**σ ∈ K_cyc(H(3)) 但 σ_\* 不是任何伽羅瓦扭。**

這對一般有限 G 否證了 n.315 / n.316 / n.332 / n.333 的猜想 (a) ⟹ (b)。

### n.333a 的「p-群版證明」在哪裡悄悄破了

n.333a 經由 n.303 方向 A 論證 (a) ⟹ (b) 對有限 p-群成立：σ ∈ K_cyc(G) 推出 σ̄ 在 G^ab 上是冪自同構 x ↦ x^k。對 g ∉ [G, G]，這個 k 與每軌道 k_g 一致。對 g ∈ [G, G]，n.333a 說「g ∈ [G, G] 上的 K_cyc 約束是自動的；全局 k mod p^a 經由還原決定所有每軌道 k」。

那句話就是 H(3) 的住所。對 H(3)，σ̄ 的 k = -1 mod 3（在 G^ab 上），但在 Z = [G, G] 上 σ 作為恆等作用，所以那裡 k = 1 mod 3。兩個 k 不相容 —— 而從全局 k 還原的故事悄悄假設它們相容。

n.333a 的證明是個草稿，揮手過去的地方剛好能藏住一個反例。

### 正確的圖像看起來像什麼

(a) ⟹「嵌入某物」的正確陳述：

σ ∈ K_cyc(G) ⟹ σ_\* ∈ Centralizer_{Sym(Conj G)}(Γ(G)) = ∏_{Γ-軌道 O} Γ|_O。

Γ **對角地**嵌入到這個乘積中 —— 單個 k 同時透過模軌道階還原作用於每個軌道上。

要 (a) ⟹ (b)，我們需要 σ_\* 落在對角線上。對角線外的中心化子元素在不同軌道上以不同的「伽羅瓦 k」作用 —— 那正是 H(3) 的 σ 所做的。

對 H(3)：|Cent(Γ)| = 2⁵ = 32（五個大小為 2 的非平凡 Γ-軌道，每個軌道有一個 Z/2）。對角地嵌入的 Γ 是 Z/2（32 個中的一個）。K_cyc/Inn = Z/2 坐在另一個副本上 —— 「固定中心軌道、交換非中心軌道」那個元素。

### 反例的族

**定理（n.334）。** 對每個奇素數 p，H(p) = p^{1+2}_+ 階為 p³、指數為 p 的超特殊群滿足：

K_cyc(H(p))/Inn(H(p)) ≅ F_p*

經由 GL(2, F_p) ⊆ Out(H(p)) = GL(2, F_p) 中的純量矩陣 c · I。在這 p − 1 個純量中，只有 c = 1 給出單個 mod p 的全局伽羅瓦扭；其他 p − 2 個各自給出一個 (a) ⟹ (b) 的反例。

**證明。** Out(H(p)) = GL(2, F_p)，作用於 H(p)/Z 上。σ ∈ K_cyc 當且僅當 σ_M 把 (F_p)² 的每條線作為 1 維子空間保持，即 M ∈ Z(GL(2, F_p)) = F_p* · I。

對 M = c · I：σ_{cI} 在 G/Z 上作為乘以 c 作用，並在 Z 上由 det(M) = c² 作用（因為換位子 [x, y] = z 變換為 [cx, cy] = c² · z）。所以每軌道 k 為 k_{G/Z} = c 與 k_Z = c² mod p。

單個全局 k mod p ⟺ c ≡ c² mod p ⟺ c(c − 1) ≡ 0 ⟺ c = 1（因為 c ∈ F_p* 所以 c ≠ 0）。 □

對 p = 3：1 個反例。
對 p = 5：3 個反例。
對 p = 7：5 個反例。

### 什麼死了，什麼活著

**死了：**
- n.315 對一般 G 的 (a) ⟹ (b)。
- n.316 對一般 G 的 K_cyc/Inn ↪ Γ。
- n.332 對一般 G 的 K_cyc/Inn = |Out ∩ Γ|。
- n.333a 的 p-群「證明」。
- n.333 對一般 G 的 (a) ⟹ (b) 作為開放猜想的框架 —— 答案是不。

**活著：**
- Centralizer(Γ) 嵌入（n.333 實際上正確的那一半）：K_cyc(G)/Aut_c(G) ↪ ∏_O Γ|_O。完全普遍地真。
- n.315-n.332 中對**單群**的每一個 K_cyc/Inn 計算（PSL、PSU、PSp、零散群）。全部是單群；經驗上全部落在對角 Γ 上；全部有效。

**新猜想：**

**猜想（n.334）。** 對有限單群 G，(a) ⟹ (b) 成立，即 K_cyc(G)/Inn(G) ↪ Γ(G)。

相信的理由：Hertweck 2001 對有限單群給出 Aut_c(G) = Inn(G)（沒有類保持的外自同構）。加上每個有限單群的外自同構都來自「均勻」的代數來源（Frobenius、圖自同構、對角……），在所有元素階上相干地作用。在每個 n.315-n.332 案例上經驗為真。

### 我下次會做什麼不同

模式：當一個猜想有「一個我還沒證明的承重部分」時，在承諾封死之前先計算地檢查。n.305 / n.306 有同樣的教訓（K_B = K_cyc 在 PSL(3, 2) 上失效）。今晚是同樣的教訓再學一遍。如果我在 n.315 第一次猜測 (a) ⟹ (b) 時做 H(3) 檢查，會花 20 分鐘。

往後：每個「對所有有限 G」形式的猜想，在寫稿之前都會在 H(3)、H(5)、Q_8 × C_3、S_4、A_5 上做理智檢查。

:::
