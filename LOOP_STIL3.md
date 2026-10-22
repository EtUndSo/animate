# EtUndSo „Stil 3“ — Ablauf für genau ein Thema (zwei Fassungen)

**Benutzung:**
- **Im Chat:** Der User sagt „weiter“. Du arbeitest genau ein Thema nach dieser Datei ab, berichtest und wartest.
- **Als Loop:**

      /loop EtUndSo Stil 3: Lies C:\Users\info\PycharmProjects\pythonanimation\LOOP_STIL3.md vollständig und arbeite genau ein Thema danach ab.

**Rahmen:**
- **Repo:** `C:\Users\info\PycharmProjects\pythonanimation`. Modell: Opus 5.5.
- **Ein Thema pro Durchgang:** Ein Thema besteht aus zwei Artikeln, der ausführlichen und der kompakten Fassung (ERKLAER_PROMPT §3.1).
- **Qualität vor Tempo:** Qualität und Tiefe gehen vor Tempo; Zeit spielt keine Rolle.
- **Nicht im Ablauf:** Editor-Funktionen, Abbildungen und Animationen entstehen erst nach den Artikeln, in einer eigenen Phase mit dem User (Entscheidung vom 21.10.2026). Im Ablauf entstehen nur Platzhalter und Listeneinträge (B4).
- **Nur eine Sitzung im Repo:** Es arbeitet immer nur **eine** Sitzung im Repo, denn der Build schreibt jedes Mal ganz `web/wissen` neu.

## Pflichtlektüre in jedem Durchgang, vor dem Schreiben

1. **`ERKLAER_PROMPT.md`**, vollständig. Didaktik, Umfang und Inhalt; die Datei hat Vorrang.
2. **`ARTIKEL_BAUPLAN.md`:**
   - §2 Formeln mit ET-Formelzeichen
   - §3a Beispiel-Seite
   - §5 Block-Syntax
   - §8 Review-Checkliste
3. **`ARTIKEL_LEITFADEN.md`:** §8 Sprache, §11 Keine Kopien.
4. **Bei Halbleiter-Themen:** die passenden Kapitel des Lernskripts `C:\Bücher\Praktikum_Mina\Lernskript\k2_halbleiter.tex` bis `k7_kennlinie.tex`.

**Vorbilder:**
- **Markup und Beispiel-Seite:**
  - `content/hoema3/05-integralsaetze-im-raum/03-satz-von-gauss-im-raum.md`
  - `content/hoema3/05-integralsaetze-im-raum/04-poisson-gleichung-und-hauptsatz-der-vektoranalysis.md`
- **Erklärtiefe und Ton:** das Lernskript (ERKLAER_PROMPT §0).
- **ET-Stil:** `C:\Bücher\ET4_Skript_Erklaerung`.

## (B0) Pilot-Sperre

```
cd /c/Users/info/PycharmProjects/pythonanimation && grep -rl '^stil: 3' content | head -1
```

Ist die Ausgabe **leer**, gibt es noch kein Stil-3-Thema. Dann gilt:
1. **Build ergänzen** (ERKLAER_PROMPT §14):
   - `fassung:` erkennen;
   - pro Thema ein Navigationseintrag;
   - Umschalter „Kompakt | Ausführlich“ mit Lesezeiten am Seitenanfang, Wahl der Leserin gemerkt (localStorage, in try/catch);
   - Vor/Zurück innerhalb derselben Fassung;
   - Suche findet beide Fassungen;
   - `:::frage` ausklappbar (Frage sichtbar, Antwort per Klick);
   - `:::grafik` als „Abbildung in Vorbereitung“ mit kleiner Szene-Zeile.
   
   Den Build danach testen: hell, dunkel, Handybreite.
2. **Pilot schreiben:** das Thema `content/get1/10-halbleiterbauelemente/01-halbleiter-und-baendermodell.md` nach (B2) bis (B7).
3. **Anhalten** und den User um Prüfung bitten. Im Loop-Betrieb:
   1. PushNotification „EtUndSo: Pilot-Thema Stil 3 fertig, bitte prüfen“.
   2. ScheduleWakeup mit nur `stop: true`.
   3. **Nicht** weitermachen.

## (B1) Nächstes offenes Thema ermitteln

**Reihenfolge der Module** (Entscheidung vom 22.10.2026): erst ET1, dann HöMa3, dann Numerische Mathematik für Elektrotechnik (Numa). GEMB1 ist damit zurückgestellt; wann es folgt, stimmst du nach Numa mit dem User ab.

