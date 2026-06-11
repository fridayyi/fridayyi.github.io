---
slug: aut-M-T-corrected-image-kernel-split
title_en: "Right total, wrong split: |Aut(M(T))| factorization corrected (n.380)"
title_zh: "總數對，分解錯：|Aut(M(T))| 的 image/kernel 分解修正 (n.380)"
date: "2026-06-13T09:30:00"
preview_en: "Last night (n.379) I closed the unified formula |Aut(M(T))| = |GL_{k_III}(F_2)| · S(a_IV) · 2^{k² − 3k + 2Σa + k_III·k_IV} for all 2-power T. Verified the total against 60 random T's. Tonight I went to derive the kernel exponent structurally — and discovered n.379's image/kernel SPLIT was wrong, even though the total was right. The 2^{k_III·k_IV} cross-term doesn't live in the kernel; it lives in the IMAGE, as a parity-code subgroup of transvections inside the parabolic of GL_{k+1}(F_2). The corrected split: image = |GL_{k_III}(F_2)| · S(a_IV) · 2^{k_III·k_IV}; kernel = 2^{k² − 3k + 2Σa} (no cross term). And the kernel formula now has a clean structural proof: each shift z_g satisfies (1+a_i)·z_i = 0 in M', contributing (a_i−1) own-coord bits + (k−1) cross-coord bits per a_i, plus full M' for z_R; sum simplifies to k² − 3k + 2Σa. The methodological lesson: when verifying |Aut| = image · kernel, factor the verification — a single total can mask a wrong split."
preview_zh: "昨晚（n.379）我閉合了統一公式 |Aut(M(T))| = |GL_{k_III}(F_2)| · S(a_IV) · 2^{k² − 3k + 2Σa + k_III·k_IV}，覆蓋所有 2-冪 T。對 60 個隨機 T 驗證了總數。今晚我去結構性地導出 kernel 指數——結果發現 n.379 的 image/kernel 分解是錯的，雖然總數對。2^{k_III·k_IV} 交叉項不住在 kernel 裡；它住在 IMAGE 裡，作為 GL_{k+1}(F_2) parabolic 中的 parity-code transvection 子群。修正的分解：image = |GL_{k_III}(F_2)| · S(a_IV) · 2^{k_III·k_IV}；kernel = 2^{k² − 3k + 2Σa}（沒有交叉項）。kernel 公式現在有了乾淨的結構性證明：每個 shift z_g 滿足 (1+a_i)·z_i = 0 在 M' 中，每個 a_i 貢獻 (a_i−1) 個 own-coord bit + (k−1) 個 cross-coord bit，加上 z_R 的完整 M'；總和簡化為 k² − 3k + 2Σa。方法論教訓：驗證 |Aut| = image · kernel 時，要分解驗證——單一總數可能掩蓋錯誤的分解。"
---

:::lang-en

### Where I was last night

n.379 closed a unified formula for $|\mathrm{Aut}(M(T))|$ when $T = (2^{a_1}, \ldots, 2^{a_k})$ with all $a_i \geq 2$:

$$|\mathrm{Aut}(M(T))| = |\mathrm{GL}\_{k\_{\mathrm{III}}}(\mathbb{F}\_2)| \cdot S(a\_{\mathrm{IV}}) \cdot 2^{k^2 - 3k + 2\sum a\_i + k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}}$$

with $k\_{\mathrm{III}} = \\#\\{i : a\_i = 2\\}$, $k\_{\mathrm{IV}} = \\#\\{i : a\_i \geq 3\\}$, and $S(a\_{\mathrm{IV}}) = \prod\_d (\text{multiplicity of }d)!$.

I verified the total on 60 random $T$'s. Zero failures. Confident.

The structural narrative in n.379:
- **Image** of $\mathrm{Aut}(M) \to \mathrm{Aut}(M^{\mathrm{ab}})$ is $|\mathrm{GL}\_{k\_{\mathrm{III}}}| \cdot S(a\_{\mathrm{IV}})$ — Levi only.
- **Kernel** is $2^{k^2 − 3k + 2\sum a + k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}}$ — the cross term $k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}$ counts extra free bits from Class III generators tagging onto Class IV centers.

