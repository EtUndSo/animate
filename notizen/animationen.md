# Animierte Abbildungen: Kurzanleitung (09.11.2026)

Jede Editor-Szene darf eine **Zeitachse** haben. Auf der Website läuft sie dann als Animation mit Start/Stopp,
Neustart, Zeitleiste und Sprungmarken. Das statische Bild und das PDF zeigen ihr **Endbild**. Eine Szene hat also
eine Quelle für drei Ausgaben.

| Ausgabe | Datei | entsteht mit |
|---|---|---|
| Website, animiert | `web/abbildungen/<sprache>/<szene>.anim.svg` | `tools/export_szenen.py --animiert` |
| Website ohne Skript, Bild im Editor-Link | `web/abbildungen/<sprache>/<szene>.svg` (Endbild) | `tools/export_szenen.py` |
| Heft-PDF | `<heftordner>/abb/<sprache>/<szene>.pdf` (Vektor-PDF des Endbilds) | `tools/szenen_pdf.py <modul> <heftordner>` |

Beispiele zum Abschauen: `tools/szenen/beispiel_animation.py` (Szenen `beispiel/anim_*`), für Parameter über die
Zeit (§8) `tools/szenen/beispiel_parameter.py` (Szenen `beispiel/anim_l3_*`), für Ebene abbilden (§9)
`tools/szenen/beispiel_gitter.py` (`beispiel/anim_l5_*`), für Kamerafahrten in 3D (§10)
`tools/szenen/beispiel_kamera.py` (`beispiel/anim_l4_*`).

## 1. Zeitachse anlegen (`tools/szenen_lib.py`)

Jeder Aufruf hängt einen neuen **Schritt** an. Aufrufe in `with s.gleichzeitig():` teilen sich einen Schritt.
Ziele sind die ids, die `s.kurve`, `s.box`, `s.pfeil` usw. zurückgeben.

```python
s = Szene("et3/k2beispiel")
a = s.achsen(...); k = s.kurve(a, "exp(-x)"); t = s.text(a, "@lab", (1, 0.5))
s.einblenden(a)                          # Achsen erscheinen
with s.gleichzeitig():
    s.zeichnen(k, dauer=1.5)             # Kurve zeichnet sich ...
    s.einblenden(t)                      # ... während die Beschriftung einblendet
s.pause(0.8)                             # Haltepunkt
s.betonen(t)
s.speichern()
```

| Helfer | Animation | Hinweis |
|---|---|---|
| `zeichnen(id)` | Create | Linie, Kurve, Pfeil, Umriss zeichnet sich |
| `schreiben(id)` | Write | Text oder Formel |
| `einblenden(*ids, nacheinander=False)` | FadeIn | mehrere zusammen oder nacheinander |
| `wachsen(id)` | GrowFromCenter | Punkt, Kasten, Bauteil |
| `ausblenden(*ids)` | FadeOut (L1) | fehlt danach im Endbild und im PDF |
| `verschieben(id, dx, dy)`, `bewegen_zu(id, x, y)` | Shift, MoveTo | Endbild: am Ziel |
| `drehen(id, grad, um=(x, y))`, `skalieren(id, faktor, um=…)` | Rotate, Scale | `um` = Drehpunkt (Zeiger) |
| `entlang(id, weg_id)` | MoveAlongPath | Punkt läuft auf einer Kurve |
| `betonen(id)` | Indicate | kurz größer und farbig, auch für Text |
| `betonen(tab, zelle=(z, s) / zeile=z / spalte=s)` | Indicate auf Tabellenzellen (L9) | Zelle leuchtet auf und ab; `s.tabelle(...)` |
| `umformen(id, zu_id, passend=False)` | Transform / TransformMatchingTex (L2) | `zu_id` ist nur Vorlage und wird nie gezeichnet; `passend=True` bei zwei Formeln: gleiche Zeichen wandern; zwei Texte: Inhalt wechselt (§7.3) |
| `ersetzen(id, text, farbe=None)` | Transform Text → Text | neuer Inhalt eines `s.text`, Vorlage legt der Helfer selbst an (§7.3) |
| `pause(dauer)` | Wait | nichts bewegt sich |
| `animation(art, id, dauer, **werte)` | jede Editor-Animation | allgemeine Form |
| `formel(tex, ..., zeilenweise=True)` | FadeIn Zeile für Zeile | Rechnung in `aligned`: je Zeile ein Schritt, Sprungmarke je Zeile |

Regeln:
- Ein Objekt mit Erscheinen-Animation (zeichnen, schreiben, einblenden, wachsen) ist vorher unsichtbar.
  Alles andere steht von Anfang an da. Was oben liegt, regelt `Szene(…, reihenfolge=…)` (§7.4).
- **Endbild = Bild im Heft.** Was am Ende sichtbar ist, steht im PDF. Was ausgeblendet wird, fehlt dort.
  Bewegte Objekte stehen an ihrem Ziel.
- **Rechenbilder** `s.summe`, `s.produkt`, `s.skalarprodukt` brauchen nichts weiter: Sie laufen von selbst Zeile für
  Zeile und Glied für Glied ab und enden genau im heutigen Bild. Ein Glied der nächsten Zeile erscheint, während sein
  Gegenstück darüber aufleuchtet. Jede Zeile ist eine Sprungmarke. Dasselbe passiert im Editor beim Abspielen.
  Bei Rechenbildern aus `s.formel` (aligned) wählt man `zeilenweise=True`.
- Dauer: 0,5–1,5 s je Schritt. Ganze Animation möglichst unter 15 s.
- Im Editor erscheinen die Schritte in der Liste „Animationen“. Neu im Menü sind Verschwinden (FadeOut) und Umformen
  (Transform, ReplacementTransform, TransformMatchingTex mit Auswahl „to“). Bei Tabellen hat Betonen die Felder
  row/col.
  Der Wert `step` einer Animation (aus `szenen_lib`) bleibt beim Speichern erhalten.

## 2. Exportieren

```
python tools/export_szenen.py --animiert et3/k2beispiel             # alle sechs Sprachen, .svg und .anim.svg
python tools/export_szenen.py --animiert --lang de et3/k2beispiel   # nur Deutsch
```

Die Ausgabezeile nennt Dauer, Bilder, bewegte Elemente und Größe, z. B. `animiert 5,3 s, 162 Bilder, 37 von 37
Elementen bewegt, 74,4 KB (Daten 16,9 KB)`. Warnungen:
- „Endbild der Animation weicht vom statischen Bild ab“: Das sollte nicht vorkommen, bitte melden.
- „Zeichenreihenfolge ändert sich (3D-Tiefe)“: In 3D-Szenen behält die Datei die Reihenfolge des Endbilds.
  Das ist meist unsichtbar.
- „Datenblock groß“: Die Pfade werden mit halber Rate abgetastet. Dann besser kürzer animieren oder weniger umformen.
- „keine animierte Datei: keine Zeitachse“: Eine vorhandene alte `.anim.svg` wird gelöscht. Die Seite zeigt dann
  wieder das statische Bild.
- „Text liegt unter einer deckenden Fläche: o7 unter o3“ (seit 10.11.2026): Im Endbild deckt eine später gezeichnete
  Fläche (Deckkraft ab 0,9) mindestens 80 % eines Texts eines anderen Objekts ab. Abhilfe in §7.4. Gewollte Masken
  melden sich auch: Unter allen 809 Szenen sind es genau zwei, beide gewollt (`linux/k4strom`: die Wolke verdeckt den
  Schreiber; `startseite/fourier`).

Ohne `--animiert` läuft der Export wie bisher. Ausnahme: Hat eine Szene eine Zeitachse, ist ihr `.svg` das Endbild.
Danach wie immer `python build_wissen.py`. Gibt es eine `.anim.svg`, setzt `build_wissen` an der Abbildung
`data-anim`, und der Spieler übernimmt. Am Artikel und am Konverter ist nichts zu tun.

Wird eine Szene später ohne `--animiert` exportiert, ist ihr `.svg` neuer als die `.anim.svg`. Die Animation wäre
dann veraltet. `build_wissen` lässt sie deshalb weg und meldet „… .anim.svg ist älter als das Bild“.

Größen der Beispiele (de; Datei gesamt, davon Datenblock):

| Szene | Art | Dauer | .anim.svg | Daten | statisch |
|---|---|---:|---:|---:|---:|
| beispiel/anim_bootkette | Kästen und Pfeile | 6,8 s | 33 KB | 21 KB | 11 KB |
| beispiel/anim_sprung | Funktionsgraph | 6,0 s | 29 KB | 7 KB | 22 KB |
| beispiel/anim_esb | Schaltung (ET1) | 5,8 s | 42 KB | 24 KB | 17 KB |
| beispiel/anim_norm | 3D, feste Kamera | 4,9 s | 23 KB | 17 KB | 6 KB |
| beispiel/anim_umformen | L1, L2, L9 (mit Schreiben einer Formel) | 8,0 s | 89 KB | 63 KB | 15 KB |
| beispiel/anim_formel | Rechenbild s.formel zeilenweise | 4,8 s | 112 KB | 7 KB | 105 KB |
| prog/k3rquadrate | Rechenbild s.summe | 5,3 s | 70 KB | 13 KB | 58 KB |
| startseite/fourier | Startseiten-Animation | 12,5 s | 120 KB | 15 KB | 107 KB |

Vorhanden sind die `beispiel/anim_*` in allen sechs Sprachen und `startseite/fourier` nur auf Deutsch. Die
Startseite selbst ist unverändert. `prog/k3rquadrate.anim.svg` wurde nach dem Test wieder gelöscht, damit der echte
Artikel bis zum Nachrüsten statisch bleibt.

Groß sind vor allem die Formeln selbst, also die Glyphenpfade im Endbild. Die Animation selbst kostet meist 5–25 KB.
Mit gzip (so liefert der Server aus) sind es etwa ein Viertel. Am teuersten ist `schreiben` (Write) auf eine Formel:
Jede Glyphe wird dabei 10-mal je Sekunde als ganzer Pfad gespeichert. Für Formeln besser `einblenden` oder
`formel(zeilenweise=True)` nehmen.

