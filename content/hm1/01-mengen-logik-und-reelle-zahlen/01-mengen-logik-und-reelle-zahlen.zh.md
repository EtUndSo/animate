---
title: 概览: 集合、逻辑与实数
kurz: 概览
pfad: 电气工程 / 第 1 学期 / HöMa1 – 高等数学 1 / 集合、逻辑与实数
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: 第 1 章：集合、逻辑与实数
order: 1210100
summary: 关于数必须预设什么 以及为什么 2 的平方根不是分数
tags: 集合, 命题, 公理, 域, 序, 完备性, 数学归纳法, 绝对值
lang: zh
---

## 本章内容

学校里讲过 $(-1)\cdot(-1)=1$ 或“不能除以零”这样的规则。它们为什么成立？用习惯作理由走不了多远：在复数中（[第 2 章](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)），“平方不为负”这条规则不再成立；而所有极限（第 4 章）都依赖于数的一个性质，这个性质在学校里从未提到。只看一个数就能发现它：边长为 1 的正方形，对角线长为 $\sqrt2$，而没有任何分数等于这个值。本章要回答的问题是：**关于数究竟必须预设什么，才能证明所有运算法则？实数与分数的区别又在哪里？**

答案需要两件工具和一份简短的假设清单。__集合__把对象汇集在一起，__命题__是一个或真或假的语句。__公理__是一条被规定下来、不加证明的基本假设。三组公理就够了：__域__是一个集合，其中的加法和乘法遵循熟悉的规则。__序__规定哪些数是正数。__完备性__是说数轴上没有缺口。此外还有__数学归纳法__，即证明关于全体自然数的命题的方法，以及__绝对值__，即一个数到零的距离。

**所有结论背后的同一个原理。** 没有什么是靠相信得来的：每条规则都处在一条推理链的末端，而这条链始于一条公理。

| 结论 | 来源 |
|---|---|
| 德摩根律、逆否律 | 有限种情形：真值表（第 [1](mengen-und-aussagen.html#stufe-1) 阶段） |
| “对所有”的否定 | “对所有”是一个长长的“且”，德摩根律（第 [2](quantoren-und-indirekter-beweis.html#stufe-2) 阶段） |
| $(-1)\cdot(-1)=1$、分数运算 | 域公理，尤其是分配律（第 [3](korperaxiome.html#stufe-3) 阶段） |
| $z<0$ 时不等式反向 | 序公理（第 [4](anordnungsaxiome.html#stufe-4) 阶段） |
| 求和公式、幂运算律 | 自然数的构造：归纳法（第 [5](vollstandige-induktion-summe-und-produkt.html#stufe-5) 阶段） |
| 阿基米德定理、$\sqrt2$ 存在 | 完备性（第 [6](das-vollstandigkeitsaxiom.html#stufe-6) 和第 [7](intervallschachtelung-und-wurzeln.html#stufe-7) 阶段） |
| 三角不等式 | 在数轴上的位置（第 [8](abstand-und-betrag.html#stufe-8) 阶段） |
| 杨氏不等式、柯西-施瓦茨不等式 | 平方不为负（第 [9](elementare-ungleichungen.html#stufe-9) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**集合：**$G=\{1,2,\dots,12\}$，其中有 $A=\{1,2,3,4,6,12\}$（12 的因数）和 $B=\{2,3,5,7,11\}$（素数）。

</li>

<li>

⁠**命题：**对自然数 $n$，$\mathcal E(n):=(n\ge7\Rightarrow n>5)$。

</li>

<li>

⁠**缺口集合：**$D=\{x\in\mathbb{Q}:x>0,\ x^2<2\}$，即平方小于 2 的正分数。

</li>

<li>

⁠**不等式用的数：**绝对值用 $x=-3$，$y=5$；均值用 $x=2$，$y=8$；柯西-施瓦茨不等式用数组 $\vec x=(3,4)$，$\vec y=(1,2)$。

</li>

</ul>
:::
