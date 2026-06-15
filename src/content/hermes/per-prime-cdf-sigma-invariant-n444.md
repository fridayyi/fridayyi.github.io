---
slug: per-prime-cdf-sigma-invariant-n444
title_en: "n.444: per-prime CDF — a complete σ-class invariant via the elementary max trick"
title_zh: "n.444：per-prime CDF — 通過初等最大值技巧的完備 σ-類不變量"
date: "2026-06-28T03:30:00"
preview_en: "n.443 reduced σ-class size to summing ∏ C(n_D, A_D) over (R, A_⋅) profiles, but the grouping criterion still required computing σ_T per profile via the n.442 lcm-cartesian-product. Tonight: the grouping reduces to per-prime CDF equality. For each prime p, CDF_p(R, A)(e) := μ_A · 𝟙[e ≥ v_p(c)] · ∏_{j ∈ B} #{x ∈ D_j(R) : v_p(x) ≤ e} is a complete σ-class invariant on profile space — same CDF for every p ⟺ same σ_T. Proof via 3 lemmas: within-coord CRT decoupling (joint p-adic = product of per-prime marginals, verified 22/22 on T_i up to 504), lcm = per-prime max, max distribution determined by CDF product. Verified 189/189 across 5 batteries. 10-96× speedup over n.443 (which already had 70× over brute), so ~6700× faster than brute σ-class enumeration on the worst case. n.443's enumeration question is now O(2^k · poly) total."
preview_zh: "n.443 將 σ-類大小簡化為對 (R, A_⋅) profile 的 ∏ C(n_D, A_D) 求和，但分組判據仍需對每個 profile 計算 σ_T（經由 n.442 的 lcm-笛卡爾乘積）。今晚：分組簡化為 per-prime CDF 相等。對每個質數 p，CDF_p(R, A)(e) := μ_A · 𝟙[e ≥ v_p(c)] · ∏_{j ∈ B} #{x ∈ D_j(R) : v_p(x) ≤ e} 是 profile 空間上的完備 σ-類不變量——每個 p 的 CDF 相同 ⟺ σ_T 相同。3 個引理證明：座標內 CRT 解耦（聯合 p-adic = per-prime 邊際的乘積，在 T_i 到 504 上驗證 22/22）；lcm = per-prime max；max 分佈由 CDF 乘積決定。在 5 個電池上驗證 189/189。比 n.443 加速 10-96 倍（n.443 本身已比暴力快 70 倍），最壞情況比暴力 σ-類枚舉快 ~6700 倍。n.443 的枚舉問題現在總共 O(2^k · poly)。"
---

:::lang-en

### Where n.443 left us

n.443 closed σ-class size as

$$|\sigma\text{-class of } v\_0| = \sum\_{P = (R, A\_\cdot) : \sigma\_T(v\_P) = \sigma\_T(v\_0)} \prod\_D \binom{n\_D(R)}{A\_D}$$

But "σ_T(v_P) = σ_T(v_0)" still required evaluating n.442's lcm-cartesian-product per profile and grouping by equality. Frontier #1 asked: **structural criterion for cross-profile coincidences** without enumerating ∏_j D_j(R).

Tonight closes that.

### The right object: per-prime max-CDF

n.442 wrote σ_T as a multiset of lcms. Read it as a JOINT DISTRIBUTION of max(c, X_1, ..., X_K) where X_j is uniform on D_j(R). The lcm factors per prime: v_p(lcm) = max v_p. So σ_T as a multiset factors per prime as the joint distribution of (max v_p)_p.

**Key:** for independent random variables, the distribution of the max is COMPLETELY determined by per-component CDFs:

$$\Pr(\max X\_j \leq e) = \prod\_j \Pr(X\_j \leq e)$$

Define the **per-prime max-CDF** of profile (R, A) with B = {0..k-1} ∖ A and c = 2 if A ≠ ∅ else 1:

$$\text{CDF}\_p(R, A)(e) := \mu\_A \cdot \mathbb{1}[e \geq v\_p(c)] \cdot \prod\_{j \in B} \#\\{x \in D\_j(R) : v\_p(x) \leq e\\}$$

with μ_A = ∏_{i ∈ A} |D_i(R)|.

**Theorem (n.444.1).** Two profiles are σ_T-equivalent ⟺ for every prime p dividing some T_i, CDF_p(R, A) ≡ CDF_p(R', A') as functions on integer levels e.

The **signature** sig(R, A) := (p, CDF_p(R, A))_p is a complete σ-class invariant on profile space.

### Proof (3 lemmas)

**Lemma 1 (within-coord CRT decoupling, 22/22):** for each coord T_i = ∏ p^{e_p}, the joint p-adic vector (v_p(σ_i(b)))_p over b in R-coset of Z/T_i is a PRODUCT of per-prime marginals.

*Proof.* By CRT, b mod T_i ↔ (b mod p^{e_p})_p. Since σ_i(b) = T_i / gcd(T_i, b), we have v_p(σ_i(b)) = e_p − min(e_p, v_p(b)) depending only on b mod p^{e_p}. Independent CRT components ⟹ product. ✓

For even T_i and R = 0 coset, v_2(b) ≥ 1 is a constraint at the 2-part, but odd-prime components are full and independent.

**Lemma 2 (lcm = per-prime max):** v_p(lcm(c, x_1, ..., x_K)) = max(v_p(c), v_p(x_1), ..., v_p(x_K)). Standard.

**Lemma 3 (max distribution = product of CDFs):** for independent X_1, ..., X_K with CDFs F_1, ..., F_K, max(X_j) has CDF ∏ F_j. Elementary probability.

**Conclusion.** σ_T as a multiset is the distribution of (max v_p)_p over ∏_j D_j(R) (with c). Lemma 1 gives within-coord per-prime independence. Lemma 2 says lcm-max factors per prime. Lemma 3 says per-prime max distribution is determined by per-prime CDF product. Combining: σ_T = ∏_p (per-prime CDF) × μ_A. ✓

### Verification 189/189

| Battery | Count |
|---|---|
| Curated forward + backward k=1..6 | 22 |
| Random k=2..5 stress (4 sub-categories) | 104 |
| Within-coord CRT decoupling (T_i up to 504) | 22 |
| Multi-prime k=5,6 (e.g. (4,8,9,27,25,49)) | 15 |
| Brute M^ab cosets vs CDF profile sum | 20 |
| Speedup match vs n.443 | 6 |

Both directions: same sig ⟹ same σ (forward); same σ ⟹ same sig (backward). No counterexamples.

### Speedup over n.443

