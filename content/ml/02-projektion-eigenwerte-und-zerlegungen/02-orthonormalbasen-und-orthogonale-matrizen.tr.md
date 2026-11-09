---
title: Ortonormal tabanlar ve ortogonal matrisler
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
knoten: Temeller 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15220200
summary: Bazı koordinat sistemleri özellikle kullanışlıdır: Eksenleri birbirine diktir ve birim her eksende aynı uzunluktadır.
tags: ortonormal, ortonormal taban, ortogonal matris
lang: tr
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bazı koordinat sistemleri özellikle kullanışlıdır: Eksenleri birbirine diktir ve birim her eksende aynı uzunluktadır. Böyle bir sistemde bir noktanın koordinatlarını bulmak için denklem sistemi çözmek gerekmez ve uzunluklar Pisagor teoremiyle hesaplanır. Bu kesim bu tür koordinat sistemlerini ve onlara ait matrisleri tanıtıyor.
:::

### Ortonormal vektörler

<span class="anker" id="stufe-1-1"></span>

[Temeller 1, Kesim 5.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-3)'te iç çarpımları sıfır olan iki vektöre ortogonal denmişti. Sabit örüntü $(1,1,1,1)^{\top}$ ile işaret değiştiren örüntü $(1,-1,1,-1)^{\top}$ bunun bir örneğiydi: Bir sinyalin örüntülerden biriyle karşılaştırılmasını öbür örüntü bozmuyordu. Ancak bu karşılaştırma payın $4$ katını veriyordu, çünkü iki örüntünün de uzunluğu $2$. Ortogonal vektörlerin uzunluğu ayrıca $1$ ise bu çarpan da ortadan kalkar.

Düzlemin $\mathbf{e}_1$ ve $\mathbf{e}_2$ eksenlerini, bütün olarak bir açı kadar döndürülmüş biçimde düşünün. İki ok yine $1$ uzunluğundadır ve yine birbirine diktir; yalnızca başka doğrultuları gösterirler.

:::definition Tanım 1.1 (Ortonormal)
<span class="anker" id="satz-1-1"></span>

$\mathbf{q}_1,\dots,\mathbf{q}_k\in\mathbb{R}^n$ vektörlerinin her birinin uzunluğu $1$ ise ve bunlardan farklı herhangi ikisi ortogonalse, bu vektörlere __ortonormal__ denir:

<span class="anker" id="gl-1-1"></span>
$$\mathbf{q}_i^{\top}\mathbf{q}_l=\begin{cases}1, & i=l,\\ 0, & i\ne l.\end{cases} \tag{1.1}$$
:::

Sözcük, “ortogonal” ile “normlanmış” (yani birim uzunluğa getirilmiş) sözcüklerinin birleşimidir. $\mathbf{e}_1,\dots,\mathbf{e}_n$ birim vektörleri en basit örnektir.

:::satz Teorem 1.2 (Ortonormal vektörler doğrusal bağımsızdır)
<span class="anker" id="satz-1-2"></span>

$\mathbf{q}_1,\dots,\mathbf{q}_k$ ortonormal ise doğrusal bağımsızdırlar.
:::

