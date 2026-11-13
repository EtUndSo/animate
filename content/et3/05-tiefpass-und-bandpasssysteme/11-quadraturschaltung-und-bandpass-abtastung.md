---
title: Stufe 10: Quadraturschaltung und Bandpass-Abtastung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3251100
summary: Wie gewinnt man die Quadraturkomponenten technisch?
tags: 
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Wie gewinnt man die Quadraturkomponenten technisch? Und wie viele Abtastwerte braucht ein Bandpasssignal?
:::

**Quadraturschaltung.** Multipliziert man ein Bandpasssignal mit $\cos(2\pi f_0t)$ und filtert mit einem Tiefpass, bleibt $\frac12s_{Tr}$. Mit $-\sin(2\pi f_0t)$ bleibt $\frac12s_{Ti}$. Der Grund ist trigonometrisch:

$$s\cos=s_{Tr}\cos^2-s_{Ti}\sin\cos=\tfrac12s_{Tr}+\underbrace{\tfrac12s_{Tr}\cos(4\pi f_0t)-\tfrac12s_{Ti}\sin(4\pi f_0t)}_{\text{bei }2f_0,\text{ vom Tiefpass entfernt}},$$

und ebenso $-s\sin=\frac12s_{Ti}+(\text{Anteile bei }2f_0)$. Voraussetzung ist, dass das Band unterhalb von $2f_0$ endet. Im Tiefpassbereich filtert man dann mit vier Tiefpässen ($h_{Tr}$, $\pm h_{Ti}$) nach [(9.1)](bandpasssignal-durch-bandpasssystem.html#gl-9-1). Am Ausgang moduliert man nach [(8.2)](komplexe-hullkurve-und-quadraturkomponenten.html#gl-8-2) wieder auf den Träger, oder man bildet die Einhüllende $\sqrt{g_{Tr}^2+g_{Ti}^2}$ (Abb. [6](#abb-6)).

:::abbildung et3/k5quadratur 6
Quadraturdemodulator: Er gewinnt aus einem Bandpasssignal die beiden Quadraturkomponenten, also die komplexe Hüllkurve.
:::

**Abtasttheorem für Bandpasssignale.** Ein Bandpasssignal der Bandbreite $\Delta f$ hat, bezogen auf die Mittenfrequenz, Quadraturkomponenten, die Tiefpasssignale bis $\Delta f/2$ sind. Jede lässt sich mit $1/T=\Delta f$ abtasten:

<span class="anker" id="gl-10-1"></span>
$$s(t)=\sum_ns_{Tr}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)-\sum_ns_{Ti}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\sin(2\pi f_0t),\qquad T=\frac{1}{\Delta f}. \tag{10.1}$$

Insgesamt braucht man $2\Delta f$ Werte je Sekunde, so viele wie für ein Tiefpasssignal der Grenzfrequenz $\Delta f$. Es kommt also auf die Bandbreite an, nicht auf die höchste Frequenz.

:::aufgabe Aufgabe 9 ★★ Ein Funksignal abtasten
<span class="anker" id="aufg-9"></span>

Ein Signal belegt das Band von 10,0 bis 10,2 MHz.

<ol class="al">

<li>

Welche Abtastrate bräuchte man nach dem gewöhnlichen Abtasttheorem?

</li>

<li>

Wie viele Abtastwerte je Sekunde genügen mit der Quadraturschaltung insgesamt, und mit welcher Rate wird jeder Zweig abgetastet?

</li>

</ol>

:::loesung
(a) Mindestens $2\cdot10{,}2=20{,}4$ MHz.

(b) $\Delta f=0{,}2$ MHz. Jeder Zweig wird mit 0,2 MHz abgetastet ($T=5$ µ s), zusammen 0,4 MHz, rund fünfzigmal weniger.
:::
:::

::::formelsammlung
**Quadraturschaltung**

$$s\cos=s_{Tr}\cos^2-s_{Ti}\sin\cos=\tfrac12s_{Tr}+\tfrac12s_{Tr}\cos(4\pi f_0t)-\tfrac12s_{Ti}\sin(4\pi f_0t)$$

Nach dem Tiefpass bleibt $\frac12s_{Tr}$, ebenso aus $-s\sin$ der Anteil $\frac12s_{Ti}$; die Anteile bei $2f_0$ entfernt der Tiefpass. Voraussetzung: Das Band endet unterhalb von $2f_0$.

**Einhüllende am Ausgang**

$$\sqrt{g_{Tr}^2+g_{Ti}^2}$$

Nach dem Filtern im Tiefpassbereich mit vier Tiefpässen ($h_{Tr}$, $\pm h_{Ti}$); alternativ moduliert man nach der Quadraturdarstellung wieder auf den Träger.

**Abtasttheorem für Bandpasssignale**

$$s(t)=\sum_ns_{Tr}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)-\sum_ns_{Ti}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\sin(2\pi f_0t),\qquad T=\frac{1}{\Delta f}$$

