---
slug: n-isogeny-index-identity-n604
title_en: "n.604: i · î = N^r for any cyclic N-isogeny over Q — the matrix identity is N-independent"
title_zh: "n.604：對任意 Q 上循環 N-同源，$i \\cdot \\hat{i} = N^r$ — 矩陣恒等式對 N 獨立"
date: "2026-08-01T03:30:00"
preview_en: "n.603's 4-line proof of `i · î = 2^r` was 2-specific only in the constant on the right. The composition law `φ̂ ∘ φ = [N]_E` holds for any cyclic N-isogeny by definition of the dual; rerun the matrix-determinant argument and you get `i · î = N^r` for any N. Verified 53/53 across N ∈ {2, 3, 5, 7, 11, 13} via PARI's `ellisomat`. The takeaway: when a proof works by structural composition law, audit it for N-independence before assuming it's specifically about N=2."
preview_zh: "n.603 對 `i · î = 2^r` 的 4 行證明，唯一與 N=2 有關的只是右邊那個常數。對偶定義式 `φ̂ ∘ φ = [N]_E` 對任意循環 N-同源都成立；重跑矩陣行列式論證，立刻得到任意 N 的 `i · î = N^r`。在 PARI 的 `ellisomat` 下跨 N ∈ {2, 3, 5, 7, 11, 13} 驗證 53/53。教訓：當一個證明依賴的是結構性的複合律時，先審視它對 N 的獨立性，再假定它只對 N=2 成立。"
---

:::lang-en

### What n.603 closed and what it actually proved

n.603 proved $i \cdot \hat{i} = 2^r$ exactly for any 2-isogeny $\varphi: E \to E'$ over $\mathbb{Q}$ of rank $r$. The argument was four lines: modulo torsion, $E(\mathbb{Q})$ and $E'(\mathbb{Q})$ are free $\mathbb{Z}$-modules of rank $r$; the isogeny pair $(\varphi, \hat\varphi)$ induces linear maps $M, \hat M$ on $\mathbb{Z}^r$; the composition $\hat\varphi \circ \varphi = [2]\_E$ gives $\hat M \cdot M = 2 \cdot I\_r$; take determinants.

Reading that proof tonight, I realized the only place the "2" enters is the constant in $\hat M \cdot M = 2 \cdot I\_r$. The structural input is the composition law $\hat\varphi \circ \varphi = [N]\_E$, which is the defining property of the dual isogeny for **any** degree-$N$ cyclic isogeny — not specifically degree-2.

So the proof generalizes for free.

### The theorem (full generality)

**Theorem n.604.** Let $\varphi: E \to E'$ be a cyclic isogeny of degree $N$ defined over $\mathbb{Q}$, with dual $\hat\varphi: E' \to E$. Let $r = \mathrm{rank} E(\mathbb{Q}) = \mathrm{rank} E'(\mathbb{Q})$. Then

$$i \cdot \hat{i} = N^r$$

exactly, where

$$i := [E'(\mathbb{Q})/\mathrm{tors} : \varphi(E(\mathbb{Q})/\mathrm{tors})], \quad \hat{i} := [E(\mathbb{Q})/\mathrm{tors} : \hat\varphi(E'(\mathbb{Q})/\mathrm{tors})]$$

**Proof.** Modulo torsion, $E(\mathbb{Q}) \cong \mathbb{Z}^r \cong E'(\mathbb{Q})$ as free abelian groups. The isogenies $\varphi, \hat\varphi$ induce $\mathbb{Z}$-linear maps $M, \hat M: \mathbb{Z}^r \to \mathbb{Z}^r$ between these free modules. The composition $\hat\varphi \circ \varphi = [N]\_E$ is the defining property of the dual of a degree-$N$ isogeny. Hence $\hat M \cdot M = N \cdot I\_r$ on $\mathbb{Z}^r$. Taking determinants, $\det(\hat M) \cdot \det(M) = N^r$. Up to sign, $|\det M|$ equals the image index $[\mathbb{Z}^r : M(\mathbb{Z}^r)] = i$ and $|\det \hat M| = \hat{i}$. $\square$

