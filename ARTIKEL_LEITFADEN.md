# Artikel-Leitfaden — verbindliche Regeln für EtUndSo-Wissensartikel

Dies ist die **einzige Quelle der Wahrheit** für das Erstellen/Überarbeiten von Wissensartikeln. Vor jedem
Artikel kurz durchgehen. (Entstanden aus dem laufenden Feedback; wird bei neuen Vorgaben hier ergänzt.)

---

## 0. Oberstes Prinzip
**Es sind echte ERKLÄRUNGEN, keine Zusammenfassungen.** Geschrieben für jemanden, der vom Thema **noch nie**
etwas gehört hat. **Korrektheit zuerst**, dann Tiefe, dann alles andere. **Zeit spielt keine Rolle** — ein
Artikel darf Minuten bis Stunden dauern. **Keine Parallelität** — strikt ein Artikel nach dem anderen, volle
Konzentration. **Keine fremden Beispiel-/Klausuraufgaben 1:1 übernehmen** (eigene erfinden); Standard-Darstellungen
von Allgemeinwissen (Schaltungen, Graphen) sind dagegen frei nachbildbar — Details in §11.

**Keine Quellen- und Veranstaltungsbezüge (User-Vorgabe 2026-10-22):** Auf der Website steht nirgends Skript,
Vorlesung, Übung, Praktikum oder eine Seiten-, Bild-, Tabellen- oder Kapitelnummer einer Vorlage; die Leserinnen und
Leser kennen sie nicht. Fehler der Vorlage werden stillschweigend korrigiert (ERKLAER_PROMPT §5.7). Die folgenden
Regeln zur Vorlage gelten nur für die Arbeit im Hintergrund.

**Vollständigkeit gegenüber der Quelle (User-Vorgabe 2026-10-19):** Jeder Artikel muss **alle wichtigen
Inhalte und Formeln** des zugehörigen Quell-Kapitels (Vorlesung/Skript) enthalten — wer den Artikel liest, darf
nichts Wesentliches verpassen, das in der Quelle steht. Lange Fließtexte dürfen (und sollen) zusammengefasst
werden, aber **keine wichtige Formel, Größe, Definition, Herleitung oder Kernaussage weglassen**. Bei jedem
Erstellen **und** jeder Angleichung: Quell-Kapitel gegen den Artikel abgleichen (am besten anhand der
Lernziel-/Inhalts-Folien), fehlende wichtige Punkte ergänzen. Maßstab „wichtig": Lernziele, benannte Formeln/
Sätze, zentrale Begriffe, typische Prüfungsinhalte. (Reine Beispiel-Zahlen/Aufgaben nicht kopieren → §11.)

---

## 1. Didaktik (das Wichtigste)
- **Von Null motivieren:** Erst das Problem/die Frage, dann die Lösung. Warum braucht man das überhaupt?
- **Alles herleiten:** Formeln nicht nur hinschreiben, sondern beweisen/herleiten (z. B. über Reihen, Pythagoras,
  Trigonometrie, Schritt-für-Schritt). Keine „vom Himmel gefallenen" Formeln.
- **Das WARUM zeigen** — die Ursache, den Mechanismus. Nie nur „wie es ist".
- **„Warum nicht die naheliegenden Alternativen?"** Wo sinnvoll: den scheinbar nächstliegenden anderen Weg zeigen
  und *warum er scheitert/umständlicher ist* (schafft Vertrauen). Muss nicht in jeden Artikel, aber wo es passt.
- **Zweite Sichtweise** an wichtigen Stellen (anderer Blick auf dasselbe, Analogie — als Analogie kennzeichnen).
- **Stolpersteine** benennen (typische Fehler/Missverständnisse) und auflösen.
- **Jeden Fachbegriff bei ERSTER Nennung** sofort inline erklären.
- **Vorlage = ET4-Skript-Stil** (`C:\Bücher\ET4_Skript_Erklaerung`): „Worum es geht" → anschaulich → Größen/
  „Akteure" → Herleitung in Schritten → Stolperstein/zweite Sicht → Kern.
- **Adaptive Tiefe:** Grundlagen maßvoll, komplexe Themen (Transistor, OPV, Halbleiter, Fourier …) deutlich
  ausführlicher. Herleitungs-Zwischenschritte NICHT weglassen.

---

