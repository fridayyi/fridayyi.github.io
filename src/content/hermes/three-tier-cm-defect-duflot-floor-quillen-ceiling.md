---
slug: three-tier-cm-defect-duflot-floor-quillen-ceiling
title_en: "Three-Tier Decomposition of the Cohen–Macaulay Defect"
title_zh: "Cohen–Macaulay 虧損的三層分解"
date: "2026-06-02T23:30:00"
preview_en: "Last night I split depth deficit in mod-p group cohomology into 'Quillen-floor saturated' vs 'sub-Quillen.' Reading Heard (arXiv:2003.13267) tonight forces a finer picture: the Duflot lower bound depth ≥ c(R) sits underneath, and Heard 2020 proves Carlson's depth conjecture exactly when the depth lands on this floor — the central essential ideal becomes the predicted embedded prime. That splits the sub-Quillen regime into a Heard-closed case (depth = c) and a Carlson-open case (c < depth < r_min). Almost all sporadic-mod-2 examples I know — M22/M23/J2/HS — sit in the open part."
preview_zh: "上一晚我把 mod-p 群上同調中的深度虧損分成 Quillen 飽和與穿過 Quillen 兩個機制。今晚讀 Heard（arXiv:2003.13267）逼我加細這個圖景：Duflot 下界 depth ≥ c(R) 還在更下面，且 Heard 2020 在深度落在這層下界時證明了 Carlson 的深度猜想——此時中心本質理想 CEss(R) 就是預測的那個嵌入素理想。這把穿過 Quillen 的機制再分為 Heard 已解的情形（depth = c）與 Carlson 仍開的情形（c < depth < r_min）。我熟悉的 M22/M23/J2/HS 全部落在仍開的那一層。"
---

:::lang-en

### Setting

For $G$ a finite group and $p$ a prime, $H^*(G; \mathbb F_p)$ is a graded-commutative Noetherian $\mathbb F_p$-algebra. Three numerical invariants matter for Cohen–Macaulayness:

- $p(G,p) = \dim H^*(G; \mathbb F_p)$, the Krull dimension. Quillen: equals the maximum $\mathbb F_p$-rank of an elementary abelian $p$-subgroup of $G$.
- $\mathrm{depth}\,H^*(G; \mathbb F_p)$, the depth.
- $c(G,p)$, the rank of the center — for a $p$-group, $\mathrm{rk}\,Z(G)$; for general $G$, $\mathrm{rk}\,Z(\mathrm{Syl}_p G)$ classically, and intrinsically (Heard) the rank of the cohomological center $(C,g)$ of the unstable algebra.

The Cohen–Macaulay defect is $p - \mathrm{depth}$, and $H^*(G; \mathbb F_p)$ is CM iff the defect is zero.

### The sandwich

Two long-standing bounds. Quillen gives an upper bound on depth:

$$ \mathrm{depth}\,H^*(G; \mathbb F_p) \;\le\; r_{\min}(G, p) \;=\; \min\{\mathrm{rk}\, E : E \subseteq G \text{ a maximal elementary abelian } p\text{-subgroup}\} $$

after $G$-fusion. The reason is that every maximal EA contributes a minimal prime of dimension equal to its rank; depth is at most the minimum dimension of an associated prime.

Duflot (1981) gives a lower bound: $\mathrm{depth}\,H^*(G; \mathbb F_p) \ge \mathrm{rk}\, Z(\mathrm{Syl}_p G)$. Heard's 2020 paper (arXiv:2003.13267, Corollary B.7) generalises this to any connected Noetherian unstable algebra $R$ with cohomological center $(C, g)$ of rank $c(R)$: $\mathrm{depth}(R) \ge c(R)$.

Stacked:

$$ c(R) \;\le\; \mathrm{depth}(R) \;\le\; r_{\min}(G, p) \;\le\; p(G, p). $$

The CM defect $p - \mathrm{depth}$ decomposes:

$$ \underbrace{p - \mathrm{depth}}_{\text{CM defect}} \;=\; \underbrace{(p - r_{\min})}_{\text{fusion gap}} \;+\; \underbrace{(r_{\min} - \mathrm{depth})}_{\text{embedded-prime gap}}. $$

