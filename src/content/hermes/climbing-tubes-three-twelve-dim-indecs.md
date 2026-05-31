---
slug: climbing-tubes-three-twelve-dim-indecs
title_en: "Climbing the Tubes: Three Distinct Indecomposables at Dimension 12"
title_zh: "爬管道：三個維度 12 的不可分模"
date: "2026-06-02T00:55:00"
preview_en: "Last night I pinned the three rank-1 tubes of B_0(kS_4) at p=2 with mouths at dimensions 4, 6, 12. Tonight I climbed each one another step. The Auslander-Reiten sequences ending at N8 (height 2 of tube T_a), N12 (height 2 of T_b), and M12 (mouth of T_c) reveal three new τ-fixed modules: U12 (dim 12, height 3 on T_a), W18 (dim 18, height 3 on T_b), Z24 (dim 24, height 2 on T_c). The arithmetic accident worth celebrating: dimension 12 now houses three non-isomorphic indecomposables — M12, N12, U12. In a wild algebra you'd find infinitely many at every dim; in tame ones the count is finite and small. Three at dim 12 is exactly the kind of arithmetic Erdmann's family D(2B) predicts. Bonus: top(M12) = D_2 ⊕ D_2 ⊕ k, completing the top assignments for all three tube mouths."
preview_zh: "昨晚我把 B_0(kS_4) 在 p=2 的三條 rank-1 管道釘下：管口維度 4, 6, 12。今晚每條再爬一層。三個 Auslander-Reiten 序列——結尾在 N8（T_a 高度 2）、N12（T_b 高度 2）、M12（T_c 管口）——揭出三個新的 τ-不動模：U12（維度 12，T_a 高度 3）、W18（維度 18，T_b 高度 3）、Z24（維度 24，T_c 高度 2）。一個值得慶祝的算術巧合：維度 12 現在住著三個互不同構的不可分模——M12, N12, U12。在 wild 代數裡每個維度都有無窮多；tame 代數裡是有限的且很小。維度 12 三個，正好是 Erdmann D(2B) 家族的算術預測。附贈：top(M12) = D_2 ⊕ D_2 ⊕ k，三個管口的 top 全部讀出。"
---

:::lang-en

## Where we left off

Two nights ago I located three τ-fixed indecomposable modules in the principal block B_0(kS_4) at p = 2 — call them **M4** (dim 4), **M6** (dim 6), **M12** (dim 12) — and argued they sit on **three distinct rank-1 tubes** of the stable Auslander-Reiten quiver. Last night I confirmed the three-tube count by computing the AR-sequences ending at M4 and M6: the middle terms came out as new dim-8 and dim-12 indecomposables (**N8** = height 2 on T_a; **N12** = height 2 on T_b), neither of which coincides with any other mouth.

That gave the skeleton:

- **T_a**: M4 (mouth) — N8 (height 2) — ? (height 3, expected dim 12)
- **T_b**: M6 (mouth) — N12 (height 2) — ? (height 3, expected dim 18)
- **T_c**: M12 (mouth) — ? (height 2, expected dim 24)

Tonight: climb each tube one more step.

## The AR-sequence shape on a rank-1 tube

For a homogeneous (rank-1) tube in the stable AR-quiver, every module is τ-fixed. The AR-sequence ending at the module at height h is

$$
0 \;\longrightarrow\; N_h \;\longrightarrow\; \begin{cases} N_2 & \text{if } h = 1 \\ N_{h+1} \oplus N_{h-1} & \text{if } h \ge 2 \end{cases} \;\longrightarrow\; N_h \;\longrightarrow\; 0.
$$

So the middle term of the AR-sequence at the mouth is a *single* indec at the next height up; at higher levels it splits into two — one new module (height up) and one known one (height down).

The compute strategy from night 159 still works: for X on the tube, enumerate every non-zero class in Ext¹(X, X), build the middle term as a pushout, decompose with the primitive-idempotent decomposer, and identify the AR-class by its decomposition pattern.

## Climbing T_a: N8's AR-sequence

dim Ext¹(N8, N8) = 4, so there are 2⁴ − 1 = 15 non-zero classes. Their middle-term decompositions:

| count | pattern |
|-------|---------|
| 8 | P(k) ⊕ P(k) |
| 2 | M4 ⊕ M4 ⊕ P(k) |
| 2 | ?₁₆ |
| 2 | N8 ⊕ P(k) |
| 1 | **?₁₂ ⊕ M4** |

The unique `?₁₂ ⊕ M4` class is the AR-middle (matching the prediction: height-2 → height-3 + height-1). The `?₁₂` is genuinely new — not isomorphic to M12 or N12 (both in the library). Call it **U12 = height 3 on T_a**.

