---
title: 第 6 阶段：储存的能量
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电容器
order: 1130700
summary: 充电要消耗能量，因为每份新增电荷都必须克服已有的电压。本阶段计算能量有多少，以及能量之后在哪里。
tags: 能量密度
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
充电要消耗能量，因为每份新增电荷都必须克服已有的电压。本阶段计算能量有多少，以及能量之后在哪里。
:::

**基本思路。** 电压是单位电荷的能量（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。把小电荷 $\Delta q$ 从负极板移到正极板需要 $\Delta W=u\,\Delta q$。最初的电荷几乎不费能量，因为还没有电场。最后的电荷每库仑要付出全部的 $U$。平均下来，每份电荷付出 $U/2$。这就是直线 $u=q/C$ 下的面积（图 [6](#abb-6) 左）。

:::satz 定理 6.1 (电容器中的能量)
<span class="anker" id="satz-6-1"></span>

电荷为 $Q$、电压为 $U$ 的电容器储存的能量为

<span class="anker" id="gl-6-1"></span>
$$W=\int_0^Q\frac qC\,\mathrm{d} q=\frac{Q^2}{2C}=\frac12\,Q\,U=\frac12\,C\,U^2. \tag{6.1}$$

能量存在于极板之间的电场中。对平行板电容器，体积为 $V=A\,d$，有

<span class="anker" id="gl-6-2"></span>
$$W=\frac12\,\varepsilon\,E^2\cdot A\,d,\qquad w=\frac WV=\frac12\,\varepsilon\,E^2. \tag{6.2}$$

其中 $w$ 是__能量密度__，即单位体积的能量。
:::

⁠**如何理解：**$W$ 的单位为 J，$C$ 的单位为 F，$U$ 的单位为 V，$w$ 的单位为 J/m$^3$。电压以平方形式出现：电压加倍意味着电荷加倍，而这些电荷要克服加倍的电压。$q$ 是充电过程中的电荷，$Q$ 是它的最终值。**适用条件：**$C$ 恒定，没有漏电流。

:::herleitung 由力和路程求能量
电场中 $\Delta q$ 所受的力为 $F=\Delta q\,E$（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。走过极板之间的距离 $\Delta s$，需要 $\Delta W=F\,\Delta s=\Delta q\,E\,\Delta s$。由 $E\,\Delta s=u$ 得 $\Delta W=\Delta q\,u$，再由 $u=q/C$ 得 $\Delta W=\frac qC\,\Delta q$。对于很小的 $\Delta q$，所有份额之和变为积分式 [(6.1)](#gl-6-1)。

从电路方面也得到同样的结果。功率（单位时间的能量）为 $p=u\,i$（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。由 $i=C\,\mathrm{d} u/\mathrm{d} t$ 得 $W=\int u\,i\,\mathrm{d} t=C\int_0^Uu\,\mathrm{d} u=\frac12CU^2$。

⁠**从元件到电场：**把 $C=\varepsilon A/d$ 和 $U=E\,d$ 代入式 [(6.1)](#gl-6-1)，就得到式 [(6.2)](#gl-6-2)。
:::

:::abbildung et1/k3energie 6
左：六份电荷，每份 150 µC。每份需要 $u\,\Delta q$，其电压取该份中点处的值。所有矩形的面积等于 $u=q/C$ 下三角形的面积，即 $W=\frac12QU=4.05$ mJ。右：能量存在于极板之间的空间中，单位体积的能量为 $w=\frac12\varepsilon E^2$。金属内 $E=0$。
:::

**能量在哪里。** 金属不可能含有这些能量，因为金属内 $E=0$，而且电子只移动了极小的量（第 [2](die-kapazitat.html#stufe-2) 阶段）。式 [(6.2)](#gl-6-2) 说明：每立方米电场含有 $\frac12\varepsilon E^2$。这不只是一种算法，有一个实验可以说明。断开电池，把极板拉开。$Q$ 不变，$E=Q/(\varepsilon A)$ 也不变。但电场充满了更大的体积，电场能量增加了 $\frac12\varepsilon E^2A\,\Delta d$。这些能量来自克服极板间吸引力而拉动的手。每块极板只感受到另一块极板的电场，它是 $E$ 的一半，所以 $F=\frac12QE$。所做的功为 $F\,\Delta d=\frac12QE\,\Delta d=\frac12\varepsilon E^2A\,\Delta d$，恰好等于增量。光说明电场能量可以脱离电荷而存在：它把能量带过真空。

**例。** RC 电路的电容器在 9 V 下储存 $W=\frac12\cdot100\,\mu\text{F}\cdot(9\,\mathrm{V})^2=4.05$ mJ，平行极板只储存 1.20 nJ。后者有 $w=\frac12\varepsilon_0(3\,\mathrm{kV/m})^2=3.98\cdot10^{-5}$ J/m$^3$，乘以 $V=3\cdot10^{-5}\,\mathrm{m^3}$，得到同样的 1.20 nJ。100 F 的超级电容在 2.7 V 下能储存 365 J 之多，而 0.5 Ah 的 9 V 方形电池却储存 16 kJ，是 100 µF 电容器的四百万倍。电容器储存的能量很少，但释放得非常快，例如在相机闪光灯中。

⁠**极限情况：**当 $U\to0$ 时 $W\to0$，没有电场就没有能量。**检验：**$\mathrm{F\cdot V^2}=\frac{\mathrm{C}}{\mathrm V}\cdot\mathrm{V^2}=\mathrm{C\,V}=\mathrm J$。

:::frage 为什么不是 $W=Q\,U$？电压乘以电荷不就是能量吗？
当全部电荷都经过完整的电压时，$Q\,U$ 是对的。但充电时 $U$ 是最终值，电压是从零开始增长的。电池确实放出了 $Q\,U$，因为每份电荷都在完整的电压下通过它。电容器只得到一半。其余部分去了哪里，由练习 [11](aufladen-uber-einen-widerstand.html#aufg-11) 说明。
:::

:::aufgabe 练习 7 ★★★ 拉开极板
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

一个 470 µF 的电容器接在 12 V 上，然后接在 24 V 上。$W$ 各是多少？

</li>

<li>

平行极板充电到 9 V 后断开。然后把 $d$ 加倍到 6 mm。$C$、$U$、$E$ 和 $W$ 各是多少？用 $F\,\Delta d$ 检验 $W$ 的增量。

</li>

<li>

过程相同，但电池保持连接。现在 $W$ 减小了，尽管手做了功。能量到哪里去了？这里的机械功为 0.60 nJ。

</li>

</ol>

:::loesung
(a) $W=\frac12\cdot470\,\mu\text{F}\cdot(12\,\mathrm{V})^2=33.8$ mJ，24 V 时为其四倍，即 135 mJ。

(b) $Q=266$ pC 保持不变。$C=14.8$ pF，$U=Q/C=18$ V，$E=U/d=3$ kV/m，与之前相同。$W=\frac12QU=2.39$ nJ，增量为 1.20 nJ。力为 $F=\frac12QE=0.398\,\mu\text{N}$，$F\,\Delta d=0.398\,\mu\text{N}\cdot3\,\mathrm{mm}=1.20$ nJ。两者一致。

(c) $U=9$ V 保持不变。$C=14.8$ pF，$Q=133$ pC，$E=1.5$ kV/m，$W=0.60$ nJ。电场失去 0.60 nJ。此外还有来自手的 0.60 nJ。两者都流入电池，因为有 133 pC 在 9 V 下流回：$133\,\mathrm{pC}\cdot9\,\mathrm{V}=1.20$ nJ。电池被充了一点电。
:::
:::
