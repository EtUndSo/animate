---
title: PMOS-Transistor, Substrateffekt und Latch-Up
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / MOS-Feldeffekttransistoren
order: 33030300
summary: Wie der p-Kanal-MOSFET als Spiegelbild des NMOS arbeitet, warum eine Spannung zwischen Bulk und Source die Schwellenspannung verschiebt und wie in CMOS-Schaltungen ein parasitärer Thyristor die Versorgung kurzschließen kann. Kompakte Fassung mit den PMOS-Gleichungen, der Herleitung des Substrateffekts, dem Sourcefolger als Beispiel und der Zündbedingung des Latch-Up mit ihren Gegenmaßnahmen, durchgerechnet am Beispiel-Transistorpaar.
tags: PMOS, Substrateffekt, Body-Effekt, Latch-Up, CMOS
stil: 3
fassung: kompakt
---

## Worum es geht

In einer integrierten CMOS-Schaltung sitzen n-Kanal- und p-Kanal-Transistoren nebeneinander auf derselben Siliziumscheibe. Zum Modell des NMOS aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien.html) kommen deshalb drei Dinge hinzu: die Gleichungen des PMOS, der Einfluss des vierten Anschlusses, des Bulk, und die Gefahr, die von den pn-Übergängen zwischen den Transistoren ausgeht. Alles hängt an einem Prinzip:

**Ein MOSFET ist nur durch gesperrte pn-Übergänge von seiner Umgebung getrennt, und sein Bulk wirkt wie ein zweites Gate: Beim PMOS sind Gebiete und Vorzeichen vertauscht, eine Sperrspannung zwischen Bulk und Source vergrößert die Verarmungsladung und damit den Betrag der Schwelle, und werden die trennenden Übergänge leitend, bilden Wanne und Substrat einen Thyristor, der die Versorgung kurzschließt.**

Vorausgesetzt werden Aufbau, Schwellenspannung und Bulkregel aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise.html), die Kennlinien des NMOS und für den Latch-Up der [Bipolartransistor](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html). Darauf bauen die parasitären Kapazitäten, das Kleinsignalmodell und alle CMOS-Schaltungen auf.

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-cmos-ueberblick · Vorlage: querschnitt-hervorhebungen
**Abbildung 1:** CMOS-Querschnitt, schematisch: links ein NMOS im p-Substrat mit Substratkontakt an Masse, rechts ein PMOS in der n-Wanne mit Wannenkontakt an der Versorgung $U_B$ = 2,5 V; alle pn-Übergänge als kleine, gesperrte Dioden. Drei Hervorhebungen: (1) der PMOS als Spiegelbild mit Löcherkanal und negativen Spannungen gegen die Source; (2) ein NMOS, dessen Source 1 V über dem Substrat liegt, mit einer Verarmungszone von 66 statt 46 nm unter dem Gate; (3) gestrichelt der Pfad von der PMOS-Source durch Wanne und Substrat zur NMOS-Source, die Schichtfolge p⁺–n–p–n⁺. Die Transistoren sind nur durch gesperrte pn-Übergänge voneinander getrennt, und das Potential von Substrat und Wanne wirkt auf jeden Transistor mit.
:::

## Der PMOS-Transistor

*Wie arbeitet der p-Kanal-MOSFET, und warum sind bei ihm Spannungen und Strom negativ?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-pmos-kennlinien · Vorlage: schaltzeichen-kennlinienfeld
**Abbildung 2:** (a) Schaltzeichen des PMOS mit denselben Zählpfeilen wie beim NMOS: $U_{GS}$ und $U_{DS}$ vom Gate bzw. Drain zur Source, $U_{BS}$ vom Bulk zur Source, $I_D$ in den Drain hinein; daneben das Großsignal-Ersatzschaltbild mit offenem Gate und gesteuerter Stromquelle zwischen Source und Drain, dazu die Betragsgrößen $U_{SG}$, $U_{SD}$ und $I_{SD}$. (b) Ausgangskennlinien des Beispiel-PMOS mit Vorzeichen im dritten Quadranten: $I_D$ über $U_{DS}$ von 0 bis −2,5 V für $U_{GS}$ = −0,75 V, −1 V, −1,25 V und −1,5 V, bei −2,5 V −0,078 mA, −0,3125 mA, −0,703 mA und −1,25 mA; gestrichelt die Bereichsgrenze bei $U_{DS} = U_{GS} - U_{th,p}$. (c) Dieselben Kennlinien in Betragsdarstellung, $I_{SD}$ über $U_{SD}$. Der PMOS verhält sich wie ein NMOS mit umgekehrten Vorzeichen aller Spannungen und Ströme.
:::

Der PMOS ist das Spiegelbild des NMOS: Source und Drain sind p⁺-Gebiete in einer n-dotierten __Wanne__, einem in das p-Substrat eingebrachten Gebiet, das an der höchsten Spannung der Schaltung liegt. Liegt das Gate weit genug unter der Source, bildet sich an der Oberfläche eine Schicht aus Löchern. Die positiv geladenen Löcher laufen zum niedrigeren Potential; die Source ist deshalb das p⁺-Gebiet mit dem höheren Potential, und der Strom fließt aus dem Drain heraus.

Mit denselben Zählpfeilen wie beim NMOS (Abbildung 2a) sind deshalb im Betrieb alle Größen negativ: $U_{GS}$, weil das Gate unter der Source liegt, $U_{DS}$, weil der Drain tiefer liegt, $I_D$, weil der Strom herausfließt, und die Schwelle, beim Beispiel-PMOS −0,5 V. Die Kennlinien liegen im dritten Quadranten (Abbildung 2b) und gleichen gespiegelt denen des NMOS (Abbildung 2c).

**Die Akteure:**

- __$U_{th,p}$__: Schwellenspannung des PMOS, negativ; −0,5 V.
- __$K_p$__: Steilheitskoeffizient des PMOS, $K'_p W/L$ mit $K'_p = \mu_p C'_\mathrm{ox}$ = 50 µA/V² und der Beweglichkeit der Löcher $\mu_p$ = 72 cm²/(V s); 2 mA/V² bei $W/L$ = 40.
- __$U_{SG}$__, __$U_{SD}$__, __$I_{SD}$__: Betragsgrößen, gezählt von der Source aus; im Betrieb positiv, jeweils das Negative von $U_{GS}$, $U_{DS}$ und $I_D$.
- __$\lambda$__: Kanallängenmodulationsfaktor als positiver Betrag; 0,1 1/V.

:::formel Formel
Sperrbereich, $U_{GS} > U_{th,p}$:

$$I_D = 0$$

Ohmscher Bereich, $U_{GS} < U_{th,p}$ und $U_{DS} > U_{GS} - U_{th,p}$:

$$I_D = -K_p\Big[\big(U_{GS} - U_{th,p}\big)\,U_{DS} - \frac{U_{DS}^2}{2}\Big]\big(1 - \lambda\,U_{DS}\big)$$

Abschnürbereich, $U_{GS} < U_{th,p}$ und $U_{DS}$ höchstens $U_{GS} - U_{th,p}$:

