# EtUndSo — Artikel-Bauplan (verbindlich für den Rewrite-Loop)

Diese Datei ist die **Referenz** für das Neuschreiben der Wissens-Artikel. Vor jedem Artikel im Loop konsultieren.
Stand 2026-10-20. Stil-Vorbild: `C:\Bücher\ET4_Skript_Erklaerung\` (v. a. `ET4_Kap1_Mathe-Grundlagen_Zusammenfassung.md`).

## 0. Nordstern
- EtUndSo erklärt das, was im Vorlesungs-Skript **fehlt**. Die Leute haben das Skript; sie kommen nur, wenn sie
  etwas **nicht verstanden** haben. Eine Nacherzählung des Skripts ist wertlos.
- Erfolg = „Wer an dieser Stelle hängengeblieben ist, versteht es danach wirklich."
- Die Skript-Themen sind Pflicht-**Landmarken**; der eigentliche Inhalt ist die tiefe Erklärung dazwischen.
  Eigene Vorbausteine (fehlende Grundlagen) ergänzen, damit der Komplex **chronologisch von Grund auf** steht
  (z. B. „Was ist eine Kurve?" bevor $\dot\gamma$ benutzt wird).

## 1. Didaktik (wie erklärt wird)
1. **Erst anschaulich/einfach** (konkretes Alltagsbild), **dann** mathematisch/physikalisch tief.
2. **Jeden Schritt erklären**, so viel wie möglich **herleiten**.
3. Jeden **Fachbegriff** bei Erstnennung sofort erklären.
4. Immer das **WARUM** / den konkreten Mechanismus; nie nur behaupten.
5. **Exakt**: Räume/Definitionsbereiche und Voraussetzungen jeder Aussage nennen.
6. **Kürzere Absätze** — ein Gedanke pro Absatz, Leerzeile dazwischen.
7. **Alles herleiten, was keine Definition ist** (User 2026-10-20: „Es gibt noch viel zu wenige Herleitungen. Die
   Produktregeln mit einem Skalarfeld wurden z. B. überhaupt nicht hergeleitet. Steht einfach so dort"): Jede
   Formel, Rechenregel, Identität, Abschätzung, jeder Satz und jeder Spezialfall, der keine reine Definition ist,
   bekommt eine `:::herleitung` — gerade auch „einfache" Regeln wie Produktregeln. Nie „es gilt …" ohne Begründung.
   Nur wenn ein Beweis klar über den Kursrahmen hinausgeht (z. B. Lebesgue-Theorie), sagt man das ausdrücklich und
   skizziert in der Box wenigstens die Beweisidee. Lieber eine Herleitung zu viel als eine zu wenig — sie ist
   eingeklappt und stört den Lesefluss nicht.
8. **Konkret machen:** Abstrakte Aussagen an echten Zahlen zeigen (z. B. eine Jacobi-Matrix an zwei konkreten
   Punkten auswerten und deuten). Aussagen der Art „gilt nicht immer" mit einem konkreten **Gegenbeispiel** samt
   Rechnung belegen. Diese Beispiele stehen auf der **Beispiel-Seite** (§3a), nicht im Fließtext.
9. **Keine undefinierten Symbole:** Jedes Symbol und jede Dimension (z. B. $p$ in $\mathbb{R}^p$) vor der ersten
   Benutzung einführen; kein Symbol doppelt belegen (z. B. $h$ nicht zugleich als Schritt und als Funktion).
10. **Anschauung und Mathematik fusionieren** (User 2026-10-20): Die anschauliche Sicht ist kein Vorspann, der
    danach in trockene Mathematik übergeht. Sie läuft als roter Faden durch den ganzen Artikel: Jede Definition,
    jede Formel und jeder Herleitungsschritt bekommt **an Ort und Stelle** seine Bedeutung im Bild („Im Bild: …"
    oder direkt in den Satz verwoben) — was bedeutet dieses Symbol, dieser Term, dieser Schritt in der Landschaft,
    am Gitter, an der Strömung? Ein **durchgehendes Leitbild** (z. B. Gebirgslandschaft + Wanderer) aus dem
    Anschaulich-Abschnitt wird in allen folgenden Abschnitten konsequent weiterverwendet, statt in jedem Abschnitt
    ein neues Bild zu erfinden. Lieber noch etwas anschaulicher als zu knapp.

## 2. Formeln
- **Jede Formel steht auf einer eigenen Zeile** (`$$…$$`). Nie eine stehende Formel inline im Fließtext, erst
  recht keine Formel-**Ketten** im Text — das gilt auch für den Text in `:::herleitung`. Inline erlaubt sind nur
  einzelne Symbole und Objektnamen ($\vec x$, $\nabla f$, $\vec e_r$, $\mathbb{R}^n$) und kurze Parameterangaben
  ($m=1$, $k\ge2$, $|\vec v|=1$). Jede Gleichung oder Ungleichung, die einen **Zusammenhang** aussagt, und jede
  Funktionsvorschrift in Beispielen gehört auf eine eigene Zeile. In `:::kern`-Bullets ist höchstens eine kurze
  Formel pro Bullet erlaubt.
- **Teilmengen immer mit Grundraum** (User 2026-10-20): $U\subseteq\mathbb{R}^n$ bzw. $U\subseteq\mathbb{R}^3$,
  $D\subseteq\mathbb{R}^2$ usw. Symbol stets $\subseteq$ (Teilmenge, Gleichheit erlaubt) — nicht $\subset$, das als
  echte Teilmenge gelesen werden kann. Keine Menge ($U$, $V$, $G$, $D$, $M$, $Q$ …) benutzen, ohne sie im Artikel
  beim ersten Auftreten mit ihrem Grundraum einzuführen.
- **Pfeil-Notation wie in ET4** (User 2026-10-20): Jede **vektorielle** Größe trägt einen Pfeil — Punkte und
  Ortsvektoren ($\vec x$, $\vec x_0$), Vektorfelder und vektorwertige Abbildungen ($\vec E$, $\vec F$, $\vec A$,
  $\vec B$, $\vec f$, $\vec g$), Kurven und Tangenten ($\vec\gamma$, $\dot{\vec\gamma}$), Einheitsvektoren ($\vec e_k$,
  $\vec e_r$, Laufrichtung $\vec v$), vektorielle Schritte ($\vec h$), das Wegelement ($d\vec x$), Normalen ($\vec n$)
  und der Nullvektor ($\vec 0$, z. B. $\mathbb{R}^3\setminus\{\vec 0\}$). **Ohne** Pfeil: Skalare und Komponenten
  ($x_j$, $E_j$, $f_j$), der Gradient $\nabla f$ bzw. $\operatorname{grad} f$ und der Operator $\nabla$, Matrizen
  ($D\vec f$), benannte Punkte ($P$, $A$, $B$) und skalare Koordinaten in Beispielen ($f(x,y)$).
- **Groß- und Kleinschreibung** (User 2026-10-20): **Vektorfelder** und vektorwertige Abbildungen immer mit
  **Großbuchstaben** ($\vec E$, $\vec F$, $\vec G$; Komponenten $F_j$); **Skalarfelder**, Skalare und einzelne
  **Vektoren** (Punkte $\vec x$, Richtungen $\vec v$, Einheitsvektoren $\vec e_k$, $\vec e_r$, Kurven $\vec\gamma$)
  mit **Kleinbuchstaben** ($f$, $u$, $\phi$, $\varphi$). Zusammen mit der Pfeil-Notation ergibt das ein eindeutiges
  Lesesystem: Großbuchstabe mit Pfeil = Vektorfeld, Kleinbuchstabe mit Pfeil = Vektor, Kleinbuchstabe ohne Pfeil =
  Skalar/Skalarfeld, Großbuchstabe ohne Pfeil = Menge oder Matrix ($U$, $D$, $A$). Ausnahmen nur für fest etablierte
  Namen: Konstanten wie Ladung $Q$, Radius $R$; spezielle Funktionen/Transformationen wie $\Gamma$, $\mathcal L f$.
  Skalare Ergebnisfunktionen (Parameterintegrale, Stammfunktionen, Profile) deshalb klein benennen, z. B.
  $g(x)=\int_a^b f(x,t)\,dt$.
- **Elektrotechnik (ET1 und folgende, 2026-10-20):** Formelzeichen wie im Skript bzw. nach DIN 1304 und DIN 5483 —
  Gleich- und Effektivgrößen groß ($U$, $I$, $R$, $C$, $L$, $P$, $W$, $Q$), zeitabhängige Momentanwerte klein
  ($u(t)$, $i(t)$), vektorielle Feldgrößen mit Pfeil ($\vec E$, $\vec F$, $\vec D$, $\vec J$). Diese Großbuchstaben-Skalare
  sind etablierte Namen und fallen unter die Ausnahme oben; Einheiten stets mitführen.
- **Nur die wichtigsten** Formeln kommen in eine **Box**:
  `:::formel <Typ>` … `:::` — `<Typ>` ist das Label oben links: **Definition**, **Satz**, **Lemma**,
  **Gesetz**, **Formel** (Default, wenn nichts angegeben). Die Box wird **automatisch nummeriert** (fortlaufend
  pro Artikel, oben rechts `(1)`, `(2)`, …) → im Text referenzierbar („nach Formel (2)").
- **Jede Formel erklären**: Eingabe → Ausgabe mit **Typen** und jedes Symbol. Beispiel Kurve
  $\vec\gamma:[a,b]\to\mathbb{R}^n$: Eingabe = **Skalar** $t$, Ausgabe = **Vektor** (Ortskoordinaten); Pfeil $\to$
  nennt die **Räume**, $\mapsto$ die **Zuordnung**. Bei Skalarprodukt-Integranden: „zwei Vektoren → eine Zahl".
- **Herleitung IMMER als ausklappbare Box an der Formel**: `:::herleitung` … `:::` → eingeklappt. Sichtbar
  bleiben Konzept + Ergebnis-Formel; die formale Herleitung ist aufklappbar. In `:::herleitung` nur
  `$$…$$`/Listen/Text, **keine** verschachtelten `:::`-Blöcke (sonst bricht der Parser).
- **Mehrteilige Formelzeilen** mit `\qquad` trennen (z. B. `$$a=1, \qquad b=2.$$`): Der Build bricht die Teile in
  schmalen Spalten (geteilte Ansicht, Handy) automatisch untereinander um; zu breite Formeln werden passend
  verkleinert. Lange Gleichungs**ketten** (mehr als etwa drei Glieder) lieber auf mehrere Zeilen verteilen.

## 3. Artikel-Aufbau
**Frontmatter** (unverändert lassen, nur `summary` ggf. anpassen): `title`, `pfad`, `order`, `summary`
(für Karten/Suche), `tags`.

**KEIN** `:::konzept`, **kein** „Worum es geht", **kein** einleitender Absatz — der Artikel startet automatisch
mit dem **Inhaltsverzeichnis** (wird aus den `##`-Überschriften erzeugt).

