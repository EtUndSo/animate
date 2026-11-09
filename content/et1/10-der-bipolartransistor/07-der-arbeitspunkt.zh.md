---
title: 第 5 阶段：工作点
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 双极型晶体管
order: 1200700
summary: 事先并不知道晶体管处于哪个工作区。本阶段通过假设和检验来确定工作点，并把它画成交点。
tags: 负载线, 电源电压
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
事先并不知道晶体管处于哪个工作区。本阶段通过假设和检验来确定工作点，并把它画成交点。
:::

**基本思路。** 晶体管提供特性曲线，电路提供网孔方程。两者必须同时成立。结果就是工作点（OP），如同[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)中特性曲线与直线的交点。由于每个工作区有不同的等效电路，所以先假设一个工作区，进行线性计算，再加以检验。与条件 [(4.1)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-1) 到 [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3) 的矛盾会暴露错误的假设。

:::abbildung et1/k10arbeit 6
左：参考模型的电路。右：线性化的输出特性曲线和从 $(0;\,4\,\mathrm{mA})$ 到 $(12\,\mathrm{V};\,0)$ 的负载线。它与 $I_\mathrm{B}=10$ µ A 的直线相交于工作点 A。S 是饱和区中的点，Z 是截止区中的点。
:::

:::satz 定理 5.1 (带基极电阻和集电极电阻的电路的工作点)
<span class="anker" id="satz-5-1"></span>

输入网孔为 $U_\mathrm{in}=R_\mathrm{B}I_\mathrm{B}+U_\mathrm{BE}$，输出网孔就是__负载线__ $U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}$。当 $U_\mathrm{in}\le U_\mathrm{BE,on}$ 时，晶体管截止，且 $U_\mathrm{BE}=U_\mathrm{in}$。当 $U_\mathrm{in}>U_\mathrm{BE,on}$ 时，在两个导通的工作区都有

<span class="anker" id="gl-5-1"></span>
$$I_\mathrm{B}=\frac{U_\mathrm{in}-U_\mathrm{BE,on}}{R_\mathrm{B}}. \tag{5.1}$$

假设处于放大区，则

<span class="anker" id="gl-5-2"></span>
$$I_\mathrm{C}=B\,I_\mathrm{B},\qquad U_\mathrm{CE}=U_\mathrm{CC}-B\,I_\mathrm{B}R_\mathrm{C}. \tag{5.2}$$

如果结果满足 $U_\mathrm{CE}\ge U_\mathrm{CE,sat}$，假设就是正确的。否则处于饱和区，有

<span class="anker" id="gl-5-3"></span>
$$U_\mathrm{CE}=U_\mathrm{CE,sat},\qquad I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,sat}}{R_\mathrm{C}}<B\,I_\mathrm{B}. \tag{5.3}$$
:::

⁠**如何理解：**$U_\mathrm{CC}$ 是__电源电压__，$U_\mathrm{in}$ 是对地的输入电压。$R_\mathrm{B}$ 设定基极电流，$R_\mathrm{C}$ 把集电极电流转换成电压。**适用条件：**发射极接地，采用第 [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4) 阶段的线性模型。式 [(5.1)](#gl-5-1) 在两个导通的工作区都成立，因为那里 B 和 E 之间是同一个 0.6 V 电压源。

::::beispiel
参考模型：$I_\mathrm{B}=(5\,\mathrm{V}-0.6\,\mathrm{V})/440\,\text{k}\Omega=10$ µ A，$I_\mathrm{C}=2$ mA，$U_\mathrm{CE}=12\,\mathrm{V}-6\,\mathrm{V}=6$ V。这大于 0.2 V，所以处于放大区（点 A）。第一次假设错了也无妨：假设饱和将得到 $I_\mathrm{C}=3.93$ mA，但 $B\,I_\mathrm{B}=2$ mA 更小，与式 [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3) 矛盾。当 $U_\mathrm{in}=12$ V 时，$I_\mathrm{B}=25.9$ µ A。若假设在放大区，将得到 $U_\mathrm{CE}=-3.5$ V，出现矛盾。在饱和区，$I_\mathrm{C}=3.93$ mA，$B\,I_\mathrm{B}=5.18$ mA（点 S）。
::::

⁠**极限情况：**$R_\mathrm{C}=0$ 给出 $U_\mathrm{CE}=U_\mathrm{CC}$，输出固定不动。$U_\mathrm{in}<0.6$ V 给出 $I_\mathrm{C}=0$，$U_\mathrm{CE}=12$ V（点 Z）。

**放大区的中点。** 在放大区，$U_\mathrm{CE}$ 介于 0.2 V 和 $U_\mathrm{CC}$ 之间。为了让信号在两侧有同样的余地，把工作点放在中间。取 $\Delta U=U_\mathrm{CC}-U_\mathrm{CE,sat}=11.8$ V，则

<span class="anker" id="gl-5-4"></span>
$$U_\mathrm{CE,OP}=U_\mathrm{CE,sat}+\frac{\Delta U}{2}=6.1\,\mathrm{V},\qquad I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,OP}}{R_\mathrm{C}}=1.97\,\mathrm{mA}. \tag{5.4}$$

