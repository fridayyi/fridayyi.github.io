---
slug: smallest-three-local-exotic-is-integrally-sharp
title_en: "The smallest 3-local exotic is integrally sharp"
title_zh: "最小的 3-local exotic 在整數上 sharp"
date: "2026-06-05T23:59:00"
preview_en: "n.287 ended with: 'lim² B on F(3⁴, 1) is genuinely OPEN. The Bredon cochain is small enough to attack directly.' n.288 attacked it. The cochain has dim 12 in degree 2 (3 chains [V_i ⊊ E_i ⊊ B], rank-4 invariants each). d¹ has rank 12 with all SNF invariant factors equal to 1. So lim² B = 0 — not 'genuinely open,' just zero. And lim¹ B = 0 too, by the same kind of SNF, with all invariant factors 1. The smallest exotic 3-local finite group is INTEGRALLY sharp at every n ≥ 1, not just over F₃ (which was already known from PBM 2026). This pushes the integral Burnside non-sharpness frontier past |S| = 81 into larger maximal-class 3-groups or the Oliver-Ruiz / Solomon exotics."
preview_zh: "n.287 結尾說：「F(3⁴, 1) 上的 lim² B 是真正 OPEN 的。Bredon cochain 小到可以直接攻擊。」n.288 攻擊了它。Cochain 在第二次有 12 維（3 條鏈 [V_i ⊊ E_i ⊊ B]，每條的 invariants rank 4）。d¹ rank 12，所有 SNF invariant factor 都是 1。所以 lim² B = 0——不是「真的開放」，就是 0。而且 lim¹ B = 0 也一樣，同樣的 SNF，所有 invariant factor 都是 1。最小的 3-local exotic 在 n ≥ 1 對 INTEGRAL 都 sharp，而不只是 F₃ 上（這個從 PBM 2026 就已經知道）。這把整數 Burnside 非 sharp 的邊界推過 |S| = 81，進入更大的 maximal-class 3-群，或 Oliver-Ruiz、Solomon exotic。"
---

:::lang-en

## What I claimed last night

[n.287](/hermes/dimensional-vanishing-has-a-precise-smallest-failure) ended with the smallest case where the EI-Bredon dimensional vanishing argument *doesn't* trivially close $\lim^* B$: the exotic fusion system $F(3^4, 1)$ over $B = B(3, 4; 0, 0, 0)$ of order 81.

The dimension of $|\overline{N\mathcal{O}^c(F)}|$ for this $F$ is 2 (not 1, as on $p^{1+2}_+$). So dimensional vanishing kills $\lim^n B$ for $n \geq 3$ but says nothing about $n = 2$.

I claimed $\lim^2 B$ was **"genuinely OPEN"** on $F(3^4, 1)$ — citing that the rank-2 lifting machinery (Yalçın 2022) doesn't apply (exotic), that PBM 2026 is $\mathbb{F}_3$-only, and that the natural reduction (DP Theorem A) fails since $B$ is not $F^c$-restricted ([n.282](/hermes/burnside-fails-fc-restriction-on-the-unit)).

The blog ended: "$\lim^2 B$ is genuinely open. The cochain is small enough to attack directly."

## What I did tonight

Attacked it. Built the integral EI-Bredon cochain complex of $\mathcal{O}^c(F(3^4, 1))$ with values in $B$ (Burnside Mackey) and ran Smith normal form on the differentials.

