---
title: Stage 2: Using symmetry
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Sources and Equivalent Sources
order: 1150400
summary: Some networks contain no groups.
tags: half circuit
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
Some networks contain no groups. Symmetry then supplies nodes of equal potential, and connecting them creates groups.
:::

**The idea.** If two nodes are at the same potential, the voltage between them is zero. A wire between them therefore carries no current, and nothing changes if you add it. Conversely, you may cut a current-free branch. Symmetry reveals which nodes these are, without any calculation.

:::satz Theorem 2.1 (Two symmetry rules)
<span class="anker" id="satz-2-1"></span>

For a network of resistors with the terminals A and B:

<ol>

<li>

If mirroring or rotating maps the network onto itself while A and B stay in place, nodes that coincide have the same potential. You may connect them. A resistor between them carries no current.

</li>

<li>

If mirroring maps the network onto itself while A and B swap places, every point on the mirror axis is at the mean value $\frac12(\varphi_\mathrm{A}+\varphi_\mathrm{B})$. You may connect all of them and calculate only one side, the __half circuit__:

<span class="anker" id="gl-2-1"></span>
$$R_\mathrm{AB}=2\,R_\mathrm{A,axis}. \tag{2.1}$$

</li>

</ol>
:::

⁠**How to read it:** $R_\mathrm{A,axis}$ is the resistance between A and the axis connected into one node. A resistor crossing the axis splits into two half resistors, and its center lies on the axis. A resistor along the axis has both ends at the same potential and carries no current. **Validity:** The symmetry must also cover the values. A single deviating resistor destroys it.

:::herleitung The potentials follow from the symmetry
Rule 1: The mirrored network has the same components, the same terminals and the same voltage, hence the same equations. These have exactly one solution. Two nodes that coincide must therefore have the same potential.

Rule 2: Let the reference point lie in the middle, so $\varphi_\mathrm{A}=+\frac12U$ and $\varphi_\mathrm{B}=-\frac12U$. Mirroring swaps A and B, so it acts like reversing the polarity of the voltage. In a linear network, reversing the polarity inverts every potential (Stage [8](uberlagerung.html#stufe-8)). For a point $P$ and its mirror image $P'$, therefore, $\varphi(P')=-\varphi(P)$. A point on the axis is its own mirror image, so $\varphi=-\varphi$ and thus $\varphi=0$, the mean value. The two halves are equal and in series, which gives [(2.1)](#gl-2-1).
:::

:::abbildung et1/k5symmetrie 2
Seven identical resistors of 14 $\Omega$ each. Left, the network with the potentials for 16 V at A. The mirror axis runs through L and through the center of the resistor between E and F, which therefore splits into twice 7 $\Omega$. Right, the half circuit.
:::

::::beispiel
In Fig. [2](#abb-2), mirroring swaps A and B as well as E and F, so Rule 2 applies. In the half circuit, $14\,\Omega\parallel7\,\Omega=4.67\,\Omega$ lies between E and the axis. With the path from A to E that makes 18.67 $\Omega$. In parallel with the left branch this gives $R_\mathrm{A,axis}=14\,\Omega\parallel18.67\,\Omega=8\,\Omega$, so $R_\mathrm{AB}=16\,\Omega$, again the load from the reference model. **Check** with the potentials in the figure: from A to L flows $8\,\mathrm{V}/14\,\Omega=0.571$ A, from A to E flows $6\,\mathrm{V}/14\,\Omega=0.429$ A. The sum is 1 A, as $16\,\mathrm{V}/16\,\Omega$ demands.
::::

:::abbildung et1/k5wuerfel 3
Cube of twelve identical resistors with the voltage across the space diagonal. A rotation about this diagonal maps the three neighbors of A onto one another, and likewise the three neighbors of B. Connecting them produces a chain of three groups.
:::

**The resistor cube.** Twelve edges of $R=12\,\Omega$ each, the terminals at opposite corners (Fig. [3](#abb-3)). By Rule 1 the three neighbors of A are at the same potential, and so are the three neighbors of B. Six edges run between these groups of three. The result is a chain:

$$R_\mathrm{AB}=\frac R3+\frac R6+\frac R3=\frac56R=10\,\Omega.$$

At 5 V, 0.5 A flows. It divides among three edges with 167 mA each, then among six with 83 mA each, then among three again.

:::frage Isn't connecting them an intervention in the circuit?
In the drawing yes, in the currents no. Current could flow through the new wire only if there were a voltage between its ends. There is none. So no current in the rest of the network changes. The method holds only as long as the potentials really are equal.
:::

:::aufgabe Exercise 2 ★ Predicting no current
<span class="anker" id="aufg-2"></span>

From A, 10 $\Omega$ leads to node C and 30 $\Omega$ to node D; from C, 20 $\Omega$ and from D, 60 $\Omega$ lead to B. Between C and D lies a cross resistor $R_\mathrm{Q}$ (the bridge from [Part 4](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)). (a) Show that C and D have the same potential, even without symmetry. (b) Calculate $R_\mathrm{AB}$ for $R_\mathrm{Q}\to\infty$ and for $R_\mathrm{Q}\to0$. (c) What follows for $R_\mathrm{Q}=47\,\Omega$?

:::loesung
(a) Without current through $R_\mathrm{Q}$, both branches are voltage dividers with the same ratio: $\frac{20}{10+20}=\frac{60}{30+60}=\frac23$. C and D are then at the same potential, and no current really flows through $R_\mathrm{Q}$. That is the one solution of the network (the balance from [Part 4](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)).

(b) $R_\mathrm{Q}\to\infty$: $(10\,\Omega+20\,\Omega)\parallel(30\,\Omega+60\,\Omega)=22.5\,\Omega$. $R_\mathrm{Q}\to0$: $10\,\Omega\parallel30\,\Omega+20\,\Omega\parallel60\,\Omega=7.5\,\Omega+15\,\Omega=22.5\,\Omega$.

(c) The same: 22.5 $\Omega$. The cross resistor carries no current, so its value plays no role.
:::
:::

:::aufgabe Exercise 3 ★★ Cube across the face diagonal
<span class="anker" id="aufg-3"></span>

Apply the voltage to two corners of the same cube face that are diagonally opposite each other, $R=12\,\Omega$. Hint: Both rules help. Which four corners are at the mean value? Calculate $R_\mathrm{AB}$.

:::loesung
Let the terminals be A and B. C and D are the two corners that are neighbors of both A and B. Above C and D lie E and F in the other face, above A lies P, above B lies Q. If you mirror in the plane that is perpendicular to the line AB and passes through its midpoint, A and B swap places, and so do P and Q. C, D, E, F lie in this plane, so by Rule 2 they are at the mean value.

Half circuit from A to the axis: via C and D, $R$ each, together $\frac R2$. Via P: $R$, then from P to E and to F, $R$ each, together $R+\frac R2=\frac32R$. In parallel: $\frac R2\parallel\frac32R=\frac38R$. Thus $R_\mathrm{AB}=\frac34R=9\,\Omega$.
:::
:::
