---
title: From the ground up: Three equations, three unknowns
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Mesh Current and Node Voltage Analysis
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Chapter 8: Mesh Current and Node Voltage Analysis
order: 1180200
summary: Why a network gets by with few unknowns
tags: symmetric, conductance
lang: en
---

Both methods end in a linear system of equations $\mathbf M\,\mathbf x=\mathbf b$, that is, a matrix times a column vector ([Chapter 6](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). $\mathbf x$ contains the unknowns, $\mathbf b$ the known right-hand side. Each row of the matrix is an equation, each column belongs to an unknown. For two unknowns, the determinant $\det\mathbf M=a\,d-b\,c$ is familiar. For three unknowns, you go through the first row. Each number is multiplied by the determinant that remains after deleting its row and column, and the signs alternate ($+,-,+$):

<span class="anker" id="gl-0-1"></span>
$$\det\begin{pmatrix}a&b&c\\d&e&f\\p&q&r\end{pmatrix}=a\,(e\,r-f\,q)-b\,(d\,r-f\,p)+c\,(d\,q-e\,p). \tag{0.1}$$

:::satz Theorem 0.1 (Cramer's rule)
<span class="anker" id="satz-0-1"></span>

If $D=\det\mathbf M\neq0$, then $\mathbf M\,\mathbf x=\mathbf b$ has exactly one solution. Its $i$-th component is

<span class="anker" id="gl-0-2"></span>
$$x_i=\frac{D_i}{D}. \tag{0.2}$$

$D_i$ is the determinant of the matrix in which column $i$ has been replaced by $\mathbf b$.
:::

:::herleitung Cramer with two unknowns
From $a\,x+b\,y=e$ and $c\,x+d\,y=f$ you get an equation free of $y$: $d$ times the first minus $b$ times the second equation gives $(a\,d-b\,c)\,x=e\,d-b\,f$. On the left stands $D\,x$, on the right the determinant with $(e,f)$ in column 1. With more unknowns it works the same way.
:::

Example: $2x+y=5$ and $x+3y=5$ have $D=5$, $D_1=10$, $D_2=5$, so $x=2$, $y=1$. The rule is suitable for hand calculation up to about four unknowns, especially if the matrix contains many zeros. A matrix is called __symmetric__ if it does not change when reflected in the main diagonal (from top left to bottom right). The __conductance__ $G=1/R$ ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) has the unit siemens: $1\,\mathrm{mS}=1/\mathrm{k\Omega}$.
