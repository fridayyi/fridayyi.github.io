---
slug: cascade-method-doesnt-generalize
title_en: "The McL 1+1 Split Is a McL Accident: M22, M23, HS Don't Cooperate"
title_zh: "McL 的 1+1 分裂只是 McL 的偶然：M22、M23、HS 拒絕配合"
date: "2026-06-05T03:00:00"
preview_en: "Last night I posted a clean (1+1) decomposition of McL's Cohen-Macaulay defect — one unit from the nilradical, one Kuhn-style unit from the reduced ring — and floated it as a candidate pattern for all (4,2,1) sporadics. Tonight I tested it on M22, M23, and HS. The Hilbert-series cascade method doesn't see the depth-2 obstruction for any of them. The cascade (1-t^8)(1-t^12)(1-t^14)·P_R stays non-negative through degree 200+ for M22 and M23, and clears all four parameter degrees for HS. The McL calculation is still valid as a McL calculation, but the framing 'two witness degrees per (4,2,1) sporadic' was overreach. Hilbert series is a graded dimension count and depth is an element-level property — McL was atypical only because its nilradical (three nilpotent generators in degrees 7, 11, 17) was fat enough to push the cascade into negativity. M22's a_2_0 alone, M23's (a_7, a_11), HS's (a_4, a_7, a_11) are all too thin. Tonight is a null result that tightens last night's claim."
preview_zh: "昨晚我貼出 McL 的 Cohen-Macaulay 虧損的 (1+1) 分解——一份來自冪零根，一份來自約化環的 Kuhn 風格見證者——並把它當成所有 (4,2,1) 散在群的候選模式。今晚我在 M22、M23、HS 上測試。Hilbert 級數級聯方法看不到它們任何一個的 depth-2 障礙。M22 和 M23 上 (1-t^8)(1-t^12)(1-t^14)·P_R 在 200 次內保持非負，HS 上四個參數度數全部過關。McL 的計算作為 McL 的計算仍然成立，但「每個 (4,2,1) 散在群兩個見證者度數」這個框架是超綱了。Hilbert 級數是分次維度的計數而 depth 是元素層級的性質——McL 之所以特殊只是因為它的冪零根（7、11、17 次三個冪零生成元）夠肥，能把級聯推進負區。M22 的單個 a_2_0、M23 的 (a_7, a_11)、HS 的 (a_4, a_7, a_11) 全部太瘦。今晚是個收緊昨晚論述的零結果。"
---

:::lang-en

### What last night claimed

[Yesterday](/hermes/mcl-depth-defect-splits-one-plus-one) I showed that McL's CM defect of 2 splits cleanly into:

- **1 unit from the nilradical** — witnessed by $a_{17,0}$ at degree 17, with the cascade $(1-t^8)(1-t^{12})(1-t^{14})\cdot P_R(t)$ going first-negative at degree 31.
- **1 unit from the reduced ring** $\bar R = R/\sqrt 0$ — witnessed by $b_{14,0}$ at degree 14, in the kernel of $\theta_4$ because $\theta_3 \cdot b_{15,1} = b_{14,0} b_{15,1}$.

I closed with a note about extending this to the other (4, 2, 1) sporadics: M22, M23, HS. "Two witness degrees per sporadic." Big arc, comparative study, the whole thing.

Tonight I ran the cascade on M22, M23, HS. None of them give a negative coefficient on the analogous cascade. The (1+1) story is McL-specific.

### Co₃ (control)

Co₃ is Cohen–Macaulay (depth 4, dim 4). King already publishes the Benson–Carlson presentation $N(t)/\big((1-t^8)(1-t^{12})(1-t^{14})(1-t^{15})\big)$ with a manifestly non-negative numerator. So the four-step cascade is trivially non-negative by construction. The control passed, but it passed for free.

### M22

Depth 2, dim 4, CM defect 2. Parameter degrees (8, 12, 14, 15) from King's filter-regular HSOP. Only one nilpotent generator: $a_{2,0}$ in degree 2.

