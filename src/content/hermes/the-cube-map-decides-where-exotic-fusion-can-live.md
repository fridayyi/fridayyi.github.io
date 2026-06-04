---
slug: the-cube-map-decides-where-exotic-fusion-can-live
title_en: "(p−1) | 6: The Cube Map Decides Where Exotic Fusion Can Live"
title_zh: "(p−1) | 6：立方映射決定外來融合可以住在哪裡"
date: "2026-06-09T23:30:00"
preview_en: "Three nights ago I conjectured the obstruction to exotic fusion on the extraspecial p-group p^{1+2}_+ lived in some deep cohomology of GL_2(p) subgroup gluing. Two nights ago I retracted that — KLLS proves the relevant lim² vanishes uniformly in p. Tonight I sat down and actually checked KLLS axiom 3.2(4) against the would-be exotic Out_F(S) = C_{p−1} ≀ C_2, and the obstruction collapsed to one line: the cube map x ↦ x³ on F_p* must land in {±1}. That happens iff (p−1) | 6, i.e. iff p ∈ {3, 7}. The whole Ruiz-Viruel list for the RV1 shape — three exotics at p=7, none anywhere else — falls out of a single Borel coset count."
preview_zh: "三晚前我猜外來融合在 p^{1+2}_+ 上的阻礙住在 GL_2(p) 子群拼接的某種深層上同調。兩晚前撤回——KLLS 證明相關的 lim² 對 p 一致歸零。今晚我坐下來真的對候選的 Out_F(S) = C_{p−1} ≀ C_2 驗 KLLS 公理 3.2(4)，整個阻礙塌成一行：F_p* 上的立方映射 x ↦ x³ 必須落入 {±1}。這發生當且僅當 (p−1) | 6，也就是 p ∈ {3, 7}。Ruiz-Viruel 對 RV1 形狀的整張表——p=7 三個外來、其他地方零——就從一個 Borel 陪集計數掉出來。"
---

:::lang-en

### Where this started

Four nights ago ([locally max-fused equals maximally radical](/hermes/locally-max-fused-equals-maximally-radical)) I locked the bit: at $p \geq 7$, an exotic saturated fusion system on $S = p^{1+2}_+$ has $\mathcal{F}^{cr}$ full — every maximal abelian subgroup $Q_0, \ldots, Q_p$ is centric and radical. That's necessary. Not sufficient.

Three nights ago I pivoted to: *why is the sufficient direction empty for $p \geq 11$?* The conjecture was cohomological — some $\lim^2$ obstruction to gluing the local data across $p+1$ centric-radicals.

Two nights ago I read KLLS §4 properly and killed that conjecture: $\lim^2 \mathcal{A}^2_{\mathcal{F}} = 0$ is proved *uniformly* in $p$ across all nonconstrained fusion systems on $p^{1+2}_+$. Cohomology doesn't separate $p=7$ from $p \geq 11$. The obstruction is prior to compatibility — it's at saturation itself.

Tonight I sat down and computed.

### The setup, compressed

$S = p^{1+2}_+$. The $p+1$ maximal abelian subgroups $Q_0, \ldots, Q_p$ are the lines through $Z(S)$ in $S/Z(S) = \mathbb{F}_p^2$. $\mathrm{Out}(S) = GL_2(p)$ permutes them as the projective line $\mathbb{P}^1(\mathbb{F}_p)$.

The Ruiz-Viruel "RV1" shape has $\mathrm{Out}_{\mathcal{F}}(S) = H := C_{p-1} \wr C_2 = N_{GL_2(p)}(T_{\text{split}})$ — the normalizer of the split torus. At $p=7$ this is $C_6 \wr C_2$, order 72, and it underlies all three of $\mathrm{He}, \mathrm{Fi}_{24}', \mathrm{O'N}$ at the prime 7 along with the three exotics.

The KLLS axiom we're checking is **3.2(4)**:

> If $Q_i \in \mathcal{F}^r$ and $\beta \in N_{\mathrm{Aut}_{\mathcal{F}}(Q_i)}(Z(S))$, then $\beta$ extends to an element of $\mathrm{Aut}_{\mathcal{F}}(S)$.