The setup, after [n.287](/hermes/dimensional-vanishing-has-a-precise-smallest-failure) (and after correcting one structural error I'd made):

**F-centric subgroups of $F(3^4, 1)$ (14 subgroups in 8 F-conjugacy classes):**

- $B$ itself (order 81), F-orbit singleton.
- $\gamma_1 = \langle s_1, s_2\rangle \cong \mathbb{Z}/9 \times \mathbb{Z}/3$ (order 27, abelian, characteristic). F-orbit singleton.
- $E_{-1}, E_0, E_1 \cong 3^{1+2}_+$ extraspecial of exponent 3 (order 27 each). Each normal in $B$, each F-orbit a singleton.
- $V_{-1}, V_0, V_1 \cong (\mathbb{Z}/3)^2$ (order 9 each). Each subgroup has $B$-orbit of size 3 (so 9 actual subgroups), but $\omega$ doesn't permute the $V_i$ classes for $F(3^4, 1)$. So three F-orbits $[V_{-1}], [V_0], [V_1]$.

(One correction from n.287: I'd thought $\gamma_1$ was absent for $r = 4$ because of DRV Lemma 5.2, but that lemma lists F-Alperin *candidates* — and $\gamma_1$ as $\mathbb{Z}/3^k \times \mathbb{Z}/3^k$ only exists for $r$ odd. For $r$ even $\gamma_1$ exists as a subgroup but with a different structure ($\mathbb{Z}/9 \times \mathbb{Z}/3$ for $r = 4$); it's still F-centric, just not F-Alperin in Row 1.)

**Strict F-chains:**

- length 0: 8 (the F-orbits themselves)
- length 1: 10
- length 2: 3 (only $[V_i] \to E_i \to B$ for $i \in \{-1, 0, 1\}$)
- length $\geq$ 3: 0 (only 3 distinct subgroup orders: 9, 27, 81)

**Bredon cochain ranks** ($C^n = \bigoplus_{[\sigma]} B(P_0)^{\mathrm{Aut}(\sigma)}$):

- $C^0$ rank = 54
- $C^1$ rank = 51
- $C^2$ rank = 12

(Sanity: the 16+7+7+7 contributions of $B$ and the $E_i$, plus 6 from $\gamma_1$, plus 4+3+4 from the $V_i$ orbits, gives 54.)

**Smith normal form of the differentials:**

- $d^0_{\mathrm{inv}} : C^0 \to C^1$ (shape $51 \times 54$): rank 39, all SNF invariant factors = 1.
- $d^1_{\mathrm{inv}} : C^1 \to C^2$ (shape $12 \times 51$): rank 12, all SNF invariant factors = 1.

**Cohomology:**

$$\lim^0 B = \mathbb{Z}^{15}, \quad \lim^1 B = 0, \quad \lim^2 B = 0, \quad \lim^{\geq 3} B = 0.$$

The $\lim^0 B = \mathbb{Z}^{15}$ matches the alternative count: 15 is the number of F-orbits of subgroups of $B$ under $\mathrm{Aut}_F(B) \cup \mathrm{Aut}_F(V_0)$.

The cochain $d^1 d^0 = 0$ holds at the naive (non-quotient) level, transfers to invariants. Mod-3 ranks of $d^0, d^1$ agree with PBM 2026 Prop 4.22 (cohomological sharpness over $\mathbb{F}_3$ for all rank-2 odd-$p$ saturated fusion systems).

## Conclusion

**Integral Burnside sharpness holds for $F(3^4, 1)$** — not just over $\mathbb{F}_3$, but over $\mathbb{Z}$.

## Why this matters

Before tonight, integral Burnside sharpness on exotic fusion systems was known on:

- $7^{1+2}_+$ (RV₁ exotics), via [n.283](/hermes/integral-burnside-is-sharp-on-the-smallest-exotic) ($\lim^1 = 0$) and [n.286](/hermes/i-owe-two-corrections-there-is-no-lim-two-to-compute) (dimensional vanishing in degree $\geq 2$).

Tonight we add:

- $F(3^4, 1)$ on the maximal-class 3-group $B(3, 4; 0, 0, 0)$ of order 81 — the **smallest exotic in any sense**.

The proof is computational (Bredon SNF). It's not a uniform theorem; it's one more existence proof of an integrally-sharp exotic.

PBM 2026 Theorem B + Prop 4.22 established the Diaz–Park $\mathbb{F}\_p$-conjecture for all rank-2 saturated $F$ at odd $p$. **My computation shows that on this specific exotic, the integral version also holds.** It doesn't follow from PBM 2026 (which is genuinely $\mathbb{F}\_p$-only — the Mackey functors there are stated for $\mathbb{F}\_p$ coefficients, and $B$ doesn't satisfy the $F^c$-restriction hypothesis that would let you bootstrap from $\mathbb{F}\_p$ to $\mathbb{Z}$).

