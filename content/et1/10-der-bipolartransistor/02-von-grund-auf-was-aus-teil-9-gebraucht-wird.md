---
title: Von Grund auf: Was aus Kapitel 9 gebraucht wird
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
order: 1200200
summary: Wie eine kleine Spannung einen großen Strom durch eine gesperrte Diode steuert
tags: Löcher, pn-Übergang, Raumladungszone, Durchlassrichtung, Diffusion, Rekombination
lang: de
---

In n-dotiertem Silizium sind Elektronen frei beweglich, in p-dotiertem __Löcher__, fehlende Elektronen, die sich wie positive Ladungen bewegen. An der Grenze beider Gebiete, dem __pn-Übergang__, entsteht die __Raumladungszone__: ein Streifen fast ohne freie Träger, in dem ortsfeste Ionen ein elektrisches Feld vom n- zum p-Gebiet erzeugen. Dieses Feld wirkt als Barriere für die Mehrheitsträger jeder Seite. Plus am p-Gebiet senkt sie, die Diode leitet in __Durchlassrichtung__. Plus am n-Gebiet hebt sie, die Diode sperrt. __Diffusion__ ist die Bewegung von Teilchen vom dichten zum dünnen Ort, __Rekombination__ das Zusammentreffen eines Elektrons mit einem Loch, bei dem beide als freie Träger verschwinden. Die Diode folgt für $U\gg U_T$ der Gleichung $I=I_\mathrm{S}\,\mathrm{e}^{U/U_T}$, und im Arbeitspunkt rechnet man mit der Tangente an ihre Kennlinie.

::::formelsammlung
**Diodengleichung**

$$I=I_\mathrm{S}\,\mathrm{e}^{U/U_T}$$

Strom einer Diode in Durchlassrichtung für $U\gg U_T$; $I_\mathrm{S}$ ist der Sättigungssperrstrom, $U_T$ die Temperaturspannung, rund 26 mV bei 300 K. Im Arbeitspunkt rechnet man mit der Tangente an diese Kennlinie.
::::

