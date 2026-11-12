---
title: Stufe 1: Vom Vierpol zum Zweitor
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1160300
summary: Ein Netzwerk mit vier Klemmen hat drei unabhängige Ströme und drei unabhängige Spannungen.
tags: Vierpol, Torgrößen, Vierpoltheorie, Eingang, Ausgang, Vorwärtsrichtung, Rückwärtsrichtung, Elementarzweitoren
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein Netzwerk mit vier Klemmen hat drei unabhängige Ströme und drei unabhängige Spannungen. Diese Stufe zeigt, welche Bedingung daraus zwei Ströme und zwei Spannungen macht.
:::

**Die Idee.** Ein __Vierpol__ ist ein Netzwerk mit vier Klemmen. Für das ganze Netzwerk gilt die Knotenregel ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) wie für einen großen Knoten: Ein Klemmenstrom liegt durch die drei anderen fest. Die Maschenregel bindet ebenso die Spannungen zwischen den Klemmen. Hängt nun an den Klemmen 1 und 1$'$ ein Zweipol, etwa eine Quelle, kommt eine Aussage hinzu: Ein Zweipol hat nur zwei Anschlüsse. Jede Ladung, die er an einem abgibt, nimmt er am anderen wieder auf. Der Strom, der bei Klemme 1 in das Netzwerk läuft, muss bei Klemme 1$'$ zurückkehren. Das Klemmenpaar verhält sich wie ein einziger Zugang mit einem Strom und einer Spannung (Abb. [1](#abb-1) links).

:::definition Definition 1.1 (Vierpol, Tor, Zweitor)
<span class="anker" id="satz-1-1"></span>

An einem Vierpol mit den Klemmen 1, 1$'$, 2, 2$'$ seien alle Klemmenströme zum Netzwerk hin gezählt. Immer gilt

<span class="anker" id="gl-1-1"></span>
$$I_1+I_{1'}+I_2+I_{2'}=0,\qquad U_{11'}+U_{1'2'}-U_{22'}+U_{21}=0. \tag{1.1}$$

Ein Klemmenpaar ist ein Tor, wenn die Torbedingung gilt. Ein Vierpol mit zwei Toren ist ein Zweitor:

<span class="anker" id="gl-1-2"></span>
$$I_{1'}=-I_1,\qquad I_{2'}=-I_2. \tag{1.2}$$

Seine __Torgrößen__ sind $U_1=U_{11'}$, $I_1$, $U_2=U_{22'}$ und $I_2$.
:::

⁠**So liest man das:** [(1.1)](#gl-1-1) lässt je drei Ströme und drei Spannungen frei. Die erste Gleichung ist die Knotenregel, die zweite die Maschenregel im Umlauf $1\to1'\to2'\to2\to1$. [(1.2)](#gl-1-2) nimmt je einen Strom weg. Auch die Spannung $U_{1'2'}$ fällt aus der Beschreibung heraus: Zwischen den Toren fließt außen kein Strom, über sie wird also keine Leistung übertragen. Ob ein Vierpol zum Zweitor wird, entscheidet seine Beschaltung: Liegt an jedem Klemmenpaar ein Zweipol, ist [(1.2)](#gl-1-2) von selbst erfüllt. Ein Zweig außen von Tor zu Tor bricht sie (Abb. [1](#abb-1) rechts). Der historische Name Vierpol lebt in der __Vierpoltheorie__ weiter.

:::abbildung et1/k6tor 1
Links: Quelle, Zweitor und Last. An beiden Toren kehrt jeder Strom an der zweiten Klemme zurück, Energie fließt in Vorwärtsrichtung von Tor 1 nach Tor 2. Rechts: Ein äußerer Zweig von Klemme 1 nach Klemme 2 führt den Strom $I_\mathrm{x}$. Nun fließt in 1 ein anderer Strom als aus 1$'$ heraus, die Klemmenpaare sind keine Tore mehr.
:::

Ein Zweitor ist eine gedanklich geschlossene Einheit, zugänglich nur über seine Tore. Seine Eigenschaften liegen durch die Zusammenhänge zwischen den Torgrößen fest, und diese lassen sich rechnen oder messen. Meist liegt an Tor 1, dem __Eingang__, eine Quelle, an Tor 2, dem __Ausgang__, ein Verbraucher. Dann fließt Energie in __Vorwärtsrichtung__ $1\to2$, die Gegenrichtung heißt __Rückwärtsrichtung__. Das Zweitor ist eine Grundstruktur: Gesteuerte Quellen sind Zweitore, Transformator, Verstärker und Transistor haben drei oder vier Anschlüsse, große Zweitore lassen sich aus __Elementarzweitoren__ aufbauen, und zusammengefügte Zweitore bilden wieder ein Zweitor. Die einfachsten Beispiele sind Spannungsteiler und Stromteiler ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

**Aufbau und Einteilung.** Hat ein Zweitor eine durchgehende Leitung von Klemme 1$'$ nach 2$'$, die __Masseleitung__, heißt es __erdunsymmetrisch__ (Abb. [2](#abb-2) links). Es ist eigentlich ein Dreipol, ein unechter Vierpol. Netzwerkmodelle von Transistoren und Verstärkern sind von dieser Art. Ein Zweitor, das wie die Brückenschaltung keine solche Leitung besitzt und spiegelbildlich zu einer Mittellinie aufgebaut ist, heißt __erdsymmetrisch__. Nach ihrem Verhalten teilt man Zweitore in lineare zeitunabhängige, zeitabhängige und nichtlineare ein. Dieses Kapitel behandelt die linearen zeitunabhängigen.

:::abbildung et1/k6masse 2
Links: Das T-Zweitor des Rechenmodells ist erdunsymmetrisch, rot die Masseleitung von 1$'$ nach 2$'$. Rechts: Die Brückenschaltung aus zwei Widerstandspaaren hat keine durchgehende Leitung zwischen den Toren, sie ist erdsymmetrisch. Stufe [3](impedanzform-und-leerlaufversuch.html#stufe-3) rechnet beide.
:::

::::beispiel
Im Betrieb des T-Zweitors (Stufe [4](das-zweitor-im-betrieb.html#stufe-4)) fließen $I_1=250$ mA hinein und $I_{1'}=-250$ mA, die Last entnimmt 50 mA, also $I_2=-50$ mA und $I_{2'}=+50$ mA. Die Summe in [(1.1)](#gl-1-1) ist null.
::::

⁠**Grenzfall:** Ist Tor 2 offen, ist $I_2=I_{2'}=0$, und das Zweitor wirkt nach außen wie ein Zweipol an Tor 1.

:::frage Die Masseleitung verbindet 1$'$ und 2$'$. Fließt da nicht doch Strom von Tor zu Tor?
Ja, im Inneren. In der Masseleitung des T-Zweitors laufen 50 mA von 2$'$ zum Fußpunkt von $R_\mathrm{b}$. Die Torbedingung sagt aber nur, was an den Klemmen geschieht. Innen darf jeder Strom laufen, solange jeder Klemmenstrom an seiner Partnerklemme zurückkommt.
:::

:::aufgabe Aufgabe 1 ★ Zählen an den Klemmen
<span class="anker" id="aufg-1"></span>

An einem Vierpol misst du $I_1=30$ mA, $I_{1'}=-30$ mA, $I_2=-10$ mA, außerdem $U_{11'}=6$ V, $U_{1'2'}=0$ V, $U_{22'}=2$ V.

<ol class="al">

<li>

Wie groß ist $I_{2'}$? Sind beide Klemmenpaare Tore?

</li>

<li>

Wie groß ist $U_{21}$?

</li>

<li>

Wie viele Ströme müsstest du mindestens messen, um alle Klemmenströme zu kennen, beim Vierpol und beim Zweitor?

</li>

</ol>

:::loesung
(a) Aus [(1.1)](#gl-1-1): $I_{2'}=-(30-30-10)\,\mathrm{mA}=+10$ mA. Es gilt $I_{1'}=-I_1$ und $I_{2'}=-I_2$, beide Paare sind Tore. (b) $U_{21}=-U_{11'}-U_{1'2'}+U_{22'}=-6\,\mathrm{V}-0\,\mathrm{V}+2\,\mathrm{V}=-4$ V. (c) Beim Vierpol drei, der vierte folgt aus der Knotenregel. Beim Zweitor zwei, die anderen folgen aus der Torbedingung.
:::
:::

::::formelsammlung
**Vierpol**

$$I_1+I_{1'}+I_2+I_{2'}=0,\qquad U_{11'}+U_{1'2'}-U_{22'}+U_{21}=0$$

Klemmen 1, 1$'$, 2, 2$'$, alle Klemmenströme zum Netzwerk hin gezählt. Knotenregel für das ganze Netzwerk und Maschenregel im Umlauf $1\to1'\to2'\to2\to1$. Gilt immer; es bleiben je drei unabhängige Ströme und Spannungen.

**Torbedingung**

$$I_{1'}=-I_1,\qquad I_{2'}=-I_2$$

Der Strom, der in die eine Klemme eines Tors hineinfließt, fließt aus der anderen wieder heraus. Ein Vierpol mit zwei Toren ist ein Zweitor. Von selbst erfüllt, wenn an jedem Klemmenpaar ein Zweipol liegt; ein äußerer Zweig von Tor zu Tor bricht sie. Innen darf jeder Strom laufen.

**Torgrößen**

$$U_1=U_{11'},\quad I_1,\quad U_2=U_{22'},\quad I_2$$

Die Ströme sind zum Zweitor hin gezählt. $U_{1'2'}$ fällt heraus: Zwischen den Toren fließt außen kein Strom, über sie wird keine Leistung übertragen. Tor 1 ist meist der Eingang mit der Quelle, Tor 2 der Ausgang mit dem Verbraucher; der Energiefluss von 1 nach 2 heißt Vorwärtsrichtung.
::::

::::lernkarten
:::karte begriff Vierpol
Was ist ein Vierpol, und wie viele seiner Klemmenströme und Spannungen sind unabhängig?
---
Ein Netzwerk mit vier Klemmen. Die Knotenregel für das ganze Netzwerk legt einen Klemmenstrom durch die drei anderen fest, die Maschenregel ebenso eine Spannung: Je drei bleiben unabhängig.
--- falsch
Ein Netzwerk aus vier Bauteilen zwischen zwei Klemmenpaaren. Jedes Bauteil hat einen eigenen Strom und eine eigene Spannung, also gibt es je vier unabhängige Ströme und Spannungen.
--- falsch
Ein Netzwerk mit vier Klemmen, an denen alle vier Ströme frei fließen dürfen. Die Knotenregel gilt nur für innere Knoten, deshalb sind alle vier Klemmenströme voneinander unabhängig.
--- falsch
Ein Netzwerk mit vier Klemmen, deren Ströme immer paarweise gleich groß und entgegengesetzt sind. Es bleiben deshalb nur zwei unabhängige Ströme und zwei unabhängige Spannungen.
:::
:::karte formel Knotenregel und Maschenregel am Vierpol
Welche zwei Gleichungen gelten an jedem Vierpol mit den Klemmen 1, 1$'$, 2, 2$'$, wenn alle Klemmenströme zum Netzwerk hin gezählt werden?
---
$I_1+I_{1'}+I_2+I_{2'}=0$, die Knotenregel für das ganze Netzwerk, und $U_{11'}+U_{1'2'}-U_{22'}+U_{21}=0$, die Maschenregel im Umlauf $1\to1'\to2'\to2\to1$. Beide gelten immer, gleich wie der Vierpol beschaltet ist.
--- falsch
$I_1+I_{1'}=0$ und $I_2+I_{2'}=0$, die Knotenregel für jedes einzelne Klemmenpaar, und $U_{11'}=U_{22'}$, die Maschenregel. Beide gelten an jedem Vierpol, gleich wie er beschaltet ist und was an seinen Klemmen hängt.
--- falsch
$I_1+I_{1'}+I_2+I_{2'}=0$, die Knotenregel, die aber nur gilt, wenn an jedem Klemmenpaar ein Zweipol liegt, und $U_{11'}+U_{22'}=0$, die Maschenregel im Umlauf um das ganze Netzwerk.
--- falsch
$I_1+I_2=I_{1'}+I_{2'}$, die Knotenregel: Was oben hineinfließt, fließt unten wieder heraus. Dazu $U_{11'}+U_{1'2'}+U_{22'}+U_{21}=0$, die Maschenregel im Umlauf $1\to1'\to2'\to2\to1$.
:::
:::karte begriff Tor und Torbedingung
Wann bildet ein Klemmenpaar eines Vierpols ein Tor, und wie lautet die Torbedingung für die Klemmenpaare 1, 1$'$ und 2, 2$'$?
---
Wenn der Strom, der in die eine Klemme hineinfließt, aus der anderen wieder herausfließt: $I_{1'}=-I_1$ und $I_{2'}=-I_2$. Das Klemmenpaar verhält sich dann wie ein einziger Zugang mit einem Strom und einer Spannung.
--- falsch
Wenn zwischen seinen beiden Klemmen eine Spannung liegt, die nicht null ist. Ein Klemmenpaar ohne Spannung ist kein Tor, auch wenn der Strom an der zweiten Klemme wieder zurückkehrt und beide Ströme gleich groß sind.
--- falsch
Wenn beide Klemmen denselben Strom in das Netzwerk führen: $I_{1'}=I_1$ und $I_{2'}=I_2$. Das Klemmenpaar verhält sich dann wie ein einziger Zugang mit dem doppelten Strom.
--- falsch
Wenn im Inneren kein Strom von diesem Klemmenpaar zum anderen fließt. Eine Masseleitung zwischen 1$'$ und 2$'$ verletzt deshalb die Torbedingung an beiden Toren zugleich.
:::
:::karte begriff Zweitor
Was macht einen Vierpol zum Zweitor, und wovon hängt es ab, ob er eines ist?
---
Ein Zweitor ist ein Vierpol mit zwei Toren, an beiden gilt die Torbedingung. Ob er eines ist, entscheidet seine Beschaltung: Liegt an jedem Klemmenpaar ein Zweipol, ist sie von selbst erfüllt; ein äußerer Zweig von Tor zu Tor bricht sie.
--- falsch
Ein Zweitor ist ein Vierpol mit genau zwei Bauteilen. Ob er eines ist, entscheidet allein sein innerer Aufbau; die äußere Beschaltung spielt dafür keine Rolle, weil sie die Bauteile im Inneren und ihre Verbindungen nicht verändert.
--- falsch
Ein Zweitor ist ein Vierpol, dessen Klemmen 1$'$ und 2$'$ durch eine durchgehende Leitung verbunden sind. Fehlt diese Masseleitung, bleibt er ein Vierpol, gleich was außen angeschlossen ist.
--- falsch
Ein Zweitor ist ein Vierpol mit zwei Toren. Ob er eines ist, entscheidet sein Inneres: Ein Zweig im Inneren von Tor zu Tor bricht die Torbedingung, außen darf man dagegen beliebig anschließen.
:::
:::karte zusammenhang Torbedingung durch einen Zweipol
Warum ist die Torbedingung von selbst erfüllt, wenn an den Klemmen 1 und 1$'$ ein Zweipol wie eine Quelle hängt?
---
Ein Zweipol hat nur zwei Anschlüsse. Jede Ladung, die er an einem abgibt, nimmt er am anderen wieder auf. Der Strom, der bei Klemme 1 in das Netzwerk läuft, muss deshalb bei Klemme 1$'$ zurückkehren.
--- falsch
Weil eine Quelle die Spannung zwischen ihren beiden Klemmen festhält. Eine feste Spannung erzwingt an beiden Klemmen gleich große Ströme in entgegengesetzter Richtung, gleich was angeschlossen ist.
--- falsch
Weil das Netzwerk im Inneren eine durchgehende Masseleitung hat. Sie führt jeden Strom, der bei Klemme 1 hineinfließt, auf kürzestem Weg zur Klemme 1$'$ zurück.
--- falsch
Weil die Knotenregel für das ganze Netzwerk gilt. Sie verlangt, dass an jedem einzelnen Klemmenpaar der hineinfließende Strom auch wieder herauskommt.
:::
:::karte begriff Torgrößen
Welche Größen beschreiben ein Zweitor von außen, und warum fällt die Spannung $U_{1'2'}$ zwischen den Toren heraus?
---
Die Torgrößen $U_1=U_{11'}$, $I_1$, $U_2=U_{22'}$ und $I_2$. $U_{1'2'}$ fällt heraus, weil zwischen den Toren außen kein Strom fließt und über sie deshalb keine Leistung übertragen wird.
--- falsch
Die vier Klemmenströme $I_1$, $I_{1'}$, $I_2$, $I_{2'}$. Spannungen braucht man gar nicht, und $U_{1'2'}$ fällt heraus, weil alle Spannungen aus den Strömen und den inneren Widerständen folgen.
--- falsch
Die Torgrößen $U_1$, $I_1$, $U_2$, $I_2$ und zusätzlich $U_{1'2'}$. Diese Spannung fällt nicht heraus, weil über sie die Leistung von Tor 1 nach Tor 2 übertragen wird.
--- falsch
Die Torgrößen $U_1=U_{11'}$, $I_1$, $U_2=U_{22'}$ und $I_2$. $U_{1'2'}$ fällt heraus, weil sie bei jedem Zweitor null ist, denn die Klemmen 1$'$ und 2$'$ sind immer verbunden.
:::
:::karte begriff Eingang und Ausgang
Welches Tor eines Zweitors heißt Eingang, welches Ausgang, und was liegt dort meist an?
---
Tor 1 ist der Eingang, an ihm liegt meist eine Quelle. Tor 2 ist der Ausgang, an ihm liegt meist ein Verbraucher.
--- falsch
Tor 1 ist der Ausgang, weil die Quelle dort Energie ausgibt. Tor 2 ist der Eingang, weil der Verbraucher dort Energie aufnimmt.
--- falsch
Eingang heißen die Klemmen 1 und 2, an denen meist die Quelle liegt. Ausgang heißen die Klemmen 1$'$ und 2$'$, an denen meist der Verbraucher liegt.
--- falsch
Eingang ist das Tor mit dem größeren Strom, Ausgang das mit dem kleineren. Was an den Toren angeschlossen ist, spielt dafür keine Rolle.
:::
:::karte begriff Vorwärtsrichtung und Rückwärtsrichtung
Was bezeichnen Vorwärtsrichtung und Rückwärtsrichtung bei einem Zweitor?
---
Die Richtung des Energieflusses: Mit der Quelle am Eingang und dem Verbraucher am Ausgang fließt Energie in Vorwärtsrichtung von Tor 1 nach Tor 2, die Gegenrichtung heißt Rückwärtsrichtung.
--- falsch
Die Richtung des Stroms in der Masseleitung: Vorwärtsrichtung heißt, er fließt von 1$'$ nach 2$'$, Rückwärtsrichtung heißt, er fließt von 2$'$ nach 1$'$ zurück zum Eingang, etwa wenn die Last abgeschaltet wird.
--- falsch
Die Zählrichtung der Torströme: Vorwärtsrichtung heißt, der Strompfeil zeigt in das Zweitor hinein, Rückwärtsrichtung heißt, er zeigt aus dem Zweitor heraus zur Last.
--- falsch
Die Lage der Klemmen in der Zeichnung: In Vorwärtsrichtung liegen die Klemmen 1 und 2 oben, in Rückwärtsrichtung liegen die Klemmen 1$'$ und 2$'$ oben.
:::
:::karte begriff Elementarzweitor
Was sind Elementarzweitore, und warum lassen sich aus ihnen große Zweitore aufbauen?
---
Einfache Grundbausteine, aus denen sich große Zweitore aufbauen lassen. Das gelingt, weil zusammengefügte Zweitore wieder ein Zweitor bilden.
--- falsch
Zweitore aus idealen Drähten ohne Bauteile. Sie dienen nur als Verbindung zwischen echten Zweitoren und verändern deren Verhalten nicht.
--- falsch
Grundbausteine, aus denen man große Zweitore aufbaut. Zusammengefügt bilden sie aber kein Zweitor mehr, sondern einen Vierpol ohne Tore.
--- falsch
Die kleinsten Zweitore, die noch eine Masseleitung haben. Ohne Masseleitung lässt sich ein Zweitor nicht in kleinere Teile zerlegen.
:::
:::karte begriff Vierpoltheorie
Woher kommt der Name Vierpoltheorie für die Beschreibung von Zweitoren?
---
Vom historischen Namen Vierpol für ein Netzwerk mit vier Klemmen. Ein Zweitor ist ein Vierpol mit zwei Toren, deshalb lebt der alte Name in der Vierpoltheorie weiter.
--- falsch
Von den vier Bauteilen, aus denen jedes Zweitor mindestens besteht. Die Theorie beschreibt, wie diese vier Pole an den beiden Toren zusammenwirken.
--- falsch
Von den vier Polen der Quelle und des Verbrauchers, die ein Zweitor miteinander verbindet. Die Theorie beschreibt den Weg der Energie zwischen ihnen.
--- falsch
Von den vier Messgeräten, die man zur Untersuchung eines Zweitors anschließt. Der Name ist jünger als das Wort Zweitor und hat es in der Fachsprache inzwischen ersetzt.
:::
:::karte begriff Masseleitung
Was ist die Masseleitung eines Zweitors, und was für ein Netzwerk ist ein Zweitor mit Masseleitung eigentlich?
---
Eine durchgehende Leitung von Klemme 1$'$ nach 2$'$. Ein Zweitor mit Masseleitung ist eigentlich ein Dreipol, ein unechter Vierpol.
--- falsch
Eine Leitung, die das Zweitor mit dem Erdpotenzial des Gebäudes verbindet. Ein Zweitor mit Masseleitung ist dadurch gegen Berührung geschützt.
--- falsch
Eine Leitung, die außen von Klemme 1 nach Klemme 2 führt. Ein Zweitor mit Masseleitung ist kein Zweitor mehr, weil die Leitung die Torbedingung bricht.
--- falsch
Eine durchgehende Leitung von 1$'$ nach 2$'$. Über sie fließt außen Strom von Tor zu Tor, deshalb gilt für ein solches Netzwerk die Torbedingung nicht.
:::
:::karte begriff erdunsymmetrisch und erdsymmetrisch
Wann heißt ein Zweitor erdunsymmetrisch, wann erdsymmetrisch?
---
Erdunsymmetrisch, wenn es eine Masseleitung von 1$'$ nach 2$'$ hat, wie das T-Zweitor. Erdsymmetrisch, wenn es wie die Brückenschaltung keine solche Leitung hat und spiegelbildlich zu einer Mittellinie aufgebaut ist.
--- falsch
Erdunsymmetrisch, wenn seine beiden Tore verschiedene Widerstände zeigen, wie beim T-Zweitor mit $R_\mathrm{a}\neq R_\mathrm{c}$. Erdsymmetrisch, wenn beide Tore gleich aussehen, gleich ob eine Masseleitung vorhanden ist.
--- falsch
Erdsymmetrisch, wenn es eine Masseleitung von 1$'$ nach 2$'$ hat, weil dann beide Tore dasselbe Bezugspotenzial haben. Erdunsymmetrisch, wenn diese Leitung fehlt, wie bei der Brückenschaltung.
--- falsch
Erdunsymmetrisch, wenn eine Klemme jedes Tors mit der Erde verbunden ist und die andere nicht. Erdsymmetrisch, wenn beide Klemmen jedes Tors geerdet sind und dasselbe Potenzial haben.
:::
:::karte zusammenhang Strom in der Masseleitung
Bricht ein Strom in der Masseleitung des T-Zweitors die Torbedingung, obwohl er von der Seite des einen Tors zur Seite des anderen fließt?
---
Nein. Die Torbedingung sagt nur, was an den Klemmen geschieht. Innen darf jeder Strom laufen, solange jeder Klemmenstrom an seiner Partnerklemme zurückkommt.
--- falsch
Ja. Jeder Strom von Tor zu Tor bricht die Torbedingung, deshalb ist ein Zweitor mit Masseleitung streng genommen nur näherungsweise ein Zweitor, solange dieser Strom klein bleibt.
--- falsch
Nein, weil in einer Masseleitung grundsätzlich kein Strom fließt. Sie liegt überall auf dem Potenzial null und kann deshalb keinen Strom führen.
--- falsch
Ja, aber nur, wenn dieser Strom größer ist als der Eingangsstrom. Kleinere Ströme in der Masseleitung gleichen sich an den Klemmen wieder aus.
:::
::::
