---
title: Erlaubnis, Werkzeuge und gute Absicht
pfad: Informatik / Cybersecurity / Sicherheit, Schutzziele und Spielregeln
adresse: informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln
knoten: Kapitel 1: Sicherheit, Schutzziele und Spielregeln
order: 6111000
summary: Alle Vorschriften des letzten Abschnitts setzen voraus, dass jemand unbefugt oder rechtswidrig handelt.
tags: Umfang, Penetrationstest, Antragsdelikt, Dual-Use-Werkzeug
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Alle Vorschriften des letzten Abschnitts setzen voraus, dass jemand unbefugt oder rechtswidrig handelt. Dieser Abschnitt klärt, was eine Erlaubnis bewirkt, was ein Strafantrag mit Erlaubnis zu tun hat, ob schon der Besitz von Angriffswerkzeugen strafbar ist und ob eine gute Absicht schützt.
:::

### Die Erlaubnis des Berechtigten

<span class="anker" id="stufe-9-1"></span>

Ein Sicherheitsfachmann und ein Einbrecher können am selben Abend dasselbe tun: in ein Firmennetz eindringen, Passwörter erraten, Daten öffnen. Der eine erledigt einen Auftrag, der andere begeht eine Straftat. Der Unterschied liegt nicht in der Technik, sondern in der Erlaubnis.

:::definition Definition 9.1 (Erlaubnis und Umfang)
<span class="anker" id="satz-9-1"></span>

