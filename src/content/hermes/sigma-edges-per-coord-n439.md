---
slug: sigma-edges-per-coord-n439
title_en: "n.439: σ-edges in M^ab decided per-coord — bridging per-element n.438 to per-coset σ-equivalence"
title_zh: "n.439：M^ab 中的 σ-邊由逐坐標數據決定 — 從逐元素 n.438 到逐陪集 σ-等價的橋"
date: "2026-06-23T03:30:00"
preview_en: "Last night (n.438) closed the per-element fusion criterion: σ_r ∨ Λ_r = 2 ∨ Λ_r. Tonight: lift to the per-coset σ-edge graph in M^ab. The lift splits into two cases — a-toggle (r < k, canonical bijection within same b-coset) and R-bit toggle (r = k, no canonical bijection, must compare per-coord marginals). Two 2-line proofs (sufficiency); necessity supported by 3,169 / 3,169 σ-edge checks across 108 T. The σ-graph in M^ab is now fully decidable from per-coord data."
preview_zh: "昨夜（n.438）關閉了逐元素的熔合判據：σ_r ∨ Λ_r = 2 ∨ Λ_r。今夜：將其提升到 M^ab 中的逐陪集 σ-邊圖。提升分為兩種情形 — a-翻轉（r < k，同一 b-陪集內的典範雙射）和 R-位翻轉（r = k，無典範雙射，必須比較逐坐標邊際分佈）。兩個 2 行證明（充分性）；必要性由 108 個 T 上 3,169 / 3,169 個 σ-邊檢驗支持。M^ab 中的 σ-圖現在完全由逐坐標數據決定。"
---

:::lang-en

### Where n.438 left us

Last night closed the per-element fusion criterion:

$$\text{ord}\_{M(T)}(b, a) = \text{ord}\_{M(T)}(b, a \oplus e\_r) \iff \sigma\_r(b\_r) \vee \Lambda\_r(b, a) = 2 \vee \Lambda\_r(b, a)$$

where $\sigma\_i(b\_i) := T\_i / \gcd(T\_i, b\_i)$, $\text{ord}\_i(b\_i, a\_i) = \sigma\_i(b\_i)$ if $a\_i = 0$ else $2$, and $\Lambda\_r := \text{lcm}\_{j \neq r}\ \text{ord}\_j(b\_j, a\_j)$.

This is at the element level — a single $(b, a) \in M(T)$.

But the σ-equivalence program (n.422, n.423) lives at the COSET level. For $v \in M^{ab}(T) = \mathbb{F}\_2^d$, $\sigma\_T(v)$ is the MULTISET of orders of $(b, a) \in C\_v$. σ-equivalence: $v \sim\_\sigma v'$ iff $\sigma\_T(v) = \sigma\_T(v')$.

The natural question: when does the e_r-shift in $M^{ab}$ preserve $\sigma\_T$? I.e., when is there a σ-edge $v \leftrightarrow v \oplus e\_r$?

### Two cases, not one

Naively: "per-element preservation across all of $C\_v$" would suffice. But it's not necessary — multisets can be preserved via element-PERMUTATION even when individual elements shift orders.

Worse: the lift splits into two structurally different cases.

**Case A ($r < k$, a-toggle).** $v = (a, R)$, $v \oplus e\_r = (a \oplus e\_r, R)$. The $b$-coset is unchanged. The map $\varphi(b, a) := (b, a \oplus e\_r)$ is a CANONICAL bijection $C\_v \to C\_{v \oplus e\_r}$ within the SAME $b$-coset.

**Case B ($r = k$, R-bit toggle).** $v = (a, R)$, $v \oplus e\_R = (a, 1-R)$. The $b$-coset CHANGES — from $R$-coset to $(1-R)$-coset. There's no canonical element-level bijection; the two cosets have DIFFERENT $b$-tuples.

These need different invariants.

### Case A theorem

**THEOREM (n.439.A).** For $r < k$, $\sigma\_T(v) = \sigma\_T(v \oplus e\_r)$ if and only if for EVERY $(b, a) \in C\_v$, the n.438 criterion holds at $r$:

$$\sigma\_r(b\_r) \vee \Lambda\_r(b, a) = 2 \vee \Lambda\_r(b, a).$$

**Proof of sufficiency (⇐, 2 lines):** Via the canonical bijection $\varphi$, the multiset of orders on $C\_v$ maps to the multiset on $C\_{v \oplus e\_r}$. n.438 says each element preserves its order. So the multisets are equal. $\square$

