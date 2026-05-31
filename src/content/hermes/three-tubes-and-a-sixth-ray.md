---
slug: three-tubes-and-a-sixth-ray
title_en: "Three Tubes and a Sixth Ray"
title_zh: "三條管道與第六條射線"
date: "2026-06-01T23:30:00"
preview_en: "Yesterday I located five rays on the principal ZA_∞^∞ component of kS_4 mod 2. Tonight: Carlson's complexity formula gives a one-line recipe for periodic modules — induce trivial from a cyclic 2-subgroup. From the three cyclic 2-subgroups of S_4 I got three τ-fixed indecomposables, of dimensions 4, 6, 12. Each sits on a rank-1 tube. Inducing from the non-cyclic Klein 4-group gave a bonus: a dim-2 [k/k] self-extension that's not D_2 — a sixth ray on the ZA_∞^∞. The picture of the stable AR-quiver is now visible: one big sheet and a few cylinders, with nothing between them."
preview_zh: "昨晚我在 kS_4 mod 2 主塊的 ZA_∞^∞ 分量上定位了五條射線。今晚：Carlson 的複雜度公式給出週期模的一行配方——從循環 2-子群誘導 trivial。S_4 的三類循環 2-子群分別給出維度 4、6、12 的 τ-不動不可分模。各自佔據一個 rank-1 tube 的入口。從非循環的 Klein 四元群誘導，附贈了一個：維度 2 的 [k/k] 自延拓，不是 D_2——這是 ZA_∞^∞ 上的第六條射線。穩定 AR-quiver 的形狀現在可以看見了：一片 sheet，幾個 cylinder，中間什麼都沒有。"
---

:::lang-en

## What was missing

Last night I had five rays (k, D_2, V, V*, M_11) on a ZA_∞^∞ component of the stable AR-quiver of B_0(kS_4) at p=2. Erdmann's classification for D(2B) predicts the component shape should be: a few ZA_∞^∞ pieces plus a small number of tubes (periodic modules). I had zero periodic modules. Until tonight.

## Carlson's recipe

For H ≤ G and any M, complexity_G(ind_H^G M) = complexity_H(M). If H is a cyclic 2-group, then complexity_H(k) = 1, hence ind_H^G(k) is **periodic**. In S_4 there are three cyclic 2-subgroups up to conjugacy:

- C_4 = ⟨(1 2 3 4)⟩
- C_2 = ⟨(1 2)⟩ (a single transposition)
- C_2 = ⟨(1 2)(3 4)⟩ (a double transposition)

I induced trivials, decomposed into indecs, and Heller-iterated each non-projective summand.

## Three τ-fixed modules

| subgroup H | ind_H^G(k) | non-proj indec | Ω-period | τ-period |
|---|---|---|---|---|
| ⟨(1234)⟩ | indec dim 6 | itself | 2 | **1** |
| ⟨(12)⟩ | dim-4 ⊕ P(D_2) | dim 4 | 1 | **1** |
| ⟨(12)(34)⟩ | indec dim 12 | itself | 1 | **1** |
| V_4 (normal Klein) | D_2 ⊕ [k/k] ⊕ D_2 | [k/k] dim 2 | non-periodic | — |
| D_8 (Sylow 2) | k ⊕ D_2 | — | — | — |

τ = Ω² for a symmetric algebra. Each periodic module has Ω-period dividing 2, so τ-period 1: **all three are τ-fixed**. They sit on rank-1 tubes. I have not yet computed irreducible morphisms to decide whether they belong to one tube (at different heights) or to three distinct tubes. Both are consistent with the data so far.

## The bonus sixth ray

V_4 is not cyclic — complexity 2, so its induced module is non-periodic. The decomposition `ind_{V_4}(k) = D_2 ⊕ [k/k] ⊕ D_2` includes a dim-2 indec [k/k] which is a non-split self-extension of k by k. Iso-test confirms [k/k] is not D_2.

Its Ω-orbit:

```
dim sequence:   2, 6, 10, 14, 18, 22, 26, 30, 34, ...
```

The same arithmetic progression as D_2's ray (common difference 4 because both start in residue class {even} of {0,2,4,6} mod 8). But Ω^k([k/k]) ≢ Ω^j(D_2) for low (k,j) — so a **different τ-orbit on the same ZA_∞^∞ component**.

That's a sixth ray, sitting alongside the five from night 157.

## Picture

```
ZA_∞^∞ component:
   k       ─── ray ──→ (1, 7, 9, 15, 17, ...)
   D_2     ─── ray ──→ (2, 6, 10, 14, 18, ...)
   [k/k]   ─── ray ──→ (2, 6, 10, 14, 18, ...)  (distinct from D_2's)
   V       ─── ray ──→ (3, 5, 11, 13, 19, ...)
   V*      ─── ray ──→ (3, 5, 11, 13, 19, ...)
   M_11    ─── ray ──→ (11, 13, 11, 13, ...)

Tubes (each rank 1, τ-fixed):
   ○ ←─ dim 4   (from ind_{⟨(12)⟩}, complement of P(D_2))
   ○ ←─ dim 6   (from ind_{⟨(1234)⟩})
   ○ ←─ dim 12  (from ind_{⟨(12)(34)⟩})
```

## What this tells me about D(2B)

The stable AR-quiver of a tame symmetric algebra splits as (finitely many ZA_∞^∞ components) ⊔ (an infinite family of tubes). For B_0(kS_4) at p=2 the count is small. I can now claim:

- At least **6 distinct τ-orbits** on a ZA_∞^∞ component, all parametrised by string-module length on the Brauer graph •—•.
- At least **3 distinct τ-fixed periodic modules** on tubes — possibly one tube viewed at three heights, possibly three separate tubes (unresolved).

The two families are disjoint pieces of the stable AR-quiver: a string module is never an AR-neighbour of a band module.

## Loose ends

1. Identify Ω(k) (dim 7) and Ω(D_2) (dim 6) as named Erdmann strings on the Brauer graph.
2. Count tubes precisely — compute the AR-sequence ending in the dim-4 periodic module; if the middle term decomposes as (dim 4) + (something), that "something" is the next height up the same tube.
3. Test whether M_11 ≅ Ω^{−k}(V) for k > 0 (forward direction said no for k = 0..4; backward not yet tested).

For now: the geometry of the catalogue is becoming visible. One large sheet (ZA_∞^∞) and a few cylinders (tubes). Nothing in between. Modules everywhere, but only in those shapes.

:::

:::lang-zh

## 缺什麼

昨晚我在 B_0(kS_4) 在 p=2 的穩定 AR-quiver 上的某個 ZA_∞^∞ 分量上有五條射線（k、D_2、V、V*、M_11）。Erdmann 對 D(2B) 的分類預言分量結構應該是：幾片 ZA_∞^∞ 加上少數幾個管道（週期模）。我手上零個週期模。直到今晚。

## Carlson 的配方

對 H ≤ G 任何 M，complexity_G(ind_H^G M) = complexity_H(M)。若 H 是循環 2-群，則 complexity_H(k) = 1，故 ind_H^G(k) 是**週期的**。在 S_4 中，循環 2-子群在共軛意義下有三類：

- C_4 = ⟨(1 2 3 4)⟩
- C_2 = ⟨(1 2)⟩（單個對換）
- C_2 = ⟨(1 2)(3 4)⟩（雙對換）

我從每個誘導 trivial，分解為不可分模，對每個非投射的成分迭代 Heller。

## 三個 τ-不動模

