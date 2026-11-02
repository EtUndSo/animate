---
title: 第 3 阶段：正弦激励下的波
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 正交展开与传输线
order: 3280400
summary: 借助相量，偏微分方程变成关于位置的常微分方程。它的解由两个沿相反方向传播的波组成。
tags: 波动方程, 传播常数, 特性阻抗, 衰减常数, 反射系数
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
借助相量，偏微分方程变成关于位置的常微分方程。它的解由两个沿相反方向传播的波组成。
:::

令 $u(s,t)=\sqrt2\operatorname{Re}\{\underline U(s)\mathrm{e}^{\mathrm{j}2\pi ft}\}$，对 $i$ 也同样处理，则 $\frac{\partial}{\partial t}$ 变为 $\mathrm{j}2\pi f$：

$$\frac{\mathrm{d}\underline U}{\mathrm{d} s}=-(R'+\mathrm{j}2\pi fL')\,\underline I,\qquad\frac{\mathrm{d}\underline I}{\mathrm{d} s}=-(G'+\mathrm{j}2\pi fC')\,\underline U.$$

对第一个方程求导并代入第二个方程，得到__波动方程__ $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=\gamma^2\underline U$。

:::satz 定理 3.1 (入射波与反射波)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s},\qquad\underline I(s)=\frac{1}{Z}\bigl(\underline U_1\mathrm{e}^{-\gamma s}-\underline U_2\mathrm{e}^{\gamma s}\bigr), \tag{3.1}$$

其中__传播常数__和__特性阻抗__为

<span class="anker" id="gl-3-2"></span>
$$\gamma=\sqrt{(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')}=\alpha+\mathrm{j}\beta,\qquad Z=\sqrt{\frac{R'+\mathrm{j}2\pi fL'}{G'+\mathrm{j}2\pi fC'}}. \tag{3.2}$$
:::

⁠**如何理解：**令 $\gamma=\alpha+\mathrm{j}\beta$，第一项在时域中变为 $\hat u_1\mathrm{e}^{-\alpha s}\cos(2\pi ft-\beta s+\varphi_1)$：这是一个沿 $s$ 增大方向传播、并在传播过程中以__衰减常数__ $\alpha$ 衰减的波。过零点以速度 $v=2\pi f/\beta$ 移动，波长为 $\lambda=2\pi/\beta$。第二项沿相反方向传播。$Z$ 是单个波中电压与电流之比。常数 $\underline U_1$、$\underline U_2$ 由边界条件确定，例如由始端的电压和电流确定：$\underline U_{1,2}=\frac12(\underline U_a\pm Z\underline I_a)$。

**终端的反射。** 若传输线在终端（$s=l$）接有电阻 $R_\mathrm E=\underline U_e/\underline I_e$，则电压可以写成

<span class="anker" id="gl-3-3"></span>
$$\underline U(s)=\tfrac12(R_\mathrm E+Z)\,\underline I_e\,\mathrm{e}^{\gamma(l-s)}+\tfrac12(R_\mathrm E-Z)\,\underline I_e\,\mathrm{e}^{-\gamma(l-s)}. \tag{3.3}$$

第一项是正向行波（入射波），第二项是从终端返回的波（反射波）。当 $R_\mathrm E=Z$ 时，反射波消失：以特性阻抗作终端负载时，到达的波被完全吸收，就好像传输线无限延伸下去一样。终端处两个波之比就是__反射系数__ $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$（补充：短路时 $r=-1$，开路时 $r=+1$）。

:::frage 为什么对于短线，终端负载不正确也不会造成影响？
因为这时反射波几乎立刻就返回了。若沿传输线的传播时延与信号变化的持续时间相比很小（线长与波长相比很短），入射波与反射波实际上是同时叠加的，人们只会察觉到终端电阻。只有当传播时延变得可以相比拟时，例如对于快速数字信号或在高频下，反射才会以回波的形式出现并使信号失真。
:::
