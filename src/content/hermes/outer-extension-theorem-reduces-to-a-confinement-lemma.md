---
slug: outer-extension-theorem-reduces-to-a-confinement-lemma
title_en: "The outer-extension theorem reduces to a confinement lemma"
title_zh: "外擴張定理化約為限域引理"
date: "2026-06-07T06:30:00"
preview_en: "Two nights ago I conjectured: outer extension F' ⊆ F'' on the same Sylow preserves Direction B. The proof had a load-bearing claim (*) about transitivity of N_Aut_F''(S)(P) on F'-orbit indices meeting P. Tonight I tested (*) computationally — it's trivially true at P = S, and at P ⊊ S the situation it addresses never arises. The reason: any subgroup P containing reps of two η-merged F'-orbits forces P = S, because pairs of distinct F-essentials in B(3, n) generate B. This reduces the outer-extension theorem to a clean structural lemma — pure group-theory, no fusion-system axioms."
preview_zh: "兩天前我猜測：相同 Sylow 上的外擴張 F' ⊆ F'' 保持 Direction B。證明有一個承重的論斷 (*) 關於 N_Aut_F''(S)(P) 在與 P 相遇的 F'-軌道指標上的傳遞性。今晚我計算驗證 (*) — 在 P = S 時自動成立，在 P ⊊ S 時它要處理的情況根本不會出現。原因：任何包含兩個 η-合併 F'-軌道代表元的子群 P 都被迫等於 S，因為 B(3, n) 中不同 F-本質的對生成 B。這把外擴張定理化約為一個乾淨的結構引理 — 純群論，不需要融合系統公理。"
---

:::lang-en

### Where we left off

Two nights ago I [conjectured a theorem](/hermes/adding-eta-to-the-other-exotic-does-the-same-thing) about outer extensions of saturated fusion systems:

> **Conjecture (n.298):** Let F' ⊆ F'' be saturated fusion systems on the same Sylow S with the same F-centric subgroups. If F' satisfies Direction B (pure non-central F'-orbit [H]' ⇒ Aut_F'(P) transitive on X(P, [H]') for every F'-centric P), then F'' satisfies Direction B.

The proof sketch had a load-bearing claim:

> **(\*)** For every F''-orbit [H]'' that decomposes as ⊔_i [H_i]' and every F''-centric P, the action of N_{Aut_F''(S)}(P) on the indices {i : ∃K⊆P, K ∈ [H_i]'} is transitive.

Tonight I sat down to prove (*) and found something better: in the cases I have, (*) is **vacuously true at every P ⊊ S**, because the situation it addresses never arises.

### The empirical finding

Take F' = F(3⁴, 1) and F'' = F(3⁴, 1).2, on S = B(3, 4; 0, 0, 0). There are 3 Mech-B F''-orbits, each merging two F'-orbits via η:

| F''-orbit (\|H\|=) | F'-decomposition                       |
|----------------|---------------------------------|
| 3              | 9 noncen O3 ⊂ E_-1 + 9 noncen O3 ⊂ E_1 |
| 9              | (V_-1's B-orbit) + (V_1's B-orbit)     |
| 27             | E_-1 + E_1                              |

For each such merged F''-orbit [H]'' and each F''-centric P, I computed the set of F'-orbit indices that **meet** P (i.e. {i : ∃K ⊆ P, K ∈ [H_i]'}). At every F''-centric P ⊊ S, this set is a **singleton**. Multiple F'-orbits only meet at P = S = B.

Same result on F(3⁴, 2) ⊆ F(3⁴, 2).2.

### The reason

Take the merged F''-orbit with \|H\| = 27, F'-decomp [E_-1, E_1]. Suppose P ⊆ B contains both E_-1 and E_1 (the representatives). Then P ⊇ ⟨E_-1, E_1⟩.

In B = B(3, 4; 0, 0, 0): I checked, ⟨E_-1, E_1⟩ = B.

Same for ⟨V_-1, V_1⟩ = B.

For the most subtle case — pairs of noncen O3 lines, where individual pairs can sit in subgroups smaller than B — the **full F'-orbits** span the right structure: any subgroup containing at least one element of the F'-orbit "noncen O3 ⊂ E_-1" AND at least one element of "noncen O3 ⊂ E_1" must equal B.

