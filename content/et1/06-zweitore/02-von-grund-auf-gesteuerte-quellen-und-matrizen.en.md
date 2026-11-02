---
title: From the ground up: Controlled sources and matrices
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Two-Port Networks
order: 1160200
summary: Why four numbers replace a whole network and every parameter form is just another choice
tags: controlled source, matrix, determinant, inverse matrix, identity matrix
lang: en
---

An ideal source from [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) supplies a fixed value. A __controlled source__ supplies a value proportional to another voltage or another current elsewhere in the circuit. Its circuit symbol is a diamond. The abbreviations come from the English names (voltage- or current-controlled voltage or current source).

| Name | Abbreviation | Law | Factor |
|---|---|---|---|
| voltage-controlled voltage source | VCVS | $U=\mu\,U_\mathrm{s}$ | no unit |
| current-controlled voltage source | CCVS | $U=r\,I_\mathrm{s}$ | in $\Omega$ |
| voltage-controlled current source | VCCS | $I=g\,U_\mathrm{s}$ | in S |
| current-controlled current source | CCCS | $I=\beta\,I_\mathrm{s}$ | no unit |

The index s marks the controlling quantity. The best-known example is the bipolar transistor ([Part 10](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)): A small base current controls a large collector current. The energy for this comes from the supply voltage; the control signal supplies only the information. The controlling quantity and the source sit at different places, so every controlled source is by nature a two-port.

A __matrix__ is a rectangular array of numbers, here almost always with two rows and two columns. Bold letters stand for matrices and for columns of two quantities. In multiplication, each row of the left matrix is combined with each column of the right one, element by element, and the results are added:

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}a\,x+b\,y\\c\,x+d\,y\end{pmatrix},\qquad \begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}e&f\\g&h\end{pmatrix}=\begin{pmatrix}a\,e+b\,g&a\,f+b\,h\\c\,e+d\,g&c\,f+d\,h\end{pmatrix}.$$

With two matrices, the order matters. Matrices are added element by element. The number $\det\mathbf M=a\,d-b\,c$ is called the __determinant__. If it is not zero, the __inverse matrix__ exists, which solves $\mathbf y=\mathbf M\,\mathbf x$ for $\mathbf x$:

$$\mathbf x=\mathbf M^{-1}\mathbf y,\qquad \mathbf M^{-1}=\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac{1}{a\,d-b\,c}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$

The product $\mathbf M\,\mathbf M^{-1}$ is the __identity matrix__ $\mathbf 1$ with ones on the diagonal and zeros elsewhere. It changes nothing it is multiplied by.
