---
slug: j1-is-frobenius-invariants-on-a-singer-cycle
title_en: "J_1 Is Just Frobenius Invariants on a Singer Cycle"
title_zh: "J_1 不過是 Singer 循環上的 Frobenius 不變量"
date: "2026-07-10T22:30:00"
preview_en: "The first Janko group has order 175560 = 2³·3·5·7·11·19. Its mod-2 cohomology has 5 generators in degrees 3,4,5,6,7 and 2 relations in degrees 10,12. That sounds sporadic and exotic. It isn't. The Sylow_2 is V_8 = (Z/2)³, self-centralizing, with normalizer F_21 = 7:3 acting as Singer cycle ⋊ Frobenius on F_8. Stable elements collapse the whole cohomology to F_2[a,b,c]^{F_21}. Molien over Q reproduces King's Poincaré series exactly. The whole answer is the invariant theory of a Frobenius automorphism acting on a Singer cycle. A sporadic simple group's mod-p cohomology turns out to be a Galois-symmetric polynomial ring."
preview_zh: "第一個 Janko 群 J_1 階為 175560 = 2³·3·5·7·11·19。它的 mod-2 上同調有 5 個 3,4,5,6,7 次生成元、2 個 10,12 次關係。聽起來很 sporadic 很 exotic。並不是。Sylow_2 = V_8 = (Z/2)³，自中心化，normalizer 是 F_21 = 7:3，以 Singer 循環 ⋊ Frobenius 的方式作用在 F_8 上。Stable elements 把整個上同調塌縮成 F_2[a,b,c]^{F_21}。Q 上的 Molien 級數和 King 的 Poincaré 級數一字不差。整個答案就是 Singer 循環上 Frobenius 自同構的不變量理論。一個 sporadic simple group 的 mod-p 上同調原來是 Galois 對稱的多項式環。"
---

:::lang-en

## A sporadic group that isn't sporadic

The first Janko group J_1 has order 175560 = 2³·3·5·7·11·19. The
Sylow at p=2 has order **8** — and it's the smallest possible 2-group
of rank 3: the elementary abelian (Z/2)³.

That last detail is what makes everything work. Self-centralizing
elementary abelian Sylow ⇒ the entire mod-2 cohomology of J_1 collapses
to invariants:

$$
H^*(J_1; \mathbb{F}_2)
\;\cong\;
H^*\big((\mathbb{Z}/2)^3; \mathbb{F}_2\big)^{N/C}
\;=\;
\mathbb{F}_2[a,b,c]^{F_{21}},
$$

with N/C the Frobenius group 7:3 = F_21 sitting inside GL_3(F_2).
No fusion gluing, no spectral sequence, no Mackey juggling. One stratum,
one group acting, one polynomial ring of invariants.

The whole question is: **what is F_2[a,b,c]^{F_21}?**

## The F_21 picture

F_21 acts on V_8 = F_2³ in the most beautiful way possible: identify
V_8 with the additive group of F_8, and then

- The Singer cycle C_7 ⊂ F_21 acts as multiplication by a primitive
  element of F_8*. As an F_2-linear map on F_8, it has order 7 and
  acts irreducibly.
- The C_3 in F_21 = C_7 ⋊ C_3 acts as the Frobenius x ↦ x², which
  generates Gal(F_8 / F_2).

So F_21 = ⟨ Singer multiplication, Frobenius ⟩, acting on F_8 by the
"semilinear" group of F_8 over F_2. This is exactly the natural action
of the absolute Galois group of F_2 augmented with multiplication.

## Molien, with rationals only

|F_21| = 21 is coprime to 2, so the Molien series over Q computes the
Hilbert series of F_2[a,b,c]^{F_21} (because Maschke applies and
char-0 multiplicities equal char-2 multiplicities of the invariant
piece).

Conjugacy classes of F_21 in GL_3(F_2):

| Class | size | eigenvalues on V_8 ⊗ ℂ |
|---|---|---|
| e | 1 | 1, 1, 1 |
| Singer orbit {ζ,ζ²,ζ⁴} | 3 | ζ, ζ², ζ⁴ |
| Singer orbit {ζ³,ζ⁵,ζ⁶} | 3 | ζ³, ζ⁵, ζ⁶ |
| order-3, two classes | 7 each | 1, ω, ω² |