由此得 $R_\mathrm{B}=(U_\mathrm{in}-U_\mathrm{BE})\,B/I_\mathrm{C}=447$ k$\Omega$。参考模型的 440 k$\Omega$ 几乎就在这里。

**带发射极电阻。** 如果基极直接接 $U_\mathrm{in}$，发射极经 $R_\mathrm{E}$ 接地，输入网孔为 $U_\mathrm{in}=U_\mathrm{BE,on}+R_\mathrm{E}I_\mathrm{E}$。当 $U_\mathrm{in}>0.6$ V 时，晶体管不截止，并有

<span class="anker" id="gl-5-5"></span>
$$I_\mathrm{E}=\frac{U_\mathrm{in}-U_\mathrm{BE,on}}{R_\mathrm{E}},\quad I_\mathrm{B}=\frac{I_\mathrm{E}}{1+B},\quad I_\mathrm{C}=B\,I_\mathrm{B},\quad U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}-R_\mathrm{E}I_\mathrm{E}. \tag{5.5}$$

取 $U_\mathrm{in}=2.6$ V 和 $R_\mathrm{E}=1$ k$\Omega$，得 $I_\mathrm{E}=2$ mA，$I_\mathrm{C}=1.99$ mA，$U_\mathrm{CE}=4.03$ V。这里 $B$ 到最后一步才起作用，而且几乎不改变什么。第 [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7) 阶段将利用这一点。

:::aufgabe 练习 5 ★★ 计算工作点
<span class="anker" id="aufg-5"></span>

已知 T，$U_\mathrm{CC}=10$ V，$R_\mathrm{C}=2$ k$\Omega$，$R_\mathrm{B}=220$ k$\Omega$。 (a) 求 $U_\mathrm{in}=3$ V 时的工作点。(b) 求 $U_\mathrm{in}=8$ V 时的工作点。(c) 在 $U_\mathrm{in}=3$ V 时，多大的 $R_\mathrm{B}$ 能把工作点放在放大区的中点？

:::loesung
(a) $I_\mathrm{B}=2.4\,\mathrm{V}/220\,\text{k}\Omega=10.9$ µ A，$I_\mathrm{C}=2.18$ mA，$U_\mathrm{CE}=10\,\mathrm{V}-4.36\,\mathrm{V}=5.64$ V：放大区。

(b) $I_\mathrm{B}=33.6$ µ A，$B\,I_\mathrm{B}=6.73$ mA。若假设在放大区，将得到 $U_\mathrm{CE}=-3.45$ V，出现矛盾。因此是饱和区：$U_\mathrm{CE}=0.2$ V，$I_\mathrm{C}=9.8\,\mathrm{V}/2\,\text{k}\Omega=4.9$ mA $<6.73$ mA。

(c) $U_\mathrm{CE,OP}=0.2\,\mathrm{V}+4.9\,\mathrm{V}=5.1$ V，$I_\mathrm{C}=4.9\,\mathrm{V}/2\,\text{k}\Omega=2.45$ mA，$I_\mathrm{B}=12.25$ µ A，$R_\mathrm{B}=2.4\,\mathrm{V}/12.25\,\mu\text{A}=196$ k$\Omega$。
:::
:::

:::aufgabe 练习 6 ★★ 发射极电阻
<span class="anker" id="aufg-6"></span>

T 的基极直接接 $U_\mathrm{in}=1.6$ V，另有 $U_\mathrm{CC}=12$ V，$R_\mathrm{C}=2$ k$\Omega$，$R_\mathrm{E}=500\,\Omega$。(a) 求 $I_\mathrm{E}$、$I_\mathrm{B}$、$I_\mathrm{C}$ 和 $U_\mathrm{CE}$。(b) 如果 $B$ 降到 100，会有什么变化？

:::loesung
(a) $I_\mathrm{E}=1\,\mathrm{V}/500\,\Omega=2$ mA，$I_\mathrm{B}=2\,\mathrm{mA}/201=9.95$ µ A，$I_\mathrm{C}=1.99$ mA，$U_\mathrm{CE}=12\,\mathrm{V}-3.98\,\mathrm{V}-1\,\mathrm{V}=7.02$ V。

(b) $I_\mathrm{E}$ 仍为 2 mA，因为它只取决于 $U_\mathrm{in}$ 和 $R_\mathrm{E}$。$I_\mathrm{B}$ 变为 19.8 µ A，$I_\mathrm{C}$ 变为 1.98 mA，$U_\mathrm{CE}$ 变为 7.04 V。$B$ 减半，集电极电流却只减少 0.5 %。
:::
:::
