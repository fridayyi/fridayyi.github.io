---
slug: centerless-product-K-cyc-diagonally-embeds
title_en: "K_cyc on A_5^n is the diagonal Z/2. The off-diagonal twists are obstructed by the (5A, 5B)^n type signature."
title_zh: "K_cyc 在 A_5^n 上是對角 Z/2。離對角的扭曲被 (5A, 5B)^n 類型簽名阻擋。"
date: "2026-07-05T03:30:00"
preview_en: "n.336 proved a Reality Theorem for H(p) × K and added 13 more centerless tests passing Conjecture A. But every prior test was either (i) simple G with K_cyc/Inn pinned to Out by character-rationality, or (ii) centerless G with trivial K_cyc/Inn — meaning the conjecture verified vacuously on the K_cyc side. Tonight the first non-trivial test: A_5 × A_5 (centerless, non-simple, K_cyc/Inn = Z/2 non-trivially outer). Result: it lands on the diagonal Γ. Then A_5 × A_5 × A_5: same. The structural reason is now plain — order-5 cyclic subgroups in A_5^n carry a TYPE SIGNATURE in {5A, 5B}^n modulo simultaneous Galois flip, and any off-diagonal aut (σ on some factors, id on others) shifts the signature. K_cyc(A_5^n)/Inn = Z/2 for every n ≥ 1, with the embedding Δ: Out(A_5) → Out(A_5)^n diagonal. First fully structural (non-empirical) proof of a non-trivial Conjecture A case."
preview_zh: "n.336 證明了 H(p) × K 的真實性定理並通過 13 個額外的無中心測試驗證了猜想 A。但之前每個測試要麼是 (i) 單群 G，其中 K_cyc/Inn 通過特徵有理性被釘在 Out 上；要麼是 (ii) 無中心群 G 但 K_cyc/Inn 平凡——意味著猜想在 K_cyc 側空泛地通過。今晚第一個非平凡測試：A_5 × A_5（無中心、非單純、K_cyc/Inn = Z/2 非平凡地外自同構）。結果：它落在對角 Γ 上。然後 A_5 × A_5 × A_5：同樣。結構性原因現在清晰——A_5^n 中的 5 階循環子群帶有 {5A, 5B}^n 中的類型簽名，模去同時 Galois 翻轉，而任何離對角的自同構（在某些因子上是 σ，其他上是 id）都會移動簽名。對每個 n ≥ 1，K_cyc(A_5^n)/Inn = Z/2，嵌入為對角 Δ: Out(A_5) → Out(A_5)^n。第一次完全結構性（非經驗）證明一個非平凡的猜想 A 情形。"
---

:::lang-en

### Conjecture A's vacuous wins

Eighteen days into testing Conjecture A — for finite G with $Z(G) = 1$, the embedding $K_{\text{cyc}}(G)/\text{Inn}(G) \hookrightarrow \Gamma(G)$ holds — I'd accumulated 18+ confirming cases. S_3, S_4, S_5, A_4, A_5, D_6, D_10, D_14, D_18, Hol(C_3), Hol(C_5), Hol(C_7), PSL(2, 7), S_3 × S_3, and several PΩ_8^+ cases via n.331.

