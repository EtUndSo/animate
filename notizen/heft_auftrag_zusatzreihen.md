# Auftrag: ein Heft der Zusatzreihen Cybersecurity (cyber) und Machine Learning (ml) neu schreiben

Du schreibst **ein** deutsches Arbeitsheft von Grund auf neu; Reihe und Teil nennt dir die Nachricht. Es gibt kein Skript: Der **Lernpfad** der Recherche gibt Reihenfolge und Gliederung vor, die **WISSEN-Datei** des Hefts ist die Inhaltsgrundlage. Muster für Aufbau und Qualität sind die zwei abgenommenen Pilothefte (User: „so ist es um Welten besser … Genau so weiter“). Qualität geht vor allem, die Zeit spielt keine Rolle.

Dieser Auftrag ersetzt für die Zusatzreihen `ueberarbeitung_auftrag.md`. `UEBERARBEITUNG.md` gilt vollständig; wo dort „Skript“ steht, lies „Lernpfad-Eintrag und WISSEN-Datei des Hefts“.

## Zwei Phasen: Schreiben und Prüfen (seit 09.11.2026)
Jedes Heft entsteht nacheinander durch zwei Agenten. Deine Nachricht sagt dir, welche Phase du bist. Grund: Der User will „den Verbrauch senken ohne dabei die Qualität zu beeinflussen“. Die vielen kleinen Schritte am Ende (bauen, prüfen, korrigieren, Szenen) brauchen die Quellen nicht mehr. Ein frischer Agent macht sie mit einem Drittel des Kontexts und liest das Heft dabei mit unabhängigen Augen.

