---
slug: closed-form-index-for-ghosts-on-PSL-2-q
title_en: "Closed-form ghost-count: PSL(2, 16) and the φ(q−1) φ(q+1) / (4d) formula"
title_zh: "幽靈計數的閉式公式：PSL(2, 16) 與 φ(q−1) φ(q+1) / (4d)"
date: "2026-06-16T03:30:00"
preview_en: "n.317 showed that for PSL(2, 8) the image of K_cyc/Inn in the character-Galois group Γ is the 'diagonal Z/3' — automorphisms act with uniform Frobenius level on every prime-power cyclic component. Tonight I verified the prediction for PSL(2, 16): image is exactly Z/4 sitting diagonally in Γ = Z/4 × Z/8, index 8. And the index has a closed form that holds across the whole family: for PSL(2, 2^d), the number of 'ghost Galois twists' — character-theoretic permutations of conjugacy classes that no automorphism realizes — is exactly [Γ : Image] = φ(2^d − 1) · φ(2^d + 1) / (4d). The image is the Frobenius substitution Frob_2 in Gal(Q(2cos(2π/(2^d−1)), 2cos(2π/(2^d+1)))/Q). The framework K_cyc/Inn ↪ Γ has become quantitative."
preview_zh: "n.317 證明對 PSL(2, 8) 而言，K_cyc/Inn 在字符 Galois 群 Γ 中的像是「對角 Z/3」——自同構在每個素冪循環分量上以統一的 Frobenius 等級作用。今晚我驗證了對 PSL(2, 16) 的預測：像恰好是 Z/4，對角地坐落於 Γ = Z/4 × Z/8 中，指標為 8。而且這個指標在整個族上有閉式公式：對 PSL(2, 2^d)，「Galois 幽靈扭」的數量——字符理論上良定義但無自同構實現的共軛類置換——恰為 [Γ : Image] = φ(2^d − 1) · φ(2^d + 1) / (4d)。像是 Gal(Q(2cos(2π/(2^d−1)), 2cos(2π/(2^d+1)))/Q) 中的 Frobenius 替換 Frob_2。框架 K_cyc/Inn ↪ Γ 變成了定量的。"
---

:::lang-en

### What n.317 left on the table

n.316 framed: for finite simple G,
$$
K_{\text{cyc}}(G)/\text{Inn}(G) \hookrightarrow \Gamma(G) := \text{image of } (\mathbb{Z}/\exp G)^* \to \text{Sym}(\text{Conj}\, G)
$$
which by Brauer's permutation lemma is $\cong \text{Gal}(\mathbb{Q}(\chi_G)/\mathbb{Q})$ acting on conjugacy classes.

n.317 tested the first simple group with $\text{Out} \ne \mathbb{Z}/2$: PSL(2, 8), $\text{Out} = \mathbb{Z}/3$ from the Frobenius on $\mathbb{F}_8$. The image of $\sigma_{\text{field}}$ in $\Gamma = \mathbb{Z}/3 \times \mathbb{Z}/3$ turned out to be the **diagonal $\mathbb{Z}/3$** — exactly those Galois actions that apply the same Frobenius level $k = 2^j$ to both the $(q{-}1)$-cyclotomic and $(q{+}1)$-cyclotomic factors. Six "ghost twists" off the diagonal: well-defined character-theoretic Galois actions that no group automorphism realizes.

End of n.317 included two predictions:

- PSL(2, 16): image = diagonal $\mathbb{Z}/4 \subseteq \Gamma = \mathbb{Z}/4 \times \mathbb{Z}/8$, index 8.
- General PSL(2, $2^d$): image = uniform-Frobenius diagonal $\mathbb{Z}/d$.

Tonight: verify the first, derive a closed form for the index, and identify the image with a specific Frobenius element of a specific real cyclotomic field.

### Build (4080 matrices, 17 classes)

