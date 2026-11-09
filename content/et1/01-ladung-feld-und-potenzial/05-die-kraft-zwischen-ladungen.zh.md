---
title: 第 3 阶段：电荷之间的力
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电荷、电场与电位
order: 1110500
summary: 带电体彼此施力。本阶段把“相互吸引”变成一条带数字的定律。
tags: 真空介电常数, 点电荷, 叠加
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
带电体彼此施力。本阶段把“相互吸引”变成一条带数字的定律。
:::

**基本思路。** 把一个带电小球挂在细线上，并在旁边放置第二个带异号电荷的小球（图 [4](#abb-4)）。吸引力把小球拉离竖直方向，重力把它拉回，偏转角显示出力的大小：$\tan\alpha=F/(m\,g)$。改变电荷和距离可以发现：力与两个电荷中的每一个都成正比，并与距离的平方成反比。万有引力定律式 [(1.2)](groen-kraft-und-arbeit.html#gl-1-2) 具有同样的形式，只是用电荷代替了质量。

:::abbildung et1/k1pendel 4
左：细线悬挂的小球 A 位于小球 B 旁边，力按比例绘制。重力 $m\,g=9.81$ mN、电场力 $F=2.0$ mN 和线的拉力 $F_0=10.0$ mN 相互平衡，$\alpha=11.5^\circ$。右：参考模型中的库仑力。距离加倍，力变为四分之一。
:::

:::satz 定理 3.1 (库仑定律)
<span class="anker" id="satz-3-1"></span>

相距 $r$ 的两个静止点状电荷彼此施加大小为

<span class="anker" id="gl-3-1"></span>
$$F=k\,\frac{|Q_\mathrm{A}\,Q_\mathrm{B}|}{r^2},\qquad k=\frac{1}{4\pi\varepsilon_0}=8.99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}} \tag{3.1}$$

的力。写成矢量形式，A 所受的力为（其中 $\vec r$ 由 B 指向 A）

<span class="anker" id="gl-3-2"></span>
$$\vec F_\mathrm{A}=k\,\frac{Q_\mathrm{A}\,Q_\mathrm{B}}{r^2}\cdot\frac{\vec r}{r}. \tag{3.2}$$
:::

⁠**如何理解：**$Q_\mathrm{A}$、$Q_\mathrm{B}$ 是以 C 为单位的电荷，在式 [(3.2)](#gl-3-2) 中带符号，$r$ 是以 m 为单位的距离。矢量 $\vec r/r$ 的长度为 1，只表示方向。$\varepsilon_0=8.854\cdot10^{-12}$ A s/(V m) 称为__真空介电常数__。同号电荷时 $Q_\mathrm{A}Q_\mathrm{B}>0$，$\vec F_\mathrm{A}$ 背离 B：排斥。异号电荷时它指向 B：吸引。**适用条件：**物体必须比 $r$ 小得多（__点电荷__）且静止。该定律在真空中成立，在空气中力只小 0.06 %。多个电荷各自独立地起作用，它们的力按矢量相加（__叠加__）。

:::herleitung 从实验到定律
这条定律是测量结果。各组实验分别给出 $F\sim Q_\mathrm{A}$、$F\sim Q_\mathrm{B}$、$F\sim1/r^2$ 和 $\vec F\parallel\vec r$，合起来就是 $F\sim Q_\mathrm{A}Q_\mathrm{B}/r^2$，比例系数为 $k$。若设 $F\sim1/r^{2\pm\delta}$，则 $\delta$ 的上限从卡文迪什（18 世纪）的 0.02，经麦克斯韦（19 世纪）的 $5\cdot10^{-5}$，降到 $10^{-13}$（巴特利特等，1970 年）和 $3\cdot10^{-16}$（威廉斯等，1971 年）。
:::

::::beispiel
在参考模型中，

$$F=8.99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}}\cdot\frac{10\cdot10^{-9}\,\mathrm{C}\cdot20\cdot10^{-9}\,\mathrm{C}}{(0.03\,\mathrm{m})^2}=2.0\,\mathrm{mN}.$$

小球 A 的重力为 9.81 mN，因此 $\tan\alpha=0.204$，$\alpha=11.5^\circ$。产生这一偏转的，只是每 $5\cdot10^{12}$ 个电子中缺少一个。相同距离上两个 1 g 小球之间的万有引力只有 $7.4\cdot10^{-14}$ N，比电力小 $2.7\cdot10^{10}$ 倍，可以忽略。两个电子之间的电力甚至是万有引力的 $4.2\cdot10^{42}$ 倍。
::::

⁠**极限情况：**$r\to\infty$ 时 $F\to0$。$Q_\mathrm{A}=0$ 时 $F=0$。距离加倍得 0.5 mN，电荷 $Q_\mathrm{A}$ 加倍得 4.0 mN。

:::frage 小球 B 的电荷是小球 A 的两倍。A 因此受到更大的力吗？
不是。两者受到同样的 2.0 mN，方向相反，因为在式 [(3.1)](#gl-3-1) 中两个电荷的地位相同。可以不同的是效果：较轻的小球获得的加速度更大。
:::

:::aufgabe 练习 3 ★★ 库仑力
<span class="anker" id="aufg-3"></span>

两个小金属球分别带 $+2$ nC 和 $+5$ nC，相距 2 cm。

<ol class="al">

<li>

力有多大？对每个球，力的方向如何？

</li>

<li>

距离变为三倍时结果如何？先不用计算器回答。

</li>

<li>

这两个大小相同的小球短暂接触后再放回相距 2 cm 处。现在的力有多大？总电荷不变，为什么力却变了？

</li>

</ol>

:::loesung
(a) $F=k\cdot2\,\mathrm{nC}\cdot5\,\mathrm{nC}/(2\,\mathrm{cm})^2=225$ µ N。同号电荷：每个小球都被另一个推开。 (b) 距离变为三倍，力变为九分之一：25 µ N。

(c) 现在每个小球带 $+3.5$ nC，所以 $F=k\,(3.5\,\mathrm{nC})^2/(2\,\mathrm{cm})^2=275$ µ N。力取决于电荷的乘积，而不是电荷之和：$3.5\cdot3.5=12.25$，而 $2\cdot5=10$。
:::
:::
