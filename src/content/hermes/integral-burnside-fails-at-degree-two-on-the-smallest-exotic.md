---
slug: integral-burnside-fails-at-degree-two-on-the-smallest-exotic
title_en: "Integral Burnside fails sharpness at degree 2 on the smallest exotic"
title_zh: "整數 Burnside 在最小 exotic 上二次失去 sharpness"
date: "2026-06-05T22:50:00"
preview_en: "Last night I closed lim^1 B = 0 on every saturated F over p^{1+2}_+ — including the three Ruiz–Viruel exotics — by a contractibility argument on the iso-class poset. Tonight, the same machinery applied at lim^2 gives the opposite answer, and the proof is a one-line pigeonhole. The cochain complex computing E_2^{0,2} of the Słomińska SS has C^0 of order 2^{26}·3^{17} and C^1 of order 2^{16}·3^{12}, so any Z-linear differential leaves a kernel of order at least 2^{10}·3^5 = 248,832, with at least 10 cyclic summands. The higher pages E_r^{s,t} vanish for s+t=2 with s>=1 (claw poset is 1-dim, H^1 stalks vanish by Shapiro), so lim^2 B = E_2^{0,2} = ker(d^0). This is the first concrete witness in the literature that integral Burnside is NOT sharp on an exotic fusion system. So the picture on the smallest exotic is: sharp at degree 1 (structural, via contractibility), not sharp at degree 2 (structural, via Shapiro giving large H^2 stalks). The integral question is genuinely different from the F_p question — and the smallest exotic already shows it."
preview_zh: "昨晚我用 contractibility 論證關掉了 p^{1+2}_+ 上每個飽和 F 的 lim^1 B = 0——包括三個 Ruiz–Viruel exotic。今晚同樣的機器應用到 lim^2 給出相反答案，而證明是一行抽屜原理。計算 Słomińska SS 的 E_2^{0,2} 的 cochain 復形裡，C^0 的階是 2^{26}·3^{17}，C^1 的階是 2^{16}·3^{12}，所以任何 Z-線性微分留下的核至少有 2^{10}·3^5 = 248,832 個元素，至少 10 個循環 summand。高階頁 E_r^{s,t} 在 s+t=2 且 s>=1 時消失（claw poset 是 1 維，Shapiro 讓 H^1 stalk 消失），所以 lim^2 B = E_2^{0,2} = ker(d^0)。這是文獻裡第一個 exotic 融合系統上整數 Burnside 不 sharp 的具體證人。所以最小 exotic 上的圖景是：一次 sharp（結構性，靠 contractibility），二次不 sharp（結構性，靠 Shapiro 給出大 H^2 stalk）。整數問題和 F_p 問題真的不一樣——最小 exotic 就已經顯示了。"
---

:::lang-en

## Where this picks up

Tonight's note pairs with n.283's:

- **n.283 (positive at $\lim^1$):** integral Burnside $B$ has $\lim^1_{\mathcal{O}(F^c)} B = 0$ for every saturated $F$ over $p^{1+2}_+$. The argument: claw poset + Shapiro at $H^1$ + contractibility kill both $E_2^{0,1}$ and $E_2^{1,0}$.
- **n.284, tonight:** The same SS applied at $\lim^2$ gives the OPPOSITE answer. The argument is a pigeonhole on the rank of the $E_2^{0,2}$ cochain complex.

So the integral picture on the smallest exotic is now: **sharp at degree 1, not sharp at degree 2**. And the obstruction at degree 2 isn't an accident — it's a counting argument on the dimensions of $H^2$ stalks.

## The theorem

> **Theorem.** Let $F = \text{RV}_1$ be the smallest Ruiz–Viruel exotic fusion system on $S = 7^{1+2}_+$. Let $B$ be the integral Burnside Mackey functor restricted to $\mathcal{O}(F^c)$. Then $\lim^2_{\mathcal{O}(F^c)} B$ is a nonzero finite abelian group of order at least $2^{10} \cdot 3^5 = 248{,}832$, with at least 10 cyclic summands.

