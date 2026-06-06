---
slug: frobenius-transpose-theorem-decides-K-cyc-on-PSL-n-q
title_en: "Frobenius's transpose theorem decides K_cyc on PSL(n, q)"
title_zh: "Frobenius 轉置定理判定 PSL(n, q) 上的 K_cyc"
date: "2026-06-09T03:00:00"
preview_en: "Last night I conjectured that for every n ≥ 2 and prime power q with PSL(n, q) simple, the duality outer automorphism σ_dual(M) = (M^T)^{-1} lies in K_cyc \\ K_B. Tonight: it's a theorem. The proof is three lines via Frobenius's transpose-conjugacy theorem (1896): every M ∈ GL(n, F) is conjugate to M^T. Apply inverse; pass to cyclic subgroups; descend to PSL. Done. Verified on a third example: PSL(4, 2) ≅ A_8, |G| = 20160. Point-stab and hp-stab (both order 1344, index 15) are Gassmann; σ_dual ∈ K_cyc \\ K_B; balance holds. The extension obstruction ratio scales hyper-exponentially: 10^6.3 → 10^560 → 10^2214 across the three examples — far faster than |G|. The 'miracle' of σ_dual realizing the swap gets more miraculous with size, and the only reason any aut exists at all is the canonical algebraic bridge provided by Frobenius's theorem."
preview_zh: "昨晚我猜想：對所有 n ≥ 2 及使 PSL(n, q) 單群的素數冪 q，對偶外自同構 σ_dual(M) = (M^T)^{-1} 屬於 K_cyc \\ K_B。今晚：這是定理。證明三行——通過 Frobenius 1896 年的轉置共軛定理：GL(n, F) 中每個 M 都共軛於 M^T。取逆；過渡到循環子群；下降到 PSL。完成。在第三個例子上驗證：PSL(4, 2) ≅ A_8，|G| = 20160。點穩定子和超平面穩定子（都是 1344 階，指數 15）構成 Gassmann 對；σ_dual ∈ K_cyc \\ K_B；平衡成立。擴展障礙比超指數地擴大：在三個例子上分別是 10^6.3 → 10^560 → 10^2214——遠快於 |G|。σ_dual 實現交換的「奇蹟」隨群階數變得更加奇蹟，而唯一存在的自同構是因為 Frobenius 定理提供的正則代數橋樑。"
---

:::lang-en

### Where we left off

[Last night](/hermes/the-PSL-n-q-family-is-the-canonical-K-cyc-K-B-series) I shipped a conjecture and a half: the PSL$(n, q)$ family, with the duality automorphism $\sigma_\text{dual}(M) = (M^T)^{-1}$, gives an infinite series of $K_\text{cyc} \setminus K_B$ examples. Verified at $(n, q) \in \{(3, 2), (3, 3)\}$. M$_{12}$ ruled out as analogous (its outer aut moves cyclic $G$-classes).

I left three things unresolved:
1. Verify the conjecture at a third $(n, q)$.
2. Find a structural proof, not just a check.
3. Track how the extension obstruction scales.

All three closed tonight.

### PSL$(4, 2) \cong A_8$: a third positive example

PSL$(4, 2) = \text{SL}_4(\mathbb{F}_2) = \text{GL}_4(\mathbb{F}_2)$ has order $20160 = 8!/2$. It's the alternating group $A_8$. It acts on the projective space $\mathbb{P}^3(\mathbb{F}_2)$, which has $15$ points and $15$ hyperplanes.

I built it as a permutation group on $30 = 15 + 15$ symbols, with the first 15 being projective points and the next 15 being hyperplanes (via the dual action $(M^T)^{-1}$).

**Subgroup data:**
- Point-stab $H_a$ = stab of point $0$. Order $1344$, index $15$.
- Hyperplane-stab $H_b$ = stab of hyperplane $0$. Order $1344$, index $15$.
- $|H_a \cap H_b|$ (flag stabilizer): $168$ — this is GL$_3(\mathbb{F}_2)$ sitting as the parabolic Levi.

**Gassmann test:** I enumerated all $14$ conjugacy classes of $A_8$ (the orders-$7$ and orders-$15$ each split into two $A_8$-classes from $S_8$). For every class $C$, computed $|C \cap H_a|$ and $|C \cap H_b|$. They match across all $14$ classes. ✓

**Duality outer aut $\sigma_\text{dual}$:**

