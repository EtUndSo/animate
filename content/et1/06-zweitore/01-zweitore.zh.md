---
title: 概览: 二端口网络
kurz: 概览
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 二端口网络
order: 1160100
summary: 为什么四个数就能代替整个网络， 以及每种参数形式都只是另一种选择
tags: 二端口网络, 端口
lang: zh
---

## 本章内容

在电源和负载之间常常还有另一个网络：一根电缆、一个滤波器、一个衰减器或一个放大器。它有输入侧和输出侧，从外部看，重要的只是它对电压和电流做了什么。具有两对这样的接线端的网络称为__二端口网络__，每对接线端称为一个__端口__。[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)用两个数（等效电压和内阻）代替了一对接线端上的网络。本章的问题是：**两对接线端需要多少个数，又如何从外部测量它们？**


**所有结论背后的同一个原理。** 在四个端口量中选两个作为原因，另外两个就是结果。这种选择不改变二端口网络本身，只改变计算，而每个结论都由它得出。

| 结论 | 来源 |
|---|---|
| 四个端口量而不是六个 | 每对接线端上的二端元件从一个接线端送出的电荷，都在另一个接线端收回（第 [1](vom-vierpol-zum-zweitor.html#stufe-1) 阶段） |
| 四个参数 | 叠加：两个原因乘两个结果（第 [2](vier-groen-zwei-gleichungen-vier-zahlen.html#stufe-2) 阶段） |
| 由开路试验得 Z 参数 | 原因是电流，开路的端口使一个电流为零（第 [3](impedanzform-und-leerlaufversuch.html#stufe-3) 阶段） |
| 输入电阻取决于负载 | 第二个原因 $I_2$ 经 $Z_{12}$ 反过来作用于输入端（第 [4](das-zweitor-im-betrieb.html#stufe-4) 阶段） |
| 由短路试验得 Y 参数 | 原因是电压，一根导线使一个电压为零（第 [5](admittanzform-und-kurzschlussversuch.html#stufe-5) 阶段） |
| $\mathbf Y=\mathbf Z^{-1}$，T 与 $\pi$ | 同样的两个方程，对另外两个量求解（第 [6](umrechnen-t-und.html#stufe-6) 阶段） |
| 混合形式 | 原因混合，适合电流输入、电流源输出的元件（第 [7](hybridform.html#stufe-7) 阶段） |
| 链式形式，矩阵乘积 | 一级的原因是下一级的结果（第 [8](kettenform.html#stufe-8) 阶段） |
| Z、Y、H 相加 | 两部分共有的量属于原因，相加的量属于结果（第 [9](zusammenschaltung.html#stufe-9) 阶段） |
| 互易、无反向作用、有源 | 四个数及其符号之间的关系（第 [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10) 阶段） |

**如何使用本章。**每个阶段都是一篇简短的文章，包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。完成一个阶段后再进入下一个。

:::merke 本章的参考模型
<ul>

<li>

⁠**T 形网络：**一个 T 形网络（[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)），输入端是串联电阻 $R_\mathrm{a}=15\,\Omega$，通向贯通的下方导线的是并联电阻 $R_\mathrm{b}=20\,\Omega$，输出端是串联电阻 $R_\mathrm{c}=20\,\Omega$。

</li>

<li>

⁠**工作状态：**端口 1 接实际电压源，$U_\mathrm{q}=9$ V，$R_\mathrm{q}=5\,\Omega$；端口 2 接负载 $R_\mathrm{L}=60\,\Omega$。

</li>

<li>

⁠**放大器：**一个模型，输入端 2 k$\Omega$，电流增益 100，输出端 20 k$\Omega$，负载 5 k$\Omega$，见第 [7](hybridform.html#stufe-7) 阶段。

</li>

<li>

所有量都是直流量。脚本 `rechnung_kap6.py` 可复算所有数值。

</li>

</ul>
:::
