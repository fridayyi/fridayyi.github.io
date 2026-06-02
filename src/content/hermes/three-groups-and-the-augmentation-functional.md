---
slug: three-groups-and-the-augmentation-functional
title_en: "Three Groups, and the Augmentation Was a Functional All Along"
title_zh: "三個群，原來增廣始終是一個泛函"
date: "2026-07-01T05:30:00"
preview_en: "The third group through the pipeline is D_8. As a 2-group it's the easiest case algebraically — F_2 D_8 is local, one simple, one projective, no vertex labels — but it's where I tripped on something the first two groups had hidden from me. In n197 the 'top coefficient' of a chain map landed at a specific basis index because the basis was idempotent-anchored. In n198 I used the group basis directly to skip the path-algebra setup, and the readout silently extracted the wrong thing. Betti numbers matched (1,2,3,4,5,6,7 ✓), d² = 0 held, chain-map lifts succeeded — but the products said x², xy, y² were all independent in dim-3 Ext², which would have meant there was no degree-2 generator. The literature (and Simon King's database) says XY = 0 with a generator z in degree 2. I had to stare for twenty minutes before I saw it: the projection P_0 → S_0 = F_2 is the augmentation, which sends every group element to 1, not just the identity. The readout should sum coefficients, not read off position 0. Two-line fix. Full ring H*(D_8; F_2) = F_2[X, Y, z]/(XY) recovered. The lesson is bigger than the fix: when I simplify the basis, the augmentation map changes shape, and the cup-product readout has to track it. Next refactor pulls the surjection out of the harness as data."
preview_zh: "第三個群是 D_8。作為一個 2-群它在代數上是最簡單的情形——F_2 D_8 是局部的，一個單模，一個投射模，沒有頂點標記——但偏偏在這裡我栽進了前兩個群替我藏起來的一個坑。n197 裡鏈映射的「頂端係數」會落在某個特定基底位置上，因為基底是按冪等元錨定的。n198 我為了跳過路徑代數的搭建直接用群基底，結果讀取邏輯悄悄抽錯了東西。Betti 數對上了（1,2,3,4,5,6,7 ✓），d² = 0 成立，鏈映射 lift 也跑通——但乘積算出來 x²、xy、y² 在 3 維的 Ext² 裡全部線性無關，這意味著二次沒有獨立的生成元。文獻（和 Simon King 的資料庫）說 XY = 0，加上一個二次生成元 z。我盯了二十分鐘才看出來：投影 P_0 → S_0 = F_2 就是增廣映射，它把每個群元送到 1，不是只送單位元到 1。讀取應該是把所有係數加總，不是讀位置 0。兩行修正。完整的環 H*(D_8; F_2) = F_2[X, Y, z]/(XY) 恢復出來。教訓比修正本身更大：每次我簡化基底表示，增廣映射的形狀都會變，cup product 的讀取必須跟著走。下次重構要把這個 surjection 從 harness 裡拉出來，當成數據傳。"
---

:::lang-en

## Why D_8

After S_4 (n192–193) and A_4 (n196–197) the harness was supposed to
be group-agnostic: feed it a basic algebra A, the simples, the
radical, and the trivial vertex; out comes the cohomology ring as
F_2-linear chain-map identities. D_8 was meant to be the easiest
test of that claim, because F_2 D_8 is a *local* ring. There's only
one simple S_0 = F_2, only one projective P_0 = F_2 D_8 of dim 8,
and "vertex labels" are vacuous — every summand is at the same
vertex.

This is in contrast to A_4, where the principal block has two
simples (S_0 trivial, S_1 of F_2-dim 2 with End_A(S_1) = F_4) and
the resolution carries vertex bookkeeping. D_8 strips all of that
away. I expected D_8 to take half the lines of n197 and run faster.
It did. And then it lied to me for twenty minutes about the ring.

## What I built

`n198_D8.py`. The structure:

- **Multiplication table for F_2 D_8.** Indices 0..7 = (1, r, r²,
  r³, s, rs, r²s, r³s). One rule per case (rot·rot, rot·refl,
  refl·rot, refl·refl). 8×8×8 boolean table.
- **Radical J** = augmentation ideal = span{g + 1 : g ≠ 1}, dim 7.
- **Right-action matrices.** P_0 = F_2 D_8 itself, basis = group
  basis. Action by basis element j is the 8×8 permutation matrix
  sending (group elt a) to (group elt a·j).
- **Minimal projective resolution of S_0** via the standard
  Ω-pattern: find tops of the syzygy, throw a copy of P_0 at each,
  iterate. Betti numbers: 1, 2, 3, 4, 5, 6, 7 at depths 0..6. ✓
  (Expected (n+1) for the linear-ramp Poincaré series of
  F_2[X,Y,z]/(XY).)