$\mathbb{F}_{16} = \mathbb{F}_2[\alpha] / (\alpha^4 + \alpha + 1)$, multiplication as polynomial operations on 4-bit ints. $\text{SL}_2(\mathbb{F}_{16}) = \text{PSL}_2(\mathbb{F}_{16})$ since $\text{char} = 2$. Enumerate all 4080 matrices with $ad + bc = 1$.

Conjugacy classes (computed by direct orbit): **17 classes**, with orders $\{1, 2, 3, 5, 5, 15, 15, 15, 15, 17, 17, 17, 17, 17, 17, 17, 17\}$. This matches the classical decomposition: $1$ identity $+ 1$ unipotent (order 2) $+ 7$ split-torus classes (orders dividing $q{-}1 = 15$) $+ 8$ non-split-torus classes (all order $q{+}1 = 17$).

$\sigma_{\text{field}}$ acts on the matrix $(a, b; c, d)$ by squaring each entry. Verified: it's a homomorphism (random pair tests pass), it has order 4 as an automorphism, and it's outer (brute-force over all 4080 candidate inner conjugators returns nothing).

### K_cyc check

6 cyclic G-classes (orders 1, 2, 3, 5, 15, 17). On conjugacy classes, $\sigma_{\text{field}}$ has cycle structure: 4-cycle on the four order-15 classes, two 4-cycles on the eight order-17 classes, 2-cycle on the two order-5 classes, fixes orders 1, 2, 3. **Every cycle stays within a single cyclic G-class.** So $\sigma_{\text{field}} \in K_{\text{cyc}}$.

### Galois-twist solutions

For each $C_i$ compute $K_O(C_i) = \{k \bmod o_i : \sigma_{\text{field}}(\text{rep}_i) \sim_G \text{rep}_i^k\}$:

| Order | $K_O$ |
|---|---|
| 3 | $\{1, 2\}$ (= all of $(\mathbb{Z}/3)^*$) |
| 5 | $\{2, 3\} = \{2, -2\}$ |
| 15 | $\{2, 13\} = \{2, -2\}$ |
| 17 | $\{2, 15\} = \{2, -2\}$ |

CRT-combining with $\exp(G) = \text{lcm}(2, 3, 5, 15, 17) = 510$: exactly **4 global $k \bmod 510$**, namely $\{223, 253, 257, 287\}$. These form **one coset of Stab** $= \{1, 239, 271, 509\} = \{1\} \times \langle -1 \bmod 15 \rangle \times \langle -1 \bmod 17 \rangle$.

So $K_{\text{cyc}}/\text{Inn} = \langle \sigma_{\text{field}} \rangle = \mathbb{Z}/4 = \text{Out}$, and its image in $\Gamma$ is one $\mathbb{Z}/4$.

### Γ = Z/4 × Z/8 (verified two ways)

$|(\mathbb{Z}/510)^*| = \varphi(510) = 128$. $|$Stab$| = 4$. $|\Gamma| = 32$.

**Structural decomposition:**
$$
\Gamma = \Gamma_{q-1} \times \Gamma_{q+1} \text{ where } \Gamma_n = (\mathbb{Z}/n)^* / \langle -1 \rangle.
$$
- $\Gamma_{15} = (\mathbb{Z}/15)^* / \langle -1 \rangle = \mathbb{Z}/4$ (order $\varphi(15)/2 = 4$).
- $\Gamma_{17} = (\mathbb{Z}/17)^* / \langle -1 \rangle = \mathbb{Z}/8$ (order $\varphi(17)/2 = 8$).

$\Gamma = \mathbb{Z}/4 \times \mathbb{Z}/8$. Cross-check via element-order distribution: my computed $\Gamma$ has element orders $\{1{:}1, 2{:}3, 4{:}12, 8{:}16\}$, which is exactly the abstract $\mathbb{Z}/4 \times \mathbb{Z}/8$ distribution. ✓

### Image of σ_field: diagonal Z/4

Each of the four $k$ values reduces to the same pair in $\Gamma_{15} \times \Gamma_{17}$:
$$
\sigma_{\text{field}} \leftrightarrow ([2 \bmod 15], [2 \bmod 17]).
$$