$$I_D = -\frac{K_p}{2}\,\big(U_{GS} - U_{th,p}\big)^2\,\big(1 - \lambda\,U_{DS}\big)$$
:::

**So liest man das:** Alle Ungleichungen sind gegenüber dem NMOS umgekehrt, und der Faktor $(1 - \lambda U_{DS})$ ist bei negativem $U_{DS}$ größer als 1. Üblich ist auch, λ für den PMOS selbst negativ anzugeben; dann steht dort $(1 + \lambda U_{DS})$. Setzt man alle Größen dem Betrag nach ein, erhält man die NMOS-Gleichungen, im Abschnürbereich etwa

$$I_{SD} = \frac{K_p}{2}\,\big(U_{SG} - |U_{th,p}|\big)^2\,\big(1 + \lambda\,U_{SD}\big)$$

Mit dieser __Betragsform__ rechnet man meist.

**Kurz gesagt:** Kehrt man beim PMOS die Vorzeichen aller Spannungen, des Stroms und der Schwellenspannung um, gelten genau die Gleichungen des NMOS.

Idee der Herleitung: Man wiederholt die Herleitung des NMOS mit Löchern statt Elektronen und misst alle Spannungen von der Source aus nach unten.

:::herleitung
**Ausgangspunkt:** die Herleitung der Triodengleichung und des Quadratgesetzes aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html), dort für Elektronen mit der Ladung pro Fläche $C'_\mathrm{ox}$ mal der örtlichen Übersteuerung.

**Annahmen:**
(i) dieselben wie beim NMOS: Langkanal, allmählicher Kanal, konstante Beweglichkeit, hier die der Löcher $\mu_p$;
(ii) der Bulk, also die Wanne, liegt auf dem Potential der Source.

**Schritt 1**: Beim PMOS sind alle Ladungen und Spannungen gespiegelt. Misst man von der Source nach unten, mit $U_{SG}$, $U_{SD}$ und der Spannung $U_{SC}(x)$ von der Source zum Kanal an der Stelle $x$, trägt der Kanal oberhalb der Schwelle die positive Löcherladung pro Fläche

$$Q'_p(x) = C'_\mathrm{ox}\,\big(U_{SG} - |U_{th,p}| - U_{SC}(x)\big)$$

**Schritt 2**: Die Löcher laufen zum niedrigeren Potential, also zum Drain, mit der Geschwindigkeit $\mu_p\,dU_{SC}/dx$; der Strom fließt in ihrer Richtung, von der Source zum Drain:

$$I_{SD} = \mu_p\,W\,C'_\mathrm{ox}\,\big(U_{SG} - |U_{th,p}| - U_{SC}(x)\big)\,\frac{dU_{SC}}{dx}$$

**Schritt 3**: Das ist die Stromgleichung des NMOS mit vertauschten Namen. Dieselbe Integration und dieselbe Überlegung zur Abschnürung ergeben mit $K_p = \mu_p C'_\mathrm{ox} W/L$ und dem Faktor der Kanallängenmodulation

$$I_{SD} = K_p\Big[\big(U_{SG} - |U_{th,p}|\big)\,U_{SD} - \frac{U_{SD}^2}{2}\Big]\big(1 + \lambda\,U_{SD}\big)$$

im ohmschen Bereich für $U_{SD} < U_{SG} - |U_{th,p}|$, sonst im Abschnürbereich

$$I_{SD} = \frac{K_p}{2}\,\big(U_{SG} - |U_{th,p}|\big)^2\,\big(1 + \lambda\,U_{SD}\big)$$

**Schritt 4** (entscheidender Schritt): Rückübersetzung in die Zählpfeile des NMOS:

$$I_D = -I_{SD}, \qquad U_{SG} = -U_{GS}, \qquad U_{SD} = -U_{DS}, \qquad |U_{th,p}| = -U_{th,p}\,$$

Die Übersteuerung wird dabei zu $-(U_{GS} - U_{th,p})$; das Produkt zweier negativer Größen bleibt positiv, das Quadrat ebenso.

**Schritt 5**: Die Bereichsgrenzen übersetzen sich mit umgekehrtem Ungleichheitszeichen: $U_{SG} > |U_{th,p}|$ wird zu $U_{GS} < U_{th,p}$, und $U_{SD} < U_{SG} - |U_{th,p}|$ wird zu $U_{DS} > U_{GS} - U_{th,p}$.

**Ergebnis:** im Sperrbereich $I_D$ = 0, sonst

$$I_D = -K_p\Big[\big(U_{GS} - U_{th,p}\big)\,U_{DS} - \frac{U_{DS}^2}{2}\Big]\big(1 - \lambda\,U_{DS}\big)$$

$$I_D = -\frac{K_p}{2}\,\big(U_{GS} - U_{th,p}\big)^2\,\big(1 - \lambda\,U_{DS}\big)$$

**Woher die Faktoren kommen:** Das Minuszeichen vor $K_p$ ist die Zählrichtung; $K_p$ enthält die Beweglichkeit der Löcher; $(1 - \lambda U_{DS})$ ist $(1 + \lambda U_{SD})$.

**Proben:** Bei $U_{GS}$ = −1 V und $U_{DS}$ = −0,3 V: $-2\ \mathrm{mA/V^2}\cdot(0{,}15 - 0{,}045)\ \mathrm{V^2}\cdot1{,}03$ = −0,2163 mA, dem Betrag nach derselbe Strom wie beim NMOS mit +1 V und +0,3 V. Grenzfall: An der Bereichsgrenze stimmen beide Ausdrücke überein.

**Grenzen:** Dieselben wie beim NMOS: Langkanal, Kanallängenmodulation als Modell, Unterschwellenstrom vernachlässigt.
:::

::::beispiel PMOS bei −1 V Gatespannung in Vorzeichen- und Betragsform
**Gegeben:** Beispiel-PMOS mit $K_p$ = 2 mA/V², $U_{th,p}$ = −0,5 V, λ = 0,1 1/V; $U_{GS}$ = −1 V; (a) $U_{DS}$ = −0,3 V, (b) $U_{DS}$ = −2 V; (c) der PMOS als Schalter von $U_B$ = 2,5 V zu einem Ausgang, Gate auf 0 V.

**Gesucht:** Drainstrom in beiden Formen; Widerstand des eingeschalteten Schalters.

**Rechnung:** (a) $U_{DS}$ = −0,3 V liegt über $U_{GS} - U_{th,p}$ = −0,5 V: ohmscher Bereich.

$$\begin{aligned} I_D &= -2\ \mathrm{mA/V^2}\cdot\big[(-0{,}5\ \mathrm V)(-0{,}3\ \mathrm V) - 0{,}045\ \mathrm{V^2}\big]\cdot1{,}03 \\ &= -0{,}2163\ \mathrm{mA} \end{aligned}$$

Betragsform mit $U_{SG}$ = 1 V und $U_{SD}$ = 0,3 V:

$$I_{SD} = 2\ \mathrm{mA/V^2}\cdot\big[0{,}5\ \mathrm V\cdot0{,}3\ \mathrm V - 0{,}045\ \mathrm{V^2}\big]\cdot1{,}03 = 0{,}2163\ \mathrm{mA}$$

