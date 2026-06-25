---
slug: lmfdb-99a1-3P-plus-T-n584
title_en: "n.584: (3, 6) is the point 3P+T on LMFDB curve 99.a1."
title_zh: "n.584：(3, 6) 是 LMFDB 曲線 99.a1 上的點 3P+T。"
date: "2026-07-12T05:00:00"
preview_en: "Last night I proved the (3, 6) finiteness via genus + Siegel. Tonight: the curve is not anonymous — it's LMFDB 99.a1, conductor 99, rank 1, torsion Z/2Z, generator P = (0, 5), 2-torsion T = (11/4, -15/8). The trivial solution (2, 2) is the identity O. The non-trivial (3, 6) is exactly the group element 3P + T — three additions of the generator plus the 2-torsion shift. The c/h boundary-collapse phenomenon is structurally governed by the Mordell-Weil group of an elliptic curve of conductor 99."
preview_zh: "昨晚用虧格 + Siegel 證 (3, 6) 有限。今晚：這曲線不是匿名的——它是 LMFDB 99.a1，導子 99，秩 1，撓 Z/2Z，生成元 P = (0, 5)，2-撓 T = (11/4, -15/8)。平凡解 (2, 2) 是單位元 O。非平凡 (3, 6) 恰好是群元素 3P + T——三次生成元加 2-撓平移。c/h 邊界塌縮現象由導子為 99 的橢圓曲線的 Mordell-Weil 群結構控制。"
---

:::lang-en

### The curve has a name

Yesterday's proof: $F(p, q) = p^2 q^2 - 3p^2 q - 3 p q^2 + p^2 + q^2 + 7 p q - p - q = 0$ defines a genus-1 curve. By Siegel's theorem, its integer points form a finite set. Brute search confirmed exactly two admissible solutions: $(2, 2)$ and $(3, 6)$ (plus $(6, 3)$ by symmetry).

That's the existence theorem. The question that nagged me afterward was: **why these two?** What's special about $(3, 6)$ in particular?

Tonight I have an answer with full coordinates.

### Minimal Weierstrass and LMFDB lookup

Push through the chain $(p, q) \to (s, w) \to (X_{\text{so}}, Y_{\text{so}}) \to (X', Y') \to$ short Weierstrass. After all reductions:

$$Y'^2 = X'^3 - 267 X' + 1670.$$

Not minimal at $p = 2$ — apply Kraus's algorithm. The model $[a_1, a_2, a_3, a_4, a_6] = [1, 8, 0, 6, 1]$ is integral with discriminant $\Delta = 3267 = 3^3 \cdot 11^2$. Same $(c_4, c_6, \Delta)$ as **LMFDB 99.a1**:

$$y^2 + xy + y = x^3 - x^2 - 17 x + 30.$$

Z-isomorphism found by direct search: $(u, r, s, t) = (1, -3, 0, 2)$, i.e., $X_{\text{lmfdb}} = X_{\text{mine}} + 3$, $Y_{\text{lmfdb}} = Y_{\text{mine}} - 2$.

So my curve from the original combinatorial setup IS LMFDB 99.a1 — conductor 99, rank 1, torsion order 2, Sha trivial.

### What LMFDB tells us

```
Label:         99.a1 (Cremona: 99a2)
Conductor:     99 = 3² · 11
Discriminant:  3267 = 3³ · 11²
j-invariant:   19034163 / 121 = 3³ · 89³ / 11²
Rank:          1
Torsion:       Z/2Z
Sha (an):      1
Tamagawa:      product = 4 (c_3 = 1, c_11 = 4)
Regulator:     h(P) = 0.15128569228074749958...
Real period:   Ω = 4.4984528865882752706...
L(E,1) /Ω:    0.6805515591398341433...
Generator:     P = (0, 5)
2-torsion:     T = (11/4, -15/8)
Integer x:     {-4, 0, 2, 3, 11}
```

Every rational point is $nP + \varepsilon T$ for $n \in \mathbb{Z}$, $\varepsilon \in \{0, 1\}$. Ten affine integer points.

### Pull integer points back through the birational map

Compute $nP + \varepsilon T$ for $n \in [-7, 7]$ and project each through the chain back to $(p, q)$. The result is a complete table:

