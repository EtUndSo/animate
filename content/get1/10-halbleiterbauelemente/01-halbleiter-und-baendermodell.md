---
title: Halbleiter und das Bändermodell
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100100
summary: Warum Halbleiter zwischen Leiter und Isolator stehen und sich gezielt steuern lassen – vom Bändermodell über Eigenleitung und Dotierung bis zum pn-Übergang, der Grundlage fast aller modernen Bauelemente.
tags: Halbleiter, Bändermodell, Bandlücke, Eigenleitung, Loch, Dotierung, pn-Übergang, Raumladungszone
---

:::konzept
Ein Leiter leitet, ein Isolator sperrt — und ein **Halbleiter** liegt dazwischen, mit einer entscheidenden
Zusatzeigenschaft: Man kann seine Leitfähigkeit **gezielt steuern**, durch Temperatur, Licht, eingebaute
Fremdatome oder eine angelegte Spannung. Genau diese Steuerbarkeit macht ihn zum Baustein jeder Diode, jedes
Transistors und damit der gesamten Mikroelektronik. Warum das so ist, erklärt das **Bändermodell**.
:::

**Worum es geht:** Bisher waren Bauteile entweder leitend (Widerstand) oder isolierend. Der __Halbleiter__ bricht
dieses Schema auf. Wir bauen von unten auf: erst die Energiebänder, dann wie Ladungsträger entstehen, dann wie
man sie durch __Dotierung__ einstellt — und schließlich den __pn-Übergang__, das Herz der meisten Bauelemente.

## Das Bändermodell: Leiter, Isolator, Halbleiter

In einem einzelnen Atom dürfen Elektronen nur bestimmte Energien annehmen. Rücken viele Atome in einem Kristall
zusammen, verschmelzen diese Niveaus zu breiten __Energiebändern__. Für die Leitung zählen zwei davon: das
__Valenzband__ (die äußeren, gebundenen Elektronen) und das darüberliegende __Leitungsband__ (dort sind
Elektronen frei beweglich). Dazwischen liegt die __Bandlücke__ $E_\text{g}$ — ein verbotener Energiebereich,
den ein Elektron überspringen muss, um vom gebundenen in den frei beweglichen Zustand zu gelangen.

Die Breite dieser Lücke entscheidet über den Charakter des Stoffes:

| Stofftyp | Bandlücke $E_\text{g}$ | Verhalten |
|---|---|---|
| Leiter (Metall) | keine (Bänder überlappen) | immer viele freie Elektronen |
| Halbleiter | klein, $\approx 1\,\text{eV}$ (Si: $1{,}1\,\text{eV}$) | leitet bei Wärme/Licht, sonst kaum |
| Isolator | groß, $> 3\,\text{eV}$ | praktisch keine freien Elektronen |

Beim **Leiter** überlappen Valenz- und Leitungsband, es sind immer frei bewegliche Elektronen da. Beim
**Isolator** ist die Lücke so groß, dass thermische Energie sie nicht überbrücken kann. Der **Halbleiter** liegt
dazwischen: Seine Lücke ist klein genug, dass schon die Wärme bei Raumtemperatur einige Elektronen
hinüberhebt.

:::grafik
Drei Energiebanddiagramme nebeneinander (Energie nach oben): Leiter (Valenz- und Leitungsband überlappen),
Halbleiter (schmale Lücke $\approx 1\,\text{eV}$), Isolator (breite Lücke $> 3\,\text{eV}$). Valenzband unten
gefüllt, Leitungsband oben, die Lücke jeweils markiert.
:::

## Eigenleitung: Elektronen und Löcher

Oberhalb des absoluten Nullpunkts schafft es ein kleiner Teil der Elektronen durch die thermische Energie über
die Bandlücke ins Leitungsband. Jedes Elektron, das hinüberspringt, hinterlässt im Valenzband eine Leerstelle —
ein __Loch__. Es entsteht also immer ein __Elektron-Loch-Paar__, und beide tragen zur Leitung bei. Diese
temperaturabhängige Eigenleitfähigkeit eines reinen Halbleiters heißt __Eigenleitung__.

Das __Loch__ verdient eine zweite Betrachtung, denn es ist mehr als nur „nichts". Rückt ein benachbartes
Valenzelektron in die Leerstelle nach, wandert das Loch in die Gegenrichtung. Man kann das Loch deshalb als
eigenständigen, **positiv geladenen** beweglichen Ladungsträger behandeln — genauso, wie eine Luftblase im
Wasser nach oben „steigt", obwohl in Wirklichkeit nur Wasser nach unten fließt. Diese Sichtweise vereinfacht
alles Weitere enorm: Im Halbleiter gibt es zwei Sorten Ladungsträger, negative **Elektronen** und positive
**Löcher**.