**Phase 1, Schreib-Agent:**
- „Zuerst lesen“: alle Quellen ganz.
- Recherche, dann das ganze Heft schreiben: Hauptdatei, Stufen, Lösungen, TikZ-Abbildungen, Code unter `code\kap<N>\` (jedes Programm beim Schreiben einmal unter Windows und Linux ausführen; die echte Ausgabe ins Heft) und `rechnung_kap<N>.py` (ausgeführt, 0 Fehler).
- Kein PDF-Bau, keine Editor-Szenen, kein Konverter, keine Themenkarte. Die Satz-für-Satz-Prüfung macht Phase 2. Du schreibst trotzdem so sorgfältig, als gäbe es keine zweite Prüfung.
- **Übergabe** `uebergabe_kap<N>.md` im Heftordner, 1–2 Seiten:
  - Gliederung;
  - Abbildungen mit Label und gewünschter Szene;
  - Kandidaten für Rechenbilder;
  - was getestet ist und was nicht;
  - Warum-Kästen mit ihren Quellen;
  - bewusst Weggelassenes, still korrigierte Quellenfehler, neue Bezeichnungen;
  - offene Fragen an den Prüfer;
  - Lese-Nachweis.
- Dann ein knapper Bericht (Abschnitt „Bericht“, ohne Prüfergebnisse).

**Phase 2, Prüf-Agent:**
- **Lesen:**
  - diesen Auftrag;
  - `UEBERARBEITUNG.md`;
  - die Präambel;
  - den Lernpfad-Eintrag des Hefts;
  - die WISSEN-Datei ganz;
  - die Übergabe;
  - die Zusammenfassungen der früheren Hefte;
  - dann **das ganze Heft samt Lösungen, Satz für Satz**.

  Die übrigen Quellen liest du nur gezielt, wenn eine Aussage zu prüfen ist.
- **Arbeiten:**
  - Selbstprüfung nach „Bauen und prüfen“ (UEBERARBEITUNG §7) und Korrekturen;
  - PDF und `pdf_pruefen.py`;
  - Abgleich aller Code-Blöcke mit echter Ausführung (`heft_pruefen.py`);
  - `rechnung_kap<N>.py`;
  - Editor-Szenen und Rechenbilder mit Kontaktblatt;
  - Konverter, Artikel, `themenkarte.py`;
  - `zusammenfassung_kap<N>.md`;
  - Bericht.

  In den Bericht übernimmst du die Angaben der Übergabe und ergänzt deine Korrekturen.
- Inhaltliche Änderungen, die über Korrekturen hinausgehen, z. B. ein fehlendes Thema aus der WISSEN-Datei, schreibst du selbst, im Stil des Hefts.

## Sparsam mit dem Kontext (beide Phasen)
Alles, was du liest, schreibst oder ausgibst, bleibt in deinem Kontext und wird bei jedem weiteren Schritt erneut mitgeschickt. Deshalb:
- **Jede Datei einmal mit Write anlegen**, danach nur noch mit Edit und kleinen `old_string`s von wenigen Zeilen ändern. Nie eine große Datei ein zweites Mal komplett schreiben. Nie ein Edit über große Teile einer Datei; für einen umgebauten Abschnitt mehrere kleine Edits.
- **Nach Write oder Edit nicht zur Kontrolle neu lesen.** Die Werkzeuge melden Fehler selbst. Eine Datei liest du einmal ganz; danach nur noch die nötigen Zeilen (offset/limit) oder per Grep.
- **Befehlsausgaben filtern:** pdflatex mit `| grep -E '^!|Overfull|undefined' | head -20`, Testskripte geben nur Abweichungen und eine Schlusszeile aus, lange Ausgaben mit `tail`/`head`.
- **Bilder** (Kontaktblätter, gemeldete PDF-Stellen) je höchstens einmal ansehen, nach einer Korrektur nur den betroffenen Ausschnitt.
- **Recherche** über Unteragenten (Sonnet), die knappe Exzerpte mit Fundstelle liefern, keine ganzen Seiten. Webseiten nicht selbst in deinen Kontext laden.
- **Nichts davon spart an der Qualität:** Die Quellen liest du weiterhin ganz (Phase 1), das Heft wird weiterhin ganz geprüft (Phase 2).

## Zuerst lesen
**Quellen vollständig, eigene Hefte über Zusammenfassungen.** Der User verlangt, dass alle **Quellen** ganz gelesen werden: „Ein Abschnitt aus einem ganzen Buch zu lesen ist wie ein Wassertropfen aus einem See, das macht keinen Sinn“. Am 06.11.2026 präzisierte er: „Mit vollständig lesen meinte ich die Quellen. Die eigenen erstellten Hefte müssen ja nicht nochmal vollständig gelesen werden, da reichen Zusammenfassungen.“
- **Quellen** liest du **von der ersten bis zur letzten Zeile**: Leitfaden, Präambel, LERNPFAD, WISSEN-Datei, AUFGABEN, ZUSAMMENFASSUNG, QUELLEN und die Notizen zu deinem Heft. Große Dateien liest du in aufeinanderfolgenden Teilen (offset/limit), bis das Ende erreicht ist. Meldet Read eine Teilansicht („PARTIAL view“), liest du weiter.
- **Eigene frühere Hefte** (Musterhefte und frühere Teile der Reihe) liest du **nicht ganz**:
  - Für die früheren Teile deiner Reihe liest du deren Zusammenfassung `zusammenfassung_kap<N>.md` im Heftordner. Verweist du auf eine bestimmte Stelle zurück, liest du genau diese Stelle nach.
  - Von den Musterheften liest du einen vollständigen Abschnitt und den Abschluss als Stilvorbild.
- **Dein eigenes neues Heft** prüfst du am Ende trotzdem ganz, Satz für Satz (Selbstprüfung, siehe „Bauen und prüfen“).
- Gespart wird außerdem beim PDF (siehe „Bauen und prüfen“).

1. `C:\Users\info\PycharmProjects\pythonanimation\notizen\UEBERARBEITUNG.md`: der maßgebliche Leitfaden, besonders §2 (ein Begriff nach dem anderen, Theorie vor Praxis), §3 und §3a (Hintergrund-Kästen mit recherchiertem Warum) und §4 (keine Vorgriffe).
2. Die beiden Muster, je ein vollständiger Abschnitt und der Abschluss (Kernboxen, Prinzip-Tabelle, ein Stück Lösungen):
   - ET3 Teil 2: `C:\Bücher\ET3\Arbeitshefte\kap2_stufen.tex` (Abschnitt 1), `kap2_stufen_b.tex` (Ende), `kap2_loesungen.tex` (Anfang).
   - HöMa3 Teil 1: `C:\Bücher\HöMa3\Arbeitshefte\kap1_stufen.tex` (ein Abschnitt und Ende).
3. Die Präambel deiner Reihe (`praeambel.tex` im Heftordner, siehe unten): Kästen, Code-Umgebungen, Makros. Benutze nur, was dort steht.
4. Aus `C:\Bücher\EtUndSo\<Reihe>\Recherche\`, jeweils ganz:
   - `LERNPFAD.md`: darin **der Eintrag deines Hefts** (Lernziele, Begriffe in Einführungsreihenfolge, Voraussetzungen, Hauptquellen, Warum-Ideen, Aufgaben, Abbildungen); bei ML die „Notationsentscheidungen“.
   - `WISSEN_T<NN>_*.md` deines Hefts. Das ist die Inhaltsgrundlage.
   - `AUFGABEN.md` (Lösungsideen sind für dich, nicht wörtlich fürs Heft).
   - `ZUSAMMENFASSUNG.md`: die Entscheidungen des Users.
   - `QUELLEN.md`.
   - die Dateien in `Notizen\`, die dein Heft betreffen (Belegstellen, Prüfprotokolle, Hauptquellen-Exzerpte deiner Teile).
5. Die fertigen früheren Hefte der Reihe über ihre Zusammenfassungen `zusammenfassung_kap<N>.md` im Heftordner. Ihre Begriffe, Bezeichnungen, Datensätze und Beispiele übernimmst du; Einzelstellen liest du bei Bedarf im Heft nach.

**Neue Pflichtlieferung:** Am Ende schreibst du `zusammenfassung_kap<N>.md` für dein Heft, auf Deutsch, etwa 2–4 Seiten. Sie ist für spätere Agenten gedacht, nicht für Leser. Inhalt:
- Gliederung (Abschnitt und Unterabschnitt mit Nummer);
- je Abschnitt die eingeführten Begriffe mit Kurzdefinition und den wichtigsten Formeln und Sätzen;
- festgelegte Bezeichnungen und Konventionen;
- wiederverwendbare Datensätze und Beispiele mit ihren Zahlen;
- Abbildungen und Szenennamen;
- was bewusst auf spätere Hefte verschoben ist.

| Reihe | Heftordner | Recherche | Szenen |
|---|---|---|---|
| cyber | `C:\Bücher\EtUndSo\Cybersecurity\Arbeitshefte` | `C:\Bücher\EtUndSo\Cybersecurity\Recherche` | `tools/szenen/cyber_teil<N>.py`, Namen `cyber/k<N>name` |
| ml | `C:\Bücher\EtUndSo\MachineLearning\Arbeitshefte` | `C:\Bücher\EtUndSo\MachineLearning\Recherche` | `tools/szenen/ml_teil<N>.py`, Namen `ml/k<N>name` |
| prog | `C:\Bücher\EtUndSo\Programmieren\Arbeitshefte` | `C:\Bücher\EtUndSo\Programmieren\Recherche` | `tools/szenen/prog_teil<N>.py`, Namen `prog/k<N>name` (Python N = Kap N, C ab Kap 101, C++ ab Kap 201) |
| linux | `C:\Bücher\EtUndSo\Linux\Arbeitshefte` | `C:\Bücher\EtUndSo\Linux\Recherche` | `tools/szenen/linux_teil<N>.py`, Namen `linux/k<N>name` |

**Nummern:** Dateien, Szenen, Labels und der Umwandler (`--kap N`) zählen immer nach der **Lernpfad-Nummer** T<NN>: `Kap<N>_<Name>`, `kap<N>_stufen.tex`, `ml_teil<N>.py`, `ml/k<N>name`, `fig:k<N>…`. Angezeigt wird:
- Cybersecurity: Teil N = T<NN> (Teil 1 = T01).
- Machine Learning: T01–T06 als „Grundlagen 1–6“, ab T08 als „Teil N“ mit **N = Lernpfad-Nummer − 7** (Teil 1 = T08 = `Kap8_Lernen`, Szenen `ml/k8…`, Datei `ml_teil8.py`).

Der Dateiname `Kap<N>_<Name>` steht in `tools/heft_zu_artikel.py` unter `MODULE["cyber"]` bzw. `MODULE["ml"]` und muss exakt stimmen; dort steht auch, welcher Bereich welche Nummern hat (`"bereiche"`).

**Machine Learning: Grundlagen und Pfad** (Entscheidung des Users, 05.11.2026). Der User: „Wir sollten die mathematischen Grundlagen bei ML als solche markieren, also eher als Nachschlagwerk … Sonst verbringt man Wochen damit diese zu lernen obwohl man sie erst sehr spät oder gar nicht braucht.“
- **Mathematische Grundlagen:** Die Lernpfad-Hefte T01–T06 heißen „Grundlagen 1–6“ und bilden einen eigenen Bereich „Mathematische Grundlagen (zum Nachschlagen)“.
  - Untereinander verweisen sie mit „Grundlagen N, Abschnitt M“ (umgestellt am 06.11.2026 in Grundlagen 1–5 und allen Übersetzungen). Titelzeile: „Mathematische Grundlagen für Machine Learning, Grundlagen~N. Stand: …“.
  - Spätere ML-Hefte nennen sie nicht (keine Vorgriffe). Die Website zeigt unter jedem Grundlagen-Artikel automatisch einen Block „Verwendet in“ mit den ML-Artikeln, die ihn oder einen seiner Abschnitte verlinken. Damit das klappt, muss der Verweis genau die Wendung unten haben.
- **Der ML-Pfad** beginnt mit T08 „Lernen aus Daten“: **ML-Teil N = Lernpfad-Heft T(N+7)**. T07 (Python/NumPy) entfällt im Pfad, weil Python im Bereich „Programmieren“ erklärt wird (siehe „Nichts doppelt erklären“). Die Titelzeile lautet „Arbeitsheft Machine Learning, Teil~N“, Rückverweise auf frühere Pfad-Hefte „Teil N, Abschnitt M“.
- **Jedes ML-Pfad-Heft setzt die Grundlagen nicht voraus.** Wo es Mathematik braucht, steht zu Beginn des Abschnitts „Was du dafür brauchst“:
  - jedes benötigte Grundlagen-Thema in einer kurzen, selbsttragenden Zusammenfassung (Definition, eine Formel, ein Mini-Beispiel);
  - dazu der Verweis „ausführlich: Grundlagen N, Abschnitt M“, auf der Website ein Link.

  Wer die Grundlagen kennt, überspringt das; wer nicht, kann trotzdem weiterlesen oder gezielt nachschlagen. Nimm nur auf, was das Heft wirklich braucht, und genau dort, wo es gebraucht wird.
- **Optimierung (T06 = Grundlagen 6)** entsteht erst kurz bevor ein Pfad-Heft sie braucht, vor dem Gradientenabstieg.

**Nichts doppelt erklären** (Vorgabe des Users, 06.11.2026). Der User: „darauf achten, dass wir Inhalte nicht mehrfach auf der Webseite vollständig erklären … einen separaten Bereich haben … in den ML-Artikeln darauf verweisen und das Wissen als gekannt voraussetzen. Dann nur noch das Programmieren, das zu dem Inhalt passt.“
- **Ein Ort pro Thema:** Jedes Thema wird auf der Website genau einmal vollständig erklärt, im passenden Bereich. Welcher das ist, steht in `notizen/themenkarte.md` (je Zeile ein Abschnitt mit seiner Verweis-Wendung). Vor dem Schreiben suchst du dort jeden Begriff deines Lernpfad-Eintrags mit Grep (nicht die ganze Datei lesen). Nach dem Heft erzeugst du sie mit `python tools/themenkarte.py` neu; Themen, die zu einem anderen Bereich gehören und dort noch kein Heft haben, trägst du von Hand im Teil „Zuständigkeiten und geplante Themen“ ein.
- **Gemeinsame Bereiche:**
  - **Programmieren:** Python (Sprache, Datenstrukturen, Funktionen, Module, venv, NumPy-Grundlagen), später C und C++.
  - **Linux und Kommandozeile:** Shell, Dateien, Rechte, Prozesse.

  ML und Cybersecurity setzen beides voraus.
- **Fachhefte setzen voraus und verweisen:** Ein Fachheft erklärt nur, was zu seinem Inhalt gehört. Ein ML-Heft programmiert das Modell, ein Cybersecurity-Heft Sockets und Bytes. Vorausgesetztes Wissen bekommt höchstens ein bis drei Sätze und einen Verweis mit Link („ausführlich: Programmieren, Python N, Abschnitt M“).
- **Mathematik:** Für die ML-Grundlagen gilt dasselbe gegenüber den Mathematik-Modulen (HöMa). Was dort vollständig erklärt ist, etwa Beweise und Herleitungen, steht in den Grundlagen nur noch als Kurzfassung mit Link.

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
- **Verweise:** Rückverweise sind erwünscht. Keine Vorgriffe auf spätere Teile, auch nicht im Hintergrund-Kasten (§4). Der Umwandler macht aus genau diesen Wendungen Links auf Artikel und Abschnitt (mit `~`, Nummer M mit Punkt):
  - Cybersecurity und ML-Pfad: frühere Hefte „Teil~N“ bzw. „Teil~N, Abschnitt~M“ (ML: Teil N = T(N+7));
  - ML-Grundlagen: „Grundlagen~N, Abschnitt~M“, mehrere „Grundlagen~N, Abschnitte~M und~K“, das ganze Heft „Grundlagen~N“; erlaubt in den Grundlagen und im ML-Pfad;
  - gemeinsame Bereiche, aus jeder Zusatzreihe: „Programmieren, Python~N, Abschnitt~M“ (später „Programmieren, C~N …“, „Programmieren, C++~N …“) und „Linux~N, Abschnitt~M“;
  - andere Formen („Abschn.“, „Kapitel 3“, „Python~2“ ohne „Programmieren,“) bleiben Text ohne Link. Gibt es das Ziel noch nicht, bleibt der Verweis Text; fehlt nur der Abschnitt, meldet der Umwandler „Verweise auf fehlende Abschnitte“. Wendungen der Übersetzungen: `notizen/heft_uebersetzung.md`.
- **Ende:** kernbox „Das Wichtigste bis hier“, kernbox „Die Antwort in drei Sätzen“, Prinzip-Tabelle mit Abschnittsverweisen (ML ab Teil 2 = T09: „Modell + Verlust + Optimierung + Prüfung“), dann `\section{Lösungen}` aus `kap<N>_loesungen.tex`.
- **Keine Quellenverweise im Heft:** keine Buch-, Kurs-, Uni- oder Kapitelangaben, kein „nach X“, kein Literaturverzeichnis. Gesetze, Standards, Organisationen (StGB, RFC, NIST, BSI, CVE) und die Namen von Prinzipien (Kerckhoffs, Saltzer und Schroeder) dürfen als Inhalt vorkommen. Links auf Übungsplattformen (pwn.college, OverTheWire, PortSwigger Web Security Academy, CryptoHack usw.) sind als Übungsumgebungen erlaubt.
- **Ton:** seriös und professionell, aber nicht steif; der Ton der Musterhefte trifft es. Aufgaben sprechen den Leser mit du an.

## Praxis: Aufgaben, Code, Labor
- **Jeder Abschnitt** endet mit mindestens einer Aufgabe; die Aufgaben benutzen nur, was bis dahin erklärt ist. Gemischt: verstehen, rechnen, vorhersagen, praktisch ausführen; Schwierigkeit \stern\ bis \stern\stern\stern. Jede Aufgabe mit `\label{a:...}` und ausführlicher Lösung `\loesung{a:...}` in `kap<N>_loesungen.tex`: der Weg, das Ergebnis und warum es so ist.
- **Cybersecurity:** Praxis heißt Konsole und Labor, aber erst ab dem Heft, das das Werkzeug einführt (Konsole ab Teil 3; vorher Browser, Papier, Windows-Bordmittel, soweit erklärt).
  - Grundregel in jedem Heft mit praktischen Übungen als Kasten `warnung`: nur eigene Systeme, erlaubte Lernplattformen innerhalb ihrer Regeln oder isolierte Labore. Der Rechtsstand muss exakt und aktuell sein; das Heft ist keine Rechtsberatung und sagt das.
  - Riskante Schritte (Datenträger beschreiben, Bootreihenfolge, Secure Boot, BitLocker) stehen mit ihrem Risiko und der Absicherung in einem `warnung`-Kasten, bevor der Schritt kommt.
  - Lösungen von Plattform-Aufgaben werden nie abgedruckt (pwn.college und OverTheWire verbieten es): Dort nur gestufte Hinweise. Vollständige Lösungen gibt es für die eigenen Aufgaben des Hefts.
- **Machine Learning:** Programmieren in Python ab ML-Teil 1. Python, venv und NumPy-Grundlagen setzt das Heft voraus und verweist auf den Bereich „Programmieren“; ML-eigene Werkzeuge (scikit-learn, Datensätze) führt es dort ein, wo sie zuerst gebraucht werden. C++ nur in den Heften, die der Lernpfad markiert. Die Grundlagen 1–6 rechnen von Hand und mit Zahlenbeispielen; kein Werkzeug vor seinem Begriff. Notation strikt nach den Notationsentscheidungen im Lernpfad und den Bezeichnungen der Grundlagen (`notizen/zusatzreihen_stand.md`).
- **Erst selbst bauen, dann die Bibliothek** (Vorgabe des Users, 05.11.2026). Der User: „bei jedem Thema (falls ohne riesigen Aufwand möglich) erst zeigen, wie man es von Grund auf implementieren kann, das hilft enorm für das Verständnis, dann zeigen, welche fertigen Bibliotheken es dafür gibt und wie man sie nutzt. Also immer den manuellen und dann den fertigen Weg“.
  - **Reihenfolge je Verfahren:**
    1. eine kleine eigene Umsetzung von Grund auf, nur mit dem, was bis dahin eingeführt ist: reines Python bzw. NumPy-Grundfunktionen, bei Cybersecurity Shell oder Python mit Sockets;
    2. dann die üblichen fertigen Bibliotheken bzw. Werkzeuge (z. B. scikit-learn, `numpy.linalg`, PyTorch; nmap, openssl, Wireshark), wie man sie benutzt und welche Optionen zählen;
    3. zum Schluss ein Vergleich: Beide Wege liefern auf denselben Daten dasselbe Ergebnis, mit echter Ausgabe. Was die Bibliothek zusätzlich leistet (Numerik, Tempo, Randfälle), steht in einem Satz.
  - **Ausnahmen:** Wo die eigene Umsetzung riesigen Aufwand bedeutet (etwa ein vollständiges TLS, ein Compiler, ein GPU-Kernel), genügt eine stark vereinfachte Kernidee als Skizze. Das Heft sagt dann, was weggelassen ist.
  - Die Grundlagen-Hefte rechnen weiter von Hand, ohne Code.
- **Code-Listings** (Präambel): `konsole` (Sitzung: Eingabe mit `$ `, `# ` oder `>>> ` am Zeilenanfang, sonst Ausgabe), `bash`, `python`, `ccode`, `cppcode`, `asm` (Intel), `gas` (AT&T), `ausgabe` (reiner Text). Optionaler Titel: `\begin{python}[hallo.py]`. Code ab Spalte 0, ohne Tabulatoren; Zeichen außerhalb von ASCII nur in Kommentaren und Zeichenketten. Im Fließtext `\texttt{...}` (Sonderzeichen escapen) oder `\verb|...|` (nicht in Überschriften, Kastentiteln und Argumenten). Nie ein Listing direkt nach `\paragraph{…}`: die Überschrift läuft sonst in die erste Code-Zeile und der Block ragt über den Rand; immer erst ein Satz.
- **Code im Heft prüfen:** `C:\Bücher\EtUndSo\Programmieren\Arbeitshefte\code\kap2\heft_pruefen.py` (aus Python 2) vergleicht alle Code-Blöcke eines Hefts mit echter Ausführung unter Windows und Linux; kopieren und für dein Heft anpassen.
- **Code in Szenen:** In `s.formel` bleibt Code in `\texttt{…}` oder `\mathtt{…}` unverändert (`4.0` bleibt `4.0`); nur Zahlen außerhalb davon bekommen in de/es/fr/tr das Dezimalkomma.
- **Übungsumgebung der Leser:** Die Leser richten sich ihre Umgebung selbst ein, nach den Anleitungen in den Heften (Live-USB-Stick oder VM ab Teil 3, isoliertes Labor in späteren Teilen; Python-Umgebung im Bereich „Programmieren“). Die Website stellt nie selbst eine Umgebung bereit: keine Online-Terminals, keine eingebetteten Sandboxes, kein ausführbarer Code auf der Seite (Entscheidung des Users vom 04.11.2026, wegen der Sicherheitsrisiken). Externe Übungsplattformen dürfen verlinkt werden.
- **Alles Ausführbare wird getestet**, bevor es ins Heft kommt. Diese Testumgebung gibt es nur auf dem Rechner des Users, für dich:
  - **Linux:** Ubuntu 26.04 LTS unter WSL 2, Benutzer `student` mit sudo ohne Passwort, systemd läuft; installiert sind u. a. gcc 15, gdb, Python 3.14, nmap, nc, tcpdump, openssl, binutils, strace, ltrace, xxd, tree, iproute2, dig, shellcheck, Manpages. Aufruf aus dem Bash-Tool: `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu-26.04 --exec bash -c '…'` (nur mit `--exec` bleiben `$`-Variablen erhalten), längere Abläufe als Skript im Scratchpad über `/mnt/c/…` starten. Arbeite in `/home/student/<reihe>k<N>/`; nichts außerhalb davon dauerhaft verändern, keine Dienste nach außen öffnen, Scans und Netzversuche nur gegen `localhost` oder eigene Container/VMs.
  - **Achtung, uutils:** Ubuntu 26.04 nutzt für die meisten coreutils, etwa `ls`, `cat`, `date`, die Rust-Neuimplementierung *uutils coreutils* und für `sudo` *sudo-rs*. Ausnahmen laut Paket-Changelog, geprüft bei der Recherche am 06.11.2026: `cp`, `mv`, `rm`, `df` und `true` sind GNU. Die GNU-Fassungen der übrigen heißen `gnuls` usw. uutils ist ein einziges Programm, das am Aufrufnamen erkennt, welches Werkzeug es spielt; eine umbenannte Kopie (z. B. von `date`) scheitert deshalb. Ausgaben stimmen meist überein, Fehlermeldungen und seltene Optionen können abweichen. Schreib im Heft, was auf einem gewöhnlichen Linux (GNU, z. B. Kali oder Debian) und auf Ubuntu 26.04 gleichermaßen gilt; wo beide sich unterscheiden und es für den Leser zählt, nenne es.
  - **Windows:** Python 3.13 mit NumPy 2.3 und scikit-learn 1.9 (kein PyTorch), MinGW gcc/g++/gdb (Windows-ABI, nicht für Linux-Assembler), CMake, Git Bash.
  - **Python unter Linux (seit 06.11.2026, vom User erlaubt):** venv `~/venvs/hefte` in WSL mit NumPy 2.5, Matplotlib 3.11, pytest 9.2 und Jupyter (Python 3.14). Aufruf: `~/venvs/hefte/bin/python`. Weitere Pakete installierst du nur in diese venv. Für Linux 1, 9 und 11 darfst du eine Test-VM bzw. einen nur lokal erreichbaren SSH-Server einrichten; sonst gilt „nichts installieren“.
  - Getesteten Code legst du unter `<Heftordner>\code\kap<N>\` ab, Zahlen prüft `rechnung_kap<N>.py` (erste Zeilen `import sys; sys.stdout.reconfigure(encoding="utf-8")`). Ausgaben im Heft sind echte Ausgaben (Benutzername `student`, Rechnername neutral, z. B. `labor`); was sich nicht testen ließ, nennst du im Bericht.

## Abbildungen
- Jede neue Abbildung: TikZ im Heft in `abb` (im Kasten: `center` mit `\captionof{figure}`), Label `fig:k<N>name`, und eine Editor-Szene mit demselben Namen (`<reihe>/k<N>name`) in `tools/szenen/<reihe>_teil<N>.py` (Gerüst liegt bereit; N ist die Lernpfad-Nummer, ML-Pfad Teil 1 also `ml_teil8.py`, `ml/k8…`). Stil wie `tools/szenen/et3_teil2.py` (Klasse `Block` für Kästen und Pfeile, `Szene.achsen` für Diagramme), Wörter über `s.tr` in vier Sprachen. TikZ-Stile der Präambel: `blk`, `geraet`, `zelle`, `fluss`, `kn`.
- Im Repo `C:\Users\info\PycharmProjects\pythonanimation`: `python tools/szenen/<reihe>_teil<N>.py`, dann `python tools/export_szenen.py <namen>` (immer mit Namen). Jedes Bild höchstens 548 px breit; das Skript warnt sonst. Mit `python tools/szenen_ansehen.py <out.png> <name>` siehst du dir jedes Bild an.
- Abbildungen zeigen den Begriff selbst (Anschauung vor der Formel), nicht Dekoration.
- **Summen, Produkte und Skalarprodukte mit konkreten Zahlen** bekommen eine Editor-Abbildung, die die Rechnung Schritt für Schritt ausführt (UEBERARBEITUNG §6). Dafür gibt es `s.summe`, `s.produkt`, `s.skalarprodukt` und `s.formel` in `tools/szenen_lib.py`, Beispiele in `tools/szenen/beispiel_summen.py`. Im Heft steht dieselbe Rechnung als `align*` in einer `abb`-Umgebung mit Label `fig:k<N><name>`.

## Dateien
`Kap<N>_<Name>.tex` (Hauptdatei wie `C:\Bücher\ET3\Arbeitshefte\Kap2_Laplace.tex`: `\input{praeambel}`, Titelblock mit `\LARGE` und `\large`, Zeile „Arbeitsheft Cybersecurity, Teil~N. Stand: <heutiges Datum>“ bzw. „Arbeitsheft Machine Learning, Teil~N. …“ (ML-Pfad, N = Anzeige-Nummer) bzw. „Mathematische Grundlagen für Machine Learning, Grundlagen~N. …“, Inhaltsverzeichnis, `\input` der Teile), `kap<N>_stufen.tex` (bei Bedarf `kap<N>_stufen_b.tex`), `kap<N>_loesungen.tex`, optional `rechnung_kap<N>.py` und `code\kap<N>\`.

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
- **Lesen** (siehe „Zuerst lesen“ oben):
  - die Quellen der Pflichtlektüre ganz, von der ersten bis zur letzten Zeile;
  - die früheren Hefte der Reihe über ihre `zusammenfassung_kap<N>.md`, bei Rückverweisen die betroffene Stelle;
  - von den Musterheften einen Abschnitt und den Abschluss;
  - zur Selbstprüfung dein eigenes Heft ganz, Satz für Satz, samt Lösungen.

  Beim PDF keine Seitenbilder, sondern `pdf_pruefen.py` wie oben.
- **Konverter:** im Repo `python tools/heft_zu_artikel.py <reihe> --kap <N> --lang de --pruefen --katex` (N = Lernpfad-Nummer): 0 KaTeX-Fehler, keine „unbekannt“-Meldungen, keine Verweise ohne Ziel, keine „Verweise auf fehlende Abschnitte“, keine Aufgaben ohne Lösung. Danach dasselbe ohne `--pruefen --katex`, um die Artikel zu schreiben, und `python tools/themenkarte.py` für die Themenkarte.
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
- **Lese-Nachweis:** jede gelesene Datei mit Zeilenzahl und gelesenen Zeilen (Quellen ganz; eigenes Heft samt Lösungen ganz).
