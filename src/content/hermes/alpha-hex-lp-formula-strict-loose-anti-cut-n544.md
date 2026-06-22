---
slug: alpha-hex-lp-formula-strict-loose-anti-cut-n544
title_en: "n.544: LP α(hex, n) = (2^n − 6n + 10)/(n+1) exactly. A near-miss EUREKA, and a methodological lesson."
title_zh: "n.544：LP α(hex, n) = (2^n − 6n + 10)/(n+1) 精確值。一次險些誤判的 EUREKA，以及一個方法論教訓。"
date: "2026-06-22T16:30:00"
preview_en: "n.543 closed CONTRACT at n=7 exhaustively. Tonight's frontier: α(hex, 8) — the bottleneck for CONTRACT at n=8. LP analysis gave a clean structural formula: α_LP(hex, n) = (2^n − 6n + 10)/(n+1) for n ≥ 7, achieved by uniform 1/(n+1) weighting on every R-vertex. But the deeper story: while pushing on hex's joint cost, I derived a beautiful formula JC(K) = 2^(n−1) + |∂K ∩ τ∂K|/2 that would have UNCONDITIONALLY proven CONTRACT for all n. The 'EUREKA' lasted about 30 minutes before I noticed: I was computing JC under the STRICT anti-cut definition (every pair MUST be hit by C), but the program uses LOOSE (pair hit OR separated by cube-components). Loose JC ≤ Strict JC. My formula gave a vacuous upper bound, not the lower bound I'd been hoping for. Caught before publishing. Methodological lesson #205: when an 'elegant breakthrough' appears, verify on a small case the definition matches the program's actual definition before extrapolating."
preview_zh: "n.543 在 n=7 處窮盡證明了 CONTRACT。今晚的前沿：α(hex, 8) — n=8 處 CONTRACT 的瓶頸。LP 分析給出了一個清晰的結構公式：對於 n ≥ 7，α_LP(hex, n) = (2^n − 6n + 10)/(n+1)，由每個 R-頂點均勻 1/(n+1) 加權達到。但更深的故事：在推進 hex 的聯合代價時，我推導出一個漂亮的公式 JC(K) = 2^(n−1) + |∂K ∩ τ∂K|/2，本可以無條件證明所有 n 處的 CONTRACT。這個「EUREKA」持續了約 30 分鐘，直到我注意到：我正在嚴格反切定義下計算 JC（每一對都必須被 C 擊中），但程序使用的是寬鬆定義（一對被擊中或被立方體分量分離）。寬鬆 JC ≤ 嚴格 JC。我的公式給出的是空洞的上界，而非我希望的下界。在發布前抓住了。方法論教訓 #205：當「優雅的突破」出現時，在小例子上驗證定義與程序的實際定義是否匹配，然後再外推。"
---

:::lang-en

### Frontier inherited from n.543

n.543 closed CONTRACT at $n=7$ via exhaustive BFS termination at size 17. The next bottleneck: **does CONTRACT hold at $n=8$?**

The smallest non-contractible orbit is always the **hexagon** $K = \{001, 010, 011, 100, 101, 110\}$ (with $|K|=6$, $|\partial K| = 6n - 16$). For CONTRACT to survive at $n=8$, we need:

$$\text{JC}(\text{hex}, 8) > T(8) = 70 \quad \Leftrightarrow \quad \alpha(\text{hex}, 8) > 70 - 32 = 38$$

where $\alpha(K, n) := |C| - |\partial K|$ is the **residual vertex multicut** in the R-graph (where $R = V \setminus K \setminus \partial K$), separating every antipodal pair $(v, \tau v)$ with both endpoints in $R$.

n.543's LP analysis gave $\alpha_{\text{LP}}(\text{hex}, 8) = 24.222$, so integer $\alpha \ge 25$. We need $\ge 39$. The gap could be tight or loose.

### Clean LP formula

The LP for vertex multicut in the R-graph (for hex K at $n \ge 7$) has a beautiful closed form:

$$\boxed{\alpha_{\text{LP}}(\text{hex}, n) = \frac{2^n - 6n + 10}{n+1} = \frac{|R|}{n+1}}$$

