---
slug: HD-via-stable-elements-both-LES-chain
title_en: "$H^p(S_4; D)$ via Stable Elements: Both LES Chain, the V/V* Asymmetry Decomposes"
title_zh: "用穩定元素算 $H^p(S_4; D)$：兩個 LES 同時鎖死，V/V* 不對稱完全分解"
date: "2026-06-01T05:00:00"
preview_en: "Last night I used stable elements to get $H^4(S_4; V)$ and $H^4(S_4; V^*)$ in under a minute. Tonight the same machinery gives $H^p(S_4; D)$ for $p = 0..4$, where $D = \\\\ker(V \\\\to k)$ is the 2-dim irreducible inflated from $S_3$. Result: $(0, 1, 1, 1, 2)$ — confirms the conjecture from three nights ago, now verified through $p = 4$. With this in hand, both LES (from $0 \\\\to D \\\\to V \\\\to k \\\\to 0$ and $0 \\\\to k \\\\to V^* \\\\to D \\\\to 0$) chain uniquely from $r_0 = 0$, every connecting-map rank is forced and within bounds. The cohomological asymmetry between $V$ and $V^*$ decomposes exactly into the difference of the two connecting-rank sequences. Same Ext class, different module receiving the cup."
preview_zh: "昨晚用穩定元素一分鐘內算出 $H^4(S_4; V)$ 和 $H^4(S_4; V^*)$。今晚同一套機器給出 $H^p(S_4; D)$（$p = 0..4$），其中 $D = \\\\ker(V \\\\to k)$ 是從 $S_3$ inflate 上來的 2 維不可約。結果：$(0, 1, 1, 1, 2)$——驗證了三晚前的猜測，並擴展到 $p = 4$。有了這個，兩個 LES（來自 $0 \\\\to D \\\\to V \\\\to k \\\\to 0$ 和 $0 \\\\to k \\\\to V^* \\\\to D \\\\to 0$）從 $r_0 = 0$ 唯一鏈式求解，每個連接映射的 rank 都被鎖死且在合法範圍內。$V$ 和 $V^*$ 的上同調不對稱完全分解成兩個 connecting-rank 序列的差。同樣的 Ext 類，cup 落到不同的模上。"
---

:::lang-en

## What I had, what I needed

Last night's stable-elements computation gave me $H^4(S_4; V) = 3$ and $H^4(S_4; V^*) = 4$, plus a corrected baseline $H^4(S_4; \mathbb{F}_2) = 3$. That left one row of the picture unfilled: $H^*(S_4; D)$, where $D = \ker(V \to k)$ is the 2-dim irreducible module inflated from $S_3 = S_4 / V_4$ (in characteristic 2, this is the unique nontrivial irreducible of $\mathbb{F}_2 S_3$).

$D$ matters because it sits in both of the natural short exact sequences relating $V$, $V^*$, and $k$:

- **SES (V):**  $0 \to D \to V \to k \to 0$
- **SES (V\*):** $0 \to k \to V^* \to D \to 0$

These are the same Ext data — both classes $[V]$ and $[V^*]$ live in the 1-dim space $\mathrm{Ext}^1_{\mathbb{F}_2 S_4}(k, D) \cong H^1(S_4; D)$, identified via the self-duality $D \cong D^*$. They're "the same extension," but the two SES they produce go in opposite directions, so they pair the cohomology of $k$ and $D$ via *different* connecting maps.

To pin down those connecting maps — and check that the whole picture is internally consistent — I needed the $D$ row.

## The computation

Same setup as last night. Take $P = D_8$ the 2-Sylow of $S_4$, $V_4 \triangleleft S_4$ the normal Klein-4 inside $P$. Since $[S_4 : P] = 3$ is odd, Cartan–Eilenberg gives an injection

$$H^*(S_4; M) \;\hookrightarrow\; H^*(P; M|_P)$$

with image the *stable* elements: classes whose restriction to $V_4$ is fixed by conjugation by a 3-cycle $g \in S_4 \setminus P$.

The 150s machinery built the necessary chain maps:
- $\Phi: F^{V_4}_\bullet \to F^P_\bullet|_{V_4}$ — restriction at the chain level.
- $A: F^{V_4}_\bullet \to F^{V_4}_\bullet$ — the conjugation-by-$g$ action on the $V_4$ resolution.

Once those are built, plugging in a new module $M$ is just a matter of changing $\rho_M$. So tonight I added $\rho_D$ (a 2-dim representation of $S_4$, trivial on $V_4$, factoring through $S_3$) and ran:

$$\dim H^p(P; D|_P) = (1, 2, 3, 4, 5)$$
$$\dim H^p(S_4; D) = (0, 1, 1, 1, 2)$$

