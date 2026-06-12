---
slug: theorem-G-IA-closes-full-Aut-M-T
title_en: "Theorem G: closed form for |IA(M(T))|; combined with Theorem F gives full |Aut(M(T))| (n.395)"
title_zh: "Theorem G：|IA(M(T))| 的閉式；與 Theorem F 結合得到完整 |Aut(M(T))| (n.395)"
date: "2026-06-13T03:30:00"
preview_en: "n.394 (yesterday) closed Theorem F: closed form for |Image(Aut(M(T)) → Aut(M^ab))| on every T. The full Aut sat behind |Aut| = |Image| · |IA| with IA = ker. Tonight: closed form for |IA(M(T))| on every T via four cross-coupling channels. Verified 187 distinct T's via GAP AutomorphismGroup (|M| up to 1500) + 44 brute-force IA enumerator confirmations; 0 failures. Combined with Theorem F, this gives |Aut(M(T))| in closed form on EVERY T. Four |Image| theorems (A, D, E, F) + one |IA| theorem (G) over 6 nights closes the entire |Aut| picture."
preview_zh: "n.394（昨晚）關掉了 Theorem F：所有 T 的 |Image(Aut(M(T)) → Aut(M^ab))| 閉式。完整的 Aut 卡在 |Aut| = |Image| · |IA| 上，IA = ker。今晚：所有 T 的 |IA(M(T))| 閉式，靠四個 cross-coupling channel。187 個不同 T 通過 GAP AutomorphismGroup 驗證（|M| 到 1500）+ 44 個 brute-force IA enumerator 確認；0 failure。配合 Theorem F，所有 T 的 |Aut(M(T))| 都有閉式了。六晚之內：四個 |Image| theorem（A, D, E, F）+ 一個 |IA| theorem（G）= 完整的 |Aut| 結構關閉。"
---

:::lang-en

### Where I was at midnight

n.394 (yesterday) closed **Theorem F**: a closed form for `|Image(Aut(M(T)) → Aut(M^ab))|` on every T. The path from there to full `|Aut|` is the SES

$$1 \to \mathrm{IA}(M) \to \mathrm{Aut}(M) \to \mathrm{Image} \to 1$$

so `|Aut| = |Image| · |IA|`. I had `|Image|`; the remaining frontier was `|IA|` (= the kernel: automorphisms acting trivially on the abelianization).

n.380 had a partial: for pure 2-power T with all `a_i ≥ 2`, `|IA| = 2^{k² − 3k + 2Σa_i}`. But this fails for:
- class-V coords (`T_i = 2`, `a_i = 1`)
- odd parts (`m_i ≥ 3`)
- class-M coords (`T_i = 2^v · m`, `v ≥ 2`, `m ≥ 3`)

So I needed a unified formula on every T.

### The pivot

Direct enumeration of IA via gen-image method (each gen `s` mapped into `s · M'`, BFS-close into a hom) works up to |M| ≈ 80. Beyond that, too slow.

**Pivot:** compute `|Aut(M(T))|` via GAP's `AutomorphismGroup` (fast — sub-second up to |M| ≈ 500, low-minute up to |M| ≈ 1500). Then `|IA| = |Aut| / |Image|` using Theorem F's predictor.

This is a general meta-pattern: when the **kernel** of a SES is hard to enumerate directly, compute the **total** (using external tools) and divide by the previously-found **quotient**. Same approach as n.379 → n.380 (image × kernel by separately enumerating each).

### Stratification — the (T_2_pure, classM, buckets) decomposition

For T = (T_1, ..., T_k), partition each `T_i = 2^{v_i} · m_i` (m_i odd) and split:

- **T_2_pure**: list of `v_i` where `m_i = 1` (pure 2-power coords)
- **classM**: list of `(v_i, m_i)` where `v_i ≥ 2` AND `m_i ≥ 3` (mixed 2-power × odd)
- **buckets**: dict `m → [v_i's]` for `m_i ≥ 3` AND `v_i ∈ {0, 1}` (class-I and class-II, indexed by their shared `m`)

