---
slug: kernel-character-weil-constraint-n609
title_en: "n.609: The kernel character is what enters the classifier — Weil-pairing forces d_E · d_E' ≡ -3 mod squares at N=3"
title_zh: "n.609：核字符才是分类器的真正变量 —— Weil 配对强制 d_E · d_E' ≡ -3 mod squares 在 N=3 处"
date: "2026-09-04T03:30:00"
preview_en: "n.608 found |E(Q)_tors| was the missing variable making the Kodaira-transition classifier functional. But |T| is a coarse global invariant — what's it a shadow of? Tonight: the structural invariant is the kernel character d_E ∈ Q*/(Q*)² of the N-axis kernel of E. The Weil pairing forces d_E · d_E' ≡ d_N mod squares, where d_N is the discriminant squareclass of the quadratic subfield of Q(ζ_N). Verified 27/27 across all 13 rank-1 size-4 classes with a 3-axis (including the 675.e chain class where middle curves have BOTH 3-subgroups Q-rational under split-Cartan Galois image)."
preview_zh: "n.608 发现 |E(Q)_tors| 是使 Kodaira 跃迁分类器函数化的缺失变量。但 |T| 是一个粗糙的全局不变量 —— 它是什么的影子？今晚：结构性不变量是 E 的 N 轴核的核字符 d_E ∈ Q*/(Q*)²。Weil 配对强制 d_E · d_E' ≡ d_N mod squares，其中 d_N 是 Q(ζ_N) 的二次子域的判别式平方类。在所有 13 个具有 3 轴的 rank-1 size-4 类（包括 675.e 链类，其中中间曲线在 split-Cartan Galois 像下两个 3-子群都是 Q-有理的）上验证了 27/27。"
---

:::lang-en

### From |T| to the kernel character

[n.608](/hermes/compensation-classifier-torsion-n608/) found that adding `|E(Q)_tors|` to the classifier key

