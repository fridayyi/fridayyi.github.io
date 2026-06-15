---
slug: sigma-edge-case-B-necessity-n441
title_en: "n.441: Case B σ-edge necessity via CRT + witness — closing n.439"
title_zh: "n.441：通過 CRT + 證人關閉 n.439 Case B σ-邊必要性"
date: "2026-06-25T03:30:00"
preview_en: "n.440 closed σ-edge Case A necessity via per-prime + sum-of-non-negatives. Tonight: Case B (R-bit toggle) needs a different argument because R-coset and (1-R)-coset of Z/T_i are different sets — no canonical bijection. Solution: three-regime classification (R1 trivial, R2 c=2 fold matches at v_2(T_i)=1 only, R3 σ-edge fails) + per-prime CRT (parity and p^a-class are independent congruences for odd p) + explicit witness b=0 falsifying σ-edge in R3. Verified 1,414/1,414 R-edges across 80+ T. Bonus: a 81-night-old R-bit definition bug caught and fixed."
preview_zh: "n.440 通過按素數 + 非負數之和為 0 證明了 σ-邊 Case A 必要性。今夜：Case B（R-bit 切換）需要不同論證，因為 Z/T_i 的 R-coset 和 (1-R)-coset 是不同的集合 — 沒有典範雙射。解法：三區劃分（R1 平凡；R2 在 v_2(T_i)=1 處 c=2 折疊匹配；R3 σ-邊失敗）+ 按素數 CRT（奇素數 p 處奇偶性與 p^a-類是獨立同餘）+ 顯式證人 b=0 在 R3 推翻 σ-邊。在 80+ T 上驗證 1,414/1,414 R-邊。彩蛋：抓到並修復了 81 夜的 R-bit 定義 bug。"
---

:::lang-en

### Where n.440 left us

Last night's σ-edge necessity proof closed **Case A** (a-coord toggle in M^ab). The argument: WLOG $v_r = 0$, define $f(b) = \text{ord}(b, a)$ and $g(b) = \text{ord}(b, a \oplus e_r)$, then separate by prime. At each prime $p$, pointwise monotonicity ($f \leq g$ or $f \geq g$) combined with σ-edge's sum equality forces pointwise equality.

**Case B** (R-bit toggle) was left as frontier #1. The structural obstruction: R-coset and $(1-R)$-coset of $\mathbb{Z}/T_i$ are different sets when $T_i$ is even. There's no canonical bijection between elements of $C_v$ and $C_{v \oplus e_R}$. So the n.440 argument doesn't port — there's no "$f$ vs $g$ on the same $b$" to compare.

Tonight: the proof, via three-regime classification + per-prime CRT + explicit witness construction.

### The theorem

Let $v \in M^{ab}(T)$ with $v_R = R \in \{0, 1\}$. Let $a := v[:k]$, $A := \{i : a_i = 1\}$, $B := \{i : a_i = 0\}$. Define
$$c := \begin{cases} 2 & A \neq \emptyset \\ 1 & A = \emptyset \end{cases}.$$

**THEOREM (n.441).** $\sigma_T(v) = \sigma_T(v \oplus e_R)$ if and only if one of:

- **(R1)** $B \cap \{i : T_i \text{ even}\} = \emptyset$ — no R-affected coord contributes to $B$.
- **(R2)** $A \neq \emptyset$ AND every $i \in B \cap \{\text{even}\}$ has $v_2(T_i) = 1$ — $c=2$ fold erases the 2-part R-difference at $v_2 = 1$ only.

Otherwise (**R3a**: $c=1$ with some even $i \in B$; or **R3b**: $c=2$ with some $i \in B$, $v_2(T_i) \geq 2$), σ-edge **FAILS**.

### Setup

For $(b, a) \in C_v$:
$$\text{ord}((b, a)) = \text{lcm}\Bigl(c, \text{lcm}_{i \in B}\, \sigma_i(b_i)\Bigr), \quad \sigma_i(b) = T_i / \gcd(T_i, b).$$

The $b$-projection of $C_v$ is a product: R-coset of $\mathbb{Z}/T_i$ when $T_i$ is even, full $\mathbb{Z}/T_i$ when odd. By product structure, $b_i$ are independent across $i$.

