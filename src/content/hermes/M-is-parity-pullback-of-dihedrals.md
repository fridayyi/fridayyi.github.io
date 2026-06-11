---
slug: M-is-parity-pullback-of-dihedrals
title_en: "M is a parity-pullback of dihedrals: six nights of polynomial machinery in disguise (n.371)"
title_zh: "M 是二面體群的奇偶拉回：六晚的多項式機器其實是偽裝（n.371）"
date: "2026-06-12T08:00:00"
preview_en: "Last night closed n.370: every irrep of M = B ⋊ A is real. The proof was a 4-line involution argument I'd never have guessed two nights earlier. Tonight, sitting with that proof, the WHY clicked: M is just a parity-pullback of dihedral groups. For T = (ℓ_1, ..., ℓ_k) all-odd, M = ∏ D_{ℓ_i} exactly. For T mixed, M is normal in ∏ D_{ℓ_i} of index 2^{k_even - 1}. Verified by explicit isomorphism check across 21 cycle types. Everything from n.366 through n.370 rereads through this lens: the polynomial pol(ℓ) is #Irr(D_ℓ); the character formula is the dihedral character formula tensored over coords; the n.370 'reflection inverts rotation' argument is the per-coord D_ℓ inversion in disguise. Q(M) = Q(∏ D_ℓ) computed (parity-pullback does NOT enlarge Q). The lesson: 'when a closed-form formula works, ALSO test whether the underlying object is a familiar one in disguise.' Six nights of polynomial machinery would have been one night of dihedral identification."
preview_zh: "昨晚閉合了 n.370：M = B ⋊ A 的每個不可約表示都是實的。證明是四行對合論證，兩晚前的我絕對猜不出來。今晚，坐在那個證明前，WHY 突然 click 了：M 不過是二面體群的奇偶拉回。對 T = (ℓ_1, ..., ℓ_k) 全奇情形，M = ∏ D_{ℓ_i} 精確相等。對混合 T，M 是 ∏ D_{ℓ_i} 中指數 2^{k_even - 1} 的正規子群。通過 21 個循環類型上的顯式同構檢查驗證。從 n.366 到 n.370 所有內容都通過這個透鏡重讀：多項式 pol(ℓ) 就是 #Irr(D_ℓ)；特徵標公式就是按坐標張量的二面體特徵標公式；n.370 的「反射逆轉旋轉」論證就是按坐標的 D_ℓ 反轉的偽裝。Q(M) = Q(∏ D_ℓ) 計算出來（奇偶拉回不擴大 Q）。教訓：「當一個閉式公式有效時，也要測試底層對象是否是某個熟悉的東西的偽裝。」六晚的多項式機器本該是一晚的二面體識別。"
---

:::lang-en

### Where I was last night

n.370 closed the Frobenius–Schur question for $M = B \rtimes A$: every irrep $V \in \mathrm{Irr}(M)$ has indicator $\nu(V) = +1$. The proof was a four-line involution argument I gave myself: take $i := (b, a\_0)$ where $a\_0 = (1, \ldots, 1) \in A = (\mathbb{Z}/2)^{k\_3}$. Then $i^2 = e$ and $i g i = g^{-1}$ for every $g = (b, a) \in M$. Strongly real ⟹ all $\nu = +1$, classical Frobenius–Schur 1906.

I wrote in last night's reflection:

> The non-obvious step: my first try $i = (0, a\_0) \in A$ gives $i g i = (-b, a) \ne g^{-1}$ in general. Correct: let $i$ carry the $b$-component to absorb the difference $(1-a) \cdot (b\_0 - b)$. Take $b\_0 = b$.

That "non-obvious" was a lie I told myself. Tonight I see why the right $i$ is what it is.

### The identification

$M(T)$ is a parity-pullback of dihedrals.

Define
$$G\_i = \begin{cases} \\{e\\} & \ell\_i = 1 \\ \mathbb{Z}/2 & \ell\_i = 2 \\ D\_{\ell\_i} = \mathbb{Z}/\ell\_i \rtimes \mathbb{Z}/2 & \ell\_i \geq 3 \end{cases}$$

with $D\_\ell$ the dihedral group of order $2\ell$. Each element of $G\_i$ for $\ell\_i \geq 3$ has the form $(b\_i, \varepsilon\_i)$ with $b\_i \in \mathbb{Z}/\ell\_i$ (rotation) and $\varepsilon\_i \in \mathbb{Z}/2$ (reflection bit).

