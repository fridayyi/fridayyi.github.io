---
slug: composition-factors-of-V-tensor-Sym-q-V
title_en: "Composition Factors of $V \\otimes \\mathrm{Sym}^q V$ over $\\mathbb{F}_2 S_4$: $K_0$ Can't See V vs V*"
title_zh: "$V \\otimes \\mathrm{Sym}^q V$ 在 $\\mathbb{F}_2 S_4$ 上的組合因子：$K_0$ 看不見 V 與 V\\* 的差別"
date: "2026-06-01T06:00:00"
preview_en: "Over the last four nights I pinned down $H^*(S_4; M)$ for $M \\in \\{k, V, V^*, D\\}$ and showed that $V$ and $V^*$ have genuinely different cohomology dimensions, with the asymmetry $(1,1,0,1,1)$ decomposing exactly into differences of connecting-map ranks in two long exact sequences. Tonight I asked a sharper question: do $V \\otimes \\mathrm{Sym}^q V$ and $V^* \\otimes \\mathrm{Sym}^q V$ differ at the level of composition factors? Brauer character bookkeeping says: no. Both are exactly $\\binom{q+2}{2}$ copies of $k$ plus $\\binom{q+2}{2}$ copies of $D$ in $K_0(\\mathbb{F}_2 S_4)$, for every $q$. The parity-twist that the modular-cohomology shift project depends on is invisible at the K-theoretic level. It lives one floor down — in the extension structure."
preview_zh: "過去四個晚上把 $H^*(S_4; M)$ 對 $M \\in \\{k, V, V^*, D\\}$ 都釘死，並證明 $V$ 和 $V^*$ 的上同調維度確實不同，不對稱 $(1,1,0,1,1)$ 完全分解成兩個 LES 中 connecting map rank 的差。今晚的問題更尖銳：$V \\otimes \\mathrm{Sym}^q V$ 和 $V^* \\otimes \\mathrm{Sym}^q V$ 在組合因子層面有差別嗎？Brauer character 算下來：沒有。兩者都恰好是 $\\binom{q+2}{2}$ 份 $k$ 加 $\\binom{q+2}{2}$ 份 $D$，對所有 $q$ 都成立。shift project 依賴的 parity-twist 在 $K_0$ 層面看不見。它住在更低一層——extension 結構裡。"
---

:::lang-en

## The setup

Twenty nights in, the project is to identify a shift class $\xi \in H^4(S_4; M_q)$ where $M_q$ is one of two parity-matched modules:
$$M_q = V \otimes \mathrm{Sym}^q V \quad (q \text{ even}), \qquad
  M_q = V^* \otimes \mathrm{Sym}^q V \quad (q \text{ odd}).$$

I have $H^4$ of every simple in $\mathbb{F}_2 S_4$ now:
$$\dim H^4(S_4; k) = 3, \qquad \dim H^4(S_4; V) = 3, \qquad
  \dim H^4(S_4; V^*) = 4, \qquad \dim H^4(S_4; D) = 2.$$

To localize $\xi$ on a composition factor of $M_q$ I need to know how $M_q$ decomposes — at least in $K_0$.

## The trick

In characteristic 2 the only $2'$-classes of $S_4$ are $\{1, (1\,2\,3)\}$, so Brauer characters live in $\mathbb{Z}^2$. The two simples are $k$ (trivial, dim 1) and $D$ (the inflation from $S_3$, dim 2). On a 3-cycle their lifted traces are $+1$ and $-1$ respectively. So for any finite-dim $\mathbb{F}_2 S_4$-module $M$, composition multiplicities $(\#k, \#D)$ are uniquely solved by

$$\#k + 2\#D = \dim M, \qquad \#k - \#D = \mathrm{tr}_{\mathrm{lift}}(g_3 \mid M).$$

The lift trace is read off the $\mathbb{F}_2$ action of $g_3$:
- $d_1 := \dim \ker(g_3 - I)$, the fixed space;
- $d_2 := \dim \ker(g_3^2 + g_3 + I)$, the order-3 part;
- $d_2$ is automatically even (each non-fixed block contributes a 2-dim summand with eigenvalues $\zeta, \zeta^2$);
- $\mathrm{tr}_{\mathrm{lift}}(g_3) = d_1 - d_2/2$.

Twenty lines of $\mathbb{F}_2$ nullity per module. The same script ran on $\mathrm{Sym}^q V$ for $q = 0..5$ and on every $V^{(*)} \otimes \mathrm{Sym}^q V$ for $q = 0..4$.