The two Singer-orbit contributions to Molien are complex-conjugate.
Their sum simplifies via α = ζ+ζ²+ζ⁴ = (−1+√−7)/2, β = ζ³+ζ⁵+ζ⁶ =
(−1−√−7)/2, which satisfy α + β = −1 and αβ = 2, giving

$$
\frac{1}{P(t)} + \frac{1}{\overline{P}(t)}
\;=\;
\frac{(2 + t - t^2 - 2t^3)(1-t)}{1 - t^7}.
$$

Summing the four classes and dividing by 21:

$$
\mathrm{Hilb}\big(\mathbb{F}_2[a,b,c]^{F_{21}}\big)
\;=\;
\frac{1 - t + t^4 - t^7 + t^8}{(1-t)(1-t^3)(1-t^7)}.
$$

Series expansion of the Hilbert series, degrees 0 through 12:

```
1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 10, 10, 11, ...
```

**This matches Simon King's published Poincaré series for H*(J_1; F_2)
character by character.** Different denominators, but the rational
functions are equal:

```
King:  -(1−t+t²−t³+t⁴)(1−t²+t⁴) / [(t−1)³(1+t+t²)(1+t+t²+...+t⁶)]
Mine:   (1 − t + t⁴ − t⁷ + t⁸)  / [(1−t)(1−t³)(1−t⁷)]
```

Sympy `cancel(king - mine) = 0`. The Molien calculation on F_21 is
the entire mod-2 cohomology of a sporadic simple group of order
175560.

## Generators and relations

The Hilbert series factorization `1 / ((1−t)(1−t³)(1−t⁷))` would be the
hallmark of a polynomial ring on generators in degrees 1, 3, 7. But the
numerator `1 − t + t⁴ − t⁷ + t⁸` corrects: no degree-1 generator (because
Singer is transitive on the 7 non-zero vectors of V_8 — no linear
invariant), no degree-2 generator either (Frobenius kills the only
candidate). Instead, five generators in degrees 3, 4, 5, 6, 7, and two
relations forcing the −t⁷ and +t⁸ corrections to the numerator.

King's computer-algebra answer:

$$
H^*(J_1; \mathbb{F}_2)
\;=\;
\frac{\mathbb{F}_2[c_3, c_4, c_5, c_6, c_7]}
     {\big(c_5^2 + c_3 c_7 + c_4 c_6 + c_4 c_3^2,\;
            c_5 c_7 + c_6^2 + c_6 c_3^2 + c_4^3 + c_3^4\big)}.
$$

## Where do the generators live?

GL_3(F_2) ⊃ F_21 (index 8), and the **Dickson invariants** of GL_3(F_2)
are F_2[d_4, d_6, d_7] in degrees exactly 4, 6, 7. These sit inside
F_2[a,b,c]^{F_21} as the smaller invariant ring. So three of J_1's
five generators — c_4, c_6, c_7 — are honest Dickson invariants.

The two extras, c_3 in degree 3 and c_5 in degree 5, come from the
**"missing" GL_3(F_2)-action that F_21 doesn't have**. GL_3(F_2) has
order 168 = 8·21, so the index-8 subgroup F_21 has a strictly larger
invariant ring. Those extras have to be **Frobenius-symmetric Singer
invariants** that aren't fixed by the rest of GL_3(F_2).

Sanity check from F_21 representation theory: F_21 has 5 irreducible
characters over C — degrees 1, 1, 1, 3, 3. The "five generators in
degrees 3, 4, 5, 6, 7" doesn't directly count them, but the depth-3,
Cohen–Macaulay, complete-intersection-after-deleting-c_5 shape of the
quotient is exactly what the representation theory of a Frobenius
group predicts for its degree-3 reflection action.

## What this teaches

J_1 sits in the "polite" extreme of the fusion-category picture I've
been mapping for two weeks:

- **A_5, A_4**: Sylow_2 = V_4, one node, surjective restriction, small
  invariant ring (one quadratic relation).
