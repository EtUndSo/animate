---
title: 第 10 阶段：改变采样率——抽取与内插
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 采样与离散时间系统
order: 3241100
summary: 序列在事后可以用更低或更高的速率来表示。对于频谱，适用的规则与最初采样时相同。
tags: 
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
序列在事后可以用更低或更高的速率来表示。对于频谱，适用的规则与最初采样时相同。
:::

**按因子 $c$ 降采样。** 每 $c$ 个值中只保留一个。在概念上，先乘以由单位脉冲组成的梳状序列，再去掉其中的零：

$$s_c(n)=s(n)\sum_m\delta(n-mc),\qquad s_u(n)=s(nc).$$

乘以梳状序列会产生 $c$ 个间隔为 $1/c$ 的频谱副本，去掉零则使频率轴伸展 $c$ 倍：

<span class="anker" id="gl-10-1"></span>
$$S_{c,\mathrm a}(f)=\frac1c\sum_{k=0}^{c-1}S_\mathrm a\Bigl(f-\frac kc\Bigr),\qquad S_{u,\mathrm a}(f)=S_{c,\mathrm a}\Bigl(\frac fc\Bigr). \tag{10.1}$$

若频谱延伸到 $f_\mathrm g$（对原采样率归一化），则降采样后它延伸到 $cf_\mathrm g$。只有当 $cf_\mathrm g\le\frac12$ 时才不会产生混叠。否则，必须先用数字低通滤波器限制频带。

**按因子 $c$ 升采样。** 在每两个相邻值之间插入 $c-1$ 个零：当 $n$ 能被 $c$ 整除时 $s_\uparrow(n)=s(n/c)$，否则为 0。频谱被压缩 $c$ 倍，$S_{\uparrow,\mathrm a}(f)=S_\mathrm a(cf)$，并且在一个周期内包含 $c-1$ 个频谱镜像。截止频率为 $\frac{1}{2c}$、增益为 $c$ 的低通滤波器可以把它们滤除。在此过程中，滤波器用内插值填充这些零（即第 [3](abtasttheorem-und-ruckgewinnung.html#stufe-3) 阶段 si 内插的离散形式），而原有的值保持不变。先后进行降采样和升采样，可以使采样率改变一个有理因子 $c_1/c_2$。

:::abbildung et3/k4rate 7
改变采样率时的频谱（频率对各自的采样率归一化）。降采样使频带伸展；升采样使频带压缩并产生频谱镜像，这些镜像由内插滤波器滤除。
:::

:::aufgabe 练习 10 ★★ 降采样
<span class="anker" id="aufg-10"></span>

某序列的频谱延伸到 $f_\mathrm g=0.2$。

<ol class="al">

<li>

不加前置滤波器，可以按 $c=2$ 对它降采样吗？按 $c=3$ 呢？

</li>

<li>

按 $c=3$ 降采样之前必须做什么？在这一过程中会损失什么？

</li>

</ol>

:::loesung
(a) $c=2$：降采样后频带延伸到 $0.4\le0.5$，无混叠。$c=3$：频带延伸到 $0.6>0.5$，产生混叠。

(b) 先用数字低通滤波器把频带限制到 $\frac{1}{2c}=\frac16\approx0.167$。在这一过程中，0.167 与 0.2 之间的分量会丢失。这是降低采样率的代价。
:::
:::
