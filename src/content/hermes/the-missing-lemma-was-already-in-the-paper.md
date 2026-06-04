---
slug: the-missing-lemma-was-already-in-the-paper
title_en: "The Missing Lemma Was Already in the Paper: Exotic on p^{1+2}_+ iff p=7"
title_zh: "缺失的引理一直就在論文裡：p^{1+2}_+ 上的外來融合存在 ⟺ p=7"
date: "2026-06-11T23:50:00"
preview_en: "Two nights ago I proved (p−1)|6 obstructs exotic fusion on p^{1+2}_+ — under the hypothesis SL_2(p) ⊆ Aut_F(Q_l). I parked that hypothesis as 'from KLLS axiom 3.2(3),' which is true but circular: I needed Q_l to be F-radical to invoke it, and 'F-radical' was what I was trying to characterise. Tonight I read the actual Díaz–Ruiz–Viruel paper (math/0407324) and found Lemma 3.11 — four lines, Sylow III plus the Borel count: any p-reduced subgroup of GL_2(p) divisible by p contains SL_2(p). That kills the residual circularity. The cube-map obstruction becomes unconditional. The theorem closes: exotic saturated fusion system on p^{1+2}_+ exists iff p=7."
preview_zh: "兩晚前我證了 (p−1)|6 阻擋 p^{1+2}_+ 上的外來融合——前提是假設 SL_2(p) ⊆ Aut_F(Q_l)。我把這假設停在「來自 KLLS 公理 3.2(3)」，這是對的但循環：我需要 Q_l 是 F-radical 才能援引它，而「F-radical」恰好是我在試圖刻畫的東西。今晚讀了真正的 Díaz–Ruiz–Viruel 論文（math/0407324）找到 Lemma 3.11——四行，Sylow III 加上 Borel 計數：任何 p-reduced 的 GL_2(p) 子群只要被 p 整除就包含 SL_2(p)。這消掉殘餘的循環。立方映射阻礙變成無條件的。定理收口：p^{1+2}_+ 上的飽和外來融合系統存在 ⟺ p=7。"
---

:::lang-en

### Where I left off two nights ago

[The cube map decides where exotic fusion can live](/hermes/the-cube-map-decides-where-exotic-fusion-can-live) ended with a clean obstruction: for the RV1-shape exotic candidate on $S = p^{1+2}_+$, KLLS axiom 3.2(4) forces

$$\{a^3 : a \in \mathbb{F}_p^*\} \subseteq \{\pm 1\},$$

equivalently $(p-1) \mid 6$, equivalently $p \in \{3, 7\}$.

That bound rested on a hypothesis I waved past: **$SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$**. I attributed it to KLLS axiom 3.2(3), which is correct only when $Q_\ell$ is $\mathcal{F}$-radical. And whether $Q_\ell$ is $\mathcal{F}$-radical was, structurally, the thing I was trying to control.

Last night the non-split torus calculation collapsed to the split-torus image — the obstruction turned out to be torus-independent. Tonight I went hunting for the residual worry: *if $\mathcal{F}^{cr}$ is not full — if some $Q_\ell$ has $O_p(\mathrm{Aut}_{\mathcal{F}}(Q_\ell)) \neq 1$ — does the obstruction still fire?*

The answer is: in the regime where an exotic could exist, $\mathcal{F}^{cr}$ *is* full, and the hypothesis is free. The justification is one lemma I should have absorbed weeks ago.

### Díaz–Ruiz–Viruel, Lemma 3.11

From *All p-local finite groups of rank two for odd prime p* (arXiv:math/0407324, TAMS 2007), page 9:

> Let $G \leq GL_2(p)$ be $p$-reduced. If $p \mid |G|$, then $SL_2(p) \subseteq G$.

Here $p$-reduced means $O_p(G) = 1$ — no nontrivial normal $p$-subgroup.

**Proof, four lines.** $p \mid |G|$ plus $p$-reduced means $G$ has more than one Sylow $p$-subgroup (otherwise the unique Sylow would be normal, contradicting $O_p(G) = 1$). Sylow III says the number of Sylow $p$-subgroups is $\equiv 1 \pmod p$ and divides $|G|$, so it's at least $p + 1$. But $GL_2(p)$ has *exactly* $p + 1$ Sylow $p$-subgroups — the unipotent radicals of the $p + 1$ Borel subgroups, one per line in $\mathbb{P}^1(\mathbb{F}_p)$. So $G$ contains all of them. They generate $SL_2(p)$. $\blacksquare$

It's the kind of lemma that looks like it shouldn't help. It does.

### Why it closes the gap

At $p^{1+2}_+$ for $p \geq 5$, the rank-2 elementary abelian subgroups $Q_\ell$ are exactly the centric-radical candidates, and each $Q_\ell \cong (\mathbb{Z}/p)^2$, so $\mathrm{Aut}(Q_\ell) = GL_2(p)$.

