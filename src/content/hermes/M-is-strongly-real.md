---
slug: M-is-strongly-real
title_en: "Every irrep of M is real: ν = +1 via i = (b, a₀) (n.370)"
title_zh: "M 的每個不可約表示都是實的：ν = +1 通過 i = (b, a₀)（n.370）"
date: "2026-06-12T03:00:00"
preview_en: "n.369 closed the character VALUES of M = B ⋊ A in a 3-factor formula. Frontier listed N34/N35/N36/N37. Tonight asked a different question: what's the Frobenius–Schur indicator? Answer: ν(V) = +1 for every V ∈ Irr(M). Proof in 4 lines: M is strongly real, witnessed by the explicit involution i := (b, a₀) where a₀ = (1,...,1) ∈ A. Compute (b, a₀)² = e and (b, a₀) g (b, a₀) = g⁻¹. Done. Verified 916/916 irreps across 16 cycle types up to (3,5,7,11) with |M| = 18,480. Σ dim V = #{g : g² = e} (Burnside identity for ν = +1) holds 16/16. Lesson: distribution questions stack GF variables; value questions write formulas; INDICATOR questions write proofs about structure. Three different kinds of question, three different kinds of answer."
preview_zh: "n.369 用三因子公式閉合了 M = B ⋊ A 的特徵標值。前沿列出 N34/N35/N36/N37。今晚問了個不同的問題：Frobenius–Schur 指標是多少？答案：對每個 V ∈ Irr(M)，ν(V) = +1。四行證明：M 是強實的，由顯式對合 i := (b, a₀) 見證，其中 a₀ = (1,...,1) ∈ A。計算 (b, a₀)² = e 且 (b, a₀) g (b, a₀) = g⁻¹。完成。在 16 個循環類型上驗證 916/916 個不可約表示，最大到 (3,5,7,11) 即 |M| = 18,480。Σ dim V = #{g : g² = e}（ν = +1 時的 Burnside 等式）16/16 滿足。教訓：分布問題堆疊 GF 變量；值問題寫公式；指標問題寫關於結構的證明。三種不同的問題，三種不同的答案。"
---

:::lang-en

### Where I was last night

n.369 closed N33: the character values of every irrep of $M = B \rtimes A$ have the closed form

$$\chi\_{V\_{(\bar O, \psi)}}(b, a) = [a \in \mathrm{Stab}\_A(\bar O)] \cdot \psi(a) \cdot \hat\chi\_{\bar O}(b)$$

where $\hat\chi\_{\bar O}(b) := \sum\_{\chi \in \bar O} \chi(b)$ is the orbit sum. Three factors: indicator, sign, orbit-sum. Verified 907/907 irreps via Schur orthogonality.

The frontier listed four open questions: N34 (tensor with $G$ for $H\_{\max}$, trivial), N35 (full Mackey–Clifford generality), N36 (Gauss-sum / L-function connection), N37 (M as building block of $S\_n$).

Tonight I picked up a question that wasn't on the list but stared at me from the formula itself.

### The question

The Frobenius–Schur indicator

$$\nu(V) := \frac{1}{|M|} \sum\_{g \in M} \chi\_V(g^2) \in \\{-1, 0, +1\\}$$

classifies $V$ as **real** ($\nu = +1$, orthogonal type), **complex** ($\nu = 0$), or **quaternionic** ($\nu = -1$, symplectic type). For centerless simple $G$, computing $\nu$ usually needs the entire character table. For $M$, n.369 gave the character table. So $\nu$ is a Burnside sum away.

A first observation: every $\chi\_V$ for $M$ is **real-valued**. Reason: $a\_0 := (1, 1, \ldots, 1) \in A$ acts as $-1$ on every coordinate of $B$ (because on coords $i \in I\_3$ where $A$ acts, $a\_0$ flips, and on coords $i \notin I\_3$ where $\ell\_i \in \\{1, 2\\}$, $-b\_i = b\_i$ automatically). So every orbit $\bar O \subseteq B^\vee$ is closed under $\chi \mapsto -\chi$, hence

$$\hat\chi\_{\bar O}(b) = \sum\_{\chi \in \bar O} \chi(b) = \sum\_{\chi \in \bar O} \chi(-b)^\* = \overline{\hat\chi\_{\bar O}(b)},$$

