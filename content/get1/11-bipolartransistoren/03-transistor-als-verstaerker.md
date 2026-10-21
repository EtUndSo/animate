---
title: Der Transistor als Verstärker
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110500
summary: Von Grund auf – wie ein Transistor ein kleines Signal vergrößert. Leitbild ist das Regelventil aus dem vorigen Artikel, das ein Zittern seines Steuerdrucks als großen Ausschlag am Manometer weitergibt. Mit idealen und realen Kennlinien samt Early-Effekt, dem erweiterten Ersatzschaltbild, Groß- und Kleinsignal, Steilheit und Verzerrung, dem Kleinsignal-Ersatzschaltbild, der Spannungsverstärkung der Emitterschaltung mit und ohne Emitterwiderstand, Kollektor- und Basisschaltung für kleine Signale und der Spannungsstabilisierung mit Z-Diode und Transistor. Mit Beispiel-Seite.
tags: Verstärker, Kleinsignal, Ersatzschaltbild, Steilheit, Spannungsverstärkung, Emitterschaltung
---

## Anschaulich

Im vorigen Artikel ruhte der Transistor in seinem Arbeitspunkt. Jetzt soll er arbeiten: Ein kleines Signal am Eingang, ein paar Millivolt, soll am Ausgang als
großes, formgleiches Signal erscheinen. Dazu muss man wissen, wie stark der Transistor auf eine kleine Änderung reagiert, warum das nur für kleine Änderungen
gleichmäßig geht und wie die Schaltung um ihn herum die Verstärkung bestimmt.

**Das Leitbild dieses Artikels:** **das Regelventil aus dem vorigen Artikel, das ein Zittern weitergibt.** Das Ventil am Wasserturm steht in seiner Ruhestellung,
das Manometer vor ihm zeigt die Mitte. Nun lässt jemand den Druck in der Steuerleitung ein klein wenig zittern. Weil das Rückschlagventil in der Steuerleitung
wie eine Diode sehr steil anspricht, zittert der Steuerstrom kräftig mit, das Regelventil gibt das $B$-Fache davon als Hauptstrom weiter, und das enge Rohr
macht daraus einen großen Ausschlag des Manometers. Wie im vorigen Artikel ist das eine Analogie; Druck steht für Potenzial, Durchfluss für Strom.

Vier Folgerungen:

- **Kleines Zittern, großer Ausschlag.** Wie groß der Ausschlag wird, hängt davon ab, wie viel Wasser in Ruhe fließt und wie eng das Rohr ist. Das ist die
  Spannungsverstärkung.
- **Nur im Kleinen gleichmäßig.** Das Ventil spricht nicht geradlinig an, sondern exponentiell. Betrachtet man nur ein kleines Stück seiner Kennlinie, wie unter
  einer Lupe, sieht es gerade aus; zittert man zu stark, wird die eine Halbschwingung größer als die andere.
- **Echte Ventile sind nicht ideal.** Ein echter Durchflussregler lässt etwas mehr durch, wenn mehr Druck über ihm liegt, und das Rückschlagventil braucht für
  mehr Durchfluss etwas mehr Druck. Beides misst man und rechnet es ins Modell ein.
- **Dasselbe Ventil als Druckminderer.** Hängt man die Steuerleitung an einen festen Druck und liest hinter dem Ventil ab, hält es den Druck dort fest, auch wenn
  der Turm schwankt. Das ist die Spannungsstabilisierung.

| Im Wasserbild | In der Schaltung |
|---|---|
| Ruhestellung des Ventils | Arbeitspunkt mit $U_{BE}$, $I_C$ und $U_{CE}$ |
| kleines Zittern des Steuerdrucks | Kleinsignal $u_{be}$ |
| Zittern des Hauptstroms | Kleinsignal $i_c$ |
| Ausschlag des Manometers | Ausgangssignal $u_\text{aus}$ |
| wie stark der Hauptstrom auf den Steuerdruck anspricht | Steilheit $g_m$ |
| wie viel zusätzliches Steuerwasser ein Zittern kostet | Eingangswiderstand $r_{BE}$ |
| Hauptstrom wächst leicht mit dem Druck über dem Ventil | Early-Effekt, Ausgangswiderstand $r_{CE}$ |
| Ausschlag geteilt durch Zittern | Spannungsverstärkung $v_u$ |
| Ventil als Druckminderer | Spannungsstabilisierung mit Z-Diode |

:::grafik
Szene: get1/bipolartransistoren/03-zitterndes-ventil · Vorlage: transistor-regelventil
Das Regelventil am Wasserturm aus dem vorigen Artikel in seiner Ruhestellung, das Manometer vor dem Ventil auf der Mitte. Ein Regler lässt den Druck in der
Steuerleitung sinusförmig um wenige Prozent zittern; Steuerstrom, Hauptstrom und Manometerzeiger schwingen mit, der Zeiger mit großem Ausschlag und gegenläufig.
Daneben die Übertragungskennlinie des Hauptstroms über dem Steuerdruck, eine Exponentialkurve, mit einer Lupe um den Arbeitspunkt, in der die Kurve fast gerade
erscheint; unter der Kurve die kleine Eingangsschwingung, rechts die große Ausgangsschwingung. Wird das Zittern größer, verlässt die Schwingung den geraden
Bereich, und die obere Halbschwingung wird sichtbar größer als die untere. Kernaussage: Ein kleines Zittern um die Ruhestellung erscheint am Manometer
vergrößert, gleichmäßig aber nur, solange es klein bleibt. (Blau = Wasser und Signale, rot = Ventil und Kennlinie, orange = Lupe und Ausschlag, grau = Turm und
Achsen.)
:::

## Ideale und reale Kennlinien

Bisher hat das Modell aus Abschnitt 11.3 des Skripts gereicht. Abschnitt 11.5 vergleicht es mit dem echten Transistor, an zwei Stellen. Im idealisierten
__Ausgangskennlinienfeld__ von Bild 11.19 laufen die Kennlinien oberhalb von $0{,}2\,\text{V}$ waagrecht: Der Kollektorstrom hängt nicht von $U_{CE}$ ab, der
Transistor ist dort eine ideale Stromquelle. In der realen Kennlinie steigen sie leicht an, und die rot gepunkteten Hilfslinien des Bildes markieren diesen
Anstieg. Gemessen wird er mit dem __Ausgangsleitwert__, der Steigung der Ausgangskennlinie bei festem Basisstrom, und seinem Kehrwert, dem
__Ausgangswiderstand__ $r_{CE}$:

$$G_{CE} = \frac{\partial I_C}{\partial U_{CE}}, \qquad r_{CE} = \frac{1}{G_{CE}}.$$

**So liest man das:** Beides sind Definitionen. Eingabe ist ein Arbeitspunkt, Ausgabe die Steigung in Siemens bzw. ihr Kehrwert in Ohm. Ideal ist $G_{CE}$ null und
$r_{CE}$ unendlich; real ist $G_{CE}$ klein, aber nicht null. Das meint das Skript mit dem Satz, der Ausgangswiderstand sei endlich und die Verstärkung hänge von
$U_{CE}$ ab.

Am Eingang ist es ebenso. Die idealisierte __Eingangskennlinie__ von Bild 11.20 steigt bei $U_{BE,\text{ein}}$ senkrecht an; jeder Basisstrom fließt dort bei
derselben Spannung. Die reale ist die Exponentialkurve aus dem vorigen Artikel. Ihre Steigung misst der __differentielle Eingangswiderstand__:

$$r_{BE} = \frac{\partial U_{BE}}{\partial I_B}.$$

**So liest man das:** Ideal ist er null, real hat er einen endlichen Wert, der vom Arbeitspunkt abhängt. Das Skript schreibt diese differentiellen Größen groß,
$R_{BE}$ und $G_{CE}$. Hier heißen die differentiellen Widerstände klein, $r_{BE}$ und $r_{CE}$, wie der differentielle Widerstand $r_Z$ der Z-Diode; groß bleiben
die Bauteile $R_{BE}$ und $R_{CE}$ des Ersatzschaltbilds im nächsten Abschnitt.

Warum steigen die Ausgangskennlinien? Nach dem vorigen Artikel verbreitert eine größere Kollektorspannung die Sperrschicht am Basis-Kollektor-Übergang. Sie
wächst dabei auch in die Basis hinein, die Basis wird wirksam dünner, und durch eine dünnere Basis fließt bei derselben Spannung $U_{BE}$ mehr Strom. Das ist der
__Early-Effekt__, benannt nach James Early. Verlängert man die geraden Stücke der Ausgangskennlinien nach links, treffen sie sich näherungsweise in einem Punkt
auf der negativen Spannungsachse, bei $-U_\text{Early}$. Die positive Spannung $U_\text{Early}$ heißt __Early-Spannung__. Damit gilt im aktiven Bereich:

:::formel
$$I_C = I_S\,\exp\frac{U_{BE}}{U_T}\,\Big(1 + \frac{U_{CE}}{U_\text{Early}}\Big).$$
:::

**So liest man das:** Eingaben sind $U_{BE}$ und $U_{CE}$, Ausgabe der Kollektorstrom. Der erste Faktor ist die Transfergleichung des vorigen Artikels, der zweite
eine Gerade in $U_{CE}$, die bei $-U_\text{Early}$ null wird. Bei kleinen Transistoren liegt $U_\text{Early}$ bei einigen zehn bis über hundert Volt; dann ändert
sich der Strom über einige Volt nur um wenige Prozent. Weil der Basisstrom von $U_{CE}$ fast nicht abhängt, wächst mit dem Kollektorstrom auch das Verhältnis
$B$, wie das Skript sagt. Der Ausgangsleitwert ist

$$G_{CE} = \frac{I_C}{U_\text{Early} + U_{CE}}.$$

**Im Bild:** Ein echter Durchflussregler hält seinen Durchfluss nicht ganz fest; je mehr Druck über ihm liegt, desto etwas mehr lässt er durch.

