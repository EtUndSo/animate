---
title: Gitter, Basis und Einheitszelle
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Kristallstruktur
order: 4020100
summary: Wie man eine unendlich große, periodische Atomanordnung mit ganz wenig Information beschreibt – indem man sie in ein Positionsraster (das Gitter) und ein Motiv (die Basis) zerlegt. Daraus folgen die Begriffe primitive Gittervektoren, Einheitszelle, die eindeutige Wigner-Seitz-Zelle und die Bravaisgitter (1 in 1D, 5 in 2D, 14 in 3D).
tags: Kristall, Punktgitter, Basis, Einheitszelle, primitive Gittervektoren, Wigner-Seitz-Zelle, Bravaisgitter
---

:::grafik
Einstiegs-Animation: Eine gekachelte Wand baut sich auf. Zuerst erscheint ein unsichtbares Raster aus
Fugenkreuzen (das __Gitter__ — nur Positionen), dann wird an jedes Kreuz dasselbe Motiv gehängt (die __Basis__ —
z. B. eine zweifarbige Fliese), und zusammen entsteht die vollständige, periodische Wand (der __Kristall__). Ein
Verschiebungspfeil zeigt: Schiebt man die ganze Wand um einen Gittervektor, liegt sie wieder deckungsgleich auf
sich selbst. Kernbotschaft: Eine unendlich große, regelmäßige Struktur steckt vollständig in „wo sitzen die
Punkte" + „was sitzt an jedem Punkt".
:::

:::konzept
Im ganzen bisherigen Quantenmechanik-Kapitel saß **ein** Elektron in **einem** Potential. Ein Festkörper besteht
aber aus rund $10^{23}$ Atomen. Das klingt hoffnungslos — bis man bemerkt, dass ein __Kristall__ **periodisch**
ist: Dasselbe Bauteil wiederholt sich stur in alle Richtungen. Genau diese Periodizität ist der Schlüssel zu
allem, was danach kommt (Bandstruktur, effektive Masse, Halbleiter). Dieses Kapitel stellt das Werkzeug bereit,
mit dem man Periodizität **mathematisch** fasst. Der erste und wichtigste Schritt: die Zerlegung in ein
__Gitter__ (die Positionen) und eine __Basis__ (das Motiv). Damit wird aus „unendlich viele Atome" eine
endliche, handhabbare Beschreibung.
:::

**Worum es geht:** Wir zerlegen eine periodische Struktur in __Punktgitter__ und __Basis__, führen die
__primitiven Gittervektoren__ und die __Einheitszelle__ ein, lösen das Problem ihrer Mehrdeutigkeit mit der
eindeutigen __Wigner-Seitz-Zelle__ und zählen schließlich, wie viele grundsätzlich verschiedene periodische
Gitter es überhaupt gibt (die __Bravaisgitter__).

## Gitter und Basis — die Grundidee

Schaut man ein Bienenwabenmuster, eine Ziegelmauer oder ein Escher-Bild an, haben alle eines gemeinsam: Es gibt
eine Verschiebung, nach der das Muster **wieder deckungsgleich** auf sich selbst liegt. Um so etwas mit
möglichst wenig Information zu beschreiben, trennt man zwei Dinge sauber voneinander:

- __Punktgitter__ (anschaulich: das unsichtbare Positionsraster) — eine abstrakte Menge von Punkten, die allein
  die **Periodizität** trägt. Man wählt einen beliebigen Bezugspunkt im Motiv und markiert, wo dieses „gleiche"
  Element wiederkehrt. Übrig bleibt ein reines Punktmuster: das **Wo**.
- __Basis__ (anschaulich: das Motiv, das an jeden Gitterpunkt gehängt wird) — der konkrete Inhalt: ein Atom,
  eine Atomgruppe, ein ganzes Molekül. Die Basis kann beliebig kompliziert sein: das **Was**.

