---
title: 第 2 阶段：平稳性与各态历经性
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 随机信号
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: 第 7 章：随机信号
order: 3270300
summary: 无限的集合是永远得不到的，通常只有单个信号。什么时候这就足够了？
tags: 平稳, 各态历经
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
无限的集合是永远得不到的，通常只有单个信号。什么时候这就足够了？
:::

若把所有观测时刻都平移同一段时间 $t_0$ 时，过程的任何平均值都不改变，就称该过程是__平稳__的：

<span class="anker" id="gl-2-1"></span>
$$\mathrm E\{F[s(t_1)]\}=\mathrm E\{F[s(t_1+t_0)]\},\qquad\mathrm E\{F[s(t_1),s(t_2)]\}=\mathrm E\{F[s(t_1+t_0),s(t_2+t_0)]\}. \tag{2.1}$$

这时均值 $m_s=\mathrm E\{s(t)\}$ 是常数，而自相关函数只取决于时间差 $\tau=t_2-t_1$：$\varphi_{ss}(\tau)=\mathrm E\{s(t)s(t+\tau)\}$。如果一个平稳过程的每个样本函数的时间平均还都等于相应的集平均，就称它是__各态历经__（遍历）的：

<span class="anker" id="gl-2-2"></span>
$$\mathrm E\{F[s(t)]\}=\overline{F[{}^ks(t)]}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t\quad\text{对每个}\ k. \tag{2.2}$$

⁠**如何理解：**平稳意味着统计特性不随时间变化。各态历经意味着：单个样本函数只要观测得足够久，就会在时间进程中呈现出整个集合所呈现的一切。恒温下电阻的噪声是各态历经的。正因为如此，才能用单台测量仪器来表征噪声。

:::frage 每个平稳过程都是各态历经的吗？
不是。例：每个样本函数都是一个常数，其值只随机抽取一次，${}^ks(t)=c_k$。这个过程是平稳的，因为没有任何量依赖于 $t$。但样本函数的时间平均是 $c_k$，它对每个样本函数都不同，并不等于集平均。单个样本函数永远“看不到”其他的取值。
:::
