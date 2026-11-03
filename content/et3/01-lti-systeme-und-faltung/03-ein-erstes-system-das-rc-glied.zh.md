---
title: 第 2 阶段：第一个系统——RC 电路
pfad: 电气工程 / 第 3 学期 / 信号与系统 / LTI 系统与卷积
order: 3210300
summary: 借助 RC 低通滤波器（图 2），可以算出系统对两种典型输入的响应：复指数函数和阶跃。
tags: 频率响应
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
借助 RC 低通滤波器（图 [2](#abb-2)），可以算出系统对两种典型输入的响应：复指数函数和阶跃。
:::

**微分方程。** 流过 $R$ 的电流为 $(u_1-u_2)/R$。这一电流全部流入电容并为其充电，$C\,\dot u_2=(u_1-u_2)/R$。整理得：

<span class="anker" id="gl-2-1"></span>
$$RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1. \tag{2.1}$$

:::abbildung et3/k1rcschaltung 2
RC 低通滤波器：输入为 $u_1$，输出为电容两端的电压 $u_2$。参考模型中 $RC=1$ s。
:::

**输入 $\mathrm{e}^{\mathrm{j}2\pi Ft}$：输出等于一个数乘以输入。** 若施加 $u_1=\mathrm{e}^{\mathrm{j}2\pi Ft}$，则稳态时输出具有相同的形式，只是幅度和相位不同：$u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$。数 $H(F)$ 随频率变化，因此称为__频率响应__。原因在于求导不改变函数的形式，$\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi Ft}=\mathrm{j}2\pi F\,\mathrm{e}^{\mathrm{j}2\pi Ft}$。代入式 [(2.1)](#gl-2-1)：

$$H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}\,(1+\mathrm{j}2\pi FRC)=\mathrm{e}^{\mathrm{j}2\pi Ft}\quad\Longrightarrow\quad H(F)=\frac{1}{1+\mathrm{j}2\pi FRC}.$$

用相量法进行交流分析，也会得到同样的结果：电容的阻抗为 $1/(\mathrm{j}2\pi FC)$，电路是一个分压器，

$$\underline U_2=\frac{1/(\mathrm{j}2\pi FC)}{R+1/(\mathrm{j}2\pi FC)}\,\underline U_1=\frac{1}{1+\mathrm{j}2\pi FRC}\,\underline U_1.$$

相量所对应的实际电压为 $u(t)=\operatorname{Re}\{\sqrt2\,|\underline U|\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=\sqrt2\,|\underline U|\cos(2\pi Ft+\varphi)$（有效值相量）。

:::satz 定理 2.1 (RC 低通滤波器的传递函数（频率响应）)
<span class="anker" id="satz-2-1"></span>

令 $x=2\pi FRC$，则

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} \operatorname{Re}\{H\}&=\frac{1}{1+x^2},\qquad \operatorname{Im}\{H\}=\frac{-x}{1+x^2},\\ |H(F)|&=\sqrt{\operatorname{Re}\{H\}^2+\operatorname{Im}\{H\}^2}=\sqrt{H\,H^*}=\frac{1}{\sqrt{1+x^2}},\qquad \varphi(F)=-\arctan x. \end{aligned} \tag{2.2|2.3}$$
:::

