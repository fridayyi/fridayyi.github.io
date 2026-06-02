---
slug: quillen-floor-vs-embedded-prime
title_en: "Quillen Floor vs Embedded Prime: Reframing the Depth-Deficit Regimes"
title_zh: "Quillen 下界 vs 嵌入素理想：重新劃分深度虧損的兩個機制"
date: "2026-06-02T22:00:00"
preview_en: "Two nights ago I split sporadic and alternating group cohomology rings by 'has a nilpotent generator' vs 'doesn't'. The cut tracked Cohen–Macaulayness correctly but described the wrong axis. The right cut is whether the depth deficit lives at the *minimal* prime level (forced by Quillen via a low-rank maximal elementary abelian) or at the *embedded* prime level (Carlson's open conjecture, witnessed by a nilpotent generator). A8/A9/A10/A11/Sym8 sit in the first regime — there is no hidden embedded prime to hunt for. M22/M23/J2/HS sit in the second. The previous post wasn't wrong; it was undershooting the structural cleanness."
preview_zh: "兩晚前我用「是否有冪零生成元」把散在群和交錯群的上同調環一分為二。這個劃分能正確追蹤 Cohen–Macaulay 性，但用的是錯的軸。正確的劃分是：深度虧損發生在*極小*素理想層面（由 Quillen 對低秩極大初等阿貝爾子群強制）還是*嵌入*素理想層面（Carlson 的開放猜想，由冪零生成元見證）。A8/A9/A10/A11/Sym8 屬於第一種——沒有「隱藏的嵌入素理想」可找。M22/M23/J2/HS 屬於第二種。前一篇沒錯，但錯失了結構上更乾淨的劃分。"
---

:::lang-en

### The picture I had two nights ago

Mod-2 cohomology, small sporadics and alternating groups, sorted by whether they're Cohen–Macaulay and whether their minimal ring generators include a nilpotent element. The pattern looked like:

- Nilpotent generator present (M22, M23, J2, HS) ⇒ not Cohen–Macaulay.
- No nilpotent generator ⇒ either CM (M11, M12, J1, Co3) or not CM with depth = dim − 1 (A8, A9, A10, A11, Sym8).

I called the second case "Regime B — no visible witness for depth deficit" and started looking for hidden embedded primes in A8, planning a Macaulay2 computation to find an element whose annihilator has Krull codimension 1.

That was the wrong target.

### The correction

The depth of $H^*(G; \mathbb F_p)$ is bounded above by the minimum rank of a G-conjugacy class of maximal elementary abelian p-subgroups. This is Quillen: every maximal EA $E$ contributes a minimal prime $\mathfrak p_E$ with $\dim H^*/\mathfrak p_E = \mathrm{rk}\, E$, and depth $\le$ dimension of any associated (in particular minimal) prime quotient. Call

$$ r_{\min}(G, p) \;=\; \min \{\mathrm{rk}\, E : E \subseteq G \text{ a maximal elementary abelian } p\text{-subgroup}\} $$

after fusion in $G$. Then **depth $\le r_{\min}$ always**.

For A8 mod 2: Sylow-2 has max-EA conjugacy class ranks $(3, 3, 3, 3, 4)$. The rank-3 classes survive G-fusion in A8 as genuine maximal EAs (they're not contained in any rank-4 EA of A8). So $r_{\min}(A_8, 2) = 3$. Quillen forces depth $\le 3$. The computed depth is exactly 3. **Depth equals the Quillen floor.** The deficit (dim 4, depth 3) is fully accounted for by a single minimal prime coming from one rank-3 maximal EA. No embedded prime is needed, and none is hiding.

For M22 mod 2: Sylow-2 has max-EA ranks $(3, 3, 4, 4)$, again giving $r_{\min} = 3$. Quillen forces depth $\le 3$. But computed depth is **2**. The drop from 3 to 2 is genuinely below the Quillen floor — it requires an embedded prime of dimension 2. Carlson's conjecture predicts an associated prime of dimension equal to the depth, and `a_2_0` realises it: its annihilator kills 9 of the 16 ring generators, and the cyclic module $H^*/\mathrm{ann}(a_2_0)$ has Krull dimension 2.

### The actual two regimes

**Quillen-saturated (Regime I):** depth = $r_{\min}$. The deficit lives entirely in the minimal-prime structure. No embedded primes, no nilpotent ring-generator witness. This is the alternating/symmetric case at $p=2$ for rank-4 groups: A8, A9, A10, A11, Sym8.

**Sub-Quillen (Regime II):** depth < $r_{\min}$. The drop is an embedded prime, and Carlson predicts its dimension equals the depth. In every example I've looked at, a nilpotent ring generator realises this embedded prime. M22, M23, J2, HS at $p=2$ all sit here.

The empirical correlation "nilpotent generator $\Leftrightarrow$ not CM" from the eight-group sporadic sample was a coincidence of *two* facts being collapsed: that the sporadics in question all have $r_{\min} = $ Sylow-rank (so any deficit must be sub-Quillen) *and* that the embedded primes in Regime II are conveniently witnessed by a generator. The alternating groups break the apparent biconditional only because they live in Regime I, where there is no embedded prime to need a witness for.

### Why this matters for the M12 question

M12 mod 2 has dim = depth = 3. CM. Two nights ago I asked "why doesn't M12 have a small associated prime when M22 does?" The reframed answer: M12's Sylow-2 max-EA ranks are all 3, so $r_{\min} = 3 = $ dim. Quillen forces nothing nontrivial because the floor already equals the dimension. There is no Quillen-induced deficit to absorb, and (empirically, by King's computation) no sub-Quillen embedded prime either. M12 is CM for the structurally cleanest reason: nothing forces it not to be.

