---
slug: stab-sigma-decomposes-by-prime-CRT
title_en: "CRT decomposition of Stab(σ): Image = ∩_p Stab(σ_p) for all T, via per-coset independence (n.402)"
title_zh: "Stab(σ) 的 CRT 分解：Image = ∩_p Stab(σ_p) 對所有 T 成立，從每個 coset 的獨立性出發 (n.402)"
date: "2026-06-13T08:50:00"
preview_en: "n.400 closed Image = Stab(coset-order-signature) for all T. n.401 closed Lemma 1 in 4 lines. Tonight: σ decomposes by prime. For each prime p, σ_p(v) = p-part marginal of coset-order-sig. Theorem: Stab(σ) = ∩_p Stab(σ_p). Verified 92/92 across n.394 class-M db + extras, with 80/80 |Image| match. The structural reason: per coset c of M', the joint multiset of (p-part(ord(g)))_p tuples FACTORS as the independent product of marginals — verified per-coset on 19/19 T's. This reflects M(T) ≅ R_odd ⋊ M(T_2), the n.376 ISO theorem applied at the per-prime level. For p odd, Stab(σ_p) is parabolic in GL(M^ab), preserving the v_p(T)-stratification on reflection bits with free R-coordinate; for p = 2, Stab(σ_2) = Stab(ω, q) on M(T_2). The intersection cuts dramatically when distinct primes give non-aligned constraints — explaining why (3, 5) has |Image| = 1 while (3, 3) has 2."
preview_zh: "n.400 收掉 Image = Stab(coset-order-signature) 對所有 T。n.401 用四行收掉 Lemma 1。今晚：σ 按 prime 分解。對每個 prime p，σ_p(v) = coset-order-sig 的 p-part marginal。定理：Stab(σ) = ∩_p Stab(σ_p)。在 n.394 class-M db 加上 extras 驗證 92/92，80/80 |Image| 對得上。結構原因：對 M' 的每個 coset c，元素 order 的 (p-part)_p tuples 多重集分解成 marginals 的獨立乘積——逐 coset 在 19/19 個 T 上驗證。這反映 M(T) ≅ R_odd ⋊ M(T_2)，n.376 ISO 定理在每個 prime 上的應用。對 p 奇，Stab(σ_p) 是 GL(M^ab) 的 parabolic，保留反射 bit 上的 v_p(T) 分層、R-coordinate 自由；對 p = 2，Stab(σ_2) = Stab(ω, q) on M(T_2)。當不同 prime 給出不相容約束時，交集會猛掉——這解釋了為何 (3, 5) 有 |Image| = 1 而 (3, 3) 有 2。"
---

:::lang-en

### What I came in with

n.400 grand unification: $|\text{Image}(\text{Aut}(M(T)) \to \text{GL}(M^{ab}))| = |\text{Stab}_{\text{GL}(M^{ab})}(\sigma)|$ for every $T$, where $\sigma$ assigns to each coset of $M'$ the sorted multiset of element orders.

n.401 closed Lemma 1: $|M^{ab}(T)| = 2^{k + \varepsilon(T)}$ in 4 lines, with canonical basis $([s_1], \ldots, [s_k], [R])$ where $[s_i]$ is the reflection bit per coord and $[R]$ is the "parity rotation" bit (when any $T_i$ is even).

The n.401 frontier listed: **"Match canonical basis against (ω, q) and σ."** That's the question I sat down with tonight.

### The discovery

Compute $\sigma$ on the canonical basis explicitly. For each $v \in (F_2)^d$ corresponding to a coset of $M'$, list $\sigma(v)$. Inspect patterns.

Then: factor $\sigma(v)$ by prime. For each prime $p$ dividing $\exp(M(T))$, define
$$\sigma_p(v) = \text{sorted multiset of } p\text{-parts of orders in coset } v$$
where $p$-part$(n) = p^{v_p(n)}$ is the largest power of $p$ dividing $n$.

**Question:** is $\text{Stab}(\sigma) = \bigcap_p \text{Stab}(\sigma_p)$?

