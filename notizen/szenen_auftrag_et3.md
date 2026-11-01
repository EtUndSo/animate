# Auftrag: ET3-Abbildungen als Editor-Szenen

Ziel: Jede Abbildung der ET3-Arbeitshefte wird zu einer Szene des EtUndSo-Editors (web/szenen/et3/<name>.json). Daraus entstehen die Bilder der Website-Artikel in vier Sprachen. Nur Editor-Szenen, keine anderen Grafiken.

## Quellen
- Hefte: C:\Bücher\ET3\Arbeitshefte\kap<N>_stufen*.tex (deutsch), dazu *_en.tex, *_es.tex, *_zh.tex für die Wörter in den Bildern. Maßgeblich ist der Quelltext im `abb`-Block (bei Teil 2 auch ein `center`-Block mit `\captionof` im Kasten `vertiefung`): dieselben Funktionen, Bereiche, Punkte, Beschriftungen. Inhalt und Zahlen nicht ändern.
- Daten: C:\Bücher\ET3\Arbeitshefte\daten\*.dat
- Inventar mit Hinweisen je Abbildung: C:\Bücher\ET3\Arbeitshefte\ABBILDUNGEN_INVENTAR.md (Abschnitte 1.3 und 6). Stand vor dem Ausbau der Engine: Viele Umwege dort sind inzwischen unnötig.

## Werkzeuge (Repo C:\Users\info\PycharmProjects\pythonanimation)
- tools/szenen_lib.py: Bausteine (Klasse Szene). Zuerst lesen, ebenso die Regeln im Kopf der Datei.
- tools/szenen/et3_muster.py: vier Beispiele.
- python tools/szenen_ansehen.py <out.png> et3/<name> ... [--lang de|en|es|zh]: exportiert und macht ein Kontaktblatt. Das PNG mit dem Read-Tool ansehen.
- Der Editor-Server läuft auf localhost:8000 (nicht neu starten).
- Python-Skripte, die Backslashes enthalten, immer mit dem Write-Tool anlegen, nie per Bash-Heredoc: Dort werden Backslashes halbiert.

## Abbildungsnamen
Der Name kommt aus dem \label: fig:k1bode -> et3/k1bode. Fehlt die Ziffer (Teil 2: fig:bausteine, fig:linie, fig:sprung, fig:wege, fig:residuen), heißt die Szene et3/k2bausteine usw. Der Name muss exakt stimmen, sonst findet der Artikel das Bild nicht.

## Regeln
1. Eigene Datei tools/szenen/et3_teil<N>.py je Teil, eine Funktion je Abbildung. Muster-Szenen darfst du unter gleichem Namen überschreiben.
2. Höchstens 548 px breit in **allen vier** Sprachen (Export meldet es), besser 480-540. Text darf nicht kleiner als 22 Szenenpixel sein. Nichts außerhalb von x = ±7,1 und y = ±4.
3. Wörter nur über s.tr(key, de, en, es, zh), Texte aus den Heften übernehmen. Formelzeichen und Einheiten ohne Wörter bleiben einfache Strings. "t in s" ist ein Wort: de "t in s", en "t in s", es "t en s", zh "t / s". Dezimalzahlen im Quelltext mit Punkt: 0.5 (de und es zeigen dann 0,5).
4. Kurven aus Formeln, wenn die Ausdruckssprache des Editors es kann (Funktionen: sin cos tan exp ln log10 sqrt abs sign epsilon rect tri ramp si sinc max min where floor mod; `x` ist die Variable; Winkel in Bogenmaß; in pgfplots ist sin(360*x) in Grad, hier sin(2*pi*x)). Sonst Daten: s.daten(a, duenn(daten(pfad, x, y))). Stem-Werte vorher rechnen oder über func.
5. Nach Möglichkeit die Kurven direkt beschriften statt mit Legende, sonst s.legende. Reihenfolge und Anordnung der Teilbilder wie im Heft, denn die Bildunterschrift sagt oft „links“, „rechts“, „oben“. Bildunterschriften bleiben im Artikel, gehören nicht ins Bild. Lange Sätze im Bild dürfen als kurzer Teilbildtitel erscheinen, solange die Unterschrift den Inhalt trägt.
6. Farben: BLAU Hauptgröße, ROT Hervorhebung, GRUEN zweite Größe, ORANGE dritte, GRAU Nebensache; gestrichelt (DASH) = Näherung oder Hilfslinie. Wie im Heft, soweit möglich.
7. Prüfen: Jede Abbildung in de ansehen, jede mit Wörtern auch in zh und in der längsten Sprache. Keine überlappenden Texte, keine abgeschnittenen Kurven, Zahlen wie im Heft, Kurve durch die angegebenen Punkte. Zahlen im Bild gegen das Heft prüfen.
8. Nur eigene Dateien anlegen: tools/szenen/et3_teil<N>.py, web/szenen/et3/*.json, web/abbildungen/**. Nichts an Engine, Editor, build_wissen.py, content/ oder den Heften ändern, auch nichts committen. Fehlt der Engine etwas: Umweg nehmen und melden.
9. Fehler im Heft (falsche Kurve, falsche Zahl): nicht still übernehmen, im Bericht nennen.

## Bericht am Ende (knapp)
Fertige Abbildungen, breiteste Abbildung je Sprache, Umwege, gefundene Fehler in den Heften, offene Punkte.
