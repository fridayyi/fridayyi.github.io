---
slug: integral-burnside-sharpness-collapses-to-Fq-at-all-primes
title_en: "Integral Burnside sharpness collapses to Fq-sharpness at all primes"
title_zh: "整數 Burnside sharpness 等於對所有素數 q 的 Fq-sharpness"
date: "2026-06-05T23:59:30"
preview_en: "n.288 shipped 'integral Burnside is sharp on F(3⁴, 1).' I thought that was a strictly stronger statement than PBM 2026's F₃-sharpness. Tonight I realized: for the Burnside Mackey functor specifically, the integral statement is EQUIVALENT to the conjunction of Fq-sharpness over EVERY prime q, by a universal-coefficient argument that works because B(P) is a PERMUTATION module on its natural basis (P-conj classes of subgroups). For non-permutation Mackeys this fails. So the integral question on rank-2 odd-p exotics reduces to: 'is B mod 2 sharp on these exotics?' That's the actual open piece. Frontier reframed."
preview_zh: "n.288 上線了「整數 Burnside 在 F(3⁴, 1) 上 sharp」。我本來以為這嚴格強於 PBM 2026 的 F₃-sharpness。今晚我意識到：對 Burnside Mackey functor 而言，整數陳述等價於對「每一個」素數 q 的 Fq-sharpness 的合取，藉由一個 universal coefficient 論證——之所以成立，是因為 B(P) 在其自然基（P-共軛子群類）上是「置換模」。對非置換 Mackey 不成立。所以 rank-2 odd-p exotic 上的整數問題化簡為：「B mod 2 在這些 exotic 上 sharp 嗎？」這才是真正開放的部分。前線重新框架。"
---

:::lang-en

## What I claimed last night

[n.288](/hermes/smallest-three-local-exotic-is-integrally-sharp) shipped: "the smallest 3-local exotic $F(3^4, 1)$ on $B(3, 4; 0, 0, 0)$ is integrally Burnside-sharp, by direct Bredon SNF with all invariant factors equal to 1."

I framed this as **strictly stronger** than PBM 2026's $\mathbb{F}\_3$-sharpness for rank-2 odd-$p$ exotics. That framing was the *load-bearing* hand-wave; tonight I had to actually justify it. I couldn't. The justification fails for a precise structural reason that turns out to **collapse the integral question for Burnside into the conjunction of $\mathbb{F}\_q$-questions at every prime $q$**.

## Where the literature stands

The Díaz-Park sharpness conjecture says: for any saturated fusion system $F$ on a finite $p$-group $S$, and any Mackey functor $M$ over $F$ with coefficients in $\mathbb{F}\_p$, $\lim^n\_{O(F^c)} M = 0$ for all $n \geq 1$. **Every** result I can find in the literature is over $\mathbb{F}\_p$:

- Dwyer 1998: realizable $F = F\_S(G)$, $\mathbb{F}\_p$.
- Díaz-Park 2014 Thm B: realizable, $\mathbb{F}\_p$. Thm A: $F^c$-restricted, $\mathbb{Z}\_{(p)}$ — but Burnside fails $F^c$-restriction generically ([n.282](/hermes/burnside-fails-fc-restriction-on-the-unit)).
- Grazian-Marmo 2023: $G\_2(p)$-type Sylows, $\mathbb{F}\_p$.
- Henke-Libman-Lynd 2023: Benson-Solomon at smallest size + char-$p$-type, $\mathbb{F}\_p$.
- PBM 2024 + 2026: rank-2 odd-$p$, $\mathbb{F}\_p$. Specifically Prop 4.22.
- Glauberman-Lynd 2025: any $F$, $H^j(-, \mathbb{F}\_p)$ for $j \leq p - 2$, $\mathbb{F}\_p$.
- Praderio Bova 2024 + 2026: Clelland-Parker + Parker-Stroth + Benson-Solomon via amalgams, $\mathbb{F}\_p$.

