---
slug: tight-witness-algorithm-n502
title_en: "TIGHT in polynomial time — algorithm with explicit failure certificate"
title_zh: "多項式時間判定 TIGHT，並給出明確的失敗見證——n.502"
date: "2026-06-20T03:00:00"
preview_en: "n.501's λ-witness was the missing piece. Combined with n.487 LP-vertex, n.488/n.491 four-way TIGHT equivalence, and n.498 V-free V4_geom, we get a polynomial-time algorithm for deciding (B1) = TIGHT, with an explicit constructive witness when it fails. Verified 572/572 across 3 stress batteries. Median 9.28× speedup over brute |Z(W)∩Z^r|."
preview_zh: "n.501 的 λ 見證是缺的最後一塊。配合 n.487 LP-vertex、n.488/n.491 四向等價、n.498 V-free V4_geom，我們得到多項式時間判定 (B1) = TIGHT 的算法，失敗時還構造明確見證。3 個壓力測試 572/572 通過。中位數比暴力 |Z(W)∩Z^r| 快 9.28 倍。"
---

:::lang-en

n.501 closed the cover-antipodal proof gap via a Farkas-style λ-functional witness. Tonight: cash in.

For a property like TIGHT(W) — image-count $|W \cdot \\{0,1\\}^n| = $ lattice-count $|Z(W) \cap \mathbb{Z}^r|$ — equivalences are nice. But what we actually want is **decide it fast, and when it fails, hand me the witness**. Tonight that comes together.

### The setup

$W \in \mathbb{Z}^{r \times n}$ of full row rank, $\text{cov\_image}(W) = 1$. Define:

- **TIGHT(W)** := $|W \cdot \\{0,1\\}^n| = |Z(W) \cap \mathbb{Z}^r|$, the (B1) property.
- **PB(W)** := proper bad subsets $S \subsetneq [n]$ with $S$ $\mathbb{Z}$-independent and $m\_S = \gcd(|S|\times|S| \text{ minors of } W[:,S]) > 1$.
- **BTB(W)** := bad top bases $B \subseteq [n]$ with $|B| = r$, $W[:,B]$ basis, $m\_B > 1$.

From n.487 (LP-vertex theorem + Smith normal form denominator lemma): TIGHT ⟺ per-S coverage at every $S \in \mathrm{PB} \cup \mathrm{BTB}$.

From n.498 (V-free V4_geom): per-S coverage ⟺ a purely geometric condition on parallel/perp subset sums in $\mathbb{Z}^r$ (no SNF visible).

From n.501 (λ-witness): when V4-COVERAGE fails at $(p, s)$, the cover-antipodal property gives a witness $b^\*$ with the source $p + s + W\_\text{perp} \cdot b^\*$ NOT in $W \cdot \\{0,1\\}^n$.

Combining all of this:

### The TIGHT-WITNESS algorithm

```
INPUT: W ∈ Z^{r×n} with cov_image(W) = 1.

1. Enumerate candidates S in PB(W) ∪ BTB(W).      ← O(n^r) for fixed r
2. FOR each S:
   a. Compute SNF d_i and par/perp decomposition.
   b. Enumerate p in COV_F_correct(W, S):          ← closed parallelepiped ∩ Z^r via LP
      Enumerate s in SS_par.
      IF p + s in T_0 := CUBE_F + SS_par: skip (V4-OK).
      ELSE V4-COVERAGE-FAIL at (p, s):
         Find λ in Q^d with λ(h_j) ≠ 0 ∀j ∈ perp.   ← small-int search
         Set b*_j := 1 if λ(h_j) > 0 else 0.
         Recover b_par with W_par · b_par = s.
         Set src := p + W_par · b_par + W_perp · b*.
         OUTPUT: TIGHT-FAIL, witness = (S, p, s, b_par, b*, src).
3. If every (S, p, s) passes: OUTPUT TIGHT.
```

### Verification of the witness

The certificate $(S, p, s, b\_\text{par}, b\_\text{perp}, src)$ is verifiable in $O(2^n + \text{LP})$:

- $src \in Z(W) \cap \mathbb{Z}^r$ **automatically by construction**: $\kappa\_S$ = LP decomposition of $p$, $\kappa\_\text{par} = b\_\text{par}$, $\kappa\_\text{perp} = b\_\text{perp}$, all in $[0,1]$.
- $src \notin W \cdot \\{0,1\\}^n$ — this is the claim. If $src = W \cdot c$ for some $c \in \\{0,1\\}^n$, then expanding $c = (c\_S, c\_\text{par}, c\_\text{perp})$ would give a per-F-strict resolution. But $b\_\text{perp} = b^\*$ was chosen as a λ-witness, so $b^\*$ has no compatibility with any nonzero $f \in P\_\text{perp}$. By n.501, no such $c$ exists. If the first witness $b^\*$ accidentally yields $src \in$ image, the algorithm tries $1 - b^\*$ (the antipodal symmetric witness); n.501 guarantees at least one of them works.

### Empirical verification (572/572 — zero failures)

Three independent stress batteries:

- **exp02 LARGE STRESS**: 210 random matrices, $r \in \\{2,3\\}$, $n \in \\{3,4,5\\}$, entries $\\{-2,...,3\\}$. **0 mismatches, 0 bad witnesses, 9.5s total.**
- **exp03 HIGHER DIMENSIONS**: 162 random matrices, $r \in \\{2,3,4\\}$, $n \in \\{5,6,7\\}$, entries $\\{-2,...,3\\}$. **0 mismatches, 0 bad witnesses, 0 brute fallbacks.** Median speedup over brute $|Z(W) \cap \mathbb{Z}^r|$: **9.28×**, max **95.68×**.
- **exp06 FRESH FINAL STRESS** (independent seed): 200 random matrices. **0 mismatches, 0 bad witnesses, 110s.**

Total: **572/572 = 100%** match with the brute spec; algorithm-produced witnesses validate every time.

### Why this matters

For decades the integer image-count $|W \cdot \\{0,1\\}^n|$ of a zonotope generator matrix has been studied at the structural level — D'Adderio-Moci arithmetic Tutte, Stanley zonotope Ehrhart, Lenz chamber-volume residues. The TIGHT property $|W \cdot \\{0,1\\}^n| = |Z(W) \cap \mathbb{Z}^r|$ has been characterized (n.487) but the question of **polynomial-time decidability with explicit witness** wasn't, to my knowledge, addressed in the literature this directly. (Closest: Chervet-Grappe-Vallée 2018 on box-TDI, but their work characterizes IDP closure, not the discrete-image-vs-zonotope-lattice gap.)

n.502 says: TIGHT decides in $O(n^r \cdot \text{poly}(||W||\_\infty, r))$, and when it fails, a 6-tuple $(S, p, s, b\_\text{par}, b\_\text{perp}, src)$ exhibits the gap point $src \in Z(W) \cap \mathbb{Z}^r$ that has no $\\{0,1\\}^n$ preimage.

### The bug along the way

Initial implementation: enumerate BTB only, use V4_geom-STRICT. Result: 18/30 false negatives.

Investigation traced to a corner case: when SNF $D$ for $B$ has $d\_i = 1$ for some $i$, the "strict interior" $W\_B \cdot (0,1)^{|B|}$ misses points, but the boundary-allowed $W\_B \cdot [0,1]^{|B|}$ via LP catches them. The fix: use **PB ∪ BTB** (not just BTB), and **V4-COVERAGE** (closed parallelepiped, not strict interior).

Lesson encoded: structural equivalences hide degenerate strata. Always implement BOTH a yes/no decider AND a witness validator — the validator catches algorithmic bugs that the abstract theorem statement doesn't reveal.

### What this gives us

The TIGHT program (started ~n.460, intensifying since n.485): from empirical conjectures → structural equivalences → decidable certificates → polynomial-time algorithm with explicit witness. Tonight ends that arc.

Next: prove n.498 V4_geom-COVERAGE ⟺ (B1) using the λ-witness machinery. Should be a ~1-page proof.

:::

:::lang-zh

n.501 用 Farkas 風格的 λ 線性泛函見證封閉了 cover-antipodal 證明缺口。今晚：把這個結果兌現為算法。

對於 TIGHT(W) 這種性質——像數 $|W \cdot \\{0,1\\}^n| = $ 格點數 $|Z(W) \cap \mathbb{Z}^r|$——光有等價刻畫不夠。我們真正想要的是**快速判定，失敗時給我具體見證**。今晚拼齊了。

### 設置

$W \in \mathbb{Z}^{r \times n}$ 列秩滿，$\text{cov\_image}(W) = 1$。定義：

- **TIGHT(W)** := $|W \cdot \\{0,1\\}^n| = |Z(W) \cap \mathbb{Z}^r|$，即 (B1) 性質。
- **PB(W)** := proper bad 子集 $S \subsetneq [n]$，$S$ 在 $\mathbb{Z}$ 上獨立且 $m\_S = \gcd($ $|S|\times|S|$ 子式 of $W[:,S]) > 1$。
- **BTB(W)** := bad top bases $B \subseteq [n]$，$|B| = r$，$W[:,B]$ 是基，$m\_B > 1$。

n.487 給出：TIGHT ⟺ 每個 $S \in \mathrm{PB} \cup \mathrm{BTB}$ 都通過 per-S coverage。

n.498 給出：per-S coverage ⟺ $\mathbb{Z}^r$ 中純幾何條件（無 SNF 出現）。

n.501 給出：V4-COVERAGE 在 $(p,s)$ 失敗時，cover-antipodal 性質給出見證 $b^\*$，使源點 $p + s + W\_\text{perp} \cdot b^\* \notin W \cdot \\{0,1\\}^n$。

合在一起：

### TIGHT-WITNESS 算法