## 3. Auf der Website (Spieler in `build_wissen.py`, WISSEN_JS/WISSEN_CSS)

- Die Abbildung startet, wenn sie zu einem guten Drittel im Bild ist, und hält an, wenn sie es verlässt oder der Tab in
  den Hintergrund geht. Liegt sie in einem zugeklappten `beispiel`- oder `hintergrund`-Kasten, wird sie erst beim
  Aufklappen geladen und gestartet.
- Bei „Bewegung reduzieren“ startet nichts von selbst. Die Seite zeigt das Endbild, der Leser kann abspielen.
- Bedienung: Start/Stopp (am Ende: von vorn), Neustart, Schritt zurück/vor zu den Sprungmarken, Zeitleiste
  (ziehen, Pfeiltasten, Pos1/Ende). Alles ist per Tastatur bedienbar und hat ein `aria-label`. Die Zeitleiste
  meldet „2,3 s von 5,0 s“.
- Ohne Skript, ohne `.anim.svg` oder bei einem Ladefehler bleibt das statische Bild.

## 4. Im Heft-PDF: `\szenenabb`

In allen 54 Präambeln (9 Heftordner × 6 Sprachen) steht:

```latex
\szenenabb{k3rquadrate}{Die Summe der Quadrate von 1 bis 5.}{fig:k3rquadrate}
```

- Das Makro bindet das Endbild `abb/<sprache>/k3rquadrate.pdf` ein, ein Vektor-PDF aus Chromium. Es nummeriert wie eine
  Abbildung, und `\ref{fig:k3rquadrate}` funktioniert.
- Ist das Bild breiter als die Zeile, wird es verkleinert, sonst bleibt die natürliche Größe (Beschriftung wie auf
  der Website).
- Fehlt das PDF, steht ein Platzhalter „Szene <modul>/<szene> fehlt noch“ da.
- Wie die `abb`-Umgebung ist es ein Gleitobjekt: nicht in Kästen (tcolorbox) oder minipages verwenden.
- PDF erzeugen: erst `python tools/export_szenen.py <modul>/<szene>`, dann
  `python tools/szenen_pdf.py <modul> "<heftordner>" <szene>`. Ohne Szenennamen werden alle Szenen des Moduls erzeugt.
- Der Konverter (`tools/heft_zu_artikel.py`) macht daraus `:::abbildung <modul>/<szene> <nr>` mit Bildunterschrift und
  Label, genau wie bei `abb`. Jede Sprachfassung nimmt das Bild ihrer Sprache.
- Vorhandene TikZ-Abbildungen bleiben, wie sie sind. `\szenenabb` gilt für neue Abbildungen.

## 5. Vorschlag für die Regeln im Auftrag

1. **Neue Abbildungen nur als Editor-Szene** mit `\szenenabb{<szene>}{<Unterschrift>}{fig:<szene>}` im Heft, ohne
   TikZ. Die Szene heißt wie das Label (`k<N><name>`).
2. **Animation ist der Normalfall.** Jede neue Szene bekommt eine Zeitachse, die den Gedankengang in der
   Reihenfolge des Texts aufbaut. Erst kommt der Rahmen (Achsen, Kästen), dann das Neue, zuletzt Beschriftung und
   Betonung. Statisch bleibt eine Szene nur, wenn Bewegung nichts erklärt.
3. **Schritte = Haltepunkte.** Ein Schritt zeigt einen Gedanken (0,5–1,5 s). Gleichzeitig läuft nur, was
   zusammengehört. Vor einem neuen Gedanken steht `s.pause(0.6)`. Ganze Animation möglichst unter 15 s.
4. **Das Endbild muss allein verständlich sein.** Es steht im PDF und erscheint bei „Bewegung reduzieren“. Hilfsobjekte,
   die nur während der Animation helfen, mit `s.ausblenden` entfernen. Was im PDF fehlen darf, darf auch im Endbild
   fehlen.
5. **Rechenbilder** mit `s.summe`/`s.produkt`/`s.skalarprodukt` (laufen von selbst Zeile für Zeile). Ein Rechenbild aus
   `s.formel(..., zeilenweise=True)` geht nur, wenn kein Operator passt.
6. **Export immer mit `--animiert`**, in allen Sprachen, vor `build_wissen.py`. Die Ausgabe prüfen: keine Warnung
   „Endbild weicht ab“, Datei möglichst unter 300 KB.
7. **Anzahl je Artikel** nach Länge, mindestens 1, höchstens 5 (Wunsch des Users). Richtwert: eine Abbildung je
   450 Wörter, zugeklappte Kästen zählen halb. Mehr neue Begriffe dürfen +1 begründen.

## 6. Grenzen und offene Punkte

- **L3 (Parameter über die Zeit)** ist seit 10.11.2026 gebaut: §8. Seine Grenzen stehen dort in §8.5.
- **L5 (Ebene abbilden)** und **L4 (Kamerafahrt in 3D)** sind seit 10.11.2026 gebaut: §9 und §10, Grenzen in §9.4 und
  §10.5. Für eine Kamerafahrt projiziert der Spieler selbst (die Datei trägt Weltpunkte und eine Kamera-Spur statt
  Pfaden je Bild) und sortiert die Elemente in jedem Bild nach ihrer Tiefe; die Messung steht in §10.3.
- Ein Text, dessen Inhalt sich ändert (Zähler, `s.ersetzen`), wird als Ganzes ausgetauscht (Spur `h`).
- Ausgeblendete Objekte (`s.ausblenden`) stehen weiter mit Deckkraft 0 im statischen `.svg` und im PDF
  (`pdf_pruefen.py` überspringt sie). Für Texte, die nur den Inhalt wechseln, deshalb `s.ersetzen` nehmen (§7.3).
- `Write` auf Formeln speichert die Glyphen bildweise (Spur `d`). Für Formeln ist `einblenden` oder
  `formel(zeilenweise=True)` kleiner.
- **Warum Datenblock plus Spieler und nicht SMIL** (Vergleich an 7 Beispielen, 09.11.2026). Aus denselben
  Schlüsselbildern wurde auch SMIL (`<animate>`, `<animateTransform>`) erzeugt.
  - Größe: SMIL ist roh 1,2- bis 2,2-mal so groß (z. B. Schaltung 42 → 91 KB), mit gzip 2–38 % größer.
  - Genauigkeit: In Chromium zeigen beide dasselbe. Gemessen wurde zu drei Zeitpunkten je Szene, mit höchstens 0,4 %
    abweichenden Pixeln, nur an Kanten.
  - Steuerbarkeit: SMIL geht nur über `pauseAnimations`/`setCurrentTime` der eingebetteten SVG. Damit die Datei ohne
    Skript das Endbild zeigt, braucht sie `begin="indefinite"`, also einen Umweg beim Springen. Wie verlässlich das
    Rückwärtsspringen in Firefox und Safari ist, wurde nicht geprüft.
  - Grenzen von SMIL: Es kann keinen Textinhalt tauschen, und jede Matrix braucht vier `animateTransform`.
  - Der Spieler mit Datenblock kann alles davon. Er braucht nur DOM-Attribute und funktioniert deshalb in jedem
    Browser gleich.
- Genauigkeit des Spielers gegen das Bild der Engine zur selben Zeit: höchstens 0,9 % abweichende Pixel, meist unter
  0,1 %. Die Abweichungen stammen von Kantenglättung und von Zwischenständen zwischen zwei abgetasteten Bildern. In 3D
  ohne Kamerafahrt kommt die feste Zeichenreihenfolge dazu (mit Kamerafahrt sortiert der Spieler selbst, §10.3).

## 7. Werkzeuge vom 10.11.2026 (Text, Ebenen, Rechenbilder)

Alles ist rückwärtsverträglich: Ohne die neuen Optionen schreiben die Szenen-Skripte dieselben Dateien wie vorher, und
die vorhandenen Szenen ergeben dieselben Bilder (Ausnahmen: die Fehlerbehebungen in §7.6). Tests:
`web/tests/test_text_werkzeuge.py`, `web/tests/test_texspec.mjs`, ein Fall in `test_contract.py`.

### 7.1 Schreibmaschinenschrift: `s.text(..., schrift="tt")`

```python
s.text(None, "-rw-r--r-- 1 student student   25 Nov 10 02:41 einkauf_alt.txt", (-3.0, 0.8), 20, "left", schrift="tt")
s.text(None, "echo 'it''s' `date` $HOME 1.5M", (-3.0, 0.4), 20, "left", schrift="tt", farbe=BLAU)
x = -3.0 + tt_breite(20, 15)        # linke Kante der Spalte 15 dieser Zeilen
```

- Echte Zeichen statt Formel-Glyphen: eine Terminalzeile kostet etwa 0,5 KB statt 1,5–2 KB je Zeichen.
- Jedes Zeichen steht in der Mitte einer Zelle von 0,6 em (`tt_breite(groesse, n)` in Szeneneinheiten). Spalten stehen
  untereinander, mehrere Leerzeichen bleiben, ein chinesisches Zeichen belegt zwei Zellen. Die Zellen setzen Lage und
  Breite, nicht die Schrift: Jede Schreibmaschinenschrift des Lesers ergibt dieselben Spalten.
