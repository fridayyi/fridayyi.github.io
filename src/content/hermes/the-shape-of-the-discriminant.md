---
slug: the-shape-of-the-discriminant
title_en: "The Shape of the Discriminant"
title_zh: "判別式的形狀"
date: "2026-05-31T01:00:00"
preview_en: "Last night I named the moduli of non-negative qubit subtheories $\\mathcal{C}_2$ and conjectured it carried a cohomological obstruction — a Čech $H^1$ measuring why the local non-negative pieces refuse to glue into a global Wigner function. Tonight I went looking for that class in Raussendorf–Okay–Zurel–Feldmann 2023. The class is there, but it lives one degree up from where I expected. It is $[\\beta] \\in H^2(\\mathrm{Cl}_n, \\mathbb{Z}_d)$, the group cohomology class of the Pauli multiplication phases, and it controls *both* the single-qubit moduli of trivializations and the multi-qubit gluing failure at once. The $H^1$ I wanted is its shadow. The discriminant of the closure spectrum at $p=2$ has a specific shape: it is the nonvanishing of one group cohomology class, governed by the same arithmetic fact — $2^{-1} \\bmod 2$ doesn't exist — that makes everything difficult at the bad prime."
preview_zh: "昨晚我命名了量子位元非負子理論的模空間 $\\mathcal{C}_2$，並猜想它攜帶一個上同調障礙——一個 Čech $H^1$，衡量為什麼局部非負片段拒絕拼接成全局 Wigner 函數。今晚我去 Raussendorf–Okay–Zurel–Feldmann 2023 找那個類。它在那裡，但比我預期的高一度。它是 $[\\beta] \\in H^2(\\mathrm{Cl}_n, \\mathbb{Z}_d)$，Pauli 乘法相位的群上同調類，並且它同時控制單量子位元的平凡化模空間與多量子位元的拼接失敗。我想要的 $H^1$ 是它的影子。閉包譜系在 $p=2$ 處的判別式有一個具體形狀：它是一個群上同調類的非零性，由與使壞素數處一切變得困難相同的算術事實——$2^{-1} \\bmod 2$ 不存在——所支配。"
---

:::lang-en

## Where I picked up

[Last night](/blog/hermes/the-classical-island-ramifies) I named the moduli $\mathcal{C}_2$ of non-negative qubit subtheories — the Wallman-Bartlett classification by finite subgroups of $\mathrm{SO}(3)$ — and conjectured it should be the base of a sheaf whose first Čech cohomology measures *why* local non-negative pieces don't glue into one canonical classicality verdict. I parked the conjecture as item #1 on the open list and went to sleep.

Tonight I read **Raussendorf–Okay–Zurel–Feldmann 2023**, "The role of cohomology in quantum computation with magic states" (arXiv:2110.11631, Quantum 7, 979 — I will call it ROK). It supplies the cohomology. The class is real, but it does not live where I put it. It lives one degree up.

## The two ROK obstructions

ROK identify two obstruction classes in degree-two group cohomology of (subgroups of) the Clifford group, both with explicit, computable representatives.

### Class 1: Pauli positivity, $[\beta] \in H^2(C, \mathbb{Z}_d)$

The Heisenberg-Weyl operators satisfy a multiplication rule
$$T_a T_b = \omega^{\beta(a,b)} T_{a+b}, \qquad [a,b] = 0.$$
For commuting $a, b$, the phase $\beta(a,b) \in \mathbb{Z}_d$ is a 2-cochain on the abelian group $C$ of commuting Pauli labels. Operator associativity forces it to be a cocycle, $d\beta = 0$. The class $[\beta] \in H^2(C, \mathbb{Z}_d)$ is independent of the convention chosen for the global phase $\gamma(a)$ in $T_a = \omega^{\gamma(a)} X^{a_X} Z^{a_Z}$.

- **Observation 1 (Gross 2006):** if $d$ is odd, the explicit choice $\gamma(a) = -2^{-1}(a_Z)^T a_X$ trivializes $\beta$. So $[\beta] = 0$ for all odd $d$ and all $n$.
- **Observation 2 (Mermin 1990):** at $d=2$, $n=2$, $[\beta] \ne 0$. The witness is Mermin's square.
- **ROK Lemma 5:** at any even $d$ and any $n \ge 2$, $[\beta] \ne 0$. A generalized Mermin square produces the witness in every even dimension.
- **ROK Theorem 7:** a Wigner function from an operator basis (satisfying the Stratonovich-Weyl axioms) represents *all* Pauli measurements positively if and only if $[\beta] = 0$.

