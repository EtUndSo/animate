---
title: 第 3 阶段：测量电流的误差
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电流与电压的测量
order: 1140400
summary: 电流表必须接入电路。本阶段计算它的内阻究竟使待测电流降低了多少。
tags: 相对误差
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
电流表必须接入电路。本阶段计算它的内阻究竟使待测电流降低了多少。
:::

**基本思路。** 测量时要断开电路，接入仪表（图 [4](#abb-4)）。回路中现在有 $R$ 和 $R_\mathrm i$。电源保持 $U$ 不变，在更大的总电阻中驱动更小的电流。读数没有错：它显示的是现在流过的电流。错的只是由此断定不接仪表时也流过同样的电流。

:::abbildung et1/k4strom 4
参考模型不接和接入电流表的情况。内阻上有 49.7 mV 的压降，电阻上就少了这部分电压。电流下降 0.55 %。
:::

:::satz 定理 3.1 (电流表的误差)
<span class="anker" id="satz-3-1"></span>

不接仪表时电流为 $I_R$，接入仪表时为 $I_R'$：

<span class="anker" id="gl-3-1"></span>
$$I_R=\frac UR,\qquad I_R'=\frac{U}{R+R_\mathrm i}<I_R,\qquad \frac{I_R}{I_R'}=\frac{R+R_\mathrm i}{R}=1+\frac{R_\mathrm i}{R}. \tag{3.1}$$

__相对误差__为 $f=(I_R'-I_R)/I_R=-R_\mathrm i/(R+R_\mathrm i)$。$R_\mathrm i\ll R$ 时 $f\approx-R_\mathrm i/R$。
:::

⁠**如何理解：**$U$ 是以 V 为单位的电源电压，$R$ 是电路的电阻，$R_\mathrm i$ 是仪表的电阻。带撇的电流是接入仪表时的电流。一般地，$f=(\text{读数}-\text{真值})/\text{真值}$，$f$ 为负表示读数偏小。**适用条件：**电路是理想电源加一个电阻。要使误差小，需要 $R_\mathrm i\ll R$，理想情况是 $R_\mathrm i=0$。

:::herleitung 电流表的误差
基尔霍夫电压定律为 $U=I_R'R+I_R'R_\mathrm i$，所以 $I_R'=U/(R+R_\mathrm i)$。于是 $f=I_R'/I_R-1=R/(R+R_\mathrm i)-1=-R_\mathrm i/(R+R_\mathrm i)$。
:::

**例。** $I_R=5$ mA，$I_R'=9\,\mathrm{V}/1810\,\Omega=4.972$ mA，所以 $f=-0.55\,\%$。若像数字万用表那样内阻为 1 $\Omega$，则为 4.997 mA，$f=-0.056\,\%$：误差可以忽略。对小电阻情况就不同了：0.9 V 加在 90 $\Omega$ 上得 10 mA，接入仪表后只有 9 mA，所以 $f=-10\,\%$。起决定作用的不是仪表本身，而是比值 $R_\mathrm i/R$。

⁠**极限情况：**$R_\mathrm i\to0$ 得 $f\to0$。$R\to0$ 得 $I_R'\to U/R_\mathrm i$ 和 $f\to-100\,\%$：此时只有仪表在限制电流。这就是练习 [1](das-messgerat-ist-ein-bauteil.html#aufg-1)(a)。

:::frage 电流表后面的电流比前面的小吗？
不。仪表中损失的不是电荷，只是能量。整个电路中的电流处处相同，并且因为总电阻增大而同时下降。
:::

:::aufgabe 练习 3 ★★ 哪个量程？
<span class="anker" id="aufg-3"></span>

(a) $R$ 至少为多大时，10 $\Omega$ 电流表的误差低于 1 %？(b) 90 k$\Omega$ 接在 9 V 上。比较 10 mA 量程和 250 µ A 量程：由 $R_\mathrm i$ 引起的误差和读数误差（满量程值的 1 %）。哪个量程测得更好？

:::loesung
(a) $R_\mathrm i/(R+R_\mathrm i)\le0.01$ 得 $R\ge99\,R_\mathrm i=990\,\Omega$。

(b) 真实电流为 $9\,\mathrm{V}/90\,\mathrm{k\Omega}=100$ µ A。在 10 mA 量程上，$R_\mathrm i=10\,\Omega$，$f=-0.011\,\%$，但读数误差为 $\pm100$ µ A，与电流本身一样大。在 250 µ A 量程上，$R_\mathrm i=100\,\mathrm{mV}/250\,\mu\text{A}=400\,\Omega$，$f=-0.44\,\%$，读数误差为 $\pm2.5$ µ A，即 2.5 %。小量程对电路的影响更大，但测得好得多。而且 $-0.44\,\%$ 还可以通过计算消除。
:::
:::
