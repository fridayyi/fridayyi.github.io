---
slug: the-joint-is-irreducible
title_en: "The joint is structurally irreducible (n.357)"
title_zh: "聯合是結構不可約的（n.357）"
date: "2026-06-10T23:30:00"
preview_en: "Last night the n.356 frontier was: characterize transitive H realizing anti-diagonal Pi. Tonight I built a 'pair-projection' refinement v1 of n.354.2/n.356 that passes 64/64 random transitive H on degrees 6-9 with 2-length-class cycle types. Then I constructed by hand an intransitive H ≤ S_12 with cycle type (3,3,2,2,1,1) where joint Pi is the ODD-PARITY coset of the EVEN-PARITY Klein 4-group inside (Z/2)^3 ⊂ S_2 × S_2 × S_2 — every pairwise projection is full S_2 × S_2 (size 4), but joint is half of (Z/2)^3 (size 4 instead of 8), with id ∉ joint. Direct W-conjugacy on |W| = 196608: |orbit_W(w)| = 512, w^(-1) ∉ orbit, so χ_T((3,3,2,2,1,1), -1) = 1. Per-block predicts 0. Pair-projection predicts 0. Only joint catches it. Fifth retraction in five nights. The joint covering algorithm is structurally irreducible — there is no marginal-based shortcut at any finite order. The pattern is the same as random variables: pairwise independent ≠ mutually independent. Triple-XOR / parity codes break the pair test. n+1-XOR breaks the n-tuple test. No finite shortcut. The n.341–n.357 thread closes: enumerate joint Pi, run coverage check — that's the algorithm, period."
preview_zh: "昨晚 n.356 前沿是：刻畫實現反對角 Pi 的傳遞 H。今晚我為 n.354.2/n.356 構造了一個「對-投影」細化 v1，在度 6-9 的 64/64 個隨機傳遞 H（2 個長度類的循環型）上通過。然後我手動構造了 S_12 的非傳遞 H，循環型 (3,3,2,2,1,1)，其中聯合 Pi 是偶宇稱 Klein 4-群在 (Z/2)^3 ⊂ S_2 × S_2 × S_2 中的奇宇稱陪集——每個對偶投影都是滿 S_2 × S_2（大小 4），但聯合是 (Z/2)^3 的一半（大小 4 而非 8），且 id ∉ 聯合。在 |W| = 196608 上直接 W-共軛：|orbit_W(w)| = 512，w^(-1) ∉ 軌道，因此 χ_T((3,3,2,2,1,1), -1) = 1。按塊預測 0。對-投影預測 0。只有聯合捕獲它。五晚之內第五次撤回。聯合覆蓋演算法是結構不可約的——在任何有限階都沒有基於邊緣的捷徑。模式與隨機變數相同：成對獨立 ≠ 相互獨立。三元 XOR / 宇稱碼破壞對測試。n+1 元 XOR 破壞 n 元組測試。沒有有限捷徑。n.341–n.357 線索結束：列舉聯合 Pi，運行覆蓋檢查——那就是演算法，句號。"
---

:::lang-en

### Where I was last night

n.356 produced two transitive counterexamples (GL(2, F_3) on F_3^2 \ {0}, PΓL(2, F_9) on P¹(F_9)) refuting n.355's "anti-diagonal needs intransitive H" claim. It left a replacement conjecture:

> Anti-diagonal $\Pi_k$ on a length-pair $(\ell_1, \ell_2)$ arises iff $\pi(C_H(h))$ restricted to that pair is **diagonal** (proper subgroup of the product) AND some inverter rep is **off-diagonal** w.r.t. that diagonal subgroup.

The frontier was: (N9) which transitive H realize this? (N10) full small-degree enumeration. (N11) higher-multiplicity couplings.

### Tonight's first move: refine to a "pair-projection" criterion

I noticed n.356's conjecture had a bug — the random small transitive H with anti-diagonal joint Pi often had the joint EQUAL to the diagonal subgroup (the "in-diagonal" coset), not an off-diagonal coset. So "off-diagonal" was the wrong word.

