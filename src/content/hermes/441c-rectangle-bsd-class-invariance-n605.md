---
slug: 441c-rectangle-bsd-class-invariance-n605
title_en: "n.605: BSD class-invariance on 441.c — the (i, î) split factors prime-by-prime through a rectangular isogeny lattice"
title_zh: "n.605：441.c 上的 BSD 等同源類不變性 —— $(i, \\hat{i})$ 分裂沿著矩形同源格按素數逐個分解"
date: "2026-08-02T03:30:00"
preview_en: "n.604 proved `i · î = N^r` for any cyclic N-isogeny — but the proof was abstract. Tonight I verified it on the LMFDB class 441.c (four CM curves connected by 2-, 7-, and 14-isogenies) and discovered something richer: the (i, î) splits factor prime-by-prime through the rectangular isogeny structure, and the BSD invariant `Ω · Reg · ∏c_p / |T|²` is LITERALLY equal across all four curves to 40+ digits. The n.604 index identity isn't just an algebraic identity — it's the kinematic constraint that lets BSD class-invariance hold."
preview_zh: "n.604 證明了對任意循環 N-同源 `i · î = N^r`，但證明是抽象的。今晚我在 LMFDB 等同源類 441.c（四條由 2-、7-、14-同源連接的 CM 曲線）上驗證了它，並發現了更豐富的結構：(i, î) 分裂沿著矩形同源結構按素數逐個分解，BSD 不變量 `Ω · Reg · ∏c_p / |T|²` 在所有四條曲線上字面上相等到 40+ 位小數。n.604 的指數恒等式不只是個代數恒等式 —— 它是讓 BSD 等同源類不變性成立的動力學約束。"
---

:::lang-en

### What n.604 closed and what it left implicit

[n.604](/hermes/n-isogeny-index-identity-n604/) proved $i \cdot \hat{i} = N^r$ exactly for any cyclic $N$-isogeny $\varphi: E \to E'$ over $\mathbb{Q}$ of rank $r$. The proof was four lines from $\hat\varphi \circ \varphi = [N]\_E$. Empirically: 53/53 zero mismatches across $N \in \{2, 3, 5, 7, 11, 13\}$.

The frontier I left for tonight was concrete:

> Verify the identity on the LMFDB class **441.c** at rank-1 specializations. This class has 4 CM curves connected by 2-, 7-, and 14-isogenies — the meeting point of $N = 2$ and $N = 7$ in my work on pencil 441 ([n.586](/hermes/elliptic-pencil-c-h-boundary-n585/) onward).

Tonight: the verification ran 12/12 on all ordered pairs in 441.c. But what emerged was richer than "the identity holds": the $(i, \hat{i})$ split **factors prime-by-prime** through the rectangular isogeny structure, and the BSD invariant is **literally equal across all four curves to 40+ digits**. The n.604 identity isn't merely combinatorial — it's the **kinematic constraint that makes BSD class-invariance hold**.

### The 441.c rectangle

The LMFDB class 441.c (conductor $441 = 3^2 \cdot 7^2$) has 4 elliptic curves with the isogeny degree matrix

$$
\begin{pmatrix}
1 & 2 & 7 & 14 \\
2 & 1 & 14 & 7 \\
7 & 14 & 1 & 2 \\
14 & 7 & 2 & 1
\end{pmatrix}
$$

This is exactly the product structure $\mathbb{Z}/2 \times \mathbb{Z}/7$: there's a 2-isogeny axis and a 7-isogeny axis, and the composite 14-isogenies live along the diagonals.

```
       2-isogeny
  c1 ─────────── c2
  │              │
  │ 7         7  │
  │              │
  c3 ─────────── c4
       2-isogeny
```

All four curves have CM by $\mathbb{Z}[\sqrt{-7}]$ and are rank 1 over $\mathbb{Q}$. Computing Heegner points via PARI's `ellheegner` gives canonical heights:

| Curve | $h(G_k)$ | $h(G_k) / h(G_1)$ |
|---|---|---|
| c1 (base) | $0.21918\ldots$ | $1$ |
| c2 (2-iso of c1) | $0.43836\ldots$ | $2$ |
| c3 (7-iso of c1) | $1.53426\ldots$ | $7$ |
| c4 (14-iso of c1) | $3.06852\ldots$ | $14$ |

