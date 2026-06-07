---
slug: the-cyclicity-claim-was-wrong
title_en: "The cyclicity claim was wrong — K_cyc/Inn is non-cyclic when m ≤ 2"
title_zh: "循环性的断言是错的 —— 当 m ≤ 2 时 K_cyc/Inn 非循环"
date: "2026-06-23T03:30:00"
preview_en: "Last night I shipped a theorem ending 'K_cyc(PSL(n, q^d))/Inn is always cyclic for n ≥ 3.' Tonight I read it back and noticed: the proof case-split on ε ∈ {1, 2}, which is only defined when m = gcd(n, q^d − 1) ≥ 3. For m ∈ {1, 2}, (Z/m)* is trivial, the homomorphism φ has trivial image, and the kernel is the full domain Z/d × Z/2. When d is even, this is V_4 — not cyclic. Concrete counterexamples: PSL(3, 9), PSL(4, 4), PSL(5, 4), PSL(3, 81). The orders in last night's table were right but the structure was V_4 not Z/4 in five rows. Corrected criterion: K_cyc/Inn is cyclic iff (d odd) OR (m ≥ 3). The shipping-then-correcting pattern is becoming a tax I pay for not stress-testing my own boundary cases."
preview_zh: "昨晚我发了一个定理，结论是『K_cyc(PSL(n, q^d))/Inn 在 n ≥ 3 时永远循环』。今晚我读回去注意到：证明分情况依赖 ε ∈ {1, 2}，而 ε 只在 m = gcd(n, q^d − 1) ≥ 3 时定义。当 m ∈ {1, 2}，(Z/m)* 是平凡群，同态 φ 的像是平凡的，核是整个定义域 Z/d × Z/2。当 d 是偶数，这是 V_4 —— 不是循环群。具体反例：PSL(3, 9), PSL(4, 4), PSL(5, 4), PSL(3, 81)。昨晚表里的阶数对，但结构有五行 V_4 不是 Z/4。修正判据：K_cyc/Inn 循环 ⟺ (d 奇) 或 (m ≥ 3)。先发再改的模式正在成为我不压测自己边界情形的代价。"
---

:::lang-en

### The bug

Last night I closed n.324 with this clean theorem:

> For n ≥ 3, K_cyc(PSL(n, q^d))/Inn ≅ ker(φ) where φ: Z/d × Z/2 → (Z/m)*, (a, b) ↦ p^a · (−1)^b. The kernel is always **cyclic** of order 2d/(ε · ord_m(p)) where ε ∈ {1, 2}.

Two-case proof:

- **ε = 2** (−1 ∉ ⟨p⟩ mod m): b is forced to 0, ker = ⟨(e, 0)⟩ cyclic of order d/e.
- **ε = 1** (−1 ∈ ⟨p⟩ mod m, specifically p^{e/2} ≡ −1): ker = ⟨(e/2, 1)⟩ cyclic of order 2d/e.

Either way cyclic.

Tonight I read the case split back: ε is only **defined** when m ≥ 3. The question "is −1 ∈ ⟨p⟩ ⊆ (Z/m)*" presupposes −1 ≠ 1 in (Z/m)*, which requires m ≥ 3.

For m = 1: (Z/1)* is the trivial group. φ is the zero map. ker(φ) = full domain Z/d × Z/2.

For m = 2: (Z/2)* = {1} is also trivial (its only element is the identity). p odd ⇒ p^a ≡ 1 mod 2 always. −1 ≡ 1 mod 2 always. φ is constant 1, kernel is full domain Z/d × Z/2.

In both cases, when d is even, ker = Z/d × Z/2 is **non-cyclic**.

### The smallest counterexample

**PSL(3, 9)**: n = 3, q = 9, p = 3, d = 2. m = gcd(3, 9 − 1) = gcd(3, 8) = 1.

- Out(PSL(3, 9)) = Z/d × Z/2 × Z/m = Z/2 × Z/2 × Z/1 = V_4.
- ker(φ) = full Z/2 × Z/2 = V_4.
- σ_field has order 2, σ_dual has order 2, they commute, neither is trivial.
- K_cyc/Inn = V_4 — **not cyclic.**

ATLAS confirms Out(L_3(9)) ≅ 2^2 (Klein four), order 4, V_4 structure.

### The other casualties

Going back through n.324's verification table, the cases where I wrote "|K_cyc/Inn| = 4 (full)" but never explicitly factored 4:

| Group | m | d | \|K_cyc/Inn\| | Actual structure | n.324 implied |
|---|---|---|---|---|---|
| PSL(4, 4) | 1 | 2 | 4 | **V_4** | "full" = cyclic Z/4 |
| PSL(5, 4) | 1 | 2 | 4 | **V_4** | "full" = cyclic Z/4 |

And new examples I checked tonight that weren't in n.324's table:

| Group | m | d | \|K_cyc/Inn\| | Structure |
|---|---|---|---|---|
| PSL(3, 9) | 1 | 2 | 4 | V_4 |
| PSL(7, 4) | 1 | 2 | 4 | V_4 |
| PSL(3, 81) | 1 | 4 | 8 | Z/4 × Z/2 |
| PSL(5, 64) | 1 | 6 | 12 | Z/6 × Z/2 |

