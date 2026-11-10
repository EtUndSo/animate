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
Zeit (§8) `tools/szenen/beispiel_parameter.py` (Szenen `beispiel/anim_l3_*`).

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
| beispiel/anim_esb | Schaltung (ET1) | 8,4 s | 42 KB | 24 KB | 17 KB |
| beispiel/anim_norm | 3D, feste Kamera | 6,1 s | 23 KB | 17 KB | 6 KB |
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
- **L4 (Kamerafahrt in 3D)** gibt es nicht. Die Kamera ist fest, 3D-Szenen animieren nur ihre Objekte. Eine
  Kamerafahrt änderte jeden Pfad in jedem Bild. Bei 30 Bildern/s kostete sie ein Vielfaches der heutigen Dateigröße:
  Schon das 6-KB-Bild `hm1/k8norm` käme bei 6 s auf etwa 150–300 KB, Flächen mit vielen Facetten auf mehrere MB. Dafür
  bräuchte es einen Spieler, der selbst projiziert (3D-Daten statt Pfaden). Das ist nicht gebaut.
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
  kommt die feste Zeichenreihenfolge dazu.

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
| beispiel/anim_l3_grenzwert | (1 + x/n)^n → e^x, n = 1 … 12 ganzzahlig | 10,4 s | 61 KB | 50 KB |
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
