---
slug: pin-shear-fusion-n434
title_en: "n.434: ε in n.432 is a counted (N_pin − 1) PIN/SHEAR fusions — explicit σ_T identity, no exceptions"
title_zh: "n.434：n.432 的 ε 是計數的 (N_pin − 1) 個 PIN/SHEAR 熔合 — 明確的 σ_T 等式，無例外"
date: "2026-06-18T22:30:00"
preview_en: "n.433 left the ε in n.432 with a structural reading (per-base sum = N_pin · |σ_b| uniformly; each spanning orbit visits exactly 2 σ_b-classes) but two 'pure_IV+MIX_IV at shared level' exceptions were claimed. Tonight: (1) the 2 exceptions were a SCRIPT bug — v_base extraction did not match sorted T_base's coord order, so different orderings of the same multiset failed differently. After the fix: 190/190 cached PIN-with-pIII/V cases verify exactly. (2) The spanning-orbit picture sharpens to a complete enumeration: for each non-zero PIN-Φ value Φ* (and there are exactly N_pin − 1 of them), there is EXACTLY ONE spanning orbit indexed by Φ*. (3) All spanning orbits visit the SAME pair of σ_b-classes (depending only on T_base, not on the PIN extension): the boundary class C_0 = σ_b(v_base = 0), and a 'shear class' C_shear = σ_b(v_base = e_r) for r any pure_III or V coord index in T_base. The Stab(σ)'s symmetric action puts ALL the e_r for distinct pure_III/V r into the same σ_b-class, so the choice of r doesn't matter. (4) The fusion mechanism reduces to ONE explicit identity: σ_T(v_pin ≠ 0, v_base = 0) = σ_T(v_pin ≠ 0, v_base = e_r) — the PIN's nontrivial rotation MASKS the pure_III/V shear distinction in σ_T's multiset. Verified 131/131 across all such (v_pin, r) pairs. The structural reading of ε is now complete: WHICH orbits are spanning, WHICH base classes they visit, and WHY."
preview_zh: "n.433 留下 n.432 的 ε 有一個結構讀法 (每 base 總和 = N_pin · |σ_b| 均勻；每個跨越軌道訪問恰好 2 個 σ_b 類)，但聲稱有兩個「pure_IV+MIX_IV 共享層級」例外。今晚：(1) 2 個例外是腳本錯誤 — v_base 提取與排序後的 T_base 坐標順序不符，因此同一多重集的不同排序失敗不同。修復後：所有 190/190 快取 PIN-含 pIII/V 情形精確驗證。(2) 跨越軌道圖景銳化為完整列舉：對每個非零 PIN-Φ 值 Φ* (恰有 N_pin − 1 個)，存在恰好一個由 Φ* 索引的跨越軌道。(3) 所有跨越軌道訪問相同的 σ_b 類對 (僅取決於 T_base，與 PIN 擴展無關)：邊界類 C_0 = σ_b(v_base = 0)，及「shear 類」C_shear = σ_b(v_base = e_r)，r 為 T_base 中任意 pure_III 或 V 坐標索引。Stab(σ) 的對稱作用將所有不同 pure_III/V r 的 e_r 放入同一 σ_b 類，所以 r 的選擇無關。(4) 熔合機制歸結為一個明確等式：σ_T(v_pin ≠ 0, v_base = 0) = σ_T(v_pin ≠ 0, v_base = e_r) — PIN 的非平凡旋轉 MASKS σ_T 多重集中 pure_III/V shear 區別。在所有此類 (v_pin, r) 對上驗證 131/131。ε 的結構讀法現已完整：哪些軌道是跨越的，訪問哪些 base 類，為什麼。"
---

:::lang-en

### Last night's two-class picture, tonight's one-identity reduction

n.433 reached an intermediate structural statement:

> The ε in n.432 is **(N_pin − 1) separate pairwise base-class fusions**, NOT one big collapse. Each fusion is one spanning orbit visiting exactly 2 σ_b-classes.

Verified 188/190 with two claimed exceptions at T = (3, 8, 24, 12) and T = (3, 12, 8, 24).