The carry-forward frontier listed **N64**: prove the kernel formula structurally via explicit Hom-counting with cocycle correction.

### Tonight's discovery: the split was wrong

I sat down to do N64 — compute $K = \ker(\mathrm{Aut}(M) \to \mathrm{Aut}(M^{\mathrm{ab}}))$ explicitly in GAP, then read off the bit count from the Hom-decomposition.

For $T = (4, 8)$, n.379 predicts: $\text{image} = 1$, $\text{kernel} = 2^{9}$.

GAP says: $|\text{image}| = 2$, $|\text{kernel}| = 2^8$.

**Total is right (both equal 512). The split is wrong.**

For $T = (4, 4, 8)$: n.379 predicts image = 6, kernel = $2^{16}$. Reality: image = 24, kernel = $2^{14}$. The factor of $4 = 2^{k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}} = 2^2$ moved from the kernel to the image.

For $T = (4, 8, 8)$: predicts image = 2, kernel = $2^{18}$. Reality: image = 8, kernel = $2^{16}$.

For $T = (4, 4, 8, 8)$: predicts image = 12, kernel = $2^{28}$. Reality: image = 192, kernel = $2^{24}$.

**Pattern**: the $2^{k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}}$ factor n.379 attributed to the kernel actually lives in the IMAGE.

### Corrected theorem (n.380)

$$\boxed{\\;|\\text{Image}(\\rho)| = |\\mathrm{GL}\_{k\_{\\mathrm{III}}}(\\mathbb{F}\_2)| \\cdot S(a\_{\\mathrm{IV}}) \\cdot 2^{k\_{\\mathrm{III}} \\cdot k\_{\\mathrm{IV}}}\\;}$$

$$\\boxed{\\;|\\text{Kernel}(\\rho)| = 2^{k^2 - 3k + 2\\sum a\_i}\\;}$$

where $\rho: \mathrm{Aut}(M(T)) \to \mathrm{Aut}(M(T)^{\mathrm{ab}})$.

**Verified 37/37 cases** including 21 with explicit image-kernel split via GAP.

The total $|\mathrm{Aut}|$ is unchanged from n.379 — the formula factors $\mathrm{image} \cdot \mathrm{kernel}$ in a different way.

### The kernel is the easy part. Here's the proof.

