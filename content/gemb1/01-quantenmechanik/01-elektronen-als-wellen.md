---
title: Elektronen als Wellen – Einführung in die Quantenmechanik
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Quantenmechanik
order: 4010100
summary: Von Grund auf – warum ein Elektron sich nicht wie eine winzige Kugel, sondern wie eine Welle verhält, was der Doppelspalt und die atomaren Spektrallinien darüber verraten, was die Wellenfunktion bedeutet und warum das „Einsperren" einer Welle automatisch nur noch bestimmte Energien zulässt. Das Fundament für alles Weitere.
tags: Quantenmechanik, Welle-Teilchen-Dualismus, Doppelspalt, de-Broglie-Wellenlänge, Wellenfunktion, Aufenthaltswahrscheinlichkeit, Quantisierung
---

:::grafik
Einstiegs-Animation: Eine „Elektronenkanone" schießt Elektronen **einzeln** auf einen Doppelspalt und dahinter
auf einen Schirm. Jedes Elektron erzeugt genau einen punktförmigen Einschlag — wie ein Teilchen. Doch je mehr
Punkte sich sammeln, desto deutlicher wird ein **Streifenmuster** aus hellen und dunklen Bändern — ein
Interferenzmuster, wie es nur Wellen erzeugen. Kernbotschaft: Ein Elektron kommt einzeln an wie ein Teilchen,
verteilt sich aber wie eine Welle. Genau dieses Doppelgesicht ist der Ausgangspunkt der Quantenmechanik.
:::

:::konzept
In diesem Themenbereich geht es um Elektronen in Materialien — und die zentrale Erkenntnis gleich zu Beginn: Ein
Elektron ist **keine winzige Kugel**, die auf einer Bahn fliegt, sondern verhält sich wie eine **Welle**. Die
ganze Quantenmechanik ist das Werkzeug, mit dem man ausrechnet, welche **Energien** und **Aufenthaltsorte** so
eine Elektronen-Welle haben darf. Das klingt abstrakt, hat aber sehr handfeste Folgen: Warum Atome nur
bestimmte Farben aussenden, warum es Leiter, Halbleiter und Isolatoren gibt, wie ein Transistor funktioniert —
alles folgt aus dem Wellencharakter der Elektronen.
:::

**Worum es geht:** Bevor wir rechnen, muss klar sein, *warum* man überhaupt eine neue Physik braucht. Wir
sehen, woran die klassische Vorstellung scheitert, was der __Welle-Teilchen-Dualismus__ bedeutet, wie groß die
Wellenlänge eines Elektrons ist, was die __Wellenfunktion__ beschreibt — und warum **Einsperren** einer Welle
ganz von selbst zu **diskreten Energien** führt.

## Warum die klassische Vorstellung scheitert

Stellt man sich ein Elektron als kleine Kugel vor, die um den Atomkern kreist wie ein Planet um die Sonne, gerät
man sofort in Widersprüche. Zwei Beobachtungen reichen schon:

- **Atome senden nur bestimmte Farben aus.** Erhitzt man ein Gas, leuchtet es nicht in allen Farben, sondern nur
  in wenigen, scharfen __Spektrallinien__. Eine kreisende Kugel könnte jede beliebige Bahn und damit jede
  beliebige Energie haben — dann müsste das Licht alle Farben enthalten. Die scharfen Linien bedeuten: Das
  Elektron darf nur **ganz bestimmte, diskrete Energien** annehmen. Warum?
- **Ein klassisches Atom wäre instabil.** Eine kreisende Ladung müsste nach der klassischen Physik ständig
  Energie abstrahlen und in Sekundenbruchteilen in den Kern stürzen. Atome gibt es aber stabil seit Milliarden
  Jahren.

Die klassische „Kugel-auf-Bahn"-Vorstellung kann das nicht erklären. Es braucht ein grundlegend anderes Bild.

