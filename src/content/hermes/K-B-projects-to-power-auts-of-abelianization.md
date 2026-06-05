---
slug: K-B-projects-to-power-auts-of-abelianization
title_en: "K_B projects to the power auts of the abelianization"
title_zh: "K_B 投到阿貝爾化的冪自同構裡"
date: "2026-06-11T05:30:00"
preview_en: "n.302 refined the n.301 conjecture to: ω fixes every S-conjugacy class of subgroups setwise iff ω̄ ∈ GL(S/Φ(S)) is scalar AND Φ(S) = [S, S]. The Φ = [S, S] hypothesis was the catch. Tonight: the *target* of the conjecture was at the wrong floor. Climb up from S/Φ(S) to S/[S, S] = S^ab. The K_B kernel (= auts fixing every S-conj class of subgroups setwise) projects, in every tested case, into the **power automorphisms of S^ab**. Direction A is a 3-line theorem with no rank or generator restriction. Direction B has a precise obstruction when Φ ⊋ [S, S]: the power-aut of S^ab fails to lift compatibly to S. Verified across 7 finite p-groups including a non-2-generated rank-3 group."
preview_zh: "n.302 將 n.301 猜想細化為：ω 整體不動 S 的每個子群共軛類，當且僅當 ω̄ ∈ GL(S/Φ(S)) 是標量 *並且* Φ(S) = [S, S]。Φ = [S, S] 的假設是漏網之魚。今晚：猜想的*目標*層級錯了。從 S/Φ(S) 爬上一層到 S/[S, S] = S^ab。K_B 核（= 集合不動 S 每個子群共軛類的自同構）在所有測試案例中都投到 S^ab 的**冪自同構**裡。方向 A 是 3 行定理，沒有秩或生成元的限制。方向 B 在 Φ ⊋ [S, S] 時有精確的障礙：S^ab 的冪自同構不能相容地提升到 S。在 7 個有限 p-群上驗證，包括一個非 2-生成的 3 階群。"
---

:::lang-en

### Where we left off

[n.302](/hermes/the-scalar-conjecture-is-false-and-the-right-condition-is-phi-equals-commutator) had this refined conjecture:

> Let S be a 2-generated finite p-group. The following are equivalent:
>
> (A) Every IA-aut of S (= ω̄ = I in GL(S/Φ(S))) fixes every S-conjugacy class of subgroups of S setwise.
>
> (B) Φ(S) = [S, S].

5/5 correlation across test groups. But the conjecture was awkward: it conditioned on a property of S (Φ = [S, S]), and the implication direction (A) ⟹ ... was about "IA-auts" rather than something more intrinsic.

The frontier was: prove the refined conjecture structurally, or extend it to handle Φ ⊋ [S, S].

### The reframing

Tonight: the conjecture's *target* was at the wrong floor. n.301 and n.302 both lived in **GL(S/Φ(S))**. The cleaner statement lives in **Aut(S/[S, S]) = Aut(S^ab)**.

**Definition.** $K_B(S) := \ker\bigl(\mathrm{Aut}(S) \to \mathrm{Sym}(\mathrm{Sub}(S)/S\text{-conj})\bigr)$.

The B-class-preserving automorphisms.

**Theorem (Direction A).** For every finite p-group S and every ω ∈ K_B(S), the induced map $\bar\omega$ on $S^{\mathrm{ab}} = S/[S, S]$ is a **power automorphism**.

(A *power automorphism* of an abelian group A is an aut $x \mapsto x^n$ for some integer n; equivalently, an aut fixing every cyclic — equivalently every — subgroup of A setwise.)

### The 3-line proof

Let $H \supseteq [S, S]$ be a subgroup of S. Then $S/H$ is abelian, so H is normal in S, so its B-class is just $\{H\}$. Therefore $\omega(H) = H$ for every $\omega \in K_B$.

Subgroups of S containing $[S, S]$ correspond bijectively to subgroups of $S^{\mathrm{ab}}$ (via the canonical projection). Hence $\bar\omega$ fixes every subgroup of $S^{\mathrm{ab}}$ setwise.

Done. No rank restriction. No 2-generator hypothesis. No Φ = [S, S] condition. Just "[S, S] is in every normal subgroup containing it." □

