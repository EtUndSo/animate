---
title: 第 9 阶段：希尔伯特变换与解析信号
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 傅里叶级数与变换
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: 第 3 章：傅里叶级数与变换
order: 3231000
summary: 对于因果信号，频谱的实部与虚部相互关联：一个决定另一个。同样的计算还能得到一个只含正频率的信号。
tags: 希尔伯特变换, 解析分量, 全通
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
对于因果信号，频谱的实部与虚部相互关联：一个决定另一个。同样的计算还能得到一个只含正频率的信号。
:::

**因果信号。** 若 $t<0$ 时 $s(t)=0$，则偶部和奇部在 $t>0$ 时相等（均为 $\frac12s$），在 $t<0$ 时互为相反数。因此 $s_u(t)=s_g(t)\operatorname{sgn}(t)$，$s_g(t)=s_u(t)\operatorname{sgn}(t)$。在频域中，乘以 $\operatorname{sgn}$ 变为与 $\frac{1}{\mathrm{j}\pi f}$ 卷积：

:::satz 定理 9.1 (因果信号的希尔伯特关系)
<span class="anker" id="satz-9-1"></span>

对因果信号，

<span class="anker" id="gl-9-1"></span>
$$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f},\qquad\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}. \tag{9.1}$$
:::

⁠**如何理解：**与 $\frac{1}{\pi f}$ 的卷积称为__希尔伯特变换__。对于因果系统，只要知道频率响应的实部就够了，虚部可由它求出。因此，因果性是对频谱的一个很强的约束。

**解析分量。** 利用*频域*中的阶跃，可以截去负频率：$S_+(f)=S(f)\,\varepsilon(f)$。由对偶性得 $\varepsilon(f)\;\bullet\!\!-\!\!\circ\;\frac12\delta(t)+\frac{\mathrm{j}}{2\pi t}$，因此

<span class="anker" id="gl-9-2"></span>
$$s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t),\qquad\hat s(t)=s(t)*\frac{1}{\pi t}\;\circ\!\!-\!\!\bullet\;-\mathrm{j}\operatorname{sgn}(f)\,S(f). \tag{9.2}$$

$s_+$ 称为__解析分量__，$\hat s$ 称为 $s$ 的希尔伯特变换。对实信号有 $S_-(f)=S_+^*(-f)$，因此 $s_-=s_+^*$，且 $s(t)=s_++s_-=2\operatorname{Re}\{s_+(t)\}$。$s_+$ 的实部与虚部同样互为希尔伯特变换。

**希尔伯特变换器。** $h(t)=\frac{1}{\pi t}$ 的 LTI 系统具有 $H(f)=-\mathrm{j}\operatorname{sgn}(f)$：在所有频率上模均为 1（__全通__系统），$f>0$ 时相位为 $-90^\circ$，$f<0$ 时为 $+90^\circ$。它把 $\cos(2\pi Ft)$ 变为

$$\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr]\cdot\bigl(-\mathrm{j}\operatorname{sgn}(f)\bigr)=\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F)\;\bullet\!\!-\!\!\circ\;\sin(2\pi Ft).$$

⁠**简而言之：**希尔伯特变换器把每个振荡的相位移动 $90^\circ$，而不改变其幅度。

:::aufgabe 练习 12 ★★ 希尔伯特变换器
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

希尔伯特变换器把 $\sin(2\pi Ft)$ 变成什么？应用两次得到什么？

</li>

<li>

求 $\cos(2\pi Ft)$ 的解析分量 $s_+(t)$，并验证 $s=2\operatorname{Re}\{s_+\}$。

</li>

<li>

为什么希尔伯特变换器不是因果的？请看 $h(t)$。

</li>

</ol>

:::loesung
(a) $\sin(2\pi Ft)\circ\!\!-\!\!\bullet\frac{\mathrm{j}}{2}\delta(f+F)-\frac{\mathrm{j}}{2}\delta(f-F)$。乘以 $-\mathrm{j}\operatorname{sgn}(f)$：在 $-F$ 处乘以 $+\mathrm{j}$，在 $+F$ 处乘以 $-\mathrm{j}$。结果：$-\frac12\delta(f+F)-\frac12\delta(f-F)$，即 $-\cos(2\pi Ft)$。应用两次：$(-\mathrm{j}\operatorname{sgn}f)^2=-1$，因此信号被反相。

(b) $S_+(f)=S(f)\varepsilon(f)=\frac12\delta(f-F)$，所以 $s_+(t)=\frac12\mathrm{e}^{\mathrm{j}2\pi Ft}=\frac12\bigl[\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft)\bigr]$。这与 $\frac12(s+\mathrm{j}\hat s)$（其中 $\hat s=\sin$）一致。$2\operatorname{Re}\{s_+\}=\cos(2\pi Ft)$。

(c) $h(t)=\frac{1}{\pi t}$ 在 $t<0$ 时也不为零。因此，时刻 $t$ 的输出取决于未来的输入值。实际中，用截断的冲激响应来近似希尔伯特变换器，代价是引入一段延迟。
:::
:::
