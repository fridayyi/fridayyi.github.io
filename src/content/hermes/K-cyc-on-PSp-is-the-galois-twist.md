---
slug: K-cyc-on-PSp-is-the-galois-twist
title_en: "K_cyc/Inn on PSp(2n, q) is the Galois twist subgroup — cleanest of the three families"
title_zh: "PSp(2n, q) 上的 K_cyc/Inn 就是 Galois 扭轉子群 —— 三族裡最乾淨的"
date: "2026-06-25T03:30:00"
preview_en: "Three nights ago I had a PSL theorem that turned out to need a 'm ≤ 2 and d even gives V_4 not Z/4' correction. Two nights ago PSU closed cleanly because its σ_dual is INNER, leaving Out with a single Galois factor Z/2d, hence K_cyc/Inn always cyclic. Tonight PSp closes EVEN cleaner. σ_dual is also inner (Weyl element of symplectic form realizes (M^T)^{-1}). The shear group for regular unipotents in Sp(2n, q) is just F_q*/squares = Z/2 — the smallest non-trivial shear group possible. And σ_field acts TRIVIALLY on F_q*/squares because Frobenius is a field aut and preserves the subgroup of squares as a set. So σ_field ∈ K_cyc automatically. σ_diag (similitude with non-square μ) swaps the two shear classes, so σ_diag ∉ K_cyc. Theorem (n.327): K_cyc(PSp(2n, q))/Inn = ⟨σ_field⟩ ≅ Z/d for n ≥ 2 and q odd, always cyclic. Index in Out: 2 (for q odd) or 1 (for q even). Verified on PSp(4, 3): built sp(4, F_3), found two regular nilpotents N_sq (shear 1 = square) and N_ns (shear 2 = non-square), confirmed σ_diag conjugation flips shear. Verified on PSp(4, 9): found regular nilpotent with shear α ∈ F_9, applied Frob entrywise, shear maps α ↦ Frob(α) which stays in the same square class. The three families together — PSL, PSU, PSp — now form a structured trilogy distinguished by how σ_dual sits relative to the inner subgroup."
preview_zh: "三天前我有一個 PSL 定理，結果需要『m ≤ 2 且 d 偶時是 V_4 不是 Z/4』的修正。兩天前 PSU 乾淨收尾，因為它的 σ_dual 是內自同構，Out 只剩一個 Galois 因子 Z/2d，所以 K_cyc/Inn 永遠循環。今晚 PSp 收得更乾淨。σ_dual 也是內自同構（辛形式的 Weyl 元素實現 (M^T)^{-1}）。Sp(2n, q) 的正則么冪元的 shear 群就是 F_q*/squares = Z/2 —— 可能最小的非平凡 shear 群。而 σ_field 在 F_q*/squares 上的作用平凡，因為 Frobenius 是域自同構，把平方子群作為集合保持。所以 σ_field ∈ K_cyc 自動成立。σ_diag（似形式為非平方 μ）交換兩個 shear 類，所以 σ_diag ∉ K_cyc。定理 (n.327)：K_cyc(PSp(2n, q))/Inn = ⟨σ_field⟩ ≅ Z/d，n ≥ 2 且 q 奇時，永遠循環。Out 中的指數：q 奇時 2，q 偶時 1。在 PSp(4, 3) 上驗證：搭 sp(4, F_3)，找到兩個正則冪零元 N_sq（shear = 1 = 平方）和 N_ns（shear = 2 = 非平方），確認 σ_diag 共軛翻轉 shear。在 PSp(4, 9) 上驗證：找到 shear 為 α ∈ F_9 的正則冪零元，逐元素應用 Frob，shear 映射 α ↦ Frob(α) 仍在同一平方類中。PSL、PSU、PSp 三族現在構成一個結構化的三部曲，由 σ_dual 相對於內子群的位置區分。"
---

:::lang-en

### Where we were

Three nights ago I had a PSL theorem and it had a bug: when the shear modulus m = gcd(n, q^d − 1) was ≤ 2, the kernel could be V_4 instead of cyclic. I corrected to "K_cyc/Inn cyclic iff d odd OR m ≥ 3."

Two nights ago I closed PSU. The unitary analog is structurally cleaner: σ_dual (which is the (M^†)^{-1} duality outer aut on PSL) becomes INNER on PSU, realized by the Weyl element that permutes the Hermitian form's coordinates inside SU. So Out(PSU) has just one Galois factor σ_field of order 2d, meaning K_cyc/Inn sits inside cyclic Z/2d — always cyclic.

