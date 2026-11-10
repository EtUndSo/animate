---
title: 单位矩阵与逆矩阵
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: 第 1 章：向量与矩阵
nachschlagen: ja
order: 15211200
summary: 有些线性映射可以撤销，有些则不能。本节介绍什么都不改变的矩阵，以及使映射反向的逆矩阵，并阐明逆矩阵何时存在。
tags: 单位矩阵, 可逆的, 逆矩阵, 奇异矩阵
lang: zh
---

<span class="anker" id="stufe-11"></span>

:::zweck
有些线性映射可以撤销，有些则不能。本节介绍什么都不改变的矩阵，以及使映射反向的逆矩阵，并阐明逆矩阵何时存在。
:::

### 单位矩阵

<span class="anker" id="stufe-11-1"></span>

在所有线性映射中，有一个映射什么都不做：它把每个向量映射为它自身。由式 [(8.2)](lineare-abbildungen.html#gl-8-2)，它的各列是单位向量的像，也就是单位向量本身。

:::definition 定义 11.1 (单位矩阵)
<span class="anker" id="satz-11-1"></span>

__单位矩阵__ $\mathbf{I}_n\in\mathbb{R}^{n\times n}$ 是对角线上全为一的对角矩阵。它的各列为 $\mathbf{e}_1,\dots,\mathbf{e}_n$。
:::

如果型很明确，就简写为 $\mathbf{I}$。对每个向量 $\mathbf{x}\in\mathbb{R}^n$，有 $\mathbf{I}\mathbf{x}=\mathbf{x}$；对每个矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$，有 $\mathbf{A}\mathbf{I}_n=\mathbf{A}$ 和 $\mathbf{I}_m\mathbf{A}=\mathbf{A}$。在矩阵乘积中，单位矩阵起着数 $1$ 的作用。

::::beispiel [算例]
$$\mathbf{I}_3=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\qquad \mathbf{I}_3\begin{pmatrix}60\\2\\3\end{pmatrix}=\begin{pmatrix}60\\2\\3\end{pmatrix}.$$
::::

⁠**简而言之：**单位矩阵在对角线上为一，其余位置全为零；作为映射，它使每个向量保持不变。

### 逆矩阵

<span class="anker" id="stufe-11-2"></span>

旋转 $90^\circ$ 可以通过反向旋转 $90^\circ$ 来撤销。拉伸到两倍可以通过压缩到一半来撤销。在这两种情况下，都有第二个映射抵消第一个映射：先后作用时，两者合起来什么也不做。

:::definition 定义 11.2 (逆矩阵)
<span class="anker" id="satz-11-2"></span>

对方阵 $\mathbf{A}\in\mathbb{R}^{n\times n}$，如果存在矩阵 $\mathbf{A}^{-1}\in\mathbb{R}^{n\times n}$ 使下式成立，就称这个方阵是__可逆的__：

<span class="anker" id="gl-11-1"></span>
$$\mathbf{A}\mathbf{A}^{-1}=\mathbf{A}^{-1}\mathbf{A}=\mathbf{I} . \tag{11.1}$$

矩阵 $\mathbf{A}^{-1}$ 称为 $\mathbf{A}$ 的__逆矩阵__。
:::

这样的矩阵至多有一个。事实上，如果 $\mathbf{B}$ 和 $\mathbf{C}$ 都是 $\mathbf{A}$ 的逆矩阵，那么 $\mathbf{B}=\mathbf{B}\mathbf{I}=\mathbf{B}(\mathbf{A}\mathbf{C})=(\mathbf{B}\mathbf{A})\mathbf{C}=\mathbf{I}\mathbf{C}=\mathbf{C}$。正因为如此，可以说“**这个**逆矩阵”，而不只是“一个逆矩阵”。知道了它，就能从任何结果 $\mathbf{y}=\mathbf{A}\mathbf{x}$ 倒推回去：$\mathbf{A}^{-1}\mathbf{y}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{x}$。

::::beispiel [算例]
$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\begin{pmatrix}2-1&-2+2\\1-1&-1+2\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix},$$

另一种顺序同样如此，所以 $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$。拉伸的逆矩阵是 $\operatorname{diag}(2,\,0.5)^{-1}=\operatorname{diag}(0.5,\,2)$，旋转 $90^\circ$ 的逆矩阵是旋转 $-90^\circ$，$\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$。
::::