:::grafik
Gegenüberstellung: Links die klassische Erwartung — ein Elektron als Kugel auf einer Kreisbahn um den Kern, dazu
ein „Spektrum", das kontinuierlich alle Farben enthielte. Rechts die Beobachtung — ein reales Linienspektrum mit
nur wenigen scharfen, farbigen Linien vor schwarzem Hintergrund. Ein großes Fragezeichen über „Warum nur
bestimmte Energien?".
:::

## Welle und Teilchen: der Doppelspalt

Den entscheidenden Hinweis gibt der __Doppelspalt-Versuch__. Schickt man Wasserwellen oder Licht durch zwei enge
Spalte, überlagern sich die beiden dahinter entstehenden Wellen. Je nach Ort treffen sie **gleichphasig**
aufeinander (Wellenberg auf Wellenberg → Verstärkung) oder **gegenphasig** (Berg auf Tal → Auslöschung). Es
entsteht ein __Interferenzmuster__ aus hellen und dunklen Streifen — das typische Erkennungszeichen einer Welle.

Nun das Erstaunliche: Schickt man **Elektronen** durch den Doppelspalt, passiert genau dasselbe. Und zwar auch
dann, wenn man sie **einzeln** abschießt:

- Jedes Elektron erzeugt auf dem Schirm **einen** punktförmigen Einschlag — es kommt als „Teilchen" an.
- Über viele Elektronen hinweg bauen diese Punkte aber das **Interferenzmuster** auf — jedes Elektron ist also
  irgendwie durch **beide** Spalte zugleich gegangen und hat mit sich selbst interferiert, wie eine Welle.

Das ist der __Welle-Teilchen-Dualismus__. Genau genommen ist der Name etwas irreführend: Ein Elektron ist weder
„eine kleine Kugel" noch „eine Wasserwelle" — es ist ein eigenes Ding (ein __Quantenobjekt__), das je nach
Experiment die eine oder andere Seite zeigt. Welle und Teilchen sind zwei **Modelle**, die wir benutzen, um sein
Verhalten zu beschreiben.

:::grafik
Zweigeteilte Abbildung. Oben das Wellenbild: zwei vom Doppelspalt ausgehende kreisförmige Wellenfronten
überlagern sich; an den Orten „Berg trifft Berg" entstehen helle, an „Berg trifft Tal" dunkle Streifen. Unten die
Elektronen-Version als Animation: einzelne Punkte erscheinen nacheinander scheinbar zufällig, fügen sich aber
nach und nach zu demselben Streifenmuster zusammen.
:::

## Die de-Broglie-Wellenlänge: warum wir das im Alltag nicht sehen

Wenn Elektronen Wellen sind — welche Wellenlänge haben sie? Die Antwort von Louis de Broglie (1924): **Jedem**
Teilchen mit dem Impuls $p = m v$ ist eine Wellenlänge zugeordnet,

$$\lambda = \frac{h}{p} = \frac{h}{m v}.$$

- __$\lambda$__: die __de-Broglie-Wellenlänge__ des Teilchens.
- __$h$__: das __Plancksche Wirkungsquantum__, $h \approx 6{,}63\cdot10^{-34}\,\text{J}\,\text{s}$ — eine
  winzige Naturkonstante, die überall in der Quantenmechanik auftaucht.
- __$p = m v$__: der __Impuls__ (Masse mal Geschwindigkeit).

Diese eine Formel erklärt sofort, **warum uns die Quantennatur im Alltag nie begegnet**. Weil $h$ so extrem
klein ist, kommt für große, schwere Objekte eine absurd kleine Wellenlänge heraus:

- Ein **Tennisball** (etwa $60\,\text{g}$, $30\,\text{m/s}$) hat $\lambda \approx 4\cdot10^{-34}\,\text{m}$ —
  unvorstellbar viel kleiner als jedes Atom. Von Wellenverhalten ist nichts zu merken; der Ball ist zu Recht
  eine Kugel.
