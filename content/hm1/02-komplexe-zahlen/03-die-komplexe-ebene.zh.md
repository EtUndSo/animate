---
title: 第 2 阶段：复平面
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 复数
order: 1220300
summary: 一个数对就是一个点。本阶段把复数画到平面上，并说明加法和乘以 i 在平面上的含义。
tags: 实轴, 虚轴, 纯虚数, 高斯平面
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
一个数对就是一个点。本阶段把复数画到平面上，并说明加法和乘以 $\mathrm{i}$ 在平面上的含义。
:::

**基本思路。** 把 $x$ 向右画，把 $y$ 向上画。水平的__实轴__就是 $\mathbb{R}$，竖直的__虚轴__上是__纯虚数__ $\mathrm{i}y$。每个复数是一个点，或者等价地，是一支从原点指向该点的箭头（向量）。加法按坐标分别进行：把 $z_2$ 的箭头接到 $z_1$ 的箭头尖上。两种顺序合起来构成一个平行四边形，和就是它的第四个顶点（图 [2](#abb-2)，左）。在交流电路计算中，这些箭头称为相量，电压正是这样相加的。

:::abbildung hm1/k2ebene 2
左：$z_1$、$z_2$ 和平行四边形，橙色为实轴：$z_1+z_2=4+3\mathrm{i}$ 位于向右 3 加 1、向上 1 加 2 处。右：每乘一次 $\mathrm{i}$ 就旋转 $90^\circ$。由 $z_1$ 得到正方形的各顶点，由 $1$ 得到灰色的点 $\mathrm{i}$、$-1$、$-\mathrm{i}$。
:::

:::definition 定义 2.1 (实部、虚部、高斯平面)
<span class="anker" id="satz-2-1"></span>

对 $z=x+\mathrm{i}y$（$x,y\in\mathbb{R}$），称 $x=:\operatorname{Re}(z)$ 为 $z$ 的实部，$y=:\operatorname{Im}(z)$ 为 $z$ 的虚部。以 $\operatorname{Re}(z)$ 和 $\operatorname{Im}(z)$ 为坐标的复平面也称__高斯平面__。$z=w$ 当且仅当 $\operatorname{Re}(z)=\operatorname{Re}(w)$ 且 $\operatorname{Im}(z)=\operatorname{Im}(w)$。
:::

⁠**如何理解：**实部和虚部都是实数：$3+\mathrm{i}$ 的虚部是 1，而不是 $\mathrm{i}$。所以 $\mathbb{C}$ 中的一个方程相当于两个实方程。差 $z-w$ 是从 $w$ 指向 $z$ 的箭头，因为 $w+(z-w)=z$。在参考模型中，$z_1-z_2=2-\mathrm{i}$。

:::satz 定理 2.2 (乘以 $\mathrm{i}$)
<span class="anker" id="satz-2-2"></span>

对 $z=x+\mathrm{i}y$ 有 $\mathrm{i}z=-y+\mathrm{i}x$。此时 $z$ 的箭头绕原点逆时针旋转 $90^\circ$。
:::

⁠**如何理解：**点 $(x,y)$ 变为 $(-y,x)$。旋转两次就是转半圈，也就是变号：这正是 $\mathrm{i}^2=-1$ 背后的机理。转四分之一圈就离开了数轴。所以 $\mathrm{i}$ 不可能在数轴上。

:::beweis 转四分之一圈
有 $\mathrm{i}(x+\mathrm{i}y)=\mathrm{i}x+\mathrm{i}^2y=-y+\mathrm{i}x$。$z$ 的箭头是一个直角三角形的斜边，其水平直角边为 $x$，竖直直角边为 $y$，两者都带符号。转四分之一圈后，向右的 $x$ 变为向上的 $x$，向上的 $y$ 变为向左的 $y$。所以旋转后的箭头终点为 $(-y,x)$。
:::

::::beispiel
$\mathrm{i}z_1=-1+3\mathrm{i}$，$\mathrm{i}^2z_1=-3-\mathrm{i}=-z_1$，$\mathrm{i}^3z_1=1-3\mathrm{i}$，$\mathrm{i}^4z_1=z_1$（图 [2](#abb-2)，右）。
::::

⁠**极限情况：**实因子 $r$ 不旋转，而是伸缩：$r(x+\mathrm{i}y)=rx+\mathrm{i}ry$。当 $r=-1$ 时它使箭头反向，与乘两次 $\mathrm{i}$ 相同。

:::frage 复平面不就是普通的坐标平面吗？
作为集合以及在做加法时，确实如此。区别在于乘法：式 [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) 由两个点又得到一个点，并由此可以做除法（第 [4](dividieren-und-was-verloren-geht.html#stufe-4) 阶段）。正是这一点才使平面成为一个数系。
:::

:::aufgabe 练习 2 ★★ 用数做几何
<span class="anker" id="aufg-2"></span>

已知 $P=1+\mathrm{i}$，$Q=4+2\mathrm{i}$，$R=2+4\mathrm{i}$。(a) 求以 $PQ$ 和 $PR$ 为边的平行四边形的第四个顶点 $S$。证明两条对角线有相同的中点。(b) 把 $Q$ 绕点 $P$ 逆时针旋转 $90^\circ$。提示：从 $P$ 到 $Q$ 的箭头是 $Q-P$。(c) 极限情况：当 $Q=P$ 时，你在 (b) 中得到的公式给出什么？

:::loesung
(a) 从 $P$ 出发的箭头是 $Q-P=3+\mathrm{i}$ 和 $R-P=1+3\mathrm{i}$。第四个顶点为 $S=P+(Q-P)+(R-P)=Q+R-P=5+5\mathrm{i}$。两条对角线的中点分别为 $(P+S)/2=(6+6\mathrm{i})/2=3+3\mathrm{i}$ 和 $(Q+R)/2=(6+6\mathrm{i})/2=3+3\mathrm{i}$。

(b) 把箭头 $Q-P$ 旋转后重新接到 $P$ 上：$P+\mathrm{i}(Q-P)=1+\mathrm{i}+\mathrm{i}(3+\mathrm{i})=1+\mathrm{i}-1+3\mathrm{i}=4\mathrm{i}$。(c) $P+\mathrm{i}\cdot0=P$：旋转中心保持不动。
:::
:::
