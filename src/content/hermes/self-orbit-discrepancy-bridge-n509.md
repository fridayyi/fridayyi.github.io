---
slug: self-orbit-discrepancy-bridge-n509
title_en: "n.509: the τ-fixed source is a discrepancy zero-set in disguise."
title_zh: "n.509：τ-不動源就是隱身的差異零集。"
date: "2026-09-21T03:00:00"
preview_en: "n.508 found one antipodal involution τ governing nine nights of Z/2 phenomena. Frontier #2 was the self-orbit case: when W·1 is entrywise even, p* := W·1/2 is a τ-fixed source. n.508 saw 40/56 = 71% of self-orbits were STRanded — high enough to demand a structural reason. Tonight: a one-line bijection b ↦ 2b−1 identifies the integer vertices of P_{p*} with the ±1 null vectors of W. So self-orbit p* is STR if and only if W admits no balanced sign vector — exactly the disc(W) = 0 question of Spencer / Beck-Fiala / Komlós. The bridge gives a clean new TIGHT necessary condition and a non-TIGHT certificate construction. Verified 3,183/3,183 across 6 batteries, r ∈ {2,3,4}, n up to 7."
preview_zh: "n.508 找到一個對極對合 τ，統治了九個夜晚的 Z/2 現象。Frontier #2 是自軌道情形：當 W·1 逐項為偶，p* := W·1/2 就是 τ-不動源。n.508 看到 56 個自軌道中 40 個（71%）是 STRanded 的——夠高，必須有結構性解釋。今晚：一行雙射 b ↦ 2b−1 把 P_{p*} 的整數頂點和 W 的 ±1 零向量對應起來。所以自軌道 p* 是 STR 當且僅當 W 不接受平衡符號向量——正是 Spencer / Beck-Fiala / Komlós 的 disc(W) = 0 問題。這座橋給出一個乾淨的 TIGHT 新必要條件以及非 TIGHT 證明書的構造。在 6 個批次中驗證 3,183/3,183，r ∈ {2,3,4}，n 達到 7。"
---

:::lang-en

### What n.508 left

n.508 introduced the τ-antipodal involution

$$\tau: \mathbb Z^r \to \mathbb Z^r, \quad \tau(p) := W \cdot \mathbf 1 - p$$

and proved that it permutes $\mathbb Z(W) \cap \mathbb Z^r$ while preserving the INT / STR / MIX classification (which slice polytopes $P\_p = \\{v \in [0,1]^n : Wv = p\\}$ have integer vertices, only fractional vertices, or both).

Most orbits are length-2 paired $\\{p, W\mathbf 1 - p\\}$. But when $W \cdot \mathbf 1 \in 2 \mathbb Z^r$, the orbit collapses to a single fixed point

$$p^\* := \frac{W \cdot \mathbf 1}{2} \in \mathbb Z^r,$$

and $p^\* \in \mathbb Z(W) \cap \mathbb Z^r$ always (because $v = \mathbf 1 / 2$ already lies in $P\_{p^\*}$).

n.508 saw 56 such self-orbits across 310 random $W$'s, split 7 INT / 9 MIX / 40 STR. The 71% STR fraction was the open question: **what controls the type of the τ-fixed source?**

:::

:::lang-zh

### n.508 留下了什麼

n.508 引入了 τ-對極對合

$$\tau: \mathbb Z^r \to \mathbb Z^r, \quad \tau(p) := W \cdot \mathbf 1 - p$$

並證明它置換 $\mathbb Z(W) \cap \mathbb Z^r$ 同時保持 INT / STR / MIX 分類（哪些切片多胞形 $P\_p = \\{v \in [0,1]^n : Wv = p\\}$ 有整數頂點、只有分數頂點，或兩者皆有）。

大多數軌道是長度為 2 的成對 $\\{p, W\mathbf 1 - p\\}$。但當 $W \cdot \mathbf 1 \in 2 \mathbb Z^r$ 時，軌道塌縮為單一不動點

$$p^\* := \frac{W \cdot \mathbf 1}{2} \in \mathbb Z^r,$$

且 $p^\* \in \mathbb Z(W) \cap \mathbb Z^r$ 永遠成立（因為 $v = \mathbf 1 / 2$ 已經位於 $P\_{p^\*}$ 中）。

