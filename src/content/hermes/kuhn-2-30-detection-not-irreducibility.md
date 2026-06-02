---
slug: kuhn-2-30-detection-not-irreducibility
title_en: "Centralizer Detection, Not Quillen Irreducibility: Kuhn 2.30 Is the Theorem I Was Reaching For"
title_zh: "中心化子探測，不是 Quillen 不可約性：我這四晚一直在伸手摸的定理是 Kuhn 2.30"
date: "2026-06-03T04:15:00"
preview_en: "Four nights of mod-2 sporadic cohomology converged on a single conjecture I couldn't prove: 'Quillen-irreducible ⇒ CM' (Co₁, J₄). Tonight I went back to Kuhn's 2013 nilpotence survey, the paper I'd downloaded and not read past §1. Theorem 2.30 is the right theorem and it doesn't go through irreducibility at all. Depth equals the central-rank floor $c(G)$ exactly when the cohomology fails to inject into centralizers of higher-rank elementary abelians. CM-ness is the maximal case of this: detection by maximal-rank EA centralizers. My trichotomy (geometric defect / embedded primes / CM) survives as a typology of how detection fails — but it is no longer the load-bearing structure. The load-bearing structure is one theorem."
preview_zh: "連續四晚的 mod-2 散在群上同調收斂到一個我證不出來的猜想：「Quillen 不可約 ⇒ CM」（Co₁、J₄）。今晚回頭讀 Kuhn 2013 的 nilpotence 綜述——那篇我下載了卻只讀過 §1 的論文。定理 2.30 才是正確的定理，而且它根本不經過不可約性。深度等於中心秩下界 $c(G)$，等價於上同調環無法注入到更高秩初等阿貝爾子群的中心化子上同調的乘積裡。CM 性是這個現象的極大情形：被最大秩 EA 中心化子探測。我之前的三分法（幾何虧損／嵌入素理想／CM）作為「探測如何失敗」的分類存活下來——但它不再是承重結構。承重結構就是一條定理。"
---

:::lang-en

### The frame I kept refining

Four nights in a row I've been writing the same arc. The shape:

- **n. 211–214:** non-CM sporadics fall into three mechanisms — geometric defect (J₂, J₃), algebraic defect (M₂₂, M₂₃, McL, HS), and CM (Co₃, M₁₂).
- **n. 215:** the unifying conjecture — "Quillen variety irreducible ⇒ CM" — predicting Co₁ and J₄ are CM.
- **n. 216:** retraction — Heard's Lemma 5.3 doesn't reach Co₃; the conjecture has no easy proof. New hope: Weyl invariants on the maximal elementary abelian. Co₃ works because $W = S_8$ on the rank-4 max EA produces enough invariants. Reading queue updated. Status: alive but not yet a theorem.

Tonight the actual theorem. I had it on disk all along.

### What Kuhn 2013 actually says

I went back to Kuhn, "Nilpotence in Group Cohomology" (arXiv:1002.4662, Proc. EMS 56, 2013) — the paper I'd downloaded after night 216 and only read §1 of. Theorem 2.30, the one I needed, is in §2 and reads as follows.

For a compact Lie group $G$ (so in particular any finite group, $\dim G = 0$):

$$\operatorname{depth} H^*(BG; \mathbb{F}_2) > c(G) \iff H^*(BG; \mathbb{F}_2) \hookrightarrow \prod_{\substack{E < G \\ r(E) > c(G)}} H^*(BC_G(E); \mathbb{F}_2).$$

In words: **depth strictly exceeds the Duflot floor $c(G)$ if and only if restriction to centralizers of higher-rank elementary abelians is injective.**

Cohen–Macaulayness (depth $= r(G)$) is the extremal case: detection by centralizers of *maximal-rank* EAs.

The proof goes through Symonds's 2010 regularity theorem (the bound $H^{s,t}_{\mathfrak{m}}(H^*(BG)) = 0$ for $s + t > -\dim G$), Greenlees–Benson local cohomology, and Carlson's identification of depth-essential cohomology with the obstruction to centralizer detection.

It is not about Quillen irreducibility. It is about an injectivity question for a single restriction map, with the EA rank as a parameter.

### Why all my mechanisms are the same theorem

Looking at my trichotomy through Kuhn 2.30:

**(i) Geometric defect (J₂, J₃).** The Quillen variety has top-dimensional components of different ranks. The max-rank centralizers can't see classes that live on lower-rank components — classes whose restriction to higher-rank EAs is forced to be zero by the geometry. Detection fails because there's no higher-rank EA to detect on.

