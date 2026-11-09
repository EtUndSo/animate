---
title: Von der Schwachstelle zum Schaden
pfad: Informatik / Cybersecurity / Sicherheit, Schutzziele und Spielregeln
order: 6110300
summary: Ein Schutzziel wird selten einfach so verletzt.
tags: Schwachstelle, Bedrohung, Angreifer, Angriff, Exploit, Schaden
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Ein Schutzziel wird selten einfach so verletzt. Dieser Abschnitt zerlegt den Weg dorthin in seine Glieder: eine Schwäche im System, eine Gefahr, die von außen kommt, wer sie ausführt, die Tat selbst, ihr Werkzeug und der Schaden am Ende.
:::

### Schwachstelle

<span class="anker" id="stufe-2-1"></span>

Wo kann überhaupt etwas schiefgehen? Ein Kellerfenster, das nicht richtig schließt, ist eine Schwäche des Hauses. Solange niemand vorbeikommt, passiert nichts, aber die Schwäche ist trotzdem da.

:::definition Definition 2.1 (Schwachstelle)
<span class="anker" id="satz-2-1"></span>

Eine __Schwachstelle__ (englisch *vulnerability*) ist eine Eigenschaft eines Systems, durch die ein Schutzziel verletzt werden kann.
:::

Eine Schwachstelle kann in einem Programmfehler liegen, in einer ungünstigen Einstellung oder in einer Gewohnheit der Menschen, die das System benutzen.

::::beispiel [Beispiele]
<ul>

<li>

⁠*Programmfehler:* Ein Kundenportal zeigt Rechnungen unter Adressen wie `shop.example/rechnung?nr=1041`. Es prüft, ob die Nummer existiert, aber nicht, ob die Rechnung dem angemeldeten Kunden gehört. Wer `1042` eintippt, sieht die Rechnung eines anderen.

</li>

<li>

⁠*Einstellung:* Ein Router wird mit dem ab Werk gesetzten Passwort `admin` betrieben, und seine Verwaltungsseite ist aus dem Internet erreichbar.

</li>

<li>

⁠*Gewohnheit:* Eine Person benutzt dasselbe Passwort für alle ihre Konten.

</li>

</ul>
::::

⁠**Kurz gesagt:** Eine Schwachstelle ist eine Eigenschaft des Systems, durch die ein Schutzziel verletzt werden kann.

### Bedrohung

<span class="anker" id="stufe-2-2"></span>

Eine Schwachstelle allein richtet keinen Schaden an. Gefährlich wird das offene Kellerfenster erst, wenn in der Gegend eingebrochen wird oder ein Starkregen das Wasser in den Keller drückt.

:::definition Definition 2.2 (Bedrohung)
<span class="anker" id="satz-2-2"></span>

Eine __Bedrohung__ (englisch *threat*) ist eine mögliche Verletzung eines Schutzziels. Sie kann von Menschen ausgehen, die absichtlich handeln, oder von Ereignissen ohne Absicht, etwa einem Brand, einem Stromausfall oder einem Bedienfehler.
:::

Das Wort „möglich“ ist wichtig. Eine Bedrohung muss nicht eintreten; sie beschreibt, was passieren *könnte*.

::::beispiel
Für den Router mit dem Passwort `admin` besteht die Bedrohung darin, dass Programme das Internet ständig automatisch nach Geräten mit Werkspasswörtern absuchen und sich dort anmelden. Das ist keine Theorie: 2016 übernahm ein Schadprogramm namens Mirai auf genau diese Weise Hunderttausende Kameras und Router und missbrauchte sie, um große Webdienste mit Anfragen zu überlasten.
::::

⁠**Kurz gesagt:** Eine Bedrohung ist eine mögliche Verletzung eines Schutzziels, durch Menschen oder Ereignisse.

:::hintergrund Warum man Schwachstelle und Bedrohung auseinanderhält
Die beiden Begriffe liegen auf verschiedenen Seiten einer Grenze. Die Bedrohung liegt meist außerhalb dessen, was man selbst beeinflussen kann: Einbrecher, Starkregen und Programme, die das Internet absuchen, gibt es, ob man will oder nicht. Die Schwachstelle dagegen liegt im eigenen System, und dort setzen fast alle Gegenmaßnahmen an. Man repariert das Kellerfenster; die Einbrecher abschaffen kann man nicht.

Deshalb fragt man bei der Analyse eines Systems getrennt: Welche Bedrohungen gibt es in meiner Umgebung? Welche Schwachstellen hat mein System? Gefährlich ist erst eine Bedrohung, zu der eine passende Schwachstelle gehört. Ein offenes Kellerfenster in einem Haus auf einer bewachten Insel ohne Regen ist ein kleines Problem; dasselbe Fenster in einem Viertel mit vielen Einbrüchen ist ein großes.
:::

### Angreifer

<span class="anker" id="stufe-2-3"></span>

Hinter vielen Bedrohungen steht jemand, der sie absichtlich herbeiführen will. Für ihn braucht man ein eigenes Wort, denn ein Mensch mit Absicht verhält sich anders als ein Unwetter.

