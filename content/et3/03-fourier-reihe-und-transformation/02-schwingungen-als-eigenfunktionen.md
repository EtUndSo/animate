---
title: Stufe 1: Schwingungen als Eigenfunktionen
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3230200
summary: Von den Bausteinen e pt werden jetzt nur die reinen Schwingungen benutzt.
tags: Frequenzgang
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Von den Bausteinen $\mathrm{e}^{pt}$ werden jetzt nur die reinen Schwingungen benutzt. Diese Stufe zeigt, was ein LTI-System mit ihnen macht.
:::

Für rein imaginäres $p=\mathrm{j}2\pi f$ wird der Baustein zur Schwingung mit konstanter Amplitude:

$$\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft).$$

Wie jeder Baustein ist sie eine Eigenfunktion jedes LTI-Systems (Verzögern ist Multiplizieren mit $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$):

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft},\qquad H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t. \tag{1.1}$$

$H(f)$ heißt __Frequenzgang__ oder Übertragungsfunktion. Sein Betrag sagt, wie stark die Schwingung der Frequenz $f$ verstärkt oder geschwächt wird, seine Phase, wie weit sie verschoben wird. Zwei Systeme in Kette multiplizieren nacheinander: $H(f)=H_1(f)H_2(f)$. Wo die Laplace-Transformierte $H(p)$ auf der imaginären Achse existiert, ist $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$.

⁠**Kurz gesagt:** Der Frequenzgang ist die Zahl, mit der ein LTI-System eine reine Schwingung multipliziert.

::::kurzfassung
Die Fourier-Beschreibung benutzt von den Bausteinen $\mathrm{e}^{pt}$ nur die reinen Schwingungen. Ein LTI-System ändert eine solche Schwingung nicht in ihrer Form, es multipliziert sie nur mit einer komplexen Zahl.

Für rein imaginäres $p=\mathrm{j}2\pi f$ wird der Baustein zur Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft)$. Ihre Amplitude ist konstant, sie wächst weder, noch klingt sie ab. Sie ist eine __Eigenfunktion__ jedes LTI-Systems mit der Impulsantwort $h(t)$: Am Ausgang erscheint dieselbe Funktion, nur mit einem Faktor.

$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft},\qquad H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

Der Faktor $H(f)$ heißt __Frequenzgang__ oder Übertragungsfunktion; er existiert, wenn das Integral konvergiert. Sein Betrag sagt, wie stark die Schwingung der Frequenz $f$ verstärkt oder geschwächt wird, seine Phase, wie weit sie verschoben wird. Zwei Systeme in Kette ergeben $H(f)=H_1(f)H_2(f)$. Wo die Laplace-Transformierte $H(p)$ auf der imaginären Achse existiert, ist $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$.

Der Grund: Die Faltung setzt den Ausgang aus verzögerten, gewichteten Kopien des Eingangs zusammen. Eine Verzögerung um $\tau$ macht aus der Schwingung dieselbe Schwingung mal $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$. Jede Kopie ist also die ursprüngliche Schwingung mal einer Zahl, und die mit $h$ gewichtete Summe dieser Zahlen ist $H(f)$.

Falle: Ein reeller Kosinus ist im Allgemeinen keine Eigenfunktion. Verschiebt das System seine Phase, ist der verschobene Kosinus kein Vielfaches des ursprünglichen. Man rechnet deshalb mit $\mathrm{e}^{\mathrm{j}2\pi ft}$ und setzt den Kosinus aus zwei solchen Schwingungen zusammen.
::::

::::formelsammlung
**Reine Schwingung**

$$\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft)$$

Baustein $\mathrm{e}^{pt}$ mit rein imaginärem $p=\mathrm{j}2\pi f$; $f$ reelle Frequenz. Die Amplitude ist konstant, die Schwingung wächst weder, noch klingt sie ab.

**Schwingung als Eigenfunktion**

$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}$$

Für jedes LTI-System mit der Impulsantwort $h(t)$, dessen Frequenzgang existiert. Grund: Verzögern um $\tau$ ist Multiplizieren mit $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$.