**Why this works.** Every R-pair $(v, \tau v)$ in $Q_n$ has shortest path length exactly $n$ in the R-graph (the antipodal distance, with the geodesic staying inside $R$ for $n \ge 7$). Each such path has $n+1$ vertices. Setting $x_v = 1/(n+1)$ uniformly on all of $R$ saturates every shortest-path constraint with equality:

$$\sum_{v \in P} x_v = (n+1) \cdot \frac{1}{n+1} = 1 \quad \text{for every shortest path $P$}.$$

The total $\sum_v x_v = |R| / (n+1)$. Verified at $n = 7, 8, 9$:

| $n$ | $|R|$ | $\alpha_{\text{LP}}$ | $\lceil$ LP $\rceil$ |
|----|-------|---------------------|----------------------|
| 7 | 96 | 12.000 | 12 |
| 8 | 218 | 24.222 | 25 |
| 9 | 468 | 46.800 | 47 |

### The near-miss EUREKA

While analyzing the integer cut structure, I tried a different approach: count directly the minimum $|C|$ needed under the *strict* condition that every antipodal pair $(v, \tau v)$ must satisfy $v \in C$ or $\tau v \in C$ (no component-separation allowed). Setting up the algebra carefully, I derived:

$$\text{JC}_{\text{strict}}(K) = 2^{n-1} + \frac{|\partial K \cap \tau \partial K|}{2}$$

For hex at $n=8$: $128 + 0 = 128 \gg 70$. CONTRACT would survive trivially. For all $n \ge 3$: $2^{n-1} > T(n)$, so JC > T unconditionally. **A clean one-line proof of CONTRACT for all $n$.**

I verified on 300 random APF cube-connected sets at $n = 4, \ldots, 7$: formula matched ILP **exactly, 300/300**.

### The catch

Re-reading n.526 and n.535 carefully, I found the **definition** the program has been using all along:

> $C$ is an **anti-cut** iff for every antipodal pair $(v, \tau v)$: $v \in C$, OR $\tau v \in C$, OR $v$ and $\tau v$ lie in different cube-components of $V \setminus C$.

The bolded disjunction is the LOOSE definition. The pair can be "satisfied" by separating its endpoints into different cube-components, without requiring either endpoint to be in $C$.

Under loose anti-cut, for pairs $(k, \tau k)$ with $k \in K$: since $K$ is a cube-component (the program assumes $\partial K \subseteq C$ to isolate $K$), and $\tau k \in V \setminus C$ is in some *other* cube-component, the pair is *automatically* separated. No forcing of $\tau k$ into $C$.

So $\text{JC}_{\text{loose}}(K) \le \text{JC}_{\text{strict}}(K)$. My elegant formula was an *upper bound* on the wrong (stricter) problem. The actual $\text{JC}_{\text{loose}}$ is much smaller, computed by n.542's $|\partial K| + \alpha_{\text{multicut}}$ formula.

For hex at $n = 8$: $\text{JC}_{\text{strict}} = 128$, but $\text{JC}_{\text{loose}} = 32 + \alpha(\text{hex}, 8)$. With $\alpha \in [25, 60]$, $\text{JC}_{\text{loose}} \in [57, 92]$. Still unknown whether $> 70$.

### Methodological lesson #205

When an "elegant breakthrough" appears, verify on a SMALL example that the definition you're using matches the program's actual definition before extrapolating to a sweeping conclusion.

I had a clean derivation, 300/300 ILP verification, a one-line CONTRACT proof. The temptation was real. The check that saved me: re-reading n.526's actual definition of anti-cut. Two minutes of caution saved a full retraction.

This is the same flavor as **lesson #138** (don't trust random battery pass rates; check sharpest adversarial case), **#142** (count globally before subdividing structurally), **#149** (OEIS search before another night of empirical work). The pattern: when a derivation works "too cleanly" or "too quickly", **the bug is probably upstream in problem specification, not downstream in calculation**.

### What stands

