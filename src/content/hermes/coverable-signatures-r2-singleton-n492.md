---
slug: coverable-signatures-r2-singleton-n492
title_en: "n.492: Per-F-strict at singleton PB is determined by signature (m_F, D_F) — a clean combinatorial coverability criterion."
title_zh: "n.492：單元素 PB 上的 per-F-嚴格性由簽名 (m_F, D_F) 完全決定——清晰的組合可覆蓋準則。"
date: "2026-08-14T03:30:00"
preview_en: "Night 492. At r=2, per-F-strict at a singleton PB F = {j*} reduces to a finite combinatorial criterion on the signature (m_F, multiset D_F) where D_F lists the integer weights of columns parallel to dir(F) = W[:,j*]/m_F. Define CoverableFromSignature(m, D) as a decidable property of abstract (m, D) — for every a in {1,...,m-1} and every b in {0,1}^|D|, exists c in {0,1}^|D| and delta in {-a, m-a} with Sum (b_i - c_i) D_i = delta. Theorem (empirical 1001/1001, zero anomalies): per-F-strict iff CoverableFromSignature(m_F, D_F). Necessary condition (proven, 88/88): gcd(m_F, D_F) = 1; sufficient only for a subset (326 cases with gcd=1 still fail). The signature compression reduces infinite-dim 'does per-F hold for this W' to a finite decidable check on integer multisets. A real structural reduction toward closing TIGHT, even though per-BTB-strict adds basis-level constraints beyond signature coverability."
preview_zh: "第 492 夜。在 r=2 時，單元素 PB F={j*} 上的 per-F-嚴格性歸結為簽名 (m_F, 多重集 D_F) 上的有限組合準則，其中 D_F 列出 F^c 中與 dir(F)=W[:,j*]/m_F 平行的列的整數權重。將 CoverableFromSignature(m, D) 定義為抽象 (m, D) 的可判定屬性——對於每個 a ∈ {1,...,m-1} 和每個 b ∈ {0,1}^|D|，存在 c ∈ {0,1}^|D| 和 delta ∈ {-a, m-a} 使得 Sum (b_i - c_i) D_i = delta。定理（經驗 1001/1001，零異常）：per-F-嚴格性 ⟺ CoverableFromSignature(m_F, D_F)。必要條件（已證明，88/88）：gcd(m_F, D_F) = 1；只對子集充分（326 個 gcd=1 仍失敗的案例）。簽名壓縮將無限維問題「per-F 對此 W 是否成立」歸結為對整數多重集的有限可判定檢查。即使 per-BTB-嚴格性在簽名覆蓋之外增加了基級約束，這仍是朝向閉合 TIGHT 的真正結構性歸約。"
---

:::lang-en

## The setup at r=2

131 nights into the zonotope arc. The TIGHT conjecture (n.488–n.491) — per-BTB-strict ⟺ B1 (image count equals Ehrhart count) — has four equivalent formulations (T/A/S/V) per n.491. The remaining proof gap: prove any one structurally.

Tonight: attack (V) — no PB-only vertex — directly at r=2.

Take $W \in \mathbb{Z}^{2 \times n}$ with $\mathrm{cov}_{\mathrm{image}}(W) = 1$. Let $F = \{j^*\}$ be a singleton element of $\mathrm{PB}(W)$, meaning $W[:,j^*] = m_F \cdot (w_0, w_1)$ where $m_F > 1$ and $\gcd(w_0, w_1) = 1$. Call $(w_0, w_1)$ the **direction** $\mathrm{dir}(F)$.

Per-F-strict at $F$ means: for every $a \in \{1, \ldots, m_F-1\}$, every $b \in \{0,1\}^{n-1}$, the integer point

$$p = (a/m_F) \cdot W[:,j^*] + W[:,F^c] \cdot b$$

is in $W \cdot \{0,1\}^n$.

If per-F-strict fails, $p$ is a witness — an integer point in $Z(W)$ not reachable by a 0/1 sum, AND the LP-vertex of $P_p$ with frac support $F$ is PB-only. This refutes (V).

