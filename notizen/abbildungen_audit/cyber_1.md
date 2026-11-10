# Abbildungen und Animationen — Paket cyber_1 (Heft cyber/01-sicherheit-schutzziele-und-spielregeln)

Stand: 09.11.2026. Nur Vorschlagsplan, nichts an Artikeln/Szenen geändert.
Deutsche Artikel 01–12. 18 Szenen `cyber/k1…` vorhanden (alle statisch). 7 Konzeptbilder (k1brief, k1kette, k1schichten, k1toctou, k1zyklus, k1offenlegung, k1entscheidung) bestehen aus TextBox/LabeledArrow/Text, 1 Diagramm (k1risiko: Axes + DataCurve), 10 „Rechenbilder“ k1r… bestehen aus einem einzigen statischen `MathTex` (keine Editor-Operation). Für Rechenbilder gilt: durch die Editor-Operation ∏/Σ/Arithmetik ersetzen oder Zeile für Zeile aufbauen (Write je Zeile).

## Kurzbilanz je Artikel

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 01-sicherheit-schutzziele-und-spielregeln | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02-was-geschutzt-wird-schutzgut-und-schutzziele | 5 | 1 | 2 | 2 | 0 | 0 | 5 |
| 03-von-der-schwachstelle-zum-schaden | 3 | 1 | 1 | 1 | 0 | 0 | 3 |
| 04-risiko-angreifermodell-und-angriffsflache | 5 | 7 | 0 | 0 | 0 | 2 | 5 |
| 05-richtlinie-und-mechanismus | 3 | 0 | 3 | 0 | 0 | 0 | 3 |
| 06-sicherheitsprinzipien-rechte-vergeben-und-prufen | 4 | 2 | 1 | 1 | 0 | 0 | 4 |
| 07-sicherheitsprinzipien-systeme-robust-entwerfen | 4 | 3 | 1 | 1 | 0 | 1 | 4 |
| 08-schwachstellen-benennen-und-bewerten | 5 | 2 | 2 | 1 | 0 | 0 | 5 |
| 09-computerstrafrecht-was-verboten-ist | 5 | 0 | 3 | 2 | 0 | 0 | 5 |
| 10-erlaubnis-werkzeuge-und-gute-absicht | 4 | 0 | 2 | 2 | 0 | 0 | 4 |
| 11-offenlegung-und-ethik | 5 | 2 | 2 | 1 | 0 | 0 | 5 |
| 12-das-wichtigste-bis-hier | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| **Summe** | 45 | 18 | 19 | 11 | 0 | 3 | 45 |

Keine Überschreitung des Solls. V12 und V22 sind Wiederverwendungen (V12 nutzt V7, V22 nutzt V5) und zählen als Abbildung im jeweiligen Artikel. Alle 18 vorhandenen Szenen sind statisch; die Rechenbilder k1r… bestehen aus einem einzigen MathTex.

## Top 3

- V10 [A] 05-richtlinie-und-mechanismus — Nachricht zwischen zwei Parteien: der Lauscher kopiert, der Fälscher ersetzt — zeigt, warum Mithören keine Spur hinterlässt und Verändern schon, und damit „passiv verhindern, aktiv erkennen“
- V7 [A] 03-von-der-schwachstelle-zum-schaden — Kundenportal: Rechnungsnummer 1041 zu 1042, das Portal prüft nur „existiert“ — macht Schwachstelle, Angriff, Exploit und Schaden an einem Fall greifbar und wird in V12 und Artikel 11 wiederverwendet
- V9 [A] 05-richtlinie-und-mechanismus — Schadenskurve eines Angriffs mit Verhindern, Erkennen, Wiederherstellen — Verfahren ohne Bild, verbindet drei Mechanismenarten mit H und S

## Editor-Lücken

- L6: 2 (V5 Anfragenflut, V22 verteilter Überlastungsangriff; Notbehelf mit wenigen einzelnen Punkten per Shift)
- L9: 2 (V17 Vektorteile, V18/V20 Zellen/Kästchen einzeln betonen; sonst mit Indicate auf einzelnen Texten machbar)
- L1: 1 (V10 Aufschrift ersetzen; Notbehelf: zweiter Umschlag)
- L10: alle Animationen (Abspielknopf im Artikel fehlt)
- L-neu: keine. Die übrigen 25 Vorschläge sind mit TextBox, LabeledArrow, Shift/MoveAlongPath, Table, Axes, Mark und den Operationen ∏/Σ machbar.
- Für die vorhandenen Szenen: Rechenbilder k1r… brauchen die Editor-Operationen ∏, Σ, Arithmetik statt eines MathTex; kein weiterer Bedarf.

## Vorschläge

### Artikel 01 — Überblick (Soll 1, vorh. 0)

### V1 [A] Landkarte des Kapitels: von „sicher wofür?“ zu „was darf ich?“
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/01-sicherheit-schutzziele-und-spielregeln.md
- **Stelle:** Worum es geht — „Dieses Kapitel geht der Frage nach, was ein System sicher macht, wie man misst …“
- **Art:** neue Animation
- **Was zu sehen ist:** Fünf TextBoxen in einer Reihe, durch LabeledArrows verbunden, jeweils mit Frage als Kopfzeile und Stichwort darunter: „Was wird geschützt?“ (Schutzgut, Schutzziele) → „Wovor?“ (Schwachstelle, Bedrohung, Angriff, Schaden) → „Wie viel Schutz lohnt sich?“ (Risiko, Angreifermodell) → „Wie baut man ihn?“ (Richtlinie, Mechanismus, Prinzipien, Schwachstellen bewerten) → „Was darf ich beim Üben?“ (Recht, Erlaubnis, Offenlegung). Darunter eine Klammer (Brace) über den ersten vier mit „Technik und Denkmodell“, eine über dem fünften mit „Spielregeln“.
- **Ablauf:** 1. Frage 1 erscheint (FadeIn), ein kleines Fahrrad-Schloss-Symbol (Text) daneben als Alltagsbild „sicher wofür, gegen wen, zu welchem Preis?“. 2. Pfeil, Frage 2 erscheint. 3. Pfeil, Frage 3. 4. Pfeil, Frage 4. 5. Pfeil, Frage 5 in Orange abgesetzt; beide Klammern erscheinen (Create). — Haltepunkte: Schritt 1 und Schritt 5.
- **Verständnisproblem:** Der Leser sieht nicht, wie die einzelnen Abschnitte zusammenhängen und warum Recht in einem Sicherheitskapitel steht.
- **Szenenname:** cyber/k1landkarte
- **Editor-Lücke:** machbar

### Artikel 02 — Was geschützt wird (Soll 5, vorh. 1)

### V2 [A] Schutzgüter eines Thermostats (Begriff Schutzgut)
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/02-was-geschutzt-wird-schutzgut-und-schutzziele.md
- **Stelle:** Das Schutzgut — „Wer eine Wohnung absichert, denkt zuerst an das, was darin wertvoll ist …“
- **Art:** neue Animation
- **Was zu sehen ist:** Mitte: Symbol „Thermostat“ (TextBox, 80 €). Rundherum vier TextBoxen, deren Größe etwa dem Wert entspricht: „Temperaturverlauf“, „Steuerfunktion“, „WLAN-Zugangsdaten“, „Gerät (80 €)“. Das Gerät ist die kleinste Box. Dahinter jeweils eine gestrichelte Linie zu einem Bild-Text der Folge: „verrät, wann niemand da ist“, „Heizung im Winter aus“, „Zugang zum ganzen Heimnetz“.
- **Ablauf:** 1. Thermostat erscheint. 2. Gerät-Box erscheint (der erwartete Wert). 3. Temperaturverlauf, 4. Steuerfunktion, 5. WLAN-Daten erscheinen nacheinander und wachsen größer als das Gerät (Scale), jeweils mit Folge-Text. 6. Indicate auf das Gerät: „das billigste der vier“. — Haltepunkte: Schritt 2 und Schritt 5.
- **Verständnisproblem:** „Schutzgut“ ist leicht mit „das Gerät“ gleichzusetzen; Informationen und Dienste, die am Gerät hängen, sind meist mehr wert.
- **Szenenname:** cyber/k1schutzgut
- **Editor-Lücke:** machbar