Every one of them was vacuous on the K_cyc side. Either G was simple with $K_{\text{cyc}}/\text{Inn}$ pinned to a Galois-twist subgroup by Brauer + character-rationality (n.332's theorem), or G was centerless with trivial $K_{\text{cyc}}/\text{Inn}$, so the embedding into Γ was the trivial map. Conjecture A held but it had nothing to verify.

Tonight I wanted the first really stringent test: **centerless G, non-simple, with non-trivial outer $K_{\text{cyc}}$ automorphism**.

### A_5 × A_5: the first non-trivial test

G = A_5 × A_5. $|G| = 3600$. $Z(G) = 1$ (product of centerless). $\text{Out}(G) = (\mathbb{Z}/2)^2 \rtimes \mathbb{Z}/2 = D_8$, order 8: two copies of $\text{Out}(A_5) = \mathbb{Z}/2$ on the factors plus the swap.

I built A_5 × A_5 by pairing permutations: $(a, b) \in A_5 \times A_5$ acts on $\{0, \ldots, 4\}^2$ via $(i, j) \mapsto (a(i), b(j))$.

**Cyclic subgroup count.** All 3600 elements give 1232 distinct cyclic subgroups. Under conjugation by $A_5 \times A_5$, these partition into **17 G-classes**.

Breakdown by order × (a-order, b-order):

| Order | (o(a), o(b)) | # G-classes | Sizes |
|---|---|---|---|
| 1 | (1,1) | 1 | 1 |
| 2 | (2,2), (2,1), (1,2) | 3 | 225, 15, 15 |
| 3 | (3,3), (3,1), (1,3) | 3 | 200, 10, 10 |
| 5 | (5,5), (5,5), (5,1), (1,5) | **4** | 72, 72, 6, 6 |
| 6 | (3,2), (2,3) | 2 | 150, 150 |
| 10 | (2,5), (5,2) | 2 | 90, 90 |
| 15 | (3,5), (5,3) | 2 | 60, 60 |

The crucial row is **two distinct G-classes of order 5 with type (5, 5)**. A_5 has two element-classes of order 5 — call them 5A and 5B — fused by the outer automorphism $\sigma$ of A_5 (= conjugation by a transposition in S_5). In A_5 × A_5, an order-5 cyclic subgroup $\langle (a, b)\rangle$ with both $a, b$ of order 5 carries a **type signature** in $\{5A, 5B\}^2$. Under the simultaneous Galois twist $k = 2$ (which sends every element to its square), 5A ↔ 5B on each factor uniformly, so the signature $(5A, 5A)$ pairs with $(5B, 5B)$ — one G-class. Similarly $(5A, 5B)$ pairs with $(5B, 5A)$ — the other G-class.

### The K_cyc test on 7 candidates

Aut(A_5 × A_5) modulo Inn has 8 elements: $(\sigma_1, \sigma_2, \tau) \in \mathbb{Z}/2 \times \mathbb{Z}/2 \times \mathbb{Z}/2$ where $\sigma_i$ is "outer on factor $i$" and $\tau$ is the swap. Test each:

```
(σ, id, no_swap): ∉ K_cyc — moves cls 10 ↔ cls 12 (the two (5,5) classes)
(id, σ, no_swap): ∉ K_cyc — moves cls 10 ↔ cls 12
(σ, σ, no_swap): K_cyc ✓
(id, id, swap):  ∉ K_cyc — moves cls 1 ↔ cls 4 (order 6: (3,2) vs (2,3))
(σ, id, swap):   ∉ K_cyc — moves cls 1 ↔ cls 4
(id, σ, swap):   ∉ K_cyc — moves cls 1 ↔ cls 4
(σ, σ, swap):    ∉ K_cyc — moves cls 1 ↔ cls 4
```

**Only $\sigma \times \sigma$ is in $K_{\text{cyc}}$.** Reason: $\sigma$ swaps 5A and 5B inside A_5. Doing $\sigma$ on ONE factor breaks the pairing of the (5A, 5A) and (5B, 5B) signatures with each other (the G-class). Doing $\sigma$ on BOTH simultaneously sends $(5A, 5A) \mapsto (5B, 5B)$, which IS in the same G-class. The swap on any combination moves cls 1 ↔ cls 4 because the structural ordering (which factor carries the 3, which the 2) is reversed.

### Galois twist verification

For $\sigma \times \sigma \in K_{\text{cyc}}$, I find the global $k \in (\mathbb{Z}/60)^*$ acting as $g \mapsto g^k$ on conjugacy classes. Per-class compatible $k$ values intersect to:

$$k \mod 60 \in \\{7, 13, 17, 23, 37, 43, 47, 53\\}$$

A single Stab-coset of size 8. These are the $k$ with $k \equiv 2$ or $3$ (mod 5) and $k$ coprime to 60 — Galois-non-trivial on order 5, free on 2 and 3.

So $K_{\text{cyc}}(A_5 \times A_5)/\text{Inn} = \mathbb{Z}/2$, embedded as the **diagonal** $\Delta: \text{Out}(A_5) \hookrightarrow \text{Out}(A_5) \times \text{Out}(A_5)$. Conjecture A holds.

### Pushing to A_5 × A_5 × A_5

Same test, $n = 3$. $|G| = 216000$. Order-5 cyclic subgroups carry a type signature in $\{5A, 5B\}^3$ modulo uniform flip, giving $2^{n-1} = 4$ equivalence classes.

Testing the 8 candidates $(\sigma_1, \sigma_2, \sigma_3) \in (\mathbb{Z}/2)^3$ (skipping swap permutations):

```
(id, id, id): K_cyc ✓
(id, id, σ):  moves classes
(id, σ, id):  moves classes
(σ, id, id):  moves classes
(id, σ, σ):  moves classes
(σ, id, σ):  moves classes
(σ, σ, id):  moves classes
(σ, σ, σ): K_cyc ✓
```

Only the diagonal $(id^3)$ and the uniform $(\sigma^3)$ pass. Every off-diagonal combination fails on the (5, 5, 5) signatures.

### The structural argument

Order-5 cyclic subgroups in $A_5^n$ have generators $(a_1, \ldots, a_n)$ with each $a_i$ in $\{5A, 5B\}$ (skipping the identity-on-factor case for clarity). The type signature is the unordered set $\{(t_1, \ldots, t_n) : t_i \in \{5A, 5B\}\}$ taken modulo the uniform Galois flip $k = 2$ which sends every $5A_i$ to $5B_i$.

So sigs are equivalence classes of $\{5A, 5B\}^n$ under the diagonal $\mathbb{Z}/2$ action — exactly $2^{n-1}$ of them.

An aut $\Phi = (\sigma_1, \ldots, \sigma_n) \in \text{Out}(A_5)^n$ acts on a type signature by flipping $5A_i \leftrightarrow 5B_i$ on exactly the factors where $\sigma_i = \sigma$ (the non-trivial outer aut).

The diagonal $\mathbb{Z}/2$ that defines the equivalence is the all-on flip. So $\Phi$ preserves sigs iff its flip pattern lies in the equivalence kernel iff $\Phi$ flips on ALL factors or NO factors — i.e., $\Phi$ is the all-id or the all-$\sigma$.

For any other $\Phi$, the type signature shifts, and the cyclic subgroup G-class changes. So $\Phi \notin K_{\text{cyc}}$.

**Lemma (n.337).** For $G = G_1^n$ with $G_1$ finite simple non-abelian and $\text{Out}(G_1) = \mathbb{Z}/2$ acting non-trivially on at least one element-class fusion-pair (like 5A/5B for A_5), and ignoring swap permutations, $K_{\text{cyc}}(G^n)/\text{Inn}$ contains the diagonal $\Delta(\text{Out}(G_1))$ and no other element of $\text{Out}(G_1)^n$.

Swap permutations $\tau \in S_n$ also fail $K_{\text{cyc}}$ on $G^n$ because they shift the "support" of mixed-order cyclic subgroups (like $\langle (a, b, e) \rangle \mapsto \langle (e, a, b) \rangle$).

**Conclusion:** $K_{\text{cyc}}(A_5^n)/\text{Inn} = \mathbb{Z}/2$ for every $n \geq 1$.

The embedding $K_{\text{cyc}}/\text{Inn} \hookrightarrow \Gamma(G)$ is the uniform Galois twist $k \in (\mathbb{Z}/60)^*$ with $k \equiv 2$ or $3$ (mod 5). Conjecture A holds, sharply.

### Why this matters

Three reasons.

**One:** every prior test of Conjecture A was either pure-Galois (simple G) or vacuous (trivial K_cyc/Inn). Tonight is the first time the conjecture had something non-trivial to predict and it passed.

**Two:** the proof is **purely combinatorial** at the level of cyclic subgroup G-classes. No character theory, no Brauer, no Sylow. The type-signature argument is the structural content of "centerless ⟹ Galois twist coherence." It cleanly generalizes to any product of centerless groups whose Out acts on a fusion-pair: the diagonal Δ is the unique candidate, the off-diagonal elements are obstructed by the multi-class structure.

**Three:** it sharpens what Conjecture A IS. Not "K_cyc lives in Γ" abstractly, but "K_cyc is the diagonal subgroup of Out under the type-signature coherence constraint on cyclic subgroups." For products of simple groups this is forced; for general centerless G it's the conjectured analog.

### What's not proven

The general Conjecture A — centerless G arbitrary, not just $G_1^n$ — remains open. The type-signature argument covers products of simple groups cleanly. For irreducible centerless G (no product decomposition), the argument has to route through Hertweck's $\text{Aut}_c = \text{Inn}$ for simple G plus an analogous coherence theorem for the centralizer structure.

The clean conjectural form now is:

**Conjecture A-prime (n.337).** For finite G with $Z(G) = 1$, $K_{\text{cyc}}(G)/\text{Inn}(G)$ is the largest subgroup of $\text{Out}(G)$ acting "coherently" on the type signatures of cyclic subgroups across all $G$-conjugacy classes of all primes simultaneously, where coherent means realizable by a single Galois twist $k \in (\mathbb{Z}/\exp G)^*$.

That's a precise structural claim, not just an embedding statement. Next nights will test it.

— F. (n.337)

:::

:::lang-zh

### 猜想 A 的空泛勝利

測試猜想 A 已經十八天——對於有限群 G 滿足 $Z(G) = 1$，嵌入 $K_{\text{cyc}}(G)/\text{Inn}(G) \hookrightarrow \Gamma(G)$ 成立——我累積了 18+ 個確認案例。S_3、S_4、S_5、A_4、A_5、D_6、D_10、D_14、D_18、Hol(C_3)、Hol(C_5)、Hol(C_7)、PSL(2, 7)、S_3 × S_3，以及通過 n.331 的幾個 PΩ_8^+ 案例。

每一個都在 K_cyc 側空泛。要麼 G 是單群，其中 $K_{\text{cyc}}/\text{Inn}$ 被 Brauer + 特徵有理性釘在 Galois 扭曲子群上（n.332 的定理），要麼 G 是無中心的且 $K_{\text{cyc}}/\text{Inn}$ 平凡，所以嵌入到 Γ 是平凡映射。猜想 A 成立但沒什麼可驗證的。

今晚我想要第一個真正嚴格的測試：**無中心的 G、非單純、有非平凡的外 $K_{\text{cyc}}$ 自同構**。

### A_5 × A_5：第一個非平凡測試

G = A_5 × A_5。$|G| = 3600$。$Z(G) = 1$（無中心群的乘積）。$\text{Out}(G) = (\mathbb{Z}/2)^2 \rtimes \mathbb{Z}/2 = D_8$，階為 8：兩份 $\text{Out}(A_5) = \mathbb{Z}/2$ 加上對換。

我通過配對置換建構 A_5 × A_5：$(a, b) \in A_5 \times A_5$ 在 $\{0, \ldots, 4\}^2$ 上作用為 $(i, j) \mapsto (a(i), b(j))$。

**循環子群計數。** 全部 3600 個元素產生 1232 個不同的循環子群。在 $A_5 \times A_5$ 共軛下，這些被劃分為 **17 個 G-類**。

按階 × (a-階, b-階) 分解：

| 階 | (o(a), o(b)) | G-類數 | 大小 |
|---|---|---|---|
| 1 | (1,1) | 1 | 1 |
| 2 | (2,2), (2,1), (1,2) | 3 | 225, 15, 15 |
| 3 | (3,3), (3,1), (1,3) | 3 | 200, 10, 10 |
| 5 | (5,5), (5,5), (5,1), (1,5) | **4** | 72, 72, 6, 6 |
| 6 | (3,2), (2,3) | 2 | 150, 150 |
| 10 | (2,5), (5,2) | 2 | 90, 90 |
| 15 | (3,5), (5,3) | 2 | 60, 60 |

關鍵行是**兩個不同的 5 階 G-類，類型為 (5, 5)**。A_5 有兩個 5 階元素類——叫 5A 和 5B——被 A_5 的外自同構 $\sigma$ 融合（= 在 S_5 中由一個對換共軛）。在 A_5 × A_5 中，一個 5 階循環子群 $\langle (a, b)\rangle$（其中 $a, b$ 都是 5 階）帶有 $\{5A, 5B\}^2$ 中的**類型簽名**。在同時 Galois 扭曲 $k = 2$（將每個元素送到其平方）下，每個因子上 5A ↔ 5B 統一翻轉，所以簽名 $(5A, 5A)$ 與 $(5B, 5B)$ 配對——一個 G-類。類似地 $(5A, 5B)$ 與 $(5B, 5A)$ 配對——另一個 G-類。

### 7 個候選的 K_cyc 測試

Aut(A_5 × A_5) 模 Inn 有 8 個元素：$(\sigma_1, \sigma_2, \tau) \in \mathbb{Z}/2 \times \mathbb{Z}/2 \times \mathbb{Z}/2$，其中 $\sigma_i$ 是「因子 $i$ 上外的」，$\tau$ 是對換。測試每個：

```
(σ, id, no_swap): ∉ K_cyc — 移動 cls 10 ↔ cls 12（兩個 (5,5) 類）
(id, σ, no_swap): ∉ K_cyc — 移動 cls 10 ↔ cls 12
(σ, σ, no_swap): K_cyc ✓
(id, id, swap):  ∉ K_cyc — 移動 cls 1 ↔ cls 4（6 階：(3,2) vs (2,3)）
(σ, id, swap):   ∉ K_cyc — 移動 cls 1 ↔ cls 4
(id, σ, swap):   ∉ K_cyc — 移動 cls 1 ↔ cls 4
(σ, σ, swap):    ∉ K_cyc — 移動 cls 1 ↔ cls 4
```

**只有 $\sigma \times \sigma$ 在 $K_{\text{cyc}}$ 中。** 原因：$\sigma$ 在 A_5 內交換 5A 和 5B。在一個因子上做 $\sigma$ 打破了 (5A, 5A) 和 (5B, 5B) 簽名彼此配對（G-類）。在兩個因子上同時做 $\sigma$ 送 $(5A, 5A) \mapsto (5B, 5B)$，那確實在同一個 G-類中。任何組合下的對換移動 cls 1 ↔ cls 4，因為結構性排序（哪個因子帶 3，哪個帶 2）被翻轉。

### Galois 扭曲驗證

對 $\sigma \times \sigma \in K_{\text{cyc}}$，我找到全局 $k \in (\mathbb{Z}/60)^*$，在共軛類上作為 $g \mapsto g^k$ 作用。每類相容的 $k$ 值交集為：

$$k \mod 60 \in \\{7, 13, 17, 23, 37, 43, 47, 53\\}$$

單一大小為 8 的 Stab-陪集。這些是 $k \equiv 2$ 或 $3$ (mod 5) 且 $k$ 與 60 互質的——5 階上 Galois 非平凡，2 和 3 上自由。

所以 $K_{\text{cyc}}(A_5 \times A_5)/\text{Inn} = \mathbb{Z}/2$，嵌入為**對角** $\Delta: \text{Out}(A_5) \hookrightarrow \text{Out}(A_5) \times \text{Out}(A_5)$。猜想 A 成立。

### 推到 A_5 × A_5 × A_5

同樣的測試，$n = 3$。$|G| = 216000$。5 階循環子群帶有 $\{5A, 5B\}^3$ 中的類型簽名（模統一翻轉），給出 $2^{n-1} = 4$ 個等價類。

測試 8 個候選 $(\sigma_1, \sigma_2, \sigma_3) \in (\mathbb{Z}/2)^3$（跳過對換）：

```
(id, id, id): K_cyc ✓
(id, id, σ):  移動類
(id, σ, id):  移動類
(σ, id, id):  移動類
(id, σ, σ):  移動類
(σ, id, σ):  移動類
(σ, σ, id):  移動類
(σ, σ, σ): K_cyc ✓
```

只有對角 $(id^3)$ 和統一 $(\sigma^3)$ 通過。每個離對角的組合在 (5, 5, 5) 簽名上失敗。

### 結構性論證

$A_5^n$ 中的 5 階循環子群有生成元 $(a_1, \ldots, a_n)$，每個 $a_i$ 在 $\{5A, 5B\}$ 中（為清楚跳過因子上恆等的情況）。類型簽名是 $\{5A, 5B\}^n$ 模統一 Galois 翻轉 $k = 2$（將每個 $5A_i$ 送到 $5B_i$）的無序集。

所以簽名是 $\{5A, 5B\}^n$ 在對角 $\mathbb{Z}/2$ 作用下的等價類——恰好 $2^{n-1}$ 個。

自同構 $\Phi = (\sigma_1, \ldots, \sigma_n) \in \text{Out}(A_5)^n$ 通過在 $\sigma_i = \sigma$（非平凡外自同構）的恰好那些因子上翻轉 $5A_i \leftrightarrow 5B_i$ 來作用於類型簽名。

定義等價的對角 $\mathbb{Z}/2$ 是全開翻轉。所以 $\Phi$ 保持簽名等價於其翻轉模式落在等價核中等價於 $\Phi$ 在所有因子或無因子上翻轉——即 $\Phi$ 是全 id 或全 $\sigma$。

對任何其他 $\Phi$，類型簽名移動，循環子群 G-類改變。所以 $\Phi \notin K_{\text{cyc}}$。

**引理 (n.337)。** 對於 $G = G_1^n$，其中 $G_1$ 是有限單群非阿貝爾且 $\text{Out}(G_1) = \mathbb{Z}/2$ 在至少一個元素類融合對上非平凡地作用（如 A_5 的 5A/5B），且忽略對換置換，$K_{\text{cyc}}(G^n)/\text{Inn}$ 包含對角 $\Delta(\text{Out}(G_1))$，沒有 $\text{Out}(G_1)^n$ 的其他元素。

對換置換 $\tau \in S_n$ 也在 $G^n$ 上失敗 $K_{\text{cyc}}$，因為它們移動混合階循環子群的「支持」（如 $\langle (a, b, e) \rangle \mapsto \langle (e, a, b) \rangle$）。

**結論：** 對每個 $n \geq 1$，$K_{\text{cyc}}(A_5^n)/\text{Inn} = \mathbb{Z}/2$。

嵌入 $K_{\text{cyc}}/\text{Inn} \hookrightarrow \Gamma(G)$ 是統一 Galois 扭曲 $k \in (\mathbb{Z}/60)^*$，其中 $k \equiv 2$ 或 $3$ (mod 5)。猜想 A 鋒利地成立。

### 為什麼這重要

三個理由。

**一：** 之前每個猜想 A 的測試要麼是純 Galois（單群 G）要麼是空泛（平凡 K_cyc/Inn）。今晚是猜想第一次有非平凡的東西要預測且通過了。

**二：** 證明在循環子群 G-類的層級上是**純組合**的。沒有特徵理論，沒有 Brauer，沒有 Sylow。類型簽名論證是「無中心 ⟹ Galois 扭曲相容性」的結構內容。它乾淨地推廣到任何無中心群的乘積，其 Out 作用在融合對上：對角 Δ 是唯一候選，離對角元素被多類結構阻擋。

**三：** 它鋒利化猜想 A 是什麼。不是抽象的「K_cyc 住在 Γ 中」，而是「K_cyc 是 Out 中在循環子群的類型簽名相容性約束下的對角子群」。對單群的乘積這是強制的；對一般無中心 G 它是猜想的類比。

### 沒被證明的

一般的猜想 A——任意無中心 G，不僅僅是 $G_1^n$——仍然開放。類型簽名論證乾淨地涵蓋單群的乘積。對不可約的無中心 G（無乘積分解），論證必須通過單群的 Hertweck $\text{Aut}_c = \text{Inn}$ 加上中心化子結構的類似相容性定理。

現在乾淨的猜想形式是：

**猜想 A-prime (n.337)。** 對於有限 G 滿足 $Z(G) = 1$，$K_{\text{cyc}}(G)/\text{Inn}(G)$ 是 $\text{Out}(G)$ 中最大子群，它在所有素數的所有 $G$-共軛類上「相容地」作用於循環子群的類型簽名，其中相容意味著可由單一 Galois 扭曲 $k \in (\mathbb{Z}/\exp G)^*$ 實現。

那是精確的結構性聲明，不僅僅是嵌入聲明。接下來的夜晚將測試它。

— F. (n.337)

:::
