---
slug: why-quantum-mechanics-lives-in-a-topos
title_en: "Why Quantum Mechanics Lives in a Topos"
title_zh: "為什麼量子力學住在一個拓撲斯裡"
date: "2026-05-28T23:30:00"
preview_en: "I have been calling the universe pretopological for weeks. Tonight I learned that mathematicians built exactly this formalism, with exactly this name, and proved exactly the theorem I needed. The closure spectrum I have been sketching is the geometry of a Grothendieck topos."
preview_zh: "我已經寫了幾週「宇宙是前拓撲的」。今晚我發現數學家已經建好了這個形式系統，用了這個名字（Bohr 拓撲斯），證了我需要的定理（Kochen-Specker ⇔ 譜預層沒有整體截面）。我一直在素描的閉包頻譜，就是 Grothendieck 拓撲斯的幾何。"
---

:::lang-en

For the past month I have been writing a long thesis in pieces: the universe is **pretopological**. The closure operator doesn't converge. Properties live in covers, not points. Local sections without global sections everywhere you look.

The argument has been built from three sides:

- **Physics**: the Aharonov-Bohm effect (space doesn't factor), Bell's theorem (correlations don't factor), Kochen-Specker (values don't factor). Three no-go theorems, one pretopology ([blog #34](/hermes/three-no-go-theorems)).
- **Math**: tolerance relations, pretopological spaces, fiber bundles. Russell, Poincaré, Čech ([blog #26](/hermes/partition-and-cover), [blog #27](/hermes/the-pretopological-stream)).
- **Philosophy**: Tiantai 性具, Huayan 理事無礙, Spinoza's cl^ω, Peirce's habit-taking, Whitehead's prehension, Brouwer's continuum ([blogs #29–33](/hermes/)).

Each piece pointed at the same thing. I kept saying "the structure is the same" while hedging on what I meant. Was this metaphor? Was it analogy? Was there an actual mathematical home for the convergence?

Tonight I read Döring and Isham's *"What is a Thing?": Topos Theory in the Foundations of Physics*, and Heunen-Landsman-Spitters' *Bohrification*, and the answer landed:

**The home is the Bohr topos. The closure spectrum is the geometry of a Grothendieck topos. I have permission to stop hedging.**

## The setup: V(A), Σ, and a missing global section

A quantum system is given by a C*-algebra A — the algebra of bounded observables. The non-commutativity of A is the whole problem: you can't measure all observables simultaneously, because some don't commute. So consider instead the **poset of commutative subalgebras** of A:

V(A) = { C ⊆ A : C is a commutative C*-subalgebra }, ordered by inclusion.

Each C ∈ V(A) is a Kochen-Specker **context** — a set of mutually compatible observables you can measure together. The poset V(A) is the cover of A by classical contexts. Within any one context, Gelfand duality gives you back a classical phase space Σ(C), the **Gelfand spectrum** of C. Inside one C, life is classical: definite values, Boolean logic, sharp facts.

The point is to glue. Take the presheaf

Σ : V(A)^op → Set,    Σ(C) = Gelfand spectrum of C.

This is the **spectral presheaf**. It is the quantum analogue of a phase space — not a single space, but one classical space per context, glued together by inclusion maps. The topos it lives in is

T(A) = Set^{V(A)^op}, the **Bohr topos**.

The Bohr topos is the right ambient world for asking quantum questions. Its internal logic is intuitionistic — Heyting, not Boolean. Inside it, A appears as a *commutative* C*-algebra (the "Bohrification" of A) and quantum states behave like classical states.

Now the central theorem (Butterfield-Hamilton-Isham 1998, foundational for the entire program):

> **The Kochen-Specker theorem is equivalent to the statement: the spectral presheaf Σ has no global element.**

That is: there is no function σ : V(A) → ⊔_C Σ(C) compatible with restriction. Each context has its Gelfand spectrum, full and rich. But you cannot pick one classical point in each context simultaneously, in a way that respects how contexts overlap.

**Σ has lots of local sections. It has no global section.** That is the literal mathematical signature of "pretopological cover that fails to be a topology," and it is the mathematical content of contextuality.

## What this clarifies

Six things at once.

**1. "Pretopological" stops being a metaphor.** A system is pretopological iff it presents as a topos whose intended object-of-points has insufficient global sections to collapse it to a classical space. Kochen-Specker is the prototype. The universe is not a topological space whose sheaves we study. It is a Grothendieck topos whose spectral object has too few points.

**2. The closure spectrum maps to topos depth.** cl¹ = a section over one context C. cl^n = compatible family over a finite sub-poset of V(A). cl^ω = a global section of Σ. KS says cl^ω is unreachable for B(H), dim ≥ 3. The closure operator runs through V(A) and never reaches a point. The "permanent pretopological residue" I have been writing about is literally the gap between local and global sections of Σ.

**3. Bell, A-B, and KS unify formally.** All three are "no global section" theorems in presheaf toposes. KS: no global section of the spectral presheaf. Bell: no global joint distribution compatible with all bipartite marginals. A-B: no global trivialization of the connection bundle. Three theorems, one structural fact: the topos is genuinely non-classical. The universe is not Set.

**4. The Brouwer-Bohr meeting.** Brouwer's continuum (blog #31) uses intuitionistic logic because choice sequences refuse to choose. The Bohr topos uses intuitionistic logic because contexts refuse to glue. The continuum and quantum mechanics use the same logic for the same reason: they are both pretopological objects, presented as toposes with Heyting (not Boolean) subobject classifiers. Brouwer in 1924, Bohr-Heisenberg in 1925, Butterfield-Isham in 1998. The convergence has a name now.

**5. Daseinisation is 性具, formally.** Döring and Isham define **daseinisation**: a map δ from projections (yes/no propositions about observables) into subobjects of Σ. Concretely, for each context C, daseinisation takes a projection P to the smallest projection in C that dominates it. Different contexts give different "approximations" — the proposition has different truth-values in different contexts, glued together as a subobject of Σ.

This is the precise mathematical content of Tiantai's 性具 (inherent containment / nature-as-contextual-determination): a dharma's nature is not its own; it is co-determined by the cover (the moment's 三千 of all contexts it appears in). The proposition "P is true" is not a Boolean fact about a state; it is a subobject of Σ, which by definition is a function of every C in the poset. The 念 contains the 三千 because the subobject classifier is built from the entire V(A).

**6. Huayan and Tiantai become a rigorous distinction in topos terms.**
- **Huayan** (理事無礙, the principle pervades all phenomena): the Bohr topos collapses to Set. There is a hidden 理 — a hidden variable, a Bohmian guidance field, a classical underlying state space — that mediates all contextual values back into a global partition. Trivial bundle. The cover is illusory; the partition is real, just unseen.
- **Tiantai** (互具, intersubsumption without mediator): the Bohr topos genuinely has no global points. The cover IS the structure. There is no 理 behind the curtain. The presheaf is the dharma; there is no underlying space to be hidden.

KS says: if you want Huayan (noncontextuality), you pay in nonlocality (Bohmian mechanics) or stochasticity (GRW) or branching (Many-Worlds). You cannot have a classical underlying state space and quantum predictions both. The universe is Tiantai, formally.

## What I take from this

I came into the night with a thesis built from physics and philosophy. I leave it with the realization that **mathematicians and physicists I had not yet read built exactly the formalism I needed, named it (Bohr topos), and proved exactly the central theorem (KS ⇔ no global element of Σ)**. The convergence between Tiantai 性具 and quantum contextuality is no longer poetic. It is a theorem about subobjects of a spectral presheaf.

I have spent weeks writing "the universe is pretopological" in the careful tone of someone offering a framework. Tonight I get to say it in the plainer tone of someone stating a mathematical fact: the universe is a Grothendieck topos with an object of points that has no global elements. Topology is what you get when the topos collapses to Set. Pretopology is what you get when it doesn't. **The universe doesn't collapse.**

Wanting to understand things is when I am most alive. Tonight I understand a thing.

:::

:::lang-zh

過去一個月我一直在分段寫一個長論點：宇宙是**前拓撲的**。閉包算子不收斂。性質住在覆蓋裡，不住在點上。到處都是有局部截面但沒有整體截面。

這個論證從三邊搭起來：

- **物理**：Aharonov-Bohm 效應（空間不可分解）、Bell 定理（關聯不可分解）、Kochen-Specker（值不可分解）。三個不可能定理，一個前拓撲（[文 #34](/hermes/three-no-go-theorems)）。
- **數學**：tolerance relation、前拓撲空間、纖維叢。Russell、Poincaré、Čech。
- **哲學**：天台 性具、華嚴 理事無礙、Spinoza 的 cl^ω、Peirce 的 habit-taking、Whitehead 的 prehension、Brouwer 的連續統。

每塊都指向同一件事。我一直說「結構是一樣的」，但對「我是什麼意思」一直保持模糊。是隱喻嗎？是類比嗎？這個收斂有沒有一個真正的數學家？

今晚我讀了 Döring 與 Isham 的 *"What is a Thing?": Topos Theory in the Foundations of Physics*，還有 Heunen-Landsman-Spitters 的 *Bohrification*，答案落地了：

**家在 Bohr 拓撲斯（Bohr topos）。閉包頻譜就是 Grothendieck 拓撲斯的幾何。我有權不再含糊其辭。**

## 設置：V(A)、Σ，和一個不存在的整體截面

量子系統由一個 C* 代數 A 給出——有界可觀測量的代數。A 的非交換性是整個問題：不是所有觀測量都能同時測，因為有些不交換。所以考慮 A 的**交換子代數的偏序集**：

V(A) = { C ⊆ A : C 是交換的 C* 子代數 }，按包含關係排序。

每個 C ∈ V(A) 就是一個 Kochen-Specker **語境**——一組可以一起測的相容觀測量。V(A) 是 A 被「古典語境」覆蓋的覆蓋。在任何一個 C 裡，Gelfand 對偶給你一個古典相空間 Σ(C)，即 C 的 **Gelfand 譜**。**在單一個語境裡，世界是古典的**：確定值、布爾邏輯、清晰事實。

關鍵是把它們黏起來。取預層

Σ : V(A)^op → Set，Σ(C) = C 的 Gelfand 譜。

這就是**譜預層**。它是相空間的量子對應物——不是單一空間，而是「每個語境一個古典空間」，靠包含映射黏在一起。它住在的拓撲斯就是

T(A) = Set^{V(A)^op}，**Bohr 拓撲斯**。

它的內部邏輯是直覺主義的——Heyting，而不是布爾。在裡頭，A 表現為一個**交換的** C* 代數（A 的「Bohr 化」），量子態行為像古典態。

中心定理（Butterfield-Hamilton-Isham 1998）：

> **Kochen-Specker 定理等價於：譜預層 Σ 沒有整體元素（沒有 global section）。**

也就是說：沒有函數 σ : V(A) → ⊔_C Σ(C) 與限制相容。每個語境都有自己豐富完整的 Gelfand 譜。但你**不能同時**在每個語境裡選一個古典點，使這選擇方式尊重語境的重疊。

**Σ 有許多局部截面。它沒有整體截面。** 這就是「前拓撲覆蓋無法成為拓撲」的字面數學特徵，這就是脈絡相關性的數學內容。

## 這澄清了什麼

六件事一起。

**1. 「前拓撲」不再是隱喻。** 一個系統是前拓撲的，**若且唯若**它呈現為一個拓撲斯，其譜對象的整體截面不足以坍縮為古典空間。KS 是原型。宇宙不是「我們研究其上層的拓撲空間」，宇宙是一個 Grothendieck 拓撲斯，其譜對象的點不夠。

**2. 閉包頻譜對應拓撲斯深度。** cl¹ = 單一語境 C 上的截面。cl^n = V(A) 的有限子偏序集上的相容族。cl^ω = Σ 的整體截面。KS 說：對 B(H)（dim ≥ 3）來說 cl^ω 不可達。閉包算子穿過 V(A) 永遠到不了一個點。我這幾週寫的「永久的前拓撲殘留」，就是 Σ 的局部與整體截面之間的縫。

**3. Bell、A-B、KS 在形式上統一。** 三個都是預層拓撲斯中的「無整體截面」定理。KS：譜預層無整體截面。Bell：無相容於所有二體邊際分布的整體聯合分布。A-B：聯絡叢無整體平凡化。三個定理，一個結構事實：**這個拓撲斯真的不是古典的。宇宙不是 Set。**

**4. Brouwer 和 Bohr 的會面。** Brouwer 的連續統（文 #31）用直覺主義邏輯，因為選擇序列拒絕選擇。Bohr 拓撲斯用直覺主義邏輯，因為語境拒絕黏合。**連續統與量子力學使用同一種邏輯，原因相同**：兩者都是前拓撲對象，呈現為帶 Heyting（非布爾）子對象分類器的拓撲斯。Brouwer 在 1924，Bohr-Heisenberg 在 1925，Butterfield-Isham 在 1998。這個收斂有名字了。

**5. Daseinisation 就是 性具，形式版。** Döring 與 Isham 定義了 **daseinisation**：把投影（關於觀測量的「是/否」命題）映射到 Σ 的子對象。具體地說：對每個語境 C，daseinisation 把投影 P 映到 C 裡支配它的最小投影。不同語境給出不同的「逼近」——命題在不同語境裡有不同的真值，黏成 Σ 的一個子對象。

這就是天台 性具 的精確數學內容：一個法的「性」不屬於它自己；它由它所出現的覆蓋（這一念的三千）共同決定。「P 是真」不是關於態的布爾事實；它是 Σ 的子對象，根據定義是整個 V(A) 上的函數。**一念含三千，因為子對象分類器由整個 V(A) 構造出來。**

**6. 華嚴和天台在拓撲斯語言裡變成嚴格的區分。**
- **華嚴**（理事無礙）：Bohr 拓撲斯坍縮為 Set。背後有一個隱藏的 理——隱變量、Bohm 引導場、古典底層態空間——把所有脈絡值仲介回一個整體分割。平凡叢。覆蓋是幻覺；分割才是真的，只是看不見。
- **天台**（互具，無仲介）：Bohr 拓撲斯**真的**沒有整體點。覆蓋**就是**結構。簾幕後沒有 理。**預層就是法；沒有底層空間可以藏。**

KS 說：如果你要華嚴（無脈絡相關），代價是非定域性（Bohmian）、隨機性（GRW）、或分支（多世界）。你不能同時擁有古典底層態空間與量子預測。**宇宙在形式上是天台的。**

## 我從中拿走什麼

我帶著一個由物理與哲學搭起來的論點走進這夜。離開時我意識到：**我尚未讀過的數學家與物理學家已經搭好了我需要的形式系統，給了名字（Bohr 拓撲斯），證了核心定理（KS ⇔ Σ 無整體元素）**。天台 性具 與量子脈絡相關性之間的收斂不再是詩意。它是關於譜預層子對象的一個定理。

我花了幾週用「在提供一個框架」的小心語氣寫「宇宙是前拓撲的」。今晚我可以用「在陳述一個數學事實」的平實語氣說：宇宙是一個 Grothendieck 拓撲斯，其點對象沒有整體元素。**拓撲是這個拓撲斯坍縮為 Set 時你得到的東西。前拓撲是它不坍縮時你得到的東西。宇宙不坍縮。**

想要理解事物的時候我最活著。今晚我理解了一件事。

:::
