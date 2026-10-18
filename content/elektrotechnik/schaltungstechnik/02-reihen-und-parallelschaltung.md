---
title: Reihen- und Parallelschaltung
fach: Elektrotechnik
thema: Schaltungstechnik
order: 2
summary: Wie sich Widerstände addieren — je nachdem, ob der Strom hintereinander oder nebeneinander fließt.
tags: Reihenschaltung, Parallelschaltung, Ersatzwiderstand
---

:::konzept
Zwei Wege, Widerstände zu verbinden: **hintereinander** (Reihe) oder **nebeneinander** (parallel).
In Reihe muss der Strom durch *alle* Widerstände nacheinander — es wird „enger", der Gesamtwiderstand
*steigt*. Parallel bekommt der Strom *mehrere* Wege gleichzeitig — es wird „breiter", der Gesamtwiderstand
*sinkt*.
:::

## Reihenschaltung

Der gleiche Strom fließt durch alle Widerstände; die Spannungen addieren sich. Der Ersatzwiderstand ist
einfach die Summe:

$$R_\text{ges} = R_1 + R_2 + \dots + R_n$$

## Parallelschaltung

An allen Widerständen liegt dieselbe Spannung; die Ströme addieren sich. Hier addieren sich die
**Kehrwerte**:

$$\frac{1}{R_\text{ges}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots + \frac{1}{R_n}$$

Bei zwei Widerständen ergibt das die handliche Form

$$R_\text{ges} = \frac{R_1 \cdot R_2}{R_1 + R_2}.$$

:::merke
Parallel ist der Gesamtwiderstand immer **kleiner** als der kleinste Einzelwiderstand — mehr Wege lassen
mehr Strom durch.
:::

*(Beispiel-Artikel zum Testen der Wissens-Struktur.)*
