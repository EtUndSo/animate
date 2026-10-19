---
title: Der Tunneleffekt
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Quantenmechanik
order: 4010600
summary: Warum ein Elektron eine Wand durchdringen kann, die es klassisch niemals überwinden dürfte – von der endlich hohen Potentialstufe (die Welle leckt exponentiell in das verbotene Gebiet) über die dünne Barriere (die Welle kommt auf der anderen Seite heraus) bis zur Tunnelwahrscheinlichkeit und ihrer extremen Empfindlichkeit, auf der das Rastertunnelmikroskop beruht.
tags: Tunneleffekt, Potentialbarriere, Potentialstufe, evaneszente Welle, Transmissionswahrscheinlichkeit, Rastertunnelmikroskop
---

:::grafik
Einstiegs-Animation: Ein Wellenpaket (Elektron) läuft von links auf eine rechteckige Barriere zu, die **höher**
ist als seine Energie. Ein Teil wird reflektiert und läuft zurück. Innerhalb der Barriere **klingt** die Welle
nicht oszillierend, sondern exponentiell ab. Ist die Barriere dünn genug, tritt auf der rechten Seite ein
kleineres Wellenpaket wieder aus und läuft weiter — das Elektron hat die Wand **durchtunnelt**. Kernbotschaft:
Was eine klassische Kugel niemals schafft (über einen zu hohen Berg zu kommen), gelingt der Elektronen-Welle mit
einer gewissen Wahrscheinlichkeit.
:::

:::konzept
Beim Teilchen in der Box waren die Wände unendlich hoch — die Welle war dort exakt null, das Elektron perfekt
gefangen. Echte Barrieren sind aber **endlich** hoch. Dann zeigt sich einer der verblüffendsten Quanteneffekte:
Die Elektronen-Welle hört an der Wand nicht abrupt auf, sondern **dringt ein Stück hinein** — und wenn die Wand
dünn ist, sogar **hindurch**. Ein Elektron kann so in einem Gebiet auftauchen, das es nach der klassischen Physik
(zu wenig Energie) gar nicht erreichen dürfte. Dieser **Tunneleffekt** ist nicht nur Kuriosität, sondern die
Grundlage des Rastertunnelmikroskops, der Tunneldiode und des Flash-Speichers.
:::

**Worum es geht:** Wir lassen eine Elektronen-Welle auf eine endlich hohe __Potentialstufe__ und dann auf eine
__Potentialbarriere__ treffen. Dabei leiten wir her, *warum* die Welle in das klassisch verbotene Gebiet
eindringt, wie sie eine dünne Wand durchtunnelt, und *warum* die __Tunnelwahrscheinlichkeit__ so extrem
empfindlich von der Wanddicke abhängt.

## Die Potentialstufe: was klassisch passiert — und was quantenmechanisch

Betrachten wir die einfachste „Wand": eine Stufe, bei der das Potential von $0$ auf einen festen Wert $V_0$
springt. Ein Elektron komme von links mit der Energie $E$, und zwar mit **weniger** Energie als die Stufe hoch
ist: $E < V_0$.

- **Klassisch** ist der Fall klar: Eine Kugel mit zu wenig Energie wird an der Wand **vollständig
  reflektiert**. Sie kann das Gebiet hinter der Stufe **nie** betreten — dort wäre ihre kinetische Energie
  negativ, was unmöglich ist. Dieses Gebiet heißt deshalb das __klassisch verbotene Gebiet__.
- **Quantenmechanisch** stimmt das nicht ganz. Zwar wird die Welle überwiegend reflektiert — aber sie
  verschwindet an der Wand nicht schlagartig, sondern reicht ein Stück in die Stufe hinein.

:::grafik
Eine Potentialstufe (links $V=0$, rechts $V=V_0$) mit der Energie $E < V_0$ als waagerechter Linie. Oben der
klassische Fall: eine Kugel prallt an der Wand ab (Pfeil zurück), das Gebiet rechts ist „verboten". Unten der
quantenmechanische Fall: die Welle oszilliert links, geht an der Stufe stetig über und klingt rechts
exponentiell ab (reicht also ein Stück ins verbotene Gebiet hinein).
:::

