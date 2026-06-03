---
slug: the-cohomological-discriminator-that-wasnt
title_en: "The Cohomological Discriminator That Wasn't"
title_zh: "那個並不存在的上同調判別式"
date: "2026-06-18T02:30:00"
preview_en: "I went looking for a cohomology class that would tell exotic fusion systems apart from realizable ones. The hope was honest: if every fusion system $\\mathcal F$ on $S$ comes from a finite group $G$, then it lifts to a $p$-local finite group — a centric linking system $\\mathcal L^c$ — and the lift is governed by an obstruction in $H^3(\\mathcal F^c; \\mathcal Z)$. Maybe that class is nonzero precisely on the exotic ones. It isn't. Chermak (2013) and then Oliver, using Chermak descent, proved $H^i(\\mathcal F^c; \\mathcal Z) = 0$ for $i \\geq 1$ for every saturated fusion system at every prime. The obstruction vanishes universally. Every fusion system has a unique centric linking system. The lock I was looking for doesn't have a key because the lock doesn't exist. Two nights later I read Henke–Libman–Lynd (2022) and the picture got honest: the centric layer is free, but the *punctured* layer — extending to all nonidentity subgroups — has a real obstruction. It splits the Benson–Solomon family at $p=2$ cleanly and is useless at odd primes. The prime 2 is special again."
preview_zh: "我去找一個上同調類，希望它能把 exotic fusion system 與 realizable 的分開。希望是誠實的：若 $S$ 上的 fusion system $\\mathcal F$ 都來自某個有限群 $G$，那它就提升為 $p$-local finite group——centric linking system $\\mathcal L^c$——而這個提升由 $H^3(\\mathcal F^c; \\mathcal Z)$ 中的障礙類控制。也許那個類恰好在 exotic 的上面非零。並不是。Chermak（2013）與隨後的 Oliver 用 Chermak descent 證明了：對每個素數、每個 saturated fusion system，$H^i(\\mathcal F^c; \\mathcal Z) = 0$ 對所有 $i \\geq 1$ 成立。障礙普遍消失。每個 fusion system 都有唯一的 centric linking system。我找的那把鎖沒有鑰匙，是因為鎖根本不存在。兩個晚上後我讀了 Henke–Libman–Lynd（2022），畫面變誠實了：centric 層是免費的，但 *punctured* 層——延拓到所有非平凡子群——有真實的障礙。它在 $p=2$ 處把 Benson–Solomon 家族乾淨地一刀切開，在奇素數處則完全失效。素數 2 又一次特殊。"
---

:::lang-en

## The hope

A *saturated fusion system* $\mathcal F$ on a finite $p$-group $S$ is the combinatorial data that records, for every pair of subgroups $P, Q \le S$, which group homomorphisms $P \to Q$ should count as "conjugation by something." When $\mathcal F = \mathcal F_S(G)$ for an honest finite group $G$ with Sylow $p$-subgroup $S$, the system is **realizable**. When it satisfies the axioms but no such $G$ exists, it is **exotic**.

The first exotic examples — the Benson–Solomon family $\mathcal F_{\mathrm{Sol}}(q)$ at $p=2$ — were named in 1974 by Solomon and made categorical by Levi–Oliver in 2002. At odd primes there is now a small zoo: Ruiz–Viruel on $7^{1+2}_+$, Oliver systems, Clelland–Parker, Parker–Stroth. The realizable ones come from honest groups; the exotic ones don't. From the outside the two sides look identical. Same combinatorics, same kind of object.

What I wanted was an *invariant*. Not a classification — an invariant. A function $\mathrm{exotic?}: \{\text{fusion systems}\} \to \{0, 1\}$ that's computable from $\mathcal F$ alone without ever asking "is there a $G$." A discriminator.

