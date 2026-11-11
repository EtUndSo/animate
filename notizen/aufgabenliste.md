# Aufgabenliste: einmalige Aufgaben und Loops (seit 11.11.2026)

Arbeitsweise laut User (11.11.2026): „Stelle eine Liste auf, die alle einmaligen Aufgaben und die Loops enthält, arbeite nach Abschluss der aktuellen Aufgaben dann erst die Aufgaben ab, die einmalig abgearbeitet werden müssen (z.B. Suchbug beheben) und danach in einer Loop die anderen Aufgaben.“

**Reihenfolge:**
1. Laufende Aufgaben zu Ende bringen (Abschnitt A).
2. Danach die einmaligen Aufgaben (B) nacheinander abarbeiten. Die Loops ruhen in dieser Zeit: Nach dem laufenden Kapitel startet kein neues.
3. Danach die Loops (C).

Jede erledigte Aufgabe hier abhaken, mit Datum. Einzelheiten stehen in den verlinkten Notizen.

## A. Laufend (zu Ende bringen)
- [x] (11.11.) Englisch: Linux, Kapitel 6 (12 Artikel, 78 S.); dazu 3 Stellen im deutschen Heft behoben. Die Englisch-Schleife ruht jetzt; die /loop-Wiederholung ist gestoppt und wird in Phase C neu gestartet.
- [x] (11.11.) Website-Welle W4a „Ansichten“, eingespielt und gebaut (+50 Seiten, `assets/formel-export.js`); dazu „Gelesen. In diesem Kapitel …“ in die Kennzahlenzeile verschoben (User). Früher: drei Ansichten, Formelsammlung bzw. Befehlsübersicht je Modul, Kapitel auf einer Seite, Download PNG/JPG/SVG/PDF, Haken für geschriebene Fassungen (`website_ausbau_plan.md`). Danach Patch prüfen und einspielen.
- [x] (11.11.) Kurzfassung und Formelsammlung ET3, Kapitel 3. Die Schleife ruht jetzt.

## B. Einmalige Aufgaben (in dieser Reihenfolge)
- [x] (11.11., Wunsch des Users zwischendurch) Sätze über das Prüfskript `rechnung_kap<N>.py` aus allen Artikeln entfernt: 98 Dateien in allen Sprachen, Konverter-Filter `ohne_rechenskript` in `tools/heft_zu_artikel.py`, damit sie nicht zurückkommen. Die Heft-PDFs behalten den Satz.
1. [x] (11.11., Abnahme durch den User offen) **Konverter für Kurzfassung und Formelsammlung:** `kurz_formeln()` in `tools/heft_zu_artikel.py`; ET3 Kap. 1–3 umgewandelt (Kurz 10/8/11, Formeln 10/7/11 Artikel), gebaut, im Browser geprüft. Früher: `tools/heft_zu_artikel.py` schreibt die Blöcke aus `kap<N>_kurz.tex` und `kap<N>_formeln.tex` als `::::kurzfassung`/`::::formelsammlung` in die Artikel. ET3 Kap. 1–3 neu umwandeln und bauen, dann **Abnahme durch den User** auf der Website.
2. [x] (11.11.) **Suchfehler behoben:** Ursache: `fold()` ändert die Länge (ß→ss, …→..., Ligaturen), die Fundstelle im gefalteten Text wurde direkt auf den Originaltext übertragen. Jetzt Zeichen für Zeichen zurückgerechnet (`SUCHE_JS` in `build_wissen.py`, `snippet`). Geprüft: „Kurve“, „Fourier“, „voltage“, „卷积“ markieren richtig. Früher: Der Ausschnitt markiert teils das falsche Wort. Testfall: „Kurve“ → markiert „ geht“ bei „Stufe 6: Die Wheatstonesche Brücke“. Ursache suchen in `suche.js` (`website_ausbau_plan.md`, Fehlerliste).
3. [x] (11.11.) **Heftstellen ET3 Kap. 1 und 3 korrigiert** (alle 8 Meldungen berechtigt; de/en/es/zh; 8 PDFs neu; 7 Artikel × 4 Sprachen; Bericht `scratchpad/korr_et3/stand.md`). Früher: (Liste in `kurzfassung_schleife.md`, „Fragliche Stellen“):
   - Kap. 1: „Nacheilwinkel“ φ = −arctan x; fehlende Bedingung b ≠ 0.
   - Kap. 3, darunter zwei echte Sachfehler: Existenzbedingung der Fourier-Transformation; Gauß-Vertiefung ohne Bedingung an das zweite Moment.
   - Danach PDFs in allen vorhandenen Sprachen (de/en/es/zh) und die Artikel neu bauen.