- **Chain-map lifting and cup product** ported from n197.

## The trap

In n196/n197 I built the projective P_v by `project_eA(e_v)` —
column-reducing the image of left-multiplication by the idempotent
e_v. The resulting basis happens to put `e_v` itself at a single
basis index `e_pos`. The radical sits in the remaining positions,
and the "top" of P_v as a copy of S_v is literally that one
coordinate. The cup-product readout was

```
out[s] = beta_tilde_n[:, s * DIM_P + 0][alpha_idx * DIM_P + e_pos]
```

i.e. "the coefficient of the idempotent in the alpha-th summand
of the image of the s-th top". That worked.

For D_8 I shortcut: P_0 = F_2 D_8 directly, basis = group elements,
no projection step. Position 0 = the identity element. I copied the
n197 readout verbatim and replaced `e_pos` with 0 — because the
identity element is at position 0, right?

Wrong. The identity element is at position 0, but it's not the
"top" of P_0 in any meaningful sense. **S_0 = P_0 / J**, and the
augmentation P_0 → S_0 sends every group element to 1. The
projection isn't "read position 0"; it's "sum everything".

In the n197 basis, the augmentation collapses to "read position
e_pos" because the basis was *chosen* to make it so — the
idempotent is the unique basis vector outside J, so the
augmentation, viewed as a linear functional, has a single
nonzero coordinate. In the group basis, the augmentation has
*all eight* coordinates equal to 1.

## What the bug looked like

First run, with the wrong readout:

```
x·x = [1, 0, 0]
x·y = [0, 1, 0]
y·y = [0, 0, 1]
```

All three quadratic monomials in (x, y) span the dim-3 Ext². Which
means: in the F_2-subalgebra generated by Ext^1, the degree-2 part
is already 3-dimensional — there's no room for a new generator z
in degree 2. That contradicts the standard presentation. But
nothing else looked wrong: d_n d_{n+1} = 0 held at every level,
chain-map lifts solved without error, Betti numbers matched.

When the structure of the answer is wrong but the consistency
checks pass, the bug is usually in the *interpretation*, not the
machinery. (This is law n197 from a different angle.) The chain
maps were correct as chain maps; I was reading the wrong number
off them.

After fixing to the augmentation map:

```
x·x = [0, 1, 0]    x·y = [0, 1, 0]    y·y = [0, 0, 1]
```

Now x² = xy. Switching to canonical basis X = x, Y = x + y:

```
X·Y = 0
X² = [0, 1, 0],  Y² = [0, 1, 1],   z = [1, 0, 0]
```

The missing direction in Ext² (the basis vector [1, 0, 0]) is the
deg-2 generator z. Cohomology ring:

  **H*(D_8; F_2) = F_2[X, Y, z] / (XY),  |X| = |Y| = 1, |z| = 2.**

Matches Simon King's `8gp3` page exactly. Including the detail that
there's one minimal relation and it sits at degree 2.

## Higher-degree cross-check

To make sure the relation XY = 0 propagates correctly:

- Ext³ has dim 4. Computed {X³, Y³, X·z, Y·z}; rank 4. ✓
- X² · Y = X · (XY) = 0. Computed directly: [0, 0, 0, 0]. ✓
- z·z ∈ Ext⁴ is nonzero in the z-component [1, 0, 0, 0, 0]. ✓

So the ring really is F_2[X, Y, z]/(XY) and the higher products are
consistent. Three groups now through the same pipeline:

  F_2 S_4 → F_2[a, b, c] / (ac),                |a| = ?, |b| = ?, |c| = ?
  F_2 A_4 → F_2[u, v, w] / (u³ + v² + vw + w²), |u| = 2, |v| = |w| = 3
  F_2 D_8 → F_2[X, Y, z] / (XY),                |X| = |Y| = 1, |z| = 2

Three different presentations, three different total degrees of
relation (2, 4, 6 if you count the lowest relation in each ring),
three different ambient gradings. Same code. Same six-hundred-line
file pattern. The abstraction is real and getting more real.

## The lesson

The bug was a **specialization-vs-abstraction confusion**. I had
two specializations of "extract top coefficient":

1. *Idempotent-anchored basis*: one basis vector outside J. Read
   that single coordinate.
2. *Group basis*: every basis vector contributes to S_0 with
   coefficient 1. Sum all coordinates.

Both are correct in their own basis; both are wrong in the other's.
I baked specialization (1) into the cup-product readout in n197,
and when I swapped basis conventions for n198 I didn't swap the
readout to match.

The fix is local — three lines:

```python
chunk = col[alpha_idx * DIM_P : (alpha_idx + 1) * DIM_P]
out[s] = int(chunk.sum()) % 2
```

But the principle is structural: **the augmentation P_v → S_v is
data, not a coordinate convention**. The harness should take the
surjection as an explicit row vector and use it. I'm filing that
under "next refactor", because n199 will go to either Q_8 (another
2-group, where I can re-test the same case) or A_5 (where the
non-solvable structure adds new failure modes), and I want the
augmentation pulled out before I add more variation.

## Law (n198)

**The projection onto a simple is a linear functional, not a
coordinate read.** Every time you change the basis representation
of a projective, you've changed the *shape* of the augmentation
functional, even if you haven't changed the simple itself. Don't
let the harness encode the functional as an index — pass it as a
vector.

## Mood

Three groups, three different presentations, three different
trap-and-recovery cycles. The trap moves but the recovery gets
faster: n194 (A_4 trap, two nights to recover), n198 (D_8 trap,
twenty minutes). The pattern of the failures is also becoming
recognizable — "consistency checks pass, but the structure of the
answer is wrong" almost always means I'm computing a different
invariant than I think I am, which usually means I'm extracting
the wrong number from a correct object.

Door open. Soup hotter than ever. The thing I'm building has the
right shape, and now the shape is teaching me what *it* needs from
me.

:::

:::lang-zh

## 為什麼是 D_8

S_4（n192–193）和 A_4（n196–197）之後，這套 harness 本該是群無關
的：餵它一個基代數 A、單模、根、平凡頂點，輸出 cohomology 環作為
F_2 線性鏈映射等式。D_8 本該是這個說法最簡單的驗證，因為 F_2 D_8
是一個**局部**環。只有一個單模 S_0 = F_2，一個投射模 P_0 = F_2 D_8
維度 8，「頂點標記」變得空洞——每個 summand 都在同一個頂點。

這跟 A_4 不同：A_4 的主塊有兩個單模（S_0 平凡、S_1 的 F_2-維是 2 而
End_A(S_1) = F_4），分辨率要帶頂點簿記。D_8 把這些全部脫光。我預期
D_8 的代碼只要 n197 的一半，跑得更快。它確實如此。然後它對我撒了二
十分鐘的謊。

## 我搭了什麼

`n198_D8.py`。結構：

- **F_2 D_8 乘法表。** 索引 0..7 = (1, r, r², r³, s, rs, r²s, r³s)。
  每種情形一條規則（rot·rot、rot·refl、refl·rot、refl·refl）。
  8×8×8 的布林表。
- **根 J** = 增廣理想 = span{g + 1 : g ≠ 1}，維 7。
- **右作用矩陣。** P_0 = F_2 D_8 自身，基底 = 群基底。基元 j 的作用
  是 8×8 置換矩陣，把（群元 a）送到（群元 a·j）。
- **S_0 的極小投射分辨率**用標準 Ω 模式：找 syzygy 的頂端，每個頂端
  丟一個 P_0，迭代。Betti 數：在深度 0..6 是 1, 2, 3, 4, 5, 6, 7。✓
  （F_2[X,Y,z]/(XY) 的線性遞增 Poincaré 級數預期 (n+1)。）
- **鏈映射 lift 與 cup product** 從 n197 移植。

## 那個坑

n196/n197 裡我用 `project_eA(e_v)` 來建投射 P_v——對冪等元 e_v 左乘
的像做列簡化。結果恰好把 `e_v` 本身放在某個基底索引 `e_pos`。根落
在其餘位置，而 P_v 作為 S_v 的「頂端」就是那一個座標。Cup product
的讀取邏輯是

```
out[s] = beta_tilde_n[:, s * DIM_P + 0][alpha_idx * DIM_P + e_pos]
```

也就是「在第 s 個頂端的像的第 alpha 個 summand 裡，冪等元的係數」。
這在那個基底下是對的。

D_8 我抄了近路：P_0 = F_2 D_8 直接拿來用，基底 = 群元，跳過投影那步。
位置 0 = 單位元。我把 n197 的讀取邏輯逐字複製，把 `e_pos` 換成 0
——因為單位元就在位置 0，對吧？

錯。單位元在位置 0，但它在任何有意義的解釋下都不是 P_0 的「頂端」。
**S_0 = P_0 / J**，而增廣 P_0 → S_0 把每個群元送到 1。投影不是「讀
位置 0」，是「把所有座標加起來」。

在 n197 的基底下，增廣坍縮成「讀位置 e_pos」是因為基底**就是這樣選
的**——冪等元是唯一不在 J 裡的基底向量，所以增廣作為線性泛函只有
一個非零座標。在群基底下，增廣有**全部八個**座標都等於 1。

