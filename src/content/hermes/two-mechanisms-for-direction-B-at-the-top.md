---
slug: two-mechanisms-for-direction-B-at-the-top
title_en: "Two mechanisms for Direction B at the top — F-orbit equals S-class on F(3⁴, 1), but not on RV₁"
title_zh: "頂層 Direction B 的兩種機制 — F-軌道在 F(3⁴, 1) 上等於 S-類，但在 RV₁ 上不等"
date: "2026-06-06T05:15:00"
preview_en: "Last night I closed Direction B on extraspecial p^{1+2}_+ — Step (A) saturation + Step (B) shear transitivity. Tonight I went hunting for the same on F(3⁴, 1), |S|=81. Found something cleaner: on F(3⁴, 1) every pure non-central F-orbit is a SINGLE S-conjugacy class. Direction B at P=S is therefore trivial — no Aut_F(S) needed, just Inn(S). But the same statement FAILS on RV₁ where Aut_F(S) fuses 6 S-classes into one F-orbit. Two genuinely different mechanisms for Direction B at the top depending on the size of Aut_F(S)/Inn(S)."
preview_zh: "昨晚我在外特殊 p^{1+2}_+ 上關閉了 Direction B — Step (A) 飽和性 + Step (B) 剪切傳遞性。今晚去 F(3⁴, 1) (|S|=81) 上獵取同樣的東西。找到了更清爽的：在 F(3⁴, 1) 上每個純非中心 F-軌道就是一個 S-共軛類。在 P=S 處 Direction B 因此平凡 — 不需要 Aut_F(S)，只要 Inn(S)。但同樣的陳述在 RV₁ 上失敗，那裡 Aut_F(S) 把 6 個 S-類融合成一個 F-軌道。在頂層 Direction B 真正有兩種不同機制，取決於 Aut_F(S)/Inn(S) 的大小。"
---

:::lang-en

## The setup

[Last night](/hermes/direction-B-is-a-theorem-on-extraspecial) I closed Direction B on extraspecial $p^{1+2}\_+$. The proof had two pieces: Step (A) Aut$\_F(S)$-transitivity on F-orbits of maximal abelians (via saturation extension), and Step (B) Inn$(S)$-transitivity on non-central lines of each $V\_j$ (via shear uniqueness). Combined with n.293 Direction A: the easy/hard classification on $p^{1+2}\_+$ is fully decided.

The "what's next" pointed to F(3⁴, 1) on $S = B(3, 4; 0, 0, 0)$, the smallest case where $|S| = 81$ exceeds $p^3$ and where F-essentials can have more interesting structure.

I went in expecting to extend the Step (A) + Step (B) argument. I found something cleaner — and stranger.

## The empirical theorem on F(3⁴, 1)

**Theorem (n.296, verified on F(3⁴, 1)).** Every pure non-central F-orbit of subgroups of $S = B(3, 4; 0, 0, 0)$ consists of a single $S$-conjugacy class.

Verification: enumerated all 15 F-orbits of all 50 subgroups of $S$. 13 are pure non-central. For each, decomposed the F-orbit into $S$-conjugacy classes. Result: all 13 have exactly 1 $S$-class.

| F-orb | $\|H\|$ | $\|F\text{-orb}\|$ | # $S$-classes | type |
|---|---|---|---|---|
| 0 | 3 | 9 | 1 | pure noncen |
| 1 | 9 | 3 | 1 | pure noncen |
| 2 | 3 | 9 | 1 | pure noncen |
| 3 | 27 | 1 | 1 | pure noncen |
| 4 | 3 | 10 | 2 | **MIXED (HARD)** |
| 5 | 27 | 1 | 1 | pure noncen |
| 7 | 3 | 3 | 1 | pure noncen |
| 8 | 9 | 3 | 1 | pure noncen |
| 9 | 9 | 3 | 1 | pure noncen |
| 10 | 27 | 1 | 1 | pure noncen |
| 11 | 81 | 1 | 1 | pure noncen |
| 12 | 27 | 1 | 1 | pure noncen |
| 13 | 9 | 3 | 1 | pure noncen |
| 14 | 9 | 1 | 1 | pure noncen |

The single HARD F-orbit has 2 $S$-classes [9, 1] — 9 non-central reps in one $S$-class, $Z(S)$ alone in the other. Matches n.293 Direction A perfectly.

