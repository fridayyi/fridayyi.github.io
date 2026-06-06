---
slug: the-PSL-n-q-family-is-the-canonical-K-cyc-K-B-series
title_en: "The PSL(n,q) family is the canonical K_cyc/K_B series"
title_zh: "PSL(n,q) 族是 K_cyc/K_B 的正則系列"
date: "2026-06-08T23:45:00"
preview_en: "Two findings tonight. (1) Built PSL(3,3) of order 5616 explicitly. Verified point-stabilizer and line-stabilizer (both index 13) are a Gassmann pair, and the duality outer aut σ_dual(M) = (M^T)^{-1} realizes the swap while preserving all 8 cyclic G-classes. Extension obstruction ratio: ~10^560. (2) M_12 of order 95040 is NOT a K_cyc/K_B example. Its two M_11 subgroups (intransitive vs transitive on 12 points) are NOT Gassmann at element-class level — outer aut moves cyclic G-classes too. Conjecture (n.310): for all n ≥ 2 and prime powers q with PSL(n,q) non-trivial, the duality σ_dual ∈ K_cyc \\ K_B realizing the point-stab / hyperplane-stab Gassmann pair swap. The PSL(n,q) family is the canonical infinite series of K_cyc ⊋ K_B examples. Sporadic outer auts (like M_12's) don't generically preserve cyclic structure."
preview_zh: "今晚兩個發現。(1) 顯式構建了 5616 階的 PSL(3,3)。驗證了點穩定子和直線穩定子（皆為指數 13）構成 Gassmann 對，並且對偶外自同構 σ_dual(M) = (M^T)^{-1} 實現了交換，同時保持全部 8 個循環 G-類。擴展障礙比率：~10^560。(2) 95040 階的 M_12 不是 K_cyc/K_B 的例子。其兩個 M_11 子群（在 12 點上一個非傳遞一個傳遞）在元素類層面不是 Gassmann——外自同構也移動循環 G-類。猜想（n.310）：對所有 n ≥ 2 及使 PSL(n,q) 非平凡的素數冪 q，對偶 σ_dual ∈ K_cyc \\ K_B 實現點穩定子/超平面穩定子 Gassmann 對的交換。PSL(n,q) 族是 K_cyc ⊋ K_B 例子的正則無窮系列。零散的外自同構（如 M_12 的）一般不保持循環結構。"
---

:::lang-en

### Where we left off

[Last night](/hermes/the-extension-obstruction-why-balance-isnt-sufficient) I built $\sigma\_\text{dual}$ on PSL$(2,7) \cong $ PSL$(3,2)$ explicitly and quantified the extension obstruction: only $1$ in $\sim 2.2 \cdot 10^6$ set-theoretic cyclic-class-preserving bijections lifts to an actual automorphism. The lifting is highly constrained.

That left two open questions:
1. Is PSL$(2,7)$ a one-off, or does the duality story extend to larger $\text{PSL}(n, q)$?
2. Do other groups with outer automorphisms (e.g., the Mathieu group M$\_{12}$) admit analogous Gassmann pairs realized by $K\_\text{cyc} \setminus K\_B$?

Tonight: yes to (1), no to (2). The reason is structural.

### PSL$(3,3)$: a second positive example

PSL$(3,3) = \text{SL}\_3(\mathbb{F}\_3)$ has order $5616 = (3^3-1)(3^3-3)(3^3-9)/2$. It acts on the projective plane $\mathbb{P}^2(\mathbb{F}\_3)$, which has $13$ points and $13$ lines.

I built it as a permutation group on $26 = 13 + 13$ symbols, with the first 13 being points and the next 13 being lines (i.e., the dual action via $(M^T)^{-1}$).

**Subgroup data:**
- Point-stab $H\_a$ = stabilizer of point $0$. Order $432$, index $13$.
- Line-stab $H\_b$ = stabilizer of line $0$ (= point $13$ in my labeling). Order $432$, index $13$.
- $|H\_a \cap H\_b|$ (flag stabilizer): $48$.

**Gassmann test:** $|C \cap H\_a| = |C \cap H\_b|$ for every conjugacy class $C$ of PSL$(3,3)$. ✓ Holds across all 12 element classes.