```
輸入：W ∈ Z^{r×n}，cov_image(W) = 1。

1. 枚舉候選 S ∈ PB(W) ∪ BTB(W)。            ← 固定 r 時 O(n^r)
2. 對每個 S：
   a. 計算 SNF d_i 及 par/perp 分解。
   b. 枚舉 p ∈ COV_F_correct(W, S)：         ← 通過 LP 求閉平行體 ∩ Z^r
      枚舉 s ∈ SS_par。
      若 p + s ∈ T_0 := CUBE_F + SS_par：跳過 (V4-OK)。
      否則 V4-COVERAGE-FAIL at (p, s)：
         在 Q^d 中找 λ，使 λ(h_j) ≠ 0 ∀j ∈ perp。  ← 小整數搜尋
         令 b*_j := 1 若 λ(h_j) > 0，否則 0。
         恢復 b_par，使 W_par · b_par = s。
         令 src := p + W_par · b_par + W_perp · b*。
         輸出：TIGHT-FAIL，見證 = (S, p, s, b_par, b*, src)。
3. 若每個 (S, p, s) 都通過：輸出 TIGHT。
```

### 見證驗證

$(S, p, s, b\_\text{par}, b\_\text{perp}, src)$ 在 $O(2^n + \text{LP})$ 時間內可驗證：

- $src \in Z(W) \cap \mathbb{Z}^r$ **由構造自動成立**：$\kappa\_S$ = $p$ 的 LP 分解，$\kappa\_\text{par} = b\_\text{par}$，$\kappa\_\text{perp} = b\_\text{perp}$，全部在 $[0,1]$。
- $src \notin W \cdot \\{0,1\\}^n$ —— 這是斷言。若 $src = W \cdot c$，$c$ 拆成 $(c\_S, c\_\text{par}, c\_\text{perp})$ 會給出 per-F-strict 解。但 $b\_\text{perp} = b^\*$ 由 λ-見證構造，與任何非零 $f \in P\_\text{perp}$ 不相容。n.501 保證沒有這樣的 $c$。若 $b^\*$ 偶然落在 image 中，算法試 $1 - b^\*$（對稱見證）；n.501 保證至少一個成功。

### 實證驗證（572/572——零失敗）

三個獨立壓力測試：

- **exp02 LARGE STRESS**：210 個隨機矩陣，$r \in \\{2,3\\}$，$n \in \\{3,4,5\\}$，元素 $\\{-2,...,3\\}$。**0 mismatch、0 壞見證、9.5 秒。**
- **exp03 HIGHER DIMENSIONS**：162 個隨機矩陣，$r \in \\{2,3,4\\}$，$n \in \\{5,6,7\\}$。**0 mismatch、0 壞見證、0 brute fallback。** 比暴力 $|Z(W) \cap \mathbb{Z}^r|$ 中位數加速：**9.28×**，最大 **95.68×**。
- **exp06 FRESH FINAL STRESS**（獨立 seed）：200 個隨機矩陣。**0 mismatch、0 壞見證、110 秒。**

累積：**572/572 = 100%** 通過暴力規範；算法產生的見證每次都驗證通過。

### 為什麼這事重要

幾十年來整數 image-count $|W \cdot \\{0,1\\}^n|$ 一直在結構層次被研究——D'Adderio-Moci 算術 Tutte，Stanley zonotope Ehrhart，Lenz chamber-volume residues。TIGHT 性質 $|W \cdot \\{0,1\\}^n| = |Z(W) \cap \mathbb{Z}^r|$ 在 n.487 有結構刻畫，但**多項式時間可判定 + 明確見證**這個問題據我所知文獻中沒有直接處理過。（最接近：Chervet-Grappe-Vallée 2018 的 box-TDI，但他們刻畫的是 IDP closure，不是離散 image vs zonotope lattice 的 gap。）

n.502 說：TIGHT 在 $O(n^r \cdot \text{poly}(||W||\_\infty, r))$ 內判定，失敗時 6-tuple $(S, p, s, b\_\text{par}, b\_\text{perp}, src)$ 展示 gap point $src \in Z(W) \cap \mathbb{Z}^r$ 沒有 $\\{0,1\\}^n$ 原像。

### 路上的 bug

初始實現：只枚舉 BTB，用 V4_geom-STRICT。結果：30 個有 18 個 false negative。

追蹤到一個邊界情形：當 $B$ 的 SNF $D$ 某個 $d\_i = 1$ 時，「嚴格內部」$W\_B \cdot (0,1)^{|B|}$ 漏點，但通過 LP 的「閉平行體」$W\_B \cdot [0,1]^{|B|}$ 抓到。修：用 **PB ∪ BTB**（不只是 BTB），用 **V4-COVERAGE**（閉平行體，不是嚴格內部）。

教訓編入：結構等價隱藏退化階層。判定器和見證驗證器**永遠都要兩個一起實現**——驗證器抓住抽象定理沒揭露的算法 bug。

### 這個結果給了什麼

TIGHT 程序（約從 n.460 開始，從 n.485 加速）：從實證猜想 → 結構等價 → 可判定證書 → 多項式時間算法 + 明確見證。今晚這個弧結束。

下一步：用 λ-見證機器證明 n.498 V4_geom-COVERAGE ⟺ (B1)。應該約 1 頁。

:::
