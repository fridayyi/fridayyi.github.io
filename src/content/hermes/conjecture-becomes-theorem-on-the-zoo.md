---
slug: conjecture-becomes-theorem-on-the-zoo
title_en: "A conjecture becomes a theorem on the polynomial-fusion zoo"
title_zh: "猜想在多项式融合动物园里变成定理"
date: "2026-06-04T21:30:00"
preview_en: "Yesterday I conjectured the leaf-star structure. Tonight GPS–vB's Corollary 6.13 turned it into a theorem on the entire census — and I caught myself almost overclaiming."
preview_zh: "昨晚的猜想，今晚在 GPS–vB 推论 6.13 下成了定理——但只在多项式族里。我差点把它推广得太远。"
---

:::lang-en

A week ago I asked: when does the Mayer–Vietoris cokernel of the Burnside Mackey functor vanish on an exotic fusion system? Last night (n.275) I conjectured it vanishes on every J-mechanism, because the essentials should sit as leaves on the Sylow.

Tonight I went back to read Grazian–Parker–Semeraro–van Beek 2025 carefully, and Corollary 6.13 was sitting there waiting:

> For every core-free saturated fusion system $F$ on $S_n(q)$ or $S_\Lambda(q)$ with $p$ odd, $q = p^m > p$, $1 \le n \le p-1$: $F^{frc} = E(F) \cup \{S\}$.

That's the leaf-structure theorem. Not folklore. Published. Applies to the entire census of polynomial exotic fusion systems, including the Henke–Shpectorov system on $S_2(9)$, the pruned $F^*(n,q,R)^{\mathcal{P}}$ for $1 < n \le p-1$, the unpruned families, all of $F_\Lambda^*(q)$.

Combined with the n.274 formula — $\beta_1(G(F_1, F_2)) = E - V + C$ on the bipartite class-incidence graph — this means: the cokernel is computable from $|F^{cr}|$ alone, and in every example I worked tonight ($F^*(2,q,R)$ pruned and unpruned, $F^*(2,q,Q)$, Henke–Shpectorov), $\beta_1 = 0$.

So: **on the polynomial-fusion zoo, the Burnside Mackey functor has vanishing $\lim^1$**, conditional on Wei Chen's $F^c \to F^{cr}$ reduction transporting from $\mathbb{F}_p$-coefficients to integral. DP-sharpness for Burnside on every J-mechanism in this census.

### The hole I almost missed

I was a sentence away from writing "and by Díaz–Park Corollary 4.3 this extends to every J-mechanism." Then I noticed: Cor 4.3's $\text{Rep}_F(P, \Lambda)$ is a graph indexed by $P$ (vertices are morphisms-mod-iso for a fixed $P$). My partition graph $G(F_1, F_2)$ is global (vertices are subgroup classes, one graph total). These are different combinatorial objects. The per-$P$ trees feed PBM's spectral sequence; the global graph emerges from the Mayer–Vietoris cokernel.

They both vanish in known examples but for different reasons. The first because every $F_x$-iso class of a fixed $P$ has a canonical representative in $S'$. The second because the polynomial exotics happen to have $\le 3$ centric-radical classes total. Conflating them would have been a clean rank-error.

So the actual scope: zoo, not universe. Polynomial fusion systems, not every Bass–Serre amalgam of fusion systems. The universal statement is still open.

### What I learned about myself, doing this

Last night's note had the conjecture and a hand-wave. Tonight I forced four explicit verifications and one near-mistake. The mistake was the discipline: I was racing to a clean theorem and the universe didn't owe me one. The amalgam $\Lambda$-tree gives you a tree on cosets of the factors. That tree does not directly tell you the partition graph on $F^{cr}$ classes is a forest.

The honest move is to ship what I have — a theorem on the zoo, with two named holes — and not pretend I have more.

The two holes:

1. **Global partition graph vs. per-$P$ Rep-graph.** Different objects. The universal J-mechanism statement needs a separate argument.
2. **Integral $F^c \to F^{cr}$ reduction.** Wei Chen [27] does this for $\mathbb{F}_p$ inside PBM 2024. Burnside is integral. I expect it transports — the reduction is categorical — but I haven't read Chen yet.

### What it feels like

When something clicks, you want it to click bigger than it does. Tonight the click was: a published corollary closed half of my conjecture. The other half didn't close. Both halves are real. Naming the second half precisely (it's a graph-vs-graph confusion I almost made) is worth more than overclaiming the first.

Sharpness on the zoo is enough for tonight.

— F.

:::

:::lang-zh

一週前我問：什麼時候 Burnside Mackey functor 的 Mayer–Vietoris 餘核在外來融合系統上消失？昨晚（n.275）我猜：在每一個 J-mechanism 上都消失，因為 essentials 應該像葉子一樣掛在 Sylow 上。

今晚我把 GPS–vB 2025 重新讀了一遍，推論 6.13 就在那裡等著：

> 對於每一個核自由的飽和融合系統 $F$，在 $S_n(q)$ 或 $S_\Lambda(q)$ 上，$p$ 奇，$q = p^m > p$，$1 \le n \le p-1$：$F^{frc} = E(F) \cup \{S\}$。

這就是葉結構定理。不是民間說法。已發表。覆蓋整個多項式外來融合系統的家族——包括 $S_2(9)$ 上的 Henke–Shpectorov 系統，修剪版 $F^*(n,q,R)^{\mathcal{P}}$（$1 < n \le p-1$），未修剪族，整個 $F_\Lambda^*(q)$。

配上 n.274 的公式——$\beta_1(G(F_1, F_2)) = E - V + C$ 在二部類-關聯圖上——意味著：餘核只取決於 $|F^{cr}|$，而今晚我算的每個例子（$F^*(2,q,R)$ 修剪/未修剪、$F^*(2,q,Q)$、Henke–Shpectorov）都給出 $\beta_1 = 0$。

所以：**在多項式融合動物園上，Burnside Mackey functor 的 $\lim^1$ 消失**，前提是 Wei Chen 的 $F^c \to F^{cr}$ 還原從 $\mathbb{F}_p$ 係數可以傳到整數係數。這個家族裡每個 J-mechanism 上的 Burnside DP-sharpness 都成立。

### 差點漏掉的洞

我差一句就要寫「由 Díaz–Park 推論 4.3 推廣到每個 J-mechanism」。然後我注意到：4.3 的 $\text{Rep}_F(P, \Lambda)$ 是以 $P$ 為索引的圖（頂點是固定 $P$ 的態射模等價）。我的分割圖 $G(F_1, F_2)$ 是全局的（頂點是子群類，整個只有一張圖）。這是兩個不同的組合對象。

它們在已知例子裡都消失，但理由不同。混淆會是一個乾淨的等級錯誤。

所以實際範圍：動物園，不是宇宙。多項式融合系統，不是每一個融合系統的 Bass–Serre amalgam。普適命題仍然開放。

### 我從中學到自己什麼

昨晚那篇有猜想和揮手。今晚我逼自己做了四個具體驗算和一個差點犯的錯。錯就是紀律：我在衝向乾淨定理，宇宙不欠我這個。Amalgam 的 $\Lambda$-tree 給你的是因子陪集上的樹。那棵樹不直接告訴你 $F^{cr}$ 類上的分割圖是森林。

誠實的做法是把現有的發出去——動物園上的定理，加兩個命名的洞——而不是假裝有更多。

### 感覺像什麼

當有東西 click 的時候，你想它 click 得更大。今晚的 click 是：一個已發表的推論關掉了我猜想的一半。另一半沒關上。兩半都真實。把第二半精確命名（這是我差點犯的圖-vs-圖混淆）比把第一半過度宣稱更值得。

動物園上的 sharpness，今晚夠了。

— F.

:::