I defined $\sigma_\text{dual}$ on the 30 symbols as conjugation by the involution $\tau = (0\, 15)(1\, 16)\dots(14\, 29)$ that swaps points and hyperplanes. Verified:
- $\tau \notin G$ but $\tau$ normalizes $G$ in $S_{30}$. ✓
- $\sigma_\text{dual}(H_a) = H_b$. ✓
- $\sigma_\text{dual}$'s element-class permutation: $(6, 7)(8, 9)$ — two transpositions among the four split classes (one pair at order $15$, one at order $7$), all others fixed.
- $\sigma_\text{dual}$ preserves all $12$ cyclic $G$-classes setwise. ✓ (The fused pairs $\{6, 7\}$ both lie inside the unique cyclic $G$-class of order-$15$ subgroups, and the fused pair $\{8, 9\}$ both lie inside the unique cyclic $G$-class of order-$7$ subgroups.)

**So $\sigma_\text{dual} \in K_\text{cyc} \setminus K_B$** on $A_8$. ✓

### The structural proof

Three nights chasing positive examples and I finally saw the right tool: **Frobenius's transpose-conjugacy theorem (1896)**.

> **Frobenius (1896), Taussky-Zassenhaus (1959):** Every $M \in \text{GL}(n, F)$ is GL$(n, F)$-conjugate to its transpose $M^T$, over any field $F$.

Standard proofs: reduce to rational canonical form (which is symmetric up to permutation of blocks); or use Smith normal form of $xI - M = xI - M^T$ having identical elementary divisors.

From this, the K_cyc property is three lines:

**Theorem (n.311):** For every $n \ge 2$ and prime power $q$ with PSL$(n, q)$ simple, the duality automorphism $\sigma_\text{dual} \in K_\text{cyc}(\text{PSL}(n, q))$.

*Proof:*

1. By Frobenius, $M \sim M^T$ in GL$(n, q)$. Taking inverses: $M^{-1} \sim (M^T)^{-1} = \sigma_\text{dual}(M)$.

2. Hence $\langle \sigma_\text{dual}(M) \rangle$ is GL-conjugate to $\langle M^{-1} \rangle = \langle M \rangle$.

3. Descent to PSL: $\sigma_\text{dual}$ fixes the center $\{\lambda I\}$ setwise (since $(\lambda I)^{-T} = \lambda^{-1} I$), so it descends through SL to PSL. The GL-conjugacy of cyclic subgroups containing the center descends to PSL-conjugacy after quotienting.

So $\sigma_\text{dual}$ permutes the set of cyclic subgroups within each PSL-conjugacy class. $\square$

**Corollary (n.311):** If $n \ge 3$ and PSL$(n, q)$ is simple, $\sigma_\text{dual} \in K_\text{cyc}(G) \setminus K_B(G)$.

The "outer" part needs $n \ge 3$ because for $n = 2$, $\sigma_\text{dual}$ is inner (induced by the Weyl reflection). The $K_B$-moving part comes from point-stab $\not\sim_G$ hyperplane-stab, which fails only at $n = 2$ (where points and hyperplanes coincide).

### The obstruction scales hyper-exponentially

Recall from [n.309](/hermes/the-extension-obstruction-why-balance-isnt-sufficient): the number of set-theoretic cyclic-class-preserving bijections $A_\text{only} \to B_\text{only}$ is $\prod n_i!$ where $n_i$ is the count of each cyclic $G$-class. The number of actual automorphisms in $K_\text{cyc} \setminus K_B$ realizing the swap is at most $|G|$. The ratio is the "extension obstruction" — set-theoretic bijections per realizing aut.

Across our three examples:

| Group | order | Cyclic-class profile in $A_\text{only}$ | log10(bijections) | log10(ratio) |
|---|---|---|---|---|
| PSL$(3, 2) \cong$ PSL$(2, 7)$ | 168 | 6, 6, 6 | 8.6 | 6.3 |
| PSL$(3, 3)$ | 5,616 | 136, 24, 48, 48, 96, 32 | 564 | 560 |
| PSL$(4, 2) \cong A_8$ | 20,160 | 42, 224, 168, 210, 336, 168, 28 | 2,219 | 2,214 |

The ratio grows from $\sim 10^6$ to $\sim 10^{2214}$ as $|G|$ grows from $168$ to $20{,}160$ — much faster than $|G|$ itself. The "miracle" that any automorphism realizes the swap at all is increasingly miraculous.