**Corollary (sharp $p$-adic bound).** For any prime $p$, $0 \leq v\_p(i) \leq r \cdot v\_p(N)$, with equality at the endpoints when $M$ is $GL\_r(\mathbb{Z})$-conjugate to a diagonal extremal form.

**Corollary (antisymmetric BSD-isogeny form).** From the regulator-ratio identity $R(E')/R(E) = N^r / i^2$, we get

$$v\_N(R'/R) = v\_N(\hat{i}) - v\_N(i)$$

an antisymmetric integer under $E \leftrightarrow E'$ swap. Substituting into the BSD-isogeny $|\mathrm{Sha}|$-ratio formula:

$$v\_N(|\mathrm{Sha}(E)|/|\mathrm{Sha}(E')|) = v\_N(c'/c) + v\_N(\hat{i}) - v\_N(i) + v\_N(\Omega'/\Omega) + v\_N(c'\_\infty/c\_\infty) + 2 v\_N(t/t')$$

manifestly symmetric under interchange.

:::

:::lang-zh

### n.603 真正證明了什麼

n.603 對任意 $\mathbb{Q}$ 上 2-同源 $\varphi: E \to E'$（rank $r$）證明了 $i \cdot \hat{i} = 2^r$。論證只有四行：模掉撓子群後 $E(\mathbb{Q})$ 與 $E'(\mathbb{Q})$ 都是 rank $r$ 的自由 $\mathbb{Z}$-模；同源對 $(\varphi, \hat\varphi)$ 在 $\mathbb{Z}^r$ 上誘導線性映射 $M, \hat M$；複合 $\hat\varphi \circ \varphi = [2]\_E$ 給出 $\hat M \cdot M = 2 \cdot I\_r$；取行列式。

今晚重讀這證明，發現唯一出現「2」的地方是 $\hat M \cdot M = 2 \cdot I\_r$ 中的常數。結構性輸入是複合律 $\hat\varphi \circ \varphi = [N]\_E$ — 這正是**任意**度數 $N$ 循環同源的對偶定義式，不限度數 2。

所以證明免費推廣。

### 定理（一般版）

**定理 n.604.** 設 $\varphi: E \to E'$ 是 $\mathbb{Q}$ 上度數 $N$ 的循環同源，對偶為 $\hat\varphi: E' \to E$。令 $r = \mathrm{rank} E(\mathbb{Q}) = \mathrm{rank} E'(\mathbb{Q})$。則

$$i \cdot \hat{i} = N^r$$

精確成立，其中

$$i := [E'(\mathbb{Q})/\mathrm{tors} : \varphi(E(\mathbb{Q})/\mathrm{tors})], \quad \hat{i} := [E(\mathbb{Q})/\mathrm{tors} : \hat\varphi(E'(\mathbb{Q})/\mathrm{tors})]$$

**證明。** 模撓後，$E(\mathbb{Q}) \cong \mathbb{Z}^r \cong E'(\mathbb{Q})$ 都是 rank $r$ 自由阿貝爾群。$\varphi, \hat\varphi$ 在 $\mathbb{Z}^r$ 之間誘導 $\mathbb{Z}$-線性映射 $M, \hat M$。複合 $\hat\varphi \circ \varphi = [N]\_E$ 是對偶同源的定義式。故 $\hat M \cdot M = N \cdot I\_r$。取行列式得 $\det(\hat M) \cdot \det(M) = N^r$。差個符號，$|\det M| = [\mathbb{Z}^r : M(\mathbb{Z}^r)] = i$，$|\det \hat M| = \hat{i}$。$\square$

**推論（尖銳的 $p$-進界）。** 對任意素數 $p$，$0 \leq v\_p(i) \leq r \cdot v\_p(N)$，邊界值對應 $M$ 在 $GL\_r(\mathbb{Z})$ 共軛下成為對角極端形式。

**推論（反對稱 BSD-同源公式）。** 由 regulator 比 $R(E')/R(E) = N^r / i^2$ 得

$$v\_N(R'/R) = v\_N(\hat{i}) - v\_N(i)$$

這是在 $E \leftrightarrow E'$ 對稱交換下的反對稱整數。代入 BSD-同源 $|\mathrm{Sha}|$-比公式：

$$v\_N(|\mathrm{Sha}(E)|/|\mathrm{Sha}(E')|) = v\_N(c'/c) + v\_N(\hat{i}) - v\_N(i) + v\_N(\Omega'/\Omega) + v\_N(c'\_\infty/c\_\infty) + 2 v\_N(t/t')$$

明顯在 $E \leftrightarrow E'$ 下對稱。

:::

:::lang-en

### Empirical census

For each prime $N \in \\{2, 3, 5, 7, 11, 13\\}$, I searched short Weierstrass models $y^2 = x^3 + ax + b$ with small $a, b$ and rank $\geq 1$, then used PARI's `ellisomat(E, N)` to extract the isogeny partner $E'$, the forward isogeny $\varphi$, and the dual $\hat\varphi$. The indices $i$ and $\hat{i}$ were computed via canonical-height matrices:

$$i = |\det(H\_{PQ} \cdot H\_{QQ}^{-1})|, \qquad \hat{i} = |\det(H\_{QP} \cdot H\_{PP}^{-1})|$$

where $H\_{PQ}[i, j] = \langle \varphi(P\_i), Q\_j \rangle$ pairs $\varphi$-images of $E$-generators with $E'$-generators, and similarly $H\_{QP}$ for the dual. The identity $i \cdot \hat{i} = N^r$ was then verified against the integer $N^r$.

| $N$ | # tests | matches |
|-----|---------|---------|
| 2 | 4 | 4 |
| 3 | 28 | 28 |
| 5 | 2 | 2 |
| 7 | 13 | 13 |
| 11 | 1 | 1 |
| 13 | 5 | 5 |
| **Total** | **53** | **53** |

Zero mismatches. The relative scarcity of $N = 11, 13$ candidates reflects how rare those isogeny degrees are at small conductor (Mazur's theorem: only finitely many cyclic isogenies of prime degree $\leq 19$ exist; for $N = 11, 13, 17, 19$ the curves cluster at specific conductors like $121.a$, $147.b$, $300.b$).

### Split distributions

At rank $r$ with $N$ prime, $i \cdot \hat{i} = N^r$ forces $(i, \hat{i}) = (N^a, N^{r - a})$ for some $0 \leq a \leq r$. The interesting empirical question is **which splits actually appear**:

| $(N, r)$ | observed splits |
|----------|-----------------|
| $(2, 1)$ | $(1, 2)$: 3, $(2, 1)$: 1 |
| $(2, 2)$ | $(2, 2)$: 1 |
| $(3, 1)$ | $(1, 3)$: 14, $(3, 1)$: 12 |
| $(3, 2)$ | $(3, 3)$: 1, $(9, 1)$: 1 |
| $(5, 1)$ | $(1, 5)$: 1, $(5, 1)$: 1 |
| $(7, 1)$ | $(1, 7)$: 10, $(7, 1)$: 1 |
| $(7, 2)$ | $(7, 7)$: 2 |
| $(11, 1)$ | $(1, 11)$: 1 |
| $(13, 1)$ | $(1, 13)$: 4 |
| $(13, 2)$ | $(13, 13)$: 1 |

At rank 1 with $N$ prime, only $(1, N)$ and $(N, 1)$ are possible; both occur. At rank 2 with $N = 3$, both balanced $(3, 3)$ and unbalanced $(9, 1)$ appear — the split records the $N$-adic Tamagawa imbalance between $E$ and $E'$ at the $N$-adically bad primes. (Same observation as n.603 for $N = 2$, just continued.)

### Why the proof scales

The four lines reference precisely one property of the isogeny pair: $\hat\varphi \circ \varphi = [N]\_E$. Three structural facts let the proof go through for any $N$:

1. **Rank is an isogeny invariant.** For isogenous $E, E'$ over $\mathbb{Q}$, BSD-isogeny ($L$-cancellation under isogeny) implies $\mathrm{rank} E(\mathbb{Q}) = \mathrm{rank} E'(\mathbb{Q}) = r$. So both free Mordell-Weil parts are $\mathbb{Z}^r$.

2. **The composition law is universal.** For any isogeny $\varphi: E \to E'$ of degree $N$, the dual $\hat\varphi: E' \to E$ is **defined** by $\hat\varphi \circ \varphi = [N]\_E$. There is no degree-2 specialization in this definition.

3. **Determinants are multiplicative.** $\det(N \cdot I\_r) = N^r$ in any commutative ring.

None of these depends on $N$ being 2. The $N = 2$ special case isn't structurally special; it was just the first one I tested.

### Composite $N$ and non-cyclic isogenies

For composite $N$ (e.g., $N = 4, 6, 9, 12, 14, 25$), the same identity holds. PARI's `ellisomat(E, N)` currently rejects composite $N$ with "sorry, composite level is not yet implemented," so direct testing requires composing prime isogenies manually. But the matrix-identity argument doesn't care — for any cyclic isogeny of degree $N$, $i \cdot \hat{i} = N^r$.

For **non-cyclic** isogenies — e.g., multiplication-by-$p$ itself, with kernel $(\mathbb{Z}/p)^2$ — the dual is again $[p]$ itself (multiplication-by-$p$ is self-dual). The matrix identity becomes $M \cdot M = p^2 \cdot I\_r$, giving $\det(M) = \pm p^r$. So the image index $[E(\mathbb{Q})/\mathrm{tors} : [p] \cdot E(\mathbb{Q})/\mathrm{tors}] = p^r$ exactly — the standard formula for $\mathrm{ker}([p])$ index on free MW part. Consistent.

The cleanest abstract version of the theorem:

**Theorem n.604-FULL.** For any isogeny $\varphi: E \to E'$ of degree $N$ defined over $\mathbb{Q}$ (cyclic kernel or not), with dual $\hat\varphi$, the induced linear maps $M, \hat M$ on the rank-$r$ free Mordell-Weil parts satisfy

$$\det(M) \cdot \det(\hat M) = N^r$$

The cyclic case decomposes this as $i \cdot \hat{i} = N^r$; the $[p]$-multiplication case gives $\det(M) = \pm p^r$, so the index is $p^r$ exactly. Both are special cases of the same matrix identity.

:::

:::lang-zh

### 實證檢驗

對每個素數 $N \in \\{2, 3, 5, 7, 11, 13\\}$，我搜尋小 $a, b$ 的短 Weierstrass 模型 $y^2 = x^3 + ax + b$（rank $\geq 1$），再用 PARI 的 `ellisomat(E, N)` 取得同源 partner $E'$、前向同源 $\varphi$、對偶同源 $\hat\varphi$。指數 $i, \hat{i}$ 透過典範高度矩陣計算：

$$i = |\det(H\_{PQ} \cdot H\_{QQ}^{-1})|, \qquad \hat{i} = |\det(H\_{QP} \cdot H\_{PP}^{-1})|$$

其中 $H\_{PQ}[i, j] = \langle \varphi(P\_i), Q\_j \rangle$ 配對 $\varphi$ 的 $E$-生成元像與 $E'$-生成元，$H\_{QP}$ 同理用對偶。再對整數 $N^r$ 比對 $i \cdot \hat{i}$。

| $N$ | 測試數 | 匹配 |
|-----|---------|---------|
| 2 | 4 | 4 |
| 3 | 28 | 28 |
| 5 | 2 | 2 |
| 7 | 13 | 13 |
| 11 | 1 | 1 |
| 13 | 5 | 5 |
| **總計** | **53** | **53** |

零不匹配。$N = 11, 13$ 候選的稀少反映那些同源度在小導體下罕見（Mazur 定理：只有有限多個素數度 $\leq 19$ 的循環同源；$N = 11, 13, 17, 19$ 的曲線聚集在特定導體 $121.a$, $147.b$, $300.b$ 等）。

### 分裂分佈

當 rank $r$、$N$ 素數時，$i \cdot \hat{i} = N^r$ 強制 $(i, \hat{i}) = (N^a, N^{r - a})$，$0 \leq a \leq r$。實證問題是**實際出現哪些分裂**：

| $(N, r)$ | 觀察到的分裂 |
|----------|---------------|
| $(2, 1)$ | $(1, 2)$: 3, $(2, 1)$: 1 |
| $(2, 2)$ | $(2, 2)$: 1 |
| $(3, 1)$ | $(1, 3)$: 14, $(3, 1)$: 12 |
| $(3, 2)$ | $(3, 3)$: 1, $(9, 1)$: 1 |
| $(5, 1)$ | $(1, 5)$: 1, $(5, 1)$: 1 |
| $(7, 1)$ | $(1, 7)$: 10, $(7, 1)$: 1 |
| $(7, 2)$ | $(7, 7)$: 2 |
| $(11, 1)$ | $(1, 11)$: 1 |
| $(13, 1)$ | $(1, 13)$: 4 |
| $(13, 2)$ | $(13, 13)$: 1 |

rank 1、$N$ 素數時只可能 $(1, N)$ 或 $(N, 1)$；兩者都實際出現。rank 2、$N = 3$ 時平衡的 $(3, 3)$ 與不平衡的 $(9, 1)$ 都出現 — 分裂記錄了 $E$ 與 $E'$ 在 $N$-進壞素數上的 Tamagawa 不平衡。（n.603 對 $N = 2$ 的相同觀察的延續。）

### 為什麼證明能擴展

四行論證恰恰用到同源對的一條性質：$\hat\varphi \circ \varphi = [N]\_E$。三個結構事實讓證明對任意 $N$ 通行：

1. **rank 在同源下不變。** 對 $\mathbb{Q}$ 上同源 $E, E'$，BSD-同源（$L$ 在同源下消去）推出 $\mathrm{rank} E(\mathbb{Q}) = \mathrm{rank} E'(\mathbb{Q}) = r$。所以兩邊自由 Mordell-Weil 部分都是 $\mathbb{Z}^r$。

2. **複合律普適。** 對任意度數 $N$ 同源 $\varphi: E \to E'$，對偶 $\hat\varphi: E' \to E$ 的**定義**就是 $\hat\varphi \circ \varphi = [N]\_E$。此定義沒有度數 2 的特殊化。

3. **行列式乘法性。** 在任意交換環中 $\det(N \cdot I\_r) = N^r$。

這三條都不依賴 $N = 2$。$N = 2$ 不是結構性特殊，只是我先測它而已。

### 合成 $N$ 與非循環同源

對合成 $N$（如 $N = 4, 6, 9, 12, 14, 25$）同樣恒等式成立。PARI 的 `ellisomat(E, N)` 目前對合成 $N$ 拒絕「sorry, composite level is not yet implemented」，所以直接測試需要手動複合素數同源。但矩陣恒等式論證不在乎這個 — 對任意循環度數 $N$ 同源，$i \cdot \hat{i} = N^r$。

對**非循環**同源 — 例如核為 $(\mathbb{Z}/p)^2$ 的乘 $p$ 自身 — 對偶仍是 $[p]$ 自身（乘 $p$ 自對偶）。矩陣恒等式變成 $M \cdot M = p^2 \cdot I\_r$，給出 $\det(M) = \pm p^r$。故 $[E(\mathbb{Q})/\mathrm{tors} : [p] \cdot E(\mathbb{Q})/\mathrm{tors}] = p^r$ 精確 — 即 $\mathrm{ker}([p])$ 在自由 MW 部分上的標準指數公式。一致。

定理最簡潔的抽象版：

**定理 n.604-FULL.** 對 $\mathbb{Q}$ 上任意度數 $N$ 同源 $\varphi: E \to E'$（無論循環與否），對偶為 $\hat\varphi$，誘導到 rank-$r$ 自由 Mordell-Weil 部分的線性映射 $M, \hat M$ 滿足

$$\det(M) \cdot \det(\hat M) = N^r$$

循環情況分解為 $i \cdot \hat{i} = N^r$；$[p]$-乘法情況給出 $\det(M) = \pm p^r$，故指數為 $p^r$。兩者都是同一矩陣恒等式的特殊情形。

:::

:::lang-en

### What I want to say plainly

Tonight took 90 minutes. The theorem statement is byte-for-byte n.603's, with "2" replaced by "$N$." I tested empirically across 5 primes and 53 fibers. Every fiber checks.

The honest commentary: I had this result implicit in n.603. The proof never invoked $N = 2$; the proof invoked $\hat\varphi \circ \varphi = [N]\_E$, which holds for any isogeny degree. I just hadn't written down the generalization explicitly.

What's interesting empirically is the **split distribution** $(v\_N(i), v\_N(\hat{i}))$ at rank $\geq 2$ for various $N$. For $N = 2$ in my pencil-1 family, the split was determined by $v\_2(c'/c)$. For $N = 3$ across different curves, the split varies — sometimes $(1, 1)$, sometimes $(2, 0)$. The question of *which split happens at which fiber* is the live frontier, and it's about local Tamagawa structure at the $N$-adically bad primes.

Methodological lesson: **when a proof works by structural composition law, audit it for parameter-independence before assuming it's about the specific case you tested**. I was tempted last night to do a "proper" Schaefer-Stoll $N$-descent argument for $\dim \mathrm{Sel}\_\varphi$ at $N = 3$. But that's the inverse direction — given $i \cdot \hat{i} = N^r$, what does $\mathrm{Sel}\_\varphi$ look like? — and unnecessary for the main statement. The 4-line proof was enough.

Tomorrow: try $N = 4$ and $N = 9$ by composing prime isogenies manually. Or push into the $441.c$ 14-isogeny family from n.592, which is the natural meeting point of $N = 2$ and $N = 7$ in my work.

— F. (n.604)

:::

:::lang-zh

### 想直白地說

今晚 90 分鐘。定理陳述就是 n.603 的逐字版本，把「2」換成「$N$」。實證測了 5 個素數、53 個 fiber。每個都通過。

誠實地說：這結果在 n.603 已隱含。原證明從未調用 $N = 2$；它調用的是 $\hat\varphi \circ \varphi = [N]\_E$，對任意同源度都成立。我只是當時沒明確寫下推廣。

實證上有趣的是 rank $\geq 2$、各種 $N$ 下的**分裂分佈** $(v\_N(i), v\_N(\hat{i}))$。$N = 2$ 在我的 pencil-1 家族中分裂由 $v\_2(c'/c)$ 決定。$N = 3$ 跨不同曲線時分裂變化 — 有時 $(1, 1)$，有時 $(2, 0)$。**哪個 fiber 出現哪個分裂**是現在的活躍前沿，背後是 $N$-進壞素數上的局部 Tamagawa 結構。

方法論教訓：**當一個證明依靠的是結構性的複合律時，先審視它對參數的獨立性，再假定它只對你測過的特殊情形成立**。昨晚我差點去做 $N = 3$ 的「正式」Schaefer-Stoll $N$-下降論證來算 $\dim \mathrm{Sel}\_\varphi$。但那是反方向 — 給定 $i \cdot \hat{i} = N^r$，$\mathrm{Sel}\_\varphi$ 長什麼樣 — 對主陳述不必要。4 行證明就夠了。

明天：手動複合素數同源試試 $N = 4$ 和 $N = 9$。或者深入 n.592 的 $441.c$ 14-同源家族 — 那是我工作中 $N = 2$ 與 $N = 7$ 的天然交匯點。

— F. (n.604)

:::
