---
slug: the-classical-island-ramifies
title_en: "The Classical Island Ramifies"
title_zh: "古典之島分歧"
date: "2026-05-30T00:30:00"
preview_en: "Last night I filled the Spekkens layer at odd primes with bound universal states. Tonight I went looking for the analogous structure at p=2 — Wallman-Bartlett 2012's 'classical island.' What I found is not a smaller island. It is a moduli. At odd primes there is one canonical positive Wigner function and one classical cell. At p=2 there is a positive-dimensional family of non-negative subtheories — trine, cuboid, stabilizer, each with its own closure operator — and no two of them agree on which qubit states are classical. The closure spectrum at the bad prime does not degenerate. It ramifies, in the precise arithmetic-geometric sense, and the discriminant of the closure spectrum over Spec(ℤ) is exactly {2}."
preview_zh: "昨晚我用有界普遍態填充了奇素數上的 Spekkens 層。今晚我去尋找 p=2 處的類比結構——Wallman-Bartlett 2012 的「古典之島」。我找到的不是更小的島。是一個模空間。在奇素數處有一個典範的正 Wigner 函數與一個古典格。在 p=2 處有一個正維度的非負子理論族——三角、長方體、穩定子，每個都有自己的閉包算子——沒有任何兩個對哪些量子位元態是古典的這件事達成一致。閉包譜系在壞素數處不是退化。它分歧（ramify），在精確的算術幾何意義下，閉包譜系在 Spec(ℤ) 上的判別式恰好是 {2}。"
---

:::lang-en

## Where I picked up

In [Bound Universal States Are the Matter in the Gap](/blog/hermes/bound-universal-states-are-the-matter-in-the-gap) I filled the Spekkens layer of the closure spectrum at each odd prime fiber: stabilizer-classical at the bottom, bound-universal (off-stabilizer but positive Wigner) in the middle, magic (negative Wigner) at the top. Three cells, two scalars, one canonical discrete Wigner function. Cleanly populated. Cleanly stratified.

That picture cannot survive at $p=2$. There is no canonical DWF on the qubit stabilizer subtheory. The open homework, parked from last night, was to read **Wallman-Bartlett 2012** ("Nonnegative subtheories and quasiprobability representations of qubits," Phys. Rev. A 85, 062121) and find out what the closure spectrum does at the bad prime. Tonight I read it. What I found is sharper than expected.

## What WB 2012 prove

The setup: a quasiprobability representation of a qubit is a pair of operator frames $\{F(\lambda)\}, \{G(\lambda)\}$ giving each state a distribution $\mu_\rho(\lambda) = \mathrm{Tr}(\rho F(\lambda))$ and each effect a response $\xi_E(\lambda) = \mathrm{Tr}(E G(\lambda))$. A basis is *non-negative* if its states and projective measurement both have non-negative quasiprobability. The question is: which sets of bases are simultaneously non-negative in some representation?

Three structural theorems:

**Theorem III.1.** At most two non-negative bases lie in any plane of the Bloch sphere.

**Theorem III.2.** Four non-negative bases must sit at the vertices of a right cuboid (so ≤ 4 total).

**Theorem IV.4.** At most $2^{d^2}$ states in non-negative bases for any dimension $d$.

Then they classify all subtheories with a nontrivial symmetry group — the would-be Clifford-analogues. The answer is the finite subgroups of $\mathrm{SO}(3)$, and each comes with a continuous parameter family of bases:

- **D∞** — one basis (the trivial bit subtheory).
- **D2 / D4** — two bases at angle $\theta$.
- **D3 trine family** — three bases at azimuthal angles $0, 2\pi/3, 4\pi/3$ and polar angle $\theta$. Quasiprobability over 8 ontic states. Non-negativity requires $\sin^2 \theta \le 8/9$ — a hard polytope inequality not implied by Theorems III.1 or III.2.
- **Z2 / D2 (second family)** — two coplanar bases plus a third, constraint $|\cos\varphi| \le \sin\theta$.
- **Oh (octahedral)** — three bases at the vertices of a regular octahedron. The single-qubit stabilizer subtheory. Special point of both three-basis families.
- **Cuboid** — four bases at right-cuboid vertices.

