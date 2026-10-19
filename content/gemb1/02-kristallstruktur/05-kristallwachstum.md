---
title: Kristallwachstum von Silizium
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Kristallstruktur
order: 4020500
summary: Wie aus billigem Quarzsand ein defektfreier, hochreiner Silizium-Einkristall wird – in drei Stufen. Erst Reduktion zu Roh-Silizium (noch 2–4 % Fremdatome), dann der entscheidende Trick der Reinigung über die flüchtige Verbindung Trichlorsilan, und schließlich das Czochralski-Verfahren, bei dem ein Impfkristall die Ordnung in die ganze Schmelze trägt.
tags: Kristallwachstum, Silizium, Trichlorsilan, Siemens-Prozess, Czochralski, Segregation, Reinigung
---

:::grafik
Einstiegs-Animation: Ein dreistufiger „Produktionsstraßen"-Verlauf. (1) Quarzsand wandert in einen glühenden
Lichtbogenofen, heraus kommt grauer Roh-Silizium-Brocken (noch „schmutzig"). (2) Der Brocken wird in ein Gas
verwandelt, das durch eine Destillationskolonne aufsteigt und sich reinigt; unten scheidet sich auf einem
glühenden Stab reines Silizium ab. (3) Ein Impfkristall taucht in eine glühende Schmelze und wird langsam
rotierend herausgezogen — es wächst ein großer, glänzender Einkristall-Barren. Kernbotschaft: Vom Sand zum
perfekten Kristall in drei Stufen, jede löst ein eigenes Reinheits-/Ordnungsproblem.
:::

:::konzept
Silizium ist nach Sauerstoff das zweithäufigste Element der Erdkruste — es steckt als $\text{SiO}_2$ in jedem
Sandkorn. Für ein funktionierendes Bauelement braucht man aber nicht irgendein Silizium, sondern einen **perfekt
geordneten Einkristall** von **extremer Reinheit**: Schon ein Fremdatom auf eine Milliarde Siliziumatome kann die
elektrischen Eigenschaften verändern. Der Weg vom Sand dorthin ist eine der beeindruckendsten Materialleistungen
der Technik und läuft in drei Stufen ab: **Reduktion**, **Reinigung** und **Einkristall-Zucht**. Jede Stufe löst
ein eigenes Problem — und an einer Stelle steckt ein besonders eleganter Trick.
:::

**Worum es geht:** Wir verfolgen den Weg vom $\text{SiO}_2$ zum fertigen Si-Einkristall. Dabei verstehen wir,
*warum* man den Umweg über die gasförmige Verbindung __Trichlorsilan__ geht, und *wie* das
__Czochralski-Verfahren__ aus einem winzigen Impfkristall einen metergroßen Einkristall macht.

## Stufe 1: Roh-Silizium aus dem Lichtbogenofen

Zuerst muss der Sauerstoff aus dem $\text{SiO}_2$ heraus. Das geschieht durch **Reduktion** mit Kohlenstoff
(Koks) im Lichtbogenofen bei sehr hoher Temperatur:

$$\text{SiO}_2 + 2\,\text{C} \;\longrightarrow\; \text{Si} + 2\,\text{CO}.$$

Der Kohlenstoff „reißt" den Sauerstoff an sich (es entsteht Kohlenmonoxid), zurück bleibt elementares Silizium.
Das Ergebnis heißt **metallurgisches Silizium** und ist mit rund **98 %** schon recht rein — enthält aber noch
**2–4 % Fremdatome**. Für die Elektronik ist das katastrophal viel: Es muss noch um etwa den Faktor $10^9$
(eine Milliarde) **reiner** werden.

:::grafik
Ein Lichtbogenofen im Schnitt: oben werden Quarz ($\text{SiO}_2$) und Koks (C) eingefüllt, in der Mitte der
glühende Lichtbogen, unten fließt flüssiges Roh-Silizium ab, Kohlenmonoxid (CO) entweicht nach oben. Die Reaktion
$\text{SiO}_2 + 2\text{C} \to \text{Si} + 2\text{CO}$ steht daneben, mit „98 % Si, aber 2–4 % Fremdatome".
:::

## Stufe 2: Reinigung über Trichlorsilan

Hier kommt der Trick. **Warum reinigt man den festen Brocken nicht direkt?** Weil Verunreinigungen in einem
Festkörper festsitzen und sich kaum heraustrennen lassen. Viel besser lässt sich ein **Gas** reinigen: durch
**Destillation**, die Stoffe nach ihrem Siedepunkt trennt. Die Idee ist deshalb, das feste, schmutzige Silizium
in eine **flüchtige Verbindung** zu verwandeln, diese zu reinigen und dann wieder festes Silizium abzuscheiden.

Dazu lässt man das gemahlene Roh-Silizium bei etwa $300\,^\circ$C mit Chlorwasserstoff reagieren — es entsteht
__Trichlorsilan__ $\text{SiHCl}_3$:

$$\text{Si} + 3\,\text{HCl} \;\longrightarrow\; \text{SiHCl}_3 + \text{H}_2.$$

Der entscheidende Punkt ist der **Siedepunkt** von Trichlorsilan: nur $31{,}8\,^\circ$C. Die Chloride der
Verunreinigungen sieden bei deutlich anderen Temperaturen (z. B. $\text{BCl}_3$ bei $12\,^\circ$C,
$\text{AsCl}_3$ bei $132\,^\circ$C). Durch mehrfache **Destillation** trennt man das $\text{SiHCl}_3$ sauber von
ihnen ab — so entsteht hochreines Trichlorsilan.

:::grafik
Links der Reaktor „Si + 3 HCl → SiHCl₃ + H₂" bei $300\,^\circ$C. Rechts eine Destillationskolonne: eine
Temperaturskala mit eingetragenen Siedepunkten ($\text{BCl}_3$ 12 °C, $\text{SiHCl}_3$ 31,8 °C, $\text{AsCl}_3$
132 °C); ein Pfeil zeigt, wie bei 31,8 °C reines $\text{SiHCl}_3$ abgezogen wird.
:::

Das gereinigte Trichlorsilan wird anschließend im __Siemens-Prozess__ wieder zu festem Silizium zersetzt: Man
leitet es mit Wasserstoff über einen **stromdurchflossenen, glühenden Siliziumstab** ($\approx 1150\,^\circ$C).
Nur an der heißen Staboberfläche zerfällt das Gas und scheidet reines Silizium ab:

$$\text{SiHCl}_3 + \text{H}_2 \;\longrightarrow\; \text{Si} + 3\,\text{HCl}.$$

Das Ergebnis ist zwar hochrein, aber **poly-kristallin** (viele kleine, verschieden orientierte Kristallite). Für
Bauelemente braucht man dagegen einen **Ein**kristall — das leistet erst die dritte Stufe
([pv-manufacturing](https://pv-manufacturing.org/silicon-production/polysilicon-production/)).

:::grafik
Eine Siemens-Glocke: im Inneren ein U-förmiger, rot glühender Si-Stab, umströmt von $\text{SiHCl}_3 + \text{H}_2$;
an der Staboberfläche wächst eine Si-Schicht an (Pfeile). Beschriftung „reines, aber poly-kristallines Silizium",
Nebenprodukt $\text{HCl}$ wird abgeführt.
:::

## Stufe 3: Einkristall-Zucht nach Czochralski

Jetzt fehlt nur noch die **Ordnung**: aus vielen kleinen Kristalliten soll ein einziger großer Einkristall
werden. Beim __Czochralski-Verfahren__ nutzt man einen __Impfkristall__ (Seed), der die gewünschte Orientierung
vorgibt. Der Ablauf:

- Das poly-kristalline Silizium wird **aufgeschmolzen** — knapp über dem Schmelzpunkt von $1414\,^\circ$C, unter
  **Argon-Atmosphäre** (verhindert Oxidation).
- Der **Impfkristall** wird von oben in die Schmelze getaucht. An der Berührstelle erstarren die Atome und
  übernehmen die **Kristallorientierung** des Seeds.
- Seed und Tiegel werden **gegenläufig gedreht** (für gleichmäßige Temperatur) und der Kristall langsam
  **herausgezogen** — an der kühleren Grenzfläche wächst er stetig weiter.

**Das Problem der Versetzungen — und der Dash-Neck.** Beim ersten Kontakt erleidet der Seed einen Thermoschock,
der **Versetzungen** (Gitterfehler) erzeugt. Würden sie in den Kristall hineinwachsen, wäre er nicht perfekt.
Der Trick: Man zieht zuerst **schnell** und erzeugt dabei einen dünnen Hals (__neck__) von nur $\approx 3\,$mm
Durchmesser. In diesem engen Hals „wachsen sich die Versetzungen aus" (sie laufen zur Seite heraus). Erst wenn
der Hals versetzungsfrei ist, zieht man **langsamer** und lässt den Kristall auf den vollen Durchmesser
anwachsen ([US6080237](https://patents.google.com/patent/US6080237), [US5628823](https://patents.google.com/patent/US5628823)).

:::grafik
Der Czochralski-Zieher im Schnitt: Tiegel mit glühender Schmelze ($1414\,^\circ$C, Argon), von oben der
rotierende, gezogene Kristall. Hervorgehoben die Abfolge am Barren: Seed → dünner neck (Versetzungen laufen
seitlich heraus) → sich weitende Schulter (cone) → zylindrischer Einkristall.
:::

**Der Segregations-Effekt.** Beim Erstarren nimmt das feste Silizium Fremdatome **schlechter** auf als die
flüssige Schmelze — die Verunreinigungen werden bevorzugt in der Schmelze **zurückgelassen** (__Segregation__).
Dadurch reichert sich die Schmelze im Lauf des Ziehens immer mehr mit Fremdatomen an. Folge: Der Kristall ist am
**Anfang** (Seed-Ende) reiner als am **Ende** — er ist leicht **inhomogen** dotiert. Dasselbe Prinzip nutzt man
umgekehrt gezielt zur Reinigung (Zonenschmelzen).

:::grafik
Die fest-flüssig-Grenzfläche vergrößert: Si-Atome ordnen sich in den Kristall ein, Fremdatome (rot) werden in die
Schmelze zurückgedrängt. Ein Zeitverlauf zeigt die steigende Fremdatom-Konzentration in der Schmelze → Kristall
am Seed-Ende rein, am Fuß-Ende unreiner.
:::

:::kern
Vom Quarzsand zum Si-Einkristall in **drei Stufen**: (1) **Reduktion** $\text{SiO}_2+2\text{C}\to\text{Si}+2\text{CO}$
im Lichtbogen → Roh-Si (noch 2–4 % Fremdatome). (2) **Reinigung** über __Trichlorsilan__
$\text{Si}+3\text{HCl}\to\text{SiHCl}_3+\text{H}_2$: als Gas per **Destillation** reinigbar (Siedepunkt
$31{,}8\,^\circ$C, verschieden von den Fremd-Chloriden), dann __Siemens-Prozess__
$\text{SiHCl}_3+\text{H}_2\to\text{Si}+3\text{HCl}$ am glühenden Stab → reines, aber **poly**-kristallines Si.
(3) __Czochralski__: Impfkristall in die Schmelze ($>1414\,^\circ$C, Argon), drehen + langsam ziehen; **Dash-Neck**
($\approx3\,$mm) wächst Versetzungen aus; __Segregation__ (Fremdatome bleiben in der Schmelze) macht den Kristall
vom Seed- zum Fuß-Ende unreiner.
:::

Damit haben wir das **reale** Material: einen periodischen, hochreinen Einkristall. Für die Physik der Elektronen
darin brauchen wir aber noch eine zweite Beschreibung der Periodizität — nicht im Orts-, sondern im
**Wellenzahl-Raum**. Dieses __reziproke Gitter__ und seine zentrale Zelle, die __Brillouin-Zone__, sind das Thema
des letzten Kristallstruktur-Artikels und zugleich die Bühne der Bandstruktur.

:::quiz
F: Warum genügt das 98 %-reine metallurgische Silizium aus Stufe 1 nicht für Bauelemente?
A: 2–4 % Fremdatome sind für die Elektronik katastrophal viel, denn schon ein Fremdatom pro Milliarde Si-Atome ändert die elektrischen Eigenschaften. Das Material muss noch um etwa den Faktor $10^9$ reiner werden.
F: Welche Rolle spielt der Kohlenstoff bei der Reduktion $\text{SiO}_2+2\text{C}\to\text{Si}+2\text{CO}$?
A: Der Kohlenstoff bindet den Sauerstoff aus dem $\text{SiO}_2$ (es entsteht Kohlenmonoxid) und reißt ihn so vom Silizium weg. Zurück bleibt elementares Silizium — das ist eine klassische Reduktion.
F: Warum reinigt man Silizium über ein Gas statt den festen Brocken direkt?
A: In einem Festkörper sitzen Verunreinigungen fest und lassen sich kaum heraustrennen. Ein Gas dagegen kann man per Destillation nach Siedepunkten sauber trennen — deshalb wandelt man das Silizium erst in eine flüchtige Verbindung um.
F: Warum ist gerade Trichlorsilan für die Reinigung so geeignet?
A: Sein Siedepunkt von $31{,}8\,^\circ$C unterscheidet sich deutlich von denen der Fremd-Chloride (z. B. $\text{BCl}_3$ 12 °C, $\text{AsCl}_3$ 132 °C). Durch mehrfache Destillation lässt es sich daher sauber von den Verunreinigungen abtrennen.
F: Warum scheidet sich beim Siemens-Prozess das Silizium nur am glühenden Stab ab?
A: Die Zersetzung $\text{SiHCl}_3+\text{H}_2\to\text{Si}+3\text{HCl}$ läuft nur bei der hohen Temperatur ($\approx1150\,^\circ$C) der Staboberfläche ab. Nur dort zerfällt das Gas und lagert reines Silizium an, während es im kühleren Raum stabil bleibt.
F: Warum ist das Silizium nach dem Siemens-Prozess noch nicht brauchbar für Bauelemente?
A: Es ist zwar hochrein, aber polykristallin — es besteht aus vielen kleinen, verschieden orientierten Kristalliten. Bauelemente brauchen einen einzigen, durchgehend geordneten Einkristall, den erst die Czochralski-Zucht liefert.
F: Wie überträgt der Impfkristall seine Ordnung auf die ganze Schmelze?
A: Taucht man den Seed in die knapp überschmelzende Masse, erstarren die Atome an seiner Berührfläche und übernehmen dabei seine Kristallorientierung. Zieht man ihn langsam heraus, wächst der Kristall an der kühleren Grenzfläche in derselben Ordnung stetig weiter.
F: Wozu dient der dünne „Dash-Neck" beim Czochralski-Ziehen?
A: Beim ersten Kontakt erzeugt der Thermoschock Versetzungen im Seed. Zieht man zunächst schnell einen nur ~3 mm dünnen Hals, laufen diese Versetzungen seitlich heraus; erst im versetzungsfreien Hals weitet man auf den vollen Durchmesser auf.
F: Was ist der Segregations-Effekt, und welche Folge hat er für den Barren?
A: Beim Erstarren nimmt das feste Silizium Fremdatome schlechter auf als die Schmelze, sodass Verunreinigungen in der Schmelze zurückbleiben und sich dort anreichern. Dadurch ist der Kristall am Seed-Ende reiner als am Fuß-Ende — er ist leicht inhomogen.
F: Wie nutzt man das Segregationsprinzip gezielt zur Reinigung?
A: Beim Zonenschmelzen schiebt man eine schmale geschmolzene Zone durch den Stab; die Fremdatome wandern mit der Schmelze zum Ende, weil das erstarrende Silizium sie zurückweist. So reichert man die Verunreinigungen gezielt an einem Ende an und trennt sie ab.
:::