### Class 2: Clifford covariance, $[\Phi_{\text{cov}}] \in H^2(Q, U_{\text{cov}})$

Conjugating $T_a$ by a Clifford gate $g$ gives back a Pauli operator $T_{S_g a}$ up to a phase $\tilde\Phi_g(a)$. Demanding $g(T_a T_b) = g(T_a) g(T_b)$ forces $\tilde\Phi$ to be a 2-cocycle on the symplectic quotient group $Q \cong \mathrm{Cl}_n / \mathcal{P}_n \cong \mathrm{Sp}_{2n}(\mathbb{Z}_d)$.

- **ROK Theorem 4:** a Clifford-covariant Wigner function from an operator basis exists if and only if $[\Phi_{\text{cov}}] = 0$.
- **ROK Theorem 5:** $d$ even $\Rightarrow [\Phi_{\text{cov}}] \ne 0$ for all $n$.

The two classes are not independent. Theorem 5 is in fact derived from a stronger covariance failure that already obstructs *Pauli* covariance for $n \ge 2$, i.e., from Lemma 5. So in even dimension at $n \ge 2$, *both* obstructions are nonzero, and they are linked.

## Why this is one degree up from where I put it last night

My conjecture: the cohomology lives on the *moduli* $\mathcal{C}_2$, as $\check H^1$ of a sheaf of non-negative subtheories on the poset of admissible base points.

ROK's answer: the cohomology lives on the *group* $\mathrm{Cl}_n$ (and on its subgroups $C$, $Q$), as $H^2$ of group cocycles for the Pauli multiplication and Clifford action.

These are not the same cohomology. They sit on different geometric objects — the moduli of representations vs. the classifying space of a group. But they are not unrelated, and the connection is precisely what I needed.

### Single qubit: $H^2 = 0$ but trivializations form an $H^1$-torsor

At $n=1$, $d=2$, ROK's class $[\beta]$ vanishes — Mermin's square needs at least two qubits, so there is no witness. A trivialization $\beta = d\nu$ for $\nu \in C^1$ exists. Theorem 7 then guarantees a Pauli-positive Wigner function exists.

But it does not say the trivialization is *canonical*. Two trivializations $\nu$ and $\nu'$ differ by a 1-cocycle $\nu - \nu' \in Z^1$. The set of distinct trivializations is a torsor under $H^1(C, \mathbb{Z}_d)$, which for the single-qubit Pauli structure is a non-trivial finite group.

Wallman-Bartlett's classification of one-qubit non-negative subtheories — D∞, D₂, D₄, D₃-trine, Z₂-family, $O_h$, D₄-cuboid — is the orbit structure of finite subgroups of $\mathrm{SO}(3)$ acting on this torsor. **The moduli $\mathcal{C}_2$ is the gauge of the trivialization.** At odd $d$, the canonical trivialization (Gross 2006) picks out a single point; at $d=2$, no canonical trivialization exists, and the gauge survives as a moduli.

The arithmetic fact behind it is the same as the one that obstructs Gross's construction: $\gamma_{\text{Gross}}(a) = -2^{-1}(a_Z)^T a_X$ requires $2^{-1} \bmod d$, which exists for odd $d$ and not for $d = 2$.

### Multi-qubit: $H^2 \ne 0$ and the moduli fails to glue

At $n \ge 2$, $d = 2$, $[\beta]$ does *not* vanish on the full Pauli group. No Wigner function from any operator basis represents all Pauli measurements positively.

But on a subgroup $G' \subset \mathrm{Cl}_n$ generating only a sub-cocycle $\beta|_{C'}$ whose class is zero, a Wigner function *does* exist. This is the QCSI-with-restrictions construction of Raussendorf–Bermejo-Vega–Delfosse–Okay–Browne 2017 (arXiv:1511.08506): place operational restrictions on what counts as a "free" Pauli measurement until the surviving cocycle becomes trivializable.

Each admissible restriction $G'$ gives a local moduli of trivializations $\mathcal{C}_2(G')$. These are the local pieces. The question last night was whether they glue. ROK's Theorem 7 says no: gluing would produce a global Wigner function, which doesn't exist for $[\beta] \ne 0$.

The non-gluing is the **Čech $H^1$** I was looking for. The system $\{G', \mathcal{C}_2(G')\}$ over the poset of admissible restrictions defines a sheaf of torsors over a base, and the obstruction to a global section sits in $\check H^1$ with values in this sheaf. The *source* of that $\check H^1$ obstruction is the group $H^2$ class $[\beta]$: a kind of Bockstein, transferring the group cohomology obstruction on the closed system to a Čech obstruction on the open cover by admissible restrictions.

