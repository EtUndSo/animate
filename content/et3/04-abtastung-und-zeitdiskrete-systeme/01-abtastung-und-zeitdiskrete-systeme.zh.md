---
title: 采样与离散时间系统
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 采样与离散时间系统
order: 3240100
summary: 从连续信号到数值序列： 采样定理、离散卷积、DFT、FFT 与 z 变换
tags: 样本值, 模拟, 离散时间, 数字, 理想采样器, 频谱镜像, 低通（带限）信号, 奈奎斯特率
lang: zh
---

## 本文内容

计算机无法存储函数 $s(t)$，只能存储数值序列。因此，人们以固定的时间间隔 $T$ 测量信号，并用__样本值__ $s(nT)$ 进行计算。本文围绕两个问题展开：**这一过程会丢失信息吗？**以及：**怎样像第 1 至[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)对函数所做的那样，对数值序列进行计算？**

:::merke 三句话的答案（读完本文后应觉得理所当然）
<ol>

<li>

采样就是乘以狄拉克梳状函数。在频谱中，它变成与一个梳状函数的卷积：频谱以采样率为周期重复。

</li>

<li>

如果这些重复的部分互不重叠（采样率高于最高频率的两倍），就可以用理想低通滤波器精确地恢复信号。否则就会产生混叠。

</li>

<li>

适用于函数的工具同样适用于数值序列：求和形式的卷积、具有周期频谱的傅里叶变换、作为该频谱样本值的 DFT，以及与拉普拉斯变换相对应的 z 变换。

</li>

</ol>
:::

**所有结论背后的同一个原理：一个域中离散，意味着另一个域中周期。**

