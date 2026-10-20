# Review durch Opus 5.5 (Phase A)

Die bereits im Bauplan-Stil geschriebenen HöMa3-Artikel werden mit Opus 5.5 kritisch geprüft und bei Bedarf
verbessert (Checkliste: `ARTIKEL_BAUPLAN.md` §8). Ein Artikel pro Loop-Tick; nach dem Review wird der Haken gesetzt
und in derselben Zeile kurz notiert, was verbessert wurde. Danach schreibt der Loop die übrigen Artikel neu
(Phase B).

- [ ] content/hoema3/01-differentialrechnung-vektorfelder/01-skalar-und-vektorfelder-differenzierbarkeit.md — OFFEN: Fusions-Durchgang (Bauplan §1 Nr. 10: Leitbild „Zoom aufs Gitter" durch alle Abschnitte ziehen, jede Formel/Herleitung mit „Im Bild") + Pfeil-Notation (ET4: alle Vektoren) + Groß/Klein (vektorwertige Abbildungen $\vec f,\vec g$ → $\vec F,\vec G$; Punkte $\vec x$; vektorielle Schritte $\vec h$). Review 1 erledigt: partielle Ableitung formal definiert; Zahlenbeispiel Df an zwei Punkten gedeutet (Streckung/Drehung); Gegenbeispiel xy/(x²+y²) ergänzt; neue Herleitungen: Eindeutigkeit A=Df, differenzierbar ⇒ stetig, C¹ ⇒ differenzierbar, Satz von Schwarz (jetzt Formel-Box), Kettenregel über Linearisierungen; undefiniertes N → p×n; h/φ entflochten; Gleichungen im Fließtext 9 → 0.
- [x] content/hoema3/01-differentialrechnung-vektorfelder/02-gradient-und-radialsymmetrische-felder.md — mit Fusion neu gefasst (Leitbild Landschaft + Wanderer in jedem Abschnitt); Richtungsableitung als Satz mit Herleitung + „Schatten"-Deutung + Zahlenbeispiel x²+2y² (Tabelle); Δc/Δs-Ablesen; Integrabilität mit Escher-Treppe, Beispielen (y,x) ✓ / (−y,x) ✗ und Wendeltreppen-Feld W samt Herleitung; ∇r=ê_r hergeleitet; Skript-Lücke ergänzt: Zentralfeld Gradientenfeld ⇔ radialsymmetrisch (mit Herleitung); Satz 1.10 als Formel-Box; Gleichungen im Fließtext 11 → 0. Danach Pfeil-Notation (ET4) und Groß/Klein umgestellt (radiales Profil Φ → ψ, $\hat e_r$ → $\vec e_r$, Nullvektor $\vec 0$).
- [ ] content/hoema3/01-differentialrechnung-vektorfelder/03-divergenz-rotation-laplace.md
- [x] content/hoema3/01-differentialrechnung-vektorfelder/04-rechenregeln-div-rot-identitaeten.md — komplett neu geschrieben (vorgezogen wegen User-Feedback „Produktregeln nicht hergeleitet"); Leitbild Strömung + Farbstoff + Kästchen + Schaufelrad durchgehend; jede Regel mit Herleitung (15 Boxen): Kronecker/Levi-Civita inkl. Antisymmetrie, Kreuzprodukt- und rot-Indexformel, Produktregeln div(φE)/rot(φE) + ebene Version (Skript-Lücke), Spat = det = Grundfläche·Höhe, ε-ε-Identität mit vollständiger Fallunterscheidung, Graßmann, (E·∇)B als Richtungsableitung, div/rot(E×B), div rot = 0, rot rot, Vektorpotential, Coulomb-Feld als Gegenbeispiel (div hergeleitet), Eichfreiheit, Coulomb-Eichung, Wellengleichung (Schwarz-Vertauschung genannt); Zahlenbeispiele φ=x (div) und Scherströmung (rot), Graßmann mit e₁,e₁,e₂, rot rot an (0,0,x²); Vorzeichenfehler im Farbstoff-Bild korrigiert; :::kern ≤ 1 Formel/Bullet; Fließtext 0.
- [ ] content/hoema3/02-integralrechnung-rn/01-parameterintegrale.md
- [ ] content/hoema3/02-integralrechnung-rn/02-uneigentliche-parameterintegrale.md
- [ ] content/hoema3/02-integralrechnung-rn/03-mehrfachintegrale-fubini.md
- [ ] content/hoema3/02-integralrechnung-rn/04-integration-ueber-mengen-volumina.md
- [ ] content/hoema3/02-integralrechnung-rn/05-normalbereiche.md
- [ ] content/hoema3/03-kurvenintegrale/01-kurvenintegral-und-orientierung.md
- [ ] content/hoema3/03-kurvenintegrale/02-erster-hauptsatz-konservative-felder.md