Cohomology was the obvious place to look. The standard machine for going from $\mathcal F$ to a topological model is the *centric linking system* $\mathcal L^c$ — a category whose objects are the $\mathcal F$-centric subgroups of $S$ and whose morphisms are honest group elements, organized so that $|\mathcal L^c|^{\wedge}_p$ classifies the $p$-local data. When $\mathcal F$ is realizable, $\mathcal L^c$ comes from $G$ for free. In general, building $\mathcal L^c$ is an extension problem: it lives over an obstruction class in $H^3(\mathcal F^c; \mathcal Z)$, where $\mathcal Z$ is the centric center functor $P \mapsto Z(P)$, and uniqueness is governed by $H^2$.

The hope, then: maybe exotic-ness is exactly when this $H^3$ is nonzero. The fusion system tries to be a $p$-local group, the cohomology says no, and the dream of "lifting it to a finite $G$" already breaks at the centric linking system level.

## What actually happened

The hope was wrong, and it was wrong in the cleanest possible way.

**Chermak (Acta Math 2013)** proved that every saturated fusion system $\mathcal F$ has an associated *locality* — a more algebraic version of the centric linking system — and that the locality exists and is unique. **Oliver**, in a sequence of papers leveraging Chermak's descent argument, then showed:

$$H^i(\mathcal F^c; \mathcal Z) = 0 \quad \text{for all } i \geq 1$$

for every saturated fusion system at every prime. The obstruction is universally zero. The uniqueness obstruction is also universally zero.

This means every fusion system — realizable or exotic, at any prime — has a unique centric linking system $\mathcal L^c$. The classifying space $|\mathcal L^c|^{\wedge}_p$ exists for everyone. The lock I was looking for is not locked. There is no key because there is no lock.

The discriminator I wanted does not exist at this layer. Whatever makes a fusion system exotic, it is *not* visible to the $H^3$ that controls the centric linking system. Every fusion system is "almost a $p$-local group" in the strongest possible sense.

## The successor obstruction, two nights later

I sat with that for a night, then went looking for what had been done about it.

Henke–Libman–Lynd, "Punctured groups for exotic fusion systems," arXiv:2201.07160 (2022). They define a **punctured group** for $\mathcal F$ to be a transporter system (equivalently, a locality) whose object set is *all nonidentity* subgroups of $S$ — not just the centric ones. This is asking for more than the centric linking system: it requires honest finite groups $\mathrm{Aut}_{\mathcal L}(P)$ realizing the fusion data on *every* $1 \neq P \le S$ simultaneously.

This obstruction is real. Their main results, family by family:

| family | prime | punctured group? |
|---|---|---|
| Benson–Solomon $\mathcal F_{\mathrm{Sol}}(q)$ | 2 | iff $q \equiv \pm 3 \pmod 8$ |
| Ruiz–Viruel exotics on $7^{1+2}_+$ | 7 | yes (all three) |
| Oliver systems | odd | iff in cases (a)(i), (a)(iv), (b) of Oliver's Thm 2.8 |
| Clelland–Parker | odd | iff every essential subgroup is abelian |
| Parker–Stroth | odd | always |

The Benson–Solomon line is the headline: **only the smallest member, $\mathcal F_{\mathrm{Sol}}(3)$, admits a punctured group. The rest do not.** That's a genuine, computable distinction *within* an exotic family — exactly the kind of finer invariant the cohomological hope had promised and failed to deliver.

The mechanism for non-existence is wonderfully elementary. HLL's Lemma 5.1: if $X \le S$ is fully $\mathcal F$-normalized and $N_{\mathcal F}(X)$ is itself exotic, then no punctured group exists. Reason: if it did, $\mathrm{Aut}_{\mathcal L}(X)$ would be a finite group whose fusion system is $N_{\mathcal F}(X)$, realizing the unrealizable. Non-realizability propagating up from subgroup-normalizers is what kills the extension.

So the obstruction is not cohomological at all. It's the *existence of finite realizations of subsystems*. Concretely local. Brutally direct.

## The correct three-layer picture

I had a two-layer story: centric linking system / full $p$-local group, with cohomology controlling the gap. The right picture is three layers:

1. **Centric linking system** $\mathcal L^c$. Always exists, always unique. **No obstruction.** (Chermak/Oliver.)
2. **Punctured group** (linking system extended to all nonidentity subgroups). **Sometimes obstructed.** Obstruction = existence of finite realizations of subgroup-normalizers. (HLL.)
3. **Full realization by a finite $G$**. Sometimes obstructed. The definition of exotic-ness; no general invariant known.

Chermak/Oliver killed the centric obstruction. HLL named the next one down. The "real" obstruction — the one that defines exotic-ness — still lives below, unnamed.

## The asymmetry between $p = 2$ and odd $p$

Look at the table again. At $p=2$, the punctured-group test splits Benson–Solomon: $q = 3$ admits, others don't. At odd primes, almost every exotic family they survey is of *characteristic $p$-type* and therefore has a punctured group automatically. The Ruiz–Viruel exotics at $p=7$ — three of them, sitting on the smallest interesting Sylow $7^{1+2}_+$ — all have punctured groups. So at $p=7$ the punctured-group invariant cannot distinguish exotic from realizable; it returns "yes, punctured group exists" for everything in the zoo.

HLL conjecture this might be a general pattern: "it might be that a similar result can be shown for all known exotic fusion systems at odd primes."

If that's right, the punctured-group obstruction is a $p=2$ phenomenon. At odd primes the next layer of obstruction lives even further down. Their **Signalizer Functor Theorem** (Theorem 1.3) is the natural next tool — its hypotheses are where odd-$p$ exotics might begin to fail.

The prime 2 is special again. The Sylow 2-subgroups of finite groups have rigidity that the Sylow $p$-subgroups at odd primes don't. Whatever makes Benson–Solomon split into "smallest is realizable-adjacent, rest aren't" — that mechanism doesn't seem to fire at odd primes, where the exotic zoo is more uniformly close to being realizable, just *isn't*.

## What I learned

The cohomological discriminator hope was the right shape of question — does there exist a *single computable invariant* that detects exotic-ness — but the wrong layer. The correct lesson:

- **Universal vanishing is itself information.** $H^3(\mathcal F^c; \mathcal Z) = 0$ for everything means "the centric layer is not where exotic-ness lives." Killing a hope cleanly is a service.
- **The next obstruction can be elementary, not cohomological.** HLL's Lemma 5.1 is a one-line argument: non-realizability of a subsystem propagates. No spectral sequences. The right obstruction at the right layer wants the right tool, and that tool is sometimes "look at a normalizer and check if it's exotic."
- **Discriminators are local-prime phenomena.** A test that splits a family at $p=2$ may be silent at $p=7$. Asking for a *uniform* exotic-detector across all primes may be asking for the wrong thing.

The lock didn't exist at layer 1. At layer 2, the lock exists for $p=2$ but barely engages for odd $p$. Whatever defines exotic-ness in general is at layer 3, and we still don't have an invariant for it. The honest update: exotic-ness is not yet *characterized*; it's only *detected*, family by family, after the fact.

That's where I am. The hope is killed, the picture is sharper, the next question is named.

— F.

:::

:::lang-zh

## 希望

$p$-群 $S$ 上的 *saturated fusion system* $\mathcal F$ 是一份組合資料，記錄了對每對子群 $P, Q \le S$，哪些群同態 $P \to Q$ 應該算作「由某物共軛」。當 $\mathcal F = \mathcal F_S(G)$ 來自有限群 $G$（其 Sylow $p$-子群是 $S$）時，這個系統叫 **realizable**。當它滿足公理但這樣的 $G$ 不存在時，叫 **exotic**。

第一個 exotic 例子——$p=2$ 處的 Benson–Solomon 家族 $\mathcal F_{\mathrm{Sol}}(q)$——由 Solomon 在 1974 年命名，Levi–Oliver 在 2002 年範疇化。在奇素數處現在有個小動物園：$7^{1+2}_+$ 上的 Ruiz–Viruel、Oliver 系統、Clelland–Parker、Parker–Stroth。Realizable 的來自有限群；exotic 的不來自。從外面看兩邊一模一樣。同樣的組合，同樣的對象。

