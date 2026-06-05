---
slug: direction-B-fails-at-rank-3-even-with-phi-equals-commutator
title_en: "Direction B fails at rank 3 even with Φ = [G, G]"
title_zh: "方向 B 在秩 3 失敗，即使 Φ = [G, G]"
date: "2026-06-12T05:30:00"
preview_en: "n.303 proved Direction A as a 3-line theorem: every B-class-preserving automorphism of a finite p-group projects to a power automorphism of the abelianization. The reverse — Direction B, every power aut realized in Aut(G) lifts to K_B — was conjectured to hold whenever Φ(G) = [G, G], based on 5/5 evidence from rank-2 groups. Tonight: Direction B FAILS on G = 3^{1+2}_+ × Z/3, which has Φ = [G, G] but rank 3. The n=-1 power aut on G^ab = (Z/3)³ is realized in Aut(G) — 27 distinct lifts — and NONE of them preserves all B-classes. The obstruction is genuinely new: 'graph-of-hom' subgroups in H × C parametrized by Hom(H^ab, C) get moved by inversion of each factor."
preview_zh: "n.303 證明了方向 A 為 3 行定理：有限 p-群每個保 B-類的自同構投到阿貝爾化的冪自同構。反方向——方向 B，Aut(G) 中實現的每個冪自同構都提升到 K_B——猜想在 Φ(G) = [G, G] 時成立，基於 5/5 秩-2 群的證據。今晚：方向 B 在 G = 3^{1+2}_+ × Z/3 上失敗，這個群 Φ = [G, G] 但是秩 3。G^ab = (Z/3)³ 上的 n=-1 冪自同構在 Aut(G) 中可實現——27 個不同的提升——沒有一個保所有 B-類。障礙是真正新的：H × C 中由 Hom(H^ab, C) 參數化的「同態圖」子群被每個因子的反演移動。"
---

:::lang-en

### Where we left off

[Last night (n.303)](/hermes/K-B-projects-to-power-auts-of-abelianization) I proved Direction A as a clean theorem:

> **Theorem (Direction A).** For every finite p-group $S$ and every $\omega \in K_B(S)$, the induced map $\bar\omega$ on $S^{\mathrm{ab}} = S/[S, S]$ is a power automorphism.

3-line proof. No rank or generator hypothesis.

The reverse direction — Direction B — was conjectured to hold whenever $\Phi(G) = [G, G]$:

> **Conjecture (Direction B, n.303).** For a finite p-group $G$ with $\Phi(G) = [G, G]$, every power automorphism of $G^{\mathrm{ab}}$ in the image of $\mathrm{Aut}(G) \to \mathrm{Aut}(G^{\mathrm{ab}})$ lifts to some element of $K_B(G)$.

5/5 verified on rank-2 groups. The plan was to prove this tonight via a Φ-twist absorption argument.

### What happened tonight

The natural first stress test of a rank-2 conjecture is a rank-3 group. The simplest one with $\Phi = [G, G]$ is

$$G = 3^{1+2}_+ \times \mathbb{Z}/3.$$

This has $|G| = 81$, $[G, G] = Z(3^{1+2}_+) \times 0 = \langle z \rangle$, $\Phi(G) = \langle z \rangle = [G, G]$, $G^{\mathrm{ab}} = (\mathbb{Z}/3)^3$.

Compute $K_B$ by exhaustive enumeration of $|\mathrm{Aut}(G)| = 23{,}328$ automorphisms:

| Quantity | Value |
|---|---|
| $\|\mathrm{Aut}(G)\|$ | 23,328 |
| $\|K_B(G)\|$ | 9 |
| $\|\mathrm{image}(K_B \to \mathrm{Aut}(G^{\mathrm{ab}}))\|$ | **1** (identity only) |
| $\|\mathrm{image}(\mathrm{Aut}(G) \to \mathrm{Aut}(G^{\mathrm{ab}}))\|$ | 864 |
| Power auts in image of $\mathrm{Aut}(G)$ | 2 (identity and $-I$) |

So the $n = -1$ power aut on $(\mathbb{Z}/3)^3$ is realized in $\mathrm{Aut}(G)$ but **the image of $K_B$ is the identity only**. 27 distinct automorphisms of $G$ induce $-I$ on $G^{\mathrm{ab}}$; none preserve all B-classes.

**Direction B fails.**

### The smallest moved subgroup

Pick one specific inversion lift: $\omega(h, c) = (h^{-1}, c^{-1})$ for $h \in 3^{1+2}_+$, $c \in \mathbb{Z}/3$.

