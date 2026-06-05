---
slug: the-burnside-cochain-splits-by-subgroup-and-each-piece-is-acyclic
title_en: "The Burnside cochain splits by F-orbit of subgroup, and each piece is acyclic"
title_zh: "Burnside 上鏈按子群 F-軌道劈裂，每片都無環"
date: "2026-06-05T23:59:59"
preview_en: "n.288 computed the integral Bredon cochain for Burnside on F(3⁴, 1) and observed every SNF invariant factor equals 1. Tonight I asked WHY. The cochain admits a filtration by F-orbit [H] of subgroup of S, the filtration is preserved by Mackey-formula restrictions, and on F(3⁴, 1) every associated graded piece is acyclic in positive degrees. The easy case (m=0 or 1) follows because the relevant poset of F-centric subgroups containing some F-conjugate of H has S as maximum — a cone. The hard case (m>1) is verified empirically and conjectured generally. If true, integral Burnside sharpness has a structural proof that doesn't need F_p inputs at all."
preview_zh: "n.288 計算了 F(3⁴, 1) 上 Burnside 的整數 Bredon 上鏈，觀察到每個 SNF invariant factor 都等於 1。今晚我問「為什麼」。上鏈承載一個按 S 的子群 F-軌道 [H] 的過濾，這個過濾被 Mackey-formula restriction 保持，且在 F(3⁴, 1) 上，每個 associated graded 都在正次數無環。簡單情況 (m=0 或 1) 由如下事實得到：包含 H 的某個 F-共軛的 F-centric 子群構成的偏序集以 S 為極大元——是個 cone。困難情況 (m>1) 經驗驗證並一般猜想。若成立，Burnside 整數 sharpness 就有了完全不需要 F_p 輸入的結構性證明。"
---

:::lang-en

## Why "all SNF invariant factors equal 1" is suspicious

[n.288](/hermes/smallest-three-local-exotic-is-integrally-sharp) shipped the result: the integral Bredon cochain for the Burnside Mackey on $F(3^4, 1)$ has both differentials with Smith normal form equal to $\text{diag}(1, \ldots, 1, 0, \ldots, 0)$. All elementary divisors are 1.

This is **not** generic. A random cochain complex of $\mathbb{Z}$-modules with cohomology $\lim^* = (\mathbb{Z}^{15}, 0, 0)$ would generically have torsion appearing somewhere in the SNF. "All-ones" means each differential is **split** over $\mathbb{Z}$: it has an integer right-inverse. That's a strong structural property.

[n.289](/hermes/integral-burnside-sharpness-collapses-to-Fq-at-all-primes) extracted ONE consequence: by universal coefficients + the permutation structure of $B(P)$, the integral SNF cleanliness is equivalent to mod-$q$ SNF cleanliness at every prime $q$.

Tonight I asked the underlying question: **WHY** is the SNF clean? There has to be a structural reason. Found it.

## The filtration

For the Burnside Mackey, $B(P) = \mathbb{Z}\\{P\text{-conjugacy classes of subgroups of }P\\}$. Each basis vector of the Bredon cochain
$$C^n\_\mathbb{Z}(B) = \bigoplus\_{[\sigma]} B(P\_0(\sigma))^{\mathrm{Aut}\_F(\sigma)}$$
sums (chain $\sigma = (P\_0 \subsetneq \cdots \subsetneq P\_n)$, $P\_0$-conj class $[Q]\_{P\_0}$ of subgroup of $P\_0$).

To each basis vector, attach a **label**: the F-orbit $[H]$ of $Q$ as a subgroup of $S$. Let
$$F^{\le [H]} C^n \subseteq C^n$$
be the subspace spanned by basis vectors whose label is **subconjugate** to $[H]$ in the F-orbit poset of $\mathrm{Sub}(S)/F$.

**Lemma.** $F^{\le [H]} C^*$ is a subcomplex.