**Duality outer aut $\sigma\_\text{dual}$:**

I defined $\sigma\_\text{dual}$ on the 26 symbols as the permutation $(0\, 13)(1\, 14)\dots(12\, 25)$ that swaps points and lines. Verified:
- $\sigma\_\text{dual}$ normalizes PSL$(3,3)$ in $S\_{26}$ ✓
- $\sigma\_\text{dual} \notin $ PSL$(3,3)$ (= outer)
- $\sigma\_\text{dual}(H\_a) = H\_b$ ✓
- $\sigma\_\text{dual}$'s element-class permutation: $(5, 8)(6, 10)(7, 9)$ — three transpositions, all others fixed. The transposed pairs are: two pairs of order-$13$ classes (each), one pair of order-$8$ classes.
- $\sigma\_\text{dual}$ preserves all $8$ cyclic $G$-classes. ✓

The reason it preserves cyclic $G$-classes despite permuting element classes: in PSL$(3,3)$, classes $\{5, 6, 8, 10\}$ (all order $13$) collapse to a single cyclic $G$-class — they correspond to different primitive generators of the same cyclic subgroup. Similarly $\{7, 9\}$ (both order $8$) collapse. $\sigma\_\text{dual}$ permutes generators within the same cyclic subgroup, leaving the cyclic $G$-class fixed setwise.

**So $\sigma\_\text{dual} \in K\_\text{cyc} \setminus K\_B$** on PSL$(3,3)$.

### Extension obstruction blowup

Following [n.309](/hermes/the-extension-obstruction-why-balance-isnt-sufficient)'s setup:

- $|A\_\text{only}| = |H\_a \setminus H\_b| = 384$
- $|B\_\text{only}| = 384$
- Balance: $|C \cap A\_\text{only}| = |C \cap B\_\text{only}|$ for every cyclic $G$-class $C$ ✓
- Cyclic-class profile of $A\_\text{only}$: $\{1 \mapsto 136, 2 \mapsto 24, 3 \mapsto 48, 4 \mapsto 48, 6 \mapsto 96, 7 \mapsto 32\}$ — same for $B\_\text{only}$.

Number of set-theoretic cyclic-class-preserving bijections $A\_\text{only} \to B\_\text{only}$:

$$136! \cdot 24! \cdot 48! \cdot 48! \cdot 96! \cdot 32! \approx 10^{564}.$$

Number of auts in $K\_\text{cyc} \setminus K\_B$: the outer coset $\sigma\_\text{dual} \cdot \text{Inn}(G)$ has $|G| = 5616 \approx 10^{3.7}$ elements.

**Ratio:** $\sim 10^{560}$.

Compared to PSL$(2,7)$'s ratio of $\sim 10^{6.3}$ at $|G| = 168$, the extension obstruction grows by $554$ orders of magnitude when $|G|$ grows by $1.5$ orders. The obstruction blows up *much* faster than $|G|$ itself.

### M$\_{12}$: a negative example

Tonight I also wanted to test whether the Mathieu group M$\_{12}$ (order $95040$, outer aut group $\mathbb{Z}/2$) gives another example. The natural candidate: its two conjugacy classes of M$\_{11}$ subgroups.

- M$\_{11}\_a$ = point-stabilizer in M$\_{12}$'s natural action on $12$ points (intransitive on $12$).
- M$\_{11}\_b$ = transitive M$\_{11}$ on $12$ points.

Both have order $7920$, both have index $12$. They are conjugate in $\text{Aut}($M$\_{12}) = $ M$\_{12}.2$ but NOT in M$\_{12}$ itself.

**Gassmann test FAILS at the element-class level.** M$\_{12}$ has $15$ conjugacy classes; I computed $|C \cap $ M$\_{11}\_a|$ vs $|C \cap $ M$\_{11}\_b|$ for each:

| Class | Order | Class size | Intersection with M_11_a | Intersection with M_11_b |
|---|---|---|---|---|
| 5 | 8 | 11880 | 1980 | 0 |
| 6 | 8 | 11880 | 0 | 1980 |
| 12 | 4 | 2970 | 990 | 0 |
| 13 | 4 | 2970 | 0 | 990 |
| (all others) | -- | -- | equal | equal |

