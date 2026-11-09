---
title: 第 9 阶段：电压对电荷的作用
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电荷、电场与电位
order: 1111100
summary: 本阶段在单个电子身上把电场、电位和电压联系起来：受多大的力，获得多少能量，速度能达到多快？
tags: 电子伏特
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
本阶段在单个电子身上把电场、电位和电压联系起来：受多大的力，获得多少能量，速度能达到多快？
:::

**基本思路。** 一个电子脱离极板 B，从静止出发。电场从 A 指向 B。由 $\vec F=Q\vec E$ 和 $Q=-e$，力的方向与电场相反，指向极板 A。力处处相同，所以加速度恒定，式 [(1.4)](groen-kraft-und-arbeit.html#gl-1-4) 成立。途中势能转化为动能。电子向高电位运动，但其能量 $Q\varphi$ 仍然下降，因为 $Q$ 为负。

:::satz 定理 9.1 (电场中的电荷)
<span class="anker" id="satz-9-1"></span>

在静电场中，动能与势能之和保持不变：

<span class="anker" id="gl-9-1"></span>
$$\tfrac12m\,v^2+Q\,\varphi=\text{常数}. \tag{9.1}$$

电荷从静止出发经过电压 $U$，在长度为 $d$ 的均匀电场中达到

<span class="anker" id="gl-9-2"></span>
$$v=\sqrt{\frac{2\,|Q\,U|}{m}},\qquad a=\frac{|Q|\,E}{m},\qquad t=\frac{2\,d}{v}. \tag{9.2}$$
:::

:::herleitung 能量定理与飞行时间
电场的功全部转化为动能：$\frac12mv_2^2-\frac12mv_1^2=W_{12}=Q(\varphi_1-\varphi_2)$。整理后得式 [(9.1)](#gl-9-1)。取 $v_1=0$，得 $|Q\,U|=\frac12m\,v^2$。加速度恒定时平均速度为 $v/2$，所以 $t=d/(v/2)$。
:::

⁠**如何理解：**$m$ 是以 kg 为单位的质量，$\varphi$ 是该位置的电位。$v$ 的表达式中不出现路程，能量只由电压决定。**适用条件与忽略项：**这些方程在真空中成立。在空气中，电子运动不足一微米就会与分子相撞。重力 $m_\mathrm{e}g=8.9\cdot10^{-30}$ N 忽略不计，它比电场力小 $5.4\cdot10^{13}$ 倍。此外还必须满足 $v\ll c$。这里 $v$ 只有光速 $c$ 的 0.6 %，动能的修正为 0.003 %。

:::abbildung et1/k1elektron 11
左：电子从极板 B 出发，逆着电场向极板 A 运动。右：从 $x=3$ mm 到 $x=0$，动能增大到 $1.44\cdot10^{-18}$ J，势能减小同样的量，参考点为 B。总和始终为零。
:::

::::beispiel
对于平行极板中的电子，

$$\begin{aligned} F&=e\,E=4.81\cdot10^{-16}\,\mathrm{N},\qquad a=\frac{F}{m_\mathrm{e}}=5.28\cdot10^{14}\,\mathrm{m/s^2},\qquad W=e\,U=1.44\cdot10^{-18}\,\mathrm{J},\\ v&=\sqrt{\frac{2\cdot1.44\cdot10^{-18}\,\mathrm{J}}{9.109\cdot10^{-31}\,\mathrm{kg}}}=1.78\cdot10^{6}\,\mathrm{m/s},\qquad t=\frac{2\cdot3\,\mathrm{mm}}{v}=3.37\,\mathrm{ns}. \end{aligned}$$

质子从 A 运动到 B。它获得相同的能量，但重 1836 倍：$v=4.15\cdot10^4$ m/s，慢 $\sqrt{1836}=42.9$ 倍，飞行时间为 144 ns。
::::

⁠**简而言之：**电荷在真空中经过一个电压时，动能的变化等于电荷乘以电压，与路径和距离无关。

⁠**极限情况：**$U\to0$ 时 $v\to0$。电压不变而极板间距加倍时，$E$ 和 $a$ 减半，但 $v$ 不变：电子的加速度变小，但加速时间变长，需要 6.74 ns。电压变为四倍时，速度变为两倍。

:::frage 电子真的逆着电场运动吗？电场不是推动电荷沿它的方向运动吗？
它推动**正**电荷沿它的方向运动，$\vec E$ 的方向就是这样规定的。每个电荷都会自发地向其势能 $Q\varphi$ 减小的地方运动。对电子来说，那就是较高的电位。
:::

:::zusatz 电子伏特
一个元电荷经过 1 V 获得的能量称为__电子伏特__：$1\,\mathrm{eV}=1.602\cdot10^{-19}$ J。例题中的电子获得 9 eV。
:::

:::aufgabe 练习 10 ★★★ 逆着电场的电子
<span class="anker" id="aufg-10"></span>

一个电子以 $v_0=1.0\cdot10^6$ m/s 离开参考模型的极板 A，飞向极板 B。

<ol class="al">

<li>

它能到达极板 B 吗？比较它的动能和所需的能量。

</li>

<li>

它在何处 $x$ 折返？分别用能量定理和式 [(1.4)](groen-kraft-und-arbeit.html#gl-1-4) 计算。

</li>

<li>

它何时回到极板 A，速度是多少？

</li>

<li>

要恰好到达 B，它需要多大的初速度？

</li>

</ol>

:::loesung
(a) $W_\mathrm{kin}=\frac12m_\mathrm{e}v_0^2=4.55\cdot10^{-19}$ J。到达 B 需要 $e\cdot9\,\mathrm{V}=1.44\cdot10^{-18}$ J。它到达不了 B。 (b) 能量定理：它一直运动，直到 $\Delta\varphi=W_\mathrm{kin}/e=2.84$ V 被耗尽。在 3 V/mm 下，$x=0.948$ mm。用式 [(1.4)](groen-kraft-und-arbeit.html#gl-1-4)：减速度 $a=5.28\cdot10^{14}\,\mathrm{m/s^2}$，在 $t=v_0/a$ 时折返，所以 $x=v_0^2/(2a)=0.948$ mm。

(c) 往返：$t=2v_0/a=3.79$ ns。电位又回到原值，所以由式 [(9.1)](#gl-9-1)，$v=v_0=1.0\cdot10^6$ m/s，方向相反。 (d) 恰好是例题中的能量：$v_0=1.78\cdot10^6$ m/s。
:::
:::