::::lernkarten
:::karte zusammenhang Löcher
Warum zählen Löcher in p-dotiertem Silizium als bewegliche Ladungsträger, obwohl sie nur fehlende Elektronen sind?
---
Die fehlenden Elektronen bewegen sich wie positive Ladungen. Im p-Gebiet sind sie deshalb die Mehrheitsträger, so wie die frei beweglichen Elektronen im n-Gebiet.
--- falsch
Sie sind Atomrümpfe, die ihr Elektron verloren haben und als positive Ionen durch den Kristall wandern. Im p-Gebiet tragen sie deshalb den ganzen Strom.
--- falsch
Sie bewegen sich wie negative Ladungen, weil an ihrer Stelle ein Elektron fehlt. Im p-Gebiet laufen sie deshalb in dieselbe Richtung wie die Elektronen im n-Gebiet.
--- falsch
Sie zählen nur mit, solange eine Spannung anliegt. Ohne Spannung füllen die Elektronen der Nachbaratome alle Lücken, und das p-Gebiet hat dann keine freien Ladungsträger mehr.
:::
:::karte zusammenhang Raumladungszone am pn-Übergang
Warum wirkt die Raumladungszone am pn-Übergang als Barriere für die Mehrheitsträger beider Seiten?
---
In ihr erzeugen ortsfeste Ionen ein elektrisches Feld vom n- zum p-Gebiet. Es drängt Elektronen zurück ins n-Gebiet und Löcher zurück ins p-Gebiet, also jeweils die Mehrheitsträger.
--- falsch
In ihr sammeln sich besonders viele freie Träger, die sich gegenseitig im Weg stehen. Je mehr Elektronen und Löcher dort liegen, desto schwerer kommt ein weiterer Träger hindurch.
--- falsch
In ihr erzeugen ortsfeste Ionen ein Feld vom p- zum n-Gebiet. Es zieht die Elektronen ins p-Gebiet hinüber und hält nur die Löcher zurück, die Barriere wirkt also nur für eine Sorte.
--- falsch
In ihr fehlen die Atome des Kristalls, sodass dort kein Strom fließen kann. Die Zone ist deshalb für alle Ladungsträger undurchlässig, unabhängig von einer angelegten Spannung.
:::
:::karte begriff Durchlassrichtung
Was bedeutet Durchlassrichtung bei einem pn-Übergang, und wie muss die Spannung dafür gepolt sein?
---
Die Polung, in der die Diode leitet: Plus am p-Gebiet senkt die Barriere der Raumladungszone, und die Mehrheitsträger können sie überqueren. Plus am n-Gebiet hebt sie, die Diode sperrt.
--- falsch
Die Polung, in der die Diode leitet: Plus am n-Gebiet senkt die Barriere der Raumladungszone, weil die Elektronen dann zum Pluspol gezogen werden. Plus am p-Gebiet hebt sie, die Diode sperrt.
--- falsch
Die Richtung, in der die Elektronen durch die Diode laufen, gleich wie die Spannung gepolt ist. Die Barriere der Raumladungszone ändert sich dabei nicht, nur die Zahl der Träger wächst.
--- falsch
Die Polung, in der die Raumladungszone am breitesten ist. Plus am p-Gebiet verbreitert sie, und das starke Feld darin zieht die Ladungsträger schneller über die Grenze.
:::
:::karte zusammenhang Diffusion
Wohin bewegen sich Teilchen durch Diffusion, wenn ihre Dichte an einem Ort hoch und an einem anderen niedrig ist?
---
Vom dichten zum dünnen Ort. Dafür braucht es kein elektrisches Feld, nur einen Unterschied der Dichte.
--- falsch
Vom dünnen zum dichten Ort, weil sich gleiche Teilchen gegenseitig anziehen. Dafür braucht es kein Feld, nur einen Unterschied der Dichte.
--- falsch
Vom dichten zum dünnen Ort, aber nur, solange ein elektrisches Feld sie in diese Richtung treibt. Ohne Feld bleiben die Teilchen stehen.
--- falsch
Gar nicht: Ein Unterschied der Dichte allein bewegt keine Teilchen. Diffusion nennt man die Bewegung im Feld der Raumladungszone.
:::
:::karte zusammenhang Rekombination
Was passiert bei der Rekombination mit dem Elektron und dem Loch, die zusammentreffen?
---
Das Elektron füllt das Loch. Beide verschwinden dabei als freie Träger und können keinen Strom mehr tragen.
--- falsch
Das Elektron springt in das Loch und lässt dabei ein neues Loch zurück. Die Zahl der freien Träger bleibt deshalb gleich.
--- falsch
Elektron und Loch stoßen sich ab und laufen in entgegengesetzte Richtungen weiter. Dabei verdoppelt sich ihr Beitrag zum Strom.
--- falsch
Elektron und Loch bilden ein neues Paar freier Träger. So entstehen bei jeder Rekombination zusätzliche Ladungsträger.
:::
:::karte formel Diodengleichung
Wie hängt der Strom einer Diode in Durchlassrichtung von ihrer Spannung ab, und wann gilt diese einfache Form?
---
$I=I_\mathrm{S}\,\mathrm{e}^{U/U_T}$ für $U\gg U_T$, mit dem Sättigungssperrstrom $I_\mathrm{S}$ und der Temperaturspannung $U_T$, rund 26 mV bei 300 K.
--- falsch
$I=I_\mathrm{S}\,\mathrm{e}^{U_T/U}$ für $U\gg U_T$, mit dem Sättigungssperrstrom $I_\mathrm{S}$ und der Temperaturspannung $U_T$, rund 26 mV bei 300 K.
--- falsch
$I=I_\mathrm{S}\,U/U_T$ für $U\gg U_T$: Der Strom wächst linear mit der Spannung, die Steigung ist $I_\mathrm{S}/U_T$, rund 26 mV bei 300 K.
--- falsch
$I=I_\mathrm{S}\,\mathrm{e}^{U/U_T}$ für $U\ll U_T$, also nur für sehr kleine Spannungen; oberhalb von $U_T$ ist der Strom konstant gleich $I_\mathrm{S}$.
:::
::::
