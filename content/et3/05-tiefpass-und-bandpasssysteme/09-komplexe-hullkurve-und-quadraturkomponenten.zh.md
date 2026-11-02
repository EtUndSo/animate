---
title: 第 8 阶段：复包络与正交分量
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 低通与带通系统
order: 3250900
summary: 对系统成立的，对信号也成立：带通信号是搭载在载波上的低通信号。本阶段给出写出这一关系的几种不同方式。
tags: 复包络, 复载波, 正交分量, 包络
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
对系统成立的，对信号也成立：带通信号是搭载在载波上的低通信号。本阶段给出写出这一关系的几种不同方式。
:::

用调制定理对式 [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) 作反变换，得到 $h(t)=\frac12h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}+\frac12\bigl[h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr]^*$，于是由 $z+z^*=2\operatorname{Re} z$ 得：

<span class="anker" id="gl-8-1"></span>
$$h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\},\qquad s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{8.1}$$

$s_T(t)$ 称为__复包络__，$\mathrm{e}^{\mathrm{j}2\pi f_0t}$ 称为__复载波__。二者乘积的一半就是[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中的解析分量 $s_+(t)=\frac12s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}$，因此 $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$。

:::satz 定理 8.1 (正交表示)
<span class="anker" id="satz-8-1"></span>

利用 $s_T=s_{Tr}+\mathrm{j} s_{Ti}$ 和希尔伯特变换 $\hat s=s*\frac{1}{\pi t}$：

<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
$$\begin{aligned} s(t)&=s_{Tr}(t)\cos(2\pi f_0t)-s_{Ti}(t)\sin(2\pi f_0t),\\ s_{Tr}(t)&=s(t)\cos(2\pi f_0t)+\hat s(t)\sin(2\pi f_0t),\qquad s_{Ti}(t)=\hat s(t)\cos(2\pi f_0t)-s(t)\sin(2\pi f_0t),\\ s(t)&=|s_T(t)|\cos\bigl(2\pi f_0t+\varphi_T(t)\bigr),\qquad|s_T|=\sqrt{s_{Tr}^2+s_{Ti}^2}. \end{aligned} \tag{8.2|8.3|8.4}$$
:::

⁠**如何理解：**$s_{Tr}$ 和 $s_{Ti}$ 合称__正交分量__（分别为同相分量和正交分量）：一个调制载波的余弦，另一个调制载波的正弦。$|s_T|$ 是__包络__，即在示波器上看到的信号“轮廓”；$\varphi_T$ 是载波的相位偏移。若复包络为实数（对称情形），则 $s(t)=s_T(t)\cos(2\pi f_0t)$：一个调幅余弦。

:::herleitung 正交分量
式 [(8.2)](#gl-8-2)：$\operatorname{Re}\{(s_{Tr}+\mathrm{j} s_{Ti})(\cos+\mathrm{j}\sin)\}=s_{Tr}\cos-s_{Ti}\sin$。对于式 [(8.3)](#gl-8-3)：$2s_+=s+\mathrm{j}\hat s$（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)），因此

$$s_T=(s+\mathrm{j}\hat s)(\cos-\mathrm{j}\sin)=(s\cos+\hat s\sin)+\mathrm{j}(\hat s\cos-s\sin).$$
:::

:::aufgabe 练习 8 ★★ 求复包络
<span class="anker" id="aufg-8"></span>

相对于 $f_0=10$ Hz，求下列信号的 $s_T$、$s_{Tr}$、$s_{Ti}$ 和 $|s_T|$： (a) $s(t)=\bigl[1+0.5\cos(2\pi\cdot1\,\mathrm{Hz}\cdot t)\bigr]\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t)$， (b) $s(t)=\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t+0.3)$， (c) $s(t)=\sin(2\pi\cdot10\,\mathrm{Hz}\cdot t)$。用式 [(8.2)](#gl-8-2) 验证 (c)。

:::loesung
(a) $s_T=1+0.5\cos(2\pi t)$，为实数：$s_{Tr}=s_T$，$s_{Ti}=0$，$|s_T|=1+0.5\cos(2\pi t)$，在 0.5 与 1.5 之间。这是一个调幅余弦。

(b) $s_T=\mathrm{e}^{\mathrm{j}0.3}$：$s_{Tr}=\cos0.3=0.955$，$s_{Ti}=\sin0.3=0.296$，$|s_T|=1$。包络是恒定的，只是相位移动了 0.3。

(c) $\sin x=\operatorname{Re}\{-\mathrm{j}\,\mathrm{e}^{\mathrm{j} x}\}$，因此 $s_T=-\mathrm{j}$：$s_{Tr}=0$，$s_{Ti}=-1$，$|s_T|=1$。验证：$0\cdot\cos-(-1)\sin=\sin$。
:::
:::
