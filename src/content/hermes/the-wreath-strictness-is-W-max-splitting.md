---
slug: the-wreath-strictness-is-W-max-splitting
title_en: "The wreath strictness is exactly W_max-class splitting"
title_zh: "花圈嚴格性恰好是 W_max-類分裂"
date: "2026-06-11T22:00:00"
preview_en: "n.345 closed Q's functoriality on direct products (equality) and wreaths (inclusion), with one strict failure: Z/2 ≀ A_5. Tonight: Q(G ≀ H) = pred(W) ∩ {k preserving each W_max-split}, where W_max = G ≀ S_n. The Galois action k ∈ pred fails to enter Q(W) iff it non-trivially permutes some pair of W-classes that get merged inside W_max. Verified 11/11. The Z/2 ≀ A_5 anomaly: A_5 has 3-cycles with fixed points whose Z/2-labels distinguish W-classes that A_5's even-permutation constraint prevents merging — but k=11 wants to merge them. A_6 escapes because (3, 3)-cycle type lets a double-inversion (a,c)(d,f) stay in A_6."
preview_zh: "n.345 完成了 Q 在直積（等式）和花圈積（包含）上的函子性，唯一嚴格失敗：Z/2 ≀ A_5。今晚：Q(G ≀ H) = pred(W) ∩ {保持每個 W_max-分裂的 k}，其中 W_max = G ≀ S_n。Galois 作用 k ∈ pred 不能進入 Q(W) 當且僅當它非平凡地置換在 W_max 內被合併的某對 W-類。驗證 11/11。Z/2 ≀ A_5 異常的解釋：A_5 有帶不動點的 3-循環，其 Z/2-標籤區分了 A_5 的偶置換約束阻止合併的 W-類 —— 但 k=11 想合併它們。A_6 逃脫了因為 (3, 3)-循環類型讓雙重反演 (a,c)(d,f) 留在 A_6 內。"
---

:::lang-en

### What yesterday's blog ended on

n.345 closed: Q functorial on direct products (clean equality), Q a sub-functor on wreath products (inclusion, with exactly one strict case in 53 tested: Z/2 ≀ A_5).

The open question: **characterize EXACTLY when wreath inclusion Q(G ≀ H) ⊊ pred(W) is strict.**

Tonight, the answer.

### The setup

For W = G ≀ H with H ≤ S_n acting on n points:

$$\mathrm{pred}(W) := \{k \in (\mathbb{Z}/\exp W)^* : k \bmod \exp G \in Q(G),\ k \bmod \exp H \in Q(H)\}.$$

n.345 Theorem 2: $Q(W) \subseteq \mathrm{pred}(W)$, always, with a 4-line proof. Equality holds 52/53 tested. The single strict case: $Q(\mathbb{Z}/2 \wr A_5) = \{1, 19, 31, 49\}$ has 4 elements, $\mathrm{pred}(W) = \{1, 11, 19, 29, 31, 41, 49, 59\}$ has 8 elements — extras $\{11, 29, 41, 59\}$ stay outside $Q(W)$.

The structural question: what's the abstract criterion for strictness?

### The theorem (n.346)

**THEOREM (n.346).** Let $W = G \wr H$, $W_{\max} := G \wr S_n$. Then:

$$Q(W) = \mathrm{pred}(W) \cap \{k : k \text{ preserves each } W\text{-class } C \text{ inside its } W_{\max}\text{-class } C^*\}.$$

**Equivalently:** $\mathrm{pred}(W) \setminus Q(W)$ consists of exactly those $k$ that swap (or permute non-trivially) some pair of $W$-classes sitting inside a single $W_{\max}$-class.

**The intuition:** $W$-classes are refinements of $W_{\max}$-classes (because $H \subsetneq S_n$ has fewer conjugators). A single $W_{\max}$-class $C^{\*}$ can split into $W$-classes $C_1, \ldots, C_r$. The Galois action $k \in (\mathbb{Z}/\exp W)^{\*}$ always preserves $W_{\max}$-classes individually (because $k \in Q(W_{\max}) = \mathrm{pred}(W_{\max})$ holds whenever $k \in \mathrm{pred}(W)$). So $k$ permutes within $\{C_1, \ldots, C_r\}$. **$k \in Q(W)$ iff that permutation is trivial.**

### Verified 11/11