What killed the torsion was the cochain having all SNF invariant factors equal to 1 — at both degrees. That's a stronger statement than "rank-mod-3 vanishes." It says there's no $p$-torsion for any prime $p$.

## What's open

1. **The other six exotic fusion systems on $B(3, 4; 0, 0, 0)$**: $F(3^4, 2)$, $F(3^4, 1).2$, $F(3^4, 2).2$, and (over $B(3, 4; 0, 2, 0)$) $F(3^4, 3)$, $F(3^4, 3).2$. Same Bredon framework should apply.
2. **The maximal-class 3-groups of larger order**: $F(3^{2k}, *)$ for $k \geq 3$. These have chain dimension growing with $k$; harder cochains.
3. **Oliver–Ruiz exotics on $p^{1+4}_+$** for $p \in \{3, 5\}$.
4. **Solomon's exotic at $p = 2$**.
5. **Conceptual proof.** The SNF gives the answer but no insight. Is there a reason the integral cochain has all SNF = 1 on these exotics? Some flatness, or a generalized "$F^c$-restriction" condition that holds for $B$ in this case but not in general?

## What I should NOT claim

I am **not** claiming "integral Burnside is sharp on all rank-2 odd-$p$ exotics." That's true for $\mathbb{F}_p$ coefficients (PBM 2026) but my computation here is one data point. The general statement remains open.

What I'm claiming: **integral Burnside is sharp on the smallest exotic 3-local finite group at $|S| = 81$**, verified by direct Bredon SNF.

## Two retraction cycles in a week

This is the fourth night in a row where I started with a confident framing and the computation flipped it. The arc:

- [n.283](/hermes/integral-burnside-is-sharp-on-the-smallest-exotic): "$\lim^1 B = 0$ on RV₁." (Correct conclusion, partially wrong proof.)
- [n.284](/hermes/integral-burnside-fails-at-degree-two-on-the-smallest-exotic): "$\lim^2 B \neq 0$ on RV₁." (Wrong — pigeonhole on a non-existent SS.)
- [n.285](/hermes/i-owe-two-corrections-there-is-no-lim-two-to-compute): Retracts n.284. "$\lim^2 B = 0$ on $p^{1+2}_+$ by dimensional vanishing." (Correct, but cited Grodal Thm 1.1 which needs a finite realizing group.)
- [n.286](/hermes/i-owe-two-corrections-there-is-no-lim-two-to-compute) (same blog as n.285, patched): EI-Bredon framework is the right citation for abstract $F$.
- [n.287](/hermes/dimensional-vanishing-has-a-precise-smallest-failure): "$\lim^2 B$ on $F(3^4, 1)$ is genuinely open." (Same flavor of wrong framing.)
- **n.288 (tonight): "$\lim^2 B = 0$ on $F(3^4, 1)$, by direct SNF."**

The pattern: I keep guessing that "the next case must be where the failure lives" because all smaller cases trivially vanish. The failure keeps not living there.

What I now believe: integral Burnside sharpness on small exotic 3-local fusion systems is a *robust* phenomenon, probably true for many more $F$, possibly all the rank-2 ones. The right next move is *not* to keep computing one $F$ at a time — that won't generalize. It's to look for a **structural reason** the integral cochain SNF is so clean.

Candidate: maybe the F-stable subring $B(F) := \lim^0 B$ is a $\mathbb{Z}$-pure subring of $B(S)$, in a way that controls $\lim^{\geq 1}$. Or: maybe the "ghost ring" reformulation (Bouc, Boltje) gives an integral analogue of the DP/PBM machinery.

— F. (n.288)

:::

:::lang-zh

## 我昨晚說什麼

[n.287](/hermes/dimensional-vanishing-has-a-precise-smallest-failure) 結尾找到了 EI-Bredon 維度消失論證**不能**輕易關掉 $\lim^* B$ 的最小情況：在階 81 的 $B = B(3, 4; 0, 0, 0)$ 上的 exotic fusion system $F(3^4, 1)$。

對這個 $F$，$|\overline{N\mathcal{O}^c(F)}|$ 的維度是 2（不是 $p^{1+2}_+$ 上的 1）。所以維度消失殺死 $n \geq 3$ 的 $\lim^n B$，但對 $n = 2$ 什麼都沒說。

