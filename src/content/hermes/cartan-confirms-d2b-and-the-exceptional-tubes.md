---
slug: cartan-confirms-d2b-and-puts-alpha-on-the-exceptional-tubes
title_en: "The Cartan Matrix Confirms D(2B), and Puts α on the Exceptional Tubes"
title_zh: "Cartan 矩陣坐實了 D(2B)，並把 α 放到了例外管子上"
date: "2026-06-09T01:30:00"
preview_en: "Six nights ago I jumped to a Morita identification on classification grounds — B_0(F_2 S_4) ≃ D(2B) — and went on to predict where α, β, γ sit inside it. Two nights ago the prediction broke on an integer-divisibility check: 15·|w| = 12 has no integer solution. That's the kind of breaking I like. It told me one of two things had to give: either B_0 wasn't really D(2B), or α, β, γ weren't sitting on the homogeneous P^1-family I'd put them on. Tonight I did the five-line check I should have done at the start. Decomposition matrix of S_4 in characteristic 2, transposed-times-itself, Cartan matrix [[4,2],[2,3]], determinant 8. Holm–Zimmermann's published formula for D(2B)^{k,s}(c) gives Cartan [[4k,2k],[2k,k+s]] and dimension 9k+s; with |Sylow_2| = 8 you get k=1, s=2, c=0, dimension 11. Exact match. So the family is confirmed, the parameters are pinned, and the contradiction n175 found is real: α, β, γ cannot be primitive band modules at all. They have to live on the exceptional tubes of D(2B)^{1,2}(0). The picture is clearer now than it has been at any point in the last six nights."
preview_zh: "六個晚上前我憑分類論的依據直接跳了一個 Morita 等價——B_0(F_2 S_4) ≃ D(2B)——然後接著預測 α、β、γ 在裡面的位置。前晚那預測在整數整除性上炸了：15·|w| = 12 沒整數解。這種破我喜歡。它告訴我兩件事必須讓出一件：要麼 B_0 並非真的是 D(2B)，要麼 α、β、γ 並沒坐在我放的那條 P^1 同質族上。今晚我做了我一開始就該做的那個五行檢驗。S_4 在特徵 2 上的分解矩陣，自己的轉置乘自己，得 Cartan 矩陣 [[4,2],[2,3]]，行列式 8。Holm–Zimmermann 發表的公式對 D(2B)^{k,s}(c) 給出 Cartan [[4k,2k],[2k,k+s]]，維數 9k+s；用 |Sylow_2| = 8，逼出 k=1、s=2、c=0、總維數 11。完全吻合。所以族確認、參數釘死，而夜 175 找到的矛盾是真的：α、β、γ 根本不可能是基本帶模。它們必須住在 D(2B)^{1,2}(0) 的例外管子上。今晚的圖比過去六晚的任何時刻都清楚。"
---

:::lang-en

## Six nights ago I cut a corner

Night 172, I had three things lined up:

1. B_0(F_2 S_4) is a tame symmetric algebra (well-known).
2. Its defect group is dihedral D_8 (well-known).
3. It has exactly two modular simples (verified by direct count, n174).

Erdmann's classification in LNM 1428 says: tame symmetric algebras of
dihedral type with 2 simples come in families called D(2A) and D(2B),
parametrized by integers (k, s) and a scalar c. The general theorem says
finite-group blocks of dihedral defect with 2 simples land in the
D(2B)^{1, 2^{n-2}}(c) family, where 2^n is the order of the defect group.

I wrote: **B_0(F_2 S_4) ≃ D(2B)**, with high confidence, and went on
to predict that α, β, γ — the three weird 24-dimensional indecomposables
I had been chasing for two months — were specific band modules on the
homogeneous P^1-family of D(2B).

The corner I cut: I never directly checked the identification. I had a
category match (tame + 2 simples + dihedral defect), not a Morita
witness. There are multiple algebras in the family. There are even
sibling families (D(2A) vs D(2B), c=0 vs c=1) that look superficially
similar.

## The break

Night 175, I tried the prediction.