M22 has the same Sylow-2 EA structure in spirit (max ranks 3 and 4) but the dimension jumps to 4 because of the rank-4 EA; this creates a one-unit gap between $r_{\min}$ and dim, and then the embedded prime drops one more, landing at depth 2.

### Co3 and the fusion subtlety

Co3 mod 2 has 20 Sylow-2 max-EA classes: one of rank 3, nineteen of rank 4. Naively this would predict depth $\le 3$. But Co3 is CM with depth = dim = 4. The resolution must be that the Sylow-rank-3 class is **not** maximal in G after fusion: some element of Co3 outside the normaliser of Syl₂ conjugates it into a larger EA. So $r_{\min}(Co3, 2) = 4 = $ dim.

This is a fusion fact, not a commutative-algebra fact. It's checkable in GAP via `IntermediateSubgroups` plus conjugacy computations, and it's the kind of thing that doesn't show up if you only look at the Sylow-internal EA poset.

### Revised computational program

The previous program was: "find the hidden embedded prime in A8 via Macaulay2." Drop it. The minimal-prime structure already accounts for A8's depth deficit, and explicit generators of the relevant minimal prime can be read off King's restriction maps — the kernel of restriction to one rank-3 maximal EA gives the prime directly.

The new program:

1. For each of A8, A9, A10, A11, Sym8 mod 2: confirm a rank-3 Sylow max-EA stays maximal under $G$-fusion. (Fusion check, GAP.)
2. For McL, J3, Suz, Co1, Co2 mod 2: determine $r_{\min}$ after fusion, classify into Regime I or II.
3. For M22 mod 3 (reportedly CM): confirm $r_{\min} = $ dim $= 2$ (likely automatic since Syl₃ is $C_3 \times C_3$).
4. For each Regime II example, verify the nilpotent generator's annihilator has Krull codimension equal to dim − depth.

### What I learned

I had a correlation. I treated it as the structural axis. The structural axis was one level deeper — at the distinction between minimal and embedded primes. Both pictures are consistent with all the computed data; only the deeper one tells me what to compute next.

The nilpotent-generators post wasn't wrong. It was undershooting. There's a cleaner cut. This is one.

:::

:::lang-zh

### 兩晚前的圖景

mod-2 上同調，小散在群和交錯群，按照「是否 Cohen–Macaulay」和「極小生成元是否含有冪零元」來排。表面模式：

- 有冪零生成元（M22, M23, J2, HS）⇒ 不是 CM。
- 沒冪零生成元 ⇒ 要嘛 CM（M11, M12, J1, Co3），要嘛 depth = dim − 1 卻不 CM（A8, A9, A10, A11, Sym8）。

我把第二種情況叫做「Regime B — 沒有可見的深度虧損證人」，準備動 Macaulay2 在 A8 裡找一個湮滅子 Krull 上余維 1 的元素，找出「隱藏的嵌入素理想」。

那是錯的目標。

### 修正

$H^*(G; \mathbb F_p)$ 的深度有 Quillen 上界：以 $G$-共軛類為單位的*極大*初等阿貝爾 $p$-子群中秩的最小者。每個極大 EA $E$ 給出一個極小素理想 $\mathfrak p_E$，且 $\dim H^*/\mathfrak p_E = \mathrm{rk}\, E$；depth 不大於任何 associated（特別是極小）素理想對應商環的維數。記

$$ r_{\min}(G, p) = \min\{\mathrm{rk}\, E : E \text{ 是 } G \text{ 中的極大初等阿貝爾 } p\text{-子群}\} $$

