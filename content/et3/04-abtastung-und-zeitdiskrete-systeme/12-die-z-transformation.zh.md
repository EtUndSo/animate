---
title: 第 11 阶段：z 变换
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 采样与离散时间系统
order: 3241200
summary: 正如拉普拉斯变换推广了傅里叶变换（第 2 部分），z 变换推广了离散时间傅里叶变换：先进行指数加权，再进行变换。
tags: 单位圆
lang: zh
---

<span class="anker" id="stufe-11"></span>

:::zweck
正如拉普拉斯变换推广了傅里叶变换（[第 2 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)），z 变换推广了离散时间傅里叶变换：先进行指数加权，再进行变换。
:::

**思路。** 将序列乘以 $\rho^{-n}$（$\rho>0$）再做变换：$\sum_ns(n)\rho^{-n}\mathrm{e}^{-\mathrm{j}2\pi fn}$。令 $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$，它就变成关于 $z^{-1}$ 的幂级数。等价的说法是：$z^n$ 是每个 LSI 系统的特征函数，因为 $z^{n-k}=z^{-k}z^n$，而特征值为 $H(z)$：

$$z^n*h(n)=\sum_kh(k)z^{n-k}=z^n\sum_kh(k)z^{-k}=H(z)\,z^n.$$

:::satz 定理 11.1 (z 变换)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$S(z)=\sum_{n=-\infty}^{\infty}s(n)\,z^{-n},\qquad s(n)=\frac{1}{2\pi\mathrm{j}}\oint S(z)\,z^{n-1}\,\mathrm{d} z, \tag{11.1}$$

其中围线积分沿收敛域内的圆 $|z|=\rho$ 按逆时针方向进行。
:::

⁠**如何理解：**圆 $|z|=\rho$ 上分布着加权序列 $s(n)\rho^{-n}$ 的频谱的一个周期。在__单位圆__ $|z|=1$ 上，$S(z)$ 就是普通的频谱 $S_\mathrm a(f)$，前提是单位圆位于收敛域内。这样，拉普拉斯变换的复平面就映射到 z 平面上：虚轴变为单位圆，左半平面变为单位圆的内部。

**基本变换对与收敛域。** 利用等比级数可得：

<span class="anker" id="gl-11-2"></span>
$$\varepsilon(n)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{1}{1-bz^{-1}}=\frac{z}{z-b},\quad|z|>|b|;\qquad -\varepsilon(-n-1)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{z}{z-b},\quad|z|<|b|. \tag{11.2}$$

与拉普拉斯变换一样，同一个表达式属于两个信号，只有收敛域才能决定是哪一个。对于右边序列，收敛域位于经过最外侧极点的圆的外部；对于左边序列，它位于经过最内侧极点的圆的内部；对于双边序列，它是一个圆环。对于 $0<b<1$ 的 $b^{|n|}$，这个圆环是 $b<|z|<1/b$。

**运算规则。** 卷积变为乘积：$g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)H(z)$。延迟 $n_0$ 个采样周期变为乘以 $z^{-n_0}$。这样，差分方程 [(5.2)](zeitdiskrete-signale-und-die-diskrete-faltung.html#gl-5-2) 就变为

<span class="anker" id="gl-11-3"></span>
$$H(z)=\frac{G(z)}{S(z)}=\frac{\sum_{q=0}^{Q}a_q\,z^{-q}}{1-\sum_{p=1}^{P}b_p\,z^{-p}}. \tag{11.3}$$

对于练习 [6](ein-rekursives-system.html#aufg-6) 中的系统，$H(z)=\frac{1+0.5z^{-1}}{1-0.6z^{-1}}$：零点位于 $z=-0.5$，极点位于 $z=0.6$。

:::satz 定理 11.2 (稳定性)
<span class="anker" id="satz-11-2"></span>

因果 LSI 系统稳定，当且仅当 $H(z)$ 的所有极点都位于单位圆内部。
:::

⁠**原因：**因果意味着收敛域位于最外侧极点之外。稳定意味着 $\sum|h(n)|<\infty$；这时 $H(z)$ 在单位圆上收敛，因此单位圆属于收敛域。只有当最外侧极点位于单位圆内部时，二者才能同时成立。对于 $H(z)=\frac{1}{1-bz^{-1}}$ 的递归系统，这又意味着 $|b|<1$。

::::beispiel
$s(n)=0.5^n\cos(\pi n/3)\,\varepsilon(n)$。利用 $\cos=\frac12(\mathrm{e}^{\mathrm{j}\pi n/3}+\mathrm{e}^{-\mathrm{j}\pi n/3})$，并对 $b=0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}$ 应用式 [(11.2)](#gl-11-2)：

$$S(z)=\frac12\Bigl[\frac{1}{1-0.5\mathrm{e}^{\mathrm{j}\pi/3}z^{-1}}+\frac{1}{1-0.5\mathrm{e}^{-\mathrm{j}\pi/3}z^{-1}}\Bigr]=\frac{1-0.25z^{-1}}{1-0.5z^{-1}+0.25z^{-2}},\qquad|z|>0.5.$$

极点位于 $0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}=0.25\pm0.433\mathrm{j}$，零点位于 $z=0$ 和 $z=0.25$（图 [8](#abb-8)）。极点的模给出每个采样周期的衰减（0.5），极点的辐角给出振荡（每个采样周期 $\pi/3$，因此每个振荡周期包含六个采样周期）。

:::abbildung et3/k4zebene 8
例题的 z 平面：极点（叉号）位于 $0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}$，零点（圆圈）位于 0 和 0.25。收敛域（蓝色）位于经过极点的圆之外，并包含单位圆。若把该序列看作单位脉冲响应，它描述的是一个因果且稳定的系统。
:::
::::

:::aufgabe 练习 11 ★★ 应用 z 变换
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

将两个分式通分，验证例题中 $S(z)$ 的分子和分母。

</li>

<li>

例题信号的频谱 $S_\mathrm a(f)$ 存在吗？用收敛域说明理由。

</li>

</ol>

:::loesung
(a) 公分母为 $(1-az^{-1})(1-a^*z^{-1})=1-(a+a^*)z^{-1}+|a|^2z^{-2}$，其中 $a=0.5\mathrm{e}^{\mathrm{j}\pi/3}$：$a+a^*=2\cdot0.25=0.5$，$|a|^2=0.25$。分子为 $\frac12[2-(a+a^*)z^{-1}]=1-0.25z^{-1}$。

(b) 存在。收敛域 $|z|>0.5$ 包含单位圆。
:::
:::

:::aufgabe 练习 12 ★★ 因果还是稳定
<span class="anker" id="aufg-12"></span>

$H(z)=\dfrac{1}{1-2z^{-1}}$。

<ol class="al">

<li>

收敛域 $|z|>2$ 对应哪个单位脉冲响应？收敛域 $|z|<2$ 又对应哪个？

</li>

<li>

两者中哪个是稳定的，哪个是因果的？是否存在既因果又稳定的？

</li>

</ol>

:::loesung
(a) $|z|>2$：$h(n)=2^n\varepsilon(n)$。$|z|<2$：$h(n)=-2^n\varepsilon(-n-1)$，即 $n=-1,-2,\dots$ 时为 $-\frac12,-\frac14,\dots$。

(b) 第一个是因果的，但不稳定（它不断增长）。第二个是稳定的（$\sum_{n\le-1}2^n=1$），但它是反因果的。二者不可能同时成立：极点 $z=2$ 位于单位圆之外，此时收敛域不可能既位于极点之外又包含单位圆。
:::
:::
