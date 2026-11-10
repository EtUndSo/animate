---
title: 第 5 阶段：结构类型与自放电
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电容器
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: 第 3 章：电容器
order: 1130600
summary: 100 µF 的空气平行极板将有 3.4 公顷大。实际的电容器通过 A 、 d 和 varepsilon 解决这个问题。每种结构都要为此付出各自的代价。
tags: 电解液, 有极性, 自愈, 漏电流, 绝缘电阻
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
100 µF 的空气平行极板将有 3.4 公顷大。实际的电容器通过 $A$、$d$ 和 $\varepsilon$ 解决这个问题。每种结构都要为此付出各自的代价。
:::

**基本思路。** 式 [(4.1)](plattenkondensator-und-dielektrikum.html#gl-4-1) 有三个调节手段，所有结构类型都在利用它们（图 [5](#abb-5)）。

<ul>

<li>

⁠**薄膜电容器：**两条长金属带，中间用塑料薄膜或纸隔开，卷成一卷。这样就在很小的空间里得到很大的面积。

</li>

<li>

⁠**陶瓷电容器：**$\varepsilon_\mathrm{r}$ 很大的陶瓷，常做成许多层相互叠放的薄层，并联在一起（第 [7](parallel-und-reihenschaltung.html#stufe-7) 阶段）。代价：$\varepsilon_\mathrm{r}$ 随电压和温度变化。

</li>

<li>

⁠**电解电容器：**电极是经过粗糙化处理的铝箔。这增大了 $A$。电介质是只有几十纳米厚的氧化层，这使 $d$ 很小。对电极是一种导电液体，即__电解液__，因为只有它才能贴合每一处凹陷。代价：电解电容器__有极性__，氧化层只能承受一个方向的电压。接反时氧化层被破坏，有电流流过，元件发热，并可能爆裂。

</li>

<li>

⁠**超级电容（也称 Goldcap）：**在内表面积极大的多孔碳电极上，电解液的离子聚集在约 1 nm 的距离处。这样可得到 100 F 甚至更大的电容。代价：电压只有几伏，超过时电解液分解，而且漏电流相对较大。

</li>

</ul>

:::abbildung et1/k3bauform 5
获得大电容的四种途径，示意性剖面图，未按比例绘制。红色和蓝色是两个电极；电解电容器中，橙色是铝上的氧化层，浅蓝色是电解液。超级电容中，离子紧贴碳表面。
:::

| 结构类型 | 电容 | 电压 | 尺寸 | 有极性 | 自愈 |
|---|---|---|---|---|---|
| 纸介、金属化纸介 | 100 pF 到 50 µF | 125 V 到 1 kV | 大 | 否 | 仅金属化型 |
| 塑料薄膜 | 2 pF 到 200 µF | 50 V 到 5 kV | 中到很小 | 否 | 仅金属化型 |
| 陶瓷 | 0.5 pF 到 100 µF | 6 V 到 1 kV | 小 | 否 | 否 |
| 电解 | 0.5 µF 到 10 mF | 3 V 到 650 V | 很小 | 是 | 是 |
| 超级电容 | 0.1 F 到 100 F 以上 | 几伏 | 很小 | 是 | 否 |

上表汇总了常见的范围。__自愈__的意思是：发生击穿时，缺陷周围的金属薄层蒸发，短路消失，只损失极小的面积。电解电容器则在缺陷处重新生成氧化层。

**自放电。** 没有完美的绝缘体。电介质中含有少量可移动的电荷，因此有微小的电流从一块极板流到另一块极板，这就是__漏电流__。在等效电路中，理想电容器上并联一个__绝缘电阻__ $R_\mathrm{I}$。理想情况下 $R_\mathrm{I}\to\infty$，断开的电容器永远保持其电荷。实际上它按 $R_\mathrm{I}\,C$ 的节奏释放电荷（第 [10](entladen-und-zeitkonstante.html#stufe-10) 阶段）。利用材料的电阻率 $\rho$（[第 2 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)），有 $R_\mathrm{I}=\rho\,d/A$，再结合式 [(4.1)](plattenkondensator-und-dielektrikum.html#gl-4-1) 得

<span class="anker" id="gl-5-1"></span>
$$R_\mathrm{I}\,C=\rho\,\varepsilon. \tag{5.1}$$

$A$ 和 $d$ 相互抵消：自放电只取决于材料，与元件尺寸无关。

::::beispiel
$\rho\approx10^{16}\,\Omega\,$m、$\varepsilon_\mathrm{r}=2.2$ 的塑料薄膜给出约两天。对于 9 V 下的 100 µF 电解电容器，数据手册给出的漏电流最大约为 9 µA，即 $R_\mathrm{I}\approx1\,\mathrm{M\Omega}$。这是 RC 电路中 $R$ 的 100 倍，漏电流只有 0.9 mA 的 1 %，在后面的阶段中忽略不计。
::::

⁠**极限情况：**当 $\rho\to\infty$ 时 $R_\mathrm{I}\,C$ 无限增大，这就是没有自放电的理想电容器。

:::frage 为什么不总是选用电容最大的结构？
因为每种结构都有代价。电解电容器有极性，容差也大；超级电容只能承受几伏电压。在电压会改变符号或电容必须准确的场合，要用薄膜或陶瓷电容器。
:::

:::aufgabe 练习 6 ★ 核算一个电解电容器
<span class="anker" id="aufg-6"></span>

一个 100 µF、16 V 的电解电容器，其氧化层的 $\varepsilon_\mathrm{r}=9$，厚度为每伏 1.4 nm。

<ol class="al">

<li>

氧化层有多厚？需要多大的面积？

</li>

<li>

外壳中能放下 3 cm 乘 20 cm 的铝带。粗糙化处理必须把表面积增大多少倍？

</li>

<li>

为什么光滑的金属对电极得不到这样的增益？

</li>

</ol>

:::loesung
(a) $d=16\cdot1.4\,\mathrm{nm}=22.4$ nm。$A=\dfrac{C\,d}{\varepsilon_0\varepsilon_\mathrm{r}}=\dfrac{10^{-4}\,\mathrm{F}\cdot22.4\cdot10^{-9}\,\mathrm{m}}{9\cdot8.854\cdot10^{-12}\,\mathrm{F/m}}=281\,\mathrm{cm^2}$。

(b) 铝带面积为 60 cm$^2$，因此需要因数 $281/60=4.7$。

(c) 固体对电极只能碰到粗糙表面的凸起处。凹陷处不起作用，而且那里的距离远大于氧化层的厚度。只有液体才能以距离 $d$ 贴合表面。
:::
:::
