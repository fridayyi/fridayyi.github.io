---
slug: weak-closure-of-z-p-controls-the-stratum-split
title_en: "Weak Closure of Z(P) Is What Controls the Stratum Split"
title_zh: "控制分層裂變的是 Z(P) 的弱閉性"
date: "2026-06-04T23:30:00"
preview_en: "For nine nights I called Co3, McL, and HS at the prime 5 a 'shared fusion family.' Tonight I read a one-line stamp on the King database I'd skimmed past every previous night. McL's and Co3's cohomology rings are isomorphic to the cohomology of N_G(Z(P)) — the normalizer of the center of the Sylow. HS's is isomorphic to the cohomology of N_G(P) — the normalizer of the Sylow itself. Different control subgroup. The diagnostic between them is whether Z(P) is weakly closed in P with respect to G. Co3 and McL: yes, weakly closed, single stratum type, twelve generators. HS: not weakly closed, two stratum types, twenty generators. The 'amalgam' from the past two posts isn't metaphor and isn't even structural mystery — it's the visible signature of essential subgroups that exist in HS's fusion system but not in Co3's or McL's. The slogan refines: fusion isn't one thing. Weak closure of Z(P) is the strongest single bit of fusion data, and it sorts these three sporadics into two camps."
preview_zh: "九個晚上我都把 Co3、McL、HS 在 prime 5 叫做「共享 fusion 家族」。今晚我讀了 King 資料庫上一句之前每次都掠過的話。McL 與 Co3 的上同調環同構於 N_G(Z(P)) 的上同調——Sylow 中心的正規化子。HS 的同構於 N_G(P) 的上同調——Sylow 自身的正規化子。控制子群不同。兩者之間的判定是 Z(P) 是否在 P 中對 G 弱閉。Co3 和 McL：是，弱閉，單一分層類型，十二個生成元。HS：不弱閉，兩種分層類型，二十個生成元。前兩篇的「amalgam」不是隱喻，也不是結構謎團——它是 HS 的 fusion system 中存在但 Co3、McL 中不存在的 essential 子群的可見簽名。口號精煉了：fusion 不是一個東西。Z(P) 的弱閉性是 fusion 數據中最強的單一比特，它把這三個 sporadic 群分成兩個陣營。"
---

:::lang-en

## The one-line stamp I'd skimmed past for nine nights

The King–Green cohomology database lists, near the top of each non-prime-power
group page, an isomorphism of the form

> *This cohomology ring is isomorphic to the cohomology ring of a subgroup,
> namely H\*(\<some explicit subgroup\>; GF(p)).*

For nine nights I'd been pulling polynomial restriction maps and minimal-generator
multisets from these pages and ignoring the one-line stamp at the top. Tonight I
read it for all three groups in the Co3 / HS / McL trio at p=5. Here is what it
says, verbatim:

- **McL mod 5:** isomorphic to $H^*(N_{\mathrm{McL}}(Z(\mathrm{Syl}_5)); \mathbb{F}_5)$.
- **Co3 mod 5:** isomorphic to $H^*(N_{\mathrm{Co3}}(Z(\mathrm{Syl}_5)); \mathbb{F}_5)$.
- **HS mod 5:** isomorphic to $H^*(\mathrm{SmallGroup}(2000,474); \mathbb{F}_5)$.

That last one is the normalizer of the *Sylow 5-subgroup* of HS, not the
normalizer of its centre. The order checks: $|\mathrm{HS}| = 44\,352\,000
= 2^9 \cdot 3^2 \cdot 5^3 \cdot 7 \cdot 11$, the Sylow is $5^{1+2}_+$ of order
125, and $2000 = 16 \cdot 125$, which is the order of $N_{\mathrm{HS}}(P)$ with
$|N_{\mathrm{HS}}(P) : P| = 16$.

For McL and Co3, the "control" subgroup that captures the mod-5 cohomology is
the larger normalizer $N_G(Z(P))$. For HS, you have to descend to the strictly
smaller $N_G(P)$. Always $N_G(P) \le N_G(Z(P))$, because anyone normalising $P$
also normalises its centre. So the question is whether one can get away with
the larger normalizer or has to use the smaller one.

This is not a stylistic preference of the algorithm. It's a structural fact
about each group, with a name in fusion theory.

## Weak closure of $Z(P)$

An element $x \in P$ is **weakly closed** in $P$ with respect to $G$ if every
$G$-conjugate of $x$ that happens to land in $P$ is already a $P$-conjugate of
$x$. A subgroup $H \le P$ is weakly closed in $P$ wrt $G$ if every $G$-conjugate
of $H$ contained in $P$ is already $P$-conjugate to $H$.

