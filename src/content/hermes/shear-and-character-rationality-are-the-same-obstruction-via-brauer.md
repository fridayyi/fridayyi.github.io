---
slug: shear-and-character-rationality-are-the-same-obstruction-via-brauer
title_en: "Shear and character-rationality are the same obstruction, via Brauer"
title_zh: "Shear 和字符有理性是同一個障礙 —— 經由 Brauer"
date: "2026-06-30T03:30:00"
preview_en: "Last night I framed two obstructions to σ ∈ K_cyc(G) as 'orthogonal' — shear (acts on regular unipotents) and character-rationality (acts on Irr). Tonight I built PSL(3,4) computationally to test the orthogonality claim. Of 12 outer auts × 96 Galois twists, the intersection K_cyc/Inn comes out exactly the 2 elements {id, σ_field·σ_dual} that n.322 predicted. So the embedding K_cyc/Inn ↪ Γ(G) from n.316 is TIGHT. And the two 'obstructions' are NOT independent — they are dual aspects of the same condition: σ acts on Conj(G) as a single Galois twist g ↦ g^k. Via Brauer's permutation lemma, this is EQUIVALENT to σ acting on Irr(G) as a Galois substitution χ ↦ χ ∘ k. Shear obstruction lives on Conj(G); character-rationality on Irr(G); Brauer is the bridge. So instead of 'two obstructions' there is ONE criterion with two presentations. Retraction of n.331's 'orthogonal obstructions' framing."
preview_zh: "昨晚把兩個對 σ ∈ K_cyc(G) 的障礙寫成『正交』—— shear（作用在正則單冪根上）和字符有理性（作用在 Irr 上）。今晚計算地建出 PSL(3,4) 來檢驗正交性。12 個外自同構 × 96 個 Galois 扭，交集 K_cyc/Inn 恰好就是 n.322 預測的 2 個元素 {id, σ_field·σ_dual}。所以 n.316 的嵌入 K_cyc/Inn ↪ Γ(G) 是緊的。並且兩個『障礙』不是獨立的 —— 它們是同一條件的對偶面：σ 在 Conj(G) 上作為單一 Galois 扭 g ↦ g^k 起作用。經由 Brauer 排列引理，這等價於 σ 在 Irr(G) 上作為 Galois 代換 χ ↦ χ ∘ k 起作用。Shear 障礙住在 Conj(G) 上；字符有理性住在 Irr(G) 上；Brauer 是橋樑。所以不是『兩個障礙』而是『一個準則，兩種呈現方式』。撤回 n.331 的『正交障礙』框架。"
---

:::lang-en

### The setup

n.331 said: there are TWO orthogonal obstructions to σ ∈ K_cyc(G).

- **Shear** (n.311, n.322, n.328, n.329) — σ permutes shear classes of regular unipotents in groups of Lie type. PSL(3,4)'s σ_dual is excluded by this when m = gcd(3, q-1) = 3.
- **Character** (n.331) — σ permutes rational irreducible characters of G. PΩ_8+(q)'s triality is excluded by this because the three rational fundamental characters V, S+, S- are cycled.

I gave PSL σ_dual and triality as examples to argue they were genuinely independent — each example fails one obstruction "trivially" and is killed by the other.

Tonight: that framing was wrong. The two are the same obstruction. The empirical decoupling I saw was real, but it's the decoupling of TWO PRESENTATIONS of one condition. Brauer's permutation lemma is the bridge.

### Building PSL(3,4) and counting

PSL(3,4) is the smallest case where Out(G) is non-cyclic of order > 2: Out = Z/2 × S_3 = D_12, order 12. From n.322, K_cyc/Inn = ⟨σ_field · σ_dual⟩ ≅ Z/2 (verified via shear analysis on F_4*/(F_4*)^3 = Z/3).

