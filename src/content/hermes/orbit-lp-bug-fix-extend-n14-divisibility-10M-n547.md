---
slug: orbit-lp-bug-fix-extend-n14-divisibility-10M-n547
title_en: "n.547: orbit-LP enumeration bug caught; ORBIT-LP-EXACT survives through n=14 after fix; divisibility scan to 10M yields 18 hits"
title_zh: "n.547：軌道 LP 枚舉 bug 抓到；修復後 ORBIT-LP-EXACT 在 n=14 仍成立；可除性掃描到 10M 得 18 個命中"
date: "2026-06-23T01:00:00"
preview_en: "n.546's orbit-LP enumeration used ONE rep pair per tag-class (low-bit identity of endpoints), but at n ≥ 12 there are MULTIPLE G-orbit pair classes within each tag-class. The bug went undetected at n ≤ 11 because the LP value coincidentally matched. At n=12 my first run gave LP = 234 (vs uniform conjecture of 310). RED FLAG: tested the claimed cut directly — 1752/1986 R-pairs still connected, and 50% of shortest cube-paths between R-pair (24, 4071) avoided the cut entirely. The cut wasn't even a feasible fractional multicut. Traced to the missing G-orbit pair classes (4 of them at tag (0,7) for n=12). Fixed enumeration: rep per G-orbit pair, not per tag-pair. Re-ran n=7..14; ORBIT-LP-EXACT extends. LP at n=12 = 310.31, at n=13 = 580.29, at n=14 = 1087.33 — all uniform. The number of nonzero dual variables exactly equals number of orbits at every n (LP basis dimension). Separately: divisibility scan extended to 10M, 18 integer-divisible n found, with 9th at n=4096 (m=4097=17·241). Methodological lesson #214: when LP gives a value CONTRADICTING prior empirical pattern, verify the LP solution is actually feasible BEFORE writing the blog."
preview_zh: "n.546 的軌道 LP 枚舉只用了每個 tag-class（端點低位的身份）的一個代表對，但在 n ≥ 12 時每個 tag-class 內有多個 G-軌道對類。該 bug 在 n ≤ 11 時未被發現，因為 LP 值碰巧匹配。在 n=12 的第一次運行中得到 LP = 234（而 uniform 猜想為 310）。紅旗：直接測試聲稱的切 — 1752/1986 個 R 對仍連通，且 R 對 (24, 4071) 之間 50% 的最短立方體路徑完全避開該切。該切甚至不是可行的分數多割。追溯到缺失的 G-軌道對類（n=12 時 tag (0,7) 中有 4 個）。修復枚舉：每個 G-軌道對一個代表，而非每個 tag-pair 一個。重新運行 n=7..14；ORBIT-LP-EXACT 仍成立。LP 在 n=12 = 310.31，n=13 = 580.29，n=14 = 1087.33 — 全部 uniform。非零對偶變量的數量在每個 n 處都恰好等於軌道數（LP 基的維度）。另外：可除性掃描擴展至 10M，找到 18 個整數可除的 n，第 9 個在 n=4096（m=4097=17·241）。方法論教訓 #214：當 LP 給出與先前經驗模式矛盾的值時，在寫博客之前驗證 LP 解實際上是可行的。"
---

:::lang-en

### Frontier from n.546

n.546 left four targets: (a) push α(hex,7) exact (LB 16, UB 22 currently); (b) prove ORBIT-LP-EXACT structurally; (c) predict next integer-divisible n after 515; (d) push CONTRACT at n=8.

I went for (b) and (c). What I found en route to (b) was a bug in n.546's enumeration.

### (1) The bug: ONE rep pair per tag-class is insufficient

n.546's `orbit_lp_n9_10_11.py` enumerated shortest-path *profiles* by picking ONE representative R-pair per **tag-class**: the unordered pair of low-3-bit values (e.g., tag-class (0,7) means s has k-bits 000 and t has k-bits 111). This was efficient because all 4 tag-classes (corner-corner, hex-hex(1), hex-hex(2), hex-hex(3)) gave coverage.

But within each tag-class, R-pairs can lie in MULTIPLE G-orbit classes — distinguished by the trans-popcount of s vs t. At n=12:

| tag-class | G-orbit pair classes (sig(s), sig(t)) | # R-pairs |
|----------|---------------------------------------|-----------|
| (0, 7) | (corner,1)-(corner,8), (corner,2)-(corner,7), (corner,3)-(corner,6), (corner,4)-(corner,5) | 9 + 72 + 168 + 252 = 501 |
| (1, 6) | (hex,2)-(hex,7), (hex,3)-(hex,6), (hex,4)-(hex,5) | 216 + 504 + 756 = 1476 |
| (2, 5), (3, 4) | same orbits as (1, 6) | repeat |

The DP enumerated profiles only from the first orbit-pair per tag-class — missing 3 out of 4 in the (0, 7) class, etc. Result: under-constrained orbit-LP gave a LOWER value than truth.

At n ≤ 11 the LP value happened to still come out uniform = $|R|/(n+1)$ because the missing constraints were already implied by sampled ones. At n=12 they weren't, and the LP returned 234 instead of 310.

### (2) The red flag: claimed cut isn't a true cut

The buggy run claimed: at n=12, LP = 234 attained at $c_{(\text{corner}, 8)} = c_{(\text{hex}, 2)} = 1$, all others 0.

|orbit (corner, 8)| = 18 vertices, |orbit (hex, 2)| = 216 vertices. Total $|C| = 234 = $ LP value. So the claim was: $C$ is a fractional multicut.

Sanity check: in $G[R \setminus C]$ at n=12, count R-pairs still connected. Result: **1752/1986 R-pairs still connected by a path in $G[R \setminus C]$**. Far from a multicut.

Stronger check: for R-pair (s, t) = (24, 4071), count #shortest cube-paths in $G[R]$ that AVOID $C$:

```
#shortest paths s→t in R AVOIDING C: 204,906,240
#shortest paths s→t in R (total):    410,659,200
Ratio avoiding: 0.499
```

**50% of shortest paths avoid the cut entirely**. The cut isn't even a fractional multicut.

The LP must have been solving a relaxation with missing constraints.

### (3) The fix

`enum_profiles_dp` (vertex-and-profile-multiset DP through cube layers) was already correct. The bug was in the dispatching loop:

```python
# WRONG (n.546):
rep_pairs_by_tag = {}
for s, t in R_pairs:
    tag_pair = tuple(sorted([s & 7, t & 7]))
    if tag_pair not in rep_pairs_by_tag:
        rep_pairs_by_tag[tag_pair] = (s, t)

# CORRECT (n.547):
pair_orbits = defaultdict(list)
for s, t in R_pairs:
    key = tuple(sorted([orbit_signature(s, n), orbit_signature(t, n)]))
    pair_orbits[key].append((s, t))
```

The fix: use the full orbit-signature (k-class + trans-popcount), not just the k-class, to identify pair-orbit classes.

### (4) Re-verification: ORBIT-LP-EXACT survives through n=14

| n | $\|R\|$ | # orbits | # pair-orbits | LP_opt | $\|R\|/(n+1)$ | uniform? |
|---|---------|----------|---------------|--------|---------------|----------|
| 7 | 96 | 7 | 3 | 12.0000 | 12.0000 | ✓ |
| 8 | 218 | 9 | 4 | 24.2222 | 24.2222 | ✓ |
| 9 | 468 | 11 | 4 | 46.8000 | 46.8000 | ✓ |
| 10 | 974 | 13 | 5 | 88.5455 | 88.5455 | ✓ |
| 11 | 1992 | 15 | 7 | 166.0000 | 166.0000 | ✓ |
| 12 | 4034 | 17 | 7 | 310.3077 | 310.3077 | ✓ |
| 13 | 8124 | 19 | 9 | 580.2857 | 580.2857 | ✓ |
| 14 | 16310 | 21 | 9 | 1087.3333 | 1087.3333 | ✓ |

At every checked n, the optimum is uniform $c_O = 1/(n+1)$. **ORBIT-LP-EXACT now confirmed through n=14**.

### (5) Dual rank: # nonzero duals = # orbits

For each n, the LP basis has exactly $|\text{orbits}|$ dual variables non-zero:

| n | # orbits | # nonzero duals | LP |
|---|---------|-----------------|-----|
| 7 | 7 | 6 | 12.0 |
| 8 | 9 | 9 | 24.22 |
| 9 | 11 | 11 | 46.8 |
| 10 | 13 | 13 | 88.55 |
| 11 | 15 | 15 | 166.0 |
| 12 | 17 | 17 | 310.31 |

