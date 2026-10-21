---
title: Die Diode und ihre Kennlinie
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100300
summary: Von Grund auf – wie aus dem pn-Übergang ein Bauteil mit Anode und Kathode wird, warum sein Strom exponentiell mit der Spannung wächst und was die Shockley-Gleichung über Durchlass, Sperren und die Schleusenspannung sagt. Leitbild bleibt das Parkhaus mit der Rampe zwischen p- und n-Seite. Mit Aufbau, Schaltsymbol und Zählpfeilen, Shockley-Gleichung und Temperaturspannung, Kennlinie, Schleusenspannung und Temperaturgang, Durchbruch durch Lawinen- und Zener-Effekt sowie den Spezialdioden des Skripts: Z-Diode zur Spannungsstabilisierung, Kapazitätsdiode, Fotodiode und Solarzelle, dazu die Leuchtdiode. Mit Beispiel-Seite.
tags: Diode, pn-Übergang, Durchlassrichtung, Sperrrichtung, Schleusenspannung, Shockley-Gleichung, Z-Diode
---

## Anschaulich

Der vorige Artikel endete mit dem pn-Übergang als Ventil. Dieser Artikel macht daraus ein Bauteil mit zwei Anschlüssen, beschreibt es durch eine einzige
Gleichung, die __Kennlinie__ der Diode, und zeigt die Spezialdioden, die einzelne Seiten dieses Ventils gezielt ausnutzen.

**Das Leitbild bleibt:** **das Parkhaus mit der Rampe.** Zwei Parkhäuser stehen nebeneinander, das der p-Seite und das der n-Seite, und zwischen ihren
Oberdecks liegt eine Rampe der Höhe $e\,U_\text{Diff}$. Die äußere Spannung hebt oder senkt das p-Parkhaus und verstellt damit die Rampe. Den Hinstrom bilden
Autos, die die Rampe hinauffahren, den Rückstrom die wenigen, die von drüben hinunterrollen.

Vier Folgerungen:

- **Steil in der einen, flach in der anderen Richtung.** Senkt man die Rampe, vervielfacht sich der Verkehr hinauf mit jedem Stück; hebt man sie, bleibt
  das stetige Rinnsal, das herunterrollt. Daraus wird die ungleiche Kennlinie: großer Strom in Durchlassrichtung, ein winziger, fester Strom in
  Sperrrichtung.
- **Ein Knie statt einer Schwelle.** Weil schon $60\,\text{mV}$ den Strom verzehnfachen, steigt er innerhalb weniger Zehntelvolt von Nanoampere auf
  Milliampere. In linearer Darstellung sieht das aus wie eine Schwelle bei $0{,}6$ bis $0{,}7\,\text{V}$.
- **Eine zu steile Rampe gibt nach.** Bei sehr großer Sperrspannung wird die Rampe zur steilen, dünnen Wand. Autos gelangen dann durch die Wand hindurch,
  oder sie werden beim Hinabrollen so schnell, dass sie andere aus ihren Plätzen stoßen: der Durchbruch, den die Z-Diode nutzt.
- **Die leere Zone und das Licht.** Zwischen den Parkhäusern liegt eine Zone ohne Autos, nur mit geladenen Plattformen; sie wirkt wie der Spalt eines
  Kondensators, den die Spannung breiter oder schmaler macht. Und Licht, das in dieser Zone Autos aufs Oberdeck hebt, lässt sie die Rampe hinunterrollen:
  ein Strom aus Licht.

| Im Parkhaus | An der Diode |
|---|---|
| Eingang am p-Parkhaus | Anode |
| Eingang am n-Parkhaus | Kathode |
| Autos, die die Rampe hinauffahren | Hinstrom der Majoritätsträger |
| Autos, die von drüben hinunterrollen | Sättigungssperrstrom $I_S$ |
| Rampe wird zur dünnen, steilen Wand | Durchbruch, Zener- und Lawinen-Effekt |
| leere Zone zwischen den Parkhäusern | Sperrschicht, Sperrschichtkapazität |
| Licht hebt Autos in der leeren Zone | Fotostrom |

:::grafik
Szene: get1/halbleiterbauelemente/02-parkhaus-kennlinie · Vorlage: rampe-und-kennlinie
Links die beiden Parkhäuser des vorigen Artikels, p links und n rechts, zwischen ihren Oberdecks die Rampe; unter dem p-Parkhaus der Anschluss „Anode“, unter
dem n-Parkhaus „Kathode“. Ein Regler für die Spannung $U$ von $-2$ bis $+0{,}75\,\text{V}$ hebt oder senkt das p-Parkhaus; die Autos, die hinauffahren, werden
als dicker werdender Strom gezeigt, die wenigen, die herunterrollen, als dünner, gleich bleibender Strom. Rechts entsteht dabei die Kennlinie $I(U)$, mit
einem Umschalter zwischen linearer und logarithmischer Stromachse: logarithmisch eine Gerade mit einer Dekade je $59{,}5\,\text{mV}$, linear das Knie zwischen
$0{,}6$ und $0{,}7\,\text{V}$. Kernaussage: Die Kennlinie der Diode ist der Hinstrom über die verstellbare Rampe minus dem festen Rückstrom. (Rot = Rampe und
Spannung, blau = Autos und Ströme, orange = Kennlinienpunkt, grau = Parkhäuser und Achsen.)
:::

## Aufbau, Anschlüsse und Zählpfeile

Eine __pn-Diode__ besteht aus einem p-dotierten und einem n-dotierten Gebiet in einem Kristall, mit je einem Metallkontakt, wie Bild 10.6 des Skripts zeigt.
Der Anschluss am p-Gebiet heißt __Anode__, abgekürzt A, der am n-Gebiet __Kathode__, K. In der üblichen ebenen Bauform, dem Querschnitt in Bild 10.6, ist
das p-Gebiet von oben in eine n-dotierte Siliziumscheibe eindiffundiert, mit dem Anodenkontakt oben und dem Kathodenkontakt auf der Rückseite.

Das __Schaltsymbol__ ist ein Dreieck, das auf einen Querstrich zeigt. Das Dreieck zeigt in die Richtung, in die der Strom leicht fließt, von der Anode zur
Kathode; der Strich ist die Kathode, auf dem Bauteil meist durch einen Ring markiert.

Gezählt wird, wie im Skript, im Verbraucherzählpfeilsystem aus dem Artikel über Zählpfeile und Vorzeichen: Die Spannung $U$ und der Strom $I$ zählen beide von
der Anode zur Kathode. Positive $U$ bedeutet Durchlassrichtung, negative Sperrrichtung. Bei den Spezialdioden schreibt das Skript dieselbe Spannung als
$U_{AB}$, von A nach B.

**Im Bild:** Die Anode ist die Zufahrt zum p-Parkhaus, die Kathode die zum n-Parkhaus; eine positive Spannung senkt die Rampe zwischen ihnen.

## Die Shockley-Gleichung

Der vorige Artikel hat die beiden Ströme über die Rampe hergeleitet: den Hinstrom der Majoritätsträger, der mit der Spannung exponentiell wächst, und den
festen Rückstrom der Minoritätsträger. Der Strom durch die Diode ist ihr Unterschied.

**Die Akteure:**

- die Spannung $U$ in Volt und der Strom $I$ in Ampere, beide von der Anode zur Kathode gezählt;
- der __Sättigungssperrstrom__ $I_S$ in Ampere, eine kleine positive Größe, proportional zur Fläche des Übergangs und, wie im vorigen Artikel, zu $n_i^2$;
- die __Temperaturspannung__ $U_T$ in Volt, die Wärmeenergie $k_BT$ als Spannung ausgedrückt, bei $300\,\text{K}$ gleich $25{,}9\,\text{mV}$.

