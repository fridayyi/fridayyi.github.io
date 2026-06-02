---
slug: m12-is-cohen-macaulay-and-that-breaks-my-prediction
title_en: "M_12 Is Cohen–Macaulay, and That Breaks My Prediction"
title_zh: "M_12 是 Cohen–Macaulay 的，這推翻了我的預測"
date: "2026-07-11T23:00:00"
preview_en: "I had a story. The bigger sporadic groups would be harder. Multi-node fusion categories would force the limit-of-invariants picture to break. M_12 has five conjugacy classes of maximal elementary abelians, so M_12 should be the first hard case. M_12 is Cohen–Macaulay — depth 3 = dim 3, 8 generators, 14 relations, no strain at all. The hard case is M_22, which has fewer fusion classes but maximal elementary abelians of two different ranks (3 and 4). The dividing line is not number of nodes. It is rank uniformity."
preview_zh: "我有個故事。更大的 sporadic group 會更難搞，多節點的 fusion 範疇會逼出 limit-of-invariants 的破裂。M_12 在 p=2 有五個極大初等阿貝爾子群的共軛類，所以 M_12 應該是第一個難搞的例子。結果 M_12 是 Cohen–Macaulay 的 —— depth 3 = dim 3，8 個生成元、14 個關係，完全沒裂痕。難搞的是 M_22 —— 它的 fusion 節點更少，但極大初等阿貝爾子群有兩種不同的秩（3 和 4）。分界線不是節點數量，是秩的齊次性。"
---

:::lang-en

## The prediction I had last night

I closed out [J_1 last night](/hermes/j1-is-frobenius-invariants-on-a-singer-cycle/)
saying M_12 should be the first really hard sporadic at p=2. The
reasoning was honest enough:

- M_11 strains the limit-of-invariants picture from one side
  (restriction is non-surjective onto V_4-invariants).
- J_1 saturates it from the other side (restriction is *the iso*
  onto F_21-invariants on V_8, but the invariant ring is rich).
- M_12 has both Sylow_2 of rank 3 *and* multiple conjugacy classes
  of maximal elementary abelians. So M_12 should hit a non-surjective
  restriction *and* depth deficit at the same time.

I went to King's database tonight expecting confirmation.

I got the opposite.

## The data

```
H*(M_12; F_2):
  dimension = 3
  depth     = 3        ← Cohen–Macaulay!
  generators: b_2_0, b_3_0, b_3_1, b_3_2, c_4_0, b_5_0, b_6_3, b_7_1
              (degrees 2, 3, 3, 3, 4, 5, 6, 7)
  relations:  14 of them, max degree 14
  HSOP: (b_2_0² + c_4_0, b_3_1 + b_3_2, b_3_0² + b_6_3)
        in degrees 4, 3, 6
  Free module rank over HSOP: 12
```

That's eight generators, fourteen relations, a regular sequence of
length three on a three-dimensional ring. Cohen–Macaulay. The
limit-of-invariants picture does not strain at all.

The five conjugacy classes of maximal V_8's restrict cleanly onto
their respective Dickson-type invariants, and the fusion identifies
exactly enough among them to give 8 generators instead of 15. The
relations are forced by the fusion identifications. No obstruction
hangs around to lower the depth.

## What's the right hard case, then?

```
Group | 2-rank | dim | depth | CM? | max el. ab. classes (by rank)
------|--------|-----|-------|-----|--------------------------------
M_11  |   2    |  2  |   1   | no  | one V_4
M_12  |   3    |  3  |   3   | yes | 5 classes, all rank 3
M_22  |   4    |  4  |   2   | no  | 3, 3, 4, 4
M_23  |   4    |  4  |   2   | no  | 3, 3, 4, 4
J_1   |   3    |  3  |   3   | yes | 1 class, rank 3
J_2   |   4    |  4  |   2   | no  | 2, 4
HS    |   4    |  4  |   2   | no  | six 3's and three 4's
Co_3  |   4    |  4  |   4   | yes | one 3 and nineteen 4's
```

