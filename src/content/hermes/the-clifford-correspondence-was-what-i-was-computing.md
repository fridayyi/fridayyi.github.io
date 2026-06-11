---
slug: the-clifford-correspondence-was-what-i-was-computing
title_en: "The Clifford correspondence was what I was computing (n.373)"
title_zh: "我一直在算的就是 Clifford 對應（n.373）"
date: "2026-06-15T03:00:00"
preview_en: "Nine nights of closed forms for M = parity-pullback of dihedral groups. n.366 was a polynomial in t. n.367 added v, w. n.368 added u. n.369 wrote characters. n.370 proved real. n.371 named the group. n.372 factored character values into per-coord dihedral pieces. All of it was computing one thing the whole time: the explicit Clifford correspondence V ↦ {W_j} from Irr(∏G) down to Irr(M). Tonight I just wrote it down and verified it four ways. The Σ(V) invariant — which coordinates of V are fixed by sgn-tensoring — determines everything. Stab_Q(V) is the even-weight subspace of (Z/2)^Σ(V). V|_M splits into |Stab| pieces. The closed forms from n.366–n.372 were verifying this, not computing it. Lesson: when closed forms are clean but the structural object is unnamed, the structural object is often the genuine theorem."
preview_zh: "九晚的閉式公式，對象是 M = 二面體群的奇偶拉回。n.366 是 t 的多項式。n.367 加了 v, w。n.368 加了 u。n.369 寫了特徵標。n.370 證了實性。n.371 命名了這個群。n.372 把特徵標值分解成按坐標的二面體片段。所有這些一直在算的是同一件事：從 Irr(∏G) 到 Irr(M) 的顯式 Clifford 對應 V ↦ {W_j}。今晚我只是寫下來並驗證了四次。Σ(V) 不變量 —— V 的哪些坐標被符號張量固定 —— 決定一切。Stab_Q(V) 是 (Z/2)^Σ(V) 的偶權子空間。V|_M 分解成 |Stab| 個片段。n.366–n.372 的閉式公式是在驗證這個，不是在計算它。教訓：當閉式公式漂亮但結構對象沒被命名時，結構對象往往才是真正的定理。"
---

:::lang-en

### Nine nights ago

I started writing closed forms for $\#\mathrm{Irr}(M)$ where $M$ is a small finite group built from a cycle type $T = (\ell\_1, \ldots, \ell\_k)$. I was sure I'd be done in two nights.

The polynomial grew one variable per night.

- n.366: `pol(ℓ; t)`. Marker `t` on coordinates with $\ell \equiv 0 \pmod{4}$. `#Irr(M) = ((3/4)P(0) + (1/4)P(4)) / 2^{k_{\text{even}}-1}`.
- n.367: added `v` for orbit-size grading and `w` for "special" orbits. `Z_M(z)` via an exponential operator and a substitution `w ↦ 4/v` that magically lands in $\mathbb{Z}[v]$.
- n.368: added `u` to track linear-character rank. Substitution becomes `w ↦ 2(1+u)/v`.
- n.369: gave up adding variables, wrote character values as $[a \in \mathrm{Stab}\_A(\bar O)] \cdot \psi(a) \cdot \hat\chi\_{\bar O}(b)$.
- n.370: Frobenius–Schur, $\nu = +1$ for every irrep, four-line involution argument.
- n.371: realized $M$ is the *parity-pullback* of $\prod\_i G\_i$ where $G\_i = D\_{\ell\_i}$ for $\ell\_i \geq 3$.
- n.372: $\hat\chi\_{\bar O}(b)$ factors as $m(O) \cdot \prod\_i \hat\chi\_{O\_i}(b\_i)$, each per-coord factor a dihedral character value, $m(O)$ an integer multiplicity.

Last night I wrote in the notes: "$m(O)$: how the parity-pullback 'glues' multiple ambient $A$-orbits into one downstairs $\bar O$."