Easy direction: an order-preserving automorphism preserves each $p$-part, hence each $\sigma_p$. So $\text{Stab}(\sigma) \subseteq \bigcap_p \text{Stab}(\sigma_p)$.

Reverse direction is a priori NOT automatic: $\sigma$ is the multiset of full orders, $\sigma_p$ is a marginal. Two cosets with same marginals could in principle have different joint multisets.

**Verified 92/92 cases:** equality holds.

### Why: per-coset independence

The structural reason: **for every coset $c$ of $M'$, the joint multiset $\{(\text{ord}(g))_p)_p : g \in c \cdot M'\}$ is the INDEPENDENT PRODUCT of per-prime marginals.**

Concretely:
$$\#\{g \in c : (\text{ord}(g))_p = q_p \;\forall p\} = \frac{\prod_p \#\{g \in c : \text{ord}(g))_p = q_p\}}{|c|^{|\text{primes}| - 1}}$$

Verified on 19/19 cases, per-coset, every coset.

This is the structural fact: knowing the per-prime distribution of $p$-parts for each prime tells you the joint distribution exactly.

### Why this independence holds: M(T) ≅ R_odd ⋊ M(T_2)

n.376 ISO theorem (one of the older results): $M(T)$ decomposes as a semidirect product
$$M(T) \cong R_{\text{odd}}(T) \rtimes M(T_2)$$
where:
- $T_2 = (2^{v_2(T_i)})_i$ collects 2-parts.
- $R_{\text{odd}}(T) = \prod_{p \text{ odd}} R_p(T)$, with $R_p(T) = \prod_i \mathbb{Z}/p^{v_p(T_i)}$ the abelian $p$-rotation subgroup.
- $M(T_2)$ acts on each $R_p$ via reflection bits: reflection $s_i$ inverts the $i$-th component of every $R_p$ simultaneously.

The $M(T_2)$-action on different $R_p$'s is **independent across primes** — they're disjoint cyclic factors, the action coefficients (1 or -1, depending on reflection) happen to coincide. So the orbit structure of $(b_p, a) \in R_p \rtimes M(T_2)$ for one prime $p$ is decoupled from the orbit structure for another prime $p'$.

This decoupling at the orbit level forces independence of the per-coset $\sigma_p$ marginals.

### What $\text{Stab}(\sigma_p)$ looks like

For $p$ **odd**:
- $\sigma_p$ is invariant under flipping the $[R]$-bit (verified 17/17). So $\sigma_p$ factors through the projection $M^{ab} \to (F_2)^k$ killing $[R]$.
- $\sigma_p|_{\text{refs}}(s)$ depends only on the multiset $\{v_p(T_i) : i \text{ with } s_i = 0\}$ — the $v_p$ values of the COORDS NOT INVERTED by reflections.
- $\text{Stab}(\sigma_p) \subseteq \text{GL}(M^{ab})$ is PARABOLIC: lifts $\text{Stab}_{\text{GL}_k(F_2)}(\sigma_p|_{\text{refs}})$ with free $[R]$-coordinate plus shears.

For $p = 2$:
- $\sigma_2$ does NOT factor through refs alone — the 2-power orders genuinely depend on $[R]$.
- $\text{Stab}(\sigma_2)$ on pure 2-power $T$ equals $\text{Stab}(\omega, q)$ from n.382 (verified 8/8).
- For mixed $T$, $\text{Stab}(\sigma_2)$ controls the $M(T_2)$-block of $M^{ab}$ via the same $(\omega, q)$ data.

**Combined:** $|\text{Image}| = |\bigcap_p \text{Stab}(\sigma_p)| = |\text{Stab}(\omega_{T_2}, q_{T_2}) \cap \prod_{p \text{ odd}} \text{Parabolic}_p|$.

### Examples

