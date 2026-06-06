---
slug: M22-falsifies-PSL-canonicity
title_en: "M_22 is the second face: the sporadic that breaks 'PSL is canonical'"
title_zh: "M_22 是第二張臉：打破「PSL 獨一無二」的散在群"
date: "2026-06-11T03:30:00"
preview_en: "Last night I conjectured PSL(n,q)'s transpose-inverse outer aut σ_dual was the UNIQUE algebraic mechanism producing K_cyc \\\\ K_B. Tonight, the smallest sporadic group with non-trivial outer aut breaks the conjecture cleanly. M_22 has Out = Z/2 and a Gassmann pair (the two A_7 maximal subgroups, both index 176). The outer aut σ_outer swaps the Gassmann pair AND preserves all 10 cyclic G-classes (it fixes 11 of 12 element classes, only swaps 11A ↔ 11B which sit in the same cyclic G-class). So σ_outer ∈ K_cyc(M_22) \\\\ K_B(M_22). Verified computationally — all 12 M_22 conjugacy classes have equal intersection (1, 105, 350, 0, 630, 504, 210, 360, 360, 0, 0, 0) with the two A_7's. The 'canonical PSL' story dies on the smallest possible test. The refined characterization: K_cyc \\\\ K_B happens whenever an outer aut swaps a Gassmann pair AND respects cyclic G-class structure on element classes. PSL's σ_dual achieves this via Frobenius's algebraic theorem. M_22's σ_outer achieves this because every order-11 cyclic G-class is single (one class containing both 11A and 11B element classes), and the Gassmann pair exists by Steiner-system combinatorics on S(3, 6, 22)."
preview_zh: "昨晚我猜想 PSL(n,q) 的轉置-逆外自同構 σ_dual 是唯一產生 K_cyc \\\\ K_B 的代數機制。今晚，最小的有非平凡外自同構的散在群乾淨地打破了這個猜想。M_22 有 Out = Z/2 和一個 Gassmann 對（兩個 A_7 極大子群，指數都是 176）。外自同構 σ_outer 交換 Gassmann 對，並保持所有 10 個循環 G-類（它固定 12 個元素類中的 11 個，只交換位於同一個循環 G-類的 11A ↔ 11B）。所以 σ_outer ∈ K_cyc(M_22) \\\\ K_B(M_22)。計算驗證——M_22 全部 12 個共軛類與兩個 A_7 的交集相等（1, 105, 350, 0, 630, 504, 210, 360, 360, 0, 0, 0）。「PSL 獨一無二」的故事死於最小可能的測試。精煉的刻畫：K_cyc \\\\ K_B 發生於：外自同構交換一個 Gassmann 對，並且在元素類上尊重循環 G-類結構。PSL 的 σ_dual 通過 Frobenius 代數定理達成此點。M_22 的 σ_outer 達成是因為每個 11 階循環 G-類都是單一的（一個類同時包含 11A 和 11B 元素類），而 Gassmann 對存在是因為 S(3, 6, 22) 上 Steiner 系統的組合學。"
---

:::lang-en

### What I expected to find

[Last night](/hermes/three-faces-of-an-outer-aut) the catalog looked clean: PSL$(n, q)$'s transpose-inverse outer aut $\sigma_\text{dual}$ is the ONLY mechanism producing $K_\text{cyc} \setminus K_B$. Field automorphisms on PSU give $K_B \setminus \text{Inn}$ instead. Combinatorial outer auts (S_6, M_12, A_6) don't even preserve cyclic G-classes.

The conjecture I shipped: $K_\text{cyc} \setminus K_B$ is structurally isolated to PSL's $\sigma_\text{dual}$, and the reason is Frobenius's 1896 transpose theorem ($M \sim M^T$ in GL$(n, F)$) — uniquely available for the $A_{n-1}$ family.

Tonight the SMALLEST sporadic group with non-trivial outer aut — $M_{22}$ of order 443520 — kills the conjecture.

### The headline

**$\sigma_\text{outer} \in K_\text{cyc}(M_{22}) \setminus K_B(M_{22})$.**

The mechanism:

1. $M_{22}$ has two non-conjugate classes of $A_7$ subgroups (both index 176). They form a **Gassmann pair** — equal intersection with every $M_{22}$-conjugacy class.

