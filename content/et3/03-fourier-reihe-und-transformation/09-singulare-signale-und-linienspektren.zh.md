---
title: 第 8 阶段：奇异信号与线谱
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 傅里叶级数与变换
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: 第 3 章：傅里叶级数与变换
order: 3230900
summary: 常数、振荡、阶跃和周期信号都不是绝对可积的。借助频谱中的狄拉克冲激，它们仍然可以进行变换。这样，傅里叶级数与傅里叶积分就统一起来了。
tags: 线谱, 狄拉克梳状函数（冲激串）
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
常数、振荡、阶跃和周期信号都不是绝对可积的。借助频谱中的狄拉克冲激，它们仍然可以进行变换。这样，傅里叶级数与傅里叶积分就统一起来了。
:::

:::satz 定理 8.1 (奇异变换对)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
<span class="anker" id="gl-8-5"></span>
<span class="anker" id="gl-8-6"></span>
<span class="anker" id="gl-8-7"></span>
$$\begin{aligned} \delta(t)&\;\circ\!\!-\!\!\bullet\;1, & c&\;\circ\!\!-\!\!\bullet\;c\,\delta(f),\\ \mathrm{e}^{\mathrm{j}2\pi Ft}&\;\circ\!\!-\!\!\bullet\;\delta(f-F), & \cos(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)+\tfrac12\delta(f-F),\\ & & \sin(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F),\\ \textstyle\sum_kS_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}&\;\circ\!\!-\!\!\bullet\;\textstyle\sum_kS_p(k)\,\delta(f-kF),\\ \textstyle\sum_n\delta(t-nT)&\;\circ\!\!-\!\!\bullet\;\frac{1}{|T|}\textstyle\sum_k\delta\Bigl(f-\frac kT\Bigr),\\ \varepsilon(t)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}, & \operatorname{sgn}(t)&\;\circ\!\!-\!\!\bullet\;\frac{1}{\mathrm{j}\pi f},\\ \int_{-\infty}^ts(\tau)\mathrm{d}\tau&\;\circ\!\!-\!\!\bullet\;\frac{S(f)}{\mathrm{j}2\pi f}+\tfrac12S(0)\,\delta(f). \end{aligned} \tag{8.1|8.2|8.3|8.4|8.5|8.6|8.7}$$
:::

⁠**如何理解：**

<ul>

<li>

常数是频率为 0 的振荡，它的频谱是 $f=0$ 处的一条谱线。振荡 $\mathrm{e}^{\mathrm{j}2\pi Ft}$ 是 $F$ 处的一条谱线。实余弦在 $\pm F$ 处有两条权重减半的谱线。

</li>

<li>

周期信号具有__线谱__：位于各次谐波处的狄拉克冲激，以傅里叶系数为权重。因此，傅里叶级数是傅里叶积分的一个特例。

</li>

<li>