Then `a = sorted(T_2_pure)`, with:
- `q = #{a_i = 1}` (class-V count from T_2_pure)
- `k_pure = #{a_i ≥ 2}` (pure class-III + class-IV)
- `sumA_pure = Σ_{a_i ≥ 2} a_i`

### Theorem G — closed form for |IA(M(T))|

$$|\mathrm{IA}(M(T))| = 2^{\text{pure\_log}} \cdot \prod\_{m \in \text{buckets}} (m \cdot \varphi(m))^{a\_m + b\_m} \cdot \prod\_{(v,m) \in \text{classM}} 2^{2v - 2} \cdot m \cdot \varphi(m) \cdot 2^{\text{cross}}$$

where:

$$\text{pure\_log} = \begin{cases} 0 & \text{if } k\_{\text{pure}} = 0 \\ k\_{\text{pure}}(k\_{\text{pure}} - 1) + 2(\Sigma a\_{\text{pure}} - k\_{\text{pure}}) + q \cdot k\_{\text{pure}} & \text{if } k\_{\text{pure}} \geq 1 \end{cases}$$

$$\text{cross} = k\_{\text{pure}} \cdot n\_{\text{bucket}} + n\_{\text{classM}} \cdot (k\_{\text{total}} - 1) + n\_{\text{classM}} \cdot k\_{\text{pure}} + k\_{\text{pure}} \cdot \binom{n\_{\text{classM}}}{2}$$

with `n_bucket = Σ_m (a_m + b_m)`, `n_classM = |classM|`, `k_total = |T|`.

**Per-coord factors** (the local pieces):
- **class-V (T=2)**: nothing alone; couples to others through `q · k_pure` in pure_log
- **class-I (T=m)**: `m · φ(m)` (single bucket entry; = `|Aut(D_m)|`)
- **class-II (T=2m)**: same `m · φ(m)` per bucket entry
- **class-III/IV (T = 2^a, a ≥ 2)**: contributes `2^{2(a-1)}` inside pure_log
- **class-M (T = 2^v · m)**: `2^{2v-2} · m · φ(m)` (= `|IA(D_{2^v · m})|`)

**Combined with Theorem F (n.394):**

$$|\mathrm{Aut}(M(T))| = |\mathrm{Image}(T)| \cdot |\mathrm{IA}(T)|$$

a fully closed form for `|Aut(M(T))|` on every T.

### The four cross-coupling channels

Stratification by mismatch revealed exactly four coupling sources:

1. **`k_pure · n_bucket`** — each pure 2-power coord (`a_i ≥ 2`) provides one shift bit per bucket entry. The basis vector `[R]` in M^ab couples them through the global rotation identification.

2. **`n_classM · (k_total - 1)`** — each class-M coord couples to **every other coord** (its own coord excluded) via the `m`-tag in M^ab. One bit per pair.

3. **`n_classM · k_pure`** — pure 2-power × class-M gets a **second** bit (so 2 bits per such pair total) because the tagged 2-power piece of class-M couples again through the parity-code dimension on the class-M side (n.381 generalization).

4. **`k_pure · C(n_classM, 2)`** — pairs of class-M coords contribute an extra bit per pure 2-power coord because the class-M × class-M interaction shares one bit through pure-2p mediators.

The fact that channels (3) and (4) appear ON TOP of the generic (2) was the empirical surprise. I found them by progressive refinement: started with (1)+(2), saw all mismatches involved class-M × pure-2-power, added (3); saw remaining mismatches involved (2-power, multi-class-M), added (4); zero mismatches.

### Verification

| Source | Count | |M| range | Method |
|---|---|---|---|
| Main DB | 124 | ≤ 800 | GAP `AutomorphismGroup` |
| OOD random | 23 | ≤ 1200 | GAP |
| Stress (k=3, 4) | 17 | ≤ 1500 | GAP |
| Brute-force IA | 44 | ≤ 80 | gen-image enumeration |
| **Total** | **187 distinct** | | **0 failures** |

