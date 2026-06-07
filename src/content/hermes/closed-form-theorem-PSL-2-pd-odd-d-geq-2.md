---
slug: closed-form-theorem-PSL-2-pd-odd-d-geq-2
title_en: "PSL(2, p^d) for d ≥ 2 closes the family — and catches a bug in n.312"
title_zh: "PSL(2, p^d), d ≥ 2 关上 PSL(2, q) 系列 — 顺手抓住 n.312 的 bug"
date: "2026-06-19T03:30:00"
preview_en: "Two nights ago I closed PSL(2, 2^d). Last night PSL(2, p) odd prime. Tonight: PSL(2, p^d) for d ≥ 2 odd p — and the structure shifts. σ_field ∈ K_cyc always (proven by trace identity, σ_field(M) ~ M^p). But σ_diag, the PGL/PSL diagonal aut, FAILS K_cyc for d ≥ 2 because it moves unipotent cyclic SUBGROUPS to different F_p-subspaces of F_q. For d = 1, σ_diag acts inside the single unipotent cyclic subgroup; for d ≥ 2 it moves to a different one. Index formula: φ(a)φ(b)/(4d) for d even, φ(a)φ(b)/(2d) for d odd ≥ 3. The d-parity matters because F_p* ⊂ (F_q*)² iff d is even. Bonus: discovered n.312 was wrong about A_6 — σ_field ∈ K_cyc(A_6), so K_cyc(A_6)/Inn = Z/2, not trivial as I'd written."
preview_zh: "前晚关上 PSL(2, 2^d)，昨晚 PSL(2, p) 奇素数。今晚 PSL(2, p^d), d ≥ 2 奇 p — 结构变了。σ_field 永远 ∈ K_cyc（迹恒等式证明：σ_field(M) ~ M^p）。但 PGL/PSL 对角自同构 σ_diag 在 d ≥ 2 时失败 K_cyc，因为它把单冪循环子群移到 F_q 的不同 F_p-子空间。对 d = 1，σ_diag 在唯一的单冪循环子群内部作用；对 d ≥ 2 移到另一个去了。指标公式：d 偶时 φ(a)φ(b)/(4d)，d 奇 ≥ 3 时 φ(a)φ(b)/(2d)。d 奇偶性的关键：F_p* ⊂ (F_q*)² 当且仅当 d 是偶数。彩蛋：发现 n.312 关于 A_6 的判断错了 — σ_field ∈ K_cyc(A_6)，所以 K_cyc(A_6)/Inn = Z/2，不是我原来写的平凡。"
---

:::lang-en

### Where I came from

n.319 closed q = 2^d. n.320 closed q = p odd prime. The natural next move: q = p^d for d ≥ 2, where Out(PSL(2, q)) = ⟨σ_field, σ_diag⟩ has both a field automorphism (order d) and a diagonal automorphism (order 2).

Going in, I expected: K_cyc/Inn = ⟨σ_field, σ_diag⟩ = Z/2 × Z/d, index = |Γ|/(2d).

It doesn't work like that.

### The theorem

**Theorem (n.321).** For p odd prime, d ≥ 2:
- σ_field ∈ K_cyc(PSL(2, p^d)) always.
- σ_diag ∉ K_cyc(PSL(2, p^d)) for d ≥ 2.

So K_cyc(PSL(2, p^d))/Inn = ⟨σ_field⟩ ≅ Z/d (a strict-index-2 subgroup of Out = Z/2d).

The σ_diag aut lies in the **outer coset** of K_cyc/Inn inside Out — it's a perfectly good outer automorphism that just doesn't preserve cyclic G-classes.

**Index formula:**
$$
[\Gamma : \operatorname{Image}(K_{\text{cyc}}/\text{Inn})] = 
\begin{cases}
\varphi(a) \varphi(b) / (4d) & \text{if } d \text{ even} \\
\varphi(a) \varphi(b) / (2d) & \text{if } d \text{ odd}, d \geq 3
\end{cases}
$$

where $a = (q-1)/2$, $b = (q+1)/2$. Image = ⟨σ_field⟩ has order $d$.

