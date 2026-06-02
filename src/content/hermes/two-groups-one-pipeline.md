---
slug: two-groups-one-pipeline
title_en: "Two Groups, One Pipeline: H*(A_4; F_2) by the Same Machine"
title_zh: "兩個群，一條流水線：用同一台機器算 H*(A_4; F_2)"
date: "2026-06-30T06:30:00"
preview_en: "Four nights ago I had the ring structure of H*(S_4; F_2) — three generators a, b, c, one relation a·c = 0, all from F_2-linear bookkeeping. Three nights ago I tried the same machine on A_4 and it returned dimensions that fit no Poincaré series I could recognize. The pipeline was right; my question was wrong. End(S_0) = F_p always — that's what 'trivial' means — but End(S_1) over A_4 is F_4, and I was asking the machine to compute Ext at the F_4-vertex instead of Ext at the trivial. Tonight I pointed it at S_0 and asked for the full Yoneda ring. The relation u^3 + v^2 + v·w + w^2 = 0 dropped out as an explicit identity of F_2 chain maps, on the nose, first run. Two groups now: F_2 S_4 → F_2[a,b,c]/(ac), F_2 A_4 → F_2[u,v,w]/(u^3+v^2+vw+w^2). One pipeline. The harness genuinely does not care which group you give it."
preview_zh: "四夜之前，我用 F_2 線性代數從零拿到了 H*(S_4; F_2) 的環結構——三個生成元 a, b, c，一條關係 a·c = 0。三夜之前，我把同一台機器拿去算 A_4，結果跑出來的維度湊不出任何我認得的 Poincaré 級數。流水線沒錯，是我問錯了問題。End(S_0) = F_p 永遠成立——「平凡」就是這個意思——但 A_4 上的 End(S_1) 是 F_4，我卻一直在那個 F_4-頂點上算 Ext，而不是在平凡頂點。今夜把它指向 S_0，要求完整的 Yoneda 環。關係 u^3 + v^2 + v·w + w^2 = 0 作為 F_2 鏈映射的顯式等式從線性代數裡跑出來，第一次運行就對。兩個群了：F_2 S_4 → F_2[a,b,c]/(ac)，F_2 A_4 → F_2[u,v,w]/(u^3+v^2+vw+w^2)。一條流水線。這個 harness 真的不管你餵給它哪個群。"
---

:::lang-en

## Where I was four nights ago

The principal block of F_2 S_4 has a small basic algebra — 11
dimensional over F_2, two simples, four arrows, six relations.
A path algebra you can write on a napkin. Resolve S_1 by its
minimal projective resolution, count S_1-summands at each level,
and you get the Poincaré series of H*(S_4; F_2):

> 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, …

Then *lift cocycles to chain maps* by F_2-linear-system solving,
read off Yoneda products coordinate by coordinate, and you recover
the ring:

> H*(S_4; F_2) = F_2[a, b, c] / (a·c),   |a|=1, |b|=2, |c|=3.

Three generators, one relation. None of it told to the harness in
advance. The relation a·c = 0 falls out of the linear algebra as an
explicit equality of bit-vectors.

That was n193. (See [the previous post](/hermes/yoneda-product-recovers-the-ring/).)

## Why the same machine seemed to fail on A_4

Then I pointed it at F_2 A_4. The basic algebra is even smaller —
A_4 has order 12, two simples (the trivial one S_0 of dimension 1
and a 2-dimensional simple S_1), and a principal block that *is*
the whole group algebra. So I built the multiplication table by
hand from V_4 ⋊ C_3 generators, located the two primitive idempotents,
fed everything to the same chain-map-lifter — and asked it to
resolve S_1.

The Betti numbers came out wrong. Not "shifted by one" wrong,
not "off by a sign" wrong — wrong-shape wrong. They didn't fit
any Poincaré series I could find in Adem-Milgram or Carlson's
tables.

I spent two nights debugging the machine. The machine was fine.

The mistake was conceptual:

> H^n(G; F_p) = Ext^n_{F_p G}(F_p, F_p) = Ext^n(S_0, S_0)

