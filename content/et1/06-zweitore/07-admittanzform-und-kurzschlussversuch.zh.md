---
title: 第 5 阶段：导纳形式与短路试验
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 二端口网络
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: 第 6 章：二端口网络
order: 1160700
summary: 第二种选择：电压是原因。本阶段把前面的内容全部移植过来，并说明为什么现在短路取代了开路的角色。
tags: Y 参数, 导纳, 短路输入电导, 短路输出电导, 短路转移电导, 跨导, 输入特性曲线, 转移特性曲线
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
第二种选择：电压是原因。本阶段把前面的内容全部移植过来，并说明为什么现在短路取代了开路的角色。
:::

**基本思路。** 如果电压是原因，就必须让一个电压消失，才能单独留下另一个份额。用导线跨接端口时，其电压为零。开路使电流为零，短路使电压为零。哪种试验正确，完全由原因的选择决定。

:::definition 定义 5.1 (导纳形式，Y 形式)
<span class="anker" id="satz-5-1"></span>

导纳形式（也称电导形式）以电压为原因：

<span class="anker" id="gl-5-1"></span>
$$I_1=Y_{11}U_1+Y_{12}U_2,\quad I_2=Y_{21}U_1+Y_{22}U_2,\qquad\text{简写为}\quad\mathbf I=\mathbf Y\cdot\mathbf U,\quad\mathbf Y=\begin{pmatrix}Y_{11}&Y_{12}\\Y_{21}&Y_{22}\end{pmatrix}. \tag{5.1}$$

__Y 参数__由两次短路试验得到：

<span class="anker" id="gl-5-2"></span>
$$Y_{11}=\left.\frac{I_1}{U_1}\right|_{U_2=0},\quad Y_{21}=\left.\frac{I_2}{U_1}\right|_{U_2=0},\quad Y_{12}=\left.\frac{I_1}{U_2}\right|_{U_1=0},\quad Y_{22}=\left.\frac{I_2}{U_2}\right|_{U_1=0}. \tag{5.2}$$

端口 2 接电导为 $Y_\mathrm{L}$ 的负载时，$I_2=-Y_\mathrm{L}U_2$，有

<span class="anker" id="gl-5-3"></span>
$$U_2=-\frac{Y_{21}}{Y_{22}+Y_\mathrm{L}}\,U_1,\qquad Y_1=\frac{I_1}{U_1}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}+Y_\mathrm{L}}, \tag{5.3}$$

其极限情况为

<span class="anker" id="gl-5-4"></span>
$$Y_{1,\mathrm{SC}}=Y_{11},\qquad Y_{1,\mathrm{OC}}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}}. \tag{5.4}$$
:::

⁠**如何理解：**$Y$ 代表__导纳__，即阻抗的倒数；这里是以西门子为单位的实电导，典型值从微西到毫西，$Y_{ii}=G_{ii}$。$Y_{11}$ 是__短路输入电导__，$Y_{22}$ 是__短路输出电导__。$Y_{21}$ 是正向__短路转移电导__，对晶体管称为__跨导__，一般称为转移导纳：输入电压对输出电流的作用。$Y_{12}$ 是反向的同一电导，即输出电压对输入电流的作用。等效电路（图 [6](#abb-6) 左）是 Z 形式的对应物：电流之和就是电导与电压控制电流源（VCCS）的并联。式 [(5.3)](#gl-5-3) 的得出与第 [4](das-zweitor-im-betrieb.html#stufe-4) 阶段相同，只是用左右节点上的节点定律代替网孔定律。

:::abbildung et1/k6yesb 6
左：Y 形式的等效电路。右：端口 2 的短路试验，施加电压为 $U_\mathrm{q}$。因 $U_2=0$，电源 $Y_{12}U_2$ 不起作用，$Y_{22}$ 中没有电流。剩下输入端的 $Y_{11}$ 和电流源 $Y_{21}U_1$，后者的电流流过导线。
:::

::::beispiel
T 形网络的端口 1 加 9 V，端口 2 短路。导线使 $R_\mathrm{c}$ 与 $R_\mathrm{b}$ 并联，总电阻为 $15\,\Omega+10\,\Omega=25\,\Omega$，所以 $I_1=360$ mA。这个电流平分，$I_2=-180$ mA，为负是因为它从端口 2 流出。端口 2 加 9 V、端口 1 短路时，总电阻为 $20\,\Omega+15\,\Omega\parallel20\,\Omega$，$I_2=315$ mA，$I_1=-180$ mA。由此得

$$\mathbf Y=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS}.$$