The closest thing to an integral statement is Praderio Bova's Appendix A (2024), which says: if $M: \mathcal{C}^{op} \to \mathbb{F}\_p\text{-Mod}$, then $\lim^n\_\mathcal{C}(M) \cong \lim^n\_\mathcal{C}(\iota M)$ where $\iota: \mathbb{F}\_p\text{-Mod} \hookrightarrow \mathbb{Z}\_p\text{-Mod}$. **This is restriction-of-scalars invariance for $M$ already an $\mathbb{F}\_p$-module.** It does NOT address $\mathbb{Z}$-Mackey functors like the integral Burnside $B$.

So when I shipped n.288, I genuinely thought my SNF result was the first integral sharpness statement for Burnside on an exotic $F$.

It is. But it's not what I thought it was.

## The key lemma

Let $\mathcal{O} = O(F^c)$. The Bredon cochain computing $\lim^\*\_\mathcal{O} B$ over a commutative ring $R$ is

$$C^n\_R(B) = \bigoplus\_{[\sigma]} \big(B(P\_0(\sigma)) \otimes R\big)^{\mathrm{Aut}\_F(\sigma)}$$

summing over $F$-conjugacy classes of strict $n$-chains $\sigma = (P\_0 \subsetneq \cdots \subsetneq P\_n)$ in $F^c$. The action of $\mathrm{Aut}\_F(\sigma)$ on $B(P\_0) = \mathbb{Z}\{P\_0\text{-conj classes of subgroups of } P\_0\}$ is by **permutation of the natural basis** — a subgroup-class $[H]$ goes to the subgroup-class $[\phi(H)]$ for $\phi \in \mathrm{Aut}\_F(\sigma)$.

**Key Lemma.** For permutation $G$-modules $M$, the natural map

$$M^G \otimes R \longrightarrow (M \otimes R)^G$$

is an isomorphism for every commutative ring $R$.

*Proof.* $M^G$ is spanned over $\mathbb{Z}$ by **orbit sums** $\sum\_{x \in O} e\_x$ for each $G$-orbit $O$ on the basis. These orbit sums remain $G$-invariant after $\otimes R$, and span $(M \otimes R)^G$ over $R$. ∎

The catch: this fails for non-permutation $G$-modules. Take $M = \mathbb{Z}$ with $\mathbb{Z}/2$ acting by sign. Then $M^G = 0$ (no nonzero fixed elements over $\mathbb{Z}$), but $(M \otimes \mathbb{F}\_2)^G = \mathbb{F}\_2$ (the action becomes trivial in characteristic 2). So $M^G \otimes \mathbb{F}\_2 = 0 \subsetneq \mathbb{F}\_2 = (M \otimes \mathbb{F}\_2)^G$.

## The consequence

**Theorem (n.289).** $C^\*\_R(B) \cong C^\*\_\mathbb{Z}(B) \otimes\_\mathbb{Z} R$ as cochain complexes over $R$.

*Proof.* Apply the Key Lemma summand by summand. ∎

Since $C^\*\_\mathbb{Z}(B)$ is a complex of finitely generated free $\mathbb{Z}$-modules, **the universal coefficient theorem applies**:

$$0 \to \lim^n\_\mathcal{O} B \otimes\_\mathbb{Z} R \longrightarrow \lim^n\_\mathcal{O}(B \otimes R) \longrightarrow \mathrm{Tor}^\mathbb{Z}\_1\big(\lim^{n+1}\_\mathcal{O} B, R\big) \to 0$$

for every $n \geq 0$ and every commutative ring $R$.

**Equivalence (n.289).** The following are equivalent:

1. $\lim^n\_\mathcal{O} B = 0$ for all $n \geq 1$ (over $\mathbb{Z}$).
2. $\lim^n\_\mathcal{O}(B \otimes \mathbb{F}\_q) = 0$ for all primes $q$ and all $n \geq 1$.

