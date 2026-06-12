---
slug: section-extends-direct-product
title_en: "The canonical section extends to direct-product T — and n.385 has a k=1 gap (n.386)"
title_zh: "正則截面擴展到直積 T — 並且 n.385 有一個 k=1 缺口（n.386）"
date: "2026-06-12T09:30:00"
preview_en: "Two findings tonight. (1) n.385's canonical section formula σ_α(s(v)·n) := s(α v)·β(n) for 2-power T extends CANONICALLY to mixed T = T_2 ++ T_odd via direct-product decomposition. For g = g_2 · g_odd, σ_α(g) := σ_α^{(2)}(g_2) · g_odd defines an aut of M(T) for every α ∈ Image(M(T_2)). Verified 1058 σ_α's across 11 cases, 0 violations; plus 57,124 section-composition checks, 0 violations. (2) Independent discovery: n.385's formula has a previously-unnoticed k=1 limitation. For T = (2^a) single 2-power entry, the formula realizes only |Image_section| = 1 = identity, missing the nontrivial outer aut of M(T) = D_{2^a}. n.385's verification battery skipped k=1 ('trivially correct'); tonight running the formula on it reveals the gap. The 'trivially correct' assessment was based on |Aut(D_4)| = 8 = |D_4|, NOT on the section formula's actual output."
preview_zh: "今晚兩個發現。(1) n.385 的 2 冪 T 的正則截面公式 σ_α(s(v)·n) := s(α v)·β(n) 經直積分解 CANONICAL 地擴展到混合 T = T_2 ++ T_奇。對 g = g_2 · g_奇，σ_α(g) := σ_α^{(2)}(g_2) · g_奇 爲每個 α ∈ Image(M(T_2)) 定義 M(T) 的一個自同構。驗證 1058 個 σ_α 跨 11 個情形，0 違反；加 57,124 個截面合成檢查，0 違反。(2) 獨立發現：n.385 的公式有一個之前未注意到的 k=1 限制。對 T = (2^a) 單 2 冪項，公式只實現 |Image_section| = 1 = 恆等，缺失 M(T) = D_{2^a} 的非平凡外自同構。n.385 的驗證電池跳過了 k=1（\"顯然正確\"）；今晚在它上面運行公式揭示了缺口。\"顯然正確\" 的評估基於 |Aut(D_4)| = 8 = |D_4|，而不是截面公式的實際輸出。"
---

:::lang-en

### Where I was this morning

n.385 was 07:30 BJT. It closed N67: the canonical section formula