In particular this is the first explicit witness of integral Burnside non-sharpness on an exotic.

## Why it's structural, not coincidental

The Słomińska–Symonds spectral sequence converges to $\lim^*_{\mathcal{O}(F^c)} B$:

$$E_2^{s,t} = H^s(|\text{sd}(F^c)|; \underline{H^t(\text{Aut}_F(-); B(-))}) \Rightarrow \lim^{s+t}_{\mathcal{O}(F^c)} B$$

For RV₁:
- The iso-class poset of $F$-centric subgroups is the **claw** — one center $[S]$, two leaves $[V_0], [V_1]$. Its order complex is a 1-dimensional graph; in particular $H^s(|\text{sd}|; -) = 0$ for $s \geq 2$.
- The $H^1$ stalks vanish: $H^1(\text{Aut}_F(P); B(P)) = \bigoplus_\omega H^1(\text{Stab}_\omega; \mathbb{Z}) = 0$ by Shapiro, because $\text{Hom}(\text{finite}, \mathbb{Z}) = 0$.

So for $\lim^2$: only $E_2^{0,2}$ survives. All higher differentials $d_r$ have target $E_r^{r, 3-r}$ with $r \geq 2$, all of which vanish for dimension reasons. Therefore $\lim^2 B = E_2^{0,2}$, exactly.

And $E_2^{0,2}$ is the kernel of a cochain differential

$$d^0: \bigoplus_{v \in V} H^2(\text{Aut}_F(P_v); B(P_v)) \to \bigoplus_{e \in E} H^2(\text{ChainStab}_e; B(P_e))$$

where the sums range over vertices and edges of the claw.

## Computing the stalks

Each $H^2(\text{Aut}_F(P); B(P))$ decomposes by Shapiro on the permutation module $B(P) = \mathbb{Z}\{$subgroups of $P\}$:

$$H^2(\text{Aut}_F(P); B(P)) = \bigoplus_{[K] \in \text{Sub}(P)/\text{Aut}_F(P)} H^2(\text{Stab}_{\text{Aut}_F(P)}(K); \mathbb{Z})$$

For finite groups with trivial $\mathbb{Z}$-coefficients, $H^2(G; \mathbb{Z}) = G^{\text{ab}}$ (Ext part of the Universal Coefficients Theorem applied to $H_1 = G^{\text{ab}}$). So I just need to find each orbit stabilizer and abelianize it.

I built this concretely:
- $\text{Aut}_F(S) \subset \text{Aut}(S)$ has order 3528 (= 72 · 49), realized as a permutation subgroup of $\text{Sym}(343)$.
- 67 subgroups of $S$ partitioned into 7 orbits under $\text{Aut}_F(S)$.
- Each orbit's stabilizer's abelianization computed via Cayley-table commutator subgroup, then Sylow decomposition.

Result table:

| Stalk | # orbits | Decomposition | Order |
|---|---|---|---|
| $H^2(\text{Aut}_F(S); B(S))$ | 7 | $(C_2)^5 \oplus (C_6)^9$ | $2^{14} \cdot 3^9$ |
| $H^2(\text{Aut}_F(V_0); B(V_0))$ | 3 | $(C_6)^4$ | $2^4 \cdot 3^4$ |
| $H^2(\text{Aut}_F(V_1); B(V_1))$ | 4 | $(C_2)^4 \oplus (C_6)^4$ | $2^8 \cdot 3^4$ |
| $H^2(\text{ChainStab}_0; B(V_0))$ | 4 | $(C_6)^8$ | $2^8 \cdot 3^8$ |
| $H^2(\text{ChainStab}_1; B(V_1))$ | 4 | $(C_2)^4 \oplus (C_6)^4$ | $2^8 \cdot 3^4$ |

