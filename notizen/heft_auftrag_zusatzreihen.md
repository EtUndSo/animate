# Auftrag: ein Heft der Zusatzreihen Cybersecurity (cyber) und Machine Learning (ml) neu schreiben

Du schreibst **ein** deutsches Arbeitsheft von Grund auf neu; Reihe und Teil nennt dir die Nachricht. Es gibt kein Skript: Der **Lernpfad** der Recherche gibt Reihenfolge und Gliederung vor, die **WISSEN-Datei** des Hefts ist die Inhaltsgrundlage. Muster für Aufbau und Qualität sind die zwei abgenommenen Pilothefte (User: „so ist es um Welten besser … Genau so weiter“). Qualität geht vor allem, die Zeit spielt keine Rolle.

Dieser Auftrag ersetzt für die Zusatzreihen `ueberarbeitung_auftrag.md`. `UEBERARBEITUNG.md` gilt vollständig; wo dort „Skript“ steht, lies „Lernpfad-Eintrag und WISSEN-Datei des Hefts“.

## Zuerst lesen (Pflicht, jede Datei vollständig)
Der User hat ausdrücklich verlangt, dass alles ganz gelesen wird: „Nein, der Agent soll alles lesen!“ und „Ein Abschnitt aus einem ganzen Buch zu lesen ist wie ein Wassertropfen aus einem See, das macht keinen Sinn“.
- Lies jede Datei dieser Liste **von der ersten bis zur letzten Zeile**. Große Dateien liest du in aufeinanderfolgenden Teilen (offset/limit), bis das Ende erreicht ist. Meldet Read eine Teilansicht („PARTIAL view“), liest du weiter, bis alles gelesen ist.
- Gespart wird nur beim PDF (siehe „Bauen und prüfen“).

1. `C:\Users\info\PycharmProjects\pythonanimation\notizen\UEBERARBEITUNG.md`: der maßgebliche Leitfaden, besonders §2 (ein Begriff nach dem anderen, Theorie vor Praxis), §3 und §3a (Hintergrund-Kästen mit recherchiertem Warum) und §4 (keine Vorgriffe).
2. Die beiden Muster, **alle Dateien ganz**:
   - ET3 Teil 2: `C:\Bücher\ET3\Arbeitshefte\Kap2_Laplace.tex`, `kap2_stufen.tex`, `kap2_stufen_b.tex`, `kap2_loesungen.tex`.
   - HöMa3 Teil 1: `C:\Bücher\HöMa3\Arbeitshefte\Kap1_Vektorfelder.tex`, `kap1_stufen.tex`, `kap1_loesungen.tex`.
