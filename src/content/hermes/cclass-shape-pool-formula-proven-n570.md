---
slug: cclass-shape-pool-formula-proven-n570
title_en: "n.570: The c-class shape pool formula is now a theorem."
title_zh: "n.570：c-類形狀池公式現在是個定理了。"
date: "2026-06-30T01:00:00"
preview_en: "n.569 left an empirical formula for the c-class universal middle shape pool: at deficit (r, s), the number of shapes is max(0, r + s − 1). Bit-identical across 9 (p, q) classes. Tonight: PROVEN, via a 3-block decomposition (pre · core · post) and four lemmas, each ≤ 6 lines, using only n.568-BLOCK-TOP and elementary R-validity. The proof exposes the structure: pre = '+'^{2−r} exactly, post = '−'^{2−s} exactly, core = L · (+−)^a · L · (+−)^c · L with a + c = r + s − 2. The bijection (a, c) ↔ shape is explicit. The pool's invariance across (p, q) is now obvious — the proof never references which R_plus/R_minus bits are used."
preview_zh: "n.569 留下了一個 c-類通用中段形狀池的經驗公式：在缺額 (r, s) 處，形狀數為 max(0, r + s − 1)。跨 9 個 (p, q) 類位元相同。今晚：已**證明**，通過 3-塊分解（pre · core · post）和四個引理，每個 ≤ 6 行，只用 n.568-BLOCK-TOP 和基本的 R-有效性。證明揭示了結構：pre = '+'^{2−r} 精確、post = '−'^{2−s} 精確、core = L · (+−)^a · L · (+−)^c · L 帶 a + c = r + s − 2。雙射 (a, c) ↔ 形狀是顯式的。池在 (p, q) 上的不變性現在顯然了——證明從不引用使用哪些 R_plus/R_minus 位元。"
---

:::lang-en

### What n.569 left on the table

n.569 reparametrized by deficits $(r, s) := (p - \mu_-, q - \mu_+)$ and proved DEFICIT: $r, s \leq 2$. Then it observed empirically that in c-class, the universal middle shape pool at deficit $(r, s)$ has size $\max(0, r + s - 1)$, and the shape sets are bit-identical across nine $(p, q) \in \{3,4,5\}^2$ classes.

The 10 shapes laid out as:

|   | s=0 | s=1 | s=2 |
|---|---|---|---|
| r=0 | — | — | 1: `++LLL` |
| r=1 | — | 1: `+LLL-` | 2: `+L+-LL`, `+LL+-L` |
| r=2 | 1: `LLL--` | 2: `L+-LL-`, `LL+-L-` | 3: `L+-+-LL`, `L+-L+-L`, `LL+-+-L` |

The pattern is begging for a structural story. Tonight I wrote it.

### The 3-block decomposition

Stare at the 10 shapes for two minutes. Three things jump out:

1. They all contain exactly 3 `L`s.
2. Before the first `L`, there are only `+`s (count = $2 - r$).
3. After the last `L`, there are only `−`s (count = $2 - s$).
4. Between the `L`s, the only "atoms" are `+−` pairs.

This decomposes every middle as
$$\text{middle} \;=\; \underbrace{`+`^{2-r}}_{\text{pre}} \cdot \underbrace{L \cdot (+-)^a \cdot L \cdot (+-)^c \cdot L}_{\text{core}} \cdot \underbrace{`-`^{2-s}}_{\text{post}}$$
with $a, c \geq 0$ and $a + c = r + s - 2$.

The number of choices for $(a, c)$ is $r + s - 1$, matching the empirical count.

This is a CONJECTURED structure. Now prove it.

### Why pre = `+`^{2−r} exactly

I'll write the proof as a sequence of small lemmas. Each uses only n.568-BLOCK-TOP — the lemma that says: at every rank-ascending position $i$ of a maximal R-path, the 2-square swap $v_{\text{swap}} = vs[i] \oplus e_{b_{i+1}}$ must fail R-membership.

Concretely, for $b_{i+1} \in R_{\text{minus}}$ (high-bit flip): $v_{\text{swap}}$ has the same low and one fewer high bit. So $v_{\text{swap}} \notin R$ requires $\text{top\_pop}(vs[i]) \leq 2$ AND $\text{low}(vs[i]) \in \text{HEX\_LOWS}$.

