---
title: 概览: 功率、匹配与效率
kurz: 概览
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 功率、匹配与效率
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: 第 7 章：功率、匹配与效率
order: 1170100
summary: 为什么在功率最大时有一半能量留在电源中
tags: 内阻, 负载, 功率
lang: zh
---

## 本章内容

一块 9 V 电池有 2 $\Omega$ 的__内阻__，即电流在电源内部必须克服的电阻。它向__负载__（所连接的设备）供电。负载应为多大，才能使到达负载的__功率__（单位时间的能量）尽可能大？答案是 2 $\Omega$，但这有代价：此时一半的能量以热的形式留在电池中。本章要回答的问题是：**功率从哪里来，到哪里去，为什么最大值恰好出现在利用率为 50 % 的地方？**

**所有结论背后的同一个原理。** 任何功率都是两个答案的乘积：一库仑电荷在此处释放多少能量，每秒有多少库仑经过？

| 结论 | 来源 |
|---|---|
| $p=u\,i$ | 单位电荷的能量乘以单位时间的电荷（第 [1](energie-je-ladung-mal-ladung-je-zeit.html#stufe-1) 阶段） |
| $P=R\,I^2=U^2/R$，额定功率 | 碰撞把一切都交给晶格；电流加倍意味着库仑数加倍，每库仑释放的能量也加倍（第 [2](warum-der-widerstand-warm-wird.html#stufe-2) 阶段） |
| $P=\frac12\hat u^2/R$ | $u$ 和 $i$ 同时变号，$\cos^2$ 的平均值为 $\frac12$（第 [3](mittlere-leistung-bei-sinusspannung.html#stufe-3) 阶段） |
| 高压线路 | 同样的功率只需较少的库仑，而每库仑损失的能量也较少（第 [4](leitungsverluste.html#stufe-4) 阶段） |
| $\eta=U_\mathrm{L}/U_\mathrm{q}$ | 每库仑的能量中到达负载的比例（第 [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5) 阶段） |
| $R_\mathrm{L}=R_\mathrm{i}$ | 电流和负载电压线性地此消彼长，两者的乘积在中点最大（第 [6](leistungsanpassung.html#stufe-6) 阶段） |
| 最大值处 $\eta=50\,\%$ | 中点意味着：每库仑的能量有一半留在内部（第 [7](warum-50-und-welches-ziel-gilt.html#stufe-7) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**电池：**[第 5 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)中的 9 V 方形电池，源电压（化学反应提供的电压）$U_\mathrm{q}=9$ V，内阻 $R_\mathrm{i}=2\,\Omega$。[第 5 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)中单个电源的内阻记作 $R_\mathrm{q}$。短路电流为 $I_\mathrm{SC}=4.5$ A。

</li>

<li>

⁠**负载：**电阻 $R_\mathrm{L}$，取 16、8、2 或 0.5 $\Omega$。

</li>

<li>

⁠**其他：**$R=5\,\Omega$ 接在峰值为 10 V 的正弦电压上（第 [3](mittlere-leistung-bei-sinusspannung.html#stufe-3) 阶段），一条 $R_\text{线路}=1\,\Omega$ 的线路连接 40 kW 的负载（第 [4](leitungsverluste.html#stufe-4) 阶段）。

</li>

</ul>

:::
