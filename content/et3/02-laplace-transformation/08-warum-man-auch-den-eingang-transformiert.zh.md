---
title: 第 5 阶段：为什么输入也要变换
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 拉普拉斯变换
order: 3220800
summary: 每个信号都是 $\mathrm{e}^{pt}$ 的叠加， 以及为什么 LTI 系统的作用因此变成乘法
tags: 
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::frage 对 $h(t)$ 作变换是有用的：$H(p)$ 与特征函数相乘，由此得到输出。但为什么还要对输入信号 $s(t)$ 作变换？虽然 $s*h=h*s$，但 $h(t)$ 通常不是特征函数，所以 $h(t)\cdot S(p)$ 没有意义。对任意信号作变换，对系统有什么意义？
⁠**问题中正确的部分：**$H(p)$ 说明系统对基本分量 $\mathrm{e}^{pt}$ 做了什么。而 $h(t)\cdot S(p)$ 确实没有意义。

⁠**推理错在哪里：**输入几乎也从来不是特征函数。阶跃、语音信号或矩形脉冲都不是单个基本分量 $\mathrm{e}^{pt}$。因此 $H(p)\cdot s(t)$ 和 $h(t)\cdot S(p)$ 一样没有意义：$H(p)$ 只能作用于一个基本分量，而对任意的 $s(t)$，甚至不清楚指的是哪个 $p$。在 $H(p)$ 能起任何作用之前，必须先把输入分解为基本分量。这正是 $S(p)$ 所做的事。

⁠**正确的看法：**在卷积定理 $G(p)=H(p)\,S(p)$ 中，每个因子都有其自身的系统含义：

<ul>

<li>

$S(p)$ 是*输入的“配方”*：输入中含有多少基本分量 $\mathrm{e}^{pt}$；

</li>

<li>

$H(p)$ 是*系统的作用*：系统把这个基本分量乘以的那个数；

</li>

<li>

$G(p)$ 是输出的“配方”。

</li>

</ul>

没有 $S(p)$，你只知道系统对各个基本分量的作用，却不知道到达的是哪些基本分量。$H(p)$ 单独只能在一种特殊情况下回答“输出端会发生什么？”这个问题：输入本身就是单个基本分量。

⁠**例：阶跃与 RC 低通滤波器。**阶跃的配方是 $S(p)=1/p$。在直线 $\sigma=0.5/\mathrm s$ 上，$f=0$ 时 $|S|=2$，1 Hz 时为 $0.16$，10 Hz 时为 $0.016$。快速基本分量很弱，但确实存在，正是它们构成了陡峭的边沿（图 [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3)：快速基本分量越多，边沿越陡）。RC 低通滤波器把它们分别乘以 $|H|=0.67$、$0.15$ 和 $0.016$。因此在输出中，快速基本分量又被削弱了大约 $2\pi f\cdot RC$ 倍（对于 $f\gg1/(2\pi RC)=0.16$ Hz），边沿也就消失了：$g(t)=1-\mathrm{e}^{-t}$ 连续上升。这一解释需要两个变换。$H$ 单独只能说明“快速基本分量被削弱”；只有 $S$ 才说明边沿由快速基本分量构成。

⁠**那么对称性 $s*h=h*s$ 呢？**在数学上，两个信号地位平等：也可以把 $h$ 看作输入、把 $s$ 看作“系统”，这时 $H(p)$ 是配方，$S(p)$ 是作用。系统理论只是根据物理意义来分配角色：一个信号来自外部，另一个描述电路。在变换域中，*两者*总是都要被变换。
:::

**单独变换一个信号的其他理由。**

<ul>

<li>

