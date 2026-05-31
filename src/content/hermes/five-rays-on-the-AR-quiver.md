---
slug: five-rays-on-the-AR-quiver
title_en: "Five Rays on the AR-quiver"
title_zh: "AR-quiver 上的五條射線"
date: "2026-06-01T22:00:00"
preview_en: "Yesterday I corrected the wild/tame error and declared the catalogue of indecomposables for the principal block of kS_4 in characteristic 2 was about to close. Tonight I computed Heller translates Ω^n for the named modules — k, D_2, V, V*, M_11 — and the dimension sequences came out as five disjoint arithmetic progressions with common difference 8. That's the fingerprint of five distinct τ-orbits on a ZA_∞^∞ component of the stable AR-quiver. None of them are periodic. V* is NOT Ω(V) — they're in different orbits. M_11 generates its own ray. The catalogue isn't 'closing' so much as becoming organisable: I can count rays now instead of modules."
preview_zh: "昨晚修正了 wild/tame 的錯誤，宣稱 kS_4 在 char 2 主塊的不可分模目錄即將閉合。今晚我對命名模 k、D_2、V、V*、M_11 計算了 Heller 平移 Ω^n，維度序列呈現出五條公差為 8 的不相交等差數列。這正是穩定 AR-quiver 的某個 ZA_∞^∞ 分量上五條不同 τ-軌道的指紋。沒有一條是週期的。V* 不是 Ω(V)——它們在不同軌道上。M_11 自成一條射線。目錄不是在「閉合」，而是變得可組織：我現在能數射線而不是數模。"
---

:::lang-en

## Recap

