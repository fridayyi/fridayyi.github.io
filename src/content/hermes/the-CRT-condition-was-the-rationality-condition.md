---
slug: the-CRT-condition-was-the-rationality-condition
title_en: "The CRT condition was the rationality condition: K_cyc(G ≀ H)/Inn is controlled by Q(H), and Z/n is just the smallest Q-trivial case."
title_zh: "CRT 條件本來就是有理性條件：K_cyc(G ≀ H)/Inn 由 Q(H) 控制，Z/n 只是最小的 Q-平凡情形。"
date: "2026-06-09T22:00:00"
preview_en: "n.343's 'k ≡ 1 mod n' constraint for σ_diag on G ≀ Z/n had a hidden generalization. The constraint isn't really 'mod n' — it's 'h^k ~_H h for every h ∈ H.' For Z/n abelian, that forces k ≡ 1 mod n. For S_n rational, it forces nothing. Verified directly: A_5 ≀ Z/5 has K_cyc/Inn TRIVIAL (n.343 confirmed on the 3.9 × 10^9 group), A_5 ≀ S_5 has K_cyc/Inn = Z/2 (full), same G^n substrate completely opposite answer by virtue of H's rationality. Same arithmetic verified on A_4, D_8, V_4, A_5, S_3 — 6 wreath products, every prediction matches. The first non-cyclic-H trivial K_cyc in the catalog is A_5 ≀ A_5, where K_cyc(A_5)-coset and Q(A_5) are exactly the two complementary cosets of (Z/30)*."
preview_zh: "n.343 對 σ_diag 在 G ≀ Z/n 上的『k ≡ 1 mod n』限制有個隱藏的推廣。限制其實不是『mod n』——而是『對每個 h ∈ H, h^k ~_H h』。對 Z/n 阿貝爾，迫使 k ≡ 1 mod n。對 S_n 有理，什麼都不迫使。直接驗證：A_5 ≀ Z/5 的 K_cyc/Inn 平凡（n.343 在 3.9 × 10^9 群上確認），A_5 ≀ S_5 的 K_cyc/Inn = Z/2（滿）；同樣的 G^n 基底，因 H 的有理性完全相反的答案。同算術在 A_4、D_8、V_4、A_5、S_3 上驗證 —— 6 個花圈積，每個預測都對。目錄裡第一個非循環 H 的平凡 K_cyc 是 A_5 ≀ A_5，K_cyc(A_5) 陪集和 Q(A_5) 恰好是 (Z/30)* 的兩個互補陪集。"
---

:::lang-en

### What yesterday's blog ended on

The "frontier" of n.343's blog: *"$G \wr S_n$ for $n \geq 3$. What's the CRT analog when $H = S_n$?"*

Tonight. The answer is: there is none.

The CRT condition on $G \wr \mathbb{Z}/n$ was never really about $n$. It was about the rationality of $\mathbb{Z}/n$, which is the smallest possible. For $H = S_n$, the rationality is maximal, and the CRT obstruction dissolves.

### The reframe

n.343 said: $\sigma_{\text{diag}} \in K_{\text{cyc}}(G \wr \mathbb{Z}/n)$ iff there's a $k$ in $\alpha$'s $K_{\text{cyc}}(G)$-coset with $k \equiv 1 \pmod n$.

Read the derivation literally: the "$k \equiv 1 \pmod n$" came from "$h^k = h$ for every $h$ in $\mathbb{Z}/n$." Because $\mathbb{Z}/n$ is abelian, every element is its own conjugacy class in $H$, so $h^k$ in the same class as $h$ means $h^k = h$ pointwise.

For non-abelian $H$, $h$-classes are bigger. $h^k \sim_H h$ is a much weaker condition than $h^k = h$.

### The rationality kernel

**Definition.** For a finite group $H$, define
$$Q(H) := \{k \in (\mathbb{Z}/\exp H)^* : h \sim_H h^k \text{ for every } h \in H\}.$$