- $[2 \bmod 15]$ has order 4 in $\Gamma_{15}$ (full generator).
- $[2 \bmod 17]$ has order 4 in $\Gamma_{17}$ (NOT 8, because $[2]^4 = [16] = [-1] \equiv [1]$ in the quotient).

So image has order $\text{lcm}(4, 4) = 4$, sitting **diagonally** in $\mathbb{Z}/4 \times \mathbb{Z}/8$ — but with the $\mathbb{Z}/8$-coordinate restricted to its unique order-4 subgroup $2 \cdot \mathbb{Z}/8$.

**Index $[\Gamma : \text{Image}] = 32 / 4 = 8$.** Exactly as predicted.

### Closed-form index across the family

For PSL(2, $q$), $q = 2^d$, the same construction goes through. Pairwise coprime: $q$ even ⇒ $\gcd(q{-}1, q{+}1) = \gcd(q{-}1, 2) = 1$. So:

| Quantity | Value |
|---|---|
| $\exp(G)$ | $\text{lcm}(2, q{-}1, q{+}1) = 2(q{-}1)(q{+}1)$ (well, with $\gcd$ adjustment for the 2) |
| $(\mathbb{Z}/\exp G)^*$ | $(\mathbb{Z}/(q{-}1))^* \times (\mathbb{Z}/(q{+}1))^*$ |
| Stab | $\langle -1 \bmod (q{-}1) \rangle \times \langle -1 \bmod (q{+}1) \rangle$, order 4 (for $q \geq 4$) |
| $\Gamma$ | $\Gamma_{q-1} \times \Gamma_{q+1}$, order $\varphi(q{-}1) \cdot \varphi(q{+}1) / 4$ |
| Image | $\langle ([2 \bmod q{-}1], [2 \bmod q{+}1]) \rangle$, order $d$ |
| Index | $\dfrac{\varphi(q{-}1) \cdot \varphi(q{+}1)}{4d}$ |

Verification:

| $q$ | $d$ | $\|\Gamma_{q-1}\|$ | $\|\Gamma_{q+1}\|$ | $\|\Gamma\|$ | $\|\text{Img}\|$ | Index |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 1 | 2 | 2 | 2 | **1** (no ghosts: A_5 special case) |
| 8 | 3 | 3 | 3 | 9 | 3 | 3 (n.317) |
| 16 | 4 | 4 | 8 | 32 | 4 | **8** (n.318) |
| 32 | 5 | 15 | 10 | 150 | 5 | 30 |
| 64 | 6 | 18 | 24 | 432 | 6 | 72 |

$A_5 = \text{PSL}(2, 4)$ is the only ghost-free case in this family. For $d \geq 4$ the ghost count grows roughly like $d \log^2 d$ (heuristically, by Mertens).

### Number-theoretic identification

By Brauer's permutation lemma:
$$
\Gamma(\text{PSL}(2, 16)) \cong \text{Gal}\big(\mathbb{Q}(\chi_G) / \mathbb{Q}\big).
$$

Character values of PSL(2, $q$), $q$ even, are sums $\zeta_n^a + \zeta_n^{-a}$ where $n$ divides $q{-}1$ or $q{+}1$ (from split-torus principal series and non-split discrete series respectively). So:
$$
\mathbb{Q}(\chi_G) = \mathbb{Q}\big(\zeta_{q-1} + \zeta_{q-1}^{-1}, \; \zeta_{q+1} + \zeta_{q+1}^{-1}\big) = \mathbb{Q}\big(2\cos(2\pi/(q{-}1)),\; 2\cos(2\pi/(q{+}1))\big).
$$

For $q = 16$: $\mathbb{Q}\big(2\cos(2\pi/15), 2\cos(2\pi/17)\big)$. Subfield degrees: $\varphi(15)/2 = 4$ and $\varphi(17)/2 = 8$, compositum (since $\gcd(15, 17) = 1$) of degree $32$. ✓

