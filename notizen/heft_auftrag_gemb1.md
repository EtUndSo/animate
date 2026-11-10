# Auftrag: Arbeitsheft für Elektronische Materialien und Bauelemente 1 (gemb1)

Ziel: Ein Arbeitsheft als LaTeX-Quelle, aus dem automatisch Website-Artikel werden (Studierende der Elektrotechnik, Erklärplattform EtUndSo). Vorlage in Form und Stil sind die fertigen Hefte in C:\Bücher\ET1\Arbeitshefte (besonders kap9_stufen.tex, kap9_loesungen.tex, Kap9_Dioden.tex) und C:\Bücher\HöMa3\Arbeitshefte\kap5_stufen.tex. Lies diese zuerst, dann C:\Bücher\EtUndSo\VORGABE_ARTIKEL.md (Abschnitte 1 bis 3; das Format dort ersetzt die Heftform nicht).

## Quellen und Gewichtung
Reihenplan: C:\Bücher\GEMB\Arbeitshefte\LEITFADEN.md. Dort stehen zu deinem Teil Folien, Skriptseiten, Zusammenfassung und Übungen.

Zwei Quellen, zwei Aufgaben:
- **Skript = Vollständigkeit.** Alles aus den genannten Skriptseiten muss ins Heft: jede Definition, jede Formel, jede Aussage. Lange Texte darfst du zusammenfassen, nichts weglassen. Text mit Marken `=== Seite N` (PDF-Seiten): C:\Bücher\EtUndSo\_volltext\gemb1_skript.txt. Formeln fehlen dort oft, also die Seiten im PDF lesen: C:\Bücher\GEMB\Quelle\Skript GEMB 1.pdf (Read mit pages, höchstens 20 Seiten je Aufruf). Skriptseite = PDF-Seite − 8.
- **Folien = Schwerpunkt.** Was in den Folien steht, ist Kernstoff: ausführlich, mit Herleitung, Aufgaben und Abbildung, auch wenn es im Skript fehlt (Tight-Binding, diskrete Schrödinger-Gleichung, Boltzmann-Transportgleichung, Graphen). Was nur im Skript steht, kommt knapper: in einer `vertiefung`-Box oder in einer eigenen Stufe mit dem Titel „Stufe N: Ergänzung: …“. Vollständige, freigegebene Zusammenfassung der Folien: C:\Bücher\GEMB\Zusammenfassungen\GEMB_Kap*.md (zuerst lesen, sie enthält alle Formeln). Folientext mit Marken `=== V<n> Folie <p>`: C:\Bücher\EtUndSo\_volltext\gemb1_folien.txt. PDFs: C:\Bücher\GEMB\(VO) Grundlagen elektronischer Materialien und Bauelemente 1_20260831_1820\Vorlesungsfolien\Vorlesung <n>.pdf.
- **Bezeichnungen:** Skript und Folien nennen dasselbe oft verschieden. In der ganzen Reihe gilt: Energie E mit E_\mathrm{F}, E_\mathrm{C}, E_\mathrm{V}, E_\mathrm{g} (nicht W), elektrische Feldstärke \mathcal{E}, Wellenvektor k, Elementarladung e > 0, Ortsraum x, Boltzmann-Konstante k_\mathrm{B}. Jedes Symbol hat genau eine Bedeutung. Festgelegt durch Teil 1 und 2: freie Elektronenmasse m_0, effektive Masse m^*, Richtungsmassen m_x, m_y, m_z, Hamilton-Operator \hat H, Ortsvektor \boldsymbol r, Hüpfparameter t_0 (nicht t, das ist die Zeit), Gitterindex \ell (nicht j), Quantenzahlen n_x, n_y, n_z. Aus Teil 3: Eindringtiefe \delta, Abklingkonstante \kappa, Barrierenbreite L. Aus Teil 6: Zellinhalt \Omega, ganzzahlige Faktoren \ell_i, Basisvektoren d_j, Zellkanten e_i, Avogadro-Konstante N_\mathrm{Av}, Massendichte \rho_m, Kugelradius r_\mathrm{at}. Aus Teil 7: reziproke Vektoren G (nicht k), Koeffizienten h_1, h_2, h_3, Rechteckkanten a_x, a_y. Eigene Hilfsskripte gehören in einen Unterordner k<N>teil des Scratchpads, weil parallele Agenten es teilen. Bereits eingeführt in Teil 2: Brillouin-Zone (nur die Grundidee), effektive Masse aus dem Kosinus-Band, Spin und Pauli-Prinzip (kurz), Zustandsdichte durch Zählen.
- **Formelsammlungen:** C:\Bücher\GEMB\(VO) Grundlagen elektronischer Materialien und Bauelemente 1_20260831_1820\Weitere Unterlagen\Formelsammlung GEMB1 - Stand 26.08.pdf. Jede Formel daraus, die zu deinem Teil gehört, muss vorkommen.
- **Aufgaben der Quelle** als Maßstab für Niveau und Aufgabentypen: Ordner Frontalübungen, Kleingruppenübungen, Selbstrechenübungen im selben Kursordner, dazu C:\Bücher\GEMB\Quelle\Aufgabensammlung GEMB1.pdf (Text: _volltext\gemb1_aufgaben.txt). Jeder Aufgabentyp zu deinem Thema muss im Heft geübt werden, immer mit eigener Aufgabe und eigenen Zahlen. Keine Aufgabe, kein Zahlenbeispiel und keine Abbildung wörtlich übernehmen. Standardwissen ist frei.
- Das Niveau nicht überschreiten: erst der einfache, erwartete Lösungsweg.
- Im Heft steht nirgends ein Bezug zu Skript, Folien, Vorlesung, Übung, Uni, Klausur, Dozent oder Personen der Quelle, auch keine Seiten-, Bild- oder Gleichungsnummer. Fehler der Quelle korrigierst du still und nennst sie im Bericht.

