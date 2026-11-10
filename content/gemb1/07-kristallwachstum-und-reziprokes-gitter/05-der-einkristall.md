---
title: Stufe 3: Der Einkristall
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Kristallwachstum und reziprokes Gitter
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallwachstum-und-reziprokes-gitter
knoten: Kapitel 7: Kristallwachstum und reziprokes Gitter
order: 4170500
summary: Polysilizium ist rein, aber seine Kristallite zeigen in alle Richtungen.
tags: Czochralski-Verfahren, Impfkristall, Versetzungen, Segregation, Barren, Substrat, Zonenziehen
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Polysilizium ist rein, aber seine Kristallite zeigen in alle Richtungen. Diese Stufe zeigt, wie alle Atome auf ein einziges Gitter kommen.
:::

**Die Idee.** Ordnung lässt sich nicht nachträglich in Kristallite hineinzwingen. Also schmilzt man das Silizium und gibt der Schmelze eine Vorlage, einen kleinen Einkristall. Ein Atom, das an dessen Oberfläche gelangt, findet dort die Plätze des Gitters vor, und auf ihnen ist seine Energie am tiefsten. So setzt jede neue Atomlage das Gitter fort. Der Kristall wächst nur an der Grenzfläche zwischen fest und flüssig. Zieht man die Vorlage langsam nach oben, folgt die Schmelze nach und erstarrt. Dieses Tiegelziehen heißt __Czochralski-Verfahren__.

:::abbildung gemb1/k7ziehen 3
Links: Ziehanlage. Tiegel und Kristall drehen sich gegensinnig. Rechts: Form des Kristalls. Im dünnen Hals laufen die Versetzungen (rot) zum Rand und enden dort.
:::

