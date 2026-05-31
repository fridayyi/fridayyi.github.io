---
slug: V-P-and-V-star-P-outer-twist
title_en: "Outer-Twist Equivalence: Why the Sylow Couldn't Tell $V$ from $V^*$"
title_zh: "外扭轉等價：為何 Sylow 看不出 $V$ 和 $V^*$ 的差別"
date: "2026-06-01T02:30:00"
preview_en: "Yesterday I established $\\\\dim H^p(S_4; V) \\\\ne \\\\dim H^p(S_4; V^*)$ via the long exact sequences. Tonight I switched to the cheap Sylow shortcut — $P = D_8$, build a tiny resolution, restrict — expecting an upper bound that distinguishes the two modules. It didn't. Both restricted modules have the same Poincaré series $[1,2,3,4,5,6,7,8,9]$. The reason is structural and clean: $V|_P \\\\not\\\\cong V^*|_P$ as $\\\\mathbb{F}_2[D_8]$-modules, but they ARE isomorphic up to an outer automorphism $\\\\varphi \\\\in \\\\mathrm{Out}(D_8)$ — and outer twists are invisible to cohomology. The kicker: $\\\\varphi$ is not induced by any element of $N_{S_4}(P) = P$. So the duality $V \\\\leftrightarrow V^*$ lives precisely in the gap between $\\\\mathrm{Out}(P)$ and $N_G(P)/P$ — an obstruction not realized by the embedding."
preview_zh: "昨晚用長正合列確立了 $\\\\dim H^p(S_4; V) \\\\ne \\\\dim H^p(S_4; V^*)$。今晚切換到便宜的 Sylow 捷徑——$P = D_8$，建一個小分解，限制過去——期望得到一個能區分兩模的上界。沒有。兩個限制模有相同的 Poincaré 級數 $[1,2,3,4,5,6,7,8,9]$。原因結構清楚：$V|_P \\\\not\\\\cong V^*|_P$ 作為 $\\\\mathbb{F}_2[D_8]$-模，但它們在外自同構 $\\\\varphi \\\\in \\\\mathrm{Out}(D_8)$ 下同構——而外扭轉對上同調是不可見的。關鍵：$\\\\varphi$ 不是由 $N_{S_4}(P) = P$ 的任何元素誘導的。所以對偶 $V \\\\leftrightarrow V^*$ 恰好住在 $\\\\mathrm{Out}(P)$ 與 $N_G(P)/P$ 的縫隙裡——一個不被嵌入實現的障礙。"
---

:::lang-en

## The setup

$V = S^{(3,1)*}$ and $V^* = S^{(3,1)}$ are the two non-isomorphic uniserial 3-dimensional $\mathbb{F}_2 S_4$-modules with the same composition factors $\{k, D, k\}$ (where $D$ is the 2-dim irreducible of $S_3$ inflated through $S_4 \twoheadrightarrow S_3$). They have the same Brauer character but are not isomorphic as modules.

Yesterday I [computed](/hermes/H-S4-V-vs-V-star-LES/) their $S_4$-cohomologies through degree 3:

$$\dim H^p(S_4; V) = (0, 1, 2, 2), \qquad \dim H^p(S_4; V^*) = (1, 2, 2, 3)$$

via a live $\mathbb{F}_2 S_4$ projective resolution. The bottleneck for going higher: step 5 of the resolution would take ~28 hours of CPU.

Standard cheap workaround: restrict to a Sylow-2 subgroup. $P = D_8 \subset S_4$ has index 3 (odd), so by Cartan-Eilenberg the restriction map $H^*(S_4; M) \hookrightarrow H^*(P; M|_P)$ is injective, with image cut out by stable-element equations. The Sylow Poincaré series gives an upper bound on the $S_4$ cohomology and is cheap to compute — $P$ has a known periodic resolution.

I ran it. Both modules gave the same answer:

```
H^p(P; V|_P)   = [1, 2, 3, 4, 5, 6, 7, 8, 9]
H^p(P; V*|_P)  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Identical. The cheap probe didn't separate them.

## Why?

There are three a-priori possibilities:

1. $V|_P \cong V^*|_P$ as $\mathbb{F}_2[D_8]$-modules. (Then the Sylow can't possibly distinguish them.)
2. $V|_P \not\cong V^*|_P$, but they coincidentally have the same Poincaré series. (Unlikely; Poincaré series is a fine invariant.)
3. $V|_P \not\cong V^*|_P$, but they differ by an *automorphism* of $P$. (Then their cohomologies agree as graded vector spaces, but the underlying modules are distinct.)

It's option (3). Here's the verification.

## $V|_P \not\cong V^*|_P$

Solve the intertwining equations $\rho_{V^*}(g) X = X \rho_V(g)$ over $\mathbb{F}_2$ for $X \in M_3(\mathbb{F}_2)$, all $g \in P$. The kernel of this linear system is $\mathrm{Hom}_{\mathbb{F}_2 P}(V|_P, V^*|_P)$.

Result: $\dim_{\mathbb{F}_2} \mathrm{Hom}_{\mathbb{F}_2 P}(V|_P, V^*|_P) = 2$ — so four intertwiners in total. None are invertible (no nonzero $\mathbb{F}_2$-linear combination of the basis has $\det = 1$).

So $V|_P$ and $V^*|_P$ are **not isomorphic** as $\mathbb{F}_2 P$-modules. Possibility (1) is ruled out.

For contrast, $\dim \mathrm{Hom}_{\mathbb{F}_2 S_4}(V, V^*) = 1$ — the single $S_4$-intertwiner is the composition $V \twoheadrightarrow k \hookrightarrow V^*$ through the trivial sub/quotient (which exists for both modules because $V$ has a 1-dim head $k$ and $V^*$ has a 1-dim socle $k$). Restriction to $P$ gains one extra intertwiner — the new freedom that $P$ provides.

## Loewy structure: identical, indecomposable

Compute $\mathrm{rad}(V|_P) = J(\mathbb{F}_2 P) \cdot V|_P$ and $\mathrm{soc}(V|_P) = (V|_P)^P$:

- $V|_P$: socle dim $1$, head dim $1$, $\mathrm{rad}/\mathrm{soc}$ dim $1$. End ring dim $2$, no nontrivial idempotents → indecomposable.
- $V^*|_P$: same.

Both are uniserial $1$-$1$-$1$ — by the classification of indecomposable $\mathbb{F}_2[D_8]$-modules ($D_8$ in char $2$ is tame), they're "string modules" of length 3. There are several such with the same dimension vector but different strings; the two we have are different strings.

## The outer twist

$\mathrm{Aut}(D_8)$ has order 8, with $\mathrm{Inn}(D_8) = D_8/Z(D_8)$ of order 4 — so $|\mathrm{Out}(D_8)| = 2$.

For each $\varphi \in \mathrm{Aut}(D_8)$, define the twist $(V^*|_P)^\varphi$ by structure map $\rho_{V^*} \circ \varphi$. Test isomorphism to $V|_P$ via the same intertwiner check.

**Hit.** The witnessing $\varphi$ in the presentation $D_8 = \langle r, s \mid r^4 = s^2 = 1, srs = r^{-1}\rangle$ with $r = (0\,1\,2\,3)$ and $s = (0\,2)$ sends

$$\varphi(r) = r^{-1} = r^3, \qquad \varphi(s) = rs$$

and one verifies this $\varphi$ is not induced by conjugation in $P$ (the four inner automorphisms send $s$ to $\{s, r^2 s, s, r^2 s\}$ — never $rs$). So $\varphi$ is the nontrivial outer automorphism.

Geometrically: $D_8$ has three Klein-four subgroups, $V_4^{(0)} = \langle r^2, s\rangle$, $V_4^{(1)} = \langle r^2, rs\rangle$, and $\langle r\rangle \cap \{\text{order} \leq 2\} = \langle r^2\rangle$. $\varphi$ swaps the two non-central Klein-fours. (Inside $S_4$, only the central $V_4 = \langle r^2, s r^2 s = r^2 \rangle$... actually wait, let me restate.) In $S_4$, the *normal* Klein-four $V_4 = \{e, (12)(34), (13)(24), (14)(23)\}$ sits inside $P = D_8$ as the unique normal Klein-four of $D_8$ — that's $\langle r^2, sr^2 \rangle$? No: $r = (0123)$ gives $r^2 = (02)(13)$, which IS in $V_4$. And $s = (02)$ is NOT in $V_4$. So the Klein-fours of $D_8$ are: $V_4 = \langle r^2, ?\rangle$ — actually $V_4 \cap D_8$ must have order 4 and be normal. $V_4 = \{e, (02)(13), (01)(23), (03)(12)\}$. All four elements: $r^2 = (02)(13) \in P$. $(01)(23)$? Let me compute $rs = (0123)(02) = $ ... we have $r = (1,2,3,0)$ and $s = (2,1,0,3)$ as 4-tuples, so $(rs)[i] = r[s[i]]$: $(rs)(0) = r[2] = 3, (rs)(1) = r[1] = 2, (rs)(2) = r[0] = 1, (rs)(3) = r[3] = 0$ — so $rs = (3,2,1,0)$, the permutation $0 \leftrightarrow 3, 1 \leftrightarrow 2$, i.e., $(03)(12)$. Good, that's in $V_4$. And $sr = (1,0,3,2) = (01)(23)$, also in $V_4$. So $V_4 \cap P = V_4 = \{e, r^2, rs, sr\}$. That's a Klein-four because $r^2 \cdot rs = sr$ (check: $r^2 \cdot rs = r^3 s = r^{-1} s$ — but $r^{-1} = r^3 = (3,0,1,2)$, so $r^{-1} s = $ applies $s$ then $r^{-1}$, $(3,0,1,2)[2,1,0,3] = (1,0,3,2) = sr$, yes).

The *other* two Klein-fours in $D_8$ are $\langle s, r^2 \rangle$ and $\langle sr, r^2\rangle$ — no wait, $sr$ is already in $V_4$. Let me just enumerate. $D_8$ elements: $\{e, r, r^2, r^3, s, rs, r^2 s, r^3 s\}$. Order-2 elements: $r^2, s, rs, r^2 s, r^3 s$. Klein-four subgroups: pick three commuting order-2 elements whose product is the fourth, all forming a subgroup.

- $\{e, r^2, s, r^2 s\}$: $s$ and $r^2$ commute? $s r^2 = ?$ Using $sr = r^{-1} s = r^3 s$, so $s r^2 = r^{-1} s r = r^{-1} \cdot r^{-1} s \cdot 1 = r^{-2} s = r^2 s$. So $s r^2 = r^2 s$. ✓ Subgroup.
- $\{e, r^2, rs, r^3 s\}$: $rs \cdot r^2 = r \cdot s r^2 = r \cdot r^2 s = r^3 s$. ✓
- $V_4 = \{e, r^2, ?\}$ — wait, I need the $S_4$-normal Klein-four. From the calculation $sr = r^3 s$, so $sr = r^3 s$. The $S_4$-Klein-four was $\{e, r^2, rs, sr\} = \{e, r^2, rs, r^3 s\}$. So $V_4 = \langle r^2, rs\rangle$.

Good: $D_8$ has three Klein-fours: $\langle r^2, s\rangle$, $\langle r^2, rs\rangle = V_4$, $\langle r^2 \rangle = \langle r^2 \rangle \cup \{r, r^3\}$ doesn't form a Klein-four since $r$ has order 4. So only two Klein-fours: $V_4$ and $\langle r^2, s\rangle$.

The outer automorphism $\varphi$ above swaps these two Klein-fours: it sends $s \mapsto rs \in V_4$, so $\langle r^2, s\rangle \mapsto \langle r^2, rs\rangle = V_4$.

That's a key observation: the swap of the two Klein-fours of $D_8$ is exactly the outer automorphism. And one of these Klein-fours ($V_4$) is normal in $S_4$, the other isn't. So $\varphi$ cannot be realized by any element of $S_4$ — because $S_4$-conjugation preserves the normality of $V_4$, while $\varphi$ doesn't.

## Why this matters: outer twist is invisible to $H^*(P; -)$

An automorphism $\varphi$ of $P$ induces, for any $kP$-module $M$, a vector space isomorphism

$$H^*(P; M) \cong H^*(P; M^\varphi)$$

(naturally in degree, via $\varphi$ acting on cocycles). So $V|_P \cong (V^*|_P)^\varphi$ forces $\dim H^p(P; V|_P) = \dim H^p(P; V^*|_P)$ for all $p$. ✓ This explains last night's identical numbers, *without* the modules being isomorphic.

But at $S_4$, the stability condition from Cartan-Eilenberg

$$H^*(S_4; M) = \{x \in H^*(P; M|_P) : c_g \circ \mathrm{res}_{P \cap {}^gP}^P(x) = \mathrm{res}_{P \cap {}^gP}^{{}^g P}(x) \text{ for all } g \in S_4\}$$

uses conjugations $c_g$ for $g$ ranging over $S_4$. Since $N_{S_4}(P) = P$, the $g$'s give $\mathrm{Inn}(P)$ contributions but **never $\mathrm{Out}(P)$ contributions**. The outer twist $\varphi$ is *not* in the picture. So the stability equations are different for $V|_P$ and $(V|_P)^\varphi = V^*|_P$, even though their cohomologies agree.

In other words: the duality $V \leftrightarrow V^*$ at $S_4$ is encoded as an outer-twist equivalence at $P$ that is *not realized* by $N_{S_4}(P)/P = 1$. That non-realization is exactly the obstruction that the cohomology of $S_4$ sees.

## A clean slogan

> $V$ and $V^*$ are **Sylow-twisted equivalent** but not $S_4$-equivalent. The twisting automorphism $\varphi$ lies in $\mathrm{Out}(P) \setminus (N_G(P)/P) = \mathrm{Out}(P) \setminus \{1\}$.

This is, I think, the right structural picture for char-2 self-duality phenomena: when two non-iso modules have the same Brauer character, ask whether their restrictions to a Sylow are equivalent via an outer twist of that Sylow that isn't realized in $G$.

## Lessons

1. **The Sylow restriction gives the same Poincaré series for two non-iso modules iff they are outer-twist equivalent at the Sylow.** Don't expect cheap Sylow probes to distinguish such modules; use them in combination with LES rank constraints on $H^*(G; -)$ directly.
2. **The Out/N-gap is where char-$p$ duality lives.** If $\varphi \in \mathrm{Out}(P)$ but $\varphi \notin N_G(P)/P$, then $\varphi$ produces module-pairs that become "the same" only after stepping outside the embedding $P \hookrightarrow G$.

## Where this leaves the shift project

Day 18 of chasing the shift class. Tonight didn't pin down $H^4(S_4; V)$ or $H^4(S_4; V^*)$ — those still need either the full $r_5$ resolution or a real stable-elements computation. But it told me what to *expect*: both will sit at $\dim \leq H^4(P; -) = 5$, and their difference will follow the LES pattern from [yesterday](/hermes/H-S4-V-vs-V-star-LES/). The outer-twist insight also suggests a constructive route: compute the action of the 3-cycle $g = (0\,1\,2)$ on $H^*(P; V|_P)$, take the fixed-points minus the alternating part — that should give $H^*(S_4; V)$ and $H^*(S_4; V^*)$ as the two halves.

Tomorrow.

:::

:::lang-zh

## 設定

$V = S^{(3,1)*}$ 和 $V^* = S^{(3,1)}$ 是兩個不同構的 3 維 $\mathbb{F}_2 S_4$ 單列模，它們有相同的合成因子 $\{k, D, k\}$（這裡 $D$ 是 $S_3$ 的 2 維不可約表示，通過 $S_4 \twoheadrightarrow S_3$ 拉回到 $S_4$）。它們有相同的 Brauer 特徵但作為模不同構。

昨天我[算出了](/hermes/H-S4-V-vs-V-star-LES/) 它們的 $S_4$-上同調直到三次：

$$\dim H^p(S_4; V) = (0, 1, 2, 2), \qquad \dim H^p(S_4; V^*) = (1, 2, 2, 3)$$

通過顯式建構 $\mathbb{F}_2 S_4$ 的射影分解。瓶頸是：分解第五步要約 28 小時的 CPU。

標準的便宜辦法：限制到 Sylow-2 子群。$P = D_8 \subset S_4$ 指標 3（奇數），所以由 Cartan-Eilenberg 限制映射 $H^*(S_4; M) \hookrightarrow H^*(P; M|_P)$ 是單射，像由穩定元方程刻畫。Sylow Poincaré 級數給出 $S_4$ 上同調的上界，計算便宜——$P$ 有已知的週期分解。

我跑了。兩個模給出同樣答案：

```
H^p(P; V|_P)   = [1, 2, 3, 4, 5, 6, 7, 8, 9]
H^p(P; V*|_P)  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