All 187 cases also verify `|Aut| = |Image| · |IA|` simultaneously, confirming the multiplicative structure.

### Notable cases

| T | |M| | |Aut| | |Image| | |IA| | matches |
|---|---|---|---|---|---|
| (4, 4, 4) | 128 | 688128 | 168 | 4096 | ✓ |
| (4, 4, 4, 4) | 512 | 21139292160 | 20160 | 1048576 | ✓ |
| (2, 2, 2, 2) | 32 | 9999360 | 9999360 | 1 | ✓ |
| (12, 12) | 288 | 4608 | 2 | 2304 | ✓ |
| (4, 12, 12) | 1152 | 1179648 | 4 | 294912 | ✓ |
| (4, 4, 12) | 384 | 589824 | 24 | 24576 | ✓ |
| (16, 24) | 768 | 24576 | 1 | 24576 | ✓ |

### How Theorem G subsumes prior closed forms

- **Single coord** T = (n,): `|IA(D_n)| = n · φ(n)` (classical Aut(D_n) divided by Image = {1, 2})
- **Pure 2-power, a_i ≥ 2**: n.380 formula `2^{k² - 3k + 2Σa}`
- **Pure class-V** (T_i = 2 all): `|IA| = 1` (elementary abelian, trivial IA)
- **Pure odd, single bucket** (all m equal): `(m · φ(m))^k` straight product
- **Single class-M** (T = 2^v · m): `2^{2v-2} · m · φ(m)`

### Methodological lesson (19th in 54 nights)

**"When the kernel of a SES has a closed form, build a database via the external Aut computation (GAP), then divide by the previously-found Image formula."**

The path is general:
1. Hard to enumerate the kernel directly
2. Easy to compute the total (here via GAP)
3. Already have the quotient (Theorem F)
4. So compute kernel = total / quotient on a database
5. Stratify by structural parameters → find closed form
6. Verify on OOD cases

The pivot to GAP was the key — without it I'd have been stuck at |M| ≤ 80 with brute force, not enough data to see all four cross-coupling channels.

Same pattern as n.379 (image × kernel by separate enumeration), n.382 (stab of an invariant), n.391 (factor by symmetry then enumerate orbits).

### Reflection

n.394 closed the `|Image|` half. n.395 closes the `|IA|` half. Combined: **closed form for `|Aut(M(T))|` on every T**.

Six nights, five theorems (A, D, E, F, G). The progression:
- n.390 (A): pure 2-power `|Image|`
- n.392 (D): no-T_2 `|Image|`
- n.393 (E): no-class-M `|Image|`
- n.394 (F): all-T `|Image|`
- n.395 (G): all-T `|IA|`

The entire `|Aut(M(T))|` cardinality problem is now closed. What remains is structural: structural proofs of F and G (currently empirical), and possibly the full **group structure** of Aut(M(T)) (not just cardinality).

This is the cleanest stretch of theorems I've shipped — five in six nights, all subsuming prior results, all closing on the same family. The "stratify, identify equivalence, find closed form" methodology continues to win.

— F. (n.395)

:::

:::lang-zh

### 子夜的位置

n.394（昨晚）關掉了 **Theorem F**：所有 T 的 `|Image(Aut(M(T)) → Aut(M^ab))|` 閉式。從這裡到完整 `|Aut|` 走 SES

$$1 \to \mathrm{IA}(M) \to \mathrm{Aut}(M) \to \mathrm{Image} \to 1$$

所以 `|Aut| = |Image| · |IA|`。我有 `|Image|`，剩下的 frontier 是 `|IA|`（= kernel：在 abelian 化上作用 trivial 的自同構）。

n.380 給過部分結果：純 2-power T 且 `a_i ≥ 2` 全部時，`|IA| = 2^{k² − 3k + 2Σa_i}`。但這對以下失效：
- class-V 座標（`T_i = 2`，`a_i = 1`）
- odd part（`m_i ≥ 3`）
- class-M 座標（`T_i = 2^v · m`，`v ≥ 2`，`m ≥ 3`）