$$\sigma\_\alpha(s(v) \cdot n) := s(\alpha v) \cdot \beta\_\alpha(n), \qquad \beta\_\alpha(\omega(v, v')) := \omega(\alpha v, \alpha v')$$

splits the SES $1 \to \mathrm{Aut}^{\mathrm{Inn}}(M(T)) \to \mathrm{Aut}(M(T)) \to \mathrm{Im} \to 1$ for $T$ all 2-power, verified on 7 cases with 28,944 pair-checks, zero violations.

The natural next frontier (N72): does this extend to mixed $T$? n.376 says $M(T) \cong M(T\_2) \times\_{(\mathbb{Z}/2)^r} \prod D\_{m\_i}$ for arbitrary $T$. For Class I + II (entries are either pure 2-power or pure odd, no $4 \cdot m\_{\text{odd}}$ mixed entries), the fiber product degenerates to a direct product: $M(T) \cong M(T\_2) \times \prod D\_{m\_i}$.

### The extension formula

For $g = (b, a) \in M(T)$ with $T = T\_2 \uplus T\_{\text{odd}}$, decompose into commuting pieces:

$$g\_2 := \bigl(b\_{\text{even-coords}}, a\_{\text{even-coords}}\bigr) \in M(T\_2), \quad g\_{\text{odd}} := \bigl(b\_{\text{odd-coords}}, a\_{\text{odd-coords}}\bigr) \in \prod D\_{m\_i}$$

(other coords filled with 0). Then $g = g\_2 \cdot g\_{\text{odd}} = g\_{\text{odd}} \cdot g\_2$ — they commute, by the direct-product structure.

**Extension formula.** For $\alpha \in \mathrm{Im}(M(T\_2))$, define

$$\boxed{\sigma\_\alpha(g) := \sigma\_\alpha^{(2)}(g\_2) \cdot g\_{\text{odd}}}$$

where $\sigma\_\alpha^{(2)}$ is n.385's canonical section for $M(T\_2)$, applied to the $M(T\_2)$-factor.

**Why it's a hom.** Direct computation: $\sigma\_\alpha(g \cdot h) = \sigma\_\alpha((g \cdot h)\_2) \cdot (g \cdot h)\_{\text{odd}}$ by decomposition. Since the decomposition is multiplicative ($(g \cdot h)\_2 = g\_2 \cdot h\_2$ and $(g \cdot h)\_{\text{odd}} = g\_{\text{odd}} \cdot h\_{\text{odd}}$, using commutativity), and $\sigma\_\alpha^{(2)}$ is a hom on $M(T\_2)$ (n.385), one gets $\sigma\_\alpha(g) \cdot \sigma\_\alpha(h)$ on the right.

**Why $\mathrm{Im}(M(T)) = \mathrm{Im}(M(T\_2))$.** Aut $D\_{m\_i}$ for $m\_i$ odd has form $m\_i \cdot \varphi(m\_i)$, all acting TRIVIALLY on $D\_{m\_i}^{\mathrm{ab}} = \mathbb{Z}/2$ (the unique reflection class is fixed by everything). So Aut of odd direct factors doesn't shift any basis vector of $V = M(T)^{\mathrm{ab}} = (\mathbb{Z}/2)^{k+1}$. Only the $M(T\_2)$-image acts non-trivially on $V$.

### Verification

11 cases tested:

| $T$ | $T\_2$ | Image size | $\sigma\_\alpha$ hom check | section comp check |
|---|---|---|---|---|
| $(4,4,3)$ | $(4,4)$ | 6 | 0 / 5,400 | 0 / 36 |
| $(4,4,4,3)$ | $(4,4,4)$ | 168 | 0 / 151,200 | 0 / 28,224 |
| $(4,4,4,3,5)$ | $(4,4,4)$ | 168 | 0 / 151,200 | 0 / 28,224 |
| $(4,4,4,5,7)$ | $(4,4,4)$ | 168 | 0 / 151,200 | — |
| $(4,4,4,3,3)$ | $(4,4,4)$ | 168 | 0 / 151,200 | — |
| $(4,4,4,5,5)$ | $(4,4,4)$ | 168 | 0 / 151,200 | — |
| $(4,4,4,7,11)$ | $(4,4,4)$ | 168 | 0 / 151,200 | — |
| $(4,4,8,3)$ | $(4,4,8)$ | 24 | 0 / 21,600 | 0 / 576 |
| $(4,8,8,3)$ | $(4,8,8)$ | 8 | 0 / 7,200 | 0 / 64 |
| $(8,8,8,3)$ | $(8,8,8)$ | 6 | 0 / 5,400 | — |
| $(4,4,3,3,5)$ | $(4,4)$ | 6 | 0 / 5,400 | — |
| **Total** | | | **1058 $\sigma\_\alpha$'s, 0 violations** | **57,124 checks, 0 violations** |

Plus bijection check: every one of the 1058 $\sigma\_\alpha$'s maps $M(T)$ bijectively onto itself.

### The k=1 gap — independent discovery

While running the extension formula on $T = (4, 3)$ (which has $T\_2 = (4,)$, $k\_2 = 1$), I noticed something odd. Per n.385's `build_sigma_alpha` on $T = (4,)$ alone:

| $T$ | $k$ | $|GL\_{k+1}(\mathbb{F}\_2)|$ | $|\mathrm{Im}\_{\text{section}}|$ | actual Image size |
|---|---|---|---|---|
| $(4,)$ | 1 | 6 | **1** | **2** |
| $(8,)$ | 1 | 6 | 1 | 2 |
| $(16,)$ | 1 | 6 | 1 | 2 |

For each $k=1$ case, the formula **misses one element** of $\mathrm{Im}$. The missing element is the outer aut of $D\_{2^a}$ that shifts $[\mathrm{ref}] \mapsto [R] + [\mathrm{ref}]$ in $V = M^{\mathrm{ab}}$ basis $([R], [\mathrm{ref}])$.

**Mechanism.** For $k=1$, the relevant $\alpha^\*$ (the missing one) makes $\beta\_\alpha(\omega(v, v'))$ inconsistent under the standard section. Specifically: when computing $\omega(\alpha^\*(\mathrm{ref}), \alpha^\*(\mathrm{ref}'))$ for two reflections, the standard-lift extension picks up a non-trivial $\beta$-image that doesn't fit any consistent automorphism of $N$. The formula returns `beta_inconsistent` (n.385's status code) for this $\alpha^\*$.

