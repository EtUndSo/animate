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
7. **Behauptungen belegen:** Was sich in wenigen Zeilen begründen lässt (Eindeutigkeit, Äquivalenzen, „A ⇒ B",
   Rechenregeln), bekommt eine `:::herleitung` — nicht nur „es gilt" hinschreiben.
8. **Konkret machen:** Abstrakte Aussagen an echten Zahlen zeigen (z. B. eine Jacobi-Matrix an zwei konkreten
   Punkten auswerten und deuten). Aussagen der Art „gilt nicht immer" mit einem konkreten **Gegenbeispiel** samt
   Rechnung belegen.
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
  einzelne Symbole und Objektnamen ($x$, $\nabla f$, $\hat e_r$, $\mathbb{R}^n$) und kurze Parameterangaben
  ($m=1$, $k\ge2$, $|v|=1$). Jede Gleichung oder Ungleichung, die einen **Zusammenhang** aussagt, und jede
  Funktionsvorschrift in Beispielen gehört auf eine eigene Zeile. In `:::kern`-Bullets ist höchstens eine kurze
  Formel pro Bullet erlaubt.
- **Nur die wichtigsten** Formeln kommen in eine **Box**:
  `:::formel <Typ>` … `:::` — `<Typ>` ist das Label oben links: **Definition**, **Satz**, **Lemma**,
  **Gesetz**, **Formel** (Default, wenn nichts angegeben). Die Box wird **automatisch nummeriert** (fortlaufend
  pro Artikel, oben rechts `(1)`, `(2)`, …) → im Text referenzierbar („nach Formel (2)").
- **Jede Formel erklären**: Eingabe → Ausgabe mit **Typen** und jedes Symbol. Beispiel Kurve
  $\gamma:[a,b]\to\mathbb{R}^n$: Eingabe = **Skalar** $t$, Ausgabe = **Vektor** (Ortskoordinaten); Pfeil $\to$
  nennt die **Räume**, $\mapsto$ die **Zuordnung**. Bei Skalarprodukt-Integranden: „zwei Vektoren → eine Zahl".
- **Herleitung IMMER als ausklappbare Box an der Formel**: `:::herleitung` … `:::` → eingeklappt. Sichtbar
  bleiben Konzept + Ergebnis-Formel; die formale Herleitung ist aufklappbar. In `:::herleitung` nur
  `$$…$$`/Listen/Text, **keine** verschachtelten `:::`-Blöcke (sonst bricht der Parser).

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
5. weitere `##`-Abschnitte je Thema; **Zahlenbeispiele** mit echten Zahlen (Rechnungen auf eigener Zeile).
6. `## Physikalische Bedeutung und Ausblick` — Anwendung + Vorgriff auf den nächsten Artikel.

Zum Schluss:
- `:::kern` — „Das Wichtigste" als **Stichpunkt-Liste** (`- …`).
- `:::quiz` — **genau 10** F:/A:-Paare (je eine Zeile), verständnisorientiert (Herleitung + Bedeutung),
  **nur Inhalte, die im Artikel vorkommen**.

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
- `__begriff__` = blau (definierter Begriff), `**wort**` = orange (wichtig), `*wort*` = kursiv,
  `**Schritt N**` = rot. Tabellen als GitHub-Pipes.

## 6. Workflow (Loop)
- Repo `C:\Users\info\PycharmProjects\pythonanimation`, Artikel in `content/<modul>/…`.
  Reihenfolge: **HöMa3 komplett zuerst**, dann `mmet`, `gemb1`, `get1`.
- „Noch nicht überarbeitet" = Quelldatei enthält `:::konzept`. Nächster offener Artikel = **erster** HöMa3-Artikel
  mit `:::konzept` (in `find … | sort`-Reihenfolge).
- **Jeden Artikel von Grund auf NEU schreiben (leere Seite).** Die Struktur ist nach diesem Bauplan ohnehin
  komplett anders — nicht die alten Artikel umbauen. Inhaltsquelle ist das **Skript** (HöMa3:
  `C:\Bücher\HöMa3\HM3_Skript_24_25.pdf`, passende Seiten/Kapitel) plus der ET4-Ordner als Stilvorbild. Der
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
Stichpunkte, Nachbar-Spalten am Ende (vorheriger | nächster Artikel mit Themen-Stichpunkten), linke Baumspalte
beim Öffnen **eingeklappt** (Textblock bleibt an gleicher Position), Panel-Buttons **mittig** in der oberen
Leiste, Formel-Boxen mit Typ-Label + Nummer.

## 8. Review-Checkliste
Gilt für jeden Artikel — beim Neuschreiben vor dem Commit, beim Überarbeiten (Phase A, `REVIEW_OPUS55.md`) als
Prüfliste:
1. **Korrektheit:** Rechnungen nachrechnen; Vorzeichen; Voraussetzungen der Sätze vollständig genannt.
2. **Vollständigkeit:** alle Definitionen, Sätze, Formeln und Beispiele des Skript-Abschnitts enthalten.
3. **Von Grund auf:** jeder Begriff, jedes Symbol, jede Dimension vor der ersten Benutzung eingeführt; kein Symbol
   doppelt belegt; Fachbegriffe bei Erstnennung erklärt.
4. **Formeln:** keine Gleichungen oder Formelketten im Fließtext (auch nicht in Herleitungen); jede wichtige Formel
   erklärt (Eingabe → Ausgabe, Symbole); Boxen nur für die wichtigsten, mit passendem Typ-Label.
5. **Herleitungen:** jede Aussage, die sich kurz begründen lässt, hat eine `:::herleitung`; Herleitungen erklären
   jeden Schritt.
6. **Konkret:** mindestens ein Zahlenbeispiel; „gilt nicht immer"-Aussagen mit konkretem Gegenbeispiel.
7. **Lesbarkeit:** Der Anschaulich-Einstieg trägt das Konzept; kurze Absätze (ein Gedanke); Abschnitte sinnvoll
   geschnitten.
8. **`:::kern`:** kurze Bullets, ein Gedanke und höchstens eine Formel pro Bullet.
9. **`:::quiz`:** genau 10; jede Frage und Antwort vollständig durch den Artikeltext gedeckt.
10. **`:::grafik`:** Szene-Zeile, präzise Beschreibung der Animation, Farblogik; Grafiken überall dort, wo ein Bild
    das Verständnis trägt.
