---
title: 第 2 阶段：传输线方程
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 正交展开与传输线
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: 第 8 章：正交展开与传输线
order: 3280300
summary: 到目前为止，导线都被看作理想的连接。如果一条线路的长度与波长相比很长，信号通过它就需要一段可察觉的时间。本阶段建立描述这一现象的方程。
tags: 单位长度参数
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
到目前为止，导线都被看作理想的连接。如果一条线路的长度与波长相比很长，信号通过它就需要一段可察觉的时间。本阶段建立描述这一现象的方程。
:::

**思路。** 把传输线分成长度为 $\mathrm{d} s$ 的许多小段。每一小段都有一个串联电阻和一个串联电感（来自去线和回线），以及一个并联电容和一个并联电导（位于两导线之间）。对于均匀传输线，这些量与长度成正比：$R'\mathrm{d} s$，$L'\mathrm{d} s$，$C'\mathrm{d} s$，$G'\mathrm{d} s$，其中 $R'$、$L'$、$C'$、$G'$ 为__单位长度参数__（分布参数），即每米的值（图 [1](#abb-1)）。

:::abbildung et3/k8element 1
长度为 $\mathrm{d} s$ 的一小段传输线的等效电路，含单位长度参数 $R'$、$L'$、$G'$、$C'$。
:::

:::satz 定理 2.1 (传输线方程（电报方程）)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$\frac{\partial u}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)i,\qquad\frac{\partial i}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)u. \tag{2.1}$$
:::

:::herleitung 传输线方程
对这一小段应用基尔霍夫电压定律：$u=R'\mathrm{d} s\,i+L'\mathrm{d} s\,\frac{\partial i}{\partial t}+\bigl(u+\frac{\partial u}{\partial s}\mathrm{d} s\bigr)$，因此 $\frac{\partial u}{\partial s}\mathrm{d} s=-R'\mathrm{d} s\,i-L'\mathrm{d} s\,\frac{\partial i}{\partial t}$。基尔霍夫电流定律：电流 $i$ 的一部分经 $G'\mathrm{d} s$ 和 $C'\mathrm{d} s$ 流走，$i=G'\mathrm{d} s\,u+C'\mathrm{d} s\,\frac{\partial u}{\partial t}+\bigl(i+\frac{\partial i}{\partial s}\mathrm{d} s\bigr)$。再除以 $\mathrm{d} s$。（严格地说，电流定律中出现的是这一小段末端的电压；二者之差是 $\mathrm{d} s$ 的二阶小量。）
:::

⁠**如何理解：**电压沿传输线下降，因为有电流流过串联元件。电流沿传输线减小，因为它经由导线之间的并联元件漏走。这两个方程在空间和时间上把 $u$ 和 $i$ 耦合起来。
