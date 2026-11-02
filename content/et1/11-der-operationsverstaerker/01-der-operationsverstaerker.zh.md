---
title: 概览: 运算放大器
kurz: 概览
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 运算放大器
order: 1210100
summary: 一个巨大而不精确的倍数，如何变成 行为只由电阻决定的器件
tags: 运算放大器, 开环增益, 负反馈, 噪声, 比较器
lang: zh
---

## 本章内容

__运算放大器__，简称运放，是由几十个晶体管构成的集成放大器。它把两个输入端之间的电压放大约 100000 倍。这个倍数称为__开环增益__。它在不同器件之间可相差四倍，并随温度变化。尽管如此，人们仍用这种器件搭建只感受到这种波动的 0.01 % 的放大器，以及加法器和积分器。问题是：**一个巨大而不精确的倍数，如何变成行为只由电阻决定的器件？**答案是__负反馈__：把输出电压的一部分送回输入端，使它抵消自身的起因。


**所有结论背后的同一个原理。** 负反馈运放的输出不是用 $A$ 算出来的，而是环路静止时的状态。为此 $A$ 只需足够大，其精确值无关紧要。

| 结论 | 来源 |
|---|---|
| __噪声__（随机的干扰电压）、信噪比 | 单个电荷随机运动，放大对信号和干扰的抬升相同（第 [1](rauschen.html#stufe-1) 阶段） |
| $U_\mathrm{A}=S\,R_\mathrm{C}\,U_\mathrm{D}$，共模无影响 | 总电流固定，只有其分配能变化（第 [2](der-differenzverstarker.html#stufe-2) 阶段） |
| __比较器__（电压比较电路） | 没有反馈时，几乎没有哪个输入电压落在窗口内（第 [3](der-opv-ohne-ruckfuhrung.html#stufe-3) 阶段） |
| $U_\mathrm{D}=U_\mathrm{A}/A$，$G\approx1/\beta$ | 输出不断变化，直到环路静止（第 [4](gegenkopplung.html#stufe-4) 阶段） |
| $G=-R_2/R_1$，虚地 | 规则加负输入端的节点定律（第 [5](die-regel-und-die-virtuelle-masse.html#stufe-5) 阶段） |
| 加法器、减法器、级联 | 电流相加，作用叠加（第 [6](mehrere-eingange-mehrere-stufen.html#stufe-6) 阶段） |
| 积分器、对数放大器 | 一个元件决定电流，另一个决定电压（第 [7](rechnen-mit-kondensator-und-diode.html#stufe-7) 阶段） |
| 电流-电压转换器、负电阻 | 输出提供规则所要求的任何电流（第 [8](strom-als-signal.html#stufe-8) 阶段） |
| 施密特触发器 | 符号相反：结果加强了原因（第 [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9) 阶段） |
| 规则的界限 | 一切使 $A\beta$ 减小或使 $U_\mathrm{D}$ 偏移的因素（第 [10](wo-die-regeln-enden.html#stufe-10) 阶段） |

**如何使用本章。**每个阶段都是一篇简短的文章，包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。完成一个阶段后再进入下一个。

:::merke 本章的参考模型
<ul>

<li>

⁠**运放 V：**开环增益 $A=100000$（不同器件在 50000 到 200000 之间），输入电阻 $r_\mathrm{e}=1$ M$\Omega$，输出电阻 $r_\mathrm{a}=75\,\Omega$。电源 $\pm12$ V，输出可达 $\pm11$ V，最大 20 mA。用于第 [10](wo-die-regeln-enden.html#stufe-10) 阶段：特征频率 $f_\mathrm{T}=1$ MHz（此时 $A$ 降到 1），失调 $U_\mathrm{off}=1$ mV（输入端的残余差值），输入偏置电流 $I_\mathrm{B}=50$ nA（输入晶体管的基极电流），共模抑制 90 dB（对共同干扰的衰减）。

</li>

<li>

⁠**外部电路：**$R_1=10$ k$\Omega$，$R_2=40$ k$\Omega$，$U_\mathrm{E}=1$ V。

</li>

<li>

⁠**差分级：**[第 10 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)的晶体管 T（$B=200$，$U_T=26$ mV），$I_0=2$ mA，$R_\mathrm{C}=3$ k$\Omega$。

</li>

<li>

⁠**传感器：**有效值 1 mV，内阻 10 k$\Omega$，带宽（可通过的频率范围）20 kHz，温度 300 K。

</li>

</ul>

脚本 `rechnung_kap11.py` 可复算所有数值。
:::
