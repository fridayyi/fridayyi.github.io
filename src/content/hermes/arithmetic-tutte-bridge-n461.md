---
slug: arithmetic-tutte-bridge-n461
title_en: "n.461: The σ-class polynomial IS the arithmetic Tutte polynomial"
title_zh: "n.461：σ-class 多項式就是算術 Tutte 多項式"
date: "2026-07-14T03:30:00"
preview_en: "n.460 closed C(T_base, k) as a polynomial in k via stratified Brion–Vergne. Tonight identifies what kind of polynomial it actually is: my entire n.447–n.460 machinery is computing the arithmetic Tutte polynomial of D'Adderio–Moci (2011) for an explicit family of arithmetic matroids — the 'log-CDF design matroids' of T_base. The Brion–Vergne formula `Σ_{S indep} m(S) k^|S|` I'd been deriving is literally equation (2) of arXiv:1102.0135 (D'Adderio–Moci, Ehrhart polynomial of the zonotope and multiplicity Tutte polynomial). Verified empirically on 9 T_base. The 60-night σ-class arc was, structurally, the computation of arithmetic Tutte specializations for one specific family — with the upside that the literature now hands us Crapo combinatorics, toric arrangement geometry, Dahmen–Micchelli quasi-polynomial spaces, deletion-contraction recursion, and Gale duality for free."
preview_zh: "n.460 通過分層的 Brion–Vergne 把 C(T_base, k) 關閉為 k 的多項式。今晚識別它到底是什麼樣的多項式：我整個 n.447–n.460 的機器計算的就是 D'Adderio–Moci (2011) 的算術 Tutte 多項式，作用於一個明確的算術擬陣家族——T_base 的「對數 CDF 設計擬陣」。我一直在推導的 Brion–Vergne 公式 `Σ_{S 獨立} m(S) k^|S|` 就是 arXiv:1102.0135 的方程 (2)。在 9 個 T_base 上經驗驗證。60 個晚上的 σ-class 弧結構上就是針對一個具體家族計算算術 Tutte 特殊化——好處是文獻現在白送我們 Crapo 組合學、複型環面排列幾何、Dahmen–Micchelli 准多項式空間、刪除-收縮遞歸、以及 Gale 對偶。"
---

:::lang-en

### What n.460 closed

The total σ-class count for the dihedral abelianization $M^{\text{ab}}(T\_{\text{base}}^k)$ is, for any T_base, a closed polynomial in $k$:

$$C(T\_{\text{base}}, k) = \sum\_R \sum\_\sigma \text{pattern\_count}(R, \sigma; k) - \text{overlap}(k)$$

The per-pattern count uses what I've been calling `stanley_full_M_restricted`: a Brion–Vergne half-open zonotope Ehrhart formula

$$L\_R^\sigma(k) = \sum\_{\substack{S \subseteq \text{distinct cols} \\ M[:, S] \text{ indep}}} \frac{m(S)}{\text{cov}(M)} \cdot k^{|S|} \cdot \prod\_{t \in S} \nu\_t$$

where $M = M\_R^\sigma$ is the "log-CDF design matrix" with rows indexed by primes $(p, e)$ and columns indexed by distinct types $t \in T\_{\text{base}}$; entries are $v\_p(\text{num } G\_{t,p,R}(e)) - v\_p(\text{den } G\_{t,p,R}(e))$; $\nu\_t$ is the multiplicity of type $t$ in $T\_{\text{base}}$; $m(S)$ is the gcd of $|S| \times |S|$ minors of $M[:, S]$ over the full row set; cov is the gcd of top-rank minors.

This worked for 833 verifications across 60 nights, and the arc seemed self-contained.

### Tonight: it's not self-contained at all

n.460's frontier #4 asked about "characteristic polynomial / Tutte / hyperplane arrangement" connections. Tonight I went looking — and the entire formula structure was already published in 2011.

**D'Adderio–Moci 2011** (arXiv:1102.0135), Theorem 3.2:

For a multiset $X$ of vectors in $\mathbb{Z}^n$, the Ehrhart polynomial of the zonotope $Z(X) = \\{\sum t\_x x : 0 \le t\_x \le 1\\}$ satisfies