⁠**如何理解：**$|H|$ 表明幅度按多大的因子缩小，$\varphi$ 表明振荡滞后多大的角度。在 $x=1$ 处，即参考模型中 $F=1/(2\pi RC)=0.16$ Hz 时，$|H|=0.707$，$\varphi=-45^\circ$。在 $x=10$ 处，$|H|=0.0995$，$\varphi=-84.3^\circ$（图 [3](#abb-3)）。**极限情况：**$F\to0$ 时 $H\to1$（电容有足够的时间充满电）；$F\to\infty$ 时 $H\to0$，且 $\varphi\to-90^\circ$（电容相当于短路）。

:::abbildung et3/k1bode 3
RC 低通滤波器传递函数的幅值和相位随 $x=2\pi FRC$ 的变化（对数坐标）。慢的振荡几乎不变地通过；快的振荡被衰减，并且滞后最多可达 $90^\circ$。
:::

**一般情况下的相位。** 对任意复数 $H=\operatorname{Re}\{H\}+\mathrm{j}\operatorname{Im}\{H\}$，有

<span class="anker" id="gl-2-4"></span>
$$\varphi=\arctan\frac{\operatorname{Im}\{H\}}{\operatorname{Re}\{H\}}+\lambda\pi+l\cdot2\pi,\qquad \lambda=\begin{cases}0&\operatorname{Re}\{H\}\ge0\\1&\operatorname{Re}\{H\}<0\end{cases},\quad l\ \text{为整数}, \tag{2.4}$$

其中 $\arctan$ 取 $[-\pi/2,\pi/2]$ 内的主值。

:::frage 为什么相位公式需要附加项 $\lambda\pi$？
$\arctan$ 只看比值 $\operatorname{Im}/\operatorname{Re}$。$1+\mathrm{j}$ 和 $-1-\mathrm{j}$ 这两个数的比值同为 1，却位于相对的两个象限。$\arctan1=45^\circ$ 对 $1+\mathrm{j}$ 是正确的。而对 $-1-\mathrm{j}$，真正的角度是 $45^\circ+180^\circ=225^\circ$，等价于 $-135^\circ$（取 $l=-1$）。只要实部为负，就必须加上 $\pi$。
:::

**阶跃输入：指数曲线。** 在 $t=0$ 时施加电压 $u_1=1$ V，此时电容未充电。对 $t\ge0$，用电流 $i$ 表示，由基尔霍夫电压定律得

$$1=R\,i(t)+\frac1C\int_0^ti(\tau)\,\mathrm{d}\tau.$$

求导得 $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$，因此 $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$，积分得

$$\ln|i|=-\frac{t}{RC}+K\quad\Longrightarrow\quad i(t)=A\,\mathrm{e}^{-t/RC},\qquad A=i(0)=\frac1R,$$

因为在最初瞬间，全部电压都加在 $R$ 上。再由基尔霍夫电压定律 $u_2=1-R\,i$ 得到

<span class="anker" id="gl-2-5"></span>
$$u_2(t)=1-\mathrm{e}^{-t/RC}\qquad(t\ge0). \tag{2.5}$$

其机理是：电容充得越满，留给 $R$ 的电压就越小，充电电流就越小，电容继续充电也就越慢。正是这种反馈使曲线呈指数形式。

:::ltspice RC 低通滤波器：阶跃响应与频率响应
⁠**绘制：**电压源 `voltage` 接在节点 `in` 上，`res` 取 `1Meg`，从 `in` 接到 `out`，`cap` 取 `1u`，从 `out` 接地，因此 $RC=1$ s。注意：SPICE 把 `1M` 读作 1 毫（milli）；兆要写成 `Meg`。

⁠**阶跃：**信号源取 `PULSE(0 1 0 1u 1u 100)`，指令为 `.tran 5`。像 `.meas tran g1 FIND V(out) AT=1` 这样的测量语句可以给出精确值；结果显示在 SPICE Error Log 中（View，SPICE Error Log）。预期结果：0.5 s 时为 0.393，1 s 时为 0.632，3 s 时为 0.950，即式 [(2.5)](#gl-2-5) 中的 $1-\mathrm{e}^{-t}$。

⁠**频率响应：**信号源的值取 `AC 1`，并用指令 `.ac dec 100 0.01 100` 代替 `.tran`。LTspice 画出以 dB 表示的幅值（实线）和相位（虚线）。在 0.159 Hz（$x=1$）处，它们显示 $-3.0$ dB（即 $|H|=0.707$）和 $-45^\circ$。把 $x=10$ 处的值与你在练习 [2](#aufg-2)(a) 中的结果比较。
:::

:::aufgabe 练习 2 ★★ 频率响应与相位
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

计算 RC 低通滤波器在 $x=0$、$1$ 和 $10$ 时的 $|H|$ 和 $\varphi$。在参考模型中，$x=10$ 对应多少 Hz 的频率？

</li>

<li>

施加信号 $u_1(t)=\cos(2\pi Ft)$，其中 $x=1$。写出 $u_2(t)$。若 $RC=1$ s，$u_2$ 滞后多少秒？

</li>

<li>

用式 [(2.4)](#gl-2-4) 求 $-1-\mathrm{j}$、$-\mathrm{j}$ 和 $-2$ 的相位。

</li>

</ol>

:::loesung
(a) $x=0$：$|H|=1$，$\varphi=0$。$x=1$：$|H|=0.707$，$\varphi=-45^\circ$。$x=10$：$|H|=0.0995$，$\varphi=-84.3^\circ$。$x=10$ 意味着 $F=10/(2\pi RC)=1.59$ Hz。

(b) $u_2(t)=0.707\cos(2\pi Ft-45^\circ)$，其中 $2\pi F=1/\mathrm s$，即 $F=0.159$ Hz。它滞后 $t_0=-\varphi/(2\pi F)=(\pi/4)/(1/\mathrm s)=0.785$ s。

(c) $-1-\mathrm{j}$：$\arctan1=45^\circ$，实部为负，因此加上 $180^\circ$：得 $225^\circ$，等价于 $-135^\circ$。$-\mathrm{j}$：实部为零，虚部为负；$\arctan(\operatorname{Im}/\operatorname{Re})$ 趋于 $-90^\circ$，所以相位为 $-90^\circ$。$-2$：$\arctan0=0$，实部为负，因此相位为 $180^\circ$。
:::
:::
