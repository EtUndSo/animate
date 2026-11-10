---
title: 第 1 阶段：无失真系统
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 低通与带通系统
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: 第 5 章：低通与带通系统
order: 3250200
summary: “好的”传输究竟应该做到什么？又用哪些特征量来衡量一个系统偏离它有多远？
tags: 相位时延, 群时延
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
“好的”传输究竟应该做到什么？又用哪些特征量来衡量一个系统偏离它有多远？
:::

**思路。** 如果信号只是变强或变弱、来得更晚，而形状相同，那么它就是无失真地到达了：

<span class="anker" id="gl-1-1"></span>
$$g(t)=h_0\,s(t-t_0)\qquad\Longleftrightarrow\qquad h(t)=h_0\,\delta(t-t_0),\qquad H(f)=h_0\,\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{1.1}$$

在频谱中，这意味着：每个振荡都乘以同一个因子 $h_0$，并且每个振荡都被平移同一段时间 $t_0$。在频率 $f$ 处，时移 $t_0$ 对应于角度 $2\pi ft_0$。因此相位 $\varphi(f)=-2\pi t_0f$ 必须是一条过原点的直线。

:::definition 定义 1.1 (LTI 系统的特征量)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-2"></span>
<span class="anker" id="gl-1-3"></span>
<span class="anker" id="gl-1-4"></span>
<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} &\text{衰减：} && a(f)=-20\lg|H(f)|\ \text{dB}\quad\text{或}\quad a(f)=-\ln|H(f)|\ \text{Np},\\ &\text{相位衰减角：} && b(f)=-\varphi(f),\\ &\text{相位时延：} && t_\mathrm p(f)=-\frac{\varphi(f)}{2\pi f},\\ &\text{群时延：} && t_\mathrm g(f)=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi(f)}{\mathrm{d} f}. \end{aligned} \tag{1.2|1.3|1.4|1.5}$$
:::

⁠**如何理解：**__相位时延__是频率为 $f$ 的单个振荡的延迟。__群时延__是一组相邻频率的延迟，也就是包络的延迟（第 [11](phasen-und-gruppenlaufzeit-beim-bandpass.html#stufe-11) 阶段）。对无失真系统，$a$、$t_\mathrm p$ 和 $t_\mathrm g$ 都是常数，且 $t_\mathrm p=t_\mathrm g=t_0$。

::::beispiel RC 电路
取 $\varphi=-\arctan(2\pi f\,RC)$ 和 $RC=1$ s：

$$t_\mathrm p=\frac{\arctan(2\pi f\,RC)}{2\pi f},\qquad t_\mathrm g=\frac{RC}{1+(2\pi f\,RC)^2}.$$

当 $f\to0$ 时，二者都等于 $RC=1$ s。在 $f=0.159$ Hz（$2\pi fRC=1$）处，$t_\mathrm p=0.785$ s，$t_\mathrm g=0.5$ s，$a=3.0$ dB。因此 RC 电路不是无失真的：它的衰减与频率有关，不同频率到达的时间也不同。
::::

:::ltspice 读出 RC 电路的衰减和时延
⁠**绘制：**RC 电路（`res` 取 `1Meg`，`cap` 取 `1u`），信号源的值取 `AC 1`，指令为 `.ac dec 100 0.01 10`。

⁠**读数：**左侧坐标轴显示以 dB 表示的 $20\lg|H|=-a$。把鼠标移到右侧坐标轴（相位）上，直到指针变成一把尺子，单击并选择“Group Delay”：这时该坐标轴显示式 [(1.5)](#gl-1-5) 中的 $t_\mathrm g(f)$。相位时延由相位算出，$t_\mathrm p=-\varphi/(2\pi f)$，其中 $\varphi$ 以弧度计。

⁠**你会看到：**频率越低，$t_\mathrm g$ 越接近 1 s。在 0.159 Hz 处读出 $a=3.0$ dB、$\varphi=-45^\circ$ 和 $t_\mathrm g=0.5$ s，由此得 $t_\mathrm p=0.785$ s。把 $2\pi fRC=10$ 处的值与你在练习 [1](#aufg-1)(b) 中的结果比较。
:::

:::aufgabe 练习 1 ★ RC 电路的时延
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

由式 [(1.5)](#gl-1-5) 推导 RC 电路的 $t_\mathrm g$。

</li>

<li>

计算 $2\pi fRC=10$ 时的 $t_\mathrm p$、$t_\mathrm g$ 和 $a$。RC 电路在哪个频率范围内近似无失真？

</li>

</ol>

:::loesung
(a) $\varphi=-\arctan(2\pi fRC)$，$\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-\frac{2\pi RC}{1+(2\pi fRC)^2}$，因此 $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}=\frac{RC}{1+(2\pi fRC)^2}$。

(b) 当 $2\pi fRC=10$ 时：$t_\mathrm p=\frac{\arctan10}{10}RC=0.147$ s，$t_\mathrm g=\frac{RC}{101}=0.0099$ s，$a=20.0$ dB。只有当 $2\pi fRC\ll1$，即频率远低于 0.16 Hz 时，RC 电路才近似无失真：在那里 $|H|\approx1$，且 $t_\mathrm p\approx t_\mathrm g\approx RC$。
:::
:::