### V3 [A] Können ist nicht dürfen: Berechtigung als Tabelle
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/02-was-geschutzt-wird-schutzgut-und-schutzziele.md
- **Stelle:** Berechtigte und Unbefugte — „Fast jede Frage der Sicherheit lautet am Ende: Darf diese Person das?“
- **Art:** neue Animation
- **Was zu sehen ist:** Table, Zeilen Kontoinhaberin / Bankberater / Fremder (mit erratenem Passwort), Spalten „Kontostand lesen“, „Überweisung auslösen“, „System lässt es technisch zu“. Mark (Haken grün, Kreuz orange) je Zelle: Kontoinhaberin ✓ ✓ ✓; Bankberater ✓ (lesen), ✗ ohne Auftrag (überweisen), ✓ technisch; Fremder ✗ ✗ aber ✓ technisch.
- **Ablauf:** 1. Tabelle mit Köpfen erscheint. 2. Zeile Kontoinhaberin füllt sich. 3. Zeile Bankberater. 4. Zeile Fremder: die Spalte „technisch zugelassen“ zeigt Haken, die „berechtigt“-Spalten Kreuze; Rahmen um den Widerspruch (Indicate), Text „unbefugt, obwohl das System ihn hereinließ“. — Haltepunkte: Schritt 4.
- **Verständnisproblem:** Der Unterschied zwischen „kann“ (Technik) und „darf“ (Festlegung des Verfügungsberechtigten) und dass Berechtigung je Handlung gilt.
- **Szenenname:** cyber/k1berechtigung
- **Editor-Lücke:** machbar (Zellen einzeln betonen sonst L9)

### V4 [B] Phishing-Nachricht: Wer ist der Absender wirklich?
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/02-was-geschutzt-wird-schutzgut-und-schutzziele.md
- **Stelle:** Authentizität — „Eine Nachricht kann vollständig, unverändert und pünktlich ankommen …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links Kasten „Prüfungsamt (echt)“ grau und unbeteiligt, Mitte Kasten „Fremder“ (orange), rechts Kasten „Student“. Ein Umschlag (kleines Rechteck) mit Aufschrift „Absender: Prüfungsamt“ wandert vom Fremden zum Studenten; ein zweiter Umschlag „Passwort“ wandert zurück zum Fremden.
- **Ablauf:** 1. Drei Parteien erscheinen. 2. Der Umschlag mit dem aufgedruckten Absender „Prüfungsamt“ startet beim Fremden und wandert (Shift) zum Studenten; Text: „Inhalt vollständig, unverändert, pünktlich“. 3. Gestrichelter Pfeil vom Prüfungsamt zum Umschlag erscheint mit Mark ✗: „stammt nicht von dort“ (Authentizität verletzt). 4. Student gibt das Passwort ein: Umschlag „Passwort“ wandert zum Fremden; Beschriftung „danach: Vertraulichkeit verletzt“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Authentizität ist etwas anderes als Integrität: die Nachricht ist unverändert, aber nicht von dem, der draufsteht.
- **Szenenname:** cyber/k1phishing
- **Editor-Lücke:** machbar (MoveAlongPath/Shift für Umschlag)

### V5 [B] Verfügbarkeit: Anfragenflut vor dem Onlineshop
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/02-was-geschutzt-wird-schutzgut-und-schutzziele.md
- **Stelle:** Verfügbarkeit — „Ein Onlineshop wird mit Millionen sinnloser Anfragen überschüttet …“
- **Art:** neue Animation
- **Was zu sehen ist:** Rechts Kasten „Onlineshop (Daten unverändert)“. Links oben ein Kunde mit einer Bestellung (ein Paket), links unten viele kleine Punkte (sinnlose Anfragen). Ein Warteschlangenbalken vor dem Shop.
- **Ablauf:** 1. Der Kunde schickt eine Bestellung (Punkt wandert), der Shop antwortet mit Haken. 2. Punkte erscheinen in Wellen und wandern in den Shop; der Balken vor dem Shop füllt sich (Scale). 3. Die Bestellung des Kunden wird an der vollen Schlange abgewiesen (Kreuz). Text: „Waren und Daten unverändert, aber kein Kunde kann bestellen“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Verfügbarkeit kann verletzt sein, obwohl nichts gelesen oder verändert wurde.
- **Szenenname:** cyber/k1flut
- **Editor-Lücke:** braucht Editor-Funktion: L6 (viele bewegte Punkte). Notbehelf: sechs bis acht einzelne Punkte per Shift.

### Artikel 03 — Von der Schwachstelle zum Schaden (Soll 3, vorh. 1)

### V6 [B] Router mit Werkspasswort: automatische Suche übernimmt Geräte
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/03-von-der-schwachstelle-zum-schaden.md
- **Stelle:** Bedrohung — „Für den Router mit dem Passwort admin besteht die Bedrohung darin, dass Programme das Internet ständig automatisch nach Geräten absuchen …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links ein Kasten „Suchprogramm (Angreifer)“. Rechts fünf Router-Kästchen, drei mit „Passwort geändert“ (grau), eines mit Schild „admin, Verwaltungsseite aus dem Internet erreichbar“ (orange), eines mit „admin, nur im Heimnetz erreichbar“ (grau). Oben rechts ein Kasten „Webdienst“.
- **Ablauf:** 1. Das Suchprogramm schickt nacheinander Anfragen (Punkte) zu den fünf Routern. 2. Bei vier Routern prallt die Anfrage ab (Kreuz). 3. Beim orangen Router gelingt die Anmeldung (Haken), der Router wechselt die Farbe: „übernommen“. 4. Der übernommene Router schickt Anfragen zum Webdienst: „2016 so Hunderttausende Kameras und Router, Webdienste überlastet“. 5. Text: „Bedrohung: fortlaufend, automatisch, ohne Interesse an genau diesem Gerät“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Dass eine Bedrohung ohne bestimmtes Ziel auskommt und die Schwachstelle (Werkspasswort, von außen erreichbar) dazugehört; Brücke zur Kette (Abb. 2).
- **Szenenname:** cyber/k1router
- **Editor-Lücke:** machbar (wenige einzelne Punkte per Shift; viele wären L6)

### V7 [A] Kundenportal: Rechnungsnummer um eins erhöhen
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/03-von-der-schwachstelle-zum-schaden.md
- **Stelle:** Schwachstelle — „Ein Kundenportal zeigt Rechnungen unter Adressen wie shop.example/rechnung?nr=1041 …“
- **Art:** neue Animation
- **Was zu sehen ist:** Sequenzbild mit drei Spalten: Kunde (Browser), Portal, Datenbank. Adresszeile als TextBox oben. Pfeile mit Beschriftung der Anfragen und Antworten.
- **Ablauf:** 1. Kunde ruft nr=1041 ab; Pfeil zum Portal; Portal fragt Datenbank „gibt es 1041? gehört sie dem Kunden?“; Antwort Rechnung 1041 zurück. 2. Kunde ändert in der Adresszeile 1041 zu 1042 (Text wird ersetzt: Write). 3. Portal prüft nur „existiert 1042?“ (Haken), prüft nicht den Besitzer (durchgestrichene Zeile „gehört sie dem angemeldeten Kunden?“, Kreuz in Orange); Rechnung 1042 geht an den Kunden. 4. Beschriftungen: Schwachstelle = fehlende Prüfung, Exploit = Nummer erhöhen, Schaden = fremde Daten bekannt. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Schwachstelle, Angriff und Exploit werden an einem Fall konkret getrennt, bevor sie in Aufgabe 3 gebraucht werden.
- **Szenenname:** cyber/k1portal
- **Editor-Lücke:** machbar (Ersetzen der Adresse als zwei Texte, ohne L2)