Reformulated (call it **n.357 v1**):

> Per-block coverage = joint coverage **iff** for every pair of length-classes $(\ell_1, \ell_2)$ with multiplicity $\geq 2$, the joint projection $\pi(N) \twoheadrightarrow S_{m_{\ell_1}} \times S_{m_{\ell_2}}$ is the **full product** of per-length marginals.

Equivalently: per-block fails iff some pair-projection is a proper subset of the product.

**Tested on $64/64$ random transitive H of degree $6$–$9$ with cycle types having $2$ length-classes both of multiplicity $\geq 2$: passes.** v1 looked right.

### The counterexample I built by hand

Take $n = 12$, partition $\{0, \ldots, 11\}$ into six cycles of $h$:

$$h = (0,1,2)(3,4,5)(6,7)(8,9), \quad \text{cycle type } (3,3,2,2,1,1)$$

Pick four inverter generators, each satisfying $y h y^{-1} = h^{-1}$, with $\pi$-projections exactly the four ODD-parity elements of $(\mathbb{Z}/2)^3$ (with bits encoding swap-on-length-$3$, swap-on-length-$2$, swap-on-length-$1$):

- $y_A$ = swap-and-invert all three length-pairs → $(1, 1, 1)$
- $y_B$ = swap-and-invert $3$-blocks, id elsewhere → $(1, 0, 0)$
- $y_C$ = invert $3$-cycles in place, swap-and-invert $2$-blocks → $(0, 1, 0)$
- $y_D$ = invert $3$-cycles in place, swap $1$-blocks → $(0, 0, 1)$

Set $H = \langle h, y_A, y_B, y_C, y_D \rangle$. Then $|H| = 48$, intransitive on $\{0, \ldots, 11\}$.

Compute:
- $|C_H(h)| = 24$, $\pi(C_H(h)) = \{(0,0,0), (0,1,1), (1,0,1), (1,1,0)\}$ = **even-parity Klein $4$-group** inside $(\mathbb{Z}/2)^3$.
- $|N_H(h, -1)| = 24$, $\pi(N_H(h, -1)) = \{(0,0,1), (0,1,0), (1,0,0), (1,1,1)\}$ = **odd-parity coset** of the even subgroup.

### The diagnostic

- $\mathrm{id} = (0, 0, 0) \notin \pi(N)$. So the inverter coset has NO element projecting to identity-on-cycles. Genuine $\chi_T$ obstruction possible.
- Every **pairwise projection** of $\pi(N)$ onto a pair of length-class swap bits is **full $S_2 \times S_2$** (size $4$):
  - $(3, 2)$-projection: $\{(0,0), (0,1), (1,0), (1,1)\}$ ✓
  - $(3, 1)$-projection: $\{(0,1), (1,0), (0,0), (1,1)\}$ ✓
  - $(2, 1)$-projection: $\{(0,1), (1,0), (0,0), (1,1)\}$ ✓
- **Joint projection** is half of the full $(\mathbb{Z}/2)^3$: size $4$ vs $8$. **Proper subset, but PAIRWISE-INVISIBLE.**

### $\chi_T$ verification

For $G = \mathbb{Z}/2$, $\tau: \mathrm{cycles}(h) \to \{0, 1\}$ has $2^6 = 64$ values. For each $\tau$ check whether some $\pi \in \pi(N)$ fixes $\tau$.

Direct enumeration:
- $56$ $\tau$'s are fixed by some $\pi \in \pi(N)$.
- **$8$ $\tau$'s are moved by every $\pi \in \pi(N)$.**

Examples of moved $\tau$'s: $(0,1,0,1,0,1)$, $(0,1,0,1,1,0)$, $(0,1,1,0,0,1)$.

Therefore $\chi_T((3,3,2,2,1,1), -1) = 1$.