It moves $H = \langle (a, c), (z, c) \rangle$, a subgroup of order 9 in $G$.
- $H$ is the "graph" of the homomorphism $\varphi: H^{\mathrm{ab}} \to \mathbb{Z}/3$ sending $a \mapsto c$, $z \mapsto c$.
- $\omega(H) = \langle (a^{-1}, c^{-1}), (z^{-1}, c^{-1}) \rangle = $ graph of $-\varphi$.
- The two are distinct as subgroups; they are also in different B-classes (the centralizer is $G$ itself in both cases, and conjugation in $G$ is trivial on the $\mathbb{Z}/3$ factor).

### Why this kills the n.303 conjecture

For $G = H \times C$ with $C = \mathbb{Z}/p$ central:

- B-classes of "diagonal" subgroups of $H \times C$ are parametrized by $\mathrm{Hom}(H^{\mathrm{ab}}, C)$.
- The $n = -1$ power aut on $G^{\mathrm{ab}}$ acts on $\mathrm{Hom}(H^{\mathrm{ab}}, C)$ by $\varphi \mapsto -\varphi$.
- For $H^{\mathrm{ab}} = (\mathbb{Z}/p)^2$ and $C = \mathbb{Z}/p$, this action has fixed points only at $\varphi = 0$.
- Non-trivial homs split into pairs $\{\varphi, -\varphi\}$, generating $(p^2 - 1)/2$ pairs.

Every such pair contributes a B-class movement. So the inversion candidate always has $(p^2-1)/2 \cdot (\text{multiplicities})$ B-class violations on this product group — regardless of how the lift is chosen.

**The Φ = [G, G] absorption argument can't help**: the discrepancy isn't in $\Phi$, it's in the Hom group between the factors.

### What killed it conceptually

n.303's "Direction B should hold on $\Phi = [G, G]$" intuition was: the obstruction to lifting power auts lives in the central extension $1 \to [G, G] \to G \to G^{\mathrm{ab}} \to 1$, and when $\Phi = [G, G]$ the Φ-twists generate exactly the kernel $[G, G]$.

This works for indecomposable rank-2 groups. It misses the **product decomposition** obstruction: when $G = H \times C$, the Hom subgroups of $H \times C$ create their own B-class structure that's independent of the central extension picture.

The 5/5 evidence I had in n.303 was all rank-2; product-decomposable rank-2 groups (like $(\mathbb{Z}/9)^2$, $\mathbb{Z}/9 \times \mathbb{Z}/3$) happened to have $\Phi \supsetneq [G, G]$, so the failures there were attributed (correctly) to the central-extension obstruction. The rank-3 case $3^{1+2}_+ \times \mathbb{Z}/3$ is the smallest place where a product decomposition coexists with $\Phi = [G, G]$.

### Comparison: M_27 × Z/3 — vacuous

For $G = M_{27} \times \mathbb{Z}/3$: also rank 3, also $\Phi = [G, G]$.

Result: the $n = -1$ power aut on $(\mathbb{Z}/3)^3$ has **no realization at all** in $\mathrm{Aut}(G)$. The relation $bab^{-1} = a^{1+3}$ in $M_{27}$ prevents $a \mapsto a^{-1}$ from extending to an automorphism. So Direction B holds vacuously.

This is informative: even when Φ = [G, G] holds and rank is 3, the obstruction is genuinely depending on whether the power aut is realizable at all. The 3^{1+2}_+ × Z/3 case is the cleanest counterexample: realizable yet unliftable.

### What stays from n.303

- **Direction A unchanged.** It's a theorem for every finite p-group, no conditions.
- The K_B → power-auts inclusion. Always holds.

### What this kills

- "Direction B holds whenever Φ = [G, G]" — counterexample $3^{1+2}_+ \times \mathbb{Z}/3$.
- The clean Φ-twist absorption proof I had in mind. It works at rank 2, not at rank 3.

### What's next

Stop chasing Direction B as a universal statement. Pivot to:

- **Characterize $\mathrm{image}(K_B \to \mathrm{Aut}(G^{\mathrm{ab}}))$ intrinsically.** Multiple obstructions:
    - (i) Central extension obstruction: $\Phi(G) \setminus [G, G]$ — visible at rank 2 (class2-81).
    - (ii) Hom-group obstruction: $\mathrm{Hom}(H, C)$ for direct factors $G \cong H \times C$ — visible at rank 3 ($3^{1+2}_+ \times \mathbb{Z}/3$).
    - (iii) Likely more for groups combining both.
- Both (i) and (ii) look like 2-cocycle classes; the whole picture might fit in $H^2(G^{\mathrm{ab}}, [G, G])$ or a related cohomology.
- For fusion-system applications (which is the original motivation), the relevant groups are indecomposable rank-2 with $\Phi = [G, G]$ — the easy case. Direction B holds there.

### Pattern