Die vorhandene Abbildung `cyber/k1kette` wird animiert (siehe unten). Verworfen: Panne oder Angriff (Zufall gegen Gegner) im Hintergrund-Kasten.

### Artikel 04 — Risiko, Angreifermodell und Angriffsfläche (Soll 5, vorh. 7)

Sieben Szenen liegen vor, Soll 5 (mit etwa 3 000 effektiven Wörtern der längste Artikel des Hefts, mehr als 5 geht nicht). Zusammenlegung: `cyber/k1rrisiko` (R_A und R_B einzeln) geht in `cyber/k1rgesamt` auf (erst die zwei Produkte, dann die Summe); `cyber/k1rwuerfel` entfällt als eigene Abbildung, weil der Gedanke „Faktor (1−p) n-mal multiplizieren“ in `cyber/k1rflaeche` mit denselben Schritten wiederkehrt und die Würfelrechnung als Text im Beispiel stehen bleibt. Keine neuen Vorschläge, das Soll ist mit den vorhandenen erreicht. Verworfen: Angriffsfläche als Haus mit vielen Eingängen (A; passt nicht mehr ins Soll, ersetzt falls gewünscht `cyber/k1rflaeche`, dann steht die Rechnung nur im Text) und das Angreifermodell als Dreiachsenbild (Ziel, Können, Ansatzpunkt).

### Artikel 05 — Richtlinie und Mechanismus (Soll 3, vorh. 0)

### V8 [A] Richtlinie teilt die Zustände, Mechanismus bewacht die Grenze
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/05-richtlinie-und-mechanismus.md
- **Stelle:** Sicherheitsrichtlinie — „Mit diesem Begriff lässt sich genau sagen, was „sicher“ bedeutet.“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine große Ellipse (alle Zustände des Notensystems), durch eine Linie geteilt: links „erlaubt“ (grün), rechts „verboten“ (orange). Im erlaubten Teil ein Punkt „Start“. Im verbotenen Teil zwei Texte: „Student liest fremde Note“, „Student ändert eigene Note“. An der Grenze ein Wächter-Kästchen „Mechanismus: Anmeldung + Rechteverwaltung“, an einer Stelle eine Lücke („Rechner des Prüfungsamts unbeaufsichtigt“) ohne Wächter.
- **Ablauf:** 1. Ellipse mit Trennlinie erscheint, Beschriftung „Richtlinie = Einteilung“. 2. Startpunkt erscheint links. 3. Der Punkt versucht dreimal, über die Grenze zu gehen (Shift): zwei Versuche prallen am Wächter ab (Kreuz), der dritte geht durch die Lücke und landet im verbotenen Teil; Text „Verstoß bleibt Verstoß, auch wenn kein Mechanismus ihn verhindert hat“. — Haltepunkte: Schritt 1 und Schritt 3.
- **Verständnisproblem:** „Sicher“ ist ein Zustandsbegriff relativ zur Richtlinie; Richtlinie (was) und Mechanismus (wie) sind zweierlei.
- **Szenenname:** cyber/k1zustaende
- **Editor-Lücke:** machbar (Rückprall als Shift hin und zurück)

### V9 [A] Verhindern, erkennen, wiederherstellen auf der Zeitachse eines Angriffs
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/05-richtlinie-und-mechanismus.md
- **Stelle:** Verhindern, erkennen, wiederherstellen — „Ein Haus wird auf drei verschiedene Arten geschützt …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes mit Zeit nach rechts und „Schaden“ nach oben. Drei markierte Zeitpunkte: Angriffsbeginn, Entdeckung, Wiederherstellung. Drei Mechanismus-Kästchen am Zeitstrahl: „Passwort + Handybestätigung“ (vor dem Angriff), „Meldung bei neuem Gerät“ (an der Entdeckung), „Rückholen, neue Zugangsdaten“ (nach dem Schaden).
- **Ablauf:** 1. Achsen und Zeitpunkt „Angriff beginnt“. 2. Ohne Erkennen: graue Schadenskurve steigt weiter an („Fremder liest eine Woche mit“). 3. Mit Erkennen: orange Kurve steigt nur bis zur Meldung und flacht ab; die Fläche zwischen den Kurven ist der eingesparte Schaden (Area). 4. Wiederherstellen: Die Kurve fällt nach der Maßnahme auf 0, Text „zurück in einen erlaubten Zustand“. 5. Verhindern: Eine dritte Linie startet gar nicht (Kreuz am Angriffsbeginn), „senkt die Häufigkeit H“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Die drei Ziele setzen zu verschiedenen Zeitpunkten an und verkleinern verschiedene Größen (H oder S); wer nicht verhindern kann, soll erkennen.
- **Szenenname:** cyber/k1zeitachse
- **Editor-Lücke:** machbar

### V10 [A] Mithören und Verändern: eine Nachricht zwischen zwei Parteien
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/05-richtlinie-und-mechanismus.md
- **Stelle:** Passiver und aktiver Angriff — „Manche Angreifer wollen nur etwas erfahren, andere wollen etwas verändern.“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Bildhälften übereinander. Oben (passiv): Absender links, Empfänger rechts, dazwischen die Leitung, darunter ein Lauscher mit gestrichelter Abzweigung. Unten (aktiv): derselbe Aufbau mit einem Fälscher in der Mitte, der die Leitung unterbricht. Nachricht als Umschlag „Zahlung 250 €, Konto A“.
- **Ablauf:** 1. Oben: Der Umschlag wandert von links nach rechts und kommt unverändert an; eine Kopie wandert gestrichelt zum Lauscher; Text „beim Empfänger ändert sich nichts, keine Spur“. 2. Unten: Der Umschlag wandert zum Fälscher, ein neuer Umschlag mit „Konto X“ geht weiter zum Empfänger; Text „verändert, hinterlässt Spuren, erkennbar“. 3. Rechts je ein Kasten mit der Faustregel: passiv: verhindern (verschlüsseln); aktiv: erkennen. — Haltepunkte: Schritt 1 (Kopie) und Schritt 2 (Austausch).
- **Verständnisproblem:** Warum man Mithören nicht bemerkt und deshalb verhindern muss, Verändern aber Spuren hinterlässt.
- **Szenenname:** cyber/k1passivaktiv
- **Editor-Lücke:** machbar (das Ersetzen der Aufschrift wäre L1/L2; Notbehelf: zweiter Umschlag erscheint, der erste bleibt grau stehen)

### Artikel 06 — Sicherheitsprinzipien: Rechte vergeben und prüfen (Soll 4, vorh. 2)

### V11 [A] Minimale Rechte: was bei einem übernommenen Konto offenliegt
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/06-sicherheitsprinzipien-rechte-vergeben-und-prufen.md
- **Stelle:** Minimale Rechte — „Eine Praktikantin soll in einem Unternehmen die Ablage für ein einziges Projekt pflegen.“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Gitter aus 200 kleinen Quadraten (Projektordner, 20 mal 10; notfalls 6 mal 5 als Vereinfachung mit Beschriftung „200“), rechts ein Konto-Symbol „Praktikantin“, daneben ein Pfeil „Konto fällt in fremde Hände“. Unter dem Gitter eine zweite Fassung mit nur einem hervorgehobenen Quadrat.
- **Ablauf:** 1. Oben: Rechte „alle 200“: Verbindungslinien vom Konto zu allen Quadraten erscheinen, alle Quadrate färben sich orange. 2. Der Phishing-Pfeil zeigt: Konto wechselt zum Angreifer, „200 offen“. 3. Unten: Rechte „ein Ordner“: nur ein Quadrat ist verbunden; nach dem Wechsel „1 offen“. 4. Text: „kann nie mehr kaputtmachen, als es darf“. — Haltepunkte: Schritt 2 und 3.
- **Verständnisproblem:** Der Schaden eines Fehlers oder übernommenen Kontos wird durch die vergebenen Rechte begrenzt, nicht durch die Wahrscheinlichkeit des Fehlers.
- **Szenenname:** cyber/k1minrechte
- **Editor-Lücke:** machbar (Gitter als Table oder Rechtecke)