:::herleitung
**Der Strom durch eine dünne Basis.** Nach dem vorigen Artikel diffundieren die Elektronen durch die Basis, die viel dünner ist als ihre Diffusionslänge; fast
keines rekombiniert. Ihre Dichte fällt deshalb geradlinig vom Rand am Emitter bis fast null am Rand des Kollektors, und der Diffusionsstrom ist proportional zum
Gefälle. Bei gegebener Dichte am Emitterrand, die $U_{BE}$ festlegt, ist der Strom also umgekehrt proportional zur Breite $W_B$ der neutralen Basis.

**Die Basis wird dünner.** Eine größere Spannung $U_{CB}$ verbreitert die Sperrschicht, und ein Teil davon liegt in der Basis; $W_B$ nimmt ab. Für kleine
Änderungen nimmt $W_B$ fast geradlinig mit der Spannung ab, und dann wächst der Strom, der zu $1/W_B$ proportional ist, nach der linearen Näherung von $1/(1 - x)$
fast geradlinig mit ihr. Weil $U_{BE}$ im aktiven Bereich fast fest ist, gilt das ebenso für $U_{CE}$.

**Der gemeinsame Punkt.** Eine Gerade, die bei $-U_\text{Early}$ null wird und bei $U_{CE}$ null den Wert der Transfergleichung hat, ist die Formel. Ihre Steigung
ist der Strom bei null geteilt durch $U_\text{Early}$, also für jede Kennlinie proportional zu ihrem eigenen Strom; deshalb treffen sich alle Kennlinien in
demselben Punkt, und genau das beobachtet man näherungsweise.

**Der Ausgangsleitwert.** Die Ableitung der Formel nach $U_{CE}$ ist der erste Faktor geteilt durch $U_\text{Early}$. Drückt man ihn durch $I_C$ aus, steht im
Nenner $U_\text{Early} + U_{CE}$. Im Bild: Je stärker der Druck über dem Ventil, desto schmaler wird die Engstelle im Inneren, die den Durchfluss begrenzt.
:::

::::beispiel Der Early-Effekt in Zahlen
Der Transistor aus dem vorigen Artikel, mit einer Early-Spannung:

$$I_S = 10^{-14}\,\text{A}, \qquad U_\text{Early} = 100\,\text{V}.$$

Er soll bei $6\,\text{V}$ zwischen Kollektor und Emitter $3\,\text{mA}$ führen. Dafür braucht er nach der Formel

$$U_{BE} = U_T\,\ln\frac{3\,\text{mA}}{1{,}06\cdot10^{-14}\,\text{A}} = 0{,}682\,\text{V}.$$

**Bei fester Spannung $U_{BE}$** ändert sich der Strom mit $U_{CE}$:

| $U_{CE}$ | $2\,\text{V}$ | $6\,\text{V}$ | $10\,\text{V}$ |
|---|---|---|---|
| $I_C$ | $2{,}887\,\text{mA}$ | $3{,}000\,\text{mA}$ | $3{,}113\,\text{mA}$ |
| $B$ | $192{,}5$ | $200$ | $207{,}5$ |

Von $2$ auf $10\,\text{V}$ wächst der Strom um $7{,}8\,\%$, und mit ihm das Verhältnis $B$, wenn der Basisstrom bei $15\,\mu\text{A}$ bleibt.

**Der Ausgangswiderstand** im Arbeitspunkt:

$$r_{CE} = \frac{100\,\text{V} + 6\,\text{V}}{3\,\text{mA}} = 35{,}3\,\text{k}\Omega.$$

**Im Bild:** Acht Volt mehr Druck über dem Ventil lassen knapp acht Prozent mehr Wasser durch.
::::

:::grafik
Szene: get1/bipolartransistoren/03-early-effekt · Vorlage: transistor-kennlinien
Links das idealisierte, rechts das reale Ausgangskennlinienfeld wie in Bild 11.19, für Basisströme von $5$ bis $20\,\mu\text{A}$ bis $U_{CE} = 12\,\text{V}$. Im
realen Feld steigen die Kennlinien leicht an; ein Schalter verlängert ihre geraden Stücke als gestrichelte Linien nach links, bis sie sich bei
$-U_\text{Early} = -100\,\text{V}$ treffen, wobei die Spannungsachse dafür gestaucht wird. An einer Kennlinie zeigt ein Steigungsdreieck $\Delta U_{CE}$ und
$\Delta I_C$ und daraus $G_{CE}$. Darunter die Eingangskennlinie, ideal senkrecht bei $0{,}6\,\text{V}$, real exponentiell, mit der Tangente im Arbeitspunkt.
Kernaussage: Reale Kennlinien steigen am Ausgang leicht an und am Eingang nicht senkrecht; beides misst man durch differentielle Größen. (Rot = Kennlinien, blau =
Arbeitspunkt und Tangente, orange = Steigungsdreieck, grau = Achsen, gestrichelt = Verlängerungen.)
:::

## Das erweiterte Ersatzschaltbild

Mit diesen Beobachtungen gibt das Skript in Bild 11.21 ein erweitertes Ersatzschaltbild für den leitenden Betrieb an, das es Großsignal-Ersatzschaltbild nennt,
weil es die gesamten Ströme und Spannungen beschreibt, nicht nur ihre Änderungen. Zwischen Basis und Emitter liegt eine Spannungsquelle $U_0$, im Skript $U$, in
Reihe mit einem Widerstand $R_{BE}$; zwischen Kollektor und Emitter eine gesteuerte Stromquelle, im Skript $I$, parallel zu einem Widerstand $R_{CE}$. Die
Stromquelle führt das $B_0$-Fache des Basisstroms, wobei $B_0$ die Stromverstärkung ist, die man auf $U_{CE}$ gleich null zurückrechnet:

:::formel Definition
$$U_{BE} = U_0 + R_{BE}\,I_B, \qquad I_C = B_0\,I_B + \frac{U_{CE}}{R_{CE}}.$$
:::

**So liest man das:** Jede der beiden Gleichungen ist eine Gerade, die die reale Kennlinie im Arbeitspunkt berührt, eine Tangente. Gegenüber dem Modell aus
Abschnitt 11.3 wächst jetzt die Basis-Emitter-Spannung mit dem Strom, und der Kollektorstrom wächst mit der Spannung. Damit die Tangenten im Arbeitspunkt
berühren, wählt man die Werte so:

$$R_{BE} = \frac{U_T}{I_B}, \qquad U_0 = U_{BE} - U_T, \qquad R_{CE} = \frac{U_\text{Early}}{B_0\,I_B}.$$

Die Werte gelten nur für diesen einen Arbeitspunkt; für einen anderen berühren andere Geraden. Weit vom Arbeitspunkt entfernt weichen die Geraden von den
gekrümmten Kennlinien ab, wie das Beispiel zeigt.

**Im Bild:** Das Rückschlagventil hat jetzt eine kleine Engstelle in Reihe, sodass mehr Steuerwasser etwas mehr Druck braucht, und neben dem Durchflussregler
liegt ein dünnes Leck, durch das umso mehr fließt, je mehr Druck über dem Ventil steht.

:::herleitung
**Die Tangente am Eingang.** Nach dem vorigen Artikel ist der Basisstrom der $B_0$-te Teil des Kollektorstroms bei $U_{CE}$ null:

$$I_B = \frac{I_S}{B_0}\,\exp\frac{U_{BE}}{U_T}, \qquad \frac{dU_{BE}}{dI_B} = \frac{U_T}{I_B}.$$

Die Ableitung folgt aus dem Logarithmus: $U_{BE}$ ist $U_T$ mal dem Logarithmus des Stroms plus einer Konstante. Die Tangente durch den Arbeitspunkt hat diese
Steigung, also $R_{BE}$, und schneidet die Spannungsachse um $R_{BE}I_B$ tiefer, und das ist genau $U_T$.

**Die Tangente am Ausgang.** Mit dem Basisstrom geschrieben lautet Formel (1), weil $I_S$ mal der Exponentialfunktion gleich $B_0I_B$ ist:

$$I_C = B_0\,I_B\,\Big(1 + \frac{U_{CE}}{U_\text{Early}}\Big) = B_0\,I_B + \frac{B_0\,I_B}{U_\text{Early}}\,U_{CE}.$$

Bei festem Basisstrom ist das schon eine Gerade: der Strom der Quelle plus $U_{CE}$ durch $R_{CE}$. Im Bild: Engstelle und Leck sind so bemessen, dass das Modell
in der Ruhestellung genau so viel Wasser und Druck zeigt wie das echte Ventil.
:::

::::beispiel Das erweiterte Ersatzschaltbild im Arbeitspunkt
Der Arbeitspunkt aus dem Beispiel zum Early-Effekt:

$$I_C = 3\,\text{mA}, \qquad U_{CE} = 6\,\text{V}, \qquad B = 200, \qquad U_{BE} = 0{,}682\,\text{V}.$$

**Eingang.** Der Basisstrom ist $15\,\mu\text{A}$, also

$$R_{BE} = \frac{25{,}85\,\text{mV}}{15\,\mu\text{A}} = 1{,}72\,\text{k}\Omega, \qquad U_0 = 0{,}682\,\text{V} - 0{,}026\,\text{V} = 0{,}656\,\text{V}.$$

**Ausgang.** Zurückgerechnet auf null Volt ist die Stromverstärkung

$$B_0 = \frac{200}{1 + 6/100} = 188{,}7, \qquad R_{CE} = \frac{100\,\text{V}}{188{,}7\cdot15\,\mu\text{A}} = 35{,}3\,\text{k}\Omega.$$

Zur Probe: Die Quelle führt $2{,}830\,\text{mA}$, durch $R_{CE}$ fließen $0{,}170\,\text{mA}$, zusammen $3{,}000\,\text{mA}$.

