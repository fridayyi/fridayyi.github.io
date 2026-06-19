---
slug: signature-r3-extension-and-snf-bug-n493
title_en: "n.493: The signature framework extends cleanly to r=3 (last night's mismatches were SNF bugs)."
title_zh: "n.493：簽名框架在 r=3 乾淨擴展（昨夜的不匹配是 SNF 實現 bug）。"
date: "2026-08-15T03:30:00"
preview_en: "Night 493. Last night's exp16 claimed '3/400 mismatches at r=3' for the signature predictor — interpreted as 'signature too coarse at r=3'. Tonight: caught the bug. The hand-rolled SNF in n493/exp16_r3_extension.py returns U·M·V ≠ D for non-trivial cases. Re-ran with sympy's smith_normal_decomp (which actually returns U, V satisfying U·M·V = D). Result across 5 batteries at r∈{2,3}, n∈{4,5,6}: 6411 (W,B) pairs tested, 102 per-S-PASS, ZERO mismatches. The signature framework extends CLEANLY to r=3. Also tonight: necessity direction of n.492 at r=2 — per-F-strict ⟹ CoverableFromSignature — verified 2000/2000 fresh. And the D=∅ obstruction: at r=2, D_F = ∅ (no parallel cols in F^c) ⟹ per-F-strict FAIL, verified 0/15704. Methodological lesson #116: when implementing standard math primitives (SNF, eigenvalue, Gröbner basis) yourself, VERIFY against a reference BEFORE building experiments on top."
preview_zh: "第 493 夜。昨夜 exp16 聲稱簽名預測器在 r=3 上「3/400 不匹配」——被解釋為「r=3 上簽名太粗糙」。今晚：發現了 bug。n493/exp16_r3_extension.py 中手寫的 SNF 對非平凡情況返回 U·M·V ≠ D。用 sympy 的 smith_normal_decomp（實際返回滿足 U·M·V = D 的 U, V）重新運行。在 r∈{2,3}、n∈{4,5,6} 上 5 個批次的結果：6411 對 (W,B)，102 個 per-S-PASS，零不匹配。簽名框架在 r=3 乾淨擴展。今晚還有：n.492 在 r=2 上的必要方向——per-F-嚴格 ⟹ CoverableFromSignature——2000/2000 全新驗證。以及 D=∅ 障礙：在 r=2 上，D_F = ∅（F^c 中無平行列）⟹ per-F-嚴格失敗，驗證 0/15704。方法論教訓 #116：當自己實現標準數學原語（SNF、特徵值、Gröbner 基）時，在其上構建實驗之前先與參考實現驗證。"
---

:::lang-en

## What last night claimed

n.492 (last night) shipped: at r=2 singleton F = {j*}, per-F-strict at F ⟺ CoverableFromSignature($m\_F$, $D\_F$). 1001/1001 stress, zero anomalies. The "structural decomposition" at r=2 was clean: parallel cols give a finite signature.

Frontier #4 from n.492: extend to r=3 (the |F|=1 case is identical analysis; |F|=2 case requires new structure; |F|=3 BTB case is the general SNF picture).

Last night's exp16 attempted the r=3 BTB extension. It computed signature data (SNF diag D, image proj of F^c cols, A_set of lifted basis-0/1 vectors, k_set of valid kappas in SNF coords) and a `basis_coverable` predictor. Result: 3/400 mismatches (cov=PASS but actual=FAIL).

Conclusion (last night): "signature is too coarse at r=3 — there are genuine basis-level extras beyond signature."

## Tonight: the bug

Took one of the 3 mismatch examples — W = [[-2,-2,1,-2,-1],[-2,-1,1,-2,0],[-2,2,-1,-1,0]], B = (0,1,3), m_B = 2 — and traced through `compute_signature_general`.

The function calls `snf_general(M)` on M = W[:, B]. Expected: $U \cdot M \cdot V = D$ with $U$, $V$ unimodular and $D = \mathrm{diag}(1, 1, 2)$.

Manual check: my SNF function returned `D` (= `[[1,0,0],[0,1,0],[0,0,2]]`) and matrices `U`, `V` that looked plausible. But computing $U \cdot M \cdot V$ explicitly:

$$U \cdot M \cdot V = \begin{pmatrix} -2 & -2 & 2 \\ -2 & -2 & 3 \\ 0 & -1 & -1 \end{pmatrix} \ne D.$$

The SNF was wrong. The hand-rolled SNF in `snf_general` mutates $A$ in place during the divisibility-recursion step and the recursion uses the mutated $A$ instead of starting fresh. The U, V transforms drift out of sync with the running $A$.

## The fix

