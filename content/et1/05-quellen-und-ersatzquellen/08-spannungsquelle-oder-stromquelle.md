---
title: Stufe 6: Spannungsquelle oder Stromquelle
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
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
Nein. Rechts in Abb. [7](#abb-7) fließen im Leerlauf 4,5 A durch 2 $\Omega$, das wären mit $P=UI$ ([Kapitel 7](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)) 40,5 W. Die echte Batterie bleibt kalt, das Spannungsquellenbild mit 0 W trifft hier zu. Ersatzschaltbilder stimmen an den Klemmen, nicht im Inneren. Was innen geschieht, hängt vom Aufbau ab, nicht von der Kennlinie. Am Arbeitspunkt ist es ebenso: 0,5 W gegen 32 W innen, außen beide Male 4 W.
:::

:::aufgabe Aufgabe 7 ★ Umwandeln
<span class="anker" id="aufg-7"></span>

(a) Wandle 5 V mit 100 $\Omega$ in eine Stromquelle um. (b) Wandle 20 mA mit 1 k$\Omega$ parallel in eine Spannungsquelle um. (c) Schließe an beide Formen aus (a) 400 $\Omega$ an und vergleiche Spannung und Strom.

:::loesung
(a) $I_\mathrm{q}=5\,\mathrm{V}/100\,\Omega=50$ mA, $G_\mathrm{q}=10$ mS. (b) $U_\mathrm{q}=20\,\mathrm{mA}\cdot1\,\mathrm{k\Omega}=20$ V, $R_\mathrm{q}=1$ k$\Omega$.

(c) Spannungsquelle: Spannungsteiler, $U=5\,\mathrm{V}\cdot\frac{400}{500}=4$ V, $I=10$ mA. Stromquelle: $50\,\mathrm{mA}\cdot(100\,\Omega\parallel400\,\Omega)=50\,\mathrm{mA}\cdot80\,\Omega=4$ V, $I=4\,\mathrm{V}/400\,\Omega=10$ mA. Gleich.
:::
:::

::::formelsammlung
**Äquivalenz realer Quellen**

$$U_\mathrm{q}=\frac{I_\mathrm{q}}{G_\mathrm{q}}\qquad\text{und}\qquad R_\mathrm{q}=\frac{1}{G_\mathrm{q}}$$

Reale Spannungsquelle ($U_\mathrm{q}$, $R_\mathrm{q}$) und reale Stromquelle ($I_\mathrm{q}$, $G_\mathrm{q}$) haben dann dieselbe Kennlinie und sind durch keine Messung an den Klemmen zu unterscheiden. Folgt aus dem Gleichsetzen beider Geraden für jeden Strom. Gilt nur an den Klemmen und nur für $0<R_\mathrm{q}<\infty$; über Leistungen im Inneren sagt sie nichts.

**Quellenstrom aus der Spannungsquelle**

$$I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{q}$$

Der Quellenstrom ist der Kurzschlussstrom, der Widerstand bleibt derselbe. Ist $R_\mathrm{q}$ klein gegen die Last, wählt man die Spannungsquellenform, ist er groß, die Stromquellenform.
::::

::::lernkarten
:::karte begriff äquivalent
Wann heißen zwei Netzwerke äquivalent, und was folgt daraus für Messungen an ihren Klemmen?
---
Wenn sie gleiche Kennlinien haben. Dann lässt sich durch keine Messung an den Klemmen feststellen, welches von beiden angeschlossen ist.
--- falsch
Wenn sie aus denselben Bauteilen bestehen, nur anders angeordnet. An den Klemmen können sie sich trotzdem deutlich voneinander unterscheiden.
--- falsch
Wenn sie bei einer bestimmten Last denselben Strom liefern. Bei anderen Lasten darf eine Messung sie unterscheiden.
--- falsch
Wenn sie gleiche Kennlinien haben und innen dieselbe Leistung umsetzen. Erst beides zusammen macht sie austauschbar.
:::
:::karte formel Äquivalenz realer Quellen
Unter welchen Bedingungen sind eine reale Spannungsquelle mit $U_\mathrm{q}$, $R_\mathrm{q}$ und eine reale Stromquelle mit $I_\mathrm{q}$, $G_\mathrm{q}$ äquivalent?
---
$U_\mathrm{q}=\frac{I_\mathrm{q}}{G_\mathrm{q}}$ und $R_\mathrm{q}=\frac{1}{G_\mathrm{q}}$. Der Quellenstrom ist der Kurzschlussstrom $I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{q}$, der Widerstand bleibt derselbe. Das gilt nur an den Klemmen und für $0<R_\mathrm{q}<\infty$.
--- falsch
$U_\mathrm{q}=I_\mathrm{q}\,G_\mathrm{q}$ und $R_\mathrm{q}=G_\mathrm{q}$. Spannung und Strom rechnet man über den Leitwert um, der Zahlenwert des Innenwiderstands bleibt gleich. Das gilt für jede Last und auch im Inneren der Quelle.
--- falsch
$U_\mathrm{q}=\frac{I_\mathrm{q}}{G_\mathrm{q}}$ und $R_\mathrm{q}=\frac{1}{G_\mathrm{q}}$. Das gilt für jede Quelle, auch für ideale mit $R_\mathrm{q}=0$ oder $R_\mathrm{q}\to\infty$, und auch für die Leistung im Inneren.
--- falsch
$I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{q}$ ist der Strom im Leerlauf, und der Leitwert ist $G_\mathrm{q}=R_\mathrm{q}$. Die Umwandlung gilt nur, wenn die Last gerade gleich $R_\mathrm{q}$ ist.
:::
:::karte herleitung Gleichsetzen der Geraden
Leite aus den Gleichungen der realen Spannungsquelle und der realen Stromquelle die Bedingungen für ihre Äquivalenz her.
---
Man stellt die Stromquellen-Gleichung $I_\mathrm{A}=I_\mathrm{q}-G_\mathrm{q}\,U_\mathrm{AB}$ nach der Spannung um, $U_\mathrm{AB}=(I_\mathrm{q}-I_\mathrm{A})/G_\mathrm{q}$, weil man sie mit der Spannungsquellen-Gleichung vergleichen will.
---
Gleichsetzen mit $U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}\,I_\mathrm{A}$ ergibt $\frac{I_\mathrm{q}}{G_\mathrm{q}}-\frac{I_\mathrm{A}}{G_\mathrm{q}}=U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}$, weil beide Quellen an den Klemmen dieselbe Spannung haben sollen.
---
Diese Gleichung muss für jeden Strom gelten, weil äquivalente Netzwerke dieselbe Kennlinie haben, nicht nur einen gemeinsamen Punkt.
---
Deshalb müssen die Glieder ohne $I_\mathrm{A}$ und die Glieder mit $I_\mathrm{A}$ einzeln gleich sein; das ergibt $U_\mathrm{q}=\frac{I_\mathrm{q}}{G_\mathrm{q}}$ und $R_\mathrm{q}=\frac{1}{G_\mathrm{q}}$, weil die Gleichung sonst bei einem anderen Strom nicht mehr stimmte.
:::
:::karte zusammenhang Stromteilung in der Stromquellenform
Warum sinkt auch in der Stromquellenform die Klemmenspannung, wenn die Last Strom zieht?
---
Im Leerlauf fließt der ganze Quellenstrom durch $G_\mathrm{q}$ und erzeugt dort die Leerlaufspannung. Zieht die Last Strom, bleibt für $G_\mathrm{q}$ weniger, und die Spannung sinkt: Stromteilung statt Spannungsteilung.
--- falsch
Weil die ideale Stromquelle bei Belastung weniger Strom liefert: Ihr Quellenstrom sinkt mit dem Laststrom, und die Spannung an den Klemmen folgt ihm im selben Verhältnis, bis im Kurzschluss nichts mehr übrig ist.
--- falsch
Sie sinkt gar nicht: In der Stromquellenform bleibt die Klemmenspannung bei jeder Last gleich, nur in der Spannungsquellenform fällt sie mit dem Strom ab.
--- falsch
Weil der Leitwert $G_\mathrm{q}$ mit dem Laststrom wächst: Ein größerer Leitwert bei gleichem Quellenstrom ergibt eine kleinere Spannung an den Klemmen, so wie ein dickerer Draht weniger Spannung trägt.
:::
:::karte formel Batterie als Stromquelle
Welche Stromquellenform hat die Batterie mit 9 V und 2 $\Omega$, und wie teilt sich ihr Quellenstrom am Arbeitspunkt mit 8 V auf?
---
$I_\mathrm{q}=4{,}5$ A und $G_\mathrm{q}=0{,}5$ S. Am Arbeitspunkt nimmt der Leitwert $0{,}5\,\mathrm{S}\cdot8\,\mathrm{V}=4$ A auf, für die Last bleiben 0,5 A.
--- falsch
$I_\mathrm{q}=4{,}5$ A und $G_\mathrm{q}=2$ S. Am Arbeitspunkt nimmt der Leitwert 16 A auf, mehr als der Quellenstrom, also fließt Strom in die Quelle zurück.
--- falsch
$I_\mathrm{q}=0{,}5$ A und $G_\mathrm{q}=0{,}5$ S. Der ganze Quellenstrom geht an die Last, weil der Leitwert am Arbeitspunkt keinen Strom aufnimmt.
--- falsch
$I_\mathrm{q}=18$ A und $G_\mathrm{q}=0{,}5$ S. Am Arbeitspunkt nimmt der Leitwert $0{,}5\,\mathrm{S}\cdot8\,\mathrm{V}=4$ A auf, für die Last bleiben 14 A.
:::
:::karte zusammenhang Welche Form man wählt
Wann wählt man für eine reale Quelle die Spannungsquellenform und wann die Stromquellenform?
---
Rechnerisch sind beide gleich gut. Ist $R_\mathrm{q}$ klein gegen die Last, ändert sich die Spannung kaum, und man nimmt die Spannungsquellenform. Ist $R_\mathrm{q}$ groß gegen die Last, ändert sich der Strom kaum: Stromquellenform.
--- falsch
Ist $R_\mathrm{q}$ klein gegen die Last, wählt man die Stromquellenform, weil dann der Strom kaum von der Last abhängt. Ist $R_\mathrm{q}$ groß gegen die Last, wählt man die Spannungsquellenform, weil dann die Spannung fest bleibt.
--- falsch
Man wählt immer die Spannungsquellenform, weil nur sie die Verluste im Inneren der Quelle richtig wiedergibt. Die Stromquellenform ist eine reine Rechenhilfe für Parallelschaltungen.
--- falsch
Das hängt von der Bauart ab: Batterien sind stets Spannungsquellen, Netzteile stets Stromquellen. Die jeweils andere Form wäre für sie falsch und liefert an den Klemmen andere Werte.
:::
:::karte zusammenhang Ideale Quellen umwandeln
Warum hat eine ideale Spannungsquelle keine Stromquellenform und eine ideale Stromquelle keine Spannungsquellenform?
---
Für $R_\mathrm{q}\to0$ geht $I_\mathrm{q}\to\infty$: Die ideale Spannungsquelle bräuchte einen unendlichen Quellenstrom. Ebenso bräuchte die ideale Stromquelle, deren Leitwert null ist, eine unendliche Quellenspannung. Die Äquivalenz gilt nur für $0<R_\mathrm{q}<\infty$.
--- falsch
Weil ideale Quellen keinen Innenwiderstand haben und man deshalb nichts umwandeln muss: Bei ihnen sind beide Formen von selbst gleich, man darf jede nach Belieben verwenden und erhält an den Klemmen stets dieselben Werte.
--- falsch
Sie haben eine: Die ideale Spannungsquelle wird zu einer idealen Stromquelle mit dem Strom, den die Last zieht, $I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{L}$, und behält dabei ihren Innenwiderstand null; umgekehrt gilt dasselbe für die ideale Stromquelle.
--- falsch
Weil die Umwandlung nur für Quellen mit einem Innenwiderstand über 1 $\Omega$ gilt. Darunter würde der Quellenstrom zu groß, um ihn mit üblichen Geräten noch zu messen.
:::
:::karte zusammenhang Leistung im Inneren
Verheizt eine Batterie mit 9 V und 2 $\Omega$ im Leerlauf 40,5 W, weil in ihrer Stromquellenform 4,5 A durch 2 $\Omega$ fließen?
---
Nein. Die echte Batterie bleibt kalt, hier trifft das Spannungsquellenbild mit 0 W zu. Ersatzschaltbilder stimmen nur an den Klemmen; was innen geschieht, hängt vom Aufbau ab, nicht von der Kennlinie.
--- falsch
Ja, die 40,5 W entstehen wirklich. Deshalb entladen sich Batterien auch ohne Last und werden dabei warm, wegen ihrer großen Masse aber so langsam, dass man es von außen kaum bemerkt, außer an der sinkenden Ladung.
--- falsch
Nein, weil ein Strom durch einen Leitwert grundsätzlich keine Wärme erzeugt. Wärme entsteht nur in Widerständen, und die Stromquellenform enthält keinen.
--- falsch
Ja, solange man die Stromquellenform benutzt. In der Spannungsquellenform sind es 0 W; welche Form stimmt, hängt davon ab, wie man rechnet, im Mittel sind es etwa 20 W.
:::
::::