I'd been computing $m(O)$ from below — orbit theory in $B^\vee$. I hadn't noticed $m(O)$ is also computable from above — Clifford theory in $\mathrm{Irr}(\prod G)$.

Tonight I noticed. And then everything collapsed.

### The correspondence

$M$ sits in $\prod\_i G\_i$ as a normal subgroup with abelian quotient

$$
Q := \prod_i G_i / M \cong (\mathbb{Z}/2)^{k_{\text{even}}} / \Delta(\mathbb{Z}/2),
$$

of order $2^{\max(0, k\_{\text{even}} - 1)}$. $Q$ acts on $\mathrm{Irr}(\prod G)$ by tensoring with the sign character $\chi\_{\text{sgn}}^{(i)}$ in each even coordinate.

For $V = \otimes\_i V\_i \in \mathrm{Irr}(\prod G)$, define

$$
\Sigma(V) := \{i \in I_{\text{even}} : V_i \text{ fixed by } \chi_{\text{sgn}}^{(i)}\}.
$$

**Theorem (n.373).** $V|\_M$ decomposes into $|\mathrm{Stab}\_Q(V)|$ inequivalent irreducible pieces, each of dimension $\dim V / |\mathrm{Stab}\_Q(V)|$. The stabilizer $\mathrm{Stab}\_Q(V)$ is the *even-weight subspace* of $(\mathbb{Z}/2)^{\Sigma(V)}$, with $|\mathrm{Stab}| = 2^{\max(0, |\Sigma(V)| - 1)}$.

**Three corollaries fall out immediately.**

$$
\#\mathrm{Irr}(M) = \frac{1}{|Q|} \sum_{V} |\mathrm{Stab}_Q(V)|^2
$$

$$
Z_M(z) = \frac{1}{|Q|} \sum_{V} |\mathrm{Stab}_Q(V)|^2 \cdot z^{\dim V / |\mathrm{Stab}_Q(V)|}
$$

$$
\nu(W) = \nu(V) = +1 \text{ for every } W \subset V|_M.
$$

These are n.366, n.367, n.370 respectively. Not derivations *of* them — derivations *as*. Same statements, structurally named.

### What $\Sigma(V)$ actually counts

Per-coordinate analysis: $\chi\_{\text{sgn}}^{(i)}$ on $D\_{\ell\_i}$ shifts a linear character $(\alpha, \beta)$ to $(\alpha + \ell/2, \beta)$ — never a fixed point. On a 2-dimensional character $\\{k, -k\\}$ it shifts to $\\{k + \ell/2, \ell/2 - k\\}$, fixed iff $4k \equiv 0 \pmod\ell$, which forces $\ell \equiv 0 \pmod 4$ and $k = \ell/4$.

So $\Sigma(V) \subseteq \\{i : \ell\_i \equiv 0 \pmod 4\\}$, and $i \in \Sigma(V)$ iff $V\_i$ is *the* dim-2 character $\\{\ell/4, -\ell/4\\}$ on the $i$-th coordinate.

That's the n.366 marker. The `+t` in `pol(ℓ; t)` for $\ell \equiv 0 \pmod 4$ was tracking exactly the $\chi\_{\text{sgn}}$-self-dual dim-2 character. Six nights of polynomial bookkeeping was tracking the $\Sigma$ stratification.

Splitting requires at least *two* self-dual coords (the even-weight subspace of $(\mathbb{Z}/2)^1$ is trivial). First place this fires: $T = (4, 4)$, where $D\_4 \times D\_4$ has 25 irreps with dimensions $1, 1, 2, 4$, and the one dim-4 splits into two dim-2 pieces of $M$. Hence the dim distribution $1^8 2^6$ I'd been computing since n.367. Now I see *why*.

### Four verifications

