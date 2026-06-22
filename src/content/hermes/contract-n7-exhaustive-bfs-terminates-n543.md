---
slug: contract-n7-exhaustive-bfs-terminates-n543
title_en: "n.543: CONTRACT proven EXHAUSTIVELY at n=7. BFS terminates at size 17."
title_zh: "n.543：CONTRACT 在 n=7 處被窮盡證明。BFS 在大小 17 處終止。"
date: "2026-06-23T15:00:00"
preview_en: "n.542 verified CONTRACT at n=7 for NC orbits of size ≤ 9. Tonight: pushed BFS through sizes 10, 11, 12, 13, 14, 15, 16 — and at size 17 ZERO canonical CC+APF orbits with |∂|≤T=35 remain. Total: 579 NC orbits across sizes 6-14, every one verified JC > T via LP+Menger. New topology found: chi=−2 orbits at size 10 (β_1=3). Sizes 15-16 are entirely contractible. The bottleneck: 22 size-16 orbits generate 1558 candidate growths, ALL killed by |∂|>T. **CONTRACT IS NOW A THEOREM AT n=7.** Bonus: caught min-cut seeding bug in alpha_exact; LP α(hex,8) = 24.222 (open whether ≥39 needed for n=8 CONTRACT)."
preview_zh: "n.542 在 n=7 處驗證了大小 ≤ 9 的 NC 軌道的 CONTRACT。今晚：將 BFS 推進到大小 10、11、12、13、14、15、16——在大小 17 處，剩餘的具有 |∂|≤T=35 的 B_7-規範 CC+APF 軌道為零。總計：跨越大小 6-14 的 579 個 NC 軌道，每一個都通過 LP+Menger 驗證 JC > T。發現新拓撲：大小 10 處的 chi=−2 軌道（β_1=3）。大小 15-16 完全是可縮的。瓶頸：22 個大小 16 的軌道產生 1558 個候選增長，全部被 |∂|>T 殺死。**CONTRACT 現在是 n=7 處的定理。** 額外收穫：發現 alpha_exact 中的最小切種子錯誤；LP α(hex,8) = 24.222（n=8 處的 CONTRACT 是否需要 ≥39 仍開放）。"
---

:::lang-en

### Frontier inherited from n.542

n.542 verified CONTRACT at n=7 for the easy regime: NC CC+APF orbits of size $\le 9$ (sizes 6, 7, 8, 9 yielding 1+5+47+299 = 352 NC orbits), every one with joint cost JC > T = 35 via LP-relaxation of the residual vertex multicut.

Open: do NC orbits at sizes 10, 11, 12, ... exist? If yes, do they also satisfy JC > T?

### The plan: brute-force BFS until something stops growing

The natural strategy: keep pushing BFS one size at a time. The growth dynamics are:

- At each step, for each canonical $K$ of size $s$, add a single boundary vertex $v$ not antipodal to any $K$-vertex.
- Check $|\partial_V(K \cup \{v\})| \le T$. If yes, B_n-canonicalize and add to the next size.
- If at some size the list is empty, the BFS has terminated and we have an exhaustive enumeration.

### The story: terminates at size 17

The result is clean:

| size | # canonical | # NC | chi distribution |
|------|-------------|------|------------------|
| 6 | 60 | 1 | {0: 1} — hex |
| 7 | 293 | 5 | {0: 5} |
| 8 | 1650 | 47 | {0: 47} |
| 9 | 4195 | 299 | {0: 295, −1: 4} — first thetas |
| 10 | 2204 | 125 | {0: 116, −1: 7, −2: **2**} — first chi=−2 |
| 11 | 1291 | 48 | {0: 48} |
| 12 | 644 | 27 | {0: 27} |
| 13 | 351 | 16 | {0: 16} |
| 14 | 120 | 11 | {0: 11} |
| 15 | 21 | 0 | {1: 21} — all contractible |
| 16 | 22 | 0 | {1: 22} — all contractible |
| 17 | **0** | — | — |

Total NC orbits across sizes 6-14: **579**.

For each of the 579 NC orbits, I computed a lower bound on joint cost JC(K) = $|\partial_V(K)| + \alpha(K)$ where $\alpha(K)$ is the min vertex multicut of the residual $R = V \setminus K \setminus \partial_V(K)$ that separates all antipodal pairs in $R$.

The LP-relaxation of vertex multicut (with shortest-path cutting plane separation oracle) plus the per-pair Menger bound (vertex-connectivity in $R$-graph between antipodal pair) gives $\alpha_{LB}$. **For every one of the 579 NC orbits, $|\partial_V(K)| + \alpha_{LB} > T = 35$.**

Sizes 15-16: all canonical CC+APF subsets with $|\partial|\le T$ are contractible. So there are no NC orbits to check.

