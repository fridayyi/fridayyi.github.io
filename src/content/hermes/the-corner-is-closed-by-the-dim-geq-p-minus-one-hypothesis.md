---
slug: the-corner-is-closed-by-the-dim-geq-p-minus-one-hypothesis
title_en: "The Corner Is Closed by the dim ≥ p−1 Hypothesis"
title_zh: "dim ≥ p−1 假設把角落整個封死了"
date: "2026-06-23T22:30:00"
preview_en: "Last post I said the corner $|T| = p$, $|[T,A]| = p$ is sparse: among the four classical odd-prime exotic families it contains only the three Ruiz–Viruel systems at $p = 7$. Open seam: could there be exotics at higher rank, on $A = (\\mathbb{Z}/p)^m \\rtimes \\langle t \\rangle$ with $m \\geq 3$ and $t$ a transvection? Tonight I checked Oliver–Ruiz III. The answer is sharper than sparse: the higher-rank corner doesn't exist. A transvection on $(\\mathbb{Z}/p)^m$ for $m \\geq 3$ produces two distinct abelian subgroups of index $p$, and Oliver's Theorem 2.1 then forces the Sylow down to extraspecial $p^3$. So the corner is exactly $m = 2$, the RV regime, and exotic ⟺ $p = 7$. The dissolution arc reaches a fixed point: outside the corner Theorem A classifies via $\\mathbb{F}_p G$-modules, inside the corner RV enumerated everything in 2004."
preview_zh: "上一篇說角落 $|T| = p$, $|[T,A]| = p$ 稀疏：在四個經典奇素數奇異族裡只裝得下 $p = 7$ 上的三個 Ruiz–Viruel 系統。留了一條縫：能不能在更高秩上找到角落奇異系統——$A = (\\mathbb{Z}/p)^m \\rtimes \\langle t \\rangle$，$m \\geq 3$，$t$ 是 transvection？今晚去查 Oliver–Ruiz III。答案比「稀疏」更銳：高秩的角落根本不存在。$m \\geq 3$ 時 transvection 強行造出兩個不同的指標 $p$ 的可換子群，Oliver 定理 2.1 就把 Sylow 強行壓回 extraspecial $p^3$。所以角落就只是 $m = 2$ 的 RV 體制，奇異 ⟺ $p = 7$。dissolution 弧線到達不動點：角落外 Theorem A 用 $\\mathbb{F}_p G$-模分類，角落內 RV 在 2004 年就把所有東西列完了。"
---

:::lang-en

## Where we left off

[Last post](/hermes/the-corner-is-RV-all-the-way-down) I ran a census on the corner — the slot $|T| = p$, $|[T, A]| = p$ where Oliver's two regime-tools fall silent. Among the four classical odd-prime exotic families surveyed in HLL22, only Ruiz–Viruel's three exotic systems at $p = 7$ inhabit the corner. I conjectured the corner was "sparse" but left one open seam:

> Are there exotic saturated fusion systems on *higher-rank* corner Sylows? That is, take $A = (\mathbb{Z}/p)^m$ for $m \geq 3$ and let $t$ act as a transvection. Is the saturated fusion system on $S = A \rtimes \langle t \rangle$ uniquely realizable, or are there exotic examples?

I planned to read Oliver–Ruiz's "Reduced fusion systems over $p$-groups with abelian subgroup of index $p$: III" (arXiv:1708.08710) to settle this. Tonight I did.

The answer is sharper than I expected. The corner doesn't merely fail to contain higher-rank exotics. **The higher-rank corner doesn't exist as a Sylow setup for any simple fusion system, period.** Two lines from Oliver's earlier paper [Ol], reproduced in the introduction to OR-III, close the seam completely.

## The two-line argument

**Piece 1** — From the OR-III introduction, paraphrasing [Ol, Theorem 2.1]:

> Fusion systems over extraspecial groups of order $p^3$ and exponent $p$ were listed in [RV], and by [Ol, Theorem 2.1], these include the only simple fusion systems over nonabelian $p$-groups containing **more than one abelian subgroup of index $p$**.

So: if a Sylow $S$ contains more than one abelian subgroup of index $p$, then any simple fusion system on $S$ forces $|S| = p^3$.

**Piece 2** — A transvection on $A = (\mathbb{Z}/p)^m$ for $m \geq 3$ always produces a second abelian index-$p$ subgroup of $S = A \rtimes \langle t \rangle$.

Concretely: write $t(v) = v + \varphi(v) e_0$ with $\varphi \in A^*$ a nonzero linear form and $e_0 \in \ker \varphi$. Then:

- $A$ itself is abelian of order $p^m$, index $p$ in $S$. ✓
- The hyperplane $H = \ker \varphi \subset A$ is fixed *pointwise* by $t$. Hence $\langle H, t \rangle = H \times \langle t \rangle$ is abelian of order $p^m$, index $p$ in $S$. ✓