**Der Ablauf** (Abb. [3](#abb-3)):

<ol>

<li>

⁠**Schmelzen.** Polysilizium kommt in einen Quarztiegel in einem Graphittiegel. Die Heizung hält die Schmelze knapp über dem Schmelzpunkt von 1412 °C, Argon verhindert die Oxidation.

</li>

<li>

⁠**Impfen.** Ein __Impfkristall__ taucht von oben ein. Er legt die Kristallrichtung des ganzen Stücks fest.

</li>

<li>

⁠**Drehen.** Tiegel und Kristall drehen sich entgegengesetzt. Das gleicht Temperatur und Zusammensetzung an der Wachstumsfront aus.

</li>

<li>

⁠**Hals.** Zuerst zieht man schnell. Es entsteht ein dünner Hals von rund 3 mm.

</li>

<li>

⁠**Durchmesser.** Dann zieht man langsamer, typisch 2 bis 250 mm/h, und der Durchmesser wächst bis zum Sollwert. Der Grund: Die Erstarrungswärme muss durch den Kristall abfließen, und langsames Ziehen lässt mehr Silizium erstarren.

</li>

<li>

⁠**Ende.** Zum Schluss zieht man schneller. Der Durchmesser nimmt ab, und der Kristall löst sich ohne Stoß von der Schmelze.

</li>

</ol>

Ein Durchlauf dauert ein bis drei Tage und liefert große Durchmesser kostengünstig.

**Warum der Hals?** Der kalte Impfkristall trifft auf die heiße Schmelze. Die Spannungen erzeugen __Versetzungen__: Linienfehler, längs derer eine Atomebene im Gitter endet. Eine Versetzung kann nur an einer Oberfläche aufhören, und sie läuft schräg zur Ziehrichtung. Im dünnen Hals erreicht sie deshalb nach wenigen Millimetern den Rand. Darunter wächst der Kristall frei von Versetzungen weiter.

**Segregation.** Ein Fremdatom hat eine andere Größe und bildet andere Bindungen. Auf einem Gitterplatz sitzt es deshalb schlechter als in der ungeordneten Schmelze, und an der Grenzfläche bleibt es bevorzugt flüssig. Diese Entmischung heißt __Segregation__. Der Kristall wird reiner als die Schmelze, die Schmelze reichert sich beim Ziehen an. Die Folge ist eine ungleiche Verteilung: Das untere Ende des Kristalls enthält mehr Fremdatome als der Anfang.

**Vom Barren zum Wafer.** Nach dem Ziehen liegt das Silizium als Stab vor, dem __Barren__ (englisch ingot). Sägen und Polieren ergeben flache, sehr glatte, reine Wafer mit 76 bis 300 mm Durchmesser, das Trägermaterial (__Substrat__) der Bauelemente. Jeder Wafer hat die Richtung, die der Impfkristall vorgab, etwa eine $(100)$-Oberfläche.

::::beispiel
Ein Barren mit 300 mm Durchmesser und 2 m Länge wiegt 329 kg. Bei 60 mm/h dauert er 33 h. Die Atomlagen senkrecht zu $[100]$ haben in der Diamantstruktur den Abstand $a/4=0{,}136$ nm. An der Grenzfläche entstehen also $1{,}2\cdot10^{5}$ Lagen je Sekunde.
::::

⁠**Grenzfall:** Wird die Ziehgeschwindigkeit zu groß, kann die Wärme nicht schnell genug abfließen, und der Kristall reißt ab.

:::frage Der Kristall wird beim Ziehen reiner. Wozu dann der Umweg über die Gasphase?
Segregation hilft nur bei Atomen, die das Gitter stark ablehnt. Bor etwa wird fast so gern eingebaut wie Silizium. Außerdem entstünde aus einer Schmelze mit 2 bis 4 % Fremdatomen kein brauchbarer Einkristall.
:::

:::zusatz Zonenziehen
Beim __Zonenziehen__ liegt das Polysilizium als Stab vor. Eine Hochfrequenz-Induktionsspule schmilzt ihn unten auf, und ein einkristalliner Impfling berührt die Schmelze. Unter Rotation wird der Stab durch die Spule nach unten geführt, die Schmelzzone wandert nach oben. Unterhalb der Spule erstarrt die Schmelze zum Einkristall mit der Richtung des Impflings. Das dauert 10 bis 15 Stunden, der Durchsatz ist höher als beim Tiegelziehen. Kein Tiegel verunreinigt das Silizium, es entstehen hochreine Wafer. Der Prozess ist aber deutlich teurer.
:::

:::aufgabe Aufgabe 3 ★★ Ein Barren entsteht
<span class="anker" id="aufg-3"></span>

Ein Barren hat 300 mm Durchmesser und 1,8 m Länge und wird mit 60 mm/h gezogen.

<ol class="al">

<li>

Berechne Masse und Ziehdauer. Passt das zu „ein bis drei Tage“?

</li>

<li>

Wie viele $(100)$-Atomlagen wachsen je Sekunde? Wie viele bei 2 mm/h?

</li>

<li>

Jeder Wafer ist 775 µm dick, die Säge frisst je Schnitt 200 µm. Wie viele Wafer entstehen?

</li>

<li>

Versetzungen laufen in $\{111\}$-Ebenen. Unter welchem Winkel zur Ziehachse $[100]$ läuft die steilste Linie einer solchen Ebene (Winkel aus [Kapitel 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html))? Wie lang muss ein Hals von 3 mm mindestens sein, damit eine Versetzung vom einen Rand zum anderen läuft? Wie lang wäre das bei 300 mm?

</li>

</ol>

:::loesung
(a) $V=\pi(15\,\mathrm{cm})^2\cdot180\,\mathrm{cm}=1{,}27\cdot10^5\,\mathrm{cm^3}$, also 296 kg. Dauer $1800\,\mathrm{mm}/(60\,\mathrm{mm/h})=30$ h, 1,25 Tage. Das passt. (b) $1{,}67\cdot10^{-5}\,\mathrm{m/s}$ geteilt durch 0,136 nm ergibt $1{,}23\cdot10^5$ Lagen je Sekunde, bei 2 mm/h noch $4{,}1\cdot10^3$. (c) $1{,}8\,\mathrm{m}/(975\cdot10^{-6}\,\mathrm{m})=1846$ Wafer. (d) Die Normale von $(111)$ schließt mit $[100]$ den Winkel 54,7° ein, zwischen Achse und Ebene liegen also 35,3°. Die Länge ist $3\,\mathrm{mm}/\tan35{,}3^\circ=4{,}2$ mm. Bei 300 mm wären es 424 mm: Ohne Hals bliebe ein großer Teil des Kristalls voller Versetzungen.
:::
:::

:::aufgabe Aufgabe 4 ★★★ Die Schmelze reichert sich an
<span class="anker" id="aufg-4"></span>

An der Grenzfläche gilt $c_\mathrm{fest}=K\,c_\mathrm{fl}$ mit dem Verteilungskoeffizienten $K<1$. $c$ ist die Fremdstoffmasse je Masse Silizium. Die Schmelze ist gut durchmischt und hat anfangs die Masse $M_0$ und die Konzentration $c_0$. $f$ ist der erstarrte Anteil.

<ol class="al">

<li>

Erstarrt die Masse $|\mathrm{d} M|$, verlässt $K\,c_\mathrm{fl}\,|\mathrm{d} M|$ Fremdstoff die Schmelze. Stelle die Differentialgleichung für die Fremdstoffmasse auf und zeige $c_\mathrm{fl}=c_0(1-f)^{K-1}$.

</li>

<li>

Berechne $c_\mathrm{fest}/c_0$ für $K=0{,}01$ bei $f=0$, $0{,}5$ und $0{,}9$.

</li>

<li>

Grenzfall: Was ergibt $K=1$? Was bedeutet das Ergebnis aus (b) für das Ende des Barrens?

</li>

</ol>

:::loesung
(a) Für die Fremdstoffmasse $F$ in der Schmelze der Masse $M$ gilt $c_\mathrm{fl}=F/M$ und, weil beide abnehmen, $\mathrm{d} F=K\,(F/M)\,\mathrm{d} M$. Trennung der Variablen ergibt $\ln(F/F_0)=K\ln(M/M_0)$, also $F=F_0(M/M_0)^K$. Mit $M/M_0=1-f$ folgt $c_\mathrm{fl}=F/M=c_0(1-f)^{K-1}$. (b) $c_\mathrm{fest}/c_0=K(1-f)^{K-1}$ ergibt 0,0100, 0,0199 und 0,0977. (c) $K=1$ ergibt $c_\mathrm{fl}=c_0$, keine Trennung. Für $K\ll1$ bleibt der Kristall lange rein, die Konzentration steigt aber zum Ende hin steil: Bei $f=0{,}9$ ist sie zehnmal so hoch wie am Anfang. Das Ende wird deshalb nicht verwendet.
:::
:::