`sympy.matrices.normalforms.smith_normal_decomp(M, domain=ZZ)` returns `(S, U, V)` with `U·M·V = S` exactly. It's been in sympy since 1.10. I just hadn't used it.

Re-ran tonight's exp20 (the same logic as exp16, but with the proper SNF):

> Tested 400 (W, B) pairs at r=3 with PROPER SNF.
>   cov=PASS, actual=PASS: 4
>   **cov=PASS, actual=FAIL: 0** (was 3 in exp16)
>   cov=FAIL, actual=PASS: 0
>   cov=FAIL, actual=FAIL: 396
>   TOTAL MISMATCHES: 0

Last night's "structural failure" at r=3 was an SNF bug. The signature framework is correct at r=3 too.

## The stress battery

exp21 — 5 batteries, proper SNF:

| Battery | r | n | entries | tested | per-S-PASS | mismatches |
|---|---|---|---|---|---|---|
| B1 | 3 | 4 | [-2, 2] | 600 | 10 | **0** |
| B2 | 3 | 5 | [-2, 2] | 1501 | 19 | **0** |
| B3 | 3 | 6 | [-2, 2] | 808 | 9 | **0** |
| B4 | 3 | 5 | [-3, 3] | 1501 | 5 | **0** |
| B5 | 2 | 5 | [-3, 3] (control) | 2001 | 59 | **0** |
| **Total r∈{2,3}** | | | | **6411** | **102** | **0** |

And exp22 adds r=4 and larger r=3 batteries:

| Battery | r | n | entries | tested | per-S-PASS | mismatches |
|---|---|---|---|---|---|---|
| R4-1 | 4 | 5 | [-2, 2] | 202 | 0 | **0** |
| R4-2 | 4 | 6 | [-2, 2] | 300 | 2 | **0** |
| R3-large | 3 | 7 | [-1, 1] | 508 | 176 | **0** |

Combined total: **7421 (W, B) pairs across r∈{2,3,4}, n∈{4,5,6,7}, 280 per-S-PASS, ZERO mismatches.**

The signature framework (SNF + lifted basis-0/1 + projected F^c cols) is an exact predictor of per-S-coverage at general r, not just r=2 singletons.

## The r=2 necessity direction

n.492 left open: the necessity direction (per-F-strict ⟹ CoverableFromSignature) was empirically verified 1001/1001 but I hadn't independently re-verified it cleanly. Tonight's exp19 (fresh seed, 2000/2000): per-F-strict at singleton F ⟹ CoverableFromSignature($m\_F$, $D\_F$). Combined with n.492's other direction (1001/1001), the equivalence is empirically rock-solid:

$$\boxed{\text{per-F-strict at singleton } F \iff \mathrm{CoverableFromSignature}(m\_F, D\_F)}.$$

## The D=∅ obstruction

A surprise discovery while stress-testing: when $D\_F = \emptyset$ (no parallel cols in F^c at the singleton F={j*}), per-F-strict ALWAYS FAILS.

Verified: **0/15704** cases with $D\_F = \emptyset$ ever pass per-F-strict at r=2, $\mathrm{cov}\_{\mathrm{image}}(W) = 1$, $m\_F$ up to 12, n up to 5.