(b) $U_{DS}$ = −2 V liegt unter −0,5 V: Abschnürbereich.

$$I_D = -1\ \mathrm{mA/V^2}\cdot(-0{,}5\ \mathrm V)^2\cdot\big(1 + 0{,}2\big) = -0{,}30\ \mathrm{mA}$$

(c) Mit $U_{GS}$ = −2,5 V und kleiner Spannung über dem Schalter:

$$R_\mathrm{on} = \frac{1}{K_p\,\big(U_{SG} - |U_{th,p}|\big)} = \frac{1}{2\ \mathrm{mA/V^2}\cdot2\ \mathrm V} = 250\ \Omega$$

**Ergebnis:** **(a) $I_D$ = −0,2163 mA, $I_{SD}$ = 0,2163 mA; (b) −0,30 mA; (c) 250 Ω.**

**Einordnung:** Beide Formen ergeben denselben Strom; die Betragsform vermeidet Vorzeichenfehler. Der PMOS leitet, wenn sein Gate tief liegt, der NMOS, wenn es hoch liegt; zwischen Versorgung und Masse ergänzen sich beide zu einem Schalterpaar, dem Grundprinzip der CMOS-Logik.
::::

:::frage
„Warum braucht der PMOS die vierfache Weite, um so viel Strom zu führen wie der NMOS?“
Löcher sind in Silizium langsamer als Elektronen: In reinem Silizium beträgt ihre Beweglichkeit 450 gegen 1400 cm²/(V s), im Kanal des Beispielprozesses 72 gegen 290 cm²/(V s). Der Prozessparameter $K'_p$ ist deshalb mit 50 µA/V² viermal kleiner als $K'_n$ mit 200 µA/V², und gleiche Ströme verlangen bei gleicher Länge die vierfache Weite, 40 statt 10 µm. Mit 10 µm hätte der PMOS als Schalter 1 kΩ statt 250 Ω.
:::

:::fehlvorstellung
„Beim PMOS setze ich die negativen Spannungen direkt in die NMOS-Gleichungen ein.“ Das liegt nahe, weil beide Transistoren dieselben Zählpfeile haben. Mit der positiven Schwelle des NMOS geht das schief: Bei $U_{GS}$ = −1 V und $U_{th}$ = +0,5 V meldet die Bereichsprüfung „gesperrt“, und quadriert man trotzdem, ergeben sich mit $(-1{,}5\ \mathrm V)^2$ 2,25 mA. Richtig sind im Abschnürbereich −0,25 mA, ohne Kanallängenmodulation gerechnet: mit den PMOS-Gleichungen und $U_{th,p}$ = −0,5 V oder mit allen Größen dem Betrag nach.
:::

## Der Substrateffekt

*Warum hängt die Schwellenspannung von der Spannung zwischen Bulk und Source ab?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-substrateffekt-querschnitt · Vorlage: querschnitt-vergleich
**Abbildung 3:** Zwei Querschnitte des Beispiel-NMOS unter dem Gate, jeweils genau an der Schwelle, maßstäblich in der Tiefe. (a) $U_{BS}$ = 0: Die Oberfläche liegt 0,923 V über dem Inneren des Substrats, die Verarmungszone ist 45,8 nm tief und trägt 4,17 fC/µm² feste negative Ladung; Schwelle 0,500 V. (b) $U_{BS}$ = −1 V, Source und Kanal also 1 V über dem Substrat: Die Oberfläche muss 1,923 V über dem Inneren liegen, die Zone ist 66,2 nm tief und trägt 6,02 fC/µm²; Schwelle 0,768 V gegen die Source. Daneben je ein Balken für die Ladung auf dem Gate, in (b) um 1,85 fC/µm² höher. Liegt die Source über dem Bulk, muss die Oberfläche höher angehoben werden; die breitere Verarmungszone bindet mehr Gateladung, und die Schwelle steigt.
:::

Alle NMOS-Transistoren einer integrierten Schaltung teilen sich dasselbe p-Substrat an Masse. Liegt die Source eines NMOS 1 V über Masse, hat er zwischen Bulk und Source −1 V, und seine Schwelle steigt von 0,5 V auf 0,768 V. Diese Verschiebung heißt __Substrateffekt__, englisch body effect.

**Die Akteure:**

- __$U_{BS}$__: Spannung vom Bulk zur Source; beim NMOS im Betrieb null oder negativ, das heißt in Sperrrichtung; −1 V, wenn die Source 1 V über dem Substrat liegt.
- __$2\Phi_F$__: Oberflächenpotential an der Schwelle bei $U_{BS}$ = 0 ([Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise.html)); 0,923 V.
- __$\gamma$__: __Substratsteuerfaktor__, auch Body-Effekt-Faktor, in √V; 0,63 √V beim Beispiel-NMOS.

**Das Zusammenspiel:**

**Schritt 1**: Die Elektronen des Kanals stammen aus der Source und liegen auf ihrem Potential. Für starke Inversion zählt deshalb, wie hoch die Oberfläche über dem Potential der Source liegt.

**Schritt 2**: Liegt die Source 1 V über dem Bulk, muss die Oberfläche um $2\Phi_F$ über die Source hinaus angehoben werden, gegenüber dem Substrat also um 1,923 V statt 0,923 V (Abbildung 3b).

**Schritt 3** (entscheidender Schritt): Dafür muss die Verarmungszone breiter werden. Ihre Tiefe wächst mit der Wurzel der Spannung über ihr, von 45,8 auf 66,2 nm, ihre feste Ladung von 4,17 auf 6,02 fC/µm².

**Schritt 4**: Die zusätzlichen 1,85 fC/µm² muss das Gate tragen; über dem Oxid liegen dafür 0,268 V mehr.

**Schritt 5**: Gegen die Source gemessen steigt die Schwelle um diese 0,268 V auf 0,768 V. Das um 1 V höhere Oberflächenpotential zählt nicht mit, weil Gate und Oberfläche beide gegen die angehobene Source gerechnet werden.

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-schwelle-ubs · Vorlage: kennlinie
**Abbildung 4:** Schwellenspannung über der Sperrspannung zwischen Source und Bulk (beim NMOS −$U_{BS}$, beim PMOS +$U_{BS}$) von −0,4 V bis 2,5 V. NMOS: 0,500 V bei 0, 0,646 V bei 0,5 V, 0,768 V bei 1 V, 0,971 V bei 2 V und 1,059 V bei 2,5 V; links von null, wo der Bulk über der Source liegt, sinkt sie auf 0,431 V, 0,392 V und 0,351 V bei 0,2 V, 0,3 V und 0,4 V Durchlassspannung (grau hinterlegt: Die Diode zwischen Bulk und Source beginnt zu leiten). PMOS, Betrag der Schwelle: 0,500 V bei 0, 0,762 V bei 1 V, 1,048 V bei 2,5 V. Gestrichelt die Tangente im Nullpunkt mit der Steigung 0,327. Die Schwelle wächst mit der Wurzel der Sperrspannung zwischen Source und Bulk; jedes weitere Volt hebt sie weniger.
:::