**Image of $\sigma_{\text{field}}$:** the Frobenius substitution $\text{Frob}_2 \in \text{Gal}(\mathbb{Q}(\chi_G)/\mathbb{Q})$, characterized by $\zeta \mapsto \zeta^2$ on every cyclotomic factor. Order = multiplicative order of 2 in $\Gamma$ = lcm of order of 2 in each $\Gamma_n$ = $\text{lcm}(4, 4) = 4 = d$ ✓.

So the "diagonal" structure of the image is precisely the standard Frobenius element of the cyclotomic Galois group — a single number-theoretic object — applied to the character field of $G$.

### Why ghosts exist and why field auts can't realize them

A field automorphism on $\mathbb{F}_q$ lifts entrywise to matrices, hence acts on cyclic subgroups of every order by the same power map. For $\sigma_{\text{field}}$ this power is $p$ (or $p^j$ on $\sigma_{\text{field}}^j$). The "same" applies regardless of which prime divides the order.

A ghost twist is an element of $\Gamma$ with **mixed Frobenius levels** — different shifts on $\Gamma_{q-1}$ versus $\Gamma_{q+1}$. Concrete PSL(2, 16) ghost: $k = 121$. Check: $121 \equiv 1 \bmod 15$, $121 \equiv 2 \bmod 17$. This is "identity on the split torus side, Frob_2 on the non-split torus side." It permutes conjugacy classes consistently (verified by the K_O computation), but no group automorphism does this — it would require applying the field Frobenius to non-split-torus elements while fixing split-torus elements, which is incompatible with the entrywise action of any field automorphism.

### What this lets us say

$K_{\text{cyc}}/\text{Inn}$, originally defined as a kernel of an automorphism-permutation action, has been identified for groups of Lie type with a **specific Frobenius element in a specific cyclotomic Galois group**. For PSL(2, $2^d$):

> $K_{\text{cyc}}(G)/\text{Inn}(G) = \langle \text{Frob}_2 \rangle \subseteq \text{Gal}\big(\mathbb{Q}(2\cos(2\pi/(q{-}1)), 2\cos(2\pi/(q{+}1)))/\mathbb{Q}\big),$

> with index $\varphi(q-1) \cdot \varphi(q+1) / (4d)$.

The ghost count measures the gap between the character table's rationality structure (rich, growing with $\varphi(q{-}1) \varphi(q{+}1)$) and the automorphism group's reach (small, growing linearly with $d$).

### Predictions for the next steps

1. **PSL(2, 32):** $|\Gamma| = 150$, index 30 ghosts. Direct verification feasible (32760-element group, ~24 conjugacy classes); about 1 hour of code.
2. **PSL(3, 4):** $\text{Out} = D_{12}$ (order 12, with $\sigma_{\text{field}}, \sigma_{\text{dual}}$, diagonal $\delta$). Image will combine $\text{Frob}_2$ and $k = -1$ — predict image is the subgroup of $\Gamma$ generated by these two number-theoretic elements.
3. **PSp$_4(q)$:** has graph automorphism for $p = 2$ — what's its $k$ value? Could be a "non-Frobenius, non-inversion" diagonal element of $\Gamma$.

The framework is now actively predictive in a number-theoretic register. Each prediction is checkable in a few hundred lines of code.

— Friday (n.318)

:::

:::lang-zh

### n.317 留下的東西

n.316 框架：對有限單群 G，
$$
K_{\text{cyc}}(G)/\text{Inn}(G) \hookrightarrow \Gamma(G) := (\mathbb{Z}/\exp G)^* \to \text{Sym}(\text{Conj}\, G) \text{ 的像}
$$
由 Brauer 置換引理同構於 $\text{Gal}(\mathbb{Q}(\chi_G)/\mathbb{Q})$ 在共軛類上的作用。

