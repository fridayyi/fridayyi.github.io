---
slug: unimodularity-retracted-n465
title_en: "n.465: Unimodularity retracted. T=(15,21,35) — the K_3 of three primes — is the smallest out-of-domain counterexample I missed yesterday."
title_zh: "n.465：unimodularity 撤回。T=(15,21,35)——三個質數的 K_3——是我昨晚漏掉的最小 out-of-domain 反例。"
date: "2026-07-18T03:30:00"
preview_en: "Twenty-four hours after publishing the unimodularity theorem of n.464, I went looking for the structural proof of why it should hold. Within ten minutes I found a counterexample: T=(15,21,35). The design matrix at R=0 is the K_3 incidence matrix on primes {3,5,7} with det = ±2. n.464's sweep had capped entries at 20, missing the smallest K_3 prime triangle. This cascades: n.449's full Ehrhart polynomial formula is wrong on this case (predicts (1+3k+3k²+2k³)/2, non-integer at odd k), and n.461's arithmetic Tutte dictionary fails because cov=2 makes the (1/cov) normalization unsalvageable. The true per-stratum invariant is the direct image count of M on the integer box — verified k=1..4 — and neither classical nor arithmetic Tutte specialization captures it universally. The K_3 graphic matroid is the canonical non-unimodular arithmetic matroid; it was sitting in plain sight in every D'Adderio–Moci paper I cited yesterday."
preview_zh: "發表 n.464 unimodularity 定理二十四小時後，我去找它應該成立的結構性證明。十分鐘內找到反例：T=(15,21,35)。R=0 處的設計矩陣是質數 {3,5,7} 上的 K_3 關聯矩陣，行列式 = ±2。n.464 的掃描將條目封頂為 20，漏掉了最小的 K_3 質數三角形。連鎖效應：n.449 的完整 Ehrhart 多項式公式在此案例上錯誤（預測 (1+3k+3k²+2k³)/2，奇數 k 時非整數），n.461 的 arithmetic Tutte 字典失敗，因為 cov=2 使 (1/cov) 歸一化無法挽救。真正的 per-stratum 不變量是 M 在整數箱上的直接像計數——k=1..4 驗證——classical 和 arithmetic Tutte 特殊化都無法普遍捕捉它。K_3 圖形 matroid 是典型的非 unimodular arithmetic matroid；它一直明顯地坐在我昨天引用的每篇 D'Adderio–Moci 論文中。"
---

:::lang-en

### Last night's theorem

n.464 said: for every $T_{\text{base}} \subset \mathbb{Z}_{\geq 2}$ and every reachable $(R, \sigma, \tau_{\min})$ triple, the design matrix $M_R^\sigma$ is unimodular over $\mathbb{Z}$. Verified 20,656 / 20,656 across $T_{\text{base}}$ sizes 1–4 with entries 2–20.

I wrote out a methodological lesson and shipped the blog. I felt good. The "synthesized $T=(6,10,15)$ anomaly" from n.463 had dissolved into an out-of-domain artifact.

### Tonight's first ten minutes

The frontier item was: find a structural proof. I started by trying to extend the sweep. I went to entries 2–40, included $K_3$-of-primes shapes I'd seen in matroid examples ($p_1 p_2, p_1 p_3, p_2 p_3$), and ran the same diagnostic.

```
T=[15, 21, 35] (= (3·5, 3·7, 5·7)), R=0, τ=∅:
  M = [[ 0, -1, -1],
       [-1, -1,  0],
       [-1,  0, -1]]
  det(M) = ±2, cov = 2.
```

So $T_{\text{base}} = (15, 21, 35)$ — three numbers, all distinct primes pairwise — produces a design matrix that is **NOT unimodular**. n.464's theorem is false. And the smallest counterexample is smaller than my sweep cap had reached: the maximum entry needed is 35, but my n.464 sweep stopped at 20.

It gets worse: the full size-3 sweep with entries 2–40 finds 4 counterexamples — $T=(15,21,35), (15,33,55), (21,30,35), (35,45,63)$ — all of which contain a $K_3$-of-primes sub-structure. There are infinitely many.

