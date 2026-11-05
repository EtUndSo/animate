---
title: Risiko, Angreifermodell und Angriffsfläche
pfad: Informatik / Cybersecurity / Sicherheit, Schutzziele und Spielregeln
order: 6110400
summary: Kein System ist gegen alles geschützt, und vollständiger Schutz wäre unbezahlbar.
tags: Eintrittshäufigkeit, Summenzeichen, Erwartungswert, unabhängig, Produktregel, Risiko, Risikomatrix, Gesamtrisiko
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Kein System ist gegen alles geschützt, und vollständiger Schutz wäre unbezahlbar. Dieser Abschnitt misst, wie groß eine Gefahr ist und wie groß alle zusammen sind, entscheidet, wann sich eine Schutzmaßnahme lohnt, legt fest, gegen wen man sich schützt, und zählt die Stellen, an denen ein Angreifer ansetzen kann.
:::

### Was du dafür brauchst: Häufigkeit und Erwartungswert

<span class="anker" id="stufe-3-1"></span>

Um Gefahren zu vergleichen, braucht man zwei Zahlen: wie oft etwas passiert und was es dann kostet.

**Häufigkeit.** Die __Eintrittshäufigkeit__ $H$ eines Ereignisses gibt an, wie oft es im Mittel pro Jahr eintritt; ihre Einheit ist $1/\text{Jahr}$. Für seltene Ereignisse ist $H$ kleiner als eins: „einmal in zehn Jahren“ heißt $H=0{,}1/\text{Jahr}$.

**Summenzeichen.** Für die Summe vieler Zahlen $a_1,a_2,\dots,a_n$ schreibt man kurz

$$\sum_{t=1}^{n}a_t=a_1+a_2+\dots+a_n .$$

Das große griechische Sigma heißt __Summenzeichen__. Der Buchstabe $t$ darunter zählt die Summanden durch, von $1$ bis $n$; wie man ihn nennt, ändert die Summe nicht.

**Erwartungswert des Schadens.** Kostet jedes Eintreten den Schaden $S$, so tritt das Ereignis in $T$ Jahren im Mittel $H\cdot T$-mal ein und kostet zusammen $H\cdot T\cdot S$. Pro Jahr sind das im Mittel

<span class="anker" id="gl-3-1"></span>
$$\frac{H\cdot T\cdot S}{T}=H\cdot S . \tag{3.1}$$

Dieser Mittelwert heißt der __Erwartungswert__ des jährlichen Schadens.

Man kann ihn auch Jahr für Jahr nachzählen. Ist $D_t$ der Schaden, der im Jahr $t$ tatsächlich entstanden ist, so ist der mittlere Schaden über $T$ Jahre

$$\frac1T\sum_{t=1}^{T}D_t .$$

Über viele Jahre liegt dieser Mittelwert nahe am Erwartungswert $H\cdot S$; das meint das Wort „im Mittel“.