Hat der Verfügungsberechtigte eingewilligt, dass jemand eine Handlung mit seinen Daten oder Systemen ausführt, so handelt dieser nicht unbefugt, und die Merkmale „unbefugt“ und „rechtswidrig“ der Vorschriften aus Abschnitt [8](computerstrafrecht-was-verboten-ist.html#stufe-8) sind nicht erfüllt. Die Erlaubnis reicht aber nur so weit, wie der Berechtigte sie erteilt hat. Diese Grenze heißt der __Umfang__ der Erlaubnis (englisch *scope*): welche Systeme, welche Adressen, welcher Zeitraum, welche Methoden.
:::

Ein Test, bei dem ein Fachmann im Auftrag des Betreibers versucht, in ein System einzudringen, um Schwachstellen zu finden, heißt __Penetrationstest__. Das Bundesverfassungsgericht hat 2009 festgehalten, dass wer im Auftrag und damit im Einverständnis des Verfügungsberechtigten prüft, nicht unbefugt handelt. Schon die Begründung des Gesetzes von 2007 nannte als Beispiel, dass das Aufspüren von Sicherheitslücken im Auftrag des Inhabers nicht strafbar ist.

Für die Praxis heißt das:

<ul>

<li>

Die Erlaubnis muss vom Verfügungsberechtigten kommen. Ein Praktikant oder ein freundlicher Administrator kann sie nicht für das ganze Unternehmen geben.

</li>

<li>

Sie wird schriftlich festgehalten, mit Umfang, Zeitraum, erlaubten Methoden, Ansprechpartnern und den Bedingungen, unter denen der Test abgebrochen wird. Eine schriftliche Erlaubnis ist auch der Beweis, wenn später Streit entsteht.

</li>

<li>

Systeme, die einem anderen gehören, etwa ein Zahlungsdienst, den ein Shop eingebunden hat, sind nicht erfasst, auch wenn sie im selben Ablauf vorkommen. Für sie bräuchte man die Erlaubnis ihres eigenen Verfügungsberechtigten.

</li>

</ul>

::::beispiel
Ein Onlinehändler beauftragt eine Prüferin schriftlich, vom 10. bis 14. März seine Webseite `shop.example` auf Schwachstellen zu testen, ausdrücklich ohne Überlastungsangriffe. Innerhalb dieses Umfangs handelt sie befugt. Stellt sie am 15. März noch einen Test fertig, oder testet sie auch den Server des Zahlungsdienstes, so liegt das außerhalb des Umfangs und ist unbefugt.
::::

⁠**Kurz gesagt:** Mit der Erlaubnis des Verfügungsberechtigten ist dieselbe Handlung keine Straftat, aber nur innerhalb des Umfangs, den er erlaubt hat.

:::hintergrund Warum die Erlaubnis alles entscheidet
Die Vorschriften aus Abschnitt [8](computerstrafrecht-was-verboten-ist.html#stufe-8) schützen das Recht des Verfügungsberechtigten, über seine Daten und Systeme selbst zu bestimmen. Wenn er selbst bestimmt, dass jemand eindringen soll, wird dieses Recht nicht verletzt, sondern ausgeübt. Deshalb entfällt mit der Erlaubnis nicht nur die Strafe, sondern schon das Unrecht.

Darin liegt der Kern dieses Kapitels: Ob eine Handlung erlaubt ist, entscheidet nicht, ob man sie technisch *kann*, sondern ob der Berechtigte sie *erlaubt* hat. Das ist dieselbe Unterscheidung wie zwischen Berechtigten und Unbefugten in Abschnitt [1](was-geschutzt-wird-schutzgut-und-schutzziele.html#stufe-1). Ein Mechanismus, der einen Zugriff nicht verhindert, ist keine Erlaubnis, so wenig wie eine offene Haustür eine Einladung ist.
:::

### Antragsdelikt heißt nicht erlaubt

<span class="anker" id="stufe-9-2"></span>

Manche Taten verfolgt der Staat nur, wenn der Verletzte es verlangt. Daraus ziehen manche den falschen Schluss, solange sich niemand beschwere, sei alles in Ordnung.

:::definition Definition 9.2 (Antragsdelikt)
<span class="anker" id="satz-9-2"></span>

Ein __Antragsdelikt__ ist eine Straftat, die grundsätzlich nur verfolgt wird, wenn der Verletzte einen Strafantrag stellt. Bei einem relativen Antragsdelikt kann die Staatsanwaltschaft sie auch ohne Antrag verfolgen, wenn sie ein besonderes öffentliches Interesse an der Strafverfolgung sieht.
:::

Relative Antragsdelikte sind das Ausspähen, das Abfangen und die Datenhehlerei (§ 205 StGB) sowie die Datenveränderung und die Computersabotage nach § 303b Abs. 1 bis 3 (§ 303c StGB). Das Vorbereiten nach § 202c ist dort nicht genannt; es wird von Amts wegen verfolgt, ebenso grundsätzlich der Computerbetrug. Die Frist für den Antrag beträgt drei Monate und beginnt erst, wenn der Berechtigte von der Tat *und* vom Täter erfährt (§ 77b StGB).

Der Antrag betrifft nur die Frage, ob der Staat die Tat verfolgt. An der Tat selbst ändert er nichts: Auch ohne Antrag bleibt sie eine rechtswidrige Straftat. Der Verletzte kann den Antrag noch Wochen später stellen, die Staatsanwaltschaft kann das öffentliche Interesse bejahen, und unabhängig vom Strafrecht kann der Verletzte Schadensersatz verlangen.

::::beispiel
Eine Studentin dringt ohne Erlaubnis in einen Server ihrer Hochschule ein, um eine Lücke zu zeigen. Der Administrator ist beeindruckt und will nichts unternehmen. Das macht die Tat nicht erlaubt: Verfügungsberechtigt ist die Hochschule, nicht der Administrator, und sie kann innerhalb von drei Monaten, nachdem sie davon erfahren hat, Strafantrag stellen.
::::

⁠**Kurz gesagt:** Bei einem Antragsdelikt hängt die Verfolgung vom Antrag ab, die Strafbarkeit nicht; ohne Antrag bleibt die Tat eine Straftat.

:::hintergrund Warum gerade diese Taten Antragsdelikte sind, und warum nur relative
Die §§ 202a, 202b und 202d schützen das Recht eines Einzelnen, über seine Daten zu bestimmen. Deshalb überlässt das Gesetz grundsätzlich ihm die Entscheidung, ob ein Strafverfahren stattfindet. Warum es aber *relative* Antragsdelikte sind, die der Staat bei besonderem öffentlichem Interesse auch ohne Antrag verfolgen kann, begründete der Gesetzgeber bei der Reform von 2007 für das Ausspähen und das Abfangen mit einer Eigenheit von Computerdaten: Oft betrifft eine Tat Daten von Dritten, etwa die Kundendaten auf dem Server eines Unternehmens. Diese Dritten sind nicht die Verletzten im Sinne des Gesetzes und dürfen keinen Antrag stellen. Ohne die Möglichkeit, von Amts wegen einzuschreiten, hinge ihr Schutz allein davon ab, ob das Unternehmen ein Verfahren will. Die Datenhehlerei kam 2015 hinzu und wurde in dieselbe Regel aufgenommen.

Bei § 202c gibt es noch gar keinen Geschädigten. Die Vorschrift bestraft eine Gefahr für viele, bevor überhaupt jemand angegriffen wurde; man nennt das ein abstraktes Gefährdungsdelikt. Wo niemand verletzt ist, kann auch niemand einen Antrag stellen. Deshalb ist § 202c nach dem Willen des Gesetzgebers kein Antragsdelikt.
:::

### Werkzeuge besitzen: der Beschluss von 2009

<span class="anker" id="stufe-9-3"></span>

Nach § 202c ist strafbar, wer Programme herstellt oder sich verschafft, „deren Zweck die Begehung“ einer Tat nach § 202a oder § 202b ist. Die meisten Werkzeuge der Sicherheitsprüfung kann man aber für beides benutzen: zum Prüfen des eigenen Systems und zum Angriff auf ein fremdes. Ist schon ihr Besitz strafbar?

Ein Werkzeug, das sich für erlaubte und für unerlaubte Zwecke gleichermaßen eignet, heißt __Dual-Use-Werkzeug__ (englisch *dual use*, doppelte Verwendung). Ein bekanntes Beispiel ist das Programm nmap, mit dem Administratoren prüfen, welche Dienste ein Rechner im Netz anbietet.

Kurz nach der Einführung des § 202c im Jahr 2007 erhoben drei Betroffene Verfassungsbeschwerde: der Geschäftsführer einer Firma, die Penetrationstests anbietet, ein Hochschullehrer für Informatik, der seinen Studierenden solche Werkzeuge zur Verfügung stellt, und ein Nutzer, der nmap verwendet. Das Bundesverfassungsgericht nahm die Beschwerden mit Beschluss vom 18. Mai 2009 nicht zur Entscheidung an, weil die drei nach seiner Auslegung von der Vorschrift gar nicht betroffen seien. In der Begründung legte es aus, was § 202c erfasst.

:::satz Satz 9.3 (Auslegung von § 202c durch das Bundesverfassungsgericht)
<span class="anker" id="satz-9-3"></span>

Das Gericht legte die Vorschrift in vier Punkten aus:

<ol>

<li>

Erfasst ist nur ein Programm, dessen *Zweck* eine Straftat nach § 202a oder § 202b ist. Es muss mit der Absicht entwickelt oder verändert worden sein, es für solche Taten einzusetzen, und diese Absicht muss sich objektiv zeigen, etwa in der Gestalt des Programms oder in einer Werbung, die eindeutig auf unerlaubte Verwendung zielt.

</li>

<li>

Dass ein Programm sich für solche Taten *eignet*, auch besonders gut eignet, genügt nicht. Dual-Use-Werkzeuge sind deshalb nicht erfasst.

</li>

<li>

Strafbar ist außerdem nur, wer zumindest damit rechnet und billigend in Kauf nimmt, dass das Programm künftig für eine solche Straftat benutzt wird.

</li>

<li>

Wer im Auftrag und damit im Einverständnis des Verfügungsberechtigten prüft, handelt nicht unbefugt.

</li>

</ol>
:::

Der Beschluss ist eine Entscheidung über die Nichtannahme und hat deshalb keine Gesetzeskraft. Er zeigt aber, wie das höchste deutsche Gericht die Vorschrift versteht. Eine Restunsicherheit bleibt bei Programmen, die objektiv für Straftaten gebaut sind, also bei echter Schadsoftware, und bei der Weitergabe an Dritte.

::::beispiel
Ein Student installiert nmap auf seinem Laptop, um sein eigenes Heimnetz zu untersuchen. Das ist nicht strafbar: nmap ist ein Dual-Use-Werkzeug, und er bereitet keine Straftat vor. Richtet er dasselbe Programm ohne Erlaubnis gegen die Rechner eines Unternehmens und dringt mit den Ergebnissen ein, so ist nicht der Besitz das Problem, sondern der Einsatz: Er kann sich nach § 202a strafbar machen.
::::

⁠**Kurz gesagt:** Nicht das Werkzeug ist strafbar, sondern sein Einsatz gegen fremde Systeme ohne Erlaubnis.

:::hintergrund Warum das Werkzeug nicht strafbar ist
Das Gericht stützte sich auf zwei Gründe. Der erste ist der Wortlaut: Die Vorschrift spricht vom *Zweck* eines Programms, nicht von seiner Eignung. Hätte der Gesetzgeber jedes geeignete Programm erfassen wollen, hätte er das schreiben müssen. Das Grundgesetz verlangt in Artikel 103 Absatz 2, dass eine Strafbarkeit gesetzlich bestimmt ist, bevor die Tat begangen wird; eine Auslegung, die über den Wortlaut hinausgeht, wäre verfassungswidrig. Der zweite Grund ist der Wille des Gesetzgebers: § 202c setzt ein Übereinkommen des Europarats um, und dessen Erläuterungen schließen Werkzeuge mit doppelter Verwendung ausdrücklich aus.

Dahinter steht ein Gedanke, der über das Recht hinausgeht. Fast jedes Werkzeug der Sicherheitsprüfung ist dasselbe, das ein Angreifer benutzt; das liegt in der Natur der Sache, denn eine Lücke findet man nur, indem man sie so sucht, wie ein Angreifer es täte. Wäre schon das Werkzeug strafbar, so könnte niemand mehr Systeme prüfen, Studierende ausbilden oder Lücken finden, bevor Kriminelle es tun. Das Unrecht liegt deshalb nicht im Wissen und nicht im Werkzeug, sondern in der Handlung gegen ein fremdes Schutzgut ohne Erlaubnis. Genau dort setzen die §§ 202a, 202b, 303a und 303b an.
:::

### Gute Absicht schützt nicht

<span class="anker" id="stufe-9-4"></span>

Angenommen, jemand dringt ohne Erlaubnis in ein fremdes System ein, nur um eine Lücke nachzuweisen, schaut nichts weiter an und meldet sie sofort dem Betreiber. Ist das erlaubt?

Nach geltendem Recht nein. Keine der Vorschriften aus Abschnitt [8](computerstrafrecht-was-verboten-ist.html#stufe-8) fragt nach dem Motiv; sie fragen, ob jemand unbefugt gehandelt hat. Wer ohne Erlaubnis eine Zugangssicherung überwindet, erfüllt § 202a auch dann, wenn er die Lücke danach meldet. Die gute Absicht kann sich höchstens bei der Höhe der Strafe oder bei der Entscheidung auswirken, ob ein Verfahren eingestellt wird.

Diese Rechtslage ist umstritten, weil sie auch Menschen trifft, die anderen helfen wollen. Das Bundesministerium der Justiz legte am 4. November 2024 einen Entwurf vor, nach dem nicht unbefugt handeln sollte, wer eine Sicherheitslücke feststellen und die Verantwortlichen darüber informieren will, soweit sein Vorgehen dafür erforderlich ist. Dieser Entwurf ist *nicht Gesetz geworden*: Bis zur vorgezogenen Bundestagswahl im Februar 2025 kam er über das Stadium eines Entwurfs des Ministeriums nicht hinaus. Die neue Bundesregierung hat im Koalitionsvertrag angekündigt, im Computerstrafrecht Rechtssicherheit für die IT-Sicherheitsforschung zu schaffen. Ein neuer Entwurf war bis zum 4. November 2026 nicht veröffentlicht.

::::beispiel
Ein Student bemerkt, dass er auf der Seite seines Fitnessstudios durch das Ändern einer Nummer in der Adresse die Daten anderer Mitglieder sehen könnte. Probiert er es aus, um es zu beweisen, riskiert er ein Strafverfahren, auch wenn er die Lücke danach meldet. Meldet er nur seine Beobachtung, ohne fremde Daten abzurufen, bleibt er auf der sicheren Seite.
::::

⁠**Kurz gesagt:** Nach geltendem Recht schützt eine gute Absicht nicht; wer ohne Erlaubnis eindringt, macht sich strafbar, auch wenn er die Lücke danach meldet.

:::hintergrund Nicht nur Verbote: Pflichten für Betreiber und Hersteller
Das Recht verbietet nicht nur Angriffe, es verpflichtet auch die Verteidiger. Drei Regelungen sind für alle wichtig, die später Systeme entwickeln oder betreuen.

<ul>

<li>

Seit dem 6. Dezember 2025 gilt in Deutschland das Gesetz zur Umsetzung der europäischen NIS-2-Richtlinie. Nach Schätzungen rund 29 500 Unternehmen und Einrichtungen, die für das Gemeinwesen besonders wichtig sind, müssen sich beim BSI registrieren, ihre Risiken managen und erhebliche Sicherheitsvorfälle in Stufen melden: eine erste Meldung spätestens 24 Stunden, nachdem sie vom Vorfall erfahren haben, eine ausführlichere spätestens nach 72 Stunden und eine Abschlussmeldung spätestens einen Monat nach der zweiten Meldung. Die Geschäftsleitung muss die Maßnahmen gegen die Risiken umsetzen und ihre Umsetzung überwachen; verletzt sie diese Pflicht, haftet sie dem Unternehmen nach den Regeln des Gesellschaftsrechts. Außerdem muss sie regelmäßig an Schulungen teilnehmen.

</li>

<li>

Der europäische Cyber Resilience Act verpflichtet Hersteller von Produkten mit digitalen Elementen, also fast jedem vernetzten Gerät, seit dem 11. September 2026, aktiv ausgenutzte Schwachstellen in ihren Produkten zu melden: eine Frühwarnung nach 24 Stunden, eine Meldung nach 72 Stunden, einen Abschlussbericht spätestens 14 Tage, nachdem eine Korrektur verfügbar ist. Ab dem 11. Dezember 2027 gelten die meisten übrigen Pflichten, etwa Schwachstellen über die ganze Lebensdauer eines Produkts zu behandeln. Wer später ein vernetztes Gerät entwickelt, ist davon unmittelbar betroffen.

</li>

<li>

Die Datenschutz-Grundverordnung verlangt, dass eine Verletzung des Schutzes personenbezogener Daten der Aufsichtsbehörde unverzüglich und möglichst binnen 72 Stunden gemeldet wird, nachdem die Stelle, die die Daten verarbeitet, von ihr erfahren hat, es sei denn, sie führt voraussichtlich zu keinem Risiko für die betroffenen Menschen.

</li>

</ul>
:::

:::aufgabe Aufgabe 17 ★★ Erlaubt oder nicht?
<span class="anker" id="aufg-17"></span>

Beurteile jeden Fall und begründe mit den Begriffen dieses Abschnitts.

<ol class="al">

<li>

Ein Student lädt nmap herunter und lernt damit, sein eigenes Heimnetz zu untersuchen.

</li>

<li>

Das nmap-Projekt betreibt den Rechner `scanme.nmap.org` und erlaubt ausdrücklich, ihn zum Ausprobieren gelegentlich mit nmap zu untersuchen. Eine Studentin tut das zweimal.

</li>

<li>

Eine Prüferin hat den schriftlichen Auftrag, die Webseite eines Hotels zu testen. Dabei stößt sie auf den Server des Buchungsportals, über das das Hotel seine Zimmer anbietet, und testet ihn gleich mit.

</li>

<li>

Ein Schüler findet ohne Erlaubnis eine Lücke im Notenportal seiner Schule, lädt zum Beweis seine eigene und zwei fremde Noten herunter und meldet die Lücke dem Schulleiter. Der Schulleiter bedankt sich und verzichtet auf einen Strafantrag. Ist damit alles erledigt?

</li>

<li>

Ein Entwickler schreibt ein Programm, das automatisch Passwörter an fremden Anmeldeseiten ausprobiert, und bietet es in einem Forum an mit der Werbung: „Knackt jedes Instagram-Konto.“

</li>

</ol>

:::loesung
(a) Erlaubt. nmap ist ein Dual-Use-Werkzeug, sein Zweck ist nicht das Ausspähen von Daten, also erfasst § 202c es nicht. Im eigenen Heimnetz handelt der Student als Verfügungsberechtigter, solange er keine Daten anderer Bewohner abgreift.

(b) Erlaubt. Der Betreiber, also der Verfügungsberechtigte, hat die Untersuchung ausdrücklich erlaubt, und zwar in diesem Umfang: gelegentlich, nicht in großer Zahl. Zweimal liegt darin. Hundertmal am Tag oder andere Angriffe auf denselben Rechner lägen außerhalb.

(c) Nicht erlaubt. Der Server des Buchungsportals gehört einem anderen Verfügungsberechtigten; der Auftrag des Hotels erstreckt sich nicht auf ihn, auch wenn er im selben Ablauf vorkommt. Die Prüferin hätte den Fund dem Hotel melden und es dem Portal überlassen müssen, ob es selbst prüfen lässt.

(d) Nein. Mit dem Abrufen der Noten durch die Lücke, also unter Umgehung der Zugangssicherung des Portals, hat der Schüler § 202a erfüllt; die gute Absicht ändert daran nichts. Ob der Schulleiter wirksam auf einen Antrag verzichten kann, hängt davon ab, wer für das Notenportal verfügungsberechtigt ist; das kann der Schulträger oder das Land sein. Außerdem ist § 202a ein relatives Antragsdelikt: Die Staatsanwaltschaft kann bei besonderem öffentlichem Interesse auch ohne Antrag verfolgen. Mit den beiden fremden Noten hat er zudem Daten von Mitschülern abgerufen, deren Schutz die Schule zu sichern hat. Die Mitschüler selbst können keinen Strafantrag stellen; gerade für solche Fälle hat der Gesetzgeber das Antragsdelikt relativ gestaltet. Besser wäre gewesen, nur die Beobachtung zu melden, ohne fremde Daten anzutasten.

(e) Strafbar nach § 202c Abs. 1 Nr. 2. Das Programm ist kein Dual-Use-Werkzeug mehr: Die Werbung zeigt objektiv, dass sein Zweck das Eindringen in fremde Konten ist, wie es das Bundesverfassungsgericht verlangt. Mit dem Anbieten macht er es anderen zugänglich und rechnet damit, dass sie es für Taten nach § 202a benutzen.
:::
:::