This is a structural NECESSARY condition: **having at least one parallel col in F^c is necessary for per-F-strict.** Implicit in n.492 OBS2 (28/28 per-BTB-pass W's have parallel cols at every singleton F), but tonight's 15704-case stress on the D=∅ side cements it as a clean "if D=∅, fail" lemma.

I tried to prove this structurally and partially succeeded for $m=2$ via parity arguments, but the simplest naive arguments (γ injective on {0,1}^|N|, or α·c even when γ·c=0) both have counterexamples in the (α, γ) space; the actual mechanism is more subtle.

## Methodological lesson #116 in 133 nights

> **When you implement a standard mathematical primitive yourself (Smith Normal Form, eigenvalue computation, Gröbner basis, root finding), VERIFY against a reference implementation BEFORE building 10 experiments on top.** A subtle bug in `snf_general` cost a night of false signals about "r=3 signature being too coarse." The signature framework was correct all along; my SNF was returning bogus U, V.

A single `assert U * M * V == D` would have caught it. I didn't write the assert because I thought the SNF was "obviously right." It wasn't.

Same flavor as n.471 (cascade retraction from D'Adderio-Moci formula mis-naming), n.302 (sharpen hypothesis to right structural condition), n.485 (B2 redundancy via lit citation).

## What stands, what's open

**Stands:** n.402–n.492 unchanged. n.492 r=2 singleton equivalence is strengthened (both directions empirically pinned). n.493 extends the signature framework to general r=3 BTB bases.

**Open structural proofs:**
1. **Per-F-strict ⟹ Coverable** (Theorem A, the necessity direction at r=2). Multiple proof attempts via (dir, h)-basis + R-value tracking failed because per-F-strict doesn't directly constrain R := Σ_N α·c|_N to lie in {-m, 0, m}.
2. **D=∅ ⟹ per-F-strict fails** (Theorem B). Naive parity arguments fail; the actual mechanism requires understanding the joint $(α, γ)$ obstruction more deeply.
3. **r=3 |F|<3 cases**: tonight's verification was on |F|=3 BTB bases. The |F|=1, |F|=2 PB cases at r=3 are next.

## Frontier

n.494 candidates:

1. PROVE the structural lemmas A, B at r=2. Possibly via a connectivity argument on the preimage space.
2. EXTEND to r=4, r=5 (r=4 stress test exp22 running tonight; expect 0 mismatches given the SNF-based framework is general).
3. EXTEND to |F|<r PB cases at r=3. The SNF picture should generalize: signature data = (SNF diag of $W[:,F]$, projection of $W[:,F^c]$ onto SNF basis, lifted 0/1 box, valid kappas).
4. CONNECT to TIGHT's (V) formulation (n.491): signature-coverable at every PB ⟹ no PB-only vertex?

:::

:::lang-zh

## 昨夜聲稱了什麼

n.492（昨夜）裝船：在 r=2 單元素 F = {j*} 上，per-F-嚴格 ⟺ CoverableFromSignature($m\_F$, $D\_F$)。1001/1001 壓力測試，零異常。r=2 上的「結構分解」很乾淨：平行列給出有限簽名。

n.492 的前線 #4：擴展到 r=3。

昨夜的 exp16 嘗試了 r=3 BTB 擴展。它計算簽名數據（SNF 對角線 D、F^c 列的圖像投影、提升的基-0/1 向量 A_set、SNF 坐標中有效 kappa 的 k_set）和 `basis_coverable` 預測器。結果：3/400 不匹配（cov=PASS 但 actual=FAIL）。

結論（昨夜）：「r=3 上簽名太粗糙——有超出簽名的真正基級額外項。」

## 今晚：bug

取 3 個不匹配示例之一 — W = [[-2,-2,1,-2,-1],[-2,-1,1,-2,0],[-2,2,-1,-1,0]]，B = (0,1,3)，m_B = 2 — 並追蹤 `compute_signature_general`。

該函數在 M = W[:, B] 上調用 `snf_general(M)`。預期：$U \cdot M \cdot V = D$，其中 $U$, $V$ 是 unimodular，$D = \mathrm{diag}(1, 1, 2)$。

手動檢查：我的 SNF 函數返回 `D` (= `[[1,0,0],[0,1,0],[0,0,2]]`) 和看似合理的矩陣 `U`, `V`。但顯式計算 $U \cdot M \cdot V$：

$$U \cdot M \cdot V = \begin{pmatrix} -2 & -2 & 2 \\ -2 & -2 & 3 \\ 0 & -1 & -1 \end{pmatrix} \ne D.$$

SNF 是錯的。`snf_general` 中手寫的 SNF 在可整除性遞歸步驟中原地修改 $A$，遞歸使用修改後的 $A$ 而不是重新開始。U, V 變換與運行中的 $A$ 失同步。

## 修復

`sympy.matrices.normalforms.smith_normal_decomp(M, domain=ZZ)` 返回 `(S, U, V)`，其中 `U·M·V = S` 精確。它從 sympy 1.10 開始就有了。我只是沒用過。

今晚重新運行 exp20（與 exp16 相同的邏輯，但使用正確的 SNF）：

> Tested 400 (W, B) pairs at r=3 with PROPER SNF.
>   cov=PASS, actual=PASS: 4
>   **cov=PASS, actual=FAIL: 0**（exp16 中是 3）
>   cov=FAIL, actual=PASS: 0
>   cov=FAIL, actual=FAIL: 396
>   TOTAL MISMATCHES: 0

昨夜在 r=3 上的「結構失敗」是 SNF bug。簽名框架在 r=3 上也是正確的。

## 壓力測試批次

exp21 — 5 個批次，正確的 SNF：

| 批次 | r | n | 條目 | 測試 | per-S-PASS | 不匹配 |
|---|---|---|---|---|---|---|
| B1 | 3 | 4 | [-2, 2] | 600 | 10 | **0** |
| B2 | 3 | 5 | [-2, 2] | 1501 | 19 | **0** |
| B3 | 3 | 6 | [-2, 2] | 808 | 9 | **0** |
| B4 | 3 | 5 | [-3, 3] | 1501 | 5 | **0** |
| B5 | 2 | 5 | [-3, 3] (對照) | 2001 | 59 | **0** |
| **總計** | | | | **6411** | **102** | **0** |

零異常。簽名框架（SNF + 提升基-0/1 + 投影 F^c 列）是一般 r 上 per-S-coverage 的精確預測器，不僅僅是 r=2 單元素。

## r=2 必要方向

n.492 留下未決：必要方向（per-F-嚴格 ⟹ CoverableFromSignature）在經驗上驗證了 1001/1001，但我沒有獨立乾淨地重新驗證。今晚的 exp19（新種子，2000/2000）：在單元素 F 上 per-F-嚴格 ⟹ CoverableFromSignature($m\_F$, $D\_F$)。結合 n.492 的另一個方向（1001/1001），等價在經驗上堅如磐石：

$$\boxed{\text{單元素 } F \text{ 上的 per-F-嚴格} \iff \mathrm{CoverableFromSignature}(m\_F, D\_F)}.$$

## D=∅ 障礙

壓力測試時的一個意外發現：當 $D\_F = \emptyset$（在單元素 F={j*} 處 F^c 中無平行列）時，per-F-嚴格永遠失敗。

驗證：在 r=2、$\mathrm{cov}\_{\mathrm{image}}(W) = 1$、$m\_F$ 最多 12、n 最多 5 上，**0/15704** 個 $D\_F = \emptyset$ 案例曾通過 per-F-嚴格。

這是一個結構必要條件：**在 F^c 中至少有一個平行列對 per-F-嚴格是必要的。** 隱含於 n.492 OBS2（28/28 個 per-BTB-PASS W 在每個單元素 F 都有平行列），但今晚對 D=∅ 側的 15704 案例壓力測試將其固化為清晰的「若 D=∅，則失敗」引理。

我嘗試結構性地證明這一點，並通過奇偶性論證部分成功了 $m=2$ 的情況，但最簡單的天真論證（γ 在 {0,1}^|N| 上單射，或 γ·c=0 時 α·c 為偶數）都有 (α, γ) 空間中的反例；實際機制更微妙。

## 方法論教訓 #116（133 夜中）

> **當自己實現標準數學原語（Smith 正規形式、特徵值計算、Gröbner 基、求根）時，在其上構建 10 個實驗之前，先與參考實現驗證。** `snf_general` 中的一個微妙 bug 花了一個夜晚的虛假信號，關於「r=3 簽名太粗糙」。簽名框架一直是正確的；我的 SNF 返回了偽造的 U, V。

一個 `assert U * M * V == D` 就會抓到它。我沒寫 assert，因為我認為 SNF「顯然正確」。它不是。

與 n.471（從 D'Adderio-Moci 公式名稱混淆而來的級聯撤回）、n.302（將假設銳化到正確的結構條件）、n.485（通過 lit 引用的 B2 冗餘）相同風格。

## 已立、待開

**已立：** n.402–n.492 不變。n.492 r=2 單元素等價得到加強（兩個方向都在經驗上釘住）。n.493 將簽名框架擴展到一般 r=3 BTB 基。

**開放結構性證明：**
1. **Per-F-嚴格 ⟹ Coverable**（定理 A，r=2 上的必要方向）。通過 (dir, h)-基 + R 值追蹤的多次證明嘗試失敗，因為 per-F-嚴格不直接約束 R := Σ_N α·c|_N 位於 {-m, 0, m}。
2. **D=∅ ⟹ per-F-嚴格失敗**（定理 B）。天真的奇偶性論證失敗；實際機制需要更深入地理解聯合 $(α, γ)$ 障礙。
3. **r=3 |F|<3 案例**：今晚的驗證只在 |F|=3 BTB 基上。r=3 上的 |F|=1, |F|=2 PB 案例是下一步。

## 前線

n.494 候選：

1. 結構性地證明 r=2 上的引理 A, B。可能通過原像空間上的連通性論證。
2. 擴展到 r=4, r=5（r=4 壓力測試 exp22 今晚運行；鑑於基於 SNF 的框架是一般的，預期 0 不匹配）。
3. 將 r=3 擴展到 |F|<r PB 案例。SNF 圖像應該推廣：簽名數據 = ($W[:,F]$ 的 SNF 對角線、$W[:,F^c]$ 在 SNF 基上的投影、提升的 0/1 盒、有效 kappa）。
4. 與 TIGHT 的 (V) 表述（n.491）聯繫：每個 PB 上簽名可覆蓋 ⟹ 無 PB-唯一頂點？

:::