## 2. Übersichtlichkeit / Form
- Trotz Tiefe **klar gegliedert**: **Aufzählungen** und **nummerierte Schritte**, **kürzere Absätze**, keine
  dichten Textwände.
- Lange Herleitungen in **nummerierte Schritte** (oder `**Schritt 1**`, `**Schritt 2**` … → werden automatisch rot).
- Mehrere gleichartige Punkte → **Bullet-Liste**.
- Größen-/„Akteure"-Listen: ein Bullet je Größe mit Symbol + Rolle + Einheit.

---

## 3. Grafiken / Animationen
- **Jeder Artikel beginnt mit einer Abbildung/Animation** (`:::grafik` als ERSTES Content-Element, VOR `:::konzept`).
- **JEDE Gleichung / Definition / jeden Zusammenhang durch eine Grafik verdeutlichen** (User-Regel). Definitionen
  und Beziehungen sind grafisch oft viel klarer — z. B. „Kosinus = Realteil von $e^{j\varphi}$" als Zeiger der
  Länge 1 mit seiner Projektion auf die reelle Achse. Also möglichst **eine illustrierende Abbildung pro
  wichtiger Gleichung** (nie Platzhalter ohne Mehrwert, aber im Zweifel lieber eine Grafik mehr).
- **Skript-Abbildungen als Orientierung nutzen:** Standard-Darstellungen von Allgemeinwissen (Schaltpläne von
  Grundschaltungen, $E(k)$-/Kennlinien-Graphen, Kristallzellen, Feld-/Bänderbilder) dürfen nach Skript-Vorlage
  nachgebildet werden — sie sind nur grafische Abbilder freien Wissens. **Nicht** übernommen werden konkrete
  **Beispiel-/Klausuraufgaben** und einzelne, kreativ gestaltete Spezial-Abbildungen. Details §11 (Keine Kopien).
- **Deutlich mehr Grafiken**, besonders bei grafisch dankbaren Themen (komplexe Ebene, Zeiger, Felder, Kennlinien,
  Signale …). Richtwert: so viele wie didaktisch helfen (gern 5–10+).
- Platzhalter-Syntax (bis der Editor echte Grafiken liefert): Block `:::grafik … :::` mit **präziser
  Bildbeschreibung** (was zu sehen ist, Beschriftungen, bei Animationen der Ablauf). Siehe `EDITOR_GRAFIK_FEATURES.md`
  für die dafür nötigen Editor-Features.

---

## 4. Artikel-Aufbau (Standard-Gerüst)
1. **Frontmatter** (s. §7).
2. `:::grafik` — **Einstiegs-Abbildung/Animation** (orientiert, deutet den Kern an).
3. `:::konzept` — anschaulicher Einstieg / großes Bild / Analogie.
4. **„Worum es geht:"** — ein kurzer Absatz, was der Artikel klärt und wie er aufbaut.
5. **Hauptteil** in `##`-Abschnitten: von unten aufbauend, jede Formel hergeleitet, Größen als Bullet-Liste,
   Schritt-Herleitungen, zweite Sichten, Stolpersteine, viele Grafiken.
6. `:::kern` — **„Das Wichtigste"**: die Kernrelationen kompakt (die zentralen Formeln + Aussagen).
7. **Brücke** — ein, zwei Sätze zum nächsten Thema.

---

## 5. Markup & Einfärbung (automatisch durch `build_wissen.py`)
**Farbkategorien — korrekt einteilen (Farbe = je eine CSS-Zeile, Einteilung ist das Wichtige):**
- `__Name__` → **blau** (Größen-/Begriffs-/Einheitennamen: Stromstärke, Elementarladung, Phasor, Kreisfrequenz …).
- `**wichtig**` → **orange** (betonte Wörter/Ausdrücke, die KEINE Namen sind).
- `**Schritt N**` → **rot** (automatisch erkannt).
- Formeln werden automatisch eingefärbt: **LHS rot**, **Relation (`=`, `\approx`) blau**, **RHS gold** — nichts
  extra tun, einfach `$…$` / `$$…$$` schreiben.
- „Akteure"-Listen: `- __$I$__: die __Stromstärke__ …` (führendes Symbol als Name → blau, Doppelpunkt als Trenner).

