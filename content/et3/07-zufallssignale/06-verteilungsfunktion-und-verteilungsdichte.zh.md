---
title: 第 5 阶段：分布函数与概率密度
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 随机信号
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: 第 7 章：随机信号
order: 3270600
summary: 平均值并不能说明一切。信号取各个值的频繁程度如何？这由分布来描述。
tags: 分布函数, 概率密度函数, 量化器
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
平均值并不能说明一切。信号取各个值的频繁程度如何？这由分布来描述。
:::

:::definition 定义 5.1 (分布)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-1"></span>
$$P_s(x)=\mathrm{Prob}[s(t)\le x],\qquad p_s(x)=\frac{\mathrm{d} P_s(x)}{\mathrm{d} x},\qquad P_s(x)=\int_{-\infty}^xp_s(\xi)\,\mathrm{d}\xi. \tag{5.1}$$
:::

⁠**如何理解：**__分布函数__ $P_s(x)$（累积分布函数）是集合中信号低于门限 $x$ 的部分所占的比例（对各态历经过程：信号低于门限 $x$ 的时间所占的比例）。它从 $P_s(-\infty)=0$ 单调上升到 $P_s(\infty)=1$。__概率密度函数__ $p_s(x)$ 永不为负，面积为 1，而 $p_s(x)\,\mathrm{d} x$ 是信号落在 $x$ 与 $x+\mathrm{d} x$ 之间的概率。由它可以得到所有的一阶平均值：

<span class="anker" id="gl-5-2"></span>
$$m_s=\int x\,p_s(x)\,\mathrm{d} x,\qquad L_s=\int x^2p_s(x)\,\mathrm{d} x,\qquad\mathrm E\{F[s]\}=\int F(x)\,p_s(x)\,\mathrm{d} x. \tag{5.2}$$

::::beispiel 均匀分布
在以 $m_s$ 为中心、宽度为 $a$ 的区间内，所有取值出现的可能性都相同：$p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$。于是

$$L_s=\frac1a\int_{m_s-a/2}^{m_s+a/2}x^2\mathrm{d} x=\frac{a^2}{12}+m_s^2,\qquad\sigma_s^2=\frac{a^2}{12}.$$

参考模型中的随机数（$a=1$，$m_s=0$）的方差为 $\frac1{12}=0.0833$。
::::

**特性曲线。** 若信号通过一条特性曲线（传输特性）$y=k(x)$（带饱和的放大器、整流器、量化器），它的分布就会改变。对单调的特性曲线，每个区间的概率保持不变：

