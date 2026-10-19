---
title: Der Transistor als Verstärker
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110500
summary: Wie aus dem Transistoreffekt eine echte Verstärkung wird – das Signal als kleine Schwingung um den Arbeitspunkt, das Kleinsignal-Ersatzschaltbild und die Spannungsverstärkung der Emitterschaltung.
tags: Verstärker, Kleinsignal, Ersatzschaltbild, Steilheit, Spannungsverstärkung, Emitterschaltung
---

:::konzept
Verstärkung heißt: Ein kleines Eingangssignal steuert eine große, formgleiche Ausgangsgröße. Beim Transistor
„reitet" das Signal als winzige Schwankung auf dem festen **Arbeitspunkt**. Eine kleine Änderung der
Basis-Emitter-Spannung bewirkt eine große Änderung des Kollektorstroms, und dieser erzeugt am
Kollektorwiderstand einen großen Spannungshub — das verstärkte (und umgekehrte) Signal. Entscheidend ist, dass
die Schwankung **klein** bleibt, damit der Transistor im linearen Bereich arbeitet.
:::

**Worum es geht:** Der Arbeitspunkt steht (voriger Abschnitt). Jetzt überlagern wir ihm ein Signal und rechnen
die __Verstärkung__ aus. Dafür trennt man Gleich- und Wechselanteil (__Groß-__ und __Kleinsignal__) und nutzt
ein lineares __Kleinsignal-Ersatzschaltbild__.

## Groß- und Kleinsignal

Jede Spannung und jeder Strom im Verstärker besteht aus zwei Teilen: dem festen __Gleichanteil__, der den
Arbeitspunkt bildet, und dem kleinen __Wechselanteil__, dem eigentlichen Signal. Man schreibt zum Beispiel
$u_\text{BE}(t) = U_\text{BE,AP} + \hat{u}_\text{BE}(t)$ — ein konstanter Betriebswert plus eine kleine
Schwingung.

Solange die Schwingung **klein** ist, darf man die gekrümmte Transistorkennlinie in der Umgebung des
Arbeitspunkts durch ihre **Tangente** ersetzen (lineare Näherung). Dann gelten für die Wechselanteile einfache
lineare Beziehungen — das ist der __Kleinsignalbetrieb__. Nur deshalb lässt sich die Verstärkung überhaupt mit
einem konstanten Faktor beschreiben.

:::grafik
Oben die Übertragungskennlinie mit dem Arbeitspunkt und einer kleinen Sinus-Aussteuerung am Eingang; über die
Tangente im AP wird daraus am Ausgang eine große, aber gegenphasige Sinusschwingung. Pfeile zeigen: kleines
$\hat{u}_\text{BE}$ → großes $\hat{u}_\text{CE}$, invertiert.
:::

## Das Kleinsignal-Ersatzschaltbild

Für die Wechselanteile ersetzt man den Transistor durch ein einfaches lineares Modell mit zwei Kennwerten:

- __$r_\text{BE}$__: der __Kleinsignal-Eingangswiderstand__ zwischen Basis und Emitter — er verknüpft die kleine
  Basisspannung mit dem kleinen Basisstrom.
- __$g_\text{m}$__: die __Steilheit__ (Transkonduktanz) — sie sagt, wie stark der Kollektorstrom auf eine
  Änderung der Basis-Emitter-Spannung reagiert, $i_\text{C} = g_\text{m}\cdot u_\text{BE}$.

Beide folgen aus dem Arbeitspunkt (durch Ableiten der exponentiellen Kennlinie, genau wie beim differentiellen
Widerstand der Diode):

$$g_\text{m} = \frac{I_\text{C}}{U_\text{T}}, \qquad r_\text{BE} = \frac{\beta}{g_\text{m}} = \frac{\beta\,U_\text{T}}{I_\text{C}}.$$

- __$I_\text{C}$__: der __Kollektorstrom__ im Arbeitspunkt.
- __$U_\text{T}$__: die __Temperaturspannung__ ($\approx 26\,\text{mV}$).
- __$\beta$__: die __Stromverstärkung__.

Bemerkenswert: Die Steilheit hängt **nur** vom Arbeitspunktstrom ab, nicht vom einzelnen Transistor — ein
größerer Arbeitspunktstrom macht den Verstärker „steiler".