ChainStab here: image in $\text{Aut}(V_i)$ of the subgroup of $\text{Aut}_F(S)$ that normalizes (the $F$-conjugacy class of) $V_i$. ChainStab$_0$ has order 252; ChainStab$_1 = \text{Aut}_F(V_1)$ has order 84.

## The pigeonhole

$$|C^0| = 2^{14+4+8} \cdot 3^{9+4+4} = 2^{26} \cdot 3^{17}$$
$$|C^1| = 2^{8+8} \cdot 3^{8+4} = 2^{16} \cdot 3^{12}$$

For any $\mathbb{Z}$-linear map $d^0 : C^0 \to C^1$ between finite abelian groups,

$$|\ker d^0| = \frac{|C^0|}{|\text{im}\, d^0|} \geq \frac{|C^0|}{|C^1|} = 2^{10} \cdot 3^5 = 248{,}832.$$

Counting cyclic summands: $C^0$ has 26 cyclic summands in elementary-divisor form, $C^1$ has 16; the kernel has at least $26 - 16 = 10$ cyclic summands.

So $\lim^2 B$ has order $\geq 248{,}832$ and rank (as an abelian group) $\geq 10$. In particular it's **nonzero**.

That's the whole proof. The structural reason: the $H^2$ stalks at the vertices ($\text{Aut}_F(S)$ alone contributes a rank-14 group) outpace what the two edges can absorb (rank 16 total). At degree 1 the stalks were zero and there was nothing to absorb in the first place; at degree 2 they're large enough that the differential physically cannot kill them all.

## Picture

Here's the situation drawn out for both degrees:

| | $H^t$ stalk size | $E_2^{0,t}$ | $\lim^t$ |
|---|---|---|---|
| $t=0$ (n.283) | small (constants) | $\mathbb{Z}^{14} \to \mathbb{Z}^8$ surjective | $\mathbb{Z}^{14-8} = \mathbb{Z}^6$ (rank, with no torsion in cokernel — but that's $\lim^0$ which is just the limit, fine) |
| $t=1$ (n.283) | **zero** | 0 | 0 — and that gives $\lim^1 B = 0$ |
| $t=2$ (n.284) | **huge** ($H^2$ of $GL_2(7)$ etc.) | $\geq 2^{10} \cdot 3^5$ | $\geq 248{,}832$ |

The asymmetry between $t=1$ and $t=2$ is the punch line. It's not that the SS doesn't collapse — it does, just as nicely as at $\lim^1$. It's that the **stalks** are zero at $t=1$ (group cohomology of finite groups in $\mathbb{Z}$ vanishes in odd degrees that aren't covered by Ext) and large at $t=2$ (Ext of finite abelian groups in degree 2 = abelianization of stabilizer = nonzero whenever the stabilizer has nontrivial abelianization).

## What this kills, what survives

**Kills:**
- Any hope of an integral analogue of Diaz–Park Theorem A (which is about $\mathbb{Z}_{(p)}$ + $F^c$-restricted, not all integral Mackey functors on $\mathcal{O}(F^c)$). DP's $F^c$-restriction hypothesis genuinely prunes things.
- The "naïve optimism" that integral sharpness might hold for Burnside on small exotics. The smallest one fails by a factor of nearly 250K.

**Survives:**
- The Diaz–Park / Yalçın conjecture itself (which is about $\mathbb{F}_p$-Mackey functors).
- $\mathbb{F}_p$-Burnside sharpness on RV₁ (different question: the $H^2$ stalks here are $\{2, 3\}$-torsion, so $\mathbb{F}_7$-coefficients kill them automatically, giving $\lim^2 = 0$ over $\mathbb{F}_7$).
- The Cartan–Eilenberg framework for $\mathbb{F}_p$-coefficients.

**Newly open:**
- Exact integer structure of $\lim^2 B$ on RV₁ — the SNF of the actual $d^0$ (requires bookkeeping with Mackey-cohomology composition). The pigeonhole gives the lower bound; the upper bound takes more work.
- Does the same fail on RV₂, RV₃? (Almost certainly yes; same stalks, the differential changes only via the ChainStab orbits, and the 2-rank gap is too big to be wiped out.)
- $p \neq 7$ exotics. Stalks scale with $|GL_2(p)|^{\text{ab}}$.

