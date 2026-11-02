---
title: 第 10 阶段：放电与时间常数
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电容器
order: 1131100
summary: 已充电的电容器通过电阻把电荷放回。这是同一个方程，只是初始值不同。由此得到适用于 RC 电路中每个开关过程的规则。
tags: 
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
已充电的电容器通过电阻把电荷放回。这是同一个方程，只是初始值不同。由此得到适用于 RC 电路中每个开关过程的规则。
:::

**基本思路。** 开关从位置 1 转到位置 2，电池被断开。电容器保持 9 V，因为电压不能跳变。这个电压现在加在 $R$ 上。负极板的电子经 $R$ 流回正极板。所以电流与图 [9](aufladen-uber-einen-widerstand.html#abb-9) 的参考箭头方向相反，而且发生跳变：刚才还是零，现在是 $-0.9$ mA。每流走一份电荷，电压就下降一些，电流也随之下降。电容器起初相当于一个越来越弱的电源。

:::satz 定理 10.1 (放电)
<span class="anker" id="satz-10-1"></span>

没有电池时，基尔霍夫电压定律为 $u_R+u_C=0$，即 $RC\,\mathrm{d} u_C/\mathrm{d} t+u_C=0$。当 $u_C(0)=U_0$ 且 $t\ge0$ 时，有

<span class="anker" id="gl-10-1"></span>
$$u_C(t)=U_0\,\mathrm{e}^{-t/\tau},\qquad i(t)=-\frac{U_0}{R}\,\mathrm{e}^{-t/\tau},\qquad u_R(t)=-U_0\,\mathrm{e}^{-t/\tau}. \tag{10.1}$$
:::

一般地，对于恒定电源的 RC 电路中的每个开关过程，电压都从初始值 $u_C(0)$ 变化到最终值 $u_\infty$：

<span class="anker" id="gl-10-2"></span>
$$u_C(t)=u_\infty+\bigl(u_C(0)-u_\infty\bigr)\,\mathrm{e}^{-t/\tau}. \tag{10.2}$$

⁠**如何理解：**$i$ 的负号表示电流与参考箭头方向相反。$u_\infty$ 是电容器经过很长时间达到的电压，充电时为 $U_0$，放电时为 0。与最终值的差每经过时间 $\tau$ 就缩小到 36.8 %。**适用条件：**$\tau$ 用相应电流路径的电阻计算。这里两个位置的 $R$ 相同。

:::herleitung 一般规则
对于距离 $x=u_\infty-u_C$，与第 [9](aufladen-uber-einen-widerstand.html#stufe-9) 阶段一样有 $\mathrm{d} x/\mathrm{d} t=-x/\tau$。写成 $\ln|x|$ 后，第 2 到 4 步对 $x$ 的任何符号都成立，并给出 $x(t)=x(0)\,\mathrm{e}^{-t/\tau}$。代入 $x(0)=u_\infty-u_C(0)$，就得到式 [(10.2)](#gl-10-2)。令 $u_\infty=0$ 得式 [(10.1)](#gl-10-1)，令 $u_\infty=U_0$ 且 $u_C(0)=0$ 得式 [(9.3)](aufladen-uber-einen-widerstand.html#gl-9-3)。
:::

**时间常数。** $\tau=RC$ 是电流和剩余电压降到 $1/\mathrm{e}$ 所需的时间。充电时这时已达到 63.2 %。$C$ 越小，要移动的电荷越少，$R$ 越小，电流越大，充放电都越快。$\tau$ 中没有 $U_0$：电压加倍使电流加倍，但电荷也加倍。下表适用于任何 RC 电路，最后一行针对参考模型。

| 时间 | $1\tau$ | $2\tau$ | $3\tau$ | $4\tau$ | $5\tau$ |
|---|---|---|---|---|---|
| 充电：$1-\mathrm{e}^{-t/\tau}$，单位 % | 63.2 | 86.5 | 95.0 | 98.2 | 99.3 |
| 放电：$\mathrm{e}^{-t/\tau}$，单位 % | 36.8 | 13.5 | 5.0 | 1.8 | 0.7 |
| 充电：$u_C$，单位 V | 5.69 | 7.78 | 8.55 | 8.84 | 8.94 |

:::abbildung et1/k3entladen 12
充电五秒，放电五秒。电压连续变化，百分数在充电时相对于最终值，在放电时相对于初始值。电流在切换时跳变，放电时改变符号，虚线表示跳变。
:::

**例。** 在参考模型中，放电从 9 V 开始。在最初瞬间，$u_R=-9$ V，$i=-0.9$ mA。1 s 后 $u_C=3.31$ V，$i=-0.331$ mA；3 s 后只剩 0.448 V。如果像图 [12](#abb-12) 那样只充电 5 s，放电就从 8.94 V 开始。

⁠**检验：**放电时流过 $R$ 的电荷为 $\int_0^\infty|i|\,\mathrm{d} t=\frac{U_0}{R}\,\tau=C\,U_0$，恰好等于储存的电荷。**极限情况：**当 $u_C(0)=u_\infty$ 时，式 [(10.2)](#gl-10-2) 中的括号为零：什么也不发生，电容器已处于最终状态。

:::frage 为什么切换时电流可以跳变，而电压不可以？
电压与储存的电荷相关联，而电荷只能以有限的电流在有限的时间内改变。电流没有这样的储存量。它在每一时刻都由 $R$ 上的电压决定，而这个电压在开关动作时就改变了。
:::

:::ltspice RC 电路的充电与放电
⁠**绘制：**`voltage`，从 `in` 到接地点，值为 `PULSE(0 9 0 1u 1u 5 10)`；`res`，值为 `10k`，从 `in` 到 `out`；`cap`，值为 `100u`，从 `out` 到接地点。信号源代替开关：5 s 内为 9 V，然后为 0 V，这相当于一条经 $R$ 返回的路径。

⁠**指令：**`.tran 0 10 0 1m`，另外加测量语句，如 `.meas tran u1 FIND V(out) AT=1`，用于 $t=1$、2、3、5 和 6 s，以及 `.meas tran i0 FIND I(R1) AT=10u`。

⁠**你会看到：**充电时为 5.69 V、7.78 V、8.55 V、8.94 V，与表中一致；6 s 时为 3.29 V，即 8.94 V 的 36.8 %。起点处 `i0` $=0.90$ mA。然后设置 12 V、`4.7k` 和 `220u`，检查你在练习 [10](aufladen-uber-einen-widerstand.html#aufg-10) 中的结果。
:::

:::aufgabe 练习 12 ★★ 初始值与自放电
<span class="anker" id="aufg-12"></span>

设 $R=10\,\mathrm{k\Omega}$，$C=100\,\mu\text{F}$，$\tau=1$ s。

<ol class="al">

<li>

接入 $U_0=9$ V 时，电容器上已有 3 V。写出 $u_C(t)$，并计算 $u_C(1\,\mathrm{s})$。

</li>

<li>

这时 $u_C$ 从 3 V 升到 6 V 需要多长时间？

</li>

<li>

从 9 V 开始放电：$u_C$ 何时降到 1 V 以下？

</li>

<li>

已充电（9 V）的电容器被断开，只有 $R_\mathrm{I}=1\,\mathrm{M\Omega}$ 使它放电。一分钟后 $u_C$ 是多少？

</li>

</ol>

:::loesung
(a) 由式 [(10.2)](#gl-10-2)，$u_\infty=9$ V，$u_C(0)=3$ V：$u_C(t)=9\,\mathrm{V}-6\,\mathrm{V}\cdot\mathrm{e}^{-t/\tau}$。当 $t=1$ s 时：6.79 V。

(b) 由 $6=9-6\,\mathrm{e}^{-t/\tau}$ 得 $\mathrm{e}^{-t/\tau}=\frac12$，因此 $t=\tau\ln2=0.693$ s。

(c) 由 $9\,\mathrm{e}^{-t/\tau}=1$ 得 $t=\tau\ln9=2.20$ s。

(d) 时间常数为 $R_\mathrm{I}\,C=100$ s，因此 $u_C(60\,\mathrm{s})=9\,\mathrm{V}\cdot\mathrm{e}^{-0.6}=4.94$ V。
:::
:::