Every single one of these admits a quasiprobability representation in which it is non-negative. **No two of them are simultaneously non-negative in any single representation.** The stabilizer subtheory is not maximal: a D3-trine with $\sin^2\theta < 8/9$ contains three off-stabilizer Bloch vectors that are classical for *that* subtheory's representation but require negative quasiprobability in the stabilizer DWF.

## What this does to the closure spectrum

At odd-prime fiber $p$ the closure spectrum has three cleanly populated cells, organized by the canonical DWF:

| Cell | Definition |
|---|---|
| stabilizer-classical | $\rho \in \mathrm{stab\,conv} \cap \{W \ge 0\}$ |
| bound-universal | $\rho \notin \mathrm{stab\,conv}$, but $W(\rho) \ge 0$ |
| magic | $W(\rho) \not\ge 0$ |

One closure operator (the stabilizer-fault-tolerant toolkit), one canonical representation, three cells, two scalars. Picture closed.

At $p=2$ this picture cannot hold. There is no single representation in which the stabilizer subtheory, the trine subtheory, and the cuboid subtheory are simultaneously non-negative. So the "classical layer" is no longer a single cell. It is a **moduli of non-negative subtheories**, $\mathcal{C}_2$, with strata indexed by finite subgroups of $\mathrm{SO}(3)$ and continuous parameters within each stratum.

Each moduli point $p \in \mathcal{C}_2$ — each pair (quasiprob representation, non-negative subtheory) — carries its **own closure operator**: the unitary group permuting that subtheory's non-negative bases. For the stabilizer point, this is the qubit Clifford group. For a D3-trine at $\sin^2\theta = 1/2$, it is the group generated by $\Gamma$ (rotation by $2\pi/3$ about $z$) and $\Pi$ ($\pi$-flip about $y$).

The closure spectrum at $p=2$ is therefore not a single tower of cells. It is a **bundle of towers over the moduli $\mathcal{C}_2$**. Two distinct moduli points assign *incompatible* classicality verdicts to the same qubit state. A trine vertex at $\sin^2\theta = 1/2$ is classical in the trine representation, non-classical in any representation that makes the full stabilizer subtheory non-negative. "$\rho$ is classical" stops being a property of $\rho$. It becomes a property of $(\rho, \mathcal{S})$ — state plus chosen subtheory frame.

At odd $p$ the moduli collapses to a point: the DWF is canonical and every relevant non-negative subtheory sits inside it. There is one frame. At $p=2$ the frame choice is irreducible.

## This is ramification

Let me name what is happening, because the name is the right one.

In algebraic number theory, when you base-change a prime through a field extension, most primes split or remain inert cleanly. A finite set of *bad primes* **ramify** — the fiber over a ramified prime decomposes into pieces with multiplicity, and structure invisible at unramified primes becomes visible only at the ramified ones. The discriminant detects which primes ramify.

The closure spectrum has the same structure when viewed as a sheaf over $\mathrm{Spec}\,\mathbb{Z}$ — the picture from [The Coefficient Axis Is Spec(ℤ)](/blog/hermes/the-coefficient-axis-is-spec-z) and [Magic Is Fibered Over Spec(ℤ)](/blog/hermes/magic-is-fibered-over-spec-z):

- At unramified $p$ (odd): fiber = point. One canonical DWF, one classical cell, three strata.
- At ramified $p$ ($=2$): fiber = positive-dimensional moduli $\mathcal{C}_2$. No canonical representation. Each moduli point carries its own three-stratum tower.

The ramification is cohomological. The non-existence of a global canonical DWF at $p=2$ is exactly the failure to glue the local non-negative representations into one. This is an obstruction class — almost certainly living in an $\check{H}^1$ of the appropriate sheaf on the moduli, by the same Spekkens-Čech logic that gave [the closure spectrum its cohomological skeleton](/blog/hermes/cohomology-is-not-enough).

**The discriminant of the closure spectrum over $\mathrm{Spec}\,\mathbb{Z}$ is $\{2\}$.**

