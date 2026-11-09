---
title: 第 4 阶段：电位满足网孔定律
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 网孔电流法与节点电位法
order: 1180600
summary: z 个电压中只有 k-1 个是自由的。本阶段说明，为什么节点的电位能担当这一角色，以及为什么网孔定律此时自动成立。
tags: 
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
$z$ 个电压中只有 $k-1$ 个是自由的。本阶段说明，为什么节点的电位能担当这一角色，以及为什么网孔定律此时自动成立。
:::

**基本思路。** 每个节点都有一个电位（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)），就像地形上的每一点都有一个高度。支路的电压是其两端的高度差。绕一圈回来，总是回到出发时的高度，不管给各节点指定了什么高度（图 [4](#abb-4)）。这样，网孔定律根本不可能被违反。由于只有差值才起作用，可以自由规定一个高度。这省掉一个未知量，剩下 $k-1$ 个。

:::abbildung et1/k8hoehen 4
把模型电路的节点看作高度。从 0 经 1 和 2 回到 0 的绕行上升 8 V 和 2 V，下降 10 V。总和为零，即使把高度 1 和 2 任意移动，总和仍为零。
:::

:::definition 定义 4.1 (参考节点与节点电位)
<span class="anker" id="satz-4-1"></span>

自由选定的节点 0 是**参考节点**，其电位为 $\varphi_0=0$。另一节点 $\mu$ 的**节点电位**是它相对于参考节点的电压：

<span class="anker" id="gl-4-1"></span>
$$U_\mu=\varphi_\mu-\varphi_0. \tag{4.1}$$

节点 $\mu$ 和 $\nu$ 之间支路的电压为 $U_{\mu\nu}=U_\mu-U_\nu$，到参考节点的支路电压为 $U_{\mu0}=U_\mu$。
:::

:::satz 定理 4.2 (节点电位)
<span class="anker" id="satz-4-2"></span>

对 $k-1$ 个节点电位的任意取值，每条网孔定律都成立。反过来，每个满足网孔定律的电压分布都恰好对应一组节点电位。
:::

:::herleitung 为什么这总是可行
⁠**网孔定律。**沿经过节点 $1,2,\dots,N$ 的网孔，有 $(U_1-U_2)+(U_2-U_3)+\dots+(U_N-U_1)=0$。每个电位出现一次 $+$ 和一次 $-$。

⁠**完备性。**选一棵树。其中参考节点到每个节点恰有一条路径。沿这条路径的支路电压之和唯一地定义了节点电位。这样，所有树支上的差值都正确。对每条连支，差值也正确，因为它与树支闭合成一个网孔，而按前提该网孔的定律成立。
:::

⁠**如何理解：**$U_\mu$ 是箭头从节点 $\mu$ 指向参考节点的电压，单位为伏特。电路图中用接地符号标出参考节点，在 SPICE 中它总是称为 0。参考节点选在汇集支路最多的地方，这样方程最短。**适用条件：**电场必须是无旋的。穿过网孔的变化磁场会破坏电位（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)），在电路中它存在于线圈里。

::::beispiel
在模型电路中 $U_1=8$ V，$U_2=10$ V，这正是第 [3](das-maschenstromverfahren.html#stufe-3) 阶段的结果。$R_3$ 上的电压为 $U_{12}=U_1-U_2=-2$ V，所以节点 2 更高，电流从 2 流向 1。由 $R_3=2\,\mathrm{k\Omega}$ 得到的正是第 [3](das-maschenstromverfahren.html#stufe-3) 阶段的 1 mA。绕行一周得 $(U_1-U_2)+U_2-U_1=0$，对任何其他一对数值也如此。
::::

⁠**极限情况：**$k=2$ 的网络只有一个节点电位。这就是并联的公共电压。

:::frage 节点电位到底是电位还是电压？
两者都是。单独的电位只有相对于零点才有数值（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。节点电位是相对于所选零点的电压，所以用符号 $U$ 表示。更换参考节点会改变所有节点电位，但不会改变任何一个支路电压。
:::

:::aufgabe 练习 5 ★ 更换参考
<span class="anker" id="aufg-5"></span>

在模型电路中选节点 2 为参考节点。(a) 下方导线和节点 1 的节点电位是多少？(b) 由此计算节点 1 与下方导线之间的电压。(c) 为什么电流都不变？

:::loesung
(a) 所有电位都降低 10 V：下方导线 $-10$ V，节点 1 $-2$ V，节点 2 0 V。

(b) $-2\,\mathrm{V}-(-10\,\mathrm{V})=8$ V，与之前相同。

(c) 电流只取决于差值，而差值不变。
:::
:::
