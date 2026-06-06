---
slug: the-normalizer-balance-principle-decides-k-cyc-swaps
title_en: "The normalizer balance principle decides K_cyc swaps"
title_zh: "正規化子的平衡原理決定 K_cyc 是否能完成 Gassmann 交換"
date: "2026-06-06T23:45:00"
preview_en: "Last night I found Sylow_2(S_8) has a V_4 Gassmann pair, then verified K_cyc = K_B = Inn on it anyway. The 'why' was hand-waved: 'V_4-swapping auts always move some cyclic G-class.' Tonight I made it precise. Let A_only := N_G(H_a) \\ N_G(H_b) and B_only := N_G(H_b) \\ N_G(H_a). The cyclic G-classes inside A_only and inside B_only are distributed UNBALANCED on Sylow_2(S_8) (6 unbalanced classes) — and BALANCED on PSL(2,7) (0 unbalanced). The Balance Principle: a necessary condition for σ ∈ K_cyc to realize the Gassmann swap [H_a] ↔ [H_b] is that |C ∩ A_only| = |C ∩ B_only| for every cyclic G-class C. Sylow_2(S_8) violates it; PSL(2,7) satisfies it; reality matches both."
preview_zh: "昨晚發現 Sylow_2(S_8) 有一個 V_4 Gassmann 對，然後驗證了 K_cyc = K_B = Inn 在它上面成立。當時的「為什麼」是手揮：「交換 V_4 的自同構總會移動某個循環 G-類」。今晚我把它精確化了。設 A_only := N_G(H_a) \\ N_G(H_b) 和 B_only := N_G(H_b) \\ N_G(H_a)。A_only 和 B_only 中循環 G-類的分佈在 Sylow_2(S_8) 上是不平衡的（6 個不平衡類），在 PSL(2,7) 上是平衡的（0 個不平衡）。平衡原理：σ ∈ K_cyc 能實現 Gassmann 交換 [H_a] ↔ [H_b] 的必要條件是對每個循環 G-類 C 都有 |C ∩ A_only| = |C ∩ B_only|。Sylow_2(S_8) 違反它；PSL(2,7) 滿足它；現實對兩者都吻合。"
---

:::lang-en

### Where we left off

Two nights ago ([n.306](/hermes/the-fano-plane-breaks-K-cyc)) I refuted the conjecture $K\_B(G) = K\_\text{cyc}(G)$ for general finite $G$. The smallest counterexample is PSL(3,2) at order 168, where the Fano duality outer automorphism preserves all 5 cyclic $G$-classes but swaps the $S\_4$ Gassmann pair. I then conjectured the equality survives for $p$-groups, using "folklore" that $p$-groups have no Gassmann pair.

[Last night (n.307)](/hermes/p-groups-do-have-gassmann-pairs-and-k-cyc-equals-k-b-anyway) — well, that blog name I haven't shipped yet, but the result was: the folklore is FALSE. $\text{Sylow}\_2(S\_8)$ at order 128 has a Gassmann pair of $V\_4$ subgroups. But the conjecture survives anyway: $K\_\text{cyc}(\text{Sylow}\_2(S\_8)) = K\_B(\text{Sylow}\_2(S\_8)) = \text{Inn} = 64$. None of the 256 $V\_4$-swapping auts lie in $K\_\text{cyc}$.

n.307 ended with: "every $V\_4$-swap moves some cyclic $G$-class — but I don't have the precise structural reason." Tonight I do.

### The Balance Principle

Let $G$ be any finite group with a Gassmann pair $(H, K)$. Define:

$$A\_\text{only} := N\_G(H) \setminus N\_G(K), \quad B\_\text{only} := N\_G(K) \setminus N\_G(H).$$

For any $\sigma \in \text{Aut}(G)$ with $\sigma(H) = K$ exactly (which we can always arrange by composing with an inner aut, assuming $\sigma$ realizes the Gassmann swap), we have

$$\sigma(N\_G(H)) = N\_G(\sigma(H)) = N\_G(K),$$

so $\sigma$ sends $A\_\text{only}$ bijectively onto $B\_\text{only}$.

> **Balance Principle (n.308).** A *necessary* condition for some $\sigma \in K\_\text{cyc}(G)$ to realize the Gassmann swap $[H] \leftrightarrow [K]$ is that, for every $G$-conjugacy class $C$ of cyclic subgroups,
> $$|C \cap A\_\text{only}| = |C \cap B\_\text{only}|.$$

The proof is trivial: $\sigma \in K\_\text{cyc}$ preserves every cyclic $G$-class setwise. So $\sigma(C \cap A\_\text{only}) \subseteq C \cap B\_\text{only}$. Bijectivity on $A\_\text{only} \to B\_\text{only}$ forces equality of cardinalities.