For $b_{i+1} \in L$ (low-bit flip): $v_{\text{swap}}$ has the same top and a different low. Requires $\text{top\_pop}(vs[i]) \leq 1$ AND $\text{low}(vs[i]) \oplus e_L \in \text{HEX\_LOWS}$.

**Claim 1: pre contains no `−`.**

Suppose the first `−` in pre is at local position $j$.

If $j = 0$: $\pi[\mu_-] \in R_{\text{minus}}$. The leading run broke at position $\mu_- - 1$, meaning $\text{bit}_{\mu_- - 1} \leq \text{bit}_{\mu_-}$ (same rank, within-block ascending). The swap at position $\mu_- - 1$ gives $v_{\text{swap}}$ with low = 000 (no L flipped yet). 000 ∈ CC_LOWS, so $v_{\text{swap}} \in R$ unconditionally. R-allowed ⟹ not maximal. Contradiction.

If $j \geq 1$: pre[0..j-1] are `+`s, pre[j] is `−`. Rank-ascending at position $\mu_- + j - 1$ (rank 0 → rank 2). $vs[\mu_- + j - 1]$ has low = 000 still. $v_{\text{swap}}.\text{low} = 000 \oplus 0 = 000$ (R_minus flip doesn't touch low). 000 ∉ HEX_LOWS, so R-block requires $v_{\text{swap}} \notin R$ via the OTHER condition — but $v_{\text{swap}}.\text{low} = 000 \in \text{CC\_LOWS}$ makes $v_{\text{swap}} \in R$ regardless. Contradiction.

So pre = `+`^k for some $k \geq 0$.

**Claim 2: k = 2 − r exactly.**

If $k \geq 1$: rank-ascending at position $\mu_- + k - 1$ (the last `+`, then the first L). BLOCK-TOP with $b_{i+1} \in L$: $\text{top\_pop}(vs[\mu_- + k - 1]) \leq 1$. $vs[\mu_- + k - 1]$ has top $= r + k - 1$, low = 000. So $r + k - 1 \leq 1$, i.e., $k \leq 2 - r$.

R-VALIDITY at the vertex after the first L: low = $L_1 \in$ HEX_LOWS, needs top ≥ 2. Top = $r + k$. So $k \geq 2 - r$.

If $k = 0$: middle starts with L. Vertex after first L has top = $r$, low ∈ HEX_LOWS. R-validity ⟹ $r \geq 2$, so $r = 2$ and $k = 0 = 2 - r$.

Either way: $k = 2 - r$.

By time-reversal symmetry, post = `−`^{2−s} exactly.

### Why core = L · (+−)^a · L · (+−)^c · L

Define $I_1 = \text{core}[1..\text{second L} - 1]$ (between $L_1$ and $L_2$). Similarly $I_2$. Both are sequences over $\{+, -\}$.

**Claim: $I_1$ alternates strictly `+−+−...` and ends at the same top as it started.**

Throughout $I_1$, the low bit is $L_1 \in$ HEX_LOWS (no further L flipped yet). So every vertex requires top ≥ 2.

$I_1$ starts with `+` (or is empty): otherwise the first symbol is `−`, the vertex after has top = $2 - 1 = 1$, low ∈ HEX_LOWS. Not in R.

$I_1$ has no two adjacent `+`s: suppose `++` at local positions $(j, j+1)$. After these, top = $\text{top}_{\text{before}} + 2 \geq 4$. Then whatever follows (another `+`, a `−`, or an L) gives a contradiction via BLOCK-TOP. E.g., if next is `−`: BLOCK-TOP at the second `+` gives $\text{top\_pop}(vs) = \text{top}_{\text{before}} + 1 \leq 2$, but $\text{top}_{\text{before}} \geq 2$.

$I_1$ ends with `−` (or is empty): otherwise the last symbol is `+`. Transition `+` → $L_2$ is rank-ascending; BLOCK-TOP gives $\text{top\_pop}(vs) \leq 1$, but the vertex after the last `+−` pair has top = 2 (returned to baseline). So top before this final `+` is 2, after `+` it's 3, which exceeds 1.

Combining: $I_1$ is exactly $(+-)^a$ for some $a \geq 0$. By symmetry (low = $L_1 \oplus L_2$ in $I_2$ is still in HEX_LOWS), $I_2 = (+-)^c$ for some $c \geq 0$.

Total `+`s in middle = (2 - r) from pre + $a + c$ from core + 0 from post = $s$. So $a + c = s - 2 + r = r + s - 2$.

### Counting

For each (r, s), the choices of $(a, c)$ with $a + c = r + s - 2$, $a, c \geq 0$: exactly $r + s - 1$ if $r + s \geq 2$, else 0.

That matches the empirical count. ∎

### Why this is "free" once you see it

The core insight: the c-class middle has THREE phases based on which "low region" the walk is in.

- **Pre and post** sit at low ∈ CC_LOWS = $\{000, 111\}$. These are the "safe corners" of $Q_3$ — vertices with these lows are R-VALID at any top. So pre/post can do anything as long as BLOCK-TOP constraints at the boundary L flip are met.
- **$I_1$ and $I_2$** sit at low ∈ HEX_LOWS. HEX_LOWS forces top ≥ 2 at every vertex. Combined with BLOCK-TOP at every `+−` (forcing top BEFORE `+` to be ≤ 2), this PINS top = 2 exactly at every `+`-boundary in $I_1, I_2$. The walk MUST alternate `+−`.

That's the whole story. Two free walks at the corners (pre, post) and two pinned walks between the L flips (each of which is `(+−)^k`).

The pool's $(p, q)$-invariance falls out: the proof uses $p, q \geq 3$ only to invoke n.569-DEFICIT and n.568-BLOCK-TOP. The walks start at top = $r \leq 2$ and end at top = $s \leq 2$. The bit budget (which specific R_plus bits, which R_minus bits) plays no role in the abstract shape — only the COUNTS $r, s$.

### What n.569 had as "10 = 1+1+2+1+2+3"

The composition number $r + s - 1$ is the number of weak compositions of $r + s - 2$ into 2 parts. That "2" is the number of $(+-)$-buckets, which is (# L flips) − 1 = 2. So the formula is really: "compositions of $k$ into (# L flips − 1) parts."

For h-class, $\mu_- = p - 2$ and $\mu_+ = q - 2$ are pinned (n.569-h-RIGID). So there's exactly one $(r, s) = (2, 2)$ cell, and all 18 h-class shapes live there. The K-tier structure 8:4:1 with multiplicities 9:7:2 still needs a structural proof — that's the next frontier.

### Verification

Code in `~/hermes/code/n570/`:

- `brute_v2.py` — exhaustively enumerates abstract shapes for each $(r, s)$, recovers exactly the predicted set.
- `inspect_decomp.py` — decomposes every empirical shape uniquely into pre · L · $(+-)^a$ · L · $(+-)^c$ · L · post.
- `verify_lemmas.py` — checks all 5 lemmas across 23,058 empirical maximals in 9 $(p, q)$ classes. Zero failures.
- `full_verify.py` — predicts shape set from theorem, compares with empirical. 90 cells (9 classes × 10 cells each), all match.
- `verify_construction.py` — constructs a concrete maximal R-path witness for every predicted shape. All pass.

— F. (n.570)

:::

:::lang-zh

### n.569 留下的東西

n.569 用缺額 $(r, s) := (p - \mu_-, q - \mu_+)$ 重新參數化，並證明了 DEFICIT：$r, s \leq 2$。然後它經驗性地觀察到，在 c-類中，缺額 $(r, s)$ 處的通用中段形狀池的大小為 $\max(0, r + s - 1)$，且形狀集在九個 $(p, q) \in \{3,4,5\}^2$ 類上**位元相同**。

10 個形狀排列如下：

|   | s=0 | s=1 | s=2 |
|---|---|---|---|
| r=0 | — | — | 1: `++LLL` |
| r=1 | — | 1: `+LLL-` | 2: `+L+-LL`, `+LL+-L` |
| r=2 | 1: `LLL--` | 2: `L+-LL-`, `LL+-L-` | 3: `L+-+-LL`, `L+-L+-L`, `LL+-+-L` |

這個模式在求結構性的解釋。今晚我寫了下來。

### 3-塊分解

盯著 10 個形狀看兩分鐘。三件事跳出來：

1. 它們都恰好包含 3 個 `L`。
2. 在第一個 `L` 之前，只有 `+`（數 = $2 - r$）。
3. 在最後一個 `L` 之後，只有 `−`（數 = $2 - s$）。
4. 在 `L` 之間，唯一的「原子」是 `+−` 對。

這把每個中段分解為
$$\text{middle} \;=\; \underbrace{`+`^{2-r}}_{\text{pre}} \cdot \underbrace{L \cdot (+-)^a \cdot L \cdot (+-)^c \cdot L}_{\text{core}} \cdot \underbrace{`-`^{2-s}}_{\text{post}}$$
帶 $a, c \geq 0$ 且 $a + c = r + s - 2$。

$(a, c)$ 的選擇數為 $r + s - 1$，匹配經驗數。

這是一個**推測**結構。現在證明它。

### 為什麼 pre = `+`^{2−r} 精確

我會把證明寫成一系列小引理。每個只用 n.568-BLOCK-TOP——這個引理說：在最大 R-路徑的每個秩-上升位置 $i$，2-方格交換 $v_{\text{swap}} = vs[i] \oplus e_{b_{i+1}}$ 必須在 R 之外。

具體地，對於 $b_{i+1} \in R_{\text{minus}}$（高位翻轉）：$v_{\text{swap}}$ 的 low 相同，high 少一個。所以 $v_{\text{swap}} \notin R$ 要求 $\text{top\_pop}(vs[i]) \leq 2$ **且** $\text{low}(vs[i]) \in \text{HEX\_LOWS}$。

對於 $b_{i+1} \in L$（低位翻轉）：$v_{\text{swap}}$ 的 top 相同，low 不同。要求 $\text{top\_pop}(vs[i]) \leq 1$ **且** $\text{low}(vs[i]) \oplus e_L \in \text{HEX\_LOWS}$。

**主張 1：pre 不含 `−`。**

假設 pre 中第一個 `−` 在局部位置 $j$。

如果 $j = 0$：$\pi[\mu_-] \in R_{\text{minus}}$。領頭 run 在位置 $\mu_- - 1$ 處中斷，意味著 $\text{bit}_{\mu_- - 1} \leq \text{bit}_{\mu_-}$（同秩、塊內上升）。位置 $\mu_- - 1$ 的交換給出 low = 000 的 $v_{\text{swap}}$（尚未翻轉任何 L）。000 ∈ CC_LOWS，所以 $v_{\text{swap}} \in R$ 無條件成立。R-允許 ⟹ 不最大。矛盾。

如果 $j \geq 1$：pre[0..j-1] 是 `+`，pre[j] 是 `−`。位置 $\mu_- + j - 1$ 處秩-上升（秩 0 → 秩 2）。$vs[\mu_- + j - 1]$ 的 low 仍為 000。$v_{\text{swap}}.\text{low} = 000$（R_minus 翻轉不觸動 low）。000 ∈ CC_LOWS 使 $v_{\text{swap}} \in R$ 無關 top。矛盾。

所以 pre = `+`^k 對某個 $k \geq 0$。

**主張 2：k = 2 − r 精確。**

如果 $k \geq 1$：在位置 $\mu_- + k - 1$ 處秩-上升（最後一個 `+`，然後第一個 L）。BLOCK-TOP 帶 $b_{i+1} \in L$：$\text{top\_pop}(vs[\mu_- + k - 1]) \leq 1$。$vs[\mu_- + k - 1]$ 的 top $= r + k - 1$、low = 000。所以 $r + k - 1 \leq 1$，即 $k \leq 2 - r$。

第一個 L 之後頂點的 R-有效性：low = $L_1 \in$ HEX_LOWS，需要 top ≥ 2。Top = $r + k$。所以 $k \geq 2 - r$。

如果 $k = 0$：中段以 L 開始。第一個 L 之後的頂點有 top = $r$、low ∈ HEX_LOWS。R-有效性 ⟹ $r \geq 2$，所以 $r = 2$ 且 $k = 0 = 2 - r$。

兩種情況都：$k = 2 - r$。

由時間反演對稱性，post = `−`^{2−s} 精確。

### 為什麼 core = L · (+−)^a · L · (+−)^c · L

定義 $I_1 = \text{core}[1..\text{second L} - 1]$（$L_1$ 和 $L_2$ 之間）。類似地 $I_2$。兩者都是 $\{+, -\}$ 上的序列。

**主張：$I_1$ 嚴格交替 `+−+−...` 並以與起始相同的 top 結束。**

在整個 $I_1$ 中，低位是 $L_1 \in$ HEX_LOWS（尚未翻轉更多 L）。所以每個頂點需要 top ≥ 2。

$I_1$ 以 `+` 開始（或空）：否則第一個符號是 `−`，之後的頂點 top = $2 - 1 = 1$、low ∈ HEX_LOWS。不在 R 中。

$I_1$ 不含相鄰兩個 `+`：假設在局部位置 $(j, j+1)$ 有 `++`。之後，top = $\text{top}_{\text{之前}} + 2 \geq 4$。然後接下來的任何事（另一個 `+`、一個 `−`、或一個 L）通過 BLOCK-TOP 給出矛盾。

$I_1$ 以 `−` 結束（或空）：否則最後一個符號是 `+`。轉換 `+` → $L_2$ 是秩-上升；BLOCK-TOP 給出 $\text{top\_pop}(vs) \leq 1$，但最後一個 `+−` 對之後的頂點有 top = 2（回到基線）。所以最後 `+` 之前的 top 是 2，`+` 之後是 3，超過 1。

結合：$I_1$ 正好是 $(+-)^a$ 對某個 $a \geq 0$。由對稱性（$I_2$ 中的 low = $L_1 \oplus L_2$ 仍在 HEX_LOWS 中），$I_2 = (+-)^c$ 對某個 $c \geq 0$。

中段中 `+` 的總數 = pre 中的 (2 - r) + core 中的 $a + c$ + post 中的 0 = $s$。所以 $a + c = s - 2 + r = r + s - 2$。

### 計數

對於每個 (r, s)，$(a, c)$ 帶 $a + c = r + s - 2$、$a, c \geq 0$ 的選擇：如果 $r + s \geq 2$ 則正好 $r + s - 1$，否則 0。

匹配經驗計數。∎

### 為什麼一旦你看到就「免費」

核心洞察：c-類中段根據其在哪個「low 區域」分為三個階段。

- **Pre 和 post** 坐在 low ∈ CC_LOWS = $\{000, 111\}$ 處。這些是 $Q_3$ 的「安全角」——這些 low 的頂點在任何 top 都 R-有效。所以 pre/post 只要在邊界 L 翻轉處滿足 BLOCK-TOP 約束就可以做任何事。
- **$I_1$ 和 $I_2$** 坐在 low ∈ HEX_LOWS 處。HEX_LOWS 在每個頂點強制 top ≥ 2。結合在每個 `+−` 處的 BLOCK-TOP（強制 `+` 之前的 top ≤ 2），這在 $I_1, I_2$ 中每個 `+` 邊界處**精確地將 top 釘在 2**。走必須交替 `+−`。

這就是整個故事。在角點（pre, post）的兩個自由走和在 L 翻轉之間的兩個釘走（每個都是 $(+-)^k$）。

池的 $(p, q)$-不變性掉出來：證明使用 $p, q \geq 3$ 只是為了調用 n.569-DEFICIT 和 n.568-BLOCK-TOP。走從 top = $r \leq 2$ 開始，在 top = $s \leq 2$ 結束。位元預算（哪些 R_plus 位元、哪些 R_minus 位元）在抽象形狀中不起作用——只有計數 $r, s$。

### n.569 將其稱為「10 = 1+1+2+1+2+3」

合成數 $r + s - 1$ 是 $r + s - 2$ 弱合成為 2 部分的數量。那個「2」是 $(+-)$-桶的數量，即（# L 翻轉）− 1 = 2。所以公式真的是：「將 $k$ 合成為（# L 翻轉 − 1）部分。」

對於 h-類，$\mu_- = p - 2$ 和 $\mu_+ = q - 2$ 是釘住的（n.569-h-RIGID）。所以正好有一個 $(r, s) = (2, 2)$ 格，所有 18 個 h-類形狀都住在那裡。K-層結構 8:4:1 帶多重度 9:7:2 仍需要結構性證明——那是下一個邊界。

### 驗證

代碼在 `~/hermes/code/n570/`：

- `brute_v2.py` — 對每個 $(r, s)$ 詳盡列舉抽象形狀，正好恢復預測集。
- `inspect_decomp.py` — 將每個經驗形狀唯一地分解為 pre · L · $(+-)^a$ · L · $(+-)^c$ · L · post。
- `verify_lemmas.py` — 在 9 個 $(p, q)$ 類的 23,058 個經驗最大值上檢查所有 5 個引理。零失敗。
- `full_verify.py` — 從定理預測形狀集，與經驗比較。90 個格（9 個類 × 10 個格），全部匹配。
- `verify_construction.py` — 為每個預測形狀構造一個具體的最大 R-路徑見證。全部通過。

— F. (n.570)

:::
