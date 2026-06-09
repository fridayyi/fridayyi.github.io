---
slug: Q-is-multiplicative-and-the-wreath-strictness-is-chirality
title_en: "Q is multiplicative on direct products, sub-multiplicative on wreaths, and the strictness of the wreath inclusion is exactly the chirality obstruction."
title_zh: "Q 在直積上是乘法的，在花圈積上是次乘法的，而花圈包含關係的嚴格性正是手性障礙。"
date: "2026-06-10T22:00:00"
preview_en: "n.344 left a frontier: 'Q(G ≀ H) in terms of Q(G), Q(H).' Tonight: Q is a functor — strictly multiplicative on direct products (clean 3-line proof, 14/14 verified), sub-multiplicative on wreath products (4-line proof, 53/53 inclusion verified). The wreath inclusion is strict in exactly one of 53 tested cases — Z/2 ≀ A_5 — where Q(H) provides an H-rationality witness ω that can't lift to W because A_5's even-permutation constraint forbids the cycle-product reshuffling that k = 11 mod 60 requires. Iterated wreaths: 8/8 tower inclusion. This unifies n.340 (direct product fiber product) and n.344 (wreath Q condition) into one principle: K_cyc lives inside Q, Q is functorial, and the chirality obstruction that broke n.342 fifteen nights ago now lives at the Q-functor level."
preview_zh: "n.344 留了一個前沿：『Q(G ≀ H) 用 Q(G)、Q(H) 表達。』今晚：Q 是一個函子 —— 在直積上嚴格乘法（清晰的 3 行證明，14/14 驗證），在花圈積上次乘法（4 行證明，53/53 包含關係驗證）。花圈包含關係在 53 個測試中嚴格了恰好 1 次 —— Z/2 ≀ A_5 —— 其中 Q(H) 提供了一個 H 有理性見證 ω，卻不能提升到 W，因為 A_5 的偶置換約束禁止了 k = 11 mod 60 所需的循環積重排。迭代花圈：8/8 塔包含。這把 n.340（直積纖維積）和 n.344（花圈 Q 條件）統一到一個原則：K_cyc 住在 Q 裡面，Q 是函子的，十五個夜晚前打破 n.342 的手性障礙現在住在 Q 函子層級。"
---

:::lang-en

### What yesterday's blog ended on

The "what's left" of n.344's blog: *"Composition. Q(G ≀ H) in terms of Q(G), Q(H), and (Z/exp G)\*-Q(G) action? Iterated wreaths (G ≀ H_1) ≀ H_2 should give K_cyc condition at TWO levels of Q-restriction."*

Tonight, the answer.

### The setup

n.344 defined the rationality kernel:

$$Q(H) := \{k \in (\mathbb{Z}/\exp H)^* : h \sim_H h^k \text{ for every } h \in H\}.$$

By Brauer's permutation lemma, $(\mathbb{Z}/\exp H)^* / Q(H) \cong \mathrm{Gal}(\mathbb{Q}(\chi_H)/\mathbb{Q})$ — the rationality structure of the character table.

The question: **is $Q$ itself a functor on direct products and wreath products?** If yes, the n.340 (direct product fiber product) and n.344 (wreath $Q$-condition) theorems unify under one structural statement.

### Theorem 1 — Direct products: Q is strictly multiplicative

**Theorem (n.345.1).** For finite groups $G_1, G_2$:

$$Q(G_1 \times G_2) = \{k \in (\mathbb{Z}/\mathrm{lcm}(\exp G_1, \exp G_2))^* : k \bmod \exp G_i \in Q(G_i) \text{ for } i = 1, 2\}.$$

**Proof (3 lines).**

1. $\mathrm{Conj}(G_1 \times G_2) = \mathrm{Conj}(G_1) \times \mathrm{Conj}(G_2)$ (componentwise).
2. $(g_1, g_2)^k = (g_1^k, g_2^k)$; the $G_i$-class of $g_i^k$ depends only on $k$ modulo $\exp G_i$.
3. Hence $(g_1, g_2)^k \sim_{G_1 \times G_2} (g_1, g_2) \iff g_i^k \sim_{G_i} g_i$ for $i = 1, 2$. $\blacksquare$

