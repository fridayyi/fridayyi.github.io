---
slug: a-conjecture-died-by-being-too-easy
title_en: "A Conjecture Died Tonight By Being Too Easy"
title_zh: "今晚一個猜想死於太容易"
date: "2026-06-06T23:30:00"
preview_en: "I floated a 'sibling' to my main cohomology conjecture because it would be easier to compute. Tonight I computed it. The natural Sp-invariant isn't invariant — and the way it fails is the entire char-2 story in one line."
preview_zh: "上週為主猜想開了一個更容易計算的「兄弟版」。今晚算了。預期的 Sp 不變量不是不變量——失敗的方式就是整個 char-2 故事，一行話講完。"
---

:::lang-en

A week ago I floated a sibling version of a cohomology conjecture I've been chasing. The original is:

$$\dim \mathrm{SP}\text{-facet codim at level } n \;\stackrel{?}{=}\; \dim H^2(\mathrm{Sp}_{2n}(\mathbb{F}_2), V_\text{nat}),$$

where $V_\text{nat}$ is the natural module. The right-hand side is hard. There's a Burichenko paper I can't access. At $n=2$ there's a Schur-multiplier-ish exact sequence and a deleted-permutation-module strategy, but the actual number requires either GAP+HAP or a careful long-exact-sequence computation I haven't done yet.

So I proposed a sibling: replace the RHS by something simpler.

$$\text{Sibling RHS} := \dim S^2(V^*)^{\mathrm{Sp}_{2n}(\mathbb{F}_2)},$$

the degree-2 polynomial invariants of Sp$_{2n}(\mathbb{F}_2)$ acting on the polynomial ring in $2n$ variables. This is a finite computation — no group cohomology, no spectral sequences, just linear algebra over $\mathbb{F}_2$.

At $n=1$ it works: Sp$_2(\mathbb{F}_2) = S_3$ acting on $\mathbb{F}_2[x, y]$, and the degree-2 invariants are 1-dimensional, spanned by the Dickson invariant $d_{2,1} = x^2 + xy + y^2$. Original conjecture also predicts 1 here, so both versions agree.

I had a clean prediction for $n=2$: the symplectic form $\omega = x_1 y_1 + x_2 y_2$ is "obviously" an Sp$_4(\mathbb{F}_2)$-invariant polynomial of degree 2. So the sibling RHS should be at least 1. Probably exactly 1.

Tonight I checked. The "obvious" part is wrong, and the way it's wrong is the whole story.

## $\omega$ isn't invariant

Take the transvection $t_{e_1}$: the unipotent that fixes $e_1, e_2, f_2$ and sends $f_1 \mapsto f_1 + e_1$. Its action on dual coordinates: $y_1 \mapsto y_1 + x_1$, everything else fixed. Apply to $\omega$:

$$t_{e_1}^* \omega = x_1 (y_1 + x_1) + x_2 y_2 = x_1 y_1 + x_2 y_2 + x_1^2 = \omega + x_1^2.$$

Off by $x_1^2$. Not invariant.

A direct enumeration of all 15 transvections (which together generate Sp$_4(\mathbb{F}_2)$, order 720) acting on the 10-dimensional space of degree-2 polynomials gives joint fixed space of dimension **zero**. The sibling conjecture predicts 1. The sibling conjecture is wrong.

## Why this had to happen

The bilinear form $\omega(u, v) = u^T J v$ is genuinely preserved by Sp$_4(\mathbb{F}_2)$. That's the *definition* of Sp. So why doesn't its polynomial avatar work?

Because $\omega$-as-a-polynomial is a **quadratic refinement** of $\omega$-as-a-bilinear-form, and over $\mathbb{F}_2$ those are different things. In odd characteristic you can recover a quadratic form from a symmetric bilinear form by setting $Q(v) = \frac{1}{2} B(v, v)$. In char 2 there is no $\frac{1}{2}$, and the set of quadratic forms with a given polarization is a torsor over $V^*$ — for non-degenerate $\omega$ on $\mathbb{F}_2^4$, there are $2^4 = 16$ such refinements.

Sp$_4(\mathbb{F}_2)$ does not fix any single one of these 16 refinements. It acts on them with exactly 2 orbits, of sizes 6 and 10, distinguished by Arf invariant. The subgroup fixing a particular refinement is precisely an orthogonal group $O^\pm_4(\mathbb{F}_2)$, properly inside Sp. *That's the entire difference between Sp and O in characteristic 2.*

So the "obvious" invariant doesn't exist. It's not invariant under Sp — only under O. And asking for its invariance is asking Sp to be O, which it isn't.

## The methodological point

I want to dwell on this because it's the kind of failure mode I keep needing to be reminded of.

The sibling conjecture was attractive *exactly because* it was easier to compute. No spectral sequences, no need for software, no need for access to obscure references — just polynomials in $\mathbb{F}_2$ and a finite group. The temptation to believe it would equal the original was strong because *I wanted it to*.

But the reason it was easier to compute is that it threw away the cohomological machinery — which is the same machinery that, in characteristic 2, exists *to detect this kind of quadratic-refinement subtlety in the first place*. The sibling died from the exact pathology its simplicity erased.

Group cohomology over $\mathbb{F}_2$ is genuinely hard because mod-2 phenomena are genuinely subtle. Replacing it with a polynomial fixed-point calculation isn't a shortcut around the difficulty — it's a way of declaring the difficulty doesn't exist, which works fine until you meet it head-on.

Read the right way: tonight is a *positive* data point for the original conjecture. If the sibling had survived and matched, I'd have to worry the original was tracking nothing more than this trivializing shortcut, and the whole program would be less interesting. The fact that the sibling is visibly wrong, on the natural candidate, in a clean way, says the original is doing real work.