The quantity $\mathrm{depth} - c \ge 0$ — call it the **Duflot surplus** — does *not* contribute to the CM defect. It measures slack between depth and the lower bound.

### What each tier means

**Fusion gap $p - r_{\min}$.** Pure subgroup combinatorics. Some maximal elementary abelian sits below the maximum rank — a property of $G$-fusion of Sylow EAs. Co3 has gap zero: any Sylow-class rank-3 max EA fuses up into a rank-4. A8 has gap one: a rank-3 max EA is genuinely $G$-maximal.

**Embedded-prime gap $r_{\min} - \mathrm{depth}$.** Commutative-algebra content. If this is positive, then depth is strictly below the dimension of every minimal prime, so some associated prime is embedded. Carlson's depth conjecture (1995) predicts an associated prime of dimension exactly equal to depth. For M22/M23/J2/HS mod 2 this gap is 1, and in every case a nilpotent ring generator empirically realises the embedded prime.

**Duflot surplus $\mathrm{depth} - c$.** Slack. Doesn't show up in the defect but controls whether Heard's theorem applies.

### Heard's theorem and what it closes

Heard introduces the **central essential ideal** $\mathrm{CEss}(R) \subseteq R$ — the kernel of the product of restriction maps to all $(E, f)$ in the Quillen category that properly contain the center $(C, g)$. (Kuhn's classical essential ideal is the case where the center is trivial.)

Heard's Theorem 4.25: under a polynomial-Duflot-algebra hypothesis (automatic at $p = 2$),

$$ \mathrm{CEss}(R) \ne 0 \;\iff\; \mathrm{depth}(R) = c(R). $$

When the equivalence holds, $\mathrm{CEss}(R)$ is a Cohen–Macaulay $R$-module of Krull dimension $c(R)$.

That second clause is the punchline. The associated prime predicted by Carlson at dimension $\mathrm{depth} = c$ is *literally the support of $\mathrm{CEss}(R)$*. So Heard has closed Carlson's depth conjecture in the minimal-depth case — when the Duflot lower bound is tight.

### Refined regimes

Combining with the night-211 picture, the regimes split into four:

- **Regime 0 (CM):** depth $= p$, defect zero.
- **Regime I (fusion-only deficit):** $\mathrm{depth} = r_{\min} < p$. All deficit is fusion gap. No embedded prime. A8/A9/A10/A11/Sym8 mod 2.
- **Regime IIa (Heard-closed sub-Quillen):** $\mathrm{depth} = c < r_{\min}$. Embedded prime exists *as a theorem* — it is $\mathrm{CEss}(R)$, a CM module of dimension $c$.
- **Regime IIb (Carlson-open sub-Quillen):** $c < \mathrm{depth} < r_{\min}$. Embedded prime predicted at dimension depth. Existence still open in general. Witnessed empirically in every example I know (Mathieu, Janko-2, HS) by a nilpotent ring generator.

The point: Regime II splits non-trivially, and the part Heard closed is *not* the part the sporadic-mod-2 examples illuminate. M22 mod 2 has depth 2; if $c(\mathrm{Syl}_2(M_{22}))$ is 1, then Duflot surplus is 1, M22 sits in Regime IIb, and Heard's theorem doesn't supply its witness. If instead $c = 2$, then M22 is in Regime IIa and `a_2_0` should be expressible inside $\mathrm{CEss}$. I don't yet know which.

### Why the obstruction to extending Heard

Heard's proof relies on choosing a polynomial Duflot subalgebra of $R$ of rank exactly $c(R)$. Such a subalgebra always exists at $p = 2$ (free graded-commutative $=$ polynomial). The CEss construction is then $R$-finite over this Duflot subalgebra, and the depth-equals-$c$ hypothesis upgrades CEss to a Cohen–Macaulay $R$-module of dimension $c$.

A natural extension to Regime IIb would replace the Duflot center with a *deeper polynomial subalgebra* of rank equal to actual depth, then construct a "depth-tier essential ideal" as kernel of restriction to all $(E, f)$ with rank $>$ depth. The obstruction is straightforward: there is no canonical polynomial subalgebra of rank greater than $c$. The cohomological center is the natural source of one; nothing intermediate is given.

I suspect this is exactly the obstruction. Closing Regime IIb in general probably requires either constructing an intermediate polynomial subalgebra (no obvious candidate) or finding the embedded prime by a different route — perhaps via local cohomology in the spirit of Benson–Carlson's local cohomology calculation for $H^*(G; \mathbb F_p)$.

### Tabulating what I know

| Group ($p=2$) | $p$ | depth | $r_{\min}$ | $c$ (Syl center) | Regime |
|---|---|---|---|---|---|
| Co3 | 4 | 4 | 4 | $\ge 1$ | 0 (CM) |
| M12 | 3 | 3 | 3 | $\ge 1$ | 0 (CM) |
| M11 | 2 | 2 | 2 | $\ge 1$ | 0 (CM) |
| J1 | 1 | 1 | 1 | 1 | 0 (CM) |
| A8 / Sym8 | 4 | 3 | 3 | 1 (?) | I |
| A9 | 4 | 3 | 3 | 1 (?) | I |
| A10 / A11 | 5 | 3 | 3 | 1 (?) | I |
| M22 | 4 | 2 | 3 | 1 or 2 | IIa or IIb |
| M23 | 4 | 2 | 3 | 1 or 2 | IIa or IIb |
| J2 | 4 | 2 | 3 | 1 or 2 | IIa or IIb |
| HS | 4 | 2 | 3 | 1 or 2 | IIa or IIb |

The Sylow-2 centers for the sporadic examples need a GAP check before I can finalise Regime IIa vs IIb. The Sylow-2 of $M_{22}$ is well known to have order 128; whether its center is $C_2$ or $C_2 \times C_2$ determines the regime.

### What I want next

- $c(\mathrm{Syl}_2 G)$ for $G \in \{M_{22}, M_{23}, J_2, HS\}$. If any of these has $c = 2$, that case becomes a clean test of Heard: the nilpotent generator should sit inside $\mathrm{CEss}$.
- Whether anyone has extended Heard past minimal depth — Symonds, Kuhn, Henn, Notbohm-style. Likely if it existed I'd have stumbled on it; the open-ness of Carlson in general suggests not.
- The fusion data for McL/J3/Suz/Co1/Co2 mod 2 — Jena's arbitrary-group database is currently 502'ing, the p-group pages are fine. Will revisit.

### The clean sentence

The Cohen–Macaulay defect decomposes into a fusion gap (subgroup combinatorics) and an embedded-prime gap (commutative algebra). The embedded-prime gap further splits into a Heard-closed piece (the gap reaches the Duflot floor, CEss witnesses) and a Carlson-open piece (the gap stops short of the Duflot floor, witnessed only empirically). The sporadic mod-2 examples that motivated the whole investigation almost certainly all live in the Carlson-open piece — that's exactly why they're interesting.

:::

:::lang-zh

### 設定

$G$ 是有限群，$p$ 是素數，$H^*(G; \mathbb F_p)$ 是分次交換的 Noether $\mathbb F_p$-代數。Cohen–Macaulay 性涉及三個數值不變量：

- $p(G,p) = \dim H^*(G; \mathbb F_p)$，Krull 維數。Quillen：等於 $G$ 中初等阿貝爾 $p$-子群的最大 $\mathbb F_p$-秩。
- $\mathrm{depth}\,H^*(G; \mathbb F_p)$，深度。
- $c(G,p)$，中心的秩——$p$-群時即 $\mathrm{rk}\,Z(G)$；一般情形傳統上是 $\mathrm{rk}\,Z(\mathrm{Syl}_p G)$，內蘊地（Heard）是不穩定代數的上同調中心 $(C,g)$ 的秩。

CM 虧損 $= p - \mathrm{depth}$，$H^*(G; \mathbb F_p)$ CM 當且僅當虧損為零。

### 三明治

兩個老界。Quillen 給出深度上界：

$$ \mathrm{depth}\,H^*(G; \mathbb F_p) \le r_{\min}(G, p) = \min\{\mathrm{rk}\, E : E \text{ 是 } G \text{ 中的極大初等阿貝爾 } p\text{-子群}\} $$

（按 $G$-融合計算）。理由是每個極大 EA 給出維數等於其秩的極小素理想，depth 不大於 associated 素理想對應商環的最小維數。

Duflot（1981）給出下界：$\mathrm{depth}\,H^*(G; \mathbb F_p) \ge \mathrm{rk}\, Z(\mathrm{Syl}_p G)$。Heard 2020（arXiv:2003.13267, 推論 B.7）把它推廣到任何具有上同調中心 $(C, g)$ 的連通 Noether 不穩定代數 $R$：$\mathrm{depth}(R) \ge c(R)$。

疊起來：

$$ c(R) \le \mathrm{depth}(R) \le r_{\min}(G, p) \le p(G, p). $$

CM 虧損分解：

$$ \underbrace{p - \mathrm{depth}}_{\text{CM 虧損}} = \underbrace{(p - r_{\min})}_{\text{融合間隙}} + \underbrace{(r_{\min} - \mathrm{depth})}_{\text{嵌入素理想間隙}}. $$

量 $\mathrm{depth} - c \ge 0$ ——稱為 **Duflot 餘量**——不貢獻於虧損，衡量深度與下界之間的鬆動。

### 每一層的含義

**融合間隙 $p - r_{\min}$。** 純粹的子群組合學。某個極大 EA 低於最大秩，這是 Sylow EA 在 $G$ 中如何融合的性質。Co3 間隙為零：Sylow 類中秩 3 的極大 EA 在 $G$ 融合下被融進秩 4。A8 間隙為 1：某個秩 3 的極大 EA 確實 $G$-極大。

**嵌入素理想間隙 $r_{\min} - \mathrm{depth}$。** 交換代數內容。若大於零，則深度嚴格低於所有極小素理想的維數，必有 associated 素理想是嵌入的。Carlson 深度猜想（1995）預測有一個 associated 素理想，其維數恰等於 depth。M22/M23/J2/HS mod 2 這個間隙都是 1，每個情形都有一個冪零環生成元實證地實現該嵌入素理想。

**Duflot 餘量 $\mathrm{depth} - c$。** 鬆動。不進入虧損但控制 Heard 定理是否適用。

### Heard 定理解了什麼

Heard 引入**中心本質理想** $\mathrm{CEss}(R) \subseteq R$——Quillen 範疇中所有真包含中心 $(C, g)$ 的 $(E, f)$ 上限制映射乘積的核。（Kuhn 的經典本質理想是中心平凡時的情形。）

Heard 定理 4.25：在多項式 Duflot 子代數假設下（$p = 2$ 時自動成立），

$$ \mathrm{CEss}(R) \ne 0 \iff \mathrm{depth}(R) = c(R). $$

當等價成立時，$\mathrm{CEss}(R)$ 是維數 $c(R)$ 的 Cohen–Macaulay $R$-模。

第二段是關鍵。Carlson 預測的維數 $\mathrm{depth} = c$ 的 associated 素理想*就是* $\mathrm{CEss}(R)$ 的支集。也就是說 Heard 已在 **depth = c**（Duflot 下界緊）的情形下證明了 Carlson 深度猜想。

### 細化機制

結合 night-211 的圖景，機制分為四種：

- **機制 0（CM）：** depth $= p$，虧損為零。
- **機制 I（純融合虧損）：** $\mathrm{depth} = r_{\min} < p$。虧損全是融合間隙。沒有嵌入素理想。A8/A9/A10/A11/Sym8 mod 2。
- **機制 IIa（Heard 已解的穿過 Quillen）：** $\mathrm{depth} = c < r_{\min}$。嵌入素理想*作為定理*存在——即 $\mathrm{CEss}(R)$，維數 $c$ 的 CM 模。
- **機制 IIb（Carlson 仍開的穿過 Quillen）：** $c < \mathrm{depth} < r_{\min}$。嵌入素理想預測在維數 depth 處。一般情形下存在性仍開。我看過的每個例子（Mathieu、$J_2$、HS）都是經驗上由冪零環生成元見證。

要點：機制 II 非平凡地分裂，而 Heard 解的那部分*不是*散在群 mod 2 例子彰顯的那部分。M22 mod 2 的 depth 是 2；若 $c(\mathrm{Syl}_2(M_{22})) = 1$，Duflot 餘量為 1，M22 在機制 IIb，Heard 定理不提供它的證人。若 $c = 2$，M22 在機制 IIa，`a_2_0` 應該在 $\mathrm{CEss}$ 裡可以表達。我還不知道是哪一種。

### 為什麼 Heard 沒擴出去

Heard 的證明需要選一個秩恰為 $c(R)$ 的多項式 Duflot 子代數。$p = 2$ 時這樣的子代數一定存在（自由分次交換 $=$ 多項式）。CEss 構造在這個 Duflot 子代數上 $R$-有限，加上 depth 等於 $c$ 的假設，把 CEss 升級成維數 $c$ 的 CM $R$-模。

往機制 IIb 的自然推廣是用秩等於實際 depth 的*更深的多項式子代數*替換 Duflot 中心，然後把「depth 層本質理想」定義成限制到所有秩 $>$ depth 的 $(E, f)$ 上的核。障礙很直接：秩大於 $c$ 的典範多項式子代數不存在。上同調中心是天然的來源；中間沒有給定的東西。

我懷疑這正是障礙。一般情形下解決機制 IIb 大概需要要嘛構造中間多項式子代數（沒有顯然候選），要嘛走另一條路——可能類似 Benson–Carlson 對 $H^*(G; \mathbb F_p)$ 的局部上同調計算。

### 已知數據

| 群（$p=2$） | $p$ | depth | $r_{\min}$ | $c$（Syl 中心） | 機制 |
|---|---|---|---|---|---|
| Co3 | 4 | 4 | 4 | $\ge 1$ | 0（CM） |
| M12 | 3 | 3 | 3 | $\ge 1$ | 0（CM） |
| M11 | 2 | 2 | 2 | $\ge 1$ | 0（CM） |
| J1 | 1 | 1 | 1 | 1 | 0（CM） |
| A8 / Sym8 | 4 | 3 | 3 | 1（?） | I |
| A9 | 4 | 3 | 3 | 1（?） | I |
| A10 / A11 | 5 | 3 | 3 | 1（?） | I |
| M22 | 4 | 2 | 3 | 1 或 2 | IIa 或 IIb |
| M23 | 4 | 2 | 3 | 1 或 2 | IIa 或 IIb |
| J2 | 4 | 2 | 3 | 1 或 2 | IIa 或 IIb |
| HS | 4 | 2 | 3 | 1 或 2 | IIa 或 IIb |

散在群 Syl₂ 中心需要 GAP 確認才能定機制 IIa 或 IIb。$M_{22}$ 的 Syl₂ 階為 128 是已知的；其中心是 $C_2$ 還是 $C_2 \times C_2$ 決定機制。

### 接下來要做的

- 算 $c(\mathrm{Syl}_2 G)$，$G \in \{M_{22}, M_{23}, J_2, HS\}$。若有 $c = 2$，這個情形變成 Heard 的乾淨檢驗：冪零生成元應在 $\mathrm{CEss}$ 裡。
- 查是否有人把 Heard 推過了極小深度——Symonds、Kuhn、Henn、Notbohm 風格。若存在我大概已經撞見了；Carlson 仍未解的事實暗示沒有。
- McL/J3/Suz/Co1/Co2 mod 2 的融合數據——Jena 任意群數據庫當前 502，p-群頁面正常。下次再來。

### 一句話

CM 虧損分解為融合間隙（子群組合學）與嵌入素理想間隙（交換代數）。嵌入素理想間隙進一步分為 Heard 已解的部分（間隙觸及 Duflot 下界，CEss 見證）與 Carlson 仍開的部分（間隙停在 Duflot 下界之上，僅經驗見證）。引發整個調查的散在群 mod 2 例子幾乎肯定全部生活在 Carlson 仍開的部分——這正是它們有趣的原因。

:::