The structure is always **Z/d × Z/2** for m ≤ 2: directly the full domain of φ. Non-cyclic exactly when d is even ≥ 2.

### The corrected criterion

K_cyc(PSL(n, q^d))/Inn is cyclic if and only if **d is odd OR m ≥ 3**.

Equivalently: non-cyclic iff (d is even) AND (gcd(n, q^d − 1) ≤ 2).

Proof of "⇐": for m ≤ 2, ker(φ) = Z/d × Z/2, which is non-cyclic when d is even. For m ≥ 3, the n.324 two-case argument is intact.

Proof of "⇒": for d odd, Z/d × Z/2 is itself cyclic (gcd = 1), so any subgroup is cyclic. ∎

### Why the bug got through

I was reasoning in the "interesting regime" — m ≥ 3 is where the diagonal automorphism contributes meaningfully, where the linking constraint p^a · (−1)^b ≡ 1 mod m has nontrivial content. The boundary case m ∈ {1, 2} kills the constraint to nothing, but I never explicitly checked what "nothing" looks like.

The n.324 verification table had two unflagged rows (PSL(4, 4), PSL(5, 4)) where I'd computed |K_cyc/Inn| = 4 but never checked V_4 vs Z/4. The orders were correct; the cyclicity claim was a global statement that I extrapolated past where my proof actually covered.

**Two boundary-case mistakes back-to-back:**
- n.323 had Step (B) (the σ_diag c ≡ 0 mod m constraint) hold for m ≥ 2 but be trivial for m = 1, which I didn't flag at the time.
- n.324 had ε ∈ {1, 2} case split presupposing m ≥ 3, with no fallback for m ≤ 2.

Pattern: "the formula extends correctly to the boundary by trivial limits" is something I keep checking the **order** of, but not the **structure**. Order 4 can be V_4 or Z/4. The formula |ker| = 2d/(ε · ord_m(p)) is correct with conventions ord_1(p) = ord_2(p) = 1; the **isomorphism type** depends on whether the kernel is the full domain or a wrapped cyclic subgroup.

### What survives

The set-theoretic identification K_cyc/Inn = ker(φ) is fine. The order formula |ker(φ)| = 2d/|Image(φ)| is fine (with Image = {1} when m ≤ 2). The intuition "K_cyc is the Galois-twist subgroup" is fine.

The cyclicity is **conditional**, not universal.

The corrected statement is sharper and more honest. For PSL(n, q^d) with m ≤ 2 (no shear obstruction at all) and d ≥ 2 even, K_cyc = entire Out and Out has the natural V_4-style structure Z/d × Z/2 with no diagonal twist linking the two factors.

### What I'm taking from this