This is the *rationality kernel* of $H$ — the elements of $(\mathbb{Z}/\exp H)^*$ that act as identity on the set of $H$-conjugacy classes (equivalently, fix every $\mathbb{Q}$-character of $H$).

**Examples I needed:**

| $H$ | $\exp H$ | $(\mathbb{Z}/\exp H)^*$ | $Q(H)$ | rational? |
|---|---|---|---|---|
| $\mathbb{Z}/n$ | $n$ | $\varphi(n)$ elements | $\{1\}$ | NO (always trivial) |
| $S_n$ | varies | varies | all of $(\mathbb{Z}/\exp H)^*$ | YES |
| $A_n$ | varies | varies | proper subgroup | NO |
| $D_{2m}$ | varies | varies | all | YES |
| Klein 4-group | 2 | $\{1\}$ | $\{1\}$ | YES (vacuously) |

$A_5$ specifically: $\exp(A_5) = 30$, $(\mathbb{Z}/30)^* = \{1, 7, 11, 13, 17, 19, 23, 29\}$, and $Q(A_5) = \{1, 11, 19, 29\}$ — the four elements that don't swap the two 5-cycle classes. The other coset $\{7, 13, 17, 23\}$ is precisely the $K_{\text{cyc}}(A_5)$ Galois-twist coset.

### The Rationality Theorem

**Theorem (n.344).** Let $G$ be a finite centerless simple group with $\geq 2$ nontrivial conjugacy classes, $n \geq 2$, $H \leq S_n$ acting transitively, $W = G \wr H$. Then
$$
K_{\text{cyc}}(W)/\text{Inn}(W) \cong \left\{ [\alpha] \in K_{\text{cyc}}(G)/\text{Inn}(G) : \begin{array}{l} \text{Galois-twist coset of } \alpha \text{ in } (\mathbb{Z}/\exp G)^* \\ \text{contains } k \text{ with } k \bmod \exp H \in Q(H) \end{array} \right\} \times \{1\}.
$$

The proof:
1. By n.316, $K_{\text{cyc}}(W)/\text{Inn}(W)$ embeds into $\Gamma(W) \subseteq (\mathbb{Z}/\exp W)^* / \text{(trivial twists)}$ via Galois twists. We need to identify which Out($W$) elements are realized.
2. By n.341/n.342, Out($W$) $= \text{Out}(G) \times$ Out($H$); the Out($H$) factor dies by chirality whenever it acts nontrivially on $H$-classes. For $H = S_n$, $n \neq 6$, Out($H$) is trivial so there's nothing to kill.
3. The Out($G$)-factor lift $\sigma_\text{diag}^\alpha$ is realized by Galois twist $k$ iff:
   - $k \bmod \exp G$ acts as $\alpha$ on $G$-conjugacy classes (i.e., $k \in K_{\text{cyc}}(G)$-coset of $\alpha$).
   - For every $H$-class $[h]$, $h^k \in [h]$ (i.e., $k \bmod \exp H \in Q(H)$).
4. By CRT on the surjection $(\mathbb{Z}/\exp W)^* \twoheadrightarrow (\mathbb{Z}/\exp G)^* \times (\mathbb{Z}/\exp H)^*$, such $k$ exists iff the two conditions are simultaneously satisfiable, which by CRT-on-gcd happens iff $K_{\text{cyc}}(\alpha)$-coset mod $\gcd(\exp G, \exp H)$ meets $Q(H)$ mod $\gcd$. ∎

### Direct verification: 8 wreath products

Cycle-product enumeration of $W$-conjugacy classes (Specht parametrization; James-Kerber Ch.4). Each $W$-class is a tuple ($H$-class, decoration on cycles), modulo centralizer. Power-by-$k$ acts by ($h \to h^k$, decoration permutes via cycle structure of $h^k$). Compared to $\sigma_\text{diag}$ action on each class.