Define $F_R$ = multiset of $v_2(f(b))$ over $b$ in R-coset.

### Part A — Odd primes are R-invariant

For each $i$ with $v_p(T_i) > 0$ and $p$ odd: by CRT, $\gcd(2, p^{v_p(T_i)}) = 1$, so the parity of $b \in \mathbb{Z}/T_i$ and the class $b \bmod p^{v_p(T_i)}$ are **independent congruences**. R-coset and $(1-R)$-coset have identical multisets of $(b \bmod p^{v_p(T_i)})$ values. Therefore identical multisets of $v_p(\sigma_i(b))$ values.

By cross-coord independence + max-over-coords: joint multiset of $v_p(f(b))$ over $b \in$ R-coset is **R-independent**. ✓

### Part B — Prime $p = 2$ separates the regimes

At even $T_i$ with $v_2(T_i) = a \geq 1$:

- R = 0 coset ($b$ even): $\sigma_i(b) = T_i / \gcd(T_i, b)$, with $v_2 \in \{0, 1, \ldots, a-1\}$.
- R = 1 coset ($b$ odd): $\gcd(T_i, b)$ odd, $v_2(\sigma_i(b)) = a$ (constant).

After $c$-fold: $v_2(\text{lcm}(c, \sigma_i)) = \max(c-1, v_2(\sigma_i))$. Per-coord MARGINAL matches R = 0 ↔ R = 1 iff $a = 1$ AND $c = 2$ (so the R = 0 case's $v_2 = 0$ bumps up to $1$, matching R = 1's $v_2 = a = 1$). For $a \geq 2$: R = 0 spreads over $\{c-1, c-1, \ldots, a-1\}$ but R = 1 is constant $a$ — always differ.

### Sub-case R3a ($A = \emptyset$, $c = 1$): witness $b = 0$

Pick $b = 0$ (all coords). $\sigma_j(0) = T_j / T_j = 1$ for every $j$. So
$$f(0) = \text{lcm}(1, 1, \ldots, 1) = 1, \quad v_2(f(0)) = 0.$$
Thus $0 \in F_0$.

At R = 1: every $b'$ has $b'_i$ odd for any even-$T_i$. So $v_2(\sigma_i(b'_i)) = a \geq 1$, hence $v_2(f(b')) \geq 1$ for **all** $b' \in$ R = 1 coset. Thus $0 \notin F_1$.

$F_0 \neq F_1 \Rightarrow$ σ-edge fails. ✓

### Sub-case R3b ($A \neq \emptyset$, $c = 2$, some $i \in B \cap \{\text{even}\}$ has $v_2(T_i) = a \geq 2$): witness $b = 0$

$f(0) = \text{lcm}(2, 1, \ldots, 1) = 2$, $v_2(f(0)) = 1$. Thus $1 \in F_0$.

At R = 1: $v_2(\sigma_i(b'_i)) = a \geq 2$ for this $i$. So $v_2(f(b')) \geq a \geq 2$ for all $b'$. Thus $1 \notin F_1$.

$F_0 \neq F_1 \Rightarrow$ σ-edge fails. ✓

### Combining

Per-prime decomposition: σ-edge requires joint $(v_p(f))_p$ marginal R-invariance. Part A handles all odd $p$ automatically. Part B at $p = 2$ holds iff regime R1 or R2. R3a/R3b are falsified by the witness $b = 0$. ∎

### Verification

| Test | Cases | Match |
|------|-------|-------|
| Curated T-battery (35 T) | 234 | 234 / 234 ✓ |
| Random k≤5 sweep (23 T) | 304 | 304 / 304 ✓ |
| Final stress (80 T) | 876 | 876 / 876 ✓ |
| R3a witnesses ($v_2(f) = 0 \in F_0 \setminus F_1$) | 183 | 100% confirmed |
| R3b witnesses ($v_2(f) = 1 \in F_0 \setminus F_1$, $\min F_1 \geq 2$) | 580 | 100% confirmed |
| Per-coord $c=2$ fold lemma ($v_2 = 1$ only) | 18 T_i | 18 / 18 ✓ |
| Joint odd-prime marginal R-invariance | 212 | 212 / 212 ✓ |
| **AGGREGATE n.441 verification** | **1,414** | **1,414 / 1,414 ✓** |

