---
title: 第 2 阶段：为什么电流能流过截止的二极管
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 双极型晶体管
order: 1200400
summary: CB 二极管截止，却有毫安级电流流过它。本阶段跟踪电子的路径，并说明为什么只需要很小的基极电流。
tags: 注入, 扩散长度, 传输电流, 放大区
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
CB 二极管截止，却有毫安级电流流过它。本阶段跟踪电子的路径，并说明为什么只需要很小的基极电流。
:::

**基本思路。** 截止的二极管之所以截止，并不是因为边界不可穿透，而是因为 p 侧几乎没有可用的自由电子。空间电荷区的电场会把每个从 p 侧到达边界的电子推到 n 区。对这样的电子来说，边界是一道陡坡（图 [2](#abb-2) 下部）。晶体管恰好提供这些缺少的电子，分四步进行：

<ol>

<li>

⁠**注入。**$U_\mathrm{BE}$ 降低 BE 边界处的势垒。来自发射极的电子进入基极。这一过程称为__注入__。基区靠发射极一侧边缘的电子密度按 $\mathrm{e}^{U_\mathrm{BE}/U_T}$ 增长。

</li>

<li>

⁠**穿越。**在 p 型基区中，电子是大量空穴中的少数。它们向集电极一侧边缘扩散，那里的电子密度几乎为零。基区远窄于__扩散长度__（复合之前的平均路程，几十微米）。因此几乎所有电子都能通过。

</li>

<li>

⁠**抽走。**在集电极一侧边缘，CB 边界的电场捕获每个到达的电子，把它拉入集电极。$U_\mathrm{CB}$ 的大小几乎不起作用，电场总能把电子全部收走。因此 $I_\mathrm{C}$ 几乎不依赖于 $U_\mathrm{CE}$。

</li>

<li>

⁠**补充。**还有两项小的损失：基极的空穴进入发射极，以及一些电子在基区复合。两者都消耗空穴。基极接线端必须补充这些空穴。这种补充就是基极电流。它之所以很小，是因为发射极的掺杂比基极重得多，而且基区很窄。

</li>

</ol>

电子从发射极流向集电极。习惯电流 $I_\mathrm{C}$ 的方向相反，从集电极到发射极（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。

:::abbildung et1/k10basis 2
上：工作点处电子的路径。2.01 mA 的发射极电流分成流向集电极的 2 mA 和流向基极的 10 µ A。下：电子能量随位置的变化（示意）。$U_\mathrm{BE}$ 降低发射极处的小台阶，$U_\mathrm{CB}$ 加深通向集电极的陡坡。
:::

:::satz 定理 2.1 (正常工作时的电流)
<span class="anker" id="satz-2-1"></span>

若 BE 二极管导通且 $U_\mathrm{BE}\gg U_T$，集电极电位高于基极，则

<span class="anker" id="gl-2-1"></span>
$$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T},\qquad I_\mathrm{B}=\frac{I_\mathrm{C}}{B},\qquad I_\mathrm{E}=\Bigl(1+\frac1B\Bigr)I_\mathrm{C}. \tag{2.1}$$
:::

⁠**如何理解：**$I_\mathrm{C}$ 也称为__传输电流__，因为它是穿过基区传输过来的。$I_\mathrm{S}$ 以 A 为单位，非常小，这里是 $1.9\cdot10^{-13}$ A，取决于面积和掺杂。$U_T=k_\mathrm{B}T/e$ 在 300 K 时约为 26 mV。$B$ 没有单位，介于 10 和 1000 之间。它的值取决于掺杂和几何结构，并有离散性：同一型号的不同个体常常相差 2 倍。**适用条件：**__放大区__（第 [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4) 阶段），电流不太大。

:::herleitung 为什么 $I_\mathrm{B}$ 与 $I_\mathrm{C}$ 成正比
电子和空穴越过同一个势垒。基区靠发射极一侧边缘的电子密度和发射区靠基极一侧边缘的空穴密度，都按 $\mathrm{e}^{U_\mathrm{BE}/U_T}$ 增长。集电极电流与前一个密度成正比，基区中的复合也是如此，空穴电流则与后一个密度成正比。所有部分都带有同一个因子，因此它们的比值 $B=I_\mathrm{C}/I_\mathrm{B}$ 与 $U_\mathrm{BE}$ 无关。
:::

**是谁在控制？** 从物理上说，控制的是 $U_\mathrm{BE}$，因为只有电压才能降低势垒。基极电流是为此付出的代价。不过在电路中常常用 $I_\mathrm{B}$ 计算：由于 $I_\mathrm{C}=B\,I_\mathrm{B}$，晶体管的行为就像一个电流控制电流源（CCCS，[第 6 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)）。两种看法描述的是同一个比例关系。用 $U_\mathrm{BE}$ 控制解释了指数定律；当电阻决定基极电流时，用 $I_\mathrm{B}$ 的看法更方便。

::::beispiel
$U_\mathrm{BE}=0.6$ V 给出 $I_\mathrm{C}=1.9\cdot10^{-13}\,\mathrm{A}\cdot\mathrm{e}^{23.08}=2.00$ mA，$I_\mathrm{B}=10$ µ A，$I_\mathrm{E}=2.01$ mA。这相当于集电极中每秒 $1.25\cdot10^{16}$ 个电子，发射极电流的 99.5 % 到达那里。指数函数很敏感：$+18$ mV 使电流加倍（$U_T\ln2$），$+60$ mV 使电流变为十倍（$U_T\ln10$），$+1$ mV 带来 $+3.9$ %。
::::

⁠**极限情况：**$U_\mathrm{BE}=0.4$ V 时只有 0.9 µ A，晶体管实际上已关断。当 $B\to\infty$ 时，$I_\mathrm{B}$ 消失，$I_\mathrm{E}=I_\mathrm{C}$。

:::analogie
一条大水渠被一块活门挡住。来自侧渠的一股细水流把活门推开。没有控制水流就什么也流不过去，控制水流越强，流过的水越多，下方两股水流汇合。这幅图景适用于三点：小的控制大的，没有控制时晶体管截止，$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$。它不适用于机理：晶体管中没有任何东西推动活门，是电压降低了势垒，而且关系是指数型的。
:::

:::frage 输出端多出来的功率从哪里来？
来自电源 $U_\mathrm{CC}$。集电极电流流过整个输出回路，电源因此输出 $U_\mathrm{CC}I_\mathrm{C}$。输入信号只付出 $U_\mathrm{BE}I_\mathrm{B}$，并以此决定电源输出多少。
:::

:::aufgabe 练习 2 ★★ 数电子
<span class="anker" id="aufg-2"></span>

用晶体管 T 计算。 (a) $I_\mathrm{C}=2$ mA 时，每秒有多少电子到达集电极？(b) 5 mA 和 0.5 mA 分别对应多大的 $U_\mathrm{BE}$？差值是多少，为什么它与 $I_\mathrm{S}$ 无关？(c) 另一只晶体管的 $B=50$。发射极电流中有多大比例经基极流出？

:::loesung
(a) $2\,\mathrm{mA}/e=1.25\cdot10^{16}$ 个每秒。 (b) 由 $U_\mathrm{BE}=U_T\ln(I_\mathrm{C}/I_\mathrm{S})$ 得 0.624 V 和 0.564 V。差值为 $U_T\ln10=59.9$ mV。在两个对数之差中，$I_\mathrm{S}$ 被约去。 (c) $I_\mathrm{B}/I_\mathrm{E}=1/(1+B)=1/51=2.0$ %。
:::
:::