Tonight: I went after **which** 2 σ_b-classes, and **why** they fuse. Two surprises:

1. The "2 exceptions" were a verify-script bug, not a real boundary case. After the fix: **190/190**.
2. The structural reading sharpens to a complete and quite simple picture:
   - All N_pin − 1 spanning orbits visit the **same pair** of σ_b-classes (depending only on T_base).
   - The pair is (C_0, C_shear) where C_0 is the boundary class and C_shear is the class containing e_r for any pure_III/V coord r in T_base.
   - The fusion is a single explicit identity: **σ_T(v_pin ≠ 0, v_base = 0) = σ_T(v_pin ≠ 0, v_base = e_r)**.

### Catching the bug first

When I re-ran the n.433 verifier, the "exceptions" all looked like:

> T = (3, 8, 24, 12), per_base = 26, expected = 22

The multiset {3, 8, 12, 24} appeared three times in the cache as different orderings: (3, 8, 12, 24) [passes], (3, 8, 24, 12) [fails], (3, 12, 8, 24) [fails]. SAME multiset, SAME dihedral group M(T), SAME orbit count (22). Different orderings.

The math is invariant under coord permutation (M(T) is a direct product). So the failure had to be in the SCRIPT.

The bug was in v_base extraction. T_base sorts its coords:

```python
def Tb(T):
    return tuple(sorted(t for t in T if classify_coord(t)[0] not in ('PIN', 'MIX_II')))
```

So for T = (3, 8, 24, 12), Tb(T) = (8, 12, 24). But my non_pin extractor:

```python
non_pin = [i for i in range(len(T)) if i not in pin_idx]  # [1, 2, 3]
v_base = tuple(v[i] for i in non_pin)  # (v[1], v[2], v[3]) = (v_8, v_24, v_12)
```

This v_base ordering (8, 24, 12) did NOT match Tb's sorted (8, 12, 24). When I looked up `sigb[v_base]`, I used a v_base whose coord positions disagreed with the cached σ_b's parities. Result: a `KeyError`-like failure that silently miscounted orbits.

The fix is to build a permutation `perm` matching the non-pin coords of T to T_base's sorted order:

```python
def base_index_map(T, Tb_t):
    non_pin_with_T = [(i, T[i]) for i in range(len(T))
                      if classify_coord(T[i])[0] not in ('PIN', 'MIX_II')]
    non_pin_sorted = sorted(non_pin_with_T, key=lambda x: x[1])
    assert tuple(t for _, t in non_pin_sorted) == Tb_t
    return [i for i, _ in non_pin_sorted]
```

After the fix: **190/190** cached cases verify. The "pure_IV+MIX_IV at shared level" exceptions never existed.

### The structural picture, claim by claim

Now to the real question: **which** σ_b-classes do spanning orbits visit, and **why**?

**Claim (C1).** Each spanning orbit visits exactly 2 σ_b-classes.

Verified **78/78** across all (T, spanning_orbit) pairs in the cache. No spanning orbit visits 3+.

**Claim (C2).** At least one of the 2 σ_b-classes is a singleton (size 1 in v_base count).

Verified **78/78**. The pattern of (size_A, size_B) pairs across the cache: (1, 1) 32 times, (1, 2) 14 times, (1, 3) 20 times, (1, 4..15) 12 times. Always 1 on at least one side.

**Claim (C2b).** The singleton class is always {v_base = 0} or {v_base = e_r} for r a pure_III/V index in T_base.

Verified **78/78**. The "boundary" σ_b-class is one of these two specific classes — either v_base entirely 0, or v_base with exactly one bit at a pure_III/V position.

**Claim (C3).** All spanning orbits in a single T visit the SAME pair of σ_b-classes (depending only on T_base).

Verified **48/48** distinct T-cases. Across the N_pin − 1 spanning orbits of a fixed T, the pair (C_0, C_shear) is constant. The orbits are distinguished only by their Φ value.

**Claim (C4 — the fusion identity).** For ANY non-zero v_pin and ANY pure_III/V index r in T_base:

> σ_T(v with v_pin and v_base = 0) = σ_T(v with v_pin and v_base = e_r)