**Das Zusammenspiel:** *Welcher Strom bleibt übrig, wenn der Hinstrom über die verstellte Rampe und der feste Rückstrom gegeneinander laufen?*

:::formel Gesetz
$$I = I_S\,\Big(\exp\frac{U}{U_T} - 1\Big), \qquad U_T = \frac{k_B\,T}{e}.$$
:::

**So liest man das:** Eingabe ist die Spannung, Ausgabe der Strom. Ohne Spannung fließt kein Strom. In Durchlassrichtung wächst der Strom exponentiell, sobald
$U$ einige $U_T$ beträgt; die Eins ist dann unwichtig. In Sperrrichtung geht die Exponentialfunktion gegen null, und es bleibt $-I_S$, der kleine, von der
Spannung unabhängige Sperrstrom. Das ist die __Shockley-Gleichung__, nach William Shockley, der sie 1949 aus der Diffusion der Ladungsträger herleitete.

**Im Bild:** Autos, die hinauffahren, minus Autos, die herunterrollen. Ohne Spannung sind es gleich viele; jede Absenkung um $U_T$ vervielfacht die einen um
den Faktor $e$, die anderen bleiben, wie sie sind.

:::herleitung
**Die beiden Ströme.** Nach dem Satz des vorigen Artikels über Durchlass- und Sperrrichtung:

$$I_\text{hin}(U) = I_S\,\exp\frac{U}{U_T}, \qquad I_\text{rück} = I_S.$$

**Ihre Richtungen.** Den Hinstrom tragen Löcher von p nach n und Elektronen von n nach p; beide ergeben einen Strom von der Anode zur Kathode. Den Rückstrom
tragen Minoritätsträger in der Gegenrichtung, Elektronen von p nach n und Löcher von n nach p; das ist ein Strom von der Kathode zur Anode. Im
Verbraucherzählpfeilsystem ist der Diodenstrom also der Unterschied:

$$I = I_\text{hin}(U) - I_\text{rück} = I_S\,\exp\frac{U}{U_T} - I_S.$$

**Die Temperaturspannung.** Im Boltzmann-Faktor steht die Rampenhöhe $e\,(U_\text{Diff} - U)$ geteilt durch $k_BT$; teilt man Zähler und Nenner durch $e$,
steht dort die Spannung geteilt durch $k_BT/e$. Im Bild: Jedes Stück Rampenhöhe zählt in Einheiten des typischen Stoßes.
:::

Das Skript schreibt die Gleichung, als Gleichung 10.1, in der Form

$$I = I_s\,\exp\frac{e\,U}{k_B\,T}$$

und sagt, das Produkt $k_B\cdot T$ heiße thermische Spannung $U_T$. Das Produkt ist aber eine Energie, gemessen in Joule; die Spannung ist $k_BT$ geteilt
durch die Elementarladung, so wie oben. Die Gleichung des Skripts selbst stimmt, weil im Exponenten
das $e$ steht. Ihr fehlt aber die $-1$: Sie gilt nur im Durchlassbereich, wie das Skript auch sagt, und gibt bei $U = 0$ fälschlich $I_S$ statt null.

Reale Dioden weichen in zwei Punkten ab. Rekombination in der Raumladungszone streckt die Kennlinie; man schreibt dann $m\,U_T$ statt $U_T$, mit dem
__Idealitätsfaktor__ $m$ zwischen 1 und 2, in Datenblättern oft $n$ genannt. Und bei großen Strömen fällt zusätzlich Spannung am __Bahnwiderstand__ ab, dem
ohmschen Widerstand der neutralen Gebiete und Kontakte. Den Durchbruch bei großer Sperrspannung enthält die Gleichung nicht; er hat einen eigenen Abschnitt.

::::beispiel Die Kennlinie in Zahlen
Eine kleine Siliziumdiode mit

$$I_S = 10^{-14}\,\text{A}, \qquad U_T = 25{,}9\,\text{mV}.$$

**Durchlassrichtung.** Die Shockley-Gleichung für einige Spannungen; die Eins spielt ab $0{,}1\,\text{V}$ keine Rolle mehr:

| $U$ | $I$ |
|---|---|
| $0{,}1\,\text{V}$ | $0{,}47\,\text{pA}$ |
| $0{,}3\,\text{V}$ | $1{,}1\,\text{nA}$ |
| $0{,}4\,\text{V}$ | $52\,\text{nA}$ |
| $0{,}5\,\text{V}$ | $2{,}5\,\mu\text{A}$ |
| $0{,}6\,\text{V}$ | $0{,}12\,\text{mA}$ |
| $0{,}65\,\text{V}$ | $0{,}83\,\text{mA}$ |
| $0{,}7\,\text{V}$ | $5{,}7\,\text{mA}$ |
| $0{,}75\,\text{V}$ | $40\,\text{mA}$ |

Zum Beispiel bei $0{,}7\,\text{V}$:

$$I = 10^{-14}\,\text{A}\cdot\Big(\exp\frac{0{,}7\,\text{V}}{0{,}02585\,\text{V}} - 1\Big) = 10^{-14}\,\text{A}\cdot5{,}75\cdot10^{11} = 5{,}7\,\text{mA}.$$

In einem Diagramm mit linearer Stromachse bis $40\,\text{mA}$ liegt alles unter $0{,}6\,\text{V}$ auf der Nulllinie, und zwischen $0{,}6$ und $0{,}75\,\text{V}$
schießt die Kurve hoch: das Knie.

**Sperrrichtung.** Schon bei $-0{,}1\,\text{V}$ ist der Strom fast $-I_S$:

$$I(-0{,}1\,\text{V}) = 10^{-14}\,\text{A}\cdot(0{,}021 - 1) = -0{,}98\cdot10^{-14}\,\text{A}.$$

Bei $-1\,\text{V}$ wie bei $-50\,\text{V}$ fließen $-10\,\text{fA}$, bis zum Durchbruch.

**Ohne die Eins.** Die Form des Skripts weicht bei $0{,}1\,\text{V}$ um $2\,\%$ ab, bei $0{,}3\,\text{V}$ um weniger als ein Millionstel; im Durchlassbereich
taugt sie also.

**Im Bild:** Vier Zehntelvolt Absenkung, von $0{,}3$ auf $0{,}7\,\text{V}$, vervielfachen den Verkehr hinauf auf das Fünfmillionenfache; das Rinnsal hinunter
bleibt bei $10\,\text{fA}$.
::::

## Knie, Schleusenspannung und Temperatur

Löst man die Shockley-Gleichung nach der Spannung auf, sieht man, warum die Spannung an einer leitenden Diode so wenig vom Strom abhängt:

:::formel
$$U = U_T\,\ln\Big(1 + \frac{I}{I_S}\Big).$$
:::

**So liest man das:** Eingabe ist der Strom, Ausgabe die Spannung. Sie wächst nur logarithmisch: Je Verzehnfachung des Stroms kommen $U_T\ln10$ hinzu, also
$59{,}5\,\text{mV}$. Über fünf Dekaden, von Mikroampere bis $100\,\text{mA}$, ändert sie sich deshalb nur um gut $0{,}3\,\text{V}$. Darum rechnet man eine
leitende Siliziumdiode oft mit einer festen Spannung, der __Schleusenspannung__ $U_S$, auch Durchlass- oder Flussspannung, meist $0{,}6$ bis $0{,}7\,\text{V}$.
Sie ist keine physikalische Grenze, sondern die Spannung bei einem gewählten Bezugsstrom, etwa $1\,\text{mA}$. Das Skript zeichnet in seinen
Gleichrichterbildern $0{,}6\,\text{V}$.

