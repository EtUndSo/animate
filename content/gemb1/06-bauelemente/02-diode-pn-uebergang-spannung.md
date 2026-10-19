---
title: Die Diode – der pn-Übergang unter Spannung
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Bauelemente
order: 4060200
summary: Was eine äußere Spannung am pn-Übergang bewirkt – und warum daraus ein Gleichrichter wird. In Durchlassrichtung senkt sie die Barriere und der Strom steigt exponentiell, in Sperrrichtung hebt sie die Barriere und es bleibt nur ein winziger Sättigungsstrom. Das Ergebnis ist die Shockley-Diodengleichung $I=I_S(e^{eV/k_BT}-1)$.
tags: Diode, Shockley-Gleichung, Durchlassrichtung, Sperrrichtung, Quasi-Fermi-Niveau, Minoritätsinjektion, Sättigungsstrom, Gleichrichter
---

:::grafik
Einstiegs-Animation: Das Banddiagramm des pn-Übergangs, dessen Barriere sich mit einem Spannungs-Schieberegler
bewegt. Bei __Durchlass__ ($V>0$) **sinkt** die Barriere, und ein Schwall Elektronen/Löcher diffundiert hinüber —
der Strom schießt hoch. Bei __Sperr__ ($V<0$) **steigt** die Barriere, der Schwall versiegt, nur ein Rinnsal
bleibt. Rechts zeichnet sich synchron die Kennlinie $I(V)$: flach und fast null für $V<0$, dann ein steiler
exponentieller Anstieg für $V>0$. Kernbotschaft: Dieselbe Barriere, von außen gehoben oder gesenkt, macht aus dem
pn-Übergang einen Einbahnstraßen-Stromventil — die Diode.
:::

:::konzept
Im Gleichgewicht hatte der pn-Übergang eine feste Barriere $eV_d$ und trug keinen Netto-Strom. Jetzt legen wir
eine **äußere Spannung** an. Sie verschiebt die Barriere — und zwar **asymmetrisch**: In der einen Richtung bricht
der Strom exponentiell hervor, in der anderen bleibt er fast null. Genau diese Asymmetrie ist die
__Gleichrichter__-Wirkung der __Diode__, des einfachsten aktiven Bauelements. Am Ende steht die berühmte
__Shockley-Diodengleichung__ — eine der wichtigsten Formeln der Elektronik.
:::

**Worum es geht:** Wir sehen, wie eine Spannung die Barriere senkt (Durchlass) oder hebt (Sperr), führen die
__Quasi-Fermi-Niveaus__ ein, und leiten über das „Gesetz des Übergangs" die __Shockley-Diodengleichung__ her.

## Durchlass und Sperre: die Barriere wandert

Die angelegte Spannung $V$ (Potential des p- gegenüber dem n-Gebiet) fällt fast vollständig über der hochohmigen
Verarmungszone ab und verschiebt dort die Barriere:

- **Durchlassrichtung** ($V>0$, Pluspol an p): Die Barriere **sinkt** von $eV_d$ auf $e(V_d-V)$. Jetzt können
  **exponentiell viel mehr** Ladungsträger über die Barriere diffundieren — der Diffusionsstrom steigt steil,
  während der (vom Restfeld getriebene) Driftstrom nahezu gleich bleibt. Netto: exponentieller Stromanstieg.
- **Sperrrichtung** ($V<0$): Die Barriere **steigt** auf $e(V_d+|V|)$, die Diffusion versiegt, es bleibt nur
  ein winziger, spannungsunabhängiger Sättigungsstrom.

:::grafik
Zwei Banddiagramme nebeneinander: links Durchlass (Barriere abgesenkt auf $e(V_d-V)$, dicke Diffusionspfeile
über die Barriere), rechts Sperr (Barriere erhöht, nur ein dünner Pfeil). Darunter die Barrierenhöhe als Formel
$e(V_d\mp V)$.
:::

