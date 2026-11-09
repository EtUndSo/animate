---
title: Überblick: Matrizen und lineare Gleichungssysteme
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Matrizen und lineare Gleichungssysteme
order: 1300100
summary: Eine Matrix ist eine lineare Abbildung in Zahlen, ein Gleichungssystem fragt rückwärts nach ihr
tags: lineare Abbildung, Matrix, Kern, Bild, Rang, Matrizenprodukt, lineares Gleichungssystem, Gauß-Algorithmus
lang: de
---

## Worum es geht

Eine Drehung der Ebene bewegt unendlich viele Punkte, trotzdem legen vier Zahlen sie fest. Drei Gleichungen mit drei Unbekannten fragen nach einem einzigen Vektor. Beides gehört zusammen. Die Frage lautet: *Warum genügt eine Tabelle aus Zahlen, um eine Abbildung festzulegen, und wie findet man den Vektor, der auf ein gegebenes Ziel abgebildet wird?*

Die Antwort führt über acht Begriffe. Eine __lineare Abbildung__ schickt Summen auf Summen und Vielfache auf Vielfache. Eine __Matrix__ ist ein rechteckiges Zahlenschema, das eine solche Abbildung festhält. Der __Kern__ enthält alle Vektoren, die auf null gehen, das __Bild__ alle Vektoren, die getroffen werden. Der __Rang__ ist die Dimension des Bilds. Das __Matrizenprodukt__ ist das Hintereinanderausführen zweier Abbildungen in Zahlen. Ein __lineares Gleichungssystem__ sucht zu einer Matrix $A$ und einem Vektor $b$ alle $x$ mit $Ax=b$, und der __Gauß-Algorithmus__ löst es durch Abziehen von Zeilen.



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Drehung und Scherung:** $D=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ dreht die Ebene um $90^\circ$ gegen den Uhrzeigersinn, $S=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ schiebt sie waagerecht, und zwar umso weiter, je höher der Punkt liegt (__Scherung__).

</li>

<li>

⁠**Presse:** $P=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ drückt die Ebene auf eine Gerade.

</li>

<li>

⁠**Flache Matrix:** $Q=\bigl(\begin{smallmatrix}1&2&1\\2&4&3\\3&6&4\end{smallmatrix}\bigr)$ hat drei Spalten, aber nur zwei unabhängige Richtungen.

</li>

<li>

⁠**Volle Matrix:** $H=\bigl(\begin{smallmatrix}2&1&1\\4&3&3\\2&3&4\end{smallmatrix}\bigr)$. Das System $Hx=(3,7,4)$ hat genau die Lösung $x=(1,2,-1)$.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap10.py` nach.
:::