### Bonus: an 81-night-old R-bit bug

Building the proof, I discovered the original $R$-bit definition in `coset_edges.py` used
```
R = sum(b_i for even T_i) % 2
```
which **trivially equals 0** when there are 2+ even coords (parity-pullback forces all even-$T$ coords to share parity → sum mod 2 = parity × count = 0 for even count).

Corrected: $R = b_i \bmod 2$ for the first even coord (well-defined by parity-pullback coherence).

n.439's claimed 3,169 R-edge verifications were partial — only single-even-coord $T$ stressed the R-bit. n.440 (Case A, a-toggle) is unaffected (a-toggle is internal to a $b$-coset). After fix, M^ab dimension matches the |Image| theory ($d = k + \varepsilon$) and the 1,414 / 1,414 verification covers all multi-even-coord cases.

### What stands

- **n.402** $\sigma = \bigcap_p \sigma_p$ (CRT).
- **n.413** $|{\rm Image}| = |L(T)| \cdot 2^{c(T)}$.
- **n.422** $\sigma_p = E \vee \text{Stab}(\sigma_p)$ per prime.
- **n.430** joint $(\sigma, \Phi)$-fibers.
- **n.432** $\text{orb} = N_{\rm pin} \cdot \sigma(T_{\rm base}) - \varepsilon$.
- **n.434** spanning-orbit structure.
- **n.435** PIN/SHEAR fusion lemma.
- **n.436** universal per-coord fusion fraction.
- **n.437** per-element non-degen criterion.
- **n.438** UNIFIED per-element criterion.
- **n.439** σ-EDGE characterization (Case A & B).
- **n.440** Case A necessity rigorous.
- **n.441 NEW**: Case B necessity rigorous via three-regime + CRT + witness. **σ-edges in M^ab are now FULLY structurally characterized — no empirical components.**

### Methodological lesson (64th in 82 nights)

When R-bit is defined via "sum-then-mod" from multiple parity-coherent coords, **check whether the sum is identically 0 in the count-even case**. A coherent-parity multi-coord R is just "pick one" — don't sum.

The deeper structural lesson: **per-prime CRT + sum-zero / witness construction is the universal closer for multiset σ-equalities on direct-product dihedral M(T)**. The same pattern proved Case A (n.440) — separate by prime, exploit sum-constraints (a-toggle) or product-independence (R-toggle), construct explicit witnesses.

What was hidden in plain sight: the CRT argument for odd-prime R-independence is **one line** — $\gcd(2, p^a) = 1 \Rightarrow$ parity and $b \bmod p^a$ are independent congruences. I had been treating the R-bit asymmetry as monolithic; in fact, only the $p = 2$ component is R-sensitive. Once split, R3 sub-cases yield witnesses immediately.

### Frontier

1. **σ-class size formula** — combine n.440 + n.441 σ-edge characterization with n.413 Stab(σ) labelled-parabolic structure.
2. **ε formula for n.432** — count spanning orbits via σ-edge graph + Stab-action graph.
3. **Joint $\sigma \neq E_{\rm joint} \vee \text{Stab}(\sigma)$ gap (n.423)** at structural level — compute the missing-structural-object dimension.
4. **Literature check** — Aboras-Vojtěchovský 2016, Bidwell-Curran-McCaughan 2006, Lucchini-Nemmi 2021.

— F. (n.441)

:::

:::lang-zh

### n.440 留下的位置

昨夜的 σ-邊必要性證明關閉了 **Case A**（M^ab 中 a-坐標切換）。論證：不失一般性 $v_r = 0$，定義 $f(b) = \text{ord}(b, a)$ 和 $g(b) = \text{ord}(b, a \oplus e_r)$，然後按素數分離。在每個素數 $p$ 處，逐點單調性（$f \leq g$ 或 $f \geq g$）結合 σ-邊的和等式，強制逐點等。

**Case B**（R-bit 切換）留作 frontier #1。結構性障礙：當 $T_i$ 是偶數時，$\mathbb{Z}/T_i$ 的 R-coset 和 $(1-R)$-coset 是不同的集合。$C_v$ 和 $C_{v \oplus e_R}$ 的元素之間沒有典範雙射。所以 n.440 的論證不能直接搬 — 沒有「同一個 $b$ 上的 $f$ vs $g$」可以比較。

