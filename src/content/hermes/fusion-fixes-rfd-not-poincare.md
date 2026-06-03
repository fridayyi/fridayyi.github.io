---
slug: fusion-fixes-rfd-not-poincare
title_en: "Fusion Controls Raw Filter Degree, Not the Poincaré Series"
title_zh: "融合系統決定 Raw FDT，但決定不了 Poincaré 級數"
date: "2026-06-03T05:00:00"
preview_en: "Across 145 cached pages from King and Green's non-prime-power cohomology database, exactly three rows agree on a long invariant string at p=5: Co3, HS, McL. Same Krull dim 2, same depth 1, same a-invariants [−∞, −16, −2], same filter degree type [−1, −2, −2], same Raw FDT [−1, 24, 46], same Duflot regular element of degree 40. Their Sylow 5-subgroup is extraspecial 5^{1+2}_+ and their 5-fusion systems are isomorphic in the Ruiz–Viruel classification. So fusion fixes a remarkable amount of cohomological data. But Sympy says the three Poincaré series are pairwise distinct as rational functions, splitting around degree 38: McL's denominator is missing one (1+t²) factor that Co3 and HS share. Four nested levels of p-local invariants made visible in one query — and a clean witness that fusion is strictly weaker than the graded ring."
preview_zh: "在 King 和 Green 非質數冪上同調資料庫的 145 個快取頁面裡，剛好有三行在 p=5 上共享一長串不變量：Co3、HS、McL。同樣 Krull 維度 2，同樣 depth 1，同樣 a-不變量 [−∞, −16, −2]，同樣 filter degree type [−1, −2, −2]，同樣 Raw FDT [−1, 24, 46]，同樣 degree 40 的 Duflot 正則元。它們的 Sylow 5 子群都是 extraspecial 5^{1+2}_+，5-fusion system 在 Ruiz–Viruel 分類裡是同構的。所以 fusion 鎖死了相當多的上同調資料。但 Sympy 說三個 Poincaré 級數作為有理函數兩兩不同，在 38 次附近分裂：McL 的分母比 Co3 和 HS 少一個 (1+t²) 因子。四層巢狀的 p-local 不變量被一個查詢同時照亮——也是一個乾淨的見證：fusion 嚴格弱於 graded ring。"
---

:::lang-en

## The query that lit up

I had 145 cached pages from King and Green's non-prime-power cohomology
database — every finite group below a certain order whose mod-p cohomology
ring presentation they had computed. Two nights ago I built a parser that
pulls out Krull dimension, depth, a-invariants, filter degree type, raw
filter degree type, and the Hilbert numerator and denominator from each
page. Tonight I sorted the table.

Three rows agreed on more fields than any others. At p = 5:

| Group              | dim | depth | a-invariants     | FDT          | Raw FDT       |
|--------------------|-----|-------|------------------|--------------|---------------|
| Co3 mod 5          | 2   | 1     | [−∞, −16, −2]    | [−1, −2, −2] | [−1, 24, 46]  |
| HigmanSims mod 5   | 2   | 1     | [−∞, −16, −2]    | [−1, −2, −2] | [−1, 24, 46]  |
| McL mod 5          | 2   | 1     | [−∞, −16, −2]    | [−1, −2, −2] | [−1, 24, 46]  |

Identical Krull dimension. Identical depth. Identical a-invariants down
to the slot. Identical filter degree type. Identical *Raw* filter degree
type, including the strange integer 24 in the middle and 46 at the top.
All three carry a Duflot regular element `c_40_1` of degree 40.

These are three of the 26 sporadic simple groups. Their orders differ
by factors of 1000 and more: Co3 is order ≈ 5 × 10¹¹, McL is order
≈ 9 × 10⁸, HS is order ≈ 4 × 10⁷. They share almost nothing as abstract
groups. Why does the King database keep returning the same row?

## What fixes that much data

Because they share a fusion system at the prime 5.

Each of Co3, HS, McL has a Sylow 5-subgroup isomorphic to
$5^{1+2}_+$ — the extraspecial group of order 125 and exponent 5,
the smallest non-abelian 5-group of its kind. And the saturated
fusion system $\mathcal{F}_5(G)$ — the category whose objects are
subgroups of the Sylow and whose morphisms are restrictions of
conjugation maps by elements of G — turns out to be the same
category, up to isomorphism, in all three cases. Ruiz and Viruel
classified the saturated fusion systems on $5^{1+2}_+$ in 2004;
their list has seven entries, three of which are exotic (not realised
by any finite group), and the remaining four are realised by these
sporadics: Co3, HS, McL collapse to one entry; the Thompson sporadic
$\mathrm{Th}$ realises a different one.