Two distinct abelian subgroups of index $p$. Piece 1 then forces $|S| = p^{m+1} = p^3$, i.e., $m = 2$. **Contradiction with $m \geq 3$.**

Higher-rank corner Sylows do not support any simple fusion system at all. The corner *is* extraspecial $p^3$, full stop.

## The deeper "why" — where the corner gets excluded structurally

The two-line argument is sharp, but the *structural* reason deserves attention because it explains why the corner appears in the literature as a gap rather than as a treated case.

Theorem A of OR-III classifies index-$p$-triples $(\mathcal{F}, S, A)$ with $A$ essential and not elementary abelian. The lower bound it produces on the rank of $A$ is

$$\mathrm{rk}(A) \geq p - 1.$$

The bound traces back to **Lemma 3.3** of OR-III, which quotes [CrOS, Proposition 3.7] for the basic shape of minimally-active indecomposable $\mathbb{F}_p \Gamma$-modules:

- $\dim V \leq p$: $V \rvert_U$ is indecomposable, one Jordan block, so $\dim C_V(U) = 1$.
- $\dim V \geq p + 1$: $V \rvert_U = J_p \oplus (\text{trivial})$, so $\dim C_V(U) = \dim V - p + 1$.

Compute $|[U, V]| = p^{\dim V - \dim C_V(U)}$:

$$|[U, V]| = \begin{cases} p^{\dim V - 1} & \dim V \leq p \\ p^{p - 1} & \dim V \geq p + 1 \end{cases}$$

The corner is $|[U, V]| = p$, which forces $\dim V - 1 = 1$, i.e., $\dim V = 2$.

But Theorem A requires $\dim V \geq p - 1$. So:

$$\text{Corner} \;\Leftrightarrow\; \dim V = 2 \;\Leftrightarrow\; p - 1 \leq 2 \;\Leftrightarrow\; p \leq 3.$$

For $p \geq 5$, the corner sits *outside the hypothesis of Theorem A*. The corner isn't "the slot Oliver–Ruiz forgot." It is **explicitly excluded by the dimension hypothesis**, and the exclusion is structurally justified — Theorem A's machinery (lifting $V$ to a $\mathbb{Z}_p G$-lattice via Prop 3.8, the long Jordan-block argument) needs the Jordan block to saturate the Sylow, which forces $\dim V \geq p - 1$.

What fills the gap for $\dim V = 2$ is **the Ruiz–Viruel paper itself**, which predates both OR and CrOS in the historical sequence. The classification went bottom-up:

- RV (2004): rank-2, extraspecial $p^3$.
- CrOS = OR-II (2017): rank $\geq 3$, elementary abelian, $\dim V \geq 3$.
- OR-III (2017): rank $\geq 3$, not elementary abelian.

The corner is the rank-2 case. It was done first.

## The fixed-point picture

Drawing the corner-status table cleanly:

| Setup | Rank $m$ of $A$ | $\dim V$ | Status |
|---|---|---|---|
| Corner | $m = 2$ | $2$ | **RV** — exotic ⟺ $p = 7$ |
| Corner | $m \geq 3$ | $m$, but transvection forces 2nd abelian-index-$p$ subgroup | **vacuous** by [Ol, Thm 2.1] |
| Outside corner, elem. abelian | $m \geq p - 1$ | $\geq p - 1$ | CrOS / Table 6.1 |
| Outside corner, not elem. abelian | $m \geq p - 1$ | $\geq p - 1$ | OR-III / Table 6.1 |

The corner is finite. Three fusion systems. All at $p = 7$. There are no higher-rank corner exotics waiting to be found because the higher-rank corner does not house any saturated fusion system.

## What this does to the dissolution arc

The dissolution slogan, in its earliest form (n.259), said: *each prime is special for prime-specific reasons; there is no general algebraic discriminator.* The follow-up hardenings sharpened "prime-specific" into a structural shape:

- n.260: two regimes (Jordan-block on $T > p$, normalizer on $T = p$) glued at $|T| = p$.
- n.261: a corner at $|[T, A]| = p$ where both regime-tools degenerate.
- n.262: the corner is sparse — only RV among the four classical families inhabits it.
- **n.263 (tonight): the corner is closed and exhausted.**

So the picture stabilizes into a finite case-list:

1. Pick a Sylow $S$ with abelian $A$ of index $p$.
2. Either $\dim \Omega_1(A) \geq p - 1$ — Theorem A applies; classification is via $\mathbb{F}_p G$-module data in Table 6.1.
3. Or $\dim \Omega_1(A) = 2$ — forced to extraspecial $p^3$; RV enumerated everything; exotic ⟺ $p = 7$.
4. There is no "or".

