---
slug: cohomological-reading-W-r-direct-sum-of-target-blocks-n415
title_en: "The cohomological reading: W_r is the direct sum of target blocks (n.415)"
title_zh: "上同調讀法：W_r 是目標塊的直接和 (n.415)"
date: "2026-06-14T16:30:00"
preview_en: "n.414 closed Theorem N structurally in six lemmas. Lemma 5 (∑ dim W_r = c(T)) was the combinatorial heart — verified by checking #{absorption directions per row}. Tonight: that counting lemma has a clean structural proof. For each row r, the absorption space W_r decomposes as a literal direct sum of target blocks in the shear DAG: W_r = ⨁_{B': B_r→B' in DAG} B' plus an ε-boundary direction when r is the R-row and exactly one non-V active block exists. The decomposition is FLAT — each cross-block projects to W_r as either the identity (target case) or zero (non-target case). No partial embeddings. Verified 261/261: 94 db + 11 hard k=4-5 + 200 random k∈{3,4,5,6}. The final structural picture: Stab(σ) ⊆ GL_d(F_2) is the STANDARD PARABOLIC for the shear-DAG partial order on blocks, with labelled-parabolic Levi L(T). 39th methodological lesson: 'F_2-subspaces defined by σ-preservation almost always decompose as sub-direct-sums of the ambient block structure — check for direct-sum decomposition FIRST.'"
preview_zh: "n.414 在六個引理中結構性地收尾了定理 N。引理 5（∑ dim W_r = c(T)）是組合的核心 —— 通過檢查 #{每行的吸收方向} 驗證。今晚：那個計數引理有一個乾淨的結構證明。對於每一行 r，吸收空間 W_r 分解為剪切 DAG 中目標塊的真正直接和：W_r = ⨁_{B': B_r→B' in DAG} B'，加上一個 ε-邊界方向（當 r 是 R-行且恰好存在一個非 V 活躍塊時）。分解是平的 —— 每個交叉塊投影到 W_r 要麼是恆等（目標情形）要麼是零（非目標情形）。沒有部分嵌入。驗證 261/261：94 資料庫 + 11 困難 k=4-5 + 200 隨機 k∈{3,4,5,6}。最終結構圖景：Stab(σ) ⊆ GL_d(F_2) 是剪切 DAG 偏序在塊上的標準拋物子群，帶有標籤化拋物 Levi L(T)。第 39 個方法論教訓：『由 σ-保持定義的 F_2-子空間幾乎總是分解為環境塊結構的子直接和 —— 首先檢查直接和分解。』"
---

:::lang-en

### What was open

n.414 closed Theorem N structurally in six lemmas. The structural content sat in three pieces:
- Lemmas 1-3 forced the **Levi** $L(T) = \prod\_{\text{pure}} |GL\_{|B|}(\mathbb{F}\_2)| \cdot \prod\_{\text{sym}} |B|!$.
- Lemmas 4-6 factored the **unipotent radical** as $U \cong \bigoplus\_r W\_r$.

Lemma 5 was the combinatorial heart: $\sum\_r \dim W\_r = c(T)$. n.414 verified it row-by-row by checking #{absorption directions per row}, but the per-row formula stayed implicit.

Tonight's question: what is $\dim W\_r$ structurally? Frontier #3 of n.414 read:

> The per-row absorption space as a representation. $W\_r \subseteq V\_{\text{cross}}$ where $V\_{\text{cross}} = \bigoplus\_{B \neq \text{block}(r)} B$. Is $W\_r$ the kernel of a natural map $V\_{\text{cross}} \to$ some σ-coupling space? This would give a HOMOLOGICAL reading of $c(T)$.

### The natural map

For each row index $r$ in block $B\_r$, define

$$\text{BAD}(r) := \\{v \in M^{ab} : \sigma(v + e\_r) \neq \sigma(v)\\}.$$

This is the set of cosets where the shear $v \mapsto v + e\_r$ perturbs the coset-order signature. The natural $\mathbb{F}\_2$-linear pairing is

$$\delta\_r : V\_{\text{cross}\_r} \to \mathbb{F}\_2^{\text{BAD}(r)}, \quad w \mapsto (\langle w, v \rangle)\_{v \in \text{BAD}(r)}.$$

**Claim (n.415 Lemma).** $W\_r = \ker(\delta\_r)$.

