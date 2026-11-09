---
title: 第 4 阶段：工作中的二端口网络
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 二端口网络
order: 1160600
summary: 工作时没有端口开路。本阶段说明，负载如何通过参数 Z 12 反过来作用于输入端，以及二端口网络对负载而言是什么。
tags: 反向作用, 无反向作用
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
工作时没有端口开路。本阶段说明，负载如何通过参数 $Z_{12}$ 反过来作用于输入端，以及二端口网络对负载而言是什么。
:::

**基本思路。** 负载从端口 2 取用电流，所以 $I_2\neq0$。通过电源 $Z_{12}I_2$，这个电流在输入端表现为一个电压。在 T 形网络中可以直观地看到：本来流过 $R_\mathrm{b}$ 的电流有一部分经 $R_\mathrm{c}$ 分流到负载。$R_\mathrm{b}$ 上的压降减小，$U_1$ 下降，输入端显得电阻更低。输出对输入的这种作用称为__反向作用__。

:::satz 定理 4.1 (输入电阻与输出侧)
<span class="anker" id="satz-4-1"></span>

端口 2 接负载 $Z_\mathrm{L}$ 时，$U_2=-Z_\mathrm{L}I_2$，并且

<span class="anker" id="gl-4-1"></span>
$$I_2=-\frac{Z_{21}}{Z_{22}+Z_\mathrm{L}}\,I_1,\qquad Z_1=\frac{U_1}{I_1}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+Z_\mathrm{L}}. \tag{4.1}$$

极限情况是开路输入电阻和短路输入电阻：

<span class="anker" id="gl-4-2"></span>
$$Z_{1,\mathrm{OC}}=Z_{11},\qquad Z_{1,\mathrm{SC}}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}}. \tag{4.2}$$

如果电源 $U_\mathrm{q}$、$R_\mathrm{q}$ 向端口 1 供电，端口 2 就相当于等效电压源（[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)），其中

<span class="anker" id="gl-4-3"></span>
$$U_\mathrm{i}=\frac{Z_{21}}{Z_{11}+R_\mathrm{q}}\,U_\mathrm{q},\qquad R_\mathrm{i}=Z_{22}-\frac{Z_{12}Z_{21}}{Z_{11}+R_\mathrm{q}}. \tag{4.3}$$
:::