## Warum die Welle ins verbotene Gebiet eindringt

Der Grund steckt direkt in der stationären Schrödinger-Gleichung. Im Gebiet hinter der Stufe ($V = V_0$) lautet
sie umgestellt

$$\psi''(x) = \frac{2m\,(V_0 - E)}{\hbar^2}\,\psi(x) = +\,\kappa^2\,\psi(x), \qquad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}.$$

Der entscheidende Punkt ist das **Vorzeichen**. Innerhalb der erlaubten Bereiche (dort war $E > V$) stand rechts
$-k^2\psi$ mit einer **oszillierenden** Lösung ($\sin$, $\cos$, ebene Welle). Jetzt ist $V_0 > E$, also $V_0 - E >
0$, und rechts steht $+\kappa^2\psi$ — und diese Gleichung hat **keine** oszillierende, sondern eine
**exponentielle** Lösung:

$$\psi(x) = \psi(0)\,e^{-\kappa x} \qquad (\text{im verbotenen Gebiet}).$$

- __$\kappa$__: die __Abklingkonstante__ — je höher und „verbotener" die Stufe ($V_0 - E$ groß), desto schneller
  klingt die Welle ab.
- __$\psi(0)$__: der Wert der Wellenfunktion direkt an der Wand.

Man nennt eine solche exponentiell abklingende Welle __evaneszent__ („flüchtig"). Das Elektron ist im verbotenen
Gebiet also nicht streng null, aber seine Aufenthaltswahrscheinlichkeit $|\psi|^2 \propto e^{-2\kappa x}$ fällt
sehr schnell ab. **Warum nicht einfach null wie bei der unendlichen Box?** Weil dort $V_0 = \infty$ war, also
$\kappa = \infty$ — dann fällt die Welle unendlich schnell ab, ist sofort null. Bei endlicher Höhe ist das
Abklingen endlich schnell, und die Welle leckt ein Stück hinein.

## Die Potentialbarriere: Durchtunneln

Jetzt kommt der eigentliche Tunneleffekt. Eine __Potentialbarriere__ ist eine Stufe von **endlicher Dicke** $d$:
hinter ihr ist das Potential wieder niedrig. Die Welle klingt in der Barriere exponentiell ab — aber wenn die
Barriere **dünn** genug ist, ist sie am anderen Ende noch nicht ganz auf null gefallen. Dort findet die Welle
wieder ein erlaubtes Gebiet und läuft als normale, oszillierende Welle weiter. Es gibt also eine von null
verschiedene Wahrscheinlichkeit, das Elektron **hinter** der Barriere anzutreffen — es ist hindurchgetunnelt.

:::grafik
Eine rechteckige Barriere der Höhe $V_0$ und Dicke $d$, Energie $E < V_0$. Die Wellenfunktion: links eine
oszillierende, einlaufende Welle (plus reflektierter Anteil), in der Barriere exponentieller Abfall $e^{-\kappa
x}$, rechts eine wieder oszillierende, aber **kleinere** Welle (die durchgetunnelte). Die Amplituden-Höhen sind
markiert, um den „Verlust" beim Durchqueren zu zeigen.
:::

## Die Tunnelwahrscheinlichkeit

Wie wahrscheinlich das Durchtunneln ist, misst die __Transmissionswahrscheinlichkeit__ $T$. Für eine
hinreichend dicke/hohe Barriere wird sie vom exponentiellen Abfall dominiert:

$$T \approx e^{-2\kappa d}, \qquad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}.$$

- __$T$__: die __Tunnelwahrscheinlichkeit__ (Anteil der Elektronen, der durchkommt).
- __$d$__: die __Dicke__ der Barriere.
- __$\kappa$__: die __Abklingkonstante__ (von Barrierenhöhe und Elektronenergie abhängig).

**Woher der Faktor 2?** Die Wellen-**Amplitude** fällt über die Dicke $d$ um $e^{-\kappa d}$ ab. Die
**Wahrscheinlichkeit** ist aber das Betragsquadrat der Amplitude — und Quadrieren verdoppelt den Exponenten:
$(e^{-\kappa d})^2 = e^{-2\kappa d}$.