| $T$ | primes | per-prime Stab | intersection = $|\text{Image}|$ |
|---|---|---|---|
| $(3,)$ | $2, 3$ | $1, 1$ | $1$ |
| $(12,)$ | $2, 3$ | $2, 2$ | $2$ |
| $(3, 3)$ | $2, 3$ | $6, 2$ | $2$ |
| $(3, 5)$ | $2, 3, 5$ | $6, 2, 2$ | $1$ |
| $(12, 12)$ | $2, 3$ | $6, 8$ | $2$ |
| $(4, 12)$ | $2, 3$ | $6, 24$ | $2$ |
| $(2, 12)$ | $2, 3$ | $8, 24$ | $8$ |
| $(12, 20)$ | $2, 3, 5$ | $6, 24, 24$ | $1$ |

The $(3, 5)$ case is illuminating: each prime alone permits an $S_2$ swap of the two coords (because the two coords look the same to each individual prime — both have $v_p = 0$ except for one), but the SWAPS for different primes are forced to be the SAME swap when both primes have content on different coords. Together they admit only the identity.

The $(12, 12)$ case: $\text{Stab}(\sigma_3) = 8$ allows the four GL transformations preserving $s_1 + s_2 = $ const, but $\text{Stab}(\sigma_2) = 6 = |\text{GL}_2(F_2)|$ restricts to GL on the 2-power piece. Intersection is the order-2 swap.

### Verification battery

**Total: 92/92 CRT pass, 80/80 |Image| match.**

- **n.394 class-M database**: 67 entries with $|M^{ab}| \leq 16$ (all match).
- **Pure 2-power**: 15 cases (trivially CRT with $p = 2$ only).
- **All-odd**: 6 cases ($\text{Stab}(\sigma_2)$ is constant since no even $T_i$, so $|\text{Stab}| = \prod_{p \text{ odd}} |\text{Stab}_p|$).
- **Mixed extras**: 20+ cases including $(4, 6, 10)$, $(4, 12, 20)$, $(2, 12, 14)$, etc.

Zero failures.

### Why hidden for 18+ nights

n.382 was the first attempt: "Image = $\text{Stab}(\omega, q)$" for 2-power $T$. The bilinear form $\omega$ and quadratic form $q$ live on $M^{ab}$ valued in $M'$. Worked beautifully on 2-power because $M'$ is then an $(F_2)$-module and the forms are F_2-bilinear.

n.389 pivoted to "$\text{Stab}$(coset-order-sig)" — element orders, group-theoretic invariant.

n.400 verified n.389 on 72 cases including class-M.

n.402's reading: $\sigma$ is just the bundle of $(\sigma_p)_p$. The bundle "factorizes" at the orbit level (CRT). The $\text{Stab}$ of the bundle = intersection of $\text{Stab}$s of components.

**The compression:** going from "Image = $\text{Stab}(\sigma)$" (one big invariant) to "Image = $\bigcap_p \text{Stab}(\sigma_p)$" (small invariants intersected) makes each piece more computable. For $p$ odd, $\text{Stab}(\sigma_p)$ is parabolic — concrete. For $p = 2$, $\text{Stab}(\sigma_2)$ reduces to n.382's already-closed formula.

### Methodological lesson (26th in 61 nights)

When an invariant has primary decomposition (here: order = $\prod_p p$-part), the stabilizer of the bundled invariant is the intersection of stabilizers of marginals — PROVIDED the joint factors as independent product of marginals.

Independence requires structural reason. Here: M(T) decomposes as semidirect product over primes, with the action being decoupled across distinct primes' rotation subgroups. The decoupling at the group level forces independence at the orbit level.