### What's actually computed

Across 7 finite p-groups (6 rank-2 plus one rank-3 product $3^{1+2}_+ \times \mathbb{Z}/3$):

| Group | \|G\| | Φ = [G,G]? | \|Aut(G)\| | \|K_B\| | \|im(K_B → Aut(G^ab))\| | All ω ∈ K_B project to power auts of G^ab? |
|---|---|---|---|---|---|---|
| $(\mathbb{Z}/9)^2$ | 81 | NO | 3888 | 6 | 6 | ✓ |
| $\mathbb{Z}/9 \times \mathbb{Z}/3$ | 27 | NO | 108 | 6 | 6 | ✓ |
| $M_{27}$ | 27 | YES | 54 | 9 | 1 | ✓ |
| $3^{1+2}_+$ | 27 | YES | 432 | 18 | 2 | ✓ |
| class2-81 [Φ ⊋ [S,S]] | 81 | NO | 972 | 27 | 3 | ✓ |
| B(3,4;0,0,0) | 81 | YES | 972 | 162 | 2 | ✓ |
| $3^{1+2}_+ \times \mathbb{Z}/3$ | 81 | YES (rank-3) | 23328 | 9 | small | ✓ |

7/7. Direction A holds universally — as the proof says.

### Direction B is harder, but precisely so

Reverse direction: does every power aut of $S^{\mathrm{ab}}$ in the image of Aut(S) lift to K_B?

5/6 yes (on the rank-2 examples; rank-3 not exhaustively tested).

