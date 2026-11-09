---
title: 第 4 阶段：负反馈
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 运算放大器
order: 1210600
summary: 没有反馈时，运放是一个开关。本阶段说明，为什么把输出的一部分送回去就能使输入差值几乎为零，以及为什么此时增益不再取决于 A 。
tags: 反馈, 正反馈, 同相放大器, 电压跟随器
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
没有反馈时，运放是一个开关。本阶段说明，为什么把输出的一部分送回去就能使输入差值几乎为零，以及为什么此时增益不再取决于 $A$。
:::

**基本思路。** __反馈__是指：输出量的一部分回到输入端。如果它抵消原因，就是负反馈；如果它加强原因，就是__正反馈__。对运放来说，通往负输入端的路径构成负反馈，因为那里的每个电压都以负号起作用。

在__同相放大器__中，$U_\mathrm{E}$ 接正输入端（图 [6](#abb-6)）。由 $R_2$ 和 $R_1$ 组成的分压器把输出的五分之一报告给负输入端。现在加上 $U_\mathrm{E}=1$ V。起初 $U_\mathrm{A}=0$，所以 $\varphi_-=0$，$U_\mathrm{D}=1$ V。目标值 $A\,U_\mathrm{D}$ 将是 100 kV，输出向上运行。输出为 4 V 时，$\varphi_-=0.8$ V，还差 200 mV。4.9 V 时差 20 mV，4.99 V 时只差 2 mV，目标已缩小到 200 V。只有当两者相等时，输出才追上目标：$A\,U_\mathrm{D}=U_\mathrm{A}$。这发生在 $U_\mathrm{A}\approx5$ V、$U_\mathrm{D}=5\,\mathrm{V}/100000=50$ µ V 处。下降也会立即得到纠正：输出下降时，$\varphi_-$ 下降，$U_\mathrm{D}$ 增大，输出又上升。

因此，这个小差值不是器件的基本定律，而是环路的结果。它不可能为零，因为没有差值就没有输出。

:::satz 定理 4.1 (负反馈放大器)
<span class="anker" id="satz-4-1"></span>

若把输出的比例 $\beta$ 送到负输入端，$U_\mathrm{E}$ 接正输入端，则在线性范围内

<span class="anker" id="gl-4-1"></span>
$$U_\mathrm{D}=\frac{U_\mathrm{E}}{1+A\beta},\qquad G=\frac{U_\mathrm{A}}{U_\mathrm{E}}=\frac{A}{1+A\beta}=\frac1\beta\cdot\frac{1}{1+\dfrac1{A\beta}}. \tag{4.1}$$

当 $A\beta\gg1$ 时，$G\approx1/\beta$，相对偏差为 $-1/(A\beta)$。$A$ 的变化被削弱 $1+A\beta$ 倍：

<span class="anker" id="gl-4-2"></span>
$$\frac{\Delta G}{G}\approx\frac{1}{1+A\beta}\cdot\frac{\Delta A}{A}. \tag{4.2}$$

对分压器，$\beta=R_1/(R_1+R_2)$，即 $G\approx1+R_2/R_1$。
:::

⁠**如何理解：**$\beta$ 是反馈比例，介于 0 和 1 之间，这里为 0.2。$G$ 是整个电路的增益。$A\beta$ 是环路增益：$U_\mathrm{D}$ 的一个小变化被放大 $A$ 倍，再经 $\beta$ 削弱后报告回来。这里 $A\beta=20000$，这就是使偏差保持很小的裕量。**适用条件：**$U_\mathrm{A,min}<U_\mathrm{A}<U_\mathrm{A,max}$，输入电流远小于分压器电流，$A$ 取所考虑频率下的值（第 [10](wo-die-regeln-enden.html#stufe-10) 阶段）。

:::herleitung 平衡和运动中的环路
平衡：$U_\mathrm{A}=A\,U_\mathrm{D}$，$U_\mathrm{D}=U_\mathrm{E}-\beta\,U_\mathrm{A}$。代入得 $U_\mathrm{D}=U_\mathrm{E}-A\beta\,U_\mathrm{D}$，由此得 [(4.1)](#gl-4-1)。$G$ 对 $A$ 求导得 $\mathrm{d} G/\mathrm{d} A=1/(1+A\beta)^2$，除以 $G$ 即得 [(4.2)](#gl-4-2)。

运动：在运放内部，与 $U_\mathrm{D}$ 成正比的电流给一个电容充电。因此输出不能跳变，而是追赶其目标值：$\tau\,\mathrm{d} U_\mathrm{A}/\mathrm{d} t=A\,U_\mathrm{D}-U_\mathrm{A}$，这里 $\tau=A/(2\pi f_\mathrm{T})=15.9$ ms。这就是[第 3 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html) RC 电路的方程。代入 $U_\mathrm{D}=U_\mathrm{E}-\beta\,U_\mathrm{A}$ 得

$$\tau\,\frac{\mathrm{d} U_\mathrm{A}}{\mathrm{d} t}=A\,U_\mathrm{E}-(1+A\beta)\,U_\mathrm{A}.$$

$U_\mathrm{A}$ 前面的系数为负，所以任何偏差都会衰减：$U_\mathrm{A}(t)=G\,U_\mathrm{E}\,(1-\mathrm{e}^{-t/\tau_G})$，其中 $\tau_G=\tau/(1+A\beta)=0.80$ µ s。环路比运放本身快 20001 倍。
:::

:::abbildung et1/k11schleife 5
左：环路的框图：在求和点减去 $\beta\,U_\mathrm{A}$。右：线性模型对从 0 到 1 V 阶跃的响应：$U_\mathrm{A}$ 以 $\tau_G=0.80$ µ s 上升到 5 V，$U_\mathrm{D}$ 从 1 V 降到 50 µ V。
:::

::::beispiel
当 $A\beta=20000$ 时，1 V 输入得到 $U_\mathrm{A}=4.99975$ V，与理想值 5 V 的偏差为 0.005 % $=1/(A\beta)$。不同器件相差四倍：

| $A$ | $U_\mathrm{D}$ | $U_\mathrm{A}$ | 与 5 V 的偏差 |
|---|---|---|---|
| 50000 | 99.99 µ V | 4.99950 V | $-0.0100$ % |
| 100000 | 50.00 µ V | 4.99975 V | $-0.0050$ % |
| 200000 | 25.00 µ V | 4.99988 V | $-0.0025$ % |

$A$ 变化 300 % 时，$G$ 只变化 0.0075 %。这是用增益换精度：100000 变成 5，但结果由两个电阻决定。
::::

⁠**简而言之：**增益是反馈比例的倒数。**极限情况：**$A\to\infty$ 时 $U_\mathrm{D}\to0$，$G=1/\beta$。$\beta\to0$ 时 $G\to A$，没有反馈，只剩开环。

**输入与输出。** 在正输入端，$r_\mathrm{e}$ 上只有 $U_\mathrm{D}=50$ µ V，流过 50 pA，是分压器电流 100 µ A 的两百万分之一。输入电阻因此升到 $r_\mathrm{e}(1+A\beta)=20$ G$\Omega$。在输出端，环路抵抗任何负载：负载把 $U_\mathrm{A}$ 拉低一点时，$U_\mathrm{D}$ 增大，内部电压上升，直到损失几乎被补偿。输出电阻降到 $r_\mathrm{a}/(1+A\beta)=3.75$ m$\Omega$。

**电压跟随器。** 取 $R_2=0$、$R_1\to\infty$，输出直接接到负输入端，$\beta=1$，$G=A/(1+A)=0.99999$。这种__电压跟随器__不放大，而是隔离：输入电阻 100 G$\Omega$，输出电阻 0.75 m$\Omega$。一个 1 M$\Omega$ 的电压表接在电压 1 V、内阻 100 k$\Omega$ 的电源上，读数为 0.909 V（[第 4 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)）。前面加上电压跟随器后，读数为 0.99999 V。

:::abbildung et1/k11nichtinv 6
左：同相放大器，标有参考模型中的电位。负输入端只比正输入端低 50 µ V。右：作为极限情况 $\beta=1$ 的电压跟随器。
:::

:::frage 为什么不直接用一个 $G=5$ 的放大器，而要买 100000 倍再扔掉几乎全部？
因为那个 5 会取决于 $B$、$U_\mathrm{Early}$ 和温度：内部变化 1 %，结果就变化 1 %。有了裕量 $A\beta=20000$，这一变化就只剩 $5\cdot10^{-5}$ %。
:::

:::frage 刚才输出太低，于是它跳上去，然后又太高。它不应该永远来回摆动吗？
如果它一步跳到 $A\,U_\mathrm{D}$，确实会这样：每绕环路一圈，误差就乘以 20000。但输出并不跳变。内部电容限制了它的速度，它连续运行，并随 $U_\mathrm{D}$ 的缩小而减速。因此它到达时没有过冲（见上面的推导）。
:::

:::ltspice 测量差值
⁠**绘制：**`voltage` `VE`，值 1，从节点 `p` 到接地点。用受控源 `e` 作运放：输出从节点 `a` 到接地点，控制输入 `p`（正）和 `m`（负），值 `{A}`。`res` `R2` 40k 从 `a` 到 `m`，`R1` 10k 从 `m` 到接地点。

⁠**指令：**`.param A=1e5`，`.step param A list 5e4 1e5 2e5`，`.op`，`.options numdgt=15`，`.meas op ua FIND V(a) AT=1e5`，`.meas op ud FIND V(p,m) AT=1e5`。

⁠**你会看到：**`ua` = 4.99975 V，`ud` = 49.9975 µ V，与计算一致。用 `AT=5e4` 得到 4.99950 V 和 99.99 µ V。做练习 [4](#aufg-4) 时把 `R2` 设为 100k。然后交换 `p` 和 `m`：`.op` 显示 5.00025 V。为什么这在现实中维持不住，见第 [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9) 阶段。
:::

:::aufgabe 练习 4 ★★ 分散性与裕量
<span class="anker" id="aufg-4"></span>

放大器应有 $G=11$，$R_1=10$ k$\Omega$。(a) 选择 $R_2$。$\beta$ 和 $A\beta$ 是多少？(b) $U_\mathrm{A}=5.5$ V 时 $U_\mathrm{D}$ 多大？(c) 计算 $A=50000$ 和 $200000$ 时的 $G$。(d) 要使偏差为 0.1 %，$A$ 至少要多大？(e) $U_\mathrm{E}=2$ V 时会怎样？此时 $U_\mathrm{D}$ 多大？

:::loesung
(a) $1+R_2/R_1=11$，所以 $R_2=100$ k$\Omega$。$\beta=1/11=0.0909$，$A\beta=9091$。 (b) $5.5\,\mathrm{V}/100000=55$ µ V。 (c) $G=10.99758$ 和 $10.99940$，相差 0.016 %。 (d) $1/(1+1/(A\beta))=0.999$ 得 $A\beta=999$，所以 $A\ge10989$。 (e) 计算值为 22 V，输出位于 11 V。这时 $\varphi_-=\beta\cdot11\,\mathrm{V}=1$ V，$U_\mathrm{D}=1$ V，规则不成立。
:::
:::