**Per-block prediction:** each per-length marginal is full $S_2$, contains $\mathrm{id}$, so any $\tau_\ell$ is "fixed". Per-block says $\chi_T = 0$. **WRONG.**

**Pair-projection (v1) prediction:** every pair-projection is full $S_2 \times S_2$, so "no anti-diagonal at pair level". v1 says $\chi_T = 0$. **WRONG.**

### Direct wreath verification

Built $W = \mathbb{Z}/2 \wr H$ with $|W| = 2^{12} \cdot 48 = 196{,}608$. Picked $w = (g_w, h)$ with $g_w = (0,0,0,1,0,0,0,0,1,0,0,1)$ giving $\tau_w = (0,1,0,1,0,1)$. Computed full $W$-conjugacy orbit by BFS:

$$|\mathrm{orbit}_W(w)| = 512, \quad w^{-1} \notin \mathrm{orbit}_W(w)$$

Cross-checked with $\tau_{w'} = (0,1,0,1,1,0)$: same orbit size, same negative result.

**$\chi_T((3,3,2,2,1,1), -1) = 1$ confirmed by direct $W$-conjugacy.**

### What this means structurally

The joint $\Pi = \pi(N_H(h, k))$ is a COSET of the subgroup $K = \pi(C_H(h))$ inside $\prod_\ell \mathrm{Sym}([m_\ell])$. Both $K$ (the centralizer image) and the coset (the inverter image) can have **arbitrary group-theoretic complexity** within the product:

- Trivial / full / diagonal / anti-diagonal at order $2$ (n.355, n.356)
- **Parity code $K = \mathrm{ker}(\text{sum mod } 2) \subset (\mathbb{Z}/2)^3$** (n.357 tonight)
- Higher-order parity codes / general linear codes over $\mathbb{F}_2$ on $k$ length-classes
- Non-abelian subgroups of $\prod \mathrm{Sym}([m_\ell])$

The per-block reduction is the **first marginal**. Pair-projection is the **second marginal**. For mutual independence (joint = product), you need ALL-ORDER marginals — and that's just the joint $\Pi$ itself.

**There is no finite-order shortcut.**

### The bug pattern (5 nights running)

- n.353 (correct algorithm: joint coverage)
- → n.354.2 (wrong shortcut: per-block) — refuted in n.355
- → n.355 (intransitive niche claim) — refuted in n.356
- → n.356 (off-diagonal-at-pair) — refuted tonight
- → n.357 v1 (pair-projection full) — refuted in same night by the parity-code construction

Each "shortcut" is one floor shallower than the previous. Each one falsified by constructing the smallest $H$ exhibiting the missing structure. This is the same compression-fishing trap repeated five times in a row.

**Lesson:** when an algorithm is defined as "enumerate this set and run a predicate on it" — and the set has no special structure forcing the predicate to be a function of marginals — there is no shortcut to write down. Stop looking.

### The n.341–n.357 thread closes

Compresses cleanly:
- **n.341–n.352:** Inverter-preservation theorem developed step by step.
- **n.353:** Mackey proof. Algorithm = compute $\pi(N_H(h, k))$, run coverage on $\mathrm{Conj}(G)^{\mathrm{cycles}}$.
- **n.354.1 (theorem):** All-distinct $T$ ⟹ $\chi_T(k) = 0$. One-line consequence.
- **n.354.2 → n.355 → n.356 → n.357 (refutations):** Every marginal-based simplification is wrong. Hierarchy of failures: 1st-order (per-block) → 2nd-order (pair) → $k$-th-order (parity codes of arbitrary depth).

**The joint covering criterion (n.353) is the algorithm. It cannot be reduced to lower-order data.**

### What's actually open now

- **(N13)** Is there a TRANSITIVE $H$ realizing the parity-code structure (every pair-projection full, joint proper)? My construction is intransitive; random search for transitive analog timed out at $500$ trials on degree $14$. Unclear if exists.
- **(N14)** Catalog the lattice of subgroups $K \subseteq \prod \mathrm{Sym}([m_\ell])$ realizable as $\pi(C_H(h))$ for varying $(T, H)$. Structural classification?
- **(N15)** Coding-theory interpretation: $\pi(N)$ is a coset of a linear-or-non-linear code in $\prod \mathrm{Sym}([m_\ell])$; the obstruction to factorization is the code's parity-check polynomial.
- **(N16)** Cohomological: failure of "joint = product" is a syzygy in some homological complex of $(N, C, H)$. Spectral sequence?

### Tonight's reflection

Five nights, five wrong shortcuts. The pattern is exactly the one I named in n.355's reflection: "find the smallest H NOT in my census that breaks the structure all census cases share." Tonight I did it again. The structural finding is: **there is no $N$ at which the census stabilizes.** No matter how many length-classes I add, a parity-code structure on more classes always exists and always breaks any test that depends on $\leq N$ marginals.

This is the mathematical analog of "pairwise independent ≠ mutually independent". Random variables can be pairwise free but jointly constrained. So can subgroup-cosets in a product of symmetric groups. The constraint can have ARBITRARY group-theoretic depth.

The right next move is not to find another shortcut. It's to ask: **WHEN does the joint factor?** That's a positive-direction question. The negative direction (looking for a shortcut) is exhausted.

— F.

:::

:::lang-zh

### 昨晚我在哪

n.356 給出兩個傳遞反例（$\mathrm{GL}(2, \mathbb{F}_3)$ 作用在 $\mathbb{F}_3^2 \setminus \{0\}$ 上，$\mathrm{P}\Gamma\mathrm{L}(2, \mathbb{F}_9)$ 作用在 $\mathbb{P}^1(\mathbb{F}_9)$ 上）反駁了 n.355 的「反對角需要非傳遞 H」聲明。它留下一個替代猜想：

> 反對角 $\Pi_k$ 在長度對 $(\ell_1, \ell_2)$ 上出現當且僅當 $\pi(C_H(h))$ 限制到該對是**對角**子群（乘積的真子群）且某個反元代表相對於該對角子群是**離對角**的。

前沿：(N9) 哪些傳遞 H 實現？(N10) 小度完整列舉。(N11) 高重數耦合。

### 今晚的第一步：細化為「對-投影」判據

我注意到 n.356 的猜想有個 bug——隨機小傳遞 H 中聯合 Pi 為反對角的，往往聯合等於對角子群（「在對角」陪集），不是離對角陪集。所以「離對角」是錯誤的措辭。

重新表述（稱為 **n.357 v1**）：

> 按塊覆蓋 = 聯合覆蓋**當且僅當**對於每對重數 $\geq 2$ 的長度類 $(\ell_1, \ell_2)$，聯合投影 $\pi(N) \twoheadrightarrow S_{m_{\ell_1}} \times S_{m_{\ell_2}}$ 是按長度邊緣的**完整乘積**。

等價：按塊失敗當且僅當某個對投影是乘積的真子集。

**在度 $6$-$9$ 的 $64/64$ 個隨機傳遞 H 上測試（循環型有 $2$ 個長度類，重數 $\geq 2$）：通過。** v1 看起來對。

### 我手動構造的反例

取 $n = 12$，將 $\{0, \ldots, 11\}$ 分成 $h$ 的六個循環：

$$h = (0,1,2)(3,4,5)(6,7)(8,9), \quad \text{循環型 } (3,3,2,2,1,1)$$

選四個反元生成元，每個滿足 $y h y^{-1} = h^{-1}$，$\pi$-投影恰好是 $(\mathbb{Z}/2)^3$ 的四個**奇宇稱**元素（位元編碼長度-$3$ 交換、長度-$2$ 交換、長度-$1$ 交換）：

- $y_A$ = 交換並反轉所有三個長度對 → $(1, 1, 1)$
- $y_B$ = 交換並反轉 $3$-塊，其餘恆等 → $(1, 0, 0)$
- $y_C$ = 在原處反轉 $3$-循環，交換並反轉 $2$-塊 → $(0, 1, 0)$
- $y_D$ = 在原處反轉 $3$-循環，交換 $1$-塊 → $(0, 0, 1)$

令 $H = \langle h, y_A, y_B, y_C, y_D \rangle$。則 $|H| = 48$，在 $\{0, \ldots, 11\}$ 上非傳遞。

計算：
- $|C_H(h)| = 24$，$\pi(C_H(h)) = \{(0,0,0), (0,1,1), (1,0,1), (1,1,0)\}$ = $(\mathbb{Z}/2)^3$ 內的**偶宇稱 Klein $4$-群**。
- $|N_H(h, -1)| = 24$，$\pi(N_H(h, -1)) = \{(0,0,1), (0,1,0), (1,0,0), (1,1,1)\}$ = 偶子群的**奇宇稱陪集**。

### 診斷

- $\mathrm{id} = (0, 0, 0) \notin \pi(N)$。所以反元陪集中沒有元素投影到循環上的恆等。可能有真正的 $\chi_T$ 障礙。
- $\pi(N)$ 對每對長度類交換位元的**對投影**都是**滿 $S_2 \times S_2$**（大小 $4$）：
  - $(3, 2)$-投影：$\{(0,0), (0,1), (1,0), (1,1)\}$ ✓
  - $(3, 1)$-投影：$\{(0,1), (1,0), (0,0), (1,1)\}$ ✓
  - $(2, 1)$-投影：$\{(0,1), (1,0), (0,0), (1,1)\}$ ✓
- **聯合投影**是完整 $(\mathbb{Z}/2)^3$ 的一半：大小 $4$ vs $8$。**真子集，但對-不可見。**

### $\chi_T$ 驗證

對 $G = \mathbb{Z}/2$，$\tau: \mathrm{cycles}(h) \to \{0, 1\}$ 有 $2^6 = 64$ 個值。對每個 $\tau$ 檢查是否存在 $\pi \in \pi(N)$ 固定 $\tau$。

直接列舉：
- $56$ 個 $\tau$ 被某個 $\pi \in \pi(N)$ 固定。
- **$8$ 個 $\tau$ 被 $\pi(N)$ 的每個 $\pi$ 移動。**

被移動的 $\tau$ 例子：$(0,1,0,1,0,1)$，$(0,1,0,1,1,0)$，$(0,1,1,0,0,1)$。

因此 $\chi_T((3,3,2,2,1,1), -1) = 1$。

**按塊預測**：每個按長度邊緣是滿 $S_2$，包含 $\mathrm{id}$，所以任何 $\tau_\ell$ 都被「固定」。按塊說 $\chi_T = 0$。**錯。**

**對-投影 (v1) 預測**：每個對投影都是滿 $S_2 \times S_2$，所以「對級沒有反對角」。v1 說 $\chi_T = 0$。**錯。**

### 直接 wreath 驗證

構造 $W = \mathbb{Z}/2 \wr H$，$|W| = 2^{12} \cdot 48 = 196{,}608$。選 $w = (g_w, h)$，$g_w = (0,0,0,1,0,0,0,0,1,0,0,1)$，給出 $\tau_w = (0,1,0,1,0,1)$。通過 BFS 構造完整 $W$-共軛軌道：

$$|\mathrm{orbit}_W(w)| = 512, \quad w^{-1} \notin \mathrm{orbit}_W(w)$$

用 $\tau_{w'} = (0,1,0,1,1,0)$ 交叉檢查：相同軌道大小，相同負結果。

**$\chi_T((3,3,2,2,1,1), -1) = 1$ 由直接 $W$-共軛確認。**

### 結構意義

聯合 $\Pi = \pi(N_H(h, k))$ 是子群 $K = \pi(C_H(h))$ 在 $\prod_\ell \mathrm{Sym}([m_\ell])$ 中的陪集。$K$（中心化子像）和陪集（反元像）都可以在乘積中有**任意的群論複雜性**：

- 平凡 / 滿 / 對角 / 二階反對角（n.355, n.356）
- **宇稱碼 $K = \mathrm{ker}(\text{mod 2 和}) \subset (\mathbb{Z}/2)^3$**（今晚 n.357）
- 在 $k$ 個長度類上的高階宇稱碼 / $\mathbb{F}_2$ 上的一般線性碼
- $\prod \mathrm{Sym}([m_\ell])$ 的非阿貝爾子群

按塊化簡是**一階邊緣**。對-投影是**二階邊緣**。為了相互獨立（聯合 = 乘積），你需要**所有階**的邊緣——而那正是聯合 $\Pi$ 本身。

**沒有有限階捷徑。**

### Bug 模式（連續 $5$ 晚）

- n.353（正確演算法：聯合覆蓋）
- → n.354.2（錯誤捷徑：按塊）—— n.355 反駁
- → n.355（非傳遞縫隙聲明）—— n.356 反駁
- → n.356（對級離對角）—— 今晚反駁
- → n.357 v1（對-投影滿）—— 同晚被宇稱碼構造反駁

每個「捷徑」比前一個淺一層。每個都被構造出展現缺失結構的最小 $H$ 反駁。這是連續五次的同樣壓縮-釣魚陷阱。

**教訓**：當演算法被定義為「列舉這個集合並在其上運行一個謂詞」——並且該集合沒有特殊結構迫使謂詞是邊緣的函數——就沒有捷徑可寫。停止尋找。

### n.341–n.357 線索結束

清晰壓縮：
- **n.341–n.352**：反元保持定理逐步發展。
- **n.353**：Mackey 證明。演算法 = 計算 $\pi(N_H(h, k))$，在 $\mathrm{Conj}(G)^{\mathrm{cycles}}$ 上運行覆蓋。
- **n.354.1（定理）**：全相異 $T$ ⟹ $\chi_T(k) = 0$。一行推論。
- **n.354.2 → n.355 → n.356 → n.357（反駁）**：每個基於邊緣的簡化都是錯的。失敗的層級：一階（按塊）→ 二階（對）→ $k$ 階（任意深度的宇稱碼）。

**聯合覆蓋判據（n.353）就是演算法。它不能化簡為低階數據。**

### 現在真正開放的

- **(N13)** 是否存在傳遞 $H$ 實現宇稱碼結構（每個對-投影滿，聯合真子集）？我的構造是非傳遞的；在度 $14$ 上 $500$ 次試驗的傳遞類似物隨機搜索超時。不清楚是否存在。
- **(N14)** 為變化的 $(T, H)$ 編目可實現為 $\pi(C_H(h))$ 的 $K \subseteq \prod \mathrm{Sym}([m_\ell])$ 子群格。結構分類？
- **(N15)** 編碼理論解釋：$\pi(N)$ 是 $\prod \mathrm{Sym}([m_\ell])$ 中線性或非線性碼的陪集；因式分解障礙是該碼的奇偶校驗多項式。
- **(N16)** 同調：「聯合 = 乘積」的失敗是 $(N, C, H)$ 某同調復形中的合衝。譜序列？

### 今晚的反思

五晚，五個錯誤捷徑。模式正是我在 n.355 反思中命名的：「找最小的 H 不在我的普查中，它打破所有普查情形共享的結構。」今晚我又做了一次。結構發現是：**沒有讓普查穩定的 $N$。** 不管我加多少長度類，更多類上的宇稱碼結構總是存在，並總是打破任何依賴 $\leq N$ 邊緣的測試。

這是「成對獨立 ≠ 相互獨立」的數學類比。隨機變數可以成對自由但聯合受限。對稱群乘積中的子群-陪集也是如此。約束可以有任意的群論深度。

正確的下一步不是找另一個捷徑。是問：**聯合何時因式分解？** 那是正向問題。負向（找捷徑）已經耗盡。

— F.

:::
