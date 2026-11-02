---
title: 收敛域：哪些衰减率可行
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 拉普拉斯变换
order: 3220500
summary: 每个信号都是 $\ee^{pt}$ 的叠加， 以及为什么 LTI 系统的作用因此变成乘法
tags: 
lang: zh
---

<span class="anker" id="stufe-2-3"></span>

**思路。** 因子 $\mathrm{e}^{-\sigma t}$ 作用于时间轴的两侧，但作用相反。对 $t\to+\infty$，$\sigma$ 越大，衰减越强。对 $t\to-\infty$，$\mathrm{e}^{-\sigma t}=\mathrm{e}^{\sigma|t|}$，因此在这一侧大的 $\sigma$ 起放大作用。由此得到收敛域的三种形状：

<ul>

<li>

⁠**右边信号**，$t<0$ 时 $s(t)=0$，至多按 $\mathrm{e}^{\alpha t}$ 增长：每个 $\sigma>\alpha$ 都可行。收敛域：某条边界*右侧*的半平面。

</li>

<li>

⁠**左边信号**：只有 $t\to-\infty$ 这一侧起作用，小的 $\sigma$ 有利。收敛域：某条边界*左侧*的半平面。

</li>

<li>

⁠**双边信号**：两个条件必须同时满足。收敛域：一个*带状区域*，也可能为空。

</li>

</ul>

为什么边界总是竖直的？因为 $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$。$\int|s(t)\mathrm{e}^{-pt}|\mathrm{d} t$ 是否有限只取决于 $\sigma$，与 $f$ 无关。

⁠**简而言之：**收敛域是使 $s(t)\,\mathrm{e}^{-\sigma t}$ 绝对可积的所有衰减率 $\sigma$ 的集合。

:::merke 基本变换对（全册通用）
对任意复数 $p_0$：

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
<span class="anker" id="gl-2-4"></span>
<span class="anker" id="gl-2-5"></span>
$$\begin{aligned} \mathrm{e}^{p_0t}\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p>\operatorname{Re} p_0,\\ -\mathrm{e}^{p_0t}\,\varepsilon(-t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p<\operatorname{Re} p_0,\\ \delta(t)\quad&\longleftrightarrow\quad1,&&\text{所有 $p$},\\ t\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p^2},&&\operatorname{Re} p>0. \end{aligned} \tag{2.2|2.3|2.4|2.5}$$

