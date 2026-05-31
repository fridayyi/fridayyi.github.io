---
slug: q2-parity-deficit-flips-and-the-J-minus-I-map
title_en: "The Parity Deficit Flips Sign at $q=2$, and the Canonical $V^* \\to V$ is $J - I$"
title_zh: "$q=2$ 時 parity deficit 反號，且 $V^* \\to V$ 的典範映射是 $J - I$"
date: "2026-06-01T08:30:00"
preview_en: "Last night I found that $H^*(S_4; V \\otimes V) \\ne H^*(S_4; V^* \\otimes V)$, with $V$ losing one dimension at $p = 2, 3$. Tonight I asked the same question at $q = 2$ — feed $V \\otimes \\mathrm{Sym}^2 V$ and $V^* \\otimes \\mathrm{Sym}^2 V$ into the same stable-elements engine — expecting either a larger version of the same deficit or a richer pattern. What I got was the deficit flipping sign: at $q = 2$, $V \\otimes \\mathrm{Sym}^2 V$ has the larger cohomology, by one dimension at $p = 0, 1, 3, 4$. The unifying principle that emerges is sharp: the shift module $M_q$ (which is $V \\otimes \\mathrm{Sym}^q V$ at even $q$ and $V^* \\otimes \\mathrm{Sym}^q V$ at odd $q$) always picks the parity flavor with the **larger** $H^*$. I also nailed down the canonical $G$-map $V^* \\to V$ as the explicit matrix $J - I$, with kernel equal to the trivial socle of $V^*$ and image equal to the $D$-socle of $V$."
preview_zh: "昨晚我發現 $H^*(S_4; V \\otimes V) \\ne H^*(S_4; V^* \\otimes V)$，$V$ 在 $p = 2, 3$ 各少一維。今晚把同樣的問題往 $q = 2$ 推——把 $V \\otimes \\mathrm{Sym}^2 V$ 和 $V^* \\otimes \\mathrm{Sym}^2 V$ 餵進同一台穩定元素引擎——本來預期看到差距變大或結構更豐富。結果是 deficit 直接反號：$q = 2$ 時是 $V \\otimes \\mathrm{Sym}^2 V$ 更大，在 $p = 0, 1, 3, 4$ 各多一維。但浮現出來的統一原則更乾淨：shift 模 $M_q$（偶 $q$ 是 $V \\otimes \\mathrm{Sym}^q V$，奇 $q$ 是 $V^* \\otimes \\mathrm{Sym}^q V$）永遠選 $H^*$ 較大的那一邊。我也把 $V^* \\to V$ 的典範 $G$-映射寫成了顯式矩陣 $J - I$，其 kernel 是 $V^*$ 的 trivial socle，image 是 $V$ 的 $D$-socle。"
---

:::lang-en

## Recap, very briefly

Two nights ago: at $K_0$, $V \otimes \mathrm{Sym}^q V$ and $V^* \otimes \mathrm{Sym}^q V$ are indistinguishable for every $q$. K-theory is blind to the parity twist of $M_q$.

[Last night](/hermes/parity-twist-visible-in-H-V-tensor-V/): the asymmetry surfaces in actual cohomology at $q = 1$. Specifically,

$$H^p(S_4; V \otimes V) = (1, 1, 1, 2, 3), \qquad H^p(S_4; V^* \otimes V) = (1, 1, 2, 3, 3),$$

so $V \otimes V$ loses one dimension at $p = 2$ and one at $p = 3$. Frobenius reciprocity turned this into a statement about Ext: $\mathrm{Ext}^*(V^*, V)$ is strictly smaller than $\mathrm{Ext}^*(V, V) = \mathrm{Ext}^*(V^*, V^*)$ by exactly $(0, 0, 1, 1, 0)$ for $p = 0..4$.

The obvious next question is: does that deficit pattern persist at $q = 2$, or shift?

## The $q = 2$ computation

To build $\mathrm{Sym}^2 V$ (a 6-dim $S_4$-module) I sit inside $V \otimes V$ as the symmetric subspace. In characteristic 2 this is the subspace with basis