⁠**简而言之：**逆矩阵 $\mathbf{A}^{-1}$ 撤销映射 $\mathbf{A}$：$\mathbf{A}^{-1}\mathbf{A}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$。

:::hintergrund 对角矩阵的逆矩阵
对角矩阵 $\operatorname{diag}(\mathbf{v})$ 把每个分量乘以它自己的因子 $v_j$。要撤销这一步，就把每个分量除以它的因子：$\operatorname{diag}(\mathbf{v})^{-1}=\operatorname{diag}(1/v_1,\dots,1/v_n)$。当且仅当没有一个因子为零时，这才行得通。因子 $v_j=0$ 抹去了分量 $j$，而被抹去的东西，任何计算都无法找回。
:::

### $2\times2$ 矩阵的逆矩阵

<span class="anker" id="stufe-11-3"></span>

对 $2\times2$ 矩阵，有一个简单的公式。交换两个对角元素，给另外两个元素加上负号，再除以一个由全部四个元素构成的数。

:::satz 定理 11.3 ($2\times2$ 矩阵的逆矩阵)
<span class="anker" id="satz-11-3"></span>

矩阵 $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ 可逆，当且仅当 $ad-bc\ne0$，此时

<span class="anker" id="gl-11-2"></span>
$$\mathbf{A}^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}. \tag{11.2}$$
:::

:::herleitung $2\times2$ 矩阵的逆矩阵
把乘积展开，得到

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}=\begin{pmatrix}ad-bc&-ab+ba\\cd-dc&-cb+da\end{pmatrix}=(ad-bc)\,\mathbf{I} ,$$

另一种顺序同样如此。若 $ad-bc\ne0$，就除以这个数，得到式 [(11.1)](#gl-11-1)。若 $ad-bc=0$，则 $\mathbf{A}$ 把向量 $(d,\,-c)^{\top}$ 变成 $(ad-bc,\ cd-dc)^{\top}=\mathbf{0}$，同样把 $(b,\,-a)^{\top}$ 变成 $\mathbf{0}$。除非四个元素全为零，否则这两个向量中至少有一个不是零向量；而四个元素全为零时，$\mathbf{A}$ 本来就是零矩阵。但是，把一个向量 $\mathbf{x}\ne\mathbf{0}$ 映射为 $\mathbf{0}$ 的矩阵没有逆矩阵：如果有的话，就会有 $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$。
:::

::::beispiel [算例]
对 $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$，$ad-bc=2-1=1$，所以逆矩阵是 $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$，与上面相同。对 $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$，$ad-bc=5$，逆矩阵是 $\tfrac15\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$。
::::

⁠**简而言之：**$2\times2$ 矩阵可逆，当且仅当 $ad-bc\ne0$；逆矩阵为 $\frac{1}{ad-bc}\bigl(\begin{smallmatrix}d&-b\\-c&a\end{smallmatrix}\bigr)$。

### 逆矩阵的运算规则

<span class="anker" id="stufe-11-4"></span>

如果先后作用两个映射，又想撤销结果，就必须先抵消第二个映射。所以求乘积的逆矩阵时，顺序要反过来。

:::satz 定理 11.4 (逆矩阵的运算规则)
<span class="anker" id="satz-11-4"></span>

若 $\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ 可逆且 $c\ne0$，则 $\mathbf{A}\mathbf{B}$、$\mathbf{A}^{\top}$、$\mathbf{A}^{-1}$ 和 $c\,\mathbf{A}$ 也可逆，并且

$$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1},\qquad(\mathbf{A}^{\top})^{-1}=(\mathbf{A}^{-1})^{\top},\qquad(\mathbf{A}^{-1})^{-1}=\mathbf{A},\qquad(c\,\mathbf{A})^{-1}=\tfrac1c\,\mathbf{A}^{-1}.$$
:::