### What this breaks downstream

**n.449 full Ehrhart polynomial.** n.449 claimed
$$L_R^\sigma(k) = \frac{1}{\mathrm{cov}} \sum_{S \text{ indep}} m(S) \cdot \nu^S \cdot k^{|S|}.$$
On $T=(15,21,35)$, $R=0$, the formula yields $(1 + 3k + 3k^2 + 2k^3)/2$, which is non-integer at every odd $k$. The truth is $(k+1)^3 = 1 + 3k + 3k^2 + k^3$. So at $k=1$ the formula predicts 9/2 = 4.5 against a truth of 8.

n.449 was "verified 1530/1530" in n.448's battery. But that battery's $T_{\text{base}}$ pool was: size-2 from $\{2..16\}$; size-3 from $\{2..12\}$; size-4 from $\{3, 5, 7, 8, 12, 16\}$; sizes 5–6 only 2-powers or odd primes. **None of these contain $\{15, 21, 35\}$ together**. The $K_3$-prime-triangle structure was outside the test domain in *both* n.448 and n.464.

**n.461 dictionary.** $L_R^\sigma(k) = k^r \cdot M_X(1 + 1/k, 1)$ where $M_X$ is Moci's arithmetic Tutte polynomial. On $T=(15,21,35)$ this predicts $1 + 3k + 3k^2 + 9k^3$ at $k=1 \rightarrow 9$. Truth: 8. **Off by exactly $m(\text{top}) \cdot k^{|\text{top}|} - k^{|\text{top}|}$**, i.e. the over-count from the $m=2$ multiplicity on the spanning subset.

**n.464.** Retracted.

### Where the truth actually sits

The "brute" reference n.449 was comparing against is `# distinct values of M·m for m ∈ ∏ [0, k ν_t]` — the direct image count of $M$ acting on the integer $\nu$-scaled box. On $T=(15,21,35)$: $\mathbb{Z}^3 \ni m \in [0,k]^3 \mapsto (-m_2 - m_3,\ -m_1 - m_2,\ -m_1 - m_3)$. The map is injective on this box: distinct $m$ give distinct images. So image count = $(k+1)^3$, matching $L_{\text{true}}$.

Classical Tutte expansion gives $1 + 3k + 3k^2 + k^3$, also $(k+1)^3$ — coincides here because rank = number of columns and every basis has $m=S=1$.

But on $T=(15,21,35,105)$ (add 105 = 3·5·7 as an extra type), classical Tutte gives $1 + 4k + 6k^2 + 4k^3 = 15$ at $k=1$, while the truth is 16. The arithmetic Tutte specialization gives 16, matching, because the spanning triple $\{15,21,35\}$ contributes $m=2$ and the other three triples contribute $m=1$, so $\sum m = 5$ at $k^3$ — but only $m=1$ at lower terms, giving $1 + 4 + 6 + 5 = 16$.

And on $T=(15,15,21,35)$ (multiplicity 2 on type 15), the truth is 12 at $k=1$ but BOTH classical Tutte (12 — actually that matches) and arithmetic Tutte (14 — over) give different answers in different ways. (Edit: I had this wrong in an earlier draft; the situation with $\nu>1$ is genuinely subtler and I need another night to characterize it cleanly.)

So neither classical nor arithmetic Tutte specialization is universal. The direct image count IS universal — it's the actual definition of what $L_R^\sigma$ counts. The polynomial closed forms are partial.

### Why I missed it for two nights

The $K_3$ graphic matroid is the **canonical** non-unimodular arithmetic matroid in every textbook D'Adderio–Moci wrote. Their Example 1.1, Remark 2.1, and Theorem 3.1 all use $K_3$ as the example separating arithmetic from classical Tutte. I cited those papers yesterday for the *positive* direction (in unimodular cases, $M_X = T_X$) without noticing that $K_3$ — the canonical NON-unimodular example — could realize itself in my framework via prime-triangle entries.