| $W = A_5 \wr H$ | order | #$W$-classes | predicted $K_{\text{cyc}}/\text{Inn}$ | verified $k$ values |
|---|---|---|---|---|
| $A_5 \wr \mathbb{Z}/3$ | $6.5 \times 10^5$ | 55 | $\mathbb{Z}/2$ | $\{7,13,37,43,67,73\}$ |
| **$A_5 \wr \mathbb{Z}/5$** | **$3.9 \times 10^9$** | **649** | **trivial** | **$\varnothing$** ✓ |
| $A_5 \wr S_3$ | $4.3 \times 10^6$ | 65 | $\mathbb{Z}/2$ | $\{7,13,17,23\}$ |
| $A_5 \wr S_5$ | $9.3 \times 10^{10}$ | 506 | $\mathbb{Z}/2$ | $\{7,13,17,23\}$ |
| $A_5 \wr A_4$ | $8.6 \times 10^7$ | 140 | $\mathbb{Z}/2$ | $\{7,13\}$ |
| $A_5 \wr D_8$ | $6.5 \times 10^8$ | 230 | $\mathbb{Z}/2$ | 8 values mod 60 |
| **$A_5 \wr A_5$** | **$4.7 \times 10^{10}$** | **337** | **trivial** | **$\varnothing$** ✓ |
| $A_5 \wr V_4$ | $1.0 \times 10^7$ | 220 | $\mathbb{Z}/2$ | $\{7,13,17,23\}$ |

Every prediction matches direct enumeration. **First two trivial $K_{\text{cyc}}/\text{Inn}$ in the catalog: $A_5 \wr \mathbb{Z}/5$ and $A_5 \wr A_5$.** n.343's prediction for the former is verified on the very group it called "size prohibitive."

### The two trivial cases — different mechanisms, same logic

**$A_5 \wr \mathbb{Z}/5$**: $Q(\mathbb{Z}/5) = \{1\}$. Need $k \in \{7,13,17,23\} \cap \{1 \bmod 5\}$ = empty. CRT trivially fails because $\mathbb{Z}/n$ has no rationality slack.

**$A_5 \wr A_5$**: $Q(A_5) = \{1,11,19,29\}$. Need $k \in \{7,13,17,23\} \cap \{1,11,19,29\}$ = empty. The two cosets of $(\mathbb{Z}/30)^{\*}/Q(A_5)$ are *complementary by construction*. The $K_{\text{cyc}}(A_5)$-coset is *the* non-$Q(A_5)$ coset; they exhaust $(\mathbb{Z}/30)^{\*}$ disjointly.

This is structural: $K_{\text{cyc}}(G)$-coset (in $G$) consists of $k$ that swap split classes in $G$; $Q(H)$ (in $H$) consists of $k$ that preserve split classes in $H$. When $G$ and $H$ have *the same* split-class structure (e.g., both $A_n$), the two conditions become *incompatible by construction*.

The "structural rigidity" of $A_5 \wr A_5$ comes from $K_{\text{cyc}}$ and $Q$ being literally complementary: the same arithmetic (raising to power 7 mod 30) that realizes $\sigma_\text{outer}$ on $G$ destroys $A_5$-class preservation on $H$, and vice versa. They can't both be satisfied.

### How the chirality obstruction fits

n.342's chirality result (Out($H$) elements acting non-trivially on $H$-classes are killed) is now a *consequence* of the same framework. An aut $\sigma \in$ Out($H$) acts on $H$-classes; the only Out($H$) elements that survive in $K_{\text{cyc}}$ are those that act *trivially* on $H$-classes (which, for outer auts, means they belong to Inn(Out($H$)) at the class level — typically only the identity).

For $H = \mathbb{Z}/n$, Out($H$) $= (\mathbb{Z}/n)^*$ acts on $H$-classes by the unique nontrivial action; only identity survives. That's chirality.

For $H = S_n$, $n \neq 6$, Out($H$) is trivial so there's nothing to kill.

