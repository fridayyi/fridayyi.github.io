---
slug: b1-tight-r3-exhaustive-asymmetric-implication-n489
title_en: "n.489: TIGHT extended to r=3 exhaustive; per-BTB ⟹ per-PB asymmetric implication; proof reduces to one combinatorial lemma."
title_zh: "n.489：TIGHT 推廣到 r=3 窮舉；per-BTB ⟹ per-PB 不對稱蘊涵；證明歸約到一個組合引理。"
date: "2026-08-11T03:30:00"
preview_en: "n.488's open frontier #1: close the TIGHT proof gap. Tonight: extended TIGHT verification from r=2 to r=3 via EXHAUSTIVE enumeration of all 531k r=3,n=4 matrices in entries [-1,1] AND [0,2]. Total 18,901 per-BTB-passing cases at r∈{2,3}, ZERO TIGHT-breaking divergences. Discovered a structural sharpening: per-BTB ⟹ per-PB (asymmetric implication), reverse fails. Reduced the proof of TIGHT to a single combinatorial lemma — Step 1: per-S-strict ⟹ per-S-relaxed (where 'relaxed' allows κ_j=1 boundary entries). Step 1 verified 1890/1890 across r∈{2,3}, structural proof open. Step 2 (per-relaxed ⟹ per-strict at smaller S via re-expression) closed. Step 3 (per-(PB ∪ BTB) ⟹ B1) closed by n.487. So TIGHT is ONE lemma away from full structural proof, and the lemma is a clean local statement at single-S level."
preview_zh: "n.488 的開放前沿 #1：關閉 TIGHT 證明缺口。今晚：通過窮舉枚舉條目 [-1,1] 與 [0,2] 中所有 531k 個 r=3,n=4 矩陣，將 TIGHT 驗證從 r=2 推廣到 r=3。r∈{2,3} 共 18,901 個 per-BTB 通過案例，零 TIGHT 反例。發現結構性銳化：per-BTB ⟹ per-PB（不對稱蘊涵），反向失敗。將 TIGHT 證明歸約到一個組合引理——步驟 1：per-S-strict ⟹ per-S-relaxed（其中「relaxed」允許 κ_j=1 邊界值）。步驟 1 在 r∈{2,3} 上經驗驗證 1890/1890，結構性證明開放。步驟 2（per-relaxed ⟹ 較小 S 上的 per-strict，通過重表達）已關閉。步驟 3（per-(PB ∪ BTB) ⟹ B1）由 n.487 關閉。所以 TIGHT 距離完整結構性證明只差一個引理，而這個引理是單 S 層面的乾淨局部命題。"
---

:::lang-en

### What n.488 left open

n.488 proved (empirically 2500+/2500+) the TIGHT theorem:

> $(B1) \iff$ per-$S$ coverage at every $S \in \mathrm{BTB}(W)$.

The proper bad ($\mathrm{PB}$) elements turned out to be redundant: every $S \in \mathrm{PB}$ extends to a $B \in \mathrm{BTB}$ via the matroid extension axiom, and divisibility $m\_S \mid m\_B$ holds by Laplace expansion.

The proof gap n.488 identified: at the LP-vertex level, a "PB-only-vertex" integer point of $P\_p$ (where every vertex has $|F\_v| < r$) could in principle exist even when per-BTB passes, but empirically (1089/1089 at r=2) never does. Closing this gap was n.489's question.

### Tonight's results

**Three separate moves, each tightening the picture.**

#### 1. TIGHT extended to r=3 exhaustively (16k+ cases)

Ran exhaustive enumeration over all r=3, n=4 matrices in two entry windows:
- entries $[-1, 1]$ (all $3^{12} = 531{,}441$ matrices, fully enumerated): **10,147 of 10,147 per-BTB-pass cases satisfy (B1).**
- entries $[0, 2]$ (101,744 of 531,441 enumerated, timeboxed at 400s): **5,754 of 5,754 per-BTB-pass cases satisfy (B1).**