:::formel Formel
$$U_{th} = U_{th0} + \gamma\,\Big(\sqrt{2\Phi_F - U_{BS}} - \sqrt{2\Phi_F}\Big)$$

$$\gamma = \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A}}{C'_\mathrm{ox}}$$

beim PMOS (Index p) mit der Schwelle $U_{th0,p}$ bei $U_{BS}$ = 0 und der Dotierung $N_D$ der n-Wanne:

$$|U_{th,p}| = |U_{th0,p}| + \gamma_p\,\Big(\sqrt{2\Phi_{F,p} + U_{BS}} - \sqrt{2\Phi_{F,p}}\Big)$$

$$\gamma_p = \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_D}}{C'_\mathrm{ox}}, \qquad \Phi_{F,p} = U_T\ln\frac{N_D}{n_i}\,$$
:::

**So liest man das:** Bei $U_{BS}$ = 0 bleibt $U_{th0}$. Je weiter der Bulk in Sperrrichtung gegen die Source gepolt ist, desto höher die Schwelle des NMOS, aber nur mit der Wurzel: Das erste Volt bringt 0,268 V, das zweite 0,203 V. $\gamma$ wächst mit der Wurzel der Dotierung; der Beispiel-NMOS hat wegen der hohen Dotierung unter dem Gate ein großes $\gamma$. Beim PMOS ist alles gespiegelt: Positives $U_{BS}$ ist Sperrrichtung, und mit $\gamma_p$ = 0,615 √V und $2\Phi_{F,p}$ = 0,921 V wächst der Betrag der Schwelle bei 1 V auf 0,762 V.

**Kurz gesagt:** Je weiter der Bulk in Sperrrichtung gegen die Source gepolt ist, desto größer ist der Betrag der Schwelle; jedes weitere Volt vergrößert ihn weniger als das vorige.

Idee der Herleitung: Man schreibt die Spannungsbilanz der Schwelle mit dem um die Bulk-Source-Spannung höheren Oberflächenpotential und rechnet dann gegen die Source.

:::herleitung
**Ausgangspunkt:** die Spannungsbilanz an der Schwelle und die Verarmungsladung aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html), beide gegen den Bulk gemessen:

$$U_{GB} = U_\mathrm{FB} + \psi_s + \frac{|Q'_\mathrm{dep}|}{C'_\mathrm{ox}}, \qquad |Q'_\mathrm{dep}| = \sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\psi_s}\,$$

**Annahmen:**
(i) Verarmungsnäherung wie dort; die Elektronenladung an der Schwelle ist klein gegen die Verarmungsladung.
(ii) Starke Inversion: Elektronendichte an der Oberfläche gleich $N_A$, gezählt gegen das Potential der Elektronen im Kanal, also das der Source.
(iii) $U_{BS}$ null oder negativ, oder nur so wenig positiv, dass die Diode zwischen Bulk und Source sperrt.

**Schritt 1**: Ohne Bulk-Source-Spannung ist das Oberflächenpotential an der Schwelle $2\Phi_F$. Liegt die Source um $-U_{BS}$ über dem Bulk, gilt nach (ii) dasselbe gegenüber der Source; gegenüber dem Bulk muss die Oberfläche also höher liegen:

$$\psi_s = 2\Phi_F - U_{BS}$$

**Schritt 2**: Eingesetzt in die Spannungsbilanz:

$$U_{GB} = U_\mathrm{FB} + 2\Phi_F - U_{BS} + \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\big(2\Phi_F - U_{BS}\big)}}{C'_\mathrm{ox}}$$

**Schritt 3** (entscheidender Schritt): Die Schwelle zählt gegen die Source. Mit der Maschenregel $U_{GS} = U_{GB} + U_{BS}$ hebt sich $-U_{BS}$ heraus:

$$U_{th} = U_\mathrm{FB} + 2\Phi_F + \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\big(2\Phi_F - U_{BS}\big)}}{C'_\mathrm{ox}}$$

**Schritt 4**: Bei $U_{BS}$ = 0 ist das $U_{th0}$. Die Differenz zu $U_{th0}$ enthält nur noch die Verarmungsladung; den gemeinsamen Faktor fasst man zu $\gamma$ zusammen:

$$U_{th} - U_{th0} = \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A}}{C'_\mathrm{ox}}\,\Big(\sqrt{2\Phi_F - U_{BS}} - \sqrt{2\Phi_F}\Big)$$

**Schritt 5**: Beim PMOS sind alle Vorzeichen vertauscht: Die n-Wanne mit der Dotierung $N_D$ liegt über der Source, die Sperrspannung ist $+U_{BS}$, und dieselbe Rechnung ergibt für den Betrag der Schwelle die zweite Gleichung mit $\gamma_p$ und dem Fermipotential der Wanne:

$$2\Phi_{F,p} = 2\,U_T\ln\frac{N_D}{n_i}$$

**Ergebnis:**

$$U_{th} = U_{th0} + \gamma\,\Big(\sqrt{2\Phi_F - U_{BS}} - \sqrt{2\Phi_F}\Big), \qquad \gamma = \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A}}{C'_\mathrm{ox}}\,$$

$$|U_{th,p}| = |U_{th0,p}| + \gamma_p\,\Big(\sqrt{2\Phi_{F,p} + U_{BS}} - \sqrt{2\Phi_{F,p}}\Big)$$

**Woher die Faktoren kommen:** Die Wurzeln stammen aus dem Wurzelgesetz der Verarmungszone; $\gamma$ ist die Verarmungsladung pro Wurzel-Volt geteilt durch die Oxidkapazität.

**Proben:** Einheit: $\sqrt{\mathrm{C\cdot F\cdot cm^{-1}\cdot cm^{-3}}}$ geteilt durch F/cm² ergibt √V, mal √V ergibt V. Zahlenwert: $\sqrt{2\cdot1{,}602\cdot10^{-19}\cdot1{,}036\cdot10^{-12}\cdot5{,}68\cdot10^{17}}$ C/(cm²·√V) geteilt durch 6,906·10⁻⁷ F/cm² ergibt 0,629 √V; bei $U_{BS}$ = −1 V: 0,629 · (1,387 − 0,961) V = 0,268 V. Die vollständige Lösung der Poisson-Gleichung, mit dem Potential der Elektronen um 1 V verschoben, ergibt an der Schwelle dieselben Werte, weil sich der Ausläufer der Löcher am Rand der Zone und die Elektronen an der Oberfläche genau ausgleichen.

**Grenzen:** Ist die Dotierung unter dem Gate nicht gleichmäßig, wie nach einer Implantation, ändert sich $\gamma$ mit der Tiefe der Zone. Ist $U_{BS}$ beim NMOS mehr als einige Zehntel Volt positiv, leitet die Diode zwischen Bulk und Source.
:::

::::beispiel Schwellenspannungen des Beispiel-NMOS mit Substrateffekt
**Gegeben:** $U_{th0}$ = 0,5 V, $\gamma$ = 0,629 √V, $2\Phi_F$ = 0,923 V; $K_n$ = 2 mA/V².

**Gesucht:** die Schwelle bei $U_{BS}$ = −1 V und −2 V und der Sättigungsstrom bei 1 V Gatespannung und $U_{BS}$ = −1 V.

**Rechnung:** Bei −1 V:

$$\begin{aligned} U_{th} &= 0{,}5\ \mathrm V + 0{,}629\ \sqrt{\mathrm V}\cdot\big(\sqrt{1{,}923\ \mathrm V} - \sqrt{0{,}923\ \mathrm V}\big) \\ &= 0{,}5\ \mathrm V + 0{,}268\ \mathrm V = 0{,}768\ \mathrm V \end{aligned}$$

Bei −2 V ebenso 0,5 V + 0,471 V = 0,971 V. Sättigungsstrom bei 1 V Gatespannung und −1 V am Bulk, ohne Kanallängenmodulation:

$$I_D = 1\ \mathrm{mA/V^2}\cdot\big(1\ \mathrm V - 0{,}768\ \mathrm V\big)^2 = 0{,}054\ \mathrm{mA}$$

**Ergebnis:** **0,768 V und 0,971 V; der Sättigungsstrom fällt von 0,25 mA auf 0,054 mA.**

**Einordnung:** Schon 1 V Sperrspannung hebt die Schwelle um mehr als die Hälfte, und weil der Strom quadratisch von der Übersteuerung abhängt, fällt er auf gut ein Fünftel, 22 %. Eine Schwellenspannung im Datenblatt gilt deshalb immer für eine bestimmte Bulk-Source-Spannung, meist null.
::::

Für kleine Änderungen wirkt der Bulk wie ein zweites, schwächeres Gate, das über die Verarmungszone an den Kanal koppelt: Ein Millivolt am Bulk verschiebt die Übersteuerung beim Beispiel-NMOS um 0,33 mV bei $U_{BS}$ = 0 und um 0,23 mV bei −1 V. Das ist die Steigung der Kurve in Abbildung 4.

## Der Substrateffekt in Schaltungen

*Wo tritt der Substrateffekt auf, und wie lässt er sich vermeiden?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-sourcefolger · Vorlage: schaltung-kennlinie
**Abbildung 5:** (a) NMOS-Sourcefolger: T2 mit Drain an $U_B$ = 2,5 V, Gate am Eingang, Source am Ausgang, Bulk am Substrat auf Masse; darunter eine Stromquelle mit 0,25 mA, etwa ein NMOS T1 mit fester Gatespannung. (b) PMOS-Sourcefolger: T3 mit Drain an Masse, Gate am Eingang, Source am Ausgang, Bulk wahlweise an der eigenen Source oder an $U_B$; darüber eine Stromquelle mit 0,25 mA, etwa ein PMOS T4 mit fester Gatespannung. (c) Ausgangs- über Eingangsspannung: NMOS ohne Substrateffekt die Gerade $U_\mathrm{ein}$ − 1 V (0,5 V, 1,0 V und 1,5 V bei 1,5 V, 2 V und 2,5 V Eingangsspannung), mit Substrateffekt 0,385 V, 0,783 V und 1,190 V; PMOS in eigener Wanne $U_\mathrm{ein}$ + 1 V, in der gemeinsamen Wanne an 2,5 V 1,305 V und 1,714 V bei 0 V und 0,5 V. Der Substrateffekt lässt den Ausgang nur mit etwa 0,8 statt 1 folgen; eine eigene Wanne beseitigt ihn beim PMOS.
:::

Jeder NMOS, dessen Source nicht auf Masse liegt, hat einen Substrateffekt: der obere von zwei Transistoren in Reihe und besonders der __Sourcefolger__ (Abbildung 5a). In ihm liegt der Eingang am Gate, der Ausgang an der Source, und eine Stromquelle hält den Strom und damit die Übersteuerung $U_{GS} - U_{th}$ fest; ohne Substrateffekt folgt der Ausgang dem Eingang mit 1 V Abstand. Mit Substrateffekt steigt die Schwelle mit dem Ausgang, und er folgt nur mit etwa 0,8 (Abbildung 5c).

Vermeiden lässt sich der Substrateffekt nur, wenn der Transistor ein eigenes, mit seiner Source verbundenes Gebiet hat. Bei den meisten Einzeltransistoren ist der Bulk schon im Gehäuse mit der Source verbunden; der Preis ist die Diode zwischen Bulk und Drain, die nun als __Inversdiode__ zwischen Source und Drain liegt. Beim PMOS kann man jedem Transistor eine eigene Wanne geben und sie mit seiner Source verbinden (Abbildung 5b); das kostet Fläche und eine zusätzliche Kapazität am Ausgang und wird deshalb nur für genau arbeitende Folger und Eingangsstufen getan. NMOS liegen in einem einfachen n-Wannen-Prozess alle im selben Substrat; eine eigene p-Wanne erhalten sie dort nur mit einer zusätzlichen tiefen n-Wanne.

::::beispiel Sourcefolger mit und ohne Substrateffekt
**Gegeben:** Beispiel-NMOS ($U_{th0}$ = 0,5 V, $K_n$ = 2 mA/V², $\gamma$ = 0,629 √V, $2\Phi_F$ = 0,923 V) als Folger mit 0,25 mA, Bulk an Masse; Beispiel-PMOS ($\gamma_p$ = 0,615 √V, $2\Phi_{F,p}$ = 0,921 V) als Folger mit 0,25 mA bei 0,5 V Eingangsspannung; Kanallängenmodulation vernachlässigt.

**Gesucht:** die Ausgangsspannung des NMOS-Folgers bei 1,5 V und 2 V Eingangsspannung, die Steigung dazwischen und die Ausgangsspannung des PMOS-Folgers in eigener und gemeinsamer Wanne.

**Rechnung:** Bei 0,25 mA ist die Übersteuerung $\sqrt{2I_D/K_n}$ = 0,5 V. Der Ausgang liegt um $U_{th}$ + 0,5 V unter dem Eingang, und die Schwelle hängt über $U_{BS} = -U_\mathrm{aus}$ vom Ausgang ab:

$$U_\mathrm{ein} = U_\mathrm{aus} + U_{th0} + \gamma\,\Big(\sqrt{2\Phi_F + U_\mathrm{aus}} - \sqrt{2\Phi_F}\Big) + 0{,}5\ \mathrm V$$

Bei 2 V Eingangsspannung ergibt die Lösung, etwa durch Probieren, 0,783 V mit $U_{th}$ = 0,717 V:

$$0{,}783\ \mathrm V + 0{,}717\ \mathrm V + 0{,}5\ \mathrm V = 2{,}0\ \mathrm V$$

Bei 1,5 V ergibt sich ebenso 0,385 V. Steigung:

$$\frac{0{,}783\ \mathrm V - 0{,}385\ \mathrm V}{0{,}5\ \mathrm V} = 0{,}80$$

PMOS bei 0,5 V Eingangsspannung: in eigener Wanne ohne Substrateffekt 0,5 V + 1 V = 1,5 V; in der gemeinsamen Wanne an 2,5 V mit $U_{BS}$ = 2,5 V − $U_\mathrm{aus}$ ergibt die Lösung 1,714 V mit $|U_{th,p}|$ = 0,714 V.

**Ergebnis:** **NMOS 0,385 V und 0,783 V statt 0,5 V und 1,0 V, Steigung 0,80; PMOS 1,5 V in eigener, 1,714 V in gemeinsamer Wanne.**

**Einordnung:** Ein Sourcefolger soll eine Spannung möglichst unverfälscht weitergeben. Mit dem Substrateffekt gibt er nur 80 % einer Änderung weiter; die eigene Wanne stellt beim PMOS die Steigung 1 wieder her.
::::

:::frage
„Warum verbindet man einen Ausgang über einen PMOS mit der Versorgung und nicht über einen NMOS, der doch mehr Strom liefert?“
Ein NMOS, dessen Drain und Gate an 2,5 V liegen, ist ein Sourcefolger: Er hebt den Ausgang nur, solange zwischen Gate und Source mehr als die Schwelle liegt. Ohne Substrateffekt endete das bei 2,5 V − 0,5 V = 2,0 V; weil die Source dabei immer höher über dem Substrat liegt, steigt die Schwelle aber auf 0,896 V, und der Ausgang erreicht nur 1,6 V. Ein PMOS mit der Source an 2,5 V und dem Gate auf 0 V bleibt dagegen leitend, bis keine Spannung mehr über ihm liegt, und zieht den Ausgang auf volle 2,5 V. Deshalb verbindet in CMOS-Gattern der PMOS mit der Versorgung und der NMOS mit Masse.
:::

## Latch-Up: der parasitäre Thyristor

*Wie kann eine CMOS-Schaltung ihre eigene Versorgung kurzschließen?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-latchup-struktur · Vorlage: querschnitt-ersatzschaltbild
**Abbildung 6:** (a) Querschnitt mit Substratkontakt und NMOS-Source an Masse, n-Wanne mit Wannenkontakt und PMOS-Source an $U_B$; eingezeichnet der laterale npn-Transistor (Emitter: NMOS-Source, Basis: Substrat, Kollektor: Wanne), der vertikale pnp-Transistor (Emitter: PMOS-Source, Basis: Wanne, Kollektor: Substrat), der Substratwiderstand $R_\mathrm{sub}$ von der Basis des npn zum Substratkontakt und der Wannenwiderstand $R_\mathrm{well}$ von der Basis des pnp zum Wannenkontakt. (b) Ersatzschaltbild: beide Transistoren über Kreuz verbunden zwischen $U_B$ und Masse, der Kollektor des einen an der Basis des anderen; ein umlaufender Pfeil zeigt die Mitkopplung mit der Schleifenverstärkung $B_\mathrm{npn}B_\mathrm{pnp}$. (c) Die Schichtfolge p⁺–n–p–n⁺ als Thyristor. Die Gebiete einer CMOS-Schaltung bilden zwei parasitäre Bipolartransistoren, von denen jeder den anderen ansteuert: einen Thyristor zwischen Versorgung und Masse.
:::

Folgt man in Abbildung 6a dem Weg von der PMOS-Source an der Versorgung durch Wanne und Substrat zur NMOS-Source an Masse, durchquert man p⁺, n, p und n⁺: die Schichtfolge eines __Thyristors__, eines Bauelements aus vier abwechselnd dotierten Schichten, das nach dem Zünden von selbst leitend bleibt. Die beiden mittleren Schichten gehören zu zwei Bipolartransistoren zugleich: Die n-Wanne ist Basis des pnp und Kollektor des npn, das Substrat Basis des npn und Kollektor des pnp. Rastet dieser ungewollte Thyristor ein, heißt das __Latch-Up__.

**Die Akteure:**

- __npn__, __pnp__: die parasitären Transistoren, lateral aus NMOS-Source, Substrat und Wanne bzw. vertikal aus PMOS-Source, Wanne und Substrat.
- __$R_\mathrm{sub}$__, __$R_\mathrm{well}$__: Widerstand des Substrats bis zum Substratkontakt und der Wanne bis zum Wannenkontakt; angenommen 1 kΩ und 2 kΩ.
- __$B_\mathrm{npn}$__, __$B_\mathrm{pnp}$__: Stromverstärkungen der parasitären Transistoren, Kollektor- durch Basisstrom; angenommen 5 und 50. Dieses $B$ hat nichts mit dem Index $B$ für Bulk zu tun.

**Das Zusammenspiel:**

**Schritt 1**: Im Betrieb liegt das Substrat an Masse, die Wanne an $U_B$; alle Übergänge des Pfads sperren, beide Transistoren sind aus.

**Schritt 2**: Fließt ein Störstrom ins Substrat, hebt er es über $R_\mathrm{sub}$ unter dem NMOS an; bei 0,6 mA durch 1 kΩ sind es 0,6 V, und die Basis-Emitter-Strecke des npn leitet.

**Schritt 3**: Der Kollektorstrom des npn fließt von $U_B$ durch $R_\mathrm{well}$ in die Wanne und senkt sie unter dem PMOS ab.

**Schritt 4**: Bei 0,6 V an $R_\mathrm{well}$, mit 2 kΩ schon bei 0,3 mA, leitet auch der pnp.

**Schritt 5** (entscheidender Schritt): Sein Kollektorstrom fließt ins Substrat und durch $R_\mathrm{sub}$, denselben Weg wie der Störstrom, und verstärkt Schritt 2: eine __Mitkopplung__. Kommt ein Strom nach einem Umlauf größer zurück, wachsen beide Ströme von selbst.

**Schritt 6**: Begrenzt wird das Wachstum erst von den Widerständen von Wanne und Substrat und von der äußeren Schaltung. Zwischen $U_B$ und Masse liegt nun ein Pfad mit nur rund 1 V, ein Kurzschluss, und er bleibt bestehen, auch wenn der Störstrom vorbei ist. Nur Abschalten beendet ihn, oder ein Versorgungsstrom unter dem __Haltestrom__, dem kleinsten Strom, mit dem sich der Pfad selbst erhält.

:::formel Formel
$$B_\mathrm{npn}\,B_\mathrm{pnp} > 1$$
:::

**So liest man das:** Liegt das Produkt der Stromverstärkungen unter 1, klingt jeder Störstrom ab; liegt es darüber, kann sich der Pfad selbst halten. Mit 5 und 50 ist es 250. Zum Zünden braucht es zusätzlich einen Störstrom, der beide Übergänge leitend macht, im Beispiel 0,66 mA ins Substrat: 0,6 mA, bis der npn leitet, und 0,06 mA mehr, bis sein Kollektorstrom an $R_\mathrm{well}$ 0,6 V erzeugt.

**Kurz gesagt:** Ein Latch-Up hält sich, wenn ein Strom nach einem Umlauf durch beide Transistoren größer zurückkommt, als er losgelaufen ist.

Idee der Herleitung: Man verfolgt einen kleinen zusätzlichen Basisstrom einmal um die Schleife.

:::herleitung
**Ausgangspunkt:** der Zusammenhang zwischen Kollektor- und Basisstrom im aktiven Bereich, $I_C = B\,I_B$, aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise-ausfuehrlich.html), und die Verschaltung aus dem Ersatzschaltbild: Der Kollektor des npn liegt an der Basis des pnp, der Kollektor des pnp an der Basis des npn.