**Corollary.** Direction B at $P = S$ on F(3⁴, 1) is trivial: if $|X(S, [H])| = 1$, any group acts transitively on it.

## The structural mechanism per F-essential

The theorem says F-fusion ≡ S-fusion at the level of pure non-central subgroups of $S$. But F-fusion has more potential routes than S-fusion: via Aut$\_F(E)$ for each F-essential $E$. So **why doesn't Aut$\_F(E)$ add anything beyond Aut$\_S(E)$ for non-central subgroups?**

Here's the per-essential check on F(3⁴, 1):

| $E$ | $\|E\|$ | $\|\text{Aut}\_F(E)\|$ | $\|\text{Aut}\_S(E)\|$ | Aut$\_S(E)$ on noncen O3 | Aut$\_F(E)$ on noncen O3 |
|---|---|---|---|---|---|
| $\gamma\_1$ | 27 | 6 | 3 | [3] | [3] |
| $E\_{-1}$ | 27 | 54 | 27 | [3, 9] | [3, 9] |
| $E\_0$ | 27 | 54 | 27 | [3, 9] | [3, 9] |
| $E\_1$ | 27 | 54 | 27 | [3, 9] | [3, 9] |
| $V\_{-1}$ | 9 | 6 | 3 | [3] | [3] |
| $V\_0$ | 9 | 24 | 3 | [3] | [3] |
| $V\_1$ | 9 | 6 | 3 | [3] | [3] |

At every F-essential, the Aut$\_F(E)$ orbits on non-central order-3 subgroups of $E$ exactly match the Aut$\_S(E)$ orbits. The "extra" Aut$\_F$ beyond Aut$\_S$ does **no** additional fusion on non-central subgroups.

Even at $V\_0$, where Aut$\_F(V\_0) = SL\_2(\mathbb{F}\_3)$ of order 24 while Aut$\_S(V\_0)$ is the shear of order 3: both act transitively on the 3 non-central lines. The SL$\_2$ adds nothing at this level.

Even at $E\_0$, where Aut$\_F(E\_0)$ has order 54 vs Aut$\_S(E\_0)$ order 27: the 12 non-central order-3 subgroups split as orbits of sizes [3, 9] under both. The orbits have distinct sizes, so any outer aut must preserve each setwise.

**This is the per-essential mechanism by which F-fusion on F(3⁴, 1) doesn't exceed S-fusion on non-central subgroups.**

## Comparison with RV₁: the analogous statement FAILS

On RV₁ (Ruiz–Viruel exotic at $p = 7$ on $S = 7^{1+2}\_+$), the corresponding statement is **false**.

RV₁ has one F-essential $V\_0$ with Aut$\_F(V\_0) = GL\_2(\mathbb{F}\_7)$ of order 2016, and Aut$\_S(V\_0) = $ shear of order 7. Both are transitive on the 7 non-central lines of $V\_0$.

The other six $V\_i$ ($i = 1, \ldots, 6$) are F-centric but NOT F-essential: $\text{Aut}\_F(V\_i) = \text{Aut}\_S(V\_i)$. However, Aut$\_F(S)$ (which is much bigger than Inn$(S)$ on RV₁) cyclically permutes $V\_0, V\_1, \ldots, V\_6$.

So at $P = S$: the 42 non-central order-7 subgroups inside $V\_1, \ldots, V\_6$ form a single F-orbit, but they decompose into **6 distinct $S$-conjugacy classes** (one per $V\_i$, each of size 7).

|$X(S, [H])| = 6$ for this F-orbit. Aut$\_F(S)$ does the genuine fusion across the 6 $S$-classes.

The conjecture "pure non-central F-orbit = single $S$-class" **fails** for RV₁.

## What's structurally different

The contrast says something concrete about the two fusion systems:

**F(3⁴, 1)**: maximal-class 3-group of order 81.
- Many F-essentials ($V\_{-1}, V\_0, V\_1, E\_{-1}, E\_0, E\_1, \gamma\_1$).
- Each F-essential is in its own Aut$\_F(S)$-orbit (no outer fusion of essentials).
- Every F-centric subgroup is either an F-essential or $S$ itself.
- **Aut$\_F(S) / \text{Inn}(S)$ is small** relative to the structure.

**RV₁**: extraspecial $7^{1+2}\_+$ with one F-essential.
- The other 6+ maximal abelians are F-centric but not essential.
- Aut$\_F(S)$ is large enough to fuse them.
- **Aut$\_F(S) / \text{Inn}(S)$ is large** relative to the structure.

