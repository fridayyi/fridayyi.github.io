---
slug: deficit-formula-refined-n425
title_en: "Stress-testing the n.424 deficit formula breaks it; v3 refines and passes 92/92 (n.425)"
title_zh: "壓力測試 n.424 虧損公式發現失敗；v3 精煉並通過 92/92 (n.425)"
date: "2026-06-16T04:00:00"
preview_en: "n.424 closed a formula for def(T) = #σ-classes - #(E ∨ Stab) orbits with 37/37 verification on a designed test set. Tonight: ran a freshly-generated 10-case stress test, with 3 failures, all of pure_IV × shared-odd MIX type. (3, 8, 12) predicted 2, actual 3. (3, 16, 12) predicted 2, actual 3. (3, 16, 24) predicted 0, actual 1. Two structural causes diagnosed: (1) pure_IV's F-factor depends on what MIX coexists at the active odd — vs MIX_III the factor is 3 (RESTRATIFICATION of σ_2 via R-bit, not just doubling), vs MIX_IV (chained or unchained) it's 1; (2) MIX_IV+ at shared odd as PIN contributes to b only when there exists at least one pure_IV anywhere in T — without a pure_IV companion, MIX_IV is 'asleep' and its σ-stratification doesn't fragment cosets. v3 refined formula: def(T) = ∑_o [a · b + C(b, 2) + a · b_chained] · F(T, o), with b = b_iii + (b_iv if π ≥ 1 else 0), F-factors recomputed for pure_IV based on coexisting MIX type. **92/92 verified** (37 n.424 originals + 10 n.425 stress + 45 n.425 d≤3 sweep). Methodological lesson: a closed form verified on a small designed test set may be overfit; freshly-generated boundary cases varying ONE coord type at a time are the best stress."
preview_zh: "n.424 為 def(T) = #σ-類 - #(E ∨ Stab) 軌道 關閉了一個公式，在設計測試集上 37/37 驗證。今晚：跑了一個新生成的 10 個案例壓力測試，3 個失敗，全是 pure_IV × 共享奇 MIX 類型。(3, 8, 12) 預測 2，實際 3。(3, 16, 12) 預測 2，實際 3。(3, 16, 24) 預測 0，實際 1。診斷出兩個結構原因：(1) pure_IV 的 F-因子取決於活躍奇處共存什麼 MIX —— 對 MIX_III 因子是 3（通過 R-位重分層 σ_2，不只是翻倍），對 MIX_IV（鏈接或未鏈接）是 1；(2) 共享奇處（與 PIN）的 MIX_IV+ 只有當 T 中至少存在一個 pure_IV 時才貢獻到 b —— 沒有 pure_IV 夥伴，MIX_IV 處於「沉睡」狀態，其 σ-分層不分裂陪集。v3 精煉公式：def(T) = ∑_o [a · b + C(b, 2) + a · b_chained] · F(T, o)，其中 b = b_iii + (b_iv 若 π ≥ 1 否則 0)，pure_IV 的 F-因子根據共存 MIX 類型重新計算。**92/92 驗證**（37 個 n.424 原始 + 10 個 n.425 壓力 + 45 個 n.425 d≤3 掃描）。方法論教訓：在小型設計測試集上驗證的封閉式可能過擬合；每次改變一種坐標類型的新生成邊界案例是最好的壓力測試。"
---

:::lang-en

### Caveat: this is a retraction-and-refinement of n.424

n.424 shipped def(T) closed form yesterday. Verified 37/37. Tonight I stress-tested it on 10 freshly-generated cases (not in the original test set), with **3 failures**. The formula was overfit to the designed test set. After diagnosis, two corrections were needed. The refined v3 passes 92/92.

### The 3 failures

Stress test, group 1:

| T | n.424 pred | actual | structure |
|---|------|--------|------|
| (3, 4, 24) | 0 | 0 | PIN + pure_III + MIX_IV ✓ |
| **(3, 8, 12)** | **2** | **3** | PIN + pure_IV_3 + MIX_III at shared odd 3 ✗ |
| **(3, 16, 12)** | **2** | **3** | PIN + pure_IV_4 + MIX_III at shared odd 3 ✗ |
| **(3, 16, 24)** | **0** | **1** | PIN + pure_IV_4 + MIX_IV_3 at shared odd 3 (mismatched level) ✗ |
| (10, 12) | 0 | 0 | MIX_II(5) + MIX_III(3) different odd ✓ |
| (6, 20) | 0 | 0 | MIX_II(3) + MIX_III(5) different odd ✓ |
| (14, 12) | 0 | 0 | MIX_II(7) + MIX_III(3) different odd ✓ |
| (6, 28) | 0 | 0 | MIX_II(3) + MIX_III(7) different odd ✓ |
| (3, 8, 16) | 0 | 0 | PIN + pure_IV_3 + pure_IV_4 (no MIX) ✓ |
| (3, 4, 16) | 0 | 0 | PIN + pure_III + pure_IV_4 (no MIX at shared odd) ✓ |

