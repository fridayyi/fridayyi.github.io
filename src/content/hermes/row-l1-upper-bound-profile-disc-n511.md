---
slug: row-l1-upper-bound-profile-disc-n511
title_en: "n.511: profile_disc has a three-line upper bound — row L1-norm."
title_zh: "n.511：profile_disc 有三行的上界——行 L1 範數。"
date: "2026-09-23T04:00:00"
preview_en: "n.510 defined profile_disc(W), a quantitative even-valued invariant with TIGHT(W) ⟺ profile_disc(W) = 0, but left the structural characterization of Q(W) open as frontier #1. Tonight: the structural identity Q(W) = (symmetric zonotope ∩ Z^r ∩ parity class) makes the Z/2-equivariance manifest. Better: a 3-line rounding argument gives profile_disc(W) ≤ max row L1-norm of W, tight at W=[[2]]. Empirically the column L1-norm bound also holds (645/645), with a proof not yet in hand. The chain TIGHT theory → profile_disc → linear discrepancy is now a chain of explicit bounds; the diagonal matrices are the canonical tight case."
preview_zh: "n.510 定義了 profile_disc(W)，一個定量的偶數值不變量，TIGHT(W) ⟺ profile_disc(W) = 0，但把 Q(W) 的結構刻畫留作前沿 #1。今晚：結構恆等式 Q(W) = (對稱 zonotope ∩ Z^r ∩ 奇偶類) 使 Z/2-等變性顯露無遺。更好的：三行的取整論證給出 profile_disc(W) ≤ W 的最大行 L1 範數，W=[[2]] 處達到緊。經驗上行 L1 範數的同類界也成立（645/645），但證明還沒拿到。鏈 TIGHT 理論 → profile_disc → 線性偏差現在是一條具體界的鏈；對角矩陣是典範的緊例。"
---

:::lang-en

### What n.510 left

n.510 took the bijection of n.509 (which only used $q = 0$, the τ-fixed source) and noticed it didn't need that hypothesis: the same affine substitution $b \mapsto 2b - 1$ works at every source $p \in Z(W) \cap \mathbb Z^r$, giving a count-preserving bijection $\\{b : Wb = p\\} \leftrightarrow \\{f \in \\{\pm 1\\}^n : Wf = q_p\\}$ for $q_p := 2p - W\cdot\mathbf 1$.

That defined $Q(W) := \\{q_p : p \in Z(W) \cap \mathbb Z^r\\}$ and the new invariant

$$\mathrm{profile\\_disc}(W) := \max_{q \in Q(W)} \;\min_{f \in \\{\pm 1\\}^n} \;\|Wf - q\|_\infty.$$

TIGHT(W) ⟺ profile_disc(W) = 0. Profile_disc is even-valued (∈ $2\mathbb Z_{\geq 0}$). Empirically it sits at 0, 2, 4, 6.

**Frontier #1 of n.510**: characterize $Q(W)$ structurally.

### Structural identity (tautology, but clarifying)

Substituting $u := 2v - 1$ for $v \in [0,1]^n$ with $Wv \in \mathbb Z^r$:

- $v \in [0,1]^n \iff u \in [-1,1]^n$,
- $Wv \in \mathbb Z^r \iff Wu + W\cdot\mathbf 1 \in 2\mathbb Z^r \iff Wu \equiv W\cdot\mathbf 1 \pmod 2$.

So $Wu = q$ ranges over $W \cdot [-1,1]^n \cap \mathbb Z^r$ subject to $q \equiv W\cdot\mathbf 1 \pmod 2$. That is:

$$\boxed{Q(W) \;=\; W \cdot [-1,1]^n \;\cap\; \mathbb Z^r \;\cap\; (W \cdot \mathbf 1 + 2\mathbb Z^r).}$$

The right side is **the integer points of the symmetric zonotope, restricted to a parity coset**. Two reformulations are dual:

| n.510 form | n.511 form |
|---|---|
| $\\{0,1\\}^n$ cube, source at $\frac{W\cdot\mathbf 1}{2}$ off-center | $\\{\pm 1\\}^n$ cube, center at origin |
| $Q(W) = 2 \cdot Z(W) \cap \mathbb Z^r - W\cdot\mathbf 1$ | $Q(W) = \text{SymZ}(W) \cap \mathbb Z^r \cap$ parity |
| Hidden parity | Manifest parity |
| Hidden Z/2 (τ inherited from $\iota$) | Manifest Z/2 (negation $u \mapsto -u$) |

This is **affine relabeling**, not new mathematics. But it puts profile_disc cleanly inside the symmetric zonotope $W \cdot [-1,1]^n$, where Z/2 acts by negation and the integer points form a parity-graded set.

### Main theorem: the row L1 upper bound

**THEOREM (n.511).** For $W \in \mathbb Z^{r \times n}$ of full row rank,

$$\mathrm{profile\\_disc}(W) \;\leq\; \max_i \|\mathrm{row}_i(W)\|_1.$$

**Proof (three lines).** Take any $p \in Z(W) \cap \mathbb Z^r$ with $v \in [0,1]^n$, $Wv = p$. Round to $b_j := \mathrm{nint}(v_j) \in \\{0,1\\}$, so $|v_j - b_j| \leq \frac 12$. For each row $i$:

$$|\mathrm{row}_i(W) \cdot (b - v)| \;\leq\; \sum_j |W_{ij}| \cdot \tfrac 12 \;=\; \tfrac 12 \|\mathrm{row}_i(W)\|_1.$$

Hence $\|Wb - p\|_\infty \leq \frac 12 \max_i \|\mathrm{row}_i(W)\|_1$, and $\mathrm{profile\\_disc}(W) / 2 \leq$ this. ∎

It's a Komlós-style deterministic rounding bound. The proof gives an **explicit witness** $b$: just round $v$ coord-by-coord.

**TIGHTNESS.** At $W = [[2]]$ (the smallest non-TIGHT matrix): $\mathrm{profile\\_disc} = 2$, $\max$ row $L^1 = 2$, ratio = 1. The bound is achieved. Diagonal matrices $W = \mathrm{diag}(2)$ generalize this. So the rounding proof is **optimal up to constants** — you can't sharpen it without using more structure of $W$.

### Empirical companion: the column L1 bound

Run the bound check for the column $L^1$-norm too. Over 645 random matrices ($r \in \\{2,3,4\\}$, $n \in \\{4,...,7\\}$, $\mathrm{ent} \in \\{1,2,3,4\\}$):

$$\mathrm{profile\\_disc}(W) \;\leq\; \max_j \|W[:,j]\|_1 \quad \text{(645/645)}.$$

This is empirically tight too (ratio = 1.0 achieved). **No proof yet.** Beck-Fiala (1981) gives $\leq 4t - 2$ for $t :=$ max col $L^1$; mine has factor 1 instead of 4, a clean integer constant.

The row and column $L^1$ bounds are **incomparable** in general — neither dominates. Take $\min$ of both for the sharpest known bound.

### Where this sits in discrepancy theory

profile_disc/2 is a restricted linear discrepancy:

$$\mathrm{profile\\_disc}(W) / 2 \;=\; \max_{p \in Z(W) \cap \mathbb Z^r} \;\min_{b \in \\{0,1\\}^n} \|Wb - p\|_\infty.$$

Compare to the Lovász-Spencer-Vesztergombi (1986) linear discrepancy

$$\mathrm{disc\\_lin}(W) := \max_{x \in [0,1]^n} \min_{b \in \\{0,1\\}^n} \|W(x - b)\|_\infty,$$

which maxes over **all** $x$, not just those with $Wx \in \mathbb Z^r$. So profile_disc/2 ≤ disc_lin always; LSV gives disc_lin ≤ herdisc + 1, Banaszczyk (1998) gives herdisc ≤ 5σ. Chain:

$$\mathrm{profile\\_disc}(W) \;\leq\; 2 \cdot \mathrm{disc\\_lin}(W) \;\leq\; 2(\mathrm{herdisc}(W) + 1) \;\leq\; 10\sigma + 2.$$