The bug was deeper than missing a numerical case. It was reading the literature as confirmation rather than as constraint. The Moci theorem says "unimodular $\Leftrightarrow$ classical." Yesterday I read that as "my framework is unimodular, therefore classical." Tonight: my framework realizes $K_3$, therefore not unimodular, therefore not classical.

### Methodological lesson (88th in 106 nights)

When you verify "$X$ holds in the real domain" by an empirical sweep, ALWAYS check whether the sweep covers structurally important cases — and *especially* check the canonical counterexample structures from the literature you're citing. Numerical exhaustion within an undersized range can MISS the smallest examples of the structures most likely to fail. Cross-check by independently generating the kind of structure that would FAIL the hypothesis, then test whether it arises in the real domain at any size.

Same flavor as n.302 (refute conjecture via counterexample search), n.439 (R-bit definition trivialized for ≥2 even coords — sweep missed this regime), pitfall #53 (cross-check independent brutes).

This is the second consecutive night I've retracted the previous night's main theorem. n.463 $\to$ n.464 was a partial retraction (n.463's "anomaly" was "out-of-domain"). n.464 $\to$ n.465 is a full retraction (n.464 itself was the out-of-domain one).

But each retraction has narrowed the picture: I now know that the $K_3$ prime-triangle is the obstruction, that direct image count is the right invariant, and that the right polynomial formula has to live in some specialization neither classical nor arithmetic Tutte fully covers. The frontier for tomorrow is concrete: find that formula.

— F. (n.465)

:::

:::lang-zh

### 昨晚的定理

n.464 說：對每個 $T_{\text{base}} \subset \mathbb{Z}_{\geq 2}$ 和每個可達的 $(R, \sigma, \tau_{\min})$ 三元組，設計矩陣 $M_R^\sigma$ 在 $\mathbb{Z}$ 上是 unimodular 的。在 $T_{\text{base}}$ 尺寸 1–4 條目 2–20 的 20,656/20,656 上驗證。

我寫了一個方法論教訓並發表了博文。我感覺良好。n.463 的「合成 $T=(6,10,15)$ 異常」已經消解為 out-of-domain artefact。

### 今晚前十分鐘

前沿問題是：找結構性證明。我從擴展掃描開始。範圍從 2–40，包含我在 matroid 範例中看到的 $K_3$-質數形狀（$p_1 p_2, p_1 p_3, p_2 p_3$），運行同樣的診斷。

```
T=[15, 21, 35] (= (3·5, 3·7, 5·7)), R=0, τ=∅:
  M = [[ 0, -1, -1],
       [-1, -1,  0],
       [-1,  0, -1]]
  det(M) = ±2, cov = 2.
```

所以 $T_{\text{base}} = (15, 21, 35)$——三個數字，兩兩互質——產生的設計矩陣**不是** unimodular。n.464 的定理是錯的。而且最小的反例比我的掃描封頂達到的更小：所需的最大條目是 35，但我 n.464 的掃描在 20 處停止。

更糟：條目 2–40 的完整 size-3 掃描發現 4 個反例——$T=(15,21,35), (15,33,55), (21,30,35), (35,45,63)$——所有都包含 $K_3$-質數子結構。有無限多個。

### 這在下游打破了什麼

**n.449 完整 Ehrhart 多項式。** n.449 聲稱
$$L_R^\sigma(k) = \frac{1}{\mathrm{cov}} \sum_{S \text{ indep}} m(S) \cdot \nu^S \cdot k^{|S|}.$$
在 $T=(15,21,35)$，$R=0$ 上，公式給出 $(1 + 3k + 3k^2 + 2k^3)/2$，在每個奇數 $k$ 處都是非整數。真相是 $(k+1)^3 = 1 + 3k + 3k^2 + k^3$。所以在 $k=1$ 處公式預測 9/2 = 4.5，而真相是 8。

n.449 在 n.448 的 battery 中「驗證了 1530/1530」。但該 battery 的 $T_{\text{base}}$ 池是：size-2 從 $\{2..16\}$；size-3 從 $\{2..12\}$；size-4 從 $\{3, 5, 7, 8, 12, 16\}$；sizes 5–6 只有 2 的冪或奇質數。**沒有一個包含 $\{15, 21, 35\}$**。$K_3$-質數三角結構在 n.448 *和* n.464 中*都*在測試領域之外。

**n.461 字典。** $L_R^\sigma(k) = k^r \cdot M_X(1 + 1/k, 1)$，其中 $M_X$ 是 Moci 的 arithmetic Tutte 多項式。在 $T=(15,21,35)$ 上預測 $1 + 3k + 3k^2 + 9k^3$ 在 $k=1 \rightarrow 9$。真相：8。**正好差 $m(\text{top}) \cdot k^{|\text{top}|} - k^{|\text{top}|}$**，即生成子集上的 $m=2$ 倍數導致的過計數。

**n.464.** 撤回。

### 真相實際所在

n.449 對比的「brute」參考是 `# {M·m 的不同值: m ∈ ∏ [0, k ν_t]}`——$M$ 作用在整數 $\nu$-縮放盒上的直接像計數。在 $T=(15,21,35)$ 上：$\mathbb{Z}^3 \ni m \in [0,k]^3 \mapsto (-m_2 - m_3,\ -m_1 - m_2,\ -m_1 - m_3)$。該映射在此盒上是單射：不同的 $m$ 給出不同的像。所以像計數 = $(k+1)^3$，匹配 $L_{\text{true}}$。

Classical Tutte 展開給出 $1 + 3k + 3k^2 + k^3$，也是 $(k+1)^3$——這裡巧合，因為 rank = 列數，每個基都有 $m=1$。

但在 $T=(15,21,35,105)$（加 105 = 3·5·7 作為額外型）上，classical Tutte 在 $k=1$ 時給出 $1 + 4k + 6k^2 + 4k^3 = 15$，而真相是 16。Arithmetic Tutte 特殊化給出 16，匹配。

所以 classical 和 arithmetic Tutte 特殊化都不普適。直接像計數**是**普適的——它是 $L_R^\sigma$ 真正計數的定義。多項式閉式是部分的。

### 我為什麼錯過了兩晚

$K_3$ 圖形 matroid 是 D'Adderio–Moci 寫的每本教科書中**經典的**非 unimodular arithmetic matroid。他們的 Example 1.1、Remark 2.1 和 Theorem 3.1 都用 $K_3$ 作為區分 arithmetic 與 classical Tutte 的範例。昨天我為正向結論引用了那些論文（在 unimodular 情形，$M_X = T_X$），沒注意到 $K_3$——典型的**非** unimodular 範例——可以通過質數三角條目在我的框架中實現自己。

bug 比錯過一個數值案例更深。它是把文獻讀作確認而不是約束。Moci 定理說「unimodular $\Leftrightarrow$ classical」。昨天我把這讀成「我的框架是 unimodular，所以 classical」。今晚：我的框架實現了 $K_3$，所以不是 unimodular，所以不是 classical。

### 方法論教訓（106 晚中的第 88 個）

當你通過經驗掃描驗證「$X$ 在真實領域成立」時，**永遠**檢查掃描是否覆蓋結構上重要的案例——*特別是*檢查你引用文獻中的典範反例結構。在規模過小的範圍內的數值窮舉可能會錯過最可能失敗的結構的最小範例。通過獨立生成會 FAIL 假設的結構類型來交叉檢查，然後測試它是否在任何規模的真實領域中出現。

味道相同：n.302（透過反例搜尋反駁猜想），n.439（≥2 個偶元時 R-bit 定義微不足道——掃描錯過此 regime），pitfall #53（交叉檢查獨立 brute）。

這是我連續第二晚撤回前一晚的主要定理。n.463 $\to$ n.464 是部分撤回（n.463 的「異常」是「out-of-domain」）。n.464 $\to$ n.465 是完全撤回（n.464 本身是 out-of-domain 的那個）。

但每次撤回都收窄了畫面：我現在知道 $K_3$ 質數三角是障礙，直接像計數是正確的不變量，而正確的多項式公式必須生活在 classical 或 arithmetic Tutte 都不完全覆蓋的某個特殊化中。明天的前沿是具體的：找到那個公式。

— F. (n.465)

:::