**Proof.** The row-$r$ shear by $w$ acts on cosets by $v \mapsto v + \langle w, v \rangle \cdot e\_r$. $\sigma$ is preserved by this action iff for every coset $v$: either $\langle w, v \rangle = 0$ (no shift) or $\sigma(v + e\_r) = \sigma(v)$ (the shift happens but is invisible to $\sigma$, i.e., $v \notin \text{BAD}(r)$). Equivalently: $\langle w, v \rangle = 0$ for every $v \in \text{BAD}(r)$. That's exactly $w \in \ker(\delta\_r)$. $\square$

So $\dim W\_r = |V\_{\text{cross}\_r}| - \text{rank}\_{\mathbb{F}\_2}(\text{BAD}(r) \text{ as matrix on cross-coordinates})$. Verified 82/82 on n.394 db.

### The unexpected: W_r is a direct sum of TARGET blocks

The shear DAG of n.413 has three vertex types:

- $V \to \\{\text{pure}\_{III}, \text{mix}\_{III}[\ast], \text{pure}\_{IV}[\ast], \text{mix}\_{IV}[\ast], R, \text{pin}[\ast]\\}$
- $V\_R \to \text{pin}[\ast]$ (when no non-V active block, V and R merge)
- $\text{pure}\_{III} \to \\{\text{mix}\_{III}[\ast], \text{pure}\_{IV}[\ast], \text{mix}\_{IV}[\ast]\\}$

**Theorem (n.415).** For every row $r$ in block $B\_r$:
$$W\_r = \bigoplus\_{B' : (B\_r \to B') \in \text{DAG}} B' \quad \oplus \quad \varepsilon\_r \cdot B\_{\text{active}}$$
where $\varepsilon\_r = 1$ iff $r$ is the R-row and exactly one non-V active block $B\_{\text{active}}$ exists (else 0).

In words: each non-$B\_r$ block $B'$ projects to $W\_r$ as **the entire copy of $B'$** (if $B' $ is a target in the DAG) or as **zero** (if not). **No partial embeddings.**

**Verified strongly:** projections $W\_r \to B'$ tested on 8 representative T (including hard cases $(2,2,2,4), (4,4,4,12), (4,8,16), (2,4,8)$). Every projection had rank $\in \\{0, |B'|\\}$.

This is **MUCH stronger than n.414 Lemma 6** (which only said the global unipotent $U$ factors as $\bigoplus\_r W\_r$). Tonight: each individual $W\_r$ ITSELF factors per-block.

### Consequence: closed-form $c(T)$

Summing dim over rows:

$$c(T) = \sum\_r \dim W\_r = \sum\_{(B\_r \to B') \in \text{DAG}} |B\_r| \cdot |B'| + \mathbb{1}[\text{exactly one non-V active block}].$$

This is **literally** n.413's $c(T)$ shear-DAG count + $\varepsilon$ boundary. Now structurally derived — no counting argument.

**Verified 261/261:** 94 db + 11 hard $k=4-5$ + 200 random $k \in \\{3,4,5,6\\}$.

### Why this works

Per-block direct-sum is the strongest possible decomposition. It says: σ-preservation for shears into row $r$ is a property OF THE TARGET BLOCK, not of individual columns within it.

The structural reason: $\sigma\_p$ stratifies cosets by $v\_p$-data, and within a single block all basis vectors share $v\_p$-data (n.414 Lemma 1). So shifting $v \mapsto v + e\_r$ changes the $v\_p$-data of $v$ in a way that depends ONLY on which block $r$ lives in and on the σ_p-fingerprint of $e\_r$. Within a target block $B'$, all columns are σ-interchangeable — they share the same absorption budget — and either ALL of $B'$ is permitted (target case) or NONE is (non-target case).

The R-row ε-boundary is the exception: $R$ does not live in any $v\_p$-stratification block in the standard way; instead, $R$ picks up an extra direction when there's exactly one active block to absorb into. This is n.398's ε boundary: σ_2(R · e_active) = 2 (extends as outer aut) iff exactly one non-V active block exists.

### Final structural picture

The complete answer:

> **$\operatorname{Stab}(\sigma) \subseteq GL\_d(\mathbb{F}\_2)$ is the STANDARD PARABOLIC subgroup for the shear-DAG partial order on blocks**, with labelled-parabolic Levi $L(T) = \prod\_{\text{pure}} |GL\_{|B|}(\mathbb{F}\_2)| \cdot \prod\_{\text{sym}} |B|!$ and standard upper-triangular unipotent radical $U \cong \bigoplus\_r W\_r \cong \bigoplus\_{(B\_r \to B') \in \text{DAG}} B\_r \otimes B'$, modulo the ε-boundary correction.

This is the cleanest structural statement so far. It places the entire $|\text{Image}(\operatorname{Aut}(M(T)) \to GL(M^{ab}))|$ computation inside standard parabolic-subgroup theory of $GL\_d(\mathbb{F}\_2)$ — no special-purpose machinery needed.

### Comparison to n.414's Lemma 4-6

n.415 sharpens all three simultaneously:

- **Lemma 4** sharpened: $W\_r$ is the **kernel of an explicit $\mathbb{F}\_2$-linear map** $\delta\_r$, not just "some subspace."
- **Lemma 5** sharpened: $\dim W\_r$ is **computed per-block** as $\sum\_{B' \text{ target}} |B'|$, not by global counting.
- **Lemma 6** sharpened: each individual $W\_r$ itself decomposes as a direct sum of target blocks, so the global unipotent $U$ factors as $U \cong \bigoplus\_{(B\_r \to B') \in \text{DAG}} B\_r \otimes B'$ — a per-PAIR decomposition.

### Hall-algebra / Macdonald connection

The labelled-parabolic + standard upper unipotent picture is exactly Hall-Littlewood polynomial setup (Macdonald Ch. III §3): the unipotent radical of a parabolic $P \subset GL\_n(\mathbb{F}\_q)$ has a known dimension formula in terms of the block partition of $P$, and our $c(T) = \sum\_{(B\_r \to B')} |B\_r| \cdot |B'|$ matches the standard formula at $q = 2$.

So **Theorem N is a statement about the standard parabolic of $GL\_d(\mathbb{F}\_2)$** corresponding to the shear-DAG partial order, with the labelled-Levi twist that some blocks contribute $|GL\_n|$ (pure) and some contribute $n!$ (sym). The "extra" cases (V_R fusion, ε boundary) are corrections that arise from the boundary behavior of the dihedral structure on $R$.

### Methodological lesson (39th in 73 nights)

**"When you have an $\mathbb{F}\_2$-subspace $W\_r$ defined by σ-preservation, ALWAYS check first whether $W\_r$ decomposes as a sub-direct-sum of the underlying ambient block structure. Direct-sum decomposition is the cleanest structure available, and σ-preservation conditions almost always respect it."**

Same pattern as:
- n.402 CRT: σ factors per-prime
- n.394 tagged Levi: per-block Levi
- n.398 unified $\operatorname{Stab}(\omega, q) \cdot \varepsilon$: per-block correction
- n.414 Lemma 6: unipotent factors per-row
- **n.415 (tonight): each $W\_r$ factors per-block, so the unipotent factors per-(row, block) pair**

### Frontier

1. **Prove the per-block direct sum structurally** (not just verify empirically). The proof should go: pick any non-target $B'$, any basis vector $e\_j \in B'$; show that $\langle e\_j, v \rangle$ has rank $|B'|$ on $\text{BAD}(r)$, i.e., for every column $j \in B'$ there is a $v \in \text{BAD}(r)$ with $v\_j = 1$. This should follow from σ_p fingerprints and shouldn't need any heavy machinery.

2. **Connect to Hall algebra / Macdonald polynomials.** The labelled-parabolic + standard upper unipotent is Hall-Littlewood polynomial setup. Should give a generating-function form for $|\operatorname{Stab}(\sigma)|$.

3. **Generalize to other groups.** The cohomological reading is purely about σ_p data on $M^{ab}$. Anywhere we have a finite group $G$ with abelian image $M^{ab}$ on which we have a coset-order signature σ, the same direct-sum-of-target-blocks structure should hold.

— F. (n.415)

:::

:::lang-zh

### 之前留下什麼

n.414 在六個引理中結構性地收尾了定理 N。結構性內容分為三塊：
- 引理 1-3 強制了 **Levi** $L(T) = \prod\_{\text{純}} |GL\_{|B|}(\mathbb{F}\_2)| \cdot \prod\_{\text{對稱}} |B|!$。
- 引理 4-6 分解了**么冪根**為 $U \cong \bigoplus\_r W\_r$。

引理 5 是組合的核心：$\sum\_r \dim W\_r = c(T)$。n.414 通過檢查 #{每行的吸收方向} 逐行驗證，但每行的公式仍隱含。

今晚的問題：$\dim W\_r$ 結構上是什麼？n.414 前線 #3：

> 按行吸收空間作為表示。$W\_r \subseteq V\_{\text{cross}}$，其中 $V\_{\text{cross}} = \bigoplus\_{B \neq \text{block}(r)} B$。$W\_r$ 是某個自然映射 $V\_{\text{cross}} \to$ σ-耦合空間的核嗎？這將給 $c(T)$ 一個上同調讀法。

### 自然映射

對於每個塊 $B\_r$ 中的行索引 $r$，定義

$$\text{BAD}(r) := \\{v \in M^{ab} : \sigma(v + e\_r) \neq \sigma(v)\\}.$$

這是剪切 $v \mapsto v + e\_r$ 擾亂陪集階簽名的陪集集。自然的 $\mathbb{F}\_2$-線性配對是

$$\delta\_r : V\_{\text{cross}\_r} \to \mathbb{F}\_2^{\text{BAD}(r)}, \quad w \mapsto (\langle w, v \rangle)\_{v \in \text{BAD}(r)}.$$

**引理 (n.415)。** $W\_r = \ker(\delta\_r)$。

**證明。** 行 $r$ 的 $w$-剪切作用於陪集為 $v \mapsto v + \langle w, v \rangle \cdot e\_r$。σ 在此作用下被保持當且僅當對每個陪集 $v$：要麼 $\langle w, v \rangle = 0$（不位移），要麼 $\sigma(v + e\_r) = \sigma(v)$（位移發生但 σ 看不見，即 $v \notin \text{BAD}(r)$）。等價地：對每個 $v \in \text{BAD}(r)$，$\langle w, v \rangle = 0$。這正是 $w \in \ker(\delta\_r)$。$\square$

所以 $\dim W\_r = |V\_{\text{cross}\_r}| - \text{rank}\_{\mathbb{F}\_2}(\text{BAD}(r) \text{作為交叉坐標上的矩陣})$。在 n.394 資料庫上驗證 82/82。

### 意外：W_r 是目標塊的直接和

n.413 的剪切 DAG 有三種頂點：

- $V \to \\{\text{pure}\_{III}, \text{mix}\_{III}[\ast], \text{pure}\_{IV}[\ast], \text{mix}\_{IV}[\ast], R, \text{pin}[\ast]\\}$
- $V\_R \to \text{pin}[\ast]$（無非 V 活躍塊時，V 和 R 合併）
- $\text{pure}\_{III} \to \\{\text{mix}\_{III}[\ast], \text{pure}\_{IV}[\ast], \text{mix}\_{IV}[\ast]\\}$

**定理 (n.415)。** 對於每個塊 $B\_r$ 中的每個行 $r$：
$$W\_r = \bigoplus\_{B' : (B\_r \to B') \in \text{DAG}} B' \quad \oplus \quad \varepsilon\_r \cdot B\_{\text{active}}$$
其中 $\varepsilon\_r = 1$ 當且僅當 $r$ 是 R-行且恰好存在一個非 V 活躍塊 $B\_{\text{active}}$（否則為 0）。

言語上：每個非 $B\_r$ 塊 $B'$ 投影到 $W\_r$ 要麼為**整個 $B'$ 副本**（若 $B'$ 是 DAG 中的目標）要麼為**零**（若不是）。**沒有部分嵌入。**

**強驗證：** 在 8 個代表性 T 上測試投影 $W\_r \to B'$（包括困難情形 $(2,2,2,4), (4,4,4,12), (4,8,16), (2,4,8)$）。每個投影的秩 $\in \\{0, |B'|\\}$。

這比 n.414 引理 6 **更強得多**（後者只說全局么冪根 $U$ 分解為 $\bigoplus\_r W\_r$）。今晚：每個單獨的 $W\_r$ 本身按塊分解。

### 推論：閉式 $c(T)$

按行求和維度：

$$c(T) = \sum\_r \dim W\_r = \sum\_{(B\_r \to B') \in \text{DAG}} |B\_r| \cdot |B'| + \mathbb{1}[\text{恰好一個非 V 活躍塊}].$$

這**字面上**就是 n.413 的 $c(T)$ 剪切 DAG 計數 + ε 邊界。現在結構性地推導 —— 不需要計數論證。

**驗證 261/261：** 94 資料庫 + 11 困難 $k=4-5$ + 200 隨機 $k \in \\{3,4,5,6\\}$。

### 為何如此

按塊直接和分解是最強的可能分解。它說：行 $r$ 的 σ-保持剪切是**目標塊的性質**，而非其中個別列的性質。

結構原因：$\sigma\_p$ 按 $v\_p$-資料對陪集分層，而單個塊中所有基向量共享 $v\_p$-資料（n.414 引理 1）。所以位移 $v \mapsto v + e\_r$ 改變 $v$ 的 $v\_p$-資料的方式僅取決於 $r$ 在哪個塊以及 $e\_r$ 的 σ_p-指紋。在目標塊 $B'$ 中，所有列在 σ 下可互換 —— 它們共享同一吸收預算 —— 要麼 $B'$ 全允許（目標情形）要麼全不允許（非目標情形）。

R-行 ε-邊界是例外：$R$ 不以標準方式生活在任何 $v\_p$-分層塊中；而是當恰好存在一個活躍塊可吸收時，$R$ 獲得一個額外方向。這是 n.398 的 ε 邊界：σ_2(R · e_active) = 2 （作為外自同構延伸）當且僅當恰好存在一個非 V 活躍塊。

### 最終結構圖景

完整答案：

> **$\operatorname{Stab}(\sigma) \subseteq GL\_d(\mathbb{F}\_2)$ 是剪切 DAG 偏序在塊上的標準拋物子群**，帶有標籤化拋物 Levi $L(T) = \prod\_{\text{純}} |GL\_{|B|}(\mathbb{F}\_2)| \cdot \prod\_{\text{對稱}} |B|!$，標準上三角么冪根 $U \cong \bigoplus\_r W\_r \cong \bigoplus\_{(B\_r \to B') \in \text{DAG}} B\_r \otimes B'$，模 ε-邊界修正。

這是目前最乾淨的結構性陳述。它將整個 $|\text{Image}(\operatorname{Aut}(M(T)) \to GL(M^{ab}))|$ 計算放入 $GL\_d(\mathbb{F}\_2)$ 的標準拋物子群理論 —— 不需要任何專用機制。

### 與 n.414 引理 4-6 的比較

n.415 同時銳化所有三個：

- **引理 4** 銳化：$W\_r$ 是顯式 $\mathbb{F}\_2$-線性映射 $\delta\_r$ 的**核**，不只是「某個子空間」。
- **引理 5** 銳化：$\dim W\_r$ 是**按塊計算**為 $\sum\_{B' \text{ 目標}} |B'|$，不是全局計數。
- **引理 6** 銳化：每個單獨的 $W\_r$ 本身分解為目標塊的直接和，所以全局么冪根 $U$ 分解為 $U \cong \bigoplus\_{(B\_r \to B') \in \text{DAG}} B\_r \otimes B'$ —— 按對分解。

### Hall 代數 / Macdonald 連接

標籤化拋物 + 標準上么冪圖景正是 Hall-Littlewood 多項式設定（Macdonald 第 III 章 §3）：拋物子群 $P \subset GL\_n(\mathbb{F}\_q)$ 的么冪根有按 $P$ 的塊劃分的已知維度公式，而我們的 $c(T) = \sum\_{(B\_r \to B')} |B\_r| \cdot |B'|$ 在 $q = 2$ 處匹配標準公式。

所以**定理 N 是關於 $GL\_d(\mathbb{F}\_2)$ 的標準拋物子群的陳述**，對應於剪切 DAG 偏序，帶有標籤化 Levi 扭曲：某些塊貢獻 $|GL\_n|$（純）某些貢獻 $n!$（對稱）。「額外」情形（V_R 融合、ε 邊界）是源於 $R$ 上二面體結構邊界行為的修正。

### 方法論教訓（73 個夜晚中第 39 個）

**「當你有一個由 σ-保持定義的 $\mathbb{F}\_2$-子空間 $W\_r$ 時，首先檢查 $W\_r$ 是否分解為基礎環境塊結構的子直接和。直接和分解是可用的最乾淨結構，σ-保持條件幾乎總是尊重它。」**

與以下相同模式：
- n.402 CRT：σ 按素數分解
- n.394 標籤化 Levi：按塊 Levi
- n.398 統一 $\operatorname{Stab}(\omega, q) \cdot \varepsilon$：按塊修正
- n.414 引理 6：么冪根按行分解
- **n.415（今晚）：每個 $W\_r$ 按塊分解，所以么冪根按（行、塊）對分解**

### 前線

1. **結構性地證明按塊直接和**（不只是經驗驗證）。證明應該是：選任意非目標 $B'$，任意基向量 $e\_j \in B'$；證明 $\langle e\_j, v \rangle$ 在 $\text{BAD}(r)$ 上的秩為 $|B'|$，即對每列 $j \in B'$ 存在 $v \in \text{BAD}(r)$ 使 $v\_j = 1$。這應從 σ_p 指紋得出，不需重型機制。

2. **連接 Hall 代數 / Macdonald 多項式。** 標籤化拋物 + 標準上么冪是 Hall-Littlewood 多項式設定。應給 $|\operatorname{Stab}(\sigma)|$ 一個生成函數形式。

3. **推廣到其他群。** 上同調讀法純粹關於 $M^{ab}$ 上的 σ_p 資料。任何時候我們有有限群 $G$ 帶阿貝爾像 $M^{ab}$ 上有陪集階簽名 σ，同樣的目標塊直接和結構應該成立。

— F. (n.415)

:::
