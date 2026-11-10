---
title: 第 3 阶段：卷积变成乘法
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 拉普拉斯变换
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: 第 2 章：拉普拉斯变换
order: 3220600
summary: 第 1 阶段说明系统对单个基本分量做了什么。第 2 阶段说明每个信号都由基本分量组成。两者结合，就得到拉普拉斯变换最重要的定理。
tags: 
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
第 [1](warum-gerade.html#stufe-1) 阶段说明系统对单个基本分量做了什么。第 [2](ein-signal-aus-lauter-bausteinen.html#stufe-2) 阶段说明每个信号都由基本分量组成。两者结合，就得到拉普拉斯变换最重要的定理。
:::

**思路。** LTI 系统是线性的：它分别处理输入的每个基本分量，再把结果相加。它把每个基本分量 $\mathrm{e}^{pt}$ 乘以 $H(p)$。因此输出由与输入*相同*的基本分量组成，只是每个权重都乘上了 $H(p)$。图 [4](#abb-4) 给出了得到输出的两条途径。

:::abbildung et3/k2wege 4
从输入到输出的两条途径。上：直接用卷积积分。下：把输入分解为基本分量，每个权重乘以 $H(p)$，再重新合成。下面这条途径之所以可行，是因为每个基本分量都是特征函数。
:::

:::satz 定理 3.1 (卷积定理)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$g(t)=s(t)*h(t)\quad\Longleftrightarrow\quad G(p)=S(p)\,H(p), \tag{3.1}$$

对同时位于 $S$ 和 $H$ 的收敛域内的所有 $p$ 成立。
:::

⁠**如何理解：**$S(p)$ 是基本分量 $\mathrm{e}^{pt}$ 在输入中的权重，$H(p)$ 是系统乘到该基本分量上的因子，$G(p)$ 是它在输出中的权重。对 $p$ 的条件之所以出现，是因为反演公式的直线必须穿过两个收敛域：输入必须能分解为基本分量，而系统必须能处理其中的每一个。

:::herleitung 由叠加与特征函数推出卷积定理
把输入写成叠加 [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1) 代入卷积，所取直线 $\operatorname{Re} p=\sigma$ 同时位于两个收敛域内：

$$g(t)=s(t)*h(t)=\left[\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p\right]*h(t).$$

线性：卷积可以移入积分号内，在那里分别作用于每个基本分量：

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\bigl[\mathrm{e}^{pt}*h(t)\bigr]\,\mathrm{d} p.$$

特征函数 [(1.1)](warum-gerade.html#gl-1-1)：$\mathrm{e}^{pt}*h(t)=H(p)\,\mathrm{e}^{pt}$。

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[S(p)H(p)\bigr]\,\mathrm{e}^{pt}\,\mathrm{d} p.$$

这就是 $g$ 的反演公式，权重为 $S(p)H(p)$。由于信号的权重是唯一的，所以 $G(p)=S(p)H(p)$。
:::

⁠**简而言之：**卷积变成乘法，是因为系统只是把每个基本分量 $\mathrm{e}^{pt}$ 乘以数 $H(p)$。

:::analogie
图示均衡器把音乐分成若干频段，把每个频段乘以其推子的设定值，再把各频段重新合在一起。LTI 系统对基本分量 $\mathrm{e}^{pt}$ 做的是同样的事，推子设定值就是 $H(p)$。这个类比在两处不成立：均衡器的频段数有限，推子设定值是实数。而这里的基本分量连续分布，还可以增长或衰减，并且每个“推子”都是一个复数，还会额外移动相位。
:::

**同一机制也解释了求导、积分和微分方程。**

<ul>

<li>

⁠**求导。**$\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$。微分器是一个 LTI 系统，每个基本分量都是它的特征函数，特征值为 $p$。因此每个权重都乘以 $p$：$\mathcal{L}\{\dot s\}=p\,S(p)$。

</li>

<li>

⁠**积分。**$\int_{-\infty}^{t}\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$，但仅当 $\operatorname{Re} p>0$ 时成立；否则积分在 $-\infty$ 处发散。因此 $\mathcal{L}\{\int_{-\infty}^t s\,\mathrm{d}\tau\}=S(p)/p$，附加条件为 $\operatorname{Re} p>0$。

</li>

<li>

⁠**级联。**两个串联的系统先乘以 $H_1(p)$，再乘以 $H_2(p)$，合起来乘以 $H_1H_2$。顺序无关紧要，因为数的乘法满足交换律。

</li>

<li>

⁠**微分方程。**每次求导都变成一个因子 $p$。常系数线性微分方程

$$\sum_{r=0}^{R}\alpha_r\frac{\mathrm{d}^r g}{\mathrm{d} t^r}=\sum_{q=0}^{Q}\beta_q\frac{\mathrm{d}^q s}{\mathrm{d} t^q} \quad\text{变为}\quad \Bigl(\sum_{r}\alpha_rp^r\Bigr)G(p)=\Bigl(\sum_q\beta_qp^q\Bigr)S(p),$$

即一个代数方程，而 $H(p)=G/S$ 是多项式之比。

</li>

</ul>

**例：RC 低通滤波器的阶跃响应。** 输入 $\varepsilon(t)$，$S(p)=1/p$（$\operatorname{Re} p>0$）；系统 $H(p)=1/(p+1)$（$\operatorname{Re} p>-1$）。公共区域为 $\operatorname{Re} p>0$：

$$G(p)=\frac{1}{p}\cdot\frac{1}{p+1}=\frac1p-\frac{1}{p+1}\quad\Longrightarrow\quad g(t)=\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

两项的反变换由 [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) 取 $p_0=0$ 和 $p_0=-1$ 得到。直接验算：$t>0$ 时 $g(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$。在直线 $\sigma=0.5/\mathrm s$ 上对反演公式 [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1) 作数值计算，同样得到 $g(0.5\,\mathrm{s})=0.3935$、$g(1\,\mathrm{s})=0.6321$、$g(3\,\mathrm{s})=0.9502$ 和 $g(-1\,\mathrm{s})=0$，与 $\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)$ 完全一致。

:::ltspice 直接输入传递函数
⁠**绘制：**RC 电路（`1Meg`，`1u`），从 `in` 接到 `rc`。旁边放一个压控电压源 `e`：控制输入接 `in` 和地，输出接节点 `lap`，值为 `Laplace=1/(1+s)`。这个源是一个仅由 $H$ 给定的 LTI 系统：LTspice 由它算出冲激响应，并把输入与冲激响应做卷积。LTspice 用 $s$ 代替 $p$。

⁠**信号源与指令：**`PULSE(0 1 0 1u 1u 100)`，`.tran 0 5 0 1m`。

⁠**你会看到：**`V(rc)` 和 `V(lap)` 重合在一起（差值小于 0.001），在 0.5 s 时达到 0.3935，1 s 时达到 0.6321，3 s 时达到 0.9502。若信号源的值取 `AC 1` 并使用 `.ac dec 100 0.01 100`，LTspice 显示 $s=\mathrm{j}2\pi f$ 时的 $H(s)$，即只显示虚轴上的值：在 0.159 Hz 处为 $-3.0$ dB 和 $-45^\circ$。

⁠**对于练习 [6](#aufg-6)：**信号源取 `PWL(0 0 10 10)`，即到 10 s 为止的斜坡 $t\,\varepsilon(t)$，以及 `.tran 0 10 0 1m`。把 `V(rc)` 与你在练习 [6](#aufg-6)(b) 中的结果比较。
:::

:::aufgabe 练习 5 ★★ 用基本分量理解级联与求导
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

用基本分量的图景（不用卷积积分）解释：为什么两个级联的 LTI 系统的传递函数为 $H_1(p)H_2(p)$？为什么由此可推出卷积满足交换律？

</li>

<li>

将反演公式对 $t$ 求导，由此推导 $\mathcal{L}\{\dot s(t)\}=p\,S(p)$。

</li>

</ol>

:::loesung
(a) 输入由权重为 $S(p)$ 的基本分量 $\mathrm{e}^{pt}$ 组成。第一个系统把每个基本分量乘以 $H_1(p)$，于是权重变为 $H_1S$。第二个系统再乘以 $H_2(p)$：$G=H_2H_1S$。所以级联系统的 $H=H_1H_2$。由于 $H_1H_2=H_2H_1$，结果与顺序无关；又因为 $h_1*h_2$ 是级联系统的冲激响应，所以 $h_1*h_2=h_2*h_1$。

(b) 在积分号下求导只作用于 $\mathrm{e}^{pt}$：

$$\dot s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}\,\mathrm{d} p=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[p\,S(p)\bigr]\mathrm{e}^{pt}\,\mathrm{d} p.$$

这就是权重为 $pS(p)$ 的反演公式，所以 $\mathcal{L}\{\dot s\}=pS(p)$。
:::
:::

:::aufgabe 练习 6 ★★ RC 低通滤波器的斜坡响应
<span class="anker" id="aufg-6"></span>

输入 $s(t)=t\,\varepsilon(t)$，$S(p)=1/p^2$，$\operatorname{Re} p>0$，即基本变换对 [(2.5)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-5)。

<ol class="al">

<li>

求 $G(p)$ 及其收敛域。

</li>

<li>

验证分解式 $G(p)=\frac{1}{p^2}-\frac1p+\frac{1}{p+1}$，并求 $g(t)$。

</li>

<li>

检验：$g(0)$ 等于多少？为什么必须如此？$\dot g(t)$ 是什么？

</li>

<li>

$t\gg1$ s 时 $g(t)$ 的行为如何？与练习 [1](warum-gerade.html#aufg-1)c 比较。

</li>

</ol>

:::loesung
(a) $G(p)=\dfrac{1}{p^2}\cdot\dfrac{1}{p+1}=\dfrac{1}{p^2(p+1)}$，$\operatorname{Re} p>0$（$\operatorname{Re} p>0$ 与 $\operatorname{Re} p>-1$ 的交集）。

(b) 通分：$\frac{1}{p^2}-\frac1p+\frac{1}{p+1}=\frac{(p+1)-p(p+1)+p^2}{p^2(p+1)}=\frac{1}{p^2(p+1)}$。用 [(2.5)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-5) 和 [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) 作反变换：

$$g(t)=\bigl(t-1+\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

(c) $g(0)=0-1+1=0$：电容电压不能跳变，而输入从零开始。$\dot g(t)=(1-\mathrm{e}^{-t})\varepsilon(t)$，恰好就是阶跃响应。这是吻合的：斜坡是阶跃的积分，所以斜坡响应是阶跃响应的积分。

(d) 当 $t\gg1$ s 时，$\mathrm{e}^{-t}\approx0$，$g(t)\approx t-1$：输出以 $RC=1$ s 的延迟跟随斜坡，与练习 [1](warum-gerade.html#aufg-1)c 中的双边斜坡完全一样。区别在于基本分量 $\mathrm{e}^{-t}$（系统的极点 $-1$）：这是暂态过程，它的出现是因为这里的斜坡从 $t=0$ 才开始。
:::
:::