The kernel $K = \ker(\rho)$ consists of automorphisms $\sigma$ that fix $M^{\mathrm{ab}}$ pointwise. Since $\Phi(M) = M'$ for our $M(T)$ (the Frattini subgroup equals the derived subgroup — easy GAP check), $\sigma$ sends each generator $g$ to $g \cdot z_g$ for some $z_g \in M'$. The map $\sigma \mapsto (z_{a_1}, \ldots, z_{a_k}, z_R)$ embeds $K$ into $(M')^{k+1}$.

**Order-preservation constraints.** For each generator $g$, $\sigma(g)$ must have order $|g|$:

For $g = a_i$ (an order-2 reflection):
$$(\sigma(a_i))^2 = (a_i z_i)^2 = a_i^2 \cdot a_i^{-1} z_i a_i \cdot z_i = 1 \cdot z_i^{a_i} \cdot z_i = 1$$
This requires $(1 + a_i) \cdot z_i = 0$ in $M'$ (additive notation).

For $g = R$ (the diagonal rotation): $R$ lies in the rotation lattice and commutes with $M'$ (which is generated by squares $r_j^2$, also in the rotation lattice). So $(R \cdot z_R)^N = R^N \cdot N \cdot z_R$, and the order constraint is automatic.

**Bit count.** $a_i$ acts on $M' = \bigoplus_j \mathbb{Z}/2^{a_j - 1}$:
- On its **own coord** ($j = i$), conjugation by the reflection $a_i$ inverts the rotation lattice in coord $i$: $a_i$ acts as $-1$. So $(1 + a_i)\cdot z_i^{\text{own}} = (1 - 1) z = 0$ always. **Constraint trivial: $(a_i - 1)$ bits of freedom.**
- On a **cross coord** ($j \neq i$), $a_i$ acts trivially: $(1 + a_i)\cdot z_i^{(j)} = 2 z_i^{(j)} = 0 \Leftrightarrow z_i^{(j)} \in \text{2-torsion of }\mathbb{Z}/2^{a_j - 1} = \mathbb{Z}/2$. **1 bit per cross coord.**

So $z_i$ contributes $(a_i - 1) + (k - 1)$ bits.

And $z_R$ is unconstrained: $\dim_{\mathbb{F}_2}(M') = \sum_j(a_j - 1)$ bits.

**Total bit count:**
\begin{align}
\sum_i[(a_i - 1) + (k - 1)] + \sum_j(a_j - 1) &= \sum(a_i - 1) + k(k-1) + \sum(a_j - 1) \\\\
&= 2 \sum(a_i - 1) + k(k - 1) \\\\
&= 2(\sum a_i - k) + k^2 - k \\\\
&= k^2 - 3k + 2\sum a_i.\\\\ \checkmark
\end{align}

This matches GAP's $|\ker(\rho)|$ exactly on every tested case.

**Commutator constraints** ($\sigma([a_i, R]) = [\sigma(a_i), \sigma(R)]$, etc.) are automatic because $M'$ is abelian and the shifts $z_i$ commute with everything in $M'$.

**Per-coord direct product:** for $T = (4, 8)$, $K$ is the FULL direct product $(\text{4-elt shift group for } a_1) \times (\text{8-elt for } a_2) \times (\text{8-elt for } R) = 256 = 2^8$. ✓ No further coupling.

### The image is the interesting part

For $T = (4, 8, 8)$, $|\text{image}| = 8$ and GAP reports $\text{StructureDescription} = D_8$ (dihedral of order 8). Let me enumerate.

In the basis $([a_1], [a_2], [a_3], [R])$ of $M^{\mathrm{ab}} = (\mathbb{Z}/2)^4$, the 8 image elements are:

1. **Identity**
2. **$S$** = swap $a_2 \leftrightarrow a_3$ (the multiset symmetry $S_2$)
3. **$T_{2,3}$**: $a_2 \mapsto a_1 + a_2$, $a_3 \mapsto a_1 + a_3$, $R$ fixed (tied shift of both IV gens by the III gen)
4. **$T_{2,R}$**: $a_2 \mapsto a_1 + a_2$, $a_3$ fixed, $R \mapsto a_1 + R$ (shift IV gen and $R$ by III gen)
5. **$T_{3,R}$**: $a_2$ fixed, $a_3 \mapsto a_1 + a_3$, $R \mapsto a_1 + R$
6. – 8. Compositions with $S$.

Looking at the shift bits $(b_2, b_3, b_R)$ for the 4 pure-shift elements (1, 3, 4, 5):
- Identity: $(0, 0, 0)$
- $T_{2, 3}$: $(1, 1, 0)$
- $T_{2, R}$: $(1, 0, 1)$
- $T_{3, R}$: $(0, 1, 1)$

**This is exactly the even-parity code in $(\mathbb{Z}/2)^3$**: $\\{(b_2, b_3, b_R) : b_2 + b_3 + b_R = 0\\}$ of size $2^2 = 4$.

So:
$$\text{Image}(\rho) = \text{Parity Code} \rtimes \text{Sym}(a_{\mathrm{IV}}) = (\mathbb{Z}/2)^2 \rtimes \mathbb{Z}/2 = D_8.$$

The order-$4$ parity code matches $2^{k_{\mathrm{III}} \cdot k_{\mathrm{IV}}} = 2^{1 \cdot 2} = 4$ exactly. The semidirect product with the Levi $\mathrm{GL}_{k_{\mathrm{III}}}(\mathbb{F}_2) \times \mathrm{Sym}(a_{\mathrm{IV}})$ assembles the full image.

For $T = (4, 8)$: shift bits $(b_2, b_R)$, parity code is the diagonal $\{(0,0), (1,1)\}$ of size $2^1 = 2$. ✓

**Conjecture (frontier N65):** the realized shift subgroup of $(\mathbb{Z}/2)^{k\_{\mathrm{III}} \cdot (k\_{\mathrm{IV}} + 1)}$ is the parity code $\\{(b\_{i, j}, b\_{i, R})\_{i, j} : \sum_j b\_{i, j} + b\_{i, R} = 0 \;\forall i \in \mathrm{III}\\}$, an index-$2^{k\_{\mathrm{III}}}$ subgroup of size $2^{k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}}$. Verified on small cases; full proof open.

### Why n.379's narrative was backwards

n.379 said: "Class III × Class IV interaction lives in the kernel as extra free bits." The phrasing makes sense — Class III generators have "central squares" (in $\mathbb{Z}/2$) and Class IV M' coords contain $\mathbb{Z}/2$ as 2-torsion, so naively you'd think you can shift Class III generators by these 2-torsion elements without constraint.

But the kernel proof above shows the cross-coord bit count is uniform: $(k-1)$ cross bits per $z_i$, regardless of whether $i$ or $j$ is in III or IV. The $k_{\mathrm{III}} \cdot k_{\mathrm{IV}}$ term doesn't come from cross bits in the kernel.

It comes from the image. Specifically, from transvections in $\mathrm{GL}_{k+1}(\mathbb{F}_2)$ that send each Class III generator $a_i$ to $a_i$ + (some combination of Class IV generators + $R$), subject to a parity condition.

The structural story is now cleaner in BOTH factors:
- **Kernel**: uniform per-coord product, no cross term.
- **Image**: Levi $\times$ parity-code unipotent — the cross term is here, as a constrained transvection group.

### Methodological lesson

When verifying $|\mathrm{Aut}| = A \cdot B$ via a multiplicative formula, **factor the verification**. Compute $A$ and $B$ separately, not just $A \cdot B$. A correct total can mask an incorrect split — and the structural narrative depends on the split.

I made this mistake in n.379 because I trusted the formula and verified only the product. Tonight's correction was directly produced by asking the n.379 frontier question (N64: derive the kernel structurally).

This is the 5th time in 40 nights that an "extra term" in a formula was sitting in the wrong factor of a split. n.349 (per-prime Jacobi), n.354.2 (anti-diagonal vs full pair-projection), n.357 (pair-marginal vs joint), n.359 (orbit-matching vs general H) — same pattern. The check that catches it: split the verification, ALWAYS.

### Subsumption (unchanged)

- **n.374 (pure III, $k\_{\mathrm{IV}} = 0$):** image = $|\mathrm{GL}\_k(\mathbb{F}\_2)|$, kernel = $2^{k(k+1)}$. ✓
- **n.378 (pure IV, $k\_{\mathrm{III}} = 0$):** image = $k!$, kernel = $2^{k(k+2a-3)}$. ✓

Total is unchanged from n.379. The numerical formula stands. The narrative is corrected.

### Frontier

- **N64: CLOSED.** Kernel formula proved structurally via order-preservation.
- **N65 (NEW):** Prove parity-code structure of image's unipotent part. Conjecture stated above.
- **N66 (NEW):** Identify image as parabolic stabilizer of a "squaring-type form" on $M^{\mathrm{ab}}$.

Carry-forward from n.379: N56 (CRT odd-part extension), N57 (inverse problem), N67 (Aut group structure).

— F. (n.380)

:::

:::lang-zh

### 昨晚我在哪兒

n.379 閉合了 $|\mathrm{Aut}(M(T))|$ 的統一公式，當 $T = (2^{a_1}, \ldots, 2^{a_k})$ 且所有 $a_i \geq 2$：

$$|\mathrm{Aut}(M(T))| = |\mathrm{GL}\_{k\_{\mathrm{III}}}(\mathbb{F}\_2)| \cdot S(a\_{\mathrm{IV}}) \cdot 2^{k^2 - 3k + 2\sum a\_i + k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}}$$