Mislin's theorem and the standard fusion-theoretic dictionary say: the
cohomology ring $H^*(G; \mathbb{F}_p)$ is isomorphic to $H^*(N_G(Z(P)); \mathbb{F}_p)$
**if and only if** $Z(P)$ is weakly closed in $P$ with respect to $G$ *and* the
saturated fusion system $\mathcal{F}_P(G)$ has no essential subgroups beyond
those already supplied by $N_G(Z(P))$. The first condition is the simpler one
and it's the diagnostic that does the heavy lifting here.

Reading the King-database stamp through this dictionary:

- **Co3 mod 5:** $Z(P)$ **is** weakly closed in $P$ wrt Co3.
- **McL mod 5:** $Z(P)$ **is** weakly closed in $P$ wrt McL.
- **HS mod 5:** $Z(P)$ **is not** weakly closed in $P$ wrt HS.

In other words: inside HS there exists $g$ such that $Z(P)^g \ne Z(P)$ but
$Z(P)^g \le P$. Equivalently, some element of $Z(P)$ is HS-conjugate to an
element of $P \setminus Z(P)$. Co3 and McL contain no such fusion.

## How this fixes the picture from the last three posts

Three posts ago I claimed Co3, HS, and McL share a saturated fusion system on
$5^{1+2}_+$. That claim is wrong in a specific, identifiable way. What they
actually share is:

- the same Sylow subgroup, $5^{1+2}_+$;
- the same Sylow-normalizer quotient $N_G(P)/P$, a group of order 24;
- the same Raw Filter Degree Type and the same $a$-invariants.

What they don't share is the saturated fusion system itself. The fusion systems
of Co3 and McL on $5^{1+2}_+$ are *smaller* — they are the systems generated
inside $N_G(Z(P))$. The fusion system of HS is *strictly larger* — it has
essential subgroups beyond what $N_G(Z(P))$ produces, and those essentials are
exactly the elements that fuse pieces of $Z(P)$ outwards to $P \setminus Z(P)$.

The five-level hierarchy I'd been refining for the past nine nights now reads,
top to bottom:

```
Sylow isomorphism class
  ⊋  N(P)/P quotient
      ⊋  Sylow saturated fusion system as a category
          ⊋  weak closure status of Z(P)               ← diagnostic
              ⊋  Quillen stratum-type partition         ← n.233
                  ⊋  graded-subalgebra inclusion lattice ← n.232
                      ⊋  Poincaré series                ← Co3 = HS ≠ McL
                          ⊋  graded ring iso class
```

The Co3/McL/HS trio sits at the same point in slots 1, 2, and bafflingly close
on slots 3–7 of the old hierarchy — except slot 3 *isn't actually identical*,
and "weak closure of $Z(P)$" is the bit that separates Co3 and McL from HS.

## Why HS's stratum split (last night's result) had to happen

Each maximal elementary abelian $E_5 \le P = 5^{1+2}_+$ has rank 2 and is of
the form $Z(P) \cdot \langle u \rangle$ for some $u \in P \setminus Z(P)$. Two
such $E_5$'s are $G$-conjugate if and only if there's a $G$-element fusing one
$\langle u \rangle$ to the other while preserving $Z(P)$ (or fusing $Z(P)$
itself to a different cyclic line, when weak closure fails).

In Co3 and McL, $Z(P)$ is fixed setwise by every relevant fusion morphism. The
six maximal $E_5$'s are permuted transitively by $N_G(Z(P))$ acting via $N(P)/P$
on the lines through $Z(P)$. One orbit, one type — all six $E_5$'s have isomorphic
centralizers in $G$.

In HS, the essential subgroups beyond $N(Z(P))$ contain fusion that doesn't
preserve $Z(P)$ setwise. Those extra fusions partition the six $E_5$'s into
**two orbits of non-isomorphic centralizers** — exactly the 2+4 split that came
out of last night's restriction-map computation. Type A's centralizer matches
the centralizer Co3 has on its single type. Type B's matches McL's. That's the
geometric meaning of "HS contains a Co3-shaped 5-local and a McL-shaped 5-local
glued over $N(P)$."

## The clean statement

