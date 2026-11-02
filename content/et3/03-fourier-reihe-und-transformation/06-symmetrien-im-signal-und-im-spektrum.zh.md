---
title: 第 5 阶段：信号与频谱中的对称性
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 傅里叶级数与变换
order: 3230600
summary: 信号是实的、偶的还是奇的，可以直接从其频谱看出。本阶段推导相应的规则。
tags: 偶, 奇
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
信号是实的、偶的还是奇的，可以直接从其频谱看出。本阶段推导相应的规则。
:::

**偶部与奇部。** 若复函数满足 $x(t)=x^*(-t)$，则称它为__偶__函数；若满足 $x(t)=-x^*(-t)$，则称它为__奇__函数。（对实函数而言，这就是通常的镜像对称和关于原点的点对称。）每个信号都可以唯一地分解为这两部分：

<span class="anker" id="gl-5-1"></span>
$$s(t)=s_g(t)+s_u(t),\qquad s_g(t)=\tfrac12\bigl[s(t)+s^*(-t)\bigr],\qquad s_u(t)=\tfrac12\bigl[s(t)-s^*(-t)\bigr]. \tag{5.1}$$

:::satz 定理 5.1 (对称性)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-2"></span>
$$s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\},\qquad s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}. \tag{5.2}$$

对**实**信号有 $S(-f)=S^*(f)$：实部和模 $|S|$ 是 $f$ 的偶函数，虚部和相位是奇函数。实的偶信号具有实的偶频谱。实的奇信号具有纯虚的奇频谱。
:::

:::herleitung 对称性
首先：$\mathcal{F}\{s^*(-t)\}=\int s^*(-t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$。令 $\tau=-t$，则该式等于 $\int s^*(\tau)\mathrm{e}^{\mathrm{j}2\pi f\tau}\mathrm{d}\tau=\bigl(\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f\tau}\mathrm{d}\tau\bigr)^*=S^*(f)$。因此

$$\mathcal{F}\{s_g\}=\tfrac12\bigl[S(f)+S^*(f)\bigr]=\operatorname{Re}\{S(f)\},\qquad\mathcal{F}\{s_u\}=\tfrac12\bigl[S(f)-S^*(f)\bigr]=\mathrm{j}\operatorname{Im}\{S(f)\}.$$

对实信号 $s$ 有 $\mathcal{F}\{s^*(t)\}=\mathcal{F}\{s(t)\}$。一般地，$\mathcal{F}\{s^*(t)\}=\int s^*\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\bigl(\int s\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} t\bigr)^*=S^*(-f)$。所以 $S(f)=S^*(-f)$。
:::

⁠**简而言之：**对实信号而言，频谱的负半部分是正半部分的共轭镜像，不包含任何新的信息。

**例。** 指数脉冲 $\varepsilon(t)\mathrm{e}^{-t}$（实信号）的偶部为 $\frac12\mathrm{e}^{-|t|}$，奇部为 $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$。其频谱 $H(f)=\frac{1}{1+\mathrm{j}2\pi f}$ 的实部 $\frac{1}{1+(2\pi f)^2}$ 是偶函数，正是 $\frac12\mathrm{e}^{-|t|}$ 的变换；虚部 $\frac{-2\pi f}{1+(2\pi f)^2}$ 是奇函数（图 [5](#abb-5)）。

:::abbildung et3/k3gerade 5
指数脉冲（$RC=1$ s）分解为偶部（蓝）和奇部（红）。右图：频谱。偶部给出实部（$f$ 的偶函数），奇部给出虚部（$f$ 的奇函数）。
:::

:::aufgabe 练习 5 ★ 由对称性判断
<span class="anker" id="aufg-5"></span>

无需计算，关于频谱可以得出什么结论？(a) $s(t)=\operatorname{rect}(t)$，(b) $s(t)=\operatorname{sgn}(t)\operatorname{rect}(t/2)$，(c) $s(t)=\mathrm{e}^{\mathrm{j}2\pi t}\operatorname{rect}(t)$，(d) 一个实信号满足 $S(1\,\mathrm{Hz})=2-3\mathrm{j}$：$S(-1\,\mathrm{Hz})$ 是多少？

:::loesung
(a) 实且偶：频谱为实偶函数（$\operatorname{si}(\pi f)$）。 (b) 实且奇：频谱为纯虚奇函数。 (c) 复信号，但 $x^*(-t)=\mathrm{e}^{-\mathrm{j}2\pi(-t)}\operatorname{rect}(-t)=x(t)$：按定义的意义，该信号是偶的，因此其频谱是实的。由调制定理，频谱为 $\operatorname{si}(\pi(f-1))$，是实的，但不关于 $f=0$ 对称，因为信号不是实的。 (d) $S(-1\,\mathrm{Hz})=S^*(1\,\mathrm{Hz})=2+3\mathrm{j}$。
:::
:::