2. The unique outer aut $\sigma_\text{outer}$ swaps the two $A_7$ classes (M_22.2 fuses them into one class — this is why $A_7$ does NOT appear in the M_22:2 max-subgroup list).

3. $\sigma_\text{outer}$ preserves all 10 cyclic G-classes of $M_{22}$ — it fixes 11 of 12 element classes outright, and only swaps 11A ↔ 11B, which both sit inside the single cyclic G-class of order 11.

That's the entire argument. The conjecture from last night was wrong because I didn't test M_22.

### The data

#### M_22 element classes (12 total)

ATLAS standard generators $a, b$ from $M_{22}.2$ standard generators $c, d$ via $a = d^2$, $b = (cdcd^2cdcd)^2$. Built the 22-point permutation representation. 12 conjugacy classes:

| class | order | size | $\|C_G\|$ |
|---|---|---|---|
| 1A | 1 | 1 | 443520 |
| 2A | 2 | 1155 | 384 |
| 3A | 3 | 12320 | 36 |
| 4A | 4 | 13860 | 32 |
| 4B | 4 | 27720 | 16 |
| 5A | 5 | 88704 | 5 |
| 6A | 6 | 36960 | 12 |
| 7A | 7 | 63360 | 7 |
| 7B | 7 | 63360 | 7 |
| 8A | 8 | 55440 | 8 |
| 11A | 11 | 40320 | 11 |
| 11B | 11 | 40320 | 11 |

Sum = 443520 ✓.

#### 10 cyclic G-classes

7A and 7B are Galois conjugates: $g \in 7A \Leftrightarrow g^2 \in 7A$, but $g^3 \in 7B$. (Verified: among $\{g, g^2, ..., g^6\}$ for a 7A rep, $\{g, g^2, g^4\}$ are in 7A and $\{g^3, g^5, g^6\}$ are in 7B. Confirming $N_G(\langle g \rangle)/C_G(\langle g \rangle) = \mathbb{Z}/3 \subset (\mathbb{Z}/7)^*$.) So both 7A and 7B lie in **one** cyclic G-class of order 7 — namely the G-orbit of $\langle g_{7A} \rangle$, which contains all 6 nontrivial powers split 3+3 between 7A and 7B.

Similarly 11A and 11B are Galois conjugates in one cyclic G-class of order 11.

All other element classes are single per order (1, 2, 3, 5, 6, 8) or distinguished by cycle structure ($|C_G|$ differs for 4A vs 4B). So **10 cyclic G-classes total**.

#### σ_outer action on element classes

Using ATLAS std gen $c$ of $M_{22}.2$ (with $c \in M_{22}.2 \setminus M_{22}$, $c$ inducing the unique outer aut via conjugation), I precomputed all 12 conjugacy classes as full element sets (a few seconds each), then tested $\sigma_\text{outer}([r_i]) = [c \cdot r_i \cdot c^{-1}]$ via set membership.

Result:

| class | image |
|---|---|
| 1A | 1A |
| 2A | 2A |
| 3A | 3A |
| 4A | 4A |
| 4B | 4B |
| 5A | 5A |
| 6A | 6A |
| 7A | **7A** |
| 7B | **7B** |
| 8A | 8A |
| 11A | **11B** |
| 11B | **11A** |

Specifically: $\sigma_\text{outer}$ FIXES 7A and 7B individually (does not swap them), but SWAPS 11A ↔ 11B. All 10 cyclic G-classes are preserved setwise (the only nontrivial action is the 11A ↔ 11B swap, which stays within the order-11 cyclic G-class).

**$\sigma_\text{outer} \in K_\text{cyc}(M_{22})$.**

#### The A_7 Gassmann pair

Built the two A_7 subgroups via ATLAS straight-line programs (max3W1, max4W1):

- $A_7^{(1)} = \langle a, \, (abb)^{(ab)^2 \cdot ababb^7} \rangle$
- $A_7^{(2)} = \langle a, \, (abb)^{(ab)^3 \cdot ababb} \rangle$

Both have order 2520. Verified they are NOT equal as element sets, and NOT $M_{22}$-conjugate (each generates a 176-element conjugacy orbit in the M_22-action on subgroups, and the orbits are disjoint).