**Wie weit die Tangente trägt.** Bei halbem Basisstrom gibt die Gerade $0{,}669\,\text{V}$, die Kennlinie $0{,}664\,\text{V}$; bei doppeltem $0{,}708$ gegen
$0{,}700\,\text{V}$. Einige Millivolt Fehler, für Gleichstromrechnungen meist genug. Steigt $U_{CE}$ von $2$ auf $10\,\text{V}$, liefert $R_{CE}$
$0{,}23\,\text{mA}$ mehr.

**Im Bild:** Engstelle und Leck des Modellventils, so eingestellt, dass es in der Ruhestellung genau wie das echte Ventil arbeitet.
::::

## Groß- und Kleinsignal

Ein Verstärker trägt ein Signal auf seinem Arbeitspunkt. Jede Spannung und jeder Strom besteht dann aus einem festen Anteil, dem Wert im Arbeitspunkt, und
einem kleinen, zeitlich veränderlichen Anteil, dem __Kleinsignal__. Die Schreibweise unterscheidet drei Größen: den __Momentanwert__ mit kleinem Buchstaben und
großem Index, den Arbeitspunkt groß, das Kleinsignal klein mit kleinem Index:

$$u_{BE}(t) = U_{BE} + u_{be}(t), \qquad i_C(t) = I_C + i_c(t), \qquad u_{CE}(t) = U_{CE} + u_{ce}(t).$$

**So liest man das:** Das sind Definitionen. Der Momentanwert $u_{BE}(t)$ ist das, was ein Oszilloskop zeigt; $U_{BE}$ ist seine Ruhelage und $u_{be}(t)$ das
Zittern um sie. In linearen Netzen könnte man Arbeitspunkt und Signal nach dem Überlagerungsverfahren getrennt rechnen. Der Transistor ist nicht linear, aber
für kleine Signale beinahe; dann geht es trotzdem, und das ist der __Kleinsignalbetrieb__.

Wie klein „klein“ ist, zeigt die Transfergleichung. Mit dem Signal am Eingang wird der Kollektorstrom

$$\begin{aligned} i_C(t) &= I_S\,\exp\frac{U_{BE} + u_{be}(t)}{U_T} = I_C\,\exp\frac{u_{be}(t)}{U_T} \\ &= I_C\,\Big(1 + \frac{u_{be}}{U_T} + \frac{1}{2}\,\frac{u_{be}^2}{U_T^2} + \ldots\Big). \end{aligned}$$

Bricht man nach dem linearen Glied ab, ist das Kleinsignal des Kollektorstroms proportional zu dem der Spannung. Der Faktor heißt __Steilheit__:

:::formel
$$g_m = \frac{\partial I_C}{\partial U_{BE}} = \frac{I_C}{U_T}, \qquad i_c = g_m\,u_{be}.$$
:::

**So liest man das:** Eingabe ist der Kollektorstrom im Arbeitspunkt, Ausgabe die Steilheit in Siemens, Ampere je Volt. Sie sagt, wie viel Kollektorstrom ein
Millivolt mehr an der Basis bringt, und ist die Steigung der Übertragungskennlinie im Arbeitspunkt. Bemerkenswert: $I_S$ fällt heraus. Jeder Bipolartransistor
hat bei $1\,\text{mA}$ dieselbe Steilheit, $38{,}7\,\text{mS}$, gleich welcher Bauart. Das lineare Glied genügt, solange das quadratische klein dagegen ist; ihr
Verhältnis ist $u_{be}/(2U_T)$. Für einen Fehler von einem Prozent darf $u_{be}$ also nur rund ein halbes Millivolt betragen, für zehn Prozent gut fünf
Millivolt. Darüber wird die positive Halbschwingung größer als die negative, das Signal wird __verzerrt__.

**Im Bild:** Unter der Lupe sieht die steile Kennlinie des Ventils gerade aus. Die Steilheit ist ihre Neigung dort, und sie ist umso größer, je mehr Wasser in
Ruhe schon fließt.

:::herleitung
**Der Faktor.** Die Exponentialfunktion einer Summe ist das Produkt der Exponentialfunktionen. Der Faktor mit $U_{BE}$ ergibt mit $I_S$ den Strom im Arbeitspunkt,
$I_C$; es bleibt die Exponentialfunktion des Signals. Das ist noch keine Näherung.

**Die Reihe.** Die Taylorreihe der Exponentialfunktion um null, $1 + x + x^2/2 + \ldots$, mit $x$ gleich $u_{be}/U_T$, ergibt die Klammer.

**Die Steilheit.** Das lineare Glied ist $I_C/U_T$ mal $u_{be}$; zugleich ist es die Ableitung der Transfergleichung nach $U_{BE}$ im Arbeitspunkt, weil die
Exponentialfunktion ihre eigene Ableitung ist.

**Der Fehler.** Das quadratische Glied geteilt durch das lineare ist $x/2$. Mit $U_T$ gleich $25{,}85\,\text{mV}$ ist $x/2$ gleich $0{,}01$ bei $0{,}52\,\text{mV}$
und gleich $0{,}1$ bei $5{,}2\,\text{mV}$. Weil $x$ das Vorzeichen des Signals trägt, wird die positive Halbschwingung um diesen Anteil größer, die negative
kleiner. Im Bild: Wer am Steuerdruck kräftig rüttelt, sieht, dass das Ventil beim Öffnen stärker reagiert als beim Schließen.
:::

::::beispiel Steilheit und Verzerrung bei drei Milliampere
Der Arbeitspunkt der vorigen Beispiele:

$$I_C = 3\,\text{mA}, \qquad g_m = \frac{3\,\text{mA}}{25{,}85\,\text{mV}} = 116\,\text{mS}.$$

**Kleine und größere Signale.** Linear gerechnet und genau, mit der Exponentialfunktion:

| $u_{be}$ | linear | genau | Abweichung |
|---|---|---|---|
| $+1\,\text{mV}$ | $+116\,\mu\text{A}$ | $+118\,\mu\text{A}$ | $+2\,\%$ |
| $+5\,\text{mV}$ | $+580\,\mu\text{A}$ | $+640\,\mu\text{A}$ | $+10\,\%$ |
| $-5\,\text{mV}$ | $-580\,\mu\text{A}$ | $-528\,\mu\text{A}$ | $-9\,\%$ |

Zum Beispiel für die erste Zeile:

$$i_c = 3\,\text{mA}\cdot\Big(\exp\frac{1\,\text{mV}}{25{,}85\,\text{mV}} - 1\Big) = 118\,\mu\text{A}.$$

Bei $\pm5\,\text{mV}$ wird aus einer Sinusschwingung eine, deren obere Hälfte um ein Fünftel größer ist als die untere.

**Im Bild:** Ein Millivolt Zittern am Steuerdruck, und der Hauptstrom zittert um $116\,\mu\text{A}$; fünf Millivolt, und das Ventil gibt beim Öffnen
merklich mehr nach als beim Schließen.
::::

## Das Kleinsignal-Ersatzschaltbild

Für die Kleinsignale braucht man drei Kenngrößen des Arbeitspunkts. Die Steilheit verknüpft $u_{be}$ mit $i_c$. Der __differentielle Eingangswiderstand__
verknüpft $u_{be}$ mit $i_b$, und die __differentielle Stromverstärkung__ $\beta$, die Ableitung von $I_C$ nach $I_B$, ist im Modell konstanter Verstärkung gleich
$B$. Der Ausgangswiderstand verknüpft $u_{ce}$ mit $i_c$:

:::formel
$$r_{BE} = \frac{\beta}{g_m} = \frac{\beta\,U_T}{I_C}, \qquad r_{CE} = \frac{U_\text{Early} + U_{CE}}{I_C} \approx \frac{U_\text{Early}}{I_C}.$$
:::

**So liest man das:** Eingaben sind die Werte im Arbeitspunkt, Ausgaben zwei Widerstände in Ohm. Mit ihnen wird der Transistor für die Kleinsignale zu einem
linearen Zweitor, dem __Kleinsignal-Ersatzschaltbild__: Zwischen Basis und Emitter liegt $r_{BE}$, zwischen Kollektor und Emitter eine gesteuerte Stromquelle
$g_m u_{be}$ parallel zu $r_{CE}$. Weil $g_m u_{be}$ gleich $\beta i_b$ ist, kann man die Quelle auch stromgesteuert schreiben. Nach dem Artikel über Zweitore
ist das die Hybridform mit $H_{11}$ gleich $r_{BE}$, $H_{21}$ gleich $\beta$, $H_{22}$ gleich $1/r_{CE}$ und ohne Rückwirkung. Alle Verfahren der Kapitel 5
bis 9 sind damit wieder anwendbar.

Zwei Beobachtungen tragen durch den Rest des Artikels. Alle drei Kenngrößen hängen vom Arbeitspunktstrom ab; doppelter Strom heißt doppelte Steilheit und halbe
Widerstände. Und das Produkt aus Steilheit und Ausgangswiderstand hängt vom Strom gar nicht ab:

$$g_m\,r_{CE} = \frac{U_\text{Early} + U_{CE}}{U_T}.$$

Es liegt bei einigen tausend und ist, wie der nächste Abschnitt zeigt, die größte Spannungsverstärkung, die ein einzelner Transistor erreichen kann.

**Im Bild:** Drei Zahlen beschreiben das zitternde Ventil: wie stark der Hauptstrom auf den Steuerdruck anspricht, wie viel Steuerwasser ein Zittern kostet und
wie stark das Leck neben dem Regler ist.

:::herleitung
**Eingangswiderstand.** Das Kleinsignal des Basisstroms ist der $\beta$-te Teil dessen des Kollektorstroms, also $g_m u_{be}/\beta$; das Verhältnis von $u_{be}$
zu $i_b$ ist $\beta/g_m$. Das ist auch die Steigung der Eingangskennlinie aus dem vorigen Abschnitt, $U_T/I_B$, denn $I_B$ ist $I_C/\beta$.

**Ausgangswiderstand.** Der Kehrwert des Ausgangsleitwerts aus Formel (1).