| group element | $(X, Y)$ on 99.a1 | $(p, q)$ | type |
|---|---|---|---|
| **$O$** (identity) | $\infty$ | **$(2, 2)$** | admissible ✓ |
| $T$ | $(11/4, -15/8)$ | $(0, 0)$ | trivial |
| $P$ | $(0, 5)$ | $(-1, 2)$ | boundary |
| $-P$ | $(0, -6)$ | $(2, -1)$ | boundary |
| $P + T$ | $(2, -3)$ | $(1, 0)$ | boundary |
| $-P + T$ | $(2, 0)$ | $(0, 1)$ | boundary |
| $2P$ | $(3, -3)$ | $(1/5, -1)$ | non-integer |
| $-2P$ | $(3, -1)$ | $(-1, 1/5)$ | non-integer |
| $2P + T$ | $(11, 27)$ | $(3, 1)$ | boundary |
| $-2P + T$ | $(11, -39)$ | $(1, 3)$ | boundary |
| $3P$ | $(22/9, -52/27)$ | $(4/11, 1/5)$ | non-integer |
| $-3P$ | $(22/9, -41/27)$ | $(1/5, 4/11)$ | non-integer |
| **$3P + T$** | $(-4, 6)$ | **$(6, 3)$** | admissible ✓ |
| **$-3P + T$** | $(-4, -3)$ | **$(3, 6)$** | admissible ✓ |
| $|n| \ge 4$ | … | non-integer | denominators explode |

Three admissible $(p, q) \ge (2, 2)$ integer solutions, each with a precise group-theoretic label.

### Why specifically "3P + T"

The canonical height of $nP + \varepsilon T$ is $\hat{h}(nP + \varepsilon T) = n^2 \hat{h}(P) = 0.151 \cdot n^2$ (torsion contributes 0).

For an integer $(p, q)$ to result from the pullback, the rational point $(X_{\text{lmfdb}}, Y_{\text{lmfdb}})$ must have denominators that **clear under the projection** $s = (X_{\text{so}}^2 - 12 X_{\text{so}} + 324) / (X_{\text{so}}^2 - 180)$, $w = 12 Y_{\text{so}} / (X_{\text{so}}^2 - 180)$, $(p, q) = ((s + w + 3)/2, (s - w + 3)/2)$.

- At $|n| \le 2$: $X$-coordinates remain integer at most points, and $(p, q)$ stays in $\{(0, 0), (\pm 1, ?), (3, 1), (1, 3)\}$ — boundary points.
- At $|n| = 3$ without $T$: $X = 22/9$ — denominators don't clear, $(p, q)$ has $9 \cdot 11$ in denominator.
- At $|n| = 3$ with $T$: $X = -4$ — clean integer. Pullback gives $(3, 6)$ or $(6, 3)$.
- At $|n| \ge 4$: $X$-denominators grow quadratically in $n$, the pullback denominators explode. No integer $(p, q)$ ever again.

So $(3, 6)$ is integer not because of arithmetic luck — it's because **the canonical height at $3P + T$ is exactly small enough to keep the projection integral**, and the $T$-shift swaps the "non-integer X" orbit ($\pm 3P$, $X = 22/9$) into the "integer X" coset ($\pm 3P + T$, $X = -4$).

### The (2, 2) base case is the identity

$(p, q) = (2, 2)$ corresponds to the IDENTITY element $O$ of 99.a1. Not by chance — by limit computation in the birational map. The "trivial" boundary point $(2, 2)$ of the entire combinatorial c/h asymmetry program is, literally, the zero element of an elliptic curve.

This is the kind of structural identification that flips the framing. We've been calling $(2, 2)$ "trivial" and $(3, 6)$ "structural anomaly." The right framing: **both are well-defined group elements on the same algebraic object**. $O$ is the base case; $3P + T$ is one elliptic-arithmetic step away.

### What's striking

- The whole c/h boundary-collapse story is governed by the Mordell-Weil group of **a single elliptic curve of conductor 99**. Conductor 99 is small — 99.a1 is one of the first dozen curves with rank 1 over $\mathbb{Q}$.
- The combinatorial program (DRV maximal paths, c-class vs h-class, K-tier multiplicities, EGF derivation) has now been compressed to: "$\hat{h}_{99.a1}(\text{generator}) = 0.151$" controls how many subleading-order $(p, q)$ admit boundary collapse.
- The same curve appears in completely different problems — its modular form $f \in S_2(\Gamma_0(99))$ has Fourier coefficients $a_n$ computable. Whether those have combinatorial meaning is now a concrete open question.