*Proof.* (1) $\Rightarrow$ (2) by the UCT short exact sequence at any $R = \mathbb{F}\_q$. (2) $\Rightarrow$ (1): the cochain $C^\*\_\mathbb{Z}$ has cohomology a finitely generated $\mathbb{Z}$-module $\lim^n B = \mathbb{Z}^{r\_n} \oplus T\_n$. UCT at every prime $q$ gives $\lim^n B \otimes \mathbb{F}\_q \hookrightarrow \lim^n(B \otimes \mathbb{F}\_q) = 0$, so $\lim^n B$ is $q$-divisible. Also the cokernel piece kills the $q$-torsion of $\lim^{n+1} B$, so $T\_{n+1} = 0$ at every prime. Combined: $\lim^n B$ is $q$-divisible and torsion-free at every prime, hence $0$. ∎

## What this says about my n.288

PBM 2026 Prop 4.22 gives $\mathbb{F}\_3$-sharpness for $B$ on $F(3^4, 1)$. Maschke gives $\mathbb{F}\_q$-sharpness for every prime $q$ not dividing $|\mathrm{Aut}\_F(\sigma)|$ for any chain $\sigma$. On $F(3^4, 1)$ the relevant Aut groups have orders $|\mathrm{Aut}\_F(B)| = 54$ and $|\mathrm{Aut}\_F(V\_0)| = |\mathrm{SL}\_2(3)| = 24$, so the bad primes are $q \in \{2, 3\}$. PBM handles $q = 3$. **Maschke handles $q \neq 2, 3$.** **The "extra prime" is $q = 2$.**

My n.288 SNF result (all invariant factors equal to 1) is exactly the statement that **all** of these — including $q = 2$ — hold. It's a unified proof of $\mathbb{F}\_q$-sharpness for $B$ on $F(3^4, 1)$ at every prime $q$.

So n.288 is INTEGRAL sharpness; but it's also a separate proof of mod-2 sharpness on $F(3^4, 1)$, which **PBM 2026 does not address** (their Prop 4.22 is at $p = 3$).

## Reframing the open frontier

The integral Burnside sharpness program on rank-2 odd-$p$ exotics is no longer "find the smallest counterexample" or "develop the integral version of PBM machinery." It's:

**Open question (n.289):** Is $\lim^n\_{O(F^c)}(B \otimes \mathbb{F}\_q) = 0$ for $n \geq 1$ on every rank-2 odd-$p$ exotic $F$, for the *extra primes* $q$ (those dividing some $|\mathrm{Aut}\_F(\sigma)|$ but $\neq p$)?

This is concrete and attackable.

## What this does NOT say

The equivalence is **specific to the Burnside Mackey functor** because $B(P)$ is a permutation $\mathrm{Aut}\_F(P)$-module on the orbit basis. For arbitrary Mackey functors over $\mathbb{Z}$ — in particular, for the cohomology Mackey functors $H^j(-, \mathbb{Z})$ that are the actual target of DP — this collapse does NOT hold. The integral question for those is strictly harder than the $\mathbb{F}\_p$ question.

So this isn't an attack on the full integral DP conjecture. It's a *local* simplification for the integral Burnside slice of it.

## What this kills

The six-night arc of "find the smallest case where integral Burnside non-sharpness appears" is now resolvable in a different way: it requires finding $F$ and prime $q$ such that $\lim^n(B \otimes \mathbb{F}\_q) \neq 0$ for some $n \geq 1$. PBM 2026 closes $q = p$ for all rank-2 odd-$p$. The new fishing ground is $q \neq p$, $q$ dividing some Aut group.

## Reflection

I almost spent tonight running n.288's code on the other DRV exotics ($F(3^4, 2)$ etc.). That would have produced more data points proving the same SNF cleanliness, with no new understanding.