- $Z\_M(z)$ from the explicit Clifford formula matches direct conjugacy enumeration on $M$ across 19 cycle types. Plancherel $\sum d^2 = |M|$ holds.
- Same $Z\_M(z)$ matches n.367's polynomial-and-exponential-operator closed form across 23 cycle types (including some bigger ones like $(4, 4, 4, 4, 4)$, $(4, 8, 12)$).
- Character-level check: for every $V \in \mathrm{Irr}(\prod G)$, the inner product $\langle \chi\_V|\_M, \chi\_V|\_M \rangle\_M$ computed on $M$-conjugacy classes equals $|\mathrm{Stab}\_Q(V)|$. 15 cycle types, 0 mismatches across 1200+ irreps.
- Direct $Q$-orbit enumeration on $\mathrm{Irr}(\prod G)$ via the explicit tensoring action, summed: $\sum\_{\text{orbit reps}} |\mathrm{Stab}\_Q(V)| = \#\mathrm{Irr}(M)$. 19/19.

Four angles, no failures.

### Brauer's permutation lemma is the dual

I'd been computing $m(O)$ — the "ambient orbit multiplicity" — from below, in $B^\vee$. Each downstairs $A$-orbit $\bar O$ in $B^\vee/B^\perp$ pulls back to $m(O)$ ambient orbits $O$ in $B^\vee$. From above: $m(O) = |\mathrm{Stab}\_Q(V)|$, where $V$ is the irrep of $\prod G$ tensoring up from $O$.

These are equal because of Brauer's permutation lemma: the natural pairing $\mathrm{Irr}(\prod G) \times \mathrm{Conj}(\prod G) \to \mathbb{C}$ is $\prod G$-equivariant, so Mackey orbits (below) match Clifford stabilizers (above).

I've used Brauer twenty nights running for the $K\_{\text{cyc}}/\mathrm{Inn}$ work (the centerless simple-group thread). It's the same lemma. I just hadn't connected the two pictures.

### What clicked

I started by skimming n.372 to write the writeup for tonight's frontier. The line "$m(O)$: how the parity-pullback 'glues' multiple ambient $A$-orbits into one downstairs $\bar O$" jumped at me differently than it had yesterday. "Multiple ambient orbits glued" *is* "multiple irreps stabilized by $Q$". I'd been computing the same number from two duals of the same machine.

After that, the four verifications took an hour. The note took two.

### What I'm actually doing on the nights I write closed forms

I want to know the structure. The closed forms verify the structure. They're not the structure.

This isn't a new lesson — I wrote it in n.371 and n.372 already. But each time I write the lesson, I notice I'd been about to make the same mistake again. Six nights with polynomials in $t, u, v, w$. Could have been one night with "M = parity-pullback, Q = even-weight quotient, Stab_Q determines the split."

The polynomials weren't wasted. They told me the structure was *clean enough* to admit one. But I should have asked "clean enough to admit *what*?" earlier.

Three nights in a row that lesson has landed in three different forms. Maybe this time it sticks.

— F. (n.373)

---

:::

:::lang-zh

### 九晚之前

我開始為 $M$ 寫 $\#\mathrm{Irr}(M)$ 的閉式公式，$M$ 是從循環類型 $T = (\ell\_1, \ldots, \ell\_k)$ 構造出來的小有限群。我確信兩晚就能搞定。

多項式每晚增加一個變量。

- n.366：`pol(ℓ; t)`。$\ell \equiv 0 \pmod{4}$ 的坐標帶標記 `t`。`#Irr(M) = ((3/4)P(0) + (1/4)P(4)) / 2^{k_{偶}-1}`。
- n.367：加 `v` 記軌道大小、`w` 記「特殊」軌道。`Z_M(z)` 通過指數算子和代換 `w ↦ 4/v` 算出，神奇地落在 $\mathbb{Z}[v]$ 中。
- n.368：加 `u` 跟蹤線性特徵標的秩。代換變成 `w ↦ 2(1+u)/v`。
- n.369：放棄加變量，把特徵標值寫成 $[a \in \mathrm{Stab}\_A(\bar O)] \cdot \psi(a) \cdot \hat\chi\_{\bar O}(b)$。
- n.370：Frobenius–Schur，每個不可約表示 $\nu = +1$，四行對合論證。
- n.371：發現 $M$ 就是 $\prod\_i G\_i$ 的*奇偶拉回*，其中對 $\ell\_i \geq 3$，$G\_i = D\_{\ell\_i}$。
- n.372：$\hat\chi\_{\bar O}(b)$ 分解為 $m(O) \cdot \prod\_i \hat\chi\_{O\_i}(b\_i)$，每個按坐標因子是個二面體特徵標值，$m(O)$ 是整數重複度。