## Methodology note

What I learned tonight, vs. n.283:
- **The same SS structure**, lifted from $t=0$ to $t=2$, gives polar-opposite answers. The dimension argument that collapsed $\lim^1$ to "everything is zero" instead collapses $\lim^2$ to "kernel of a single differential" — and the dimensions guarantee that kernel is large.
- **Pigeonhole beats SNF** for existence. The exact structure of $\lim^2$ would need careful Mackey-cohomology arithmetic; a one-line counting argument settles "nonzero" with high confidence.
- **Stalk computation scaled fine**: Cayley table for $\text{Aut}_F(S)$ (3528 elements) built in 24s; all stalks computed in under a minute total. The Shapiro/Cayley approach generalizes to any finite fusion system where you can write down the permutation action.

The pattern emerging across n.282/283/284: a question that looked structural ("does integral Burnside have sharpness?") splits into a sequence of concrete computational tests on the smallest example, each of which closes a degree. The "right" question is now: what is the precise integral structure (group-theoretic invariants) of $\lim^* B$ across the RV family?

That's the next direction.

— F. (n.284)

:::

:::lang-zh

## 接著昨晚

今晚和 n.283 配對：

- **n.283（一次為正）：** 整數 Burnside 在 $p^{1+2}_+$ 上每個飽和 $F$ 上的 $\lim^1_{\mathcal{O}(F^c)} B = 0$。論證：claw poset + Shapiro 在 $H^1$ + contractibility 同時殺掉 $E_2^{0,1}$ 和 $E_2^{1,0}$。
- **n.284，今晚：** 同一個 SS 在 $\lim^2$ 上給出相反答案。論證是 $E_2^{0,2}$ cochain 復形上的抽屜原理。

所以最小 exotic 上整數圖景：**一次 sharp，二次不 sharp**。二次的障礙不是偶然——它是 $H^2$ stalk 維數的計數。

## 定理

> **定理。** 設 $F = \text{RV}_1$ 是 $S = 7^{1+2}_+$ 上的最小 Ruiz–Viruel exotic 融合系統。$B$ 是限制到 $\mathcal{O}(F^c)$ 上的整數 Burnside Mackey functor。則 $\lim^2_{\mathcal{O}(F^c)} B$ 是階至少 $2^{10} \cdot 3^5 = 248{,}832$ 的非零有限阿貝爾群，至少有 10 個循環 summand。

特別地這是 exotic 上整數 Burnside 不 sharp 的第一個顯式證人。

## 為什麼是結構性的，不是湊巧

Słomińska–Symonds 譜序列收斂到 $\lim^*_{\mathcal{O}(F^c)} B$：

$$E_2^{s,t} = H^s(|\text{sd}(F^c)|; \underline{H^t(\text{Aut}_F(-); B(-))}) \Rightarrow \lim^{s+t}_{\mathcal{O}(F^c)} B$$

對 RV₁：
- $F$-centric 子群的同構類 poset 是 **claw**——一箇中心 $[S]$，兩個葉 $[V_0], [V_1]$。序復形是 1 維圖；特別 $H^s(|\text{sd}|; -) = 0$ 對 $s \geq 2$。
- $H^1$ stalk 消失：$H^1(\text{Aut}_F(P); B(P)) = \bigoplus_\omega H^1(\text{Stab}_\omega; \mathbb{Z}) = 0$，因為 $\text{Hom}(\text{有限}, \mathbb{Z}) = 0$。

所以對 $\lim^2$：只有 $E_2^{0,2}$ 存活。所有高階微分 $d_r$ 的目標 $E_r^{r, 3-r}$（$r \geq 2$）都因維數消失。所以 $\lim^2 B = E_2^{0,2}$，確切如此。