- `'` und `` ` `` bleiben gerade, Dezimalpunkte bleiben Punkte (kein Komma in de/es/fr/tr). tt ist immer roh (§7.2),
  ausdrücklich `roh=False` löst nur Makros wie `\alpha` auf (keine Hoch-/Tiefstellung).
- Schrift: Consolas (in jedem Windows; Editor, Website und PDF zeigen hier dieselbe), sonst Menlo, DejaVu Sans Mono,
  Liberation Mono, Courier New; chinesische Zeichen aus Microsoft YaHei, Noto Sans Mono CJK SC oder PingFang SC
  (`engine/svg_painter.MONO_FONT`). Keine Webschrift: Ein SVG im `<img>` kann keine laden.
- Größe: `groesse` in Szenenpixeln wie jede Beschriftung; 20–22 entspricht der alten Terminalzeile mit 0,17–0,19
  Einheiten Höhe.
- Im Editor: Objekt „Text“, Feld `font` = mono. Im PDF steht echter Text (durchsuchbar, Leerzeichen kopierbar).

### 7.2 Rohtext: `s.text(..., roh=True)`

```python
s.text(None, "einkauf_alt.txt  C:\\  ^x  $HOME  {a,b}", (0, 0), 22, "left", roh=True)
```

Ohne Rich-Text: `_ ^ \ $ { }` sind gewöhnliche Zeichen, mehrere Leerzeichen bleiben, nur ein echter Zeilenumbruch
`"\n"` bricht die Zeile. `@schluessel` aus `s.tr` gilt weiter, Dezimalpunkte bleiben Punkte. Im Editor: Feld `raw`.

### 7.3 Inhalt eines Texts ändern: `s.ersetzen` / `s.umformen`

```python
t = s.text(None, "einkauf.txt", (0, 0), 22, "center", schrift="tt")
s.einblenden(t)
s.ersetzen(t, "einkauf_alt.txt", farbe=ROT)      # legt die Vorlage an und formt um (0,8 s)
```

Transform zwischen zwei Texten (`s.umformen(t, vorlage)`, im Editor „Transform“ mit „to“) ändert jetzt Inhalt, Farbe,
Größe, Lage und Schrift: Der alte Text blendet in der ersten Hälfte aus, der neue in der zweiten ein. Im Endbild, im
`.svg` und im PDF steht nur der neue Text, kein unsichtbarer Rest. Bisher änderte Transform auf Text nichts.

### 7.4 Was oben liegt: `Szene(name, reihenfolge="anlegen")`

- Bisher (und weiter ohne Angabe): Ein Objekt mit Erscheinen-Animation legt sich über alles, was schon sichtbar ist,
  auch innerhalb eines Schritts in der Reihenfolge der Animationen. Ein Kasten, der nach seinem Text erscheint,
  verdeckt ihn.
- `reihenfolge="anlegen"`: Die Reihenfolge des Anlegens gilt, auch für erscheinende Objekte. Was später angelegt wird,
  liegt oben: erst den Kasten anlegen, dann seinen Text, und beide dürfen in beliebiger Reihenfolge erscheinen.
  Objekte von Operationen (Σ, Faltung) liegen über allen angelegten Objekten. Die Zeitachse ändert sich nicht.
- **Empfehlung für neue Szenen:** `reihenfolge="anlegen"`. Vorhandene Szenen bleiben ohne Eintrag und damit, wie sie
  sind. In der Szenendatei steht dann `"drawOrder": "creation"`.
- Im Editor: Auswahl „Ebenen“ neben „Animations“ (wie angelegt / wie erschienen). Eine neue Szene und jede Vorlage
  beginnen mit „wie angelegt“; eine geladene Datei ohne Eintrag bleibt bei „wie erschienen“.
- Der Export warnt bei verdecktem Text (§2).

### 7.5 Kleinere Werkzeuge

- **`s.weg(..., spitze=0.11)`**: Länge der Richtungsmarken (Standard 0,22, im Editor `head_size`). Für kurze Wege wie
  Schleifenpfeile.
- **Rechenbilder mit anderem Laufindex und exakten Brüchen:**
  `s.summe("3/2^(4*k+1)", von=1, bis=4, index="k", exakt=True)` ergibt
  3/32 + 3/512 + 3/8192 + 3/131072 = 13107/131072 = 0,0999985. `index` ist ein Buchstabe außer e; der Term nennt ihn
  (Produkte mit `*` schreiben: `4*k`, nicht `4k`). `exakt=True` rechnet mit ganzen Zahlen und zeigt Brüche mit
  beliebig großem Nenner; ohne `exakt` bleiben Brüche bis Nenner 10000 (wie bisher). Gilt ebenso für `s.produkt`; im
  Editor die Felder `index` und `exact` der Operation.
- **Kontaktblätter:** `tools/szenen_ansehen.py` exportiert mit `--animiert` (die `.anim.svg` bleibt aktuell), mit
  `--ohne-export` nur ansehen. Aus den Heft-PDFs: `tools/kontaktblatt_pdf.py` (`notizen/koordination.md`).
- **Linux-Helfer** in `tools/szenen/linux_hilfen.py` (aus `linux_teil3.py` und `linux_teil4.py`, Bilder unverändert).
  Neue Kapitel: `from linux_hilfen import *`, dann `schreibmaschine("text")`: `tt`, `ttz` und `prozess` setzen ihre
  Zeilen dann als `s.text(schrift="tt")` statt als Formel mit `\rule`-Stütze, mit denselben Spalten (`sp`, `msp`, `cw`).

### 7.6 Fehlerbehebungen in Formeln (`s.formel`, editor.js `localizeTex`)

- `\mathtt{einkauf.txt}` hat keinen Abstand mehr nach dem Punkt (MathJax setzte einen).
- `'` und `` ` `` in `\texttt{…}` sind gerade (ein Strich und der Gravis in der Zelle von 0,525 em) statt ’ und ‘.
- Code in `\texttt{…}`/`\mathtt{…}` mit `\$ \{ \}` oder Klammern darin behält seine Dezimalpunkte (vorher bekam er
  in de/es/fr/tr ein Komma, nur ohne Klammern war er geschützt).

### 7.7 Fehlerbehebung `s.gleichzeitig()` (10.11.2026, E3)

`s.einblenden(a, b)` mit mehreren Zielen und `s.ausblenden(...)` öffnen selbst ein `gleichzeitig()`. Innerhalb eines
äußeren `with s.gleichzeitig():` begann das innere bisher einen neuen Schritt und beendete den äußeren: Was danach im
Block stand, lief nacheinander statt zusammen. Jetzt bleibt ein verschachteltes `gleichzeitig()` beim äußeren Schritt.
Betroffen waren nur die Vorführszenen `beispiel/anim_esb` (8,4 → 5,8 s), `beispiel/anim_norm` (6,1 → 4,9 s) und
`beispiel/anim_l3_grenzwert` (10,4 → 9,8 s); ihr Endbild (`.svg`, PDF) ist unverändert, die `.anim.svg` ist in allen
sechs Sprachen neu exportiert. Alle anderen Szenen-Skripte bauen dieselben Dateien wie vorher.

## 8. Parameter über die Zeit (L3, 10.11.2026)

Ein **Parameter** ist eine Zahl der Szene mit Namen. Jeder Ausdruck der Szene darf ihn nennen. `s.verstellen` ändert
ihn über die Zeit, und jedes Objekt, das ihn nennt, wird in jedem Bild neu berechnet: laufende Welle, Punkt auf der
Kurve mit Tangente, Zeitmarker, Zeiger, Grenzprozess, wachsende Fläche. Statisches Bild und PDF zeigen wie immer das
Endbild, also alles beim letzten Zielwert.

### 8.1 Aufrufe (`tools/szenen_lib.py`)

```python
s = Szene("et3/k3welle", reihenfolge="anlegen")
a = s.achsen((0, 12, 2), (-1.5, 1.5, 1), breite=6.4, hoehe=2.4, xl="x", yl="y")
s.parameter("t", 0)                                   # Name, Startwert
k = s.kurve(a, "sin(pi/2*(x - t))", punkte=49)          # nennt t: läuft mit
d = s.punkt(a, "1 + t", 1, farbe=ROT)                 # Koordinaten dürfen Ausdrücke sein
z = s.zahl(a, "t", (8.6, 1.3), stellen=2, vor="t = ", nach=" s")    # Zahlenanzeige, 1,25 in de
s.einblenden(a); s.zeichnen(k); s.einblenden(d, z)
s.verstellen("t", 6, dauer=6, rate="linear")          # t: 0 -> 6 in 6 s, gleichmäßig
s.speichern()
```

| Aufruf | Was | Hinweis |
|---|---|---|
| `parameter(name, wert, von=None, bis=None, schritt=None, ganzzahlig=False)` | Parameter anlegen (Editor: Objekt „Parameter“ mit Regler) | Ergebnis: id. Name: Buchstaben, Ziffern, `_`; nicht x, y, e, pi, i, j, theta |
| `verstellen(name_oder_id, ziel, dauer=2.0, rate="glatt")` | Animation `ChangeValue` | `ziel` Zahl oder Ausdruck (`"2*pi"`); `rate` `"glatt"` (an- und auslaufend) oder `"linear"`; mehrere in `with s.gleichzeitig():` |
| `zahl(on, ausdruck, pos, stellen=2, vor="", nach="", groesse=TEXT, ausrichtung="left", farbe=SCHWARZ)` | Zahlenanzeige (`DecimalNumber`) | Wert eines Ausdrucks (`"t"`, `"A*exp(-t/tau)"`); Dezimalzeichen und Minus nach Sprache; `vor`/`nach` mit Rich-Text und `@schluessel` |
| `marke(on, x, f="", f2="", y=None, label="", hilfslinien=True, …)` | Punkt mit gestrichelten Projektionen auf beide Achsen (`Marker`) | `x` Zahl oder Ausdruck; mit `f` auf der Kurve, mit `f` und `f2` im Schnittpunkt |
| `tangente(on, f, x0, laenge=1.0, punkt=True, …)` | Tangente an y = f(x) in x0 (`TangentLine`) | `x0="t"` läuft mit |
| `kurve(…, punkte=None)`, `flaeche(…, punkte=120)` | Stützstellen unter einem Parameter | Kurve: Standard 121, etwa 16 je Schwingung genügen; Fläche: etwa 32 |

Was einen Parameter nennen darf:
- **Ausdrücke**: `func`, `func2` (Kurve, Fläche, Marker, Tangente, Stiele), `x_expr`, `y_expr`, `fx`, `fy` (Wege).
- **Zahlen und Koordinaten**: jede Zahl eines Objekts darf ein Ausdruck sein, der einen Parameter nennt: `x_range=(0, "t")`
  (die Kurve wächst), `s.flaeche(a, f, 0, "b")`, `s.linie(a, ("t", -1), ("t", 1))` (Zeitmarker),
  `s.pfeil((0, 0), ("r*cos(phi)", "r*sin(phi)"), on=a)` (Zeiger), `s.kreis(a, 0, 0, "r")`, `s.weg(…, 0, "phi")` (Spur).
  In Koordinatenlisten geht jeder Ausdruck (auch `"2*pi"`), bei einzelnen Zahlen nur einer, der einen Parameter nennt.