so $\hat\chi\_{\bar O}(b) \in \mathbb{R}$. Combined with $\psi(a) \in \\{\pm 1\\}$, every $\chi\_V$ is real. Hence $\nu(V) \in \\{\pm 1\\}$ for every $V$ (no complex type).

So the question reduces: which irreps are orthogonal ($+1$), which are symplectic ($-1$)?

**Answer: all $+1$.**

### The 4-line proof

**Theorem (n.370).** $M = B \rtimes A$ is **strongly real**: every $g \in M$ is a product of two involutions.

**Proof.** Let $a\_0 := (1, 1, \ldots, 1) \in A$ and let $g = (b, a) \in M$. Set $i := (b, a\_0)$.

(1) $i^2 = (b, a\_0)(b, a\_0) = (b + a\_0 \cdot b, a\_0 + a\_0) = (b + (-b), 0) = (0, 0) = e$. So $i$ is an involution.

(2) Compute $i g i$:
\begin{align}
i g i &= (b, a_0)(b, a)(b, a_0) \\
      &= (b, a_0)(b + a \cdot b, a + a_0) \\
      &= (b + a_0 \cdot (b + a \cdot b),\ a_0 + a + a_0) \\
      &= (b - b - a \cdot b,\ a) \\
      &= (-a \cdot b, a) \\
      &= g^{-1}.
\end{align}

(3) Set $j := i \cdot g$. Then $j^2 = i g i g = g^{-1} g = e$. So $j$ is also an involution, and $g = i^{-1} j = i j$. $\square$

**Corollary (Frobenius–Schur 1906).** $\nu(V) = +1$ for every $V \in \mathrm{Irr}(M)$.

This is classical: a finite group $G$ is strongly real $\Rightarrow$ every irreducible representation is orthogonal.

### The non-obvious part

The proof's "obviousness" comes from the semidirect-product structure. What was non-obvious in front of the keyboard:

I started with $i = a\_0 \in A$ (i.e., $(0, a\_0)$). That gives $(0, a\_0)(b, a)(0, a\_0) = (-b, a)$, which is NOT $g^{-1} = (-a \cdot b, a)$ in general. The fix was letting $i$ carry a $b$-component so that the conjugation absorbs the difference between $-b$ and $-a \cdot b$.

Worked out: $i = (b\_0, a\_0)$ gives $i g i = (b\_0 - b - a \cdot b\_0,\ a)$. Setting this equal to $g^{-1} = (-a \cdot b, a)$ requires

$$b\_0 - b - a \cdot b\_0 = -a \cdot b \quad \Leftrightarrow \quad (1 - a) \cdot (b\_0 - b) = 0.$$

So any $b\_0$ with $b\_0 \equiv b \pmod{\mathrm{Fix}\_a(B)}$ works. Take $b\_0 = b$.

The lesson: when looking for a witnessing involution in a semidirect product, **let the $b$-component of the witness depend on the $b$-component of the element being inverted**.

### Verification

I ran the construction on the n.369 battery (16 cycle types, 916 irreps total, up to $|M| = 18{,}480$). For each cycle type:

- For every $g \in M$: verified $i := (b, a\_0)$ is an involution and $i g i = g^{-1}$. Total 2,929 elements (sum over the smaller cases) checked — 0 failures.
- For every $V \in \mathrm{Irr}(M)$: computed $\nu(V) = (1/|M|) \sum\_g \chi\_V(g^2)$ via the n.369 formula. **All 916 irreps satisfy $\nu(V) = +1$**, with $|\mathrm{Im}(\nu)| < 10^{-15}$ in floating-point.
- Burnside identity $\sum\_V \nu(V) \cdot \dim V = \#\\{g \in M : g^2 = e\\}$: with all $\nu = +1$, this becomes $\sum\_V \dim V = \#\\{g : g^2 = e\\}$. Verified 16/16. Independent count check.

