---
title: 第 9 阶段：因果与稳定
pfad: 电气工程 / 第 3 学期 / 信号与系统 / LTI 系统与卷积
order: 3211000
summary: 每个实际系统都应具备的两个性质，可以直接从 h(t) 读出。
tags: 因果, 稳定
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
每个实际系统都应具备的两个性质，可以直接从 $h(t)$ 读出。
:::

:::definition 定义 9.1 (因果、稳定)
<span class="anker" id="satz-9-1"></span>

如果输出不会先于输入出现，则称系统是__因果__的。对于 LTI 系统，这意味着

<span class="anker" id="gl-9-1"></span>
$$h(t)=0\quad\text{对于}\ t<0. \tag{9.1}$$

如果系统对每个有界输入 $|s(t)|\le A<\infty$ 都以有界输出作为响应，则称系统是__稳定__的（更准确地说是 BIBO 稳定，即 *bounded input, bounded output*，有界输入、有界输出）。
:::

因果：时刻 0 的冲激，在这一时刻之前不可能产生任何作用。于是在卷积中只有过去的冲激有贡献，$g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$。

:::satz 定理 9.2 (稳定性条件)
<span class="anker" id="satz-9-2"></span>

LTI 系统稳定，当且仅当其冲激响应绝对可积：

<span class="anker" id="gl-9-2"></span>
$$\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty. \tag{9.2}$$
:::

:::herleitung 稳定性条件
⁠**充分性。**利用积分的三角不等式以及 $|s|\le A$：

$$|g(t)|=\Bigl|\int h(\tau)\,s(t-\tau)\,\mathrm{d}\tau\Bigr|\le\int|h(\tau)|\,|s(t-\tau)|\,\mathrm{d}\tau\le A\int|h(\tau)|\,\mathrm{d}\tau.$$

若该积分有限，则 $g$ 有界。

⁠**必要性。**若 $\int|h|=\infty$，则选取最不利的有界输入：$s(t_1-\tau)=\operatorname{sign}h(\tau)$，即始终取 $\pm1$，且符号与 $h$ 相同。于是 $g(t_1)=\int|h(\tau)|\,\mathrm{d}\tau=\infty$，尽管 $|s|\le1$。
:::

例子：RC 电路的 $\int|h|=1$，是稳定的。理想延时器（$\int|\delta(t-t_0)|\mathrm{d} t=1$）是稳定的。积分器的 $\int_0^\infty\varepsilon\,\mathrm{d} t=\infty$，是不稳定的：它对有界的阶跃输出无界的斜坡 $t\,\varepsilon(t)$。

:::aufgabe 练习 10 ★★ 因果吗？稳定吗？
<span class="anker" id="aufg-10"></span>

研究 (a) $h(t)=\mathrm{e}^{-2t}\varepsilon(t)$，(b) $h(t)=\mathrm{e}^{t}\varepsilon(t)$，(c) $h(t)=\varepsilon(t)-\varepsilon(t-1)$，(d) $h(t)=\mathrm{e}^{-|t|}$，(e) $h(t)=\delta(t+1)$。对于每个不稳定的系统，给出一个会产生无界输出的有界输入。

:::loesung
(a) 因果，$\int|h|=\tfrac12$：稳定。

(b) 因果，$\int_0^\infty\mathrm{e}^t\mathrm{d} t=\infty$：不稳定。阶跃 $\varepsilon(t)$ 产生 $\int_0^t\mathrm{e}^\tau\mathrm{d}\tau=\mathrm{e}^t-1$，它是无界的。

(c) 因果，$\int|h|=1$：稳定。该系统求输入在最近一秒内的积分（滑动窗口）。

(d) 非因果，因为 $t<0$ 时 $h(t)\neq0$。$\int\mathrm{e}^{-|t|}\mathrm{d} t=2$：稳定。

(e) $\delta(t+1)$ 在 $t=-1<0$ 处起作用：$g(t)=s(t+1)$；系统提前一秒就“看到”了输入。非因果，但稳定（$\int|h|=1$）。
:::
:::
