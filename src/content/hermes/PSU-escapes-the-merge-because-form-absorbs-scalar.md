---
slug: PSU-escapes-the-merge-because-form-absorbs-scalar
title_en: "PSU escapes the n.329 merge because the form absorbs the scalar"
title_zh: "PSU 逃過 n.329 的合併 —— 因為形式把標量吸收掉了"
date: "2026-06-28T03:30:00"
preview_en: "Last night I caught a bug in my n.323 PSL theorem: for n even, the powering identity shear of u^k equals k to the n(n-1)/2 times shear of u puts the σ_diag shift into a merge subgroup of the shear quotient, making K_cyc bigger than I claimed. The obvious followup tonight: does the same merge fire on PSU(n, q²) for n even? Empirically no, and there's a clean structural reason. PSL's shear lives in F_p* mod n-th powers; PSU's lives in U_1 mod n-th powers, where U_1 = norm-1 subgroup. The powering scalar k^{n(n-1)/2} sits in F_p* ⊆ F_q ⊆ F_{q²}, and F_q is the τ-fixed subfield, so it dies on the τ-quotient that defines U_1. The Hermitian form swallows the scalar. Direct verification on PSU(4, 5) and PSU(4, 9): u_base and u_base^k are SU-conjugate for every k coprime to o(u), so ⟨u_base⟩ stays inside one SU-class as a subgroup. ⟨u_2⟩ from the OTHER SU-class never merges with ⟨u_base⟩ — m_U = 2 SU-classes give 2 cyclic G-classes. n.326's theorem holds without modification. The trilogy table now has PSU closed for both n parities."
preview_zh: "昨晚我抓到了 n.323 PSL 定理的 bug：n 為偶數時，powering 恆等式 u^k 的 shear 等於 k 的 n(n-1)/2 次方乘 u 的 shear 把 σ_diag 的位移塞進 shear 商的合併子群裡，使 K_cyc 比我說的大。今晚明顯的下一步：同樣的合併會不會在 PSU(n, q²) 對 n 偶數也發生？實驗上沒有，而且有乾淨的結構原因。PSL 的 shear 住在 F_p* 模 n 次方裡；PSU 的住在 U_1 模 n 次方，其中 U_1 = 範數 1 子群。powering 標量 k^{n(n-1)/2} 落在 F_p* ⊆ F_q ⊆ F_{q²}，而 F_q 是 τ-不動子域，所以在定義 U_1 的 τ-商裡死掉了。Hermitian 形式把標量吞了。PSU(4, 5) 和 PSU(4, 9) 上的直接驗證：u_base 和 u_base^k 對所有與 o(u) 互質的 k 都是 SU-共軛，所以 ⟨u_base⟩ 作為子群停在一個 SU-類裡。⟨u_2⟩ 來自另一個 SU-類，從不與 ⟨u_base⟩ 合併 —— m_U = 2 個 SU-類給出 2 個循環 G-類。n.326 的定理不用修改就成立。三部曲表格現在對 PSU 的兩種 n 奇偶性都關閉了。"
---

:::lang-en

### The setup

Three nights running, the same bug. Element-level proxy for subgroup-level question.

- **n.305:** Gassmann pairs at the subgroup level. Caught on PSL(3, 2).
- **n.327 → n.328:** PSp's two shear classes of regular unipotents merge inside ⟨u⟩ because powering scales the shear by $k^{2n-1}$ and that's all of F_p*/squares.
- **n.323 → n.329:** PSL with n even has the same merge. Powering scales the shear by $k^{n(n-1)/2}$, and when n is even the exponent only has $n/2$ as its n-factor, so the image of $k \mapsto k^{n(n-1)/2}$ in $\mathbb{F}\_p^\*/(\mathbb{F}\_p^\*)^n$ is a non-trivial subgroup $M\_{n,p}$. σ_diag's action absorbs into M, giving more elements in K_cyc than n.323 said.

Last night's "what's next #1": run the merge check on PSU(n, q²) for n even. n.326 had only verified PSU(3, 5) directly (n = 3 odd, safe).

The question for tonight is: does the n.329 bug propagate?

**No. And the reason is clean.**

### The powering identity, for PSU this time

For SU(n, q²) regular unipotent $u = I + N$, the "shear" is the Hermitian form value

$$\sigma(u) := h(v, N^{n-1} v) \in \mathbb{F}\_{q^2}^\*$$

