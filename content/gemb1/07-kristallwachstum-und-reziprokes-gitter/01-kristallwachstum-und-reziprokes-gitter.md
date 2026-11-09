---
title: Überblick: Kristallwachstum und reziprokes Gitter
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallwachstum und reziprokes Gitter
order: 4170100
summary: Wie aus Sand ein Einkristall wird und wie eine Welle sein Gitter sieht
tags: Einkristall, Wafer, reziprokes Gitter, Brillouin-Zone
lang: de
---

## Worum es geht

Jeder Mikrochip beginnt als Sand. Dazwischen liegt einer der reinsten Stoffe, die Menschen herstellen: ein __Einkristall__ aus Silizium, ein Stück, in dem alle Atome zu einem einzigen durchgehenden Gitter gehören. Aus ihm sägt man den __Wafer__, die dünne runde Scheibe, auf der Bauelemente entstehen. Die erste Frage dieses Kapitels lautet: *Wie wird aus Sand ein fast fehlerfreier Kristall?*

Die zweite Frage folgt aus der Ordnung selbst. Elektronen sind Wellen, und eine Welle läuft durch ein Gitter anders als durch leeren Raum. *Wie beschreibt man einen Kristall so, wie eine Welle ihn sieht?* Dafür gehört zu jedem Kristallgitter ein zweites Gitter im Raum der Wellenvektoren, ein __reziprokes Gitter__, und dazu eine besondere Zelle, die __Brillouin-Zone__. Beide sind das Werkzeug für alles, was man über Elektronen im Kristall wissen will.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Silizium:** Diamantstruktur, also FCC-Gitter mit zweiatomiger Basis ([Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html)), $a=0{,}5431$ nm, 8 Atome im Würfel. Daraus folgt $n_\mathrm{Si}=8/a^3=4{,}99\cdot10^{22}\,\mathrm{cm^{-3}}$. Dichte $\rho_\mathrm m=2{,}33\,\mathrm{g/cm^3}$.

</li>

<li>

⁠**Molare Massen** in g/mol: Si 28,09, O 16,00, C 12,01, H 1,008, Cl 35,45. Dazu $N_\mathrm{Av}=6{,}022\cdot10^{23}\,\mathrm{mol^{-1}}$.

</li>

<li>

⁠**Atomkette:** wie in [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html), $a=0{,}2$ nm, $m=m_0$, $V_0=0$, also $t_0=0{,}953$ eV. Rechengröße: $\hbar^2/(2m_0)=0{,}0381\,\mathrm{eV\,nm^2}$.

</li>

<li>

⁠**Rechteckgitter:** Kanten $a_x=0{,}40$ nm und $a_y=0{,}60$ nm (in [Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html) hießen sie $a$ und $b$).

</li>

</ul>
:::