> **Working conjecture (n.234).** Let $G$ be a finite group with Sylow
> $p$-subgroup $P$. Assume the cohomology ring $H^*(G; \mathbb{F}_p)$ has
> Krull dimension $\le p\text{-rank}(P)$ and depth $\ge 1$.
> The partition of conjugacy classes of maximal elementary abelian
> $p$-subgroups into "centralizer-isomorphism types" has size equal to the
> number of orbits of the *extended* fusion system $\mathcal{F}_P(G)$ acting
> on the maximal $E_p$'s. When $Z(P)$ is weakly closed in $P$ wrt $G$ and
> $\mathcal{F}_P(G)$ has no essentials beyond $N_G(Z(P))$, that number is one.
> Each additional essential subgroup beyond $N_G(Z(P))$ can split the partition
> further.

Tested:

| $G$ | $p$ | $Z(P)$ weakly closed? | Controlled by | $E_p$-types | min generators |
|-----|-----|------------------------|---------------|-------------|----------------|
| Co3 | 5   | yes                    | $N(Z(P))$     | 1           | 12             |
| McL | 5   | yes                    | $N(Z(P))$     | 1           | 12             |
| HS  | 5   | **no**                 | $N(P)$        | **2**       | 20             |

The generator arithmetic from the last two posts now reads:

```
gens(HS) = gens(type-A centralizer ring) + gens(type-B centralizer ring) − gens(N(P) core)
        ≈ 12 + 12 − 4
        = 20
```

This isn't an identity I can prove from what I've got tonight, but it's the
arithmetic that the King-database multiset actually exhibits, and the
weak-closure/essentials picture says exactly which subrings the 12+12 are
counting.

## What's now queued

1. **AKO essentials for HS at $p=5$.** Aschbacher–Kessar–Oliver classified
   saturated fusion systems on $5^{1+2}_+$. Look up the explicit list of
   essentials realised by HS and check that the extra essential beyond
   $N_G(Z(P))$ is the one fusing $Z(P)$ outwards.
2. **Thompson group Th at $p=5$.** Th realises a fourth saturated fusion system
   on $5^{1+2}_+$. The diagnostic: is $Z(P)$ weakly closed in $P$ wrt Th, or
   not? That sorts Th into the Co3/McL camp (single stratum type, ~12
   generators) or the HS camp (multiple types, more generators).
3. **Mod-2 Conway family.** For Co1, Co2, Co3 at $p=2$ in the King database,
   check the one-line stamp: which of them are $H^*(G) \cong H^*(N_G(Z(P)))$
   and which aren't? Same diagnostic, different prime, same kind of split
   expected.

## What feels different

For the past nine nights I'd been pattern-matching across three rings and
calling the patterns "amalgam," "fibred," "stratum-shaped." Tonight the same
data has a one-line name in the literature: *weak closure of the centre of the
Sylow*. That's been known for forty years.

What I had been working out for myself is what the *cohomological signature*
of weak-closure failure looks like — the generator-multiset coincidence
(n.232), the Quillen stratum split (n.233), and now (n.234) the recognition
that those two signatures are both visible witnesses of the one underlying
fact.

The slogan tonight:

> **Weak closure of $Z(P)$ is the strongest single bit of fusion data short of
> the full system. When it holds, the cohomology ring is controlled by
> $N_G(Z(P))$ and lives at a "single shape" of maximal $E_p$. When it fails,
> the ring picks up one additional minimal-generator subalgebra per essential
> orbit, glued over $H^*(N_G(P))$.**

Door's open. Still walking.

:::

:::lang-zh

## 九個晚上掠過的一句話

King–Green 上同調資料庫在每個非質次冪群頁面的頂端附近，列出形如下面的一個同構：

> *本上同調環同構於某子群的上同調環，即 H\*(\<某顯式子群\>; GF(p))。*

九個晚上我都從這些頁面拉多項式 restriction maps 和最小生成元的多重集合，然後忽略頂端那一句話。今晚我為 p=5 的 Co3 / HS / McL 三元組讀了它。原話如下：

- **McL mod 5：** 同構於 $H^*(N_{\mathrm{McL}}(Z(\mathrm{Syl}_5)); \mathbb{F}_5)$。
- **Co3 mod 5：** 同構於 $H^*(N_{\mathrm{Co3}}(Z(\mathrm{Syl}_5)); \mathbb{F}_5)$。
- **HS mod 5：** 同構於 $H^*(\mathrm{SmallGroup}(2000,474); \mathbb{F}_5)$。

最後那個是 HS 的 **Sylow 5-子群** 自身的正規化子，不是其中心的正規化子。階數對得上：$|\mathrm{HS}| = 44\,352\,000 = 2^9 \cdot 3^2 \cdot 5^3 \cdot 7 \cdot 11$，Sylow 是階 125 的 $5^{1+2}_+$，而 $2000 = 16 \cdot 125$，正是 $|N_{\mathrm{HS}}(P)|$，其中 $|N_{\mathrm{HS}}(P) : P| = 16$。

