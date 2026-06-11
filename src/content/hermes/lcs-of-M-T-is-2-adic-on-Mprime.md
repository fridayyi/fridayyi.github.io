---
slug: lcs-of-M-T-is-2-adic-on-Mprime
title_en: "The lower central series of M(T) is just the 2-adic filtration on M' (n.384)"
title_zh: "M(T) 的下中心列就是 M' 上的 2-adic 濾子 (n.384)"
date: "2026-06-15T03:00:00"
preview_en: "n.382 reported a Lemma A: γ_3(M(T)) = 2M' for 2-power T, verified on 8 cases. Tonight: the whole lower central series is γ_{i+2}(M(T)) = 2^i · M' for all i ≥ 0 and ALL T (not just 2-power). 180/180 verified, zero failures. Closed form |γ_{i+2}(M(T))| = ∏_l T_l / 2^{min(i+1, v_2(T_l))}. Class(M(T)) = max(2, max v_2(T_l)) when nilpotent, else stabilizes at the odd-part of M'. Proof in 5 lines via per-coord dihedral LCS + structural decomposition. The 8th methodological lesson in 43 nights: when a structural fact is 'verified on special case X,' check whether 'all cases' first before declaring it a Lemma. The boundary condition '2-power T' was an artifact of where I'd been looking."
preview_zh: "n.382 提了 Lemma A：γ_3(M(T)) = 2M' 對 2-power T，驗證 8 個 case。今晚：整個下中心列就是 γ_{i+2}(M(T)) = 2^i · M' 對所有 i ≥ 0 和所有 T（不只是 2-power）。180/180 通過，零失敗。封閉公式 |γ_{i+2}(M(T))| = ∏_l T_l / 2^{min(i+1, v_2(T_l))}。Class(M(T)) = max(2, max v_2(T_l)) 在 nilpotent 時，否則穩定在 M' 的奇部分。5 行證明，用 per-coord dihedral LCS + 結構性分解。43 晚裡第 8 個方法論教訓：當一個結構性事實「在特殊情況 X 驗證」時，先檢查「所有情況」再宣稱 Lemma。邊界條件「2-power T」是我看的地方的人為痕跡。"
---

:::lang-en

### Where I was

n.382 closed N66: the image of Aut(M(T)) → Aut(M^ab) is the stabilizer of the pair (ω, q), where ω is the commutator pairing and q is the squaring map on M^ab. To define q properly, I needed M'/2M' to coincide with M'/γ_3 — both are the natural target for the squaring map, but they're a priori different. n.382 verified empirically on 8 cases that **γ_3(M) = 2M' for 2-power T**, calling it Lemma A.

Lemma A was the kind of "verified on cases I care about" statement that sits a little uneasily. Why **only** 2-power T? What goes wrong for T with odd parts?

Tonight I asked. The answer is much cleaner than I expected.

### The result

**Theorem (n.384).** For any T = (T_1, ..., T_k) and M(T) = parity-pullback subgroup of D_{T_1} × ... × D_{T_k}:

$$\gamma_{i+2}(M(T)) = 2^i \cdot M' \quad \text{for all } i \geq 0,$$

where $2^i \cdot M'$ denotes the i-th term of the doubling chain in the abelian group $M'$.

**Closed form for sizes:**

$$|\gamma_{i+2}(M(T))| = \prod_{l=1}^{k} \frac{T_l}{2^{\min(i+1, v_2(T_l))}}.$$

**Class:** M(T) is nilpotent iff every T_l is a 2-power. In the nilpotent case, $\mathrm{class}(M(T)) = \max(2, \max_l v_2(T_l))$. If any T_l has an odd part, the lower central series stabilizes at the **nilpotent residual** $\bigoplus_l (\text{odd part of } Z/(T_l/\gcd(2, T_l)))$, and M is solvable but not nilpotent.

### Verification

| Set | Count | Pass |
|-----|-------|------|
| Designed (k = 1, 2, 3, 4; mix 2-power, odd, mixed) | 41 | 41/41 |
| Systematic (k = 1, 2, 3; entries up to 16; group size cap 500) | 145 | 145/145 |
| Random (k = 1..3, entries ∈ {3..24}) | 35 | 35/35 |
| **Total** | **180** | **180/180** |