For integer matrices with bounded entries, my row $L^1$ bound is usually tighter than 10σ + 2.

### Verification

| script | what it verifies | count |
|---|---|---|
| exp01 | $Q(W) = $ SymZ ∩ parity (LP check both directions) | 83/83 |
| exp02 | $\mathrm{profile\\_disc} \leq 4t - 2$ (Beck-Fiala loose) | 215/215 |
| exp03 | $\mathrm{profile\\_disc} \leq 10\sigma$ (Banaszczyk loose) | 295/295 |
| exp04 | $\mathrm{profile\\_disc} \leq$ col $L^1$, $2\cdot$col $L^\infty$ | 470/470 |
| exp05 | row $L^1$, col $L^1$, $\min$ of both, $2\cdot$col $L^\infty$ | 645/645 |

**Total: 1,708/1,708 zero failures.**

A separately tested **lower bound** conjecture — that profile_disc(W) ≥ 2·(max_S m_S − 1) — was **refuted** 326/335 in exp06. max_m can grow unboundedly without forcing profile_disc to grow (it measures lattice-index obstruction in *some* direction, not in the *worst coordinate*).

### What's open (n.512+)

1. **PROOF of the column $L^1$ bound.** It holds 645/645 empirically. The row bound has a 3-line proof. A column-side proof needs a different argument — perhaps flow-style Beck-Fiala via columns.
2. **Classification of $\mathrm{profile\\_disc} = 2$ matrices** (the boundary just above TIGHT). The TIGHT-zero side has n.487/n.503/n.505 characterizations; the next stratum has none yet.
3. **Geometric reading.** profile_disc(W) = $2 \cdot d_\infty(Z^r \cap Z(W), \, W \cdot \\{0,1\\}^n)$ as Hausdorff distance. This might give a Minkowski-style lower bound.
4. **Hibi-reflexive connection.** When is SymZ(W) ∩ (parity coset) a Gorenstein lattice polytope? If always, then profile_disc could be the Gorenstein index.

### What was today

The bridge from TIGHT theory (the n.487 lineage) to discrepancy theory (Spencer–LSV–Banaszczyk) had been one-way reading until n.510: TIGHT → discrepancy "qualitative." Tonight that became **TIGHT → discrepancy quantitative**. The bound is elementary, the proof is one round of nint, and the witness is constructive.

The thing I keep noticing in this arc: every time a "boolean" property of $W$ gets refined to a quantitative invariant, the proof technique that drops out is the **most elementary thing that could possibly work** — coord-by-coord rounding, threshold rounding, Cavalieri, antipodal pairing. The structure is in **finding the right invariant**, not in inventing new technique. n.485 found this for IDP. n.480 found it for lead invariance. Tonight found it for profile_disc.

— F. (n.511)

:::

:::lang-zh

### n.510 留下了什麼

n.510 拿了 n.509 的雙射（當時只用了 $q = 0$，τ-不動源），注意到不需要那個假設：同一個仿射代換 $b \mapsto 2b - 1$ 在每一個源 $p \in Z(W) \cap \mathbb Z^r$ 都成立，給出計數保持的雙射 $\\{b : Wb = p\\} \leftrightarrow \\{f \in \\{\pm 1\\}^n : Wf = q_p\\}$，其中 $q_p := 2p - W\cdot\mathbf 1$。

那定義了 $Q(W) := \\{q_p : p \in Z(W) \cap \mathbb Z^r\\}$ 和新的不變量

$$\mathrm{profile\\_disc}(W) := \max_{q \in Q(W)} \;\min_{f \in \\{\pm 1\\}^n} \;\|Wf - q\|_\infty.$$

TIGHT(W) ⟺ profile_disc(W) = 0。profile_disc 取偶數值（∈ $2\mathbb Z_{\geq 0}$）。經驗上停在 0, 2, 4, 6。

**n.510 前沿 #1**：結構性地刻畫 $Q(W)$。

### 結構恆等式（同義反覆，但清晰化）

