---
title: 第 4 阶段：无损传输线
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 正交展开与传输线
order: 3280500
summary: 没有损耗（ R'=G'=0 ）时，特性阻抗和传播速度都与频率无关。于是波动解对任意信号都成立，而不仅限于正弦信号。
tags: 
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
没有损耗（$R'=G'=0$）时，特性阻抗和传播速度都与频率无关。于是波动解对任意信号都成立，而不仅限于正弦信号。
:::

当 $R'=G'=0$ 时，$\gamma=\mathrm{j}2\pi f\sqrt{L'C'}$：没有衰减（$\alpha=0$），且 $\beta$ 与 $f$ 成正比。由此得：

<span class="anker" id="gl-4-1"></span>
$$Z=\sqrt{\frac{L'}{C'}},\qquad v=\frac{1}{\sqrt{L'C'}},\qquad\frac{\partial^2u}{\partial s^2}=L'C'\frac{\partial^2u}{\partial t^2}. \tag{4.1}$$

:::satz 定理 4.1 (达朗贝尔解)
<span class="anker" id="satz-4-1"></span>

波动方程 [(4.1)](#gl-4-1) 的每个解都具有形式

<span class="anker" id="gl-4-2"></span>
$$u(s,t)=u_\mathrm{fw}(s-vt)+u_\mathrm{bw}(s+vt) \tag{4.2}$$

其中 $u_\mathrm{fw}$（正向）和 $u_\mathrm{bw}$（反向）是任意（二次可微的）函数。
:::

⁠**如何理解：**任意的信号波形都以速度 $v$ 沿传输线不变地传播。这是因为所有频率分量都同样快，衰减也同样小：传输线是[第 5 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)意义上的无失真系统，时延为 $l/v$。$u$ 的波动方程可由式 [(2.1)](die-leitungsgleichungen.html#gl-2-1) 得到：把第一个方程对 $s$ 求导，把第二个方程对 $t$ 求导，再消去 $i$。

**例：同轴电缆。** 由 $Z=50\,\Omega$ 和 $C'=100$ pF/m 得 $L'=Z^2C'=250$ nH/m 以及 $v=\frac{1}{\sqrt{L'C'}}=2\cdot10^8$ m/s，即光速的三分之二（由于电缆中的电介质）。信号通过 10 m 电缆需要 50 ns。若电缆终端接的是 75 $\Omega$ 而不是 50 $\Omega$，则 $r=\frac{75-50}{75+50}=0.2$：电压幅度的 20 % 作为回波返回。

:::ltspice 传输线上的反射
⁠**绘制：**电压源 `voltage`，取 `PULSE(0 2 0 1n 1n 10n 1)`，内阻 `res` 取 `50`，接到节点 `in`。从 `in` 引出一条无损传输线 `tline`，取 `Td=50n Z0=50`（例子中 10 m 长的同轴电缆），接到节点 `end`，在那里接 `res`，取 `{RE}`，接地。由于内阻等于 $Z$，出发的是一个 1 V 的波，而回波在信号源处被完全吸收。

⁠**指令：**`.param RE=75`，`.step param RE list 1m 50 75 1G`（几乎短路、匹配、75 $\Omega$、几乎开路），`.tran 0 200n 0 0.1n`。

⁠**你会看到：**在 `in` 处，首先是 1 V 的脉冲。经过 $2\cdot50\,\mathrm{ns}=100$ ns 后，回波以高度 $r\cdot1$ V 返回：$-1$、$0$、$0.2$ 和 $+1$，恰好是 $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$。在 `end` 处，50 ns 后出现的是正向波与反向波之和，$(1+r)\cdot1$ V。把 `Td` 和 `Z0` 设为你在练习 [4](#aufg-4)(a) 中得到的值，把 `RE` 设为 100，并把回波高度与你在练习 [4](#aufg-4)(b) 中的结果比较。
:::

:::aufgabe 练习 3 ★★ 验证达朗贝尔解
<span class="anker" id="aufg-3"></span>

通过代入证明：$u(s,t)=u_\mathrm{fw}(s-vt)$ 在 $v=1/\sqrt{L'C'}$ 时是波动方程 [(4.1)](#gl-4-1) 的解。相应的电流与电压有什么关系？提示：利用 $R'=0$ 时的第一个传输线方程。

:::loesung
令 $x=s-vt$：$\frac{\partial^2u}{\partial s^2}=u_\mathrm{fw}''(x)$，$\frac{\partial^2u}{\partial t^2}=v^2u_\mathrm{fw}''(x)$。波动方程要求 $u''=L'C'v^2u''$，因此 $v^2=\frac{1}{L'C'}$。电流：当 $R'=0$ 时，$\frac{\partial u}{\partial s}=-L'\frac{\partial i}{\partial t}$，因此 $u_\mathrm{fw}'(x)=-L'\frac{\partial i}{\partial t}$。设 $i=u_\mathrm{fw}(x)/Z$，得 $\frac{\partial i}{\partial t}=-\frac vZu'_\mathrm{fw}$；由于 $L'v/Z=L'\cdot\frac{1}{\sqrt{L'C'}}\cdot\sqrt{\frac{C'}{L'}}=1$，二者是一致的。在正向行波中，电压与电流处处之比为 $Z$。
:::
:::

:::aufgabe 练习 4 ★★ 电缆与终端负载
<span class="anker" id="aufg-4"></span>

一条无损电缆的 $L'=300$ nH/m，$C'=120$ pF/m。

<ol class="al">

<li>

计算 $Z$、$v$ 以及 5 m 电缆的传播时延。

</li>

<li>

终端必须接多大的电阻，才不会产生反射？终端接 100 $\Omega$ 时，反射系数是多少？

</li>

<li>

若要求线长至多为波长的十分之一，那么 5 m 电缆在多高的频率以下仍可视为“短”线？

</li>

</ol>

:::loesung
(a) $Z=\sqrt{300/120}\cdot\sqrt{\frac{\text{nH}}{\text{pF}}}=\sqrt{2.5\cdot10^3}\,\Omega=50\,\Omega$。$v=\frac{1}{\sqrt{300\cdot10^{-9}\cdot120\cdot10^{-12}}}\,\mathrm{m/s}=\frac{1}{\sqrt{3.6\cdot10^{-17}}}\,\mathrm{m/s}=1.67\cdot10^8$ m/s。5 m 的传播时延：30 ns。

(b) 接 $Z=50\,\Omega$ 的电阻。接 100 $\Omega$ 时：$r=\frac{100-50}{150}=\frac13$。

(c) $\lambda=v/f\ge50$ m，因此 $f\le\frac{1.67\cdot10^8}{50}\,\mathrm{Hz}=3.3$ MHz。
:::
:::