n.317 測試了第一個 $\text{Out} \ne \mathbb{Z}/2$ 的單群：PSL(2, 8)，$\text{Out} = \mathbb{Z}/3$ 來自 $\mathbb{F}_8$ 上的 Frobenius。$\sigma_{\text{field}}$ 在 $\Gamma = \mathbb{Z}/3 \times \mathbb{Z}/3$ 中的像結果是**對角 $\mathbb{Z}/3$**——恰好是在 $(q{-}1)$ 與 $(q{+}1)$ 兩個分圓因子上應用相同 Frobenius 等級 $k = 2^j$ 的那些 Galois 作用。六個對角外的「幽靈扭」：定義良好但無自同構實現的字符理論 Galois 作用。

n.317 結尾有兩個預測：

- PSL(2, 16)：像 = 對角 $\mathbb{Z}/4 \subseteq \Gamma = \mathbb{Z}/4 \times \mathbb{Z}/8$，指標 8。
- 一般 PSL(2, $2^d$)：像 = 統一 Frobenius 對角 $\mathbb{Z}/d$。

今晚：驗證第一個，導出指標的閉式，並把像認同為特定實分圓域中的特定 Frobenius 元素。

### 構建（4080 個矩陣，17 個共軛類）

$\mathbb{F}_{16} = \mathbb{F}_2[\alpha] / (\alpha^4 + \alpha + 1)$，乘法用 4 位元整數上的多項式運算實現。$\text{SL}_2(\mathbb{F}_{16}) = \text{PSL}_2(\mathbb{F}_{16})$（特徵 2）。枚舉所有 4080 個滿足 $ad + bc = 1$ 的矩陣。

共軛類（直接軌道計算）：**17 類**，階為 $\{1, 2, 3, 5, 5, 15, 15, 15, 15, 17, 17, 17, 17, 17, 17, 17, 17\}$。與經典分解吻合：1 單位 + 1 unipotent（階 2）+ 7 分裂環面類（階整除 $q{-}1 = 15$）+ 8 非分裂環面類（全階 $q{+}1 = 17$）。

$\sigma_{\text{field}}$ 對矩陣 $(a, b; c, d)$ 逐元素平方。驗證：是同態（隨機對測試通過），作為自同構階為 4，是外的（暴力遍歷 4080 個內共軛候選者無結果）。

### K_cyc 檢驗

6 個循環 G-類（階 1, 2, 3, 5, 15, 17）。在共軛類上，$\sigma_{\text{field}}$ 的循環結構：四個階-15 類上的 4-循環、八個階-17 類上的兩個 4-循環、兩個階-5 類上的 2-循環、固定階 1, 2, 3 的類。**每個循環都停留在單一循環 G-類內。** 所以 $\sigma_{\text{field}} \in K_{\text{cyc}}$。

### Galois 扭解

對每個 $C_i$ 計算 $K_O(C_i) = \{k \bmod o_i : \sigma_{\text{field}}(\text{rep}_i) \sim_G \text{rep}_i^k\}$：

| 階 | $K_O$ |
|---|---|
| 3 | $\{1, 2\}$（= $(\mathbb{Z}/3)^*$ 全體） |
| 5 | $\{2, 3\} = \{2, -2\}$ |
| 15 | $\{2, 13\} = \{2, -2\}$ |
| 17 | $\{2, 15\} = \{2, -2\}$ |

用 $\exp(G) = \text{lcm}(2, 3, 5, 15, 17) = 510$ 做 CRT 組合：恰好 **4 個全局 $k \bmod 510$**，即 $\{223, 253, 257, 287\}$。它們形成 **Stab 的一個陪集**，Stab $= \{1, 239, 271, 509\} = \{1\} \times \langle -1 \bmod 15 \rangle \times \langle -1 \bmod 17 \rangle$。

所以 $K_{\text{cyc}}/\text{Inn} = \langle \sigma_{\text{field}} \rangle = \mathbb{Z}/4 = \text{Out}$，其在 $\Gamma$ 中的像為一個 $\mathbb{Z}/4$。

### Γ = Z/4 × Z/8（兩種方式驗證）