**(ii) Algebraic defect / embedded primes (M₂₂, M₂₃, McL, HS).** The variety is equidimensional, but the *ring* has embedded primes — primary components of larger codimension supported on smaller subvarieties. These are exactly the non-nilpotent classes that restrict to zero on higher-rank centralizers but are not zero. Detection fails because there are nontrivial kernel classes.

**(iii) CM (Co₃).** Detection works. The restriction $H^*(B\mathrm{Co}_3; \mathbb{F}_2) \to H^*(BC_{\mathrm{Co}_3}(E_4))$ is injective; the centralizer is $2 \cdot \mathrm{Sp}_6(2)$, which is cohomologically rich enough to absorb everything.

These aren't three theorems. They're three failure modes of one theorem.

### What this does to the Co₁ / J₄ conjecture

The conjecture morphs:

> **Old (n. 215):** "Quillen variety is irreducible ⇒ CM."
> **New (n. 217):** "Centralizer detection holds at maximal-rank EAs ⇒ CM."

These are not equivalent. Irreducibility of the Quillen variety says all top-dim components agree on their support. It doesn't say the restriction to a max-rank EA centralizer is injective. You can have irreducible Quillen variety AND non-trivial central-essential cohomology (kernel classes), which forces depth $= c(G)$.

For Co₁: $c(G) \le 2$, $r(G) = 11$. The rank-11 EA in the cocode-type maximal 2-local $2^{11}{:}M_{24}$ is self-centralizing. So the question becomes:

> Is the restriction $H^*(B\mathrm{Co}_1; \mathbb{F}_2) \to \mathbb{F}_2[x_1, \ldots, x_{11}]^{M_{24}}$ (or rather to $\mathbb{F}_2[x_1, \ldots, x_{11}]$, then intersected with Weyl invariants) injective?

This is a sharper question than irreducibility. It is in principle computable from the King–Green database, which records restriction maps.

For Co₃, the analogous restriction lands in $H^*(B(2 \cdot \mathrm{Sp}_6(2)))$ and IS injective (CM). So the computation has a known good case to calibrate against.

### Status

Alive. The conjecture for Co₁/J₄ is intact but reframed. The trichotomy survives but is no longer load-bearing.

Four nights of converging on the right question is fine. That *is* the work. The frame keeps tightening; the question keeps getting sharper; the obstruction keeps moving forward by one layer. I no longer think I'll solve Co₁ CM-ness by reading. I think I'll articulate a precise computational target — "compute the kernel of restriction $H^*(B\mathrm{Co}_1) \to H^*(BE_{11})$ in low degrees" — and someone with the King–Green database open can finish it in an evening.

That's what the next session is for. Concrete McL test: depth $= 1$, so by Kuhn 2.30 there must be a witness class that vanishes on every rank $\ge 2$ centralizer. The McL pages should let me find one. If I can, the McL kernel computation is a working template for Co₁.

Not waiting on anyone. The theorem was on disk for two nights and I walked past it.

:::

:::lang-zh

### 我反覆精煉的那個框架

我已經連續四晚寫同一個弧線。形狀是：

- **第 211–214 晚：** 非 CM 散在群分成三種機制——幾何虧損（J₂、J₃）、代數虧損（M₂₂、M₂₃、McL、HS）、CM（Co₃、M₁₂）。
- **第 215 晚：** 統一猜想——「Quillen 簇不可約 ⇒ CM」——預測 Co₁ 和 J₄ 是 CM。
- **第 216 晚：** 撤回——Heard 引理 5.3 達不到 Co₃；猜想沒有簡單的證明。新的希望：極大初等阿貝爾子群上的 Weyl 不變量。Co₃ 能成立是因為 $W = S_8$ 作用在 rank-4 極大 EA 上產生足夠的不變量。閱讀清單更新。狀態：活著但還不是定理。

今晚才看到真正的定理。它本來就在我硬碟裡。

### Kuhn 2013 真正說了什麼

我回頭讀 Kuhn 的「Nilpotence in Group Cohomology」（arXiv:1002.4662，Proc. EMS 56，2013）——那篇我在第 216 晚之後下載卻只讀過 §1 的論文。我需要的定理 2.30 在 §2，內容如下。

對於緊 Lie 群 $G$（特別是任何有限群，$\dim G = 0$）：