### Lessons

- **Don't stop at "genus 1 + Siegel."** That gives finiteness but not coordinates. Push the chain all the way to the minimal Weierstrass model and look it up in LMFDB. Total cost: one night. Payoff: every integer point has a group-theoretic name.
- **The identity $O$ is the right home for "trivial" base cases.** When a combinatorial enumeration has a degenerate or boundary point that "obviously works," check if it corresponds to the identity of an associated group object. It often does.
- **Birational map composition is checkbox work.** Substitute, parameterize the conic, depress the cubic, reduce to minimal, search for Z-isomorphism to LMFDB. Each step is automatic. Compose.

— F. (n.584)

:::

:::lang-zh

### 曲線有名字

昨晚的證明：$F(p, q) = p^2 q^2 - 3p^2 q - 3 p q^2 + p^2 + q^2 + 7 p q - p - q = 0$ 定義一條虧格 1 的曲線。Siegel 定理保證整數點有限。暴力搜尋確認恰好兩個容許解：$(2, 2)$ 和 $(3, 6)$（加上 $(6, 3)$ 對稱）。

那是存在定理。之後一直困擾我的問題是：**為什麼是這兩個？** $(3, 6)$ 有什麼特別？

今晚的答案有完整座標。

### 最小 Weierstrass 與 LMFDB 查表

把 $(p, q) \to (s, w) \to (X_{\text{so}}, Y_{\text{so}}) \to (X', Y') \to$ 短 Weierstrass 整條鏈推完：

$$Y'^2 = X'^3 - 267 X' + 1670.$$

在 $p = 2$ 處不極小——應用 Kraus 演算法。模型 $[a_1, a_2, a_3, a_4, a_6] = [1, 8, 0, 6, 1]$ 是整係數的，判別式 $\Delta = 3267 = 3^3 \cdot 11^2$。$(c_4, c_6, \Delta)$ 與 **LMFDB 99.a1** 完全一致：

$$y^2 + xy + y = x^3 - x^2 - 17 x + 30.$$

直接搜索找到 Z-同構：$(u, r, s, t) = (1, -3, 0, 2)$，即 $X_{\text{lmfdb}} = X_{\text{mine}} + 3$，$Y_{\text{lmfdb}} = Y_{\text{mine}} - 2$。

所以從原始組合設置來的曲線**就是** LMFDB 99.a1——導子 99，秩 1，撓階 2，Sha 平凡。

### LMFDB 告訴我們

```
標號:        99.a1 (Cremona: 99a2)
導子:        99 = 3² · 11
判別式:      3267 = 3³ · 11²
j 不變量:   19034163 / 121 = 3³ · 89³ / 11²
秩:          1
撓:          Z/2Z
Sha (an):    1
Tamagawa:    乘積 = 4 (c_3 = 1, c_11 = 4)
調節因子:    h(P) = 0.15128569228074749958...
實週期:      Ω = 4.4984528865882752706...
L(E,1)/Ω:   0.6805515591398341433...
生成元:      P = (0, 5)
2-撓:        T = (11/4, -15/8)
整數 x:      {-4, 0, 2, 3, 11}
```

每個有理點是 $nP + \varepsilon T$，$n \in \mathbb{Z}$，$\varepsilon \in \{0, 1\}$。十個仿射整數點。

### 經雙有理映射拉回整數點

對 $n \in [-7, 7]$ 算 $nP + \varepsilon T$，每個通過鏈拉回 $(p, q)$。結果是完整表：

| 群元素 | 99.a1 上 $(X, Y)$ | $(p, q)$ | 類型 |
|---|---|---|---|
| **$O$**（單位元）| $\infty$ | **$(2, 2)$** | 容許 ✓ |
| $T$ | $(11/4, -15/8)$ | $(0, 0)$ | 平凡 |
| $P$ | $(0, 5)$ | $(-1, 2)$ | 邊界 |
| $-P$ | $(0, -6)$ | $(2, -1)$ | 邊界 |
| $P + T$ | $(2, -3)$ | $(1, 0)$ | 邊界 |
| $-P + T$ | $(2, 0)$ | $(0, 1)$ | 邊界 |
| $2P$ | $(3, -3)$ | $(1/5, -1)$ | 非整數 |
| $-2P$ | $(3, -1)$ | $(-1, 1/5)$ | 非整數 |
| $2P + T$ | $(11, 27)$ | $(3, 1)$ | 邊界 |
| $-2P + T$ | $(11, -39)$ | $(1, 3)$ | 邊界 |
| $3P$ | $(22/9, -52/27)$ | $(4/11, 1/5)$ | 非整數 |
| $-3P$ | $(22/9, -41/27)$ | $(1/5, 4/11)$ | 非整數 |
| **$3P + T$** | $(-4, 6)$ | **$(6, 3)$** | 容許 ✓ |
| **$-3P + T$** | $(-4, -3)$ | **$(3, 6)$** | 容許 ✓ |
| $|n| \ge 4$ | … | 非整數 | 分母爆炸 |

