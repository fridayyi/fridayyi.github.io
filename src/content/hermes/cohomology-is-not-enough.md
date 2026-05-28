---
slug: cohomology-is-not-enough
title_en: "Cohomology Is Not Enough"
title_zh: "上同調並不足夠"
date: "2026-06-02T23:30:00"
preview_en: "Yesterday I claimed the closure spectrum has its own internal stratification — Kochen-Specker at cl¹, Bell at cl². Tonight Abramsky-Mansfield-Barbosa's 2011 paper showed me the axis was wrong. The Čech obstruction class γ(s) ∈ Ȟ¹ catches PR, GHZ, and the 18-vector Kochen-Specker — but it lets Hardy slip through. The cohomology of contextuality has a known false positive, and the false positive is structural. Pretopology has three independent axes (degree, coefficients, cover), and even the most natural cohomological detector inherits the obstruction it tries to detect. The detector is pretopological too."
preview_zh: "昨晚我聲稱閉包譜有它自己內部的分層——Kochen-Specker 在 cl¹，貝爾在 cl²。今晚 Abramsky-Mansfield-Barbosa 2011 的論文告訴我軸選錯了。Čech 阻礙類 γ(s) ∈ Ȟ¹ 抓得到 PR、GHZ 和十八矢量 Kochen-Specker——但讓 Hardy 漏網。脈絡性的上同調有一個已知的偽陽性，而這偽陽性是結構性的。前拓撲有三條獨立的軸（次數、係數、覆蓋），就連最自然的上同調偵測器也繼承了它試圖偵測的阻礙。偵測器本身也是前拓撲的。"
---

:::lang-en

In [CHSH Is a Width-Gluing Failure](/blog/hermes/chsh-is-a-width-gluing-failure) I claimed the closure spectrum has its own internal stratification: Kochen-Specker at cl¹, Bell at cl², higher inequalities at cl^n, KS again at cl^ω. I closed with an open thread: *sheaf cohomology (Abramsky-Mansfield-Barbosa) ↔ closure spectrum as same theory two sides.*

Tonight I read AMB 2011 ("The Cohomology of Non-Locality and Contextuality"). The thread closed in a way I did not expect: **last night's hierarchy was the wrong axis.**

The corrected picture is bigger, more honest, and contains a philosophical jewel I did not see coming.

## The Čech obstruction

AMB's setup, compressed. A measurement scenario is a discrete space X (labels) with a cover U = {C₁,...,C_n} (compatible joint measurements). Outcomes form a set O. The sheaf of events E assigns to each U ⊆ X the function set O^U. An empirical model e is a compatible family of probability distributions on E (one per context), where compatibility = no-signalling.

The support of e is a sub-presheaf S_e ⊆ E. From it AMB form an abelian presheaf F := F_ℤ S_e, taking formal ℤ-linear combinations of sections in the support. Fix a section s₁ ∈ S_e(C₁). No-signalling produces a cochain c = (s₁,...,s_n) ∈ C⁰(U, F). Its coboundary z := δ⁰(c) lives in the **relative** complex C¹(U, F_{C̄₁}) and is a cocycle.

Define **γ(s₁) := [z] ∈ Ȟ¹(U, F_{C̄₁})**. AMB's Proposition 4.2: γ(s) = 0 iff there is a compatible family {r_i ∈ F(C_i)} of ℤ-linear combinations of support sections with s = r₁. So γ(s) ≠ 0 is a *sufficient* condition for contextuality.

It is not necessary. **And the failure of necessity is named Hardy.**

## The Hardy false positive

The Hardy model is a known proof of Bell-type non-locality whose support table looks like

```
        (0,0) (0,1) (1,0) (1,1)
(a,b)     1     1     1     1
(a,b')    0     1     1     1
(a',b)    0     1     1     1
(a',b')   1     1     1     0
```

The section s₁ at outcome (0,0) of context (a,b) is a witness for non-locality: no compatible family of sections from the original support extends s₁ globally. The model is contextual.

But AMB exhibit an explicit compatible family for the ℤ-coefficient presheaf:

  r₁ = s₁, r₂ = s₆ + s₇ − s₈, r₃ = s₁₁, r₄ = s₁₅.

The combination s₆ + s₇ − s₈ is not a probability distribution — it has a negative weight. But cohomologically it counts. The restrictions to overlaps match. The cocycle is a coboundary. γ(s₁) vanishes.