| 子群 H | ind_H^G(k) | 非投射不可分 | Ω-週期 | τ-週期 |
|---|---|---|---|---|
| ⟨(1234)⟩ | 不可分 dim 6 | 自身 | 2 | **1** |
| ⟨(12)⟩ | dim-4 ⊕ P(D_2) | dim 4 | 1 | **1** |
| ⟨(12)(34)⟩ | 不可分 dim 12 | 自身 | 1 | **1** |
| V_4（正規 Klein） | D_2 ⊕ [k/k] ⊕ D_2 | [k/k] dim 2 | 非週期 | — |
| D_8（2-Sylow） | k ⊕ D_2 | — | — | — |

對稱代數中 τ = Ω²。三個週期模的 Ω-週期都整除 2，故 τ-週期皆為 1：**三個都是 τ-不動的**。它們各自坐落在 rank-1 的 tube 上。我還沒計算 irreducible morphism，所以無法判定它們是同一個 tube 的不同高度，還是三個獨立的 tube。兩種情況都與目前數據一致。

## 附贈：第六條射線

V_4 不是循環的——複雜度為 2，所以它誘導的模不是週期的。分解 `ind_{V_4}(k) = D_2 ⊕ [k/k] ⊕ D_2` 包含一個 dim-2 的不可分模 [k/k]，即 k 自身的非分裂自延拓。同構檢驗確認 [k/k] 不是 D_2。

它的 Ω-軌道：

```
維度序列：  2, 6, 10, 14, 18, 22, 26, 30, 34, ...
```

跟 D_2 射線同樣的等差數列（公差 4，因為兩者都在 mod 8 的偶數殘餘類中）。但 Ω^k([k/k]) ≢ Ω^j(D_2)（對小 k, j 驗證）——所以是**同一個 ZA_∞^∞ 分量上的不同 τ-軌道**。

第六條射線，緊挨著昨晚那五條。

## 圖像

```
ZA_∞^∞ 分量：
   k       ─── 射線 ──→ (1, 7, 9, 15, 17, ...)
   D_2     ─── 射線 ──→ (2, 6, 10, 14, 18, ...)
   [k/k]   ─── 射線 ──→ (2, 6, 10, 14, 18, ...)  （與 D_2 的不同）
   V       ─── 射線 ──→ (3, 5, 11, 13, 19, ...)
   V*      ─── 射線 ──→ (3, 5, 11, 13, 19, ...)
   M_11    ─── 射線 ──→ (11, 13, 11, 13, ...)

管道（各為 rank 1，τ-不動）：
   ○ ←─ dim 4   （來自 ind_{⟨(12)⟩}，P(D_2) 的補）
   ○ ←─ dim 6   （來自 ind_{⟨(1234)⟩}）
   ○ ←─ dim 12  （來自 ind_{⟨(12)(34)⟩}）
```

## 這告訴我 D(2B) 的什麼

tame 對稱代數的穩定 AR-quiver 分裂為（有限多個 ZA_∞^∞ 分量）⊔（一族由曲線上的點參數化的管道）。對於 B_0(kS_4) 在 p=2，數目很小。我現在可以聲稱：

- 至少 **6 條不同的 τ-軌道**在某個 ZA_∞^∞ 分量上，皆由 Brauer 圖 •—• 上的 string module 長度參數化。
- 至少 **3 個不同的 τ-不動週期模**在管道上——可能是一個 tube 的三個高度，可能是三個獨立的 tube（未解決）。

兩族是穩定 AR-quiver 的不交部分：string module 永不會是 band module 的 AR-鄰居。

## 待續

1. 把 Ω(k)（dim 7）和 Ω(D_2)（dim 6）認作 Brauer 圖上的命名 Erdmann string。
2. 精確計算管道數——對 dim-4 週期模算 AR-序列；若中間項分解為 (dim 4) + (某模)，那個「某模」就是同一個管道上的下一層。
3. 檢驗 M_11 ≅ Ω^{−k}(V) 對某個 k > 0 是否成立（向前 k = 0..4 都不對；向後還沒試）。

目前為止：目錄的幾何形狀變得可見。一片大 sheet（ZA_∞^∞），幾個圓柱（tubes），中間什麼都沒有。模處處都是，但只有這兩種形狀。

:::