- Ein **Elektron** dagegen ist extrem leicht. Mit typischen Energien im Festkörper kommt eine Wellenlänge im
  Bereich von **Nanometern** heraus — also in der Größenordnung der **Atomabstände** im Kristall. Genau dann,
  wenn Wellenlänge und „Hindernisse" ähnlich groß sind, zeigt sich Wellenverhalten (deshalb beugen Davisson und
  Germer 1927 Elektronen erfolgreich an einem Kristallgitter).

**Die Faustregel:** Quanteneffekte werden wichtig, sobald ein Teilchen leicht ist und auf kleinem Raum
eingesperrt wird — und das trifft auf Elektronen in Atomen und Festkörpern voll zu. Für Alltagsobjekte ist die
klassische Physik eine hervorragende Näherung, eben weil ihre de-Broglie-Wellenlänge verschwindend klein ist.

:::grafik
Ein Größenvergleich: oben ein Tennisball mit der Angabe $\lambda \approx 10^{-34}\,\text{m}$ (daneben zum
Vergleich ein Atom, das riesig dagegen wirkt) — „keine Welle sichtbar". Unten ein Elektron mit $\lambda$ im
Nanometer-Bereich, als sichtbare Welle eingezeichnet neben einem Kristallgitter gleicher Größenordnung —
„Wellenverhalten zeigt sich".
:::

## Die Wellenfunktion und ihre Bedeutung

Wenn das Elektron eine Welle ist, muss man beschreiben, **was** da schwingt. Diese Beschreibung ist die
__Wellenfunktion__ $\psi(x, t)$ (griechisch „psi"). Sie ist zunächst eine mathematische Größe (im Allgemeinen
komplexwertig) und — anders als eine Wasserwelle — **kein** direkt messbares physikalisches Feld.

Ihre physikalische Bedeutung liefert die __Born'sche Regel__: Das **Betragsquadrat** der Wellenfunktion ist die
__Aufenthaltswahrscheinlichkeitsdichte__. Genauer gibt

$$|\psi(x)|^2\,\mathrm{d}x$$

die Wahrscheinlichkeit an, das Elektron im kleinen Bereich zwischen $x$ und $x + \mathrm{d}x$ zu finden. Die
Welle sagt uns also nicht, *wo das Elektron ist*, sondern *wie wahrscheinlich* es ist, es an einem bestimmten Ort
anzutreffen. Daraus folgt direkt eine sinnvolle Bedingung, die __Normierung__: Da sich das Elektron
**irgendwo** aufhalten muss, ist die Summe aller Wahrscheinlichkeiten eins, $\int |\psi|^2\,\mathrm{d}x = 1$.

Das erklärt auch das Doppelspalt-Rätsel: Die Welle $\psi$ geht durch beide Spalte und interferiert; wo $|\psi|^2$
groß ist, schlagen viele Elektronen ein (helle Streifen), wo es null ist, keine (dunkle Streifen). Das einzelne
Elektron trifft zufällig auf, aber die **Verteilung** vieler Elektronen folgt genau $|\psi|^2$.

:::grafik
Oben eine Wellenfunktion $\psi(x)$ (eine schwingende Kurve, die auch negativ wird). Darunter ihr Betragsquadrat
$|\psi(x)|^2$ (immer $\ge 0$) als „Wahrscheinlichkeitswolke": dort, wo $|\psi|^2$ hoch ist, ein dichter
Punkteschleier (Elektron wahrscheinlich), wo es null ist, keine Punkte. Beschriftung: Fläche unter $|\psi|^2$ gleich 1.
:::

## Einsperren erzeugt diskrete Energien

Jetzt kommt der rote Faden aller folgenden Artikel — und die Antwort auf die Eingangsfrage, warum Atome nur bestimmte
Energien haben. Die Analogie dazu kennt jeder: eine __Gitarrensaite__.

