---
title: 第 9 阶段：带通信号通过带通系统
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 低通与带通系统
order: 3251000
summary: 包络的用处：带通对带通信号的作用，可以完全在低通域中计算。
tags: 
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
包络的用处：带通对带通信号的作用，可以完全在低通域中计算。
:::

:::satz 定理 9.1 (在等效低通域中的传输)
<span class="anker" id="satz-9-1"></span>

若 $S_T$ 和 $H_T$ 都满足式 [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2)（在 $-f_0$ 以下没有分量），则输出的包络满足

<span class="anker" id="gl-9-1"></span>
$$G_T(f)=\tfrac12S_T(f)\,H_T(f)\qquad\bullet\!\!-\!\!\circ\qquad g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr],\qquad g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{9.1}$$
:::

:::herleitung 传输
用两种表示式 [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) 把 $G=S\cdot H$ 展开，得到四个乘积。混合项，例如 $S_T(f-f_0)H_T^*(-f-f_0)$，为零：第一个因子只存在于正频率，第二个只存在于负频率。剩下的是 $G=\frac14S_T(f-f_0)H_T(f-f_0)+\frac14S_T^*(-f-f_0)H_T^*(-f-f_0)$。将其与 $G=\frac12G_T(f-f_0)+\frac12G_T^*(-f-f_0)$ 比较，得 $G_T=\frac12S_TH_T$。
:::

⁠**如何理解：**因子 $\frac12$ 补偿了 $S_T$ 和 $H_T$ 都被加倍这一事实。除此之外，它就是熟悉的卷积定理，只不过是对包络而言。载波根本不必参与计算。

::::beispiel 接通的余弦通过理想带通
$s(t)=\varepsilon(t)\cos(2\pi f_0t)$，$f_0=10$ Hz，带通以 $f_0$ 为中心，$\Delta f=2$ Hz。输入的包络为 $s_T\approx\varepsilon(t)$。（这是近似：阶跃的频谱并不局限于 $f>-f_0$，但在通带 $|f|\le\Delta f/2\ll f_0$ 内它是正确的。）利用 $h_T=2\Delta f\operatorname{si}(\pi\Delta f\,t)$：

$$g_T(t)\approx\tfrac12\bigl[\varepsilon(t)*2\Delta f\operatorname{si}(\pi\Delta f\,t)\bigr]=\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t),\qquad g(t)\approx\Bigl[\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t)\Bigr]\cos(2\pi f_0t).$$

包络就是 $f_\mathrm g=\Delta f/2$ 的理想低通的阶跃响应：上升时间 $1/\Delta f=0.5$ s，过冲 8.95 %（图 [5](#abb-5)）。窄带通需要很长时间才能“稳定下来”。

:::abbildung et3/k5bandpass 5
理想带通（$f_0=10$ Hz，$\Delta f=2$ Hz）对在 $t=0$ 时接通的中心频率余弦的响应。蓝：输出信号；红：包络 $\pm g_T(t)$。包络在约 0.5 s 内上升，并过冲到 1.09。
:::
::::

:::ltspice 接通的载波通过谐振电路
理想带通无法实现，但串联谐振电路可以实现。**绘制：**电压源 `voltage` 接在节点 `in` 上，然后依次串联 `ind`（取 `{L}`）、`cap`（取 `{1/((2*pi*f0)**2*L)}`）和 `res`（取 `{2*pi*df*L}`）到地。输出 `out` 是电阻两端的电压。取 `.param f0=10 df=2 L=1` 时，中心频率为 10 Hz，两个 $-3$ dB 点之间的带宽为 2 Hz。

⁠**检验：**信号源的值取 `AC 1` 并使用 `.ac lin 2001 5 15`，可以看到 10 Hz 处的最大值 1，以及位于 9.05 Hz 和 11.05 Hz 的 $-3$ dB 点。

⁠**实验：**信号源取 `SINE(0 1 10 0 0 90)`，即 $\varepsilon(t)\cos(2\pi f_0t)$，指令为 `.tran 0 3 0 0.1m`。包络无过冲地上升：载波峰值在 0.2 s 时达到 0.72，0.5 s 时达到 0.96，1 s 后实际上达到 1，几乎恰好与 $1-\mathrm{e}^{-t/0.16\,\mathrm s}$ 一致。相比之下，理想带通会过冲到 1.09（图 [5](#abb-5)）。原因与第 [3](sprungantwort-und-einschwingzeit.html#stufe-3) 阶段中低通的情形相同：谐振电路的边沿是平缓的，而理想带通的边沿是竖直的。
:::