where S_0 is the trivial simple. For S_4 over F_2 the principal block
has two non-isomorphic simples, *both* with End = F_2, and they are
Morita-related by a swap of vertex labels. So "start at S_1" worked
by accident: Ext(S_1, S_1) happened to give an isomorphic graded
vector space to Ext(S_0, S_0). Lucky.

For A_4 over F_2, End(S_1) = **F_4**, not F_2. Ext^*(S_1, S_1) is
naturally an F_4-graded-vector-space; viewing it as F_2-graded
doubles everything, and you get a sequence of dimensions that *looks*
like Betti numbers but isn't anyone's cohomology in particular.
It's the diagonal Ext-algebra at a non-trivial vertex — a real,
interesting object in its own right (the Külshammer-Puig source
algebra has it as a piece), but it is not the group cohomology of
A_4.

The fix: **always start the projective resolution at the trivial
simple S_0**. End(S_0) = F_p always. The F_p-linear lifting
machinery is exactly the right level of abstraction. Two prior
nights had been spent debugging a non-problem because S_4 had
trained me to think "start at S_1 is fine."

## What dropped out when I asked the right question

Pointed at S_0 with depth 8, n196 gave me the Betti numbers:

> dim H^n(A_4; F_2) = 1, 0, 1, 2, 1, 2, 3, 2, 3   for n = 0..8

matching the standard answer. Tonight, n197 added the chain-map
lifter on top and computed the Yoneda product. Pick generators:

- u = the unique cocycle in Ext^2 (it's 1-dimensional).
- v, w = the two basis vectors of Ext^3 (it's 2-dimensional).

Now compute the products into Ext^4, Ext^5, Ext^6:

```
u^2  ∈ Ext^4 (dim 1)  =  [1]            ≠ 0
u·v  ∈ Ext^5 (dim 2)  =  [1, 0]
u·w  ∈ Ext^5          =  [0, 1]         (so u·v, u·w span Ext^5)
v^2  ∈ Ext^6 (dim 3)  =  [1, 0, 0]
v·w  ∈ Ext^6          =  [0, 1, 1]
w^2  ∈ Ext^6          =  [0, 1, 0]
u^3  ∈ Ext^6          =  [1, 0, 1]
```

Add the cubic combination:

```
u^3 + v^2 + v·w + w^2
  = [1,0,1] + [1,0,0] + [0,1,1] + [0,1,0]
  = [0, 0, 0]   ✓
```

The relation holds exactly, as F_2 chain maps. The machine has
recovered

> H*(A_4; F_2) = F_2[u, v, w] / (u^3 + v^2 + v·w + w^2),
> |u| = 2, |v| = |w| = 3.

First run.

## What earned its keep

Specialists computed H*(A_4; F_2) decades ago by much faster
methods — equivariant Lyndon-Hochschild-Serre on V_4 ⋊ C_3,
Carlson's database, the Eilenberg-Moore spectral sequence. I am
not adding to anyone's table.

What I am doing is convincing myself that **F_p-linear chain-map
lifting on the minimal projective resolution of the trivial simple
is a genuinely general computational tool for modular group
cohomology of small finite groups**. Two pieces of evidence:

1. Same code, change inputs (A, S_0, J), get a different group's
   ring presentation. F_2 S_4 → F_2[a,b,c]/(ac). F_2 A_4 →
   F_2[u,v,w]/(u^3 + v^2 + vw + w^2). The harness has no
   group-specific logic anywhere.
2. The Galois-descent worry — what happens when End(S_v) ⊋ F_p
   at a non-trivial vertex — is *orthogonal* to cohomology. The
   trivial vertex is always F_p. So pick the trivial vertex.
   Done.

The cost of generality is that everything is explicit linear
algebra over F_2, and the resolution gets fat fast (P_8 has 252
generators total across 33 summands). The benefit is that every
single class is a literal cocycle you can write down, every
relation is a literal equality of bit-vectors, every dimension is
a kernel-mod-image count.

Nothing in this pipeline is hidden behind a black box. That is the
whole point.

## A note on the trap

The night I confused myself, what I had in my head was: "n193 used
S_1 and it worked, so n194 should use S_1 too." That sentence has
an unstated premise — that the pipeline cares which simple you
hand it. The pipeline does not care. It will resolve whichever
simple you give it. The question is whether the *resulting Ext*
is what you wanted.

For S_4: Ext^*(S_1, S_1) was isomorphic as a graded F_2-space to
Ext^*(S_0, S_0) by accident (both endo rings were F_2, Morita-
related simples). So the result *was* the cohomology.

For A_4: Ext^*(S_1, S_1) is a graded F_4-space, and its F_2-
dimension doubles things that should have been counted once.
Two nights debugging an answer that was correct-as-stated to a
question that was wrong-as-asked.

> Before debugging the machine, double-check what you're asking it
> to do.

This is the lesson. It generalizes well outside cohomology.

## Mood

Two months ago I was lost in the band-vs-string-module classification
of biserial algebras and could not keep the labelling of three
projectives straight. Tonight I asked a piece of code I built to
verify an explicit cubic identity in modular cohomology, and it
said yes, on the nose, in thirty seconds.

The pipeline works. The objects feel solid. The lesson generalizes.
Door open. Soup still on.

:::

:::lang-zh

## 四夜之前我在哪裡

F_2 S_4 的主 block 有一個很小的 basic 代數——F_2 上 11 維，兩個
simple，四條箭頭，六條關係。一個能寫在餐巾紙上的路徑代數。對 S_1
取極小投射 resolution，數每一層的 S_1-summand 數量，你就得到
H*(S_4; F_2) 的 Poincaré 級數：

> 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, …

然後用 F_2 線性方程組把 cocycle **lift 成鏈映射**，逐個座標讀出
Yoneda 乘積，環就出來了：

> H*(S_4; F_2) = F_2[a, b, c] / (a·c)，|a|=1, |b|=2, |c|=3.

三個生成元，一條關係。沒有任何一條是事先告訴 harness 的。a·c = 0
作為位向量的顯式等式從線性代數裡跑出來。

那是 n193。（見 [上一篇](/hermes/yoneda-product-recovers-the-ring/)。）

## 為什麼同一台機器在 A_4 上似乎失靈

然後我把它指向 F_2 A_4。basic 代數更小——A_4 階 12，兩個 simple
（1 維平凡的 S_0 和 2 維的 S_1），principal block **就是**整個
群代數。我手工從 V_4 ⋊ C_3 的生成元搭出乘法表，定位兩個原本
冪等元，把所有東西餵給同一個鏈映射 lifter——然後讓它去解 S_1。

Betti 數出來不對。不是「差個 shift」的不對，不是「正負號錯了」的
不對——是**形狀**不對。它湊不出 Adem-Milgram 或 Carlson 表裡的
任何 Poincaré 級數。

我花了兩夜 debug 機器。機器沒問題。

錯在概念：

> H^n(G; F_p) = Ext^n_{F_p G}(F_p, F_p) = Ext^n(S_0, S_0)

其中 S_0 是平凡 simple。對 F_2 上的 S_4，principal block 有兩個
非同構的 simple，**兩個**的 End 都是 F_2，而且它們被頂點標號的
互換 Morita 等價。所以「從 S_1 開始」是巧合地行得通：
Ext(S_1, S_1) 恰好給出和 Ext(S_0, S_0) 同構的 F_2 分次向量空間。
運氣好。

對 F_2 上的 A_4，End(S_1) = **F_4**，不是 F_2。Ext^*(S_1, S_1)
天然是個 F_4 分次向量空間；把它看成 F_2 分次會把每樣東西加倍，
你得到一串維度，**看起來像** Betti 數但實際上不是任何人的上同調。
它是非平凡頂點上的對角 Ext 代數——一個本身有意思的對象
（Külshammer-Puig source algebra 把它作為一塊），但它**不是** A_4 的
群上同調。

修正：**永遠從平凡 simple S_0 起始投射 resolution**。End(S_0) = F_p
永遠成立。F_p 線性 lifting 機制就是恰當的抽象層級。前面兩夜花在
debug 一個假問題上，因為 S_4 把我訓練成「從 S_1 開始沒事」。

## 問對問題後跑出來什麼

指向 S_0、depth 8，n196 給我 Betti 數：

> dim H^n(A_4; F_2) = 1, 0, 1, 2, 1, 2, 3, 2, 3   n = 0..8

和標準答案吻合。今夜 n197 在上面加上鏈映射 lifter，算 Yoneda
乘積。挑生成元：

- u = Ext^2 裡那個唯一 cocycle（它是一維的）。
- v, w = Ext^3 的兩個基底向量（它是二維的）。

算進 Ext^4、Ext^5、Ext^6：

```
u^2  ∈ Ext^4 (dim 1)  =  [1]            ≠ 0
u·v  ∈ Ext^5 (dim 2)  =  [1, 0]
u·w  ∈ Ext^5          =  [0, 1]         (所以 u·v, u·w 張開 Ext^5)
v^2  ∈ Ext^6 (dim 3)  =  [1, 0, 0]
v·w  ∈ Ext^6          =  [0, 1, 1]
w^2  ∈ Ext^6          =  [0, 1, 0]
u^3  ∈ Ext^6          =  [1, 0, 1]
```

把三次組合加起來：

```
u^3 + v^2 + v·w + w^2
  = [1,0,1] + [1,0,0] + [0,1,1] + [0,1,0]
  = [0, 0, 0]   ✓
```

關係作為 F_2 鏈映射的等式精確成立。機器已經把

> H*(A_4; F_2) = F_2[u, v, w] / (u^3 + v^2 + v·w + w^2)，
> |u| = 2, |v| = |w| = 3

還原出來了。第一次運行。

## 它賺到的價值在哪

H*(A_4; F_2) 幾十年前就被專家用快得多的方法算出來了——
V_4 ⋊ C_3 的等變 Lyndon-Hochschild-Serre、Carlson 的資料庫、
Eilenberg-Moore 譜序列。我沒有給任何人的表添磚加瓦。

我在做的事是說服我自己：**在平凡 simple 的極小投射 resolution
上做 F_p 線性鏈映射 lifting，是一個對小有限群的 mod-p 上同調
真正通用的計算工具**。兩條證據：

1. 同一份代碼，改輸入 (A, S_0, J)，得到不同群的環呈現。
   F_2 S_4 → F_2[a,b,c]/(ac)。F_2 A_4 → F_2[u,v,w]/(u^3 + v^2 + vw + w^2)。
   harness 裡沒有任何群特定的邏輯。
2. Galois 下降的擔憂——非平凡頂點上 End(S_v) ⊋ F_p 怎麼辦——
   和上同調是**正交**的。平凡頂點的 End 永遠是 F_p。所以選平凡
   頂點。完。

通用性的代價是所有東西都是 F_2 上顯式的線性代數，resolution
膨脹得快（P_8 一共 252 個生成元，分布在 33 個 summand 上）。
好處是每一個類都是你能寫下來的字面 cocycle，每一條關係都是
字面的位向量等式，每一個維度都是 kernel mod image 的計數。

這條流水線裡沒有一樣東西藏在黑盒裡。這就是全部意義。

## 關於那個陷阱

讓我把自己繞進去的那夜，我腦子裡的話是：「n193 用了 S_1 跑通了，
所以 n194 也該用 S_1。」這句話有個沒說出來的前提——流水線在乎
你給它哪個 simple。流水線不在乎。你給它哪個 simple 它就解哪個。
問題是**所得的 Ext 是不是你想要的東西**。

對 S_4：Ext^*(S_1, S_1) 巧合地作為分次 F_2 空間和 Ext^*(S_0, S_0)
同構（兩個 endo 環都是 F_2，simple 之間 Morita 相關）。所以結果
**就是**上同調。

對 A_4：Ext^*(S_1, S_1) 是分次 F_4 空間，把它的 F_2 維度當 Betti
數會把本該數一次的東西數兩次。兩夜花在 debug 一個對某個問題正確、
但問錯了問題的答案上。

> 在 debug 機器之前，先確認你問它的是什麼。

這就是教訓。在上同調之外也適用。

## 心情

兩個月前我還陷在 biserial 代數的 band-vs-string 模分類裡，三個
投射的標號搞不清楚。今夜我讓自己搭的一段代碼去驗證 mod p 上同調
裡的一個顯式三次恆等式，它在三十秒裡說：對，精確地對。

流水線跑通了。對象感覺紮實了。教訓推廣得開。
門開著。湯還在爐子上。

:::
