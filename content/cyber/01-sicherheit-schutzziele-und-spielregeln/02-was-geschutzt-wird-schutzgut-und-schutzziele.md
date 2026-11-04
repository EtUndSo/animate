---
title: Was geschützt wird: Schutzgut und Schutzziele
pfad: Informatik / Cybersecurity / Sicherheit, Schutzziele und Spielregeln
order: 6110200
summary: „Sicher“ bedeutet für sich allein nichts.
tags: Dienst, Schutzgut, Verfügungsberechtigter, berechtigt, unbefugt, Schutzziel, CIA-Triade, Vertraulichkeit
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
„Sicher“ bedeutet für sich allein nichts. Dieser Abschnitt klärt, *was* geschützt werden soll, *wer* damit umgehen darf und *welche Eigenschaften* dabei erhalten bleiben sollen.
:::

### Das Schutzgut

<span class="anker" id="stufe-1-1"></span>

Wer eine Wohnung absichert, denkt zuerst an das, was darin wertvoll ist: Bargeld, Ausweise, den Laptop, vielleicht ein Erbstück. Erst danach entscheidet er über Schloss, Alarmanlage oder Versicherung. Bei Rechnern und Netzen ist es genauso: Bevor man über Schutz redet, muss feststehen, was geschützt werden soll.

Mit *System* ist in diesem Kapitel alles gemeint, was Informationen speichert, verarbeitet oder überträgt: ein einzelnes Gerät, ein Programm, ein Netz oder eine ganze Organisation mit ihren Rechnern. Ein __Dienst__ ist eine Leistung, die ein System für andere erbringt, zum Beispiel eine Überweisung beim Online-Banking oder das Regeln der Raumtemperatur.

:::definition Definition 1.1 (Schutzgut)
<span class="anker" id="satz-1-1"></span>

Ein __Schutzgut__ ist alles, was für jemanden Wert hat und deshalb geschützt werden soll. Schutzgüter sind vor allem Informationen und Dienste, außerdem Geräte, Geld und der gute Ruf einer Person oder Organisation.
:::

Im Englischen heißt das Schutzgut *asset*.

⁠**Beispiel: ein vernetztes Thermostat.** Ein Heizungsthermostat, das sich über das heimische Funknetz (WLAN) per App bedienen lässt, hat mindestens vier Schutzgüter:

<ul>

<li>

den *Temperaturverlauf*: Er verrät, wann jemand zu Hause ist und wann die Wohnung leer steht;

</li>

<li>

die *Steuerfunktion*: Wer sie bedient, kann im Winter die Heizung abschalten;

</li>

<li>

die *Zugangsdaten zum WLAN*, die im Gerät gespeichert sind: Wer sie ausliest, kommt in das ganze Heimnetz;

</li>

<li>

das *Gerät selbst*, das 80 € gekostet hat.

</li>

</ul>

Das Gerät ist das billigste der vier Schutzgüter. Die Informationen und der Dienst, die daran hängen, sind mehr wert.

⁠**Kurz gesagt:** Sicherheit ist immer Schutz *von etwas*; das Schutzgut legt fest, wovon.

### Berechtigte und Unbefugte

<span class="anker" id="stufe-1-2"></span>

Fast jede Frage der Sicherheit lautet am Ende: Darf diese Person das? Dafür braucht man Wörter für die, die dürfen, und für die, die nicht dürfen.

Ein Haus zeigt das Prinzip. Die Bewohner haben einen Schlüssel. Die Nachbarin, die während des Urlaubs die Blumen gießt, bekommt ihn für eine Woche. Ein Schlosser könnte die Tür jederzeit öffnen, er darf es aber nur, wenn die Bewohner ihn beauftragen. Ob jemand eine Tür öffnen *kann*, sagt also nichts darüber, ob er es *darf*. Das entscheiden die Bewohner.

:::definition Definition 1.2 (Verfügungsberechtigter, berechtigt, unbefugt)
<span class="anker" id="satz-1-2"></span>

