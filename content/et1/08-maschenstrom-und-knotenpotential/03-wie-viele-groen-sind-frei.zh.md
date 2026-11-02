---
title: 第 1 阶段：有多少个量是自由的？
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 网孔电流法与节点电位法
order: 1180300
summary: 第 2 部分说明，网络有 2z 个未知量和 2z 个方程。本阶段说明，为什么计算时只需两个小得多的数。
tags: 
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)说明，网络有 $2z$ 个未知量和 $2z$ 个方程。本阶段说明，为什么计算时只需两个小得多的数。
:::

**基本思路。** 一棵树（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）用 $k-1$ 条支路连接所有节点，其余 $m=z-k+1$ 条支路是连支。知道了树支的电压，就知道了所有电压：每条连支与树支恰好闭合一个网孔，网孔定律给出它的电压。知道了连支的电流，就知道了所有电流：在树的末端，一条树支单独处在连支之间，节点定律给出它的电流，然后逐条支路继续下去。所以 $z$ 个电流中只能给定 $m$ 个，$z$ 个电压中只能给定 $k-1$ 个。

:::satz 定理 1.1 (网络的自由量)
<span class="anker" id="satz-1-1"></span>

连通网络的 $z$ 个支路电流必须满足 $k-1$ 个独立的节点方程，$z$ 个支路电压必须满足 $z-k+1$ 个独立的网孔方程。因此，

<span class="anker" id="gl-1-1"></span>
$$m=z-k+1\ \text{个电流}\qquad\text{和}\qquad k-1\ \text{个电压} \tag{1.1}$$

可以自由选取。其余所有电流和电压都由基尔霍夫定律得出。
:::

⁠**如何理解：**“可以自由选取”的意思是：给定这些值不会违反任何一条基尔霍夫定律。$z$ 像[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)一样计数支路，在英文书籍中这个数常记作 $b$（取自 **branch**）。**适用条件：**这一计数只取决于图，与元件无关。它对非线性元件也成立。

:::abbildung et1/k8netz 1
模型电路。三个节点（红色），六条支路。左边的支路包含串联的电池和 $R_1$，因为两者之间没有分支。节点 0 是整条下方导线。
:::

**例。** 图 [1](#abb-1) 中的网络 $k=3$，$z=6$，所以 $m=4$：

| 做法 | 未知量 | 方程 |
|---|---|---|
| 所有电流和电压 | 12 | 6 个元件，2 个节点，4 个网孔 |
| 代入欧姆定律 | 6 | 2 个节点，4 个网孔 |
| 网孔电流 | 4 | 4 个网孔；电流源确定一个值，剩下 3 个 |
| 节点电位 | 2 | 2 个节点 |

⁠**极限情况：**串联成环时 $z=k$，$m=1$：处处是同一个电流，这正是串联的核心。并联时 $k=2$，$k-1=1$：处处是同一个电压，这正是并联的核心。

:::frage 还能用更少的未知量吗？
不改变网络就不行，因为 $m$ 和 $k-1$ 恰好计数了可以给定的量。但可以事先化简。如果合并串联和并联（[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)），$z$ 和 $k$ 就会减小。这时计数对较小的网络成立。
:::

:::aufgabe 练习 1 ★ 计数
<span class="anker" id="aufg-1"></span>

写出 $k$、$z$、$m$ 和 $k-1$。

<ol class="al">

<li>

[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)的电桥：电源和五个电阻接在四个节点之间。

</li>

<li>

五个节点，每两个节点之间都用一个电阻相连。

</li>

<li>

模型电路，把电流源和 $R_5$ 合并为一条支路之后。

</li>

<li>

由六个元件构成的环。

</li>

</ol>

:::loesung
(a) $k=4$，$z=6$，$m=3$，$k-1=3$。(b) $k=5$，$z=10$（10 对节点各一条），$m=6$，$k-1=4$。(c) $k=3$，$z=5$，$m=3$，$k-1=2$。(d) $k=6$，$z=6$，$m=1$，$k-1=5$。
:::
:::