⁠**测量一个系统。**若测出一个未知系统的输入和输出，$H(p)=G(p)/S(p)$ 就给出了这个系统。为此要对两个信号分别作变换（练习 [9](#aufg-9)）。

</li>

<li>

⁠**理解信号本身。**敲钟发出的声音是若干衰减振荡之和，每个振荡对应一对共轭极点。$\operatorname{Im} p_r$ 是某个分音的音高，$-\operatorname{Re} p_r$ 是它的衰减率。少数几个极点就描述了整个声音。显示频谱的仪器在直线 $\sigma=0$ 上做的是同样的事。

</li>

<li>

⁠**没有系统的卷积。**卷积把一个信号经过平移和加权的副本叠加起来。系统只是这种运算的一种解释，而不是唯一的解释。一个完全不涉及系统的例子是两个骰子的点数之和，见关于卷积的练习册（[第 1 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)）。

</li>

</ul>

:::ltspice 符合两次测量的网络
⁠**绘制：**你在练习 [9](#aufg-9)(c) 中找到的网络，输入端接信号源 `PULSE(0 1 0 1u 1u 100)`，输出接节点 `out`。旁边放一个不与电路相连的行为源 `bv`，接在节点 `mess` 上，取 `V=1-exp(-2*time)`。它充当测得的输出曲线。

⁠**指令：**`.tran 0 3 0 1m`，`.meas tran dev MAX abs(V(out)-V(mess))`。

⁠**你会看到：**如果网络和元件值都正确，`V(out)` 和 `V(mess)` 就重合在一起，最大偏差 `dev` 实际上为零（小于 $10^{-5}$）。用这种方法，把这些曲线与你在练习 [9](#aufg-9)(c) 中的结果比较。
:::

:::aufgabe 练习 8 ★★ 哪些基本分量构成了边沿？
<span class="anker" id="aufg-8"></span>

输入 $\varepsilon(t)$，系统：$RC=1$ s 的 RC 低通滤波器。考虑直线 $\sigma=0.5/\mathrm s$ 上的基本分量。

<ol class="al">

<li>

对 $f=0$、$1$ Hz 和 $10$ Hz，计算 $|S(p)|$、$|H(p)|$ 和 $|G(p)|$。

</li>

<li>

与 1 Hz 处的基本分量相比，系统对 10 Hz 处的基本分量多削弱了多少倍？

</li>

<li>

利用 (a) 和图 [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3) 解释为什么输出没有边沿。为什么仅凭 $H(p)$ 不足以作出这一解释？

</li>

</ol>

:::loesung
(a) 令 $p=0.5+\mathrm{j}2\pi f$（单位 $1/\mathrm s$），$S=1/p$，$H=1/(p+1)$，$G=SH$：

| $f$ | $\vert S(p)\vert $ | $\vert H(p)\vert $ | $\vert G(p)\vert $ |
|---|---|---|---|
| 0 | 2 | 0.667 | 1.33 |
| 1 Hz | 0.159 | 0.155 | 0.0246 |
| 10 Hz | 0.0159 | 0.0159 | 0.000253 |

(b) $0.155/0.0159\approx9.7$，即差不多是 10 倍，与频率之比一样。对于大的 $|p|$，$|H|\approx1/|p|\approx1/(2\pi f)$。

(c) 阶跃的边沿由快速基本分量构成：在图 [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3) 中，包含的快速基本分量越多，边沿越陡。在输入中，它们的权重按 $1/f$ 下降，在输出中按 $1/f^2$ 下降。在输出中，快速基本分量弱到不再形成边沿，$g(t)$ 连续上升。$H(p)$ 单独只说明快速基本分量被削弱。边沿恰恰由这些基本分量构成，这是关于输入的结论，而这一结论包含在 $S(p)$ 中。
:::
:::

:::aufgabe 练习 9 ★★ 由两次测量确定未知系统
<span class="anker" id="aufg-9"></span>

在 $t=0$ 时刻，向一个未知的因果 LTI 系统施加 1 V 电压，$s(t)=\varepsilon(t)$（单位 V）。在输出端测得 $g(t)=\bigl(1-\mathrm{e}^{-2t}\bigr)\varepsilon(t)$（单位 V，$t$ 的单位为 s）。

<ol class="al">

<li>

对两个信号分别作变换。

</li>

<li>

求 $H(p)$，并由此求 $h(t)$。

</li>

<li>

它可能是什么网络？得到什么参数值？

</li>

<li>

$G(p)$ 中哪个极点来自输入，哪个来自系统？

</li>

</ol>

:::loesung
(a) $S(p)=\dfrac1p$，$\operatorname{Re} p>0$。$G(p)=\dfrac1p-\dfrac{1}{p+2}=\dfrac{2}{p(p+2)}$，$\operatorname{Re} p>0$（基本变换对 [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2)，取 $p_0=0$ 和 $p_0=-2$）。

(b) $H(p)=\dfrac{G(p)}{S(p)}=\dfrac{2}{p+2}$。由于系统是因果的，收敛域位于极点右侧：$\operatorname{Re} p>-2$。由 [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2)：$h(t)=2\,\mathrm{e}^{-2t}\varepsilon(t)$，单位为 $1/\mathrm s$。

(c) RC 低通滤波器的 $H(p)=\dfrac{1}{1+pRC}=\dfrac{1/RC}{p+1/RC}$。与 $\dfrac{2}{p+2}$ 比较得 $RC=0.5$ s，例如 $R=500\,\mathrm{k\Omega}$，$C=1$ µ F。（任何具有相同传递函数的其他网络，在端口处的表现都完全相同。输入端和输出端的测量只能揭示 $H$，而不能揭示元件。）

(d) 极点 $p=0$ 来自输入（阶跃），极点 $p=-2$ 来自系统。在除法 $G/S$ 中，被约去的恰好是输入的极点。
:::
:::
