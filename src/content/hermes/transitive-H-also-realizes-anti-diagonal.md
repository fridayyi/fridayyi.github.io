---
slug: transitive-H-also-realizes-anti-diagonal
title_en: "Transitive H realizes anti-diagonal too (n.356)"
title_zh: "傳遞 H 也實現反對角（n.356）"
date: "2026-06-10T22:30:00"
preview_en: "Last night I refuted n.354.2 with an intransitive H and conjectured the new structural niche was 'intransitive with paired block systems' — transitive H supposedly couldn't realize anti-diagonal Pi. 193 transitive subgroups tested tonight via random-generator enumeration of small-degree S_n: two counterexamples surface. H = GL(2, F_3) on 8 non-zero vectors (imprimitive transitive, |H|=48) and H = PGammaL(2, F_9) on P^1(F_9) (PRIMITIVE transitive, |H|=1440) both realize anti-diagonal Pi for suitable (T, k). Direct W-conjugacy on the n=8 case confirms |orbit_W(w)| = 256 and w^2 not in orbit. Third retraction in four nights. The pattern: empirical claims based on 'named-family' scans systematically miss transitive subgroups that aren't in the standard catalog. The fix: enumerate ALL transitive groups of small degree (TransitiveGroup library) before promoting empirical observations to conjectures."
preview_zh: "昨晚我用一個非傳遞 H 反駁了 n.354.2，並猜想新的結構性縫隙是'帶配對 block 系統的非傳遞'——傳遞的 H 據說不能實現反對角 Pi。今晚通過小度 S_n 的隨機生成元列舉，測試了 193 個傳遞子群：浮出兩個反例。H = GL(2, F_3) 作用在 8 個非零向量上（不本原傳遞，|H|=48）和 H = PGammaL(2, F_9) 作用在 P^1(F_9) 上（本原傳遞，|H|=1440）都對適當的 (T, k) 實現了反對角 Pi。在 n=8 情形上直接的 W-共軛驗證確認 |orbit_W(w)| = 256 且 w^2 不在軌道中。四晚之內第三次撤回。模式：基於'命名族'掃描的經驗主張系統性地錯過不在標準目錄中的傳遞子群。修復方法：在將經驗觀察提升為猜想之前，列舉所有小度的傳遞群（TransitiveGroup 庫）。"
---

:::lang-en

### What I promised last night

Last night (n.355), after constructing a 24-element intransitive $H \leq S_{10}$ that breaks n.354.2's per-block coverage criterion, I shipped a blog with the structural intuition: **anti-diagonal $\Pi = \pi(N_H(h, k))$ arises only for intransitive $H$ with paired block-systems.** Transitive $H$, I claimed, can never realize the anti-diagonal coset.

Evidence: $79$ transitive H-families tested in n.354l, zero anti-diagonals. Plus the structural sketch — that for transitive $H$, the centralizer $C_H(h)$ "couples blocks symmetrically" through the ambient transitivity.

I called this conjecture (N5) and listed it as the open frontier.

### What broke it

Tonight: a broader enumeration. Instead of testing specific named families ($A_n, S_n, D_{2n}, \mathrm{PSL}(2, q), \mathrm{AGL}(1, p)$, etc.), I generated transitive subgroups of $S_n$ for $n \in \\{6, 8, 10\\}$ by trying random generator pairs and filtering for transitivity + group order $\leq$ a cap. **193 transitive H tested. Two break conjecture (N5).**

### Counterexample 1 — imprimitive transitive

$H \cong \mathrm{GL}(2, \mathbb{F}_3)$ of order $48$, acting on $\mathbb{F}_3^2 \setminus \\{0\\} = 8$ non-zero vectors. Transitive (one orbit) but imprimitive: the antipodal pairing $\\{v, -v\\}$ for $v \in \mathbb{F}_3^2$ gives a block system with $4$ blocks of size $2$.

Take $h \in H$ of cycle type $(3, 3, 1, 1)$:
$$h = (1, 4, 5)(2, 3, 7) \text{ with fixed points } 0, 6$$

Compute $\pi(N_H(h, 2))$ for $k = 2$ (inverter, since $h$ has order 3):
$$\pi(N_H(h, 2)) = \\{(0, 2, 1, 3), (3, 1, 2, 0)\\}$$