⁠**如何理解：**$Z_\mathrm{L}$ 是负载，这里是一个电阻。$U_2=-Z_\mathrm{L}I_2$ 中的负号是因为 $I_2$ 指向二端口网络内部，与流过负载的电流方向相反。式 [(4.1)](#gl-4-1) 中的分式就是负载改变输入电阻的量。$Z_{12}=0$ 时它为零：输入端察觉不到负载，这样的二端口网络称为__无反向作用__网络。**适用条件：**二端口网络必须是线性的，等效电源的公式要求电源是线性的。

:::herleitung 输入电阻与输出侧
右网孔：$U_2=Z_{21}I_1+Z_{22}I_2=-Z_\mathrm{L}I_2$，解出 $I_2$ 得式 [(4.1)](#gl-4-1) 的第一部分。代入左网孔 $U_1=Z_{11}I_1+Z_{12}I_2$ 并除以 $I_1$ 得 $Z_1$。$Z_\mathrm{L}\to\infty$ 时分式消失，$Z_\mathrm{L}=0$ 时由 $I_2=-Z_{21}I_1/Z_{22}$ 得 $Z_{1,\mathrm{SC}}$。

对式 [(4.3)](#gl-4-3)，要替换负载。电源规定 $U_1=U_\mathrm{q}-R_\mathrm{q}I_1$。$I_2=0$ 时，$I_1=U_\mathrm{q}/(Z_{11}+R_\mathrm{q})$，$U_\mathrm{i}=Z_{21}I_1$。$U_\mathrm{q}=0$ 时，端口 1 由 $R_\mathrm{q}$ 端接，$R_\mathrm{i}$ 就是下标互换后的 $Z_1$。
:::

:::abbildung et1/k6betrieb 5
带电源和负载的 T 形网络等效电路。电流为 $I_1=250$ mA 和 $I_2=-50$ mA。反向作用为 $Z_{12}I_2=-1$ V，正向电源提供 $Z_{21}I_1=5$ V。输入端呈现 31 $\Omega$ 而不是 35 $\Omega$。
:::

::::beispiel
对 T 形网络，$Z_{1,\mathrm{OC}}=35\,\Omega$，$Z_{1,\mathrm{SC}}=35\,\Omega-400\,\Omega^2/40\,\Omega=25\,\Omega$，这就是 $R_\mathrm{a}+R_\mathrm{b}\parallel R_\mathrm{c}$。取 $R_\mathrm{L}=60\,\Omega$，得

$$Z_1=35\,\Omega-\frac{400\,\Omega^2}{100\,\Omega}=31\,\Omega,\quad I_1=\frac{9\,\mathrm{V}}{5\,\Omega+31\,\Omega}=250\,\mathrm{mA},\quad I_2=-\frac{20}{100}\,I_1=-50\,\mathrm{mA}.$$

输入端 $U_1=9\,\mathrm{V}-5\,\Omega\cdot250\,\mathrm{mA}=7.75$ V，输出端 $U_2=60\,\Omega\cdot50\,\mathrm{mA}=3$ V。$R_\mathrm{b}$ 中流过 $I_1+I_2=200$ mA 而不是 250 mA，这使 $U_1$ 恰好降低 1 V（图 [5](#abb-5)）。从负载看：$U_\mathrm{i}=\frac{20}{40}\cdot9\,\mathrm{V}=4.5$ V，$R_\mathrm{i}=40\,\Omega-400\,\Omega^2/40\,\Omega=30\,\Omega$。于是 $I=4.5\,\mathrm{V}/90\,\Omega=50$ mA，是同一个电流。可见[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)的等效电源就包含在这四个数中。
::::

⁠**极限情况：**$R_\mathrm{L}\to\infty$ 得 $Z_1\to35\,\Omega$，$R_\mathrm{L}\to0$ 得 $25\,\Omega$。任何负载都介于两者之间。

:::frage 负载只接在端口 2 上。输入端怎么知道它？
通过公共元件。在 T 形网络中，两个端口的电流都流过 $R_\mathrm{b}$，其压降取决于 $I_1+I_2$。一般而言，$Z_{12}$ 是这种耦合的度量。这里不需要信号往回传输，网络中的电压是共同建立的。
:::

:::ltspice 工作中的 T 形网络
⁠**绘制：**电压源 `voltage` 取 `9`，从 `q` 接地，`res` 取 `5`，从 `q` 接到 `1`，`Ra` 取 `15`，从 `1` 接到 `m`，`Rb` 取 `20`，从 `m` 接地，`Rc` 取 `20`，从 `m` 接到 `2`，`RL` 取 `{RL}`，从 `2` 接地。

⁠**指令：**`.param RL=60`，`.op`，`.meas op Uin FIND V(1)`，`.meas op Iin FIND I(Ra)`，`.meas op Zin PARAM Uin/Iin`，`.meas op Uout FIND V(2)`。

⁠**你会看到：**$\mathtt{V(1)}=7.75$ V，$\mathtt{I(Ra)}=250$ mA，`Zin` $=31\,\Omega$，$\mathtt{V(2)}=3$ V。取 `RL=1m` 时 `Zin` 变为 25.0 $\Omega$，取 `RL=1G` 时变为 35.0 $\Omega$，且 $\mathtt{V(2)}=4.5$ V，即电压 $U_\mathrm{i}$。设 `RL=10`，检验练习 [4](#aufg-4)(a) 和 (c)。
:::

:::aufgabe 练习 4 ★★ T 形网络上的负载
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

$R_\mathrm{L}=10\,\Omega$ 时 $Z_1$ 是多少？

</li>

<li>

负载为多少时，输入端呈现 $Z_1=30\,\Omega$？

</li>

<li>

对 $R_\mathrm{L}=10\,\Omega$，接上电源，计算电流 $I_1$、$I_2$ 和 $U_2$。用等效电源检验负载电流。

</li>

</ol>

:::loesung
(a) $Z_1=35\,\Omega-400\,\Omega^2/50\,\Omega=27\,\Omega$。 (b) $400\,\Omega^2/(40\,\Omega+R_\mathrm{L})=5\,\Omega$，所以 $R_\mathrm{L}=40\,\Omega$。 (c) $I_1=9\,\mathrm{V}/32\,\Omega=281.25$ mA，$I_2=-\frac{20}{50}I_1=-112.5$ mA，$U_2=1.125$ V。等效电源给出 $4.5\,\mathrm{V}/(30\,\Omega+10\,\Omega)=112.5$ mA。
:::
:::