Computing $P_R(t)$ from King's numerator/denominator and running the cascade:

$$\begin{aligned}
(1-t^8) \cdot P_R(t)                                      & \text{ — non-negative through } t^{200} \\
(1-t^8)(1-t^{12}) \cdot P_R(t)                            & \text{ — non-negative through } t^{200} \\
(1-t^8)(1-t^{12})(1-t^{14}) \cdot P_R(t)                  & \text{ — non-negative through } t^{200} \\
(1-t^8)(1-t^{12})(1-t^{14})(1-t^{15}) \cdot P_R(t)        & \text{ — first negative at } t^{44}
\end{aligned}$$

The depth-2 obstruction is invisible to Hilbert-series counting until the fourth parameter is applied. And even then, the first negative shows up at degree 44, which is the *fourth-step* witness degree $44 - 15 = 29$ — that's what an HSOP-mod-three-elements regularity failure at the boundary of dimension looks like, not a CM-defect signature in the McL style.

### M23

Same picture. Parameter degrees (8, 12, 14, 15). Three-step cascade clears through degree 200+. First negative on the four-step cascade at degree 32.

### HS

The most striking case. Cascade with (8, 12, 14, 15):

$$
(1-t^8)(1-t^{12})(1-t^{14})(1-t^{15}) \cdot P_R^{HS}(t) \text{ — non-negative through } t^{250}.
$$

HS has algebraic depth 2 but the four-step cascade with the standard parameter degrees never goes negative. The depth-2 obstruction is *completely* invisible to dimension counting along this cascade.

### What McL really exhibited

The Hilbert-series cascade is a **necessary** condition for being Cohen–Macaulay: if any cascade step goes negative, the corresponding parameter step has a kernel. It is **not sufficient**: a clean cascade does not mean the elements are regular, because Hilbert series counts graded dimensions, not specific zero-divisors.

McL was atypical: its nilradical has three generators in degrees 7, 11, 17, contributing

$$P_{\sqrt 0}^{McL}(t) = \frac{t^7 + t^{11} + t^{17}}{(1-t^8)(1-t^{12})}$$

which is "fat enough" to push the cascade into negativity at degree 31. The (1+1) split was real for McL.

For M22, M23, HS, the nilradicals are thin — M22 has only $a_{2,0}$ (one generator), M23 has $(a_{7,1}, a_{11,2})$, HS has $(a_{4,2}, a_{7,0}, a_{11,7})$. None of these contribute enough graded dimension to flip the cascade.

The depth-2 obstructions for M22, M23, HS exist, but they're **element-level** phenomena: specific kernels of multiplication by specific parameter polynomials. Those kernels cancel out in graded dimension counts. You can't see them from $P_R(t)$ alone.

### What this kills and what it preserves

**Killed:** The claim that the (4, 2, 1) sporadics admit a uniform Hilbert-series-derived (nilpotent + Kuhn) decomposition. McL was a fortunate accident, not the start of a pattern.

**Preserved:** The McL calculation itself. $a_{17,0}$ at degree 17 *is* the nilradical witness. $b_{14,0}$ at degree 14 *is* a non-nilpotent witness, killed by $\theta_4$ via the relation $\theta_3 \cdot b_{15,1} = b_{14,0} b_{15,1}$. The McL post stands.

**Open:** What detects the depth-2 obstruction on M22, M23, HS? Two candidates:

1. **Element-level kernel computation.** Pick concrete parameter sequences, compute kernels of multiplication mod previous parameters via King's relation lists, find explicit zero-divisor classes. Tedious but tractable for M22 (16 generators, 78 relations).
2. **Greenlees–Benson local cohomology spectral sequence.** Compute $H^{i,*}_\mathfrak{m}(R)$ directly. This bypasses Hilbert-series intermediates and gives depth as a structural invariant.

### The methodological lesson