Wer über ein Schutzgut entscheiden darf, heißt sein __Verfügungsberechtigter__. Meist ist das der Eigentümer der Information oder der Betreiber des Dienstes. Er legt fest, wer welche Handlung mit dem Schutzgut ausführen darf.

Wer eine bestimmte Handlung ausführen darf, ist für diese Handlung __berechtigt__. Wer sie ohne diese Erlaubnis ausführt, handelt __unbefugt__.
:::

Eine Berechtigung bezieht sich immer auf eine bestimmte Handlung. Wer ein Dokument lesen darf, darf es deshalb noch nicht ändern. Und wer eine Handlung technisch ausführen kann, ist dadurch nicht berechtigt.

⁠**Beispiel: ein Girokonto.**

<ul>

<li>

Die Kontoinhaberin darf den Kontostand lesen und Überweisungen auftragen.

</li>

<li>

Ihr Bankberater darf den Kontostand lesen, weil er ihn für die Beratung braucht. Eine Überweisung in ihrem Namen darf er nur auf ihren Auftrag hin ausführen.

</li>

<li>

Ein Fremder darf nichts davon. Errät er das Passwort und sieht den Kontostand an, so handelt er unbefugt, obwohl das System ihn hereingelassen hat.

</li>

</ul>

⁠**Kurz gesagt:** Berechtigt ist, wer eine bestimmte Handlung mit dem Schutzgut ausführen darf. Wer es ohne Erlaubnis tut, handelt unbefugt, auch wenn er es technisch kann.

### Schutzziele

<span class="anker" id="stufe-1-3"></span>

Information verhält sich anders als ein Fahrrad. Wird ein Fahrrad gestohlen, ist es weg. Liest jemand heimlich ein Tagebuch, ist es danach noch vollständig da, und trotzdem ist etwas verloren gegangen. Man muss deshalb genauer sagen, *welche Eigenschaft* eines Schutzguts in Gefahr ist.

