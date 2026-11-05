---
title: Schwachstellen benennen und bewerten
pfad: Informatik / Cybersecurity / Sicherheit, Schutzziele und Spielregeln
order: 6110800
summary: Jeden Tag werden weltweit über hundert neue Schwachstellen bekannt.
tags: CVE, National Vulnerability Database, CWE, Common Vulnerability Scoring System, Vektor, Ausnutzbarkeit, Auswirkung, Patch
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Jeden Tag werden weltweit über hundert neue Schwachstellen bekannt. Dieser Abschnitt zeigt, wie man sie eindeutig benennt, nach ihrer Art ordnet, ihre Schwere in einer Zahl ausdrückt und welchen Weg eine Schwachstelle von ihrer Entstehung bis zur Behebung nimmt.
:::

### CVE: der Name einer Schwachstelle

<span class="anker" id="stufe-7-1"></span>

Das BSI zählte für den Zeitraum von Mitte 2024 bis Mitte 2025 im Schnitt 119 neu bekannt gewordene Schwachstellen pro Tag, hochgerechnet über 43 000 im Jahr. Hersteller, Behörden und Sicherheitsfirmen müssen sich über jede davon verständigen können. Dafür braucht jede Schwachstelle einen eindeutigen Namen.

:::definition Definition 7.1 (CVE)
<span class="anker" id="satz-7-1"></span>

__CVE__ (englisch *Common Vulnerabilities and Exposures*) ist ein weltweites Verzeichnis öffentlich bekannter Schwachstellen. Jede Schwachstelle darin erhält eine eindeutige Kennung der Form `CVE-JJJJ-NNNN`: eine Jahreszahl und eine laufende Nummer mit mindestens vier Ziffern.
:::

Betrieben wird das Verzeichnis von der gemeinnützigen Organisation MITRE im Auftrag der US-Behörde CISA. Die Kennungen vergeben viele dazu berechtigte Stellen, darunter große Hersteller und Sicherheitsbehörden. Die Jahreszahl gibt in der Regel an, in welchem Jahr die Kennung reserviert wurde, nicht, wann der Fehler entstand.

Zu jeder Kennung gibt es einen Eintrag mit einer kurzen Beschreibung, den betroffenen Produkten und Versionen und Verweisen auf weitere Informationen. Die US-Behörde NIST ergänzt die Einträge in ihrer __National Vulnerability Database__ (NVD) um Bewertungen und Einordnungen; ihre Seiten sind frei zugänglich und auf Englisch.

⁠**Beispiel:** Im Dezember 2021 wurde eine Schwachstelle in Log4j bekannt, einem sehr weit verbreiteten Baustein, mit dem Programme Protokolldateien schreiben. Sie erhielt die Kennung `CVE-2021-44228` und wurde unter dem Namen Log4Shell bekannt. Über die Kennung findet man sie in jeder Datenbank, jeder Herstellerwarnung und jedem Prüfwerkzeug wieder.

⁠**Kurz gesagt:** Eine CVE-Kennung ist der weltweit eindeutige Name einer bekannten Schwachstelle.

:::hintergrund Warum ein gemeinsamer Name so wichtig ist
Bis Ende der 1990er-Jahre führte jede Sicherheitsfirma und jede Datenbank ihre eigenen Namen. Ein Fehler in einem Dateifreigabedienst von 1991 hieß in einem Prüfwerkzeug „nfs-guess“, in einem anderen „NFS file handle guessing check“. Wer zwei Werkzeuge benutzte, konnte nicht erkennen, ob beide dieselbe Schwachstelle meldeten oder zwei verschiedene, und wer wissen wollte, wie viele Lücken ein System hatte, bekam je nach Werkzeug eine andere Zahl. Zwei Mitarbeiter von MITRE schlugen 1999 deshalb eine einzige öffentliche Liste vor, die jeder Schwachstelle einen eindeutigen Namen gibt. Daraus wurde CVE.