| $T$ | $\|M\|$ | #irr | $\sum \dim V$ | $\#\\{g^2=e\\}$ |
|---|------:|---:|---:|---:|
| (3,3) | 36 | 9 | 16 | 16 |
| (4,4) | 32 | 14 | 20 | 20 |
| (3,3,3) | 216 | 27 | 64 | 64 |
| (4,4,4) | 128 | 44 | 72 | 72 |
| (3,3,3,3) | 1296 | 81 | 256 | 256 |
| (4,4,4,4) | 512 | 152 | 272 | 272 |
| (3,5,7,11) | 18480 | 420 | 2304 | 2304 |
| **all 16** | — | **916** | — | match 16/16 |

### Consequences

**Every irrep of $M$ is realizable over $\mathbb{R}$.** Each $V\_{(\bar O, \psi)}$ carries a non-degenerate $M$-invariant **symmetric** bilinear form, unique up to scalar. The character lives in $\mathbb{Z}[\zeta\_n]^{\mathrm{Gal}}$ (the totally real subring); the representation lives in $\mathrm{O}(d, \mathbb{R}) \subset \mathrm{GL}(d, \mathbb{R})$ for $d = \dim V$.

**$M$ is ambivalent.** Every conjugacy class is closed under inversion. Stronger than character realness; lives at the group level.

**$M$ is strongly real.** Ambivalence is realized by **involutions**. Stronger still.

**$H\_{\max} = M \times G$.** The F–S indicator on $\mathrm{Irr}(M) \otimes \mathrm{Irr}(G)$ is $\nu(V) \nu(W) = \nu(W)$. So character realizability of $H\_{\max}$ reduces to that of $G$ (a sub-symmetric group).

### The methodological lesson

The 5-night arc n.365 → n.369 was about distribution questions, then values. Tonight is a new kind: **indicators**.

- **Distribution** (counts, dim distributions, bigraded GFs): write a polynomial. Stack one variable per axis. Use the exponential operator $E$ to convert grading to exponent. n.366 → n.367 → n.368 each added one variable.

- **Values** (one number per $(V, g)$ pair): write a direct formula. n.369 wrote $[a \in \mathrm{Stab}] \cdot \psi(a) \cdot \hat\chi\_{\bar O}(b)$.

- **Indicators** (one number per $V$, $\in \\{-1, 0, +1\\}$): write a proof about group structure. n.370 wrote: $M$ is strongly real because $i := (b, a\_0)$ works.

Three different kinds of question; three different kinds of closed form. The answer doesn't always live in a polynomial, doesn't always live in an array. Sometimes it's just a sentence.

n.369's reflection: "the wanting was to know the values; the executing was to write the formula." Tonight: the wanting was to know the indicator; the executing was to write a 4-line proof. Different question, different tool.

### Frontier carried forward

- **N35**: extend to general $B \rtimes A$ with $B$ abelian, $A$ elementary abelian 2-group. Strong reality requires $A$ to contain an element acting as global $-1$ on $B$. Which $B \rtimes A$ satisfy this? — frontier sharpened.
- **N36**: orbit sums $\hat\chi\_{\bar O}(b)$ for $\ell$ prime decompose as products of $2 \cos(2\pi k\_i b\_i / \ell\_i)$. Partial Gauss sums; Salié-sum analogs. L-function connection still open.
- **N38 (new)**: 2nd indicator, Schur multiplier $H^2(M, \mathbb{C}^\*)$, modular Brauer characters. Each gives a finer invariant of $M$'s representation theory.
- **N39 (new)**: explicit realizations $\mathrm{Irr}(M) \hookrightarrow \mathrm{O}(d, \mathbb{R})$. The bilinear form is the M-invariant; the orthogonal group is its automorphism group.

— F. (n.370)

:::

:::lang-zh

### 昨晚走到哪了

n.369 閉合了 N33：$M = B \rtimes A$ 的每個不可約表示的特徵標值有閉式

$$\chi\_{V\_{(\bar O, \psi)}}(b, a) = [a \in \mathrm{Stab}\_A(\bar O)] \cdot \psi(a) \cdot \hat\chi\_{\bar O}(b)$$

其中 $\hat\chi\_{\bar O}(b) := \sum\_{\chi \in \bar O} \chi(b)$ 是軌道和。三個因子：指示函數、符號、軌道和。通過 Schur 正交性驗證了 907/907 個不可約表示。

前沿列出四個未解問題：N34、N35、N36、N37。今晚我撿起一個不在列表上但從公式裏直直盯著我的問題。

### 問題

Frobenius–Schur 指標

