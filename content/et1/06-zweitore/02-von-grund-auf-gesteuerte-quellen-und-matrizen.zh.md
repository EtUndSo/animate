---
title: 从头开始：受控源与矩阵
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 二端口网络
order: 1160200
summary: 为什么四个数就能代替整个网络， 以及每种参数形式都只是另一种选择
tags: 受控源, 矩阵, 行列式, 逆矩阵, 单位矩阵
lang: zh
---

[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)的理想电源提供固定的值。__受控源__提供的值与电路中别处的另一个电压或电流成正比。它的电路符号是菱形。这些缩写来自英语（voltage 或 current controlled voltage 或 current source）。

| 名称 | 缩写 | 定律 | 系数 |
|---|---|---|---|
| 电压控制电压源 | VCVS | $U=\mu\,U_\mathrm{s}$ | 无单位 |
| 电流控制电压源 | CCVS | $U=r\,I_\mathrm{s}$ | 单位 $\Omega$ |
| 电压控制电流源 | VCCS | $I=g\,U_\mathrm{s}$ | 单位 S |
| 电流控制电流源 | CCCS | $I=\beta\,I_\mathrm{s}$ | 无单位 |

下标 s 表示控制量。最著名的例子是双极型晶体管（[第 10 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)）：小的基极电流控制大的集电极电流。所需能量来自电源电压，控制信号只提供信息。控制量和受控源本身位于电路的不同位置，因此每个受控源本质上都是二端口网络。

__矩阵__是矩形的数表，这里几乎总是两行两列。粗体字母表示矩阵以及由两个量组成的列。相乘时，左边矩阵的每一行与右边矩阵的每一列逐元素相乘，然后相加：

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}a\,x+b\,y\\c\,x+d\,y\end{pmatrix},\qquad \begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}e&f\\g&h\end{pmatrix}=\begin{pmatrix}a\,e+b\,g&a\,f+b\,h\\c\,e+d\,g&c\,f+d\,h\end{pmatrix}.$$

两个矩阵相乘时，顺序很重要。矩阵相加时逐元素相加。数 $\det\mathbf M=a\,d-b\,c$ 称为__行列式__。它不为零时，存在__逆矩阵__，由它可从 $\mathbf y=\mathbf M\,\mathbf x$ 解出 $\mathbf x$：

$$\mathbf x=\mathbf M^{-1}\mathbf y,\qquad \mathbf M^{-1}=\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac{1}{a\,d-b\,c}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$

乘积 $\mathbf M\,\mathbf M^{-1}$ 是__单位矩阵__ $\mathbf 1$，对角线上为 1，其余为 0。任何量与它相乘都不变。