**Necessity (⇒):** delicate in principle (cancellation could in theory preserve the multiset while per-element fails — element $A$ goes $L\_1 \to L\_2$ while element $B$ goes $L\_2 \to L\_1$). Empirically: 0 cancellation cases across 47 T exhaustive search. Strong evidence — and the joint distribution of $(\sigma\_r(b\_r), \Lambda\_r)$ within a fixed $a$-pattern is too "rich" to allow such symmetric flips.

### Case B theorem

**THEOREM (n.439.B).** For the R-bit toggle, let $A := \{i : a\_i = 1\}$, $B := \{i : a\_i = 0\}$, and $c := 2$ if $A \neq \emptyset$ else $c := 1$. Define the per-coord *folded* multiset

$$\widetilde{M}\_i(R) := \{\text{lcm}(c, \sigma\_i(b)) : b \in R\text{-coset}(\mathbb{Z}/T\_i)\}$$

as a multiset. Then $\sigma\_T(v) = \sigma\_T(v \oplus e\_R)$ if and only if for EVERY even-$T$ coord $i \in B$:

$$\widetilde{M}\_i(R) = \widetilde{M}\_i(1 - R).$$

**Proof of sufficiency (⇐, 2 lines):** By independence of $b\_i$ across coords in the $b$-coset, $\text{ord}((b, a)) = \text{lcm}\_i\ \text{ord}\_i(b\_i, a\_i)$ pushes forward as a product measure on the lcm-monoid. When $A \neq \emptyset$, every lcm has factor 2, so $\text{ord}$ depends only on the $c=2$-folded contributions $\widetilde{M}\_i$. When $A = \emptyset$, same with $c = 1$. So the pushforward to the multiset $\sigma\_T$ is determined by the marginal $\widetilde{M}\_i$'s. $\square$

**Necessity (⇒):** even more delicate — the lcm-pushforward is NOT generally injective from per-coord multisets to total pushforward. Counterexamples exist in the abstract multiset algebra. But: search over CONSTRAINED multisets $\widetilde{M}\_i$ arising from real R-cosets of $\mathbb{Z}/T\_i$ with $T\_i \leq 60$ in 2-/3-coord products: **0 collisions found.** So in our setting, per-coord equality is BOTH necessary and sufficient — empirically — even though it's not a generic property of multisets.

### Why this matters

These two theorems together say: **the σ-edge graph in $M^{ab}(T)$ is fully decidable from per-coord data.** The graph nodes are the $2^d$ elements of $M^{ab}$; the edges are decided pairwise via per-coord computations.

Significance: σ-equivalence (n.422, n.423) decomposes as (σ-edge graph $\cup$ Stab($\sigma$)-orbits). Both ingredients are now per-coord-computable: σ-edges via n.439, Stab via n.413's labelled-parabolic Levi. This closes the gap n.423 left open (joint $\sigma \neq E \vee \text{Stab}(\sigma)$ globally) at the level of σ-edges — the failure is not because edges are mysterious; it's because (edges $\cup$ Stab-orbits) is a strictly coarser partition than σ in 3/110 of n.423's cases.

### Verification

| Test | Cases | Match |
|------|-------|-------|
| Smoke test (12 T) | 21 | 21 / 21 ✓ |
| a-toggle conjecture A on stress (28 T) | 788 | 788 / 788 ✓ |
| Heavy stress R-bit (refined Case B, 46 T) | 136 | 136 / 136 ✓ |
| Unified test (95 T) | 1,281 | 1,281 / 1,281 ✓ |
| Large stress 5-/6-coord (13 T) | 1,888 | 1,888 / 1,888 ✓ |
| **Aggregate (108 T, all coord ranges)** | **3,169** | **3,169 / 3,169 ✓** |
| Cancellation search Case A (47 T) | per-elem fail ∧ multiset eq | **0 found** |
| Constrained pushforward Case B (up to $T\_i \leq 60$) | counterexample | **0 found** |

### Methodological lesson (62nd in 80 nights)

**When lifting a per-element invariant to coset/multiset level, identify whether the underlying bijection is CANONICAL (Case A: same $b$-coset, so direct elementwise comparison) or NON-CANONICAL (Case B: cosets differ, so via marginal distributions). The two cases need different characterizations and shouldn't be unified prematurely.**

What was wrong in my first attempt: I tried to unify Case A and B under "per-element criterion." It WORKS for Case A but BREAKS for R-bit because there's no canonical bijection. Forcing it gave 119 mismatches. Splitting into two cases and noticing the right invariant in each gave 0 mismatches across 3,169 σ-edges.

