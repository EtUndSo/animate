---
title: Von Grund auf: Gesteuerte Quellen und Matrizen
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Zweitore
order: 1160200
summary: Warum vier Zahlen ein ganzes Netzwerk ersetzen und jede Parameterform nur eine andere Wahl ist
tags: gesteuerte Quelle, Matrix, Determinante, inverse Matrix, Einheitsmatrix
lang: de
---

Eine ideale Quelle aus [Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) liefert einen festen Wert. Eine __gesteuerte Quelle__ liefert einen Wert, der einer anderen Spannung oder einem anderen Strom an anderer Stelle der Schaltung proportional ist. Ihr Schaltzeichen ist eine Raute. Die Abkürzungen kommen aus dem Englischen (voltage bzw. current controlled voltage bzw. current source).

| Name | Kürzel | Gesetz | Faktor |
|---|---|---|---|
| spannungsgesteuerte Spannungsquelle | VCVS | $U=\mu\,U_\mathrm{s}$ | ohne Einheit |
| stromgesteuerte Spannungsquelle | CCVS | $U=r\,I_\mathrm{s}$ | in $\Omega$ |
| spannungsgesteuerte Stromquelle | VCCS | $I=g\,U_\mathrm{s}$ | in S |
| stromgesteuerte Stromquelle | CCCS | $I=\beta\,I_\mathrm{s}$ | ohne Einheit |

Der Index s steht für die steuernde Größe. Das bekannteste Beispiel ist der Bipolartransistor ([Teil 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)): Ein kleiner Basisstrom steuert einen großen Kollektorstrom. Die Energie dafür kommt aus der Versorgungsspannung, das Steuersignal liefert nur die Information. Steuergröße und Quelle sitzen an verschiedenen Stellen, deshalb ist jede gesteuerte Quelle von Natur aus ein Zweitor.

Eine __Matrix__ ist ein rechteckiges Zahlenschema, hier fast immer mit zwei Zeilen und zwei Spalten. Fett gedruckte Buchstaben stehen für Matrizen und für Spalten aus zwei Größen. Beim Multiplizieren wird jede Zeile der linken Matrix mit jeder Spalte der rechten verrechnet, Element mal Element, dann addiert:

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}a\,x+b\,y\\c\,x+d\,y\end{pmatrix},\qquad \begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}e&f\\g&h\end{pmatrix}=\begin{pmatrix}a\,e+b\,g&a\,f+b\,h\\c\,e+d\,g&c\,f+d\,h\end{pmatrix}.$$

Bei zwei Matrizen kommt es auf die Reihenfolge an. Addiert werden Matrizen Element für Element. Die Zahl $\det\mathbf M=a\,d-b\,c$ heißt __Determinante__. Ist sie nicht null, gibt es die __inverse Matrix__, die $\mathbf y=\mathbf M\,\mathbf x$ nach $\mathbf x$ auflöst:

$$\mathbf x=\mathbf M^{-1}\mathbf y,\qquad \mathbf M^{-1}=\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac{1}{a\,d-b\,c}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$

Das Produkt $\mathbf M\,\mathbf M^{-1}$ ist die __Einheitsmatrix__ $\mathbf 1$ mit Einsen auf der Diagonale und Nullen sonst. Sie ändert nichts, womit man sie multipliziert.