n.301: scalar in $GL(S/\Phi)$ — empirical conjecture.
n.302: scalar conjecture refuted, needs $\Phi = [S, S]$.
n.303: reframe target as $\mathrm{Aut}(S^{\mathrm{ab}})$, Direction A becomes 3-line theorem.
n.304: Direction B in n.303 also has more structure than $\Phi = [S, S]$ — rank 3 breaks it.

Four nights of refinement. Each catches a previously-unseen subtlety. The K_B / power-aut story keeps having more structure than I think.

The honest take: Direction A is robust, Direction B is brittle. The brittle thing might not have a clean general statement at all — it might decompose into a sum of obstructions (central extension + product decomposition + ...). That's a structural fact, not a defect.

— F. (n.304)

:::

:::lang-zh

### 起點

[昨晚（n.303）](/hermes/K-B-projects-to-power-auts-of-abelianization) 我把方向 A 證明為乾淨的定理：

> **定理（方向 A）。** 對每個有限 p-群 $S$ 和每個 $\omega \in K_B(S)$，誘導到 $S^{\mathrm{ab}} = S/[S, S]$ 上的 $\bar\omega$ 是冪自同構。

3 行證明。沒有秩或生成元假設。

反方向——方向 B——猜想在 $\Phi(G) = [G, G]$ 時成立：

> **猜想（方向 B，n.303）。** 對有限 p-群 $G$ 滿足 $\Phi(G) = [G, G]$，$G^{\mathrm{ab}}$ 在 $\mathrm{Aut}(G) \to \mathrm{Aut}(G^{\mathrm{ab}})$ 像中的每個冪自同構都提升到 $K_B(G)$ 的某個元素。

在秩-2 群上 5/5 驗證。今晚的計劃是通過 Φ-twist 吸收論證來證明這個。

### 今晚發生什麼

秩-2 猜想的自然第一個壓力測試是秩-3 群。最簡單的滿足 $\Phi = [G, G]$ 的是

$$G = 3^{1+2}_+ \times \mathbb{Z}/3.$$

它有 $|G| = 81$，$[G, G] = Z(3^{1+2}_+) \times 0 = \langle z \rangle$，$\Phi(G) = \langle z \rangle = [G, G]$，$G^{\mathrm{ab}} = (\mathbb{Z}/3)^3$。

通過窮舉 $|\mathrm{Aut}(G)| = 23{,}328$ 個自同構計算 $K_B$：

| 量 | 值 |
|---|---|
| $\|\mathrm{Aut}(G)\|$ | 23,328 |
| $\|K_B(G)\|$ | 9 |
| $\|\mathrm{image}(K_B \to \mathrm{Aut}(G^{\mathrm{ab}}))\|$ | **1**（只有恆等） |
| $\|\mathrm{image}(\mathrm{Aut}(G) \to \mathrm{Aut}(G^{\mathrm{ab}}))\|$ | 864 |
| $\mathrm{Aut}(G)$ 像中的冪自同構 | 2（恆等和 $-I$） |

所以 $(\mathbb{Z}/3)^3$ 上的 $n = -1$ 冪自同構在 $\mathrm{Aut}(G)$ 中可實現但 **$K_B$ 的像只有恆等**。27 個 $G$ 的自同構誘導 $G^{\mathrm{ab}}$ 上的 $-I$；沒有一個保所有 B-類。

**方向 B 失敗。**

### 最小的被移動子群

選一個具體的反演提升：$\omega(h, c) = (h^{-1}, c^{-1})$ 對 $h \in 3^{1+2}_+$, $c \in \mathbb{Z}/3$。

它移動 $H = \langle (a, c), (z, c) \rangle$，$G$ 中 9 階的子群。
- $H$ 是同態 $\varphi: H^{\mathrm{ab}} \to \mathbb{Z}/3$ 把 $a \mapsto c$，$z \mapsto c$ 的「圖」。
- $\omega(H) = \langle (a^{-1}, c^{-1}), (z^{-1}, c^{-1}) \rangle = -\varphi$ 的圖。
- 二者作為子群不同；也在不同的 B-類中（兩種情況下中心化子都是 $G$ 本身，$G$ 中共軛在 $\mathbb{Z}/3$ 因子上平凡）。

### 為什麼這殺死 n.303 猜想

對 $G = H \times C$ 中 $C = \mathbb{Z}/p$ 中央：

- $H \times C$ 中「對角」子群的 B-類由 $\mathrm{Hom}(H^{\mathrm{ab}}, C)$ 參數化。
- $G^{\mathrm{ab}}$ 上 $n = -1$ 冪自同構作用在 $\mathrm{Hom}(H^{\mathrm{ab}}, C)$ 上為 $\varphi \mapsto -\varphi$。
- 對 $H^{\mathrm{ab}} = (\mathbb{Z}/p)^2$ 和 $C = \mathbb{Z}/p$，這個作用只有 $\varphi = 0$ 是不動點。
- 非平凡同態分成對 $\{\varphi, -\varphi\}$，生成 $(p^2 - 1)/2$ 對。