## Quasi-Fermi-Niveaus: das Gleichgewicht ist aufgehoben

Im Gleichgewicht war das Fermi-Niveau überall konstant. Unter Spannung fließt Strom — also ist es das **nicht
mehr**. Man beschreibt die beiden Ladungsträgersorten dann durch getrennte __Quasi-Fermi-Niveaus__: $E_f^{\,n}$
für Elektronen, $E_f^{\,p}$ für Löcher. Jede Sorte ist für sich im Gleichgewicht, aber nicht mit der anderen. Über
die Verarmungszone spalten die beiden Niveaus genau um die angelegte Spannung auf:

$$E_f^{\,n} - E_f^{\,p} = e\,V.$$

:::grafik
Banddiagramm unter Durchlass mit zwei getrennten gestrichelten Linien $E_f^{\,n}$ und $E_f^{\,p}$, die über der
Verarmungszone um $eV$ auseinanderlaufen; außerhalb fallen sie je mit dem Majoritäts-Fermi-Niveau zusammen.
:::

## Die Shockley-Näherung

Um die Kennlinie geschlossen herzuleiten, macht man einige vereinfachende Annahmen (nach William Shockley) — kurz:

- **schwache Injektion** (injizierte Minoritäten ≪ Majoritäten),
- **Störstellenerschöpfung** (alle Dotieratome ionisiert),
- **Boltzmann-Statistik** (statt der vollen Fermi-Funktion),
- nur **Drift- und Diffusionsströme**,
- **lange** Bahngebiete (groß gegen die Diffusionslänge),
- **keine Generation/Rekombination in der Verarmungszone** (dort ist der Strom konstant),
- **abrupte** Verarmungszone (Schottky-Näherung).

## Das „Gesetz des Übergangs"

Der Kern der Herleitung ist, wie viele Minoritäten am Rand der Verarmungszone injiziert werden. Mit der
Boltzmann-Statistik ($n=N_L\,e^{-(E_L-E_f)/k_BT}$) und der Aufspaltung $E_f^{\,n}-E_f^{\,p}=eV$ bekommt die
Minoritätsdichte am p-seitigen Rand die Form

$$n_p = n_p^{\text{eq}}\,e^{\,eV/k_BT} \quad\Longrightarrow\quad \Delta n_p = n_p^{\text{eq}}\left(e^{\,eV/k_BT}-1\right).$$

- __$n_p^{\text{eq}}$__: die Gleichgewichts-Minoritätsdichte (über das Massenwirkungsgesetz $n_p^{\text{eq}}=n_i^2/N_A$).
- Der Überschuss am Rand steigt also **exponentiell** mit der Spannung — das ist der entscheidende Schritt.

:::grafik
Minoritäts-Dichteprofil $\Delta n_p(x)$: am Rand der Verarmungszone ein durch $e^{eV/k_BT}$ angehobener Wert, der
ins neutrale p-Gebiet hinein exponentiell über die Diffusionslänge $L_n$ abklingt. Daneben
$\Delta n_p=n_p^{\text{eq}}(e^{eV/k_BT}-1)$.
:::

## Die Shockley-Diodengleichung

Diese injizierten Minoritäten diffundieren ins Bahngebiet und klingen über die __Diffusionslänge__ ab. Der
Diffusionsstrom am Rand ist proportional zum Überschuss; summiert man den Elektronen- und den Löcherbeitrag, ergibt
sich die __Shockley-Diodengleichung__:

$$I = I_S\left(e^{\,eV/k_BT}-1\right),$$

mit dem __Sättigungsstrom__

$$I_S = e\,A\left(\frac{D_p}{L_p}\,\frac{n_i^2}{N_D} + \frac{D_n}{L_n}\,\frac{n_i^2}{N_A}\right) \;\propto\; n_i^2 \;\propto\; e^{-E_g/k_BT}.$$