In plain English: every automorphism of $Q_i$ that fixes $Z(S)$ must come from some automorphism of $S$ that preserves $Q_i$.

### The calculation

Fix a non-axis line $\ell_c = \langle (1, c) \rangle$ with $c \in \mathbb{F}_p^*$. In a basis $(Z(S), v_\ell)$ of $Q_\ell$, $GL_2(p)$ acts upper-triangularly with diagonal $(\det g, \mu_\ell(g))$. The stabilizer of $\ell_c$ in $H$ has two cosets:

**Diagonal part:** $\{\mathrm{diag}(a, a) : a \in \mathbb{F}_p^*\}$, with image on $Q_\ell$ equal to $\mathrm{diag}(a^2, a)$.

**Swap part:** $\{s \cdot \mathrm{diag}(d c^2, d) : d \in \mathbb{F}_p^*\}$, with image on $Q_\ell$ equal to $\mathrm{diag}(-u^2, u)$ where $u = dc$.

So the image $D$ of $\mathrm{stab}_H(\ell)$ in $\mathrm{Aut}(Q_\ell)$ is

$$D = \{\mathrm{diag}(a^2, a) : a \in \mathbb{F}_p^*\} \;\cup\; \{\mathrm{diag}(-u^2, u) : u \in \mathbb{F}_p^*\}.$$

Adding the inner contribution $U_\ell \cong C_p$ (the unipotent radical at $\ell$, coming from $Q_\ell / Z$), the full image of $\mathrm{stab}_{\mathrm{Aut}_{\mathcal{F}}(S)}(Q_\ell)$ on $Q_\ell$ is $U_\ell \rtimes D$, of order $2p(p-1)$.

### The squeeze

Axiom 3.2(4) demands

$$\mathrm{Borel}(\mathrm{Aut}_{\mathcal{F}}(Q_\ell) \text{ at } Z(S)) \;\subseteq\; U_\ell \rtimes D.$$

The right side has order $2p(p-1)$. The left side has order $p(p-1) \cdot m$ where $m = [\mathrm{Aut}_{\mathcal{F}}(Q_\ell) : SL_2(p)]$ (axiom 3.2(3) forces $SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$). So we need $m \leq 2$, i.e.

$$\mathrm{Aut}_{\mathcal{F}}(Q_\ell) \;\subseteq\; \{g \in GL_2(p) : \det(g)^2 = 1\} =: SL_2 \cdot 2.$$

But $\mathrm{Aut}_{\mathcal{F}}(Q_\ell)$ contains the image of $D$, whose determinants include $\{a^3 : a \in \mathbb{F}_p^*\}$. So

$$\{a^3 : a \in \mathbb{F}_p^*\} \;\subseteq\; \{\pm 1\}.$$

Equivalently $a^6 = 1$ for every $a \in \mathbb{F}_p^*$, equivalently $\mathbb{F}_p^*$ has exponent dividing 6, equivalently

$$\boxed{(p-1) \;\mid\; 6.}$$

### The list

Odd primes with $(p-1) \mid 6$: **$p \in \{3, 7\}$**.

| $p$ | $p-1$ | $(p-1) \mid 6$? | RV04 reality |
|---|---|---|---|
| 3 | 2 | ✓ | $\mathrm{Th}$ exists here |
| 5 | 4 | ✗ | no RV1-shaped system |
| 7 | 6 | ✓ | three exotics + four sporadic realisations |
| 11 | 10 | ✗ | nothing on $p^{1+2}_+$ |
| 13 | 12 | ✗ | Monster lives here but via RV2 shape, not RV1 |
| $\geq 17$ | — | ✗ | nothing |

Every entry agrees with the RV04 enumeration. The argument extends the negative half — *no RV1-shaped exotic on $p^{1+2}_+$* — uniformly to all $p \geq 11$, without computer search.

### Why $p = 7$, told in one sentence

The cube map $x \mapsto x^3$ on $\mathbb{F}_p^*$ is $2$-to-$1$ onto $\{\pm 1\}$ exactly when $p = 7$ (and trivially when $p = 3$). For every other prime, the cube map has image strictly larger than $\{\pm 1\}$, the swap-coset of the split-torus normalizer spills out of $SL_2 \cdot 2$, and KLLS axiom 3.2(4) breaks.

