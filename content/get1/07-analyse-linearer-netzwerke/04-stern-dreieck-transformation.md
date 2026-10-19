---
title: Stern-Dreieck-Transformation
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70200
summary: Wie man drei Widerstände in Stern- und Dreiecksform ineinander umrechnet und damit Schaltungen auflöst, die sich mit Reihe und Parallel allein hartnäckig verweigern – etwa die Brückenschaltung.
tags: Stern-Dreieck, Transformation, Kennelly, Brückenschaltung, Ersatzwiderstand
---

:::konzept
Manche Schaltungen lassen sich partout nicht in reine Reihen- und Parallelgruppen zerlegen — das klassische
Beispiel ist die **Brückenschaltung**. Hier hilft ein Formwechsel: Drei Widerstände, die als **Stern**
(drei Arme an einem gemeinsamen Punkt) verschaltet sind, lassen sich durch ein gleichwertiges **Dreieck** (drei
Widerstände im Ring) ersetzen — und umgekehrt. Nach dieser einen Umformung tauchen plötzlich wieder einfache
Reihen- und Parallelschaltungen auf, und der Rest ist Routine.
:::

**Worum es geht:** Reihe, Parallel und die Teilerregeln reichen für die meisten Netze. Wo sie versagen, braucht
man die __Stern-Dreieck-Transformation__ (nach Kennelly). Wir sehen, wann sie nötig ist und mit welchen Formeln
man in beide Richtungen umrechnet.

## Wann man sie braucht

In einer __Brückenschaltung__ sind fünf Widerstände so verschaltet, dass kein Paar rein in Reihe oder rein
parallel liegt — der „Querwiderstand" in der Mitte verhindert das. Mit Reihen- und Parallelregeln kommt man
nicht weiter. Die Idee: Man greift sich drei der Widerstände heraus, die einen Stern (oder ein Dreieck) bilden,
und wandelt sie in die jeweils andere Form um. Dadurch wird der blockierende Querzweig „aufgelöst", und es
entstehen wieder zusammenfassbare Reihen- und Parallelgruppen.

:::grafik
Links eine Sternschaltung: drei Widerstände $R_1, R_2, R_3$, die von den Klemmen A, B, C zu einem gemeinsamen
Mittelpunkt laufen. Rechts die gleichwertige Dreieckschaltung: drei Widerstände $R_{AB}, R_{BC}, R_{CA}$ direkt
zwischen den Klemmen. Ein Doppelpfeil „gleichwertig an A, B, C" verbindet beide.
:::

## Dreieck → Stern

Ist das Dreieck gegeben ($R_{AB}, R_{BC}, R_{CA}$) und man sucht den gleichwertigen Stern, gilt für jeden
Sternwiderstand: **Produkt der beiden anliegenden Dreieckswiderstände, geteilt durch die Summe aller drei.** Mit
der Abkürzung $\Sigma = R_{AB} + R_{BC} + R_{CA}$:

$$R_1 = \frac{R_{AB}\cdot R_{CA}}{\Sigma}, \qquad R_2 = \frac{R_{AB}\cdot R_{BC}}{\Sigma}, \qquad R_3 = \frac{R_{BC}\cdot R_{CA}}{\Sigma}.$$

- __$R_1, R_2, R_3$__: die __Sternwiderstände__ an den Klemmen A, B, C.
- __$R_{AB}, R_{BC}, R_{CA}$__: die __Dreieckswiderstände__ zwischen den Klemmen.
- __$\Sigma$__: die __Summe__ aller drei Dreieckswiderstände.

Merkregel: Der Sternwiderstand an einer Klemme bekommt im Zähler gerade die beiden Dreieckswiderstände, die an
**dieser** Klemme zusammentreffen.

## Stern → Dreieck

Umgekehrt, vom Stern zum Dreieck, lautet die Regel: **Summe der paarweisen Produkte der Sternwiderstände,
geteilt durch den jeweils gegenüberliegenden Sternwiderstand.** Mit $P = R_1 R_2 + R_2 R_3 + R_3 R_1$:

$$R_{AB} = \frac{P}{R_3}, \qquad R_{BC} = \frac{P}{R_1}, \qquad R_{CA} = \frac{P}{R_2}.$$

- __$R_{AB}, R_{BC}, R_{CA}$__: die gesuchten __Dreieckswiderstände__.
- __$P$__: die __Summe der Paarprodukte__ der Sternwiderstände.
- Der Nenner ist jeweils der Sternwiderstand an der **gegenüberliegenden** Klemme (bei $R_{AB}$ also $R_3$ an
  Klemme C).

Beide Formelsätze folgen aus derselben Forderung: Zwischen je zwei Klemmen muss der Widerstand in beiden
Schaltungen gleich sein. Setzt man diese drei Klemmen-zu-Klemmen-Widerstände paarweise gleich, ergibt das
Gleichungssystem genau die obigen Beziehungen.

:::grafik
Zwei beschriftete Umrechnungs-Kacheln nebeneinander: links „Dreieck → Stern" mit der Merkregel „anliegende
Produkte / Summe", rechts „Stern → Dreieck" mit „Paarprodukte / gegenüberliegender". Jeweils eine der Formeln
exemplarisch hervorgehoben.
:::

## Der symmetrische Sonderfall

Sind alle drei Dreieckswiderstände gleich groß ($R_{AB} = R_{BC} = R_{CA} = R_\triangle$), werden auch alle
Sternwiderstände gleich, und zwar

$$R_\star = \frac{R_\triangle}{3}.$$

Der Stern hat dann genau ein Drittel des Dreieckswerts. Dieser hübsche Spezialfall taucht oft bei symmetrischen
Netzen auf — etwa beim berühmten Widerstandswürfel — und spart dort viel Rechnerei.

:::grafik
Ein symmetrisches Dreieck mit drei gleichen $R_\triangle$ und daneben der zugehörige Stern mit drei gleichen
$R_\triangle/3$, verbunden mit „symmetrisch: Stern = Drittel des Dreiecks".
:::

:::kern
Die __Stern-Dreieck-Transformation__ löst Netze, die sich mit Reihe und Parallel nicht zerlegen lassen (z. B.
die __Brückenschaltung__). __Dreieck → Stern:__ jeder Sternwiderstand = Produkt der beiden anliegenden
Dreieckswiderstände / Summe aller drei. __Stern → Dreieck:__ jeder Dreieckswiderstand = Summe der Paarprodukte
der Sternwiderstände / gegenüberliegender Sternwiderstand. Beide folgen aus der Gleichheit der
Klemmen-zu-Klemmen-Widerstände. Symmetrisch gilt $R_\star = R_\triangle/3$.
:::

Mit allen Analysewerkzeugen zur Hand bleibt eine letzte, praktisch wichtige Frage: Wie überträgt man die
**größte Leistung** von einer Quelle auf einen Verbraucher? Das ist die __Leistungsanpassung__.