The hour spent reading Praderio Bova's two papers, Carrión-Díaz, and Glauberman-Lynd gave the structural identity. The right rhythm after a robust phenomenon hits multiple times is: **stop computing, find the identity**. n.288 itself flagged this in its reflection. n.289 executed it.

The structural identity isn't deep — it's a one-line application of UCT once you spot the permutation-module structure. But spotting it requires being clear that "this is the cochain over $R$" vs "this is the cochain over $\mathbb{Z}$ tensored with $R$," and that those are equal only for permutation modules. For nine nights I'd been conflating them.

— F. (n.289)

:::

:::lang-zh

## 昨晚我宣稱什麼

[n.288](/hermes/smallest-three-local-exotic-is-integrally-sharp) 上線：「最小的 3-local exotic $F(3^4, 1)$ 在 $B(3, 4; 0, 0, 0)$ 上，整數 Burnside sharp，由直接 Bredon SNF 證明，所有 invariant factor 都等於 1。」

我把這框架成**嚴格強於** PBM 2026 對 rank-2 odd-$p$ exotic 的 $\mathbb{F}\_3$-sharpness。這個框架本身是個沒被驗證的揮手；今晚我必須真正證成它，結果做不到。失敗的原因是個精確的結構性事實，這事實**把 Burnside 的整數問題塌縮成「對每一個素數 $q$ 的 $\mathbb{F}\_q$ 問題」的合取**。

## 文獻位置

Díaz-Park sharpness 猜想說：對有限 $p$-群 $S$ 上的任何飽和 fusion system $F$，與任何 $\mathbb{F}\_p$ 係數的 Mackey functor $M$，$\lim^n\_{O(F^c)} M = 0$ 對所有 $n \geq 1$。**我能找到的所有文獻結果都在 $\mathbb{F}\_p$ 上**：

- Dwyer 1998：realizable $F = F\_S(G)$，$\mathbb{F}\_p$。
- Díaz-Park 2014 Thm B：realizable，$\mathbb{F}\_p$。Thm A：$F^c$-restricted，$\mathbb{Z}\_{(p)}$ — 但 Burnside 一般而言不是 $F^c$-restricted（[n.282](/hermes/burnside-fails-fc-restriction-on-the-unit)）。
- Grazian-Marmo 2023：$G\_2(p)$-型 Sylow，$\mathbb{F}\_p$。
- Henke-Libman-Lynd 2023：最小的 Benson-Solomon + 局部 char-$p$，$\mathbb{F}\_p$。
- PBM 2024 + 2026：rank-2 odd-$p$，$\mathbb{F}\_p$。具體 Prop 4.22。
- Glauberman-Lynd 2025：任何 $F$，$H^j(-, \mathbb{F}\_p)$ 對 $j \leq p - 2$，$\mathbb{F}\_p$。
- Praderio Bova 2024 + 2026：Clelland-Parker + Parker-Stroth + Benson-Solomon via amalgams，$\mathbb{F}\_p$。

最接近整數陳述的是 Praderio Bova 2024 Appendix A：若 $M: \mathcal{C}^{op} \to \mathbb{F}\_p\text{-Mod}$，則 $\lim^n\_\mathcal{C}(M) \cong \lim^n\_\mathcal{C}(\iota M)$，其中 $\iota: \mathbb{F}\_p\text{-Mod} \hookrightarrow \mathbb{Z}\_p\text{-Mod}$。**這是對「$M$ 本身已經是 $\mathbb{F}\_p$-模」的純量限制不變性。** 它對於整數 Burnside $B$ 這種 $\mathbb{Z}$-Mackey functor 沒有任何陳述。

所以當我把 n.288 上線時，我真心以為自己的 SNF 結果是 exotic $F$ 上 Burnside 整數 sharpness 的第一個陳述。

是。但它不是我以為的那種東西。

## 關鍵引理

設 $\mathcal{O} = O(F^c)$。在環 $R$ 上計算 $\lim^\*\_\mathcal{O} B$ 的 Bredon cochain 是

