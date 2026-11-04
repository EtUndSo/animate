# Auftrag: Recherche für eine neue Heftreihe (Cybersecurity bzw. Machine Learning)

Der User möchte zwei neue Arbeitsheft-Reihen, die später auch Website-Artikel auf EtUndSo werden: **Cybersecurity** und **Machine Learning**. Seine Worte:
- „Dabei auch von Grund auf anfangen, die Basics erklären, danach in die verschiedenen Abzweige reingehen.“
- „Stelle zunächst eine umfassende Recherche der besten Quellen an, um die nötigen Informationen zu sammeln. Speicher die Informationen auch in dem Ordner EtUndSo.“
- „Bestmöglich auch mit Aufgaben, z. B. Bedienung der Konsole über Linux-Boot-USB-Stick, Programmierung von Machine-Learning-Methoden in Python oder C++.“
- „Alle Themen sollten von Grund auf erklärt werden und dann mit der Komplexität steigern, also genau so wie bei den Uni-Modulen. Sodass alles aufeinander aufbaut und man es gut nachvollziehen kann.“

Du machst **nur die Recherche** für **ein** Thema (siehe Nachricht) und legst alles geordnet ab. Die Hefte selbst schreibst du nicht.

## Leser und Maßstab
Leser sind Studierende der Elektrotechnik (etwa 5. Semester).
- Sie kennen Mathematik bis Höhere Mathematik 3/4, Signale und Systeme und etwas Programmierung.
- Für das Fach selbst bringen sie kein Vorwissen mit.

Die späteren Hefte folgen `C:\Users\info\PycharmProjects\pythonanimation\notizen\UEBERARBEITUNG.md`; lies diese Datei, damit die Recherche dazu passt:
- ein neuer Begriff nach dem anderen;
- Theorie vor Praxis;
- keine Vorgriffe;
- zu jedem Thema ein recherchiertes „Warum“.

## Gründlichkeit vor Tempo
Der User sagte: „die Recherchen können Minuten bis Stunden laufen, das ist in Ordnung. Denn sie bilden die Grundlage der gesamten Hefte und entscheiden somit größtenteils darüber, ob sie gut oder schlecht werden.“
- Hauptquellen wirklich lesen, also Kapitel und Abschnitte, nicht nur Inhaltsverzeichnisse.
- Aussagen gegen mehrere Quellen prüfen.

## Rangfolge der Quellen (Vorgabe des Users, 04.11.2026)
„Versuche als Quellen hauptsächlich Bücher und Kurse professioneller Universitäten zu nutzen, sodass wir die qualitativ hochwertigsten Quellen und damit Informationen nutzen.“
- **Hauptquellen:** Lehrbücher von Universitätsverlagen und anerkannten Fachautoren sowie Kursmaterialien renommierter Universitäten (Skripte, Lecture Notes, Kursbücher).
- **Ergänzung:**
  - offizielle Standards und Dokumentationen;
  - Lernplattformen, nur für Übungen;
  - Blogs und Videos, nur für Anschauung.
- In QUELLEN.md steht je Quelle „Hauptquelle“ oder „Ergänzung“. Die WISSEN-Dateien belegen bevorzugt aus Hauptquellen.

## Was du recherchierst
1. **Die besten Quellen**, mindestens 30, breit gestreut. Für jede Quelle:
   - Titel, Autor oder Anbieter und URL;
   - welche Themen sie abdeckt, in welcher Tiefe, für welches Niveau;
   - Format (Kurs, Buch, Plattform, Paper, Doku), ob kostenlos, und die Lizenz (darf man sie nur als Wissensquelle nutzen oder auch Material übernehmen?);
   - wofür genau sie in unserer Reihe taugt.

   Prüfe jede Quelle selbst (WebSearch/WebFetch). Bevorzuge anerkannte, aktuelle Quellen: Uni-Kurse mit freien Materialien, Standardwerke, offizielle Dokumentationen, etablierte Lernplattformen. Bei Plattformen mit Modulen (z. B. pwn.college-Dojos) liste die Module einzeln auf.