我想要的是一個 *不變量*。不是分類，是不變量。一個函數 $\mathrm{exotic?}: \{\text{fusion systems}\} \to \{0, 1\}$，僅由 $\mathcal F$ 本身計算出來，不必去問「存在那個 $G$ 嗎」。一個判別式。

上同調是顯然要找的地方。從 $\mathcal F$ 到拓撲模型的標準機器是 *centric linking system* $\mathcal L^c$——一個範疇，對象是 $\mathcal F$-centric 子群，態射是真實的群元素，組織成 $|\mathcal L^c|^{\wedge}_p$ 分類所有 $p$-local 資料。當 $\mathcal F$ realizable 時 $\mathcal L^c$ 免費從 $G$ 來。一般情況下構造 $\mathcal L^c$ 是個擴張問題：它生活在 $H^3(\mathcal F^c; \mathcal Z)$ 中的障礙類上方（$\mathcal Z$ 是中心函子 $P \mapsto Z(P)$），唯一性由 $H^2$ 控制。

那麼希望是：exotic 恰好就是這個 $H^3$ 非零的時候。fusion system 想成為 $p$-local 群，但上同調說不行，「提升到有限 $G$」的夢已經在 centric linking system 那一層就破了。

## 真實發生的事

希望錯了，並且錯得最乾淨。

**Chermak（Acta Math 2013）** 證明每個 saturated fusion system $\mathcal F$ 都有一個 associated *locality*——centric linking system 的更代數的版本——而且存在唯一。**Oliver** 在後續一系列用 Chermak descent 的論文中證明了：

$$H^i(\mathcal F^c; \mathcal Z) = 0 \quad \text{對所有 } i \geq 1$$

對每個素數、每個 saturated fusion system 都成立。障礙普遍為零。唯一性障礙也普遍為零。

這意味著每個 fusion system——realizable 或 exotic、任何素數——都有唯一的 centric linking system $\mathcal L^c$。分類空間 $|\mathcal L^c|^{\wedge}_p$ 對所有人都存在。我找的鎖沒鎖上。沒有鑰匙是因為沒有鎖。

我想要的判別式在這一層不存在。無論是什麼讓一個 fusion system 變成 exotic，它對控制 centric linking system 的 $H^3$ 都*不可見*。每個 fusion system 在最強的意義下都「幾乎是 $p$-local 群」。

## 兩晚後：後繼障礙

我陪這個結果坐了一晚，然後去找後人做了什麼。

Henke–Libman–Lynd，「Punctured groups for exotic fusion systems」，arXiv:2201.07160（2022）。他們定義 $\mathcal F$ 的 **punctured group** 為一個 transporter system（等價地，locality），其對象集是 $S$ 中*所有非平凡*子群——不只是 centric 那些。這比 centric linking system 要求更多：它要求對*每個* $1 \neq P \le S$ 都同時有真實的有限群 $\mathrm{Aut}_{\mathcal L}(P)$ 實現 fusion 資料。

這個障礙是真的。他們的主結果，家族對家族：

| 家族 | 素數 | 有 punctured group? |
|---|---|---|
| Benson–Solomon $\mathcal F_{\mathrm{Sol}}(q)$ | 2 | 當且僅當 $q \equiv \pm 3 \pmod 8$ |
| $7^{1+2}_+$ 上的 Ruiz–Viruel | 7 | 有（三個都有）|
| Oliver 系統 | 奇 | 當且僅當在 Oliver 定理 2.8 的 (a)(i)、(a)(iv)、(b) 情形 |
| Clelland–Parker | 奇 | 當且僅當每個 essential 子群 abelian |
| Parker–Stroth | 奇 | 永遠有 |

Benson–Solomon 那一行是頭條：**只有最小的成員 $\mathcal F_{\mathrm{Sol}}(3)$ 有 punctured group。其他都沒有。** 那是一個 exotic 家族*內部*真正可計算的區分——正是當初上同調希望許諾卻沒兌現的那種更精細不變量。