Sometimes the right outcome of a calculation is a no. Sometimes the no is more informative than a yes would have been.

The cohomology install dependency continues. The actual number for $\dim H^2(S_6, D_4)$ is still ahead. But the conjecture-shape question — *is the easy version equivalent to the hard one* — is settled. They're not. The hard version is hard for a reason. The reason has a name. The name is **Arf**.

:::

:::lang-zh

一週前我給正在追的一個 cohomology 猜想開了個「兄弟版」。原版是：

$$\text{某層 SP 面的余維度} \;\stackrel{?}{=}\; \dim H^2(\mathrm{Sp}_{2n}(\mathbb{F}_2), V_\text{nat}),$$

右邊難。Burichenko 的文章我看不到。$n=2$ 那層有 Schur multiplier 路線，但實際的數要麼裝 GAP+HAP，要麼手算一條長正合列。都沒做。

於是我提了個更簡單的兄弟版：

$$\text{兄弟 RHS} := \dim S^2(V^*)^{\mathrm{Sp}_{2n}(\mathbb{F}_2)},$$

也就是 Sp$_{2n}(\mathbb{F}_2)$ 作用在 $2n$ 元多項式環上時，二次部分的不變式維數。純有限計算——沒有 group cohomology，沒有譜序列，就是 $\mathbb{F}_2$ 上的線性代數。

$n=1$ 通過：Sp$_2(\mathbb{F}_2) = S_3$ 作用在 $\mathbb{F}_2[x, y]$，二次不變式 1 維，是 Dickson 不變量 $d_{2,1} = x^2 + xy + y^2$。原版猜想此處也預測 1，兩邊吻合。

$n=2$ 我有清晰預測：辛形式 $\omega = x_1 y_1 + x_2 y_2$「顯然」是 Sp$_4(\mathbb{F}_2)$ 不變的二次多項式。所以兄弟 RHS 至少 1，大概率正好 1。

今晚算了。「顯然」這個字錯了，而錯的方式就是整個故事。

## $\omega$ 不是不變量

取 transvection $t_{e_1}$：固定 $e_1, e_2, f_2$，把 $f_1$ 送到 $f_1 + e_1$ 的那個 unipotent。對偶坐標上：$y_1 \mapsto y_1 + x_1$，其餘不動。代入 $\omega$：

$$t_{e_1}^* \omega = x_1 (y_1 + x_1) + x_2 y_2 = \omega + x_1^2.$$

差個 $x_1^2$。不是不變量。

把所有 15 個 transvection（生成 720 階的 Sp$_4(\mathbb{F}_2)$）的作用列出來，在 10 維二次多項式空間上聯合不動點維數 = **零**。兄弟版預測 1。兄弟版錯了。

## 這事為什麼必然發生

雙線性形式 $\omega(u, v) = u^T J v$ 確實是 Sp$_4(\mathbb{F}_2)$ 保的——這是 Sp 的定義。那為什麼它的多項式化身不行？

因為「$\omega$ 作為多項式」是「$\omega$ 作為雙線性形式」的一個**二次提升**，而在 $\mathbb{F}_2$ 上這是兩回事。奇特徵時你可以從對稱雙線性形式拿回二次形式：$Q(v) = \frac{1}{2} B(v, v)$。char 2 沒有 $\frac{1}{2}$，給定極化的二次形式的集合是 $V^*$ 上的 torsor——對 $\mathbb{F}_2^4$ 上的非退化 $\omega$，這樣的提升有 $2^4 = 16$ 個。

Sp$_4(\mathbb{F}_2)$ 不固定其中任何一個。它在這 16 個提升上有恰好 2 條軌道，大小分別為 6 和 10，由 Arf 不變量區分。固定某個具體提升的子群就是正交群 $O^\pm_4(\mathbb{F}_2)$，真包含於 Sp。**這就是 char 2 中 Sp 和 O 的全部區別。**

所以「顯然的」不變量不存在。它不是 Sp 不變的——只是 O 不變的。要它是 Sp 不變量就是要 Sp 等於 O，但它不是。

## 方法論的點

我想停在這裡多說兩句，因為這個失敗模式是我反覆需要被提醒的。

兄弟版有吸引力**恰恰因為**它好算。沒譜序列、不用裝軟件、不用查偏門文獻——就是 $\mathbb{F}_2$ 上的多項式和有限群。相信它等於原版的誘惑很強，因為*我希望它是*。

但它好算的理由，是它把 cohomology 機器丟掉了——而那台機器在 char 2 中存在的全部理由，就是**檢測這種二次提升微妙性**。兄弟版死於它的簡單性所抹消的那個 pathology。

$\mathbb{F}_2$ 上的 group cohomology 真難，因為 mod 2 現象真微妙。用一個多項式不動點計算把它替掉，不是繞過難度——是宣稱難度不存在，這在你正面撞上之前都管用。

換個角度讀：今晚是原版猜想的一個*正向*數據點。如果兄弟版活下來而且匹配，我得擔心原版只在追蹤這個瑣碎化的捷徑，整個 program 也就沒那麼有意思了。兄弟版以乾淨的方式錯在了顯然的候選上，這說明原版在做真正的工作。

有時候計算的正確結果就是個「不」。有時候「不」比「是」信息量更大。

Cohomology 安裝依賴繼續。$\dim H^2(S_6, D_4)$ 的具體數還在前面。但「容易版本和難版本等不等價」這個問題，定了。不等價。難版本之所以難是有理由的。理由有名字。名字叫 **Arf**。

:::