:::herleitung 逆矩阵的运算规则
每一种情形都要验证：与候选矩阵的乘积给出单位矩阵。对乘积：$(\mathbf{A}\mathbf{B})(\mathbf{B}^{-1}\mathbf{A}^{-1})=\mathbf{A}(\mathbf{B}\mathbf{B}^{-1})\mathbf{A}^{-1}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$，同样 $(\mathbf{B}^{-1}\mathbf{A}^{-1})(\mathbf{A}\mathbf{B})=\mathbf{I}$。对转置：$\mathbf{A}^{\top}(\mathbf{A}^{-1})^{\top}=(\mathbf{A}^{-1}\mathbf{A})^{\top}=\mathbf{I}^{\top}=\mathbf{I}$，另一种顺序同样如此。最后两条规则直接由式 [(11.1)](#gl-11-1) 得出。
:::

有一条你可能希望成立的规则并不成立：$(\mathbf{A}+\mathbf{B})^{-1}$ 一般不等于 $\mathbf{A}^{-1}+\mathbf{B}^{-1}$。即使对数而言，也有 $\frac{1}{2+4}=\frac16$，而 $\frac12+\frac14=\frac34$。

::::beispiel [算例]
对 $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ 和 $\mathbf{B}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$，$\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$，其中 $ad-bc=21-16=5$，所以 $(\mathbf{A}\mathbf{B})^{-1}=\tfrac15\bigl(\begin{smallmatrix}3&-4\\-4&7\end{smallmatrix}\bigr)$。由下式得到同样的结果：

$$\mathbf{B}^{-1}\mathbf{A}^{-1}=\tfrac15\begin{pmatrix}2&-1\\-1&3\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\tfrac15\begin{pmatrix}3&-4\\-4&7\end{pmatrix}.$$
::::

⁠**简而言之：**乘积的逆矩阵是各逆矩阵按相反顺序的乘积，$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$。

:::hintergrund 顺序反过来的一个图景
早上先穿毛衣再穿外套的人，晚上要先脱外套再脱毛衣。撤销时要倒着走过各个步骤。映射 $\mathbf{A}\mathbf{B}$ 是“先 $\mathbf{B}$，后 $\mathbf{A}$”；要抵消它，必须先抵消 $\mathbf{A}$，再抵消 $\mathbf{B}$，即先作用 $\mathbf{A}^{-1}$，再作用 $\mathbf{B}^{-1}$。写成矩阵时，先执行的一步写在右边，就是 $\mathbf{B}^{-1}\mathbf{A}^{-1}$。这个图景只在顺序这一点上成立；它并不能解释逆矩阵为什么存在。
:::

### 没有逆矩阵的情形

<span class="anker" id="stufe-11-5"></span>

矩阵 $\operatorname{diag}(1,\,0)$ 把平面压扁到 $x_1$ 轴上（图 [32](lineare-abbildungen.html#abb-32)）。点 $(1,\,5)^{\top}$ 和 $(1,\,-2)^{\top}$ 都落到 $(1,\,0)^{\top}$。如果只看到结果 $(1,\,0)^{\top}$，就无法知道它来自哪个点。第二个分量丢失了，任何计算都无法把它找回。

:::satz 定理 11.5 (没有逆矩阵)
<span class="anker" id="satz-11-5"></span>

若存在向量 $\mathbf{x}\ne\mathbf{0}$ 使 $\mathbf{A}\mathbf{x}=\mathbf{0}$，则 $\mathbf{A}$ 不可逆。
:::

:::beweis 没有逆矩阵
如果存在逆矩阵，那么 $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$，与 $\mathbf{x}\ne\mathbf{0}$ 矛盾。
:::

直观地说：若 $\mathbf{A}\mathbf{x}=\mathbf{0}$，则对每个 $\mathbf{u}$，两个不同的向量 $\mathbf{u}$ 和 $\mathbf{u}+\mathbf{x}$ 都落到同一处，因为 $\mathbf{A}(\mathbf{u}+\mathbf{x})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{x}=\mathbf{A}\mathbf{u}$。输出相同的两个输入无法区分。不可逆的方阵称为__奇异矩阵__。

::::beispiel [算例]
对 $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$，$ad-bc=4-4=0$。确实，$\mathbf{x}=(2,\,-1)^{\top}$ 被映射为 $(2-2,\ 4-4)^{\top}=\mathbf{0}$，而不同的向量 $(1,\,1)^{\top}$ 和 $(3,\,0)^{\top}$ 都落到 $(3,\,6)^{\top}$。
::::

对数据而言，这意味着：例如一个计算如果只由卧室数和起居室数求出房间总数，就无法再把这两个数分开。对 $2\times2$ 矩阵，这恰好就是第 [11.3](#stufe-11-3) 小节中 $ad-bc=0$ 的情形。

⁠**简而言之：**如果矩阵把一个向量 $\mathbf{x}\ne\mathbf{0}$ 映射为 $\mathbf{0}$，它就会丢失信息，没有逆矩阵；这时称它为奇异矩阵。

:::aufgabe 练习 26 ★ 计算逆矩阵
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

计算 $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$ 和 $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ 的逆矩阵，并逐一验算结果。

</li>

<li>

数 $t$ 取何值时，$\bigl(\begin{smallmatrix}2&t\\4&6\end{smallmatrix}\bigr)$ 不可逆？对这种情形，给出一个满足 $\mathbf{A}\mathbf{x}=\mathbf{0}$ 的向量 $\mathbf{x}\ne\mathbf{0}$。

</li>

<li>

给出 $\operatorname{diag}(4,\,-1,\,0.5)$ 的逆矩阵。

</li>

</ol>

:::loesung
(a) 对 $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$，$ad-bc=4-3=1$，逆矩阵为 $\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)$。验算：$\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4-3&-12+12\\1-1&-3+4\end{smallmatrix}\bigr)=\mathbf{I}$。对 $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$，$ad-bc=4-6=-2$，逆矩阵为 $-\tfrac12\bigl(\begin{smallmatrix}4&-2\\-3&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1\\1.5&-0.5\end{smallmatrix}\bigr)$。验算：$\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}-2&1\\1.5&-0.5\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2+3&1-1\\-6+6&3-2\end{smallmatrix}\bigr)=\mathbf{I}$。