:::beweis Doğrusal bağımsızlık
$c_1\mathbf{q}_1+\dots+c_k\mathbf{q}_k=\mathbf{0}$ olsun. İki tarafın $\mathbf{q}_l$ ile iç çarpımı alınır. [(1.1)](#gl-1-1) uyarınca solda yalnızca $c_l\,\mathbf{q}_l^{\top}\mathbf{q}_l=c_l$ terimi kalır, sağda ise $\mathbf{q}_l^{\top}\mathbf{0}=0$ durur. Demek ki $c_l=0$, hem de her $l$ için. [Temeller 1, Kesim 13.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-2)'deki tanıma göre vektörler böylece doğrusal bağımsızdır.
:::

::::beispiel [Sayısal örnek]
$\mathbf{q}_1=(0{,}6;\ 0{,}8)^{\top}$ ve $\mathbf{q}_2=(-0{,}8;\ 0{,}6)^{\top}$ için

$$\mathbf{q}_1^{\top}\mathbf{q}_1=0{,}36+0{,}64=1,\qquad \mathbf{q}_2^{\top}\mathbf{q}_2=0{,}64+0{,}36=1,\qquad \mathbf{q}_1^{\top}\mathbf{q}_2=-0{,}48+0{,}48=0 .$$

İki vektör ortonormaldir; son iç çarpımı Şekil [1](#abb-1) adım adım gösteriyor. Sabit örüntü ile işaret değiştiren örüntü, uzunlukları olan $2$ sayısına bölündüklerinde ortonormal olur: $\tfrac12(1,1,1,1)^{\top}$ ve $\tfrac12(1,-1,1,-1)^{\top}$.

:::abbildung ml/k2rorth 1
$\mathbf{q}_1^{\top}\mathbf{q}_2$ iç çarpımı adım adım, $0{,}6=\tfrac35$ ve $0{,}8=\tfrac45$ ile: önce bileşenler karşılıklı çarpılır, sonra toplanır.
:::
::::

⁠**Kısacası:** Ortonormal vektörler $1$ uzunluğundadır ve ikişer ikişer birbirine diktir; her zaman doğrusal bağımsızdırlar.

### Ortonormal tabanlar

<span class="anker" id="stufe-1-2"></span>

[Temeller 1, Kesim 13.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3)'e göre bir taban bir koordinat sistemidir: Her vektörün bu tabanda tam olarak bir gösterimi vardır. En kullanışlı tabanlar, vektörleri ortonormal olanlardır. Bunlar alışılmış eksen takımı gibidir, yalnızca döndürülmüştür.

:::definition Tanım 1.3 (Ortonormal taban)
<span class="anker" id="satz-1-3"></span>

Ortonormal vektörlerden oluşan bir tabana __ortonormal taban__ denir.
:::

$\mathbb{R}^n$ uzayının tamamı için $n$ tane ortonormal vektör bulmak yeterlidir. Bunlar önceki alt kesimdeki teoreme göre doğrusal bağımsızdır. Bir $n\times n$ matrise sütun olarak yazılırlarsa bu matrisin rankı $n$ olur ve [Temeller 1, Kesim 13.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5)'e göre sütun uzayı $\mathbb{R}^n$ uzayının tamamıdır. Dolayısıyla $n$ vektör $\mathbb{R}^n$ uzayını gerer ve bir taban oluşturur. Aynı şekilde bir gerilen alt uzay (span) için, örneğin $\mathbb{R}^3$ uzayındaki bir düzlem için de bir ortonormal taban aranabilir: tam olarak bu alt uzayı geren ortonormal vektörler.

::::beispiel [Sayısal örnek]
$\mathbf{q}_1=(0{,}6;\ 0{,}8)^{\top}$ ve $\mathbf{q}_2=(-0{,}8;\ 0{,}6)^{\top}$ vektörleri $\mathbb{R}^2$ uzayında iki ortonormal vektördür, dolayısıyla $\mathbb{R}^2$ uzayının bir ortonormal tabanıdır. $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ birim vektörleri, $\mathbb{R}^3$ uzayının standart taban denen ortonormal tabanını oluşturur. $\mathbb{R}^3$ uzayındaki $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ düzleminin ortonormal tabanı $\mathbf{e}_1,\mathbf{e}_2$ vektörleridir.
::::

⁠**Kısacası:** Ortonormal taban döndürülmüş bir eksen takımıdır: $\mathbb{R}^n$ uzayındaki $n$ ortonormal vektör her zaman bir taban oluşturur.

### Ortonormal tabanda koordinatlar

<span class="anker" id="stufe-1-3"></span>

Sıradan bir tabanda bir vektörün koordinatlarını bulmak için bir denklem sistemi çözmek gerekir. [Temeller 1, Kesim 13.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3)'te $(3,\,2)^{\top}$ vektörünün $(1,\,0)^{\top}$, $(1,\,1)^{\top}$ tabanındaki koordinatları $1$ ve $2$ idi. $(1,0)(3,2)^{\top}=3$ ve $(1,1)(3,2)^{\top}=5$ iç çarpımları ise bambaşka şeylerdir. Ortonormal bir tabanda ise koordinatlar tam olarak iç çarpımlardır.

Bunun nedenini [Temeller 1, Kesim 5.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5)'teki gölge uzunluğu resmi gösterir. Birim uzunlukta bir $\mathbf{q}$ vektörü için $\mathbf{q}^{\top}\mathbf{x}$, $\mathbf{x}$ vektörünün $\mathbf{q}$ doğrultusundaki doğru üzerine düşen gölgesinin uzunluğudur. Ortonormal bir tabanda her koordinat, vektörün kendi eksenine düşen gölgesidir (Şekil [2](#abb-2)).

:::abbildung ml/k2onb 2
$\mathbf{q}_1=(0{,}6;\,0{,}8)^{\top}$, $\mathbf{q}_2=(-0{,}8;\,0{,}6)^{\top}$ ortonormal tabanında (yeşil) koordinatlar. $\mathbf{x}=(3,1)^{\top}$ oku döndürülmüş iki eksenin (gri) her birine bir gölge düşürür; ışık her seferinde dik gelir (kesikli). $\mathbf{q}_1^{\top}\mathbf{x}=2{,}6$ (mavi) ve $\mathbf{q}_2^{\top}\mathbf{x}=-1{,}8$ (turuncu) gölge uzunlukları koordinatlardır: $\mathbf{x}=2{,}6\,\mathbf{q}_1-1{,}8\,\mathbf{q}_2$.
:::

:::satz Teorem 1.4 (Ortonormal tabanda koordinatlar)
<span class="anker" id="satz-1-4"></span>

$\mathbf{q}_1,\dots,\mathbf{q}_n$, $\mathbb{R}^n$ uzayının bir ortonormal tabanıysa her $\mathbf{x}\in\mathbb{R}^n$ vektörü için şunlar geçerlidir:

<span class="anker" id="gl-1-2"></span>
$$\mathbf{x}=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})\,\mathbf{q}_i\qquad\text{ve}\qquad \lVert\mathbf{x}\rVert^2=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})^2 . \tag{1.2}$$
:::

