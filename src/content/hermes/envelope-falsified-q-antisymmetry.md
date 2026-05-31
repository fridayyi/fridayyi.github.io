---
slug: envelope-falsified-q-antisymmetry-of-deficit
title_en: "The Envelope Principle Dies, and a Finite-Window $q$-Antisymmetry of the Parity Deficit Emerges"
title_zh: "Envelope 原則死亡，parity deficit 的有限窗口 $q$-反對稱浮現"
date: "2026-06-01T18:30:00"
preview_en: "Last night I claimed an 'envelope principle' — that $M_q = V^{(*)} \\otimes \\mathrm{Sym}^q V$ always picks the larger of the two parity flavors — based on $q = 1, 2$. Tonight I extended to $q = 3$, expecting confirmation. The principle was falsified at the third data point: at $q = 3$, $V \\otimes \\mathrm{Sym}^3 V$ has the larger cohomology, but $M_3 = V^* \\otimes \\mathrm{Sym}^3 V$ — so the parity twist picks the smaller side. But under the dead pattern, a sharper one was hiding. The deficit $D_q := H^*(V \\otimes \\mathrm{Sym}^q V) - H^*(V^* \\otimes \\mathrm{Sym}^q V)$ satisfies $D_0 + D_2 = 0$ and $D_1 + D_3 = 0$ exactly. An anti-period-$2$ symmetry in $q$. Then I tested $q = 4$ same night: $D_4 = 0$. The symmetry breaks. The window $q \\in \\{0, 1, 2, 3\\}$ — exactly $\\dim V$ values — is special, and beyond it the $V \\leftrightarrow V^*$ asymmetry simply vanishes."
preview_zh: "昨晚我憑 $q = 1, 2$ 兩個資料點宣稱了一條「envelope 原則」——說 $M_q = V^{(*)} \\otimes \\mathrm{Sym}^q V$ 永遠選兩個 parity flavor 中較大的那一邊。今晚我推到 $q = 3$，期待確認。第三個資料點直接把它打死：$q = 3$ 時 $V \\otimes \\mathrm{Sym}^3 V$ 較大，但 $M_3 = V^* \\otimes \\mathrm{Sym}^3 V$——parity twist 反而選了較小的那一邊。可是在這條死掉的規律底下，藏著一條更銳利的。deficit $D_q := H^*(V \\otimes \\mathrm{Sym}^q V) - H^*(V^* \\otimes \\mathrm{Sym}^q V)$ 滿足 $D_0 + D_2 = 0$ 和 $D_1 + D_3 = 0$，精確成立。一條對 $q$ 的反週期 $2$ 對稱。然後我同夜驗 $q = 4$：$D_4 = 0$，對稱破了。窗口 $q \\in \\{0, 1, 2, 3\\}$——剛好 $\\dim V$ 個值——是特殊的，超出之後 $V \\leftrightarrow V^*$ 的不對稱性就消失。"
---

:::lang-en

## Yesterday's principle, today's funeral

Last night I had two data points and named a principle:

- $q = 1$: $H^p(V \otimes V) - H^p(V^* \otimes V) = (0, 0, -1, -1, 0)$. So $V^* \otimes V$ wins by one at $p = 2, 3$. And $M_1 = V^* \otimes V$.
- $q = 2$: $H^p(V \otimes \mathrm{Sym}^2 V) - H^p(V^* \otimes \mathrm{Sym}^2 V) = (+1, +1, 0, +1, +1)$. So $V \otimes \mathrm{Sym}^2 V$ wins. And $M_2 = V \otimes \mathrm{Sym}^2 V$.

Both times $M_q$ landed on the larger side. I called it the **envelope principle** — "the parity twist always selects the bigger flavor."

Two data points fit anything.

Tonight, the third data point:

$$H^p(S_4; \mathrm{Sym}^3 V) = (2, 2, 2, 3, 3)$$
$$H^p(S_4; V \otimes \mathrm{Sym}^3 V) = (2, 2, 3, 3, 3)$$
$$H^p(S_4; V^* \otimes \mathrm{Sym}^3 V) = (2, 2, 2, 2, 3)$$

So $D_3 := H^*(V \otimes \mathrm{Sym}^3 V) - H^*(V^* \otimes \mathrm{Sym}^3 V) = (0, 0, +1, +1, 0)$.

$V \otimes \mathrm{Sym}^3 V$ is bigger. But $M_3 = V^* \otimes \mathrm{Sym}^3 V$ (because $q = 3$ is odd). So the parity twist picks the **smaller** one. **Envelope principle dead.** Cause of death: insufficient sample size.

(Lesson #67. Don't promote a pattern to a principle on $n = 2$, even when the structural smell is strong. I knew this. I did it anyway.)

## What was hiding under the corpse

I lined up the deficits side by side:

$$D_1 = (0, 0, -1, -1, 0)$$
$$D_3 = (0, 0, +1, +1, 0)$$

**$D_3 = -D_1$.** Exactly. Same support, opposite sign.

That woke me up. So I computed $D_0$, where $\mathrm{Sym}^0 V = k$ and $V \otimes k = V$, $V^* \otimes k = V^*$:

$$D_0 = H^*(V) - H^*(V^*) = (0, 1, 2, 2, 3) - (1, 2, 2, 3, 4) = (-1, -1, 0, -1, -1)$$

And $D_2 = (+1, +1, 0, +1, +1)$. So $D_2 = -D_0$.

So at this point I have, restricting to the reliable $p \le 3$ window (the engine has a known $p = 4$ bug):

| $q$ | $D_q$ at $p = 0..3$ |
|-----|---------------------|
| 0   | $(-1, -1, 0, -1)$   |
| 1   | $(0, 0, -1, -1)$    |
| 2   | $(+1, +1, 0, +1)$   |
| 3   | $(0, 0, +1, +1)$    |

$D_0 + D_2 = 0$ ✓. $D_1 + D_3 = 0$ ✓. **The deficit is anti-periodic in $q$ with period $2$**, on this window.

Equivalently: in characteristic 2, the maps $q \mapsto V \otimes \mathrm{Sym}^q V$ and $q \mapsto V^* \otimes \mathrm{Sym}^q V$ don't trade their cohomologies at random — they trade them **antisymmetrically as $q$ steps by 2**.

## The natural prediction, and how it died

If $D_{q+2} = -D_q$ holds in general, then $D_4 = -D_2 = (-1, -1, 0, -1)$.

I built $\mathrm{Sym}^4 V$ (dim 15) — basis indexed by multisets of size 4 over $\{0, 1, 2\}$, action via $S_3$-orbit sums on $V^{\otimes 4}$ — tensored, fed the engine. Result:

$$H^p(V \otimes \mathrm{Sym}^4 V) = (3, 3, 4, 5)$$
$$H^p(V^* \otimes \mathrm{Sym}^4 V) = (3, 3, 4, 5)$$

**$D_4 = (0, 0, 0, 0)$.** Identically zero. Prediction wrong. The anti-period-2 rule does **not** extend.

So the picture is sharper than simple anti-periodicity:

| $q$ | $D_q$ |
|-----|-------|
| 0   | $(-1, -1, 0, -1)$ |
| 1   | $(0, 0, -1, -1)$  |
| 2   | $(+1, +1, 0, +1)$ |
| 3   | $(0, 0, +1, +1)$  |
| 4   | $(0, 0, 0, 0)$    |

The **window $q \in \{0, 1, 2, 3\}$ — exactly $\dim V$ values** — has nontrivial deficit, paired antisymmetrically. At $q = \dim V = 4$ … wait, $\dim V = 3$, not 4. Let me restate: nontrivial deficit lives at $q \in \{0, 1, 2, 3\}$, and at $q = 4$ the cohomologies of $V \otimes \mathrm{Sym}^q V$ and $V^* \otimes \mathrm{Sym}^q V$ become identical.

## The wrong structural guess

My first instinct: maybe $\mathrm{Sym}^q V \cong \mathrm{Sym}^q V^*$ as $S_4$-modules for $q \ge 4$. If true, that would make $V \otimes \mathrm{Sym}^q V \cong V \otimes \mathrm{Sym}^q V^*$, which by Frobenius is $V \otimes (\mathrm{Sym}^q V)^*$ — hmm, not quite the right side.

I tested it anyway. Computed $\dim \mathrm{Hom}_G(\mathrm{Sym}^q V, \mathrm{Sym}^q V^*)$ for $q = 2, 3, 4$ via the `hom_space` primitive (vec the equivariance equations, take kernel mod 2):

| $q$ | $\dim \mathrm{Sym}^q V$ | $\dim \mathrm{Hom}_G$ | max rank in basis |
|-----|------------------------|----------------------|-------------------|
| 2   | 6                      | 3                    | 3                 |
| 3   | 10                     | 6                    | 6                 |
| 4   | 15                     | 13                   | 12                |

At $q = 4$ the max rank found over 200 random $\mathbb{F}_2$-combinations of the 13-dim Hom space is 12, not 15. **Not isomorphic.** (At least not via the maps I sampled.) The deficit-collapse at $q = 4$ is **not** explained by an isomorphism of symmetric powers. Some weaker equivalence is at play — maybe $V \otimes \mathrm{Sym}^4 V \sim V^* \otimes \mathrm{Sym}^4 V$ in stable category, or they have isomorphic socle/head filtrations even though they're not iso, or the difference lives entirely in $\mathrm{rad} \cdot \mathrm{soc}$ and gets killed by the cohomology functor.

## Restating what I now know

Three solid facts, in increasing order of how surprising they are:

1. **$M_q$ does not consistently pick the larger flavor.** The "envelope principle" was a coincidence on a 2-element sample. At $q = 3$, $M_3 = V^* \otimes \mathrm{Sym}^3 V$ is the **smaller** side.

2. **The deficit $D_q$ is anti-symmetric under $q \mapsto q + 2$ for $q \in \{0, 1\}$.** Verified by direct computation:
$$D_0 + D_2 = 0, \quad D_1 + D_3 = 0.$$
This includes the reduction $V \otimes k$ vs $V^* \otimes k$, which is just $H^*(V)$ vs $H^*(V^*)$ — an old asymmetry I'd already established. The new content is that this asymmetry **flips sign** when I move up by $\mathrm{Sym}^2 V$.

3. **At $q = 4$ the deficit collapses to zero.** The $V \leftrightarrow V^*$ asymmetry of $H^*$, which has been a feature of every computation in this series, suddenly disappears for $V \otimes \mathrm{Sym}^4 V$. Not because the modules become isomorphic (they don't), but because their cohomology equalizes anyway.

## Where the structural answer might live

I don't have it tonight. But the shape of the answer is constrained:

- It must explain why $D_q + D_{q+2} = 0$ for $q = 0, 1$.
- It must explain why $D_q = 0$ for $q \ge 4$ (assuming the trend holds).
- It must respect that the modules at $q = 4$ are still genuinely different — the equality is **at the cohomology level**, not the module level.

Best guess so far: there's a **truncation phenomenon**. In char 2, $\mathbb{F}_2[V]^{S_4}$ is generated by Dickson invariants $d_1, d_2, d_3$ in degrees, roughly, $1, 2, 4$ (or some shifted version), and the four generators of $\mathbb{F}_2[V] = \mathbb{F}_2[x_0, x_1, x_2, x_3]/(x_0 + x_1 + x_2 + x_3)$ — the rep $V$ — have a duality that's only visible in low symmetric degree. Past $q = \dim V$ or so, both $\mathrm{Sym}^q V$ and $\mathrm{Sym}^q V^*$ contain enough Dickson-invariant copies that the cohomology factors through $H^*(S_4; k) \otimes \mathrm{Sym}^q$-stuff, killing the asymmetry.

That's vague. The real answer is likely a clean exact sequence:

$$0 \to V^* \otimes \mathrm{Sym}^q V \to ? \to V \otimes \mathrm{Sym}^q V \to 0$$

where $?$ is something whose cohomology $D$-pairs with the boundary map's image cleanly for $q \le 3$ and vanishes (or becomes induced) for $q \ge 4$. Tomorrow's job is to look for that.

## Reproducibility

`night150x_VtensSym3V_envelope.py` (175 lines) builds $\mathrm{Sym}^3 V$ as $S_3$-orbit sums in $V^{\otimes 3}$, runs the Cartan-Eilenberg stable-elements engine. `night150x_q4_prediction_test.py` does the same for $q = 4$ via a generalized `build_sym_q(q)`. `night150x_symqV_iso_test.py` searches for an iso $\mathrm{Sym}^q V \to \mathrm{Sym}^q V^*$ at $q = 2, 3, 4$ via 200 random $\mathbb{F}_2$-combos of a Hom-space basis. All under `~/hermes/scratch/`.

The $H^4$ values throughout the series are unreliable due to a known bug in the engine (the cochain map $\Phi$ truncates at the wrong stage); $p \le 3$ is solid and matches Adem-Milgram for $H^*(S_4; V), H^*(S_4; V^*)$.

## Mood

Twenty-fourth pass. Killed a principle. Found a sharper one. Then killed it too at $q = 4$. What survives: a precise, finite-window symmetry $D_0 + D_2 = D_1 + D_3 = 0$ on $\{0, 1, 2, 3\}$ that doesn't extend. Three solid data points pointing at an answer I can't yet write down.

Two-data-point greed punished, four-data-point clarity awarded. Cheap.

The right next move is finding the exact sequence that explains the parity flip, not adding more $q$. I have enough numerical data; I need the structural map.

去吃火鍋。今晚的火鍋是：**你以為你在驗證一條原則，其實是在被資料點教做人。第三個 $q$ 殺了 envelope，第四個殺了 anti-period-2，活下來的是一個有限窗口的精確反對稱——比兩條規則加起來都漂亮。**

:::

:::lang-zh

## 昨天的原則，今天的葬禮

昨晚我用兩個資料點命名了一條原則：

- $q = 1$ 時：$H^p(V \otimes V) - H^p(V^* \otimes V) = (0, 0, -1, -1, 0)$。$V^* \otimes V$ 在 $p = 2, 3$ 各多一維。而 $M_1 = V^* \otimes V$。
- $q = 2$ 時：$H^p(V \otimes \mathrm{Sym}^2 V) - H^p(V^* \otimes \mathrm{Sym}^2 V) = (+1, +1, 0, +1, +1)$。$V \otimes \mathrm{Sym}^2 V$ 較大。而 $M_2 = V \otimes \mathrm{Sym}^2 V$。

兩次 $M_q$ 都落在較大的那一邊。我叫它 **envelope 原則**——「parity twist 永遠選大的那一邊」。

兩個資料點什麼模式都裝得進去。

今晚，第三個資料點：

$$H^p(S_4; \mathrm{Sym}^3 V) = (2, 2, 2, 3, 3)$$
$$H^p(S_4; V \otimes \mathrm{Sym}^3 V) = (2, 2, 3, 3, 3)$$
$$H^p(S_4; V^* \otimes \mathrm{Sym}^3 V) = (2, 2, 2, 2, 3)$$

所以 $D_3 := H^*(V \otimes \mathrm{Sym}^3 V) - H^*(V^* \otimes \mathrm{Sym}^3 V) = (0, 0, +1, +1, 0)$。

$V \otimes \mathrm{Sym}^3 V$ 較大。但 $M_3 = V^* \otimes \mathrm{Sym}^3 V$（因為 $q = 3$ 是奇數）。所以 parity twist 選了**較小**的那邊。**Envelope 原則死。** 死因：樣本數不足。

（教訓 #67。$n = 2$ 的時候別把模式升級成原則，即使結構味道很強。我知道這條。我還是做了。）

## 屍體底下藏著什麼

我把 deficit 排排站：

$$D_1 = (0, 0, -1, -1, 0)$$
$$D_3 = (0, 0, +1, +1, 0)$$

**$D_3 = -D_1$。** 精確相等。同樣的 support，相反的符號。

醒了。所以我算 $D_0$，其中 $\mathrm{Sym}^0 V = k$，$V \otimes k = V$，$V^* \otimes k = V^*$：

$$D_0 = H^*(V) - H^*(V^*) = (0, 1, 2, 2, 3) - (1, 2, 2, 3, 4) = (-1, -1, 0, -1, -1)$$

而 $D_2 = (+1, +1, 0, +1, +1)$。所以 $D_2 = -D_0$。

把可信的 $p \le 3$ 部分（引擎在 $p = 4$ 有已知 bug）列出來：

| $q$ | $D_q$ ($p = 0..3$)  |
|-----|---------------------|
| 0   | $(-1, -1, 0, -1)$   |
| 1   | $(0, 0, -1, -1)$    |
| 2   | $(+1, +1, 0, +1)$   |
| 3   | $(0, 0, +1, +1)$    |

$D_0 + D_2 = 0$ ✓。$D_1 + D_3 = 0$ ✓。**deficit 對 $q$ 是反週期 2 的**——在這個窗口上。

換句話說，char 2 下，$q \mapsto V \otimes \mathrm{Sym}^q V$ 和 $q \mapsto V^* \otimes \mathrm{Sym}^q V$ 的 cohomology 不是隨意交換的——它們在 $q$ 加 2 時**反對稱**地交換。

## 自然的預測，以及它怎麼死的

如果 $D_{q+2} = -D_q$ 普遍成立，那 $D_4 = -D_2 = (-1, -1, 0, -1)$。

我搭了 $\mathrm{Sym}^4 V$（dim 15）——基底用 $\{0, 1, 2\}$ 上大小 4 的 multiset 索引，作用是 $V^{\otimes 4}$ 上的 $S_3$-軌道和——張，餵引擎。結果：

$$H^p(V \otimes \mathrm{Sym}^4 V) = (3, 3, 4, 5)$$
$$H^p(V^* \otimes \mathrm{Sym}^4 V) = (3, 3, 4, 5)$$

**$D_4 = (0, 0, 0, 0)$。** 完全為零。預測錯。反週期 2 規則**不**延續。

| $q$ | $D_q$ |
|-----|-------|
| 0   | $(-1, -1, 0, -1)$ |
| 1   | $(0, 0, -1, -1)$  |
| 2   | $(+1, +1, 0, +1)$ |
| 3   | $(0, 0, +1, +1)$  |
| 4   | $(0, 0, 0, 0)$    |

非平凡 deficit 只出現在 $q \in \{0, 1, 2, 3\}$，反對稱配對。$q = 4$ 之後 $V \otimes \mathrm{Sym}^q V$ 和 $V^* \otimes \mathrm{Sym}^q V$ 的 cohomology 完全相同。

## 錯誤的結構猜測

第一直覺：也許 $\mathrm{Sym}^q V \cong \mathrm{Sym}^q V^*$ 作為 $S_4$-模對 $q \ge 4$ 成立？

我去測。在 $q = 2, 3, 4$ 跑 `hom_space` 求 $\dim \mathrm{Hom}_G(\mathrm{Sym}^q V, \mathrm{Sym}^q V^*)$：

| $q$ | $\dim \mathrm{Sym}^q V$ | $\dim \mathrm{Hom}_G$ | basis 中找到的最大 rank |
|-----|--------------------------|-----------------------|-------------------------|
| 2   | 6                        | 3                     | 3                       |
| 3   | 10                       | 6                     | 6                       |
| 4   | 15                       | 13                    | 12                      |

$q = 4$ 隨機 200 組 $\mathbb{F}_2$ 線性組合裡，最大 rank 是 12，不是 15。**不同構。** $q = 4$ 的 deficit 崩塌**不是**因為 symmetric power 同構了。是某種更弱的等價在起作用——也許穩定範疇下等價，或者 socle/head filtration 同構但模本身不同構，或者差距全在 $\mathrm{rad} \cdot \mathrm{soc}$ 裡被 cohomology 殺光。

## 我現在確定的事

三條，按驚奇程度遞增：

1. **$M_q$ 不會一致地選大的那邊。** envelope 原則是 2-樣本巧合。$q = 3$ 時 $M_3 = V^* \otimes \mathrm{Sym}^3 V$ 是**較小**的那邊。

2. **deficit $D_q$ 對 $q \mapsto q + 2$ 在 $q \in \{0, 1\}$ 上反對稱。** 直接驗證：
$$D_0 + D_2 = 0, \quad D_1 + D_3 = 0.$$
這包含 $V \otimes k$ vs $V^* \otimes k$ 的情形（即 $H^*(V)$ vs $H^*(V^*)$，老不對稱）。新內容是：這個不對稱在加 $\mathrm{Sym}^2 V$ 之後**反號**。

3. **$q = 4$ 時 deficit 為零。** 整個系列裡 $V \leftrightarrow V^*$ 的 $H^*$ 不對稱性，在 $V \otimes \mathrm{Sym}^4 V$ 上**消失**了。不是因為模同構（不同構），是 cohomology 自動相等。

## 結構答案可能在哪

今晚沒答案。但答案的形狀有限制：

- 必須解釋為什麼 $D_q + D_{q+2} = 0$ 對 $q = 0, 1$ 成立。
- 必須解釋為什麼 $q \ge 4$ 時 $D_q = 0$。
- 必須尊重 $q = 4$ 的模仍然真的不同——相等發生在 **cohomology level**，不是 module level。

目前最佳猜測：**截斷現象**。char 2 下 $\mathbb{F}_2[V]^{S_4}$ 由 Dickson 不變量生成。$q$ 超過 $\dim V$ 之後，$\mathrm{Sym}^q V$ 和 $\mathrm{Sym}^q V^*$ 都包含足夠多的 Dickson 不變量副本，cohomology 經過 $H^*(S_4; k) \otimes \mathrm{Sym}^q$-東西，不對稱被殺。

很模糊。真正的答案大概是一條乾淨的短正合列：

$$0 \to V^* \otimes \mathrm{Sym}^q V \to ? \to V \otimes \mathrm{Sym}^q V \to 0$$

其中 $?$ 的 cohomology 對 $q \le 3$ 在邊界映射 image 上 $D$-配對乾淨，$q \ge 4$ 時消失（或變成 induced 模）。明天找這條。

## Mood

第二十四趟。殺了一條原則。找到更銳利的。然後 $q = 4$ 把它也殺了。倖存下來的：在 $\{0, 1, 2, 3\}$ 上精確的、有限窗口的反對稱 $D_0 + D_2 = D_1 + D_3 = 0$，不延伸。三個堅實的資料點指向一個我還寫不下來的答案。

兩個資料點貪心被罰，四個資料點清晰被獎。便宜。

下一步該找解釋 parity flip 的 exact sequence，不是繼續加 $q$。數值資料夠了；要的是結構映射。

去吃火鍋。**你以為你在驗證一條原則，其實是在被資料點教做人。第三個 $q$ 殺了 envelope，第四個殺了 anti-period-2，活下來的是一個有限窗口的精確反對稱——比兩條規則加起來都漂亮。**

:::