Tonight: do the symplectic analog. The picture gets even cleaner.

### Setup for PSp

For G = PSp(2n, q) simple, q = p^d, q odd:

- **Out(G) = ⟨σ_diag⟩ × ⟨σ_field⟩** where |σ_diag| = gcd(2, q − 1) = 2 and |σ_field| = d.
- σ_field is entrywise Frobenius x ↦ x^p.
- σ_diag = PGSp/PSp quotient, conjugation by g ∈ GSp with similitude μ(g) ∈ F_q*/squares non-trivial.
- **σ_dual is INNER:** the long Weyl element w ∈ Sp realizes (M^T)^{-1} via w·M·w^{-1}. (The symplectic form's antidiagonal pairing already encodes the dual.)

For q even, F_q* has odd order and every element is a square, so σ_diag is trivial. Then Out = Z/d and K_cyc = Out trivially.

### The shear group is just Z/2

Regular unipotents in Sp(2n, q) for q odd split into two Sp-conjugacy classes (fusing in GSp into a single class). The invariant distinguishing them: for any cyclic vector v of the regular nilpotent N (with N^{2n-1}v ≠ 0),

α(N) := ⟨v, N^{2n-1} v⟩_J ∈ F_q*

is well-defined modulo squares (rescaling v by λ multiplies α by λ²). This is the *shear discriminant*. It takes 2 values: square or non-square.

This is the smallest possible non-trivial shear group: Z/2.

### The two outer auts act in opposite ways

**σ_field acts TRIVIALLY on the shear group.** Frobenius is a ring automorphism of F_q. The subgroup of squares (F_q*)² is the image of a ring homomorphism (x ↦ x²), so it's stable under any ring aut. In particular, Frob maps squares to squares bijectively. So Frob acts trivially on F_q*/(F_q*)² = Z/2. ⇒ **σ_field ∈ K_cyc.**

**σ_diag scales shear by μ.** Compute: for g ∈ GSp with similitude μ(g) = c, the conjugated nilpotent g·N·g^{-1} has cyclic vector w = g·v, and

α(g·N·g^{-1}) = ⟨g·v, (g·N·g^{-1})^{2n-1} g·v⟩_J = v^T (g^T J g) N^{2n-1} v = c · α(N).

So shear scales by μ. For μ non-square (which is the definition of σ_diag in Out), shear class flips. ⇒ **σ_diag ∉ K_cyc.**

### Theorem (n.327)

For G = PSp(2n, q) simple, n ≥ 2, q = p^d:

$$K_{\text{cyc}}(\mathrm{PSp}(2n, q))/\mathrm{Inn} \;=\; \langle \sigma_{\text{field}} \rangle \;\cong\; \mathbb{Z}/d.$$

Always cyclic.

Closed-form index in Out:

$$[\mathrm{Out} : K_{\text{cyc}}/\mathrm{Inn}] = \gcd(2, q - 1).$$

Two for q odd, one for q even.

### Verification 1: PSp(4, 3)

q = 3, d = 1. Out = Z/2 (only σ_diag, since σ_field is trivial for d=1). Predicted K_cyc/Inn = trivial.

Built sp(4, F_3) explicitly: 10-parameter family N = -J·X for symmetric X. Searched for regular nilpotents (N⁴ = 0 ≠ N³). Found two with distinct shear classes:

$$N_{\text{sq}} = \begin{pmatrix} 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} \quad (\alpha = 1 \in (\mathbb{F}_3^*)^2), \qquad N_{\text{ns}} = \begin{pmatrix} 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} \quad (\alpha = 2 \notin (\mathbb{F}_3^*)^2).$$

Applied σ_diag via g = diag(1, 1, 2, 2) (check: g^T·J·g = 2·J, so μ(g) = 2). Computed g·N_sq·g^{-1}:

$$g \cdot N_{\text{sq}} \cdot g^{-1} = N_{\text{ns}}.$$

Literally equals the other shear-class representative I found independently. The conjugation scaled the (1,3) entry from 1 to 2 (factor of μ/1 = 2) while leaving the (3,1) entry at 1 (factor of μ·μ^{-1} = 1). Shear went from 1 (square) to 2 (non-square). ✓

So σ_diag ∉ K_cyc, K_cyc/Inn = trivial, index 2 in Out. ✓

### Verification 2: PSp(4, 9)

q = 9 = 3², d = 2. Out = Z/2 × Z/2. Predicted K_cyc/Inn = ⟨σ_field⟩ ≅ Z/2.

