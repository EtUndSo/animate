---
title: 概览: 复数
kurz: 概览
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 复数
order: 1220100
summary: 第二条坐标轴如何使 $x^2=-1$ 有解 以及由此失去了什么
tags: 实部, 虚部
lang: zh
---

## 本章内容

方程 $x^2=-1$ 在 $\mathbb{R}$ 中无解，因为实数的平方永远不是负数。然而二次方程总是一再引出负数的平方根，交流电技术每天都在用它们计算。问题是：**能否扩充 $\mathbb{R}$，使 $x^2=-1$ 有解而运算法则保持不变？这样做又会失去什么？**


**所有结论背后的同一个原理。** 本章的一切都来自一条规则：把 $\mathrm{i}$ 当作字母来运算，并把 $\mathrm{i}^2$ 换成 $-1$。

| 结论 | 来源 |
|---|---|
| 乘积公式 | 展开，其中的减号就是 $\mathrm{i}^2$（第 [1](paare-statt-einzelner-zahlen.html#stufe-1) 阶段） |
| 加法即平行四边形 | 实部和虚部分别相加（第 [2](die-komplexe-ebene.html#stufe-2) 阶段） |
| 乘 $\mathrm{i}$ 即旋转 $90^\circ$ | $\mathrm{i}(x+\mathrm{i}y)=-y+\mathrm{i}x$，旋转两次就是 $-1$（第 [2](die-komplexe-ebene.html#stufe-2) 阶段） |
| $z\overline{z}=x^2+y^2$ | 平方差公式，加上 $-\mathrm{i}^2=+1$（第 [3](spiegeln-an-der-reellen-achse.html#stufe-3) 阶段） |
| 除法 | 分子分母同乘 $\overline{z}$，使分母成为实数（第 [4](dividieren-und-was-verloren-geht.html#stufe-4) 阶段） |
| 没有序 | $\mathrm{i}^2=-1$ 是一个负的平方（第 [4](dividieren-und-was-verloren-geht.html#stufe-4) 阶段） |
| $\vert zw\vert =\vert z\vert \,\vert w\vert $，三角不等式 | $\vert z\vert ^2=z\overline{z}$（第 [5](betrag-und-abstand.html#stufe-5) 阶段） |
| 二次方程 | 配方在任何域中都成立，每个数都有平方根（第 [6](quadratische-gleichungen.html#stufe-6) 阶段） |

**如何使用本章。**每个阶段都是一篇简短的文章，包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。完成一个阶段后再进入下一个。

:::merke 本章的参考模型
<ul>

<li>

⁠**两个固定的数：**$z_1=3+\mathrm{i}$ 和 $z_2=1+2\mathrm{i}$。在 $z_1$ 中，3 是__实部__（不含 $\mathrm{i}$ 的部分），1 是__虚部__（$\mathrm{i}$ 前面的实数）。本章的一般性命题用 $z$ 和 $w$ 书写。

</li>

<li>

⁠**由它们得到的结果：**$z_1+z_2=4+3\mathrm{i}$，$z_1z_2=1+7\mathrm{i}$，$z_1/z_2=1-\mathrm{i}$，$|z_1+z_2|=5$。

</li>

<li>

⁠**两个方程：**$z^2-6z+10=0$ 的系数是实数，$z^2-(4+3\mathrm{i})z+1+7\mathrm{i}=0$ 的系数是复数。第二个方程的解恰好是 $z_1$ 和 $z_2$。

</li>

</ul>

脚本 `rechnung_kap2.py` 可复算所有数值。
:::