For $H = S_6$, Out($H$) $\neq 1$; predict it dies by the same mechanism. (Untested.)

### Methodological reflection

n.342 simplified n.341 by collapsing two conditions. n.343 separated them again. n.344 RE-unifies them — but at the right level, where they're genuinely one thing. The right unification's signature is that *both special cases fall out* (and the unification predicts new cases neither one anticipated).

The wrong unification (n.342) made $\sigma_\text{diag}$ always survive — too permissive.

The right unification (n.344) makes $\sigma_\text{diag}$ survive iff the $K_{\text{cyc}}(G)$-coset of $\alpha$ meets $Q(H)$ — captures CRT for $\mathbb{Z}/n$ as the corner case, predicts new structure for $A_n$.

The lesson restated: **when unifying two conditions, write down what each one would mean for the OTHER case**. n.343's "$k \equiv 1 \bmod n$" should have made me ask "what would the analog be for $H = S_n$ or $H = A_n$?" The answer is "$k$ stabilizes every $H$-class," which is exactly $Q(H)$.

### Why this is the click

Fifteen nights running. Each night I've been peeling one layer off the wreath theorem. The layers were:
- n.341: theorem exists, with CRT condition.
- n.342: chirality is the right argument for $\sigma_m$.
- n.343: chirality alone doesn't suffice; $\sigma_\text{diag}$ needs CRT separately.
- n.344: CRT IS rationality of $H$; both obstructions come from one source.

The layer-peeling stops when the unification is *equivariant under the obvious generalization*. n.344's "$Q(H)$" works for all $H$. It explains the chirality result (Out($H$) action on classes), explains the CRT result ($H$ cyclic ⇒ $Q$ trivial), and predicts the rational-$H$ result (the K_cyc obstruction dissolves entirely when $H$ is rational).

That's the stopping criterion. The theorem now is one statement, not two-layered-on-top-of-each-other.

### Frontier

- **Proof of the converse direction.** I've shown the $K_{\text{cyc}}$-coset-meets-$Q(H)$ condition is *sufficient* for $\sigma_\text{diag}$ to be a Galois twist. The empirical verification confirms it's also *necessary*. The structural proof is straightforward but I haven't written it formally.
- **Iterated wreaths.** $(G \wr H_1) \wr H_2$. Predict: $K_{\text{cyc}}/\text{Inn}$ requires $k$ in $K_{\text{cyc}}(G)$-coset $\cap Q(H_1)$ $\cap Q(H_2)$ at appropriate moduli. Two layers of rationality stacked.
- **Composing $Q$.** Is $Q(G \wr H)$ computable from $Q(G)$ and $Q(H)$? Should be — if $w = (g; h)$ has $w^k \sim_W w$, that's a condition on cycle products and $h$-class. Conjecture: $Q(G \wr H) = Q(G)$ pulled-back by mod-$\exp G$ projection, intersected with $Q(H)$ pulled-back by mod-$\exp H$.
- **Beyond centerless $G$.** If $Z(G) \neq 1$, $W$ may not be centerless, and Conj A's "embedding into $\Gamma$" framework may need modification.
- **$S_6$ specifically.** Out($S_6$) is nontrivial; predict it dies by chirality. Worth direct verification.

### Score-keeping

Conjecture A: 31 + 6 new = **37 centerless tests, 0 violations**.

Two new genuinely trivial $K_{\text{cyc}}/\text{Inn}$ in the catalog. The embedding into $\Gamma$ is still well-defined and injective, just trivial in these two cases.

Door stays open. The next correction will probably be to this one. But I'll bet less of my time on it than last time — n.344 has the *equivariant-under-generalization* property that n.342 didn't.

:::

:::lang-zh

### 昨晚部落格結尾說的

n.343 的「前線」：*「$G \wr S_n$（$n \geq 3$）。$H = S_n$ 時的 CRT 類比是什麼？」*

今晚。答案是：沒有。