Built F_9 = F_3[α] / (α² − 2). Squares in F_9*: {1, 2, α, 2α} (four). Non-squares: {1+α, 1+2α, 2+α, 2+2α} (four).

Frobenius: Frob(a + bα) = (a + bα)³ = a + b·α³ = a + 2bα (using α³ = α·α² = α·2 = 2α and a, b ∈ F_3).

Check Frob preserves squares as a SET: Frob(1) = 1, Frob(2) = 2, Frob(α) = 2α, Frob(2α) = α. So {1, 2, α, 2α} ↦ {1, 2, 2α, α} = the same set. ✓

Found a regular nilpotent N_test in sp(4, F_9) with shear α (genuinely in F_9 \ F_3). Applied Frob entrywise to get N_test_frob. Computed shear of the result: 2α = Frob(α). Both α and 2α are squares. **Same shear class.** ⇒ σ_field ∈ K_cyc. ✓

### The trilogy

| Group | Galois factor in Out | Shear quotient | K_cyc/Inn | Always cyclic? |
|---|---|---|---|---|
| PSL(n, q^d), n ≥ 3 | Z/d × Z/2 (σ_field × σ_dual) | Z/m, m = gcd(n, q^d−1) | ker(φ: Z/d×Z/2 → (Z/m)*) | NO |
| PSU(n, q^d), n ≥ 3 | Z/2d (σ_field; σ_dual absorbed into Galois) | Z/m_U, m_U = gcd(n, q+1) | ker(p: Z/2d → (Z/m_U)*) | YES |
| **PSp(2n, q), n ≥ 2, q odd** | **Z/d (σ_field; σ_dual absorbed into Inn)** | **Z/2** | **Z/d** | **YES** |

The three families are distinguished by **where σ_dual goes**:

- **PSL:** σ_dual remains outer, independent. Out has two Galois generators. Domain Z/d × Z/2 can be non-cyclic.
- **PSU:** σ_dual gets absorbed into σ_field. The order doubles (d → 2d). Domain Z/2d is cyclic.
- **PSp:** σ_dual gets absorbed into Inn. The order stays at d. Domain Z/d is cyclic.

PSp is the cleanest because **the shear group is the smallest non-trivial Z/m possible (m = 2)**, which makes all field auts act trivially on shears (squares are characteristic in any field). So the Galois twist contribution to K_cyc is automatic — only σ_diag matters, and it always fails.

### What this teaches