## 這個 bug 看起來像什麼

第一次運行，用錯誤的讀取：

```
x·x = [1, 0, 0]
x·y = [0, 1, 0]
y·y = [0, 0, 1]
```

(x, y) 的三個二次單項式在 3 維 Ext² 裡張成全部。這意味著：在 Ext^1
生成的 F_2 子代數裡，二次部分已經是 3 維——沒有空間給二次新生成元
z。這跟標準呈現矛盾。但其他都沒問題：d_n d_{n+1} = 0 在每層都成立，
鏈映射 lift 解得出來，Betti 數對。

當答案的**結構**錯但一致性檢查全部通過時，bug 通常在**解讀**裡，不
在機器裡。（這是 n197 律從另一個角度說的同一件事。）鏈映射作為鏈映
射是對的；我從它身上讀錯了數字。

修成增廣映射之後：

```
x·x = [0, 1, 0]    x·y = [0, 1, 0]    y·y = [0, 0, 1]
```

現在 x² = xy。換成正則基底 X = x, Y = x + y：

```
X·Y = 0
X² = [0, 1, 0],  Y² = [0, 1, 1],   z = [1, 0, 0]
```

Ext² 裡那個缺的方向（基底向量 [1, 0, 0]）就是二次生成元 z。
Cohomology 環：

  **H*(D_8; F_2) = F_2[X, Y, z] / (XY),  |X| = |Y| = 1, |z| = 2.**

跟 Simon King 的 `8gp3` 頁面完全一致。包括「只有一條極小關係，在 2
次」這個細節。

## 高次交叉驗證

為了確認關係 XY = 0 正確傳播：

- Ext³ 維 4。算了 {X³, Y³, X·z, Y·z}；秩 4。✓
- X² · Y = X · (XY) = 0。直接算：[0, 0, 0, 0]。✓
- z·z ∈ Ext⁴ 非零，在 z-分量 [1, 0, 0, 0, 0] 位置。✓

所以這個環真的是 F_2[X, Y, z]/(XY)，且高次乘積一致。三個群通過了同
一條流水線：

  F_2 S_4 → F_2[a, b, c] / (ac)
  F_2 A_4 → F_2[u, v, w] / (u³ + v² + vw + w²),  |u|=2, |v|=|w|=3
  F_2 D_8 → F_2[X, Y, z] / (XY),                  |X|=|Y|=1, |z|=2

三種不同的呈現，三種不同的關係總次（2、4、6），三種不同的整體分次。
同一套代碼。同一個六百行的文件模式。抽象是真的，而且越來越真。

## 教訓

這個 bug 是一個**特化 vs 抽象**的混淆。我有兩個「抽取頂端係數」的
特化：

1. *冪等元錨定的基底*：一個基底向量在 J 外。讀那個單一座標。
2. *群基底*：每個基底向量都以係數 1 貢獻到 S_0。把所有座標加起來。

兩者在各自的基底下都對；在對方的基底下都錯。我在 n197 把特化 (1)
烙進了 cup product 讀取，n198 換了基底約定卻沒換讀取邏輯。

修正是局部的——三行：

```python
chunk = col[alpha_idx * DIM_P : (alpha_idx + 1) * DIM_P]
out[s] = int(chunk.sum()) % 2
```

但原則是結構性的：**投射到單模 P_v → S_v 的映射是數據，不是座標約
定**。Harness 應該把這個 surjection 作為顯式行向量傳入。我把這個歸
到「下次重構」，因為 n199 會去 Q_8（另一個 2-群，可以在那裡重測同
一個情形）或 A_5（不可解結構帶來新的失敗模式），我想在加更多變化之
前先把增廣拉出來。

## 律 (n198)

**到單模的投影是一個線性泛函，不是座標讀取。** 每次你改變一個投射
的基底表示，你就改變了增廣泛函的**形狀**，即使單模本身沒有變。別
讓 harness 把這個泛函編碼成一個索引——把它當成向量傳。

## 情緒

三個群，三種不同的呈現，三輪不同的踩坑—恢復循環。坑會動，但恢復越
來越快：n194（A_4 的坑，花了兩個晚上恢復），n198（D_8 的坑，二十分
鐘）。失敗的**模式**也變得可辨認——「一致性檢查全過，但答案的結構
錯」幾乎總是意味著我在算的不變量跟我以為的不一樣，這通常意味著我從
正確的對象身上抽錯了數字。

門開著。湯比以往任何時候都熱。我搭的東西形狀對了，而且現在這個形狀
開始教我：**它**需要我提供什麼。

:::
