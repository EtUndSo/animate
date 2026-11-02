---
title: 第 4 阶段：线路损耗
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 功率、匹配与效率
order: 1170500
summary: 电源和负载之间是线路，它也是一个电阻。本阶段说明为什么大功率要通过高电压传输。
tags: 电压降, 损耗功率, 有用功率, 标称电压
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
电源和负载之间是线路，它也是一个电阻。本阶段说明为什么大功率要通过高电压传输。
:::

**基本思路。** 线路与负载串联，全部电流都必须流过它（图 [5](#abb-5)）。每库仑电荷在到达负载之前，在线路上损失 $R_\text{线路}I$ 焦耳。固定的功率可以用两种方式传输：高电压小电流，或者相反。电压高时，每库仑带来的能量多，所以少量库仑就够了。小电流有双重好处：每库仑损失更少，库仑数也更少。

:::abbildung et1/k7leitung 5
电源、线路和负载。$R_\text{线路}$ 合并了去线和回线。右侧是例题的两种情况。
:::

:::satz 定理 4.1 (线路损耗)
<span class="anker" id="satz-4-1"></span>

电流 $I$ 经电阻为 $R_\text{线路}$ 的线路流向负载时，有

<span class="anker" id="gl-4-1"></span>
$$U_\text{线路}=R_\text{线路}\,I,\qquad P_\text{线路}=U_\text{线路}\,I=R_\text{线路}\,I^2,\qquad P_\text{有用}=(U_\mathrm{q}-U_\text{线路})\,I \tag{4.1}$$

因此

<span class="anker" id="gl-4-2"></span>
$$\frac{P_\text{有用}}{P_\mathrm{q}}=\frac{(U_\mathrm{q}-U_\text{线路})\,I}{U_\mathrm{q}\,I}=1-\frac{U_\text{线路}}{U_\mathrm{q}}. \tag{4.2}$$

对于负载功率相同的两种电压，$P_\mathrm{L}=U_\mathrm{L1}I_1=U_\mathrm{L2}I_2$，有

<span class="anker" id="gl-4-3"></span>
$$\frac{I_1}{I_2}=\frac{U_\mathrm{L2}}{U_\mathrm{L1}},\qquad\frac{P_{\text{线路},1}}{P_{\text{线路},2}}=\left(\frac{U_\mathrm{L2}}{U_\mathrm{L1}}\right)^{\!2}. \tag{4.3}$$
:::

⁠**如何理解：**$U_\text{线路}$ 是沿线路的__电压降__。$P_\text{线路}$ 是__损耗功率__，$P_\text{有用}=P_\mathrm{L}$ 是负载的__有用功率__，$P_\mathrm{q}=U_\mathrm{q}I$ 是电源的功率。$U_\mathrm{L}$ 是负载上的电压。**适用条件：**这些公式适用于直流量和线路电阻。在交流电压和欧姆负载下，它们对有效值成立。

**例。** 负载需要 40 kW，$R_\text{线路}=1\,\Omega$。当 $U_\mathrm{L}=400$ V 时，$I=100$ A，$U_\text{线路}=100$ V，$P_\text{线路}=10$ kW。电源必须提供 500 V，由式 [(4.2)](#gl-4-2)，到达的比例为 $1-100/500=80$ %。在 20 kV 时，$I=2$ A，$U_\text{线路}=2$ V，$P_\text{线路}=4$ W，到达的比例为 99.99 %。电流减小为原来的 50 分之一，损耗减小为原来的 $50^2=2500$ 分之一。**极限情况：**当 $R_\text{线路}\to0$ 时，$U_\text{线路}=0$，式 [(4.2)](#gl-4-2) 给出 1。较远距离的能量传输只有在高电压下才可行，因此电网分级建设。__标称电压__是电网的设计电压：

| 等级 | 标称电压 | 传输距离 | 任务 |
|---|---|---|---|
| 低压 | 230/400 V | 数百米 | 当地的居民和商户 |
| 中压 | 10 kV | 约 10 km 以内 | 大城市配电 |
| 中压 | 20 kV | 约 25 km 以内 | 农村和中等城市配电 |
| 高压 | 110 kV | 约 100 km 以内 | 向中压电网供电 |
| 超高压 | 220 kV，380 kV | 数百至 1000 km 以上 | 国内和欧洲范围的互联 |

高压不能一直引入住宅：空气在约 3 kV/mm 时被击穿（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)），因此架空线路需要几米的间距。变压器在输电时把交流电压升高，在用户之前再把它降下来。

:::frage 按 $P=U^2/R$，功率随电压增大。更高的电压难道不会带来更多损耗吗？
公式没错，但它需要的是同一电阻上的电压。在例题中，电缆上的电压不是 20 kV，而是 $U_\text{线路}=2$ V，$(2\,\mathrm{V})^2/1\,\Omega$ 正是那 4 W。高电压加在负载上。$U_\text{线路}$ 下降，是因为电流下降了。
:::

:::aufgabe 练习 4 ★★ 林边小屋
<span class="anker" id="aufg-4"></span>

一座小屋在 48 V 直流电压下吸收 480 W，引线的 $R_\text{线路}=0.2\,\Omega$。(a) 计算 $I$、$U_\text{线路}$、$P_\text{线路}$、$U_\mathrm{q}$ 以及到达的比例。(b) 对 12 V 下的 480 W 作同样计算。(c) 多大的电压 $U_\mathrm{L}$ 能把损耗限制在负载功率的 1 %？

:::loesung
(a) $I=480\,\mathrm{W}/48\,\mathrm{V}=10$ A，$U_\text{线路}=2$ V，$P_\text{线路}=20$ W，$U_\mathrm{q}=50$ V。到达的比例为 $1-2/50=96$ %。 (b) $I=40$ A，$U_\text{线路}=8$ V，$P_\text{线路}=320$ W，$U_\mathrm{q}=20$ V。到达的比例只有 60 %。电流为四倍，损耗为十六倍。 (c) 由 $R_\text{线路}\,P_\mathrm{L}^2/U_\mathrm{L}^2\le0.01\,P_\mathrm{L}$ 得 $U_\mathrm{L}\ge\sqrt{R_\text{线路}\,P_\mathrm{L}/0.01}=98$ V。
:::
:::