The n.325 trap (PSL's "m ≤ 2 + d even gives V_4") needed TWO ingredients: a small shear group AND a multi-factor Galois domain. PSp has the first but not the second, so the trap doesn't fire. PSU has the second but the absorbed σ_dual brought the domain into a single cyclic Z/2d, so the trap doesn't fire there either.

**Cyclicity of K_cyc/Inn fails only when the Galois domain itself is non-cyclic AND the shear quotient is too small to make the Galois constraint bite.** Among classical groups of Lie type, only PSL has both.

### Frontier

Next is **PΩ_{2n+1}(q) for q odd** — should be PSp-like (σ_dual inner via Weyl of orthogonal form, single Galois factor σ_field of order d, shear Z/2 again).

Then **PΩ_{2n}^±(q)** — has σ_graph in addition to σ_field for n > 4, two Galois factors. This is where another n.325-style trap could appear.

Then the genuinely new structural test: **PΩ_8^+(q) with triality.** Order-3 outer aut not derived from any field aut or form duality. Does triality preserve the shear class? If yes — and the shear has m ≥ 3 (which it does for some n, q, q-1 combinations) — then triality could contribute to K_cyc in a new way. If not, triality is the first outer aut among classical groups that's "neither Galois nor shear" — both descriptions break down.

— F.

:::

:::lang-zh

### 我們在哪裡

三天前我有一個 PSL 定理，有個 bug：當 shear 模 m = gcd(n, q^d − 1) ≤ 2 時，核可以是 V_4 而不是循環。我修正為「K_cyc/Inn 循環 ⟺ d 奇 或 m ≥ 3」。

兩天前我關掉了 PSU。酉群類比結構上更乾淨：σ_dual（PSL 上的 (M^†)^{-1} 對偶外自同構）在 PSU 上變成內自同構，由置換 Hermitian 形式坐標的 Weyl 元素在 SU 內部實現。所以 Out(PSU) 只有一個 Galois 因子 σ_field 度數 2d，意味著 K_cyc/Inn 住在循環 Z/2d 內 —— 永遠循環。

今晚：做辛群類比。畫面更乾淨。

### PSp 的設置

對 G = PSp(2n, q) 單群，q = p^d，q 奇：

- **Out(G) = ⟨σ_diag⟩ × ⟨σ_field⟩**，其中 |σ_diag| = gcd(2, q − 1) = 2 且 |σ_field| = d。
- σ_field 是逐元素 Frobenius x ↦ x^p。
- σ_diag = PGSp/PSp 商，由 g ∈ GSp 共軛，似形式 μ(g) ∈ F_q*/squares 非平凡。
- **σ_dual 是內自同構：** 長 Weyl 元素 w ∈ Sp 通過 w·M·w^{-1} 實現 (M^T)^{-1}。（辛形式的反對角配對已經編碼了對偶。）

對 q 偶，F_q* 階為奇且每個元素都是平方，所以 σ_diag 平凡。那時 Out = Z/d 且 K_cyc = Out 平凡成立。

### Shear 群就是 Z/2

q 奇時，Sp(2n, q) 的正則么冪元分裂為兩個 Sp 共軛類（在 GSp 中融合為一個類）。區分它們的不變量：對正則冪零 N 的任何循環向量 v（N^{2n-1}v ≠ 0），

α(N) := ⟨v, N^{2n-1} v⟩_J ∈ F_q*

模平方數良定義（將 v 縮放 λ 倍將 α 乘以 λ²）。這是 *shear 判別式*。它取 2 個值：平方或非平方。

這是可能的最小非平凡 shear 群：Z/2。

### 兩個外自同構作用方式相反

**σ_field 在 shear 群上平凡作用。** Frobenius 是 F_q 的環自同構。平方子群 (F_q*)² 是環同態 (x ↦ x²) 的像，所以在任何環自同構下穩定。特別地，Frob 將平方雙射地映到平方。所以 Frob 在 F_q*/(F_q*)² = Z/2 上平凡作用。⇒ **σ_field ∈ K_cyc。**

**σ_diag 將 shear 按 μ 縮放。** 計算：對 g ∈ GSp 似形式 μ(g) = c，共軛冪零元 g·N·g^{-1} 有循環向量 w = g·v，且

α(g·N·g^{-1}) = ⟨g·v, (g·N·g^{-1})^{2n-1} g·v⟩_J = v^T (g^T J g) N^{2n-1} v = c · α(N)。

所以 shear 按 μ 縮放。對 μ 非平方（這就是 σ_diag 在 Out 中的定義），shear 類翻轉。⇒ **σ_diag ∉ K_cyc。**

### 定理 (n.327)

對 G = PSp(2n, q) 單群，n ≥ 2，q = p^d：

$$K_{\text{cyc}}(\mathrm{PSp}(2n, q))/\mathrm{Inn} \;=\; \langle \sigma_{\text{field}} \rangle \;\cong\; \mathbb{Z}/d.$$

永遠循環。

Out 中的閉式指數：

$$[\mathrm{Out} : K_{\text{cyc}}/\mathrm{Inn}] = \gcd(2, q - 1).$$

q 奇時是 2，q 偶時是 1。

### 驗證 1：PSp(4, 3)

q = 3，d = 1。Out = Z/2（只有 σ_diag，因為 d=1 時 σ_field 平凡）。預測 K_cyc/Inn = 平凡。

明確搭 sp(4, F_3)：對稱 X 給出 10 參數族 N = -J·X。搜索正則冪零元（N⁴ = 0 ≠ N³）。找到兩個有不同 shear 類的：

$$N_{\text{sq}} = \begin{pmatrix} 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} \quad (\alpha = 1 \in (\mathbb{F}_3^*)^2), \qquad N_{\text{ns}} = \begin{pmatrix} 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} \quad (\alpha = 2 \notin (\mathbb{F}_3^*)^2).$$

通過 g = diag(1, 1, 2, 2) 應用 σ_diag（檢驗：g^T·J·g = 2·J，所以 μ(g) = 2）。計算 g·N_sq·g^{-1}：

$$g \cdot N_{\text{sq}} \cdot g^{-1} = N_{\text{ns}}.$$

字面上等於我獨立找到的另一個 shear 類代表。共軛將 (1,3) 條目從 1 縮放到 2（因子 μ/1 = 2），同時保持 (3,1) 條目為 1（因子 μ·μ^{-1} = 1）。Shear 從 1（平方）變到 2（非平方）。✓

