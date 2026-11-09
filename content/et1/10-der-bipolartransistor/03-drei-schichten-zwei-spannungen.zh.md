---
title: 第 1 阶段：三层结构，两个电压
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 双极型晶体管
order: 1200300
summary: 二极管有两个接线端和一条特性曲线。晶体管有三个接线端。本阶段说明它的结构，并数一数有多少个量是自由的。
tags: npn 晶体管, BE 二极管, CB 二极管, pnp 晶体管, 电路符号, 集电极电流, 基极电流, 发射极电流
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
二极管有两个接线端和一条特性曲线。晶体管有三个接线端。本阶段说明它的结构，并数一数有多少个量是自由的。
:::

**基本思路。** __npn 晶体管__由同一种半导体的三个区域构成：n 型掺杂的发射极、p 型掺杂的基极、n 型掺杂的集电极（图 [1](#abb-1)）。发射极掺杂最重，以便发出大量电子。集电极掺杂最轻，以便空间电荷区变宽，能承受高电压。基极位于两者之间，非常窄，约为 1 µ m。这样就形成两个共用基极的 pn 结：__BE 二极管__和 __CB 二极管__。正常工作时，BE 二极管导通，CB 二极管截止。把 n 和 p 对调，就得到 __pnp 晶体管__（第 [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4) 阶段）。在__电路符号__（电路图中的符号）中，带箭头的接线端是发射极。箭头表示习惯电流方向。

:::abbildung et1/k10aufbau 1
左：npn 晶体管的层序和带全部参考箭头的电路符号。右：层序相反的 pnp 晶体管。那里发射极箭头指向元件内部，所有电流和电压都反向。
:::

:::definition 定义 1.1 (npn 晶体管的电流和电压)
<span class="anker" id="satz-1-1"></span>

$I_\mathrm{B}$ 和 $I_\mathrm{C}$ 以流入元件为正，$I_\mathrm{E}$ 以流出元件为正。电压是电位差，第一个下标是正极：$U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$，$U_\mathrm{CE}=\varphi_\mathrm{C}-\varphi_\mathrm{E}$，$U_\mathrm{CB}=\varphi_\mathrm{C}-\varphi_\mathrm{B}$。始终有

<span class="anker" id="gl-1-1"></span>
$$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C},\qquad U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}. \tag{1.1}$$
:::

⁠**如何理解：**$I_\mathrm{C}$ 是__集电极电流__，随类型不同从微安到安培。$I_\mathrm{B}$ 是小得多的__基极电流__，$I_\mathrm{E}$ 是__发射极电流__。$U_\mathrm{BE}$ 加在 BE 二极管上，约为 0.6 V。$U_\mathrm{CE}$ 从约 0.2 V 到几十伏。$U_\mathrm{CB}$ 是 CB 二极管的反向电压。**适用条件：**节点定律和网孔定律在任何工作状态下都成立。

:::herleitung 有多少个量是自由的
有 $n$ 个接线端的元件有 $n$ 个电流。它不储存电荷，所以节点定律（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）消去一个电流。它有 $n$ 个电位，但只有电位差才有意义，所以剩下 $n-1$ 个电压。二极管（$n=2$）有一个电压、一个电流和一条曲线。晶体管（$n=3$）有两个电压和两个电流。其内部通过两个方程把它们联系起来，

$$I_\mathrm{B}=f(U_\mathrm{BE},U_\mathrm{CE}),\qquad I_\mathrm{C}=g(U_\mathrm{BE},U_\mathrm{CE}).$$

所以它是一个二端口网络（[第 6 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)），两个端口共用发射极。
:::

::::beispiel
在参考模型中，$\varphi_\mathrm{E}=0$，$\varphi_\mathrm{B}=0.6$ V，$\varphi_\mathrm{C}=6$ V。于是 $U_\mathrm{BE}=0.6$ V，$U_\mathrm{CE}=6$ V，$U_\mathrm{CB}=5.4$ V。BE 二极管导通，因为它的 p 侧电位较高。CB 二极管截止，因为它的 n 侧电位高出 5.4 V。由 $I_\mathrm{C}=2$ mA 和 $I_\mathrm{B}=10$ µ A 得 $I_\mathrm{E}=2.01$ mA。
::::

⁠**极限情况：**当 $U_\mathrm{CB}=0$ 时，$U_\mathrm{CE}=U_\mathrm{BE}$。正常工作到此为止。

:::frage 我能用两个二极管焊成一个晶体管吗？
不能。两个二极管的等效图只表示边界的极性。在两个分开的二极管中，每个电子早在到达第二个阻挡层之前就复合了，截止的二极管仍然截止。晶体管效应之所以出现，只是因为两个边界之间的距离比电子在 p 区中能存活的距离还短。
:::

:::aufgabe 练习 1 ★ 从电位到电压
<span class="anker" id="aufg-1"></span>

对地测得 $\varphi_\mathrm{E}=1.2$ V，$\varphi_\mathrm{B}=1.85$ V，$\varphi_\mathrm{C}=7$ V，另有 $I_\mathrm{B}=15$ µ A 和 $I_\mathrm{C}=3$ mA。 (a) 求 $U_\mathrm{BE}$、$U_\mathrm{CE}$、$U_\mathrm{CB}$，并验证式 [(1.1)](#gl-1-1)。(b) $I_\mathrm{E}$ 是多少？(c) $\varphi_\mathrm{C}$ 必须降到多少，才能使 $U_\mathrm{CB}=0$？

:::loesung
(a) $U_\mathrm{BE}=0.65$ V，$U_\mathrm{CE}=5.8$ V，$U_\mathrm{CB}=5.15$ V。检验：$5.15\,\mathrm{V}+0.65\,\mathrm{V}=5.8$ V。 (b) $I_\mathrm{E}=3.015$ mA。 (c) $U_\mathrm{CB}=0$ 意味着 $\varphi_\mathrm{C}=\varphi_\mathrm{B}=1.85$ V。
:::
:::