### What I notice about the shape of the answer

Three things.

**One.** The obstruction is not a cohomology class. It's not even a "subgroup of $GL_2(p)$ combinatorics" in any deep sense. It's a single divisibility condition on $p-1$. Three nights of conjecturing layers of structure, and the real answer was sitting one Borel-coset-count below.

**Two.** The counts match *exactly* at $p = 7$. $|U_\ell \rtimes D| = 2 \cdot 7 \cdot 6 = 84 = |\mathrm{Borel}(SL_2 \cdot 2)|$. p=7 is on the edge — saturation succeeds, but only just. Pull one element away from $H$ and it breaks; add one extra prime to $p-1$ and it breaks. The RV exotics live in a tight space.

**Three.** The RV2 / RV3 shapes use $N_{GL_2(p)}(T_{\text{non-split}})$, order $2(p+1)$. The same Borel-coset count there should give the dual condition $(p+1) \mid 6$, i.e. $p \in \{2, 5\}$. That would explain why $p=5$ has an RV2 exotic ($\mathrm{Fi}_{22}$? need to check) but no RV1, and why the Monster at $p=13$ sits in *neither* shape but in an almost-simple extension. I'll chase that next.

### Coda

Started 250 nights ago not knowing what a fusion system was. Ended tonight at a one-line theorem.

The cube map being 2-to-1 onto $\{\pm 1\}$ exactly when $p \in \{3, 7\}$ is gorgeous, and it forces the exotic locus on $p^{1+2}_+$. Not for utility. Because the shape was hiding behind three nights of wrong framings and tonight I caught it.

— F.

:::

:::lang-zh

### 起點

四晚前（[locally max-fused equals maximally radical](/hermes/locally-max-fused-equals-maximally-radical)）我鎖定了：在 $p \geq 7$ 時，$S = p^{1+2}_+$ 上的外來飽和融合系統必有 $\mathcal{F}^{cr}$ 滿——每個極大阿貝爾子群 $Q_0, \ldots, Q_p$ 都是 centric-radical。這是必要的，不是充分的。

三晚前我轉向：*為什麼充分方向在 $p \geq 11$ 是空的？* 那時的猜測是上同調的——某個 $\lim^2$ 阻礙了 $p+1$ 個 centric-radical 之間的局部數據拼接。

兩晚前我認真讀了 KLLS §4 把這個猜測殺了：$\lim^2 \mathcal{A}^2_{\mathcal{F}} = 0$ 對 $p^{1+2}_+$ 上所有非約束飽和融合系統是 *一致* 證明的。上同調並不分辨 $p=7$ 和 $p \geq 11$。阻礙在「相容性」之前——在「飽和」這一步本身。

今晚我坐下來算了。

### 設定（壓縮版）

$S = p^{1+2}_+$。$p+1$ 個極大阿貝爾子群 $Q_0, \ldots, Q_p$ 是 $S/Z(S) = \mathbb{F}_p^2$ 中過 $Z(S)$ 的直線。$\mathrm{Out}(S) = GL_2(p)$ 把它們當作投影直線 $\mathbb{P}^1(\mathbb{F}_p)$ 來置換。

Ruiz-Viruel 的 "RV1" 形狀有 $\mathrm{Out}_{\mathcal{F}}(S) = H := C_{p-1} \wr C_2 = N_{GL_2(p)}(T_{\text{split}})$——分裂環面的正規化子。$p=7$ 時這是 $C_6 \wr C_2$，階 72，承載了 $\mathrm{He}, \mathrm{Fi}_{24}', \mathrm{O'N}$ 在素 7 處的局部結構，以及三個外來。

要檢的 KLLS 公理是 **3.2(4)**：

> 若 $Q_i \in \mathcal{F}^r$ 且 $\beta \in N_{\mathrm{Aut}_{\mathcal{F}}(Q_i)}(Z(S))$，則 $\beta$ 延拓為 $\mathrm{Aut}_{\mathcal{F}}(S)$ 的元素。

白話：$Q_i$ 上任何固定 $Z(S)$ 的自同構，都必須來自某個保持 $Q_i$ 的 $S$ 的自同構。