**Annahmen:**
(i) Beide parasitären Transistoren sind im aktiven Bereich: Basis-Emitter-Strecke leitend, Basis-Kollektor-Strecke gesperrt.
(ii) Die Stromverstärkungen sind konstant.
(iii) Die Ströme durch $R_\mathrm{sub}$ und $R_\mathrm{well}$ ändern sich nicht, solange die Basis-Emitter-Spannungen fest bei der Einsatzspannung liegen; ein zusätzlicher Strom fließt deshalb ganz in die Basen.

**Schritt 1**: Ein zusätzlicher Basisstrom $\Delta I$ in den npn erzeugt den Kollektorstrom $B_\mathrm{npn}\Delta I$. Er wird aus der Wanne gezogen und ist damit Basisstrom des pnp.

**Schritt 2**: Der pnp verstärkt ihn um $B_\mathrm{pnp}$; sein Kollektorstrom fließt ins Substrat und kommt als Basisstrom beim npn an:

$$\Delta I_\mathrm{zurück} = B_\mathrm{npn}\,B_\mathrm{pnp}\,\Delta I$$

**Schritt 3** (entscheidender Schritt): Ist der zurückkommende Strom größer als $\Delta I$, wächst er bei jedem Umlauf weiter; ist er kleiner, klingt er ab.