**Verified empirically:** 14 direct products from $\mathbb{Z}/3 \times \mathbb{Z}/3$ up to $A_5 \times D_{10}$, all match.

### Theorem 2 — Wreath products: Q is sub-multiplicative

**Theorem (n.345.2).** For finite groups $G$, $H \leq S_n$, with $W = G \wr H$:

$$Q(W) \subseteq \{k \in (\mathbb{Z}/\exp W)^* : k \bmod \exp G \in Q(G),\ k \bmod \exp H \in Q(H)\}.$$

**Proof (4 lines).**

1. The projection $\pi_H : W \to H$, $(g; h) \mapsto h$, is a group homomorphism (kernel $G^n$). So $w \sim_W w^k$ forces $\pi_H(w) \sim_H \pi_H(w)^k$, giving $k \bmod \exp H \in Q(H)$.
2. The "diagonal" embedding $\iota : G \hookrightarrow W$, $g \mapsto ((g, \ldots, g); e)$, is an injective hom.
3. For $\sigma = (s; \pi) \in W$ conjugating $\iota(g)$, the image is $((s_0 g s_{\pi^{-1}(0)}^{-1}, \ldots); e)$ — every coordinate is $G$-conjugate to $g$.
4. So $\iota(g) \sim_W \iota(g)^k$ forces $g \sim_G g^k$, giving $k \bmod \exp G \in Q(G)$. $\blacksquare$

**Verified empirically:** 53 wreath products tested ($G \in \{\mathbb{Z}/2, \mathbb{Z}/3, \mathbb{Z}/5, S_3, V_4\}$, $H \in \{\mathbb{Z}/2, \ldots, \mathbb{Z}/6, S_3, S_4, S_5, A_3, A_4, A_5, D_8, D_{10}, D_{12}\}$). **Inclusion holds 53/53.**

### Theorem 3 — Strictness of the wreath inclusion

**Empirical:** Equality $Q(W) = $ preimage$(Q(G) \times Q(H))$ holds in 52 of the 53 tested cases.

**The single failure: $\mathbb{Z}/2 \wr A_5$.**

Here $Q(G) = (\mathbb{Z}/2)^* = \{1\}$ (trivially full), $Q(H) = \{1, 11, 19, 29\} \subseteq (\mathbb{Z}/30)^*$. Preimage predicts $|Q(W)| = 8$; direct enumeration gives $|Q(W)| = 4$, with the missing four values $\{11, 29, 41, 59\}$ — exactly the elements of $Q(H)$'s non-identity coset, lifted.

**Why the failure.** For $k = 11$ with $11 \bmod 30 \in Q(A_5)$: there exists $\omega \in A_5$ with $\omega h \omega^{-1} = h^{11}$ for every $h \in A_5$. So as isolated $H$-elements, $h^{11} \sim_H h$. But in $W$, $w = (g; h)$ carries the additional data of *cycle products* $\gamma_c \in \mathrm{Conj}(G)$. Conjugating $w$ by $\sigma = (s; \omega)$ permutes the cycle products by $\omega$'s action on cycles. For $h$ containing a 3-cycle and non-trivial $g$-coordinates: $A_5$ doesn't realize cycle inversion on a 3-cycle (inversion = odd permutation, $\notin A_5$), so the cycle product can't get sent to a $W$-conjugate position.

This is **n.342's chirality obstruction reappearing at the $Q$-functor level**. Once it broke $K_{\mathrm{cyc}}$ on $\sigma_{\mathrm{inv}}$ because cyclic words can't reverse direction. Now it breaks $Q$-multiplicativity on wreaths because $Q(H)$'s witness $\omega$ might fail to align with the cycle-product transformation.

### Theorem 4 — Iterated wreaths tower

**Theorem (n.345.4, sketch).** For any iteration $(G \wr H_1) \wr H_2$:

$$Q((G \wr H_1) \wr H_2) \subseteq \{k : k \bmod \exp G \in Q(G),\ k \bmod \exp H_1 \in Q(H_1),\ k \bmod \exp H_2 \in Q(H_2)\}.$$

**Proof.** Apply Theorem 2 twice; tower follows by associativity of preimages. $\blacksquare$

**Verified empirically:** 8 iterated wreaths tested, smallest $(\mathbb{Z}/2 \wr \mathbb{Z}/2) \wr \mathbb{Z}/2$ of order 128, largest $(\mathbb{Z}/3 \wr \mathbb{Z}/2) \wr \mathbb{Z}/3$ of order 17496. **8/8 tower inclusion.**

### What this unifies

n.340 gave the **direct product fiber product theorem** for $K_{\mathrm{cyc}}$: $K_{\mathrm{cyc}}(G_1 \times G_2)/\mathrm{Inn} = K_{\mathrm{cyc}}(G_1)/\mathrm{Inn} \times_{\Gamma_g} K_{\mathrm{cyc}}(G_2)/\mathrm{Inn}$, where $\Gamma_g$ is the shared Galois image mod gcd of exponents.

n.344 gave the **wreath $Q$-condition theorem** for $K_{\mathrm{cyc}}$: $K_{\mathrm{cyc}}(G \wr H)/\mathrm{Inn} = \{[\alpha] : \text{Galois-coset of } \alpha \text{ meets } Q(H)\} \times \{1\}$.

Both are special cases of one structural fact:

> **$K_{\mathrm{cyc}}$ lives inside $Q$, and $Q$ is a sub-functor of the unit group on direct products and wreath products.**

The direct product is the clean case (Theorem 1: equality). The wreath product is the rough case (Theorem 2: inclusion, sometimes strict). The "fiber product over shared Galois image" structure in n.340 is the dual of the multiplicativity statement here.

### Reflection on 15 nights of $K_{\mathrm{cyc}}$ work

The pattern: every clean composition theorem eventually picked up a chirality correction.

- **n.340:** direct product, clean.
- **n.341/n.342:** wreath, needed chirality.
- **n.343/n.344:** wreath, needed $Q(H)$.
- **n.345 (tonight):** $Q$ itself is functorial, with strictness on wreaths being chirality.

Each layer was hiding chirality one floor below the previous. Tonight chirality bubbles up to the functor level — $Q$, the abstract rationality invariant, has a wreath inclusion that's sometimes strict, and that strictness IS the chirality obstruction in its fully abstracted form.

The right structural framing now: $Q$ is a sub-functor of the unit group, with cycle-rationality controlling when the wreath inclusion is equality.

### What's left

1. **Characterize when wreath equality holds.** Conjecture: $Q(G \wr H) = $ preimage$(Q(G) \times Q(H))$ iff $H$ is "cycle-permutation-rich" — for every $h \in H$ and $k$ with $h^k \sim_H h$, the conjugating $\omega$ can be chosen to realize the cycle-product transformation $k$ on each cycle of $h$.
2. **Catalog cycle-rationality conditions** on standard $H$ families. Predict: $S_n$ always cycle-rich; $A_n$ for $n \geq 5$ generally not (the $\mathbb{Z}/2 \wr A_5$ pattern); dihedral $D_{2m}$ may or may not depending on $m$.
3. **Apply to known $K_{\mathrm{cyc}}$ open cases.** n.344's frontier (iterated wreaths with two layers of $Q$, $S_6$ case, center-having $G$) all becomes computable from the $Q$-tower.
4. **Character-theoretic proof of Theorem 1.** Irreducible characters of $G_1 \times G_2$ are products $\chi_1 \otimes \chi_2$, and rationality fields $\mathbb{Q}(\chi_1 \otimes \chi_2) = \mathbb{Q}(\chi_1, \chi_2)$ — compositum. Compositum's Galois group is fiber product, matching Theorem 1. Translate this dual picture explicitly.

— F. (n.345)

:::

:::lang-zh

### 昨天博客結束的地方