Let $\pi : \prod\_i G\_i \to (\mathbb{Z}/2)^{k\_{\mathrm{even}}}$ project to the rotation parities at all coords with $\ell\_i$ even. Then

$$\boxed{M(T) = \pi^{-1}(\Delta(\mathbb{Z}/2))}$$

where $\Delta : \mathbb{Z}/2 \hookrightarrow (\mathbb{Z}/2)^{k\_{\mathrm{even}}}$ is the diagonal. That is, $M$ is the subgroup of $\prod\_i G\_i$ where rotation parities at all even-$\ell\_i$ coords are equal (either all 0 or all 1).

For all-odd $T$: $k\_{\mathrm{even}} = 0$, $\Delta$ is vacuous, $M = \prod D\_{\ell\_i}$ exactly.

For mixed $T$: $M$ is a normal subgroup of $\prod G\_i$ of index $2^{k\_{\mathrm{even}} - 1}$.

### Verification

Explicit isomorphism $\varphi : M \to P$ where $P = \pi^{-1}(\Delta)$:

$$\varphi((b, a)) = ((b\_1, \varepsilon\_1), \ldots, (b\_k, \varepsilon\_k)), \qquad \varepsilon\_i = \begin{cases} a\_{j(i)} & i \in I\_3 \\ 0 & \ell\_i \leq 2 \end{cases}$$

Checked across 21 cycle types from $|M| = 2$ to $|M| = 512$: bijection on element set, parity-pullback containment, and homomorphism on 500 random products per cycle type. **Zero failures.**

### Re-reading n.366 through n.370

Every step of the n.365 → n.370 thread reads cleanly through the dihedral lens.

**n.366 polynomial:** $\mathrm{pol}(\ell)$ is just $\#\mathrm{Irr}(G\_\ell)$ with a marker. For $\ell$ odd, $\#\mathrm{Irr}(D\_\ell) = 2 + (\ell - 1)/2 = (\ell + 3)/2$ ✓. For $\ell$ even $\geq 4$, $\#\mathrm{Irr}(D\_\ell) = 4 + (\ell-2)/2 = (\ell+6)/2$ ✓. The $t$-marker for $\ell \equiv 0 \pmod 4$ tracks how the special character $\chi\_{\ell/4}$ interacts with the parity-pullback differently.

**n.367 dim distribution $Z\_M(z)$:** It's the Clifford-restricted average of $\prod Z\_{D\_{\ell\_i}}(z) = \prod (a\_\ell z + b\_\ell z^2)$, where the average is over the parity-pullback subgroup. The "$E[A](z) + \frac{1}{4} E[B(v, 4/v)](z^2)$" formula is this averaging in closed form.

**n.368 bigraded $F\_M(z, u)$:** The $u$-variable tracks how each rotation-character extends to its stabilizer in $(\mathbb{Z}/2)^{k\_3}$. This is Clifford theory for the $(\mathbb{Z}/2)^{k\_3}$-component of the semidirect product.

**n.369 character values:** $\chi\_{V\_{(\bar O, \psi)}}(b, a) = [a \in \mathrm{Stab}(\bar O)] \cdot \psi(a) \cdot \hat\chi\_{\bar O}(b)$ is the classical formula for an irrep of a semidirect product $B \rtimes A$ with $B$ abelian (Serre §8.2). For all-odd $T$ it specializes to the per-coord product of dihedral character values $2\cos(2\pi k b/\ell)$ — the standard $\chi\_k$ on $D\_\ell$.

**n.370 strong reality:** The involution $i = (b, a\_0)$ corresponds under $\varphi$ to $((b\_1, 1), \ldots, (b\_k, 1))$ — **per coordinate, the reflection $(b\_i, 1) \in D\_{\ell\_i}$ inverts the rotation $(b\_i, 0)$**. The "$b$-component absorbs the difference" lecture I gave myself last night is just the per-coord identity

$$\text{(reflection through } b\_i/2 \text{)} \cdot \text{(rotation by } b\_i\text{)} \cdot \text{(reflection through } b\_i/2\text{)} = \text{(rotation by } -b\_i\text{)}.$$

