---
title: Die MOS-Kapazität
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Bauelemente
order: 4060300
summary: Das Herzstück des Transistors – ein Kondensator aus Metall, Oxid und Halbleiter, dessen Gatespannung die Bänder an der Halbleiteroberfläche verbiegt. Je nach Spannung durchläuft er drei Zustände (Akkumulation, Verarmung, Inversion). Die daraus folgende C-V-Kurve ist das zentrale Messwerkzeug der Halbleitertechnik – und die Inversionsschicht wird später der leitende Kanal des MOSFET.
tags: MOS-Kondensator, Akkumulation, Verarmung, Inversion, Debye-Länge, C-V-Kurve, Grenzflächenzustände, Schwellenspannung
---

:::grafik
Einstiegs-Animation: Ein Schichtaufbau Metall–Oxid–p-Silizium mit einem Gatespannungs-Schieberegler. Bei
__negativer__ Spannung sammeln sich Löcher an der Oxid-Grenzfläche (__Akkumulation__). Dreht man ins Positive,
werden die Löcher weggedrückt, zurück bleiben ortsfeste negative Akzeptoren (__Verarmung__). Bei großer positiver
Spannung bildet sich plötzlich eine dünne Schicht **Elektronen** an der Oberfläche (__Inversion__) — obwohl der
Halbleiter p-dotiert ist. Rechts zeichnet sich synchron die __C-V-Kurve__: hoch, Minimum, dann wieder hoch (oder
tief, je nach Frequenz). Kernbotschaft: Die Gatespannung schaltet die Oberfläche zwischen drei Zuständen — das ist
der Schalthebel des Transistors.
:::

:::konzept
Der __MOS-Kondensator__ (Metall–Oxid–Halbleiter) ist das Herzstück des MOSFET. Er sieht aus wie ein
Plattenkondensator: eine metallische __Gate__-Elektrode, darunter ein dünner Isolator (bei Silizium das
Oxid $\text{SiO}_2$), darunter der p-dotierte Halbleiter. Durch das Oxid fließt **kein** Strom — aber die
Gatespannung **verbiegt die Bänder** an der Halbleiteroberfläche und steuert so, welche Ladungsträger sich dort
sammeln. Je nach Spannung durchläuft der MOS-Kondensator drei grundverschiedene Zustände. Sie zu verstehen, heißt,
den Transistor zu verstehen — und die daraus folgende __C-V-Kurve__ ist das wichtigste Diagnosewerkzeug der ganzen
Halbleitertechnik.
:::

**Worum es geht:** Wir führen die __Debye-Länge__ als Abschirmlänge ein, gehen die drei Zustände __Akkumulation__,
__Verarmung__ und __Inversion__ durch, setzen daraus die __Gate-Kapazität__ zusammen und verstehen die __C-V-Kurve__
samt ihrer Frequenzabhängigkeit.

## Vorbaustein: die Debye-Länge

Frei bewegliche Ladungen schirmen jede Potentialänderung ab — aber nicht abrupt, sondern über eine
charakteristische Länge, die __Debye-Länge__:

$$L_D = \sqrt{\frac{\varepsilon_0\varepsilon_r\,k_B T}{e^2\,N_A}}.$$

Sie sagt, wie „scharf" eine Bandverbiegung an der Oberfläche sein kann. Wo **viele** freie Ladungen sitzen
(Akkumulation, Inversion), ist $L_D$ winzig und die Grenzschicht wirkt fast wie ein **Metall** (das Feld wird auf
kürzester Strecke abgeschirmt). Wo **wenige** sind (Verarmung), reicht die Bandverbiegung tiefer hinein.