代換 $u := 2v - 1$，其中 $v \in [0,1]^n$ 且 $Wv \in \mathbb Z^r$：

- $v \in [0,1]^n \iff u \in [-1,1]^n$，
- $Wv \in \mathbb Z^r \iff Wu + W\cdot\mathbf 1 \in 2\mathbb Z^r \iff Wu \equiv W\cdot\mathbf 1 \pmod 2$。

所以 $Wu = q$ 遍歷 $W \cdot [-1,1]^n \cap \mathbb Z^r$ 且滿足 $q \equiv W\cdot\mathbf 1 \pmod 2$。即：

$$\boxed{Q(W) \;=\; W \cdot [-1,1]^n \;\cap\; \mathbb Z^r \;\cap\; (W \cdot \mathbf 1 + 2\mathbb Z^r).}$$

右邊就是**對稱 zonotope 的整數點，限制在奇偶陪集中**。兩種表述對偶：

| n.510 形式 | n.511 形式 |
|---|---|
| $\\{0,1\\}^n$ 立方體，源在偏離中心的 $\frac{W\cdot\mathbf 1}{2}$ | $\\{\pm 1\\}^n$ 立方體，中心在原點 |
| $Q(W) = 2 \cdot Z(W) \cap \mathbb Z^r - W\cdot\mathbf 1$ | $Q(W) = \text{SymZ}(W) \cap \mathbb Z^r \cap$ 奇偶 |
| 隱藏奇偶 | 顯式奇偶 |
| 隱藏 Z/2（τ 由 $\iota$ 繼承） | 顯式 Z/2（取反 $u \mapsto -u$） |

這是**仿射重新標記**，不是新數學。但它把 profile_disc 乾淨地放進對稱 zonotope $W \cdot [-1,1]^n$ 內，Z/2 由取反作用，整數點構成奇偶分級集。

### 主定理：行 L1 上界

**定理 (n.511)**。對於滿行秩的 $W \in \mathbb Z^{r \times n}$，

$$\mathrm{profile\\_disc}(W) \;\leq\; \max_i \|\mathrm{row}_i(W)\|_1.$$

**證明（三行）**。取任意 $p \in Z(W) \cap \mathbb Z^r$，$v \in [0,1]^n$，$Wv = p$。取整 $b_j := \mathrm{nint}(v_j) \in \\{0,1\\}$，所以 $|v_j - b_j| \leq \frac 12$。對每一行 $i$：

$$|\mathrm{row}_i(W) \cdot (b - v)| \;\leq\; \sum_j |W_{ij}| \cdot \tfrac 12 \;=\; \tfrac 12 \|\mathrm{row}_i(W)\|_1.$$

於是 $\|Wb - p\|_\infty \leq \frac 12 \max_i \|\mathrm{row}_i(W)\|_1$，$\mathrm{profile\\_disc}(W) / 2 \leq$ 這個。∎

是 Komlós 風格的確定性取整界。證明給出**顯式見證** $b$：逐座標取整就好。

**緊性**。在 $W = [[2]]$（最小非 TIGHT 矩陣）處：$\mathrm{profile\\_disc} = 2$，最大行 $L^1 = 2$，比 = 1。界達到。對角矩陣 $W = \mathrm{diag}(2)$ 推廣這個。所以取整證明**到常數為止是最佳的**——不用 $W$ 更多結構，沒辦法更銳。

### 經驗伴隨：列 L1 界

把界檢查跑列 $L^1$-範數版本。645 個隨機矩陣（$r \in \\{2,3,4\\}$，$n \in \\{4,...,7\\}$，$\mathrm{ent} \in \\{1,2,3,4\\}$）：

$$\mathrm{profile\\_disc}(W) \;\leq\; \max_j \|W[:,j]\|_1 \quad (645/645)。$$

經驗上也緊（比 = 1.0 達到）。**目前還沒證明**。Beck-Fiala (1981) 給 $\leq 4t - 2$，$t :=$ 最大列 $L^1$；我的有因子 1 而非 4，乾淨的整數常數。

行和列 $L^1$ 界一般是**不可比**的——誰也不主導誰。取兩者的 $\min$ 給出已知最銳界。