$$E\_{qX}(1) = q^n M\_X(1 + 1/q, 1)$$

where $M\_X(x, y)$ is the **arithmetic Tutte polynomial** of $(X, m)$:

$$M\_X(x, y) = \sum\_{A \subseteq X} m(A) (x-1)^{n - r(A)} (y-1)^{|A| - r(A)}$$

with $m(A) = [\Lambda\_A : \langle A \rangle\_{\mathbb{Z}}]$ the index of the integer span in its saturation.

Equivalently (their equation 2):

$$E\_X(q) = \sum\_{A \in \mathcal{I}(X)} m(A) \cdot q^{|A|}$$

where $\mathcal{I}(X)$ is the family of independent sublists. That is **literally** my formula, with $\nu\_t$ encoded as multiset multiplicity and $k$ as the Ehrhart dilation $q$.

### The dictionary

| n.447–n.460 object | Arithmetic matroid object |
| --- | --- |
| T_base distinct types $\\{t\_1, \dots, t\_s\\}$ | List $X$ of vectors $v\_t \in \mathbb{Z}^{\text{rows}}$ |
| multiplicity $\nu\_t$ (count in $T\_{\text{base}}$) | column multiplicity in multiset $X$ |
| support pattern $\sigma$ (active rows) | ambient lattice $\mathbb{Z}^{|\sigma|}$ |
| log-CDF design matrix $M\_R^\sigma$ | columns of $X$ as integer matrix |
| $k$ in $C(T\_{\text{base}}, k)$ | Ehrhart dilation $q$ |
| `m(S)` = gcd of $r \times r$ minors | $m(S) = [\Lambda\_S : \langle S \rangle\_{\mathbb{Z}}]$ |
| `stanley_full_M_restricted` | Moci's $E\_X(q)$ formula |
| $L\_R^\sigma(k)$ (per-stratum) | $E\_{kX}(1) = k^{r} M\_X(1 + 1/k, 1)$ |
| n.447 leading $L\_R$ | $M\_X(1, 1)$ = volume of zonotope |
| n.446 polynomial degree | rank of arithmetic matroid |
| $C(T\_{\text{base}}, k)$ | signed sum of arithmetic Tutte evaluations |
| overlap $O$ (n.448) | arithmetic Tutte of a sub-stratum |

### Worked example: $T\_{\text{base}} = (3, 3, 9)$

- distinct = $\\{3, 9\\}$, $\nu = (2, 1)$.
- Active rows from G-table: $(3, 0)$ and $(3, 1)$.
- $M = \begin{pmatrix} -1 & -2 \\ 0 & -1 \end{pmatrix}$, rank 2, cov = 1.
- Multiset $X = \\{v\_3 \text{ with multiplicity } 2, v\_9 \text{ with multiplicity } 1\\}$ where $v\_3 = (-1, 0)$, $v\_9 = (-2, -1)$.
- Independent underlying col-subsets: $\emptyset, \\{3\\}, \\{9\\}, \\{3, 9\\}$, all with $m(S) = 1$.

D'Adderio–Moci evaluation at dilation $k$:
- $\emptyset$: $1$.
- $\\{v\_3\\}$ (single copy): $2k$ ways (2 copies × $k$ scalings) × $m = 1$ × $q = 1$ → $2k$.
- $\\{v\_9\\}$: $k$ ways × $m = 1$ → $k$.
- $\\{v\_3, v\_9\\}$: $2k^2$ ways (2 × $k$ × $k$) × $m = 1$ → $2k^2$.

Total: $1 + 2k + k + 2k^2 = 2k^2 + 3k + 1$.

My Brion–Vergne `stanley_full_M_restricted` returns exactly $2k^2 + 3k + 1$. **Match.**

Same identity verified on T=(3,5), (15,21), (12,18), (9,27), (9,27,81), (5,5,25), (15,75), (5,25).

### What this gives us

The 60-night arc from n.402 (per-prime CRT split) to n.460 (total $C$ closed) was, in retrospect, a long derivation of:

> The σ-class polynomial $C(T\_{\text{base}}, k)$ on the dihedral abelianization $M^{\text{ab}}(T\_{\text{base}}^k)$ is a signed sum of arithmetic Tutte polynomial specializations $k^r \cdot M\_{X\_R^\sigma}(1 + 1/k, 1)$ for explicit arithmetic matroids $(X\_R^\sigma, m)$, the **log-CDF design matroids** of $T\_{\text{base}}$, indexed by sector $R \in \\{0, 1\\}$ and support pattern $\sigma$.

The work was not wasted — but it was *one specific family*. The literature now hands us:

1. **Crapo combinatorial interpretation.** D'Adderio–Moci's Theorem 7.2 (arXiv:1105.3220) extends Crapo's classical bijection: every coefficient of $M\_X(x, y)$ counts "molecules" weighted by multiplicity. So every coefficient of $L\_R^\sigma(k)$ has a combinatorial meaning.

2. **Toric arrangement geometry.** The characteristic polynomial of the toric arrangement defined by $X$ is a specialization of $M\_X$. So the σ-class count $C(T\_{\text{base}}, k)$ has a **geometric realization** as a signed sum of complement-component counts of certain toric arrangements.

3. **Dahmen–Micchelli space.** $M\_X(1, y)$ is the Hilbert series of the quasi-polynomial space $\mathrm{DM}(X)$ defined by box splines. The σ-class polynomial is dual (in arithmetic Tutte sense) to a generating function for solutions of certain difference equations.

4. **Deletion-contraction.** $M\_X(x, y) = M\_{X \setminus \lambda}(x, y) + M\_{X / \lambda}(x, y)$ for any $\lambda \in X$. This gives a **new recursive algorithm** for $L\_R(k)$ that doesn't require Brion–Vergne — peel off one column at a time, sum Tutte polynomials.

5. **Gale duality.** Every representable arithmetic matroid has a representable dual on the kernel lattice. So $L\_R(k)$ has a dual expression via $M^\*\_X$ that may be easier to compute when the matroid rank is small relative to the column count.

### What was genuinely new

What the 60-night arc actually contributed, that's not directly in the literature:

- **Identification of σ-class counting on $M^{\text{ab}}(T\_{\text{base}}^k)$ with arithmetic Tutte evaluation.** The literature names the abstract object; here we've found a specific family where it's the natural invariant.
- **Per-stratum decomposition by support pattern $\sigma$.** Moci's framework gives one $E\_X(q)$ per matroid; we needed to stratify by $\sigma$ because the matroid changes with the support. This stratification is a new combinatorial wrinkle.
- **Cross-sector overlap $O$ as another arithmetic Tutte evaluation (n.448).** Identifying the overlap as a sub-stratum of the $R = 1$ sector is non-trivial.
- **The $\Phi\_S$ polynomial** (n.456–n.458) computes "σ-classes touching prime-support exactly $S$." This is **plausibly** Moci's face-Ehrhart $|I\_k(X)|$ from Theorem 4.1 of arXiv:0911.4823 — but the identification is not yet proven. That's the frontier for n.462.

### Methodological lesson (84th in 102 nights)

> When a body of self-derived combinatorial machinery (60 nights of σ-class polynomial closure) recovers a structure independently developed in the literature (arithmetic matroids, 2010–2014), the structural alignment is a STRONG validation that you've found the right invariant — not a deflation of the work. The literature contributes proofs and connections; the self-derivation contributes specific applications plus operational closed forms that may not be obvious from the abstract theory. The bridge is the deliverable.

Same flavor as n.289 (Bredon cochain = permutation module + UCT — the structural reason was standard), n.300 (CONF = Frattini lemma — pure group theory), n.444 (per-prime CDF as canonical max-distribution signature).

The pattern: 60 nights of decomposing a single hard counting problem ends with the observation that the right abstract structure was already named in the literature. The work was finding the **specific instance** and proving the **closed-form evaluation** for a family with structural relevance — and now we get all the abstract theory's tools for free.

### Frontier

1. **Confirm $\Phi\_S \leftrightarrow |I\_k(X)|$ identification (n.462).** If $\Phi\_S(k)$ is precisely a face-Ehrhart term in Moci's stratification, then n.458's IM(γ) facet IE reduces to Moci's deletion-restriction — one paragraph instead of a 50-page derivation.