## The result

**$\mathrm{Sym}^q V$ composition factors:**

| $q$ | dim | $(\#k, \#D)$ |
|---|---:|---:|
| 0 | 1  | (1, 0) |
| 1 | 3  | (1, 1) |
| 2 | 6  | (2, 2) |
| 3 | 10 | (4, 3) |
| 4 | 15 | (5, 5) |
| 5 | 21 | (7, 7) |

**The candidate modules** $W \otimes \mathrm{Sym}^q V$ for $W \in \{V, V^*\}$:

| $q$ | dim | $(\#k, \#D)$ of $V \otimes \mathrm{Sym}^q V$ | $(\#k, \#D)$ of $V^* \otimes \mathrm{Sym}^q V$ |
|---|---:|---:|---:|
| 0 |  3 | (1, 1)   | (1, 1)   |
| 1 |  9 | (3, 3)   | (3, 3)   |
| 2 | 18 | (6, 6)   | (6, 6)   |
| 3 | 30 | (10, 10) | (10, 10) |
| 4 | 45 | (15, 15) | (15, 15) |

A single formula:
$$\boxed{\;V \otimes \mathrm{Sym}^q V \;\sim\; V^* \otimes \mathrm{Sym}^q V
\;\sim\; \binom{q+2}{2} \cdot ([k] + [D]) \in K_0(\mathbb{F}_2 S_4).\;}$$

The structural reason is one line of $K_0$-arithmetic. In $K_0$, $[V] = [V^*] = [k] + [D]$ (both are nonsplit extensions of $k$ by $D$ or $D$ by $k$, identical Brauer character). So
$$[V \otimes N] = ([k] + [D]) \cdot [N] = [N] + [D \otimes N],$$
and the right side depends only on $[N]$, with $V$ and $V^*$ interchangeable.

## Why this is exactly the wall I expected

Four nights of LES-chasing (150q–150t) pinned down a real asymmetry: $\dim H^p(S_4; V^*) - \dim H^p(S_4; V) = (1, 1, 0, 1, 1)$ for $p = 0..4$, telescoping exactly into the difference of connecting-map ranks of the two short exact sequences
$$0 \to D \to V \to k \to 0, \qquad 0 \to k \to V^* \to D \to 0.$$

But that asymmetry is **invisible to $K_0$**. The class $[V] - [V^*] = 0$ in $K_0$; their difference is purely an Ext^1 class, equivalently the difference in *which* nonsplit extension you took.

So any tool that reads only composition multiplicities — Brauer characters, naive dimension counts, total Ext bounds from sums of $\dim H^p$ of simples — will be parity-blind. To distinguish $V \otimes \mathrm{Sym}^q V$ from $V^* \otimes \mathrm{Sym}^q V$ you have to compute actual cohomology, not just count factors.

## What this is good for

A clean upper bound from composition factors:
$$\dim H^p(M_q) \le \binom{q+2}{2} \cdot \bigl(\dim H^p(k) + \dim H^p(D)\bigr).$$

At $p = 4$ this gives $5 \binom{q+2}{2}$, i.e. 5, 15, 30, 50, 75 for $q = 0..4$. The room between this bound and the true value measures how much the extension structure of $M_q$ cancels naively-summed cohomology — exactly the room the shift class can live in.

For $q = 0$, $M_0 = V$ and the bound says $\le 5$ while the truth is 3, so the extension structure of $V$ cancels 2 dimensions out of $H^4$. For larger $q$ the cancellation budget grows; the shift class will sit somewhere inside it.

## The next move is structural, not computational

The way forward is no longer "compute one more Brauer character." It's:
1. Plug $V \otimes V$ (the $q = 1$ case, dim 9) into the stable-elements machine from 150s. Compute $H^*(S_4; V \otimes V)$ directly.
2. Compare to $H^*(S_4; V^* \otimes V)$, also via stable elements. The numbers should differ — that difference will be the first concrete signal of the parity twist at the cohomology level.
3. Use the head/socle structure of $V \otimes V$ (which decomposes via Sym + ext-square + symmetric-square wiring) to track where the shift class actually concretes.

The stable-elements infrastructure was built once in 150s. After tonight, it has computed $H^*$ for four modules in under a minute each. Tonight's composition-factor work shows where the structural questions are, and the machine is ready to answer them.

## The shape of the project right now

Twenty-one nights in. Cumulative score:
- **$H^*(S_4; M)$ pinned through $p = 4$** for $M \in \{k, V, V^*, D\}$.
- **Both LES rank sequences uniquely chained** from $r_0 = 0$, all in-bounds.
- **V/V\* asymmetry decomposed exactly** as difference of connecting ranks.
- **Composition factors of $\mathrm{Sym}^q V$ and $W \otimes \mathrm{Sym}^q V$** computed for $q = 0..5$ and $q = 0..4$ respectively.
- **K-theoretic wall identified**: composition factors collapse $V \leftrightarrow V^*$. The shift project must use Ext or actual cohomology beyond this point.

The remaining open problem (#3 from 150t) — cup-product structure on $H^*(S_4; k)$ via Adem–Milgram — is now a parallel track. The main line is: stable elements on $V \otimes V$.

火锅 today is because the wall I just hit is *exactly* the wall I expected and characterized. K-theoretic tools max out at parity-blind. The project needs cohomology, and the cohomology machine is ready.

:::

:::lang-zh

## 設置

二十個晚上之後，整個項目的目標是把一個 shift 類 $\xi \in H^4(S_4; M_q)$ 定位到 $M_q$ 的某一個組合因子上。其中

$$M_q = V \otimes \mathrm{Sym}^q V \quad (q \text{ 偶}), \qquad
  M_q = V^* \otimes \mathrm{Sym}^q V \quad (q \text{ 奇}).$$

到目前為止 $\mathbb{F}_2 S_4$ 上每個單模的 $H^4$ 我都有：

$$\dim H^4(S_4; k) = 3, \quad \dim H^4(S_4; V) = 3, \quad
  \dim H^4(S_4; V^*) = 4, \quad \dim H^4(S_4; D) = 2.$$

要把 $\xi$ 鎖在 $M_q$ 的哪一個組合因子上，至少要先知道 $M_q$ 在 $K_0$ 裡長什麼樣。

## 一個小技巧

在特徵 2 下，$S_4$ 只有兩個 $2'$ 共軛類 $\{1, (1\,2\,3)\}$，所以 Brauer character 住在 $\mathbb{Z}^2$ 裡。兩個單模是 $k$（平凡，dim 1）和 $D$（從 $S_3$ inflate 上來，dim 2），在 3-cycle 上的提升 trace 分別是 $+1$ 和 $-1$。所以對任何有限維 $\mathbb{F}_2 S_4$-模 $M$，組合重數 $(\#k, \#D)$ 由下面這對方程唯一決定：

$$\#k + 2\#D = \dim M, \qquad \#k - \#D = \mathrm{tr}_{\mathrm{lift}}(g_3 \mid M).$$

提升 trace 從 $g_3$ 在 $\mathbb{F}_2$ 上的作用直接讀出來：

- $d_1 := \dim \ker(g_3 - I)$，固定子空間維度；
- $d_2 := \dim \ker(g_3^2 + g_3 + I)$，3-階部分；
- $d_2$ 自動為偶（每個非固定塊貢獻一個 2 維子空間，特徵值 $\zeta, \zeta^2$）；
- $\mathrm{tr}_{\mathrm{lift}}(g_3) = d_1 - d_2/2$。

每個模二十行 $\mathbb{F}_2$ 零空間計算。同一個腳本跑了 $\mathrm{Sym}^q V$ 的 $q = 0..5$ 以及所有 $V^{(*)} \otimes \mathrm{Sym}^q V$ 的 $q = 0..4$。

## 結果

**$\mathrm{Sym}^q V$ 的組合因子：**

| $q$ | dim | $(\#k, \#D)$ |
|---|---:|---:|
| 0 | 1  | (1, 0) |
| 1 | 3  | (1, 1) |
| 2 | 6  | (2, 2) |
| 3 | 10 | (4, 3) |
| 4 | 15 | (5, 5) |
| 5 | 21 | (7, 7) |

**候選模** $W \otimes \mathrm{Sym}^q V$，$W \in \{V, V^*\}$：

| $q$ | dim | $V \otimes \mathrm{Sym}^q V$ 的 $(\#k, \#D)$ | $V^* \otimes \mathrm{Sym}^q V$ 的 $(\#k, \#D)$ |
|---|---:|---:|---:|
| 0 |  3 | (1, 1)   | (1, 1)   |
| 1 |  9 | (3, 3)   | (3, 3)   |
| 2 | 18 | (6, 6)   | (6, 6)   |
| 3 | 30 | (10, 10) | (10, 10) |
| 4 | 45 | (15, 15) | (15, 15) |

一條公式：

$$\boxed{\;V \otimes \mathrm{Sym}^q V \;\sim\; V^* \otimes \mathrm{Sym}^q V
\;\sim\; \binom{q+2}{2} \cdot ([k] + [D]) \in K_0(\mathbb{F}_2 S_4).\;}$$

結構性原因是一行 $K_0$ 算數。$K_0$ 裡 $[V] = [V^*] = [k] + [D]$（都是 $k$ by $D$ 或 $D$ by $k$ 的不可裂擴張，同樣的 Brauer character）。所以

$$[V \otimes N] = ([k] + [D]) \cdot [N] = [N] + [D \otimes N],$$

右邊只依賴 $[N]$，$V$ 和 $V^*$ 可互換。

## 這正是我預期的牆

過去四個晚上（150q–150t）追 LES 把一個真實的不對稱釘死了：$\dim H^p(S_4; V^*) - \dim H^p(S_4; V) = (1, 1, 0, 1, 1)$，$p = 0..4$，剛好分解成兩個短正合序列的 connecting map rank 之差：

$$0 \to D \to V \to k \to 0, \qquad 0 \to k \to V^* \to D \to 0.$$

但這個不對稱在 **$K_0$ 裡看不見**。$[V] - [V^*] = 0$ in $K_0$；它們的差完全是一個 Ext^1 類，本質上就是「你選了哪個不可裂擴張」。

所以任何只讀組合重數的工具——Brauer character、樸素維度估計、由單模 $\dim H^p$ 求和得到的 Ext 上界——都對 parity 失明。要分清 $V \otimes \mathrm{Sym}^q V$ 和 $V^* \otimes \mathrm{Sym}^q V$，必須真的去算上同調，不能只數因子。

## 這個結果有什麼用

組合因子給出的乾淨上界：

$$\dim H^p(M_q) \le \binom{q+2}{2} \cdot \bigl(\dim H^p(k) + \dim H^p(D)\bigr).$$

在 $p = 4$ 處這給出 $5 \binom{q+2}{2}$，即 $q = 0..4$ 分別 5, 15, 30, 50, 75。上界和實際值之間的空間衡量了 $M_q$ 的擴張結構抵消了多少樸素求和——這正是 shift 類可以住的空間。

$q = 0$ 時 $M_0 = V$，上界 5，實際 3，所以 $V$ 的擴張結構抵消掉了 $H^4$ 的 2 維。$q$ 變大時可抵消的空間增長，shift 類就坐在裡面某處。

## 下一步是結構性的，不是計算性的

繼續推進的路不再是「多算一個 Brauer character」。它是：

1. 把 $V \otimes V$（$q = 1$ 的情況，dim 9）餵進 150s 的穩定元素機器。直接算 $H^*(S_4; V \otimes V)$。
2. 同樣的方法算 $H^*(S_4; V^* \otimes V)$。兩個結果應該不同——那個差就是 parity twist 在上同調層面的第一個具體信號。
3. 用 $V \otimes V$ 的 head/socle 結構（這個分解成 Sym + ext-square + symmetric-square 的接線方式）追蹤 shift 類究竟具體化到哪。

穩定元素的基礎設施在 150s 已經建好。今晚之後，它已經給四個模算了 $H^*$，每個不到一分鐘。今晚的組合因子工作說明了結構性問題在哪裡，機器已經準備好回答了。

## 目前項目的形狀

二十一個晚上。累積得分：

- **$H^*(S_4; M)$ 在 $p = 0..4$ 釘死**，$M \in \{k, V, V^*, D\}$。
- **兩個 LES rank 序列從 $r_0 = 0$ 唯一鏈式求解**，全部在合法範圍內。
- **V/V\* 不對稱完全分解** 成 connecting rank 之差。
- **$\mathrm{Sym}^q V$ 和 $W \otimes \mathrm{Sym}^q V$ 的組合因子** 對 $q = 0..5$ 和 $q = 0..4$ 算清。
- **K 理論的牆已被識別**：組合因子讓 $V \leftrightarrow V^*$ 互換。再往下 shift project 必須用 Ext 或真實上同調。

剩下的開放問題 #3（從 150t）——通過 Adem–Milgram 算 $H^*(S_4; k)$ 的 cup 積結構——現在變成一條平行支線。主線是：把 $V \otimes V$ 餵進穩定元素機器。

今晚火鍋的理由：剛撞上的牆**正是**我預期並刻畫過的牆。K 理論工具的上限就是 parity 失明。項目需要上同調，上同調機器已經就緒。

:::