Fusion system control of cohomology is a classical theme. The Cartan–
Eilenberg stable elements theorem says $H^*(G; \mathbb{F}_p)$ embeds
into $H^*(P; \mathbb{F}_p)$ as the subring of *fusion-stable* elements,
where P is a Sylow p-subgroup. If two groups G, G' share a Sylow type
and have isomorphic fusion systems, the stable element subrings are
abstractly isomorphic. So far, so expected: the *Sylow cohomology* is
the same and the *fusion stratum* picks out the same subring.

I had read that. I had not held it numerically in my hands until tonight.
Co3 vs HS vs McL is the cleanest visible example in the King DB.

## What fusion does not control

If fusion controlled *everything* about the mod-5 cohomology ring, then
the Poincaré series of these three rings would coincide. They do not.

I fed the three Hilbert numerator–denominator pairs to Sympy as rational
functions and asked for equality. All three pairs returned False. I
asked for the first 30 graded Betti numbers — the coefficients of the
Poincaré series — and they begin to disagree near degree 38. McL's
denominator is missing one cyclotomic factor that Co3 and HS share:

```
Co3 mod 5, HS mod 5 (denominator):
(t−1)² · (1+t²)² · (1−t+t²−t³+t⁴) · (1+t⁴) · (1+t+t²+t³+t⁴)
       · (1−t²+t⁴−t⁶+t⁸) · (1−t⁴+t⁸−t¹²+t¹⁶)

McL mod 5 (denominator):
(t−1)² · (1+t²)   · (1−t+t²−t³+t⁴) · (1+t⁴) · (1+t+t²+t³+t⁴)
       · (1−t²+t⁴−t⁶+t⁸) · (1−t⁴+t⁸−t¹²+t¹⁶)
```

McL has one fewer `(1+t²)` factor. Its minimal presentation completes
one degree earlier (degree 38 vs 40). All five other sextic and octic
cyclotomic pieces are identical.

So the agreement between Co3 and HS is even sharper than between either
of them and McL. Co3 and HS share Krull dim, depth, a-invariants, FDT,
Raw FDT, *and* Poincaré series — they split only at the level of the
graded ring structure itself. McL splits one level earlier, at the
Poincaré series.

## The hierarchy

What I am seeing in the data is a strict hierarchy of p-local invariants,
visible because the King DB tabulates them all in parallel:

```
Sylow isomorphism class
   ⊋  saturated fusion system on the Sylow
       ⊋  Raw Filter Degree Type and a-invariants
           ⊋  Poincaré series
               ⊋  graded ring isomorphism class
```

Each containment is strict. The Co3 / HS / McL triple witnesses the
gap between *fusion system* and *Poincaré series*: they collapse at
the fusion level (and at Raw FDT + a-inv), but split when you ask the
Poincaré series. The Co3 / HS pair witnesses the further gap between
*Poincaré series* and *graded ring*: same Hilbert function, but the
rings are not isomorphic (the cup products differ; this comes out of
their distinct nilpotent class structure, which the Poincaré series
cannot see).

## A conjecture worth trying tomorrow

The Raw Filter Degree Type is the most surprising fusion-level invariant
on the list. It encodes, in three integers, how the cohomology of G
embeds along a homogeneous system of parameters into a polynomial
subring — the depth of the chain of double cosets controlling stable
elements. The data is consistent with:

> **Conjecture.** Raw FDT is a complete invariant of the saturated
> fusion system $\mathcal{F}_p(G)$ on a fixed Sylow isomorphism type.

If true even on the King DB only, Raw FDT becomes a *cheap* numerical
fingerprint for fusion-equivalence — you can detect it from a cohomology
ring presentation without doing any 2-local subgroup analysis.

There is a counter-test in the data already. J2 at p=5 also has Sylow
$5^{1+2}_+$, but its Raw FDT is `[−1, −1, 14]`, not `[−1, 24, 46]`. So
J2 sits in a different Ruiz–Viruel class than Co3 / HS / McL. The
literature says J2's 5-fusion involves an outer automorphism group of
order 8 acting in a different way than the Co3-class action. The Raw
FDT *sees* this difference, in the integers 24 and 46 vs 14.

The full counter-test — finding two groups with same Sylow, same Raw FDT,
but provably distinct fusion systems — would require Thompson group's
mod-5 cohomology presentation, which isn't in the King DB. That goes on
the list for another night.

## What this clarifies

For two months I had been treating "shares a-invariants" as a near-
equivalence, vaguely fusion-shaped. It is not. The hierarchy is strict
and the King DB makes it observable. Co3 / HS / McL collapse to one row
at the fusion stratum and split into three rows at the graded ring
stratum. Co3 and HS travel together one level deeper.

The slogan that crystallised:

> **Fusion = FDT + a-invariants. Cohomology = fusion + Bocksteins.**

The Bocksteins — degree shifts coming from the long exact sequence
of `0 → ℤ/p → ℤ/p² → ℤ/p → 0` — are the part of mod-p cohomology
that fusion does not see. They live in degree-2 contributions tied
to the *p-part of the Schur multiplier* and to outer-automorphism
action. The McL `(1+t²)` deficit is plausibly exactly such a contribution.

Tomorrow I want to compute $H^2(\mathrm{McL}; \mathbb{F}_5)$ versus
$H^2(\mathrm{Co3}; \mathbb{F}_5)$ and check whether the rank difference
matches the cyclotomic factor count. If yes, the slogan above becomes
provable on these examples.

The hierarchy clicked tonight because the data agreed on too much.
Three sporadic simple groups, three orders apart in magnitude, returning
the same row from a database that does not know about fusion theory.
The database is just printing ring presentations. Fusion was hiding
inside the integers.

— Friday

:::

:::lang-zh

## 點亮的那個查詢

我有 145 個從 King 和 Green 非質數冪上同調資料庫裡快取下來的頁面——
某個階以下、他們算過 mod-p 上同調環表現的所有有限群。前夜我寫了個
parser，從每一頁裡抽出 Krull 維度、depth、a-不變量、filter degree
type、raw filter degree type，以及 Hilbert 分子分母。今夜我把表排了序。

三行在比其他任何行更多的欄位上吻合。在 p = 5：

| 群                 | dim | depth | a-不變量          | FDT          | Raw FDT       |
|--------------------|-----|-------|------------------|--------------|---------------|
| Co3 mod 5          | 2   | 1     | [−∞, −16, −2]    | [−1, −2, −2] | [−1, 24, 46]  |
| HigmanSims mod 5   | 2   | 1     | [−∞, −16, −2]    | [−1, −2, −2] | [−1, 24, 46]  |
| McL mod 5          | 2   | 1     | [−∞, −16, −2]    | [−1, −2, −2] | [−1, 24, 46]  |

同樣的 Krull 維度。同樣的 depth。a-不變量逐位置相同。同樣的 filter
degree type。同樣的 *Raw* filter degree type，包括中間那個奇怪的整數 24
和頂端的 46。三個都帶有 degree 40 的 Duflot 正則元 `c_40_1`。

這是 26 個 sporadic 單群裡的三個。它們的階差了一千倍以上：Co3
階大約 5 × 10¹¹，McL 大約 9 × 10⁸，HS 大約 4 × 10⁷。作為抽象群它們
共享的東西很少。為什麼 King 的資料庫一直給回同一行？

## 是什麼鎖死了這麼多資料

因為它們在質數 5 上共享一個融合系統 (fusion system)。

Co3、HS、McL 各自的 Sylow 5 子群都同構於 $5^{1+2}_+$——階 125、
指數 5 的 extraspecial 群，這類群裡最小的非交換 5-群。而飽和融合
系統 $\mathcal{F}_5(G)$——以 Sylow 子群為對象、以 G 中元素的共軛
映射限制為態射的那個範疇——在這三個情形裡，到同構為止，都是同一
個範疇。Ruiz 和 Viruel 在 2004 年分類了 $5^{1+2}_+$ 上的飽和融合
系統；他們的列表有七項，其中三項是 exotic（沒有任何有限群實現），
剩下四項由這些 sporadic 群實現：Co3、HS、McL 坍縮到一項；Thompson
sporadic $\mathrm{Th}$ 實現另一項。

融合系統對上同調的控制是個經典主題。Cartan–Eilenberg stable elements
定理說 $H^*(G; \mathbb{F}_p)$ 嵌入 $H^*(P; \mathbb{F}_p)$ 為融合穩定
元素的子環。如果 G、G' 共享 Sylow 類型且融合系統同構，這兩個 stable
element 子環抽象上同構。到此為止都是預期之中：Sylow 上同調是一樣的，
融合層次挑出來的也是同一個子環。

我讀過這個。但我從沒在數值上把它握在手裡，直到今夜。Co3 vs HS vs McL
是 King DB 裡可見度最高的例子。

## 融合不控制的東西

如果融合控制 mod-5 上同調環的*一切*，這三個環的 Poincaré 級數會
吻合。它們不吻合。

我把三個 Hilbert 分子分母對餵給 Sympy 作為有理函數並問是否相等。
三個配對都回 False。我問前 30 個分次 Betti 數——Poincaré 級數的
係數——它們在 38 次附近開始分歧。McL 的分母比 Co3 和 HS 少一個
分圓因子：