:::definition Definition 2.3 (Angreifer)
<span class="anker" id="satz-2-3"></span>

Ein __Angreifer__ ist ein Mensch oder eine Gruppe, die absichtlich versucht, ein Schutzziel zu verletzen, oder ein Programm, das in ihrem Auftrag handelt.
:::

Eine Bedrohung ist also eine Möglichkeit, ein Angreifer ist jemand, der handelt. Nicht hinter jeder Bedrohung steht ein Angreifer: Ein Brand im Rechenzentrum ist eine Bedrohung für die Verfügbarkeit, aber er will nichts.

::::beispiel
Beim Router sind die Angreifer die Leute, die das Suchprogramm geschrieben haben und betreiben, um die übernommenen Geräte zu vermieten.
::::

⁠**Kurz gesagt:** Ein Angreifer ist jemand, der absichtlich ein Schutzziel verletzen will.

:::hintergrund Panne oder Angriff: warum Sicherheit schwerer ist als Zuverlässigkeit
Ingenieure schützen ihre Systeme seit jeher gegen zufällige Fehler. Ein Flugzeug-Steuerrechner wird so gebaut, dass ein gefährlicher Ausfall im Mittel erst nach $10^9$ Betriebsstunden zu erwarten ist; dann ist er für den Alltag so gut wie ausgeschlossen. Diese Rechnung beruht darauf, dass der Zufall keine Absicht hat.

Ein Angreifer dagegen hat eine. Er wartet nicht, bis die eine ungünstige Kombination zufällig eintritt, er stellt sie gezielt her, und zwar zum ungünstigsten Zeitpunkt und so oft er will. Ein Programm, das bei einer von einer Million zufälliger Eingaben abstürzt, ist im Alltag zuverlässig. Wer die eine Eingabe kennt, schickt genau diese, jedes Mal.

Das ist der eigentliche Unterschied zwischen Zuverlässigkeit (englisch *safety*) und Sicherheit (englisch *security*): Bei der Zuverlässigkeit ist der Gegner der Zufall, bei der Sicherheit ein Mensch, der nach dem schlimmsten Fall sucht. Deshalb kann man Sicherheit nicht durch Wahrscheinlichkeiten von Zufallsfehlern belegen. Man muss sich fragen, was ein Gegner *absichtlich* erreichen kann. Im Deutschen deckt das eine Wort „Sicherheit“ beide Bedeutungen ab; in diesem Kapitel ist immer die zweite gemeint.
:::

### Angriff

<span class="anker" id="stufe-2-4"></span>

Die Bedrohung ist eine Möglichkeit, der Angreifer ein Handelnder. Was noch fehlt, ist die Tat selbst.

:::definition Definition 2.4 (Angriff)
<span class="anker" id="satz-2-4"></span>

Ein __Angriff__ ist eine Handlung, mit der ein Angreifer eine Schwachstelle ausnutzt, um ein Schutzziel zu verletzen.
:::

Ein Angriff kann scheitern, etwa weil die Schwachstelle inzwischen behoben ist. Auch dann war es ein Angriff: Der Begriff beschreibt die Handlung, nicht ihren Erfolg.

::::beispiel
Das Suchprogramm findet den Router, meldet sich mit `admin` an und ändert seine Einstellungen so, dass er künftig Befehle des Angreifers ausführt.
::::

⁠**Kurz gesagt:** Ein Angriff ist die Tat, mit der ein Angreifer eine Schwachstelle ausnutzt.

### Exploit

<span class="anker" id="stufe-2-5"></span>

Wer eine Schwachstelle ausnutzen will, braucht ein konkretes Vorgehen, das genau zu ihr passt. Beim Kellerfenster ist es der Handgriff, mit dem man es mit einem Schraubenzieher an der richtigen Ecke aufhebelt.

:::definition Definition 2.5 (Exploit)
<span class="anker" id="satz-2-5"></span>

Ein __Exploit__ (von englisch *to exploit*, ausnutzen) ist das konkrete Verfahren oder Programm, mit dem eine bestimmte Schwachstelle ausgenutzt wird.
:::

Ein Exploit gehört immer zu einer bestimmten Schwachstelle. Ist sie behoben, wird er wertlos. Umgekehrt kann ein Exploit existieren, ohne dass ihn je jemand für einen Angriff benutzt.

::::beispiel [Beispiele]
<ul>

<li>

Beim Kundenportal besteht der Exploit darin, in der Adresse die Rechnungsnummer um eins zu erhöhen.

</li>

<li>

Beim Router besteht er aus einer Liste von Werkspasswörtern und einem Programm, das sie der Reihe nach ausprobiert.

</li>

</ul>
::::

⁠**Kurz gesagt:** Ein Exploit ist das Werkzeug, das zu einer bestimmten Schwachstelle passt.

### Der Schaden

<span class="anker" id="stufe-2-6"></span>

Am Ende der Kette steht, was den Verfügungsberechtigten tatsächlich trifft.

:::definition Definition 2.6 (Schaden)
<span class="anker" id="satz-2-6"></span>