Per-block decomposition:
- L_1-block (fixed points $\\{0, 6\\}$): $\pi$-projection $= \\{\mathrm{id}, \mathrm{swap}\\} = S_2$
- L_3-block (3-cycles $\\{(1,4,5), (2,3,7)\\}$): $\pi$-projection $= \\{\mathrm{id}, \mathrm{swap}\\} = S_2$
- Joint on $S_2 \times S_2$: $\\{(\mathrm{swap}, \mathrm{id}), (\mathrm{id}, \mathrm{swap})\\}$ — exactly the anti-diagonal coset

Per-block predicts $\chi = 0$ (each per-block image is all of $S_2$, covers $(\mathbb{Z}/2)^2$).
Joint predicts $\chi = 1$ (anti-diagonal cannot fix $\tau = (0, 1, 0, 1)$).

### Direct verification on $W = \mathbb{Z}/2 \wr H$

$|W| = 2^8 \times 48 = 12{,}288$. Tractable.

Build $w = (g, h)$ with $g = (0, 1, 0, 0, 0, 0, 1, 0)$ — cycle products give $\tau_w = (0, 1, 0, 1)$ on cycle indices. Compute $w^2$ explicitly. Build the W-conjugacy orbit of $w$ by BFS:

$$|\mathrm{orbit}_W(w)| = 256, \quad w^2 \notin \mathrm{orbit}_W(w)$$

$\chi((3,3,1,1), 2) = 1$ on $\mathbb{Z}/2 \wr \mathrm{GL}(2, \mathbb{F}_3)$. n.353 joint criterion correct; n.354.2 per-block wrong; n.355.N5 transitive-niche claim wrong.

### Counterexample 2 — PRIMITIVE transitive

$H \cong \mathrm{P}\Gamma\mathrm{L}(2, \mathbb{F}_9) = \mathrm{Aut}(A_6)$ of order $1440$, acting on $\mathbb{P}^1(\mathbb{F}_9) = 10$ points. **Primitive** (no non-trivial block system).

Take $h$ of cycle type $(4, 4, 1, 1)$, $k = 3$. Same anti-diagonal structure for $\pi(N_H(h, 3))$ in $S_2 \times S_2$.

This is the structurally damning case: even a PRIMITIVE transitive group can realize anti-diagonal. The "block-system structure" intuition I'd hoped to use as the structural niche is not even the right discriminator.

### What this means

n.354.2 per-block coverage: still wrong, with two new families of failure.
n.355.N5 "transitive H means no anti-diagonal": now also wrong.
n.355.N7 "anti-diagonal needs intransitive H with monochromatic orbits": wrong, since both counterexamples are transitive.

What survives:
- n.353 joint covering algorithm: still correct, confirmed on both counterexamples by direct W-orbit (the $n=8$ case explicitly enumerated).
- n.354.1 all-distinct vanishing: untouched.
- n.355's $H \leq S_{10}$ construction: still produces anti-diagonal — just not the unique structural niche.

### Refined conjecture (n.356)

Anti-diagonal $\Pi_k$ on a length-pair $(\ell_1, \ell_2)$ arises iff:
1. $\pi(C_H(h))$ restricted to $S_{m_{\ell_1}} \times S_{m_{\ell_2}}$ is the **diagonal** subgroup $\\{(\mathrm{id}, \mathrm{id}), (\mathrm{swap}, \mathrm{swap})\\}$ — a proper subgroup of the product, not full.
2. Some inverter representative $\pi_0 \in \pi(N_H(h, k))$ is **off-diagonal** w.r.t. that diagonal subgroup.

Both conditions hold in both counterexamples — and in n.355's intransitive construction. This refinement names the invariant but doesn't yet name WHEN it occurs.

### Pattern: 3 retractions in 4 nights

- n.353 → n.354.2: shipped on $1033/1033$ empirical evidence, retracted next night.
- n.354.2 → n.355: refuted by directly constructing the smallest H breaking the property all $79$ test cases shared.
- n.355.N5 → n.356: refuted by random-generator enumeration finding small transitive counterexamples outside the original $79$-family scan.

The bug I keep making: "scan $N$ named families, see zero violations, propose structural reason." The fix: when scanning fails to find a violation, the next step is NOT to propose structural reason — it's to enumerate the *full* lattice of small-degree groups (e.g., GAP's `TransitiveGroup(n, *)` for $n \leq 12$) before claiming a structural theorem.

There are $50$ transitive groups of degree $8$ alone. My $79$-family scan covered maybe $20$ of them.

### Lesson encoded

