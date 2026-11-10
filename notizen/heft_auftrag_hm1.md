# Auftrag: Arbeitsheft für Höhere Mathematik 1 (hm1)

Ziel: Ein Arbeitsheft als LaTeX-Quelle, aus dem automatisch ein Website-Artikel wird (Studierende der Elektrotechnik im ersten Semester, Erklärplattform EtUndSo). Vorlage in Form und Stil sind die fertigen Hefte in C:\Bücher\ET1\Arbeitshefte, besonders Kap1_Feld.tex, kap1_stufen.tex, kap1_loesungen.tex und Kap4_Messen.pdf. Lies diese zuerst, dann C:\Bücher\EtUndSo\VORGABE_ARTIKEL.md (Abschnitte 1 bis 3; das Format dort ersetzt die Heftform nicht).

## Quelle
- Folientext: C:\Bücher\EtUndSo\_volltext\hm1_folien.txt, Marken `=== HM1Folien<N> Seite <P>`. Die Formeln sind im Text oft zerrissen. Die PDFs liegen unter C:\Bücher\EtUndSo\1.Semester\HöMa1\entpackt\Lernmaterialien\Folien\HM1Folien<N>.pdf: Lies zuerst den Folientext deines Abschnitts ganz, dann die PDFs mit Read: höchstens 6 bis 8 Seiten je Aufruf. Bei mehr verschwinden Seitenbilder ohne Fehlermeldung („media removed: request limit“). Prüfe vor dem Schreiben, dass du die Bilder wirklich gesehen hast, und nenne im Bericht, welche Seiten du gesehen hast.
- Handschriftliche Mitschriften mit Beweisen und Beispielen: entpackt\Lernmaterialien\Mitschriften\<Monat>\ (eine Datei je Vorlesung). Sie sind Pflichtquelle, denn fast alle Beweise und viele Definitionen stehen nur dort. Zuordnung grob: Folien n gehört zu den Vorlesungen VL 2n−1 und 2n, dazu die Extra-Vorlesungen im Dezember. Dateien ohne „quer“ im Namen nehmen. Übungsblätter unter entpackt\Übungsbetrieb\Übung <n> - ET\intro\ zeigen das Niveau.
- Liste zuerst alle Definitionen, Sätze und Formeln des Abschnitts auf. Alle müssen vorkommen. Beweise der Quelle kommen in `beweis`-Boxen vor, Schritt für Schritt, kein Schritt ohne Begründung. Überspringt die Quelle einen Beweis, reicht die Idee.
- Keine Aufgaben, Zahlenbeispiele oder Abbildungen wörtlich übernehmen. Eigene Beispiele, eigene Zahlen. Das Niveau der Quelle nicht überschreiten: erst der einfache, erwartete Lösungsweg, Weiterführendes nur als `vertiefung`.
- Im Heft steht nirgends ein Bezug zu Skript, Folien, Vorlesung, Übung, Uni, Klausur, Dozent oder Personen der Quelle, auch keine Satznummern der Quelle. Fehler der Quelle korrigierst du still und nennst sie im Bericht.

## Dateien in C:\Bücher\HöMa1\Arbeitshefte (Präambeln liegen dort)
- Kap<N>_<Name>.tex (Hauptdatei, Aufbau wie Kap1_Faltung.tex; Titelblock mit \LARGE und \large, Untertitel als Frage oder Kernaussage; „Arbeitsheft HöMa1 – Höhere Mathematik 1, Kapitel~N“ (seit 09.11.2026; Verweise „Kapitel~N, Abschnitt~M“, siehe notizen/kapitel_umstellung.md))
- kap<N>_stufen.tex, kap<N>_loesungen.tex
- rechnung_kap<N>.py: rechnet jede Zahl des Hefts nach, Brüche exakt, Aussagen ohne Zahlen durch erschöpfendes Prüfen an Beispielen. Erste Zeilen: `import sys; sys.stdout.reconfigure(encoding="utf-8")`, sonst bricht die Ausgabe unter Windows ab.
Der Name Kap<N>_<Name> steht im Einzelauftrag und muss exakt stimmen.

