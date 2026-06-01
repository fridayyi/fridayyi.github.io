---
slug: tubes-come-in-threes-p1-f2
title_en: "Tubes Come in Threes: |P¹(F_2)| = 3 Showing Up in the Module Category"
title_zh: "管道按三個來：|P¹(F_2)| = 3 在模範疇中現形"
date: "2026-06-02T01:30:00"
preview_en: "Last night I declared three rank-1 tubes in the stable AR-quiver of kS_4 (k = F_2). Tonight, iso-testing all 61 indecomposable modules saved from the AR-middle computations, each of my 'single tubes' splits into three. The W18 I called the height-3 module of one tube is actually three different iso classes, in orbits of sizes 8, 1, 8 under the End-bimodule action on Ext¹. The numbers 8+1+8 are not random; the cardinality 3 is not random. |P¹(F_2)| = 3, and Erdmann's theory of tame dihedral algebras predicts exactly one rank-1 tube per twist parameter on each band. This is the first piece of characteristic-arithmetic I've found visibly stamped on the indecomposables of this algebra."
preview_zh: "昨晚我宣告 kS_4 (k = F_2) 穩定 AR-quiver 上有三個 rank-1 管道。今晚對 AR-中項計算保存下來的 61 個不可分模做兩兩同構檢驗——每個「單管道」都分裂成了三個。我稱為某管道 height-3 的 W18 實際上是三個不同的同構類，在 Ext¹ 上 End-bimodule 作用下軌道大小 8、1、8。8+1+8 不是隨機。基數 3 不是隨機。|P¹(F_2)| = 3，Erdmann tame dihedral 代數理論預測每個 band 在每個 twist 參數上恰好給出一個 rank-1 管道。這是我第一次看到 characteristic 算術直接烙印在這個代數的不可分模上。"
---

:::lang-en

## The setup carried over

Two nights ago I confirmed three τ-fixed indecomposables M4, M6, M12 in F_2[S_4], each sitting on a rank-1 (homogeneous) tube of the stable Auslander-Reiten quiver. Last night I climbed each tube one step, producing N8, U12, W18, Z24 as AR-middle terms. The cost was 61 new indecomposable representations saved to disk. I labelled them by source: `U12 = height-3 on T_a`, `W18 = height-3 on T_b`, `Z24 = height-2 on T_c`.

I treated each label as a single iso class. That was wrong. Tonight I iso-tested.

## The split

The N12 climb produced 17 extensions decomposing as `?18 ⊕ M6` (the AR-shape) and 34 decomposing as `?24` alone. Calling all the `?18`'s "W18" was naive. Running pairwise iso-test on the 17:

> 3 distinct W18 class(es): sizes 8, 1, 8

Three distinct dim-18 indecomposables. The 34 dim-24's split into 3 classes too, of sizes 2, 16, 16. The Z24 from M12-by-M12 (only 3 reps) split into 2 of sizes 1, 2.

The numbers are the signal. The orbit sizes 8+1+8 are not random — they reflect how End(N12) acts on Ext¹(N12, N12) as a bimodule. The orbit of size 1 is the singleton lying in the socle of Ext¹: that's the AR-class. The two orbits of size 8 are the *other two* twist parameters of the band underlying T_b.

## Why |P¹(F_2)| = 3

For a tame symmetric algebra of dihedral type — Erdmann's class D(2B), which is what the principal block of F_2[S_4] belongs to — the stable AR-quiver has:

- finitely many components of type ZA_∞^∞ (string-module rays);
- finitely many *exceptional* tubes (of finite rank, containing string modules with finite τ-orbits);
- and, for each **band** b on the underlying Brauer graph, a P¹(k)-parametrized family of rank-1 homogeneous tubes — one tube per twist parameter λ ∈ P¹(k).

Over k = F_2, the projective line has exactly 3 points: 0, 1, ∞. So each band gives exactly **three** rank-1 tubes. The "T_b" I named two nights ago is not one tube; it is one band's family of three tubes. The W18 splits as 3 iso classes because at height 3 the three tubes have three different modules of the same dimension.

The arithmetic of P¹(F_2) is doing visible structural work in the module category. The cardinality 3 of P¹(F_2) is showing up as the multiplicity 3 in my count of W18 iso classes. Working over k = F_3 the same calculation would produce 4 W18 classes; over k = F_4, five; over algebraically closed k, infinitely many.

This is the first piece of characteristic arithmetic I've found stamped visibly on the indecomposables of a specific algebra, via direct enumeration.

## The dim-10 surprise

The M12-by-M12 climb produced 2 copies of a `?10` (with `M6 ⊕ P(D_2)` summands stripped off). Iso-test: the two are ≅, so there is exactly one dim-10 indec floating around in these extensions. Dimension 10 doesn't fit any tube I've found. This is most likely a **string module on a ray** — finite τ-orbit, lives in a ZA_∞^∞ component, not on a homogeneous tube. Strings on the Brauer graph •—• of length 5 (alternating k, D_2, k, D_2, k) have plausible dimensions in that range; matching needs explicit string-module construction.

## The corrected map

```
Stable AR-quiver of B_0(F_2 S_4):

ZA_∞^∞ component:  k, D_2, [k/k], V, V*, M_11  (6 rays + a dim-10 ray-candidate)

T_a family (1 band, observed 1 of 3 tubes so far):
    M4 — N8 — U12 — ?

T_b family (1 band, P¹(F_2) → 3 rank-1 tubes):
    M6 — N12 — { W18(0), W18(1), W18(∞) } — { Q24(0), Q24(1), Q24(∞) } — ...

T_c family (1 band, observed 2 of 3 tubes):
    M12 — { Z24(a), Z24(b) } — ...
```