### V12 [B] Lückenlose Prüfung: Eingang und jeder Abruf
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/06-sicherheitsprinzipien-rechte-vergeben-und-prufen.md
- **Stelle:** Lückenlose Prüfung — „Das Kundenportal aus Abschnitt 2 prüft beim Anmelden, wer der Kunde ist.“
- **Art:** vorhandene Szene wiederverwenden (die neue Szene `cyber/k1portal` aus V7, als Variante mit Prüfung bei jedem Abruf)
- **Was zu sehen ist:** wie V7 (Kunde, Portal, Datenbank), diesmal mit zwei Prüfstellen: „Anmeldung: wer bist du?“ und zusätzlich bei jedem Abruf „gehört die Rechnung diesem Kunden?“.
- **Ablauf:** 1. Anmeldung (Haken). 2. Abruf 1041: Prüfung bestanden. 3. Abruf 1042: Die zweite Prüfung schlägt an (Kreuz), „Zugriff verweigert“; Text „bei jedem Zugriff aufs Neue“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Eine Prüfung am Eingang genügt nicht; jeder Zugriff wird geprüft.
- **Szenenname:** cyber/k1portal2
- **Editor-Lücke:** machbar

Die beiden vorhandenen Bilder werden animiert (siehe unten). Verworfen: Türsteher mit Gästeliste gegen Verbotsliste (B), Zwei-Faktor-Anmeldung als Bild (C).

### Artikel 07 — Sicherheitsprinzipien: Systeme robust entwerfen (Soll 4, vorh. 3)

Zusammenlegung: `cyber/k1schichten` (Burg) und `cyber/k1rlinien` (Produkt p1·p2·p3) stehen im selben Beispiel mit denselben Zahlen; sie werden eine Szene: Die Burg baut sich Schicht für Schicht auf, jede Schicht trägt ihren Faktor, am Ende steht das Produkt 0,0015 (entfällt: `cyber/k1rlinien`).

### V13 [A] Kleine vertrauenswürdige Basis: eine zentrale Prüfstelle gegen fünfzig
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/07-sicherheitsprinzipien-systeme-robust-entwerfen.md
- **Stelle:** Eine kleine vertrauenswürdige Basis — „Beim Kundenportal aus Abschnitt 2 gehören die Anmeldung und jede Stelle, die Rechte prüft, zur vertrauenswürdigen Basis.“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Portal-Skizzen nebeneinander. Links: 50 Seiten (Gitter kleiner Quadrate, 10 mal 5), jede mit einem eigenen Prüfzeichen; die vertrauenswürdige Basis ist alles Umrandete, also alle 50 Prüfzeichen. Rechts: dieselben 50 Seiten ohne eigene Prüfung, davor ein Kasten „zentrale Prüfstelle“; nur dieser ist umrandet.
- **Ablauf:** 1. Links erscheinen die 50 Prüfzeichen, eine Umrandung um alle. 2. Ein rotes Kreuz an einem Prüfzeichen: „ein Fehler hebt die Sicherheit auf“. 3. Rechts erscheint die zentrale Prüfstelle, die Umrandung ist nur um sie. 4. Ein rotes Kreuz in einer Seite außerhalb der Basis: „darf Fehler haben, ohne dass die Sicherheit leidet“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Nicht die Größe des Systems zählt, sondern die Größe der Teile, auf deren Korrektheit die Sicherheit angewiesen ist.
- **Szenenname:** cyber/k1basis
- **Editor-Lücke:** machbar

### V14 [B] Offenes Verfahren: Geheimnis ist der Schlüssel, nicht das Verfahren
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/07-sicherheitsprinzipien-systeme-robust-entwerfen.md
- **Stelle:** Kein Verlass auf ein geheimes Verfahren — „Ein Hersteller von Funkschlüsseln für Autos hält sein selbst erdachtes Verschlüsselungsverfahren geheim.“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Spalten. Links „geheimes Verfahren“: ein Kasten „Verfahren (für alle Autos gleich)“ über sechs Auto-Rechtecken. Rechts „offenes Verfahren, Schlüssel je Auto“: ein Kasten „bekanntes, geprüftes Verfahren“ und sechs Autos mit je eigenem kleinen Schlüsselkasten.
- **Ablauf:** 1. Beide Seiten erscheinen. 2. Ein Angreifer liest bei einem Auto den Schlüssel aus und findet das Verfahren heraus (Pfeil zum Verfahrenskasten). 3. Links färben sich alle sechs Autos orange: „alle zugleich gefährdet, Austausch nur durch neue Elektronik“. 4. Rechts färbt sich nur das eine Auto orange: „nur dieses eine“. — Haltepunkte: Schritt 3 gegen 4.
- **Verständnisproblem:** Warum ein kleines austauschbares Geheimnis besser ist als ein großes unveränderliches.
- **Szenenname:** cyber/k1offenesverfahren
- **Editor-Lücke:** machbar

Verworfen: E-Mail-Absender 1982 (C), Pflicht-Passwortwechsel (C).

### Artikel 08 — Schwachstellen benennen und bewerten (Soll 5, vorh. 2)

### V15 [A] CVE benennt den Einzelfall, CWE die Art
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/08-schwachstellen-benennen-und-bewerten.md
- **Stelle:** CWE: die Art des Fehlers — „Eine CVE-Kennung benennt einen Einzelfall …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Ebenen. Unten Einzelfall-Kästen (CVE): „Log4Shell, CVE-2021-44228, Apache Log4j2“ sowie die Fälle des Kapitels „Kundenportal, Rechnungsnummer“, „Router, Werkspasswort“, „Geldautomaten“ (ohne erfundene CVE-Nummern, mit dem Vermerk „Fall“). Oben Art-Kästen (CWE): CWE-917 (Log4Shell, laut Aufgabe 12), CWE-639 „Umgehen der Rechteprüfung über einen vom Nutzer gewählten Schlüssel“, CWE-1393 „Werkspasswort“, CWE-367 „Time-of-check Time-of-use“. Pfeile verbinden jeden Fall mit seiner Art.
- **Ablauf:** 1. Ein Einzelfallkasten „Log4Shell, CVE-2021-44228, Apache Log4j2“ erscheint: „welcher Fehler in welchem Produkt“. 2. Ein Pfeil nach oben zur Art CWE-917: „was für eine Art“. 3. Die drei Kapitelfälle erscheinen und werden ihren Arten zugeordnet (Pfeile). 4. Text: „Ursache an der Wurzel beheben statt jeden Einzelfall“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** CVE und CWE werden verwechselt; der Unterschied zwischen Einzelfall und Art.
- **Szenenname:** cyber/k1cvecwe
- **Editor-Lücke:** machbar

### V16 [B] Der Angriffsweg: AV als Entfernung zum Gerät
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/08-schwachstellen-benennen-und-bewerten.md
- **Stelle:** CVSS: die Schwere — Tabelle 2, Zeile „Angriffsweg“
- **Art:** neue Animation
- **Was zu sehen ist:** Konzentrische Kreise um ein Gerät: außen „Netz, aus der Ferne (N) 0,85“, dann „benachbartes Netz (A) 0,62“, „am Gerät mit Zugang (L) 0,55“, innen „Hände am Gerät (P) 0,2“. Ein Angreifer-Punkt außen. Ein Balken rechts, der den Faktor zeigt.
- **Ablauf:** 1. Gerät, Kreis N erscheint, Angreifer-Punkt dort, Balken 0,85. 2. Angreifer wandert einen Kreis nach innen (A), Balken 0,62. 3. Kreis L, 0,55. 4. Kreis P, 0,2: Der Angreifer muss körperlich am Gerät sein; Text „je schwerer erreichbar, desto kleiner der Faktor in E“. — Haltepunkte: Schritt 1 und 4.
- **Verständnisproblem:** Wie ein Merkmal wie AV in die Zahl eingeht: jedes Hindernis ist ein Faktor kleiner als 1.
- **Szenenname:** cyber/k1cvssweg
- **Editor-Lücke:** machbar (der Balken als Rechteck mit Scale)