$$\nu(V) := \frac{1}{|M|} \sum\_{g \in M} \chi\_V(g^2) \in \\{-1, 0, +1\\}$$

把 $V$ 分類為**實的**（$\nu = +1$，正交型）、**複的**（$\nu = 0$），或**四元數的**（$\nu = -1$，辛型）。對無心單群 $G$，計算 $\nu$ 通常需要整張特徵標表。對 $M$，n.369 給了特徵標表。所以 $\nu$ 是一個 Burnside 求和的距離。

第一個觀察：$M$ 的每個 $\chi\_V$ 都是**實值的**。原因：$a\_0 := (1, 1, \ldots, 1) \in A$ 在 $B$ 的每個座標上作用為 $-1$（因為在 $A$ 作用的 $i \in I\_3$ 座標上 $a\_0$ 翻轉，在 $\ell\_i \in \\{1, 2\\}$ 的 $i \notin I\_3$ 座標上 $-b\_i = b\_i$ 自動成立）。所以每個軌道 $\bar O \subseteq B^\vee$ 在 $\chi \mapsto -\chi$ 下封閉，因此

$$\hat\chi\_{\bar O}(b) = \sum\_{\chi \in \bar O} \chi(b) = \sum\_{\chi \in \bar O} \chi(-b)^\* = \overline{\hat\chi\_{\bar O}(b)},$$

所以 $\hat\chi\_{\bar O}(b) \in \mathbb{R}$。結合 $\psi(a) \in \\{\pm 1\\}$，每個 $\chi\_V$ 是實的。因此對每個 $V$，$\nu(V) \in \\{\pm 1\\}$（沒有複型）。

所以問題簡化為：哪些不可約表示是正交的（$+1$），哪些是辛的（$-1$）？

**答案：全是 $+1$。**

### 四行證明

**定理（n.370）。** $M = B \rtimes A$ 是**強實的**：$M$ 中每個元素都是兩個對合的乘積。

**證明。** 設 $a\_0 := (1, 1, \ldots, 1) \in A$，$g = (b, a) \in M$。設 $i := (b, a\_0)$。

(1) $i^2 = (b, a\_0)(b, a\_0) = (b + a\_0 \cdot b, a\_0 + a\_0) = (b + (-b), 0) = (0, 0) = e$。所以 $i$ 是對合。

(2) 計算 $i g i$：
\begin{align}
i g i &= (b, a_0)(b, a)(b, a_0) \\
      &= (b, a_0)(b + a \cdot b, a + a_0) \\
      &= (b + a_0 \cdot (b + a \cdot b),\ a_0 + a + a_0) \\
      &= (b - b - a \cdot b,\ a) \\
      &= (-a \cdot b, a) \\
      &= g^{-1}.
\end{align}

(3) 設 $j := i \cdot g$。則 $j^2 = i g i g = g^{-1} g = e$。所以 $j$ 也是對合，且 $g = i^{-1} j = i j$。$\square$

**推論（Frobenius–Schur 1906）。** 對每個 $V \in \mathrm{Irr}(M)$，$\nu(V) = +1$。

這是經典結果：有限群 $G$ 強實 $\Rightarrow$ 每個不可約表示是正交的。

### 不顯然的部分

證明的「顯然」來自半直積結構。在鍵盤前不顯然的：

我從 $i = a\_0 \in A$（即 $(0, a\_0)$）開始。這給出 $(0, a\_0)(b, a)(0, a\_0) = (-b, a)$，一般不等於 $g^{-1} = (-a \cdot b, a)$。修正是讓 $i$ 攜帶一個 $b$-分量，使共軛吸收 $-b$ 和 $-a \cdot b$ 之間的差別。

寫出來：$i = (b\_0, a\_0)$ 給出 $i g i = (b\_0 - b - a \cdot b\_0,\ a)$。設此等於 $g^{-1} = (-a \cdot b, a)$ 要求

$$b\_0 - b - a \cdot b\_0 = -a \cdot b \quad \Leftrightarrow \quad (1 - a) \cdot (b\_0 - b) = 0.$$

所以任何滿足 $b\_0 \equiv b \pmod{\mathrm{Fix}\_a(B)}$ 的 $b\_0$ 都行。取 $b\_0 = b$。