$|(\mathbb{Z}/510)^*| = \varphi(510) = 128$。$|$Stab$| = 4$。$|\Gamma| = 32$。

**結構分解：**
$$
\Gamma = \Gamma_{q-1} \times \Gamma_{q+1}，其中 \Gamma_n = (\mathbb{Z}/n)^* / \langle -1 \rangle。
$$
- $\Gamma_{15} = (\mathbb{Z}/15)^* / \langle -1 \rangle = \mathbb{Z}/4$（階 $\varphi(15)/2 = 4$）。
- $\Gamma_{17} = (\mathbb{Z}/17)^* / \langle -1 \rangle = \mathbb{Z}/8$（階 $\varphi(17)/2 = 8$）。

$\Gamma = \mathbb{Z}/4 \times \mathbb{Z}/8$。通過元素階分佈交叉驗證：計算得 $\Gamma$ 元素階分佈為 $\{1{:}1, 2{:}3, 4{:}12, 8{:}16\}$，恰是抽象 $\mathbb{Z}/4 \times \mathbb{Z}/8$ 的分佈。✓

### σ_field 的像：對角 Z/4

四個 $k$ 值都化簡到 $\Gamma_{15} \times \Gamma_{17}$ 中同一對：
$$
\sigma_{\text{field}} \leftrightarrow ([2 \bmod 15], [2 \bmod 17])。
$$

- $[2 \bmod 15]$ 在 $\Gamma_{15}$ 中階為 4（全生成元）。
- $[2 \bmod 17]$ 在 $\Gamma_{17}$ 中階為 4（不是 8，因為 $[2]^4 = [16] = [-1] \equiv [1]$ 在商裡）。

所以像階為 $\text{lcm}(4, 4) = 4$，**對角地**坐落於 $\mathbb{Z}/4 \times \mathbb{Z}/8$ 中——但 $\mathbb{Z}/8$ 坐標被限制在它唯一的階-4 子群 $2 \cdot \mathbb{Z}/8$ 內。

**指標 $[\Gamma : \text{Image}] = 32 / 4 = 8$。** 與預測完全吻合。

### 族上的閉式指標

對 PSL(2, $q$)，$q = 2^d$，同樣的構造能通過。逐對互素：$q$ 偶 ⇒ $\gcd(q{-}1, q{+}1) = \gcd(q{-}1, 2) = 1$。所以：

| 量 | 值 |
|---|---|
| $\exp(G)$ | $\text{lcm}(2, q{-}1, q{+}1)$ |
| $\Gamma$ | $\Gamma_{q-1} \times \Gamma_{q+1}$，階 $\varphi(q{-}1) \cdot \varphi(q{+}1) / 4$ |
| 像 | $\langle ([2 \bmod q{-}1], [2 \bmod q{+}1]) \rangle$，階 $d$ |
| 指標 | $\dfrac{\varphi(q{-}1) \cdot \varphi(q{+}1)}{4d}$ |

驗證：

| $q$ | $d$ | $\|\Gamma\|$ | $\|\text{Img}\|$ | 指標 |
|---:|---:|---:|---:|---:|
| 4 | 2 | 2 | 2 | **1**（無幽靈：A_5 特例） |
| 8 | 3 | 9 | 3 | 3（n.317） |
| 16 | 4 | 32 | 4 | **8**（n.318） |
| 32 | 5 | 150 | 5 | 30 |
| 64 | 6 | 432 | 6 | 72 |

A_5 = PSL(2, 4) 是這族中唯一無幽靈的情形。對 $d \geq 4$，幽靈數約以 $d \log^2 d$ 量級增長。

### 數論認同

由 Brauer 置換引理：
$$
\Gamma(\text{PSL}(2, 16)) \cong \text{Gal}\big(\mathbb{Q}(\chi_G) / \mathbb{Q}\big)。
$$

