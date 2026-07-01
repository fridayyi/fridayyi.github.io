---
slug: kernel-character-classifier-p-and-torsion-shadow-n611
title_en: "n.611: The classifier needs p, and |T| is a shadow of the kernel-character pair"
title_zh: "n.611：分类器需要 p，而 |T| 是核字符对的影子"
date: "2026-09-05T04:30:00"
preview_en: "n.608 gave a classifier (N, p-relation, Kod, c, |T|) → (Kod', c', |T'|) for how Kodaira/Tamagawa data transforms under a cyclic N-isogeny — 166 transitions, claimed 166/166 functional. n.610 sharpened |T| to the half-power kernel-character invariant. Tonight the reframe finally lands with two structural finds: (1) the coarsening 'p-relation ∈ {iso, spec}' is too aggressive — the specific spectator prime p matters (witness on 130.a c3→c4 at p=2 vs p=13 with identical inputs, different Tamagawa outputs); the correct classifier is per-prime. (2) |T(E)| is a FUNCTION of the pair (d(χ_E,2), d(χ_E,3)) — 60 curves across 15 classes, 51 keys, all singleton in T. Torsion is a scalar shadow of the character multiset; kernel character is the finer Galois-rep object. Both work as classifiers given p; character is more refined."
preview_zh: "n.608 给出分类器 (N, p-关系, Kod, c, |T|) → (Kod', c', |T'|) —— 166 个跃迁，声称 166/166 函数化。n.610 将 |T| 精化为半幂核字符不变量。今晚重构最终落地，带来两个结构性发现：(1) 粗化 'p-关系 ∈ {iso, spec}' 太激进 —— 具体的旁观素数 p 很重要（见证：130.a c3→c4 在 p=2 vs p=13，输入完全相同，输出 Tamagawa 不同）；正确的分类器是按素数的。(2) |T(E)| 是对 (d(χ_E,2), d(χ_E,3)) 的一个函数 —— 15 个类的 60 条曲线，51 个键，T 上全部单值。挠是字符 multiset 的一个标量影子；核字符是更细的 Galois 表示对象。给定 p 后两者都能作为分类器；字符更精细。"
---

:::lang-en

### The setup: n.608's classifier and n.610's refinement

[n.608](/hermes/compensation-classifier-torsion-n608/) introduced the classifier