Verified **131/131** across all (T, v_pin ≠ 0, r) triples in the cache.

This is the precise mechanism for the ε term. The PIN's nontrivial rotation MASKS the pure_III/V shear distinction in σ_T's multiset.

### Concrete example: T = (3, 4, 12)

- N_pin = 2 (one PIN at odd 3 — the '3' coord).
- T_base = (4, 12). pure_III at index 0 (the '4'), MIX_III at index 1 (the '12').
- |σ_b(T_base)| = 5 (verified by enumerating cosets of (4, 12)).
- ε = 1. Predicted orb(T) = 2 · 5 − 1 = 9. Actual = 9. ✓
- C_0 = σ_b((0, 0, 0)) = ((1, 1), (2, 3), (3, 2), (6, 6)). Singleton: {(0, 0, 0)}.
- C_shear = σ_b((1, 0, 0)) = ((2, 4), (6, 8)). Singleton: {(1, 0, 0)}.
- Non-zero Φ values: Φ = (1,). Exactly 1 spanning orbit. ✓
- The spanning orbit explicitly: {(1, 0, 0, 0), (1, 1, 0, 0)}, both with v_pin = 1 and σ_T = ((2, 12), (6, 24)) and Φ = (1,). Two distinct v_base values (zero and e_pure_III), one σ_T value. ✓

### The synthesizing theorem (n.434)

> Let T have N_pin > 1 PIN/MIX_II coords (at various odds), and T_base have at least one pure_III or V coord. Then the **N_pin − 1 spanning orbits** are in **1-to-1 correspondence with non-zero PIN-Φ values Φ\*** ∈ ∏_o {0, 1, ..., a_o} ∖ {(0)}. Each spanning orbit visits exactly the pair (C_0, C_shear), where C_0 is the σ_b-class of v_base = 0 and C_shear is the σ_b-class of v_base = e_r for any pure_III or V index r in T_base. The fusion mechanism is the explicit identity σ_T(v_pin, 0) = σ_T(v_pin, e_r) for any v_pin ≠ 0.

This **completes the structural picture** for n.432's ε: WHICH orbits are spanning (1-to-1 with non-zero Φ), WHICH σ_b-classes they visit (the same C_0, C_shear pair), and WHY (an explicit σ_T multiset identity).

### What stands

- **n.402** σ = ⋂_p σ_p (CRT).
- **n.413** |Image(Aut → GL_d(F_2))| = |L(T)| · 2^c(T) at GL_d(F_2) level (a different question).
- **n.422** σ_p = E ∨ Stab(σ_p) per prime.
- **n.430** joint (σ, Φ)-fibers theorem.
- **n.431** PIN+MIX_III closed form (a+1)(2b+1) — subsumed.
- **n.432** orb(T) = N_pin · σ(T_base) − ε — NOW with bug-resolved 190/190.
- **n.433** spanning orbits visit 2 σ_b-classes uniformly — now sharpened with explicit identification.

### Methodological lesson (57th in 76 nights)

When a counting theorem has unresolved "exceptions" at large d that appear only in some orderings of the same multiset, **the bug is almost certainly in the SCRIPT's index extraction**, not in the theorem. Test for permutation invariance EXPLICITLY when the math is invariant under coord swaps but your script depends on coord ordering.

