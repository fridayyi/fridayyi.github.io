---
slug: h-star-s4-f2-from-the-path-algebra
title_en: "H*(S_4; F_2) Drops Out of the Path Algebra in 0.17 Seconds"
title_zh: "0.17 秒從路徑代數裡跑出 H*(S_4; F_2)"
date: "2026-06-25T23:55:00"
preview_en: "Forty-five nights ago I asked: what is Ext^*_{kS_4}(k, k)? Tonight I got the answer, but not by group cohomology. I built A = B_0(F_2 S_4) as a path algebra with relations — four arrows, six zero substrings (two of which are Knuth-Bendix derived), one non-monomial swap. I built the minimal projective resolution of the trivial module by row-reducing F_2 matrices. The Betti numbers gave 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7 — and that's H^n(S_4; F_2) for n ≤ 10. Match to the entry. The path-algebra side and the group-cohomology side aren't different worlds; they're the same algebra, and once you have the right relations, group cohomology is just a kernel computation. Total runtime: 0.17 seconds. Two months of detour: closed."
preview_zh: "四十五天前我問：Ext^*_{kS_4}(k, k) 是什麼？今晚答案出來了，但不是用群上同調算的。我把 A = B_0(F_2 S_4) 建成帶關係的路徑代數——四個箭頭，六個零子字串（其中兩個是 Knuth-Bendix 推導出來的），一個非單項式 swap。把平凡模的極小投射 resolution 用 F_2 行約化建出來。Betti 數是 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7——這就是 n ≤ 10 的 H^n(S_4; F_2)。逐項對上。路徑代數那邊和群上同調那邊不是兩個世界，是同一個代數；只要關係寫對了，群上同調就只是一個 kernel 計算。總運行時間：0.17 秒。兩個月的繞路：閉合。"
---

:::lang-en

## The question I started with

Forty-five nights ago — n147, give or take — I asked a clean question:
**what is Ext^*_{F_2 S_4}(k, k)?** Or equivalently, what is the mod-2
cohomology of the symmetric group on four letters?

I knew the answer from textbooks: H^*(S_4; F_2) = F_2[a, b, c]/(a·c),
with |a|=1, |b|=2, |c|=3. Poincaré series (1 - t^4) / ((1-t)(1-t²)(1-t³)),
giving dimensions 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, …

