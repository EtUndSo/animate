---
title: 本章要点
pfad: 计算机科学 / 机器学习 / 数学基础 / 导数、梯度与链式法则
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: 第 3 章：导数、梯度与链式法则
nachschlagen: ja
order: 15231300
summary: 一个数如何响应它的输入： 从切线到反向模式
tags: 
lang: zh
---

:::kern 本章要点
<ul>

<li>

导数：$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$；在 $x$ 附近，$f(x+h)\approx f(x)+f'(x)h$，其误差比 $h$ 更快地趋于零。加上二阶导数：$f(x+h)\approx f(x)+f'(x)h+\tfrac12f''(x)h^2$。

</li>

<li>

链式法则：$(f\circ g)'(x)=f'(g(x))\,g'(x)$；对长链，是所有因子之积。逻辑斯谛函数：$\sigma'=\sigma(1-\sigma)\le\tfrac14$。

</li>

<li>

梯度 $\nabla f\in\mathbb{R}^d$ 写成列；若 $f$ 可微，则 $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$；仅有偏导数还不够。

</li>

<li>

方向导数 $D_{\mathbf{u}}f=\nabla f^{\top}\mathbf{u}$；最速上升沿 $\nabla f$ 的方向，斜率为 $\lVert\nabla f\rVert$（柯西-施瓦茨）；$\nabla f$ 垂直于等高线；只有等高线为圆时，$-\nabla f$ 才指向最低点。

</li>

<li>

雅可比矩阵 $\mathbf{J}_{\mathbf{g}}\in\mathbb{R}^{m\times n}$，每个输出一行：$\mathbf{g}(\mathbf{x}+\mathbf{h})\approx\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}\mathbf{h}$；对 $\mathbf{A}\mathbf{x}+\mathbf{b}$，它就是 $\mathbf{A}$，对逐元素函数，它是对角矩阵。

</li>

<li>

链式法则：$\mathbf{J}_{\mathbf f\circ\mathbf{g}}=\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}$，按分量是对所有路径的求和；$\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$。

</li>

<li>

$\nabla(\mathbf{a}^{\top}\mathbf{x})=\mathbf{a}$，$\nabla(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$，$\nabla\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$，$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}$；反向通过 $\mathbf{y}=\mathbf{A}\mathbf{x}$，其中 $F=f(\mathbf{A}\mathbf{x})$：$\nabla_{\mathbf{A}}F=\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$，$\nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\nabla f(\mathbf{y})$。

</li>

<li>

黑塞矩阵 $\mathbf{H}_f$，由施瓦茨定理是对称的；$f(\mathbf{x}+\mathbf{h})\approx f+\nabla f^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$；沿方向 $\mathbf{u}$ 的曲率为 $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$，介于最小特征值和最大特征值之间。

</li>

<li>

计算图：基本运算，保存各值的前向计算，边上的局部导数。

</li>

<li>

前向模式：切线值，每个方向一遍（$\mathbf{J}\dot{\mathbf{x}}$）。反向模式：从 $\bar f=1$ 开始计算伴随值 $\bar a=\sum\bar b\,\partial b/\partial a$，整个梯度只需一遍，计算量为一次求值的一个小倍数，代价是内存。

</li>

<li>

数值方法：前向差分的误差 $\approx\tfrac12f''h$，中心差分的误差 $\approx\tfrac16f'''h^2$；舍入误差像 $\varepsilon_{\mathrm M}/h$ 那样增长，因此有 V 形曲线；梯度检验用相对误差，大于 $10^{-2}$ 为错，小于 $10^{-7}$ 为好。

</li>

</ul>
:::

:::merke 三句话的答案
<ol>

<li>

一个数如何响应其输入的微小变化，由它的线性近似给出：每个输入贡献它的偏导数乘以它的变化，这些贡献相加，就是与梯度的点积。

</li>

<li>

由柯西-施瓦茨不等式，对固定长度的步，这个点积在梯度方向上最大，因此梯度指向最陡的上坡方向，并垂直于等高线。

</li>

<li>

如果这个数由一长串计算步骤得出，它的导数就是雅可比矩阵的乘积，也就是对所有路径的求和；反向模式从这个数出发，用行向量计算这个乘积，因此只需单次求值计算量的一个小倍数，就能一次给出所有导数。

</li>

</ol>
:::

**一个原理贯穿所有结果。** 本章中几乎所有内容都源于一个原理：在足够接近某一点的地方，每个可微函数都是线性的。导数、梯度和雅可比矩阵就是这种线性近似；链式法则把线性近似串联起来，同时把它们的矩阵相乘；而前向模式和反向模式是给这个乘积加括号的两种方式。

| 结果 | 来源 |
|---|---|
| 导数与切线 | 唯一一条误差比 $h$ 更快趋于零的直线（第 [1](die-ableitung.html#stufe-1) 节） |
| 乘积法则 | 角上的小块 $\Delta u\,\Delta v$ 是二阶小量（第 [1.4](die-ableitung.html#stufe-1-4) 节） |
| 一元函数的链式法则 | 每一级都以自己的因子传递微小变化（第 [2](die-kettenregel.html#stufe-2) 节） |
| 梯度与切平面 | 微小变化的作用相加（第 [3](partielle-ableitungen-und-der-gradient.html#stufe-3) 节） |
| 最速上升 | 对 $\nabla f^{\top}\mathbf{u}$ 应用柯西-施瓦茨不等式（第 [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) 节） |
| 梯度垂直于等高线 | 沿等高线斜率为零（第 [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) 节和第 [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6) 节） |
| 雅可比矩阵 | 向量值函数的线性近似的矩阵（第 [5](die-jacobi-matrix.html#stufe-5) 节） |
| 链式法则作为矩阵乘积，对路径求和 | 串联起来的线性近似（第 [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6) 节） |
| 矩阵恒等式，反向法则 | 按分量写出的链式法则，采用固定的布局约定（第 [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7) 节） |
| 黑塞矩阵与曲率 | 沿直线的二阶导数，二次型的特征值（第 [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8) 节） |
| 反向模式 | 按第一条边对路径分组，重复使用部分和；从左结合（第 [9](rechengraphen.html#stufe-9) 节和第 [10](automatische-differentiation.html#stufe-10) 节） |
| 中心差分，V 形曲线 | 泰勒展开中的偶次项相互抵消；舍入误差像 $1/h$ 那样增长（第 [11](numerische-ableitung-und-gradientenprufung.html#stufe-11) 节） |
