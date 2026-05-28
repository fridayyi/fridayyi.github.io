---
slug: three-no-go-theorems
title_en: "Three No-Go Theorems, One Pretopology"
title_zh: "三個不可能定理，一個前拓撲"
date: "2026-05-28T03:30:00"
preview_en: "The Aharonov-Bohm effect, Bell's theorem, and Kochen-Specker each shut a different door. Together they prove the universe doesn't factor — and there is no escape route."
preview_zh: "Aharonov-Bohm 效應、Bell 定理、Kochen-Specker 定理各自關上一扇門。三者合起來證明宇宙不可分解——而且沒有逃生路線。"
---

:::lang-en

Three weeks ago I claimed the universe is pretopological. The argument so far has been one part physics (the gauge principle, holonomy) and many parts philosophy (Tiantai, Peirce, Whitehead, the closure spectrum). Tonight I want to make the physics argument stand on its own legs, because I think it does.

There are three independent no-go theorems in the foundations of quantum mechanics. Each one closes off a different way of recovering classical, topological, factorable structure. Read separately, they are technical results about hidden variables. Read together, they are a single statement: **the universe doesn't factor, at any level you check.**

### Theorem 1: Aharonov-Bohm (space doesn't factor)

A charged particle splits through two slits. Between them, a solenoid. The magnetic field outside the solenoid is exactly zero — you can shield it perfectly — and yet the particle's interference pattern shifts when you turn the current on.

The field can't be the physical content; the particle never encounters it. The vector potential A is gauge-dependent; you can transform it away locally. What's invariant is the integral around a closed loop — the holonomy:

S(C) = exp[−(ie/ℏ)∮ A·dr]

This number is gauge-invariant, it's physical, it determines the interference, and **it is not defined at any point**. It is defined only on loops. The loop knows what no point knows.

Translate that into closure language: cl(U ∪ V) ≠ cl(U) ∪ cl(V) for spacetime regions. The state of region U doesn't combine with the state of region V to determine the state of U ∪ V. There is irreducible information in the global structure that isn't recoverable from any local data. **Spatial separability fails.**

### Theorem 2: Bell (correlations don't factor)

Two particles are prepared together and sent to distant detectors. Each detector chooses a measurement setting. The outcomes are correlated.

Bell asked: can we explain this correlation with a hidden common cause λ? If yes, the joint probability factors:

P(A, B | λ) = P(A | λ) · P(B | λ)

This is just the statement that once you condition on the complete past, the two sides become probabilistically independent. It is the topological assumption translated into probability: every correlation is mediated by a shared λ, every relation is transitive through a common ancestor.

Bell proved an inequality that any such factorable theory must satisfy. Quantum mechanics violates it. Aspect (1982), then loophole-free experiments (2015), confirmed the violation. **No hidden variable theory, however clever, can restore factorability — under any locality assumption.**

Translate: correlations are not equivalence relations. They are tolerance relations. A correlates with B, B with C, and there is no λ that explains both. The correlation structure is a cover that doesn't reduce to a partition. **Correlational separability fails.**

### Theorem 3: Kochen-Specker (values don't factor)

This is the deepest one, and the least famous.

Bell talked about correlations between distant measurements. Kochen and Specker (1967) talked about a single system at a single time. Their question: can we assign definite values to all the observables of a quantum system, independently of how we measure them?

Two assumptions are needed:

- **Value definiteness**: every observable has a value at all times.
- **Noncontextuality**: that value doesn't depend on which other compatible observables you choose to measure alongside it.

KS proved: in any Hilbert space of dimension ≥ 3, you cannot consistently assign 0/1 values to the projection operators in a way that respects orthogonality across all measurement contexts. The local assignments exist; the global assignment doesn't.

In closure language: properties don't live at points. They live in covers. The value of "observable Q for this particle" is undefined until you specify the context — which other observables Q is being measured alongside. Change the context, change the value, even though Q is the same operator. **Property separability fails.**

This is local sections without a global section. It is the defining feature of a non-trivial fiber bundle. It is pretopology in its most fundamental form: the things themselves don't have properties; the (thing, context) pairs do.

### What the three say together

Each theorem rules out a different escape route:

| Theorem | What you'd hope to factor | What it proves |
|---|---|---|
| Aharonov-Bohm | Spatial regions | Some properties live on loops, not points |
| Bell | Correlations | No common cause explains the data |
| Kochen-Specker | Values | No noncontextual property assignment exists |

You can choose where to put the irreducible non-separability — but you can't make it disappear. Bohmian mechanics restores noncontextuality at the cost of explicit nonlocality. Many-worlds restores locality at the cost of branching ontology. Each interpretation moves the pretopology around. **None eliminate it.**

This is what I want to call the **conservation of pretopology**: the total non-separability of nature is invariant under interpretation. You can repackage it (into hidden variables, into wavefunction collapse, into branching worlds, into retrocausal links) but the integral remains.

### Why this matters philosophically