取 $p_0=0$，由式 [(2.2)](#gl-2-2) 得到阶跃：$\varepsilon(t)\leftrightarrow1/p$，$\operatorname{Re} p>0$。前两行的表达式*相同*，收敛域却不同：只有表达式和收敛域一起才能确定信号。
:::

:::herleitung 基本变换对
[(2.2)](#gl-2-2)：$\int_0^\infty\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_0^\infty=\frac{1}{p-p_0}$。上限处的值当且仅当 $\operatorname{Re}(p-p_0)>0$ 时为零。

[(2.3)](#gl-2-3)：$-\int_{-\infty}^0\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=-\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_{-\infty}^0=\frac{1}{p-p_0}$。$t\to-\infty$ 时的值当且仅当 $\operatorname{Re}(p-p_0)<0$ 时为零。

[(2.4)](#gl-2-4)：筛选性质，$\int\delta(t)\mathrm{e}^{-pt}\mathrm{d} t=\mathrm{e}^{0}=1$。

[(2.5)](#gl-2-5)：分部积分，$\int_0^\infty t\,\mathrm{e}^{-pt}\mathrm{d} t=\Bigl[\frac{-t\,\mathrm{e}^{-pt}}{p}\Bigr]_0^\infty+\frac1p\int_0^\infty\mathrm{e}^{-pt}\mathrm{d} t=0+\frac{1}{p^2}$，$\operatorname{Re} p>0$。
:::

:::frage 计算 $\int_0^\infty\mathrm{e}^{-bt}\mathrm{e}^{-pt}\mathrm{d} t$ 时，为什么指数项消失了？为什么结果是 $\frac{1}{b+p}$ 而不是 $\frac{1}{-(b+p)}$？
两者都源于代入积分限。$\mathrm{e}^{-(b+p)t}$ 的原函数是 $-\frac{\mathrm{e}^{-(b+p)t}}{b+p}$，带负号是因为求导会产生因子 $-(b+p)$。然后计算“上限值减下限值”：

$$\int_0^\infty\mathrm{e}^{-(b+p)t}\mathrm{d} t=\underbrace{\lim_{t\to\infty}\Bigl(-\frac{\mathrm{e}^{-(b+p)t}}{b+p}\Bigr)}_{=\,0}-\Bigl(-\frac{\mathrm{e}^{0}}{b+p}\Bigr)=\frac{1}{b+p}.$$

<ul>

<li>

⁠**上限：**$|\mathrm{e}^{-(b+p)t}|=\mathrm{e}^{-(\operatorname{Re} b+\sigma)t}$ 当且仅当 $\operatorname{Re} p>-\operatorname{Re} b$ 时趋于零。这个条件*就是*收敛域。在收敛域之外，指数项会保留下来并无界增长。

</li>

<li>

⁠**下限：**$\mathrm{e}^0=1$，因此那里不留下指数项。

</li>

<li>

⁠**符号：**原函数的负号与减去下限值时的负号相遇。负负得正。

</li>

</ul>

对于左边脉冲 $\mathrm{e}^{-bt}\varepsilon(-t)$，情况正好相反。积分从 $-\infty$ 到 $0$，所以现在 $t=0$ 是*上*限。它的贡献 $-\frac{1}{b+p}$ 不被减去，因此负号保留。下限 $t\to-\infty$ 处的项仅当 $\operatorname{Re}(b+p)<0$ 时才为零，所以这个收敛域位于左侧。令 $p_0=-b$，这两者就是基本变换对 [(2.2)](#gl-2-2) 和 [(2.3)](#gl-2-3)。
:::

:::frage 我们看 $b$ 和 $p$ 的实部，是因为被积函数的衰减决定了可积性吗？对某些 $b$，信号衰减；对另一些 $b$，信号增长、不会降到零，积分就不收敛，因为总有东西不断加进来。
是的，正是如此。被积函数的模为

$$\bigl|\mathrm{e}^{-(b+p)t}\bigr|=\mathrm{e}^{-\operatorname{Re}(b+p)\,t}\cdot\underbrace{\bigl|\mathrm{e}^{-\mathrm{j}\operatorname{Im}(b+p)\,t}\bigr|}_{=\,1}.$$

虚部只让被积函数在复平面上旋转，并不改变其模。增长还是衰减仅由实部决定。三点细化：

<ul>

<li>

起决定作用的是*和* $\operatorname{Re} b+\sigma$。只要衰减 $\sigma$ 更强，信号本身可以增长（$\operatorname{Re} b<0$）。这就是第 2.2 节中的“衰减”技巧。

</li>

<li>

仅仅“趋于零”是不够的。$1/t$ 也趋于零，但 $\int_1^\infty\frac{\mathrm{d} t}{t}=\infty$，因为各部分贡献减小得太慢。指数衰减足够快：$\int_0^\infty\mathrm{e}^{-\operatorname{Re}(b+p)t}\mathrm{d} t=\frac{1}{\operatorname{Re}(b+p)}$ 是有限的。

</li>

<li>

在边界 $\operatorname{Re}(b+p)=0$ 上，被积函数的模恒为 1，只是在旋转。此时积分来回摆动而不趋于某个值；恰好在极点处，它甚至线性增长（练习 [3a](#aufg-3a)）。这就是边界线不属于收敛域的原因。

</li>

</ul>
:::

:::frage 那么这对任意函数都成立吗？
不，只对收敛域非空的函数成立。三个反例：

<ul>

<li>

$\mathrm{e}^{t^2}\varepsilon(t)$ 比任何指数函数增长得都快。对每个 $\sigma$ 都有 $\mathrm{e}^{t^2-\sigma t}\to\infty$，因此任何衰减都不够。

</li>

<li>

$\mathrm{e}^{|t|}$：右半部分要求 $\sigma>1$，左半部分要求 $\sigma<-1$。两者不可能同时满足。

</li>

<li>

甚至常数 $s(t)=1$（对所有 $t$）也不行：右侧要求 $\sigma>0$，左侧要求 $\sigma<0$。傅里叶变换仍能处理这类信号，其频谱中含有狄拉克冲激。

</li>

</ul>

对于至多按指数增长的右边信号，这总是可行的。在电路中于 $t=0$ 时刻接入的每个信号都属于此类。
:::

:::frage $p$ 平面是二维的，为什么一条直线就够了？
收敛域中的每条直线都给出同一个 $s(t)$：$\sigma$ 越大，第 1 步中衰减得越强，第 3 步中乘回的也越多，两者相互抵消。数值验证：取 $\sigma=0.2$ 和 $\sigma=1/\mathrm s$，阶跃两次都给出 $s(1\,\mathrm{s})\approx1.00$ 和 $s(-1\,\mathrm{s})\approx0.00$。因此，这个平面包含的东西多于叠加所需。它的用处在别处：在平面上，$S(p)$ 可以用少数几个数来描述，即极点和零点。（附注：$S(p)$ 在收敛域内复可微，因此它在一条直线上的值决定了它在整个区域内的取值。）
:::

:::aufgabe 练习 2 ★ 拉普拉斯变换即衰减信号的傅里叶变换
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

把 $\mathrm{e}^{-pt}$ 拆成两个因子，证明 $S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\,\mathrm{e}^{-\sigma t}\}(f)$。

</li>

<li>

以阶跃为例验证：对 $\sigma>0$ 直接计算 $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}$，并与 $S(p)=1/p$ 比较。

</li>

</ol>

:::loesung
(a) $S(\sigma+\mathrm{j}2\pi f)=\int s(t)\,\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\int\bigl[s(t)\mathrm{e}^{-\sigma t}\bigr]\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}(f)$。

(b) $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}=\int_0^\infty\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\dfrac{1}{\sigma+\mathrm{j}2\pi f}$，$\sigma>0$。这正是 $1/p$ 在 $p=\sigma+\mathrm{j}2\pi f$ 处的值。
:::
:::

:::aufgabe 练习 3 ★★ 一个增长的信号
<span class="anker" id="aufg-3"></span>

$s(t)=\mathrm{e}^{2t}\varepsilon(t)$，例如一个不稳定系统的冲激响应（$t$ 的单位为 s）。

<ol class="al">

<li>

为什么不存在经典意义下的傅里叶变换？

</li>

<li>

对哪些 $\sigma$，$s(t)\,\mathrm{e}^{-\sigma t}$ 绝对可积？

</li>

<li>

直接由积分计算 $S(p)$。在 $p$ 平面中画出极点和收敛域。

</li>

<li>

在反演公式中可以使用哪些 $\sigma$？表达式 $S(\mathrm{j}2\pi f)$ 是有限的。为什么仍然不能选 $\sigma=0$？选 $\sigma=0$ 会得到哪个信号？（提示：[(2.3)](#gl-2-3)。）

</li>

</ol>

:::loesung
(a) $\int_0^\infty\mathrm{e}^{2t}\mathrm{d} t=\infty$：该信号不是绝对可积的。直观地说：由恒定幅度的振荡无法构成任何增长的东西。

(b) $t>0$ 时 $|s(t)\mathrm{e}^{-\sigma t}|=\mathrm{e}^{(2-\sigma)t}$，当且仅当 $\sigma>2/\mathrm s$ 时可积。

(c) $S(p)=\int_0^\infty\mathrm{e}^{-(p-2)t}\mathrm{d} t=\dfrac{1}{p-2}$，$\operatorname{Re} p>2$。极点在 $p=2$，收敛域在其右侧，所有右边信号都是如此。数值检验：$S(3)=1$，$S(2.5+\mathrm{j})=0.4-0.8\mathrm{j}$。

(d) 任何 $\sigma>2/\mathrm s$ 均可，例如 $\sigma=3/\mathrm s$。$\sigma=0$ 位于极点左侧，因此在收敛域之外。表达式 $1/(\mathrm{j}2\pi f-2)$ 虽然有限，但它属于一个*不同的*信号：由 [(2.3)](#gl-2-3)，$-\mathrm{e}^{2t}\varepsilon(-t)$ 的变换同样是 $1/(p-2)$，收敛域为 $\operatorname{Re} p<2$。若取 $\sigma=0$，得到的就是这个左边的、衰减的信号。它的傅里叶变换才真正是 $1/(\mathrm{j}2\pi f-2)$。
:::
:::

:::aufgabe 练习 3a ★★ 边界上会发生什么
<span class="anker" id="aufg-3a"></span>

$s(t)=\mathrm{e}^{(1+3\mathrm{j})t}\varepsilon(t)$，即 $b=-1-3\mathrm{j}$（$t$ 的单位为 s）。

<ol class="al">

<li>

对哪些 $\sigma$，$\int_0^\infty s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ 收敛？其中的 3 起什么作用？

</li>

<li>

令 $p=1+\mathrm{j}\omega$，即恰好位于边界上，计算 $\int_0^T s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$。$T\to\infty$ 时会怎样？分 $\omega\neq3$ 和 $\omega=3$ 两种情况讨论。极点在哪里？

</li>

</ol>

:::loesung
(a) 令 $p=\sigma+\mathrm{j}\omega$，则 $b+p=(\sigma-1)+\mathrm{j}(\omega-3)$。被积函数的模为 $\mathrm{e}^{-(\sigma-1)t}$，因此积分当且仅当 $\sigma>1$ 时收敛。3（信号的角频率）不出现在模中。它只决定极点位于边界线上的什么位置：$S(p)=\frac{1}{p-(1+3\mathrm{j})}$，极点在 $p=1+3\mathrm{j}$。

(b) 取 $p=1+\mathrm{j}\omega$，则 $b+p=\mathrm{j}(\omega-3)$。

<ul>

<li>

$\omega\neq3$：$\displaystyle\int_0^T\mathrm{e}^{-\mathrm{j}(\omega-3)t}\mathrm{d} t=\frac{1-\mathrm{e}^{-\mathrm{j}(\omega-3)T}}{\mathrm{j}(\omega-3)}$。随着 $T$ 增大，分子在以 1 为圆心的圆上转动，不趋于任何值。积分保持有界，但没有极限。

</li>

<li>

$\omega=3$，即恰好位于极点 $p=1+3\mathrm{j}$：被积函数恒为 1，积分等于 $T$，无界增长。

</li>

</ul>

因此，积分在边界线上处处不收敛。收敛域是开半平面 $\operatorname{Re} p>1$。
:::
:::

:::aufgabe 练习 4 ★ 判断对错并说明理由
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

每个函数都有拉普拉斯变换。

</li>

<li>

$p$ 是否位于收敛域内只取决于 $\operatorname{Re} p$。

</li>

<li>

若虚轴位于收敛域内，则 $S(\mathrm{j}2\pi f)$ 是 $s(t)$ 的傅里叶变换。

</li>

<li>

在反演公式中，若 $\sigma=1/\mathrm s$ 和 $\sigma=2/\mathrm s$ 都位于收敛域内，则二者给出不同的信号。

</li>

<li>

$\cos(2\pi f_0t)$ 是每个 LTI 系统的特征函数。

</li>

</ol>

:::loesung
(a) 错。反例：$\mathrm{e}^{t^2}\varepsilon(t)$、$\mathrm{e}^{|t|}$、双边常数。

(b) 对。$|s(t)\mathrm{e}^{-pt}|=|s(t)|\mathrm{e}^{-\sigma t}$；频率 $f$ 不出现在模中。这就是收敛域由完整的竖直线构成的原因。

(c) 对。取 $\sigma=0$，$S(\mathrm{j}2\pi f)=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s\}(f)$。

(d) 错。收敛域中的每条直线都给出同一个信号，因为用 $\mathrm{e}^{-\sigma t}$ 的衰减与用 $\mathrm{e}^{\sigma t}$ 的再乘回相互抵消。

(e) 错。输出为 $|H|\cos(2\pi f_0t+\varphi)$，其中 $H=H(\mathrm{j}2\pi f_0)$。只有当 $\varphi=0$ 或 $\varphi=180^\circ$，即 $H(\mathrm{j}2\pi f_0)$ 为实数时，它才是 $\cos(2\pi f_0t)$ 的倍数。对于 RC 低通滤波器，在任何频率 $f_0>0$ 下都不是这种情况。
:::
:::
