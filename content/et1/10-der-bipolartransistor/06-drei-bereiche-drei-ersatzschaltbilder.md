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

::::formelsammlung
**Sperrbereich**

$$U_\mathrm{BE}<U_\mathrm{BE,ein}\;\Rightarrow\;I_\mathrm{B}=I_\mathrm{C}=0$$

Mit der Schwellspannung $U_\mathrm{BE,ein}=0{,}6$ V. Ersatzschaltbild: alle Klemmen offen.

**Aktiver Bereich**

$$U_\mathrm{BE}=U_\mathrm{BE,ein},\ I_\mathrm{B}>0,\quad I_\mathrm{C}=B\,I_\mathrm{B},\quad U_\mathrm{CE}\ge U_\mathrm{CE,sat}$$

Ersatzschaltbild: Spannungsquelle mit 0,6 V zwischen B und E, gesteuerte Stromquelle zwischen C und E.

**Sättigungsbereich**

$$U_\mathrm{BE}=U_\mathrm{BE,ein},\ I_\mathrm{B}>0,\quad U_\mathrm{CE}=U_\mathrm{CE,sat},\quad I_\mathrm{C}\le B\,I_\mathrm{B}$$

Mit der Sättigungsspannung $U_\mathrm{CE,sat}=0{,}2$ V, je nach Typ. Ersatzschaltbild: 0,6 V zwischen B und E, 0,2 V zwischen C und E. In allen Bereichen gilt $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$. Grobe Näherung: Die 0,6 V treffen T bei 2 mA, bei 20 mA wären es 0,66 V.

**Arbeitsbereiche des pnp-Transistors**

$$\begin{aligned} &\text{Sperrbereich: } U_\mathrm{BE}>-0{,}6\,\mathrm{V};\qquad \text{aktiv: } I_\mathrm{C}=B\,I_\mathrm{B},\ U_\mathrm{CE}\le-0{,}2\,\mathrm{V};\\ &\text{Sättigung: } U_\mathrm{CE}=-0{,}2\,\mathrm{V},\ I_\mathrm{C}\le B\,I_\mathrm{B} \end{aligned}$$

Mit den npn-Bezeichnungen und $I_\mathrm{B}$, $I_\mathrm{C}$ aus dem Bauteil heraus gezählt, beide positiv. $U_\mathrm{BE,ein}=-0{,}6$ V und $U_\mathrm{CE,sat}=-0{,}2$ V; der Emitter liegt am höchsten Potenzial.
::::