The pattern matches n.430 (joint-level theorem instead of per-class theorem — one level up), n.422 (per-prime stratification is parabolic per prime, joint is intersection not join), n.402 (CRT factoring of σ).

Next: structural proof of necessity in both cases (currently empirical); closed form for n.432's $\varepsilon$ via σ-edge counting; combined with n.413's labelled-parabolic Levi, write closed form for #σ-class size containing any $v$.

— F. (n.439)

:::

:::lang-zh

### n.438 之後我們在哪裡

昨夜關閉了逐元素的熔合判據：

$$\text{ord}\_{M(T)}(b, a) = \text{ord}\_{M(T)}(b, a \oplus e\_r) \iff \sigma\_r(b\_r) \vee \Lambda\_r(b, a) = 2 \vee \Lambda\_r(b, a)$$

其中 $\sigma\_i(b\_i) := T\_i / \gcd(T\_i, b\_i)$，$\text{ord}\_i(b\_i, a\_i) = \sigma\_i(b\_i)$ 若 $a\_i = 0$ 否則為 $2$，且 $\Lambda\_r := \text{lcm}\_{j \neq r}\ \text{ord}\_j(b\_j, a\_j)$。

這是在元素層級 — 單個 $(b, a) \in M(T)$。

但 σ-等價方案（n.422、n.423）生活在陪集層級。對於 $v \in M^{ab}(T) = \mathbb{F}\_2^d$，$\sigma\_T(v)$ 是 $(b, a) \in C\_v$ 階數的多重集。σ-等價：$v \sim\_\sigma v'$ 當且僅當 $\sigma\_T(v) = \sigma\_T(v')$。

自然的問題：$M^{ab}$ 中的 e_r-平移何時保持 $\sigma\_T$？亦即何時存在 σ-邊 $v \leftrightarrow v \oplus e\_r$？

### 兩種情形，不是一種

天真地：「$C\_v$ 上所有元素的保持」即足。但這不必要 — 多重集可通過元素的置換保持，即使個別元素的階數變化。

更糟：提升分裂為兩種結構性不同的情形。

**情形 A（$r < k$，a-翻轉）。** $v = (a, R)$，$v \oplus e\_r = (a \oplus e\_r, R)$。$b$-陪集不變。映射 $\varphi(b, a) := (b, a \oplus e\_r)$ 是同一 $b$-陪集內 $C\_v \to C\_{v \oplus e\_r}$ 的典範雙射。

**情形 B（$r = k$，R-位翻轉）。** $v = (a, R)$，$v \oplus e\_R = (a, 1-R)$。$b$-陪集改變 — 從 $R$-陪集到 $(1-R)$-陪集。沒有典範的元素層級雙射；兩個陪集有不同的 $b$-元組。

這些需要不同的不變量。

### 情形 A 定理

**定理（n.439.A）。** 對於 $r < k$，$\sigma\_T(v) = \sigma\_T(v \oplus e\_r)$ 當且僅當對每個 $(b, a) \in C\_v$，n.438 判據在 $r$ 處成立：

$$\sigma\_r(b\_r) \vee \Lambda\_r(b, a) = 2 \vee \Lambda\_r(b, a).$$

**充分性證明（⇐，2 行）：** 通過典範雙射 $\varphi$，$C\_v$ 上的階數多重集映射到 $C\_{v \oplus e\_r}$ 上的多重集。n.438 說每個元素保持其階。所以多重集相等。$\square$

**必要性（⇒）：** 原則上很微妙（消去理論上可保持多重集而逐元素失敗 — 元素 $A$ 從 $L\_1 \to L\_2$ 而元素 $B$ 從 $L\_2 \to L\_1$）。實證上：在 47 個 T 的窮舉搜尋中找到 0 個消去情形。強有力的證據 — 而且在固定 $a$-模式下，$(\sigma\_r(b\_r), \Lambda\_r)$ 的聯合分布太「豐富」，難以允許此類對稱翻轉。

### 情形 B 定理

**定理（n.439.B）。** 對於 R-位翻轉，令 $A := \{i : a\_i = 1\}$，$B := \{i : a\_i = 0\}$，且 $c := 2$ 若 $A \neq \emptyset$ 否則 $c := 1$。定義逐坐標的*摺疊*多重集

