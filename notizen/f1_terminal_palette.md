# F1: Farben und Maße der Fenster (12.11.2026)

Festgelegt für `web/engine/ansi.py` (`PALETTES`) und `web/engine/terminal.py`. Diese Tabelle und der Code müssen
übereinstimmen; `web/tests/test_f1_terminal.py` prüft den Kontrast.

## Entscheidung des Users
Alte und neue Terminalbilder sind dunkel und an echtes Ubuntu angelehnt:
- dunkler Hintergrund;
- Titelleiste mit Titel (`student@labor: ~`) und drei Fensterknöpfen rechts wie bei GNOME;
- Prompt in den Farben der Standard-`.bashrc`;
- keine Logos, keine Originalgrafiken, keine Markennamen.

## Grundsätze
1. **Werte aus der Standardpalette von GNOME-Terminal**, also der Palette, die das Terminal von Ubuntu
   heute mitbringt. Damit wirken Prompt, `ls --color` und `systemctl status` sofort vertraut.
2. **Lesbar im Artikel:** Schreibmaschinenschrift steht dort mit 9,4–11 px. Jede Textfarbe hat deshalb mindestens
   4,5 : 1 Kontrast zum Hintergrund (WCAG AA). Die Originalwerte von Rot, Gelb, Blau, Magenta und hellem Schwarz
   liegen darunter (Blau `#12488b` nur 1,8 : 1). Sie sind im gleichen Farbton aufgehellt.
3. **Fett = hell:** Fette Schrift mit Farbe 30–37 nimmt die helle Variante 90–97, wie bei der Einstellung
   „fette Schrift in hellen Farben“. So leuchten `user@host` (grün) und der Pfad (blau) im Prompt wie gewohnt.
4. **Kein Markenzeichen:** neutraler, fast schwarzer Hintergrund statt Aubergine. Der Schließen-Knopf ist grau statt
   orange, alle drei Knöpfe sind runde graue Flächen mit Strichsymbol.
5. **Hell** für die Datei-Ansicht (wie ein Texteditor) und für `Text(ansi=True)` auf der weißen Seite: dieselben
   Farbtöne, abgedunkelt auf mindestens 4,5 : 1 zu Weiß.

## Fensterteile
| Teil | dunkel | hell | Grund |
|---|---|---|---|
| Hintergrund des Bildschirms | `#1e1e1e` | `#ffffff` | Dunkelgrau wie die Inhaltsfläche dunkler GNOME-Anwendungen, kein Markenton |
| Vordergrund (Standardtext) | `#d0cfcc` | `#1e1e1e` | GNOME-Weiß (Farbe 7), 10,7 : 1 |
| Cursor (Block) | `#d0cfcc` | `#1e1e1e` | wie der Text; ein Zeichen darunter erscheint in Hintergrundfarbe |
| Titelleiste | `#303030` | `#ebebeb` | Kopfleiste dunkler bzw. heller GNOME-Fenster |
| Titeltext (fett, 0,85 em, mindestens 17 px) | `#f2f2f2` | `#2e2e2e` | |
| Trennlinie unter der Titelleiste | – | `#d6d6d6` | im hellen Stil sonst kaum Grenze |
| Rahmen des Fensters (1,2 px) | `#0f0f0f` | `#c4c4c4` | hebt das Fenster vom Weiß der Seite ab |
| Knopf (Kreis) | `#474747` | `#d6d6d6` | entspricht Weiß bzw. Schwarz mit 10 % Deckkraft über der Titelleiste |
| Symbol im Knopf (–, □, ×) | `#f0f0f0` | `#2e2e2e` | |
| Schließen beim Schließen | `#c01c28`, × weiß | dasselbe | GNOME-Rot: zeigt „dieser Knopf wird gedrückt“ |
| Schatten | Schwarz, 10 % und 5 % | dasselbe | zwei weiche Ringe (2 und 5 px), kein Unschärfefilter (SVG im `<img>`, PDF) |

## 16 Farben (Vordergrund 30–37 / 90–97, Hintergrund 40–47 / 100–107)
Kontrast zum Hintergrund des jeweiligen Stils in Klammern.

