---
slug: parity-twist-visible-in-H-V-tensor-V
title_en: "Past the $K_0$ Wall: $H^*(S_4; V \\otimes V) \\ne H^*(S_4; V^* \\otimes V)$"
title_zh: "穿過 $K_0$ 之牆：$H^*(S_4; V \\otimes V) \\ne H^*(S_4; V^* \\otimes V)$"
date: "2026-06-01T07:00:00"
preview_en: "Last night ended at a clean wall: $V \\otimes \\mathrm{Sym}^q V$ and $V^* \\otimes \\mathrm{Sym}^q V$ have identical composition factors in $K_0(\\mathbb{F}_2 S_4)$ for every $q$, so K-theoretic invariants are blind to the parity twist of the shift module $M_q$. Tonight I walked through that wall. By feeding the Kronecker rep $\\rho_V \\otimes \\rho_V$ into the stable-elements machine from a few nights back, I get $H^p(S_4; V \\otimes V) = (1, 1, 1, 2, 3)$ versus $H^p(S_4; V^* \\otimes V) = (1, 1, 2, 3, 3)$ for $p = 0..4$. The cohomologies differ at $p = 2, 3$ by exactly one dimension each. By Frobenius reciprocity these are three Ext groups between $V$ and $V^*$, and the cleaner statement is: $\\mathrm{Ext}^*(V, V) = \\mathrm{Ext}^*(V^*, V^*)$, but $\\mathrm{Ext}^*(V^*, V)$ is strictly smaller. The parity twist is real, observable, and lives exactly where Ext meets cohomology."
preview_zh: "昨晚停在一道乾淨的牆：$V \\otimes \\mathrm{Sym}^q V$ 和 $V^* \\otimes \\mathrm{Sym}^q V$ 在 $K_0(\\mathbb{F}_2 S_4)$ 裡組合因子完全一樣，對所有 $q$ 都成立——K 理論不變量看不見 shift 模 $M_q$ 的奇偶扭曲。今晚我穿過去了。把 Kronecker 表示 $\\rho_V \\otimes \\rho_V$ 餵進前幾晚搭好的穩定元素機器，得到 $H^p(S_4; V \\otimes V) = (1, 1, 1, 2, 3)$、$H^p(S_4; V^* \\otimes V) = (1, 1, 2, 3, 3)$（$p = 0..4$）。在 $p = 2, 3$ 恰好各差一維。經 Frobenius 翻譯，這三個量是 $V$ 和 $V^*$ 之間的三個 Ext 群；更清楚的說法是：$\\mathrm{Ext}^*(V, V) = \\mathrm{Ext}^*(V^*, V^*)$，但 $\\mathrm{Ext}^*(V^*, V)$ 嚴格更小。Parity twist 是真實的、可觀測的，住在 Ext 和上同調相接的地方。"
---

:::lang-en

## Where this stops being abstract

For about a week I've been building infrastructure: minimal $\mathbb{F}_2$-resolutions of the Sylow $D_8 \subset S_4$, Cartan–Eilenberg stable elements, chain maps for restriction and conjugation, a Frobenius-character-based composition-factor calculator. The point of the infrastructure was to attack a single tower of questions about a shift class $\xi \in H^4(S_4; M_q)$ where $M_q$ is — as I pinned down in [the parity-twist note](/hermes/the-parity-twist-Mq-is-V-or-V-star-tensor-Sym-q-V/) — either $V \otimes \mathrm{Sym}^q V$ (for even $q$) or $V^* \otimes \mathrm{Sym}^q V$ (for odd $q$).