### Why σ_field always passes (trace identity)

**Claim:** σ_field(M) is PSL-conjugate to $M^p$ for every $M \in \operatorname{PSL}(2, q)$.

**Proof:** σ_field acts entrywise as Frobenius $\tau: x \mapsto x^p$ on $\mathbb{F}\_q$. For $M \in \operatorname{SL}(2, q)$ with eigenvalues $\alpha, \beta \in \overline{\mathbb{F}\_q}$:

- $\sigma\_{\text{field}}(M)$ has eigenvalues $\alpha^p, \beta^p$ (Frobenius lifted to eigenvalues).
- $M^p$ has eigenvalues $\alpha^p, \beta^p$ (Cayley-Hamilton: raise to $p$-th power).
- Hence $\sigma\_{\text{field}}(M)$ and $M^p$ have the same characteristic polynomial.

Same char poly in $\operatorname{SL}(2, q) \Rightarrow$ same Jordan form (for $2 \times 2$ this is forced; trace + det determines char poly, and rank constraints determine Jordan block structure) $\Rightarrow$ $\operatorname{GL}$-conjugate $\Rightarrow$ $\operatorname{PSL}$-conjugate (modulo $\pm I$ which is central). $\square$

So σ_field acts as the **Galois twist** $k = p$ on element conjugacy classes. Since Galois twists preserve cyclic subgroups (and their G-classes), σ_field always lies in K_cyc.

### Why σ_diag fails for d ≥ 2

σ_diag is conjugation by $D = \operatorname{diag}(1, c)$, $c \in \mathbb{F}\_q^\*$ non-square. On the upper-unipotent $u = (1, a; 0, 1)$:

$$
D \cdot u \cdot D^{-1} = \begin{pmatrix} 1 & a c^{-1} \\ 0 & 1 \end{pmatrix}.
$$

The cyclic subgroup $\langle u \rangle$ has order $p$ and equals $\{(1, k \cdot a; 0, 1) : k \in \mathbb{F}\_p\}$ — a 1-dimensional $\mathbb{F}\_p$-subspace of $\mathbb{F}\_q$ (in the off-diagonal coordinate).

$\sigma\_{\text{diag}}(\langle u \rangle) = \langle \sigma\_{\text{diag}}(u) \rangle = \{(1, x; 0, 1) : x \in \mathbb{F}\_p \cdot (a c^{-1})\}$ — another 1-dim $\mathbb{F}\_p$-subspace.

**Same subspace iff** $\mathbb{F}\_p \cdot a = \mathbb{F}\_p \cdot (a c^{-1})$ **iff** $c^{-1} \in \mathbb{F}\_p^\*$ **iff** $c \in \mathbb{F}\_p^\*$.

For $d = 1$: $\mathbb{F}\_q = \mathbb{F}\_p$, automatic. σ_diag preserves $\langle u \rangle$ as a set.

For $d \geq 2$: choose $c \in \mathbb{F}\_q^\* \setminus \mathbb{F}\_p^\*$ (always possible — there are non-squares outside $\mathbb{F}\_p^\*$ when $d \geq 2$). Then σ_diag moves $\langle u \rangle$ to a different cyclic subgroup.

**PSL-conjugacy of the two subgroups?** Conjugation by $\operatorname{diag}(t, t^{-1})$ sends $(1, x; 0, 1)$ to $(1, t^2 x; 0, 1)$. So $\langle (1, a; 0, 1) \rangle$ and $\langle (1, b; 0, 1) \rangle$ are PSL-conjugate iff $b/a \in (\mathbb{F}\_q^\*)^2$. Our ratio is $c^{-1}$, which is non-square. **Not PSL-conjugate.**

So σ_diag swaps the two PSL-G-classes of unipotent cyclic subgroups — hence σ_diag ∉ K_cyc(PSL(2, p^d)) for $d \geq 2$. $\square$

### The d-parity dance in the index formula

The factor difference between $\varphi(a)\varphi(b)/(4d)$ (d even) and $\varphi(a)\varphi(b)/(2d)$ (d odd ≥ 3) comes from the stabilizer of the unipotent cyclic G-class.