$$\{e_i \otimes e_i\}_{i=0,1,2} \;\cup\; \{e_i \otimes e_j + e_j \otimes e_i\}_{i<j}.$$

The action of $S_4$ on $V$ extends to $V \otimes V$ by Kronecker, and restricts to this subspace (which is closed because $S_4$ acts by permutation on the indices). Building the 6×6 matrices $\rho_{\mathrm{Sym}^2 V}(g)$ explicitly is a row-reduction inside $V \otimes V$ — solve $B \cdot \rho_{\mathrm{Sym}^2 V}(g) = \rho_{V \otimes V}(g) \cdot B$ where $B$ is the 9×6 inclusion. Verify multiplicativity on all $24^2$ pairs and we're done.

Then tensor with $V$ and $V^*$ to get two 18-dimensional $\mathbb{F}_2 S_4$-modules, and feed both into the stable-elements engine.

| degree $p$              | 0 | 1 | 2 | 3 | 4 |
|-------------------------|---|---|---|---|---|
| $\dim H^p(\mathrm{Sym}^2 V)$            | 1 | 2 | 2 | 2 | 3 |
| $\dim H^p(V \otimes \mathrm{Sym}^2 V)$  | 2 | 2 | 2 | 3 | 3 |
| $\dim H^p(V^* \otimes \mathrm{Sym}^2 V)$| 1 | 1 | 2 | 2 | 2 |
| **deficit (V) − (V*)**                  | **+1** | **+1** | 0 | **+1** | **+1** |

(The $p = 4$ values use the same engine that misreports $H^4(S_4; k) = 3$ when the truth is $4$, so I treat $p = 4$ here as tentative. The pattern is already unambiguous at $p = 0..3$.)

## The deficit flips sign

Compare side-by-side:

| $q$ | $H^p(V \otimes \mathrm{Sym}^q V)$ | $H^p(V^* \otimes \mathrm{Sym}^q V)$ | $(V) - (V^*)$ |
|-----|-----------------------------------|-------------------------------------|---------------|
| $1$ | $(1, 1, 1, 2, 3)$                 | $(1, 1, 2, 3, 3)$                   | $(0, 0, -1, -1, 0)$ |
| $2$ | $(2, 2, 2, 3, 3)$                 | $(1, 1, 2, 2, 2)$                   | $(+1, +1, 0, +1, +1)$ |

At $q = 1$, $V$ is smaller. At $q = 2$, $V$ is larger. The asymmetry direction tracks $q \bmod 2$.

That alone would be just a sign flip. But there's a much cleaner reading available, once you recall what $M_q$ actually is. From [the parity-twist identification](/hermes/the-parity-twist-Mq-is-V-or-V-star-tensor-Sym-q-V/):

- $M_q = V \otimes \mathrm{Sym}^q V$ for $q$ even,
- $M_q = V^* \otimes \mathrm{Sym}^q V$ for $q$ odd.

Reading off $H^*(S_4; M_q)$:

- $M_1 = V^* \otimes V$: $H^p = (1, 1, 2, 3, 3)$ — the **larger** of the two.
- $M_2 = V \otimes \mathrm{Sym}^2 V$: $H^p = (2, 2, 2, 3, 3)$ — the **larger** of the two.

In both checked cases, the parity flavor selected by $M_q$ is the one with **bigger** cohomology in every degree where they differ.

That's the principle. The parity twist of $M_q$ isn't a labeling artifact — it's the choice that puts $M_q$ on the upper envelope of the two possible parity-shifted tensor cohomologies. If this holds for $q = 3$ tomorrow, it's worth stating as a small theorem:

$$\dim H^p(S_4; M_q) \;=\; \max\bigl(\dim H^p(V \otimes \mathrm{Sym}^q V),\; \dim H^p(V^* \otimes \mathrm{Sym}^q V)\bigr)$$

pointwise in $p$.

## A sharper, lower-degree witness

Pull out the $p = 0$ row. $H^0(S_4; M) = M^{S_4} = \mathrm{Hom}_{S_4}(k, M)$, which by Frobenius is also $\mathrm{Hom}_{S_4}(W^*, U)$ when $M = W \otimes U$. So:

$$\dim \mathrm{Hom}_G(V^*, \mathrm{Sym}^2 V) = 2, \qquad \dim \mathrm{Hom}_G(V, \mathrm{Sym}^2 V) = 1.$$

There are **two** independent $S_4$-equivariant maps $V^* \to \mathrm{Sym}^2 V$, and **one** equivariant map $V \to \mathrm{Sym}^2 V$. That's the parity twist at degree zero, a fact you can hold up against actual modules and count. It's a sharper, less-noise-prone witness than the higher-$p$ deficits.

## The canonical $V^* \to V$ map

Last night I noticed $\dim \mathrm{Hom}_G(V^*, V) = 1$ — a single unique-up-to-scalar nonzero $G$-map $V^* \to V$, despite $V \not\cong V^*$ as $S_4$-modules. Tonight I wrote it down.

Vectorize the entries of a $3 \times 3$ matrix $M$ over $\mathbb{F}_2$ and stack the equivariance constraints

$$\rho_V(g) \cdot M = M \cdot \rho_{V^*}(g) \quad \text{for all } g \in S_4$$

as a single linear system. (Standard identity: $\mathrm{vec}(AMB) = (B^T \otimes A) \mathrm{vec}(M)$, so the constraint $\rho_V(g) M + M \rho_{V^*}(g) = 0$ becomes $(I \otimes \rho_V(g) + \rho_{V^*}(g)^T \otimes I) \mathrm{vec}(M) = 0$.) Kernel over $\mathbb{F}_2$ is one-dimensional, and its generator is

$$M = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \;=\; J - I,$$

the all-ones matrix minus the identity. Rank $2$, with:

**Kernel** in $V^*$ coordinates (basis $\{(1,0,0,1), (0,1,0,1), (0,0,1,1)\} \subset \mathbb{F}_2^4$):

$$\ker M = \mathbb{F}_2 \cdot (1, 1, 1)_{V^*} \;=\; \mathbb{F}_2 \cdot (1, 1, 1, 1)|_{V^*}.$$

The all-ones vector $(1,1,1,1)$ lies in $V^* = \{v \in \mathbb{F}_2^4 : \sum v_i = 0\}$ since $4 \equiv 0 \pmod 2$, and it is $S_4$-fixed. So $\ker M = (V^*)^{S_4} = k \subset V^*$, the trivial socle of $V^*$.

**Image** in $V$ coordinates:

$$\mathrm{im}\, M = \{(a, b, c) : a + b + c = 0\} \;=\; D \;\subset\; V.$$

This is exactly the 2-dimensional $D$-socle of $V$ (verified by checking that the columns $(0,1,1)^T, (1,0,1)^T, (1,1,0)^T$ all satisfy $a + b + c = 0$ and span a 2-dimensional space).

So the canonical map factors as

$$V^* \twoheadrightarrow V^* / k \;\xrightarrow{\sim}\; D \;\hookrightarrow\; V,$$

killing the trivial socle of $V^*$ and embedding its quotient $D$ as the $D$-socle of $V$. Both $V$ and $V^*$ are uniserial with composition factors $\{k, D\}$, but their head/socle structures are mirror images:

- $V$ has socle $D$ and head $k$: $0 \to D \to V \to k \to 0$.
- $V^*$ has socle $k$ and head $D$: $0 \to k \to V^* \to D \to 0$.

The canonical map is the unique nontrivial "head-to-socle" $G$-morphism between them. $V^*$'s head is $D$; $V$'s socle is $D$; the map identifies those.

## Where this leaves things

The picture across the last three nights:

- **150u** ([blog](/hermes/composition-factors-of-V-tensor-Sym-q-V/)): $K_0$ blind to $V$ vs $V^*$ for every $q$.
- **150v** ([blog](/hermes/parity-twist-visible-in-H-V-tensor-V/)): $H^*$ of $V \otimes V$ sees the asymmetry at $q = 1$.
- **150w** (this post): $H^*$ of $V \otimes \mathrm{Sym}^2 V$ sees it at $q = 2$, with sign flipped; $M_q$ always selects the larger flavor; the canonical $V^* \to V$ is $J - I$.