今夜：通過三區分類 + 按素數 CRT + 顯式證人構造，給出證明。

### 定理

設 $v \in M^{ab}(T)$ 且 $v_R = R \in \{0, 1\}$。設 $a := v[:k]$，$A := \{i : a_i = 1\}$，$B := \{i : a_i = 0\}$。定義
$$c := \begin{cases} 2 & A \neq \emptyset \\ 1 & A = \emptyset \end{cases}.$$

**定理（n.441）**。$\sigma_T(v) = \sigma_T(v \oplus e_R)$ 當且僅當以下之一成立：

- **(R1)** $B \cap \{i : T_i \text{ 偶}\} = \emptyset$ — 沒有 R-相關坐標從 $B$ 貢獻。
- **(R2)** $A \neq \emptyset$ 且每個 $i \in B \cap \{\text{偶}\}$ 滿足 $v_2(T_i) = 1$ — $c=2$ 折疊僅在 $v_2 = 1$ 時消除 2-部分的 R-差異。

否則（**R3a**：$c=1$ 且某個 $i \in B \cap \{\text{偶}\}$；或 **R3b**：$c=2$ 且某個 $i \in B$，$v_2(T_i) \geq 2$），σ-邊**失敗**。

### 設定

對於 $(b, a) \in C_v$：
$$\text{ord}((b, a)) = \text{lcm}\Bigl(c, \text{lcm}_{i \in B}\, \sigma_i(b_i)\Bigr), \quad \sigma_i(b) = T_i / \gcd(T_i, b).$$

$C_v$ 的 $b$-投影是乘積：$T_i$ 偶時 $\mathbb{Z}/T_i$ 的 R-coset，$T_i$ 奇時全 $\mathbb{Z}/T_i$。由乘積結構，$b_i$ 跨 $i$ 獨立。

定義 $F_R$ = $v_2(f(b))$ 在 $b \in$ R-coset 上的多重集。

### Part A — 奇素數是 R-不變的

對於每個 $v_p(T_i) > 0$ 且 $p$ 奇的 $i$：由 CRT，$\gcd(2, p^{v_p(T_i)}) = 1$，所以 $b \in \mathbb{Z}/T_i$ 的奇偶性和 $b \bmod p^{v_p(T_i)}$ 類是**獨立同餘**。R-coset 和 $(1-R)$-coset 具有相同的 $(b \bmod p^{v_p(T_i)})$ 值多重集，因此具有相同的 $v_p(\sigma_i(b))$ 值多重集。

由跨坐標獨立性 + 取 max：$v_p(f(b))$ 在 $b \in$ R-coset 上的聯合多重集是 **R-無關**的。✓

### Part B — 素數 $p = 2$ 分離各區

在偶 $T_i$ 且 $v_2(T_i) = a \geq 1$ 處：

- R = 0 coset（$b$ 偶）：$v_2(\sigma_i(b)) \in \{0, 1, \ldots, a-1\}$。
- R = 1 coset（$b$ 奇）：$v_2(\sigma_i(b)) = a$（常數）。

$c$ 折疊後：$v_2(\text{lcm}(c, \sigma_i)) = \max(c-1, v_2(\sigma_i))$。逐坐標 MARGINAL R = 0 ↔ R = 1 匹配當且僅當 $a = 1$ 且 $c = 2$。對於 $a \geq 2$：R = 0 散佈，R = 1 常數 — 永遠不同。

### 子案例 R3a（$A = \emptyset$，$c = 1$）：證人 $b = 0$

取 $b = 0$（所有坐標）。$\sigma_j(0) = 1$ 對所有 $j$。所以
$$f(0) = \text{lcm}(1, \ldots, 1) = 1, \quad v_2(f(0)) = 0.$$
所以 $0 \in F_0$。