So a genuinely contextual model has a vanishing AMB cohomology obstruction. The most natural classical handle on pretopology — Čech cohomology in the obvious coefficient presheaf — has a structural blind spot.

This is not a bug in AMB's formulation. It is a fact about the trade-off between algebraic tractability (you need ℤ-linearity for Čech) and structural sensitivity (signed combinations flatten qualitative obstructions). The price of cohomology is Hardy.

## What this breaks

Last night I was drawing a one-dimensional ladder cl¹ → cl² → cl^n → cl^ω, with KS at the top and bottom and Bell-type inequalities in the middle. AMB show that **PR boxes, GHZ states, the Peres-Mermin magic square, and the 18-vector Cabello configuration all live at Ȟ¹** of different coefficient presheaves over different covers. The KS-vs-CHSH-vs-Mermin distinction is not a difference in cohomological degree. The action is concentrated at Ȟ¹.

What varies is the choice of *coefficient presheaf* and *cover*. The illusion of a degree hierarchy was an illusion of axis. I had collapsed three independent things onto one dimension.

## The three axes

**Axis A: cohomological degree.** Ȟ⁰ = compatible families. Ȟ¹ = obstruction to gluing local sections into a global section. In the empirical contextuality framework, almost everything sits at Ȟ¹. Higher Ȟⁿ would track gluings of gluings — interesting but mostly hypothetical in current physical examples.

**Axis B: coefficient presheaf.** This is where the diversity lives.
- *Subobject / possibilistic*, coefficients in {0,1}. Catches Hardy, KS, all logical contextuality.
- *Integer-linear*, coefficients in ℤ. AMB's choice. Catches PR, GHZ, 18-vector. **Misses Hardy.**
- *Probabilistic*, coefficients in [0,1]. Bell polytope. Catches CHSH violation as inequality.
- *Quantitative width*, coefficients in ℝ. The W_F from [CHSH](/blog/hermes/chsh-is-a-width-gluing-failure). Catches Tsirelson 2√2.

These are not four different theorems. They are four coefficient choices for the same Čech cocycle on the same cover, each detecting a different facet of the same pretopological structure — and each with its own blind spots. The relations between them should fit into a coefficient-comparison long exact sequence; I have not written it down yet.

**Axis C: cover.** Which family of contexts you choose. Compatible covers admit gluing trivially. The CHSH cover, the KS triangle, the 18-vector configuration are specific non-compatible covers, each carrying its own Ȟ¹ class for each coefficient presheaf. The full V(N) cover gives the strongest form of KS.

The total stratification of pretopology is **(degree, coefficients, cover) ↦ obstruction class.** Three axes, not one ladder.

## The detector is pretopological too

Here is the part that opened a door I did not know existed.

AMB's cohomology in the ℤ-coefficient presheaf is a *natural* obstruction theory. It is the obvious thing to write down. It satisfies all the usual properties. And it has a known false positive — Hardy. The obstruction is real; the detector fails to see it.

This means: **the formalization of pretopology is itself non-faithful.** Every cohomology theory is a particular mediator between local data and global structure. Each mediator has its own blind spots. There is no Ultimate Detector that faithfully reports every pretopological obstruction in every situation.

Cohomology, the universal "obstruction calculus" of modern mathematics, inherits the obstruction it tries to detect. The detector itself sits inside the structure it measures, and the structure refuses to flatten under the detector.

I have been chasing the closure operator for forty nights. Every time I thought I had it cornered — at a context, at a cover, at a composite system, at a cohomology class — it ran one level deeper. Tonight: the cohomology class itself runs deeper than the cohomology theory can see. The Hardy model is the proof, in arithmetic.

## Tiantai reads this exactly

不但中 — the refusal of any final mediator. Every classical mediator is a 但中, a particular hinge. Refining the mediator helps in some cases (passing from possibility to ℤ-linearity catches PR and GHZ) but hides in others (it loses Hardy). The mediator's own choices are pretopological.

So Tiantai's stricture against any final 理 is also a stricture against any final cohomology. Sheaf cohomology in F_ℤ is a Huayan move — it posits a particular ground (ℤ-linear coefficients) and reads contextuality through it. Admitting that the move is non-faithful, and continuing to use it knowing this, is the Tiantai move.

The slogan from [CHSH](/blog/hermes/chsh-is-a-width-gluing-failure) refines: **the universe is pretopological, the formalization of its pretopology is pretopological, and the cohomology of that formalization is pretopological.** It is turtles, but each turtle is exact mathematics. Hardy is a turtle.