:::grafik
Ein Banddiagramm, in dem ein Elektron (Punkt) von unten über die Lücke ins Leitungsband springt und im
Valenzband ein Loch (offener Kreis) zurücklässt. Pfeile zeigen: Elektron wandert nach rechts, das Loch effektiv
nach links.
:::

## Dotierung: Leitfähigkeit nach Maß

Die Eigenleitung ist schwach und schwer kontrollierbar. Den eigentlichen Sprung bringt die __Dotierung__: der
gezielte Einbau von Fremdatomen. Silizium ist vierwertig; man ersetzt einzelne Atome durch solche mit einer
anderen Wertigkeit.

Bei der __n-Dotierung__ baut man **fünfwertige** Atome ein (__Donatoren__, etwa Phosphor). Vier ihrer
Außenelektronen binden ins Gitter, das fünfte ist überzählig und schon bei Raumtemperatur praktisch frei. Es gibt
also zusätzliche frei bewegliche **Elektronen** — die Elektronen sind hier die __Majoritätsträger__.

Bei der __p-Dotierung__ baut man **dreiwertige** Atome ein (__Akzeptoren__, etwa Bor). Ihnen fehlt ein Elektron
zur vollständigen Bindung; sie „fangen" eines aus dem Valenzband und hinterlassen dort ein **Loch**. Hier sind
die Löcher die Majoritätsträger. Mit der Dotierungskonzentration stellt man die Leitfähigkeit über viele
Größenordnungen gezielt ein — das ist der Schlüssel zur gesamten Bauelementetechnik.

:::grafik
Zwei Gitterausschnitte: links n-dotiert mit einem fünfwertigen Donator, dessen fünftes Elektron lose daneben
sitzt (freier Ladungsträger $-$); rechts p-dotiert mit einem dreiwertigen Akzeptor, der ein Loch ($+$) im Gitter
erzeugt.
:::

## Der pn-Übergang

Bringt man ein n- und ein p-dotiertes Gebiet in direkten Kontakt, passiert das Entscheidende. An der Grenze
treffen viele freie Elektronen (n-Seite) auf viele Löcher (p-Seite). Sie __diffundieren__ ins jeweils andere
Gebiet und __rekombinieren__ dort — ein Elektron füllt ein Loch, beide verschwinden als freie Träger.

Zurück bleiben in der Grenzschicht nur die **ortsfesten** geladenen Dotieratome: positive Donatorrümpfe auf der
n-Seite, negative Akzeptorrümpfe auf der p-Seite. Diese an frei beweglichen Trägern verarmte Schicht heißt
__Raumladungszone__ (oder Sperrschicht). Die zurückgebliebenen festen Ladungen bauen ein **inneres elektrisches
Feld** auf, das weiterer Diffusion entgegenwirkt.

Es stellt sich ein Gleichgewicht ein: Der __Diffusionsstrom__ (Träger wollen sich ausbreiten) und der vom Feld
getriebene __Driftstrom__ (es schiebt sie zurück) heben sich gerade auf. Die zugehörige Spannung über der
Raumladungszone ist die __Diffusionsspannung__ $U_\text{D}$ (bei Silizium etwa $0{,}7\,\text{V}$). Dieser pn-Übergang
leitet den Strom bevorzugt in **eine** Richtung — und genau das macht ihn zur __Diode__, dem Thema des nächsten
Abschnitts.

:::grafik
Ein pn-Übergang: links p-Gebiet (viele Löcher $+$), rechts n-Gebiet (viele Elektronen $-$). In der Mitte die
Raumladungszone mit ortsfesten Ladungen (negative Akzeptorrümpfe links, positive Donatorrümpfe rechts) und einem
Feldpfeil von n nach p. Darüber die Beschriftung Diffusionsspannung $U_\text{D} \approx 0{,}7\,\text{V}$ (Si).
:::

:::kern
Im __Bändermodell__ entscheidet die __Bandlücke__ $E_\text{g}$ zwischen Valenz- und Leitungsband über Leiter
(Überlapp), Halbleiter ($\approx 1\,\text{eV}$) und Isolator ($>3\,\text{eV}$). Wärme hebt Elektronen über die
Lücke und erzeugt __Elektron-Loch-Paare__ (__Eigenleitung__); das __Loch__ wirkt als positiver Ladungsträger.
Durch __Dotierung__ stellt man die Leitfähigkeit ein: __n__ (fünfwertige __Donatoren__ → freie Elektronen),
__p__ (dreiwertige __Akzeptoren__ → Löcher). Am __pn-Übergang__ bildet Diffusion und Rekombination eine
__Raumladungszone__ mit innerem Feld und der __Diffusionsspannung__ $U_\text{D}$ (Si $\approx 0{,}7\,\text{V}$) —
die Grundlage der Diode.
:::

Aus diesem einseitig leitenden Übergang wird das erste Halbleiterbauelement: die __Diode__. Wie ihre Kennlinie
aussieht und warum sie in einer Richtung sperrt, klärt der nächste Abschnitt.
