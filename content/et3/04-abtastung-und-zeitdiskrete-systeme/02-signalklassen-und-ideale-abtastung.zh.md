---
title: 第 1 阶段：信号类别与理想采样
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 采样与离散时间系统
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: 第 4 章：采样与离散时间系统
order: 3240200
summary: 信号有哪些类型？采样在数学上如何描述？
tags: 模拟, 离散时间, 数字, 理想采样器
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
信号有哪些类型？采样在数学上如何描述？
:::

**四种类别。** 时间和幅度都可以是连续的或离散的。__模拟__信号在这两方面都是连续的。__离散时间__信号只在时刻 $nT$ 有取值，但这些取值可以任意精确。__数字__信号的幅度还是分级的（量化），因为计算机只能表示有限多个数。本章讨论时间的离散化。幅度的量化是另一个专题。

**从实际采样器到理想采样器。** 实际采样器在每个采样周期内将开关闭合一段很短的时间 $T_0$：

<span class="anker" id="gl-1-1"></span>
$$s_0(t)=s(t)\sum_{n=-\infty}^{\infty}\operatorname{rect}\Bigl(\frac{t-nT}{T_0}\Bigr)=s(t)\Bigl[\operatorname{rect}\Bigl(\frac{t}{T_0}\Bigr)*\sum_n\delta(t-nT)\Bigr]. \tag{1.1}$$

若使 $T_0$ 越来越短，就只剩下取值 $s(nT)$。在数学上，用狄拉克冲激代替矩形。这就是__理想采样器__：

<span class="anker" id="gl-1-2"></span>
$$s_\mathrm a(t)=s(t)\sum_{n=-\infty}^{\infty}\delta(t-nT)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT). \tag{1.2}$$

采样信号是一串狄拉克冲激，每个冲激以一个样本值为权重。第二步用到的是筛选性质 $s(t)\delta(t-nT)=s(nT)\delta(t-nT)$。写成这种形式后，采样信号就可以用处理连续信号的全部工具来处理。