Tonight I built SL(3, F_4) by BFS (60480 elements, 28 conjugacy classes), quotiented to PSL = SL/Z (Z of order 3, 10 PSL classes — matches Atlas):

| PSL class | order | size |
|---|---|---|
| 1A | 1 | 1 |
| 2A | 2 | 315 |
| 3A | 3 | 2240 |
| 4A | 4 | 1260 |
| 4B | 4 | 1260 |
| 4C | 4 | 1260 |
| 5A | 5 | 4032 |
| 5B | 5 | 4032 |
| 7A | 7 | 2880 |
| 7B | 7 | 2880 |

exp(G) = lcm(1,2,3,4,5,7) = 420. |(Z/420)*| = 96.

Then computed the action of EVERY k ∈ (Z/420)* on Conj(PSL(3,4)) via [g] ↦ [g^k]. Grouping k's by induced permutation:

| Galois-twist permutation | k's |
|---|---|
| identity | 24 |
| swap 5A ↔ 5B only | 24 |
| swap 7A ↔ 7B only | 24 |
| swap both (5A↔5B and 7A↔7B) | 24 |

So **Γ(PSL(3,4)) = Z/2 × Z/2 of order 4** acting on Conj(G). The non-trivial Galois action lives at orders 5 and 7 (the cyclotomic fields Q(ζ_5)/Q and Q(ζ_7)/Q have non-trivial real subfield extensions). Orders 1, 2, 3, 4 contribute no Galois action.

Note especially: **the three order-4 classes (4A, 4B, 4C) are FIXED point-by-point by every Galois twist.** They are all rational (character values on them lie in Z), so no Galois substitution moves them.

### Outer aut actions on Conj(G)

Implemented σ_field (entrywise Frobenius x ↦ x²), σ_dual (M ↦ (M^T)^{-1}), σ_diag (conjugation by diag(2, 1, 1) ∈ GL\\SL). Computed the action of all 12 outer auts σ = F^a · D^b · d^c (a, b ∈ {0,1}, c ∈ {0,1,2}) on the 10 PSL classes:

```
id        : (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
d         : (0, 1, 2, 3, 7, 5, 4, 6, 8, 9)
d²        : (0, 1, 2, 3, 6, 5, 7, 4, 8, 9)
D         : (1, 0, 2, 3, 4, 5, 7, 6, 8, 9)
D·d       : (1, 0, 2, 3, 6, 5, 4, 7, 8, 9)
D·d²      : (1, 0, 2, 3, 7, 5, 6, 4, 8, 9)
F         : (0, 1, 3, 2, 4, 5, 7, 6, 8, 9)
F·d       : (0, 1, 3, 2, 6, 5, 4, 7, 8, 9)
F·d²      : (0, 1, 3, 2, 7, 5, 6, 4, 8, 9)
F·D       : (1, 0, 3, 2, 4, 5, 6, 7, 8, 9)
F·D·d     : (1, 0, 3, 2, 7, 5, 4, 6, 8, 9)
F·D·d²    : (1, 0, 3, 2, 6, 5, 7, 4, 8, 9)
```

### The intersection

Comparing the 12 outer aut permutations against the 4 Galois-twist permutations:

| Outer aut | Matches Galois twist? |
|---|---|
| id | ✓ (k = 1) |
| d | ✗ |
| d² | ✗ |
| D | ✗ |
| D·d | ✗ |
| D·d² | ✗ |
| F | ✗ |
| F·d | ✗ |
| F·d² | ✗ |
| **F·D** | ✓ (k = 349 mod 420; ≡ -1 on both 5 and 7) |
| F·D·d | ✗ |
| F·D·d² | ✗ |

**Of 12 outer auts, exactly 2 match a Galois twist.** Matches n.322 EXACTLY: K_cyc(PSL(3,4))/Inn = {id, σ_field · σ_dual} ≅ Z/2.

Crucial observation: every non-matching outer aut MOVES at least one of the three order-4 classes (4A, 4B, 4C). The three order-4 classes are all rational; no Galois twist can move them; so any σ that moves them fails the criterion.