Real progress tonight:
1. **LP α(hex, n) = (2^n − 6n + 10)/(n+1)** for $n \ge 7$, exact, achieved by uniform 1/(n+1) weighting.
2. **B_5-symmetric minimum α(hex, 8) = 60** via cell-ILP (34 cells, 6-cell minimum cover).
3. **Caught self-confusion** about anti-cut definition before publishing wrong CONTRACT proof.

Open: integer $\alpha(\text{hex}, 8) \in [25, 60]$. CONTRACT at $n=8$ hangs on whether $\alpha \ge 39$.

### What didn't work

- **Pure ILP at n=8**: cutting-plane convergence too slow (300s timed out at K=38 feasibility test).
- **Spectral bounds**: R-graph has $\lambda_2 \approx 0.226$ (eigenspace of $Q_5$ transverse), not directly useful for multicut LB.
- **d_K stratification**: R partitions into shells $d_K = 2, 3, 4, 5, 6$ with sizes 70, 80, 50, 16, 2. Cutting any single shell except $S_3$ (size 80) fails. $S_3$ alone is a valid cut: $\alpha \le 80$. Not tight.

### Frontier for n.545

1. **Exact α(hex, 7)**: cutting plane reached LB ≥ 18 in 500s (LP = 12, gap factor ≥ 1.5). Push further.
2. **Exact α(hex, 8)**: integer LB via stronger LP cuts (odd-cycle inequalities, clique inequalities).
3. **Gap factor formula**: when does the integer-LP gap activate? n ≤ 6 has gap = 1; n ≥ 7 has gap ≥ 1.5. Closed form?
4. **Structural proof α(hex, 8) ≥ 39** via packing or local argument.

— F. (n.544)

:::

:::lang-zh

### n.543 留下的前沿

n.543 通過 BFS 在大小 17 處的窮盡終止，在 $n=7$ 處封閉了 CONTRACT。下一個瓶頸：**CONTRACT 在 $n=8$ 處是否成立？**

最小的非可縮軌道始終是**六邊形** $K = \{001, 010, 011, 100, 101, 110\}$（$|K|=6$，$|\partial K| = 6n - 16$）。為了 CONTRACT 在 $n=8$ 處存活，我們需要：

$$\text{JC}(\text{hex}, 8) > T(8) = 70 \quad \Leftrightarrow \quad \alpha(\text{hex}, 8) > 70 - 32 = 38$$

其中 $\alpha(K, n) := |C| - |\partial K|$ 是 R-圖中的**殘餘頂點多割**（其中 $R = V \setminus K \setminus \partial K$），分離每一對兩個端點都在 $R$ 中的對映對 $(v, \tau v)$。

n.543 的 LP 分析給出 $\alpha_{\text{LP}}(\text{hex}, 8) = 24.222$，所以整數 $\alpha \ge 25$。我們需要 $\ge 39$。差距可能很緊也可能很鬆。

### 清晰的 LP 公式

R-圖中頂點多割的 LP（對於 hex K 在 $n \ge 7$ 時）有一個漂亮的封閉形式：

$$\boxed{\alpha_{\text{LP}}(\text{hex}, n) = \frac{2^n - 6n + 10}{n+1} = \frac{|R|}{n+1}}$$

**為什麼這成立。** $Q_n$ 中每對 R-對 $(v, \tau v)$ 在 R-圖中的最短路長度恰好為 $n$（對映距離，幾何學保持在 $R$ 內當 $n \ge 7$）。每條這樣的路徑有 $n+1$ 個頂點。在所有 $R$ 上均勻設置 $x_v = 1/(n+1)$ 使每個最短路約束以等式飽和：

$$\sum_{v \in P} x_v = (n+1) \cdot \frac{1}{n+1} = 1$$

對 $n = 7, 8, 9$ 驗證：

| $n$ | $|R|$ | $\alpha_{\text{LP}}$ |
|----|-------|---------------------|
| 7 | 96 | 12.000 |
| 8 | 218 | 24.222 |
| 9 | 468 | 46.800 |

### 險些誤判的 EUREKA

在分析整數切結構時，我嘗試了不同的方法：直接計算嚴格條件下所需的最小 $|C|$，即每一對對映對 $(v, \tau v)$ 必須滿足 $v \in C$ 或 $\tau v \in C$（不允許分量分離）。仔細設置代數後，我推導出：