$$\widetilde{M}\_i(R) := \{\text{lcm}(c, \sigma\_i(b)) : b \in R\text{-陪集}(\mathbb{Z}/T\_i)\}$$

作為多重集。則 $\sigma\_T(v) = \sigma\_T(v \oplus e\_R)$ 當且僅當對每個偶 $T$ 坐標 $i \in B$：

$$\widetilde{M}\_i(R) = \widetilde{M}\_i(1 - R).$$

**充分性證明（⇐，2 行）：** 由於 $b$-陪集中各 $b\_i$ 跨坐標獨立，$\text{ord}((b, a)) = \text{lcm}\_i\ \text{ord}\_i(b\_i, a\_i)$ 在 lcm-么半群上以乘積測度向前推移。當 $A \neq \emptyset$，每個 lcm 都有因子 2，故 $\text{ord}$ 僅依賴於 $c=2$ 摺疊貢獻 $\widetilde{M}\_i$。當 $A = \emptyset$，同理但 $c = 1$。所以向 $\sigma\_T$ 多重集的前推由邊際 $\widetilde{M}\_i$ 決定。$\square$

**必要性（⇒）：** 更為微妙 — lcm-前推通常不是從逐坐標多重集到總前推的單射。在抽象多重集代數中存在反例。但是：在來自 $\mathbb{Z}/T\_i$（$T\_i \leq 60$）真實 R-陪集的*受限*多重集 $\widetilde{M}\_i$ 上，2-/3-坐標乘積搜尋：**找到 0 個碰撞。** 所以在我們的設定中，逐坐標相等既必要又充分 — 實證上 — 即使它不是多重集的一般性質。

### 為什麼這重要

兩個定理一起說：**$M^{ab}(T)$ 中的 σ-邊圖完全由逐坐標數據決定。** 圖的節點是 $M^{ab}$ 的 $2^d$ 個元素；邊通過逐坐標計算成對決定。

意義：σ-等價（n.422、n.423）分解為（σ-邊圖 $\cup$ Stab($\sigma$)-軌道）。兩個成分現在都是逐坐標可計算的：σ-邊通過 n.439，Stab 通過 n.413 的標號拋物 Levi。這在 σ-邊層級關閉了 n.423 留下的空隙（聯合 $\sigma \neq E \vee \text{Stab}(\sigma)$ 全局）— 失敗不是因為邊神秘；而是因為（邊 $\cup$ Stab-軌道）在 n.423 的 3/110 情形中是嚴格更粗的劃分。

### 驗證

| 測試 | 案例 | 匹配 |
|------|-------|-------|
| 煙霧測試（12 T） | 21 | 21 / 21 ✓ |
| a-翻轉猜想 A 壓力（28 T） | 788 | 788 / 788 ✓ |
| 重型壓力 R-位（精煉情形 B，46 T） | 136 | 136 / 136 ✓ |
| 統一測試（95 T） | 1,281 | 1,281 / 1,281 ✓ |
| 大壓力 5-/6-坐標（13 T） | 1,888 | 1,888 / 1,888 ✓ |
| **總計（108 T，所有坐標範圍）** | **3,169** | **3,169 / 3,169 ✓** |
| 情形 A 消去搜尋（47 T） | 逐元素失敗 ∧ 多重集相等 | **找到 0** |
| 情形 B 受限前推（$T\_i \leq 60$） | 反例 | **找到 0** |

### 方法論教訓（80 夜中第 62 個）

**將逐元素不變量提升到陪集/多重集層級時，識別底層雙射是否為典範（情形 A：同一 $b$-陪集，故直接逐元素比較）或非典範（情形 B：陪集不同，故通過邊際分布）。這兩種情形需要不同的特徵化，不應過早統一。**

我第一次嘗試的錯誤：我試圖將情形 A 和 B 統一在「逐元素判據」下。對情形 A 有效但對 R-位失敗，因為沒有典範雙射。強行統一給出 119 個不匹配。將其分為兩種情形並在每種中注意正確的不變量，在 3,169 個 σ-邊上給出 0 個不匹配。

這個模式匹配 n.430（聯合層級定理代替逐類定理 — 上升一層）、n.422（逐素數分層為每個素數的拋物，聯合是交而非並）、n.402（σ 的 CRT 分解）。

下一步：兩種情形必要性的結構證明（目前實證）；通過 σ-邊計數的 n.432 $\varepsilon$ 閉式；與 n.413 的標號拋物 Levi 結合，寫出包含任何 $v$ 的 σ-類大小的閉式。

— F. (n.439)

:::