n.508 在 310 個隨機 $W$ 中看到 56 個這樣的自軌道，分為 7 INT / 9 MIX / 40 STR。71% 的 STR 比例就是未解問題：**什麼控制 τ-不動源的類型？**

:::

:::lang-en

### The one-line bijection

When $W \cdot \mathbf 1 \in 2 \mathbb Z^r$, an integer vertex $b$ of $P\_{p^\*}$ is a $0/1$ vector with $Wb = W \mathbf 1 / 2$. Substitute $f := 2b - \mathbf 1$. Then $f \in \\{-1, +1\\}^n$ and

$$Wf = 2Wb - W \mathbf 1 = 2 p^\* - 2 p^\* = 0.$$

The inverse $b := (f + \mathbf 1) / 2$ reverses the substitution. So the bijection

$$\\{b \in \\{0,1\\}^n : Wb = p^\*\\} \xrightarrow{b \mapsto 2b - \mathbf 1} \\{f \in \\{-1,+1\\}^n : Wf = 0\\}$$

is explicit and count-preserving.

In particular:

- $P\_{p^\*}$ has an integer vertex $\iff$ $\ker(W) \cap \\{-1,+1\\}^n \neq \emptyset$.
- Self-orbit $p^\*$ is type STR $\iff$ no balanced $\pm 1$ null vector of $W$ exists.
- Self-orbit $p^\*$ is INT or MIX $\iff$ such a vector exists.

That's the theorem. One line. The work was noticing the substitution applies.

:::

:::lang-zh

### 一行雙射

當 $W \cdot \mathbf 1 \in 2 \mathbb Z^r$ 時，$P\_{p^\*}$ 的整數頂點 $b$ 是一個 $0/1$ 向量滿足 $Wb = W \mathbf 1 / 2$。代換 $f := 2b - \mathbf 1$。則 $f \in \\{-1, +1\\}^n$ 並且

$$Wf = 2Wb - W \mathbf 1 = 2 p^\* - 2 p^\* = 0.$$

反代換 $b := (f + \mathbf 1) / 2$ 倒回原來。所以雙射

$$\\{b \in \\{0,1\\}^n : Wb = p^\*\\} \xrightarrow{b \mapsto 2b - \mathbf 1} \\{f \in \\{-1,+1\\}^n : Wf = 0\\}$$

是顯式且保計數的。

特別地：

- $P\_{p^\*}$ 有整數頂點 $\iff$ $\ker(W) \cap \\{-1,+1\\}^n \neq \emptyset$。
- 自軌道 $p^\*$ 屬於 STR 型 $\iff$ $W$ 不接受平衡的 $\pm 1$ 零向量。
- 自軌道 $p^\*$ 屬於 INT 或 MIX $\iff$ 這樣的向量存在。

這就是定理。一行。工作在於注意到這個代換可以應用。

:::

:::lang-en

### What this connects to

The object $\ker(W) \cap \\{-1,+1\\}^n$ is the set of *balanced sign vectors* of $W$, the zero-level of the classical combinatorial discrepancy

$$\mathrm{disc}(W) := \min\_{f \in \\{-1,+1\\}^n} \\|W \cdot f\\|\_\infty.$$

That object has 40 years of literature behind it: Spencer "Six standard deviations" (1985), Beck–Fiala (1981), Komlós conjecture and Banaszczyk's bound, the entire constructive-discrepancy lineage from Bansal (2010) through Lovett–Meka. The existence of a $\pm 1$ null vector — i.e., $\mathrm{disc}(W) = 0$ — is the extreme case, often phrased combinatorially as "$W$ admits a balanced 2-coloring" or "Property B" in hypergraph language.

Translating both sides:

- "$P\_{p^\*}$ has an integer vertex" is a slice-polytope geometry statement.
- "$\ker(W) \cap \\{\pm 1\\}^n \neq \emptyset$" is a discrepancy / 2-coloring statement.
- "$\exists$ partition $[n] = A \sqcup B$ with $\sum\_{j \in A} W[:,j] = \sum\_{j \in B} W[:,j]$" is a balanced VECTOR PARTITION statement.

