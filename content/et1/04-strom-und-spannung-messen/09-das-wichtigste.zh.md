---
title: 要点
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电流与电压的测量
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: 第 4 章：电流与电压的测量
order: 1140900
summary: 为什么每台测量仪表都会改变电路 以及如何仍然测得准确
tags: 电流表, 电压表, 电流正确的测量, 电压正确的测量, 惠斯通电桥, 平衡
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

__电流表__（测量电流的仪表）串联在电路中，把自己的内阻加入电路。__电压表__（测量电压的仪表）并联在电路上，开辟了第二条电流通路。两者显示的都是被改变后的电路的值。

</li>

<li>

电流表的相对误差约为 $R_\mathrm i/R$，电压表的相对误差约为 $R/R_\mathrm i$。若同时测量两者，只有一个读数是正确的：__电流正确的测量__（电流正确）或__电压正确的测量__（电压正确）。

</li>

<li>

__惠斯通电桥__（两个分压器接在同一电源上，中间接一台仪表）用于比较电阻。在__平衡__状态（调到读数为零）下，没有电流流过仪表。因此，它的内阻、刻度和电源电压都从结果 $R_4=R_3R_2/R_1$ 中消失了。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

测量仪表是一个电阻，显示的是被改变后的电路的值。

</li>

<li>

电流表：$I_R/I_R'=1+R_\mathrm i/R$。电压表：$U_L/U_L'=1+R_L/R_\mathrm i$。

</li>

<li>

扩展量程：$R_\mathrm{Shunt}=R_\text{旧}I_\text{旧}/(I_\text{新}-I_\text{旧})$ 和 $R_\mathrm V=R_\text{旧}(\alpha-1)$。

</li>

<li>

电流正确 $U/I=R+R_\mathrm{iA}$ 用于大 $R$，电压正确 $U/I=R\parallel R_\mathrm{iV}$ 用于小 $R$。

</li>

<li>

平衡：$R_4=R_3R_2/R_1$，与内阻、刻度和电源电压无关。

</li>

<li>

不平衡：$U_\mathrm d\approx\frac14U_\mathrm q\,\Delta R/R$。没有公共电压，小量程就够了。

</li>

</ul>
:::