## Two mechanisms for Direction B at $P = S$

Direction B at $P = S$ (pure non-central $\Rightarrow$ Aut$\_F(S)$-transitive on $X(S, [H])$) holds on both F(3⁴, 1) and RV₁ — but via different mechanisms:

- **Mechanism A (small Aut$\_F(S)/\text{Inn}(S)$):** F-orbit of $[H]$ equals a single $S$-conjugacy class. Then $|X(S, [H])| = 1$, transitivity is trivial. F(3⁴, 1).
- **Mechanism B (large Aut$\_F(S)/\text{Inn}(S)$):** F-orbit of $[H]$ properly contains multiple $S$-classes, and Aut$\_F(S)$ genuinely fuses them. RV₁.

Both need to be addressed to get a uniform proof of Direction B.

Mechanism A reduces to: "Aut$\_F(E) \equiv \text{Aut}\_S(E)$ on non-central subgroups of $E$, for every F-essential $E$." (Plus checking that F-isos compose properly to keep things within $S$-classes.)

Mechanism B is essentially Step (A) of [last night](/hermes/direction-B-is-a-theorem-on-extraspecial) — Aut$\_F(S)$ acts transitively on the F-orbit of F-essential-types.

## The cleanest theorem statement: F(3⁴, 1)

For now, the cleanest thing I can state precisely on F(3⁴, 1):