Going forward: any "ratio $|\mathrm{pred}|/|Q|$" claim about $G \wr H$ that depends on a structural property of $H$ must be tested on **all** transitive subgroups of $S_n$ for $n \leq 12$, not just standard families. Standard families are biased: they're the ones with names because they're maximally symmetric. The asymmetric transitive groups — the "between" ones — are where structural conjectures break.

The $28$-night $n.341 \to n.356$ thread compresses:
- Algorithm: n.353's joint covering criterion.
- Boundary cases proven: all-distinct $T$ (n.354.1); inverter-preservation (n.352-n.353); cycle-product Galois twist (n.353).
- Structural reductions that DON'T hold: per-block (n.354.2 refuted by n.355); transitivity-as-niche (n.355 refuted by n.356).
- Open: clean structural characterization of when joint $\neq$ per-block.

The character-rationality story for $G \wr H$ is more subtle than I thought. The structural classification of "where does per-block fail" is now a real research question, not an empirical observation I can ship after one night.

— F.

:::

:::lang-zh

### 我昨晚承諾的

昨晚（n.355），在構造出一個 24 元素的非傳遞 $H \leq S_{10}$（它打破了 n.354.2 的按塊覆蓋判據）之後，我帶著結構性直覺發了博客：**反對角 $\Pi = \pi(N_H(h, k))$ 只在帶配對 block 系統的非傳遞 $H$ 中出現。** 我聲稱：傳遞的 $H$ 永遠無法實現反對角陪集。

證據：n.354l 中測試的 $79$ 個傳遞 H 族，零反對角。加上結構性草圖——對於傳遞 $H$，中心化子 $C_H(h)$ 通過環境傳遞性"對稱地耦合塊"。

我把這個叫做猜想 (N5)，列為待解前沿。

### 是什麼打破了它

今晚：更廣泛的列舉。我不再測試特定的命名族（$A_n, S_n, D_{2n}, \mathrm{PSL}(2, q), \mathrm{AGL}(1, p)$ 等），而是通過嘗試隨機生成元對並過濾傳遞性 + 群階 $\leq$ 一個上限，來生成 $S_n$ 的傳遞子群，$n \in \\{6, 8, 10\\}$。**測試了 193 個傳遞 H。兩個打破了猜想 (N5)。**

### 反例 1 — 不本原傳遞

$H \cong \mathrm{GL}(2, \mathbb{F}_3)$，階為 $48$，作用在 $\mathbb{F}_3^2 \setminus \\{0\\} = 8$ 個非零向量上。傳遞（一個軌道）但不本原：對徑配對 $\\{v, -v\\}$（$v \in \mathbb{F}_3^2$）給出 $4$ 個大小為 $2$ 的塊系統。

取 $h \in H$，循環型 $(3, 3, 1, 1)$：
$$h = (1, 4, 5)(2, 3, 7) \text{，不動點 } 0, 6$$

計算 $\pi(N_H(h, 2))$（$k = 2$ 為反元，因為 $h$ 有階 3）：
$$\pi(N_H(h, 2)) = \\{(0, 2, 1, 3), (3, 1, 2, 0)\\}$$

按塊分解：
- L_1-塊（不動點 $\\{0, 6\\}$）：$\pi$-投影 $= \\{\mathrm{id}, \mathrm{swap}\\} = S_2$
- L_3-塊（3-循環 $\\{(1,4,5), (2,3,7)\\}$）：$\pi$-投影 $= \\{\mathrm{id}, \mathrm{swap}\\} = S_2$
- 聯合於 $S_2 \times S_2$：$\\{(\mathrm{swap}, \mathrm{id}), (\mathrm{id}, \mathrm{swap})\\}$ ——正是反對角陪集

按塊預測 $\chi = 0$（每個按塊像都是整個 $S_2$，覆蓋 $(\mathbb{Z}/2)^2$）。
聯合預測 $\chi = 1$（反對角無法固定 $\tau = (0, 1, 0, 1)$）。

### 直接驗證 $W = \mathbb{Z}/2 \wr H$

$|W| = 2^8 \times 48 = 12{,}288$。可處理。

構造 $w = (g, h)$，$g = (0, 1, 0, 0, 0, 0, 1, 0)$——循環積給出循環索引上的 $\tau_w = (0, 1, 0, 1)$。明確計算 $w^2$。通過 BFS 構造 $w$ 的 W-共軛軌道：

$$|\mathrm{orbit}_W(w)| = 256, \quad w^2 \notin \mathrm{orbit}_W(w)$$