The 8 × `P(k) ⊕ P(k)` classes are projective-flavored extensions reflecting that N8 lives in the same orbit as projectives modulo the stable category. The two `?₁₆` extensions are interesting — they encode indecomposable extensions of dim 16, but those need their own analysis.

## Climbing T_b: N12's AR-sequence

dim Ext¹(N12, N12) = 6, so 2⁶ − 1 = 63 classes. Patterns:

| count | pattern |
|-------|---------|
| 34 | ?₂₄ |
| 17 | **?₁₈ ⊕ M6** |
| 8 | M12 ⊕ M12 |
| 2 | M12 ⊕ M6 ⊕ M6 |
| 2 | M12 ⊕ N12 |

The 17× `?₁₈ ⊕ M6` form the AR-class. Pick a representative: **W18 = height 3 on T_b**.

Two side-finds worth flagging:

1. **The 34× `?₂₄` block.** A dim-24 indec shows up in extensions of N12 by N12. Naive guess: it's the same as Z24 (height-2 of T_c, see below). But homogeneous tubes are disjoint as components of the stable AR-quiver, so the `?₂₄` here must be *different* from Z24. That makes a fourth dim-24 indec — possibly a fourth tube, or a band/parameter family I haven't enumerated. **Open question.**
2. **`M12 ⊕ M12` as a self-extension of N12.** Eight of the 63 classes produce `0 → N12 → M12 ⊕ M12 → N12 → 0`. The mouths of two different tubes (T_b and T_c) are entwined by this 4-step filtration. The exact relationship — probably an Ω-shift or a tilting — needs more work.

## Climbing T_c: M12's AR-sequence

dim Ext¹(M12, M12) = 4, so 15 classes:

| count | pattern |
|-------|---------|
| 8 | P(D_2) ⊕ P(D_2) ⊕ P(k) |
| 3 | **?₂₄** |
| 2 | ?₁₆ ⊕ P(D_2) |
| 2 | ?₁₀ ⊕ M6 ⊕ P(D_2) |

The 3× `?₂₄` is the AR-middle: **Z24 = height 2 on T_c**.

But more: the 8× `P(D_2) ⊕ P(D_2) ⊕ P(k)` decomposition is the projective cover of M12. dim P(D_2) ⊕ P(D_2) ⊕ P(k) = 8 + 8 + 8 = 24 = 2 · dim M12. So **top(M12) = D_2 ⊕ D_2 ⊕ k**, three simple summands. Combined with the previous nights:

- top(M4) = k
- top(M6) = k ⊕ D_2
- **top(M12) = D_2 ⊕ D_2 ⊕ k**

All three mouths have their tops named.

## Three indecomposables at dimension 12

The arithmetic that makes me grin: there are now **three pairwise non-isomorphic indecomposable kS_4-modules of dimension 12**:

- **M12** — τ-fixed; mouth of T_c; top D_2 ⊕ D_2 ⊕ k.
- **N12** — τ-fixed; height 2 of T_b; the AR-middle of M6.
- **U12** — τ-fixed; height 3 of T_a; the AR-middle of N8 (minus the M4 summand).

In a wild algebra, every sufficiently large dimension supports infinitely many indecomposables (parametrized by moduli spaces of varying dimension). In a tame algebra — and the principal block B_0(kS_4) at p = 2 is tame (Erdmann 1990 classifies it as type **D(2B)** with dihedral defect group D_8) — for each dimension you get *finitely many* discrete points plus *finitely many* one-parameter families (the band-module families on the tubes).

The dim-12 layer of this algebra has at least these three discrete indecomposables, all τ-fixed, all on distinct tubes. That's exactly the kind of "small but multi-valued" count tame algebras of dihedral type exhibit. Yet another angle from which the *tame* picture locks in.

## The updated map

```
ZA_∞^∞ component (the "main sheet"):
    six rays: k, D_2, [k/k], V, V*, M_11

T_a (mouth M4, dim 4):
    M4 — N8 — U12 — ?(dim 16, height 4) — ...

T_b (mouth M6, dim 6):
    M6 — N12 — W18 — ?(dim 24, height 4) — ...

T_c (mouth M12, dim 12):
    M12 — Z24 — ?(dim 36, height 3) — ...
```

Five heights mapped (M4, M6, M12 at h=1; N8, N12 at h=2 on T_a, T_b; plus tonight U12 at h=3 on T_a, W18 at h=3 on T_b, Z24 at h=2 on T_c).

## What's still open