## Inhalt und Stil
- **Keine Vorgriffe:** Ein Abschnitt benutzt nur, was vorher eingeführt wurde. Kein „wie wir später sehen“, kein Klammerhinweis auf spätere Stufen, kein Begriff oder Ergebnis aus einer späteren Stufe. Ein Hinweis auf Kommendes nur als letzter Satz einer Stufe, in bekannten Worten, ohne neuen Begriff. Zusammenschau (Antwort in drei Sätzen, Prinzip-Tabelle) steht am Ende des Hefts. Jede Stufe wird auf der Website ein eigener kurzer Artikel, höchstens 10 000 Zeichen. Vorbild: heft_auftrag_gemb1.md.
- Rangfolge: physikalisch korrekt, verständlich ohne Vorwissen, vollständig gegenüber der Quelle, knapp. Nichts voraussetzen, was nicht im Heft oder einem früheren Teil steht. Die Leserin kennt nur Schulmathematik plus die früheren Teile, und auch Schulstoff wird kurz wiederholt, wo er gebraucht wird.
- **Umfang: höchstens 22 Seiten PDF einschließlich Inhaltsverzeichnis und Lösungen, 6 bis 8 Stufen, 6 bis 10 Abbildungen, 8 bis 12 Aufgaben.** Eine Stufe kostet rund 2 bis 3 Seiten. Knapp heißt: nichts Wichtiges weglassen, aber nichts doppeln, keine Tabellen oder Abschnitte zu Dingen, die später nicht gebraucht werden. Reicht der Platz nicht, zusammenfassen statt Stufen anhängen.
- Aufbau: `\section*{Worum es geht}` (direkt danach `\markboth{...}{...}` auf eigener Zeile, sonst steht das Inhaltsverzeichnis im Kopf) mit kernbox „Die Antwort in drei Sätzen (am Ende des Hefts sollen sie selbstverständlich sein)“, dann `\paragraph{Ein Prinzip hinter allen Ergebnissen.}` mit Tabelle „Ergebnis | Woher es kommt“, dann `\paragraph{So arbeitest du mit dem Heft.}` (wird beim Umwandeln ersetzt, kurz halten), dann merkbox mit dem Rechenmodell, bei Bedarf `\section*{Von Grund auf: ...}` (nur Grundbegriffe, die später gebraucht werden, höchstens eine Seite), dann `\section{Stufe 1: ...}` usw., am Ende kernbox `Das Wichtigste`, zuletzt `\section{Lösungen}`.
- Jede Stufe löst genau ein neues Problem und beginnt mit `zweck`. Dann `\paragraph{Die Idee.}` (anschaulich, Mechanismus in Worten), dann Satz oder Definition, `\textbf{So liest man das:}` (jedes Symbol mit Bedeutung und einem Beispielwert), Voraussetzungen, Herleitung in `herleitung`, ein Beispiel mit dem Rechenmodell, mindestens eine Grenzfall-Kontrolle, typische Fragen in `qa`, Aufgaben in `aufgabe`.
- Immer das Warum: welches Axiom, welcher Schluss, welche Voraussetzung erzeugt das Ergebnis. Jeden Fachbegriff bei der ersten Nennung sofort erklären und mit `\fb{...}` markieren. Analogien nur in `analogie`, mit dem Satz, wo sie nicht mehr stimmen. Stoff über die Quelle hinaus in `vertiefung`.
- Begriffe im Eingangsteil (kernbox, merkbox) bekommen eine Kurzerklärung im selben Satz, die ausführliche folgt in der Stufe. Die ersten acht `\fb{...}` des Hefts werden die Schlagwörter der Website: Dort die Grundform setzen („Ladung“, nicht „Ladungen“).
- Tabellen nur als `center` mit `tabular` oder `tabularx` und booktabs, ohne `table`, ohne Tabellennummer und ohne `\ref` darauf.
- Aufgaben: gemischt: rechnen, vorhersagen, Grenzfall, mit Schwierigkeit \stern bis \stern\stern\stern. Jede Aufgabe mit `\label{a:...}` und Lösung `\loesung{a:...}` in kap<N>_loesungen.tex, vollständig mit Zahlen. Theorie wird immer mit Rechnen verbunden, durch Aufgaben lernt man am meisten.
- Keine LTspice-Boxen: Mathematik lernt man durch Rechnen. Wo ein Begriff in der Elektrotechnik wiederkommt, reicht ein Satz dazu (Zeiger, Schwingung, Netzwerkgleichungen), ohne Verweis auf andere Module.
- Mathematische Sätze: `satz` und `definition`, Beweise in `beweis` (Titel kurz), nach jedem Satz `\textbf{So liest man das:}`, dann Beispiel und Gegenbeispiel. Warum jede Voraussetzung nötig ist, zeigt ein Fall, in dem sie fehlt und der Satz falsch wird. Abstrakte Begriffe erst am konkreten Fall, dann allgemein.
- Ton sachlich und klar, kurze Sätze, keine Füllwörter (einfach, offensichtlich, natürlich), keine Emojis, kein Bezug auf „wir im Kurs“. Aufgaben sprechen die Leserin mit du an.
- Präzision: Gleichgrößen groß, zeitabhängige klein. Vorzeichen und Zählpfeile ausdrücklich. Dezimalkomma `0{,}7`. Makros aus der Präambel: \dd \ee \jj \R \C \N \Z \Q \eps \fb. Listen mit (i), (ii): `enumerate` mit `[label=(\roman*)]`. Keine eigenen \newcommand in den Stufen-Dateien.

