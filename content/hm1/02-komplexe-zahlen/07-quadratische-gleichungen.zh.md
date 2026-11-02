---
title: 第 6 阶段：二次方程
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 复数
order: 1220700
summary: 目标原本是求 x 2=-1 的解。本阶段说明 mathbb C 能做到更多：在其中每个二次方程都有解，即使系数是复数。
tags: 二重解, 判别式, 极坐标表示
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
目标原本是求 $x^2=-1$ 的解。本阶段说明 $\mathbb{C}$ 能做到更多：在其中每个二次方程都有解，即使系数是复数。
:::

**基本思路。** 配方只用到域公理，所以在 $\mathbb{C}$ 中也成立。最后剩下方程 $w^2=D$。在 $\mathbb{R}$ 中，它在 $D<0$ 时无解。在 $\mathbb{C}$ 中它总有解：$w^2=D$ 分解为实部和虚部，也就是关于 $w$ 的两个实未知量的两个实方程。

:::satz 定理 6.1 ($\mathbb{C}$ 中的平方根)
<span class="anker" id="satz-6-1"></span>

设 $D=s+\mathrm{i}t\ne0$，其中 $s,t\in\mathbb{R}$。对 $w=u+\mathrm{i}v$（$u,v$ 为实数），$w^2=D$ 等价于 $u^2-v^2=s$ 和 $2uv=t$。恰有两个解 $\pm w$，其中

<span class="anker" id="gl-6-1"></span>
$$u^2=\frac{|D|+s}2,\qquad v^2=\frac{|D|-s}2. \tag{6.1}$$

$u$ 和 $v$ 的符号要选得使 $2uv=t$ 成立。当 $D=0$ 时，$w=0$ 是唯一解。
:::

⁠**如何理解：**$s$ 和 $t$ 是 $D$ 的实部和虚部。若 $t>0$，则 $u$ 和 $v$ 同号；若 $t<0$，则异号。**极限情况：**对实数 $D<0$，$u=0$，$v^2=-D$：解是纯虚数，当 $D=-1$ 时即 $w=\pm\mathrm{i}$。

