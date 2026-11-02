---
title: 从头开始：阀门、交流电压与热能
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 半导体与二极管
order: 1190200
summary: 硅如何变成电流的阀门， 以及如何用它进行计算
tags: 交流电压, 峰值, 频率, 半波整流器, 电子伏特, 热能, 玻尔兹曼常数, 玻尔兹曼分布
lang: zh
---

__交流电压__周期性地改变符号。这里它是正弦形的，$u_\mathrm e(t)=\hat u\sin(2\pi ft)$，其中 $\hat u$ 是__峰值__（最大绝对值），$f$ 是__频率__（每秒振荡次数，单位 Hz）。一次振荡持续 $T=1/f$，在 50 Hz 时为 20 ms。小写字母表示随时间变化的量。

:::abbildung et1/k9einweg 1
左：二极管（端子为阳极 A 和阴极 K）与电阻串联，接在交流电压上。右上：电阻上只出现正半波，并减小 0.7 V。右下：二极管导通时保持 0.7 V，截止时承受全部负电压。$\hat u=12$ V，50 Hz。
:::

图 [1](#abb-1) 显示了二极管的作用。由网孔得 $u_\mathrm e=u_\mathrm D+u_\mathrm a$。若 $u_\mathrm e$ 为正，二极管导通，其上保留约 0.7 V，其余电压加在电阻上。若 $u_\mathrm e$ 为负，则没有电流。此时 $u_\mathrm a=0$，二极管承受全部电压。交流电压变成只有一种符号的电压。这种电路称为__半波整流器__。其峰值为 $12\,\mathrm{V}-0.7\,\mathrm{V}=11.3$ V。

为了解释其原因，本章需要两个能量量。__电子伏特__（eV）是一个电子经过 1 V 电压获得的能量（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）：$1\,\mathrm{eV}=e\cdot1\,\mathrm{V}=1.602\cdot10^{-19}$ J。__热能__的来源是：原子和电子在任何温度下都作无规则运动。它的量度是 $k_\mathrm BT$，其中 $T$ 是以 K 为单位的绝对温度，$k_\mathrm B$ 是__玻尔兹曼常数__。在 300 K 时，$k_\mathrm BT=4.14\cdot10^{-21}\,\mathrm{J}=25.85$ meV。碰撞使这些能量分配不均：少数粒子能量多，多数粒子能量少。平衡时服从__玻尔兹曼分布__：

<span class="anker" id="gl-0-1"></span>
$$\text{能量不低于 }W\text{ 的粒子所占比例}=\mathrm{e}^{-W/(k_\mathrm BT)}. \tag{0.1}$$

能量每增加一个 $k_\mathrm BT$，比例就缩小到原来的 1/2.718；在 $10\,k_\mathrm BT$ 处为 $4.5\cdot10^{-5}$。同一规律也描述了空气如何随高度变稀薄。