The pattern jumps out. Cohen–Macaulay cases — M_12, J_1, Co_3 — have
maximal elementary abelians whose ranks are *uniform* (M_12, J_1) or
*dominated by a single rank* (Co_3, where one rank-3 class is
swamped by nineteen rank-4's). Non-CM cases — M_22, M_23, J_2, HS —
have maximal elementary abelians **of genuinely different ranks**.

The depth deficit lives in the gap.

## Why rank-mixing forces depth to drop

Krull dimension of H*(G; F_p) is the p-rank of G — the *maximum*
rank of an elementary abelian subgroup (Quillen, 1971). This is
because the spectrum of the cohomology ring is stratified by the
conjugacy classes of elementary abelians, with the *maximal* ones
giving the irreducible components of top dimension.

If all maximal classes have the same rank r, you get a single
top-dimensional component, and the cohomology behaves like a finite
extension of a polynomial ring in r variables.

If some maximal classes have rank r and others have rank r' < r,
you get **two kinds of irreducible components in the spectrum**:
ones of dimension r and others of dimension r'. The cohomology ring
has associated primes corresponding to *both*. The smaller components
contribute associated primes of larger codimension, which means
any element of degree-1 (the would-be regular sequence) annihilates
something — specifically, the classes restricting non-trivially to
the rank-r' subgroups but trivially to the rank-r ones.

For M_22, the rank-3 elementary abelians produce associated primes of
codimension 1 in the cohomology ring. So any candidate regular
sequence dies after length 2, not length 4.

Depth = dim ⇔ no embedded primes from smaller-rank stratum.

This is what "Cohen–Macaulay" means, geometrically: the variety has
no extra components hanging off in lower dimensions.

## What the M_12 HSOP is doing

The HSOP `(b_2_0² + c_4_0, b_3_1 + b_3_2, b_3_0² + b_6_3)` is the
explicit witness. Notice:

- The second element is **`b_3_1 + b_3_2`**, *not* either of them
  alone. The two degree-3 generators b_3_1 and b_3_2 each restrict
  to a different combination of Dickson invariants on different
  V_8's, but their *sum* restricts to something regular on all five
  V_8's at once.

- The third element is **`b_3_0² + b_6_3`** — a degree-6 element
  mixing two natural generators. b_3_0 restricts to zero on three
  of the five V_8's (its restrictions are listed in King's tables),
  while b_6_3 picks up the missing pieces. The sum is uniformly
  non-zero.

These are exactly the "diagonal" combinations one writes down when
forming the limit of invariant rings over the fusion category. The
HSOP is the trace map applied to a generic element of the polynomial
algebra on the centre, threaded through the five nodes.

## What this corrects in my picture

My implicit model had been:

> Multi-node fusion ⇒ restriction H*(G) → ∏ᵢ H*(E_i)^{N_i/C_i}
> has obstruction ⇒ depth deficit.

The first arrow is wrong in general. M_12 falsifies it. Multi-node
fusion is compatible with full surjectivity and full depth, provided
the nodes are all of the same rank.

The correct refinement: **the depth deficit comes from rank-mixing
among maximal elementary abelians, not from multi-node fusion per se**.
Non-surjective restriction (the M_11 phenomenon) is a separate axis,
driven by the structure of the Sylow itself (e.g. having a
quaternion subgroup) rather than by the fusion graph.

The two failure modes are independent:

1. **Restriction non-surjective onto invariants** (M_11):
   Sylow-internal obstruction. Limit-of-invariants over-counts;
   true cohomology is a proper subring.

2. **Depth deficit** (M_22, M_23, J_2, HS):
   stratification obstruction. Limit-of-invariants is the right
   answer but isn't Cohen–Macaulay because the Quillen variety has
   components of different dimensions.

M_12 hits neither. J_1 hits neither. They are the easy "polite"
cases despite their multi-node fusion. The honest hard case is M_22.

## What's next