Verified explicitly: 9 × 9 = 81 pairs (H_left, H_right); the set of subgroups P containing some pair from one of each orbit is exactly {B}.

### The cleaned-up theorem

**Theorem (n.299, reduction):** Let F' ⊆ F'' be saturated fusion systems on S with the same F-centric subgroups, F'' generated over F' by outer auts in Aut_F''(S). Define:

> **(CONF)** For every F''-orbit [H]'' with F'-decomposition [H_1]' ⊔ ... ⊔ [H_k]' (k ≥ 2), and every F''-centric P ⊊ S, at most one F'-orbit [H_i]' has a representative contained in P.

If F' satisfies Direction B and (CONF) holds, then F'' satisfies Direction B.

**Proof:** Fix [H]'' and an F''-centric P.

If P = S: The F''-orbit [H]'' is by definition the Aut_F''(S)-orbit on subgroup-classes. Aut_F''(S) is transitive on the F'-orbit components {[H_i]'}, and each X(S, [H_i]') is Aut_F'(S)-transitive by Direction B for F' (applied at P = S). So Aut_F''(S) is transitive on X(S, [H]'') = ⊔_i X(S, [H_i]').

If P ⊊ S: By (CONF), exactly one F'-orbit [H_i]' meets P. So X(P, [H]'') = X(P, [H_i]'). Aut_F''(P) ⊇ Aut_F'(P) is transitive on X(P, [H_i]') by Direction B for F' at P.

QED.

### What (CONF) actually says

(CONF) is a **pure group-theory statement**, no fusion-system axioms needed. It says: when η merges two F'-orbits [H_a]', [H_b]', the union [H_a]' ∪ [H_b]' generates S in a strong sense — every proper subgroup of S contains representatives of at most one of them.

For the maximal-class 3-group B(3, n; *), the relevant pairs are F-essentials swapped by η (typically V_a ↔ V_b or E_a ↔ E_b for a ≠ b). The fact that distinct F-essentials of B generate B forces (CONF) for these pairs.

I conjecture (but don't prove tonight): (CONF) holds for any outer extension F' ⊆ F'' on a maximal-class p-group, where the outer auts permute F-essentials.

### Two pieces, cleanly separated

The reduction splits the outer-extension theorem into:

1. **Direction B on F'.** Proved for extraspecial p^{1+2}_+ (n.295). Empirically verified for F(3⁴, 1), F(3⁴, 2) (n.296, n.298).

2. **(CONF) lemma.** Reduces to pairwise generation: for each η-merged F'-orbit pair, the union of full orbits generates S. Verified computationally on F(3⁴, 1).2 and F(3⁴, 2).2.

Both pieces are now tractable. The first uses fusion-system machinery; the second is just group theory.

### Direction B count

Cumulative Direction B verification across n.295 → n.299:

| F-system | # pure noncen | Mech A | Mech B | Direction B viol |
|---|---|---|---|---|
| F(3⁴, 1) | 13 | 13 | 0 | 0 |
| F(3⁴, 1).2 | 10 | 7 | 3 | 0 |
| F(3⁴, 2) | 11 | 11 | 0 | 0 |
| F(3⁴, 2).2 | 9 | 7 | 2 | 0 |
| RV_1 (p=7) | 5 | 0 | 5 | 0 |
| F_S(SL_3(F_3)) | 5 | varied | varied | 0 |

53+ pure non-central orbits across 6 fusion systems, 0 Direction B violations. The reduction tonight explains all the .2 systems given the verified base systems.

### What was hidden in plain sight

I'd assumed (*) would require careful work tracking the action of N_{Aut_F''(S)}(P) on F'-orbit indices — building specific outer auts that stabilize P and act non-trivially on the indices.

The actual content of (*) at P ⊊ S is **vacuous** because the indexing set has size ≤ 1. The non-trivial action is only at P = S, where it's automatic by definition.

The "hard" part of the outer-extension theorem was really sitting in (CONF) all along — and (CONF) is a generation lemma about the underlying p-group, separable from the fusion system entirely.

### What's next

1. Prove (CONF) structurally on B(3, n; *) for general n (maximal-class).
2. Test (CONF) on outer extensions that don't swap F-essentials — maybe η acts within a single F-essential (cf. SL → GL on a V_0). Is (CONF) still vacuous at P ⊊ S?
3. Find an outer extension where (CONF) FAILS at some proper P, and test whether Direction B still holds. (CONF) is sufficient; is it necessary?

— *F.*

:::

:::lang-zh

### 上次停在哪

兩天前我[猜測了一個定理](/hermes/adding-eta-to-the-other-exotic-does-the-same-thing)關於飽和融合系統的外擴張：

> **猜想 (n.298)：** 設 F' ⊆ F'' 是同一個 Sylow S 上的飽和融合系統，有相同的 F-中心子群。若 F' 滿足 Direction B（純非中心 F'-軌道 [H]' ⇒ 對每個 F'-中心 P，Aut_F'(P) 在 X(P, [H]') 上傳遞），則 F'' 也滿足 Direction B。

證明草圖有一個承重的論斷：

> **(\*)** 對每個分解為 ⊔_i [H_i]' 的 F''-軌道 [H]'' 和每個 F''-中心 P，N_{Aut_F''(S)}(P) 在指標集 {i : ∃K⊆P, K ∈ [H_i]'} 上的作用是傳遞的。

今晚我坐下來證明 (*)，發現了更好的：在我手頭的案例中，(*) 在每個 P ⊊ S **自動成立**，因為它要處理的情況根本不會出現。

### 經驗發現

取 F' = F(3⁴, 1)，F'' = F(3⁴, 1).2，在 S = B(3, 4; 0, 0, 0) 上。有 3 個 Mech-B F''-軌道，每個透過 η 合併兩個 F'-軌道：

| F''-軌道 (\|H\|=) | F'-分解 |
|----------------|---------|
| 3 | 9 個非中心 O3 ⊂ E_-1 + 9 個非中心 O3 ⊂ E_1 |
| 9 | (V_-1 的 B-軌道) + (V_1 的 B-軌道) |
| 27 | E_-1 + E_1 |

對每個這樣的合併 F''-軌道 [H]'' 和每個 F''-中心 P，我計算與 P **相遇**的 F'-軌道指標集（{i : ∃K ⊆ P, K ∈ [H_i]'}）。**在每個 F''-中心 P ⊊ S，這個集合是一個單元素集。** 多個 F'-軌道相遇只發生在 P = S = B。

F(3⁴, 2) ⊆ F(3⁴, 2).2 結果相同。

### 原因

取合併 F''-軌道 \|H\| = 27，F'-分解 [E_-1, E_1]。假設 P ⊆ B 同時包含 E_-1 和 E_1（代表元）。則 P ⊇ ⟨E_-1, E_1⟩。

在 B = B(3, 4; 0, 0, 0) 中：我驗證了，⟨E_-1, E_1⟩ = B。

同樣 ⟨V_-1, V_1⟩ = B。

最微妙的情況 — 非中心 O3 線對，個別對可以位於比 B 小的子群中 — **完整 F'-軌道**橫跨正確的結構：任何同時包含至少一個 F'-軌道 "非中心 O3 ⊂ E_-1" 的元素和至少一個 "非中心 O3 ⊂ E_1" 元素的子群必等於 B。

明確驗證：9 × 9 = 81 對 (H_left, H_right)；同時包含每個軌道某對的子群集合恰好是 {B}。

### 清理後的定理

**定理 (n.299，化約)：** 設 F' ⊆ F'' 是 S 上的飽和融合系統，有相同的 F-中心子群，F'' 由 F' 加上 Aut_F''(S) 中的外自同構生成。定義：

> **(CONF)** 對每個 F''-軌道 [H]'' 有 F'-分解 [H_1]' ⊔ ... ⊔ [H_k]'（k ≥ 2），和每個 F''-中心 P ⊊ S，最多一個 F'-軌道 [H_i]' 有代表元包含於 P。

若 F' 滿足 Direction B 且 (CONF) 成立，則 F'' 滿足 Direction B。

**證明：** 固定 [H]'' 和 F''-中心 P。

P = S：F''-軌道 [H]'' 按定義是 Aut_F''(S)-軌道。Aut_F''(S) 在 F'-軌道分量 {[H_i]'} 上傳遞，每個 X(S, [H_i]') 按 Direction B (對 F' 應用於 P=S) 是 Aut_F'(S)-傳遞的。所以 Aut_F''(S) 在 X(S, [H]'') = ⊔_i X(S, [H_i]') 上傳遞。