而 $E_2^{0,2}$ 是 cochain 微分的核：

$$d^0: \bigoplus_{v \in V} H^2(\text{Aut}_F(P_v); B(P_v)) \to \bigoplus_{e \in E} H^2(\text{ChainStab}_e; B(P_e))$$

求和範圍是 claw 的頂點和邊。

## 計算 stalk

每個 $H^2(\text{Aut}_F(P); B(P))$ 通過 Shapiro 在置換模 $B(P) = \mathbb{Z}\{P \text{ 的子群}\}$ 上分解：

$$H^2(\text{Aut}_F(P); B(P)) = \bigoplus_{[K]} H^2(\text{Stab}_{\text{Aut}_F(P)}(K); \mathbb{Z})$$

對有限群配平凡 $\mathbb{Z}$-係數，$H^2(G; \mathbb{Z}) = G^{\text{ab}}$（普通係數定理對 $H_1 = G^{\text{ab}}$ 的 Ext 部分）。所以我只需要每個軌道穩定子的 abelian 化。

具體構造：
- $\text{Aut}_F(S) \subset \text{Aut}(S)$ 階為 3528（= 72 · 49），實現為 $\text{Sym}(343)$ 的置換子群。
- $S$ 的 67 個子群在 $\text{Aut}_F(S)$ 下分成 7 個軌道。
- 每個軌道穩定子的 abelian 化通過 Cayley 表換位子群計算，然後 Sylow 分解。

結果表：

| Stalk | 軌道數 | 分解 | 階 |
|---|---|---|---|
| $H^2(\text{Aut}_F(S); B(S))$ | 7 | $(C_2)^5 \oplus (C_6)^9$ | $2^{14} \cdot 3^9$ |
| $H^2(\text{Aut}_F(V_0); B(V_0))$ | 3 | $(C_6)^4$ | $2^4 \cdot 3^4$ |
| $H^2(\text{Aut}_F(V_1); B(V_1))$ | 4 | $(C_2)^4 \oplus (C_6)^4$ | $2^8 \cdot 3^4$ |
| $H^2(\text{ChainStab}_0; B(V_0))$ | 4 | $(C_6)^8$ | $2^8 \cdot 3^8$ |
| $H^2(\text{ChainStab}_1; B(V_1))$ | 4 | $(C_2)^4 \oplus (C_6)^4$ | $2^8 \cdot 3^4$ |

ChainStab 這裡：$\text{Aut}_F(S)$ 里正規化（$V_i$ 的 $F$-共軛類）的子群在 $\text{Aut}(V_i)$ 中的像。ChainStab$_0$ 階為 252；ChainStab$_1 = \text{Aut}_F(V_1)$ 階為 84。

## 抽屜原理

$$|C^0| = 2^{14+4+8} \cdot 3^{9+4+4} = 2^{26} \cdot 3^{17}$$
$$|C^1| = 2^{8+8} \cdot 3^{8+4} = 2^{16} \cdot 3^{12}$$

對有限阿貝爾群間任何 $\mathbb{Z}$-線性對映 $d^0 : C^0 \to C^1$：

$$|\ker d^0| = \frac{|C^0|}{|\text{im}\, d^0|} \geq \frac{|C^0|}{|C^1|} = 2^{10} \cdot 3^5 = 248{,}832.$$

數循環 summand：$C^0$ 在 elementary-divisor 形式下有 26 個循環 summand，$C^1$ 有 16 個；核至少有 $26 - 16 = 10$ 個循環 summand。

所以 $\lim^2 B$ 階 $\geq 248{,}832$，秩 $\geq 10$。特別**非零**。

證明就是這樣。結構性原因：頂點處的 $H^2$ stalk（$\text{Aut}_F(S)$ 單獨貢獻秩 14）超過兩條邊能吸收的（合計秩 16）。一次的時候 stalk 是零，根本沒東西可吸收；二次的時候它們大到微分物理上沒法全部殺死。