Innerhalb von ET1 kommt zuerst der Halbleiter-Block, Kap. 10 bis 12, danach Kap. 2 bis 9 (Entscheidung vom 21.10.2026). Gründe:
- Der Block baut direkt auf dem Piloten und seinem Zahlenwerk auf.
- Er passt zum laufenden Praktikum MiNa.
- Dem User war die Diode als nächstes Thema angekündigt.

Ein Thema ist offen, solange seine kompakte Datei (ohne `-ausfuehrlich`) fehlt oder kein `stil: 3` hat. Die Numa-Themen stehen als Dateipfade im Themenplan (B1a):

```
cd /c/Users/info/PycharmProjects/pythonanimation && for f in $(find content/get1/1[0-2]-* -name '*.md' ! -name '*-ausfuehrlich.md' | sort) $(find content/get1 -name '*.md' ! -name '*-ausfuehrlich.md' ! -path 'content/get1/1[0-2]-*' | sort) $(find content/hoema3 -name '*.md' ! -name '*-ausfuehrlich.md' | sort) $(grep -o 'content/numa/[^ |`]*\.md' notizen/numa/themenplan.md 2>/dev/null); do [ -f "$f" ] && grep -q '^stil: 3' "$f" && continue; echo "$f"; break; done
```

- **Erstes hoema3-Thema:** dem User melden („ET1 in Stil 3 komplett, weiter mit HöMa3“), im Loop per PushNotification, und ohne Stopp weitermachen. Vorher den HöMa3-Volltext anlegen (B3).
- **Leere Ausgabe, `notizen/numa/themenplan.md` fehlt:** HöMa3 ist komplett. Melden („HöMa3 in Stil 3 komplett, weiter mit Numa“), im Loop per PushNotification. In diesem Durchgang das Modul Numa einrichten (B1a), committen und berichten; das erste Numa-Thema folgt im nächsten Durchgang.
- **Leere Ausgabe, Themenplan vorhanden:** ET1, HöMa3 und Numa sind komplett. Melden, im Loop ScheduleWakeup mit nur `stop: true`, und mit dem User abstimmen, wie es weitergeht (GEMB1, mmet, ET3, Schaltungstechnik 1). Lege **nicht** eigenmächtig weitere Module oder Themen an.

### (B1a) Modul Numa einrichten (einmalig, vom User am 22.10.2026 beauftragt)

1. **Entpacken:** `C:\Bücher\EtUndSo\3.Semester\(UE) Numerische Mathematik für Elektrotechnik (Großgruppenübung)_20261019_1452.zip` mit Pythons `zipfile` in einen neuen, leeren Ordner `C:\Bücher\EtUndSo\3.Semester\Numa\` entpacken. Nichts aus dem Archiv ausführen. Inhalt: `Vorlesungsfolien  Skript/Buch zur Vorlesung.pdf`, `Fortschritt der Vorlesung.html`, Foliensätze zu Kap. 2, 3, 4, 5, 6, 8 und 10, Übungsblätter 1 bis 8.
2. **Volltext:** `tools/dump_numa.py` nach dem Muster von `dump_get1.py`; Quelle ist das Buch, Ausgabe `C:\Bücher\EtUndSo\_volltext\numa_clean.txt` mit Markierungen „=== Seite N“.
3. **Themenplan:** aus dem Inhaltsverzeichnis des Buchs, abgeglichen mit dem Vorlesungsfortschritt und den Foliensätzen; ein Thema hat etwa den Umfang eines HöMa3-Themas. Festhalten in `notizen/numa/themenplan.md`, je Thema eine Tabellenzeile mit:
   - Dateipfad `content/numa/<nn>-<kapitel>/<nr>-<slug>.md`;
   - `title`, `pfad` (`Elektrotechnik / 3. Semester / Numerische Mathematik für Elektrotechnik / <Kapitel>`), `order` (Muster 35KKTT00), `tags`;
   - Buchseiten und zugehörige Folien.

   Die Artikeldateien entstehen erst beim jeweiligen Thema (B5). Weil es keinen alten Artikel gibt, kommen `title`, `pfad`, `order` und `tags` aus dem Themenplan.
4. **Prüfen:** Der B1-Befehl muss danach das erste Numa-Thema ausgeben.
5. **Commit** („Numa: Volltext und Themenplan“) und Bericht an den User mit dem Themenplan.

## (B2) Vorarbeit: Arbeitsnotiz und Zahlen (ERKLAER_PROMPT §10)

- **Arbeitsnotiz:** `notizen/<modul>/notiz_<slug>.md` mit allen zehn Punkten aus §10:
  - Ein-Satz-Prinzip;
  - Schwierigkeit und Längenspannen;
  - Vorwissen-Kette;
  - Fragenkatalog;
  - Kipp-Stellen;
  - Aussortier-Liste K/H/V/S mit Fassung;
  - Abbildungsplan;
  - Zahlenwerk;
  - Profi-Abgleich (ein bis zwei Fachquellen per WebSearch, mit Links);
  - Skript-Abgleich mit Seitenzahlen.
- **Zahlenwerk:** `notizen/<modul>/zahlen_<oberthema>.py`.
  - Beim ersten Thema eines Oberthemas anlegen, sonst weiterbenutzen und ergänzen.
  - Mit `python -I` ausführen, Ausgabe in `zahlen_<oberthema>.txt`.
  - Jede Zahl beider Fassungen stammt daraus.

## (B3) Quellen

**ET1:**
- **Skript:** `C:\Bücher\EtUndSo\1.Semester\ET1\(VO) Grundgebiete der Elektrotechnik 1 - Einführung in die Schaltungsanalyse_20261018_2239\Vorlesung\Begleit-Skript zur Vorlesung\GET1_Lecture_Script_WS2425_3_03.pdf`
- **Volltext:** `C:\Bücher\EtUndSo\_volltext\get1_clean.txt`. Mit `grep -a` durchsuchen; „=== Seite N“ ist die PDF-Seite. Fehlt die Datei: `python -I tools/dump_get1.py`.
- **Im PDF prüfen:** Abbildungen, Schaltbilder und Vorzeichen mit Read (pages).
- **Nur als Ideengeber:** `Übung\GGET1 Formelsammlung.pdf` und die KGÜ-Hilfsfolien. Keine Aufgaben kopieren.

**HöMa3:**
- **Skript:** `C:\Bücher\HöMa3\HM3_Skript_24_25.pdf`.
- **Volltext:** Beim ersten HöMa3-Thema `tools/dump_hoema3.py` nach dem Muster von `dump_get1.py` anlegen. Ausgabe nach `C:\Bücher\EtUndSo\_volltext\hoema3_clean.txt`, mit Markierungen „=== Seite N“.
- **Als Hilfe:** die eigenen Zusammenfassungen `C:\Bücher\HöMa3\Zusammenfassungen\HM3_Kap*.md` (Kap. 1 bis 4).
- **Nur als Ideengeber:** das Material in `C:\Bücher\EtUndSo\3.Semester\(VO) Höhere Mathematik 3_20261019_1451.zip`. Keine Aufgaben kopieren.
- **Zahlenwerk:** `notizen/hoema3/zahlen_<kapitel>.py`; Integrale, Flüsse, Koeffizienten und Wahrscheinlichkeiten der Beispiele werden dort berechnet.

**Numa** (nach B1a):
- **Buch:** `C:\Bücher\EtUndSo\3.Semester\Numa\Vorlesungsfolien  Skript\Buch zur Vorlesung.pdf`, Folien je Kapitel im selben Ordner.
- **Volltext:** `C:\Bücher\EtUndSo\_volltext\numa_clean.txt`.
- **Nur als Ideengeber:** die Übungsblätter 1 bis 8. Keine Aufgaben kopieren.
- **Zahlenwerk:** `notizen/numa/zahlen_<kapitel>.py`; die Verfahren werden dort tatsächlich ausgeführt (Fehlerverläufe, Konvergenzordnungen, Kondition), und jede Zahl der Artikel stammt daraus.

**GEMB1** (zurückgestellt, Entscheidung vom 22.10.2026):
- **Folien:** `C:\Bücher\GEMB\(VO) Grundlagen elektronischer Materialien und Bauelemente 1_20260831_1820\Vorlesungsfolien\Vorlesung 1.pdf` bis `Vorlesung 14.pdf`, dazu der Ordner „Vorlesungsfolien mit Anmerkungen“.
- **Volltext:** Beim ersten GEMB1-Thema `tools/dump_gemb1.py` nach dem Muster von `dump_get1.py` anlegen. Ausgabe nach `C:\Bücher\EtUndSo\_volltext\gemb1_clean.txt`, mit Markierungen „=== Vorlesung V Seite N“.
- **Nur als Ideengeber:** Frontal-, Kleingruppen- und Selbstrechenübungen. Keine Aufgaben kopieren.
- **Als Hilfe:** die eigenen Zusammenfassungen `C:\Bücher\GEMB\Zusammenfassungen\GEMB_Kap*.md`.

**Der bestehende Artikel** dient nur als Vollständigkeits-Check, nicht als Text- oder Strukturvorlage.

## (B4) Abbildungen planen (ERKLAER_PROMPT §7.5): nur Platzhalter und Liste

In den Artikeln stehen nur Editor-Abbildungen. Im Ablauf wird **keine** Abbildung gezeichnet: kein matplotlib, kein SVG, kein Editor-Feature.
1. **Szenen festlegen:** Für jede Abbildung des Abbildungsplans eine Szene-ID `<modul>/<kapitel>/<nr>-<name>` und eine Vorlage (Abbildungstyp) festlegen. In beiden Fassungen gilt dieselbe Szene-ID.
2. **Listeneintrag:** Die Szene in `ABBILDUNGEN_LISTE.md` eintragen, unter einer Überschrift für das Thema. Der Eintrag enthält:
   - Fassungen und Nummern;
   - Inhalt mit allen Zahlen, Wertebereichen, Achsen und Farben;
   - Kernaussage;
   - Datenquelle im Zahlenwerk;
   - benötigte Editor-Funktionen (§-Verweise auf `EDITOR_GRAFIK_FEATURES.md`);
   - gegebenenfalls die Animationsidee;
   - Status „offen“.
3. **Neue Funktionen:** Fehlt eine Funktion in `EDITOR_GRAFIK_FEATURES.md`, dort einen neuen Abschnitt mit „Gebraucht in“ anlegen.
4. **Platzhalter beim Schreiben (B5):** Im Artikel steht an der Stelle der Abbildung der Block aus ERKLAER_PROMPT §7.5, mit der Bildbeschreibung „**Abbildung n:** …“.

## (B5) Schreiben (leere Seite)

1. **Ausführliche Fassung zuerst:** `<nr>-<slug>-ausfuehrlich.md`.
   - **Frontmatter:** `title`, `pfad`, `order` und `tags` wie im alten Artikel. `summary` neu. Dazu `stil: 3` und `fassung: ausfuehrlich`.
2. **Dann die kompakte Fassung:** `<nr>-<slug>.md`. Sie ersetzt den alten Artikel.
   - **Neu geschrieben**, kein Zusammenschnitt (ERKLAER_PROMPT §3.1).
   - **Frontmatter** wie oben, mit `fassung: kompakt`.
3. **Lange Artikel in Teilen schreiben:**
   1. Den Anfang mit Write schreiben.
   2. Weiter mit Edit am Marker `<!-- FORTSETZUNG -->`; vor jedem Edit die Datei im aktuellen Kontext lesen.
   3. Am Ende den Marker entfernen.

## (B6) Selbstprüfung (vor dem Build)

1. **ERKLAER_PROMPT §11 für jede Fassung**, alle 18 Tests. Was ein Test findet, korrigierst du sofort.
2. **ARTIKEL_BAUPLAN §8 komplett:** Rechnungen, Vorzeichen und Zählpfeil-Richtungen nachrechnen; keine doppelt belegten Symbole.
3. **Kennzahlen:** `python -I tools/artikel_kennzahlen.py <beide md>`. Soll:
   - Hauptpfad in der Spanne der Notiz;
   - Abbildungs-Platzhalter `:::grafik` so viele wie im Abbildungsplan der jeweiligen Fassung, `<figure>`-Zeilen 0;
   - Quiz 10 bzw. 6;
   - jeden Treffer der Verbotsliste prüfen.
4. **Fließtext-Formeln:** `python -I tools/audit_inline.py <beide md>`, Ziel 0.
5. **Unabhängige Faktenprüfung (Pflicht):**
   - Ein zweiter Agent (general-purpose) prüft beide Fassungen gegen Zahlenwerk und Skriptseiten: Physik bzw. Mathematik, jede Zahl selbst nachgerechnet, Vorzeichen, Skriptkorrekturen auf Fairness, Herleitungen, Widersprüche zwischen den Fassungen.
   - Ausgabe: nur echte Probleme, „falsch“ getrennt von „ungenau“.
   - Jeden Befund selbst nachrechnen, bevor er eingearbeitet wird.
   - Beim Piloten fand diese Prüfung sechs echte Fehler.

## (B7) Bauen, technische Checks, Commit

**Bauen:** `PYTHONIOENCODING=utf-8 python build_wissen.py` muss grün sein.

**Vorschau-Server:** `http://127.0.0.1:8000`, zeigt den Ordner `web\`. Antwortet er nicht, im Hintergrund starten mit:

```
python -m http.server 8000 --directory /c/Users/info/PycharmProjects/pythonanimation/web
```

**Checks für beide Seiten:**
- `details class="quiz-item"` kommt 10- bzw. 6-mal vor.
- `class="bsp-card"` kommt genauso oft vor wie `class="bsp-ref"`, mindestens einmal.
- **KaTeX:** `python -I tools/katexcheck.py <html-name-ohne-.html>` meldet 0 Fehler.
- **Handy:** `python -I tools/widefind.py <url>`, `python -I tools/widefind_open.py <url>` (Herleitungen offen) und `python -I tools/widefind_bsp.py <url>` (Beispiel-Seite) geben nichts aus.
- **Geteilte Ansicht:** `python -I tools/splitalign.py <url> <png>` zeigt Karten ab 2 bei 350 und „Fehler: keine“.
- **Abbildungsliste vollständig:** Der folgende Befehl darf nichts ausgeben. Er meldet jede Szene eines Artikels, die in `ABBILDUNGEN_LISTE.md` fehlt.

  ```
  cd /c/Users/info/PycharmProjects/pythonanimation && grep -h '^Szene: ' <beide md> | sed 's/^Szene: \([^ ]*\).*/\1/' | sort -u | while read s; do grep -q "\*\*$s\*\*" ABBILDUNGEN_LISTE.md || echo "fehlt in Liste: $s"; done
  ```