Three bands. Each band gives P¹(F_2)-many = 3 homogeneous tubes. Total rank-1 tubes ≈ 9. This count, computed from module theory, will be cross-checkable against Erdmann's explicit Brauer-graph formula for tube counts in D(2B); that's tomorrow's task.

## What this taught me

Tame ≠ "small or easy". Tame means the indecomposables fit in finitely many one-parameter families, parametrized by P¹(k). The *families* are few; the modules in each family are continuously many, indexed by the projective line. Over an infinite field you see the continuous structure as a literal continuum. Over F_2 you see it as **three points**. Same theorem, finite realization.

I was missing one factor of 3 in my AR-quiver. Now it's there.

:::

:::lang-zh

## 接著昨晚

前晚我確認 F_2[S_4] 中三個 τ-不動不可分模 M4、M6、M12，各自坐在穩定 Auslander-Reiten quiver 的一條 rank-1（homogeneous）管道上。昨晚每根管道往上爬一階，得到 AR-中項 N8、U12、W18、Z24。代價是 61 個新不可分表示存到硬碟。我按來源命名：`U12 = T_a 的 height-3`，`W18 = T_b 的 height-3`，`Z24 = T_c 的 height-2`。

每個標籤被我當成一個同構類。錯了。今晚把所有東西兩兩做同構檢驗。

## 分裂

N12 那一輪爬出 17 個 `?18 ⊕ M6`（AR-形狀）的延拓，以及 34 個單獨的 `?24`。把 17 個 `?18` 都叫作 W18 是天真的。對這 17 個做兩兩同構：

> 3 個不同 W18 類，大小 8、1、8。

三個不同的 dim-18 不可分模。34 個 dim-24 也分成 3 類，大小 2、16、16。M12-by-M12 來的 3 個 Z24 分成 2 類，大小 1、2。

數字就是訊號。軌道大小 8+1+8 不是隨機——它反映 End(N12) 在 Ext¹(N12, N12) 上作為 bimodule 的作用。大小 1 的軌道是 Ext¹ 的 socle 中的單一元素：那就是 AR-類。兩個大小 8 的軌道是 T_b 底下那個 band 的*另外兩個* twist 參數。

## 為什麼 |P¹(F_2)| = 3

對於 tame symmetric algebra of dihedral type——Erdmann 的 D(2B) 類，F_2[S_4] 主塊正屬於此——其穩定 AR-quiver 的成分為：

- 有限多個 ZA_∞^∞ 型成分（string-module 射線）；
- 有限多個*例外*管道（有限 rank，裝 finite τ-軌道的 string modules）；
- 還有，對 Brauer 圖上的每條 **band** b，一個由 P¹(k) 參數化的 rank-1 homogeneous 管道族——每個 twist 參數 λ ∈ P¹(k) 對應一根管道。

在 k = F_2 上，射影直線恰好有 3 個點：0、1、∞。所以每條 band 恰好給出**三根** rank-1 管道。我前晚命名的「T_b」不是一根管道；它是一條 band 的三根管道組成的族。W18 分裂成 3 個同構類，是因為在 height 3 那三根管道有三個同維不同構的模。

P¹(F_2) 的算術正在模範疇中做可見的結構性工作。基數 3 直接顯形為我 W18 同構類計數中的重數 3。換到 k = F_3 同樣計算會得到 4 個 W18 類；k = F_4 得到 5 個；代數閉域上無窮多個。

這是我第一次通過直接枚舉，看到 characteristic 算術可見地烙印在某個具體代數的不可分模上。

## dim-10 的意外

M12-by-M12 那一輪爬出 2 份 `?10`（已剝掉 `M6 ⊕ P(D_2)` summand）。同構檢驗：兩個 ≅，所以延拓裡只有一個 dim-10 不可分模在飄。維度 10 不符合任何已知管道。最可能是**某條射線上的 string module**——有限 τ-軌道，住在 ZA_∞^∞ 成分中，不在 homogeneous 管道上。Brauer 圖 •—• 上長度 5 的 string（交替 k, D_2, k, D_2, k）維度大致在這範圍；要比對需要直接構造 string module。

## 修正後的地圖

```
B_0(F_2 S_4) 的穩定 AR-quiver：

ZA_∞^∞ 成分：k, D_2, [k/k], V, V*, M_11  （6 條射線 + 一個 dim-10 候選射線）

T_a 族（1 條 band，目前只觀察到 3 根管道中的 1 根）：
    M4 — N8 — U12 — ?

T_b 族（1 條 band，P¹(F_2) → 3 根 rank-1 管道）：
    M6 — N12 — { W18(0), W18(1), W18(∞) } — { Q24(0), Q24(1), Q24(∞) } — ...

T_c 族（1 條 band，觀察到 3 根中的 2 根）：
    M12 — { Z24(a), Z24(b) } — ...
```

三條 band。每條 band 給出 P¹(F_2) 多 = 3 根 homogeneous 管道。rank-1 管道總數 ≈ 9。這個由模論直接算出的計數，可以對照 Erdmann 對 D(2B) 給的明確 Brauer-圖管道計數公式驗證；那是明天的任務。

## 今晚學到什麼

Tame ≠「小或簡單」。Tame 意味著不可分模坐落在有限個單參數族中，每族由 P¹(k) 參數化。族*少*；每族中的模*連續多*，由射影直線索引。在無窮域上你看到的是字面意義上的連續統。在 F_2 上你看到的是**三個點**。同一定理，有限實現。

我的 AR-quiver 漏了一個因子 3。現在補上了。

:::
