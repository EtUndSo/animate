# Auftrag: Arbeitsheft für Grundlagen der Elektrotechnik (ET1)

Ziel: Ein Arbeitsheft als LaTeX-Quelle, aus dem automatisch ein Website-Artikel wird (Lernende im ersten Semester, Erklärplattform EtUndSo). Vorlage in Form und Stil sind die fertigen ET3-Hefte in C:\Bücher\ET3\Arbeitshefte, besonders kap1_stufen.tex, kap1_loesungen.tex, Kap1_Faltung.tex und kap8_stufen.tex. Lies diese zuerst, dann C:\Bücher\EtUndSo\VORGABE_ARTIKEL.md (Abschnitte 1 bis 3; das Format dort ersetzt die Heftform nicht).

## Quelle
- Volltext des Skripts: C:\Bücher\EtUndSo\_volltext\get1_clean.txt, Marken `=== Seite N`. Die Seitenbereiche im Einzelauftrag meinen diese Marken, das sind die PDF-Seiten. Abbildungen und Formeln fehlen im Text teils; das PDF liegt unter C:\Bücher\EtUndSo\1.Semester\ET1\(VO) Grundgebiete der Elektrotechnik 1 - Einführung in die Schaltungsanalyse_20261018_2239\Vorlesung\Begleit-Skript zur Vorlesung\GET1_Lecture_Script_WS2425_3_03.pdf (Read mit pages, höchstens 20 Seiten je Aufruf).
- Liste zuerst alle Kerninhalte und Formeln des Abschnitts auf. Alle wichtigen Inhalte und Formeln müssen vorkommen. Lange Texte darfst du zusammenfassen.
- Keine Aufgaben, Zahlenbeispiele oder Abbildungen wörtlich übernehmen. Standardschaltungen und Allgemeinwissen sind frei. Eigene Zahlen, eigenes durchgehendes Rechenmodell.
- Im Heft steht nirgends ein Bezug zu Skript, Vorlesung, Übung, Uni, Praktikum, Klausur oder einer Seiten-, Bild- oder Gleichungsnummer der Quelle. Fehler der Quelle korrigierst du still und nennst sie im Bericht.

## Dateien in C:\Bücher\ET1\Arbeitshefte (Präambeln liegen dort)
- Kap<N>_<Name>.tex (Hauptdatei, Aufbau wie Kap1_Faltung.tex; Titelblock mit \LARGE und \large, Untertitel als Frage oder Kernaussage; „Arbeitsheft ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse, Kapitel~N“ (seit 09.11.2026; Verweise „Kapitel~N, Abschnitt~M“, siehe notizen/kapitel_umstellung.md))
- kap<N>_stufen.tex, kap<N>_loesungen.tex
- rechnung_kap<N>.py: rechnet jede Zahl des Hefts nach. Keine Zahl ohne Rechnung.
Der Name Kap<N>_<Name> steht im Einzelauftrag und muss exakt stimmen.

## Inhalt und Stil
- **Keine Vorgriffe:** Ein Abschnitt benutzt nur, was vorher eingeführt wurde. Kein „wie wir später sehen“, kein Klammerhinweis auf spätere Stufen, kein Begriff oder Ergebnis aus einer späteren Stufe. Ein Hinweis auf Kommendes nur als letzter Satz einer Stufe, in bekannten Worten, ohne neuen Begriff. Zusammenschau (Antwort in drei Sätzen, Prinzip-Tabelle) steht am Ende des Hefts. Jede Stufe wird auf der Website ein eigener kurzer Artikel, höchstens 10 000 Zeichen. Vorbild: heft_auftrag_gemb1.md.
- Rangfolge: physikalisch korrekt, verständlich ohne Vorwissen, vollständig gegenüber der Quelle, knapp. Nichts voraussetzen, was nicht im Heft oder einem früheren Teil steht. Die Leserin kennt nur Schulmathematik plus die früheren Teile.
- **Umfang: höchstens 25 Seiten PDF, 7 bis 10 Stufen, 8 bis 12 Abbildungen, 8 bis 12 Aufgaben.** Eine Stufe kostet rund 2 bis 3 Seiten. Knapp heißt: nichts Wichtiges weglassen, aber nichts doppeln, keine Tabellen oder Abschnitte zu Dingen, die später nicht gebraucht werden. Reicht der Platz nicht, zusammenfassen statt Stufen anhängen.
- Aufbau: `\section*{Worum es geht}` (direkt danach `\markboth{...}{...}` auf eigener Zeile, sonst steht das Inhaltsverzeichnis im Kopf) mit kernbox „Die Antwort in drei Sätzen (am Ende des Hefts sollen sie selbstverständlich sein)“, dann `\paragraph{Ein Prinzip hinter allen Ergebnissen.}` mit Tabelle „Ergebnis | Woher es kommt“, dann `\paragraph{So arbeitest du mit dem Heft.}` (wird beim Umwandeln ersetzt, kurz halten), dann merkbox mit dem Rechenmodell, bei Bedarf `\section*{Von Grund auf: ...}` (nur Grundbegriffe, die später gebraucht werden, höchstens eine Seite), dann `\section{Stufe 1: ...}` usw., am Ende kernbox `Das Wichtigste`, zuletzt `\section{Lösungen}`.
- Jede Stufe löst genau ein neues Problem und beginnt mit `zweck`. Dann `\paragraph{Die Idee.}` (anschaulich, Mechanismus in Worten), dann Satz oder Definition, `\textbf{So liest man das:}` (jedes Symbol mit Bedeutung, Einheit, typischer Größe), Gültigkeitsbedingung, Herleitung in `herleitung`, ein Beispiel mit dem Rechenmodell, mindestens eine Grenzfall-Kontrolle, typische Fragen in `qa`, Aufgaben in `aufgabe`.
- Immer das Warum und der konkrete Mechanismus: welches Teilchen, welcher Knoten, welcher Strompfad erzeugt die Wirkung. Jede Vernachlässigung mit Zahl begründen. Jeden Fachbegriff bei der ersten Nennung sofort erklären und mit `\fb{...}` markieren. Analogien nur in `analogie`, mit dem Satz, wo sie nicht mehr stimmen. Stoff über die Quelle hinaus in `vertiefung`.
- Begriffe im Eingangsteil (kernbox, merkbox) bekommen eine Kurzerklärung im selben Satz, die ausführliche folgt in der Stufe. Die ersten acht `\fb{...}` des Hefts werden die Schlagwörter der Website: Dort die Grundform setzen („Ladung“, nicht „Ladungen“).
- Tabellen nur als `center` mit `tabular` oder `tabularx` und booktabs, ohne `table`, ohne Tabellennummer und ohne `\ref` darauf.
- Aufgaben: gemischt: rechnen, vorhersagen, Grenzfall, mit Schwierigkeit \stern bis \stern\stern\stern. Jede Aufgabe mit `\label{a:...}` und Lösung `\loesung{a:...}` in kap<N>_loesungen.tex, vollständig mit Zahlen. Theorie wird immer mit Rechnen verbunden, durch Aufgaben lernt man am meisten.
- 1 bis 3 LTspice-Boxen (Umgebung `ltspice`, wie in kap8_stufen.tex): Zeichnen, Direktiven, Was du siehst, plus ein Bezug zu einer Aufgabe. Jede Box mit LTspice prüfen: Netzliste schreiben, `"C:\Users\info\AppData\Local\Programs\ADI\LTspice\LTspice.exe" -b datei.net` im Scratchpad ausführen, die .log auswerten, Zahlen vergleichen. Die .log enthält bei `.op` nur `.meas`-Ergebnisse, also immer `.meas op`; `V(0)` geht dort nicht.
- Ton sachlich und klar, kurze Sätze, keine Füllwörter (einfach, offensichtlich, natürlich), keine Emojis, kein Bezug auf „wir im Kurs“. Aufgaben sprechen die Leserin mit du an.
- Präzision: Gleichgrößen groß, zeitabhängige klein. Vorzeichen und Zählpfeile ausdrücklich. Dezimalkomma `0{,}7`. Makros aus der Präambel: \dd \ee \jj \un{kHz} \fb. Keine eigenen \newcommand in den Stufen-Dateien.