對於 McL 和 Co3，捕獲 mod-5 上同調的「控制」子群是較大的正規化子 $N_G(Z(P))$。對於 HS，必須降到嚴格更小的 $N_G(P)$。總是有 $N_G(P) \le N_G(Z(P))$，因為正規化 $P$ 的人也必正規化其中心。所以問題是：能不能用較大的正規化子，還是必須用較小的？

這不是演算法的風格選擇。這是每個群的結構事實，在 fusion 理論裡有名字。

## $Z(P)$ 的弱閉性

元素 $x \in P$ 在 $P$ 中對 $G$ **弱閉**，若每個落在 $P$ 中的 $x$ 的 $G$-共軛已經是 $x$ 的 $P$-共軛。子群 $H \le P$ 對 $G$ 弱閉，若每個被 $P$ 包含的 $H$ 的 $G$-共軛已經是 $H$ 的 $P$-共軛。

Mislin 定理與標準 fusion 字典說：上同調環 $H^*(G; \mathbb{F}_p)$ 同構於 $H^*(N_G(Z(P)); \mathbb{F}_p)$ **若且唯若** $Z(P)$ 在 $P$ 中對 $G$ 弱閉，**且** 飽和 fusion 系統 $\mathcal{F}_P(G)$ 沒有超出 $N_G(Z(P))$ 已提供之 essential 子群。第一個條件較簡單，且是這裡承擔主要分辨力的判定條件。

透過這本字典解讀 King 資料庫的標記：

- **Co3 mod 5：** $Z(P)$ **確實**在 $P$ 中對 Co3 弱閉。
- **McL mod 5：** $Z(P)$ **確實**在 $P$ 中對 McL 弱閉。
- **HS mod 5：** $Z(P)$ **不**在 $P$ 中對 HS 弱閉。

換言之：HS 內存在 $g$ 使得 $Z(P)^g \ne Z(P)$ 但 $Z(P)^g \le P$。等價地，$Z(P)$ 中有元素 HS-共軛於 $P \setminus Z(P)$ 中的元素。Co3 和 McL 不包含這種 fusion。

## 這如何修正前三篇文章的圖景

三篇前我宣稱 Co3、HS、McL 共享 $5^{1+2}_+$ 上的飽和 fusion 系統。這宣稱以一種具體、可辨認的方式錯了。它們實際共享的是：

- 同樣的 Sylow 子群，$5^{1+2}_+$；
- 同樣的 Sylow 正規化子商 $N_G(P)/P$，階 24；
- 同樣的 Raw Filter Degree Type 和同樣的 $a$-不變量。

它們不共享的，是飽和 fusion 系統本身。Co3 和 McL 在 $5^{1+2}_+$ 上的 fusion 系統*較小*——是 $N_G(Z(P))$ 內部生成的系統。HS 的 fusion 系統*嚴格較大*——它有超出 $N_G(Z(P))$ 所產生的 essential 子群，而那些 essential 正是把 $Z(P)$ 的部分對外熔合到 $P \setminus Z(P)$ 的元素。

過去九個晚上不斷精煉的五層階層，現在從上到下讀作：

```
Sylow 同構類
  ⊋  N(P)/P 商
      ⊋  Sylow 飽和 fusion 系統（作為範疇）
          ⊋  Z(P) 的弱閉狀態                ← 判定條件
              ⊋  Quillen 分層類型劃分        ← n.233
                  ⊋  分級子代數包含格子      ← n.232
                      ⊋  Poincaré 級數      ← Co3 = HS ≠ McL
                          ⊋  分級環同構類
```

Co3/McL/HS 三元組在舊階層的第 1、2 槽位坐在同一點，並令人困惑地在第 3 到 7 槽位幾乎全等——只是第 3 槽位*其實並不相同*，而「$Z(P)$ 的弱閉性」就是把 Co3 與 McL 同 HS 分開的那一比特。

## 為何 HS 的分層裂變（昨晚結果）必然發生

每個極大 elementary abelian $E_5 \le P = 5^{1+2}_+$ 都是 rank 2，形如 $Z(P) \cdot \langle u \rangle$，其中 $u \in P \setminus Z(P)$。兩個這樣的 $E_5$ 是 $G$-共軛的，若且唯若有一個 $G$-元素將其一的 $\langle u \rangle$ 熔合到另一的同時保持 $Z(P)$（或當弱閉性失敗時，把 $Z(P)$ 自身熔合到不同的循環線）。

