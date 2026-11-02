---
title: 第 11 阶段：带通中的相位时延与群时延
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 低通与带通系统
order: 3251200
summary: 为什么有两种时延？因为载波和包络可以被延迟不同的时间。
tags: 时延失真
lang: zh
---

<span class="anker" id="stufe-11"></span>

:::zweck
为什么有两种时延？因为载波和包络可以被延迟不同的时间。
:::

**思路。** 设一个带通在通带内模恒定，相位略有弯曲。在 $f_0$ 附近，用相位的切线来近似它：

$$\varphi(f)\approx\varphi(f_0)+(f-f_0)\frac{\mathrm{d}\varphi}{\mathrm{d} f}\Big|_{f_0}=-2\pi f_0t_\mathrm p-2\pi(f-f_0)t_\mathrm g,$$

其中 $t_\mathrm p=t_\mathrm p(f_0)$，$t_\mathrm g=t_\mathrm g(f_0)$，由式 [(1.4)](das-verzerrungsfreie-system.html#gl-1-4) 和式 [(1.5)](das-verzerrungsfreie-system.html#gl-1-5) 给出。在低通域中（$f-f_0\to f$），这就是 $H_T(f)=2\operatorname{rect}(f/\Delta f)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}\,\mathrm{e}^{-\mathrm{j}2\pi ft_\mathrm g}$：一个恒定相位加上一个延迟。

:::satz 定理 11.1 (带通中的时延)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$g_T(t)=s_T(t-t_\mathrm g)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p},\qquad g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm g)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm p)}\bigr\}. \tag{11.1}$$
:::

⁠**如何理解：**携带信息的包络被延迟一个*群时延*。载波被延迟一个*相位时延*。只有当二者相等时，传输才是严格意义上无失真的，也就是说，相位直线通过原点（或在 $f=0$ 处通过 $2\pi$ 的整数倍）。对信息而言，通常只要群时延恒定就够了：若 $t_\mathrm g$ 不恒定，包络的不同频率分量到达的时间不同，脉冲就会展宽（__时延失真__）。

:::ltspice 包络和载波在不同时刻到达
⁠**绘制：**第 [9](bandpasssignal-durch-bandpasssystem.html#stufe-9) 阶段 LTspice 提示中的谐振电路（$f_0=10$ Hz，$\Delta f=2$ Hz）。在 `.ac` 分析中，它在 10 Hz 处的相位为 $0^\circ$，因此 $t_\mathrm p(f_0)=0$。如果把相位坐标轴切换为“Group Delay”，它在 10 Hz 处显示 $t_\mathrm g(f_0)=0.16$ s。

⁠**实验：**输入用行为源 `bv`，即一个包络缓慢变化的载波：

`V=(1+0.5*cos(2*pi*0.2*time))*cos(2*pi*10*time)`

指令 `.tran 0 20 0 0.2m` 和 `.options plotwinsize=0`。

⁠**你会看到：**把 `V(in)` 和 `V(out)` 叠画在一起，并缩放到 14.5 s 至 15.5 s。包络的最大值在输出端晚到约 0.16 s，但载波的过零点与输入端位于相同的位置。这正是式 [(11.1)](#gl-11-1) 所说的：包络被延迟 $t_\mathrm g$，载波被延迟 $t_\mathrm p$。
:::

:::aufgabe 练习 10 ★★ 读出时延
<span class="anker" id="aufg-10"></span>

一个带通在 $f_0=1$ MHz 处的相位为 $\varphi(f_0)=-\pi/2$，斜率为 $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-2\pi\cdot2\,\mu\text{s}$。

<ol class="al">

<li>

计算 $t_\mathrm p$ 和 $t_\mathrm g$。

</li>

<li>

输出端脉冲的包络被延迟了多少？之后载波相对于包络是否仍处于同一位置？

</li>

</ol>

:::loesung
(a) $t_\mathrm p=-\frac{\varphi(f_0)}{2\pi f_0}=\frac{\pi/2}{2\pi\cdot10^6\,\mathrm{Hz}}=0.25$ µ s。$t_\mathrm g=2$ µ s。

(b) 包络晚 2 µ s 到达。载波只移动了 0.25 µ s。因此，它相对于包络转过了 $2\pi f_0(t_\mathrm g-t_\mathrm p)=3.5\pi$，对 $2\pi$ 取模为 $1.5\pi$，即 $-\pi/2$：四分之一周期。只要 $t_\mathrm g$ 在整个频带内恒定，包络中的信息就保持无失真。
:::
:::