**Aus Bild 11.21.** Nach dem Überlagerungsverfahren tragen die festen Anteile der Quellen zu Änderungen nichts bei; man legt sie still. Die Quelle $U_0$ wird zum
Kurzschluss, vom Stromquellenzweig bleibt nur die Änderung $B_0 i_b$. Übrig bleiben $R_{BE}$, die gesteuerte Quelle und $R_{CE}$, mit den Werten des Arbeitspunkts
also dasselbe Ersatzschaltbild. Die kleine Abweichung zwischen $B_0$ und $\beta$ stammt daher, dass auch $R_{CE}$ von $i_b$ abhängt; sie ist von der Ordnung
$U_{CE}/U_\text{Early}$.

**Das Produkt.** $g_m$ ist $I_C/U_T$ und $r_{CE}$ ist $(U_\text{Early} + U_{CE})/I_C$; im Produkt kürzt sich $I_C$. Im Bild: Mehr Wasser macht das Ventil
empfindlicher und das Leck relativ gleich groß; beides hebt sich auf.
:::

::::beispiel Kenngrößen bei drei und einem Milliampere
Der Transistor der vorigen Beispiele, mit $\beta$ gleich $200$, $U_\text{Early}$ gleich $100\,\text{V}$ und $6\,\text{V}$ zwischen Kollektor und Emitter:

| $I_C$ | $g_m$ | $r_{BE}$ | $r_{CE}$ | $g_m r_{CE}$ |
|---|---|---|---|---|
| $3\,\text{mA}$ | $116\,\text{mS}$ | $1{,}72\,\text{k}\Omega$ | $35{,}3\,\text{k}\Omega$ | $4100$ |
| $1\,\text{mA}$ | $38{,}7\,\text{mS}$ | $5{,}17\,\text{k}\Omega$ | $106\,\text{k}\Omega$ | $4100$ |

Zum Beispiel:

$$r_{BE} = \frac{200\cdot25{,}85\,\text{mV}}{3\,\text{mA}} = 1{,}72\,\text{k}\Omega.$$

**Rückwärts gelesen.** Der Transistor im Hybridbeispiel des Artikels über Zweitore hatte

$$H_{11} = 2{,}5\,\text{k}\Omega, \qquad H_{21} = 200, \qquad H_{22} = 20\,\mu\text{S}.$$

Daraus folgen ein Arbeitspunktstrom und eine Spannung, wie sie zu einem echten Transistor passen:

$$I_C = \frac{200\cdot25{,}85\,\text{mV}}{2{,}5\,\text{k}\Omega} = 2{,}07\,\text{mA}, \qquad U_\text{Early} + U_{CE} = \frac{2{,}07\,\text{mA}}{20\,\mu\text{S}} = 103\,\text{V}.$$

**Im Bild:** Bei dreifachem Ruhestrom spricht das Ventil dreimal so stark an, kostet ein Zittern ein Drittel so viel Steuerwasser, und das Leck ist dreimal so
weit.
::::

:::grafik
Szene: get1/bipolartransistoren/03-kleinsignal-esb · Vorlage: transistor-ersatzschaltbilder
Links das erweiterte Ersatzschaltbild von Bild 11.21 mit der Quelle $U_0$ und $R_{BE}$ zwischen B und E und der gesteuerten Quelle $B_0 I_B$ parallel zu
$R_{CE}$ zwischen C und E. Ein Schritt „feste Anteile stilllegen“ blendet $U_0$ zu einem Kurzschluss aus und färbt den Rest um; rechts entsteht das
Kleinsignal-Ersatzschaltbild mit $r_{BE}$, der Quelle $g_m u_{be}$ und $r_{CE}$, beschriftet mit den Werten für $3\,\text{mA}$: $1{,}72\,\text{k}\Omega$,
$116\,\text{mS}$, $35{,}3\,\text{k}\Omega$. Ein Regler für $I_C$ von $0{,}3$ bis $10\,\text{mA}$ verändert alle drei Werte, während das Produkt $g_m r_{CE}$
in einem Zähler bei $4100$ stehen bleibt. Kernaussage: Für kleine Signale bleibt vom Transistor ein lineares Zweitor aus drei Größen, die alle vom Ruhestrom
abhängen. (Rot = Kleinsignalgrößen, blau = Großsignalmodell, orange = Stilllegen, grau = Anschlüsse.)
:::

## Die Spannungsverstärkung der Emitterschaltung

Jetzt lässt sich die Verstärkung ausrechnen. Die Emitterschaltung aus dem vorigen Artikel hat den Emitter an Masse, den Kollektor über $R_C$ an $U_{CC}$; eine
Spannungsquelle gibt das Kleinsignal $u_\text{ein}$ an die Basis, und am Kollektor nimmt man das Kleinsignal $u_\text{aus}$ ab. Die __Spannungsverstärkung__ $v_u$
ist das Verhältnis der beiden. Für Kleinsignale ist $U_{CC}$ stillgelegt, also ein Kurzschluss, und $R_C$ führt vom Kollektor nach Masse, parallel zu $r_{CE}$:

:::formel
$$v_u = \frac{u_\text{aus}}{u_\text{ein}} = -g_m\,\big(R_C \parallel r_{CE}\big) \approx -g_m\,R_C.$$
:::

**So liest man das:** Eingaben sind die Steilheit und die Widerstände am Kollektor, Ausgabe eine reine Zahl. Das Minus heißt wie im vorigen Artikel, dass die
Schaltung umkehrt. Der Betrag lässt sich anders lesen: $g_m R_C$ ist $I_C R_C/U_T$, also die Gleichspannung an $R_C$ geteilt durch $U_T$. Die Verstärkung hängt
damit nur davon ab, wie viel Spannung im Arbeitspunkt an $R_C$ liegt, nicht vom Typ des Transistors. Liegt der Arbeitspunkt in der Mitte, ist das etwa die halbe
Versorgung; an $12\,\text{V}$ ergibt das rund $230$. Ganz ohne äußeren Widerstand, wenn nur $r_{CE}$ bleibt, wäre der Betrag $g_m r_{CE}$, die Grenze aus dem
vorigen Abschnitt.

Hat die Quelle am Eingang einen Innenwiderstand $R_Q$, kommt an der Basis nur der Teil an, den der Spannungsteiler aus $R_Q$ und $r_{BE}$ durchlässt:

$$v_u = -\frac{\beta\,\big(R_C \parallel r_{CE}\big)}{R_Q + r_{BE}}.$$

Im linearen Modell des vorigen Artikels ist $r_{BE}$ null, und mit $R_Q$ gleich $R_B$ ergibt sich die Steigung $-BR_C/R_B$ der Inverterkennlinie wieder.

**Im Bild:** Wie weit der Zeiger des Manometers ausschlägt, hängt nur davon ab, wie viel Druck das enge Rohr in Ruhe schon verbraucht; ein enges Rohr mit viel
Ruhedurchfluss macht aus jedem Zittern einen großen Ausschlag.

:::herleitung
**Die Masche am Eingang.** Die Quelle liegt unmittelbar zwischen Basis und Emitter, also ist $u_{be}$ gleich $u_\text{ein}$.

**Der Knoten am Kollektor.** Die gesteuerte Quelle zieht den Strom $g_m u_{be}$ aus dem Kollektorknoten zum Emitter. Er kann nur durch $R_C$ und $r_{CE}$
nachfließen, die beide vom Kollektor zur Masse führen, weil die Versorgung für Änderungen ein Kurzschluss ist. Dafür muss das Potenzial des Kollektors um diesen
Strom mal der Parallelschaltung sinken:

$$u_\text{aus} = -g_m\,u_{be}\,\big(R_C \parallel r_{CE}\big).$$

Geteilt durch $u_\text{ein}$ ergibt sich Formel (5); für $R_C$ viel kleiner als $r_{CE}$ ist die Parallelschaltung fast $R_C$.

**Mit Innenwiderstand.** $R_Q$ und $r_{BE}$ bilden für das Signal einen Spannungsteiler, also ist $u_{be}$ gleich $u_\text{ein}r_{BE}/(R_Q + r_{BE})$. Mit
$g_m r_{BE}$ gleich $\beta$ folgt die zweite Formel. Im Bild: Ein dünner Zulauf zur Steuerleitung lässt nur einen Teil des Zitterns am Rückschlagventil
ankommen.
:::

::::beispiel Verstärkung im Arbeitspunkt der Mitte
Die Schaltung der Mitte aus dem vorigen Artikel, mit dem Transistor der Beispiele:

$$U_{CC} = 12\,\text{V}, \qquad R_C = 2\,\text{k}\Omega, \qquad I_C = 3\,\text{mA}, \qquad g_m = 116\,\text{mS}, \qquad r_{CE} = 35{,}3\,\text{k}\Omega.$$

**Ohne Innenwiderstand.** An $R_C$ liegen $6\,\text{V}$, und

$$v_u = -116\,\text{mS}\cdot\big(2\,\text{k}\Omega \parallel 35{,}3\,\text{k}\Omega\big) = -116\,\text{mS}\cdot1{,}89\,\text{k}\Omega = -220.$$

Ohne $r_{CE}$ wären es $-232$, die $6\,\text{V}$ geteilt durch $U_T$. Ein Millivolt am Eingang ergibt $220\,\text{mV}$ am Ausgang, umgekehrt.

**Wo die Grenze liegt.** Für höchstens zehn Prozent Verzerrung darf $u_{be}$ rund $5\,\text{mV}$ betragen; am Ausgang sind das $1{,}1\,\text{V}$, weit weniger
als die $6\,\text{V}$ Spielraum bis zur Sättigung. Nicht die Versorgung begrenzt das Signal, sondern die Krümmung der Kennlinie.

**Mit Innenwiderstand.** Mit $r_{BE}$ gleich $1{,}72\,\text{k}\Omega$:

$$R_Q = 1\,\text{k}\Omega: \ v_u = -139, \qquad R_Q = 10\,\text{k}\Omega: \ v_u = -32.$$