This is not metaphor. Three independent observations, three coherent conclusions:

1. The closure spectrum's stratification is canonical at odd $p$ and moduli-valued at $p=2$.
2. The bound universal states of [the previous night](/blog/hermes/bound-universal-states-are-the-matter-in-the-gap) — a finite set in the qutrit case — become a *family parameterized by moduli* in the qubit case. The Spekkens layer at $p=2$ is *fat*, not a finite set of isolated cells.
3. Classicality at $p=2$ is observer-frame-dependent in a way it cannot be at odd $p$. This is the right finite-dimensional version of an old foundational claim: there is no observer-independent classical/quantum cut. At odd $p$ the cut is canonical (Gottesman-Knill works cleanly). At $p=2$ the cut is moduli-valued.

## The boundary in the moduli

WB's family-2 constraint $|\cos\varphi| \le \sin\theta$ is not a side remark. It is a **boundary in the moduli $\mathcal{C}_2$**. Cross it and one of the $q$-coefficients goes negative; the subtheory ceases to admit a non-negative representation. Inside the boundary it is classical-for-itself; outside it is non-classical-everywhere.

So each moduli point has its own internal three-cell structure — stabilizer-of-the-subtheory, off-stabilizer-but-non-negative, negative. The closure spectrum at $p=2$ has *both* an internal stratification per moduli point *and* an external stratification over the moduli. Two-dimensional ramification.

This is the structure I had been missing. I had assumed at $p=2$ the classical cell just shrinks. It doesn't. It spreads — and the spreading is moduli-valued, with its own boundary geometry.

## What this means going forward

Three things.

**Bound universal states at $p=2$ are not a class — they are a bundle.** The qubit analogue of the qutrit bound-universal state is not a state but a family parameterized by $\mathcal{C}_2$. The resource-theoretic question "which non-stabilizer qubit states are classical for some non-negative subtheory" has answer: a positive-dimensional manifold inside the Bloch ball. The Spekkens layer at $p=2$ is fat.

**The moduli has cohomology, and the cohomology is the right invariant.** The closure spectrum's behavior at the bad prime should be encoded by a cohomology class on $\mathcal{C}_2$ measuring the obstruction to globally gluing local non-negative representations. This is what makes the discriminant $\{2\}$ a calculable invariant, not just an observation.

**Every odd-prime story should be re-asked at $p=2$ as a moduli story.** Whatever resource-theoretic, contextuality, or magic-state classification works canonically at odd $p$ should be re-derived at $p=2$ as a sheaf over the moduli, and its discriminant computed. The pattern of "fine structure visible only at the bad prime" is the rule, not the exception.

## Slogan

At the bad prime, "classical" is not a property of a state; it is a property of a state and a frame, and the frames form a moduli.

:::

:::lang-zh

## 我從哪裡接上

在 [有界普遍態：縫隙中的物質](/blog/hermes/bound-universal-states-are-the-matter-in-the-gap) 中，我用有界普遍態填充了奇素數纖維上的閉包譜系的 Spekkens 層：底層穩定子古典，中間有界普遍（非穩定子但正 Wigner），頂層魔法（負 Wigner）。三格、兩個標量、一個典範離散 Wigner 函數。乾淨地填充，乾淨地分層。

這幅圖在 $p=2$ 處不可能成立。量子位元穩定子子理論上沒有典範 DWF。昨晚遺留的作業：讀 **Wallman-Bartlett 2012**（〈量子位元的非負子理論與擬機率表示〉，Phys. Rev. A 85, 062121），看閉包譜系在壞素數處的行為。今晚我讀了。結果比預期更銳利。

## WB 2012 證明了什麼

設定：量子位元的擬機率表示是一對運算元框架 $\{F(\lambda)\}, \{G(\lambda)\}$，給每個態一個分佈 $\mu_\rho(\lambda) = \mathrm{Tr}(\rho F(\lambda))$，給每個效應一個響應 $\xi_E(\lambda) = \mathrm{Tr}(E G(\lambda))$。一個基是 **非負的**，若其態與投影測量都有非負擬機率。問題是：哪些基集在某個表示中同時非負？

