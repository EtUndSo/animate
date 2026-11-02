---
title: Stufe 10: Grenze des Bildes: Magnetismus und Induktion
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Ladung, Feld und Potenzial
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

Die Richtung des Magnetfelds liefert die __Rechte-Faust-Regel__: Der Daumen zeigt in die technische Stromrichtung, die Finger zeigen in Richtung des Felds. Die __technische Stromrichtung__ läuft von Plus nach Minus, die Elektronen im Draht laufen entgegengesetzt ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

:::satz Satz 10.1 (Induktionsgesetz)
<span class="anker" id="satz-10-1"></span>

Ändert sich der magnetische Fluss $\Phi$ durch eine Spule mit $N$ Windungen, entsteht zwischen ihren Enden die Spannung

<span class="anker" id="gl-10-1"></span>
$$u_\mathrm{ind}(t)=-N\,\frac{\mathrm{d}\Phi}{\mathrm{d} t}. \tag{10.1}$$
:::

⁠**So liest man das:** Der __magnetische Fluss__ $\Phi$ misst, wie viel Magnetfeld durch die Spulenfläche tritt, $[\Phi]=\mathrm{V\,s}=\mathrm{Wb}$ (Weber). Kleine Spulen führen Mikro- bis Milliweber. Es zählt nur die Änderung, nicht der Fluss selbst. Das Gesetz ist ein Messergebnis: Das Wirbelfeld liefert längs einer Windung die Spannung $|\mathrm{d}\Phi/\mathrm{d} t|$, die $N$ Windungen liegen hintereinander, ihre Spannungen addieren sich. Der Kleinbuchstabe $u$ steht für eine zeitabhängige Spannung. Das Minuszeichen sagt: Ein Strom, den diese Spannung treibt, wirkt der Flussänderung entgegen. **Gültigkeit:** Alle Windungen müssen denselben Fluss umfassen.

Faraday zeigte die Induktion auch ohne Magnet: Er wickelte zwei Spulen auf einen Ring, schloss an die eine eine Batterie an, an die andere ein Galvanometer (ein frühes Strommessgerät). Es schlug nur beim Ein- und Ausschalten aus, denn nur dann ändert sich der Fluss.

**Maxwells Gleichungen in Worten.** Die Gleichungen selbst brauchen mehr Mathematik, ihr Inhalt passt in vier Sätze. Die __Flussdichte__ ist dabei das Maß für die Dichte der Feldlinien. **Gaußsches Gesetz für elektrische Felder:** Ladungen sind Quellen und Senken der elektrischen Flussdichte. **Gaußsches Gesetz für Magnetismus:** Die magnetische Flussdichte hat keine Quellen, ihre Linien sind geschlossen. **Induktionsgesetz:** Zeitliche Änderungen des magnetischen Flusses führen zu einem elektrischen Wirbelfeld. **Durchflutungsgesetz:** Ströme und zeitliche Änderungen des elektrischen Felds führen zu einem magnetischen Wirbelfeld.

**Beispiel.** Der Magnet in Abb. [12](#abb-12) ändert den Fluss durch die Spule mit $N=500$ gleichmäßig um 0,2 mWb in 25 ms. Die Spannung ist dann konstant: $|U_\mathrm{ind}|=500\cdot0{,}2\,\mathrm{mWb}/25\,\mathrm{ms}=4$ V. In dieser Zeit ist das Umlaufintegral von $\vec E$ um den Fluss nicht null, und die Spannung zwischen zwei Punkten hängt davon ab, auf welcher Seite des Flusses der Weg verläuft.

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