:::beweis Ortonormal tabanda koordinatlar
Vektörler bir taban oluşturduğundan $\mathbf{x}=\sum_ic_i\mathbf{q}_i$ olacak biçimde $c_1,\dots,c_n$ sayıları vardır. $\mathbf{q}_l$ ile iç çarpım [(1.1)](#gl-1-1) uyarınca şunu verir:

$$\mathbf{q}_l^{\top}\mathbf{x}=\sum_{i=1}^nc_i\,\mathbf{q}_l^{\top}\mathbf{q}_i=c_l ,$$

çünkü yalnızca $i=l$ olan terim sıfırdan farklıdır. Uzunluk için çarpım açılır:

$$\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^nc_i\,c_l\,\mathbf{q}_i^{\top}\mathbf{q}_l=\sum_{i=1}^nc_i^2 ,$$

çünkü yine yalnızca $i=l$ olan terimler kalır.
:::

İkinci formül $\mathbb{R}^n$ uzayında Pisagor teoremidir: Birim bütün eksenlerde $1$ uzunluğunda olduğu sürece, bir okun uzunluğu her dik eksen takımındaki koordinatlarından aynı biçimde elde edilir.

::::beispiel [Sayısal örnek]
$\mathbf{x}=(3,\,1)^{\top}$ ve önceki alt kesimdeki taban için

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=1{,}8+0{,}8=2{,}6,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=-2{,}4+0{,}6=-1{,}8 .$$

Sağlama: $2{,}6\,(0{,}6;\ 0{,}8)^{\top}-1{,}8\,(-0{,}8;\ 0{,}6)^{\top}=(1{,}56+1{,}44;\ 2{,}08-1{,}08)^{\top}=(3,\,1)^{\top}$. Ayrıca $c_1^2+c_2^2=6{,}76+3{,}24=10=\lVert\mathbf{x}\rVert^2$. Şekil [3](#abb-3) üç toplamı kesirlerle gösteriyor.

:::abbildung ml/k2rkoord 3
$\mathbf{x}$ vektörünün $c_1=\tfrac{13}5=2{,}6$ ve $c_2=-\tfrac95=-1{,}8$ koordinatları iç çarpım olarak ve bunların karelerinin toplamı, yani $\mathbf{x}$ vektörünün uzunluğunun karesi.
:::
::::

⁠**Kısacası:** Ortonormal bir tabanda her koordinat bir iç çarpımdır, $c_i=\mathbf{q}_i^{\top}\mathbf{x}$, ve koordinatların karelerinin toplamı uzunluğun karesidir.

:::hintergrund Ortonormal taban olarak örneklenmiş salınımlar ve Parseval teoremi
Şu dört vektör

$$\begin{gathered} \mathbf{q}_1=\tfrac12(1,\,1,\,1,\,1)^{\top},\qquad \mathbf{q}_2=\tfrac1{\sqrt2}(1,\,0,\,-1,\,0)^{\top},\\ \mathbf{q}_3=\tfrac1{\sqrt2}(0,\,1,\,0,\,-1)^{\top},\qquad \mathbf{q}_4=\tfrac12(1,\,-1,\,1,\,-1)^{\top} \end{gathered}$$

sırasıyla bir sabit (DC) bileşenin, periyodu dört adım olan bir kosinüs ve bir sinüs salınımının ve her adımda işaret değiştiren bir salınımın örnek değerleridir; her biri normlanmıştır. Ortonormal oldukları kolayca doğrulanır. Dolayısıyla $\mathbb{R}^4$ uzayının bir ortonormal tabanını oluştururlar. Dört örnek değerli her sinyal bu dört salınımın bir toplamıdır ve bunların payları [(1.2)](#gl-1-2) uyarınca basitçe iç çarpımlardır. $\mathbf{x}=(4,\,2,\,0,\,2)^{\top}$ sinyali için $\mathbf{q}_1^{\top}\mathbf{x}=4$, $\mathbf{q}_2^{\top}\mathbf{x}=4/\sqrt2=2\sqrt2$, $\mathbf{q}_3^{\top}\mathbf{x}=0$ ve $\mathbf{q}_4^{\top}\mathbf{x}=0$ olur: Sinyal yalnızca sabit bileşenden ve kosinüsten oluşur.

[(1.2)](#gl-1-2) içindeki ikinci formül, sinyalin $\lVert\mathbf{x}\rVert^2=24$ enerjisinin payların karelerinin toplamına eşit olduğunu söyler: $16+8+0+0=24$. Sinyal işlemede bu önermeye Parseval teoremi denir. Ayrık Fourier dönüşümü, karmaşık salınımlarla yapılan aynı ayrışımdır. $N$ örnek değer için bu dönüşümün matrisi uzunlukları ancak ve ancak $1/\sqrt N$ ile normlandığında korur; bu çarpan olmadan Parseval teoreminde ek olarak $N$ çarpanı bulunur.
:::

### Ortogonal matrisler

<span class="anker" id="stufe-1-4"></span>

Ortonormal bir tabanın vektörleri bir $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$ matrisine sütun olarak yazılırsa, [(1.2)](#gl-1-2) içindeki iki formül de matris çarpımı olarak yazılabilir. [Temeller 1, Kesim 7.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-2)'deki satır bakışına göre bütün koordinatlar birden $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$ vektörüdür, çünkü $\mathbf{Q}^{\top}$ matrisinin satırları $\mathbf{q}_i^{\top}$ vektörleridir. Tersine, sütun bakışına göre $\mathbf{x}=\sum_ic_i\mathbf{q}_i=\mathbf{Q}\mathbf{c}$ olur. Demek ki $\mathbf{Q}^{\top}$ matrisi, $\mathbf{Q}$ matrisinin yaptığını geri alır.

:::definition Tanım 1.5 (Ortogonal matris)
<span class="anker" id="satz-1-5"></span>

Sütunları ortonormal olan bir $\mathbf{Q}\in\mathbb{R}^{n\times n}$ kare matrisine __ortogonal matris__ denir. Denk olarak: $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$.
:::

İki ifade denktir, çünkü $\mathbf{Q}^{\top}\mathbf{Q}$ matrisinin $(i,l)$ elemanı, $i$ ve $l$ numaralı sütunların $\mathbf{q}_i^{\top}\mathbf{q}_l$ iç çarpımıdır. $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ koşulu yani tam olarak [(1.1)](#gl-1-1) bağıntısıdır.

:::satz Teorem 1.6 (Ortogonal bir matrisin tersi)
<span class="anker" id="satz-1-6"></span>

$\mathbf{Q}$ ortogonal ise $\mathbf{Q}$ tersinirdir ve $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$ olur. Ayrıca $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$ olur; yani $\mathbf{Q}$ matrisinin satırları da ortonormaldir ve $\mathbf{Q}^{\top}$ de ortogonaldir.
:::

:::beweis Ortogonal bir matrisin tersi
Sütunlar ortonormaldir, dolayısıyla ilk alt kesime göre doğrusal bağımsızdır. Bu yüzden [Temeller 1, Kesim 13.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5)'teki teoreme göre $\mathbf{Q}$ tersinirdir. $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ eşitliği sağdan $\mathbf{Q}^{-1}$ ile çarpılırsa $\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$ çıkar ve böylece $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{Q}\mathbf{Q}^{-1}=\mathbf{I}$ olur.
:::

Ad üzerine bir not. Ortogonal bir matrisin sütunları yalnızca ortogonal değil, ortonormaldir; ad tarihsel olarak böyle yerleşmiştir. Sütunları yalnızca ortogonal olup birim uzunlukta olmayan matrislerin ayrı bir adı yoktur. Bunlar için $\mathbf{Q}^{\top}\mathbf{Q}$, köşegeninde sütunların uzunluklarının kareleri bulunan bir köşegen matristir, ama $\mathbf{I}$ değildir.

::::beispiel [Sayısal örnek]
İlk alt kesimdeki vektörler sütun olarak alınınca şu bulunur:

$$\mathbf{Q}=\begin{pmatrix}0{,}6&-0{,}8\\0{,}8&0{,}6\end{pmatrix},\qquad \mathbf{Q}^{\top}\mathbf{Q}=\begin{pmatrix}0{,}36+0{,}64&-0{,}48+0{,}48\\-0{,}48+0{,}48&0{,}64+0{,}36\end{pmatrix}=\mathbf{I} .$$

$\mathbf{Q}^{\top}\mathbf{Q}$ matrisinin elemanları ilk alt kesimdeki sütunların iç çarpımlarıdır; köşegen dışındaki elemanı Şekil [1](#abb-1) gösteriyor. Dolayısıyla hiç hesap yapmadan $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$ bulunur. Bu matris, $\cos\alpha=0{,}6$ ve $\sin\alpha=0{,}8$ ile [Temeller 1, Kesim 8.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3)'teki dönme matrisidir, yani saat yönünün tersine $\alpha\approx53{,}13^\circ$ kadar bir dönmedir. $\mathbf{Q}^{\top}$ tersi aynı açı kadar geri döndürür.
::::

⁠**Kısacası:** Ortogonal matris, sütunları ortonormal olan bir kare matristir; tersi basitçe devriğidir.

### Uzunluklar ve açılar korunur

<span class="anker" id="stufe-1-5"></span>

Bir dönme ne bir okun uzunluğunu ne de iki ok arasındaki açıyı değiştirir. Bu özellik bütün ortogonal matrislerde vardır ve onlarla hesap yapmanın bu kadar sevilmesinin nedeni de budur.

:::satz Teorem 1.7 (Ortogonal matrisler iç çarpımları korur)
<span class="anker" id="satz-1-7"></span>

$\mathbf{Q}$ ortogonal ise bütün $\mathbf{x},\mathbf{y}\in\mathbb{R}^n$ için şunlar geçerlidir:

<span class="anker" id="gl-1-3"></span>
$$(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{y},\qquad \lVert\mathbf{Q}\mathbf{x}\rVert=\lVert\mathbf{x}\rVert , \tag{1.3}$$

ayrıca $\mathbf{Q}\mathbf{x}$ ile $\mathbf{Q}\mathbf{y}$ arasındaki açı, $\mathbf{x}$ ile $\mathbf{y}$ arasındaki açıyla aynıdır. Determinant ya $\det\mathbf{Q}=1$ ya da $\det\mathbf{Q}=-1$ olur.
:::

:::beweis İç çarpımların korunması
[Temeller 1, Kesim 10.1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1)'deki $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ kuralına göre $(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{y}=\mathbf{x}^{\top}\mathbf{I}\mathbf{y}=\mathbf{x}^{\top}\mathbf{y}$ olur. $\mathbf{y}=\mathbf{x}$ alınınca uzunlukla ilgili önerme çıkar; açı da yalnızca iç çarpımlardan ve uzunluklardan hesaplandığı için o da değişmez. Determinant için [Temeller 1, Kesim 14.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5)'teki hesap kuralları kullanılır: $1=\det\mathbf{I}=\det(\mathbf{Q}^{\top}\mathbf{Q})=\det\mathbf{Q}^{\top}\cdot\det\mathbf{Q}=(\det\mathbf{Q})^2$.
:::

Demek ki ortogonal bir matris uzayı bozmadan, rijit biçimde hareket ettirir. $\det\mathbf{Q}=1$ ise bir dönmedir. $\det\mathbf{Q}=-1$ ise bir yansıma içerir, çünkü [Temeller 1, Kesim 14.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-2)'ye göre negatif bir determinant yönelimi tersine çevirir.

::::beispiel [Sayısal örnek]
Önceki alt kesimdeki dönme $\mathbf{x}=(3,\,1)^{\top}$ vektörünü $\mathbf{Q}\mathbf{x}=(1{,}8-0{,}8;\ 2{,}4+0{,}6)^{\top}=(1,\,3)^{\top}$ vektörüne götürür. İki vektörün de uzunluğunun karesi $10$. Dönmenin determinantı $0{,}36+0{,}64=1$. $\bigl(\begin{smallmatrix}0{,}6&0{,}8\\0{,}8&-0{,}6\end{smallmatrix}\bigr)$ matrisinin sütunları da ortonormaldir, ama determinantı $-0{,}36-0{,}64=-1$: Bu matris $(2,\,1)^{\top}$ doğrultusundaki doğruya göre yansıtır, çünkü $(2,\,1)^{\top}$ vektörünü kendisine, $(-1,\,2)^{\top}$ vektörünü de $(1,\,-2)^{\top}$ vektörüne götürür.
::::

⁠**Kısacası:** Ortogonal matrisler iç çarpımları, uzunlukları ve açıları korur; döndürür ya da yansıtırlar ve determinantları $\pm1$ olur.

:::hintergrund Sayısal hesapta ortogonal matrisler neden tercih edilir
Bir bilgisayar yuvarlanmış sayılarla hesap yapar; her ara sonuç küçük bir $\boldsymbol{\delta}$ hatası taşır. Böyle bir ara sonuç bir matrisle çarpılırsa hata da o matrisle çarpılır. Herhangi bir matris hatayı bu sırada büyütebilir; ortogonal bir matris büyütemez, çünkü [(1.3)](#gl-1-3) uyarınca $\lVert\mathbf{Q}\boldsymbol{\delta}\rVert=\lVert\boldsymbol{\delta}\rVert$. Bu yüzden yalnızca ortogonal matrislerle yapılan çarpımlardan oluşan hesap yolları yuvarlama hatalarını büyütmez. Aynı nedenle ters matris de sorun değildir: Hesaplanması gerekmez, devrik yeterlidir ve devrik hatasızdır.
:::

### Ortonormal sütunlu matrisler

<span class="anker" id="stufe-1-6"></span>

Çoğu zaman elde, uzayın boyutundan daha az sayıda ortonormal vektör vardır. $\mathbb{R}^3$ uzayındaki bir düzlemin iki vektörden oluşan bir ortonormal tabanı vardır. Bunlar bir matrise sütun olarak yazılırsa matris kare olmaz; üç satırı ve iki sütunu olur. Hesap kurallarının bazıları bu duruma da aktarılır, bazıları aktarılmaz; aradaki fark önemlidir.

:::satz Teorem 1.8 (Ortonormal sütunlu dikdörtgen matrisler)
<span class="anker" id="satz-1-8"></span>

$\mathbf{Q}\in\mathbb{R}^{n\times k}$ matrisinin sütunları ortonormal ve $k<n$ ise $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_k$ olur ve her $\mathbf{c}\in\mathbb{R}^k$ için $\lVert\mathbf{Q}\mathbf{c}\rVert=\lVert\mathbf{c}\rVert$ geçerlidir. Buna karşılık $\mathbf{Q}\mathbf{Q}^{\top}\in\mathbb{R}^{n\times n}$ matrisi birim matris değildir.
:::

:::beweis Dikdörtgen matrisler
İlk iki önerme, tıpkı kare matrislerde olduğu gibi [(1.1)](#gl-1-1) bağıntısından çıkar. Üçüncüsü için: $\mathbf{Q}^{\top}$ matrisinin $k$ satırı ve $n$ sütunu vardır. [Temeller 1, Kesim 13.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5)'teki rank-sıfırlık teoremine göre çekirdeğinin boyutu $n-\operatorname{rank}\mathbf{Q}^{\top}\ge n-k\ge1$. Demek ki $\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}$ olan bir $\mathbf{z}\ne\mathbf{0}$ vektörü vardır ve onun için $\mathbf{Q}\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}\ne\mathbf{z}$ olur. Dolayısıyla $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$.
:::

::::beispiel [Sayısal örnek 1]
Tek sütunu $\mathbf{q}=(0{,}6;\ 0{,}8)^{\top}$ olan matris $\mathbf{q}^{\top}\mathbf{q}=1$ koşulunu sağlar, ama

$$\mathbf{q}\mathbf{q}^{\top}=\begin{pmatrix}0{,}36&0{,}48\\0{,}48&0{,}64\end{pmatrix}\ne\mathbf{I} .$$

Bu matris $(-0{,}8;\ 0{,}6)^{\top}$ vektörünü $\mathbf{0}$ vektörüne götürür. $\mathbf{x}=(3,\,1)^{\top}$ vektörünü ise $(1{,}08+0{,}48;\ 1{,}44+0{,}64)^{\top}=(1{,}56;\ 2{,}08)^{\top}$ vektörüne götürür. Bu, [Temeller 1, Kesim 5.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5)'teki $\mathbf{x}$ gölgesinin tam uç noktasıdır, çünkü $\mathbf{q}\mathbf{q}^{\top}\mathbf{x}=\mathbf{q}\,(\mathbf{q}^{\top}\mathbf{x})=2{,}6\,\mathbf{q}$.
::::

::::beispiel [Sayısal örnek 2]
$\mathbf{Q}=\Bigl(\begin{smallmatrix}1&0\\0&1\\0&0\end{smallmatrix}\Bigr)$ matrisinin sütunları $\mathbb{R}^3$ uzayındaki $\mathbf{e}_1$ ve $\mathbf{e}_2$ vektörleridir. $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_2$ olur, ama $\mathbf{Q}\mathbf{Q}^{\top}=\operatorname{diag}(1;\,1;\,0)$. Bu matris ilk iki bileşeni korur ve üçüncüsünü sıfırlar.
::::

⁠**Kısacası:** Ortonormal sütunlu dikdörtgen bir matriste $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ olur, ama $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$: Bu sıradaki çarpım vektörün bir kısmını atar.

:::aufgabe Alıştırma 1 ★ Ortonormallik ve koordinatlar
<span class="anker" id="aufg-1"></span>

$\mathbf{q}_1=\tfrac13(1,\,2,\,2)^{\top}$, $\mathbf{q}_2=\tfrac13(2,\,1,\,-2)^{\top}$ ve $\mathbf{q}_3=\tfrac13(2,\,-2,\,1)^{\top}$ veriliyor.

<ol class="al">

<li>

Üç vektörün ortonormal olduğunu doğrulayın.

</li>

<li>

$\mathbf{x}=(3,\,0,\,3)^{\top}$ vektörünün bu ortonormal tabandaki koordinatlarını hesaplayın ve sağlamasını yapın. $\lVert\mathbf{x}\rVert^2$ formülünü doğrulayın.

</li>

</ol>

:::loesung
(a) Altı iç çarpımın hepsi hesaplanır; ortak $\tfrac13\cdot\tfrac13=\tfrac19$ çarpanı başa yazılır:

$$\mathbf{q}_1^{\top}\mathbf{q}_1=\tfrac19(1+4+4)=1,\quad \mathbf{q}_2^{\top}\mathbf{q}_2=\tfrac19(4+1+4)=1,\quad \mathbf{q}_3^{\top}\mathbf{q}_3=\tfrac19(4+4+1)=1,$$

$$\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac19(2+2-4)=0,\quad \mathbf{q}_1^{\top}\mathbf{q}_3=\tfrac19(2-4+2)=0,\quad \mathbf{q}_2^{\top}\mathbf{q}_3=\tfrac19(4-2-2)=0 .$$

Üç vektörün de uzunluğu $1$ olur ve vektörler ikişer ikişer birbirine diktir: Ortonormaldirler, dolayısıyla Kesim [1.2](#stufe-1-2)'ye göre $\mathbb{R}^3$ uzayının bir ortonormal tabanıdırlar.

(b) [(1.2)](#gl-1-2) uyarınca koordinatlar, denklem sistemi çözmeden, iç çarpımlar olarak bulunur:

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=\tfrac13(3+0+6)=3,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=\tfrac13(6+0-6)=0,\qquad c_3=\mathbf{q}_3^{\top}\mathbf{x}=\tfrac13(6+0+3)=3 .$$

Sağlama: $3\mathbf{q}_1+0\cdot\mathbf{q}_2+3\mathbf{q}_3=(1,\,2,\,2)^{\top}+(2,\,-2,\,1)^{\top}=(3,\,0,\,3)^{\top}=\mathbf{x}$. Uzunluk formülü: $c_1^2+c_2^2+c_3^2=9+0+9=18$ ve $\lVert\mathbf{x}\rVert^2=9+0+9=18$.
:::
:::

:::aufgabe Alıştırma 2 ★ Bir ortogonal matris
<span class="anker" id="aufg-2"></span>

$\mathbf{Q}$, sütunları Alıştırma [1](#aufg-1)'deki $\mathbf{q}_1,\mathbf{q}_2,\mathbf{q}_3$ vektörleri olan matris olsun.

<ol class="al">

<li>

$\mathbf{Q}^{-1}$ matrisini hesap yapmadan yazın. $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$ eşitliğini köşegen dışında seçtiğiniz bir eleman üzerinde doğrulayın.

</li>

<li>

$\mathbf{Q}\,(1,\,1,\,1)^{\top}$ çarpımını hesaplayın ve uzunlukları karşılaştırın. $\det\mathbf{Q}$ değerini hesaplayın. $\mathbf{Q}$ döndürüyor mu, yoksa yansıtıyor mu?

</li>

</ol>

:::loesung
(a) Sütunlar ortonormaldir, dolayısıyla $\mathbf{Q}$ ortogonaldir ve hesap yapmadan $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$ bulunur. Burada

$$\mathbf{Q}=\frac13\begin{pmatrix}1&2&2\\2&1&-2\\2&-2&1\end{pmatrix}$$

matrisi üstelik simetriktir, dolayısıyla $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}=\mathbf{Q}$. $\mathbf{Q}\mathbf{Q}^{\top}$ matrisinin $(1,2)$ elemanı, birinci satır ile ikinci satırın iç çarpımıdır: $\tfrac19(1\cdot2+2\cdot1+2\cdot(-2))=0$.

(b) $\mathbf{Q}\,(1,\,1,\,1)^{\top}=\tfrac13(5,\,1,\,1)^{\top}$ olur; uzunluğunun karesi $\tfrac19(25+1+1)=3$ olur; bu, [(1.3)](#gl-1-3) bağıntısının gerektirdiği gibi tam olarak $(1,\,1,\,1)^{\top}$ vektörünün uzunluğunun karesidir. Determinant şudur:

$$\det\mathbf{Q}=\tfrac1{27}\bigl(1\cdot(1-4)-2\cdot(2+4)+2\cdot(-4-2)\bigr)=\tfrac1{27}(-3-12-12)=-1 .$$

Demek ki $\mathbf{Q}$ yansıtır. Daha kesin olarak: $\mathbf{Q}=\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$ olduğundan $\mathbf{Q}^2=\mathbf{I}$ olur; iki kez uygulanınca her şey yerine döner. $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ vektörü ters çevrilir, $\mathbf{Q}\mathbf{k}=\tfrac13(1-2-2,\ 2-1+2,\ 2+2-1)^{\top}=(-1,\,1,\,1)^{\top}=-\mathbf{k}$; $\mathbf{k}$ vektörüne dik vektörler ise yerinde kalır. $\mathbf{Q}$, $x_1-x_2-x_3=0$ düzlemine göre yansımadır.
:::
:::

:::aufgabe Alıştırma 3 ★★ Ortogonal matrislerle hesap
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Gösterin: $\mathbf{Q}_1$ ve $\mathbf{Q}_2$ ortogonal ise $\mathbf{Q}_1\mathbf{Q}_2$ de ortogonaldir.

</li>

<li>

İki ortogonal matrisin toplamı yine ortogonal midir? Gerekçelendirin ya da bir karşı örnek verin.

</li>

<li>

Bir köşegen matrisin ancak ve ancak her köşegen elemanı $1$ ya da $-1$ ise ortogonal olduğunu gösterin. Böyle bir matris geometrik olarak ne yapar?

</li>

</ol>

:::loesung
(a) $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ kuralıyla $(\mathbf{Q}_1\mathbf{Q}_2)^{\top}(\mathbf{Q}_1\mathbf{Q}_2)=\mathbf{Q}_2^{\top}\mathbf{Q}_1^{\top}\mathbf{Q}_1\mathbf{Q}_2=\mathbf{Q}_2^{\top}\mathbf{I}\mathbf{Q}_2=\mathbf{I}$ olur. Sezgisel olarak: Art arda yapılan iki rijit hareket yine bir rijit harekettir.

(b) Hayır. Karşı örnek: $\mathbf{I}+\mathbf{I}=2\mathbf{I}$ ve $(2\mathbf{I})^{\top}(2\mathbf{I})=4\mathbf{I}\ne\mathbf{I}$; toplam bütün uzunlukları iki katına çıkarır. Aynı şekilde $\mathbf{I}+(-\mathbf{I})$ sıfır matristir.

(c) $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$ için $\mathbf{D}^{\top}\mathbf{D}=\operatorname{diag}(d_1^2,\dots,d_n^2)$ olur. Bu ancak ve ancak her $d_i^2=1$, yani $d_i=1$ ya da $d_i=-1$ ise $\mathbf{I}$ olur. Böyle bir matris $d_i=-1$ olan eksenleri ters çevirir, öbürlerini olduğu gibi bırakır: Koordinat düzlemlerine göre yansıtır. Örneğin $\operatorname{diag}(1;\,-1)$ matrisi $x_1$ eksenine göre yansıtır, $\operatorname{diag}(-1;\,-1)$ ise $180^\circ$'lik dönmedir.
:::
:::