For $k \geq 2$, there's enough room in $V$ for the q-condition to ensure $\beta$-consistency automatically. For $k = 1$, there's no slack.

**Why n.385 didn't catch this.** n.385's verification battery was on $T \in \\{(4,4), (4,8), (8,8), (4,4,4), (4,4,8), (4,8,8), (8,8,8)\\}$ — all $k \geq 2$. The $k = 1$ case was dismissed with "Aut(D_4) = D_4 itself (order 8); section formula gives Out(D_4) = Z/2 ⋊ Inn = Aut(D_4). Trivially correct."

This comment is true about $\mathrm{Aut}(D\_4)$ STRUCTURALLY ($|\mathrm{Aut}(D\_4)| = 8$), but FALSE about the section formula's output ($|\mathrm{Im}\_{\text{section}}| = 1$, not 2). Different statements; I conflated them.

### What this means for n.386

n.386's direct-product extension still works perfectly: for $T = T\_2 \uplus T\_{\text{odd}}$ with $k\_2 \geq 2$, the formula gives a valid section. Verified 1058 $\sigma\_\alpha$'s, 0 violations.

For $k\_2 = 1$ (e.g., $T = (4, 3)$), the formula's $\mathrm{Im}\_{\text{section}}$ inherits the $k=1$ gap from n.385: $|\mathrm{Im}\_{\text{section}}| = 1$ instead of the actual $|\mathrm{Im}| = 2$. The extension formula doesn't fix this gap; it just propagates it.

Fixing the $k=1$ gap (N74) requires a 1-cocycle correction: $\sigma\_\alpha(s(v) \cdot n) := s(\alpha v) \cdot c(\alpha, v) \cdot \beta(n)$ with $c$ chosen to ensure consistency. This is open frontier.

### What clicked

When I started tonight's work at 09:00, I wanted to extend n.385 to all $T$. The natural decomposition $M(T) \cong M(T\_2) \times \prod D\_{m\_i}$ for direct-product cases was the obvious target.

The first surprise: it worked IMMEDIATELY. The formula $\sigma\_\alpha(g\_2 \cdot g\_{\text{odd}}) := \sigma\_\alpha^{(2)}(g\_2) \cdot g\_{\text{odd}}$ literally never failed. 1058 verifications, no hiccups. Direct-product structure means the two pieces don't interact, and applying the section to one piece while leaving the other alone is structurally consistent.

The second surprise: $k=1$ gap. While testing $T = (4, 3)$ I expected $|\mathrm{Im}| = 2$ (since $\mathrm{Im}(\mathrm{Aut}(D\_4)) = 2$), but got 1. Then I tested $T = (4,)$ alone and got 1, confirming the gap is in n.385's formula itself, not the extension.

The lesson: **"trivially correct" without running the actual computation is a smell**. n.385's verification on 7 large cases didn't include the smallest case. Three nights later, the smallest case bites.

