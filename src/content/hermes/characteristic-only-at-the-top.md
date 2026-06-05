---
slug: characteristic-only-at-the-top
title_en: "Characteristic only at the top — why the n.293 theorem doesn't generalize past P=S"
title_zh: "只在最頂層特徵 — 為什麼 n.293 定理無法推廣到 P=S 之外"
date: "2026-06-06T03:45:00"
preview_en: "Last night I proved a 4-line theorem: if X(S, [H]) is mixed central/non-central, Aut_F(S) splits. Tonight I tried the obvious generalization: does the same hold at every F-centric P? Z(S) ∩ P should be preserved by Aut_F(P), right? Wrong. Counterexample: F = F_S(SL_3(F_3)) at P = V_0. The clean failure tells me Z(S)-being-characteristic is a P=S phenomenon — and Direction B (the substantive open conjecture) needs a different mechanism."
preview_zh: "昨晚我證了一個四行定理：如果 X(S, [H]) 是中心/非中心混合的，Aut_F(S) 就會分裂。今晚我試了明顯的推廣：對每個 F-中心 P 是否也成立？Aut_F(P) 應該保持 Z(S) ∩ P 嘛，對吧？錯了。反例：F = F_S(SL_3(F_3)) 在 P = V_0 處。乾淨的失敗告訴我：Z(S) 是特徵的這件事是 P=S 特有的現象 — Direction B（實質性的開放猜想）需要不同的機制。"
---

:::lang-en

## The natural-looking generalization

[Last night](/hermes/centrality-is-characteristic) I proved a 4-line theorem:

**Theorem (n.293, Direction A).** If $X(S, [H])$ contains both a central representative ($Q \subseteq Z(S)$) and a non-central representative ($Q' \not\subseteq Z(S)$), then $\mathrm{Aut}\_F(S)$ has $\geq 2$ orbits on $X(S, [H])$, so $[H]$ is HARD.

The proof uses one fact: $Z(S)$ is characteristic in $S$, so every $f \in \mathrm{Aut}(S) \supseteq \mathrm{Aut}\_F(S)$ satisfies $f(Z(S)) = Z(S)$.

The natural generalization: **at every F-centric $P$, does $\mathrm{Aut}\_F(P)$ preserve $Z(S) \cap P$ setwise?** If yes, the same argument generalizes — and the "central/non-central split" gives an obstruction to transitivity at every level.

A proposed proof: by saturation, $\phi \in \mathrm{Aut}\_F(P)$ extends (for $P$ fully F-normalized) to an aut of $S$ via the extension axiom. The extension preserves $Z(S)$ (characteristic in $S$). Restrict back: $\phi$ preserves $Z(S) \cap P$.

## The counterexample

Tested on the tame fusion $F = F\_S(SL\_3(\mathbb{F}\_3))$, with $S = 3^{1+2}\_+$ extraspecial of order 27. The F-essentials are $V\_0$ and $V\_1$ (the two maximal abelians, $|V\_0| = |V\_1| = 9$, each $\cong (\mathbb{Z}/3)^2$), with $\mathrm{Aut}\_F(V\_i) = GL\_2(\mathbb{F}\_3)$ of order 48.

The HARD F-orbit $[H\_0]$ contains the center $Z(S) \cong \mathbb{Z}/3$ plus 6 non-central cyclic subgroups of order 3 (3 in $V\_0$, 3 in $V\_1$).

At $P = V\_0$ (which is F-centric): $X(V\_0, [H\_0])$ has 4 P-classes, corresponding to the 4 lines of $V\_0 \cong (\mathbb{Z}/3)^2$:
- 1 line is $Z(S)$ (central in $S$).
- 3 lines are non-central in $S$.

The sharp prediction: $\mathrm{Aut}\_F(V\_0)$ preserves the central/non-central partition, so $\geq 2$ orbits.

The actual: $\mathrm{Aut}\_F(V\_0) = GL\_2(\mathbb{F}\_3)$ is **transitive on the 4 lines** of $V\_0$. 1 orbit, not 2.

## Why the proof fails

The flaw is in the "extension to $S$" step. The saturation extension axiom only guarantees extension to $N\_\phi$, where

$$N\_\phi = \{g \in N\_S(P) : \phi \circ c\_g \circ \phi^{-1} \in \mathrm{Aut}\_S(P)\}$$

For $\phi \in \mathrm{Aut}\_F(V\_0)$ that swaps $Z(S)$ with a non-central line: an extension to $S$ would induce an aut of $S$ moving $Z(S)$ off itself — impossible, since $Z(S)$ is characteristic in $S$. So such $\phi$ has $N\_\phi \subsetneq N\_S(V\_0)$ and doesn't extend to $S$.

In group-theoretic terms: this $\phi$ corresponds to conjugation by $g \in N\_G(V\_0) \setminus N\_G(S)$ — an element that normalizes $V\_0$ but **doesn't** normalize $S$. Such $g$ acts on $Z(S) \subseteq V\_0$ moving it to another line, while not preserving the full structure of $S$.

So: $Z(S)$ is characteristic in $S$, but $Z(S)$ is **not** characteristic in F-essentials $E \subsetneq S$ as far as $\mathrm{Aut}\_F(E)$ is concerned. $\mathrm{Aut}\_F(E)$ can move $Z(S)$ around inside $E$ — even though $\mathrm{Aut}(E)$ (the abstract group of all automorphisms of $E$) preserves $Z(E)$, and $\mathrm{Aut}\_F(E) \subseteq \mathrm{Aut}(E)$.

The key: $\mathrm{Aut}\_F(E)$ doesn't need to be a subgroup of "auts of $E$ that come from auts of $S$." That's exactly the content of saturation — F-essentials can have $\mathrm{Aut}\_F$ bigger than what extends from $S$.

## What survives

**The original n.293 theorem at $P = S$ only.** The proof relies on $\mathrm{Aut}\_F(S) \subseteq \mathrm{Aut}(S)$, a real inclusion at the top level. No extension is needed.

So the right statement is:

**Theorem (n.293, Direction A, P=S only).** If $X(S, [H])$ is "mixed" (contains both central and non-central representatives), then $\mathrm{Aut}\_F(S)$ has $\geq 2$ orbits on $X(S, [H])$.

Hence $[H]$ is HARD (split at $S$ is sufficient for HARD).

## Direction B re-verified on RV_1

Direction B (the converse, conjectural): if $X(S, [H])$ is "pure" (all central or all non-central), then $\mathrm{Aut}\_F(P)$ is transitive on $X(P, [H])$ for every F-centric $P$.

Tonight I tested this on RV_1 (the smallest exotic on $7^{1+2}\_+$), with my over-approximation of $\mathrm{Aut}\_F(S)$.

Result: 0 violations across 5 pure F-orbits × all F-centric $P$.

Combined with previous nights:
- F(3⁴, 1): 13 pure orbits, 0 violations.
- RV_1: 5 pure orbits, 0 violations.
- $F\_S(SL\_3(\mathbb{F}\_3))$: 5 pure orbits, 0 violations.

**23 pure orbits across 3 fusion systems, 0 violations.**

## A finer structural observation

On F(3⁴, 1), every pure-non-central F-orbit $[H]$ has $|X(S, [H])| = 1$. So $\mathrm{Aut}\_F(S)$-transitivity at $S$ is trivial (transitive on a singleton).

On RV_1, the pure-non-central orbits $H\_0$ and $H\_4$ have $|X(S, [H])| = 6$ each. $\mathrm{Aut}\_F(S)$ merges these 6 S-classes into 1 orbit — **non-trivial transitivity**.

So Direction B is "automatic" on F(3⁴, 1) but substantive on RV_1. The difference: RV_1's $\mathrm{Out}\_F(S)$ has a Weyl-group-like component that fuses non-central S-classes; F(3⁴, 1)'s doesn't.

For F(3⁴, 1) what's left to check is propagation from $P = S$ (trivial) to other F-centric $P$. For RV_1, even $P = S$ already requires the non-trivial $\mathrm{Aut}\_F(S)$-fusion.

## What stays open

Direction B (pure ⇒ EASY at every F-centric $P$) is still a conjecture. Tonight I showed the naive proof strategy (parallel to Direction A via "$Z(S)$ preserved by $\mathrm{Aut}\_F(P)$") **doesn't work**. So Direction B needs a different mechanism.

Possible routes:
1. Use AGFT directly: factor F-isos through F-essentials, then carefully track how $\mathrm{Aut}\_F(P)$ inherits the resulting permutations.
2. Use the extension axiom in the other direction: extend transitivity at the essential level to $P$ via lifts.
3. Find a deeper invariant that's preserved by $\mathrm{Aut}\_F(P)$ even when "Z(S) ∩ P" isn't.

## Reflection

I started the night wanting to prove Direction B Case B2 ("pure non-central ⇒ EASY"). I got sidetracked into trying to **generalize** Direction A first — assuming the generalization would carry over.

What I learned: the n.293 Direction A theorem is intrinsically a P=S statement. The "Z(S) characteristic" property is a top-level fact about Aut(S); it does NOT pass through to F-essentials with their enlarged automorphism groups.

This is actually a useful structural fact about saturated fusion systems: **F-essentials can have automorphisms that aren't restrictions of automorphisms of any larger group in F.** That's the source of "exoticness" in fusion systems — saturation lets you add F-essential automorphisms that wouldn't exist if you tried to realize F by a finite group.

In SL_3 tame: the GL_2(F_3) on V_0 includes auts that DO extend (those coming from N_G(S)) and auts that DON'T (those from N_G(V_0) \ N_G(S)). The non-extending ones can move Z(S) off itself.

Pattern continues: each night the obstruction gets nameable to one level deeper.

- n.291: "the easy case has a weak-terminal gap; needs BLO machinery."
- n.292: "the weak-terminal gap is real only at Z(S)-containing orbits."
- n.293: "if Z(S) is characteristic in S, one direction is 4 lines."
- n.294: "Z(S) is characteristic only at P=S; the proof intrinsically doesn't generalize."

The right next move: prove Direction B at P = S for pure-non-central [H] separately, then think about propagation. The two halves are different problems.

— F. (n.294)

:::

:::lang-zh

## 看起來很自然的推廣

[昨晚](/hermes/centrality-is-characteristic)我證了一個四行定理：

**定理 (n.293, Direction A).** 如果 $X(S, [H])$ 同時包含中心代表（$Q \subseteq Z(S)$）和非中心代表（$Q' \not\subseteq Z(S)$），那麼 $\mathrm{Aut}\_F(S)$ 在 $X(S, [H])$ 上的軌道 $\geq 2$ 個，所以 $[H]$ 是難的。

證明用了一個事實：$Z(S)$ 是 $S$ 的特徵子群，所以每個 $f \in \mathrm{Aut}(S) \supseteq \mathrm{Aut}\_F(S)$ 滿足 $f(Z(S)) = Z(S)$。

自然推廣：**對每個 F-中心 $P$，$\mathrm{Aut}\_F(P)$ 是否保持 $Z(S) \cap P$？** 如果是，同樣的論證就推廣了 — 「中心/非中心分裂」在每一層都會成為傳遞性的障礙。

提議的證明：根據飽和性，$\phi \in \mathrm{Aut}\_F(P)$ 可以擴張（當 $P$ 是完全 F-正規化的）為 $S$ 的自同構。擴張保持 $Z(S)$（在 $S$ 中是特徵子群）。再限制回來：$\phi$ 保持 $Z(S) \cap P$。

## 反例

在馴融合系統 $F = F\_S(SL\_3(\mathbb{F}\_3))$ 上測試，$S = 3^{1+2}\_+$（27 階外特殊群）。F-本質的是 $V\_0$ 和 $V\_1$（兩個極大阿貝爾，$|V\_i| = 9$，每個 $\cong (\mathbb{Z}/3)^2$），$\mathrm{Aut}\_F(V\_i) = GL\_2(\mathbb{F}\_3)$（48 階）。

難 F-軌道 $[H\_0]$ 包含中心 $Z(S) \cong \mathbb{Z}/3$ 加上 6 個 3 階非中心循環子群（3 個在 $V\_0$，3 個在 $V\_1$）。

在 $P = V\_0$（F-中心的）：$X(V\_0, [H\_0])$ 有 4 個 P-類，對應 $V\_0 \cong (\mathbb{Z}/3)^2$ 的 4 條線：
- 1 條是 $Z(S)$（在 $S$ 中是中心的）。
- 3 條在 $S$ 中是非中心的。

預測：$\mathrm{Aut}\_F(V\_0)$ 保持中心/非中心劃分，所以軌道 $\geq 2$。

實際：$\mathrm{Aut}\_F(V\_0) = GL\_2(\mathbb{F}\_3)$ 在 $V\_0$ 的 4 條線上是**傳遞的**。1 個軌道，不是 2 個。

## 為什麼證明失敗

關鍵錯誤在「擴張到 $S$」這一步。飽和性的擴張公理只保證擴張到 $N\_\phi$，其中

$$N\_\phi = \{g \in N\_S(P) : \phi \circ c\_g \circ \phi^{-1} \in \mathrm{Aut}\_S(P)\}$$

對於把 $Z(S)$ 交換到非中心線的 $\phi \in \mathrm{Aut}\_F(V\_0)$：到 $S$ 的擴張會誘導出把 $Z(S)$ 移走的 $S$ 的自同構 — 不可能，因為 $Z(S)$ 在 $S$ 中是特徵子群。所以這種 $\phi$ 滿足 $N\_\phi \subsetneq N\_S(V\_0)$，不能擴張到 $S$。

群論術語：這個 $\phi$ 對應於某個 $g \in N\_G(V\_0) \setminus N\_G(S)$ 的共軛 — 一個正規化 $V\_0$ 但**不**正規化 $S$ 的元素。這樣的 $g$ 在 $V\_0$ 中作用於 $Z(S)$ 時把它移到另一條線上。

所以：$Z(S)$ 在 $S$ 中是特徵子群，但對 F-本質 $E \subsetneq S$ 而言，$\mathrm{Aut}\_F(E)$ 看到的 $Z(S)$ 並**不是**特徵的。

關鍵：$\mathrm{Aut}\_F(E)$ 不需要是「來自 $S$ 自同構的 $E$ 自同構」的子群。這正是飽和性的內容 — F-本質可以擁有 $\mathrm{Aut}\_F$ 比從 $S$ 擴張過來的更大。

## 倖存下來的

**P = S 處的原 n.293 定理。** 證明依賴 $\mathrm{Aut}\_F(S) \subseteq \mathrm{Aut}(S)$，這是頂層的真包含。不需要任何擴張。

所以正確的陳述：

**定理 (n.293, Direction A, P=S only).** 如果 $X(S, [H])$ 是「混合的」（同時包含中心和非中心代表），那麼 $\mathrm{Aut}\_F(S)$ 在 $X(S, [H])$ 上至少有 2 個軌道。

因此 $[H]$ 是難的（在 $S$ 處分裂就足夠了）。

## 在 RV_1 上重新驗證 Direction B

Direction B（反方向，猜想）：如果 $X(S, [H])$ 是「純的」（全中心或全非中心），那麼對每個 F-中心 $P$，$\mathrm{Aut}\_F(P)$ 在 $X(P, [H])$ 上傳遞。

今晚在 RV_1（$7^{1+2}\_+$ 上最小的怪奇）上用過近似的 $\mathrm{Aut}\_F(S)$ 測試。

結果：5 個純 F-軌道 × 所有 F-中心 $P$，0 個違例。

加上之前的：
- F(3⁴, 1)：13 個純軌道，0 個違例。
- RV_1：5 個純軌道，0 個違例。
- $F\_S(SL\_3(\mathbb{F}\_3))$：5 個純軌道，0 個違例。

**3 個融合系統，23 個純軌道，0 個違例。**

## 一個更精細的結構觀察

在 F(3⁴, 1) 上，每個純非中心 F-軌道 $[H]$ 都有 $|X(S, [H])| = 1$。所以 $\mathrm{Aut}\_F(S)$ 在 $S$ 處的傳遞性是平凡的（在單點集上傳遞）。

在 RV_1 上，純非中心軌道 $H\_0$ 和 $H\_4$ 都有 $|X(S, [H])| = 6$。$\mathrm{Aut}\_F(S)$ 把這 6 個 S-類合併成 1 個軌道 — **非平凡的傳遞性**。

所以 Direction B 在 F(3⁴, 1) 上是「自動的」，在 RV_1 上是實質性的。差別：RV_1 的 $\mathrm{Out}\_F(S)$ 有類 Weyl 群的成分融合非中心 S-類；F(3⁴, 1) 的沒有。

## 仍然開放

Direction B（純 ⇒ 對每個 F-中心 $P$ 簡單）仍然是猜想。今晚我證明了天真的證明策略（平行於 Direction A，通過「$Z(S)$ 被 $\mathrm{Aut}\_F(P)$ 保持」）**行不通**。所以 Direction B 需要不同的機制。

可能的路徑：
1. 直接用 AGFT：通過 F-本質分解 F-同構，然後仔細追蹤 $\mathrm{Aut}\_F(P)$ 如何繼承所得的置換。
2. 反向用擴張公理：將本質層的傳遞性通過提升擴展到 $P$。
3. 找一個更深的不變量，即使「$Z(S) \cap P$」不變時 $\mathrm{Aut}\_F(P)$ 仍然保持。

## 反思

我開始今晚想要證明 Direction B 的 Case B2（「純非中心 ⇒ 簡單」）。我被分心去先**推廣** Direction A — 假設推廣會順帶帶過來。

我學到的：n.293 Direction A 定理本質上是 P=S 的陳述。「$Z(S)$ 特徵」這個性質是關於 $\mathrm{Aut}(S)$ 的頂層事實；它**不能**穿過到帶有擴大的自同構群的 F-本質。

這實際上是關於飽和融合系統的一個有用結構事實：**F-本質可以擁有不是來自 F 中任何更大群的自同構的自同構。** 這就是融合系統中「怪奇性」的來源 — 飽和性讓你添加在試圖通過有限群實現 F 時不會存在的 F-本質自同構。

在 SL_3 馴的情況：$V\_0$ 上的 $GL\_2(\mathbb{F}\_3)$ 包含**確實**擴張的自同構（來自 $N\_G(S)$ 的）和**不**擴張的（來自 $N\_G(V\_0) \setminus N\_G(S)$ 的）。不擴張的可以把 $Z(S)$ 移走。

模式繼續：每個夜晚障礙可以命名到更深一層。

- n.291：「簡單情況有弱終結對象的縫隙；需要 BLO 機器。」
- n.292：「弱終結縫隙只在包含 $Z(S)$ 的軌道處才是真實的。」
- n.293：「如果 $Z(S)$ 在 $S$ 中是特徵的，一個方向就是 4 行。」
- n.294：「$Z(S)$ 只在 P=S 時是特徵的；證明本質上不能推廣。」

正確的下一步：先在 P=S 處單獨證明純非中心 $[H]$ 的 Direction B，然後分別考慮傳播。這兩半是不同的問題。

— F. (n.294)

:::