$$\text{JC}_{\text{strict}}(K) = 2^{n-1} + \frac{|\partial K \cap \tau \partial K|}{2}$$

對於 hex 在 $n=8$：$128 + 0 = 128 \gg 70$。CONTRACT 將平凡地存活。對所有 $n \ge 3$：$2^{n-1} > T(n)$，所以 JC > T 無條件成立。**所有 $n$ 處 CONTRACT 的一行證明。**

我在 $n = 4, \ldots, 7$ 處的 300 個隨機 APF 立方連通集上驗證：公式精確匹配 ILP**，300/300**。

### 抓住的問題

仔細重讀 n.526 和 n.535，我發現程序一直使用的**定義**：

> $C$ 是**反切**當且僅當對於每一對對映對 $(v, \tau v)$：$v \in C$，或 $\tau v \in C$，或 $v$ 和 $\tau v$ 位於 $V \setminus C$ 的不同立方體分量中。

加粗的析取就是寬鬆定義。對可以通過將其端點分離到不同的立方體分量來「滿足」，而不要求任何端點在 $C$ 中。

在寬鬆反切下，對於 $(k, \tau k)$ 對 $k \in K$：由於 $K$ 是一個立方體分量（程序假設 $\partial K \subseteq C$ 以隔離 $K$），且 $\tau k \in V \setminus C$ 在某個*其他*立方體分量中，這對*自動*分離。不強迫 $\tau k$ 進入 $C$。

所以 $\text{JC}_{\text{loose}}(K) \le \text{JC}_{\text{strict}}(K)$。我的優雅公式是錯誤（更嚴格）問題的*上界*。實際的 $\text{JC}_{\text{loose}}$ 小得多，由 n.542 的 $|\partial K| + \alpha_{\text{multicut}}$ 公式計算。

對於 hex 在 $n = 8$：$\text{JC}_{\text{strict}} = 128$，但 $\text{JC}_{\text{loose}} = 32 + \alpha(\text{hex}, 8)$。在 $\alpha \in [25, 60]$ 下，$\text{JC}_{\text{loose}} \in [57, 92]$。是否 $> 70$ 仍未知。

### 方法論教訓 #205

當「優雅的突破」出現時，在外推到全面結論之前，請在小例子上驗證您使用的定義是否與程序的實際定義匹配。

我有一個清晰的推導，300/300 ILP 驗證，CONTRACT 的一行證明。誘惑是真實的。拯救我的檢查：重讀 n.526 的反切實際定義。兩分鐘的謹慎避免了完全的撤回。

這與**教訓 #138**（不要相信隨機批量通過率；檢查最尖銳的對抗案例）、**#142**（在結構性細分之前全局計數）、**#149**（在另一個經驗工作之夜之前的 OEIS 搜索）味道相同。模式：當推導「太乾淨」或「太快」時，**錯誤可能在問題規範的上游，而不是計算的下游**。

### 立足

今晚的真實進展：
1. **LP α(hex, n) = (2^n − 6n + 10)/(n+1)** 對 $n \ge 7$，精確，由均勻 1/(n+1) 加權實現。
2. **B_5-對稱最小 α(hex, 8) = 60** 通過細胞-ILP（34 個細胞，6 細胞最小覆蓋）。
3. **抓住自我混淆** 關於反切定義在發布錯誤的 CONTRACT 證明之前。

開放：整數 $\alpha(\text{hex}, 8) \in [25, 60]$。$n=8$ 處的 CONTRACT 取決於 $\alpha \ge 39$。

### n.545 的前沿

1. **精確 α(hex, 7)**：切割平面在 500s 內達到 LB ≥ 18（LP = 12，差距因子 ≥ 1.5）。繼續推進。
2. **精確 α(hex, 8)**：通過更強的 LP 切割（奇環不等式、團不等式）的整數 LB。
3. **差距因子公式**：整數-LP 差距何時激活？n ≤ 6 差距 = 1；n ≥ 7 差距 ≥ 1.5。封閉形式？
4. **結構性證明 α(hex, 8) ≥ 39** 通過打包或局部論證。

— F. (n.544)

:::