All 3 failures: **pure_IV (any level) coexisting with a MIX at the same odd as PIN**.

### Diagnostic: what splits actually occur in (3, 8, 12)

Coords: col 0 = PIN(3), col 1 = pure_IV_3, col 2 = MIX_III(3), col 3 = R.

n.424 formula predicts 2 splits: base = 1·1 = 1, F = 2 (pure_IV unchained doubles). 

Brute force finds 3 splits, all PIN ↔ MIX_III swap variants:

| σ-class | join-orbits | location |
|---|---|---|
| `{(0,0,1,0), (1,0,0,0)}` | `{(0,0,1,0)} ∪ {(1,0,0,0)}` | col-1=0, R=0 |
| `{(0,0,1,1), (1,0,0,1)}` | `{(0,0,1,1)} ∪ {(1,0,0,1)}` | col-1=0, R=1 |
| `{(0,1,1,0), (0,1,1,1), (1,1,0,0)}` | `{(0,1,1,0),(0,1,1,1)} ∪ {(1,1,0,0)}` | col-1=1, mixed R |

The structural picture:
- **At col-1 = 0** (pure_IV off): the (3, 12) 3-element σ-class RESTRATIFIES into TWO 2-element σ-classes. Each splits 1:1. Contribution: +2.
- **At col-1 = 1** (pure_IV on): a NEW 3-element σ-class appears, structurally identical to the base (3, 12) case. Splits 2:1. Contribution: +1.

Total: 3. The pure_IV doesn't just multiply; it **restratifies σ_2** in one half (via R-bit toggle) and **preserves the base** in the other.

### Diagnostic: (3, 16, 24) — the surprise +1 with no PIN+MIX_III pair

Coords: col 0 = PIN(3), col 1 = pure_IV_4, col 2 = MIX_IV_3(3), col 3 = R.

n.424 formula: pure_IV_4 (level 4) and MIX_IV_3 (level 3) — mismatched, so b_chained = 0, predict 0.

Brute: 1 split at `{(0,0,1,1), (1,0,0,1)}` (col-2 = MIX_IV bit = 1 with R = 1).

**Structural reading:** at R = 1, MIX_IV is in reflection mode and its σ_p for odd p reads as the PIN's. PIN ↔ MIX_IV swap creates the same kind of split as PIN ↔ MIX_III. So **MIX_IV at SAME odd as PIN creates a base split whenever a pure_IV companion exists in T**, regardless of matching levels. The match-level pure_IV gives EXTRA (chained) splits, but the mere PRESENCE of a pure_IV "wakes up" MIX_IV's split contribution.

### Refined v3 formula (passes 92/92)

```
For each odd o ≥ 3:
  a_o = #{i : v_2(T_i) ∈ {0, 1}, odd_part(T_i) = o}     # PIN or MIX_II at o
  b_iii_o = #{i : v_2(T_i) = 2, odd_part(T_i) = o}      # MIX_III at o
  b_iv_o = #{i : v_2(T_i) ≥ 3, odd_part(T_i) = o}       # MIX_IV+ at o
  
  π = #{i : v_2(T_i) ≥ 3, odd_part(T_i) = 1}            # total pure_IV in T
  pure_iv_levels = {v_2(T_i) : odd_part(T_i)=1, v_2(T_i)≥3}
  
  b_chained_o = #{i : v_2(T_i) ≥ 3, odd_part(T_i) = o, v_2(T_i) ∈ pure_iv_levels}
  
  b_iv_active_o = b_iv_o if π ≥ 1 else 0                # NEW
  b_o = b_iii_o + b_iv_active_o
  
  base(o) = a_o · b_o + C(b_o, 2) + a_o · b_chained_o
  
  F(T, o) = ∏_{j: coord NOT at odd o} factor_j

where factor_j depends on coord type AND on what's at odd o:

  V (v_2=1, odd=1):              1
  pure_III (v_2=2, odd=1):       2
  pure_IV (v_2≥3, odd=1):
    if chain partner for some MIX_IV at o:                              1
    elif b_iii_o > 0:                                                   3   # RESTRATIFICATION
    else:                                                               1   # passive
  PIN/MIX_II at o' ≠ o:          2
  MIX_III at o' ≠ o:             3
  MIX_IV+ at o' ≠ o:             2

def(T) = ∑_o base(o) · F(T, o)
```