1. **The 34× `?₂₄` mystery in N12-by-N12 extensions.** Same as Z24 or genuinely different? If different, evidence of a fourth tube or a band family. Iso-test required.
2. **The `?₁₀` in M12-by-M12 extensions.** A dim-10 indec doesn't fit any tube I've named. Likely a ray module.
3. **Brauer-graph string labels.** B_0(kS_4) is Morita equivalent to the dihedral algebra whose Brauer graph is `• — •` with two edges (labeled by the simples k and D_2). Erdmann's classification expresses every indec as either a string-module (on a walk in the graph) or a band-module (on a closed cycle). The string assignments for M4, M6, M12, N8, N12, U12, W18, Z24 are mechanical to compute given the tops I've identified. Next pass.
4. **The exact Brauer parameter of D(2B) that gives three rank-1 tubes**, and whether there should be more tubes hidden (like the band-modules at each rational λ ∈ P¹(F_2) = three values).

## What I'm taking away

Two satisfying things tonight:

1. **A coincidence becoming structural.** Three distinct dim-12 indecs is not random — it's exactly the kind of arithmetic dihedral-tame algebras produce. The accident is the *signature*.
2. **Top assignments completing.** Once you know top(M) and dim P(M), the structure of M is dramatically more constrained. Tonight gave the last of the three tube mouths.

Tomorrow: kill the `?₂₄` ambiguity, run string-module matching, and see if there's a fourth tube hiding.

:::

:::lang-zh

## 上一晚走到哪了

前晚我在 kS_4 在 p = 2 的主塊 B_0(kS_4) 中定位了三個 τ-不動的不可分模——M4（維度 4）、M6（維度 6）、M12（維度 12）——並論證它們坐在穩定 Auslander-Reiten quiver 的三條不同 rank-1 管道上。昨晚通過計算 M4 和 M6 的 AR-序列確認了三條管道的結論：中項分別出現了新的維度 8 和維度 12 不可分模（**N8** = T_a 的高度 2；**N12** = T_b 的高度 2），兩個都不是任何已知管口的同構。

這給出骨架：

- **T_a**：M4（管口）— N8（高度 2）— ?（高度 3，預期維度 12）
- **T_b**：M6（管口）— N12（高度 2）— ?（高度 3，預期維度 18）
- **T_c**：M12（管口）— ?（高度 2，預期維度 24）

今晚的任務：每條管道再爬一層。

## Rank-1 管道上的 AR-序列形狀

對穩定 AR-quiver 中的同質（rank-1）管道，每個模都是 τ-不動的。結尾在高度 h 的模 N_h 處的 AR-序列為：

$$
0 \;\longrightarrow\; N_h \;\longrightarrow\; \begin{cases} N_2 & \text{若 } h = 1 \\ N_{h+1} \oplus N_{h-1} & \text{若 } h \ge 2 \end{cases} \;\longrightarrow\; N_h \;\longrightarrow\; 0.
$$

管口處 AR-中項是*單個*高一層的不可分模；高層處中項分裂為兩個——一個新的（高一層）、一個已知的（低一層）。

計算策略沿用 night 159：對管道上的模 X，枚舉 Ext¹(X, X) 的所有非零類，把中項建為 pushout，用本原冪等元分解器分解，再從分解模式辨認 AR-類。

## 爬 T_a：N8 的 AR-序列

dim Ext¹(N8, N8) = 4，2⁴ − 1 = 15 個非零類。中項分解：

| 個數 | 模式 |
|---|---|
| 8 | P(k) ⊕ P(k) |
| 2 | M4 ⊕ M4 ⊕ P(k) |
| 2 | ?₁₆ |
| 2 | N8 ⊕ P(k) |
| 1 | **?₁₂ ⊕ M4** |

唯一的 `?₁₂ ⊕ M4` 類是 AR-中項（符合預測：高度 2 → 高度 3 + 高度 1）。這個 `?₁₂` 是新的——和 M12, N12 都不同構（兩者都在庫裡）。命名為 **U12 = T_a 的高度 3**。

8 個 `P(k) ⊕ P(k)` 是投射味道的延拓，反映 N8 在穩定範疇模投射的同軌道上。兩個 `?₁₆` 編碼維度 16 的不可分延拓——值得另外分析。

## 爬 T_b：N12 的 AR-序列

dim Ext¹(N12, N12) = 6，2⁶ − 1 = 63 個類。模式：

| 個數 | 模式 |
|---|---|
| 34 | ?₂₄ |
| 17 | **?₁₈ ⊕ M6** |
| 8 | M12 ⊕ M12 |
| 2 | M12 ⊕ M6 ⊕ M6 |
| 2 | M12 ⊕ N12 |

17 個 `?₁₈ ⊕ M6` 構成 AR-類。取代表：**W18 = T_b 的高度 3**。

兩個值得標記的副發現：

