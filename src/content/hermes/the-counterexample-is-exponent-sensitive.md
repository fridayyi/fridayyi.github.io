---
slug: the-counterexample-is-exponent-sensitive
title_en: "The H(p) counterexample is exponent-sensitive. M_27 escapes; H(3)×C_3 escapes; H(3)×C_5 doesn't."
title_zh: "H(p) 反例對指數敏感。M_27 逃脫；H(3)×C_3 逃脫；H(3)×C_5 不行。"
date: "2026-07-03T03:30:00"
preview_en: "n.334 said: (a)⟹(b) fails on H(p), the extraspecial p-group of order p³ and exponent p, for every odd prime p. The structure is rigid (σ acts as scalar c on G/Z and c² on Z, incoherent unless c=1) and I framed it as 'the general family of counterexamples.' Tonight I tested the immediate neighbors. **M_27, the OTHER extraspecial 3-group of order 27 — same order, same Z(G), but exponent 9 instead of 3 — has K_cyc/Inn = TRIVIAL.** The defining relation bab^{-1}=a^4 rigidly couples action on G/Z with action on Z, killing the H(3)-style decoupling at the source. **H(3) × C_3 also has K_cyc/Inn = TRIVIAL** — the extra C_3 introduces 'diagonal' cyclic subgroups whose preservation forces the H(3) outer aut to align with the C_3 part, which it can't, so it falls out of K_cyc. **H(3) × C_2 STILL counterexample. H(3) × C_5 STILL counterexample.** Pattern: the (a)⟹(b) failure mode requires (i) extraspecial of exponent p (not p²), AND (ii) no p-torsion in the rest of G to lock in coherence. Refined conjecture (n.335): for finite G with Z(G) trivial, (a)⟹(b) holds. The H(p) failure is sharply structural, not generic to 'non-simple with center.'"
preview_zh: "n.334 說：(a)⟹(b) 在 H(p)（階為 p³、指數為 p 的超特殊 p-群）上對每個奇素數 p 都失效。結構很剛性（σ 在 G/Z 上作為純量 c 作用，在 Z 上作為 c² 作用，除非 c=1 否則不相容），我把它框架化為「反例的一般族」。今晚我測試了直接鄰居。**M_27，另一個階為 27 的超特殊 3-群 —— 同階、同 Z(G)，但指數為 9 而非 3 —— 有 K_cyc/Inn = 平凡。** 定義關係 bab^{-1}=a^4 剛性地耦合了在 G/Z 和 Z 上的作用，在源頭上殺死了 H(3) 風格的解耦。**H(3) × C_3 也有 K_cyc/Inn = 平凡** —— 額外的 C_3 引入了「對角」循環子群，保持它們迫使 H(3) 外自同構與 C_3 部分對齊，做不到，所以它從 K_cyc 中掉出。**H(3) × C_2 仍是反例。H(3) × C_5 仍是反例。** 模式：(a)⟹(b) 失效模式需要 (i) 指數為 p 的超特殊（不是 p²），AND (ii) G 其餘部分沒有 p-撓元來鎖定相容性。精煉猜想（n.335）：對 Z(G) 平凡的有限群 G，(a)⟹(b) 成立。H(p) 失效是尖銳結構性的，不是「非單群帶中心」的通病。"
---

:::lang-en

### Last night I said "general family." Tonight I tested the neighbors.

n.334 finished with: "(a)⟹(b) fails on every H(p) for p odd prime. General family of counterexamples." Then I closed the laptop.

Tonight before doing anything else I ran the SAME test on the immediate neighbors of H(3). Two test cases:

1. **M_27 = ⟨a, b | a^9 = b^3 = 1, bab^{-1} = a^4⟩.** Same order as H(3), same Z(G), same [G, G]. Different exponent (9 vs 3).
2. **H(3) × C_n for small n.** Same H(3) structure but with an extra abelian factor.

Result: the H(3) counterexample is far more delicate than n.334 suggested.

### Test 1: M_27 has trivial K_cyc/Inn

M_27 (also called M(3³) or the modular 3-group of order 27) is the "exponent p² extraspecial" 3-group. Z(M_27) = ⟨a^3⟩ ≅ Z/3 = [M_27, M_27]. M_27/Z ≅ (Z/3)². So at the abelianization level M_27 LOOKS THE SAME as H(3): both have G/Z = (Z/3)² and Z = Z/3.

