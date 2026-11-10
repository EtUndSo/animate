---
title: 第 9 阶段：白噪声与热噪声
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 随机信号
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: 第 7 章：随机信号
order: 3271000
summary: 最重要的干扰模型：在所有频率上功率谱密度都相同的噪声。
tags: 白噪声
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
最重要的干扰模型：在所有频率上功率谱密度都相同的噪声。
:::

:::definition 定义 9.1 (白噪声)
<span class="anker" id="satz-9-1"></span>

对所有 $f$ 都有 $\Phi_{ss}(f)=N_0$ 的零均值过程称为__白噪声__。它的自相关函数为 $\varphi_{ss}(\tau)=N_0\,\delta(\tau)$。
:::

⁠**如何理解：**不同时刻的取值互不相关，无论它们靠得多近。功率 $\int N_0\mathrm{d} f$ 为无穷大：白噪声是一种极限模型，就像狄拉克冲激一样。实际测到的总是经过滤波的噪声，即“有色”噪声：

<span class="anker" id="gl-9-1"></span>
$$\Phi_{gg}(f)=N_0|H(f)|^2,\qquad\varphi_{gg}(\tau)=N_0\,\varphi^E_{hh}(\tau),\qquad L_g=N_0\int|h(t)|^2\mathrm{d} t=N_0\int|H(f)|^2\mathrm{d} f. \tag{9.1}$$

在截止频率为 $f_\mathrm g$ 的理想低通之后：$L_g=2N_0f_\mathrm g$，$\varphi_{gg}(\tau)=2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$（图 [3](#abb-3)）。自相关函数在 $\tau=k/(2f_\mathrm g)$（$k\neq0$）处为零：以奈奎斯特率采得的样本值互不相关。

:::abbildung et3/k7tp 3
白噪声通过理想低通后的自相关函数：$2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$。在 $\tau=0$ 处它等于功率 $2N_0f_\mathrm g$。在红点处（$\tau=k/(2f_\mathrm g)$）它为零。
:::

**热噪声。** 电子的热运动在每个电阻 $R$ 上产生噪声电压。在开路状态下，在频率范围 $|f|\le f_\mathrm g$ 内测量：

<span class="anker" id="gl-9-2"></span>
$$\mathrm E\{u^2\}=4kT_\mathrm{abs}Rf_\mathrm g,\qquad N_0=2kT_\mathrm{abs}R,\qquad L_{\max}=kT_\mathrm{abs}f_\mathrm g, \tag{9.2}$$

其中玻尔兹曼常数 $k=1.38\cdot10^{-23}$ W s/K。在室温（290 K）下，$kT\approx4\cdot10^{-21}$ W/Hz，即每 GHz 带宽 4 pW。$L_{\max}$ 是在功率匹配时最多能从电阻取出的功率。在参考模型中（$1\,\mathrm{k\Omega}$，20 kHz），有效值为 $\sqrt{\mathrm E\{u^2\}}=0.57$ µ V。这个数量级限制了传声器放大器所能达到的灵敏度。频谱直到约 $10^{12}$ Hz 都是平坦的。

:::ltspice 测量热噪声
LTspice 为每个电阻都加上它的热噪声。`.noise` 分析计算某个节点上的噪声密度 `V(onoise)`，单位为 V$/\sqrt{\mathrm{Hz}}$。测量语句 `.meas noise urms INTEG V(onoise)` 在分析的频率范围内对它按平方积分（如式 [(8.3)](zufallssignale-in-lti-systemen-leistungsdichte.html#gl-8-3)），并给出有效值。`.temp 16.85` 把温度设为 290 K。

⁠**电阻：**`res` 取 `{Rx}`，从节点 `a` 接地；与它并联一个值为 0 的电流源 `current`（名称为 `I1`）。它不构成任何负载，`.noise` 只是把它用作参考源。指令 `.param Rx=1k` 和 `.noise V(a) I1 lin 20001 1 20k`。结果：4.0 nV$/\sqrt{\mathrm{Hz}}$，`urms` $=0.57$ µ V，与上文相同。设 `Rx=1Meg`，并与你在练习 [8](#aufg-8) 中的结果比较。

⁠**$kT/C$：**电压源 `voltage` `V1`，值为 0 和 `AC 1`；`res` 取 `{Rx}`，接到 `out`；`cap` 取 `1p`，接地。指令 `.step param Rx list 1k 1Meg` 和 `.noise V(out) V1 dec 200 1 1T`，再加上 `.temp 16.85` 以及同样的测量语句 `urms`。两个电阻得到的 `urms` 相同。把这个值与你在练习 [9](#aufg-9)(b) 中的结果比较。
:::

:::aufgabe 练习 8 ★ 电阻的噪声
<span class="anker" id="aufg-8"></span>

计算一个 $1\,\mathrm{M\Omega}$ 电阻在 290 K、20 kHz 带宽下的噪声电压有效值。它是 $1\,\mathrm{k\Omega}$ 电阻的多少倍？为什么恰好是这个倍数？

:::loesung
有效值随 $\sqrt R$ 增长：变为 $\sqrt{1000}=31.6$ 倍，因此为 $0.566\cdot31.6=17.9$ µ V。
:::
:::

:::aufgabe 练习 9 ★★ $kT/C$ 噪声
<span class="anker" id="aufg-9"></span>

电阻的热噪声（$N_0=2kTR$）通过该电阻与电容 $C$ 构成的 RC 电路（$h(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$）。

<ol class="al">

<li>

利用式 [(9.1)](#gl-9-1) 证明：电容上的噪声功率为 $kT/C$，与 $R$ 无关。

</li>

<li>

当 $C=1$ pF、温度为 290 K 时，有效值是多少？为什么在这里减小电阻无济于事？

</li>

</ol>

:::loesung
(a) $\int h^2\mathrm{d} t=\frac{1}{(RC)^2}\int_0^\infty\mathrm{e}^{-2t/RC}\mathrm{d} t=\frac{1}{2RC}$。因此 $L=N_0\cdot\frac{1}{2RC}=\frac{2kTR}{2RC}=\frac{kT}{C}$。

(b) $\sqrt{4\cdot10^{-21}/10^{-12}}\,\mathrm{V}=\sqrt{4\cdot10^{-9}}\,\mathrm{V}=63$ µ V。较小的电阻在每赫兹上产生的噪声确实较少，但 RC 电路的频带随之变宽（$1/RC$ 变大）。两种效应恰好相互抵消。只有更大的电容才能减小噪声。
:::
:::