⁠**Rechenbeispiele:** Ein Fahrradschlauch platzt dreimal im Jahr, jeder neue kostet 15 €: Der Erwartungswert ist $45$ € pro Jahr. Ein Wasserschaden tritt einmal in 20 Jahren auf und kostet 10 000 €: Der Erwartungswert ist $500$ € pro Jahr. Tritt der Schaden in 20 Jahren genau einmal ein, so ist in 19 Jahren $D_t=0$ und in einem Jahr $D_t=10\,000$ €, und der Mittelwert über die 20 Jahre ist ebenfalls $500$ € pro Jahr (Abb. [3](#abb-3)).

:::abbildung cyber/k1rerwartung 3
Zwei Erwartungswerte des jährlichen Schadens in Euro pro Jahr: oben der Fahrradschlauch, darunter der Wasserschaden. Die letzten beiden Zeilen zählen den Wasserschaden Jahr für Jahr nach: 19 Jahre ohne Schaden, ein Jahr mit 10 000 €, im Mittel ebenfalls 500 € pro Jahr.
:::

Der Erwartungswert sagt nichts darüber, was in einem bestimmten Jahr passiert. Der Wasserschaden kostet in 19 von 20 Jahren nichts und in einem Jahr 10 000 €; 500 € kostet er in keinem einzigen Jahr.

⁠**Kurz gesagt:** Tritt ein Ereignis im Mittel $H$-mal pro Jahr ein und kostet jedes Mal $S$, so kostet es im Mittel $H\cdot S$ pro Jahr.

### Was du dafür brauchst: unabhängige Ereignisse

<span class="anker" id="stufe-3-2"></span>

Mehrere Schutzmaßnahmen oder mehrere Schwachstellen wirken zusammen. Um das zu rechnen, braucht man eine Regel der Wahrscheinlichkeitsrechnung.

Eine Wahrscheinlichkeit $p$ ist eine Zahl zwischen 0 (tritt nie ein) und 1 (tritt sicher ein). Zwei Ereignisse heißen __unabhängig__, wenn das Eintreten des einen nichts an der Wahrscheinlichkeit des anderen ändert. Dann gilt die __Produktregel__: Die Wahrscheinlichkeit, dass beide eintreten, ist das Produkt der einzelnen Wahrscheinlichkeiten,

<span class="anker" id="gl-3-2"></span>
$$P(\text{A und B})=p_\mathrm A\cdot p_\mathrm B . \tag{3.2}$$

Daraus folgt eine zweite Regel. Die Wahrscheinlichkeit, dass ein Ereignis *nicht* eintritt, ist $1-p$. Bei $n$ unabhängigen Ereignissen mit derselben Wahrscheinlichkeit $p$ tritt mit der Wahrscheinlichkeit $(1-p)^n$ keines ein, und folglich mit

<span class="anker" id="gl-3-3"></span>
$$P(\text{mindestens eines})=1-(1-p)^n \tag{3.3}$$

mindestens eines. Ist $n\cdot p$ klein gegen 1, so ist das ungefähr $n\cdot p$.

⁠**Rechenbeispiel:** Ein Würfel zeigt eine Sechs mit der Wahrscheinlichkeit $p=\frac16$. Zwei Würfel zeigen beide eine Sechs mit der Wahrscheinlichkeit $p\cdot p=\frac1{36}$. Bei vier Würfen eines Würfels kommt mit der Wahrscheinlichkeit $(1-p)^4\approx0{,}482$ keine Sechs, also mit $1-(1-p)^4\approx0{,}518$ mindestens eine (Abb. [4](#abb-4)).

:::abbildung cyber/k1rwuerfel 4
Würfeln mit der Produktregel, $p=\frac16$: oben zwei Sechsen mit zwei Würfeln, in der Mitte keine Sechs in vier Würfen als Produkt aus vier gleichen Faktoren, unten das Gegenereignis, mindestens eine Sechs.
:::

Unabhängigkeit ist eine Annahme, die man prüfen muss. Zwei Dinge, die eine gemeinsame Ursache haben, sind nicht unabhängig: Ob es heute in Köln und in Bonn regnet, hängt vom selben Wetter ab.

⁠**Kurz gesagt:** Bei unabhängigen Ereignissen multiplizieren sich die Wahrscheinlichkeiten; mindestens eines von $n$ tritt mit $1-(1-p)^n$ ein.

:::hintergrund Warum $n\cdot p$ die Wahrscheinlichkeit nie unterschätzt
Die Näherung $n\cdot p$ ist nicht nur für kleine $n\cdot p$ brauchbar, sie ist immer eine obere Schranke: $1-(1-p)^n\le n\cdot p$. Der Grund ist ein Zählfehler mit festem Vorzeichen. Wer die Wahrscheinlichkeiten der $n$ einzelnen Ereignisse addiert, zählt jeden Fall, in dem zwei oder mehr Ereignisse zugleich eintreten, mehrfach. Die Summe ist deshalb nie kleiner als die Wahrscheinlichkeit, dass mindestens eines eintritt. Beim Würfeln ist $4\cdot\frac16\approx0{,}667$, gegenüber dem richtigen Wert $0{,}518$; die Differenz sind die mehrfach gezählten Würfe mit zwei, drei oder vier Sechsen. Ist $n\cdot p$ klein, sind solche Fälle selten, und die Schranke liegt dicht am richtigen Wert.

Für diese Schranke braucht man die Unabhängigkeit nicht einmal. Sie gilt für beliebige Ereignisse und heißt in der Wahrscheinlichkeitsrechnung Boolesche Ungleichung: Die Wahrscheinlichkeit, dass mindestens eines eintritt, ist höchstens die Summe der einzelnen Wahrscheinlichkeiten. Die genaue Formel $1-(1-p)^n$ dagegen setzt Unabhängigkeit voraus.
:::

### Risiko

<span class="anker" id="stufe-3-3"></span>

Ein Ereignis kann selten und teuer sein, ein anderes häufig und billig. Welches ist gefährlicher? Um das zu entscheiden, braucht man eine Größe, die beides zusammenfasst.

:::definition Definition 3.1 (Risiko)
<span class="anker" id="satz-3-1"></span>

Das __Risiko__ eines schädlichen Ereignisses ist die Verbindung aus der Wahrscheinlichkeit, mit der es eintritt, und dem Schaden, den es dann anrichtet. Kann man beides in Zahlen angeben, so misst man es als erwarteten Schaden pro Jahr:

<span class="anker" id="gl-3-4"></span>
$$R=H\cdot S , \tag{3.4}$$

mit der Eintrittshäufigkeit $H$ in $1/\text{Jahr}$, dem Schaden $S$ je Ereignis in Euro und dem Risiko $R$ in Euro pro Jahr.
:::

⁠**Rechenbeispiel:** Ein kleines Unternehmen betrachtet zwei Ereignisse.

<ul>

<li>

A: ein Einbruch in das Firmennetz, im Mittel einmal in zehn Jahren, also $H_\mathrm A=0{,}1/\text{Jahr}$, Schaden $S_\mathrm A=50\,000$ €.

</li>

<li>

B: ein gestohlenes Kundenkonto, das zurückgesetzt und dessen Kunde entschädigt werden muss, im Mittel zehnmal im Jahr, also $H_\mathrm B=10/\text{Jahr}$, Schaden je $S_\mathrm B=100$ €.

</li>

</ul>

Die Risiken sind $R_\mathrm A=5\,000$ €/Jahr und $R_\mathrm B=1\,000$ €/Jahr (Abb. [5](#abb-5)). Das seltene Ereignis A ist hier fünfmal so riskant wie das häufige Ereignis B.

:::abbildung cyber/k1rrisiko 5
Die Risiken der Ereignisse A und B in Euro pro Jahr: Eintrittshäufigkeit pro Jahr mal Schaden je Ereignis.
:::

Abbildung [6](#abb-6) zeigt das als Landkarte. Häufigkeit und Schaden sind dort logarithmisch aufgetragen, jeder Teilstrich ist eine Zehnerpotenz. Auf einer solchen Karte liegen alle Ereignisse mit demselben Produkt $H\cdot S$ auf einer schrägen Geraden: Wird $H$ zehnmal so groß und $S$ zehnmal so klein, bleibt das Risiko gleich. Ein Ereignis, das hundertmal im Jahr eintritt und jedes Mal 50 € kostet, liegt auf derselben Geraden wie A.

:::abbildung cyber/k1risiko 6
Häufigkeit und Schaden auf logarithmischen Achsen. A: einmal in zehn Jahren 50 000 €. B: zehnmal im Jahr 100 €. Auf jeder gestrichelten Linie ist das Produkt $H\cdot S$ gleich, also auch das Risiko: Die rote Linie verbindet alle Ereignisse mit dem Risiko von A, die blaue alle mit dem Risiko von B. Nach rechts oben steigt das Risiko.
:::

Oft kennt man $H$ und $S$ nur grob. Dann teilt man beide in wenige Stufen ein, etwa „selten, gelegentlich, häufig“ und „gering, mittel, hoch“, und liest das Risiko aus einer Tabelle ab. Eine solche Tabelle heißt __Risikomatrix__. Sie ist die vergröberte Form der Landkarte in Abbildung [6](#abb-6).

⁠**Kurz gesagt:** Risiko ist Häufigkeit mal Schaden, gemessen als erwarteter Schaden pro Jahr.

:::hintergrund Was die Formel nicht erfasst
Die Formel $R=H\cdot S$ ist ein Werkzeug zum Vergleichen, keine Wahrheit. Drei Einschränkungen muss man kennen.

⁠**Die Zahlen sind Schätzungen.** Wie oft ein Angriff gelingt, weiß niemand genau; Abweichungen um den Faktor zehn sind normal. Deshalb sind die Achsen in Abbildung [6](#abb-6) logarithmisch: Es kommt auf die Größenordnung an, nicht auf die zweite Stelle.

⁠**Gleiches Risiko heißt nicht gleich gefährlich.** Ein Ereignis mit $H=0{,}001/\text{Jahr}$ und $S=5$ Millionen € hat dasselbe Risiko wie eines mit $H=5/\text{Jahr}$ und $S=1\,000$ €, nämlich 5 000 € pro Jahr. Für ein Unternehmen mit einer Million Euro Rücklagen ist das erste trotzdem viel schlimmer, denn wenn es eintritt, ist das Unternehmen am Ende; einen Mittelwert über tausend Jahre erlebt es nicht. Für solche Ereignisse, deren Schaden die eigene Existenz bedroht, schließt man Versicherungen ab, auch wenn die Prämie höher ist als der Erwartungswert.

⁠**Das Risiko ändert sich, ohne dass man etwas tut.** Ein Mitarbeiter schließt einen eigenen Funkzugang an das Firmennetz an, eine neue Schwachstelle wird bekannt, eine Tätergruppe entdeckt die Branche als Ziel: Jedes Mal verschiebt sich $H$, obwohl am eigenen System nichts geändert wurde. Eine Risikoabschätzung muss deshalb regelmäßig wiederholt werden.
:::

### Das Gesamtrisiko

<span class="anker" id="stufe-3-4"></span>

Ein Unternehmen fürchtet nicht nur ein einziges schädliches Ereignis, sondern viele. Wie viel erwarteter Schaden kommt insgesamt in einem Jahr zusammen?

Man kann sich jedes Risiko wie eine laufende Rechnung vorstellen, die im Mittel jedes Jahr fällig wird. Die laufenden Rechnungen eines Haushalts addieren sich zu seinen jährlichen Gesamtkosten; genauso addieren sich die Risiken.

:::definition Definition 3.2 (Gesamtrisiko)
<span class="anker" id="satz-3-2"></span>

Hat ein System die schädlichen Ereignisse $k=1,\dots,m$ mit den Eintrittshäufigkeiten $H_k$, den Schäden $S_k$ und den Risiken $R_k=H_k\cdot S_k$, so ist sein __Gesamtrisiko__

<span class="anker" id="gl-3-5"></span>
$$R_\Sigma=\sum_{k=1}^{m}R_k=\sum_{k=1}^{m}H_k\cdot S_k , \tag{3.5}$$

gemessen wie jedes Risiko in Euro pro Jahr.
:::

⁠**Rechenbeispiel:** Das Unternehmen aus dem letzten Unterabschnitt hat mit den Ereignissen A und B das Gesamtrisiko $R_\Sigma=6\,000$ €/Jahr (Abb. [7](#abb-7)). Fünf Sechstel davon stammen aus dem seltenen Ereignis A.

:::abbildung cyber/k1rgesamt 7
Das Gesamtrisiko der Ereignisse A und B in Euro pro Jahr: jedes Risiko als Produkt aus Häufigkeit und Schaden, dann die Summe.
:::

⁠**Kurz gesagt:** Das Gesamtrisiko ist die Summe der einzelnen Risiken, $R_\Sigma=\sum_kH_k\,S_k$.

:::hintergrund Warum man Risiken einfach addieren darf, auch wenn die Ereignisse zusammenhängen
Der Schaden eines Jahres ist die Summe der Schäden, die die einzelnen Ereignisse in diesem Jahr anrichten: $D_t=D_{t,1}+\dots+D_{t,m}$, wobei $D_{t,k}$ der Schaden durch Ereignis $k$ im Jahr $t$ ist. Mittelt man über $T$ Jahre, so darf man die Reihenfolge der beiden Summen vertauschen:

$$\frac1T\sum_{t=1}^{T}\sum_{k=1}^{m}D_{t,k}=\sum_{k=1}^{m}\frac1T\sum_{t=1}^{T}D_{t,k} .$$

Links steht der mittlere Gesamtschaden, rechts die Summe der mittleren Einzelschäden, also auf lange Sicht die Summe der Risiken. Diese Umordnung gilt immer, gleichgültig, ob die Ereignisse unabhängig sind oder einander auslösen. Auch wenn ein übernommenes E-Mail-Konto den Weg für eine Erpressungssoftware bereitet, bleibt das Gesamtrisiko die Summe der beiden Risiken.

Was die Summe nicht zeigt, ist die Schwankung. Hängen Ereignisse zusammen, so treffen sie oft im selben Jahr ein, und ein schlechtes Jahr wird viel schlechter als der Durchschnitt. Für die Frage, ob ein Unternehmen ein schlechtes Jahr übersteht, genügt das Gesamtrisiko deshalb nicht; dafür braucht man wieder die einzelnen Schäden, wie im Kasten „Was die Formel nicht erfasst“.
:::

### Sicherheit ist Ökonomie

<span class="anker" id="stufe-3-5"></span>

Niemand kauft für ein Fahrrad für 100 € ein Schloss für 300 €. Schutz kostet Geld, Zeit und Bequemlichkeit, und er ist nur so viel wert wie der Schaden, den er verhindert.

:::definition Definition 3.3 (Nutzen einer Schutzmaßnahme)
<span class="anker" id="satz-3-3"></span>

Eine Schutzmaßnahme koste pro Jahr $K$ und senke das Risiko von $R_\text{vorher}$ auf $R_\text{nachher}$. Ihr __Nettonutzen__ ist

<span class="anker" id="gl-3-6"></span>
$$N=R_\text{vorher}-R_\text{nachher}-K . \tag{3.6}$$

Die Maßnahme lohnt sich, wenn $N>0$ ist, wenn sie also mehr erwarteten Schaden verhindert, als sie kostet.
:::

Der Grundsatz dahinter heißt __Sicherheit ist Ökonomie__: Wie viel Schutz angemessen ist, entscheidet der Vergleich von Aufwand und verhindertem Schaden, nicht der Wunsch nach vollkommener Sicherheit. Derselbe Grundsatz gilt für den Angreifer: Ein Angriff, der mehr kostet, als er einbringt, lohnt sich für einen Angreifer, der auf Gewinn aus ist, nicht. Und weil Angreifer den Weg des geringsten Widerstands gehen, ist ein System nur so stark wie seine schwächste Stelle.

⁠**Rechenbeispiel:** Eine Maßnahme kostet $K=2\,000$ € pro Jahr. Für die Ereignisse A und B aus Unterabschnitt [3.3](#stufe-3-3) gilt (Abb. [8](#abb-8)):

<ul>

<li>

Gegen A: Verhindert sie 80 % der Einbrüche, sinkt $R_\mathrm A$ von 5 000 auf 1 000 €/Jahr, und der Nettonutzen ist $+2\,000$ €/Jahr. Sie lohnt sich. Verhindert sie nur 30 %, sinkt $R_\mathrm A$ nur auf 3 500 €/Jahr, und der Nettonutzen ist $-500$ €/Jahr; dann lohnt sie sich nicht. Die Schwelle liegt dort, wo der verhinderte Anteil des Risikos gerade die Kosten deckt, bei $2\,000/5\,000=40\,\%$.

</li>

<li>

Gegen B: Selbst wenn sie jeden Fall verhindert, spart sie höchstens $R_\mathrm B=1\,000$ €/Jahr, also ist $N\le1\,000-2\,000=-1\,000$ €/Jahr. Gegen B lohnt sie sich nie.

</li>

</ul>

:::abbildung cyber/k1rnutzen 8
Der Nettonutzen $N=R_\text{vorher}-R_\text{nachher}-K$ der Maßnahme gegen Ereignis A in Euro pro Jahr, wenn sie 80 % oder 30 % der Einbrüche verhindert. Unten die Schwelle: Die Maßnahme muss mindestens den Anteil $K/R_\mathrm A$ des Risikos verhindern.
:::

⁠**Kurz gesagt:** Eine Schutzmaßnahme lohnt sich, wenn sie mehr erwarteten Schaden verhindert, als sie kostet.

:::hintergrund Wie viel man höchstens ausgeben sollte
Wirtschaftswissenschaftler haben die Frage, wie viel ein Unternehmen in Sicherheit stecken sollte, mit einem einfachen Modell untersucht, dem *Gordon-Loeb-Modell*. Darin hat ein Schutzgut den Wert $L$, und ohne Schutz kommt es mit der Wahrscheinlichkeit $v$ zu einem Schaden; der erwartete Verlust ist $v\cdot L$. Jeder investierte Euro senkt $v$, aber mit abnehmender Wirkung: Die ersten Euro schließen die gröbsten Lücken, die späteren immer kleinere.

Unter dieser Annahme liegt die beste Investition dort, wo der letzte Euro gerade noch einen Euro an erwartetem Verlust verhindert. Für zwei breite Klassen solcher Modelle zeigten Gordon und Loeb, dass diese beste Investition nie mehr als den Bruchteil $1/\mathrm{e}\approx37\,\%$ des erwarteten Verlusts $v\cdot L$ beträgt. Bei einem erwarteten Verlust von 120 000 € pro Jahr wären das höchstens etwa 44 000 € pro Jahr.

Zwei Dinge sind an diesem Ergebnis lehrreich. Erstens: Es ist fast nie sinnvoll, den erwarteten Verlust vollständig wegzukaufen; die letzten Prozent werden zu teuer. Zweitens: Die beste Investition wächst nicht immer mit der Verwundbarkeit. Ein extrem verwundbares System kann so teuer zu schützen sein, dass sich das Geld anderswo mehr lohnt. Die 37 % sind keine Faustregel für jeden Fall; für andere Formen der Kurve gibt es Gegenbeispiele mit höheren Werten. Der Gedanke dahinter gilt aber allgemein: Man investiert so lange, wie der nächste Euro mehr Schaden verhindert, als er kostet.
:::

### Angreifermodell

<span class="anker" id="stufe-3-6"></span>

Ist ein Fahrradschloss sicher? Gegen einen Gelegenheitsdieb, der ohne Werkzeug vorbeikommt, ja. Gegen jemanden mit einem Winkelschleifer und zwei Minuten Zeit, nein. Die Frage lässt sich erst beantworten, wenn man sagt, gegen wen.

:::definition Definition 3.4 (Angreifermodell)
<span class="anker" id="satz-3-4"></span>

Ein __Angreifermodell__ (englisch *threat model*) beschreibt die Angreifer, gegen die ein System geschützt sein soll. Es legt fest,

<ul>

<li>

was sie wollen: ihr Ziel und ihren Antrieb, etwa Geld, Neugier, Spionage, politische Botschaften oder Sabotage;

</li>

<li>

was sie können: ihr Wissen, ihr Geld, ihre Zeit und ihre Werkzeuge;

</li>

<li>

wo sie ansetzen können: aus der Ferne über das Internet, im selben Netz, mit den Händen am Gerät oder als Mitglied der eigenen Organisation.

</li>

</ul>
:::

Ein Angreifer, der selbst zur angegriffenen Organisation gehört, heißt __Innentäter__. Er ist besonders gefährlich, weil er schon Berechtigungen hat und das System kennt.

Ein System ist immer nur *gegenüber einem Angreifermodell* sicher. Bei der Wahl des Modells ist man vorsichtig und nimmt eher zu viel als zu wenig an: dass Angreifer unbemerkt handeln können, dass sie das System genau studieren und dass sie es immer wieder versuchen.

⁠**Beispiel:** Für eine private Notizen-App auf dem Handy ist ein vernünftiges Angreifermodell: ein Dieb, der das Handy stiehlt, keine besonderen Mittel hat und das Gerät weiterverkaufen will. Eine Bildschirmsperre und ein verschlüsselter Speicher genügen dagegen. Für die Steuerung eines Stromnetzes sieht das Modell anders aus: staatliche Gruppen mit großem Budget, monatelanger Geduld und vielleicht einem Innentäter. Dagegen genügt das nicht annähernd.

⁠**Kurz gesagt:** Ein Angreifermodell legt fest, gegen wen ein System schützen soll; erst damit lässt sich sagen, ob ein Schutz genügt.

:::hintergrund Warum Sicherheit immer relativ zu einem Angreifermodell ist
Die meisten Anforderungen an ein System sind *positive* Ziele: „Die Kontoinhaberin kann ihren Kontostand sehen.“ Ob das erfüllt ist, zeigt man, indem man es einmal vorführt. Sicherheit dagegen ist ein *negatives* Ziel: „Kein Unbefugter kann den Kontostand sehen.“ Um das zu zeigen, müsste man beweisen, dass es *keinen* Weg gibt, und zwar keinen einzigen unter allen denkbaren Wegen.

Die Menge aller denkbaren Wege ist aber unbegrenzt, solange man nichts über den Angreifer annimmt. Darf er das Gebäude betreten? Kann er einen Mitarbeiter bestechen? Hat er die Rechenleistung eines Staates? Ohne Antwort auf solche Fragen lässt sich nicht einmal sagen, welche Wege man prüfen muss. Das Angreifermodell begrenzt die Wege auf eine Menge, über die man nachdenken kann. Erst dann wird „sicher“ eine prüfbare Aussage: sicher gegen *diese* Angreifer.

Daraus folgt auch, woran viele Systeme scheitern. Selten ist ein Mechanismus falsch gebaut; viel öfter war das Angreifermodell zu eng. Der Entwickler hielt einen Weg für unmöglich, den ein Angreifer dann doch gegangen ist, zum Beispiel weil Rechenleistung billiger wurde oder weil jemand den Lieferanten angegriffen hat statt das Unternehmen. Und es folgt, warum absolute Sicherheit nicht erreichbar ist: Ein System, das gegen jeden denkbaren Angreifer geschützt wäre, könnte niemand mehr zu vertretbaren Kosten bauen und benutzen.
:::

:::hintergrund Wer in Deutschland tatsächlich angreift
Das BSI beschreibt in seinem jährlichen Lagebericht, mit welchen Angreifern man in Deutschland rechnen muss. Für den Zeitraum von Mitte 2024 bis Mitte 2025 nennt es vier Gruppen.

<ul>

<li>

⁠*Kriminelle*, die mit Erpressungssoftware und gestohlenen Daten Geld verdienen. Sie sind die größte Bedrohung. Viele kaufen ihre Werkzeuge als fertige Dienstleistung bei anderen Kriminellen ein; man braucht dafür kaum noch eigenes Können.

</li>

<li>

⁠*Staatlich gesteuerte Gruppen*, die vor allem spionieren. Deutschland steht bei ihnen auf Platz vier der Zielländer; Hauptziel ist die öffentliche Verwaltung.

</li>

<li>

⁠*Politisch motivierte Gruppen*, die Webseiten mit Anfragen überlasten, um Aufmerksamkeit zu erzeugen.

</li>

<li>

⁠*Innentäter*.

</li>

</ul>

Rund 80 % der angezeigten Angriffe trafen kleine und mittlere Unternehmen. Die Zahl der beobachteten Versuche, bekannte Schwachstellen auszunutzen, stieg um 38 %, und weltweit entstanden jeden Tag über 800 neue Adressen für Phishing-Seiten. Manche billigen vernetzten Geräte kamen sogar schon ab Werk mit Schadsoftware zu ihren Käufern; allein bei einer solchen Gerätefamilie hat das BSI für rund 30 000 Geräte in Deutschland die Verbindung zu den Tätern blockiert oder die Besitzer gewarnt. Der Trend geht zu vielen kleinen, einfachen Angriffen, die automatisiert gegen alles laufen, was erreichbar ist. Für ein Angreifermodell heißt das: Auch wer sich für kein lohnendes Ziel hält, wird angegriffen, weil das Suchprogramm nicht danach fragt.
:::

### Angriffsfläche

<span class="anker" id="stufe-3-7"></span>

Ein Haus kann man durch die Tür betreten, aber auch durch jedes Fenster, über den Kellerabgang, den Balkon, durch den Briefschlitz oder mit dem Schlüssel des Handwerkers. Jede dieser Stellen ist eine Gelegenheit.

:::definition Definition 3.5 (Angriffsfläche)
<span class="anker" id="satz-3-5"></span>

Die __Angriffsfläche__ eines Systems ist die Gesamtheit der Stellen, an denen ein Angreifer mit dem System in Berührung kommen kann: Eingaben, die das System annimmt, über ein Netz erreichbare Dienste, Anschlüsse und Schnittstellen am Gerät, die Menschen, die es bedienen, und die Lieferanten seiner Teile.
:::

Je größer die Angriffsfläche, desto mehr Gelegenheiten hat ein Angreifer.

Das lässt sich rechnen. Ein System habe $n$ Stellen, an denen ein Angreifer ansetzen kann, und an jeder stecke unabhängig von den anderen mit der Wahrscheinlichkeit $p$ eine Schwachstelle. Nach [(3.3)](#gl-3-3) hat das System dann mit der Wahrscheinlichkeit

<span class="anker" id="gl-3-7"></span>
$$P=1-(1-p)^n \tag{3.7}$$

mindestens eine Schwachstelle.

⁠**Rechenbeispiel:** Ein vernetztes Gerät bietet $n=10$ Dienste an, und jeder enthält mit $p=2\,\%$ eine ausnutzbare Schwachstelle. Dann ist $P_{10}=0{,}183$ (Abb. [9](#abb-9)): In fast jedem fünften Fall hat das Gerät eine offene Stelle. Schaltet der Hersteller die sieben Dienste ab, die kaum jemand braucht, bleiben $n=3$ und $P_3=0{,}059$. Die Angriffsfläche ist kleiner, und die Wahrscheinlichkeit einer offenen Stelle sinkt auf ein Drittel, ohne dass ein einziger Dienst besser programmiert wurde.

:::abbildung cyber/k1rflaeche 9
Die Wahrscheinlichkeit, dass mindestens eine von $n$ Stellen eine Schwachstelle hat, für $p=0{,}02$: oben mit $n=10$ Diensten, unten mit $n=3$. Das Produkt der Faktoren $1-p=0{,}98$ ist die Wahrscheinlichkeit, dass keine Stelle eine hat.
:::

⁠**Kurz gesagt:** Die Angriffsfläche ist die Menge der Stellen, an denen ein Angreifer ansetzen kann; jede Stelle, die man abschafft, ist eine Gelegenheit weniger.

:::hintergrund Der Angreifer braucht eine Lücke, der Verteidiger muss alle schließen
Formel [(3.7)](#gl-3-7) zeigt eine grundsätzliche Ungleichheit zwischen den beiden Seiten. Der Angreifer gewinnt, sobald er *eine* Schwachstelle findet; der Verteidiger hat nur gewonnen, wenn *keine* der $n$ Stellen eine hat. Wächst $n$, so geht $(1-p)^n$ gegen null, und die Wahrscheinlichkeit, dass irgendwo eine Lücke steckt, gegen eins, selbst wenn jede einzelne Stelle sorgfältig gebaut ist.

Daraus folgt die wirksamste und oft billigste Schutzmaßnahme: Stellen, die man nicht braucht, gar nicht erst anbieten. Ein abgeschalteter Dienst hat keine Schwachstellen mehr. Das BSI nennt „Angriffsflächen schützen!“ in seinem Lagebericht als größten Hebel für das Jahr 2026.

Die Ungleichheit hat eine Grenze: Der Verteidiger muss nicht jede Lücke schließen, er muss sie nur für den Angreifer teurer machen, als sie ihm nützt. Das ist der Grundsatz „Sicherheit ist Ökonomie“ von der Seite des Angreifers aus.
:::

:::hintergrund Andere Wörter für dieselbe Kette
Die Begriffe dieses Kapitels sind in der Fachliteratur nicht einheitlich. Das BSI beschreibt die Kette in seinem Lagebericht so: Eine Schwäche (bei ihm „Angriffsfläche“) wird von einem Akteur (bei ihm „Bedrohung“) ausgenutzt, der in einer Aktion (bei ihm „Gefährdung“) einen Schaden („Schadwirkung“) anrichtet. Dazu kommt die Widerstandskraft einer Organisation, die „Resilienz“: wie gut sie vorbeugt, sich verteidigt und einen Vorfall bewältigt. Das BSI nennt also den Akteur „Bedrohung“, während dieses Kapitel den Akteur „Angreifer“ und die Möglichkeit „Bedrohung“ nennt. Gemeint ist dieselbe Kette; beim Lesen fremder Texte lohnt es sich, kurz zu prüfen, wie dort die Wörter verteilt sind.
:::

:::aufgabe Aufgabe 4 ★★ Risiko rechnen und entscheiden
<span class="anker" id="aufg-4"></span>

Eine Steuerberatung mit zwölf Mitarbeitern schätzt drei Ereignisse ab:

<ul>

<li>

Diebstahl eines Laptops: im Mittel einmal in fünf Jahren, Schaden 3 000 € (davon 1 000 € für das Gerät und 2 000 € für die Folgen, weil Mandantendaten darauf lagen);

</li>

<li>

ein durch Phishing übernommenes E-Mail-Konto: zweimal im Jahr, je 800 €;

</li>

<li>

Erpressungssoftware: einmal in 20 Jahren, Schaden 120 000 €.

</li>

</ul>

<ol class="al">

<li>

Berechne die drei Risiken und das Gesamtrisiko, und ordne die Ereignisse nach ihrem Risiko.

</li>

<li>

Drei Maßnahmen stehen zur Wahl: eine tägliche, vom Netz getrennte Sicherungskopie für 1 500 €/Jahr, die den Schaden durch Erpressungssoftware auf 20 000 € senkt; eine Schulung gegen Phishing für 1 000 €/Jahr, die die Häufigkeit übernommener Konten halbiert; eine Verschlüsselung der Laptop-Festplatten für 50 €/Jahr, die die Folgekosten eines Diebstahls verhindert. Berechne für jede den Nettonutzen. Welche lohnen sich?

</li>

<li>

Die Schulung lohnt sich nach (b) nicht. Nenne zwei Gründe, warum die Steuerberatung sie trotzdem durchführen könnte, und ordne jeden einer Einschränkung der Formel $R=H\cdot S$ zu.

</li>

</ol>

:::loesung
(a) Mit $R=H\cdot S$:

<ul>

<li>

Laptop: $H=0{,}2/\text{Jahr}$, $R=0{,}2\cdot3\,000=600$ €/Jahr.

</li>

<li>

Phishing: $R=2\cdot800=1\,600$ €/Jahr.

</li>

<li>

Erpressungssoftware: $H=0{,}05/\text{Jahr}$, $R=0{,}05\cdot120\,000=6\,000$ €/Jahr.

</li>

</ul>

Gesamtrisiko nach [(3.5)](#gl-3-5): $R_\Sigma=600+1\,600+6\,000=8\,200$ €/Jahr. Reihenfolge: Erpressungssoftware vor Phishing vor Laptop. Das seltenste Ereignis hat das größte Risiko; es macht allein fast drei Viertel des Gesamtrisikos aus.

(b) Nettonutzen $N=R_\text{vorher}-R_\text{nachher}-K$:

<ul>

<li>

Sicherungskopie: $R_\text{nachher}=0{,}05\cdot20\,000=1\,000$, also $N=6\,000-1\,000-1\,500=+3\,500$ €/Jahr. Lohnt sich.

</li>

<li>

Schulung: $R_\text{nachher}=1\cdot800=800$, also $N=1\,600-800-1\,000=-200$ €/Jahr. Lohnt sich nach dieser Rechnung knapp nicht.

</li>

<li>

Verschlüsselung: Ein Diebstahl kostet nur noch das Gerät, $R_\text{nachher}=0{,}2\cdot1\,000=200$, also $N=600-200-50=+350$ €/Jahr. Lohnt sich, und zwar im Verhältnis zu ihren Kosten am meisten.

</li>

</ul>

(c) Zwei mögliche Gründe:

<ul>

<li>

⁠*Die Zahlen sind Schätzungen.* Die Schulung kann mehr bewirken als eine Halbierung, oder die Häufigkeit von Phishing steigt; schon bei $H=3/\text{Jahr}$ wäre $N=2\,400-1\,200-1\,000=+200$ €/Jahr. Die Formel hängt an unsicheren Eingaben.

</li>

<li>

⁠*Ein übernommenes Konto kann mehr kosten als 800 €.* Über ein E-Mail-Konto kann ein Angreifer auch Erpressungssoftware einschleusen; dann hängt das größte Risiko am kleinsten. Die Formel betrachtet die Ereignisse getrennt, sie sind aber nicht unabhängig, und ein seltener, sehr hoher Schaden zählt für die Existenz der Firma mehr als sein Erwartungswert.

</li>

</ul>

Dazu kommen Pflichten: Eine Steuerberatung muss die Daten ihrer Mandanten nach dem Datenschutzrecht angemessen schützen, ob sich das rechnet oder nicht.
:::
:::

:::aufgabe Aufgabe 5 ★★ Dein eigenes Gerät, Teil 2: Angreifermodell und Angriffsfläche
<span class="anker" id="aufg-5"></span>

Nimm dein Blatt aus Aufgabe [2](was-geschutzt-wird-schutzgut-und-schutzziele.html#aufg-2).

<ol class="al">

<li>

Beschreibe zwei verschiedene Angreifer, mit denen du für dein Gerät rechnen musst, jeweils mit Ziel, Können und Zugang. Einer davon soll aus der Ferne angreifen, der andere nicht.

</li>

<li>

Zähle die Angriffsfläche deines Geräts auf: alle Stellen, an denen einer deiner beiden Angreifer ansetzen könnte. Ordne sie nach Eingaben, Netzdiensten, Anschlüssen, Menschen und Lieferanten.

</li>

<li>

Welche zwei Stellen könntest du ganz abschalten oder entfernen, ohne dass dir eine Funktion fehlt, die du wirklich nutzt?

</li>

</ol>

:::loesung
Musterlösung für den Router aus Aufgabe [2](was-geschutzt-wird-schutzgut-und-schutzziele.html#aufg-2).

(a) *Angreifer 1, aus der Ferne:* Betreiber automatischer Suchprogramme. Ziel: Geräte übernehmen und für Angriffe auf andere vermieten. Können: fertige Listen von Werkspasswörtern und Exploits für bekannte Lücken, unbegrenzt Zeit, aber kein Interesse an genau diesem Router. Zugang: über das Internet, nur zu Diensten, die von außen erreichbar sind. *Angreifer 2, nicht aus der Ferne:* ein Gast oder ehemaliger Mitbewohner. Ziel: den Verkehr der anderen mitlesen oder aus Ärger stören. Können: Alltagswissen, ein Laptop, Zeit. Zugang: im WLAN, vielleicht mit den Händen am Gerät, wenn es im Flur steht.

(b) Angriffsfläche: *Eingaben* sind die Verwaltungsoberfläche mit ihrer Anmeldung und die Einrichtung per Knopfdruck am Gerät. *Netzdienste* sind die Verwaltung aus dem Internet (falls eingeschaltet), Fernwartung durch den Anbieter, Gäste-WLAN, ein Dienst zur Freigabe angeschlossener Festplatten, die WLAN-Funkschnittstelle selbst. *Anschlüsse* sind die Netzwerkbuchsen, ein USB-Anschluss und die Reset-Taste. *Menschen* sind alle Bewohner, die das WLAN-Passwort weitergeben könnten. *Lieferanten* sind der Hersteller, dessen Updates man vertraut, und der Anbieter des Anschlusses.

(c) Typische Kandidaten: die Verwaltung aus dem Internet ausschalten und den Freigabedienst für Festplatten abschalten, wenn niemand ihn nutzt. Jede abgeschaltete Stelle senkt die Wahrscheinlichkeit einer offenen Stelle nach [(3.7)](#gl-3-7).
:::
:::

:::aufgabe Aufgabe 6 ★★ Wie die Angriffsfläche wächst
<span class="anker" id="aufg-6"></span>

Ein Hersteller vernetzter Kameras rechnet damit, dass jede Schnittstelle unabhängig mit $p=5\,\%$ eine ausnutzbare Schwachstelle enthält.

<ol class="al">

<li>

Wie groß ist die Wahrscheinlichkeit, dass eine Kamera mit $n=10$ Schnittstellen mindestens eine solche Schwachstelle hat? Wie groß ist sie bei $n=20$?

</li>

<li>

Wie gut ist die Näherung $n\cdot p$ in beiden Fällen? Warum muss sie bei großem $n$ versagen?

</li>

<li>

Bei wie vielen Schnittstellen liegt die Wahrscheinlichkeit gerade noch unter 25 %?

</li>

</ol>

:::loesung
(a) Mit [(3.7)](#gl-3-7): $n=10$: $P=1-0{,}95^{10}=1-0{,}5987=0{,}401$. $n=20$: $P=1-0{,}95^{20}=1-0{,}3585=0{,}642$.

(b) Die Näherung $n\cdot p$ liefert $0{,}5$ und $1{,}0$. Bei $n=10$ liegt sie um 25 % zu hoch, bei $n=20$ ist sie unbrauchbar. Sie muss versagen, denn eine Wahrscheinlichkeit kann nicht größer als 1 werden, $n\cdot p$ aber schon. Die Näherung zählt Fälle mit zwei oder mehr Schwachstellen mehrfach; das fällt nur ins Gewicht, wenn $n\cdot p$ nicht mehr klein gegen 1 ist.

(c) Gesucht ist das größte $n$ mit $1-0{,}95^n<0{,}25$, also $0{,}95^n>0{,}75$. Logarithmieren: $n<\ln0{,}75/\ln0{,}95=5{,}61$. Also höchstens $n=5$ Schnittstellen; dann ist $P=0{,}226$, bei sechs wären es $0{,}265$.
:::
:::
