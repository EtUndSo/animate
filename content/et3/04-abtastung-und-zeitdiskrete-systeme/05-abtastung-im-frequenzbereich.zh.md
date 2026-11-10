---
title: 第 4 阶段：频域采样
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 采样与离散时间系统
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: 第 4 章：采样与离散时间系统
order: 3240500
summary: 角色互换后，同一原理依然成立：对频谱采样，信号就变为周期的。
tags: 
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
角色互换后，同一原理依然成立：对频谱采样，信号就变为周期的。
:::

只在频率 $kF$ 处已知的频谱，是由加权狄拉克冲激组成的梳状函数。乘上因子 $F$ 后，各权重恰好就是[第 3 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中的傅里叶系数：

<span class="anker" id="gl-4-1"></span>
$$S_p(f)=F\sum_kS(kF)\,\delta(f-kF)=F\,S(f)\cdot\sum_k\delta(f-kF)\;\bullet\!\!-\!\!\circ\;s_p(t)=\sum_ns\Bigl(t-\frac nF\Bigr). \tag{4.1}$$

对应的信号是以 $1/F$ 为周期重复的原信号。若信号的持续时间短于 $1/F$，各次重复就不会重叠。这时可以用一个时间窗恢复信号，并用 si 函数恢复频谱：

<span class="anker" id="gl-4-2"></span>
$$s(t)=s_p(t)\cdot\operatorname{rect}(Ft)\qquad\Longrightarrow\qquad S(f)=\sum_kS(kF)\operatorname{si}\Bigl(\pi\frac{f-kF}{F}\Bigr). \tag{4.2}$$

⁠**简而言之：**时间离散意味着频谱周期，频谱离散意味着时间周期。后者就是[第 3 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中的傅里叶级数：其系数是单个脉冲频谱的样本值，$S_p(k)=F\cdot S(kF)$。
