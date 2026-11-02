---
title: 第 8 阶段：离散傅里叶变换（DFT）
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 采样与离散时间系统
order: 3240900
summary: S mathrm a(f) 是连续函数，而计算机需要的是有限多个数。对于有限长序列，频谱的有限多个样本值就足够了。
tags: 
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
$S_\mathrm a(f)$ 是连续函数，而计算机需要的是有限多个数。对于有限长序列，频谱的有限多个样本值就足够了。
:::

**思路。** 若 $s(n)$ 只有 $M$ 个值，那么根据第 [4](abtastung-im-frequenzbereich.html#stufe-4) 阶段，间隔为 $F=1/M$ 的频谱样本值就足够了。它们对应于以 $M$ 为周期重复的信号 $s_d(n)$。由于频谱也是周期的（时间离散），$M$ 个频谱值就足够了。现在两边都是离散且周期的。

:::satz 定理 8.1 (离散傅里叶变换)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
$$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M},\qquad s_d(n)=\frac1M\sum_{k=0}^{M-1}S_d(k)\,\mathrm{e}^{\mathrm{j}2\pi kn/M},\qquad k,n=0,\dots,M-1. \tag{8.1}$$
:::

⁠**如何理解：**$S_d(k)$ 是频谱 $S_\mathrm a(f)$ 在 $f=k/M$ 处的值。下标 $k$ 对应于在这 $M$ 个值中恰好完成 $k$ 个周期的振荡。反变换是一个有 $M$ 项的傅里叶级数。各定理相应地成立，例如移位定理 $s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k)\mathrm{e}^{-\mathrm{j}2\pi mk/M}$（循环移位：从末尾移出的值又从开头移入）和帕塞瓦尔定理 $\sum_n|s_d(n)|^2=\frac1M\sum_k|S_d(k)|^2$。

**例。** $s_d=(1,\,2,\,0,\,-1)$，$M=4$，$\mathrm{e}^{-\mathrm{j}2\pi/4}=-\mathrm{j}$：

$$S_d(k)=\sum_{n=0}^{3}s_d(n)(-\mathrm{j})^{kn}:\qquad S_d(0)=2,\quad S_d(1)=1-3\mathrm{j},\quad S_d(2)=0,\quad S_d(3)=1+3\mathrm{j}.$$

验证：$S_d(3)=S_d^*(1)$，因为信号是实信号（$k=3$ 对应于 $k=-1$）。帕塞瓦尔定理：$1+4+0+1=6=\frac14(4+10+0+10)$。

:::aufgabe 练习 8 ★★ 手算 DFT
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

对 $s_d=(1,2,0,-1)$ 重新计算 $S_d(1)$。

</li>

<li>

用移位定理求循环移位后的序列 $(-1,1,2,0)$ 的 DFT，并直接验证 $S_d(1)$。

</li>

</ol>

:::loesung
(a) $S_d(1)=1+2(-\mathrm{j})+0\cdot(-1)+(-1)(-\mathrm{j})^3=1-2\mathrm{j}-\mathrm{j}=1-3\mathrm{j}$，因为 $(-\mathrm{j})^3=\mathrm{j}$。

(b) 移位 $m=1$：$S_d(k)\,(-\mathrm{j})^k$，因此得 $(2,\;(1-3\mathrm{j})(-\mathrm{j}),\;0,\;(1+3\mathrm{j})\mathrm{j})=(2,\;-3-\mathrm{j},\;0,\;-3+\mathrm{j})$。直接计算：$S_d(1)=-1+1\cdot(-\mathrm{j})+2\cdot(-1)+0=-3-\mathrm{j}$。
:::
:::
