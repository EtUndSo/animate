---
title: Offenlegung und Ethik
pfad: Informatik / Cybersecurity / Sicherheit, Schutzziele und Spielregeln
adresse: informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln
knoten: Kapitel 1: Sicherheit, Schutzziele und Spielregeln
order: 6111100
summary: Was tut man, wenn man eine Schwachstelle gefunden hat?
tags: Domain, Pfad, koordinierten Offenlegung, Koordinator, Full Disclosure, Proof of Concept, Meldeprogramm, Bug-Bounty-Programm
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Was tut man, wenn man eine Schwachstelle gefunden hat? Dieser Abschnitt beschreibt den verantwortungsvollen Weg von der Entdeckung bis zur Veröffentlichung, die Datei, über die eine Organisation ihren Sicherheitskontakt nennt, die Ethik der Sicherheitsforschung und schließlich die Regeln, unter denen in dieser Reihe geübt wird.
:::

### Was du dafür brauchst: der Aufbau einer Webadresse

<span class="anker" id="stufe-10-1"></span>

Meldungen, Erlaubnisse und Kontaktangaben im Netz beziehen sich auf Adressen von Webseiten. Wer sie lesen will, muss wissen, aus welchen Teilen eine solche Adresse besteht.

Eine Adresse wie `https://app.example.com/konto/rechnungen` besteht aus drei Teilen. Vorn steht das Verfahren, mit dem der Browser die Seite abruft, hier `https`. Danach folgt der Name des Rechners, die __Domain__, hier `app.example.com`. Der Rest, beginnend mit dem ersten einzelnen Schrägstrich, ist der __Pfad__: Er bezeichnet, welche Datei oder Seite auf diesem Rechner gemeint ist, hier `/konto/rechnungen`.

Eine Domain wird von rechts nach links gelesen. `example.com` ist der Name, den eine Organisation registriert hat. Davor kann sie weitere Namen setzen, etwa `app.example.com` und `intern.example.com`; das sind verschiedene Rechner oder Dienste derselben Organisation.

::::beispiel
In `https://www.example.org/hilfe/kontakt.html` ist das Verfahren `https`, die Domain `www.example.org` und der Pfad `/hilfe/kontakt.html`. Hängt man an dieselbe Domain einen anderen Pfad, etwa `/impressum.html`, so fragt man denselben Rechner nach einer anderen Seite.
::::

⁠**Kurz gesagt:** Eine Webadresse besteht aus dem Verfahren, der Domain, die den Rechner nennt, und dem Pfad, der die Seite auf diesem Rechner nennt.

### Koordinierte Offenlegung

<span class="anker" id="stufe-10-2"></span>

Wer eine Schwachstelle findet, steht vor einem Dilemma. Schweigt er, bleibt die Lücke offen, und vielleicht kennt ein Angreifer sie längst. Veröffentlicht er sie sofort, erfahren alle Angreifer davon, bevor es einen Patch gibt.

:::definition Definition 10.1 (Koordinierte Offenlegung)
<span class="anker" id="satz-10-1"></span>

Bei der __koordinierten Offenlegung__ (englisch *coordinated vulnerability disclosure*, CVD) meldet der Finder eine Schwachstelle vertraulich dem Hersteller oder Betreiber. Beide stimmen ab, wann und wie die Lücke öffentlich wird, in der Regel erst, wenn ein Patch verfügbar ist. Bei Bedarf vermittelt eine dritte Stelle, ein __Koordinator__.
:::

