---
title: 第 3 阶段：由电场和碰撞得出欧姆定律
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电流、电阻与基尔霍夫定律
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: 第 2 章：电流、电阻与基尔霍夫定律
order: 1120400
summary: 第 2 阶段表明：漂移与电场成正比。本阶段用几步就由此得出电路技术中最重要的定律。
tags: 电导率, 电阻率, 电导, 线性, 均匀, 功率
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
第 [2](langsame-elektronen-sofortiger-strom.html#stufe-2) 阶段表明：漂移与电场成正比。本阶段用几步就由此得出电路技术中最重要的定律。
:::

**基本思路。** 电压越高，导体中的电场越强；电场越强，漂移越快；漂移越快，电流越大。每一步都是正比关系，所以从 $U$ 到 $I$ 的全过程也是。比例因子包含材料和形状（图 [4](#abb-4)）。

:::abbildung et1/k2ohm 4
左：长度为 $L$、横截面积为 $A$ 的导体。电场 $E$ 和电流密度 $j$ 处处相同。右：参考模型中的特性曲线。$I$ 随 $U$ 的变化是一条过原点的直线，其斜率是电导 $G=\Delta I/\Delta U$，即 $R=\Delta U/\Delta I$ 的倒数。图中的点对应 9 V 加在 $R_1+R_2=3\,\mathrm{k\Omega}$ 上。
:::

:::satz 定理 3.1 (欧姆定律)
<span class="anker" id="satz-3-1"></span>

对电子密度为 $n$ 的导体，有

<span class="anker" id="gl-3-1"></span>
<span class="anker" id="gl-3-2"></span>
$$\begin{aligned} \vec j&=\sigma\,\vec E,\qquad\sigma=n\,e\,\mu,\qquad\rho=\frac1\sigma,\\ U&=R\,I,\qquad R=\frac{L}{\sigma\,A}=\rho\,\frac LA,\qquad G=\frac1R=\frac IU. \end{aligned} \tag{3.1|3.2}$$
:::

⁠**如何理解：**$\sigma$ 是__电导率__，单位为 S/m；$\rho$ 是__电阻率__，单位为 $\Omega\,\mathrm m$。它也常用 $\Omega\,\mathrm{mm^2/m}$ 表示，这时铜为 0.017。$R$ 是电阻，单位为 $\Omega$（欧姆），$1\,\Omega=1$ V/A：导线中是 m$\Omega$ 量级，电路中是 k$\Omega$ 量级。它的电路符号是一个矩形（图 [6](zweipole-und-zahlpfeile.html#abb-6)）。$G$ 是__电导__，单位为 S（西门子），$1\,\mathrm{S}=1\,\Omega^{-1}$。这些单位以 Georg Simon Ohm 和 Werner von Siemens 的名字命名。**适用条件：**导体必须是__线性__的（$\vec j$ 与 $\vec E$ 成正比）和__均匀__的（处处是同一种材料）。温度必须恒定（第 [4](reale-widerstande-werte-und-temperatur.html#stufe-4) 阶段），并且必须满足 $L\gg\sqrt A$，使两端的电场不起作用。线性关系在金属中非常精确地成立：飞行时间 $T$ 与 $E$ 无关，因为漂移比无序运动小 $10^{9}$ 倍以上。

:::herleitung 从电场到元件
电子的电流密度（第 [1](strom-ist-bewegte-ladung.html#stufe-1) 阶段），代入 $q=-n\,e$ 和式 [(2.1)](langsame-elektronen-sofortiger-strom.html#gl-2-1)：

$$\vec j=q\,\vec v_\mathrm D=(-n\,e)(-\mu\,\vec E)=n\,e\,\mu\,\vec E=\sigma\,\vec E.$$

电场是均匀的，所以 $U=E\,L$（[第 1 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。于是

$$I=j\,A=\sigma\,E\,A=\frac{\sigma\,A}{L}\,U\quad\Longrightarrow\quad U=\frac{L}{\sigma\,A}\,I=R\,I.$$
:::

| 导体 | $\rho$（$10^{-8}\,\Omega\,\mathrm m$） | $\sigma$（$10^{6}$ S/m） | 导体 | $\rho$（$10^{-8}\,\Omega\,\mathrm m$） | $\sigma$（$10^{6}$ S/m） |
|---|---|---|---|---|---|
| 银 | 1.6 | 62 | 黄铜 | 7 至 9 | 14 至 11 |
| 铜 | 1.7 | 59 | 铁 | 10 至 15 | 10 至 7 |
| 金 | 2.3 | 43 | 铂 | 11 | 9 |
| 铝 | 2.8 | 36 | 康铜 | 50 | 2 |
| 钨 | 5.5 | 18 | 碳 | 5000 至 10000 | 0.02 至 0.01 |

::::beispiel
这根导线的电阻为 $R=\rho\,L/A=34\,\mathrm{m\Omega}$。在 3 mA 时，它上面的压降为 0.10 mV，是 9 V 的 $1.1\cdot10^{-5}$。这说明了为什么电路图把导线画成理想的，沿导线没有电压。同样的计算也说明了为什么电阻器不用铜制作：横截面积为 $0.01\,\mathrm{mm^2}$ 时，$2\,\mathrm{k\Omega}$ 需要 1.2 km 的铜，而康铜只需 40 m。
::::

⁠**极限情况：**电压不变时长度加倍，电场减半，电流也减半。横截面积加倍相当于两根并排的导线，电流加倍。$U=0$ 时 $I=0$。

**能量去了哪里。** 每次碰撞时，电子把在电场中获得的动能交给晶格。晶格振动加剧，这就是热。每库仑电荷释放能量 $U$（以焦耳计），每秒通过 $I$ 库仑。因此，__功率__（单位时间的能量）为 $P=U\,I=R\,I^2$。串联链转换的功率为 $9\,\mathrm{V}\cdot3\,\mathrm{mA}=27$ mW。[第 7 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)将更详细地讨论功率。

:::frage $R=U/I$ 总是可以算出来。那欧姆定律还说了什么？
任何元件都有商 $U/I$。定律说的更多：这个商是**恒定**的，与 $U$ 无关。这是关于材料的陈述，源于固定的飞行时间。对白炽灯它不成立（第 [4](reale-widerstande-werte-und-temperatur.html#stufe-4) 阶段）。
:::

:::aufgabe 练习 3 ★★ 由几何尺寸求电阻
<span class="anker" id="aufg-3"></span>

一条供电线路由去线和回线组成，每根都是 20 m 长、横截面积为 $1.5\,\mathrm{mm^2}$ 的铜线。

<ol class="al">

<li>

计算它的电阻以及 16 A 时它上面的压降。

</li>

<li>

若用铝，要得到相同的电阻需要多大的横截面积？

</li>

<li>

预测：把一根导线拉长到两倍，体积不变。$R$ 变为原来的多少倍？

</li>

</ol>

:::loesung
(a) $R=\rho\cdot40\,\mathrm{m}/1.5\,\mathrm{mm^2}=0.453\,\Omega$。压降为 $0.453\,\Omega\cdot16\,\mathrm{A}=7.3$ V，是 230 V 的 3.2 %。 (b) $R$ 相同意味着 $\rho/A$ 相同：$A_\mathrm{Al}=1.5\,\mathrm{mm^2}\cdot2.8/1.7=2.5\,\mathrm{mm^2}$。 (c) 体积 $L\,A$ 不变：$L\to2L$ 迫使 $A\to A/2$。所以 $R\to4R$。
:::
:::