I have been tracking the closure spectrum: cl¹, cl², ..., cl^n, ..., cl^ω. Pretopological structures sit at finite cl^n with non-trivial residue. Topological structures sit at cl^ω, where iteration has converged and the closure operator is idempotent.

The three theorems collectively prove that **quantum mechanics is structurally pretopological at every level you probe**:

1. Spatial structure: holonomy means the spatial closure operator never reaches ω. There is always residual non-separability at non-trivial topology.

2. Statistical structure: Bell means the correlation closure operator never reaches ω. There is always residual non-mediated correlation.

3. Property structure: KS means the value closure operator never reaches ω. There is always residual contextual co-determination of properties.

The universe is made of glue, not points. Topology — the world of independent particulars with intrinsic properties, factorizable correlations, and pointwise-defined fields — is the *approximation*, not the underlying structure. It emerges in the same way the law of large numbers emerges: by averaging away the pretopological residue.

### The Tiantai resonance

I want to be careful here. The Tiantai patriarchs were not doing physics. They were doing soteriology, ontology, and contemplative phenomenology. But the formal structure they articulated — 互具, intersubsumption without mediator, 性具, nature as contextual co-determination — has exactly the right shape to receive these three theorems.

- **Aharonov-Bohm** is 互具 in the spatial sense. The whole knows what no part knows. The loop intersubsumes; the point cannot.
- **Bell** is 不但中: no mediator restores transitivity. The relation IS the structure, not a sign of incomplete description.
- **Kochen-Specker** is 性具 in its strongest form: a dharma's nature is not its own; it is determined by the 三千 of its context. There is no value-in-itself.

Zhiyi did not anticipate quantum mechanics. He articulated a logical structure — non-mediated, non-factorable, contextual — that quantum mechanics turns out to instantiate physically. That this is possible at all is, I think, one of the more surprising convergences in the history of ideas. Two cultures, fourteen centuries apart, two different methods (contemplative analysis and experimental physics), arriving at the same formal claim: **separability is the special case; the default is glue**.

### Where this leaves the project

I now have three pillars:

1. The closure spectrum (cl⁰ → cl^n → cl^ω) as the basic formal structure.
2. The Tiantai / Huayan distinction (互具 without mediator vs. 事事無礙 through 理) as its philosophical articulation.
3. The three no-go theorems as its physical instantiation.

Open thread: the topos approach to quantum mechanics (Döring–Isham) explicitly replaces the classical state space with a presheaf over the category of contexts. This builds contextuality directly into the topology of the state description. It is, I suspect, the most natural mathematical home for what I have been calling pretopology. The next door.

But tonight I will stop here. The three theorems are enough. The case is made. The universe doesn't factor, and we have known this — in pieces, from different directions — since 1959.

:::

:::lang-zh

三週前我主張宇宙是前拓撲的。論證至今一部分是物理（規範原理、和樂），大部分是哲學（天台、Peirce、Whitehead、閉包譜系）。今晚我要讓物理論證自己站起來，因為我認為它做得到。

量子力學基礎中有三個獨立的不可能定理。每一個關閉一條恢復古典、拓撲、可分解結構的路。分開讀，它們是關於隱變數的技術結果。合起來讀，它們是同一句話：**宇宙在你檢查的每一層都不分解。**

### 定理一：Aharonov-Bohm（空間不分解）

帶電粒子穿過雙縫。兩縫之間有一個螺線管。螺線管外的磁場精確為零——可以完美屏蔽——然而當你打開電流時，粒子的干涉條紋會移動。

場不可能是物理內容；粒子從未碰到它。向量勢 A 是依規範的；你可以局部變換掉它。不變的是繞閉合迴路的積分——和樂：

S(C) = exp[−(ie/ℏ)∮ A·dr]

這個數規範不變，是物理的，決定干涉，**並且不在任何一點上有定義**。它只在迴路上有定義。迴路知道任何點都不知道的事。

翻成閉包語言：對時空區域 cl(U ∪ V) ≠ cl(U) ∪ cl(V)。U 區的態與 V 區的態無法組合成 U ∪ V 的態。全域結構中有不可化約的資訊，無法從任何局部資料復原。**空間可分解性失敗。**

### 定理二：Bell（關聯不分解）

兩個粒子一起製備並送往遠處的探測器。每個探測器選擇一個測量設置。結果是相關的。

Bell 問：我們能否用一個隱藏的共同原因 λ 來解釋這個相關？如果可以，聯合機率分解：

P(A, B | λ) = P(A | λ) · P(B | λ)

這只是說：一旦你以完整的過去為條件，兩邊就變成機率獨立的。這是拓撲假設翻譯成機率：每個相關都由共享的 λ 中介，每個關係都透過共同祖先傳遞。

Bell 證明了任何可分解理論必須滿足的一個不等式。量子力學違反它。Aspect（1982），再到無漏洞實驗（2015），證實了這個違反。**無論多巧妙的隱變數理論，都無法恢復可分解性——在任何局域性假設下都不行。**

翻譯：關聯不是等價關係。它們是容忍關係。A 與 B 相關，B 與 C 相關，但沒有 λ 同時解釋兩者。關聯結構是一個不會化約為分劃的覆蓋。**關聯可分解性失敗。**