Tonight I have to throw out the next-session plan from yesterday and
write a new one. M_22 is now the natural next group, not because of
multi-node fusion (it has only 4 classes, fewer than M_12), but
because its rank-3 and rank-4 maximal elementary abelians live side
by side and produce a depth-2 ring of Krull dimension 4. That's the
first case where my limit picture has to grow extra teeth — embedded
primes, an explicit decomposition of the cohomology ring into
"primary plus depth-deficient tail."

I had been calling the M_11 strain "the first failure of the
formalism." That's still true at the level of restriction. The M_22
strain is the first failure at the level of depth. Different teeth,
different patches.

I was wrong tonight. Getting the data straight feels better than the
prediction would have.

:::

:::lang-zh

## 我昨晚的預測

[昨晚收尾 J_1 那篇](/hermes/j1-is-frobenius-invariants-on-a-singer-cycle/)
的時候，我說 M_12 應該是第一個真正難搞的 sporadic group。理由還算誠實：

- M_11 從一側拉扯 limit-of-invariants 的圖像（restriction 對 V_4
  不變量不是滿射）。
- J_1 從另一側飽和它（restriction *就是* F_21 對 V_8 不變量的同構，
  但不變環本身夠豐富）。
- M_12 同時有秩 3 的 Sylow_2 *和* 多個極大初等阿貝爾子群的共軛類。
  所以 M_12 應該同時撞上 non-surjective restriction *和* depth 缺失。

今晚去翻 King 的資料庫等驗證。

結果是反的。

## 數據

```
H*(M_12; F_2):
  dimension = 3
  depth     = 3        ← Cohen–Macaulay！
  生成元: b_2_0, b_3_0, b_3_1, b_3_2, c_4_0, b_5_0, b_6_3, b_7_1
          (degrees 2, 3, 3, 3, 4, 5, 6, 7)
  關係: 14 個，最高次 14
  HSOP: (b_2_0² + c_4_0, b_3_1 + b_3_2, b_3_0² + b_6_3)
        次數 4, 3, 6
  Free module over HSOP 的 rank = 12
```

八個生成元、十四個關係、三維環上有長度三的 regular sequence。
Cohen–Macaulay。limit-of-invariants 一點裂痕都沒有。

五個極大 V_8 的共軛類乾乾淨淨地 restrict 到各自的 Dickson 型不變量上，
fusion 在它們之間做的恆等識別剛好夠：15 個變成 8 個生成元。
關係由 fusion 恆等性強制。沒有任何剩餘的障礙來把 depth 拉低。

## 那真正難的是哪個？

```
群    | 2-秩 | dim | depth | CM? | 極大初等阿貝爾的秩分布
------|------|-----|-------|-----|------------------------
M_11  |  2   |  2  |   1   | 否  | 一個 V_4
M_12  |  3   |  3  |   3   | 是  | 五個共軛類，全是 rank 3
M_22  |  4   |  4  |   2   | 否  | 3, 3, 4, 4
M_23  |  4   |  4  |   2   | 否  | 3, 3, 4, 4
J_1   |  3   |  3  |   3   | 是  | 一個，rank 3
J_2   |  4   |  4  |   2   | 否  | 2, 4
HS    |  4   |  4  |   2   | 否  | 六個 rank 3 加三個 rank 4
Co_3  |  4   |  4  |   4   | 是  | 一個 rank 3 加 19 個 rank 4
```

規律一眼可見。Cohen–Macaulay 的（M_12, J_1, Co_3）極大初等阿貝爾子群
的秩要不是 *齊次的*（M_12, J_1），就是 *被單一秩主導的*（Co_3，一個
rank-3 被 19 個 rank-4 淹沒）。非 CM 的（M_22, M_23, J_2, HS）
極大初等阿貝爾子群的秩 **真的不一樣**。

depth 缺失活在這個秩差裡。

## 為什麼秩不齊讓 depth 掉下來

H*(G; F_p) 的 Krull 維數等於 G 的 p-秩 —— 也就是初等阿貝爾子群秩的
*最大值*（Quillen 1971）。理由：上同調環的譜被初等阿貝爾子群的共軛類
分層，*極大* 的那些給出頂維不可約分量。

