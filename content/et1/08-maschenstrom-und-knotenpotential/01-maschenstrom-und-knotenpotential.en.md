---
title: Overview: Mesh Current and Node Voltage Analysis
kurz: Overview
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Mesh Current and Node Voltage Analysis
order: 1180100
summary: Why a network gets by with few unknowns
tags: 
lang: en
---

## What this is about

The network from [Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) has six branches. Each carries a current and a voltage, which makes twelve unknowns, and only after long substitution did three equations remain. A circuit with transistors has hundreds of branches. The question of this chapter is: *How few unknowns are enough for an entire network, and how do you write down the equations without rearranging?*



**How to work with this chapter.** Each stage is a short article of its own with the idea, typical questions you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise. Finish one stage before you move on to the next.

:::merke The model network for this chapter
<ul>

<li>

⁠**The network** (Fig. [1](wie-viele-groen-sind-frei.html#abb-1)) has three nodes: ground 0 and the nodes 1 and 2. On the left, a battery with $U_\mathrm q=9$ V and internal resistance $R_1=1\,\mathrm{k\Omega}$ ([Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) feeds it; on the right, a real current source with $I_\mathrm q=4$ mA and $R_5=5\,\mathrm{k\Omega}$ in parallel. Between them lie $R_2=4\,\mathrm{k\Omega}$ from 1 to ground, $R_3=2\,\mathrm{k\Omega}$ from 1 to 2 and $R_4=10\,\mathrm{k\Omega}$ from 2 to ground.

</li>

<li>

⁠**The amplifier** (Stage [8](gesteuerte-quellen-und-verstarker.html#stufe-8)) is the model from [Part 6](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html): input resistance $R_\mathrm i=2\,\mathrm{k\Omega}$, controlled current source with $g=50$ mS, output resistance $R_\mathrm o=20\,\mathrm{k\Omega}$, load $R_\mathrm L=5\,\mathrm{k\Omega}$.

</li>

<li>

⁠**Units:** All calculations use V, mA, k$\Omega$ and mS. Because $\mathrm{k\Omega\cdot mA}=\mathrm V$ and $\mathrm{mS\cdot V}=\mathrm{mA}$, no powers of ten appear. The script `rechnung_kap8.py` recalculates all the numbers.

</li>

</ul>
:::