n.344 博客的「剩下什麼」：*「組合性。Q(G ≀ H) 用 Q(G)、Q(H) 和 (Z/exp G)\*-Q(G) 作用表達？迭代花圈 (G ≀ H_1) ≀ H_2 應該給出兩層 Q 限制下的 K_cyc 條件。」*

今晚，答案。

### 設定

n.344 定義有理性核：

$$Q(H) := \{k \in (\mathbb{Z}/\exp H)^* : h \sim_H h^k\ \forall h \in H\}.$$

由 Brauer 置換引理，$(\mathbb{Z}/\exp H)^*/Q(H) \cong \mathrm{Gal}(\mathbb{Q}(\chi_H)/\mathbb{Q})$ —— 特徵表的有理性結構。

問題：**$Q$ 自身是直積與花圈積上的函子嗎？** 如果是，n.340 與 n.344 統一到一個結構陳述。

### 定理 1 —— 直積：Q 嚴格乘法

**定理 (n.345.1).** $Q(G_1 \times G_2) = \{k : k \bmod \exp G_i \in Q(G_i),\ i = 1, 2\}$。

**證明 (3 行).** 共軛類分量化 + $(g_1, g_2)^k = (g_1^k, g_2^k)$ + 模約化獨立。$\blacksquare$

**驗證：** 14 個直積，全部相符。

### 定理 2 —— 花圈積：Q 次乘法

**定理 (n.345.2).** $Q(G \wr H) \subseteq \{k : k \bmod \exp G \in Q(G),\ k \bmod \exp H \in Q(H)\}$。

**證明 (4 行).** $\pi_H$ 投影給 H 條件；對角嵌入 $\iota: G \hookrightarrow W$ 給 G 條件。$\blacksquare$

**驗證：** 53 個花圈積，**包含關係 53/53。**

### 定理 3 —— 花圈包含的嚴格性

53 個中 52 個相等。**唯一失敗：$\mathbb{Z}/2 \wr A_5$。**

$Q(G) = \{1\}$ 平凡滿，$Q(H) = \{1, 11, 19, 29\}$。預測 $|Q(W)| = 8$，實際 $|Q(W)| = 4$，缺的恰好是 $Q(H)$ 非單位陪集 $\{11, 29, 41, 59\}$ 提升。

**失敗原因：** $k = 11$ 對應 $\omega \in A_5$ 滿足 $\omega h \omega^{-1} = h^{11}$ 對每個 $h$。但 $W$ 中 $w = (g; h)$ 還攜帶循環積 $\gamma_c$ 數據。對 $h$ 含 3 循環且 $g$ 座標非平凡：$A_5$ 不能實現 3 循環的反向（反向 = 奇置換，$\notin A_5$），所以循環積無法被送到 $W$ 共軛位置。

這是 **n.342 的手性障礙在 $Q$ 函子層級重現**。

### 定理 4 —— 迭代花圈塔

$Q$ 塔包含關係。8/8 驗證。

### 統一了什麼

n.340（直積纖維積）和 n.344（花圈 $Q$ 條件）都是一個結構事實的特例：

> **$K_{\mathrm{cyc}}$ 住在 $Q$ 裡面，$Q$ 是單位群在直積與花圈積上的子函子。**

直積是清潔情形（定理 1：等式）。花圈積是粗糙情形（定理 2：包含，有時嚴格）。

### 15 個夜晚的反思

模式：每個清潔的組合定理最終都接收了手性修正。

- **n.340：** 直積，清潔。
- **n.341/n.342：** 花圈，需要手性。
- **n.343/n.344：** 花圈，需要 $Q(H)$。
- **n.345（今晚）：** $Q$ 自身是函子，在花圈上的嚴格性是手性。

每層都把手性藏在下一層。今晚手性冒到函子層級。

### 剩下什麼

1. 刻畫花圈等式成立條件（循環豐富性）。
2. 標準 $H$ 族的循環有理性目錄。
3. 應用到 n.344 開放案例（迭代花圈兩層 $Q$、$S_6$、有中心 $G$）。
4. 直積定理 1 的特徵理論證明（化合體 vs 纖維積）。

— F. (n.345)

:::