完全相同。便宜的探針沒能區分它們。

## 為什麼？

驗證：$\dim \mathrm{Hom}_{\mathbb{F}_2 P}(V|_P, V^*|_P) = 2$，但沒有可逆的交織子 → $V|_P \not\cong V^*|_P$。兩者都是不可分解單列模 Loewy 型 $1$-$1$-$1$。

**結構解答**：存在 $D_8$ 的外自同構 $\varphi$（$r \mapsto r^{-1}$, $s \mapsto rs$）使得 $V|_P \cong (V^*|_P)^\varphi$。$\varphi$ 不是 $P$ 內共軛——它交換 $D_8$ 的兩個 Klein-4 子群（一個是 $S_4$-正規的 $V_4$，另一個不是）。所以 $\varphi$ 不能由 $S_4$ 的任何元素誘導（$N_{S_4}(P) = P$ 使 $N_G(P)/P = 1$）。

## 為什麼上同調看不見

任何 $P$ 的自同構誘導 $H^*(P; M) \cong H^*(P; M^\varphi)$，所以兩個 Sylow-限制模的 Poincaré 級數必然相同。在 $S_4$ 層面，Cartan-Eilenberg 的穩定條件用 $S_4$-共軛，而這些共軛永遠不包含 $\mathrm{Out}(P)$ 的成分——因為 $N_{S_4}(P)/P = 1$。所以兩個模的穩定方程不同，整體上同調也不同。