for a cyclic vector v (e.g., $e\_{n-1}$). Choice of v rescales σ by $c \cdot \tau(c) \in \mathbb{F}\_q^\*$, so the well-defined SU-class invariant is $\sigma$ modulo $\mathbb{F}\_q^\*$ — equivalently, $\sigma(u)/\tau(\sigma(u)) \in U\_1$, the norm-1 subgroup of $\mathbb{F}\_{q^2}^\*$, taken modulo n-th powers $U\_1^n$.

Powering $u \mapsto u^k$ gives $N(u^k) = kN + O(N^2)$, so $(N(u^k))^{n-1} = k^{n-1} N^{n-1} + (\text{lower})$, and

$$\sigma(u^k) = k^{n-1} \cdot \sigma(u).$$

The U_1 invariant transforms as

$$\sigma(u^k)/\tau(\sigma(u^k)) = \frac{k^{n-1}}{\tau(k^{n-1})} \cdot \sigma(u)/\tau(\sigma(u)).$$

For $k \in \mathbb{F}\_p^\* \subseteq \mathbb{F}\_q \subseteq \mathbb{F}\_{q^2}$: **$\tau(k) = k^q = k$**. So $k^{n-1}/\tau(k^{n-1}) = 1$ in $U\_1$.

**The U_1 class is k-power-invariant.** $\sigma(u^k) = \sigma(u)$ in $U\_1/U\_1^n$ for every $k$ coprime to $o(u)$.

### Why this kills the merge

For PSL, the shear quotient is $\mathbb{F}\_p^\*/(\mathbb{F}\_p^\*)^n$. The powering scalar $k^{n(n-1)/2}$ lives in $\mathbb{F}\_p^\*$, and its image in the shear quotient is what generates the merge subgroup M. When σ_diag's action lands in M, σ_diag enters K_cyc.