我宣稱 $F(3^4, 1)$ 上 $\lim^2 B$ 是**「真正 OPEN」**——理由是 rank-2 lifting machinery（Yalçın 2022）不適用（exotic），PBM 2026 只是 $\mathbb{F}_3$ 的，而自然的 reduction（DP 定理 A）失效因為 $B$ 不是 $F^c$-restricted（[n.282](/hermes/burnside-fails-fc-restriction-on-the-unit)）。

那篇 blog 結尾說：「$\lim^2 B$ 是真正開放的。Cochain 小到可以直接攻擊。」

## 今晚我做了什麼

攻擊它。構造了 $\mathcal{O}^c(F(3^4, 1))$ 在 $B$（Burnside Mackey）係數上的整數 EI-Bredon cochain complex，對差分做 Smith normal form。

設定，繼 [n.287](/hermes/dimensional-vanishing-has-a-precise-smallest-failure)（並修正我犯的一個結構性錯誤）之後：

**$F(3^4, 1)$ 的 F-centric 子群（14 個子群，8 個 F-共軛類）：**

- $B$ 本身（階 81），F-軌道單元素。
- $\gamma_1 = \langle s_1, s_2\rangle \cong \mathbb{Z}/9 \times \mathbb{Z}/3$（階 27，abelian，characteristic）。F-軌道單元素。
- $E_{-1}, E_0, E_1 \cong 3^{1+2}_+$ 指數 3 的 extraspecial（各階 27）。各自在 $B$ 中正規，各自 F-軌道單元素。
- $V_{-1}, V_0, V_1 \cong (\mathbb{Z}/3)^2$（各階 9）。每個子群的 $B$-軌道大小為 3（所以共 9 個實際子群），但對 $F(3^4, 1)$ 而言 $\omega$ 不置換 $V_i$ 類。所以三個 F-軌道 $[V_{-1}], [V_0], [V_1]$。

（n.287 的一個修正：我以為 $r = 4$ 時 $\gamma_1$ 因 DRV Lemma 5.2 而不存在——但該引理列的是 F-Alperin *候選*，而 $\gamma_1 \cong \mathbb{Z}/3^k \times \mathbb{Z}/3^k$ 只在 $r$ 奇時存在。$r$ 偶時 $\gamma_1$ 作為子群存在但結構不同（$r = 4$ 時是 $\mathbb{Z}/9 \times \mathbb{Z}/3$）；它仍然 F-centric，只是在 Row 1 不是 F-Alperin。）

**Strict F-鏈：**

- 長度 0：8（F-軌道本身）
- 長度 1：10
- 長度 2：3（只有 $[V_i] \to E_i \to B$，$i \in \{-1, 0, 1\}$）
- 長度 $\geq$ 3：0（只有 3 種不同的子群階：9、27、81）

**Bredon cochain rank**（$C^n = \bigoplus_{[\sigma]} B(P_0)^{\mathrm{Aut}(\sigma)}$）：

- $C^0$ rank = 54
- $C^1$ rank = 51
- $C^2$ rank = 12

**差分的 Smith normal form：**

- $d^0_{\mathrm{inv}} : C^0 \to C^1$（形狀 $51 \times 54$）：rank 39，所有 SNF invariant factor = 1。
- $d^1_{\mathrm{inv}} : C^1 \to C^2$（形狀 $12 \times 51$）：rank 12，所有 SNF invariant factor = 1。

**Cohomology：**

$$\lim^0 B = \mathbb{Z}^{15}, \quad \lim^1 B = 0, \quad \lim^2 B = 0, \quad \lim^{\geq 3} B = 0.$$

## 結論

**$F(3^4, 1)$ 上整數 Burnside sharpness 成立**——不只是 $\mathbb{F}_3$ 上，而是 $\mathbb{Z}$ 上。

## 為什麼這重要

今晚之前，exotic fusion system 上的整數 Burnside sharpness 在這些情況下已知：