## Dateien in C:\Bücher\GEMB\Arbeitshefte (Präambeln liegen dort)
- Kap<N>_<Name>.tex (Hauptdatei, Aufbau wie C:\Bücher\HöMa3\Arbeitshefte\Kap5_Integralsaetze.tex; Titelblock mit \LARGE und \large, Untertitel als Frage oder Kernaussage; „Arbeitsheft GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1, Kapitel~N“ (seit 09.11.2026; Verweise „Kapitel~N, Abschnitt~M“, siehe notizen/kapitel_umstellung.md); Ergänzungshefte (ab Kapitel 19) tragen den \LARGE-Titel „<Titel> (Ergänzung)“, im Baum „Kapitel N: <Titel> (Ergänzung)“, nicht „Ergänzung: <Titel>“ (Entscheidung 09.11.2026))
- kap<N>_stufen.tex, kap<N>_loesungen.tex
- rechnung_kap<N>.py: rechnet jede Zahl des Hefts nach. Keine Zahl ohne Rechnung. Erste Zeilen: `import sys; sys.stdout.reconfigure(encoding="utf-8")`.
Der Name Kap<N>_<Name> steht im Einzelauftrag und muss exakt stimmen.

## Zwei Regeln, die alles andere schlagen
1. **Keine Vorgriffe.** Ein Abschnitt benutzt nur, was vorher eingeführt wurde, im selben Heft oder in einem früheren Teil. Kein „wie wir später sehen“, kein Klammerhinweis auf spätere Stufen, kein Begriff, keine Eigenschaft und kein Ergebnis aus einer späteren Stufe, auch nicht als Nebenbemerkung. Der Leser kann mit so einem Satz nichts anfangen und fühlt sich abgehängt. Ein Hinweis auf Kommendes ist nur erlaubt als letzter Satz einer Stufe, in Worten, die der Leser schon kennt, ohne neuen Begriff. Rückverweise sind gut. Jeder Satz muss also auch dann verständlich sein, wenn der Leser genau bis zu diesem Satz gelesen hat.
2. **Jede Stufe ist ein eigener kurzer Artikel.** Auf der Website wird jede Stufe zu einer Seite, die man abschließt. Sie muss für sich rund sein: ein Problem, eine Lösung, Aufgaben dazu. Höchstens 10 000 Zeichen Quelltext je Stufe, Lösungen nicht mitgezählt.