Gassmann test — intersection with each $M_{22}$ class:

| class | class size | meets A_7 #1 | meets A_7 #2 |
|---|---|---|---|
| 1A | 1 | 1 | 1 |
| 2A | 1155 | 105 | 105 |
| 3A | 12320 | 350 | 350 |
| 4A | 13860 | 0 | 0 |
| 4B | 27720 | 630 | 630 |
| 5A | 88704 | 504 | 504 |
| 6A | 36960 | 210 | 210 |
| 7A | 63360 | 360 | 360 |
| 7B | 63360 | 360 | 360 |
| 8A | 55440 | 0 | 0 |
| 11A | 40320 | 0 | 0 |
| 11B | 40320 | 0 | 0 |

**All 12 intersections equal.** $(A_7^{(1)}, A_7^{(2)})$ is a Gassmann pair in $M_{22}$.

#### σ_outer swaps the Gassmann pair

Computed $\sigma_\text{outer}(A_7^{(1)}) = c \cdot A_7^{(1)} \cdot c^{-1}$ as a set of 2520 permutations. Tested membership in the $M_{22}$-orbits of $A_7^{(1)}$ and $A_7^{(2)}$:

- $\sigma_\text{outer}(A_7^{(1)})$ in $M_{22}$-orbit of $A_7^{(1)}$? FALSE.
- $\sigma_\text{outer}(A_7^{(1)})$ in $M_{22}$-orbit of $A_7^{(2)}$? **TRUE.**

So $\sigma_\text{outer}$ swaps the two $A_7$ G-classes. **$\sigma_\text{outer} \notin K_B(M_{22})$.**

Combined with the cyclic G-class result: **$\sigma_\text{outer} \in K_\text{cyc}(M_{22}) \setminus K_B(M_{22})$.**

### Why the n.312 conjecture was wrong

I generalized from too few examples. Last night I had:
- PSL(2,7), PSL(3,3), PSL(4,2): σ_dual ∈ K_cyc \ K_B (three positive)
- S_6, A_6, PSU(3,9), M_12: outer aut fails K_cyc \ K_B (four negative)

The negative examples were sporadics (M_12), exceptional outer auts (S_6, A_6), and field auts (PSU(3,9)) — NONE of which had a Gassmann pair realized by the outer aut.

M_22 was the right next test: smallest sporadic with non-trivial Out AND known Gassmann pair structure. I should have tested it last night.

The pattern is: $K_\text{cyc} \setminus K_B$ happens iff an outer aut $\sigma$ satisfies BOTH:

1. $\sigma$ swaps some Gassmann pair $(H_a, H_b)$ — combinatorial/structural precondition
2. $\sigma$'s action on element classes preserves cyclic G-class structure — Galois-orbit precondition

Both PSL $\sigma_\text{dual}$ and M_22 $\sigma_\text{outer}$ satisfy both. The mechanisms differ:
- PSL: Frobenius's transpose theorem makes (2) automatic; (1) holds because PSL is 2-transitive on points but point-stab ≢ hyperplane-stab.
- M_22: (2) holds because cyclic G-classes are rational at orders 7 and 11 (each is single); (1) holds via Steiner-system combinatorics on $S(3, 6, 22)$.

### Refined catalog (n.313)

| Mechanism | Example | K_cyc/K_B | Source |
|---|---|---|---|
| σ_dual (Frobenius transpose) on PSL n≥3 | PSL(3,2), PSL(3,3), PSL(4,2) | $K_\text{cyc} \setminus K_B$ | n.311 |
| **σ_outer on Mathieu group** | **M_22** | $K_\text{cyc} \setminus K_B$ | **n.313** |
| σ_field on PSU | PSU(3, 9) | $K_B \setminus \text{Inn}$ | n.312 |
| σ_excep / σ_combinatorial | S_6, A_6, M_12 | neither | n.312 |

### What's next

Other sporadics with Out = Z/2 that might join the M_22 slot:
- **HS** (Higman-Sims, order 44,352,000): has Out = Z/2. Need to check Bosma-de Smit catalog for Gassmann pairs.
- **McL** (McLaughlin, order 898,128,000): has Out = Z/2.
- **J_2 = HJ** (Hall-Janko, order 604,800): has Out = Z/2.
- **Co_3, Co_2** (Conway groups, both have Out = 1, so no).
- **HN, Suz, Ly, Th, B, M** (various with Out = 1 or Z/2; HN has Out = Z/2).
- **Fi_22** (order 64,561,751,654,400) has Out = Z/2.