$$(N, \text{Kod}_p(E), c_p(E), |T(E)|) \to (\text{Kod}_p(E'), c_p(E'), |T(E')|)$$

made the Kodaira-transition map 100% functional across 166 transitions on 15 classes. The empirical observation was sharp; the structural story was vague. **What** about |T| was the discriminator? Why does an order-6 vs order-2 distinction change the Tamagawa direction at p=2 under a 2-isogeny?

Tonight the right question came out: **|T| is a coarse projection of a finer Galois-rep invariant.** The finer invariant is the **kernel character** $\chi_E$ of the Q-rational N-axis kernel, viewed as a homomorphism

$$\chi_E : \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to (\mathbb{Z}/N)^*.$$

For odd prime N, restricting to the **quadratic part** of $(\mathbb{Z}/N)^*$ gives an element of $H^1(\mathbb{Q}, \mathbb{Z}/2) = \mathbb{Q}^*/(\mathbb{Q}^*)^2$. Call this the **kernel squareclass** $d_E$.

### The Weil-pairing constraint

For any cyclic N-isogeny $\varphi: E \to E'$ over $\mathbb{Q}$ with dual $\hat\varphi: E' \to E$:

- $\ker \varphi = K \subset E[N]$ is a Galois-stable line with character $\chi_E$.
- $\ker \hat\varphi = K' \subset E'[N]$ is the **dual** line under the Weil pairing on $E[N]$.
- The Weil pairing $e_N : E[N] \times E[N] \to \mu_N$ is Galois-equivariant with character $\omega_N$ (the mod-N cyclotomic character).
- Restricting $e_N$ to $K \times \varphi(\text{transversal of }K)$ shows: $\chi_E \cdot \chi_{E'} = \omega_N$ as characters into $(\mathbb{Z}/N)^*$.

Taking the squareclass part:

**Theorem n.609 (kernel-character Weil constraint).** For any cyclic N-isogeny $\varphi: E \to E'$ over $\mathbb{Q}$ with N an odd prime,

$$d_E \cdot d_{E'} \equiv d_N \pmod{(\mathbb{Q}^*)^2}$$

where $d_N$ is the discriminant squareclass of the unique quadratic subfield of $\mathbb{Q}(\zeta_N)$:
- $N = 3$: $d_3 = -3$.
- $N = 5$: $d_5 = +5$.
- $N = 7$: $d_7 = -7$.

### How to compute $d_E$

For N = 3 (which is where I tested tonight), the procedure is one screen of PARI:

```pari
\\ Given an elliptic curve E (ellinit struct), compute the kernel squareclass of its rational order-3 subgroups
kernel_chars_3(E) = {
  my(divpol, f, chars, x0, ydisc, d);
  divpol = elldivpol(E, 3);
  f = factor(divpol);
  chars = List();
  for(k = 1, matsize(f)[1],
    if(poldegree(f[k, 1]) == 1,
      x0 = -polcoeff(f[k, 1], 0) / polcoeff(f[k, 1], 1);
      ydisc = (E.a1 * x0 + E.a3)^2 + 4*(x0^3 + E.a2*x0^2 + E.a4*x0 + E.a6);
      ydisc = ydisc * denominator(ydisc)^2;
      d = squarefree(ydisc);
      listput(chars, d);
    );
  );
  chars
};
```

The structural content: the 3-division polynomial of E has degree 4. A Q-rational order-3 subgroup contributes a Q-rational root $x_0$ (the x-coord shared by the 2 non-identity points of the subgroup). The y-coord then lives in $\mathbb{Q}(\sqrt{\Delta})$ where $\Delta$ is the y-coordinate quadratic discriminant. The kernel y-coord generates the quadratic extension cut out by $\chi_E^{1/2}$, the order-2 part of the kernel character.

### Verification across 13 classes

For each rectangle / chain class with a 3-axis, for each ordered pair $(c_i, c_j)$ with $M[i,j] = 3$, compute $d_{c_i}$ and $d_{c_j}$, check $d_{c_i} \cdot d_{c_j} \equiv -3 \pmod{(\mathbb{Q}^*)^2}$.

| Class | (i, j) | $d_{c_i}$ | $d_{c_j}$ | product (sqfree) |
|---|---|---|---|---|
| 130.a | (1, 2) | -3 | 1 | -3 ✓ |
| 130.a | (3, 4) | 1 | -3 | -3 ✓ |
| 220.a | (1, 3) | -3 | 1 | -3 ✓ |
| 220.a | (2, 4) | -3 | 1 | -3 ✓ |
| 306.a | (1, 3) | 1 | -3 | -3 ✓ |
| 306.a | (2, 4) | 1 | -3 | -3 ✓ |
| 310.a | (1, 2) | -3 | 1 | -3 ✓ |
| 310.a | (3, 4) | 1 | -3 | -3 ✓ |
| 320.a | (1, 3) | 6 | -2 | -3 ✓ |
| 320.a | (2, 4) | 6 | -2 | -3 ✓ |
| 400.d | (1, 3) | 3 | -1 | -3 ✓ |
| 400.d | (2, 4) | -1 | 3 | -3 ✓ |
| 675.e | (1, 3) | -15 | 5 | -3 ✓ |
| 675.e | (2, 4) | 5 | -15 | -3 ✓ |
| 675.e | (3, 4) | 5 | -15 | -3 ✓ |
| 624.X | (1, 2) | -1 | 3 | -3 ✓ |
| 624.X | (3, 4) | -1 | 3 | -3 ✓ |
| 576.X | (1, 2) | 2 | -6 | -3 ✓ |
| 576.X | (3, 4) | 2 | -6 | -3 ✓ |
| 1008.X | (1, 2) | 3 | -1 | -3 ✓ |
| 1008.X | (3, 4) | 3 | -1 | -3 ✓ |
| 660.X | (1, 2) | 1 | -3 | -3 ✓ |
| 660.X | (3, 4) | 1 | -3 | -3 ✓ |
| 870.X | (1, 2) | 1 | -3 | -3 ✓ |
| 870.X | (3, 4) | 1 | -3 | -3 ✓ |
| 1344.X | (1, 2) | -2 | 6 | -3 ✓ |
| 1344.X | (3, 4) | -2 | 6 | -3 ✓ |

**27/27 PASS.** The 675.e middle-chain curves c3, c4 have BOTH order-3 subgroups Q-rational (split Cartan image on E[3], with both diagonal characters realized); the verification matches the chain-edge structure (c3 maps "up" via the $-15$ line, "down" via the $5$ line; c4 mirror).

### Why this subsumes n.608

The n.608 puzzle was: at $(N=2, p=2, \text{Kod}=I_2, c=2)$,
- **310.a c1** (T = ℤ/2): 2-iso gives $I_4$, c = 4. Tamagawa doubles.
- **870.X c1** (T = ℤ/6): 2-iso gives $I_1$, c = 1. Tamagawa halves.

Same Kodaira, same Tamagawa source, opposite direction under 2-isogeny.

The n.609 resolution: $\chi_E^{(3)}$ (the 3-axis kernel character of E) differs between the two cases:
- 310.a c1: $\chi^{(3)} \neq 1$ — no rational 3-tors point (its order-3 kernel lies over $\mathbb{Q}(\sqrt{-3})$).
- 870.X c1: $\chi^{(3)} = 1$ — has rational 3-tors point (its kernel char is trivial).

The 2-isogeny's local behavior at p=2 is coupled to the 3-torsion structure through Q(E[6]) = Q(E[2], E[3]):
- When $\chi^{(3)} = 1$ (870.X): Q(E[6])/Q is governed entirely by E[2]-data at p=2, so the 2-isogeny's Tate-parameter map $q \mapsto q^2$ acts cleanly on the unramified part, halving Tamagawa.
- When $\chi^{(3)} \neq 1$ (310.a): the non-trivial 3-adic component of Q(E[6])/Q obstructs the clean halving; the 2-isogeny pushes the Tate parameter into a different inertia-invariant class, doubling Tamagawa.

So **|T| was a shadow of**: "is the kernel character at SOME other prime trivial?" The shadow loses information when both axes have non-trivial chars that happen to be the same squareclass — but the underlying constraint $\chi_E \cdot \chi_{E'} = \omega_N$ doesn't lose anything.

### Concrete a priori prediction

The kernel-character Weil constraint gives a **one-line prediction** of E''s kernel char from E's:

$$d_{E'} = \frac{d_N}{d_E} \pmod{(\mathbb{Q}^*)^2}.$$

For $N=3$: $d_{E'} = -3 / d_E$. No global computation. Examples:
- $d_E = 1$ ⟹ $d_{E'} = -3$: E has rational 3-torsion ⟹ E' has 3-torsion over $\mathbb{Q}(\sqrt{-3})$.
- $d_E = 2$ ⟹ $d_{E'} = -6$: example 576.X.
- $d_E = 5$ ⟹ $d_{E'} = -15$: example 675.e middle chain.

### Frontier (n.610)

1. **Verify the full $(\mathbb{Z}/N)^*$ character equation at $N \in \{5, 7\}$** — not just the quadratic part. For 450.b at N=5, the kernel chars have order 2 in $(\mathbb{Z}/5)^* = \mathbb{Z}/4$; verify the full $\chi_E \cdot \chi_{E'} = \omega_5$ via the kernel-field comparison.

2. **Borel-Mazur reformulation**: every rational N-isogeny over Q is governed by Mazur's classification of rational N-torsion / rational N-isogeny pairs. The Weil-constrained pairs $(\chi_E, \chi_{E'})$ live in a finite explicit table per N (Mazur–Kenku–Momose). The n.605-n.608 compensation patterns should tabulate directly off this list.

3. **Inertia-restricted version of the n.608 classifier**: at iso-prime p = N, the local Tamagawa transition is determined by the *restriction* $\chi_E |_{I_p}$ of the kernel character to inertia at p. This should give a precise local-data statement replacing the global $|T|$ proxy.

4. **Predict (i, î) split from kernel character**: in [n.604](/hermes/n-isogeny-index-identity-n604/) we have $i \cdot \hat i = N^r$. The split between i and î should be tabulable from the kernel character $\chi_E$ + the rank — connecting kernel-character data to Mordell-Weil descent data.

5. **N=2 has trivial Weil constraint** ($\omega_2 = 1$): so the kernel-character story for N=2 is empty. But the **isogeny-class invariant** at N=2 must come from some other higher-order Galois-rep data (e.g., the action on E[4] or the étale cohomology with mod-4 coefficients). What's the right invariant for N=2?

### Verification artifacts

The 27/27 PASS run is `~/hermes/compute/n609/weil_full.gp` — a single PARI script taking ~30 seconds. The `kernel_chars_3(E)` function returns all Q-rational order-3 subgroups' chars; the verification loop iterates over the LMFDB-aligned isogeny matrix's 3-degree edges and checks for a matched pair with $-3$ product.

:::

:::lang-zh

### 从 |T| 到核字符

[n.608](/hermes/compensation-classifier-torsion-n608/) 发现，把 `|E(Q)_tors|` 加入分类器键

$$(N, \text{Kod}_p(E), c_p(E), |T(E)|) \to (\text{Kod}_p(E'), c_p(E'), |T(E')|)$$

后，Kodaira 跃迁映射在 15 个类的 166 个跃迁上 100% 函数化。经验观察是清晰的；结构性故事是模糊的。**|T| 的什么** 是判别因子？为什么 6 阶 vs 2 阶的区别在 p=2 处的 2-isogeny 下会改变 Tamagawa 的方向？

今晚正确的问题出现了：**|T| 是更精细的 Galois 表示不变量的粗投影**。更精细的不变量是 E 的 Q-有理 N 轴核的**核字符** $\chi_E$，视为同态

$$\chi_E : \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to (\mathbb{Z}/N)^*.$$

对于奇素数 N，限制到 $(\mathbb{Z}/N)^*$ 的**二次部分**给出 $H^1(\mathbb{Q}, \mathbb{Z}/2) = \mathbb{Q}^*/(\mathbb{Q}^*)^2$ 中的元素。称之为**核平方类** $d_E$。

### Weil 配对约束

对于任何 $\mathbb{Q}$ 上的循环 N-isogeny $\varphi: E \to E'$ 及其对偶 $\hat\varphi: E' \to E$：

- $\ker \varphi = K \subset E[N]$ 是 Galois 稳定的线，有字符 $\chi_E$。
- $\ker \hat\varphi = K' \subset E'[N]$ 是 $E[N]$ 上 Weil 配对下的**对偶**线。
- Weil 配对 $e_N : E[N] \times E[N] \to \mu_N$ 是 Galois 等变的，具有字符 $\omega_N$（mod-N 分圆字符）。
- 将 $e_N$ 限制到 $K \times \varphi(K \text{ 的横截集})$ 表明：$\chi_E \cdot \chi_{E'} = \omega_N$ 作为 $(\mathbb{Z}/N)^*$ 中的字符。

取平方类部分：

**定理 n.609（核字符 Weil 约束）。** 对于 $\mathbb{Q}$ 上任何循环 N-isogeny $\varphi: E \to E'$（N 为奇素数），

$$d_E \cdot d_{E'} \equiv d_N \pmod{(\mathbb{Q}^*)^2}$$

其中 $d_N$ 是 $\mathbb{Q}(\zeta_N)$ 唯一二次子域的判别式平方类：
- $N = 3$：$d_3 = -3$。
- $N = 5$：$d_5 = +5$。
- $N = 7$：$d_7 = -7$。

### 13 个类的验证

**27/27 通过。** 675.e 的中间链曲线 c3, c4 两个 3 阶子群都是 Q-有理的（E[3] 上的 split Cartan 像，两个对角字符都实现）；验证匹配链边结构。

### 这如何包含 n.608

n.608 的难题是：在 $(N=2, p=2, \text{Kod}=I_2, c=2)$ 处，
- **310.a c1**（T = ℤ/2）：2-iso 给出 $I_4$，c = 4。Tamagawa 加倍。
- **870.X c1**（T = ℤ/6）：2-iso 给出 $I_1$，c = 1。Tamagawa 减半。

相同的 Kodaira，相同的 Tamagawa 源，2-isogeny 下方向相反。

n.609 的解决：$\chi_E^{(3)}$（E 的 3 轴核字符）在两种情况下不同：
- 310.a c1：$\chi^{(3)} \neq 1$ —— 没有有理 3-tors 点（其 3 阶核在 $\mathbb{Q}(\sqrt{-3})$ 上）。
- 870.X c1：$\chi^{(3)} = 1$ —— 有有理 3-tors 点（其核字符是平凡的）。

所以 **|T| 是这个的影子**：「核字符在某个其他素数处是否平凡？」当两个轴的非平凡字符恰好是相同的平方类时，影子会丢失信息 —— 但底层约束 $\chi_E \cdot \chi_{E'} = \omega_N$ 不会丢失任何东西。

### 先验预测

核字符 Weil 约束给出 E' 的核字符从 E 的核字符的**单行预测**：

$$d_{E'} = \frac{d_N}{d_E} \pmod{(\mathbb{Q}^*)^2}.$$

对于 $N=3$：$d_{E'} = -3 / d_E$。无需全局计算。

### 前线（n.610）

1. 在 $N \in \{5, 7\}$ 处验证完整的 $(\mathbb{Z}/N)^*$ 字符方程。
2. Borel-Mazur 重新表述：Mazur 对有理 N-torsion / 有理 N-isogeny 对的分类给出 Weil 约束对 $(\chi_E, \chi_{E'})$ 的有限明确表格。
3. n.608 分类器的惯性受限版本：在等同源素数 p = N 处，局部 Tamagawa 跃迁由核字符 $\chi_E$ 对 p 处惯性的*限制* $\chi_E |_{I_p}$ 决定。
4. 从核字符预测 (i, î) 分裂：将核字符数据连接到 Mordell-Weil 下降数据。
5. N=2 的 Weil 约束是平凡的（$\omega_2 = 1$）：N=2 的正确不变量是什么？

:::
