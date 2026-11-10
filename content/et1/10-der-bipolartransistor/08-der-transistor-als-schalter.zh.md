---
title: 第 6 阶段：晶体管作为开关
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 双极型晶体管
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: 第 10 章：双极型晶体管
order: 1200800
summary: 开关应当要么完全断开，要么完全接通。本阶段说明为什么开关要用负载线的两端，由此构成反相器，并给出元件的极限。
tags: 反相器, 逻辑电平, 功率双曲线
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
开关应当要么完全断开，要么完全接通。本阶段说明为什么开关要用负载线的两端，由此构成反相器，并给出元件的极限。
:::

**基本思路。** 晶体管把功率 $P=U_\mathrm{CE}I_\mathrm{C}+U_\mathrm{BE}I_\mathrm{B}$ 转化为热，实际上只需考虑第一部分。在截止区 $I_\mathrm{C}=0$，在饱和区 $U_\mathrm{CE}$ 很小。这两点上乘积都很小。在负载线中点乘积最大。因此开关在 Z 和 S 之间跳变。这样两个输出电平的间距也最大，而且没有机械部件：晶体管开关极快，也没有磨损。放大器则工作在放大区。那里特性曲线近似线性，较高的功耗不如不失真的信号重要。

最小的逻辑电路是__反相器__：电路与图 [6](der-arbeitspunkt.html#abb-6) 相同，以 $U_\mathrm{out}=U_\mathrm{CE}$ 为输出。输入电压高时输出电压低，反之亦然。作为__逻辑电平__，低电压表示 0，高电压表示 1。

:::satz 定理 6.1 (反相器的特性曲线)
<span class="anker" id="satz-6-1"></span>

由线性模型得

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{out}= \begin{cases} U_\mathrm{CC} & U_\mathrm{in}<U_\mathrm{BE},\\[2pt] U_\mathrm{CC}-B\,R_\mathrm{C}\dfrac{U_\mathrm{in}-U_\mathrm{BE}}{R_\mathrm{B}} & U_\mathrm{BE}\le U_\mathrm{in}\le U_\mathrm{in,sat},\\[6pt] U_\mathrm{CE,sat} & U_\mathrm{in}>U_\mathrm{in,sat}, \end{cases} \tag{6.1}$$

<span class="anker" id="gl-6-2"></span>
$$U_\mathrm{in,sat}=\frac{(U_\mathrm{CC}-U_\mathrm{CE,sat})\,R_\mathrm{B}}{B\,R_\mathrm{C}}+U_\mathrm{BE}. \tag{6.2}$$
:::

⁠**如何理解：**中间一段是斜率为 $-B\,R_\mathrm{C}/R_\mathrm{B}$ 的直线。$U_\mathrm{in,sat}$ 是晶体管达到饱和时的输入电压。输入低于 $U_\mathrm{BE}$ 时视为 0，高于 $U_\mathrm{in,sat}$ 时视为 1。两者之间信号不明确。因此要把 $R_\mathrm{B}$ 选得足够小，使 $U_\mathrm{in,sat}$ 靠近 $U_\mathrm{BE}$。推导是把式 [(5.1)](der-arbeitspunkt.html#gl-5-1) 代入式 [(5.2)](der-arbeitspunkt.html#gl-5-2)，在 $U_\mathrm{CE}=U_\mathrm{CE,sat}$ 时解出 $U_\mathrm{in}$。**适用条件：**慢信号。极快的变化受基区电荷的限制。

:::abbildung et1/k10schalter 7
左：$R_\mathrm{B}=20$ k$\Omega$ 时的反相器特性曲线，拐点在 0.6 V 和 0.99 V。中：输入端 0 到 5 V 之间的方波信号（灰色）和 12 V 到 0.2 V 之间的反相输出（蓝色）。右：允许的工作点：位于功率双曲线、$I_\mathrm{C,max}$ 和 $U_\mathrm{CE,max}$ 以下。工作点 A 的功率为 12 mW，远在允许区域之内。
:::

::::beispiel
当 $R_\mathrm{B}=20$ k$\Omega$ 时，斜率为 $-30$，$U_\mathrm{in,sat}=0.99$ V。5 V 的逻辑输入给出 $I_\mathrm{B}=220$ µ A 和 $B\,I_\mathrm{B}=44$ mA，远大于 $R_\mathrm{C}$ 所允许的 3.93 mA。所以晶体管被过驱动了十一倍，即使是性能较差的个体也能可靠接通。晶体管上产生 $0.2\,\mathrm{V}\cdot3.93\,\mathrm{mA}+0.6\,\mathrm{V}\cdot0.22\,\mathrm{mA}=0.92$ mW，而它在 $R_\mathrm{C}$ 上开关的功率为 46 mW。在点 A，晶体管上的功率是 12 mW。
::::

⁠**极限情况：**当 $B\,R_\mathrm{C}/R_\mathrm{B}\to\infty$ 时，特性曲线变成在 $U_\mathrm{BE}$ 处的垂直跳变。

**工作极限。** 三个值限制了允许的工作点（图 [7](#abb-7) 右侧）。超过 $U_\mathrm{CE,max}$，CB 边界被击穿。超过 $I_\mathrm{C,max}$，基极和引线过载。超过__功率双曲线__ $I_\mathrm{C}=P_\mathrm{max}/U_\mathrm{CE}$，元件过热。在这些极限之外，寿命迅速缩短，或者元件立即损坏。对 T，双曲线在 40 V 处为 10 mA，在 4 V 处为 100 mA。

:::aufgabe 练习 7 ★★ 反相器
<span class="anker" id="aufg-7"></span>

用 T 构成的反相器工作在 $U_\mathrm{CC}=5$ V，$R_\mathrm{C}=1$ k$\Omega$，$R_\mathrm{B}=10$ k$\Omega$。(a) 求斜率和 $U_\mathrm{in,sat}$。(b) 输入为 3.3 V。求 $I_\mathrm{B}$、$I_\mathrm{C}$ 和晶体管上的功率，并与负载线上的最大值比较。(c) 当 $B=50$ 时，3.3 V 的输入还够吗？

:::loesung
(a) 斜率为 $-200\cdot1\,\text{k}\Omega/10\,\text{k}\Omega=-20$。$U_\mathrm{in,sat}=4.8\,\mathrm{V}/20+0.6\,\mathrm{V}=0.84$ V。

(b) $I_\mathrm{B}=2.7\,\mathrm{V}/10\,\text{k}\Omega=270$ µ A，$B\,I_\mathrm{B}=54$ mA，远大于 $I_\mathrm{C}=4.8\,\mathrm{V}/1\,\text{k}\Omega=4.8$ mA，因此处于饱和区。$P=0.2\,\mathrm{V}\cdot4.8\,\mathrm{mA}+0.6\,\mathrm{V}\cdot0.27\,\mathrm{mA}=1.12$ mW。在负载线上，$U_\mathrm{CE}I_\mathrm{C}=U_\mathrm{CE}(U_\mathrm{CC}-U_\mathrm{CE})/R_\mathrm{C}$。最大值出现在 $U_\mathrm{CC}/2$ 处，等于 $U_\mathrm{CC}^2/(4R_\mathrm{C})=6.25$ mW。

(c) $U_\mathrm{in,sat}=4.8\,\mathrm{V}/5+0.6\,\mathrm{V}=1.56$ V $<3.3$ V：够用。
:::
:::