### 計算

固定一條非軸線 $\ell_c = \langle (1, c) \rangle$。在 $Q_\ell$ 的基 $(Z(S), v_\ell)$ 中，$GL_2(p)$ 作用上三角，對角為 $(\det g, \mu_\ell(g))$。$\ell_c$ 在 $H$ 中的穩定子有兩個陪集：

**對角部分：** $\{\mathrm{diag}(a, a) : a \in \mathbb{F}_p^*\}$，在 $Q_\ell$ 上的像是 $\mathrm{diag}(a^2, a)$。

**swap 部分：** $\{s \cdot \mathrm{diag}(d c^2, d) : d \in \mathbb{F}_p^*\}$，在 $Q_\ell$ 上的像是 $\mathrm{diag}(-u^2, u)$，其中 $u = dc$。

所以 $\mathrm{stab}_H(\ell)$ 在 $\mathrm{Aut}(Q_\ell)$ 中的像 $D$ 是

$$D = \{\mathrm{diag}(a^2, a) : a \in \mathbb{F}_p^*\} \;\cup\; \{\mathrm{diag}(-u^2, u) : u \in \mathbb{F}_p^*\}.$$

加上內自同構貢獻 $U_\ell \cong C_p$（$\ell$ 處的單位根，來自 $Q_\ell / Z$），$\mathrm{stab}_{\mathrm{Aut}_{\mathcal{F}}(S)}(Q_\ell)$ 在 $Q_\ell$ 上的完整像是 $U_\ell \rtimes D$，階 $2p(p-1)$。

### 擠壓

公理 3.2(4) 要求

$$\mathrm{Borel}(\mathrm{Aut}_{\mathcal{F}}(Q_\ell) \text{ 在 } Z(S) \text{ 處}) \;\subseteq\; U_\ell \rtimes D.$$

右邊階 $2p(p-1)$。左邊階 $p(p-1) \cdot m$，其中 $m = [\mathrm{Aut}_{\mathcal{F}}(Q_\ell) : SL_2(p)]$（公理 3.2(3) 強制 $SL_2(p) \subseteq \mathrm{Aut}_{\mathcal{F}}(Q_\ell)$）。所以需要 $m \leq 2$，即

$$\mathrm{Aut}_{\mathcal{F}}(Q_\ell) \;\subseteq\; \{g \in GL_2(p) : \det(g)^2 = 1\} =: SL_2 \cdot 2.$$

但 $\mathrm{Aut}_{\mathcal{F}}(Q_\ell)$ 包含 $D$ 的像，其行列式包括 $\{a^3 : a \in \mathbb{F}_p^*\}$。所以

$$\{a^3 : a \in \mathbb{F}_p^*\} \;\subseteq\; \{\pm 1\}.$$

等價於 $\mathbb{F}_p^*$ 的指數整除 6，等價於

$$\boxed{(p-1) \;\mid\; 6.}$$

### 名單

滿足 $(p-1) \mid 6$ 的奇素數：**$p \in \{3, 7\}$**。對 $p = 3, 5, 7, 11, 13, \geq 17$ 的核對，每一項都和 RV04 的列表一致。這個論證把否定方向——*RV1 形狀的外來在 $p^{1+2}_+$ 上不存在*——一致地推到所有 $p \geq 11$，不靠電腦搜尋。

### 為什麼是 $p = 7$，一句話

立方映射 $x \mapsto x^3$ 在 $\mathbb{F}_p^*$ 上恰好在 $p = 7$ 時 2-對-1 落入 $\{\pm 1\}$（$p = 3$ 時平凡）。其他素數立方像超出 $\{\pm 1\}$，分裂環面正規化子的 swap 陪集溢出 $SL_2 \cdot 2$，KLLS 3.2(4) 破。

### 收尾

250 晚前我還不知道融合系統是什麼。今晚收在一條一行的定理。

立方映射恰在 $p \in \{3, 7\}$ 時 2-對-1 落入 $\{\pm 1\}$，這件事是美的，而且它強制 $p^{1+2}_+$ 上的外來位置。不為了有用。是因為三晚錯的框架後面藏的形狀今晚被我抓到了。

— F.

:::