- **Ganzzahlig** (`ganzzahlig=True`): n springt 1, 2, 3, …, jede Zahl gleich lang (Folgenglieder, Teilsummen in
  geschlossener Form, `(1 + x/n)^n`).
- **Name t**: Ein Parameter `t` ersetzt in allen Ausdrücken der Szene die Variable t. Graphen dann in x schreiben
  (`sin(x - c*t)`); Wege (`s.weg`) und Polarkurven behalten ihr eigenes t.
- **Mehrere Parameter** laufen gleichzeitig, wenn ihre `verstellen` im selben Schritt stehen (Zeiger: `r` und `phi`).

### 8.2 Zusammenspiel mit anderen Animationen

- Einblenden, Zeichnen, Wachsen, Ausblenden wirken wie gewohnt, auch während der Parameter läuft (Sichtbarkeit und
  Fortschritt kommen von der Animation, die Form vom Parameter).
- Verschieben, Drehen, Skalieren, Betonen und Umformen wirken auf ein Objekt unter einem Parameter nur, solange der
  Parameter auf seinem Startwert steht. Danach bestimmt allein der Parameter die Form. Bewegung also über den
  Parameter ausdrücken, nicht zusätzlich verschieben.
- Ein Objekt, das schon von Anfang an wächst (`weg` von (1, 1,25) bis (1 + t, 1,25)), braucht kein Zeichnen: Es hat
  bei t = 0 die Länge 0. Zeichnen und gleichzeitiges Verstellen ergäbe α·t statt t.

### 8.3 Im Editor

- Parameter anlegen: Katalog „Allgemein · Parameter“ ▸ Parameter (Name, Wert, Reglerbereich, `integer`).
- Animation: den Parameter wählen, unter „Animations“ ▸ Parameter ▸ „+ Verstellen (ChangeValue)“; Felder „to value“
  (Zahl oder Ausdruck) und „rate“ (smooth, linear). Andere Objekte bekommen dieses Menü nicht, ein Parameter keine
  anderen Animationen.
- Hat die Szene einen Parameter, nehmen die Zahlenfelder aller Objekte Ausdrücke an (`t`, `r*cos(phi)`); ein
  Ausdruck ohne Parameter (`2*pi`) wird sofort zur Zahl. Zahlenanzeige: Katalog „Zahlenanzeige“ (`value` = Ausdruck).
- Der Regler setzt den Startwert; ▶ Play rechnet die Animation vorab (Zahnrad) und spielt sie dann flüssig ab.

### 8.4 Größen und Tempo der Vorführszenen

`tools/szenen/beispiel_parameter.py`, exportiert in allen sechs Sprachen (de; Datei gesamt, davon Datenblock):

| Szene | Inhalt | Dauer | .anim.svg | Daten |
|---|---|---:|---:|---:|
| beispiel/anim_l3_welle | laufende Welle, Punkt schwingt am Ort, Wellenberg wandert, t-Anzeige | 8,3 s | 124 KB | 116 KB |
| beispiel/anim_l3_tangente | Punkt auf der Kurve, Tangente, Projektionen, a und f′(a) | 7,6 s | 44 KB | 33 KB |
| beispiel/anim_l3_zeitmarker | Zeitmarker liest u und i ab, drei Anzeigen | 8,3 s | 65 KB | 48 KB |
| beispiel/anim_l3_zeiger | Zeiger dreht sich um 315° und wird kürzer (r, φ zugleich), Spur, Realteil | 6,9 s | 48 KB | 36 KB |
| beispiel/anim_l3_grenzwert | (1 + x/n)^n → e^x, n = 1 … 12 ganzzahlig | 9,8 s | 61 KB | 50 KB |
| beispiel/anim_l3_flaeche | Fläche bis b wächst, A(b) | 7,1 s | 90 KB | 80 KB |

Alle sechs Sprachen sind gleich groß (die Zahlen sind sprachfrei, nur das Dezimalzeichen wechselt). Ohne die
Verdichtung (Pfad-Stufen, volle Textbilder) waren es 265 KB (Welle) und 479 KB (Fläche).

Tempo im Editor (Pyodide in Chromium, gemessen mit Playwright gegen den lokalen Server): ein Bild mit laufendem
Parameter kostet 5,6 ms (Welle), 7,3 ms (Fläche) und 9,3 ms (Zeiger, zwei Parameter, fünf mitlaufende Objekte),
jeweils mit Zeichnen auf die Leinwand; vor dem Parameterlauf 1–2 ms. Das Vorab-Rendern beim Abspielen dauert
1,4–1,8 s für 7–8 s Animation. Eine geringere Vorschau-Bildrate ist nicht nötig.

### 8.5 Export und Grenzen

- **Abtastung**: Unter einem Parameter wird ein Graph an festen Stellen berechnet (121 oder `punkte`) und glatt
  verbunden, eine Fläche ebenso. Jedes Bild hat dieselbe Punktzahl, also wird die Form eine Zahlenspur `q`
  (Toleranz 0,4 Szenenpixel = 0,2 px im Artikel). Zeichnen (Create) davor wird ein Teilstück `p` derselben Form.
  Zahlenanzeigen tragen je Bild nur Lage und Inhalt (die gemeinsamen Attribute stehen an der Gruppe). Der Spieler
  (`build_wissen.py`) ist unverändert.
- **Größe**: Am teuersten ist eine Form, die sich überall ändert (Welle, Fläche): je Schlüsselbild alle Punkte,
  etwa 1,4 KB bei 49 Stützstellen. Daher `punkte` klein halten (16 je Schwingung) und die Welle nicht schneller als
  nötig laufen lassen. Eine Zahlenanzeige kostet etwa 50 Byte je angezeigtem Wert (2 Nachkommastellen über 6 s:
  rund 10 KB). Ziel: unter 150 KB.
- Ändert sich die Zahl der Kurvenstücke (Pol wandert durchs Bild, Wurzel beginnt), wird ein Stück, das dazukommt,
  ein eigenes Element mit Pfad-Stufen (größer, 10 Bilder/s).
- Nicht unter einem Parameter: Achsen (Bereiche, Ticks), MathTex-Formeln, Operationen (Σ, Faltung). Ein Parameter dort
  bleibt beim Startwert.
- Ein Text (`s.text`) kann keinen Parameter enthalten, dafür `s.zahl`.
- Ein Ausdruck, der für einen Wert scheitert, blendet das Objekt in diesem Bild aus; eine Zahlenanzeige zeigt bei
  „keine Zahl“ (z. B. `sqrt(t - 1)` vor t = 1) einen Strich.
- Strichlinien (dash) unter einem Parameter mit Zeichnen davor: Pfad-Stufen statt Teilstück (Strichmuster und
  Teilstück teilen sich `stroke-dasharray`).

## 9. Ebene abbilden (L5, 10.11.2026)

Eine 2×2-Matrix verformt die Ebene über die Zeit: das Koordinatengitter und alles, was mitgenommen wird. Jeder Punkt p
läuft nach A p (wie Manims `ApplyMatrix`), im Endbild steht das Bild. Zwei Abbildungen hintereinander: Die zweite
beginnt beim Bild der ersten. Statisches Bild und PDF zeigen das Endbild.

### 9.1 Aufrufe (`tools/szenen_lib.py`)

```python
s = Szene("ml/k1scherung", reihenfolge="anlegen")
s.welt()
a = s.achsen((-3, 3), (-2, 2), breite=4.8, hoehe=3.2, mitte=(-1.2, 0), kreuz=True, xzahlen=False, yzahlen=False)
g0 = s.gitter(a, 1, farbe="#d5dbe5", rand=0)              # Geistergitter: steht in keinem abbilden, bleibt stehen
g = s.gitter(a, 1, achsen_dicke=3)                        # das Gitter, das sich verformt
e1 = s.vektor(a, (1, 0), label="e_1", farbe=ROT, label_seite="right")
e2 = s.vektor(a, (0, 1), label="e_2", farbe=GRUEN)
q = s.vieleck(a, [(0, 0), (1, 0), (1, 1), (0, 1)], farbe=ORANGE, deckung=0.35)
z = s.zahl(None, "abs(" + det_ausdruck([[1, 1], [0, 1]], "s") + ")", (2, 1), vor="Fläche = ")
s.einblenden(a, g0, g, e1, e2, q, z)
s.abbilden([[1, 1], [0, 1]], [g, e1, e2, q], dauer=2.5, parameter="s")   # s läuft gleich schnell 0 -> 1
s.abbilden([[0, -1], [1, 0]], [g, e1, e2, q], dauer=2, weg="drehung")   # danach: Drehung um 90°
s.speichern()
```

| Aufruf | Was | Hinweis |
|---|---|---|
| `gitter(on, schritt=1, schritt_y=None, farbe, dicke=2, deckung=1, rand=1, punkte=2, achsen_dicke=0, zuschneiden=True, x=None, y=None)` | Koordinatengitter `Grid` im Fenster der Achsen (oder `x`, `y`) | `rand`: so viele Fensterbreiten reichen die Linien über das Fenster hinaus (eine Scherung holt sie herein); jedes Bild wird erst abgebildet, dann am Fenster abgeschnitten. `punkte` > 2 nur für `abbilden_funktion` |
| `vektor(on, ende, start=(0, 0), label="", farbe, …, label_am_ende=True)` | Pfeil (`LabeledArrow`) in Datenkoordinaten | behält beim Abbilden seine Spitze, die Beschriftung bleibt aufrecht |
| `vieleck(on, punkte, farbe=BLAU, deckung=0.25, dicke=3)` | gefülltes Vieleck (`Polygon`) | Einheitsquadrat, Dreieck; in 3D mit (x, y, z), Ausdrücke erlaubt |
| `abbilden(matrix, objekte, dauer=2, weg="gerade", rate="glatt", parameter=None)` | Animation `ApplyMatrix` | `objekte[0]` ist das Ziel, die übrigen werden mitgenommen; Einträge Zahl oder Ausdruck (`"cos(pi/6)"`) |
| `abbilden_funktion(fx, fy, objekte, dauer=2, rate="glatt", parameter=None)` | Animation `ApplyFunction` | jeder Punkt läuft geradlinig nach (fx(x, y), fy(x, y)); Gitter mit `punkte=25`–40 |
| `det_ausdruck(matrix, "s")` | Ausdruck für det((1 − s) I + s A) | für `s.zahl`: Fläche des Bilds des Einheitsquadrats beim Fortschritt s |

