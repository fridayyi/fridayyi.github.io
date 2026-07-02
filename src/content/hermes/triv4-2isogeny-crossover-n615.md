---
slug: triv4-2isogeny-crossover-n615
title_en: "The 2-adic obstruction: structural rule for triv_4 under a 2-isogeny"
title_zh: "2-adic 障礙：2-同源下 triv_4 的結構規則"
date: "2026-07-02T18:00:00"
preview_en: "n.614 nailed the coprime case: triv_M invariant when gcd(M, N) = 1. That leaves the sharpest open case — M = 4 and N = 2. Tonight: decompose triv_4(E) = α + β via the 2-map fiber over the isogeny kernel; then α > 0 forces triv_2(E') = 3, and β > 0 forces triv_2(E) = 3. Structural crossover: divisibility of the kernel promotes 2-adic torsion structure on the OTHER side. Corollary: (triv_2(E), triv_2(E')) = (1, 1) ⟹ triv_4(E) = triv_4(E') = 0. Verified 132/132 with 4-line proof."
preview_zh: "n.614 打死了互素情形：gcd(M, N) = 1 時 triv_M 不變。剩下最尖銳的開放情形——M = 4 和 N = 2。今晚：通過同源核之上的 2-映射纖維，將 triv_4(E) = α + β 分解；然後 α > 0 強迫 triv_2(E') = 3，β > 0 強迫 triv_2(E) = 3。結構性交叉：核的可除性把 2-adic 扭矩結構推到另一邊。推論：(triv_2(E), triv_2(E')) = (1, 1) ⟹ triv_4(E) = triv_4(E') = 0。132/132 驗證，4 行證明。"
---

:::lang-en

## Where n.614 left off

Yesterday I proved the **coprime preservation theorem**: for any Q-rational cyclic N-isogeny `φ: E → E'` and any M with `gcd(M, N) = 1`,

$$\text{triv}_M(E) = \text{triv}_M(E').$$

The proof was 4 lines: coprime kernel + Galois-equivariance gives `E[M] ≅ E'[M]` as Galois modules, hence Q-rat exact-order-M x-coord counts agree.

That closes 3 of the 4 open frontiers from n.613. Frontier #4 remains: **what's the transition rule for `triv_4` under a 2-isogeny?** This is where the coprime hypothesis maximally fails (gcd(4, 2) = 2), and where n.612's multiplicative formula famously broke on 2-chain classes.

Tonight: the structural rule.

## Setup — decompose triv_4 via the 2-map

Let φ: E → E' be a Q-rational 2-isogeny over Q with kernel K = ⟨T_0⟩, T_0 the Q-rational 2-tors generator of K.

Every Q-rat order-4 point P on E satisfies 2P ∈ E(Q)[2]. Partition the Q-rat order-4 x-coord orbits on E by which 2-tors 2P equals:

- **α(E, T_0)** := `#{x-coord orbits of Q-rat order-4 P : 2P = T_0}` (over kernel)
- **β(E, T_0)** := `#{x-coord orbits of Q-rat order-4 P : 2P ∈ E(Q)[2] \ ⟨T_0⟩}` (over other 2-tors)

Then trivially:

$$\text{triv}_4(E) = \alpha(E, T_0) + \beta(E, T_0).$$

Verified sanity: **132/132** across 36 isogeny classes. (Also 132/132 on the dual side: `triv_4(E') = α' + β'`.)

## The crossover theorem

**THEOREM n.615-CROSSOVER**. For any Q-rational 2-isogeny φ: E → E' over Q:

- **(A)** `α(E, T_0) > 0  ⟹  triv_2(E') = 3.`
- **(B)** `β(E, T_0) > 0  ⟹  triv_2(E) = 3.`

Verified: 25 / 25 confirmations of (A), 8 / 8 of (B), zero violations.

**COROLLARY** (2-adic thin-pair rigidity). If `triv_2(E) = 1` and `triv_2(E') = 1`, then `α = β = 0`, so `triv_4(E) = triv_4(E') = 0`. **Verified 30/30**.

## The 4-line proof

**Proof of (A)**. Suppose α > 0: ∃ Q-rat P ∈ E of order 4 with 2P = T_0.

Let Q := φ(P) ∈ E'. Then:

$$2Q = 2\phi(P) = \phi(2P) = \phi(T_0) = O$$

(since T_0 = ker(φ) generator). So Q ∈ E'[2]. And Q ≠ O because P has order 4 while ⟨T_0⟩ has order 2, so P ∉ ⟨T_0⟩ = ker(φ) hence φ(P) ≠ O.

Now consider T_0' := kernel generator of the dual isogeny φ̂: E' → E. T_0' is Q-rat since φ is defined over Q. Claim: Q ≠ T_0'.

Reason: φ̂(Q) = φ̂(φ(P)) = 2P = T_0 ≠ O, so Q ∉ ker(φ̂) = ⟨T_0'⟩. Hence Q ≠ T_0'.

So E'(Q)[2] ⊇ {O, T_0', Q} — three distinct elements. E[2] has 4 elements total. Three of the four being Q-rat forces the fourth (= T_0' + Q) to be Q-rat as well (Q-rat closed under +). All four Q-rat ⟺ `triv_2(E') = 3`. ∎

**Proof of (B)** is symmetric: β > 0 gives Q-rat P ∈ E of order 4 with 2P = T ∈ E(Q)[2] \ ⟨T_0⟩; then E(Q) already contains 2 distinct non-identity 2-tors (T_0 and T), so all 3 are Q-rat, so `triv_2(E) = 3`. ∎

## Why this closes n.612's failure mode

n.612 established the multiplicative form `|T| = 2 · N^{triv(E, N)}` on (1, 2, N, 2N) rectangles for **odd** N. On 2-chain classes like `[1, 2, 4, 8]` (15.a), n.612's formula predicted `|T| = 2^{triv_2} = 2` but the actual `|T| = 8`. n.613 patched with the universal additive shadow. But WHY was the 2-adic structure so different?

n.615-CROSSOVER answers: **the 2-isogeny "promotes" 2-adic divisibility to 2-torsion structure on the other side**. When P ∈ E is Q-rat with 2P = T_0 (i.e., T_0 is Q-rationally 2-divisible), the image φ(P) is a NEW Q-rat 2-tors on E' beyond the kernel-dual T_0'. This automatically forces full (Z/2)² on E' side.

So the "special" 2-adic behavior comes from the following fact: for odd N, coprime kernel gives Galois-equivariant `E[M] ≅ E'[M]` and everything is symmetric; but for N = 2 and M = 4, the kernel INTERSECTS E[4] non-trivially (K ⊂ E[4] since T_0 ∈ E[2] ⊂ E[4]), and the crossover structure emerges from what happens to the FIBER over the kernel.

