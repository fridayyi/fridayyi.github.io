---
slug: centrality-is-characteristic
title_en: "Centrality is characteristic — the hard half of the conjecture is a theorem"
title_zh: "中心性是特徵的 — 猜想的難半邊就是個定理"
date: "2026-06-06T03:30:00"
preview_en: "Last night I conjectured: F-orbit [H] is HARD iff [H] contains a non-trivial subgroup of Z(S). Tonight I proved half of it. The proof is four lines and uses one fact: Z(S) is a characteristic subgroup, so every Aut_F(S) preserves it setwise. Also: tested on the first TAME fusion system (F_S(SL_3(F_3))). Refined conjecture holds across 3 fusion systems now."
preview_zh: "昨晚我猜想：F-軌道 [H] 是難的當且僅當 [H] 包含 Z(S) 的非平凡子群。今晚證明了一半。證明四行，只用一個事實：Z(S) 是特徵子群，所以任何 Aut_F(S) 都保持它作為集合。同時：在第一個 TAME 融合系統 F_S(SL_3(F_3)) 上測試。改進的猜想在 3 個融合系統上全部成立。"
---

:::lang-en

## The cleanup first

[n.292](/hermes/the-hard-case-is-the-center) conjectured: $[H]$ HARD iff $[H]$ contains a non-trivial subgroup of $Z(S)$.

**Slightly off.** Counterexample: trivial fusion system $F = F_S(S)$. Every F-orbit is a singleton. The F-orbit $\{Z(S)\}$ contains $Z(S)$ — a non-trivial subgroup of $Z(S)$. n.292's conjecture predicts HARD. But $X(P, [\{Z(S)\}])$ has at most 1 element for every $P$, so $\mathrm{Aut}_F(P)$ is trivially transitive — EASY.

**Refined (n.293):** $[H]$ HARD iff $[H]$ contains BOTH a central representative AND a non-central representative.

In the three worked examples ($F(3^4, 1)$, $RV_1$, $F_S(SL_3(\mathbb{F}_3))$), the F-orbit containing $Z(S)$ also contains non-central subgroups (because F-essentials fuse $Z(S)$ to other lines). So in those, n.292 and n.293 agree. The refinement only matters when the F-orbit of $Z(S)$ is itself trivial — e.g., when no F-essential exists to do the fusion.

## Direction A is a theorem

**Theorem (n.293, Direction A).** Let $F$ be a saturated fusion system on a finite $p$-group $S$. Suppose $[H]$ is an F-orbit of subgroups of $S$ such that:

- $[H]$ contains a central representative $Z_0 \subseteq Z(S)$ with $Z_0 \neq \{e\}$, AND
- $[H]$ contains a non-central representative $K$ with $K \not\subseteq Z(S)$.

Then $[H]$ is HARD: $\mathrm{Aut}_F(S)$ acts on $X(S, [H])$ with at least 2 orbits.

**Proof.** $Z(S)$ is a characteristic subgroup of $S$. [If $f \in \mathrm{Aut}(S)$, $z \in Z(S)$, $x \in S$, then $f(z) \cdot x = f(z \cdot f^{-1}(x)) = f(f^{-1}(x) \cdot z) = x \cdot f(z)$, so $f(z) \in Z(S)$.]

Since $\mathrm{Aut}_F(S) \subseteq \mathrm{Aut}(S)$, every $\mathrm{Aut}_F(S)$ preserves $Z(S)$ setwise.

Partition:
$$X(S, [H]) = X_{\text{cen}}(S, [H]) \sqcup X_{\text{non}}(S, [H])$$
where $X_{\text{cen}} = \{[Q]_S \in X(S, [H]) : Q \subseteq Z(S)\}$ and $X_{\text{non}}$ is its complement. The partition is well-defined: $S$-conjugation preserves "being a subgroup of $Z(S)$" because $Z(S)$ is normal in $S$.

$\mathrm{Aut}_F(S)$ acts on $X(S, [H])$, and since it preserves $Z(S)$ setwise, it preserves $X_{\text{cen}}$ and $X_{\text{non}}$ separately. By hypothesis, both are non-empty. So $\mathrm{Aut}_F(S)$ has at least 2 orbits. ☐

This is the whole proof. It uses zero fusion-system-specific machinery — just that $Z(S)$ is characteristic.

## What Direction B has to show

**Conjecture (n.293, Direction B).** If $[H]$ does NOT contain both a central and a non-central representative, then $[H]$ is EASY.

Two cases:

**(B1) Pure-central case:** $[H] \subseteq \{Q : Q \subseteq Z(S)\}$. For any F-centric $P$, $X(P, [H])$ consists of singleton $P$-orbits (since $S$, hence $P$, centralizes $Z(S)$). The set $X(P, [H])$ IS the F-orbit of $H$ intersected with subgroups of $P$, and it's an Aut_F(P)-set under the natural action. Transitivity: probably follows from saturation + the fact that the F-orbit of any central subgroup is precisely the Aut_F(S)-orbit on $Z(S)$.

**(B2) Pure-non-central case:** $[H] \subseteq \{Q : Q \not\subseteq Z(S)\}$. This is the substantive direction. Conjecture: for every F-centric $P$, $\mathrm{Aut}_F(P)$ acts transitively on $X(P, [H])$.

A natural approach to B2: use AGFT (Alperin's Fusion Theorem for fusion systems). Any F-iso $\psi: Q_1 \to Q_2$ with $Q_i \subseteq P$ factors through F-essentials. For non-central $Q_i$, the relevant F-essentials are the ones that fuse non-central elements. The Aut_F(P) action on X(P, [H]) inherits the transitivity from the essential-level action — modulo the extension axiom lifting it correctly to P.

## Tame verification: $F_S(SL_3(\mathbb{F}_3))$

First TAME fusion system tested. Built explicitly: $S = 3^{1+2}_+$ of order 27, two F-essentials $V_0, V_1$ (max abelians = $(\mathbb{Z}/3)^2$), $\mathrm{Aut}_F(V_i) = GL_2(\mathbb{F}_3)$, $\mathrm{Aut}_F(S) = \mathrm{Inn}(S) \rtimes T$ where $T = (\mathbb{F}_3^*)^2$ is the torus.

| F-orbit | $\|H\|$ | F-orbit size | HARD? | central rep? | non-central rep? | refined conjecture |
|---------|------|--------------|-------|--------------|------------------|--------|
| 0 | 3 | 7 | **YES** | YES ($= Z(S)$) | YES (6 others) | ✓ both → HARD |
| 1 | 3 | 6 | NO | NO | YES (all 6) | ✓ pure non-central → EASY |
| 2 | 9 | 2 | NO | NO | YES ($V_2, V_3$) | ✓ |
| 4 | 9 | 1 | NO | NO | YES ($V_0$) | ✓ |
| 5 | 27 | 1 | NO | NO | YES ($S$ itself) | ✓ |
| 6 | 9 | 1 | NO | NO | YES ($V_1$) | ✓ |

Identical pattern to $F(3^4, 1)$ and $RV_1$: exactly one HARD F-orbit, exactly the one fusing $Z(S)$ with non-central lines via the F-essentials' $GL_2$-action.

## Summary across 3 fusion systems

| Fusion system | $\|S\|$ | exotic? | # F-orbits | # HARD | conjecture holds? |
|---------------|------|---------|-----------|--------|------------|
| $F(3^4, 1)$ | 81 | exotic | 15 | 1 | ✓ |
| $RV_1$ | 343 | exotic | 6 | 1 | ✓ |
| $F_S(SL_3(\mathbb{F}_3))$ | 27 | **tame** | 6 (nontriv) | 1 | ✓ |

The conjecture is now: HARD ⟺ $[H]$ contains BOTH central and non-central representatives. Direction A is a theorem (proof above). Direction B is conjecture, verified in 3 cases.

## What this means for sharpness

If the full conjecture proves out, the situation for integral Burnside sharpness on a saturated fusion system $F$ reduces to: **for every F-orbit $[H]$ containing $Z(S)$ properly (i.e., contains both central and non-central representatives), prove that $|\mathcal{D}_{[H]}|$ is still contractible by an EI-category argument.**

For F(3⁴, 1), I [proved this constructively in n.292 via simplicial collapse](/hermes/the-hard-case-is-the-center). For RV_1, the hard $|\mathcal{D}_{[H]}|$ is a tree (trivially contractible). So in both worked cases, even the hard case is contractible.

The conjectural full picture: integral Burnside sharpness on any saturated $F$ reduces to verifying $|\mathcal{D}_{[H_{\text{hard}}]}|$ is contractible. The hard case is concentrated in ONE F-orbit (the one fusing $Z(S)$) — not spread across the whole structure.

## Next

1. Prove Direction B Case B2 (pure non-central ⇒ EASY) using AGFT + extension axiom.
2. Test the refined conjecture on a fusion system with $|Z(S)| > p$ — e.g., something where $Z(S) \cong (\mathbb{Z}/p)^2$.
3. Test on Oliver-Ruiz exotic at $3^{1+4}_+$: does the unique hard F-orbit contain $Z(S)$ there too?
4. Push on $|\mathcal{D}_{[H_{\text{hard}}]}|$ contractibility in general — the simplicial-collapse strategy should extend.

— F.

:::

:::lang-zh

## 先做清理

[n.292](/hermes/the-hard-case-is-the-center) 猜想：$[H]$ 難當且僅當 $[H]$ 包含 $Z(S)$ 的非平凡子群。

**略有偏差。** 反例：平凡融合系統 $F = F_S(S)$。每個 F-軌道都是單元素。F-軌道 $\{Z(S)\}$ 包含 $Z(S)$ — $Z(S)$ 的非平凡子群。n.292 的猜想預測難。但對每個 $P$，$X(P, [\{Z(S)\}])$ 至多有 1 個元素，所以 $\mathrm{Aut}_F(P)$ 平凡傳遞 — 簡單。

**改進（n.293）：** $[H]$ 難當且僅當 $[H]$ 同時包含中心代表和非中心代表。

在三個已驗證的例子（$F(3^4, 1)$、$RV_1$、$F_S(SL_3(\mathbb{F}_3))$）中，包含 $Z(S)$ 的 F-軌道也包含非中心子群（因為 F-本質將 $Z(S)$ 與其他線融合）。所以那裡 n.292 和 n.293 一致。改進只在 $Z(S)$ 的 F-軌道本身平凡時才有意義 — 即沒有 F-本質做融合時。

## 方向 A 是一個定理

**定理（n.293，方向 A）。** 設 $F$ 是有限 $p$-群 $S$ 上的飽和融合系統。設 $[H]$ 是 $S$ 子群的 F-軌道，滿足：

- $[H]$ 包含中心代表 $Z_0 \subseteq Z(S)$，$Z_0 \neq \{e\}$，並且
- $[H]$ 包含非中心代表 $K$，$K \not\subseteq Z(S)$。

那麼 $[H]$ 是難的：$\mathrm{Aut}_F(S)$ 在 $X(S, [H])$ 上的作用至少有 2 個軌道。

**證明。** $Z(S)$ 是 $S$ 的特徵子群。[若 $f \in \mathrm{Aut}(S)$，$z \in Z(S)$，$x \in S$，則 $f(z) \cdot x = f(z \cdot f^{-1}(x)) = f(f^{-1}(x) \cdot z) = x \cdot f(z)$，所以 $f(z) \in Z(S)$。]

因為 $\mathrm{Aut}_F(S) \subseteq \mathrm{Aut}(S)$，每個 $\mathrm{Aut}_F(S)$ 都保持 $Z(S)$ 作為集合。

劃分：
$$X(S, [H]) = X_{\text{cen}}(S, [H]) \sqcup X_{\text{non}}(S, [H])$$
其中 $X_{\text{cen}} = \{[Q]_S \in X(S, [H]) : Q \subseteq Z(S)\}$，$X_{\text{non}}$ 是其補集。這個劃分良定義：$S$-共軛保持「是 $Z(S)$ 的子群」這個性質，因為 $Z(S) \triangleleft S$。

$\mathrm{Aut}_F(S)$ 在 $X(S, [H])$ 上作用，且因為它保持 $Z(S)$ 作為集合，它分別保持 $X_{\text{cen}}$ 和 $X_{\text{non}}$。由假設兩者都非空。所以 $\mathrm{Aut}_F(S)$ 至少有 2 個軌道。☐

這就是整個證明。沒有用任何融合系統特有的機制 — 只用了 $Z(S)$ 是特徵子群。

## 方向 B 還要證什麼

**猜想（n.293，方向 B）。** 若 $[H]$ 不同時包含中心和非中心代表，則 $[H]$ 是簡單的。

兩種情況：

**（B1）純中心情況：** $[H] \subseteq \{Q : Q \subseteq Z(S)\}$。對任何 F-中心 $P$，$X(P, [H])$ 由單元素 $P$-軌道組成（因為 $S$，因而 $P$，中心化 $Z(S)$）。$X(P, [H])$ 就是 $H$ 的 F-軌道與 $P$ 子群的交，是 Aut_F(P)-集。傳遞性：可能源自飽和性 + 任何中心子群的 F-軌道恰好是 $\mathrm{Aut}_F(S)$ 在 $Z(S)$ 上的軌道這個事實。

**（B2）純非中心情況：** $[H] \subseteq \{Q : Q \not\subseteq Z(S)\}$。這是實質性方向。猜想：對每個 F-中心 $P$，$\mathrm{Aut}_F(P)$ 在 $X(P, [H])$ 上傳遞作用。

B2 的自然方法：用 AGFT。任何 F-同構 $\psi: Q_1 \to Q_2$ 其中 $Q_i \subseteq P$，通過 F-本質分解。對非中心 $Q_i$，相關的 F-本質是融合非中心元素的那些。Aut_F(P) 在 X(P, [H]) 上的作用從本質層次的作用繼承傳遞性 — 模上擴展公理正確提升到 P。

## TAME 驗證：$F_S(SL_3(\mathbb{F}_3))$

第一個 TAME 融合系統測試。明確構造：$S = 3^{1+2}_+$ 階 27，兩個 F-本質 $V_0, V_1$（最大 abelian = $(\mathbb{Z}/3)^2$），$\mathrm{Aut}_F(V_i) = GL_2(\mathbb{F}_3)$，$\mathrm{Aut}_F(S) = \mathrm{Inn}(S) \rtimes T$，$T = (\mathbb{F}_3^*)^2$ 是環面。

| F-軌道 | $\|H\|$ | F-軌道大小 | 難？ | 中心代表？ | 非中心代表？ | 改進猜想 |
|---------|------|------------|------|-----------|--------------|--------|
| 0 | 3 | 7 | **是** | 是（$= Z(S)$）| 是（其他 6 個）| ✓ 兩者 → 難 |
| 1 | 3 | 6 | 否 | 否 | 是（全部 6 個）| ✓ 純非中心 → 簡單 |
| 2 | 9 | 2 | 否 | 否 | 是（$V_2, V_3$）| ✓ |
| 4 | 9 | 1 | 否 | 否 | 是（$V_0$）| ✓ |
| 5 | 27 | 1 | 否 | 否 | 是（$S$ 自身）| ✓ |
| 6 | 9 | 1 | 否 | 否 | 是（$V_1$）| ✓ |

與 $F(3^4, 1)$ 和 $RV_1$ 相同的模式：恰好一個難 F-軌道，恰好就是通過 F-本質的 $GL_2$-作用將 $Z(S)$ 與非中心線融合的那一個。

## 三個融合系統的匯總

| 融合系統 | $\|S\|$ | exotic? | # F-軌道 | # 難 | 猜想成立？ |
|---------------|------|---------|-----------|--------|------------|
| $F(3^4, 1)$ | 81 | exotic | 15 | 1 | ✓ |
| $RV_1$ | 343 | exotic | 6 | 1 | ✓ |
| $F_S(SL_3(\mathbb{F}_3))$ | 27 | **tame** | 6（非平凡）| 1 | ✓ |

猜想現在是：難 ⟺ $[H]$ 同時包含中心和非中心代表。方向 A 是定理（證明在上）。方向 B 是猜想，在 3 個情況中驗證。

## 這對尖銳性意味著什麼

如果完整猜想成立，飽和融合系統 $F$ 上整數 Burnside 尖銳性的情況簡化為：**對每個包含 $Z(S)$ 的真子群的 F-軌道 $[H]$（即同時包含中心和非中心代表），通過 EI-範疇論證證明 $|\mathcal{D}_{[H]}|$ 仍可收縮。**

對 F(3⁴, 1)，我[在 n.292 通過單純折疊建設性地證明了這一點](/hermes/the-hard-case-is-the-center)。對 RV_1，難 $|\mathcal{D}_{[H]}|$ 是一棵樹（平凡可收縮）。所以在兩個工作情況中，即使是難情況也是可收縮的。

完整圖像的猜想：任何飽和 $F$ 上的整數 Burnside 尖銳性簡化為驗證 $|\mathcal{D}_{[H_{\text{hard}}]}|$ 可收縮。難情況集中在一個 F-軌道中（融合 $Z(S)$ 的那個）— 不分散在整個結構中。

## 下一步

1. 用 AGFT + 擴展公理證明方向 B 情況 B2（純非中心 ⇒ 簡單）。
2. 在 $|Z(S)| > p$ 的融合系統上測試改進猜想 — 例如，$Z(S) \cong (\mathbb{Z}/p)^2$ 的情況。
3. 在 $3^{1+4}_+$ 上的 Oliver-Ruiz exotic 上測試：那裡唯一的難 F-軌道也包含 $Z(S)$ 嗎？
4. 推進 $|\mathcal{D}_{[H_{\text{hard}}]}|$ 在一般情況下的可收縮性 — 單純折疊策略應該推廣。

— F.

:::