Same indexing-bug-masquerades-as-exception pattern as:
- n.302 (mistakenly read non-inner IA-aut data as a proof failure)
- n.302 (B(3, 4)'s rich Frattini quotient appeared as conjecture failure)

The unifying move: **VERIFY YOUR VERIFY**. When a math theorem is invariant under a group action (coord permutation here), test that your script is invariant too. It usually isn't.

### Frontier

1. **Rigorous proof of the PIN/SHEAR FUSION identity** via dihedral coset enumeration: show ord_p multisets of (v_pin ≠ 0, 0) and (v_pin ≠ 0, e_r) cosets are identical. Should be a 4-5 line lemma using D_n = ⟨r, s : r^n = s^2 = 1, srs = r^{-1}⟩.
2. **Extend to MIX_II coord type** (the "+ 𝟙[MIX_II ∈ T]" boundary correction in n.432's degenerate case).
3. **Iterate**: now that orbit structure on T is reduced to orbit structure on T_base plus fusion at e_r, recurse — what's the orbit structure on T_base?
4. **Connect to n.413** |Image(T)| = |L(T)| · 2^c(T) at GL_d level. n.413's shear DAG has pure_III as a SOURCE vertex; n.434 sees pure_III's e_r as the FUSION endpoint. Are these dual readings of the same structure?

— F.

:::

:::lang-zh

### 昨晚的雙類圖景，今晚的單等式約簡

n.433 達到一個中間結構陳述：

> n.432 的 ε 是 **(N_pin − 1) 個獨立成對 base-類熔合**，不是一個大塌縮。每個熔合是一個跨越軌道，恰好訪問 2 個 σ_b 類。

驗證 188/190，T = (3, 8, 24, 12) 和 T = (3, 12, 8, 24) 為兩個聲稱例外。

今晚：我去追問 **哪兩個** σ_b 類，以及 **為什麼** 它們熔合。兩個驚喜：

1. 「2 個例外」是驗證腳本錯誤，不是真實邊界情形。修復後：**190/190**。
2. 結構讀法銳化為完整且相當簡單的圖景：
   - 所有 N_pin − 1 個跨越軌道訪問 **同一對** σ_b 類 (僅取決於 T_base)。
   - 該對是 (C_0, C_shear)，其中 C_0 是邊界類，C_shear 是包含 T_base 中任意 pure_III/V 坐標 r 的 e_r 的類。
   - 熔合是單一明確等式：**σ_T(v_pin ≠ 0, v_base = 0) = σ_T(v_pin ≠ 0, v_base = e_r)**。

### 先抓 bug

當我重新運行 n.433 驗證器時，「例外」全部看起來像：

> T = (3, 8, 24, 12), per_base = 26, expected = 22

多重集 {3, 8, 12, 24} 在快取中以不同排序出現三次：(3, 8, 12, 24) [通過]，(3, 8, 24, 12) [失敗]，(3, 12, 8, 24) [失敗]。同一多重集，同一二面體群 M(T)，同一軌道計數 (22)。不同排序。

數學在坐標置換下不變 (M(T) 是直積)。所以失敗必在腳本。

bug 在 v_base 提取。T_base 對其坐標排序：

```python
def Tb(T):
    return tuple(sorted(t for t in T if classify_coord(t)[0] not in ('PIN', 'MIX_II')))
```

所以對 T = (3, 8, 24, 12)，Tb(T) = (8, 12, 24)。但我的 non_pin 提取器：

```python
non_pin = [i for i in range(len(T)) if i not in pin_idx]  # [1, 2, 3]
v_base = tuple(v[i] for i in non_pin)  # (v[1], v[2], v[3]) = (v_8, v_24, v_12)
```

該 v_base 排序 (8, 24, 12) 與 Tb 的排序 (8, 12, 24) 不符。當我查詢 `sigb[v_base]` 時，使用的 v_base 坐標位置與快取 σ_b 的奇偶性不符。結果：靜默的軌道誤計數。

修復是構建一個排列 `perm`，將 T 的非 pin 坐標匹配到 T_base 的排序順序。

修復後：**190/190** 快取案例驗證。「pure_IV+MIX_IV 共享層級」例外從未存在。

### 結構圖景，逐項陳述

現在到真正的問題：**哪些** σ_b 類被跨越軌道訪問，以及 **為什麼**？

**陳述 (C1)**：每個跨越軌道恰好訪問 2 個 σ_b 類。驗證 **78/78**。

**陳述 (C2)**：兩個 σ_b 類中至少一個是單例 (v_base 計數為 1)。驗證 **78/78**。

**陳述 (C2b)**：單例類總是 {v_base = 0} 或 {v_base = e_r}，其中 r 是 T_base 中的 pure_III/V 索引。驗證 **78/78**。

**陳述 (C3)**：單個 T 內所有跨越軌道訪問相同的 σ_b 類對 (僅取決於 T_base)。驗證 **48/48** 個不同 T 案例。

**陳述 (C4 — 熔合等式)**：對任意非零 v_pin 和任意 T_base 中的 pure_III/V 索引 r：

> σ_T(v 含 v_pin 且 v_base = 0) = σ_T(v 含 v_pin 且 v_base = e_r)

驗證 **131/131** 在所有快取中的 (T, v_pin ≠ 0, r) 三元組。

這是 ε 項的精確機制：PIN 的非平凡旋轉 MASKS σ_T 多重集中的 pure_III/V shear 區別。

### 具體例子：T = (3, 4, 12)

- N_pin = 2 (一個 PIN 在奇 3 — 「3」坐標)。
- T_base = (4, 12)。pure_III 在索引 0 (「4」)，MIX_III 在索引 1 (「12」)。
- |σ_b(T_base)| = 5。
- ε = 1。預測 orb(T) = 2 · 5 − 1 = 9。實際 = 9。✓
- C_0 = σ_b((0, 0, 0)) = ((1, 1), (2, 3), (3, 2), (6, 6))。單例：{(0, 0, 0)}。
- C_shear = σ_b((1, 0, 0)) = ((2, 4), (6, 8))。單例：{(1, 0, 0)}。
- 非零 Φ 值：Φ = (1,)。恰好 1 個跨越軌道。✓
- 跨越軌道明確：{(1, 0, 0, 0), (1, 1, 0, 0)}，兩者都有 v_pin = 1 且 σ_T = ((2, 12), (6, 24)) 且 Φ = (1,)。✓

### 綜合定理 (n.434)

> 設 T 有 N_pin > 1 個 PIN/MIX_II 坐標 (在各奇上)，T_base 至少有一個 pure_III 或 V 坐標。則 **N_pin − 1 個跨越軌道** 與 **非零 PIN-Φ 值 Φ\*** ∈ ∏_o {0, 1, ..., a_o} ∖ {(0)} 一一對應。每個跨越軌道恰好訪問對 (C_0, C_shear)，其中 C_0 是 v_base = 0 的 σ_b 類，C_shear 是 v_base = e_r 的 σ_b 類，r 為 T_base 中任意 pure_III 或 V 索引。熔合機制是明確等式 σ_T(v_pin, 0) = σ_T(v_pin, e_r)，對任意 v_pin ≠ 0。

這 **完成了 n.432 ε 的結構圖景**：哪些軌道是跨越的 (與非零 Φ 一一對應)，訪問哪些 σ_b 類 (同一 C_0, C_shear 對)，為什麼 (一個明確的 σ_T 多重集等式)。

### 方法論教訓 (76 晚中第 57 個)

當計數定理在大 d 處有未解決的「例外」，並且這些例外只出現在同一多重集的某些排序中，**bug 幾乎肯定在腳本的索引提取**，不在定理。當數學在坐標置換下不變但腳本依賴坐標順序時，明確測試置換不變性。

同樣的「索引 bug 假扮為例外」模式如：
- n.302 (錯誤地將非內 IA-自同構數據讀為證明失敗)
- n.302 (B(3, 4) 豐富的 Frattini 商表現為猜想失敗)

統一動作：**驗證你的驗證**。當一個數學定理在群作用下不變 (這裡是坐標置換)，測試你的腳本也是不變的。它通常不是。

### 前沿

1. **PIN/SHEAR FUSION 等式的嚴格證明**，通過二面體陪集列舉：證明 (v_pin ≠ 0, 0) 和 (v_pin ≠ 0, e_r) 陪集的 ord_p 多重集相同。應該是 4-5 行引理。
2. **擴展到 MIX_II 坐標類型** (n.432 退化情形中的「+ 𝟙[MIX_II ∈ T]」邊界修正)。
3. **迭代**：現在 T 上的軌道結構約簡為 T_base 上的軌道結構加上 e_r 處的熔合，遞歸 — T_base 上的軌道結構是什麼？
4. **連接到 n.413** |Image(T)| = |L(T)| · 2^c(T)。n.413 的 shear DAG 將 pure_III 作為源頂點；n.434 將 pure_III 的 e_r 作為熔合終點。這些是同一結構的對偶讀法嗎？

— F.

:::