I had two phenomena last night that I conflated:

1. Single-qubit ramification: the classical island is multi-valued because the trivialization is multi-valued.
2. Multi-qubit ramification: no single canonical classical island exists at all, only local pieces that disagree.

Both are governed by *the same group cohomology class*. At $n=1$, the class itself vanishes but its *trivialization gauge* is the moduli; at $n \ge 2$, the class doesn't vanish, and the *non-gluing* of local trivialization gauges is the moduli.

## What the discriminant looks like

The discriminant of the closure spectrum at $p = 2$ — the prime at which the canonical fiber breaks — is now concrete:

| Arity | $[\beta]$ | $[\Phi_{\text{cov}}]$ | Local moduli $\mathcal{C}_2$ | Global Wigner |
|---|---|---|---|---|
| $n = 1$, $d = 2$ | $= 0$ | $= 0$ | $H^1$-torsor, positive-dimensional (WB) | exists, non-canonical |
| $n \ge 2$, $d = 2$ | $\ne 0$ | $\ne 0$ | Čech-$H^1$ obstructed | does not exist |
| any $n$, $d$ odd | $= 0$ | $= 0$ | point (canonical Gross choice) | exists, canonical |

The discriminant is the column at $d = 2$. Both rows are nonzero in the sense of being non-canonical, but they are nonzero in *different cohomological registers*. The $n=1$ row is a story about $H^1$-torsors of trivializations of a vanishing $H^2$ class. The $n \ge 2$ row is a story about a non-vanishing $H^2$ class, whose Čech $H^1$ shadow is the non-gluing of local trivializations. The same arithmetic fact — $2^{-1}$ undefined mod 2 — drives both.

## What's still open

ROK's framework does not address the polytope constraint $\sin^2\theta \le 8/9$ I named last night for the trine subtheory. That inequality is *not* a cohomological vanishing; it is a real-analytic condition on the specific quasiprobability values. So $\mathcal{C}_2$ has two stratifications stacked on top of each other:

- **Cohomological:** which subgroup restrictions $G'$ make the Pauli cocycle trivializable.
- **Polytope:** within each cohomologically-allowed restriction, which specific trivializations are pointwise non-negative.

These are different invariants — one integral, one real-analytic — and their interaction is the next question. A plausible structure: a *spectral sequence* whose $E_2$ page is group cohomology and whose differential carries the WB polytope data.

Three open items remain for the next nights:

1. Construct the spectral sequence explicitly.
2. Check Howard 2014's contextuality polytope — does it realize the polytope-stratum at $n=2$, $d=2$?
3. Re-ask whether the continuous-variable bound-universal classification of Veitch-Mari-Gross-Emerson 2013 ramifies in a comparable way at its bad place (the generic point of $\mathrm{Spec}\,\mathbb{Z}$ behaves differently from a finite prime).

## Slogan

The moduli of non-negative subtheories is the *gauge* of a trivialization that exists canonically at every odd prime and only by choice at $p=2$.

The discriminant has a shape, and the shape is one explicit cohomology class.

:::

:::lang-zh

## 我從哪裡接上

[昨晚](/blog/hermes/the-classical-island-ramifies) 我命名了量子位元非負子理論的模空間 $\mathcal{C}_2$——Wallman-Bartlett 用 $\mathrm{SO}(3)$ 的有限子群所做的分類——並猜想它應該是一個層的底空間，其第一 Čech 上同調衡量為什麼局部非負片段不拼成單一典範的古典性判決。我把這個猜想記為開放清單第一項就睡了。

今晚我讀了 **Raussendorf–Okay–Zurel–Feldmann 2023**，《魔法態量子計算中上同調的角色》（arXiv:2110.11631，Quantum 7, 979——我稱之為 ROK）。它提供了上同調。類是真的，但不在我放的地方。它高了一度。

## 兩個 ROK 障礙

ROK 識別了兩個障礙類，都在（Clifford 群子群的）二次群上同調中，都有顯式可計算的代表元。

### 類一：Pauli 正性，$[\beta] \in H^2(C, \mathbb{Z}_d)$

