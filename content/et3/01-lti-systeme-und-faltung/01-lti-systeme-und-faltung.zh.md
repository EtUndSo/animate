---
title: 概览: 信号、LTI 系统与卷积
kurz: 概览
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / LTI 系统与卷积
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: 第 1 章：LTI 系统与卷积
order: 3210100
summary: 为什么对单个冲激的响应 能够描述整个系统
tags: 
lang: zh
---

## 本章内容

系统接收一个信号，输出另一个信号：RC 电路使电压变得平滑，音箱箱体给声音染上音色，测量放大器对信号进行延迟和放大。本章要回答的问题是：**要对任意输入信号算出系统的输出，需要知道系统的哪些信息？**

对于线性时不变（LTI）系统这一大类系统，答案出奇地简短：只需知道系统对单个无限短冲激的响应。把这一个响应变成其他所有响应的工具，就是卷积。


**所有结论背后的同一个原理。** 下表把本章的每一项结论都归结到“分解、让一个基本单元通过系统、再合成”这一原理上。

| 结论 | 来源 |
|---|---|
| 卷积积分 | 叠加冲激，叠加平移后的冲激响应（第 [4](das-faltungsintegral.html#stufe-4) 阶段） |
| 计算时的反转 | $h(t-\tau)$ 是对 $t-\tau$ 秒之前到达的冲激的响应（第 [5](die-faltung-ausrechnen.html#stufe-5) 阶段） |
| $\delta$ 是单位元 | 由冲激组成的信号，通过一个使每个冲激都保持不变的系统（第 [6](rechenregeln-der-faltung.html#stufe-6) 阶段） |
| 交换律、结合律、分配律 | 互换角色、系统级联、系统并联（第 [6](rechenregeln-der-faltung.html#stufe-6) 阶段） |
| 筛选性质、狄拉克冲激的尺度变换 | $\delta$ 仅通过其面积来定义（第 [7](der-dirac-impuls.html#stufe-7) 阶段） |
| 阶跃响应 $=$ 冲激响应的积分 | 阶跃是到 $t$ 为止所有冲激之和（第 [8](integrieren-und-differenzieren.html#stufe-8) 阶段） |
| 因果性、稳定性 | 对 $h(t)$ 的条件：冲激到来之前为零，$\vert h\vert $ 的面积有限（第 [9](kausal-und-stabil.html#stufe-9) 阶段） |
| 没有系统的卷积 | 同样的叠加，例如两个骰子的点数之和（第 [10](faltung-ganz-ohne-system.html#stufe-10) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**RC 低通滤波器**，$T=RC=1$ s（例如 $R=1\,\mathrm{M}\Omega$，$C=1\,\mu\text{F}$）。时间以 s 为单位，电压以 V 为单位，因此所有计算都是无量纲的。

</li>

<li>

⁠**矩形脉冲**：高度 $a=1$ V，持续时间 $T_0=1$ s，从 $t=0$ 开始。

</li>

</ul>

脚本 `rechnung_kap1.py` 可复算这些数值和曲线。
:::