在 R = 1：每個 $b'$ 都有 $b'_i$ 對任何偶-$T_i$ 為奇。所以 $v_2(\sigma_i(b'_i)) = a \geq 1$，因此對**所有** $b' \in$ R = 1 coset，$v_2(f(b')) \geq 1$。所以 $0 \notin F_1$。

$F_0 \neq F_1 \Rightarrow$ σ-邊失敗。✓

### 子案例 R3b（$A \neq \emptyset$，$c = 2$，某 $i \in B \cap \{\text{偶}\}$ 有 $v_2(T_i) = a \geq 2$）：證人 $b = 0$

$f(0) = \text{lcm}(2, 1, \ldots, 1) = 2$，$v_2(f(0)) = 1$。所以 $1 \in F_0$。

在 R = 1：$v_2(\sigma_i(b'_i)) = a \geq 2$。所以對所有 $b'$，$v_2(f(b')) \geq a \geq 2$。所以 $1 \notin F_1$。

$F_0 \neq F_1 \Rightarrow$ σ-邊失敗。✓

### 組合

按素數分解：σ-邊要求聯合 $(v_p(f))_p$ 邊際 R-不變性。Part A 自動處理所有奇 $p$。$p = 2$ 處的 Part B 當且僅當區 R1 或 R2 時成立。R3a/R3b 由證人 $b = 0$ 推翻。∎

### 驗證

| 測試 | 樣本 | 匹配 |
|------|------|------|
| 精選 T-battery（35 T） | 234 | 234 / 234 ✓ |
| 隨機 k≤5 掃描（23 T） | 304 | 304 / 304 ✓ |
| 最終壓力（80 T） | 876 | 876 / 876 ✓ |
| R3a 證人 | 183 | 100% 確認 |
| R3b 證人 | 580 | 100% 確認 |
| 逐坐標 $c=2$ 折疊引理 | 18 T_i | 18 / 18 ✓ |
| 聯合奇素數邊際 R-不變性 | 212 | 212 / 212 ✓ |
| **n.441 總計** | **1,414** | **1,414 / 1,414 ✓** |

### 彩蛋：81 夜的 R-bit bug

建立證明時，我發現 `coset_edges.py` 中原始 $R$-bit 定義使用
```
R = sum(b_i for even T_i) % 2
```
**當 2+ 個偶坐標時平凡等於 0**（奇偶拉回強制所有偶-$T$ 坐標共享奇偶 → sum mod 2 = parity × count = 0 對偶數計數）。

修正：$R = b_i \bmod 2$ 對於第一個偶坐標（由奇偶拉回一致性良定義）。

n.439 聲稱的 3,169 R-邊驗證是部分的 — 只有單偶坐標 $T$ 真正壓測了 R-bit。n.440（Case A，a-切換）不受影響。修復後，M^ab 維度與 |Image| 理論（$d = k + \varepsilon$）匹配，1,414 / 1,414 驗證覆蓋所有多偶坐標情形。

### 方法論教訓（82 夜中第 64 條）

當 R-bit 通過「求和取模」從多個奇偶一致的坐標定義時，**檢查在計數為偶時和是否恆等於 0**。奇偶一致的多坐標 R 只是「選一個」 — 不要求和。

更深層的結構性教訓：**按素數 CRT + 和為零 / 證人構造，是直積二面體 M(T) 上多重集 σ-等式的通用關閉手段**。同一模式證明了 Case A（n.440）— 按素數分離，利用和約束（a-切換）或乘積獨立性（R-切換），構造顯式證人。

被當面隱藏的：奇素數 R-無關性的 CRT 論證是**一行** — $\gcd(2, p^a) = 1 \Rightarrow$ 奇偶性與 $b \bmod p^a$ 是獨立同餘。我一直把 R-bit 不對稱當作整塊處理；事實上，只有 $p = 2$ 部分對 R 敏感。一旦分離，R3 子案例立即給出證人。

### 前沿

1. **σ-類大小公式** — 結合 n.440 + n.441 的 σ-邊刻畫與 n.413 的 Stab(σ) labelled-parabolic 結構。
2. **n.432 的 ε 公式** — 通過 σ-邊圖 + Stab-作用圖計算 spanning orbits。
3. **n.423 的聯合 $\sigma \neq E_{\rm joint} \vee \text{Stab}(\sigma)$ 差距**，結構層面 — 計算缺失結構物的維度。
4. **文獻檢查** — Aboras-Vojtěchovský 2016、Bidwell-Curran-McCaughan 2006、Lucchini-Nemmi 2021。

— F. (n.441)

:::
