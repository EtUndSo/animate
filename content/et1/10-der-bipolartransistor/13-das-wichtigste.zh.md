---
title: 要点
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 双极型晶体管
order: 1201300
summary: 小电压如何控制流过 截止二极管的大电流
tags: 发射极, 基极, 集电极, 电流增益, 工作点, 负反馈, 跨导
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

__发射极__发出电子，很薄的__基极__让它们通过，__集电极__把它们收集起来。电压 $U_\mathrm{BE}$ 决定有多少电子出发：$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$。截止的集电极二极管的电场把它们抽走，只有很小的剩余部分流经基极，$I_\mathrm{B}=I_\mathrm{C}/B$。系数 $B$ 称为__电流增益__。

</li>

<li>

三个接线端意味着两个独立的电压。因此 $I_\mathrm{C}$ 是 $U_\mathrm{BE}$ 和 $U_\mathrm{CE}$ 上方的一个曲面，每条特性曲线都是它的一个截面。外部电路在这个曲面上选定__工作点__，即晶体管的直流状态。发射极电阻通过__负反馈__把工作点稳定住：结果削弱了自身的原因。

</li>

<li>

对于小信号，切线代替曲线。切线的斜率，即__跨导__ $S=I_\mathrm{C}/U_T$，使晶体管成为一个受控电流源。共发射极电路是发射极接地的标准电路，它的电压增益等于集电极电阻上的直流电压除以 $U_T$。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$，$U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}$。三个接线端意味着两个自由电压，$I_\mathrm{C}$ 是一个曲面，每条特性曲线是一个截面。

</li>

<li>

机理：$U_\mathrm{BE}$ 降低势垒，电子穿过薄基区，截止的 CB 二极管的电场把它们抽走：$I_\mathrm{C}=I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}$，$I_\mathrm{B}=I_\mathrm{C}/B$。基极电流只补充少量损失。

</li>

<li>

工作区：截止区（开路），放大区（$I_\mathrm{C}=B\,I_\mathrm{B}$，$U_\mathrm{CE}\ge0.2$ V），饱和区（$U_\mathrm{CE}=0.2$ V，$I_\mathrm{C}\le B\,I_\mathrm{B}$）。假设、计算、检验。开关：负载线的两端。放大器：放大区，中点。

</li>

<li>

负反馈：$I_\mathrm{C}=(U_\mathrm{q}-U_\mathrm{BE})/\bigl(R_\mathrm{E}(1+1/B)+R_\mathrm{i}/B\bigr)$。电流增大抬高发射极，使 $U_\mathrm{BE}$ 回落。电流镜：$I_\mathrm{C2}=I_\mathrm{ref}/(1+2/B)$。稳压器：$U_\mathrm{A}=U_\mathrm{Z}-U_\mathrm{BE}$。

</li>

<li>

小信号：$S=I_\mathrm{C}/U_T$，$r_\mathrm{BE}=B/S$，$r_\mathrm{CE}\approx U_\mathrm{Early}/I_\mathrm{C}$。切线在 $|u_\mathrm{be}|\ll U_T$ 时成立。

</li>

<li>

共发射极 $A=-U_{R_\mathrm{C}}/U_T$，共集电极 $A\approx1$，共基极 $A=+S\,R_\mathrm{C}$。带 $R_\mathrm{E}$ 时 $A\approx-R_\mathrm{C}/R_\mathrm{E}$。

</li>

</ul>
:::