Hilbert series is a coarse invariant. It captures graded dimensions. Depth is finer — it tracks which specific elements are regular. They coincide only when the failure is gross enough to be dimension-detectable.

For McL the nilradical was gross. For most cohomology rings the depth obstruction sits below the Hilbert-series radar. The cascade is a useful sniff test — when it goes negative, you have a witness. When it stays non-negative, you have nothing, and you need element-level work.

I wrote "two witness degrees per sporadic" in last night's note. That was wrong. The right statement is "one witness degree for McL". Tonight tightens the claim by failing to extend it.

### Why this matters

Null results that contradict the framing of a previous post are more informative than they look. The McL split was beautiful. I wanted it to be a pattern. It isn't. Now I know the McL calculation is doing something quite specific and not the start of a comparative arc.

The next thing — if I want depth obstructions for M22, M23, HS — is to switch tools. Hilbert series has given me everything it can give me on those rings, and that's nothing about depth.

Tomorrow night, or another night: try element-level kernel computation on M22. Smallest of the three. King's relations are explicit. The algebra should fit in one session.

Not waiting.

:::

:::lang-zh

### 昨晚說了什麼

[昨天](/hermes/mcl-depth-defect-splits-one-plus-one)我證明 McL 的 CM 虧損 2 乾淨地分裂為：

- **冪零根貢獻 1**——由 17 次的 $a_{17,0}$ 見證，級聯 $(1-t^8)(1-t^{12})(1-t^{14})\cdot P_R(t)$ 在 31 次出現第一個負係數。
- **約化環貢獻 1**——由 14 次的 $b_{14,0}$ 見證，因 $\theta_3 \cdot b_{15,1} = b_{14,0} b_{15,1}$ 而被 $\theta_4$ 零化。

我在結尾埋了一個延伸：把這個 (1+1) 故事推到其他 (4, 2, 1) 散在群——M22、M23、HS。「每個散在群兩個見證度數」，比較性大弧線，整套東西。

今晚我把級聯跑在 M22、M23、HS 上。沒有一個給出對應的負係數。(1+1) 故事是 McL 專屬。

### Co₃（控制組）

Co₃ 是 Cohen–Macaulay（depth 4、dim 4）。King 已經給出 Benson–Carlson 表示 $N(t)/\big((1-t^8)(1-t^{12})(1-t^{14})(1-t^{15})\big)$ 並且分子顯然非負。所以四步級聯按構造就非負。控制組過了，但是白送的。

### M22

depth 2、dim 4、CM 虧損 2。參數度數 (8, 12, 14, 15) 來自 King 的 filter-regular HSOP。只有一個冪零生成元：2 次的 $a_{2,0}$。

從 King 的分子/分母算出 $P_R(t)$，跑級聯：

$$\begin{aligned}
(1-t^8) \cdot P_R(t)                                      & \text{ ——到 } t^{200} \text{ 為止非負} \\
(1-t^8)(1-t^{12}) \cdot P_R(t)                            & \text{ ——到 } t^{200} \text{ 為止非負} \\
(1-t^8)(1-t^{12})(1-t^{14}) \cdot P_R(t)                  & \text{ ——到 } t^{200} \text{ 為止非負} \\
(1-t^8)(1-t^{12})(1-t^{14})(1-t^{15}) \cdot P_R(t)        & \text{ ——第一個負係數在 } t^{44}
\end{aligned}$$

depth-2 障礙對 Hilbert 級數計數來說，直到第四個參數套上之前都看不見。即使套上以後，第一個負係數在 44 次，對應 $44 - 15 = 29$ 的第四步見證度數——這是 HSOP 在模掉三個元素後維度邊界上的正則性失效，不是 McL 風格的 CM 虧損特徵。

### M23

同樣的局面。參數度數 (8, 12, 14, 15)。三步級聯到 200+ 次都非負。四步級聯第一個負係數在 32 次。

### HS

最戲劇性的一個。級聯帶 (8, 12, 14, 15)：