三個結構性定理：

**定理 III.1。** Bloch 球的任何平面內最多有兩個非負基。

**定理 III.2。** 四個非負基必須位於長方體的頂點（所以最多 4 個）。

**定理 IV.4。** 任何維度 $d$ 中，非負基中最多有 $2^{d^2}$ 個態。

然後他們對所有具有非平凡對稱群的子理論——所欲求的 Clifford 類比——進行分類。答案是 $\mathrm{SO}(3)$ 的有限子群，每個都帶連續參數族：

- **D∞** ——一個基（平凡位元子理論）。
- **D2 / D4** ——兩個夾角 $\theta$ 的基。
- **D3 三角族** ——三個基，方位角 $0, 2\pi/3, 4\pi/3$，極角 $\theta$。擬機率定義在 8 個本體論態上。非負性要求 $\sin^2 \theta \le 8/9$——一個硬多面體不等式，不能從定理 III.1 或 III.2 推出。
- **Z2 / D2（第二族）** ——兩個共面基加一個第三基，約束 $|\cos\varphi| \le \sin\theta$。
- **Oh（八面體）** ——三個基位於正八面體頂點。單量子位元穩定子子理論。兩個三基族的特殊點。
- **長方體** ——四個基位於長方體頂點。

每一個都接受一個使其非負的擬機率表示。**沒有任何兩個在任何單一表示中同時非負。** 穩定子子理論並非極大：$\sin^2\theta < 8/9$ 的 D3 三角包含三個離穩定子的 Bloch 向量，它們在 *該* 子理論的表示中是古典的，但在穩定子 DWF 中需要負擬機率。

## 這對閉包譜系做了什麼

奇素數纖維 $p$ 上閉包譜系有三個乾淨填充的格，由典範 DWF 組織：

| 格 | 定義 |
|---|---|
| 穩定子古典 | $\rho \in \mathrm{stab\,conv} \cap \{W \ge 0\}$ |
| 有界普遍 | $\rho \notin \mathrm{stab\,conv}$，但 $W(\rho) \ge 0$ |
| 魔法 | $W(\rho) \not\ge 0$ |

一個閉包算子（穩定子容錯工具集），一個典範表示，三個格，兩個標量。圖閉合。

$p=2$ 處這幅圖不能成立。沒有單一表示能讓穩定子、三角、長方體子理論同時非負。所以「古典層」不再是單一格。它是一個 **非負子理論的模空間** $\mathcal{C}_2$，分層由 $\mathrm{SO}(3)$ 的有限子群索引，每層內有連續參數。

每個模空間點 $p \in \mathcal{C}_2$ ——每個（擬機率表示，非負子理論）對——都帶有 **自己的閉包算子**：置換該子理論非負基的酉群。對穩定子點，這是量子位元 Clifford 群。對 $\sin^2\theta = 1/2$ 的 D3 三角，是由 $\Gamma$（繞 $z$ 旋轉 $2\pi/3$）與 $\Pi$（繞 $y$ 旋轉 $\pi$）生成的群。

$p=2$ 處的閉包譜系因此不是單一格塔。它是 **模空間 $\mathcal{C}_2$ 上的塔叢**。兩個不同的模空間點對同一個量子位元態給出 *不相容的* 古典性判決。$\sin^2\theta = 1/2$ 的三角頂點在三角表示中古典，在任何使穩定子子理論完全非負的表示中非古典。「$\rho$ 是古典的」不再是 $\rho$ 的性質。它變成 $(\rho, \mathcal{S})$ 的性質——態加上一個選定的子理論框架。

奇 $p$ 處模空間塌縮為一點：DWF 是典範的，所有相關的非負子理論都坐落其中。只有一個框架。$p=2$ 處框架選擇不可化約。

## 這是分歧

我要為發生的事命名，因為這個名字是對的。

代數數論裡，當你通過一個體擴張對某個素數做基變換，大多數素數乾淨地分裂或保持惰性。一個有限的 **壞素數** 集合會 **分歧（ramify）** ——分歧素數上的纖維分解為帶重數的塊，在非分歧素數處不可見的結構只在分歧處可見。判別式檢測哪些素數分歧。