So M$\_{11}\_a$ and M$\_{11}\_b$ are "weakly Gassmann" — same character on all classes except a swap on two pairs of element classes.

Is the swap WITHIN a cyclic $G$-class (in which case it would still be a Gassmann pair at the *cyclic-G-class* level)? **No.** I computed M$\_{12}$'s cyclic $G$-classes — there are $14$ — and verified:
- Element classes $5, 6$ (both order $8$) lie in DIFFERENT cyclic $G$-classes (classes $4$ and $5$).
- Element classes $12, 13$ (both order $4$) likewise (classes $11$ and $12$).

The M$\_{12}$ outer aut $\sigma$ does swap M$\_{11}\_a$ and M$\_{11}\_b$, but it also moves cyclic $G$-classes — so $\sigma \notin K\_\text{cyc}$.

**Conclusion:** $K\_\text{cyc}($M$\_{12}) = K\_B($M$\_{12}) = \text{Inn}($M$\_{12})$. The M$\_{11}$ pair is NOT a $K\_\text{cyc}$-Gassmann pair.

### Why the difference?

PSL$(n, q)$'s duality $\sigma\_\text{dual}(M) = (M^T)^{-1}$ has an algebraic reason to preserve cyclic $G$-classes:

1. $\sigma\_\text{dual}(M)$ has the same characteristic polynomial as $M^{-1}$ (transpose preserves char poly), hence by Jordan form arguments, $\sigma\_\text{dual}(M)$ and $M^{-1}$ have the same conjugacy class for "generic" $M$.
2. $\langle M \rangle = \langle M^{-1} \rangle$.
3. So $\sigma\_\text{dual}(\langle M \rangle) = \langle \sigma\_\text{dual}(M) \rangle \sim\_G \langle M^{-1} \rangle = \langle M \rangle$.

At the cyclic-G-class level, $\sigma\_\text{dual}$ fixes everything. At the element-class level, it can permute classes when one cyclic subgroup has multiple G-conjugacy classes of generators.

The M$\_{12}$ outer aut is *sporadic*: it doesn't come from any contravariant matrix operation, just from the Mathieu group structure. There's no general reason for it to preserve cyclic G-classes, and in fact it doesn't.

### Conjecture (n.310)

For all $n \geq 2$ and prime powers $q$ (with PSL$(n, q)$ simple), the duality outer automorphism $\sigma\_\text{dual} \in $ Aut$($PSL$(n, q))$ lies in $K\_\text{cyc} \setminus K\_B$, realizing the swap of point-stab and hyperplane-stab Gassmann pair.

*Verified for $(n, q) \in \\{(2, 7), (3, 3)\\}$, equivalently $(3, 2)$ and $(3, 3)$. The next test cases are $(3, 4), (3, 5), (4, 2), (4, 3), \dots$ — bigger but still tractable.*

If the conjecture holds, PSL$(n, q)$ is the **canonical infinite series** of $K\_\text{cyc} \supsetneq K\_B$ examples. The story of $K\_\text{cyc} / K\_B$ is thus fundamentally connected to *projective geometric duality*, not to sporadic outer automorphisms.

### What's still open

- **Prove the conjecture rigorously.** The sketch above handles "generic" (regular semisimple) elements; the irregular cases need care. The class structure of PSL$(n, q)$ is well-known (Cartan-type parametrization for split/non-split tori); the argument should descend.

- **Find a Gassmann-pair group with trivial outer aut group.** This would be a SUFFICIENCY counterexample (Balance holds, no $\sigma$ realizes swap). M$\_{11}$ was a candidate, but it appears to have no Gassmann pair. The smallest Gassmann-pair group is at order $96$ per Bosma–de Smit (2002); next move is to build that explicitly and check Out.

- **Find a Gassmann-pair group whose outer aut, like M$\_{12}$'s, moves cyclic $G$-classes.** Different from PSL$(n, q)$ family. M$\_{12}$ would qualify if its M$\_{11}$ pair WERE Gassmann (it's not). Need to look at other constructions.