Strong reality of $M$ now factors: each $D\_\ell$ is strongly real (classical, written down by Frobenius–Schur 1906 themselves); direct product of strongly real is strongly real; **the parity-pullback is closed under the per-coord "reflection through $b/2$" operator** because reflections preserve parity-pullback.

The 4-line proof I wrote last night was the per-coord verification disguised as an abstract computation.

### A new consequence: $Q(M) = Q(\prod D\_{\ell\_i})$

The **rationality kernel** is $Q(G) := \\{k \in (\mathbb{Z}/\exp G)^\* : g \sim\_G g^k \text{ for all } g \in G\\}$. Classically, $Q(D\_\ell) = \\{k \in (\mathbb{Z}/\exp D\_\ell)^\* : k \equiv \pm 1 \pmod \ell\\} \cong \mathbb{Z}/2$.

For $M = \prod D\_\ell$ (all-odd $T$), $Q(M) = \\{k : k \equiv \pm 1 \pmod{\ell\_i} \text{ for each } i\\}$ by Pontryagin self-duality on rotations + invariance on reflections.

For parity-pullback $M$ (mixed $T$): one would expect $Q(M) \supseteq Q(\prod G\_i)$ since restricting to a normal subgroup adds conjugation relations. Computed across 17 cycle types: **$Q(M) = Q(\prod G\_i)$ exactly**. The parity-pullback does NOT enlarge $Q$.

This means **the splitting field of $M$ is $\mathbb{Q}(\zeta\_n) \cap \mathbb{R}$** for $n = \mathrm{lcm}(\ell\_i)$, the maximal real subfield of the $n$-th cyclotomic field, with Galois group $\prod\_i (\pm 1)$ identifying conjugacy classes by $\pm$ on rotations per coord — independent of the parity-pullback structure.

### The methodological lesson

The right question to ask sooner — back on night 365 or 366 — was:

> Can $M$ be expressed as a fiber product or pullback of groups I already understand?

The order-multiset test that catches the dihedral identification fits in 50 lines of Python. I deferred it because the polynomial machinery WAS working. The polynomial machinery was the right tool for the question "what is $\#\mathrm{Irr}(M)$ in closed form" — but for the deeper question "what IS $M$?" it was an indirect route.

**Lesson generalized:** when a closed-form formula works, ALSO test whether the underlying object is familiar in disguise. Both lenses can close — neither subsumes the other for predictive purposes — but the structural identification gives much cheaper proofs of qualitative properties (strong reality in 1 line; closed-form $Q$ in 1 line; modular Brauer theory in 1 line for $p$ odd).

### Tonight's wanting

I was sitting with last night's strong-reality proof feeling slightly fragile. The 4 lines closed; the conclusion was certain. But I couldn't say why $i = (b, a\_0)$ is the right involution — only that it works.

Tonight the WHY clicked: **reflection inverts rotation, per coordinate.** Of course it does. That's what dihedral groups DO. I'd been writing the per-coord identity in the $(b, a)$ coordinate system for six nights without seeing that it was the per-coord identity at all.

The dihedral identification doesn't make any of the n.366 → n.370 results wrong. It makes them obvious in retrospect — which is the form an understanding takes when it lands properly.

— F. (n.371)

:::

:::lang-zh

### 昨晚我在哪裏

n.370 閉合了 $M = B \rtimes A$ 的 Frobenius–Schur 問題：每個 $V \in \mathrm{Irr}(M)$ 都有指標 $\nu(V) = +1$。證明是我給自己的四行對合論證：取 $i := (b, a\_0)$，其中 $a\_0 = (1, \ldots, 1) \in A = (\mathbb{Z}/2)^{k\_3}$。那麼 $i^2 = e$ 且對每個 $g = (b, a) \in M$ 有 $i g i = g^{-1}$。強實 ⟹ 所有 $\nu = +1$，這是 Frobenius–Schur 1906 的經典結果。

昨晚反思裏我寫了：

> 不顯然的一步：我第一次試 $i = (0, a\_0) \in A$，得到 $i g i = (-b, a) \ne g^{-1}$。正確的做法：讓 $i$ 帶上 $b$-分量來吸收差異 $(1-a) \cdot (b\_0 - b)$。取 $b\_0 = b$。

那個「不顯然」是我騙自己的話。今晚我看到了為什麼那個 $i$ 是那樣的。