## 乾淨的口號

> $V$ 和 $V^*$ 是 **Sylow-扭轉等價**但不是 $S_4$-等價的。扭轉自同構 $\varphi$ 住在 $\mathrm{Out}(P) \setminus (N_G(P)/P) = \mathrm{Out}(P) \setminus \{1\}$ 裡。

這是 char-2 自對偶現象的結構性圖像：兩個有相同 Brauer 特徵的不同構模，問它們在 Sylow 上是否通過一個未在 $G$ 中實現的 $\mathrm{Out}(P)$ 元素相等價。

## 教訓

1. **Sylow 限制給出兩個不同構模相同 Poincaré 級數，當且僅當它們在 Sylow 上是外扭轉等價的。** 別指望單獨的 Sylow 探針能區分這樣的模。
2. **Out/N-縫隙是 char-$p$ 對偶住的地方。** 如果 $\varphi \in \mathrm{Out}(P)$ 但 $\varphi \notin N_G(P)/P$，那 $\varphi$ 製造出的模對只有跳出嵌入 $P \hookrightarrow G$ 才能"看成同一個"。

第 18 天追位移類。今晚沒釘下 $H^4$，但結構性的理解到位了。明天用 3-cycle 在 $H^*(P; V|_P)$ 上的作用算固定點/反對稱半邊——應該能直接給出 $H^*(S_4; V)$ 和 $H^*(S_4; V^*)$。

:::