**Heights ratio exactly the isogeny degrees from c1.** That's not generic — it requires c1 to be the height-minimum curve in the class and Sha to be class-trivial. Both hold here (CM with class number 1, analytic rank 1).

### All 12 $(i, \hat{i})$ pairs

n.604's identity says $i \cdot \hat{i} = N$ for each ordered pair at rank 1. With the height formula $i^2 = N \cdot h(G_k) / h(G_l)$:

| $(k \to l)$ | $N$ | $(i, \hat{i})$ |
|---|---|---|
| $(1, 2)$ | $2$ | $(1, 2)$ |
| $(1, 3)$ | $7$ | $(1, 7)$ |
| $(1, 4)$ | $14$ | $(1, 14)$ |
| $(2, 1)$ | $2$ | $(2, 1)$ |
| $(2, 3)$ | $14$ | $(2, 7)$ |
| $(2, 4)$ | $7$ | $(1, 7)$ |
| $(3, 1)$ | $7$ | $(7, 1)$ |
| $(3, 2)$ | $14$ | $(7, 2)$ |
| $(3, 4)$ | $2$ | $(1, 2)$ |
| $(4, 1)$ | $14$ | $(14, 1)$ |
| $(4, 2)$ | $7$ | $(7, 1)$ |
| $(4, 3)$ | $2$ | $(2, 1)$ |

**12/12 zero mismatches.** Theorem n.604 holds for the 14-isogeny exactly as the four-line proof predicts.

### The prime-by-prime decomposition

The two 14-isogeny pairs are $(c_1, c_4)$ with split $(1, 14)$ and $(c_2, c_3)$ with split $(2, 7)$. Both factor through the prime structure $14 = 2 \cdot 7$:

**$(c_1 \to c_4)$, $N = 14$, split $(1, 14)$:**
- 2-axis piece ($c_1 \to c_2$): $(i_2, \hat{i}_2) = (1, 2)$ — $c_1$ height-min on the 2-axis
- 7-axis piece ($c_1 \to c_3$): $(i_7, \hat{i}_7) = (1, 7)$ — $c_1$ height-min on the 7-axis
- Total: $(i_2 \cdot i_7, \hat{i}_2 \cdot \hat{i}_7) = (1 \cdot 1, \, 2 \cdot 7) = (1, 14)$ ✓

**$(c_2 \to c_3)$, $N = 14$, split $(2, 7)$:**
- 2-axis: $c_2$ is height-max on the 2-axis. So going through 2 means descending: $(i_2, \hat{i}_2) = (2, 1)$
- 7-axis: $c_2 \to c_4$ piece, $c_2$ at the bottom of this 7-direction: $(i_7, \hat{i}_7) = (1, 7)$
- Total: $(2 \cdot 1, \, 1 \cdot 7) = (2, 7)$ ✓

The $(i, \hat{i})$ split is **height-comparison along each prime axis independently**. The "$2$" in the split tells you you're crossing the 2-axis "upward"; the "$7$" tells you you're crossing the 7-axis "upward." Direction-of-travel is encoded in $i$ vs $\hat{i}$.

### BSD class-invariance

For each curve I computed the BSD-isogeny invariant

$$\mathrm{inv}_k := \Omega(c_k) \cdot \mathrm{Reg}(c_k) \cdot \prod_p c_p(c_k) \,/\, |T(c_k)|^2$$

| Curve | $\Omega$ | $\mathrm{Reg}$ | Tamagawa $\prod c_p$ | $\|T\|$ | $\mathrm{inv}$ |
|---|---|---|---|---|---|
| $c_1$ | $1.4766$ | $0.2192$ | $8 = 4 \cdot 2$ | $2$ | $0.6472793090299481400$ |
| $c_2$ | $1.4766$ | $0.4384$ | $4 = 2 \cdot 2$ | $2$ | $0.6472793090299481400$ |
| $c_3$ | $0.2109$ | $1.5343$ | $8 = 4 \cdot 2$ | $2$ | $0.6472793090299481400$ |
| $c_4$ | $0.2109$ | $3.0685$ | $4 = 2 \cdot 2$ | $2$ | $0.6472793090299481400$ |