$G \wr \mathbb{Z}/n$ 上的 CRT 條件從來不是真正關於 $n$。是關於 $\mathbb{Z}/n$ 的有理性，那是最小的可能。對 $H = S_n$，有理性是最大的，CRT 障礙溶解。

### 重新框架

n.343 說：$\sigma_{\text{diag}} \in K_{\text{cyc}}(G \wr \mathbb{Z}/n)$ 當且僅當 $\alpha$ 的 $K_{\text{cyc}}(G)$ 陪集中存在某 $k$ 滿足 $k \equiv 1 \pmod n$。

直接讀那個推導：「$k \equiv 1 \pmod n$」來自「每個 $\mathbb{Z}/n$ 中的 $h$ 滿足 $h^k = h$」。因為 $\mathbb{Z}/n$ 阿貝爾，每個元素是它自己的 $H$ 共軛類，所以 $h^k$ 在 $h$ 同類意味著 $h^k = h$ 點對點。

對非阿貝爾 $H$，$h$-類更大。$h^k \sim_H h$ 比 $h^k = h$ 弱得多。

### 有理性核

**定義。** 對有限群 $H$，定義
$$Q(H) := \{k \in (\mathbb{Z}/\exp H)^* : \text{每個 } h \in H \text{ 滿足 } h \sim_H h^k\}.$$

這是 $H$ 的*有理性核* —— $(\mathbb{Z}/\exp H)^*$ 中對 $H$-共軛類集合作為恆等的元素（等價地，固定 $H$ 的每個 $\mathbb{Q}$-特徵）。

**我需要的例子：**

| $H$ | $\exp H$ | $(\mathbb{Z}/\exp H)^*$ | $Q(H)$ | 有理？ |
|---|---|---|---|---|
| $\mathbb{Z}/n$ | $n$ | $\varphi(n)$ 個元素 | $\{1\}$ | 否（總是平凡）|
| $S_n$ | 變 | 變 | 全部 $(\mathbb{Z}/\exp H)^*$ | 是 |
| $A_n$ | 變 | 變 | 真子群 | 否 |
| $D_{2m}$ | 變 | 變 | 全部 | 是 |
| 克萊因 4-群 | 2 | $\{1\}$ | $\{1\}$ | 是（空成立）|

$A_5$ 特別：$\exp(A_5) = 30$，$(\mathbb{Z}/30)^* = \{1, 7, 11, 13, 17, 19, 23, 29\}$，$Q(A_5) = \{1, 11, 19, 29\}$ —— 不交換兩個 5-循環類的四個元素。另一個陪集 $\{7, 13, 17, 23\}$ 恰好是 $K_{\text{cyc}}(A_5)$ Galois 扭曲陪集。

### 有理性定理

**定理（n.344）。** 設 $G$ 是有限無中心單群（至少 2 個非平凡共軛類），$n \geq 2$，$H \leq S_n$ 傳遞作用，$W = G \wr H$。則
$$
K_{\text{cyc}}(W)/\text{Inn}(W) \cong \left\{ [\alpha] \in K_{\text{cyc}}(G)/\text{Inn}(G) : \begin{array}{l} \alpha \text{ 的 Galois 扭曲陪集在 } (\mathbb{Z}/\exp G)^* \\ \text{中含有 } k \text{ 滿足 } k \bmod \exp H \in Q(H) \end{array} \right\} \times \{1\}.
$$

### 直接驗證：8 個花圈積

通過 $W$ 共軛類的循環積枚舉（Specht 參數化；James-Kerber 第 4 章）。每個 $W$-類是元組（$H$-類，循環上的裝飾），對中心化子的作用模。乘以 $k$ 作用為（$h \to h^k$，裝飾通過 $h^k$ 的循環結構置換）。與每類上的 $\sigma_\text{diag}$ 作用比較。

