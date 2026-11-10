---
title: 第 1 阶段：作为特征函数的振荡
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 傅里叶级数与变换
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: 第 3 章：傅里叶级数与变换
order: 3230200
summary: 在基本单元 e pt 中，从现在起只使用纯振荡。本阶段说明 LTI 系统对它们起什么作用。
tags: 频率响应
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
在基本单元 $\mathrm{e}^{pt}$ 中，从现在起只使用纯振荡。本阶段说明 LTI 系统对它们起什么作用。
:::

当 $p=\mathrm{j}2\pi f$ 为纯虚数时，基本单元变成幅度恒定的振荡：

$$\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft).$$

与每个基本单元一样，它是每个 LTI 系统的特征函数（延迟就是乘以 $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$）：

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft},\qquad H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t. \tag{1.1}$$

$H(f)$ 称为__频率响应__或传递函数。它的模表示频率为 $f$ 的振荡被放大或衰减的程度，它的相位表示该振荡被移动了多少。两个系统级联时，依次相乘：$H(f)=H_1(f)H_2(f)$。若拉普拉斯变换 $H(p)$ 在虚轴上存在，则 $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$。

⁠**简而言之：**频率响应就是 LTI 系统乘到纯振荡上的那个数。