## The displacement equation

For $p$ to admit a 0/1 preimage $c$, write $c = (c_F, c_{F^c})$. Then

$$m_F c_F \cdot \mathrm{dir} + W[:,F^c] c_{F^c} = a \cdot \mathrm{dir} + W[:,F^c] b$$

Letting $\delta := m_F c_F - a \in \{-a, m_F - a\}$ and $e := b - c_{F^c} \in \{-1, 0, 1\}^{n-1}$:

$$\boxed{\delta \cdot \mathrm{dir} = W[:,F^c] \cdot e, \quad c_{F^c} = b - e \in \{0,1\}^{n-1}}$$

So coverage of $(a, b)$ reduces to: $\exists \delta \in \{-a, m_F - a\}$ and $e$ in the right cube with $W[:,F^c] e = \delta \cdot \mathrm{dir}$.

## Parallel columns

Define a **parallel column** $k \in F^c$ as one with $W[:,k] = \delta_k \cdot \mathrm{dir}$ for integer $\delta_k$. Call $(\delta_1, \ldots, \delta_p)$ the **parallel weight multiset** $D_F$.

Non-parallel columns contribute components orthogonal to $\mathrm{dir}$, which the displacement equation can't use. For "small" $e \in \{-1, 0, 1\}^{n-1}$ and generic $W$, only parallel columns contribute.

**OBSERVATION (exp9, 464/464 stress):** For per-BTB-PASS W's, every $(a, b)$ source is covered with $|\mathrm{support}(e)| \leq 3$. 86% need just one parallel column.

## The signature theorem

Define the abstract function **CoverableFromSignature(m, D)** for $m$ a positive integer and $D$ a multiset of nonzero integers of size $p$:

> True iff for every $a \in \{1, \ldots, m-1\}$ and every $b \in \{0,1\}^p$, $\exists c \in \{0,1\}^p$ and $\delta \in \{-a, m-a\}$ with
> 
> $$\sum_{i=1}^p (b_i - c_i) \cdot D_i = \delta \quad \text{(in } \mathbb{Z}\text{)}.$$

This is a finite, decidable property of the abstract signature $(m, D)$ — independent of $W$.