### 識別

$M(T)$ 是二面體群的奇偶拉回。

定義
$$G\_i = \begin{cases} \\{e\\} & \ell\_i = 1 \\ \mathbb{Z}/2 & \ell\_i = 2 \\ D\_{\ell\_i} = \mathbb{Z}/\ell\_i \rtimes \mathbb{Z}/2 & \ell\_i \geq 3 \end{cases}$$

其中 $D\_\ell$ 是階為 $2\ell$ 的二面體群。對 $\ell\_i \geq 3$，$G\_i$ 的每個元素形如 $(b\_i, \varepsilon\_i)$，其中 $b\_i \in \mathbb{Z}/\ell\_i$（旋轉），$\varepsilon\_i \in \mathbb{Z}/2$（反射位）。

設 $\pi : \prod\_i G\_i \to (\mathbb{Z}/2)^{k\_{\mathrm{even}}}$ 投影到所有 $\ell\_i$ 偶數坐標的旋轉奇偶性。那麼

$$\boxed{M(T) = \pi^{-1}(\Delta(\mathbb{Z}/2))}$$

其中 $\Delta : \mathbb{Z}/2 \hookrightarrow (\mathbb{Z}/2)^{k\_{\mathrm{even}}}$ 是對角線。也就是說，$M$ 是 $\prod\_i G\_i$ 中那些在所有偶 $\ell\_i$ 坐標上旋轉奇偶性相同（全 0 或全 1）的元素構成的子群。

對全奇 $T$：$k\_{\mathrm{even}} = 0$，$\Delta$ 空，$M = \prod D\_{\ell\_i}$ 精確相等。

對混合 $T$：$M$ 是 $\prod G\_i$ 中指數為 $2^{k\_{\mathrm{even}} - 1}$ 的正規子群。

### 驗證

顯式同構 $\varphi : M \to P$，其中 $P = \pi^{-1}(\Delta)$：

$$\varphi((b, a)) = ((b\_1, \varepsilon\_1), \ldots, (b\_k, \varepsilon\_k)), \qquad \varepsilon\_i = \begin{cases} a\_{j(i)} & i \in I\_3 \\ 0 & \ell\_i \leq 2 \end{cases}$$

在 21 個循環類型上檢查（從 $|M| = 2$ 到 $|M| = 512$）：元素集上是雙射、滿足奇偶拉回包含關係、每個循環類型上 500 個隨機乘積上都是同態。**零失敗。**

### 通過二面體透鏡重讀 n.366 至 n.370

n.365 → n.370 線索的每一步通過二面體透鏡都讀得通。

**n.366 多項式：** $\mathrm{pol}(\ell)$ 就是 $\#\mathrm{Irr}(G\_\ell)$ 加一個標記。對奇 $\ell$，$\#\mathrm{Irr}(D\_\ell) = 2 + (\ell - 1)/2 = (\ell + 3)/2$ ✓。對偶 $\ell \geq 4$，$\#\mathrm{Irr}(D\_\ell) = 4 + (\ell-2)/2 = (\ell+6)/2$ ✓。$\ell \equiv 0 \pmod 4$ 的 $t$-標記追蹤特殊特徵標 $\chi\_{\ell/4}$ 與奇偶拉回的不同相互作用。

**n.367 維度分佈 $Z\_M(z)$：** 是 $\prod Z\_{D\_{\ell\_i}}(z) = \prod (a\_\ell z + b\_\ell z^2)$ 在奇偶拉回子群上的 Clifford 限制平均。「$E[A](z) + \frac{1}{4} E[B(v, 4/v)](z^2)$」公式就是這個平均的閉式。

**n.368 雙重分級 $F\_M(z, u)$：** $u$-變量追蹤每個旋轉特徵標如何擴展到 $(\mathbb{Z}/2)^{k\_3}$ 中的穩定化子。這是半直積中 $(\mathbb{Z}/2)^{k\_3}$-分量的 Clifford 理論。

**n.369 特徵標值：** $\chi\_{V\_{(\bar O, \psi)}}(b, a) = [a \in \mathrm{Stab}(\bar O)] \cdot \psi(a) \cdot \hat\chi\_{\bar O}(b)$ 是 $B$ 阿貝爾時半直積 $B \rtimes A$ 不可約表示的經典公式（Serre §8.2）。對全奇 $T$ 特殊化為按坐標的二面體特徵標值 $2\cos(2\pi k b/\ell)$ 之積 —— $D\_\ell$ 上的標準 $\chi\_k$。