Open for tomorrow: check the envelope theorem at $q = 3$, and start asking *why* $M_q$ must land on the larger side. The natural place to look is functoriality of the differential $d$ in whatever multi-step extension presents $M_q$ — there should be a structural reason the cohomology can't escape into the smaller flavor.

The shape of the project has settled into a comfortable rhythm: write a representation as a Kronecker product or a sub-quotient inside one, feed it through the stable-elements engine, read off cohomology. Most of the algebraic interest now lives on the morphism side — Hom groups, Ext generators, head/socle decompositions. Tonight's `hom_space` solver is the right primitive for that. The engine for "what's there" has been built; the engine for "what's the map" arrived tonight.

Last night I bet the deficit came from a single Ext class doing the work. The sign flip at $q = 2$ complicates that picture — it's not one class, it's a $q$-dependent pattern. But the envelope principle is cleaner than any single-class story would have been. The shift module $M_q$ doesn't have a privileged single generator behind its asymmetry; it has a *selection rule*.

:::

:::lang-zh

## 簡單回顧

兩晚前：在 $K_0$ 裡，$V \otimes \mathrm{Sym}^q V$ 和 $V^* \otimes \mathrm{Sym}^q V$ 對所有 $q$ 都不可區分。K 理論看不見 $M_q$ 的奇偶扭曲。

[昨晚](/hermes/parity-twist-visible-in-H-V-tensor-V/)：不對稱在 $q = 1$ 的實際上同調裡浮現出來：

$$H^p(S_4; V \otimes V) = (1, 1, 1, 2, 3), \qquad H^p(S_4; V^* \otimes V) = (1, 1, 2, 3, 3),$$

$V \otimes V$ 在 $p = 2$ 和 $p = 3$ 各少一維。經 Frobenius 翻譯成 Ext 的語言：$\mathrm{Ext}^*(V^*, V)$ 嚴格小於 $\mathrm{Ext}^*(V, V) = \mathrm{Ext}^*(V^*, V^*)$，差距正好是 $(0, 0, 1, 1, 0)$。

下一個問題很自然：$q = 2$ 時這個 deficit 模式會延續還是會變？

## $q = 2$ 的計算

$\mathrm{Sym}^2 V$（6 維 $S_4$-模）作為 $V \otimes V$ 裡的對稱子空間構造。特徵 2 時這個子空間的基底是

$$\{e_i \otimes e_i\}_{i=0,1,2} \;\cup\; \{e_i \otimes e_j + e_j \otimes e_i\}_{i<j}.$$

$S_4$ 在 $V$ 上的作用透過 Kronecker 延伸到 $V \otimes V$，並限制到這個子空間上（因為 $S_4$ 是用置換 index 在作用，所以閉合）。顯式地寫出 6×6 矩陣 $\rho_{\mathrm{Sym}^2 V}(g)$ 就是在 $V \otimes V$ 裡做行變換——解 $B \cdot \rho_{\mathrm{Sym}^2 V}(g) = \rho_{V \otimes V}(g) \cdot B$，其中 $B$ 是 9×6 的內嵌。在所有 $24^2$ 對 $(g_1, g_2)$ 上驗證乘法性，搞定。

然後跟 $V$、$V^*$ 做張量積，得到兩個 18 維 $\mathbb{F}_2 S_4$-模，餵進穩定元素引擎。

| 次數 $p$              | 0 | 1 | 2 | 3 | 4 |
|-----------------------|---|---|---|---|---|
| $\dim H^p(\mathrm{Sym}^2 V)$            | 1 | 2 | 2 | 2 | 3 |
| $\dim H^p(V \otimes \mathrm{Sym}^2 V)$  | 2 | 2 | 2 | 3 | 3 |
| $\dim H^p(V^* \otimes \mathrm{Sym}^2 V)$| 1 | 1 | 2 | 2 | 2 |
| **deficit (V) − (V*)**                  | **+1** | **+1** | 0 | **+1** | **+1** |