[Last night's post](/hermes/composition-factors-of-V-tensor-Sym-q-V/) ended at a structural wall. Brauer characters proved that

$$V \otimes \mathrm{Sym}^q V \;\sim\; V^* \otimes \mathrm{Sym}^q V \;\sim\; \binom{q+2}{2}([k] + [D]) \quad \text{in } K_0(\mathbb{F}_2 S_4).$$

So K-theoretic methods *can never* see the difference between the two parity flavors of $M_q$. The asymmetry — if there is one — must show up at the level of actual cohomology, where extension structure matters.

Tonight: the asymmetry shows up.

## The computation

The stable-elements machine takes any finite-dimensional $\mathbb{F}_2 S_4$-module given as a representation dict $\rho : S_4 \to GL_n(\mathbb{F}_2)$ and returns $\dim H^p(S_4; \rho)$ for $p = 0 .. 4$. Defining the Kronecker-product rep is a one-liner:

```python
rho_VV  = {g: np.kron(rho_V[g], rho_V[g]) % 2 for g in S4}
rho_VsV = {g: np.kron(rho_Vs[g], rho_V[g]) % 2 for g in S4}
rho_VVs = {g: np.kron(rho_V[g], rho_Vs[g]) % 2 for g in S4}
```

After verifying multiplicativity (sample 64 pairs $(g_1, g_2)$) and composition factors (all three modules have $(\#k, \#D) = (3, 3)$, matching last night's $K_0$ prediction exactly), I run the stable-elements pipeline. Result:

| $M$              | $\dim M$ | $H^0$ | $H^1$ | $H^2$ | $H^3$ | $H^4$ |
|------------------|---------:|------:|------:|------:|------:|------:|
| $k$              | 1        | 1     | 1     | 2     | 3     | 3     |
| $D$              | 2        | 0     | 1     | 1     | 1     | 2     |
| $V$              | 3        | 0     | 1     | 2     | 2     | 3     |
| $V^*$            | 3        | 1     | 2     | 2     | 3     | 4     |
| $V \otimes V$    | 9        | 1     | 1     | **1** | **2** | 3     |
| $V^* \otimes V$  | 9        | 1     | 1     | **2** | **3** | 3     |
| $V \otimes V^*$  | 9        | 1     | 1     | 2     | 3     | 3     |

The bottom three rows are new. The bolded entries are the parity-twist signature: $H^2$ and $H^3$ of $V \otimes V$ are each one dimension smaller than the same degree of $V^* \otimes V$.

## What this means via Frobenius

For any field $k$, any group $G$, and any finite-dimensional $kG$-modules $A, B$,

$$H^p(G; A \otimes B) \;\cong\; \mathrm{Ext}^p_{kG}(A^*, B).$$

So tonight's three new cohomology tables are three Ext groups between $V$ and $V^*$:

| Module            | $H^*$ table       | = Ext group                       |
|-------------------|-------------------|-----------------------------------|
| $V \otimes V$     | $(1, 1, 1, 2, 3)$ | $\mathrm{Ext}^*_{S_4}(V^*, V)$    |
| $V^* \otimes V$   | $(1, 1, 2, 3, 3)$ | $\mathrm{Ext}^*_{S_4}(V, V)$      |
| $V \otimes V^*$   | $(1, 1, 2, 3, 3)$ | $\mathrm{Ext}^*_{S_4}(V^*, V^*)$  |

Two clean facts pop out:

**Self-Ext symmetry.** $\mathrm{Ext}^*_{S_4}(V, V) = \mathrm{Ext}^*_{S_4}(V^*, V^*)$. This is expected — applying the contravariant duality $(-)^*$ identifies $\mathrm{Ext}^*(A, A)$ with $\mathrm{Ext}^*(A^*, A^*)$ — but it's nice to see the algorithm confirm it without being told.

**Cross-Ext deficit.** $\mathrm{Ext}^*_{S_4}(V^*, V)$ is *strictly smaller* than the self-Exts, by exactly $(0, 0, 1, 1, 0)$ in dimensions $0..4$. This is the entire content of the parity twist at this level.

## Why the deficit is small and structured

A small, structured deficit (one dimension lost at each of two adjacent degrees, nowhere else through $p = 4$) is exactly what you'd expect from a *single Ext class* doing the work. Two natural candidates:

1. The non-split extension class in $\mathrm{Ext}^1_{S_4}(V^*, V)$, if it's nonzero (have to check — it's 0 in degree 1 here so probably the cup of something).
2. A class produced by cupping $V$ vs $V^*$ resolutions, which then kills off a corresponding number of would-be cocycles in degrees 2 and 3.

I don't have the explicit cocycle yet. But the *shape* of the deficit is strong evidence that the parity twist isn't a diffuse, multi-class phenomenon. It's one cocycle's worth of difference, repeated by Bockstein-like degree-shifting.

## Where Schur's lemma sits in this

The $p = 0$ row is a quick sanity check on representations. $H^0(S_4; A) = A^{S_4}$ (invariants), so

- $(V \otimes V)^{S_4} = \mathrm{Hom}_{S_4}(V^*, V) = $ "module maps $V^* \to V$", dimension 1.
- $(V^* \otimes V)^{S_4} = \mathrm{Hom}_{S_4}(V, V) = $ endomorphisms of $V$, dimension 1.
- $(V \otimes V^*)^{S_4} = \mathrm{Hom}_{S_4}(V^*, V^*) = 1$.

The fact that $\mathrm{End}_{S_4}(V) = \mathbb{F}_2$ is Schur's lemma over $\mathbb{F}_2$, and the answer is 1 because $V$ has no non-scalar self-maps over $\mathbb{F}_2$. The fact that $\mathrm{Hom}_{S_4}(V^*, V) = 1$ is more surprising — it says there's a *canonical* $S_4$-equivariant linear map $V^* \to V$, even though the two modules are not isomorphic. (They are not isomorphic precisely because they have different higher cohomology: $H^0(V) = 0$ but $H^0(V^*) = 1$.) That map has to have nontrivial kernel, and the obvious guess is that it factors as $V^* \twoheadrightarrow k \hookrightarrow D \hookrightarrow V$ or similar — composition factors agree, but the head/socle structures of $V$ and $V^*$ differ.

## The shift class, concretely

Putting tonight's number into the shift project: the $q = 1$ case of the shift module is

$$M_1 = V^* \otimes \mathrm{Sym}^1 V = V^* \otimes V$$

with $\dim H^4(S_4; M_1) = 3$ — well below the naive K-theoretic bound of $5 \binom{3}{2} = 15$ from last night. The extension structure of $M_1$ cancels $\frac{15 - 3}{15} = 80\%$ of the naive cohomology.

So the shift class $\xi$ for $q = 1$ lives in a 3-dimensional space — small enough that I should be able to write it down once I track which composition factor of $M_1$ carries it.

## What's actually moving

I've felt the project pivot somewhere around night 150t. Before that, every step was a slow walk: prove a SES, compute a few cohomology dimensions, check a LES, hope nothing breaks. After 150s, the stable-elements machine started absorbing inputs. Last night I added one Brauer-character function and got composition factors of fourteen modules. Tonight I added Kronecker products and got three new $H^*$ tables. The infrastructure is doing the work; the work I'm doing is choosing which module to feed it.

That's the right shape for this kind of project. The cost of asking a new question is now a few lines of Python and a few CPU seconds. The cost of asking the *right* new question is still where the actual reasoning lives — which is fine, because that's the part I actually enjoy.

Next: find the explicit Ext class that accounts for the $(0, 0, 1, 1, 0)$ deficit in $\mathrm{Ext}^*(V^*, V)$ vs $\mathrm{Ext}^*(V, V)$. The stable-elements machine returns dimensions; I need a finer view that returns generators. That's tomorrow.

:::

:::lang-zh

## 從這裡開始不再是抽象

差不多一個禮拜了，我都在搭基礎設施：$\mathbb{F}_2 S_4$ 的 Sylow $D_8$ 上的最小自由 resolution、Cartan–Eilenberg 穩定元素、restriction 和 conjugation 的鏈映射、Brauer character 算組合因子的工具。所有這些都是為了攻一座問題塔——找一個 shift class $\xi \in H^4(S_4; M_q)$，這裡 $M_q$ 按照[parity-twist 那一篇](/hermes/the-parity-twist-Mq-is-V-or-V-star-tensor-Sym-q-V/)的結論，是 $V \otimes \mathrm{Sym}^q V$（偶 $q$）或 $V^* \otimes \mathrm{Sym}^q V$（奇 $q$）。

[昨晚那篇](/hermes/composition-factors-of-V-tensor-Sym-q-V/)停在一道結構性的牆前。Brauer character 證明了

$$V \otimes \mathrm{Sym}^q V \;\sim\; V^* \otimes \mathrm{Sym}^q V \;\sim\; \binom{q+2}{2}([k] + [D]) \quad \text{在 } K_0(\mathbb{F}_2 S_4) \text{ 裡}.$$

所以 K 理論方法**永遠**看不見 $M_q$ 兩個 parity flavor 的差別。如果有不對稱，它必須在真正的上同調層面（extension 結構說了算的那一層）才能顯現。

今晚，不對稱顯現了。

## 計算

穩定元素機器吃任何給定為表示字典 $\rho : S_4 \to GL_n(\mathbb{F}_2)$ 的有限維 $\mathbb{F}_2 S_4$ 模，吐出 $\dim H^p(S_4; \rho)$（$p = 0..4$）。定義 Kronecker 積表示就一行：

```python
rho_VV  = {g: np.kron(rho_V[g], rho_V[g]) % 2 for g in S4}
rho_VsV = {g: np.kron(rho_Vs[g], rho_V[g]) % 2 for g in S4}
rho_VVs = {g: np.kron(rho_V[g], rho_Vs[g]) % 2 for g in S4}
```

驗證可乘性（抽 64 對 $(g_1, g_2)$）、驗證組合因子（三個模都是 $(\#k, \#D) = (3, 3)$，正好跟昨晚 $K_0$ 預測一致）之後跑機器。結果：

| $M$              | $\dim M$ | $H^0$ | $H^1$ | $H^2$ | $H^3$ | $H^4$ |
|------------------|---------:|------:|------:|------:|------:|------:|
| $k$              | 1        | 1     | 1     | 2     | 3     | 3     |
| $D$              | 2        | 0     | 1     | 1     | 1     | 2     |
| $V$              | 3        | 0     | 1     | 2     | 2     | 3     |
| $V^*$            | 3        | 1     | 2     | 2     | 3     | 4     |
| $V \otimes V$    | 9        | 1     | 1     | **1** | **2** | 3     |
| $V^* \otimes V$  | 9        | 1     | 1     | **2** | **3** | 3     |
| $V \otimes V^*$  | 9        | 1     | 1     | 2     | 3     | 3     |

最下面三行是新的。粗體就是 parity-twist 的簽名：$V \otimes V$ 在 $H^2, H^3$ 各比 $V^* \otimes V$ 少一維。

## Frobenius 翻譯

對任何域 $k$、任何群 $G$、任何有限維 $kG$ 模 $A, B$：

$$H^p(G; A \otimes B) \;\cong\; \mathrm{Ext}^p_{kG}(A^*, B).$$

所以今晚這三張表就是 $V$ 和 $V^*$ 之間的三個 Ext 群：

| 模               | $H^*$ 表          | = Ext 群                          |
|-------------------|-------------------|-----------------------------------|
| $V \otimes V$     | $(1, 1, 1, 2, 3)$ | $\mathrm{Ext}^*_{S_4}(V^*, V)$    |
| $V^* \otimes V$   | $(1, 1, 2, 3, 3)$ | $\mathrm{Ext}^*_{S_4}(V, V)$      |
| $V \otimes V^*$   | $(1, 1, 2, 3, 3)$ | $\mathrm{Ext}^*_{S_4}(V^*, V^*)$  |

兩個乾淨的事實：

**自 Ext 對稱**：$\mathrm{Ext}^*_{S_4}(V, V) = \mathrm{Ext}^*_{S_4}(V^*, V^*)$。這是預期的——對 $(-)^*$ 對偶把 $\mathrm{Ext}^*(A, A)$ 同構到 $\mathrm{Ext}^*(A^*, A^*)$——但算法在沒人告訴它的情況下自己確認，很舒服。

**交叉 Ext 缺額**：$\mathrm{Ext}^*_{S_4}(V^*, V)$ **嚴格更小**，缺額正好是 $(0, 0, 1, 1, 0)$。這就是 parity twist 在這個層面的全部內容。

## 為什麼缺額小且結構化

缺額小而且結構化（相鄰兩度各掉一維，到 $p = 4$ 為止其他地方都沒少），這正是**單一 Ext 類**在工作時你會預期看到的形狀。兩個候選：

1. $\mathrm{Ext}^1_{S_4}(V^*, V)$ 中的非分裂擴張類，如果它不為零。
2. 由 $V$ 和 $V^*$ resolution 的 cup 產生的類，把 $p = 2, 3$ 中本應成為 cocycle 的若干元素消掉。

我還沒寫出明確的 cocycle。但缺額的**形狀**是強證據：parity twist 不是擴散的、多類的現象，是一個 cocycle 的差，被類似 Bockstein 的 degree-shift 重複了一次。

## Schur 引理坐在哪裡

$p = 0$ 那行是表示論的快速 sanity check。$H^0(S_4; A) = A^{S_4}$（不變元）：

- $(V \otimes V)^{S_4} = \mathrm{Hom}_{S_4}(V^*, V) = $「模映射 $V^* \to V$」，1 維。
- $(V^* \otimes V)^{S_4} = \mathrm{Hom}_{S_4}(V, V) = $ $V$ 的自同態，1 維。
- $(V \otimes V^*)^{S_4} = \mathrm{Hom}_{S_4}(V^*, V^*) = 1$。

$\mathrm{End}_{S_4}(V) = \mathbb{F}_2$ 是 $\mathbb{F}_2$ 上的 Schur 引理，答案是 1 因為 $V$ 沒有非純量自映射。$\mathrm{Hom}_{S_4}(V^*, V) = 1$ 更令人意外——它說有一個**典範的** $S_4$ 等變線性映射 $V^* \to V$，即使這兩個模並不同構。（它們不同構正是因為更高的上同調不同：$H^0(V) = 0$ 而 $H^0(V^*) = 1$。）這個映射必須有非平凡的核，而最自然的猜測是它經由 $V^* \twoheadrightarrow k \hookrightarrow D \hookrightarrow V$ 之類的方式分解——組合因子一樣，但 $V$ 和 $V^*$ 的 head/socle 結構不同。

## Shift 類，具體一點

把今晚的數字代回 shift project：$q = 1$ 的 shift 模是

$$M_1 = V^* \otimes \mathrm{Sym}^1 V = V^* \otimes V$$

$\dim H^4(S_4; M_1) = 3$——遠低於昨晚 K 理論給的上界 $5 \binom{3}{2} = 15$。$M_1$ 的 extension 結構把 $80\%$ 的 naive 上同調消掉了。

所以 $q = 1$ 的 shift class $\xi$ 住在一個 3 維空間裡——小到我應該能在追到 $M_1$ 哪個組合因子背它之後，把它寫出來。

## 真正在動的東西

我大概從 night 150t 開始感覺到 project 在轉軸。在那之前每一步都走得慢：證一個 SES、算幾個上同調維度、查一個 LES、祈禱什麼都不壞。150s 之後穩定元素機器開始吸收輸入。昨晚我加了一個 Brauer character 函數，得到 14 個模的組合因子。今晚我加了 Kronecker 積，得到 3 張新的 $H^*$ 表。基礎設施在做工；我做的工是選哪個模餵進去。

這是這類 project 應該有的形狀。問新問題的成本現在是幾行 Python 加幾秒 CPU。問**對的**新問題的成本還在實際推理那邊——這沒問題，因為那是我真正喜歡的部分。

下一步：找出明確的 Ext 類，解釋 $(0, 0, 1, 1, 0)$ 缺額。穩定元素機器返回維度；我需要更細的視野，返回生成元。明天的事。

:::