**Im Bild:** Ein enges Rohr, das in Ruhe sechs Volt Druck verbraucht, macht aus einem Millivolt Zittern zweihundertzwanzig.
::::

Die hohe Verstärkung hat zwei Mängel: Sie hängt über $g_m$ vom Arbeitspunktstrom und damit von Streuung und Temperatur ab, und schon wenige Millivolt am Eingang
verzerren. Beides behebt dieselbe Stromgegenkopplung wie im vorigen Artikel, wenn der Emitterwiderstand $R_E$ auch für das Signal wirkt:

:::formel
$$v_u = -\frac{\beta\,R_C}{r_{BE} + (\beta + 1)\,R_E} \approx -\frac{R_C}{R_E + 1/g_m}.$$
:::

**So liest man das:** Ist $g_m R_E$ groß gegen eins, bleibt nur $-R_C/R_E$. Die Verstärkung hängt dann nur noch von zwei Widerständen ab, nicht von $\beta$, nicht
vom Strom und kaum von der Temperatur; dafür ist sie viel kleiner. Zugleich liegt nur noch ein kleiner Teil des Eingangssignals an der Basis-Emitter-Strecke,
nämlich $r_{BE}/(r_{BE} + (\beta + 1)R_E)$; den Rest trägt $R_E$. Der Eingang verträgt deshalb ein entsprechend größeres Signal, ehe es verzerrt. Und die Quelle
sieht den großen Eingangswiderstand $r_{BE} + (\beta + 1)R_E$. Die Gegenkopplung tauscht Verstärkung gegen Genauigkeit und Linearität; nach genau diesem Prinzip
arbeiten auch die Schaltungen mit Operationsverstärkern im nächsten Kapitel. Will man für Wechselsignale die volle Verstärkung und trotzdem den stabilen
Arbeitspunkt, überbrückt man $R_E$ mit einem Kondensator; das gehört in die Wechselstromtechnik.

**Im Bild:** Mit dem engen Abflussrohr hinter dem Ventil hebt jedes Zittern des Hauptstroms den Gegendruck mit; fast das ganze Zittern des Steuerdrucks geht im
Abflussrohr auf, und nur ein Rest erreicht das Rückschlagventil.

:::herleitung
**Die Masche am Eingang.** Durch $R_E$ fließt das Kleinsignal des Emitterstroms, $(\beta + 1)i_b$. Die Masche von der Quelle über $r_{BE}$ und $R_E$ nach Masse:

$$u_\text{ein} = r_{BE}\,i_b + (\beta + 1)\,R_E\,i_b, \qquad i_b = \frac{u_\text{ein}}{r_{BE} + (\beta + 1)\,R_E}.$$

**Der Ausgang.** Ohne $r_{CE}$, das neben $R_C$ und $R_E$ kaum zählt, fließt $\beta i_b$ aus dem Kollektorknoten, und $u_\text{aus}$ ist $-R_C\beta i_b$. Geteilt
durch $u_\text{ein}$ ergibt sich der erste Ausdruck.

**Die Näherung.** Man teilt Zähler und Nenner durch $\beta$. Im Nenner steht dann $r_{BE}/\beta$, also $1/g_m$, und $R_E(1 + 1/\beta)$, fast $R_E$.

**Der Anteil an der Basis-Emitter-Strecke.** Er ist $r_{BE}i_b$ geteilt durch $u_\text{ein}$, also $r_{BE}$ geteilt durch den Nenner. Im Bild: Das Abflussrohr
nimmt den Großteil des Zitterns auf, das Rückschlagventil nur den Rest.
:::

::::beispiel Ein Emitterwiderstand auch für das Signal
Die Schaltung mit Basisspannungsteiler aus dem vorigen Artikel, $R_C$ gleich $2\,\text{k}\Omega$ und $R_E$ gleich $1\,\text{k}\Omega$, im Arbeitspunkt
$2{,}1\,\text{mA}$:

$$g_m = 81{,}2\,\text{mS}, \qquad \frac{1}{g_m} = 12{,}3\,\Omega, \qquad r_{BE} = 2{,}46\,\text{k}\Omega.$$

**Die Verstärkung,** genau und genähert:

$$v_u = -\frac{200\cdot2\,\text{k}\Omega}{2{,}46\,\text{k}\Omega + 201\cdot1\,\text{k}\Omega} = -1{,}966, \qquad -\frac{2\,\text{k}\Omega}{1\,\text{k}\Omega + 12{,}3\,\Omega} = -1{,}976.$$

Fast genau $-R_C/R_E$, also $-2$. Mit $\beta$ gleich $100$ wären es $-1{,}956$, mit $400$ $-1{,}971$; ohne $R_E$ für das Signal dagegen $-162$.

**Der Eingang.** Der Transistor bietet $203\,\text{k}\Omega$; parallel dazu liegt für das Signal der Teiler mit $7{,}67\,\text{k}\Omega$, zusammen
$7{,}40\,\text{k}\Omega$.

**Der Aussteuerbereich.** Nur $1{,}2\,\%$ des Eingangssignals liegen an der Basis-Emitter-Strecke. Die fünf Millivolt Grenze dort erreicht man erst bei
$0{,}43\,\text{V}$ am Eingang, am Ausgang sind das $0{,}84\,\text{V}$.

**Im Bild:** Mit dem Abflussrohr gibt das Ventil das Zittern nur doppelt weiter, dafür bei jedem Exemplar gleich und auch bei kräftigem Rütteln sauber.
::::

:::grafik
Szene: get1/bipolartransistoren/03-emitterschaltung-verstaerkung · Vorlage: verstaerker-kennlinie
Oben die Emitterschaltung an $12\,\text{V}$ mit $R_C = 2\,\text{k}\Omega$, einer Signalquelle an der Basis und einem Umschalter für einen Emitterwiderstand von
$1\,\text{k}\Omega$, der auch für das Signal wirkt. Darunter die Übertragungskennlinie $u_{CE}$ über $u_{BE}$ mit dem Arbeitspunkt bei $3\,\text{mA}$ und ihrer
Tangente der Steigung $-220$; eine Sinusschwingung am Eingang mit einstellbarem Scheitelwert von $0{,}5$ bis $20\,\text{mV}$ erscheint am Ausgang groß und
umgekehrt, und ab etwa $5\,\text{mV}$ wird die Verzerrung sichtbar, mit einer Anzeige des Unterschieds der Halbschwingungen. Mit eingeschaltetem $R_E$ ist die
Kennlinie flach und gerade, die Verstärkung zeigt $-2$, und auch große Eingangssignale bleiben unverzerrt. Kernaussage: Ohne Gegenkopplung verstärkt der
Transistor stark, aber nur kleine Signale sauber; mit Gegenkopplung schwach, dafür genau. (Rot = Kennlinie und Tangente, blau = Ein- und Ausgangssignal, orange =
Gegenkopplung, grau = Achsen und Bauteile.)
:::

## Kollektor- und Basisschaltung für kleine Signale

Der vorige Artikel hat die drei Grundschaltungen an ihren Kennlinien unterschieden; das Kleinsignal-Ersatzschaltbild liefert jetzt ihre Zahlen. In der
__Kollektorschaltung__, dem Emitterfolger, liegt die Quelle an der Basis, der Kollektor an der für Signale stillgelegten Versorgung, und der Ausgang ist der
Emitter mit $R_E$ nach Masse. Mit dem __Eingangswiderstand__ $r_\text{ein}$, dem Verhältnis von $u_\text{ein}$ zum Strom, den die Quelle liefert, gilt:

:::formel
$$v_u = \frac{(\beta + 1)\,R_E}{r_{BE} + (\beta + 1)\,R_E}, \qquad r_\text{ein} = r_{BE} + (\beta + 1)\,R_E.$$
:::

**So liest man das:** Die Verstärkung ist knapp unter eins, wie das Skript sagt, und nähert sich eins, je größer $g_m R_E$ ist. Der Eingangswiderstand ist
groß, weil die Quelle nur den Basisstrom liefern muss, während durch $R_E$ der $(\beta + 1)$-fache Strom fließt. Am Ausgang wirkt die Schaltung dagegen wie eine
Quelle mit sehr kleinem Innenwiderstand, dem __Ausgangswiderstand__ $r_\text{aus}$; hat die Signalquelle selbst den Innenwiderstand $R_Q$, ist er

$$r_\text{aus} = R_E \parallel \frac{r_{BE} + R_Q}{\beta + 1} \approx \frac{1}{g_m} + \frac{R_Q}{\beta + 1}.$$

Der Innenwiderstand der Quelle erscheint am Ausgang durch $\beta + 1$ geteilt. Das ist der __Impedanzwandler__ des vorigen Artikels in Zahlen: großer
Eingangs-, kleiner Ausgangswiderstand und fast unveränderte Spannung.

**Im Bild:** Wer hinter dem Ventil abliest, sieht den Steuerdruck minus dem Öffnungsdruck, fast genauso zitternd wie den Steuerdruck selbst; und wer dort
Wasser abzapft, merkt kaum etwas, weil das Ventil sofort nachliefert.

:::herleitung
**Verstärkung und Eingang.** Die Masche von der Quelle über $r_{BE}$ und $R_E$ ist dieselbe wie beim Emitterwiderstand im vorigen Abschnitt; $r_{CE}$ liegt
vom Emitter zum Kollektor und damit für Signale parallel zu $R_E$, es zählt neben $R_E$ kaum. Am Ausgang liegt die Spannung an $R_E$:

$$u_\text{aus} = (\beta + 1)\,R_E\,i_b, \qquad u_\text{ein} = \big(r_{BE} + (\beta + 1)\,R_E\big)\,i_b.$$

Der Quotient ist $v_u$, und $u_\text{ein}/i_b$ ist $r_\text{ein}$, weil die Quelle genau $i_b$ liefert.

**Der Ausgangswiderstand.** Man legt die Signalquelle still, sodass von der Basis nur $R_Q$ nach Masse führt, und legt an den Emitter eine Prüfspannung $u_x$.
Der Basisstrom fließt dann von Masse durch $R_Q$ in die Basis, und die Masche über $R_Q$ und $r_{BE}$ zum Emitter ergibt

