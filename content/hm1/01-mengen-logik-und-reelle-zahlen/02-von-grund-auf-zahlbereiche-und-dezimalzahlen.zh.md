---
title: 从头开始：数系与小数
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 集合、逻辑与实数
order: 1210200
summary: 关于数必须预设什么 以及为什么 2 的平方根不是分数
tags: 自然数, 整数, 有理数, 实数, 无理数
lang: zh
---

符号 $:=$ 表示“定义为”。__自然数__是 $\mathbb{N}:=\{1,2,3,\dots\}$，__整数__是 $\mathbb{Z}:=\{0,1,-1,2,-2,\dots\}$，__有理数__（分数）是 $\mathbb{Q}:=\{p/q:p,q\in\mathbb{Z},\ q\ne0\}$。冒号表示“满足”。

:::definition 定义 0.1 (实数，暂定)
<span class="anker" id="satz-0-1"></span>

__实数__是具有小数表示的数，即有一个符号、一个 $m\in\mathbb{N}\cup\{0\}$ 和数字 $a_1,a_2,\ldots\in\{0,1,\dots,9\}$，数字有有限个或无限个：

<span class="anker" id="gl-0-1"></span>
$$x=\pm\Bigl(m+\frac{a_1}{10}+\frac{a_2}{100}+\frac{a_3}{1000}+\dots\Bigr). \tag{0.1}$$

$\mathbb{R}$ 是全体实数的集合。$\mathbb{R}$ 中不是分数的数称为__无理数__。
:::

⁠**如何理解：**$3/8=0.375$ 是有限小数，$5/11=0.4545\ldots$ 是循环小数，每个分数都具有这两种形式之一。$\sqrt2=1.41421356\ldots$ 永远不会循环。有 $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$。这个定义只是过渡方案：它没有解释无穷和是什么（第 4 部分），而且表示不唯一，$1.000\ldots$ 和 $0.999\ldots$ 是同一个数。第 [6](das-vollstandigkeitsaxiom.html#stufe-6) 阶段将用公理取代它。