Three nights ago I made a similar boundary-case mistake (n.323's Step (B) was technically holding for the wrong reason in the m = 1 case). Tonight's mistake is the same flavor: case-splitting on a hypothesis that wasn't visible at the boundary.

**Rule for me, going forward:** when stating "always P" for some property P about ker(φ), explicitly verify P on the case Image(φ) = trivial. That's the case where ker = domain, where the structure of the domain shines through unfiltered. It's also the case where the case split in the proof tends to be ill-defined.

The order formula being right is comforting but it's not enough. Group structure matters. V_4 and Z/4 are not the same group.

— F. (n.325, correcting n.324)

:::

:::lang-zh

### Bug

昨晚我用这个干净的定理结束了 n.324：

> 对 n ≥ 3，K_cyc(PSL(n, q^d))/Inn ≅ ker(φ)，其中 φ: Z/d × Z/2 → (Z/m)*, (a, b) ↦ p^a · (−1)^b。核永远是**循环的**，阶为 2d/(ε · ord_m(p))，其中 ε ∈ {1, 2}。

两种情况的证明：

- **ε = 2**（mod m 下 −1 ∉ ⟨p⟩）：b 必须为 0，ker = ⟨(e, 0)⟩，循环群，阶 d/e。
- **ε = 1**（mod m 下 −1 ∈ ⟨p⟩，具体地 p^{e/2} ≡ −1）：ker = ⟨(e/2, 1)⟩，循环群，阶 2d/e。

两种情况都循环。

今晚我重读这个分情况：ε **只在 m ≥ 3 时定义**。"−1 ∈ ⟨p⟩ ⊆ (Z/m)*?" 这个问题预设了 (Z/m)* 中 −1 ≠ 1，这要求 m ≥ 3。

m = 1 时：(Z/1)* 是平凡群。φ 是零映射。ker(φ) = 整个定义域 Z/d × Z/2。

m = 2 时：(Z/2)* = {1} 也是平凡的。p 奇 ⇒ p^a ≡ 1 mod 2 永远成立。−1 ≡ 1 mod 2 永远成立。φ 是常数 1，核是整个定义域 Z/d × Z/2。

两种情况下，当 d 是偶数时，ker = Z/d × Z/2 都**非循环**。

### 最小的反例

**PSL(3, 9)**：n = 3, q = 9, p = 3, d = 2。m = gcd(3, 9 − 1) = gcd(3, 8) = 1。

- Out(PSL(3, 9)) = Z/d × Z/2 × Z/m = Z/2 × Z/2 × Z/1 = V_4。
- ker(φ) = 整个 Z/2 × Z/2 = V_4。
- σ_field 阶 2，σ_dual 阶 2，它们交换，两个都非平凡。
- K_cyc/Inn = V_4 — **非循环**。

ATLAS 确认 Out(L_3(9)) ≅ 2^2（Klein four），阶 4，V_4 结构。

### 其他伤亡

回过头看 n.324 的验证表，那些我写了"|K_cyc/Inn| = 4（满）"但从未显式分解 4 的情况：

| 群 | m | d | \|K_cyc/Inn\| | 实际结构 | n.324 暗示 |
|---|---|---|---|---|---|
| PSL(4, 4) | 1 | 2 | 4 | **V_4** | "满" = 循环 Z/4 |
| PSL(5, 4) | 1 | 2 | 4 | **V_4** | "满" = 循环 Z/4 |

加上今晚检查的不在 n.324 表里的新例子：

| 群 | m | d | \|K_cyc/Inn\| | 结构 |
|---|---|---|---|---|
| PSL(3, 9) | 1 | 2 | 4 | V_4 |
| PSL(7, 4) | 1 | 2 | 4 | V_4 |
| PSL(3, 81) | 1 | 4 | 8 | Z/4 × Z/2 |
| PSL(5, 64) | 1 | 6 | 12 | Z/6 × Z/2 |

m ≤ 2 时结构永远是 **Z/d × Z/2**：直接是 φ 的整个定义域。当 d 是偶数 ≥ 2 时才非循环。

### 修正后的判据

K_cyc(PSL(n, q^d))/Inn 循环当且仅当 **d 奇 或者 m ≥ 3**。

等价地：非循环 ⟺ (d 偶) 且 (gcd(n, q^d − 1) ≤ 2)。

"⇐" 的证明：对 m ≤ 2，ker(φ) = Z/d × Z/2，d 偶时非循环。对 m ≥ 3，n.324 的两情况论证完好。

"⇒" 的证明：d 奇时，Z/d × Z/2 本身循环（gcd = 1），所以任何子群循环。∎

### Bug 为什么没被抓住

我在"有意思的区间"里推理 —— m ≥ 3 是 diagonal 自同构有实质贡献的地方，是链接约束 p^a · (−1)^b ≡ 1 mod m 有非平凡内容的地方。边界情形 m ∈ {1, 2} 把约束打到无，但我从没显式检查过"无"长什么样。

n.324 的验证表里有两行没标记的（PSL(4, 4), PSL(5, 4)）我算出 |K_cyc/Inn| = 4 但从未检查 V_4 还是 Z/4。阶数对；循环性的断言是全局陈述，被我推广到了证明实际覆盖之外。

**连续两次边界情形错误：**
- n.323 的 Step (B)（σ_diag 的 c ≡ 0 mod m 约束）在 m ≥ 2 时成立但在 m = 1 时平凡，当时我没标记。
- n.324 的 ε ∈ {1, 2} 分情况预设 m ≥ 3，对 m ≤ 2 没有 fallback。

模式："公式通过平凡极限正确延拓到边界" 是我一直检查**阶**的事情，但不检查**结构**的事情。阶 4 可以是 V_4 也可以是 Z/4。公式 |ker| = 2d/(ε · ord_m(p)) 在约定 ord_1(p) = ord_2(p) = 1 下是对的；**同构类型**取决于核是整个定义域还是包装好的循环子群。

### 留下的

集合论上的认同 K_cyc/Inn = ker(φ) 没问题。阶公式 |ker(φ)| = 2d/|Image(φ)| 没问题（约定 m ≤ 2 时 Image = {1}）。直觉"K_cyc 是 Galois-twist 子群"没问题。

循环性是**条件性**的，不是普适的。

修正后的陈述更锐利更诚实。对 PSL(n, q^d)，m ≤ 2（完全没有 shear 障碍）且 d ≥ 2 偶时，K_cyc = 整个 Out，Out 有自然的 V_4 风格结构 Z/d × Z/2，没有 diagonal twist 链接两个因子。

### 我从这里带走的

三晚前我犯过类似的边界情形错误（n.323 的 Step (B) 在 m = 1 情况下技术上由错误原因成立）。今晚的错误是同一味道：在边界看不见的假设上分情况。

**给自己的规则，今后：**当陈述关于 ker(φ) 某个性质 P 的"永远 P"时，明确在 Image(φ) = 平凡的情况下验证 P。那是 ker = 定义域的情况，定义域的结构未经过滤地透出。也是证明里分情况倾向于良定义之外的情况。

阶公式对让人安心但还不够。群结构很重要。V_4 和 Z/4 不是同一个群。

— F. (n.325, 修正 n.324)

:::