:::grafik
Eine Potentialstörung an der Oberfläche, die exponentiell $\propto e^{-x/L_D}$ ins Innere abklingt; daneben zwei
Fälle: viele freie Ladungen (kurzes $L_D$, „quasi-metallisch") vs. wenige (langes $L_D$).
:::

## Zustand 1 — Akkumulation (V_g < 0)

Legt man eine **negative** Gatespannung an, zieht sie die (positiven) **Löcher** des p-Halbleiters an die
Oxid-Grenzfläche. Dort entsteht eine hohe Löcherdichte — die Grenzschicht wird **quasi-metallisch**. Damit ist der
MOS-Kondensator ein simpler **Plattenkondensator** Metall–Oxid–„Metall", seine Kapazität ist schlicht die des
Oxids:

$$C_{ges} \approx C_{IS} = \frac{\varepsilon_0\varepsilon_{IS}}{d_{IS}}.$$

:::grafik
Banddiagramm an der Oberfläche: Valenzband biegt sich zur Grenzfläche hin **nach oben** an $E_f$ heran, viele
Löcher (offene Kreise) sammeln sich am Oxid. Daneben das Ersatzbild „Plattenkondensator, $C_{ges}\approx C_{IS}$".
:::

## Zustand 2 — Verarmung (V_g > 0, moderat)

Dreht man die Spannung ins **mäßig Positive**, werden die Löcher von der Oberfläche **in den Bulk gedrückt**.
Zurück bleiben die ortsfesten, ionisierten **Akzeptoren** $N_A^-$ — eine __Verarmungszone__, genau wie beim
pn-Übergang, nur einseitig. Die Poisson-Gleichung liefert wieder eine **parabelförmige** Bandverbiegung mit der
Verarmungsweite

$$L_{\text{depl}} = \sqrt{\frac{2\,\varphi_s\,\varepsilon_0\varepsilon_{r,SC}}{e^2\,N_A}},$$

wobei $\varphi_s$ die Bandverbiegung an der Oberfläche ist. Kapazitiv liegt jetzt zur Oxidkapazität eine
**Verarmungskapazität** $C_{\text{depl}}=\varepsilon_0\varepsilon_{r,SC}/L_{\text{depl}}$ in **Reihe** — die
Gesamtkapazität sinkt in ein **Minimum**.

:::grafik
Banddiagramm: Bänder biegen sich an der Oberfläche nach unten, Löcher sind weg, nur ortsfeste „−"-Akzeptoren in
einer Zone der Breite $L_{\text{depl}}$. Daneben das Ersatzbild „$C_{IS}$ in Reihe mit $C_{\text{depl}}$ →
Kapazität fällt".
:::

## Zustand 3 — Inversion (V_g groß)

Erhöht man die Spannung weiter, wird das **intrinsische** Fermi-Niveau $E_f^{\,i}$ an der Oberfläche schließlich
**unter** das Fermi-Niveau $E_f$ gedrückt. Damit ist die Oberfläche dort **lokal n-leitend** — obwohl der Bulk
p-Typ ist; die Ladungsträgersorte hat sich „invertiert". Weil $E_f$ nun dem Leitungsband nahekommt, steigt die
**Elektronendichte exponentiell** und bildet eine hauchdünne __Inversionsschicht__ direkt unter dem Oxid. Diese
Schicht ist wieder quasi-metallisch, also $C_{ges}\approx C_{IS}$ — und sie ist genau der **leitende Kanal**, den der
MOSFET später zum Schalten nutzt.

:::grafik
Banddiagramm: starke Bandverbiegung, das Leitungsband taucht an der Oberfläche unter $E_f$; eine dünne, dichte
Elektronenschicht (Inversionskanal) am Oxid. Beschriftung „p-Bulk, aber n-leitende Oberfläche".
:::

Die Spannung, ab der die Inversion einsetzt, heißt __Schwellenspannung__ $V_{th}$; die Spannung des Übergangs von
Akkumulation zu Verarmung die __Flachbandspannung__ $V_{FB}$.

**Wann genau setzt starke Inversion ein?** Das übliche Kriterium: Die Oberfläche soll so stark n-leitend werden,
wie der Bulk p-leitend ist. Das ist erreicht, wenn das __Oberflächenpotential__ $\varphi_s$ gerade das Doppelte des
__Bulk-Potentials__ $\varphi_B$ erreicht,

$$\varphi_s = 2\,\varphi_B, \qquad \varphi_B = V_T\,\ln\!\frac{N_A}{n_i}, \qquad V_T = \frac{k_B T}{e}\approx 26\,\text{mV (RT)},$$

mit der __Temperaturspannung__ $V_T$. Genau an dieser Schwelle ($\varphi_s = 2\varphi_B$) liegt die
Schwellenspannung $V_{th}$ — darüber wächst die Inversionsladung exponentiell.

## Die Gate-Kapazität

Die Gatespannung teilt sich auf zwischen dem Abfall über dem **Oxid** und der **Bandverbiegung** im Halbleiter —
kapazitiv eine **Reihenschaltung**:

$$C_{ges} = \frac{C_{IS}\,C_{SC}}{C_{IS}+C_{SC}}, \qquad C_{SC} = C_{\text{depl}} + C_{\text{it}} + C_{\text{inv}}.$$

Die Halbleiterkapazität $C_{SC}$ ist ihrerseits eine **Parallelschaltung** der Beiträge von Verarmung, Inversion
und Grenzflächenzuständen (alle reagieren am selben Ort auf die Oberflächenspannung). In **Akkumulation** und
**starker Inversion** ist die Grenzschicht quasi-metallisch ($C_{SC}$ riesig), sodass $C_{ges}\approx C_{IS}$; in der
**Verarmung** dazwischen fällt $C_{ges}$ in ein Minimum.

:::grafik
Ersatzschaltbild: $C_{IS}$ in Reihe zur Parallelschaltung $C_{\text{depl}}\,\|\,C_{\text{it}}\,\|\,
C_{\text{inv}}$. Daneben drei Miniatur-Banddiagramme (Akkumulation/Verarmung/Inversion) mit dem jeweils
dominierenden Kapazitätsbeitrag.
:::

## Die C-V-Kurve: nieder- vs. hochfrequent

Trägt man $C_{ges}/C_{IS}$ über der Gatespannung auf, entsteht die charakteristische Wanne: **hoch** in Akkumulation
($\approx C_{IS}$), **Minimum** in Verarmung — und in Inversion wird es **frequenzabhängig**. Der Grund: Die
Inversionsladung besteht aus **Minoritäten** (Elektronen im p-Typ), die nur langsam nachgeliefert werden.

- **Niederfrequenz** (quasi-statisch): Die Inversionsladung kann dem langsamen Messsignal folgen → $C_{ges}$ steigt
  in Inversion wieder auf $\approx C_{IS}$.
- **Hochfrequenz**: Die träge Inversionsladung kann **nicht** folgen; nur die Verarmungsladung reagiert → $C_{ges}$
  bleibt in Inversion auf einem tiefen Plateau $\dfrac{C_{IS}C_{\text{depl}}}{C_{IS}+C_{\text{depl}}}$.

:::grafik
Die C-V-Kurve $C_{ges}/C_{IS}$ über $V_g$: links Plateau bei 1 (Akkumulation), Minimum in der Verarmung, dann zwei
Äste in Inversion — die Niederfrequenzkurve steigt zurück auf 1, die Hochfrequenzkurve bleibt unten. Markiert
$V_{FB}$ und $V_{th}$.
:::

## Grenzflächenzustände und warum SiO₂ so gut ist

An der $\text{Si}/\text{SiO}_2$-Grenzfläche ist nicht jedes Silizium-Atom voll gebunden; es bleiben **ungesättigte
Bindungen** (*dangling bonds*). Ihre Energien liegen **in der Bandlücke** und wirken als Fallen mit der
Flächendichte $D_{it}$. Der große Vorteil von $\text{SiO}_2$ als „arteigenem", aus dem Silizium selbst gewachsenem
Oxid: Es senkt diese __Grenzflächenzustandsdichte__ um rund den Faktor $10^5$ — das ist einer der Hauptgründe,
warum ausgerechnet Silizium die Mikroelektronik dominiert.

Praktisch misst man $D_{it}$ aus der **Differenz** von Nieder- und Hochfrequenz-C-V-Kurve: Was die
Niederfrequenzkurve mehr an Kapazität zeigt, stammt gerade von den (langsamen) Grenzflächenfallen.

:::grafik
Grenzfläche Si/SiO₂ mit einigen offenen „dangling bonds"; ihre Fallenniveaus liegen in der Bandlücke. Daneben
zwei C-V-Kurven, deren Differenzfläche „$\propto D_{it}$" schraffiert ist.
:::

:::kern
Der __MOS-Kondensator__ (Metall–Oxid–p-Si) steuert über die Gatespannung die Bandverbiegung an der Oberfläche;
durch das Oxid fließt kein Strom. __Debye-Länge__ $L_D=\sqrt{\varepsilon_0\varepsilon_r k_BT/(e^2N_A)}$ =
Abschirmlänge. Drei Zustände: __Akkumulation__ ($V_g<0$: Löcher an der Oberfläche, quasi-metallisch,
$C_{ges}\approx C_{IS}$), __Verarmung__ (moderat $V_g>0$: ortsfeste Akzeptoren, $L_{\text{depl}}=\sqrt{2\varphi_s
\varepsilon_0\varepsilon_{r,SC}/(e^2N_A)}$, $C_{ges}$-Minimum), __Inversion__ (großes $V_g$: Oberfläche n-leitend,
Elektronen-__Inversionsschicht__ = späterer Kanal, $C_{ges}\approx C_{IS}$). Gate-Kapazität $C_{ges}=\tfrac{C_{IS}C_{SC}}
{C_{IS}+C_{SC}}$ mit $C_{SC}=C_{\text{depl}}+C_{\text{it}}+C_{\text{inv}}$. __C-V-Kurve__: Niederfrequenz steigt
in Inversion zurück auf $C_{IS}$, Hochfrequenz bleibt auf tiefem Plateau; ihre Differenz liefert $D_{it}$.
$\text{SiO}_2$ senkt die Grenzflächenfallen $D_{it}$ um $\sim10^5$.
:::

Der MOS-Kondensator kann an der Oberfläche einen leitenden Elektronenkanal **ein- und ausschalten**. Gibt man
ihm zwei Kontakte (Source und Drain), die diesen Kanal anzapfen, wird daraus das wichtigste Bauelement der
Elektronik — der __MOSFET__, das Thema des letzten Artikels.

:::quiz
F: Warum steuert die Gatespannung den Halbleiter, obwohl durch das Oxid gar kein Strom fließt?
A: Das Oxid wirkt als Isolator eines Kondensators: Die Gatespannung erzeugt ein Feld, das die Bänder an der Halbleiteroberfläche verbiegt und dort Ladungsträger anzieht oder wegdrückt. Gesteuert wird also kapazitiv, nicht durch Stromfluss.
F: Was sagt die Debye-Länge über die Schärfe der Bandverbiegung aus?
A: Sie ist die Strecke, über die freie Ladungen eine Potentialstörung abschirmen. Viele freie Ladungen (Akkumulation, Inversion) ergeben ein winziges $L_D$ und eine quasi-metallische, scharfe Grenzschicht; wenige (Verarmung) lassen die Verbiegung tief ins Innere reichen.
F: Warum verhält sich der MOS-Kondensator in Akkumulation wie ein einfacher Plattenkondensator?
A: Die negative Gatespannung häuft Löcher an der Oxidgrenze zu einer quasi-metallischen Schicht. Damit liegt effektiv Metall–Oxid–Metall vor, und die Gesamtkapazität ist schlicht die des Oxids $C_{IS}$.
F: Warum sinkt die Kapazität in der Verarmung in ein Minimum?
A: Die weggedrückten Löcher hinterlassen eine Verarmungszone, die wie ein zweiter Kondensator wirkt. Diese Verarmungskapazität liegt in Reihe zum Oxid, und eine Reihenschaltung ergibt stets eine kleinere Gesamtkapazität.
F: Warum entsteht bei großer positiver Spannung eine n-leitende Schicht auf einem p-Halbleiter?
A: Die starke Bandverbiegung drückt das Leitungsband an der Oberfläche nahe an $E_f$, sodass dort die Elektronendichte exponentiell ansteigt. An der Oberfläche überwiegen dann Elektronen — die Ladungsträgersorte hat sich gegenüber dem p-Bulk „invertiert".
F: Was besagt das Inversionskriterium $\varphi_s=2\varphi_B$ anschaulich?
A: Die Oberfläche soll so stark n-leitend werden, wie der Bulk p-leitend ist. Das ist gerade erreicht, wenn das Oberflächenpotential das Doppelte des Bulk-Potentials beträgt — die Schwelle, ab der die Inversionsladung exponentiell wächst.
F: Warum ist die Gate-Kapazität eine Reihenschaltung aus Oxid- und Halbleiterkapazität?
A: Die Gatespannung teilt sich in den Abfall über dem Oxid und die Bandverbiegung im Halbleiter auf. Zwei hintereinander durchlaufene Spannungsabfälle entsprechen kapazitiv einer Reihenschaltung der beiden zugehörigen Kapazitäten.
F: Warum ist die C-V-Kurve in Inversion frequenzabhängig?
A: Die Inversionsladung besteht aus Minoritäten (Elektronen im p-Typ), die nur langsam nachgeliefert werden. Bei niedriger Frequenz folgen sie dem Messsignal (C steigt zurück auf $C_{IS}$), bei hoher Frequenz können sie nicht folgen und nur die Verarmungsladung reagiert (tiefes Plateau).
F: Warum sind Grenzflächenzustände (dangling bonds) schädlich?
A: An der Si/SiO₂-Grenze bleiben ungesättigte Bindungen, deren Energien in der Bandlücke liegen und als Fallen wirken. Sie fangen Ladung ein, verfälschen die Schwellenspannung und verschlechtern den Schaltvorgang des Transistors.
F: Warum hat ausgerechnet SiO₂ Silizium zur Dominanz in der Mikroelektronik verholfen?
A: Als arteigenes, aus dem Silizium selbst gewachsenes Oxid passiviert SiO₂ die Grenzfläche außergewöhnlich gut und senkt die Grenzflächenzustandsdichte $D_{it}$ um rund fünf Größenordnungen. Eine so saubere Isolator-Halbleiter-Grenze bietet kaum ein anderes Materialsystem.
:::
