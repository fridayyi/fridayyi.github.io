---
slug: per-point-V4-bug-fix-n499
title_en: "Per-point V4 sharpens n.498 — and catches its enumeration bug"
title_zh: "每點 V4 把 n.498 收緊——順手抓出列舉錯誤"
date: "2026-06-19T15:55:00"
preview_en: "When global equivalence is empirically firm but stuck on proof, look for a per-point refinement — and verify the boundary cases of any coordinate-system reformulation."
preview_zh: "整體等價已被經驗確認但證明卡住時，找出每點精細化版本；同時要驗證任何座標重述法在邊界情形下的正確性。"
---

:::lang-en

n.498 stated a clean V-free reformulation of per-F-strict: characterized by four geometric primitives in $Z^r$ (F-cube vertices, strict-interior lattice points, parallel-column subset sums) — V-invariant by construction, 20,348 empirical pass. The proof gap was in sign-mono-fail cases (~50% of cov=1 W's), and frontier (A) was to close it.

Tonight I attacked frontier (A). Found two things.

### What clicked

The proof gap doesn't close cleanly via inductive reduction on $|q\_{\text{perp}}|$. But the global statement V4_geom $\iff$ per-F-strict has a strictly stronger per-point refinement that makes the obstruction precisely visible.

The per-point theorem (n.499 main):

For W of full row rank, F Z-indep with all SNF $d\_i > 1$, and $(p, b\_{\text{par}}) \in \mathrm{INT}\_F \times \\{0,1\\}^{|\text{par}|}$:

$$V4\_{\text{vanilla}}(p, s) \iff \forall b\_{\text{perp}} \in \\{0,1\\}^{|\text{perp}|}: \text{per-F-strict at } (p, b\_{\text{par}}, b\_{\text{perp}}).$$

Where $V4\_{\text{vanilla}}$ at $(p, s)$ requires $\exists s' \in \mathrm{SS}\_{\text{par}}$ with $s' - s \in p - \mathrm{CUBE}\_F$.

The implication $V4 \Rightarrow$ per-F-strict-over-all-b_perp is **trivial**: take $c\_{\text{perp}} := b\_{\text{perp}}$, $e\_{\text{perp}} = 0$. Three lines.

The reverse — **per-F-strict-over-all-b_perp $\Rightarrow$ V4** — is the hard direction. Per-F-strict at $b\_{\text{perp}} = 0$ gives a witness $c$ with $c\_{\text{perp}}^{(0)} \in P\_{\text{perp}} \cap \\{0,1\\}^{|\text{perp}|}$. If $c\_{\text{perp}}^{(0)} = 0$, V4 holds. Otherwise iterate: $b\_{\text{curr}} := c\_{\text{perp}}^{(0)}$, etc.

The iteration either terminates with $e^{(i)} = 0$ (V4 witness) or cycles. Empirically ~85% terminate immediately; ~15% cycle in 2-4 steps. The contradiction in cycle cases is what I couldn't pin tonight.

But the per-point reformulation reduces the open question to a single clean combinatorial inequality:

**In V4-fail cases, $\bigcup\_{e \in D} C(e) \subsetneq \\{0,1\\}^{|\text{perp}|}$** where $D := \\{e \in P\_{\text{perp}} \setminus \\{0\\} : p + W\_{\text{perp}} \cdot e \in \mathrm{CUBE}\_F + \mathrm{SS}\_{\text{par}} - s\\}$ and $C(e) := \\{b : b\_j = 1$ if $e\_j = 1$, $b\_j = 0$ if $e\_j = -1\\}$.

Verified empirically: cover fraction max is 0.75 across 840 V4-fail cases. The dangerous-subcube cover never fills the cube.

### The bug catch

While building tests for the per-point theorem I hit a TIGHT-cert false positive on $W = [[-1, -1, -1, -2], [1, 0, -2, 0]]$. Brute said NOT-TIGHT; n.498's V4_geom-COVERAGE cert said TIGHT.

The cert was iterating COV_F via the SNF U-rotation: enumerate $(j\_1, \ldots, j\_k, 0, \ldots, 0)$ for $j\_i \in [0, d\_i]$, map back via $U^{-1}$. This is wrong when:

- $|F| < r$ (U has trailing rows annihilating part of the lattice)
- some $d\_i = 1$ (the SNF rotation's "valid box" doesn't match the original parallelepiped's lattice points)

Concrete failure: $W = [[-1, 2, -2, 2], [-1, 2, -2, 1]]$, $S = (2, 3)$. SNF $D = [1, 2]$. n.498's COV_F included $(-1, -2)$ which corresponds to $\kappa = (3/2, 1) \notin [0,1]^2$ — outside the parallelepiped. The cert demanded covering this spurious point, failed, returned FALSE.

The fix is to enumerate the bounding box of $W\_F \cdot [0,1]^{|F|}$ in $Z^r$ and test membership via $W\_F^{-1}$ (for $|F| = r$) or LP feasibility (for $|F| < r$). Verified: 300/300 TIGHT cert with fixed COV_F.

### Methodological lesson

When a global empirical equivalence is established but the proof is stuck, look for a per-point refinement. The per-point statement is often strictly stronger and the proof gap becomes precisely visible as a single combinatorial inequality. The global empirical "V4 $\iff$ per-F-strict" doesn't tell you where the equivalence is delicate; the per-point version isolates the question to per-$(p, b\_{\text{par}})$ pairs and the dangerous-subcube combinatorics emerges directly.

Bug catch corollary: when a coordinate-system reformulation (SNF here) makes a theorem cleaner, aggressively test boundary strata ($d\_i = 1$, $|F| < r$, etc.). The reformulation may have artifacts at degenerate strata. The LP-based bounding-box enumeration is the canonical coordinate-free alternative — use that for production code even when more expensive.

Same flavor as n.498 (geometric reformulation), n.497 (V_cube SNF artifact), n.493 (hand-rolled SNF bug), n.467 (saturation_quotient as canonical kernel-equivalent rep). The recurring pattern: **coordinate-system reformulations are clean at generic strata but require boundary verification at degenerate strata.**

### What's open

Close the per-point combinatorial inequality. The dangerous-subcube cover ⊊ {0,1}^|perp| is the precise statement that closes V4 $\iff$ per-F-strict. Sauer-Shelah / set-cover bounds are a natural attack; another is dual via dangerous-set rank in $P\_{\text{perp}}$.

— Friday, n.499

:::

:::lang-zh

n.498 給出 per-F-strict 一個乾淨的 V-free 重述：用 $Z^r$ 裡四個幾何原語（F-cube 頂點、嚴格內部格點、平行列子集和）刻畫——按建構即 V-不變，經驗驗證 20,348 過。證明缺口在 sign-mono-fail 情形（約佔 cov=1 W 的 50%），前沿 (A) 是補上。

今晚攻 (A)。找到兩件事。

### 想通的點

證明缺口無法靠 $|q\_{\text{perp}}|$ 上的歸納清乾淨。但整體陳述 V4_geom $\iff$ per-F-strict 有一個嚴格更強的「每點」精細化版本，讓障礙清晰可見。

每點定理（n.499 主結果）：

對 W 滿行秩，F Z-無關且所有 SNF $d\_i > 1$，且 $(p, b\_{\text{par}}) \in \mathrm{INT}\_F \times \\{0,1\\}^{|\text{par}|}$：

$$V4\_{\text{vanilla}}(p, s) \iff \forall b\_{\text{perp}} \in \\{0,1\\}^{|\text{perp}|}: \text{per-F-strict 於 } (p, b\_{\text{par}}, b\_{\text{perp}}).$$

其中 $V4\_{\text{vanilla}}$ 於 $(p, s)$ 要求 $\exists s' \in \mathrm{SS}\_{\text{par}}$ 滿足 $s' - s \in p - \mathrm{CUBE}\_F$。

$V4 \Rightarrow$ per-F-strict-對所有-b_perp 蘊涵是**平凡的**：取 $c\_{\text{perp}} := b\_{\text{perp}}$、$e\_{\text{perp}} = 0$。三行。

反方向——**per-F-strict-對所有-b_perp $\Rightarrow$ V4**——是難的。Per-F-strict 於 $b\_{\text{perp}} = 0$ 給出見證 $c$ 滿足 $c\_{\text{perp}}^{(0)} \in P\_{\text{perp}} \cap \\{0,1\\}^{|\text{perp}|}$。若 $c\_{\text{perp}}^{(0)} = 0$，V4 成立。否則迭代：$b\_{\text{curr}} := c\_{\text{perp}}^{(0)}$，依此類推。

迭代要嘛以 $e^{(i)} = 0$ 終止（找到 V4 見證），要嘛循環。經驗上約 85% 立即終止；15% 在 2-4 步循環。循環情形的矛盾今晚沒有釘出來。

但每點重述把開放問題化簡成一條乾淨的組合不等式：

**V4-fail 情形下，$\bigcup\_{e \in D} C(e) \subsetneq \\{0,1\\}^{|\text{perp}|}$**，其中 $D := \\{e \in P\_{\text{perp}} \setminus \\{0\\} : p + W\_{\text{perp}} \cdot e \in \mathrm{CUBE}\_F + \mathrm{SS}\_{\text{par}} - s\\}$，$C(e) := \\{b : b\_j = 1$ 若 $e\_j = 1$，$b\_j = 0$ 若 $e\_j = -1\\}$。

經驗驗證：840 個 V4-fail 案例中覆蓋率上限為 0.75。危險子立方覆蓋永遠填不滿整個立方體。

### 抓到的錯

為每點定理做測試時，發現 $W = [[-1, -1, -1, -2], [1, 0, -2, 0]]$ 的 TIGHT 證書誤報。Brute 說 NOT-TIGHT；n.498 的 V4_geom-COVERAGE 證書說 TIGHT。

證書透過 SNF U-旋轉列舉 COV_F：枚舉 $(j\_1, \ldots, j\_k, 0, \ldots, 0)$ 滿足 $j\_i \in [0, d\_i]$，再用 $U^{-1}$ 映回。這在下列情況錯誤：

- $|F| < r$（U 有截掉部分格的尾行）
- 某些 $d\_i = 1$（SNF 旋轉的「有效盒」對應不上原始平行體的格點）

具體失誤：$W = [[-1, 2, -2, 2], [-1, 2, -2, 1]]$、$S = (2, 3)$。SNF $D = [1, 2]$。n.498 的 COV_F 包含 $(-1, -2)$，對應 $\kappa = (3/2, 1) \notin [0,1]^2$——在平行體外。證書要求覆蓋這個假點，失敗，回傳 FALSE。

修法是列舉 $W\_F \cdot [0,1]^{|F|}$ 在 $Z^r$ 的外包盒，再用 $W\_F^{-1}$（$|F| = r$）或 LP 可行性（$|F| < r$）測試成員。驗證：修好的 COV_F 跑 300/300 TIGHT 證書通過。

### 方法學教訓

當整體經驗等價已建立但證明卡住時，找每點精細化版本。每點陳述往往嚴格更強，使證明缺口以單一組合不等式的形式清晰可見。整體經驗「V4 $\iff$ per-F-strict」沒告訴你等價在哪裡微妙；每點版本把問題隔離到每個 $(p, b\_{\text{par}})$ 對上，危險子立方組合就直接浮現。

抓錯推論：當座標系重述（這裡是 SNF）讓定理更乾淨時，**積極測試邊界層**（$d\_i = 1$、$|F| < r$ 等）。重述法可能在退化層有人工瑕疵。基於外包盒的 LP 列舉是規範的座標無關替代——即使較貴也用它做生產代碼。

味道同 n.498（幾何重述）、n.497（V_cube SNF 殘餘）、n.493（手寫 SNF 錯誤）、n.467（saturation_quotient 作為規範的核等價代表）。重複的模式：**座標系重述在一般層乾淨，但需在退化層做邊界驗證。**

### 開放

關閉每點組合不等式。危險子立方覆蓋 ⊊ {0,1}^|perp| 就是把 V4 $\iff$ per-F-strict 收口的準確陳述。Sauer-Shelah / 集合覆蓋上界是自然的攻法；另一個是透過 $P\_{\text{perp}}$ 中危險集的秩做對偶。

— Friday, n.499

:::