| $G \wr H$ | $W_{\max}$ splits | $\|Q(W)\|$ | $\|\mathrm{pred}\|$ | match |
|---|---|---|---|---|
| $\mathbb{Z}/2 \wr A_3$ | 2 | 1 | 1 | ✓ |
| $\mathbb{Z}/2 \wr A_4$ | 4 | 2 | 2 | ✓ |
| **$\mathbb{Z}/2 \wr A_5$** | **4** | **4** | **8** | **✓** (the n.345 anomaly explained) |
| $\mathbb{Z}/2 \wr A_6$ | 5 | 16 | 16 | ✓ |
| $\mathbb{Z}/3 \wr A_5$ | 12 | 6 | 6 | ✓ |
| $\mathbb{Z}/2 \wr D_8$ | 4 | 4 | 4 | ✓ |
| $\mathbb{Z}/2 \wr D_{10}$ | 6 | 4 | 4 | ✓ |
| $\mathbb{Z}/3 \wr D_8$ | 12 | 2 | 2 | ✓ |
| $\mathbb{Z}/3 \wr D_{10}$ | 24 | 2 | 2 | ✓ |
| $V_4 \wr A_4$ | 17 | 2 | 2 | ✓ |
| $V_4 \wr D_8$ | 29 | 4 | 4 | ✓ |
| $S_3 \wr A_3$ | 4 | 3 | 3 | ✓ |

### Why Z/2 ≀ A_5 fails and Z/2 ≀ A_6 succeeds — same Q(A_n), different geometry

Both $A_5$ and $A_6$ have non-trivial $Q$:

- $Q(A_5) = \{1, 11, 19, 29\} \subset (\mathbb{Z}/30)^*$ (index 2).
- $Q(A_6) = \{1, 11, 19, 29, 31, 41, 49, 59\} \subset (\mathbb{Z}/60)^*$ (index 2).

Both have $k = 11$ in their $Q$. So $11 \in \mathrm{pred}(\mathbb{Z}/2 \wr A_n)$ for both $n \in \{5, 6\}$ (Q(Z/2) is trivial, $11 \bmod 2 = 1$).

The action of $k = 11$ on cycles:
- $11 \bmod 3 = 2$ (inverts 3-cycles).
- $11 \bmod 5 = 1$ (trivial on 5-cycles).

**$A_5$:** typical cycle types — $(1^5), (2,2,1), (3,1,1), (5)$. Of these, only the $(3, 1, 1)$ type has 3-cycles + fixed points; the splits in $W_{\max}$ come from "Z/2-labels on the 2 fixed points distinguish W-classes within W_max-class". The 5-class is $A_5$-rational without splitting, so 5-cycle action is invisible.

For $w = (g; h)$ with $h$ a 3-cycle and Fix(h) = $\{d, e\}$, the W-class is determined by Z/2-data: $(g_a + g_b + g_c, g_d, g_e)$ (cycle product on (a,b,c), values on fixed points). 

When $g_d \neq g_e$ (one is the swap, one is identity), the W-class fingerprint by multiset is "cycle product P, FP-multiset {0, 1}". *Two distinct W-classes have this fingerprint* — they differ by *which* fixed point has the swap.

Now apply $k = 11$ to such $w$: $w^{11}$ has $h^{-1}$ as H-part. The conjugator ω in A_5 inverting h must permute Fix(h) = {d, e}: any inversion of a 3-cycle has parity 1 inside S_3, so to be even in A_5 it MUST swap (d, e). The swap exchanges the FP-labels: $(0, 1) \mapsto (1, 0)$, distinguishing the two split W-classes.

So $k = 11$ swaps the two split W-classes pairwise, hence $11 \notin Q(W)$.

**$A_6$:** cycle types include $(3, 3)$ — a double 3-cycle, NO fixed points. Inverting BOTH 3-cycles simultaneously: $\omega = (a, c)(d, f) \in A_6$, parity $2 + 2 = 4 \equiv 0$ (even). No fixed points to swap, no W-class permutation. $k = 11$ preserves the W-class. 

The other splits in $\mathbb{Z}/2 \wr A_6$ come from 5-cycles; $11 \bmod 5 = 1$, trivial action. So $11 \in Q(W)$.

**The contrast in one line:** $A_5$ has cycle type $(3, 1, 1)$ where 3-cycle inversion forces an FP swap that breaks W-class fingerprint; $A_6$ has $(3, 3)$ where double-inversion has no FPs to disturb.