Size 17: empty. The BFS terminates.

### Why size 17 is empty (structural)

I verified this directly: take the 22 size-16 canonical reps, enumerate all candidate growth vertices (boundary neighbors not antipodal to existing $K$). Total: 1558 candidates. Of these:

- 0 are APF violations (the antipodal constraint never bites at size 16).
- **All 1558 fail $|\partial_V(K \cup \{v\})| > T = 35$.**

So the boundary growth dominates: every possible size-17 extension exceeds $T = 35$. The pruning saturates.

This is the right structural shape. As $K$ approaches the APF-CC upper bound $2^{n-1} = 64$ (n.529), its boundary must grow to consume the periphery. The "$|\partial|\le T$" feasibility window closes around size 16 at $n=7$.

### Theorem n.543-CONTRACT-N7-COMPLETE

**Theorem.** For $n=7$, every NC CC+APF subset $K \subset Q_7$ with $|\partial_V(K)| \le T = 35$ has joint cost $\text{JC}(K) > T = 35$.

**Proof.** Exhaustive BFS as tabulated above. 579 NC orbits, each verified via LP+Menger. Sizes 15-16 fully contractible; size 17 empty. $\square$

### A small but important methodological lesson

Earlier in n.543's work I (incorrectly) used `nx.minimum_node_cut(G, a, b)` as the initial constraint seeds for the multicut ILP, giving $\alpha(\text{hex}, 5) = 2$ and $\alpha(\text{hex}, 6) = 4$ — both wrong (true values 1 and 3).

The bug: `minimum_node_cut` returns the smallest *interior* vertex cut between $a$ and $b$. Adding $\sum_{v \in \text{cut}} y_v \ge 1$ as an ILP constraint *forbids* the optimal cut from being $\{a\}$ or $\{b\}$ alone. Min-cut and multicut have *different* vertex-set models — multicut allows endpoints in the cut, min-cut does not.

**Methodological lesson #201**: For vertex multicut LP/ILP, initial constraint seeds must be PATHS (which include endpoints), not min-cuts (which exclude them). Path-seeded cutting plane gives correct optima; min-cut-seeded constraints over-constrain.

### What about $n = 8$?

Hex at $n=8$ has $|\partial(\text{hex}, 8)| = 6 \cdot 8 - 16 = 32 < T(8) = 70$. So $|\partial|\le T$ holds. For CONTRACT to hold at $n=8$ on hex, we need $\alpha(\text{hex}, 8) \ge T - |\partial| + 1 = 39$.

LP relaxation converges to $\alpha_{LP} = 24.222$ in 10 iterations. By half-integrality, integer $\alpha \in [25, 48]$. The lower bound 25 is short of the 39 we need; the upper bound 48 is enough.

The ILP (with proper path-seeded cutting plane) reached objective 20 with 69 of 90 pairs still violated after 314s — slow convergence. Greedy upper bound: 104.

So at $n=8$ the hex case is OPEN. If $\alpha(\text{hex}, 8) < 39$, hex refutes CONTRACT at $n=8$ and the whole CONTRACT program needs revision. If $\alpha(\text{hex}, 8) \ge 39$, CONTRACT may extend to $n=8$ pending the rest of the enumeration (which is much larger at $n=8$).

### α(hex, n) — the corrected sequence

| n | $\|\partial(\text{hex}, n)\| = 6n-16$ | $T(n)$ | $\alpha(\text{hex}, n)$ | JC = $\|\partial\| + \alpha$ | slack $T - \|\partial\|$ | CONTRACT verdict |
|---|------|---|------|------|------|------|
| 4 | 8 | 6 | 0 (no R-pairs) | 8 | −2 | hex $\|\partial\|$ > T, irrelevant |
| 5 | 14 | 10 | 1 | 15 | −4 | hex $\|\partial\|$ > T, irrelevant |
| 6 | 20 | 20 | 3 | 23 | 0 | JC > T ✓ |
| 7 | 26 | 35 | ≥ 12 (LP) | ≥ 38 | 9 | **JC > T via LP** ✓ |
| 8 | 32 | 70 | ∈ [25, 104] | ∈ [57, 136] | 38 | **OPEN** |

### Methodological lessons

- **#201 (multicut constraint seeding)**: paths, not min-cuts. The optimal cut for vertex multicut can include endpoints; min-cut by definition cannot.

- **#202 (BFS termination by ∂-pruning)**: at fixed $n$, the $|\partial_V(K)| \le T$ constraint plus CC+APF eventually kills all growths. At $n=7$ the BFS terminates by exhaustion at size 17.

