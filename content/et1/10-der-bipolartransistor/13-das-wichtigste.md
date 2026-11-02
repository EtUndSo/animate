---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Bipolartransistor
order: 1201300
summary: Wie eine kleine Spannung einen großen Strom durch eine gesperrte Diode steuert
tags: Emitter, Basis, Kollektor, Stromverstärkung, Arbeitspunkt, Gegenkopplung, Steilheit
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Der __Emitter__ gibt Elektronen ab, die dünne __Basis__ lässt sie durch, der __Kollektor__ sammelt sie ein. Die Spannung $U_\mathrm{BE}$ entscheidet, wie viele Elektronen loslaufen: $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$. Das Feld der gesperrten Kollektordiode saugt sie ab, nur ein kleiner Rest fließt über die Basis, $I_\mathrm{B}=I_\mathrm{C}/B$. Der Faktor $B$ heißt __Stromverstärkung__.

</li>

<li>

Drei Anschlüsse heißen zwei unabhängige Spannungen. $I_\mathrm{C}$ ist deshalb eine Fläche über $U_\mathrm{BE}$ und $U_\mathrm{CE}$, jede Kennlinie ein Schnitt. Die äußere Schaltung wählt darauf den __Arbeitspunkt__, den Gleichstromzustand des Transistors. Ein Emitterwiderstand hält ihn durch __Gegenkopplung__ fest: Die Wirkung schwächt ihre eigene Ursache.

</li>

<li>

Für kleine Signale ersetzt die Tangente die Kurve. Ihre Steigung, die __Steilheit__ $S=I_\mathrm{C}/U_T$, macht den Transistor zur gesteuerten Stromquelle. Die Spannungsverstärkung der Emitterschaltung, der Standardschaltung mit dem Emitter an Masse, ist die Gleichspannung am Kollektorwiderstand geteilt durch $U_T$.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$, $U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}$. Drei Anschlüsse heißen zwei freie Spannungen, $I_\mathrm{C}$ ist eine Fläche, jede Kennlinie ein Schnitt.

</li>

<li>

Mechanismus: $U_\mathrm{BE}$ senkt die Barriere, Elektronen durchqueren die dünne Basis, das Feld der gesperrten CB-Diode saugt sie ab: $I_\mathrm{C}=I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}$, $I_\mathrm{B}=I_\mathrm{C}/B$. Basisstrom ersetzt nur die wenigen Verluste.

</li>

<li>

Bereiche: Sperrbereich (offen), aktiv ($I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}\ge0{,}2$ V), Sättigung ($U_\mathrm{CE}=0{,}2$ V, $I_\mathrm{C}\le B\,I_\mathrm{B}$). Annehmen, rechnen, prüfen. Schalter: Enden der Arbeitsgeraden. Verstärker: aktiv, in der Mitte.

</li>

<li>

Gegenkopplung: $I_\mathrm{C}=(U_\mathrm{q}-U_\mathrm{BE})/\bigl(R_\mathrm{E}(1+1/B)+R_\mathrm{i}/B\bigr)$. Mehr Strom hebt den Emitter und nimmt $U_\mathrm{BE}$ zurück. Stromspiegel: $I_\mathrm{C2}=I_\mathrm{ref}/(1+2/B)$. Regler: $U_\mathrm{A}=U_\mathrm{Z}-U_\mathrm{BE}$.

</li>

<li>

Kleinsignal: $S=I_\mathrm{C}/U_T$, $r_\mathrm{BE}=B/S$, $r_\mathrm{CE}\approx U_\mathrm{Early}/I_\mathrm{C}$. Die Tangente gilt für $|u_\mathrm{be}|\ll U_T$.

</li>

<li>

Emitterschaltung $A=-U_{R_\mathrm{C}}/U_T$, Kollektorschaltung $A\approx1$, Basisschaltung $A=+S\,R_\mathrm{C}$. Mit $R_\mathrm{E}$ ist $A\approx-R_\mathrm{C}/R_\mathrm{E}$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Der Transistor hat zwei Grenzen mit zwei Aufgaben. An der Basis-Emitter-Grenze wird gesteuert: Die Spannung dort legt exponentiell fest, wie viele Elektronen starten. An der Kollektor-Basis-Grenze wird nur abgeholt: Wer ankommt, wird abgesaugt, die Spannung dort spielt kaum eine Rolle.

| Ergebnis | Woher es kommt |
|---|---|
| $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$, zwei freie Spannungen | Drei Anschlüsse, Knoten- und Maschenregel (Stufe [1](drei-schichten-zwei-spannungen.html#stufe-1)) |
| $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$, $I_\mathrm{B}=I_\mathrm{C}/B$ | Starten, dünne Basis durchqueren, abgesaugt werden (Stufe [2](warum-strom-durch-die-gesperrte-diode-fliet.html#stufe-2)) |
| Viele Kennlinien | Schnitte durch eine Fläche: steil in $U_\mathrm{BE}$, flach in $U_\mathrm{CE}$ (Stufe [3](eine-flache-viele-kennlinien.html#stufe-3)) |
| Drei Arbeitsbereiche | Welche der beiden Grenzen leitet (Stufe [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4)) |
| Arbeitspunkt | Transistorgleichung und Masche müssen zugleich gelten (Stufe [5](der-arbeitspunkt.html#stufe-5)) |
| Schalter, Inverter | Die beiden Enden der Arbeitsgeraden: wenig Leistung im Transistor (Stufe [6](der-transistor-als-schalter.html#stufe-6)) |
| Stabiler Arbeitspunkt | Mehr Strom hebt den Emitter und nimmt $U_\mathrm{BE}$ zurück (Stufe [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7)) |
| Stromspiegel, Spannungsregler | Gleiches $U_\mathrm{BE}$ heißt gleicher Strom, und $U_\mathrm{BE}$ bleibt fast konstant (Stufe [8](zwei-schaltungen-die-nutzen.html#stufe-8)) |
| $S=I_\mathrm{C}/U_T$ | Die Steigung einer e-Funktion ist ihr Wert durch die Skala $U_T$ (Stufe [9](tangente-statt-kurve.html#stufe-9)) |
| $\vert A\vert =U_{R_\mathrm{C}}/U_T$ | Stromänderung $S\,u_\mathrm{ein}$ mal $R_\mathrm{C}$ (Stufe [10](drei-grundschaltungen.html#stufe-10)) |
