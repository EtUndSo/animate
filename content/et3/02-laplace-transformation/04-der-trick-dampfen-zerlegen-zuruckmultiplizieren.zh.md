---
title: 技巧：衰减、分解、再乘回
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 拉普拉斯变换
order: 3220400
summary: 每个信号都是 $\mathrm{e}^{pt}$ 的叠加， 以及为什么 LTI 系统的作用因此变成乘法
tags: 密度
lang: zh
---

<span class="anker" id="stufe-2-2"></span>

**思路。** 先使信号变得可分解，之后再撤销这一改动：

<ol>

<li>

⁠**衰减。**乘以 $\mathrm{e}^{-\sigma t}$。若右边信号至多按 $\mathrm{e}^{\alpha t}$ 增长，则对每个 $\sigma>\alpha$，$s(t)\,\mathrm{e}^{-\sigma t}$ 都衰减且绝对可积。

</li>

<li>

⁠**分解。**衰减后的信号是纯振荡的叠加。它的傅里叶频谱恰好就是拉普拉斯变换 $S(p)=\int s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ 在直线 $\operatorname{Re} p=\sigma$ 上的取值（练习 [2](konvergenzbereich-welche-dampfungen-funktionieren.html#aufg-2)）：

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

:::abbildung et3/k2linie 2
阶跃 $\varepsilon(t)$ 的 $p$ 平面，$S(p)=1/p$。收敛域（蓝色阴影）位于极点 $p=0$ 的右侧。其中任何一条竖直线都可以作为积分路径；这里取 $\sigma=0.5/\mathrm s$。直线上的每一点都是一个基本分量 $\mathrm{e}^{pt}$，其权重为 $S(p)$。
:::

:::abbildung et3/k2sprung 3
由直线 $\operatorname{Re} p=0.5/\mathrm s$ 上的基本分量 $\mathrm{e}^{pt}$ 叠加而成的阶跃，只保留 $|f|\le F$ 的基本分量：$s_F(t)=\int_{-F}^{F}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} f$，其中 $S(p)=1/p$。基本分量越多，阶跃越精确；在 $t=0$ 处曲线趋于 $\tfrac12$。
:::

:::frage 所有基本分量都是复的。为什么得到的是一条实曲线？
基本分量成对出现：$f$ 与 $-f$ 配对，因而 $p$ 与共轭点 $p^*$ 配对。对于实信号，该处的权重是复共轭，$S(p^*)=S(p)^*$（对实的 $s$ 计算 $S(p)=\int s(t)\mathrm{e}^{-pt}\mathrm{d} t$ 即可看出）。每一对给出 $S\mathrm{e}^{pt}+(S\mathrm{e}^{pt})^*=2\operatorname{Re}\{S(p)\mathrm{e}^{pt}\}$，即一个实的衰减或增长振荡。虚部成对抵消。
:::

:::frage 那么它到底是求和还是积分？
一般是积分：直线上分布着连续的基本分量，每个的权重都是无穷小量 $S\,\mathrm{d} f$。
:::