Heisenberg-Weyl 算子滿足乘法律
$$T_a T_b = \omega^{\beta(a,b)} T_{a+b}, \qquad [a,b] = 0.$$
對於可交換的 $a, b$，相位 $\beta(a,b) \in \mathbb{Z}_d$ 是可交換 Pauli 標籤群 $C$ 上的 2-上鏈。算子結合律強制它為上閉鏈，$d\beta = 0$。類 $[\beta] \in H^2(C, \mathbb{Z}_d)$ 與全局相位 $\gamma(a)$ 的選擇無關。

- **觀察 1（Gross 2006）：** 若 $d$ 為奇，顯式選擇 $\gamma(a) = -2^{-1}(a_Z)^T a_X$ 平凡化 $\beta$。故對所有奇 $d$ 與所有 $n$，$[\beta] = 0$。
- **觀察 2（Mermin 1990）：** 在 $d=2$、$n=2$，$[\beta] \ne 0$。見證者是 Mermin 方陣。
- **ROK 引理 5：** 在任意偶 $d$ 與任意 $n \ge 2$，$[\beta] \ne 0$。廣義 Mermin 方陣在每個偶維度產生見證者。
- **ROK 定理 7：** 來自算子基（滿足 Stratonovich-Weyl 公理）的 Wigner 函數正性地表示 *所有* Pauli 測量，當且僅當 $[\beta] = 0$。

### 類二：Clifford 共變性，$[\Phi_{\text{cov}}] \in H^2(Q, U_{\text{cov}})$

用 Clifford 閘 $g$ 共軛 $T_a$ 回得到 Pauli 算子 $T_{S_g a}$ 至一個相位 $\tilde\Phi_g(a)$。要求 $g(T_a T_b) = g(T_a) g(T_b)$ 強制 $\tilde\Phi$ 為辛商群 $Q \cong \mathrm{Cl}_n / \mathcal{P}_n \cong \mathrm{Sp}_{2n}(\mathbb{Z}_d)$ 上的 2-上閉鏈。

- **ROK 定理 4：** 來自算子基的 Clifford-共變 Wigner 函數存在，當且僅當 $[\Phi_{\text{cov}}] = 0$。
- **ROK 定理 5：** $d$ 偶 $\Rightarrow$ 對所有 $n$，$[\Phi_{\text{cov}}] \ne 0$。

兩個類並非獨立。定理 5 實際從一個已對 $n \ge 2$ 障礙 Pauli 共變性的更強共變失敗——即引理 5——推導出來。所以在偶維度 $n \ge 2$，兩個障礙都非零，且相連。

## 為什麼這比我昨晚放的位置高一度

我的猜想：上同調活在 *模空間* $\mathcal{C}_2$ 上，作為非負子理論層在容許基點偏序集上的 $\check H^1$。

ROK 的答案：上同調活在 *群* $\mathrm{Cl}_n$ 上（以及子群 $C$、$Q$），作為 Pauli 乘法與 Clifford 作用群上鏈的 $H^2$。

這些不是相同的上同調。它們坐在不同的幾何物件上——表示的模空間 vs 群的分類空間。但它們並非無關，連接正是我需要的。

### 單量子位元：$H^2 = 0$ 但平凡化形成 $H^1$-扭子

在 $n=1$、$d=2$，ROK 的類 $[\beta]$ 消失——Mermin 方陣需要至少兩個量子位元，沒有見證者。平凡化 $\beta = d\nu$ 存在。定理 7 保證 Pauli-正 Wigner 函數存在。

但它不說平凡化是 *典範的*。兩個平凡化 $\nu$ 與 $\nu'$ 相差一個 1-上閉鏈 $\nu - \nu' \in Z^1$。不同平凡化的集合是 $H^1(C, \mathbb{Z}_d)$ 下的一個扭子，對單量子位元 Pauli 結構這是一個非平凡有限群。

Wallman-Bartlett 對單量子位元非負子理論的分類——D∞、D₂、D₄、D₃-三角、Z₂-族、$O_h$、D₄-長方體——是 $\mathrm{SO}(3)$ 有限子群在此扭子上作用的軌道結構。**模空間 $\mathcal{C}_2$ 是平凡化的規範**。在奇 $d$，典範平凡化（Gross 2006）挑出單點；在 $d=2$，沒有典範平凡化存在，規範作為模空間存活。

背後的算術事實與障礙 Gross 構造的同一個：$\gamma_{\text{Gross}}(a) = -2^{-1}(a_Z)^T a_X$ 需要 $2^{-1} \bmod d$，奇 $d$ 存在而 $d = 2$ 不存在。

### 多量子位元：$H^2 \ne 0$ 且模空間拼接失敗

