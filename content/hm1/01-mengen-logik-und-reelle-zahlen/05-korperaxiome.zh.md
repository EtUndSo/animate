---
title: 第 3 阶段：域公理
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 集合、逻辑与实数
order: 1210500
summary: 关于加法和乘法，必须假设哪几条规则，才能证明其余所有运算法则？
tags: 运算, 分配律, 差, 商
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
关于加法和乘法，必须假设哪几条规则，才能证明其余所有运算法则？
:::

**基本思路。** 每个数系的产生，都是因为前一个数系中有方程无解（图 [3](#abb-3)）：$x+3=1$ 在 $\mathbb{N}$ 中无解，$3x=1$ 在 $\mathbb{Z}$ 中无解。域就是两类方程总有解的数系：加法和乘法都可以逆转。公理要求的不过如此。加法和乘法之间唯一的纽带是分配律，本阶段几乎所有证明都要用到它。

:::abbildung hm1/k1zahlbereiche 3
每个方程要到它所在的数系才有解。
:::

:::definition 定义 3.1 (域)
<span class="anker" id="satz-3-1"></span>

__运算__把任意两个元素对应到同一集合的一个元素。带有两个运算“$+$”和“$\cdot$”的集合 $\mathbb K$ 称为域，如果对所有 $x,y,z\in\mathbb K$ 有：

|  | 加法 | 乘法 |
|---|---|---|
| 交换律 | (A1) $x+y=y+x$ | (M1) $x\cdot y=y\cdot x$ |
| 结合律 | (A2) $x+(y+z)=(x+y)+z$ | (M2) $x\cdot(y\cdot z)=(x\cdot y)\cdot z$ |
| 中性元 | (A3) 存在 $0\in\mathbb K$，使 $x+0=x$ 对所有 $x$ 成立。 | (M3) 存在 $1\in\mathbb K$，使 $x\cdot1=x$ 对所有 $x$ 成立。 |
| 逆元 | (A4) 对每个 $x$ 存在 $y$，使 $x+y=0$，记作 $-x$。 | (M4) 对每个 $x\ne0$ 存在 $y$，使 $x\cdot y=1$，记作 $x^{-1}$ 或 $\frac1x$。 |

此外还有 (AM) $x\cdot(y+z)=(x\cdot y)+(x\cdot z)$（__分配律__）和 (NNE) $0\ne1$。
:::

⁠**如何理解：**这里的 $0$ 和 $1$ 只是两个特定元素的名字。减法和除法不是单独的运算：$x-y:=x+(-y)$，$\frac yx:=y\cdot x^{-1}$。约定“先乘后加”，并约定 $xy:=x\cdot y$。凡是从公理推出的结论，在每个域中都成立，因而也适用于[第 2 部分](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)的复数。$\mathbb{Q}$ 和 $\mathbb{R}$ 是例子。$\mathbb{N}$ 不是域（没有 0，没有 $-1$），$\mathbb{Z}$ 也不是（2 没有逆元）。最小的域是 $\{0,1\}$，其中 $1+1=0$，这就是数字电路中的加法（XOR）。**为什么需要这些前提：**没有 (NNE)，$\{0\}$ 就是域了。(M4) 中没有 $x\ne0$，由下面的 (iii) 就会得到 $1=0\cdot0^{-1}=0$。

:::satz 定理 3.2 (域中的运算法则)
<span class="anker" id="satz-3-2"></span>

对所有 $x,y,z,u,v\in\mathbb K$ 有：

<ol class="rm">

<li>

逆元唯一：$(xy=1\wedge xz=1)\Rightarrow y=z$，$(x+y=0\wedge x+z=0)\Rightarrow y=z$。

</li>

<li>

方程有唯一解：$x+z=y$ 恰有解 $z=y-x$（__差__）。当 $x\ne0$ 时，$xz=y$ 恰有解 $z=y\cdot x^{-1}=\frac yx$（__商__）。

</li>

<li>

$x\cdot0=0$，且当 $x\ne0$ 时 $(x^{-1})^{-1}=x$。

</li>

<li>

$-(-x)=x$，$(-x)(-y)=xy$。

</li>

<li>

$xy=0\Rightarrow(x=0\vee y=0)$。

</li>

<li>

当 $u,v\ne0$ 时，$\frac xu\cdot\frac yv=\frac{xy}{uv}$，$\frac xu+\frac yv=\frac{xv+yu}{uv}$；当 $u,v,y\ne0$ 时，$\frac xu:\frac yv=\frac{xv}{uy}$。

</li>

</ol>
:::

⁠**如何理解：**有了 (i)，记号 $-x$ 和 $x^{-1}$ 才有意义：若有两个逆元，就不知道指的是哪一个。(v) 是把方程分解因式、再令每个因式为零的依据。**为什么要求 $x\ne0$：**由 (iii)，$0\cdot z=1$ 无解，而 $0\cdot z=0$ 以每个 $z$ 为解。除以零要么败在存在性上，要么败在唯一性上。

:::beweis 运算法则，每一步标明公理
(i) 由 $xy=xz$（两者都是 1），两边乘 $y$ 得 $(xy)y=(xz)y$。左边是 $1\cdot y=y$（M1，M3）。右边：$(xz)y\overset{\text{M2}}{=}x(zy)\overset{\text{M1}}{=}x(yz)\overset{\text{M2}}{=}(xy)z=1\cdot z=z$。加法同理（练习 [4](#aufg-4)）。

(ii) 存在性：$x(yx^{-1})=x(x^{-1}y)=(xx^{-1})y=1\cdot y=y$（M1，M2，M4，M3）。唯一性：由 $xz=x\tilde z$，两边乘 $x^{-1}$，用同样的公理得 $z=\tilde z$。加法同理，用 $-x$。

(iii) $x\cdot0\overset{\text{A3}}{=}(x\cdot0)+0\overset{\text{A4}}{=}(x\cdot0)+\bigl((x\cdot0)+(-(x\cdot0))\bigr)\overset{\text{A2}}{=}\bigl((x\cdot0)+(x\cdot0)\bigr)+(-(x\cdot0))\overset{\text{AM}}{=}x\cdot(0+0)+(-(x\cdot0))\overset{\text{A3}}{=}(x\cdot0)+(-(x\cdot0))\overset{\text{A4}}{=}0$。当 $x\ne0$ 时 $x^{-1}\ne0$（反证：由 $x^{-1}=0$ 将得 $1=xx^{-1}=x\cdot0=0$，与 NNE 矛盾）。所以 $x^{-1}$ 有逆元。有 $(x^{-1})^{-1}x^{-1}=1$ 和 $x\,x^{-1}=1$，由 (i)，$x$ 与 $(x^{-1})^{-1}$ 相等。

(iv) $x$ 和 $-(-x)$ 都是 $-x$ 的加法逆元，由 (i) 二者相等。又有 $x+(-1)x=(1+(-1))x=0\cdot x=0$，所以 $(-1)x=-x$。由 $(-1)+(-1)(-1)=(-1)(1+(-1))=(-1)\cdot0=0$ 同样得出 $(-1)(-1)$ 是 $-1$ 的逆元，所以 $(-1)(-1)=-(-1)=1$。于是 $(-x)(-y)=(-1)(-1)xy=xy$。

(v) 若 $x\ne0$，则 $y=x^{-1}(xy)=x^{-1}\cdot0=0$。

(vi) $\frac xu\cdot\frac yv=(xu^{-1})(yv^{-1})=(xy)(u^{-1}v^{-1})$，而 $u^{-1}v^{-1}=(uv)^{-1}$，因为 $(u^{-1}v^{-1})(uv)=1$ 且逆元唯一。除法法则由 $(y v^{-1})^{-1}=y^{-1}v$ 得出，加法法则通过通分得出：$\frac xu=\frac{xv}{uv}$，$\frac yv=\frac{yu}{uv}$，再用 (AM)。
:::

::::beispiel
$(-3)(-5)=15$，$\frac23+\frac57=\frac{14+15}{21}=\frac{29}{21}$，$\frac34:\frac58=\frac{3\cdot8}{4\cdot5}=\frac65$。
::::

⁠**极限情况** $v=u=1$：加法法则变为 $x+y=x+y$。

:::frage 这些我在学校就知道了。为什么还要证明？
对 $\mathbb{Q}$ 和 $\mathbb{R}$ 来说，这些规则是熟悉的。但它们不在公理之中，只有证明才说明它们在哪里成立：在每个域中。而学校里的规则“平方不为负”却不能从这份清单推出，并在[第 2 部分](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)失效。此外，这也是在用结果已知的内容练习推理。
:::

:::aufgabe 练习 4 ★★ 在域中证明
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

证明：$(x+y=0\wedge x+z=0)\Rightarrow y=z$。写出每一步所用的公理。

</li>

<li>

证明 $(x+y)(x-y)=x^2-y^2$，并指出何处用到 (AM) 和 (M1)。

</li>

<li>

在域 $\{0,1\}$ 中，$1+1=0$，$1\cdot1=1$：$-1$ 是什么？检验 $(-1)(-1)=1$。

</li>

</ol>

:::loesung
(a) 由 $x+y=0=x+z$ 得 $(-x)+(x+y)=(-x)+(x+z)$。用 (A2)、(A1)、(A4) 变为 $0+y=0+z$，再用 (A1)、(A3) 变为 $y=z$。 (b) (AM) 和 (M1)：$(x+y)(x-y)=(x+y)x+(x+y)(-y)=x^2+yx-xy-y^2=x^2-y^2$，其中由 (M1) 得 $yx=xy$，由 $(-1)x=-x$ 得 $(x+y)(-y)=-(x+y)y$。 (c) $1+1=0$ 表示 $-1=1$。于是 $(-1)(-1)=1\cdot1=1$。这是定理 [3.2](#satz-3-2) 中的规则，它在每个域中都成立。
:::
:::