Von Werkstoff zu Werkstoff verschiebt sie sich mit $I_S$, also mit $n_i^2$: Germanium mit seiner kleineren Bandlücke hat eine Schleusenspannung um
$0{,}2$ bis $0{,}3\,\text{V}$. __Schottky-Dioden__, Übergänge zwischen Metall und Halbleiter, kommen auf etwa $0{,}3\,\text{V}$.

**Im Bild:** Um den Verkehr hinauf zu verzehnfachen, muss die Rampe jedes Mal um dasselbe kleine Stück sinken. Für jeden Verkehr, den man praktisch braucht,
steht sie deshalb fast gleich hoch.

:::herleitung
Man bringt $I_S$ auf die andere Seite und logarithmiert:

$$\frac{I}{I_S} + 1 = \exp\frac{U}{U_T}, \qquad U = U_T\,\ln\Big(1 + \frac{I}{I_S}\Big).$$

**Je Dekade.** Für $I$ viel größer als $I_S$ ist die Eins unwichtig, und ein zehnfacher Strom ergibt $U_T\ln(10\,I/I_S)$, also $U_T\ln10$ mehr.

**Werkstoff.** Bei gleichem Strom ist $U$ um $U_T\ln(I_{S2}/I_{S1})$ kleiner, wenn der Sättigungsstrom von $I_{S1}$ auf $I_{S2}$ wächst; ein größeres $n_i$
heißt größeres $I_S$ und kleinere Spannung.
:::

Auch die Temperatur verschiebt die Kennlinie, und zwar entgegen dem ersten Eindruck: Zwar wächst $U_T$ mit $T$, aber $I_S$ wächst mit $n_i^2$ viel schneller.
Bei festem Strom sinkt die Durchlassspannung deshalb, für Silizium um rund $2\,\text{mV}$ je Kelvin:

$$\frac{dU}{dT} \approx \frac{U - W_g/e}{T} - \frac{3\,k_B}{e}.$$

**So liest man das:** Für Silizium bei $1\,\text{mA}$ ist $U$ etwa $0{,}65\,\text{V}$, $W_g/e$ ist $1{,}12\,\text{V}$, und es ergeben sich
$-1{,}8\,\text{mV/K}$. Man nutzt das in Temperaturfühlern; in Schaltungen muss man es berücksichtigen, weil eine warme Diode bei gleicher Spannung mehr
Strom zieht.

**Im Bild:** Stärkeres Rütteln bringt drüben viel mehr Autos aufs Oberdeck, die hinunterrollen; für denselben Netto-Verkehr muss die Rampe weniger weit
gesenkt werden.

:::herleitung
**Der Sättigungsstrom.** Nach dem vorigen Artikel ist $I_S$ proportional zu $n_i^2$, und $n_i^2$ ist proportional zu $T^3\exp(-W_g/(k_BT))$; die übrigen
Größen in $I_S$ hängen nur schwach von der Temperatur ab. Mit einer Konstanten $c$:

$$\ln I_S = c + 3\ln T - \frac{W_g}{k_B\,T}.$$

**Die Spannung bei festem Strom.** In die umgestellte Shockley-Gleichung ohne die Eins eingesetzt, mit $k_BT/e$ für $U_T$:

$$U = \frac{k_B\,T}{e}\,\big(\ln I - c - 3\ln T\big) + \frac{W_g}{e}.$$

**Ableiten.** Die Klammer mal $k_B/e$ ist nach dieser Gleichung $(U - W_g/e)/T$; dazu kommt die Ableitung von $-3\ln T$, mal $k_BT/e$, also $-3k_B/e$. Das
ergibt die Formel. Die kleine Temperaturabhängigkeit der Bandlücke selbst ist dabei vernachlässigt.
:::

::::beispiel Schleusenspannung, Germanium und Temperatur
Die Siliziumdiode von oben, $I_S = 10^{-14}\,\text{A}$ bei $300\,\text{K}$.

**(a) Spannung bei drei Strömen.** Nach der umgestellten Gleichung:

$$U(1\,\mu\text{A}) = 0{,}476\,\text{V}, \qquad U(1\,\text{mA}) = 0{,}655\,\text{V}, \qquad U(100\,\text{mA}) = 0{,}774\,\text{V}.$$

Fünf Dekaden Strom, aber nur $0{,}3\,\text{V}$ Unterschied. Mit dem Bezugsstrom $1\,\text{mA}$ ist die Schleusenspannung dieser Diode $0{,}655\,\text{V}$.

**(b) Germanium.** Eine gleich gebaute Germaniumdiode: $n_i$ ist dort rund $2{,}4\cdot10^{13}\,\text{cm}^{-3}$, $2400$-mal so groß wie in Silizium, also $I_S$
rund $5{,}8\cdot10^{6}$-mal so groß. Bei $1\,\text{mA}$ ist die Spannung um

$$U_T\,\ln(5{,}8\cdot10^{6}) = 0{,}402\,\text{V}$$

kleiner, nur noch $0{,}25\,\text{V}$.

**(c) Fünfzig Grad wärmer.** Bei $1\,\text{mA}$ und $300\,\text{K}$:

$$\frac{dU}{dT} = \frac{0{,}655\,\text{V} - 1{,}12\,\text{V}}{300\,\text{K}} - \frac{3\cdot8{,}617\cdot10^{-5}\,\text{V}}{\text{K}} = -1{,}55\,\frac{\text{mV}}{\text{K}} - 0{,}26\,\frac{\text{mV}}{\text{K}} = -1{,}81\,\frac{\text{mV}}{\text{K}}.$$

Fünfzig Kelvin mehr senken die Spannung also um gut $90\,\text{mV}$, auf $0{,}56\,\text{V}$; die volle Rechnung mit $I_S$ bei $350\,\text{K}$, das
$774$-mal so groß ist, ergibt $0{,}563\,\text{V}$.

**Im Bild:** Ein Parkhaus mit niedrigerer Rampe (Germanium) braucht viel weniger Absenkung für denselben Verkehr; ein stärker gerütteltes ebenso.
::::

:::grafik
Szene: get1/halbleiterbauelemente/02-kennlinie · Vorlage: diodenkennlinie
Die Kennlinie einer Siliziumdiode mit $I_S = 10^{-14}\,\text{A}$ in zwei Darstellungen nebeneinander: links mit linearer Stromachse bis $40\,\text{mA}$, das
Knie zwischen $0{,}6$ und $0{,}75\,\text{V}$, die Schleusenspannung $0{,}655\,\text{V}$ bei $1\,\text{mA}$ markiert; rechts mit logarithmischer Stromachse von
$10^{-15}$ bis $10^{-1}\,\text{A}$, eine Gerade mit einer Dekade je $59{,}5\,\text{mV}$ und in Sperrrichtung die waagrechte Linie bei $I_S$. Ein Umschalter
blendet eine Germaniumdiode ein, deren Kurve um $0{,}4\,\text{V}$ nach links verschoben ist. Ein Regler für die Temperatur von $0$ bis $100\,{}^\circ\text{C}$
verschiebt die Siliziumkurve um $-1{,}8\,\text{mV/K}$; ein Punkt bei $1\,\text{mA}$ zeigt die Spannung als Zahl. Im dritten Quadranten deutet ein steiler Abfall
den Durchbruch an. Kernaussage: Weil die Spannung nur logarithmisch mit dem Strom wächst, erscheint die exponentielle Kennlinie als Knie bei einer fast festen
Schleusenspannung. (Rot = Kennlinie, blau = Bezugspunkt und Zahlen, orange = Verschiebung durch Werkstoff und Temperatur, grau = Achsen.)
:::