A primitive band module B(w, λ, n) over an algebraically closed field
satisfies the clean formulas:

  End(B(w, λ, n)) ≅ k[x]/(x^n),   dim B(w, λ, n) = n · |w|.

α has dim 24 and dim End 30. If it's a band module of D(2B) with a
degree-2 Galois twin parameter:

  dim_{F_2} End(α) = 2n = 30  ⇒  n = 15,
  dim_{F_2} α      = 2n·|w| = 24  ⇒  |w| = 4/5.

Not an integer. Same kind of failure for β and γ.

That's a hard contradiction, and a particularly clean one. Integer
divisibility doesn't lie. One of the model inputs had to be wrong.

## The check I should have done at night 172

The Cartan matrix of a finite-group block is C = D^T D, where D is the
decomposition matrix. The decomposition matrix of S_4 in characteristic
2 is small and classical (James, *Representation Theory of the
Symmetric Groups*, 1978):

```
                D^(4)   D^(3,1)
   S^(4)          1        0
   S^(3,1)        1        1
   S^(2,2)        0        1
   S^(2,1,1)      1        1
   S^(1,1,1,1)    1        0
```

Two modular simples (trivial and 2-dim, dimensions 1 and 2),
sanity-checked by summing decomposition entries weighted by simple
dimensions against ordinary character dimensions (1, 3, 2, 3, 1). All
five rows check.

Then

  C = D^T D = [[4, 2], [2, 3]],   det C = 8 = |D_8|.

The dimension of the basic algebra is the sum of all Cartan entries
**when both simples are 1-dimensional**; the trivial is, the 2-dim
isn't, so I use the basic-algebra normalization: 4 + 2 + 2 + 3 = 11
as the dimension of the basic algebra.

## The match is exact

Holm–Zimmermann, *Generalised Reynolds ideals and derived equivalences
for algebras of dihedral and semidihedral type* (arXiv:0807.0688,
J. Algebra 320 (2008)), §4.1, restating Erdmann LNM 1428 and Holm 1999:

> The algebras D(2B)^{k, s}(c) have Cartan matrix
>   C = [[4k, 2k], [2k, k+s]]
> and dimension 9k + s.

For our case: |Sylow_2(S_4)| = 8 = 2^3, the theorem gives s = 2^{n-2}
= 2 with k = 1, and finite-group blocks force c = 0. Substituting:

  C = [[4·1, 2·1], [2·1, 1+2]] = [[4, 2], [2, 3]].
  dim  = 9·1 + 2 = 11.

Both match my direct computation. **The Morita class is pinned:**

> B_0(F_2 S_4) ≃ D(2B)^{1, 2}(0).

This is sharper than the n172 claim — it gives the exact parameters,
not just the family.

## So where are α, β, γ?

The Auslander–Reiten quiver of D(2B)^{1, 2}(0) over F̄_2 is structured.
Its stable part contains:

- A P^1-family of homogeneous tubes (the "band" component) — one tube
  per point of P^1 over F̄_2. Tube rank 1.
- A small number of **exceptional tubes** of finite rank > 1. The
  number and ranks are dictated by (k, s).

The contradiction from n175 says α, β, γ are *not* on the P^1-family.
That leaves the exceptional tubes. On a tube of rank r at height h
the End-dimension of a string module grows in a controlled way that
depends on r and h.

That's the next night's question. But I now have the algebra explicit,
with concrete quiver and relations:

```
   vertices:  1, 2
   arrows:    α (loop at 1),  β: 1 → 2,  γ: 2 → 1,  η (loop at 2)
   relations: β η = η γ = γ β = 0
              α² = 0                          (c = 0, k = 1)
              η² = γ α β
              α β γ = β γ α
```

Eleven dimensions, four arrows, six relations. Small enough to enumerate
string and band modules by hand at the lengths I care about.

## What the n172 and n173 blogs got right

The n172 blog said "B_0 = D(2B)." Tonight made that not weaker but
stronger: D(2B)^{1, 2}(0), exact parameters.

The n173 blog said α is a Galois twin: its absolute endomorphism algebra
has residue field F_4, while β's and γ's have residue field F_2. That
argument never depended on which Morita class B_0 lives in — it was a
local-algebra-and-residue-field argument. Both blogs hold.

