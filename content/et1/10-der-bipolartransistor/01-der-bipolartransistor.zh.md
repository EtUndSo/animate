---
title: 概览: 双极型晶体管
kurz: 概览
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 双极型晶体管
order: 1200100
summary: 小电压如何控制流过 截止二极管的大电流
tags: 双极型晶体管
lang: zh
---

## 本章内容

麦克风输出的是毫伏，扬声器需要的是伏特。计算机输出的是毫安，电动机需要的是安培。两者之间有一种元件，用小信号控制大电流。它的经典代表是__双极型晶体管__，一种由三层构成、有三个接线端的半导体元件。能量来自电源电压，信号只负责调节大小。另一种重要类型 MOSFET 主导着数字电子技术，不在本章讨论范围之内。问题是：**0.6 V 的电压如何能控制流过截止二极管的电流？**


**所有结论背后的同一个原理。** 晶体管有两个边界，承担两项任务。基极-发射极边界负责控制：那里的电压按指数规律决定有多少电子出发。集电极-基极边界只负责收集：到达的电子都被抽走，那里的电压几乎不起作用。

| 结论 | 来源 |
|---|---|
| $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$，两个自由电压 | 三个接线端，节点定律和网孔定律（第 [1](drei-schichten-zwei-spannungen.html#stufe-1) 阶段） |
| $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$，$I_\mathrm{B}=I_\mathrm{C}/B$ | 出发、穿过薄基区、被抽走（第 [2](warum-strom-durch-die-gesperrte-diode-fliet.html#stufe-2) 阶段） |
| 多条特性曲线 | 同一曲面的截面：沿 $U_\mathrm{BE}$ 陡，沿 $U_\mathrm{CE}$ 平（第 [3](eine-flache-viele-kennlinien.html#stufe-3) 阶段） |
| 三个工作区 | 两个边界中哪一个导通（第 [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4) 阶段） |
| 工作点 | 晶体管方程和网孔方程必须同时成立（第 [5](der-arbeitspunkt.html#stufe-5) 阶段） |
| 开关、反相器 | 负载线的两端：晶体管上的功率很小（第 [6](der-transistor-als-schalter.html#stufe-6) 阶段） |
| 稳定的工作点 | 电流增大抬高发射极，使 $U_\mathrm{BE}$ 回落（第 [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7) 阶段） |
| 电流镜、稳压器 | $U_\mathrm{BE}$ 相同则电流相同，而且 $U_\mathrm{BE}$ 几乎不变（第 [8](zwei-schaltungen-die-nutzen.html#stufe-8) 阶段） |
| $S=I_\mathrm{C}/U_T$ | 指数函数的斜率等于函数值除以标度 $U_T$（第 [9](tangente-statt-kurve.html#stufe-9) 阶段） |
| $\vert A\vert =U_{R_\mathrm{C}}/U_T$ | 电流变化量 $S\,u_\mathrm{in}$ 乘以 $R_\mathrm{C}$（第 [10](drei-grundschaltungen.html#stufe-10) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**晶体管 T：**硅材料的 npn 小信号晶体管，$B=200$，$I_\mathrm{S}=1.9\cdot10^{-13}$ A（反向饱和电流，[第 9 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)），$U_T=26$ mV（300 K 时的热电压，由 25.85 mV 取整）。手工计算时，晶体管导通时近似取 $U_\mathrm{BE}=0.6$ V，完全接通时近似取 $U_\mathrm{CE,sat}=0.2$ V。极限参数：$U_\mathrm{CE,max}=40$ V，$I_\mathrm{C,max}=100$ mA，$P_\mathrm{max}=400$ mW。

</li>

<li>

⁠**电路：**电源 $U_\mathrm{CC}=12$ V，集电极电阻 $R_\mathrm{C}=3$ k$\Omega$，基极电阻 $R_\mathrm{B}=440$ k$\Omega$，输入电压 $U_\mathrm{in}=5$ V。由此得到工作点 $I_\mathrm{B}=10$ µ A，$I_\mathrm{C}=2$ mA，$U_\mathrm{CE}=6$ V。

</li>

<li>

⁠**负反馈版本：**基极分压器 $R_1=31$ k$\Omega$，$R_2=9$ k$\Omega$，发射极电阻 $R_\mathrm{E}=1$ k$\Omega$（第 [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7) 阶段）。

</li>

</ul>

脚本 `rechnung_kap10.py` 可复算所有数值。
:::