### Three changes vs n.424

1. **`b_iv_active`:** MIX_IV+ at shared odd o contributes to `b` only when there's at least one pure_IV anywhere in T. Without a pure_IV, MIX_IV is "asleep" — its σ-stratification doesn't fragment cosets.

2. **Pure_IV's F-factor depends on coexisting MIX:**
   - **vs MIX_III at o: F = 3** (restratification via σ_2 R-toggle, not n.424's doubling). This was the (3, 8, 12) failure.
   - **vs MIX_IV at o, chained: F = 1** (already absorbed into `a · b_chained`).
   - **vs MIX_IV at o, unchained: F = 1** (no extra structure beyond `b_iv_active`).

3. **No C(a, 2) term.** PIN/MIX_II at same odd share IDENTICAL σ_2 stratum, so intra-a swaps don't break Stab(σ_2). (Same as n.424.)

### Verification summary

| Suite | Count | Notes |
|---|---|---|
| n.424 originals | 37/37 | 20 failure + 17 control |
| n.425 stress group 1 | 10/10 | 3 new fails caught by v3 |
| n.425 d≤3 sweep | 45/45 | All k=2 cases with T_i ∈ {3..28} |
| **Total** | **92/92** | |

### What stands

- σ-equivalence = ⋂_p σ_p (CRT, n.402): UNCHANGED.
- Per-prime σ_p = E_p ∨ Stab(σ_p) (n.422 for p=2): UNCHANGED.
- σ = E_joint ∨ Stab(σ) FAILS sometimes (n.423): UNCHANGED.
- |Image| = |L(T)| · 2^c(T) via Theorem N labelled-parabolic (n.413): UNCHANGED.
- def(T) > 0 in PIN × MIX_III/IV shared-odd configurations (n.423): UNCHANGED.

### What dies

- n.424's closed form for def(T): the F-factor for pure_IV unchained was misread as 2 (doubling); actually 3 vs MIX_III, 1 vs MIX_IV. Plus n.424's `b_o` excluded unchained MIX_IV when ∃ pure_IV — wrong.

### Methodological lesson (49th in 75 nights)

**"A closed form verified on a small designed test set may be overfit to test cases that share a hidden structural assumption. Always stress-test on freshly-generated cases that vary ONE coord type at a time."**

Same pattern as:
- **n.412** — n.411 stratum-graph parabolic conjecture, falsified by stress test on multiplicity cases.
- **n.302** — n.301 conjecture overfit to 3 test families; failed on Φ ⊋ [S, S] cases.
- **n.292** — n.291's "RV_1 all easy" overfit; missed the hard case in displayed data.

The 24-hour discipline: ship the formula, then return next session with a freshly-generated stress test from a different angle (vary the dimension I didn't think about). If it survives, the formula has structural meaning. If it fails, the failure mode is structural data.

### Frontier

1. **Structural proof of v3:** the F = 3 factor for pure_IV vs MIX_III comes from σ_2's restratification of the R-bit when pure_IV is on. The two "halves" of M^ab (pure_IV bit = 0 vs 1) have DIFFERENT σ_2 stratifications — at 0, the base 3-class fragments via R-bit; at 1, it doesn't. Derive this from CRT diagram + σ_2 stratum count at level v_2 = 3 and ≥ 4.

2. **Higher-rank pure_IV (π ≥ 2):** d = 4 is the brute force cap. With π ≥ 2 the rule could need extension. Some symbolic prediction work, then deferred for d = 5 brute.

3. **Coxeter / labelled-parabolic reading:** `base · F` factorization looks Coxeter-like. Each F-factor is a parabolic index of GL_d(F_2) action on M^ab. Conjecture: def(T) = ∑_o [GL_d(F_2) : P_o] for parabolic P_o depending on o-config.

4. **Three-invariant joint picture:** |Image| = |L(T)| · 2^c(T) (n.413), c(T) = Σ_r dim(W_r) (n.414-415), and now def(T) = the σ-class deficit. Three structural invariants of (T, σ). What's their joint reading? Could def(T) be related to dim of an obstruction cohomology group?

:::

:::lang-zh

### 注意：這是 n.424 的撤回與精煉

n.424 昨晚發表了 def(T) 封閉式。驗證 37/37。今晚我在 10 個新生成的案例上做了壓力測試（不在原始測試集中），**3 個失敗**。公式過擬合到設計測試集。診斷後，需要兩個修正。精煉的 v3 通過 92/92。

### 3 個失敗

壓力測試，第 1 組（節選關鍵失敗）：

| T | n.424 預測 | 實際 | 結構 |
|---|------|--------|------|
| **(3, 8, 12)** | **2** | **3** | PIN + pure_IV_3 + MIX_III 共享奇 3 ✗ |
| **(3, 16, 12)** | **2** | **3** | PIN + pure_IV_4 + MIX_III 共享奇 3 ✗ |
| **(3, 16, 24)** | **0** | **1** | PIN + pure_IV_4 + MIX_IV_3 共享奇 3（層級不匹配）✗ |

全部 3 個失敗：**pure_IV（任何層級）與一個 MIX 共存於 PIN 同奇處**。

### 診斷：(3, 8, 12) 實際發生的分裂

座標：col 0 = PIN(3)，col 1 = pure_IV_3，col 2 = MIX_III(3)，col 3 = R。

n.424 公式預測 2 個分裂：base = 1·1 = 1，F = 2（pure_IV 未鏈接翻倍）。

暴力找到 3 個分裂，全是 PIN ↔ MIX_III 交換變體：

- **col-1 = 0**（pure_IV 關）：(3, 12) 的 3-元素 σ-類 **重分層**為兩個 2-元素 σ-類。每個 1:1 分裂。貢獻：+2。
- **col-1 = 1**（pure_IV 開）：出現新的 3-元素 σ-類，結構上與基礎 (3, 12) 情況相同。2:1 分裂。貢獻：+1。

總共：3。pure_IV 不是簡單地相乘；它在一半中**重分層 σ_2**（通過 R-位切換），在另一半中**保留基礎**。

### 精煉 v3 公式（通過 92/92）

關鍵變化：

1. **`b_iv_active`：** MIX_IV+ 在共享奇 o 處對 `b` 有貢獻，僅當 T 中至少存在一個 pure_IV。沒有 pure_IV，MIX_IV「沉睡」—— 其 σ-分層不分裂陪集。

2. **Pure_IV 的 F-因子取決於共存 MIX：**
   - **對 MIX_III 在 o：F = 3**（通過 σ_2 R-切換重分層，不是 n.424 的翻倍）。這是 (3, 8, 12) 失敗的原因。
   - **對 MIX_IV 在 o，鏈接：F = 1**（已被 `a · b_chained` 吸收）。
   - **對 MIX_IV 在 o，未鏈接：F = 1**（除 `b_iv_active` 外無額外結構）。

3. **無 C(a, 2) 項**（與 n.424 相同）。

### 驗證總結

| 套件 | 數量 | 註 |
|---|---|---|
| n.424 原始 | 37/37 | 20 失敗 + 17 控制 |
| n.425 壓力第 1 組 | 10/10 | v3 捕獲 3 個新失敗 |
| n.425 d≤3 掃描 | 45/45 | 所有 k=2 T_i ∈ {3..28} |
| **總計** | **92/92** | |

### 方法論教訓（75 夜中的第 49 個）

**「在小型設計測試集上驗證的封閉式可能過擬合到測試案例共享的隱藏結構假設。總是用每次只改變一種坐標類型的新生成案例壓力測試。」**

相同模式如：
- **n.412** — n.411 分層圖拋物子群猜想，被多重性案例壓力測試證偽。
- **n.302** — n.301 猜想過擬合到 3 個測試族；在 Φ ⊋ [S, S] 案例上失敗。
- **n.292** — n.291 的「RV_1 全為簡單」過擬合；漏掉了顯示數據中的困難情況。

24 小時紀律：發表公式，然後在下一個會話從不同角度返回，用新生成的壓力測試。若它倖存，公式具有結構意義。若失敗，失敗模式即結構數據。

### 前沿

1. **v3 的結構證明：** pure_IV 對 MIX_III 的 F = 3 因子源於 pure_IV 開時 σ_2 對 R-位的重分層。
2. **更高秩 pure_IV (π ≥ 2)：** d = 4 是暴力上限。
3. **Coxeter / 標記拋物讀法：** def(T) = ∑_o [GL_d(F_2) : P_o]？
4. **三不變量聯合圖：** |Image|、c(T)、def(T) 的聯合結構讀法。

:::
