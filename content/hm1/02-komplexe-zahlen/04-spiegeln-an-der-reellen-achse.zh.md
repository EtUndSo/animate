---
title: 第 3 阶段：关于实轴的镜像
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 复数
order: 1220400
summary: 现在还不能除以 x+iy 。本阶段引入 z 的镜像，它通过乘法可使任何数变为实数，并汇总运算法则。
tags: 
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
现在还不能除以 $x+\mathrm{i}y$。本阶段引入 $z$ 的镜像，它通过乘法可使任何数变为实数，并汇总运算法则。
:::

**基本思路。** $-\mathrm{i}$ 也满足 $x^2=-1$，因为 $(-\mathrm{i})^2=\mathrm{i}^2=-1$。运算法则无法区分 $\mathrm{i}$ 和 $-\mathrm{i}$。因此，在一个正确的计算中处处把 $\mathrm{i}$ 换成 $-\mathrm{i}$，计算仍然正确。在平面上，这种交换就是关于实轴的镜像（图 [3](#abb-3)）。把 $z$ 与它的镜像相乘，含 $\mathrm{i}$ 的交叉项就相互抵消。

:::abbildung hm1/k2konjugiert 3
$z_1$ 及其镜像 $\overline{z_1}$。和位于实轴上，因为虚部相互抵消；差位于虚轴上，因为实部相互抵消。
:::

:::definition 定义 3.1 (共轭复数)
<span class="anker" id="satz-3-1"></span>

对 $z=x+\mathrm{i}y$，称 $\overline{z}:=x-\mathrm{i}y\in\mathbb{C}$ 为 $z$ 的共轭复数。
:::

:::satz 定理 3.2 ($\mathbb{C}$ 中的运算法则)
<span class="anker" id="satz-3-2"></span>

对所有 $z=x+\mathrm{i}y$ 和 $w=u+\mathrm{i}v$（$x,y,u,v$ 为实数）有：

<ol class="rm">

<li>

$\operatorname{Re}(z+w)=\operatorname{Re}(z)+\operatorname{Re}(w)$，

</li>

<li>

$\operatorname{Im}(z+w)=\operatorname{Im}(z)+\operatorname{Im}(w)$，

</li>

<li>

$\overline{z+w}=\overline{z}+\overline{w}$，

</li>

<li>

$\overline{z\cdot w}=\overline{z}\cdot\overline{w}$，

</li>

<li>

$\overline{\overline{z}}=z$，

</li>

<li>

$z\overline{z}=x^2+y^2$，因而 $\operatorname{Im}(z\overline{z})=0$，$\operatorname{Re}(z\overline{z})=x^2+y^2$，

</li>

<li>

$z+\overline{z}=2\operatorname{Re}(z)$，$z-\overline{z}=2\mathrm{i}\operatorname{Im}(z)$。

</li>

</ol>
:::

⁠**如何理解：**取实部、取虚部和取共轭都可以逐项作用于和。取共轭还可以逐个作用于积的因子，这就是交换 $\mathrm{i}\leftrightarrow-\mathrm{i}$。取实部则不行：$\operatorname{Re}(z_1z_2)=1$，但 $\operatorname{Re}(z_1)\operatorname{Re}(z_2)=3$，因为积的实部中还含有 $-y_1y_2$。在电气工程中，常用 $z^*$ 代替 $\overline{z}$。

:::beweis 运算法则
(i)、(ii)：加法分别进行，$z+w=(x+u)+\mathrm{i}(y+v)$。

(iii)：$\overline{z+w}=(x+u)-\mathrm{i}(y+v)=(x-\mathrm{i}y)+(u-\mathrm{i}v)$。

(iv)：由式 [(1.3)](paare-statt-einzelner-zahlen.html#gl-1-3)，$zw=(xu-yv)+\mathrm{i}(xv+uy)$，所以 $\overline{zw}=(xu-yv)-\mathrm{i}(xv+uy)$。把同一公式用于 $-y$ 和 $-v$，得 $\overline{z}\,\overline{w}=(xu-yv)+\mathrm{i}(-xv-uy)$。两者一致。

(v)：把 $y$ 的符号改变两次。

(vi)：$(x+\mathrm{i}y)(x-\mathrm{i}y)=x^2-\mathrm{i}xy+\mathrm{i}xy-\mathrm{i}^2y^2=x^2+y^2$。

(vii)：$(x+\mathrm{i}y)+(x-\mathrm{i}y)=2x$，$(x+\mathrm{i}y)-(x-\mathrm{i}y)=2\mathrm{i}y$。
:::

::::beispiel
对 $z_1$ 有 $\overline{z_1}=3-\mathrm{i}$，$z_1\overline{z_1}=9+1=10$，$z_1+\overline{z_1}=6=2\cdot3$，$z_1-\overline{z_1}=2\mathrm{i}=2\mathrm{i}\cdot1$。对 (iv) 的检验：$\overline{z_1z_2}=1-7\mathrm{i}$，$\overline{z_1}\,\overline{z_2}=(3-\mathrm{i})(1-2\mathrm{i})=3-6\mathrm{i}-\mathrm{i}+2\mathrm{i}^2=1-7\mathrm{i}$。
::::

⁠**极限情况：**当 $y=0$ 时，$\overline{z}=z$，$z\overline{z}=x^2$。实数位于镜像轴上，保持不变。

:::frage $z\overline{z}$ 不就是 $z^2$ 吗？
只有 $z$ 为实数时才是。在 $z^2$ 中交叉项相加得 $2\mathrm{i}xy$，在 $z\overline{z}$ 中它们相互抵消。在参考模型中，$z_2^2=-3+4\mathrm{i}$，而 $z_2\overline{z_2}=5$。
:::

:::aufgabe 练习 3 ★ 实数还是纯虚数？
<span class="anker" id="aufg-3"></span>

设 $z=2-5\mathrm{i}$。(a) 不经计算预测 $z+\overline{z}$、$z-\overline{z}$、$z\overline{z}$、$z^2+\overline{z}^2$、$(z-\overline{z})^2$ 中哪些是实数，哪些是纯虚数。然后计算验证。(b) 证明对每个 $z\in\mathbb{C}$：$z$ 是实数当且仅当 $\overline{z}=z$，$z$ 是纯虚数当且仅当 $\overline{z}=-z$。

:::loesung
(a) 预测：$z+\overline{z}$ 是实数，$z-\overline{z}$ 是纯虚数，$z\overline{z}$ 是实数，$z^2+\overline{z}^2=z^2+\overline{z^2}$ 是实数（一个数与其镜像之和），$(z-\overline{z})^2$ 是实数（纯虚数的平方）。计算：$z+\overline{z}=4$，$z-\overline{z}=-10\mathrm{i}$，$z\overline{z}=4+25=29$。由 $z^2=4-20\mathrm{i}+25\mathrm{i}^2=-21-20\mathrm{i}$ 得 $z^2+\overline{z}^2=-42$，而 $(z-\overline{z})^2=(-10\mathrm{i})^2=-100$。

(b) 由第 [3](#stufe-3) 阶段的规则 (vii)，$\overline{z}=z$ 等价于 $2\mathrm{i}\operatorname{Im}(z)=0$，即 $\operatorname{Im}(z)=0$。同样，$\overline{z}=-z$ 等价于 $2\operatorname{Re}(z)=0$，即 $\operatorname{Re}(z)=0$。
:::
:::