## Abbildungen
- Jede Stufe hat mindestens eine Abbildung. Schaltungen und Kurven werden nur mit dem Editor gezeichnet, nicht mit TikZ oder circuitikz.
- Im Heft steht:
  \begin{abb}\szene{k<N>name}\caption{...}\label{fig:k<N>name}\end{abb}
- Die Szene baust du in tools/szenen/et1_teil<N>.py im Repo C:\Users\info\PycharmProjects\pythonanimation. Lies dazu notizen/szenen_auftrag_et3.md (Regeln 2 bis 7 gelten, Szenenname et1/k<N>name), tools/szenen_lib.py und als Beispiel tools/szenen/et1_teil1.py. Schaltungen: s.bauteil, s.draht, s.pfeil, s.geraet (ground, terminal, node, npn, opamp); Editor-Katalog in web/editor.js ab `Elektrotechnik · Schaltplan`. Wörter in den Bildern in vier Sprachen über s.tr. Mischt eine Szene Achsen und freie Zeichnung: s.welt() als erstes Objekt.
- Danach: python tools/szenen_ansehen.py <out.png> et1/... ; Bild ansehen; dann python tools/export_szenen.py et1/name1 et1/name2 ... (immer mit Namen, ohne Namen schreibt es alle Module neu); dann python tools/szenen_pdf.py et1 "C:/Bücher/ET1/Arbeitshefte" <namen>.

## Bauen und prüfen
- pdflatex Kap<N>_<Name>.tex dreimal im Ordner, fehlerfrei; danach .aux .log .out .toc löschen. PDF mit Read ansehen und prüfen.
- python tools/heft_zu_artikel.py et1 --kap <N> --lang de --pruefen --katex muss ohne Warnung durchlaufen (unbekannte Befehle, Verweise ohne Ziel, Aufgaben ohne Lösung, Formeln, die KaTeX nicht setzen kann).
- LaTeX und Python-Skripte nur mit Write oder Edit schreiben. Im Bash-Tool werden doppelte Backslashes halbiert und Heredocs mit dreifachen Anführungszeichen brechen ab.

## Grenzen
Nur eigene Dateien anlegen: die Heftdateien des eigenen Teils, tools/szenen/et1_teil<N>.py, web/szenen/et1/*, web/abbildungen/**. Nichts an Engine, Editor, build_wissen.py, heft_zu_artikel.py, den Präambeln oder content/ ändern, nichts committen. Andere Agenten schreiben parallel die anderen Teile. Auf frühere Teile darfst du mit „Teil N“ verweisen, die Gliederung steht unten.

## Gliederung der Reihe
1 Ladung, Feld und Potenzial · 2 Strom, Widerstand und Kirchhoff · 3 Der Kondensator · 4 Strom und Spannung messen · 5 Quellen und Ersatzquellen · 6 Zweitore · 7 Leistung, Anpassung und Wirkungsgrad · 8 Maschenstrom- und Knotenpotentialverfahren · 9 Halbleiter und Dioden · 10 Der Bipolartransistor · 11 Der Operationsverstärker

## Bericht am Ende (knapp)
Seitenzahl, Stufen, Aufgaben, Abbildungen, LTspice-Boxen mit Mess- gegen Rechenwert, bewusst gekürzte Inhalte, Fehler der Quelle, offene Punkte.