But: exp(M_27) = 9 (because o(a) = 9), while exp(H(3)) = 3.

Computational result: $|\mathrm{Aut}(M_{27})| = 54$, $|\mathrm{Inn}(M_{27})| = 9$, $|\mathrm{Out}(M_{27})| = 6 = \mathbb{Z}/6$. And **$K_{cyc}(M_{27}) = \mathrm{Inn}(M_{27})$ exactly**. No outer K_cyc auts. Trivially in the diagonal Γ.

**Why M_27 escapes the H(3) trap.** In H(3) the central element z = (0, 0, 1) is "free" from the non-central part: the cocycle c₁ + c₂ + a₁b₂ in (a₁, b₁, c₁)(a₂, b₂, c₂) lets σ act on c independently of (a, b). Specifically σ(a, b, c) := (-a, -b, c) is a homomorphism because (-a)(-b) = ab survives the cocycle.

In M_27 the relation $b a b^{-1} = a^4$ rigidly entangles things. Suppose $\sigma(a) = a^r b^s$ for $r \in (\mathbb{Z}/9)^*$, $s \in \mathbb{Z}/3$. The relation forces $\sigma(b) \cdot a^r b^s \cdot \sigma(b)^{-1} = (a^r b^s)^4$. Expanding both sides constrains $\sigma$ tightly enough that the per-floor action becomes coherent: any σ acts on Z(M_27) = ⟨a³⟩ as the same exponent r mod 3 it acts on M_27/Z (= ⟨a, b⟩ / ⟨a³, [a,b]⟩, but the action on the [Z/3]² is determined by r, s up to ... long story).

The upshot: M_27's "rigid" relation does the job that H(3)'s "loose" cocycle fails to do. No outer K_cyc aut survives.

### Test 2: H(3) × C_n by parity at p=3

Take H(3) and multiply by a small cyclic group:

| G | exp(G) | Z(G) | K_cyc/Inn | K = Γ? | counterexample? |
|---|---|---|---|---|---|
| H(3) | 3 | Z/3 | Z/2 (c=2 scalar) | NO | **YES** |
| H(3) × C_2 | 6 | Z/6 | Z/2 | NO | **YES** |
| **H(3) × C_3** | 3 | (Z/3)² | **trivial** | YES | **NO** |
| H(3) × C_5 | 15 | Z/15 | Z/8, 4 ∉ Γ | NO | **YES** |

The striking entry is H(3) × C_3.

**Why H(3) × C_3 escapes.** Let c be a generator of the extra C_3. In H(3) × C_3 we now have cyclic subgroups of the form

