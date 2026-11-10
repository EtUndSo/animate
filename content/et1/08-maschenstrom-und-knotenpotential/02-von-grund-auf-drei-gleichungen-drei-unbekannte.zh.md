---
title: 从头开始：三个方程，三个未知量
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 网孔电流法与节点电位法
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: 第 8 章：网孔电流法与节点电位法
order: 1180200
summary: 为什么一个网络只需很少的未知量
tags: 对称, 电导
lang: zh
---

两种方法最后都得到一个线性方程组 $\mathbf M\,\mathbf x=\mathbf b$，即矩阵乘以列向量（[第 6 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)）。$\mathbf x$ 包含未知量，$\mathbf b$ 是已知的右端。矩阵的每一行是一个方程，每一列对应一个未知量。对两个未知量，行列式 $\det\mathbf M=a\,d-b\,c$ 已经熟悉。对三个未知量，沿第一行展开。每个数乘以划去其所在行和列后剩下的行列式，符号交替（$+,-,+$）：

<span class="anker" id="gl-0-1"></span>
$$\det\begin{pmatrix}a&b&c\\d&e&f\\p&q&r\end{pmatrix}=a\,(e\,r-f\,q)-b\,(d\,r-f\,p)+c\,(d\,q-e\,p). \tag{0.1}$$

:::satz 定理 0.1 (克莱姆法则)
<span class="anker" id="satz-0-1"></span>

若 $D=\det\mathbf M\neq0$，则 $\mathbf M\,\mathbf x=\mathbf b$ 恰有一个解。其第 $i$ 个分量为

<span class="anker" id="gl-0-2"></span>
$$x_i=\frac{D_i}{D}. \tag{0.2}$$

$D_i$ 是把第 $i$ 列换成 $\mathbf b$ 后所得矩阵的行列式。
:::

:::herleitung 两个未知量时的克莱姆法则
由 $a\,x+b\,y=e$ 和 $c\,x+d\,y=f$ 消去 $y$：第一个方程乘以 $d$，减去第二个方程乘以 $b$，得 $(a\,d-b\,c)\,x=e\,d-b\,f$。左边是 $D\,x$，右边是第 1 列为 $(e,f)$ 的行列式。未知量更多时做法相同。
:::

例：$2x+y=5$ 和 $x+3y=5$ 有 $D=5$，$D_1=10$，$D_2=5$，所以 $x=2$，$y=1$。这条法则适合手算约四个以内的未知量，尤其是矩阵含有许多零的时候。如果矩阵关于主对角线（从左上到右下）镜像后不变，就称为__对称__矩阵。__电导__ $G=1/R$（[第 2 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）的单位是西门子：$1\,\mathrm{mS}=1/\mathrm{k\Omega}$。