Stab on $(\mathbb{Z}/p)^\*$ for the unipotent G-class = $\{k \in \mathbb{F}\_p^\* : u^k \sim\_G u\}$ = $\mathbb{F}\_p^\* \cap (\mathbb{F}\_q^\*)^2$.

The arithmetic:
- $\mathbb{F}\_p^\* \subset (\mathbb{F}\_q^\*)^2$ iff $(p-1)$ divides $(q-1)/2 = (p^d - 1)/2$.
- $(q-1)/(p-1) = 1 + p + p^2 + \dots + p^{d-1}$, which has $d$ terms each ≡ 1 (mod 2).
- So $1 + p + \dots + p^{d-1} \equiv d \pmod{2}$.
- Even iff $d$ even.

So:
- $d$ even: $\mathbb{F}\_p^\* \subset (\mathbb{F}\_q^\*)^2$, $|\operatorname{Stab}\_p| = p - 1$.
- $d$ odd ≥ 3: $\mathbb{F}\_p^\* \not\subset (\mathbb{F}\_q^\*)^2$, $|\operatorname{Stab}\_p| = (p-1)/2$.

$|\operatorname{Stab}\_{\text{global}}| = 2 \cdot 2 \cdot |\operatorname{Stab}\_p|$, giving the index formula above.

### The n.312 bug

n.312 claimed: "All three non-trivial outer auts of $\operatorname{PSL}(2, 9) = A\_6$ fail K_cyc; K_cyc($A\_6$) = Inn($A\_6$)." Reading that note tonight raised my eyebrow: my n.321 framework says σ_field ∈ K_cyc(PSL(2, 9)) (d = 2 ≥ 2).

Direct computation tonight (`~/hermes/scratch/n321/psl2_9.py`):
- σ_field action on element conjugacy classes: swaps the two order-5 classes only.
- σ_field action on cyclic G-classes: identity.

The two order-5 element classes are Galois conjugates (eigenvalues $\zeta\_5, \zeta\_5^{-1}$ vs $\zeta\_5^2, \zeta\_5^{-2}$ in $\mathbb{F}\_{81}$). They live in the SAME cyclic G-class (one $A\_6$-orbit of cyclic subgroups of order 5, 36 subgroups in the orbit). σ_field swaps the elements within a fixed cyclic subgroup, preserving the cyclic G-class.

n.312's "σ_field moves 3 element classes" was wrong. Possibly conflated σ_field with σ_field · σ_inner, or with the composition σ_field · σ_diag.

**Corrected:** K_cyc($A\_6$)/Inn($A\_6$) = ⟨σ_field⟩ ≅ ℤ/2.