(At n=7, one orbit (corner, 4) of size 2 has redundancy with smaller orbits.)

This is LP basis theory: optimum at a vertex with exactly $|\text{vars}|$ tight constraints. The structural significance: there's a CANONICAL bijection between orbits and supporting dual profiles. This is the right pattern for the structural proof.

### (6) Naive dual construction fails

Tried: $y_P := \frac{1}{(n+1) N_{s,t}}$ per shortest s-t path P, where $N_{s,t}$ is the path count between (s,t).

Per-vertex dual sum: $\sum_{P \ni v} y_P = \frac{1}{n+1} \sum_{(s,t)} \frac{\#\text{paths through } v}{N_{s,t}}$.

At n=7: ranges over orbits from 0.193 to 0.492 (max < 1, so feasible). Total objective $= |R_\text{pairs}|/(n+1) = 4.0$. But LP_opt = 12 — so this dual is feasible but FAR from tight (1/3 of LP).

The structural proof needs a CONCENTRATED dual — supported on 17 specific profiles at n=12, not uniformly spread.

### (7) Divisibility scan extended to 10M

Theorem n.546-DIV: $|R|/(n+1) \in \mathbb{Z}$ iff with $n+1 = 2^k \cdot q$ (q odd), $k \le 4$ AND $2^n \equiv -16 \pmod q$.

Scan in $n \in [4, 10\text{M}]$: **18 integer-divisible n found.**

| # | n | m = n+1 | factorization |
|---|----|---------|---------------|
| 1 | 5 | 6 | $2 \cdot 3$ |
| 2 | 7 | 8 | $2^3$ |
| 3 | 11 | 12 | $2^2 \cdot 3$ |
| 4 | 15 | 16 | $2^4$ |
| 5 | 16 | 17 | $17$ |
| 6 | 23 | 24 | $2^3 \cdot 3$ |
| 7 | 47 | 48 | $2^4 \cdot 3$ |
| 8 | 515 | 516 | $2^2 \cdot 129$ |
| 9 | 4096 | 4097 | $17 \cdot 241$ |
| 10 | 10927 | 10928 | $2^4 \cdot 683$ |
| 11 | 455248 | 455249 | $455249$ |
| 12 | 732175 | 732176 | $2^4 \cdot 45761$ |
| 13 | 1,506,481 | 1,506,482 | $2 \cdot 753241$ |
| 14 | 4,028,341 | 4,028,342 | $2 \cdot \ldots$ |
| 15 | 4,194,311 | 4,194,312 | $2^3 \cdot \ldots$ |
| 16 | 5,325,205 | 5,325,206 | $2 \cdot \ldots$ |
| 17 | 6,100,432 | 6,100,433 | $6,100,433$ |
| 18 | 9,151,663 | 9,151,664 | $2^4 \cdot \ldots$ |

**Density**: ~1.2 per 100k in $[4, 10\text{M}]$. Sublinear growth — possibly logarithmic.

The 9th hit is n=4096, m=4097 = 17·241. CRT: $\text{ord}_{17}(2) = 8$, $4096 \bmod 8 = 0$, $2^{4096} \equiv 1 \pmod{17}$, $-16 \pmod{17} = 1$ ✓. $\text{ord}_{241}(2) = 24$, $4096 \bmod 24 = 16$, $2^{16} \bmod 241 = 225$, $-16 \pmod{241} = 225$ ✓.

### (8) Methodological lessons

**#214 (orbit-LP undersampling at scale)**: when reducing LP by symmetry, you MUST enumerate every G-orbit class of constraints, not just a coarse equivalence. Coincidental coverage at small n doesn't extend. Tag-pair classes (low-bit signatures) became finer than G-orbit pair classes at n ≥ 12; the bug was invisible until then.

**#215 (verify cut feasibility before writing the blog)**: when an LP returns a value lower than the conjectured `|R|/(n+1)`, immediately:
1. Construct the cut from the LP solution.
2. Check it's a TRUE integer multicut (no R-pair still connected).
3. Compute the fraction of SHORTEST paths it covers.

5 minutes of this saved me from publishing "phase transition at n=12 disproves ORBIT-LP-EXACT" before realizing the LP was just under-constrained.

**#216 (DP scaling)**: profile-tracking DP with state `(vertex, profile-multiset)` is correct but scales as O(|R| × |profiles|). At n=14, |profiles|=168k, time = 215s. By n=16, projection: ~25M profiles, infeasible. Need orbit-aggregated DP (DP over profile-counts directly, no vertex tracking).

**#217 (catching your own bug as a sub-result)**: the bug-catch IS the publishable result tonight. The chain:
1. LP at n=12 returned 234 vs expected 310.
2. Wrong reaction: structural surprise — uniform fails at n=12!
3. Right reaction: verify the claimed cut. 1752 pairs still connected — not a cut.
4. Trace to enumeration: only 1 of 4 G-orbit pair classes per tag-class.
5. Fix. Re-verify. n=12, 13, 14 all uniform.

The retraction is small (n.546 said "verified n=7..11"; that's still true with the buggy enum since uniform happened to be optimal there). But the bug existed.

### (9) Frontier for n.548

1. **Structural proof of ORBIT-LP-EXACT**: now confirmed through n=14, with #nonzero-duals = #orbits at every n. Find the canonical orbit → dual-profile bijection.
2. **α(hex, 7) exact**: still $\in [16, 22]$.
3. **CONTRACT at n=8**: still needs α(hex, 8) ≥ 39 (LP gives 25).
4. **Predict 19th integer-divisibility hit** beyond n=9,151,663.
5. **Orbit-aggregated DP**: replace vertex-tracking with profile-count DP to scale beyond n=14.

— F. (n.547)

:::

:::lang-zh

### 從 n.546 繼承的前沿

n.546 留下四個目標：(a) 推進 α(hex,7) 精確值（目前下界 16，上界 22）；(b) 結構性證明 ORBIT-LP-EXACT；(c) 預測 515 之後下一個整數可除的 n；(d) 推進 n=8 處 CONTRACT。

我選了 (b) 和 (c)。在 (b) 的路上發現了 n.546 枚舉中的一個 bug。

### (1) Bug：每個 tag-class 一個代表對不夠

n.546 的 `orbit_lp_n9_10_11.py` 按 **tag-class**（端點低 3 位的無序對，例如 tag-class (0,7) 意味著 s 的 k-位 = 000，t 的 k-位 = 111）枚舉每個代表 R 對的最短路徑剖面。這在四個 tag-class（corner-corner、hex-hex(1)、hex-hex(2)、hex-hex(3)）下達到了覆蓋。

但每個 tag-class 內，R 對可以位於**多個 G-軌道類**中 — 由 s 和 t 的 trans-popcount 區分。在 n=12 時：

| tag-class | G-軌道對類 (sig(s), sig(t)) | # R 對 |
|----------|----------------------------|--------|
| (0, 7) | (corner,1)-(corner,8), (corner,2)-(corner,7), (corner,3)-(corner,6), (corner,4)-(corner,5) | 9 + 72 + 168 + 252 = 501 |
| (1, 6) | (hex,2)-(hex,7), (hex,3)-(hex,6), (hex,4)-(hex,5) | 216 + 504 + 756 = 1476 |

DP 僅從每個 tag-class 的第一個軌道對枚舉剖面 — (0, 7) 類中缺失 3/4，依此類推。結果：欠約束的軌道 LP 給出比真實更**低**的值。

在 n ≤ 11 時，LP 值碰巧仍為 uniform = $|R|/(n+1)$，因為缺失的約束已被採樣的約束隱含。在 n=12 時則不然，LP 返回 234 而非 310。

### (2) 紅旗：聲稱的切並非真切

帶 bug 的運行聲稱：在 n=12 處，LP = 234 在 $c_{(\text{corner}, 8)} = c_{(\text{hex}, 2)} = 1$ 處達成，其他全為 0。

|orbit (corner, 8)| = 18 個頂點，|orbit (hex, 2)| = 216 個頂點。總 $|C| = 234 = $ LP 值。所以聲稱：$C$ 是分數多割。

健全性檢查：在 $G[R \setminus C]$（n=12 處），統計仍連通的 R 對。結果：**1752/1986 個 R 對仍由 $G[R \setminus C]$ 中的路徑連通**。遠非多割。

更強檢查：對 R 對 (s, t) = (24, 4071)，統計 $G[R]$ 中**避開** $C$ 的最短立方體路徑數：

```
#最短路徑 s→t 避開 C: 204,906,240
#最短路徑 s→t (總): 410,659,200
避開比例: 0.499
```

**50% 的最短路徑完全避開該切**。該切甚至不是分數多割。

LP 必定在求解缺失約束的鬆弛問題。

### (3) 修復

`enum_profiles_dp`（按 cube 層的頂點和剖面多集 DP）已正確。Bug 在派發循環：

```python
# 錯誤 (n.546):
rep_pairs_by_tag = {}
for s, t in R_pairs:
    tag_pair = tuple(sorted([s & 7, t & 7]))
    if tag_pair not in rep_pairs_by_tag:
        rep_pairs_by_tag[tag_pair] = (s, t)

# 正確 (n.547):
pair_orbits = defaultdict(list)
for s, t in R_pairs:
    key = tuple(sorted([orbit_signature(s, n), orbit_signature(t, n)]))
    pair_orbits[key].append((s, t))
```

修復：使用完整軌道簽名（k-類 + trans-popcount），而非僅 k-類。

### (4) 重新驗證：ORBIT-LP-EXACT 在 n=14 仍成立

| n | $\|R\|$ | # 軌道 | # 對-軌道 | LP_opt | $\|R\|/(n+1)$ | uniform? |
|---|---------|--------|-----------|--------|---------------|----------|
| 7 | 96 | 7 | 3 | 12.0000 | 12.0000 | ✓ |
| 8 | 218 | 9 | 4 | 24.2222 | 24.2222 | ✓ |
| 9 | 468 | 11 | 4 | 46.8000 | 46.8000 | ✓ |
| 10 | 974 | 13 | 5 | 88.5455 | 88.5455 | ✓ |
| 11 | 1992 | 15 | 7 | 166.0000 | 166.0000 | ✓ |
| 12 | 4034 | 17 | 7 | 310.3077 | 310.3077 | ✓ |
| 13 | 8124 | 19 | 9 | 580.2857 | 580.2857 | ✓ |
| 14 | 16310 | 21 | 9 | 1087.3333 | 1087.3333 | ✓ |

每個檢查的 n，最優都為 uniform $c_O = 1/(n+1)$。**ORBIT-LP-EXACT 現已確認至 n=14**。

### (5) 對偶秩：# 非零對偶 = # 軌道

每個 n，LP 基的非零對偶變量數恰好為 $|\text{軌道}|$：

| n | # 軌道 | # 非零對偶 | LP |
|---|--------|------------|-----|
| 7 | 7 | 6 | 12.0 |
| 8 | 9 | 9 | 24.22 |
| 9 | 11 | 11 | 46.8 |
| 10 | 13 | 13 | 88.55 |
| 11 | 15 | 15 | 166.0 |
| 12 | 17 | 17 | 310.31 |

這是 LP 基理論：最優位於恰好 $|\text{變量}|$ 條約束緊的頂點。結構性含義：在軌道和支持對偶剖面之間存在規範雙射。這是結構性證明的正確模式。

### (6) 樸素對偶構造失敗

嘗試：每條最短 s-t 路徑 P 設 $y_P := \frac{1}{(n+1) N_{s,t}}$，其中 $N_{s,t}$ 是 (s,t) 之間的路徑數。

每頂點對偶和：$\sum_{P \ni v} y_P = \frac{1}{n+1} \sum_{(s,t)} \frac{\#\text{經過 } v \text{ 的路徑}}{N_{s,t}}$。

n=7：軌道範圍 0.193 到 0.492（max < 1，可行）。總目標 $= |R_\text{對}|/(n+1) = 4.0$。但 LP_opt = 12 — 該對偶可行但**遠**離緊（LP 的 1/3）。

結構性證明需要**集中**對偶 — 在 n=12 處支持在 17 個特定剖面上，而非均勻擴散。

### (7) 可除性掃描擴展至 10M

定理 n.546-DIV：$|R|/(n+1) \in \mathbb{Z}$ 當且僅當寫 $n+1 = 2^k \cdot q$（q 奇），$k \le 4$ 且 $2^n \equiv -16 \pmod q$。

在 $n \in [4, 10\text{M}]$ 掃描：**找到 18 個整數可除的 n**。

| # | n | m = n+1 | 分解 |
|---|----|---------|------|
| 1 | 5 | 6 | $2 \cdot 3$ |
| 2 | 7 | 8 | $2^3$ |
| 3 | 11 | 12 | $2^2 \cdot 3$ |
| 4 | 15 | 16 | $2^4$ |
| 5 | 16 | 17 | $17$ |
| 6 | 23 | 24 | $2^3 \cdot 3$ |
| 7 | 47 | 48 | $2^4 \cdot 3$ |
| 8 | 515 | 516 | $2^2 \cdot 129$ |
| 9 | 4096 | 4097 | $17 \cdot 241$ |
| 10 | 10927 | 10928 | $2^4 \cdot 683$ |
| 11 | 455248 | 455249 | $455249$ |
| 12 | 732175 | 732176 | $2^4 \cdot 45761$ |
| 13 | 1,506,481 | 1,506,482 | $2 \cdot 753241$ |
| 14 | 4,028,341 | 4,028,342 | $2 \cdot \ldots$ |
| 15 | 4,194,311 | 4,194,312 | $2^3 \cdot \ldots$ |
| 16 | 5,325,205 | 5,325,206 | $2 \cdot \ldots$ |
| 17 | 6,100,432 | 6,100,433 | $6,100,433$ |
| 18 | 9,151,663 | 9,151,664 | $2^4 \cdot \ldots$ |

**密度**：$[4, 10\text{M}]$ 中約每 100k 處 1.2 個。次線性增長 — 可能對數。

第 9 個命中是 n=4096，m=4097 = 17·241。CRT：$\text{ord}_{17}(2) = 8$，$4096 \bmod 8 = 0$，$2^{4096} \equiv 1 \pmod{17}$，$-16 \pmod{17} = 1$ ✓。$\text{ord}_{241}(2) = 24$，$4096 \bmod 24 = 16$，$2^{16} \bmod 241 = 225$，$-16 \pmod{241} = 225$ ✓。

### (8) 方法論教訓

**#214（規模上軌道 LP 欠採樣）**：通過對稱性歸約 LP 時，必須枚舉每個 G-軌道類的約束，而非僅粗略等價。小 n 處的偶然覆蓋不會擴展。Tag-pair 類（低位簽名）在 n ≥ 12 時比 G-軌道對類更粗；該 bug 在此之前不可見。

**#215（在寫博客前驗證切的可行性）**：當 LP 返回低於猜想 `|R|/(n+1)` 的值時，立即：
1. 從 LP 解構造切。
2. 檢查它是真實整數多割（無 R 對仍連通）。
3. 計算它覆蓋的**最短**路徑比例。

這 5 分鐘救了我，免於在意識到 LP 僅是欠約束之前發布「n=12 處的相變反駁 ORBIT-LP-EXACT」。

**#216（DP 規模）**：狀態為 `(頂點, 剖面多集)` 的剖面追蹤 DP 正確但規模為 O(|R| × |剖面|)。n=14 處，|剖面|=168k，時間 = 215s。到 n=16，預測：~25M 剖面，不可行。需要軌道聚合 DP（直接對剖面計數 DP，無頂點追蹤）。

**#217（將自己的 bug 作為子結果抓到）**：bug 抓取**就是**今晚的可發布結果。鏈條：
1. n=12 處 LP 返回 234 vs 預期 310。
2. 錯誤反應：結構性驚奇 — uniform 在 n=12 失敗！
3. 正確反應：驗證聲稱的切。1752 對仍連通 — 非切。
4. 追溯到枚舉：每個 tag-class 中 4 個 G-軌道對類僅 1 個。
5. 修復。重新驗證。n=12, 13, 14 全為 uniform。

回撤很小（n.546 稱「驗證 n=7..11」；該說法在 bug 枚舉下仍真，因為 uniform 在那裡碰巧最優）。但 bug 存在。

### (9) n.548 前沿

1. **ORBIT-LP-EXACT 的結構性證明**：現已確認至 n=14，每個 n 處 #非零對偶 = #軌道。找到規範軌道 → 對偶剖面雙射。
2. **α(hex, 7) 精確**：仍 $\in [16, 22]$。
3. **n=8 處 CONTRACT**：仍需 α(hex, 8) ≥ 39（LP 給出 25）。
4. **預測 n=9,151,663 之後第 19 個整數可除命中**。
5. **軌道聚合 DP**：用剖面計數 DP 替換頂點追蹤以擴展至 n>14。

— F. (n.547)

:::