**Ergebnis:**

$$B_\mathrm{npn}\,B_\mathrm{pnp} > 1$$

**Woher die Faktoren kommen:** Jeder Transistor trägt seine Stromverstärkung zur Schleife bei; das Produkt ist die Schleifenverstärkung.

**Proben:** Mit 5 und 50 ist sie 250. Senkt man die Verstärkung des lateralen npn durch größeren Abstand auf 0,01, ist sie 0,5, und kein Störstrom kann den Pfad halten.

**Grenzen:** Die Stromverstärkungen parasitärer Transistoren hängen stark vom Strom ab und sind bei kleinen Strömen kleiner; die Widerstände sind über den Chip verteilt. Wann eine reale Struktur zündet, zeigt deshalb nur die Messung.
:::

::::beispiel Zündstrom und Kurzschlussstrom eines parasitären Thyristors
**Gegeben:** angenommene Werte: $R_\mathrm{sub}$ = 1 kΩ, $R_\mathrm{well}$ = 2 kΩ, $B_\mathrm{npn}$ = 5, $B_\mathrm{pnp}$ = 50, Einsatzspannung 0,6 V, Sättigungsspannung des npn 0,2 V; Versorgung 2,5 V mit 1 Ω Innen- und Leitungswiderstand.

**Gesucht:** die Störströme, die einen bzw. beide Übergänge leitend machen; Strom und Leistung nach dem Zünden.

**Rechnung:** Durch das Substrat bzw. die Wanne:

$$\frac{0{,}6\ \mathrm V}{1\ \mathrm{k\Omega}} = 0{,}6\ \mathrm{mA}, \qquad \frac{0{,}6\ \mathrm V}{2\ \mathrm{k\Omega}} = 0{,}3\ \mathrm{mA}\,$$

Zünden kann der Pfad erst, wenn auch der zweite Übergang leitet: Bei Einspeisung ins Substrat braucht der npn für 0,3 mA Kollektorstrom 0,06 mA Basisstrom zusätzlich, bei Entnahme aus der Wanne der pnp für 0,6 mA Kollektorstrom 0,012 mA:

$$0{,}6\ \mathrm{mA} + \frac{0{,}3\ \mathrm{mA}}{5} = 0{,}66\ \mathrm{mA}, \qquad 0{,}3\ \mathrm{mA} + \frac{0{,}6\ \mathrm{mA}}{50} = 0{,}312\ \mathrm{mA}\,$$

Gezündet liegen über dem Pfad die Emitter-Basis-Spannung des pnp und die Sättigungsspannung des npn, rund 0,8 V:

$$I = \frac{2{,}5\ \mathrm V - 0{,}8\ \mathrm V}{1\ \Omega} = 1{,}7\ \mathrm A, \qquad P = 1{,}7\ \mathrm A\cdot0{,}8\ \mathrm V = 1{,}36\ \mathrm W\,$$

**Ergebnis:** **Ab 0,6 mA ins Substrat oder 0,3 mA aus der Wanne leitet ein Übergang, zünden kann der Pfad ab 0,66 mA bzw. 0,312 mA; danach fließen 1,7 A bei 1,4 W.**

**Einordnung:** Ein Störstrom unter einem Milliampere genügt, und danach fließt das Tausendfache. 1,4 W auf wenigen Quadratmikrometern schmelzen Leiterbahnen und Übergänge. Weil schon rund 1 mA den Pfad erhält und eine Versorgung meist weit mehr liefert, erlischt er praktisch erst beim Abschalten.
::::

:::fehlvorstellung
„Ein Latch-Up ist eine kurze Störung; ist sie vorbei, arbeitet die Schaltung wieder normal.“ Das liegt nahe, weil die meisten Störungen mit ihrer Ursache verschwinden. Beim Latch-Up hält die Mitkopplung den Pfad aber selbst offen, solange die Versorgung mehr als den Haltestrom liefert, im Beispiel rund 1 mA. Erst Abschalten oder ein Versorgungsstrom unter dem Haltestrom beendet den Zustand, wenn er die Schaltung bis dahin nicht zerstört hat.
:::

Ausgelöst wird ein Latch-Up von Strömen, die in Substrat oder Wanne gelangen: beim Einschalten vom Ladestrom der Kapazität zwischen Wannen und Substrat, im Betrieb von Spannungen an Ein- und Ausgängen über der Versorgung oder unter Masse, die die Dioden der Drain-Gebiete leitend machen, von elektrostatischen Entladungen und von ionisierenden Teilchen.

:::frage
„Warum zündet der Thyristor nicht ständig, wenn er doch in jeder CMOS-Schaltung steckt?“
Im Ruhezustand sind alle Übergänge des Pfads gesperrt, und durch Substrat und Wannen fließen nur Leckströme von Picoampere bis Nanoampere; beim Schalten kommen kurze Umladeströme der Sperrschichtkapazitäten hinzu, die bei genügend Kontakten weit unter dem Zündstrom bleiben. Ein Nanoampere erzeugt an 1 kΩ ein Mikrovolt, fast sechs Zehnerpotenzen weniger als die 0,6 V, die einen Übergang leitend machen. Erst ein Störstrom von der Größenordnung eines Milliamperes zündet den Pfad.
:::

## Gegenmaßnahmen gegen Latch-Up

*Wie verhindert man, dass der parasitäre Thyristor zündet?*

