---
title: 概览: 相关函数
kurz: 概览
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 相关函数
order: 3260100
summary: 两个信号有多相似？ 能量又如何分布在各个频率上？
tags: 
lang: zh
---

## 本章内容

雷达发出一个脉冲，并在接收信号中寻找它的回波。手机在噪声中寻找一个已知的同步序列。二者提出的是同一个问题：**一个信号与另一个信号有多相似？在什么时移下最相似？**答案由相关函数给出。此外，相关函数的傅里叶变换还表明信号的能量如何分布在各个频率上。


**所有结论背后的同一个原理。** 相关就是与反转信号的卷积。因此，卷积的所有工具都适用：

| 结论 | 来源 |
|---|---|
| 相关系数 | 两个归一化信号之差的能量（第 [2](ahnlichkeit-messen-der-korrelationskoeffizient.html#stufe-2) 阶段） |
| 相关积 | 与反转并共轭后的信号做卷积（第 [3](korrelationsfunktion-und-korrelationsprodukt.html#stufe-3) 阶段） |
| 自相关函数为偶函数，最大值在 0 处 | 反转；并且信号与自身最相似（第 [3](korrelationsfunktion-und-korrelationsprodukt.html#stufe-3) 阶段） |
| 能量谱密度、帕塞瓦尔定理 | 反转与共轭变为 $S^*$，卷积变为乘积（第 [4](energiedichtespektrum.html#stufe-4) 阶段） |
| 维纳–李关系 | 卷积的结合律（第 [5](korrelation-und-lti-systeme.html#stufe-5) 阶段） |
| 离散时间、周期、DFT | 同样的计算，只是改用求和（第 [7](zeitdiskrete-und-periodische-korrelation.html#stufe-7) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
矩形脉冲 $\operatorname{rect}(t)$、三角脉冲 $\Lambda(t)$、指数脉冲 $\varepsilon(t)\mathrm{e}^{-t}$（$RC=1$ s 的 RC 电路的冲激响应）以及序列 $(1,2,1)$。脚本 `rechnung_kap6.py` 可复算这些数值。
:::