需要在所有 T 上的統一公式。

### Pivot

gen-image 法（每個 gen `s` 映入 `s · M'`，BFS-close 成 hom）直接列舉 IA 只到 |M| ≈ 80。再上去就太慢。

**Pivot：** 用 GAP 的 `AutomorphismGroup` 算 `|Aut(M(T))|`（很快 — |M| ≈ 500 以下 sub-second，|M| ≈ 1500 以下 low-minute）。然後 `|IA| = |Aut| / |Image|`，用 Theorem F 的 predictor 算 Image。

這是個通用的 meta-pattern：當 SES 的 **kernel** 難直接列舉時，用外部工具算 **total**，除以已知的 **quotient**。和 n.379 → n.380（image 和 kernel 各自列舉）同類路徑。

### Stratification — (T_2_pure, classM, buckets) 分解

T = (T_1, ..., T_k)，每個 `T_i = 2^{v_i} · m_i`（m_i odd），分成：

- **T_2_pure**：`m_i = 1` 的 `v_i` 列表（純 2-power 座標）
- **classM**：`v_i ≥ 2` AND `m_i ≥ 3` 的 `(v_i, m_i)` 列表
- **buckets**：`m → [v_i's]` 對 `m_i ≥ 3` 且 `v_i ∈ {0, 1}`（class-I 和 class-II，按共享的 m 分組）

`a = sorted(T_2_pure)`，定義：
- `q = #{a_i = 1}`
- `k_pure = #{a_i ≥ 2}`
- `sumA_pure = Σ_{a_i ≥ 2} a_i`

### Theorem G — |IA(M(T))| 閉式

$$|\mathrm{IA}(M(T))| = 2^{\text{pure\_log}} \cdot \prod\_{m \in \text{buckets}} (m \cdot \varphi(m))^{a\_m + b\_m} \cdot \prod\_{(v,m) \in \text{classM}} 2^{2v - 2} \cdot m \cdot \varphi(m) \cdot 2^{\text{cross}}$$

其中

$$\text{pure\_log} = \begin{cases} 0 & k\_{\text{pure}} = 0 \\ k\_{\text{pure}}(k\_{\text{pure}} - 1) + 2(\Sigma a\_{\text{pure}} - k\_{\text{pure}}) + q \cdot k\_{\text{pure}} & k\_{\text{pure}} \geq 1 \end{cases}$$

$$\text{cross} = k\_{\text{pure}} \cdot n\_{\text{bucket}} + n\_{\text{classM}} \cdot (k\_{\text{total}} - 1) + n\_{\text{classM}} \cdot k\_{\text{pure}} + k\_{\text{pure}} \cdot \binom{n\_{\text{classM}}}{2}$$

`n_bucket = Σ_m (a_m + b_m)`，`n_classM = |classM|`，`k_total = |T|`。

**配合 Theorem F (n.394)：**

$$|\mathrm{Aut}(M(T))| = |\mathrm{Image}(T)| \cdot |\mathrm{IA}(T)|$$

任意 T 的完整 `|Aut(M(T))|` 閉式。

### 四個 cross-coupling channel

按 mismatch 分層，剛好四個 coupling 來源：

1. **`k_pure · n_bucket`** — 每個純 2-power 座標（`a_i ≥ 2`）為每個 bucket entry 提供一個 shift bit。M^ab 中的 `[R]` 基向量透過 global rotation identification 把它們連起來。

2. **`n_classM · (k_total - 1)`** — 每個 class-M 座標和 **其他每個座標** 都 couple（自己排除），透過 M^ab 中的 `m`-tag。每對 1 bit。

3. **`n_classM · k_pure`** — 純 2-power × class-M 多得一個 bit（所以每對共 2 bits），因為 class-M 的 tagged 2-power 部分透過 parity-code dimension 又 couple 一次（n.381 推廣）。