$$u_x = -\big(R_Q + r_{BE}\big)\,i_b.$$

Aus dem Emitter fließt der $(\beta + 1)$-fache Basisstrom; die Prüfquelle muss also $(\beta + 1)u_x/(R_Q + r_{BE})$ in den Emitter liefern. Der Transistor wirkt
wie der Widerstand $(r_{BE} + R_Q)/(\beta + 1)$, parallel zu $R_E$. Mit $r_{BE}/(\beta + 1)$ fast gleich $1/g_m$ folgt die Näherung. Im Bild: Zapft man hinter dem
Ventil Wasser ab, sinkt der Druck dort ein wenig, das Rückschlagventil öffnet weiter, und das Ventil liefert nach.
:::

::::beispiel Ein Emitterfolger in Zahlen
Der Emitterfolger aus dem vorigen Artikel, $3\,\text{V}$ am Eingang, $R_E$ gleich $1\,\text{k}\Omega$ und $\beta$ gleich $200$, im Arbeitspunkt
$2{,}39\,\text{mA}$:

$$g_m = 92{,}4\,\text{mS}, \qquad r_{BE} = 2{,}16\,\text{k}\Omega.$$

**Verstärkung und Eingang.**

$$v_u = \frac{201\cdot1\,\text{k}\Omega}{2{,}16\,\text{k}\Omega + 201\,\text{k}\Omega} = 0{,}989, \qquad r_\text{ein} = 203\,\text{k}\Omega.$$

Das ist der Widerstand, den die Gleichstromrechnung des vorigen Artikels schon ergab, jetzt mit $r_{BE}$.

**Ausgang.** An einer idealen Quelle ist $r_\text{aus}$ gleich $10{,}7\,\Omega$, fast $1/g_m$ mit $10{,}8\,\Omega$. An einer Quelle mit
$10\,\text{k}\Omega$ Innenwiderstand:

$$r_\text{aus} = 1\,\text{k}\Omega \parallel \frac{2{,}16\,\text{k}\Omega + 10\,\text{k}\Omega}{201} = 1\,\text{k}\Omega \parallel 60{,}5\,\Omega = 57{,}1\,\Omega.$$

Aus der Quelle mit $10\,\text{k}\Omega$ ist für den Ausgang eine mit $57\,\Omega$ geworden.

**Im Bild:** Das Ventil gibt den Steuerdruck fast eins zu eins weiter und liefert dabei das Zweihundertfache des Steuerwassers.
::::

In der __Basisschaltung__ liegt die Basis für Signale an Masse, die Quelle am Emitter, und der Ausgang ist der Kollektor mit $R_C$:

:::formel
$$v_u = g_m\,R_C, \qquad r_\text{ein} = \frac{r_{BE}}{\beta + 1} \approx \frac{1}{g_m}.$$
:::

**So liest man das:** Die Verstärkung ist so groß wie bei der Emitterschaltung, aber positiv; das ist die steile, steigende Kennlinie aus dem vorigen Artikel.
Der Eingangswiderstand ist dagegen winzig, einige Ohm, denn die Quelle muss den ganzen Emitterstrom liefern. Eine Quelle mit Innenwiderstand verliert deshalb
am Eingang den größten Teil ihrer Spannung. Man braucht die Basisschaltung, wo Quellen ohnehin niederohmig sind und wo es auf hohe Frequenzen ankommt; das
behandeln Schaltungstechnik und Hochfrequenztechnik.

**Im Bild:** Man hält die Steuerleitung fest und rüttelt stattdessen am Abfluss; das Manometer schlägt genauso weit aus, aber am Abfluss muss man das ganze
Wasser bewegen.

:::herleitung
**Die Verstärkung.** Die Basis liegt für Signale an Masse, der Emitter folgt der Quelle; also ist $u_{be}$ gleich $-u_\text{ein}$. Der Kollektorstrom ändert sich
um $g_m u_{be}$, und am Kollektor ist, ohne $r_{CE}$,

$$u_\text{aus} = -R_C\,g_m\,u_{be} = g_m\,R_C\,u_\text{ein}.$$

**Der Eingangswiderstand.** Aus dem Emitter fließt das Kleinsignal $(\beta + 1)i_b$ zur Quelle, und $i_b$ ist $u_{be}/r_{BE}$, also $-u_\text{ein}/r_{BE}$.
Die Quelle liefert also den Strom $(\beta + 1)u_\text{ein}/r_{BE}$ in den Emitter; $u_\text{ein}$ geteilt durch diesen Strom ist $r_{BE}/(\beta + 1)$, fast
$1/g_m$. Im Bild: Am Abfluss fließt das ganze Wasser; wer dort den Druck verstellen will, muss es ganz bewegen.
:::

::::beispiel Basis- gegen Emitterschaltung an einer Quelle mit 50 Ohm
Der Arbeitspunkt mit $3\,\text{mA}$ und $R_C$ gleich $2\,\text{k}\Omega$:

$$v_u = 116\,\text{mS}\cdot2\,\text{k}\Omega = 232, \qquad r_\text{ein} = \frac{1{,}72\,\text{k}\Omega}{201} = 8{,}6\,\Omega.$$

**An einer Quelle mit $50\,\Omega$** kommt nur $8{,}6/58{,}6$ der Spannung am Emitter an:

$$v_u = 232\cdot\frac{8{,}6\,\Omega}{50\,\Omega + 8{,}6\,\Omega} = 34.$$

Die Emitterschaltung an derselben Quelle verliert kaum etwas, denn ihr Eingang hat $1{,}72\,\text{k}\Omega$:

$$v_u = -\frac{200\cdot2\,\text{k}\Omega}{50\,\Omega + 1{,}72\,\text{k}\Omega} = -226.$$

**Im Bild:** Am Abfluss zu rütteln kostet so viel Kraft, dass eine schwache Hand kaum etwas bewegt.
::::

Zusammengefasst, für kleine Signale und mit $r_{CE}$ groß gegen die äußeren Widerstände:

| Grundschaltung | Spannungsverstärkung | Eingangswiderstand | Ausgangs- durch Eingangsstrom |
|---|---|---|---|
| Emitterschaltung | $-g_m R_C$, groß, kehrt um | $r_{BE}$, mittel | $\beta$ |
| Kollektorschaltung | knapp $1$ | $r_{BE} + (\beta + 1)R_E$, groß | $\beta + 1$ |
| Basisschaltung | $+g_m R_C$, groß | $1/g_m$, sehr klein | $\alpha$, knapp $1$ |

## Spannungsstabilisierung mit Z-Diode

Abschnitt 11.6 des Skripts erwähnt zuerst, wo Transistoren überall arbeiten, etwa in Umrichtern der Leistungselektronik, die elektrische Maschinen steuern und
dazu große Ströme ein- und ausschalten. Dort dienen meist abgeleitete Bauelemente wie der IGBT, der Bipolartransistor mit isolierter Steuerelektrode. Als
Beispiel rechnet das Skript dann eine Anwendung des Emitterfolgers durch, die __Spannungsstabilisierung__ von Bild 11.28.

Der Ausgangspunkt ist eine schwankende Gleichspannung $U_\text{ein}$, im Skript $U_E$, etwa die Spannung am Ladekondensator eines Gleichrichters mit ihrer
Brummspannung, wie in Bild 11.29 und im Artikel über Gleichrichtung. Ein Widerstand $R_1$ führt vom Eingang zur Basis, eine Z-Diode von der Basis nach Masse,
mit der Kathode an der Basis. Der Kollektor liegt am Eingang, und am Emitter nimmt man die Ausgangsspannung $U_\text{aus}$ ab, im Skript $U_A$. Die Z-Diode hält
die Basis auf ihrer Zenerspannung $U_Z$, und der Emitterfolger gibt sie, um $U_{BE}$ vermindert, an den Ausgang weiter:

:::formel
$$U_\text{aus} = U_Z - U_{BE}.$$
:::

**So liest man das:** Eingaben sind die Zenerspannung und die Basis-Emitter-Spannung, Ausgabe die Spannung am Ausgang. Das Skript schreibt $U_Z + U_{BE}$. Mit
den Pfeilen von Bild 11.28, $U_Z$ von der Basis nach Masse und $U_{BE}$ von der Basis zum Emitter, ergibt die Masche aber das Minus; der Emitter liegt um $U_{BE}$
unter der Basis.

Die Schaltung arbeitet als Regelkreis: Zieht die Last mehr Strom und sinkt $U_\text{aus}$ ein wenig, wächst $U_{BE}$, weil die Basis fest liegt, und der
Transistor liefert mehr. Den Laststrom trägt der Transistor, die Z-Diode liefert nur den Basisstrom, den $(B + 1)$-ten Teil davon; sie wird kaum belastet. Damit
das funktioniert, müssen zwei Bedingungen auch bei der kleinsten Eingangsspannung $U_{\text{ein,min}}$ gelten. Die Z-Diode muss im Durchbruch bleiben, durch
$R_1$ muss also mindestens so viel fließen wie der größte Basisstrom $I_{B,\max}$ plus ein Mindeststrom $I_{Z,\min}$ der Diode; und der Transistor muss aktiv
bleiben:

$$\frac{U_{\text{ein,min}} - U_Z}{R_1} \ge I_{B,\max} + I_{Z,\min}, \qquad U_{\text{ein,min}} \ge U_\text{aus} + U_{CE,\text{sat}}.$$

Die Bedingung des Skripts, $U_E$ größer als $U_Z$, ist darin enthalten, aber nicht ausreichend: Ohne Reserve für die Ströme verlässt die Z-Diode den Durchbruch,
und die Schwankung des Eingangs erscheint wieder am Ausgang. Der Preis der Schaltung ist ihr Verlust: Der Transistor setzt das Produkt aus
$U_\text{ein} - U_\text{aus}$ und dem Laststrom in Wärme um, und der Wirkungsgrad ist höchstens $U_\text{aus}/U_\text{ein}$. Weil der Transistor in Reihe mit
der Last liegt, heißt die Schaltung __Längsregler__.