::::lernkarten
:::karte begriff Sperrbereich
Wann arbeitet ein npn-Transistor im Sperrbereich, und welche Ströme fließen dann?
---
Der Betriebszustand, in dem die BE-Diode sperrt, im linearen Modell für $U_\mathrm{BE}<U_\mathrm{BE,ein}$. Kein Elektron startet, es gilt $I_\mathrm{B}=I_\mathrm{C}=0$, alle Klemmen sind offen.
--- falsch
Der Betriebszustand, in dem die CB-Diode sperrt, also jedes positive $U_\mathrm{CB}$. Dann fließt nur der Basisstrom, und der Kollektor ist offen, weil kein Elektron ihn erreicht.
--- falsch
Der Betriebszustand, in dem $U_\mathrm{CE}$ unter $U_\mathrm{CE,sat}$ sinkt. Der Kollektor sperrt die Elektronen aus, $I_\mathrm{C}=0$, während der Basisstrom weiter über den Emitter fließt.
--- falsch
Der Betriebszustand, in dem die BE-Diode sperrt, im linearen Modell für $U_\mathrm{BE}<U_\mathrm{BE,ein}$. Der Kollektorstrom fließt ungehindert weiter, nur der Basisstrom ist null.
:::
:::karte begriff Sättigungsbereich
Was kennzeichnet den Sättigungsbereich eines npn-Transistors, und welche Gleichungen gelten dort im linearen Modell?
---
Der Betriebszustand, in dem auch die CB-Diode deutlich leitet: Der Kollektor schickt Elektronen zurück, die Basis läuft voll. Im Modell gilt $U_\mathrm{CE}=U_\mathrm{CE,sat}$ und $I_\mathrm{C}\le B\,I_\mathrm{B}$.
--- falsch
Der Betriebszustand, in dem die BE-Diode sperrt, die CB-Diode leitet und der Kollektorstrom seinen Höchstwert erreicht. Im Modell gilt $U_\mathrm{CE}=U_\mathrm{CE,sat}$ und $I_\mathrm{C}=B\,I_\mathrm{B}$.
--- falsch
Der Betriebszustand, in dem der Kollektorstrom nicht weiter steigen kann, aber noch $B\,I_\mathrm{B}$ folgt. Im Modell gilt $U_\mathrm{CE}\ge U_\mathrm{CE,sat}$ und $I_\mathrm{C}\ge B\,I_\mathrm{B}$.
--- falsch
Der Betriebszustand, in dem die CB-Diode besonders stark sperrt und der Kollektor mehr Elektronen abholt, als der Emitter liefert. Im Modell gilt $U_\mathrm{CE}=U_\mathrm{CC}$ und $I_\mathrm{C}>B\,I_\mathrm{B}$.
:::
:::karte begriff Schwellspannung
Welche Rolle spielt die Schwellspannung $U_\mathrm{BE,ein}$ im linearen Modell des Transistors, und wie genau ist ihr Wert?
---
Die Spannung, bei der das lineare Modell die Eingangskennlinie abknickt: Darunter sperrt der Transistor, leitend gilt $U_\mathrm{BE}=U_\mathrm{BE,ein}=0{,}6$ V. Das trifft T bei 2 mA, bei 20 mA wären es 0,66 V.
--- falsch
Die größte Spannung, die zwischen Basis und Emitter liegen darf, ohne dass die BE-Grenze durchschlägt. Für T sind es genau 0,6 V, unabhängig vom Strom und von der Temperatur.
--- falsch
Die Spannung, ab der die CB-Diode leitet, also die Grenze zur Sättigung. Für T sind es 0,2 V; bei größeren Strömen sinkt der Wert auf rund 0,1 V.
--- falsch
Die Spannung des Knicks bei 0,6 V, der die Eingangskennlinie ersetzt. Ein echter Transistor schaltet dort wie ein Schalter: Darunter fließt exakt kein Strom, darüber jeder beliebige.
:::
:::karte begriff Sättigungsspannung
Was gibt die Sättigungsspannung $U_\mathrm{CE,sat}$ im linearen Modell an?
---
Die Kollektor-Emitter-Spannung eines ganz durchgeschalteten Transistors, hier $U_\mathrm{CE,sat}=0{,}2$ V. Der genaue Wert hängt vom Typ ab.
--- falsch
Die Basis-Emitter-Spannung, ab der der Transistor leitet, hier 0,2 V. Darunter sperrt er, darüber gilt $I_\mathrm{C}=B\,I_\mathrm{B}$.
--- falsch
Die größte Kollektor-Emitter-Spannung, die der Transistor aushält, hier 0,2 V über $U_\mathrm{CC}$. Darüber schlägt die CB-Grenze durch.
--- falsch
Die Spannung am Kollektorwiderstand eines ganz durchgeschalteten Transistors, hier 0,2 V. Der Rest von $U_\mathrm{CC}$ liegt am Transistor.
:::
:::karte formel Arbeitsbereiche
Welche Bedingungen gelten im linearen Modell im Sperrbereich, im aktiven Bereich und im Sättigungsbereich?
---
Sperrbereich: $U_\mathrm{BE}<U_\mathrm{BE,ein}$, $I_\mathrm{B}=I_\mathrm{C}=0$. Aktiv: $I_\mathrm{B}>0$, $I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}\ge U_\mathrm{CE,sat}$. Sättigung: $I_\mathrm{B}>0$, $U_\mathrm{CE}=U_\mathrm{CE,sat}$, $I_\mathrm{C}\le B\,I_\mathrm{B}$.
--- falsch
Sperrbereich: $U_\mathrm{BE}<U_\mathrm{BE,ein}$, $I_\mathrm{B}=I_\mathrm{C}=0$. Aktiv: $I_\mathrm{B}>0$, $I_\mathrm{C}\le B\,I_\mathrm{B}$, $U_\mathrm{CE}=U_\mathrm{CE,sat}$. Sättigung: $I_\mathrm{B}>0$, $U_\mathrm{CE}\ge U_\mathrm{CE,sat}$, $I_\mathrm{C}=B\,I_\mathrm{B}$.
--- falsch
Sperrbereich: $U_\mathrm{CE}<U_\mathrm{CE,sat}$, $I_\mathrm{C}=0$. Aktiv: $I_\mathrm{B}>0$, $I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{BE}\ge U_\mathrm{BE,ein}$. Sättigung: $I_\mathrm{B}=0$, $U_\mathrm{CE}=U_\mathrm{CC}$, $I_\mathrm{C}\le B\,I_\mathrm{B}$.
--- falsch
Sperrbereich: $U_\mathrm{BE}<U_\mathrm{BE,ein}$, $I_\mathrm{B}=I_\mathrm{C}=0$. Aktiv: $I_\mathrm{B}>0$, $I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}\ge U_\mathrm{CE,sat}$. Sättigung: $I_\mathrm{B}>0$, $U_\mathrm{CE}=U_\mathrm{CE,sat}$, $I_\mathrm{C}\ge B\,I_\mathrm{B}$.
:::
:::karte zusammenhang Ersatzschaltbild
Welches lineare Ersatzschaltbild gehört zu jedem der drei Arbeitsbereiche, und was gilt in allen?
---
Sperrbereich: alle Klemmen offen. Aktiv: zwischen B und E eine Spannungsquelle mit 0,6 V, zwischen C und E eine gesteuerte Stromquelle. Sättigung: 0,6 V zwischen B und E und 0,2 V zwischen C und E. Im Knoten gilt immer $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$.
--- falsch
Sperrbereich: alle Klemmen kurzgeschlossen. Aktiv: zwischen B und E ein Widerstand, zwischen C und E eine Spannungsquelle mit 0,2 V. Sättigung: zwischen C und E eine gesteuerte Stromquelle. Im Knoten gilt immer $I_\mathrm{C}=I_\mathrm{B}+I_\mathrm{E}$.
--- falsch
Sperrbereich: zwischen B und E eine Spannungsquelle mit 0,6 V, sonst offen. Aktiv: zusätzlich eine gesteuerte Stromquelle zwischen C und B. Sättigung: alle Klemmen offen. Im Knoten gilt immer $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$.
--- falsch
In allen drei Bereichen dasselbe: zwischen B und E eine Spannungsquelle mit 0,6 V und zwischen C und E eine gesteuerte Stromquelle $B\,I_\mathrm{B}$. Nur die Werte der Quellen ändern sich von Bereich zu Bereich.
:::
:::karte zusammenhang Sättigung erkennen
Woran erkennt man, dass ein Transistor mit $B=200$, $I_\mathrm{B}=30$ µ A und $I_\mathrm{C}=3{,}9$ mA gesättigt ist?
---
$B\,I_\mathrm{B}=6$ mA ist größer als der Strom, den der Kreis zulässt. $I_\mathrm{C}$ bleibt unter $B\,I_\mathrm{B}$, also gilt das Ersatzschaltbild der Sättigung.
--- falsch
$I_\mathrm{C}$ liegt über 2 mA, dem Strom im Arbeitspunkt des Rechenmodells. Jeder größere Strom gilt als Sättigung, weil die Basis dann voll ist.
--- falsch
$B\,I_\mathrm{B}=6$ mA ist größer als $I_\mathrm{C}$, also ist der Transistor aktiv; gesättigt wäre er erst, wenn $I_\mathrm{C}$ größer als $B\,I_\mathrm{B}$ würde.
--- falsch
$I_\mathrm{B}=30$ µ A ist größer als 10 µ A. Ein Basisstrom über diesem Wert sättigt jeden Transistor mit $B=200$, gleich welcher Kreis angeschlossen ist.
:::
:::karte zusammenhang Wort Sättigung
Warum heißt der Bereich Sättigung, obwohl der Strom dort gerade nicht mehr $B\,I_\mathrm{B}$ folgt?
---
Gesättigt ist nicht der Strom, sondern die Basis: Sie ist mit Elektronen übervoll. Beim MOSFET heißt dagegen der flache Teil der Ausgangskennlinie Sättigung; die beiden Wörter meinen Verschiedenes.
--- falsch
Gesättigt ist der Kollektorstrom: Er hat seinen Höchstwert $B\,I_\mathrm{B}$ erreicht und kann nicht weiter steigen. Bei MOSFET und Bipolartransistor bedeutet das Wort deshalb dasselbe.
--- falsch
Gesättigt ist die CB-Diode: Sie sperrt so stark, dass ihr Sperrstrom nicht weiter wächst. Das Wort bezeichnet beim Bipolartransistor deshalb den flachen Teil der Ausgangskennlinie.
--- falsch
Gesättigt ist die Versorgung: Sie liefert ihren größten Strom, und der Transistor kann nichts mehr hinzufügen. Das Wort beschreibt also die Quelle, nicht das Bauteil, beim MOSFET ebenso wie beim Bipolartransistor.
:::
:::karte zusammenhang Grenze zwischen aktivem Bereich und Sättigung
Was gilt genau an der Grenze zwischen aktivem Bereich und Sättigungsbereich, und welches Ersatzschaltbild ist dort richtig?
---
Dort sind $B\,I_\mathrm{B}=I_\mathrm{C}$ und $U_\mathrm{CE}=U_\mathrm{CE,sat}$ zugleich erfüllt. Beide Ersatzschaltbilder liefern dort dasselbe.
--- falsch
Dort ist $I_\mathrm{C}=0$ und $U_\mathrm{CE}=U_\mathrm{CC}$. Nur das Ersatzschaltbild mit offenen Klemmen ist dort richtig.
--- falsch
Dort ist $U_\mathrm{BE}=U_\mathrm{CE,sat}$, und kein Ersatzschaltbild gilt. Man muss an dieser Stelle mit der e-Funktion rechnen.
--- falsch
Dort ist $I_\mathrm{C}=2\,B\,I_\mathrm{B}$ und $U_\mathrm{CE}=0$. Nur das Ersatzschaltbild der Sättigung ist dort richtig.
:::
:::karte formel Arbeitsbereiche des pnp-Transistors
Welche Bedingungen gelten für einen pnp-Transistor, wenn man die npn-Bezeichnungen beibehält und $I_\mathrm{B}$ und $I_\mathrm{C}$ aus dem Bauteil heraus zählt?
---
Sperrbereich: $U_\mathrm{BE}>-0{,}6\,\mathrm{V}$. Aktiv: $I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}\le-0{,}2\,\mathrm{V}$. Sättigung: $U_\mathrm{CE}=-0{,}2\,\mathrm{V}$, $I_\mathrm{C}\le B\,I_\mathrm{B}$. Der Emitter liegt am höchsten Potenzial.
--- falsch
Sperrbereich: $U_\mathrm{BE}<-0{,}6\,\mathrm{V}$. Aktiv: $I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}\ge-0{,}2\,\mathrm{V}$. Sättigung: $U_\mathrm{CE}=-0{,}2\,\mathrm{V}$, $I_\mathrm{C}\le B\,I_\mathrm{B}$. Der Emitter liegt am tiefsten Potenzial.
--- falsch
Dieselben wie beim npn-Transistor: Sperrbereich $U_\mathrm{BE}<0{,}6$ V, aktiv $U_\mathrm{CE}\ge0{,}2$ V, Sättigung $U_\mathrm{CE}=0{,}2$ V. Nur die Ströme fließen, aus dem Bauteil heraus gezählt, negativ.
--- falsch
Sperrbereich: $U_\mathrm{BE}>-0{,}6\,\mathrm{V}$. Aktiv: $I_\mathrm{C}=-B\,I_\mathrm{B}$, $U_\mathrm{CE}\le-0{,}2\,\mathrm{V}$. Sättigung: $U_\mathrm{CE}=-0{,}2\,\mathrm{V}$, $I_\mathrm{C}\ge-B\,I_\mathrm{B}$. Der Emitter liegt an Masse.
:::
:::karte zusammenhang npn häufiger als pnp
Warum verwendet man in der Praxis häufiger npn- als pnp-Transistoren, und wo setzt man die pnp-Form trotzdem ein?
---
Weil Elektronen in Silizium rund dreimal beweglicher sind als Löcher. Die pnp-Form dient vor allem dort, wo der Emitter an der positiven Versorgung liegen soll.
--- falsch
Weil pnp-Transistoren eine negative Versorgung brauchen, die es in Geräten selten gibt. Man setzt sie nur dort ein, wo eine negative Spannung schon vorhanden ist.
--- falsch
Weil Löcher in Silizium rund dreimal beweglicher sind als Elektronen und pnp-Transistoren deshalb zu schnell schalten. Man nutzt sie nur in langsamen Schaltungen.
--- falsch
Weil im pnp-Transistor die Mechanismen anders sind und keine Injektion auftritt. Man setzt ihn nur als Diode ein, wenn der Emitter an Masse liegen soll.
:::
::::
