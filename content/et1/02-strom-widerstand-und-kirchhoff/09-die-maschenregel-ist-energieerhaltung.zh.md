---
title: 第 8 阶段：网孔定律就是能量守恒
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电流、电阻与基尔霍夫定律
order: 1120900
summary: 第二类方程：能量守恒对闭合路径有什么要求？有了它，就能完全解出网络。
tags: 
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
第二类方程：能量守恒对闭合路径有什么要求？有了它，就能完全解出网络。
:::

**基本思路。** 网络中的每一点都有一个电位（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。绕行一周回到同一点，也就回到同一电位（图 [9](#abb-9)）。对电荷来说，这意味着：它在电源中获得的能量，又在电阻中释放出去。在电池中，化学力把电荷逆着电场抬升到较高的电位。

:::analogie
环形徒步的终点就是起点。所有上坡加起来与所有下坡一样高，无论选择哪条路线。当磁场变化时，这个类比就失效了：这时一个地点不再有固定的“高度”（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。
:::

:::satz 定理 8.1 (网孔定律，基尔霍夫第二定律)
<span class="anker" id="satz-8-1"></span>

沿一个网孔的所有支路电压之和，在任何绕行方向和任何时刻都为零：

<span class="anker" id="gl-8-1"></span>
$$\sum_{\nu=1}^{N}U_\nu=0,\qquad U_\nu\text{ 与绕行方向一致时计为正，相反时计为负。} \tag{8.1}$$

对一个网络，这些方程中有 $z-k+1$ 个是独立的，其余的也就自动满足。
:::

⁠**如何理解：**$U_\nu$ 是一条支路的电压，带有其箭头。绕行方向可自由选择，它只改变总的符号。**适用条件：**穿过网孔的磁通量不得变化，否则电场不是无旋的（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。在电路中，这种磁通几乎全部集中在线圈中。该定律也适用于经过开路端子的路径，因为路径不必沿着导线。

:::herleitung 由电位得网孔定律
根据[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)，$U_{12}=\varphi_1-\varphi_2=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$ 与路径无关，所以 $\oint\vec E\cdot\mathrm{d}\vec s=0$。对沿网孔的点 $P_1,\dots,P_N$，得

$$(\varphi_1-\varphi_2)+(\varphi_2-\varphi_3)+\dots+(\varphi_N-\varphi_1)=0.$$

每个电位出现一次带 $+$，一次带 $-$。乘以电荷 $Q$，这就是绕行一周的能量平衡：所有 $Q\,U_\nu$ 之和为零。
:::

:::abbildung et1/k2masche 9
已解网络中沿两个网孔的电位。沿箭头方向走时，正电压使电位降低；逆箭头方向走时使电位升高。左：电源升高，$R_\mathrm a$ 和 $R_\mathrm b$ 共降低 $4+5=9$ V。右边的绕行不经过电源：逆着电流经 $R_\mathrm b$ 返回的路径使电位升高。两次绕行都回到起始值。
:::

::::beispiel 求解网络
电阻上的电压箭头采用负载惯例，即从上到下，$U_\mathrm e$ 从 $K_2$ 到 $K_3$。$U_0=9$ V 从 $K_1$ 指向 $K_4$（发电机惯例）。由图 [7](knoten-zweige-maschen.html#abb-7) 的三个网孔得

$$M_1:\ U_\mathrm a+U_\mathrm b-U_0=0,\qquad M_2:\ U_\mathrm c+U_\mathrm d-U_0=0,\qquad M_3:\ U_\mathrm e+U_\mathrm d-U_\mathrm b=0.$$

代入欧姆定律和节点方程 $I_\mathrm b=I_\mathrm a-I_\mathrm e$、$I_\mathrm d=I_\mathrm c+I_\mathrm e$，剩下三个未知量（单位为 mA、$\mathrm{k\Omega}$、V）：

$$7\,I_\mathrm a-5\,I_\mathrm e=9,\qquad4\,I_\mathrm c+I_\mathrm e=9,\qquad-5\,I_\mathrm a+I_\mathrm c+8\,I_\mathrm e=0.$$

由前两个方程得 $I_\mathrm a=(9+5\,I_\mathrm e)/7$ 和 $I_\mathrm c=(9-I_\mathrm e)/4$。代入第三个方程并乘以 28，得 $117\,I_\mathrm e=117$，即 $I_\mathrm e=1$ mA。于是

| 支路 | 0 | a | b | c | d | e |
|---|---|---|---|---|---|---|
| $I$（mA） | 4 | 2 | 1 | 2 | 3 | 1 |
| $U$（V） | 9 | 4 | 5 | 6 | 3 | 2 |

相对于 $K_4$ 的电位分别为 9、5、3 和 0 V。**检验：**经过 $K_1$、$K_2$、$K_3$ 的第四个网孔必须自动成立：$U_\mathrm a+U_\mathrm e-U_\mathrm c=4+2-6=0$。能量：电源提供 $9\,\mathrm{V}\cdot4\,\mathrm{mA}=36$ mW，电阻吸收 $8+5+12+9+2=36$ mW。如果同样两点之间有两条路径，例如 $R_1$、$R_2$ 串联后与 $R_3$ 并排，则得 $U_1+U_2-U_3=0$。
::::

:::ltspice 验算网络
⁠**绘制：**电压源 `voltage` 取 `9`，从 `k1` 接地，因此 $K_4$ 就是接地点。`res`：`Ra 2k` 从 `k1` 接到 `k2`，`Rb 5k` 从 `k2` 接地，`Rc 3k` 从 `k1` 接到 `k3`，`Rd 1k` 从 `k3` 接地，`Re 2k` 从 `k2` 接到 `k3`。

⁠**指令：**`.op`，另加 `.meas op p2 FIND V(k2)`、`.meas op ie FIND I(Re)`，其他量同样处理。结果显示在 SPICE Error Log 中。

⁠**你会看到：**$\mathtt{V(k2)}=5$ V，$\mathtt{V(k3)}=3$ V，$\mathtt{I(Ra)}=\mathtt{I(Rc)}=2$ mA，$\mathtt{I(Rb)}=\mathtt{I(Re)}=1$ mA，$\mathtt{I(Rd)}=3$ mA。$\mathtt{I(V1)}=-4$ mA：SPICE 按负载惯例计算电源电流，所以为负。然后搭建练习 [8](#aufg-8)。
:::

:::frage 电流怎么“知道”该如何分配？
它什么也不知道。接通时，节点上聚集极少的电荷，使节点电位不断移动，直到每个节点上都不再有电荷滞留。这在纳秒内完成。结果就是同时满足两条定律的唯一解。
:::

:::aufgabe 练习 8 ★★ 网孔与节点结合
<span class="anker" id="aufg-8"></span>

一个 12 V 电源给 $R_1=1.5\,\mathrm{k\Omega}$ 供电，其后是并排的 $R_2=3\,\mathrm{k\Omega}$ 和一个未知电阻 $R_3$。测得 $U_1=9$ V。

<ol class="al">

<li>

用网孔定律求 $U_2$ 和 $U_3$。

</li>

<li>

求所有电流和 $R_3$。

</li>

<li>

检验能量平衡。

</li>

<li>

预测：一根运动的条形磁铁穿过由电源、$R_1$ 和 $R_2$ 构成的网孔。现在什么不再成立？

</li>

</ol>

:::loesung
(a) 由电源、$R_1$、$R_2$ 构成的网孔：$U_2=12\,\mathrm{V}-9\,\mathrm{V}=3$ V。由 $R_2$、$R_3$ 构成的网孔：$U_3=U_2=3$ V。

(b) $I_1=9\,\mathrm{V}/1.5\,\mathrm{k\Omega}=6$ mA，$I_2=3\,\mathrm{V}/3\,\mathrm{k\Omega}=1$ mA。节点定律：$I_3=5$ mA，所以 $R_3=3\,\mathrm{V}/5\,\mathrm{mA}=600\,\Omega$。检验：$R_2\parallel R_3=500\,\Omega$，总计 $2\,\mathrm{k\Omega}$，$12\,\mathrm{V}/2\,\mathrm{k\Omega}=6$ mA。

(c) 电源提供 $12\,\mathrm{V}\cdot6\,\mathrm{mA}=72$ mW，电阻吸收 $54+3+15=72$ mW。

(d) 网孔定律。变化的磁通沿网孔产生涡旋场，$\oint\vec E\cdot\mathrm{d}\vec s$ 不为零，各电压之和等于感应电压。节点定律仍然成立。
:::
:::