<span class="anker" id="gl-5-3"></span>
$$p_g(y)\,|\mathrm{d} y|=p_s(x)\,|\mathrm{d} x|\qquad\Longrightarrow\qquad p_g(y)=\frac{p_s(x)}{|k'(x)|},\qquad P_g\bigl(k(x)\bigr)=P_s(x)\ \ (k\ \text{单调递增}). \tag{5.3}$$

特性曲线陡峭的地方，取值被分散到较宽的范围内，概率密度随之减小。利用这一规则，可以把任意分布变换成所需的分布。例：$k(x)=(2|x|-x^2)\operatorname{sgn}x$ 把 $[-1,1]$ 上的三角分布变换为均匀分布（练习 [4](#aufg-4)）。

**量化。** __量化器__把每个值替换为 $M$ 个量化电平中最接近的那一个。若各电平均匀分布、间隔为 $\Delta$，且没有过载，则误差在 $-\frac\Delta2$ 与 $\frac\Delta2$ 之间近似均匀分布，因而方差为 $\frac{\Delta^2}{12}$。对于在全部 $M$ 个电平上均匀分布的信号（方差为 $\frac{(M\Delta)^2}{12}$），信噪比为 $M^2$，用分贝表示为 $20\lg M\approx6\,\text{dB/比特}$：8 比特时为 48 dB，16 比特时为 96 dB。

:::aufgabe 练习 3 ★ 均匀分布
<span class="anker" id="aufg-3"></span>

一个信号在 1 V 与 3 V 之间均匀分布。计算 $m_s$、$L_s$、$\sigma_s^2$ 以及信号高于 2.5 V 的概率。

:::loesung
$a=2$ V，$m_s=2$ V。$\sigma_s^2=\frac{a^2}{12}=\frac13$ V$^2$，$L_s=\frac13+4=4.33$ V$^2$。区间的四分之一位于 2.5 V 以上，因此 $\mathrm{Prob}=\frac{0.5}{2}=0.25$。
:::
:::

:::aufgabe 练习 4 ★★ 变换分布
<span class="anker" id="aufg-4"></span>

一个信号在 $[-1,1]$ 上具有三角形概率密度 $p_s(x)=\Lambda(x)$。

<ol class="al">

<li>

求 $0\le x\le1$ 时的 $P_s(x)$。

</li>

<li>

利用式 [(5.3)](#gl-5-3) 证明：$x\ge0$ 时取 $k(x)=(2x-x^2)$（并作奇延拓），就得到 $[-1,1]$ 上的均匀分布。提示：对均匀分布，$P_g(y)=\frac12+\frac y2$。

</li>

</ol>

:::loesung
(a) 当 $0\le x\le1$ 时，$P_s(x)=\frac12+\int_0^x(1-\xi)\,\mathrm{d}\xi=\frac12+x-\frac{x^2}{2}$。

(b) 根据式 [(5.3)](#gl-5-3)，必须有 $P_g(k(x))=P_s(x)$，即 $\frac12+\frac{k(x)}{2}=\frac12+x-\frac{x^2}{2}$。由此得 $k(x)=2x-x^2$。特性曲线在 $x=0$ 处陡峭（斜率为 2），那里三角形概率密度最大；在边缘处则很平缓。这样，频繁出现的值被拉开，稀少的值被挤拢。模拟得到一个高度为 0.5 的平坦直方图。
:::
:::

:::aufgabe 练习 4a ★★★ （拓展阅读）最佳量化器
<span class="anker" id="aufg-4a"></span>

一个量化器的门限为 $u_i$，量化电平值为 $v_i$（当 $u_i<x\le u_{i+1}$ 时取电平 $i$），其均方误差为 $N_q=\sum_i\int_{u_i}^{u_{i+1}}(v_i-x)^2p_s(x)\,\mathrm{d} x$。

<ol class="al">

<li>

通过对 $v_i$ 求导证明：在最佳点，$v_i$ 位于概率密度在其区间上的质心处。

</li>

<li>

通过对 $u_i$ 求导证明：在最佳点，$u_i$ 恰好位于 $v_{i-1}$ 与 $v_i$ 的正中间。

</li>

<li>

为什么对均匀分布的信号，均匀量化器是最佳的？

</li>

</ol>

:::loesung
(a) $\frac{\partial N_q}{\partial v_i}=\int_{u_i}^{u_{i+1}}2(v_i-x)p_s(x)\mathrm{d} x=0$，因此 $v_i=\dfrac{\int_{u_i}^{u_{i+1}}x\,p_s\,\mathrm{d} x}{\int_{u_i}^{u_{i+1}}p_s\,\mathrm{d} x}$，即质心。

(b) $u_i$ 既是区间 $i-1$ 的上限，又是区间 $i$ 的下限：$\frac{\partial N_q}{\partial u_i}=(v_{i-1}-u_i)^2p_s(u_i)-(v_i-u_i)^2p_s(u_i)=0$，因此 $u_i=\frac12(v_{i-1}+v_i)$。每个值被分配给电平值离它更近的那个电平。

(c) 对于恒定的概率密度，每个区间的质心就是它的中点。宽度相等、以各自中点为电平值的区间满足这两个条件，量化间隔为 $\Delta=a/M$。
:::
:::
