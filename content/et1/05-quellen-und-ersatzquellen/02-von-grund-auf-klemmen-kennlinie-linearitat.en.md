---
title: From the ground up: Terminals, characteristic curve, linearity
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Sources and Equivalent Sources
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Chapter 5: Sources and Equivalent Sources
order: 1150200
summary: Why two numbers replace an entire network
tags: terminal, one-port, characteristic curve, Open circuit, linear
lang: en
---

A __terminal__ is a connection point to the outside. A __one-port__ is a network with exactly two terminals that form a pair: the current flowing out at A comes back in at B, because charge is not lost (node rule, [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). A one-port therefore has only one current and one voltage. It is a two-terminal element from [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), even if it contains many components inside. The __characteristic curve__ is the relationship between these two quantities. In this chapter it always appears in the same diagram: terminal current horizontal, terminal voltage vertical.

The reference arrows apply throughout the chapter: $U_\mathrm{AB}=\varphi_\mathrm{A}-\varphi_\mathrm{B}$ counts from A to B, $I_\mathrm{A}$ counts out of terminal A. For the connected load both arrows point in the same direction (passive sign convention, [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)), for the one-port itself in opposite directions (active sign convention). If both are positive, the one-port delivers power. __Open circuit__ means: the terminals are open, $I_\mathrm{A}=0$. Short circuit means: the terminals are connected by a wire, $U_\mathrm{AB}=0$.

A component is __linear__ if its current is proportional to its voltage. A resistor is linear as long as $R$ does not depend on the current: its characteristic curve is a straight line through the origin. An incandescent lamp or a diode ([Chapter 9](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) is not. The symbol $\parallel$ stands for the resistance of a parallel connection, $R_1\parallel R_2=\frac{R_1R_2}{R_1+R_2}$ ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). It binds more tightly than the plus sign, as multiplication does.