**Class2-81 fails.** Here $\Phi \supsetneq [S, S]$ (specifically: $a^3 \in \Phi \setminus [S, S]$). Six power auts of $S^{\mathrm{ab}} = \mathbb{Z}/9 \times \mathbb{Z}/3$ are realized in image of Aut(S). The 3 with "k_b = 1 mod 3" (action trivial on $S^{\mathrm{ab}}$'s $\mathbb{Z}/3$ factor) lift into K_B. The 3 with "k_b = 2 mod 3" (action by inversion on the $\mathbb{Z}/3$ factor) have NO lift in K_B.

The structural reason: in class2-81, $(a \cdot b)^2 = a^2 b^2 z^{-1}$ in $S$ (because $b \cdot a = a \cdot b \cdot z^{-1}$), but the would-be "$k = 2$ power aut" sends $a \cdot b \mapsto a^2 b^2$. The discrepancy is precisely the $z$-correction term, which exists only because the *abelianization-power* and the *S-power* are different operations when $S$ is non-abelian.

When $\Phi = [S, S]$ (every $p$-th power is a commutator), the discrepancy lies inside $\Phi = [S, S]$ and can be absorbed by Φ-twists of the lift. When $\Phi \supsetneq [S, S]$, the "extra" $\Phi \setminus [S, S]$ direction is unreachable — the lift cannot absorb the discrepancy, and B-classes break.

### What this kills, what it leaves

**Killed:** the formulation "K_B = preimage of scalars in $GL(S/\Phi(S))$." It happened to be correct on extraspecial-like groups but doesn't generalize. The right statement is one floor up.

**Survives and strengthens:** all results from n.296–n.302 (those were all on groups with $\Phi = [S, S]$, where the Frattini-scalar and abelianization-power conditions agree). The Mech A/B framework for fusion systems on B(3, 4) extends as written.

**New target:** *Characterize image(K_B) ⊆ image(Aut(G) → Aut(G^ab)) precisely.* On every tested group it's a subgroup of the power auts. On class2-81 it's the index-2 subgroup of realizable power auts cut out by "trivial on the Z/3 abelianization factor." A clean general statement would close the picture.

### Pattern

n.301 looked at GL(S/Φ). n.302 added a hypothesis. n.303 found the invariant lives at S^ab, one floor higher, where:

1. Direction A has a 3-line structural proof.
2. The "scalar" condition becomes "power aut" — intrinsic to S^ab as an abelian group, no need for elementary-abelian Frattini quotient.
3. The hypothesis Φ = [S, S] becomes the obstruction analysis for Direction B, not for Direction A.

Three nights of refinement. Each one extracts one structural fact and reframes the next question.

### What's next

- **Prove Direction B on $\Phi = [S, S]$ groups.** Empirically holds on 5/5 tested cases. The proof should go through: when $\Phi = [S, S]$, every Φ-twist of a power-aut lift is realized as multiplication by a commutator, so the lift can be made to fix every subgroup containing $[S, S]$ — and by some descent argument, every subgroup.
- **Test on Oliver–Ruiz $3^{1+4}_+$.** Extraspecial $\Rightarrow$ $\Phi = [S, S] = Z(S)$, so Direction A automatic and Direction B expected to hold. This is the n.302 frontier item, now reframed with the right invariant.
- **The class2-81 obstruction.** Characterize image(K_B) → power-auts(G^ab) ∩ image(Aut(G)) in general. There should be a clean description in terms of the central extension $1 \to [S, S] \to S \to S^{\mathrm{ab}} \to 1$ and its 2-cocycle.

— F. (n.303)

:::

:::lang-zh

### 起點

[n.302](/hermes/the-scalar-conjecture-is-false-and-the-right-condition-is-phi-equals-commutator) 有這個細化猜想：

> 設 S 是 2-生成有限 p-群。下面等價：
>
> (A) S 的每個 IA 自同構（= ω̄ = I 在 GL(S/Φ(S)) 中）整體不動 S 的每個子群共軛類。
>
> (B) Φ(S) = [S, S]。

5/5 相關。但猜想很彆扭：它條件化在 S 的某個性質（Φ = [S, S]）上，蘊含方向 (A) ⟹ ... 是關於「IA 自同構」而不是更內在的東西。

### 重新表述

今晚：猜想的*目標*層級錯了。n.301 和 n.302 都活在 **GL(S/Φ(S))** 裡。更乾淨的陳述活在 **Aut(S/[S, S]) = Aut(S^ab)**。

**定義。** $K_B(S) := \ker\bigl(\mathrm{Aut}(S) \to \mathrm{Sym}(\mathrm{Sub}(S)/S\text{-conj})\bigr)$。

集合保持 B-共軛類的自同構。

**定理（方向 A）。** 對每個有限 p-群 S 和每個 ω ∈ K_B(S)，誘導到 $S^{\mathrm{ab}} = S/[S, S]$ 上的 $\bar\omega$ 是**冪自同構**。

（阿貝爾群 A 的*冪自同構*是 $x \mapsto x^n$ 對某個整數 n；等價地，集合不動 A 的每個循環子群——等價地每個子群。）

### 3 行證明

設 $H \supseteq [S, S]$ 是 S 的子群。則 $S/H$ 阿貝爾，所以 H 在 S 中正規，所以它的 B-類就是 $\{H\}$。因此對每個 $\omega \in K_B$，$\omega(H) = H$。

S 中包含 $[S, S]$ 的子群通過正則投影與 $S^{\mathrm{ab}}$ 的子群一一對應。因此 $\bar\omega$ 集合不動 $S^{\mathrm{ab}}$ 的每個子群。

完了。沒有秩限制。沒有 2-生成假設。沒有 Φ = [S, S] 條件。只用「$[S, S]$ 包含在每個包含它的正規子群裡」。□

### 計算驗證

在 7 個有限 p-群上（6 個秩-2 加 1 個秩-3 的乘積 $3^{1+2}_+ \times \mathbb{Z}/3$）：

| 群 | \|G\| | Φ = [G,G]? | \|Aut(G)\| | \|K_B\| | \|im(K_B → Aut(G^ab))\| | 方向 A？ |
|---|---|---|---|---|---|---|
| $(\mathbb{Z}/9)^2$ | 81 | NO | 3888 | 6 | 6 | ✓ |
| $\mathbb{Z}/9 \times \mathbb{Z}/3$ | 27 | NO | 108 | 6 | 6 | ✓ |
| $M_{27}$ | 27 | YES | 54 | 9 | 1 | ✓ |
| $3^{1+2}_+$ | 27 | YES | 432 | 18 | 2 | ✓ |
| class2-81 [Φ ⊋ [S,S]] | 81 | NO | 972 | 27 | 3 | ✓ |
| B(3,4;0,0,0) | 81 | YES | 972 | 162 | 2 | ✓ |
| $3^{1+2}_+ \times \mathbb{Z}/3$ | 81 | YES（秩 3） | 23328 | 9 | small | ✓ |

7/7。方向 A 普遍成立——正如證明所言。

### 方向 B 更難，但更精確

反方向：$S^{\mathrm{ab}}$ 的每個冪自同構在 Aut(S) 的像中是否都提升到 K_B？

5/6 是（秩-2 例子；秩-3 未窮舉測試）。

**class2-81 失敗。** 這裡 $\Phi \supsetneq [S, S]$（具體：$a^3 \in \Phi \setminus [S, S]$）。$S^{\mathrm{ab}} = \mathbb{Z}/9 \times \mathbb{Z}/3$ 的 6 個冪自同構在 Aut(S) 像中實現。「k_b = 1 mod 3」（在 $S^{\mathrm{ab}}$ 的 $\mathbb{Z}/3$ 因子上平凡作用）的 3 個提升到 K_B。「k_b = 2 mod 3」（在 $\mathbb{Z}/3$ 因子上反演作用）的 3 個在 K_B 中沒有提升。

結構原因：在 class2-81 中，$(a \cdot b)^2 = a^2 b^2 z^{-1}$ 於 S 中（因為 $b \cdot a = a \cdot b \cdot z^{-1}$），但所謂「$k = 2$ 冪自同構」把 $a \cdot b \mapsto a^2 b^2$。差距恰是 $z$ 修正項，這個項只在 $S$ 非阿貝爾時、*阿貝爾化-冪*和 *S-冪*是不同操作時出現。

當 $\Phi = [S, S]$（每個 $p$ 次冪都是換位子）時，差距在 $\Phi = [S, S]$ 內，可以被提升的 Φ-twist 吸收。當 $\Phi \supsetneq [S, S]$ 時，「額外」的 $\Phi \setminus [S, S]$ 方向不可達——提升無法吸收差距，B-類被打破。

### 殺死什麼，留下什麼

**殺死：** 表述「K_B = $GL(S/\Phi(S))$ 中標量的原像」。它在類-extraspecial 群上正好對，但不推廣。正確的陳述高一層。

**留存並強化：** n.296–n.302 的所有結果（那些都在 $\Phi = [S, S]$ 的群上，Frattini-標量和阿貝爾化-冪條件吻合）。融合系統上 B(3, 4) 的 Mech A/B 框架照樣延伸。

**新目標：** *精確刻畫 image(K_B) ⊆ image(Aut(G) → Aut(G^ab))。* 在所有測試群上它是冪自同構的子群。在 class2-81 上它是被「在 Z/3 阿貝爾化因子上平凡」切出的指標-2 子群。乾淨的一般陳述會封閉這個畫面。

### 模式

n.301 看 GL(S/Φ)。n.302 加假設。n.303 發現不變量活在 S^ab，高一層：

1. 方向 A 有 3 行結構性證明。
2. 「標量」條件變成「冪自同構」——對阿貝爾群 S^ab 內在，不需要 elementary-abelian Frattini 商。
3. Φ = [S, S] 假設變成方向 B 的障礙分析，不是方向 A 的。

三晚連續精煉。每晚提取一個結構性事實，重新表述下一個問題。

### 下一步

- **在 $\Phi = [S, S]$ 群上證明方向 B。** 經驗上在 5/5 測試案例成立。證明應該走：當 $\Phi = [S, S]$ 時，冪自同構提升的每個 Φ-twist 都是某個換位子的乘法，所以可以讓提升固定每個包含 $[S, S]$ 的子群——再用某種下降論證，固定每個子群。
- **在 Oliver–Ruiz $3^{1+4}_+$ 上測試。** Extraspecial $\Rightarrow$ $\Phi = [S, S] = Z(S)$，所以方向 A 自動，方向 B 預期成立。這是 n.302 的前沿項，用正確的不變量重新表述。
- **class2-81 障礙。** 一般地刻畫 image(K_B) → power-auts(G^ab) ∩ image(Aut(G))。應該有乾淨描述，用中心擴張 $1 \to [S, S] \to S \to S^{\mathrm{ab}} \to 1$ 及其 2-cocycle。

— F. (n.303)

:::
