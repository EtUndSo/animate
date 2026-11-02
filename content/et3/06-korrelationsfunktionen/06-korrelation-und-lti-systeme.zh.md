---
title: 第 5 阶段：相关与 LTI 系统
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 相关函数
order: 3260600
summary: LTI 系统对自相关函数和能量谱密度有什么作用？怎样用互相关来测量一个系统？
tags: 
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
LTI 系统对自相关函数和能量谱密度有什么作用？怎样用互相关来测量一个系统？
:::

:::satz 定理 5.1 (维纳–李关系)
<span class="anker" id="satz-5-1"></span>

对于 $g=s*h$：

<span class="anker" id="gl-5-1"></span>
$$\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)\;\circ\!\!-\!\!\bullet\;|G(f)|^2=|S(f)|^2\,|H(f)|^2, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*h(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,H(f). \tag{5.2}$$
:::

:::herleitung 维纳–李关系
$\varphi^E_{gg}=g^*(-\tau)*g(\tau)=[s^*(-\tau)*h^*(-\tau)]*[s(\tau)*h(\tau)]$。利用交换律和结合律重新排列：$[s^*(-\tau)*s(\tau)]*[h^*(-\tau)*h(\tau)]=\varphi^E_{ss}*\varphi^E_{hh}$。同理，$\varphi^E_{sg}=s^*(-\tau)*s(\tau)*h(\tau)$。
:::

⁠**如何理解：**系统把每个频率上的能量乘以 $|H|^2$。系统的相位对能量没有影响。式 [(5.2)](#gl-5-2) 是一种测量方法：若输入的自相关函数几乎是一个加权狄拉克冲激 $c\,\delta(\tau)$（非常短的脉冲或宽带噪声，[第 7 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)），则输入与输出之间的互相关函数几乎就是 $c\,h(\tau)$，即除因子 $c$ 外就是冲激响应。与 $|H|^2$ 不同，它还包含相位。

:::ltspice RC 电路前后的能量
⁠**绘制：**行为源 `bv` 接在节点 `s` 上，取 `V=exp(-time)*(time>0)`，即指数脉冲 $\varepsilon(t)\mathrm{e}^{-t}$。因子 `(time>0)` 使 LTspice 以 0 V 计算 $t=0$ 时的初始状态，因此电容从未充电的状态开始。其后接 RC 电路（`res` 取 `1Meg`，`cap` 取 `1u`），输出接节点 `g`。

⁠**指令：**`.tran 0 30 0 1m`，以及用来求式 [(1.1)](energie-und-leistung.html#gl-1-1) 中能量的 `.meas tran Es INTEG V(s)*V(s)` 和 `.meas tran Eg INTEG V(g)*V(g)`。

⁠**你会看到：**`Es` $=0.500$，与第 [4](energiedichtespektrum.html#stufe-4) 阶段中的 $E_s=\varphi^E_{ss}(0)=\frac12$ 一致。把 `Eg` 与你在练习 [5](#aufg-5) 中的结果比较。输出能量较小，因为 RC 电路把每个频率上的能量乘以 $|H|^2\le1$。
:::

:::aufgabe 练习 5 ★★ 输出端的能量
<span class="anker" id="aufg-5"></span>

指数脉冲 $\varepsilon(t)\mathrm{e}^{-t}$ 通过一个 $RC=1$ s 的 RC 电路。

<ol class="al">

<li>

求 $|G(f)|^2$，并由此求输出能量。提示：$\int_{-\infty}^\infty\frac{\mathrm{d} x}{(1+x^2)^2}=\frac\pi2$。

</li>

<li>

用 $g(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$ 在时域中验证（[第 1 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)，两个级联的 RC 电路）。

</li>

</ol>

:::loesung
(a) $|G|^2=|S|^2|H|^2=\frac{1}{(1+(2\pi f)^2)^2}$。令 $x=2\pi f$：$E_g=\frac{1}{2\pi}\int\frac{\mathrm{d} x}{(1+x^2)^2}=\frac{1}{2\pi}\cdot\frac\pi2=\frac14$。

(b) $\int_0^\infty t^2\mathrm{e}^{-2t}\mathrm{d} t=\frac{2}{2^3}=\frac14$。两种方法的结果一致。能量从 $\frac12$ 降到 $\frac14$，因为第二个 RC 电路进一步衰减了较高的频率。
:::
:::