Bezieht man alles auf die Querschnittsfläche $A$, erhält man die im Skript übliche **Stromdichte-Form** mit der
__Sättigungsstromdichte__ $J_s = I_S/A$:

$$J_\text{ges} = J_s\left(e^{\,eV/k_BT}-1\right), \qquad J_s = e\left(\frac{D_p}{L_p}\,\frac{n_i^2}{N_D} + \frac{D_n}{L_n}\,\frac{n_i^2}{N_A}\right).$$

- __Durchlass__ ($V>0$, einige $k_BT/e$): Der Exponentialterm dominiert, $I\approx I_S\,e^{eV/k_BT}$ — steiler
  Anstieg. Praktische Faustregel: Der Strom steigt um etwa eine Dekade pro $\approx 60\,$mV mehr Spannung.
- __Sperr__ ($V<0$): $e^{eV/k_BT}\to 0$, also $I\to -I_S$ — ein kleiner, konstanter Sperrstrom.

:::grafik
Die Diodenkennlinie $I(V)$: für $V<0$ ein winziges konstantes $-I_S$, bei $V=0$ null, dann für $V>0$ der steile
exponentielle Anstieg. In einer kleinen Nebenachse halblogarithmisch ($\log I$ über $V$) die Gerade mit „$\approx
60\,$mV/Dekade".
:::

**Warum kein symmetrischer Widerstand?** Ein Ohmscher Widerstand gäbe $I\propto V$ (punktsymmetrisch). Die Diode
nicht, weil die Barriere **exponentiell** und **vorzeichenabhängig** auf die Spannung reagiert: Senken flutet den
Strom, Heben blockiert ihn. Diese eingebaute Asymmetrie ist die Gleichrichtung — der Grund, warum man mit Dioden
Wechsel- in Gleichspannung verwandeln kann.

**Starke Temperaturabhängigkeit.** Weil $I_S\propto n_i^2\propto e^{-E_g/k_BT}$, wächst der Sperrstrom mit der
Temperatur rapide an und ist bei großlückigen Halbleitern viel kleiner. Das ist ein zentraler Grund, warum
Leistungselektronik zunehmend auf Materialien mit großer Bandlücke (SiC, GaN) setzt.

:::grafik
Zwei Kennlinien $I(V)$ für zwei Temperaturen: bei höherer Temperatur ist der Sperrstrom $I_S$ deutlich größer und
die Durchlasskurve setzt früher ein. Pfeil „$I_S\propto e^{-E_g/k_BT}$: steigt stark mit $T$".
:::

:::kern
Eine äußere Spannung $V$ verschiebt die Barriere des pn-Übergangs: __Durchlass__ ($V>0$) senkt sie auf
$e(V_d-V)$ → exponentiell mehr Diffusion; __Sperr__ ($V<0$) hebt sie → nur Sättigungsstrom. Im Nichtgleichgewicht
spalten die __Quasi-Fermi-Niveaus__ um $E_f^{\,n}-E_f^{\,p}=eV$ auf. Das „Gesetz des Übergangs"
$\Delta n_p=n_p^{\text{eq}}(e^{eV/k_BT}-1)$ (Minoritätsinjektion) führt über Diffusion zur
__Shockley-Diodengleichung__ $I=I_S(e^{eV/k_BT}-1)$ mit $I_S\propto n_i^2\propto e^{-E_g/k_BT}$. Kennlinie:
exponentiell in Durchlass ($\approx60\,$mV/Dekade), konstant $-I_S$ in Sperr → __Gleichrichter__. $I_S$ (und damit
der Sperrstrom) ist stark temperatur- und bandlückenabhängig.
:::

Die Diode steuert ihre Barriere über eine Spannung **im** Halbleiter. Beim Transistor steuert man sie stattdessen
berührungslos über eine **isolierte Elektrode** — das Prinzip des __MOS-Kondensators__, den wir als Nächstes
untersuchen, bevor daraus der MOSFET wird.
