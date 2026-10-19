---
title: Die endlich hohe Box
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Quantenmechanik
order: 4010700
summary: Was passiert, wenn die Wände der Box nicht mehr unendlich hoch sind, sondern endlich? Dann leckt die Welle – wie beim Tunneleffekt – in die Wände hinein. Das hat drei Folgen: Es gibt nur noch endlich viele gebundene Zustände, ihre Energien liegen tiefer als in der unendlichen Box, und es gibt keine saubere Formel mehr, sondern eine grafisch zu lösende Bedingung.
tags: endlicher Potentialtopf, gebundene Zustände, transzendente Gleichung, Wellenfunktion, Abklinglänge, gerade und ungerade Lösungen
---

:::grafik
Einstiegs-Animation: Ein Potentialtopf mit **endlicher** Tiefe $V_0$. Innen oszilliert die Wellenfunktion wie in
der bekannten Box, aber an den Wänden springt sie nicht auf null — sie geht stetig in ein exponentielles
Abklingen über, das **in die Wände hineinragt** und erst dort langsam verschwindet. Ein Schieberegler senkt die
Wandhöhe $V_0$: Je niedriger die Wand, desto weiter lecken die Wellen heraus, desto tiefer rutschen die
Energieniveaus, und nacheinander fallen obere Niveaus ganz aus dem Topf heraus. Kernbotschaft: Endliche Wände →
die Welle leckt heraus → weniger und tiefer liegende Zustände.
:::

:::konzept
Bisher hatte unsere Box **unendlich** hohe Wände. Das war bequem — die Welle war an den Wänden exakt null, es
passte immer eine ganzzahlige Zahl von Halbwellen hinein, und es kam die saubere Formel $E_n = n^2 h^2/(8mL^2)$
heraus. Aber reale „Kästen" (ein Elektron in einem Störstellen-Potential, in einem Quantenpunkt, in einem Atom)
haben **endlich** hohe Wände. Dann greift genau das, was wir beim Tunneleffekt gesehen haben: Die Welle
verschwindet an der Wand nicht abrupt, sondern **leckt exponentiell hinein**. Dieses eine Detail ändert das
Ergebnis grundlegend — und erklärt zugleich, warum die unendliche Box trotzdem eine so brauchbare Näherung ist.
:::

**Worum es geht:** Wir lösen dasselbe Kastenproblem noch einmal, aber mit **endlicher** Wandhöhe $V_0$. Wir
leiten her, warum die Welle in die Wände eindringt, warum daraus eine nur noch **grafisch** lösbare Bedingung
wird, und warum es dann (1.) nur **endlich viele** Zustände gibt, (2.) deren Energien **tiefer** liegen als in
der unendlichen Box und (3.) **immer mindestens einen** gebundenen Zustand.

## Das Modell und die drei Gebiete

Wir legen einen Topf der Breite $L$ symmetrisch um den Ursprung: innen ($-L/2 < x < L/2$) ist das Potential $0$,
außen ist es eine endliche Höhe $V_0$. Ein gebundenes Elektron hat eine Energie zwischen null und der Wandhöhe,
also $0 < E < V_0$. Dadurch zerfällt der Raum in drei Gebiete mit **zwei verschiedenen** Sorten von Lösungen:

- **Innen** ($0 < E$, also $E > V$): Hier ist die Schrödinger-Gleichung die oszillierende Sorte, die Lösungen
  sind $\sin$ und $\cos$ mit der __Wellenzahl__ $k = \sqrt{2mE}/\hbar$.
- **Außen** ($E < V_0$): Hier ist es die „verbotene" Sorte wie beim Tunneleffekt — die Lösungen klingen
  exponentiell ab mit der __Abklingkonstante__ $\kappa = \sqrt{2m(V_0 - E)}/\hbar$.

