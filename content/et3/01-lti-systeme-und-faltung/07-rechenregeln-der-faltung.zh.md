---
title: 第 6 阶段：卷积的运算规则
pfad: 电气工程 / 第 3 学期 / 信号与系统 / LTI 系统与卷积
order: 3210700
summary: 卷积在许多方面与乘法相似。每一条运算规则对系统都有其含义。
tags: 卷积乘积, 理想无失真
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
卷积在许多方面与乘法相似。每一条运算规则对系统都有其含义。
:::

卷积积分简写为__卷积乘积__ $g(t)=s(t)*h(t)$。于是式 [(4.1)](das-faltungsintegral.html#gl-4-1) 可写成 $s(t)=s(t)*\delta(t)$。

<ol class="al">

<li>

⁠**单位元。**$s*\delta=s$：狄拉克冲激扮演数字 1 的角色。$h(t)=\delta(t)$ 的系统使每个信号都原样通过，称为__理想无失真__系统。

</li>

<li>

⁠**交换律。**$s*h=h*s$。含义：输入和冲激响应可以互换角色。冲激响应为 $s$ 的系统对输入 $h$ 的响应，与系统 $h$ 对输入 $s$ 的响应完全相同。

</li>

<li>

⁠**结合律。**$(f*s)*h=f*(s*h)$。含义：两个级联的系统相当于一个系统，其冲激响应是这两个冲激响应的卷积。

</li>

<li>

⁠**分配律。**$f*(s+h)=f*s+f*h$。含义：两个并联且输出相加的系统，相当于一个冲激响应为两者冲激响应之和的系统。

</li>

<li>

⁠**复信号。**由于卷积是线性的，它可以分解为实部和虚部：

<span class="anker" id="gl-6-1"></span>
$$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h-\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h+\operatorname{Im} s*\operatorname{Re} h\bigr]. \tag{6.1}$$

</li>

</ol>

:::herleitung 交换律
作代换 $\tau'=t-\tau$，于是 $\tau=t-\tau'$，$\mathrm{d}\tau=-\mathrm{d}\tau'$。积分限 $\tau=\mp\infty$ 变为 $\tau'=\pm\infty$；交换上下限恰好抵消负号：

$$s*h=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau=\int_{-\infty}^{\infty}s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'=h*s.$$
:::

:::abbildung et3/k1bloecke 7
上：级联，冲激响应为 $h_1*h_2$（结合律）。下：并联后相加，冲激响应为 $h_1+h_2$（分配律）。
:::

:::aufgabe 练习 7 ★★ 两个 RC 电路级联
<span class="anker" id="aufg-7"></span>

两个 $RC=1$ s 的 RC 电路级联。假设第二个电路不对第一个电路构成负载（例如在两者之间接入一个电压跟随器）。

<ol class="al">

<li>

计算级联系统的冲激响应 $h*h$，其中 $h(t)=\mathrm{e}^{-t}\varepsilon(t)$。

</li>

<li>

它在何时达到最大值？它的面积是多少？

</li>

<li>

为什么需要“不构成负载”这一条件？

</li>

</ol>

:::loesung
(a) 对于 $t\ge0$：

$$(h*h)(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{e}^{-(t-\tau)}\mathrm{d}\tau=\mathrm{e}^{-t}\int_0^t\mathrm{d}\tau=t\,\mathrm{e}^{-t}.$$

因此 $h_{\text{级联}}(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$。

(b) 导数：$(1-t)\mathrm{e}^{-t}$ 在 $t=1$ s 处为零，最大值为 $\mathrm{e}^{-1}=0.368$。面积：$\int_0^\infty t\mathrm{e}^{-t}\mathrm{d} t=1=1\cdot1$（面积之积）。

(c) 如果不加解耦，第二个 RC 电路会从第一个电容中汲取电流。这时第一个电容上的电压就不再是空载 RC 电路的电压，级联系统的冲激响应也就不是 $h*h$。它仍然是一个 LTI 系统，只是冲激响应不同。把各个响应做卷积的前提是：没有哪个系统会反过来影响自己的输入。
:::
:::