4. [x] (11.11.) **Website-Welle W4b „Bereiche“** eingespielt: Kopfleiste Wissen/Lernkarten/Aufgaben/Editor; `/lernen/` (drei Tiefen, Lernen/Quiz/Mischtest), `/aufgaben/` (1 076 de); Haken `::::lernkarten`; alte `lernkarten.html` leiten weiter; +63 Dateien (8 292). Startseite: „Videos“ und „Editor öffnen“ nicht mehr in der Kopfleiste. Früher:
   - Kopfleiste und Startseite mit vier Bereichen: Wissen, Lernkarten/Quiz, Aufgaben, Editor.
   - Lernkarten-Bereich mit drei Tiefen (Artikel, Kapitel, Modul).
   - Aufgaben-Bereich mit 1 076 Aufgaben samt Lösungen.
   - Mischtest; Verweise unter jedem Artikel.
   - Die Karteninhalte bleiben vorerst automatisch, ihre Überarbeitung ist B5.
5. [ ] (11.11.: Pilot ET1 Kap. 1 fertig und eingebaut, 98 Karten; Build übernimmt die Bestimmungen der Begriffskarten in Zusammenfassung und Begriffsverzeichnis; **Abnahme durch den User offen**, danach Loop C2. Muster `notizen/lernkarten_muster.md`) **Lernkarten neu, in Ruhe** (Wunsch des User: wenn kein anderer Agent läuft):
   - zuerst mit dem User Kartenarten und Muster festlegen (Begriffe, Formeln, Herleitungen, Zusammenhänge; sinnvolle Fragen und Antworten), dann ein Pilot an einem Heft;
   - dabei die Begriffsbestimmungen für Zusammenfassung und Begriffsverzeichnis gleich mit lösen (Konverter-Wunsch `\fb[Bestimmung]{Begriff}`, Satzbruch um abgesetzte Formeln, `summary:` als Klartext);
   - das Schreiben für alle Hefte läuft danach in Loop C2.
6. [ ] (läuft seit 11.11. abends: Agent in Arbeitskopie `scratchpad/wt_w3b`, Port 8006, Patch `scratchpad/website_w3b/w3b.patch`; KaTeX 0.16.11 + MathJax 3.2.2 aus npm, Prüfsumme geprüft, in `scratchpad/npm_pakete`; Vorschaubilder je Kapitel und Sprache) **Website-Welle W3b „Auffindbarkeit“:**
   - Sitemap, `canonical`, `x-default`, strukturierte Daten;
   - Vorschaubilder je Kapitel;
   - KaTeX **und MathJax** selbst ausliefern (MathJax lädt der Download-Knopf heute beim Klick von cdnjs; cdnjs fehlt auch in der Datenschutzerklärung);
   - Startseiten-Abbildungen fr/tr.
7. [ ] **Website-Welle W5:**
   - „Hat das geholfen?“ und „Fehler melden“ (vorher mit dem User klären, wohin Meldungen gehen);
   - Regler-Modus für Abbildungen.
8. [ ] **Editor F1 „Bildschirme und Fenster“** (`editor_bildschirme_plan.md`): Fenster, Terminal mit Raster und ANSI, Mitschrift-Import, Maus, Tasten, Lupe. Vorher Funktionsliste aus Linux 7/8 abstimmen. **User 11.11. abends: „F1 bleibt vorne, danach dann die Loops.“** (ersetzt „erst nach den Übersetzungen“)
9. [ ] **Linux 7 Phase 2b, Linux 8 Phase 2b-1 und 2b-2** (Abbildungen, PDF, Artikel), mit dem neuen Terminal aus F1.
10. [ ] **Editor E4** (L6 Teilchen, L7 Operationen, L8 Code-Objekt = F2 Code-Editor, diskrete Faltung, komplexe Rechenbilder, Pfeil umhängen), danach die **Ansicht Szene ↔ Code**.
    - Werkzeug-Wünsche dazu:
      - Export meldet unsichtbare Objekte;
      - `s.summe(werte=[…])`;
      - `s.ersetzen` für bewegte Texte;
      - `$` in Überschriften ohne `\texttt`;
      - Eckenrundung bei `s.box`.