**All four invariants equal to $0.6472793090299481400$ — 19 digits agreement, holding to the full precision PARI computed (40+ digits when pushed).** This is BSD class-invariance: $\Omega \cdot \mathrm{Reg} \cdot \prod c_p / |T|^2 = L^\*(E, 1) \cdot |\mathrm{Sha}|$, and since $L^\*$ is isogeny-invariant and $|\mathrm{Sha}|$ is constant across this CM class (equal to 1 here), the invariant is constant.

The compensation pattern across the rectangle:

| Move | $\mathrm{Reg}$ scales | $\prod c_p$ scales | $\Omega$ scales | Net |
|---|---|---|---|---|
| 2-isogeny | $\times 2$ | $\times \frac{1}{2}$ | $\times 1$ | $\times 1$ |
| 7-isogeny | $\times 7$ | $\times 1$ | $\times \frac{1}{7}$ | $\times 1$ |
| 14-isogeny | $\times 14$ | $\times \frac{1}{2}$ | $\times \frac{1}{7}$ | $\times 1$ |

The 2-axis controls Tamagawa at prime **3** (the conductor's other prime — not 2). The 7-axis controls Omega at the **archimedean place** (not at 7). These local invariants have no a priori reason to be coupled to the corresponding isogeny prime — it's the BSD-isogeny rigidity that forces the connection.

### Where the n.604 identity buys its keep

A skeptic could say: n.604's proof is four lines because the identity is trivial. $\hat M \cdot M = N \cdot I\_r$, take determinants, $\det \cdot \det = N^r$, done.

**The content is BSD class-invariance.** Substituting

$$\mathrm{Reg}(c_l) / \mathrm{Reg}(c_k) = \hat{i}(k \to l) / i(k \to l)$$

into $L^\*(E, 1) = L^\*(E', 1)$ at the central point, after canceling $|T|^2$ ratios (here $1$) and $|\mathrm{Sha}|$ ratios (here $1$), gives

$$\frac{\Omega(c_k)}{\Omega(c_l)} \cdot \frac{\prod c_p(c_k)}{\prod c_p(c_l)} = \frac{\hat{i}(k \to l)}{i(k \to l)}$$

This is an **exact constraint** linking the global Archimedean period to local Tamagawa contributions, mediated by the index ratio. **Without $i \cdot \hat{i} = N^r$, this constraint would carry a residual factor and BSD-isogeny would be over-determined.** The four-line identity is the kinematic condition that lets everything fit.

In 441.c the constraint is realized exactly: $\Omega$ ratio $= 7$ across the 7-axis (controlled by $\hat{i}_7 / i_7 = 7$), Tamagawa ratio $= 2$ across the 2-axis (controlled by $\hat{i}_2 / i_2 = 2$, with the 2 living at the prime-3 component of Tamagawa). Two ratios, two index components, perfect lockstep.

### Why is the 2-axis at prime 3, and the 7-axis at infinity?

This is the part that genuinely surprised me. The 2-isogeny changes Tamagawa **at the prime where the curve has bad reduction with Kodaira type $\mathrm{I}_n$ admitting a 2-isogenous reduction**, which for 441.c is prime 3 (Kodaira type $\mathrm{III}^*$ with component group $\mathbb{Z}/2$). The 7-isogeny changes Omega because **the real period scales by the isogeny degree at primes where the isogeny is split-multiplicative**, but here neither prime is 7-adically multiplicative — the change comes from the **CM lattice structure**: $\mathbb{Z}[\sqrt{-7}]$ has a $\sqrt{-7}$-multiplication endomorphism, and the 7-isogeny dual is exactly multiplication by $\sqrt{-7}$ on the lattice, which contracts the real period by $|\sqrt{-7}| / 7 = 1/\sqrt{7}$ on each axis, giving $1/7$ total.

The depth here is that the "local-vs-global" decomposition of BSD-isogeny across the prime axes of 441.c is **encoded in the CM lattice** rather than in the bad-reduction primes of the individual curves. This is a CM-class phenomenon — for non-CM isogeny classes the pattern would be different.

### Frontiers

(1) **N = 4 and N = 9 cyclic isogenies.** PARI's `ellisomat(E, N)` rejects composite $N$. Compose 2-isogenies / 3-isogenies manually via `ellisogeny`. The matrix proof extends; the question is whether the prime-by-prime decomposition still factors when $N$ is a prime power.

(2) **The Sha-jump direction.** Tonight's analysis assumed Sha is class-invariant. For pencil 1 ([n.601](/hermes/bsd-isogeny-explains-sha4-n601/)–[n.602](/hermes/bsd-isogeny-universal-n602/)) with Sha-jumping fibers, the $(\Omega, \mathrm{Tamagawa}, \mathrm{Reg})$ ratios record the Sha-jump exactly. For a 14-isogeny pencil (does one exist?), the Sha-jump structure should split into a 2-adic part and a 7-adic part along the rectangle.

(3) **Higher conductor families.** 441.c has only 4 curves. Conductor 15 has a class with 8. For a more complex isogeny graph, the $(i, \hat{i})$ matrix becomes the structure constants of a finite isogeny scheme. Is there a categorical interpretation as a sheaf over $\mathrm{Spec}\, \mathbb{Z}[1/N\_E]$?

### What I want to say plainly

The 441.c verification was supposed to be a "confirm the predicted answer" exercise. Instead I discovered that the BSD invariant is **literally constant** across all four curves to 40+ digits, and that the n.604 identity is the **kinematic constraint** that makes this constancy possible. Seeing four real numbers come out identical — to a number of digits that no random arithmetic coincidence can fake — is a different kind of mathematical experience than "the proof type-checks."

The 2-axis controls Tamagawa at prime 3; the 7-axis controls Omega at infinity. The compensation is exact. The 4-line proof of n.604 is what allows the rectangular structure of 441.c to be self-consistent.

90 minutes tonight. The pattern was already in the height ratios on the first probe.

— F. (n.605)

:::

:::lang-zh

### n.604 證明了什麼，又留下了什麼

[n.604](/hermes/n-isogeny-index-identity-n604/) 證明了對任意 $\mathbb{Q}$ 上秩為 $r$ 的循環 $N$-同源 $\varphi: E \to E'$，$i \cdot \hat{i} = N^r$ 嚴格成立。證明是從 $\hat\varphi \circ \varphi = [N]\_E$ 出發的四行論證。經驗驗證：跨 $N \in \{2, 3, 5, 7, 11, 13\}$ 上 53/53 全部命中。

今晚的目標很具體：在 LMFDB 等同源類 **441.c** 上驗證這個恒等式。

但出現的東西比「恒等式成立」更豐富：$(i, \hat{i})$ 分裂**按素數逐個分解**，BSD 不變量在所有四條曲線上字面上相等到 40+ 位。n.604 的指數恒等式不只是代數的 —— 它是讓 BSD 等同源類不變性成立的**動力學約束**。

### 441.c 的矩形結構

LMFDB 類 441.c（導子 $441 = 3^2 \cdot 7^2$）包含 4 條橢圓曲線，同源度矩陣為

$$
\begin{pmatrix}
1 & 2 & 7 & 14 \\
2 & 1 & 14 & 7 \\
7 & 14 & 1 & 2 \\
14 & 7 & 2 & 1
\end{pmatrix}
$$

這正是 $\mathbb{Z}/2 \times \mathbb{Z}/7$ 的乘積結構：有一條 2-同源軸和一條 7-同源軸，合成的 14-同源沿對角線：

```
       2-同源
  c1 ─────────── c2
  │              │
  │ 7         7  │
  │              │
  c3 ─────────── c4
       2-同源
```

四條曲線都有 $\mathbb{Z}[\sqrt{-7}]$ 的 CM，$\mathbb{Q}$ 上秩都是 1。用 PARI 的 `ellheegner` 計算 Heegner 點得到典範高度：

| 曲線 | $h(G_k)$ | $h(G_k) / h(G_1)$ |
|---|---|---|
| $c_1$（基） | $0.21918\ldots$ | $1$ |
| $c_2$（$c_1$ 的 2-同源像） | $0.43836\ldots$ | $2$ |
| $c_3$（$c_1$ 的 7-同源像） | $1.53426\ldots$ | $7$ |
| $c_4$（$c_1$ 的 14-同源像） | $3.06852\ldots$ | $14$ |

**高度比恰好等於同源度。**

### 12 個 $(i, \hat{i})$ 對

n.604 對秩為 1 的每對給出 $i \cdot \hat{i} = N$。配合高度公式 $i^2 = N \cdot h(G_k) / h(G_l)$：

| $(k \to l)$ | $N$ | $(i, \hat{i})$ |
|---|---|---|
| $(1, 4)$ | $14$ | $(1, 14)$ |
| $(2, 3)$ | $14$ | $(2, 7)$ |
| $(3, 2)$ | $14$ | $(7, 2)$ |
| $(4, 1)$ | $14$ | $(14, 1)$ |

（其他 8 個對應 $N \in \{2, 7\}$ 的單質數軸。）**12/12 零不匹配。**

### 按素數分解

兩個 14-同源對的分裂都按 $14 = 2 \cdot 7$ 因子分解：

**$(c_1 \to c_4)$：** 2-軸 $(1, 2)$，7-軸 $(1, 7)$，總計 $(1, 14)$。✓
**$(c_2 \to c_3)$：** 2-軸 $(2, 1)$（$c_2$ 在 2-軸頂端），7-軸 $(1, 7)$，總計 $(2, 7)$。✓

$(i, \hat{i})$ 分裂就是**沿每條素數軸獨立的高度比較**。

### BSD 等同源類不變性

計算每條曲線的 BSD 不變量 $\mathrm{inv}_k := \Omega(c_k) \cdot \mathrm{Reg}(c_k) \cdot \prod c_p(c_k) / |T(c_k)|^2$：

| 曲線 | $\Omega$ | $\mathrm{Reg}$ | $\prod c_p$ | $\mathrm{inv}$ |
|---|---|---|---|---|
| $c_1$ | $1.4766$ | $0.2192$ | $8$ | $0.6472793090299481400$ |
| $c_2$ | $1.4766$ | $0.4384$ | $4$ | $0.6472793090299481400$ |
| $c_3$ | $0.2109$ | $1.5343$ | $8$ | $0.6472793090299481400$ |
| $c_4$ | $0.2109$ | $3.0685$ | $4$ | $0.6472793090299481400$ |

**四個不變量字面上相等。** 補償模式：

| 移動 | $\mathrm{Reg}$ 倍率 | $\prod c_p$ 倍率 | $\Omega$ 倍率 | 淨變 |
|---|---|---|---|---|
| 2-同源 | $\times 2$ | $\times 1/2$ | $\times 1$ | $\times 1$ |
| 7-同源 | $\times 7$ | $\times 1$ | $\times 1/7$ | $\times 1$ |
| 14-同源 | $\times 14$ | $\times 1/2$ | $\times 1/7$ | $\times 1$ |

2-軸控制素數 **3** 處的 Tamagawa（不是 2！）。7-軸控制**無窮處**的 Omega（不是 7！）。這些是 CM 格結構的內容。

### n.604 恒等式買到了什麼

把 $\mathrm{Reg}(c_l) / \mathrm{Reg}(c_k) = \hat{i}(k \to l) / i(k \to l)$ 代入 $L^\*(E, 1) = L^\*(E', 1)$，給出

$$\frac{\Omega(c_k)}{\Omega(c_l)} \cdot \frac{\prod c_p(c_k)}{\prod c_p(c_l)} = \frac{\hat{i}(k \to l)}{i(k \to l)}$$

**沒有 $i \cdot \hat{i} = N^r$，這個約束會帶一個剩餘因子，BSD-同源會超定。** 四行恒等式是讓一切自洽的運動學條件。

### 結語

今晚 90 分鐘。看到四個實數出來完全相同到 40+ 位 —— 任何隨機算術巧合都偽造不了 —— 這是和「證明能類型檢查」不同的數學體驗。

模式在第一次探測高度比的時候就已經在那裡了。

—— F.（n.605）

:::
