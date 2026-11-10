---
title: 第 8 阶段：利用 $U_\mathrm{BE}$ 的两种电路
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 双极型晶体管
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: 第 10 章：双极型晶体管
order: 1201000
summary: 到目前为止， U BE 一直是干扰因素。本阶段利用它的两个性质： U BE 相同则电流相同，电流变化时 U BE 几乎不变。
tags: 电流镜, 参考电流, 纹波
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
到目前为止，$U_\mathrm{BE}$ 一直是干扰因素。本阶段利用它的两个性质：$U_\mathrm{BE}$ 相同则电流相同，电流变化时 $U_\mathrm{BE}$ 几乎不变。
:::

**基本思路：电流镜。** 根据式 [(2.1)](warum-strom-durch-die-gesperrte-diode-fliet.html#gl-2-1)，$U_\mathrm{BE}$ 决定电流。所以两个相同的晶体管在相同的电压 $U_\mathrm{BE}$ 下通过相同的电流。在__电流镜__（图 [9](#abb-9) 左侧）中，T1 接成二极管：基极和集电极相连。流过电阻的电流 $I_\mathrm{ref}$ 在 T1 上建立起这个电流恰好需要的电压 $U_\mathrm{BE}$。T2 接在同一电压上，把电流复制到另一支路，与其负载无关。

:::satz 定理 8.1 (电流镜)
<span class="anker" id="satz-8-1"></span>

对于相同的晶体管，且 $I_\mathrm{B1}=I_\mathrm{B2}$，有

<span class="anker" id="gl-8-1"></span>
$$I_\mathrm{ref}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{ref}}=I_\mathrm{C1}+I_\mathrm{B1}+I_\mathrm{B2}=(B+2)I_\mathrm{B2},\qquad I_\mathrm{C2}=B\,I_\mathrm{B2}=\frac{I_\mathrm{ref}}{1+\frac2B}\approx I_\mathrm{ref}. \tag{8.1}$$
:::

⁠**如何理解：**$I_\mathrm{ref}$ 是__参考电流__。两个基极电流从它分出。这就是小误差 $2/B$ 的来源。**适用条件：**T2 处于放大区，晶体管相同且温度相同，例如在同一芯片上。由于特性曲线有斜率，$U_\mathrm{CE2}$ 大时 T2 输出略多一些。