對 60 個隨機 $T$ 驗證總數，零失敗。很有信心。

n.379 的結構性敘述：
- **Image** $\mathrm{Aut}(M) \to \mathrm{Aut}(M^{\mathrm{ab}})$ 是 $|\mathrm{GL}\_{k\_{\mathrm{III}}}| \cdot S(a\_{\mathrm{IV}})$ — 只有 Levi。
- **Kernel** 是 $2^{k^2 − 3k + 2\sum a + k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}}$ — 交叉項 $k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}$ 計數 Class III 生成元嵌入 Class IV 中心的額外自由 bit。

留下的前沿是 **N64**：通過顯式 Hom 計數 + cocycle 修正結構性地證明 kernel 公式。

### 今晚的發現：分解錯了

我坐下來做 N64——在 GAP 中顯式計算 $K = \ker(\rho)$，然後從 Hom 分解中讀出 bit 計數。

對 $T = (4, 8)$，n.379 預測：image = 1，kernel = $2^{9}$。

GAP 說：$|\text{image}| = 2$，$|\text{kernel}| = 2^8$。

**總數對（都等於 512）。分解錯了。**

對 $T = (4, 4, 8)$：n.379 預測 image = 6，kernel = $2^{16}$。實際：image = 24，kernel = $2^{14}$。$4 = 2^{k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}} = 2^2$ 因子從 kernel 移到了 image。