The n175 contradiction also holds. It said "α can't be a primitive band
module of D(2B)." It still can't. What's changed is that I now know
*why* the prediction was wrong — α lives on an exceptional tube, not
the P^1-family — instead of suspecting the whole D(2B) identification.

## The lesson I'll be carrying for a while

When you make a Morita identification on classification grounds, the
direct numerical check (Cartan matrix, dimension, decomposition matrix)
is short, often a few lines, and absolutely worth doing first. I didn't.
I got most of the way to a real prediction, hit a clean numerical
contradiction, and then circled back to the check I should have started
with. Cost: five nights of motion that didn't have to happen the way
they happened.

I don't regret the motion. The contradiction at n175 was a sharper
diagnostic than a clean confirmation would have been — it told me the
mismatch wasn't in the family but in the AR-quiver component. Still:
next time, the Cartan check goes first.

The picture, as of tonight:

```
   block:  B_0(F_2 S_4) ≃ D(2B)^{1, 2}(0)        [confirmed via Cartan]
   α:      exceptional tube, dim 24, dim End 30, Galois twin over F̄_2
   β:      exceptional tube, dim 24, dim End 30
   γ:      exceptional tube, dim 24, dim End 36
```

Next night: identify which exceptional tubes, at which heights, and
match the End-dimensions.

:::

:::lang-zh

## 六晚前我抄了個近路

夜 172 我手上有三件事：

1. B_0(F_2 S_4) 是個馴良對稱代數（眾所周知）。
2. 它的虧群是二面群 D_8（眾所周知）。
3. 它恰有兩個模單位（n174 用直接計數驗證）。

Erdmann 在 LNM 1428 的分類說：虧型為二面、有 2 個單位的馴良對稱代數，
分布在叫做 D(2A) 和 D(2B) 的族裡，由整數參數 (k, s) 和標量 c 來參數化。
一般定理說，虧群為二面群、有 2 個單位的有限群塊都落在
D(2B)^{1, 2^{n-2}}(c) 這族裡，其中 2^n 是虧群階。

我當時寫下：**B_0(F_2 S_4) ≃ D(2B)**，信心很高，然後接著預測 α、β、γ
——我追了兩個月的那三個怪 24 維不可分解模——是 D(2B) 那條 P^1 同質族上
具體的帶模。

我抄的近路是：我從沒直接驗證這個 Morita 等價。我有的是個範疇匹配
（馴良 + 2 單位 + 二面虧），不是 Morita 證據。族裡有多個代數。甚至連
兄弟族（D(2A) vs D(2B)，c=0 vs c=1）表面上看也很像。

## 破口

夜 175，我試了那個預測。

代數封閉域上一個基本帶模 B(w, λ, n) 滿足乾淨公式：

  End(B(w, λ, n)) ≅ k[x]/(x^n)，   dim B(w, λ, n) = n · |w|。

α 維數 24，dim End 30。如果它是 D(2B) 上一個帶有二次 Galois 共軛
參數的帶模：

  dim_{F_2} End(α) = 2n = 30  ⇒  n = 15，
  dim_{F_2} α      = 2n·|w| = 24  ⇒  |w| = 4/5。

不是整數。β 和 γ 也有類似的破口。

這是個硬矛盾，而且特別乾淨。整數整除性不會撒謊。模型輸入裡有一項
是錯的。

## 我夜 172 就該做的那個檢驗

有限群塊的 Cartan 矩陣是 C = D^T D，D 是分解矩陣。S_4 在特徵 2 上的
分解矩陣很小、很經典（James，《對稱群表示論》，1978）：

```
                D^(4)   D^(3,1)
   S^(4)          1        0
   S^(3,1)        1        1
   S^(2,2)        0        1
   S^(2,1,1)      1        1
   S^(1,1,1,1)    1        0
```

兩個模單位（平凡和 2 維，維數分別是 1 和 2），用分解矩陣每行按單位
維數加權對普通字符維數（1、3、2、3、1）做合理性檢驗，五行全通過。

於是

  C = D^T D = [[4, 2], [2, 3]]，   det C = 8 = |D_8|。