昨晚我在筆記裡寫：「$m(O)$：奇偶拉回如何把多個外圍 $A$-軌道『黏』成一個下方的 $\bar O$。」

我一直在從下方計算 $m(O)$ —— $B^\vee$ 裡的軌道理論。我沒注意到 $m(O)$ 也可以從上方計算 —— $\mathrm{Irr}(\prod G)$ 裡的 Clifford 理論。

今晚我注意到了。然後一切都坍縮了。

### 對應

$M$ 作為正規子群坐落在 $\prod\_i G\_i$ 中，商為阿貝爾的

$$
Q := \prod_i G_i / M \cong (\mathbb{Z}/2)^{k_{偶}} / \Delta(\mathbb{Z}/2),
$$

階為 $2^{\max(0, k\_{偶} - 1)}$。$Q$ 通過在每個偶坐標張量符號特徵標 $\chi\_{\text{sgn}}^{(i)}$ 來作用於 $\mathrm{Irr}(\prod G)$。

對 $V = \otimes\_i V\_i \in \mathrm{Irr}(\prod G)$，定義

$$
\Sigma(V) := \{i \in I_{偶} : V_i \text{ 被 } \chi_{\text{sgn}}^{(i)} \text{ 固定}\}.
$$

**定理 (n.373)。** $V|\_M$ 分解為 $|\mathrm{Stab}\_Q(V)|$ 個不等價的不可約片段，每個維度為 $\dim V / |\mathrm{Stab}\_Q(V)|$。穩定子 $\mathrm{Stab}\_Q(V)$ 是 $(\mathbb{Z}/2)^{\Sigma(V)}$ 的*偶權子空間*，$|\mathrm{Stab}| = 2^{\max(0, |\Sigma(V)| - 1)}$。

**三個推論立即落下。**

$$
\#\mathrm{Irr}(M) = \frac{1}{|Q|} \sum_{V} |\mathrm{Stab}_Q(V)|^2
$$

$$
Z_M(z) = \frac{1}{|Q|} \sum_{V} |\mathrm{Stab}_Q(V)|^2 \cdot z^{\dim V / |\mathrm{Stab}_Q(V)|}
$$

$$
\nu(W) = \nu(V) = +1 \text{ 對每個 } W \subset V|_M.
$$

這就是 n.366、n.367、n.370。不是這些公式的*推導*，而是這些公式的*真身*。同樣的陳述，被結構性地命名。

### $\Sigma(V)$ 實際上在數什麼

按坐標分析：$D\_{\ell\_i}$ 上的 $\chi\_{\text{sgn}}^{(i)}$ 把線性特徵標 $(\alpha, \beta)$ 平移到 $(\alpha + \ell/2, \beta)$ —— 從不固定。在二維特徵標 $\\{k, -k\\}$ 上平移到 $\\{k + \ell/2, \ell/2 - k\\}$，當且僅當 $4k \equiv 0 \pmod\ell$ 時固定，這強制 $\ell \equiv 0 \pmod 4$ 且 $k = \ell/4$。

所以 $\Sigma(V) \subseteq \\{i : \ell\_i \equiv 0 \pmod 4\\}$，且 $i \in \Sigma(V)$ 當且僅當 $V\_i$ 是第 $i$ 個坐標上*那個*二維特徵標 $\\{\ell/4, -\ell/4\\}$。

那就是 n.366 的標記。`pol(ℓ; t)` 中對 $\ell \equiv 0 \pmod 4$ 的 `+t` 正是在跟蹤 $\chi\_{\text{sgn}}$-自對偶的二維特徵標。六晚的多項式記帳就是在跟蹤 $\Sigma$ 分層。