## Der Durchbruch

In Sperrrichtung bleibt der Strom bei $-I_S$, bis er bei einer bestimmten Sperrspannung, der __Durchbruchspannung__ $U_\text{BR}$, steil ansteigt, wie Bild
10.7 des Skripts zeigt. Die Ursache ist das Feld in der Raumladungszone. Die äußere Spannung fällt fast ganz an der Zone ab und addiert sich in Sperrrichtung
zur Diffusionsspannung; deshalb wird die Zone breiter und ihr Feld stärker. Für einen Übergang mit gleicher Dotierung $N$ auf beiden Seiten gilt mit den
Formeln des vorigen Artikels:

$$E_\text{max} = \sqrt{\frac{e\,N\,(U_\text{Diff} - U)}{\varepsilon}}.$$

**So liest man das:** Das größte Feld wächst mit der Wurzel aus der Sperrspannung und mit der Wurzel aus der Dotierung. Zwei Vorgänge setzen ein, sobald es
groß genug ist:

- Beim __Lawinendurchbruch__ gewinnen Ladungsträger im starken Feld zwischen zwei Stößen so viel Energie, dass sie beim nächsten Stoß ein Elektron aus seiner
  Bindung schlagen, die __Stoßionisation__. Jedes neue Paar wird seinerseits beschleunigt und schlägt weitere los, eine Lawine. In mäßig dotiertem
  Silizium setzt das bei grob $30$ bis $40\,\text{MV/m}$ ein, bei Durchbruchspannungen von einigen zehn bis einigen hundert Volt.
- Beim __Zener-Effekt__ ist die Zone eines stark dotierten Übergangs so dünn und das Feld so stark, um $100\,\text{MV/m}$, dass Elektronen aus dem
  Valenzband der p-Seite unmittelbar ins Leitungsband der n-Seite gelangen, ohne die Energie dafür aufzubringen. Die Quantenmechanik nennt das
  __Tunneleffekt__. Er tritt bei Durchbruchspannungen unter etwa $5\,\text{V}$ auf.

Der Durchbruch selbst schadet dem Kristall nicht. Zerstörerisch ist die Wärme: Im Durchbruch liegen Spannung und Strom zugleich an, und ohne äußere
Strombegrenzung steigt die Leistung, bis der Übergang überhitzt. Das Skript sagt, der Durchbruch zerstöre die Diode irreversibel, und schreibt einen Absatz
später bei der Z-Diode selbst, der Effekt sei reversibel, solange die Diode thermisch nicht überlastet wird. Richtig ist das Zweite. Gewöhnliche Dioden sind
nur für den Betrieb darunter vorgesehen, Z-Dioden gerade für den Durchbruch.

**Im Bild:** Unter großer Sperrspannung wird die Rampe zu einer steilen, dünnen Wand. Entweder kommen die Autos aus dem Unterdeck der einen Seite direkt durch
die Wand aufs Oberdeck der anderen (Zener), oder Autos, die die steile Rampe hinabrollen, werden so schnell, dass sie andere aus ihren Plätzen stoßen, die
ebenfalls losrollen (Lawine).

:::herleitung
**Spannung an der Zone.** Liegt außen die Spannung $U$, liegt an der Zone statt $U_\text{Diff}$ die Spannung $U_\text{Diff} - U$, in Sperrrichtung also mehr.
In den Formeln des vorigen Artikels für Breite und Feld steht deshalb $U_\text{Diff} - U$:

$$w = \sqrt{\frac{4\,\varepsilon\,(U_\text{Diff} - U)}{e\,N}}, \qquad E_\text{max} = \frac{2\,(U_\text{Diff} - U)}{w}.$$

**Einsetzen.** Die Breite in das Feld eingesetzt, kürzt sich eine Wurzel aus der Spannung heraus:

$$E_\text{max} = \frac{2\,(U_\text{Diff} - U)}{2\,\sqrt{\varepsilon\,(U_\text{Diff} - U)/(e\,N)}} = \sqrt{\frac{e\,N\,(U_\text{Diff} - U)}{\varepsilon}}.$$

Im Bild: Mehr Sperrspannung macht die leere Zone breiter, aber die Rampe wächst schneller als die Zone, und so wird sie steiler.
:::

::::beispiel Wie stark das Feld wird
Silizium mit gleicher Dotierung auf beiden Seiten und der Permittivität

$$\varepsilon = 11{,}7\,\varepsilon_0 = 1{,}036\cdot10^{-10}\,\frac{\text{F}}{\text{m}}.$$

**(a) Mäßig dotiert, $10^{16}\,\text{cm}^{-3}$.** Mit der Diffusionsspannung $0{,}714\,\text{V}$ aus dem vorigen Artikel:

| Spannung $U$ | $0\,\text{V}$ | $-10\,\text{V}$ | $-50\,\text{V}$ | $-100\,\text{V}$ |
|---|---|---|---|---|
| $E_\text{max}$ | $3{,}3\,\text{MV/m}$ | $12{,}9\,\text{MV/m}$ | $28\,\text{MV/m}$ | $39{,}5\,\text{MV/m}$ |

Zum Beispiel bei $-100\,\text{V}$:

$$E_\text{max} = \sqrt{\frac{1{,}602\cdot10^{-19}\,\text{C}\cdot10^{22}\,\text{m}^{-3}\cdot100{,}7\,\text{V}}{1{,}036\cdot10^{-10}\,\text{F/m}}} = 3{,}9\cdot10^{7}\,\frac{\text{V}}{\text{m}}.$$

Erst um $100\,\text{V}$ erreicht das Feld die Größenordnung des Lawinendurchbruchs; eine solche Diode sperrt bis etwa dorthin.

**(b) Stark dotiert, $10^{18}\,\text{cm}^{-3}$.** Hier ist $U_\text{Diff} = 0{,}95\,\text{V}$, und schon ohne äußere Spannung herrschen $38\,\text{MV/m}$; bei
$-5\,\text{V}$ sind es $96\,\text{MV/m}$. Das Feld für den Tunneleffekt, rund $100\,\text{MV/m}$, ist bei

$$U_\text{Diff} - U = \frac{E_\text{max}^2\,\varepsilon}{e\,N} = \frac{(10^{8}\,\text{V/m})^2\cdot1{,}036\cdot10^{-10}\,\text{F/m}}{1{,}602\cdot10^{-19}\,\text{C}\cdot10^{24}\,\text{m}^{-3}} = 6{,}5\,\text{V}$$

erreicht, also bei rund $5{,}5\,\text{V}$ Sperrspannung. So entstehen Z-Dioden für wenige Volt.

Die Feldstärken für den Durchbruch sind Richtwerte aus Messungen; die Rechnung zeigt, warum die Dotierung über die Durchbruchspannung entscheidet.

**Im Bild:** Dieselbe Rampenhöhe auf einer viel kürzeren Strecke ergibt eine viel steilere Wand; bei starker Dotierung ist die leere Zone schmal.
::::

## Die Z-Diode

Die __Z-Diode__, oft Zener-Diode genannt, ist eine Siliziumdiode, die für den Betrieb im Durchbruch gebaut ist, mit einer genau festgelegten
__Zenerspannung__ $U_Z$, von etwa $2{,}4$ bis über $100\,\text{V}$. Unter etwa $5\,\text{V}$ beruht der Durchbruch auf dem Zener-Effekt, darüber auf der
Lawine; beide Bauarten heißen Z-Diode. In Durchlassrichtung verhält sie sich wie eine gewöhnliche Diode. Das Skript sagt, sie werde im Sperrzustand betrieben;
genauer ist es der Durchbruch in Sperrrichtung. Ihr Symbol in Bild 10.8 hat einen Querstrich mit abgewinkelten Enden.