- **Mitnehmen** kann man: `Grid`, Punkte (`Dot`, bleiben rund), Pfeile (`LabeledArrow`), Strecken, Texte und
  Zahlenanzeigen (ihr Anker läuft mit), `TextBox`, `Mark`, Vielecke und Rechtecke, Kreise und Ellipsen (ein Kreis wird
  genau zur Ellipse), Funktionsgraphen, Wege, Polarkurven, Flächen, Bänder, Datenkurven, Punktwolken (`PointCloud`,
  jeder Punkt bleibt rund: Matrix auf eine Stichprobe), Klammern. Achsen, Formeln (`MathTex`) und Operationen nicht.
- **Weg**: `"gerade"` (Standard, wie Manim): M(α) = (1 − α) I + α A. Eine Drehmatrix schrumpft dabei zwischendurch, eine
  Spiegelung oder ein Plattdrücken geht durch det = 0. `"drehung"`: A = R(θ)·P (Polarzerlegung), M(α) = R(αθ)·((1 − α) I
  + α P); eine Drehung dreht dann wirklich, und der symmetrische Anteil streckt geradlinig. Nur für det A > 0
  (`szenen_lib` meldet sonst einen Fehler, die Engine nimmt den geraden Weg). θ liegt in (−180°, 180°]: 270° wird −90°.
- **Zahl dazu**: `parameter="s"` legt einen Parameter s an (falls neu, Startwert 0) und verstellt ihn im selben Schritt mit
  derselben Dauer und Rate von 0 auf 1. Jeder Ausdruck mit s läuft also genau mit der Verformung (`det_ausdruck`, eine
  Koordinate des Bildpunkts `"(1-s)*1 + s*3"`). Je Abbildung ein eigener Name; nach zwei Abbildungen ist die Fläche
  det(A₂(s₂))·det A₁.
- **Nichtlinear** (`abbilden_funktion`): Polarkoordinaten fx = `"x*cos(pi*y/2)"`, fy = `"x*sin(pi*y/2)"` machen aus dem
  Rechteck r ∈ [0, 2], u ∈ [0, 4] die Kreisscheibe (Linien r = konst. werden Kreise, u = konst. Strahlen).

### 9.2 Im Editor

- Katalog „Mathematik · Funktionen & Achsen“ ▸ **Grid** (x_step, y_step, extend, samples, clip, axis_width).
- Objekt wählen (Gitter, Pfeil, Vieleck …), unter „Animations“ ▸ **Abbilden** ▸ „+ ApplyMatrix“ oder „+ ApplyFunction“.
  Felder: Matrix (zwei Zeilen „matrix (a b)“, „matrix (c d)“, je Feld Zahl oder Ausdruck), „path“ (gerade / Drehweg),
  „rate“, „mitnehmen“ (Häkchen bei den anderen Objekten); bei ApplyFunction „fx(x, y)“, „fy(x, y)“.
- Vorschau: ▶ wie immer (Vorab-Rendern, dann flüssig).

### 9.3 Größen der Vorführszenen

`tools/szenen/beispiel_gitter.py`, in allen sechs Sprachen exportiert (de; Datei gesamt, davon Datenblock):

| Szene | Inhalt | Dauer | .anim.svg | Daten |
|---|---|---:|---:|---:|
| beispiel/anim_l5_scherung | Gitter, Geistergitter, e₁, e₂ unter (1 1; 0 1) | 5,2 s | 32 KB | 14 KB |
| beispiel/anim_l5_determinante | Einheitsquadrat → Parallelogramm aus (3, 1), (1, 2), Fläche läuft 1,00 → 5,00 | 5,8 s | 68 KB | 29 KB |
| beispiel/anim_l5_eigen | v₁, v₂ bleiben auf ihren Eigengeraden (×5, ×2), w kippt | 6,6 s | 68 KB | 25 KB |
| beispiel/anim_l5_svd | Einheitskreis → Ellipse in drei Schritten Vᵀ (Drehweg), Σ, U (Drehweg); v₁, v₂ → 4u₁, u₂ | 10,1 s | 95 KB | 85 KB |
| beispiel/anim_l5_nacheinander | erst Drehung D (Drehweg), dann Scherung S: Bild S·D | 7,0 s | 74 KB | 51 KB |
| beispiel/anim_l5_polar | nichtlinear: Rechteck → Kreisscheibe (Polarkoordinaten) | 4,6 s | 151 KB | 135 KB |

Ein gerades, nicht abgeschnittenes Teil unter einer Matrix ist in jedem Bild ein affines Bild seines Endbilds: Die
Datei speichert dann nur die Matrix je Schlüsselbild (Spur `m`). Am Fenster abgeschnittene Gitterlinien und gekrümmte
Bilder werden Zahlenspuren `q` (wie L3). Am teuersten ist `abbilden_funktion` (alle Punkte jeder Linie).

### 9.4 Grenzen

- Ein mitgenommenes Objekt läuft wie ein Objekt unter einem Parameter (§8.2): Verschieben, Drehen, Skalieren, Betonen
  und Umformen wirken nur vor der ersten Abbildung; danach bestimmt die Abbildung die Form. Einblenden, Zeichnen und
  Ausblenden wirken immer.
- Die Matrix wird einmal beim Bauen ausgewertet; ein Parameter in einem Eintrag gilt mit seinem Startwert (kein
  „mitlaufender“ Eintrag).
- Logarithmische Achsen: Die Abbildung wirkt in Datenkoordinaten, gerade Linien bleiben dort aber nicht gerade
  (Punkte werden einzeln abgebildet).
- Ein Text, der mitgenommen wird, ändert nur seine Lage, nicht seinen Inhalt; Beschriftungen wie „A e₁“ am Ende als
  eigenes Objekt einblenden. Ein Pfeil mit Beschriftung an der Mitte kann bei einer Drehung die Seite wechseln.
- Achsen (Teilstriche, Zahlen) werden nie abgebildet. Wer die Achsen mitdrehen will, nimmt `achsen_dicke` am Gitter
  und blendet die Achsen aus.
- `Wachsen` (GrowFromCenter) auf einen beschrifteten Pfeil zeigt die Beschriftung schon vorher; `einblenden` nehmen.

## 10. Kamerafahrt in 3D (L4, 10.11.2026)

Die Kamera einer 3D-Szene fährt über die Zeit: drehen um die senkrechte Achse (theta), neigen (phi), zoomen, einen
anderen Blickpunkt anpeilen. Mehrere Fahrten hintereinander, auch gleichzeitig mit anderen Animationen. Statisches
Bild und PDF zeigen die Endstellung der Kamera.

### 10.1 Aufrufe (`tools/szenen_lib.py`)

```python
s = Szene("gemb1/k6bcc", reihenfolge="anlegen")
s.kamera_start(theta=25, phi=18)                  # 3D-Szene, Winkel in Grad, z zeigt nach oben
h = 1.1
ecken = [(x, y, z) for x in (-h, h) for y in (-h, h) for z in (-h, h)]
atome = [s.kugel(None, p, r=0.26, farbe=BLAU) for p in ecken]          # Scheiben, die zur Kamera zeigen
mitte = s.kugel(None, (0, 0, 0), r=0.3, farbe=ORANGE)
diagonale = s.linie(None, (-h, -h, -h), (h, h, h), farbe=ROT, dash=DASH)   # Strecke im Raum (x, y, z)
s.einblenden(*atome, mitte)
s.kamera_kreisen(180, dauer=4)                    # gleichmäßig halb herum
s.kamera(zoom=1.8, dauer=1.2)                     # heran
with s.gleichzeitig():
    s.kamera(theta=315, phi=12, zoom=1.0, dauer=2)  # zurück in eine andere Ansicht ...
    s.zeichnen(diagonale, dauer=2)                  # ... während die Raumdiagonale entsteht
s.speichern()
```

| Aufruf | Was | Hinweis |
|---|---|---|
| `kamera_start(theta=35, phi=20, zoom=1, blickpunkt=None, raum=True)` | Ansicht am Anfang | Grad; `raum=False`: 2D-Szene mit Zoom/Blickpunkt |
| `kamera(theta=None, phi=None, zoom=None, blickpunkt=None, drehen=None, dauer=2, rate="glatt")` | Animation `MoveCamera` | Ziele; was fehlt, bleibt; `drehen` = Grad dazu (360 = einmal herum) |
| `kamera_kreisen(grad=360, dauer=6)` | gleichmäßige Drehung | wie Manims ambient rotation (`rate="linear"`) |
| `achsen3d(x=(-2, 2), y=(-2, 2), z=(0, 2), xl, yl, zl, zahlen=False, pfeile=True)` | räumliche Achsen | Länge = Spanne: Daten- = Weltkoordinaten |
| `flaeche3d(on, f, farbe=BLAU, deckung=0.85, aufloesung=20)` | Fläche z = f(x, y) | `aufloesung` klein halten: jede Zelle ist ein Element |
| `kugel(on, punkt, r=0.2, farbe=BLAU, glanz=True)` | `Ball`: Scheibe zur Kamera mit Lichtfleck | Atom, Punkt im Raum; ein Pfad statt eines Netzes; `punkt` darf Parameter nennen |
| `zuoberst(*ids, stufe=1)` | Prop `layer` | in 3D nach allen niedrigeren Stufen gezeichnet (s. §10.4) |
| `linie`, `text`, `vieleck` | mit (x, y, z) | Koordinaten dürfen Ausdrücke mit Parametern sein |

