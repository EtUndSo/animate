---
title: 第 8 阶段：LTI 系统中的随机信号与功率谱密度
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 随机信号
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: 第 7 章：随机信号
order: 3270900
summary: LTI 系统对随机信号有什么作用？每个样本函数都被卷积。因此，平均值遵循简单的规则。
tags: 功率谱密度
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
LTI 系统对随机信号有什么作用？每个样本函数都被卷积。因此，平均值遵循简单的规则。
:::

**均值。** 对每个样本函数有 ${}^kg={}^ks*h$。数学期望是线性的，可以移入卷积积分之中：

<span class="anker" id="gl-8-1"></span>
$$m_g=\mathrm E\Bigl\{\int s(\tau)h(t-\tau)\mathrm{d}\tau\Bigr\}=\int\mathrm E\{s(\tau)\}\,h(t-\tau)\,\mathrm{d}\tau=m_s\int h\,\mathrm{d}\tau=m_s\,H(0). \tag{8.1}$$

均值像直流分量一样被传输。

:::satz 定理 8.1 (平稳过程的维纳–李关系)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)*\varphi^E_{hh}(\tau),\qquad\Phi_{gg}(f)=\Phi_{ss}(f)\,|H(f)|^2, \tag{8.2}$$

其中 $\varphi^E_{hh}(\tau)=\int h(\vartheta)h(\vartheta+\tau)\mathrm{d}\vartheta$ 是冲激响应的自相关函数（确定性自相关函数），$\Phi_{ss}(f)\;\bullet\!\!-\!\!\circ\;\varphi_{ss}(\tau)$ 称为__功率谱密度__。功率为

<span class="anker" id="gl-8-3"></span>
$$L_s=\varphi_{ss}(0)=\int_{-\infty}^{\infty}\Phi_{ss}(f)\,\mathrm{d} f. \tag{8.3}$$
:::

:::herleitung 维纳–李关系
写出两个卷积积分，使用不同的积分变量：

$$g(t)g(t+\tau)=\iint s(t-\alpha)\,s(t+\tau-\beta)\,h(\alpha)h(\beta)\,\mathrm{d}\alpha\,\mathrm{d}\beta.$$

把数学期望移入二重积分。对平稳过程，$\mathrm E\{s(t-\alpha)s(t+\tau-\beta)\}=\varphi_{ss}(\tau-\beta+\alpha)$。令 $\vartheta=\beta-\alpha$：

$$\varphi_{gg}(\tau)=\int\varphi_{ss}(\tau-\vartheta)\underbrace{\int h(\alpha)h(\alpha+\vartheta)\,\mathrm{d}\alpha}_{\varphi^E_{hh}(\vartheta)}\,\mathrm{d}\vartheta=\varphi_{ss}*\varphi^E_{hh}.$$

在频域中，$\varphi^E_{hh}$ 变为 $|H|^2$（[第 6 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)）。
:::

⁠**如何理解：**$\Phi_{ss}(f)$ 表示功率如何分布在各个频率上。它是实的，永不为负，对实信号而言是偶函数。LTI 系统把每个频率上的功率乘以 $|H(f)|^2$，系统的相位不起作用。这与[第 6 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)中能量信号的规则相同，只是现在用于随机过程。（注：严格地说，$\Phi_{ss}$ 定义为对持续时间为 $T$ 的信号片段的短时频谱所取的极限 $\lim_{T\to\infty}\frac1T\mathrm E\{|S_T(f)|^2\}$。这一极限与自相关函数的傅里叶变换相同，这才是维纳–辛钦定理真正的内容。）

:::ltspice 带均值的噪声通过低通和高通
⁠**绘制：**行为源 `bv` 接在节点 `s` 上，取 `V=1+white(1e3*time)`。`white(x)` 给出 $-0.5$ 与 $0.5$ 之间的随机值，在每个整数 $x$ 处取一个新值，相邻值之间平滑过渡，因此这里每毫秒取一个新值。与它并联一个 RC 低通（`res` 取 `1Meg`，接到 `tp`；`cap` 取 `1u`，接地）和一个 CR 高通（`cap` 取 `1u`，接到 `hp`；`res` 取 `1Meg`，接地）。

⁠**指令：**`.tran 0 200 0 0.1m`。

⁠**读数：**把显示范围缩放到 20 s 至 200 s，即暂态过程结束之后的时间段。按住 Ctrl 键单击曲线名称，就会显示可见范围内的均值（Average）和有效值（RMS）。

⁠**你会看到：**输入的均值为 1 V。把 `V(tp)` 和 `V(hp)` 的均值与你在练习 [7](#aufg-7) 中的结果比较。低通输出的起伏要小得多：画出 `V(s)-1` 和 `V(tp)-1`，它们的有效值约为 0.25 和 0.01。低通大致只让宽广的功率谱密度中低于 $1/(2\pi RC)=0.16$ Hz 的部分通过，而根据式 [(8.3)](#gl-8-3)，功率就是功率谱密度曲线下的面积。
:::

:::aufgabe 练习 7 ★ 均值通过滤波器
<span class="anker" id="aufg-7"></span>

均值为 1 V 的噪声分别通过一个 RC 低通滤波器和一个 CR 高通滤波器。两个输出的均值各是多少？为什么？

:::loesung
RC 低通滤波器：$H(0)=1$，均值为 1 V。CR 高通滤波器：$H(0)=0$，均值为 0。电容不让直流电流通过，因此直流分量被阻断。
:::
:::