Ein Brief zeigt die drei wichtigsten Eigenschaften (Abb. [1](#abb-1)). Er ist unterwegs vom Absender zum Empfänger, und drei verschiedene Dinge können ihm zustoßen: Jemand liest ihn mit, jemand ändert ihn ab, oder jemand hält ihn auf. Jedes Mal ist etwas anderes verletzt.

:::abbildung cyber/k1brief 1
Drei Dinge, die einem Brief unterwegs zustoßen können. Liest ihn ein Unbefugter mit, ist die Vertraulichkeit verletzt; ändert er ihn ab, die Integrität; hält er ihn auf, die Verfügbarkeit.
:::

:::definition Definition 1.3 (Schutzziel)
<span class="anker" id="satz-1-3"></span>

Ein __Schutzziel__ ist eine Eigenschaft eines Schutzguts, die gegenüber unbefugten Handlungen und schädlichen Ereignissen erhalten bleiben soll. Die drei grundlegenden Schutzziele sind die Vertraulichkeit, die Integrität und die Verfügbarkeit.
:::

Im Englischen heißen sie *confidentiality*, *integrity* und *availability*. Nach den Anfangsbuchstaben spricht man von der __CIA-Triade__.

⁠**Beispiel:** Beim Tagebuch ist die Vertraulichkeit verletzt, nicht die Integrität: Der Inhalt ist unverändert. Hätte die Leserin eine Seite herausgerissen, wäre zusätzlich die Integrität verletzt.

⁠**Kurz gesagt:** Ein Schutzziel sagt, welche Eigenschaft eines Schutzguts erhalten bleiben soll; die drei grundlegenden sind Vertraulichkeit, Integrität und Verfügbarkeit.

### Vertraulichkeit

<span class="anker" id="stufe-1-4"></span>

Vertraulichkeit beantwortet die Frage: Wer darf etwas *erfahren*? Beim Brief ist es der verschlossene Umschlag, der nur dem Empfänger den Inhalt zeigen soll.

:::definition Definition 1.4 (Vertraulichkeit)
<span class="anker" id="satz-1-4"></span>

__Vertraulichkeit__ heißt: Eine Information wird nur Berechtigten bekannt. Sie ist verletzt, wenn Unbefugte die Information zur Kenntnis nehmen oder weitergeben.
:::

Manchmal ist schon die *Existenz* einer Information vertraulich. Dass ein Unternehmen eine Datei mit dem Namen „Standortschließung 2027“ angelegt hat, verrät unter Umständen mehr als jede Zahl darin. Vertraulichkeit kann sich also auf den Inhalt beziehen, aber auch darauf, ob es etwas überhaupt gibt.

⁠**Beispiele:**

<ul>

<li>

Jemand im selben offenen Funknetz eines Cafés liest unverschlüsselte Nachrichten mit, die ein anderer Gast verschickt.

</li>

<li>

Eine Lehrkraft schickt die Notenliste versehentlich an den ganzen Kurs. Hier gibt es keinen Täter, und trotzdem ist die Vertraulichkeit verletzt: Schutzziele können auch durch Versehen verletzt werden.

</li>

</ul>

⁠**Kurz gesagt:** Vertraulichkeit heißt, nur Berechtigte erfahren die Information.

### Integrität

<span class="anker" id="stufe-1-5"></span>

Eine Information nützt nur, wenn sie stimmt. Ein Kontoauszug mit falschem Betrag ist schlimmer als gar keiner, weil man ihm glaubt. Beim Brief ist es das Siegel auf dem Umschlag: Es hindert niemanden daran, den Brief zu öffnen, aber ein gebrochenes Siegel zeigt dem Empfänger, dass jemand daran war.

:::definition Definition 1.5 (Integrität)
<span class="anker" id="satz-1-5"></span>

__Integrität__ heißt: Informationen und die Funktionen eines Systems sind korrekt und unverfälscht. Unbefugte Änderungen werden verhindert oder wenigstens erkannt.
:::

Die Definition nennt zwei Dinge. Integrität betrifft Daten, also zum Beispiel den Betrag einer Überweisung. Sie betrifft aber auch Funktionen: Ein Thermostat, das „21 °C“ anzeigt, aber auf 30 °C heizt, hat seine Integrität verloren, obwohl keine gespeicherte Zahl falsch ist. Die zweite Hälfte des letzten Satzes ist ebenso wichtig: Wie beim Siegel genügt es oft schon, eine Änderung sicher zu *erkennen*.

⁠**Beispiel:** Auf dem Weg von der Bank-App zur Bank wird in einer Überweisung über 250 € die Nummer des Empfängerkontos ausgetauscht. Der Betrag stimmt, der Empfänger nicht: Die Integrität der Überweisung ist verletzt, und das Geld landet beim Täter.

⁠**Kurz gesagt:** Integrität heißt, Informationen und Funktionen sind unverfälscht, und unbefugte Änderungen fallen auf.

### Verfügbarkeit

<span class="anker" id="stufe-1-6"></span>

Was nützt das sicherste Konto, wenn man an sein Geld nicht herankommt? Beim Brief ist Verfügbarkeit die Frage, ob er rechtzeitig ankommt.

:::definition Definition 1.6 (Verfügbarkeit)
<span class="anker" id="satz-1-6"></span>

__Verfügbarkeit__ heißt: Berechtigte können Informationen und Dienste nutzen, wann und wie es vorgesehen ist. Sie ist verletzt, wenn Berechtigte dabei behindert werden.
:::

⁠**Beispiele:**

<ul>

<li>

Ein Onlineshop wird mit Millionen sinnloser Anfragen überschüttet und ist stundenlang nicht erreichbar. Die Waren und die Daten sind unverändert, aber kein Kunde kann bestellen.

</li>

<li>

Eine __Erpressungssoftware__ (englisch *ransomware*) verschlüsselt die Dateien eines Opfers, macht sie also mit einem nur den Tätern bekannten Schlüssel unlesbar, und verlangt Geld für den Schlüssel. Damit ist zuerst die Verfügbarkeit verletzt. Streng genommen auch die Integrität, denn die Dateien wurden verändert.

</li>

</ul>

Gegen den Verlust der Verfügbarkeit hilft vor allem eine __Sicherungskopie__ (englisch *backup*): eine zweite Kopie der Daten, die getrennt aufbewahrt wird und aus der man den alten Stand zurückholen kann. Erpressungssoftware ist in Deutschland die größte Bedrohung für Unternehmen. Das Bundesamt für Sicherheit in der Informationstechnik (BSI) berichtet für den Zeitraum von Mitte 2024 bis Mitte 2025 von 950 polizeilich angezeigten Fällen, und in 72 % davon hatten die Täter die Daten vorher kopiert und drohten, sie zu veröffentlichen. Dann ist zusätzlich die Vertraulichkeit verletzt.

⁠**Kurz gesagt:** Verfügbarkeit heißt, Berechtigte kommen an ihre Informationen und Dienste, wenn sie sie brauchen.

:::hintergrund Warum gerade diese drei Schutzziele?
Mit einer Information kann ein Unbefugter im Kern dreierlei anstellen, das den Berechtigten schadet: Er kann sie *erfahren*, er kann sie *verändern*, oder er kann verhindern, dass die Berechtigten sie *nutzen*. Jede dieser drei Handlungen verletzt genau eines der drei Schutzziele. Deshalb taugen die drei als Raster, mit dem man ein Schutzgut systematisch abklopft: Was passiert, wenn es bekannt wird? Was, wenn es verfälscht wird? Was, wenn es fehlt?

Die drei Ziele sind unabhängig voneinander, und eine Maßnahme für das eine hilft dem anderen oft nicht. Eine Verschlüsselung, die Mitlesen verhindert, schützt nicht davor, dass jemand den Server lahmlegt. Eine Sicherungskopie, mit der man nach einem Ausfall weiterarbeiten kann, verhindert keinen Datendiebstahl, im Gegenteil: Sie ist eine zweite Kopie, die ebenfalls gestohlen werden kann. Wer nur an eines der Ziele denkt, übersieht deshalb leicht die anderen. Auch der Satz „Ich habe nichts zu verbergen“ greift aus diesem Grund zu kurz: Er betrifft höchstens die Vertraulichkeit. Dass niemand das eigene Konto verfälscht oder den eigenen Rechner lahmlegt, will jeder.

Das Raster ist bewährt, aber kein Naturgesetz. Viele Fachleute ergänzen weitere Ziele, weil die drei manche Fragen nicht klar genug trennen.
:::

### Authentizität

<span class="anker" id="stufe-1-7"></span>

Eine Nachricht kann vollständig, unverändert und pünktlich ankommen und trotzdem gefährlich sein: wenn sie gar nicht von dem stammt, der als Absender draufsteht.

:::definition Definition 1.7 (Authentizität)
<span class="anker" id="satz-1-7"></span>

__Authentizität__ (Echtheit) heißt: Eine Information stammt tatsächlich von dem, der als Urheber angegeben ist, und ein Kommunikationspartner ist tatsächlich der, für den er sich ausgibt.
:::

Manche Lehrbücher zählen die Echtheit der Herkunft zur Integrität und sprechen dann von Herkunftsintegrität. Wer die Authentizität als eigenes Ziel nennt, meint dieselbe Eigenschaft.

⁠**Beispiel:** Eine E-Mail trägt als Absender „Prüfungsamt“ und fordert dazu auf, sich über einen Link mit Benutzername und Passwort anzumelden, „damit die Anmeldung zur Prüfung nicht verfällt“. Der Link führt auf eine nachgemachte Seite eines Fremden. Eine solche gefälschte Nachricht, die zur Herausgabe von Zugangsdaten verleiten soll, heißt __Phishing__. Verletzt ist die Authentizität der E-Mail. Gibt das Opfer sein Passwort ein, folgt daraus eine Verletzung der Vertraulichkeit.

⁠**Kurz gesagt:** Authentizität heißt, der angegebene Absender ist der echte.

### Verbindlichkeit

<span class="anker" id="stufe-1-8"></span>

Im Geschäftsleben reicht es nicht, dass eine Handlung echt war. Man muss es später auch *beweisen* können, notfalls gegen den Willen dessen, der gehandelt hat.

:::definition Definition 1.8 (Verbindlichkeit)
<span class="anker" id="satz-1-8"></span>

__Verbindlichkeit__, auch Zurechenbarkeit genannt, heißt: Eine Handlung lässt sich nachträglich nachweisbar einer bestimmten Person zuordnen, sodass diese sie nicht glaubhaft abstreiten kann.
:::

Englisch spricht man von *non-repudiation*, wörtlich „Nicht-Abstreitbarkeit“.

⁠**Beispiel:** Ein Kunde bestreitet, in einem Onlineshop einen Fernseher für 900 € bestellt zu haben. Hat der Shop nur gespeichert, dass sich jemand mit seinem Passwort angemeldet hat, steht Aussage gegen Aussage: Das Passwort könnte auch ein anderer gekannt haben. Musste der Kunde die Bestellung zusätzlich auf seinem Handy bestätigen und hat der Shop das mit Uhrzeit festgehalten, ist die Bestellung ihm deutlich besser zuzurechnen.

⁠**Kurz gesagt:** Verbindlichkeit heißt, eine Handlung lässt sich später beweisbar ihrem Urheber zuordnen.

### Schutzbedarf

<span class="anker" id="stufe-1-9"></span>

Nicht jedes Schutzgut braucht denselben Schutz. Ein Einkaufszettel und ein Reisepass sind beide Papier, aber nur einen der beiden schließt man weg. Um Schutz sinnvoll zu verteilen, muss man deshalb für jedes Schutzgut abschätzen, wie schlimm eine Verletzung wäre.

:::definition Definition 1.9 (Schutzbedarf)
<span class="anker" id="satz-1-9"></span>

Der __Schutzbedarf__ eines Schutzguts gibt für jedes Schutzziel an, wie schwer der Schaden wäre, wenn dieses Schutzziel verletzt würde. Das BSI unterscheidet drei Stufen:

<ul>

<li>

⁠**normal**: Die Schadensauswirkungen sind „begrenzt und überschaubar“;

</li>

<li>

⁠**hoch**: Sie „können beträchtlich sein“;

</li>

<li>

⁠**sehr hoch**: Sie „können ein existentiell bedrohliches, katastrophales Ausmaß erreichen“.

</li>

</ul>
:::

Der Schutzbedarf wird für jedes Schutzgut und jedes Schutzziel getrennt bestimmt. Dasselbe Schutzgut kann für die Vertraulichkeit einen hohen und für die Verfügbarkeit einen normalen Schutzbedarf haben.

⁠**Beispiel:** Tabelle [1](#tab-1) bestimmt den Schutzbedarf des vernetzten Thermostats aus dem ersten Unterabschnitt für eine Familie in einer Mietwohnung. Das Gerät selbst fehlt, weil sein Verlust nur 80 € kostet: normaler Schutzbedarf in allen drei Spalten.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Schutzbedarf des vernetzten Thermostats. V: Vertraulichkeit, I: Integrität, Vf: Verfügbarkeit.

| Schutzgut | V | I | Vf | Begründung |
|---|---|---|---|---|
| Temperaturverlauf | hoch | normal | normal | Er verrät, wann die Wohnung leer steht, und erleichtert damit einen Einbruch. Ein falscher oder fehlender Verlauf schadet kaum. |
| Steuerfunktion | normal | hoch | hoch | Wer sie verfälscht oder lahmlegt, kann im Winter die Heizung abschalten; gefrorene Wasserleitungen kosten schnell mehrere tausend Euro. |
| WLAN-Zugangsdaten | hoch | normal | normal | Wer sie kennt, ist im ganzen Heimnetz und erreicht auch Laptop und Handy. |

⁠**Kurz gesagt:** Der Schutzbedarf sagt für jedes Schutzgut und jedes Schutzziel, wie schwer eine Verletzung wöge, in den Stufen normal, hoch und sehr hoch.

:::hintergrund Woran man die Stufe festmacht, und warum der höchste Wert zählt
Ob ein Schaden „beträchtlich“ ist, hängt davon ab, wen er trifft. Damit die Einstufung nicht beliebig wird, fragt man reihum nach den Arten von Schaden, die eine Verletzung auslösen kann. Das BSI nennt dafür sechs Schadensszenarien: ein Verstoß gegen Gesetze, Vorschriften oder Verträge; eine Beeinträchtigung des Rechts, selbst über die eigenen persönlichen Daten zu bestimmen; eine Gefahr für Leib und Leben; eine Beeinträchtigung der eigentlichen Aufgabe, etwa der Produktion; eine Rufschädigung; finanzielle Folgen. Für jedes Szenario schätzt man die Stufe, und die höchste gibt den Ausschlag.

Dasselbe Maximum gilt, wenn ein System mehrere Schutzgüter trägt: Liegen auf einem Rechner der Speiseplan der Kantine und die Gehaltsdaten, hat der Rechner für die Vertraulichkeit den Schutzbedarf der Gehaltsdaten. Der Grund ist einfach: Ein Angreifer, der in den Rechner kommt, kommt an beides. Der Schutz eines Systems muss sich deshalb nach dem wertvollsten Schutzgut richten, das darauf liegt, nicht nach dem Durchschnitt.
:::

:::aufgabe Aufgabe 1 ★ Welches Schutzziel ist verletzt?
<span class="anker" id="aufg-1"></span>

Nenne für jeden Vorfall alle verletzten Schutzziele (Vertraulichkeit, Integrität, Verfügbarkeit, Authentizität, Verbindlichkeit) und begründe jedes in einem Satz.

<ol class="al">

<li>

Ein Mitarbeiter lässt ein Notebook mit unverschlüsselten Kundendaten im Zug liegen.

</li>

<li>

In einer Bestellung wird unterwegs die Liefermenge von 10 auf 100 geändert.

</li>

<li>

Ein Angreifer überlastet das Anmeldesystem einer Hochschule in der Woche der Prüfungsanmeldung.

</li>

<li>

Eine Erpressungssoftware verschlüsselt die Patientenakten einer Arztpraxis; die Täter drohen, die Akten zu veröffentlichen.

</li>

<li>

Eine SMS „von der Paketzustellung“ führt auf eine gefälschte Seite, die eine Zahlung von 1,99 € verlangt.

</li>

<li>

Ein Vermieter behauptet, eine Kündigung per E-Mail nie erhalten zu haben, und die Mieterin kann nicht nachweisen, dass sie sie geschickt hat.

</li>

</ol>

:::loesung
(a) *Vertraulichkeit*: Wer das Notebook findet, kann die Kundendaten lesen; sie sind nicht verschlüsselt. Zusätzlich ist für den Mitarbeiter die *Verfügbarkeit* seiner Daten verletzt, falls es keine Kopie gibt. Ob die Vertraulichkeit tatsächlich verletzt *wird*, hängt davon ab, wer das Gerät findet; bedroht ist sie sofort.

(b) *Integrität*: Die Bestellung wurde unbefugt verändert. Fällt die Änderung nicht auf, folgen falsche Lieferung und falsche Rechnung.

(c) *Verfügbarkeit*: Die Studierenden können sich nicht anmelden. Gespeicherte Daten werden weder bekannt noch verändert.

(d) *Verfügbarkeit*, weil die Praxis nicht mehr an die Akten kommt; *Integrität*, weil die Dateien verändert wurden; *Vertraulichkeit*, weil die Täter die Akten kopiert haben. Für Patientenakten ist der Schutzbedarf bei der Vertraulichkeit sehr hoch.

(e) *Authentizität*: Die Nachricht stammt nicht von der Paketzustellung. Wer zahlt und seine Kartendaten eingibt, verliert zusätzlich deren Vertraulichkeit.

(f) *Verbindlichkeit*: Ob die Kündigung abgeschickt und empfangen wurde, lässt sich nicht nachweisen. Eine Empfangsbestätigung oder ein Einschreiben hätte sie verbindlich gemacht.
:::
:::

:::aufgabe Aufgabe 2 ★★ Dein eigenes Gerät, Teil 1: Schutzgüter und Schutzbedarf
<span class="anker" id="aufg-2"></span>

Wähle ein Gerät oder einen Dienst, den du selbst benutzt oder gebaut hast, zum Beispiel deinen Router, ein Mikrocontroller-Projekt mit WLAN, dein Smartphone oder dein Konto bei einem Onlineshop. Arbeite auf Papier.

<ol class="al">

<li>

Nenne mindestens drei Schutzgüter. Denke auch an Informationen, die nicht auf dem Gerät liegen, aber über das Gerät erreichbar sind.

</li>

<li>

Wer ist Verfügungsberechtigter? Wer ist wofür berechtigt? Nenne mindestens drei Personen oder Gruppen mit ihren Handlungen.

</li>

<li>

Bestimme den Schutzbedarf für jedes Schutzgut und jedes der drei grundlegenden Schutzziele in einer Tabelle wie Tabelle [1](#tab-1). Begründe jede Stufe „hoch“ oder „sehr hoch“ mit einem Schadensszenario.

</li>

</ol>

Bewahre das Blatt auf; Aufgabe [5](risiko-angreifermodell-und-angriffsflache.html#aufg-5) baut darauf auf.

:::loesung
Jede gut begründete Lösung ist richtig; hier eine Musterlösung für einen *Router im Heimnetz einer Wohngemeinschaft*.

(a) Schutzgüter: die Verwaltungsoberfläche mit allen Einstellungen (Steuerfunktion); das WLAN-Passwort; der gesamte Datenverkehr, der durch den Router läuft; der Internetanschluss selbst (ein Dienst, der für alle wichtig ist); die Geräte im Heimnetz, die über den Router erreichbar sind. Die letzten beiden liegen nicht auf dem Router, hängen aber von ihm ab.

(b) Verfügungsberechtigt ist die Person, die den Anschluss gemietet hat, hier etwa die Hauptmieterin. Sie darf die Einstellungen ändern. Die Mitbewohner dürfen das WLAN nutzen, aber nicht die Einstellungen ändern und nicht den Verkehr der anderen einsehen. Gäste dürfen das Gäste-WLAN nutzen. Der Anbieter des Anschlusses darf den Router aus der Ferne aktualisieren, wenn der Vertrag das vorsieht.

(c) Mögliche Tabelle:

| Schutzgut | V | I | Vf | Begründung für „hoch“ |
|---|---|---|---|---|
| Einstellungen | normal | hoch | hoch | Wer sie ändert, kann Verkehr umleiten (Integrität) oder den Anschluss für alle lahmlegen; ohne Internet können drei Bewohner nicht studieren oder arbeiten (Aufgabenerfüllung). |
| WLAN-Passwort | hoch | normal | normal | Mit ihm kommt ein Fremder ins Heimnetz zu allen Geräten (Selbstbestimmung über persönliche Daten). |
| Datenverkehr | hoch | hoch | normal | Er enthält Nachrichten und Anmeldungen aller Bewohner (Selbstbestimmung, finanzielle Folgen). |
:::
:::
