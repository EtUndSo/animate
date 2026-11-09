---
title: 第 2 阶段：网孔电流满足节点定律
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 网孔电流法与节点电位法
order: 1180400
summary: 要找 m 个量，由它们得出所有支路电流。本阶段说明，为什么环流能做到这一点，以及为什么节点定律此时自动成立。
tags: 窗口
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
要找 $m$ 个量，由它们得出所有支路电流。本阶段说明，为什么环流能做到这一点，以及为什么节点定律此时自动成立。
:::

**基本思路。** 设想每个独立网孔中都有一个自己的电流沿环路流动（图 [2](#abb-2)）。机理就在“环”这个字上：电流经一条支路流入节点，就经同一网孔的另一条支路流出。它不给节点带来净电流。这对每个环流、每个节点和每个数值都成立。在属于两个网孔的支路中，两个环流相互叠加。测量到的只是这个和。

:::analogie
两条环形公交线路共用一条街道。共用的街道上跑着两条线路的公交车，每条线路驶入路口后也会再驶出。这个类比到单个粒子就结束了：电子不属于任何网孔。网孔电流是计算量，真正流动的只有支路电流。
:::

:::abbildung et1/k8kreis 2
节点 1 及网孔电流 I 和 II。左：每个环流都穿过节点。右：同一情形用支路电流表示。流向节点的是 $I_\mathrm I$，流出的是 $I_\mathrm I-I_\mathrm{II}$ 和 $I_\mathrm{II}$。对所有数值，其和都为零。
:::

:::satz 定理 2.1 (网孔电流)
<span class="anker" id="satz-2-1"></span>

在 $m$ 个独立网孔的每一个中放入一个方向自由选定的**网孔电流** $I_\mu$，则支路电流为

<span class="anker" id="gl-2-1"></span>
$$I_\text{支路}=\sum_{\mu=1}^{m}\sigma_\mu\,I_\mu,\qquad\sigma_\mu=\begin{cases}+1&\text{网孔 }\mu\text{ 沿支路箭头方向，}\\-1&\text{网孔 }\mu\text{ 逆着箭头，}\\0&\text{网孔 }\mu\text{ 不含该支路。}\end{cases} \tag{2.1}$$

这时对 $I_\mu$ 的所有取值，节点定律都成立。反过来，每个满足节点定律的电流分布都可以这样表示。
:::

:::herleitung 为什么这总是可行
⁠**节点定律。**在一个网孔中，每个节点恰好与两条支路相连（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。网孔电流在节点处计入一次流入和一次流出，两者抵消。

⁠**完备性。**选一棵树。每条连支恰好闭合一个网孔，取该网孔的网孔电流等于这条连支的电流。从给定的分布中减去所有这些环流，剩余部分仍满足节点定律，并且在所有连支中为零。它只能在树中流动。但树有末端，即只有一条树支的节点。在那里，节点定律迫使电流为零。划去这条支路，重复上述步骤。剩余部分处处为零。
:::

⁠**如何理解：**$\mu$ 为网孔编号，例题中用罗马数字。方向是自由的，负值表示环流实际反向流动。**适用条件：**各网孔必须独立。如果网络可以画成没有交叉的形式，就选__窗口__，即支路之间的区域。从树开始构造时，每条新连支恰好把一个区域分成两个，所以恰好有 $m$ 个窗口。

::::beispiel
如果在模型电路中把电流源和 $R_5$ 合并为一条带电压源的支路（第 [3](das-maschenstromverfahren.html#stufe-3) 阶段），就剩下三个窗口 I、II、III，网孔电流均为顺时针。由此得出全部五个支路电流：

| 支路 | 左，$R_1$ | $R_2$ | $R_3$ | $R_4$ | 右，$R_5$ |
|---|---|---|---|---|---|
| 电流 | $I_\mathrm I$ | $I_\mathrm I-I_\mathrm{II}$ | $I_\mathrm{II}$ | $I_\mathrm{II}-I_\mathrm{III}$ | $I_\mathrm{III}$ |

在节点 1 处得 $I_\mathrm I-(I_\mathrm I-I_\mathrm{II})-I_\mathrm{II}=0$，无论这些电流取什么值。
::::

⁠**极限情况：**$m=1$ 时，网孔电流就是串联电路的电流。$I_\mathrm{II}=0$ 时，$R_3$ 中的电流消失，左右两半不交换任何电流。

:::frage $R_2$ 支路中的电流表测到的是 $I_\mathrm I$ 还是 $I_\mathrm{II}$？
都不是，而是支路电流 $I_\mathrm I-I_\mathrm{II}$。网孔电流只有在单独流过的地方才能直接测量，这里例如 $R_1$ 中的 $I_\mathrm I$。这就是树的思想：网孔电流是只属于该网孔的那条支路的电流。
:::

:::aufgabe 练习 2 ★ 从网孔电流到支路电流
<span class="anker" id="aufg-2"></span>

两个网孔共用竖直电阻 $R_\mathrm g=3\,\mathrm{k\Omega}$，网孔 a 在它左边，网孔 b 在它右边。此外，a 只含一个电源和 $R_\mathrm a=2\,\mathrm{k\Omega}$，b 只含一个电源和 $R_\mathrm b=1\,\mathrm{k\Omega}$。两个网孔电流都是顺时针，$I_\mathrm a=3$ mA，$I_\mathrm b=-1$ mA。

<ol class="al">

<li>

$R_\mathrm g$ 中沿 $I_\mathrm a$ 方向的电流是多大？

</li>

<li>

在 $R_\mathrm g$ 的上端检验节点定律。

</li>

<li>

每个网孔中的电源必须沿绕行方向提供多大的电压？

</li>

</ol>

:::loesung
(a) 在公共支路中，两个顺时针环路彼此反向：$I_\mathrm a-I_\mathrm b=3-(-1)=4$ mA，沿 $I_\mathrm a$ 的方向。

(b) $R_\mathrm g$ 竖直位于两个网孔之间时，在上端 $I_\mathrm a$ 流向节点，$I_\mathrm b$ 离开节点。流出的是向下的 $I_\mathrm a-I_\mathrm b$ 和向右的 $I_\mathrm b$：$3-4-(-1)=0$。

(c) 网孔 a：$R_\mathrm a\,I_\mathrm a+R_\mathrm g\,(I_\mathrm a-I_\mathrm b)=6+12=18$ V。网孔 b：$R_\mathrm b\,I_\mathrm b+R_\mathrm g\,(I_\mathrm b-I_\mathrm a)=-1-12=-13$ V。所以 b 中的电源以 13 V 沿逆时针方向驱动。
:::
:::