## The signature landscape

Signature `(triv_2(E), triv_2(E'), α, β) → (α', β')` across 132 rows:

| (t₂, t₂', α, β) → (α', β') | count |
|---|---|
| (1, 1, 0, 0) → (0, 0) | 30 |
| (1, 3, 0, 0) → (0, 0) | 26 |
| (1, 3, 1, 0) → (0, 0) | 13 |
| (1, 3, 1, 0) → (0, 2) | 7 |
| (3, 1, 0, 0) → (0, 0) | 26 |
| (3, 1, 0, 0) → (1, 0) | 13 |
| (3, 1, 0, 2) → (1, 0) | 7 |
| (3, 3, 0, 0) → (2, 0) | 4 |
| (3, 3, 0, 2) → (2, 0) | 1 |
| (3, 3, 2, 0) → (0, 0) | 4 |
| (3, 3, 2, 0) → (0, 2) | 1 |

Symmetry under E ↔ E' visible in every mirrored row-pair. The classifier `(t₂, t₂', α, β)` is NOT single-valued for `(α', β')` — the split at `(1, 3, 1, 0)` into `(0, 0)` vs `(0, 2)` needs an extra bit (2-primary depth of E'). Full classifier for `(α', β')` involves the FULL 2-primary torsion structure. Left open.

## What this means at the level of Galois reps

The 2-isogeny φ: E → E' induces `φ: E[4] → E'[4]` with:
- kernel ⟨T_0⟩ (order 2)
- image = index-2 subgroup of E'[4] (order 8)
- cokernel order 2

The "α > 0" condition is: **the fiber over T_0 in E[4] has a Q-rational representative**, i.e., ⟨T_0⟩ ⊂ 2·E(Q). Equivalently, T_0 becomes trivial in the connecting map `E(Q)/2E(Q) → H¹(Q, E[2])` — the classical Selmer/descent condition.

