---
title: 从头开始：接线端、特性曲线、线性
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电源与等效电源
order: 1150200
summary: 为什么两个数就能代替整个网络
tags: 接线端, 一端口网络, 特性曲线, 开路, 线性
lang: zh
---

__接线端__是通向外部的连接点。__一端口网络__是恰有两个接线端且二者构成一对的网络：从 A 流出的电流又从 B 流回，因为电荷不会丢失（节点定律，[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。因此一端口网络只有一个电流和一个电压。它就是[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)所说的二端元件，即使内部含有许多元器件。__特性曲线__是这两个量之间的关系。在本章中它总是画在同一种图里：接线端电流为横轴，接线端电压为纵轴。

参考箭头在本章中统一规定：$U_\mathrm{AB}=\varphi_\mathrm{A}-\varphi_\mathrm{B}$ 从 A 指向 B，$I_\mathrm{A}$ 以流出接线端 A 为正。对接上的负载，两个箭头方向相同（负载惯例，[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）；对一端口网络本身，两者方向相反（发电机惯例）。两者都为正时，一端口网络输出功率。__开路__是指：接线端断开，$I_\mathrm{A}=0$。短路是指：接线端由一根导线相连，$U_\mathrm{AB}=0$。

元件的电流与其电压成正比时，该元件是__线性__的。只要 $R$ 不随电流变化，电阻就是线性的：其特性曲线是一条过原点的直线。白炽灯或二极管（[第 9 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)）则不是。符号 $\parallel$ 表示并联电路的电阻，$R_1\parallel R_2=\frac{R_1R_2}{R_1+R_2}$（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。它的优先级高于加号，就像乘法一样。