## Abbildungen
- Jede Stufe hat mindestens eine Abbildung. Schaltungen und Kurven werden nur mit dem Editor gezeichnet, nicht mit TikZ oder circuitikz.
- Im Heft steht:
  \begin{abb}\szene{k<N>name}\caption{...}\label{fig:k<N>name}\end{abb}
- Die Szene baust du in tools/szenen/hm1_teil<N>.py im Repo C:\Users\info\PycharmProjects\pythonanimation. Lies dazu notizen/szenen_auftrag_et3.md (Regeln 2 bis 7 gelten, Szenenname hm1/k<N>name), tools/szenen_lib.py und als Beispiele tools/szenen/et1_teil1.py und tools/szenen/et3_teil2.py (komplexe Ebene). 3D-Kamera: siehe speichern3d in tools/szenen/et1_teil10.py. Wörter in den Bildern in vier Sprachen über s.tr. Mischt eine Szene Achsen und freie Zeichnung: s.welt() als erstes Objekt.
- Danach: python tools/szenen_ansehen.py <out.png> hm1/... ; Bild ansehen; dann python tools/export_szenen.py hm1/name1 hm1/name2 ... (immer mit Namen, ohne Namen schreibt es alle Module neu); dann python tools/szenen_pdf.py hm1 "C:/Bücher/HöMa1/Arbeitshefte" <namen>.

## Bauen und prüfen
- pdflatex Kap<N>_<Name>.tex dreimal im Ordner, fehlerfrei; danach .aux .log .out .toc löschen. PDF mit Read ansehen und prüfen.
- python tools/heft_zu_artikel.py hm1 --kap <N> --lang de --pruefen --katex muss ohne Warnung durchlaufen (unbekannte Befehle, Verweise ohne Ziel, Aufgaben ohne Lösung, Formeln, die KaTeX nicht setzen kann).
- LaTeX und Python-Skripte nur mit Write oder Edit schreiben. Im Bash-Tool werden doppelte Backslashes halbiert und Heredocs mit dreifachen Anführungszeichen brechen ab.

## Grenzen
Nur eigene Dateien anlegen: die Heftdateien des eigenen Teils, tools/szenen/hm1_teil<N>.py, web/szenen/hm1/*, web/abbildungen/**. Nichts an Engine, Editor, build_wissen.py, heft_zu_artikel.py, den Präambeln oder content/ ändern, nichts committen. Andere Agenten schreiben parallel die anderen Teile. Auf andere Teile darfst du mit „Teil N“ verweisen, auch vorwärts, die Gliederung steht unten. Fertige Teile liegen im Heftordner, ihre Begriffe und Satznamen übernimmst du.

## Gliederung der Reihe
1 Mengen, Logik und reelle Zahlen · 2 Komplexe Zahlen · 3 Funktionen und Polynome · 4 Folgen und Grenzwerte · 5 Exponentialfunktion und Stetigkeit · 6 Unendliche Reihen · 7 Potenzreihen und Eulersche Formel · 8 Vektoren und Skalarprodukt · 9 Vektorprodukt und Basen · 10 Matrizen und lineare Gleichungssysteme

## Bericht am Ende (knapp)
Seitenzahl, Stufen, Aufgaben, Abbildungen, bewusst gekürzte Inhalte, Fehler der Quelle, offene Punkte.