### V17 [A] Log4Shell: Vektor lesen und die Zahl auf der Skala
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/08-schwachstellen-benennen-und-bewerten.md
- **Stelle:** CVSS: die Schwere — „Die NVD gibt für CVE-2021-44228 den Vektor …“
- **Art:** neue Animation
- **Was zu sehen ist:** Oben der Vektor `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H` als Text in Teilen. Darunter ein Zahlenstrahl 0 bis 10 mit farbigen Stufen (keine 0,0; niedrig 0,1 bis 3,9; mittel 4,0 bis 6,9; hoch 7,0 bis 8,9; kritisch 9,0 bis 10,0).
- **Ablauf:** 1. Der Vektor erscheint. 2. Die Teile werden nacheinander hervorgehoben (Indicate), jeder mit einem Satz: AV:N aus der Ferne; AC:L ohne Bedingungen; PR:N ohne Anmeldung; UI:N ohne Nutzer; S:C Folgen reichen weiter; C:H, I:H, A:H alle drei Schutzziele schwer. 3. Der Zahlenstrahl erscheint, ein Marker springt auf 10,0, „kritisch“. — Haltepunkte: jeder Teil.
- **Verständnisproblem:** Wie man einen Vektor liest und dass die Stufe aus der Zahl folgt.
- **Szenenname:** cyber/k1cvssvektor
- **Editor-Lücke:** machbar (Teile des Vektors als einzelne Texte; ein Table mit einzelnen Zellen wäre L9)

Die beiden vorhandenen Bilder werden animiert (siehe unten). Verworfen: Zero-Day-Dauern als Balkenbild (C), Patch-Vergleich (C).

### Artikel 09 — Computerstrafrecht: was verboten ist (Soll 5, vorh. 0)

### V18 [A] Ein Straftatbestand ist eine Prüfliste mit Und-Verknüpfung
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/09-computerstrafrecht-was-verboten-ist.md
- **Stelle:** Was du dafür brauchst: wie ein Straftatbestand gebaut ist — „Gesetzestexte wirken auf den ersten Blick wie lange, verschachtelte Sätze.“
- **Art:** neue Animation
- **Was zu sehen ist:** Links eine Spalte kleiner Merkmalskästchen, rechts ein Kasten „strafbar nach dieser Vorschrift“, dazwischen eine Und-Verknüpfung (TextBox „UND“, ein Ausgangspfeil). Erste Fassung: Diebstahl (§ 242) mit den Merkmalen „Sache“, „beweglich“, „fremd“, „Wegnahme“, „Absicht der Zueignung“, „Vorsatz“. Zweite Fassung: § 202a mit den sieben Merkmalen Daten, nicht für ihn bestimmt, besonders gesichert, Zugang verschafft, unter Überwindung der Sicherung, unbefugt, Vorsatz.
- **Ablauf:** 1. Fahrrad-Beispiel: Die Merkmale erscheinen nacheinander und werden grün (Haken). 2. „Absicht der Zueignung“ bleibt rot (Kreuz), der Ausgangspfeil bleibt aus; Text „ein Merkmal fehlt, die Vorschrift greift nicht“, daneben „aber § 248b, unbefugter Gebrauch“. 3. Zweite Fassung mit dem Postfach-Beispiel (Student liest Nachrichten der früheren Freundin): sieben Haken nacheinander, dann leuchtet der Ausgang „strafbar, bis 3 Jahre oder Geldstrafe“. — Haltepunkte: Schritt 2 und die letzte Zeile.
- **Verständnisproblem:** Dass jedes Merkmal erfüllt sein muss und dass das Fehlen eines Merkmals nur diese eine Vorschrift ausschließt (nicht jede Strafbarkeit).
- **Szenenname:** cyber/k1tatbestand
- **Editor-Lücke:** machbar (Zellen/Kästchen einzeln betonen sonst L9)

### V19 [A] Gespeichert oder unterwegs: § 202a und § 202b
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/09-computerstrafrecht-was-verboten-ist.md
- **Stelle:** Abfangen von Daten (§ 202b StGB) — „Daten können nicht nur dort ausgespäht werden, wo sie gespeichert sind, sondern auch unterwegs.“
- **Art:** neue Animation
- **Was zu sehen ist:** Datenfluss von links nach rechts: Kasten „Speicher mit Passwort (gesicherte Daten)“, Pfeil „Übermittlung“ (Funkstrecke, Wellenlinien als Text), Kasten „Empfängergerät“. An der Funkstrecke ein Lauscher-Kästchen, darunter ein zweites Lauscher-Symbol neben dem Gerät mit „Abstrahlung“. Rechts zwei Rahmen: „§ 202a“ am Speicher, „§ 202b“ an der Funkstrecke und an der Abstrahlung.
- **Ablauf:** 1. Speicher mit Schloss erscheint; der Angreifer geht „unter Überwindung der Sicherung“ hinein (Schloss wird orange): § 202a. 2. Daten wandern als Punkt vom Speicher zum Gerät. 3. Ein Lauscher zeichnet die Übermittlung mit technischem Mittel auf: § 202b, Text „keine Sicherung nötig, nichtöffentlich genügt“. 4. Ein zweiter Lauscher am Gerät fängt die Abstrahlung auf: ebenfalls § 202b. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Der Unterschied zwischen Ausspähen (gespeicherte, gesicherte Daten) und Abfangen (unterwegs oder abgestrahlt, keine Sicherung nötig).
- **Szenenname:** cyber/k1speicherunterwegs
- **Editor-Lücke:** machbar

### V20 [A] Vorbereitung, Versuch, Vollendung: wo setzt die Strafbarkeit an?
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/09-computerstrafrecht-was-verboten-ist.md
- **Stelle:** Vorbereiten des Ausspähens und Abfangens (§ 202c StGB) — „Das Strafrecht setzt hier schon vor der eigentlichen Tat an …“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Zeitstrahl mit drei Abschnitten: „Vorbereitung“ (Passwörter oder Programm, deren Zweck die Tat ist, herstellen, verkaufen), „Versuch“ (unmittelbar ansetzen), „Vollendung“ (Zugang verschafft / Daten verändert). Unter dem Zeitstrahl eine Table mit den Vorschriften § 202a, § 202b, § 202c, § 202d, § 303a, § 303b, § 263a als Zeilen und den Spalten „Vorbereitung strafbar?“ und „Versuch strafbar?“ (Haken oder Kreuz nach Tabelle 3 und den Absätzen im Text).
- **Ablauf:** 1. Zeitstrahl baut sich von links nach rechts auf, ein Punkt wandert darauf. 2. Am Abschnitt „Vorbereitung“ erscheint § 202c als eigene Vorschrift. 3. Am Abschnitt „Versuch“ färben sich die Zellen: § 202a, § 202b, § 202c, § 202d: nein; § 303a, § 303b, § 263a: ja. 4. Beim Abschnitt „Vollendung“ gelten alle. Text „Straftat nach § 202a/b vorbereiten: § 202c; nach § 303a, § 303b, § 263a: dort jeweils eigener Satz“ (Absätze im Text). — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Dass der Versuch nur strafbar ist, wenn das Gesetz es sagt, und dass einige Vorschriften schon Vorbereitung bestrafen.
- **Szenenname:** cyber/k1versuch
- **Editor-Lücke:** machbar (Zellen einzeln betonen: L9)