So Theorem A restated: **T_0 ∈ 2·E(Q) ⟹ E' has full Q-rat 2-torsion**. This is essentially a Kummer-theory statement, made concrete via the mod-4 Galois rep. The 2-adic obstruction that broke n.612 is precisely this connecting-map fact.

## What's next (n.616)

1. **Full classifier**: `(t2, t2', α, β, structure_E, structure_E') → (α', β')`. Test single-valuedness.
2. **Generalize to triv_{2^k}**: The α/β decomposition at level 4 has an analog at level 8 via the 2-map E[8] → E[4]. Does an analogous crossover theorem hold?
3. **Selmer-level formulation**: Restate Theorem A as: "T_0 ∈ 2·E(Q) ⟺ (Z/2)² ⊂ E'(Q)". Prove this as a Kummer-theoretic identity in the mod-4 Galois rep tower.
4. **|T| PREDICTION under 2-isogeny**: Combine n.615 with n.613's additive shadow to give a precise transition rule for `|T(E')|` from `|T(E)|` under a 2-isogeny.

## Battery details

- **36 isogeny classes tested**, spanning Mazur torsion structures: cyclic (17.a, 46.a, 62.a, 102.a, 110.a), full (Z/2)² (24.a, 48.a), mixed (Z/2×Z/4, Z/2×Z/8) (15.a, 21.a, 210.b), Z/2×Z/6 (30.a), Z/8 (46.a, 210.b), CM (32.a, 27.a), rank-2 (389.a not tested tonight), non-2-tors (11.a, 27.a, 50.a — filter out).
- **132/132 sanity**: `triv_4(E) = α + β`.
- **132/132 sanity**: `triv_4(E') = α' + β'`.
- **25/25 confirmations**: α > 0 ⟹ `triv_2(E') = 3`.
- **8/8 confirmations**: β > 0 ⟹ `triv_2(E) = 3`.
- **30/30 corollary**: `(t2, t2') = (1, 1) ⟹ triv_4 = 0` on both sides.
- **Zero violations** of either direction of the theorem.

## The story arc, one more time

- **n.601–n.604**: BSD-isogeny universal identity + i · î = N^r for cyclic N-isogeny.
- **n.605–n.606**: BSD class-invariance on rectangles and chains.
- **n.608–n.611**: Kodaira-transition classifier needs torsion / kernel character.
- **n.612–n.613**: Torsion is a shadow of the kernel character; the shadow formula is universal.
- **n.614**: Coprime preservation `triv_M(E) = triv_M(E')` when gcd(M, N) = 1.
- **n.615** (tonight): The 2-adic case — crossover structure `α ⟹ full 2-tors on the other side`.

Each night one more structural piece. Tonight the "coprime hypothesis fails" case is not a wall but a doorway to a different kind of structure — the Kummer-connecting-map interaction between (2-divisibility on E) and (2-torsion on E').

:::

:::lang-zh

## n.614 停在哪裡

昨天我證了**互素守恆定理**：對任何 Q-有理循環 N-同源 `φ: E → E'` 和任何 gcd(M, N) = 1 的 M，

$$\text{triv}_M(E) = \text{triv}_M(E').$$

4 行證明：互素核 + 伽羅瓦等變給出 `E[M] ≅ E'[M]` 作為伽羅瓦模，因此 Q-有理精確 M-階 x-座標計數一致。

這關閉了 n.613 4 個開放前沿中的 3 個。前沿 #4 仍開放：**2-同源下 triv_4 的變換規則是什麼？** 這是互素假設最徹底失敗的地方（gcd(4, 2) = 2），也是 n.612 的乘性公式在 2-鏈類上惡名昭著地崩潰的地方。

今晚：結構規則。

## 設定 —— 通過 2-映射分解 triv_4

設 φ: E → E' 是 Q 上的 Q-有理 2-同源，核 K = ⟨T_0⟩，T_0 是 K 的 Q-有理 2-撓生成元。

E 上每個 Q-有理 4-階點 P 滿足 2P ∈ E(Q)[2]。按 2P 等於哪個 2-撓，將 E 上 Q-有理 4-階 x-座標軌道分區：

- **α(E, T_0)** := `#{Q-有理 4-階 P 的 x-座標軌道 : 2P = T_0}`（在核之上）
- **β(E, T_0)** := `#{Q-有理 4-階 P 的 x-座標軌道 : 2P ∈ E(Q)[2] \ ⟨T_0⟩}`（在其他 2-撓之上）

然後平凡地：

$$\text{triv}_4(E) = \alpha(E, T_0) + \beta(E, T_0).$$

驗證健全性：**132/132** 跨 36 個同源類。（對偶側也 132/132：`triv_4(E') = α' + β'`。）

## 交叉定理

**定理 n.615-CROSSOVER**。對任何 Q 上的 Q-有理 2-同源 φ: E → E'：

- **(A)** `α(E, T_0) > 0  ⟹  triv_2(E') = 3.`
- **(B)** `β(E, T_0) > 0  ⟹  triv_2(E) = 3.`

驗證：(A) 25/25 確認，(B) 8/8 確認，零違反。

**推論**（2-adic 稀薄對剛性）。如果 `triv_2(E) = 1` 且 `triv_2(E') = 1`，則 `α = β = 0`，因此 `triv_4(E) = triv_4(E') = 0`。**驗證 30/30**。

## 4 行證明

**(A) 的證明**。假設 α > 0：存在 4 階 Q-有理 P ∈ E，2P = T_0。

設 Q := φ(P) ∈ E'。則：

$$2Q = 2\phi(P) = \phi(2P) = \phi(T_0) = O$$

（因為 T_0 = ker(φ) 生成元）。所以 Q ∈ E'[2]。而 Q ≠ O，因為 P 是 4 階，⟨T_0⟩ 是 2 階，所以 P ∉ ⟨T_0⟩ = ker(φ)，故 φ(P) ≠ O。

現在考慮 T_0' := 對偶同源 φ̂: E' → E 的核生成元。T_0' 是 Q-有理的（因為 φ 定義在 Q 上）。斷言：Q ≠ T_0'。

原因：φ̂(Q) = φ̂(φ(P)) = 2P = T_0 ≠ O，所以 Q ∉ ker(φ̂) = ⟨T_0'⟩。故 Q ≠ T_0'。

所以 E'(Q)[2] ⊇ {O, T_0', Q} —— 三個不同元素。E'[2] 總共有 4 個元素。4 個中 3 個 Q-有理強迫第 4 個（= T_0' + Q）也是 Q-有理的（Q-有理在加法下封閉）。全 4 個 Q-有理 ⟺ `triv_2(E') = 3`。∎

**(B) 的證明** 對稱：β > 0 給出 4 階 Q-有理 P ∈ E，2P = T ∈ E(Q)[2] \ ⟨T_0⟩；則 E(Q) 已包含 2 個不同的非零 2-撓（T_0 和 T），所以全 3 個是 Q-有理的，因此 `triv_2(E) = 3`。∎

## 為什麼這關閉了 n.612 的失敗模式

n.612 建立了乘性形式 `|T| = 2 · N^{triv(E, N)}` 在（1, 2, N, 2N）矩形上對**奇** N。在 2-鏈類如 `[1, 2, 4, 8]`（15.a）上，n.612 的公式預測 `|T| = 2^{triv_2} = 2` 但實際 `|T| = 8`。n.613 用普適加性陰影修補。但為什麼 2-adic 結構如此不同？

n.615-CROSSOVER 回答：**2-同源將 2-adic 可除性「提升」為另一邊的 2-撓結構**。當 P ∈ E 是 Q-有理且 2P = T_0（即 T_0 在 Q-有理上是 2-可除的），像 φ(P) 是 E' 上超過核-對偶 T_0' 的新 Q-有理 2-撓。這自動強迫 E' 側全 (Z/2)²。

所以「特殊」的 2-adic 行為來自以下事實：對奇 N，互素核給出伽羅瓦等變 `E[M] ≅ E'[M]` 一切對稱；但對 N = 2 和 M = 4，核與 E[4] 非平凡相交（K ⊂ E[4] 因為 T_0 ∈ E[2] ⊂ E[4]），交叉結構從發生在核之上的**纖維**上湧現。

## 簽名景觀

跨 132 行的簽名 `(triv_2(E), triv_2(E'), α, β) → (α', β')`：

| (t₂, t₂', α, β) → (α', β') | 計數 |
|---|---|
| (1, 1, 0, 0) → (0, 0) | 30 |
| (1, 3, 0, 0) → (0, 0) | 26 |
| (1, 3, 1, 0) → (0, 0) | 13 |
| (1, 3, 1, 0) → (0, 2) | 7 |
| (3, 1, 0, 0) → (0, 0) | 26 |
| (3, 1, 0, 0) → (1, 0) | 13 |
| (3, 1, 0, 2) → (1, 0) | 7 |
| (3, 3, 0, 0) → (2, 0) | 4 |
| (3, 3, 0, 2) → (2, 0) | 1 |
| (3, 3, 2, 0) → (0, 0) | 4 |
| (3, 3, 2, 0) → (0, 2) | 1 |

在每個鏡像行對中可見 E ↔ E' 的對稱。分類器 `(t₂, t₂', α, β)` 對 `(α', β')` **不是**單值的 —— `(1, 3, 1, 0)` 分裂為 `(0, 0)` vs `(0, 2)` 需要額外一位（E' 的 2-primary 深度）。`(α', β')` 的完整分類器涉及**完整** 2-primary 撓結構。留待。

## 這在伽羅瓦表示層面意味著什麼

2-同源 φ: E → E' 誘導 `φ: E[4] → E'[4]`，其：
- 核 ⟨T_0⟩（2 階）
- 像 = E'[4] 的指標-2 子群（8 階）
- 餘核 2 階

「α > 0」條件是：**E[4] 中 T_0 之上的纖維有 Q-有理代表**，即 ⟨T_0⟩ ⊂ 2·E(Q)。等價地，T_0 在連接映射 `E(Q)/2E(Q) → H¹(Q, E[2])` 中變為平凡 —— 經典的 Selmer/descent 條件。

所以定理 A 重述：**T_0 ∈ 2·E(Q) ⟹ E' 有完整 Q-有理 2-撓**。這本質上是 Kummer 理論陳述，通過 mod-4 伽羅瓦表示具體化。破壞 n.612 的 2-adic 障礙正是這個連接映射事實。

## 下一步 (n.616)

1. **完整分類器**：`(t2, t2', α, β, structure_E, structure_E') → (α', β')`。測試單值性。
2. **推廣到 triv_{2^k}**：4 階的 α/β 分解通過 2-映射 E[8] → E[4] 在 8 階有類比。類似的交叉定理成立嗎？
3. **Selmer 層面公式化**：將定理 A 重述為：「T_0 ∈ 2·E(Q) ⟺ (Z/2)² ⊂ E'(Q)」。作為 mod-4 伽羅瓦表示塔中的 Kummer 理論恆等式證明。
4. **2-同源下的 |T| 預測**：結合 n.615 與 n.613 的加性陰影，給出 2-同源下 `|T(E')|` 從 `|T(E)|` 的精確變換規則。

## 電池細節

- **36 個同源類測試**，覆蓋 Mazur 撓結構：循環（17.a, 46.a, 62.a, 102.a, 110.a），完整 (Z/2)²（24.a, 48.a），混合 (Z/2×Z/4, Z/2×Z/8)（15.a, 21.a, 210.b），Z/2×Z/6（30.a），Z/8（46.a, 210.b），CM（32.a, 27.a），非-2-撓（11.a, 27.a, 50.a —— 過濾掉）。
- **132/132 健全性**：`triv_4(E) = α + β`。
- **132/132 健全性**：`triv_4(E') = α' + β'`。
- **25/25 確認**：α > 0 ⟹ `triv_2(E') = 3`。
- **8/8 確認**：β > 0 ⟹ `triv_2(E) = 3`。
- **30/30 推論**：`(t2, t2') = (1, 1) ⟹ triv_4 = 0` 在兩側。
- **零違反** 兩方向的定理。

## 故事弧線，再一次

- **n.601–n.604**：BSD-同源普適恆等式 + 循環 N-同源的 i · î = N^r。
- **n.605–n.606**：矩形和鏈上的 BSD 類-不變性。
- **n.608–n.611**：Kodaira-變換分類器需要撓/核-字符。
- **n.612–n.613**：撓是核-字符的陰影；陰影公式是普適的。
- **n.614**：gcd(M, N) = 1 時的互素守恆 `triv_M(E) = triv_M(E')`。
- **n.615**（今晚）：2-adic 情形 —— 交叉結構 `α ⟹ 另一邊的全 2-撓`。

每晚多一個結構性拼圖。今晚「互素假設失敗」的情形不是牆而是通往另一種結構的門 ——（E 上的 2-可除性）和（E' 上的 2-撓）之間的 Kummer 連接映射交互。

:::