| 结论 | 来源 |
|---|---|
| 采样后的周期频谱 | 时间离散 $\Rightarrow$ 频谱周期（第 [2](#stufe-2) 阶段） |
| 采样定理、混叠 | 周期性的各个副本是否重叠（第 [3](#stufe-3) 阶段） |
| si 内插 | 理想低通滤波器截取出一个副本（第 [3](#stufe-3) 阶段） |
| 傅里叶级数 | 频谱离散 $\Rightarrow$ 时间周期（第 [4](#stufe-4) 阶段） |
| 离散卷积 | 对以样本值加权的狄拉克冲激求卷积积分（第 [5](#stufe-5) 阶段） |
| 离散时间傅里叶变换 | 样本值的频谱，周期为 1（第 [7](#stufe-7) 阶段） |
| DFT | 两边都离散 $\Rightarrow$ 两边都周期（第 [8](#stufe-8) 阶段） |
| 抽取、内插 | 对已采样的序列再次采样（第 [10](#stufe-10) 阶段） |
| z 变换 | 把拉普拉斯变换的思路用于序列：先加权，再变换（第 [11](#stufe-11) 阶段） |

**如何使用本文。**每个阶段包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。

:::merke 本文的参考模型
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

## 第 1 阶段：信号类别与理想采样

<span class="anker" id="stufe-1"></span>

:::zweck
信号有哪些类型？采样在数学上如何描述？
:::

**四种类别。** 时间和幅度都可以是连续的或离散的。__模拟__信号在这两方面都是连续的。__离散时间__信号只在时刻 $nT$ 有取值，但这些取值可以任意精确。__数字__信号的幅度还是分级的（量化），因为计算机只能表示有限多个数。本文讨论时间的离散化。幅度的量化是另一个专题。

**从实际采样器到理想采样器。** 实际采样器在每个采样周期内将开关闭合一段很短的时间 $T_0$：

<span class="anker" id="gl-1-1"></span>
$$s_0(t)=s(t)\sum_{n=-\infty}^{\infty}\operatorname{rect}\Bigl(\frac{t-nT}{T_0}\Bigr)=s(t)\Bigl[\operatorname{rect}\Bigl(\frac{t}{T_0}\Bigr)*\sum_n\delta(t-nT)\Bigr]. \tag{1.1}$$

若使 $T_0$ 越来越短，就只剩下取值 $s(nT)$。在数学上，用狄拉克冲激代替矩形。这就是__理想采样器__：

<span class="anker" id="gl-1-2"></span>
$$s_\mathrm a(t)=s(t)\sum_{n=-\infty}^{\infty}\delta(t-nT)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT). \tag{1.2}$$

采样信号是一串狄拉克冲激，每个冲激以一个样本值为权重。第二步用到的是筛选性质 $s(t)\delta(t-nT)=s(nT)\delta(t-nT)$。写成这种形式后，采样信号就可以用处理连续信号的全部工具来处理。

## 第 2 阶段：采样信号的频谱

<span class="anker" id="stufe-2"></span>

:::zweck
采样对频谱有什么影响？本阶段将表明：频谱周期性地重复。
:::

**思路。** 频率相差采样率 $1/T$ 整数倍的两个振荡，具有相同的样本值：

$$\mathrm{e}^{\mathrm{j}2\pi(f_0+k/T)nT}=\mathrm{e}^{\mathrm{j}2\pi f_0nT}\cdot\underbrace{\mathrm{e}^{\mathrm{j}2\pi kn}}_{=1}.$$

样本值无法区分它们。因此，样本值的频谱在 $f_0$ 处和在 $f_0+k/T$ 处必定一样。频谱是周期性的。

:::satz 定理 2.1 (理想采样信号的频谱)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$S_\mathrm a(f)=\frac1T\sum_{k=-\infty}^{\infty}S\Bigl(f-\frac kT\Bigr)\qquad(T>0). \tag{2.1}$$
:::

⁠**如何理解：**原信号的频谱以不变的形状出现，但乘上了因子 $1/T$，并在采样率的每个整数倍处重复出现。这些副本称为__频谱镜像__。

:::herleitung 采样信号的频谱
相乘变为卷积（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)），而狄拉克梳状函数的频谱仍是梳状函数：

$$s(t)\cdot\sum_n\delta(t-nT)\;\circ\!\!-\!\!\bullet\;S(f)*\frac1T\sum_k\delta\Bigl(f-\frac kT\Bigr)=\frac1T\sum_kS\Bigl(f-\frac kT\Bigr).$$

与平移后的狄拉克冲激做卷积，就是把频谱平移。
:::

:::abbildung et3/k4spektrum
对一个最高频率为 $f_\mathrm g=300$ Hz 的频谱（蓝色，为直观起见画成三角形）进行采样。上：以 1 kHz 采样，位于 1 kHz 整数倍处的副本相互分开。下：以 500 Hz 采样，间隔 500 Hz 的副本相互重叠，其和（红色）不再是原频谱。图中略去了因子 $1/T$。
:::

:::frage 频谱是怎么“知道”信号被采样过的？采样点之间的信号明明就这样没有了。
正是因为这一点。在采样点之间，采样信号为零，只有冲激处例外。凡是在所有点 $nT$ 上取值都相同的振荡，都同样好地描述了这个信号。频谱无法在它们之间做出选择，于是把它们全部包含进来：原信号以及它位于 $1/T$ 每个整数倍处的副本。
:::

## 第 3 阶段：采样定理与信号恢复

<span class="anker" id="stufe-3"></span>

:::zweck
什么时候能由样本值精确地恢复原信号？怎样恢复？
:::

:::satz 定理 3.1 (采样定理)
<span class="anker" id="satz-3-1"></span>

一个频谱在 $f_\mathrm g$ 以上为零的信号（__低通（带限）信号__）由其样本值 $s(nT)$ 唯一确定，条件是

<span class="anker" id="gl-3-1"></span>
$$T\le\frac{1}{2f_\mathrm g}\qquad\text{即}\qquad f_\mathrm A=\frac1T\ge2f_\mathrm g. \tag{3.1}$$

利用理想低通滤波器 $H_\mathrm{TP}(f)=T\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$，有

<span class="anker" id="gl-3-2"></span>
$$s(t)=s_\mathrm a(t)*\bigl[2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)\bigr], \tag{3.2}$$

当 $T=1/(2f_\mathrm g)$ 时：

<span class="anker" id="gl-3-3"></span>
$$s(t)=\sum_{n=-\infty}^{\infty}s(nT)\,\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr). \tag{3.3}$$
:::

⁠**如何理解：**当 $f_\mathrm A\ge2f_\mathrm g$ 时，图 [1](#abb-1) 中的各副本相互分开。低通滤波器截取出位于 $f=0$ 处的副本，它恰好具有原频谱的形状。在时域中，这意味着：每个样本值都被一个 si 函数代替，该函数在它自己的采样点处为 1，在其他所有采样点处为零（图 [2](#abb-2)）。这些函数之和经过所有样本值，并以不产生任何高于 $f_\mathrm g$ 的频率的方式填补其间的空隙。最低采样率 $2f_\mathrm g$ 称为__奈奎斯特率__。

:::herleitung 信号恢复
在 $|f|\le f_\mathrm g$ 内只有副本 $k=0$，因此 $S_\mathrm a(f)=\frac1TS(f)$。取 $H_\mathrm{TP}=T\operatorname{rect}(f/2f_\mathrm g)$，则 $S_\mathrm a\cdot H_\mathrm{TP}=S$。在时域中：$T\operatorname{rect}(f/2f_\mathrm g)\;\bullet\!\!-\!\!\circ\;2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)$（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)，矩形与 si 函数）。利用式 [(1.2)](#gl-1-2) 和 $2f_\mathrm g=1/T$，得到 $s_\mathrm a*\operatorname{si}(\pi t/T)=\sum_ns(nT)\operatorname{si}(\pi(t-nT)/T)$。
:::

:::abbildung et3/k4siinterp
si 内插：样本值 $0,\ 1,\ 0.6,\ -0.4,\ 0.8,\ 0$（红色）、加权后的 si 函数（灰色）及其和（蓝色）。每个 si 函数在其他采样点处都为零，因此其和精确地经过所有样本值。
:::

**混叠。** 如果采样太慢，各副本就会重叠。高于 $f_\mathrm A/2$ 的频率在恢复后表现为一个错误的、较低的频率，即它的__混叠频率__。在参考模型中，当 $f_\mathrm A=1$ kHz 时，700 Hz 的余弦与 300 Hz 的余弦具有完全相同的样本值，因为 $\cos(2\pi\cdot0.7n)=\cos(2\pi n-2\pi\cdot0.3n)=\cos(2\pi\cdot0.3n)$（图 [3](#abb-3)）。事后已无法再将二者分开。因此，在每个采样器之前都要用低通滤波器对信号进行滤波（__抗混叠滤波器__）。

:::abbildung et3/k4alias
当 $f_\mathrm A=1$ kHz 时，700 Hz 与 300 Hz 的样本值（黑色）重合。700 Hz 高于 $f_\mathrm A/2=500$ Hz，表现为 300 Hz 处的混叠频率。
:::

:::frage 恰好取 $f_\mathrm A=2f_\mathrm g$ 难道不够吗？对于频率恰为 $f_\mathrm g$ 的正弦，这样做明明会出错。
对，恰好在边界上会出错：在相位不利的情况下，频率为 $f_\mathrm g=f_\mathrm A/2$ 的正弦可能每次都恰好在过零点处被采样，于是所有样本值都为零。因此，严格地说，该定理要求频谱*在* $f_\mathrm g$ 处没有谱线，或者 $f_\mathrm A>2f_\mathrm g$。实际上人们本来就会采样得更快，因为实际的低通滤波器并不是垂直下降的，需要为其过渡带留出空间。
:::

:::ltspice 采样保持：看见混叠
⁠**绘制：**电压源 `voltage` 接在节点 `in` 上，取 `SINE(0 1 700 0 0 90)`，即 700 Hz 的余弦。开关 `sw`（值为 `SW1`）从 `in` 接到 `sh`，在 `sh` 处接一个 `cap`，取 `100n`，接地。第二个信号源取 `PULSE(0 1 0 10n 10n 1u 1m)`，驱动开关的控制输入：开关每毫秒闭合 1 µ s（$f_\mathrm A=1$ kHz），其间电容保持样本值。`sh` 之后接一个输出为 `out` 的 `e` 源，作为恢复信号用的低通。它是一个截止频率为 400 Hz 的 4 阶巴特沃斯低通（通带尽可能平坦），其值为

`Laplace=1/(((s/wg)**2+0.7654*s/wg+1)*((s/wg)**2+1.8478*s/wg+1))`

⁠**指令：**`.model SW1 SW(Ron=1 Roff=1G Vt=0.5)`，`.param wg=2*pi*400`，`.tran 0 40m 0 1u`，`.options plotwinsize=0`，`.four 100 15 V(sh) V(out)`。

⁠**你会看到：**`sh` 处的阶梯波跟随一个 300 Hz 的振荡，而 `out` 处出现的是 300 Hz 而不是 700 Hz 的余弦。在 `.four` 的结果中，300 Hz 处的谱线最强。改用 `SINE(0 1 300 0 0 90)` 时，出现同样的阶梯波。设为 1.2 kHz，并与你在练习 [1](#aufg-1)(a) 中的结果比较。

⁠**抗混叠：**在开关前面再放一个相同的 `e` 源。输入为 700 Hz 时，`out` 处 300 Hz 的谱线降到约十分之一，而 300 Hz 的输入几乎不受衰减地通过。因此，必须在采样之前防止混叠：采样之后，它就再也无法与真正的 300 Hz 信号区分开了。
:::

:::aufgabe 练习 1 ★ 混叠频率
<span class="anker" id="aufg-1"></span>

$f_\mathrm A=1$ kHz。

<ol class="al">

<li>

1.2 kHz 的余弦在恢复后表现为什么频率？

</li>

<li>

哪些频率与 50 Hz 的余弦给出相同的样本值？

</li>

</ol>

:::loesung
(a) 1.2 kHz 高于 $f_\mathrm A/2$。它与 $1.2-1=0.2$ kHz 具有相同的样本值，表现为 200 Hz。

(b) 所有 $\pm50\,\mathrm{Hz}+k\cdot1\,\mathrm{kHz}$：950 Hz、1050 Hz、1950 Hz、2050 Hz，依此类推。对余弦而言，负频率与正频率是等价的，因此 $1000-50$ 也属于其中。
:::
:::

:::aufgabe 练习 2 ★★ 实际中的采样率
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

电话语音被限制在 3.4 kHz 以内，并以 8 kHz 采样。奈奎斯特率是多少？留出的余量有什么用？

</li>

<li>

音频 CD 以 44.1 kHz 采样。它最高能存储多高频率的声音？若可听频带延伸到 20 kHz，留给抗混叠滤波器的过渡带有多宽？

</li>

</ol>

:::loesung
(a) 奈奎斯特率为 $2\cdot3.4=6.8$ kHz。采样率为 8 kHz 时，$f_\mathrm A/2$ 位于 4 kHz。在 3.4 kHz 与 4 kHz 之间，抗混叠滤波器有空间从通带过渡到阻带。

(b) 最高到 $f_\mathrm A/2=22.05$ kHz。从 20 kHz 到 22.05 kHz 的过渡带只有 2.05 kHz 宽。因此需要陡峭的滤波器或过采样。
:::
:::

:::aufgabe 练习 3 ★★ 手算 si 内插
<span class="anker" id="aufg-3"></span>

用式 [(3.3)](#gl-3-3) 计算图 [2](#abb-2) 中信号在 $t=2.5T$ 处的值。提示：$\operatorname{si}(\pi\cdot0.5)=2/\pi$，$\operatorname{si}(\pi\cdot1.5)=-2/(3\pi)$。哪些样本值没有贡献？

:::loesung
在 $t=2.5T$ 处，$\operatorname{si}(\pi(2.5-k))$ 在 $k\in\{2,3\}$ 时等于 $\frac2\pi$，在 $k\in\{1,4\}$ 时等于 $-\frac{2}{3\pi}$。$k=0$ 和 $k=5$ 处的样本值为零，没有贡献：

$$s(2.5T)=\frac2\pi\Bigl[-\tfrac13\cdot1+0.6-0.4-\tfrac13\cdot0.8\Bigr]=\frac2\pi\cdot(-0.4)=-0.255.$$
:::
:::

## 第 4 阶段：频域采样

<span class="anker" id="stufe-4"></span>

:::zweck
角色互换后，同一原理依然成立：对频谱采样，信号就变为周期的。
:::

只在频率 $kF$ 处已知的频谱，是由加权狄拉克冲激组成的梳状函数。乘上因子 $F$ 后，各权重恰好就是[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中的傅里叶系数：

<span class="anker" id="gl-4-1"></span>
$$S_p(f)=F\sum_kS(kF)\,\delta(f-kF)=F\,S(f)\cdot\sum_k\delta(f-kF)\;\bullet\!\!-\!\!\circ\;s_p(t)=\sum_ns\Bigl(t-\frac nF\Bigr). \tag{4.1}$$

对应的信号是以 $1/F$ 为周期重复的原信号。若信号的持续时间短于 $1/F$，各次重复就不会重叠。这时可以用一个时间窗恢复信号，并用 si 函数恢复频谱：

<span class="anker" id="gl-4-2"></span>
$$s(t)=s_p(t)\cdot\operatorname{rect}(Ft)\qquad\Longrightarrow\qquad S(f)=\sum_kS(kF)\operatorname{si}\Bigl(\pi\frac{f-kF}{F}\Bigr). \tag{4.2}$$

⁠**简而言之：**时间离散意味着频谱周期，频谱离散意味着时间周期。后者就是[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中的傅里叶级数：其系数是单个脉冲频谱的样本值，$S_p(k)=F\cdot S(kF)$。

## 第 5 阶段：离散时间信号与离散卷积

<span class="anker" id="stufe-5"></span>

:::zweck
从现在起，所有计算都只使用数值序列 $s(n)$。本阶段把卷积、基本信号和 LTI 系统推广到序列。
:::

**样本值的卷积。** 若系统的输入 $s$ 和冲激响应 $h$ 都是低通信号，并以奈奎斯特率采样，则二者都可以写成 si 级数 [(3.3)](#gl-3-3)。由于 $\operatorname{si}(\pi t/T)*\operatorname{si}(\pi t/T)=T\operatorname{si}(\pi t/T)$（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)），输出的样本值仅由样本值即可求得：

$$g(nT)=T\sum_{m=-\infty}^{\infty}s(mT)\,h\bigl((n-m)T\bigr).$$

归一化到 $T=1$ 后，这就是__离散卷积__：

<span class="anker" id="gl-5-1"></span>
$$g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(n-m)=s(n)*h(n). \tag{5.1}$$

**基本序列。**

$$\delta(n)=\begin{cases}1&n=0\\0&n\neq0\end{cases},\qquad \varepsilon(n)=\sum_{m=-\infty}^n\delta(m)=\begin{cases}0&n<0\\1&n\ge0\end{cases},\qquad \varepsilon(n)\,a^n,\qquad \mathrm{e}^{\mathrm{j}2\pi Fn}.$$

__单位脉冲__ $\delta(n)$ 是普通的序列，而不是广义函数：它在 $n=0$ 处取值 1。它是离散卷积的单位元，$s(n)*\delta(n)=s(n)$。以 $n=0$ 为中心、由 $2M+1$ 个 1 组成的矩形序列为 $\varepsilon(n+M)-\varepsilon(n-M-1)$。

**线性与移不变。** 若叠加原理成立，则称离散时间系统是线性的；若对每个整数 $m$ 都有 $\operatorname{Tr}\{s(n-m)\}=g(n-m)$，则称它是__移不变__的。同时具有这两个性质的系统称为__LSI 系统__。利用__单位脉冲响应__ $h(n)=\operatorname{Tr}\{\delta(n)\}$，与[第 1 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)一样可得

$$g(n)=\operatorname{Tr}\Bigl\{\sum_ms(m)\delta(n-m)\Bigr\}=\sum_ms(m)\operatorname{Tr}\{\delta(n-m)\}=\sum_ms(m)\,h(n-m).$$

这里不需要取极限：序列本身*就是*加权、平移后的单位脉冲之和。

**差分与求和。** 与导数相对应的是__差分__ $g(n)=s(n)-s(n-1)$，因此 $h(n)=\delta(n)-\delta(n-1)$。与积分相对应的是__累加__ $g(n)=\sum_{m\le n}s(m)=s(n)*\varepsilon(n)$。二者相互抵消：$[\delta(n)-\delta(n-1)]*\varepsilon(n)=\varepsilon(n)-\varepsilon(n-1)=\delta(n)$。

**差分方程、FIR 与 IIR。** 描述离散时间系统的不是微分方程，而是差分方程：

<span class="anker" id="gl-5-2"></span>
$$g(n)=\underbrace{\sum_{q=0}^{Q}a_q\,s(n-q)}_{\text{FIR 部分}}+\underbrace{\sum_{p=1}^{P}b_p\,g(n-p)}_{\text{IIR 部分}}. \tag{5.2}$$

输出是以往输入值和输出值的加权和。若输出只取决于输入值（$b_p=0$），单位脉冲响应在 $Q+1$ 个值之后就结束：这是__FIR 滤波器__（finite impulse response，有限长单位脉冲响应）。有反馈时（$b_p\neq0$），单位脉冲响应可以无限长：这是__IIR 滤波器__（infinite impulse response，无限长单位脉冲响应）。二者都由延时单元（存储一个采样周期的存储器）、乘法器和加法器构成（图 [4](#abb-4)）。

:::abbildung et3/k4block
一阶系统 $g(n)=a_0s(n)+a_1s(n-1)+b_1g(n-1)$。方框 $T$ 将一个值存储一个采样周期。左边是非递归部分，右边是输出的反馈。
:::

:::aufgabe 练习 4 ★ 手算离散卷积
<span class="anker" id="aufg-4"></span>

将 $s=(1,1,1)$ 与 $h=(1,2)$ 做卷积，二者均从 $n=0$ 开始。结果有多长？为什么？

:::loesung
$g(0)=1$，$g(1)=1\cdot2+1\cdot1=3$，$g(2)=3$，$g(3)=1\cdot2=2$：$(1,3,3,2)$。长度为 $3+2-1=4$：当 $h$ 的最后一个值与 $s$ 的最后一个值相遇时，产生最后一个非零值。
:::
:::

## 第 6 阶段：一个递归系统

<span class="anker" id="stufe-6"></span>

:::zweck
通过最简单的 IIR 系统可以看出：反馈如何产生无限长的单位脉冲响应，以及系统何时稳定。
:::

系统 $g(n)=s(n)+b\,g(n-1)$ 把以 $b$ 加权的上一个输出值加到输入上。对于 $s=\delta$，且系统在 $n=0$ 之前处于静止状态，有：

<span class="anker" id="gl-6-1"></span>
$$h(n)=\delta(n)+b\,h(n-1)\quad\Longrightarrow\quad h(0)=1,\ h(1)=b,\ h(2)=b^2,\dots\quad\Longrightarrow\quad h(n)=\varepsilon(n)\,b^n. \tag{6.1}$$

这个脉冲在反馈环路中一圈又一圈地循环，每循环一次就乘以 $b$。该系统是__因果__的（$n<0$ 时 $h(n)=0$）。若 $\sum_n|h(n)|<\infty$（[第 1 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)中条件的离散对应形式），则系统是__稳定__的；在这里，这恰好对应于 $|b|<1$，此时 $\sum_n|b|^n=\frac{1}{1-|b|}$。

**对矩形序列的响应。** 输入 $s(n)=\varepsilon(n)-\varepsilon(n-M)$（$M$ 个 1）。利用卷积和以及等比数列求和公式 $\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q}$：

<span class="anker" id="gl-6-2"></span>
$$g(n)=\begin{cases}0&n<0,\\[2pt]\displaystyle\sum_{m=0}^{n}b^{n-m}=\frac{1-b^{n+1}}{1-b}&0\le n<M,\\[8pt]\displaystyle\sum_{m=0}^{M-1}b^{n-m}=\frac{b^{n-M+1}-b^{n+1}}{1-b}&n\ge M.\end{cases} \tag{6.2}$$

在参考模型中（$b=0.6$，$M=4$）：$g=1,\ 1.6,\ 1.96,\ 2.176$，随后为 $1.306,\ 0.783,\ 0.470,\dots$，每个值都是前一个值的 0.6 倍（图 [5](#abb-5)）。这就是[第 1 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)中 RC 电路对矩形脉冲的响应在离散情形下的对应。

:::abbildung et3/k4rek
$b=0.6$ 的递归系统。左：单位脉冲响应。右：对四个 1 的响应；它上升到 2.176，然后每个采样周期按因子 0.6 衰减。
:::

:::aufgabe 练习 5 ★★ 研究递归系统
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

直接用递推式验证参考模型中 $g(n)$ 的前五个值。

</li>

<li>

对于无限长的全 1 序列（$M\to\infty$），输出趋于什么值？与 $\sum_nh(n)$ 进行比较。

</li>

<li>

当 $b=-0.6$ 和 $b=1.1$ 时，$h(n)$ 是什么样的？哪个系统是稳定的？

</li>

</ol>

:::loesung
(a) $g(0)=1$，$g(1)=1+0.6=1.6$，$g(2)=1+0.96=1.96$，$g(3)=1+1.176=2.176$，$g(4)=0+0.6\cdot2.176=1.306$。

(b) $\frac{1}{1-b}=2.5$。这正是 $\sum_nh(n)=\sum0.6^n=2.5$：对于恒定输入 1，卷积把单位脉冲响应的所有值加起来。此外，$H_\mathrm a(0)=2.5$。

(c) $b=-0.6$：$1,\ -0.6,\ 0.36,\ -0.216,\dots$，符号交替，逐渐衰减，稳定。$b=1.1$：$1,\ 1.1,\ 1.21,\dots$，不断增长，不稳定。
:::
:::

:::aufgabe 练习 6 ★★ 一阶系统
<span class="anker" id="aufg-6"></span>

$g(n)=s(n)+0.5\,s(n-1)+0.6\,g(n-1)$（即图 [4](#abb-4) 中 $a_0=1$，$a_1=0.5$，$b_1=0.6$）。

<ol class="al">

<li>

用递推式计算 $h(0)$ 到 $h(3)$。

</li>

<li>

证明 $h(n)=\frac{11}{6}\,0.6^n\varepsilon(n)-\frac56\delta(n)$。

</li>

</ol>

:::loesung
(a) $h(0)=1$，$h(1)=0.5+0.6\cdot1=1.1$，$h(2)=0.6\cdot1.1=0.66$，$h(3)=0.396$。

(b) 由该公式得 $h(0)=\frac{11}{6}-\frac56=1$，$h(1)=\frac{11}{6}\cdot0.6=1.1$。从 $n=2$ 起输入为零，递推式为 $h(n)=0.6\,h(n-1)$，而该公式满足这一递推式，因为 $\frac{11}{6}0.6^n=0.6\cdot\frac{11}{6}0.6^{n-1}$。（利用 z 变换，由分解式 $H(z)=-\frac56+\frac{11/6}{1-0.6z^{-1}}$ 即可得到该公式。）
:::
:::

## 第 7 阶段：离散时间傅里叶变换

<span class="anker" id="stufe-7"></span>

:::zweck
数值序列具有怎样的频谱？它就是理想采样信号的频谱，直接由样本值计算。
:::

把 $s_\mathrm a(t)=\sum_ns(nT)\delta(t-nT)$ 代入傅里叶积分，利用筛选性质后只剩下一个求和。归一化到 $T=1$ 后：

:::satz 定理 7.1 (离散时间傅里叶变换)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf},\qquad s(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f. \tag{7.1}$$
:::

⁠**如何理解：**$S_\mathrm a(f)$ 是周期为 1 的周期函数，而 1 正是采样率。一个周期 $|f|\le\frac12$ 就包含了全部信息。因此，反变换只需在长度为 1 的区间上积分。这个求和式是关于 $f$ 的傅里叶级数，以样本值为系数。

**例。** 对 $|b|<1$ 的 $s(n)=\varepsilon(n)\,b^n$（等比级数）：

<span class="anker" id="gl-7-2"></span>
$$S_\mathrm a(f)=\sum_{n=0}^{\infty}\bigl(b\,\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)^n=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}},\qquad|S_\mathrm a(f)|^2=\frac{1}{1+b^2-2b\cos(2\pi f)}. \tag{7.2}$$

这同时也是第 [6](#stufe-6) 阶段中递归系统的频率响应 $H_\mathrm a(f)$。当 $b=0.6$ 时：$f=0$ 处 $|H_\mathrm a|=2.5$，$f=0.1$ 处为 $1.60$，$f=0.25$ 处为 $0.86$，$f=0.5$ 处为 $0.625$（图 [6](#abb-6)）。该系统是低通滤波器，但其频率响应是周期性的：在 $f=1$ 处，它的放大作用又和 $f=0$ 处一样强。

:::abbildung et3/k4dtft
$b=0.6$ 的递归系统频率响应的幅值。它以采样率为周期。两条红线之间是足以描述全部信息的那一个周期。
:::

**卷积与相乘。** 与函数的情形一样，$s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)H_\mathrm a(f)$。两个序列的乘积对应于两个频谱在一个周期上的__周期卷积__：

<span class="anker" id="gl-7-3"></span>
$$s(n)\cdot h(n)\;\circ\!\!-\!\!\bullet\;\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu. \tag{7.3}$$

:::aufgabe 练习 7 ★ 滑动平均
<span class="anker" id="aufg-7"></span>

$h(n)=\frac13\bigl[\delta(n)+\delta(n-1)+\delta(n-2)\bigr]$ 对三个相继的值求平均。

<ol class="al">

<li>

证明 $H_\mathrm a(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$。

</li>

<li>

在哪个频率处 $H_\mathrm a=0$？因此该滤波器会完全消除哪个振荡？原因是什么（提示：周期为 3 的振荡的三个值之和）？

</li>

</ol>

:::loesung
(a) $\frac13\bigl(1+\mathrm{e}^{-\mathrm{j}2\pi f}+\mathrm{e}^{-\mathrm{j}4\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl(\mathrm{e}^{\mathrm{j}2\pi f}+1+\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$。

(b) $\cos(2\pi f)=-\frac12$，因此 $f=\frac13$（当 $f_\mathrm A=1$ kHz 时为 333 Hz）。每个周期有三个值的振荡由三个彼此相隔 $120^\circ$ 的相量组成。它们的和为零；在每个窗口中，滤波器看到的恰好是一个完整的周期。
:::
:::

## 第 8 阶段：离散傅里叶变换（DFT）

<span class="anker" id="stufe-8"></span>

:::zweck
$S_\mathrm a(f)$ 是连续函数，而计算机需要的是有限多个数。对于有限长序列，频谱的有限多个样本值就足够了。
:::

**思路。** 若 $s(n)$ 只有 $M$ 个值，那么根据第 [4](#stufe-4) 阶段，间隔为 $F=1/M$ 的频谱样本值就足够了。它们对应于以 $M$ 为周期重复的信号 $s_d(n)$。由于频谱也是周期的（时间离散），$M$ 个频谱值就足够了。现在两边都是离散且周期的。

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

## 第 9 阶段：FFT 与快速卷积

<span class="anker" id="stufe-9"></span>

:::zweck
DFT 需要 $M^2$ 次乘法。FFT 只需大约 $M\,\mathrm{lb}\,M$ 次。这样一来，经由频域计算卷积也变得很快。
:::

**FFT 的思路。** 令 $W_M=\mathrm{e}^{-\mathrm{j}2\pi/M}$，则 $S_d(k)=\sum_ns_d(n)W_M^{kn}$。当 $M$ 为偶数时，把序列分成下标为偶数和下标为奇数的两组值：

<span class="anker" id="gl-9-1"></span>
$$S_d(k)=\underbrace{\sum_{n=0}^{M/2-1}s_d(2n)\,W_{M/2}^{kn}}_{S_{d,1}(k)}+W_M^k\underbrace{\sum_{n=0}^{M/2-1}s_d(2n+1)\,W_{M/2}^{kn}}_{S_{d,2}(k)}, \tag{9.1}$$

这是因为 $W_M^{2kn}=W_{M/2}^{kn}$。这样，就不必做一次长度为 $M$ 的 DFT，而只需做两次长度为 $M/2$ 的 DFT，再加上 $M$ 次与 $W_M^k$ 的乘法，即 $2(M/2)^2+M$ 次，而不是 $M^2$ 次。两个部分 DFT 都以 $M/2$ 为周期，因此它们也给出了 $k\ge M/2$ 时的值。若 $M$ 是 2 的幂，就把这种拆分重复 $\mathrm{lb}\,M$ 次。计算量降到大约 $M\,\mathrm{lb}\,M$。对于 $M=1024$，这是 10,240 次乘法，而不是 1,048,576 次，大约少了一百倍。这就是__快速傅里叶变换__（FFT）。

**循环卷积。** 对于周期为 $M$ 的周期序列，__循环__（周期）卷积为

<span class="anker" id="gl-9-2"></span>
$$g_d(n)=\sum_{m=0}^{M-1}s_d(m)\,h_d\bigl((n-m)\bmod M\bigr)\;\circ\!\!-\!\!\bullet\;G_d(k)=S_d(k)\,H_d(k). \tag{9.2}$$

它是普通卷积结果的周期重复。若 $M$ 太小，各次重复就会重叠。对于 $s=(1,1,1)$ 和 $h=(1,2)$，普通卷积为 $(1,3,3,2)$，共四个值。取 $M=3$ 时，最后一个值落到第一个值上：$(3,3,3)$。取 $M=4$ 时结果正确：$(1,3,3,2)$。一般地，要求 $M\ge M_1+M_2-1$（$M_1$、$M_2$ 为两个序列的长度）；为此要对序列补零。

**快速卷积。** 不直接计算卷积和，而是用 FFT 对两个序列进行变换，相乘后再反变换回去。任意长的信号被分成若干块，每块分别做卷积，再把结果相加。之所以可以这样做，是因为卷积满足分配律：

$$s(n)*h(n)=\Bigl[\sum_is_i(n)\Bigr]*h(n)=\sum_i\bigl[s_i(n)*h(n)\bigr].$$

:::aufgabe 练习 9 ★★ 循环卷积还是线性卷积
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

手算 $(1,1,1)$ 与 $(1,2,0)$ 在 $M=3$ 时的循环卷积。线性卷积的哪个值移到了哪里？

</li>

<li>

一个有 1000 个值的信号要通过 DFT 与一个有 25 个值的滤波器做卷积。DFT 的长度至少应为多少？

</li>

</ol>

:::loesung
(a) $g(0)=s_0h_0+s_1h_2+s_2h_1=1+0+2=3$，$g(1)=s_0h_1+s_1h_0+s_2h_2=2+1+0=3$，$g(2)=s_0h_2+s_1h_1+s_2h_0=0+2+1=3$。线性卷积的第四个值（$n=3$ 处的 2）循环地移到了 $n=0$ 处：$1+2=3$。

(b) 至少为 $1000+25-1=1024$。它恰好是 2 的幂，十分方便。
:::
:::

## 第 10 阶段：改变采样率——抽取与内插

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

**按因子 $c$ 升采样。** 在每两个相邻值之间插入 $c-1$ 个零：当 $n$ 能被 $c$ 整除时 $s_\uparrow(n)=s(n/c)$，否则为 0。频谱被压缩 $c$ 倍，$S_{\uparrow,\mathrm a}(f)=S_\mathrm a(cf)$，并且在一个周期内包含 $c-1$ 个频谱镜像。截止频率为 $\frac{1}{2c}$、增益为 $c$ 的低通滤波器可以把它们滤除。在此过程中，滤波器用内插值填充这些零（即第 [3](#stufe-3) 阶段 si 内插的离散形式），而原有的值保持不变。先后进行降采样和升采样，可以使采样率改变一个有理因子 $c_1/c_2$。

:::abbildung et3/k4rate
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

## 第 11 阶段：z 变换

<span class="anker" id="stufe-11"></span>

:::zweck
正如拉普拉斯变换推广了傅里叶变换（[第 2 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)），z 变换推广了离散时间傅里叶变换：先进行指数加权，再进行变换。
:::

**思路。** 将序列乘以 $\rho^{-n}$（$\rho>0$）再做变换：$\sum_ns(n)\rho^{-n}\mathrm{e}^{-\mathrm{j}2\pi fn}$。令 $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$，它就变成关于 $z^{-1}$ 的幂级数。等价的说法是：$z^n$ 是每个 LSI 系统的特征函数，因为 $z^{n-k}=z^{-k}z^n$，而特征值为 $H(z)$：

$$z^n*h(n)=\sum_kh(k)z^{n-k}=z^n\sum_kh(k)z^{-k}=H(z)\,z^n.$$

:::satz 定理 11.1 (z 变换)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$S(z)=\sum_{n=-\infty}^{\infty}s(n)\,z^{-n},\qquad s(n)=\frac{1}{2\pi\mathrm{j}}\oint S(z)\,z^{n-1}\,\mathrm{d} z, \tag{11.1}$$

其中围线积分沿收敛域内的圆 $|z|=\rho$ 按逆时针方向进行。
:::

⁠**如何理解：**圆 $|z|=\rho$ 上分布着加权序列 $s(n)\rho^{-n}$ 的频谱的一个周期。在__单位圆__ $|z|=1$ 上，$S(z)$ 就是普通的频谱 $S_\mathrm a(f)$，前提是单位圆位于收敛域内。这样，拉普拉斯变换的复平面就映射到 z 平面上：虚轴变为单位圆，左半平面变为单位圆的内部。

**基本变换对与收敛域。** 利用等比级数可得：

<span class="anker" id="gl-11-2"></span>
$$\varepsilon(n)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{1}{1-bz^{-1}}=\frac{z}{z-b},\quad|z|>|b|;\qquad -\varepsilon(-n-1)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{z}{z-b},\quad|z|<|b|. \tag{11.2}$$

与拉普拉斯变换一样，同一个表达式属于两个信号，只有收敛域才能决定是哪一个。对于右边序列，收敛域位于经过最外侧极点的圆的外部；对于左边序列，它位于经过最内侧极点的圆的内部；对于双边序列，它是一个圆环。对于 $0<b<1$ 的 $b^{|n|}$，这个圆环是 $b<|z|<1/b$。

**运算规则。** 卷积变为乘积：$g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)H(z)$。延迟 $n_0$ 个采样周期变为乘以 $z^{-n_0}$。这样，差分方程 [(5.2)](#gl-5-2) 就变为

<span class="anker" id="gl-11-3"></span>
$$H(z)=\frac{G(z)}{S(z)}=\frac{\sum_{q=0}^{Q}a_q\,z^{-q}}{1-\sum_{p=1}^{P}b_p\,z^{-p}}. \tag{11.3}$$

对于练习 [6](#aufg-6) 中的系统，$H(z)=\frac{1+0.5z^{-1}}{1-0.6z^{-1}}$：零点位于 $z=-0.5$，极点位于 $z=0.6$。

:::satz 定理 11.2 (稳定性)
<span class="anker" id="satz-11-2"></span>

因果 LSI 系统稳定，当且仅当 $H(z)$ 的所有极点都位于单位圆内部。
:::

⁠**原因：**因果意味着收敛域位于最外侧极点之外。稳定意味着 $\sum|h(n)|<\infty$；这时 $H(z)$ 在单位圆上收敛，因此单位圆属于收敛域。只有当最外侧极点位于单位圆内部时，二者才能同时成立。对于 $H(z)=\frac{1}{1-bz^{-1}}$ 的递归系统，这又意味着 $|b|<1$。

**例。** $s(n)=0.5^n\cos(\pi n/3)\,\varepsilon(n)$。利用 $\cos=\frac12(\mathrm{e}^{\mathrm{j}\pi n/3}+\mathrm{e}^{-\mathrm{j}\pi n/3})$，并对 $b=0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}$ 应用式 [(11.2)](#gl-11-2)：

$$S(z)=\frac12\Bigl[\frac{1}{1-0.5\mathrm{e}^{\mathrm{j}\pi/3}z^{-1}}+\frac{1}{1-0.5\mathrm{e}^{-\mathrm{j}\pi/3}z^{-1}}\Bigr]=\frac{1-0.25z^{-1}}{1-0.5z^{-1}+0.25z^{-2}},\qquad|z|>0.5.$$

极点位于 $0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}=0.25\pm0.433\mathrm{j}$，零点位于 $z=0$ 和 $z=0.25$（图 [8](#abb-8)）。极点的模给出每个采样周期的衰减（0.5），极点的辐角给出振荡（每个采样周期 $\pi/3$，因此每个振荡周期包含六个采样周期）。

:::abbildung et3/k4zebene
例题的 z 平面：极点（叉号）位于 $0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}$，零点（圆圈）位于 0 和 0.25。收敛域（蓝色）位于经过极点的圆之外，并包含单位圆。若把该序列看作单位脉冲响应，它描述的是一个因果且稳定的系统。
:::

:::aufgabe 练习 11 ★★ 应用 z 变换
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

将两个分式通分，验证例题中 $S(z)$ 的分子和分母。

</li>

<li>

例题信号的频谱 $S_\mathrm a(f)$ 存在吗？用收敛域说明理由。

</li>

</ol>

:::loesung
(a) 公分母为 $(1-az^{-1})(1-a^*z^{-1})=1-(a+a^*)z^{-1}+|a|^2z^{-2}$，其中 $a=0.5\mathrm{e}^{\mathrm{j}\pi/3}$：$a+a^*=2\cdot0.25=0.5$，$|a|^2=0.25$。分子为 $\frac12[2-(a+a^*)z^{-1}]=1-0.25z^{-1}$。

(b) 存在。收敛域 $|z|>0.5$ 包含单位圆。
:::
:::

:::aufgabe 练习 12 ★★ 因果还是稳定
<span class="anker" id="aufg-12"></span>

$H(z)=\dfrac{1}{1-2z^{-1}}$。

<ol class="al">

<li>

收敛域 $|z|>2$ 对应哪个单位脉冲响应？收敛域 $|z|<2$ 又对应哪个？

</li>

<li>

两者中哪个是稳定的，哪个是因果的？是否存在既因果又稳定的？

</li>

</ol>

:::loesung
(a) $|z|>2$：$h(n)=2^n\varepsilon(n)$。$|z|<2$：$h(n)=-2^n\varepsilon(-n-1)$，即 $n=-1,-2,\dots$ 时为 $-\frac12,-\frac14,\dots$。

(b) 第一个是因果的，但不稳定（它不断增长）。第二个是稳定的（$\sum_{n\le-1}2^n=1$），但它是反因果的。二者不可能同时成立：极点 $z=2$ 位于单位圆之外，此时收敛域不可能既位于极点之外又包含单位圆。
:::
:::

:::kern 要点
<ul>

<li>

理想采样：$s_\mathrm a=\sum s(nT)\delta(t-nT)$；频谱为 $\frac1T\sum_kS(f-k/T)$，以 $1/T$ 为周期。

</li>

<li>

采样定理：$f_\mathrm A\ge2f_\mathrm g$；恢复：$s(t)=\sum s(nT)\operatorname{si}(\pi(t-nT)/T)$；否则产生混叠。

</li>

<li>

一个域中离散，意味着另一个域中周期。

</li>

<li>

离散卷积 $g(n)=\sum_ms(m)h(n-m)$；$h(n)=\operatorname{Tr}\{\delta(n)\}$；稳定：$\sum|h(n)|<\infty$。

</li>

<li>

递归系统 $g(n)=s(n)+bg(n-1)$：$h(n)=b^n\varepsilon(n)$，$H_\mathrm a=\frac{1}{1-b\mathrm{e}^{-\mathrm{j}2\pi f}}$。

</li>

<li>

$S_\mathrm a(f)=\sum s(n)\mathrm{e}^{-\mathrm{j}2\pi nf}$，周期为 1；$s(n)=\int_{-1/2}^{1/2}S_\mathrm a\mathrm{e}^{\mathrm{j}2\pi nf}\mathrm{d} f$。

</li>

<li>

DFT：$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\mathrm{e}^{-\mathrm{j}2\pi kn/M}$，$s_d=\frac1M\sum S_d\mathrm{e}^{\mathrm{j}2\pi kn/M}$；FFT $\approx M\,\mathrm{lb}\,M$；循环卷积 $\leftrightarrow S_dH_d$。

</li>

<li>

降采样使频带伸展（若 $cf_\mathrm g>\frac12$ 则产生混叠），升采样产生频谱镜像。

</li>

<li>

$S(z)=\sum s(n)z^{-n}$；$z^{-n_0}$ $=$ 延时；$H(z)=\frac{\sum a_qz^{-q}}{1-\sum b_pz^{-p}}$；因果且稳定：所有极点都在 $|z|<1$ 内。

</li>

</ul>
:::