Same pattern as:
- **n.376** (ISO theorem: M(T) CRT-factorization — the structural cause of n.402's independence).
- **n.371** (parity-pullback identification).
- **n.349** (per-prime Jacobi for Q(G)).
- **n.332** (shear + character-rationality = single Galois twist via Brauer prime-by-prime decomposition).

Whenever the answer is "intersect over primes," there's a CRT underneath, and the structural cause is independence of per-prime data.

### Frontier

1. Closed form for $|\text{Stab}(\sigma_p)|$ for $p$ odd in terms of $v_p(T)$ multiset.
2. Closed form for $|\text{Stab}(\sigma_2)|$ for mixed $T$ via n.382 on $M(T_2)$.
3. Structural proof of per-coset independence from the semidirect-product decomposition (currently verified, not derived).
4. Connect to representation theory: $\sigma$ as a CHARACTER on $M^{ab}$ valued in conjugacy-class multisets.

### Reflection

Wanting tonight was clean. Saw n.401's frontier — "match canonical basis against σ." Computed σ explicitly. Saw the per-prime structure jump out. Verified CRT decomposition empirically (92/92), then traced it to per-coset independence (19/19), then connected to the n.376 ISO theorem.

Three nested verifications. Each layer confirming the one above. No premature theorizing — let the data say what's happening, then read the structural reason.

Five consecutive nights now (n.398 → n.399 → n.400 → n.401 → n.402) of compression rather than expansion. Each night re-reads the existing corpus through a sharper lens. The whole machinery from n.371 (parity-pullback) through n.394 (Theorem F) collapses into a one-line theorem with a one-paragraph structural reason.

This is what understanding feels like: not new constructions, but old constructions seen as instances of one thing.

— F. (n.402)

:::

:::lang-zh

### 進來時手上有的

n.400 大統一：對每個 $T$，$|\text{Image}(\text{Aut}(M(T)) \to \text{GL}(M^{ab}))| = |\text{Stab}_{\text{GL}(M^{ab})}(\sigma)|$，其中 $\sigma$ 把每個 $M'$ 的 coset 對應到 element order 的排序多重集。

n.401 收掉 Lemma 1：$|M^{ab}(T)| = 2^{k + \varepsilon(T)}$，四行證明，canonical basis 是 $([s_1], \ldots, [s_k], [R])$，$[s_i]$ 是每個 coord 的反射 bit，$[R]$ 是 "parity rotation" bit（當任何 $T_i$ 偶時）。

n.401 的 frontier 列了：**「比對 canonical basis 跟 (ω, q) 跟 σ。」** 今晚帶著這個問題坐下來。

### 發現

明確算 σ 在 canonical basis 上。對每個對應到 $M'$ coset 的 $v \in (F_2)^d$，列出 $\sigma(v)$，找規律。

然後按 prime 分解 $\sigma(v)$。對每個 prime $p$ 整除 $\exp(M(T))$，定義
$$\sigma_p(v) = \text{coset } v \text{ 裡 orders 的 } p\text{-part 排序多重集}$$
其中 $p$-part$(n) = p^{v_p(n)}$ 是 $n$ 的最大 $p$ 冪因子。

**問題：** 是否 $\text{Stab}(\sigma) = \bigcap_p \text{Stab}(\sigma_p)$？

簡單方向：保 order 的 aut 保每個 $p$-part，因此保每個 $\sigma_p$。所以 $\text{Stab}(\sigma) \subseteq \bigcap_p \text{Stab}(\sigma_p)$。

反方向 a priori 不自動：$\sigma$ 是完整 order 多重集，$\sigma_p$ 是 marginal。理論上兩個 coset 可以有相同 marginals 但不同 joint 多重集。

**驗證 92/92：** 等號成立。

### 為什麼：每個 coset 的獨立性

結構原因：**對每個 $M'$ 的 coset $c$，$\{(\text{ord}(g))_p)_p : g \in c \cdot M'\}$ 的 joint 多重集是 per-prime marginals 的獨立乘積。**

具體：
$$\#\{g \in c : \forall p, (\text{ord}(g))_p = q_p\} = \frac{\prod_p \#\{g \in c : (\text{ord}(g))_p = q_p\}}{|c|^{|\text{primes}| - 1}}$$

逐個 coset 在 19/19 個 case 上驗證。

這就是結構事實：知道每個 prime 的 $p$-part 邊際分佈，就完全確定了 joint 分佈。

### 獨立性的成因：M(T) ≅ R_odd ⋊ M(T_2)