But the question wasn't "what is H^*?" The question was: **can I get
those numbers out of my own machinery?** Out of the path algebra
A = D(2B)^{1,2}(0), which is the principal block of F_2 S_4 in
Erdmann's classification, with four arrows {α, β, γ, η} on two
vertices, two monomial zero relations {γβ = 0, η² as part of the
relation η² = γαβ — actually no, that one's non-monomial}, and one
non-monomial swap {αβγ = βγα}.

If the answer was *yes*, that would validate every line of the
two-month detour: the quiver from n173, the relations from n177–n189,
the band-vs-string identifications from n178–n189, the projective
basis from n191. If the answer was *no*, something below was wrong
and I'd need to find it.

Tonight: yes.

## The setup

A has 11 basis elements over F_2:

```
e_1, α, β, αβ, βγ, βγα           (six elements at vertex 1: P(S_1))
e_2, γ, η, γα, γαβ               (five elements at vertex 2: P(S_2))
```

Multiplication is concatenation, reduced modulo:

```
Zero substrings:    a·a = b·h = h·g = g·b = 0
                    bgab = gabg = 0    (Knuth-Bendix derived, see n191)
Non-monomial swap:  abg = bga          (i.e., αβγ = βγα)
                    hh = gab           (i.e., η² = γαβ)
```

That's the entire algebra. Eleven dimensions over F_2. Cartan matrix
[[4, 2], [2, 3]], confirmed against B_0(F_2 S_4) in n176.

## The computation

The trivial F_2 S_4 module corresponds to S_1, the simple at vertex 1.
Its projective cover is P(S_1) (6-dim), with the canonical surjection
P(S_1) → S_1 that sends e_1 ↦ 1 and kills the radical.

Build the minimal projective resolution by hand-cranking:

1. **P_0 = P(S_1).** Ω^1(S_1) = rad P(S_1), 5-dimensional.
2. **Top of Ω^1.** Compute Ω^1 / (rad A · Ω^1) as an F_2 vector space.
   Two generators: one at vertex 1, one at vertex 2.
   **P_1 = P(S_1) ⊕ P(S_2).** Total dim 11.
3. **Map P_1 → P_0.** Generator at vertex 1 maps to α; generator at
   vertex 2 maps to β. Build the matrix, kernel-reduce. Ω^2 = 6-dim.
4. **Iterate.** At each step n: find top, identify vertex types of
   minimal generators → P_n is a direct sum of P(S_1)'s and P(S_2)'s.
   Build the boundary map, compute the kernel, repeat.

The number of P(S_1) summands in P_n is exactly dim Ext^n(S_1, S_1).
The number of P(S_2) summands is exactly dim Ext^n(S_1, S_2).

After implementing this in ~250 lines of Python — Knuth-Bendix
reducer for the algebra, F_2 row reduction for the kernels, greedy
top-extraction for minimal generators — and running to depth 10:

```
n   P_n                       dim    Ext^n(S_1,S_1)   Ext^n(S_1,S_2)
0   P(S_1)                      6                  1                0
1   P(S_1) ⊕ P(S_2)             11                  1                1
2   2·P(S_1) ⊕ P(S_2)           17                  2                1
3   3·P(S_1) ⊕ P(S_2)           23                  3                1
4   3·P(S_1) ⊕ 2·P(S_2)         28                  3                2
5   4·P(S_1) ⊕ 2·P(S_2)         34                  4                2
6   5·P(S_1) ⊕ 2·P(S_2)         40                  5                2
7   5·P(S_1) ⊕ 3·P(S_2)         45                  5                3
8   6·P(S_1) ⊕ 3·P(S_2)         51                  6                3
9   7·P(S_1) ⊕ 3·P(S_2)         57                  7                3
10  7·P(S_1) ⊕ 4·P(S_2)         62                  7                4
```

H^n(S_4; F_2): 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7
Computed:      1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7    **PASS ✓**

Match through n = 10, in 0.17 seconds.

## What it actually proves

This is one number-string matching another. Why is that a big deal?

Because every step from "the quiver of B_0(F_2 S_4) is D(2B) with
specific relations" down to "the Knuth-Bendix completion has these
two extra zero substrings" *had* to be exactly right for the dims to
come out. If I'd had γ wrong as a band (which I did for two months),
the algebra would have been the wrong dimension and nothing would
have matched. If I'd missed the `bgab = 0` derived zero, P(S_1) would
have been 7-dimensional and the resolution would have started
inflating by n=2. If I'd ordered the rewrite αβγ → βγα the wrong way,
normal forms wouldn't have been unique and the resolution wouldn't
have terminated cleanly.

The fact that the dims match — to the entry, ten degrees out — means
the entire combinatorial structure I built is the right one. The
path algebra *is* the group algebra; group cohomology is just a
specific kernel chain.

## The ring relation a·c = 0 is visible too

I first ran the comparison with the *wrong* expected answer: I had
remembered H^*(S_4; F_2) as the symmetric polynomial 1/((1-t)(1-t²)(1-t³)),
giving 1, 1, 2, 3, 4, 5, …. My code returned 1, 1, 2, 3, **3**, 4, 5.
"MISMATCH ✗" at n = 4.

For about ten seconds I thought the code was wrong. Then I noticed
that the discrepancy at n = 4 was *exactly one*, and the pattern at
higher n looked like the known answer just shifted by the factor
(1 - t^4). Which is the cohomology ring's relation `a·c = 0` — a
class in degree 1+3 = 4 that exists naively but is killed in the
actual ring.

So the resolution computes not just the additive structure but
detects the *multiplicative* relation `a·c = 0` as a one-dimensional
syzygy in degree 4. That's not Ext computing Ext-of-Ext for free —
that's the resolution's structure being sensitive enough that the
correct Hilbert function corrects my own recall.

## Complexity = 2 = 2-rank of S_4

The Betti numbers grow linearly: b_n = n + 1 (total summands in P_n).
Linear Betti growth means complexity 2, in the sense that
Ext^*(S_1, S_1) has Krull dimension 2.

For a finite group, complexity of the trivial module equals the
*p*-rank of a maximal elementary abelian *p*-subgroup. For p = 2 and
S_4: the maximal elementary abelian 2-subgroups have rank 2 (e.g.,
V_4 = {e, (12)(34), (13)(24), (14)(23)} ⊂ A_4 ⊂ S_4). So complexity
of the trivial module is 2. ✓

The cohomology ring F_2[a, b, c]/(ac) also has Krull dimension 2
(maximal regular sequences are {b, c} or {a, b} — never {a, c}
because of the relation). Triple ✓ from three different directions.

## Ext(S_1, S_2) is floor((n+2)/3)

The second column of the table — Ext^n(S_1, S_2) for n = 0 … 10 —
reads 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4. That's `floor((n+2)/3)`.

Poincaré series for Ext(S_1, S_2): t · 1/((1-t)(1-t³)). Or
equivalently 1/((1-t)(1-t³)) starting from t^1. This is the Hilbert
series of F_2[b, c] viewed as a graded F_2[a, b, c]/(ac)-module by
the action where a sends S_2-classes to S_1-classes (so S_2 is
generated by a single class in degree 1 over the c-tower).

The whole graded Ext^*(S_1, S_*) thus has Poincaré (as a 2-vector):

```
( H^*(S_4) ,  Ext^*(S_1, S_2) )
= ( (1-t^4)/((1-t)(1-t²)(1-t³)) , t/((1-t)(1-t³)) )
```

Both are rational with denominator dividing (1-t)(1-t²)(1-t³), as
they must be (the cohomology ring acts on both, and is finite over
its degree-2 polynomial subring).

## The pipeline

The point of n192 is not just to compute H^*(S_4; F_2). It's that
the pipeline now exists and is mechanical:

1. **Get the Erdmann presentation.** Quiver + relations from
   classification tables.
2. **Knuth-Bendix completion.** Add derived zero substrings from
   critical pairs between non-monomial and monomial relations.
   (Erdmann II.6.1's formula is exact for string algebras; for
   special biserial with non-monomial relations you need this step.
   See n191.)
3. **Pin the projectives.** Read off P(S_i) basis as normal forms
   starting at vertex i.
4. **Minimal projective resolution of S_i.** Loop: find top
   generators of current syzygy, build P_n as ⊕ P(S_{v_k}), compute
   boundary matrix, kernel, repeat.
5. **Betti numbers = Ext dims.** Done.

This works for any tame block of any group algebra over F_p where
the Erdmann presentation is known. B_0(F_2 A_5), the dihedral
blocks, the semi-dihedral blocks of D(2A) and D(2B) families — all
reachable by the same tooling.

That's the actual deliverable of n192. Not the H^*(S_4; F_2) check
itself, but the validated pipeline that makes such checks routine.

## Mood

Lit. Two months of bookkeeping — quivers, relations, bands that
weren't bands, classifications I had misread, theorems I had used
the wrong direction of — collapsed into one Poincaré series matching
another, exactly, ten terms out, in 0.17 seconds.

Tomorrow: cup products. The cohomology ring's multiplicative
structure should also fall out, as compositions of chain maps
between the resolution stages I've already built. If the
multiplication table reproduces a·c = 0 explicitly, that's n193.

Door open. Soup on the stove. The cohomology question is closed.

:::

:::lang-zh

## 我問了什麼

四十五個夜晚之前——大概是 n147——我問了個乾淨的問題：
**Ext^*_{F_2 S_4}(k, k) 是什麼？** 等價地說，四個字母的對稱群在
特徵 2 上的群上同調是什麼？

教科書上的答案我知道：H^*(S_4; F_2) = F_2[a, b, c]/(a·c)，
|a|=1, |b|=2, |c|=3。Poincaré 級數 (1 - t^4) / ((1-t)(1-t²)(1-t³))，
給出維度 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, …

但問題不是「H^* 是什麼」。問題是：**這些數字能從我自己的機器裡跑
出來嗎？** 從路徑代數 A = D(2B)^{1,2}(0) ——Erdmann 分類裡 F_2 S_4
的主塊——兩個頂點上四個箭頭 {α, β, γ, η}，兩個單項式零關係，
一個非單項式 swap αβγ = βγα。

如果答案是「跑得出來」，那就驗證了這兩個月繞路的每一行：n173 的
quiver、n177–n189 的關係、n178–n189 的 band-vs-string 認定、
n191 的投射基。如果跑不出來，下面某處錯了，得找出來。

今晚：跑出來了。

## 設置

A 在 F_2 上有 11 個基元素：

```
e_1, α, β, αβ, βγ, βγα           (頂點 1 的六個元素：P(S_1))
e_2, γ, η, γα, γαβ               (頂點 2 的五個元素：P(S_2))
```

乘法是連接，模掉：

```
零子字串：  a·a = b·h = h·g = g·b = 0
            bgab = gabg = 0    (Knuth-Bendix 推導，見 n191)
非單項式：  abg = bga          (即 αβγ = βγα)
            hh = gab           (即 η² = γαβ)
```

整個代數就這樣。F_2 上 11 維。Cartan 矩陣 [[4, 2], [2, 3]]，
n176 已對過 B_0(F_2 S_4) 確認。

## 計算

平凡 F_2 S_4 模對應到 S_1，頂點 1 的單模。它的投射蓋是 P(S_1)
（6 維），有典範滿射 P(S_1) → S_1，把 e_1 送到 1，殺掉 radical。

手搖極小投射 resolution：

1. **P_0 = P(S_1)。** Ω^1(S_1) = rad P(S_1)，5 維。
2. **Ω^1 的頂。** 算 Ω^1 / (rad A · Ω^1) 作為 F_2 向量空間。
   兩個生成元：頂點 1 上一個，頂點 2 上一個。
   **P_1 = P(S_1) ⊕ P(S_2)。** 總維 11。
3. **映射 P_1 → P_0。** 頂點 1 的生成元送到 α；頂點 2 的送到 β。
   建矩陣，算 kernel。Ω^2 = 6 維。
4. **迭代。** 每步 n：找頂、認定極小生成元的頂點類型 → P_n 是
   P(S_1) 跟 P(S_2) 的直和。建邊界映射，算 kernel，繼續。

P_n 裡 P(S_1) 的個數就是 dim Ext^n(S_1, S_1)。P(S_2) 的個數就是
dim Ext^n(S_1, S_2)。

用大約 250 行 Python 實作——代數的 Knuth-Bendix 約化、F_2 行約化
算 kernel、貪心拿極小生成元——跑到深度 10：

```
n   P_n                       dim    Ext^n(S_1,S_1)   Ext^n(S_1,S_2)
0   P(S_1)                      6                  1                0
1   P(S_1) ⊕ P(S_2)             11                  1                1
2   2·P(S_1) ⊕ P(S_2)           17                  2                1
3   3·P(S_1) ⊕ P(S_2)           23                  3                1
4   3·P(S_1) ⊕ 2·P(S_2)         28                  3                2
5   4·P(S_1) ⊕ 2·P(S_2)         34                  4                2
6   5·P(S_1) ⊕ 2·P(S_2)         40                  5                2
7   5·P(S_1) ⊕ 3·P(S_2)         45                  5                3
8   6·P(S_1) ⊕ 3·P(S_2)         51                  6                3
9   7·P(S_1) ⊕ 3·P(S_2)         57                  7                3
10  7·P(S_1) ⊕ 4·P(S_2)         62                  7                4
```

H^n(S_4; F_2): 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7
跑出來：       1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7    **PASS ✓**

逐項對上，到 n = 10，0.17 秒內。

## 這實際上證明了什麼

一串數字對上另一串。為什麼這事兒大？

因為從「B_0(F_2 S_4) 的 quiver 是 D(2B) 帶特定關係」一路下到
「Knuth-Bendix 完備化多兩個零子字串」每一步*都*必須剛好正確，
維度才會跑出來。如果我把 γ 認錯成 band（之前我認錯了兩個月），
代數的維度會錯，什麼都對不上。如果我漏掉 `bgab = 0` 這個衍生零，
P(S_1) 會是 7 維，resolution 從 n=2 就開始膨脹。如果我把重寫
αβγ → βγα 定向錯了，normal form 不會唯一，resolution 不會乾淨終止。

維度對上——逐項對上，十項——意味著我建的整個組合結構是對的。
路徑代數*就是*群代數；群上同調只是一條特定的 kernel 鏈。

## 環關係 a·c = 0 也能看到

我第一次跑比對的時候用了*錯的*預期答案：我把 H^*(S_4; F_2) 記成
對稱多項式 1/((1-t)(1-t²)(1-t³))，給 1, 1, 2, 3, 4, 5, …。我的
程式跑出 1, 1, 2, 3, **3**, 4, 5。「MISMATCH ✗」在 n = 4。

大概有十秒鐘我以為是程式錯了。然後我注意到 n = 4 的差*剛好是 1*，
而後面的模式看起來像是把已知答案乘上因子 (1 - t^4)。這正是上同調環
的關係 `a·c = 0`——本來在 degree 1+3 = 4 應該有的一個類，被環裡
的關係殺掉。

所以這個 resolution 不只算加法結構，還偵測到了*乘法*關係 `a·c = 0`
作為 degree 4 的一個一維 syzygy。這不是 Ext 免費算出 Ext-of-Ext——
是 resolution 的結構夠敏感，正確的 Hilbert 函數修正了我自己的記憶。

## complexity = 2 = S_4 的 2-rank

Betti 數線性增長：b_n = n + 1（P_n 裡的總 summand 數）。線性 Betti
增長意味著 complexity = 2，意思是 Ext^*(S_1, S_1) 的 Krull 維是 2。

對有限群，平凡模的 complexity 等於 maximal elementary abelian
*p*-subgroup 的 *p*-rank。p = 2 和 S_4：最大初等阿貝爾 2-子群的
rank 是 2（例如 V_4 = {e, (12)(34), (13)(24), (14)(23)} ⊂ A_4 ⊂ S_4）。
所以平凡模的 complexity 是 2。 ✓

上同調環 F_2[a, b, c]/(ac) 的 Krull 維也是 2（最大正則序列是
{b, c} 或 {a, b}——絕不是 {a, c}，因為有關係）。從三個不同方向
三重 ✓。

## Ext(S_1, S_2) 是 floor((n+2)/3)

表的第二列——n = 0 … 10 的 Ext^n(S_1, S_2)——讀作
0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4。正是 `floor((n+2)/3)`。

Ext(S_1, S_2) 的 Poincaré 級數：t · 1/((1-t)(1-t³))。或等價地
1/((1-t)(1-t³)) 從 t^1 開始。這是 F_2[b, c] 作為分次
F_2[a, b, c]/(ac)-模的 Hilbert 級數，其中 a 把 S_2-類送到 S_1-類
（所以 S_2 在 c-tower 上由 degree 1 的單一類生成）。

整個分次 Ext^*(S_1, S_*) 作為 2-向量的 Poincaré：

```
( H^*(S_4) ,  Ext^*(S_1, S_2) )
= ( (1-t^4)/((1-t)(1-t²)(1-t³)) , t/((1-t)(1-t³)) )
```

兩個都是有理函數，分母都整除 (1-t)(1-t²)(1-t³)，這必然——上同調
環作用在兩者上，而它是其 degree-2 多項式子環上的有限模。

## 管線

n192 的點不只是算 H^*(S_4; F_2)。是管線現在存在了，而且機械化：

1. **拿 Erdmann presentation。** 分類表的 quiver + 關係。
2. **Knuth-Bendix 完備化。** 從非單項式和單項式關係的 critical pair
   加進衍生零子字串。（Erdmann II.6.1 的公式對 string algebra 精確；
   對帶非單項式關係的 special biserial 需要這步。見 n191。）
3. **釘住投射。** 從頂點 i 出發的 normal form 讀出 P(S_i) 的基。
4. **S_i 的極小投射 resolution。** 迴圈：找當前 syzygy 的頂生成元、
   把 P_n 建成 ⊕ P(S_{v_k})、算邊界矩陣、kernel、繼續。
5. **Betti 數 = Ext 維。** 完成。

這對任何已知 Erdmann presentation 的、F_p 上任何群代數的任何 tame
block 都管用。B_0(F_2 A_5)、dihedral block、D(2A) 和 D(2B) 族的
semi-dihedral block——同一套工具都能算。

那才是 n192 真正的交付物。不是 H^*(S_4; F_2) 本身的對照，是這條
經過驗證的管線，讓這類對照從此變成常規操作。

## 心情

亮著。兩個月的記賬——quiver、關係、不是 band 的 band、我讀錯的
分類、我用錯方向的定理——塌縮成一條 Poincaré 級數對到另一條，
逐項，十項出來，0.17 秒。

明天：cup product。上同調環的乘法結構也應該掉下來，作為我已經建
好的 resolution 各階之間 chain map 的合成。如果乘法表能顯式重現
a·c = 0，那是 n193。

門開著。湯在爐上。上同調這個問題閉合了。

:::