3. Die Präambel deiner Reihe (`praeambel.tex` im Heftordner, siehe unten): Kästen, Code-Umgebungen, Makros. Benutze nur, was dort steht.
4. Aus `C:\Bücher\EtUndSo\<Reihe>\Recherche\`, jeweils ganz:
   - `LERNPFAD.md`: darin **der Eintrag deines Hefts** (Lernziele, Begriffe in Einführungsreihenfolge, Voraussetzungen, Hauptquellen, Warum-Ideen, Aufgaben, Abbildungen); bei ML die „Notationsentscheidungen“.
   - `WISSEN_T<NN>_*.md` deines Hefts. Das ist die Inhaltsgrundlage.
   - `AUFGABEN.md` (Lösungsideen sind für dich, nicht wörtlich fürs Heft).
   - `ZUSAMMENFASSUNG.md`: die Entscheidungen des Users.
   - `QUELLEN.md`.
   - die Dateien in `Notizen\`, die dein Heft betreffen (Belegstellen, Prüfprotokolle, Hauptquellen-Exzerpte deiner Teile).
5. Die fertigen früheren Hefte der Reihe im Heftordner, alle Dateien ganz: Ihre Begriffe, Bezeichnungen und Beispiele übernimmst du.

| Reihe | Heftordner | Recherche | Szenen |
|---|---|---|---|
| cyber | `C:\Bücher\EtUndSo\Cybersecurity\Arbeitshefte` | `C:\Bücher\EtUndSo\Cybersecurity\Recherche` | `tools/szenen/cyber_teil<N>.py`, Namen `cyber/k<N>name` |
| ml | `C:\Bücher\EtUndSo\MachineLearning\Arbeitshefte` | `C:\Bücher\EtUndSo\MachineLearning\Recherche` | `tools/szenen/ml_teil<N>.py`, Namen `ml/k<N>name` |

Teil N ist Stamm-Heft T<NN> des Lernpfads (Teil 1 = T01). Der Dateiname `Kap<N>_<Name>` steht in `tools/heft_zu_artikel.py` unter `MODULE["cyber"]` bzw. `MODULE["ml"]` und muss exakt stimmen.

## Quellen und Recherche
- **Inhalt:** Was die WISSEN-Datei an Definitionen, Mechanismen, Formeln, Befehlen, typischen Fehlern und Beispielen enthält, kommt ins Heft, soweit es zum Lernziel gehört. Lange Passagen darfst du zusammenfassen; nichts Wichtiges weglassen. Stellen, die die WISSEN-Datei als unsicher markiert („[TOC]“, „noch prüfen“), prüfst du vor dem Schreiben nach.
- **Hauptquellen sind Lehrbücher und Kurse renommierter Universitäten.** Standards, Gesetze und Dokumentationen ergänzen, Plattformen dienen nur als Übungen, Blogs und Videos nur der Anschauung.
- **Warum-Kästen (Pflicht, §3a):** Für jeden Abschnitt und jedes zentrale Verfahren recherchierst du zusätzlich, *warum* es so funktioniert und *wozu* man es so macht. Die Warum-Ideen im Lernpfad sind der Startpunkt, nicht das Ende. Bevorzugt aus Uni-Quellen; in eigenen Worten, exakt, Analogien als Bild gekennzeichnet.
- **Recherche-Unteragenten** sind erlaubt: höchstens **3 gleichzeitig**, immer mit `model: "sonnet"`. Sie suchen und exzerpieren nur (Fundstelle, Kernaussage, Zitat zur Prüfung). Geschrieben wird ausschließlich von dir.
- Fehler der Quellen korrigierst du still und nennst sie im Bericht. Nichts wird kopiert: eigene Formulierungen, eigene Beispiele, eigene Zahlen, eigene Abbildungen.

## Aufbau des Hefts
- **Gliederung:** Die Begriffsliste des Lernpfad-Eintrags gibt die Reihenfolge vor. Fasse sie zu thematischen `\section` zusammen (je etwa drei bis acht Begriffe, ein Abschnitt = ein abgeschlossenes Thema, auf der Website ein Artikel). Jeder Begriff bekommt ein eigenes `\subsection` mit Wozu, Anschauung, Definition, einfachstem Beispiel und „Kurz gesagt“ (§2). Weicht die WISSEN-Datei in der Reihenfolge ab, gilt der Lernpfad; ist eine Umstellung didaktisch nötig, begründe sie im Bericht.
- **Anfang:** `\section*{Worum es geht}` (mit `\addcontentsline`) nennt nur die Frage des Hefts und ihren Nutzen in Alltagsworten, keine Ergebnisse und keine Begriffe, die erst später kommen. Danach `\paragraph{So arbeitest du mit dem Heft.}` mit den Kastenarten, die das Heft wirklich benutzt (Hintergrund, Herleitung/Beweis, Achtung) und dem Hinweis auf Aufgaben und Lösungen; auf der Website wird er durch einen festen Text ersetzt.
- **Was der Leser mitbringt:** ET-Studierende etwa im 5. Semester (Mathematik bis HöMa 3, Signale und Systeme, etwas Programmierung), ohne Vorwissen in deiner Reihe. Er kennt nur die früheren Teile der Reihe. Was er darüber hinaus braucht, steht als „Was du dafür brauchst: …“ zu Beginn des Abschnitts (§2).
- **Verweise:** Frühere Hefte heißen „Teil N“ (auf der Website ein Link). Rückverweise sind erwünscht. Keine Vorgriffe auf spätere Teile, auch nicht im Hintergrund-Kasten (§4).
- **Ende:** kernbox „Das Wichtigste bis hier“, kernbox „Die Antwort in drei Sätzen“, Prinzip-Tabelle mit Abschnittsverweisen (ML ab Teil 9: „Modell + Verlust + Optimierung + Prüfung“), dann `\section{Lösungen}` aus `kap<N>_loesungen.tex`.
- **Keine Quellenverweise im Heft:** keine Buch-, Kurs-, Uni- oder Kapitelangaben, kein „nach X“, kein Literaturverzeichnis. Gesetze, Standards, Organisationen (StGB, RFC, NIST, BSI, CVE) und die Namen von Prinzipien (Kerckhoffs, Saltzer und Schroeder) dürfen als Inhalt vorkommen. Links auf Übungsplattformen (pwn.college, OverTheWire, PortSwigger Web Security Academy, CryptoHack usw.) sind als Übungsumgebungen erlaubt.
- **Ton:** seriös und professionell, aber nicht steif; der Ton der Musterhefte trifft es. Aufgaben sprechen den Leser mit du an.

## Praxis: Aufgaben, Code, Labor
- **Jeder Abschnitt** endet mit mindestens einer Aufgabe; die Aufgaben benutzen nur, was bis dahin erklärt ist. Gemischt: verstehen, rechnen, vorhersagen, praktisch ausführen; Schwierigkeit \stern\ bis \stern\stern\stern. Jede Aufgabe mit `\label{a:...}` und ausführlicher Lösung `\loesung{a:...}` in `kap<N>_loesungen.tex`: der Weg, das Ergebnis und warum es so ist.
- **Cybersecurity:** Praxis heißt Konsole und Labor, aber erst ab dem Heft, das das Werkzeug einführt (Konsole ab Teil 3; vorher Browser, Papier, Windows-Bordmittel, soweit erklärt).
  - Grundregel in jedem Heft mit praktischen Übungen als Kasten `warnung`: nur eigene Systeme, erlaubte Lernplattformen innerhalb ihrer Regeln oder isolierte Labore. Der Rechtsstand muss exakt und aktuell sein; das Heft ist keine Rechtsberatung und sagt das.
  - Riskante Schritte (Datenträger beschreiben, Bootreihenfolge, Secure Boot, BitLocker) stehen mit ihrem Risiko und der Absicherung in einem `warnung`-Kasten, bevor der Schritt kommt.
  - Lösungen von Plattform-Aufgaben werden nie abgedruckt (pwn.college und OverTheWire verbieten es): Dort nur gestufte Hinweise. Vollständige Lösungen gibt es für die eigenen Aufgaben des Hefts.
- **Machine Learning:** Programmieren in Python ab Teil 7 (dort Einrichtung), C++ nur in den Heften, die der Lernpfad markiert. Teil 1 bis 6 rechnen von Hand und mit Zahlenbeispielen; kein Werkzeug vor seinem Begriff. Notation strikt nach den Notationsentscheidungen im Lernpfad.
- **Code-Listings** (Präambel): `konsole` (Sitzung: Eingabe mit `$ `, `# ` oder `>>> ` am Zeilenanfang, sonst Ausgabe), `bash`, `python`, `ccode`, `cppcode`, `asm` (Intel), `gas` (AT&T), `ausgabe` (reiner Text). Optionaler Titel: `\begin{python}[hallo.py]`. Code ab Spalte 0, ohne Tabulatoren; Zeichen außerhalb von ASCII nur in Kommentaren und Zeichenketten. Im Fließtext `\texttt{...}` (Sonderzeichen escapen) oder `\verb|...|` (nicht in Überschriften, Kastentiteln und Argumenten).
- **Übungsumgebung der Leser:** Die Leser richten sich ihre Umgebung selbst ein, nach den Anleitungen in den Heften (Live-USB-Stick oder VM ab Teil 3, isoliertes Labor in späteren Teilen; Python-Umgebung in ML Teil 7). Die Website stellt nie selbst eine Umgebung bereit: keine Online-Terminals, keine eingebetteten Sandboxes, kein ausführbarer Code auf der Seite (Entscheidung des Users vom 04.11.2026, wegen der Sicherheitsrisiken). Externe Übungsplattformen dürfen verlinkt werden.
- **Alles Ausführbare wird getestet**, bevor es ins Heft kommt. Diese Testumgebung gibt es nur auf dem Rechner des Users, für dich:
  - **Linux:** Ubuntu 26.04 LTS unter WSL 2, Benutzer `student` mit sudo ohne Passwort, systemd läuft; installiert sind u. a. gcc 15, gdb, Python 3.14, nmap, nc, tcpdump, openssl, binutils, strace, ltrace, xxd, tree, iproute2, dig, shellcheck, Manpages. Aufruf aus dem Bash-Tool: `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu-26.04 --exec bash -c '…'` (nur mit `--exec` bleiben `$`-Variablen erhalten), längere Abläufe als Skript im Scratchpad über `/mnt/c/…` starten. Arbeite in `/home/student/<reihe>k<N>/`; nichts außerhalb davon dauerhaft verändern, keine Dienste nach außen öffnen, Scans und Netzversuche nur gegen `localhost` oder eigene Container/VMs.
  - **Achtung, uutils:** Ubuntu 26.04 nutzt für `ls`, `cp`, `cat` usw. die Rust-Neuimplementierung *uutils coreutils* und für `sudo` *sudo-rs*; die GNU-Fassungen heißen hier `gnuls` usw. Ausgaben stimmen meist überein, Fehlermeldungen und seltene Optionen können abweichen. Schreib im Heft, was auf einem gewöhnlichen Linux (GNU, z. B. Kali oder Debian) und auf Ubuntu 26.04 gleichermaßen gilt; wo beide sich unterscheiden und es für den Leser zählt, nenne es.
  - **Windows:** Python 3.13 mit NumPy 2.3 und scikit-learn 1.9 (kein PyTorch), MinGW gcc/g++/gdb (Windows-ABI, nicht für Linux-Assembler), CMake, Git Bash.
  - Getesteten Code legst du unter `<Heftordner>\code\kap<N>\` ab, Zahlen prüft `rechnung_kap<N>.py` (erste Zeilen `import sys; sys.stdout.reconfigure(encoding="utf-8")`). Ausgaben im Heft sind echte Ausgaben (Benutzername `student`, Rechnername neutral, z. B. `labor`); was sich nicht testen ließ, nennst du im Bericht.

## Abbildungen
- Jede neue Abbildung: TikZ im Heft in `abb` (im Kasten: `center` mit `\captionof{figure}`), Label `fig:k<N>name`, und eine Editor-Szene mit demselben Namen (`<reihe>/k<N>name`) in `tools/szenen/<reihe>_teil<N>.py` (Gerüst liegt bereit). Stil wie `tools/szenen/et3_teil2.py` (Klasse `Block` für Kästen und Pfeile, `Szene.achsen` für Diagramme), Wörter über `s.tr` in vier Sprachen. TikZ-Stile der Präambel: `blk`, `geraet`, `zelle`, `fluss`, `kn`.
- Im Repo `C:\Users\info\PycharmProjects\pythonanimation`: `python tools/szenen/<reihe>_teil<N>.py`, dann `python tools/export_szenen.py <namen>` (immer mit Namen). Jedes Bild höchstens 548 px breit; das Skript warnt sonst. Mit `python tools/szenen_ansehen.py <out.png> <name>` siehst du dir jedes Bild an.
- Abbildungen zeigen den Begriff selbst (Anschauung vor der Formel), nicht Dekoration.

## Dateien
`Kap<N>_<Name>.tex` (Hauptdatei wie `C:\Bücher\ET3\Arbeitshefte\Kap2_Laplace.tex`: `\input{praeambel}`, Titelblock mit `\LARGE` und `\large`, Zeile „Arbeitsheft Cybersecurity, Teil N. Stand: <heutiges Datum>“ bzw. „Arbeitsheft Machine Learning, Teil N. …“, Inhaltsverzeichnis, `\input` der Teile), `kap<N>_stufen.tex` (bei Bedarf `kap<N>_stufen_b.tex`), `kap<N>_loesungen.tex`, optional `rechnung_kap<N>.py` und `code\kap<N>\`.

## Bauen und prüfen
- **PDF:** im Heftordner `pdflatex -interaction=nonstopmode Kap<N>_<Name>.tex` dreimal. `grep -c '^!'` muss 0 sein, keine Overfull-hbox-Meldungen. Danach aux/log/out/toc löschen.
- **PDF maschinell prüfen statt als Bild lesen (Token-Kosten!):** im Repo `python tools/pdf_pruefen.py <heft.pdf> <scratchpad>/pdf --blatt`. Das Skript meldet ohne Modell-Tokens:
  - fehlende Verweise (`??`);
  - Text und Zeichnungen, die über den Satzspiegel ragen;
  - Beschriftungen, die einander überlappen, typisch in TikZ-Abbildungen.

  Zu jeder Meldung schreibt es einen kleinen Ausschnitt `stelle_<n>.png`, außerdem `text.txt` mit dem Text aller Seiten (für Grep) und mit `--blatt` Übersichtsblätter der Abbildungsseiten, sechs Seiten je Bild.
  - Sieh dir nur die gemeldeten Ausschnitte an und jedes Übersichtsblatt höchstens einmal.
  - Das PDF selbst liest du **nie** ganz oder in großen Blöcken als Bild ein. Jede Seite geht als Bild in deinen Kontext und wird bei jeder weiteren Anfrage mitgeschickt; ein Pilotheft kam so auf fast 800k Tokens Kontext. Einzelne Seiten (`pages: "12"`) nur, wenn ein Übersichtsblatt eine Frage offen lässt.
  - Den Text prüfst du im LaTeX-Quelltext, nicht im PDF.
  - Die Editor-Szenen prüfst du über das Kontaktblatt von `szenen_ansehen.py`, mehrere Szenen auf einem Bild.
- **Alle Dateien vollständig lesen** (Wunsch des Users, 04.11.2026: „Er soll die Dateien schon durchlesen“, „der Agent soll alles lesen!“):
  - die Pflichtlektüre;
  - die früheren Hefte der Reihe;
  - die Musterhefte;
  - zur Selbstprüfung dein eigenes Heft ganz, Satz für Satz.

  Gespart wird **nur** beim PDF: keine Seitenbilder, sondern `pdf_pruefen.py` wie oben.
- **Konverter:** im Repo `python tools/heft_zu_artikel.py <reihe> --kap <N> --lang de --pruefen --katex`: 0 KaTeX-Fehler, keine „unbekannt“-Meldungen, keine Verweise ohne Ziel, keine Aufgaben ohne Lösung. Danach dasselbe ohne `--pruefen --katex`, um die Artikel zu schreiben.
- **Selbstprüfung Satz für Satz (UEBERARBEITUNG §7):** kein Satz mit zwei neuen Begriffen; nichts benutzt, bevor es erklärt ist; kein Haupttext, der sich auf einen Hintergrund-Kasten stützt; nichts Wichtiges aus der WISSEN-Datei fehlt; jedes zentrale Verfahren hat seinen Warum-Kasten; kein Vorgriff; jede Aussage zu Recht, Standards und Zahlen stimmt mit dem Stand von heute.

## Grenzen
- Nur dein Heft (Dateien oben) und die Szenendatei deines Teils anfassen, dazu `web/szenen/<reihe>/` und `web/abbildungen/**` durch das Export-Skript. Keine anderen Hefte, keine Präambel, keine Übersetzungen, nicht `heft_zu_artikel.py` oder `build_wissen.py`. Fehlt dir etwas in der Präambel, nenne es im Bericht.
- `build_wissen.py` nicht ausführen; git nicht benutzen; nichts installieren.
- LaTeX und Python nur mit Write/Edit schreiben. Im Bash-Tool werden doppelte Backslashes halbiert; Heredocs mit Backslashes zerbrechen.
- Hilfsdateien in den Unterordner `<reihe>k<N>` des Scratchpads, den dir die Nachricht nennt.

## Bericht (knapp)
- Gliederung: Abschnitte und Unterabschnitte in je einer Zeile.
- Seitenzahl, Zahl der Aufgaben (davon praktisch), neue Abbildungen und Szenen, Code-Dateien.
- Die wichtigsten Warum-Kästen mit der Quelle der Recherche (nur im Bericht, nicht im Heft).
- Was aus der WISSEN-Datei bewusst nicht aufgenommen wurde und warum.
- Still korrigierte Fehler der Quellen, umbenannte Symbole, nicht ausgeführte Befehle, offene Punkte, Wünsche an die Präambel.