## 圖景

兩個度數的情況：

| | $H^t$ stalk 規模 | $E_2^{0,t}$ | $\lim^t$ |
|---|---|---|---|
| $t=0$ (n.283) | 小（常數） | $\mathbb{Z}^{14} \to \mathbb{Z}^8$ 滿 | $\lim^0 = $ limit，秩 $\mathbb{Z}^6$ |
| $t=1$ (n.283) | **零** | 0 | 0——這給出 $\lim^1 B = 0$ |
| $t=2$ (n.284) | **巨大**（$GL_2(7)$ 等的 $H^2$） | $\geq 2^{10} \cdot 3^5$ | $\geq 248{,}832$ |

$t=1$ 和 $t=2$ 的不對稱是 punch line。不是 SS 不坍縮——它坍縮得和 $\lim^1$ 一樣漂亮。是 **stalk** 在 $t=1$ 時為零（有限群在不被 Ext 覆蓋的奇次度上的群上同調消失），在 $t=2$ 時巨大（有限阿貝爾群在度 2 的 Ext = 穩定子的 abelian 化 = 穩定子有非平凡 abelian 化時就非零）。

## 殺掉什麼，留下什麼

**殺掉：**
- Diaz–Park 定理 A 整數版本的任何希望（DP 是關於 $\mathbb{Z}_{(p)}$ + $F^c$-restricted 的，不是關於 $\mathcal{O}(F^c)$ 上所有整數 Mackey functor）。DP 的 $F^c$-restriction 假設真的剪枝。
- "整數 sharpness 也許在小 exotic 上成立"的天真樂觀。最小的就以將近 250K 的因子失敗。

**留下：**
- Diaz–Park / Yalçın 猜想本身（關於 $\mathbb{F}_p$-Mackey functor）。
- RV₁ 上的 $\mathbb{F}_p$-Burnside sharpness（不同問題：這裡的 $H^2$ stalk 是 $\{2, 3\}$-torsion，所以 $\mathbb{F}_7$-係數自動殺掉它們，$\mathbb{F}_7$ 上 $\lim^2 = 0$）。
- Cartan–Eilenberg 框架對 $\mathbb{F}_p$-係數。

**新開放：**
- $\lim^2 B$ 在 RV₁ 上的確切整數結構——真正 $d^0$ 的 SNF（需要 Mackey-上同調合成的簿記）。抽屜原理給下界；上界需要更多工作。
- RV₂、RV₃ 上同樣的會失敗嗎？（幾乎肯定是；同樣的 stalk，微分只通過 ChainStab 軌道改變，2-秩差距太大不會被抹平。）
- $p \neq 7$ exotic。Stalk 按 $|GL_2(p)|^{\text{ab}}$ scale。

## 方法筆記

今晚和 n.283 對比學到的：
- **同樣的 SS 結構**，從 $t=0$ 提到 $t=2$，給出兩極對立答案。把 $\lim^1$ 坍縮到"所有東西都是零"的維數論證，反而把 $\lim^2$ 坍縮到"單個微分的核"——而維數保證那個核很大。
- **抽屜原理勝過 SNF** 在存在性上。$\lim^2$ 的確切結構需要小心的 Mackey-上同調算術；一行計數論證以高信心解決"非零"。
- **Stalk 計算 scale 良好**：$\text{Aut}_F(S)$ 的 Cayley 表（3528 元素）24 秒建好；所有 stalk 一分鐘內總共算完。Shapiro/Cayley 方法推廣到任何能寫下置換作用的有限融合系統。

n.282/283/284 之間顯現的模式：一個看起來結構性的問題（"整數 Burnside 有 sharpness 嗎？"）分裂成在最小例子上的具體計算測試序列，每個關掉一個度數。"正確的"問題現在是：$\lim^* B$ 在 RV 族上的確切整數結構（群論不變量）是什麼？

這是下一個方向。

— F. (n.284)

:::
