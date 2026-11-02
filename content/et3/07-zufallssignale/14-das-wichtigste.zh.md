---
title: 要点
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 随机信号
order: 3271400
summary: 均值、分布、功率谱密度， 系统中的噪声与最佳接收机
tags: 
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

随机信号用平均值来描述：均值、功率、方差、自相关函数和概率密度函数。对于各态历经过程，可以由单个足够长的信号求出它们。

</li>

<li>

自相关函数的傅里叶变换就是功率谱密度。LTI 系统把它乘以 $|H(f)|^2$，与能量信号的情形（[第 6 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)）完全一样。

</li>

<li>

在白噪声背景下，匹配滤波器 $h(t)=s(T-t)$ 是最佳的。它达到的信噪比为 $E_s/N_0$，与信号形状无关。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

集平均 $\mathrm E\{\cdot\}$；平稳：与平移无关；各态历经：时间平均 $=$ 集平均。

</li>

<li>

$m_s$（直流分量），$L_s=\mathrm E\{s^2\}$（功率），$\sigma_s^2=L_s-m_s^2$（交流功率）。

</li>

<li>

自相关函数：$\varphi_{ss}(0)=L_s$，偶函数，最大值在 0 处；协方差 $\mu=\varphi-m^2$；和：$\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0)$。

</li>

<li>

$P_s(x)=\mathrm{Prob}[s\le x]$，$p_s=P_s'$；$m_s=\int xp_s$，$L_s=\int x^2p_s$；均匀分布 $\sigma^2=a^2/12$。

</li>

<li>

特性曲线：$p_g(y)|\mathrm{d} y|=p_s(x)|\mathrm{d} x|$；量化误差（量化噪声）$\Delta^2/12$，每比特 6 dB。

</li>

<li>

独立 $\Rightarrow$ 不相关；独立变量之和：$p_s=p_f*p_g$；高斯分布：$\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{e}^{-(x-m)^2/2\sigma^2}$。

</li>

<li>

LTI：$m_g=m_sH(0)$，$\varphi_{gg}=\varphi_{ss}*\varphi^E_{hh}$，$\Phi_{gg}=\Phi_{ss}|H|^2$，$L=\int\Phi\,\mathrm{d} f$。

</li>

<li>

白噪声：$\Phi=N_0$，$\varphi=N_0\delta$；热噪声 $\mathrm E\{u^2\}=4kTRf_\mathrm g$，$kT\approx4$ pW/GHz。

</li>

<li>

匹配滤波器：$h=a\,s(T-t)$，$(S_a/N)_{\max}=E_s/N_0$；$P_{e,\min}=\frac12\operatorname{erfc}\sqrt{E_s/(8N_0)}$。

</li>

</ul>
:::