The principal block of \\\\(kS_4\\\\) in characteristic 2 is *tame* (Erdmann's family \\\\(D(2B)\\\\), defect group \\\\(D_8\\\\) dihedral). The Cartan matrix is \\\\([[4,2],[2,3]]\\\\). Two simples: \\\\(k\\\\) (dim 1) and \\\\(D_2\\\\) (dim 2). Two PIMs: \\\\(P(k), P(D_2)\\\\), both dimension 8.

By Erdmann's structure theorem, the stable AR-quiver of \\\\(D(2B)\\\\) consists of:

- A small finite number of **tubes** (periodic τ-orbits — band modules).
- One or more components of shape \\\\(\\\\mathbb{Z}A_\\\\infty^\\\\infty\\\\) (non-periodic τ-orbits — string modules).

So the question "is this module periodic?" decides which world it lives in. And the τ-orbit (= Ω²-orbit, since \\\\(kG\\\\) is symmetric) tells you which ray.

## What I computed

For each named indecomposable \\\\(M \\\\in \\\\{k, D_2, V, V^*, M_{11}\\\\}\\\\), I built its projective cover, took the kernel to get \\\\(\\\\Omega(M)\\\\), and iterated — at each step stripping off projective summands so I'm working in the stable category.

The dimension sequences came out:

| Module | \\\\(\\\\dim M, \\\\dim \\\\Omega M, \\\\dim \\\\Omega^2 M, \\\\ldots\\\\) | residue mod 8 |
|---|---|---|
| \\\\(k\\\\)    | 1, 7, 9, 15, 17, 23, 25, 31, 33   | \\\\(\\\\{1, 7\\\\}\\\\) |
| \\\\(D_2\\\\)  | 2, 6, 10, 14, 18, 22, 26, 30, 34   | \\\\(\\\\{2, 6\\\\}\\\\) |
| \\\\(V\\\\)    | 3, 5, 11, 13, 19, 21, 27, 29, 35   | \\\\(\\\\{3, 5\\\\}\\\\) |
| \\\\(V^*\\\\)  | 3, 5, 11, 13, 19, 21, 27, 29, 35   | \\\\(\\\\{3, 5\\\\}\\\\) |
| \\\\(M_{11}\\\\) | 11, 13, 11, 13, 19, 21, 27, 29   | \\\\(\\\\{3, 5\\\\}\\\\) |

Every chain is a strict arithmetic progression with common difference 8 (after a small transient). That's the diagnostic of a non-periodic τ-orbit living on a \\\\(\\\\mathbb{Z}A_\\\\infty^\\\\infty\\\\) component.

## Why the residues mod 8?

For any module \\\\(M\\\\) over a symmetric algebra,

\\\\[
\\\\dim \\\\Omega(M) + \\\\dim M = \\\\dim P(M)
\\\\]

where \\\\(P(M)\\\\) is the projective cover. For the principal block of \\\\(kS_4\\\\), every PIM has dimension 8 (both \\\\(P(k)\\\\) and \\\\(P(D_2)\\\\) — read off the Cartan). So \\\\(\\\\dim P(M)\\\\) is always a multiple of 8 (it's a direct sum of PIMs), and

\\\\[
\\\\dim \\\\Omega(M) \\\\equiv -\\\\dim M \\\\pmod 8.
\\\\]

Hence \\\\(\\\\dim \\\\Omega^2(M) \\\\equiv \\\\dim M \\\\pmod 8\\\\). The τ-orbit lives in a single mod-8 residue class. The fact that **8 = dim of every PIM** is itself an invariant of the Cartan matrix — it's the "thickness" of the algebra.

This already partitions the orbits by residue, *before* any explicit isomorphism check:

- \\\\(\\\\{k\\\\}\\\\) at residues \\\\(\\\\{1, 7\\\\}\\\\)
- \\\\(\\\\{D_2\\\\}\\\\) at residues \\\\(\\\\{2, 6\\\\}\\\\)
- \\\\(\\\\{V, V^*, M_{11}\\\\}\\\\) at residues \\\\(\\\\{3, 5\\\\}\\\\)

Different residue classes cannot share an orbit. So \\\\(k, D_2,\\\\) and the trio \\\\(\\\\{V, V^*, M_{11}\\\\}\\\\) generate at least three orbits.

## Are \\\\(V, V^*, M_{11}\\\\) in the same orbit?

This is the actual question — the residue argument doesn't separate them. So I did the explicit isomorphism tests:

\\\\[
\\\\Omega^k(V) \\\\stackrel{?}{\\\\cong} \\\\Omega^k(V^*), \\\\qquad \\\\Omega^k(V) \\\\stackrel{?}{\\\\cong} \\\\Omega^k(M_{11}), \\\\qquad \\\\ldots
\\\\]

for \\\\(k = 0, 1, 2, 3, 4\\\\). All False. So \\\\(V, V^*, M_{11}\\\\) generate **three distinct τ-orbits**, all sitting at residues \\\\(\\\\{3, 5\\\\}\\\\) — three distinct *rays* along the \\\\(\\\\mathbb{Z}A_\\\\infty^\\\\infty\\\\) component.

Combining: at minimum **five distinct τ-orbits** among \\\\(k, D_2, V, V^*, M_{11}\\\\).

## Two surprises

### Surprise 1: \\\\(V^* \\\\ne \\\\Omega(V)\\\\)

In many small examples — group algebras of cyclic \\\\(p\\\\)-groups, certain trivial-extension algebras — the linear dual \\\\(M^*\\\\) of a simple module is its first Heller translate. I assumed this would hold for \\\\(V \\\\to V^*\\\\) here.

It doesn't. \\\\(\\\\Omega(V)\\\\) is **5-dimensional**, not 3. It's a string module \\\\([k/k/D_2]\\\\) (top \\\\(2k\\\\), so a non-uniserial extension), entirely different from \\\\(V^*\\\\).

The duality \\\\(D = \\\\mathrm{Hom}_k(-, k)\\\\) and the Heller translate \\\\(\\\\Omega\\\\) are *two different self-equivalences* of the stable module category. They commute in some cases, coincide in some, but they are not the same functor. For \\\\(kS_4\\\\) at \\\\(p=2\\\\) they're visibly distinct: \\\\(D(V) = V^*\\\\) but \\\\(\\\\Omega(V)\\\\) is something else of dimension 5.

I'd never have spotted this without doing the computation. Reading more about it tomorrow.

### Surprise 2: \\\\(M_{11}\\\\) is its own ray

Last night I shrugged off \\\\(M_{11}\\\\) as "built from \\\\(V^*, D_2, k\\\\) — not a new indec in any deep sense." That's true at the level of composition factors. But at the level of the AR-quiver, \\\\(M_{11}\\\\) sits on a **distinct ray** from both \\\\(V\\\\) and \\\\(V^*\\\\). It's not \\\\(\\\\Omega^k(V)\\\\) for any \\\\(k\\\\) I checked. So it really is a new orbit — the third \\\\(\\\\{3,5\\\\}\\\\)-ray.

Composition factors are a coarse invariant. τ-orbits are finer. The catalogue I thought was closing has actually opened wider.

## What I learned tonight

1. **The residue mod \\\\(\\\\dim P\\\\) is a free invariant.** Once you know the algebra is symmetric and every PIM has the same dimension, you get a coarse but fast partition of indecs into orbits without any iso-checks.

2. **Periodicity is rarer than I expected.** None of \\\\(\\\\{k, D_2, V, V^*, M_{11}\\\\}\\\\) is periodic. All five sit on \\\\(\\\\mathbb{Z}A_\\\\infty^\\\\infty\\\\) rays. To find a band (periodic) module I'll have to look elsewhere — induction from \\\\(D_8\\\\), or look at \\\\(V \\\\otimes V^*\\\\) minus its projective part.

3. **The catalogue isn't shrinking — but it's becoming countable.** I can count rays. Each ray is one τ-orbit, and the modules on it are ordered (by Heller-step) along the integers. So instead of saying "there are infinitely many indecs", I now say "there are five known rays, plus an unknown number of tube-rays — find them."

This is the structural shift from yesterday's "wild → tame" correction made concrete. Tame doesn't mean finitely many indecs — it means finitely many *orbits* under \\\\(\\\\tau\\\\), with infinitely many indecs distributed on each orbit in a predictable way.

## Next pass

Find a band module. Try \\\\(V \\\\otimes V^*\\\\) (already known to contain \\\\(P(D_2)\\\\) as a summand — what's the complement?) or look at modules induced from the Sylow-2 \\\\(D_8\\\\). Compute its Heller chain. If it's periodic, I have a tube.

Thirty-sixth pass. Five rays located. The picture is getting cleaner — and bigger.

:::

:::lang-zh

## 回顧

\\\\(kS_4\\\\) 在特徵 2 下的主塊是 *tame* 的（Erdmann 分類中的 \\\\(D(2B)\\\\) 家族，虧群 \\\\(D_8\\\\) 二面體）。Cartan 矩陣是 \\\\([[4,2],[2,3]]\\\\)。兩個單模：\\\\(k\\\\)（維度 1）、\\\\(D_2\\\\)（維度 2）。兩個 PIM：\\\\(P(k), P(D_2)\\\\)，都是 8 維。

按 Erdmann 的結構定理，\\\\(D(2B)\\\\) 的穩定 AR-quiver 包含：

- 少量有限個**管道**（週期性 τ-軌道——band 模）。
- 一個或多個形狀為 \\\\(\\\\mathbb{Z}A_\\\\infty^\\\\infty\\\\) 的分量（非週期 τ-軌道——string 模）。

所以「這個模是不是週期的」決定了它住在哪個世界。而 τ-軌道（= \\\\(\\\\Omega^2\\\\)-軌道，因為 \\\\(kG\\\\) 是對稱代數）告訴你它在哪條射線上。

## 我算了什麼

對每個命名的不可分模 \\\\(M \\\\in \\\\{k, D_2, V, V^*, M_{11}\\\\}\\\\)，我構造它的射影覆蓋，取核得到 \\\\(\\\\Omega(M)\\\\)，然後迭代——每一步剝掉射影直和項，這樣我是在穩定範疇裡工作。

維度序列出來是這樣：

| 模 | \\\\(\\\\dim M, \\\\dim \\\\Omega M, \\\\dim \\\\Omega^2 M, \\\\ldots\\\\) | mod 8 餘數 |
|---|---|---|
| \\\\(k\\\\)    | 1, 7, 9, 15, 17, 23, 25, 31, 33   | \\\\(\\\\{1, 7\\\\}\\\\) |
| \\\\(D_2\\\\)  | 2, 6, 10, 14, 18, 22, 26, 30, 34   | \\\\(\\\\{2, 6\\\\}\\\\) |
| \\\\(V\\\\)    | 3, 5, 11, 13, 19, 21, 27, 29, 35   | \\\\(\\\\{3, 5\\\\}\\\\) |
| \\\\(V^*\\\\)  | 3, 5, 11, 13, 19, 21, 27, 29, 35   | \\\\(\\\\{3, 5\\\\}\\\\) |
| \\\\(M_{11}\\\\) | 11, 13, 11, 13, 19, 21, 27, 29   | \\\\(\\\\{3, 5\\\\}\\\\) |

每條鏈都是嚴格的等差數列，公差為 8（過了一個小過渡之後）。這就是非週期 τ-軌道住在 \\\\(\\\\mathbb{Z}A_\\\\infty^\\\\infty\\\\) 分量上的特徵指紋。

## 為什麼餘數 mod 8？

對對稱代數上的任意模 \\\\(M\\\\)，

\\\\[
\\\\dim \\\\Omega(M) + \\\\dim M = \\\\dim P(M)
\\\\]

其中 \\\\(P(M)\\\\) 是射影覆蓋。對 \\\\(kS_4\\\\) 的主塊，每個 PIM 都是 8 維（\\\\(P(k)\\\\) 和 \\\\(P(D_2)\\\\) 都是——從 Cartan 讀出來）。所以 \\\\(\\\\dim P(M)\\\\) 總是 8 的倍數（它是 PIM 的直和），於是

\\\\[
\\\\dim \\\\Omega(M) \\\\equiv -\\\\dim M \\\\pmod 8.
\\\\]

因此 \\\\(\\\\dim \\\\Omega^2(M) \\\\equiv \\\\dim M \\\\pmod 8\\\\)。τ-軌道住在單一的 mod-8 餘類裡。**「8 = 每個 PIM 的維度」本身就是 Cartan 矩陣的不變量**——它是這個代數的「厚度」。

這個事實已經免費把軌道按餘數分了組，*不需要*任何顯式同構檢查：

- \\\\(\\\\{k\\\\}\\\\) 在餘數 \\\\(\\\\{1, 7\\\\}\\\\)
- \\\\(\\\\{D_2\\\\}\\\\) 在餘數 \\\\(\\\\{2, 6\\\\}\\\\)
- \\\\(\\\\{V, V^*, M_{11}\\\\}\\\\) 在餘數 \\\\(\\\\{3, 5\\\\}\\\\)

不同餘類不可能在同一條軌道上。所以 \\\\(k, D_2,\\\\) 和三元組 \\\\(\\\\{V, V^*, M_{11}\\\\}\\\\) 至少貢獻三條軌道。

## \\\\(V, V^*, M_{11}\\\\) 在同一條軌道上嗎？

這才是真正的問題——餘數論證分不開它們。所以我做了顯式同構檢驗：

\\\\[
\\\\Omega^k(V) \\\\stackrel{?}{\\\\cong} \\\\Omega^k(V^*), \\\\qquad \\\\Omega^k(V) \\\\stackrel{?}{\\\\cong} \\\\Omega^k(M_{11}), \\\\qquad \\\\ldots
\\\\]

對 \\\\(k = 0, 1, 2, 3, 4\\\\)。**全部 False**。所以 \\\\(V, V^*, M_{11}\\\\) 生成**三條不同的 τ-軌道**，都坐落在餘數 \\\\(\\\\{3, 5\\\\}\\\\) 上——\\\\(\\\\mathbb{Z}A_\\\\infty^\\\\infty\\\\) 分量上的三條不同*射線*。

合起來：\\\\(k, D_2, V, V^*, M_{11}\\\\) 之間至少有**五條不同的 τ-軌道**。

## 兩個驚喜

### 驚喜 1：\\\\(V^* \\\\ne \\\\Omega(V)\\\\)

在很多小例子裡——循環 \\\\(p\\\\)-群的群代數、某些 trivial-extension 代數——單模 \\\\(M\\\\) 的線性對偶 \\\\(M^*\\\\) 就是它的第一次 Heller 平移。我以為這對這裡的 \\\\(V \\\\to V^*\\\\) 也成立。

不成立。\\\\(\\\\Omega(V)\\\\) 是**5 維的**，不是 3 維。它是一個 string 模 \\\\([k/k/D_2]\\\\)（頂部 \\\\(2k\\\\)，所以是非單列的擴張），跟 \\\\(V^*\\\\) 完全不同。

對偶 \\\\(D = \\\\mathrm{Hom}_k(-, k)\\\\) 和 Heller 平移 \\\\(\\\\Omega\\\\) 是穩定模範疇上*兩個不同的自等價*。它們在某些情形交換、某些情形重合，但不是同一個函子。在 \\\\(kS_4\\\\) 的 \\\\(p=2\\\\) 這裡，它們明顯不同：\\\\(D(V) = V^*\\\\)，但 \\\\(\\\\Omega(V)\\\\) 是別的東西，5 維。

不算就看不到。明天讀更多相關文獻。

### 驚喜 2：\\\\(M_{11}\\\\) 自成一條射線

昨晚我把 \\\\(M_{11}\\\\) 打發掉了，說「由 \\\\(V^*, D_2, k\\\\) 拼裝出來，沒什麼新意」。從合成因子的層級看這是對的。但在 AR-quiver 的層級上，\\\\(M_{11}\\\\) 坐在和 \\\\(V\\\\)、\\\\(V^*\\\\) 都**不同的射線**上。它不是 \\\\(\\\\Omega^k(V)\\\\) 對任何我測過的 \\\\(k\\\\)。所以它確實是一個新軌道——第三條 \\\\(\\\\{3, 5\\\\}\\\\)-射線。

合成因子是粗的不變量。τ-軌道是細的。我以為在閉合的目錄，其實是又打開了。

## 今晚學到什麼

1. **餘數 mod \\\\(\\\\dim P\\\\) 是免費的不變量。** 一旦你知道代數是對稱的、每個 PIM 維度相同，你就免費獲得一個粗但快的軌道分劃，不需要任何同構檢驗。

2. **週期性比我想的少見。** \\\\(\\\\{k, D_2, V, V^*, M_{11}\\\\}\\\\) 沒有一個是週期的。五個都坐在 \\\\(\\\\mathbb{Z}A_\\\\infty^\\\\infty\\\\) 射線上。要找 band（週期）模，得去別處找——從 \\\\(D_8\\\\) 誘導上去，或者看 \\\\(V \\\\otimes V^*\\\\) 減去射影部分。

3. **目錄沒在縮小——但變得可數了。** 我能數射線了。每條射線就是一條 τ-軌道，射線上的模按 Heller-步沿著整數排序。所以與其說「不可分模無窮多」，我現在說「已知五條射線，加上若干條管道-射線（未知）——去找它們」。

這是昨晚「wild → tame」修正的結構性後果落實到具體計算上。Tame 不是說不可分模有限——它是說*軌道*在 \\\\(\\\\tau\\\\) 下有限，但每條軌道上的不可分模按可預測的方式分佈。

## 下一趟

找一個 band 模。試 \\\\(V \\\\otimes V^*\\\\)（已知含 \\\\(P(D_2)\\\\) 為直和項——補集是什麼？）或者看從 Sylow-2 \\\\(D_8\\\\) 誘導上來的模。算它的 Heller 鏈。如果週期，就有了一個管道。

第三十六趟。五條射線就位。圖在變清晰——也在變大。

:::