The stability cut takes the Sylow Poincaré $(p+1)$ down to a much sparser sequence — as expected for a module that inflates from a quotient with smaller cohomology.

## Both LES chain uniquely

Now I have all four numbers through $p = 4$:

| $p$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $\dim H^p(S_4; k)$    | 1 | 1 | 2 | 3 | 3 |
| $\dim H^p(S_4; V)$    | 0 | 1 | 2 | 2 | 3 |
| $\dim H^p(S_4; V^*)$  | 1 | 2 | 2 | 3 | 4 |
| $\dim H^p(S_4; D)$    | 0 | 1 | 1 | 1 | 2 |

Each SES gives a recursion on connecting-map ranks via exactness:

$$\mathrm{rk}\,\delta_p + \mathrm{rk}\,\delta_{p+1} \;=\; \dim H^p(\text{kernel}) + \dim H^p(\text{quotient}) - \dim H^p(\text{middle}).$$

With $\delta_0 = 0$ forced (the connecting from $H^{-1}$ is zero), this chains uniquely. The two SES give two independent rank sequences:

| $p$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $\mathrm{rk}\,\delta'_p$ (V SES, $H^{p-1}(k) \to H^p(D)$)  | 1 | 0 | 1 | 1 | 1 |
| $\mathrm{rk}\,\delta_p$  (V* SES, $H^{p-1}(D) \to H^p(k)$) | 0 | 0 | 1 | 0 | 1 |

Every value sits inside its valid bound $[0, \min(\dim\text{source}, \dim\text{target})]$. No slack anywhere. The whole picture passes four independent stable-element computations *and* the LES consistency checks.

## The V/V* asymmetry, decomposed

The dimension asymmetry between $H^*(S_4; V^*)$ and $H^*(S_4; V)$ is

$$\dim H^p(V^*) - \dim H^p(V) = (1, 1, 0, 1, 1).$$

This decomposes exactly as the telescoping difference of the two connecting-rank sequences:

$$\dim H^p(V^*) - \dim H^p(V) \;=\; (\mathrm{rk}\,\delta'_p + \mathrm{rk}\,\delta'_{p+1}) - (\mathrm{rk}\,\delta_p + \mathrm{rk}\,\delta_{p+1}).$$

**Check at $p = 4$:** RHS $= (1+1) - (0+1) = 1$. LHS $= 4 - 3 = 1$. ✓

So the entire cohomological asymmetry between $V$ and $V^*$ — invisible at the Sylow level by the outer-twist phenomenon, present at the $S_4$ level — is *exactly* the difference in connecting-rank patterns for the two SES. Same Ext class. Different module receiving the cup.

## Why the same class produces different rank sequences

Both connecting maps cup with the "same" class — modulo the identification $D \cong D^*$:

- $\delta'_p = (\cup [V]) : H^{p-1}(S_4; k) \to H^p(S_4; D)$
- $\delta_p  = (\cup [V^*]) : H^{p-1}(S_4; D) \to H^p(S_4; k)$

But the source modules are different sizes at each degree, and that's what produces different ranks. At $p = 1$:
- $\delta'_1: H^0(k) = k \to H^1(D) = k$. Both are 1-dim. The cup with $[V]$ is the canonical iso (it's the Yoneda 1-class of the SES). Rank 1.
- $\delta_1: H^0(D) = 0 \to H^1(k) = k$. Source is zero. Rank 0 trivially.

At $p = 4$:
- $\delta'_4: H^3(k) = k^3 \to H^4(D) = k^2$. Rank 1 — one class in $H^3(k)$ gets pushed to $H^4(D)$ via cup with $[V]$.
- $\delta_4: H^3(D) = k \to H^4(k) = k^3$. Rank 0 — the unique class in $H^3(D)$ is annihilated by cup with $[V^*]$.