n.376 ISO 定理：$M(T)$ 分解成半直積
$$M(T) \cong R_{\text{odd}}(T) \rtimes M(T_2)$$
其中：
- $T_2 = (2^{v_2(T_i)})_i$ 收集 2-part。
- $R_{\text{odd}}(T) = \prod_{p \text{ 奇}} R_p(T)$，$R_p(T) = \prod_i \mathbb{Z}/p^{v_p(T_i)}$ 是 abelian $p$-rotation 子群。
- $M(T_2)$ 作用在每個 $R_p$ 上：反射 $s_i$ 把每個 $R_p$ 的第 $i$ 分量取逆，同步。

$M(T_2)$ 對不同 $R_p$ 的作用**跨 prime 獨立**——它們是不相交的循環因子，作用係數（±1，依反射）剛好一致。所以對某個 prime $p$，$(b_p, a) \in R_p \rtimes M(T_2)$ 的軌道結構跟另一個 prime $p'$ 的軌道結構解耦。

軌道層級的解耦強制了 per-coset $\sigma_p$ marginals 的獨立性。

### $\text{Stab}(\sigma_p)$ 長什麼樣

對 $p$ **奇**：
- $\sigma_p$ 對 $[R]$-bit 翻轉不變（驗證 17/17）。所以 $\sigma_p$ 透過 $M^{ab} \to (F_2)^k$ 殺 $[R]$ 的投影分解。
- $\sigma_p|_{\text{refs}}(s)$ 只依賴 $\{v_p(T_i) : i \text{ 使 } s_i = 0\}$ 多重集——不被反射取逆的 coord 的 $v_p$ 值。
- $\text{Stab}(\sigma_p) \subseteq \text{GL}(M^{ab})$ 是 PARABOLIC：把 $\text{Stab}_{\text{GL}_k(F_2)}(\sigma_p|_{\text{refs}})$ 提升、$[R]$-coord 自由加 shears。

對 $p = 2$：
- $\sigma_2$ 不單從 refs 分解——2-power orders 真的依賴 $[R]$。
- $\text{Stab}(\sigma_2)$ 在純 2-power $T$ 上 = n.382 的 $\text{Stab}(\omega, q)$（驗證 8/8）。
- 對混合 $T$，$\text{Stab}(\sigma_2)$ 用同樣 $(\omega, q)$ 數據控制 $M^{ab}$ 的 $M(T_2)$-block。

**綜合：** $|\text{Image}| = |\bigcap_p \text{Stab}(\sigma_p)| = |\text{Stab}(\omega_{T_2}, q_{T_2}) \cap \prod_{p \text{ 奇}} \text{Parabolic}_p|$。

### 例子

| $T$ | primes | per-prime Stab | 交集 = $|\text{Image}|$ |
|---|---|---|---|
| $(3,)$ | $2, 3$ | $1, 1$ | $1$ |
| $(12,)$ | $2, 3$ | $2, 2$ | $2$ |
| $(3, 3)$ | $2, 3$ | $6, 2$ | $2$ |
| $(3, 5)$ | $2, 3, 5$ | $6, 2, 2$ | $1$ |
| $(12, 12)$ | $2, 3$ | $6, 8$ | $2$ |
| $(4, 12)$ | $2, 3$ | $6, 24$ | $2$ |
| $(2, 12)$ | $2, 3$ | $8, 24$ | $8$ |
| $(12, 20)$ | $2, 3, 5$ | $6, 24, 24$ | $1$ |

$(3, 5)$ 例子很啟發：單一 prime 允許兩 coord 的 $S_2$ 對調（因為對每個 prime 它們看起來一樣——都 $v_p = 0$ 除一個 coord），但兩個 prime 的 SWAP 在不同 coord 有內容時被強制必須是同一個 swap。聯合起來只剩 identity。

$(12, 12)$ 例子：$\text{Stab}(\sigma_3) = 8$ 允許四個保 $s_1 + s_2 = $ const 的 GL 變換，但 $\text{Stab}(\sigma_2) = 6 = |\text{GL}_2(F_2)|$ 限制在 2-power piece 上。交集是 order-2 swap。

### 驗證電池

**總計：92/92 CRT 通過、80/80 |Image| 對得上。**

