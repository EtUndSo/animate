---
title: Richtlinie und Mechanismus
pfad: Informatik / Cybersecurity / Sicherheit, Schutzziele und Spielregeln
adresse: informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln
knoten: Kapitel 1: Sicherheit, Schutzziele und Spielregeln
order: 6110500
summary: Bisher war offen, wer festlegt, was erlaubt ist, und womit das durchgesetzt wird.
tags: Sicherheitsrichtlinie, Sicherheitsmechanismus, Verhindern, Erkennen, Wiederherstellen, passiver Angriff, aktiver Angriff
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Bisher war offen, wer festlegt, was erlaubt ist, und womit das durchgesetzt wird. Dieser Abschnitt trennt beides, zeigt, was ein Schutzmechanismus leisten kann, und unterscheidet Angriffe danach, ob sie etwas verändern.
:::

### Sicherheitsrichtlinie

<span class="anker" id="stufe-4-1"></span>

„Sicher“ kann ein System nur in Bezug auf eine Vorgabe sein. Solange niemand aufgeschrieben hat, was erlaubt ist, kann man auch nicht sagen, ob etwas Unerlaubtes passiert ist.

:::definition Definition 4.1 (Sicherheitsrichtlinie)
<span class="anker" id="satz-4-1"></span>

Eine __Sicherheitsrichtlinie__ (englisch *security policy*) ist eine Festlegung dessen, was in einem System erlaubt ist und was nicht: wer welche Handlung mit welchem Schutzgut ausführen darf.
:::

Mit diesem Begriff lässt sich genau sagen, was „sicher“ bedeutet. Die Richtlinie teilt alle Zustände, in die ein System geraten kann, in erlaubte und verbotene. Ein System ist in Bezug auf seine Richtlinie *sicher*, wenn es in einem erlaubten Zustand beginnt und nie in einen verbotenen gelangen kann.

::::beispiel
Eine Hochschule legt für ihr Notensystem fest:

<ul>

<li>

Nur das Prüfungsamt darf Noten eintragen und ändern.

</li>

<li>

Jede Studentin und jeder Student darf die eigenen Noten lesen, aber keine fremden.

</li>

<li>

Prüferinnen und Prüfer dürfen die Noten ihrer eigenen Prüfungen lesen.

</li>

</ul>

Ein Zustand, in dem ein Student eine fremde Note gelesen oder seine eigene geändert hat, ist verboten.
::::

⁠**Kurz gesagt:** Eine Sicherheitsrichtlinie legt fest, was erlaubt ist; „sicher“ heißt, dass nie ein verbotener Zustand eintritt.

### Sicherheitsmechanismus

<span class="anker" id="stufe-4-2"></span>

Eine Richtlinie ist zunächst nur Papier. Damit sie gilt, braucht es etwas, das sie durchsetzt.

:::definition Definition 4.2 (Sicherheitsmechanismus)
<span class="anker" id="satz-4-2"></span>

Ein __Sicherheitsmechanismus__ ist ein Verfahren, ein Werkzeug oder eine Vorgehensweise, die eine Sicherheitsrichtlinie oder einen Teil davon durchsetzt.
:::

Mechanismen müssen nicht technisch sein. Eine Anmeldung mit Passwort ist ein Mechanismus, aber auch eine abgeschlossene Bürotür oder die Anweisung, sich am Telefon erst auszuweisen, bevor man ein neues Passwort bekommt.

::::beispiel
Im Notensystem setzt die Anmeldung mit Benutzername und Passwort durch, dass das System weiß, wer vor ihm sitzt. Eine Rechteverwaltung setzt durch, dass Studierende nur ihre eigenen Noten sehen und nur Konten des Prüfungsamts Noten ändern können.
::::

Eine Richtlinie gilt auch dort, wo kein Mechanismus sie durchsetzt. Lässt eine Mitarbeiterin des Prüfungsamts ihren Rechner angemeldet und unbeaufsichtigt, und ein Student ändert dort seine Note, so hat kein Mechanismus das verhindert. Ein Verstoß gegen die Richtlinie ist es trotzdem.

Mit den beiden Begriffen lassen sich auch Schwachstellen genauer fassen. Eine Schwachstelle sitzt entweder im Mechanismus, der die Richtlinie an einer Stelle nicht durchsetzt, oder in der Richtlinie selbst, die mehr erlaubt, als beabsichtigt war.

⁠**Kurz gesagt:** Ein Sicherheitsmechanismus setzt die Richtlinie durch; ein Verstoß bleibt ein Verstoß, auch wenn kein Mechanismus ihn verhindert hat.

:::hintergrund Warum man Richtlinie und Mechanismus trennt
Die Richtlinie beantwortet die Frage *was*, der Mechanismus die Frage *wie*. Diese Trennung hat drei Vorteile.

⁠**Man kann den Mechanismus beurteilen.** Ob ein Mechanismus gut ist, lässt sich nur im Vergleich mit einer Richtlinie sagen. Ein Schloss, das nur Bewohner hereinlässt, ist für ein Wohnhaus richtig und für ein Geschäft falsch. Ohne die Richtlinie gibt es keinen Maßstab.