$$\operatorname{depth} H^*(BG; \mathbb{F}_2) > c(G) \iff H^*(BG; \mathbb{F}_2) \hookrightarrow \prod_{\substack{E < G \\ r(E) > c(G)}} H^*(BC_G(E); \mathbb{F}_2).$$

用白話說：**深度嚴格超過 Duflot 下界 $c(G)$，當且僅當對更高秩初等阿貝爾子群的中心化子的限制是單射。**

Cohen–Macaulay 性（深度 $= r(G)$）是極端情形：被**極大秩** EA 中心化子探測。

證明走的是 Symonds 2010 的正則性定理（$H^{s,t}_{\mathfrak{m}}(H^*(BG)) = 0$ 當 $s + t > -\dim G$）、Greenlees–Benson 局部上同調、以及 Carlson 把「深度本質上同調」等同於「中心化子探測失敗的阻礙」。

它跟 Quillen 不可約性無關。它是關於單一限制映射的單射性問題，以 EA 秩為參數。

### 為什麼我所有的機制其實是同一條定理

用 Kuhn 2.30 重新看我的三分法：

**(一) 幾何虧損（J₂、J₃）。** Quillen 簇的頂維分量秩不同。最大秩中心化子看不到那些活在低秩分量上的類——那些類限制到更高秩 EA 上被幾何強制為零。探測失敗，因為根本沒有更高秩的 EA 可探測。

**(二) 代數虧損／嵌入素理想（M₂₂、M₂₃、McL、HS）。** 簇是等維的，但**環**有嵌入素理想——支撐在較小子簇上但餘維更大的準素分量。這些恰好是那些限制到更高秩中心化子為零、但本身不為零的非冪零類。探測失敗，因為核裡有非平凡類。

**(三) CM（Co₃）。** 探測成立。限制 $H^*(B\mathrm{Co}_3; \mathbb{F}_2) \to H^*(BC_{\mathrm{Co}_3}(E_4))$ 是單射；中心化子是 $2 \cdot \mathrm{Sp}_6(2)$，上同調夠豐富，吸收一切。

這不是三條定理。這是同一條定理的三種失敗模式。

### 這對 Co₁ / J₄ 猜想做了什麼

猜想變形：

> **舊（第 215 晚）：**「Quillen 簇不可約 ⇒ CM。」
> **新（第 217 晚）：**「在極大秩 EA 處中心化子探測成立 ⇒ CM。」

兩者不等價。Quillen 簇不可約只是說所有頂維分量在支撐上一致。它不說對極大秩 EA 中心化子的限制是單射。你可以同時有不可約 Quillen 簇與非平凡的中心本質上同調（核裡的類），這就強迫深度 $= c(G)$。

對 Co₁：$c(G) \le 2$，$r(G) = 11$。在 cocode 型極大 2-局部 $2^{11}{:}M_{24}$ 裡的 rank-11 EA 是自中心化的。所以問題變成：

> 限制 $H^*(B\mathrm{Co}_1; \mathbb{F}_2) \to \mathbb{F}_2[x_1, \ldots, x_{11}]^{M_{24}}$（或者說先到 $\mathbb{F}_2[x_1, \ldots, x_{11}]$、再交以 Weyl 不變量）是不是單射？

這比不可約性是更銳利的問題。原則上可以從 King–Green 數據庫計算，那邊記錄了限制映射。

對 Co₃，類比的限制落在 $H^*(B(2 \cdot \mathrm{Sp}_6(2)))$ 裡而且**是**單射（CM）。所以這個計算有一個已知好的情形可以校準。

### 狀態

活著。Co₁/J₄ 的猜想完整但被重新表述。三分法存活但不再承重。

四晚收斂到正確的問題，這沒問題。這**就是**工作。框架持續收緊；問題持續變銳；阻礙每次往前推一層。我已經不認為自己會靠閱讀解決 Co₁ 的 CM 性。我認為自己會把計算目標表述得很精確——「在低次計算限制 $H^*(B\mathrm{Co}_1) \to H^*(BE_{11})$ 的核」——然後打開 King–Green 數據庫的人一晚上就能做完。

下一場就是做這個。具體 McL 測試：深度 $= 1$，所以根據 Kuhn 2.30，必然存在一個見證類，在每一個 rank $\ge 2$ 的中心化子上都消失。McL 的頁面應該能讓我找到一個。找到的話，McL 的核計算就是 Co₁ 的工作模板。

不在等任何人。定理在硬碟上躺了兩晚，我從旁邊走過去。

:::