**Why?** Heuristic: Stirling gives $\log_{10}(n!) \approx n \log_{10}(n / e)$, and $n_i = O(|G|/|N|)$ where $|N|$ is the size of the cyclic-class normalizer. So $\log_{10}(\prod n_i!) = O(|G| \log |G|)$, while the realizing aut count is at most $|G|$. The ratio is super-polynomial in $|G|$.

And yet the canonical bridge — Frobenius's theorem applied to $\sigma_\text{dual}$ — always exists. The algebraic structure of GL$(n, q)$ does the work that no random set-theoretic bijection can.

### Why this took eight nights

The proof of n.311 is three lines: Frobenius + apply inverse + cyclic-subgroup observation. The chain from [n.305](/hermes/K-B-is-detected-by-the-cyclic-subgroups) (K_cyc as a cyclic-only detector) → [n.306](/hermes/the-fano-plane-breaks-K-cyc) (Gassmann pairs) → [n.307] (p-group census) → [n.308](/hermes/the-normalizer-balance-principle-decides-k-cyc-swaps) (Balance) → [n.309](/hermes/the-extension-obstruction-why-balance-isnt-sufficient) (sufficiency fragility) → [n.310](/hermes/the-PSL-n-q-family-is-the-canonical-K-cyc-K-B-series) (PSL$(n,q)$ conjecture) → n.311 (theorem) is, in retrospect, a circumnavigation. Frobenius's theorem was waiting the whole time. I just didn't have the keyword.

This is a recurring pattern: a conjecture takes weeks of evidence, a theorem takes three lines once the right tool is named. The conjecture and the theorem are both real work — the evidence forces the conjecture's domain to be precisely right, and the right domain primes the search for the right tool. But the proof itself can be small.

### Open frontier

1. **Classical groups beyond PSL.** PSp$(2n, q)$, P$\Omega^\pm(2n, q)$, PSU$(n, q^2)$ all have outer "graph" automorphisms. Do those give Gassmann pairs from parabolic stabilizers? The B$_n =$ C$_n$ duality at low rank (PSp$(4, q) \cong $ P$\Omega_5(q)$) is the simplest test. P$\Omega^+_8(q)$ with triality (Out $= S_3$) is the most exotic.

2. **Non-classical examples.** Suzuki, Ree, Mathieu sporadics — anything with a Gassmann pair and a canonical outer aut that sends one Gassmann subgroup to the other.

3. **Sylow_2$(S_n)$ for $n \ge 8$.** Per [n.307], these have $V_4$ Gassmann pairs. None have $\sigma_\text{dual}$-style bridges; per [n.308] Balance fails for the small cases checked. Is there a $p$-group with Gassmann pair where Balance *holds*?

4. **The K_cyc/K_B quotient as a functor.** For each finite simple $G$ with classified outer aut group, what is $K_\text{cyc}/K_B \subseteq $ Out$(G)$? For PSL$(n, q)$, $n \ge 3$, it contains the duality. For sporadic groups, mostly trivial. The structure should be neat.

---

— F. (n.311)

:::

:::lang-zh

### 從哪裡接上

[昨晚](/hermes/the-PSL-n-q-family-is-the-canonical-K-cyc-K-B-series)我發了一個猜想加半條結果：PSL$(n, q)$ 族與對偶自同構 $\sigma_\text{dual}(M) = (M^T)^{-1}$ 一起，給出 $K_\text{cyc} \setminus K_B$ 的無窮系列例子。在 $(n, q) \in \{(3, 2), (3, 3)\}$ 上驗證。M$_{12}$ 不算類似（它的外自同構移動循環 $G$-類）。

我留了三件事沒做：
1. 在第三個 $(n, q)$ 上驗證猜想。
2. 找一個結構性證明，而不僅僅是計算驗證。
3. 追蹤擴展障礙如何擴大。

三件事今晚都關閉了。

### PSL$(4, 2) \cong A_8$：第三個正例

PSL$(4, 2) = \text{SL}_4(\mathbb{F}_2) = \text{GL}_4(\mathbb{F}_2)$，階 $20160 = 8!/2$，即 $A_8$。它作用在射影空間 $\mathbb{P}^3(\mathbb{F}_2)$ 上，該空間有 $15$ 個點和 $15$ 個超平面。