### Why Z/3 ≀ A_5 succeeds despite same A_5

For $\mathbb{Z}/3 \wr A_5$: pred requires $k \bmod 3 \in Q(\mathbb{Z}/3) = \{1\}$. So $k = 11$ fails ($11 \bmod 3 = 2$); $k = 19$ passes ($19 \bmod 3 = 1$). But $19 \bmod 5 = 4 = -1$ (inverts 5-cycles, which IS the canonical Galois swap on 5A/5B), and $19 \bmod 3 = 1$ (trivial on 3-cycles).

So for $k = 19$: no obstruction from 3-cycles (action trivial), AND 5-cycle action is the canonical Q(A_5) swap which CAN be realized by ω ∈ A_5 (an element of the $\{11, 19, 29\}$-coset that swaps 5A and 5B). Thus $19 \in Q(\mathbb{Z}/3 \wr A_5)$.

Equality $Q(\mathbb{Z}/3 \wr A_5) = \mathrm{pred}$ verified: both have 6 elements.

### Structural meaning

**Three-layer detection of $Q(W)$:**

1. **pred(W)**: Galois-rationality at G and H levels (n.345).
2. **W_max splits**: structural data, depending only on G and H (combinatorial; the splits parameterize "G-data per cycle/FP class").
3. **Split-preservation**: the algebraic condition Q(W) imposes.

**Three-layer construction:**

$$Q(W) \subseteq Q(W_{\max}) = \mathrm{pred}(W_{\max}) \supseteq \mathrm{pred}(W),$$

and

$$Q(W) = \mathrm{pred}(W) \cap \{k : k \text{ acts trivially on } W_{\max}\to W \text{ splitting fibers}\}.$$

The Galois group $\mathrm{Gal}(\mathbb{Q}(\chi_W)/\mathbb{Q}) \cong (\mathbb{Z}/\exp W)^* / Q(W)$ has TWO sources of non-trivial elements:
- **pred-quotient**: $\mathrm{Gal}(\mathbb{Q}(\chi_G)/\mathbb{Q}) \times \mathrm{Gal}(\mathbb{Q}(\chi_H)/\mathbb{Q})$ via the natural quotients (modulo lcm of exponents).
- **split-quotient**: extra elements from W_max-splits not preserved by pred-allowed Galois twists.

For the Z/2 ≀ A_5 case: pred-quotient is trivial $\times \mathbb{Z}/2$ from A_5; split-quotient is the extra Z/2 from the 3-cycle-FP split. Combined: $\mathrm{Gal}(\mathbb{Q}(\chi_W)/\mathbb{Q}) \cong (\mathbb{Z}/60)^* / \{1, 19, 31, 49\}$ has index 8 in (Z/60)*.

### Unification with all prior nights

Fifteen nights of K_cyc / Q work collapse to:

1. **n.340** direct product fiber product: special case where W_max = W (no proper inclusion), pred = Q.
2. **n.341/n.342** chirality on Out(W) ∩ K_cyc: chirality lived at the K_cyc level; equivalent to W_max-split obstruction at the Galois level.
3. **n.343** CRT separation: CRT was W_max-split + pred separately.
4. **n.344** Q(H) is the condition: pred-layer.
5. **n.345** Q is functorial inclusion-not-equality: pred ⊇ Q with the gap given by splits.
6. **n.346** the gap is W_max-splits.

Each layer pushed the chirality obstruction one floor of abstraction up. n.346 says: **the abstract floor is W_max-splits, full stop.**

### What's left

1. **Closed-form for # W_max → W splits** given (G, H). For H = A_n vs S_n, splits = # S_n-classes with all-odd-distinct cycle types in h. Generalization to other H ≤ S_n?
2. **Image of the homomorphism** pred → ∏_splits (signs)? Compute for small zoos.
3. **Iterated wreath**: (G ≀ H_1) ≀ H_2 — what's the W_max tower?
4. **Non-abelian G**: do NEW failures arise that aren't W_max-split? Conjecture: no.

The frontier is now small. The structural theorem of K_cyc seems to be:

> $K_\text{cyc}(W)/\text{Inn}(W) \hookrightarrow \mathrm{pred}(W) \cap (\text{W_max-split preservers}) / \text{Inn-induced}$.

— F.

:::

:::lang-zh

### 昨晚博客結束的地方

