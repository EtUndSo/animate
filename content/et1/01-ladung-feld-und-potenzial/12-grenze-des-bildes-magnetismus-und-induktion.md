---
title: Stufe 10: Grenze des Bildes: Magnetismus und Induktion
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
order: 1111200
summary: Alles bisher galt für ruhende Ladungen.
tags: Magnetfeld, Spule, Induktion, Elektromagnetismus, Wirbelfeld, Rechte-Faust-Regel, technische Stromrichtung, magnetische Fluss
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Alles bisher galt für ruhende Ladungen. Diese Stufe zeigt, was sich ändert, wenn Ladungen sich bewegen und Magnetfelder sich ändern, und wo die Wegunabhängigkeit aufhört.
:::

**Die Idee.** Lange galten Elektrizität und Magnetismus als getrennte Gebiete. 1820 sah Ørsted, dass eine Kompassnadel neben einem stromführenden Draht ausschlägt: Bewegte Ladung erzeugt ein __Magnetfeld__ $H$. 1831 kehrte Faraday den Gedanken um: Ein Magnet, den er in einer __Spule__ bewegte, einem zu Windungen aufgewickelten Draht, erzeugte an deren Enden eine Spannung. Das heißt __Induktion__. 1864 fasste Maxwell alles zum __Elektromagnetismus__ zusammen. Der Mechanismus der Induktion ist ein neues Feld: Ein sich änderndes Magnetfeld erzeugt ein elektrisches Feld mit geschlossenen Linien, ein __Wirbelfeld__. Auf einem Umlauf gewinnt eine Ladung darin Energie, damit endet die Aussage [(6.2)](arbeit-im-feld.html#gl-6-2).

:::abbildung et1/k1oersted 12
Links: Querschnitt eines Drahts, der Strom $I$ fließt in die Zeichenebene. Das Magnetfeld $H$ läuft in Kreisen um den Draht, Kompassnadeln richten ihre rote Spitze danach aus. Rechts: Ein bewegter Stabmagnet ändert den magnetischen Fluss $\Phi$ durch die Spule. Solange er sich bewegt, zeigt das Messgerät die Spannung $u_\mathrm{ind}$.
:::

Die Richtung des Magnetfelds liefert die __Rechte-Faust-Regel__: Der Daumen zeigt in die technische Stromrichtung, die Finger zeigen in Richtung des Felds. Die __technische Stromrichtung__ läuft von Plus nach Minus, die Elektronen im Draht laufen entgegengesetzt ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

:::satz Satz 10.1 (Induktionsgesetz)
<span class="anker" id="satz-10-1"></span>

Ändert sich der magnetische Fluss $\Phi$ durch eine Spule mit $N$ Windungen, entsteht zwischen ihren Enden die Spannung

<span class="anker" id="gl-10-1"></span>
$$u_\mathrm{ind}(t)=-N\,\frac{\mathrm{d}\Phi}{\mathrm{d} t}. \tag{10.1}$$
:::

⁠**So liest man das:** Der __magnetische Fluss__ $\Phi$ misst, wie viel Magnetfeld durch die Spulenfläche tritt, $[\Phi]=\mathrm{V\,s}=\mathrm{Wb}$ (Weber). Kleine Spulen führen Mikro- bis Milliweber. Es zählt nur die Änderung, nicht der Fluss selbst. Das Gesetz ist ein Messergebnis: Das Wirbelfeld liefert längs einer Windung die Spannung $|\mathrm{d}\Phi/\mathrm{d} t|$, die $N$ Windungen liegen hintereinander, ihre Spannungen addieren sich. Der Kleinbuchstabe $u$ steht für eine zeitabhängige Spannung. Das Minuszeichen sagt: Ein Strom, den diese Spannung treibt, wirkt der Flussänderung entgegen. **Gültigkeit:** Alle Windungen müssen denselben Fluss umfassen.

Faraday zeigte die Induktion auch ohne Magnet: Er wickelte zwei Spulen auf einen Ring, schloss an die eine eine Batterie an, an die andere ein Galvanometer (ein frühes Strommessgerät). Es schlug nur beim Ein- und Ausschalten aus, denn nur dann ändert sich der Fluss.

**Maxwells Gleichungen in Worten.** Die Gleichungen selbst brauchen mehr Mathematik, ihr Inhalt passt in vier Sätze. Die __Flussdichte__ ist dabei das Maß für die Dichte der Feldlinien. **Gaußsches Gesetz für elektrische Felder:** Ladungen sind Quellen und Senken der elektrischen Flussdichte. **Gaußsches Gesetz für Magnetismus:** Die magnetische Flussdichte hat keine Quellen, ihre Linien sind geschlossen. **Induktionsgesetz:** Zeitliche Änderungen des magnetischen Flusses führen zu einem elektrischen Wirbelfeld. **Durchflutungsgesetz:** Ströme und zeitliche Änderungen des elektrischen Felds führen zu einem magnetischen Wirbelfeld.

::::beispiel
Der Magnet in Abb. [12](#abb-12) ändert den Fluss durch die Spule mit $N=500$ gleichmäßig um 0,2 mWb in 25 ms. Die Spannung ist dann konstant: $|U_\mathrm{ind}|=500\cdot0{,}2\,\mathrm{mWb}/25\,\mathrm{ms}=4$ V. In dieser Zeit ist das Umlaufintegral von $\vec E$ um den Fluss nicht null, und die Spannung zwischen zwei Punkten hängt davon ab, auf welcher Seite des Flusses der Weg verläuft.
::::

⁠**Grenzfälle:** Für konstanten Fluss ist $u_\mathrm{ind}=0$, ein ruhender Magnet erzeugt keine Spannung. In den meisten Schaltungen sitzen die sich ändernden Flüsse fast vollständig in Spulen. Zwischen den Bauteilen bleibt das Feld praktisch wirbelfrei, deshalb bleiben Potenziale und Spannungen dort das Werkzeug.

:::frage Warum darf man in einem Wirbelfeld kein Potenzial angeben?
Das Potenzial eines Orts ist die Arbeit je Ladung bis zum Bezugspunkt. Im Wirbelfeld hängt sie vom Weg ab. Zwei Wege liefern zwei Werte, der Ort hätte kein eindeutiges Potenzial.
:::

:::aufgabe Aufgabe 11 ★ Induktion
<span class="anker" id="aufg-11"></span>

Eine Spule mit 200 Windungen umfasst einen Fluss, der gleichmäßig in 10 ms um 0,5 mWb zunimmt. (a) Wie groß ist der Betrag der induzierten Spannung? (b) Der Fluss bleibt danach konstant. Welche Spannung liegt nun an?

:::loesung
(a) $|U_\mathrm{ind}|=200\cdot0{,}5\,\mathrm{mWb}/10\,\mathrm{ms}=10$ V. (b) Null, denn $\mathrm{d}\Phi/\mathrm{d} t=0$.
:::
:::

::::formelsammlung
**Induktionsgesetz**

$$u_\mathrm{ind}(t)=-N\,\frac{\mathrm{d}\Phi}{\mathrm{d} t}$$

Spannung zwischen den Enden einer Spule mit $N$ Windungen, wenn sich der magnetische Fluss $\Phi$ ändert; alle Windungen umfassen denselben Fluss. Es zählt nur die Änderung: Für konstanten Fluss ist $u_\mathrm{ind}=0$. Das Minuszeichen sagt: Ein Strom, den diese Spannung treibt, wirkt der Flussänderung entgegen.

**Einheit des magnetischen Flusses**

$$[\Phi]=\mathrm{V\,s}=\mathrm{Wb}$$

Weber; der Fluss misst, wie viel Magnetfeld durch die Spulenfläche tritt.

**Wirbelfeld**

$$\oint_L\vec E\cdot\mathrm{d}\vec s\neq0$$

Für einen Weg $L$ um einen sich ändernden magnetischen Fluss: Das Feld hat geschlossene Linien, auf einem Umlauf gewinnt eine Ladung Energie. Die Arbeit hängt vom Weg ab, ein Ort hat kein eindeutiges Potenzial.
::::

::::lernkarten
:::karte begriff Induktion
Was versteht man unter Induktion, und was ist ihre Ursache?
---
Das Entstehen einer elektrischen Spannung durch einen sich ändernden magnetischen Fluss, etwa an den Enden einer Spule. Ursache ist ein elektrisches Wirbelfeld, erzeugt vom sich ändernden Magnetfeld.
--- falsch
Das Entstehen einer elektrischen Spannung durch einen ruhenden Magneten in einer Spule. Je stärker der Magnet, desto größer die Spannung, auch wenn sich dabei nichts bewegt oder ändert.
--- falsch
Das Entstehen eines Magnetfelds um einen Draht, durch den ein Strom fließt. Eine Kompassnadel neben dem Draht schlägt dadurch aus und richtet sich nach dem Feld aus, solange der Strom fließt.
--- falsch
Die Verschiebung der freien Elektronen in einem Metall durch ein äußeres elektrisches Feld. Sie wandern, bis keine Kraft mehr auf sie wirkt und das Innere feldfrei ist.
:::
:::karte begriff Wirbelfeld
Was kennzeichnet ein elektrisches Wirbelfeld, wie es bei der Induktion auftritt, und was gilt in ihm auf einem geschlossenen Umlauf?
---
Ein elektrisches Feld mit geschlossenen Linien, das ein sich änderndes Magnetfeld erzeugt. Auf einem Umlauf gewinnt eine Ladung darin Energie, $\oint_L\vec E\cdot\mathrm{d}\vec s=0$ gilt nicht mehr.
--- falsch
Ein elektrisches Feld ruhender Ladungen, dessen Linien auf positiven Ladungen beginnen und auf negativen enden. Auf einem Umlauf gewinnt eine Ladung darin keine Energie.
--- falsch
Ein elektrisches Feld, dessen Linien sich schneiden und verwirbeln, weil sich die Felder mehrerer Ladungen an denselben Orten überlagern.
--- falsch
Ein elektrisches Feld mit geschlossenen Linien, in dem jeder Ort ein eindeutiges Potenzial hat. Auf einem Umlauf ist die Arbeit an einer Ladung null.
:::
:::karte begriff magnetischer Fluss
Was misst der magnetische Fluss $\Phi$?
---
Wie viel Magnetfeld durch eine Fläche tritt, etwa durch die Fläche einer Spule. Seine Einheit ist $\mathrm{V\,s}=\mathrm{Wb}$, Weber.
--- falsch
Wie viel Ladung je Sekunde durch eine Spule fließt, gezählt über alle Windungen. Seine Einheit ist $\mathrm{C/s}=\mathrm{A}$, Ampere.
--- falsch
Wie schnell sich das Magnetfeld in einer Spule ändert, gemessen an ihren Enden. Seine Einheit ist $\mathrm{V/s}$, Volt je Sekunde.
--- falsch
Welche Spannung eine Spule an ihren Enden liefert, wenn sich ein Magnet in ihr bewegt. Seine Einheit ist Volt.
:::
:::karte formel Induktionsgesetz
Welche Spannung entsteht zwischen den Enden einer Spule mit $N$ Windungen, wenn sich der magnetische Fluss $\Phi$ durch sie ändert?
---
$u_\mathrm{ind}(t)=-N\,\frac{\mathrm{d}\Phi}{\mathrm{d} t}$. Es zählt nur die Änderung des Flusses; die $N$ Windungen liegen hintereinander, ihre Spannungen addieren sich. Gilt, wenn alle Windungen denselben Fluss umfassen.
--- falsch
$u_\mathrm{ind}(t)=-N\,\Phi$. Es zählt der Fluss selbst, nicht seine Änderung; die $N$ Windungen liegen hintereinander, ihre Spannungen addieren sich. Auch ein ruhender Magnet erzeugt so eine Spannung.
--- falsch
$u_\mathrm{ind}(t)=-\frac{1}{N}\,\frac{\mathrm{d}\Phi}{\mathrm{d} t}$. Es zählt nur die Änderung des Flusses; die $N$ Windungen teilen sich die Spannung, mehr Windungen ergeben eine kleinere Spannung.
--- falsch
$u_\mathrm{ind}(t)=-N\,\frac{\mathrm{d}\Phi}{\mathrm{d} t}$. Es zählt nur die Änderung des Flusses; das Minuszeichen zeigt, dass die induzierte Spannung immer negativ ist, gleich ob der Fluss wächst oder sinkt.
:::
:::karte zusammenhang Konstanter Fluss
Was passiert mit der induzierten Spannung, wenn der Fluss durch die Spule konstant bleibt?
---
Sie ist null, weil nur die Änderung des Flusses zählt: $\mathrm{d}\Phi/\mathrm{d} t=0$. Ein ruhender Magnet erzeugt keine Spannung; deshalb schlug Faradays Galvanometer nur beim Ein- und Ausschalten aus.
--- falsch
Sie bleibt auf dem zuletzt erreichten Wert stehen, weil der Fluss weiterhin durch alle Windungen der Spule tritt. Erst wenn der Fluss verschwindet, geht auch die Spannung auf null zurück.
--- falsch
Sie wird am größten, weil der volle Fluss nun dauerhaft durch alle Windungen tritt. Während der Änderung war der Fluss noch nicht vollständig in der Spule angekommen.
--- falsch
Sie sinkt langsam auf null, weil die Windungen die Spannung noch eine Weile speichern und sie nach und nach abgeben. Wie lange das dauert, hängt von der Zahl der Windungen ab.
:::
:::karte zusammenhang Minuszeichen im Induktionsgesetz
Was passiert mit einem Strom, den die induzierte Spannung treibt?
---
Er wirkt der Flussänderung entgegen, die ihn hervorruft. Das drückt das Minuszeichen in $u_\mathrm{ind}(t)=-N\,\frac{\mathrm{d}\Phi}{\mathrm{d} t}$ aus.
--- falsch
Er verstärkt die Flussänderung, die ihn hervorruft. Das drückt das Minuszeichen in $u_\mathrm{ind}(t)=-N\,\frac{\mathrm{d}\Phi}{\mathrm{d} t}$ aus.
--- falsch
Er fließt immer gegen die technische Stromrichtung, also von Minus nach Plus. Das drückt das Minuszeichen im Induktionsgesetz aus.
--- falsch
Er hebt die induzierte Spannung sofort auf, sodass an der Spule keine Spannung mehr liegt. Das drückt das Minuszeichen aus.
:::
:::karte zusammenhang Kein Potenzial im Wirbelfeld
Warum kann man in einem Wirbelfeld kein Potenzial angeben?
---
Weil das Potenzial eines Orts die Arbeit je Ladung bis zum Bezugspunkt ist, und die hängt im Wirbelfeld vom Weg ab. Zwei Wege liefern zwei Werte, also kein eindeutiges Potenzial.
--- falsch
Weil die Feldstärke in einem Wirbelfeld überall null ist. Ohne Gefälle gibt es auch kein Potenzial, das man einem Ort zuordnen könnte; alle Werte wären gleich.
--- falsch
Weil ein Wirbelfeld keine Ladungen als Quellen hat. Ein Potenzial lässt sich nur angeben, wenn am Bezugspunkt eine Ladung sitzt, von der die Feldlinien ausgehen und auf die sie zulaufen.
--- falsch
Weil im Wirbelfeld die Arbeit auf jedem Weg null ist. Alle Orte hätten dasselbe Potenzial, und die Angabe eines Potenzials wäre deshalb ohne jeden Inhalt.
:::
:::karte zusammenhang Potenziale in Schaltungen
Warum darf man in den meisten Schaltungen trotz Induktion mit Potenzialen und Spannungen rechnen?
---
Weil die sich ändernden Flüsse fast vollständig in Spulen sitzen. Zwischen den Bauteilen bleibt das Feld praktisch wirbelfrei, dort hängt die Arbeit je Ladung nicht vom Weg ab.
--- falsch
Weil Induktion nur bei sehr hohen Spannungen auftritt. In Schaltungen mit wenigen Volt bleibt das Feld deshalb überall wirbelfrei, auch in den Spulen.
--- falsch
Weil sich die induzierten Spannungen wegen des Minuszeichens im Induktionsgesetz in jeder Schaltung zu null aufheben, sobald man alle Bauteile zusammenzählt.
--- falsch
Weil Schaltungen keine bewegten Magnete enthalten. Ohne bewegten Magneten ändert sich kein Fluss, also entsteht in einer Schaltung auch kein Wirbelfeld, auch nicht in ihren Spulen.
:::
:::karte begriff Gaußsche Gesetze
Was besagen das Gaußsche Gesetz für elektrische Felder und das für Magnetismus?
---
Ladungen sind Quellen und Senken der elektrischen Flussdichte. Die magnetische Flussdichte hat keine Quellen, ihre Linien sind geschlossen.
--- falsch
Ladungen sind Quellen und Senken der elektrischen und der magnetischen Flussdichte. Beide Arten von Linien beginnen auf Ladungen.
--- falsch
Die elektrische Flussdichte hat keine Quellen, ihre Linien sind geschlossen. Ladungen sind Quellen und Senken der magnetischen Flussdichte.
--- falsch
Ladungen sind Quellen und Senken der elektrischen Flussdichte. Die magnetischen Linien beginnen am Nordpol eines Magneten und enden am Südpol.
:::
:::karte begriff technische Stromrichtung
In welche Richtung zeigt die technische Stromrichtung, nach der man etwa den Daumen bei der Rechte-Faust-Regel ausrichtet, und wie laufen dabei die Elektronen?
---
Die vereinbarte Richtung des Stroms von Plus nach Minus. Die Elektronen im Draht laufen ihr entgegen.
--- falsch
Die Richtung, in der die Elektronen im Draht tatsächlich laufen, von Plus nach Minus.
--- falsch
Die vereinbarte Richtung des Stroms von Minus nach Plus. Die Elektronen im Draht laufen in dieselbe Richtung.
--- falsch
Die Richtung, in der die Protonen im Draht laufen, von Plus nach Minus. Die Elektronen bleiben stehen.
:::
:::karte begriff Rechte-Faust-Regel
Was gibt die Rechte-Faust-Regel an?
---
Die Richtung des Magnetfelds um einen stromführenden Draht: Zeigt der Daumen der rechten Faust in die technische Stromrichtung, zeigen die Finger in Richtung des Felds.
--- falsch
Die Richtung des Magnetfelds um einen stromführenden Draht: Zeigt der Daumen der rechten Faust in die Laufrichtung der Elektronen, zeigen die Finger in Richtung des Felds.
--- falsch
Die Richtung des Magnetfelds um einen stromführenden Draht: Das Feld verläuft parallel zum Draht, in die Richtung, in die der Daumen der rechten Faust zeigt.
--- falsch
Die Richtung der induzierten Spannung in einer Spule: Zeigt der Daumen der rechten Faust in die Bewegungsrichtung des Magneten, zeigen die Finger in Richtung der Spannung.
:::
::::