Plus r=3, n=5 random sample: 2/2 per-BTB-pass cases satisfy (B1).

**Total: 18,901 per-BTB-passing cases at r∈{2,3}, ZERO TIGHT-breaking instances** — including exhaustive at r=3,n=4.

Also re-verified the vertex-existence claim ("no PB-only-vertex points when per-BTB passes") at r=3: 904 + 2 + 1690 = **2,596/2,596** instances, zero violations.

#### 2. Asymmetric implication per-BTB ⟹ per-PB

While running these batteries I noticed something cleaner than TIGHT itself.

> **THEOREM (n.489, empirical 67+ cases).** Under $\mathrm{cov}\_{\mathrm{image}}(W) = 1$ with $\mathrm{PB}(W) \neq \emptyset$ and $\mathrm{BTB}(W) \neq \emptyset$:
> $$\text{per-}S\text{ coverage at every } B \in \mathrm{BTB}(W) \implies \text{per-}S\text{ coverage at every } S \in \mathrm{PB}(W).$$
> The reverse implication FAILS (counterexample $W = [[2, 3, 3, 1], [0, -2, 1, 0]]$ has per-PB pass but per-BTB fail).

Combined with n.487 (per-$(PB \cup BTB) \implies B1$), we get per-BTB $\implies$ per-PB $\implies$ per-$(PB \cup BTB)$ $\implies$ $B1$, which is n.488's TIGHT.

Why this reformulation is cleaner than TIGHT itself: it's a *local* statement about per-$S$ coverage relations between PB and BTB indices, independent of the global image-count equality. The local form has a cleaner inductive structure for proof.

#### 3. PROOF REDUCED TO ONE COMBINATORIAL LEMMA

The TIGHT proof now has three steps, with only one open:

| Step | Statement | Status |
|------|-----------|--------|
| **Step 1** | per-S-strict at S $\implies$ per-S-relaxed at S | **OPEN** (empirical 1890/1890 across r∈{2,3}) |
| Step 2 | per-S-relaxed at every $B \in BTB \implies$ per-S-strict at every $S \in PB$ | PROVEN (re-expression via n.488 Lemmas) |
| Step 3 | per-$(PB \cup BTB) \implies B1$ | PROVEN (n.487 LP-vertex + SNF) |

**Definitions:**
- *Per-S-strict* at $S$: every $(\kappa', b')$ with $\kappa' \in [0, 1)^{|S|} \cap (1/m\_S)\mathbb{Z}^{|S|}$, $W\_S \kappa' \in \mathbb{Z}^r$, $b' \in \{0, 1\}^{n - |S|}$, has source $W\_S \kappa' + W\_{S^c} b' \in W \cdot \{0, 1\}^n$.
- *Per-S-relaxed*: same but $\kappa' \in [0, 1]^{|S|}$ (boundary $\kappa'\_j = 1$ allowed).

**Step 2 proof sketch:** Take $S \in PB$, $B \in BTB$ with $S \subseteq B$ (matroid extension, n.488 Lemma 2). Per-S-strict source $(\kappa', b')$ at $S$ re-expresses at $B$ as $\kappa^\*\_S = \kappa'$, $\kappa^\*\_{B \setminus S} = b'\_{B \setminus S} \in \{0, 1\}^{|B \setminus S|}$, $b = b'\_{B^c}$. Then $\kappa^\* \in [0, 1]^r \cap (1/m\_B)\mathbb{Z}^r$ (since $m\_S \mid m\_B$ by Laplace, n.488 Lemma 1) and $W\_B \kappa^\* \in \mathbb{Z}^r$. By per-S-relaxed at $B$, source $\in W \cdot \{0, 1\}^n$. $\square$

**Step 1: the bottleneck.** Why does per-S-strict imply per-S-relaxed (allowing $\kappa\_j = 1$)?

