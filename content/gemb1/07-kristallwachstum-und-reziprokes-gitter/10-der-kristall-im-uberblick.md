---
title: Stufe 8: Der Kristall im Überblick
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallwachstum und reziprokes Gitter
order: 4171000
summary: Von der Bindung bis zur Zone sind viele Begriffe zusammengekommen.
tags: 
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Von der Bindung bis zur Zone sind viele Begriffe zusammengekommen. Diese Stufe ordnet sie zu einer Kette und vergleicht vier reale Kristalle.
:::

**Die Idee.** Die Bindung entscheidet, welche Struktur entsteht. Die Struktur zerfällt in Gitter und Basis. Das Gitter allein legt dann zwei Spalten fest, eine im Ort und eine im $k$-Raum, und jede Größe links hat ihr Gegenstück rechts (Abb. [8](#abb-8)).

:::abbildung gemb1/k7ueberblick 8
Von der Bindung zum Bravais-Gitter und seine zwei Spalten. Die Basis geht nur links ein, das reziproke Gitter hängt allein vom Bravais-Gitter ab.
:::

:::merke Die Kette in vier Aussagen
<ol>

<li>

Jede periodische Struktur lässt sich in ein Punktgitter (Bravais-Gitter) mit Basis zerlegen. Auf dem Punktgitter wird eine primitive Einheitszelle so wiederholt, dass der Raum oder die Fläche lückenlos gefüllt ist.

</li>

<li>

Die primitive Einheitszelle ist nicht eindeutig. Eine eindeutige Zelle liefert die Konstruktion nach Wigner und Seitz.

</li>

<li>

Zu jedem realen Gitter gibt es ein reziprokes Gitter. Dessen Wigner-Seitz-Zelle heißt erste Brillouin-Zone.

</li>

<li>

Man unterscheidet ionische, metallische und kovalente Bindung. **Ionisch:** Elektronentransfer zwischen den Partnern (Oktettregel), die Bindung geschieht durch Coulomb-Kräfte. **Metallisch:** Die äußersten Elektronen sind nur schwach gebunden und gehen in ein Elektronengas aus delokalisierten Elektronen über, das die positiven Ionenrümpfe bindet. **Kovalent:** Die Partner teilen sich Elektronen in überlappenden Orbitalen (Oktettregel), die Elektronen sind lokalisiert.

</li>

</ol>
:::

**Vier Kristalle im Vergleich.**

|  | Silizium | Kupfer | Kochsalz | Wolfram |
|---|---|---|---|---|
| Bindung | kovalent | metallisch | ionisch | metallisch |
| Bravais-Gitter | FCC | FCC | FCC | BCC |
| Basis | 2 Si-Atome | 1 Atom | Na$^+$ und Cl$^-$ | 1 Atom |
| $a$ in nm | 0,5431 | 0,3615 | 0,5640 | 0,3165 |
| reziprokes Gitter | BCC | BCC | BCC | FCC |
| Zone | abgest. Oktaeder | abgest. Oktaeder | abgest. Oktaeder | Rhombendodekaeder |
| $2\pi/a$ in nm$^{-1}$ | 11,57 | 17,38 | 11,14 | 19,85 |

⁠**So liest man das:** Drei völlig verschiedene Bindungen führen auf dieselbe Form der Zone, denn sie hängt nur vom Bravais-Gitter ab. Die Größe setzt die Gitterkonstante. Der Stoff selbst steckt in Basis und Bindung. **Grenzfall:** Sind beide Atomsorten einer Zinkblendestruktur gleich, wird aus ihr die Diamantstruktur. Bravais-Gitter und Zone ändern sich dabei nicht.

:::frage Heißt gleiche Zone auch gleiches Verhalten der Elektronen?
Nein. Die Zone sagt nur, welche Wellenvektoren verschieden sind. Welche Energie zu welchem $\boldsymbol k$ gehört, hängt von den Atomen ab. Kupfer leitet, reines Silizium kaum.
:::

:::aufgabe Aufgabe 10 ★★ CsCl ist nicht BCC
<span class="anker" id="aufg-10"></span>

In Caesiumchlorid sitzen Cs-Ionen auf den Würfelecken und Cl-Ionen in den Würfelmitten, $a=0{,}4123$ nm.

<ol class="al">

<li>

Welches Bravais-Gitter liegt vor, welche Basis? Warum ist es nicht BCC, obwohl das Bild so aussieht?

</li>

<li>

Gib das reziproke Gitter, die Form der Zone, ihre Kante und ihren Inhalt an.

</li>

<li>

Wie viele Elektronen fasst eine Zone je cm$^3$?

</li>

<li>

Vorhersage: Wären Ecken und Mitten gleich besetzt, wie änderten sich Form und Inhalt der Zone?

</li>

</ol>

:::loesung
(a) SC mit der Basis $\boldsymbol d_1=0$ (Cs) und $\boldsymbol d_2=\frac a2(1,1,1)$ (Cl). Die Verschiebung um $\boldsymbol d_2$ führt Cs auf Cl, ist also keine Translation des Gitters. (b) Reziprok SC, die Zone ist ein Würfel mit der Kante $2\pi/a=15{,}24\,\mathrm{nm^{-1}}$ und dem Inhalt $3540\,\mathrm{nm^{-3}}$. (c) $N=1/a^3=1{,}43\cdot10^{22}\,\mathrm{cm^{-3}}$, also $2N=2{,}85\cdot10^{22}$ Elektronen je cm$^3$. (d) Dann wäre es BCC: Die Zone wird zum Rhombendodekaeder mit dem doppelten Inhalt $7080\,\mathrm{nm^{-3}}$. Eine kleinere Zelle im Ort gibt eine größere Zone.
:::
:::