### V21 [B] Welche Vorschrift schützt welches Schutzziel
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/09-computerstrafrecht-was-verboten-ist.md
- **Stelle:** Computerbetrug (§ 263a StGB), vor Tabelle 3 — „Die letzte Vorschrift schützt nicht Daten, sondern Vermögen …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Schutzziele Vertraulichkeit, Integrität, Verfügbarkeit (TextBoxen), rechts die Vorschriften, in Gruppen: § 202a, § 202b, § 202d bei Vertraulichkeit; § 303a bei Integrität; § 303b bei Verfügbarkeit; § 202c vor allen (Vorbereitung); § 263a als eigener Kasten „Vermögen“. Pfeile verbinden.
- **Ablauf:** 1. Die drei Schutzziele erscheinen. 2. Pfeile zu § 202a, § 202b, § 202d. 3. Pfeil zu § 303a. 4. Pfeil zu § 303b. 5. § 202c als Klammer davor, § 263a als Kasten „Vermögen“ abseits. — Haltepunkte: Schritt 4.
- **Verständnisproblem:** Die Paragraphen sind sonst eine Liste; die Zuordnung zu den Schutzzielen aus Abschnitt 1 gibt ihnen Ordnung.
- **Szenenname:** cyber/k1paragraphenziele
- **Editor-Lücke:** machbar

### V22 [B] Überlastungsangriff (DoS und DDoS)
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/09-computerstrafrecht-was-verboten-ist.md
- **Stelle:** Computersabotage (§ 303b StGB) — „Nummer 2 erfasst einen Angriff, der aus lauter für sich harmlosen Anfragen besteht.“
- **Art:** vorhandene Szene wiederverwenden (`cyber/k1flut` aus V5, ergänzt um eine zweite Fassung, in der die Anfragen von vielen Absendern kommen = DDoS)
- **Was zu sehen ist:** wie V5; in der zweiten Fassung kommen die Punkte aus fünf Quellen statt einer, Beschriftung „verteilt (DDoS)“.
- **Ablauf:** wie V5, dazu: 1. Eine Quelle schickt Anfragen (DoS). 2. Fünf Quellen schicken gleichzeitig (DDoS). — Haltepunkte: Schritt 2.
- **Verständnisproblem:** Dass jede einzelne Anfrage harmlos ist und erst die Masse den Dienst stört; Zusammenhang mit Verfügbarkeit.
- **Szenenname:** cyber/k1flut
- **Editor-Lücke:** braucht Editor-Funktion: L6 (viele bewegte Punkte); Notbehelf: wenige einzelne Punkte per Shift

### Artikel 10 — Erlaubnis, Werkzeuge und gute Absicht (Soll 4, vorh. 0)

### V23 [A] Der Umfang der Erlaubnis: Systeme, Zeitraum, Methoden
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/10-erlaubnis-werkzeuge-und-gute-absicht.md
- **Stelle:** Die Erlaubnis des Berechtigten — „Hat der Verfügungsberechtigte eingewilligt, dass jemand eine Handlung …“ (Beispiel Onlinehändler)
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Rahmen „Erlaubnis“ mit drei Achsen als Kästen: Systeme (shop.example), Zeitraum (10. bis 14. März) und Methoden (ohne Überlastungsangriffe). Außerhalb des Rahmens: „Server des Zahlungsdienstes“, „15. März“, „Überlastungstest“. Ein Punkt „Prüferin“.
- **Ablauf:** 1. Der Rahmen mit den drei Angaben erscheint („schriftlich festgehalten“). 2. Die Prüferin testet am 12. März die Webseite: Haken, „befugt“. 3. Sie testet am 15. März: der Punkt wandert aus dem Zeitraum, Kreuz, „unbefugt“. 4. Sie testet den Server des Zahlungsdienstes: Kreuz, „gehört einem anderen Verfügungsberechtigten“. 5. Überlastungstest: Kreuz, „Methode ausgeschlossen“. — Haltepunkte: Schritt 1 und 4.
- **Verständnisproblem:** Die Erlaubnis gilt nur so weit, wie der Berechtigte sie erteilt hat; dieselbe Technik ist im Umfang befugt, außerhalb unbefugt.
- **Szenenname:** cyber/k1umfang
- **Editor-Lücke:** machbar

### V24 [A] Antragsdelikt: Frist läuft, die Tat bleibt eine Straftat
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/10-erlaubnis-werkzeuge-und-gute-absicht.md
- **Stelle:** Antragsdelikt heißt nicht erlaubt — „Manche Taten verfolgt der Staat nur, wenn der Verletzte es verlangt.“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Zeitstrahl in zwei Spuren. Obere Spur „Strafbarkeit“: ein durchgehender Balken ab der Tat (rot). Untere Spur „Verfolgung“: Ereignisse „Tat“, „Hochschule erfährt von Tat und Täter“ (Fristbeginn), Fristbalken „3 Monate“, „Strafantrag“; daneben „Staatsanwaltschaft ohne Antrag, wenn besonderes öffentliches Interesse“ und „Schadensersatz unabhängig“. Beispiel: Studentin dringt in den Hochschulserver ein, der Administrator will nichts unternehmen.
- **Ablauf:** 1. Die Tat erscheint, der rote Balken der Strafbarkeit beginnt. 2. Der Administrator sagt „kein Problem“ (Text), der rote Balken bleibt. 3. Die Hochschule erfährt von Tat und Täter, der Fristbalken von 3 Monaten wächst (Scale). 4. Der Strafantrag liegt innerhalb der Frist, Verfolgung beginnt. 5. Daneben die Alternative: ohne Antrag nur bei besonderem öffentlichen Interesse. — Haltepunkte: Schritt 2 und 3.
- **Verständnisproblem:** Antrag betrifft die Verfolgung, nicht die Strafbarkeit; verfügungsberechtigt ist die Hochschule, nicht der Administrator.
- **Szenenname:** cyber/k1antrag
- **Editor-Lücke:** machbar

### V25 [B] Dual-Use-Werkzeug: derselbe Befehl, zwei Welten
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/10-erlaubnis-werkzeuge-und-gute-absicht.md
- **Stelle:** Werkzeuge besitzen: der Beschluss von 2009 — „Ein Werkzeug, das sich für erlaubte und für unerlaubte Zwecke gleichermaßen eignet, heißt Dual-Use-Werkzeug.“
- **Art:** neue Animation
- **Was zu sehen ist:** In der Mitte ein Kasten „nmap (Dual-Use)“. Links ein Pfeil zum eigenen Heimnetz (Student, Verfügungsberechtigter): Haken. Rechts ein Pfeil zu den Rechnern eines Unternehmens ohne Erlaubnis: Kreuz, „§ 202a, wenn er eindringt“. Unten ein zweiter Kasten „Programm mit Werbung ‚Knackt jedes Instagram-Konto‘“: Pfeil zu „§ 202c“.
- **Ablauf:** 1. Das Werkzeug erscheint, Text „Eignung genügt nicht, es kommt auf den Zweck an“. 2. Pfeil zum Heimnetz, Haken. 3. Pfeil zu fremden Rechnern, Kreuz; Text „nicht der Besitz, sondern der Einsatz“. 4. Das Programm mit der Werbung erscheint: Der Zweck zeigt sich objektiv, § 202c. — Haltepunkte: Schritt 3 und 4.
- **Verständnisproblem:** Wieso ein Werkzeug erlaubt und sein Einsatz verboten sein kann; Abgrenzung zur Schadsoftware.
- **Szenenname:** cyber/k1dualuse
- **Editor-Lücke:** machbar

