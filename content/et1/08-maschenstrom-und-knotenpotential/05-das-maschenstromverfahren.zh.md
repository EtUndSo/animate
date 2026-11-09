---
title: 第 3 阶段：网孔电流法
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 网孔电流法与节点电位法
order: 1180500
summary: 节点定律已经解决，剩下 m 条网孔定律和 m 个未知量。本阶段列出这些方程，并说明为什么矩阵可以直接读出。
tags: 互电阻
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
节点定律已经解决，剩下 $m$ 条网孔定律和 $m$ 个未知量。本阶段列出这些方程，并说明为什么矩阵可以直接读出。
:::

**基本思路。** 沿网孔电流的方向绕行网孔。在每个电阻上压降为 $R$ 乘以支路电流，而支路电流是本网孔电流加上或减去相邻网孔的电流。按网孔电流整理后，本网孔电流前面是该网孔所有电阻之和。其他网孔电流前面只有两个网孔共同经过的部分。那里不可能有更多内容。所以矩阵就是电路的一张清单。

:::definition 定义 3.1 (网孔电流法)
<span class="anker" id="satz-3-1"></span>

该方法有四步：

<ol>

<li>

把实际电流源变换为实际电压源：$U_\mathrm q=I_\mathrm q\,R$，同一电阻改为串联（[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）。

</li>

<li>

选 $m$ 个独立网孔，各标一个方向任意的网孔电流。网孔的绕行方向就是这个方向。

</li>

<li>

对每个网孔列出网孔定律，或直接读出矩阵。

</li>

<li>

解方程组得到网孔电流，再由此计算支路电流和支路电压。

</li>

</ol>
:::

:::satz 定理 3.2 (网孔电流法的矩阵形式)
<span class="anker" id="satz-3-2"></span>

网孔电流满足 $\mathbf Z\,\mathbf I=\mathbf U_\mathrm q$：

<span class="anker" id="gl-3-1"></span>
$$\begin{pmatrix}Z_{11}&Z_{12}&\dots&Z_{1m}\\mathbb{Z}_{21}&Z_{22}&\dots&Z_{2m}\\\vdots&\vdots&\ddots&\vdots\\mathbb{Z}_{m1}&Z_{m2}&\dots&Z_{mm}\end{pmatrix} \begin{pmatrix}I_1\\I_2\\\vdots\\I_m\end{pmatrix}= \begin{pmatrix}U_\mathrm{q1}\\U_\mathrm{q2}\\\vdots\\U_{\mathrm qm}\end{pmatrix}. \tag{3.1}$$

<ul>

<li>

$Z_{\mu\mu}$ 是网孔 $\mu$ 所有电阻之和。

</li>

<li>

$Z_{\mu\nu}$ 是__互电阻__，即两个网孔共同经过的电阻之和：两个电流在那里同向时为正，反向时为负，没有公共支路时为零。有 $Z_{\mu\nu}=Z_{\nu\mu}$。

</li>

<li>

$U_{\mathrm q\mu}$ 是网孔中电源电压之和，每个驱动网孔电流的电源计为正。对于从正极指向负极的电压箭头（发电机惯例，[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)），这意味着：箭头与绕行方向相反时计为正，相同时计为负。

</li>

</ul>
:::

:::herleitung 从网孔定律到矩阵
对网孔 $\mu$，所有 $R_a\,I_a$ 之和等于驱动电压 $U_{\mathrm q\mu}$，因为电源被移到了右端。这里 $I_a$ 是 $R_a$ 中的电流，按 $\mu$ 的绕行方向计数。由式 [(2.1)](maschenstrome-erfullen-die-knotenregel.html#gl-2-1)，$I_a=I_\mu+\sum_{\nu\neq\mu}\sigma_{a\nu}\,I_\nu$。整理后，$I_\mu$ 前面是所有 $R_a$ 之和，$I_\nu$ 前面是公共电阻上的和 $\sum_a\sigma_{a\nu}R_a$。网孔 $\nu$ 得到相同的电阻和相同的符号，因为“同向”是两个网孔之间的关系。所以 $\mathbf Z$ 是对称的。
:::

⁠**如何理解：**第 $\mu$ 行是网孔 $\mu$ 的网孔定律。第 $\nu$ 列表示一安培网孔电流 $\nu$ 在每个网孔中产生的电压。因此单位是欧姆，这里典型值是千欧。字母 $Z$ 来自阻抗（[第 6 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)），这里都是纯电阻。**适用条件：**网络含线性电阻和固定电压源。对称性同时也是一种检验：列方程时的错误通常会破坏它。

:::abbildung et1/k8maschen 3
用于网孔电流法的模型电路。右边的电流源已变换为电压源。红色是公共电阻 $R_2$ 和 $R_4$：它们出现在 $\mathbf Z$ 的对角线之外。I 和 III 没有公共支路，所以 $Z_{13}=0$。
:::

::::beispiel
右边得到 $U_\mathrm{q5}=I_\mathrm q\,R_5=20$ V，与 $R_5$ 串联（图 [3](#abb-3)）。三次顺时针绕行得

$$\begin{aligned} \text{I:}\quad&R_1I_\mathrm I+R_2(I_\mathrm I-I_\mathrm{II})-U_\mathrm q=0,\\ \text{II:}\quad&R_2(I_\mathrm{II}-I_\mathrm I)+R_3I_\mathrm{II}+R_4(I_\mathrm{II}-I_\mathrm{III})=0,\\ \text{III:}\quad&R_4(I_\mathrm{III}-I_\mathrm{II})+R_5I_\mathrm{III}+U_\mathrm{q5}=0. \end{aligned}$$

整理后，以 k$\Omega$、mA 和 V 为单位，这正是直接读出的结果：

$$\begin{pmatrix}R_1+R_2&-R_2&0\\-R_2&R_2+R_3+R_4&-R_4\\0&-R_4&R_4+R_5\end{pmatrix} \begin{pmatrix}I_\mathrm I\\I_\mathrm{II}\\I_\mathrm{III}\end{pmatrix}= \begin{pmatrix}5&-4&0\\-4&16&-10\\0&-10&15\end{pmatrix} \begin{pmatrix}I_\mathrm I\\I_\mathrm{II}\\I_\mathrm{III}\end{pmatrix}= \begin{pmatrix}9\\0\\-20\end{pmatrix}.$$

所有非对角元都是负的，因为旋转方向相同的相邻环路在公共支路中彼此反向。$U_\mathrm q$ 驱动网孔 I，$U_\mathrm{q5}$ 与网孔 III 方向相反。由式 [(0.1)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-1) 和式 [(0.2)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-2) 得

$$D=5\cdot140+4\cdot(-60)=460,\qquad D_1=9\cdot140+4\cdot(-200)=460,$$

$$D_2=5\cdot(-200)-9\cdot(-60)=-460,\qquad D_3=-1600+320+360=-920.$$

所以 $I_\mathrm I=1$ mA，$I_\mathrm{II}=-1$ mA，$I_\mathrm{III}=-2$ mA。负号表示：网孔 II 和 III 实际上是逆时针流动的。由第 [2](maschenstrome-erfullen-die-knotenregel.html#stufe-2) 阶段得支路电流：$R_1$ 中 1 mA，$R_2$ 中向下 2 mA，$R_3$ 中从节点 2 到节点 1 为 1 mA，$R_4$ 中向下 1 mA。**检验：**$U_1=R_2\cdot2\,\mathrm{mA}=8$ V，$U_2=R_4\cdot1\,\mathrm{mA}=10$ V。网孔 I：$1+8-9=0$。
::::

⁠**极限情况：**$R_2\to0$ 时 $Z_{12}=0$，网孔 I 解耦：中间的导线把两侧分开，因为不论流过多大电流，它上面的电压都为零。

:::frage 所有网孔电流都必须朝同一方向吗？
不必。旋转方向相同只是方便，因为这样所有非对角元都是负的。把一个网孔电流反向，它所在的行和列变号，对角线不变，电流的数值也变号。支路电流不变。
:::

:::zusatz 理想电流源
$R_5\to\infty$ 时，$U_\mathrm{q5}$ 无限增大，变换失效（[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）。这时要这样布置网孔，使得只有一个网孔穿过电流源。它的网孔电流是已知的。这个网孔的方程要省去，因为其中含有电源的未知电压。少一个未知量，也少一个方程。
:::

:::aufgabe 练习 3 ★★ 第 2 部分的网络
<span class="anker" id="aufg-3"></span>

[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)的网络在 $K_1$ 和 $K_4$ 之间有一个 9 V 的理想电源，并有 $R_\mathrm a=2\,\mathrm{k\Omega}$（$K_1K_2$），$R_\mathrm b=5\,\mathrm{k\Omega}$（$K_2K_4$），$R_\mathrm c=3\,\mathrm{k\Omega}$（$K_1K_3$），$R_\mathrm d=1\,\mathrm{k\Omega}$（$K_3K_4$），$R_\mathrm e=2\,\mathrm{k\Omega}$（$K_2K_3$）。网孔这样走：$I_\mathrm A$ 穿过电源从 $K_4$ 到 $K_1$，再到 $K_2$，回到 $K_4$。$I_\mathrm B$ 从 $K_1$ 到 $K_3$、$K_2$，回到 $K_1$。$I_\mathrm C$ 从 $K_2$ 到 $K_3$、$K_4$，回到 $K_2$。

<ol class="al">

<li>

读出 $\mathbf Z$ 和右端。检验对称性。

</li>

<li>

用克莱姆法则计算网孔电流。

</li>

<li>

求五个电阻电流，并与[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)比较。

</li>

</ol>

:::loesung
(a) 网孔 A 含 $R_\mathrm a$、$R_\mathrm b$，网孔 B 含 $R_\mathrm a$、$R_\mathrm c$、$R_\mathrm e$，网孔 C 含 $R_\mathrm b$、$R_\mathrm d$、$R_\mathrm e$。所有网孔在公共支路中都是反向的：

$$\mathbf Z=\begin{pmatrix}7&-2&-5\\-2&7&-2\\-5&-2&8\end{pmatrix}\mathrm{k\Omega},\qquad\mathbf U_\mathrm q=\begin{pmatrix}9\\0\\0\end{pmatrix}\mathrm V.$$

矩阵是对称的。

(b) $D=7(56-4)+2(-16-10)-5(4+35)=364-52-195=117$。$D_1=9\cdot52=468$，$D_2=234$，$D_3=351$。所以 $I_\mathrm A=4$ mA，$I_\mathrm B=2$ mA，$I_\mathrm C=3$ mA。

(c) $I_\mathrm a=I_\mathrm A-I_\mathrm B=2$ mA，$I_\mathrm b=I_\mathrm A-I_\mathrm C=1$ mA，$I_\mathrm c=I_\mathrm B=2$ mA，$I_\mathrm d=I_\mathrm C=3$ mA，$I_\mathrm e=I_\mathrm C-I_\mathrm B=1$ mA，从 $K_2$ 到 $K_3$。这就是[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)的表，只用了三个方程而不是十二个。
:::
:::

:::aufgabe 练习 4 ★★ 反向与短路
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

在模型电路中只把网孔电流 II 反向。$\mathbf Z$、右端和 $I_\mathrm{II}$ 变成什么？

</li>

<li>

预测：把 $R_4$ 换成导线。$\mathbf Z$ 的哪些元素变为零？不解方程组求出 $I_\mathrm{III}$。

</li>

</ol>

:::loesung
(a) 第 II 行和第 II 列变号，对角线不变：

$$\mathbf Z=\begin{pmatrix}5&4&0\\4&16&10\\0&10&15\end{pmatrix}\mathrm{k\Omega},\qquad\mathbf U_\mathrm q=\begin{pmatrix}9\\0\\-20\end{pmatrix}\mathrm V,\qquad I_\mathrm{II}=+1\,\mathrm{mA}.$$

现在两条公共支路中的环路都是同向的。右端不变，因为网孔 II 中没有电源。

(b) $Z_{23}=Z_{32}=0$，因为 $R_4$ 是唯一的公共电阻。网孔 III 只剩下 $R_5$ 和 $U_\mathrm{q5}$：$I_\mathrm{III}=-20\,\mathrm{V}/5\,\mathrm{k\Omega}=-4$ mA。这就是变换后的电流源被短路，即 4 mA 的短路电流。网孔 I 和 II 仍然耦合。
:::
:::
