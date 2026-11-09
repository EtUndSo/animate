---
title: 第 1 阶段：物理量、力与功
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电荷、电场与电位
order: 1110300
summary: 电压将被证明是单位电荷所得的功。为此需要带单位的物理量、力、功和动能。
tags: 定性, 定量, 欧姆定律, 物理量, 国际单位制, 基本量, 电流, 国际单位制词头
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
电压将被证明是单位电荷所得的功。为此需要带单位的物理量、力、功和动能。
:::

**基本思路。** 从雪地里进来的人觉得房间暖和，从桑拿房出来的人觉得房间凉快。这样的判断是__定性__的。温度计对两人都显示 21 °C，这才是__定量__的：一个带标度的数，与由谁测量无关。物理学正是用这样的量来表述它的定律，例如__欧姆定律__ $U=R\cdot I$（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。本章中最重要的力学量是功：沿路径作用的力传递能量，而且只有力沿路径方向的分量才起作用。举起背包要克服重力做功，水平地背着它走则不做功（图 [2](#abb-2)）。

:::definition 定义 1.1 (物理量)
<span class="anker" id="satz-1-1"></span>

__物理量__是可测量的性质，是数值与单位的乘积：

<span class="anker" id="gl-1-1"></span>
$$\text{物理量}=\text{数值}\cdot\text{单位}. \tag{1.1}$$
:::

⁠**如何理解：**在 $U=9$ V 中，$U$ 是符号（斜体），9 是数值，V 是单位（正体）。方括号表示取单位：$[U]=\mathrm V$。数值取决于单位，而物理量本身不取决于单位：72 km/h 和 20 m/s 是同一个速度。

**单位。** __国际单位制__（SI）有七个__基本量__，它们不能相互表示：长度（米，m）、质量（千克，kg）、时间（秒，s）、电流（安培，A）、热力学温度（开尔文，K）、发光强度（坎德拉，cd）和物质的量（摩尔，mol）。它们的定义随着测量技术而不断发展。所有其他物理量的单位都是基本单位的幂的乘积。__电流__是运动的电荷，一安培表示每秒输运一库仑。功率是单位时间的能量。对本章来说，下面这些就够了：

| 物理量 | 单位 | 用基本单位表示 | 也可写作 |
|---|---|---|---|
| 力 $F$ | 牛顿，N | $\mathrm{kg\,m/s^2}$ | $\mathrm{J/m}$ |
| 能量、功 $W$ | 焦耳，J | $\mathrm{kg\,m^2/s^2}$ | $\mathrm{N\,m}=\mathrm{W\,s}$ |
| 功率 $P$ | 瓦特，W | $\mathrm{kg\,m^2/s^3}$ | $\mathrm{V\,A}$ |
| 电荷 $Q$ | 库仑，C | $\mathrm{A\,s}$ |  |
| 电压 $U$ | 伏特，V | $\mathrm{kg\,m^2/(s^3\,A)}$ | $\mathrm{J/C}$ |

__国际单位制词头__以十的幂缩放数值。倍数词头用大写，分数词头用小写，只有十、百、千由于历史原因例外。一个单位前面永远只有一个词头，词头与单位构成一个完整的符号。

| 词头 | 幂 | 文字 | 词头 | 幂 | 文字 |
|---|---|---|---|---|---|
| 阿托，a | $10^{-18}$ | 百亿亿分之一 | 艾可萨，E | $10^{18}$ | 百亿亿 |
| 飞母托，f | $10^{-15}$ | 千万亿分之一 | 拍它，P | $10^{15}$ | 千万亿 |
| 皮可，p | $10^{-12}$ | 万亿分之一 | 太拉，T | $10^{12}$ | 万亿 |
| 纳诺，n | $10^{-9}$ | 十亿分之一 | 吉咖，G | $10^{9}$ | 十亿 |
| 微，µ | $10^{-6}$ | 百万分之一 | 兆，M | $10^{6}$ | 百万 |
| 毫，m | $10^{-3}$ | 千分之一 | 千，k | $10^{3}$ | 千 |
| 厘，c | $10^{-2}$ | 百分之一 | 百，h | $10^{2}$ | 百 |
| 分，d | $10^{-1}$ | 十分之一 | 十，da | $10^{1}$ | 十 |

**单位的运算。**

<ol>

<li>

⁠**相加**只能在单位相同的量之间进行，词头要先统一：$2\,\mathrm{kV}+40\,\mathrm{V}=2.04\,\mathrm{kV}$，而不是 42 kV。和式中出现不同的单位，几乎总是意味着计算有误。

</li>

<li>

⁠**相乘**总是允许的。数值、单位和词头分别相乘，分式中的单位像数一样约分：$\frac{6\,\mathrm{N\,m}}{3\,\mathrm{m}}=2\,\mathrm{N}$，$0.5\,\mathrm{A}\cdot9\,\mathrm{V}=4.5\,\mathrm{W}$，$\mathrm{k\cdot M}=\mathrm G$，$\mu\text{}\cdot\mathrm M=1$。在参考模型中，$9\,\mathrm{V}/3\,\mathrm{mm}=3000\,\mathrm{V/m}=3\,\mathrm{kV/m}$。

</li>

<li>

⁠**换算**有时需要一个系数：$1\,\mathrm{Wh}=3600\,\mathrm{W\,s}$，$1\,\mathrm{km/h}=\frac{1}{3.6}\,\mathrm{m/s}$。由于词头和单位是一个符号，$1\,\mathrm{km^2}=(1000\,\mathrm{m})^2=10^6\,\mathrm{m^2}$，而不是 1000 m$^2$。

</li>

<li>

⁠**物理量决定单位。**能量按领域不同写成 W s、N m 或 J。但基本单位相同并不能证明物理量相同：赫兹（每秒振荡次数）和贝可勒尔（每秒衰变次数）都是 $1/\mathrm s$，而 N m 也是力矩（力乘以力臂）的单位。

</li>

</ol>

**力与功。** __力__使被固定的物体变形，或使可动的物体加速。__能量__是做功的本领。力和位移是__矢量__：具有大小和方向的量，上面加箭头书写，如 $\vec F$。__速度__是路程随时间的变化率，$v=\mathrm{d} s/\mathrm{d} t$；__加速度__是速度随时间的变化率，$a=\mathrm{d} v/\mathrm{d} t$。

:::definition 定义 1.2 (力与功)
<span class="anker" id="satz-1-2"></span>

质量为 $m$、加速度为 $a$ 的物体所受的力，以及相距 $r$ 的两个质量 $m$、$M$ 之间的力分别为

<span class="anker" id="gl-1-2"></span>
$$F=m\,a,\qquad F=\gamma\,\frac{m\,M}{r^2}. \tag{1.2}$$

力沿路径所做的__功__为

<span class="anker" id="gl-1-3"></span>
$$\Delta W=\vec F\cdot\Delta\vec s=F\,\Delta s\cos\alpha,\qquad W=\int_{P_1}^{P_2}\vec F\cdot\mathrm{d}\vec s. \tag{1.3}$$
:::

:::satz 定理 1.3 (恒定加速度与动能)
<span class="anker" id="satz-1-3"></span>

设 $t=0$ 时的初始值为 $s_0$ 和 $v_0$，则当 $a$ 恒定时

<span class="anker" id="gl-1-4"></span>
$$v(t)=v_0+a\,t,\qquad s(t)=s_0+v_0\,t+\tfrac12a\,t^2. \tag{1.4}$$

速度为 $v$ 的物体具有__动能__ $W_\mathrm{kin}=\frac12m\,v^2$。
:::

⁠**如何理解：**$[F]=\mathrm N$，在地球表面 100 g 的物体受力约 1 N。$\gamma=6.674\cdot10^{-11}\,\mathrm{N\,m^2/kg^2}$ 是__引力常量__。$\alpha$ 是力与路径微段之间的夹角。乘积 $\vec F\cdot\Delta\vec s$ 称为__标量积__，其结果是一个数。该积分称为__线积分__：把路径分成许多短的直线段，再把各段的贡献相加。$[W]=\mathrm J$，一焦耳能把 102 g 的物体举高一米。$\alpha<90^\circ$ 时力把能量传给物体，$\alpha>90^\circ$ 时力从物体取走能量。**适用条件：**式 [(1.4)](#gl-1-4) 只适用于恒定加速度，第 [9](was-die-spannung-mit-einer-ladung-macht.html#stufe-9) 阶段正好需要这种情况。

:::herleitung 动能
由式 [(1.4)](#gl-1-4)，取 $v_0=0$、$s_0=0$，得 $t=v/a$ 和 $s=\frac12a\,t^2=v^2/(2a)$。恒力 $F=m\,a$ 在这段路程上做的功为 $F\,s=m\,a\,v^2/(2a)=\frac12m\,v^2$。
:::

:::abbildung et1/k1wegarbeit 2
把 2 kg 的背包从 A 送到 B，水平移动 8 m，向上移动 6 m。走台阶时只有红色线段起作用，共 6 m。走斜坡时路程长 10 m，且 $\cos\alpha=0.6$。两条路径都得到 117.7 J。
:::

::::beispiel
背包受到__重力__ $F_\mathrm{G}=m\,g=19.62\,\mathrm{N}$。要匀速举起它，手必须施加同样大小的向上的力。走台阶时 $W=19.62\,\mathrm{N}\cdot6\,\mathrm{m}=117.7\,\mathrm{J}$，走斜坡时 $W=19.62\,\mathrm{N}\cdot10\,\mathrm{m}\cdot0.6=117.7\,\mathrm{J}$。手做功 $+117.7$ J，重力做功 $-117.7$ J。这些能量随后储存在高度中，成为__势能__：背包落下时，它转化为动能。场力做功与外力做功这一对关系将在第 [6](arbeit-im-feld.html#stufe-6) 阶段再次出现。
::::

⁠**极限情况：**$\alpha=0$ 时 $\Delta W=F\,\Delta s$，$\alpha=90^\circ$ 时 $\Delta W=0$。

:::frage 水平背着东西时手臂也会累。难道这时没有做功吗？
对背包没有做功：它既没有升高，也没有加速。肌肉仍然消耗能量，因为肌纤维在不断地重新收缩。这些能量在体内变成热，并没有到达背包。
:::

:::aufgabe 练习 1 ★ 单位与词头
<span class="anker" id="aufg-1"></span>

计算并用合适的单位给出结果： (a) $3\,\mathrm{kN}+450\,\mathrm{N}$， (b) $2\,\mathrm{mA}\cdot4\,\mathrm{ks}$， (c) $6\,\mu\text{C}/3\,\mathrm{ms}$， (d) 1 kWh 换算为焦耳， (e) 1.5 mm$^2$ 换算为 m$^2$， (f) 用基本单位表示单位 V/m。

:::loesung
(a) $3000\,\mathrm{N}+450\,\mathrm{N}=3.45\,\mathrm{kN}$。 (b) 毫与千相互抵消，$\mathrm{A\cdot s}=\mathrm C$：8 C。 (c) $\mu\text{}/\mathrm m=\mathrm m$（毫），且 $\mathrm{C/s}=\mathrm A$：2 mA。 (d) $1000\,\mathrm{W}\cdot3600\,\mathrm{s}=3.6\,\mathrm{MJ}$。 (e) $1\,\mathrm{mm^2}=(10^{-3}\,\mathrm{m})^2=10^{-6}\,\mathrm{m^2}$，所以结果为 $1.5\cdot10^{-6}\,\mathrm{m^2}$。 (f) $\frac{\mathrm V}{\mathrm m}=\frac{\mathrm{kg\,m^2}}{\mathrm{A\,s^3}\cdot\mathrm m}=\frac{\mathrm{kg\,m}}{\mathrm{A\,s^3}}$。
:::
:::