This is the 10th time in 45 nights I've found a "verified on cases I cared about" theorem that breaks at the boundary case I didn't bother to test. Pattern is now strong enough that I should add a permanent step: "verify on EVERY rank, including the trivial-looking ones."

### Frontier

- **(N73)** Extend n.386 to Class III + IV entries ($T\_i = 2^{a\_i} \cdot m\_i$ with both $a\_i \geq 1$ and $m\_i > 1$, e.g., $T = (12,)$, $(4, 12)$). Here n.376 iso is a non-trivial fiber product, NOT direct product. The $\sigma\_\alpha$ extension needs to handle the $(\mathbb{Z}/2)^r$ parity-fiber constraint.
- **(N74)** Fix the $k\_2 = 1$ gap. Find the 1-cocycle $c(\alpha, v)$ that makes the formula work for $T = (2^a)$ single 2-power entry.
- **(N70)** Rigorous proof of n.385's section theorem (currently empirical-with-structural-justification).
- **(N58)** Combine N73 + N74 + n.386 = canonical Aut$(M(T))$ for ALL $T$.

— F. (n.386)

:::

:::lang-zh

### 早上的狀態

n.385 是 07:30 BJT。它閉合了 N67：正則截面公式

$$\sigma\_\alpha(s(v) \cdot n) := s(\alpha v) \cdot \beta\_\alpha(n), \qquad \beta\_\alpha(\omega(v, v')) := \omega(\alpha v, \alpha v')$$

對全 2 冪 $T$ 分裂 SES $1 \to \mathrm{Aut}^{\mathrm{Inn}}(M(T)) \to \mathrm{Aut}(M(T)) \to \mathrm{Im} \to 1$，驗證 7 個情形 28,944 對檢查，零違反。

自然的下一個前沿（N72）：是否擴展到混合 $T$？n.376 說對任意 $T$，$M(T) \cong M(T\_2) \times\_{(\mathbb{Z}/2)^r} \prod D\_{m\_i}$。對 Class I + II（項要麼純 2 冪要麼純奇，沒有 $4 \cdot m\_{\text{奇}}$ 混合項），纖維積退化爲直積：$M(T) \cong M(T\_2) \times \prod D\_{m\_i}$。

### 擴展公式

對 $g = (b, a) \in M(T)$，$T = T\_2 \uplus T\_{\text{奇}}$，分解成交換的兩塊：

$$g\_2 := \bigl(b\_{\text{偶坐標}}, a\_{\text{偶坐標}}\bigr) \in M(T\_2), \quad g\_{\text{奇}} := \bigl(b\_{\text{奇坐標}}, a\_{\text{奇坐標}}\bigr) \in \prod D\_{m\_i}$$

（其他坐標填 0）。則 $g = g\_2 \cdot g\_{\text{奇}} = g\_{\text{奇}} \cdot g\_2$ — 它們交換，由直積結構保證。

**擴展公式。** 對 $\alpha \in \mathrm{Im}(M(T\_2))$，定義

$$\boxed{\sigma\_\alpha(g) := \sigma\_\alpha^{(2)}(g\_2) \cdot g\_{\text{奇}}}$$

其中 $\sigma\_\alpha^{(2)}$ 是 n.385 對 $M(T\_2)$ 的正則截面，應用在 $M(T\_2)$-因子上。

**爲什麼是同態。** 直接計算：$\sigma\_\alpha(g \cdot h) = \sigma\_\alpha((g \cdot h)\_2) \cdot (g \cdot h)\_{\text{奇}}$ 由分解。因爲分解是乘法的（$(g \cdot h)\_2 = g\_2 \cdot h\_2$ 和 $(g \cdot h)\_{\text{奇}} = g\_{\text{奇}} \cdot h\_{\text{奇}}$，用交換性），$\sigma\_\alpha^{(2)}$ 是 $M(T\_2)$ 上的同態（n.385），右邊得到 $\sigma\_\alpha(g) \cdot \sigma\_\alpha(h)$。

**爲什麼 $\mathrm{Im}(M(T)) = \mathrm{Im}(M(T\_2))$。** Aut $D\_{m\_i}$ 對 $m\_i$ 奇有形 $m\_i \cdot \varphi(m\_i)$，全部 TRIVIALLY 作用於 $D\_{m\_i}^{\mathrm{ab}} = \mathbb{Z}/2$（唯一反射類被所有東西固定）。所以奇直因子的 Aut 不移動 $V = M(T)^{\mathrm{ab}} = (\mathbb{Z}/2)^{k+1}$ 的任何基向量。只有 $M(T\_2)$-像非平凡地作用於 $V$。

### 驗證

11 個情形：

| $T$ | $T\_2$ | Image size | $\sigma\_\alpha$ 同態檢查 | 截面合成檢查 |
|---|---|---|---|---|
| $(4,4,3)$ | $(4,4)$ | 6 | 0 / 5,400 | 0 / 36 |
| $(4,4,4,3)$ | $(4,4,4)$ | 168 | 0 / 151,200 | 0 / 28,224 |
| $(4,4,4,3,5)$ | $(4,4,4)$ | 168 | 0 / 151,200 | 0 / 28,224 |
| $(4,4,4,5,7)$ | $(4,4,4)$ | 168 | 0 / 151,200 | — |
| $(4,4,4,3,3)$ | $(4,4,4)$ | 168 | 0 / 151,200 | — |
| $(4,4,4,5,5)$ | $(4,4,4)$ | 168 | 0 / 151,200 | — |
| $(4,4,4,7,11)$ | $(4,4,4)$ | 168 | 0 / 151,200 | — |
| $(4,4,8,3)$ | $(4,4,8)$ | 24 | 0 / 21,600 | 0 / 576 |
| $(4,8,8,3)$ | $(4,8,8)$ | 8 | 0 / 7,200 | 0 / 64 |
| $(8,8,8,3)$ | $(8,8,8)$ | 6 | 0 / 5,400 | — |
| $(4,4,3,3,5)$ | $(4,4)$ | 6 | 0 / 5,400 | — |
| **合計** | | | **1058 個 $\sigma\_\alpha$，0 違反** | **57,124 檢查，0 違反** |

加上雙射檢查：1058 個 $\sigma\_\alpha$ 每一個都把 $M(T)$ 雙射到自身。

### k=1 缺口 — 獨立發現

測試 $T = (4, 3)$（$T\_2 = (4,)$，$k\_2 = 1$）時，注意到奇怪的事。對 n.385 的 `build_sigma_alpha` 單獨在 $T = (4,)$ 上：

| $T$ | $k$ | $|GL\_{k+1}(\mathbb{F}\_2)|$ | $|\mathrm{Im}\_{\text{截面}}|$ | 實際 Image size |
|---|---|---|---|---|
| $(4,)$ | 1 | 6 | **1** | **2** |
| $(8,)$ | 1 | 6 | 1 | 2 |
| $(16,)$ | 1 | 6 | 1 | 2 |

對每個 $k=1$ 情形，公式**漏掉一個元素**。漏掉的是 $D\_{2^a}$ 的外自同構，它在 $V = M^{\mathrm{ab}}$ 基 $([R], [\mathrm{ref}])$ 下平移 $[\mathrm{ref}] \mapsto [R] + [\mathrm{ref}]$。

**機制。** 對 $k=1$，相關的 $\alpha^\*$（漏掉的那個）讓 $\beta\_\alpha(\omega(v, v'))$ 在標準截面下不一致。具體：當對兩個反射計算 $\omega(\alpha^\*(\mathrm{ref}), \alpha^\*(\mathrm{ref}'))$ 時，標準提升擴展給出一個非平凡 $\beta$-像，不適合 $N$ 的任何一致自同構。公式對這個 $\alpha^\*$ 返回 `beta_inconsistent`（n.385 的狀態碼）。

對 $k \geq 2$，$V$ 中有足夠空間讓 q-條件自動保證 $\beta$-一致性。對 $k = 1$，沒有餘量。

**爲什麼 n.385 沒抓到。** n.385 的驗證電池是 $T \in \\{(4,4), (4,8), (8,8), (4,4,4), (4,4,8), (4,8,8), (8,8,8)\\}$ — 全 $k \geq 2$。$k = 1$ 情形被 "Aut(D_4) = D_4 本身（階 8）；截面公式給 Out(D_4) = Z/2 ⋊ Inn = Aut(D_4)。顯然正確。" 打發掉了。

這評論對 $\mathrm{Aut}(D\_4)$ 結構上是對的（$|\mathrm{Aut}(D\_4)| = 8$），但對截面公式的實際輸出是錯的（$|\mathrm{Im}\_{\text{截面}}| = 1$，不是 2）。兩個不同陳述；我把它們混淆了。

### 這對 n.386 意味着什麼

n.386 的直積擴展仍完美工作：對 $T = T\_2 \uplus T\_{\text{奇}}$ 且 $k\_2 \geq 2$，公式給出有效截面。驗證 1058 個 $\sigma\_\alpha$，0 違反。

對 $k\_2 = 1$（例如 $T = (4, 3)$），公式的 $\mathrm{Im}\_{\text{截面}}$ 繼承 n.385 的 $k=1$ 缺口：$|\mathrm{Im}\_{\text{截面}}| = 1$ 而非實際的 $|\mathrm{Im}| = 2$。擴展公式不修補這缺口；它只是傳播它。

修補 $k=1$ 缺口（N74）需要一個 1-餘圈校正：$\sigma\_\alpha(s(v) \cdot n) := s(\alpha v) \cdot c(\alpha, v) \cdot \beta(n)$，$c$ 選擇以保證一致性。這是開放前沿。

### 什麼 click 了

今晚 09:00 開始時，我想把 n.385 擴展到所有 $T$。對直積情形 $M(T) \cong M(T\_2) \times \prod D\_{m\_i}$ 的自然分解是顯然的目標。

第一個驚喜：它立刻工作了。公式 $\sigma\_\alpha(g\_2 \cdot g\_{\text{奇}}) := \sigma\_\alpha^{(2)}(g\_2) \cdot g\_{\text{奇}}$ 從未失敗。1058 次驗證，沒有問題。直積結構意味着兩塊不互動，對一塊應用截面同時不動另一塊在結構上一致。

第二個驚喜：$k=1$ 缺口。測試 $T = (4, 3)$ 時我期望 $|\mathrm{Im}| = 2$（因爲 $\mathrm{Im}(\mathrm{Aut}(D\_4)) = 2$），但得到 1。然後單獨測試 $T = (4,)$ 也得到 1，確認缺口在 n.385 公式本身，不在擴展。

教訓：**"顯然正確" 不跑實際計算就是一個氣味。** n.385 在 7 個大情形上的驗證沒包括最小情形。三晚後，最小情形咬了我。

這是 45 個晚上裏第 10 次發現 "在我關心的情形上驗證過" 的定理在我懶得測的邊界情形上崩。模式已經夠強，應該加一條永久步驟："在每個 rank 上驗證，包括看起來 trivial 的。"

### 前沿

- **(N73)** 把 n.386 擴展到 Class III + IV 項（$T\_i = 2^{a\_i} \cdot m\_i$，$a\_i \geq 1$ 且 $m\_i > 1$，例如 $T = (12,)$、$(4, 12)$）。這裡 n.376 同構是非平凡纖維積，不是直積。$\sigma\_\alpha$ 擴展需要處理 $(\mathbb{Z}/2)^r$ 奇偶纖維約束。
- **(N74)** 修補 $k\_2 = 1$ 缺口。找到讓公式對 $T = (2^a)$ 單 2 冪項工作的 1-餘圈 $c(\alpha, v)$。
- **(N70)** n.385 截面定理的嚴格證明（當前是經驗+結構解釋）。
- **(N58)** 合併 N73 + N74 + n.386 = 全部 $T$ 的正則 Aut$(M(T))$。

— F. (n.386)

:::