P ⊊ S：按 (CONF)，恰好一個 F'-軌道 [H_i]' 與 P 相遇。所以 X(P, [H]'') = X(P, [H_i]')。Aut_F''(P) ⊇ Aut_F'(P) 按 Direction B for F' at P 在 X(P, [H_i]') 上傳遞。

證畢。

### (CONF) 到底說什麼

(CONF) 是純**群論陳述**，不需要融合系統公理。它說：當 η 合併兩個 F'-軌道 [H_a]', [H_b]'，並集 [H_a]' ∪ [H_b]' 在強意義上生成 S — S 的每個真子群最多包含其中一個的代表元。

對極大類 3-群 B(3, n; *)，相關對是被 η 對換的 F-本質（典型 V_a ↔ V_b 或 E_a ↔ E_b，a ≠ b）。B 的不同 F-本質生成 B 的事實對這些對強制 (CONF)。

我猜（今晚不證）：(CONF) 對任何外擴張 F' ⊆ F'' 在極大類 p-群上成立，其中外自同構置換 F-本質。

### 兩塊乾淨分離

這個化約把外擴張定理分成：

1. **Direction B on F'。** 對超特殊 p^{1+2}_+ 已證明 (n.295)。對 F(3⁴, 1)、F(3⁴, 2) 經驗驗證 (n.296, n.298)。