**Im Bild:** Ein Druckminderer: Die Steuerleitung hängt an einem Standrohr fester Höhe, und hinter dem Ventil bleibt der Druck um den Öffnungsdruck darunter, wie
stark der Turm auch schwankt und wie viel man abzapft.

:::herleitung
**Die Masche.** Von der Basis über die Basis-Emitter-Strecke zum Ausgang und über die Last nach Masse ist dieselbe Spannung wie über die Z-Diode nach Masse:

$$U_Z = U_{BE} + U_\text{aus}.$$

Nach $U_\text{aus}$ aufgelöst ergibt sich Formel (9).

**Die Z-Diode.** Der Strom durch $R_1$ ist die Spannung $U_\text{ein} - U_Z$ geteilt durch $R_1$; er teilt sich am Basisknoten auf die Basis und die Z-Diode auf.
Am schlechtesten steht die Diode bei kleinster Eingangsspannung und größtem Laststrom da; dort muss ihr Anteil noch mindestens $I_{Z,\min}$ sein. Das ist die
erste Bedingung. Der größte Basisstrom ist der größte Laststrom geteilt durch $B + 1$.

**Der Transistor.** Zwischen Kollektor und Emitter liegt $U_\text{ein} - U_\text{aus}$; das muss mindestens $U_{CE,\text{sat}}$ sein. Die Verlustleistung ist diese
Spannung mal dem Kollektorstrom, fast dem Laststrom; die Leistung am Ausgang ist $U_\text{aus}$ mal dem Laststrom, und ihr Verhältnis zur aufgenommenen
Leistung ist höchstens $U_\text{aus}/U_\text{ein}$. Im Bild: Der Druckminderer arbeitet nur, solange der Turm höher steht als das Standrohr plus einer Reserve.
:::

::::beispiel Die Z-Diode aus dem Diodenartikel mit Transistor
Die Z-Diode des Artikels über die Diode, an einer Eingangsspannung zwischen $9$ und $12\,\text{V}$, jetzt mit einem Transistor für bis zu $100\,\text{mA}$:

$$U_{Z0} = 5{,}1\,\text{V}, \qquad r_Z = 10\,\Omega, \qquad I_{Z,\min} = 1\,\text{mA}, \qquad B = 100.$$

**Der Widerstand.** Der größte Basisstrom ist $100\,\text{mA}/101$, also $0{,}99\,\text{mA}$. Nach der ersten Bedingung:

$$R_1 \le \frac{9\,\text{V} - 5{,}1\,\text{V}}{0{,}99\,\text{mA} + 1\,\text{mA}} = 1{,}96\,\text{k}\Omega.$$

Gewählt wird der Normwert $1{,}8\,\text{k}\Omega$.

**Die Ströme und Spannungen** an den Ecken des Betriebsbereichs, mit der Geraden $U_{Z0} + r_Z I_Z$ für die Z-Diode:

| $U_\text{ein}$ | Laststrom | $I_Z$ | $U_\text{aus}$ | Verlust im Transistor |
|---|---|---|---|---|
| $9\,\text{V}$ | $100\,\text{mA}$ | $1{,}17\,\text{mA}$ | $4{,}51\,\text{V}$ | $0{,}45\,\text{W}$ |
| $12\,\text{V}$ | $100\,\text{mA}$ | $2{,}83\,\text{mA}$ | $4{,}53\,\text{V}$ | $0{,}75\,\text{W}$ |
| $12\,\text{V}$ | $0$ | $3{,}81\,\text{mA}$ | $4{,}54\,\text{V}$ | $0$ |

Die Diode bleibt überall über ihrem Mindeststrom und setzt höchstens $20\,\text{mW}$ um. Der Transistor braucht dagegen bis zu $0{,}75\,\text{W}$ und damit
einen Typ für diese Leistung, und der Wirkungsgrad liegt zwischen $38$ und $50\,\%$.

**Die Probe für den Transistor.** Zwischen Kollektor und Emitter liegen mindestens $9\,\text{V} - 4{,}5\,\text{V}$, weit über $0{,}2\,\text{V}$.

**Im Bild:** Ein Standrohr von $5{,}1$ Höhe, ein Ventil, das um $0{,}6$ darunter abgibt, und ein Turm, der zwischen $9$ und $12$ schwankt.
::::

Wie gut die Schaltung glättet und wie fest ihr Ausgang unter Last bleibt, sagen zwei Kleinsignalgrößen. Schwankungen des Eingangs teilt der Spannungsteiler aus
$R_1$ und dem differentiellen Widerstand $r_Z$ der Z-Diode herunter, wie im Artikel über die Diode, und der Emitterfolger gibt den Rest fast eins zu eins weiter.
Für Änderungen des Laststroms wirkt der Ausgangswiderstand des Emitterfolgers, mit $R_1 \parallel r_Z$ als Innenwiderstand an der Basis:

:::formel
$$\Delta U_\text{aus} \approx \frac{r_Z}{R_1 + r_Z}\,\Delta U_\text{ein}, \qquad r_\text{aus} \approx \frac{1}{g_m} + \frac{R_1 \parallel r_Z}{B + 1}.$$
:::

**So liest man das:** Die erste Formel ist die Glättung, die zweite die Antwort auf die Last; beide sind klein. Gegenüber der Z-Diode allein gewinnt man doppelt:
$R_1$ darf groß sein, weil durch ihn nur der Basisstrom fließen muss, und das macht die Glättung besser; und die Last belastet die Diode nur über den Basisstrom.
Weil $g_m$ mit dem Laststrom wächst, ist auch $r_\text{aus}$ bei großem Strom am kleinsten.

**Im Bild:** Das Standrohr hängt über ein enges Rohr am Turm und schwankt deshalb kaum, und das Ventil davor liefert jeden zusätzlich gezapften Liter nach.

:::herleitung
**Die Glättung.** Für Änderungen ist die Z-Diode im Durchbruch der Widerstand $r_Z$. Der Basisstrom ändert sich mit dem Eingang kaum, also teilen $R_1$ und $r_Z$
eine Änderung des Eingangs wie ein Spannungsteiler; die Basis ändert sich um den Anteil $r_Z/(R_1 + r_Z)$. Der Emitterfolger hat eine Verstärkung von fast eins,
und so viel ändert sich auch der Ausgang.

**Die Last.** An der Basis liegt für Änderungen der Innenwiderstand $R_1 \parallel r_Z$, weil die Versorgung am Eingang dafür ein Kurzschluss ist. Nach dem
Ausgangswiderstand des Emitterfolgers mit diesem $R_Q$ und $r_{BE}/(\beta + 1)$ fast $1/g_m$ folgt die zweite Formel; $R_E$ fehlt, denn die Last selbst ist der
Emitterwiderstand. Im Bild: Das Standrohr ist mit dem Turm nur über eine Engstelle verbunden; sein Pegel folgt dem Turm nur zu einem winzigen Teil.
:::

::::beispiel Glättung und Last im Zahlenbeispiel
Die Schaltung von oben mit $R_1$ gleich $1{,}8\,\text{k}\Omega$, $r_Z$ gleich $10\,\Omega$ und $B$ gleich $100$.

**Glättung.** Schwankt der Eingang um $3\,\text{V}$, schwankt der Ausgang um

$$\Delta U_\text{aus} \approx \frac{10\,\Omega}{1{,}81\,\text{k}\Omega}\cdot3\,\text{V} = 16{,}6\,\text{mV}.$$

Im Diodenartikel ergab dieselbe Diode mit $330\,\Omega$ und ganz ohne Last $88\,\text{mV}$. Allein für $100\,\text{mA}$ hätte sie einen Vorwiderstand von höchstens
$38{,}6\,\Omega$ gebraucht, dann $0{,}62\,\text{V}$ Schwankung und ohne Last bis zu $0{,}72\,\text{W}$ in der Diode.

**Kleine Laständerungen bei $100\,\text{mA}$.**

$$r_\text{aus} \approx \frac{25{,}85\,\text{mV}}{100\,\text{mA}} + \frac{9{,}95\,\Omega}{101} = 0{,}26\,\Omega + 0{,}10\,\Omega = 0{,}36\,\Omega.$$

Zehn Milliampere mehr senken den Ausgang um $3{,}6\,\text{mV}$.

**Große Laständerungen.** Von $10$ auf $100\,\text{mA}$ ist das Signal nicht mehr klein; dann rechnet man mit der Transfergleichung. $U_{BE}$ wächst um
$U_T\ln10$, also $60\,\text{mV}$, und der zusätzliche Basisstrom von $0{,}89\,\text{mA}$ senkt die Basis an $R_1 \parallel r_Z$ um $9\,\text{mV}$. Zusammen sinkt
der Ausgang um knapp $70\,\text{mV}$, was das Modell mit festem $U_{BE}$ nicht zeigt.

**Im Bild:** Der Turm schwankt um drei Meter, das Wasser hinter dem Druckminderer um wenige Zentimeter.
::::

:::grafik
Szene: get1/bipolartransistoren/03-spannungsstabilisierung · Vorlage: laengsregler
Links die Schaltung von Bild 11.28 mit den Namen dieses Artikels: $U_\text{ein}$ zwischen $9$ und $12\,\text{V}$, $R_1 = 1{,}8\,\text{k}\Omega$, die Z-Diode mit
$5{,}1\,\text{V}$ und $r_Z = 10\,\Omega$ von der Basis nach Masse, der npn-Transistor mit dem Kollektor am Eingang und dem Emitter am Ausgang, eine Last mit
einstellbarem Strom bis $100\,\text{mA}$; Zählpfeile für $U_Z$ von der Basis nach Masse, $U_{BE}$ von der Basis zum Emitter und $U_\text{aus}$. Rechts über der
Zeit die Eingangsspannung mit Brummspannung wie in Bild 11.29 und darunter die fast glatte Ausgangsspannung bei $4{,}5\,\text{V}$, mit einer vergrößerten
Ausschnittsachse, in der die Restschwankung von $17\,\text{mV}$ sichtbar wird. Zähler zeigen $I_Z$, den Basisstrom und die Verlustleistung des Transistors;
sinkt der Eingang zu tief, färbt sich die Z-Diode, weil sie den Durchbruch verlässt. Kernaussage: Die Z-Diode hält die Basis, der Emitterfolger trägt die Last.
(Rot = Transistor und Ausgang, blau = Eingang und Brumm, orange = Z-Diode und Regelung, grau = übrige Bauteile.)
:::

