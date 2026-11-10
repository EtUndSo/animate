---
title: 第 4 阶段：自相关、协方差与互相关
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 随机信号
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: 第 7 章：随机信号
order: 3270500
summary: 随机信号变化得有多快？自相关函数给出答案：经过时间 tau 之后，信号与自身还有多相似。
tags: 自协方差函数
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
随机信号变化得有多快？自相关函数给出答案：经过时间 $\tau$ 之后，信号与自身还有多相似。
:::

:::satz 定理 4.1 (平稳过程自相关函数的性质)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi_{ss}(0)=L_s,\qquad\varphi_{ss}(\tau)=\varphi_{ss}(-\tau),\qquad|\varphi_{ss}(\tau)|\le\varphi_{ss}(0). \tag{4.1}$$

对各态历经过程，$\varphi_{ss}(\tau)=\overline{s(t)s(t+\tau)}$，即[第 6 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)中功率信号的自相关函数。
:::

:::herleitung $\tau=0$ 处的最大值
$\mathrm E\{[s(t)\pm s(t+\tau)]^2\}\ge0$，因为平方的数学期望永不为负。展开并利用线性：$\mathrm E\{s^2(t)\}+\mathrm E\{s^2(t+\tau)\}\pm2\mathrm E\{s(t)s(t+\tau)\}\ge0$，因此 $2\varphi_{ss}(0)\pm2\varphi_{ss}(\tau)\ge0$。偶对称性：在定义中作代换 $t\to t-\tau$。
:::

**协方差。** 若先减去均值，就得到__自协方差函数__

<span class="anker" id="gl-4-2"></span>
$$\mu_{ss}(\tau)=\mathrm E\{[s(t)-m_s][s(t+\tau)-m_s]\}=\varphi_{ss}(\tau)-m_s^2,\qquad\mu_{ss}(0)=\sigma_s^2. \tag{4.2}$$

若过程不含周期分量，相距很远的取值就变得相互独立：当 $\tau\to\infty$ 时，$\varphi_{ss}(\tau)\to m_s^2$，$\mu_{ss}(\tau)\to0$。

**互相关与和。** 对两个过程，$\varphi_{uv}(\tau)=\mathrm E\{u(t)v(t+\tau)\}$，且 $\varphi_{vu}(\tau)=\varphi_{uv}(-\tau)$；互协方差为 $\mu_{uv}(\tau)=\varphi_{uv}(\tau)-m_um_v$。对和 $s=u+v$，展开得

<span class="anker" id="gl-4-3"></span>
$$\varphi_{ss}(\tau)=\varphi_{uu}+\varphi_{uv}+\varphi_{vu}+\varphi_{vv},\qquad L_s=L_u+L_v+2\varphi_{uv}(0),\qquad\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0). \tag{4.3}$$

⁠**简而言之：**只有当信号互不相关时，功率才直接相加。否则还要加上交叉项。两个相同的信号给出四倍的功率，两个相反的信号给出零功率。

:::aufgabe 练习 2 ★★ 两个噪声源
<span class="anker" id="aufg-2"></span>

把两个有效值分别为 3 mV 和 4 mV 的零均值噪声电压相加。在下列情况下，和的有效值是多少：(a) 二者不相关，(b) 二者形状相同（$\varphi_{uv}(0)=\sigma_u\sigma_v$），(c) 二者形状相同但符号相反（$\varphi_{uv}(0)=-\sigma_u\sigma_v$）？

:::loesung
(a) $\sigma=\sqrt{9+16}=5$ mV。(b) $\sigma^2=9+16+2\cdot12=49$，因此为 7 mV：幅度直接相加。(c) $\sigma^2=9+16-24=1$，因此为 1 mV：两个信号几乎相互抵消。
:::
:::