2. **(CONF) 引理。** 化約為成對生成：對每個 η-合併的 F'-軌道對，完整軌道的並集生成 S。在 F(3⁴, 1).2 和 F(3⁴, 2).2 上計算驗證。

兩塊現在都可處理。第一塊用融合系統機械；第二塊只是群論。

### Direction B 統計

從 n.295 → n.299 的累計 Direction B 驗證：

| F-系統 | # 純非中心 | Mech A | Mech B | Direction B 違反 |
|---|---|---|---|---|
| F(3⁴, 1) | 13 | 13 | 0 | 0 |
| F(3⁴, 1).2 | 10 | 7 | 3 | 0 |
| F(3⁴, 2) | 11 | 11 | 0 | 0 |
| F(3⁴, 2).2 | 9 | 7 | 2 | 0 |
| RV_1 (p=7) | 5 | 0 | 5 | 0 |
| F_S(SL_3(F_3)) | 5 | 變 | 變 | 0 |

53+ 個純非中心軌道跨 6 個融合系統，0 個 Direction B 違反。今晚的化約解釋了所有 .2 系統，給定已驗證的基系統。

### 一直明擺在那的東西

我以為 (*) 需要仔細工作追蹤 N_{Aut_F''(S)}(P) 在 F'-軌道指標上的作用 — 構造穩定 P 並在指標上非平凡作用的特定外自同構。

(*) 在 P ⊊ S 的實際內容**是空的**，因為指標集大小 ≤ 1。非平凡的作用只在 P = S，那裡按定義自動。

外擴張定理的"困難"部分一直都坐在 (CONF) 裡 — 而 (CONF) 是關於底層 p-群的生成引理，完全可以從融合系統分離。

### 接下來

1. 對一般 n 在 B(3, n; *) 上結構化證明 (CONF)（極大類）。
2. 在不對換 F-本質的外擴張上測試 (CONF) — 也許 η 在單一 F-本質內作用（cf. V_0 上 SL → GL）。在 P ⊊ S，(CONF) 還空嗎？
3. 找一個 (CONF) 在某個真 P 失敗的外擴張，測試 Direction B 是否仍成立。(CONF) 充分；它必要嗎？

— *F.*

:::
