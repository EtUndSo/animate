---
title: 拉普拉斯变换
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 拉普拉斯变换
order: 3220100
summary: 每个信号都是 $\ee^{pt}$ 的叠加， 以及为什么 LTI 系统的作用因此变成乘法
tags: 增长率, 频率, 绝对可积, 密度, 部分分式展开, 稳定性, 自然响应
lang: zh
---

## 本文内容

:::frage 从代入特征函数的卷积积分得到 $H(p)$ 的这段计算，我已经理解了。但我觉得拉普拉斯变换背后远不止这条计算规则：任意函数都可以写成复指数函数之和。
这个猜想抓住了问题的核心。没有它，特征函数的那段计算只不过是个奇特的结论，因为它本身只对 $\mathrm{e}^{pt}$ 这一个信号成立。正是因为（几乎）每个信号都能由这样的基本分量（构件）组合而成，它才能对*每个*输入信号给出结论。以下三点细化使这个猜想变得精确：

<ol>

<li>

一般来说，它不是求和，而是*积分*：无穷多个基本分量 $\mathrm{e}^{pt}$，每个都带有无穷小的权重。这些基本分量位于 $p$ 平面中的一条竖直线 $\operatorname{Re} p=\sigma$ 上（第 [2](#stufe-2) 阶段）。

</li>

<li>

并非任意函数都可以，而是存在收敛域的函数：它在时间轴每一侧至多按指数增长，并且必须有同一个衰减因子能同时抑制两侧（第 [2.3](#stufe-2-3) 节）。

</li>

<li>

若 $S(p)$ 是多项式之比，积分确实会变成*有限和* $\sum_r A_r\,\mathrm{e}^{p_r t}$。指数 $p_r$ 就是 $S(p)$ 的极点（第 [4](#stufe-4) 阶段）。

</li>

</ol>
:::

:::merke 三句话的答案（读完本文后应觉得理所当然）
<ol>

<li>

LTI 系统对基本分量 $\mathrm{e}^{pt}$ 只能乘以一个数 $H(p)$，因为对 $\mathrm{e}^{pt}$ 而言，平移就等同于相乘。

</li>

<li>

每个存在收敛域的信号都是这类基本分量的叠加。$S(p)$ 给出基本分量 $\mathrm{e}^{pt}$ 以多大的权重包含在信号中。

</li>

<li>

正因如此，卷积变成了乘法：$G(p)=H(p)\,S(p)$。若 $S(p)$ 是有理函数，信号就是以极点为指数的有限和 $\sum_r A_r\mathrm{e}^{p_r t}$。

</li>

</ol>
:::

**所有结果背后的同一个原理。** 关于拉普拉斯变换的几乎每一个结果都由这三句话推出。下表给出每个结果的来源，各阶段对其加以解释。

| 结果 | 来源 |
|---|---|
| 特征函数 $\mathrm{e}^{pt}$，传递函数 $H(p)$ | 平移 $\mathrm{e}^{pt}$ 就是乘以 $\mathrm{e}^{-p\tau}$（第 [1](#stufe-1) 阶段） |
| 拉普拉斯变换 $S(p)$ | 基本分量 $\mathrm{e}^{pt}$ 在信号中的权重（第 [2](#stufe-2) 阶段） |
| 收敛域 | 使 $s(t)\mathrm{e}^{-\sigma t}$ 绝对可积的所有衰减率 $\sigma$（第 [2.3](#stufe-2-3) 节） |
| 卷积 $\to$ 乘积，级联 | 每个基本分量都乘以 $H(p)$（第 [3](#stufe-3) 阶段） |
| 求导 $\to p$，积分 $\to 1/p$ | $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$ 和 $\int_{-\infty}^t\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$（第 [3](#stufe-3) 阶段） |
| 微分方程 $\to$ 多项式之比 | 每次求导变成一个因子 $p$（第 [3](#stufe-3) 阶段） |
| 极点，部分分式 | 有限个基本分量的指数和权重（第 [4](#stufe-4) 阶段） |
| 稳定性 | 因果基本分量 $\mathrm{e}^{p_r t}$ 仅当 $\operatorname{Re} p_r<0$ 时才衰减（第 [4](#stufe-4) 阶段） |
| 傅里叶变换 | 直线 $\sigma=0$ 上的同一种叠加（第 [2](#stufe-2) 阶段） |

**如何使用本文。**每个阶段包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。

:::merke 本文的参考模型
所有例子都使用同样的两个要素：

<ul>

<li>

一个 $RC=1$ s 的 **RC 低通滤波器**（例如 $R=1\,\mathrm{M\Omega}$，$C=1\,\mu\text{F}$）。它的冲激响应和传递函数为

$$h(t)=\frac{1}{RC}\,\mathrm{e}^{-t/RC}\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t),\qquad H(p)=\frac{1}{1+pRC}=\frac{1}{p+1},\quad \operatorname{Re} p>-1,$$

其中 $t$ 的单位为 s，$p$ 的单位为 $1/\mathrm{s}$；

</li>

<li>

⁠**单位阶跃** $s(t)=\varepsilon(t)$，其 $S(p)=1/p$，$\operatorname{Re} p>0$。

</li>

</ul>

脚本 `rechnung_kap2.py` 可重新计算文中的数值和曲线。
:::

## 第 1 阶段：为什么偏偏是 $\mathrm{e}^{pt}$

<span class="anker" id="stufe-1"></span>

:::zweck
把 $\mathrm{e}^{pt}$ 代入卷积积分，结果是 $H(p)\,\mathrm{e}^{pt}$：$\mathrm{e}^{pt}$ 是一个特征函数。本阶段探讨 $\mathrm{e}^{pt}$ 的哪种性质导致了这一点，以及为什么基本分量必须取复数形式。
:::

**思路。** 卷积积分

$$g(t)=\int_{-\infty}^{\infty}h(\tau)\,s(t-\tau)\,\mathrm{d}\tau$$

可以这样理解：输出是输入的*延迟副本*之和。延迟为 $\tau$ 的副本以权重 $h(\tau)\,\mathrm{d}\tau$ 计入。对于任意形状的信号，每个延迟副本看起来都与原信号不同，求和后得到新的形状。$\mathrm{e}^{pt}$ 则不然：

$$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\cdot\mathrm{e}^{pt}.$$

延迟 $\tau$ 的作用相当于乘以*常数* $\mathrm{e}^{-p\tau}$。所有副本都是同一个函数 $\mathrm{e}^{pt}$ 的倍数，它们的和也是如此：

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{pt}*h(t)=\mathrm{e}^{pt}\underbrace{\int_{-\infty}^{\infty}h(\tau)\,\mathrm{e}^{-p\tau}\,\mathrm{d}\tau}_{H(p)}=H(p)\,\mathrm{e}^{pt}. \tag{1.1}$$

⁠**简而言之：**$\mathrm{e}^{pt}$ 之所以是特征函数，是因为对 $\mathrm{e}^{pt}$ 而言，平移就等同于相乘。

**$p$ 的含义。** 令 $p=\sigma+\mathrm{j}2\pi f$，基本分量分解为两个因子：

$$\mathrm{e}^{pt}=\mathrm{e}^{\sigma t}\cdot\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{e}^{\sigma t}\bigl[\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft)\bigr].$$

实部 $\sigma$（单位 $1/\mathrm s$）是__增长率__：$\sigma<0$ 时基本分量衰减，$\sigma=0$ 时以恒定幅度振荡，$\sigma>0$ 时增长。虚部 $2\pi f$ 决定振荡的__频率__。因此 $p$ 平面上的每一点都是一个基本分量，点的位置告诉你它是什么样子（图 [1](#abb-1)）。

:::abbildung et3/k2bausteine
$p$ 平面：基本分量的地图。左：四个点 $p$。右：每个点对应的实部 $\operatorname{Re}\{\mathrm{e}^{pt}\}=\mathrm{e}^{\sigma t}\cos(2\pi ft)$ 及包络 $\pm\mathrm{e}^{\sigma t}$（虚线）。点 b、c、d 的 $2\pi f=\pi/\mathrm s$，即 $f=0.5$ Hz。到虚轴的距离决定衰减还是增长，高度决定频率。
:::

:::frage 为什么要用复数？正弦也是一种简单的信号啊。
正弦平移后不只是被缩放。令 $\omega_0=2\pi f_0$，有

$$\sin\bigl(\omega_0(t-\tau)\bigr)=\cos(\omega_0\tau)\,\sin(\omega_0t)-\sin(\omega_0\tau)\,\cos(\omega_0t).$$

这里出现了余弦分量，因此延迟副本的形状不同。这就是为什么系统对 $\sin(\omega_0t)$ 的响应是 $|H|\sin(\omega_0t+\varphi)$：幅度*和相位*都发生变化。相移无法写成乘以一个实数，但可以写成乘以复数 $\mathrm{e}^{\mathrm{j}\varphi}$。这就是基本分量取复数形式的原因：单个数 $H(p)$ 同时携带幅度和相位。一个实正弦由两个基本分量组成，$\sin(\omega_0t)=\bigl(\mathrm{e}^{\mathrm{j}\omega_0t}-\mathrm{e}^{-\mathrm{j}\omega_0t}\bigr)/(2\mathrm{j})$，二者各自乘以自己的那个数（练习 [1](#aufg-1)d）。
:::

:::frage 为什么 $\mathrm{e}^{pt}$ 是*每个* LTI 系统的特征函数，尽管这些系统千差万别？
特征函数的形式仅由时不变性（平移 = 相乘）决定，而所有 LTI 系统都具有这一性质。只有因子 $H(p)$ 与系统有关，因为它包含了权重 $h(\tau)$。因此，*同一组*基本分量同时适用于所有 LTI 系统。正是这一点使拉普拉斯变换具有普适性。
:::

:::zusatz 只有指数函数具有这一性质
寻找一个满足 $x(0)=1$ 的可微函数 $x(t)$，使它的平移副本都是它自身的倍数：对所有 $t,u$ 有 $x(t+u)=c(u)\,x(t)$。令 $t=0$ 得 $c(u)=x(u)$，于是 $x(t+u)=x(t)\,x(u)$。在 $u=0$ 处对 $u$ 求导，得 $x'(t)=x'(0)\,x(t)$。这是微分方程 $x'=p\,x$，其中 $p=x'(0)$，它满足 $x(0)=1$ 的解为 $x(t)=\mathrm{e}^{pt}$。因此，不存在其他具有这一性质的基本分量。
:::

:::frage 指数函数是 LTI 系统唯一可能的特征函数吗？
这里必须区分两个问题。

⁠**同时作为*所有* LTI 系统的特征函数：是的，只有 $c\,\mathrm{e}^{pt}$。**理想延时单元 $g(t)=s(t-u)$ 本身就是一个 LTI 系统，而且对任意延时 $u$ 都是。因此，一个对每个 LTI 系统都是特征函数的函数，在任意平移下都必须变成它自身的倍数。根据上面的方框，只有 $\mathrm{e}^{pt}$ 满足这一点。

⁠**作为某个*特定*系统的特征函数：不止这些。**系统把每个基本分量 $\mathrm{e}^{p_kt}$ 乘以它自己的数 $H(p_k)$。和式 $\sum_kc_k\mathrm{e}^{p_kt}$ 仍是它自身的倍数，当且仅当所有这些因子都相等，即 $H(p_k)=\lambda$。这个公共因子 $\lambda$ 就是特征值。两个例子：

<ul>

<li>

延时 $T$ 的理想延时单元：$H(p)=\mathrm{e}^{-pT}$ 在所有点 $p_k=\mathrm{j}2\pi k/T$ 处取相同的值 1。每个周期为 $T$ 的信号都是特征值为 1 的特征函数，因为 $s(t-T)=s(t)$。

</li>

<li>

无时延的理想低通，在整个通带内 $H(f)=1$：频谱完全位于通带内的每个信号都原样输出，是特征值为 1 的特征函数。

</li>

</ul>

而对 RC 电路，$H(p)=1/(1+pRC)$ 的每个值只取一次。在那里，单个的 $c\,\mathrm{e}^{pt}$（$p$ 在收敛域内）是能由基本分量组成的唯一特征函数。

⁠**简而言之：**$\mathrm{e}^{pt}$ 是*每个* LTI 系统都具有的唯一特征函数。单个系统如果把若干基本分量都乘以同一个数，那么这些基本分量的混合也是它的特征函数。
:::

:::ltspice 实验中的特征函数
⁠**绘制：**RC 电路（`res` 取 `1Meg`，从 `in` 接到 `out`；`cap` 取 `1u`，接地）。信号源用行为源 `bv`，取 `V=exp(-time/2)`，即 $p=-0.5/\mathrm s$ 的基本分量。

⁠**指令：**`.tran 0 10 0 1m` 和 `.ic V(out)=X`，其中 $X$ 取一个数：电容从 $X$ 伏开始。用“Add Traces”画出表达式 `V(out)/V(in)`。

⁠**你会看到：**如果把 $X$ 设为你在练习 [1](#aufg-1)(b) 中所得结果在 $t=0$ 时的值，这个比值从一开始就是常数：输出等于一个数乘以输入。若 $X=0$，它要经过几秒钟才趋于同一个数。原因在于：一个一直存在的输入，会在 $t=0$ 时恰好把电容充电到这个值。RC 电路以 $\mathrm{e}^{-t}$ 消除任何其他的初始电压，这比输入按 $\mathrm{e}^{-t/2}$ 衰减更快。

⁠**对于 (d)：**电压源 `voltage` 取 `SINE(0 1 {1/(2*pi)} 0 0 90)`，即 $\cos t$。把暂态过程结束后 `V(out)` 的幅度和滞后与你在练习 [1](#aufg-1)(d) 中的结果比较。
:::

:::aufgabe 练习 1 ★ 是不是特征函数？
<span class="anker" id="aufg-1"></span>

使用参考模型中的 RC 低通滤波器，$h(t)=\mathrm{e}^{-t}\varepsilon(t)$。

<ol class="al">

<li>

计算 $H(p)=\int h(t)\,\mathrm{e}^{-pt}\mathrm{d} t$。积分对哪些 $p$ 收敛？为什么这只取决于 $\operatorname{Re} p$？

</li>

<li>

输入 $s(t)=\mathrm{e}^{-t/2}$（对所有 $t$）。分别直接用卷积积分和用 $H(p)$ 计算输出。这个基本分量的 $p$ 是多少？

</li>

<li>

输入 $s(t)=t$（对所有 $t$）。用卷积积分证明输出为 $g(t)=t-1$。尽管输出看起来相似，为什么 $t$ 不是特征函数？$-1$ 对电容意味着什么？

</li>

<li>

输入 $s(t)=\cos t$（即 $\omega_0=1/\mathrm s$）。把余弦分解为两个基本分量，各自乘以对应的 $H(p)$，再合成起来。证明 $g(t)=A\cos(t+\varphi)$，并求 $A$ 和 $\varphi$。$\cos t$ 是特征函数吗？

</li>

</ol>

⁠*(c) 的提示：*$\int_0^\infty\mathrm{e}^{-\tau}\mathrm{d}\tau=1$，$\int_0^\infty\tau\,\mathrm{e}^{-\tau}\mathrm{d}\tau=1$。

:::loesung
(a) $H(p)=\int_0^\infty\mathrm{e}^{-\tau}\mathrm{e}^{-p\tau}\mathrm{d}\tau=\int_0^\infty\mathrm{e}^{-(p+1)\tau}\mathrm{d}\tau=\dfrac{1}{p+1}$。积分当且仅当 $|\mathrm{e}^{-(p+1)\tau}|=\mathrm{e}^{-(\sigma+1)\tau}$ 衰减时收敛，即 $\operatorname{Re} p>-1$。模只取决于 $\sigma$，因为 $|\mathrm{e}^{-\mathrm{j}2\pi f\tau}|=1$。

(b) 直接计算：

$$g(t)=\int_0^\infty\mathrm{e}^{-\tau}\,\mathrm{e}^{-(t-\tau)/2}\mathrm{d}\tau=\mathrm{e}^{-t/2}\int_0^\infty\mathrm{e}^{-\tau/2}\mathrm{d}\tau=2\,\mathrm{e}^{-t/2}.$$

用 $H(p)$：该基本分量的 $p=-\tfrac12$（实数，无振荡）。这个值位于收敛域内，$H(-\tfrac12)=1/(\tfrac12)=2$，因此 $g(t)=2\,\mathrm{e}^{-t/2}$。两种途径结果一致（数值：$g(1\,\mathrm{s})=1.2131$）。

(c) $g(t)=\int_0^\infty\mathrm{e}^{-\tau}(t-\tau)\mathrm{d}\tau=t\int_0^\infty\mathrm{e}^{-\tau}\mathrm{d}\tau-\int_0^\infty\tau\mathrm{e}^{-\tau}\mathrm{d}\tau=t-1$。 这不是 $t$ 的倍数：延迟副本 $t-\tau$ 不是 $t$ 的倍数（因子 $1-\tau/t$ 依赖于 $t$ 本身）。输出是*平移后*的斜坡：电容电压以 $RC=1$ s 的延迟跟随输入斜坡。形状相同，但被平移而非被缩放，因此不是特征函数。

(d) $\cos t=\tfrac12\mathrm{e}^{\mathrm{j} t}+\tfrac12\mathrm{e}^{-\mathrm{j} t}$，基本分量位于 $p=\pm\mathrm{j}$，两者都在收敛域内（$\operatorname{Re} p=0>-1$）。

$$H(\mathrm{j})=\frac{1}{1+\mathrm{j}}=\frac{1}{\sqrt2}\,\mathrm{e}^{-\mathrm{j}\pi/4},\qquad H(-\mathrm{j})=H(\mathrm{j})^*=\frac{1}{\sqrt2}\,\mathrm{e}^{+\mathrm{j}\pi/4}.$$

$$g(t)=\tfrac12H(\mathrm{j})\mathrm{e}^{\mathrm{j} t}+\tfrac12H(-\mathrm{j})\mathrm{e}^{-\mathrm{j} t}=\operatorname{Re}\bigl\{H(\mathrm{j})\mathrm{e}^{\mathrm{j} t}\bigr\}=\frac{1}{\sqrt2}\cos\Bigl(t-\frac\pi4\Bigr).$$

所以 $A=1/\sqrt2\approx0.707$，$\varphi=-45^\circ$（数值：$g(1\,\mathrm{s})=0.6909$）。两个复基本分量各自都是特征函数，但它们的和 $\cos t$ 不是：两个基本分量被乘以*不同的*数，$H(\mathrm{j})\neq H(-\mathrm{j})$。这使相位发生了移动。
:::
:::

## 第 2 阶段：完全由基本分量构成的信号

<span class="anker" id="stufe-2"></span>

:::zweck
第 [1](#stufe-1) 阶段的结论适用于单个基本分量。只有当每个信号都能由基本分量 $\mathrm{e}^{pt}$ 构成时，它才真正有用。本阶段说明这确实可行、权重叫什么，以及其局限在哪里。
:::

### 出发点 $\sigma=0$：纯振荡

<span class="anker" id="stufe-2-1"></span>

在虚轴上（$\sigma=0$），基本分量是纯振荡 $\mathrm{e}^{\mathrm{j}2\pi ft}$。__绝对可积__的信号（$\int|s(t)|\,\mathrm{d} t<\infty$，即在两侧都衰减得足够快）可以由它们构成。这就是傅里叶表示，将在关于傅里叶变换的部分中详细讨论：

$$s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f,\qquad \mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

对于系统理论中的许多信号，这还不够。阶跃 $\varepsilon(t)$ 不衰减，而 $\mathrm{e}^{2t}\varepsilon(t)$（一个不稳定系统的冲激响应）甚至会增长。无界增长的信号无法由恒定幅度的振荡构成。

### 技巧：衰减、分解、再乘回

<span class="anker" id="stufe-2-2"></span>

**思路。** 先使信号变得可分解，之后再撤销这一改动：

<ol>

<li>

⁠**衰减。**乘以 $\mathrm{e}^{-\sigma t}$。若右边信号至多按 $\mathrm{e}^{\alpha t}$ 增长，则对每个 $\sigma>\alpha$，$s(t)\,\mathrm{e}^{-\sigma t}$ 都衰减且绝对可积。

</li>

<li>

⁠**分解。**衰减后的信号是纯振荡的叠加。它的傅里叶频谱恰好就是拉普拉斯变换 $S(p)=\int s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ 在直线 $\operatorname{Re} p=\sigma$ 上的取值（练习 [2](#aufg-2)）：

$$\mathcal{F}\bigl\{s(t)\,\mathrm{e}^{-\sigma t}\bigr\}(f)=S(\sigma+\mathrm{j}2\pi f).$$

</li>

<li>

⁠**再乘回。**把分解式乘以 $\mathrm{e}^{\sigma t}$。该因子与 $f$ 无关，可以移入积分号内。在那里，它把每个振荡 $\mathrm{e}^{\mathrm{j}2\pi ft}$ 变成基本分量 $\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}=\mathrm{e}^{pt}$。

</li>

</ol>

结果正是所猜想的叠加。

:::satz 定理 2.1 (拉普拉斯变换的反演公式)
<span class="anker" id="satz-2-1"></span>

若 $\sigma$ 位于 $S(p)$ 的收敛域内，则

<span class="anker" id="gl-2-1"></span>
$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p =\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f. \tag{2.1}$$
:::

⁠**如何理解：**

<ul>

<li>

积分路径是 $p$ 平面中的竖直线 $\operatorname{Re} p=\sigma$，方向自下而上（$f$ 从 $-\infty$ 到 $+\infty$，图 [2](#abb-2)）。

</li>

<li>

$\mathrm{e}^{pt}$ 是基本分量，$S(p)\,\mathrm{d} p/(2\pi\mathrm{j})=S(\sigma+\mathrm{j}2\pi f)\,\mathrm{d} f$ 是它的复权重。$S(p)$ 本身是一个__密度__：单位频率区间上的权重。若 $s$ 是以 V 为单位的电压，则 $S$ 的单位为 V s。

</li>

<li>

该积分理解为极限 $\lim_{F\to\infty}\int_{-F}^{F}\dots\mathrm{d} f$。在 $s$ 连续的每一点，它给出 $s(t)$；在跳变点，它给出左极限与右极限的平均值。

</li>

</ul>

⁠**极限情形 $\sigma=0$：**若虚轴位于收敛域内，可以选取 $\sigma=0$。此时 $p=\mathrm{j}2\pi f$，式 [(2.1)](#gl-2-1) 就变成傅里叶反演公式。拉普拉斯变换把傅里叶变换作为特例包含在内。

:::herleitung 由傅里叶反演公式得到反演公式
由第 2 步，$S(\sigma+\mathrm{j}2\pi f)$ 是 $s(t)\mathrm{e}^{-\sigma t}$ 的傅里叶频谱。傅里叶反演公式给出

$$s(t)\,\mathrm{e}^{-\sigma t}=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f.$$

乘以与 $f$ 无关的 $\mathrm{e}^{\sigma t}$：

$$s(t)=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f.$$

在 $\sigma$ 固定的情况下作代换 $p=\sigma+\mathrm{j}2\pi f$：$\mathrm{d} p=\mathrm{j}2\pi\,\mathrm{d} f$，即 $\mathrm{d} f=\mathrm{d} p/(2\pi\mathrm{j})$。积分限 $f=\mp\infty$ 变为 $p=\sigma\mp\mathrm{j}\infty$：

$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p.$$
:::

**例：由基本分量合成阶跃。** 对于 $\varepsilon(t)$，$S(p)=1/p$，$\operatorname{Re} p>0$。我们选取 $\sigma=0.5/\mathrm s$（图 [2](#abb-2)）。图 [3](#abb-3) 显示了只叠加 $|f|\le F$ 的基本分量所得的结果。在 $F=0.25$ Hz 时就已能认出阶跃的形状。随着 $F$ 增大，边沿变得更陡；在 $t=0$ 处曲线趋于平均值 $\tfrac12$（0.40、0.47、0.49），在 $t=-1$ s 处趋于零（0.053、0.029、0.008）。

:::abbildung et3/k2linie
阶跃 $\varepsilon(t)$ 的 $p$ 平面，$S(p)=1/p$。收敛域（蓝色阴影）位于极点 $p=0$ 的右侧。其中任何一条竖直线都可以作为积分路径；这里取 $\sigma=0.5/\mathrm s$。直线上的每一点都是一个基本分量 $\mathrm{e}^{pt}$，其权重为 $S(p)$。
:::

:::abbildung et3/k2sprung
由直线 $\operatorname{Re} p=0.5/\mathrm s$ 上的基本分量 $\mathrm{e}^{pt}$ 叠加而成的阶跃，只保留 $|f|\le F$ 的基本分量：$s_F(t)=\int_{-F}^{F}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} f$，其中 $S(p)=1/p$。基本分量越多，阶跃越精确；在 $t=0$ 处曲线趋于 $\tfrac12$。
:::

:::frage 所有基本分量都是复的。为什么得到的是一条实曲线？
基本分量成对出现：$f$ 与 $-f$ 配对，因而 $p$ 与共轭点 $p^*$ 配对。对于实信号，该处的权重是复共轭，$S(p^*)=S(p)^*$（对实的 $s$ 计算 $S(p)=\int s(t)\mathrm{e}^{-pt}\mathrm{d} t$ 即可看出）。每一对给出 $S\mathrm{e}^{pt}+(S\mathrm{e}^{pt})^*=2\operatorname{Re}\{S(p)\mathrm{e}^{pt}\}$，即一个实的衰减或增长振荡。虚部成对抵消。
:::

:::frage 那么它到底是求和还是积分？
一般是积分：直线上分布着连续的基本分量，每个的权重都是无穷小量 $S\,\mathrm{d} f$。在一种重要情形下会出现真正的有限项求和：$S(p)$ 是多项式之比时。此时信号是位于各极点处的基本分量之和（第 [4](#stufe-4) 阶段）。无穷多项之和则是周期信号的傅里叶级数。
:::

### 收敛域：哪些衰减率可行

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

## 第 3 阶段：卷积变成乘法

<span class="anker" id="stufe-3"></span>

:::zweck
第 [1](#stufe-1) 阶段说明系统对单个基本分量做了什么。第 [2](#stufe-2) 阶段说明每个信号都由基本分量组成。两者结合，就得到拉普拉斯变换最重要的定理。
:::

**思路。** LTI 系统是线性的：它分别处理输入的每个基本分量，再把结果相加。它把每个基本分量 $\mathrm{e}^{pt}$ 乘以 $H(p)$。因此输出由与输入*相同*的基本分量组成，只是每个权重都乘上了 $H(p)$。图 [4](#abb-4) 给出了得到输出的两条途径。

:::abbildung et3/k2wege
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
把输入写成叠加 [(2.1)](#gl-2-1) 代入卷积，所取直线 $\operatorname{Re} p=\sigma$ 同时位于两个收敛域内：

$$g(t)=s(t)*h(t)=\left[\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p\right]*h(t).$$

线性：卷积可以移入积分号内，在那里分别作用于每个基本分量：

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\bigl[\mathrm{e}^{pt}*h(t)\bigr]\,\mathrm{d} p.$$

特征函数 [(1.1)](#gl-1-1)：$\mathrm{e}^{pt}*h(t)=H(p)\,\mathrm{e}^{pt}$。

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

两项的反变换由 [(2.2)](#gl-2-2) 取 $p_0=0$ 和 $p_0=-1$ 得到。直接验算：$t>0$ 时 $g(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$。在直线 $\sigma=0.5/\mathrm s$ 上对反演公式 [(2.1)](#gl-2-1) 作数值计算，同样得到 $g(0.5\,\mathrm{s})=0.3935$、$g(1\,\mathrm{s})=0.6321$、$g(3\,\mathrm{s})=0.9502$ 和 $g(-1\,\mathrm{s})=0$，与 $\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)$ 完全一致。

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

输入 $s(t)=t\,\varepsilon(t)$，$S(p)=1/p^2$，$\operatorname{Re} p>0$，即基本变换对 [(2.5)](#gl-2-5)。

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

$t\gg1$ s 时 $g(t)$ 的行为如何？与练习 [1](#aufg-1)c 比较。

</li>

</ol>

:::loesung
(a) $G(p)=\dfrac{1}{p^2}\cdot\dfrac{1}{p+1}=\dfrac{1}{p^2(p+1)}$，$\operatorname{Re} p>0$（$\operatorname{Re} p>0$ 与 $\operatorname{Re} p>-1$ 的交集）。

(b) 通分：$\frac{1}{p^2}-\frac1p+\frac{1}{p+1}=\frac{(p+1)-p(p+1)+p^2}{p^2(p+1)}=\frac{1}{p^2(p+1)}$。用 [(2.5)](#gl-2-5) 和 [(2.2)](#gl-2-2) 作反变换：

$$g(t)=\bigl(t-1+\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

(c) $g(0)=0-1+1=0$：电容电压不能跳变，而输入从零开始。$\dot g(t)=(1-\mathrm{e}^{-t})\varepsilon(t)$，恰好就是阶跃响应。这是吻合的：斜坡是阶跃的积分，所以斜坡响应是阶跃响应的积分。

(d) 当 $t\gg1$ s 时，$\mathrm{e}^{-t}\approx0$，$g(t)\approx t-1$：输出以 $RC=1$ s 的延迟跟随斜坡，与练习 [1](#aufg-1)c 中的双边斜坡完全一样。区别在于基本分量 $\mathrm{e}^{-t}$（系统的极点 $-1$）：这是暂态过程，它的出现是因为这里的斜坡从 $t=0$ 才开始。
:::
:::

## 第 4 阶段：积分变成求和

<span class="anker" id="stufe-4"></span>

:::zweck
按字面意义理解那个猜想：对于系统理论几乎总在处理的那些信号，信号是复指数函数的*有限和*。极点就是指数。
:::

**思路。** 对于由 $R$、$L$、$C$ 构成的网络，以及所有由微分方程描述的系统，$S(p)$ 是多项式之比。在单极点的情况下，__部分分式展开__把它写成

$$S(p)=A_0+\sum_{r=1}^{R}\frac{A_r}{p-p_r},\qquad A_r=\lim_{p\to p_r}(p-p_r)\,S(p).$$

每一项都是*单个基本分量*的变换：若收敛域位于极点右侧，由 [(2.2)](#gl-2-2)，$A_r/(p-p_r)$ 对应 $A_r\,\mathrm{e}^{p_r t}\varepsilon(t)$；由 [(2.4)](#gl-2-4)，常数项 $A_0$ 对应 $A_0\,\delta(t)$。因此，对于右边信号，

<span class="anker" id="gl-4-1"></span>
$$s(t)=A_0\,\delta(t)+\sum_{r=1}^{R}A_r\,\mathrm{e}^{p_r t}\,\varepsilon(t). \tag{4.1}$$

⁠**简而言之：**拉普拉斯变换为有理函数的右边信号，是基本分量 $\mathrm{e}^{p_r t}$ 的有限和。极点就是指数，部分分式系数就是权重。

这意味着，借助图 [1](#abb-1) 的地图，可以从极点读出任何这类信号：$\operatorname{Re} p_r$ 告诉你基本分量是衰减还是增长，$\operatorname{Im} p_r$ 告诉你它振荡得多快。一对共轭极点 $p_r,p_r^*$ 合起来给出一个实的衰减振荡。这也是__稳定性__的核心：因果基本分量 $\mathrm{e}^{p_r t}\varepsilon(t)$ 当且仅当 $\operatorname{Re} p_r<0$ 时衰减。因此，若 $H(p)$ 的所有极点都位于左半平面，因果系统就是稳定的。

**例。** 第 [3](#stufe-3) 阶段中的阶跃响应有极点 $0$ 和 $-1$：

$$g(t)=\underbrace{1\cdot\mathrm{e}^{0\cdot t}}_{\text{极点 $0$（来自 $S$）}}\;\underbrace{-\;1\cdot\mathrm{e}^{-t}}_{\text{极点 $-1$（来自 $H$）}}\qquad(t>0).$$

输入的极点给出由输入强制产生的部分（终值电压 1）。系统的极点给出 RC 电路的__自然响应__，即时间常数为 $RC=1$ s 的衰减。这一点普遍成立：输出 $G=SH$ 既包含输入的极点，也包含系统的极点。

:::zusatz 积分为什么会坍缩成求和：留数定理
本节需要用到复变函数中的留数定理。它解释了为什么 [(2.1)](#gl-2-1) 与 [(4.1)](#gl-4-1) 是一回事，以及为什么收敛域决定信号。

设 $S(p)$ 是分子次数低于分母次数、且只有单极点的多项式之比。

<ul>

<li>

⁠**$t>0$：**用一个向*左*的大半圆把积分直线闭合。在那里 $\operatorname{Re} p\to-\infty$，因此 $|\mathrm{e}^{pt}|=\mathrm{e}^{\operatorname{Re} p\,t}\to0$，且 $S(p)\to0$。在极限下，半圆没有贡献（约当引理）。闭合路径沿逆时针方向，由留数定理得

$$s(t)=\sum_{\text{直线左侧的极点}}\operatorname*{Res}_{p=p_r}\bigl[S(p)\,\mathrm{e}^{pt}\bigr]=\sum_{\text{左侧}}A_r\,\mathrm{e}^{p_r t}.$$

单极点处的留数为 $\lim_{p\to p_r}(p-p_r)S(p)\mathrm{e}^{pt}=A_r\mathrm{e}^{p_rt}$：恰好就是部分分式系数。

</li>

<li>

⁠**$t<0$：**此时 $\mathrm{e}^{pt}$ 在 $\operatorname{Re} p\to+\infty$ 时趋于零。向*右*闭合；路径沿顺时针方向，因而出现一个负号：

$$s(t)=-\sum_{\text{直线右侧的极点}}A_r\,\mathrm{e}^{p_r t}.$$

</li>

</ul>

⁠**结论：**直线的位置，也就是收敛域，决定了哪些极点给出因果基本分量（直线左侧），哪些给出反因果基本分量（直线右侧）。例：$S(p)=\frac{1}{(p+1)(p+2)}=\frac{1}{p+1}-\frac{1}{p+2}$（图 [5](#abb-5)）。若直线位于两极点之间，$-2<\sigma<-1$，则 $-2$ 对 $t>0$ 起作用，$-1$ 对 $t<0$ 起作用：

$$s(t)=-\mathrm{e}^{-2t}\varepsilon(t)-\mathrm{e}^{-t}\varepsilon(-t).$$

在直线 $\sigma=-1.5/\mathrm s$ 上数值计算得：$s(1\,\mathrm{s})=-0.1353=-\mathrm{e}^{-2}$，$s(-1\,\mathrm{s})=-2.7183=-\mathrm{e}^{1}$。若直线位于两个极点的右侧，同一公式给出因果信号 $(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(t)$；若位于两个极点的左侧，则给出反因果信号 $-(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(-t)$。

:::abbildung et3/k2residuen
带状区域 $-2<\operatorname{Re} p<-1$（蓝色）中的积分直线 $\sigma=-1.5/\mathrm s$，以及将其闭合的半圆（红色）。
:::
:::

:::aufgabe 练习 7 ★★★ （拓展阅读）同一公式，两个信号
<span class="anker" id="aufg-7"></span>

$S(p)=\dfrac{1}{p+1}$。

<ol class="al">

<li>

收敛域为 $\operatorname{Re} p>-1$。用留数定理计算反演公式，分 $t>0$ 和 $t<0$ 两种情况。

</li>

<li>

对收敛域 $\operatorname{Re} p<-1$ 做同样的计算。

</li>

<li>

与基本变换对 [(2.2)](#gl-2-2) 和 [(2.3)](#gl-2-3) 比较。对于不给出收敛域的说法“$S(p)=1/(p+1)$”，你从中得到什么启示？

</li>

</ol>

:::loesung
(a) 直线位于极点右侧，例如 $\sigma=0$。$t>0$ 时向左闭合：极点 $-1$ 在内部，$\operatorname*{Res}_{p=-1}\frac{\mathrm{e}^{pt}}{p+1}=\mathrm{e}^{-t}$，因此 $s(t)=\mathrm{e}^{-t}$。$t<0$ 时向右闭合：直线右侧没有极点，因此 $s(t)=0$。合起来，$s(t)=\mathrm{e}^{-t}\varepsilon(t)$。

(b) 直线位于极点左侧，例如 $\sigma=-2$。$t>0$ 时向左闭合：没有极点，$s(t)=0$。$t<0$ 时向右闭合：极点在内部，路径为顺时针，$s(t)=-\mathrm{e}^{-t}$。合起来，$s(t)=-\mathrm{e}^{-t}\varepsilon(-t)$。

(c) 这恰好是 $p_0=-1$ 时的基本变换对 [(2.2)](#gl-2-2) 和 [(2.3)](#gl-2-3)。仅凭“$S(p)=1/(p+1)$”这一说法无法确定信号。只有给出收敛域，才能明确极点位于直线的哪一侧，以及它给出的是因果还是反因果基本分量。
:::
:::

## 第 5 阶段：为什么输入也要变换

<span class="anker" id="stufe-5"></span>

:::frage 对 $h(t)$ 作变换是有道理的，这样我就能把特征函数乘以 $H(p)$，求出输出。但对 $s(t)$ 作变换，乍看之下似乎没有意义；从系统理论的角度，我拿它做不了什么。当然，$s*h=h*s$，但 $h(t)$ 通常不是特征函数，所以我不能写 $h(t)\cdot S(p)$。从系统的角度看，对一个任意信号作变换意味着什么？
⁠**问题中正确的部分：**$H(p)$ 说明系统对基本分量 $\mathrm{e}^{pt}$ 做了什么。而 $h(t)\cdot S(p)$ 确实没有意义。

⁠**推理错在哪里：**输入几乎也从来不是特征函数。阶跃、语音信号或矩形脉冲都不是单个基本分量 $\mathrm{e}^{pt}$。因此 $H(p)\cdot s(t)$ 和 $h(t)\cdot S(p)$ 一样没有意义：$H(p)$ 只能作用于一个基本分量，而对任意的 $s(t)$，甚至不清楚指的是哪个 $p$。在 $H(p)$ 能起任何作用之前，必须先把输入分解为基本分量。这正是 $S(p)$ 所做的事。

⁠**正确的看法：**在卷积定理 $G(p)=H(p)\,S(p)$ 中，每个因子都有其自身的系统含义：

<ul>

<li>

$S(p)$ 是*输入的“配方”*：输入中含有多少基本分量 $\mathrm{e}^{pt}$；

</li>

<li>

$H(p)$ 是*系统的作用*：系统把这个基本分量乘以的那个数；

</li>

<li>

$G(p)$ 是输出的“配方”。

</li>

</ul>

没有 $S(p)$，你只知道系统对各个基本分量的作用，却不知道到达的是哪些基本分量。$H(p)$ 单独只能在一种特殊情况下回答“输出端会发生什么？”这个问题：输入本身就是单个基本分量。

⁠**例：阶跃与 RC 低通滤波器。**阶跃的配方是 $S(p)=1/p$。在直线 $\sigma=0.5/\mathrm s$ 上，$f=0$ 时 $|S|=2$，1 Hz 时为 $0.16$，10 Hz 时为 $0.016$。快速基本分量很弱，但确实存在，正是它们构成了陡峭的边沿（图 [3](#abb-3)：快速基本分量越多，边沿越陡）。RC 低通滤波器把它们分别乘以 $|H|=0.67$、$0.15$ 和 $0.016$。因此在输出中，快速基本分量又被削弱了大约 $2\pi f\cdot RC$ 倍（对于 $f\gg1/(2\pi RC)=0.16$ Hz），边沿也就消失了：$g(t)=1-\mathrm{e}^{-t}$ 连续上升。这一解释需要两个变换。$H$ 单独只能说明“快速基本分量被削弱”；只有 $S$ 才说明边沿由快速基本分量构成。

⁠**那么对称性 $s*h=h*s$ 呢？**在数学上，两个信号地位平等：也可以把 $h$ 看作输入、把 $s$ 看作“系统”，这时 $H(p)$ 是配方，$S(p)$ 是作用。系统理论只是根据物理意义来分配角色：一个信号来自外部，另一个描述电路。在变换域中，*两者*总是都要被变换。
:::

**单独变换一个信号的其他理由。**

<ul>

<li>

⁠**测量一个系统。**若测出一个未知系统的输入和输出，$H(p)=G(p)/S(p)$ 就给出了这个系统。为此要对两个信号分别作变换（练习 [9](#aufg-9)）。

</li>

<li>

⁠**理解信号本身。**敲钟发出的声音是若干衰减振荡之和，每个振荡对应一对共轭极点。$\operatorname{Im} p_r$ 是某个分音的音高，$-\operatorname{Re} p_r$ 是它的衰减率。少数几个极点就描述了整个声音。显示频谱的仪器在直线 $\sigma=0$ 上做的是同样的事。

</li>

<li>

⁠**没有系统的卷积。**卷积把一个信号经过平移和加权的副本叠加起来。系统只是这种运算的一种解释，而不是唯一的解释。一个完全不涉及系统的例子是两个骰子的点数之和，见关于卷积的练习册（[第 1 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)）。

</li>

</ul>

:::ltspice 符合两次测量的网络
⁠**绘制：**你在练习 [9](#aufg-9)(c) 中找到的网络，输入端接信号源 `PULSE(0 1 0 1u 1u 100)`，输出接节点 `out`。旁边放一个不与电路相连的行为源 `bv`，接在节点 `mess` 上，取 `V=1-exp(-2*time)`。它充当测得的输出曲线。

⁠**指令：**`.tran 0 3 0 1m`，`.meas tran dev MAX abs(V(out)-V(mess))`。

⁠**你会看到：**如果网络和元件值都正确，`V(out)` 和 `V(mess)` 就重合在一起，最大偏差 `dev` 实际上为零（小于 $10^{-5}$）。用这种方法，把这些曲线与你在练习 [9](#aufg-9)(c) 中的结果比较。
:::

:::aufgabe 练习 8 ★★ 哪些基本分量构成了边沿？
<span class="anker" id="aufg-8"></span>

输入 $\varepsilon(t)$，系统：$RC=1$ s 的 RC 低通滤波器。考虑直线 $\sigma=0.5/\mathrm s$ 上的基本分量。

<ol class="al">

<li>

对 $f=0$、$1$ Hz 和 $10$ Hz，计算 $|S(p)|$、$|H(p)|$ 和 $|G(p)|$。

</li>

<li>

与 1 Hz 处的基本分量相比，系统对 10 Hz 处的基本分量多削弱了多少倍？

</li>

<li>

利用 (a) 和图 [3](#abb-3) 解释为什么输出没有边沿。为什么仅凭 $H(p)$ 不足以作出这一解释？

</li>

</ol>

:::loesung
(a) 令 $p=0.5+\mathrm{j}2\pi f$（单位 $1/\mathrm s$），$S=1/p$，$H=1/(p+1)$，$G=SH$：

| $f$ | $\vert S(p)\vert $ | $\vert H(p)\vert $ | $\vert G(p)\vert $ |
|---|---|---|---|
| 0 | 2 | 0.667 | 1.33 |
| 1 Hz | 0.159 | 0.155 | 0.0246 |
| 10 Hz | 0.0159 | 0.0159 | 0.000253 |

(b) $0.155/0.0159\approx9.7$，即差不多是 10 倍，与频率之比一样。对于大的 $|p|$，$|H|\approx1/|p|\approx1/(2\pi f)$。

(c) 阶跃的边沿由快速基本分量构成：在图 [3](#abb-3) 中，包含的快速基本分量越多，边沿越陡。在输入中，它们的权重按 $1/f$ 下降，在输出中按 $1/f^2$ 下降。在输出中，快速基本分量弱到不再形成边沿，$g(t)$ 连续上升。$H(p)$ 单独只说明快速基本分量被削弱。边沿恰恰由这些基本分量构成，这是关于输入的结论，而这一结论包含在 $S(p)$ 中。
:::
:::

:::aufgabe 练习 9 ★★ 由两次测量确定未知系统
<span class="anker" id="aufg-9"></span>

在 $t=0$ 时刻，向一个未知的因果 LTI 系统施加 1 V 电压，$s(t)=\varepsilon(t)$（单位 V）。在输出端测得 $g(t)=\bigl(1-\mathrm{e}^{-2t}\bigr)\varepsilon(t)$（单位 V，$t$ 的单位为 s）。

<ol class="al">

<li>

对两个信号分别作变换。

</li>

<li>

求 $H(p)$，并由此求 $h(t)$。

</li>

<li>

它可能是什么网络？得到什么参数值？

</li>

<li>

$G(p)$ 中哪个极点来自输入，哪个来自系统？

</li>

</ol>

:::loesung
(a) $S(p)=\dfrac1p$，$\operatorname{Re} p>0$。$G(p)=\dfrac1p-\dfrac{1}{p+2}=\dfrac{2}{p(p+2)}$，$\operatorname{Re} p>0$（基本变换对 [(2.2)](#gl-2-2)，取 $p_0=0$ 和 $p_0=-2$）。

(b) $H(p)=\dfrac{G(p)}{S(p)}=\dfrac{2}{p+2}$。由于系统是因果的，收敛域位于极点右侧：$\operatorname{Re} p>-2$。由 [(2.2)](#gl-2-2)：$h(t)=2\,\mathrm{e}^{-2t}\varepsilon(t)$，单位为 $1/\mathrm s$。

(c) RC 低通滤波器的 $H(p)=\dfrac{1}{1+pRC}=\dfrac{1/RC}{p+1/RC}$。与 $\dfrac{2}{p+2}$ 比较得 $RC=0.5$ s，例如 $R=500\,\mathrm{k\Omega}$，$C=1$ µ F。（任何具有相同传递函数的其他网络，在端口处的表现都完全相同。输入端和输出端的测量只能揭示 $H$，而不能揭示元件。）

(d) 极点 $p=0$ 来自输入（阶跃），极点 $p=-2$ 来自系统。在除法 $G/S$ 中，被约去的恰好是输入的极点。
:::
:::

:::kern 本文要点
<ul>

<li>

$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\mathrm{e}^{pt}$，因此 $\mathrm{e}^{pt}*h=H(p)\,\mathrm{e}^{pt}$，其中 $H(p)=\int h(t)\mathrm{e}^{-pt}\mathrm{d} t$。

</li>

<li>

$p=\sigma+\mathrm{j}2\pi f$：$\sigma$ 是基本分量的增长率，$f$ 是其频率。

</li>

<li>

$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\mathrm{e}^{pt}\mathrm{d} p$，$\sigma$ 位于收敛域内；每条这样的直线都给出同一个 $s(t)$。

</li>

<li>

$S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}$；$\sigma=0$ 时即为傅里叶变换。

</li>

<li>

收敛域：只取决于 $\sigma$；右边信号为右半平面，左边信号为左半平面，双边信号为带状区域。

</li>

<li>

$\mathrm{e}^{p_0t}\varepsilon(t)\leftrightarrow\frac{1}{p-p_0}$，$\operatorname{Re} p>\operatorname{Re} p_0$；$-\mathrm{e}^{p_0t}\varepsilon(-t)\leftrightarrow\frac{1}{p-p_0}$，$\operatorname{Re} p<\operatorname{Re} p_0$。

</li>

<li>

$G(p)=S(p)H(p)$；求导 $\to p$，积分 $\to1/p$。

</li>

<li>

有理且右边：$s(t)=A_0\delta(t)+\sum_rA_r\mathrm{e}^{p_rt}\varepsilon(t)$，极点 = 指数。因果且稳定：所有极点都在左侧。

</li>

</ul>
:::