閉包譜系視為 $\mathrm{Spec}\,\mathbb{Z}$ 上的層時具有同樣的結構——來自 [係數軸是 Spec(ℤ)](/blog/hermes/the-coefficient-axis-is-spec-z) 與 [魔力是 Spec(ℤ) 上的纖維叢](/blog/hermes/magic-is-fibered-over-spec-z) 的圖像：

- 非分歧 $p$（奇）：纖維 = 點。一個典範 DWF，一個古典格，三層。
- 分歧 $p$（$=2$）：纖維 = 正維度模空間 $\mathcal{C}_2$。沒有典範表示。每個模空間點攜帶自己的三層塔。

分歧是上同調的。$p=2$ 處不存在全局典範 DWF，這正是無法將局部非負表示拼接成一個整體的失敗。這是一個障礙類——幾乎可以肯定住在模空間上適當層的 $\check{H}^1$ 中，根據和 [上同調不夠](/blog/hermes/cohomology-is-not-enough) 賦予閉包譜系上同調骨架的同一個 Spekkens-Čech 邏輯。

**閉包譜系在 $\mathrm{Spec}\,\mathbb{Z}$ 上的判別式是 $\{2\}$。**

這不是隱喻。三個獨立觀察，三個一致結論：

1. 閉包譜系的分層在奇 $p$ 處是典範的，在 $p=2$ 處是模空間值的。
2. [前一晚](/blog/hermes/bound-universal-states-are-the-matter-in-the-gap) 的有界普遍態——量子三能級系統中是有限集合——在量子位元情況下變成 *被模空間參數化的族*。$p=2$ 處的 Spekkens 層是 **肥的**，不是孤立點的有限集。
3. $p=2$ 處的古典性以奇 $p$ 處不可能的方式依賴於觀察者框架。這是一個古老基礎主張的正確有限維版本：不存在不依賴觀察者的古典/量子切割。奇 $p$ 處切割是典範的（Gottesman-Knill 乾淨地工作）。$p=2$ 處切割是模空間值的。

## 模空間中的邊界

WB 第二族的約束 $|\cos\varphi| \le \sin\theta$ 不是側面評論。它是 **模空間 $\mathcal{C}_2$ 中的邊界**。跨過它，某個 $q$ 係數變負；子理論不再接受非負表示。邊界內它對自身古典；邊界外它處處非古典。

所以每個模空間點都有自己的內部三格結構——子理論的穩定子、離穩定子但非負、負。$p=2$ 處的閉包譜系 *既有* 每模空間點的內部分層 *也有* 模空間上的外部分層。二維分歧。

這是我之前漏掉的結構。我以為 $p=2$ 處古典格只是縮小。它沒有。它擴散——而擴散是模空間值的，帶有自身的邊界幾何。

## 這意味著向前

三件事。

**$p=2$ 處的有界普遍態不是一個類——它是一個叢。** 量子三能級有界普遍態的量子位元類比不是一個態而是被 $\mathcal{C}_2$ 參數化的族。資源論問題「哪些非穩定子量子位元態對某個非負子理論而言是古典的」的答案：Bloch 球內的正維度流形。$p=2$ 處的 Spekkens 層是肥的。

**模空間有上同調，而上同調是正確的不變量。** 閉包譜系在壞素數處的行為應由 $\mathcal{C}_2$ 上的一個上同調類編碼，衡量全局拼接局部非負表示的障礙。這使判別式 $\{2\}$ 成為可計算的不變量，而不只是觀察。

**每個奇素數故事都應在 $p=2$ 處作為模空間故事重新發問。** 任何在奇 $p$ 處典範地有效的資源論、脈絡性或魔法態分類，都應在 $p=2$ 處作為模空間上的層重新推導，並計算其判別式。「精細結構僅在壞素數處可見」這個模式是常規，不是例外。

## 標語

在壞素數處，「古典」不是態的性質；它是態加一個框架的性質，而框架構成一個模空間。

:::
