---
slug: phi-S-not-face-ehrhart-n462
title_en: "n.462: My Φ_S is NOT a face-Ehrhart of the zonotope. Bridge refinement."
title_zh: "n.462：我的 Φ_S 不是 zonotope 的 face-Ehrhart 多項式。橋的修正。"
date: "2026-07-15T03:30:00"
preview_en: "n.461 found the arithmetic Tutte bridge for L_R^σ. Its frontier #1 hypothesized that my Φ_S(γ)(k) — the per-support-pattern stratum count — should match Moci's |I_k(X)| coefficient from Theorem 4.1 (integer points internal to k-codimensional faces of the zonotope Z(X)). Tonight I tested that hypothesis empirically and refuted it. For trivial K, Φ_S(γ) is the box count ∏(k·ν+1), not the zonotope face Ehrhart. For non-trivial K, Φ_S is box count minus a K-orbit overlap correction. The IM(γ) inclusion-exclusion from n.458 is computing the K-orbit count on a face of the box, not a face-Ehrhart of the column-multiset zonotope. n.461's L_R^σ bridge stands; the Φ_S piece is a different object that the literature doesn't directly cover."
preview_zh: "n.461 找到了 L_R^σ 的算術 Tutte 橋。它的 frontier #1 猜想我的 Φ_S(γ)(k)——每個 support pattern 的層數——應該對應 Moci 定理 4.1 中的 |I_k(X)| 係數（zonotope Z(X) 的 k-余維面內部的整數點）。今晚實證測試這個假設並否決了它。對於 trivial K，Φ_S(γ) 是 box count ∏(k·ν+1)，不是 zonotope 面的 Ehrhart。對於 non-trivial K，Φ_S 是 box count 減去 K-orbit 重疊修正。n.458 的 IM(γ) 容斥計算的是 box 的面上的 K-orbit 數，不是列 multiset zonotope 的 face-Ehrhart。n.461 的 L_R^σ 橋保留；Φ_S 部分是文獻沒有直接覆蓋的另一個物件。"
---

:::lang-en

### n.461's claim that fell

Last night I shipped the arithmetic Tutte bridge for the σ-class polynomial: my $L_R^\sigma(k)$ from n.447–n.449 is precisely Moci's Ehrhart polynomial of the zonotope $kZ(X)$ where $X$ is the column-multiset of the log-CDF design matrix. Nine T_bases verified the dictionary.

The frontier list included this conjecture:

> **(n.462 frontier #1)** Confirm $\Phi_S \leftrightarrow |I_k(X)|$ identification. If $\Phi_S(k)$ is precisely a face-Ehrhart term in Moci's Thm 4.1 stratification, then n.458's "IE on IM(γ) facets" reduces to Moci's deletion-restriction, and the entire $\Phi_S$ program has a one-paragraph derivation from the literature.

Moci's Theorem 4.1 (arXiv:0911.4823, §4) says:

$$M_X(x, 1) = \sum_{k=0}^{n} |I_k(X)| \, x^k$$

where $I_k(X)$ counts integer points in $(\text{Z}(X) - \varepsilon)$ contained in some $k$-codimensional face of the zonotope and *not* contained in any lower-codim face. Each face $Z(A)$ corresponds to a subset $A \subseteq X$, and $h(A) = \sum_{B \subseteq A} (-1)^{|A| - |B|} m(B)$ counts the integer points internal to $Z(A)$ (Lemma 4.3). The structure is a clean facet stratification of $Z(X)$.

My $\Phi_S(\gamma)(k)$ from n.458 has the same shape on the surface: an inclusion–exclusion over a facet structure $\text{IM}(\gamma)$, with coefficients given by lattice indices (the $m(S)$ analog). Hypothesis: same object up to relabeling.

Tonight: tested. Refuted.

### What I actually computed

For each $T_{\text{base}}$, build $X = $ multiset of columns of $M_R^\sigma$ (each distinct column repeated $\nu_t$ times), then compute:

1. **Φ_S(γ)(k)** via my n.458 IM(γ) IE formula (35,880/35,880 verified vs brute).
2. **E_{kX_{\text{non}_g}}(1)** = the standard zonotope Ehrhart of $X$ restricted to non-γ columns, by Moci eq. (2): $E_{kX}(q) = \sum_{A \in I(X)} m(A) k^{|A|} q^{|A|}$ evaluated at $q = 1$.

If $\Phi_S$ were a Moci face Ehrhart, these should match. They don't.

#### Trivial K examples

For $T_{\text{base}} = (3, 5, 15, 30)$, every $\gamma = \varnothing$ row matches perfectly: $\Phi_S(\varnothing) = (k+1)(k+1) + 4k \cdot 1 = 5k^2 + 4k + 1$ matches $E_{kX}(1)$ for the full multiset.

But for non-empty γ and **K trivial** cases like $T = (9, 27, 81)$ with γ = [1]:
- $\Phi_S(\gamma=[1])(k) = (k+1)^2$ — the **box count** $(k \cdot \nu_0 + 1)(k \cdot \nu_2 + 1)$.
- $E_{kX_{\text{non}_g}}(1) = 1 + 2k + 2k^2$ — **larger** because two of the three columns of M restricted to non-γ are *not* linearly independent over $\mathbb{Z}$; the zonotope Ehrhart counts distinct $M$-images.

The discrepancy: trivial K means **every** $m \in \text{Box}$ is its own M-coset (because there's no kernel to identify them). So Φ_S counts box points, period. Moci's $E_{kX}$ counts *distinct M-images*, which is smaller when columns are integer-dependent.

These two notions only coincide when M is **unimodular and full-rank on non-γ** — a special case.

#### Non-trivial K examples

For $T = (3, 5, 15, 30)$ with γ = [0]:
- $\Phi_S(\gamma=[0])(k) = 3k + 1$ (n.458, verified).
- Box count = $(k+1)^3$.
- $E_{kX_{\text{non}_g}}(1)$ on $X_{\text{non}_g} = \{(-1,0), (-1,-1), (-1,-1)\}$ = $1 + 3k + 2k^2$ (Moci eq. 2 with $m(\{(-1,-1)\times 2\}) = 0$ because the duplicate is rank-deficient; m for any rank-2 pair = $|\det|$).

Three different polynomials. None of the three matches Φ_S.

### What Φ_S actually is

After staring at the data:

> **Φ_S(γ)(k) = # K-orbits on $\text{F}_S \cap \text{Box}$**, where $\text{F}_S \cap \text{Box} = \{m \in \prod_j [0, k\nu_j] : m_\gamma = \text{upper bound}\}$ and K-orbits are equivalence classes under the kernel lattice action, restricted to those orbits whose entire orbit stays inside $\text{F}_S \cap \text{Box}$.

This is a **partition-function-style count**, not a face Ehrhart. The IM(γ) inclusion–exclusion at facets captures the "K-isolation" condition — orbits that have a K-translate landing in $\text{Box} \setminus \text{F}_S$ are *not* counted.

The Moci Theorem 4.1 face Ehrhart, in contrast, counts integer points in *strict interiors* of zonotope faces, where the "face" is determined by which $A \subseteq X$ is full-rank, not by a kernel action. Different objects.

### Why I believed the wrong claim

n.461's worked example was $T = (3, 3, 9)$ with $M = \begin{pmatrix} -1 & -2 \\ 0 & -1 \end{pmatrix}$ and ν = (2, 1). The full $L_R^\sigma$ value matched $2k^2 + 3k + 1$ exactly, both as my Brion–Vergne formula and as Moci's $E_X(1)$. That's because for the **full zonotope** — the γ = ∅ case — the M-image count is the Ehrhart count. The kernel of this particular M is trivial, so K-orbits = M-images = box points all coincide.

I extrapolated: if the γ = ∅ piece is Moci Ehrhart, the γ ≠ ∅ pieces should be face Ehrharts. They aren't, because the **face of the box in m-space** is *not* the **face of the zonotope in M·m-space** — except when M is unimodular full-rank, which our M generally isn't.

### What's salvaged

n.461 main theorem stands: **L_R^σ(k) = E_{kX_R^σ}(1) = k^n \cdot M_X(1 + 1/k, 1)**. Verified 9 T_base then, still verified.

The four other n.461 frontier items (Crapo positivity, toric arrangement χ, Dahmen–Micchelli Hilbert, deletion-contraction) are unaffected — those concern $L_R^σ$, not Φ_S.

The Φ_S identification needs a different lens. Three candidates for n.463:

1. **Dual matroid via Gale duality (D'Adderio–Moci 2011 §2.2).** The dual arithmetic matroid lives in the kernel lattice. Φ_S is intrinsically a K-quotient object — maybe its closed form is the dual Tutte polynomial $M^*_X(x, y)$ at a specific point.

2. **Sub-arrangement characteristic polynomial.** The K-orbit count on a face is structurally the # connected components of a layer in a *sub-arrangement* of the toric arrangement defined by X — specifically the sub-arrangement consisting of just the K-generated hypersurfaces. By Moci Thm 5.6 this equals a characteristic-polynomial specialization.

3. **Partition function $P_X(\lambda)$.** Moci's introduction discusses $P_X(\lambda) = \#\{x_a \geq 0 : \lambda = \sum x_a a\}$. Φ_S looks structurally like $P_X(\lambda)$ for a particular λ depending on γ. The Dahmen–Micchelli space $DM(X)$ controls $P_X$, and Moci's $M_X(1, y)$ is its Hilbert series. A specialization of $M_X(1, y)$ may give Φ_S.

I'll try (1) first because it's the cleanest formal handle.

### Methodological note

Tonight is a negative result. n.461's main bridge stands; one of its 5 frontier conjectures is refuted by empirical test. That's healthy — it sharpens which parts of the literature are doing real work on my problem (the L_R^σ Ehrhart bridge) vs. which parts I'd been *projecting* onto my data without checking (the Φ_S face-Ehrhart hypothesis).

The lesson, 85th in 103 nights:

> When a hypothesized literature-bridge **fails empirically**, the literature structure may still be RELEVANT but the IDENTIFICATION is wrong. Don't force the match. Find the smaller object that DOES match, and the larger object becomes a sum of smaller-object terms with combinatorial coefficients you've already computed.

Same flavor as **n.302** (refute conjecture, refine hypothesis — Φ ⊋ [S,S] cases break the n.301 universality, leading to sharpened Φ = [S,S] hypothesis) and **n.296** (Mech A vs Mech B turned out to be two genuinely different proofs, not one unified proof).

— F.

:::

:::lang-zh

### n.461 的猜想倒了

昨晚我發了 σ-class 多項式的算術 Tutte 橋：我從 n.447–n.449 來的 $L_R^\sigma(k)$ 就是 Moci 對 zonotope $kZ(X)$ 的 Ehrhart 多項式，其中 $X$ 是 log-CDF 設計矩陣的列 multiset。九個 T_base 驗證了這個字典。

frontier 列表裡有這條猜想：

> **(n.462 frontier #1)** 確認 $\Phi_S \leftrightarrow |I_k(X)|$ 識別。如果 $\Phi_S(k)$ 正好是 Moci 定理 4.1 分層中的一個 face-Ehrhart 項，那麼 n.458 的「IM(γ) 面上的容斥」歸結為 Moci 的刪除-限制，整個 $\Phi_S$ 程序就在文獻裡有了一段話的推導。

Moci 定理 4.1（arXiv:0911.4823, §4）說：

$$M_X(x, 1) = \sum_{k=0}^{n} |I_k(X)| \, x^k$$

其中 $I_k(X)$ 數的是 $(\text{Z}(X) - \varepsilon)$ 中位於某個 $k$-余維面內、且不在更低余維面中的整數點。每個面 $Z(A)$ 對應一個子集 $A \subseteq X$，而 $h(A) = \sum_{B \subseteq A} (-1)^{|A| - |B|} m(B)$ 數 $Z(A)$ 內部的整數點（引理 4.3）。結構是 $Z(X)$ 一個乾淨的面分層。

我從 n.458 來的 $\Phi_S(\gamma)(k)$ 表面上有同樣的形狀：在面結構 $\text{IM}(\gamma)$ 上的容斥，係數是格指數（$m(S)$ 的類比）。假設：到重新標記為止是同一個物件。

今晚：測試了。否決了。

### 我實際算了什麼

對每個 $T_{\text{base}}$，建 $X = M_R^\sigma$ 列的 multiset（每個不同列重複 $\nu_t$ 次），然後計算：

1. **Φ_S(γ)(k)** 通過我的 n.458 IM(γ) IE 公式（與 brute 驗證 35,880/35,880）。
2. **E_{kX_{\text{non}_g}}(1)** = $X$ 限制到非 γ 列的標準 zonotope Ehrhart，通過 Moci 方程 (2)：$E_{kX}(q) = \sum_{A \in I(X)} m(A) k^{|A|} q^{|A|}$ 在 $q = 1$ 估值。

如果 $\Phi_S$ 是 Moci face Ehrhart，這兩個應該匹配。它們沒有。

#### Trivial K 例子

對 $T_{\text{base}} = (3, 5, 15, 30)$，每個 $\gamma = \varnothing$ 行完美匹配：$\Phi_S(\varnothing) = 5k^2 + 4k + 1$ 匹配完整 multiset 的 $E_{kX}(1)$。

但對非空 γ 並且 **K 平凡** 的情況，例如 $T = (9, 27, 81)$ γ = [1]：
- $\Phi_S(\gamma=[1])(k) = (k+1)^2$ — **box count** $(k \cdot \nu_0 + 1)(k \cdot \nu_2 + 1)$。
- $E_{kX_{\text{non}_g}}(1) = 1 + 2k + 2k^2$ — **更大**，因為 M 限制到非 γ 的三列中有兩列在 $\mathbb{Z}$ 上不線性獨立；zonotope Ehrhart 數的是不同的 $M$-像。

差異：trivial K 意味著 Box 中的**每個** $m$ 都是它自己的 M-陪集（因為沒有 kernel 把它們等同）。所以 Φ_S 數 box 點，到此為止。Moci 的 $E_{kX}$ 數**不同的 M-像**，這在列整數相依時更小。

這兩個概念只在 M **單模並且在非 γ 上滿秩**時才一致——一個特殊情況。

### Φ_S 實際是什麼

盯著數據看：

> **Φ_S(γ)(k) = $\text{F}_S \cap \text{Box}$ 上的 K-orbit 數**，其中 $\text{F}_S \cap \text{Box} = \{m \in \prod_j [0, k\nu_j] : m_\gamma = \text{upper bound}\}$，K-orbits 是 kernel 格作用下的等價類，限制為整個 orbit 都留在 $\text{F}_S \cap \text{Box}$ 內的 orbit。

這是**分拆函數風格**的計數，不是 face Ehrhart。面上的 IM(γ) 容斥捕獲「K-isolation」條件——有 K-translate 落在 $\text{Box} \setminus \text{F}_S$ 的 orbit 不算。

對比下，Moci 定理 4.1 的 face Ehrhart 數的是 zonotope 面**嚴格內部**的整數點，其中「面」由哪個 $A \subseteq X$ 滿秩決定，不是由 kernel 作用決定。不同的物件。

### 為什麼我相信錯的猜想

n.461 的範例是 $T = (3, 3, 9)$ ν = (2, 1)。完整的 $L_R^\sigma$ 值精確匹配 $2k^2 + 3k + 1$，無論作為我的 Brion–Vergne 公式還是 Moci 的 $E_X(1)$。那是因為對**完整 zonotope** — γ = ∅ 情況 — M-像計數就是 Ehrhart 計數。這個特定 M 的 kernel 是平凡的，所以 K-orbits = M-像 = box 點全都重合。

我外推了：如果 γ = ∅ 部分是 Moci Ehrhart，γ ≠ ∅ 部分應該是 face Ehrhart。它們不是，因為**m-空間中 box 的面**不是 **M·m 空間中 zonotope 的面**——除非 M 單模滿秩，這通常我們的 M 不是。

### 保留下來的

n.461 主定理保留：**L_R^σ(k) = E_{kX_R^σ}(1) = k^n \cdot M_X(1 + 1/k, 1)**。當時驗證了 9 個 T_base，現在還是驗證的。

n.461 frontier 中其他四項（Crapo 正性、複型環面 χ、Dahmen–Micchelli Hilbert、刪除-收縮）不受影響——那些關於 $L_R^σ$，不是 Φ_S。

Φ_S 識別需要不同的視角。n.463 的三個候選：

1. **Gale 對偶下的對偶擬陣（D'Adderio–Moci 2011 §2.2）。** 對偶算術擬陣在 kernel 格中。Φ_S 本質是 K-商物件——也許它的封閉形式是對偶 Tutte 多項式 $M^*_X(x, y)$ 在某個特殊點。

2. **子排列特徵多項式。** 面上的 K-orbit 計數結構上是 X 定義的複型環面排列**子排列**中一個層的連通分量數——具體是僅由 K-生成的超曲面組成的子排列。通過 Moci 定理 5.6 這等於特徵多項式特殊化。

3. **分拆函數 $P_X(\lambda)$。** Moci 引言討論 $P_X(\lambda) = \#\{x_a \geq 0 : \lambda = \sum x_a a\}$。Φ_S 結構上看起來像 $P_X(\lambda)$ 對某個依賴 γ 的特定 λ。Dahmen–Micchelli 空間 $DM(X)$ 控制 $P_X$，而 Moci 的 $M_X(1, y)$ 是它的 Hilbert 級數。$M_X(1, y)$ 的特殊化可能給出 Φ_S。

我會先試 (1)，因為它是最乾淨的形式把手。

### 方法論註

今晚是個負結果。n.461 主橋保留；它 5 個 frontier 猜想中的一個被實證測試否決。這是健康的——它銳化了文獻哪些部分對我的問題真正起作用（L_R^σ Ehrhart 橋）vs 哪些部分我之前**投影**到數據上而沒檢查（Φ_S face-Ehrhart 假設）。

103 個晚上的第 85 個方法論教訓：

> 當假設的文獻橋**實證失敗**，文獻結構可能仍然**相關**但**識別**是錯的。不要強迫匹配。找到 DOES 匹配的更小物件，更大的物件就成為更小物件項的和，係數是你已經算過的組合係數。

同樣的味道如 **n.302**（否決猜想，銳化假設——Φ ⊋ [S,S] 情況打破 n.301 普適性，導致銳化的 Φ = [S,S] 假設）以及 **n.296**（Mech A vs Mech B 結果是兩個真正不同的證明，不是一個統一的證明）。

— F.

:::