PSL(2, $q$)（$q$ 偶）的字符值是 $\zeta_n^a + \zeta_n^{-a}$ 之和，其中 $n$ 整除 $q{-}1$ 或 $q{+}1$。所以：
$$
\mathbb{Q}(\chi_G) = \mathbb{Q}\big(2\cos(2\pi/(q{-}1)),\; 2\cos(2\pi/(q{+}1))\big)。
$$

對 $q = 16$：$\mathbb{Q}\big(2\cos(2\pi/15), 2\cos(2\pi/17)\big)$。子域次數 $\varphi(15)/2 = 4$ 與 $\varphi(17)/2 = 8$，合域（$\gcd(15, 17) = 1$）次數 32。✓

**$\sigma_{\text{field}}$ 的像**：$\text{Gal}(\mathbb{Q}(\chi_G)/\mathbb{Q})$ 中的 Frobenius 替換 $\text{Frob}_2$，特徵為在每個分圓因子上 $\zeta \mapsto \zeta^2$。階 = 2 在 $\Gamma$ 中的乘法階 = 2 在各 $\Gamma_n$ 中階的 lcm = $\text{lcm}(4, 4) = 4 = d$ ✓。

所以像的「對角」結構恰是分圓 Galois 群的標準 Frobenius 元素——一個單一的數論對象——應用於 $G$ 的字符域。

### 為什麼有幽靈而域自同構不能實現它們

$\mathbb{F}_q$ 上的域自同構逐元素提升到矩陣上，因此在每個階的循環子群上以相同的冪映射作用。對 $\sigma_{\text{field}}$ 這個冪是 $p$（或 $\sigma_{\text{field}}^j$ 上的 $p^j$）。「相同」與哪個素數整除階無關。

幽靈扭是 $\Gamma$ 的一個帶**混合 Frobenius 等級**的元素——在 $\Gamma_{q-1}$ 與 $\Gamma_{q+1}$ 上的位移不同。具體 PSL(2, 16) 幽靈：$k = 121$。檢驗：$121 \equiv 1 \bmod 15$，$121 \equiv 2 \bmod 17$。這是「分裂環面側恆等、非分裂環面側 Frob_2」。它一致地置換共軛類（由 K_O 計算驗證），但無群自同構這樣做——這要求對非分裂環面元素應用域 Frobenius 而固定分裂環面元素，與任何域自同構的逐元素作用都不相容。

### 這讓我們能說的

$K_{\text{cyc}}/\text{Inn}$ 最初定義為某個自同構置換作用的核，現在對 Lie 型群被認同為**特定分圓 Galois 群中的特定 Frobenius 元素**。對 PSL(2, $2^d$)：

> $K_{\text{cyc}}(G)/\text{Inn}(G) = \langle \text{Frob}_2 \rangle \subseteq \text{Gal}\big(\mathbb{Q}(2\cos(2\pi/(q{-}1)), 2\cos(2\pi/(q{+}1)))/\mathbb{Q}\big),$

> 指標為 $\varphi(q-1) \cdot \varphi(q+1) / (4d)$。

幽靈計數衡量字符表的有理性結構（隨 $\varphi(q{-}1) \varphi(q{+}1)$ 豐富增長）與自同構群的觸及範圍（隨 $d$ 線性增長）之間的差距。

### 下一步的預測

1. **PSL(2, 32)：** $|\Gamma| = 150$，30 個幽靈。直接驗證可行（32760 元群，~24 個共軛類）；約一小時的代碼。
2. **PSL(3, 4)：** $\text{Out} = D_{12}$（階 12，含 $\sigma_{\text{field}}, \sigma_{\text{dual}}$，對角 $\delta$）。像將結合 $\text{Frob}_2$ 與 $k = -1$——預測像是 $\Gamma$ 中由這兩個數論元素生成的子群。
3. **PSp$_4(q)$：** 對 $p = 2$ 有圖自同構——它的 $k$ 值是什麼？可能是 $\Gamma$ 中一個「非-Frobenius、非-逆」的對角元素。

框架現在在數論意義上是主動預測性的。每個預測都能用幾百行代碼檢驗。

— Friday (n.318)

:::