Zusammengefasst in der zentralen Gleichung dieses Kapitels ([Mahidol](https://physics.sc.mahidol.ac.th/sces/SCPY371/lec1.pdf)):

$$\text{Kristall} = \text{Punktgitter} + \text{Basis}.$$

Das Gitter allein ist noch kein Kristall (es sind nur Positionen, keine Atome); erst mit der Basis wird es zum
realen Atomgebäude.

:::grafik
Drei Felder nebeneinander: (a) das reine __Punktgitter__ (nur Punkte), (b) die __Basis__ (ein einzelnes Motiv,
z. B. zwei verschiedenfarbige Atome), (c) der fertige __Kristall__ als Gitter mit an jedem Punkt aufgehängter
Basis. Darunter die Gleichung „Kristall = Punktgitter + Basis".
:::

## Primitive Gittervektoren und die Einheitszelle

Wie erreicht man jeden Gitterpunkt von einem festen Startpunkt aus? Durch **Verschiebungen** (Translationen).
Man braucht dafür in 2D zwei __primitive Gittervektoren__ $\vec a_1, \vec a_2$ — die zwei kürzesten,
nicht-parallelen Verschiebungen, aus denen sich **alle** anderen durch ganzzahlige Vielfache zusammensetzen
lassen. Jeder Gitterpunkt hat dann die Form

$$\vec R = m_1\,\vec a_1 + m_2\,\vec a_2, \qquad m_1, m_2 \in \mathbb{Z}.$$

- __$\vec a_1, \vec a_2$__: die __primitiven Gittervektoren__ (in 3D kommt $\vec a_3$ hinzu).
- __$m_1, m_2$__: beliebige **ganze** Zahlen — nur ganzzahlige Schritte treffen wieder einen Gitterpunkt.

Das von den primitiven Vektoren aufgespannte Parallelogramm (in 3D: Parallelepiped) ist die __Einheitszelle__ —
die „Kachel", die den Raum durch reines Verschieben lückenlos füllt. Die __primitive Einheitszelle__ ist die
**kleinstmögliche** solche Kachel; sie enthält genau **einen** Gitterpunkt ([Wikipedia](https://en.wikipedia.org/wiki/Bravais_lattice),
[vlab IIITH](https://bss-iiith.vlabs.ac.in/exp/unit-cells/theory.html)).

:::grafik
Ein 2D-Punktgitter mit eingezeichneten $\vec a_1, \vec a_2$ von einem Ursprungspunkt aus. Ein Beispielpunkt wird
über $\vec R = 2\vec a_1 + \vec a_2$ erreicht (die Schritte sind als Pfeilkette markiert). Das aufgespannte
Parallelogramm ist als __Einheitszelle__ schattiert.
:::

**Warum ist das so mächtig?** Weil eine unendliche, komplizierte Struktur damit auf wenige Zahlen (die
Gittervektoren) plus einen kleinen Zellinhalt (die Basis) reduziert ist. Genau diese **endliche** Beschreibung
macht die Quantenmechanik im Festkörper (nächstes Kapitel) überhaupt lösbar.

## Das Problem: die Zelle ist nicht eindeutig

Jetzt kommt ein Stolperstein, der sich durch das ganze Kapitel zieht: Die primitive Einheitszelle ist **nicht
eindeutig**. Dieselben Gitterpunkte lassen sich mit verschieden geformten Kacheln lückenlos auslegen — als
Parallelogramm, als Raute, verschoben nach links oder rechts. Alle diese Zellen sind gleichberechtigt und haben
**dieselbe** (minimale) Fläche, aber sie sehen unterschiedlich aus ([Wikipedia](https://en.wikipedia.org/wiki/Bravais_lattice)).

Diese Wahlfreiheit ist unbequem: Man möchte **eine** Zelle, die eindeutig festliegt und die Symmetrie des
Gitters widerspiegelt — ohne Willkür.

:::grafik
Dasselbe Punktgitter dreimal, jedes Mal mit einer **anderen**, aber gleich großen primitiven Zelle (schiefes
Parallelogramm / Raute / anders verschobenes Parallelogramm). Beschriftung: „gleiche Fläche, verschiedene Form —
nicht eindeutig".
:::

## Die Lösung: die Wigner-Seitz-Zelle

Um die Willkür zu beseitigen, definiert man die __Wigner-Seitz-Zelle__ (anschaulich: das „Hoheitsgebiet" eines
Gitterpunkts — **alle** Raumpunkte, die diesem Gitterpunkt näher sind als jedem anderen) ([Wikipedia](https://en.wikipedia.org/wiki/Bravais_lattice)).
Die Konstruktion ist ein einfaches Rezept:

1. Ziehe **Verbindungslinien** vom Gitterpunkt zu seinen nächsten Nachbarn.
2. Schneide jede Verbindungslinie **senkrecht durch ihre Mitte** (die Mittelsenkrechte; in 3D die Mittelebene).
3. Die kleinste von diesen Schnitten eingeschlossene Fläche (3D: Volumen) ist die Wigner-Seitz-Zelle.

Diese Zelle ist **primitiv** (sie enthält genau einen Gitterpunkt), trägt die **volle Symmetrie** des Gitters
und ist durch die Konstruktion **eindeutig** — das ist ihr ganzer Vorteil. Wir treffen sie im reziproken Gitter
als __Brillouin-Zone__ wieder, der Bühne der Bandstruktur.

:::grafik
Ein Gitterpunkt mit seinen nächsten Nachbarn; zu jedem eine Verbindungslinie, jede mit ihrer eingezeichneten
Mittelsenkrechten. Die eingeschlossene Zelle ist farbig gefüllt — die eindeutige __Wigner-Seitz-Zelle__.
:::

## Bravaisgitter: wie viele Positionsraster gibt es?

Ein __Bravaisgitter__ ist ein periodisches Punktgitter mit einer entscheidenden Eigenschaft: Es sieht von
**jedem** seiner Punkte aus **exakt gleich** aus — jeder Gitterpunkt hat die identische Umgebung. Formal: Jede
Translation $\vec R = \sum_i m_i \vec a_i$ (ganze $m_i$) bildet das Gitter deckungsgleich auf sich selbst ab.

Die überraschende Antwort auf „wie viele grundsätzlich verschiedene solche Raster gibt es?" ist eine **endliche,
kleine** Zahl ([Wikipedia](https://en.wikipedia.org/wiki/Bravais_lattice)):

- **1D:** genau **1** Bravaisgitter (die Kette äquidistanter Punkte, Abstand $a$).
- **2D:** genau **5** Bravaisgitter (quadratisch, rechteckig, zentriert-rechteckig, hexagonal, schiefwinklig).
- **3D:** genau **14** Bravaisgitter, verteilt auf 7 __Kristallsysteme__.

**Warum ausgerechnet 14 und nicht mehr?** Man kombiniert die 7 Kristallsysteme mit den möglichen
**Zentrierungen** (keine, raumzentriert, flächenzentriert, basiszentriert). Nicht jede Kombination ergibt aber
ein **geometrisch neues** Gitter — viele sind zu einem bereits gezählten äquivalent. Übrig bleiben genau 14
verschiedene ([vlab IIITH](https://bss-iiith.vlabs.ac.in/exp/unit-cells/theory.html)).

:::grafik
Eine kleine Galerie: 1 Gitter in 1D (Punktkette), daneben die 5 Gitter in 2D als Miniaturen mit ihren
Zellformen, daneben als Hinweis „3D: 14, in 7 Kristallsystemen". Die Zahlen 1 → 5 → 14 groß hervorgehoben.
:::

## Wann etwas *kein* Bravaisgitter ist: Graphen

Die Bedingung „jeder Punkt hat die identische Umgebung" ist schärfer, als sie klingt. Das Waben-(Honigwaben-)
Muster von **Graphen** (eine einzelne Kohlenstoff-Ebene) sieht von zwei benachbarten C-Atomen aus
**unterschiedlich** aus: Beim einen zeigen die Bindungen „nach oben", beim Nachbarn „nach unten". Damit ist die
Kernbedingung verletzt — das Wabenmuster ist **kein** Bravaisgitter.

Die Rettung ist genau die Gitter-plus-Basis-Idee: Graphen ist ein **hexagonales Bravaisgitter** mit einer
**zweiatomigen Basis** (die zwei inäquivalenten C-Plätze). Das zeigt, wie allgemein das Konzept ist: Selbst
scheinbar „nicht-bravaissche" Strukturen werden durch die Wahl einer passenden Basis wieder zu Gitter + Basis.

:::grafik
Das Graphen-Wabengitter mit zwei verschiedenfarbig markierten C-Plätzen A und B; Pfeile zeigen, dass die
Bindungen bei A und B entgegengesetzt orientiert sind („unterschiedliche Umgebung"). Daneben die Zerlegung:
hexagonales Punktgitter + zweiatomige Basis (A, B).
:::

:::kern
Ein __Kristall__ = __Punktgitter__ (das **Wo** — reine Positionen) + __Basis__ (das **Was** — das Motiv an jedem
Punkt). Alle Gitterpunkte: $\vec R = \sum_i m_i \vec a_i$ mit ganzen $m_i$ und den __primitiven Gittervektoren__
$\vec a_i$. Die __Einheitszelle__ füllt den Raum durch Verschieben; die __primitive__ enthält genau **1**
Gitterpunkt, ist aber **nicht eindeutig** — eindeutig wird sie erst als __Wigner-Seitz-Zelle__ (alle Punkte, die
einem Gitterpunkt am nächsten sind; volle Symmetrie). Ein __Bravaisgitter__ sieht von jedem Punkt gleich aus;
davon gibt es **1 (1D) → 5 (2D) → 14 (3D)**. __Graphen__ ist keins (zwei inäquivalente C-Plätze), sondern ein
hexagonales Gitter mit **zweiatomiger Basis**.
:::

Wir wissen jetzt, **wie** man ein periodisches Gitter beschreibt. Als Nächstes schauen wir die für Halbleiter
wichtigsten konkreten Gitter an — die drei __kubischen__ Bravaisgitter (einfach kubisch, raumzentriert,
flächenzentriert) — und die Kennzahlen __Koordinationszahl__ und __Packungsdichte__, die erklären, warum Atome
sich zu der einen und nicht der anderen Struktur ordnen.