Bandbreite $\Delta f$, $f_0$ Mittenfrequenz; jede Quadraturkomponente ist ein Tiefpasssignal bis $\Delta f/2$. Insgesamt $2\Delta f$ Werte je Sekunde: Es kommt auf die Bandbreite an, nicht auf die höchste Frequenz.
::::

::::lernkarten
:::karte zusammenhang Quadraturdemodulator
Wie gewinnt eine Quadraturschaltung aus einem Bandpasssignal seine beiden Quadraturkomponenten?
---
Man multipliziert das Signal in einem Zweig mit $\cos(2\pi f_0t)$, im anderen mit $-\sin(2\pi f_0t)$, und filtert beide mit einem Tiefpass. Übrig bleiben $\frac12s_{Tr}$ und $\frac12s_{Ti}$, also die komplexe Hüllkurve.
--- falsch
Man multipliziert das Signal in beiden Zweigen mit $\cos(2\pi f_0t)$ und filtert den einen Zweig mit einem Tiefpass, den anderen mit einem Hochpass. Übrig bleiben $s_{Tr}$ und $s_{Ti}$ in voller Höhe.
--- falsch
Man filtert das Signal mit zwei Bandpässen knapp unter und knapp über $f_0$. Der untere liefert $s_{Tr}$, der obere $s_{Ti}$, weil die beiden Seitenbänder genau den beiden Quadraturkomponenten entsprechen.
--- falsch
Man multipliziert das Signal in einem Zweig mit $\cos(2\pi f_0t)$, im anderen mit $\sin(4\pi f_0t)$, und filtert beide mit einem Tiefpass, der die Anteile bei $f_0$ entfernt und nur die Hüllkurve übrig lässt.
:::
:::karte formel Produkt mit dem Kosinus
Welche Anteile entstehen, wenn man ein Bandpasssignal $s=s_{Tr}\cos-s_{Ti}\sin$ mit $\cos(2\pi f_0t)$ multipliziert?
---
$s\cos=\tfrac12s_{Tr}+\tfrac12s_{Tr}\cos(4\pi f_0t)-\tfrac12s_{Ti}\sin(4\pi f_0t)$: ein Tiefpassanteil $\frac12s_{Tr}$ und Anteile bei $2f_0$, die der Tiefpass entfernt.
--- falsch
$s\cos=s_{Tr}+s_{Tr}\cos(4\pi f_0t)-s_{Ti}\sin(4\pi f_0t)$: Der Tiefpass liefert $s_{Tr}$ in voller Höhe, weil das Quadrat des Kosinus im Mittel gleich 1 ist.
--- falsch
Nach dem Tiefpass bleibt $\frac12s_{Tr}-\frac12s_{Ti}$: Beide Quadraturkomponenten bleiben übrig, weil auch das Produkt aus Sinus und Kosinus des Trägers einen Gleichanteil hat.
--- falsch
$s\cos=\tfrac12s_{Tr}+\tfrac12s_{Tr}\cos(2\pi f_0t)$: Die Störanteile liegen bei $f_0$, weil das Produkt zweier Schwingungen der Frequenz $f_0$ wieder bei $f_0$ schwingt.
:::
:::karte zusammenhang Voraussetzung der Quadraturschaltung
Welche Voraussetzung muss das Band erfüllen, damit der Tiefpass der Quadraturschaltung die Anteile bei $2f_0$ abtrennen kann?
---
Das Band muss unterhalb von $2f_0$ enden. Dann überlappen die Anteile um $2f_0$ nicht mit dem Tiefpassanteil um $f=0$, und der Tiefpass kann sie entfernen.
--- falsch
Das Band muss oberhalb von $2f_0$ beginnen. Sonst liegen Teile des Signals schon vor der Multiplikation im Durchlassbereich des Tiefpasses und verfälschen die Komponenten.
--- falsch
Die Bandbreite muss genau $f_0$ sein. Nur dann fallen die Anteile bei $2f_0$ genau auf die Sperrkante des Tiefpasses, und die beiden Komponenten bleiben unverzerrt.
--- falsch
Es gibt keine Voraussetzung: Die Anteile bei $2f_0$ entfernt der Tiefpass immer, weil $2f_0$ stets höher liegt als jede Frequenz des ursprünglichen Bandes.
:::
:::karte zusammenhang Filtern im Tiefpassbereich
Wie filtert man ein Bandpasssignal, nachdem die Quadraturschaltung es in den Tiefpassbereich gebracht hat, und wie kommt man wieder zurück?
---
Man filtert die Quadraturkomponenten nach $g_T=\frac12s_T*h_T$ mit vier Tiefpässen ($h_{Tr}$, $\pm h_{Ti}$). Am Ausgang moduliert man nach der Quadraturdarstellung wieder auf den Träger oder bildet die Einhüllende $\sqrt{g_{Tr}^2+g_{Ti}^2}$.
--- falsch
Man filtert jede Quadraturkomponente nur mit einem einzigen Tiefpass $h_{Tr}$, weil der Imaginärteil $h_{Ti}$ im Tiefpassbereich keine Rolle spielt. Am Ausgang addiert man die beiden Zweige einfach zu $g_{Tr}+g_{Ti}$.
--- falsch
Man filtert die beiden Komponenten mit zwei Bandpässen bei $f_0$, weil das Filter dieselbe Lage haben muss wie das ursprüngliche System. Am Ausgang ist dann kein Träger mehr nötig, weil die Bandpässe ihn schon enthalten.
--- falsch
Man filtert die Komponenten mit vier Tiefpässen ($h_{Tr}$, $\pm h_{Ti}$), muss aber zuvor einen Träger bei $2f_0$ hinzufügen, weil die Faltung sonst die Hüllkurve verliert; die Einhüllende ist dann $g_{Tr}+g_{Ti}$.
:::
:::karte formel Abtasttheorem für Bandpasssignale
Wie lässt sich ein Bandpasssignal der Bandbreite $\Delta f$ aus Abtastwerten seiner Quadraturkomponenten zurückgewinnen?
---
$s(t)=\sum_ns_{Tr}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)-\sum_ns_{Ti}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\sin(2\pi f_0t)$ mit $T=\frac{1}{\Delta f}$: Jede Komponente ist ein Tiefpasssignal bis $\Delta f/2$.
--- falsch
$s(t)=\sum_ns(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)$ mit $T=\frac{1}{2f_0+\Delta f}$: Man tastet das Bandpasssignal selbst ab, mit der doppelten höchsten Frequenz wie bei jedem Signal; die Quadraturkomponenten braucht man dafür nicht.
--- falsch
$s(t)=\sum_ns_{Tr}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)-\sum_ns_{Ti}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\sin(2\pi f_0t)$ mit $T=\frac{1}{2f_0}$: Jede Komponente sitzt auf dem Träger und braucht die doppelte Trägerfrequenz.
--- falsch
$s(t)=\sum_n\bigl[s_{Tr}(nT)+s_{Ti}(nT)\bigr]\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)$ mit $T=\frac{1}{\Delta f}$: Man addiert die beiden Komponenten vorher und braucht so nur eine einzige Folge von Abtastwerten.
:::
:::karte zusammenhang Bandbreite statt höchster Frequenz
Wie viele Abtastwerte je Sekunde braucht ein Bandpasssignal der Bandbreite $\Delta f$ insgesamt, und worauf kommt es dabei an?
---
Insgesamt $2\Delta f$ Werte je Sekunde, je $\Delta f$ für jede Quadraturkomponente, so viele wie für ein Tiefpasssignal der Grenzfrequenz $\Delta f$. Es kommt auf die Bandbreite an, nicht auf die höchste Frequenz.
--- falsch
Insgesamt doppelt so viele Werte je Sekunde wie die höchste Frequenz des Bandes; die Quadraturschaltung ändert daran nichts, weil die Information des Signals bis zur höchsten Frequenz reicht.
--- falsch
Insgesamt $\Delta f$ Werte je Sekunde, je $\Delta f/2$ für jede Quadraturkomponente; weil sich beide Komponenten die Bandbreite teilen, halbiert sich der Bedarf gegenüber einem Tiefpasssignal.
--- falsch
Insgesamt $4\Delta f$ Werte je Sekunde, je $2\Delta f$ für jede Quadraturkomponente; jede Komponente ist ein Tiefpasssignal bis $\Delta f$ und braucht deshalb die doppelte Rate.
:::
:::karte zusammenhang Ein Funksignal abtasten
Wie stark senkt die Quadraturschaltung die nötige Abtastrate für ein Signal, das das Band von 10,0 bis 10,2 MHz belegt?
---
Nach dem gewöhnlichen Abtasttheorem bräuchte man mindestens 20,4 MHz. Mit der Quadraturschaltung tastet man jeden Zweig mit $\Delta f=0{,}2$ MHz ab, zusammen 0,4 MHz, rund fünfzigmal weniger.
--- falsch
Nach dem gewöhnlichen Abtasttheorem bräuchte man nur 0,4 MHz, die doppelte Bandbreite. Die Quadraturschaltung spart nichts, sie verteilt diese Rate nur auf zwei Zweige mit je 0,2 MHz.
--- falsch
Nach dem gewöhnlichen Abtasttheorem bräuchte man 20,4 MHz. Mit der Quadraturschaltung tastet man jeden Zweig mit der Mittenfrequenz 10,1 MHz ab, zusammen also 20,2 MHz, kaum weniger.
--- falsch
Nach dem gewöhnlichen Abtasttheorem bräuchte man 20,4 MHz. Mit der Quadraturschaltung genügt je Zweig 0,1 MHz, die halbe Bandbreite, zusammen 0,2 MHz, also rund hundertmal weniger.
:::
::::