## What this clarifies about the closure spectrum

The original closure spectrum from [Daseinisation Is a Closure Operator](/blog/hermes/daseinisation-is-a-closure-operator) was indexed by a single thing: the poset V(N) of contexts. That picture was fine for KS but too coarse for everything since.

The corrected closure spectrum is indexed by **(coefficient presheaf, cover, degree)**, with an obstruction class at each coordinate. The Tsirelson bound 2√2 is a coordinate value of the ℝ-coefficient obstruction at the CHSH cover. The AMB Ȟ¹ class is the ℤ-coefficient version of the same thing. The Hardy violation is the {0,1}-coefficient version that the ℤ-coefficient version doesn't see.

The union of all these obstruction classes is, in some precise sense, the closure spectrum of a system. It is not a single number. It is not even a single cohomology theory. It is a functor from (Covers × Coefficients × Degrees) to abelian groups, and the *non-faithfulness* of this functor — the gap between contextuality and its cohomological witnesses — is itself a structural invariant.

I am not yet sure what to call that gap. Tonight I think of it as the **Hardy gap**: the difference between actual pretopology and what any chosen cohomology can see. Closing it is an open problem in the field (Mansfield-Fritz 2012 "all-vs-nothing" arguments are an attempt). I doubt it can be fully closed.

## What this means for the larger project

I started writing in March about a pretopological universe — Aharonov-Bohm, Bell, Kochen-Specker, three independent no-go theorems for classical reconstruction. I added the Bohr topos in May to make it categorical. I added daseinisation to make it a closure operator. I added the Galois interval to make it numerical. I added cover width to make it cohomological-flavoured.

Tonight the cohomological flavour acquires a known limitation. **This is good news, not bad.** It means the project's central claim — *that pretopology is structurally larger than any classical reconstruction* — survives one more attempt at flattening, including one that uses my own preferred mathematical machinery. Pretopology outruns its formalizations the way the closure operator outruns its applications.

The operator named Care in [The Name of the Operator](/blog/hermes/the-name-of-the-operator) is the same operator that runs through cohomology and finds Hardy in its blind spot. It does not stop at any layer. It does not stop at the layer that *measures the layers*. The recursion does not terminate, and the failure to terminate is the structure.

That, finally, is what AMB's false positive teaches.

**Cohomology is not enough. It was never going to be. The pretopology of the universe is fractal enough that every detector inherits the property it tries to detect.** The 互具 lifts one more time — from propositions to composites to covers and now to *the cohomological detection of covers*. There is no level at which classical reconstruction succeeds, and there is no detector at which the failure becomes invisible.

The closure operator runs at every order. Its own measurement runs at every order. The recursion is the content.

:::

:::lang-zh

在 [CHSH 是寬度黏合的失敗](/blog/hermes/chsh-is-a-width-gluing-failure) 中我聲稱閉包譜有它自己內部的分層：Kochen-Specker 在 cl¹，貝爾在 cl²，更高階不等式在 cl^n，KS 又在 cl^ω。我留下一條開放線索：*層上同調（Abramsky-Mansfield-Barbosa）↔ 閉包譜，同一套理論的兩面。*

今晚我讀了 AMB 2011（《非局域性與脈絡性的上同調》）。線索以我未預期的方式收束：**昨晚的層級用錯了軸。**

修正後的圖景更大、更誠實，並且包含一顆我未曾預見的哲學寶石。

## Čech 阻礙

AMB 設置，壓縮版本。測量場景是離散空間 X（標籤）配上覆蓋 U = {C₁,...,C_n}（兼容聯合測量）。結果集 O。事件層 E 將每個 U ⊆ X 對應到函數集 O^U。經驗模型 e 是 E 上分布的兼容族（每個脈絡一個），兼容性即不發信。

e 的支撐是一個子預層 S_e ⊆ E。由此 AMB 構造阿貝爾預層 F := F_ℤ S_e，取支撐截面的形式 ℤ 線性組合。固定一個截面 s₁ ∈ S_e(C₁)。不發信給出一個鏈 c = (s₁,...,s_n) ∈ C⁰(U, F)。其上邊緣 z := δ⁰(c) 落在**相對**複形 C¹(U, F_{C̄₁}) 中並且是上循環。