Der Nutzen ist derselbe wie bei Bauteilbezeichnungen in der Elektrotechnik: Erst ein gemeinsamer Name macht Informationen aus verschiedenen Quellen vergleichbar. Ein Prüfwerkzeug meldet eine CVE-Kennung, die Herstellerwarnung nennt dieselbe Kennung und den Patch dazu, und die Liste aktiv ausgenutzter Lücken einer Behörde verwendet sie ebenfalls.
:::

### CWE: die Art des Fehlers

<span class="anker" id="stufe-7-2"></span>

Eine CVE-Kennung benennt einen Einzelfall: genau diesen Fehler in genau diesem Produkt. Viele Einzelfälle haben aber dieselbe Ursache, und wer Fehler vermeiden will, muss die Ursachen kennen.

:::definition Definition 7.2 (CWE)
<span class="anker" id="satz-7-2"></span>

__CWE__ (englisch *Common Weakness Enumeration*) ist ein öffentlicher Katalog von *Arten* von Schwachstellen in Software und Hardware. Jede Art hat eine Nummer der Form `CWE-N` und einen Namen.
:::

CVE und CWE beantworten verschiedene Fragen: CVE sagt, *welcher* Fehler in *welchem* Produkt steckt; CWE sagt, *was für eine Art* von Fehler es ist. Ein CVE-Eintrag verweist deshalb meist auf eine oder mehrere CWE-Nummern.

⁠**Beispiele** aus diesem Kapitel:

<ul>

<li>

Das Kundenportal, das bei der Rechnungsnummer nicht prüft, wem die Rechnung gehört, hat eine Schwachstelle der Art CWE-639, „Authorization Bypass Through User-Controlled Key“: Umgehen der Rechteprüfung über einen Schlüssel, den der Nutzer selbst angibt.

</li>

<li>

Der Router mit dem Werkspasswort hat eine Schwachstelle der Art CWE-1393, „Use of Default Password“.

</li>

<li>

Die Geldautomaten haben eine Schwachstelle der Art CWE-367, „Time-of-check Time-of-use (TOCTOU) Race Condition“.

</li>

</ul>

Jedes Jahr veröffentlichen MITRE und CISA eine Liste der 25 gefährlichsten Arten, gemessen an den gemeldeten Schwachstellen. In der Liste von 2025 belegen drei Arten von Fehlern in Webanwendungen die ersten Plätze; auf Platz vier steht CWE-862, „Missing Authorization“, die fehlende Rechteprüfung, also ein Verstoß gegen die lückenlose Prüfung aus Abschnitt [5](sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5).

⁠**Kurz gesagt:** CVE benennt den Einzelfall, CWE die Art des Fehlers.