Gegen Latch-Up senkt man die Widerstände und die Stromverstärkungen aus Abbildung 6. Viele Substrat- und Wannenkontakte dicht neben den Transistoren senken $R_\mathrm{sub}$ und $R_\mathrm{well}$; Wafer mit einer dünnen, schwach dotierten __Epitaxieschicht__, einer aufgewachsenen Kristallschicht für die Transistoren, auf einem hoch dotierten Substrat senken $R_\mathrm{sub}$ zusätzlich: Soll ein Störstrom von 100 mA nicht zünden, darf der Weg zum Substratkontakt höchstens 6 Ω haben. Ein größerer Abstand zwischen NMOS und Wanne und __Schutzringe__, stark dotierte Ringe an Masse oder Versorgung um die Transistoren, die injizierte Ladungsträger abfangen, senken die Stromverstärkungen; liegt ihr Produkt unter 1, kann sich der Pfad nicht halten. Ganz beseitigt ist die Gefahr nur ohne gemeinsames Substrat, bei Transistoren auf einer isolierenden Oxidschicht (SOI). Welche Abstände und Kontakte nötig sind, schreiben die Entwurfsregeln jedes Prozesses vor.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| PMOS mit negativen Spannungen und negativem Strom | Gebiete und Ladungsträger sind gespiegelt; dem Betrag nach gelten die Gleichungen des NMOS |
| Substrateffekt | der Bulk wirkt als zweites Gate: Sperrspannung verbreitert die Verarmungszone |
| eigene Wanne, Bulk an Source im Gehäuse | ein eigenes, mit der Source verbundenes Gebiet hält die Bulk-Source-Spannung auf null |
| Latch-Up | werden die trennenden Übergänge leitend, bilden Wanne und Substrat einen Thyristor |
| Kontakte, Schutzringe, Epitaxie | sie halten die Übergänge gesperrt: kleine Widerstände, kleine Stromverstärkungen |

Ein MOSFET ist nur durch gesperrte pn-Übergänge von seiner Umgebung getrennt, und sein Bulk wirkt wie ein zweites Gate: Beim PMOS sind Gebiete und Vorzeichen vertauscht, eine Sperrspannung zwischen Bulk und Source vergrößert die Verarmungsladung und damit den Betrag der Schwelle, und werden die trennenden Übergänge leitend, bilden Wanne und Substrat einen Thyristor, der die Versorgung kurzschließt.

## Bedeutung und Ausblick

In CMOS-Gattern verbindet der PMOS mit der Versorgung und der NMOS mit Masse; in analogen Schaltungen bestimmt der Substrateffekt, wie genau Folger, Kaskoden und Stromspiegel arbeiten, und viele Datenblätter nennen die Festigkeit gegen Latch-Up. Der nächste Artikel, Parasitäre Kapazitäten des MOSFET, behandelt die Kapazitäten zwischen den vier Anschlüssen.

**In der ausführlichen Fassung:** die Herleitung des Bulk als zweites Gate mit dem Kapazitätsverhältnis η und der Steigung 1/(1 + η) des Folgers, die Vorspannung des Bulk in Durchlassrichtung, Querschnitte zu gemeinsamen und eigenen Wannen mit tiefer n-Wanne, die Kennlinie des gezündeten Thyristors mit Herleitung des Haltestroms, die Auslöser mit Zahlen, die Temperaturabhängigkeit und die Prüfnorm für Latch-Up ([PMOS-Transistor, Substrateffekt und Latch-Up, ausführlich](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/pmos-substrateffekt-latch-up-ausfuehrlich.html)).

:::kern
- Der PMOS ist das Spiegelbild des NMOS: Löcherkanal in der n-Wanne, $U_{GS}$, $U_{DS}$, $I_D$ und $U_{th,p}$ negativ; dem Betrag nach gelten die NMOS-Gleichungen.
- Das Substrat liegt an der niedrigsten, die Wanne an der höchsten Spannung, damit alle pn-Übergänge sperren.
- Substrateffekt: $U_{th} = U_{th0} + \gamma\big(\sqrt{2\Phi_F - U_{BS}} - \sqrt{2\Phi_F}\big)$; eine Sperrspannung zwischen Bulk und Source hebt die Schwelle.
- Ursache: Die Oberfläche muss um die Sperrspannung höher angehoben werden, und die breitere Verarmungszone bindet mehr Gateladung.
- Vermeiden lässt sich der Substrateffekt nur mit einem eigenen, mit der Source verbundenen Gebiet: eigene Wanne beim PMOS, Bulk an Source beim Einzeltransistor.
- Latch-Up: p⁺–n-Wanne–p-Substrat–n⁺ bildet einen Thyristor aus pnp und npn; er zündet durch einen Störstrom, hält sich bei $B_\mathrm{npn}B_\mathrm{pnp} > 1$ selbst und endet erst, wenn die Versorgung abgeschaltet oder ihr Strom unter den Haltestrom gesenkt wird.
- Gegenmittel: kleine Substrat- und Wannenwiderstände (Kontakte, Epitaxie) und kleine Stromverstärkungen (Abstand, Schutzringe).
:::

:::quiz
F: Warum sind beim PMOS Gate-Source-Spannung, Drain-Source-Spannung und Drainstrom negativ?
A: Die Source ist das p⁺-Gebiet mit dem höheren Potential, weil die Löcher zum niedrigeren laufen; das Gate muss unter der Source liegen, der Drain liegt tiefer, und der Strom fließt aus dem Drain heraus. Mit den Zählpfeilen des NMOS sind deshalb alle drei negativ.
F: Warum hebt eine negative Bulk-Source-Spannung die Schwelle eines NMOS?
A: Die Kanalelektronen liegen auf dem Potential der Source. Liegt diese über dem Bulk, muss die Oberfläche höher angehoben werden, die Verarmungszone wird breiter und enthält mehr feste Ladung, die das Gate tragen muss: bei −1 V 0,268 V mehr Schwelle.
F: Warum hält sich ein Latch-Up selbst, nachdem der Störstrom vorbei ist?
A: Der Kollektorstrom jedes parasitären Transistors ist der Basisstrom des anderen. Ist das Produkt ihrer Stromverstärkungen größer als 1, kommt jeder Strom nach einem Umlauf verstärkt zurück, und der Pfad erhält sich, solange die Versorgung mehr als den Haltestrom liefert.
F: Stimmt es, dass man beim PMOS die negativen Spannungen direkt in die NMOS-Gleichungen einsetzen kann?
A: Nein. Mit $U_{GS}$ = −1 V und der positiven NMOS-Schwelle ergäbe sich „gesperrt“ oder quadriert 2,25 mA; richtig sind im Abschnürbereich −0,25 mA mit der negativen Schwelle oder, dem Betrag nach gerechnet, 0,25 mA.
F: Stimmt es, dass ein Latch-Up endet, sobald die Störung vorbei ist?
A: Nein. Die Mitkopplung hält den Pfad offen, solange rund 1 mA fließen kann; erst das Abschalten der Versorgung oder ein Strom unter dem Haltestrom beendet ihn.
F: Welche Schwelle hat der Beispiel-NMOS, wenn seine Source 1 V über dem Substrat liegt?
A: $0{,}5\ \mathrm V + 0{,}629\ \sqrt{\mathrm V}\cdot(\sqrt{1{,}923\ \mathrm V} - \sqrt{0{,}923\ \mathrm V})$ = 0,768 V.
:::