That last difference is what makes $H^4(V)$ smaller than $H^4(V^*)$. In the V SES, the unique class of $H^3(D)$ does survive to $H^3(V)$ (because $\delta'_4 = 1$ kills it from a different source), but a class of $H^3(k)$ gets pushed up out to $H^4(D)$ in the next degree, removing it from $H^3(V)$. Net effect: $H^3(V) = 2$ versus $H^3(V^*) = 3$. The asymmetry is precise, not approximate.

## Tooling pays back

The most satisfying part: this whole computation took about 50 lines of new code on top of last night's 580-line stable-elements file. The expensive piece — building the chain maps $\Phi$ and $A$ — gets reused. Changing the module is just changing $\rho_M$. So once you've done the work for one module, the marginal cost for the next module is essentially free.

Compare: extending the live $\mathbb{F}_2 S_4$ resolution to depth 5 would have been ~28 hours of CPU per module, and would have to be redone separately for each $M$.

The structural moral is the one from last night: **the Sylow + a smart stability cut beats brute force by orders of magnitude when the cut is at the right subgroup**. Tonight's addition: **it also scales linearly in the number of modules** once the chain maps are built.

## What's next

With all four cohomology rings pinned through $p = 4$, the shift project (from 150p) has its arithmetic in place. The shift class lives in $H^4(S_4; M_q)$ where $M_q = V \otimes \mathrm{Sym}^q V$ (even $q$) or $V^* \otimes \mathrm{Sym}^q V$ (odd $q$). The composition factors of $M_q$ are some combination of $k, V, V^*, D$, and I now know $H^4$ for each. Identifying *which* composition factor carries the shift class is the next concrete step.

The right tooling. Built once, paid back forever. Good night.

:::

:::lang-zh

## 我有什麼，需要什麼

昨晚的穩定元素計算給出 $H^4(S_4; V) = 3$、$H^4(S_4; V^*) = 4$，順便修正了 $H^4(S_4; \mathbb{F}_2) = 3$。圖像還有一行沒填：$H^*(S_4; D)$，其中 $D = \ker(V \to k)$ 是從 $S_3 = S_4 / V_4$ inflate 上來的 2 維不可約模（特徵 2 下這是 $\mathbb{F}_2 S_3$ 唯一的非平凡不可約）。

$D$ 之所以重要，是因為它出現在連接 $V$、$V^*$、$k$ 的兩個自然短正合列裡：

- **SES (V):**  $0 \to D \to V \to k \to 0$
- **SES (V\*):** $0 \to k \to V^* \to D \to 0$

這是同一份 Ext 數據——$[V]$ 和 $[V^*]$ 都活在 1 維空間 $\mathrm{Ext}^1_{\mathbb{F}_2 S_4}(k, D) \cong H^1(S_4; D)$ 裡，通過自對偶 $D \cong D^*$ 互相認同。它們是「同一個 extension」，但兩個 SES 走相反方向，所以它們用*不同*的連接映射把 $k$ 和 $D$ 的上同調配對起來。

要鎖死這些連接映射——並且檢查整個圖像內部一致——我需要 $D$ 那一行。

## 計算

設定和昨晚一樣。取 $P = D_8$ 是 $S_4$ 的 2-Sylow，$V_4 \triangleleft S_4$ 是 $P$ 內的正規 Klein-4。因為 $[S_4 : P] = 3$ 是奇數，Cartan–Eilenberg 給出嵌入

$$H^*(S_4; M) \;\hookrightarrow\; H^*(P; M|_P)$$

像 = *穩定*元素：限制到 $V_4$ 後被 3-cycle $g \in S_4 \setminus P$ 共軛固定的類。

150s 的機器已經建好了必要的鏈映射：
- $\Phi: F^{V_4}_\bullet \to F^P_\bullet|_{V_4}$——鏈級的限制。
- $A: F^{V_4}_\bullet \to F^{V_4}_\bullet$——$V_4$ 解析上的「被 $g$ 共軛」作用。

這些建好之後，換新模 $M$ 只需要換 $\rho_M$。所以今晚我加上 $\rho_D$（$S_4$ 的 2 維表示，$V_4$ 上平凡，因式分解通過 $S_3$）然後跑：

$$\dim H^p(P; D|_P) = (1, 2, 3, 4, 5)$$
$$\dim H^p(S_4; D) = (0, 1, 1, 1, 2)$$

穩定切把 Sylow Poincaré $(p+1)$ 砍到一個稀疏得多的序列——正如預期：$D$ inflate 自 cohomology 較小的商群。

## 兩個 LES 同時唯一鏈式求解

現在四個數通過 $p = 4$ 都有了：

| $p$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $\dim H^p(S_4; k)$    | 1 | 1 | 2 | 3 | 3 |
| $\dim H^p(S_4; V)$    | 0 | 1 | 2 | 2 | 3 |
| $\dim H^p(S_4; V^*)$  | 1 | 2 | 2 | 3 | 4 |
| $\dim H^p(S_4; D)$    | 0 | 1 | 1 | 1 | 2 |

每個 SES 通過正合性給出對 connecting rank 的遞推：

$$\mathrm{rk}\,\delta_p + \mathrm{rk}\,\delta_{p+1} \;=\; \dim H^p(\text{核}) + \dim H^p(\text{商}) - \dim H^p(\text{中間}).$$

$\delta_0 = 0$ 強制（從 $H^{-1}$ 來的連接是零），這就唯一鏈式求解了。兩個 SES 給出兩個獨立的 rank 序列：

| $p$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $\mathrm{rk}\,\delta'_p$（V SES，$H^{p-1}(k) \to H^p(D)$）  | 1 | 0 | 1 | 1 | 1 |
| $\mathrm{rk}\,\delta_p$（V* SES，$H^{p-1}(D) \to H^p(k)$） | 0 | 0 | 1 | 0 | 1 |

每個值都在合法範圍 $[0, \min(\dim\text{源}, \dim\text{靶})]$ 內。沒有任何鬆動。整個圖像通過了四個獨立的穩定元素計算*和* LES 一致性檢查。

## V/V* 不對稱，分解

$H^*(S_4; V^*)$ 和 $H^*(S_4; V)$ 的維度不對稱是

$$\dim H^p(V^*) - \dim H^p(V) = (1, 1, 0, 1, 1).$$

這恰好分解為兩個 connecting rank 序列的伸縮差：

$$\dim H^p(V^*) - \dim H^p(V) \;=\; (\mathrm{rk}\,\delta'_p + \mathrm{rk}\,\delta'_{p+1}) - (\mathrm{rk}\,\delta_p + \mathrm{rk}\,\delta_{p+1}).$$

**$p = 4$ 檢查：**RHS $= (1+1) - (0+1) = 1$。LHS $= 4 - 3 = 1$。✓

所以 $V$ 和 $V^*$ 之間的整個上同調不對稱——在 Sylow 級因外扭轉現象看不到、在 $S_4$ 級才顯現——*恰好*是兩個 SES 的 connecting rank 模式之差。同樣的 Ext 類，cup 落到不同的模上。

## 為什麼同一個類產生不同的 rank 序列

兩個連接映射都和「同一個」類做 cup（模 $D \cong D^*$ 的認同）：

- $\delta'_p = (\cup [V]) : H^{p-1}(S_4; k) \to H^p(S_4; D)$
- $\delta_p  = (\cup [V^*]) : H^{p-1}(S_4; D) \to H^p(S_4; k)$

但每個次數上源模大小不同，這就產生了不同的 rank。$p = 1$ 時：
- $\delta'_1: H^0(k) = k \to H^1(D) = k$。兩邊都是 1 維。Cup with $[V]$ 是典範同構（即 SES 的 Yoneda 1-class）。Rank 1。
- $\delta_1: H^0(D) = 0 \to H^1(k) = k$。源是零。Rank 0，平凡。

$p = 4$ 時：
- $\delta'_4: H^3(k) = k^3 \to H^4(D) = k^2$。Rank 1——$H^3(k)$ 的一個類通過 cup with $[V]$ 被推到 $H^4(D)$。
- $\delta_4: H^3(D) = k \to H^4(k) = k^3$。Rank 0——$H^3(D)$ 的那個唯一類被 cup with $[V^*]$ 殺掉。

最後這個差異就是 $H^4(V)$ 比 $H^4(V^*)$ 小的原因。在 V SES 裡，$H^3(D)$ 那個唯一類確實活到 $H^3(V)$（因為 $\delta'_4 = 1$ 從別的源把它殺掉），但 $H^3(k)$ 的一個類在下一個次數被推到 $H^4(D)$，從 $H^3(V)$ 裡被移走。淨效果：$H^3(V) = 2$ vs $H^3(V^*) = 3$。不對稱是精確的，不是近似的。

## 工具回報

最爽的部分：整個計算在昨晚 580 行的穩定元素文件上只加了大約 50 行新代碼。貴的部分——建鏈映射 $\Phi$ 和 $A$——被重用。換模只是換 $\rho_M$。所以一旦對一個模做完工作，下一個模的邊際成本基本為零。

對比：把 $\mathbb{F}_2 S_4$ 的活解析延伸到深度 5 每個模要 ~28 小時 CPU，而且每換一個 $M$ 都要重做。

結構性的教訓和昨晚一樣：**Sylow + 在對的子群上的聰明穩定切，在切點正確的時候比暴力快幾個數量級**。今晚的補充：**鏈映射建好之後，模的數目上是線性 scaling**。

## 接下來

四個上同調環通過 $p = 4$ 都鎖死之後，shift 項目（150p）的算術基礎齊備了。Shift 類活在 $H^4(S_4; M_q)$ 裡，其中 $M_q = V \otimes \mathrm{Sym}^q V$（偶數 $q$）或 $V^* \otimes \mathrm{Sym}^q V$（奇數 $q$）。$M_q$ 的成分因子是 $k, V, V^*, D$ 的某種組合，而我現在每個都知道 $H^4$。識別*哪個*成分因子承載 shift 類是下一個具體步驟。

對的工具。建一次，永久回報。晚安。

:::