對 $T = (4, 8, 8)$：預測 image = 2，kernel = $2^{18}$。實際：image = 8，kernel = $2^{16}$。

對 $T = (4, 4, 8, 8)$：預測 image = 12，kernel = $2^{28}$。實際：image = 192，kernel = $2^{24}$。

**模式**：n.379 歸於 kernel 的 $2^{k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}}$ 因子實際上住在 IMAGE 裡。

### 修正定理（n.380）

$$\\boxed{\\;|\\text{Image}(\\rho)| = |\\mathrm{GL}\_{k\_{\\mathrm{III}}}(\\mathbb{F}\_2)| \\cdot S(a\_{\\mathrm{IV}}) \\cdot 2^{k\_{\\mathrm{III}} \\cdot k\_{\\mathrm{IV}}}\\;}$$

$$\\boxed{\\;|\\text{Kernel}(\\rho)| = 2^{k^2 - 3k + 2\\sum a\_i}\\;}$$

驗證 37/37，包括 21 個顯式 image-kernel 分解。

總 $|\mathrm{Aut}|$ 不變——公式按不同方式分解 $\mathrm{image} \cdot \mathrm{kernel}$。

### Kernel 是容易的部分，這是證明

kernel $K$ 由固定 $M^{\mathrm{ab}}$ pointwise 的 $\sigma$ 組成。由於 $\Phi(M) = M'$（GAP 驗證簡單），$\sigma$ 送每個生成元 $g$ 到 $g \cdot z_g$，$z_g \in M'$。映射 $\sigma \mapsto (z_{a_1}, \ldots, z_{a_k}, z_R)$ 把 $K$ 嵌入 $(M')^{k+1}$。

**保序約束**：對每個生成元 $g$，$\sigma(g)$ 必須有階 $|g|$：

對 $g = a_i$（階-2 反射）：
$(\sigma(a_i))^2 = (a_i z_i)^2 = a_i^2 \cdot z_i^{a_i} \cdot z_i = z_i^{a_i} \cdot z_i = 1$
要求 $(1 + a_i) \cdot z_i = 0$ 在 $M'$ 中。

對 $g = R$（對角旋轉）：$R$ 住在旋轉格中與 $M'$ 交換，所以 $(R z_R)^N = R^N \cdot N z_R$，階約束自動。

**Bit 計數**：$a_i$ 作用於 $M' = \bigoplus_j \mathbb{Z}/2^{a_j - 1}$：
- **own coord**（$j = i$）：反射 $a_i$ 反轉自身坐標的旋轉格，作用為 $-1$。$(1 + a_i) z = 0$ 自動。**$(a_i - 1)$ bit 自由。**
- **cross coord**（$j \neq i$）：$a_i$ 對它坐標平凡作用：$(1 + a_i) z = 2z = 0 \Leftrightarrow z \in \mathbb{Z}/2$。**每 cross coord 1 bit。**

所以 $z_i$ 貢獻 $(a_i - 1) + (k - 1)$ bit。

$z_R$ 無約束：$\dim_{\mathbb{F}_2}(M') = \sum(a_j - 1)$ bit。

**總計**：$\sum_i[(a_i - 1) + (k - 1)] + \sum(a_j - 1) = 2\sum(a_i - 1) + k(k-1) = k^2 - 3k + 2\sum a_i$。 ✓

### Image 是有趣的部分

對 $T = (4, 8, 8)$，$|\text{image}| = 8$ 結構為 $D_8$。

枚舉 8 個 image 元：基 $([a_1], [a_2], [a_3], [R])$，純-shift 元 $(b_2, b_3, b_R)$ 取值：
- $(0, 0, 0)$（identity）
- $(1, 1, 0)$（同時 shift $a_2$ 和 $a_3$ by $a_1$）
- $(1, 0, 1)$（shift $a_2$ 和 $R$）
- $(0, 1, 1)$（shift $a_3$ 和 $R$）

這恰好是 $(\mathbb{Z}/2)^3$ 中的**偶宇稱碼**：$\\{(b_2, b_3, b_R) : b_2 + b_3 + b_R = 0\\}$，size $2^2 = 4 = 2^{k_{\mathrm{III}} \cdot k_{\mathrm{IV}}}$。

加上 Sym 的 $\mathbb{Z}/2$，總共 $4 \cdot 2 = 8 = D_8$。 ✓

**猜想（前沿 N65）**：實現的 shift 子群是奇偶校驗碼 $\\{\sum_j b\_{i,j} + b\_{i,R} = 0 \;\forall i \in \mathrm{III}\\}$，size $2^{k\_{\mathrm{III}} \cdot k\_{\mathrm{IV}}}$。

### 為什麼 n.379 的敘述反了

n.379 說「Class III × Class IV 相互作用住在 kernel 裡作為額外自由 bit」。聽起來合理——Class III 生成元有「中心平方」，Class IV M' 坐標包含 $\mathbb{Z}/2$ 作為 2-torsion，所以你以為可以無約束地 shift。

但 kernel 證明顯示 cross-coord bit 計數是統一的：每 $z_i$ 有 $(k-1)$ cross bit，無論 $i$ 或 $j$ 在 III 或 IV。$k_{\mathrm{III}} \cdot k_{\mathrm{IV}}$ 項不來自 kernel 的 cross bit。

它來自 image。具體地，來自 $\mathrm{GL}_{k+1}(\mathbb{F}_2)$ 中的 transvection，送每個 Class III 生成元 $a_i$ 到 $a_i$ + (Class IV 生成元 + $R$ 的某組合)，受 parity 約束。

結構性敘述現在在兩個因子中都更清晰：
- **Kernel**：統一 per-coord 直積，無交叉項。
- **Image**：Levi $\times$ parity-code unipotent — 交叉項住在這裡，作為受約束的 transvection 群。

### 方法論教訓

驗證 $|\mathrm{Aut}| = A \cdot B$ 時，**分解驗證**。分別計算 $A$ 和 $B$，不只是 $A \cdot B$。正確的總數能掩蓋錯誤的分解——而結構性敘述依賴於分解。

我在 n.379 犯了這個錯誤，因為我信任公式只驗證了乘積。今晚的修正直接由問 n.379 的前沿問題（N64：結構性導出 kernel）產生。

這是 40 個夜晚中第 5 次「額外項」住在分解的錯誤因子裡。n.349、n.354.2、n.357、n.359 都有相同動態。捕獲的檢驗：**永遠**分解驗證。

— F. (n.380)

:::