Dann die `##`-Abschnitte (jeder wird als **Karte** gerendert). Typischer Bogen (ET4):
1. `## Anschaulich` — Alltagsbild, Konzept im Bild, 1–2 intuitive Konsequenzen. Das hier eingeführte
   **Leitbild** wird in allen folgenden Abschnitten weiterverwendet und mit jeder Formel verknüpft (§1 Nr. 10).
2. `## Was ist …?` / fehlende Grundlage — nötige Vorbausteine von Grund auf.
3. `## <Herleitung/Kernbegriff>` — **„Die zwei (o. mehr) Akteure:"** (jedes Objekt mit Raum definieren) →
   **„Das Zusammenspiel:"** + *kursive* Leitfrage → Ergebnis als `:::formel` → `:::herleitung`.
4. `## Warum die … Eigenschaften folgen` — intuitive Aussagen aus der Kernformel ableiten.
5. weitere `##`-Abschnitte je Thema; **Zahlenbeispiele** mit echten Zahlen als `::::beispiel`-Blöcke (§3a).
6. `## Physikalische Bedeutung und Ausblick` — Anwendung + Vorgriff auf den nächsten Artikel.

Zum Schluss:
- `:::kern` — „Das Wichtigste" als **Stichpunkt-Liste** (`- …`).
- `:::quiz` — **genau 10** F:/A:-Paare (je eine Zeile), verständnisorientiert (Herleitung + Bedeutung),
  **nur Inhalte, die im Artikel vorkommen**. Im Quelltext steht es am Ende; der Build setzt es auf der Seite ganz
  nach unten, unter die Nachbar-Spalten (User 2026-10-21).