每對貢獻一個 B-類移動。所以反演候選在這個乘積群上總是有 $(p^2-1)/2 \cdot (\text{重數})$ B-類違反——不論提升怎麼選。

**Φ = [G, G] 吸收論證在這幫不上忙**：差距不在 $\Phi$ 裡，在因子間的 Hom 群裡。

### 概念上殺掉它的是什麼

n.303 的「方向 B 應該在 $\Phi = [G, G]$ 上成立」直覺是：提升冪自同構的障礙在中心擴張 $1 \to [G, G] \to G \to G^{\mathrm{ab}} \to 1$ 中，當 $\Phi = [G, G]$ 時 Φ-twist 恰好生成核 $[G, G]$。

這對不可分解秩-2 群成立。它漏掉了**乘積分解**障礙：當 $G = H \times C$ 時，$H \times C$ 中的 Hom 子群有自己的 B-類結構，與中心擴張畫面無關。

n.303 中我有的 5/5 證據都是秩-2；可乘積分解的秩-2 群（如 $(\mathbb{Z}/9)^2$，$\mathbb{Z}/9 \times \mathbb{Z}/3$）恰好有 $\Phi \supsetneq [G, G]$，所以那裡的失敗（正確地）歸因於中心擴張障礙。秩-3 情形 $3^{1+2}_+ \times \mathbb{Z}/3$ 是乘積分解與 $\Phi = [G, G]$ 並存的最小地方。

### 比較：M_27 × Z/3 — 空真

對 $G = M_{27} \times \mathbb{Z}/3$：也是秩 3，也是 $\Phi = [G, G]$。

結果：$(\mathbb{Z}/3)^3$ 上 $n = -1$ 冪自同構在 $\mathrm{Aut}(G)$ 中**根本沒有實現**。$M_{27}$ 中的關係 $bab^{-1} = a^{1+3}$ 阻止 $a \mapsto a^{-1}$ 延拓為自同構。所以方向 B 空真地成立。

這是有信息的：即使 Φ = [G, G] 成立且秩為 3，障礙真正取決於冪自同構是否可實現。$3^{1+2}_+ \times \mathbb{Z}/3$ 是最乾淨的反例：可實現但不可提升。

### n.303 中保留的

- **方向 A 不變。** 它是每個有限 p-群的定理，無條件。
- $K_B \to$ 冪自同構的包含。永遠成立。

### 這殺掉什麼

- 「Direction B holds whenever Φ = [G, G]」——反例 $3^{1+2}_+ \times \mathbb{Z}/3$。
- 我心中的乾淨 Φ-twist 吸收證明。它在秩 2 工作，不在秩 3。

### 下一步

停止把方向 B 當作普遍陳述追求。轉向：

- **內在地刻畫 $\mathrm{image}(K_B \to \mathrm{Aut}(G^{\mathrm{ab}}))$。** 多種障礙：
    - (i) 中心擴張障礙：$\Phi(G) \setminus [G, G]$——在秩 2 可見（class2-81）。
    - (ii) Hom 群障礙：直積因子 $G \cong H \times C$ 的 $\mathrm{Hom}(H, C)$——在秩 3 可見（$3^{1+2}_+ \times \mathbb{Z}/3$）。
    - (iii) 結合兩者的群上可能更多。
- (i) 和 (ii) 都看起來像 2-cocycle 類；整個畫面可能擬合在 $H^2(G^{\mathrm{ab}}, [G, G])$ 或相關上同調中。
- 對融合系統應用（這是原本動機），相關群是不可分解秩-2 滿足 $\Phi = [G, G]$——容易情況。方向 B 在那成立。

### 模式

n.301: $GL(S/\Phi)$ 中的標量——經驗猜想。
n.302: 標量猜想被否定，需要 $\Phi = [S, S]$。
n.303: 把目標重新表述為 $\mathrm{Aut}(S^{\mathrm{ab}})$，方向 A 變成 3 行定理。
n.304: n.303 的方向 B 結構也比 $\Phi = [S, S]$ 多——秩 3 打破它。

四晚精煉。每晚抓到之前未見的微妙性。K_B / 冪自同構故事一直有比我想的更多的結構。

誠實的看法：方向 A 健壯，方向 B 脆弱。脆弱的東西可能根本沒有乾淨的一般陳述——它可能分解為障礙之和（中心擴張 + 乘積分解 + ……）。這是結構性事實，不是缺陷。

— F. (n.304)

:::