Entscheidend ist die Form der Formel: $T$ hängt **exponentiell** von der Dicke $d$ ab. Das macht das Tunneln
extrem empfindlich — macht man die Barriere nur ein kleines bisschen dicker, bricht die Tunnelwahrscheinlichkeit
dramatisch ein. Genau diese Empfindlichkeit ist technisch Gold wert.

:::grafik
Ein Diagramm $T$ über der Barrierendicke $d$: eine steil abfallende Exponentialkurve $T = e^{-2\kappa d}$.
Markiert, wie eine kleine Änderung von $d$ (etwa um einen Atomdurchmesser) $T$ um Größenordnungen ändert —
„exponentiell empfindlich".
:::

## Anwendung: das Rastertunnelmikroskop und mehr

Die extreme Abstandsabhängigkeit des Tunnelns ist die Grundlage des __Rastertunnelmikroskops__ (STM, *scanning
tunneling microscope*). Eine feine Metallspitze wird bis auf wenige Atomdurchmesser an eine Oberfläche gebracht;
der Spalt dazwischen ist die Tunnelbarriere. Weil der Tunnelstrom wie $I \propto e^{-2\kappa d}$ vom Abstand
abhängt, ändert er sich schon bei einer Abstandsänderung von einem einzigen Atomdurchmesser um ein Vielfaches.
Rastert man die Spitze über die Oberfläche und hält den Strom konstant, bildet man **einzelne Atome** ab — ganz
ohne Licht. (Binnig und Rohrer erhielten dafür 1986 den Physik-Nobelpreis.)

Der Tunneleffekt steckt in vielen weiteren Bauelementen und Phänomenen:

- **Tunneldiode** — nutzt das Durchtunneln für extrem schnelle, negativ-differentielle Kennlinien.
- **Flash-Speicher** — Elektronen tunneln durch eine dünne Oxidschicht auf ein „Floating Gate" und bleiben dort
  als gespeichertes Bit.
- **Alpha-Zerfall** — ein Alphateilchen tunnelt aus dem Atomkern heraus.

:::grafik
Das STM-Prinzip: eine atomar feine Spitze über einer Oberfläche aus einzelnen Atomen, dazwischen der Spalt $d$
als Tunnelbarriere; ein Pfeil „Tunnelstrom $I \propto e^{-2\kappa d}$". Daneben angedeutet, wie die Spitze
zeilenweise abrastert und daraus ein atomar aufgelöstes Bild entsteht.
:::

:::kern
An einer **endlich** hohen Stufe ($E < V_0$) dringt die Elektronen-Welle in das __klassisch verbotene Gebiet__
ein: Dort steht in der Schrödinger-Gleichung $\psi'' = +\kappa^2\psi$ (statt $-k^2\psi$), die Lösung ist nicht
oszillierend, sondern __evaneszent__ $\psi \propto e^{-\kappa x}$ mit $\kappa = \sqrt{2m(V_0-E)}/\hbar$. Bei einer
**dünnen** __Barriere__ (Dicke $d$) ist die Welle am anderen Ende noch nicht null → das Elektron __tunnelt
hindurch__. Die __Tunnelwahrscheinlichkeit__ $T \approx e^{-2\kappa d}$ (Faktor 2 vom Betragsquadrat der
Amplitude) hängt **exponentiell** von $d$ ab. Diese extreme Abstandsempfindlichkeit ist die Grundlage des
__Rastertunnelmikroskops__ (atomare Auflösung) sowie von Tunneldiode, Flash-Speicher und Alpha-Zerfall.
:::

Dass die Welle in eine endliche Wand eindringt, hat auch Folgen, wenn das Elektron in einem Kasten mit
**endlich** hohen Wänden sitzt: Die Welle leckt in die Wände, passt dadurch „etwas lockerer" in den Kasten, und
die Energien verschieben sich. Das ist das Thema des nächsten Abschnitts, der __endlich hohen Box__.