2. **Den Lernpfad.** Er besteht aus einer Folge von Heften, die von Grund auf aufbauen: erst ein gemeinsamer Grundlagenstamm, dann Abzweige. Für jedes geplante Heft:
   - Titel;
   - Lernziele;
   - Begriffe in der Reihenfolge ihrer Einführung;
   - Voraussetzungen (welche früheren Hefte);
   - Hauptquellen mit genauen Kapiteln, Modulen oder Abschnitten;
   - die wichtigsten „Warum“-Ideen;
   - praktische Aufgaben;
   - Ideen für Abbildungen.

   Begründe die Reihenfolge.
3. **Das Wissen selbst.** Je geplantes Heft eine Datei mit dem Kernwissen: Definitionen, Mechanismen, Formeln bzw. Befehle, typische Fehler und Missverständnisse, Beispiele, Quellenangaben je Absatz.
   - Schreibe in eigenen Worten auf Deutsch und so ausführlich, dass später ein Heft daraus geschrieben werden kann, ohne die Quellen noch einmal komplett lesen zu müssen.
   - Nichts wörtlich abschreiben, nur kurze Zitate mit Quellenangabe.
4. **Die Aufgaben.** Praktische Aufgaben je Heft mit genauer Einrichtungsanleitung und Lösungsidee, steigend in der Schwierigkeit.

## Ablage
Alles kommt in `C:\Bücher\EtUndSo\<Thema>\Recherche\` (`Cybersecurity` bzw. `MachineLearning`):
- `QUELLEN.md`: die bewertete Quellenliste, gegliedert nach Art und Thema.
- `LERNPFAD.md`: die Heftfolge mit allen Angaben aus Punkt 2 und einer Übersichtsgrafik als Text (Stamm und Äste).
- `WISSEN_T<NN>_<kurzname>.md`: eine Datei je geplantem Heft (Punkt 3).
- `AUFGABEN.md`: alle praktischen Aufgaben (Punkt 4).
- `ZUSAMMENFASSUNG.md`: eine Seite mit den wichtigsten Entscheidungen und offenen Fragen an den User.

Frei verfügbare und frei lizenzierte Dokumente (z. B. CC-lizenziert) darfst du zusätzlich in `Recherche\Material\` speichern. Urheberrechtlich geschützte PDFs nicht herunterladen, nur verlinken.

## Grenzen
- Für die **Recherche** darfst du Unteragenten einsetzen; das hat der User ausdrücklich erlaubt. Wegen des Nutzungslimits gilt (Entscheidung des Users vom 04.11.2026):
  - **höchstens drei Unteragenten gleichzeitig.** Weitere startest du erst, wenn einer fertig ist;
  - **Unteragenten laufen auf Sonnet** (beim Agent-Aufruf `model: "sonnet"`). Sie suchen, rufen Seiten ab und exzerpieren Kapitel in Notizdateien;
  - die Quellenbewertung, den Lernpfad und die WISSEN-Dateien schreibst du selbst, damit sie aus einem Guss sind;
  - PDF-Seiten nur als Bild lesen, wenn der Text Formeln oder Abbildungen nicht wiedergibt. Sonst den Text extrahieren.
- Zwischennotizen (z. B. Mitschriften zu einzelnen Quellen) kommen nach `Recherche\Notizen\`, nicht ins Scratchpad. Auf sie wird später verwiesen, und das Scratchpad ist nur temporär.
- Nur recherchieren und Dateien in deinem `Recherche`-Ordner schreiben. Keine Hefte, keine Änderungen am Repo, kein git.
- Dateien mit dem Write-Tool schreiben. Im Bash-Tool werden doppelte Backslashes halbiert.
- Hilfsdateien kommen in einen eigenen Unterordner des Scratchpads `C:\Users\info\AppData\Local\Temp\claude\C--B-cher\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\recherche_<thema>\`.
- Am Ende ein knapper Bericht:
  - Zahl der Quellen;
  - der Lernpfad als Liste;
  - die wichtigsten Entscheidungen;
  - offene Fragen an den User.
