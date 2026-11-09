---
title: Stufe 6: Spannungsquelle oder Stromquelle
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Quellen und Ersatzquellen
order: 1150800
summary: Für dieselbe reale Quelle gibt es zwei Schaltbilder.
tags: äquivalent
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Für dieselbe reale Quelle gibt es zwei Schaltbilder. Diese Stufe zeigt, dass beide dieselbe Gerade beschreiben, und wie man sie ineinander umrechnet.
:::

**Die Idee.** Eine Gerade lässt sich von der Spannungsachse her lesen (Höhe $U_\mathrm{q}$, Neigung $R_\mathrm{q}$) oder von der Stromachse her (Abschnitt $I_\mathrm{q}$, Neigung $G_\mathrm{q}$). Zwei Netzwerke heißen __äquivalent__, wenn sie gleiche Kennlinien haben. Von außen lässt sich dann durch keine Messung an den Klemmen feststellen, welches von beiden angeschlossen ist.

:::satz Satz 6.1 (Äquivalenz realer Quellen)
<span class="anker" id="satz-6-1"></span>

Eine reale Spannungsquelle und eine reale Stromquelle sind äquivalent, wenn gilt

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{q}=\frac{I_\mathrm{q}}{G_\mathrm{q}}\qquad\text{und}\qquad R_\mathrm{q}=\frac{1}{G_\mathrm{q}}. \tag{6.1}$$
:::

:::herleitung Gleichsetzen der Geraden
Man stellt die Stromquellen-Gleichung aus [(5.1)](reale-quellen-und-der-arbeitspunkt.html#gl-5-1) nach der Spannung um, $U_\mathrm{AB}=(I_\mathrm{q}-I_\mathrm{A})/G_\mathrm{q}$, und setzt sie der Spannungsquellen-Gleichung gleich:

$$\frac{I_\mathrm{q}}{G_\mathrm{q}}-\frac{I_\mathrm{A}}{G_\mathrm{q}}=U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}.$$

Das muss für jeden Strom gelten. Die Glieder ohne $I_\mathrm{A}$ und die Glieder mit $I_\mathrm{A}$ müssen also einzeln gleich sein. Das ist [(6.1)](#gl-6-1).
:::

⁠**So liest man das:** Der Strom $I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{q}$ ist der Kurzschlussstrom, der Widerstand bleibt derselbe. In der Stromquellenform läuft im Leerlauf der ganze Quellenstrom durch $G_\mathrm{q}$ und erzeugt dort die Leerlaufspannung. Zieht die Last Strom, bleibt für $G_\mathrm{q}$ weniger, die Spannung sinkt. Das ist derselbe Abfall, nur als Stromteilung statt als Spannungsteilung. **Gültigkeit:** Die Äquivalenz gilt nur an den Klemmen und nur für $0<R_\mathrm{q}<\infty$.

:::abbildung et1/k5umwandlung 7
Dieselbe Batterie am selben Arbeitspunkt. Links fließen 0,5 A durch alles. Rechts teilt sich der Quellenstrom von 4,5 A in 4 A durch den Leitwert und 0,5 A zur Last. An den Klemmen stimmen Spannung und Strom überein.
:::

::::beispiel
Die Batterie mit 9 V und 2 $\Omega$ wird zu $I_\mathrm{q}=4{,}5$ A und $G_\mathrm{q}=0{,}5$ S. Am Arbeitspunkt mit 8 V nimmt der Leitwert $0{,}5\,\mathrm{S}\cdot8\,\mathrm{V}=4$ A auf, für die Last bleiben 0,5 A (Abb. [7](#abb-7)).
::::

⁠**Grenzfall:** Für $R_\mathrm{q}\to0$ geht $I_\mathrm{q}\to\infty$. Eine ideale Spannungsquelle hat keine Stromquellenform, eine ideale Stromquelle keine Spannungsquellenform.

**Welche Form wählt man?** Rechnerisch sind beide gleich gut. Man nimmt die Form, die das Verhalten besser zeigt: Spannungsquellen sind niederohmig (ideal null), Stromquellen sind hochohmig (ideal unendlich). Ist $R_\mathrm{q}$ klein gegen die Last, ändert sich die Spannung kaum, und man wählt die Spannungsquellenform. Ist $R_\mathrm{q}$ groß gegen die Last, ändert sich der Strom kaum, und man wählt die Stromquellenform.

:::frage Wenn beide gleich sind, verheizt die Batterie dann im Leerlauf 40,5 W?
Nein. Rechts in Abb. [7](#abb-7) fließen im Leerlauf 4,5 A durch 2 $\Omega$, das wären mit $P=UI$ ([Teil 7](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)) 40,5 W. Die echte Batterie bleibt kalt, das Spannungsquellenbild mit 0 W trifft hier zu. Ersatzschaltbilder stimmen an den Klemmen, nicht im Inneren. Was innen geschieht, hängt vom Aufbau ab, nicht von der Kennlinie. Am Arbeitspunkt ist es ebenso: 0,5 W gegen 32 W innen, außen beide Male 4 W.
:::

:::aufgabe Aufgabe 7 ★ Umwandeln
<span class="anker" id="aufg-7"></span>

(a) Wandle 5 V mit 100 $\Omega$ in eine Stromquelle um. (b) Wandle 20 mA mit 1 k$\Omega$ parallel in eine Spannungsquelle um. (c) Schließe an beide Formen aus (a) 400 $\Omega$ an und vergleiche Spannung und Strom.

:::loesung
(a) $I_\mathrm{q}=5\,\mathrm{V}/100\,\Omega=50$ mA, $G_\mathrm{q}=10$ mS. (b) $U_\mathrm{q}=20\,\mathrm{mA}\cdot1\,\mathrm{k\Omega}=20$ V, $R_\mathrm{q}=1$ k$\Omega$.

(c) Spannungsquelle: Spannungsteiler, $U=5\,\mathrm{V}\cdot\frac{400}{500}=4$ V, $I=10$ mA. Stromquelle: $50\,\mathrm{mA}\cdot(100\,\Omega\parallel400\,\Omega)=50\,\mathrm{mA}\cdot80\,\Omega=4$ V, $I=4\,\mathrm{V}/400\,\Omega=10$ mA. Gleich.
:::
:::