Den Gegenentwurf, die sofortige vollständige Veröffentlichung, nennt man __Full Disclosure__. Sie war lange ein Druckmittel gegen Hersteller, die gemeldete Lücken jahrelang ignorierten. Abbildung [17](#abb-17) zeigt die Beteiligten der koordinierten Offenlegung.

:::abbildung cyber/k1offenlegung 17
Die Beteiligten der koordinierten Offenlegung. Der Finder meldet vertraulich an den Hersteller; reagiert dieser nicht, vermittelt ein Koordinator. Öffentlich wird die Lücke erst, wenn ein Patch bereitsteht.
:::

Eine gute Meldung nennt das Produkt und die getestete Version, beschreibt die Schwachstelle so, dass der Hersteller sie nachvollziehen kann, ordnet sie einer CWE-Nummer zu und schätzt ihre Schwere nach CVSS ein. Oft gehört ein __Proof of Concept__ dazu: ein Exploit, der nur zeigen soll, dass die Lücke ausnutzbar ist, ohne Schaden anzurichten.

Damit ein Hersteller eine Meldung nicht endlos liegen lässt, setzen viele Finder Fristen. Ein bekanntes Beispiel ist das Sicherheitsteam Project Zero von Google: Der Hersteller hat 90 Tage Zeit für einen Patch, und 30 Tage nach dem Patch werden die Einzelheiten veröffentlicht. Wird die Lücke nachweislich schon ausgenutzt, verkürzt sich die Frist auf sieben Tage.

::::beispiel der Weg über das BSI
Das BSI nimmt Meldungen über Schwachstellen entgegen. Betrifft die Lücke ein Produkt eines Herstellers, meldet man sie zuerst dem Hersteller. Nur wenn dieser nicht reagiert oder die Abstimmung zu scheitern droht, wendet man sich an das BSI, das dann vermittelt. Für Schwachstellen in Systemen der Bundesverwaltung ist das BSI selbst der Ansprechpartner. Es sagt zu, Meldungen vertraulich zu behandeln, und verspricht, keine strafrechtlichen Schritte gegen den Finder einzuleiten, solange dieser sich an die Regeln des BSI hält, etwa nichts über den Nachweis hinaus ausnutzt, keine Daten Dritter verändert und keine Überlastungsangriffe ausführt. Diese Zusage bindet nur das BSI selbst; sie ist keine Erlaubnis für Systeme anderer Betreiber.
::::

⁠**Kurz gesagt:** Bei der koordinierten Offenlegung meldet der Finder vertraulich und veröffentlicht erst nach Abstimmung, in der Regel, wenn ein Patch bereitsteht.

:::hintergrund Warum koordiniert und nicht sofort oder nie
Die koordinierte Offenlegung ist ein Kompromiss zwischen zwei Gefahren, und beide lassen sich in Zahlen fassen. Veröffentlicht man vor dem Patch, so wächst die Zahl der Angriffe auf die Lücke, wie der Abschnitt über den Lebenszyklus gezeigt hat, um Größenordnungen, während sich noch niemand schützen kann. Schweigt man dagegen ganz, so hat der Hersteller keinen Grund zur Eile, und Angreifer, die die Lücke ebenfalls kennen, nutzen sie weiter. Eine Untersuchung des Patchverhaltens großer Hersteller fand, dass die Bereitschaft, einen Patch herauszugeben, nach einer Veröffentlichung um fast das Zweieinhalbfache stieg. Die Aussicht auf Veröffentlichung wirkt also.

Die Frist verbindet beides: Sie lässt dem Hersteller Zeit für einen Patch, und sie sorgt dafür, dass die Lücke nicht für immer verschwiegen wird. Das amerikanische Koordinationszentrum CERT/CC, das solche Verfahren seit Jahrzehnten vermittelt, fasst die Haltung dahinter in Grundsätzen zusammen: den Schaden verringern, dem Meldenden gute Absicht unterstellen, Überraschungen vermeiden, erwünschtes Verhalten belohnen statt unerwünschtes zu bestrafen, die üblichen Regeln der Berufsethik einhalten und das Verfahren nach jedem Fall verbessern.
:::

### Meldeprogramme und Bug-Bounty

<span class="anker" id="stufe-10-3"></span>

Viele Organisationen warten nicht, bis jemand zufällig eine Lücke meldet; sie laden ausdrücklich dazu ein.

:::definition Definition 10.2 (Meldeprogramm, Bug-Bounty)
<span class="anker" id="satz-10-2"></span>

Ein __Meldeprogramm__ (englisch *vulnerability disclosure program*, VDP) ist eine veröffentlichte Regelung einer Organisation, die beschreibt, wie man ihr Schwachstellen meldet, welche Systeme und welche Tests dabei erlaubt sind und wie sie mit Meldungen umgeht. Ein __Bug-Bounty-Programm__ ist ein Meldeprogramm, das für gültige Meldungen eine Prämie zahlt.
:::

Ein solches Programm legt einen Umfang fest, wie ihn Abschnitt [9](erlaubnis-werkzeuge-und-gute-absicht.html#stufe-9) beschrieben hat: welche Adressen getestet werden dürfen und welche Methoden verboten sind, fast immer Überlastungsangriffe und das Täuschen von Mitarbeitern. Viele Programme sagen außerdem ausdrücklich zu, gegen Finder, die sich an die Regeln halten, nicht rechtlich vorzugehen. Damit erteilt der Verfügungsberechtigte eine Erlaubnis für genau die beschriebenen Tests. Was außerhalb des Umfangs liegt, bleibt unbefugt.

::::beispiel
Ein Programm erlaubt Tests an `app.example.com`, verbietet aber Tests an `intern.example.com` und jede Form von Überlastung. Ein Finder, der auf `app.example.com` eine Lücke findet und meldet, handelt im Rahmen der Erlaubnis. Untersucht er auch `intern.example.com`, weil es „ja zur selben Firma gehört“, verlässt er sie.
::::

⁠**Kurz gesagt:** Meldeprogramme und Bug-Bounty-Programme erlauben Tests in einem festgelegten Umfang; außerhalb davon gilt die Erlaubnis nicht.

### security.txt

<span class="anker" id="stufe-10-4"></span>

Wer eine Lücke in einer Webseite findet, muss wissen, an wen er sie melden soll. Auf vielen Webseiten ist dieser Kontakt schwer zu finden, und eine Meldung an die allgemeine Kundenhotline geht leicht verloren.

:::definition Definition 10.3 (security.txt)
<span class="anker" id="satz-10-3"></span>

Eine __security.txt__ ist eine kurze Textdatei, in der eine Organisation angibt, wie man ihr Sicherheitsprobleme meldet. Sie liegt nach dem Standard RFC 9116 immer unter demselben Pfad, `/.well-known/security.txt`, und wird über `https` abgerufen. Jede Zeile hat die Form `Feldname: Wert`. Zwei Felder sind Pflicht:

<ul>

<li>

`Contact`: ein Kontakt für Meldungen, etwa eine E-Mail-Adresse oder eine Webseite. Das Feld darf mehrfach vorkommen, in der Reihenfolge der Vorliebe.

</li>

<li>

`Expires`: das Datum, ab dem die Angaben nicht mehr als gültig gelten sollen. Es kommt genau einmal vor und soll weniger als ein Jahr in der Zukunft liegen.

</li>

</ul>

Freiwillig sind unter anderem `Policy` (ein Verweis auf die Regeln des Meldeprogramms), `Encryption` (ein Schlüssel, mit dem man die Meldung verschlüsseln kann), `Acknowledgments` (eine Seite, die Finder namentlich dankt) und `Preferred-Languages` (die Sprachen, in denen man Meldungen bevorzugt).
:::

::::beispiel
Die security.txt einer erfundenen Firma `example.org` könnte so aussehen; Zeilen, die mit `#` beginnen, sind Kommentare.

```text https://example.org/.well-known/security.txt
# Meldungen über Schwachstellen bitte an:
Contact: mailto:security@example.org
Contact: https://example.org/sicherheit/meldung
Expires: 2027-06-30T23:00:00Z
Preferred-Languages: de, en
Policy: https://example.org/sicherheit/meldeprogramm
```

Eine Meldung geht hier zuerst an `security@example.org`. Die Angaben gelten bis zum 30. Juni 2027, Meldungen auf Deutsch oder Englisch sind willkommen, und die Regeln des Meldeprogramms stehen auf der angegebenen Seite. Eine security.txt abzurufen ist ein gewöhnlicher Seitenabruf, wie ihn jeder Browser bei jedem Klick ausführt.
::::

⁠**Kurz gesagt:** Die security.txt unter `/.well-known/security.txt` nennt den Sicherheitskontakt einer Webseite; Pflicht sind `Contact` und `Expires`.

:::hintergrund Warum ein fester Ort und ein Ablaufdatum
Ein fester Ort spart die Suche. Wer eine Lücke meldet, soll nicht erst die Webseite durchforsten müssen; er hängt an jede Domain denselben Pfad an und weiß sofort, ob es einen Kontakt gibt. Damit sich solche festen Orte nicht mit gewöhnlichen Seiten einer Webseite überschneiden, hat die Internet-Normungsorganisation IETF für sie einen eigenen Bereich reserviert, den Pfad `/.well-known/`; jeder Name darunter wird in einer öffentlichen Liste eingetragen.

Das Pflichtfeld `Expires` löst ein Problem, das bei Kontaktangaben ständig auftritt: Sie veralten. Die Mitarbeiterin, deren Adresse darin steht, wechselt die Stelle, das Postfach wird abgeschaltet, und Meldungen verschwinden ungelesen. Eine veraltete Kontaktangabe ist schlimmer als keine, weil der Finder glaubt, gemeldet zu haben. Das Ablaufdatum zwingt die Organisation, die Datei regelmäßig zu prüfen, und es sagt dem Finder, ob er den Angaben noch trauen kann. Halten sich nicht alle daran, ist das ein Hinweis darauf, die Angaben im Zweifel zu überprüfen.
:::

### Was man bei einem Zufallsfund tut

<span class="anker" id="stufe-10-5"></span>

Lücken findet man nicht nur, wenn man sie sucht. Manchmal sieht man beim gewöhnlichen Benutzen einer Webseite oder eines Geräts, dass etwas nicht stimmt.

:::definition Definition 10.4 (Vorgehen bei einem Zufallsfund)
<span class="anker" id="satz-10-4"></span>

Bemerkt man bei der gewöhnlichen, erlaubten Benutzung eines fremden Systems Hinweise auf eine Schwachstelle, so geht man so vor:

<ol>

<li>

⁠**Aufhören.** Man probiert nichts weiter aus, ruft keine fremden Daten ab und versucht nicht, die Lücke zu bestätigen.

</li>

<li>

⁠**Nichts mitnehmen, nichts verändern.** Man lädt nichts herunter und ändert nichts.

</li>

<li>

⁠**Aufschreiben.** Man notiert, was man wann und wie bemerkt hat, so genau wie möglich.

</li>

<li>

⁠**Koordiniert melden.** Man sucht den Sicherheitskontakt, etwa über die security.txt, und meldet die Beobachtung vertraulich; reagiert niemand, wendet man sich an einen Koordinator wie das BSI.

</li>

<li>

⁠**Schweigen bis zur Abstimmung.** Man veröffentlicht nichts, bevor die Lücke behoben oder eine Veröffentlichung abgestimmt ist.

</li>

</ol>
:::

::::beispiel
Beim Ansehen der eigenen Rechnung im Kundenportal aus Abschnitt [2](von-der-schwachstelle-zum-schaden.html#stufe-2) fällt einer Kundin auf, dass die Adresse eine fortlaufende Nummer enthält. Sie probiert die Nummer 1042 *nicht* aus. Sie schreibt dem Sicherheitskontakt des Shops: „In der Adresse meiner Rechnung steht eine fortlaufende Nummer. Bitte prüfen Sie, ob das Portal bei jedem Abruf kontrolliert, wem die Rechnung gehört; andernfalls könnten Kunden fremde Rechnungen sehen.“ Damit hat sie geholfen, ohne ein fremdes Schutzgut anzutasten.
::::

⁠**Kurz gesagt:** Bei einem Zufallsfund hört man auf, nimmt nichts mit, schreibt auf und meldet koordiniert.

:::hintergrund Warum man eine Lücke nicht selbst beweisen muss
Der Betreiber kann das, was der Finder vermutet, selbst und erlaubt prüfen. Er hat Zugang zu seinem System, er kann eigene Testkonten anlegen und in seinen Protokollen nachsehen, und er darf die Daten seiner Kunden ansehen. Eine gut beschriebene Beobachtung zu prüfen, kostet ihn oft nur Minuten.

Der Finder dagegen kann eine Lücke in einem fremden System nur bestätigen, indem er genau das tut, wovor die Lücke schützen soll: fremde Daten abrufen. Dieser Beweis kann selbst strafbar sein, er trifft gerade die Menschen, deren Daten geschützt werden sollen, und er liefert dem Betreiber kaum mehr als die genaue Beschreibung. Deshalb teilt man die Arbeit: Der Finder beobachtet und beschreibt, der Betreiber prüft und behebt.
:::

### Hackerethik

<span class="anker" id="stufe-10-6"></span>

Das Wort „Hacker“ hat in der Öffentlichkeit einen schlechten Klang. Ursprünglich meinte es etwas anderes: jemanden, der technische Systeme mit Neugier und Einfallsreichtum bis ins Letzte verstehen will und sie dabei oft anders benutzt, als ihre Erbauer es vorgesehen hatten. Kriminelle Angreifer sind nur ein kleiner Teil derer, auf die das zutrifft.

:::definition Definition 10.5 (Hackerethik)
<span class="anker" id="satz-10-5"></span>

Die __Hackerethik__ ist eine Sammlung von Grundsätzen, mit denen sich die Hacker-Szene selbst Regeln gibt. In Deutschland verbreitet ist die Fassung des Chaos Computer Clubs (CCC) mit acht Grundsätzen. Sechs davon stammen aus der Kultur früher Programmierer an amerikanischen Universitäten; zwei hat der CCC in den 1980er-Jahren ergänzt:

<ul>

<li>

„Mülle nicht in den Daten anderer Leute.“

</li>

<li>

„Öffentliche Daten nützen, private Daten schützen.“

</li>

</ul>
:::

Die Hackerethik ist eine freiwillige Selbstverpflichtung und keine Rechtsgrundlage. Wer sich auf sie beruft, ist dadurch nicht befugt. Umgekehrt ist nicht alles anständig, was erlaubt ist: Das Recht zieht nur die äußere Grenze. Auch eine erlaubte Handlung, etwa das Veröffentlichen einer Lücke nach Ablauf einer Frist, kann Menschen schaden, wenn man sie rücksichtslos ausführt. Ein anderer ihrer Grundsätze lautet „Alle Informationen müssen frei sein“. Er ist eine Haltung zum freien Austausch von Wissen und kein Freibrief, in fremde Systeme einzudringen; mit den beiden ergänzten Grundsätzen und mit dem Strafrecht steht er in einer Spannung, über die man nachdenken sollte.

Ein Gedanke aus dieser Kultur trägt die ganze Reihe: Wer Angriffe versteht, kann sich gegen sie verteidigen, und wer die Frage nach Angriffen unterdrückt, beseitigt damit keine einzige Lücke. Am Wissen selbst ist nichts gut oder schlecht; gut oder schlecht ist, was man damit tut. Das ist derselbe Gedanke, mit dem das Bundesverfassungsgericht das Werkzeug vom Einsatz getrennt hat.

::::beispiel
Ein Mitglied eines Hackervereins entdeckt, dass eine Stadtverwaltung die Daten von Bürgern ungeschützt im Netz stehen hat. Nach der Hackerethik meldet es den Fund, statt die Daten zu sammeln, zu verändern oder bloßzustellen: Es nützt das Wissen über die Lücke und schützt die privaten Daten.
::::

⁠**Kurz gesagt:** Die Hackerethik ist eine Selbstverpflichtung, die Neugier mit Rücksicht verbindet; Erlaubnis ersetzt sie nicht.

### Die Spielregeln dieser Reihe

<span class="anker" id="stufe-10-7"></span>

Alle praktischen Übungen dieser Reihe, auch die, in denen man aus Sicht eines Angreifers arbeitet, finden unter Regeln statt, die aus diesem Kapitel folgen. Die Frage, die vor jeder Übung steht, lautet: Darf ich das hier testen? Abbildung [18](#abb-18) zeigt, wie man sie beantwortet.

Zwei Begriffe kommen darin vor. Eine __Lernplattform__ ist ein Angebot im Internet, dessen Betreiber eigens verwundbare Übungssysteme bereitstellt und ausdrücklich erlaubt, sie innerhalb seiner Regeln anzugreifen. Ein __isoliertes Labor__ ist eine eigene Übungsumgebung, die vom Internet und vom übrigen Heimnetz getrennt ist und in der nur eigene, absichtlich verwundbare Übungsprogramme laufen.

:::abbildung cyber/k1entscheidung 18
Darf ich das testen? Nur wenn eine der drei Fragen mit Ja beantwortet ist, und dann nur in dem Rahmen, den die Antwort nennt. In jedem anderen Fall lautet die Antwort: nicht testen.
:::

:::warnung Die Spielregeln für alle Übungen
Diese Regeln gelten für jede praktische Übung in diesem Kapitel und in allen weiteren Teilen der Reihe.

<ol>

<li>

⁠**Nur wo du darfst.** Angreifen, untersuchen und mitschneiden darfst du nur

<ul>

<li>

eigene Systeme, und nur, wenn keine Daten anderer Menschen betroffen sind; Mitbewohner und Familie im selben Netz sind andere Menschen;

</li>

<li>

isolierte Labore mit eigenen Übungsprogrammen;

</li>

<li>

Lernplattformen, und nur die Ziele, die sie freigeben, zum Beispiel pwn.college ([https://pwn.college](https://pwn.college)), OverTheWire ([https://overthewire.org](https://overthewire.org)), die PortSwigger Web Security Academy ([https://portswigger.net/web-security](https://portswigger.net/web-security)) und CryptoHack ([https://cryptohack.org](https://cryptohack.org)).

</li>

</ul>

</li>

<li>

⁠**Nie ein fremdes System ohne Erlaubnis.** Auch nicht „nur kurz schauen“, auch nicht mit guter Absicht. Für jeden Test an einem fremden System brauchst du eine ausdrückliche, schriftliche Erlaubnis des Verfügungsberechtigten mit festgelegtem Umfang.

</li>

<li>

⁠**Nichts mitschneiden, überlasten, verändern oder hehlen.** Kein Aufzeichnen fremder Funk- oder Kabelnetze (§ 202b), keine Überlastungs- oder Belastungstests gegen fremde Dienste (§ 303b), kein Verändern oder Löschen fremder Daten (§ 303a), keine geleakten Datenbanken oder Passwortlisten beschaffen oder weitergeben (§ 202d).

</li>

<li>

⁠**Die Regeln der Plattform gelten.** Greife nur die freigegebenen Ziele an, nie die Plattform selbst oder andere Nutzer, und benutze sie nie als Ausgangspunkt für Angriffe nach außen. Veröffentliche keine Lösungen oder Passwörter von Plattform-Aufgaben: OverTheWire untersagt ausdrücklich, die Passwörter seiner Stufen zu veröffentlichen, und pwn.college bittet darum, keine Lösungen zu veröffentlichen. Diese Reihe gibt zu Plattform-Aufgaben deshalb nur gestufte Hinweise.

</li>

<li>

⁠**Zufallsfund: aufhören und melden.** Nichts weiter ausprobieren, nichts herunterladen, aufschreiben und koordiniert melden.

</li>

<li>

⁠**Im Zweifel nicht.** Bist du unsicher, ob etwas erlaubt ist, tu es nicht und frag nach.

</li>

</ol>

Die Regeln geben eine Orientierung nach deutschem Recht, Stand 4. November 2026; sie sind keine Rechtsberatung.
:::

⁠**Kurz gesagt:** Geübt wird nur an eigenen Systemen, in isolierten Laboren und auf Lernplattformen innerhalb ihrer Regeln; an fremden Systemen nie ohne schriftliche Erlaubnis.

:::aufgabe Aufgabe 18 ★ Die security.txt einer Webseite lesen
<span class="anker" id="aufg-18"></span>

Öffne im Browser die Adresse [https://www.bsi.bund.de/.well-known/security.txt](https://www.bsi.bund.de/.well-known/security.txt). Der Browser zeigt eine kurze Textdatei. Wähle dir außerdem zwei große Webseiten, die du selbst benutzt, und hänge an ihre Domain denselben Pfad an.

<ol class="al">

<li>

Welche Kontakte nennt die Datei des BSI? Welcher steht an erster Stelle?

</li>

<li>

Bis wann sollen die Angaben gelten? Entspricht das der Empfehlung des Standards?

</li>

<li>

Welche freiwilligen Felder kommen vor, und wofür steht jedes?

</li>

<li>

Haben deine beiden anderen Webseiten eine security.txt? Wenn ja: Ist ihr `Expires` noch nicht erreicht? Wenn nein: Wie würdest du dort einen Sicherheitskontakt finden?

</li>

</ol>

Die Abrufe sind gewöhnliche Seitenaufrufe öffentlicher Dateien; sie berühren kein Schutzgut.

:::loesung
Stand der Dateien am 4. November 2026; die Inhalte können sich ändern.

(a) Die Datei des BSI nennt als Kontakte zuerst `mailto:vulnerability@bsi.bund.de`, dann eine Webseite des BSI für Sicherheitsmeldungen und außerdem `mailto:certbund@bsi.bund.de`, laut Kommentar für Sicherheitsvorfälle, die das BSI selbst betreffen. An erster Stelle steht die E-Mail-Adresse für Schwachstellenmeldungen.

(b) `Expires: 2099-06-29T12:00:00.000Z`. Das entspricht nicht der Empfehlung des Standards, das Datum weniger als ein Jahr in die Zukunft zu legen. Das Feld ist vorhanden, wie verlangt, verliert aber seinen Zweck, die Organisation zur regelmäßigen Prüfung zu zwingen.

(c) Unter anderem `Encryption` (Verweis auf den Schlüssel, mit dem man vertraulich schreiben kann), `Policy` (die Regeln des BSI für Schwachstellenmeldungen), `Acknowledgments` (die Seite, auf der das BSI Findern dankt), `Preferred-Languages: de, en`, `Canonical` (die Adresse, unter der die Datei maßgeblich liegt) und `Hiring` (Stellenangebote). Dazu kommt ein Feld `CSAF`, das auf maschinenlesbare Sicherheitshinweise verweist und nicht zu den Feldern des ursprünglichen Standards gehört. Die Zeilen mit `#` sind Kommentare.

(d) Das hängt von deiner Wahl ab. Zum Vergleich am 4. November 2026: Google nennt eine Meldeseite und `security@google.com`, gültig bis 2030; GitHub verweist auf sein Bug-Bounty-Programm bei einer Plattform für solche Programme, gültig bis 4. Dezember 2026, also nur noch einen Monat. Gibt es keine security.txt, sucht man auf der Webseite nach einer Seite zu Sicherheit oder Schwachstellenmeldungen oder im Impressum nach einem Kontakt und fragt dort nach dem richtigen Ansprechpartner, ohne Einzelheiten der Lücke zu nennen.
:::
:::

:::aufgabe Aufgabe 19 ★★ Ein Fund im Smart-Home
<span class="anker" id="aufg-19"></span>

Du hast dir ein vernetztes Thermostat gekauft. Beim Einrichten in deinem eigenen Heimnetz siehst du in der App, dass das Gerät eine Verwaltungsseite hat, die im Heimnetz ohne Passwort erreichbar ist. Dort könnte jeder im Netz die WLAN-Zugangsdaten auslesen.

<ol class="al">

<li>

Darfst du an deinem eigenen Gerät weiter untersuchen, wie weit die Lücke reicht? Wo liegen die Grenzen? Benutze Abbildung [18](#abb-18).

</li>

<li>

Du willst prüfen, ob auch das Gerät eines Freundes betroffen ist. Was brauchst du dafür?

</li>

<li>

Gliedere eine Meldung an den Hersteller: Welche Angaben gehören hinein? Schätze dazu auch einen CVSS-Vektor nach Tabelle [2](schwachstellen-benennen-und-bewerten.html#tab-2) ab.

</li>

<li>

Der Hersteller antwortet acht Wochen lang nicht. Was tust du, und was tust du nicht?

</li>

</ol>

:::loesung
(a) Ja, an deinem eigenen Gerät in deinem eigenen Netz darfst du untersuchen, wie weit die Lücke reicht; die erste Frage in Abbildung [18](#abb-18) ist mit Ja beantwortet. Die Grenzen: Leben andere im selben Netz, deren Daten berührt werden könnten, hältst du dich davon fern. Die Server des Herstellers, mit denen die App spricht, gehören dir nicht; sie zu untersuchen wäre unbefugt. Du veröffentlichst nichts, solange der Hersteller nicht informiert ist.

(b) Die ausdrückliche, am besten schriftliche Erlaubnis deines Freundes als Verfügungsberechtigtem, mit Umfang: welches Gerät, wann, was du tust. Wohnen bei ihm weitere Menschen, sollten auch sie einverstanden sein, weil ihre Daten im selben Netz laufen.

(c) Gliederung: Produkt und Firmware-Version; wie und wo die Verwaltungsseite erreichbar ist; was ohne Anmeldung möglich ist, insbesondere das Auslesen der WLAN-Zugangsdaten; die Schritte, mit denen der Hersteller es nachvollziehen kann; Einordnung als CWE, etwa CWE-306 „Missing Authentication for Critical Function“; Schätzung der Schwere; deine Kontaktdaten und die Bitte um Rückmeldung. CVSS-Schätzung: Der Angreifer muss im selben Netz sein, also AV:A; keine besonderen Bedingungen, keine Anmeldung, kein Nutzer nötig: AC:L, PR:N, UI:N. Kann man nur lesen: C:H, I:N, A:N, mit S:U ergibt das 6,5, mittel. Kann man auch Einstellungen ändern, sind I und A ebenfalls hoch, das ergibt 8,8, hoch. Man kann auch S:C begründen, weil die WLAN-Zugangsdaten das ganze Heimnetz öffnen; für das reine Auslesen ergibt das 7,4.

(d) Du erinnerst den Hersteller einmal mit einer angemessenen Frist und wendest dich, wenn wieder nichts kommt, an einen Koordinator, in Deutschland das BSI. Du veröffentlichst nicht auf eigene Faust, nutzt die Lücke an fremden Geräten nicht aus und gibst keine Anleitung weiter. Eine Veröffentlichung stimmst du mit dem Koordinator ab.
:::
:::

:::aufgabe Aufgabe 20 ★★ Hackerethik und Recht
<span class="anker" id="aufg-20"></span>

<ol class="al">

<li>

Ein Bekannter sagt: „Alle Informationen müssen frei sein, das ist Hackerethik. Also darf ich mir die Klausur aus dem Hochschulserver holen.“ Antworte ihm mit zwei Argumenten aus der Ethik und einem aus dem Recht.

</li>

<li>

Ist es ein Widerspruch, dass ein Kapitel über Verteidigung Angriffe lehrt? Begründe mit dem Gedanken, dass Wissen weder gut noch schlecht ist, und mit dem Beschluss von 2009.

</li>

</ol>

:::loesung
(a) Ethik: Zwei der Grundsätze lauten „Mülle nicht in den Daten anderer Leute“ und „Öffentliche Daten nützen, private Daten schützen“; eine unveröffentlichte Klausur auf dem Server der Hochschule ist nicht öffentlich, und wer in fremde Systeme eindringt, um sich einen Vorteil zu verschaffen, handelt gegen beide. Außerdem ist die Hackerethik eine Selbstverpflichtung der Szene, keine Erlaubnis; wer sich auf sie beruft, wird dadurch nicht befugt. Recht: Das Eindringen in den Server ist nach § 202a strafbar, wenn er eine Sicherung überwindet, gleich, wie er es begründet.

(b) Kein Widerspruch. Eine Lücke findet und schließt nur, wer weiß, wie ein Angreifer vorgeht; Verteidigung ohne Kenntnis des Angriffs ist Raten. Das Wissen selbst ist weder gut noch schlecht, gut oder schlecht ist sein Einsatz. Genau so hat das Bundesverfassungsgericht 2009 unterschieden: Werkzeuge, die für Prüfung und Angriff taugen, sind nicht strafbar; strafbar ist ihr Einsatz gegen fremde Systeme ohne Erlaubnis. Deshalb übt diese Reihe Angriffe nur unter den Spielregeln.
:::
:::