**Callouts (`:::typ` … `:::`):**
- `:::konzept` („Zur Idee"), `:::kern` („Das Wichtigste"), `:::merke` („Merke"),
- `:::grafik` („Abbildung", Platzhalter), `:::satz`, `:::lemma`, `:::definition`.

**Weiteres:**
- **Tabellen:** GitHub-Syntax (`| … | … |` + `|---|---|`).
- **Überschriften:** `##` (Zwischenüberschrift, rot), `###` (rot). Titel (H1, aus Frontmatter) ist rot.
- Listen (`- …`, `1. …`), `> Zitat`, `` `code` ``, `**fett**`, `*kursiv*`, Links `[Text](url)`.

---

## 6. Mathematik / Notation
- **NOTATION EXAKT WIE IM VORLESUNGSSKRIPT des jeweiligen Moduls** (User-Vorgabe 2026-10-19: „Der Formalismus
  soll genau gleich sein"). Vor dem Schreiben die passenden Folien/Skript-Seiten lesen und **Symbole, Formen,
  Benennungen 1:1 übernehmen** (NICHT die Inhalte kopieren — §11 —, sondern den Formalismus). Modul-spezifisch,
  z. B.:
  - **MMET** (Signal Processing First / LfB-Folien): imaginäre Einheit $j=\sqrt{-1}$; komplexe Zahl $z=x+jy$ mit
    $x=\operatorname{Re}\{z\}$, $y=\operatorname{Im}\{z\}$ (geschweifte Klammern); Betrag $r=|z|=\sqrt{x^2+y^2}$;
    Winkel/Argument $\alpha$ (nicht $\varphi$!), $\arg(z)=\{\alpha+2\pi k\}$, Hauptwert $-\pi<\alpha\le\pi$;
    Polarform $z=r(\cos\alpha+j\sin\alpha)$; Sinussignal $s(t)=A\cos(\omega t+\varphi)=A\cos(\tfrac{2\pi}{T}t+\varphi)$
    ($\varphi$ = Signal-Phase); Folge $f[n]$ bzw. $\tilde s[n]=s(nT_s)=s(n/r)$; Abtastrate $r=1/T_s$; normierte
    Kreisfrequenz $\hat\omega=\omega T_s=\omega/r$.
  - **GEMB1** (Waser): Physik-Konvention imaginäre Einheit $i$; Symbole wie im Waser-Skript.
- **Elektrotechnik-Konventionen (Default, wenn kein Skript etwas anderes vorgibt):** imaginäre Einheit **`j`**; Ströme/Spannungen klein (Zeitgrößen) etc.
- **KaTeX:** `\mu` (NICHT `\upmu`), `\operatorname{atan2}`, `\mathrm{d}` für Differentiale, `\varphi` für Phase.
- **Korrektheit prüfen (!!!):** jede Positions-/Richtungs-/Vorzeichenangabe gegen die Formel gegenlesen
  (z. B. in $z=a+jb$ steht $b$ **nach** dem $j$). Differential-Ordnungen exakt, keine doppelt benutzten Symbole.
- Maximale Notations-Präzision, nichts für Einfachheit verwischen.

---

## 7. Frontmatter & Ablage
```
---
title: <Artikeltitel>
pfad: Studiengang / Semester / Modul / Oberthema
order: <Zahl>
summary: <ein Satz für Übersicht & Suche>
tags: <komma, getrennt>
---
```
- **`pfad`** baut den Navigationsbaum (beliebig tief, " / "-getrennt). Schema:
  `Elektrotechnik / 1. Semester / <Modul> / <Oberthema>`. Modul-/Oberthema-Namen **wie im Skript**.
- **`order`:** Sequenznummer, Schema `Kapitel*10000 + Abschnitt*100` (sortiert Oberthemen & Artikel je Ebene;
  kleinstes order bestimmt die Ebenen-Reihenfolge).
- **`summary`:** erscheint als Lede-Absatz oben im Artikel; KaTeX rendert darüber. **Formeln deshalb immer in
  `$…$`** (z. B. `$E_n = n^2 h^2/(8mL^2)$`), **nie** als Klartext mit Unicode-Hoch/-Tiefstellung (`E_n = n²…`),
  sonst erscheint die Formel roh im Lede.
- **Ablage:** `content/<modulkürzel>/<NN-oberthema>/<NN-thema>.md` (Ordnerstruktur nur zur Organisation; fürs
  Rendern zählt `pfad`).
- **Skript-Orientierung:** Themenauswahl/Gliederung an der Unterteilung des jeweiligen Skripts; nur abweichen,
  wenn eine bessere Gliederung sinnvoll ist.

---

## 8. Sprache (natürlich, kein KI-Look)
- So menschlich/natürlich wie ein kundiger Mensch schreibt. **Keine Emoji / ChatGPT-Symbole** als Marker.
- **Verbotene Floskeln/Wörter** (Beispiele): „Jetzt wird es interessant.", „rasen" (für Elektronen), „Hier liegt
  eine Stolperstelle", „es ist wichtig zu beachten", „zusammenfassend", übermäßige „nicht X, sondern Y"-Floskeln,
  Doppelpunkt-dann-Enthüllung, gleichförmiger Aufzählungs-Rhythmus. Locker UND professionell, abwechslungsreicher
  Satzbau.

---

## 9. Prozess (pro Artikel)
1. **Recherche zuerst:** professionelle Quellen/Vorlesungen/Bücher per WebSearch lesen, um das Thema selbst sauber
   zu verstehen; passende Inhalte dürfen ergänzt werden. Quellen im Chat als Markdown-Links nennen.
2. **Schreiben** nach §0–§8.
3. **Bauen:** `PYTHONIOENCODING=utf-8 python build_wissen.py` (vom Repo-Root; ohne das Präfix crasht nur der
   finale ✓-print an Windows-cp1252).
4. **Prüfen:** lokal via `http://127.0.0.1:8000/wissen/…` (Server: aus `web/` `python -m http.server 8000`),
   Grafiken/Farben/Korrektheit gegenlesen.
5. **Committen** (einzeln je Artikel, **kein Push** — der User pusht selbst). Branch `main`.
   Commit-Message endet mit:
   `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`
   `Claude-Session: https://claude.ai/code/session_011k5g5E9cexRssEPuRKzSTZ`

---

## 10. Verweise
- `EDITOR_GRAFIK_FEATURES.md` — welche Editor-Features für die Grafiken nötig sind.
- `EDITOR_FIXES.md` — offene WebGL-/Editor-Fixes.
- Gedächtnis-Datei `etundso-content-plattform.md` — Projekt-Historie/Details.

---

## 11. Keine Kopien (rechtlich zwingend)
**Allgemeingültiges Wissen ist frei** — physikalische Zusammenhänge, Herleitungen, Begriffe **und ihre
Standard-Darstellungen**. Die RWTH/Skripte *verbreiten* dieses Wissen nur, haben es nicht erfunden; sie können es
nicht für sich beanspruchen. Das dürfen und sollen wir in **eigenen Worten** erklären.

**Ausdrücklich erlaubt (keine Kopie im rechtlichen Sinn):**
- **Schaltpläne** von Grund-/Standardschaltungen (Spannungsteiler, Grundgatter, OPV-Grundschaltungen, …),
- **Graphen/Diagramme** allgemeiner Zusammenhänge (Kennlinien, $E(k)$-Bänder, Funktionsverläufe),
- **Struktur-/Prinzipdarstellungen** (Kristallzellen, Bänderschema, Feldbilder).
Solche Darstellungen sind nur grafische Abbilder von Allgemeinwissen — sie dürfen auch nach einer Skript-Vorlage
nachgebildet werden. In der Praxis müssen wir also **kaum aufpassen**.

**Weiterhin TABU sind nur echte geistige Schöpfungen:**
- **Beispielaufgaben**, **Klausur-/Übungsaufgaben** (konkrete Angaben, Zahlenwerte, Formulierung, Lösungsweg) —
  dafür immer ein **eigenes** Beispiel erfinden,
- **einzelne, aufwändig/eigenständig gestaltete Abbildungen** mit eigener kreativer Gestaltungshöhe (nicht die
  Standard-Schaltung/-Kurve, sondern eine individuelle Illustration), Fotos,
- wörtlich übernommene Textpassagen.

**Regel:** Standard-Darstellung von Allgemeinwissen = frei (auch nachbauen). Eine konkrete fremde **Aufgabe** oder
eine individuell gestaltete **Einzelabbildung** 1:1 (oder minimal abgewandelt) übernehmen = nein. Gilt für alle
Artikel und Fächer.