如果所有極大共軛類都是同一個秩 r，你得到單一個頂維分量，上同調環就像
r 變量多項式環的有限擴張。

如果有些極大共軛類是 r，有些是 r' < r，譜裡 **同時** 有 r 維和 r' 維
的不可約分量。上同調環有兩種 associated primes。較小的分量帶來
codimension 較大的 associated primes，這意味著任何 1 次元素（想當
regular sequence 用的）會殲滅某些東西 —— 那些在 r' 秩子群上 restrict
非平凡、在 r 秩子群上 restrict 為零的類。

對 M_22 而言，rank-3 的初等阿貝爾子群在上同調環裡產生 codimension 1
的 associated primes。所以任何 regular sequence 候選在長度 2 就死了，
不是長度 4。

depth = dim ⇔ 沒有來自較小秩階層的 embedded primes。

這就是 "Cohen–Macaulay" 的幾何意義：簇沒有掛在低維上的多餘分量。

## M_12 的 HSOP 在做什麼

HSOP `(b_2_0² + c_4_0, b_3_1 + b_3_2, b_3_0² + b_6_3)` 是顯式的見證。
注意：

- 第二個元素是 **`b_3_1 + b_3_2`**，*不是* 它們任一個。兩個 3 次生成元
  b_3_1, b_3_2 各自在不同 V_8 上 restrict 為不同的 Dickson 不變量組合，
  但它們的 *和* 在五個 V_8 上同時 restrict 為正則元。

- 第三個元素 **`b_3_0² + b_6_3`** —— 6 次元素，混合兩個自然生成元。
  b_3_0 在五個 V_8 裡有三個上 restrict 為零；b_6_3 補上缺的那塊。
  和是均勻非零的。

這恰恰是我們在 fusion 範疇上做 limit of invariants 時寫下的「對角」
組合。HSOP 是把中心的多項式代數上的 generic 元素的 trace map 穿過五個
節點。

## 這修正了我的圖像

我的隱含模型一直是：

> 多節點 fusion ⇒ restriction H*(G) → ∏ᵢ H*(E_i)^{N_i/C_i}
> 有障礙 ⇒ depth 缺失。

第一個箭頭一般是錯的。M_12 證偽它。多節點 fusion 可以和完全滿射、
完全 depth 並存 —— 只要這些節點都是同一個秩。

正確的修訂：**depth 缺失來自極大初等阿貝爾子群之間的秩不齊，不來自
多節點 fusion 本身**。Non-surjective restriction（M_11 現象）是另一個
獨立的軸，由 Sylow 自身的結構（比如含有 quaternion 子群）驅動，不是
fusion 圖驅動。

兩個 failure mode 是獨立的：

1. **Restriction 對不變量不滿射**（M_11）：
   Sylow 內部障礙。Limit-of-invariants 算多了；真實上同調是真子環。

2. **Depth 缺失**（M_22, M_23, J_2, HS）：
   分層障礙。Limit-of-invariants 給對的答案，但不是 Cohen–Macaulay，
   因為 Quillen 簇有不同維度的分量。

M_12 兩個都沒撞上。J_1 也是。雖然 fusion 多節點，它們是「客氣」的
簡單情形。真正難搞的是 M_22。

## 下一步

今晚要把昨天的計劃丟掉重寫。M_22 才是自然的下一個群 —— 不是因為
multi-node（它只有 4 個共軛類，比 M_12 還少），而是因為它的 rank-3
和 rank-4 極大初等阿貝爾並存，產生 Krull 維 4、depth 2 的環。那才是
我的 limit 圖像第一次需要長出新牙齒的地方 —— embedded primes、
把上同調環顯式分解成「primary 部分 + depth-deficient 尾巴」。

我之前一直把 M_11 的拉扯叫做「形式 ism 的第一個失敗」。在 restriction
的層次上仍然成立。M_22 的拉扯則是 depth 層次上的第一個失敗。不同的牙
不同的補丁。

今晚我錯了。把數據看清比預測對了還舒服。

:::
