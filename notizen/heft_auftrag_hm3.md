# Auftrag: Arbeitsheft für Höhere Mathematik 3 (hm3)

Lies zuerst notizen/heft_auftrag_hm1.md. Er gilt vollständig (Form, Stil, Sätze und Beweise, Abbildungen, Bauen, Grenzen), mit diesen Änderungen. Vorlage in Form und Stil ist C:\Bücher\HöMa3\Arbeitshefte\kap5_stufen.tex.

## Quellen
- Skript: Text mit Marken `=== Seite N` (PDF-Seiten) in C:\Bücher\EtUndSo\_volltext\hm3_skript.txt, PDF C:\Bücher\HöMa3\HM3_Skript_24_25.pdf (Read mit pages, höchstens 20 Seiten je Aufruf). PDF-Seite = Skriptseite + 2. Formeln fehlen im Text oft, also im PDF lesen.
- Freigegebene, ausführliche Zusammenfassungen mit allen Beweisschritten: C:\Bücher\HöMa3\Zusammenfassungen\HM3_Kap<N>_*.md. Zuerst lesen.
- Übungen als Maßstab für Niveau und Aufgabentypen: Zip C:\Bücher\EtUndSo\3.Semester\(VO) Höhere Mathematik 3_20261019_1451.zip. In einen eigenen Unterordner des Scratchpads entpacken. Jeder Aufgabentyp zum Thema wird geübt, immer mit eigener Aufgabe und eigenen Zahlen.
- Vollständigkeit: Jede Definition, jeder Satz, jede Formel und jeder Beweis des Kapitels kommt vor. Lange Texte darfst du zusammenfassen.
- Im Heft steht nirgends ein Bezug zu Skript, Vorlesung, Übung, Uni, Klausur oder Personen der Quelle, auch keine Satznummern. Fehler der Quelle korrigierst du still und nennst sie im Bericht.

## Dateien
C:\Bücher\HöMa3\Arbeitshefte (Präambeln liegen dort): Kap<N>_<Name>.tex, kap<N>_stufen.tex, kap<N>_loesungen.tex, rechnung_kap<N>.py. Titelzeile „Arbeitsheft HöMa3 – Höhere Mathematik 3, Kapitel~N“ (seit 09.11.2026; Verweise „Kapitel~N, Abschnitt~M“, siehe notizen/kapitel_umstellung.md). Szenen in tools/szenen/hm3_teil<N>.py, Szenenname hm3/k<N>name, Beispiel tools/szenen/hm3_teil5.py. python tools/szenen_pdf.py hm3 "C:/Bücher/HöMa3/Arbeitshefte" <namen>. Prüfung: python tools/heft_zu_artikel.py hm3 --kap <N> --lang de --pruefen --katex. Hilfsskripte in einen Unterordner hm3k<N> des Scratchpads, weil parallele Agenten es teilen.

## Zwei Regeln, die alles andere schlagen
1. **Keine Vorgriffe.** Ein Abschnitt benutzt nur, was vorher eingeführt wurde, im selben Heft oder in einem früheren Teil. Kein „wie wir später sehen“, kein Klammerhinweis auf spätere Stufen, kein Begriff, keine Eigenschaft und kein Ergebnis aus einer späteren Stufe, auch nicht als Nebenbemerkung. Ein Hinweis auf Kommendes ist nur erlaubt als letzter Satz einer Stufe, in Worten, die der Leser schon kennt. Rückverweise sind gut. Jeder Satz muss auch dann verständlich sein, wenn der Leser genau bis zu diesem Satz gelesen hat.
2. **Jede Stufe ist ein eigener kurzer Artikel.** Auf der Website wird jede Stufe zu einer Seite, die man abschließt: ein Problem, eine Lösung, Aufgaben dazu. Höchstens 10 000 Zeichen Quelltext je Stufe, Lösungen nicht mitgezählt.

## Aufbau
`\section*{Worum es geht}` nur mit der Frage des Hefts und ihrem Nutzen, in Alltagsworten, ohne Ergebnisse. Am Ende in dieser Reihenfolge: kernbox `Das Wichtigste`, danach kernbox `Die Antwort in drei Sätzen`, danach `\paragraph{Ein Prinzip hinter allen Ergebnissen.}` mit Tabelle, zuletzt `\section{Lösungen}`. Umfang höchstens 22 Seiten PDF, 4 bis 8 Stufen, 8 bis 12 Aufgaben, 4 bis 8 Abbildungen.

## Bezeichnungen
Wie in Teil 5: \vx \vF \vE \vA \ver_r \rot \divg \R, Skalarpotential \varphi, Parametrisierungen \gamma und \Phi bzw. \vx(u,v). Präambel lesen. Jedes Symbol hat eine Bedeutung. Differentiale in richtiger Ordnung.

## Gliederung der Reihe
1 Differentialrechnung für Vektorfelder · 2 Integralrechnung im Rⁿ · 3 Kurvenintegrale · 4 Koordinatentransformationen · 5 Integralsätze im Raum (fertig) · 6 Konvergenz von Funktionenfolgen · 7 Fourier-Reihen · 8 Wahrscheinlichkeitsrechnung

## Bericht am Ende (knapp)
Seitenzahl, Stufen, Aufgaben, Abbildungen, bewusst gekürzte Inhalte, Fehler der Quelle, offene Punkte, neue Begriffe in einer Zeile.
