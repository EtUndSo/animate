---
title: 概览: 采样与离散时间系统
kurz: 概览
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 采样与离散时间系统
order: 3240100
summary: 从连续信号到数值序列： 采样定理、离散卷积、DFT、FFT 与 z 变换
tags: 样本值
lang: zh
---

## 本章内容

计算机无法存储函数 $s(t)$，只能存储数值序列。因此，人们以固定的时间间隔 $T$ 测量信号，并用__样本值__ $s(nT)$ 进行计算。本章围绕两个问题展开：**这一过程会丢失信息吗？**以及：**怎样像第 1 至[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)对函数所做的那样，对数值序列进行计算？**


**所有结论背后的同一个原理：一个域中离散，意味着另一个域中周期。**

| 结论 | 来源 |
|---|---|
| 采样后的周期频谱 | 时间离散 $\Rightarrow$ 频谱周期（第 [2](das-spektrum-des-abgetasteten-signals.html#stufe-2) 阶段） |
| 采样定理、混叠 | 周期性的各个副本是否重叠（第 [3](abtasttheorem-und-ruckgewinnung.html#stufe-3) 阶段） |
| si 内插 | 理想低通滤波器截取出一个副本（第 [3](abtasttheorem-und-ruckgewinnung.html#stufe-3) 阶段） |
| 傅里叶级数 | 频谱离散 $\Rightarrow$ 时间周期（第 [4](abtastung-im-frequenzbereich.html#stufe-4) 阶段） |
| 离散卷积 | 对以样本值加权的狄拉克冲激求卷积积分（第 [5](zeitdiskrete-signale-und-die-diskrete-faltung.html#stufe-5) 阶段） |
| 离散时间傅里叶变换 | 样本值的频谱，周期为 1（第 [7](fourier-transformation-zeitdiskreter-signale.html#stufe-7) 阶段） |
| DFT | 两边都离散 $\Rightarrow$ 两边都周期（第 [8](die-diskrete-fourier-transformation-dft.html#stufe-8) 阶段） |
| 抽取、内插 | 对已采样的序列再次采样（第 [10](abtastrate-andern-dezimation-und-interpolation.html#stufe-10) 阶段） |
| z 变换 | 把拉普拉斯变换的思路用于序列：先加权，再变换（第 [11](die-z-transformation.html#stufe-11) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**采样率** $f_\mathrm A=1/T=1$ kHz（$T=1$ ms）。测试信号：300 Hz 和 700 Hz 的余弦振荡。

</li>

<li>

对于序列，频率对采样率归一化：$f=1$ 对应于 $f_\mathrm A$。因此，在 $f_\mathrm A=1$ kHz 时，$f=0.3$ 表示 300 Hz。

</li>

<li>

⁠**递归系统** $g(n)=s(n)+0.6\,g(n-1)$。

</li>

<li>

⁠**DFT 示例** $s_d=(1,\,2,\,0,\,-1)$。

</li>

</ul>

脚本 `rechnung_kap4.py` 可复算这些数值和曲线。
:::