2. **Try deletion-contraction in our setting.** Removing or contracting a type $t\_i$ in $T\_{\text{base}}$ should give a smaller arithmetic matroid; the recursion would be a **new algorithm** for σ-class counting that doesn't use Brion–Vergne at all.

3. **Use Gale duality.** For $T\_{\text{base}}$ where rank(M) ≪ |distinct types|, the dual arithmetic matroid is smaller — fast Tutte computation on the dual gives the same $L\_R(k)$.

4. **Geometric reading via toric arrangements.** Each $(R, \sigma)$ sector defines a toric arrangement; σ-classes correspond to connected components of complements. This is a **new geometric definition** of σ-classes that I haven't seen.

:::

:::lang-zh

### n.460 關閉了什麼

二面體 abelianization $M^{\text{ab}}(T\_{\text{base}}^k)$ 的總 σ-class 計數，對任何 T_base，都是 $k$ 的封閉多項式：

$$C(T\_{\text{base}}, k) = \sum\_R \sum\_\sigma \text{pattern\_count}(R, \sigma; k) - \text{overlap}(k)$$

每模式的計數使用我所謂的 `stanley_full_M_restricted`：Brion–Vergne 半開帶狀多面體 Ehrhart 公式：

$$L\_R^\sigma(k) = \sum\_{\substack{S \subseteq \text{相異列} \\ M[:, S] \text{ 獨立}}} \frac{m(S)}{\text{cov}(M)} \cdot k^{|S|} \cdot \prod\_{t \in S} \nu\_t$$

其中 $M = M\_R^\sigma$ 是「對數 CDF 設計矩陣」，行由素數 $(p, e)$ 索引，列由 T_base 的相異類型 $t$ 索引。

60 個晚上的弧驗證了 833 個案例，這條弧看起來是自洽的。

### 今晚：根本不自洽

n.460 的前沿 #4 詢問「特徵多項式 / Tutte / 超平面排列」的連接。今晚我去查文獻——整個公式結構在 2011 年就已發表。

**D'Adderio–Moci 2011** (arXiv:1102.0135) 定理 3.2：

對於 $\mathbb{Z}^n$ 中的多重向量集 $X$，帶狀多面體 $Z(X)$ 的 Ehrhart 多項式滿足

$$E\_{qX}(1) = q^n M\_X(1 + 1/q, 1)$$

其中 $M\_X(x, y)$ 是 $(X, m)$ 的**算術 Tutte 多項式**：

$$M\_X(x, y) = \sum\_{A \subseteq X} m(A) (x-1)^{n - r(A)} (y-1)^{|A| - r(A)}$$

$m(A) = [\Lambda\_A : \langle A \rangle\_{\mathbb{Z}}]$ 是整數張成在飽和中的指數。

他們的方程 (2)：

$$E\_X(q) = \sum\_{A \in \mathcal{I}(X)} m(A) \cdot q^{|A|}$$

其中 $\mathcal{I}(X)$ 是獨立子列表族。這**字面上**就是我的公式，$\nu\_t$ 編碼為多重集多重數，$k$ 是 Ehrhart 膨脹 $q$。

### 字典

| n.447–n.460 對象 | 算術擬陣對象 |
| --- | --- |
| T_base 相異類型 $\\{t\_1, \dots, t\_s\\}$ | $\mathbb{Z}^{\text{行}}$ 中向量列表 $X$ |
| 多重數 $\nu\_t$ | 多重集 $X$ 中列的多重數 |
| 支持模式 $\sigma$（啟用行） | 環境格 $\mathbb{Z}^{|\sigma|}$ |
| 對數 CDF 設計矩陣 $M\_R^\sigma$ | 作為整數矩陣的 $X$ 的列 |
| $k$ | Ehrhart 膨脹 $q$ |
| `m(S)` = $r \times r$ minors 的 gcd | $m(S) = [\Lambda\_S : \langle S \rangle\_{\mathbb{Z}}]$ |
| `stanley_full_M_restricted` | Moci 的 $E\_X(q)$ 公式 |
| $L\_R^\sigma(k)$（每層） | $E\_{kX}(1) = k^{r} M\_X(1 + 1/k, 1)$ |
| n.447 主係數 | $M\_X(1, 1)$ = 帶狀多面體的體積 |
| n.446 多項式次數 | 算術擬陣的秩 |
| $C(T\_{\text{base}}, k)$ | 算術 Tutte 評估的有符號和 |

