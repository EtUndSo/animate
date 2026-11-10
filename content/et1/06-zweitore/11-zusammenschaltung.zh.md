---
title: 第 9 阶段：互联
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 二端口网络
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: 第 6 章：二端口网络
order: 1161100
summary: 第 8 阶段表明，级联适合 A 形式。本阶段一般地回答这个问题：哪种形式适合哪种互联？
tags: 
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
第 [8](kettenform.html#stufe-8) 阶段表明，级联适合 A 形式。本阶段一般地回答这个问题：哪种形式适合哪种互联？
:::

**基本思路。** 连接两个二端口网络时，它们在每个端口要么共享电流（串联），要么共享电压（并联）。共享的量对两部分相同，另一个量相加。这就说明了哪种形式合适：共同的量属于原因，相加的量属于结果。这样，右边对两部分都相同，参数就相加。

:::satz 定理 9.1 (两个二端口网络的互联)
<span class="anker" id="satz-9-1"></span>

如果两部分都保持端口条件，则有：

| 连接（端口 1，端口 2） | 两部分相同 | 相加 | 规则 |
|---|---|---|---|
| 串联，串联 | $I_1$，$I_2$ | $U_1$，$U_2$ | $\mathbf Z=\mathbf Z'+\mathbf Z''$ |
| 并联，并联 | $U_1$，$U_2$ | $I_1$，$I_2$ | $\mathbf Y=\mathbf Y'+\mathbf Y''$ |
| 串联，并联 | $I_1$，$U_2$ | $U_1$，$I_2$ | $\mathbf H=\mathbf H'+\mathbf H''$ |
| 级联 | $U_2'=U_1''$，$-I_2'=I_1''$ | 无 | $\mathbf A=\mathbf A'\mathbf A''$ |
:::

⁠**如何理解：**电路图说明哪些量相同，表格说明哪种形式相加（图 [11](#abb-11)）。H 矩阵的第二个名称串并联矩阵就由此而来。“并联，串联”这种连接是缺少的情况。与之对应的是以 $U_1$ 和 $I_2$ 为原因的逆混合形式，可由 $\mathbf H$ 的逆矩阵得到。

:::herleitung 为什么参数相加
串联，串联时，两部分流过相同的电流：$\mathbf I'=\mathbf I''=\mathbf I$。所以 $\mathbf U=\mathbf U'+\mathbf U''=\mathbf Z'\mathbf I+\mathbf Z''\mathbf I=(\mathbf Z'+\mathbf Z'')\mathbf I$。并联时同理，只是角色互换。串联，并联时，原因列 $(I_1,\,U_2)$ 对两部分相同，结果列 $(U_1,\,I_2)$ 是两个结果列之和。
:::

:::abbildung et1/k6zusammen 11
三种互联。左为串联，串联：电流相同，Z 相加。中为并联，并联：电压相同，Y 相加。右为串联，并联：$I_1$ 和 $U_2$ 相同，H 相加。
:::

::::beispiel
⁠**串联：**T 形网络本身就是两个分开的串联电阻和一个并联电阻的串联连接：

$$\mathbf Z=\begin{pmatrix}15&0\\0&20\end{pmatrix}\Omega+\begin{pmatrix}20&20\\20&20\end{pmatrix}\Omega=\begin{pmatrix}35&20\\20&40\end{pmatrix}\Omega.$$
::::

⁠**并联：**在 T 形网络上从接线端 1 到接线端 2 跨接一个 100 $\Omega$ 的电阻，$\mathbf Y$ 就加上串联电导：

$$\mathbf Y=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS}+\begin{pmatrix}10&-10\\-10&10\end{pmatrix}\mathrm{mS}=\begin{pmatrix}50&-30\\-30&45\end{pmatrix}\mathrm{mS}.$$

检验：端口 2 短路时 $1/Y_{11}=20\,\Omega$，直接计算是 $25\,\Omega\parallel100\,\Omega=20\,\Omega$。

**规则何时失效。** 这些规则要求每一部分各自保持端口条件。级联时这是有保证的，因为后一部分连同负载对前一部分而言就是一个二端元件。具有公共地线的两个三端网络也可以并联：它们的 1$'$ 和 2$'$ 合于一点，只有返回电流之和起作用。串联时必须小心。如果把两个 T 形网络连同各自的地线上下叠放，上面网络的地线就把下面网络的两个上方接线端短路。这时端口 1 的一部分电流在下面的 T 中流过 $R_\mathrm{c}$，端口条件被破坏。测得的不是 $Z_{11}=70\,\Omega$，而是 $35\,\Omega+15\,\Omega\parallel20\,\Omega+20\,\Omega=63.6\,\Omega$。补救办法：把下面的 T 镜像翻转，使只有两条地线相连。这样两者都仍是三端网络，规则给出正确的 70 $\Omega$。

⁠**极限情况：**两个相同的二端口网络并联时，矩阵 $\mathbf Z$ 减半，相同的电阻并联时电阻减半。串联时 $\mathbf Z$ 加倍。

:::frage 为什么串联时链式矩阵不也相加？
因为串联时 $I_1$ 对两部分相同，$U_1$ 却不同。在链式形式中，$U_1$ 和 $I_1$ 一起在左边，右边则是输出量。右边的列对两部分不同，无法合并。
:::

:::aufgabe 练习 9 ★★ 哪种形式合适？
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

两个相同的 T 形网络按并联，并联连接。整个电路的 $\mathbf Z$ 是多少？为什么这里可以这样计算？

</li>

<li>

两个相同的 T 形网络，下面的一个镜像翻转，按串联，串联连接。$\mathbf Z$ 是多少？

</li>

<li>

T 形网络的混合矩阵已知。两个相同的二端口网络按串联，并联连接时（假设端口条件成立），$\mathbf H$ 是多少？

</li>

<li>

T 形网络按串联，串联再接一个 10 $\Omega$ 的并联电阻。得到什么样的 $\mathbf Z$，对应什么样的 T 形网络？

</li>

</ol>

:::loesung
(a) $\mathbf Y$ 加倍，所以 $\mathbf Z$ 减半：$Z_{11}=17.5\,\Omega$，$Z_{12}=Z_{21}=10\,\Omega$，$Z_{22}=20\,\Omega$。两者都是具有公共地线的三端网络，端口仍是端口。 (b) $\mathbf Z$ 加倍：70、40、40、80 $\Omega$。 (c) $\mathbf H$ 加倍：$H_{11}=50\,\Omega$，$H_{12}=1$，$H_{21}=-1$，$H_{22}=50$ mS。 (d) $Z_{11}=45\,\Omega$，$Z_{12}=Z_{21}=30\,\Omega$，$Z_{22}=50\,\Omega$。这是 $R_\mathrm{a}=15\,\Omega$，$R_\mathrm{b}=30\,\Omega$，$R_\mathrm{c}=20\,\Omega$ 的 T 形网络：并联电阻与 $R_\mathrm{b}$ 串联，因为它流过相同的和电流。
:::
:::