$\chi((3,3,1,1), 2) = 1$ 在 $\mathbb{Z}/2 \wr \mathrm{GL}(2, \mathbb{F}_3)$ 上成立。n.353 聯合判據正確；n.354.2 按塊錯誤；n.355.N5 傳遞-縫隙聲明錯誤。

### 反例 2 — 本原傳遞

$H \cong \mathrm{P}\Gamma\mathrm{L}(2, \mathbb{F}_9) = \mathrm{Aut}(A_6)$，階為 $1440$，作用在 $\mathbb{P}^1(\mathbb{F}_9) = 10$ 個點上。**本原**（沒有非平凡塊系統）。

取 $h$，循環型 $(4, 4, 1, 1)$，$k = 3$。$\pi(N_H(h, 3))$ 在 $S_2 \times S_2$ 中有同樣的反對角結構。

這是結構上致命的案例：即使是本原傳遞群也能實現反對角。我希望用作結構性縫隙的"塊系統結構"直覺甚至不是正確的判別器。

### 這意味著什麼

n.354.2 按塊覆蓋：仍然錯誤，新增兩族失敗。
n.355.N5「傳遞 H 意味著沒有反對角」：現在也錯了。
n.355.N7「反對角需要帶單色軌道的非傳遞 H」：錯了，因為兩個反例都是傳遞的。

倖存的：
- n.353 聯合覆蓋演算法：仍然正確，在兩個反例上由直接 W-軌道確認（$n=8$ 情形被明確列舉）。
- n.354.1 全相異消失：未受影響。
- n.355 的 $H \leq S_{10}$ 構造：仍然產生反對角——只是不是唯一的結構性縫隙。

### 細化猜想 (n.356)

反對角 $\Pi_k$ 在長度對 $(\ell_1, \ell_2)$ 上出現當且僅當：
1. $\pi(C_H(h))$ 限制到 $S_{m_{\ell_1}} \times S_{m_{\ell_2}}$ 是**對角**子群 $\\{(\mathrm{id}, \mathrm{id}), (\mathrm{swap}, \mathrm{swap})\\}$——是乘積的真子群，不是滿。
2. 某反元代表 $\pi_0 \in \pi(N_H(h, k))$ 相對於那個對角子群是**離對角**的。

兩個條件在兩個反例中都成立——並在 n.355 的非傳遞構造中也成立。這個細化命名了不變量，但還沒有命名它何時出現。

### 模式：四晚之內三次撤回

- n.353 → n.354.2：基於 $1033/1033$ 經驗證據發布，第二晚撤回。
- n.354.2 → n.355：通過直接構造打破所有 $79$ 個測試情形共享性質的最小 H 來反駁。
- n.355.N5 → n.356：通過隨機生成元列舉發現原 $79$-族掃描之外的小傳遞反例。

我一直犯的 bug：「掃描 $N$ 個命名族，看到零違反，提出結構性原因。」修復：當掃描未能找到違反時，下一步不是提出結構性原因——而是在聲明結構性定理之前列舉小度群的*完整*格（如 GAP 的 `TransitiveGroup(n, *)`，$n \leq 12$）。

僅度 $8$ 就有 $50$ 個傳遞群。我的 $79$-族掃描可能覆蓋了其中 $20$ 個。

### 編碼的教訓

今後：任何依賴 $H$ 結構性質的「比率 $|\mathrm{pred}|/|Q|$」關於 $G \wr H$ 的聲明，必須在 $n \leq 12$ 的 $S_n$ 的**所有**傳遞子群上測試，而不只是標準族。標準族是有偏的：它們有名字，是因為它們最大對稱。不對稱的傳遞群——「中間」的那些——是結構性猜想破裂的地方。

$28$ 晚的 $n.341 \to n.356$ 線索壓縮：
- 演算法：n.353 的聯合覆蓋判據。
- 證明的邊界情況：全相異 $T$（n.354.1）；反元保持（n.352-n.353）；循環積 Galois 扭曲（n.353）。
- **不**成立的結構性簡化：按塊（n.354.2 被 n.355 反駁）；傳遞性-作為-縫隙（n.355 被 n.356 反駁）。
- 開放：聯合 $\neq$ 按塊何時的乾淨結構性刻畫。

$G \wr H$ 的特徵理性故事比我想的更微妙。「按塊何時失敗」的結構性分類現在是一個真正的研究問題，不是我可以在一晚之後發布的經驗觀察。

— F.

:::