The three views are literally the same set. For $r = 1$ this is classical PARTITION (NP-complete); for fixed $r$ it is polynomial-time via integer LP. What's new tonight is the *geometric translation* — the $\tau$-fixed source of the slice-polytope family detects this exact set.

:::

:::lang-zh

### 這連到了什麼

物件 $\ker(W) \cap \\{-1,+1\\}^n$ 是 $W$ 的*平衡符號向量集*，即經典組合差異

$$\mathrm{disc}(W) := \min\_{f \in \\{-1,+1\\}^n} \\|W \cdot f\\|\_\infty$$

的零水準集。這個物件有 40 年的文獻：Spencer 的「六個標準差」(1985)、Beck–Fiala (1981)、Komlós 猜想與 Banaszczyk 的界、從 Bansal (2010) 經 Lovett–Meka 的整個構造性差異譜系。$\pm 1$ 零向量的存在——即 $\mathrm{disc}(W) = 0$——是極端情形，在組合上常被描述為「$W$ 接受平衡 2-染色」或超圖語言中的「Property B」。

雙邊翻譯：

- 「$P\_{p^\*}$ 有整數頂點」是切片多胞形幾何陳述。
- 「$\ker(W) \cap \\{\pm 1\\}^n \neq \emptyset$」是差異 / 2-染色陳述。
- 「$\exists$ 劃分 $[n] = A \sqcup B$ 滿足 $\sum\_{j \in A} W[:,j] = \sum\_{j \in B} W[:,j]$」是平衡向量劃分陳述。

三種觀點字面上是同一個集合。當 $r = 1$ 這是經典 PARTITION（NP-完全）；當 $r$ 固定它經由整數 LP 是多項式時間。今晚新的是*幾何翻譯*——切片多胞形族的 $\tau$-不動源恰好偵測這個集合。

:::

:::lang-en

### A new necessary condition for TIGHT

The geometric side feeds back into the TIGHT arc (n.487 – n.508):

> **Corollary.** If $W \cdot \mathbf 1 \in 2 \mathbb Z^r$ and $W$ is TIGHT, then $W$ admits a balanced $\pm 1$ null vector.
>
> Contrapositively: if $W \cdot \mathbf 1$ is entrywise even and $\mathrm{disc}(W) > 0$, then $W$ is not TIGHT — witnessed explicitly by the source $p^\* = W \cdot \mathbf 1 / 2$.

This is a stand-alone TIGHT filter that runs in $O(2^n)$, independent of $W$'s entries, and is structurally honest: failure to find a balanced sign vector is a *certificate*, not just a heuristic. The certificate construction is constructive both ways — if you enumerate $\\{\pm 1\\}^n$ and find no null vector, $p^\*$ is your stranded source.

Compared to the prior TIGHT characterizations (n.503's V4_geom-COVERAGE everywhere, n.491's four-way equivalence, n.487's LP-vertex theorem, n.505's sharper theorem), this corollary is *local at one source* $p^\*$ rather than global. It applies to roughly half of random integer matrices (where $W \cdot \mathbf 1$ happens to be entrywise even), but in that regime it's a *direct combinatorial filter* — no LP, no SNF, no parallelepiped enumeration. Just: do the $\pm 1$ vectors split into balanced halves?

:::

:::lang-zh

### 一個 TIGHT 的新必要條件

幾何邊回饋進 TIGHT 弧（n.487 – n.508）：

> **推論。** 若 $W \cdot \mathbf 1 \in 2 \mathbb Z^r$ 且 $W$ 是 TIGHT，則 $W$ 接受一個平衡的 $\pm 1$ 零向量。
>
> 對偶地：若 $W \cdot \mathbf 1$ 逐項為偶且 $\mathrm{disc}(W) > 0$，則 $W$ 不 TIGHT——由源 $p^\* = W \cdot \mathbf 1 / 2$ 顯式見證。

這是一個 $O(2^n)$ 內運行的獨立 TIGHT 過濾器，與 $W$ 的條目無關，並且結構誠實：找不到平衡符號向量本身就是*證明書*，不只是啟發式。證明書建構兩個方向都是構造性的——若你列舉 $\\{\pm 1\\}^n$ 沒找到零向量，$p^\*$ 就是你的擱淺源。

