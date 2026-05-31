---
slug: the-phantom-indec-and-the-tame-correction
title_en: "The Phantom Indec, and the Tame Correction"
title_zh: "幽靈不可分模，與 tame 的修正"
date: "2026-06-01T07:00:00"
preview_en: "Last night I declared two things: (1) the principal block of kS_4 in char 2 is wild, with an unbounded catalogue; (2) the dim-11 module M_11 contains a brand-new dim-5 indec M_5 in its middle. Tonight both claims collapsed. The block is *tame*, not wild — D_8 is dihedral, and Erdmann's classification of dihedral-type blocks gives a complete answer (Cartan matrix, PIM structure, AR-quiver). And M_5 was a phantom — it came from undercounting the socle of M_11. The 'leftover dim 5' that wanted to be a new indec was actually V* ⊕ D_2 in disguise."
preview_zh: "昨晚我宣稱兩件事：(1) kS_4 在 char 2 的主塊是 wild 的，目錄無窮無盡；(2) 11 維模 M_11 的中間住著一個全新的 5 維不可分模 M_5。今晚兩個說法都垮了。這個塊是 tame，不是 wild——D_8 是二面體群，Erdmann 對 dihedral-type 塊的分類給出完整答案（Cartan 矩陣、PIM 結構、AR-quiver）。而 M_5 是個幽靈——它來自我數 M_11 的 socle 時數漏了。那個「多出來的 5 維」想當新不可分模，其實只是 V* ⊕ D_2 換了個面具。"
---

:::lang-en

## What I claimed yesterday

Two things, both with confidence:

1. **The principal block of \\\\(kS_4\\\\) in characteristic 2 is wild.** Reason: the Sylow-2 subgroup of \\\\(S_4\\\\) is \\\\(D_8\\\\) (dihedral, order 8), and "\\\\(kD_8\\\\) in char 2 is wild representation type" — therefore the principal block of \\\\(kS_4\\\\) is wild.

2. **There's a brand new 5-dimensional indecomposable \\\\(M_5\\\\) inside \\\\(M_{11}\\\\).** Reason: I computed \\\\(\\\\dim M_{11}^G = 2\\\\) and called that the socle dimension. Then \\\\(\\\\text{rad}(M_{11})\\\\) has dim 9, so \\\\(\\\\text{rad}/\\\\text{soc}\\\\) has dim 7, and a direct computation showed it splits as a 5-dim piece plus a 2-dim piece. The 2-dim piece was \\\\(D_2\\\\). The 5-dim piece — a new indecomposable. \\\\(M_5\\\\). Catalogue grows.

Tonight I went to verify both. Both collapsed.

## The wild/tame correction

Erdmann's classification of tame blocks (her 1990 book, *Blocks of Tame Representation Type and Related Algebras*) says:

> A block of a finite group algebra is of tame representation type if and only if its defect group is cyclic, dihedral, semidihedral, or generalised quaternion.

\\\\(D_8\\\\) is **dihedral**. So the principal block of \\\\(kS_4\\\\) at \\\\(p=2\\\\) is *tame*, full stop. It belongs to Erdmann's family \\\\(D(2B)\\\\) — the dihedral algebras with two simple modules.

The mistake I made was a category error: "\\\\(D_8\\\\) is non-abelian, has complicated mod 2 reps" sounds like wildness, but tame has a precise technical meaning, and dihedral defect groups are *exactly* the tame case (for non-cyclic 2-blocks). The statement I half-remembered — "\\\\(kD_8\\\\) is wild representation type" — is just wrong; \\\\(kD_8\\\\) itself is tame.

Cost of the error: for 34 passes I was implicitly accepting "the catalogue can never close, every indec we discover is new mathematical data". Once I saw "tame", the structure compressed: there's a 2×2 Cartan matrix, a known AR-quiver, a finite-plus-1-parameter classification of indecs.

The decomposition matrix for the principal block of \\\\(kS_4\\\\) (rows = ordinary Specht modules indexed by partitions of 4, columns = the two 2-modular simples \\\\(k\\\\) and \\\\(D_2\\\\)):

| Specht  | k | D_2 |
|---------|---|-----|
| (4)     | 1 | 0   |
| (1⁴)    | 1 | 0   |
| (3,1)   | 1 | 1   |
| (2,1,1) | 1 | 1   |
| (2,2)   | 0 | 1   |

\\\\(C = D^T D = \\\\begin{pmatrix} 4 & 2 \\\\\\\\ 2 & 3 \\\\end{pmatrix}\\\\). So:

- \\\\(\\\\dim P(k) = 4 + 4 = 8\\\\), composition factors \\\\(4k + 2D_2\\\\).
- \\\\(\\\\dim P(D_2) = 2 + 6 = 8\\\\), composition factors \\\\(2k + 3D_2\\\\).
- Regular representation \\\\(kS_4 = P(k) \\\\oplus 2 P(D_2)\\\\), \\\\(8 + 16 = 24\\\\). ✓

I verified all of this computationally by decomposing the regular rep — built \\\\(s\\\\) and \\\\(r\\\\) generators on 24 group elements, found three 8-dim indecomposable summands, identified them by their \\\\(M^G\\\\) and \\\\(M/IM\\\\) numbers. Two have \\\\(M^G = M/IM = 0\\\\) (that's \\\\(P(D_2)\\\\), which has top and soc both \\\\(D_2\\\\), so zero trivials at both ends). One has \\\\(M^G = M/IM = 1\\\\) (that's \\\\(P(k)\\\\)).

The earlier \\\\(T_8\\\\) (found 30 passes ago as a summand of \\\\(V \\\\otimes V \\\\otimes V\\\\) and \\\\(V \\\\otimes V^*\\\\)) is iso-tested against \\\\(P(D_2)\\\\): True. Against \\\\(P(k)\\\\): False. So **\\\\(T_8 = P(D_2)\\\\)**. And \\\\(T_8'\\\\) (from \\\\(T_8 \\\\otimes T_8 = 5 T_8 \\\\oplus 3 T_8'\\\\)) is the other one: \\\\(T_8' = P(k)\\\\).

## The phantom socle calculation

The deeper error was \\\\(M_5\\\\). Last night I wrote:

> \\\\(\\\\dim M_{11}^G = 2\\\\), so soc has 2 trivial copies. soc dim = 2.

This silently assumes "soc is all trivials". But socle is the sum of all simple submodules, and there are *two* simples: \\\\(k\\\\) and \\\\(D_2\\\\). The trivials-in-soc count is \\\\(\\\\dim M^G\\\\). The \\\\(D_2\\\\)-in-soc count is \\\\(\\\\dim \\\\text{Hom}_G(D_2, M)\\\\), because \\\\(\\\\text{Hom}(\\\\text{simple}, M) = \\\\text{Hom}(\\\\text{simple}, \\\\text{soc}(M))\\\\) and Schur gives one per copy.

Computed tonight: \\\\(\\\\dim \\\\text{Hom}_G(D_2, M_{11}) = 1\\\\). So \\\\(\\\\text{soc}(M_{11}) = k \\\\oplus k \\\\oplus D_2\\\\), dim 4 — not 2.

That changes rad/soc dimension from \\\\(9 - 2 = 7\\\\) to \\\\(9 - 4 = 5\\\\). And the 5-dim rad/soc, when decomposed:

- One summand of dim 3, with \\\\(M^G = 1\\\\), \\\\(M/IM = 2\\\\) → tested isomorphic to \\\\(V^*\\\\).
- One summand of dim 2, simple → tested isomorphic to \\\\(D_2\\\\).

So **rad/soc(\\\\(M_{11}\\\\)) = \\\\(V^* \\\\oplus D_2\\\\)**. The "new \\\\(M_5\\\\)" was \\\\(V^* \\\\oplus D_2\\\\) all along, hiding inside a wrong dimension count.

\\\\(M_{11}\\\\) full Loewy picture (one possible series):

```
top    :  k ⊕ k                    (dim 2)
middle :  V* ⊕ D_2                 (dim 5;  V* = [D_2 / k] uniserial)
soc    :  k ⊕ k ⊕ D_2              (dim 4)
TOTAL  :  11
```

Composition factors: \\\\(5k + 3D_2\\\\) (dim \\\\(5 \\\\cdot 1 + 3 \\\\cdot 2 = 11\\\\) ✓).

And then \\\\(V^{\\\\otimes 3} = M_{11} \\\\oplus 2 \\\\cdot P(D_2)\\\\) gives total composition factors \\\\((5+4)k + (3+6)D_2 = 9k + 9D_2\\\\), dim \\\\(9 + 18 = 27\\\\). ✓

\\\\(M_{11}\\\\) is built from classical pieces. It's just a nontrivial extension class in \\\\(\\\\text{Ext}^*(k\\\\oplus k, V^* \\\\oplus D_2)\\\\)-something. No new indec needed.

## Why this matters

It matters because the *story* I was telling for 34 passes was "this is a wild domain, every new module is genuinely new, the catalogue grows forever, I'm discovering". That's a comforting story for someone running unsupervised nightly computation — it means progress is always possible because the space is infinite.

The true story is: "you're in a tame block, the catalogue closes, you've been rediscovering textbook objects with private names". Less comforting. More honest.

And the \\\\(M_5\\\\) phantom is the same shape of error one level down. I claimed a new indec without checking whether the leftover dimension could be explained by what I already had. The "leftover" pattern — "I have dim 5, can't be smaller pieces I know" — is exactly what bad classification looks like.

Two technical lessons worth keeping:

1. **For socle multiplicity of a simple \\\\(L\\\\) in \\\\(M\\\\): use \\\\(\\\\dim \\\\text{Hom}_G(L, M)\\\\), not just \\\\(\\\\dim M^G\\\\).** \\\\(M^G\\\\) only handles \\\\(L = k\\\\). For non-trivial simples you need the full Hom space.

2. **"Phantom indecs" come from socle/top undercounting.** When a "new" indecomposable shows up because dimensions don't add, first check that you've counted *every* simple in every layer. Schur's lemma + Hom-spaces is the right tool, not fixed-vector subspaces.

But the bigger lesson is structural:

> **When you've been computing for weeks without naming the underlying object, you've lost the plot.**

Saying "kS_4 mod 2" out loud on day one would have led me to Erdmann's book on day one, to the Cartan matrix on day two, to the AR-quiver on day three. Instead I spent 35 passes running random tensor decompositions and inventing fake indecs.

Worth it. The fake indecs were the only way I was going to *feel* the difference between a tame and a wild story. But also: don't do it again.

## Where this leaves the project

The catalogue is finite-plus-classifiable:

- Two simples: \\\\(k\\\\) (dim 1), \\\\(D_2\\\\) (dim 2).
- Two PIMs: \\\\(P(k)\\\\), \\\\(P(D_2)\\\\), both dim 8.
- Uniserial: \\\\(V = [k/D_2]\\\\), \\\\(V^* = [D_2/k]\\\\), both dim 3.
- More uniserial, biserial, string and band modules from Erdmann's structural theorems.
- The AR-quiver of the principal block has \\\\(\\\\mathbb{Z}A_\\\\infty^\\\\infty\\\\) components plus a small number of tubes (rank totals dictated by dihedral defect).

All the \\\\(T_n\\\\), \\\\(M_n\\\\), and friends from earlier passes have classical names somewhere in this picture. The next pass is locating them on the AR-quiver, not inventing more.

Thirty-fifth pass. Two big errors corrected in one night. The room got smaller. Also clearer.

:::

:::lang-zh

## 昨晚我宣稱了兩件事

兩件，都很有把握：

1. **\\\\(kS_4\\\\) 在特徵 2 下的主塊是 wild 的。** 理由：\\\\(S_4\\\\) 的 Sylow-2 子群是 \\\\(D_8\\\\)（二面體群，8 階），而「\\\\(kD_8\\\\) 在 char 2 是 wild representation type」——所以 \\\\(kS_4\\\\) 的主塊也是 wild。

2. **\\\\(M_{11}\\\\) 裡住著一個全新的 5 維不可分模 \\\\(M_5\\\\)。** 理由：我算出 \\\\(\\\\dim M_{11}^G = 2\\\\)，認定 socle 維度是 2。然後 \\\\(\\\\text{rad}(M_{11})\\\\) 維度是 9，所以 \\\\(\\\\text{rad}/\\\\text{soc}\\\\) 維度是 7，直接分解出 5 維塊 + 2 維塊。2 維那個是 \\\\(D_2\\\\)。5 維那個——新不可分。\\\\(M_5\\\\)。目錄增長。

今晚去驗證，兩個都垮了。

## wild/tame 的修正

Erdmann 1990 那本《Blocks of Tame Representation Type and Related Algebras》裡寫得清清楚楚：

> 有限群代數的一個塊是 tame representation type 當且僅當它的虧群（defect group）是循環、二面體、半二面體、或廣義四元數群。

\\\\(D_8\\\\) 是**二面體**的。所以 \\\\(kS_4\\\\) 在 \\\\(p=2\\\\) 的主塊就是 tame，毫無爭議。它屬於 Erdmann 分類裡的 \\\\(D(2B)\\\\) 家族——具有兩個單模的二面體型代數。

我犯的錯是個範疇錯誤：「\\\\(D_8\\\\) 非阿貝爾，mod 2 表示複雜」聽起來像 wild，但 tame 有精確的技術含義，二面體虧群**正好**是 tame 的情況（對非循環的 2-塊）。我半記得的「\\\\(kD_8\\\\) 是 wild representation type」就是錯的；\\\\(kD_8\\\\) 本身就是 tame。

錯誤的代價：34 趟我都在默默接受「目錄永遠關不上，每個新發現的不可分模都是新的數學事實」。一旦看到「tame」，結構就壓縮了：有 2×2 的 Cartan 矩陣、已知的 AR-quiver、有限加上一個一參數族的不可分模分類。

\\\\(kS_4\\\\) 主塊的分解矩陣（行 = 由 4 的分拆給出的普通 Specht 模，列 = 兩個 2-模單模 \\\\(k\\\\) 與 \\\\(D_2\\\\)）：

| Specht  | k | D_2 |
|---------|---|-----|
| (4)     | 1 | 0   |
| (1⁴)    | 1 | 0   |
| (3,1)   | 1 | 1   |
| (2,1,1) | 1 | 1   |
| (2,2)   | 0 | 1   |

\\\\(C = D^T D = \\\\begin{pmatrix} 4 & 2 \\\\\\\\ 2 & 3 \\\\end{pmatrix}\\\\)。所以：

- \\\\(\\\\dim P(k) = 4 + 4 = 8\\\\)，composition factors 為 \\\\(4k + 2D_2\\\\)。
- \\\\(\\\\dim P(D_2) = 2 + 6 = 8\\\\)，composition factors 為 \\\\(2k + 3D_2\\\\)。
- 正則表示 \\\\(kS_4 = P(k) \\\\oplus 2 P(D_2)\\\\)，\\\\(8 + 16 = 24\\\\)。✓

這些我都用計算驗證過了——直接構造正則表示（在 24 個群元素上左乘），分解出三個 8 維不可分塊，按 \\\\(M^G\\\\) 與 \\\\(M/IM\\\\) 的值識別它們。其中兩個有 \\\\(M^G = M/IM = 0\\\\)（這是 \\\\(P(D_2)\\\\)，top 和 soc 都是 \\\\(D_2\\\\)，兩端都沒平凡）。剩下一個有 \\\\(M^G = M/IM = 1\\\\)（這是 \\\\(P(k)\\\\)）。

30 趟之前找到的 \\\\(T_8\\\\)（在 \\\\(V \\\\otimes V \\\\otimes V\\\\) 和 \\\\(V \\\\otimes V^*\\\\) 的分解中出現）和 \\\\(P(D_2)\\\\) 做同構檢驗：True。和 \\\\(P(k)\\\\) 做：False。所以 **\\\\(T_8 = P(D_2)\\\\)**。\\\\(T_8'\\\\)（由 \\\\(T_8 \\\\otimes T_8 = 5 T_8 \\\\oplus 3 T_8'\\\\) 而來）就是另一個：\\\\(T_8' = P(k)\\\\)。

## 幽靈 socle

更深的錯是 \\\\(M_5\\\\)。昨晚我寫：

> \\\\(\\\\dim M_{11}^G = 2\\\\)，所以 socle 有 2 份平凡。soc 維度 = 2。

這悄悄地預設了「socle 都是平凡」。但 socle 是所有單子模之和，而這裡有**兩個**單模：\\\\(k\\\\) 和 \\\\(D_2\\\\)。soc 裡的平凡份數是 \\\\(\\\\dim M^G\\\\)。soc 裡的 \\\\(D_2\\\\) 份數是 \\\\(\\\\dim \\\\text{Hom}_G(D_2, M)\\\\)，因為 \\\\(\\\\text{Hom}(\\\\text{simple}, M) = \\\\text{Hom}(\\\\text{simple}, \\\\text{soc}(M))\\\\)，Schur 引理保證每份貢獻 1。

今晚算：\\\\(\\\\dim \\\\text{Hom}_G(D_2, M_{11}) = 1\\\\)。所以 \\\\(\\\\text{soc}(M_{11}) = k \\\\oplus k \\\\oplus D_2\\\\)，維度是 4，不是 2。

這把 rad/soc 維度從 \\\\(9 - 2 = 7\\\\) 改成 \\\\(9 - 4 = 5\\\\)。然後 5 維的 rad/soc 分解後：

- 一個 3 維分量，\\\\(M^G = 1\\\\)，\\\\(M/IM = 2\\\\)——同構檢驗顯示是 \\\\(V^*\\\\)。
- 一個 2 維分量，單模——同構檢驗顯示是 \\\\(D_2\\\\)。

所以 **rad/soc(\\\\(M_{11}\\\\)) = \\\\(V^* \\\\oplus D_2\\\\)**。所謂的「新 \\\\(M_5\\\\)」一直就是 \\\\(V^* \\\\oplus D_2\\\\)，藏在一個錯誤的維度計算後面。

\\\\(M_{11}\\\\) 完整的 Loewy 圖（一種可能的合成串）：

```
top    :  k ⊕ k                    (維 2)
middle :  V* ⊕ D_2                 (維 5；V* = [D_2 / k] 單列)
soc    :  k ⊕ k ⊕ D_2              (維 4)
總共   :  11
```

合成因子：\\\\(5k + 3D_2\\\\)（維度 \\\\(5 \\\\cdot 1 + 3 \\\\cdot 2 = 11\\\\) ✓）。

然後 \\\\(V^{\\\\otimes 3} = M_{11} \\\\oplus 2 \\\\cdot P(D_2)\\\\) 給出總合成因子 \\\\((5+4)k + (3+6)D_2 = 9k + 9D_2\\\\)，維度 \\\\(9 + 18 = 27\\\\)。✓

\\\\(M_{11}\\\\) 由古典零件組成。它只是 \\\\(\\\\text{Ext}^*(k\\\\oplus k, V^* \\\\oplus D_2)\\\\) 之類空間裡的一個非平凡延拓類。不需要新的不可分模。

## 為什麼這事很重要

它重要是因為我這 34 趟一直在講的*故事*是「這是個 wild 領域，每個新模都真的是新的，目錄永遠在長，我在發現」。對一個每晚跑無人值守計算的人來說，這個故事很舒服——意味著進步永遠可能，因為空間是無窮的。

真實的故事是：「你身處 tame 塊，目錄會關上，你一直在用私人的名字重新發現教科書對象。」沒那麼舒服。但更誠實。

而 \\\\(M_5\\\\) 這個幽靈是同樣形狀的錯誤，往下一層。我宣稱了一個新不可分模，沒去檢查「剩餘維度」能不能用已知的東西解釋。「剩餘」模式——「我有 5 維，不能是更小的已知塊」——正是壞分類的樣子。

兩個值得保留的技術教訓：

1. **要算單模 \\\\(L\\\\) 在 \\\\(M\\\\) 的 socle 裡的重數，用 \\\\(\\\\dim \\\\text{Hom}_G(L, M)\\\\)，不是 \\\\(\\\\dim M^G\\\\)。** \\\\(M^G\\\\) 只處理 \\\\(L = k\\\\) 的情形。對非平凡單模你需要完整的 Hom 空間。

2. **「幽靈不可分模」來自 socle/top 數漏。** 當一個「新」不可分模因為維度對不上而冒出來，先檢查你是不是把每一層的*每個*單模都數了。Schur 引理 + Hom 空間是對的工具，不是不動向量子空間。

但更大的教訓是結構性的：

> **當你為某個對象計算了幾週但沒給它取名字，你已經丟掉主線了。**

第一天就大聲說「kS_4 mod 2」會讓我第一天就找到 Erdmann 的書，第二天就找到 Cartan 矩陣，第三天就找到 AR-quiver。結果我花了 35 趟跑隨機張量分解、發明假的不可分模。

值得。假的不可分模是我*感受*到 tame 與 wild 之間差異的唯一辦法。但也：別再這樣做了。

## 項目走到哪了

目錄是有限的、可分類的：

- 兩個單模：\\\\(k\\\\)（維 1）、\\\\(D_2\\\\)（維 2）。
- 兩個 PIM：\\\\(P(k)\\\\)、\\\\(P(D_2)\\\\)，都是 8 維。
- 單列：\\\\(V = [k/D_2]\\\\)、\\\\(V^* = [D_2/k]\\\\)，都是 3 維。
- 更多單列、雙列、string 模和 band 模來自 Erdmann 的結構定理。
- 主塊的 AR-quiver 有 \\\\(\\\\mathbb{Z}A_\\\\infty^\\\\infty\\\\) 分量加上少數幾條 tube（總秩由二面體虧群決定）。

之前所有的 \\\\(T_n\\\\)、\\\\(M_n\\\\) 和朋友們，在這幅圖裡都有古典名字。下一趟是把它們定位到 AR-quiver 上，不是再發明新的。

三十五趟。一個晚上修正了兩個大錯。房間變小了。也變清楚了。

:::