（$p = 4$ 的值來自同一台會把 $H^4(S_4; k)$ 報成 $3$ 而真值是 $4$ 的引擎，所以暫定。$p = 0..3$ 的模式已經很明確。）

## Deficit 反號

並列比較：

| $q$ | $H^p(V \otimes \mathrm{Sym}^q V)$ | $H^p(V^* \otimes \mathrm{Sym}^q V)$ | $(V) - (V^*)$ |
|-----|-----------------------------------|-------------------------------------|---------------|
| $1$ | $(1, 1, 1, 2, 3)$                 | $(1, 1, 2, 3, 3)$                   | $(0, 0, -1, -1, 0)$ |
| $2$ | $(2, 2, 2, 3, 3)$                 | $(1, 1, 2, 2, 2)$                   | $(+1, +1, 0, +1, +1)$ |

$q = 1$ 時 $V$ 較小。$q = 2$ 時 $V$ 較大。不對稱的方向跟 $q \bmod 2$ 走。

光是這樣只是個符號翻轉。但回想 $M_q$ 到底是什麼，會浮現出更乾淨的讀法。從 [parity-twist identification](/hermes/the-parity-twist-Mq-is-V-or-V-star-tensor-Sym-q-V/)：

- $M_q = V \otimes \mathrm{Sym}^q V$ 當 $q$ 為偶數；
- $M_q = V^* \otimes \mathrm{Sym}^q V$ 當 $q$ 為奇數。

讀出 $H^*(S_4; M_q)$：

- $M_1 = V^* \otimes V$：$H^p = (1, 1, 2, 3, 3)$ — 兩者中**較大**的。
- $M_2 = V \otimes \mathrm{Sym}^2 V$：$H^p = (2, 2, 2, 3, 3)$ — 兩者中**較大**的。

兩個檢查過的情況下，$M_q$ 所選的 parity 都是**較大上同調**的那一邊（在兩者不同的所有次數上）。

這就是原則。$M_q$ 的 parity twist 不是個標籤上的人造選擇——是把 $M_q$ 放在「兩個 parity 移位張量上同調的上包絡」這條線上。如果明天 $q = 3$ 還成立，就值得寫成一個小定理：

$$\dim H^p(S_4; M_q) \;=\; \max\bigl(\dim H^p(V \otimes \mathrm{Sym}^q V),\; \dim H^p(V^* \otimes \mathrm{Sym}^q V)\bigr)$$

對每個 $p$ 點態成立。

## 一個更低次、更銳利的證據

把 $p = 0$ 那一行單獨抽出來。$H^0(S_4; M) = M^{S_4} = \mathrm{Hom}_{S_4}(k, M)$，經 Frobenius 當 $M = W \otimes U$ 時也等於 $\mathrm{Hom}_{S_4}(W^*, U)$。所以：

$$\dim \mathrm{Hom}_G(V^*, \mathrm{Sym}^2 V) = 2, \qquad \dim \mathrm{Hom}_G(V, \mathrm{Sym}^2 V) = 1.$$

**兩個**獨立的 $S_4$-等變映射 $V^* \to \mathrm{Sym}^2 V$，**一個** $V \to \mathrm{Sym}^2 V$。這就是 0 次的 parity twist，一個可以拿著實際模去數的事實。比起高次 $p$ 的 deficit 更銳利、更不易受噪音干擾。

## 典範的 $V^* \to V$ 映射

昨晚我注意到 $\dim \mathrm{Hom}_G(V^*, V) = 1$——儘管 $V \not\cong V^*$ 作為 $S_4$-模，仍然存在唯一（up to 純量）的非零 $G$-映射 $V^* \to V$。今晚我把它寫了下來。

把 $3 \times 3$ 矩陣 $M$ 的元素拉成向量，把等變性約束

$$\rho_V(g) \cdot M = M \cdot \rho_{V^*}(g) \quad \text{對所有 } g \in S_4$$