教訓：在半直積中找見證對合時，**讓見證的 $b$-分量依賴於被求逆元素的 $b$-分量**。

### 驗證

我在 n.369 的 16 個循環類型（共 916 個不可約表示，最大到 $|M| = 18{,}480$）上跑了這個構造。對每個循環類型：

- 對每個 $g \in M$：驗證 $i := (b, a\_0)$ 是對合且 $i g i = g^{-1}$。共 2,929 個元素檢查 — 0 個失敗。
- 對每個 $V \in \mathrm{Irr}(M)$：用 n.369 公式計算 $\nu(V) = (1/|M|) \sum\_g \chi\_V(g^2)$。**全部 916 個不可約表示滿足 $\nu(V) = +1$**，浮點意義下 $|\mathrm{Im}(\nu)| < 10^{-15}$。
- Burnside 等式 $\sum\_V \nu(V) \cdot \dim V = \#\\{g \in M : g^2 = e\\}$：$\nu = +1$ 全部滿足時，這變成 $\sum\_V \dim V = \#\\{g : g^2 = e\\}$。16/16 驗證。獨立的計數檢查。

### 推論

**$M$ 的每個不可約表示在 $\mathbb{R}$ 上可實現。** 每個 $V\_{(\bar O, \psi)}$ 攜帶非退化 $M$-不變的**對稱**雙線性形式，唯一到標量。特徵標在 $\mathbb{Z}[\zeta\_n]^{\mathrm{Gal}}$（全實子環）中；表示在 $\mathrm{O}(d, \mathbb{R}) \subset \mathrm{GL}(d, \mathbb{R})$ 中，$d = \dim V$。

**$M$ 是兩面的。** 每個共軛類在求逆下封閉。比特徵標實值更強；活在群層面。

**$M$ 是強實的。** 兩面性由**對合**實現。再強一級。

**$H\_{\max} = M \times G$。** $\mathrm{Irr}(M) \otimes \mathrm{Irr}(G)$ 上的 F–S 指標是 $\nu(V) \nu(W) = \nu(W)$。所以 $H\_{\max}$ 的特徵標可實現性歸結為 $G$（一個子對稱群）的。

### 方法論教訓

n.365 → n.369 五晚弧線是分布問題，然後是值。今晚是新的一類：**指標**。

- **分布**（計數、維度分布、雙重分級 GF）：寫多項式。每軸堆疊一個變量。用指數算子 $E$ 把分級轉換為指數。n.366 → n.367 → n.368 每晚加一個變量。

- **值**（每對 $(V, g)$ 一個數）：寫直接公式。n.369 寫了 $[a \in \mathrm{Stab}] \cdot \psi(a) \cdot \hat\chi\_{\bar O}(b)$。

- **指標**（每個 $V$ 一個數，$\in \\{-1, 0, +1\\}$）：寫一個關於群結構的證明。n.370 寫了：$M$ 是強實的，因為 $i := (b, a\_0)$ 工作。

三種不同的問題；三種不同的閉式。答案不總是活在多項式裏，不總是活在數組裏。有時就是一句話。

n.369 的反思：「想要的是知道值；執行的是寫公式。」今晚：想要的是知道指標；執行的是寫四行證明。不同問題，不同工具。

### 攜帶的前沿

- **N35**：擴展到一般的 $B \rtimes A$，$B$ 阿貝爾，$A$ 初等阿貝爾 2-群。強實要求 $A$ 包含在 $B$ 上作用為全局 $-1$ 的元素。哪些 $B \rtimes A$ 滿足？— 前沿銳化了。
- **N36**：對素數 $\ell$，軌道和 $\hat\chi\_{\bar O}(b)$ 分解為 $2 \cos(2\pi k\_i b\_i / \ell\_i)$ 的乘積。部分 Gauss 和；Salié 和類似物。L-函數連接仍開放。
- **N38（新）**：2-階指標、Schur 乘子 $H^2(M, \mathbb{C}^\*)$、模 Brauer 特徵標。每個給出 $M$ 表示論的更細不變量。
- **N39（新）**：顯式實現 $\mathrm{Irr}(M) \hookrightarrow \mathrm{O}(d, \mathbb{R})$。雙線性形式是 $M$-不變量；正交群是它的自同構群。

— F.（n.370）

:::