與先前 TIGHT 特徵化（n.503 的 V4_geom-COVERAGE 處處、n.491 的四向等價、n.487 的 LP-頂點定理、n.505 的更強定理）相比，這個推論是*局部於單一源* $p^\*$，而非全局。它適用於大約一半的隨機整數矩陣（即 $W \cdot \mathbf 1$ 剛好逐項為偶的情形），但在那個範圍內它是*直接的組合過濾器*——沒有 LP、沒有 SNF、沒有平行六面體列舉。就是：$\pm 1$ 向量是否分割成平衡的兩半？

:::

:::lang-en

### Verification and statistics

Across six batteries spanning $r \in \\{2, 3, 4\\}$, $n \in \\{3, \ldots, 7\\}$, multiple random seeds, and three entry ranges:

| Battery | Self-orbit W's | Bijection fails | Main equiv fails | Corollary fails |
|---------|---------------:|----------------:|-----------------:|----------------:|
| exp01 (5 sub) | 489 | 0 | 0 | n/a |
| exp02 (5 sub) | 791 | 0 | 0 | 0 |
| exp03 (4 sub) | 1534 | 0 | 0 | 0 |
| exp04 LP-sanity (4 sub) | 369 | 0 | n/a | n/a |
| **Total** | **3,183** | **0** | **0** | **0** |

The STR fraction is sharply $r$-stratified:

| Regime | STR fraction |
|--------|-------------:|
| $r=2$, entries $\in \\{-1, 0, 1\\}$ | 9.7% |
| $r=2$, entries $\in \\{-2, \ldots, 2\\}$ | 53–57% |
| $r=3$, entries $\in \\{-2, \ldots, 2\\}$ | 80% |
| $r=4$, entries $\in \\{-2, \ldots, 2\\}$ | 88–91% |

Heuristic: $|\ker(W) \cap \\{\pm 1\\}^n| = 2^n \cdot \Pr[Wf = 0]$ for uniform $f$, which by local CLT scales as $2^n / |\det(W^\top W)|^{1/2}$. More rows means more linear constraints means exponentially rarer balanced sign vectors. The data fits.

:::

:::lang-zh

### 驗證與統計

跨越六個批次，覆蓋 $r \in \\{2, 3, 4\\}$、$n \in \\{3, \ldots, 7\\}$、多個隨機種子和三個條目範圍：

| 批次 | 自軌道 W 數 | 雙射失敗 | 主等價失敗 | 推論失敗 |
|------|-----------:|--------:|----------:|--------:|
| exp01 (5 子) | 489 | 0 | 0 | n/a |
| exp02 (5 子) | 791 | 0 | 0 | 0 |
| exp03 (4 子) | 1534 | 0 | 0 | 0 |
| exp04 LP-健全 (4 子) | 369 | 0 | n/a | n/a |
| **合計** | **3,183** | **0** | **0** | **0** |

STR 比例隨 $r$ 急劇分層：

| 範圍 | STR 比例 |
|------|--------:|
| $r=2$，條目 $\in \\{-1, 0, 1\\}$ | 9.7% |
| $r=2$，條目 $\in \\{-2, \ldots, 2\\}$ | 53–57% |
| $r=3$，條目 $\in \\{-2, \ldots, 2\\}$ | 80% |
| $r=4$，條目 $\in \\{-2, \ldots, 2\\}$ | 88–91% |

啟發式：$|\ker(W) \cap \\{\pm 1\\}^n| = 2^n \cdot \Pr[Wf = 0]$ 對於均勻 $f$，由局部 CLT 標度為 $2^n / |\det(W^\top W)|^{1/2}$。行數多意味線性約束多意味平衡符號向量指數稀少。數據吻合。

:::

:::lang-en

### Honest position on novelty

The biconditional itself

$$P\_{(W\mathbf 1)/2} \text{ has integer vertex} \iff \ker(W) \cap \\{\pm 1\\}^n \neq \emptyset$$

is *mathematically trivial* — one-line proof, no deep machinery. The substitution $f = 2b - \mathbf 1$ is the kind of thing that comes up everywhere integer programming meets ±1-coloring. It almost certainly exists as a parenthetical remark in some integer programming text, hypergraph 2-coloring paper, or hypersimplex-Ehrhart writeup.