:::grafik
Das Kleinsignal-Ersatzschaltbild der Emitterschaltung: am Eingang zwischen Basis und Emitter der Widerstand
$r_\text{BE}$, am Ausgang eine gesteuerte Stromquelle $g_\text{m}\,u_\text{BE}$ parallel zum Kollektorwiderstand
$R_\text{C}$. Ein- und Ausgangsklemmen beschriftet.
:::

## Die Spannungsverstärkung der Emitterschaltung

Jetzt ist die Verstärkung in zwei Zeilen hergeleitet. Der gesteuerte Kollektorstrom $i_\text{C} =
g_\text{m}\,u_\text{BE}$ fließt durch den Kollektorwiderstand $R_\text{C}$ und erzeugt dort die
Ausgangsspannung $u_\text{CE} = -i_\text{C}\,R_\text{C}$ (das Minus, weil ein größerer Strom die Spannung am
Kollektor **absinken** lässt). Einsetzen und durch $u_\text{BE}$ teilen ergibt die __Spannungsverstärkung__:

$$v_U = \frac{u_\text{CE}}{u_\text{BE}} = -\,g_\text{m}\cdot R_\text{C} = -\frac{I_\text{C}}{U_\text{T}}\,R_\text{C}.$$

- __$v_U$__: die __Spannungsverstärkung__.
- __$g_\text{m}$__: die __Steilheit__.
- __$R_\text{C}$__: der __Kollektorwiderstand__.

Das negative Vorzeichen bedeutet, dass die Emitterschaltung **invertiert** — steigt die Eingangsspannung, sinkt
die Ausgangsspannung. Der Betrag kann leicht im Bereich von einigen Hundert liegen. Ein Zahlenbeispiel: Bei
$I_\text{C} = 2\,\text{mA}$ ist $g_\text{m} = 2\,\text{mA}/26\,\text{mV} \approx 77\,\text{mS}$, und mit
$R_\text{C} = 3{,}3\,\text{k}\Omega$ wird $v_U \approx -254$ — ein Eingangssignal von $10\,\text{mV}$ erscheint am
Ausgang als $2{,}5\,\text{V}$.

Hier schließt sich der Kreis zum Emitterwiderstand: Ließe man $R_\text{E}$ auch für das Signal wirksam (ohne
Überbrückungskondensator), sänke die Verstärkung auf $v_U \approx -R_\text{C}/R_\text{E}$ — stabiler, aber
schwächer. Man wählt den Kompromiss je nach Anwendung.

:::grafik
Die durchgerechnete Emitterschaltung mit eingezeichnetem kleinen Eingangssignal ($10\,\text{mV}$) und dem großen,
invertierten Ausgangssignal ($2{,}5\,\text{V}$), dazu die Kennwerte $g_\text{m} \approx 77\,\text{mS}$,
$R_\text{C} = 3{,}3\,\text{k}\Omega$, $v_U \approx -254$.
:::

:::kern
Verstärkung heißt: ein kleines Signal schwingt um den __Arbeitspunkt__ (__Kleinsignalbetrieb__, lineare Näherung
der Kennlinie). Im __Kleinsignal-Ersatzschaltbild__ ist der Transistor eine gesteuerte Stromquelle mit der
__Steilheit__ $g_\text{m} = I_\text{C}/U_\text{T}$ und dem Eingangswiderstand $r_\text{BE} = \beta/g_\text{m}$.
Die __Emitterschaltung__ hat die __Spannungsverstärkung__ $v_U = -g_\text{m}R_\text{C} = -\dfrac{I_\text{C}}{U_\text{T}}R_\text{C}$
— groß und __invertierend__. Ein wirksamer Emitterwiderstand senkt sie auf $-R_\text{C}/R_\text{E}$ (stabiler,
aber kleiner).
:::

Ein einzelner Transistor verstärkt also kräftig, aber die Verstärkung hängt noch von Bauteilwerten und
Arbeitspunkt ab. Kombiniert man viele Transistoren zu einem fertigen Baustein mit riesiger Verstärkung, entsteht
das vielleicht vielseitigste analoge Bauteil: der __Operationsverstärker__.