⁠**Man kann den Mechanismus austauschen.** Die Richtlinie „nur das Prüfungsamt ändert Noten“ gilt seit Jahrzehnten. Durchgesetzt wurde sie erst mit einem abgeschlossenen Aktenschrank, dann mit Passwörtern, heute vielleicht mit einer Chipkarte. Die Richtlinie musste dafür nicht geändert werden.

⁠**Man sieht, was keiner durchsetzt.** Legt man Richtlinie und Mechanismen nebeneinander, fallen die Stellen auf, an denen eine Regel steht, aber nichts sie durchsetzt. Genau dort liegen Schwachstellen. Zusammen mit dem Angreifermodell aus Abschnitt [3](risiko-angreifermodell-und-angriffsflache.html#stufe-3) ergeben sich die drei Fragen, mit denen man jedes System untersucht: Was soll gelten (Richtlinie)? Gegen wen (Angreifermodell)? Womit (Mechanismus)?
:::

### Verhindern, erkennen, wiederherstellen

<span class="anker" id="stufe-4-3"></span>

Ein Haus wird auf drei verschiedene Arten geschützt: Das Schloss soll den Einbruch verhindern. Die Alarmanlage verhindert ihn nicht, aber sie meldet ihn. Und die Hausratversicherung ersetzt nach dem Einbruch, was fehlt. Dieselben drei Arten gibt es bei jedem Sicherheitsmechanismus.

:::definition Definition 4.3 (Ziele eines Sicherheitsmechanismus)
<span class="anker" id="satz-4-3"></span>

Ein Sicherheitsmechanismus kann eines von drei Zielen verfolgen:

<ul>

<li>

__Verhindern__: Er sorgt dafür, dass ein Angriff scheitert.

</li>

<li>

__Erkennen__: Er stellt fest, dass ein Angriff stattfindet oder stattgefunden hat, und meldet ihn.

</li>

<li>

__Wiederherstellen__: Er beendet die Folgen eines Angriffs und bringt das System in einen erlaubten Zustand zurück.

</li>

</ul>
:::

Das wichtigste Werkzeug zum Wiederherstellen von Daten ist die Sicherungskopie aus Abschnitt [1](was-geschutzt-wird-schutzgut-und-schutzziele.html#stufe-1).

Daraus folgt der Grundsatz __erkennen, wenn man nicht verhindern kann__. Lässt sich ein Angriff nicht oder nur zu unvertretbaren Kosten verhindern, so soll man ihn wenigstens bemerken, um rechtzeitig zu reagieren und den Schaden zu begrenzen. Ein Angriff, den niemand bemerkt, kann beliebig lange weiterlaufen.

::::beispiel ein Online-Bankkonto
<ul>

<li>

Verhindern: Für eine Überweisung braucht man das Passwort und eine Bestätigung auf dem Handy.

</li>

<li>

Erkennen: Die Bank schickt bei jeder Anmeldung von einem neuen Gerät eine Nachricht. Die Kontoinhaberin bemerkt einen Fremden auch dann, wenn er beides überwunden hat.

</li>

<li>

Wiederherstellen: Eine betrügerische Überweisung kann die Bank in vielen Fällen zurückholen, und die Kontoinhaberin bekommt neue Zugangsdaten. Danach muss die Schwachstelle beseitigt werden, über die der Fremde hereinkam; sonst kommt er wieder.

</li>

</ul>
::::

⁠**Kurz gesagt:** Mechanismen verhindern, erkennen oder stellen wieder her; wer nicht verhindern kann, soll wenigstens erkennen.

:::hintergrund Welche Größe des Risikos jedes der drei Ziele verkleinert
Mit der Formel $R=H\cdot S$ aus Abschnitt [3](risiko-angreifermodell-und-angriffsflache.html#stufe-3) lassen sich die drei Ziele genau unterscheiden. Ein Mechanismus, der *verhindert*, senkt die Häufigkeit $H$: Weniger Angriffe gelingen. Ein Mechanismus, der *erkennt*, hält den einzelnen Angriff nicht auf und ändert an $H$ zunächst nichts. Er verkürzt aber die Zeit, in der ein Angreifer unbemerkt weitermachen kann, und senkt damit den Schaden $S$ je Ereignis: Wer nach einer Stunde bemerkt wird, liest eine Stunde lang mit, nicht eine Woche. Ein Mechanismus, der *wiederherstellt*, senkt ebenfalls $S$, aber erst nach der Tat: Mit einer Sicherungskopie kostet ein Datenverlust nur die Arbeit seit der letzten Kopie. In Aufgabe [4](risiko-angreifermodell-und-angriffsflache.html#aufg-4) senkt die Sicherungskopie den Schaden einer Erpressung von 120 000 auf 20 000 €, ohne dass ein einziger Angriff seltener wird.

Daraus folgt, warum man alle drei braucht. Wer sich nur auf das Verhindern verlässt, braucht einen vollkommenen Mechanismus, und den gibt es nicht; jeder Angriff, der doch durchkommt, richtet dann den vollen Schaden an. Erkennen und Wiederherstellen setzen genau dort an, wo das Verhindern versagt hat.
:::

### Passiver und aktiver Angriff

<span class="anker" id="stufe-4-4"></span>

Manche Angreifer wollen nur etwas erfahren, andere wollen etwas verändern. Das macht einen großen Unterschied dafür, welches der drei Ziele aus dem letzten Unterabschnitt gegen sie hilft.

:::definition Definition 4.4 (Passiver und aktiver Angriff)
<span class="anker" id="satz-4-4"></span>

Ein __passiver Angriff__ beobachtet nur, ohne etwas zu verändern, zum Beispiel durch Mithören oder Mitlesen.

Ein __aktiver Angriff__ verändert etwas: Er fälscht oder löscht Daten, schleust Nachrichten ein oder legt einen Dienst lahm.
:::

Passive Angriffe richten sich gegen die Vertraulichkeit. Aktive Angriffe richten sich gegen die Integrität, die Authentizität oder die Verfügbarkeit.

::::beispiel das Funknetz im Café
Ein Gast zeichnet mit seinem Laptop alles auf, was über das Funknetz geht, und liest unverschlüsselte Nachrichten der anderen Gäste. Das ist ein passiver Angriff. Ein anderer stellt einen eigenen Zugangspunkt mit demselben Netznamen auf, die Geräte der Gäste verbinden sich mit ihm, und er leitet ihren Verkehr um und verändert ihn. Das ist ein aktiver Angriff.
::::

Für die Verteidigung folgt daraus eine Faustregel. Ein passiver Angriff hinterlässt keine Spuren; man kann ihn kaum erkennen und muss ihn deshalb *verhindern*, etwa indem man die Nachrichten verschlüsselt, sodass Mithören nichts nützt. Ein aktiver Angriff muss etwas verändern und hinterlässt dabei Spuren; man kann ihn *erkennen*, auch wenn man ihn nicht immer ganz verhindern kann.

⁠**Kurz gesagt:** Passive Angriffe beobachten und müssen verhindert werden; aktive Angriffe verändern und lassen sich erkennen.

:::hintergrund Warum Mithören keine Spuren hinterlässt
Ein Funknetz verhält sich wie eine Durchsage in einer Bahnhofshalle. Die Durchsage erreicht jeden in Hörweite, und wer zuhört, nimmt dem Lautsprecher nichts weg: Der Sprecher klingt für die anderen genauso laut, ob niemand, einer oder hundert Menschen mithören. Ebenso breiten sich die Funkwellen eines WLAN-Routers im ganzen Raum aus, und ein zusätzliches Gerät, das sie empfängt, ändert für den Sender und den rechtmäßigen Empfänger nichts Messbares. Deshalb kann man passives Mithören grundsätzlich nicht zuverlässig bemerken; man muss davon ausgehen, dass jede Funkübertragung mitgehört werden kann.

Ein aktiver Angriff dagegen muss etwas in die Welt setzen: ein gefälschtes Paket, einen zweiten Sender, eine veränderte Datei. Was in die Welt gesetzt wird, kann man messen, vergleichen und protokollieren. Darauf beruhen alle Verfahren, die aktive Angriffe erkennen, vom Siegel auf dem Brief bis zu Prüfsummen über Dateien.
:::

:::aufgabe Aufgabe 7 ★ Richtlinie, Mechanismus und ihre Ziele
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Richtlinie oder Mechanismus? (1) „Gäste dürfen das Internet nutzen, aber nicht auf den Drucker zugreifen.“ (2) Das Gäste-WLAN ist vom Firmennetz getrennt. (3) Jede Nacht wird eine Sicherungskopie auf ein Band geschrieben, das im Tresor liegt. (4) „Kundendaten dürfen nur auf Rechnern der Firma gespeichert werden.“ (5) Jede Anmeldung am Server wird mit Uhrzeit und Benutzername festgehalten.

</li>

<li>

Ordne jedem Mechanismus aus (a) das Ziel zu, das er verfolgt: verhindern, erkennen oder wiederherstellen.

</li>

<li>

Passiv oder aktiv? (1) Jemand zeichnet die Funksignale einer Funkmaus auf, um die Klicks nachzuvollziehen. (2) Jemand ändert in einer Datei auf dem Server einen Preis. (3) Jemand überlastet die Webseite eines Konkurrenten mit Anfragen.

</li>

</ol>

:::loesung
(a) (1) Richtlinie. (2) Mechanismus. (3) Mechanismus. (4) Richtlinie. (5) Mechanismus.

(b) (2) verhindern: Gäste können den Drucker nicht erreichen. (3) wiederherstellen: Nach einem Verlust holt man den Stand der letzten Nacht zurück; weil das Band im Tresor liegt, übersteht es auch einen Angriff auf den Server. (5) erkennen: Aus den Aufzeichnungen sieht man unerwartete Anmeldungen, verhindert werden sie dadurch nicht.

(c) (1) passiv: Das Aufzeichnen verändert nichts. (2) aktiv: Ein Wert wird verändert. (3) aktiv: Ein Dienst wird lahmgelegt.
:::
:::