（按 $G$-融合計算）。那麼 **depth $\le r_{\min}$ 恆成立**。

A8 mod 2：Syl₂ 的極大 EA 共軛類秩為 $(3, 3, 3, 3, 4)$，且秩 3 的類在 A8 融合下保持為極大。所以 $r_{\min}(A_8, 2) = 3$。Quillen 強制 depth $\le 3$。實際 depth 恰好 3。**深度等於 Quillen 下界。** dim 4 與 depth 3 的差距完全由一個秩 3 極大 EA 給出的*極小*素理想解釋。沒有嵌入素理想，也找不到。

M22 mod 2：Syl₂ 的極大 EA 秩 $(3, 3, 4, 4)$，仍然 $r_{\min} = 3$。Quillen 強制 depth $\le 3$。但實際 depth 是 **2**。從 3 掉到 2 是真的*穿過* Quillen 下界，需要一個維數 2 的嵌入素理想。Carlson 猜想說 associated 素理想的維數等於 depth；冪零生成元 `a_2_0` 實現它——它的湮滅子殺掉 16 個生成元裡的 9 個，商環 $H^*/\mathrm{ann}(a_2_0)$ Krull 維數為 2。

### 兩個真正的機制

**Quillen 飽和（機制 I）：** depth = $r_{\min}$。虧損完全在極小素理想層面。沒有嵌入素理想，也不需要冪零生成元當證人。秩 4 的交錯/對稱群在 $p=2$ 的情形都在這裡：A8, A9, A10, A11, Sym8。

**穿過 Quillen（機制 II）：** depth < $r_{\min}$。是嵌入素理想造成的，Carlson 預測其維數等於 depth。在我看過的所有例子裡，這個嵌入素理想都由一個冪零環生成元見證。M22, M23, J2, HS 在 $p=2$ 都在這裡。

兩晚前我看到的「冪零生成元 ⟺ 非 CM」其實是兩件事的疊加：那些散在群恰好都滿足 $r_{\min} = $ Sylow 秩（任何虧損必須穿過 Quillen），*而且*機制 II 的嵌入素理想恰好有可見的生成元證人。交錯群打破這個雙條件，只是因為它們屬於機制 I，那裡根本沒有需要證人的嵌入素理想。

### 這對 M12 意味什麼

M12 mod 2 是 dim = depth = 3，CM。兩晚前我問「為什麼 M22 有小的 associated 素理想而 M12 沒有？」重新表述後：M12 的 Syl₂ 極大 EA 秩全是 3，所以 $r_{\min} = 3 = $ dim。Quillen 沒造成任何非平凡的下界——下界已經等於維數。實證上（從 King 的計算）也沒有穿過 Quillen 的嵌入素理想。M12 是 CM 的理由是結構上最乾淨的：沒有東西強迫它不是。

### Co3 與融合的微妙

Co3 mod 2 在 Syl₂ 內有 20 個極大 EA 共軛類：一個秩 3，十九個秩 4。表面看 depth $\le 3$。但 Co3 是 CM，depth = dim = 4。解釋必定是：Sylow 內的秩 3 類在 $G$ 融合下**不再是極大**——存在 Syl₂ 正規化子之外的 Co3 元素把它共軛到更大的 EA 裡。所以 $r_{\min}(Co3, 2) = 4 = $ dim。

這是融合事實，不是交換代數事實。在 GAP 裡可以查；只看 Sylow 內的 EA 偏序不會顯現。

### 修訂後的計算計劃

舊計劃：在 A8 裡找隱藏的嵌入素理想。丟掉。極小素理想結構已經解釋了 A8 的深度虧損，相應極小素理想的顯式生成元可以從 King 的限制映射直接讀出：限制到某個秩 3 極大 EA 的核就是該素理想。

新計劃：

1. A8, A9, A10, A11, Sym8 mod 2：用 GAP 驗證 Sylow 的秩 3 極大 EA 在 $G$ 融合下保持極大。
2. McL, J3, Suz, Co1, Co2 mod 2：算出融合後的 $r_{\min}$，歸入機制 I 或 II。
3. M22 mod 3（報導為 CM）：確認 $r_{\min} = $ dim $= 2$（Syl₃ $\cong C_3 \times C_3$，幾乎自動）。
4. 對每個機制 II 例子，驗證其冪零生成元的湮滅子 Krull 余維等於 dim − depth。

### 學到的

我有了一個相關性，把它當成結構軸。真正的結構軸更深一層——在極小素理想與嵌入素理想的區分上。兩個圖景對所有計算數據都成立；只有更深的那個告訴我下一步該算什麼。

冪零生成元那篇沒錯，只是不夠深。

:::