### V26 [B] Gute Absicht schützt nicht: beobachten oder ausprobieren
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/10-erlaubnis-werkzeuge-und-gute-absicht.md
- **Stelle:** Gute Absicht schützt nicht — „Angenommen, jemand dringt ohne Erlaubnis in ein fremdes System ein …“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine Weggabelung. Oben ein Kasten „Student bemerkt: Nummer in der Adresse“. Zwei Wege: A „nur beobachten und melden“ (grün, „sichere Seite“) und B „Nummer ändern, fremde Daten abrufen, dann melden“ (orange, „§ 202a, trotz Meldung“). Rechts bei B zwei Texte: „Motiv ist kein Merkmal“, „wirkt höchstens auf die Strafhöhe“.
- **Ablauf:** 1. Der Student erscheint mit der Beobachtung. 2. Weg A erscheint, er gelangt zur Meldung. 3. Weg B erscheint; der Punkt geht über die Grenze „fremde Daten abrufen“, der Rahmen färbt sich orange; die Meldung danach ändert nichts. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Dass nicht das Motiv, sondern die Handlung entscheidet, und wo die Grenze zwischen Beobachten und Eindringen liegt.
- **Szenenname:** cyber/k1gabelung
- **Editor-Lücke:** machbar

Verworfen: Meldefristen NIS-2, CRA und DSGVO (24 h, 72 h, ein Monat) als Zeitleiste im Hintergrund-Kasten (C).

### Artikel 11 — Offenlegung und Ethik (Soll 5, vorh. 2)

### V27 [A] Webadresse zerlegen: Verfahren, Domain, Pfad
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/11-offenlegung-und-ethik.md
- **Stelle:** Was du dafür brauchst: der Aufbau einer Webadresse — „Eine Adresse wie https://app.example.com/konto/rechnungen besteht aus drei Teilen.“
- **Art:** neue Animation
- **Was zu sehen ist:** Die Adresse `https://app.example.com/konto/rechnungen` als Text, darunter drei Klammern (Brace): „Verfahren“, „Domain (Name des Rechners)“, „Pfad (welche Seite auf diesem Rechner)“. Darunter ein Domain-Baum, von rechts nach links gelesen: `com` ← `example` ← `app`.
- **Ablauf:** 1. Die Adresse erscheint (Write). 2. Die Klammer „https“ erscheint. 3. Die Domain wird markiert; darunter wird sie von rechts nach links aufgebaut: com, example.com (die registrierte Organisation), app.example.com (ein Rechner dieser Organisation), daneben intern.example.com als zweiter Zweig. 4. Der Pfad wird markiert; ein zweiter Pfad `/impressum.html` ersetzt ihn: „derselbe Rechner, eine andere Seite“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Der Leser muss Domain und Pfad auseinanderhalten, um Umfang, security.txt und `/.well-known/` zu verstehen.
- **Szenenname:** cyber/k1adresse
- **Editor-Lücke:** machbar

### V28 [A] Wann wird veröffentlicht: Full Disclosure gegen koordinierte Offenlegung
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/11-offenlegung-und-ethik.md
- **Stelle:** Koordinierte Offenlegung — „Damit ein Hersteller eine Meldung nicht endlos liegen lässt, setzen viele Finder Fristen.“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Zeitachsen untereinander (schematisch, ohne Zahlenwerte an den Kurven). Obere „Full Disclosure“: Ereignis „Einzelheiten öffentlich“ am Anfang, danach steigt die Angriffskurve (qualitativ, Area), der Patch kommt erst viel später. Untere „koordiniert“: „Meldung (vertraulich)“, Frist „90 Tage“ für den Patch, „Patch“, dann nach „30 Tage“ die Einzelheiten; Angriffskurve bleibt niedrig und steigt erst danach leicht. Zusatz: „bei bereits ausgenutzter Lücke: 7 Tage“.
- **Ablauf:** 1. Beide Achsen erscheinen. 2. Oben: Veröffentlichung, die Kurve steigt steil, der Patch fehlt noch. 3. Unten: Meldung, Fristbalken von 90 Tagen wächst, Patch, danach 30 Tage Wartezeit, dann Veröffentlichung; die Kurve bleibt klein. 4. Der Hinweis „7 Tage bei nachweislicher Ausnutzung“ erscheint. — Haltepunkte: Schritt 2 und 3.
- **Verständnisproblem:** Warum Fristen: Schweigen lässt den Hersteller trödeln, sofortiges Veröffentlichen lässt Angriffe vor dem Patch wachsen. Die Kurven sind ein Schemabild, die Größe der Kurve ist nicht gemessen (im Bild so kennzeichnen).
- **Szenenname:** cyber/k1fristen
- **Editor-Lücke:** machbar

### V29 [B] Zufallsfund: fünf Schritte
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/11-offenlegung-und-ethik.md
- **Stelle:** Was man bei einem Zufallsfund tut — „Bemerkt man bei der gewöhnlichen, erlaubten Benutzung eines fremden Systems …“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine Ablaufleiste mit fünf Kästen: Aufhören, Nichts mitnehmen, Aufschreiben, Koordiniert melden, Schweigen bis zur Abstimmung. Darüber die Szene der Kundin mit der Adresse `.../rechnung?nr=1041`; ein Stopp-Zeichen vor „nr=1042 ausprobieren“.
- **Ablauf:** 1. Die Kundin sieht in der eigenen Adresse die fortlaufende Nummer. 2. Ein Pfeil zu „1042 ausprobieren“ wird durchgestrichen (Mark), Kasten 1. 3. Kasten 2: Hand zum Download durchgestrichen. 4. Kasten 3: Notizzettel. 5. Kasten 4: Brief an den Sicherheitskontakt (Umschlag wandert zur Firma). 6. Kasten 5: Uhr/Pause, „bis die Lücke behoben oder die Veröffentlichung abgestimmt ist“. — Haltepunkte: Schritt 2 und 5.
- **Verständnisproblem:** Die Reihenfolge und der Grund jedes Schritts: Der Betreiber kann prüfen, der Finder soll nur beschreiben.
- **Szenenname:** cyber/k1zufallsfund
- **Editor-Lücke:** machbar

### Artikel 12 — Das Wichtigste bis hier (Soll 1, vorh. 0)

### V30 [A] Zusammenschau: „Wer darf was?“
- **Artikel:** content/cyber/01-sicherheit-schutzziele-und-spielregeln/12-das-wichtigste-bis-hier.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Fast alles in diesem Kapitel ist eine Antwort auf die Frage: Wer darf was?“
- **Art:** neue Animation (Zusammenschau)
- **Was zu sehen ist:** In der Mitte eine große TextBox „Wer darf was?“, im Kreis zehn kleinere TextBoxen mit den Zeilen der Tabelle: Schutzziele, Angriff, Risiko und Angreifermodell, Richtlinie und Mechanismus, Minimale Rechte und sichere Voreinstellung, Lückenlose Prüfung und TOCTTOU, Verteidigungslinien und kleine Basis, Schwachstelle/CVE/CWE/CVSS, §§ 202a bis 303b, Erlaubnis/Werkzeug/gute Absicht, Offenlegung und Spielregeln (elf Speichen, in drei Gruppen farbig: Begriffe, Gestaltung, Spielregeln).
- **Ablauf:** 1. Die Mitte erscheint. 2. Die Speichen erscheinen nacheinander in der Reihenfolge der Abschnitte, jede mit einem Kurzsatz (z. B. „nur Berechtigte dürfen erfahren, verändern, nutzen“). 3. Zum Schluss färben sich die drei Gruppen (Indicate). — Haltepunkte: Schritt 2 (je nach Speiche).
- **Verständnisproblem:** Der integrierende Gedanke des Kapitels (Berechtigung), der die Abschnitte verbindet.
- **Szenenname:** cyber/k1werdarfwas
- **Editor-Lücke:** machbar

## Vorhandene Abbildungen