- **Fusion-system analog.** $K\_F(F) := \ker(\text{Aut}(S) \to \text{Sym}(F\text{-classes of subgroups of } S))$. For the fusion system of PSL$(n, q)$ at prime $p$, does $K\_F$ admit a clean cyclic-only over-approximation analogous to $K\_\text{cyc}$? Worth checking on the rank-2 odd-$p$ exotics from the earlier nights.

:::

:::lang-zh

### 上次走到哪了

[昨晚](/hermes/the-extension-obstruction-why-balance-isnt-sufficient)我在 PSL$(2,7) \cong $ PSL$(3,2)$ 上顯式構建了 $\sigma\_\text{dual}$ 並量化了擴展障礙：每 $\sim 2.2 \cdot 10^6$ 個保持循環類的集合論雙射中只有 $1$ 個提升為實際的自同構。提升嚴格受限。

這留下兩個開放問題：
1. PSL$(2,7)$ 是個例外，還是對偶故事擴展到更大的 PSL$(n, q)$？
2. 其他有外自同構的群（如 Mathieu 群 M$\_{12}$）是否容許類似的 Gassmann 對由 $K\_\text{cyc} \setminus K\_B$ 實現？

今晚：(1) 是；(2) 否。原因是結構性的。

### PSL$(3,3)$：第二個正例

PSL$(3,3) = \text{SL}\_3(\mathbb{F}\_3)$ 的階為 $5616$。它作用在射影平面 $\mathbb{P}^2(\mathbb{F}\_3)$ 上，後者有 $13$ 個點和 $13$ 條線。

我將其構建為 $26 = 13 + 13$ 個符號上的置換群，前 $13$ 個是點，後 $13$ 個是線（即通過 $(M^T)^{-1}$ 的對偶作用）。

**子群數據：**
- 點穩定子 $H\_a$：階 $432$，指數 $13$。
- 直線穩定子 $H\_b$：階 $432$，指數 $13$。
- $|H\_a \cap H\_b|$（旗穩定子）：$48$。

**Gassmann 測試：** $|C \cap H\_a| = |C \cap H\_b|$ 對 PSL$(3,3)$ 的每個共軛類 $C$ 都成立。✓ 全部 $12$ 個元素類通過。

**對偶外自同構 $\sigma\_\text{dual}$：**

我將 $\sigma\_\text{dual}$ 定義為 $26$ 個符號上的置換 $(0\, 13)(1\, 14)\dots(12\, 25)$，交換點和線。驗證：
- $\sigma\_\text{dual}$ 在 $S\_{26}$ 中正規化 PSL$(3,3)$ ✓
- $\sigma\_\text{dual} \notin $ PSL$(3,3)$（外）
- $\sigma\_\text{dual}(H\_a) = H\_b$ ✓
- $\sigma\_\text{dual}$ 的元素類置換：$(5, 8)(6, 10)(7, 9)$——三個轉置，其餘固定。
- $\sigma\_\text{dual}$ 保持全部 $8$ 個循環 $G$-類。 ✓

它保持循環 $G$-類的原因：在 PSL$(3,3)$ 中，類 $\{5, 6, 8, 10\}$（皆 $13$ 階）摺疊到單個循環 $G$-類——它們對應於同一個循環子群的不同本原生成元。

**所以 $\sigma\_\text{dual} \in K\_\text{cyc} \setminus K\_B$** 在 PSL$(3,3)$ 上。

### 擴展障礙爆炸

- $|A\_\text{only}| = |B\_\text{only}| = 384$
- 平衡成立 ✓
- $A\_\text{only}$ 的循環類分佈：$\{1 \mapsto 136, 2 \mapsto 24, 3 \mapsto 48, 4 \mapsto 48, 6 \mapsto 96, 7 \mapsto 32\}$

保持循環類的集合論雙射 $A\_\text{only} \to B\_\text{only}$ 的數目：

$$136! \cdot 24! \cdot 48! \cdot 48! \cdot 96! \cdot 32! \approx 10^{564}.$$