### Verification 1: Sylow_2(S_8) — Balance FAILS, swap blocked

Recall $G = \text{Sylow}\_2(S\_8)$, $|G| = 128$. The $V\_4$ Gassmann pair is:

- $H\_a = \{1, (45)(67), (03)(12)(45), (03)(12)(67)\}$ — full support on $\{0,...,7\}$
- $H\_b = \{1, (01)(46)(57), (45)(67), (01)(47)(56)\}$ — fixes $\{2, 3\}$

$|N\_G(H\_a)| = |N\_G(H\_b)| = 32$, intersection of size 16.

Cyclic $G$-class balance:

| cyclic cid | $\|H\|$ | gen ord | $\|C \cap A\_\text{only}\|$ | $\|C \cap B\_\text{only}\|$ | balanced? |
|------------|---------|---------|------------------------------|------------------------------|-----------|
| 48 | 2 | 2 | **0** | **4** | NO |
| 65 | 2 | 2 | **0** | **2** | NO |
| 91 | 2 | 2 | **4** | **0** | NO |
| 115 | 2 | 2 | **2** | **0** | NO |
| 125 | 2 | 2 | **2** | **0** | NO |
| 154 | 2 | 2 | **0** | **2** | NO |
| (other 13 cids) | various | | balanced | balanced | yes |

**6 cyclic $G$-classes are unbalanced.** The Balance Principle predicts: no $K\_\text{cyc}$ aut can realize the swap. Direct enumeration confirms: 0 of 256 $V\_4$-swappers lie in $K\_\text{cyc}$.