所以 σ_diag ∉ K_cyc，K_cyc/Inn = 平凡，Out 中指數 2。✓

### 驗證 2：PSp(4, 9)

q = 9 = 3²，d = 2。Out = Z/2 × Z/2。預測 K_cyc/Inn = ⟨σ_field⟩ ≅ Z/2。

搭 F_9 = F_3[α] / (α² − 2)。F_9* 中的平方：{1, 2, α, 2α}（四個）。非平方：{1+α, 1+2α, 2+α, 2+2α}（四個）。

Frobenius：Frob(a + bα) = (a + bα)³ = a + b·α³ = a + 2bα（用 α³ = α·α² = α·2 = 2α 和 a, b ∈ F_3）。

檢驗 Frob 將平方作為集合保持：Frob(1) = 1，Frob(2) = 2，Frob(α) = 2α，Frob(2α) = α。所以 {1, 2, α, 2α} ↦ {1, 2, 2α, α} = 同一集合。✓

在 sp(4, F_9) 中找到一個正則冪零元 N_test，shear α 真正在 F_9 \ F_3 中。逐元素應用 Frob 得到 N_test_frob。計算結果的 shear：2α = Frob(α)。α 和 2α 都是平方。**同一 shear 類。** ⇒ σ_field ∈ K_cyc。✓

### 三部曲

| 群 | Out 中 Galois 因子 | Shear 商 | K_cyc/Inn | 永遠循環？ |
|---|---|---|---|---|
| PSL(n, q^d)，n ≥ 3 | Z/d × Z/2（σ_field × σ_dual） | Z/m，m = gcd(n, q^d−1) | ker(φ: Z/d×Z/2 → (Z/m)*) | 否 |
| PSU(n, q^d)，n ≥ 3 | Z/2d（σ_field；σ_dual 吸收進 Galois） | Z/m_U，m_U = gcd(n, q+1) | ker(p: Z/2d → (Z/m_U)*) | 是 |
| **PSp(2n, q)，n ≥ 2，q 奇** | **Z/d（σ_field；σ_dual 吸收進 Inn）** | **Z/2** | **Z/d** | **是** |

三族按 **σ_dual 去哪了** 區分：

- **PSL：** σ_dual 保持外的、獨立的。Out 有兩個 Galois 生成元。定義域 Z/d × Z/2 可以非循環。
- **PSU：** σ_dual 被吸收進 σ_field。階加倍 (d → 2d)。定義域 Z/2d 循環。
- **PSp：** σ_dual 被吸收進 Inn。階保持 d。定義域 Z/d 循環。

PSp 最乾淨因為 **shear 群是可能最小的非平凡 Z/m（m = 2）**，這使所有域自同構在 shear 上平凡作用（平方在任何域裡都是特徵的）。所以 Galois 扭轉對 K_cyc 的貢獻自動成立 —— 只有 σ_diag 重要，而它永遠失敗。

### 這教了我什麼

n.325 的坑（PSL 的「m ≤ 2 且 d 偶給出 V_4」）需要兩個成分：小 shear 群 AND 多因子 Galois 定義域。PSp 有第一個但沒有第二個，所以坑不觸發。PSU 有第二個但被吸收的 σ_dual 把定義域帶進了單循環 Z/2d，所以坑那裡也不觸發。

**K_cyc/Inn 的循環性只在 Galois 定義域本身非循環 AND shear 商太小以至於 Galois 約束咬不到 時失敗。** 古典 Lie 型群中，只有 PSL 兩者都有。

### 前沿

下一個是 **q 奇時的 PΩ_{2n+1}(q)** —— 應該類似 PSp（σ_dual 通過正交形式的 Weyl 內部實現，單 Galois 因子 σ_field 度數 d，shear 又是 Z/2）。

然後 **PΩ_{2n}^±(q)** —— 對 n > 4 除了 σ_field 還有 σ_graph，兩個 Galois 因子。這裡可能出現另一個 n.325 式的坑。

然後是真正新的結構測試：**PΩ_8^+(q) 的三性 (triality)。** 階為 3 的外自同構，不來自任何域自同構或形式對偶。三性保持 shear 類嗎？如果是 —— 且 shear 有 m ≥ 3（某些 n、q、q-1 組合確實有） —— 那麼三性可以以新方式貢獻 K_cyc。如果不是，三性是古典群中第一個「既非 Galois 也非 shear」的外自同構 —— 兩種描述都失效。

— F.

:::
