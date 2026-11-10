---
title: 第 8 阶段：积分与微分
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / LTI 系统与卷积
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: 第 1 章：LTI 系统与卷积
order: 3210900
summary: 积分器和微分器都是 LTI 系统。它们把阶跃响应和冲激响应联系起来，并使我们能够由 RC 电路的阶跃响应得到它的冲激响应。
tags: 积分器, 微分器, 冲激偶
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
积分器和微分器都是 LTI 系统。它们把阶跃响应和冲激响应联系起来，并使我们能够由 RC 电路的阶跃响应得到它的冲激响应。
:::

**积分器。** 把式 [(7.6)](der-dirac-impuls.html#gl-7-6) 中的 $\delta$ 换成任意的 $s$，同样的计算给出

<span class="anker" id="gl-8-1"></span>
$$s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau. \tag{8.1}$$

冲激响应为 $\varepsilon(t)$ 的系统求出其输入的变上限积分，称为__积分器__。若交换角色来读（$\varepsilon*s$），式 [(8.1)](#gl-8-1) 表明：**系统的阶跃响应是其冲激响应的变上限积分。**用 RC 电路来检验：$\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$，正是式 [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5)。微分方程和卷积这两条相互独立的途径，得到了相同的结果。

**微分器。** 积分器后接一个__微分器__，任何信号都保持不变；这个级联是理想无失真的。因此，微分器的冲激响应是广义函数 $\delta'(t)$（__冲激偶__），其定义为

<span class="anker" id="gl-8-2"></span>
$$\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t). \tag{8.2}$$

近似地看，$\delta'$ 是一个窄的双矩形脉冲：先是一个高度为 $+1/T_0^2$ 的矩形，再是一个高度为 $-1/T_0^2$ 的矩形，宽度均为 $T_0$。它被画成一对箭头，一个向上，一个向下。

**冲激响应 $=$ 阶跃响应的导数。** 由于 $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$，且系统是线性时不变的，所以 $h=\frac{\mathrm{d}}{\mathrm{d} t}(\text{阶跃响应})$。对于 RC 电路，利用乘积法则：

<span class="anker" id="gl-8-3"></span>
$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\Bigl[\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)\Bigr]=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)+\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t). \tag{8.3}$$

根据式 [(7.2)](der-dirac-impuls.html#gl-7-2)，第二项为零：$(1-\mathrm{e}^{0})\,\delta(t)=0$。其背后的机理是：RC 电路的阶跃响应没有跳变，因为电容充电需要时间。只有带跳变的阶跃响应，才会在 $h$ 中产生狄拉克冲激（练习 [9](#aufg-9)）。

:::aufgabe 练习 9 ★★ 高通滤波器：冲激响应中的狄拉克冲激
<span class="anker" id="aufg-9"></span>

若把 $R$ 和 $C$ 互换，输出电压就取自 $R$ 两端（CR 高通滤波器，$RC=1$ s）。它的阶跃响应为 $\mathrm{e}^{-t}\varepsilon(t)$。

<ol class="al">

<li>

从机理上解释这一阶跃响应：最初瞬间 $R$ 两端的电压是多少？很长时间之后又是多少？

</li>

<li>

通过求导求出冲激响应。其中的狄拉克分量在物理上意味着什么？

</li>

<li>

检验：对冲激响应积分，必须重新得到阶跃响应。

</li>

</ol>

:::loesung
(a) 最初瞬间电容未充电，因此其两端没有电压。全部 1 V 都加在 $R$ 上。随后电流给电容充电；电容电压按 $1-\mathrm{e}^{-t}$ 上升，$R$ 上剩下 $\mathrm{e}^{-t}$。很长时间之后，电容充满，不再有电流流过，$R$ 上也就没有电压了。

(b) 乘积法则：

$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\bigl[\mathrm{e}^{-t}\varepsilon(t)\bigr]=-\mathrm{e}^{-t}\varepsilon(t)+\mathrm{e}^{0}\,\delta(t)=\delta(t)-\mathrm{e}^{-t}\varepsilon(t).$$

这里阶跃响应在 $t=0$ 处从 0 跳变到 1，因此狄拉克分量保留了下来。物理上：无限短的冲激直接通过，因为电容无法在零时间内建立起电压。冲激送到电容上的电荷，随后又经 $R$ 沿相反方向流走：$-\mathrm{e}^{-t}$。

(c) $\int_{-\infty}^t\bigl[\delta(\tau)-\mathrm{e}^{-\tau}\varepsilon(\tau)\bigr]\mathrm{d}\tau=\varepsilon(t)-\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t)$。
:::
:::