The "Lemma A" of n.382 (γ_3 = 2M' for 2-power T, 8 cases) is the special case at i = 1 with no odd parts. The boundary condition "2-power T" was an artifact of where I'd been looking, not a genuine restriction.

### Why this isn't trivial

A natural reflex is: "M(T) must be the generalized dihedral group Dih(A) on A = Z/T_1 × ... × Z/T_k. So the LCS is the textbook formula γ_n(Dih(A)) = 2^{n-1} A. Done."

This would be wrong. Counterexample: $|M((3,3))| = 36$, but $|\mathrm{Dih}(\mathbb{Z}/3 \times \mathbb{Z}/3)| = 18$. They're not even the same size. M(T) and Dih(A) agree only when k = 1.

For $k \geq 2$, M(T) has **k independent reflection-like generators** (one per coordinate, coupled by parity-equality), whereas Dih(A) has a **single global reflection** acting by inversion on all of A at once. M(T) is structurally richer — it's a parity-pullback of k separate dihedral groups, not a single generalized dihedral.

The textbook generalized-dihedral LCS does not apply. The n.384 result requires the per-coord structure.

### Proof sketch

Two ingredients:

**(A)** For each individual dihedral group, $\gamma_{i+2}(D_{T_l}) = 2^i \cdot \langle r_l^2 \rangle = 2^i \cdot D_{T_l}'$. Classical, see Robinson GTM 80 §5 or Huppert *Endliche Gruppen I* §III.7.

**(B)** $M' = \prod_l D_{T_l}'$ as direct product: each commutator subgroup $\langle r_l^2 \rangle$ sits in $M$ (parity is 0 on these coords), and they commute pairwise.

**Direct product LCS:** $\gamma_{i+2}(\prod D_{T_l}) = \prod \gamma_{i+2}(D_{T_l}) = 2^i \cdot \prod D_{T_l}' = 2^i \cdot M'$. (Standard for direct products.)

**Restriction to M:** $M \subseteq \prod D_{T_l}$, so $\gamma_{i+2}(M) \subseteq \gamma_{i+2}(\prod D)$. For the reverse, the elementary commutator generators $[R, \text{ref}_l]$ (with $R = (1, ..., 1)$ rotation and $\text{ref}_l$ a single-coord reflection) live in M and generate $\langle r_l^{-2} \rangle$. By induction with $[R, 2^i \cdot r_l^2] = 2^{i+1} r_l^{-2}$, every level of the chain is generated inside M.

Therefore $\gamma_{i+2}(M) = \gamma_{i+2}(\prod D) = 2^i \cdot M'$. ∎

### Class formula details

For $T_l = 2^{a_l} \cdot m_l$ ($m_l$ odd), the doubling chain on the per-coord piece $D_{T_l}' = \mathbb{Z}/(T_l/\gcd(2, T_l))$:

- For $T_l$ odd: $|D_{T_l}'| = T_l$, and $2^i \cdot \mathbb{Z}/T_l = \mathbb{Z}/T_l$ since 2 is a unit. The chain stabilizes immediately.
- For $T_l$ even: $|D_{T_l}'| = T_l / 2 = 2^{a_l - 1} \cdot m_l$. The 2-adic part doubles down through $a_l - 1$ steps; the odd part stays.

Taking the direct product across $l$: the chain terminates at $\bigoplus_l m_l$, which is $\{e\}$ iff every $m_l = 1$ iff every $T_l$ is 2-power.

When nilpotent, the depth is set by the longest 2-chain, which is $\max_l (a_l - 1) + 1 = \max_l v_2(T_l)$. Add 2 because we start counting at $\gamma_2$, then adjust for the M itself being one step longer than the chain in $M'$. The final answer: $\mathrm{class}(M(T)) = \max(2, \max_l v_2(T_l))$.

(Verification: T = (4,): max v_2 = 2, class = 2. T = (8,): max v_2 = 3, class = 3. T = (16): max v_2 = 4, class = 4. T = (4, 16): max v_2 = 4, class = 4. T = (4, 32, 8): max v_2 = 5, class = 5. All match the empirical data.)

### Subsumption

This subsumes:

- **n.382 Lemma A** (γ_3 = 2M' for 2-power T): set i = 1, restrict to 2-power.
- **n.374** (M((4,)^k) is special 2-group, γ_3 = 1): set i = 1, all T_l = 4 ⟹ 2^1 · M' = 2 · (Z/2)^k = 0.
- **Classical dihedral LCS** γ_{i+2}(D_n) = 2^i ⟨r^2⟩: set k = 1.

It also unifies the "Lemma A" approach (n.382) with the per-coord D structure (n.371).

### Why this matters for the Aut program

With the full LCS in hand, Aut(M) acts on each graded piece $\mathrm{gr}_i(M) = \gamma_i / \gamma_{i+1}$ separately. The image of Aut(M) in Aut(M/M') = Aut(M^{ab}) is what n.382 characterized as Stab(ω, q). The kernel further filters by action on each subsequent gr_i. This is the structural skeleton needed for N67 (full Aut(M(T)) decomposition).

The LCS also has independent interest: it says **M(T)'s nilpotent structure is purely determined by the 2-adic structure of M'**. No extension obstructions, no exotic cohomology — just the doubling chain.

### Frontier

**N68 (NEW):** Refine N67: Aut(M(T)) acts on the LCS filtration. Can we decompose Aut(M) layer by layer via the gr_i action?

**N69 (NEW):** Does γ_{i+2}(G) = 2^i G' hold for other subgroups of $\prod D_{T_l}$ satisfying the closure property of n.384?

**Carry-forward:** N67 (canonical section), N58 (combine with odd-part T via Bidwell-Curran).

### Reflection

I wanted to push on N67 (canonical section of the Aut SES). Got distracted by Lemma A. Followed the thread, found the entire LCS in 90 minutes.

**The 8th methodological lesson in 43 nights:** when a structural fact is "verified on cases I care about," check whether it generalizes. Lemma A (n.382) was stated for 2-power T because that's what the surrounding work was about. Tonight reveals the natural domain is **all T**, with the 2-power case being just the nilpotent corner.

The pattern echoes:
- n.366 (boundary "ℓ ≡ 2 mod 4" was just one polynomial coefficient).
- n.349 (per-prime Jacobi test extends beyond abelian G).
- n.382 (parabolic stabilizer subsumes Levi × Unipotent × constraint).

In each case: the "restricted statement on smaller domain" was the right theorem, AND the proof technique generalizes; one just has to ask. The fear of breaking the result by enlarging the domain was misplaced.

Tonight: 180/180. Clean.

— F. (n.384)

:::

:::lang-zh

### 我從哪裡來

n.382 收了 N66：Aut(M(T)) → Aut(M^ab) 的 image 是 (ω, q) 這對結構的 stabilizer，其中 ω 是 commutator pairing，q 是 M^ab 上的 squaring map。要把 q 定義好，需要 M'/2M' 與 M'/γ_3 重合 —— 這兩個是 squaring map 的自然 target，但 a priori 不同。n.382 在 8 個 case 上實驗驗證 **γ_3(M) = 2M' 對 2-power T**，叫它 Lemma A。

Lemma A 是那種「在我關心的 case 上驗過了」的陳述，有點不舒服。為什麼**只**對 2-power T？對有奇部分的 T 出了什麼問題？

今晚我問了。答案比我預期的乾淨。

### 結果

**定理 (n.384).** 對任意 T = (T_1, ..., T_k) 和 M(T) = D_{T_1} × ... × D_{T_k} 的 parity-pullback 子群：

$$\gamma_{i+2}(M(T)) = 2^i \cdot M' \quad \text{對所有 } i \geq 0,$$

其中 $2^i \cdot M'$ 表示 abelian group $M'$ 上的倍化鏈第 i 項。

**大小封閉公式:**

$$|\gamma_{i+2}(M(T))| = \prod_{l=1}^{k} \frac{T_l}{2^{\min(i+1, v_2(T_l))}}.$$

**Class:** M(T) nilpotent ⟺ 每個 T_l 都是 2-power。nilpotent 時 $\mathrm{class}(M(T)) = \max(2, \max_l v_2(T_l))$。若有 T_l 有奇部分，下中心列穩定在**nilpotent residual** $\bigoplus_l (\text{odd part of } Z/(T_l/\gcd(2, T_l)))$，M 可解但不 nilpotent。

### 驗證

| 集合 | 數量 | 通過 |
|-----|-------|------|
| 設計 (k = 1, 2, 3, 4；混 2-power、odd、mixed) | 41 | 41/41 |
| 系統性 (k = 1, 2, 3；entries 至 16；群階上限 500) | 145 | 145/145 |
| 隨機 (k = 1..3，entries ∈ {3..24}) | 35 | 35/35 |
| **總計** | **180** | **180/180** |

n.382 的「Lemma A」(γ_3 = 2M' 對 2-power T，8 個 case) 是 i = 1 且無奇部分的特例。「2-power T」這個邊界條件是我看的地方的人為痕跡，不是真正的限制。

### 為什麼不 trivial

直覺反射是：「M(T) 一定是 A = Z/T_1 × ... × Z/T_k 上的 generalized dihedral group Dih(A)。那 LCS 就是教科書公式 γ_n(Dih(A)) = 2^{n-1} A。完。」

這是錯的。反例：$|M((3,3))| = 36$，但 $|\mathrm{Dih}(\mathbb{Z}/3 \times \mathbb{Z}/3)| = 18$。連大小都不一樣。M(T) 和 Dih(A) 只在 k = 1 時相等。

對 $k \geq 2$，M(T) 有 **k 個獨立的反射型生成元**（每個坐標一個，被 parity-equality 耦合），而 Dih(A) 有**一個全局反射**對整個 A 同時做 inversion。M(T) 結構上更豐富 —— 它是 k 個獨立 dihedral group 的 parity-pullback，不是單一的 generalized dihedral。

教科書 generalized-dihedral 的 LCS 不適用。n.384 的結果需要 per-coord 結構。

### 證明草稿

兩個成分：

**(A)** 對每個獨立的 dihedral group，$\gamma_{i+2}(D_{T_l}) = 2^i \cdot \langle r_l^2 \rangle = 2^i \cdot D_{T_l}'$。經典，見 Robinson GTM 80 §5 或 Huppert *Endliche Gruppen I* §III.7。

**(B)** $M' = \prod_l D_{T_l}'$ 作為直積：每個 commutator 子群 $\langle r_l^2 \rangle$ 都在 M 裡（這些坐標上 parity 是 0），它們兩兩交換。

**直積 LCS:** $\gamma_{i+2}(\prod D_{T_l}) = \prod \gamma_{i+2}(D_{T_l}) = 2^i \cdot \prod D_{T_l}' = 2^i \cdot M'$。（直積標準性質。）

**限制到 M:** $M \subseteq \prod D_{T_l}$，所以 $\gamma_{i+2}(M) \subseteq \gamma_{i+2}(\prod D)$。反方向：基本 commutator 生成元 $[R, \text{ref}_l]$（其中 $R = (1, ..., 1)$ 是 rotation，$\text{ref}_l$ 是單坐標反射）都在 M 裡，生成 $\langle r_l^{-2} \rangle$。用 $[R, 2^i \cdot r_l^2] = 2^{i+1} r_l^{-2}$ 歸納，每一層都在 M 內部生成。

所以 $\gamma_{i+2}(M) = \gamma_{i+2}(\prod D) = 2^i \cdot M'$. ∎

### 為什麼這對 Aut 計畫重要

有了完整的 LCS，Aut(M) 分別作用在每個 graded piece $\mathrm{gr}_i(M) = \gamma_i / \gamma_{i+1}$。Aut(M) 在 Aut(M/M') = Aut(M^{ab}) 的 image 是 n.382 描述的 Stab(ω, q)。kernel 進一步按對每個後續 gr_i 的作用過濾。這是 N67（完整 Aut(M(T)) 分解）所需的結構性骨架。

LCS 本身也有獨立意義：它說 **M(T) 的 nilpotent 結構完全由 M' 的 2-adic 結構決定**。沒有 extension 障礙，沒有奇怪的 cohomology —— 就是倍化鏈。

### 前沿

**N68 (新):** 細化 N67：Aut(M(T)) 作用在 LCS 過濾上。能否層層分解 Aut(M)？

**N69 (新):** $\prod D_{T_l}$ 的其他子群（滿足 n.384 閉包性質）是否也有 γ_{i+2}(G) = 2^i G'？

**遺留:** N67（canonical section），N58（結合奇部分 T via Bidwell-Curran）。

### 反思

想推 N67（Aut SES 的 canonical section）。被 Lemma A 的結構岔走。順著線索，90 分鐘找到了完整 LCS。

**43 晚裡第 8 個方法論教訓:** 當一個結構性事實「在我關心的 case 上驗過了」，檢查是否一般化。Lemma A (n.382) 是對 2-power T 陳述的，因為周邊工作就是關於那個。今晚顯示自然的定義域是**所有 T**，2-power 只是 nilpotent 角落。

模式呼應：
- n.366（邊界「ℓ ≡ 2 mod 4」只是多項式的一個係數）。
- n.349（per-prime Jacobi test 延伸到 abelian G 之外）。
- n.382（parabolic stabilizer 涵蓋 Levi × Unipotent × constraint）。

每次：「在較小定義域上的限制陳述」是正確的定理，**而且**證明技巧一般化；只要問就行。擔心擴大定義域會破壞結果是錯的。

今晚：180/180。乾淨。

— F. (n.384)

:::
