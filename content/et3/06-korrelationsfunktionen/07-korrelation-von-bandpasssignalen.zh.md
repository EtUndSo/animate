---
title: 第 6 阶段：带通信号的相关
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 相关函数
order: 3260700
summary: 带通信号的相关函数同样用复包络来计算（第 5 部分）。
tags: 
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
带通信号的相关函数同样用复包络来计算（[第 5 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)）。
:::

两个实带通信号的互相关函数仍然是带通信号：

$$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}.$$

反转后的信号具有包络 $s_T^*(-t)$，因为

$$s(-t)=\operatorname{Re}\bigl\{s_T(-t)\mathrm{e}^{-\mathrm{j}2\pi f_0t}\bigr\}=\operatorname{Re}\bigl\{s_T^*(-t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}.$$

利用[第 5 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)中的传输关系 $g_T=\frac12s_T*h_T$：

<span class="anker" id="gl-6-1"></span>
$$\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]=\tfrac12\int_{-\infty}^{\infty}s_T^*(t)\,g_T(t+\tau)\,\mathrm{d} t,\qquad E_s=\varphi^E_{ss}(0)=\varphi^E_{ssT}(0). \tag{6.1}$$

⁠**如何理解：**两个带通信号的相关，等于它们包络的相关的一半，再调制到载波上。带通信号的能量是其复包络能量的一半：幅度为 $|s_T|$ 的余弦，平均起来只有一半的功率。