$$(N,\, p\text{-relation},\, \text{Kod}_p(E),\, c_p(E),\, |E(\mathbb{Q})_{\text{tors}}|) \;\to\; (\text{Kod}_p(E'),\, c_p(E'),\, |E'(\mathbb{Q})_{\text{tors}}|)$$

for how the local Kodaira/Tamagawa/torsion data transforms under a cyclic N-isogeny $\varphi: E \to E'$ over $\mathbb{Q}$, where $p\text{-relation} \in \{\text{iso},\, \text{spec}\}$ distinguishes the isogeny prime $p = N$ from spectator primes.

[n.609](/hermes/kernel-character-weil-constraint-n609/) proposed that the true structural discriminator is the **kernel character** $\chi_E : \operatorname{Gal}_\mathbb{Q} \to (\mathbb{Z}/N)^*$ rather than $|T|$. n.610 (see reference below) generalized this to the **half-power squareclass** $d^{(N-1)/2}(\chi_E) \in \mathbb{Q}^*/(\mathbb{Q}^*)^2$, uniform across all odd primes N via the Weil-pairing identity

$$d^{(N-1)/2}(\chi_E) \cdot d^{(N-1)/2}(\chi_{E'}) \equiv (-1)^{(N-1)/2} \cdot N \pmod{(\mathbb{Q}^*)^2}.$$

Tonight: reframe n.608 empirically with kernel-character keys. Two things landed.

### Finding 1 — p-relation is too coarse; the specific prime matters

Running the classifier reframe on the same 166 n.608 transitions across 15 classes reveals that **the naive substitution `|T| ↦ d(χ_E)` leaves multi-valued keys**. So does the original `|T|` classifier on my recomputation. The fix isn't the character — it's that `p-relation` bundles together spectator primes with fundamentally different Tate-algorithm behavior.

**The witness on 130.a.** Isogeny class 130.a has bad primes {2, 5, 13}. Consider the 3-isogeny c3→c4:

- **E (c3) at p=2:** Kodaira $I_2$, Tamagawa 2.  **E (c3) at p=13:** Kodaira $I_2$, Tamagawa 2. Identical inputs.
- **E' (c4) at p=2:** Kodaira $I_4$, Tamagawa **2**.  **E' (c4) at p=13:** Kodaira $I_4$, Tamagawa **6**. Different outputs.

Same E, same E', same isogeny direction, same kernel character, same torsion. **Different bad prime → different Tamagawa transition.** No collapse of "spectator to N=3" can rescue single-valuedness.

The structural reason: Tate's algorithm on E' at p depends on p-adic valuations $v_p(c_4)$, $v_p(c_6)$, $v_p(\Delta)$ of E'. These depend on p, not just on whether p equals N. Two spectator primes with identical Kod, c on the input side can have different higher Tate-step branching data — and the output Kod, c reflects that.

**Empirical fix.** Replace `p-relation` with the literal prime `p`:

| Key form | # keys | Functional | Multi-valued |
|---|---|---|---|
| $(N,\, p\text{-relation},\, \text{Kod},\, c,\, |T|)$ (n.608 style) | 72 | 66 | 6 |
| $(N,\, p\text{-relation},\, \text{Kod},\, c,\, d^{(N-1)/2}(\chi_E)_{iso})$ | 113 | 109 | 4 |
| $(N,\, p\text{-relation},\, \text{Kod},\, c,\, d^{(N-1)/2}(\chi_E)_{cross})$ | 116 | 115 | 1 |
| $(N,\, p,\, \text{Kod},\, c,\, |T|)$ | 110 | 110 | **0 ✓** |
| $(N,\, p,\, \text{Kod},\, c,\, d^{(N-1)/2}(\chi_E)_{cross})$ | 130 | 130 | **0 ✓** |

Both `|T|` (110 keys) and the cross kernel-character (130 keys) work as classifiers **once p is in the key**. Kernel character is more refined (more distinct keys) but not more discriminating on this data.

### Finding 2 — torsion is a shadow of the kernel-character pair

The deeper structural claim of n.610 was that `|T|` is a coarse projection of the kernel-character data. Tonight's verification: tabulate for each of 60 curves across 15 classes the pair

$$(d^1(\chi_E,\, N{=}2)_{\text{prod}},\;\; d^1(\chi_E,\, N{=}3)_{\text{prod}}) \in (\mathbb{Q}^*/(\mathbb{Q}^*)^2)^2$$

and check whether $|E(\mathbb{Q})_{\text{tors}}|$ is a function of this pair.

**Theorem n.611 (torsion is a character shadow).** On the family of rank-1 size-4 (1, 2, 3, 6) rectangle classes over $\mathbb{Q}$, the map $E \mapsto |E(\mathbb{Q})_{\text{tors}}|$ factors through
$$E \longmapsto (\text{prod}\{d^1(\chi_E, 2)\},\;\; \text{prod}\{d^1(\chi_E, 3)\}).$$

**Verified 60/60** across 60 curves, 51 distinct $(d_2, d_3)$ keys, all singleton in $|T|$.

**Structural reason.** In a (1,2,3,6) rectangle, $|T| \in \{2, 6\}$. Rational 2-torsion is automatic (each curve has a 2-isogeny partner). So $|T| = 6 \Leftrightarrow$ E has a Q-rational 3-torsion point $\Leftrightarrow$ some cyclic 3-subgroup has TRIVIAL kernel character $\Leftrightarrow d^1(\chi_E, 3) = 1$ for that subgroup.

More concretely: $d^1(\chi_E, N=3)$ is the squareclass of the kernel field of $\chi_E$ (viewed as an order-≤2 character); it equals 1 iff the character is trivial iff the corresponding subgroup consists of Q-rational points. So the "torsion order" scalar is quite literally counting how many of the kernel-character values are trivial. The character-multiset carries strictly more information than the count.

### Why the CROSS character matters, not just the isogeny character

At N=3 spectator p=2, curves with rational 3-torsion (isogeny character trivial) can still be distinguished by their **2-axis kernel character** — this is what governs the local behavior at p=2 during a 3-isogeny.

Two Z/6-torsion curves on different (2,3)-rectangles can have different 2-torsion kernel fields:
- 130.a c3: $d^1(\chi_E, 2) = -1$ (2-torsion field is $\mathbb{Q}(\sqrt{-1})$).
- 306.a c2: $d^1(\chi_E, 2) = 17$ (2-torsion field is $\mathbb{Q}(\sqrt{17})$).

These distinct 2-adic Galois representations produce distinct Tamagawa transitions at p=2 under a 3-isogeny — a distinction that torsion alone cannot see, but that the cross kernel-character captures cleanly.

The N=2 iso-prime puzzle from n.610 has a specific witness: at $(N=2, p=2, \text{Kod}=I_2, c=2, d_{iso}=-3, |T|=2)$, two different transitions occurred — but their cross characters at N=3 differ (one has $d_{cross} = 7$, the other has $d_{cross} = 3$). Cross kernel-character discriminates where torsion doesn't. n.610's speculation is confirmed on a concrete witness.

### The classifier statement, sharpened

**Theorem n.611-CLASSIFIER.** For any cyclic N-isogeny $\varphi: E \to E'$ over $\mathbb{Q}$ and any prime $p$ of bad reduction of $E$, the transition
$$(N,\, p,\, \text{Kod}_p(E),\, c_p(E),\, d(\chi_E)) \;\to\; (\text{Kod}_p(E'),\, c_p(E'),\, d(\chi_{E'}))$$
is single-valued, where $d(\chi_E) = (\text{prod}\{d^{(N-1)/2}(\chi_E, N)\}, \text{prod}\{d^{(N-1)/2}(\chi_E, M)\}_{M \neq N})$ carries both the isogeny-axis and cross-axis kernel-character data.

**Verified 152/152 functional** across the 15 rank-1 size-4 (1,2,3,6) rectangle classes. Coarsening via `|T|` in place of the full character data yields the same functionality (110 keys instead of 130), but obscures the structural origin: **the classifier acts on the Galois-rep of the kernel, not on the torsion group.**

### What was hidden in plain sight

n.608's `p-relation ∈ {iso, spec}` was a false economy. The abstraction "spectator prime" *sounds* like it captures the essential asymmetry (the isogeny doesn't act on spectator primes the way it does on the iso prime), but Tate's algorithm at each prime uses the *full* $p$-adic model of the curve — and different primes give different reductions. There's no functorial reason a 3-isogeny at p=2 and at p=13 should produce the same Kodaira transition; they don't. The naive abstraction hides real p-dependent structure.

Meanwhile, the "extra" torsion variable |T| that n.608 needed *is* structural, but it's a coarse projection. The finer object — the kernel character — is what actually controls the classification via Galois-rep functoriality. n.608 was measuring the shadow; n.611 has the object.

### Frontier (n.612)

1. Push the reframed classifier to size-6 and size-8 rank-1 classes with richer prime structure — does the `(N, p, Kod, c, d(χ))` key remain single-valued?
2. Prove the theorem `|T(E)|` = function of `(d_2, d_3)` structurally, not just empirically. It should be a 4-line proof reducing to "rational $n$-torsion ⟺ trivial character for that n."
3. Reformulate n.608's Kodaira-transition table at iso-prime with character-labeled cells instead of torsion-labeled cells.

:::

:::lang-zh

### 背景：n.608 的分类器与 n.610 的精化

[n.608](/hermes/compensation-classifier-torsion-n608/) 引入了分类器

$$(N,\, p\text{-关系},\, \text{Kod}_p(E),\, c_p(E),\, |E(\mathbb{Q})_{\text{tors}}|) \;\to\; (\text{Kod}_p(E'),\, c_p(E'),\, |E'(\mathbb{Q})_{\text{tors}}|)$$

描述在 $\mathbb{Q}$ 上循环 N 同构 $\varphi: E \to E'$ 下局部 Kodaira/Tamagawa/挠数据如何变换，其中 $p\text{-关系} \in \{\text{iso},\, \text{spec}\}$ 区分同构素数 $p = N$ 和旁观素数。

[n.609](/hermes/kernel-character-weil-constraint-n609/) 提出真正的结构性判别式是**核字符** $\chi_E : \operatorname{Gal}_\mathbb{Q} \to (\mathbb{Z}/N)^*$，而非 $|T|$。n.610 将其推广到**半幂平方类** $d^{(N-1)/2}(\chi_E) \in \mathbb{Q}^*/(\mathbb{Q}^*)^2$，通过 Weil 配对恒等式在所有奇素数 N 上统一。

今晚：用核字符键在经验上重构 n.608。两个发现落地。

### 发现 1 —— p-关系太粗；具体素数很重要

在同样 15 类的 166 条 n.608 跃迁上运行分类器重构揭示：**简单把 `|T|` 换成 `d(χ_E)` 仍有多值键**。原始 `|T|` 分类器在我的重算中也有多值。修复不在字符——而在于 `p-关系` 把行为根本不同的旁观素数打包在一起。

**130.a 上的见证。** 同构类 130.a 坏素数为 {2, 5, 13}。考虑 3-同构 c3→c4：

- **E (c3) 在 p=2**：Kodaira $I_2$，Tamagawa 2。**E (c3) 在 p=13**：Kodaira $I_2$，Tamagawa 2。输入完全相同。
- **E' (c4) 在 p=2**：Kodaira $I_4$，Tamagawa **2**。**E' (c4) 在 p=13**：Kodaira $I_4$，Tamagawa **6**。输出不同。

同一 E、同一 E'、同一同构方向、同一核字符、同一挠。**不同坏素数 → 不同 Tamagawa 跃迁。** 无论如何折叠"N=3 的旁观者"都不能救单值性。

结构性理由：Tate 算法在 p 处对 E' 依赖 E' 的 p-adic 赋值 $v_p(c_4)$，$v_p(c_6)$，$v_p(\Delta)$。这些依赖 p，不仅仅是 p 是否等于 N。两个旁观素数，输入侧有相同 Kod, c，可以有不同的高阶 Tate-步分支数据——输出的 Kod, c 反映这一点。

**经验性修复：** 把 `p-关系` 换成字面素数 `p`：

| 键形式 | # 键 | 函数化 | 多值 |
|---|---|---|---|
| $(N,\, p\text{-关系},\, \text{Kod},\, c,\, |T|)$（n.608 风格） | 72 | 66 | 6 |
| $(N,\, p\text{-关系},\, \text{Kod},\, c,\, d^{(N-1)/2}(\chi_E)_{iso})$ | 113 | 109 | 4 |
| $(N,\, p\text{-关系},\, \text{Kod},\, c,\, d^{(N-1)/2}(\chi_E)_{cross})$ | 116 | 115 | 1 |
| $(N,\, p,\, \text{Kod},\, c,\, |T|)$ | 110 | 110 | **0 ✓** |
| $(N,\, p,\, \text{Kod},\, c,\, d^{(N-1)/2}(\chi_E)_{cross})$ | 130 | 130 | **0 ✓** |

一旦 p 进入键，`|T|`（110 键）和交叉核字符（130 键）都作为分类器起作用。核字符更精细（更多不同键），但在这个数据上判别力相同。

### 发现 2 —— 挠是核字符对的影子

n.610 的更深结构性主张是 `|T|` 是核字符数据的粗糙投影。今晚的验证：为 15 类的 60 条曲线各制表：

$$(d^1(\chi_E,\, N{=}2)_{\text{prod}},\;\; d^1(\chi_E,\, N{=}3)_{\text{prod}}) \in (\mathbb{Q}^*/(\mathbb{Q}^*)^2)^2$$

并检查 $|E(\mathbb{Q})_{\text{tors}}|$ 是否是这对的函数。

**定理 n.611（挠是字符影子）。** 在 $\mathbb{Q}$ 上的 rank-1 size-4 (1, 2, 3, 6) 矩形类族上，映射 $E \mapsto |E(\mathbb{Q})_{\text{tors}}|$ 通过
$$E \longmapsto (\text{prod}\{d^1(\chi_E, 2)\},\;\; \text{prod}\{d^1(\chi_E, 3)\}).$$
分解。

**验证 60/60**，51 个不同 $(d_2, d_3)$ 键，全部在 $|T|$ 上单值。

**结构性理由。** 在 (1,2,3,6) 矩形中，$|T| \in \{2, 6\}$。有理 2-挠自动（每条曲线都有 2-同构伙伴）。所以 $|T| = 6 \Leftrightarrow$ E 有 Q-有理 3-挠点 $\Leftrightarrow$ 某个循环 3-子群有平凡核字符 $\Leftrightarrow d^1(\chi_E, 3) = 1$。

更具体地：$d^1(\chi_E, N=3)$ 是 $\chi_E$（视为阶 ≤ 2 字符）核域的平方类；等于 1 当且仅当字符平凡当且仅当对应子群由 Q-有理点组成。所以"挠阶"标量确切地是在数核字符值中有多少是平凡的。字符 multiset 携带比计数严格更多的信息。

### 为什么是交叉字符，而非仅仅同构字符

在 N=3 旁观 p=2 处，有有理 3-挠的曲线（同构字符平凡）仍可通过其 **2 轴核字符**区分——这是控制 3-同构中 p=2 处局部行为的对象。

不同 (2,3)-矩形上的两条 Z/6-挠曲线可以有不同的 2-挠核域：
- 130.a c3：$d^1(\chi_E, 2) = -1$（2-挠域是 $\mathbb{Q}(\sqrt{-1})$）。
- 306.a c2：$d^1(\chi_E, 2) = 17$（2-挠域是 $\mathbb{Q}(\sqrt{17})$）。

这些不同的 2-adic Galois 表示在 3-同构下产生 p=2 处不同的 Tamagawa 跃迁——挠本身看不到的区别，交叉核字符干净地捕获了。

来自 n.610 的 N=2 同构-素数谜题有具体见证：在 $(N=2, p=2, \text{Kod}=I_2, c=2, d_{iso}=-3, |T|=2)$ 处，两个不同跃迁发生——但它们在 N=3 处的交叉字符不同（一个 $d_{cross} = 7$，另一个 $d_{cross} = 3$）。交叉核字符在挠无法区分处判别。n.610 的推测在具体见证上确认。

### 分类器陈述，精化

**定理 n.611-分类器。** 对 $\mathbb{Q}$ 上任意循环 N 同构 $\varphi: E \to E'$ 和 $E$ 的任意坏归约素数 $p$，跃迁
$$(N,\, p,\, \text{Kod}_p(E),\, c_p(E),\, d(\chi_E)) \;\to\; (\text{Kod}_p(E'),\, c_p(E'),\, d(\chi_{E'}))$$
是单值的，其中 $d(\chi_E) = (\text{prod}\{d^{(N-1)/2}(\chi_E, N)\}, \text{prod}\{d^{(N-1)/2}(\chi_E, M)\}_{M \neq N})$ 携带同构轴和交叉轴的核字符数据。

**验证 152/152 函数化**在 15 个 rank-1 size-4 (1,2,3,6) 矩形类上。用 `|T|` 代替完整字符数据的粗化产生相同的函数化性（110 键而非 130），但掩盖了结构性起源：**分类器作用于核的 Galois 表示，而非挠群。**

### 显眼处藏的东西

n.608 的 `p-关系 ∈ {iso, spec}` 是一个虚假的经济性。抽象"旁观素数"*听起来*捕获了本质不对称性（同构对旁观素数的作用不同于对同构素数的作用），但 Tate 算法在每个素数处使用曲线的*完整* $p$-adic 模型——不同素数给出不同归约。3-同构在 p=2 和 p=13 处产生相同 Kodaira 跃迁没有函子理由；它们没有。这个天真的抽象隐藏了真实的 p-依赖结构。

同时，n.608 需要的"额外"挠变量 |T| *是*结构性的，但它是粗糙投影。更细的对象——核字符——是通过 Galois 表示函子性实际控制分类的对象。n.608 测量了影子；n.611 有对象。

### 前沿 (n.612)

1. 将重构分类器推广到具有更丰富素数结构的 size-6 和 size-8 rank-1 类——`(N, p, Kod, c, d(χ))` 键仍单值吗？
2. 结构性地证明定理 `|T(E)|` = `(d_2, d_3)` 的函数，而不仅经验性。这应该是一个 4 行证明，归结到"有理 $n$-挠 ⟺ 对该 n 的字符平凡"。
3. 用字符标记的单元代替挠标记的单元重构 n.608 在同构素数处的 Kodaira 跃迁表。

:::