Der __Schaden__ ist die tatsächliche Verletzung eines Schutzziels und alles, was daraus folgt: zum Beispiel Geldverlust, Ausfallzeit, Kosten für die Wiederherstellung oder ein beschädigter Ruf.
:::

Abbildung [2](#abb-2) setzt die Glieder zusammen. Eine Schwachstelle allein richtet keinen Schaden an, eine Bedrohung allein auch nicht. Erst wenn eine Bedrohung auf eine passende Schwachstelle trifft und ein Angriff, oder bei einer Bedrohung ohne Absicht ein Ereignis, sie ausnutzt, entsteht Schaden.

:::abbildung cyber/k1kette 2
Die Kette von der Schwachstelle zum Schaden, am Beispiel eines Hauses. Erst wenn eine Bedrohung auf eine passende Schwachstelle trifft und ein Angriff sie mit einem Exploit ausnutzt, entsteht ein Schaden.
:::

Weil es eine Kette ist, kann man sie an jedem Glied unterbrechen: das Fenster reparieren (Schwachstelle), einen Zaun bauen, der Einbrecher fernhält (Bedrohung), eine Alarmanlage einbauen, die den Einstieg meldet (Angriff), den Laptop in einen Tresor legen (Schaden).

::::beispiel
Beim Router besteht der Schaden für den Besitzer zuerst in einem verlangsamten Internetanschluss. Schwerer wiegt, dass Angriffe auf andere von seinem Anschluss ausgehen und zunächst zu ihm zurückverfolgt werden.
::::

⁠**Kurz gesagt:** Ein Schaden entsteht, wenn eine Bedrohung auf eine passende Schwachstelle trifft und ausgenutzt wird; jede Gegenmaßnahme unterbricht ein Glied dieser Kette.

:::aufgabe Aufgabe 3 ★ Die Kette zerlegen
<span class="anker" id="aufg-3"></span>

Nenne für jeden Fall Schwachstelle, Bedrohung, Angreifer (falls es einen gibt), Angriff, Exploit (falls es einen gibt), Schaden und die verletzten Schutzziele.

<ol class="al">

<li>

Eine Kundin des Kundenportals aus diesem Abschnitt ändert aus Neugier die Rechnungsnummer in der Adresszeile und sieht Name, Anschrift und Einkäufe eines anderen Kunden.

</li>

<li>

Ein Server steht in einem Kellerraum ohne Abfluss. Nach einem Starkregen steht das Wasser 20 cm hoch, der Server fällt aus, die letzte Sicherungskopie ist drei Wochen alt.

</li>

<li>

Ein Angreifer schickt den Mitarbeitern einer Firma eine E-Mail im Namen der IT-Abteilung und bittet um das Passwort „zur Umstellung des Postfachs“. Zwei Mitarbeiter antworten. Mit ihren Konten liest er eine Woche lang die Geschäftspost mit.

</li>

<li>

In welchem Fall gibt es keinen Angreifer und keinen Exploit? Welche Begriffe der Kette braucht man dann trotzdem?

</li>

</ol>

:::loesung
(a) Schwachstelle: Das Portal prüft nicht, wem eine Rechnung gehört (fehlende Prüfung). Bedrohung: Neugierige oder böswillige Kunden rufen fremde Rechnungen ab. Angreifer: die Kundin; sie handelt absichtlich, wenn auch aus Neugier. Angriff: das Abrufen der fremden Rechnung. Exploit: die Nummer in der Adresse um eins erhöhen. Schaden: Name, Anschrift und Einkäufe eines anderen Kunden sind bekannt geworden; für den Shop drohen Meldepflichten und Ansehensverlust. Verletzt: Vertraulichkeit.

(b) Schwachstelle: Serverraum ohne Abfluss im Keller, dazu eine veraltete Sicherungskopie. Bedrohung: Starkregen. Angreifer: keiner. Angriff: keiner; an seine Stelle tritt das Ereignis, das eindringende Wasser. Exploit: keiner. Schaden: Ausfall des Servers und drei Wochen verlorene Arbeit. Verletzt: Verfügbarkeit, durch die verlorenen Daten auch Integrität (der Datenbestand ist nicht mehr vollständig).

(c) Schwachstelle: Mitarbeiter, die Passwörter auf Anfrage per E-Mail herausgeben (Gewohnheit), dazu fehlende Prüfung des Absenders. Bedrohung: Phishing gegen die Belegschaft. Angreifer: der Absender der E-Mail. Angriff: die gefälschte Bitte um das Passwort und danach die Anmeldung mit den erbeuteten Daten. Exploit: die glaubwürdige E-Mail im Namen der IT-Abteilung. Schaden: eine Woche mitgelesene Geschäftspost. Verletzt: zuerst Authentizität (die E-Mail), dann Vertraulichkeit (die Post).

(d) Im Fall (b). Die Begriffe Schwachstelle, Bedrohung und Schaden braucht man trotzdem: Auch ohne Angreifer trifft eine Bedrohung auf eine Schwachstelle, und an die Stelle des Angriffs tritt das Ereignis. Deshalb ist eine Bedrohung als *mögliche Verletzung* definiert und nicht als Angreifer; Zufall und Natur gehören ebenso dazu.
:::
:::