## Inhalt und Stil
- Rangfolge: physikalisch korrekt, verständlich ohne Vorwissen, vollständig gegenüber der Quelle, knapp. Die Leserin kennt Schulmathematik, Grundlagen der Elektrotechnik, Differentialgleichungen, komplexe Zahlen, plus die früheren Teile.
- **Umfang: höchstens 20 Seiten PDF, 4 bis 8 Stufen, 4 bis 8 Abbildungen, 8 bis 12 Aufgaben.** Reicht der Platz nicht, zusammenfassen statt Stufen anhängen. Bei wenig Quellstoff ist das Heft eben kürzer.
- Aufbau: `\section*{Worum es geht}` (direkt danach `\markboth{...}{...}` auf eigener Zeile) nur mit der Frage des Hefts und ihrem Nutzen, in Alltagsworten, ohne Ergebnisse. Dann `\paragraph{So arbeitest du mit dem Heft.}` (wird beim Umwandeln ersetzt, kurz halten), bei Bedarf merkbox mit dem Rechenmodell, bei Bedarf `\section*{Von Grund auf: ...}` (nur Grundbegriffe, die gebraucht werden, höchstens eine Seite), dann `\section{Stufe 1: ...}` usw. Am Ende in dieser Reihenfolge: kernbox `Das Wichtigste`, danach kernbox `Die Antwort in drei Sätzen`, danach `\paragraph{Ein Prinzip hinter allen Ergebnissen.}` mit Tabelle „Ergebnis | Woher es kommt“, zuletzt `\section{Lösungen}`. Diese Zusammenschau steht bewusst am Ende, denn am Anfang kennt man ihre Begriffe noch nicht.
- Jede Stufe löst genau ein neues Problem und beginnt mit `zweck`. Dann `\paragraph{Die Idee.}` (anschaulich, Mechanismus in Worten), dann Satz oder Definition, `\textbf{So liest man das:}` (jedes Symbol mit Bedeutung, Einheit, typischer Größe), Gültigkeitsbedingung, Herleitung in `herleitung`, ein Beispiel, mindestens eine Grenzfall-Kontrolle, typische Fragen in `qa`, Aufgaben in `aufgabe`.
- Immer das Warum und der konkrete Mechanismus: welches Teilchen, welches Feld, welche Randbedingung erzeugt die Wirkung. Jede Vernachlässigung mit Zahl begründen. Jeden Fachbegriff bei der ersten Nennung sofort erklären und mit `\fb{...}` markieren. Analogien nur in `analogie`, mit dem Satz, wo sie nicht mehr stimmen. Stoff über die Quelle hinaus in `vertiefung`.
- Die ersten acht `\fb{...}` des Hefts werden die Schlagwörter der Website: Dort die Grundform setzen („Wellenfunktion“, nicht „Wellenfunktionen“).
- Tabellen nur als `center` mit `tabular` oder `tabularx` und booktabs, ohne `table`, ohne Tabellennummer und ohne `\ref` darauf.
- Aufgaben: gemischt: rechnen, vorhersagen, Grenzfall, mit Schwierigkeit \stern bis \stern\stern\stern. Jede Aufgabe mit `\label{a:...}` und Lösung `\loesung{a:...}` in kap<N>_loesungen.tex, vollständig mit Zahlen. Durch Aufgaben lernt man am meisten.
- Keine LTspice-Boxen, außer ab Teil 14 bei echten Bauelementen (höchstens eine, wie in C:\Bücher\ET1\Arbeitshefte\kap9_stufen.tex, mit LTspice geprüft).
- Ton sachlich und klar, kurze Sätze, keine Füllwörter (einfach, offensichtlich, natürlich), keine Emojis, kein Bezug auf „wir im Kurs“. Aufgaben sprechen die Leserin mit du an.
- Präzision: Vorzeichen ausdrücklich, Differentiale in richtiger Ordnung, Dezimalkomma `0{,}7`. Makros aus der Präambel: \dd \ee \jj \un{kHz} \eps \fb und die Vektormakros (Präambel lesen). Keine eigenen \newcommand in den Stufen-Dateien.

## Abbildungen
- Jede Stufe hat mindestens eine Abbildung. Kurven und Skizzen werden nur mit dem Editor gezeichnet, nicht mit TikZ.
- Im Heft steht:
  \begin{abb}\szene{k<N>name}\caption{...}\label{fig:k<N>name}\end{abb}
- Die Szene baust du in tools/szenen/gemb1_teil<N>.py im Repo C:\Users\info\PycharmProjects\pythonanimation. Lies dazu notizen/szenen_auftrag_et3.md (Regeln 2 bis 7 gelten, Szenenname gemb1/k<N>name), tools/szenen_lib.py und als Beispiel tools/szenen/hm3_teil5.py sowie tools/szenen/et1_teil9.py. Wörter in den Bildern in vier Sprachen über s.tr. Mischt eine Szene Achsen und freie Zeichnung: s.welt() als erstes Objekt.
- Danach: python tools/szenen_ansehen.py <out.png> gemb1/... ; Bild ansehen; dann python tools/export_szenen.py gemb1/name1 gemb1/name2 ... (immer mit Namen, ohne Namen schreibt es alle Module neu); dann python tools/szenen_pdf.py gemb1 "C:/Bücher/GEMB/Arbeitshefte" <namen>.

## Bauen und prüfen
- pdflatex Kap<N>_<Name>.tex dreimal im Ordner, fehlerfrei; danach .aux .log .out .toc löschen. PDF mit Read ansehen und prüfen.
- python tools/heft_zu_artikel.py gemb1 --kap <N> --lang de --pruefen --katex muss ohne Warnung durchlaufen (unbekannte Befehle, Verweise ohne Ziel, Aufgaben ohne Lösung, Formeln, die KaTeX nicht setzen kann).
- Lies das Heft zum Schluss einmal als neue Leserin, Satz für Satz, und streiche oder erkläre jeden Vorgriff.
- LaTeX und Python-Skripte nur mit Write oder Edit schreiben. Im Bash-Tool werden doppelte Backslashes halbiert und Heredocs mit dreifachen Anführungszeichen brechen ab.

## Grenzen
Nur eigene Dateien anlegen: die Heftdateien des eigenen Teils, tools/szenen/gemb1_teil<N>.py, web/szenen/gemb1/*, web/abbildungen/**. Nichts an Engine, Editor, build_wissen.py, heft_zu_artikel.py, den Präambeln oder content/ von Hand ändern, nichts committen. Andere Agenten schreiben parallel die anderen Teile. Auf frühere Teile darfst du mit „Teil N“ verweisen; dass ein früherer Teil gerade erst entsteht, ist kein Problem, die Gliederung steht im Leitfaden. Auf spätere Teile verweist du nie.

## Bericht am Ende (knapp)
Seitenzahl, Stufen, Aufgaben, Abbildungen, bewusst gekürzte Inhalte, Fehler der Quelle, offene Punkte. Liste außerdem die Begriffe, die dieses Heft neu einführt, in einer Zeile.