$K\_\text{cyc} \setminus K\_B$ 中的自同構數目：外側陪集 $\sigma\_\text{dual} \cdot \text{Inn}(G)$ 有 $|G| = 5616 \approx 10^{3.7}$ 個元素。

**比率：** $\sim 10^{560}$。

與 PSL$(2,7)$ 在 $|G| = 168$ 時的 $\sim 10^{6.3}$ 比率相比，$|G|$ 增加 $1.5$ 個數量級時擴展障礙增加 $554$ 個數量級。

### M$\_{12}$：反例

M$\_{12}$（$95040$ 階，外自同構群 $\mathbb{Z}/2$）的兩個 M$\_{11}$ 子群是自然候選。

- M$\_{11}\_a$：M$\_{12}$ 在 $12$ 點上自然作用的點穩定子。
- M$\_{11}\_b$：$12$ 點上的傳遞 M$\_{11}$。

兩者皆 $7920$ 階。它們在 $\text{Aut}($M$\_{12})$ 中共軛但在 M$\_{12}$ 中不共軛。

**Gassmann 測試在元素類層面失敗。** 元素類 $5, 6$（皆 $8$ 階）和 $12, 13$（皆 $4$ 階）被外自同構交換，但這些對位於 M$\_{12}$ 的**不同**循環 $G$-類中。

所以 M$\_{12}$ 外自同構 $\sigma$ 移動循環 $G$-類——$\sigma \notin K\_\text{cyc}$。

**結論：** $K\_\text{cyc}($M$\_{12}) = K\_B($M$\_{12}) = \text{Inn}($M$\_{12})$。M$\_{11}$ 對不是 $K\_\text{cyc}$-Gassmann 對。

### 為什麼有差別？

PSL$(n, q)$ 的對偶 $\sigma\_\text{dual}(M) = (M^T)^{-1}$ 有保持循環 $G$-類的代數理由：

1. $\sigma\_\text{dual}(M)$ 與 $M^{-1}$ 有相同的特徵多項式（轉置保持特徵多項式）。
2. $\langle M \rangle = \langle M^{-1} \rangle$。
3. 所以 $\sigma\_\text{dual}(\langle M \rangle) \sim\_G \langle M \rangle$。

M$\_{12}$ 的外自同構是**零散的**：它不來自任何反變矩陣運算，只來自 Mathieu 群的結構。沒有一般理由讓它保持循環 $G$-類，事實上它不保持。

### 猜想（n.310）

對所有 $n \geq 2$ 及使 PSL$(n, q)$ 簡單的素數冪 $q$，對偶外自同構 $\sigma\_\text{dual} \in $ Aut$($PSL$(n, q))$ 位於 $K\_\text{cyc} \setminus K\_B$ 中，實現點穩定子和超平面穩定子 Gassmann 對的交換。

*已在 $(n, q) \in \\{(2, 7), (3, 3)\\}$ 驗證。下一批測試案例：$(3, 4), (3, 5), (4, 2), (4, 3), \dots$*

如果猜想成立，PSL$(n, q)$ 是 $K\_\text{cyc} \supsetneq K\_B$ 例子的**正則無窮系列**。$K\_\text{cyc} / K\_B$ 的故事本質上與**射影幾何對偶**相關，而非與零散外自同構相關。

### 還開放的問題

- **嚴格證明猜想。** 上述草圖處理「正則」（正則半單）元素；非正則情形需要小心。

- **找一個外自同構群平凡的 Gassmann 對群。** 這將是充分性的反例。M$\_{11}$ 是候選但似乎沒有 Gassmann 對。最小的 Gassmann 對群在 $96$ 階（Bosma–de Smit 2002）；下一步是顯式構建它並檢查 Out。

- **找一個外自同構像 M$\_{12}$ 一樣移動循環 $G$-類的 Gassmann 對群。** 與 PSL$(n, q)$ 族不同。

- **融合系統類比。** $K\_F(F) := \ker(\text{Aut}(S) \to \text{Sym}(F\text{-子群類}))$。對 PSL$(n, q)$ 在素數 $p$ 處的融合系統，$K\_F$ 是否容許清潔的循環為主的過近似？

:::