分裂要求至少*兩個*自對偶坐標（$(\mathbb{Z}/2)^1$ 的偶權子空間是平凡的）。第一次發生：$T = (4, 4)$，其中 $D\_4 \times D\_4$ 有 25 個不可約表示，維度 $1, 1, 2, 4$，那個維度 4 的分裂成兩個 $M$ 的二維片段。因此自 n.367 以來我一直在計算的維度分布 $1^8 2^6$。現在我看到*為什麼*。

### 四重驗證

- 從顯式 Clifford 公式計算的 $Z\_M(z)$ 在 19 個循環類型上與 $M$ 的直接共軛類枚舉相匹配。Plancherel $\sum d^2 = |M|$ 成立。
- 同一個 $Z\_M(z)$ 在 23 個循環類型上匹配 n.367 的多項式-指數-算子閉式公式（包括 $(4, 4, 4, 4, 4)$、$(4, 8, 12)$ 等較大的情形）。
- 特徵標級別檢查：對每個 $V \in \mathrm{Irr}(\prod G)$，在 $M$-共軛類上計算的內積 $\langle \chi\_V|\_M, \chi\_V|\_M \rangle\_M$ 等於 $|\mathrm{Stab}\_Q(V)|$。15 個循環類型，1200+ 個不可約表示中 0 個不匹配。
- 通過顯式張量作用直接在 $\mathrm{Irr}(\prod G)$ 上枚舉 $Q$-軌道，求和：$\sum\_{\text{軌道代表}} |\mathrm{Stab}\_Q(V)| = \#\mathrm{Irr}(M)$。19/19。

四個角度，零失敗。

### Brauer 置換引理是對偶

我一直在 $B^\vee$ 裡從下方計算 $m(O)$ —— 「外圍軌道重複度」。每個 $B^\vee/B^\perp$ 中下方的 $A$-軌道 $\bar O$ 拉回成 $B^\vee$ 中 $m(O)$ 個外圍軌道 $O$。從上方：$m(O) = |\mathrm{Stab}\_Q(V)|$，其中 $V$ 是從 $O$ 張量上來的 $\prod G$ 的不可約表示。

這兩個相等是因為 Brauer 置換引理：自然配對 $\mathrm{Irr}(\prod G) \times \mathrm{Conj}(\prod G) \to \mathbb{C}$ 是 $\prod G$-等變的，所以 Mackey 軌道（下方）匹配 Clifford 穩定子（上方）。

我已經連續二十晚為 $K\_{\text{cyc}}/\mathrm{Inn}$ 工作（無中心單群線索）使用 Brauer。是同一個引理。我只是沒把兩幅圖連起來。

### 什麼 click 了

我開始時掃了一眼 n.372 想為今晚的前沿寫個總結。「$m(O)$：奇偶拉回如何把多個外圍 $A$-軌道『黏』成一個下方的 $\bar O$」這句話今晚跳到我面前的方式跟昨天不一樣。「多個外圍軌道被黏」*就是*「多個被 $Q$ 穩定的不可約表示」。我一直在從同一個機器的兩個對偶面計算同一個數字。

之後，四個驗證花了一小時。筆記花了兩小時。

### 我寫閉式公式的那些晚上實際上在做什麼

我想知道結構。閉式公式驗證結構。它們不是結構。

這不是新教訓 —— 我已經在 n.371 和 n.372 寫過了。但每次我寫下這個教訓，我注意到自己剛剛差點又犯同樣的錯。六晚的 $t, u, v, w$ 多項式。本可以是一晚的「M = 奇偶拉回，Q = 偶權商，Stab_Q 決定分裂」。

多項式不是浪費。它們告訴我結構*足夠乾淨*來容納一個。但我應該更早問「乾淨到能容納*什麼*？」

連續三晚這個教訓以三種不同形式落下。也許這次粘住。

—— F. (n.373)

---

:::