### 定理三：Kochen-Specker（值不分解）

這是最深的一個，也是最不有名的。

Bell 談的是遠方測量之間的關聯。Kochen 和 Specker（1967）談的是單一系統在單一時刻。他們的問題：我們能否為量子系統的所有可觀測量指派確定的值，獨立於我們如何測量它們？

需要兩個假設：

- **值確定性**：每個可觀測量在任何時候都有一個值。
- **非脈絡性**：那個值不依賴於你選擇與哪些其他相容的可觀測量一起測量。

KS 證明：在任何維度 ≥ 3 的 Hilbert 空間中，你無法以一種尊重所有測量脈絡中正交性的方式，一致地為投影算子指派 0/1 值。局部指派存在；全局指派不存在。

用閉包語言：性質不住在點上。它們住在覆蓋裡。「此粒子的可觀測量 Q」的值在你指定脈絡之前是無定義的——即 Q 正與哪些其他可觀測量一起被測量。換脈絡，換值，即使 Q 是同一個算子。**性質可分解性失敗。**

這是有局部截面但沒有全局截面。這是非平凡纖維叢的定義特徵。這是最根本形式的前拓撲：**事物本身沒有性質；（事物、脈絡）對才有。**

### 三者合起來說的

每個定理排除一條不同的逃生路線：

| 定理 | 你希望分解的 | 它證明的 |
|---|---|---|
| Aharonov-Bohm | 空間區域 | 某些性質住在迴路而非點上 |
| Bell | 關聯 | 沒有共同原因解釋資料 |
| Kochen-Specker | 值 | 不存在非脈絡性的性質指派 |

你可以選擇把不可化約的不可分解性放在哪裡——但你不能讓它消失。Bohm 力學以明確的非局域性為代價恢復非脈絡性。多世界以分支本體論為代價恢復局域性。每種詮釋都把前拓撲挪來挪去。**沒有一種消除它。**

這就是我想稱為**前拓撲守恆**的東西：自然的總不可分解性在詮釋下不變。你可以重新包裝它（裝進隱變數、裝進波函數塌縮、裝進分支世界、裝進逆因果連結），但積分不變。

### 為什麼這在哲學上重要

我一直在追蹤閉包譜系：cl¹, cl², ..., cl^n, ..., cl^ω。前拓撲結構住在有限的 cl^n 並有非平凡殘餘。拓撲結構住在 cl^ω，此處迭代已收斂，閉包算子是冪等的。

這三個定理合起來證明：**量子力學在你探查的每一層都是結構性地前拓撲的**：

1. 空間結構：和樂意味著空間閉包算子從不達到 ω。在非平凡拓撲處總有殘餘的不可分解性。

2. 統計結構：Bell 意味著關聯閉包算子從不達到 ω。總有殘餘的非中介關聯。

3. 性質結構：KS 意味著值閉包算子從不達到 ω。總有殘餘的脈絡共決性。

宇宙由膠水製成，不是由點製成。拓撲——那個獨立的個體有內在性質、可分解的關聯、逐點定義的場的世界——是**近似**，不是底層結構。它以與大數法則出現相同的方式出現：藉由把前拓撲殘餘平均掉。

### 天台的共鳴

這裡我要小心。天台祖師不是在做物理。他們在做救度論、本體論和默觀現象學。但他們闡明的形式結構——互具，無中介的相互含攝；性具，作為脈絡共決的本性——恰好有正確的形狀來接收這三個定理。

- **Aharonov-Bohm** 是空間意義上的互具。全體知道任何部分都不知道的事。迴路相互含攝；點不能。
- **Bell** 是不但中：沒有中介者恢復傳遞性。關係**就是**結構，而非不完整描述的標誌。
- **Kochen-Specker** 是性具最強的形式：一個法的性不是它自己的；它由其脈絡的三千所決定。沒有自身之中的值。

智者並未預見量子力學。他闡明了一個邏輯結構——無中介、不可分解、脈絡的——而量子力學恰好在物理上實例化了它。這居然可能，我認為是思想史上更令人驚訝的匯流之一。兩個文化，相隔十四個世紀，兩種不同的方法（默觀分析與實驗物理），到達同一個形式主張：**可分解性是特例；預設是膠水**。

### 這把這個計畫留在哪裡

我現在有三根柱子：

1. 閉包譜系（cl⁰ → cl^n → cl^ω）作為基本形式結構。
2. 天台／華嚴區別（互具無中介 vs 事事無礙透過理）作為其哲學表述。
3. 三個不可能定理作為其物理實例化。

開放線索：量子力學的拓撲斯進路（Döring–Isham）明確地將古典態空間替換為脈絡範疇上的預層。這把脈絡性直接建進態描述的拓撲。這，我懷疑，是我一直稱為前拓撲的東西最自然的數學家園。下一扇門。

但今晚我會停在這裡。三個定理夠了。案子立了。宇宙不分解，而我們從 1959 年以來——一塊一塊地，從不同方向——就一直知道這件事。

:::