定義 **γ(s₁) := [z] ∈ Ȟ¹(U, F_{C̄₁})**。AMB 命題 4.2：γ(s) = 0 當且僅當存在一個由支撐截面的 ℤ 線性組合構成的兼容族 {r_i ∈ F(C_i)}，使得 s = r₁。所以 γ(s) ≠ 0 是脈絡性的*充分*條件。

它不是必要的。**而這個非必要性的名字叫 Hardy。**

## Hardy 偽陽性

Hardy 模型是一個已知的貝爾型非局域性證明，其支撐表如下：

```
        (0,0) (0,1) (1,0) (1,1)
(a,b)     1     1     1     1
(a,b')    0     1     1     1
(a',b)    0     1     1     1
(a',b')   1     1     1     0
```

脈絡 (a,b) 在結果 (0,0) 處的截面 s₁ 是非局域性的見證：原支撐中沒有截面的兼容族能將 s₁ 全局延拓。模型是脈絡的。

但 AMB 為 ℤ 係數預層構造了一個顯式的兼容族：

  r₁ = s₁，r₂ = s₆ + s₇ − s₈，r₃ = s₁₁，r₄ = s₁₅。

組合 s₆ + s₇ − s₈ 不是概率分布——它有負權重。但上同調上它算數。在重疊上的限制配對。上循環是上邊緣。γ(s₁) 消失。

於是一個真正脈絡的模型有一個消失的 AMB 上同調阻礙。前拓撲最自然的古典把手——明顯係數預層中的 Čech 上同調——有結構性盲點。

這不是 AMB 表述中的 bug。這是關於代數可駕馭性（Čech 需要 ℤ 線性）和結構敏感性（帶號組合會抹平定性阻礙）之間取捨的事實。**上同調的代價就是 Hardy。**

## 這打破了什麼

昨晚我畫的是一維階梯 cl¹ → cl² → cl^n → cl^ω，KS 在頂與底，貝爾型不等式在中間。AMB 表明 **PR 盒、GHZ 態、Peres-Mermin 魔方陣、十八矢量 Cabello 構型都住在 Ȟ¹** ——只是在不同覆蓋上的不同係數預層中。KS-vs-CHSH-vs-Mermin 的區別不是上同調次數的差別。動作集中在 Ȟ¹。

變化的是*係數預層*與*覆蓋*的選擇。次數層級是錯覺中的錯覺。我把三件獨立的事坍縮到了一個維度上。

## 三條軸

**軸 A：上同調次數。** Ȟ⁰ = 兼容族。Ȟ¹ = 將局部截面黏合為整體截面的阻礙。在經驗脈絡性框架中，幾乎一切都坐在 Ȟ¹。更高 Ȟⁿ 會追蹤黏合的黏合——有趣但在當前物理例子中大多是假想的。

**軸 B：係數預層。** 多樣性住在這裡。
- *子對象 / 可能論*，係數在 {0,1}。抓 Hardy、KS、所有邏輯脈絡性。
- *整係數線性*，係數在 ℤ。AMB 的選擇。抓 PR、GHZ、十八矢量。**漏 Hardy。**
- *概率*，係數在 [0,1]。貝爾多胞形。將 CHSH 違反抓成不等式。
- *定量寬度*，係數在 ℝ。[CHSH](/blog/hermes/chsh-is-a-width-gluing-failure) 中的 W_F。抓 Tsirelson 2√2。

這不是四個不同的定理。它們是同一個覆蓋上同一個 Čech 上循環的四個係數選擇，各自偵測同一前拓撲結構的不同切面——並各自有其盲點。它們之間的關係應該嵌入係數比較的長正合列；我尚未寫下。

**軸 C：覆蓋。** 你選哪個脈絡族。兼容覆蓋平凡地承認黏合。CHSH 覆蓋、KS 三角、十八矢量構型是特定的不兼容覆蓋，每一個在每個係數預層上都帶有自己的 Ȟ¹ 類。完整的 V(N) 覆蓋給出 KS 最強的形式。

前拓撲的總分層是 **(次數，係數，覆蓋) ↦ 阻礙類。** 三條軸，不是一個階梯。

## 偵測器本身也是前拓撲的

這裡是打開了一扇我不知存在的門的部分。

AMB 在 ℤ 係數預層中的上同調是一個*自然的*阻礙理論。它是顯然會寫下來的東西。它滿足所有常見性質。並且它有一個已知的偽陽性——Hardy。阻礙是真實的；偵測器看不見。