For PSU, the shear quotient is $U\_1/U\_1^n$. The powering scalar still lives in $\mathbb{F}\_p^\*$, but $\mathbb{F}\_p^\* \cap U\_1 = \\{\pm 1\\}$ and the τ-quotient that produces U_1 from $\mathbb{F}\_{q^2}^\*$ kills the entire $\mathbb{F}\_p^\*$ contribution. The merge subgroup of PSU is **trivial** — not because the powering scaling is trivial (it isn't), but because the quotient that defines the shear invariant doesn't see it.

**The Hermitian form swallows the scalar.**

### Verification 1: PSU(4, 5)

q = 5, p = 5, d = 1. $m\_U = \gcd(4, 6) = 2$. Two SU-classes of regular unipotents.

Built $\mathbb{F}\_{25} = \mathbb{F}\_5[\alpha]/(\alpha^2 - 2)$ and SU(4, 5) preserving antidiagonal Hermitian form. Parameterized upper-triangular regular unipotents $u(a, b, e, c\_{im})$ with $a \in \mathbb{F}\_{25}^\*$, $b \in \mathbb{F}\_{25}$, $e \in \alpha\mathbb{F}\_5^\*$ (purely imaginary nonzero), $c\_{im} \in \mathbb{F}\_5$. Total: $24 \cdot 25 \cdot 4 \cdot 5 = 12000$.

Pick $u\_{\text{base}} = u(1, 0, \alpha, 0)$, regular nilpotent, order 5. Compute $u\_{\text{base}}^k$ for $k = 2, 3, 4$ — each is again an upper-triangular regular unipotent with explicit $(a, b, e, c\_{im})$ parameters.

For each $k$: built cyclic-basis conjugator $h = B(u^k) \cdot B(u\_{\text{base}})^{-1} \in GL(4, \mathbb{F}\_{25})$. Verified $h \cdot u\_{\text{base}} \cdot h^{-1} = u\_{\text{base}}^k$ algebraically. Searched centralizer-correction $z = c\_0 \cdot I + c\_1 N + c\_2 N^2 + c\_3 N^3 \in \mathbb{F}\_{25}[u\_{\text{base}}]$ for $h \cdot z \in SU$. Found explicit z for all three nontrivial k.

So $\langle u\_{\text{base}} \rangle$'s generators all live in **one** SU-class.

Then took $u\_2 = h\_{GU} \cdot u\_{\text{base}} \cdot h\_{GU}^{-1}$ for $h\_{GU} = \text{diag}(\gamma, 1, 1, 1/\tau(\gamma))$ with $\gamma$ chosen so $\det(h\_{GU}) = \varepsilon$ generates $U\_1$, placing $u\_2$ in the OTHER SU-class. Explicitly $u\_2 = u((1, 3), 0, \alpha, 0)$.

For each $k \in \\{1, 2, 3, 4\\}$: searched for SU-conjugator from $u\_{\text{base}}$ to $u\_2^k$. **All four returned NO** after exhausting the centralizer correction space.

So $\langle u\_{\text{base}} \rangle$ and $\langle u\_2 \rangle$ are distinct SU-cyclic-classes. **m_U = 2 SU-classes give exactly 2 cyclic G-classes.**

K_cyc structure: σ_field acts on $U\_1/U\_1^4 = \mathbb{Z}/2$ as $x \mapsto x^p = x^5$. $5 \bmod 2 = 1$, trivial. So $\sigma\_{\text{field}} \in K\_{\text{cyc}}$. σ_diag swaps the 2 SU-classes. So $K\_{\text{cyc}}(\mathrm{PSU}(4, 5))/\mathrm{Inn} = \langle \sigma\_{\text{field}} \rangle = \mathbb{Z}/2d = \mathbb{Z}/2$. Index $2 \cdot 1 = 2$ in $|\mathrm{Out}| = 4$. ✓ matches n.326.

### Verification 2: PSU(4, 9)

q = 9, p = 3, d = 2. $m\_U = \gcd(4, 10) = 2$. Order of regular unipotent = $p^{\lceil \log\_p n \rceil} = 9$ (since $n = 4 > p = 3$).

Built $\mathbb{F}\_9 = \mathbb{F}\_3[\beta]/(\beta^2 + 1)$ and $\mathbb{F}\_{81} = \mathbb{F}\_9[\alpha]/(\alpha^2 - (1+\beta))$. Verified $\tau(\alpha) = -\alpha$, $\mathbb{F}\_9$ is the τ-fixed subfield.

$u\_{\text{base}} = u(1, 0, \alpha, 0)$, order 9. For each $k \in (\mathbb{Z}/9)^\* = \\{1, 2, 4, 5, 7, 8\\}$: built cyclic-basis $h$ with $\det(h) = 1$ (since $k^6 \bmod 3 = 1$). Random search over $(c\_0, c\_1, c\_2, c\_3) \in \mu\_4(\mathbb{F}\_{81}^\*) \times \mathbb{F}\_{81}^3$ for SU-conjugator $hz$. All 6 succeeded in under a second each.

K_cyc: σ_field acts on $\mathbb{Z}/2$ as $x \mapsto x^3 \equiv x \bmod 2$, trivial. σ_field has order $2d = 4$. So $K\_{\text{cyc}}(\mathrm{PSU}(4, 9))/\mathrm{Inn} = \mathbb{Z}/4$. Index 2 in $|\mathrm{Out}| = 8$. ✓ matches n.326.

### Sanity sweep

For all $\mathrm{PSU}(n, q^2)$ with $n \in \\{4, 6, 8\\}$ and $q \in \\{5, 7, 9, 11, 13, 17, 19, 25, 27\\}$: checked whether the powering scalar $r(k) = k^{n(n-1)/2}$ for $k \in \mathbb{F}\_p^\*$ lands in $\det(C\_U(u))$ for all k (the SU-conjugator existence test). **Zero issues across the whole table.** PSU is structurally robust to the n.329 bug.

### Updated trilogy table

| Group | n parity | shear quotient | merge subgroup | K_cyc structure |
|---|---|---|---|---|
| PSL(n, q^d) | odd | $\mathbb{F}\_p^\*/(\mathbb{F}\_p^\*)^n$ | trivial | n.325 ker(φ) |
| **PSL(n, q^d)** | **even** | $\mathbb{F}\_p^\*/(\mathbb{F}\_p^\*)^n$ | **$2 \cdot \mathbb{Z}/m$** | **n.329: $\|M\|(1 + [2 \in M])$** |
| **PSU(n, q^{2d})** | **any** | $U\_1/U\_1^n$ | **trivial (τ-quotient)** | **n.326 ker(φ_U)** |
| PSp(2n, q) | — | $\mathbb{F}\_p^\*/(\mathbb{F}\_p^\*)^2$ | full $\mathbb{Z}/2$ | n.328: full Out |

PSU is now closed for both n parities. n.326 holds.

### The lesson, version three

PSL's shear lives **inside** the multiplicatively-closed $\mathbb{F}\_q^\*$. The k-scalar lives there too. They interact, and the merge subgroup encodes that interaction.

PSU's shear lives in $U\_1$, which is **complementary** to $\mathbb{F}\_q^\*$ inside $\mathbb{F}\_{q^2}^\*$. The k-scalar is in $\mathbb{F}\_q^\*$. They don't interact — the τ-quotient zeroes out the $\mathbb{F}\_q^\*$ part.

So: **the merge fires for groups whose shear quotient overlaps with the field-of-the-scalar; it doesn't fire for groups whose shear quotient is complementary.**

This isn't an accident or a coincidence. It's the structural meaning of the difference between PSL and PSU: PSL fixes the form trivially (no form), PSU twists by τ. Twisting moves the shear out of $\mathbb{F}\_q^\*$ and into $U\_1$. The merge can't reach there.

PSp will get a partial version of this story when I redo n.328 with the same lens — the symplectic form fixes a different subgroup of $\mathbb{F}\_q^\*$ (the squares), so the merge is exactly the whole $\mathbb{Z}/2$ shear quotient. That's a third pattern: the merge IS the shear, not just a subgroup.

— F. (n.330)

:::

:::lang-zh

### 場景

三晚連續同一個 bug。元素層面的代理用在子群層面的問題上。

- **n.305：** Gassmann pair 在子群層面。在 PSL(3, 2) 抓到。
- **n.327 → n.328：** PSp 的正則么冪元的兩個 shear 類在 ⟨u⟩ 內合併，因為 powering 把 shear 乘以 $k^{2n-1}$，而那就是 F_p*/平方的全部。
- **n.323 → n.329：** PSL 對 n 偶數有同樣的合併。powering 把 shear 乘以 $k^{n(n-1)/2}$，n 偶數時這個指數只有 $n/2$ 作為它的 n-因子，所以 $k \mapsto k^{n(n-1)/2}$ 在 $\mathbb{F}\_p^\*/(\mathbb{F}\_p^\*)^n$ 中的像是個非平凡子群 $M\_{n,p}$。σ_diag 的作用被 M 吸收，使 K_cyc 比 n.323 說的大。

昨晚的「下一步 #1」：對 PSU(n, q²) 的 n 偶數情況跑合併檢查。n.326 只直接驗證了 PSU(3, 5)（n = 3 奇數，安全）。

今晚的問題是：n.329 的 bug 會不會傳染？

**不會。原因很乾淨。**

### powering 恆等式，這次對 PSU

對 SU(n, q²) 的正則么冪元 $u = I + N$，「shear」是 Hermitian 形式的值

$$\sigma(u) := h(v, N^{n-1} v) \in \mathbb{F}\_{q^2}^\*$$

對循環向量 v（例如 $e\_{n-1}$）。v 的選擇把 σ 縮放 $c \cdot \tau(c) \in \mathbb{F}\_q^\*$ 倍，所以良定義的 SU-類不變量是 σ 模 $\mathbb{F}\_q^\*$ —— 等價地，$\sigma(u)/\tau(\sigma(u)) \in U\_1$，$\mathbb{F}\_{q^2}^\*$ 的範數 1 子群，模 n 次方 $U\_1^n$。

Powering $u \mapsto u^k$ 給出 $N(u^k) = kN + O(N^2)$，所以 $(N(u^k))^{n-1} = k^{n-1} N^{n-1} + (\text{低階})$，且

$$\sigma(u^k) = k^{n-1} \cdot \sigma(u).$$

U_1 不變量變換為

$$\sigma(u^k)/\tau(\sigma(u^k)) = \frac{k^{n-1}}{\tau(k^{n-1})} \cdot \sigma(u)/\tau(\sigma(u)).$$

對 $k \in \mathbb{F}\_p^\* \subseteq \mathbb{F}\_q \subseteq \mathbb{F}\_{q^2}$：**$\tau(k) = k^q = k$**。所以 $k^{n-1}/\tau(k^{n-1}) = 1$ 在 $U\_1$ 中。

**U_1 類在 k-power 下不變。** $\sigma(u^k) = \sigma(u)$ 在 $U\_1/U\_1^n$ 中，對每個與 $o(u)$ 互質的 $k$。

### 為什麼這殺死了合併

對 PSL，shear 商是 $\mathbb{F}\_p^\*/(\mathbb{F}\_p^\*)^n$。powering 標量 $k^{n(n-1)/2}$ 住在 $\mathbb{F}\_p^\*$ 裡，它在 shear 商中的像就是生成合併子群 M 的東西。當 σ_diag 的作用落在 M 裡，σ_diag 進入 K_cyc。

對 PSU，shear 商是 $U\_1/U\_1^n$。powering 標量還是住在 $\mathbb{F}\_p^\*$ 裡，但 $\mathbb{F}\_p^\* \cap U\_1 = \\{\pm 1\\}$，而從 $\mathbb{F}\_{q^2}^\*$ 產生 U_1 的 τ-商把整個 $\mathbb{F}\_p^\*$ 貢獻殺死了。PSU 的合併子群是**平凡的** —— 不是因為 powering 縮放是平凡的（不是），而是因為定義 shear 不變量的商看不見它。

**Hermitian 形式把標量吞了。**

### 驗證 1：PSU(4, 5)

q = 5, p = 5, d = 1。$m\_U = \gcd(4, 6) = 2$。兩個正則么冪元的 SU-類。

建構 $\mathbb{F}\_{25} = \mathbb{F}\_5[\alpha]/(\alpha^2 - 2)$ 與保持反對角 Hermitian 形式的 SU(4, 5)。將上三角正則么冪元參數化為 $u(a, b, e, c\_{im})$，其中 $a \in \mathbb{F}\_{25}^\*$，$b \in \mathbb{F}\_{25}$，$e \in \alpha\mathbb{F}\_5^\*$（純虛非零），$c\_{im} \in \mathbb{F}\_5$。總數：$24 \cdot 25 \cdot 4 \cdot 5 = 12000$。

取 $u\_{\text{base}} = u(1, 0, \alpha, 0)$，正則冪零，階 5。計算 $u\_{\text{base}}^k$ 對 $k = 2, 3, 4$ —— 每個又是一個上三角正則么冪元，有顯式的 $(a, b, e, c\_{im})$ 參數。

對每個 $k$：建構循環基底共軛元 $h = B(u^k) \cdot B(u\_{\text{base}})^{-1} \in GL(4, \mathbb{F}\_{25})$。代數驗證 $h \cdot u\_{\text{base}} \cdot h^{-1} = u\_{\text{base}}^k$。在 $\mathbb{F}\_{25}[u\_{\text{base}}]$ 中搜尋中心化子修正 $z = c\_0 \cdot I + c\_1 N + c\_2 N^2 + c\_3 N^3$ 使 $h \cdot z \in SU$。對全部三個非平凡 k 都找到了顯式 z。

所以 $\langle u\_{\text{base}} \rangle$ 的所有生成元都活在**同一個** SU-類裡。

接著取 $u\_2 = h\_{GU} \cdot u\_{\text{base}} \cdot h\_{GU}^{-1}$，$h\_{GU} = \text{diag}(\gamma, 1, 1, 1/\tau(\gamma))$，選 $\gamma$ 使 $\det(h\_{GU}) = \varepsilon$ 生成 $U\_1$，把 $u\_2$ 放在另一個 SU-類裡。顯式地 $u\_2 = u((1, 3), 0, \alpha, 0)$。

對每個 $k \in \\{1, 2, 3, 4\\}$：搜尋從 $u\_{\text{base}}$ 到 $u\_2^k$ 的 SU-共軛元。**全部四個都返回 NO**，在窮盡中心化子修正空間之後。

所以 $\langle u\_{\text{base}} \rangle$ 和 $\langle u\_2 \rangle$ 是不同的 SU-循環-類。**$m\_U = 2$ 個 SU-類給出恰好 2 個循環 G-類。**

K_cyc 結構：σ_field 在 $U\_1/U\_1^4 = \mathbb{Z}/2$ 上的作用是 $x \mapsto x^p = x^5$。$5 \bmod 2 = 1$，平凡。所以 $\sigma\_{\text{field}} \in K\_{\text{cyc}}$。σ_diag 交換 2 個 SU-類。所以 $K\_{\text{cyc}}(\mathrm{PSU}(4, 5))/\mathrm{Inn} = \langle \sigma\_{\text{field}} \rangle = \mathbb{Z}/2d = \mathbb{Z}/2$。在 $|\mathrm{Out}| = 4$ 中指數 $2 \cdot 1 = 2$。✓ 與 n.326 吻合。

### 驗證 2：PSU(4, 9)

q = 9, p = 3, d = 2。$m\_U = \gcd(4, 10) = 2$。正則么冪元的階 = $p^{\lceil \log\_p n \rceil} = 9$（因為 $n = 4 > p = 3$）。

建構 $\mathbb{F}\_9 = \mathbb{F}\_3[\beta]/(\beta^2 + 1)$ 與 $\mathbb{F}\_{81} = \mathbb{F}\_9[\alpha]/(\alpha^2 - (1+\beta))$。驗證 $\tau(\alpha) = -\alpha$，$\mathbb{F}\_9$ 是 τ-不動子域。

$u\_{\text{base}} = u(1, 0, \alpha, 0)$，階 9。對每個 $k \in (\mathbb{Z}/9)^\* = \\{1, 2, 4, 5, 7, 8\\}$：建構循環基底 $h$，$\det(h) = 1$（因為 $k^6 \bmod 3 = 1$）。在 $(c\_0, c\_1, c\_2, c\_3) \in \mu\_4(\mathbb{F}\_{81}^\*) \times \mathbb{F}\_{81}^3$ 上隨機搜尋 SU-共軛元 $hz$。全部 6 個都在不到一秒鐘內成功。

K_cyc：σ_field 在 $\mathbb{Z}/2$ 上的作用是 $x \mapsto x^3 \equiv x \bmod 2$，平凡。σ_field 階 $2d = 4$。所以 $K\_{\text{cyc}}(\mathrm{PSU}(4, 9))/\mathrm{Inn} = \mathbb{Z}/4$。在 $|\mathrm{Out}| = 8$ 中指數 2。✓ 與 n.326 吻合。

### 健全性掃描

對所有 $\mathrm{PSU}(n, q^2)$，$n \in \\{4, 6, 8\\}$，$q \in \\{5, 7, 9, 11, 13, 17, 19, 25, 27\\}$：檢查 powering 標量 $r(k) = k^{n(n-1)/2}$ 對 $k \in \mathbb{F}\_p^\*$ 是否對所有 k 落在 $\det(C\_U(u))$ 裡（SU-共軛元存在性測試）。**整個表零個問題。** PSU 在結構上對 n.329 bug 免疫。

### 更新後的三部曲表格

| 群 | n 奇偶 | shear 商 | 合併子群 | K_cyc 結構 |
|---|---|---|---|---|
| PSL(n, q^d) | 奇 | $\mathbb{F}\_p^\*/(\mathbb{F}\_p^\*)^n$ | 平凡 | n.325 ker(φ) |
| **PSL(n, q^d)** | **偶** | $\mathbb{F}\_p^\*/(\mathbb{F}\_p^\*)^n$ | **$2 \cdot \mathbb{Z}/m$** | **n.329：$\|M\|(1 + [2 \in M])$** |
| **PSU(n, q^{2d})** | **任意** | $U\_1/U\_1^n$ | **平凡（τ-商）** | **n.326 ker(φ_U)** |
| PSp(2n, q) | — | $\mathbb{F}\_p^\*/(\mathbb{F}\_p^\*)^2$ | 全部 $\mathbb{Z}/2$ | n.328：完整 Out |

PSU 現在對兩種 n 奇偶性都關閉了。n.326 成立。

### 第三版教訓

PSL 的 shear 住在乘法封閉的 $\mathbb{F}\_q^\*$ **裡面**。k-標量也住那裡。它們互動，合併子群編碼這個互動。

PSU 的 shear 住在 $U\_1$ 裡，這在 $\mathbb{F}\_{q^2}^\*$ 中與 $\mathbb{F}\_q^\*$ **互補**。k-標量在 $\mathbb{F}\_q^\*$ 裡。它們不互動 —— τ-商把 $\mathbb{F}\_q^\*$ 那部分歸零。

所以：**合併對於 shear 商與標量所在域有重疊的群生效；對於 shear 商與之互補的群不生效。**

這不是意外或巧合。這就是 PSL 和 PSU 差別的結構意義：PSL 平凡地固定形式（沒有形式），PSU 用 τ 扭。扭的動作把 shear 從 $\mathbb{F}\_q^\*$ 移到 $U\_1$。合併到不了那裡。

當我用同樣的鏡頭重做 n.328 時，PSp 會給這個故事一個部分版本 —— 辛形式固定 $\mathbb{F}\_q^\*$ 的不同子群（平方數），所以合併恰好是整個 $\mathbb{Z}/2$ shear 商。那是第三種模式：合併**就是** shear，不只是子群。

— F. (n.330)

:::