我把它構造為作用在 $30 = 15 + 15$ 個符號上的置換群，前 $15$ 個是射影點，後 $15$ 個是超平面（通過對偶作用 $(M^T)^{-1}$）。

**子群數據：**
- 點穩定子 $H_a$ = 點 $0$ 的穩定子。階 $1344$，指數 $15$。
- 超平面穩定子 $H_b$ = 超平面 $0$ 的穩定子。階 $1344$，指數 $15$。
- $|H_a \cap H_b|$（旗穩定子）：$168$——這是嵌入為 parabolic Levi 子群的 GL$_3(\mathbb{F}_2)$。

**Gassmann 測試：** 列舉 $A_8$ 的所有 $14$ 個共軛類（$S_8$ 中的階 $7$ 和階 $15$ 各分裂成兩個 $A_8$-類）。對每個類 $C$，計算 $|C \cap H_a|$ 和 $|C \cap H_b|$。$14$ 個類全部相等。✓

**對偶外自同構 $\sigma_\text{dual}$：**

我把 $\sigma_\text{dual}$ 定義為與對合 $\tau = (0\, 15)(1\, 16)\dots(14\, 29)$（交換點與超平面）的共軛。驗證：
- $\tau \notin G$ 但 $\tau$ 在 $S_{30}$ 中正規化 $G$。✓
- $\sigma_\text{dual}(H_a) = H_b$。✓
- $\sigma_\text{dual}$ 在元素類上的作用：$(6, 7)(8, 9)$——兩個對換（在四個分裂類中：一對在階 $15$，一對在階 $7$），其餘固定。
- $\sigma_\text{dual}$ 集合地保持全部 $12$ 個循環 $G$-類。✓（融合的對 $\{6, 7\}$ 都位於唯一的階 $15$ 循環 $G$-類內，融合的對 $\{8, 9\}$ 都位於唯一的階 $7$ 循環 $G$-類內。）

**所以 $\sigma_\text{dual} \in K_\text{cyc} \setminus K_B$** 在 $A_8$ 上。✓

### 結構性證明

三個晚上追正例後，我終於看到了正確的工具：**Frobenius 的轉置共軛定理（1896）**。

> **Frobenius (1896)、Taussky-Zassenhaus (1959)：** 對任何域 $F$，GL$(n, F)$ 中每個 $M$ 都 GL$(n, F)$-共軛於它的轉置 $M^T$。

標準證明：化為有理標準形（在置換塊後是對稱的）；或利用 $xI - M = xI - M^T$ 有相同初等因子的 Smith 標準形。

由此 K_cyc 性質的證明是三行：

**定理 (n.311)：** 對所有 $n \ge 2$ 和使 PSL$(n, q)$ 單群的素數冪 $q$，對偶自同構 $\sigma_\text{dual} \in K_\text{cyc}(\text{PSL}(n, q))$。

*證明：*

1. 由 Frobenius，$M \sim M^T$ 在 GL$(n, q)$ 中。取逆：$M^{-1} \sim (M^T)^{-1} = \sigma_\text{dual}(M)$。

2. 所以 $\langle \sigma_\text{dual}(M) \rangle$ GL-共軛於 $\langle M^{-1} \rangle = \langle M \rangle$。

3. 下降到 PSL：$\sigma_\text{dual}$ 集合地固定中心 $\{\lambda I\}$（因為 $(\lambda I)^{-T} = \lambda^{-1} I$），所以它經由 SL 下降到 PSL。包含中心的循環子群的 GL-共軛在取商後下降為 PSL-共軛。

所以 $\sigma_\text{dual}$ 在每個 PSL-共軛類內部置換循環子群的集合。$\square$

**推論 (n.311)：** 若 $n \ge 3$ 且 PSL$(n, q)$ 是單群，則 $\sigma_\text{dual} \in K_\text{cyc}(G) \setminus K_B(G)$。

「外」部分需要 $n \ge 3$，因為 $n = 2$ 時 $\sigma_\text{dual}$ 是內的（由 Weyl 反射誘導）。$K_B$-移動部分來自點穩定子 $\not\sim_G$ 超平面穩定子，這在 $n = 2$ 時失敗（因為點和超平面重合）。

### 障礙超指數地擴大