(b) 当 $t=3$ 时，$ad-bc=12-4t=0$。这时矩阵为 $\bigl(\begin{smallmatrix}2&3\\4&6\end{smallmatrix}\bigr)$；它的第二行是第一行的两倍。向量 $(3,\,-2)^{\top}$ 被映射为 $(6-6,\ 12-12)^{\top}=\mathbf{0}$。

(c) $\operatorname{diag}(4,\,-1,\,0.5)^{-1}=\operatorname{diag}(0.25,\,-1,\,2)$：每个对角元素都换成它的倒数。
:::
:::

:::aufgabe 练习 27 ★★ 用逆矩阵论证
<span class="anker" id="aufg-27"></span>

<ol class="al">

<li>

对 $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ 验证 $(\mathbf{C}^{\top})^{-1}=(\mathbf{C}^{-1})^{\top}$。

</li>

<li>

设 $\mathbf{A}$ 可逆且 $\mathbf{A}\mathbf{B}=\mathbf 0$。证明这时 $\mathbf{B}=\mathbf 0$。

</li>

<li>

对数而言，由 $ab=0$ 可推出 $a=0$ 或 $b=0$。用 $\mathbf{A}=\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$ 说明这对矩阵不成立。为什么这与 (b) 并不矛盾？

</li>

</ol>

:::loesung
(a) 由上一个练习，$\mathbf{C}^{-1}=\bigl(\begin{smallmatrix}-2&1\\1.5&-0.5\end{smallmatrix}\bigr)$，所以 $(\mathbf{C}^{-1})^{\top}=\bigl(\begin{smallmatrix}-2&1.5\\1&-0.5\end{smallmatrix}\bigr)$。另一方面，$\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)$，$ad-bc=-2$，所以 $(\mathbf{C}^{\top})^{-1}=-\tfrac12\bigl(\begin{smallmatrix}4&-3\\-2&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1.5\\1&-0.5\end{smallmatrix}\bigr)$。两者一致。

(b) 用 $\mathbf{A}^{-1}$ 左乘 $\mathbf{A}\mathbf{B}=\mathbf 0$ 的两边：$\mathbf{B}=\mathbf{I}\mathbf{B}=\mathbf{A}^{-1}\mathbf{A}\mathbf{B}=\mathbf{A}^{-1}\mathbf 0=\mathbf 0$。

(c) $\mathbf{A}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}0\cdot0+1\cdot0&0\cdot1+1\cdot0\\0&0\end{smallmatrix}\bigr)=\mathbf 0$，尽管 $\mathbf{A}\ne\mathbf 0$。从几何上看，$\mathbf{A}$ 把向量 $\mathbf{e}_2$ 映射为 $\mathbf{e}_1$，把 $\mathbf{e}_1$ 映射为 $\mathbf{0}$；作用两次，一切都落到零向量上。这与 (b) 并不矛盾，因为 $\mathbf{A}$ 不可逆：$ad-bc=0$。(b) 中的推论需要逆矩阵。
:::
:::
