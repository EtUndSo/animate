---
title: 第 3 阶段：什么是 LTI 系统
pfad: 电气工程 / 第 3 学期 / 信号与系统 / LTI 系统与卷积
order: 3210400
summary: RC 电路具有两个性质，其余一切都建立在这两个性质之上：它是线性的，并且是时不变的。本阶段给出这两个性质的定义，并说明它们使什么成为可能。
tags: 系统, 变换, 线性, 时不变, LTI 系统
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
RC 电路具有两个性质，其余一切都建立在这两个性质之上：它是线性的，并且是时不变的。本阶段给出这两个性质的定义，并说明它们使什么成为可能。
:::

__系统__把输入信号对应到一个输出信号：

$$g(t)=\operatorname{Tr}\{s(t)\}.$$

这种从函数到函数的映射称为__变换__。它并不是把一个数值映射为另一个数值：时刻 $t$ 的输出可以取决于输入在过去的整个变化过程。在 RC 电路中，$u_2(t)$ 取决于到时刻 $t$ 为止积累了多少电荷。

:::definition 定义 3.1 (LTI 系统)
<span class="anker" id="satz-3-1"></span>

称一个系统为

<ul>

<li>

__线性__系统，如果对任意常数 $a_i$ 叠加原理都成立：

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Tr}\Bigl\{\sum_ia_is_i(t)\Bigr\}=\sum_ia_i\operatorname{Tr}\{s_i(t)\}=\sum_ia_ig_i(t); \tag{3.1}$$

</li>

<li>

__时不变__系统，如果对任意平移量 $t_0$ 都有

<span class="anker" id="gl-3-2"></span>
$$\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0). \tag{3.2}$$

</li>

</ul>

既线性又时不变的系统简称为__LTI 系统__（LTI 即 linear time-invariant，线性时不变）。
:::

在 RC 电路中，线性来自这样一个事实：微分方程 [(2.1)](ein-erstes-system-das-rc-glied.html#gl-2-1) 中既不含 $u_1$ 与 $u_2$ 的乘积，也不含它们的平方。时不变性则来自 $R$ 和 $C$ 不随时间变化。所有由 $R$、$L$、$C$ 组成的网络都可以用常系数线性微分方程来描述。但并非每个 LTI 系统都如此：例如理想延时器只把输入信号延迟一段固定时间，它就没有这样的方程。

**这两个性质带来了什么。** 如果已知系统对矩形脉冲 $s_0$ 的响应 $g_0$，那么无需进一步计算，就能知道系统对任意多个经过平移和缩放的矩形脉冲之和的响应。图 [4](#abb-4) 以 $s(t)=s_0(t)+0.5\,s_0(t-2)$ 为例展示了这一点：输出为 $g_0(t)+0.5\,g_0(t-2)$。

:::abbildung et3/k1doppel 4
左：矩形 $s_0$（高度 1 V，持续时间 1 s）及 RC 电路的响应 $g_0$。右：一对脉冲。响应（红色）是 $g_0(t)$ 与经过平移、减半的副本 $0.5\,g_0(t-2)$（虚线）之和。
:::

:::frage $g(t)=2s(t)+1$ 是线性的吗？它的特性曲线毕竟是一条直线啊。
不是。对于线性系统，零输入必须产生零输出：在式 [(3.1)](#gl-3-1) 中令所有 $a_i=0$，就得到 $\operatorname{Tr}\{0\}=0$。而这里 $\operatorname{Tr}\{0\}=1$。叠加原理同样不成立：两个输入分别作用时，输出之和为 $2s_1+2s_2+2$；而两者同时作用时，输出为 $2s_1+2s_2+1$。不经过原点的直线称为*仿射*的，而不是线性的。
:::

:::ltspice 验证叠加性：两个矩形
⁠**绘制：**第 [2](ein-erstes-system-das-rc-glied.html#stufe-2) 阶段中的 RC 电路，但用两个串联的电压源 `voltage`：`V1` 负端接地、正端接节点 `a`，值为 `PULSE(0 {a1} 0 1u 1u 1)`；在它上面串接 `V2`，从 `a` 接到 `in`，值为 `PULSE(0 {a2} 2 1u 1u 1)`。串联时电压相加，因此 RC 电路得到的输入是 $a_1s_0(t)+a_2s_0(t-2)$。

⁠**指令：**`.param a1=1 a2=0.5`，`.step param a1 list 0 1`，`.step param a2 list 0 0.5`，`.tran 0 6 0 1m`。LTspice 运行全部四种组合，并把结果叠画在一起。

⁠**你会看到：**曲线 $0$、$g_0(t)$、$0.5\,g_0(t-2)$ 以及它们的和，与图 [4](#abb-4) 相同。在 $t=2.5$ s 处：$0.141+0.197=0.338$。输入之和给出响应之和（线性），平移 2 s 的信号源给出平移 2 s 的曲线（时不变性）。
:::

:::aufgabe 练习 3 ★ 是不是 LTI？
<span class="anker" id="aufg-3"></span>

检验下列各系统是否线性、是否时不变： (a) $g(t)=3\,s(t-2)$， (b) $g(t)=s(t)^2$， (c) $g(t)=s(t)+1$， (d) $g(t)=t\,s(t)$， (e) $g(t)=s(2t)$， (f) $g(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$。

:::loesung
(a) 线性且时不变（增益为 3，延迟为 2）：LTI。 (b) 非线性：$\operatorname{Tr}\{2s\}=4s^2\neq2s^2$。时不变。 (c) 非线性（仿射，$\operatorname{Tr}\{0\}=1$）。时不变。 (d) 线性。不是时不变的：$\operatorname{Tr}\{s(t-t_0)\}=t\,s(t-t_0)$，但 $g(t-t_0)=(t-t_0)\,s(t-t_0)$。因子 $t$ 是一个随时间变化的元件。 (e) 线性。不是时不变的：$\operatorname{Tr}\{s(t-t_0)\}=s(2t-t_0)$，但 $g(t-t_0)=s(2t-2t_0)$。压缩时间的同时，也压缩了每一次平移。 (f) LTI。线性，因为积分是线性的。时不变：$\int_{-\infty}^ts(\tau-t_0)\mathrm{d}\tau=\int_{-\infty}^{t-t_0}s(\vartheta)\mathrm{d}\vartheta=g(t-t_0)$。它的冲激响应为 $\varepsilon(t)$（第 [8](integrieren-und-differenzieren.html#stufe-8) 阶段）。
:::
:::
