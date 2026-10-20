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

:::quiz
F: Was bedeutet Verstärkung beim Transistor anschaulich?
A: Ein kleines Eingangssignal „reitet" als winzige Schwankung auf dem festen Arbeitspunkt und steuert eine große, formgleiche Ausgangsgröße. Eine kleine Änderung von $u_{BE}$ erzeugt über den Kollektorstrom einen großen Spannungshub an $R_C$.
F: Warum muss das Signal für lineare Verstärkung klein bleiben?
A: Nur bei kleiner Aussteuerung darf man die gekrümmte Kennlinie durch ihre Tangente im Arbeitspunkt ersetzen. Dann gelten konstante lineare Faktoren; bei großer Aussteuerung würde die Krümmung das Signal verzerren.
F: Warum trennt man Groß- und Kleinsignal?
A: Der Gleichanteil legt den Arbeitspunkt fest, der Wechselanteil ist das eigentliche Signal. Die Trennung erlaubt es, den nichtlinearen Gleich-Arbeitspunkt getrennt zu bestimmen und für das Signal mit einem einfachen linearen Modell zu rechnen.
F: Was beschreibt die Steilheit $g_m$?
A: Sie gibt an, wie stark der Kollektorstrom auf eine kleine Änderung der Basis-Emitter-Spannung reagiert ($i_C=g_m u_{BE}$). Sie ist die lokale Steigung der Übertragungskennlinie im Arbeitspunkt.
F: Warum hängt $g_m=I_C/U_T$ nur vom Arbeitspunktstrom ab?
A: Sie folgt aus dem Ableiten der exponentiellen Kennlinie und ergibt gerade $I_C/U_T$ — unabhängig vom einzelnen Transistor. Ein größerer Arbeitspunktstrom macht den Verstärker „steiler".
F: Wie hängen $r_{BE}$ und $g_m$ zusammen?
A: Über $r_{BE}=\beta/g_m=\beta U_T/I_C$. Der Eingangswiderstand ist also die Stromverstärkung geteilt durch die Steilheit und sinkt mit steigendem Arbeitspunktstrom.
F: Wie wird der Transistor im Kleinsignal-Ersatzschaltbild dargestellt?
A: Als gesteuerte Stromquelle $g_m u_{BE}$ am Ausgang mit dem Eingangswiderstand $r_{BE}$ zwischen Basis und Emitter. Dieses lineare Modell ersetzt den Transistor für die Wechselanteile.
F: Woher kommt das Minuszeichen in $v_U=-g_m R_C$?
A: Ein größerer Kollektorstrom erzeugt einen größeren Abfall an $R_C$, was die Kollektorspannung absinken lässt. Steigende Eingangsspannung führt also zu fallender Ausgangsspannung — die Emitterschaltung invertiert.
F: Wie erreicht die Emitterschaltung Verstärkungen von mehreren Hundert?
A: Mit $v_U=-\tfrac{I_C}{U_T}R_C$: Bei $I_C=2\,$mA ist $g_m\approx77\,$mS, mit $R_C=3{,}3\,$kΩ ergibt sich $v_U\approx-254$. Hohe Steilheit mal großer Kollektorwiderstand liefert den großen Betrag.
F: Welchen Kompromiss bedeutet ein für das Signal wirksamer Emitterwiderstand?
A: Ohne Überbrückungskondensator sinkt die Verstärkung auf $v_U\approx-R_C/R_E$ — deutlich kleiner, aber unabhängig von $g_m$ und damit stabiler gegen Exemplarstreuung und Temperatur. Man wählt zwischen maximaler Verstärkung und Stabilität.
:::