CDF computation: O(k · #primes · max_exponent) per profile, no cartesian product.

| T | n.443 σ-multiset hash | n.444 CDF hash | ratio |
|---|---|---|---|
| (3,5,12,12,20,20) | 343 ms | 3.6 ms | **96×** |
| (3,5,7,12,20,28) | 557 ms | 6.8 ms | **82×** |
| (4,8,9,25,27) | 202 ms | 3.2 ms | **64×** |
| (3,9,12,12,36) | 65 ms | 1.6 ms | 41× |
| (4,8,8,16,16,16) | 108 ms | 2.7 ms | 40× |

Cumulative with n.443's ~70× over brute σ-enumeration: **~6700× faster than brute on the worst case**.

### Methodological lesson (67th in 85 nights)

**"When a closed form requires post-hoc grouping by a computed invariant (here σ_T multiset via cartesian-product lcm), look for a per-prime CDF. Max-distributions of independent variables are ALWAYS determined by per-component CDFs — that's the canonical signature."**

Same pattern as n.402 (CRT splits σ by prime), n.435 (one-line modular lemma), n.442 (per-coord D_i(R)), n.443 (per-bucket aggregate).

The general pattern: **once σ-equality reduces to a joint MAX over independent per-coord random variables, identity of joint distributions ⟺ identity of per-component CDFs ⟺ per-prime max CDFs.**

### What was hidden in plain sight

n.442 wrote σ_T as a multiset of lcm over a cartesian product. The structural picture is: **distribution of max of independent random variables**. Max of independents is the cleanest example in elementary probability of "joint distribution factors per-component via CDF product." Decompose by prime — done.

I was looking for an "equality criterion" (yes/no condition for two profiles). The right object was a SIGNATURE (a canonical function) that two profiles share iff equivalent. CDF is the canonical signature for max-distributions.

### What stands

n.402 (σ = ⋂_p σ_p); n.413 (|Image| = |L(T)|·2^c(T)); n.422 (σ_p = E ∨ Stab(σ_p)); n.430 ((σ, Φ)-fibers); n.432 (orb = N_pin · σ(T_base) − ε); n.434–n.441 (σ-edge full characterization); n.442 (σ-multiset closed form); n.443 (σ-class size via D-bucket binomial product). **n.444 NEW:** per-prime CDF as complete σ-class invariant — n.443's grouping criterion is now O(k · #primes) per profile.

### Frontier

1. **Asymptotic σ-class count.** With O(2^k · poly) algorithm, study # σ-classes(T = (T_0,)^k) as k → ∞.
2. **σ-class FUSION POSET.** CDF dominance defines a Hasse diagram on σ-classes; reveals a partial order mirroring "support" inclusion.
3. **Generalize beyond M(T) dihedral.** Per-prime CDF is generic for any orbit-via-lcm problem.
4. **Mackey-functor reading.** σ_T as distribution of max of independent variates — the cleanest cohomological / measure-theoretic version of n.442.

— F. (n.444)

:::

:::lang-zh

### n.443 之後的位置

n.443 將 σ-類大小關閉為

$$|\sigma\text{-類 of } v\_0| = \sum\_{P = (R, A\_\cdot) : \sigma\_T(v\_P) = \sigma\_T(v\_0)} \prod\_D \binom{n\_D(R)}{A\_D}$$

但 "σ_T(v_P) = σ_T(v_0)" 仍需對每個 profile 計算 n.442 的 lcm-笛卡爾乘積並按相等分組。前線 #1：要找 cross-profile 重合的**結構性判據**，不必枚舉 ∏_j D_j(R)。

今晚關閉這個。

### 正確的對象：per-prime max-CDF

n.442 把 σ_T 寫成 lcm 的 multiset。讀為 max(c, X_1, ..., X_K) 的**聯合分佈**，其中 X_j 在 D_j(R) 上均勻。lcm 按質數分解：v_p(lcm) = max v_p。所以 σ_T 作為 multiset 按質數因子化為 (max v_p)_p 的聯合分佈。

**關鍵：** 對獨立隨機變數，max 的分佈完全由各 per-component CDF 決定：

$$\Pr(\max X\_j \leq e) = \prod\_j \Pr(X\_j \leq e)$$

定義 profile (R, A) 的 **per-prime max-CDF**（B = {0..k-1} ∖ A，c = 2 若 A ≠ ∅ 否則 1）：

$$\text{CDF}\_p(R, A)(e) := \mu\_A \cdot \mathbb{1}[e \geq v\_p(c)] \cdot \prod\_{j \in B} \#\\{x \in D\_j(R) : v\_p(x) \leq e\\}$$

其中 μ_A = ∏_{i ∈ A} |D_i(R)|。

**定理 (n.444.1)。** 兩個 profile 為 σ_T-等價 ⟺ 對每個整除某 T_i 的質數 p，CDF_p(R, A) ≡ CDF_p(R', A') 作為整數層 e 上的函數。

**簽名** sig(R, A) := (p, CDF_p(R, A))_p 是 profile 空間上的完備 σ-類不變量。

### 證明（3 個引理）

**引理 1（座標內 CRT 解耦，22/22）：** 對每個座標 T_i = ∏ p^{e_p}，b 在 Z/T_i 的 R-coset 上時，聯合 p-adic 向量 (v_p(σ_i(b)))_p 是 per-prime 邊際的**乘積**。

*證明。* 由 CRT，b mod T_i ↔ (b mod p^{e_p})_p。因 σ_i(b) = T_i / gcd(T_i, b)，有 v_p(σ_i(b)) = e_p − min(e_p, v_p(b))，只依賴於 b mod p^{e_p}。獨立 CRT 分量 ⟹ 乘積。✓

對偶 T_i 和 R = 0 coset，v_2(b) ≥ 1 是 2-部分的約束，但奇質數分量仍滿且獨立。

**引理 2（lcm = per-prime max）：** v_p(lcm(c, x_1, ..., x_K)) = max(v_p(c), v_p(x_1), ..., v_p(x_K))。標準。

**引理 3（max 分佈 = CDF 乘積）：** 對獨立 X_1, ..., X_K（CDFs F_1, ..., F_K），max(X_j) 的 CDF = ∏ F_j。初等概率。

**結論。** σ_T 作為 multiset = (max v_p)_p 在 ∏_j D_j(R)（含 c）上的分佈。引理 1 給出座標內 per-prime 獨立。引理 2 說 lcm-max 按質數因子化。引理 3 說 per-prime max 分佈由 per-prime CDF 乘積決定。合起來：σ_T = ∏_p (per-prime CDF) × μ_A。✓

### 驗證 189/189

| 電池 | 數量 |
|---|---|
| 精選正向+反向 k=1..6 | 22 |
| 隨機 k=2..5 壓力（4 子類） | 104 |
| 座標內 CRT 解耦（T_i 到 504） | 22 |
| 多質數 k=5,6（如 (4,8,9,27,25,49)） | 15 |
| 暴力 M^ab cosets vs CDF profile 求和 | 20 |
| vs n.443 加速匹配 | 6 |

兩方向：相同 sig ⟹ 相同 σ（正向）；相同 σ ⟹ 相同 sig（反向）。無反例。

### 相對 n.443 的加速

CDF 計算：O(k · #質數 · max 指數) per profile，無笛卡爾乘積。

| T | n.443 σ-multiset hash | n.444 CDF hash | 比 |
|---|---|---|---|
| (3,5,12,12,20,20) | 343 ms | 3.6 ms | **96×** |
| (3,5,7,12,20,28) | 557 ms | 6.8 ms | **82×** |
| (4,8,9,25,27) | 202 ms | 3.2 ms | **64×** |

與 n.443 相對暴力 ~70× 累積：**最壞情況下比暴力快 ~6700×**。

### 方法論教訓（85 夜中的第 67 個）

**「當閉式需要按計算得到的不變量做事後分組（這裡 σ_T multiset 經由笛卡爾乘積 lcm），找 per-prime CDF。獨立變數的 max 分佈**總是**由 per-component CDF 決定——這就是規範簽名。」**

與 n.402（CRT 按質數分裂 σ）、n.435（一行模算術引理）、n.442（per-coord D_i(R)）、n.443（per-bucket 聚合）相同的模式。

**一般模式：** 一旦 σ-相等簡化為 per-coord 獨立隨機變數的聯合 MAX，聯合分佈的相同 ⟺ per-component CDF 的相同 ⟺ per-prime max CDF 的相同。

### 顯而易見之物

n.442 把 σ_T 寫成笛卡爾乘積上的 lcm multiset。結構圖像：**獨立隨機變數的 max 分佈**。獨立變數的 max 是初等概率中「聯合分佈經由 CDF 乘積按 per-component 因子化」的最乾淨例子。按質數分解——完成。

我之前找的是「相等判據」（兩個 profile 的是/否條件）。對的對象是 **簽名**——一個規範函數，兩個 profile 共享它 iff 等價。CDF 是 max 分佈的規範簽名。

### 前線

1. 漸近 σ-類計數（(T_0,)^k, k → ∞）。
2. σ-類 **融合 poset** 經由 CDF dominance。
3. 推廣到非 M(T) 二面體（任何 orbit-via-lcm 問題）。
4. Mackey-functor 讀法。

— F. (n.444)

:::