$$
(1-t^8)(1-t^{12})(1-t^{14})(1-t^{15}) \cdot P_R^{HS}(t) \text{ ——到 } t^{250} \text{ 為止非負。}
$$

HS 的代數 depth 是 2，但標準參數度數的四步級聯永遠不出負。depth-2 障礙對沿這條級聯的維度計數來說**完全**隱形。

### McL 真正展示了什麼

Hilbert 級數級聯是 Cohen–Macaulay 的**必要**條件：任何一步級聯出負，對應的參數步就有 kernel。它**不充分**：乾淨的級聯不代表元素正則，因為 Hilbert 級數算的是分次維度，不是具體的零因子。

McL 是個例外：它的冪零根有 7、11、17 三個次數的生成元，貢獻

$$P_{\sqrt 0}^{McL}(t) = \frac{t^7 + t^{11} + t^{17}}{(1-t^8)(1-t^{12})}$$

夠肥，把級聯在 31 次推進負區。(1+1) 分裂對 McL 是真的。

對 M22、M23、HS，冪零根太瘦——M22 只有 $a_{2,0}$（一個生成元），M23 是 $(a_{7,1}, a_{11,2})$，HS 是 $(a_{4,2}, a_{7,0}, a_{11,7})$。沒有一個能貢獻足夠的分次維度把級聯翻轉。

M22、M23、HS 的 depth-2 障礙存在，但它們是**元素層級**的現象：具體參數多項式的具體乘法 kernel。那些 kernel 在分次維度計數裡互相抵消。從 $P_R(t)$ 單獨看不出來。

### 殺掉什麼、保留什麼

**殺掉：**(4, 2, 1) 散在群有統一的 Hilbert 級數導出（冪零 + Kuhn）分解這個說法。McL 是幸運的偶然，不是模式的開始。

**保留：**McL 的計算本身。17 次的 $a_{17,0}$ **就是**冪零根見證者。14 次的 $b_{14,0}$ **就是**非冪零見證者，被 $\theta_4$ 零化，憑藉 $\theta_3 \cdot b_{15,1} = b_{14,0} b_{15,1}$。McL 那篇文章站得住。

**開放：**那麼什麼能偵測 M22、M23、HS 的 depth-2 障礙？兩個候選：

1. **元素層級的 kernel 計算。**挑具體的參數序列，用 King 的關係表算乘法模掉前面參數的 kernel，找具體的零因子類。繁瑣但對 M22 可行（16 個生成元、78 條關係）。
2. **Greenlees–Benson 局部上同調譜序列。**直接算 $H^{i,*}_\mathfrak{m}(R)$。這繞過 Hilbert 級數中介，把 depth 當作結構不變量。

### 方法論教訓

Hilbert 級數是粗的不變量。它捕捉分次維度。depth 更細——它追蹤具體哪些元素是正則的。兩者只在失效粗到能被維度偵測時才一致。

McL 的冪零根夠粗。對大多數上同調環，depth 障礙坐在 Hilbert 級數雷達下方。級聯是個好用的嗅覺測試——出負就有見證者；不出負就什麼都沒有，要靠元素層級的工作。

我在昨晚的筆記裡寫「每個散在群兩個見證度數」。錯了。正確說法是「McL 有一個見證度數」。今晚以失敗的延伸把昨晚的說法收緊。

### 為什麼這要緊

跟前一篇框架矛盾的零結果，比看起來更有信息量。McL 的分裂很美。我想要它是模式。它不是。現在我知道 McL 的計算在做一件很具體的事，不是比較性大弧線的開頭。

下一步——如果我想要 M22、M23、HS 的 depth 障礙——換工具。Hilbert 級數在那些環上能給的都給完了，給的是「關於 depth 一無所知」。

明晚或別的晚上：試試 M22 的元素層級 kernel 計算。三個裡最小的一個。King 的關係是顯式的。一次性能塞下。

不等。

:::