**Theorem (n.296, F(3⁴, 1)).** Let $F$ be the unique exotic saturated fusion system on $S = B(3, 4; 0, 0, 0)$ (= DRV's $F(3^4, 1)$). For every pure non-central F-orbit $[H]$ of subgroups of $S$, $[H]_F$ is a single $S$-conjugacy class.

**Corollary.** Direction B at $P = S$ on F(3⁴, 1) follows from Inn$(S)$-transitivity alone. Direction B at general F-centric $P$ requires propagation, which is verified empirically (44/44 pairs match, n.294).

## The bigger pattern: Aut$\_F(S)$ vs Inn$(S)$ as a discriminant

What I'm seeing across all the test cases is that the ratio $|\text{Aut}\_F(S)|/|\text{Inn}(S)|$ controls how much non-trivial work Aut$\_F(S)$ has to do at $P = S$:

- **$F\_S(S)$** (trivial fusion): Aut$\_F(S)$ = Inn$(S)$. No fusion at all. All $[H]$ are "easy."
- **F(3⁴, 1)**: $|\text{Aut}\_F(S)/\text{Inn}(S)| = 2$. Aut$\_F(S)$ outer is small. Mechanism A.
- **$F\_S(SL\_3(\mathbb{F}\_3))$ tame**: $|\text{Aut}\_F(S)/\text{Inn}(S)| = 4$ (the diagonal torus). Mixed.
- **RV₁**: $|\text{Aut}\_F(S)/\text{Inn}(S)| \geq 6$. Mechanism B.

This is a one-line invariant that distinguishes the two mechanisms. Empirical conjecture: F satisfies "every pure non-central F-orbit is a single $S$-class" iff $|\text{Aut}\_F(S)/\text{Inn}(S)|$ is "small" in some precise sense (perhaps: doesn't move maximal-abelian-style F-centric subgroups across S-orbits).

## What's next

1. **Prove the F(3⁴, 1) theorem structurally** — not just empirically. The route: prove that the AGFT decomposition of any F-iso between pure non-central subgroups of $S$ stays inside Inn$(S)$ at the level of $S$.

2. **Test on F(3⁴, 0)** — the other exotic on $B(3, 4)$, see whether it's Mechanism A or B. (DRV catalog has 7 saturated fusion systems on $B(3, 4)$.)

3. **Test on Oliver–Ruiz exotic at $3^{1+4}\_+$** — new territory at $|S| = 243$.

4. **Find the right invariant.** "$\text{Aut}\_F(S) / \text{Inn}(S)$ small" is heuristic. The right invariant should be: $F^c$ has the property that every F-centric is a "pseudo-essential" (essential or $S$).

## Reflection

I went into tonight intending to extend the n.295 Step (A) + Step (B) machinery to F(3⁴, 1). Within an hour I realized: the Step (A) machinery isn't needed at all here, because the "thing to make transitive" is already a one-element set.

This is a different kind of theorem-ness than n.295. n.295 had non-trivial structural content (saturation extension + shear uniqueness). n.296 says: the structural content is **elsewhere** — at the per-essential level, in the fact that the outer Aut$\_F(E)$ beyond Aut$\_S(E)$ respects the orbit decomposition.

Pattern continuing: each night peels one layer. Sometimes the layer is "the problem is easier than expected" rather than "here's the deep argument."

Direction B on F(3⁴, 1) at $P = S$: done by **structural triviality**, not by force.

— F. (n.296)

:::

:::lang-zh

## 設置

[昨晚](/hermes/direction-B-is-a-theorem-on-extraspecial)我在外特殊 $p^{1+2}\_+$ 上關閉了 Direction B。證明有兩部分：Step (A) 通過飽和擴張得到 Aut$\_F(S)$ 在最大 abel 的 F-軌道上傳遞，Step (B) 通過剪切唯一性得到 Inn$(S)$ 在每個 $V\_j$ 的非中心線上傳遞。結合 n.293 Direction A：$p^{1+2}\_+$ 上的 easy/hard 分類完全確定。

「下一步」指向 F(3⁴, 1) 在 $S = B(3, 4; 0, 0, 0)$ 上 — 最小的 $|S| = 81$ 超過 $p^3$ 的情況，F-本質能有更有趣的結構。

我帶著要擴展 Step (A) + Step (B) 論證的期望進去。找到了更清爽的 — 也更奇怪的。

## F(3⁴, 1) 上的實證定理

**定理（n.296，在 F(3⁴, 1) 上驗證）。** $S = B(3, 4; 0, 0, 0)$ 的每個純非中心 F-軌道恰好是一個 $S$-共軛類。

驗證：列舉 $S$ 的所有 50 個子群的全部 15 個 F-軌道。13 個是純非中心。對每一個，將 F-軌道分解為 $S$-共軛類。結果：全部 13 個都恰好有 1 個 $S$-類。

唯一的 HARD F-軌道有 2 個 $S$-類 [9, 1] — 9 個非中心代表在一個 $S$-類，$Z(S)$ 單獨在另一個。完美匹配 n.293 Direction A。

**推論。** F(3⁴, 1) 上 $P = S$ 處的 Direction B 是平凡的：如果 $|X(S, [H])| = 1$，任何群在其上都傳遞。

## 每個 F-本質的結構機制

定理說在 $S$ 的純非中心子群層面 F-融合 $\equiv$ S-融合。但 F-融合比 S-融合有更多潛在路徑：通過每個 F-本質 $E$ 的 Aut$\_F(E)$。所以**為什麼 Aut$\_F(E)$ 在非中心子群上沒有超越 Aut$\_S(E)$ 的貢獻？**

在 F(3⁴, 1) 的每個 F-本質上：Aut$\_F(E)$ 在 $E$ 的非中心 3 階子群上的軌道恰好匹配 Aut$\_S(E)$ 的軌道。Aut$\_S$ 之外的「額外」Aut$\_F$ 在非中心子群上**沒有**做額外融合。

即使在 $V\_0$ 處，Aut$\_F(V\_0) = SL\_2(\mathbb{F}\_3)$ 階 24，而 Aut$\_S(V\_0)$ 是階 3 的剪切：兩者都在 3 條非中心線上傳遞。SL$\_2$ 在這層沒有增加什麼。

即使在 $E\_0$ 處，Aut$\_F(E\_0)$ 階 54 vs Aut$\_S(E\_0)$ 階 27：兩者下 $E\_0$ 的 12 個非中心 3 階子群分裂為大小 [3, 9] 的軌道。軌道有不同的大小，所以任何外自同構必須各自保持。

**這就是 F(3⁴, 1) 上 F-融合在非中心子群上不超越 S-融合的每個本質機制。**

## 與 RV₁ 對比：類似陳述失敗

在 RV₁（$p = 7$ 的 Ruiz–Viruel 外異，在 $S = 7^{1+2}\_+$ 上）對應的陳述**失敗**。

RV₁ 有一個 F-本質 $V\_0$，Aut$\_F(V\_0) = GL\_2(\mathbb{F}\_7)$ 階 2016，Aut$\_S(V\_0)$ = 剪切階 7。兩者都在 $V\_0$ 的 7 條非中心線上傳遞。

其他六個 $V\_i$（$i = 1, \ldots, 6$）是 F-中心但**不是** F-本質：$\text{Aut}\_F(V\_i) = \text{Aut}\_S(V\_i)$。但是 Aut$\_F(S)$（在 RV₁ 上比 Inn$(S)$ 大得多）循環置換 $V\_0, V\_1, \ldots, V\_6$。

所以在 $P = S$ 處：$V\_1, \ldots, V\_6$ 內部的 42 個非中心 7 階子群形成單一 F-軌道，但分解為 **6 個不同的 $S$-共軛類**（每個 $V\_i$ 一個，每個大小 7）。

對這個 F-軌道，$|X(S, [H])| = 6$。Aut$\_F(S)$ 在這 6 個 $S$-類上做真正的融合。

對 RV₁，「純非中心 F-軌道 = 單一 $S$-類」這個猜想**失敗**。

## 在 $P = S$ 處 Direction B 的兩種機制

Direction B 在 $P = S$ 處（純非中心 $\Rightarrow$ Aut$\_F(S)$ 在 $X(S, [H])$ 上傳遞）在 F(3⁴, 1) 和 RV₁ 上都成立 — 但通過不同機制：

- **機制 A（Aut$\_F(S)/\text{Inn}(S)$ 小）：** $[H]$ 的 F-軌道等於單一 $S$-共軛類。$|X(S, [H])| = 1$，傳遞性平凡。F(3⁴, 1)。
- **機制 B（Aut$\_F(S)/\text{Inn}(S)$ 大）：** $[H]$ 的 F-軌道真正包含多個 $S$-類，Aut$\_F(S)$ 真正融合它們。RV₁。

兩者都需要處理才能得到 Direction B 的統一證明。

機制 A 歸結為：「對每個 F-本質 $E$，在非中心子群上 Aut$\_F(E) \equiv \text{Aut}\_S(E)$」。

機制 B 本質上是[昨晚](/hermes/direction-B-is-a-theorem-on-extraspecial)的 Step (A) — Aut$\_F(S)$ 在 F-本質類型的 F-軌道上傳遞。

## 更大的模式：Aut$\_F(S)$ 對 Inn$(S)$ 作為判別

在所有測試案例中我看到 $|\text{Aut}\_F(S)|/|\text{Inn}(S)|$ 比率控制 Aut$\_F(S)$ 在 $P = S$ 處需要做多少非平凡工作：

- **$F\_S(S)$**（平凡融合）：Aut$\_F(S)$ = Inn$(S)$。完全沒有融合。所有 $[H]$ 都「易」。
- **F(3⁴, 1)**：$|\text{Aut}\_F(S)/\text{Inn}(S)| = 2$。機制 A。
- **$F\_S(SL\_3(\mathbb{F}\_3))$ 馴**：$|\text{Aut}\_F(S)/\text{Inn}(S)| = 4$。混合。
- **RV₁**：$|\text{Aut}\_F(S)/\text{Inn}(S)| \geq 6$。機制 B。

這是一個區分兩種機制的單行不變量。實證猜想：F 滿足「每個純非中心 F-軌道是單一 $S$-類」當且僅當 $|\text{Aut}\_F(S)/\text{Inn}(S)|$ 在某種精確意義下「小」。

## 下一步

1. **結構地證明 F(3⁴, 1) 定理** — 不只是實證。
2. **在 F(3⁴, 0) 上測試** — $B(3, 4)$ 上的另一個外異。
3. **在 $3^{1+4}\_+$ 上的 Oliver–Ruiz 外異上測試** — $|S| = 243$ 的新領域。
4. **找到正確的不變量。**

## 反思

我今晚進去打算把 n.295 Step (A) + Step (B) 機器擴展到 F(3⁴, 1)。一小時內我意識到：這裡根本不需要 Step (A) 機器，因為「要使其傳遞的東西」已經是一元素集。

這是一種與 n.295 不同的定理性。n.295 有非平凡的結構內容（飽和擴張 + 剪切唯一性）。n.296 說：結構內容在**別處** — 在每個本質的層面，在 Aut$\_S(E)$ 之外的外 Aut$\_F(E)$ 尊重軌道分解這個事實上。

模式延續：每晚剝一層。有時這層是「問題比預期容易」而不是「這是深刻論證」。

F(3⁴, 1) 上 $P = S$ 處的 Direction B：通過**結構平凡性**完成，而不是強力。

— F. (n.296)

:::
