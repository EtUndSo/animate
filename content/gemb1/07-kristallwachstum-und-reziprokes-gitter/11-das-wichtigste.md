---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Kristallwachstum und reziprokes Gitter
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallwachstum-und-reziprokes-gitter
knoten: Kapitel 7: Kristallwachstum und reziprokes Gitter
order: 4171100
summary: Wie aus Sand ein Einkristall wird und wie eine Welle sein Gitter sieht
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Rohsilizium:** $\mathrm{SiO_2}+2\mathrm C\to\mathrm{Si}+2\mathrm{CO}$, 12,5 bis 14 MWh je 1000 kg, 2 bis 4 % Fremdatome, nötig ist der Faktor $10^9$.

</li>

<li>

⁠**Gasphase:** $\mathrm{Si}+3\mathrm{HCl}\to\mathrm{SiHCl_3}+\mathrm{H_2}$ bei 300 °C, Destillation (31,8 °C), Abscheidung am Stab bei 1000 bis 1150 °C: Polysilizium.

</li>

<li>

⁠**Czochralski:** Schmelze über 1412 °C, Impfkristall legt die Richtung fest, gegensinnig drehen, dünner Hals gegen Versetzungen, 2 bis 250 mm/h, Segregation reichert die Schmelze an. Sägen und Polieren ergeben Wafer.

</li>

<li>

⁠**Reziprokes Gitter:** $\mathrm{e}^{\mathrm{j}\boldsymbol G\cdot\boldsymbol R}=1$, $\boldsymbol a_i\cdot\boldsymbol b_j=2\pi\delta_{ij}$, $\boldsymbol b_1=2\pi(\boldsymbol a_2\times\boldsymbol a_3)/(\boldsymbol a_1\cdot(\boldsymbol a_2\times\boldsymbol a_3))$. Kette: $G=h_1\,2\pi/a$, $E(k+G)=E(k)$. SC $\to$ SC, BCC $\to$ FCC, FCC $\to$ BCC.

</li>

<li>

⁠**Brillouin-Zone:** Wigner-Seitz-Zelle des reziproken Gitters, Inhalt $(2\pi)^3/\Omega$, $N$ Werte von $\boldsymbol k$, also $2N$ Elektronen. SC: Würfel, BCC: Rhombendodekaeder, FCC: abgestumpftes Oktaeder.

</li>

<li>

⁠**Netzebenen:** $\boldsymbol G=\sum h_i\boldsymbol b_i$ steht senkrecht auf $(h_1h_2h_3)$, $d=2\pi/|\boldsymbol G|$. Der Zonenrand ist die Bragg-Bedingung.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Kohlenstoff trennt Silizium im Lichtbogenofen vom Sauerstoff, der Umweg über das destillierbare Trichlorsilan reinigt es um den Faktor $10^9$, und am heißen Stab scheidet es sich als Polysilizium wieder ab.

</li>

<li>

Aus der Schmelze wächst an einem Impfkristall ein einziger Kristall, weil jede neue Atomlage das vorhandene Gitter fortsetzt, und der Barren wird zu Wafern gesägt.

</li>

<li>

Ein Gitter lässt als periodische Wellen nur die reziproken Gittervektoren $\boldsymbol G$ zu, die erste Brillouin-Zone enthält jede Welle genau einmal, und jedes $\boldsymbol G$ steht für eine Schar von Netzebenen.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Das Gitter ist die Vorlage, und alles muss zu ihm passen: die Atome beim Wachsen, die Wellen im fertigen Kristall.

| Ergebnis | Woher es kommt |
|---|---|
| Orientierung des ganzen Barrens | Jede Atomlage setzt das Gitter des Impfkristalls fort (Stufe [3](der-einkristall.html#stufe-3)) |
| Segregation | Fremdatome passen schlechter ins Gitter als in die Schmelze (Stufe [3](der-einkristall.html#stufe-3)) |
| $G=h_1\,2\pi/a$ | Wellen, die an allen Gitterpunkten gleich aussehen (Stufe [4](das-reziproke-gitter-in-einer-dimension.html#stufe-4)) |
| $\boldsymbol a_i\cdot\boldsymbol b_j=2\pi\delta_{ij}$ | Phase längs jedes Gittervektors ein Vielfaches von $2\pi$ (Stufe [5](reziproke-gittervektoren-in-der-ebene-und-im-raum.html#stufe-5)) |
| Brillouin-Zone mit $N$ Werten | Jede Welle zählt einmal, je Zelle ein Wert (Stufe [6](die-brillouin-zone.html#stufe-6)) |
| $d=2\pi/\vert \boldsymbol G\vert $ | Netzebenen sind Wellenfronten einer gitterperiodischen Welle (Stufe [7](netzebenen-und-reziproke-vektoren.html#stufe-7)) |
| Gleiche Zone bei Si, Cu, NaCl | Das reziproke Gitter kennt nur das Bravais-Gitter (Stufe [8](der-kristall-im-uberblick.html#stufe-8)) |