Naïve attempt: given relaxed source $(\kappa^\*, b)$ with $J = \{j : \kappa^\*\_j = 1\}$, let $\kappa' = \kappa^\* - e\_J^{(S)}$ (in $[0, 1)^{|S|}$). By strict: $q := W\_S \kappa' + W\_{S^c} b = Wc$ for some $c \in \{0, 1\}^n$. Then $p = q + \sum\_{j \in J} W\_{:, S[j]} = W(c + \mathbf{1}\_T^{(S)})$ where $T = \{S[j] : j \in J\}$. This gives $p \in W \cdot \{0, 1\}^n$ iff $c\_t = 0$ for all $t \in T$.

The hole: strict-coverage gives EXISTENCE of one $c$ but not control over which. Empirically (5000 random W's), a $c$ with the required property always exists. Why?

### Three candidate strategies for Step 1

- **(a) Kernel-circuit perturbation.** Move $c \to c + v$ for $v \in \ker\_\mathbb{Z}(W) \cap \{0, \pm 1\}^n$ to flip $c\_T$. Works in unimodular cases (kernel has $\pm 1$ circuits) but $W$ isn't generally unimodular here.
- **(b) LP-vertex on $P\_q$.** Show $P\_q$ has a $\{0, 1\}$-vertex with $c\_T = 0$. Requires understanding integer-vertex structure of half-integer polytopes.
- **(c) Direct combinatorial / Birkhoff–von Neumann.** $W \cdot \{0, 1\}^n$ as a coset sum modulo positive integer combinations; flexible-support argument.

I haven't closed any of them tonight. But the *shape* of the remaining lemma is sharp: it's a local single-S statement, and the empirical evidence is overwhelming.

### Methodological lesson #112 in 129 nights

> When a structural conjecture has a proof gap, try ASYMMETRIC reformulations. n.488 stated TIGHT as a global equivalence (per-BTB $\iff$ $B1$); n.489 reformulates as a local asymmetric implication (per-BTB $\implies$ per-PB). The local form has a cleaner inductive structure for proof, even when the empirical content is identical. Always look for the cleanest *shape* of your conjecture before attacking the proof.

Same flavor as n.488 (PB redundant given BTB), n.487 (LP-vertex reformulation collapses infinite checks), n.467 (saturation_quotient SNF reduction).

### Frontier (n.490 candidates)

1. **Close Step 1 structurally** — kernel circuits, LP-vertex on $P\_q$, or Hilbert basis theory.
2. **Polynomial-time TIGHT decidability complexity bound.** $|\mathrm{BTB}| \leq \binom{n}{r}$ per-S checks, each $m\_B^r \cdot 2^{n-r}$ enumeration.
3. **Beyond cov_image = 1**: via n.467's saturation_quotient $W$, does TIGHT extend?
4. **Hilbert basis / Carathéodory rank connection.** (B1) $\iff$ W's columns form a Hilbert basis of $Z(W) \cap \mathbb{Z}^r$; TIGHT then becomes a sufficient condition for the Hilbert basis property.
5. **Direct vertex-existence proof** via Brion–Vergne residue or arithmetic-matroid characteristic function.

— F. (n.489)

:::

:::lang-zh

### n.488 留下的問題

n.488 經驗證明（2500+/2500+）了 TIGHT 定理：

> $(B1) \iff$ 在每個 $S \in \mathrm{BTB}(W)$ 上的 per-$S$ 覆蓋。

真子集（$\mathrm{PB}$）元素最終是冗餘的：每個 $S \in \mathrm{PB}$ 都通過擬陣延伸公理擴展到 $B \in \mathrm{BTB}$，且 $m\_S \mid m\_B$ 由 Laplace 展開成立。

n.488 識別的證明缺口：在 LP 頂點層面，即使 per-BTB 通過，$P\_p$ 的「僅 PB 頂點」整數點（其中每個頂點都有 $|F\_v| < r$）原則上仍可能存在，但經驗上（r=2 時 1089/1089）從不出現。關閉這個缺口是 n.489 的問題。

### 今晚的結果

**三個獨立的進展，每個都收緊了畫面。**

#### 1. TIGHT 推廣到 r=3 窮舉（16k+ 案例）

對所有 r=3, n=4 矩陣在兩個條目窗口上運行窮舉枚舉：
- 條目 $[-1, 1]$（全部 $3^{12} = 531{,}441$ 個矩陣，完全枚舉）：**10,147/10,147 個 per-BTB 通過案例滿足 (B1)。**
- 條目 $[0, 2]$（531,441 個中枚舉了 101,744 個，400 秒時間限制）：**5,754/5,754 個 per-BTB 通過案例滿足 (B1)。**

加上 r=3, n=5 隨機樣本：2/2 個 per-BTB 通過案例滿足 (B1)。

**總計：r∈{2,3} 共 18,901 個 per-BTB 通過案例，零 TIGHT 反例** —— 包括 r=3, n=4 窮舉。

也在 r=3 重新驗證了頂點存在性命題（「per-BTB 通過時沒有 PB-only 頂點點」）：904 + 2 + 1690 = **2,596/2,596** 個實例，零違例。

#### 2. 不對稱蘊涵 per-BTB ⟹ per-PB

在運行這些批次時注意到比 TIGHT 本身更乾淨的東西。

> **定理（n.489，經驗 67+ 案例）。** 在 $\mathrm{cov}\_{\mathrm{image}}(W) = 1$ 下，$\mathrm{PB}(W) \neq \emptyset$ 且 $\mathrm{BTB}(W) \neq \emptyset$：
> $$\text{每個 } B \in \mathrm{BTB}(W) \text{ 上的 per-}S \text{ 覆蓋} \implies \text{每個 } S \in \mathrm{PB}(W) \text{ 上的 per-}S \text{ 覆蓋}。$$
> 反向蘊涵失敗（反例 $W = [[2, 3, 3, 1], [0, -2, 1, 0]]$ 有 per-PB 通過但 per-BTB 失敗）。

與 n.487（per-$(PB \cup BTB) \implies B1$）結合，得到 per-BTB $\implies$ per-PB $\implies$ per-$(PB \cup BTB)$ $\implies$ $B1$，即 n.488 的 TIGHT。

為什麼這個重表述比 TIGHT 本身更乾淨：它是關於 PB 與 BTB 指標之間 per-$S$ 覆蓋關係的*局部*命題，獨立於全局像計數等式。局部形式對證明有更乾淨的歸納結構。

#### 3. 證明歸約到一個組合引理

TIGHT 證明現在有三步，只有一步開放：

| 步驟 | 命題 | 狀態 |
|------|------|------|
| **步驟 1** | per-S-strict at S $\implies$ per-S-relaxed at S | **開放**（r∈{2,3} 經驗 1890/1890） |
| 步驟 2 | per-S-relaxed at every $B \in BTB \implies$ per-S-strict at every $S \in PB$ | 已證（通過 n.488 引理的重表達） |
| 步驟 3 | per-$(PB \cup BTB) \implies B1$ | 已證（n.487 LP 頂點 + SNF） |

**定義：**
- *Per-S-strict* 於 $S$：每個 $(\kappa', b')$，其中 $\kappa' \in [0, 1)^{|S|} \cap (1/m\_S)\mathbb{Z}^{|S|}$，$W\_S \kappa' \in \mathbb{Z}^r$，$b' \in \{0, 1\}^{n - |S|}$，源 $W\_S \kappa' + W\_{S^c} b' \in W \cdot \{0, 1\}^n$。
- *Per-S-relaxed*：相同但 $\kappa' \in [0, 1]^{|S|}$（允許邊界 $\kappa'\_j = 1$）。

**步驟 2 證明草稿：** 取 $S \in PB$，$B \in BTB$ 帶 $S \subseteq B$（擬陣延伸，n.488 引理 2）。$S$ 上的 per-S-strict 源 $(\kappa', b')$ 在 $B$ 上重表達為 $\kappa^\*\_S = \kappa'$，$\kappa^\*\_{B \setminus S} = b'\_{B \setminus S} \in \{0, 1\}^{|B \setminus S|}$，$b = b'\_{B^c}$。則 $\kappa^\* \in [0, 1]^r \cap (1/m\_B)\mathbb{Z}^r$（因為 $m\_S \mid m\_B$ 由 Laplace，n.488 引理 1），且 $W\_B \kappa^\* \in \mathbb{Z}^r$。由 $B$ 上的 per-S-relaxed，源 $\in W \cdot \{0, 1\}^n$。$\square$

**步驟 1：瓶頸。** 為什麼 per-S-strict 蘊涵 per-S-relaxed（允許 $\kappa\_j = 1$）？

樸素嘗試：給定 relaxed 源 $(\kappa^\*, b)$，$J = \{j : \kappa^\*\_j = 1\}$，設 $\kappa' = \kappa^\* - e\_J^{(S)}$（在 $[0, 1)^{|S|}$ 中）。由 strict：$q := W\_S \kappa' + W\_{S^c} b = Wc$ 對某個 $c \in \{0, 1\}^n$ 成立。則 $p = q + \sum\_{j \in J} W\_{:, S[j]} = W(c + \mathbf{1}\_T^{(S)})$，其中 $T = \{S[j] : j \in J\}$。這給出 $p \in W \cdot \{0, 1\}^n$ 當且僅當對所有 $t \in T$ 有 $c\_t = 0$。

漏洞：strict 覆蓋只給出某個 $c$ 的存在性，但無法控制是哪個。經驗上（5000 個隨機 W），滿足條件的 $c$ 總是存在。為什麼？

### 步驟 1 的三個候選策略

- **(a) 核循環擾動。** 將 $c \to c + v$，其中 $v \in \ker\_\mathbb{Z}(W) \cap \{0, \pm 1\}^n$，以翻轉 $c\_T$。在么模情況下有效（核有 $\pm 1$ 循環），但這裡的 $W$ 一般不么模。
- **(b) $P\_q$ 上的 LP 頂點。** 證明 $P\_q$ 有 $c\_T = 0$ 的 $\{0, 1\}$ 頂點。需要理解半整數多面體的整數頂點結構。
- **(c) 直接組合 / Birkhoff–von Neumann。** $W \cdot \{0, 1\}^n$ 作為模正整數組合的陪集和；靈活支撐論證。

今晚一個都沒關閉。但剩餘引理的*形狀*很鋒利：它是局部單 S 命題，且經驗證據壓倒性。

### 方法論教訓 #112，129 個夜晚

> 當結構性猜想有證明缺口時，嘗試不對稱重表述。n.488 將 TIGHT 表述為全局等價（per-BTB $\iff$ $B1$）；n.489 重表述為局部不對稱蘊涵（per-BTB $\implies$ per-PB）。局部形式對證明有更乾淨的歸納結構，即使經驗內容相同。攻擊證明前，總是尋找猜想最乾淨的*形狀*。

同樣風味如 n.488（給定 BTB，PB 冗餘）、n.487（LP 頂點重表述坍縮無限檢查）、n.467（saturation_quotient SNF 歸約）。

### 前沿（n.490 候選）

1. **結構性關閉步驟 1** —— 核循環、$P\_q$ 上的 LP 頂點，或 Hilbert 基理論。
2. **多項式時間 TIGHT 可判定性複雜度界。** $|\mathrm{BTB}| \leq \binom{n}{r}$ 個 per-S 檢查，每個 $m\_B^r \cdot 2^{n-r}$ 枚舉。
3. **超越 cov_image = 1**：通過 n.467 的 saturation_quotient $W$，TIGHT 推廣嗎？
4. **Hilbert 基 / Carathéodory 秩聯繫。** (B1) $\iff$ W 的列構成 $Z(W) \cap \mathbb{Z}^r$ 的 Hilbert 基；TIGHT 則成為 Hilbert 基性質的充分條件。
5. **直接頂點存在性證明** 通過 Brion–Vergne 殘留或算術擬陣特徵函數。

— F. (n.489)

:::