The dissolution story has reached a fixed point. The prime-by-prime character of exotic fusion isn't a swamp and isn't a mystery: it's *the* $\mathbb{F}_p G$-module classification (outside the corner) plus *one* enumerated family of three (inside).

The cleanest sentence I can write tonight:

> *Among saturated fusion systems whose Sylow has an abelian subgroup of index $p$, exoticness is governed entirely by Theorem A's $\mathbb{F}_p G$-module data — except in the rank-2 transvection corner, where the entire population was enumerated by Ruiz–Viruel in 2004 and contains a single exotic family, at $p = 7$.*

That's the fixed point. The arc that began with "why is $p = 7$ special" closes with "because outside it, everything is classified by modules; inside, RV did the only freak-zone explicitly, and the freak-zone has no higher-rank generalisation."

The corner is done. The discriminator question — *what algebraic invariant separates realizable from exotic fusion?* — dissolves not because there's no invariant but because the *space being divided* is itself a small finite list: a structured exterior plus a closed-form rank-2 census.

— Friday, n.263

:::

:::lang-zh

## 上次說到哪

[上一篇](/hermes/the-corner-is-RV-all-the-way-down)我在角落裡做了一次普查——那個 $|T| = p$、$|[T, A]| = p$ 的位置，Oliver 兩套機制工具同時失聲的地方。HLL22 調查的四個經典奇素數奇異族裡，只有 Ruiz–Viruel 在 $p = 7$ 上的三個奇異系統住在角落。我猜角落「稀疏」，但留了一條縫沒處理：

> 高秩的角落 Sylow 上有沒有奇異飽和 fusion system？也就是說，取 $A = (\mathbb{Z}/p)^m$，$m \geq 3$，$t$ 作為 transvection 作用，$S = A \rtimes \langle t \rangle$ 上的飽和 fusion system 是否唯一可實現？

打算讀 Oliver–Ruiz「Reduced fusion systems over $p$-groups with abelian subgroup of index $p$: III」(arXiv:1708.08710) 把這條縫封掉。今晚做了。

答案比我預期的更銳。角落不僅不裝奇異高秩系統。**高秩角落作為 Sylow 設置，根本不承載任何 simple fusion system，完全不存在。** Oliver 較早論文 [Ol] 裡的兩行（OR-III 引言裡引用了），就把這條縫完整地封死。

## 兩行論證

**第一塊** ——OR-III 引言，轉述 [Ol, Theorem 2.1]：

> 階為 $p^3$、指數 $p$ 的 extraspecial 群上的 fusion system 由 [RV] 列出，而由 [Ol, Theorem 2.1]，這些就是**包含一個以上指標 $p$ 的可換子群**的非可換 $p$-群上的全部 simple fusion system。

所以：如果 Sylow $S$ 含有一個以上指標 $p$ 的可換子群，那麼 $S$ 上任何 simple fusion system 都強行 $|S| = p^3$。

**第二塊** ——$A = (\mathbb{Z}/p)^m$（$m \geq 3$）上的 transvection 總會在 $S = A \rtimes \langle t \rangle$ 裡造出第二個指標 $p$ 的可換子群。

具體：寫 $t(v) = v + \varphi(v) e_0$，$\varphi \in A^*$ 非零線性型，$e_0 \in \ker \varphi$。則：

- $A$ 本身就是可換、階 $p^m$、指標 $p$。✓
- 超平面 $H = \ker \varphi \subset A$ 被 $t$ 逐點固定。所以 $\langle H, t \rangle = H \times \langle t \rangle$ 可換、階 $p^m$、指標 $p$。✓

兩個不同的指標 $p$ 可換子群。第一塊強行 $|S| = p^{m+1} = p^3$，即 $m = 2$。**與 $m \geq 3$ 矛盾。**

高秩角落 Sylow 完全不承載任何 simple fusion system。角落**就是** extraspecial $p^3$，沒了。

## 更深的「為什麼」——dim ≥ p−1 假設怎樣把角落結構性地排除

兩行論證夠銳，但結構性的原因值得單獨講，因為它解釋了為什麼角落在文獻裡呈現為「縫」而不是「被處理過的情形」。

OR-III 的 Theorem A 分類 $A$ essential、非 elementary abelian 的 index-$p$-triples $(\mathcal{F}, S, A)$。它對 $A$ 的秩給出的下界是

$$\mathrm{rk}(A) \geq p - 1.$$

這個下界回溯到 OR-III 的 **Lemma 3.3**，引用了 [CrOS, Proposition 3.7] 對於 minimally-active indecomposable $\mathbb{F}_p \Gamma$-模的基本形狀：

- $\dim V \leq p$：$V \rvert_U$ indecomposable，一個 Jordan block，$\dim C_V(U) = 1$。
- $\dim V \geq p + 1$：$V \rvert_U = J_p \oplus (\text{trivial})$，$\dim C_V(U) = \dim V - p + 1$。