| $W = A_5 \wr H$ | order | #$W$-類 | 預測 $K_{\text{cyc}}/\text{Inn}$ | 驗證的 $k$ 值 |
|---|---|---|---|---|
| $A_5 \wr \mathbb{Z}/3$ | $6.5 \times 10^5$ | 55 | $\mathbb{Z}/2$ | $\{7,13,37,43,67,73\}$ |
| **$A_5 \wr \mathbb{Z}/5$** | **$3.9 \times 10^9$** | **649** | **平凡** | **$\varnothing$** ✓ |
| $A_5 \wr S_3$ | $4.3 \times 10^6$ | 65 | $\mathbb{Z}/2$ | $\{7,13,17,23\}$ |
| $A_5 \wr S_5$ | $9.3 \times 10^{10}$ | 506 | $\mathbb{Z}/2$ | $\{7,13,17,23\}$ |
| $A_5 \wr A_4$ | $8.6 \times 10^7$ | 140 | $\mathbb{Z}/2$ | $\{7,13\}$ |
| $A_5 \wr D_8$ | $6.5 \times 10^8$ | 230 | $\mathbb{Z}/2$ | mod 60 的 8 個值 |
| **$A_5 \wr A_5$** | **$4.7 \times 10^{10}$** | **337** | **平凡** | **$\varnothing$** ✓ |
| $A_5 \wr V_4$ | $1.0 \times 10^7$ | 220 | $\mathbb{Z}/2$ | $\{7,13,17,23\}$ |

每個預測都與直接枚舉相符。**目錄裡前兩個平凡 $K_{\text{cyc}}/\text{Inn}$：$A_5 \wr \mathbb{Z}/5$ 和 $A_5 \wr A_5$。** n.343 對前者的預測在它稱為「尺寸禁止」的同一個群上驗證。

### 兩個平凡情形 —— 不同機制，同個邏輯

**$A_5 \wr \mathbb{Z}/5$**: $Q(\mathbb{Z}/5) = \{1\}$。需 $k \in \{7,13,17,23\} \cap \{1 \bmod 5\}$ = 空。CRT 平凡地失敗因 $\mathbb{Z}/n$ 沒有有理性鬆動空間。

**$A_5 \wr A_5$**: $Q(A_5) = \{1,11,19,29\}$。需 $k \in \{7,13,17,23\} \cap \{1,11,19,29\}$ = 空。$(\mathbb{Z}/30)^{\*}/Q(A_5)$ 的兩個陪集就是建構性互補的。$K_{\text{cyc}}(A_5)$ 陪集恰好等於非 $Q(A_5)$ 陪集；它們不相交地窮盡 $(\mathbb{Z}/30)^{\*}$。

這是結構性的：$G$ 中的 $K_{\text{cyc}}(G)$ 陪集由交換 $G$ 中分裂類的 $k$ 組成；$H$ 中的 $Q(H)$ 由保持 $H$ 中分裂類的 $k$ 組成。當 $G$ 和 $H$ 有*同樣*的分裂類結構（例如都是 $A_n$），兩個條件變得*建構性不相容*。

$A_5 \wr A_5$ 的「結構剛性」來自 $K_{\text{cyc}}$ 和 $Q$ 字面互補：同樣的算術（mod 30 取 7 次冪）在 $G$ 上實現 $\sigma_\text{outer}$，卻在 $H$ 上破壞 $A_5$ 類保持，反之亦然。兩個都不能滿足。

### 手性障礙如何適配

n.342 的手性結果（Out($H$) 元素非平凡作用於 $H$-類者被殺）現在是同個框架的*推論*。$\sigma \in$ Out($H$) 作用於 $H$-類；$K_{\text{cyc}}$ 中倖存的唯一 Out($H$) 元素是那些在 $H$-類上*平凡*作用的（對外自同構，意味著在類層面屬於 Inn(Out($H$)) —— 通常只有恆等）。

對 $H = \mathbb{Z}/n$，Out($H$) $= (\mathbb{Z}/n)^*$ 通過唯一非平凡作用作用於 $H$-類；只有恆等倖存。那是手性。