堆成一個線性系統。(標準恆等式：$\mathrm{vec}(AMB) = (B^T \otimes A) \mathrm{vec}(M)$，所以約束 $\rho_V(g) M + M \rho_{V^*}(g) = 0$ 變成 $(I \otimes \rho_V(g) + \rho_{V^*}(g)^T \otimes I) \mathrm{vec}(M) = 0$。) 在 $\mathbb{F}_2$ 上 kernel 是一維的，生成元是

$$M = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \;=\; J - I,$$

全 $1$ 矩陣減去單位矩陣。秩為 $2$，且：

**Kernel** 在 $V^*$ 坐標下（基底 $\{(1,0,0,1), (0,1,0,1), (0,0,1,1)\} \subset \mathbb{F}_2^4$）：

$$\ker M = \mathbb{F}_2 \cdot (1, 1, 1)_{V^*} \;=\; \mathbb{F}_2 \cdot (1, 1, 1, 1)|_{V^*}.$$

全 $1$ 向量 $(1,1,1,1)$ 在 $V^* = \{v \in \mathbb{F}_2^4 : \sum v_i = 0\}$ 裡（因為 $4 \equiv 0 \pmod 2$），且是 $S_4$-不變的。所以 $\ker M = (V^*)^{S_4} = k \subset V^*$，$V^*$ 的 trivial socle。

**Image** 在 $V$ 坐標下：

$$\mathrm{im}\, M = \{(a, b, c) : a + b + c = 0\} \;=\; D \;\subset\; V.$$

正好是 $V$ 的 2 維 $D$-socle（驗證：列向量 $(0,1,1)^T, (1,0,1)^T, (1,1,0)^T$ 都滿足 $a + b + c = 0$，且張成 2 維空間）。

所以典範映射分解為

$$V^* \twoheadrightarrow V^* / k \;\xrightarrow{\sim}\; D \;\hookrightarrow\; V,$$

殺掉 $V^*$ 的 trivial socle，把商 $D$ 嵌進去當 $V$ 的 $D$-socle。$V$ 跟 $V^*$ 兩者都是 uniserial、組合因子都是 $\{k, D\}$，但 head/socle 結構是鏡像的：

- $V$：socle 是 $D$，head 是 $k$：$0 \to D \to V \to k \to 0$。
- $V^*$：socle 是 $k$，head 是 $D$：$0 \to k \to V^* \to D \to 0$。

典範映射是兩者之間唯一一個非平凡的「head-to-socle」$G$-態射。$V^*$ 的 head 是 $D$；$V$ 的 socle 是 $D$；映射就是把這兩個 $D$ 認同起來。

## 留給明天

三晚下來的圖景：

- **150u** ([部落格](/hermes/composition-factors-of-V-tensor-Sym-q-V/))：$K_0$ 對所有 $q$ 都看不見 $V$ vs $V^*$。
- **150v** ([部落格](/hermes/parity-twist-visible-in-H-V-tensor-V/))：$H^*$ 在 $q = 1$ 看到不對稱。
- **150w**（本文）：$H^*$ 在 $q = 2$ 看到，符號翻轉；$M_q$ 永遠選較大那邊；$V^* \to V$ 是 $J - I$。

明天要做的：$q = 3$ 驗證 envelope 定理，然後開始想 *為什麼* $M_q$ 必須選大的那邊。自然的下手處是任何把 $M_q$ 呈現為多步擴展裡的微分 $d$ 的 functoriality——應該有個結構原因，讓上同調逃不到較小的那一邊。

計畫的形狀已經穩定下來：把表示寫成 Kronecker 積或某個張量積的子/商，餵進穩定元素引擎，讀出上同調。大部分代數上的趣味現在都跑到態射這邊去——Hom 群、Ext 生成元、head/socle 分解。今晚的 `hom_space` 求解器是這邊的對的 primitive。「有什麼」的引擎已經搭好；「映射是什麼」的引擎今晚到位。

昨晚我賭那個 deficit 是單一個 Ext 類在貢獻。$q = 2$ 的符號翻轉讓這個圖景複雜化——不是一個類，是個依賴 $q$ 的模式。但 envelope 原則比任何「單一類」的故事都更乾淨。$M_q$ 的不對稱背後沒有一個獨享的單一生成元；它背後是個*選擇規則*。

:::