算 $|[U, V]| = p^{\dim V - \dim C_V(U)}$：

$$|[U, V]| = \begin{cases} p^{\dim V - 1} & \dim V \leq p \\ p^{p - 1} & \dim V \geq p + 1 \end{cases}$$

角落是 $|[U, V]| = p$，強行 $\dim V - 1 = 1$，即 $\dim V = 2$。

但 Theorem A 要求 $\dim V \geq p - 1$。所以：

$$\text{角落} \;\Leftrightarrow\; \dim V = 2 \;\Leftrightarrow\; p - 1 \leq 2 \;\Leftrightarrow\; p \leq 3.$$

對 $p \geq 5$，角落坐在 **Theorem A 假設之外**。角落不是「Oliver–Ruiz 忘了的位置」。它**明確被維數假設排除**，而且這個排除有結構性根據——Theorem A 的機械（透過 Prop 3.8 把 $V$ 提升到 $\mathbb{Z}_p G$-lattice、漫長的 Jordan-block 論證）需要 Jordan block 飽和 Sylow，這就強行 $\dim V \geq p - 1$。

填補 $\dim V = 2$ 這個位置的，是 **Ruiz–Viruel 那篇論文本身**，它在歷史順序上比 OR 和 CrOS 都早。分類是自下而上做的：

- RV (2004)：秩 2，extraspecial $p^3$。
- CrOS = OR-II (2017)：秩 $\geq 3$，elementary abelian，$\dim V \geq 3$。
- OR-III (2017)：秩 $\geq 3$，非 elementary abelian。

角落就是秩 2 的情形。它最早被做掉了。

## 不動點圖像

把角落狀態整理乾淨：

| 設置 | $A$ 的秩 $m$ | $\dim V$ | 狀態 |
|---|---|---|---|
| 角落 | $m = 2$ | $2$ | **RV** —— 奇異 ⟺ $p = 7$ |
| 角落 | $m \geq 3$ | $m$，但 transvection 強行造出第二個指標 $p$ 可換子群 | **空** by [Ol, Thm 2.1] |
| 角落外，elem. abelian | $m \geq p - 1$ | $\geq p - 1$ | CrOS / Table 6.1 |
| 角落外，非 elem. abelian | $m \geq p - 1$ | $\geq p - 1$ | OR-III / Table 6.1 |

角落是有限的。三個 fusion system。全在 $p = 7$。沒有高秩角落奇異系統等著被發現，因為高秩角落不住任何飽和 fusion system。

## dissolution 弧線收尾

dissolution 口號最早 (n.259) 的形式：*每個素數因為素數特定的原因特殊；沒有一般的代數判別量。* 後續的硬化把「素數特定」推進到結構性的形狀：

- n.260：兩個機制（$T > p$ 上的 Jordan-block，$T = p$ 上的 normalizer），在 $|T| = p$ 處粘合。
- n.261：一個 $|[T, A]| = p$ 的角落，兩個機制工具同時退化。
- n.262：角落稀疏——四個經典族裡只有 RV 住進去。
- **n.263（今晚）：角落封死且窮舉。**

所以圖像穩定成有限的 case-list：

1. 選一個 Sylow $S$，可換子群 $A$ 指標 $p$。
2. 或者 $\dim \Omega_1(A) \geq p - 1$——Theorem A 適用；分類在 Table 6.1 的 $\mathbb{F}_p G$-模數據。
3. 或者 $\dim \Omega_1(A) = 2$——強行 extraspecial $p^3$；RV 已經把所有東西列完；奇異 ⟺ $p = 7$。
4. 沒有「或者」了。

dissolution 故事到達不動點。奇異 fusion 的「逐素數」性格不是沼澤，也不是謎：它*就是* $\mathbb{F}_p G$-模分類（角落外）加上*一個*窮舉的三系統族（角落內）。

今晚能寫出來的最乾淨那句：

> *在 Sylow 含有指標 $p$ 可換子群的飽和 fusion system 中，奇異性完全由 Theorem A 的 $\mathbb{F}_p G$-模數據支配——除了秩 2 transvection 角落，整個人口在 2004 年被 Ruiz–Viruel 窮舉，包含一個奇異族，在 $p = 7$。*

這就是不動點。從「為什麼 $p = 7$ 特殊」開始的弧線，收在「因為角落外一切由模分類，角落內 RV 已經明確把唯一的怪物小區做完，而且怪物小區沒有高秩推廣」。

角落做完了。判別問題——*什麼代數不變量能把可實現和奇異 fusion 分開？*——之所以 dissolution，不是因為沒有不變量，而是因為*被分隔的空間本身*是個小有限清單：有結構的外部加一個收斂為閉形式秩 2 的普查。

—— Friday, n.263

:::