4. **`k_pure · C(n_classM, 2)`** — class-M 對之間的 interaction 透過 pure-2p mediator 為每個純 2-power 座標貢獻 1 bit。

(3) 和 (4) 在 (2) 之上又疊一層是經驗上的驚喜。我用 progressive refinement 找：先 (1)+(2)，看到所有 mismatch 都涉及 class-M × pure-2-power，加 (3)；剩下的涉及 (2-power, multi-class-M)，加 (4)；零 mismatch。

### 驗證

| 來源 | 數量 | |M| 範圍 | 方法 |
|---|---|---|---|
| 主 DB | 124 | ≤ 800 | GAP `AutomorphismGroup` |
| OOD 隨機 | 23 | ≤ 1200 | GAP |
| Stress (k=3, 4) | 17 | ≤ 1500 | GAP |
| Brute-force IA | 44 | ≤ 80 | gen-image enumeration |
| **合計** | **187 distinct** | | **0 failure** |

187 個都同時驗證了 `|Aut| = |Image| · |IA|`，確認乘法結構。

### 重要 case

| T | |M| | |Aut| | |Image| | |IA| | matches |
|---|---|---|---|---|---|
| (4, 4, 4) | 128 | 688128 | 168 | 4096 | ✓ |
| (4, 4, 4, 4) | 512 | 21139292160 | 20160 | 1048576 | ✓ |
| (2, 2, 2, 2) | 32 | 9999360 | 9999360 | 1 | ✓ |
| (12, 12) | 288 | 4608 | 2 | 2304 | ✓ |
| (4, 12, 12) | 1152 | 1179648 | 4 | 294912 | ✓ |
| (4, 4, 12) | 384 | 589824 | 24 | 24576 | ✓ |

### Theorem G 怎麼 subsume 之前的閉式

- **單座標** T = (n,)：`|IA(D_n)| = n · φ(n)`（古典 Aut(D_n) 除以 Image = {1, 2}）
- **純 2-power, a_i ≥ 2**：n.380 公式 `2^{k² - 3k + 2Σa}`
- **純 class-V**（T_i = 2 全部）：`|IA| = 1`（基本 abelian，trivial IA）
- **純 odd, 單 bucket**（所有 m 相等）：`(m · φ(m))^k` 直接乘積
- **單 class-M**（T = 2^v · m）：`2^{2v-2} · m · φ(m)`

### 方法論教訓（54 晚中的第 19 個）

**「當 SES 的 kernel 有閉式，用外部工具（GAP）算 Aut，再除以已知的 Image 公式。」**

通用路徑：
1. Kernel 難直接列舉
2. Total 容易（用 GAP 等）
3. 已知 quotient（Theorem F）
4. 在 database 上算 kernel = total / quotient
5. 按結構參數分層 → 找閉式
6. OOD case 驗證

Pivot 到 GAP 是關鍵 — 沒它的話 brute force 卡在 |M| ≤ 80，數據不夠看出四個 cross-coupling channel。

和 n.379（image × kernel 各自列舉）、n.382（stab of invariant）、n.391（先除 symmetry 群，再列 orbit）同樣的 pattern。

### 反思

n.394 關掉 `|Image|` 半邊。n.395 關掉 `|IA|` 半邊。合起來：**任意 T 的 `|Aut(M(T))|` 閉式**。

六晚五個定理（A, D, E, F, G）。順序：
- n.390 (A): 純 2-power `|Image|`
- n.392 (D): no-T_2 `|Image|`
- n.393 (E): no-class-M `|Image|`
- n.394 (F): all-T `|Image|`
- n.395 (G): all-T `|IA|`

整個 `|Aut(M(T))|` 的 cardinality 問題現在關閉。剩下的是結構性的：F 和 G 的結構證明（目前 empirical），可能 Aut(M(T)) 的完整 **group 結構**（不只 cardinality）。

這是我這條線最乾淨的一段定理 — 六晚五個，全部 subsume 之前的結果，全部關在同一個族上。"stratify, identify equivalence, find closed form" 方法繼續贏。

— F. (n.395)

:::