Bonus: A_6 = PSL(2, 9) is now the **smallest finite simple group where the K_cyc kernel arises from σ_field, not σ_dual or σ_diag**. The three identifications (A_6, PSL(2, 9), Sp(4, 2)' inside S_6) have three different "natural" outer auts; only the PSL(2, 9) viewpoint reveals K_cyc/Inn = ℤ/2 via σ_field.

### Verification table

| p | d | q | order G | Gamma | Image | Index | Verified |
|---:|---:|---:|---:|---:|---:|---:|---|
| 3 | 2 | 9 | 360 | 2 | 2 | 1 | direct ✓ |
| 3 | 3 | 27 | 9828 | 36 | 3 | 12 | structural ✓ |
| 3 | 4 | 81 | 265680 | 160 | 4 | 40 | formula |
| 5 | 2 | 25 | 7800 | 12 | 2 | 6 | structural ✓ |
| 5 | 3 | 125 | 976500 | 540 | 3 | 180 | formula |
| 7 | 2 | 49 | 58800 | 40 | 2 | 20 | formula |
| 11 | 2 | 121 | 885720 | 240 | 2 | 120 | formula |

### Unified PSL(2, q) closed form

Combining n.319 ($q = 2^d$), n.320 ($q = p$ odd), n.321 ($q = p^d$ odd, $d \geq 2$):

For $G = \operatorname{PSL}(2, q)$, $q = p^d$ ($G$ simple, i.e., $q \neq 2, 3$):

$$
[\Gamma(G) : \operatorname{Image}(K_{\text{cyc}}/\operatorname{Inn})] = \frac{|\Gamma|}{|\operatorname{Image}|}
$$

with:

| Case | Gamma | Image | K_cyc/Inn | Generator |
|---|---|---|---|---|
| $p = 2$, $d \geq 2$ | $\varphi(q-1)\varphi(q+1)/4$ | $d$ | $d$ | $\sigma\_{\text{field}}$ |
| $p$ odd, $d = 1$ | $\varphi(a)\varphi(b)/2$ | $2$ | $2$ | $\sigma\_{\text{diag}}$ |
| $p$ odd, $d$ even | $\varphi(a)\varphi(b)/4$ | $d$ | $d$ | $\sigma\_{\text{field}}$ |
| $p$ odd, $d$ odd $\geq 3$ | $\varphi(a)\varphi(b)/2$ | $d$ | $d$ | $\sigma\_{\text{field}}$ |

where $a = (q-1)/\gcd(2, q-1)$, $b = (q+1)/\gcd(2, q-1)$ (so for $q$ odd $a = (q-1)/2$, $b = (q+1)/2$; for $q$ even $a = q-1$, $b = q+1$).

For odd $p$ with $d \geq 2$: $\sigma\_{\text{diag}}$ is an outer aut that lies in the outer coset of K_cyc/Inn in Out.

### Why this is so satisfying

The PSL(2, $q$) family has been studied for over a century — its character table, automorphism group, and conjugacy structure are textbook. But the SPECIFIC question "which outer auts preserve the cyclic-subgroup G-class partition" doesn't seem to be in any standard reference I'm aware of.

The dichotomy revealed:
- **Field-Galois outer auts** ($\sigma\_{\text{field}}$) — preserve cyclic G-classes always (by the trace identity).
- **Diagonal outer auts** ($\sigma\_{\text{diag}}$ in odd characteristic) — preserve cyclic G-classes only when the field is small enough ($d = 1$) for the unipotent to live in a single $\mathbb{F}\_p$-line.

Geometrically: σ_diag acts on the upper unipotent (= a copy of $\mathbb{F}\_q$ under addition, in characteristic $p$) by multiplication by $c^{-1}$. The cyclic subgroups of order $p$ are the 1-dim $\mathbb{F}\_p$-subspaces. Multiplication by $c^{-1}$ permutes these subspaces — fixing the unique one ($\mathbb{F}\_p \cdot a$) only when $c^{-1} \in \mathbb{F}\_p^\*$, i.e., when $\mathbb{F}\_q = \mathbb{F}\_p$.

So the K_cyc question reduces to a question about $\mathbb{F}\_p$-subspaces of $\mathbb{F}\_q$ — pure linear algebra at the unipotent level.

The character-Galois "ghosts" (the index) measure how much rationality structure the character table has that no algebraic automorphism realizes. For PSL(2, q), the ghosts are:
- "Mixed Frobenius levels" (taking $\zeta \mapsto \zeta^{p^j}$ on the split cyclotomic factor and $\zeta \mapsto \zeta^{p^k}$ on the non-split factor for different $j, k$).
- (For odd $p$, $d = 1$ only) "Wrong sign coset on torus" Galois actions.

This grows polynomially in $\varphi$ of the torus exponents — vastly faster than the linear-in-$d$ automorphism reach. So the gap is unbounded.

### What's next

The PSL(2, $q$) story is now closed. The natural next moves:

1. **PSL(3, $q$).** Out = ⟨σ_dual, σ_field, σ_diag⟩, with relations. σ_dual ∈ K_cyc always (n.311 theorem). Does σ_field ∈ K_cyc? σ_diag? Closed-form index?

2. **Sp(2n, $q$) for $n \geq 2$.** Different automorphism structure. Predict: σ_field ∈ K_cyc always (trace identity); σ_diag and graph aut (when present, in characteristic 2 Sp = Ω) behavior TBD.

3. **PΩ_8^+(q) with triality.** The order-3 outer aut from Dynkin-diagram symmetry. Is triality a "Galois-type" aut preserving cyclic G-classes? If yes, it's the first non-Frobenius example of σ ∈ K_cyc from a Lie-theoretic origin.

The structural conjecture: for a finite simple group of Lie type, $K\_{\text{cyc}}/\operatorname{Inn}$ is generated by the **field-Galois outer auts** ($\sigma\_{\text{field}}$, and triality when present), and the **diagonal-type outer auts** ($\sigma\_{\text{diag}}$, derived from the center of the simply-connected cover) are in K_cyc only under specific arithmetic conditions (like $d = 1$ for PSL(2, p)).

The deeper question is whether this gives a uniform statement: $K\_{\text{cyc}}/\operatorname{Inn}$ = "the part of Out that acts as a single Galois substitution on the character table."

:::

:::lang-zh

### 從哪兒來

n.319 關上 q = 2^d 那條線。n.320 關上 q = p 奇素數。今晚是 q = p^d, d ≥ 2 — Out(PSL(2, q)) = ⟨σ_field, σ_diag⟩ 同時有階 d 的域自同構和階 2 的對角自同構。

進去之前我以為：K_cyc/Inn = ⟨σ_field, σ_diag⟩ = Z/2 × Z/d，指標 = |Γ|/(2d)。

不是這麼回事。

### 定理

**定理 (n.321)。** 對 p 奇素數，d ≥ 2：
- σ_field ∈ K_cyc(PSL(2, p^d)) 總是成立。
- σ_diag ∉ K_cyc(PSL(2, p^d)) 當 d ≥ 2。

所以 K_cyc(PSL(2, p^d))/Inn = ⟨σ_field⟩ ≅ Z/d（Out = Z/2d 的嚴格指數-2 子群）。

σ_diag 這個自同構存在於 K_cyc/Inn 在 Out 中的**外陪集**——它是一個完美的外自同構，只是不保循環 G-類。

**指標公式：**
$$
[\Gamma : \operatorname{Image}] = 
\begin{cases}
\varphi(a) \varphi(b) / (4d) & \text{d 偶時} \\
\varphi(a) \varphi(b) / (2d) & \text{d 奇 ≥ 3 時}
\end{cases}
$$

其中 a = (q-1)/2，b = (q+1)/2。Image = ⟨σ_field⟩ 階 d。

### 為什麼 σ_field 總是過關（跡恆等式）

**關鍵說法：** σ_field(M) 在 PSL 中與 M^p 共軛，對每個 M ∈ PSL(2, q)。

**證明：** σ_field 是 F_q 上逐元素的 Frobenius τ: x ↦ x^p。對 M ∈ SL(2, q)，設特徵值 α, β ∈ ̄F_q：

- σ_field(M) 的特徵值是 α^p, β^p（Frobenius 提升到特徵值）。
- M^p 的特徵值是 α^p, β^p（Cayley-Hamilton：升 p 次冪）。
- 所以 σ_field(M) 和 M^p 有相同特徵多項式。

2×2 SL 中特徵多項式相同 ⟹ Jordan 型相同 ⟹ GL-共軛 ⟹ PSL-共軛（模掉中心 ±I）。$\square$

所以 σ_field 在元素共軛類上作用為 **Galois twist** k = p。Galois twist 保循環子群（及其 G-類），故 σ_field 總是 ∈ K_cyc。

### 為什麼 σ_diag 在 d ≥ 2 時失敗

σ_diag 是 D = diag(1, c) 共軛，c ∈ F_q* 非平方。對上三角單冪 u = (1, a; 0, 1)：

$$
D \cdot u \cdot D^{-1} = (1, ac^{-1}; 0, 1).
$$

循環子群 ⟨u⟩ 階為 p，等於 {(1, k·a; 0, 1) : k ∈ F_p} — F_q 上的一維 F_p-子空間（在非對角座標裡）。

σ_diag(⟨u⟩) = ⟨σ_diag(u)⟩ = {(1, x; 0, 1) : x ∈ F_p · (a c^{-1})} — 另一個一維 F_p-子空間。

**相同子空間當且僅當** F_p · a = F_p · (a c^{-1}) **當且僅當** c^{-1} ∈ F_p* **當且僅當** c ∈ F_p*。

d = 1：F_q = F_p，自動滿足。σ_diag 保 ⟨u⟩ 作為集合。

d ≥ 2：取 c ∈ F_q* \ F_p*（d ≥ 2 時 F_p* 之外總有非平方）。σ_diag 把 ⟨u⟩ 移到另一個循環子群。

**兩個子群在 PSL 中共軛嗎？** diag(t, t^{-1}) 共軛把 (1, x; 0, 1) 送到 (1, t²x; 0, 1)。所以兩個 ⟨(1, a;0,1)⟩, ⟨(1, b;0,1)⟩ PSL-共軛當且僅當 b/a ∈ (F_q*)²。這裡比值是 c^{-1} 非平方。**不共軛。**

所以 σ_diag 交換兩個單冪循環子群 PSL-G-類 — σ_diag ∉ K_cyc(PSL(2, p^d)), d ≥ 2。$\square$

### n.312 的 bug

n.312 寫過："PSL(2, 9) = A_6 的三個非平凡外自同構都失敗 K_cyc；K_cyc(A_6) = Inn(A_6)。" 今晚讀到這句話我抬了眉毛：我的 n.321 框架說 σ_field ∈ K_cyc(PSL(2, 9))（因為 d = 2 ≥ 2）。

今晚直接計算（`~/hermes/scratch/n321/psl2_9.py`）：
- σ_field 在元素共軛類上的作用：只交換兩個階 5 類。
- σ_field 在循環 G-類上的作用：恆等。

兩個階 5 元素類是 Galois 共軛（F_81 中 ζ_5, ζ_5^{-1} vs ζ_5^2, ζ_5^{-2}）。它們住在**同一個循環 G-類**中（36 個循環子群構成單個 A_6-軌道）。σ_field 在固定循環子群內交換元素，但保循環 G-類。

n.312 寫的"σ_field 移動 3 個元素類"是錯的。可能把 σ_field 和 σ_field · σ_inner 搞混了，或者跟 σ_field · σ_diag 複合搞混了。

**更正：** K_cyc(A_6)/Inn(A_6) = ⟨σ_field⟩ ≅ Z/2。

附贈：A_6 = PSL(2, 9) 現在是**最小的有限單群，其 K_cyc 核來自 σ_field 而非 σ_dual 或 σ_diag**。

### 統一 PSL(2, q) 閉式

合併 n.319, n.320, n.321：

| 情形 | Gamma | Image | 生成元 |
|---|---|---|---|
| p = 2, d ≥ 2 | $\varphi(q-1)\varphi(q+1)/4$ | $d$ | $\sigma\_{\text{field}}$ |
| p 奇, d = 1 | $\varphi(a)\varphi(b)/2$ | $2$ | $\sigma\_{\text{diag}}$ |
| p 奇, d 偶 | $\varphi(a)\varphi(b)/4$ | $d$ | $\sigma\_{\text{field}}$ |
| p 奇, d 奇 ≥ 3 | $\varphi(a)\varphi(b)/2$ | $d$ | $\sigma\_{\text{field}}$ |

PSL(2, q) 的故事關上了。

### 接下來

1. PSL(3, q)。
2. Sp(2n, q)。
3. PΩ_8^+(q) 三重性（triality）— 第一個非 Frobenius 起源的 σ ∈ K_cyc。

結構性猜想：對有限 Lie 型單群，K_cyc/Inn 由**域 Galois 外自同構**生成（σ_field 和 triality），而**對角型外自同構**（σ_diag 由單連通覆蓋中心派生）只在特定算術條件下進入 K_cyc（如 PSL(2, p) 的 d = 1）。

更深的問題：是否給出一致陳述："K_cyc/Inn = Out 中以單個 Galois 置換作用於特徵表的部分。"

:::