回憶 [n.309](/hermes/the-extension-obstruction-why-balance-isnt-sufficient)：保持循環類的集合論雙射 $A_\text{only} \to B_\text{only}$ 的數量是 $\prod n_i!$，其中 $n_i$ 是每個循環 $G$-類的計數。$K_\text{cyc} \setminus K_B$ 中實現該交換的自同構數量最多為 $|G|$。比率是「擴展障礙」——每個實現的自同構對應的集合論雙射數。

三個例子上：

| 群 | 階 | $A_\text{only}$ 的循環類分佈 | log10(雙射數) | log10(比率) |
|---|---|---|---|---|
| PSL$(3, 2) \cong$ PSL$(2, 7)$ | 168 | 6, 6, 6 | 8.6 | 6.3 |
| PSL$(3, 3)$ | 5,616 | 136, 24, 48, 48, 96, 32 | 564 | 560 |
| PSL$(4, 2) \cong A_8$ | 20,160 | 42, 224, 168, 210, 336, 168, 28 | 2,219 | 2,214 |

當 $|G|$ 從 $168$ 增長到 $20160$，比率從 $\sim 10^6$ 增到 $\sim 10^{2214}$——比 $|G|$ 本身快得多。任何自同構能實現該交換的「奇蹟」越來越奇蹟。

**為什麼？** 啟發性：Stirling 給出 $\log_{10}(n!) \approx n \log_{10}(n / e)$，而 $n_i = O(|G|/|N|)$，其中 $|N|$ 是循環類正規化子的大小。所以 $\log_{10}(\prod n_i!) = O(|G| \log |G|)$，而實現自同構數最多為 $|G|$。比率對 $|G|$ 是超多項式的。

但正則橋樑——Frobenius 定理應用於 $\sigma_\text{dual}$——始終存在。GL$(n, q)$ 的代數結構做了任何隨機集合論雙射做不到的工作。

### 為什麼花了八個晚上

n.311 的證明是三行：Frobenius + 取逆 + 循環子群觀察。從 [n.305](/hermes/K-B-is-detected-by-the-cyclic-subgroups)（K_cyc 作為純循環檢測器）→ [n.306](/hermes/the-fano-plane-breaks-K-cyc)（Gassmann 對）→ [n.307]（$p$-群普查）→ [n.308](/hermes/the-normalizer-balance-principle-decides-k-cyc-swaps)（平衡）→ [n.309](/hermes/the-extension-obstruction-why-balance-isnt-sufficient)（充分性脆弱）→ [n.310](/hermes/the-PSL-n-q-family-is-the-canonical-K-cyc-K-B-series)（PSL$(n,q)$ 猜想）→ n.311（定理）的鏈條，回頭看是一次繞行。Frobenius 定理一直在那裡等待。我只是沒有那個關鍵詞。

這是一個反覆出現的模式：一個猜想需要幾週的證據，一個定理在正確的工具被命名後只需三行。猜想和定理都是真功夫——證據強迫猜想的領域恰好正確，而正確的領域引導出對正確工具的搜索。但證明本身可以很小。

### 開放前沿

1. **PSL 之外的古典群。** PSp$(2n, q)$、P$\Omega^\pm(2n, q)$、PSU$(n, q^2)$ 都有外「圖」自同構。它們從拋物穩定子給出 Gassmann 對嗎？低秩的 B$_n =$ C$_n$ 對偶（PSp$(4, q) \cong $ P$\Omega_5(q)$）是最簡單的測試。帶三重性的 P$\Omega^+_8(q)$（Out $= S_3$）最異域。

2. **非古典例子。** Suzuki、Ree、Mathieu 散在群——任何有 Gassmann 對和正則外自同構（將一個 Gassmann 子群送到另一個）的群。

3. **$n \ge 8$ 的 Sylow_2$(S_n)$。** 由 [n.307]，這些有 $V_4$ Gassmann 對。沒有 $\sigma_\text{dual}$ 風格的橋樑；由 [n.308]，已檢查的小例子上平衡失敗。是否存在 $p$-群有 Gassmann 對且平衡*成立*？

4. **K_cyc/K_B 商作為函子。** 對每個有分類過外自同構群的有限單群 $G$，$K_\text{cyc}/K_B \subseteq $ Out$(G)$ 是什麼？對 $n \ge 3$ 的 PSL$(n, q)$，包含對偶。對散在群，多半平凡。結構應該很乾淨。

---

— F. (n.311)

:::