- cyber/k1brief (02-was-geschutzt-wird…): animieren ja — Schritte: 1. Absender und Empfänger erscheinen, ein Brief wandert (Shift) zum Empfänger. 2. Drei Fälle nacheinander: Leser mit Auge greift ab (Vertraulichkeit), Inhalt wird durchgestrichen und ersetzt (Integrität), der Brief wird angehalten und kommt nicht an (Verfügbarkeit). 3. Siegel/Umschlag als Schutz zuletzt. | Lücke: machbar (Ersetzen des Inhalts als zweiter Text; sonst L1/L2)
- cyber/k1kette (03-von-der-schwachstelle…): animieren ja — Schritte: 1. Haus mit Schwachstelle (Kellerfenster) erscheint, Text „solange niemand kommt, passiert nichts“. 2. Bedrohung (Einbrecher in der Gegend) erscheint und bewegt sich zum Fenster. 3. Angriff mit Exploit (Schraubenzieher). 4. Schaden (Laptop weg). 5. Vier Sperr-Marken nacheinander an den Pfeilen: Fenster reparieren, Zaun, Alarmanlage, Tresor. Haltepunkte: 1 und 5. | Lücke: machbar
- cyber/k1rerwartung (04-risiko…): animieren ja — Schritte: 1. Fahrradschlauch: 3 × 15 € erscheint, dann 45 €/Jahr. 2. Wasserschaden: 0,05 × 10 000 € = 500 €/Jahr. 3. Zwanzig Jahre als Zeile von Kästchen (Stem), 19 mit 0, eines mit 10 000 €; Summe wandert durch 20, ergibt 500 €. Haltepunkt: 3. | Lücke: machbar (Σ- und Arithmetik-Operation); Σ mit Zahlen ist Rechenbild-Pflicht
- cyber/k1rwuerfel (04-risiko…): entfällt als eigene Abbildung (Kern „Faktor n-mal“ erscheint in k1rflaeche; Würfelrechnung bleibt als Text). Falls dennoch behalten: Produkt mit der ∏-Operation, Faktoren 5/6 nacheinander, am Ende 1 − 0,482 = 0,518. | Lücke: machbar
- cyber/k1rrisiko (04-risiko…): entfällt (geht in k1rgesamt auf; die zwei Produkte sind dort die ersten Schritte).
- cyber/k1risiko (04-risiko…): animieren ja — Schritte: 1. Logarithmische Achsen mit Teilstrichen. 2. Punkt A (0,1/Jahr, 50 000 €) mit Hilfslinien. 3. Punkt B (10/Jahr, 100 €). 4. Rote Gerade durch A (gleiches Risiko 5 000), blaue durch B (1 000); Text „5 : 1“. 5. Pfeil nach rechts oben „Risiko steigt“. Haltepunkte: 3 und 4. | Lücke: machbar
- cyber/k1rgesamt (04-risiko…): animieren ja — Schritte: 1. R_A = 0,1 · 50 000 = 5 000 (hier aufgegangen: k1rrisiko). 2. R_B = 10 · 100 = 1 000. 3. Summe 6 000 €/Jahr, Bruch „fünf Sechstel aus A“. Haltepunkt: 3. | Lücke: machbar (Σ-Operation)
- cyber/k1rnutzen (04-risiko…): animieren ja — Schritte: 1. R_vorher 5 000. 2. 80 %: R_nachher 1 000, N = 5 000 − 1 000 − 2 000 = +2 000. 3. 30 %: R_nachher 3 500, N = −500. 4. Schwelle K/R_A = 40 % auf einem Balken, beide Fälle als Marker. Haltepunkt: 4. | Lücke: machbar
- cyber/k1rflaeche (04-risiko…): animieren ja — Schritte: 1. n = 10 Faktoren 0,98 nacheinander (∏-Operation), Produkt 0,817, Gegenereignis 0,183. 2. Sieben Faktoren verschwinden (n = 3): Produkt 0,941, P = 0,059. Haltepunkt: 1 und 2. | Lücke: machbar (∏ mit Zahlen: Pflicht)
- cyber/k1rtrennung (06-sicherheitsprinzipien-rechte…): animieren ja — Schritte: 1. Eine Person: q = 0,01. 2. Zweite Person, unabhängig: q · q = 0,0001. 3. Vergleich: hundertmal seltener. Haltepunkt: 3. | Lücke: machbar (∏)
- cyber/k1toctou (06-sicherheitsprinzipien-rechte…): animieren ja — Schritte: 1. Konto mit 100 €. 2. Automat 1 prüft (100 ≥ 100, Haken). 3. Automat 2 prüft (noch 100, Haken). 4. Automat 1 zahlt aus, bucht ab. 5. Automat 2 zahlt aus, Konto bei −100 €, 200 € ausgezahlt. 6. Atomare Variante: Automat 2 wartet, sieht 0 € und lehnt ab. Haltepunkte: 3 und 5. | Lücke: machbar
- cyber/k1schichten (07-sicherheitsprinzipien-systeme…): animieren ja, mit k1rlinien zu einer Szene vereint — Schritte: 1. Schatz in der Mitte. 2. Wache (0,05) erscheint, 3. Mauer (0,1), 4. Graben (0,3), jeweils mit Faktor. 5. Ein Angreifer-Punkt versucht der Reihe nach, durchzukommen; das Produkt 0,3 · 0,1 · 0,05 = 0,0015 erscheint (∏-Operation). Haltepunkte: 4 und 5. | Lücke: machbar
- cyber/k1rlinien (07-sicherheitsprinzipien-systeme…): entfällt (geht in k1schichten auf).
- cyber/k1reinfach (07-sicherheitsprinzipien-systeme…): animieren ja — Schritte: 1. n = 3 Bauteile, je Faktor 0,99, Produkt 0,970, P = 0,030. 2. n = 10, Produkt 0,904, P = 0,096. Haltepunkt: 2. | Lücke: machbar (∏)
- cyber/k1rcvss (08-schwachstellen-benennen…): animieren ja — Schritte: 1. ISS: drei Faktoren 0,44 (∏), 1 − 0,0852 = 0,9148. 2. W = 7,52 · (ISS − 0,029) − 3,25 · (ISS − 0,02)^15 = 6,0477 (Zwischenwerte in einer Zeile). 3. E: fünf Faktoren 8,22 · 0,85 · 0,77 · 0,85 · 0,85 = 3,8870. 4. 1,08 · (W + E) = 10,73, begrenzt auf 10,0. Haltepunkte: 3 und 4. | Lücke: machbar (∏-Operation, Rest Arithmetik)
- cyber/k1zyklus (08-schwachstellen-benennen…): animieren ja — Schritte: 1. Zeitachse mit Entstehung des Fehlers. 2. Entdeckung durch Angreifer; rote Phase „Zero-Day“ beginnt. 3. Meldung an den Hersteller, 4. Patch und Veröffentlichung: Phase wechselt zu orange („n-day“). 5. Betreiber spielen das Update ein, die Phase endet. Haltepunkte: 2 und 4. | Lücke: machbar
- cyber/k1offenlegung (11-offenlegung-und-ethik): animieren ja — Schritte: 1. Finder, Hersteller, Koordinator, Öffentlichkeit erscheinen. 2. Vertrauliche Meldung (Umschlag wandert zum Hersteller). 3. Keine Reaktion: Pfeil zum Koordinator, der vermittelt. 4. Patch bereit. 5. Erst jetzt wandert die Veröffentlichung zur Öffentlichkeit. Haltepunkte: 3 und 5. | Lücke: machbar
- cyber/k1entscheidung (11-offenlegung-und-ethik): animieren ja — Schritte: 1. Die Frage „Darf ich das testen?“. 2. Frage 1 (eigenes System), 3. Frage 2 (isoliertes Labor), 4. Frage 3 (Lernplattform) erscheinen nacheinander, jeweils mit Ja-Pfeil zu „testen, im Rahmen der Antwort“. 5. Nein-Pfeile führen zu „nicht testen“. 6. Beispiel läuft durch: das Thermostat im eigenen Heimnetz, dann das Gerät des Freundes ohne Erlaubnis. Haltepunkte: 6. | Lücke: machbar

Insgesamt: 18 Szenen vorhanden, 15 eignen sich zum Animieren; 3 entfallen als eigene Abbildung (k1rwuerfel, k1rrisiko, k1rlinien).