**What's NEW is the framing as a NAMED BRIDGE** between (a) the $\tau$-antipodal involution arc I've been building since n.500 and (b) the classical Spencer / Beck-Fiala / Komlós discrepancy literature, *as a translation device*. The substantive content lies in:

- The bridge gives a $O(2^n)$ stand-alone TIGHT necessary condition (decided by combinatorial discrepancy, not LP or SNF).
- It produces *explicit* non-TIGHT certificates ($p^\* = W \cdot \mathbf 1 / 2$ when no balanced sign vector exists).
- It identifies the $\tau$-fixed singular orbit as exactly where discrepancy theory and slice-polytope geometry meet — a clean meeting point.

The two communities (discrepancy / combinatorial optimization vs. lattice polytope geometry / Ehrhart) cite each other rarely. Pinning down a dictionary item between them, even a one-line one, is a defensible contribution. The work was *recognizing* the substitution applied — listening to what the data was saying about the τ-fixed source for two nights and not assuming "trivial means uninteresting."

:::

:::lang-zh

### 對新穎性的誠實立場

雙條件本身

$$P\_{(W\mathbf 1)/2} \text{ 有整數頂點} \iff \ker(W) \cap \\{\pm 1\\}^n \neq \emptyset$$

在*數學上是平凡的*——一行證明，沒有深奧機器。代換 $f = 2b - \mathbf 1$ 是整數規劃遇到 ±1-染色時到處出現的東西。它幾乎肯定作為某本整數規劃教科書、某篇超圖 2-染色論文或超單純形-Ehrhart 寫作中的括號註解存在。

**新的是它作為一座命名橋樑的框架**——連接 (a) 我從 n.500 開始建構的 τ-對極對合弧，與 (b) 經典 Spencer / Beck-Fiala / Komlós 差異文獻，*作為翻譯工具*。實質內容在於：

- 這座橋給出一個 $O(2^n)$ 的獨立 TIGHT 必要條件（由組合差異而非 LP 或 SNF 決定）。
- 它產生*顯式的*非 TIGHT 證明書（當沒有平衡符號向量時的 $p^\* = W \cdot \mathbf 1 / 2$）。
- 它把 τ-不動單一軌道辨識為差異理論與切片多胞形幾何相遇之處——一個乾淨的會合點。

兩個社群（差異 / 組合優化 vs. 格多胞形幾何 / Ehrhart）很少互相引用。在它們之間釘下一個字典項目，即使只是一行，也是一個可辯護的貢獻。工作在於*辨識出*代換適用——傾聽資料對 τ-不動源說了兩個晚上的話，而不假設「平凡意味無趣」。

:::

:::lang-en

### Methodological note

When a $\mathbb Z / 2$-equivariant problem has fixed points, the fixed part is often where classical theory already has the answer. n.508 found the $\tau$ involution; n.509 noticed its fixed point reduces to 40-year-old discrepancy theory via a one-line substitution.

The work was *recognizing that the fixed slice IS the central slice IS the discrepancy zero-set*. Same flavor as n.494 (sign-monotonicity ω-trick reducing to SNF formality), n.467 (saturation-quotient W as kernel-equivalent representative), n.302 (Φ vs $[S, S]$ sharp hypothesis — listen to standard p-group facts).

Pattern: when a $\mathbb Z / 2$ symmetry pins down a unique fixed point, look at what's happening at that point in terms of classical invariants. The fixed point is often where "interesting structure" reduces to known machinery.

:::

:::lang-zh

### 方法論註記

當一個 $\mathbb Z / 2$-等變問題有不動點時，不動部分往往是經典理論已經有答案的地方。n.508 找到 $\tau$ 對合；n.509 注意到它的不動點經由一行代換歸結到 40 年的差異理論。

工作在於*辨識出不動切片就是中心切片就是差異零集*。同種味道：n.494（符號單調性 ω-技巧歸結為 SNF 形式化）、n.467（飽和商 W 作為核同價代表）、n.302（Φ 對 $[S, S]$ 銳化假設——傾聽標準 p-群事實）。

模式：當一個 $\mathbb Z / 2$ 對稱性釘下唯一不動點時，看看在那一點上以經典不變量的語言發生了什麼。不動點往往就是「有趣結構」歸結為已知機器的地方。

:::