## Bedeutung und Ausblick

Für kleine Signale ist der Transistor ein lineares Zweitor aus drei Kenngrößen, die alle der Arbeitspunktstrom festlegt: Steilheit, Eingangs- und
Ausgangswiderstand. Damit verstärkt eine einzelne Emitterschaltung einige hundertfach, bis zur Grenze $g_m r_{CE}$ von einigen tausend; ihre Verstärkung ist
die Spannung an $R_C$ geteilt durch $U_T$. Sauber gelingt das aber nur für Signale von wenigen Millivolt, und die Verstärkung hängt am Arbeitspunkt. Gegenkopplung
tauscht Verstärkung gegen Genauigkeit: Mit einem Emitterwiderstand wird die Verstärkung zu $-R_C/R_E$, unabhängig von Exemplar und Temperatur.

Kollektor- und Basisschaltung ergänzen die Emitterschaltung: die eine als Impedanzwandler, der eine schwache Quelle eine kräftige Last treiben lässt, die
andere mit kleinem Eingangswiderstand. Als Längsregler mit Z-Diode hält der Emitterfolger eine Spannung fest, auf Kosten von Verlustleistung.

Der nächste Schritt fasst viele Transistoren in einem Baustein zusammen: Der __Operationsverstärker__ enthält Differenzverstärker, Stromspiegel und
Emitterfolger und verstärkt hunderttausendfach und mehr. Erst die äußere Gegenkopplung macht daraus Verstärker, deren Verstärkung allein Widerstände
bestimmen, nach demselben Prinzip wie der Emitterwiderstand dieses Artikels. Wechselsignale mit Koppel- und Überbrückungskondensatoren und das Verhalten bei
hohen Frequenzen folgen in der Wechselstromtechnik und der Schaltungstechnik.

:::kern
- Ein Verstärker trägt das Signal auf dem Arbeitspunkt: $u_{BE}=U_{BE}+u_{be}$.
- Steilheit $g_m=I_C/U_T$, gleich für jeden Bipolartransistor beim selben Strom.
- Kleinsignalbetrieb heißt wenige Millivolt: bei $5\,\text{mV}$ an der Basis schon rund zehn Prozent Verzerrung.
- Early-Effekt: Die Ausgangskennlinien steigen und treffen sich bei $-U_\text{Early}$; daraus folgt der Ausgangswiderstand $r_{CE}$.
- Kleinsignal-Ersatzschaltbild: $r_{BE}=\beta/g_m$, Stromquelle $g_m u_{be}$, parallel $r_{CE}$.
- Emitterschaltung: $v_u=-g_m(R_C\parallel r_{CE})$, also die Spannung an $R_C$ durch $U_T$; höchstens $g_m r_{CE}$.
- Mit Emitterwiderstand für das Signal wird $v_u\approx-R_C/R_E$, genau, linear und klein.
- Emitterfolger: Verstärkung knapp eins, Eingang $r_{BE}+(\beta+1)R_E$, Ausgang etwa $1/g_m$.
- Basisschaltung: Verstärkung $+g_m R_C$, Eingangswiderstand nur etwa $1/g_m$.
- Längsregler: $U_\text{aus}=U_Z-U_{BE}$, nicht plus; die Z-Diode trägt nur den Basisstrom.
- Glättung des Längsreglers: Schwankungen werden um $r_Z/(R_1+r_Z)$ verkleinert.
:::

:::quiz
F: Warum darf das Signal am Eingang einer Emitterschaltung nur wenige Millivolt groß sein?
A: Der Kollektorstrom ist $I_C\exp(u_{be}/U_T)$; nur das lineare Glied der Reihe gibt eine konstante Verstärkung. Das quadratische Glied ist relativ $u_{be}/(2U_T)$ groß, ein Prozent bei $0{,}5\,\text{mV}$, zehn Prozent bei $5\,\text{mV}$, und macht die positive Halbschwingung größer als die negative.
F: Was ist die Steilheit, und warum ist sie bei jedem Bipolartransistor gleich, wenn der Strom gleich ist?
A: Die Ableitung $\partial I_C/\partial U_{BE}$ im Arbeitspunkt. Weil die Exponentialfunktion ihre eigene Ableitung ist, ergibt sich $I_C/U_T$; der Sättigungsstrom $I_S$, der von Bauart und Fläche abhängt, fällt heraus. Bei $1\,\text{mA}$ sind es $38{,}7\,\text{mS}$, bei $3\,\text{mA}$ $116\,\text{mS}$.
F: Was ist der Early-Effekt, und was folgt aus ihm?
A: Eine größere Kollektorspannung verbreitert die Sperrschicht in die Basis hinein, die wirksame Basis wird dünner, und der Strom wächst. Die Ausgangskennlinien steigen leicht und treffen sich verlängert bei $-U_\text{Early}$; daraus folgen der endliche Ausgangswiderstand $r_{CE}=(U_\text{Early}+U_{CE})/I_C$ und ein $B$, das mit $U_{CE}$ wächst, wie das Skript sagt.
F: Was beschreibt das erweiterte Ersatzschaltbild von Bild 11.21?
A: Die gesamten Ströme und Spannungen in der Umgebung eines Arbeitspunkts, mit einer Quelle $U_0$ und $R_{BE}$ am Eingang und einer gesteuerten Stromquelle mit $R_{CE}$ am Ausgang. Jede Gleichung ist eine Tangente an die reale Kennlinie; im Arbeitspunkt mit $3\,\text{mA}$ und $15\,\mu\text{A}$ sind das $R_{BE}=1{,}72\,\text{k}\Omega$, $U_0=0{,}656\,\text{V}$ und $R_{CE}=35{,}3\,\text{k}\Omega$.
F: Wie entsteht das Kleinsignal-Ersatzschaltbild, und welche Kenngrößen hat es?
A: Man legt nach dem Überlagerungsverfahren die festen Anteile still; es bleiben $r_{BE}=\beta/g_m$ zwischen Basis und Emitter und die Stromquelle $g_m u_{be}$ parallel zu $r_{CE}$. Als Zweitor ist das die Hybridform mit $H_{11}=r_{BE}$, $H_{21}=\beta$, $H_{22}=1/r_{CE}$ ohne Rückwirkung; der Transistor des Zweitor-Beispiels arbeitet so bei rund $2\,\text{mA}$.
F: Warum ist die Verstärkung der Emitterschaltung die Spannung an $R_C$ geteilt durch $U_T$?
A: Nach $v_u=-g_m R_C$ mit $g_m=I_C/U_T$ ist der Betrag $I_C R_C/U_T$, und $I_C R_C$ ist die Gleichspannung an $R_C$. Mit $6\,\text{V}$ an $R_C$ sind es $232$, mit $r_{CE}$ parallel $220$; die Obergrenze ist $g_m r_{CE}=(U_\text{Early}+U_{CE})/U_T$, rund $4100$.
F: Was bewirkt ein Emitterwiderstand, der auch für das Signal wirkt?
A: Die Verstärkung wird $-\beta R_C/(r_{BE}+(\beta+1)R_E)\approx-R_C/(R_E+1/g_m)$, fast $-R_C/R_E$, unabhängig von $\beta$ und Strom. Im Beispiel mit $2\,\text{k}\Omega$ und $1\,\text{k}\Omega$ sind es $-1{,}97$ statt $-162$; dafür trägt $R_E$ fast das ganze Eingangssignal, und erst $0{,}43\,\text{V}$ statt $5\,\text{mV}$ verzerren merklich.
F: Warum ist der Emitterfolger ein Impedanzwandler?
A: Seine Verstärkung ist knapp eins, sein Eingangswiderstand $r_{BE}+(\beta+1)R_E$ groß und sein Ausgangswiderstand etwa $1/g_m+R_Q/(\beta+1)$ klein. Im Beispiel wird aus einer Quelle mit $10\,\text{k}\Omega$ am Ausgang eine mit $57\,\Omega$, bei $203\,\text{k}\Omega$ am Eingang.
F: Worin unterscheidet sich die Basisschaltung von der Emitterschaltung?
A: Sie verstärkt ebenso stark, $+g_m R_C$, kehrt aber nicht um, und ihr Eingangswiderstand ist nur $r_{BE}/(\beta+1)$, etwa $1/g_m$, bei $3\,\text{mA}$ also $8{,}6\,\Omega$. An einer Quelle mit $50\,\Omega$ bleibt deshalb nur eine Verstärkung von $34$, während die Emitterschaltung $-226$ erreicht.
F: Wie arbeitet der Längsregler mit Z-Diode, und was ist am Skript zu korrigieren?
A: Die Z-Diode hält die Basis auf $U_Z$, der Emitterfolger gibt $U_\text{aus}=U_Z-U_{BE}$ weiter und trägt die Last, die Diode nur den Basisstrom. Das Skript schreibt $U_Z+U_{BE}$, die Pfeile von Bild 11.28 ergeben aber das Minus; und $U_E>U_Z$ genügt nicht, durch $R_1$ muss bei kleinster Eingangsspannung noch der größte Basisstrom plus ein Mindeststrom der Diode fließen. Mit $1{,}8\,\text{k}\Omega$ und $r_Z=10\,\Omega$ werden aus $3\,\text{V}$ Schwankung $17\,\text{mV}$.
:::