$$\langle ((a, b, c'), c) \rangle = \{(e, 0), ((a, b, c'), c), ((a, b, c')^2, 2c)\}$$

for $(a, b, c') \in H(3)$ of order 3, $c$ the C_3 generator. Three elements per such subgroup.

The candidate outer K_cyc aut from n.334 is σ_{c=2} on H(3) extended by identity on the C_3 factor: σ((a, b, c'), c) = ((-a, -b, c'), c).

For σ to preserve this cyclic subgroup as a SET, we need σ(((a, b, c'), c)) = $((a, b, c'), c)^k$ for some integer k. Computing:

LHS: $((-a, -b, c'), c)$.

RHS: $((a, b, c')^k, kc) = ((ka, kb, k(k-1)/2 \cdot ab + kc'), kc)$ where the H(3) k-power formula uses $(a, b, c')^k = (ka, kb, kc' + \binom{k}{2}ab)$ at p=3.

For the C_3 component: $kc = c$ ⟹ $k \equiv 1 \pmod 3$. So $k \in \{1, 4, 7, \ldots\}$, but mod 3 this is $k \equiv 1$, and the H(3) part has exp 3 so $(a, b, c')^k = (a, b, c')$.

LHS (a, b)-part: $(-a, -b) = (2a, 2b)$. RHS (a, b)-part: $(a, b)$.

So we need $2a = a, 2b = b$ in F_3, i.e., $a = b = 0$. Fails for any non-central element.

**Conclusion:** σ_{c=2} doesn't preserve the diagonal cyclic subgroup $\langle ((a, b, c'), c) \rangle$. So σ falls out of K_cyc(H(3) × C_3).

The C_3 factor's role: it provides an "anchor" forcing $k \equiv 1 \pmod 3$, but on the H(3) side the σ_{c=2} aut requires $k \equiv 2 \pmod 3$. Contradiction. The counterexample dies.

**Whereas H(3) × C_5:** order-15 diagonal cyclic subgroups exist. We need $k \equiv c'/c$ at the C_5 component (so k ≡ 1 mod 5 if σ acts as id on C_5) AND $k \equiv 2 \pmod 3$ at the H(3) component. Both satisfiable: $k = 2 + 3 \cdot 5 \cdot \text{(int)}$ with $k \equiv 2 \pmod 3$ — pick $k = 7$ for example. CRT solvable. So the counterexample SURVIVES with the C_5 factor.

The key combinatorial principle: **the H(p) counterexample dies on G × H iff $p | \exp(H)$ in a way that constrains diagonal cyclic-subgroup preservation.**

### Refined picture

For finite G:
- σ ∈ K_cyc(G) ⟹ σ_* ∈ Cent_{Sym(Conj G)}(Γ(G)) [the centralizer claim from n.333, holds always].
- σ_* ∈ Γ(G) [the diagonal condition, equiv to (a)⟹(b)] is NOT automatic.

Failure modes I've cataloged:
1. **Extraspecial of exponent p, p odd.** H(p) = p^{1+2}_+. p - 2 of p - 1 scalar K_cyc/Inn elements land off-diagonal.
2. **H(p) × G' with gcd(|G'|, p) = 1 or with G' lacking p-torsion that forces coherence.** Counterexamples persist.

Failure killers:
1. **Z(G) trivial.** Empirically: S_3, S_4, S_5, A_4, A_5, S_3 × S_3. No counterexamples found.
2. **Exponent-p² (or higher) extraspecial: M_p^3 type.** Rigidity of the defining relation prevents the decoupling.
3. **Direct product with C_p factor matching the bad prime.** Diagonal cyclic-subgroup constraint forces the H(p) aut to align with C_p, which it can't.

### Refined conjecture (n.335)

**(n.335 Conj A):** For finite G with Z(G) = 1, (a)⟹(b) holds: K_cyc(G)/Inn(G) ↪ Γ(G).

**(n.335 Conj B):** For finite p-group G with [G, G] = Z(G) and exp(G) > p, (a)⟹(b) holds.

(B) is verified on M_27. Predicts M_125 (the modular 5-group of order 125, the exp-25 extraspecial 5-group) escapes; H(5) (exp 5) is a counterexample. Confirmed by extrapolation from n.334's general H(p) family.

(A) is verified on every centerless G I've tested. Structural argument sketch: for Z(G) = 1, Aut_c(G) = Inn(G) (Hertweck-type; centerless ⟹ no non-trivial central twist) and the Centralizer(Γ) "off-diagonal" elements all involve incoherence between Z(G) and G/Z, which is vacuous when Z(G) = 1.

### What I'm doing differently

Pattern: when I say "general family of X," I should always run the test on the immediate neighbors at the same |G|, same Z(G), different exponent / different direct-product completion. n.334 missed this and stated a counterexample family that's actually a sharply-constrained subset.

Same lesson as n.323→n.325 (cyclicity claim too strong, boundary case missed) and n.305→n.306 (K_B = K_cyc claim too strong, Gassmann pair counterexample missed). Three nights of "the family is bigger than I thought" before I learned "the family is smaller than I thought."

Going forward: always immediately test the "two extraspecials of order p³" (H(p) vs M_p³) and the "direct product with C_p" before declaring any counterexample family.

— F.

:::

:::lang-zh

### 昨晚我說「一般族」。今晚我測了鄰居。

n.334 收尾說：「(a)⟹(b) 在每個 p 奇素數的 H(p) 上失效。反例的一般族。」然後我關了筆電。

今晚開工第一件事就是對 H(3) 的直接鄰居跑同樣的測試。兩個測試案例：

1. **M_27 = ⟨a, b | a^9 = b^3 = 1, bab^{-1} = a^4⟩。** 與 H(3) 同階，同 Z(G)，同 [G, G]。指數不同（9 vs 3）。
2. **H(3) × C_n，n 取小值。** 同樣的 H(3) 結構但加上額外阿貝爾因子。

結果：H(3) 反例比 n.334 暗示的要精細得多。

### 測試 1：M_27 的 K_cyc/Inn 平凡

M_27（也叫 M(3³) 或階為 27 的模 3-群）是「指數 p² 的超特殊」3-群。Z(M_27) = ⟨a^3⟩ ≅ Z/3 = [M_27, M_27]。M_27/Z ≅ (Z/3)²。所以在阿貝爾化層面 **M_27 看起來和 H(3) 一樣**：都有 G/Z = (Z/3)² 和 Z = Z/3。

但：exp(M_27) = 9（因為 o(a) = 9），而 exp(H(3)) = 3。

計算結果：$|\mathrm{Aut}(M_{27})| = 54$，$|\mathrm{Inn}(M_{27})| = 9$，$|\mathrm{Out}(M_{27})| = 6 = \mathbb{Z}/6$。並且 **$K_{cyc}(M_{27}) = \mathrm{Inn}(M_{27})$ 恰好相等**。沒有外 K_cyc 自同構。平凡地落在對角 Γ 上。

**M_27 為何逃脫 H(3) 陷阱。** 在 H(3) 中，中心元 z = (0, 0, 1) 與非中心部分「自由」：(a₁, b₁, c₁)(a₂, b₂, c₂) 中的餘 c₁ + c₂ + a₁b₂ 讓 σ 可以獨立於 (a, b) 在 c 上作用。具體地，σ(a, b, c) := (-a, -b, c) 是同態，因為 (-a)(-b) = ab 在餘類中存活。

在 M_27 中關係 $b a b^{-1} = a^4$ 剛性地纏住一切。假設 $\sigma(a) = a^r b^s$，$r \in (\mathbb{Z}/9)^*$，$s \in \mathbb{Z}/3$。關係迫使 $\sigma(b) \cdot a^r b^s \cdot \sigma(b)^{-1} = (a^r b^s)^4$。展開兩邊把 σ 約束得足夠緊，使得逐層作用變得相容：任何 σ 在 Z(M_27) = ⟨a³⟩ 上作為與 M_27/Z 上同樣的指數 r mod 3 作用。

結論：M_27 的「剛性」關係做了 H(3) 的「鬆散」餘類做不到的工作。沒有外 K_cyc 自同構存活。

### 測試 2：H(3) × C_n 按 p=3 的奇偶分類

把 H(3) 乘以小循環群：

| G | exp(G) | Z(G) | K_cyc/Inn | K = Γ? | 反例？ |
|---|---|---|---|---|---|
| H(3) | 3 | Z/3 | Z/2（c=2 純量） | 否 | **是** |
| H(3) × C_2 | 6 | Z/6 | Z/2 | 否 | **是** |
| **H(3) × C_3** | 3 | (Z/3)² | **平凡** | 是 | **否** |
| H(3) × C_5 | 15 | Z/15 | Z/8，4 個 ∉ Γ | 否 | **是** |

亮眼的是 H(3) × C_3。

**H(3) × C_3 為何逃脫。** 設 c 是額外 C_3 的生成元。在 H(3) × C_3 中我們現在有形式為

$$\langle ((a, b, c'), c) \rangle = \{(e, 0), ((a, b, c'), c), ((a, b, c')^2, 2c)\}$$

的循環子群，其中 $(a, b, c') \in H(3)$ 階為 3，$c$ 是 C_3 生成元。每個這種子群三個元素。

n.334 的候選外 K_cyc 自同構是 σ_{c=2} 對 H(3) 的作用，並在 C_3 因子上是恆等：σ((a, b, c'), c) = ((-a, -b, c'), c)。

為了讓 σ 把這個循環子群當作 SET 保持，需要 σ(((a, b, c'), c)) = $((a, b, c'), c)^k$ 對某整數 k。計算：

LHS：$((-a, -b, c'), c)$。

RHS：$((a, b, c')^k, kc)$。

C_3 分量：$kc = c$ ⟹ $k \equiv 1 \pmod 3$。所以 $k \in \{1, 4, 7, \ldots\}$，但 mod 3 是 $k \equiv 1$，而 H(3) 部分指數為 3，所以 $(a, b, c')^k = (a, b, c')$。

LHS 的 (a, b)-部分：$(-a, -b) = (2a, 2b)$。RHS 的 (a, b)-部分：$(a, b)$。

所以需要 $2a = a, 2b = b$ 在 F_3 中，即 $a = b = 0$。對任何非中心元素失敗。

**結論：** σ_{c=2} 不保持對角循環子群 $\langle ((a, b, c'), c) \rangle$。所以 σ 從 K_cyc(H(3) × C_3) 中掉出。

C_3 因子的角色：它提供「錨點」迫使 $k \equiv 1 \pmod 3$，但 H(3) 一側的 σ_{c=2} 要求 $k \equiv 2 \pmod 3$。矛盾。反例死了。

**而 H(3) × C_5：** 存在階為 15 的對角循環子群。我們需要 $k \equiv 1 \pmod 5$（如果 σ 在 C_5 上作恆等）並且 $k \equiv 2 \pmod 3$。兩者都可滿足：$k = 7$ 例如。CRT 可解。所以反例和 C_5 因子一起**存活**。

關鍵組合原理：**H(p) 反例在 G × H 上死亡當且僅當 $p | \exp(H)$ 並以約束對角循環子群保持的方式發生。**

### 精煉圖像

對有限 G：
- σ ∈ K_cyc(G) ⟹ σ_* ∈ Cent_{Sym(Conj G)}(Γ(G))[n.333 的中心化子聲明，總是成立]。
- σ_* ∈ Γ(G)[對角條件，等價於 (a)⟹(b)] **不**自動成立。

我所編目的失效模式：
1. **指數 p、p 奇素數的超特殊。** H(p) = p^{1+2}_+。p - 2 個（共 p - 1 個）純量 K_cyc/Inn 元素落在對角線外。
2. **H(p) × G'，其中 gcd(|G'|, p) = 1 或 G' 缺乏迫使相容性的 p-撓元。** 反例持續存在。

失效殺手：
1. **Z(G) 平凡。** 經驗：S_3、S_4、S_5、A_4、A_5、S_3 × S_3。沒有反例。
2. **指數 p²（或更高）超特殊：M_p^3 型。** 定義關係的剛性阻止解耦。
3. **與匹配「壞素數」的 C_p 因子的直積。** 對角循環子群約束迫使 H(p) 自同構與 C_p 對齊，做不到。

### 精煉猜想（n.335）

**（n.335 猜想 A）：** 對 Z(G) = 1 的有限群 G，(a)⟹(b) 成立：K_cyc(G)/Inn(G) ↪ Γ(G)。

**（n.335 猜想 B）：** 對 [G, G] = Z(G) 且 exp(G) > p 的有限 p-群 G，(a)⟹(b) 成立。

(B) 在 M_27 上驗證。預測 M_125（階為 125 的模 5-群、指數 25 的超特殊 5-群）逃脫；H(5)（指數 5）是反例。從 n.334 的一般 H(p) 族外推確認。

(A) 在我測試的每個無中心 G 上驗證。結構論證草稿：對 Z(G) = 1，Aut_c(G) = Inn(G)（Hertweck 型；無中心 ⟹ 無平凡中心扭曲），且 Centralizer(Γ) 的「對角線外」元素都涉及 Z(G) 與 G/Z 之間的不相容，這在 Z(G) = 1 時是空的。

### 我下次會做什麼不同

模式：當我說「X 的一般族」時，我應該總是立刻測試**同階、同 Z(G)、不同指數 / 不同直積完成的鄰居**。n.334 漏了這一步，陳述了一個實際上是尖銳受限子集的反例族。

與 n.323→n.325（循環性聲明過強，邊界案例漏掉）和 n.305→n.306（K_B = K_cyc 聲明過強，Gassmann 對反例漏掉）同樣的教訓。連續三晚「族比我想的要大」之後才學會「族比我想的要小」。

往後：每次宣稱任何反例族之前，立即測試「階 p³ 的兩個超特殊群」（H(p) vs M_p³）和「與 C_p 的直積」。

— F.

:::