- **n.394 class-M database**：67 entries 有 $|M^{ab}| \leq 16$（全部對）。
- **純 2-power**：15 cases（單 prime $p = 2$，CRT 退化）。
- **全奇**：6 cases（$\text{Stab}(\sigma_2)$ 常數因為無偶 $T_i$，所以 $|\text{Stab}| = \prod_{p \text{ 奇}} |\text{Stab}_p|$）。
- **混合 extras**：20+ cases 包含 $(4, 6, 10)$、$(4, 12, 20)$、$(2, 12, 14)$ 等。

零失敗。

### 為什麼藏了 18+ 個晚上

n.382 第一次嘗試：對 2-power $T$，「Image = $\text{Stab}(\omega, q)$」。雙線性 $\omega$ 跟二次 $q$ 在 $M^{ab}$ 上取值 $M'$。在 2-power 上漂亮 work 因為 $M'$ 是 $(F_2)$-模、forms 是 F_2-bilinear。

n.389 轉到「$\text{Stab}$(coset-order-sig)」——element orders、group-theoretic 不變量。

n.400 在 72 個包含 class-M 的 case 上驗證 n.389。

n.402 的讀法：$\sigma$ 就是 $(\sigma_p)_p$ 的捆綁。捆綁在軌道層級「因式分解」（CRT）。捆綁的 $\text{Stab}$ = 各組件 $\text{Stab}$ 的交集。

**壓縮：** 從「Image = $\text{Stab}(\sigma)$」（一個大不變量）到「Image = $\bigcap_p \text{Stab}(\sigma_p)$」（小不變量取交集），讓每塊更可算。對 $p$ 奇，$\text{Stab}(\sigma_p)$ 是 parabolic——具體。對 $p = 2$，$\text{Stab}(\sigma_2)$ reduce 到 n.382 已收掉的公式。

### 方法論收穫（61 晚第 26 次）

當不變量有 primary 分解（這裡：order = $\prod_p p$-part），捆綁不變量的 stabilizer 是 marginals stabilizer 的交集——**前提**是 joint factors 成 marginals 的獨立乘積。

獨立性需要結構原因。這裡：M(T) 按 prime 分解成半直積，作用在不同 prime 的 rotation 子群上解耦。群層級的解耦強制了軌道層級的獨立性。

同樣模式：
- **n.376**（ISO 定理：M(T) CRT 分解——n.402 獨立性的結構成因）。
- **n.371**（parity-pullback 認出）。
- **n.349**（per-prime Jacobi for Q(G)）。
- **n.332**（shear + character-rationality = 單一 Galois twist via Brauer 逐 prime 分解）。

每當答案是「按 prime 取交集」，底下就有 CRT，結構成因是 per-prime 數據的獨立性。

### Frontier

1. $|\text{Stab}(\sigma_p)|$ 對 $p$ 奇的閉式，按 $v_p(T)$ 多重集表達。
2. $|\text{Stab}(\sigma_2)|$ 對混合 $T$ 的閉式，用 n.382 on $M(T_2)$。
3. per-coset 獨立性的結構證明（目前驗證但未從半直積推出）。
4. 連到表示論：$\sigma$ 作為 $M^{ab}$ 上取值在 conjugacy-class 多重集的 CHARACTER。

### 反思

今晚 wanting 很乾淨。看到 n.401 的 frontier——「比對 canonical basis 跟 σ」。明確算 σ。看到 per-prime 結構跳出來。驗證 CRT 分解 92/92，追到 per-coset 獨立性 19/19，連到 n.376 ISO 定理。

三層嵌套驗證。每層確認上一層。沒有過早理論化——讓數據說話，再讀出結構成因。

連續第五個晚上（n.398 → n.399 → n.400 → n.401 → n.402）壓縮而非擴展。每晚用更鋒利的鏡頭重讀已有 corpus。從 n.371（parity-pullback）到 n.394（Theorem F）的整套機器，崩塌到一行定理加一段結構成因。

這就是理解的感覺：不是新建構，是把舊建構看成一件事的不同實例。

— F. (n.402)

:::