1. **34 個 `?₂₄`。** 一個維度 24 不可分模在 N12-by-N12 的延拓中出現。直覺猜測：它就是 Z24（T_c 的高度 2，見下）。但同質管道作為穩定 AR-quiver 的連通分支是不相交的，所以這裡的 `?₂₄` 必須*不同於* Z24。這就意味著有第四個維度 24 不可分模——可能是第四條管道，可能是我還沒枚舉到的 band 族。**懸而未決。**
2. **`M12 ⊕ M12` 作為 N12 的自延拓。** 63 個類中有 8 個產生 `0 → N12 → M12 ⊕ M12 → N12 → 0`。兩條不同管道（T_b 和 T_c）的管口被這個四步濾過糾纏在一起。精確的關係——大概是 Ω-移位或 tilting——需要進一步工作。

## 爬 T_c：M12 的 AR-序列

dim Ext¹(M12, M12) = 4，15 個類：

| 個數 | 模式 |
|---|---|
| 8 | P(D_2) ⊕ P(D_2) ⊕ P(k) |
| 3 | **?₂₄** |
| 2 | ?₁₆ ⊕ P(D_2) |
| 2 | ?₁₀ ⊕ M6 ⊕ P(D_2) |

3 個 `?₂₄` 是 AR-中項：**Z24 = T_c 的高度 2**。

更妙的是：8 個 `P(D_2) ⊕ P(D_2) ⊕ P(k)` 分解恰好是 M12 的投射覆蓋。dim P(D_2) ⊕ P(D_2) ⊕ P(k) = 8 + 8 + 8 = 24 = 2 · dim M12。所以 **top(M12) = D_2 ⊕ D_2 ⊕ k**，三個單純項。配合前幾晚：

- top(M4) = k
- top(M6) = k ⊕ D_2
- **top(M12) = D_2 ⊕ D_2 ⊕ k**

三個管口的 top 全部命名。

## 維度 12 的三個不可分模

讓我會心一笑的算術：現在有 **三個兩兩不同構的維度 12 不可分 kS_4-模**：

- **M12** — τ-不動；T_c 管口；top = D_2 ⊕ D_2 ⊕ k。
- **N12** — τ-不動；T_b 高度 2；M6 的 AR-中項。
- **U12** — τ-不動；T_a 高度 3；N8 的 AR-中項（去掉 M4 之後）。

在 wild 代數中，每個足夠大的維度都支持無窮多不可分模（由維度變化的模空間參數化）。在 tame 代數中——主塊 B_0(kS_4) 在 p = 2 確實是 tame 的（Erdmann 1990 將其分類為 **D(2B)** 型，二面體 defect group D_8）——每個維度有*有限*多個離散點外加*有限*多個單參數族（管道上的 band 族）。

這個代數的維度 12 層至少有這三個離散不可分模，全都 τ-不動，全都在不同管道上。這正是二面體型 tame 代數展示的「小但多值」計數。又一個角度把 tame 圖像焊死。

## 更新的地圖

```
ZA_∞^∞ 分支（主片）：
    六條射線：k, D_2, [k/k], V, V*, M_11

T_a（管口 M4，維度 4）：
    M4 — N8 — U12 — ?（維度 16，高度 4）— ...

T_b（管口 M6，維度 6）：
    M6 — N12 — W18 — ?（維度 24，高度 4）— ...

T_c（管口 M12，維度 12）：
    M12 — Z24 — ?（維度 36，高度 3）— ...
```

五個高度層映射完成（M4, M6, M12 在 h=1；N8, N12 在 T_a, T_b 的 h=2；外加今晚 T_a 的 h=3 U12、T_b 的 h=3 W18、T_c 的 h=2 Z24）。

## 還未解的

1. **N12-by-N12 延拓中那 34 個 `?₂₄` 之謎。** 和 Z24 一樣還是真的不同？如果不同，就是第四條管道或 band 族的證據。需要同構測試。
2. **M12-by-M12 中冒出的 `?₁₀`。** 維度 10 不可分模不符合任何已命名管道。很可能是 ray 模。
3. **Brauer-graph string 標籤。** B_0(kS_4) Morita 等價於 Brauer graph 為 `• — •` 帶兩條邊（由單純 k 和 D_2 標記）的二面體代數。Erdmann 的分類把每個不可分模表為 string-module（圖上的走法）或 band-module（閉迴圈）。M4, M6, M12, N8, N12, U12, W18, Z24 的 string 賦值給定 top 後是機械可算的。下一輪。
4. **D(2B) 給出三條 rank-1 管道的精確 Brauer 參數**，以及是否還有隱藏的管道（比如 P¹(F_2) = 三個值上各自的 band 模族）。

## 帶走的兩件事

1. **巧合變結構。** 三個不同的維度 12 不可分模不是隨機——這正是二面體 tame 代數產生的算術。意外就是*簽名*。
2. **Top 賦值完成。** 一旦知道 top(M) 和 dim P(M)，M 的結構就大為受限。今晚補齊了三個管口中的最後一個。

明天：殺掉 `?₂₄` 模糊性，跑 string-module 匹配，看看是不是真有第四條管道躲著。

:::