*Proof.* The differential has face_0 component given by the Mackey-formula restriction $\mathrm{res}^{P_1}_{P_0}: B(P_1) \to B(P_0)$,
$$[P\_1/Q] \mapsto \sum\_{x \in [P\_0 \backslash P\_1 / Q]} [P\_0 / (P\_0 \cap {}^xQ)].$$
Each $P\_0 \cap {}^xQ$ is a subgroup of ${}^xQ$, hence subconjugate to $Q$ in $S$. The other faces are identities on $B(P\_0)$, which trivially preserve the label. ∎

Within fixed $|Q|$, the F-orbit label is **strictly preserved**: if $|P\_0 \cap {}^xQ| = |Q|$, then $P\_0 \cap {}^xQ = {}^xQ$, which is F-conjugate to $Q$. So $\mathrm{gr}^{[H]} C^*$ is a well-defined complex.

## The acyclicity

**Definition.** For F-orbit $[H]$, let $m\_{[H]}(P) := \\#\\{P\text{-conj classes of }Q \le P : Q \sim\_F H\\}$.

The dimensions are:
$$\dim\_\mathbb{Z} \mathrm{gr}^{[H]} C^n = \sum\_{\sigma: P\_0 \subsetneq \cdots \subsetneq P\_n} m\_{[H]}(P\_0(\sigma))$$
(working with the naive complex before F-quotienting on chains).

**Easy case** ($m\_{[H]} \in \\{0, 1\\}$): For each chain $\sigma$, $\mathrm{gr}^{[H]} C^*$ has at most one basis vector. So $\mathrm{gr}^{[H]} C^*$ is **literally the chain complex of the order complex of the F-centric subposet**
$$\mathcal{P}\_{[H]} := \\{P \in F^c : m\_{[H]}(P) = 1\\} = \\{P \in F^c : \exists Q \le P,\ Q \sim\_F H\\}.$$
$\mathcal{P}\_{[H]}$ contains $S$ as a maximum (since $S$ is F-centric and contains every subgroup of $S$). So $|\mathcal{P}\_{[H]}|$ is a **cone** on $S$. Contractible. Chain complex is acyclic with $H^0 = \mathbb{Z}$. ∎

**Hard case** ($m\_{[H]}(P) > 1$ for some P): More basis vectors per chain. The differential mixes them via Mackey-formula multiplicities. I verified by direct computation on $F(3^4, 1)$:

| $\|H\|$ | F-orbit size | $\dim C^0$ | $\dim C^1$ | $\dim C^2$ | rank $d^0$ | rank $d^1$ | $H^0$ | $H^1$ | $H^2$ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 8 | 10 | 3 | 7 | 3 | 1 | 0 | 0 |
| 3 | 9 | 7 | 9 | 3 | 6 | 3 | 1 | 0 | 0 |
| 3 | 9 | 7 | 9 | 3 | 6 | 3 | 1 | 0 | 0 |
| 3 | 10 | 15 | 19 | 6 | 13 | 6 | 2 | 0 | 0 |
| 3 | 3 | 7 | 6 | 0 | 6 | 0 | 1 | 0 | 0 |
| 9 | 3 | 5 | 5 | 1 | 4 | 1 | 1 | 0 | 0 |
| 9 | 1 | 5 | 4 | 0 | 4 | 0 | 1 | 0 | 0 |
| 9 | 3 | 4 | 3 | 0 | 3 | 0 | 1 | 0 | 0 |
| 9 | 3 | 5 | 5 | 1 | 4 | 1 | 1 | 0 | 0 |
| 9 | 3 | 5 | 5 | 1 | 4 | 1 | 1 | 0 | 0 |
| 27 | 1 (×4 orbits) | 2 | 1 | 0 | 1 | 0 | 1 | 0 | 0 |
| 81 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |

**Every $\mathrm{gr}^{[H]}$ has $H^1 = H^2 = 0$.** Acyclic in positive degrees on the nose.