用第 [4](das-zweitor-im-betrieb.html#stufe-4) 阶段的工作状态检验：$I_1=40\,\mathrm{mS}\cdot7.75\,\mathrm{V}-20\,\mathrm{mS}\cdot3\,\mathrm{V}=250$ mA。负载 $Y_\mathrm{L}=16.67$ mS 给出 $Y_1=40\,\mathrm{mS}-400\,\mathrm{mS^2}/51.67\,\mathrm{mS}=32.26$ mS，即 $1/(31\,\Omega)$。
::::

⁠**极限情况：**$Y_{1,\mathrm{SC}}=40$ mS 即 $1/(25\,\Omega)$，$Y_{1,\mathrm{OC}}=28.57$ mS 即 $1/(35\,\Omega)$，与第 [4](das-zweitor-im-betrieb.html#stufe-4) 阶段一致。

**特性曲线。** Y 方程也可以画出来。__输入特性曲线__是固定 $U_2$ 时的 $I_1=f_1(U_1)$，__转移特性曲线__是固定 $U_2$ 时的 $I_2=f_2(U_1)$，__输出特性曲线__是固定 $U_1$ 时的 $I_2=f_3(U_2)$。线性二端口网络的这些曲线都是直线（图 [7](#abb-7)）：斜率是一个 Y 参数，固定值使其平行移动。固定参数的每个值给出一条直线，合起来形成一族曲线。

:::abbildung et1/k6kennlinien 7
T 形网络的特性曲线。左为输入特性曲线：斜率 $Y_{11}=40$ mS，$U_2$ 每一伏使曲线移动 $Y_{12}\cdot1\,\mathrm{V}=-20$ mA。中为转移特性曲线：斜率 $Y_{21}=-20$ mS。右为输出特性曲线：斜率 $Y_{22}=35$ mS。晶体管的这些曲线是弯曲的（[第 10 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)）。
:::

:::frage 为什么 $Y_{11}$ 不等于 $1/Z_{11}$？两者描述的都是输入端。
两者都描述输入端，但端接不同：$Z_{11}$ 对应输出端开路，$Y_{11}$ 对应输出端短路。在 T 形网络中，分别是 35 $\Omega$ 和 25 $\Omega$。只有 $Z_{12}$ 或 $Z_{21}$ 为零时，才有 $1/Y_{11}=Z_{11}$。
:::

:::aufgabe 练习 5 ★★ 一个 $\pi$ 形网络
<span class="anker" id="aufg-5"></span>

一个 $\pi$ 形网络的输入端并联电导为 $G_1=10$ mS，输出端并联电导为 $G_3=20$ mS，串联电导为 $G_2=40$ mS。

<ol class="al">

<li>

由短路试验求 $\mathbf Y$。端口 1 加 2 V 时流过哪些电流？

</li>

<li>

计算 $Y_{1,\mathrm{OC}}$，并用直接的电阻计算检验结果。

</li>

<li>

预测：$U_1=0$，$U_2=5$ V 时 $I_1$ 是多少，方向如何？

</li>

</ol>

:::loesung
(a) 端口 2 短路：$Y_{11}=G_1+G_2=50$ mS，$Y_{21}=-G_2=-40$ mS。端口 1 短路：$Y_{22}=G_2+G_3=60$ mS，$Y_{12}=-40$ mS。2 V 时：$I_1=100$ mA，$I_2=-80$ mA。 (b) $Y_{1,\mathrm{OC}}=50\,\mathrm{mS}-1600\,\mathrm{mS^2}/60\,\mathrm{mS}=23.33$ mS，即 42.86 $\Omega$。直接计算：$100\,\Omega\parallel(25\,\Omega+50\,\Omega)=42.86\,\Omega$。 (c) $I_1=Y_{12}U_2=-200$ mA。端口 1 短路，电流从端口 2 经 $G_2$ 流动，并在接线端 1 离开二端口网络。
:::
:::
