---
title: 第 12 阶段：离散时间带通与高通
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 低通与带通系统
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: 第 5 章：低通与带通系统
order: 3251300
summary: 数字带通和数字高通可以通过调制由低通得到。
tags: 高通
lang: zh
---

<span class="anker" id="stufe-12"></span>

:::zweck
数字带通和数字高通可以通过调制由低通得到。
:::

若离散时间低通的单位脉冲响应为实数，乘以 $2\cos(2\pi f_0n)$ 就会把它的通带搬移到 $\pm f_0$：

<span class="anker" id="gl-12-1"></span>
$$H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr],\qquad h_{\mathrm{BP}}(n)=2\cos(2\pi f_0n)\,h_{\mathrm{TP}}(n), \tag{12.1}$$

只要搬移后的各频带不重叠，该式就成立：$f_{\mathrm g,\mathrm{TP}}\le f_0\le\frac12-f_{\mathrm g,\mathrm{TP}}$。由于周期性，位于 $f_0$ 处的频带既不能接触位于 $-f_0$ 处的频带，也不能接触它在 $1-f_0$ 处的副本。一般地，对于复的低通单位脉冲响应也一样，与式 [(8.1)](komplexe-hullkurve-und-quadraturkomponenten.html#gl-8-1) 相同，有 $h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$。因子 2 对应于加倍的等效低通系统 $H_T=2H_{\mathrm{TP}}$。

__高通__是被搬移到采样率一半处（$f_0=\frac12$）的低通。在那里，频带与其镜像重合，因此只搬移一次：$H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)$。利用 $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$：

<span class="anker" id="gl-12-2"></span>
$$h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n). \tag{12.2}$$

⁠**简而言之：**把低通单位脉冲响应每隔一个值改变一次符号，就得到数字高通。

:::aufgabe 练习 11 ★ 由滑动平均得到高通
<span class="anker" id="aufg-11"></span>

滑动平均 $h_{\mathrm{TP}}=\frac13(1,1,1)$（[第 4 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)）是一个简单的低通。

<ol class="al">

<li>

按照式 [(12.2)](#gl-12-2) 构造 $h_{\mathrm{HP}}$。

</li>

<li>

计算 $f=0$ 和 $f=\frac12$ 处的 $H_{\mathrm{TP}}$ 和 $H_{\mathrm{HP}}$。这与高通相符吗？

</li>

</ol>

:::loesung
(a) $h_{\mathrm{HP}}=\frac13(1,-1,1)$。

(b) $H_{\mathrm{TP}}(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}[1+2\cos(2\pi f)]$：$|H_{\mathrm{TP}}(0)|=1$，$|H_{\mathrm{TP}}(\frac12)|=\frac13$。高通被搬移了 $\frac12$：$|H_{\mathrm{HP}}(0)|=\frac13$，$|H_{\mathrm{HP}}(\frac12)|=1$。它让变化最快的序列 $(+1,-1,+1,\dots)$ 完全通过，并把直流分量衰减到三分之一。这是一个简单的高通，但不是很陡。
:::
:::