::::beispiel
当 $R_\mathrm{ref}=5.7$ k$\Omega$ 时，$I_\mathrm{ref}=2$ mA，$I_\mathrm{C2}=1.98$ mA，$R_\mathrm{L}$ 可取到 $11.8\,\mathrm{V}/1.98\,\mathrm{mA}=5.96$ k$\Omega$ 之内的任意值。超过这个值 T2 就会饱和。由式 [(3.1)](eine-flache-viele-kennlinien.html#gl-3-1)，在 $U_\mathrm{CE2}=6$ V 和 $U_\mathrm{CE1}=0.6$ V 时，T2 中的电流将大 7 %。
::::

⁠**极限情况：**当 $B\to\infty$ 时，$I_\mathrm{C2}=I_\mathrm{ref}$。

**基本思路：稳压器。** 带滤波的整流器（[第 9 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)）提供的直流电压带有残余波动，即__纹波__。在稳压器（图 [9](#abb-9) 右侧）中，齐纳二极管把基极稳定在 $U_\mathrm{Z}$。发射极是输出端，比基极低一个二极管电压。如果负载取用更多电流使输出电压下降，$U_\mathrm{BE}$ 就增大，晶体管就多提供电流。输入电压的其余部分降在 $U_\mathrm{CE}$ 上。负载电流不流过 $R_1$，基极只需要它的 $B$ 分之一。所以齐纳二极管几乎不受负载影响。

:::satz 定理 8.2 (带齐纳二极管的稳压器)
<span class="anker" id="satz-8-2"></span>

由经过齐纳二极管、BE 通路和负载的网孔得

<span class="anker" id="gl-8-2"></span>
$$U_\mathrm{A}=U_\mathrm{Z}-U_\mathrm{BE}. \tag{8.2}$$
:::

⁠**如何理解：**$U_\mathrm{E,min}$ 是输入电压 $U_\mathrm{E}$ 在纹波谷底的最小值，$U_\mathrm{A}$ 是输出电压。**适用条件：**必须始终满足 $U_\mathrm{E}>U_\mathrm{A}+U_\mathrm{CE,sat}$，T 才能保持在放大区，并且 $R_1$ 必须提供足够的电流：$(U_\mathrm{E,min}-U_\mathrm{Z})/R_1>I_\mathrm{B}$。否则齐纳二极管退出击穿状态，纹波就会到达输出端。

:::abbildung et1/k10spiegel 9
左：电流镜，T1 接成二极管产生 $U_\mathrm{BE}$，T2 复制电流。中：带齐纳二极管的稳压器，发射极是输出端。右：波形，输入电压在 10.5 V 和 13.5 V 之间波动，输出保持在 5.6 V。
:::

::::beispiel
$U_\mathrm{Z}=6.2$ V 给出 $U_\mathrm{A}=5.6$ V。负载为 50 mA 时，基极需要 0.25 mA。取 $R_1=1$ k$\Omega$ 和 $U_\mathrm{E}=12$ V$\,\pm1.5$ V，流过齐纳二极管的电流为 4.05 mA 到 7.05 mA。小信号电阻为 10 $\Omega$ 的齐纳二极管把 3 V 纹波减小到只有 30 mV。晶体管上产生的功率最高为 $7.9\,\mathrm{V}\cdot50\,\mathrm{mA}=395$ mW，刚好低于 $P_\mathrm{max}$。稳压器把多余的电压转化为热。如果用 0.68 V（50 mA 时更准确的 $U_\mathrm{BE}$）代替 0.6 V，$U_\mathrm{A}$ 将小 80 mV。
::::

⁠**极限情况：**没有负载时，$I_\mathrm{B}\approx0$，$U_\mathrm{A}$ 略有上升，$U_\mathrm{Z}$ 不变。

:::frage 为什么不只用齐纳二极管？
那样的话，串联电阻在输入电压最低时必须提供全部 50 mA，再加上留给齐纳二极管的余量。在峰值电压时，差额将流过齐纳二极管，串联电阻的发热约为 0.7 W。晶体管把两者分开：齐纳二极管给定电压，电源经集电极提供电流。功率晶体管及由其派生的元件还能开关大电流，例如在电动机变流器中。
:::

:::aufgabe 练习 10 ★★ 电流镜和稳压器
<span class="anker" id="aufg-10"></span>

(a) 在 $U_\mathrm{CC}=12$ V 下，多大的 $R_\mathrm{ref}$ 给出 1 mA 的参考电流？$B=200$ 和 $B=50$ 时 $I_\mathrm{C2}$ 各是多少？(b) $B=200$ 时，电流镜能工作到多大的 $R_\mathrm{L}$？(c) 稳压器的 $U_\mathrm{Z}=9.1$ V，$R_1=470\,\Omega$，负载 30 mA，$U_\mathrm{E}$ 从 12 V 到 15 V。求 $U_\mathrm{A}$、最小的齐纳电流、晶体管的最大功率以及向下的电压裕量。

:::loesung
(a) $R_\mathrm{ref}=11.4\,\mathrm{V}/1\,\mathrm{mA}=11.4$ k$\Omega$。$I_\mathrm{C2}=1\,\mathrm{mA}/1.01=0.990$ mA，$B=50$ 时为 $1\,\mathrm{mA}/1.04=0.962$ mA。

(b) $R_\mathrm{L}\le11.8\,\mathrm{V}/0.990\,\mathrm{mA}=11.9$ k$\Omega$。

(c) $U_\mathrm{A}=8.5$ V，$I_\mathrm{B}=0.15$ mA。在 12 V 时，流过 $R_1$ 的电流为 $2.9\,\mathrm{V}/470\,\Omega=6.17$ mA，流过齐纳二极管的电流为 6.02 mA。在 15 V 时，$P=6.5\,\mathrm{V}\cdot30\,\mathrm{mA}=195$ mW。裕量：$12\,\mathrm{V}-8.5\,\mathrm{V}-0.2\,\mathrm{V}=3.3$ V。
:::
:::