:::beweis 两个实方程
有 $w^2=u^2-v^2+2\mathrm{i}uv$。比较实部和虚部，得到这两个方程。由 $|w|^2=|w^2|=|D|$ 还可得 $u^2+v^2=|D|$。与 $u^2-v^2=s$ 相加、相减，得式 [(6.1)](#gl-6-1)。等式右边非负，因为 $|s|\le|D|$（第 [5](betrag-und-abstand.html#stufe-5) 阶段，规则 (v)）。反过来，由式 [(6.1)](#gl-6-1) 得到的 $u,v$ 满足 $u^2-v^2=s$ 和 $(2uv)^2=(|D|+s)(|D|-s)=|D|^2-s^2=t^2$。所以 $2uv=\pm t$，而符号的选择确定 $2uv=t$。
:::

:::satz 定理 6.2 ($\mathbb{C}$ 中的二次方程)
<span class="anker" id="satz-6-2"></span>

设 $p,q\in\mathbb{C}$，$D:=p^2/4-q$。方程 $z^2+pz+q=0$ 的解为

<span class="anker" id="gl-6-2"></span>
$$z=-\frac p2\pm w\qquad\text{其中}\qquad w^2=D. \tag{6.2}$$

当 $D\ne0$ 时，这是两个解 $z_+\ne z_-$，满足 $z_++z_-=-p$ 和 $z_+z_-=q$。当 $D=0$ 时，只有 $z=-p/2$，即一个__二重解__。对实数 $p,q$：$D>0$ 给出两个实数解，$D=0$ 给出一个实数解，$D<0$ 给出互相共轭的解 $z=-\frac p2\pm\mathrm{i}\sqrt{-D}$。
:::

⁠**如何理解：**$D$ 称为__判别式__。两个解关于中点 $-p/2$ 点对称（图 [6](#abb-6)）。**适用条件：**$z^2$ 的系数必须为 1。否则先除以它，在 $\mathbb{C}$ 中即使系数是不为零的复数也可以这样做。这类实系数方程描述振荡：一对共轭解对应一个阻尼振荡。

:::herleitung 配方
有 $z^2+pz+q=(z+\frac p2)^2-\frac{p^2}4+q=(z+\frac p2)^2-w^2=(z+\frac p2-w)(z+\frac p2+w)$。乘积为零只有在某个因子为零时才可能（第 [4](dividieren-und-was-verloren-geht.html#stufe-4) 阶段）。由此得式 [(6.2)](#gl-6-2)，并得 $z_++z_-=-p$ 和 $z_+z_-=\frac{p^2}4-w^2=q$。当 $p,q$ 为实数时，$D$ 是实数，当 $D<0$ 时 $w=\pm\mathrm{i}\sqrt{-D}$。
:::

:::abbildung hm1/k2loesungen 6
左：参考模型的实系数方程：解 $3\pm\mathrm{i}$ 互为镜像。右：复系数方程：$z_1$ 和 $z_2$ 关于中点 $2+1.5\mathrm{i}$ 对称。
:::

**例 1，实系数。** $z^2-6z+10=0$ 中 $p=-6$，$q=10$，$D=9-10=-1$，所以 $z=3\pm\mathrm{i}$。这就是 $z_1$ 和 $\overline{z_1}$。检验：和 $6=-p$，积 $|z_1|^2=10=q$。

**例 2，复系数。** 对 $z^2-(4+3\mathrm{i})z+1+7\mathrm{i}=0$，有 $-p/2=2+1.5\mathrm{i}$ 和

$$D=(2+1.5\mathrm{i})^2-(1+7\mathrm{i})=1.75+6\mathrm{i}-1-7\mathrm{i}=0.75-\mathrm{i}.$$

所以 $s=0.75$，$t=-1$，$|D|=\sqrt{0.5625+1}=1.25$。由式 [(6.1)](#gl-6-1) 得 $u^2=1$，$v^2=0.25$。因为 $t<0$，$u$ 和 $v$ 异号：$w=\pm(1-0.5\mathrm{i})$。于是 $z=2+1.5\mathrm{i}\pm(1-0.5\mathrm{i})$，即 $z=3+\mathrm{i}$ 或 $z=1+2\mathrm{i}$。检验：和 $4+3\mathrm{i}=-p$，积 $1+7\mathrm{i}=q$。

⁠**极限情况：**当 $q=0$ 时，式 [(6.2)](#gl-6-2) 给出 $z=-p/2\pm p/2$，即 $z=0$ 和 $z=-p$，与 $z(z+p)=0$ 相符。

:::frage 为什么不能这样算：$\sqrt{-1}\cdot\sqrt{-1}=\sqrt{(-1)(-1)}=1$？
[第 1 部分](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)的法则 $\sqrt{ab}=\sqrt a\sqrt b$ 只对 $a,b\ge0$ 成立。对负数，根号没有定义：$w^2=-1$ 有两个地位相同的解，其中哪一个都不是“那个”平方根。所以本章写 $w^2=D$，而不写 $w=\sqrt D$。
:::

:::aufgabe 练习 8 ★★ 解二次方程
<span class="anker" id="aufg-8"></span>

(a) 解 $z^2+4z+13=0$，并检验和与积。(b) 实系数方程 $z^2+pz+q=0$ 有解 $2-5\mathrm{i}$。第二个解是什么，$p$ 和 $q$ 等于多少？(c) 解 $z^2-3z+3-\mathrm{i}=0$ 并检验。(d) 解 $\mathrm{i}z^2+2z-2\mathrm{i}=0$。

:::loesung
(a) $D=4-13=-9$，所以 $z=-2\pm3\mathrm{i}$。和 $-4=-p$，积 $4+9=13=q$。(b) 系数为实数时，第二个解是共轭解 $2+5\mathrm{i}$。于是 $p=-(2-5\mathrm{i})-(2+5\mathrm{i})=-4$，$q=(2-5\mathrm{i})(2+5\mathrm{i})=29$。

(c) $p=-3$，$q=3-\mathrm{i}$，所以 $D=2.25-3+\mathrm{i}=-0.75+\mathrm{i}$。由 $|D|=\sqrt{0.5625+1}=1.25$，式 [(6.1)](#gl-6-1) 给出 $u^2=0.25$ 和 $v^2=1$。因为 $t=1>0$，$u$ 和 $v$ 同号：$w=\pm(0.5+\mathrm{i})$。所以 $z=1.5\pm(0.5+\mathrm{i})$，即 $z=2+\mathrm{i}$ 或 $z=1-\mathrm{i}$。检验：和 $3=-p$，积 $(2+\mathrm{i})(1-\mathrm{i})=2-2\mathrm{i}+\mathrm{i}-\mathrm{i}^2=3-\mathrm{i}=q$。

(d) 先把 $z^2$ 的系数化为 1：用 $1/\mathrm{i}=-\mathrm{i}$ 除以 $\mathrm{i}$，得 $z^2-2\mathrm{i}z-2=0$。于是 $p=-2\mathrm{i}$，$q=-2$，$D=(-2\mathrm{i})^2/4+2=-1+2=1$。由 $w=\pm1$ 得 $z=\mathrm{i}\pm1$。对 $z=1+\mathrm{i}$ 检验：$\mathrm{i}\cdot2\mathrm{i}+2+2\mathrm{i}-2\mathrm{i}=-2+2=0$。对 $z=-1+\mathrm{i}$ 检验：$\mathrm{i}\cdot(-2\mathrm{i})-2+2\mathrm{i}-2\mathrm{i}=2-2=0$。
:::
:::

**展望。** 平面上的点也可以用绝对值和角度来表示。这样，做乘法时绝对值相乘、角度相加，第 [2](die-komplexe-ebene.html#stufe-2) 阶段的旋转就是 $|\mathrm{i}|=1$、角度为 $90^\circ$ 的特例。这种__极坐标表示__、指数形式和 $n$ 次方根需要正弦、余弦和指数函数，所以留到第 7 部分。
