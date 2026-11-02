---
title: 第 1 阶段：为什么偏偏是 $\mathrm{e}^{pt}$
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 拉普拉斯变换
order: 3220200
summary: 把 e pt 代入卷积积分，结果是 H(p)\,e pt ： e pt 是一个特征函数。本阶段探讨 e pt 的哪种性质导致了这一点，以及为什么基本分量必须取复数形式。
tags: 增长率, 频率
lang: zh
---

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

:::abbildung et3/k2bausteine 1
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