:::grafik
Der symmetrische Topf (Breite $L$, Tiefe $V_0$) mit der Energie $E$ als waagerechter Linie. Drei Gebiete farblich
getrennt: links „abklingend", Mitte „oszillierend", rechts „abklingend". Über den Gebieten die jeweilige
Lösungssorte ($e^{+\kappa x}$ | $\sin/\cos$ mit $k$ | $e^{-\kappa x}$) mit den Formeln für $k$ und $\kappa$.
:::

## Warum Symmetrie die Lösungen in zwei Sorten teilt

Weil der Topf **symmetrisch** liegt ($V(-x) = V(x)$), muss die Aufenthaltswahrscheinlichkeit $|\psi|^2$ ebenfalls
symmetrisch sein — das Elektron kann links nicht „anders" sein als rechts. Daraus folgt, dass die
Wellenfunktionen selbst entweder **gerade** (spiegelsymmetrisch, $\psi(-x) = \psi(x)$) oder **ungerade**
(punktsymmetrisch, $\psi(-x) = -\psi(x)$) sein müssen:

- **Gerade Zustände:** innen $\propto \cos(kx)$ (Bauch in der Mitte).
- **Ungerade Zustände:** innen $\propto \sin(kx)$ (Knoten in der Mitte).

Das ist eine enorme Vereinfachung: Statt an beiden Wänden getrennt rechnen zu müssen, genügt **eine** Wand — die
andere Seite ergibt sich aus der Symmetrie. Deshalb behandeln wir beide Sorten ab jetzt getrennt.

:::grafik
Zwei kleine Töpfe nebeneinander. Links ein __gerader__ Zustand: ein $\cos$-Bauch mittig, an beiden Wänden stetig
in abklingende Schwänze übergehend (spiegelsymmetrisch). Rechts ein __ungerader__ Zustand: ein $\sin$ mit Knoten
in der Mitte, die Schwänze auf beiden Seiten mit entgegengesetztem Vorzeichen (punktsymmetrisch).
:::

## Die Anschlussbedingung — warum es keine saubere Formel mehr gibt

In der unendlichen Box war die Randbedingung simpel: $\psi = 0$ an der Wand. Das erzwang exakt
$k L = n\pi$ und damit die bekannte Formel. Jetzt ist die Welle an der Wand **nicht** null. Stattdessen müssen an
der Wandstelle $x = L/2$ zwei Dinge **stetig** aneinander anschließen, weil die Schrödinger-Gleichung das
verlangt:

- die Wellenfunktion $\psi$ selbst (kein Sprung),
- ihre Steigung $\psi'$ (kein Knick).

Bildet man das Verhältnis $\psi'/\psi$ beider Seiten (das eliminiert die unbekannten Amplituden), erhält man für
die **geraden** Zustände die Bedingung

$$k\,\tan\!\left(\frac{kL}{2}\right) = \kappa.$$

- __$k$__: die innere __Wellenzahl__ ($\propto \sqrt{E}$).
- __$\kappa$__: die äußere __Abklingkonstante__ ($\propto \sqrt{V_0 - E}$).