__狄拉克梳状函数（冲激串）__，即间隔为 $T$ 的一串冲激，其频谱仍是狄拉克梳状函数，间隔为 $1/T$，权重为 $1/|T|$（图 [7](#abb-7)）。

</li>

<li>

阶跃具有直流分量 $\frac12$（谱线 $\frac12\delta(f)$）和交流分量 $\frac12\operatorname{sgn}(t)$，后者的频谱按 $1/f$ 衰减。

</li>

</ul>

:::herleitung 奇异变换对
⁠**常数、振荡：**对 $\delta(t)\circ\!\!-\!\!\bullet\,1$ 应用对偶性：$1\circ\!\!-\!\!\bullet\,\delta(-f)=\delta(f)$。调制使谱线移动：$\mathrm{e}^{\mathrm{j}2\pi Ft}\cdot1\circ\!\!-\!\!\bullet\,\delta(f-F)$。余弦和正弦由欧拉公式得到。

⁠**线谱：**对所有谐波叠加。

⁠**狄拉克梳状函数：**它以 $T$ 为周期。其傅里叶系数为 $S_p(k)=\frac1T\int_{-T/2}^{T/2}\delta(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac1T$，对所有 $k$ 均成立。结合线谱即得式 [(8.5)](#gl-8-5)。

⁠**符号函数：**$\operatorname{sgn}(t)$ 是 $\operatorname{sgn}(t)\mathrm{e}^{-a|t|}$ 在 $a\to0$ 时的极限情况：

$$\int_0^\infty\mathrm{e}^{-(a+\mathrm{j}2\pi f)t}\mathrm{d} t-\int_{-\infty}^0\mathrm{e}^{(a-\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{a+\mathrm{j}2\pi f}-\frac{1}{a-\mathrm{j}2\pi f}=\frac{-\mathrm{j}4\pi f}{a^2+(2\pi f)^2}\;\xrightarrow{a\to0}\;\frac{1}{\mathrm{j}\pi f}.$$

⁠**阶跃：**$\varepsilon(t)=\frac12+\frac12\operatorname{sgn}(t)$，因此为 $\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$。

⁠**积分：**$\int_{-\infty}^ts\,\mathrm{d}\tau=s*\varepsilon$，再利用卷积定理和筛选性质 $S(f)\delta(f)=S(0)\delta(f)$。
:::

:::abbildung et3/k3kamm 7
$T=0.5$ s 的狄拉克梳状函数及其频谱：仍是梳状函数，间隔为 $1/T=2$ Hz，权重为 $1/T=2$。时域中冲激越密，谱线相距越远。
:::

:::frage 可是由 $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$ 可得 $\mathrm{j}2\pi f\,S(f)=1$，所以 $S(f)=\frac{1}{\mathrm{j}2\pi f}$。那么 $\frac12\delta(f)$ 是从哪里来的？
方程 $\mathrm{j}2\pi f\,S(f)=1$ 只在 $f\neq0$ 处确定 $S$。在 $f=0$ 处，左边为 $0\cdot S(0)$；$S$ 中若含有一项 $c\,\delta(f)$，它会因 $f\delta(f)=0$ 而被消去。这与求导会“遗忘”常数相对应：$\varepsilon(t)$ 与 $\varepsilon(t)+b$ 具有相同的导数。哪个常数是正确的，由偶部决定：$\varepsilon$ 的平均值为 $\frac12$，所以 $c=\frac12$。
:::

::::beispiel 接通的余弦
$\varepsilon(t)\cos(2\pi Ft)$。相乘变为卷积，而与狄拉克冲激卷积就是平移：

$$\Bigl[\tfrac12\delta(f)+\tfrac{1}{\mathrm{j}2\pi f}\Bigr]*\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr] =\tfrac14\bigl[\delta(f+F)+\delta(f-F)\bigr]-\frac{\mathrm{j}}{4\pi}\Bigl[\frac{1}{f+F}+\frac{1}{f-F}\Bigr].$$

除了 $\pm F$ 处减半的谱线外，还出现了一个宽的频谱：接通过程本身包含 $\pm F$ 附近的频率。
::::

:::aufgabe 练习 10 ★ 线谱
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

给出 $s(t)=3+2\cos(2\pi\cdot50\,\mathrm{Hz}\cdot t)$ 的频谱，并画出草图。

</li>

<li>

给出参考模型中方波在 $|f|\le0.5$ Hz 范围内的频谱。

</li>

</ol>

:::loesung
(a) $3\,\delta(f)+\delta(f-50\,\mathrm{Hz})+\delta(f+50\,\mathrm{Hz})$：零频处一条权重为 3 的谱线，$\pm50$ Hz 处两条权重为 1 的谱线。

(b) $F=0.159$ Hz。0.5 Hz 以内有 $k=0,\pm1,\pm2,\pm3$，但 $k=\pm2$ 不存在：

$$0.5\,\delta(f)+0.318\bigl[\delta(f-0.159)+\delta(f+0.159)\bigr]-0.106\bigl[\delta(f-0.477)+\delta(f+0.477)\bigr].$$
:::
:::

:::aufgabe 练习 11 ★★ 符号函数与积分
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

用式 [(5.2)](symmetrien-im-signal-und-im-spektrum.html#gl-5-2) 验证：$\operatorname{sgn}(t)$ 的频谱必定是纯虚的奇函数。

</li>

<li>

用式 [(8.7)](#gl-8-7) 计算 $\int_{-\infty}^t\operatorname{rect}(\tau)\mathrm{d}\tau$ 的频谱。这是什么信号？

</li>

</ol>

:::loesung
(a) $\frac{1}{\mathrm{j}\pi f}=-\frac{\mathrm{j}}{\pi f}$：纯虚；且 $-\frac{\mathrm{j}}{\pi(-f)}=+\frac{\mathrm{j}}{\pi f}$，所以是奇函数。这与实的奇信号相符。

(b) $\frac{\operatorname{si}(\pi f)}{\mathrm{j}2\pi f}+\frac12\delta(f)$。该信号是矩形的变上限积分：$t\le-\frac12$ 时为 0，然后是一段斜坡，在 $t=\frac12$ 处升到 1，此后恒为 1。它在全部时间上的平均值为 $\frac12$，因此有 $\frac12\delta(f)$。
:::
:::
