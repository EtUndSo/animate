---
title: Stage 2: The transmission-line equations
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Orthogonal Expansion and Transmission Lines
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Chapter 8: Orthogonal Expansion and Transmission Lines
order: 3280300
summary: So far, lines were ideal connections.
tags: per-unit-length parameters
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
So far, lines were ideal connections. If a line is long compared with the wavelength, a signal needs a noticeable time to travel through it. This stage sets up the equations that describe this.
:::

**The idea.** The line is divided into short pieces of length $\mathrm{d} s$. Each piece has a series resistance and a series inductance (the outgoing and return conductors), plus a shunt capacitance and a shunt conductance (between the conductors). For a uniform line these quantities are proportional to the length: $R'\mathrm{d} s$, $L'\mathrm{d} s$, $C'\mathrm{d} s$, $G'\mathrm{d} s$, with the __per-unit-length parameters__ (line constants) $R'$, $L'$, $C'$, $G'$ (values per meter, Fig. [1](#abb-1)).

:::abbildung et3/k8element 1
Equivalent circuit of a short line segment of length $\mathrm{d} s$ with the per-unit-length parameters $R'$, $L'$, $G'$, $C'$.
:::

:::satz Theorem 2.1 (Transmission-line equations, telegrapher's equations)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$\frac{\partial u}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)i,\qquad\frac{\partial i}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)u. \tag{2.1}$$
:::

:::herleitung Transmission-line equations
Kirchhoff's voltage law around the piece: $u=R'\mathrm{d} s\,i+L'\mathrm{d} s\,\frac{\partial i}{\partial t}+\bigl(u+\frac{\partial u}{\partial s}\mathrm{d} s\bigr)$, so $\frac{\partial u}{\partial s}\mathrm{d} s=-R'\mathrm{d} s\,i-L'\mathrm{d} s\,\frac{\partial i}{\partial t}$. Kirchhoff's current law: part of the current $i$ flows away through $G'\mathrm{d} s$ and $C'\mathrm{d} s$, $i=G'\mathrm{d} s\,u+C'\mathrm{d} s\,\frac{\partial u}{\partial t}+\bigl(i+\frac{\partial i}{\partial s}\mathrm{d} s\bigr)$. Divide by $\mathrm{d} s$. (Strictly speaking, the current law contains the voltage at the end of the piece; the difference is of second order in $\mathrm{d} s$.)
:::

⁠**How to read it:** The voltage drops along the line because current flows through the series elements. The current decreases because it leaks away through the shunt elements between the conductors. The two equations couple $u$ and $i$ in space and time.