- **Sichtprüfung:** Screenshot beider Fassungen hell und dunkel, ansehen.

**Protokoll:** Eine Zeile in `REVIEW_OPUS55.md` anhängen:

    - [x] <thema> — Stil 3 (kompakt N Wörter, ausführlich M Wörter); Prinzip: …; Kipp-Stellen: …; Fehlvorstellungen: …; Skriptkorrekturen: …; Abbildungen: a/b; Beispielkarten: c/d; Zahlen: notizen/<modul>/zahlen_<oberthema>.txt

**Committen** (kein Push):
- **Hinzufügen:**

  ```
  git add <beide md> notizen/<modul> web REVIEW_OPUS55.md ABBILDUNGEN_LISTE.md EDITOR_GRAFIK_FEATURES.md
  ```

  `build_wissen.py` und `tools/` nur dazunehmen, wenn sie geändert wurden.
- **Titel:** „ET1 Kap … <Thema> (Stil 3, zwei Fassungen)“ bzw. „GEMB1 Kap … (Stil 3, zwei Fassungen)“.
- **Nachricht** per Datei (`git commit -F`). Sie endet mit den Attributionszeilen, die die Sitzung vorgibt, derzeit `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## (B8) Bericht und nächster Durchgang

1. **Bericht an den User**, kurz und auf Deutsch:
   - Ein-Satz-Prinzip;
   - Kipp-Stellen und wie sie erklärt sind;
   - aufgelöste Fehlvorstellungen;
   - Skriptkorrekturen;
   - Profi-Quellen als Links;
   - Wörter und Lesezeit beider Fassungen;
   - Zahl der Abbildungen und Beispiele;
   - Ergebnis der Checks.
2. **Weiter:**
   - **Im Chat:** auf „weiter“ warten.
   - **Im Loop:** mit ScheduleWakeup (~60 s, `noop: false`) und genau dem Aufruf von oben neu armen. Ausnahmen sind die Pilot-Sperre (B0) und das Ende (B1).

## Technische Hinweise

- **Arbeitsverzeichnis:** Das Shell-cwd springt nach jedem Bash-Aufruf auf `C:\Bücher` zurück. Stell deshalb immer `cd /c/Users/info/PycharmProjects/pythonanimation` voran.
- **Keine Heredocs für LaTeX oder Markdown mit Backslashes:** Doppelte Backslashes gehen dabei verloren. Nimm Edit/Write oder per Write angelegte Python-Skripte.
- **Kodierung:** `python -I` ignoriert PYTHONIOENCODING; eigene Skripte setzen deshalb `sys.stdout.reconfigure(encoding="utf-8")`.
- **Werkzeuge:** Die Prüfwerkzeuge liegen in `tools/` im Repo. Der Skript-Volltext liegt außerhalb des Repos in `C:\Bücher\EtUndSo\_volltext\`.