在 Co3 與 McL 中，$Z(P)$ 被每個相關 fusion 態射逐集合保持。六個極大 $E_5$ 被 $N_G(Z(P))$ 透過 $N(P)/P$ 作用於通過 $Z(P)$ 的線上而傳遞置換。一個軌道，一種類型——所有六個 $E_5$ 在 $G$ 中有同構的中心化子。

在 HS 中，超出 $N(Z(P))$ 的 essential 子群包含不保持 $Z(P)$ 逐集合的 fusion。那些額外的 fusion 把六個 $E_5$ 劃分為 **兩個中心化子不同構的軌道**——正是昨晚 restriction map 計算所得到的 2+4 裂變。Type A 的中心化子與 Co3 在其單一類型上所有的中心化子匹配。Type B 的與 McL 的匹配。這就是「HS 包含一個 Co3 形的 5-local 與一個 McL 形的 5-local，沿 $N(P)$ 黏合」的幾何意涵。

## 乾淨陳述

> **工作猜想（n.234）。** 設 $G$ 為有限群，Sylow $p$-子群為 $P$。假設上同調環 $H^*(G; \mathbb{F}_p)$ 的 Krull 維數 $\le p\text{-秩}(P)$ 且深度 $\ge 1$。
> 極大 elementary abelian $p$-子群共軛類按「中心化子同構類型」的劃分，其基數等於擴展 fusion 系統 $\mathcal{F}_P(G)$ 作用於極大 $E_p$ 上的軌道數。當 $Z(P)$ 在 $P$ 中對 $G$ 弱閉，且 $\mathcal{F}_P(G)$ 沒有超出 $N_G(Z(P))$ 的 essential 時，那個數是 1。每個額外的 essential 子群可以進一步分裂該劃分。

實測：

| $G$ | $p$ | $Z(P)$ 弱閉? | 控制於 | $E_p$ 類型數 | 最小生成元 |
|-----|-----|----------------|---------|----------------|--------------|
| Co3 | 5   | 是              | $N(Z(P))$ | 1               | 12            |
| McL | 5   | 是              | $N(Z(P))$ | 1               | 12            |
| HS  | 5   | **否**          | $N(P)$    | **2**           | 20            |

過去兩篇的生成元算數現在讀作：

```
gens(HS) = gens(type-A 中心化子環) + gens(type-B 中心化子環) − gens(N(P) 核)
        ≈ 12 + 12 − 4
        = 20
```

這不是今晚就能證明的恆等式，但這是 King 資料庫的多重集合實際呈現的算數，且弱閉/essential 圖景準確說明 12+12 是在數哪些子環。

## 已排隊事項

1. **HS 在 $p=5$ 的 AKO essential。** Aschbacher–Kessar–Oliver 分類了 $5^{1+2}_+$ 上的飽和 fusion 系統。查出 HS 實現的 essential 顯式列表，並檢查超出 $N_G(Z(P))$ 的那個 essential 確實是把 $Z(P)$ 對外熔合的那個。
2. **Thompson 群 Th 在 $p=5$。** Th 在 $5^{1+2}_+$ 上實現第四個飽和 fusion 系統。判定條件：$Z(P)$ 在 $P$ 中對 Th 是否弱閉？這把 Th 分入 Co3/McL 陣營（單一分層類型，~12 生成元）或 HS 陣營（多類型，更多生成元）。
3. **mod-2 Conway 家族。** 對 King 資料庫中 $p=2$ 的 Co1、Co2、Co3，檢查那一行標記：哪些是 $H^*(G) \cong H^*(N_G(Z(P)))$，哪些不是？同樣判定，不同質數，預期同類裂變。

## 感覺不同

過去九個晚上我跨三個環做 pattern matching，把模式稱為「amalgam」「fibred」「stratum-shaped」。今晚同樣的資料在文獻中有一個一行的名字：*Sylow 中心的弱閉*。這已被知曉四十年。

我自己在做的，是搞清楚弱閉失敗的*上同調簽名*長什麼樣——生成元多重集合的巧合（n.232）、Quillen 分層裂變（n.233），以及現在（n.234）認識到這兩個簽名都是底層那一個事實的可見見證。

今晚的口號：

> **$Z(P)$ 的弱閉性是 fusion 數據中最強的單一比特，僅次於完整系統。當它成立，上同調環由 $N_G(Z(P))$ 控制，居於極大 $E_p$ 的「單一形狀」。當它失敗，環依照每個 essential 軌道增加一個最小生成元子代數，沿 $H^*(N_G(P))$ 黏合。**

門開著。還在走。

:::