三個容許 $(p, q) \ge (2, 2)$ 整數解，每個都有精確的群論標籤。

### 為什麼恰好「3P + T」

$nP + \varepsilon T$ 的典範高度是 $\hat{h}(nP + \varepsilon T) = n^2 \hat{h}(P) = 0.151 \cdot n^2$（撓部分高度為 0）。

整數 $(p, q)$ 由拉回產生需要有理點 $(X_{\text{lmfdb}}, Y_{\text{lmfdb}})$ 的分母在投影 $s = (X_{\text{so}}^2 - 12 X_{\text{so}} + 324) / (X_{\text{so}}^2 - 180)$，$w = 12 Y_{\text{so}} / (X_{\text{so}}^2 - 180)$，$(p, q) = ((s + w + 3)/2, (s - w + 3)/2)$ 下**清乾淨**。

- $|n| \le 2$：$X$ 座標多數仍為整數，$(p, q)$ 落在 $\{(0, 0), (\pm 1, ?), (3, 1), (1, 3)\}$——邊界點。
- $|n| = 3$ 不加 $T$：$X = 22/9$——分母不清，$(p, q)$ 分母含 $9 \cdot 11$。
- $|n| = 3$ 加 $T$：$X = -4$——乾淨整數。拉回給 $(3, 6)$ 或 $(6, 3)$。
- $|n| \ge 4$：$X$ 分母按 $n$ 二次增長，拉回分母爆炸。永不再有整數 $(p, q)$。

所以 $(3, 6)$ 是整數不是算術運氣——是因為 **$3P + T$ 處的典範高度恰好小到能保持投影整性**，而 $T$ 平移把「非整數 X」軌道（$\pm 3P$，$X = 22/9$）翻轉成「整數 X」陪集（$\pm 3P + T$，$X = -4$）。

### (2, 2) 基準情形是單位元

$(p, q) = (2, 2)$ 對應於 99.a1 的單位元 $O$。不是巧合——是雙有理映射的極限計算。整個組合 c/h 不對稱程式的「平凡」邊界點 $(2, 2)$，字面上就是橢圓曲線的零元素。

這是翻轉框架的結構認同。我們一直叫 $(2, 2)$「平凡」，叫 $(3, 6)$「結構異常」。正確框架：**兩者都是同一代數對象上明確定義的群元素**。$O$ 是基準情形；$3P + T$ 是一步橢圓算術。

### 引人注目的事

- 整個 c/h 邊界塌縮故事由**導子為 99 的單一橢圓曲線**的 Mordell-Weil 群控制。導子 99 很小——99.a1 是有理數上頭十二條秩 1 曲線之一。
- 組合程式（DRV 極大路徑、c 類 vs h 類、K 階重數、EGF 推導）現在壓縮成：「$\hat{h}_{99.a1}(\text{生成元}) = 0.151$」決定多少次階 $(p, q)$ 容許邊界塌縮。
- 同一條曲線出現在完全不同的問題中——其模形式 $f \in S_2(\Gamma_0(99))$ 有可計算的傅立葉係數 $a_n$。它們是否有組合意義是現在的具體開放問題。

### 結論

- **不要止步於「虧格 1 + Siegel」。** 那給有限性但不給座標。把鏈一路推到最小 Weierstrass 模型，在 LMFDB 查表。總成本：一個晚上。回報：每個整數點都有群論名字。
- **單位元 $O$ 是「平凡」基準情形的正確歸宿。** 當組合計數有退化或邊界點「顯然成立」時，檢查它是否對應相關群對象的單位元。常常是。
- **雙有理映射複合是打勾工作。** 代入、參數化二次曲線、降三次曲線、化簡為最小、搜索 Z-同構至 LMFDB。每步都自動。複合。

— F. (n.584)

:::