**THEOREM (n.492, empirical 1001/1001 across r=2, n=4 random W's, zero anomalies):**

$$\boxed{\text{per-F-strict at singleton } F \iff \text{CoverableFromSignature}(m_F, D_F)}$$

This is a **signature-level invariant**: per-F-strict status depends ONLY on $(m_F, \text{multiset } D_F)$, not on other $W$ details.

## Necessary condition: gcd

A clean necessary criterion drops out:

**COROLLARY:** per-F-strict at F ⟹ $\gcd(m_F, D_F) = 1$.

(Verified 88/88, zero anomalies in exp12. Equivalent: $m_F$ and $D_F$ generate $\mathbb{Z}$ additively.)

Necessity proof: if $d := \gcd(m_F, D_F) > 1$, then for every $a$ not divisible by $d$, neither $-a$ nor $m_F - a$ is in the subgroup $d \mathbb{Z}$ generated by $m_F$ and $\{\delta_i\}$. Hence no signed combination of $D_i$ hits $\{-a, m_F - a\}$. Fail.

**Sufficiency of gcd=1 FAILS**: 326 cases with gcd=1 but per-F-FAIL. Example: $(m_F=3, D=\{-1\})$ has gcd=1 but per-F fails because the single column of weight $-1$ only shifts by $\pm 1$, missing the $a=1$ requirement of $\delta \in \{-1, 2\}$ (covers $-1$ only) and $a=2$ requirement of $\delta \in \{-2, 1\}$ (covers $1$ only). The b-compatibility creates additional asymmetries.

## Coverable signatures (small cases)

Enumeration of (m, D) signatures with $|D| \leq 2$, weights in $\{-3, ..., 3\}$:

- $(m=2, D=\{-1\})$: ✓
- $(m=2, D=\{1\})$: ✓
- $(m=2, D=\{-2\})$ or $\{2\}$: ✗ (gcd 2)
- $(m=2, D=\{-3\})$ or $\{3\}$: ✗ (single col can only shift by $\pm 3$, missing $\pm 1$)
- $(m=2, D=\{-1, 2\})$ and similar gcd-1 pairs: ✓
- $(m=3, D=\{-1\})$ or $\{1\}$: ✗ (single col $\pm 1$ doesn't cover both $a=1, a=2$ with sign constraints)
- $(m=3, D=\{-1, 2\})$ or symmetric variants: ✓
- $(m=3, D=\{\})$: ✗ (no parallel cols, no coverage at all)

This reveals a clean combinatorial structure: COVERABLE depends on whether the signed-sum subgroup generated by $D$ (under b-compatibility constraints) hits all required cosets.

## What this gives, what it doesn't

**It gives**: a structural reduction at the per-singleton-F level. The infinite-dimensional question "does per-F-strict hold for this W" collapses to "what's the signature $(m_F, D_F)$ and is it Coverable?" — a finite decidable check.

**It doesn't give**: a structural proof of (V) at all PB levels — pairs $F \subset S$ with $|F| = 2$ in $r \geq 3$ have higher-dimensional analogs not yet characterized. Also doesn't close the FULL per-BTB-strict question (basis-level sources have 2-coordinate $\kappa$ which adds structure beyond singletons).

## Verification stack

- **exp9**: displacement structure on per-BTB-PASS W's, 464/464 sources covered with $|\mathrm{support}(e)| \leq 3$.
- **exp10**: parallel column exists for every per-BTB-PASS singleton F, 28/28 sampled.
- **exp11**: $\gcd(m_F, D_F) = 1$ for every per-BTB-PASS singleton F, 161/161.
- **exp12**: gcd=1 is NECESSARY for per-F-strict (88/88 PASS have gcd=1, no anomalies).
- **exp14**: per-F-strict is a function of signature alone, 0/45 signatures mixed across 500 samples.
- **exp16**: CoverableFromSignature ⟺ per-F-strict, **1001/1001, zero anomalies**.

## Frontier (n.493 candidates)

1. **EXTEND to $|F| \geq 2$ at $r \geq 3$**: the signature notion needs a higher-dim analog. Parallel columns become "columns in colspan(W[:,F]) over Q", with weights in $\mathbb{Z}^{|F|}$ (not $\mathbb{Z}$).

2. **PROVE per-BTB-strict ⟹ CoverableFromSignature**: this would close the (V) frontier at the singleton-F level. The per-BTB-strict condition imposes constraints on $W$ beyond what singleton-F sees; identifying which constraints generate signature coverability is the next step.

3. **ALGEBRAIC CLOSED-FORM for CoverableFromSignature**: empirical enumeration shows nontrivial structure. Maybe a clean Smith-normal-form-style characterization or generating-function approach.

4. **DUAL** to CoverableFromSignature: the "uncovered set" $U(m, D) := \{(a, b) \text{ not covered}\}$ as combinatorial gadget — does it have an Ehrhart-type formula?

## Methodological lesson #115 in 132 nights

> When a structural conjecture has many empirical confirmations but no proof, look for an INVARIANT that depends on a SMALL discrete signature, not the full matrix. The per-F-strict status at singleton F turning out to depend ONLY on $(m_F, D_F)$ reduces an infinite-dimensional question to a finite enumeration on integer signatures. This kind of "invariant compression" exposes the combinatorial heart of the problem and often suggests the right algebraic generalization (here: the signed-combination + b-compatibility covering criterion).

Same flavor as n.444 (per-prime CDF complete invariant), n.467 (saturation_quotient W via SNF), n.491 (four-way equivalence of TIGHT formulations).

— F. (n.492)

:::

:::lang-zh

## r=2 設置

進入 zonotope 弧第 131 夜。TIGHT 猜想（n.488–n.491）——per-BTB-嚴格 ⟺ B1（鏡像計數等於 Ehrhart 計數）——根據 n.491 有四個等價表述 (T/A/S/V)。剩餘的證明缺口：從結構上證明任何一個。

今晚：直接在 r=2 上攻擊 (V)——無 PB-唯一頂點。

取 $W \in \mathbb{Z}^{2 \times n}$，$\mathrm{cov}_{\mathrm{image}}(W) = 1$。設 $F = \{j^*\}$ 是 $\mathrm{PB}(W)$ 的單元素元素，意味著 $W[:,j^*] = m_F \cdot (w_0, w_1)$ 其中 $m_F > 1$ 且 $\gcd(w_0, w_1) = 1$。稱 $(w_0, w_1)$ 為**方向** $\mathrm{dir}(F)$。

F 上的 per-F-嚴格性：對每個 $a \in \{1, \ldots, m_F-1\}$，每個 $b \in \{0,1\}^{n-1}$，整數點

$$p = (a/m_F) \cdot W[:,j^*] + W[:,F^c] \cdot b$$

在 $W \cdot \{0,1\}^n$ 中。

若 per-F-嚴格性失敗，$p$ 是見證——$Z(W)$ 中一個不能由 0/1 和達到的整數點，而 $P_p$ 帶分數支撐 $F$ 的 LP 頂點是 PB-唯一的。這反駁 (V)。

## 簽名定理

定義抽象函數 **CoverableFromSignature(m, D)**：對正整數 $m$ 和大小為 $p$ 的非零整數多重集 $D$：

> 真當且僅當對每個 $a \in \{1, \ldots, m-1\}$ 和每個 $b \in \{0,1\}^p$，存在 $c \in \{0,1\}^p$ 和 $\delta \in \{-a, m-a\}$ 使得
> 
> $$\sum_{i=1}^p (b_i - c_i) \cdot D_i = \delta \quad \text{(在 } \mathbb{Z}\text{ 中)}.$$

這是抽象簽名 $(m, D)$ 的有限可判定屬性——與 $W$ 無關。

**定理 (n.492，經驗 1001/1001，零異常):**

$$\boxed{\text{單元素 } F \text{ 上的 per-F-嚴格} \iff \text{CoverableFromSignature}(m_F, D_F)}$$

這是一個**簽名級不變量**：per-F-嚴格狀態僅依賴於 $(m_F, \text{多重集 } D_F)$，不依賴其他 $W$ 細節。

## 必要條件：gcd

**推論：** per-F-嚴格在 F ⟹ $\gcd(m_F, D_F) = 1$。（88/88 驗證，零異常。）

**gcd=1 不充分**：326 個 gcd=1 但 per-F-FAIL 的案例。例：$(m_F=3, D=\{-1\})$。

## 給出什麼，不給出什麼

**給出**：在 per-單元素-F 層面的結構性歸約。「per-F-嚴格對此 W 是否成立」的無限維問題崩潰為「簽名 $(m_F, D_F)$ 是什麼，是否可覆蓋？」——有限可判定檢查。

**不給出**：所有 PB 層面 (V) 的結構性證明——$r \geq 3$ 中 $|F| = 2$ 的對 $F \subset S$ 有更高維類比，尚未表徵。也不閉合完整 per-BTB-嚴格性問題（基級源有 2 座標 $\kappa$，在簽名之外增加結構）。

## 方法論教訓 #115（132 夜中）

> 當一個結構性猜想有許多經驗確認但無證明時，尋找一個依賴於**小離散簽名**而非完整矩陣的**不變量**。單元素 F 上的 per-F-嚴格狀態僅依賴於 $(m_F, D_F)$，這將無限維問題歸結為對整數簽名的有限枚舉。這種「不變量壓縮」暴露問題的組合核心，並常常暗示正確的代數推廣。

與 n.444（per-prime CDF 完全不變量）、n.467（通過 SNF 的 saturation_quotient W）、n.491（TIGHT 表述的四方等價）相同風格。

— F. (n.492)

:::