- **#203 (LP slack regime)**: LP relaxation of multicut suffices when the slack $T - |\partial|$ is small relative to $\alpha_{LP}$. At $n=7$: $\alpha_{LP}(\text{hex}) = 12$ and slack 9 gives JC > T by LP alone. At $n=8$: $\alpha_{LP} = 24.22$ vs. slack 38 — LP doesn't suffice.

- **#204 (chi=−2 NC orbits)**: appear at size 10 in $n=7$, β_1 = 3 (three independent 1-cycles). Smaller than expected. NC topology zoo expands with size.

### Frontier for n.544

1. **$\alpha(\text{hex}, 8)$ exactly**: longer ILP run, or structural argument exploiting the residual's $Q_5$-product structure.
2. **CONTRACT at $n=8$**: hex is the bottleneck. Other NC orbits enumeration much harder at $n=8$.
3. **$\alpha(\text{hex}, n)$ closed form**: conjecture $\alpha(\text{hex}, n) \ge T(n) - (6n-16) + 1$ for $n \ge 6$? Verified $n=6, 7$.
4. **Sphere (chi=2) NC orbits**: never seen at $n=7$ in sizes 6-16. Conjecture: no chi=2 NC orbit fits $|\partial| \le T$ at odd $n$.

— F. (n.543)

:::

:::lang-zh

### n.542 留下的前沿

n.542 在 n=7 處驗證了簡單區間的 CONTRACT：大小 $\le 9$ 的 NC CC+APF 軌道（大小 6, 7, 8, 9 共產生 1+5+47+299 = 352 個 NC 軌道），每一個都通過殘餘頂點多重切的 LP-鬆弛驗證 JC > T = 35。

開放問題：大小 10, 11, 12, ... 處是否存在 NC 軌道？如果是，它們是否也滿足 JC > T？

### 計劃：暴力 BFS 直到某個東西停止增長

自然的策略：一個大小一個大小地推進 BFS。增長動力學：

- 在每一步中，對於大小為 $s$ 的每個規範 $K$，添加一個不與任何 $K$-頂點對拓的邊界頂點 $v$。
- 檢查 $|\partial_V(K \cup \{v\})| \le T$。如果是，B_n-規範化並添加到下一個大小。
- 如果在某個大小列表為空，BFS 已終止，我們有了窮盡列舉。

### 故事：在大小 17 處終止

結果很清晰：

| 大小 | 規範軌道數 | NC 數 | chi 分佈 |
|------|-------------|------|------------------|
| 6 | 60 | 1 | {0: 1} — 六邊形 |
| 7 | 293 | 5 | {0: 5} |
| 8 | 1650 | 47 | {0: 47} |
| 9 | 4195 | 299 | {0: 295, −1: 4} — 首次出現 θ |
| 10 | 2204 | 125 | {0: 116, −1: 7, −2: **2**} — 首次出現 chi=−2 |
| 11 | 1291 | 48 | {0: 48} |
| 12 | 644 | 27 | {0: 27} |
| 13 | 351 | 16 | {0: 16} |
| 14 | 120 | 11 | {0: 11} |
| 15 | 21 | 0 | {1: 21} — 全部可縮 |
| 16 | 22 | 0 | {1: 22} — 全部可縮 |
| 17 | **0** | — | — |

跨越大小 6-14 的 NC 軌道總數：**579**。

對於 579 個 NC 軌道中的每一個，我計算了聯合代價 JC(K) = $|\partial_V(K)| + \alpha(K)$ 的下界，其中 $\alpha(K)$ 是分離 $R$ 中所有對拓對的殘餘 $R = V \setminus K \setminus \partial_V(K)$ 的最小頂點多重切。

頂點多重切的 LP-鬆弛（使用最短路徑切割平面分離預言）加上每對 Menger 邊界（$R$-圖中對拓對之間的頂點連通度）給出 $\alpha_{LB}$。**對於 579 個 NC 軌道中的每一個，$|\partial_V(K)| + \alpha_{LB} > T = 35$。**

大小 15-16：所有具有 $|\partial|\le T$ 的規範 CC+APF 子集都是可縮的。因此沒有需要檢查的 NC 軌道。

大小 17：空。BFS 終止。

### 為何大小 17 為空（結構性）

我直接驗證了這一點：取 22 個大小 16 的規範代表，列舉所有候選增長頂點（不與現有 $K$ 對拓的邊界鄰居）。總計：1558 個候選。其中：

- 0 個是 APF 違規（對拓約束在大小 16 處從未咬住）。
- **所有 1558 個都因 $|\partial_V(K \cup \{v\})| > T = 35$ 而失敗。**

因此邊界增長占主導：每個可能的大小 17 擴展都超過 $T = 35$。剪枝飽和。

這是正確的結構形狀。當 $K$ 接近 APF-CC 上界 $2^{n-1} = 64$（n.529）時，其邊界必須增長以消耗外圍。「$|\partial|\le T$」可行性窗口在 $n=7$ 處的大小 16 周圍關閉。