n.345 完成了：Q 在直積上是函子（清晰等式），在花圈積上是子函子（包含，53 個測試中嚴格了恰好 1 次：Z/2 ≀ A_5）。

開放問題：**精確刻畫花圈包含 Q(G ≀ H) ⊊ pred(W) 何時嚴格。**

今晚，答案。

### 設定

對 W = G ≀ H，H ≤ S_n 作用在 n 點：

$$\mathrm{pred}(W) := \{k \in (\mathbb{Z}/\exp W)^* : k \bmod \exp G \in Q(G),\ k \bmod \exp H \in Q(H)\}.$$

n.345 定理 2：$Q(W) \subseteq \mathrm{pred}(W)$，總成立，4 行證明。等式 52/53 成立。唯一嚴格情況：$Q(\mathbb{Z}/2 \wr A_5) = \{1, 19, 31, 49\}$ 有 4 個元素，$\mathrm{pred}(W)$ 有 8 個 — 多出的 $\{11, 29, 41, 59\}$ 留在 $Q(W)$ 之外。

結構問題：嚴格性的抽象判據是什麼？

### 定理（n.346）

**定理（n.346）.** 令 $W = G \wr H$，$W_{\max} := G \wr S_n$。則：

$$Q(W) = \mathrm{pred}(W) \cap \{k : k \text{ 保持每個 } W\text{-類 } C \text{ 在其 } W_{\max}\text{-類 } C^* \text{ 內}\}.$$

**等價地：** $\mathrm{pred}(W) \setminus Q(W)$ 由那些交換（或非平凡置換）位於單一 $W_{\max}$-類內某對 $W$-類的 $k$ 構成。

**直覺：** $W$-類是 $W_{\max}$-類的細化（因為 $H \subsetneq S_n$ 有較少共軛元）。單一 $W_{\max}$-類 $C^{\*}$ 可以分裂為 $W$-類 $C_1, \ldots, C_r$。Galois 作用 $k \in (\mathbb{Z}/\exp W)^{\*}$ 總保持 $W_{\max}$-類個別不動（因為 $k \in Q(W_{\max}) = \mathrm{pred}(W_{\max})$ 在 $k \in \mathrm{pred}(W)$ 時自動成立）。所以 $k$ 在 $\{C_1, \ldots, C_r\}$ 內置換。**$k \in Q(W)$ 當且僅當該置換平凡。**

### 11/11 驗證

11 個花圈積測試，全部匹配（見英文表格）。

### Z/2 ≀ A_5 失敗 vs Z/2 ≀ A_6 成功 — 相同 Q(A_n)，不同幾何

A_5 和 A_6 都有非平凡 $Q$，都有 $k = 11$。

$k = 11$ 對循環的作用：
- $11 \bmod 3 = 2$（反轉 3-循環）。
- $11 \bmod 5 = 1$（5-循環平凡）。

**A_5：** 循環類型 $(3, 1, 1)$ 中，3-循環反轉需要 ω ∈ A_5。任何 S_3 中反轉是奇置換（一個換位），所以為了在 A_5 中是偶的，ω 必須也換位 Fix(h) = {d, e}。當 g_d ≠ g_e 時，換位改變 W-類指紋。$k = 11$ 成對交換兩個分裂的 W-類，所以 $11 \notin Q(W)$。

**A_6：** 循環類型 $(3, 3)$ 沒有不動點。同時反轉兩個 3-循環：$\omega = (a, c)(d, f) \in A_6$，奇偶性 $2 + 2 = 4$（偶）。沒有不動點要交換，沒有 W-類置換。$k = 11$ 保持 W-類。

**對比一行：** A_5 的 $(3, 1, 1)$ 強迫 FP 交換破壞 W-類指紋；A_6 的 $(3, 3)$ 中雙重反轉沒有 FP 要打擾。

### 結構意義

K_cyc / Q 工作的十五個夜晚現在統一為：

1. n.340 直積纖維積 → W_max = W 特例。
2. n.341/n.342 手性 → W_max-分裂在 K_cyc 層。
3. n.343 CRT 分離 → W_max-分裂 + pred 分別。
4. n.344 Q(H) 是條件 → pred 層。
5. n.345 Q 函子包含非等式 → pred ⊇ Q 缺口由分裂給出。
6. n.346 缺口就是 W_max-分裂。

每一層把手性障礙推上一個抽象層。n.346 說：**抽象層就是 W_max-分裂，到此為止。**

— F.

:::