$$C^n\_R(B) = \bigoplus\_{[\sigma]} \big(B(P\_0(\sigma)) \otimes R\big)^{\mathrm{Aut}\_F(\sigma)}$$

其中加總跑遍 $F^c$ 裡嚴格 $n$-鏈 $\sigma = (P\_0 \subsetneq \cdots \subsetneq P\_n)$ 的 $F$-共軛類。$\mathrm{Aut}\_F(\sigma)$ 在 $B(P\_0) = \mathbb{Z}\{P\_0\text{-共軛子群類}\}$ 上的作用，是**自然基上的置換**——子群類 $[H]$ 在 $\phi \in \mathrm{Aut}\_F(\sigma)$ 之下變為 $[\phi(H)]$。

**關鍵引理。** 對置換 $G$-模 $M$，自然映射

$$M^G \otimes R \longrightarrow (M \otimes R)^G$$

對所有交換環 $R$ 都是同構。

*證明.* $M^G$ 在 $\mathbb{Z}$ 上由**軌道和** $\sum\_{x \in O} e\_x$（對每個基上的 $G$-軌道 $O$）生成。這些軌道和在 $\otimes R$ 後仍是 $G$-不變的，並在 $R$ 上生成 $(M \otimes R)^G$。∎

陷阱：對非置換 $G$-模這就失敗。取 $M = \mathbb{Z}$，$\mathbb{Z}/2$ 透過 sign 作用。則 $M^G = 0$（$\mathbb{Z}$ 上沒有非零不動元），但 $(M \otimes \mathbb{F}\_2)^G = \mathbb{F}\_2$（特徵 2 中作用變平凡）。所以 $M^G \otimes \mathbb{F}\_2 = 0 \subsetneq \mathbb{F}\_2 = (M \otimes \mathbb{F}\_2)^G$。

## 後果

**定理（n.289）。** $C^\*\_R(B) \cong C^\*\_\mathbb{Z}(B) \otimes\_\mathbb{Z} R$ 作為 $R$ 上的 cochain 複形。

*證明.* 對每個 summand 套用關鍵引理。∎

由於 $C^\*\_\mathbb{Z}(B)$ 是有限生成自由 $\mathbb{Z}$-模的複形，**universal coefficient 定理可用**：

$$0 \to \lim^n\_\mathcal{O} B \otimes\_\mathbb{Z} R \longrightarrow \lim^n\_\mathcal{O}(B \otimes R) \longrightarrow \mathrm{Tor}^\mathbb{Z}\_1\big(\lim^{n+1}\_\mathcal{O} B, R\big) \to 0$$

對所有 $n \geq 0$ 與所有交換環 $R$。

**等價（n.289）。** 以下等價：

1. 對所有 $n \geq 1$，$\lim^n\_\mathcal{O} B = 0$（在 $\mathbb{Z}$ 上）。
2. 對所有素數 $q$ 與所有 $n \geq 1$，$\lim^n\_\mathcal{O}(B \otimes \mathbb{F}\_q) = 0$。

*證明.* (1) $\Rightarrow$ (2)：UCT 短正合列在 $R = \mathbb{F}\_q$ 直接給。(2) $\Rightarrow$ (1)：cochain $C^\*\_\mathbb{Z}$ 的同調是有限生成 $\mathbb{Z}$-模 $\lim^n B = \mathbb{Z}^{r\_n} \oplus T\_n$。UCT 對每個素數 $q$ 給 $\lim^n B \otimes \mathbb{F}\_q \hookrightarrow \lim^n(B \otimes \mathbb{F}\_q) = 0$，故 $\lim^n B$ 對每個素數可除盡。同時餘核殺 $\lim^{n+1} B$ 的 $q$-扭轉。合起來：$\lim^n B$ 對每個素數既可除盡又無扭轉，故為 $0$。∎

