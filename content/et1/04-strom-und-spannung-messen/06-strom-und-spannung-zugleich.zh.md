---
title: 第 5 阶段：同时测量电流和电压
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电流与电压的测量
order: 1140600
summary: 用 R=U/I 求电阻时，两台仪表都要用。此时其中一台处在另一台的测量回路中。本阶段比较两种可能的电路。
tags: 
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
用 $R=U/I$ 求电阻时，两台仪表都要用。此时其中一台处在另一台的测量回路中。本阶段比较两种可能的电路。
:::

**基本思路。** 电压表可以接在电流表之前或之后（图 [6](#abb-6)）。如果接在电流表之前，电流表测到的恰好是流过 $R$ 的电流，但电压表测到的是 $R$ 和电流表上的电压之和。如果直接接在 $R$ 上，电压是正确的，但电流表把电压表的电流也算了进去。

:::abbildung et1/k4richtig 6
两种测量电路。绿色为正确的读数，红色为含有另一台仪表影响的读数。
:::

:::definition 定义 5.1 (电流正确的测量与电压正确的测量)
<span class="anker" id="satz-5-1"></span>

$U$ 和 $I$ 是读数，$U_R$ 和 $I_R$ 是电阻上的值。

电流正确：$I=I_R$，但 $U=U_R+U_\mathrm{iA}\neq U_R$。由此得

<span class="anker" id="gl-5-1"></span>
$$\frac UI=R+R_\mathrm{iA},\qquad f=+\frac{R_\mathrm{iA}}{R}. \tag{5.1}$$

电压正确：$U=U_R$，但 $I=I_R+I_\mathrm{iV}\neq I_R$。由此得

<span class="anker" id="gl-5-2"></span>
$$\frac UI=R\parallel R_\mathrm{iV},\qquad f=-\frac{R}{R+R_\mathrm{iV}}. \tag{5.2}$$
:::

⁠**如何理解：**$U_\mathrm{iA}$ 是电流表上的压降，$I_\mathrm{iV}$ 是流过电压表的电流。$f$ 是 $U/I$ 相对于 $R$ 的误差。不可能同时正确读出同一电阻上的电流和电压。但如果已知内阻，结果可以修正：$R=U/I-R_\mathrm{iA}$ 或 $1/R=I/U-1/R_\mathrm{iV}$。

:::herleitung 读数之比
电流正确：$U/I=(I_RR+I_RR_\mathrm{iA})/I_R=R+R_\mathrm{iA}$。电压正确：$I/U=(I_R+I_\mathrm{iV})/U_R=1/R+1/R_\mathrm{iV}$，所以 $U/I=R\parallel R_\mathrm{iV}$，$f=(R\parallel R_\mathrm{iV})/R-1=-R/(R+R_\mathrm{iV})$。
:::

::::beispiel
参考模型在两种电路中的结果：

|  | 读数 $U$ | 读数 $I$ | $U/I$ 及误差 |
|---|---|---|---|
| 电流正确 | 9.000 V（$R$ 上：8.950 V） | 4.972 mA | 1810 $\Omega$， $+0.56\,\%$ |
| 电压正确 | 8.950 V | 5.017 mA（流过 $R$：4.972 mA） | 1783.9 $\Omega$， $-0.89\,\%$ |

计算修正在两种情况下都回到 1800 $\Omega$。
::::

**用哪种电路？** 图 [7](#abb-7) 给出了两种误差随 $R$ 的变化。小电阻用电压正确的电路测量，因为其电流远大于电压表的电流。大电阻用电流正确的电路测量，因为其电压远大于电流表上的压降。两条曲线在 1.4 k$\Omega$ 附近相交（练习 [6](#aufg-6)）。在 1.8 k$\Omega$ 时，电流正确的电路略好。

:::abbildung et1/k4fehler 7
$R_\mathrm{iA}=10\,\Omega$、$R_\mathrm{iV}=200$ k$\Omega$ 时 $U/I$ 的相对误差的绝对值，两轴均为对数刻度。圆点对应参考模型。
:::

:::ltspice 两种测量电路
⁠**绘制：**电源 `voltage`，9 V，接在节点 `q` 上。电流表是一个值为 10 的 `res`，电压表是一个值为 200k 的 `res`。电流正确：`RA1` 从 `q` 到 `a`，`RX1` = 1.8k 从 `a` 到接地点，`RV1` 从 `q` 到接地点。电压正确：`RA2` 从 `q` 到 `b`，`RX2` = 1.8k 和 `RV2` 从 `b` 到接地点。

⁠**指令：**`.op`

⁠**你会看到：**`I(RA1)` = 4.972 mA，`V(q)` = 9 V，所以为 1810 $\Omega$。`I(RA2)` = 5.017 mA，`V(b)` = 8.950 V，所以为 1783.9 $\Omega$。然后代入练习 [5](#aufg-5) 的数值并进行比较。
:::

:::frage 为什么不先后测量，先测电流，再测电压？
这在这里没有帮助。电流表单独接在回路中，仍显示 4.972 mA；电压表单独接在 $R$ 上，显示 9.000 V。结果是 1810 $\Omega$，与电流正确的电路相同：每台仪表自身的误差依然存在。
:::

**不用电流表测电阻。** 因此，数字万用表用另一种方式测电阻。一个精确的恒流源（电流已知且固定的电流源）驱动电流 $I_\mathrm q$ 流过 $R$，只需测量电压：$R=U/I_\mathrm q\propto U$。电流是整的十的幂，所以显示时只需设定小数点和词头（毫、千、兆）：1 mA 流过 1.8 k$\Omega$ 得 1.800 V，显示为 1.800 k$\Omega$。剩下的误差是 $R/(R+R_\mathrm{iV})$，内阻为 10 M$\Omega$ 时为 0.018 %。测小电阻时，连接导线会造成干扰：0.5 $\Omega$ 上有 0.1 $\Omega$ 的导线电阻就是 20 %。因此，开尔文测量把两条路径分开：两根导线通电流，另外两根直接在元件上取电压。后者中几乎没有电流，所以它们的电阻不起作用。

:::aufgabe 练习 5 ★★ 用哪种电路？
<span class="anker" id="aufg-5"></span>

仪表同参考模型，量程选择合适，内阻不变。计算两种电路中的 $U/I$ 和 $f$：(a) $R=100\,\Omega$，接 0.9 V；(b) $R=180$ k$\Omega$，接 9 V。(c) 证明两个修正公式都能由参考模型得回 1800 $\Omega$。

:::loesung
(a) 电流正确：$U/I=110\,\Omega$，$f=+10\,\%$。电压正确：$U/I=100\,\Omega\parallel200\,\mathrm{k\Omega}=99.95\,\Omega$，$f=-0.05\,\%$。

(b) 电流正确：$U/I=180.01$ k$\Omega$，$f=+0.0056\,\%$。电压正确：$U/I=180\,\mathrm{k\Omega}\parallel200\,\mathrm{k\Omega}=94.74$ k$\Omega$，$f=-47.4\,\%$：流过电压表的电流几乎和流过 $R$ 的一样大（45 µ A 对 50 µ A）。所以小电阻用电压正确的电路，大电阻用电流正确的电路。

(c) $1810\,\Omega-10\,\Omega=1800\,\Omega$，$1/(1/1783.94\,\Omega-1/200\,\mathrm{k\Omega})=1800\,\Omega$。
:::
:::

:::aufgabe 练习 6 ★★★ 误差相等
<span class="anker" id="aufg-6"></span>

$R$ 为多大时两种误差的大小相等？求出精确值，并证明在 $R_\mathrm{iA}\ll R\ll R_\mathrm{iV}$ 时近似有 $R\approx\sqrt{R_\mathrm{iA}R_\mathrm{iV}}$。

:::loesung
$R_\mathrm{iA}/R=R/(R+R_\mathrm{iV})$ 化为 $R^2-R_\mathrm{iA}R-R_\mathrm{iA}R_\mathrm{iV}=0$，其正解为

$$R=\frac{R_\mathrm{iA}}{2}+\sqrt{\frac{R_\mathrm{iA}^2}{4}+R_\mathrm{iA}R_\mathrm{iV}}=1419\,\Omega.$$

$R\ll R_\mathrm{iV}$ 时，右边变为 $R/R_\mathrm{iV}$，所以 $R^2\approx R_\mathrm{iA}R_\mathrm{iV}$，$R\approx1414\,\Omega$。此时两种误差都约为 0.7 %。
:::
:::