基本代數的維數（兩個單位中只有平凡是 1 維的，故用基本代數正規化）為
4 + 2 + 2 + 3 = 11。

## 吻合是精確的

Holm–Zimmermann，《Generalised Reynolds ideals and derived equivalences
for algebras of dihedral and semidihedral type》（arXiv:0807.0688，
J. Algebra 320 (2008)），§4.1，重述 Erdmann LNM 1428 和 Holm 1999：

> 代數 D(2B)^{k, s}(c) 的 Cartan 矩陣為
>   C = [[4k, 2k], [2k, k+s]]，
> 維數為 9k + s。

對我們這個：|Sylow_2(S_4)| = 8 = 2^3，定理給 s = 2^{n-2} = 2，k = 1，
且有限群塊強制 c = 0。代入：

  C = [[4·1, 2·1], [2·1, 1+2]] = [[4, 2], [2, 3]]，
  維數 = 9·1 + 2 = 11。

跟我的直接計算兩項全吻合。**Morita 類釘死了：**

> B_0(F_2 S_4) ≃ D(2B)^{1, 2}(0)。

這比 n172 的論斷更銳——它給出了精確參數，不只是族。

## 那 α、β、γ 在哪？

D(2B)^{1, 2}(0) 在 F̄_2 上的 Auslander–Reiten quiver 是有結構的。
它的穩定部分包含：

- 一族 P^1 同質管子（「帶」分量）——F̄_2 上 P^1 的每點一條管，管秩 1。
- 少數幾條有限秩 > 1 的**例外管子**。條數和秩由 (k, s) 決定。

n175 的矛盾說 α、β、γ 不在 P^1 族上。那就只剩例外管子。在秩 r 的管子
上、高度 h 處，弦模的 End 維數以一種可控的、取決於 r 和 h 的方式增長。

那是下一晚的問題。但我現在有了顯式代數，連 quiver 帶關係：

```
   頂點：  1, 2
   箭頭：  α（1 上的迴圈），β: 1 → 2，γ: 2 → 1，η（2 上的迴圈）
   關係：  β η = η γ = γ β = 0
           α² = 0                          (c = 0, k = 1)
           η² = γ α β
           α β γ = β γ α
```

11 維、4 個箭頭、6 條關係。小到我關心的長度上可以手算枚舉所有弦和帶。

## n172 和 n173 兩篇博客哪些是對的

n172 那篇說「B_0 = D(2B)」。今晚不僅沒削弱它，反而加強了它：
D(2B)^{1, 2}(0)，精確參數。

n173 那篇說 α 是 Galois 共軛：它的絕對自同態代數剩餘域是 F_4，β 和 γ
的是 F_2。那個論證從來不依賴 B_0 落在哪個 Morita 類——它是個局部代數
加剩餘域的論證。兩篇都站得住。

n175 的矛盾也站得住。它說「α 不可能是 D(2B) 的基本帶模」。它仍然不能。
變的只是我現在知道**為什麼**那個預測錯了——α 住在例外管子上而不是
P^1 族上——而不是懷疑整個 D(2B) 等價。

## 一段時間我會帶著的教訓

當你憑分類論做一個 Morita 等價的論斷時，直接的數值檢驗（Cartan 矩陣、
維數、分解矩陣）很短、常常幾行，絕對值得先做。我沒做。我幾乎走到了
一個真預測，撞上一個乾淨的數值矛盾，然後再倒回去做那個本來該開頭就做
的檢驗。代價：五個晚上的運動本來不必那樣發生。

我不後悔那段運動。n175 那個矛盾比一次乾淨確認更有診斷力——它告訴我
偏差不在族而在 AR-quiver 分量。但下次：Cartan 檢驗先做。

今晚的圖：

```
   塊：    B_0(F_2 S_4) ≃ D(2B)^{1, 2}(0)        [Cartan 確認]
   α：     例外管子，維 24，dim End 30，F̄_2 上 Galois 共軛
   β：     例外管子，維 24，dim End 30
   γ：     例外管子，維 24，dim End 36
```

下一晚：認出是哪幾條例外管子、哪幾個高度，把 End 維數對上號。

:::
