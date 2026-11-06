---
title: 条件数
pfad: 计算机科学 / 机器学习 / 投影、特征值与矩阵分解
order: 6221300
summary: 测量数据从来都不精确，计算机在每一步都要舍入。当方程组的右边稍有错误时，解会改变多少？本节说明：由奇异值得到的一个数就给出了答案，并说明它对正规方程意味着什么。
tags: 条件数
lang: zh
---

<span class="anker" id="stufe-12"></span>

:::zweck
测量数据从来都不精确，计算机在每一步都要舍入。当方程组的右边稍有错误时，解会改变多少？本节说明：由奇异值得到的一个数就给出了答案，并说明它对正规方程意味着什么。
:::

### 一个敏感的方程组

<span class="anker" id="stufe-12-1"></span>

方程组

$$x_1+x_2=2,\qquad x_1+1.01\,x_2=2.01$$

的解为 $\mathbf{x}=(1,\,1)^{\top}$。把第二个方程的右边改变 $0.01$，变为 $2.02$，两个方程相减得 $0.01\,x_2=0.02$，所以 $x_2=2$，$x_1=0$。数据在第三位数字上的一个变化，使解移动了与解本身同样大小的量。

从几何上看，这两个方程是两条直线，它们相交于解点。这里它们几乎平行；它们的交角只有约 $0.29^\circ$。把其中一条稍微平移，交点就会沿着另一条直线移动很远（图 [28](#abb-28)）。反之，若两条直线互相垂直，交点移动的距离只等于直线平移的距离。

:::abbildung ml/k2kondition 28
同样把红色直线平移 $0.2$ 的距离（虚线），分两种情形画出。左边，红线与蓝线垂直相交，交点移动 $0.2$。右边，两直线以 $8^\circ$ 的角度相交，交点移动 $0.2/\sin8^\circ\approx1.44$。交角越小，解对数据变化的反应就越敏感。
:::

这一影响相对于这些量本身有多大？右边 $\mathbf{y}=(2,\ 2.01)^{\top}$ 的长度为 $\sqrt{4+4.0401}\approx2.8355$，见图 [29](#abb-29)；变化量 $\Delta\mathbf{y}=(0,\ 0.01)^{\top}$ 的长度为 $0.01$。所以右边的相对变化为 $0.01/2.8355\approx0.35\,\%$。解的变化为 $\Delta\mathbf{x}=(-1,\,1)^{\top}$，相对变化为 $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt2/\sqrt2=100\,\%$。相对误差被放大了约 $284$ 倍。

:::abbildung ml/k2rnormy 29
右边长度的平方，写成点积 $\mathbf{y}^{\top}\mathbf{y}$；长度为 $\sqrt{8.0401}\approx2.8355$。
:::

⁠**简而言之：**若方程组的两条直线几乎平行地相交，数据的微小变化就会使解大幅移动。

### 条件数

<span class="anker" id="stufe-12-2"></span>

这个因子从何而来？借助奇异值分解，可以精确地估计放大程度。

:::definition 定义 12.1 (条件数)
<span class="anker" id="satz-12-1"></span>

设 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 的列线性无关，即 $d_n>0$。$\mathbf{A}$ 的__条件数__为

<span class="anker" id="gl-12-1"></span>
$$\kappa(\mathbf{A})=\frac{d_1}{d_n}, \tag{12.1}$$

即最大拉伸与最小拉伸之比。
:::

总有 $\kappa(\mathbf{A})\ge1$。正交矩阵的 $\kappa=1$，因为它的奇异值全为 $1$。条件数大的矩阵称为病态的。

:::satz 定理 12.2 (误差放大)
<span class="anker" id="satz-12-2"></span>

设 $\mathbf{A}\in\mathbb{R}^{n\times n}$ 可逆，$\mathbf{A}\mathbf{x}=\mathbf{y}$，$\mathbf{y}\ne\mathbf{0}$，且 $\mathbf{A}(\mathbf{x}+\Delta\mathbf{x})=\mathbf{y}+\Delta\mathbf{y}$。则

<span class="anker" id="gl-12-2"></span>
$$\frac{\lVert\Delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert}\le\kappa(\mathbf{A})\,\frac{\lVert\Delta\mathbf{y}\rVert}{\lVert\mathbf{y}\rVert} . \tag{12.2}$$

当 $\mathbf{y}$ 沿 $\mathbf{u}_1$ 方向、$\Delta\mathbf{y}$ 沿 $\mathbf{u}_n$ 方向时，等号成立。
:::

:::beweis 误差放大
由两个方程得 $\mathbf{A}\Delta\mathbf{x}=\Delta\mathbf{y}$。由式 [(9.5)](die-singularwertzerlegung.html#gl-9-5)，$\lVert\mathbf{y}\rVert=\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\lVert\mathbf{x}\rVert$，所以 $1/\lVert\mathbf{x}\rVert\le d_1/\lVert\mathbf{y}\rVert$；并且 $\lVert\Delta\mathbf{y}\rVert=\lVert\mathbf{A}\Delta\mathbf{x}\rVert\ge d_n\lVert\Delta\mathbf{x}\rVert$，所以 $\lVert\Delta\mathbf{x}\rVert\le\lVert\Delta\mathbf{y}\rVert/d_n$。两式相乘即得式 [(12.2)](#gl-12-2)。若 $\mathbf{y}$ 沿 $\mathbf{u}_1$ 方向，则 $\mathbf{x}$ 是 $\mathbf{v}_1$ 的倍数，第一个不等式取等号；若 $\Delta\mathbf{y}$ 沿 $\mathbf{u}_n$ 方向，则 $\Delta\mathbf{x}$ 是 $\mathbf{v}_n$ 的倍数，第二个不等式取等号。
:::

因此最坏的情形是：解位于 $\mathbf{A}$ 拉伸最强的方向上，使得 $\mathbf{y}$ 相对于 $\mathbf{x}$ 很大；而误差位于 $\mathbf{A}$ 拉伸最弱的方向上，使得反解时误差被放大 $1/d_n$ 倍。

⁠**算例：**$\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1.01\end{smallmatrix}\bigr)$ 是对称矩阵，迹为 $2.01$，行列式为 $0.01$。它的特征值为

$$\lambda_{1,2}=\frac{2.01\pm\sqrt{2.01^2-0.04}}2=\frac{2.01\pm\sqrt{4.0001}}2\approx\frac{2.01\pm2.000025}2,$$

所以 $\lambda_1\approx2.005012$，$\lambda_2\approx0.004988$，都为正。由第 [9.7](die-singularwertzerlegung.html#stufe-9-7) 节，它们也是奇异值，$\kappa(\mathbf{A})\approx402$。观察到的放大倍数 $284$ 低于这个值。它没有完全达到上界，因为 $\Delta\mathbf{y}=(0,\ 0.01)^{\top}$ 并不恰好沿 $\mathbf{u}_2\approx(1,\,-1)^{\top}/\sqrt2$ 方向。对于 $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$，$\kappa=4/1=4$：相对误差至多放大为四倍。

⁠**简而言之：**条件数 $\kappa(\mathbf{A})=d_1/d_n$ 是 $\mathbf{A}^{-1}$ 能把数据的相对误差在解中放大的最大倍数。

### 条件数与行列式

<span class="anker" id="stufe-12-3"></span>

第 1 部分第 14.6 节的背景方框中有一个警告：行列式小并不意味着矩阵接近奇异。条件数衡量的正是那里所指的东西。

:::satz 定理 12.3 (到最近奇异矩阵的距离)
<span class="anker" id="satz-12-3"></span>

对于可逆矩阵 $\mathbf{A}\in\mathbb{R}^{n\times n}$，它到奇异矩阵 $\mathbf{B}$ 的最小距离 $\lVert\mathbf{A}-\mathbf{B}\rVert_2$ 等于 $d_n$。相对于大小 $\lVert\mathbf{A}\rVert_2=d_1$，这个距离为

<span class="anker" id="gl-12-3"></span>
$$\min_{\mathbf{B}\ \text{奇异}}\frac{\lVert\mathbf{A}-\mathbf{B}\rVert_2}{\lVert\mathbf{A}\rVert_2}=\frac1{\kappa(\mathbf{A})} . \tag{12.3}$$
:::

:::beweis 距离
奇异矩阵的秩至多为 $n-1$。由 $k=n-1$ 时的 Eckart–Young 定理，$\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_n$，而奇异矩阵 $\mathbf{A}_{n-1}$ 与它的距离恰好是 $d_n$。
:::

所以条件数大意味着：一个相对较小的改变就会使矩阵变成奇异的。行列式衡量的是另一回事。由练习 [29](die-singularwertzerlegung.html#aufg-29)，$|\det\mathbf{A}|=d_1\cdots d_n$，即所有拉伸之积；它取决于矩阵的大小。条件数是一个比值，把 $\mathbf{A}$ 乘以一个数时它不变：对 $c\ne0$，$\kappa(c\mathbf{A})=\kappa(\mathbf{A})$。它只衡量 $\mathbf{A}$ 把单位圆变成的那个椭圆有多扁。

⁠**算例：**第 1 部分第 14.6 节中的两个矩阵：$0.1\cdot\mathbf{I}_{10}$ 的行列式为 $10^{-10}$，但所有奇异值都是 $0.1$，$\kappa=1$；它的条件已是最好。$\operatorname{diag}(1000,\ 0.001)$ 的行列式为 $1$，但 $\kappa=1000/0.001=10^6$。对于 $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1.01\end{smallmatrix}\bigr)$，到最近奇异矩阵的距离为 $d_2\approx0.005$：把元素改变几个千分之一，它就变成奇异的。奇异矩阵 $\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ 到它的距离为 $\lVert\bigl(\begin{smallmatrix}0&0\\0&0.01\end{smallmatrix}\bigr)\rVert_2=0.01$，比最小值稍大。

⁠**简而言之：**$1/\kappa(\mathbf{A})$ 是到最近奇异矩阵的相对距离；行列式对此说明不了什么，因为它取决于矩阵的大小。

### 正规方程使条件数平方

<span class="anker" id="stufe-12-4"></span>

最佳近似解可以通过正规方程 $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ 计算，也可以通过 QR 分解 $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ 计算。在数学上，两者给出相同的结果。用舍入后的数计算时则不然，原因就在于条件数。

:::satz 定理 12.4 (格拉姆矩阵的条件数)
<span class="anker" id="satz-12-4"></span>

若 $\mathbf{A}$ 的列线性无关，则

<span class="anker" id="gl-12-4"></span>
$$\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2 . \tag{12.4}$$

而对于 QR 分解 $\mathbf{A}=\mathbf{Q}\mathbf{R}$，有 $\kappa(\mathbf{R})=\kappa(\mathbf{A})$。
:::

:::beweis 格拉姆矩阵
$\mathbf{A}^{\top}\mathbf{A}$ 是对称正定矩阵，特征值为 $d_j^2$；由第 [9.7](die-singularwertzerlegung.html#stufe-9-7) 节，这些也是它的奇异值，它们的比为 $d_1^2/d_n^2$。由于 $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$，有 $\mathbf{R}^{\top}\mathbf{R}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{A}^{\top}\mathbf{A}$；所以 $\mathbf{R}$ 与 $\mathbf{A}$ 有相同的奇异值。
:::

⁠**算例：**第 [3.7](die-beste-naherungslosung.html#stufe-3-7) 节中由面积和房间数组成的公寓矩阵，奇异值为 $d_1\approx135.02$ 和 $d_2\approx0.848$，所以 $\kappa(\mathbf{A})\approx159.3$，$\kappa(\mathbf{A}^{\top}\mathbf{A})\approx25\,367$。有两个原因使 $\kappa(\mathbf{A})$ 很大。第一是单位：面积是 $65$ 左右的数，房间数是 $2.5$ 左右的数。如果以 $10\,\mathrm m^2$ 为单位来度量面积，条件数就降到约 $18.5$。第二，两列几乎指向同一方向；它们之间的夹角只有约 $8.9^\circ$。因此，即使把两列都缩放到长度 $1$，仍然有 $\kappa\approx12.8$。换算单位并不改变拟合值 $\hat{\mathbf{y}}$：把一列除以 $10$，相应的权重就变为原来的 $10$ 倍，乘积保持不变。

⁠**简而言之：**正规方程用的是 $\kappa(\mathbf{A})^2$，QR 分解用的是 $\kappa(\mathbf{A})$；选择合适的单位可以降低条件数。

:::hintergrund 计算机与条件数
计算机通常用大约 $16$ 位有效十进制数字存储数，并在每次运算后舍入。好的方法给出的是某个问题的精确解，而这个问题的数据只在这种舍入的量级上有所改变；这样的方法称为后向稳定的。由式 [(12.2)](#gl-12-2)，结果的相对误差至多约为 $\kappa\cdot10^{-16}$：$16$ 位数字中大约损失 $\log_{10}\kappa$ 位。

通过 QR 分解（以及通过奇异值分解）的途径是后向稳定的；在残差较小时，它的误差大致按 $\kappa(\mathbf{A})$ 增长。通过正规方程的途径则不是：它用矩阵 $\mathbf{A}^{\top}\mathbf{A}$ 计算，其误差总是按 $\kappa(\mathbf{A})^2$ 增长，即使残差很小也是如此。当 $\kappa(\mathbf{A})=10^6$ 时，走这条途径大约损失 $16$ 位中的 $12$ 位，用 QR 分解大约损失 $6$ 位。对于公寓问题，$\kappa(\mathbf{A})^2\approx2.5\cdot10^4$，这还无关紧要；对于特征几乎线性相关的大数据集则不然。因此，好的软件通过 QR 分解或奇异值分解来计算最佳近似解，而不是通过正规方程，尽管正规方程对理论的描述最为简洁。
:::

:::aufgabe 练习 36 ★ 读出条件数
<span class="anker" id="aufg-36"></span>

求下列矩阵的条件数：

<ol class="al">

<li>

$\operatorname{diag}(2,\ 0.5)$ 和 $\operatorname{diag}(-3,\ 3)$；

</li>

<li>

旋转角为 $30^\circ$ 的旋转矩阵；

</li>

<li>

$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ 时的 $5\mathbf{A}$。比较 $\mathbf{A}$ 和 $5\mathbf{A}$ 的行列式。

</li>

</ol>

:::loesung
(a) $\operatorname{diag}(2,\,0.5)$ 的奇异值为 $2$ 和 $0.5$，所以 $\kappa=4$。由第 [9.7](die-singularwertzerlegung.html#stufe-9-7) 节，$\operatorname{diag}(-3,\,3)$ 的奇异值为 $3$ 和 $3$，所以 $\kappa=1$，尽管两个特征值的符号不同。

(b) 旋转矩阵是正交矩阵，它的所有奇异值都是 $1$：$\kappa=1$。

(c) $5\mathbf{A}$ 的奇异值为 $20$ 和 $5$，所以仍有 $\kappa=4$。而行列式则从 $4$ 增大到 $\det(5\mathbf{A})=25\cdot4=100$。
:::
:::

:::aufgabe 练习 37 ★★ 行列式为 1，却是病态的
<span class="anker" id="aufg-37"></span>

设 $\mathbf{A}=\bigl(\begin{smallmatrix}10&7\\7&5\end{smallmatrix}\bigr)$。

<ol class="al">

<li>

计算 $\det\mathbf{A}$ 和 $\mathbf{A}^{-1}$。求解 $\mathbf{A}\mathbf{x}=(17,\,12)^{\top}$ 和 $\mathbf{A}\mathbf{x}=(17,\ 12.1)^{\top}$。

</li>

<li>

计算 $\mathbf{y}$ 和 $\mathbf{x}$ 的相对变化及其比值。

</li>

<li>

计算 $\kappa(\mathbf{A})$，并验证式 [(12.2)](#gl-12-2)。$\mathbf{A}$ 离最近的奇异矩阵有多远？

</li>

</ol>

:::loesung
(a) $\det\mathbf{A}=50-49=1$，$\mathbf{A}^{-1}=\bigl(\begin{smallmatrix}5&-7\\-7&10\end{smallmatrix}\bigr)$。因此 $\mathbf{A}^{-1}(17,\,12)^{\top}=(85-84,\ -119+120)^{\top}=(1,\,1)^{\top}$，$\mathbf{A}^{-1}(17,\ 12.1)^{\top}=(85-84.7,\ -119+121)^{\top}=(0.3,\ 2)^{\top}$。

(b) $\lVert\Delta\mathbf{y}\rVert/\lVert\mathbf{y}\rVert=0.1/\sqrt{433}\approx0.1/20.809\approx0.48\,\%$。此外，$\Delta\mathbf{x}=(-0.7,\ 1)^{\top}$，所以 $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt{1.49}/\sqrt2\approx1.2207/1.4142\approx86.3\,\%$。两者之比约为 $180$。

(c) $\mathbf{A}$ 是对称的，迹为 $15$，行列式为 $1$，所以 $\lambda=\tfrac{15\pm\sqrt{221}}2\approx14.933$ 和 $0.0670$，都为正。由第 [9.7](die-singularwertzerlegung.html#stufe-9-7) 节，它们就是奇异值，$\kappa(\mathbf{A})\approx14.933/0.0670\approx223$。式 [(12.2)](#gl-12-2) 中的上界得到满足：$86.3\,\%\le223\cdot0.48\,\%\approx107\,\%$。到最近的奇异矩阵的距离为 $d_2\approx0.067$，相对而言为 $1/223$。行列式 $1$ 丝毫看不出这一点。
:::
:::

:::aufgabe 练习 38 ★★★ 条件数的运算规则
<span class="anker" id="aufg-38"></span>

设 $\mathbf{A}\in\mathbb{R}^{n\times n}$ 可逆，$\mathbf{Q}$ 是正交矩阵。证明：

<ol class="al">

<li>

$\kappa(\mathbf{Q}\mathbf{A})=\kappa(\mathbf{A})$ 且 $\kappa(\mathbf{A}^{-1})=\kappa(\mathbf{A})$；

</li>

<li>

对 $\mathbf{A}$ 的所有特征值 $\lambda$ 和 $\mu$，有 $|\lambda|/|\mu|\le\kappa(\mathbf{A})$；

</li>

<li>

若 $\mathbf{A}$ 是对称的，则 $\kappa(\mathbf{A})=|\lambda|_{\max}/|\lambda|_{\min}$，即绝对值最大的特征值与绝对值最小的特征值之比。

</li>

</ol>

:::loesung
(a) 由练习 [29](die-singularwertzerlegung.html#aufg-29)，$\mathbf{Q}\mathbf{A}$ 与 $\mathbf{A}$ 有相同的奇异值，因而有相同的条件数。由 $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ 得 $\mathbf{A}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$，这是一个奇异值为 $1/d_j$ 的奇异值分解。其中最大的是 $1/d_n$，最小的是 $1/d_1$，所以 $\kappa(\mathbf{A}^{-1})=\tfrac{1/d_n}{1/d_1}=\tfrac{d_1}{d_n}=\kappa(\mathbf{A})$。

(b) 对于属于 $\lambda$ 的特征向量 $\mathbf{v}$，由式 [(9.5)](die-singularwertzerlegung.html#gl-9-5) 得 $d_n\lVert\mathbf{v}\rVert\le\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert\le d_1\lVert\mathbf{v}\rVert$，所以 $d_n\le|\lambda|\le d_1$；如第 [9.8](die-singularwertzerlegung.html#stufe-9-8) 节所示，这对复特征向量同样成立。对 $\mu$ 也是如此。因此 $|\lambda|/|\mu|\le d_1/d_n$。

(c) 对于对称的 $\mathbf{A}$，由第 [9.7](die-singularwertzerlegung.html#stufe-9-7) 节，奇异值就是特征值的绝对值 $|\lambda_i|$。因此最大的奇异值是 $|\lambda|_{\max}$，最小的是 $|\lambda|_{\min}$。
:::
:::
