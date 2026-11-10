---
title: 第 1 阶段：随机过程
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 随机信号
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: 第 7 章：随机信号
order: 3270200
summary: 怎样描述一个不知道其波形的信号？设想许多同类的信号，并对它们取平均。
tags: 样本函数, 随机过程, 随机变量, 数学期望, 自相关函数
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
怎样描述一个不知道其波形的信号？设想许多同类的信号，并对它们取平均。
:::

**思路。** 在相同温度下测量许多结构完全相同的电阻的噪声，就会得到许多不同的曲线 ${}^ks(t)$，$k=1,2,\dots$（图 [1](#abb-1)）。其中每一条称为一个__样本函数__或一个实现。所有样本函数构成的设想中的总体（集合，即样本函数族）称为__随机过程__ $s(t)$。所有样本函数在某一固定时刻 $t_1$ 的取值构成一个__随机变量__ $s(t_1)$。

:::definition 定义 1.1 (集平均)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} \mathrm E\{s(t_1)\}&=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks(t_1),\qquad \mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr],\\ \varphi_{ss}(t_1,t_2)&=\mathrm E\{s(t_1)\,s(t_2)\}. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**如何理解：**$\mathrm E\{\cdot\}$ 称为__数学期望__或集平均：在同一时刻对所有样本函数取平均，也就是在图 [1](#abb-1) 中沿竖直方向取平均。取 $F[x]=x^2$，就得到均方值。__自相关函数__对两个时刻取值的乘积求平均。它表明 $t_2$ 时刻的值与 $t_1$ 时刻的值关联有多强。

:::abbildung et3/k7schar 1
一个随机过程的三个样本函数（模拟得到，均值为 1）。集平均沿竖直方向求取，即在同一个 $t_1$ 处对所有样本函数求平均（红色虚线）。时间平均沿水平方向求取，即沿着一个样本函数求平均。
:::