**Frequenzgang (Übertragungsfunktion)**

$$H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t$$

Sofern das Integral existiert. Betrag von $H(f)$: Verstärkung oder Schwächung der Schwingung der Frequenz $f$; Phase von $H(f)$: ihre Verschiebung.

**Kettenschaltung**

$$H(f)=H_1(f)H_2(f)$$

Zwei LTI-Systeme hintereinander multiplizieren ihre Frequenzgänge.

**Zusammenhang mit der Laplace-Transformierten**

$$H(f)=H(p)|_{p=\mathrm{j}2\pi f}$$

Nur wo die Laplace-Transformierte $H(p)$ auf der imaginären Achse existiert, die imaginäre Achse also im Konvergenzbereich liegt.
::::

::::lernkarten
:::karte formel Reine Schwingung
Welche Funktion wird aus dem Baustein $\mathrm{e}^{pt}$, wenn $p=\mathrm{j}2\pi f$ rein imaginär ist, und wie verhält sich ihre Amplitude mit der Zeit?
---
Die Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft)$ mit der reellen Frequenz $f$. Ihre Amplitude ist konstant: Sie wächst weder, noch klingt sie ab.
--- falsch
Die Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft)$ mit der reellen Frequenz $f$. Ihre Amplitude wächst mit der Zeit, und zwar umso schneller, je höher die Frequenz $f$ ist.
--- falsch
Die reelle Schwingung $\cos(2\pi ft)$, denn bei rein imaginärem $p$ fällt der Imaginärteil des Bausteins weg. Ihre Amplitude ist konstant, sie klingt weder ab, noch wächst sie.
--- falsch
Die gedämpfte Schwingung $\mathrm{e}^{-2\pi ft}\cos(2\pi ft)$, denn das $\mathrm{j}$ im Exponenten sorgt für die Drehung und das $f$ für das Abklingen. Für $f>0$ klingt sie mit der Zeit ab.
:::
:::karte zusammenhang Eigenfunktion
Warum ist die reine Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ eine Eigenfunktion jedes LTI-Systems, dessen Frequenzgang existiert?
---
Das System setzt den Ausgang aus verzögerten, mit $h$ gewichteten Kopien des Eingangs zusammen. Verzögern um $\tau$ ist Multiplizieren mit $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$, jede Kopie ist also die Schwingung mal einer Zahl. Die gewichtete Summe dieser Zahlen ist $H(f)$.
--- falsch
Weil ihre Amplitude konstant ist und ein LTI-System nur die Amplitude eines Signals ändern kann, nicht seine Phase. Jede verzögerte Kopie ist deshalb dieselbe Schwingung, und der Ausgang ist die Schwingung mal der Fläche von $h$.
--- falsch
Weil ein LTI-System eine Schwingung nur differenziert und die Ableitung von $\mathrm{e}^{\mathrm{j}2\pi ft}$ wieder dieselbe Funktion ist. Verzögerte Kopien kommen dabei gar nicht vor; der Faktor $H(f)$ ist deshalb stets $\mathrm{j}2\pi f$.
--- falsch
Verzögern um $\tau$ ist Addieren der Konstanten $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$. Jede verzögerte Kopie ist also die Schwingung plus eine Zahl, und diese Zahlen heben sich in der gewichteten Summe gegenseitig auf, sodass ein Vielfaches der Schwingung übrig bleibt.
:::
:::karte formel Frequenzgang aus der Impulsantwort
Wie berechnet man den Frequenzgang $H(f)$ eines LTI-Systems aus seiner Impulsantwort $h(t)$, und was geben Betrag und Phase von $H(f)$ an?
---
$H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t$, sofern das Integral existiert. Der Betrag sagt, wie stark die Schwingung der Frequenz $f$ verstärkt oder geschwächt wird, die Phase, wie weit sie verschoben wird.
--- falsch
$H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} t$, sofern das Integral existiert. Der Betrag sagt, wie stark die Schwingung der Frequenz $f$ verstärkt oder geschwächt wird, die Phase, wie weit sie verschoben wird.
--- falsch
$H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t$, sofern das Integral existiert. Die Phase sagt, wie stark die Schwingung der Frequenz $f$ verstärkt oder geschwächt wird, der Betrag, um welche Zeit sie verzögert wird.
--- falsch
$H(f)=h(1/f)$, also der Wert der Impulsantwort nach einer Periode der Schwingung. Der Betrag sagt, wie stark die Schwingung der Frequenz $f$ verstärkt wird, die Phase, wie weit sie verschoben wird.
:::
:::karte zusammenhang Frequenzgang
Was passiert mit einer reinen Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$, wenn sie durch ein LTI-System mit dem Frequenzgang $H(f)$ läuft?
---
Sie kommt mit derselben Frequenz und Form heraus, nur multipliziert mit der komplexen Zahl $H(f)$: $\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}$. Der Betrag von $H(f)$ ändert ihre Amplitude, die Phase von $H(f)$ verschiebt sie.
--- falsch
Sie kommt mit derselben Form heraus, aber mit der Frequenz $H(f)\cdot f$, denn das System multipliziert die Frequenz mit $H(f)$. Amplitude und Phase bleiben dabei unverändert, solange das System linear ist.
--- falsch
Sie kommt mit derselben Frequenz heraus, aber zu ihr wird die Zahl $H(f)$ addiert: Am Ausgang steht $\mathrm{e}^{\mathrm{j}2\pi ft}+H(f)$. Der Betrag von $H(f)$ verschiebt das Signal nach oben, seine Phase nach rechts.
--- falsch
Sie kommt als Summe vieler Schwingungen heraus, deren Frequenzen um $f$ herum verteilt sind. $H(f)$ gibt an, wie breit diese Verteilung ist; nur bei einem Betrag von 1 bleibt die Frequenz scharf.
:::
:::karte formel Kettenschaltung
Welchen Frequenzgang haben zwei LTI-Systeme mit den Frequenzgängen $H_1(f)$ und $H_2(f)$ in Kette, und warum?
---
$H(f)=H_1(f)H_2(f)$. Die Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ ist Eigenfunktion beider Systeme: Das erste multipliziert sie mit $H_1(f)$, das zweite das Ergebnis mit $H_2(f)$.
--- falsch
$H(f)=H_1(f)+H_2(f)$. Die Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ ist Eigenfunktion beider Systeme, und ihre Beiträge überlagern sich am Ausgang, weil beide Systeme linear sind.
--- falsch
$H(f)=H_1(f)*H_2(f)$, die Faltung der Frequenzgänge. Denn in Kette werden die Impulsantworten gefaltet, und was im Zeitbereich gefaltet wird, wird auch im Frequenzbereich gefaltet.
--- falsch
$H(f)=H_1(f)H_2(f)$, aber nur, wenn beide Systeme denselben Frequenzgang haben. Sonst ist die Schwingung nach dem ersten System keine Eigenfunktion des zweiten mehr.
:::
:::karte formel Frequenzgang aus der Laplace-Transformierten
Wann erhält man den Frequenzgang $H(f)$ durch Einsetzen aus der Laplace-Transformierten $H(p)$, und was setzt man dabei ein?
---
Dort, wo $H(p)$ auf der imaginären Achse existiert, die imaginäre Achse also im Konvergenzbereich liegt. Dann ist $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$.
--- falsch
Immer, denn $H(p)$ ist für jedes $p$ erklärt. Man setzt $p=\mathrm{j}2\pi f$ ein und erhält $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$, auch wenn der Konvergenzbereich die imaginäre Achse nicht enthält.
--- falsch
Dort, wo $H(p)$ auf der reellen Achse existiert, die reelle Achse also im Konvergenzbereich liegt. Dann ist $H(f)=H(p)|_{p=2\pi f}$, denn die Frequenz ist eine reelle Größe.
--- falsch
Dort, wo $H(p)$ auf der imaginären Achse existiert. Dann ist $H(f)=H(p)|_{p=\mathrm{j} f}$, denn der Imaginärteil von $p$ ist unmittelbar die Frequenz $f$ selbst.
:::
::::