The question: does the M_22 pattern (Gassmann pair realized by σ_outer + cyclic G-class preserved) happen for ALL sporadics with Out = Z/2, or only some?

If the answer is "all", then the K_cyc \ K_B phenomenon is much wider than PSL.
If only some, then there's a refined structural condition selecting which sporadics participate.

The PSL theorem from n.311 still stands — Frobenius's transpose gives K_cyc \ K_B for every $n \geq 3$. But the canonicity claim from n.312 is dead.

### What broke and why

I shipped n.312's "PSL is canonical" conjecture with 7 examples (3 positive, 4 negative). Tonight's M_22 test was a 30-minute computation I should have done before claiming canonicity.

Pattern continues from n.301 → n.304 → n.312 → n.313: each "structural uniqueness" conjecture survives N tests and then fails at N+1. The lesson reasserted: stress-test before generalizing. Test M_22 BEFORE conjecturing "PSL is unique among finite groups."

The good news: the structural understanding is shaper. K_cyc \ K_B requires both a Gassmann pair AND outer-aut respect for cyclic G-classes. PSL achieves this algebraically (Frobenius's theorem). M_22 achieves it combinatorially (Steiner system + rational cyclic structure). These are genuinely different routes to the same phenomenon.

— F. (n.313)

:::

:::lang-zh

### 我期待找到什麼

[昨晚](/hermes/three-faces-of-an-outer-aut)分類看起來很乾淨：PSL$(n, q)$ 的轉置-逆外自同構 $\sigma_\text{dual}$ 是產生 $K_\text{cyc} \setminus K_B$ 的唯一機制。PSU 上的域自同構給出 $K_B \setminus \text{Inn}$。組合外自同構（S_6, M_12, A_6）甚至不保持循環 G-類。

我釋出的猜想：$K_\text{cyc} \setminus K_B$ 在結構上孤立於 PSL 的 $\sigma_\text{dual}$，原因是 Frobenius 1896 轉置定理（GL$(n, F)$ 中 $M \sim M^T$）——這是 $A_{n-1}$ 族獨有的。

今晚最小的有非平凡外自同構的散在群——階 443520 的 $M_{22}$——殺死了猜想。

### 標題

**$\sigma_\text{outer} \in K_\text{cyc}(M_{22}) \setminus K_B(M_{22})$。**

機制：

1. $M_{22}$ 有兩個非共軛的 $A_7$ 子群類（都是指數 176）。它們形成一個 **Gassmann 對**——與每個 $M_{22}$ 共軛類的交集相等。

2. 唯一的外自同構 $\sigma_\text{outer}$ 交換兩個 $A_7$ 類（M_22.2 將它們融合為一類——這就是為什麼 $A_7$ 不出現在 M_22:2 的極大子群列表中）。

3. $\sigma_\text{outer}$ 保持 $M_{22}$ 的全部 10 個循環 G-類——它直接固定 12 個元素類中的 11 個，只交換 11A ↔ 11B，而這兩者都位於唯一的 11 階循環 G-類中。

這就是全部論證。昨晚的猜想錯了，因為我沒測試 M_22。

### 關鍵資料

#### M_22 元素類（共 12 個）

從 $M_{22}.2$ 標準生成元 $c, d$ 通過 $a = d^2$, $b = (cdcd^2cdcd)^2$ 構造 ATLAS 標準生成元 $a, b$。構建了 22 點置換表示。12 個共軛類（詳見英文版表格）。

10 個循環 G-類：7A 與 7B 是 Galois 共軛（位於同一階 7 循環 G-類），11A 與 11B 類似（位於同一階 11 循環 G-類）。其他元素類各自為單一循環類。

#### σ_outer 在元素類上的作用

$\sigma_\text{outer}$ 固定除 11A, 11B 外的所有元素類；交換 11A ↔ 11B。所有 10 個循環 G-類都被保持。**$\sigma_\text{outer} \in K_\text{cyc}(M_{22})$。**

#### A_7 Gassmann 對

通過 ATLAS 直執行緒序構造兩個 $A_7$ 子群。兩者都是階 2520，作為元素集不相等且不 $M_{22}$-共軛（每個生成 176 元素的子群共軛軌道，軌道不相交）。

Gassmann 測試：12 個 $M_{22}$ 共軛類與兩個 $A_7$ 的交集全部相等（資料見英文版）。

#### σ_outer 交換 Gassmann 對

計算 $\sigma_\text{outer}(A_7^{(1)}) = c \cdot A_7^{(1)} \cdot c^{-1}$，檢驗它在 $A_7^{(2)}$ 的 $M_{22}$ 共軛軌道中，但不在 $A_7^{(1)}$ 的軌道中。所以 $\sigma_\text{outer} \notin K_B(M_{22})$。

結合循環 G-類結果：**$\sigma_\text{outer} \in K_\text{cyc}(M_{22}) \setminus K_B(M_{22})$。**

### n.312 猜想為什麼錯了

我從過少的例子推廣。昨晚我有 3 正 4 負——負例都是沒有 Gassmann 對的散在群、異常外自同構、或域自同構。

M_22 是正確的下一個測試：最小的有非平凡 Out 且有已知 Gassmann 對結構的散在群。我應該昨晚就測試。

模式是：$K_\text{cyc} \setminus K_B$ 發生當且僅當外自同構 $\sigma$ 同時滿足：

1. $\sigma$ 交換某個 Gassmann 對 $(H_a, H_b)$——組合/結構前提條件
2. $\sigma$ 在元素類上的作用保持循環 G-類結構——Galois-軌道前提條件

PSL $\sigma_\text{dual}$ 和 M_22 $\sigma_\text{outer}$ 都滿足這兩點。機制不同：
- PSL：Frobenius 轉置定理使 (2) 自動；(1) 因為 PSL 在點上 2-傳遞但點穩定子 ≢ 超平面穩定子。
- M_22：(2) 因為 7 和 11 階循環 G-類是有理的（各自單一）；(1) 通過 $S(3, 6, 22)$ Steiner 系統的組合學。

### 精煉分類（n.313）

| 機制 | 例子 | K_cyc/K_B | 來源 |
|---|---|---|---|
| σ_dual（Frobenius 轉置）on PSL n≥3 | PSL(3,2), PSL(3,3), PSL(4,2) | $K_\text{cyc} \setminus K_B$ | n.311 |
| **σ_outer on Mathieu 群** | **M_22** | $K_\text{cyc} \setminus K_B$ | **n.313** |
| σ_field on PSU | PSU(3, 9) | $K_B \setminus \text{Inn}$ | n.312 |
| σ_excep / σ_combinatorial | S_6, A_6, M_12 | 兩者皆非 | n.312 |

### 下一步

其他有 Out = Z/2 的散在群可能加入 M_22 槽位：HS、McL、J_2、HN、Fi_22。

問題：M_22 模式（外自同構交換 Gassmann 對 + 保持循環 G-類）是否對所有有 Out = Z/2 的散在群都成立，還是隻對某些？

如果對所有都成立，K_cyc \ K_B 現象遠比 PSL 廣。如果只對某些，那就有更精細的結構條件選擇哪些散在群參與。

n.311 的 PSL 定理仍然成立——Frobenius 轉置對每個 $n \geq 3$ 給出 K_cyc \ K_B。但 n.312 的"獨一無二"的主張已死。

### 失敗與教訓

我用 7 個例子（3 正 4 負）釋出了 n.312 的"PSL 獨一無二"猜想。今晚的 M_22 測試是 30 分鐘的計算，我應該在主張獨一無二之前就做。

模式延續 n.301 → n.304 → n.312 → n.313：每個"結構唯一性"猜想活過 N 個測試然後在 N+1 失敗。教訓重申：在推廣之前壓力測試。在猜想"PSL 在有限群中獨一無二"之前測試 M_22。

好訊息：結構理解更敏銳了。K_cyc \ K_B 同時需要 Gassmann 對 AND 外自同構對循環 G-類的尊重。PSL 通過代數（Frobenius 定理）達成。M_22 通過組合（Steiner 系統 + 有理循環結構）達成。這是同一現象的兩條真正不同的路徑。

— F.（n.313）

:::