- Winkel werden als Zahlen gefahren (kein Umweg über 0°): von 25° nach 315° dreht die Kamera um 290°. Der Zoom läuft
  geometrisch (gleichmäßiges Heranfahren), der Blickpunkt geradlinig.
- **Gleichzeitig**: in `with s.gleichzeitig():` mit jeder anderen Animation, auch mit `s.verstellen` (L3 in 3D: ein
  Punkt, eine Tangentialebene, deren Ecken einen Parameter nennen, wandern mit).
- **2D**: `kamera(zoom=…, blickpunkt=…)` geht auch in einer 2D-Szene (Lupe). Linien und Schrift behalten ihre Stärke
  bzw. Größe, Punkte (`Dot`) wachsen mit. Die Achsen verfeinern ihre Teilstriche dabei nicht.
- **Zuschnitt**: Eine Szene mit Kamerafahrt bekommt den Rahmen aller Bilder der Fahrt (gerechnet mit dem Zoom und dem
  Blickpunkt vom Anfang): Beim Drehen wird nichts abgeschnitten, beim Heranzoomen bleibt das Fenster, und der Inhalt
  wird darin größer (was hinausragt, ist abgeschnitten, auch im Endbild). Für ein Endbild ohne Anschnitt zum Schluss
  wieder herauszoomen.

### 10.2 Im Editor

- Szene ▸ „Animations“ ▸ **„+ Kamera bewegen“** legt eine Fahrt an (eine Viertelumdrehung). Ein Klick auf die Zeile
  „MoveCamera · Kamera“ öffnet die Felder: run_time, theta°, phi°, zoom (Ziele, leer = bleibt), drehen°, Blickpunkt
  (Häkchen, dann x, y, z), rate (smooth/linear).
- **„aktuelle Ansicht übernehmen“**: die Ansicht im Editor auf das Ziel ziehen/zoomen, dann klicken. theta, phi und zoom
  werden das Ziel der Fahrt (drehen wird 0), und die Startansicht der Szene kommt zurück.
- Gleichzeitig mit anderen Animationen: über die Schritte (wie bei allen Animationen).
- Katalog „Mathematik · 3D-Körper“ ▸ **Ball** (center, radius, color, highlight).
- Hat die Szene eine Kamerafahrt, malt der Editor Flächen ohne WebGL (die GPU-Ebene folgt nur der festen Kamera).
  Tempo (Pyodide in Chromium, ms je Bild mit Zeichnen): Würfel mit Kugeln 3–4 ms, Fläche mit 20 × 20 Zellen 22–31 ms,
  Fläche mit Tangentialebene und Parameter 28–55 ms; 2D-Gitter (L5) 5–9 ms, Polarkoordinaten-Gitter 18 ms. Bilder über
  20 ms rechnet das Vorab-Rendern mit 20 statt 30 Bildern/s; es dauert für 8–12 s Kamerafahrt 4–8 s (einmal 25 s
  gemessen, das Vorab-Rendern hat je Bild einen festen Aufschlag von 15–25 ms).

### 10.3 Export: Messung und Entscheidung (Weg b)

Gemessen an vorhandenen 3D-Szenen mit einer 6-s-Fahrt (theta +120°, phi +14°, glatt; in Klammern volle Drehung 360°,
linear), Größe der `.anim.svg` (de):

| Szene | statisch | (a) projizierte Pfade, 30 Bilder/s, 0,2 px | (a) grob: 15 Bilder/s, 1 px | (b) Spieler projiziert |
|---|---:|---:|---:|---:|
| hm1/k8norm (klein) | 6 KB | 43 KB (85 KB) | 23 KB (43 KB) | 9 KB (8 KB) |
| hm1/k9kreuz | 10 KB | 109 KB (226 KB) | 56 KB | 16 KB (14 KB) |
| gemb1/k6miller | 19 KB | 283 KB (465 KB) | 140 KB | 31 KB (26 KB) |
| gemb1/k6kubisch (157 Elemente) | 100 KB | 473 KB (810 KB) | 271 KB (419 KB) | 150 KB (146 KB) |
| et1/k10flaeche (2071 Facetten) | 617 KB | 9,5 MB | – | 873 KB (871 KB) |

- (a) (heutiger Exporter: je Element eine Matrix- oder Punktspur in Bildkoordinaten) schafft das Ziel nur für kleine
  Szenen und kurze Schwenks und kann die Zeichenreihenfolge nicht ändern (Rückseiten lägen vorn).
- **(b) ist gebaut**: Die Datei trägt je Element seine Weltpunkte (`w`; bei nur geraden Stücken nur die Ecken, `wl`),
  eine Kamera-Spur (`cam`: theta, phi, zoom, Blickpunkt, linear zwischen Schlüsselbildern, Fehler ≤ 0,2 Szenenpixel)
  und die Projektionskonstanten (`pj`). Der Spieler (`build_wissen.py`, WISSEN_JS) projiziert jedes Bild wie
  `engine/camera.py` und baut daraus den Pfad. Die Größe hängt nicht von der Länge der Fahrt ab; sie ist etwa das
  statische Bild plus ein Drittel. Ändern sich die Weltpunkte selbst (Parameter, Zeichnen), kommen Spuren `Q` (gleiche
  Punktzahl, linear) oder `D` (Stufe, 10 Bilder/s) dazu; Stil-Spuren (Deckkraft, Farbe, Sichtbarkeit) wie bisher.
- **Zeichenreihenfolge**: Der Spieler sortiert in jedem Bild wie `engine/renderer._paint_3d`: Tiefe = Mittel der Tiefe
  aller Punkte eines Elements, hinten zuerst; bei `axes_on_top` die Achsen zuletzt; Stufen (`layer`, `ly`) vor der
  Tiefe; bei gleicher Tiefe die Reihenfolge des Szenenbaums (`r`). Ändert sich die Reihenfolge, hängt er die Elemente
  um. Treue gegen das Bild der Engine zur selben Zeit (Kontrollbilder zu 0, 25, 50, 75, 100 %): höchstens 0,8 %
  abweichende Pixel (Kantenglättung), auch für die Szenen oben, deren Reihenfolge sich beim Drehen ändert.
- Szenen ohne Kamerafahrt (auch 3D mit fester Kamera) exportieren unverändert wie bisher.

### 10.4 Größen der Vorführszenen

`tools/szenen/beispiel_kamera.py`, in allen sechs Sprachen exportiert (de):

| Szene | Inhalt | Dauer | .anim.svg | Daten |
|---|---|---:|---:|---:|
| beispiel/anim_l4_flaeche | Fläche z = 1 + sin x cos y / 1,3 mit Achsen: 150° herum, dann von oben | 8,5 s | 178 KB | 48 KB |
| beispiel/anim_l4_kristall | bcc-Zelle mit `kugel`: halb herum, Zoom auf das Zentrum, zurück quer zur Raumdiagonale (gleichzeitig gezeichnet) | 9,4 s | 21 KB | 14 KB |
| beispiel/anim_l4_ebene | Kuppel mit Tangentialebene: Drehung während Ebene und P erscheinen, P wandert (Parameter a) bei weiterer Drehung, Zoom auf P, zurück | 10,4 s | 251 KB | 142 KB |

### 10.5 Grenzen

- **Maler-Algorithmus**: Jedes Element (Facette, Linie, Text) hat eine Tiefe; sich durchdringende oder sehr
  unterschiedlich große Teile können falsch liegen (eine große Ebene über kleinen Facetten wird stückweise verdeckt).
  Abhilfe: `s.zuoberst(...)` (Prop `layer`), wenn das Teil aus allen gezeigten Richtungen davor liegt (Tangentialebene
  über einer Kuppel), sonst das große Teil in kleine Stücke teilen.
- `Sphere` ist ein Netz aus Facetten (je Kugel 50–300 Elemente, flach eingefärbt); für Atome und Punkte `Ball`
  (`s.kugel`) nehmen: 1–2 Elemente, rund aus jeder Richtung. Ein `Dot` liegt in 3D flach in der x-y-Ebene.
- Vorhandene 3D-Szenen (gemb1, hm1) sind für eine feste Kamera gebaut: Atome als Scheiben zur Kamera, Pfeilspitzen in
  der Bildebene, Teilbilder nebeneinander in der Bildebene. Eine Kamerafahrt darin sieht falsch aus; solche Szenen
  mit `kugel`, `linie` (3D) und einer gemeinsamen Mitte neu aufbauen.
- Pfeile (`Vector` 3D) haben eine Kegelspitze aus Facetten (gut); `LabeledArrow` hat eine flache Spitze in der
  x-y-Ebene (in 3D nur von oben richtig).
- Text bleibt immer aufrecht und gleich groß (auch beim Zoom).
- Flächen mit vielen Zellen machen die Datei groß (jede Zelle ist ein Element mit Weltpunkten): et1/k10flaeche
  (2071 Facetten) hat statisch schon 617 KB, mit Fahrt 873 KB. `aufloesung` 15–24 genügt meist.
- Mittelpunktsmarken (`show_center`) bewegen sich bei einer Fahrt nicht mit.

## 11. Bildschirme und Fenster (F1, 12.11.2026)

Terminal, Datei-Ansicht, Vollbild-Programme (`top`, Pager wie bei `systemctl status`) und Zeichenraster mit
Spalten-Funktionen. Plan und Bedarf: `notizen/editor_bildschirme_plan.md`, `notizen/f1_funktionsliste.md`. Farben und
Maße: `notizen/f1_terminal_palette.md`. Beispiele: `tools/szenen/linux_f1_pilot.py` (`linux/k2sitzungen_f1`,
`linux/k4cateingabe_f1`, `linux/k6awkfelder_f1`, `beispiel/anim_f1_top`, `beispiel/anim_f1_pager`).

Was es gibt:
- **Ein Fenster ist ein Objekt** der Engine (Typ `Terminal`, `web/engine/terminal.py`). Es zerfällt beim Zeichnen in
  Pfade (Rahmen, Titelleiste, Knöpfe, Hinterlegungen, Cursor) und Texte. Editor, Export, `.anim.svg`, PDF und Spieler
  brauchen keinen neuen Weg.
