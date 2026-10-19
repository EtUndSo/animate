# Editor – offene Fixes / WebGL-Regressionen

Nach der Umstellung der 3D-Darstellung auf WebGL sind einige Einstellungen wirkungslos geworden oder müssen
anders implementiert werden. Gemeldet vom User 2026-10-19.

## Offene Punkte

1. **Shadows (Schattierung) nicht mehr einstellbar.**
   Vor WebGL ließ sich die Schattierung/der Schatten einstellen; seit die 3D-Objekte im WebGL-Shader
   gerendert werden, hat die Einstellung keine Wirkung mehr. → Entweder an den GL-Shader anbinden (das
   Phong-Shading nutzt derzeit eine fest verdrahtete Lichtrichtung) oder als bewusste Option neu implementieren.

2. **„Axes on Top" ohne Wirkung.**
   Die Achsen werden auf dem 2D-Canvas gezeichnet, der hinter/vor dem transparenten GL-Canvas liegt; „Achsen
   über dem Objekt" kann die 2D-Achsen nicht vor die GL-Mesh bringen. → Achsen im GL mitzeichnen (echte
   Verdeckung) oder Kompositing so lösen, dass die Option wieder greift.

3. **„Transparent" ohne Wirkung.**
   3D-Körper wurden in der WebGL-v2 bewusst opak gemacht; Transparenz ist im GL-Pfad nicht umgesetzt. →
   Transparenz/Alpha-Blending im GL-Renderer ergänzen und an die Option anbinden (Tiefensortierung beachten).

4. **3D-Plots haben kein aufgelegtes Grid mehr.**
   Früher lag ein Gitternetz auf dem 3D-Plot (wie bei GeoGebra die Flächen-Gitterlinien); die glatt
   schattierte GL-Fläche hat kein Wireframe/Grid mehr. → Optionales Gitter-Overlay auf der GL-Fläche
   (Wireframe-Linien entlang der u/v-Linien) wieder einbauen.

5. **resolution + static/adaptive entfernen.**
   Seit WebGL sind die Plots auch bei resolution 1 völlig glatt, die Unterscheidung static/adaptive und der
   resolution-Regler bringen im echten Editor keinen sichtbaren Nutzen mehr (im Testeditor war eine
   Glätte-Änderung sichtbar). → Aus dem echten Editor **entfernen**. ACHTUNG: intern eine sinnvolle feste/
   automatische Netzauflösung behalten (die e-Funktions-„Zacken" wurden früher gerade durch höhere
   GL-Auflösung behoben) — nur die UI-Steuerung raus.

## Status
- Aufgenommen 2026-10-19.
- **#5 ERLEDIGT** (Commit „Editor-Fix #5"): resolution/static-adaptive aus der UI entfernt, Props intern auf Default behalten.
- **#1 ERLEDIGT (Browsertest offen)**: Fragment-Shader nutzt jetzt ein `uShade`-Uniform; `draw()` setzt es aus `model.background.shadows` (`0.4+0.6*d` an / flach `1.0` aus). `editor.js` (FS + loc + draw).
- **#3 ERLEDIGT (Browsertest offen)**: `scene_model.py` setzt für 3D-Körper nicht mehr hart `_gl_opacity=1.0`, sondern `fill_opacity`; `draw()` schaltet bei `opacity<1` zusätzlich `depthMask(false)` (und stellt den Default danach/vor dem Clear wieder her), damit transparente Körper nicht verdecken. Hinweis: Für mehrere überlappende transparente Flächen fehlt noch Tiefensortierung (bei einfachen Szenen ok).
- **#2, #4 offen.** #4 (Grid-Overlay) = Wireframe-Linien entlang der u/v-Linien auf der GL-Fläche (Backend muss Linien-Indizes liefern, Frontend als `LINES` zeichnen). #2 (Achsen „on top") = Achsen im GL mitzeichnen (echte Verdeckung) = WebGL-v3-Schritt. Beide im nächsten Durchgang, nach dem Browsertest von #1/#3.