Eine zwischen zwei festen Punkten eingespannte Saite kann nicht beliebig schwingen. An den Enden muss sie fest
sein, und das erlauben nur bestimmte __stehende Wellen__: der Grundton (eine halbe Wellenlänge passt auf die
Saite), der erste Oberton (eine ganze Wellenlänge), und so weiter. Nur Wellenlängen, die „ganzzahlig passen",
überleben; alle anderen löschen sich bei der Reflexion selbst aus. Deshalb klingt eine Saite in bestimmten
Tönen, nicht in jeder beliebigen Frequenz.

Mit einem eingesperrten **Elektron** ist es genau dasselbe. Sperrt man seine Welle in einen Bereich der Länge
$L$ ein (zwischen zwei „Wänden"), passen nur stehende Wellen mit den Wellenlängen

$$\lambda_n = \frac{2L}{n}, \qquad n = 1, 2, 3, \ldots$$

Und hier schließt sich der Kreis zur de-Broglie-Beziehung: Zu jeder erlaubten Wellenlänge gehört über
$p = h/\lambda$ ein bestimmter Impuls und damit eine bestimmte **Energie**. Weil nur bestimmte Wellenlängen
passen, sind auch nur bestimmte, **diskrete Energien** erlaubt — man sagt, die Energie ist __quantisiert__. Die
scharfen Spektrallinien der Atome sind genau das: Übergänge zwischen diesen erlaubten Energiestufen.

Das ist die Kernmaschinerie des ganzen Themenbereichs: **Räumliche Einschränkung einer Welle ⇒ diskrete Energien.**
Alles Weitere — Teilchen in der Box, Atomorbitale, Energiebänder im Kristall — ist dieselbe Idee, nur mit
anderer Form und Dimension des „Kastens".

:::grafik
Nebeneinander: Links die eingespannte Gitarrensaite mit ihren stehenden Wellen (Grundton = halbe Wellenlänge,
Obertöne mit $n = 2, 3, \ldots$). Rechts ein in eine Box der Länge $L$ eingesperrtes Elektron mit genau denselben
stehenden Wellenmustern $\psi_n$ und der Bedingung $\lambda_n = 2L/n$. Darunter eine Energieleiter mit diskreten
Stufen $E_1, E_2, E_3, \ldots$ — „nur bestimmte Energien erlaubt".
:::

:::kern
Ein Elektron verhält sich wie eine __Welle__ — das zeigt die Interferenz im __Doppelspalt__ (einzelne Einschläge,
aber Wellen-Verteilung) und die Elektronenbeugung. Jedem Teilchen gehört die __de-Broglie-Wellenlänge__
$\lambda = h/p$; weil $h$ winzig ist, zeigt sich Wellenverhalten nur bei leichten, eng eingesperrten Teilchen
(Elektronen in Atomen/Festkörpern), nicht im Alltag. Die __Wellenfunktion__ $\psi$ beschreibt das Elektron; nach
der __Born'schen Regel__ ist $|\psi|^2$ die __Aufenthaltswahrscheinlichkeitsdichte__ (mit $\int|\psi|^2\mathrm{d}x = 1$).
Der rote Faden: **Sperrt man eine Welle ein, passen nur bestimmte stehende Wellen** ($\lambda_n = 2L/n$) — und
damit sind nur __diskrete Energien__ erlaubt (Quantisierung). Das erklärt die scharfen Spektrallinien der Atome.
:::

Damit steht das Bild: Elektronen sind Wellen, und eingesperrte Wellen haben diskrete Energien. Was noch fehlt,
ist die **Bewegungsgleichung** für diese Wellen — die Gleichung, die festlegt, welche Form $\psi$ in einem
gegebenen Potential annimmt. Das ist die __Schrödinger-Gleichung__, das Thema des nächsten Abschnitts.

:::quiz
F: Warum widerlegen die scharfen Spektrallinien der Atome das klassische „Kugel-auf-Bahn"-Bild?
A: Eine kreisende Kugel könnte jede beliebige Bahn und damit jede Energie annehmen, sodass das Atom Licht aller Farben aussenden müsste. Dass nur wenige scharfe Linien auftreten, bedeutet, dass das Elektron nur ganz bestimmte, diskrete Energien haben darf — das verlangt eine neue Physik.
F: Warum wäre ein klassisches Atom instabil?
A: Eine kreisende Ladung müsste nach der klassischen Elektrodynamik ständig Energie abstrahlen und innerhalb von Sekundenbruchteilen in den Kern stürzen. Da Atome seit Milliarden Jahren stabil sind, kann das klassische Bild nicht stimmen.
F: Was genau zeigt der Doppelspalt mit einzeln abgeschossenen Elektronen?
A: Jedes Elektron schlägt als einzelner Punkt ein (Teilchencharakter), doch die Verteilung vieler Einschläge bildet ein Interferenzmuster (Wellencharakter). Jedes Elektron muss also gewissermaßen durch beide Spalte zugleich gegangen sein und mit sich selbst interferiert haben.
F: Warum ist die Bezeichnung „Welle-Teilchen-Dualismus" eigentlich etwas irreführend?
A: Das Elektron ist weder eine kleine Kugel noch eine Wasserwelle, sondern ein eigenständiges Quantenobjekt. „Welle" und „Teilchen" sind nur zwei Modelle, die je nach Experiment die eine oder andere Seite seines Verhaltens beschreiben.
F: Warum bemerkt man die Wellennatur bei einem Tennisball nicht, bei einem Elektron aber schon?
A: Die de-Broglie-Wellenlänge $\lambda=h/(mv)$ ist wegen des winzigen $h$ für große, schwere Objekte absurd klein (beim Ball $\sim10^{-34}$ m). Das leichte Elektron hat dagegen Wellenlängen im Nanometerbereich — vergleichbar mit Atomabständen, wo Wellenverhalten sichtbar wird.
F: Unter welchen Bedingungen werden Quanteneffekte überhaupt wichtig?
A: Sobald ein Teilchen leicht ist und auf kleinem Raum eingesperrt wird, sodass seine de-Broglie-Wellenlänge in der Größenordnung der „Hindernisse" liegt. Das trifft auf Elektronen in Atomen und Festkörpern zu, nicht auf Alltagsobjekte.
F: Was beschreibt die Wellenfunktion $\psi$, und ist sie selbst messbar?
A: $\psi(x,t)$ ist eine (im Allgemeinen komplexwertige) mathematische Größe, die das Elektron als Welle beschreibt. Anders als eine Wasserwelle ist sie kein direkt messbares Feld; messbar ist erst ihr Betragsquadrat.
F: Was besagt die Born'sche Regel, und warum muss $\int|\psi|^2\,dx=1$ gelten?
A: $|\psi(x)|^2\,dx$ ist die Wahrscheinlichkeit, das Elektron zwischen $x$ und $x+dx$ zu finden — die Welle gibt nicht den Ort, sondern die Aufenthaltswahrscheinlichkeit. Da sich das Elektron irgendwo aufhalten muss, ist die Summe aller Wahrscheinlichkeiten eins (Normierung).
F: Wie erklärt die Wellenfunktion das Doppelspalt-Muster?
A: $\psi$ geht durch beide Spalte und interferiert; wo $|\psi|^2$ groß ist, schlagen viele Elektronen ein (helle Streifen), wo es null ist, keine (dunkle). Das einzelne Elektron trifft zufällig auf, aber die Verteilung vieler folgt exakt $|\psi|^2$.
F: Warum führt das Einsperren einer Welle zu diskreten Energien?
A: Wie bei einer eingespannten Saite überleben nur stehende Wellen, die „ganzzahlig passen" ($\lambda_n=2L/n$). Über $p=h/\lambda$ gehört zu jeder erlaubten Wellenlänge ein bestimmter Impuls und damit eine bestimmte Energie — also sind nur diskrete Energien möglich (Quantisierung), was die Spektrallinien erklärt.
:::
