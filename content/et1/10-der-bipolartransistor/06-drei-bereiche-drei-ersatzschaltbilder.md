---
title: Stufe 4: Drei Bereiche, drei Ersatzschaltbilder
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
order: 1200600
summary: Mit e-Funktionen lassen sich Schaltungen von Hand kaum lösen.
tags: Sperrbereich, Sättigungsbereich, Schwellspannung, Sättigungsspannung, Ersatzschaltbild
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Mit e-Funktionen lassen sich Schaltungen von Hand kaum lösen. Diese Stufe ersetzt die Fläche durch drei lineare Stücke.
:::

**Die Idee.** Jede der beiden Dioden kann leiten oder sperren. Daraus ergeben sich die Betriebszustände. Sperrt die BE-Diode, startet kein Elektron, und nichts fließt. Das ist der __Sperrbereich__. Leitet sie und sperrt die CB-Diode, holt der Kollektor alle Elektronen ab, und es gilt $I_\mathrm{C}=B\,I_\mathrm{B}$. Das ist der aktive Bereich. Fällt $U_\mathrm{CE}$ so weit, dass auch die CB-Diode deutlich leitet, schickt der Kollektor Elektronen zurück. Dann kann er nicht mehr alle abholen, die Basis läuft mit Elektronen voll, und $I_\mathrm{C}$ bleibt unter $B\,I_\mathrm{B}$. Das ist der __Sättigungsbereich__. Wie bei der Diode ([Kapitel 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) ersetzt man die Kurven durch Geraden: Die Eingangskennlinie bekommt einen Knick bei 0,6 V, die Stromsteuerkennlinie wird eine Gerade mit Steigung $B$, die in der Sättigung waagerecht abknickt, die Ausgangskennlinien werden rechts von 0,2 V waagerecht (Abb. [6](der-arbeitspunkt.html#abb-6)).

:::definition Definition 4.1 (Arbeitsbereiche des npn-Transistors)
<span class="anker" id="satz-4-1"></span>

Mit der __Schwellspannung__ $U_\mathrm{BE,ein}=0{,}6$ V und der __Sättigungsspannung__ $U_\mathrm{CE,sat}=0{,}2$ V gilt:

<span class="anker" id="gl-4-1"></span>
<span class="anker" id="gl-4-2"></span>
<span class="anker" id="gl-4-3"></span>
$$\begin{aligned} \text{Sperrbereich:}\quad & U_\mathrm{BE}<U_\mathrm{BE,ein}\;\Rightarrow\; I_\mathrm{B}=I_\mathrm{C}=0,\\ \text{aktiver Bereich:}\quad & U_\mathrm{BE}=U_\mathrm{BE,ein},\ I_\mathrm{B}>0,\quad I_\mathrm{C}=B\,I_\mathrm{B},\quad U_\mathrm{CE}\ge U_\mathrm{CE,sat},\\ \text{Sättigungsbereich:}\quad & U_\mathrm{BE}=U_\mathrm{BE,ein},\ I_\mathrm{B}>0,\quad U_\mathrm{CE}=U_\mathrm{CE,sat},\quad I_\mathrm{C}\le B\,I_\mathrm{B}. \end{aligned} \tag{4.1|4.2|4.3}$$
:::

⁠**So liest man das:** Jeder Bereich hat ein lineares __Ersatzschaltbild__ aus idealen Elementen, das zwischen B, C und E gilt (Abb. [5](#abb-5)). Im Sperrbereich sind alle Klemmen offen. In den beiden leitenden Bereichen liegt zwischen B und E eine Spannungsquelle mit 0,6 V, im aktiven Bereich zwischen C und E eine gesteuerte Stromquelle, in der Sättigung eine Spannungsquelle mit 0,2 V. Im gemeinsamen Knoten gilt immer $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$. **Gültigkeit:** eine grobe, aber bewährte Näherung. Die Schwelle ist kein echter Schalter (Stufe [2](warum-strom-durch-die-gesperrte-diode-fliet.html#stufe-2)), die 0,6 V treffen T bei 2 mA, bei 20 mA wären es 0,66 V. Der Wert 0,2 V hängt vom Typ ab.

:::abbildung et1/k10esb 5
Die drei Ersatzschaltbilder des npn-Transistors. Links offen im Sperrbereich, Mitte mit gesteuerter Stromquelle im aktiven Bereich, rechts mit zwei Spannungsquellen in der Sättigung. Im Knoten über E vereinigen sich $I_\mathrm{B}$ und $I_\mathrm{C}$.
:::

::::beispiel
Bei T ($B=200$) gilt: $I_\mathrm{B}=10$ µ A mit $U_\mathrm{CE}=6$ V ist aktiv, also $I_\mathrm{C}=2$ mA. $I_\mathrm{B}=30$ µ A mit $I_\mathrm{C}=3{,}9$ mA ist Sättigung, denn $B\,I_\mathrm{B}=6$ mA ist größer als der Strom, den der Kreis zulässt. $U_\mathrm{BE}=0{,}3$ V ist Sperrbereich.
::::

⁠**Grenzfall:** Für $B\,I_\mathrm{B}=I_\mathrm{C}$ und $U_\mathrm{CE}=U_\mathrm{CE,sat}$ liegt der Transistor genau auf der Grenze zwischen aktiv und Sättigung. Beide Ersatzschaltbilder liefern dort dasselbe.

:::frage Warum heißt es Sättigung, wenn der Strom gerade nicht mehr folgt?
Gesättigt ist nicht der Strom, sondern die Basis: Sie ist mit Elektronen übervoll. Das Wort bedeutet beim Bipolartransistor deshalb den steilen Teil links der Ausgangskennlinie. Beim MOSFET heißt der flache Teil Sättigung. Die beiden Wörter meinen Verschiedenes.
:::

**Der pnp-Transistor.** Beim pnp-Transistor sind n und p vertauscht (Abb. [1](drei-schichten-zwei-spannungen.html#abb-1)). Die Mechanismen bleiben gleich, nur übernehmen Löcher die Rolle der Elektronen. Der Emitter liegt am höchsten Potenzial, und alle Vorzeichen drehen sich um. Mit den npn-Bezeichnungen sind jetzt $U_\mathrm{BE,ein}=-0{,}6$ V und $U_\mathrm{CE,sat}=-0{,}2$ V negativ. Zählt man $I_\mathrm{B}$ und $I_\mathrm{C}$ aus dem Bauteil heraus, sind beide positiv, und es gilt:

<span class="anker" id="gl-4-4"></span>
$$\begin{aligned} &\text{Sperrbereich: } U_\mathrm{BE}>-0{,}6\,\mathrm{V};\qquad \text{aktiv: } I_\mathrm{C}=B\,I_\mathrm{B},\ U_\mathrm{CE}\le-0{,}2\,\mathrm{V};\\ &\text{Sättigung: } U_\mathrm{CE}=-0{,}2\,\mathrm{V},\ I_\mathrm{C}\le B\,I_\mathrm{B}. \end{aligned} \tag{4.4}$$

In der Praxis ist der npn-Transistor häufiger, weil Elektronen in Silizium rund dreimal beweglicher sind als Löcher. Die pnp-Form dient vor allem dort, wo der Emitter an der positiven Versorgung liegen soll.

:::aufgabe Aufgabe 4 ★ Bereich erkennen
<span class="anker" id="aufg-4"></span>

Bestimme den Bereich von T und den fehlenden Strom oder die fehlende Spannung. (a) $I_\mathrm{B}=20$ µ A, $U_\mathrm{CE}=5$ V. (b) $I_\mathrm{B}=40$ µ A, $I_\mathrm{C}=3$ mA. (c) $U_\mathrm{BE}=-1$ V, $U_\mathrm{CE}=12$ V. (d) Ein pnp-Transistor mit $B=200$: $U_\mathrm{CE}=-5$ V und $I_\mathrm{B}=10$ µ A.

:::loesung
(a) $I_\mathrm{B}>0$ und $U_\mathrm{CE}>0{,}2$ V: aktiv, $I_\mathrm{C}=4$ mA. (b) $B\,I_\mathrm{B}=8$ mA $>3$ mA: Sättigung, $U_\mathrm{CE}=0{,}2$ V. (c) $U_\mathrm{BE}<0{,}6$ V: Sperrbereich, $I_\mathrm{B}=I_\mathrm{C}=0$. (d) $U_\mathrm{CE}\le-0{,}2$ V und $I_\mathrm{B}>0$: aktiv, $I_\mathrm{C}=2$ mA, $U_\mathrm{BE}=-0{,}6$ V.
:::
:::