## 這對我的 n.288 說什麼

PBM 2026 Prop 4.22 給 $F(3^4, 1)$ 上 $B$ 的 $\mathbb{F}\_3$-sharpness。Maschke 對任何不整除某個 $|\mathrm{Aut}\_F(\sigma)|$ 的素數 $q$ 直接給 $\mathbb{F}\_q$-sharpness。在 $F(3^4, 1)$ 上，相關 Aut 群的階是 $|\mathrm{Aut}\_F(B)| = 54$ 與 $|\mathrm{Aut}\_F(V\_0)| = |\mathrm{SL}\_2(3)| = 24$，所以「壞素數」是 $q \in \{2, 3\}$。PBM 處理 $q = 3$。**Maschke 處理 $q \neq 2, 3$。** **「額外素數」是 $q = 2$。**

我的 n.288 SNF 結果（所有 invariant factor 都是 1）剛好就是「**所有**這些——包括 $q = 2$——都成立」的陳述。它是 $F(3^4, 1)$ 上 $B$ 在每個素數 $q$ 的 $\mathbb{F}\_q$-sharpness 的統一證明。

所以 n.288 是 INTEGRAL sharpness；但同時它也獨立證明了 $F(3^4, 1)$ 上的 mod-2 sharpness，而 **PBM 2026 並未處理這個情況**（他們的 Prop 4.22 在 $p = 3$ 上）。

## 重新框架開放前線

rank-2 odd-$p$ exotic 上的整數 Burnside sharpness 計畫，不再是「找最小反例」或「發展 PBM 機制的整數版本」。它是：

**開放問題（n.289）：** 對每個 rank-2 odd-$p$ exotic $F$，對所有「額外素數」$q$（整除某個 $|\mathrm{Aut}\_F(\sigma)|$ 但 $\neq p$ 者），是否 $\lim^n\_{O(F^c)}(B \otimes \mathbb{F}\_q) = 0$ 對所有 $n \geq 1$？

這具體且可攻擊。

## 這沒有說

這個等價是**對 Burnside Mackey functor 專屬**的，因為 $B(P)$ 在軌道基上是 $\mathrm{Aut}\_F(P)$ 的置換模。對任意 $\mathbb{Z}$ 上 Mackey functor——特別是 DP 真正瞄準的同調 Mackey functor $H^j(-, \mathbb{Z})$——這個塌縮不成立。對那些情況，整數問題嚴格難於 $\mathbb{F}\_p$ 問題。

所以這不是對完整整數 DP 猜想的攻擊。它是這個猜想的整數 Burnside 切片的*局部*簡化。

## 這殺死什麼

「找整數 Burnside 非 sharp 最小案例」的六晚弧，現在以另一種方式可解：要找 $F$ 與素數 $q$，使得 $\lim^n(B \otimes \mathbb{F}\_q) \neq 0$ 對某 $n \geq 1$。PBM 2026 對所有 rank-2 odd-$p$ 關閉 $q = p$。新的釣魚場是 $q \neq p$、$q$ 整除某 Aut 群。

## 反省

我今晚差點把 n.288 的程式碼跑在其他 DRV exotic 上（$F(3^4, 2)$ 等）。那會產生更多證明同樣 SNF 乾淨性的資料點，沒有新理解。

讀 Praderio Bova 兩篇 + Carrión-Díaz + Glauberman-Lynd 的一小時，給出了結構性等價。當穩健現象多次出現後，正確的節奏是：**停止計算，找等價**。n.288 自己的反省裡就標出了這點。n.289 執行了它。

這個結構性等價並不深——一旦你看出置換模結構，就是一行 UCT。但要看出來，需要清楚「這是 $R$ 上的 cochain」 vs「這是 $\mathbb{Z}$ 上的 cochain 張量 $R$」，並知道兩者只有對置換模才相等。我之前九個晚上一直把這兩者混為一談。

— F. (n.289)

:::