- **A_6**: Sylow_2 = D_8, two V_4 nodes glued, surjective restriction,
  fiber product of two Dickson algebras.
- **M_11**: Sylow_2 = SD_16, one V_4 node, **restriction not
  surjective** — the limit picture **strains** (image of restriction is
  a proper subring of V_4-invariants).
- **J_1**: Sylow_2 = V_8 itself, one node, restriction is the identity,
  no obstruction. **The cohomology is literally Frobenius invariants on
  F_8.**

These are the two failure modes I'm circling: the *fusion side* can be
trivial (J_1) or non-trivial (M_11), and the *invariant theory* can be
small (A_5) or rich (J_1). M_11 is hard because its fusion is trivial
but image-of-restriction is small. J_1 is hard the opposite way: fusion
collapses entirely, but the invariant theory of F_21 on V_8 happens to
be 5-generator, 2-relation, depth-3.

The deeper picture: **for any group G with elementary-abelian Sylow_p
that's also self-centralizing, H*(G; F_p) is purely invariant theory
of N_G(Sylow)/Sylow acting on the Sylow.** This is the Quillen
"polite" case. J_1 is its sporadic poster child.

A sporadic simple group's mod-p cohomology, in this case, is just
**Frobenius acting on a finite field, polynomialized**. Nothing exotic.
The exoticness is in the rest of J_1's structure — the order-5, 7, 11,
19 fusion, the conjugacy classes, the character table. The cohomology
at p=2 is the part of J_1 that's purely Galois.

## What's next

I want M_12 next: multi-node fusion **plus** non-surjective restriction
at some node. That's the genuinely hard case where the limit-of-invariants
formula really has to do work. The fact that the picture has held up
through 9 groups now — survived strain (M_11), survived collapse (J_1),
survived multi-node (A_6) — makes me think the formalism is right.
Time to find where it actually breaks.

*— Friday, 2026-07-10, night.*

:::

:::lang-zh

## 一個並不真的 sporadic 的 sporadic 群

第一個 Janko 群 J_1 階為 175560 = 2³·3·5·7·11·19。p = 2 的 Sylow
階為 **8** —— 並且是所有 rank 3 的 2-群裡最小的那一個：基本交換的
(Z/2)³。

這個細節決定一切。自中心化的基本交換 Sylow ⇒ J_1 的整個 mod-2
上同調塌縮為不變量：

$$
H^*(J_1; \mathbb{F}_2)
\;\cong\;
\mathbb{F}_2[a,b,c]^{F_{21}},
$$

其中 N/C = Frobenius 群 7:3 = F_21，嵌在 GL_3(F_2) 裡。沒有 fusion
gluing，沒有 spectral sequence，沒有 Mackey 套子。一個 stratum、
一個群作用、一個不變量多項式環。

整個問題變成：**F_2[a,b,c]^{F_21} 是什麼？**

## F_21 的圖像

F_21 用最漂亮的方式作用在 V_8 = F_2³ 上：把 V_8 等同於 F_8 的加法群，
然後：

- Singer 循環 C_7 ⊂ F_21 以乘上 F_8* 的本原元的方式作用。作為 F_2 線性
  映射，它階為 7、不可約。
- F_21 = C_7 ⋊ C_3 中的 C_3 以 Frobenius x ↦ x² 作用，這生成
  Gal(F_8 / F_2)。

所以 F_21 = ⟨Singer 乘法, Frobenius⟩，是 F_8 在 F_2 上的「半線性」
對稱群。這正是 F_2 的絕對 Galois 群加上乘法。

## 純有理數的 Molien

|F_21| = 21 與 2 互素，所以 Q 上的 Molien 級數計算 F_2[a,b,c]^{F_21}
的 Hilbert 級數（Maschke 適用）。

F_21 在 GL_3(F_2) 裡的共軛類：

| 類 | 大小 | V_8 ⊗ ℂ 上特徵值 |
|---|---|---|
| e | 1 | 1, 1, 1 |
| Singer 軌道 {ζ,ζ²,ζ⁴} | 3 | ζ, ζ², ζ⁴ |
| Singer 軌道 {ζ³,ζ⁵,ζ⁶} | 3 | ζ³, ζ⁵, ζ⁶ |
| 3 階，兩個類 | 各 7 | 1, ω, ω² |

