---
title: 第 2 阶段：电阻为什么会发热
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 功率、匹配与效率
order: 1170300
summary: 在电阻中，能量离开电路。本阶段说明其机理以及由此产生的极限。
tags: 额定功率, 双曲线
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
在电阻中，能量离开电路。本阶段说明其机理以及由此产生的极限。
:::

**基本思路。** 电阻上加有电压时，其内部存在电场。电场使每个自由电子加速。经过飞行时间 $T$ 后，电子发生碰撞，又失去定向速度（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。此时它的动能传给晶格，原子振动加剧，这种振动就是热（图 [2](#abb-2)）。电子只是传递者：在电阻之后，它的漂移与之前相同，因为电流和横截面积相同。它失去了电位，却没有变快。所以全部能量都进入了晶格。漂移本身可以忽略：在 0.44 µ m/s（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）时，一个电子携带 $8.8\cdot10^{-44}$ J，而在 9 V 上它释放 $1.44\cdot10^{-18}$ J，是前者的 $1.6\cdot10^{25}$ 倍。

:::abbildung et1/k7stoss 2
单个电子的碰撞模型。飞行时，电场做的功（蓝）增长，并以动能的形式储存在电子中。碰撞时，晶格中的热量跃升 $W_1$（红）。每次碰撞之后，两条曲线一样高：一切都交给了晶格。
:::

:::satz 定理 2.1 (焦耳热与额定功率)
<span class="anker" id="satz-2-1"></span>

在电阻中，全部电功率都变成热：

<span class="anker" id="gl-2-1"></span>
$$P=U\,I=R\,I^2=\frac{U^2}{R}. \tag{2.1}$$

元件只能承受到其__额定功率__ $P_\mathrm{max}$：

<span class="anker" id="gl-2-2"></span>
$$P\le P_\mathrm{max}. \tag{2.2}$$
:::

⁠**如何理解：**小型膜式电阻的 $P_\mathrm{max}=250$ mW，暖风机转换 2 kW。公式是平方关系，因为电流起了两次作用：电流加倍意味着每秒的库仑数加倍，而由 $U=R\,I$，每库仑释放的能量也加倍。电流相同时（串联），热量随 $R$ 增大；电压相同时（并联），热量随 $R$ 减小。**适用条件：**$P=U\,I$ 总是成立，另外两种形式只适用于欧姆电阻（$R$ 与电流无关），并且 $U$ 和 $I$ 必须属于这个电阻。

:::herleitung 从碰撞到 $U^2/R$
在[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)的模型中，电子以 $a=e\,E/m_\mathrm e$ 加速，在路程 $s=\frac12a\,T^2$ 上达到 $v_\mathrm{max}=a\,T$。电场做功 $e\,E\,s=m_\mathrm e\,a\,s=\frac12m_\mathrm e(a\,T)^2=W_1$，恰好等于碰撞时的动能。体积 $A\,L$ 中有 $n\,A\,L$ 个自由电子，每个电子每秒碰撞 $1/T$ 次：

$$P=n\,A\,L\,\frac{W_1}{T}=n\,A\,L\,\frac{e^2E^2\,T}{2\,m_\mathrm e}=\sigma\,E^2\,A\,L.$$

其中 $\sigma=n\,e\,\mu$，$\mu=e\,T/(2\,m_\mathrm e)$（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。由 $U=E\,L$ 和 $R=L/(\sigma A)$ 得 $P=U^2/R$。
:::

**额定功率。** 温度不断上升，直到元件每秒向周围散发的热量等于内部产生的热量。所以功率越大，温度越高，而温度过高会损坏元件。在图 [3](#abb-3) 的图表中，极限是__双曲线__ $I=P_\mathrm{max}/U$，每个电阻是一条过原点的直线。它们的交点位于 $U_\mathrm{max}=\sqrt{P_\mathrm{max}\,R}$ 和 $I_\mathrm{max}=\sqrt{P_\mathrm{max}/R}$。

:::abbildung et1/k7grenze 3
250 mW 电阻的极限。每个阻值只能工作到双曲线为止：25 $\Omega$ 到 100 mA，100 $\Omega$ 到 50 mA，400 $\Omega$ 到 25 mA。
:::

::::beispiel
对于 100 $\Omega$ 和 250 mW，允许 $U_\mathrm{max}=5$ V，$I_\mathrm{max}=50$ mA。接在理想的 9 V 上会产生 810 mW，是极限值的 3.24 倍。需要 $R\ge(9\,\mathrm{V})^2/250\,\mathrm{mW}=324\,\Omega$。
::::

⁠**极限情况：**$R\to\infty$ 时 $P\to0$。$R\to0$ 时，在固定电压下 $P\to\infty$。只有电源的内阻能阻止这种情况（第 [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5) 阶段）。

:::frage 电热丝和引线流过相同的电流。为什么只有电热丝发红？
电流相同时，热量与 $R$ 成正比。一段 10 m$\Omega$ 的引线在 0.5 A 时只转换 2.5 mW，而 16 $\Omega$ 的负载转换 4 W，是前者的 1600 倍。在吹风机和电烙铁中，热就是目的；在线路中，它是损耗（第 [4](leitungsverluste.html#stufe-4) 阶段）。
:::

:::aufgabe 练习 2 ★★ 哪一个更热？
<span class="anker" id="aufg-2"></span>

两个电阻 100 $\Omega$ 和 300 $\Omega$，额定功率都是 250 mW，接在 12 V 上。先预测每种情况下哪一个更热。(a) 它们串联。(b) 它们并联。计算所有功率。(c) 哪里超过了额定功率？

:::loesung
(a) 串联：$I=12\,\mathrm{V}/400\,\Omega=30$ mA，由 $P=R\,I^2$ 得 90 mW 和 270 mW。较大的电阻更热：库仑数相同，而每库仑在那里释放的能量是三倍。 (b) 并联：由 $P=U^2/R$ 得 1.44 W 和 0.48 W。较小的电阻更热：每库仑的能量相同，但库仑数是三倍。 (c) 串联时 300 $\Omega$ 的电阻以 270 mW 过载，并联时两个都过载。
:::
:::