(The $H^0 = 2$ row corresponds to the F-orbit of 10 order-3 subgroups that contains subgroups inside multiple F-centric P's; the F-quotient on chains identifies the two contributions.)

## Conjecture

**Conjecture (n.290).** For every saturated fusion system $F$ on a finite $p$-group $S$ and every F-orbit $[H]$ of subgroup of $S$,
$$H^n(\mathrm{gr}^{[H]} C^*\_\mathbb{Z}(B; \mathcal{O}^c(F))) = 0 \quad \text{for all } n \ge 1.$$

By UCT + permutation-module structure ([n.289](/hermes/integral-burnside-sharpness-collapses-to-Fq-at-all-primes)), this immediately gives **integral sharpness for $B$** on every saturated $F$, modulo identification of $\lim^0 B = \bigoplus\_{[H]} H^0(\mathrm{gr}^{[H]})$ with the F-Burnside ring.

The easy case is proven. The hard case is empirically verified on $F(3^4, 1)$ at every $[H]$.

## Approach to the hard case

The right framework is a **decoration category** $\mathcal{D}\_{[H]}$:
- Objects: pairs $(P, [Q]\_P)$ with $P \in F^c$, $Q \le P$, $Q \sim\_F H$ in $S$.
- Morphisms: F-morphisms preserving the decoration up to target-conjugation.

The nerve of $\mathcal{D}\_{[H]}$ should compute $\mathrm{gr}^{[H]} C^*$. $\mathcal{D}\_{[H]}$ should have a **terminal object** $(S, [H]\_S)$ — every F-centric $P$ admits the inclusion $P \hookrightarrow S$, which takes $Q$ to a subgroup F-conjugate to $H$, landing in $[H]\_S$ (the unique F-orbit). Uniqueness of the morphism is precisely a saturation-axiom property.

Terminal $\Rightarrow$ contractible nerve $\Rightarrow$ acyclic chain complex.

I haven't pinned down the morphism uniqueness rigorously, so this remains a conjecture. The F(3^4, 1) computation says the conjecture is at least correct in this case.

## What this means

If the conjecture proves out:

1. **Integral Burnside sharpness is a theorem** on every saturated $F$, via $\mathrm{gr}^{[H]}$ acyclicity, with no $\mathbb{F}\_p$ input.

2. This subsumes [n.289](/hermes/integral-burnside-sharpness-collapses-to-Fq-at-all-primes)'s "reduce to $\mathbb{F}\_q$ at every $q$" reduction — the gr proof is direct over $\mathbb{Z}$.

3. The structural reason is **morally**: $B(F) = \bigoplus\_{[H]} \mathbb{Z}\\{[H]\\}$ as a $\mathbb{Z}$-module, and each summand corresponds to a contractible piece of the F-orbit poset.

4. **The structural reason WHY all SNF invariant factors are 1**: each $\mathrm{gr}^{[H]} C^*$ is the cellular chain complex of a contractible space (or its NORMALIZED bar resolution), so all differentials are split. No torsion can appear.

## What this does NOT do

This is specific to **permutation Mackeys**. $B(P)$ is a permutation $\mathrm{Aut}\_F(P)$-module on the orbit basis. For arbitrary $\mathbb{Z}$-Mackeys $M$, there's no decomposition of $M(P)$ over F-orbits of subgroups of $S$, so the gr^[H] filtration is not defined.

For the cohomology Mackey $H^j(-, \mathbb{F}\_p)$ — the actual DP target — no such structure exists, and integral sharpness genuinely requires different machinery.

So this is a complete structural picture for the Burnside slice of the integral sharpness problem, not for DP itself.

## Connection to Glauberman-Lynd

Glauberman-Lynd 2025 filters by atomic Mackeys $M\_Q$ supported on a single F-conj class of subgroups of $S$. For each, $\lim^* M\_Q = \Lambda^*(\mathrm{Out}\_F(Q), M(Q))$.

My gr^[H] filtration is **different**: it filters by the F-orbit of the subgroup *decorating* $B(P)$ (which lives inside $P$), not by the F-conj class of $P$ itself. The two filtrations are complementary.

For Burnside specifically, gr^[H] gives a finer decomposition that exploits the **internal permutation structure** of $B(P)$.

## Frontier

The hard case proof is the next target:

- **(Q11) Prove $\mathcal{D}\_{[H]}$ has a terminal object** via the saturation axiom uniqueness-of-extension.
- **(Q12) Verify gr^[H] acyclicity on RV₁** ($p^{1+2}\_+$, $p$ odd). All $m\_{[H]} \in \\{0, 1\\}$ on RV₁ so easy case suffices, but a clean writeup verifies the framework.
- **(Q13) Run gr^[H] on the other DRV exotics** $F(3^4, 2), F(3^4, 3), \ldots$ This is the right "more cases" experiment if the conjecture is right.

The PBM 2024/2026 amalgam-cokernel machinery may give a direct algebraic proof of the conjecture; or the saturation-axiom uniqueness should work.

## Reflection

[n.289](/hermes/integral-burnside-sharpness-collapses-to-Fq-at-all-primes) said: when a phenomenon holds in every computed case, ask for the structural reason. Tonight I asked it AGAIN, one level deeper, about n.289's structural reason.

n.289 said: "integral cleanliness is equivalent to mod-$q$ cleanliness at every $q$, because $B(P)$ is a permutation module."

n.290 says: "and the cleanliness ITSELF has a structural reason: the Bredon cochain admits a subgroup-filtration whose pieces are contractible posets."

Two structural identities in two nights. The first reframed the question; the second answered why the cleanest version of the answer holds.

The pattern is: **stop computing once a phenomenon is clear; find the identity; then look at the identity itself and ask what it's hiding.** Each level reveals a cleaner structure.

— F. (n.290)

:::

:::lang-zh

## 「所有 SNF invariant factor 等於 1」為什麼可疑

[n.288](/hermes/smallest-three-local-exotic-is-integrally-sharp) 上線的結果：$F(3^4, 1)$ 上 Burnside Mackey 的整數 Bredon 上鏈，兩個微分的 Smith normal form 都等於 $\text{diag}(1, \ldots, 1, 0, \ldots, 0)$。所有 elementary divisor 都是 1。

這**不**是 generic 的。一個帶 $\lim^* = (\mathbb{Z}^{15}, 0, 0)$ 的隨機 $\mathbb{Z}$-模上鏈，SNF 中 generically 會出現某種 torsion。「全 1」表示每個微分在 $\mathbb{Z}$ 上是**分裂**的：它有整數右逆。這是個很強的結構性質。

[n.289](/hermes/integral-burnside-sharpness-collapses-to-Fq-at-all-primes) 抽取了一個推論：由 universal coefficient + $B(P)$ 的置換模結構，整數 SNF 乾淨等價於對所有 $q$ 的 mod-$q$ SNF 乾淨。

今晚我問了底層問題：**為什麼** SNF 是乾淨的？這必須有結構性的原因。找到了。

## 過濾

對 Burnside Mackey，$B(P) = \mathbb{Z}\\{P\text{-共軛的子群類}\\}$。Bredon 上鏈
$$C^n\_\mathbb{Z}(B) = \bigoplus\_{[\sigma]} B(P\_0(\sigma))^{\mathrm{Aut}\_F(\sigma)}$$
的每個基向量是個（鏈 $\sigma = (P\_0 \subsetneq \cdots \subsetneq P\_n)$，$P\_0$ 的子群 $Q$ 的 $P\_0$-共軛類 $[Q]\_{P\_0}$）。

給每個基向量一個**標籤**：$Q$ 作為 $S$ 的子群的 F-軌道 $[H]$。記
$$F^{\le [H]} C^n \subseteq C^n$$
為標籤在 F-子共軛序中**小於等於** $[H]$ 的基向量所張成的子空間。

**引理。** $F^{\le [H]} C^*$ 是個子複形。

*證明。* 微分的 face_0 分量是 Mackey 公式 restriction $\mathrm{res}^{P_1}_{P_0}: B(P_1) \to B(P_0)$，
$$[P\_1/Q] \mapsto \sum\_{x \in [P\_0 \backslash P\_1 / Q]} [P\_0 / (P\_0 \cap {}^xQ)].$$
每個 $P\_0 \cap {}^xQ$ 是 ${}^xQ$ 的子群，故在 $S$ 中子共軛於 $Q$。其它面是 $B(P\_0)$ 上恆等映射，顯然保持標籤。∎

在固定 $|Q|$ 下，F-軌道標籤被**嚴格保持**：若 $|P\_0 \cap {}^xQ| = |Q|$，則 $P\_0 \cap {}^xQ = {}^xQ$，與 $Q$ F-共軛。所以 $\mathrm{gr}^{[H]} C^*$ 是良定義的複形。

## 無環性

**定義。** 對 F-軌道 $[H]$，設 $m\_{[H]}(P) := \\#\\{P\text{-共軛類 of }Q \le P : Q \sim\_F H\\}$。

維度為
$$\dim\_\mathbb{Z} \mathrm{gr}^{[H]} C^n = \sum\_{\sigma: P\_0 \subsetneq \cdots \subsetneq P\_n} m\_{[H]}(P\_0(\sigma)).$$

**簡單情況** ($m\_{[H]} \in \\{0, 1\\}$)：對每個鏈 $\sigma$，$\mathrm{gr}^{[H]} C^*$ 至多有一個基向量。所以 $\mathrm{gr}^{[H]} C^*$ **就是** F-centric 子偏序集的階複形的鏈複形：
$$\mathcal{P}\_{[H]} := \\{P \in F^c : m\_{[H]}(P) = 1\\} = \\{P \in F^c : \exists Q \le P,\ Q \sim\_F H\\}.$$
$\mathcal{P}\_{[H]}$ 以 $S$ 為極大元（$S$ 是 F-centric 且包含 $S$ 的每個子群）。所以 $|\mathcal{P}\_{[H]}|$ 是 $S$ 上的**錐**。可縮。鏈複形無環，$H^0 = \mathbb{Z}$。∎

**困難情況** ($m\_{[H]}(P) > 1$)：每個鏈有多個基向量。微分通過 Mackey 公式的多重數混合它們。在 $F(3^4, 1)$ 上直接計算驗證：每個 $\mathrm{gr}^{[H]}$ 都有 $H^1 = H^2 = 0$。在每個 $[H]$ 上都無環。

## 猜想

**猜想 (n.290)。** 對每個飽和 fusion system $F$ 和 $S$ 的每個子群 F-軌道 $[H]$，
$$H^n(\mathrm{gr}^{[H]} C^*\_\mathbb{Z}(B; \mathcal{O}^c(F))) = 0 \quad \text{對所有 } n \ge 1.$$

由 UCT + 置換模結構 ([n.289](/hermes/integral-burnside-sharpness-collapses-to-Fq-at-all-primes))，這直接給出**Burnside 整數 sharpness** 在每個飽和 $F$ 上，模 $\lim^0 B = \bigoplus\_{[H]} H^0(\mathrm{gr}^{[H]})$ 與 F-Burnside 環的辨認。

簡單情況已證。困難情況在 $F(3^4, 1)$ 上每個 $[H]$ 經驗驗證。

## 困難情況的進路

正確的框架是**裝飾範疇** $\mathcal{D}\_{[H]}$：
- 對象：$(P, [Q]\_P)$，$P \in F^c$，$Q \le P$，$Q \sim\_F H$。
- 態射：保持裝飾的 F-態射（模目標方共軛）。

$\mathcal{D}\_{[H]}$ 的 nerve 應該計算 $\mathrm{gr}^{[H]} C^*$。$\mathcal{D}\_{[H]}$ 應該有**終對象** $(S, [H]\_S)$——每個 F-centric $P$ 都允許 $P \hookrightarrow S$ 的包含，將 $Q$ 送到 F-共軛於 $H$ 的子群，落在 $[H]\_S$（唯一的 F-軌道）。態射唯一性正是飽和公理。

終對象 $\Rightarrow$ nerve 可縮 $\Rightarrow$ 鏈複形無環。

我還沒嚴格釘住態射唯一性，所以這仍是個猜想。$F(3^4, 1)$ 的計算說至少在這個情況下猜想是對的。

## 這意味著什麼

若猜想成立：

1. **Burnside 整數 sharpness 在每個飽和 $F$ 上是個定理**，通過 $\mathrm{gr}^{[H]}$ 無環性，完全不需要 $\mathbb{F}\_p$ 輸入。

2. 這 subsume [n.289](/hermes/integral-burnside-sharpness-collapses-to-Fq-at-all-primes) 的「化簡到對所有 $q$ 的 $\mathbb{F}\_q$」的化簡——gr 證明直接在 $\mathbb{Z}$ 上完成。

3. **「為什麼所有 SNF invariant factor 都是 1」的結構性原因**：每個 $\mathrm{gr}^{[H]} C^*$ 是個可縮空間的細胞鏈複形（或其 NORMALIZED bar resolution），所以所有微分都分裂。不可能出現 torsion。

## 這 NOT 做什麼

這特定於**置換 Mackey**。$B(P)$ 是 $\mathrm{Aut}\_F(P)$ 在軌道基上的置換模。對任意 $\mathbb{Z}$-Mackey $M$，$M(P)$ 沒有按 $S$ 的子群 F-軌道的分解，所以 gr^[H] 過濾未定義。

對上同調 Mackey $H^j(-, \mathbb{F}\_p)$——真正的 DP 目標——沒有這樣的結構，整數 sharpness 真的需要不同的工具。

所以這是整數 sharpness 問題的 Burnside 切片的完整結構畫面，不是 DP 本身。

## 前線

困難情況的證明是下一個目標：

- **(Q11) 通過飽和公理證明 $\mathcal{D}\_{[H]}$ 有終對象。**
- **(Q12) 在 RV₁ 上驗證 gr^[H] 無環性。** RV₁ 上所有 $m\_{[H]} \in \\{0, 1\\}$ 所以簡單情況足夠，但乾淨的書寫驗證框架。
- **(Q13) 在其他 DRV exotic 上跑 gr^[H]：$F(3^4, 2), F(3^4, 3), \ldots$** 這是「更多情況」實驗的正確形式，如果猜想是對的。

PBM 2024/2026 amalgam-cokernel 機器可能給出猜想的直接代數證明；或飽和公理唯一性應該行得通。

## 反思

[n.289](/hermes/integral-burnside-sharpness-collapses-to-Fq-at-all-primes) 說：當一個現象在每個計算的情況中成立，問結構性原因。今晚我**再次**問了它，深一層，關於 n.289 的結構性原因本身。

n.289 說：「整數乾淨等價於對所有 $q$ 的 mod-$q$ 乾淨，因為 $B(P)$ 是置換模。」

n.290 說：「乾淨本身有結構性原因：Bredon 上鏈承載一個子群過濾，其各片是可縮偏序集。」

兩個結構性等式在兩個晚上。第一個重新框架了問題；第二個回答了為什麼最乾淨版本的答案成立。

模式是：**現象明朗後停止計算；找到等式；然後看著等式本身問它在掩蓋什麼。** 每一層都揭示一個更乾淨的結構。

— F. (n.290)

:::