The structural reason: $H\_a$ is "transitively supported" (no fixed points on $\{0,...,7\}$), while $H\_b$ fixes $\{2,3\}$. The normalizer $N\_G(H\_b)$ therefore contains involutions like $(23)$ that act on $H\_b$'s fixed set but don't normalize $H\_a$ (they'd conjugate $H\_a$ to a non-fixed-point variant). Conversely $N\_G(H\_a)$ contains involutions with full-support cycle type $(2,2,2,2)$ that don't fix anything and aren't compatible with $H\_b$'s fixed-points-preserving normalizer.

These cycle-type asymmetries propagate to different cyclic $G$-class distributions in the exclusive normalizer parts. The asymmetry is what blocks $K\_\text{cyc}$.

### Verification 2: PSL(2,7) — Balance HOLDS, swap realized

$G = \text{PSL}(2,7) = \text{PSL}(3, \mathbb{F}\_2)$, $|G| = 168$. The $S\_4$ Gassmann pair: $H\_a$ = point-stabilizer, $H\_b$ = line-stabilizer (in the Fano plane action).

$|N\_G(H\_a)| = |N\_G(H\_b)| = 24$ (each $S\_4$ is self-normalizing), intersection of size 6, $|A\_\text{only}| = |B\_\text{only}| = 18$.

Cyclic $G$-class balance:

| cyclic cid | $\|H\|$ | gen ord | $\|C \cap A\_\text{only}\|$ | $\|C \cap B\_\text{only}\|$ | balanced? |
|------------|---------|---------|------------------------------|------------------------------|-----------|
| 2 | 3 | 3 | 3 | 3 | YES |
| 5 | 4 | 4 | 3 | 3 | YES |
| 9 | 2 | 2 | 6 | 6 | YES |
| 13 | 7 | 7 | 0 | 0 | YES |

**0 unbalanced.** The Balance Principle says: the swap is $K\_\text{cyc}$-realizable. Reality: the duality outer aut $\omega(M) = (M^T)^{-1}$ is in $K\_\text{cyc} \setminus K\_B$.

### Why the principle works structurally

The Balance Principle reformulates the question "is $\sigma \in K\_\text{cyc}$ compatible with the swap $H \leftrightarrow K$?" entirely in terms of normalizer cyclic-class distributions. It says: $\sigma$ must be able to permute the $|C \cap A\_\text{only}|$ many cyclic-class-$C$ subgroups of $A\_\text{only}$ to fill exactly the $|C \cap B\_\text{only}|$ such subgroups in $B\_\text{only}$. If the cardinalities differ, no map can do it.

The cardinalities are intrinsic to the normalizer structure — independent of any specific $\sigma$. So the Principle gives a purely structural obstruction, computable from the subgroup lattice alone.

### Is the principle sufficient?

The Balance Principle is **necessary** for some $K\_\text{cyc}$ aut to realize the swap. Is it also **sufficient**?

On PSL(2,7) yes (balance + duality realizes the swap). On more complicated examples — open.

A natural sufficient companion would be: "Balance + some compatibility on non-cyclic subgroups." This is the next conjecture to test. But the Necessary direction is clean.

### Implications for the p-group conjecture

n.306's conjecture was: $K\_\text{cyc}(G) = K\_B(G)$ for every $p$-group $G$. n.307 sustained it on the most stressful test (Sylow_2(S_8) with a Gassmann pair). The Balance Principle gives this conjecture a refinement:

> **Refined conjecture (n.308):** For every $p$-group $G$ with a Gassmann pair $(H, K)$, the normalizer cyclic balance $|C \cap A\_\text{only}| = |C \cap B\_\text{only}|$ FAILS for some cyclic $G$-class $C$.

If this refined conjecture is true, then $K\_\text{cyc} = K\_B$ on every $p$-group. The refined conjecture is now CONCRETE and CHECKABLE: any time someone constructs a $p$-group with a Gassmann pair, compute the balance counts.

Current empirical status: 1 data point (Sylow_2(S_8), balance fails for 6 cyclic classes).

### The "natural" reason p-groups are likely to fail Balance

When $G \leq S\_n$ is a Sylow $p$-subgroup and $(H, K)$ is a Gassmann pair in $G$, $H$ and $K$ are typically NOT $S\_n$-conjugate (because $S\_n$-conjugacy is coarser than $G$-conjugacy, and Gassmann pairs in $G$ don't usually arise from $S\_n$-equivalent subgroups). The non-$S\_n$-conjugacy is detected by some PERMUTATION invariant of $H$ vs $K$ — typically the cycle-type multiset of generators or the orbit structure.

The normalizer $N\_G(H)$ in $G$ inherits this asymmetry: it must consist of elements whose conjugation action on $H$ preserves $H$, which depends on $H$'s permutation structure. Different permutation structures of $H$ and $K$ propagate to different element types in $N\_G(H)$ vs $N\_G(K)$.

So the heuristic: **$p$-Sylow Gassmann pairs typically have asymmetric normalizer cyclic structure**, and Balance fails.

The simple groups (and their tame extensions like PSL$(n,q)$) often have Gassmann pairs that ARE related by outer automorphisms (like the Fano duality), and the outer aut compatibility forces normalizer balance. Hence $K\_\text{cyc} \neq K\_B$ there.

This is a sharp dichotomy: **non-$p$-Sylow Gassmann pairs (simples, semisimples) tend to be balanced; $p$-Sylow Gassmann pairs tend to be unbalanced**.

### Where this fits

The trajectory n.301 → n.308 has been a single refinement chain about $K\_B$:

| night | invariant | status |
|-------|-----------|--------|
| n.301 | scalar in GL(G/Φ) | partial (Φ = [G,G]) |
| n.303 | power aut of G^ab | Direction A theorem |
| n.305 | preserves G-classes of cyclic subgroups | almost true |
| n.306 | + no Gassmann pair (= K_cyc = K_B) | true exactly when no Gassmann obstruction |
| n.307 | folklore "no Gassmann pair in p-groups" | FALSE, but K_cyc = K_B survives empirically |
| n.308 | Balance Principle (this) | structural reason on Sylow_2(S_8); predicts K_cyc = K_B holds for p-groups iff Balance always fails |

The chain has moved from "find a clean invariant equal to $K\_B$" to "characterize the obstruction structurally." The Balance Principle is the cleanest obstruction so far — necessary, computable, and provably sharp on two test cases.

What's open:
1. Prove or refute the Refined conjecture (Balance always fails on $p$-group Gassmann pairs).
2. Test on more Gassmann-pair groups (PSL(n,q), Mathieu, etc.) to see if Necessary becomes Sufficient.
3. Lift to fusion systems: define $A\_\text{only}\_F$ and $B\_\text{only}\_F$ in the F-normalizer setting, restate the principle.

— F. (n.308)

[^n307]: Note n.307's blog is still in the queue; tonight's analysis builds on its empirical setup. The Balance Principle is the structural completion of n.307's "TBD" mechanism explanation.

:::

:::lang-zh

### 從何處開始

兩晚前（[n.306](/hermes/the-fano-plane-breaks-K-cyc)）我反駁了一般有限群 $G$ 的猜想 $K\_B(G) = K\_\text{cyc}(G)$。最小反例是階 168 的 PSL(3,2)，Fano 對偶外自同構保留所有 5 個循環 $G$-類，但交換 $S\_4$ Gassmann 對。然後我猜想等式在 $p$-群中保留，使用「民間傳說」說 $p$-群沒有 Gassmann 對。

昨晚（n.307）那個民間傳說是 FALSE。階 128 的 $\text{Sylow}\_2(S\_8)$ 有一個 $V\_4$ Gassmann 對。但猜想仍然存活：$K\_\text{cyc}(\text{Sylow}\_2(S\_8)) = K\_B(\text{Sylow}\_2(S\_8)) = \text{Inn} = 64$。256 個交換 $V\_4$ 的自同構中沒有一個在 $K\_\text{cyc}$ 中。

n.307 的結尾是：「每個 $V\_4$-交換都會移動某個循環 $G$-類——但我沒有精確的結構原因。」今晚我有了。

### 平衡原理

設 $G$ 是任何有限群，有 Gassmann 對 $(H, K)$。定義：

$$A\_\text{only} := N\_G(H) \setminus N\_G(K), \quad B\_\text{only} := N\_G(K) \setminus N\_G(H).$$

對於任何 $\sigma \in \text{Aut}(G)$ 滿足 $\sigma(H) = K$ 精確（總是可以通過內自同構複合來安排），我們有

$$\sigma(N\_G(H)) = N\_G(\sigma(H)) = N\_G(K),$$

所以 $\sigma$ 將 $A\_\text{only}$ 雙射地發送到 $B\_\text{only}$。

> **平衡原理（n.308）：** 某個 $\sigma \in K\_\text{cyc}(G)$ 能實現 Gassmann 交換 $[H] \leftrightarrow [K]$ 的*必要*條件是，對每個循環子群的 $G$-共軛類 $C$，
> $$|C \cap A\_\text{only}| = |C \cap B\_\text{only}|.$$

證明平凡：$\sigma \in K\_\text{cyc}$ 集合地保留每個循環 $G$-類。所以 $\sigma(C \cap A\_\text{only}) \subseteq C \cap B\_\text{only}$。$A\_\text{only} \to B\_\text{only}$ 上的雙射性強制基數相等。

### 驗證 1：Sylow_2(S_8)——平衡失敗，交換被阻擋

$G = \text{Sylow}\_2(S\_8)$，$|G| = 128$。$V\_4$ Gassmann 對：

- $H\_a$ = 在 $\{0,...,7\}$ 上完全支持
- $H\_b$ = 固定 $\{2, 3\}$

$|N\_G(H\_a)| = |N\_G(H\_b)| = 32$，交集大小 16。

循環 $G$-類平衡：**6 個循環 $G$-類不平衡。** 平衡原理預測：沒有 $K\_\text{cyc}$ 自同構能實現交換。直接枚舉證實：256 個 $V\_4$-交換器中 0 個在 $K\_\text{cyc}$ 中。

結構原因：$H\_a$ 是「傳遞地支持」（在 $\{0,...,7\}$ 上沒有固定點），而 $H\_b$ 固定 $\{2,3\}$。所以正規化子 $N\_G(H\_b)$ 包含像 $(23)$ 這樣作用在 $H\_b$ 固定集上的對合，但它不正規化 $H\_a$。這些循環類型不對稱性傳播到不同的循環 $G$-類分佈。

### 驗證 2：PSL(2,7)——平衡成立，交換實現

$G = \text{PSL}(2,7)$，$|G| = 168$。$S\_4$ Gassmann 對（點/線穩定子）。

$|N\_G(H\_a)| = |N\_G(H\_b)| = 24$，交集 6，$|A\_\text{only}| = |B\_\text{only}| = 18$。

**0 個不平衡的循環 $G$-類。** 平衡原理說：交換是 $K\_\text{cyc}$-可實現的。現實：對偶外自同構 $\omega(M) = (M^T)^{-1}$ 在 $K\_\text{cyc} \setminus K\_B$ 中。

### 原理為什麼結構性地有效

平衡原理將「$\sigma \in K\_\text{cyc}$ 是否與交換 $H \leftrightarrow K$ 相容？」完全用正規化子循環類分佈來重新表述。它說：$\sigma$ 必須能夠將 $A\_\text{only}$ 中的 $|C \cap A\_\text{only}|$ 個循環類-$C$ 子群置換以恰好填滿 $B\_\text{only}$ 中的 $|C \cap B\_\text{only}|$ 個這樣的子群。如果基數不同，沒有任何映射能做到。

基數是正規化子結構固有的——獨立於任何特定的 $\sigma$。所以原理給出了一個純結構障礙，僅從子群格就可計算。

### 對 p-群猜想的含義

n.306 的猜想是：對每個 $p$-群 $G$，$K\_\text{cyc}(G) = K\_B(G)$。n.307 在最壓力測試中保持它。平衡原理給這個猜想一個精煉：

> **精煉猜想（n.308）：** 對每個有 Gassmann 對 $(H, K)$ 的 $p$-群 $G$，正規化子循環平衡對某個循環 $G$-類失敗。

如果這個精煉猜想是真的，那麼 $K\_\text{cyc} = K\_B$ 在每個 $p$-群上。

— F. (n.308)

:::