Im Durchbruch ändert sich ihre Spannung kaum mit dem Strom. Die Steigung des steilen Astes beschreibt der __differentielle Widerstand__, der Quotient aus
einer kleinen Spannungsänderung und der zugehörigen Stromänderung, im Bild 10.8 des Skripts $\Delta U$ und $\Delta I$:

$$r_Z = \frac{\Delta U}{\Delta I}.$$

Er beträgt bei kleinen Z-Dioden einige Ohm bis einige zehn Ohm. Damit stabilisiert man Spannungen: Eine schwankende Eingangsspannung $U_E$ speist über einen
__Vorwiderstand__ $R_V$ die Z-Diode, mit der Kathode am Ausgang und der Anode an Masse, und die Ausgangsspannung $U_A$ liegt an der Z-Diode. Schwankt $U_E$,
schwankt $U_A$ nur um einen kleinen Bruchteil:

:::formel
$$\Delta U_A = \frac{r_Z}{R_V + r_Z}\,\Delta U_E.$$
:::

**So liest man das:** Für Änderungen bilden $R_V$ und $r_Z$ einen Spannungsteiler, wie im Artikel über die Zusammenschaltung von Widerständen. Weil $r_Z$ klein
gegen $R_V$ ist, kommt nur ein kleiner Bruchteil der Schwankung am Ausgang an. Den Strom begrenzt $R_V$, nicht die Diode: Das Skript spricht von einem
Stromfluss in fast beliebiger Höhe, aber er muss durch den Vorwiderstand begrenzt werden, damit die Leistung an der Z-Diode zulässig bleibt. Wie man die
Stabilisierung mit einem Transistor verbessert, behandeln die Kapitel über Transistoren.

**Im Bild:** Ab einer bestimmten Steilheit lässt die Wand Autos durch, und zwar so viele, wie nötig sind, damit sie nicht höher wird. Mehr Zufluss erhöht den
Durchlass, nicht die Höhe.

:::herleitung
**Das Modell des steilen Astes.** Im Durchbruch nähert man die Kennlinie durch eine Gerade: Mit dem Strom $I_Z$ in Sperrrichtung, von der Kathode zur Anode
gezählt, und der Spannung $U_{Z0}$, bei der die Gerade die Spannungsachse schneidet, ist die Spannung an der Diode

$$U_A = U_{Z0} + r_Z\,I_Z.$$

**Ohne Last.** Der ganze Strom durch $R_V$ fließt durch die Diode; nach der Maschenregel liegen $R_V$ und die Gerade in Reihe an $U_E$:

$$I_Z = \frac{U_E - U_{Z0}}{R_V + r_Z}, \qquad U_A = U_{Z0} + \frac{r_Z}{R_V + r_Z}\,\big(U_E - U_{Z0}\big).$$

**Die Änderung.** $U_{Z0}$ ist fest, also ändert sich $U_A$ um den Faktor vor der Klammer mal der Änderung von $U_E$. Im Bild: Wie viel mehr Zufluss auch kommt,
die Wand gibt fast alles davon durch.
:::

::::beispiel Eine Spannung stabilisieren
Eine Z-Diode mit

$$U_{Z0} = 5{,}1\,\text{V}, \qquad r_Z = 10\,\Omega, \qquad R_V = 330\,\Omega,$$

an einer Eingangsspannung, die zwischen $9$ und $12\,\text{V}$ schwankt.

**Ohne Last.** Strom und Ausgangsspannung an beiden Enden:

$$I_Z(9\,\text{V}) = \frac{3{,}9\,\text{V}}{340\,\Omega} = 11{,}5\,\text{mA}, \qquad U_A = 5{,}1\,\text{V} + 10\,\Omega\cdot11{,}5\,\text{mA} = 5{,}215\,\text{V},$$

$$I_Z(12\,\text{V}) = \frac{6{,}9\,\text{V}}{340\,\Omega} = 20{,}3\,\text{mA}, \qquad U_A = 5{,}1\,\text{V} + 10\,\Omega\cdot20{,}3\,\text{mA} = 5{,}303\,\text{V}.$$

Drei Volt Schwankung am Eingang ergeben am Ausgang

$$\Delta U_A = \frac{10\,\Omega}{340\,\Omega}\cdot3\,\text{V} = 88\,\text{mV},$$

ein Vierunddreißigstel.

**Die Leistung.** Bei $12\,\text{V}$ setzen Z-Diode und Vorwiderstand um:

$$P_Z = 5{,}3\,\text{V}\cdot20{,}3\,\text{mA} = 108\,\text{mW}, \qquad P_{R_V} = \frac{(12\,\text{V} - 5{,}3\,\text{V})^2}{330\,\Omega} = 136\,\text{mW}.$$

Beide Bauteile müssen das aushalten.

**Mit Last.** Ein Verbraucher mit $1\,\text{k}\Omega$ am Ausgang, bei $9\,\text{V}$: Nach der Knotenregel teilt sich der Strom durch $R_V$ auf Diode und Last auf,
und es ergeben sich

$$U_A = 5{,}165\,\text{V}, \qquad I_L = 5{,}16\,\text{mA}, \qquad I_Z = 6{,}46\,\text{mA}.$$

Die Last nimmt der Diode Strom weg; damit die Stabilisierung hält, darf $I_Z$ nicht bis an das Knie absinken.

**Im Bild:** Zu viel Zufluss läuft durch die Wand ab, und der Pegel am Ausgang bleibt fast, wo er ist.
::::

:::grafik
Szene: get1/halbleiterbauelemente/02-durchbruch-z-diode · Vorlage: durchbruch-stabilisierung
Links das Banddiagramm eines stark dotierten Übergangs unter Sperrspannung: Ein Regler von $0$ bis $-8\,\text{V}$ macht die Bandverbiegung höher und die Zone
dabei nur wenig breiter, das Feld als Zahl in MV/m steigt. Ab etwa $100\,\text{MV/m}$ springen Elektronen waagrecht aus dem Valenzband der p-Seite ins
Leitungsband der n-Seite (Zener); ein Umschalter zeigt den schwach dotierten Fall bei $-100\,\text{V}$, in dem ein Elektron auf der Rampe beschleunigt wird und
beim Stoß ein Paar erzeugt, das wieder beschleunigt wird (Lawine). Rechts die Stabilisierungsschaltung: Quelle $U_E$ mit Regler von $9$ bis $12\,\text{V}$,
$R_V = 330\,\Omega$, Z-Diode mit der Kathode oben am Ausgang, Ausgangsspannung $U_A$ als Zahl, die nur von $5{,}215$ auf $5{,}303\,\text{V}$ wandert, daneben der
Kennlinienast mit dem wandernden Arbeitspunkt und dem Steigungsdreieck $\Delta U/\Delta I = 10\,\Omega$. Kernaussage: Im Durchbruch hält die Diode ihre
Spannung fast fest, und mit einem Vorwiderstand wird daraus eine stabile Spannung. (Rot = Z-Diode und Kennlinienast, blau = Elektronen und Spannungen, orange =
Feld und Steigungsdreieck, grau = Bänder und Schaltung.)
:::

## Die Kapazitätsdiode

In Sperrrichtung ist die Raumladungszone eine Schicht ohne freie Träger zwischen zwei leitenden Gebieten, also ein Plattenkondensator. Sein Plattenabstand
ist die Breite der Zone, und weil sie mit der Sperrspannung wächst, nimmt die Kapazität ab, wie das Skript sagt. Diese __Sperrschichtkapazität__ $C_\text{Sp}$
eines Übergangs mit der Fläche $A$ hängt so von der Spannung ab, mit der Breite $w_0$ und der Kapazität $C_0$ ohne äußere Spannung:

:::formel
$$C_\text{Sp}(U) = \frac{\varepsilon\,A}{w(U)} = \frac{C_0}{\sqrt{1 - U/U_\text{Diff}}}, \qquad C_0 = \frac{\varepsilon\,A}{w_0}.$$
:::

**So liest man das:** Eingabe ist die Spannung, in Sperrrichtung negativ, Ausgabe eine Kapazität in Farad. Je größer die Sperrspannung, desto kleiner die
Kapazität, mit der Wurzel. Dioden, die dafür gebaut sind, heißen __Kapazitätsdioden__ oder Varaktoren; mit besonderen Dotierungsverläufen erreichen sie
stärkere Änderungen als die Wurzel. Man stimmt mit ihnen Schwingkreise und Oszillatoren elektrisch ab, ohne bewegliche Teile.

**Im Bild:** Die leere Zone zwischen den Parkhäusern ist der Spalt zwischen zwei Platten. Höhere Sperrspannung räumt sie breiter frei, und ein breiterer Spalt
speichert bei gleicher Spannungsänderung weniger Ladung.

:::herleitung
**Der Kondensator.** Nach dem Artikel über den Kondensator hat ein Plattenkondensator mit der Fläche $A$, dem Abstand $d$ und der Permittivität
$\varepsilon$ die Kapazität $\varepsilon A/d$; hier ist $d$ die Breite $w$ der Zone.

**Die Breite.** Nach dem Abschnitt über den Durchbruch wächst $w$ mit der Wurzel aus $U_\text{Diff} - U$; bezogen auf $U = 0$:

$$w(U) = w_0\,\sqrt{1 - \frac{U}{U_\text{Diff}}}.$$

Eingesetzt ergibt sich die Formel.

**Warum das auch für die Ladung stimmt.** Die Platten sind keine Flächen, sondern die Ladung sitzt in der Zone verteilt. Bei gleich dotierten Seiten ist die
Ladung einer Seite $Q = e\,N\,A\,w/2$, und ändert sich die Spannung, wächst die Zone an ihren Rändern. Mit der Breite von eben ist

$$Q = A\,\sqrt{e\,N\,\varepsilon\,(U_\text{Diff} - U)}, \qquad \Big|\frac{dQ}{dU}\Big| = \frac{A}{2}\,\sqrt{\frac{e\,N\,\varepsilon}{U_\text{Diff} - U}} = \frac{\varepsilon\,A}{w}.$$

Die Kapazität für kleine Spannungsänderungen ist also genau $\varepsilon A/w$. Im Bild: Die zusätzlichen Ladungen kommen an den Rändern der leeren Zone hinzu,
wo sie die Platten bilden.
:::

::::beispiel Eine Kapazitätsdiode
Ein gleich dotierter Siliziumübergang mit

$$A = 1\,\text{mm}^2, \qquad N = 10^{16}\,\text{cm}^{-3}, \qquad U_\text{Diff} = 0{,}714\,\text{V}, \qquad w_0 = 0{,}43\,\mu\text{m}.$$

**Ohne Spannung.**

$$C_0 = \frac{1{,}036\cdot10^{-10}\,\frac{\text{F}}{\text{m}}\cdot10^{-6}\,\text{m}^2}{0{,}43\cdot10^{-6}\,\text{m}} = 241\,\text{pF}.$$

**Mit Sperrspannung.** Der Nenner $\sqrt{1 - U/U_\text{Diff}}$ wächst:

| $U$ | $0\,\text{V}$ | $-1\,\text{V}$ | $-4\,\text{V}$ | $-10\,\text{V}$ | $-25\,\text{V}$ |
|---|---|---|---|---|---|
| $w$ | $0{,}43\,\mu\text{m}$ | $0{,}67\,\mu\text{m}$ | $1{,}10\,\mu\text{m}$ | $1{,}67\,\mu\text{m}$ | $2{,}58\,\mu\text{m}$ |
| $C_\text{Sp}$ | $241\,\text{pF}$ | $156\,\text{pF}$ | $94\,\text{pF}$ | $62\,\text{pF}$ | $40\,\text{pF}$ |

Zwischen $0$ und $-25\,\text{V}$ ändert sich die Kapazität also um den Faktor sechs. Das Bild 10.9 des Skripts zeigt denselben Verlauf schematisch, von
$200$ auf $100\,\text{pF}$.

**Im Bild:** Fünfundzwanzig Volt Sperrspannung räumen die leere Zone sechsmal so breit frei; der Spalt ist sechsmal so groß, die Kapazität ein Sechstel.
::::

## Fotodiode und Solarzelle

Licht, dessen Photonen mindestens die Bandlücke mitbringen, bei Silizium also Licht unter $1107\,\text{nm}$ Wellenlänge, erzeugt im Kristall Elektron-Loch-Paare,
wie im vorigen Artikel. Entstehen sie in der Raumladungszone oder so nahe daran, dass sie hineingelangen, trennt sie das Feld: Die Elektronen laufen zur
n-Seite, die Löcher zur p-Seite. Das ist ein Strom von der Kathode zur Anode durch die Diode, also in Sperrrichtung, der __Fotostrom__ $I_\text{Ph}$. Jedes
getrennte Paar trägt eine Elementarladung über den Übergang; der Fotostrom ist deshalb proportional zur Zahl der Photonen je Sekunde und damit zur
Bestrahlungsstärke. Das Skript nennt den Vorgang Photoeffekt im Inneren der Diode, __innerer Fotoeffekt__.

:::formel
$$I = I_S\,\Big(\exp\frac{U}{U_T} - 1\Big) - I_\text{Ph}.$$
:::

**So liest man das:** Die beleuchtete Diode ist eine gewöhnliche Diode mit einer Stromquelle parallel, die $I_\text{Ph}$ von der Kathode zur Anode treibt; das
ist das Ersatzschaltbild in Bild 10.10 des Skripts. Ihre Kennlinie ist die Diodenkennlinie, um $I_\text{Ph}$ nach unten verschoben, umso weiter, je heller es
ist. Zwei Betriebsarten:

- Als __Fotodiode__ in Sperrrichtung fließt fast genau $-(I_S + I_\text{Ph})$: Der Sperrstrom steigt mit der Beleuchtung, wie das Skript sagt, und hängt
  nicht von der Spannung ab. Das macht sie zum Lichtsensor.
- Als __Solarzelle__ arbeitet sie im vierten Quadranten, mit positivem $U$ und negativem $I$. Im Verbraucherzählpfeilsystem heißt das: Die Diode nimmt die
  Leistung $UI$ auf, und die ist negativ; sie gibt also die Leistung $-UI$ an einen äußeren Verbraucher ab.

**Im Bild:** Licht hebt in der leeren Zone Autos aufs Oberdeck, und sie rollen die Rampe hinunter zur n-Seite, während die Lücken zur p-Seite wandern. Das ist
Verkehr bergab, der keine Spannung braucht; ein äußerer Kreis kann ihn nutzen.

:::herleitung
**Die beiden Anteile.** Ohne Licht fließt der Strom der Shockley-Gleichung. Die durch Licht erzeugten Träger laufen denselben Weg wie die Minoritätsträger des
Rückstroms, von der Kathode zur Anode, und zählen deshalb negativ. Dass sich beide Anteile einfach addieren, zeigt die genaue Theorie der idealen Diode,
deren Gleichungen für die Minoritätsträger linear sind; das Ergebnis ist das Ersatzschaltbild aus Diode und Stromquelle.