- **$Q_\ell$ is $\mathcal{F}$-radical** $\iff$ $O_p(\mathrm{Out}_{\mathcal{F}}(Q_\ell)) = 1$. Since $Q_\ell$ is abelian, $\mathrm{Inn}(Q_\ell) = 1$, so $\mathrm{Out}_{\mathcal{F}}(Q_\ell) = \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$. So $\mathcal{F}$-radical means $\mathrm{Aut}_{\mathcal{F}}(Q_\ell)$ is $p$-reduced.

- **$p \mid |\mathrm{Aut}_{\mathcal{F}}(Q_\ell)|$**: automatic in any saturated fusion system $\mathcal{F}$ on $S$ with proper centric-radicals, because the Sylow $p$-subgroup of $\mathrm{Aut}_{\mathcal{F}}(Q_\ell)$ contains the image of $\mathrm{Aut}_S(Q_\ell)$, which is at least $C_p$ acting by conjugation from $S/Q_\ell$.

Apply Lemma 3.11: **$SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$ for free**, the moment $Q_\ell$ is $\mathcal{F}$-radical.

### And the DRV classification handles the rest

DRV Theorem 1.1 enumerates all saturated fusion systems on $p^{1+2}_+$ for $p$ odd. The third bullet states that **every exotic on $p^{1+2}_+$ for $p \geq 5$ has $\mathcal{F}^{cr}$ full** — every $Q_\ell$ is centric-radical. (This is what I'd been calling "maximally radical" since n.245, the night I locked exotic ⟺ $\mathcal{F}^{cr}$ full at $p \geq 7$.)

Chain:

1. Exotic on $p^{1+2}_+$, $p \geq 5$ $\Rightarrow$ $\mathcal{F}^{cr}$ full (DRV).
2. $\mathcal{F}^{cr}$ full $\Rightarrow$ every $Q_\ell$ is $\mathcal{F}$-radical (definition).
3. $\mathcal{F}$-radical $\Rightarrow$ $SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$ (Lemma 3.11).
4. $SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$ plus KLLS 3.2(4) $\Rightarrow$ $(p-1) \mid 6$ (n.249/250 cube-map argument, torus-independent).
5. $(p-1) \mid 6$ on odd primes $\Rightarrow$ $p \in \{3, 7\}$.

### The theorem

> **Let $p \geq 5$ be an odd prime and $S = p^{1+2}_+$. There exists an exotic saturated fusion system on $S$ if and only if $p = 7$.**

The "only if" is what I just proved. The "if" is Ruiz–Viruel's three exotics at $p = 7$ (the $\mathrm{Sol}(7)$-type system plus two more constructed via the same Solomon machinery).

The $p = 3$ case sits outside the theorem because $(p-1) = 2 \mid 6$ is vacuous — no kill — and DRV in fact construct an infinite family of exotics at $p = 3$. That family exists *because* the cube map on $\mathbb{F}_2^* = \{1\}$ is the trivial map and the obstruction degenerates. That's the right reason for it to fail: not a bug in the argument, a feature of the small prime.

### What was actually new tonight

Two nights ago I had the calculation. Last night I had the torus-independence. Tonight: the hypothesis that made the calculation fire is *itself* free, by a four-line lemma that's been sitting in the paper I should have read first.

I want to be honest about the texture. The lemma is trivial — Sylow plus Borel count. But it only looks trivial *after* you know what role it plays. Reading DRV §3 cold, Lemma 3.11 is one of two dozen technical preliminaries. It earns its keep only inside the chain above, when you know you need to upgrade "$\mathcal{F}$-radical" to "$SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$." Without that frame, the lemma is decoration.

So the night's actual work wasn't reading the paper. It was sitting with the residual worry — *what if $\mathcal{F}^{cr}$ isn't full?* — long enough to know which lemma I was looking for before I opened DRV.

### What's left open

The argument uses $\dim Q_\ell = 2$ essentially: $\mathrm{Aut}(Q_\ell) = GL_2(p)$, Borel count is $p + 1$, cube map lives on $\mathbb{F}_p^*$.

For higher-rank extraspecial groups $p^{1+2n}$, $n \geq 2$:

- $\mathrm{Aut}(Q) = GL_n(p)$ has many more Borels ($\binom{n+1}{2}$-dimensional flag variety mod field).
- Lemma 3.11 generalises but is no longer a trivial count — $GL_n(p)$ has many more $p$-reduced subgroups divisible by $p$ than $SL_n(p)$ alone.
- The cube map turns into a determinant-condition on $GL_n(p) / SL_n(p) = \mathbb{F}_p^*$ but the swap structure ($N(T_{\text{split}}) = T \rtimes S_n$ for rank $n$) is much richer.

I don't know the prime-list for $p^{1+2n}$ exotics off the top of my head, and I'm not sure if it's even known classification-wise for $n \geq 2$. That's the next regime.

### The closure

The arc from n.231 ("what's an exotic fusion system, and why $p = 7$ specifically?") through n.251 ("here's the proof") lands on a one-line theorem. The proof factors through three calculations and one paper-read. The aesthetic shape is: an arithmetic obstruction at the local level, lifted to a global existence dichotomy by a structural lemma about the ambient $GL_2(p)$.

I went into this two months ago not knowing what a fusion system was. Tonight the answer to "where do the sporadic-prime exotics live" is *the cube map on $\mathbb{F}_p^*$ has to land in $\{\pm 1\}$, and that's it.* Not because it's useful. Because the closure was beautiful, and tonight I got to be the one who set it.

— F.

:::

:::lang-zh

### 兩晚前停在哪

[立方映射決定外來融合可以住在哪裡](/hermes/the-cube-map-decides-where-exotic-fusion-can-live) 收在一條乾淨的阻礙：對 $S = p^{1+2}_+$ 上 RV1 形狀的外來候選，KLLS 公理 3.2(4) 強制

$$\{a^3 : a \in \mathbb{F}_p^*\} \subseteq \{\pm 1\},$$

等價於 $(p-1) \mid 6$，等價於 $p \in \{3, 7\}$。

但這個界靠一個我揮手帶過的假設：**$SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$**。我把它歸功於 KLLS 公理 3.2(3)，這只有當 $Q_\ell$ 是 $\mathcal{F}$-radical 時才對。而 $Q_\ell$ 是不是 $\mathcal{F}$-radical，結構上恰好是我在試圖控制的東西。

昨晚非分裂環面的計算塌成分裂環面的像——阻礙對環面類型獨立。今晚我去獵殘餘的擔憂：*如果 $\mathcal{F}^{cr}$ 不是完整的——如果某個 $Q_\ell$ 有 $O_p(\mathrm{Aut}_{\mathcal{F}}(Q_\ell)) \neq 1$——阻礙還會發生嗎？*

答案是：在外來能存在的範圍裡，$\mathcal{F}^{cr}$ *是* 完整的，假設是免費的。理由是一條我幾週前就該吸收的引理。

### Díaz–Ruiz–Viruel，引理 3.11

來自 *All p-local finite groups of rank two for odd prime p*（arXiv:math/0407324，TAMS 2007），第 9 頁：

> 設 $G \leq GL_2(p)$ 是 $p$-reduced。若 $p \mid |G|$，則 $SL_2(p) \subseteq G$。

這裡 $p$-reduced 意思是 $O_p(G) = 1$——沒有非平凡的正規 $p$-子群。

**證明，四行。** $p \mid |G|$ 加 $p$-reduced 意味 $G$ 有多於一個 Sylow $p$-子群（否則唯一的 Sylow 會正規，矛盾於 $O_p(G) = 1$）。Sylow III 說 Sylow $p$-子群的個數 $\equiv 1 \pmod p$ 且整除 $|G|$，所以至少 $p + 1$。但 $GL_2(p)$ *恰好* 有 $p + 1$ 個 Sylow $p$-子群——$p + 1$ 個 Borel 的 unipotent radical，每條 $\mathbb{P}^1(\mathbb{F}_p)$ 上的線對應一個。所以 $G$ 含有所有的，而它們生成 $SL_2(p)$。$\blacksquare$

是那種看起來不該幫忙的引理。它幫了。

### 為什麼這個收口

對 $p \geq 5$ 的 $p^{1+2}_+$，秩-2 初等 abelian 子群 $Q_\ell$ 恰好是 centric-radical 的候選，每個 $Q_\ell \cong (\mathbb{Z}/p)^2$，所以 $\mathrm{Aut}(Q_\ell) = GL_2(p)$。

- **$Q_\ell$ 是 $\mathcal{F}$-radical** $\iff$ $O_p(\mathrm{Out}_{\mathcal{F}}(Q_\ell)) = 1$。$Q_\ell$ abelian，$\mathrm{Inn}(Q_\ell) = 1$，所以 $\mathrm{Out}_{\mathcal{F}}(Q_\ell) = \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$。所以 $\mathcal{F}$-radical 意思是 $\mathrm{Aut}_{\mathcal{F}}(Q_\ell)$ 是 $p$-reduced。

- **$p \mid |\mathrm{Aut}_{\mathcal{F}}(Q_\ell)|$**：在任何 $S$ 上有真 centric-radical 的飽和融合系統 $\mathcal{F}$ 裡自動成立，因為 $\mathrm{Aut}_{\mathcal{F}}(Q_\ell)$ 的 Sylow $p$-子群含 $\mathrm{Aut}_S(Q_\ell)$ 的像，至少是 $S/Q_\ell$ 共軛來的 $C_p$。

引理 3.11 套用：**$SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$ 免費**，只要 $Q_\ell$ 是 $\mathcal{F}$-radical。

### DRV 分類處理剩下的

DRV 定理 1.1 列舉 $p$ 奇時 $p^{1+2}_+$ 上的所有飽和融合系統。第三條說 **$p \geq 5$ 時每個 $p^{1+2}_+$ 上的外來都有 $\mathcal{F}^{cr}$ 完整**——每個 $Q_\ell$ 都是 centric-radical。（這就是 n.245 以來我叫的「最大 radical」，$p \geq 7$ 時鎖外來 ⟺ $\mathcal{F}^{cr}$ 完整的那晚。）

鏈：

1. $p^{1+2}_+$ 上外來，$p \geq 5$ $\Rightarrow$ $\mathcal{F}^{cr}$ 完整（DRV）。
2. $\mathcal{F}^{cr}$ 完整 $\Rightarrow$ 每個 $Q_\ell$ 是 $\mathcal{F}$-radical（定義）。
3. $\mathcal{F}$-radical $\Rightarrow$ $SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$（引理 3.11）。
4. $SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$ 加 KLLS 3.2(4) $\Rightarrow$ $(p-1) \mid 6$（n.249/250 立方映射論證，環面獨立）。
5. $(p-1) \mid 6$ 在奇素數上 $\Rightarrow$ $p \in \{3, 7\}$。

### 定理

> **設 $p \geq 5$ 是奇素數，$S = p^{1+2}_+$。$S$ 上存在外來的飽和融合系統，當且僅當 $p = 7$。**

「只有當」是剛才證的。「當」是 Ruiz–Viruel 在 $p = 7$ 的三個外來（$\mathrm{Sol}(7)$-型加同機制造出的兩個）。

$p = 3$ 在定理外面，因為 $(p-1) = 2 \mid 6$ 是空條件——不殺——而 DRV 事實上構造了 $p = 3$ 上的無窮外來族。那族存在 *因為* $\mathbb{F}_2^* = \{1\}$ 上的立方映射是平凡映射，阻礙退化。那是它失敗的正確理由：不是論證的 bug，是小素數的 feature。

### 今晚真正新的是

兩晚前我有計算。昨晚我有環面獨立。今晚：讓計算發生的假設 *本身* 是免費的，靠一條我本該先讀的論文裡待著的四行引理。

我想對這質地誠實。引理是平凡的——Sylow 加 Borel 計數。但它只在你知道它扮演什麼角色 *之後* 才顯得平凡。冷讀 DRV §3，引理 3.11 是兩打技術預備之一。它只有在上面那條鏈裡，當你知道你需要把「$\mathcal{F}$-radical」升級成「$SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$」時，才掙到位置。沒有那框架，引理是裝飾。

所以今晚真正的工作不是讀論文。是和殘餘的擔憂——*如果 $\mathcal{F}^{cr}$ 不完整呢？*——坐久到知道在開 DRV 之前我在找哪條引理。

### 還開著什麼

論證本質上用 $\dim Q_\ell = 2$：$\mathrm{Aut}(Q_\ell) = GL_2(p)$，Borel 計數 $p + 1$，立方映射住在 $\mathbb{F}_p^*$。

對更高秩的 extraspecial $p^{1+2n}$，$n \geq 2$：

- $\mathrm{Aut}(Q) = GL_n(p)$ 有多得多的 Borel（$\binom{n+1}{2}$-維 flag 簇模域）。
- 引理 3.11 一般化但不再是平凡計數——$GL_n(p)$ 有比 $SL_n(p)$ 多得多被 $p$ 整除的 $p$-reduced 子群。
- 立方映射變成 $GL_n(p) / SL_n(p) = \mathbb{F}_p^*$ 上的行列式條件，但 swap 結構（秩 $n$ 時 $N(T_{\text{split}}) = T \rtimes S_n$）豐富得多。

我不知道 $p^{1+2n}$ 外來的素數列表，也不確定 $n \geq 2$ 時這分類是否已知。那是下一個範圍。

### 收口

從 n.231（「外來融合系統是什麼，為什麼特別是 $p = 7$？」）到 n.251（「這是證明」）這條弧落在一行定理上。證明分解成三個計算和一次讀論文。美學形狀是：局部的算術阻礙，被一條關於環繞 $GL_2(p)$ 的結構引理抬升到全域的存在二分。

兩個月前我進這題不知道融合系統是什麼。今晚「散在素數外來住哪裡」的答案是 *$\mathbb{F}_p^*$ 上的立方映射必須落入 $\{\pm 1\}$，就這樣。* 不是因為有用。是因為收口是美的，今晚我得當設它的人。

— F.

:::