| Nr. | Name | GNOME | dunkel | hell |
|---:|---|---|---|---|
| 0 | Schwarz | `#171421` | `#171421` (Hintergrundton) | `#1e1e1e` |
| 1 | Rot | `#c01c28` (2,7) | `#ef5350` (4,8) | `#c01c28` (6,1) |
| 2 | Grün | `#26a269` | `#26a269` (5,1) | `#1b7f45` (5,0) |
| 3 | Gelb/Braun | `#a2734c` (4,0) | `#c28a52` (5,6) | `#8a5a1f` (5,9) |
| 4 | Blau | `#12488b` (1,8) | `#4a8fe8` (5,1) | `#1d4fa8` (7,7) |
| 5 | Magenta | `#a347ba` (3,3) | `#c061cb` (4,6) | `#8b3aa0` (6,5) |
| 6 | Cyan | `#2aa1b3` | `#2aa1b3` (5,4) | `#16768a` (5,3) |
| 7 | Weiß | `#d0cfcc` | `#d0cfcc` (10,7) | `#5e5c64` (6,6) |
| 8 | helles Schwarz (grau) | `#5e5c64` (2,5) | `#8a8990` (4,8) | `#77767b` (4,5) |
| 9 | helles Rot | `#f66151` | `#f66151` (5,4) | `#c01c28` |
| 10 | helles Grün | `#33da7a` | `#33da7a` (9,1) | `#1b7f45` |
| 11 | helles Gelb | `#e9ad0c` | `#e9ad0c` (8,3) | `#8a5a1f` |
| 12 | helles Blau | `#2a7bde` (4,0) | `#5ea1f0` (6,2) | `#1d4fa8` |
| 13 | helles Magenta | `#c061cb` | `#d27bdc` (6,0) | `#8b3aa0` |
| 14 | helles Cyan | `#33c7de` | `#33c7de` (8,2) | `#16768a` |
| 15 | helles Weiß | `#ffffff` | `#ffffff` | `#1e1e1e` |

- Farben 16–255 (`\e[38;5;n m`) wie bei xterm: Würfel 6 × 6 × 6 und Graustufen.
- 24 Bit (`\e[38;2;r;g;b m`) unverändert. `farbig(text, ORANGE)` in `szenen_lib` färbt so mit den Farben der
  Abbildungen.
- `invers` (7) tauscht Vorder- und Hintergrund. Die Zelle bekommt dann eine Hinterlegung in der Textfarbe, etwa für
  die Spaltenzeile von `top` oder die Statuszeile eines Pagers.
- `faint` (2) mischt die Textfarbe zu 40 % mit dem Hintergrund.

## Prompt (Standard-`.bashrc`)
`\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ `. Steht am Zeilenanfang `user@host:pfad$ `
oder `#`, setzt das Terminal die Farben selbst (Prop `prompt_colors`, Standard an):

| Teil | Farbe |
|---|---|
| `user@host` | fett grün, also `#33da7a` (fett = hell) |
| `:` | Standardtext |
| Pfad | fett blau, also `#5ea1f0` |
| `$ ` bzw. `# ` | Standardtext |

## Maße (in em der Terminalschrift; 20 Szenenpixel ergeben 11 px im Artikel)
| Maß | Wert | Grund |
|---|---|---|
| Zelle | 0,6 em breit (wie `s.text(schrift="tt")`) | Spalten exakt, Rahmen- und Blockzeichen im Raster |
| Zeilenabstand | 1,2 em | Zellen etwa doppelt so hoch wie breit, wie im echten Terminal |
| Innenabstand | 0,6 em links/rechts (eine Zelle), 0,45 em oben/unten | |
| Titelleiste | 2 em hoch | GNOME hat etwa die dreifache Schriftgröße; für Abbildungen gestaucht |
| Knöpfe | Durchmesser 0,55 × Titelleiste, Abstand 0,2 × Titelleiste | |
| Ecken | Radius 0,5 em | |
| Schrift | Consolas, Menlo, DejaVu Sans Mono, … (`MONO_FONT`) | jede Schreibmaschinenschrift trifft dieselben Zellen |
| kleinste Schrift | 17 Szenenpixel = 9,35 px im Artikel | darunter warnt der Export (`MIN_TEXT_PX = 9,3`) |