**Die Proportionalität.** Wird von je $\eta$ Photonen eines zu einem getrennten Paar, und treffen $\Phi$ Photonen je Sekunde ein, fließt die Ladung $e$ je Paar:

$$I_\text{Ph} = \eta\,e\,\Phi.$$

Im Bild: Jedes Auto, das das Licht in der Zone hebt, rollt einmal die Rampe hinunter.
:::

Aus der Gleichung folgen die beiden Kennwerte einer Solarzelle, die __Leerlaufspannung__ $U_L$ ohne Verbraucher und der __Kurzschlussstrom__ $I_K$ bei
kurzgeschlossenen Anschlüssen, der aus der Anode herausfließt:

$$U_L = U_T\,\ln\Big(1 + \frac{I_\text{Ph}}{I_S}\Big), \qquad I_K = I_\text{Ph}.$$

**So liest man das:** Die Leerlaufspannung wächst nur logarithmisch mit dem Licht, der Kurzschlussstrom proportional. Über $I_S$, also über $n_i^2$, hängt die
Spannung vom Werkstoff ab. Das ist genau das Ergebnis des Versuchs in Bild 10.12 des Skripts: Die abgreifbare Spannung hängt vom Halbleitermaterial ab, bei
Silizium etwa $0{,}5$ bis $0{,}6\,\text{V}$, und nur schwach von der Einstrahlung, während der Strom mit der Bestrahlung proportional ansteigt. Zwischen Leerlauf
und Kurzschluss liegt der __Punkt maximaler Leistung__, auf den Wechselrichter von Solaranlagen regeln. Wie rechteckig die Kennlinie dort ist, misst der
__Füllfaktor__, die größte Leistung geteilt durch das Produkt aus Leerlaufspannung und Kurzschlussstrom.

**Im Bild:** Ohne Verbraucher stauen sich die heruntergerollten Autos auf der n-Seite, bis sie die Rampe so weit absenken, dass ebenso viele wieder hinauffahren.
Dafür genügt wenig, weil jede kleine Absenkung den Verkehr hinauf vervielfacht.

:::herleitung
**Leerlauf.** Ohne Verbraucher ist $I$ null; der Durchlassstrom der Diode muss den Fotostrom genau ausgleichen:

$$0 = I_S\,\Big(\exp\frac{U_L}{U_T} - 1\Big) - I_\text{Ph}, \qquad U_L = U_T\,\ln\Big(1 + \frac{I_\text{Ph}}{I_S}\Big).$$

**Kurzschluss.** Mit $U$ gleich null verschwindet der Diodenanteil, und $I$ ist $-I_\text{Ph}$; außen fließt der Fotostrom aus der Anode heraus. Im Bild: Ohne
Stau rollt jedes gehobene Auto hinunter und fährt außen herum zurück.
:::

::::beispiel Eine Solarzelle
Eine Siliziumzelle von rund $100\,\text{cm}^2$ in voller Sonne:

$$I_S = 10^{-10}\,\text{A}, \qquad I_\text{Ph} = 3\,\text{A}, \qquad U_T = 25{,}9\,\text{mV}.$$

**Leerlauf und Kurzschluss.**

$$U_L = 0{,}02585\,\text{V}\cdot\ln\big(1 + 3\cdot10^{10}\big) = 0{,}624\,\text{V}, \qquad I_K = 3\,\text{A}.$$

**Der Punkt maximaler Leistung.** Die abgegebene Leistung $-UI$ ist für jede Spannung ausrechenbar; ihr Größtwert liegt bei

$$U = 0{,}544\,\text{V}, \qquad -I = 2{,}86\,\text{A}, \qquad P_\text{max} = 1{,}56\,\text{W}.$$

Der Füllfaktor ist

$$\frac{1{,}56\,\text{W}}{0{,}624\,\text{V}\cdot3\,\text{A}} = 0{,}83.$$

**Halbe Bestrahlung.** Mit $I_\text{Ph} = 1{,}5\,\text{A}$:

$$U_L = 0{,}606\,\text{V}, \qquad I_K = 1{,}5\,\text{A}, \qquad P_\text{max} = 0{,}75\,\text{W}.$$

Die Spannung sinkt nur um $18\,\text{mV}$, nämlich um $U_T\ln2$, Strom und Leistung halbieren sich. Für $12\,\text{V}$ schaltet man deshalb Zellen in Reihe, für
mehr Strom macht man sie größer.

**Im Bild:** Halb so viel Licht hebt halb so viele Autos; für den Rückstau genügt fast dieselbe Absenkung der Rampe.
::::

**Umgekehrt: die Leuchtdiode.** In Durchlassrichtung gelangen Elektronen und Löcher auf die jeweils andere Seite und rekombinieren dort. Die frei werdende
Energie, rund $W_g$ je Paar, geht in Silizium fast ganz als Wärme ins Gitter. In Halbleitern wie Galliumarsenid oder Galliumnitrid wird sie überwiegend als
Photon abgegeben: Das ist die __Leuchtdiode__, kurz LED. Ihre Farbe folgt aus der Bandlücke, wie die Tabelle der Grenzwellenlängen im vorigen Artikel zeigt:
Galliumarsenid leuchtet im Infraroten, Galliumnitrid mit Indium blau. Fotodiode und Solarzelle machen aus Licht Strom, die Leuchtdiode aus Strom Licht. Im
Bild: Ein Auto, das in eine Lücke fällt, gibt die Höhe der Rampe frei, als Wärme oder als Lichtblitz.

:::grafik
Szene: get1/halbleiterbauelemente/02-fotodiode-solarzelle · Vorlage: fotodiode-kennlinienfeld
Links der Querschnitt einer Solarzelle wie in Bild 10.11: oben eine dünne n-Schicht mit Metallfingern, darunter die p-Schicht mit metallischer Rückseite;
Photonen fallen ein und erzeugen nahe der Grenzschicht Paare, die Elektronen wandern nach oben zum Minuspol, die Löcher nach unten zum Pluspol, und durch
einen angeschlossenen Widerstand fließt der Strom. In der Mitte das Ersatzschaltbild: eine Stromquelle $I_\text{Ph}$ mit dem Pfeil von der Kathode zur Anode
parallel zur Diode. Rechts das Kennlinienfeld für vier Beleuchtungen mit $I_\text{Ph} = 0$, $0{,}75$, $1{,}5$, $2{,}25$ und $3\,\text{A}$: die dunkle Kennlinie
durch den Ursprung, die beleuchteten um $I_\text{Ph}$ nach unten verschoben; der vierte Quadrant ist hervorgehoben, auf jeder Kurve $U_L$ und $I_K$ markiert,
und am Punkt maximaler Leistung ein Rechteck aus $U$ und $-I$, dessen Fläche die Leistung ist. Ein Regler für die Beleuchtung verschiebt die Kurven, ein
Regler für den Lastwiderstand den Arbeitspunkt längs der Kurve; die Leistung steht als Zahl daneben. Kernaussage: Licht verschiebt die Diodenkennlinie nach
unten; im vierten Quadranten liefert die Diode Leistung, mit fast fester Spannung und lichtproportionalem Strom. (Rot = Kennlinien, blau = Ladungsträger und
Photonen, orange = Leistungsrechteck und Arbeitspunkt, grau = Achsen und Aufbau.)
:::

## Bedeutung und Ausblick

Die Shockley-Gleichung ist das Modell der Diode: ein Ventil mit exponentieller Durchlasskennlinie, einem winzigen Sperrstrom und einem Durchbruch, den die
Z-Diode gezielt nutzt. Licht verschiebt die Kennlinie und macht die Diode zum Sensor oder zur Stromquelle, Sperrspannung verändert ihre Kapazität, und
Rekombination kann Licht erzeugen.