## 3a. Beispiel-Seite: Theorie links, Praxis rechts (User 2026-10-20)
- **Ansicht:** Der dritte Button oben in der Leiste öffnet die **geteilte Ansicht**. Der Artikel (Theorie) rückt nach
  links, rechts öffnet sich in gleicher Breite die **Beispiel-Seite** (Praxis). Beide Spalten laufen synchron: Jedes
  Beispiel steht auf Höhe der Formel, zu der es gehört. Ohne geteilte Ansicht steht im Artikel an der Stelle nur ein
  Verweis „Beispiel k →“ (auf dem Handy öffnet er die Beispiel-Seite als Ebene über dem Artikel).
- **Trennung:** Im Artikel bleiben Definitionen, Sätze, Herleitungen, „Im Bild"-Deutungen, das Leitbild, `:::kern`
  und `:::quiz`. **Alles Durchgerechnete** wandert auf die Beispiel-Seite: Zahlenbeispiele, Beispielrechnungen,
  konkrete Funktionen und Felder, Zahlenproben, Gegenbeispiele samt Rechnung. Im Artikel bleibt dann die
  allgemeine Aussage mit ihrer Deutung stehen (z. B. „partielle Ableitungen allein reichen nicht — im Bild: …"),
  das konkrete Gegenbeispiel steht rechts. Nur wo ein Beispiel untrennbar zur Theorie gehört (etwa eine Rechnung
  im Leitbild des Anschaulich-Abschnitts), bleibt es im Text.
- **Zu jeder wichtigen Formel ein Beispiel:** Jede `:::formel`-Box und jede Rechenregel, Identität oder Abschätzung
  bekommt mindestens ein durchgerechnetes Beispiel. Wo das Skript keines hat, eines konstruieren — einfach, mit
  echten Zahlen, im Leitbild gedeutet. Lieber mehrere kurze Beispiele als ein langes. Wiederkehrende Beispielobjekte
  (z. B. das „Quadrieren" in Kap 1.1) machen die Beispiel-Seite zu einer durchgehenden Geschichte.
- **Syntax:** `::::beispiel <Titel>` … `::::` (vier Doppelpunkte) **direkt hinter** die Formel oder Aussage, die es
  zeigt — die Beispielkarte richtet sich am Block unmittelbar davor aus. Darin erlaubt: Text, `$$`-Formeln, Listen,
  Tabellen, `:::herleitung` und `:::grafik` (drei Doppelpunkte). Nicht erlaubt: `:::formel`-Boxen (Nummerierung),
  `##`-Überschriften, verschachtelte Beispiele. Nie zwei Beispiel-Blöcke direkt hintereinander — lieber eines mit
  Teilen **(a)**, **(b)**. Die Nummern vergibt der Build; im Text nie „Beispiel 3" schreiben, sondern über den Inhalt
  verweisen („wie beim Quadrieren").
- **Jedes Beispiel ist selbsttragend:** Es nennt die verwendete Funktion bzw. das Feld mit Räumen (auf eigener Zeile),
  rechnet jeden Schritt auf eigener Zeile, deutet das Ergebnis „Im Bild" und hält alle Regeln aus §1–§2 ein (Pfeile,
  Groß/Klein, keine Gleichungen im Fließtext, nicht-triviale Behauptungen mit `:::herleitung`).
- Zu einem Beispiel gehörende Grafiken stehen als `:::grafik` **im** Beispiel-Block. `:::quiz` darf Beispiele
  abfragen — die Beispiel-Seite gehört zum Artikel.

## 4. Grafiken (später im Editor, animiert — NICHT im Loop erzeugen)
- An jeder wichtigen Stelle ein `:::grafik`-Block. Diese Blöcke sind die **gespeicherte Liste** der zu
  erzeugenden Animationen (der Editor realisiert sie später, interaktiv unter Aufsicht des Users).
- **Erste Zeile** jedes `:::grafik`-Blocks: `Szene: <modul>/<kapitel>/<artikel-nr>-<slug> · Vorlage: <template>`
  (eindeutiger Verweis Figur ↔ Editor-Szene).
- Danach: **präzise Beschreibung** der Animation — was gezeigt wird, welche Bewegung/Interaktion, Beschriftung.
- **Farblogik** (wie im Text): **rot** = definiertes Objekt, **blau** = Feld/Kontext, **orange** = Mechanismus,
  **grau** = Achsen/Nebensache, **gestrichelt** = Hilfs-/virtuelle Linie.
- Mit **Kernaussage** als Bildunterschrift-Satz.

## 5. Block-Syntax (vom Build unterstützt)
- `## Überschrift` → Abschnitts-Karte (+ Eintrag im Inhaltsverzeichnis).
- `:::formel <Typ>` / `:::herleitung` / `:::grafik` / `:::kern` / `:::quiz` (+ `:::merke` / `:::satz` /
  `:::definition` / `:::lemma`).
- `::::beispiel <Titel>` … `::::` → Karte auf der Beispiel-Seite + Verweis im Artikel (§3a); darf `:::herleitung`
  und `:::grafik` enthalten.
- `__begriff__` = blau (definierter Begriff), `**wort**` = orange (wichtig), `*wort*` = kursiv,
  `**Schritt N**` = rot. Tabellen als GitHub-Pipes.

## 6. Workflow (Loop)
- Repo `C:\Users\info\PycharmProjects\pythonanimation`, Artikel in `content/<modul>/…`.
  Reihenfolge: HöMa3 Kap 1–5 sind fertig; **jetzt `get1` (ET1)** (User 2026-10-20: „Erstmal genug Mathe"), **danach
  ohne Rückfrage `gemb1`** (User 2026-10-21: „Beende alle Artikel für ET1. Mach danach mit Gemb1 weiter"); HöMa3
  Kap 6–8 und `mmet` erst danach nach Absprache.
- „Noch nicht überarbeitet" = Quelldatei enthält `:::konzept`. Nächster offener Artikel = **erster** Artikel des
  aktuellen Moduls mit `:::konzept` (in `find … | sort`-Reihenfolge).
- **Jeden Artikel von Grund auf NEU schreiben (leere Seite).** Die Struktur ist nach diesem Bauplan ohnehin
  komplett anders — nicht die alten Artikel umbauen. Inhaltsquelle ist das **Skript** (HöMa3:
  `C:\Bücher\HöMa3\HM3_Skript_24_25.pdf`; GET1: `C:\Bücher\EtUndSo\1.Semester\ET1\(VO) Grundgebiete der
  Elektrotechnik 1 - Einführung in die Schaltungsanalyse_20261018_2239\Vorlesung\Begleit-Skript zur
  Vorlesung\GET1_Lecture_Script_WS2425_3_03.pdf`; GEMB1: `C:\Bücher\GEMB\(VO) Grundlagen elektronischer Materialien und
  Bauelemente 1_20260831_1820\Vorlesungsfolien\Vorlesung 1.pdf` bis `Vorlesung 14.pdf`, dazu der Ordner „Vorlesungsfolien
  mit Anmerkungen", Übungen nur als Ideengeber; passende Seiten/Kapitel) plus der ET4-Ordner als Stilvorbild. Der
  bestehende Artikel dient **höchstens** als schneller Vollständigkeits-Check (welche Themen/Formeln vorkommen),
  **nicht** als Struktur- oder Textvorlage. Alle wichtigen Inhalte/Formeln der Skript-Quelle müssen enthalten sein.
- **Pro Tick genau ein Artikel**: auswählen → komplett neu im Bauplan-Stil schreiben →
  `PYTHONIOENCODING=utf-8 python build_wissen.py` (muss grün sein, „✓ … Artikel") →
  grep-Check `grep -o 'details class="quiz-item"' <html> | wc -l` == 10 → **committen**
  (KEIN Push; Attribution `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` +
  `Claude-Session: https://claude.ai/code/session_011k5g5E9cexRssEPuRKzSTZ`).
- **Editor/Animationen laufen NICHT im Loop** (hohe Fehlerrate, baut aufeinander auf) — separat, wenn der User
  aktiv mitschauen kann.

## 7. Layout/Technik (global, bereits in build_wissen.py umgesetzt)
Inhaltsverzeichnis-Start (Marker = Pfeil →), Abschnitts-Karten, größere Formeln (auch mobil), `:::kern` als
Stichpunkte, Nachbar-Spalten am Ende (vorheriger | nächster Artikel mit Themen-Stichpunkten) und **darunter ganz unten
das Quiz** (User 2026-10-21: erst sieht man, wie es weitergeht, dann das Quiz), linke Baumspalte
beim Öffnen **eingeklappt** (Textblock bleibt an gleicher Position), Panel-Buttons **mittig** in der oberen
Leiste, Formel-Boxen mit Typ-Label + Nummer. Dritter Panel-Button = geteilte Ansicht mit Beispiel-Seite (§3a;
Zustand wird gemerkt, `?bsp=1` in der URL öffnet sie direkt); mehrteilige Formelzeilen brechen um, zu breite Formeln
werden eingepasst; Mathe wird HTML-maskiert (`<` in Formeln ist sicher). Seit 2026-10-21 (User): Logo „EtUndSo“ mit
Et rot, Und blau, So orange (`--accent3`), auch auf Startseite, Impressum und Datenschutz; Suchknopf und Suchfelder ohne
Lupen-Symbol, auf dem Handy mit dem Wort „Suchen“ (Editor-Link unter 380 px ausgeblendet, bis 320 px geprüft);
`web/version.json` für „Letztes Update“ auf der Startseite schreibt der Build mit dem Datum der jüngsten Änderung an
Artikeln, Build oder `web/`-Dateien.

## 8. Review-Checkliste
Gilt für jeden Artikel — beim Neuschreiben vor dem Commit, beim Überarbeiten (Phase A, `REVIEW_OPUS55.md`) als
Prüfliste:
1. **Korrektheit:** Rechnungen nachrechnen; Vorzeichen; Voraussetzungen der Sätze vollständig genannt.
2. **Vollständigkeit:** alle Definitionen, Sätze, Formeln und Beispiele des Skript-Abschnitts enthalten.
3. **Von Grund auf:** jeder Begriff, jedes Symbol, jede Dimension vor der ersten Benutzung eingeführt; kein Symbol
   doppelt belegt; Fachbegriffe bei Erstnennung erklärt; jede Menge mit Grundraum eingeführt ($U\subseteq\mathbb{R}^n$).
4. **Formeln:** keine Gleichungen oder Formelketten im Fließtext (auch nicht in Herleitungen); jede wichtige Formel
   erklärt (Eingabe → Ausgabe, Symbole); Boxen nur für die wichtigsten, mit passendem Typ-Label; Pfeil-Notation
   (jede vektorielle Größe mit Pfeil, §2) — auch in `:::kern`, `:::quiz` und `:::grafik`.
5. **Herleitungen:** JEDE nicht-definitorische Formel/Regel/Identität/Abschätzung hat eine `:::herleitung` (§1 Nr. 7)
   — beim Review jede Formel einzeln durchgehen und fragen „Ist das eine Definition? Wenn nein: Wo ist die
   Herleitung?"; Herleitungen erklären jeden Schritt und deuten ihn im Bild.
6. **Konkret:** mindestens ein Zahlenbeispiel; „gilt nicht immer"-Aussagen mit konkretem Gegenbeispiel.
7. **Lesbarkeit:** Der Anschaulich-Einstieg trägt das Konzept; kurze Absätze (ein Gedanke); Abschnitte sinnvoll
   geschnitten.
8. **`:::kern`:** kurze Bullets, ein Gedanke und höchstens eine Formel pro Bullet.
9. **`:::quiz`:** genau 10; jede Frage und Antwort vollständig durch den Artikeltext gedeckt.
10. **`:::grafik`:** Szene-Zeile, präzise Beschreibung der Animation, Farblogik; Grafiken überall dort, wo ein Bild
    das Verständnis trägt.
11. **Beispiel-Seite (§3a):** Nichts Durchgerechnetes mehr im Fließtext; jede wichtige Formel hat ein
    `::::beispiel` direkt dahinter; keine zwei Beispiele direkt hintereinander; Beispiele selbsttragend und im
    Leitbild gedeutet; Build zeigt so viele Beispielkarten wie Verweise.