:::hintergrund Warum man die Art eines Fehlers kennen will
Ein Patch behebt einen Einzelfall. Kennt man dagegen die Art des Fehlers, kann man seine Ursache abstellen und damit alle künftigen Fälle derselben Art auf einmal verhindern. Beim Kundenportal hieße das: nicht nur die Rechnungsseite reparieren, sondern eine einzige zentrale Stelle bauen, die bei jedem Abruf prüft, wem die Daten gehören. Dann kann auch die nächste Seite, die jemand ergänzt, den Fehler CWE-639 nicht mehr haben; das ist die kleine vertrauenswürdige Basis aus Abschnitt [6](sicherheitsprinzipien-systeme-robust-entwerfen.html#stufe-6). Deshalb lohnt es sich, Schwachstellen nach ihrer Art zu zählen: Häufen sich Fehler einer Art, beseitigt man ihre Ursache an der Wurzel, statt jeden Einzelfall nachzubessern.
:::

### CVSS: die Schwere

<span class="anker" id="stufe-7-3"></span>

Wer 119 neue Schwachstellen am Tag vor sich hat, muss entscheiden, welche er zuerst behebt. Dafür braucht man ein Maß für die Schwere, das jeder auf dieselbe Weise bestimmt.

:::definition Definition 7.3 (CVSS)
<span class="anker" id="satz-7-3"></span>

Das __Common Vulnerability Scoring System__ (CVSS) bewertet die Schwere einer Schwachstelle mit einer Zahl von 0,0 bis 10,0. Die Zahl wird nach festen Regeln aus einem __Vektor__ berechnet, einer Liste von Merkmalen der Schwachstelle, die man unabhängig voneinander einstuft. Aus der Zahl folgt eine Stufe: keine (0,0), niedrig (0,1 bis 3,9), mittel (4,0 bis 6,9), hoch (7,0 bis 8,9) und kritisch (9,0 bis 10,0).
:::

Herausgeber ist FIRST, ein internationaler Verband von Teams, die auf Sicherheitsvorfälle reagieren. Die aktuelle Version 4.0 gibt es seit November 2023. In älteren Einträgen wie dem zu Log4Shell steht noch die Version 3.1, deren Merkmale Tabelle [2](#tab-2) zeigt.

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Die Merkmale des CVSS-Vektors in Version 3.1 (Basis-Metriken). Die Kürzel stehen so im Vektor.

| Merkmal | Kürzel | mögliche Werte |
|---|---|---|
| Angriffsweg | AV | N: über das Netz, aus der Ferne; A: aus einem benachbarten Netz, etwa demselben Funknetz; L: nur am Gerät selbst, mit einem Zugang dort; P: nur mit den Händen am Gerät |
| Angriffskomplexität | AC | L: keine besonderen Bedingungen; H: der Angriff gelingt nur unter Bedingungen, die der Angreifer nicht steuern kann |
| benötigte Rechte | PR | N: keine; L: die eines gewöhnlichen Nutzers; H: weitreichende Rechte |
| Mitwirkung eines Nutzers | UI | N: nicht nötig; R: ein Nutzer muss etwas tun, etwa einen Link anklicken |
| Wirkungsbereich | S | U: Die Folgen bleiben in der verwundbaren Komponente; C: Sie reichen darüber hinaus in andere Teile des Systems |
| Folgen für Vertraulichkeit, Integrität, Verfügbarkeit | C, I, A | je H: hoch; L: gering; N: keine |

⁠**Beispiel: Log4Shell.** Die NVD gibt für CVE-2021-44228 den Vektor

`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`

und die Bewertung 10,0, kritisch, an. Gelesen heißt das: Ein Angreifer erreicht die Lücke aus der Ferne über das Netz (AV:N), ohne besondere Bedingungen (AC:L), ohne jede Anmeldung (PR:N) und ohne dass ein Nutzer mitwirken muss (UI:N). Die Folgen reichen über den verwundbaren Baustein hinaus in das ganze Programm, das ihn benutzt (S:C), und Vertraulichkeit, Integrität und Verfügbarkeit sind jeweils schwer betroffen (C:H, I:H, A:H). Schlimmer geht es in diesem Schema nicht.

In Version 4.0 sind einige Merkmale neu geordnet. Es gibt ein zusätzliches Merkmal für Voraussetzungen des Angriffs (AT), die Mitwirkung eines Nutzers wird feiner unterschieden (keine, passiv, aktiv), und statt des Wirkungsbereichs S werden die Folgen getrennt für das verwundbare System (VC, VI, VA) und für nachfolgende Systeme (SC, SI, SA) angegeben.

⁠**Kurz gesagt:** CVSS fasst die Merkmale einer Schwachstelle in einem Vektor zusammen und macht daraus eine Zahl von 0 bis 10, die ihre Schwere angibt.

### Wie aus dem Vektor die Zahl wird

<span class="anker" id="stufe-7-4"></span>

Damit zwei Fachleute für denselben Vektor dieselbe Zahl bekommen, ist die Rechnung fest vorgeschrieben. In Version 3.1 ist sie eine Formel, die man mit dem Taschenrechner nachvollziehen kann.

Die Zahl setzt sich aus zwei Teilen zusammen. Der eine sagt, wie leicht ein Angreifer die Lücke erreicht und ausnutzt; jedes Hindernis, das er dabei überwinden muss, macht diesen Teil kleiner. Der andere sagt, wie schwer die Folgen für die drei grundlegenden Schutzziele sind.

:::definition Definition 7.4 (Basisbewertung nach CVSS 3.1)
<span class="anker" id="satz-7-4"></span>

Jeder Wert im Vektor steht für eine Zahl:

<ul>

<li>

AV: N 0,85; A 0,62; L 0,55; P 0,2. AC: L 0,77; H 0,44. UI: N 0,85; R 0,62.

</li>

<li>

PR: N 0,85; L 0,62 (bei S:C 0,68); H 0,27 (bei S:C 0,5).

</li>

<li>

C, I, A: H 0,56; L 0,22; N 0.

</li>

</ul>

Die __Ausnutzbarkeit__ ist das Produkt

<span class="anker" id="gl-7-1"></span>
$$E=8{,}22\cdot\mathrm{AV}\cdot\mathrm{AC}\cdot\mathrm{PR}\cdot\mathrm{UI}. \tag{7.1}$$

Die __Auswirkung__ geht von der Größe $\mathrm{ISS}=1-(1-C)(1-I)(1-A)$ aus und ist

<span class="anker" id="gl-7-2"></span>
$$W=6{,}42\cdot\mathrm{ISS}\quad\text{(bei S:U)},\qquad W=7{,}52\,(\mathrm{ISS}-0{,}029)-3{,}25\,(\mathrm{ISS}-0{,}02)^{15}\quad\text{(bei S:C)}. \tag{7.2}$$

Ist $W\le0$, so ist die Bewertung 0. Sonst ist sie $\min(W+E,\,10)$ bei S:U und $\min\bigl(1{,}08\,(W+E),\,10\bigr)$ bei S:C, jeweils aufgerundet auf eine Nachkommastelle.
:::

Die Abkürzung ISS steht für *impact sub-score*. Die Zahlen $8{,}22$, $6{,}42$, $7{,}52$ und die übrigen Konstanten sind festgelegt, nicht hergeleitet: Sie stehen so in der Beschreibung des Verfahrens, und man schlägt sie dort nach.

⁠**Rechenbeispiel: Log4Shell.** Für `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H` ist $\mathrm{ISS}=0{,}9148$, die Auswirkung $W=6{,}0477$ und die Ausnutzbarkeit $E=3{,}8870$. Mit S:C ergibt sich $1{,}08\cdot(W+E)=10{,}73$, begrenzt auf $10{,}0$ (Abb. [15](#abb-15)).

:::abbildung cyber/k1rcvss 15
Die Basisbewertung von Log4Shell nach CVSS 3.1: Die Auswirkung $W$ beginnt mit dem Produkt der drei Faktoren $1-0{,}56=0{,}44$, die Ausnutzbarkeit $E$ ist ein Produkt aus fünf Faktoren. Die Summe, mal $1{,}08$, liegt über $10$ und wird auf $10{,}0$ begrenzt.
:::

⁠**Kurz gesagt:** In Version 3.1 ist die Bewertung eine Formel: das Produkt der Hindernisse als Ausnutzbarkeit, dazu die Auswirkung auf Vertraulichkeit, Integrität und Verfügbarkeit.

:::hintergrund Warum die Formel so gebaut ist
In der Formel stecken zwei Gedanken aus diesem Kapitel. Die Ausnutzbarkeit $E$ ist ein Produkt: Jedes Hindernis für den Angreifer, ob ein weiter Weg, eine nötige Anmeldung oder ein Nutzer, der mitspielen muss, verkleinert sie um einen Faktor, so wie mehrere Verteidigungslinien in Abschnitt [6](sicherheitsprinzipien-systeme-robust-entwerfen.html#stufe-6). Und die Größe ISS hat dieselbe Gestalt wie die Formel [(3.3)](risiko-angreifermodell-und-angriffsflache.html#gl-3-3) für „mindestens eines“: Schon ein einziges schwer getroffenes Schutzziel ergibt $\mathrm{ISS}=1-0{,}44=0{,}56$, zwei ergeben $1-0{,}44^2=0{,}81$, drei $1-0{,}44^3=0{,}91$. Jedes weitere getroffene Ziel erhöht den Wert weniger als das vorige, so wie jede weitere Stelle die Wahrscheinlichkeit für „mindestens eine Schwachstelle“ immer weniger erhöht. Eine Lücke ist also schon schwer, wenn ein einziges Schutzziel schwer getroffen ist.

Version 4.0 verzichtet auf eine geschlossene Formel. Fachleute haben die rund 15 Millionen möglichen Vektoren in 270 Gruppen eingeteilt, deren Vektoren sie für ungefähr gleich schwer halten, und jeder Gruppe einen Wert zugeordnet. Die Bewertung wird aus dieser Tabelle abgelesen und innerhalb der Gruppe durch Interpolation verfeinert. Die Stufen von „keine“ bis „kritisch“ sind gleich geblieben.
:::

:::hintergrund Schwere ist nicht Risiko
FIRST betont selbst, dass die Basisbewertung die *Schwere* einer Schwachstelle misst und nicht allein zur Einschätzung des Risikos dienen soll. Der Grund ist die Formel $R=H\cdot S$ aus Abschnitt [3](risiko-angreifermodell-und-angriffsflache.html#stufe-3). Die Basisbewertung beschreibt die Schwachstelle selbst, gleich, wo sie vorkommt. Sie sagt nichts darüber, wie oft sie tatsächlich ausgenutzt wird, und damit nichts über $H$; und sie sagt nichts darüber, wie wertvoll das betroffene Schutzgut in der eigenen Umgebung ist, also über $S$.

Eine Lücke mit 9,8 in einem Gerät, das nicht mit dem Netz verbunden ist und keine wichtigen Daten hält, kann ein kleineres Risiko sein als eine Lücke mit 6,5 im Kundenportal, die gerade weltweit ausgenutzt wird. Deshalb hat CVSS weitere Metrikgruppen für die Bedrohungslage und für die eigene Umgebung, und deshalb führt die US-Behörde CISA eine eigene Liste der Schwachstellen, die nachweislich ausgenutzt werden, den Katalog *Known Exploited Vulnerabilities* (KEV). Wer entscheidet, was er zuerst behebt, schaut auf beides: wie schwer eine Lücke ist und ob sie gerade angegriffen wird.
:::

### Der Lebenszyklus einer Schwachstelle

<span class="anker" id="stufe-7-5"></span>

Eine Schwachstelle hat eine Geschichte: Sie entsteht, wird irgendwann von jemandem entdeckt, und mit etwas Glück wird sie behoben. Wie gefährlich sie ist, hängt davon ab, in welcher Phase dieser Geschichte man sich befindet.

:::definition Definition 7.5 (Patch, Update, Lebenszyklus)
<span class="anker" id="satz-7-5"></span>

Ein __Patch__ ist eine Korrektur, die der Hersteller für eine Schwachstelle bereitstellt. Ein __Update__ ist das Einspielen dieser Korrektur durch den Betreiber des betroffenen Systems. Der __Lebenszyklus__ einer Schwachstelle ist die Folge ihrer Phasen: Der Fehler entsteht, wird entdeckt, dem Hersteller gemeldet, durch einen Patch behoben und veröffentlicht, und schließlich spielen die Betreiber das Update ein.
:::

Abbildung [16](#abb-16) zeigt den Lebenszyklus für den ungünstigen Fall, dass Angreifer die Lücke zuerst finden.

:::abbildung cyber/k1zyklus 16
Der Lebenszyklus einer Schwachstelle im ungünstigen Fall. Rot: Angreifer nutzen die Lücke aus, und es gibt noch keinen Patch. Orange: Der Patch ist veröffentlicht, aber noch nicht eingespielt; jetzt kennen auch alle übrigen Angreifer die Lücke.
:::

Die Phase nach der Veröffentlichung ist besonders gefährlich, obwohl es einen Patch gibt. Mit der Veröffentlichung erfahren alle Angreifer von der Lücke, und viele Systeme sind noch nicht aktualisiert. Eine Schwachstelle, die bekannt ist und für die es einen Patch gibt, der aber noch nicht überall eingespielt ist, nennt man auch __n-day__. Eine Untersuchung von Angriffen aus den Jahren 2008 bis 2011 fand, dass die Zahl der Angriffe auf eine Lücke nach ihrer Veröffentlichung um bis zu fünf Größenordnungen zunahm.

⁠**Beispiel: Log4Shell.** Die Kennung CVE-2021-44228 wurde am 10. Dezember 2021 veröffentlicht. Am selben Tag nahm die US-Behörde CISA die Lücke in ihren Katalog nachweislich ausgenutzter Schwachstellen auf und verpflichtete die Bundesbehörden der USA, sie bis zum 24. Dezember 2021 zu beheben. Behoben ist der Fehler ab Version 2.15.0 des Bausteins und, für ältere Umgebungen, in den Versionen 2.12.2 und 2.3.1. Weil Log4j in unzähligen Programmen steckt, oft ohne dass deren Betreiber es wussten, dauerte es bei vielen Systemen Monate, bis das Update eingespielt war.

⁠**Kurz gesagt:** Eine Schwachstelle durchläuft Entstehung, Entdeckung, Meldung, Patch, Veröffentlichung und Update; nach der Veröffentlichung ist sie allen bekannt, und gefährdet ist jedes System, das das Update noch nicht hat.

:::hintergrund Warum ein Patch die Lücke verrät
Ein Patch ändert das Programm genau an der fehlerhaften Stelle. Vergleicht man die alte und die neue Fassung, sieht man deshalb, wo der Fehler lag, oft schon wenige Tage, manchmal Stunden nach der Veröffentlichung. Ein Angreifer muss die Lücke dann nicht mehr selbst finden; der Patch zeigt sie ihm. Für jedes System, das noch die alte Fassung hat, ist der Patch eine Anleitung zum Angriff.

Daraus folgt die wichtigste Regel des Betriebs: Updates schnell einspielen, besonders für Lücken, die bereits ausgenutzt werden. Das BSI zählt die Ausnutzung bekannter Lücken in schlecht gepflegten Systemen, für die längst ein Patch bereitstand, zu den Hauptbedrohungen in Deutschland.
:::

### Zero-Day

<span class="anker" id="stufe-7-6"></span>

Der gefährlichste Fall ist der, in dem Angreifer eine Lücke kennen und niemand sonst. Dann gibt es keinen Patch, keine Warnung und keine CVE-Kennung.

:::definition Definition 7.6 (Zero-Day)
<span class="anker" id="satz-7-6"></span>

Eine Schwachstelle heißt __Zero-Day__, wenn Angreifer sie kennen oder ausnutzen, bevor der Hersteller einen Patch bereitstellen konnte. Ein Angriff, der eine solche Lücke ausnutzt, heißt Zero-Day-Angriff.
:::

Der Name sagt: Der Hersteller hatte null Tage Zeit, sich vorzubereiten. In Abbildung [16](#abb-16) ist das die rote Phase.

⁠**Beispiel:** Eine Untersuchung von 18 Zero-Day-Angriffen aus den Jahren 2008 bis 2011 ergab, dass sie zwischen 19 Tagen und 30 Monaten unentdeckt blieben, im Median acht Monate. So lange konnten die Angreifer die Lücke benutzen, ohne dass sich jemand dagegen wehren konnte.

Gegen einen Zero-Day hilft kein Update, denn es gibt noch keines. Was dann schützt, sind die Grundsätze aus den Abschnitten [4](richtlinie-und-mechanismus.html#stufe-4) bis [6](sicherheitsprinzipien-systeme-robust-entwerfen.html#stufe-6): Minimale Rechte begrenzen, was der Angreifer nach dem Einbruch tun kann, mehrere Verteidigungslinien zwingen ihn, weitere Hindernisse zu überwinden, und Mechanismen, die erkennen, bemerken ihn auch dann, wenn keiner ihn verhindert hat.

⁠**Kurz gesagt:** Ein Zero-Day ist eine Lücke, die Angreifer ausnutzen, bevor es einen Patch gibt; dagegen helfen nur Grundsätze, die nicht auf einen bekannten Fehler angewiesen sind.

:::aufgabe Aufgabe 12 ★★ Einen CVE-Eintrag lesen
<span class="anker" id="aufg-12"></span>

Öffne im Browser die Seite der NVD zu Log4Shell: [https://nvd.nist.gov/vuln/detail/CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228). Die Beschreibung enthält Fachwörter, die in diesem Kapitel nicht vorkommen; für die Aufgabe brauchst du sie nicht.

<ol class="al">

<li>

Welches Produkt ist betroffen, und welche Versionen nennt die Beschreibung?

</li>

<li>

Suche unter „Metrics“ die Bewertung nach CVSS 3.x. Notiere Vektor und Zahl der Bewertung durch NIST und, falls angegeben, durch den Hersteller. Erkläre jedes Merkmal des Vektors mit Tabelle [2](#tab-2) in eigenen Worten.

</li>

<li>

Welche CWE-Nummern stehen unter „Weakness Enumeration“, und wer hat sie vergeben? Warum kann ein Eintrag mehrere CWE-Nummern haben?

</li>

<li>

Was sagt der Abschnitt zum KEV-Katalog der CISA? Welche der beiden Größen aus $R=H\cdot S$ betrifft diese Angabe?

</li>

<li>

Gibt es eine Bewertung nach CVSS 4.0? Erkläre, warum das bei einem Eintrag aus dem Jahr 2021 zu erwarten ist.

</li>

</ol>

:::loesung
Stand der Seite am 4. November 2026; die Gestaltung der Seite kann sich ändern.

(a) Betroffen ist Apache Log4j2, ein Baustein zum Schreiben von Protokolldateien. Die Beschreibung nennt die Versionen 2.0-beta9 bis 2.15.0, ausgenommen die Korrekturversionen 2.12.2, 2.12.3 und 2.3.1.

(b) NIST gibt nach CVSS 3.1 den Vektor `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H` und die Bewertung 10,0, kritisch, an; der Hersteller, die Apache Software Foundation, hat denselben Vektor und dieselbe Zahl vergeben. Bedeutung: aus der Ferne über das Netz (AV:N), ohne besondere Bedingungen (AC:L), ohne Anmeldung (PR:N), ohne Mitwirkung eines Nutzers (UI:N), Folgen über den Baustein hinaus (S:C), schwere Folgen für Vertraulichkeit, Integrität und Verfügbarkeit (C:H, I:H, A:H). Zusätzlich steht eine ältere Bewertung nach CVSS 2.0 mit 9,3 da.

(c) NIST nennt CWE-917, eine Art von Einschleusen über Ausdrücke, die das Programm auswertet. Der Hersteller nennt CWE-20 (unzureichende Prüfung von Eingaben), CWE-400 (unkontrollierter Verbrauch von Ressourcen) und CWE-502 (Verarbeitung nicht vertrauenswürdiger, serialisierter Daten). Ein Eintrag kann mehrere CWE-Nummern haben, weil ein Fehler oft aus mehreren Ursachen zusammenwirkt und weil verschiedene Stellen ihn verschieden einordnen: Die Nummern beschreiben Arten von Fehlern, und eine einzelne Schwachstelle kann zu mehreren Arten gehören.

(d) Die Lücke wurde am 10. Dezember 2021 in den Katalog der nachweislich ausgenutzten Schwachstellen aufgenommen; die US-Bundesbehörden mussten sie bis zum 24. Dezember 2021 beheben. Die Angabe betrifft die Häufigkeit $H$: Die Lücke wird tatsächlich angegriffen. Den Schaden $S$ kann nur jeder Betreiber für seine eigene Umgebung abschätzen.

(e) Nein. CVSS 4.0 erschien im November 2023, der Eintrag stammt von 2021 und wurde damals nach 3.1 bewertet. Alte Einträge werden in der Regel nicht neu bewertet.
:::
:::

:::aufgabe Aufgabe 13 ★★★ Eine Bewertung selbst berechnen
<span class="anker" id="aufg-13"></span>

Benutze die Formeln und Zahlen aus Unterabschnitt [7.4](#stufe-7-4).

<ol class="al">

<li>

Berechne die Bewertung für `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`. Vergleiche mit Log4Shell: Was ändert der Wirkungsbereich?

</li>

<li>

Dieselbe Schwachstelle sei nur mit den Händen am Gerät ausnutzbar (AV:P). Berechne die Bewertung und die Stufe.

</li>

<li>

Eine Lücke erlaubt es, aus der Ferne ohne Anmeldung vertrauliche Daten mitzulesen, aber nur unter Bedingungen, die der Angreifer nicht steuern kann; Integrität und Verfügbarkeit sind nicht betroffen. Stelle den Vektor auf (S:U) und berechne die Bewertung.

</li>

</ol>

:::loesung
(a) $\mathrm{ISS}=1-0{,}44^3=0{,}9148$. Bei S:U ist $W=6{,}42\cdot0{,}9148=5{,}8731$. $E=8{,}22\cdot0{,}85\cdot0{,}77\cdot0{,}85\cdot0{,}85=3{,}8870$. Summe $9{,}7601$, aufgerundet **9,8**, kritisch. Bei Log4Shell machten der Wirkungsbereich S:C, die andere Auswirkungsformel und der Faktor 1,08 daraus 10,0: Weil die Folgen über die verwundbare Komponente hinausreichen, wird die Lücke als schwerer eingestuft.

(b) Nur $E$ ändert sich: $E=8{,}22\cdot0{,}2\cdot0{,}77\cdot0{,}85\cdot0{,}85=0{,}9146$. Summe $5{,}8731+0{,}9146=6{,}7877$, aufgerundet **6,8**, mittel. Wer die Hand am Gerät haben muss, hat ein großes Hindernis; der Faktor 0,2 statt 0,85 drückt die Bewertung um drei Punkte.

(c) Vektor `AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N`. $\mathrm{ISS}=1-(1-0{,}56)=0{,}56$, $W=6{,}42\cdot0{,}56=3{,}5952$. $E=8{,}22\cdot0{,}85\cdot0{,}44\cdot0{,}85\cdot0{,}85=2{,}2212$. Summe $5{,}8164$, aufgerundet **5,9**, mittel.
:::
:::

:::aufgabe Aufgabe 14 ★ Phasen einer Schwachstelle
<span class="anker" id="aufg-14"></span>

Ein Sicherheitsforscher meldet am 3. März einem Hersteller eine Lücke in einer Kamera. Der Hersteller veröffentlicht 60 Tage später einen Patch, und 30 Tage nach dem Patch erscheinen die Einzelheiten. Ein Jahr später sind laut einer Zählung noch 40 % der Kameras nicht aktualisiert.

<ol class="al">

<li>

An welchen Daten erscheinen Patch und Einzelheiten?

</li>

<li>

War die Lücke ein Zero-Day? Was müsste man wissen, um die Frage sicher zu beantworten?

</li>

<li>

In welcher Phase befinden sich die 40 % der Kameras, und warum ist ihre Lage schlechter als vor der Veröffentlichung?

</li>

</ol>

:::loesung
(a) 3. März plus 60 Tage: Der Patch erscheint am 2. Mai (28 Tage bis Ende März, 30 im April, 2 im Mai). 30 Tage später, am 1. Juni, erscheinen die Einzelheiten.

(b) Aus den Angaben allein lässt sich das nicht sagen. Ein Zero-Day wäre die Lücke, wenn Angreifer sie schon vor dem Patch kannten oder ausnutzten. Man müsste also wissen, ob es vor dem 2. Mai Angriffe gab, etwa aus Spuren auf betroffenen Kameras oder aus Berichten von Sicherheitsfirmen. Dass ein Forscher sie gemeldet hat, schließt das nicht aus.

(c) Sie sind in der Phase „Patch da, nicht eingespielt“. Ihre Lage ist schlechter als vor der Veröffentlichung, weil jetzt jeder Angreifer die Lücke kennt und der Patch zeigt, wo sie liegt. Vorher kannten sie höchstens wenige.
:::
:::
