---
title: Die Ableitung — anschaulich
fach: Mathematik
thema: Analysis
order: 1
summary: Was eine Ableitung wirklich misst: die momentane Steigung — als Grenzwert immer kleinerer Steigungsdreiecke.
tags: Ableitung, Steigung, Differentialquotient, Grenzwert
---

:::konzept
Die Ableitung einer Funktion an einer Stelle ist ihre **Steigung** genau dort — wie steil die Kurve in
diesem Moment bergauf oder bergab geht. Technisch: Man legt eine Gerade an zwei immer näher
zusammenrückende Punkte und schaut, gegen welche Steigung das strebt.
:::

## Vom Steigungsdreieck zur Tangente

Die Steigung zwischen zwei Punkten $x$ und $x+h$ ist der **Differenzenquotient**

$$\frac{f(x+h) - f(x)}{h}.$$

Lässt man den Abstand $h$ gegen null gehen, rücken die Punkte zusammen und die Sekante wird zur Tangente.
Dieser Grenzwert ist die Ableitung:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}.$$

:::kern
Ableitung = **momentane Steigung** = Grenzwert des Steigungsdreiecks, wenn seine Breite gegen null geht.
:::

*(Beispiel-Artikel zum Testen der Wissens-Struktur.)*