11. [ ] **Kleinkram:**
    - ET3 Kap. 2 en/es/zh neu übersetzen (veraltet, 7 statt 9 Artikel);
    - HöMa1 Kap. 3 es/zh neu;
    - Datum auf dem Titelblatt von Grundlagen 3;
    - Weiterleitung der alten Python-3-Adresse;
    - Videos-Link in der Kopfleiste unter 480 px;
    - aria-label der Abbildungen mit Leerzeichen vor Satzzeichen nach Code;
    - 22 Begriffe, die in ET-Beispielkästen erklärt sind;
    - E3-Demo „A w kippt“;
    - doppelte id „x“ auf `zh/index.html`;
    - „Gelesen“ in der Ansicht „Formeln“ nicht mehr zählen (Vorschlag W4a: Nachschlagen ist kein Lesen);
    - beim Umbruch auf dem Handy beginnt die Kennzahlenzeile mit „·“;
    - ET3 Kap. 3, schon vorher vorhanden: Hann-Fenster-Abbildung ragt über den Rand (de/en/es S. 17), zh 4 Stellen (S. 14, 15, 17); zh-Kursiven (`\emph` kap1_zh Z. 95, qa-Titel kap3a_zh Z. 156);
    - in den Ansichten „Kurz“ und „Formeln“ zeigen „In diesem Artikel“ und „Auf dieser Seite“ noch die Abschnitte der ausführlichen Fassung (bei geschriebenen Blöcken ausblenden), die Kennzahlen zählen Abbildungen und Aufgaben der Langfassung.
12. [x] (11.11.) **Kopfleiste live als Liste mit Punkten:**
    - Ursache: Cloudflare hält CSS/JS/SVG 4 h im Browser (Browser Cache TTL), das HTML nicht.
    - Behoben: wissen.css/.js, suche.js, formel-export.js und bereiche.js bekommen `?v=<Inhalts-Hash>` (`assets_bauen`, `asset()` in `build_wissen.py`), auch in `web/index.html`.
    - Empfehlung an den User: Cloudflare → Caching → Browser Cache TTL → „Respect Existing Headers“.

## C. Loops (nach B)
Wie bisher: höchstens ein Schreib-Agent und parallel ein Übersetzer (C1 ‖ C2). Reihenfolge C1–C5 wie unten; User 11.11.: „danach dann die Loops“.
- **C1 Englisch-Übersetzung:** Cybersecurity 1, ML 4–5, HöMa1 4–10, HöMa3 1, 2, 4–8, GEMB1 1–15. Danach alle en-Fassungen neu umwandeln (Links). Siehe `uebersetzung_en_schleife.md`.
- **C2 Formelsammlung bzw. Befehlsübersicht** (und die neuen Lernkarten, falls im selben Durchgang) für alle Hefte; **Kurzfassungen entfallen** (User 11.11. abends: die Zusammenfassung am Artikelende genügt, die Ansicht „Kurz“ ist entfernt): ET3, HöMa1, HöMa3, ML, ET1, GEMB1, dann Linux, Python, Cybersecurity. Siehe `kurzfassung_schleife.md`.
- **C3 Übersetzungen es/zh/fr/tr:** alle Hefte nach Englisch, dazu die neuen Kurzfassungs-Dateien.
- **C4 Neue Hefte** in der Reihenfolge des Users: Cybersecurity 2 (vorher Cyber-LERNPFAD auf 12 Hefte umstellen), Linux 9–10, Cybersecurity 3, Cybersecurity 4–5, weitere Cyber-Hefte. Danach Python 4/5/12/13, ML-Pfad, GEMB1 ab Teil 16. Je Heft Phase 1, 2a, 2b.
- **C5 Nachrüstwellen** (ältere Hefte mit neuen Editor-Funktionen und Animationen), nach E4.

## Pausiert (nicht von selbst anstoßen)
- Website vom Raspberry Pi (`hosting/ANLEITUNG.md`); Frage offen, ob auf der NVMe schon Daten liegen.
- Anmeldung/Konten.
- HöMa3, Kapitel 3: halb überarbeitet.