Und hier steckt der Haken: In dieser Gleichung tauchen $k$ und $\kappa$ beide auf, und beide hängen über
$\sqrt{E}$ bzw. $\sqrt{V_0-E}$ von derselben Unbekannten $E$ ab — $E$ steckt einmal **im** Tangens (im Argument)
und einmal **außerhalb**. Eine solche Gleichung heißt __transzendent__: Man kann sie nicht nach $E$ auflösen. Es
gibt also **keine** geschlossene Formel wie $E_n = n^2 h^2/(8mL^2)$ mehr; die Energien muss man grafisch oder
numerisch bestimmen ([dxwl.bnu.edu.cn](https://dxwl.bnu.edu.cn/EN/Y2018/V37/I12/49),
[people.goshen.edu](https://people.goshen.edu/~paulmr/physix/313/gco/5.7.php?bigify=yup)).

:::grafik
Die Wandstelle $x = L/2$ im Ausschnitt: links der $\cos$-Ast (innen), rechts der $e^{-\kappa x}$-Ast (außen). Zwei
Bedingungen hervorgehoben — die Kurven treffen sich **ohne Sprung** (gleicher Wert) und **ohne Knick** (gleiche
Steigung). Ein Kästchen zeigt, wie aus „gleicher Wert + gleiche Steigung" das Verhältnis $\psi'/\psi$ und daraus
$k\tan(kL/2) = \kappa$ wird.
:::

**Die ungeraden Zustände** liefern auf genau demselben Weg (nur mit $\sin$ statt $\cos$) die Bedingung

$$-\,k\,\cot\!\left(\frac{kL}{2}\right) = \kappa.$$

## Die grafische Lösung: ein Kreis und zwei Kurvenscharen

Dass man nicht auflösen kann, heißt nicht, dass man nichts sieht. Macht man die Gleichungen dimensionslos — mit
den Abkürzungen $u = kL/2$ und $v = \kappa L/2$ — dann verbindet eine schlichte Beziehung beide Größen. Denn aus
den Definitionen folgt

$$u^2 + v^2 = \left(\frac{L}{2}\right)^2\frac{2mV_0}{\hbar^2} \equiv z_0^2, \qquad z_0 = \frac{L}{2}\frac{\sqrt{2mV_0}}{\hbar}.$$

- __$u = kL/2$__: Maß für die innere Oszillation (steigt mit $\sqrt{E}$).
- __$v = \kappa L/2$__: Maß für das äußere Abklingen (steigt mit $\sqrt{V_0-E}$).
- __$z_0$__: der __Topf-Parameter__ — er fasst Breite $L$ und Tiefe $V_0$ in **einer** Zahl zusammen.

Diese eine Zeile ist der Schlüssel: $u^2 + v^2 = z_0^2$ ist die Gleichung eines **Viertelkreises** mit Radius
$z_0$. Die Anschlussbedingungen von oben, in denselben Variablen geschrieben ($v = u\tan u$ für gerade,
$v = -u\cot u$ für ungerade Zustände), sind **Kurvenscharen**. Jeder **Schnittpunkt** von Kreis und Kurve ist ein
erlaubter gebundener Zustand ([zzz.physics.umn.edu](https://zzz.physics.umn.edu/_export/xhtml/classes/2009/fall/phys4101.001/lec_notes_1014)).

:::grafik
Das klassische $u$-$v$-Diagramm: ein Viertelkreis mit Radius $z_0$, dazu die Tangens-Äste (gerade Zustände) und
die $-\cot$-Äste (ungerade Zustände). Die **Schnittpunkte** sind als dicke Punkte markiert und zu den
zugehörigen Energieniveaus im Topf daneben verbunden. Ein Schieberegler für $z_0$ zeigt, wie beim Vergrößern des
Radius neue Schnittpunkte (= neue Zustände) hinzukommen.
:::

## Was man aus dem Bild abliest

Dieses eine Diagramm liefert direkt die drei physikalischen Kernaussagen:

- **Endlich viele Zustände.** Der Kreis hat nur den endlichen Radius $z_0$; er kann die Kurvenschar nur
  endlich oft schneiden. Also gibt es **nur endlich viele** gebundene Zustände — anders als in der unendlichen
  Box mit ihrer unendlichen Leiter. Ihre Zahl wächst mit $z_0$, also mit **Breite $\times \sqrt{\text{Tiefe}}$**.
- **Mindestens einer existiert immer.** Der erste Tangens-Ast beginnt im Ursprung, der Viertelkreis ebenfalls im
  Bereich $u \ge 0$ — sie schneiden sich **immer**, egal wie klein $z_0$ ist. Selbst der flachste Topf hält also
  **einen** (geraden) Zustand fest ([cmms.triumf.ca](https://cmms.triumf.ca/~jess/p200/sq_well/sq_well.html)).
- **Energien tiefer als in der unendlichen Box.** Weil die Welle in die Wände hineinleckt, passt sie effektiv in
  eine **etwas breitere** Box. Und breiter heißt (Erinnerung: $E \propto 1/L^2$) **niedrigere** Energie. Jedes
  Niveau liegt damit **unter** dem entsprechenden Niveau der unendlich hohen Box gleicher Breite.

:::grafik
Zwei Energieleitern nebeneinander für gleiche Breite $L$: links die unendliche Box (viele, höher liegende
Sprossen), rechts die endliche Box (nur wenige Sprossen, jede etwas **tiefer**, oben durch $V_0$ abgeschnitten).
Pfeile „nach unten" verbinden die entsprechenden Niveaus und sind mit „Welle leckt heraus → effektiv breiter →
tiefer" beschriftet.
:::

## Der Grenzfall: zurück zur unendlichen Box

Jetzt sieht man auch, **warum** die bequeme unendliche Box überhaupt eine gute Näherung ist. Lässt man die
Wandhöhe sehr groß werden ($V_0 \to \infty$), dann wird $z_0 \to \infty$ (der Kreis-Radius wächst über alle
Grenzen) und die Abklingkonstante $\kappa \to \infty$ (die Welle leckt gar nicht mehr heraus). Die Schnittpunkte
rücken dann genau auf die Stellen $kL = n\pi$ — und wir erhalten die vertraute Formel
$E_n = n^2 h^2/(8mL^2)$ zurück ([dxwl.bnu.edu.cn](https://dxwl.bnu.edu.cn/EN/Y2018/V37/I12/49)).

Die unendliche Box ist also kein anderes Modell, sondern der **Grenzfall sehr hoher Wände** der endlichen Box.
Für ein tief gebundenes Elektron (Energie weit unter der Wandhöhe) ist das Hineinlecken winzig, und die einfache
Formel stimmt sehr gut. Erst wenn ein Niveau nahe an die Wandoberkante $V_0$ kommt, wird die Welle weich und das
Hineinlecken spürbar.

:::kern
Bei **endlicher** Wandhöhe $V_0$ leckt die Welle wie beim __Tunneleffekt__ in die Wände: innen oszillierend
($k = \sqrt{2mE}/\hbar$), außen abklingend ($\kappa = \sqrt{2m(V_0-E)}/\hbar$). Die Symmetrie teilt die Lösungen
in **gerade** ($\cos$) und **ungerade** ($\sin$). Der stetige Anschluss von $\psi$ **und** $\psi'$ liefert
__transzendente__ Bedingungen ($k\tan(kL/2)=\kappa$ bzw. $-k\cot(kL/2)=\kappa$) — **keine** geschlossene Formel.
Grafisch: Viertelkreis $u^2+v^2=z_0^2$ mit $z_0=\tfrac{L}{2}\sqrt{2mV_0}/\hbar$, geschnitten mit den
Tangens-/Cotangens-Ästen; jeder Schnitt = ein Zustand. Folgen: **endlich viele** Zustände (Zahl $\propto$
Breite$\cdot\sqrt{\text{Tiefe}}$), **mindestens einer** existiert immer, und alle Energien liegen **tiefer** als
in der unendlichen Box (Hineinlecken → effektiv breiter). Grenzfall $V_0\to\infty$ liefert
$E_n=n^2h^2/(8mL^2)$ zurück.
:::

Bisher waren unsere Potentiale **kastenförmig** — mit ebenem Boden und senkrechten Wänden. Das echte Potential,
das ein Elektron im Atom fühlt, ist aber kein Kasten, sondern der **trichterförmige** Coulomb-Topf des Kerns. Löst
man die Schrödinger-Gleichung für dieses Potential, bekommt man die __Atomorbitale__ — das Thema des nächsten
Abschnitts.