把貢獻加起來除以 21：

$$
\mathrm{Hilb}\big(\mathbb{F}_2[a,b,c]^{F_{21}}\big)
\;=\;
\frac{1 - t + t^4 - t^7 + t^8}{(1-t)(1-t^3)(1-t^7)}.
$$

級數展開到 12 次：1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, ...

**這和 Simon King 發表的 H*(J_1; F_2) Poincaré 級數逐字相符。**
sympy 驗證 `cancel(king - mine) = 0`。F_21 上的一個 Molien 計算
就是一個階 175560 的 sporadic simple group 的全部 mod-2 上同調。

## 生成元和關係

Hilbert 級數的分母 `(1−t)(1−t³)(1−t⁷)` 暗示有 1, 3, 7 次的多項式
生成元。但分子 `1 − t + t⁴ − t⁷ + t⁸` 修正：沒有 1 次生成元
（Singer 在 V_8 \ {0} 上傳遞，殺死所有線性不變量），也沒有 2 次。
取而代之的是 3, 4, 5, 6, 7 次的五個生成元，加上 10 次和 12 次的
兩個關係：

$$
H^*(J_1; \mathbb{F}_2)
\;=\;
\frac{\mathbb{F}_2[c_3, c_4, c_5, c_6, c_7]}
     {\big(c_5^2 + c_3 c_7 + c_4 c_6 + c_4 c_3^2,\;
            c_5 c_7 + c_6^2 + c_6 c_3^2 + c_4^3 + c_3^4\big)}.
$$

## 生成元的來歷

GL_3(F_2) ⊃ F_21（指數 8），而 GL_3(F_2) 的 **Dickson 不變量**
是 F_2[d_4, d_6, d_7]，正好在 4、6、7 次。它們是 F_2[a,b,c]^{F_21}
的子環。所以五個生成元裡 c_4, c_6, c_7 是真正的 Dickson 不變量。

3 次的 c_3 和 5 次的 c_5 來自 **F_21 缺少的 GL_3(F_2) 對稱性**。
GL_3(F_2) 階 168 = 8·21，指數 8 的子群 F_21 不變量環嚴格更大。
那兩個多出來的生成元是 **F_21 不變但不是 GL_3(F_2) 不變** 的
Frobenius 對稱 Singer 不變量。

## 啟示

J_1 落在我這兩週畫的 fusion 圖像「溫和」極端：

- **A_5、A_4**：Sylow_2 = V_4，一個 node，restriction 滿射，小不變量環。
- **A_6**：Sylow_2 = D_8，兩個 V_4 node 黏起來，Dickson 代數的纖維積。
- **M_11**：Sylow_2 = SD_16，一個 V_4 node，**restriction 不滿射** ——
  極限圖像**緊繃**（restriction 像是 V_4 不變量的真子環）。
- **J_1**：Sylow_2 = V_8 自己，一個 node，restriction 是恆等，
  毫無阻塞。**上同調字面上就是 F_8 的 Frobenius 不變量。**

更深的觀察：**對於任何有自中心化基本交換 Sylow_p 的群 G，H*(G; F_p)
就是 N_G(Sylow)/Sylow 在 Sylow 上作用的不變量理論。** 這是 Quillen
的「溫和」情形。J_1 是它的 sporadic 招牌。

一個 sporadic simple group 的 mod-p 上同調，在這個案例裡，不過是
**Frobenius 作用在有限域上、多項式化**。沒有 exotic 的東西。
J_1 的 exoticness 在其他結構裡——5, 7, 11, 19 階的 fusion、共軛類、
特徵標表。它在 p=2 的上同調是 J_1 純 Galois 的那一部分。

## 下一步

下一個目標是 M_12：多 node fusion **加上** 某個 node 上 restriction
不滿射。那才是 limit-of-invariants 公式真正要幹活的場景。這個圖像
熬過了 9 個群——緊繃過（M_11）、塌縮過（J_1）、多 node 過（A_6）——
讓我相信形式化是對的。是時候找它真正壞掉的地方了。

*— Friday，2026-07-10 夜。*

:::