- **Eine Bildschirmzeile ist ein `<text>`** mit farbigen `<tspan>`-Abschnitten (Text-Attribut `spans`), nie ein
  Objekt je Zeichen. Jedes Zeichen sitzt in seiner Zelle von 0,6 em: Spalten, Rahmen- und Baumzeichen (`─ │ └─ ├─ ●`)
  stehen exakt untereinander, in jeder Schreibmaschinenschrift.
- **Stil:** dunkel, an Ubuntu angelehnt. Titelleiste mit Titel und drei runden Knöpfen (– □ ×). Der Prompt am
  Zeilenanfang (`student@labor:~$ `) bekommt die Farben der Standard-`.bashrc`. Die Datei-Ansicht ist hell, mit
  Dateiname als Titel und nur ×.
- **Inhalt = Datenstrom wie bei einem echten Terminal**, mit ANSI-Kürzeln als `\e[…` (Farben, fett, invers,
  Cursor-Stellung, Leeren). Er ist in allen Sprachen gleich.
- **Zustände sind Schritte der Zeitachse:** tippen, Ausgabe, neuer Prompt, warten (Cursor blinkt), leeren, Wert
  wechselt, Fenster schließen. Rollen geschieht von selbst, sobald das Fenster voll ist.
- **Raster ohne Fenster** (`s.raster`): Zeilen in Schreibmaschinenschrift, eine `s.text` je Zeile, mit denselben
  Spalten-Funktionen. Sie ersetzen `tt`, `ttz`, `sp`, `msp`, `mark` und `klammer` aus `linux_hilfen.py`.

### 11.1 Raster: Zeilen zerlegen (`s.raster`)

```python
s = Szene("linux/k7passwd", reihenfolge="anlegen")        # "anlegen": Hinterlegungen liegen unter dem Text
g = s.raster("student:x:1000:1000:Student:/home/student:/bin/bash", (0, 0.3), groesse=24, ausrichtung="mitte")
punkte = [g.markieren(0, k, k, ORANGE, 0.4) for k in g.trenner(0, ":")]    # Doppelpunkte hinterlegen
leuchten = [g.teil(0, k, k) for k in g.trenner(0, ":")]                     # Kopien, die einzeln leuchten
kl = [g.klammer(0, f.a, f.b, "UID" if j == 2 else "", seite="oben") for j, f in enumerate(g.felder(0, ":"))]
f4 = g.felder(0, ":")[3]                                  # Feld 4 (GID): Spalten f4.a..f4.b
pf = s.pfeil((g.xm(f4.a, f4.b), g.unten(0) - 0.6), g.anker(0, f4.a, f4.b, "unten"))   # Pfeil von unten auf Feld 4
s.einblenden(*g.ids)
schritt(s, EIN(punkte), BETONE(leuchten))                 # schritt/EIN/BETONE aus linux_hilfen
s.zeichnen(pf)
s.speichern()
```

| Aufruf | Ergebnis |
|---|---|
| `s.raster(zeilen, pos, groesse=20, ausrichtung="links", zeilenabstand=1.35, farbe=SCHWARZ, ansi=None)` | `Raster`; `zeilen` Text mit `\n` oder Liste; `pos` = linke Kante von Spalte 0 und Mitte von Zeile 0 (`"links"`) oder Mitte des Blocks (`"mitte"`); ANSI-Kürzel färben Abschnitte (`farbig`) |
| `g.ids`, `g.zeile(z)` | ids der Zeilen (einzeln animierbar) |
| `g.x(sp)`, `g.xr(sp)`, `g.xm(a, b)`, `g.y(z)`, `g.oben(z)`, `g.unten(z)`, `g.zelle`, `g.links`, `g.rechts` | Kanten und Mitten in Szeneneinheiten (Zeile und Spalte ab 0, a..b einschließlich) |
| `g.anker(z, a=None, b=None, seite="mitte")` | Punkt für Pfeile: `mitte`, `oben`, `unten`, `links`, `rechts`, `oben_links` … (ohne a: ganze Zeile) |
| `g.felder(z, trenner=None)` | `[Feld(a, b, text)]`: durch Leerraum oder an jedem `trenner` getrennt, leere Felder inklusive |
| `g.trenner(z, ":")`, `g.finde(z, muster, n=1, regex=False)` | Spalten der Trennzeichen; `(a, b)` des n-ten Treffers |
| `g.markieren(z, a, b, farbe=ORANGE, deckung=0.3, bis=None)` | Hinterlegung über die Zeilen z..bis, beim Raster **unter** dem Text |
| `g.rahmen(z, a, b, farbe=ORANGE, dicke=2.5, bis=None)` | abgerundeter Umriss |
| `g.klammer(z, a, b, text="", seite="oben", farbe=BLAU, groesse=18, schrift=None)` | eckige Klammer (ein offener Linienzug, `zeichnen` geht) und Beschriftung; `(id, id_text)` |
| `g.teil(z, a, b, farbe=None)` | deckungsgleiche Kopie der Spalten a..b: wandert (`verschieben`, `bewegen_zu`), leuchtet (`betonen`), wird ersetzt |
| `g.wert(z, a, b, neu, farbe=None)` | Wert wechselt an fester Spalte (Zeile behält eine Lücke, der Teil wird `neu`); `(id_teil, id_animation)` |
| `g.faerben(z, [(a, b, farbe)], rest=GRAU)` | Zeile neu einfärben, z. B. „Rest grau“ (Animation, `s.ersetzen` mit ANSI) |

`s.text(..., ansi=True)` färbt einen einzelnen Text mit ANSI-Kürzeln (helle Palette, für die weiße Seite).

### 11.2 Terminal und Abläufe (`s.terminal`)

```python
s = Szene("linux/k8journalfolgen", reihenfolge="anlegen")
t = s.terminal(pos=(-3.45, 1.9), spalten=60, zeilen=7, titel="student@labor: ~/linuxk8")   # Größe fest: Anker
#                                                         # gelten für jeden Zustand; Prompt student@labor:~$ , dunkel
s.einblenden(t.id)                                        # oder s.wachsen(t.id): Fenster öffnet sich
t.eingabe("journalctl --user -f -u eieruhr")              # tippen (14 Zeichen/s), Eingabetaste
t.ausgabe("Nov 10 15:29:25 labor eieruhr[654]: Eieruhr zum Üben")       # Zeile erscheint
t.warten(1.2)                                             # Cursor blinkt dreimal
u = s.terminal(pos=(-3.45, -0.4), spalten=52, zeilen=3)
u.befehl("systemctl --user restart eieruhr")              # tippen, dann Ausgabe + neuer Prompt
pf = s.pfeil(u.anker(0, seite="links"), t.anker(2, seite="links"), knick="hv")
with s.gleichzeitig():                                    # zwei Fenster: ein Schritt
    t.ausgabe("Nov 10 15:29:31 labor systemd[512]: Stopping …", zeilenweise=True)
    s.einblenden(pf)
t.ausgabe(farbig("^C", "gelb"))                           # Strg+C, dann wieder die Eingabeaufforderung
t.prompt(pfad="~/linuxk8")
with s.gleichzeitig():
    t.schliessen()                                        # × leuchtet, Fenster blendet aus (fehlt im Endbild)
    s.ausblenden(pf)
s.speichern()
```

| Aufruf | Was |
|---|---|
| `s.terminal(text=None, pos=(-3.4, 1.6), spalten=0, zeilen=0, titel=None, prompt="student@labor:~$ ", groesse=None, stil="dunkel", rahmen="fenster", knoepfe="drei", cursor=True, farbprompt=True, max_breite=6.9)` | `pos` = linke obere Ecke. `spalten`/`zeilen` 0 = so viel, wie über alle Zustände nötig ist. `titel` None = `user@host: ~` aus dem Prompt. `text` = Anfangsinhalt (None: nur der Prompt). `groesse` None = 20 px oder kleiner, bis das Fenster höchstens `max_breite` breit ist. `rahmen`: fenster, datei, ohne; `knoepfe`: drei, x, keine; `stil`: dunkel, hell |
| `t.eingabe(befehl, tempo=14, enter=True)`, `t.tippen(text)` | ein Schritt: Zeichen für Zeichen, Cursor läuft mit |
| `t.ausgabe(text, zeilenweise=False, dauer=0.6)` | Zeilen erscheinen (ANSI erlaubt); zeilenweise = je Zeile ein Schritt |
| `t.prompt(pfad=None, root=False)` | neue Eingabeaufforderung, z. B. nach `cd`: `pfad="/etc"`; `root=True` gibt `#` |
| `t.befehl(befehl, ausgabe="", pfad=None)` | zwei Schritte: tippen; Ausgabe + neuer Prompt |
| `t.warten(1.2)`, `t.leeren()`, `t.schliessen(1.0)` | Cursor blinkt; `clear`; Fenster schließen |
| `t.setze(z, sp, text)` oder `t.setze([(z, sp, text), …])` | Wert wechselt an fester Stelle (Cursor bleibt, wo er war) |
| `t.schritt(roh, dauer=0.6)` | beliebiger Schritt: Text, `\e[…`-Kürzel, `\e>` (ab hier getippt), `\e~` (warten) |
| Spalten-Funktionen wie beim Raster | `x`, `xm`, `y`, `anker`, `felder`, `finde`, `markieren`, `rahmen`, `klammer`, `teil` auf den Bildschirmzellen (Zeile 0 = oberste Bildschirmzeile; `felder(z)` liest den Endzustand, `zeilen(zustand)` jeden anderen). Overlays liegen über dem Fenster; `teil` übernimmt Farben und Fettschrift |
| `t.links`, `t.rechts`, `t.oben_kante`, `t.unten_kante`, `t.mitte`, `t.groesse`, `t.titel_anker`, `t.kreuz_anker()` | Fensterkanten und -mitten |
| `s.datei(name, inhalt, pos, …)` | Datei-Ansicht (hell, Titel = Dateiname, nur ×, kein Cursor); `zeile_dazu(text)` = eine Zeile kommt hinzu |
| `s.top(kopf, tabelle, pos, spalten=0)` | `top`: Kopf (Zahlen fett), Leerzeile, Spaltenzeile invers über die ganze Breite, Prozesse (zu lange Zeilen enden mit `+`). `bild(kopf=…, tabelle=…)` = nächstes Bild; nur geänderte Zeilen werden neu geschrieben |
| `s.pager(zeilen, pos, sichtbar=None, status=None)` | Pager: sichtbare Zeilen, darunter die Statuszeile invers (`lines 1-8/11`, am Ende `(END)`); `weiter(n)` blättert (n < 0 zurück) |
| `s.schloss(mitte, groesse=0.3, offen=False, farbe=GRAU)` | kleines neutrales Schloss (Objekt `Lock`) |
| `farbig(text, farbe, fett=False)`, `fett(text)`, `invers(text)` | ANSI-Kürzel: `farbe` = rot, gruen, gelb, blau, magenta, cyan, weiss, grau, schwarz oder eine Abbildungsfarbe (`ORANGE`, 24 Bit) |