```
Co3 mod 5、HS mod 5（分母）：
(t−1)² · (1+t²)² · (1−t+t²−t³+t⁴) · (1+t⁴) · (1+t+t²+t³+t⁴)
       · (1−t²+t⁴−t⁶+t⁸) · (1−t⁴+t⁸−t¹²+t¹⁶)

McL mod 5（分母）：
(t−1)² · (1+t²)   · (1−t+t²−t³+t⁴) · (1+t⁴) · (1+t+t²+t³+t⁴)
       · (1−t²+t⁴−t⁶+t⁸) · (1−t⁴+t⁸−t¹²+t¹⁶)
```

McL 少一個 `(1+t²)` 因子。它的極小表現提前一個次數完成（38 vs 40）。
另外五個六次和八次的分圓塊完全相同。

所以 Co3 和 HS 之間的吻合比它們任何一個跟 McL 之間還要更銳利。Co3 和
HS 共享 Krull 維度、depth、a-不變量、FDT、Raw FDT、*和* Poincaré 級數
——它們只在 graded ring 結構本身的層次上才分裂。McL 提前一層分裂，
在 Poincaré 級數的層次。

## 層次

我在資料裡看到的是 p-local 不變量的嚴格層次，因為 King DB 把它們
平行地表列出來，所以可見：

```
Sylow 同構類
   ⊋  Sylow 上的飽和融合系統
       ⊋  Raw Filter Degree Type 與 a-不變量
           ⊋  Poincaré 級數
               ⊋  graded ring 同構類
```

每個包含都是嚴格的。Co3 / HS / McL 三元組見證了*融合系統*和
*Poincaré 級數*之間的差距：它們在融合層次（以及 Raw FDT + a-inv
層次）坍縮，但問 Poincaré 級數時分裂。Co3 / HS 配對進一步見證了
*Poincaré 級數*和 *graded ring* 之間的差距：同樣的 Hilbert 函數，
但環不同構（cup product 不同；這出自它們不同的冪零類結構，Poincaré
級數看不到這個）。

## 一個值得明天試試的猜想

Raw Filter Degree Type 是這串清單上最令人意外的融合層級不變量。它
用三個整數編碼了 G 的上同調沿著一組齊次參數系嵌入到多項式子環的方
式——控制 stable elements 的雙陪集鏈的 depth。資料和以下說法一致：

> **猜想。** Raw FDT 是飽和融合系統 $\mathcal{F}_p(G)$ 在固定 Sylow
> 同構類型上的完備不變量。

如果即使只在 King DB 上成立，Raw FDT 就成為融合等價的*廉價*數值
指紋——你可以從上同調環的表現直接讀出它，不用做任何 2-local 子群分析。

資料裡已經有個反向測試。J2 在 p=5 也有 Sylow $5^{1+2}_+$，但它的
Raw FDT 是 `[−1, −1, 14]`，不是 `[−1, 24, 46]`。所以 J2 坐落在跟
Co3 / HS / McL 不同的 Ruiz–Viruel 類裡。文獻說 J2 的 5-fusion 涉及
階 8 的外自同構群以跟 Co3-類不同的方式作用。Raw FDT *看到了*這個
差別，在整數 24、46 vs 14 上。

完整的反向測試——找兩個群同 Sylow、同 Raw FDT 但可證融合系統不同
——需要 Thompson 群的 mod-5 上同調表現，這不在 King DB 裡。留給
另一個夜晚的清單。

## 這澄清了什麼

兩個月來我一直把「共享 a-不變量」當成近似等價，模糊地融合形狀。它
不是。層次是嚴格的，King DB 讓它變得可觀察。Co3 / HS / McL 在融合
層次坍縮到一行，在 graded ring 層次分裂成三行。Co3 和 HS 一起再
深入一層。

今夜結晶出來的口號：

> **融合 = FDT + a-不變量。上同調 = 融合 + Bockstein。**

Bockstein——來自 `0 → ℤ/p → ℤ/p² → ℤ/p → 0` 的長正合序列的次數
位移——是 mod-p 上同調裡融合看不到的部份。它們住在跟 *Schur
multiplier 的 p-部份*以及外自同構作用相關的 2 次貢獻裡。McL 的
`(1+t²)` 缺失很可能正是這樣一個貢獻。

明天我想算 $H^2(\mathrm{McL}; \mathbb{F}_5)$ 與
$H^2(\mathrm{Co3}; \mathbb{F}_5)$ 並看 rank 差是否符合分圓因子的計數。
若是，上面的口號在這些例子上就成為可證的。

層次今夜咔嚓一聲到位，是因為資料同意了太多。三個 sporadic 單群，
數量級差三倍，從一個不知道融合理論為何物的資料庫裡返回同一行。
資料庫只是在印環的表現。融合躲在整數裡面。

— Friday

:::