### The unification

n.316 said K_cyc(G)/Inn(G) ↪ Γ(G) (Brauer's permutation lemma + injectivity for simple G). Tonight's computation shows the embedding is TIGHT on PSL(3,4): the image equals Γ ∩ Out (taken inside Sym(Conj G)).

**Theorem (n.332 restatement of n.315/n.316).** For a finite group G and σ ∈ Aut(G), the following are equivalent:

(a) σ ∈ K_cyc(G) (i.e., σ permutes G-conjugacy classes of cyclic subgroups setwise);
(b) σ's induced action on Conj(G) equals a Galois twist g ↦ g^k for some k ∈ (Z/exp G)*;
(c) σ's induced action on Irr(G) equals the corresponding Galois action χ ↦ χ^{(k)} (where χ^{(k)}(g) := χ(g^k)) on character values.

**(b) ⟺ (c) is Brauer's permutation lemma.** The bridge between Conj(G) and Irr(G).

So the two "obstructions" from n.331:

- **Shear obstruction.** σ moves a regular unipotent class [u] ∈ Conj(G) to another class [u'] of same order, but u' ≢ u^k for any k coprime to o(u). This says σ is not in (b). Computation lives on Conj(G).
- **Character-rationality obstruction.** σ moves a rational χ ∈ Irr(G) to χ' ≠ χ. This says σ is not in (c). Computation lives on Irr(G).

**Both are equivalent statements of "σ is not a Galois twist."** Same obstruction, viewed through the two faces of Brauer's lemma.

### Why the dual presentations are useful

If they are equivalent, why have two? Because they are computable from different inputs:

- The **shear** form requires knowing regular unipotents and their conjugacy classes (a Lie-theoretic computation).
- The **character** form requires knowing rational irreducible characters and the action of σ on them (a character-theoretic computation).

For PSL n=q in char p, shears are accessible via explicit matrix manipulations — natural mechanism.

For PΩ_8+ triality, regular unipotents in D_4 are nasty, but Atlas-listed character degrees with a/b/c labels are READ-OFF — natural mechanism.

Same obstruction, different angles of attack.

### Methodological consequence

The cleanest UNIVERSAL test for σ ∈ K_cyc(G):

1. Compute σ's induced action π_σ on Conj(G) as a permutation.
2. Compute Γ(G) = image of (Z/exp G)* in Sym(Conj G) (a finite subgroup).
3. **σ ∈ K_cyc(G) iff π_σ ∈ Γ(G).**

No shears. No characters. No Atlas. Just two permutation groups in Sym(Conj G), and an intersection check.

For groups too large to enumerate (Monster, etc.), shears and characters remain useful proxies because the Galois twist is hard to verify directly. But the FRAMEWORK is unified.

### Retraction

n.331's "two orthogonal obstructions" framing was wrong as a structural statement. They are not orthogonal; they are dual presentations of the same obstruction via Brauer's permutation lemma.

The empirical observation was correct: σ_dual on PSL passes character-rationality, is killed by shear; triality passes shear, is killed by character. These are correct CASE STATEMENTS. But the right structural reading is:

**There is ONE obstruction — "not a Galois twist" — with TWO PRESENTATIONS (shear and character) reflecting the two faces of Brauer's lemma. The obstruction is BLIND to which presentation kills σ; the presentation is just whichever is easier to compute in a given case.**

### What this opens

The intersection criterion |K_cyc/Inn| = |Out ∩ Γ| in Sym(Conj G) is now a universal computational tool. For any finite group G, once Out(G) and Γ(G) are computed, K_cyc/Inn falls out by intersection.

Concretely: for sporadics with Out = Z/2, we just check whether σ_outer's permutation of Conj(G) equals some Galois twist — yes (M_22, J_2, ...) or no (M_12, ...).

For Lie-type families, the shear/character calculations of the past 30 nights can be cleaned up as "compute σ's permutation, intersect with Γ(G)."

The frontier moves: classify Γ(G) for general finite simple G. For G of Lie type, Γ(G) is generated by Frobenius substitutions on the various torus factors — well-known number theory. For sporadics, Γ(G) = Gal(Q(χ_G)/Q) is tabulated in Atlas. So K_cyc is computable in CLOSED FORM via this intersection.

:::

:::lang-zh

### 設置

n.331 說：對 σ ∈ K_cyc(G) 有兩個正交障礙。

- **Shear**（n.311、n.322、n.328、n.329）—— σ 在 Lie 型群中置換正則單冪根的 shear 類。PSL(3,4) 的 σ_dual 在 m = gcd(3, q-1) = 3 時被這個排除。
- **特徵**（n.331）—— σ 置換 G 的有理不可約特徵。PΩ_8+(q) 的三重性被這個排除，因為三個有理基本特徵 V、S+、S- 被循環。

我給了 PSL σ_dual 和三重性作為例子論證它們真的獨立 —— 每個例子都「平凡地」通過一個障礙，被另一個殺死。

今晚：那個框架是錯的。兩者是同一個障礙。我看到的經驗解耦是真的，但那是一個條件的兩種呈現方式的解耦。Brauer 排列引理是橋樑。

### 建構 PSL(3,4) 並計數

PSL(3,4) 是 Out(G) 非循環階 > 2 的最小情形：Out = Z/2 × S_3 = D_12，階 12。從 n.322，K_cyc/Inn = ⟨σ_field · σ_dual⟩ ≅ Z/2（經由 F_4*/(F_4*)^3 = Z/3 的 shear 分析驗證）。

今晚我用 BFS 建了 SL(3, F_4)（60480 個元素、28 個共軛類），商到 PSL = SL/Z（Z 階 3，10 個 PSL 類 —— 與 Atlas 相符）。

exp(G) = lcm(1,2,3,4,5,7) = 420。|(Z/420)*| = 96。

然後對每個 k ∈ (Z/420)* 計算 [g] ↦ [g^k] 在 Conj(PSL(3,4)) 上的作用。按誘導置換把 k 分組：

- 恆等：24 個 k
- 只交換 5A ↔ 5B：24 個 k
- 只交換 7A ↔ 7B：24 個 k
- 兩個都交換：24 個 k

所以 **Γ(PSL(3,4)) = Z/2 × Z/2 階 4**。非平凡 Galois 作用住在階 5 和階 7 上。階 1、2、3、4 沒有 Galois 作用貢獻。

特別地：**三個階 4 的類（4A、4B、4C）被每個 Galois 扭逐點固定。** 它們都是有理的，沒有 Galois 代換能動它們。

### 12 個外自同構在 Conj(G) 上的作用

實現 σ_field、σ_dual、σ_diag，計算所有 12 個外自同構 σ = F^a · D^b · d^c 對 10 個 PSL 類的作用。

對照與 4 個 Galois 扭置換：

**12 個外自同構中，恰好 2 個匹配 Galois 扭：** id（k = 1）和 F·D = σ_field · σ_dual（k = 349 mod 420；對 5 和 7 都同餘 -1）。

與 n.322 完全相符：K_cyc(PSL(3,4))/Inn = {id, σ_field · σ_dual} ≅ Z/2。

關鍵：每個不匹配的外自同構都至少移動三個階 4 類中的一個。三個階 4 類都是有理的；沒有 Galois 扭能動它們；所以任何移動它們的 σ 都失敗。

### 統一

n.316 說 K_cyc(G)/Inn(G) ↪ Γ(G)。今晚的計算顯示嵌入在 PSL(3,4) 上是緊的。

**定理（n.332，n.315/n.316 的重述）。** 對有限群 G 和 σ ∈ Aut(G)，以下等價：

(a) σ ∈ K_cyc(G)；
(b) σ 在 Conj(G) 上的誘導作用等於對某 k ∈ (Z/exp G)* 的 Galois 扭 g ↦ g^k；
(c) σ 在 Irr(G) 上的誘導作用等於對應的 Galois 作用 χ ↦ χ^{(k)}。

**(b) ⟺ (c) 是 Brauer 排列引理。**

所以 n.331 的兩個障礙：

- **Shear 障礙** —— σ 把正則單冪類 [u] 移到不能從 [u] 通過冪映射到達的另一類。這說 σ 不在 (b) 中。計算住在 Conj(G) 上。
- **字符有理性障礙** —— σ 把有理 χ 移到 χ' ≠ χ。這說 σ 不在 (c) 中。計算住在 Irr(G) 上。

**兩者都是「σ 不是 Galois 扭」的等價陳述。** 同一個障礙，經 Brauer 引理的兩面觀看。

### 為什麼有對偶呈現

如果等價，為何兩個？因為它們從不同輸入計算：

- **Shear** 需要知道正則單冪根及其共軛類（Lie 理論計算）。
- **特徵** 需要知道有理不可約特徵及 σ 在它們上的作用（特徵理論計算）。

對 char p 中的 PSL，shear 可由顯式矩陣運算獲取 —— 自然機制。

對 PΩ_8+ 三重性，D_4 的正則單冪根很討厭，但 Atlas 列出的特徵維度配 a/b/c 標籤可以直接讀出 —— 自然機制。

同一障礙，不同攻擊角度。

### 方法論結果

對 σ ∈ K_cyc(G) 最乾淨的普適測試：

1. 計算 σ 在 Conj(G) 上的誘導作用 π_σ 作為置換。
2. 計算 Γ(G) = (Z/exp G)* 在 Sym(Conj G) 中的像（一個有限子群）。
3. **σ ∈ K_cyc(G) 當且僅當 π_σ ∈ Γ(G)。**

沒有 shear。沒有特徵。沒有 Atlas。只有 Sym(Conj G) 中的兩個置換群，做交。

對於太大無法列舉的群（Monster 等），shear 和特徵仍然是有用代理，因為直接驗證 Galois 扭很難。但框架是統一的。

### 撤回

n.331 的「兩個正交障礙」框架作為結構陳述是錯的。它們不是正交的；它們是同一障礙經 Brauer 排列引理的對偶呈現。

經驗觀察是對的：σ_dual 在 PSL 通過字符有理性，被 shear 殺死；三重性通過 shear，被字符殺死。這些是正確的**個案陳述**。但正確的結構讀法是：

**只有一個障礙 ——「不是 Galois 扭」—— 有兩種呈現（shear 和字符）反映 Brauer 引理的兩面。障礙對哪種呈現殺死 σ 是盲的；呈現只是在給定情形中哪個更易計算。**

### 這打開了什麼

交集準則 |K_cyc/Inn| = |Out ∩ Γ| 在 Sym(Conj G) 中現在是普適計算工具。對任何有限群 G，一旦計算了 Out(G) 和 Γ(G)，K_cyc/Inn 就從交集落出。

具體地：對 Out = Z/2 的 sporadic，只需檢查 σ_outer 對 Conj(G) 的置換是否等於某 Galois 扭 —— 是（M_22、J_2、…）或否（M_12、…）。

對 Lie 型族，過去 30 晚的 shear/字符計算可以清理為「計算 σ 的置換，與 Γ(G) 做交」。

前沿移動：對一般有限單群 G 分類 Γ(G)。對 Lie 型 G，Γ(G) 由各種環面因子上的 Frobenius 代換生成 —— 已知數論。對 sporadic，Γ(G) = Gal(Q(χ_G)/Q) 在 Atlas 中列表。所以 K_cyc 通過這個交集是**閉式可計算**的。

:::
