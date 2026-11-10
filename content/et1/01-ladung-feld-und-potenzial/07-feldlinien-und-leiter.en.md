---
title: Stage 5: Field lines and conductors
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Charge, Field and Potential
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Chapter 1: Charge, Field and Potential
order: 1110700
summary: Field lines show an entire field at a glance.
tags: electrostatic induction, field line, sources, sinks, shielding, uniform, fringing field
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Field lines show an entire field at a glance. They also make clear what a metal does to a field.
:::

**The idea.** Placing the field arrows end to end produces lines (Fig. [6](#abb-6)). They can be made visible with elongated grains in oil: the field shifts the charges in each grain slightly, and the grain turns in the field direction. In metal, the free electrons move until no force acts on them any more. This displacement is called __electrostatic induction__.

:::satz Theorem 5.1 (Field lines of charges at rest)
<span class="anker" id="satz-5-1"></span>

A __field line__ is a curve whose tangent at each point has the direction of $\vec E$; the density of the lines shows the strength of the field. The following hold:

<ol>

<li>

Field lines begin on positive charges (__sources__) and end on negative ones (__sinks__), never in empty space. For a single charge, the other end runs off to infinity.

</li>

<li>

Field lines do not cross.

</li>

<li>

They are perpendicular to the surface of a conductor.

</li>

<li>

Inside a conductor, $\vec E=0$. A charge-free cavity enclosed by the conductor is field-free (__shielding__).

</li>

</ol>
:::

⁠**How to read it:** Rules 1 and 2 hold in empty space; rules 3 and 4 say what metal changes about the field. Nothing flows at sources and sinks; the words mean the beginning and end of the lines. **Validity:** All the rules assume charges at rest; Stage [10](grenze-des-bildes-magnetismus-und-induktion.html#stufe-10) shows fields with closed lines.

:::abbildung et1/k1feldlinien 6
Calculated field lines. Top: with opposite charges they run from $+$ to $-$; with like charges they avoid each other. Bottom left: between two plates they run parallel and equally dense; only at the edge do they bulge outward. Bottom right: metal tube in cross section between two plates. Electrons collect on the left, positive charges remain on the right, inside $E=0$.
:::

:::herleitung Where the rules come from
⁠**Rule 2.** At an intersection, $\vec E$ would have two directions, but the force on a test charge is unique.

⁠**Rule 4, metal.** If there were a field in the metal, the free electrons would keep moving. Rest is reached only when the displaced charges exactly cancel the external field inside. Excess charges sit on the surface.

⁠**Rule 3.** A field component along the surface would push the electrons along it. At rest, only the perpendicular component remains.

⁠**Rule 4, cavity.** The external field ends on the induced charges of the outer side. With no charge in the cavity, a line there would have to run from wall to wall. A charge could gain energy along this line and return at no cost through the field-free metal. That would be energy from nothing, which Stage [6](arbeit-im-feld.html#stufe-6) rules out.
:::

::::beispiel
In the pair of plates, the charge sits on the inner sides of the plates, and the lines run parallel and equally dense from A to B. Equal density means that $\vec E$ is the same everywhere; the field is __uniform__. This holds as long as $d$ is small compared with the plate width; only at the edge does a weaker __fringing field__ bulge outward. The tube in Fig. [6](#abb-6) shows rules 3 and 4; at its apex the field is around twice as strong as without the tube. A closed metal shell protects its interior, which is why you are safe in a car during a thunderstorm.
::::

⁠**Check:** Rule 1 fits Coulomb's law. From a charge, $N$ lines run evenly in all directions and pierce a sphere of area $4\pi r^2$. The density $N/(4\pi r^2)$ falls with $1/r^2$, hence also the factor $4\pi$ in $k=1/(4\pi\varepsilon_0)$. Conversely, shielding is perfect only for an exponent of exactly 2. This gave rise to the measurements from Stage [3](die-kraft-zwischen-ladungen.html#stufe-3): one searched for a residual field in a charged hollow sphere.

:::frage Does a charge fly along the field line?
In general, no. The field line gives the direction of the force, that is, of the acceleration, not of the velocity. Only for straight lines and a start from rest do path and line coincide.
:::

:::aufgabe Exercise 5 ★ Predicting shielding
<span class="anker" id="aufg-5"></span>

First answer with field lines alone, without calculating.

<ol class="al">

<li>

A metal box with no charge of its own stands in the field of a charged rod. How large is the field in the box? Where are the induced charges?

</li>

<li>

A charge $+Q$ is placed at the center of an isolated, neutral hollow metal sphere. Is there a field in the cavity? Is there a field outside?

</li>

</ol>

:::loesung
(a) In the box, $E=0$. The induced charges sit on the outside: facing the rod with the opposite sign, on the far side with the same sign. (b) There is a field in the cavity, because lines start from the charge. They end on the inner wall, which acquires $-Q$ by electrostatic induction. The sphere is neutral, so $+Q$ sits on the outside, and outside there is the field of a charge $+Q$. Shielding protects only the interior from external fields.
:::
:::
