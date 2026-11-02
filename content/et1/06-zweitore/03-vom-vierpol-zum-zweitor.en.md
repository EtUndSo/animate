---
title: Stage 1: From four-pole to two-port
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Two-Port Networks
order: 1160300
summary: A network with four terminals has three independent currents and three independent voltages.
tags: four-pole, port quantities, four-pole theory, input, output, forward direction, reverse direction, elementary two-ports
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
A network with four terminals has three independent currents and three independent voltages. This stage shows which condition turns these into two currents and two voltages.
:::

**The idea.** A __four-pole__ is a network with four terminals. The node rule ([Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) holds for the whole network as for one large node: One terminal current is fixed by the other three. The mesh rule likewise ties together the voltages between the terminals. Now if a two-terminal element, say a source, is connected to terminals 1 and 1$'$, a further statement is added: A two-terminal element has only two connections. Every charge it gives off at one it takes back at the other. The current that enters the network at terminal 1 must return at terminal 1$'$. The terminal pair behaves like a single access with one current and one voltage (Fig. [1](#abb-1) left).

:::definition Definition 1.1 (Four-pole, port, two-port)
<span class="anker" id="satz-1-1"></span>

At a four-pole with the terminals 1, 1$'$, 2, 2$'$, let all terminal currents be counted toward the network. It always holds that

<span class="anker" id="gl-1-1"></span>
$$I_1+I_{1'}+I_2+I_{2'}=0,\qquad U_{11'}+U_{1'2'}-U_{22'}+U_{21}=0. \tag{1.1}$$

A terminal pair is a port if the port condition holds. A four-pole with two ports is a two-port:

<span class="anker" id="gl-1-2"></span>
$$I_{1'}=-I_1,\qquad I_{2'}=-I_2. \tag{1.2}$$

Its __port quantities__ are $U_1=U_{11'}$, $I_1$, $U_2=U_{22'}$ and $I_2$.
:::

⁠**How to read it:** [(1.1)](#gl-1-1) leaves three currents and three voltages free. The first equation is the node rule, the second the mesh rule around the loop $1\to1'\to2'\to2\to1$. [(1.2)](#gl-1-2) removes one current each. The voltage $U_{1'2'}$ also drops out of the description: No current flows between the ports on the outside, so no power is transferred through it. Whether a four-pole becomes a two-port is decided by what is connected to it: If a two-terminal element is connected to each terminal pair, [(1.2)](#gl-1-2) holds automatically. A branch running outside from port to port breaks it (Fig. [1](#abb-1) right). The historical name four-pole lives on in __four-pole theory__.

:::abbildung et1/k6tor 1
Left: source, two-port and load. At both ports, each current returns at the second terminal, and energy flows in the forward direction from port 1 to port 2. Right: An external branch from terminal 1 to terminal 2 carries the current $I_\mathrm{x}$. Now a different current flows into 1 than out of 1$'$, and the terminal pairs are no longer ports.
:::

A two-port is a conceptually closed unit, accessible only through its ports. Its properties are fixed by the relations between the port quantities, and these can be calculated or measured. Usually a source is connected to port 1, the __input__, and a load to port 2, the __output__. Energy then flows in the __forward direction__ $1\to2$; the opposite direction is called the __reverse direction__. The two-port is a basic structure: Controlled sources are two-ports, transformers, amplifiers and transistors have three or four connections, large two-ports can be built from __elementary two-ports__, and two-ports joined together form a two-port again. The simplest examples are the voltage divider and the current divider ([Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

**Structure and classification.** If a two-port has a continuous line from terminal 1$'$ to 2$'$, the __ground line__, it is called __unbalanced__ (Fig. [2](#abb-2) left). It is really a three-pole, an improper four-pole. Network models of transistors and amplifiers are of this kind. A two-port that, like the bridge circuit, has no such line and is built as a mirror image about a center line is called __balanced__. By their behavior, two-ports are divided into linear time-invariant, time-varying and nonlinear ones. This chapter deals with the linear time-invariant ones.

:::abbildung et1/k6masse 2
Left: The T two-port of the reference model is unbalanced; in red, the ground line from 1$'$ to 2$'$. Right: The bridge circuit of two resistor pairs has no continuous line between the ports; it is balanced. Stage [3](impedanzform-und-leerlaufversuch.html#stufe-3) calculates both.
:::

**Example.** In the operation of the T two-port (Stage [4](das-zweitor-im-betrieb.html#stufe-4)), $I_1=250$ mA flows in and $I_{1'}=-250$ mA; the load draws 50 mA, so $I_2=-50$ mA and $I_{2'}=+50$ mA. The sum in [(1.1)](#gl-1-1) is zero. **Limiting case:** If port 2 is open, $I_2=I_{2'}=0$, and to the outside the two-port acts like a two-terminal element at port 1.

:::frage The ground line connects 1$'$ and 2$'$. Doesn't current flow from port to port there after all?
Yes, on the inside. In the ground line of the T two-port, 50 mA runs from 2$'$ to the foot of $R_\mathrm{b}$. But the port condition only speaks of what happens at the terminals. Inside, any current may flow, as long as each terminal current comes back at its partner terminal.
:::

:::aufgabe Exercise 1 ★ Counting at the terminals
<span class="anker" id="aufg-1"></span>

At a four-pole you measure $I_1=30$ mA, $I_{1'}=-30$ mA, $I_2=-10$ mA, and also $U_{11'}=6$ V, $U_{1'2'}=0$ V, $U_{22'}=2$ V.

<ol class="al">

<li>

What is $I_{2'}$? Are both terminal pairs ports?

</li>

<li>

What is $U_{21}$?

</li>

<li>

How many currents would you have to measure at least to know all the terminal currents, for the four-pole and for the two-port?

</li>

</ol>

:::loesung
(a) From [(1.1)](#gl-1-1): $I_{2'}=-(30-30-10)\,\mathrm{mA}=+10$ mA. We have $I_{1'}=-I_1$ and $I_{2'}=-I_2$, so both pairs are ports. (b) $U_{21}=-U_{11'}-U_{1'2'}+U_{22'}=-6\,\mathrm{V}-0\,\mathrm{V}+2\,\mathrm{V}=-4$ V. (c) For the four-pole three; the fourth follows from the node rule. For the two-port two; the others follow from the port condition.
:::
:::