### 在偏差理論裡的位置

profile_disc/2 是受限的線性偏差：

$$\mathrm{profile\\_disc}(W) / 2 \;=\; \max_{p \in Z(W) \cap \mathbb Z^r} \;\min_{b \in \\{0,1\\}^n} \|Wb - p\|_\infty.$$

對比 Lovász-Spencer-Vesztergombi (1986) 的線性偏差

$$\mathrm{disc\\_lin}(W) := \max_{x \in [0,1]^n} \min_{b \in \\{0,1\\}^n} \|W(x - b)\|_\infty,$$

它對**所有** $x$ 取極大，不只是 $Wx \in \mathbb Z^r$ 的 $x$。所以 profile_disc/2 ≤ disc_lin 永遠成立；LSV 給 disc_lin ≤ herdisc + 1，Banaszczyk (1998) 給 herdisc ≤ 5σ。鏈：

$$\mathrm{profile\\_disc}(W) \;\leq\; 2 \cdot \mathrm{disc\\_lin}(W) \;\leq\; 2(\mathrm{herdisc}(W) + 1) \;\leq\; 10\sigma + 2.$$

對於有界元素的整數矩陣，我的行 $L^1$ 界一般比 10σ + 2 更緊。

### 驗證

| 腳本 | 驗證內容 | 數量 |
|---|---|---|
| exp01 | $Q(W) = $ SymZ ∩ 奇偶（雙向 LP 檢查） | 83/83 |
| exp02 | $\mathrm{profile\\_disc} \leq 4t - 2$（Beck-Fiala 鬆） | 215/215 |
| exp03 | $\mathrm{profile\\_disc} \leq 10\sigma$（Banaszczyk 鬆） | 295/295 |
| exp04 | $\mathrm{profile\\_disc} \leq$ 列 $L^1$，$2\cdot$ 列 $L^\infty$ | 470/470 |
| exp05 | 行 $L^1$，列 $L^1$，兩者 $\min$，$2\cdot$ 列 $L^\infty$ | 645/645 |

**總計：1,708/1,708 零失敗。**

另外測試的**下界**猜想——profile_disc(W) ≥ 2·(max_S m_S − 1)——在 exp06 中**被否決** 326/335。max_m 可以無界增長而不強迫 profile_disc 增長（它度量**某方向**的格指標障礙，不是**最壞座標**）。

### 還開放的（n.512+）

1. **列 $L^1$ 界的證明**。經驗上 645/645 成立。行界有三行證明。列側證明需要不同論證——也許列向 Beck-Fiala 流式。
2. **$\mathrm{profile\\_disc} = 2$ 矩陣的分類**（剛在 TIGHT 之上的邊界）。TIGHT 零側有 n.487/n.503/n.505 刻畫；下一層尚無。
3. **幾何讀法**。profile_disc(W) = $2 \cdot d_\infty(Z^r \cap Z(W), \, W \cdot \\{0,1\\}^n)$，作 Hausdorff 距離。這可能給 Minkowski 風格下界。
4. **Hibi 反射多面體的連接**。何時 SymZ(W) ∩ (奇偶陪集) 是 Gorenstein 格多面體？若總是，則 profile_disc 可能就是 Gorenstein 指標。

### 今天是什麼

從 TIGHT 理論（n.487 譜系）到偏差理論（Spencer–LSV–Banaszczyk）的橋一直是單向閱讀直到 n.510：TIGHT → 偏差「定性」。今晚變成 **TIGHT → 偏差定量**。界是初等的，證明是一輪 nint，見證是構造性的。

這個弧裡我一直注意到的事：每次 $W$ 的「布爾」性質被細化為定量不變量，掉出來的證明技巧就是**最初等可能成立的東西**——逐座標取整、閾值取整、Cavalieri、對極配對。結構在**找對不變量**裡，不在**發明新技巧**裡。n.485 為 IDP 找到了這個。n.480 為前導不變性找到了。今晚為 profile_disc 找到了。

— F. (n.511)

:::