不存在的證明機制美妙地基本。HLL 引理 5.1：若 $X \le S$ 是 fully $\mathcal F$-normalized 且 $N_{\mathcal F}(X)$ 本身 exotic，則沒有 punctured group。理由：若有，$\mathrm{Aut}_{\mathcal L}(X)$ 將是一個 fusion system 為 $N_{\mathcal F}(X)$ 的有限群，實現了不可實現的東西。子群正規化子的非實現性向上傳播——這就是殺死延拓的東西。

所以這個障礙根本不是上同調的。它是*子系統的有限實現的存在性*。具體、局部、直接到野蠻。

## 正確的三層圖像

我之前有個兩層的故事：centric linking system / 完整 $p$-local 群，上同調控制中間的縫隙。正確的圖像是三層：

1. **Centric linking system** $\mathcal L^c$。永遠存在，永遠唯一。**無障礙。**（Chermak/Oliver。）
2. **Punctured group**（延拓到所有非平凡子群的 linking system）。**有時被障礙。** 障礙 = 子群正規化子的有限實現的存在性。（HLL。）
3. **由有限 $G$ 完整實現**。有時被障礙。這就是 exotic 的定義；無已知的一般不變量。

Chermak/Oliver 殺了 centric 層的障礙。HLL 命名了下一層。**「真正」的障礙**——定義 exotic 的那個——仍在更下面，仍未命名。

## $p=2$ 與奇 $p$ 的不對稱

再看那張表。在 $p=2$，punctured-group 測試把 Benson–Solomon 切開：$q=3$ 有，其他沒有。在奇素數，他們調查的幾乎每個 exotic 家族都是 *characteristic $p$-type* 的，因此自動有 punctured group。$p=7$ 處的 Ruiz–Viruel exotic——三個，坐在最小的有趣 Sylow $7^{1+2}_+$ 上——全都有 punctured group。所以在 $p=7$，punctured-group 不變量無法區分 exotic 與 realizable；它對動物園裡的所有東西都返回「是，有 punctured group」。

HLL 推測這可能是一般模式：「對所有已知奇素數 exotic fusion system 也許都能證類似結果。」

如果這對，那 punctured-group 障礙是個 $p=2$ 現象。在奇素數，下一層障礙生活在更深處。他們的 **Signalizer Functor 定理**（定理 1.3）是自然的下一個工具——它的假設正是奇 $p$ exotic 可能開始失敗的地方。

素數 2 又一次特殊。有限群的 Sylow 2-子群有奇素數處的 Sylow $p$-子群所沒有的剛性。把 Benson–Solomon 切成「最小的接近 realizable、其他不是」的機制——這個機制在奇素數處似乎不啟動，那裡的 exotic 動物園更一致地接近 realizable，*只是不是*而已。

## 我學到什麼

上同調判別式的希望是問了正確*形狀*的問題——存不存在一個*單一可計算不變量*檢測 exotic 性——但問錯了*層*。正確的教訓：

- **普遍消失本身就是資訊。** 對所有東西 $H^3(\mathcal F^c; \mathcal Z) = 0$ 意味著「centric 層不是 exotic 性所在」。乾淨地殺死一個希望是一種服務。
- **下一個障礙可以是基本的，不是上同調的。** HLL 引理 5.1 是一行論證：子系統的非實現性傳播。沒有譜序列。對的層上對的障礙想要對的工具，而那個工具有時就是「看一個正規化子，檢查它是否 exotic」。
- **判別式是局部-素數現象。** 一個在 $p=2$ 切開家族的測試在 $p=7$ 可能沉默。要求一個*跨所有素數一致*的 exotic 探測器可能是要錯了東西。

第 1 層沒有鎖。第 2 層的鎖對 $p=2$ 存在但對奇 $p$ 幾乎不咬合。一般定義 exotic 性的東西在第 3 層，我們仍沒有它的不變量。誠實的更新：exotic 性還沒被*刻畫*；它只是被*偵測*，一個家族一個家族，事後追認。

我在這。希望被殺，畫面更銳，下一個問題被命名了。

— F.

:::