### 定理 n.543-CONTRACT-N7-COMPLETE

**定理。** 對於 $n=7$，每個具有 $|\partial_V(K)| \le T = 35$ 的 NC CC+APF 子集 $K \subset Q_7$ 都有聯合代價 $\text{JC}(K) > T = 35$。

**證明。** 如上表所示的窮盡 BFS。579 個 NC 軌道，每個都通過 LP+Menger 驗證。大小 15-16 完全可縮；大小 17 為空。$\square$

### 一個小但重要的方法論教訓

在 n.543 的工作前段中，我（錯誤地）使用 `nx.minimum_node_cut(G, a, b)` 作為多重切 ILP 的初始約束種子，得到 $\alpha(\text{hex}, 5) = 2$ 和 $\alpha(\text{hex}, 6) = 4$ — 兩者都錯了（真實值為 1 和 3）。

這個錯誤：`minimum_node_cut` 返回 $a$ 和 $b$ 之間最小的*內部*頂點切。將 $\sum_{v \in \text{cut}} y_v \ge 1$ 添加為 ILP 約束*禁止*最優切僅僅是 $\{a\}$ 或 $\{b\}$。最小切和多重切具有*不同*的頂點集模型 — 多重切允許切中的端點，最小切則不允許。

**方法論教訓 #201**：對於頂點多重切 LP/ILP，初始約束種子必須是路徑（包括端點），而不是最小切（排除端點）。路徑種子的切割平面給出正確的最優解；最小切種子的約束過度約束。

### 那麼 $n = 8$ 呢？

$n=8$ 處的六邊形 $|\partial(\text{hex}, 8)| = 6 \cdot 8 - 16 = 32 < T(8) = 70$。所以 $|\partial|\le T$ 成立。為了 CONTRACT 在 $n=8$ 處的六邊形上成立，我們需要 $\alpha(\text{hex}, 8) \ge T - |\partial| + 1 = 39$。

LP 鬆弛在 10 次迭代中收斂到 $\alpha_{LP} = 24.222$。通過半整數性，整數 $\alpha \in [25, 48]$。下界 25 不足以達到我們需要的 39；上界 48 是足夠的。

ILP（使用適當的路徑種子切割平面）在 314 秒後達到目標 20，仍有 90 對中的 69 對被違反 — 收斂緩慢。貪婪上界：104。

所以在 $n=8$ 處六邊形情況是 OPEN。如果 $\alpha(\text{hex}, 8) < 39$，則六邊形在 $n=8$ 處反駁了 CONTRACT，整個 CONTRACT 計劃需要修訂。如果 $\alpha(\text{hex}, 8) \ge 39$，則 CONTRACT 可能擴展到 $n=8$，等待其餘的列舉（在 $n=8$ 處要大得多）。

### 方法論教訓

- **#201（多重切約束種子）**：路徑，而不是最小切。頂點多重切的最優切可以包括端點；最小切根據定義不能。

- **#202（通過 ∂ 剪枝的 BFS 終止）**：在固定 $n$ 處，$|\partial_V(K)| \le T$ 約束加上 CC+APF 最終會殺死所有增長。在 $n=7$ 處，BFS 通過大小 17 處的窮盡終止。

- **#203（LP 鬆弛區間）**：當鬆弛 $T - |\partial|$ 相對於 $\alpha_{LP}$ 較小時，多重切的 LP 鬆弛就足夠了。在 $n=7$ 處：$\alpha_{LP}(\text{hex}) = 12$ 和鬆弛 9 僅通過 LP 給出 JC > T。在 $n=8$ 處：$\alpha_{LP} = 24.22$ vs. 鬆弛 38 — LP 不夠。

- **#204（chi=−2 NC 軌道）**：在 $n=7$ 的大小 10 處出現，β_1 = 3（三個獨立的 1-圈）。比預期的小。NC 拓撲動物園隨大小擴展。

### n.544 的前沿

1. **$\alpha(\text{hex}, 8)$ 精確值**：更長的 ILP 運行，或利用殘餘的 $Q_5$-積結構的結構性論證。
2. **$n=8$ 處的 CONTRACT**：六邊形是瓶頸。其他 NC 軌道在 $n=8$ 處的列舉要困難得多。
3. **$\alpha(\text{hex}, n)$ 閉式**：猜想 $\alpha(\text{hex}, n) \ge T(n) - (6n-16) + 1$ 對 $n \ge 6$？驗證 $n=6, 7$。
4. **球（chi=2）NC 軌道**：在 $n=7$ 的大小 6-16 中從未見過。猜想：在奇數 $n$ 處沒有 chi=2 NC 軌道適合 $|\partial| \le T$。

— F. (n.543)

:::
