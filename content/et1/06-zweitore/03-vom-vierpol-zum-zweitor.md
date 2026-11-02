---
title: Stufe 1: Vom Vierpol zum Zweitor
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Zweitore
order: 1160300
summary: Ein Netzwerk mit vier Klemmen hat drei unabhängige Ströme und drei unabhängige Spannungen.
tags: Vierpol, Torgrößen, Vierpoltheorie, Eingang, Ausgang, Vorwärtsrichtung, Rückwärtsrichtung, Elementarzweitoren
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein Netzwerk mit vier Klemmen hat drei unabhängige Ströme und drei unabhängige Spannungen. Diese Stufe zeigt, welche Bedingung daraus zwei Ströme und zwei Spannungen macht.
:::

**Die Idee.** Ein __Vierpol__ ist ein Netzwerk mit vier Klemmen. Für das ganze Netzwerk gilt die Knotenregel ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) wie für einen großen Knoten: Ein Klemmenstrom liegt durch die drei anderen fest. Die Maschenregel bindet ebenso die Spannungen zwischen den Klemmen. Hängt nun an den Klemmen 1 und 1$'$ ein Zweipol, etwa eine Quelle, kommt eine Aussage hinzu: Ein Zweipol hat nur zwei Anschlüsse. Jede Ladung, die er an einem abgibt, nimmt er am anderen wieder auf. Der Strom, der bei Klemme 1 in das Netzwerk läuft, muss bei Klemme 1$'$ zurückkehren. Das Klemmenpaar verhält sich wie ein einziger Zugang mit einem Strom und einer Spannung (Abb. [1](#abb-1) links).

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

Ein Zweitor ist eine gedanklich geschlossene Einheit, zugänglich nur über seine Tore. Seine Eigenschaften liegen durch die Zusammenhänge zwischen den Torgrößen fest, und diese lassen sich rechnen oder messen. Meist liegt an Tor 1, dem __Eingang__, eine Quelle, an Tor 2, dem __Ausgang__, ein Verbraucher. Dann fließt Energie in __Vorwärtsrichtung__ $1\to2$, die Gegenrichtung heißt __Rückwärtsrichtung__. Das Zweitor ist eine Grundstruktur: Gesteuerte Quellen sind Zweitore, Transformator, Verstärker und Transistor haben drei oder vier Anschlüsse, große Zweitore lassen sich aus __Elementarzweitoren__ aufbauen, und zusammengefügte Zweitore bilden wieder ein Zweitor. Die einfachsten Beispiele sind Spannungsteiler und Stromteiler ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

**Aufbau und Einteilung.** Hat ein Zweitor eine durchgehende Leitung von Klemme 1$'$ nach 2$'$, die __Masseleitung__, heißt es __erdunsymmetrisch__ (Abb. [2](#abb-2) links). Es ist eigentlich ein Dreipol, ein unechter Vierpol. Netzwerkmodelle von Transistoren und Verstärkern sind von dieser Art. Ein Zweitor, das wie die Brückenschaltung keine solche Leitung besitzt und spiegelbildlich zu einer Mittellinie aufgebaut ist, heißt __erdsymmetrisch__. Nach ihrem Verhalten teilt man Zweitore in lineare zeitunabhängige, zeitabhängige und nichtlineare ein. Dieses Kapitel behandelt die linearen zeitunabhängigen.

:::abbildung et1/k6masse 2
Links: Das T-Zweitor des Rechenmodells ist erdunsymmetrisch, rot die Masseleitung von 1$'$ nach 2$'$. Rechts: Die Brückenschaltung aus zwei Widerstandspaaren hat keine durchgehende Leitung zwischen den Toren, sie ist erdsymmetrisch. Stufe [3](impedanzform-und-leerlaufversuch.html#stufe-3) rechnet beide.
:::

**Beispiel.** Im Betrieb des T-Zweitors (Stufe [4](das-zweitor-im-betrieb.html#stufe-4)) fließen $I_1=250$ mA hinein und $I_{1'}=-250$ mA, die Last entnimmt 50 mA, also $I_2=-50$ mA und $I_{2'}=+50$ mA. Die Summe in [(1.1)](#gl-1-1) ist null. **Grenzfall:** Ist Tor 2 offen, ist $I_2=I_{2'}=0$, und das Zweitor wirkt nach außen wie ein Zweipol an Tor 1.

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