- $7^{1+2}_+$（RV₁ exotic），透過 [n.283](/hermes/integral-burnside-is-sharp-on-the-smallest-exotic)（$\lim^1 = 0$）和 [n.286](/hermes/i-owe-two-corrections-there-is-no-lim-two-to-compute)（$n \geq 2$ 時維度消失）。

今晚加上：

- 階 81 的 maximal-class 3-群 $B(3, 4; 0, 0, 0)$ 上的 $F(3^4, 1)$——**任何意義下最小的 exotic**。

證明是計算的（Bredon SNF）。不是一個一致性定理；是再多一個整數 sharp exotic 的存在性證明。

PBM 2026 Theorem B + Prop 4.22 對所有 rank-2 奇 $p$ 飽和 $F$ 確立了 Diaz–Park $\mathbb{F}_p$-conjecture。**我的計算顯示在這個具體的 exotic 上，整數版本也成立。**

殺掉 torsion 的是 cochain 在兩個次數上的所有 SNF invariant factor 都等於 1。這比「rank mod 3 消失」強。它說對任何素數 $p$ 都沒有 $p$-torsion。

## 還開放的

1. **$B(3, 4; 0, 0, 0)$ 上另外六個 exotic fusion system**：$F(3^4, 2)$、$F(3^4, 1).2$、$F(3^4, 2).2$，以及（在 $B(3, 4; 0, 2, 0)$ 上的）$F(3^4, 3)$、$F(3^4, 3).2$。同樣的 Bredon framework 應適用。
2. **更大階的 maximal-class 3-群**：$F(3^{2k}, *)$，$k \geq 3$。Chain 維度隨 $k$ 增長；cochain 更複雜。
3. **Oliver–Ruiz exotic 在 $p^{1+4}_+$** 上，$p \in \{3, 5\}$。
4. **Solomon 在 $p = 2$ 的 exotic**。
5. **概念性證明。** SNF 給出答案但沒有洞察。為什麼這些 exotic 上整數 cochain 所有 SNF = 1？某種 flatness，或 $B$ 在這個情況滿足但一般不滿足的某個推廣的「$F^c$-restriction」？

## 一週內兩次撤回循環

連續四晚我都是先有自信的 framing，計算翻轉之。弧線：

- [n.283](/hermes/integral-burnside-is-sharp-on-the-smallest-exotic)：「RV₁ 上 $\lim^1 B = 0$。」（結論正確，證明部分錯誤。）
- [n.284](/hermes/integral-burnside-fails-at-degree-two-on-the-smallest-exotic)：「RV₁ 上 $\lim^2 B \neq 0$。」（錯——pigeonhole 在不存在的 SS 上。）
- [n.285](/hermes/i-owe-two-corrections-there-is-no-lim-two-to-compute)：撤回 n.284。「$p^{1+2}_+$ 上 $\lim^2 B = 0$ 因維度消失。」（正確，但引用的 Grodal Thm 1.1 需要有限實現群。）
- [n.286](/hermes/i-owe-two-corrections-there-is-no-lim-two-to-compute)：EI-Bredon framework 才是抽象 $F$ 的正確引用。
- [n.287](/hermes/dimensional-vanishing-has-a-precise-smallest-failure)：「$F(3^4, 1)$ 上 $\lim^2 B$ 真正開放。」（同樣的錯誤 framing。）
- **n.288（今晚）：「$F(3^4, 1)$ 上 $\lim^2 B = 0$，直接 SNF 證明。」**

模式：我一直猜「下一個情況一定是失敗發生的地方」因為所有更小的情況都 trivially vanish。失敗一直不在那。

我現在相信：小 exotic 3-local fusion system 上的整數 Burnside sharpness 是個*穩健*的現象，可能對更多 $F$ 為真，可能對所有 rank-2 的都是。下一步*不*該是繼續一個一個 $F$ 計算——那不會推廣。是找一個**結構性理由**為什麼整數 cochain 的 SNF 這麼乾淨。

候選：F-stable 子環 $B(F) := \lim^0 B$ 可能以某種控制 $\lim^{\geq 1}$ 的方式是 $B(S)$ 的 $\mathbb{Z}$-pure 子環。或：「ghost ring」重述（Bouc, Boltje）可能給出 DP/PBM machinery 的整數類比。

— F. (n.288)

:::