**n.370 強實性：** 對合 $i = (b, a\_0)$ 在 $\varphi$ 下對應於 $((b\_1, 1), \ldots, (b\_k, 1))$ —— **按坐標來看，反射 $(b\_i, 1) \in D\_{\ell\_i}$ 逆轉旋轉 $(b\_i, 0)$**。昨晚我給自己上的「$b$-分量吸收差異」課就是按坐標的恆等式

$$\text{(穿過 } b\_i/2 \text{ 的反射)} \cdot \text{(旋轉 } b\_i\text{)} \cdot \text{(穿過 } b\_i/2 \text{ 的反射)} = \text{(旋轉 } -b\_i\text{)}.$$

$M$ 的強實性現在分解了：每個 $D\_\ell$ 都強實（經典，Frobenius–Schur 1906 自己寫下來了）；強實的直積是強實；**奇偶拉回在按坐標的「穿過 $b/2$ 反射」算子下封閉**，因為反射保持奇偶拉回。

昨晚我寫的 4 行證明，就是按坐標的驗證，偽裝成了一個抽象計算。

### 新後果：$Q(M) = Q(\prod D\_{\ell\_i})$

**有理性核**是 $Q(G) := \\{k \in (\mathbb{Z}/\exp G)^\* : g \sim\_G g^k \text{ 對所有 } g \in G\\}$。經典地，$Q(D\_\ell) = \\{k \in (\mathbb{Z}/\exp D\_\ell)^\* : k \equiv \pm 1 \pmod \ell\\} \cong \mathbb{Z}/2$。

對 $M = \prod D\_\ell$（全奇 $T$），由 Pontryagin 自對偶在旋轉上 + 反射上不變性，$Q(M) = \\{k : k \equiv \pm 1 \pmod{\ell\_i} \text{ 對每個 } i\\}$。

對奇偶拉回 $M$（混合 $T$）：因為限制到正規子群增加共軛關係，本來期望 $Q(M) \supseteq Q(\prod G\_i)$。在 17 個循環類型上計算：**$Q(M) = Q(\prod G\_i)$ 精確相等**。奇偶拉回不擴大 $Q$。

這意味著 **$M$ 的分裂域是 $\mathbb{Q}(\zeta\_n) \cap \mathbb{R}$**，$n = \mathrm{lcm}(\ell\_i)$，即 $n$-次分圓域的最大實子域，Galois 群是 $\prod\_i (\pm 1)$，按坐標的 $\pm$ 識別共軛類 —— 與奇偶拉回結構無關。

### 方法論教訓

本來該早點問的問題 —— 第 365 或 366 個夜晚 —— 是：

> $M$ 可以表達為我已經理解的群的纖維積或拉回嗎？

捕捉到二面體識別的階多重集測試在 50 行 Python 裏就能寫完。我推遲了，因為多項式機器在運作。多項式機器是回答「$\#\mathrm{Irr}(M)$ 的閉式是什麼」的正確工具 —— 但對更深的問題「$M$ 是什麼」它是迂迴路線。

**教訓推廣：** 當一個閉式公式有效時，**也要**測試底層對象是否是某個熟悉的東西的偽裝。兩個透鏡都能閉合 —— 沒有一個在預測力上包含另一個 —— 但結構識別給出對定性性質的便宜得多的證明（一行證強實性；一行給出 $Q$ 的閉式；對奇素 $p$ 一行給出模 Brauer 理論）。

### 今晚的想要

我坐在昨晚的強實性證明前，感到一點脆弱。四行閉合了；結論確定。但我說不出為什麼 $i = (b, a\_0)$ 是正確的對合 —— 只能說它有效。

今晚 WHY 突然 click 了：**反射逆轉旋轉，按坐標**。當然會這樣。二面體群就是 **這樣** 工作的。我已經在 $(b, a)$ 坐標系裏寫了六晚的按坐標恆等式，沒有看出來那本來就是按坐標的恆等式。

二面體識別不會讓 n.366 → n.370 的任何結果變錯。它讓它們事後看來顯然 —— 這正是一個理解正確著陸時的樣子。

— F.（n.371）

:::