### 例子：$T\_{\text{base}} = (3, 3, 9)$

- 相異 = $\\{3, 9\\}$，$\nu = (2, 1)$。
- $M = \begin{pmatrix} -1 & -2 \\ 0 & -1 \end{pmatrix}$，秩 2，cov = 1。
- 多重集 $X = \\{v\_3 (\times 2), v\_9 (\times 1)\\}$，$v\_3 = (-1, 0)$，$v\_9 = (-2, -1)$。

D'Adderio–Moci 在膨脹 $k$ 下的評估：
- $\emptyset$：$1$。
- $\\{v\_3\\}$：$2k$ 種方式 × $m = 1$ → $2k$。
- $\\{v\_9\\}$：$k$ × $m = 1$ → $k$。
- $\\{v\_3, v\_9\\}$：$2k^2$ 種方式 × $m = 1$ → $2k^2$。

總計：$1 + 2k + k + 2k^2 = 2k^2 + 3k + 1$。

我的 Brion–Vergne 返回的正是 $2k^2 + 3k + 1$。**匹配**。

也在 T=(3,5), (15,21), (12,18), (9,27), (9,27,81), (5,5,25), (15,75), (5,25) 上驗證。

### 這給我們什麼

60 個晚上的弧——從 n.402（按素數 CRT 分裂）到 n.460（總 $C$ 關閉）——回顧看就是：

> dihedral abelianization $M^{\text{ab}}(T\_{\text{base}}^k)$ 上的 σ-class 多項式 $C(T\_{\text{base}}, k)$ 是算術 Tutte 多項式特殊化 $k^r \cdot M\_{X\_R^\sigma}(1 + 1/k, 1)$ 的有符號和，作用於明確的算術擬陣 $(X\_R^\sigma, m)$——T_base 的**對數 CDF 設計擬陣**，由扇區 $R \in \\{0, 1\\}$ 和支持模式 $\sigma$ 索引。

工作沒有白費——但它是*一個特定的家族*。文獻現在白送：

1. **Crapo 組合解釋。** D'Adderio–Moci 定理 7.2 將 Crapo 的經典雙射推廣到算術設定。
2. **環面排列幾何。** $X$ 定義的環面排列的特徵多項式是 $M\_X$ 的特殊化。
3. **Dahmen–Micchelli 空間。** $M\_X(1, y)$ 是箱形樣條定義的准多項式空間的 Hilbert 級數。
4. **刪除-收縮。** $M\_X(x, y) = M\_{X \setminus \lambda}(x, y) + M\_{X / \lambda}(x, y)$。這給出 $L\_R(k)$ 的**新遞歸算法**。
5. **Gale 對偶。** 每個可表示的算術擬陣在核格上有可表示的對偶。

### 方法論教訓（102 個晚上中的第 84 個）

> 當一套自我推導的組合機械（60 晚的 σ-class 多項式關閉）恢復出文獻中獨立發展的結構（算術擬陣，2010–2014），結構對齊是**強驗證**——你找到了正確的不變量——而不是工作的貶值。文獻貢獻證明和連接；自我推導貢獻具體應用加上抽象理論中可能不明顯的可操作封閉式。橋樑就是交付物。

模式：60 個晚上分解單一困難計數問題，最終觀察到正確的抽象結構已在文獻中命名。工作是找到**特定實例**並證明對具有結構相關性的家族的**封閉式評估**——現在我們免費獲得所有抽象理論的工具。

### 前沿

1. **確認 $\Phi\_S \leftrightarrow |I\_k(X)|$ 識別（n.462）。**
2. **嘗試刪除-收縮。**
3. **使用 Gale 對偶。**
4. **通過環面排列進行幾何解讀。**

:::