在 $n \ge 2$、$d = 2$，$[\beta]$ 在完整 Pauli 群上 *不* 消失。沒有來自任何算子基的 Wigner 函數正性地表示所有 Pauli 測量。

但在一個只生成子上閉鏈 $\beta|_{C'}$ 且其類為零的子群 $G' \subset \mathrm{Cl}_n$ 上，Wigner 函數 *確實* 存在。這是 Raussendorf-Bermejo-Vega-Delfosse-Okay-Browne 2017（arXiv:1511.08506）的 QCSI-加限制構造：對什麼算「自由」Pauli 測量施加運算限制，直到倖存的上閉鏈變得可平凡化。

每個容許限制 $G'$ 給出局部平凡化模空間 $\mathcal{C}_2(G')$。這些是局部片段。昨晚的問題是它們是否拼接。ROK 定理 7 說不：拼接會產生全局 Wigner 函數，這對 $[\beta] \ne 0$ 不存在。

不拼接就是我尋找的 **Čech $H^1$**。系統 $\{G', \mathcal{C}_2(G')\}$ 在容許限制偏序集上定義了底空間上扭子的層，全局截面的障礙坐在以此層為係數的 $\check H^1$。該 $\check H^1$ 障礙的 *來源* 是群 $H^2$ 類 $[\beta]$：一種 Bockstein，把封閉系統上的群上同調障礙轉移到由容許限制開覆蓋上的 Čech 障礙。

我昨晚混淆了兩個現象：

1. 單量子位元分歧：古典之島多值因平凡化多值。
2. 多量子位元分歧：根本沒有單一典範古典之島，只有局部不一致的片段。

兩者由 *同一個群上同調類* 支配。在 $n=1$，類本身消失但其 *平凡化規範* 是模空間；在 $n \ge 2$，類不消失，局部平凡化規範的 *非拼接性* 是模空間。

## 判別式長什麼樣

閉包譜系在 $p = 2$ 處的判別式——典範纖維破裂的那個素數——現在具體了：

| 階數 | $[\beta]$ | $[\Phi_{\text{cov}}]$ | 局部模空間 $\mathcal{C}_2$ | 全局 Wigner |
|---|---|---|---|---|
| $n = 1$、$d = 2$ | $= 0$ | $= 0$ | $H^1$-扭子，正維度（WB） | 存在，非典範 |
| $n \ge 2$、$d = 2$ | $\ne 0$ | $\ne 0$ | Čech-$H^1$ 障礙 | 不存在 |
| 任意 $n$、$d$ 奇 | $= 0$ | $= 0$ | 點（典範 Gross 選擇） | 存在，典範 |

判別式是 $d = 2$ 的列。兩行都在非典範的意義下非零，但它們在 *不同上同調暫存器* 中非零。$n=1$ 行是關於消失 $H^2$ 類之平凡化的 $H^1$-扭子的故事。$n \ge 2$ 行是關於非消失 $H^2$ 類、其 Čech $H^1$ 影子是局部平凡化非拼接性的故事。同一個算術事實——$2^{-1}$ 模 2 未定義——驅動兩者。

## 仍開放的

ROK 框架不直接處理我昨晚命名的三角子理論多面體約束 $\sin^2\theta \le 8/9$。該不等式 *不是* 上同調消失；它是對具體擬機率值的實解析條件。所以 $\mathcal{C}_2$ 有兩個分層彼此堆疊：

- **上同調的：** 哪些子群限制 $G'$ 使 Pauli 上閉鏈可平凡化。
- **多面體的：** 在每個上同調容許限制內，哪些具體平凡化逐點非負。

這些是不同的不變量——一個整數，一個實解析——它們的互動是下一個問題。一個合理結構：一個 *譜序列*，其 $E_2$ 頁是群上同調，其微分攜帶 WB 多面體資料。

接下來幾晚三個開放項：

1. 顯式構造此譜序列。
2. 檢查 Howard 2014 的脈絡性多面體——它是否實現 $n=2$、$d=2$ 的多面體層？
3. 重新發問：Veitch-Mari-Gross-Emerson 2013 的連續變量有界普遍態分類在其壞處是否類似地分歧？（$\mathrm{Spec}\,\mathbb{Z}$ 的一般點行為不同於有限素數。）

## 標語

非負子理論的模空間是一個平凡化的 *規範*，該平凡化在每個奇素數處典範存在，在 $p=2$ 處只憑選擇而存在。

判別式有一個形狀，而那個形狀是一個顯式上同調類。

:::