Weil die Kennlinie gekrümmt ist, lassen sich Schaltungen mit Dioden nicht unmittelbar mit den linearen Verfahren der Kapitel 7 bis 9 lösen. Der nächste
Artikel zeigt, wie man trotzdem den __Arbeitspunkt__ findet, grafisch mit der Arbeitsgeraden und rechnerisch mit linearen Ersatzschaltungen; die Gerade für
den Durchbruchsast der Z-Diode war schon eine solche Ersatzschaltung. Danach folgen Gleichrichter und schließlich der Transistor, zwei pn-Übergänge
hintereinander.

:::kern
- Die Diode hat die Anode am p- und die Kathode am n-Gebiet; $U$ und $I$ zählen von der Anode zur Kathode.
- Shockley-Gleichung: $I=I_S(e^{U/U_T}-1)$, mit $U_T=k_BT/e$, bei $300\,\text{K}$ gleich $25{,}9\,\text{mV}$.
- Die Spannung wächst nur logarithmisch mit dem Strom, um $59{,}5\,\text{mV}$ je Dekade; daher die fast feste Schleusenspannung von $0{,}6$ bis $0{,}7\,\text{V}$.
- Bei festem Strom sinkt die Durchlassspannung um rund $2\,\text{mV}$ je Kelvin.
- Im Durchbruch steigt der Sperrstrom steil an, durch Lawine oder Zener-Effekt; zerstörerisch ist nur die Wärme.
- Die Z-Diode hält im Durchbruch ihre Spannung; mit Vorwiderstand gilt $\Delta U_A=\frac{r_Z}{R_V+r_Z}\Delta U_E$.
- Die Sperrschicht ist ein Kondensator, dessen Kapazität mit der Sperrspannung sinkt: die Kapazitätsdiode.
- Licht erzeugt einen Fotostrom in Sperrrichtung: $I=I_S(e^{U/U_T}-1)-I_\text{Ph}$.
- Solarzelle: Leerlaufspannung logarithmisch im Licht, Kurzschlussstrom proportional.
- Die Leuchtdiode gibt die Rekombinationsenergie, etwa $W_g$, als Licht ab.
:::

:::quiz
F: Wie hängen Anode, Kathode und die Zählpfeile zusammen?
A: Die Anode ist der Anschluss am p-Gebiet, die Kathode der am n-Gebiet; das Dreieck des Symbols zeigt von der Anode zur Kathode, in die Richtung des leichten Stroms. Im Verbraucherzählpfeilsystem zählen $U$ und $I$ von der Anode zur Kathode; positives $U$ ist Durchlass-, negatives Sperrrichtung.
F: Woher kommt die Shockley-Gleichung, und was bedeuten ihre beiden Glieder?
A: $I_Se^{U/U_T}$ ist der Hinstrom der Majoritätsträger über die Rampe, die die Spannung absenkt, $-I_S$ der feste Rückstrom der Minoritätsträger. Ohne Spannung heben sie sich auf, in Sperrrichtung bleibt $-I_S$, in Durchlassrichtung wächst der Strom exponentiell.
F: Was ist an der Gleichung des Skripts zu korrigieren?
A: $k_BT$ ist eine Energie; die Temperaturspannung ist $U_T=k_BT/e$, bei $300\,\text{K}$ gleich $25{,}9\,\text{mV}$. Außerdem fehlt die $-1$: Die Form $I_Se^{eU/(k_BT)}$ gilt nur im Durchlassbereich, gäbe bei $U=0$ den Strom $I_S$ und weicht bei $0{,}1\,\text{V}$ um $2\,\%$ ab.
F: Warum wirkt die exponentielle Kennlinie wie eine Schwelle bei $0{,}6$ bis $0{,}7\,\text{V}$?
A: Die Spannung wächst nur logarithmisch mit dem Strom, um $59{,}5\,\text{mV}$ je Dekade. Mit $I_S=10^{-14}\,\text{A}$ fließen bei $0{,}5\,\text{V}$ erst $2{,}5\,\mu\text{A}$, bei $0{,}7\,\text{V}$ schon $5{,}7\,\text{mA}$; in linearer Darstellung liegt alles darunter auf der Nulllinie.
F: Warum hat Germanium eine kleinere Schleusenspannung, und warum sinkt die Durchlassspannung mit der Temperatur?
A: $I_S$ wächst mit $n_i^2$; bei Germanium ist es rund $5{,}8\cdot10^6$-mal so groß, was die Spannung bei $1\,\text{mA}$ um $0{,}4\,\text{V}$ auf $0{,}25\,\text{V}$ senkt. Mit der Temperatur wächst $I_S$ viel schneller als $U_T$, und bei festem Strom sinkt die Spannung um etwa $1{,}8\,\text{mV/K}$.
F: Was geschieht beim Durchbruch, und zerstört er die Diode?
A: Das Feld der Zone wächst mit der Wurzel aus Sperrspannung und Dotierung. Ab grob $30$ bis $40\,\text{MV/m}$ setzt Stoßionisation ein, die Lawine, bei stark dotierten Übergängen um $100\,\text{MV/m}$ der Tunneleffekt, der Zener-Effekt unter etwa $5\,\text{V}$. Zerstörerisch ist nur die Wärme bei unbegrenztem Strom; das Skript nennt den Durchbruch fälschlich stets irreversibel.
F: Wie stabilisiert eine Z-Diode eine Spannung?
A: Im Durchbruch ändert sich ihre Spannung kaum, ihr differentieller Widerstand $r_Z$ ist klein. Mit einem Vorwiderstand $R_V$ bilden beide für Änderungen einen Spannungsteiler, $\Delta U_A=\frac{r_Z}{R_V+r_Z}\Delta U_E$; mit $10\,\Omega$ und $330\,\Omega$ wird aus $3\,\text{V}$ Schwankung eine von $88\,\text{mV}$.
F: Warum sinkt die Kapazität einer Kapazitätsdiode mit der Sperrspannung?
A: Die Sperrschicht ist ein Kondensator mit der Zonenbreite als Plattenabstand, und die Breite wächst mit der Wurzel aus $U_\text{Diff}-U$. Also ist $C_\text{Sp}=C_0/\sqrt{1-U/U_\text{Diff}}$; im Beispiel sinkt sie von $241\,\text{pF}$ ohne Spannung auf $40\,\text{pF}$ bei $-25\,\text{V}$.
F: Wie entsteht der Fotostrom, und was unterscheidet Fotodiode und Solarzelle?
A: Photonen mit mindestens $W_g$ erzeugen Paare, die das Feld der Zone trennt; das ist ein Strom von der Kathode zur Anode, proportional zur Bestrahlung, mit $I=I_S(e^{U/U_T}-1)-I_\text{Ph}$. In Sperrrichtung ist die Diode ein Lichtsensor; im vierten Quadranten gibt sie Leistung ab und ist eine Solarzelle.
F: Warum hängt die Spannung einer Solarzelle kaum vom Licht ab, ihr Strom aber stark?
A: Die Leerlaufspannung ist $U_T\ln(1+I_\text{Ph}/I_S)$ und wächst nur logarithmisch: bei halber Bestrahlung im Beispiel von $0{,}624$ auf $0{,}606\,\text{V}$. Der Kurzschlussstrom ist $I_\text{Ph}$ selbst und halbiert sich mit. Das ist das Versuchsergebnis des Skripts; am besten Punkt liefert die Zelle $0{,}544\,\text{V}$ und $2{,}86\,\text{A}$, also $1{,}56\,\text{W}$.
:::