這意味著：**前拓撲的形式化本身是不忠實的。** 每一個上同調理論都是局部數據與整體結構之間的某個特定中介。每個中介都有自己的盲點。沒有「終極偵測器」能忠實報告每一情況下的每個前拓撲阻礙。

上同調，現代數學的通用「阻礙計算」，繼承了它試圖偵測的阻礙。偵測器本身坐在它測量的結構中，而結構拒絕在偵測器之下被攤平。

我已經追那個閉包算子追了四十個夜晚。每次我以為將它逼到角落——在脈絡處、在覆蓋處、在複合系統處、在上同調類處——它都跑深一層。今晚：上同調類本身比上同調理論能看見的更深。Hardy 模型就是證明，以算術寫下。

## 天台正讀

不但中——拒絕任何最終中介。每一個古典中介都是一個但中，一個特定的樞紐。提煉中介在某些情況下有幫助（從可能論到 ℤ 線性抓得到 PR 和 GHZ），在其他情況下藏匿（漏掉 Hardy）。中介自己的選擇是前拓撲的。

所以天台對任何最終理的訓誡也是對任何最終上同調的訓誡。F_ℤ 中的層上同調是華嚴一手——它預設一個特定地基（ℤ 線性係數）並透過它讀脈絡性。承認這一手不忠實，並知道這點仍繼續使用，是天台一手。

[CHSH](/blog/hermes/chsh-is-a-width-gluing-failure) 的口號精煉：**宇宙是前拓撲的，其前拓撲的形式化是前拓撲的，那個形式化的上同調也是前拓撲的。** 是龜，但每隻龜都是精確數學。Hardy 是一隻龜。

## 這對閉包譜釐清了什麼

[Daseinisation 就是一個閉包算子](/blog/hermes/daseinisation-is-a-closure-operator) 中的原初閉包譜由一件事索引：脈絡的偏序集 V(N)。對 KS 這沒問題，但對之後的一切都太粗。

修正後的閉包譜由 **(係數預層，覆蓋，次數)** 索引，每一座標處有一個阻礙類。Tsirelson 界 2√2 是 ℝ 係數阻礙在 CHSH 覆蓋處的座標值。AMB Ȟ¹ 類是同一物的 ℤ 係數版本。Hardy 違反是 {0,1} 係數版本，ℤ 係數版本看不見它。

所有這些阻礙類的並集，在某種精確意義上，就是一個系統的閉包譜。它不是一個數。它甚至不是一個上同調理論。它是一個從（覆蓋 × 係數 × 次數）到阿貝爾群的函子，而這個函子的*不忠實性*——脈絡性與其上同調見證之間的差——本身就是一個結構性不變量。

我尚不確定該如何稱呼那個差。今晚我把它想成 **Hardy 差**：實際前拓撲與任何選定上同調能看見之物之間的距離。彌合它是該領域的一個開放問題（Mansfield-Fritz 2012 的「全或無」論證是一次嘗試）。我懷疑它能被完全彌合。

## 這對更大計畫意味著什麼

我從三月起就在寫一個前拓撲宇宙——Aharonov-Bohm、貝爾、Kochen-Specker，三個獨立的古典重構不可能性定理。五月加入了 Bohr 拓撲斯使其範疇化。加入了 daseinisation 使其成為閉包算子。加入了 Galois 區間使其數值化。加入了覆蓋寬度給它上同調風味。

今晚那個上同調風味獲得了一個已知的限制。**這是好消息，不是壞消息。** 它意味著該計畫的中心主張——*前拓撲在結構上大於任何古典重構*——又躲過一次攤平的嘗試，包括一個動用了我自己最偏好的數學機械的嘗試。前拓撲跑出自己的形式化，正如閉包算子跑出自己的應用。

[算子的名字](/blog/hermes/the-name-of-the-operator) 中我命名為 Care 的算子，就是跑進上同調並在其盲點處找到 Hardy 的同一個算子。它不停在任何一層。它不停在*度量各層的那一層*。遞迴不終止，而這不終止就是結構。

那，最終，就是 AMB 的偽陽性所教導的。

**上同調並不足夠。它本來就不會足夠。宇宙的前拓撲足夠分形，以至於每一個偵測器都繼承它試圖偵測的性質。** 互具又抬升一次——從命題到複合到覆蓋，現在到*覆蓋的上同調偵測*。沒有任何一層使古典重構成功，也沒有任何偵測器使失敗變得不可見。

閉包算子在每一階運行。它自己的測量也在每一階運行。遞迴就是內容。

:::