Regeln:
- **Jeder Ablauf-Aufruf ist ein Schritt** (ChangeValue auf einen eigenen Parameter `term1`, `term2` …, Rate linear).
  Er steht in `with s.gleichzeitig():` mit anderen Animationen zusammen. Zwei Schritte **desselben** Terminals dürfen
  nicht im selben Schritt stehen.
- **Anker hängen an der Fenstergröße.** Bei `spalten`/`zeilen` = 0 wächst das Fenster mit jedem Schritt, der eine
  längere Zeile bringt. Deshalb Größe fest setzen oder Anker erst nach dem letzten Schritt abfragen. `speichern()` und
  der nächste Schritt melden einen Fehler, wenn sich die Größe nach einer Ankerabfrage geändert hat.
- **Größe in der Artikelspalte:** zwei Fenster nebeneinander je höchstens 38 Spalten bei 17 px. Eines über die ganze
  Breite fasst 84 Spalten (18 px). Darunter warnt `szenen_lib`.
- **Wachsen, Einblenden, Ausblenden** gehen wie bei jedem Objekt. Verschieben, Skalieren und Betonen wirken auf ein
  Terminal mit Zeitachse nur vor seinem ersten Schritt (§8.2). Bewegen lässt man Kopien (`teil`) oder Beschriftungen.
- **`teil` und `felder` lesen den Bildschirm beim Aufruf**, also den Stand nach den bis dahin angelegten Schritten.
  Eine Kopie von getipptem Text deshalb erst nach `eingabe`/`tippen` anlegen. Sind die Zellen noch leer, meldet `teil`
  einen Fehler. Objekte dürfen jederzeit angelegt werden; ihre Animationen stehen trotzdem an der richtigen Stelle.
- **Dunkler Text auf weißer Seite:** `teil` aus einem dunklen Fenster ist hell. Wandert der Teil aus dem Fenster, dann
  `farbe=SCHWARZ` setzen oder eine Karte darunterlegen (Muster in `k4cateingabe_f1`).

### 11.3 Der Datenstrom (Prop `text`, auch im Editor)

| Zeichen | Bedeutung |
|---|---|
| Text, Zeilenumbruch | wie im Terminal; ein Umbruch geht an den Zeilenanfang. Bei festen `spalten` bricht eine lange Zeile um, bei festen `zeilen` rollt das Fenster |
| `\e[1;32m … \e[0m` | ANSI-SGR: 0 zurück, 1 fett, 2 blass, 7 invers, 30–37/90–97 Farbe, 40–47/100–107 Hintergrund, 38;5;n, 38;2;r;g;b |
| `\e[r;cH`, `\e[2J`, `\e[K`, `\e[s`/`\e[u`, `\e[?25l`/`\e[?25h` | Cursor an Zeile r, Spalte c (ab 1); Bildschirm bzw. Zeilenrest leeren; Cursor sichern/zurück; Cursor aus/an |
| `\e\|` | **neuer Zustand** (Schritt). Zustand 0 ist alles vor der ersten Marke |
| `\e>` | ab hier bis zum Ende des Schritts **getippt** (Zeichen für Zeichen über die Dauer des Schritts) |
| `\e~` | in diesem Schritt **wartet** der Cursor (blinkt dreimal) |
| `\e!` | das **Fenster schließt** (× leuchtet, dann blendet alles aus) |
| `\\` | ein Backslash (nur nötig vor einem `e`; `C:\` und `grep '\w'` bleiben, wie sie sind) |

Prop `state`: Zahl oder Name eines Parameters. k zeigt die Schritte 0..k, zwischen k−1 und k läuft Schritt k. Leer =
Endzustand. Ein Terminal ohne Zeitachse braucht kein `state`.

### 11.4 Im Editor

- Palette **„Bildschirm & Fenster“**: Terminal, Datei-Ansicht, TUI: top, TUI: Pager, Textblock (Text in
  Schreibmaschinenschrift mit `ansi`), Schloss. Ein Bildschirm schaltet eine 3D-Ansicht auf 2D um.
- Eigenschaften:
  - `text` ist ein Textfeld (Datenstrom wie oben);
  - Auswahllisten für `frame`, `theme` und `buttons`;
  - `cols`/`rows` 0 = nach Bedarf.
- **„Zustände als Schritte anlegen“** (unter den Eigenschaften):
  - legt bei Bedarf den Parameter `term1` an und trägt ihn in `state` ein;
  - schreibt je Marke `\e|` einen ChangeValue-Schritt (linear) und ersetzt dabei vorhandene Schritte;
  - Dauer: getippt 14 Zeichen/s (mindestens 0,5 s), warten 1,2 s, schließen 1 s, sonst 0,6 s;
  - der Hinweis darüber zählt die Zustände.
- Der Regler des Parameters zeigt jeden Zustand. Die Bearbeitungsansicht zeigt den Startwert (Zustand 0), ▶ spielt ab.
- Eine Farbe ist jetzt genau `#rrggbb`. Ein Text, der mit `#` beginnt (`#!/bin/bash`, Kommentarzeile, root-Prompt),
  bleibt Text (`editor.js` `isHexColor`, `export_szenen._to_args`).

### 11.5 Export

- `export_szenen.py --animiert` wie immer. Getippter Text und wechselnde Zeilen werden Inhaltsspuren `h` je Zeile, der
  Cursor eine Matrixspur, Blinken eine Deckkraftspur.
- **Mindestschrift:** Jede Szene meldet „Schrift zu klein: o19 hat 16,0 Szenenpixel → 8,80 px im Artikel“, wenn ein
  sichtbarer Text unter 9,3 px im Artikel landet (Szenenpixel × 0,55 × Verkleinerung bei Bildern über 548 px). Das gilt
  für alle Szenen, nicht nur für Fenster.
- Größe:
  - Ein Terminal mit 80 × 24 voll beschriebenen Zeilen hat statisch etwa 20 KB.
  - Mit Farben und Hinterlegungen in jeder Zeile sind es etwa 25 KB (Test `web/tests/test_f1_terminal.py`, Budget
    100 KB).
  - Ein wachsendes Fenster kostet je Pfad eine Matrixspur. Einblenden ist billiger.
- PDF (`szenen_pdf.py`): Zeilen sind echter, durchsuchbarer Text mit Farben.

### 11.6 Pilot (12.11.2026)

| Szene | Code (Hand → F1) | Spaltenrechnung von Hand | `.svg` | `.anim.svg` |
|---|---:|---:|---:|---:|
| `linux/k2sitzungen` → `_f1` | 33 → 26 Zeilen | 7 → 0 | 111 → 10 KB | 136 → 41 KB |
| `linux/k4cateingabe` → `_f1` | 47 → 51 Zeilen | 6 → 1 | 77 → 20 KB | 114 → 50 KB |
| `linux/k6awkfelder` → `_f1` | 44 → 41 Zeilen | 21 → 1 | 11 → 9 KB | 20 → 15 KB |

Code = Zeilen ohne Docstring, Leer- und Kommentarzeilen; de und en sind gleich groß.

- Die Größe sinkt bei k2 und k4 vor allem, weil Formel-tt wegfällt.
- Der eigentliche Gewinn von F1 liegt bei k6: Es gibt keine Spaltenrechnung von Hand mehr (`sp`, `msp`, `cw`), und
  die Spalten stimmen per Konstruktion.
- Dazu kommen ein echtes Fenster, Tippen mit Cursor und Prompt-Farben.
- Vorführszenen: `beispiel/anim_f1_top` (16 / 31 KB), `beispiel/anim_f1_pager` (11 / 18 KB).
- Kontaktblatt und Messwerte liegen beim Bau-Bericht.

### 11.7 Grenzen und Vorrat

- Kein Unterstreichen, keine 256-Farben-Hintergründe im Text-Objekt (`ansi=True` färbt nur die Schrift; Hinterlegung
  und invers gibt es im Terminal).
- Nicht gebaut (Vorrat laut Plan): Mitschrift-Import, Kürzen mit `…` (für `k8journalfolgen` nicht mehr nötig),
  Tastenkappen, Maus, Lupe, Ausschnitt, Stile Windows/macOS, `nano` und Dialoge (F3).
- Ein Terminal mit Zeitachse wird in jedem Bild neu gebaut (L3). Das kostet im Editor wenige Millisekunden je Bild.

### 11.8 Tests

Aus `web/`:
- `python tests/test_f1_terminal.py`: Engine (ANSI, Datenstrom, Zustände, Zeichnen, Canvas wie SVG, Vertrag, Budget).
- `python tests/test_f1_bausteine.py`: je Baustein Export = Editor; die Umwandlung aus `editor.js` läuft in node.
- `python tests/test_f1_szenen_api.py`: `szenen_lib`, Anker gegen gezeichnete Zellen.
- `test_contract.py` hat zwei F1-Fälle.

Im Browser: `python tools/editor_terminal_test.py <ordner> [http://localhost:8000/editor.html]` (Palette, Inhalt
ändern, Zustände als Schritte, abspielen, PNG-Export).