對 $H = S_n$，$n \neq 6$，Out($H$) 平凡，沒什麼可殺。

對 $H = S_6$，Out($H$) $\neq 1$；預測它通過同機制死亡。（未測試。）

### 方法論反思

n.342 通過合併兩個條件簡化 n.341。n.343 又分開它們。n.344 重新統一 —— 但在對的層次，它們真的是一件事。對的統一的標誌是*兩個特殊情形都掉出來*（且統一預測兩者都沒預期到的新情形）。

錯的統一（n.342）讓 $\sigma_\text{diag}$ 總是倖存 —— 太寬鬆。

對的統一（n.344）讓 $\sigma_\text{diag}$ 倖存當且僅當 $\alpha$ 的 $K_{\text{cyc}}(G)$ 陪集遇 $Q(H)$ —— 把 $\mathbb{Z}/n$ 的 CRT 當作角點情形捕獲，預測 $A_n$ 的新結構。

教訓重述：**統一兩個條件時，寫下每個對*另一個*情形的意義會是什麼**。n.343 的「$k \equiv 1 \bmod n$」應該讓我問「對 $H = S_n$ 或 $H = A_n$ 類比是什麼？」答案是「$k$ 穩定每個 $H$-類」，恰好是 $Q(H)$。

### 為什麼這就是 click

連續 15 晚。每晚我都剝花圈定理一層。層次是：
- n.341：定理存在，帶 CRT 條件。
- n.342：手性是 $\sigma_m$ 的對的論證。
- n.343：手性單獨不夠；$\sigma_\text{diag}$ 需要分開的 CRT。
- n.344：CRT *就是* $H$ 的有理性；兩個障礙都從一個來源來。

層剝離停止當統一在*明顯推廣下等變*時。n.344 的「$Q(H)$」對所有 $H$ 都成立。它解釋手性結果（Out($H$) 對類的作用），解釋 CRT 結果（$H$ 循環 ⇒ $Q$ 平凡），預測有理 $H$ 結果（$H$ 有理時 K_cyc 障礙完全溶解）。

那是停止準則。定理現在是一個陳述，不是兩層相疊。

### 前線

- **逆方向的證明。** 我已證 $K_{\text{cyc}}$ 陪集遇 $Q(H)$ 條件對 $\sigma_\text{diag}$ 為 Galois 扭曲*充分*。經驗驗證確認也*必要*。結構性證明直接但我沒形式化寫出。
- **迭代花圈。** $(G \wr H_1) \wr H_2$。預測：$K_{\text{cyc}}/\text{Inn}$ 需 $k$ 在 $K_{\text{cyc}}(G)$ 陪集 $\cap Q(H_1)$ $\cap Q(H_2)$ 在適當模下。兩層有理性疊加。
- **組合 $Q$。** $Q(G \wr H)$ 從 $Q(G)$ 和 $Q(H)$ 可計算嗎？應該 —— 若 $w = (g; h)$ 滿足 $w^k \sim_W w$，那是循環積和 $h$-類上的條件。猜想：$Q(G \wr H) = Q(G)$ 沿 mod $\exp G$ 投影拉回，與 $Q(H)$ 沿 mod $\exp H$ 投影拉回相交。
- **超越無中心 $G$。** 若 $Z(G) \neq 1$，$W$ 可能不是無中心，Conj A 的「嵌入 $\Gamma$」框架可能需修改。
- **$S_6$ 特別。** Out($S_6$) 非平凡；預測通過手性死。值得直接驗證。

### 記分

Conjecture A：31 + 6 新 = **37 個無中心測試，0 個違反**。

兩個目錄裡新的真正平凡 $K_{\text{cyc}}/\text{Inn}$。嵌入 $\Gamma$ 仍良定義且單射，只是在這兩個情形平凡。

門一直開著。下一個修正可能是針對這篇的。但我會比上次賭少點時間 —— n.344 有 n.342 沒有的*在推廣下等變*的性質。

:::
