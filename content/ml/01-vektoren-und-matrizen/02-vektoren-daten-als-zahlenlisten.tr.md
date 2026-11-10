---
title: Vektörler: Sayı listesi olarak veriler
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Bölüm 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15210200
summary: Bir bilgisayar yalnızca sayılarla çalışabilir.
tags: indis, toplam sembolü, toplam indisi, çift toplam, Öznitelik, Örnek, Veri kümesi, vektör
lang: tr
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bir bilgisayar yalnızca sayılarla çalışabilir. Bu kesim, gerçek dünyadaki bir nesnenin bir sayı listesiyle nasıl betimlendiğini ve bu tür listelerle hangi hesapların yapılabileceğini açıklıyor.
:::

:::::vorwissen Bunun için gerekenler: Toplam sembolü ve indisler

<span class="anker" id="stufe-1-1"></span>

Bu bölümde sürekli birçok sayı toplanır. Her seferinde “$a_1+a_2+\dots$” diye uzun uzun yazmak gerekmesin diye bir kısaltma vardır.

**İndisler.** Aynı türden birkaç sayı varsa bunlar numaralanır: $a_1,a_2,\dots,a_n$. Alta yazılan numaraya __indis__ denir. İndis yalnızca kaçıncı sayının kastedildiğini söyler; sayının değeriyle bir ilgisi yoktur.

**Toplam sembolü.** $a_1$ ile başlayıp $a_n$ ile biten toplam şöyle yazılır:

<span class="anker" id="gl-1-1"></span>
$$\sum_{i=1}^{n} a_i = a_1+a_2+\dots+a_n , \tag{1.1}$$

ve “$i$, $1$'den $n$'ye kadar giderken $a_i$ terimlerinin toplamı” diye okunur. Büyük Yunan harfi sigmaya __toplam sembolü__ denir. Altındaki $i$ harfine __toplam indisi__ denir: Sırasıyla $1,2,\dots,n$ değerlerini alır ve her değer için toplama bir terim eklenir. Toplam indisi yalnızca bir yer tutucudur. Ona $i$, $j$ ya da $k$ denmesi toplamı değiştirmez: $\sum_{i=1}^n a_i=\sum_{j=1}^n a_j$.

**İki hesap kuralı.** Toplam sembolüyle yazılmış bir toplam, sonlu sayıda sayının kısaltılmış biçimde yazılan sıradan bir toplamıdır. Bu yüzden bilinen kurallar onun için de geçerlidir: Ortak bir çarpan paranteze alınabilir (dağılma özelliği), terimlerin sırası istenildiği gibi değiştirilebilir ve terimler istenildiği gibi gruplanabilir (değişme ve birleşme özelliği). Toplam sembolüyle yazıldığında bu şu anlama gelir: Ortak bir çarpan toplamın önüne alınabilir ve toplamların toplamı ayrı toplamlara bölünebilir:

<span class="anker" id="gl-1-2"></span>
$$\sum_{i=1}^n c\,a_i=c\sum_{i=1}^n a_i ,\qquad \sum_{i=1}^n (a_i+b_i)=\sum_{i=1}^n a_i+\sum_{i=1}^n b_i . \tag{1.2}$$

**Çift toplamlar.** Bir tabloda duran sayılar iki indis alır: $a_{ij}$, $i$ numaralı satırda ve $j$ numaralı sütunda duran sayıdır. $m$ satırlı ve $n$ sütunlu bir tablonun bütün elemanlarının toplamı bir __çift toplam__ olarak şöyle yazılır:

$$\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij} .$$

Çift toplam içeriden dışarıya doğru okunur: Her $i$ satırı için içteki toplam o satırın sayılarını toplar, dıştaki toplam da satır toplamlarını toplar. Terim sayısı sonlu olduğunda sıra önemli olmadığından iki toplam sembolünün yeri değiştirilebilir ve önce sütun sütun toplanabilir.

::::beispiel [Sayısal örnek 1]
$a_1=2$, $a_2=5$, $a_3=1$ için her toplam önce açık yazılır, sonra sayılar yerine konur ve toplanır (Şekil [1](#abb-1)). Böylece $\sum_{i=1}^3 a_i=8$ ve $\sum_{i=1}^3 a_i^2=30$ bulunur. Üçüncü toplamda terim, toplam indisinin kendisidir: $\sum_{j=1}^{3}j=6$.

:::abbildung ml/k1rsumme 1
Adım adım üç toplam: Toplam sembolü açık yazılır, sayılar yerine konur, toplanır.
:::
::::

::::beispiel [Sayısal örnek 2]
Satırları $(1,\,2)$ ve $(3,\,4)$ olan tablonun elemanları şunlardır: $a_{11}=1$, $a_{12}=2$, $a_{21}=3$, $a_{22}=4$. Satır satır toplandığında çift toplam $(1+2)+(3+4)=10$, sütun sütun toplandığında $(1+3)+(2+4)=10$ olur (Şekil [2](#abb-2)).

:::abbildung ml/k1rdoppel 2
Satırları $(1,\,2)$ ve $(3,\,4)$ olan tablo üzerinden çift toplam; üstte önce satır satır, altta önce sütun sütun. İki sıra da aynı toplamı verir.
:::
::::

⁠**Kısacası:** $\sum_{i=1}^n a_i$, $a_1$ ile başlayıp $a_n$ ile biten toplamdır; $i$ toplam indisi yalnızca bir yer tutucudur.

:::::

### Örnekler ve öznitelikler

<span class="anker" id="stufe-1-2"></span>

Verilerden öğrenmek isteyen kişinin önünde önce aynı türden nesnelerden oluşan bir topluluk vardır: daireler, hastalar, mektuplar, bir makinede yapılan ölçümler. Her nesne aynı ölçülen büyüklüklerle betimlenir. Daireler örneğin alanlarıyla, oda sayılarıyla ve şehir merkezine uzaklıklarıyla. Bu bilgiler birkaç daire için yazılınca bir tablo ortaya çıkar (Tablo [1](#tab-1)). Bu tablo bölümün tamamında kullanılacak.

<span class="anker" id="tab-1"></span>

**Tablo 1:** Bu bölümün daire veri kümesi: dört daire, her biri üç öznitelikle betimlenmiş. Sayılar uydurmadır.

|  | Alan ($\mathrm{m}^2$) | Oda | Merkeze uzaklık (km) |
|---|---|---|---|
| Daire 1 | 60 | 2 | 3 |
| Daire 2 | 40 | 1 | 1 |
| Daire 3 | 90 | 4 | 6 |
| Daire 4 | 70 | 3 | 2 |

Tablonun her satırı bir nesneye, her sütunu ölçülen bir büyüklüğe aittir. İkisi için de yerleşik sözcükler vardır.

:::definition Tanım 1.1 (Öznitelik, örnek, veri kümesi)
<span class="anker" id="satz-1-1"></span>

__Öznitelik__, bir gerçel sayıyla ifade edilebilen bir özelliktir.

__Örnek__, $d$ özniteliğin değerleriyle betimlenen tek bir nesnedir.

__Veri kümesi__, hepsi aynı $d$ öznitelikle betimlenen $N$ örnekten oluşan bir topluluktur.
:::

Bütün seri boyunca şu geçerlidir: $N$ örneklerin sayısı, $d$ özniteliklerin sayısıdır. Örnekler $i=1,\dots,N$ ile, öznitelikler $j=1,\dots,d$ ile numaralanır.

Sözcüklerle ilgili iki not. Veritabanlarında bir tablonun tek bir satırına genellikle “kayıt” denir; burada ise veri kümesi tek bir satır değil, bütün topluluktur. Ayrıca “örnek” sözcüğü bu bölümde her zaman bir veri kümesindeki bir nesne anlamına gelir; baştan sona hesaplanmış örnekler bu yüzden “sayısal örnek” diye adlandırılır.

::::beispiel [Sayısal örnek]
Daire veri kümesinde $N=4$ örnek ve $d=3$ öznitelik vardır. Öznitelik 2 oda sayısıdır. Bu öznitelik Daire 3'te $4$ değerini alır.
::::

Her özellik kendiliğinden bir sayı değildir. Bir dairenin bulunduğu semt bir addır. Bu tür özelliklerle hesap yapabilmek için önce onları sayılara çevirmek gerekir. Bu bölümde bütün öznitelikler zaten sayıdır.

⁠**Kısacası:** Bir veri kümesi $N$ örnekten oluşur ve her örnek aynı $d$ öznitelikle betimlenir.

:::hintergrund Aynı şeylere başka adlar
İngilizce metinlerde örneğe *example*, *sample*, *instance* ya da *data point*, özniteliğe *feature* ya da *attribute*, veri kümesine de *dataset* denir. Türkçede de bir örnek için “veri noktası” ve “gözlem” sözcükleri yaygındır. Kastedilen her zaman aynı şeydir: tablonun bir satırı.
:::

### Vektörler

<span class="anker" id="stufe-1-3"></span>

Bilgisayar için bir daire, üç sayısından başka bir şey değildir. Bu üç sayıyla tek bir nesneymiş gibi hesap yapabilmek için sayılar bir listede bir araya getirilir. Listedeki sıra sabittir: önce alan, sonra oda sayısı, sonra uzaklık.

Böyle bir liste yalnızca iki sayı içeriyorsa çizilebilir de. Daire 4'ün yalnızca oda sayısı $3$ ile uzaklığı $2$ alınırsa bu, yatay ekseni odaları, düşey ekseni kilometreleri sayan bir düzlemde $(3,\,2)$ koordinatlı noktadır. Aynı liste, orijinden bu noktaya giden bir ok olarak da düşünülebilir (Şekil [3](#abb-3)). İki resim de aynı iki sayıyı betimler.

:::abbildung ml/k1punktpfeil 3
$\mathbf{x}=(3,\,2)^{\top}$ vektörü, solda nokta olarak, sağda orijinden bu noktaya giden ok olarak. Burada $x_1$, Daire 4'ün oda sayısını, $x_2$ de merkeze km cinsinden uzaklığını gösterir.
:::

:::definition Tanım 1.2 (Vektör)
<span class="anker" id="satz-1-2"></span>

$d$ bileşenli bir __vektör__ $\mathbf{x}$, alt alta yazılmış $d$ tane $x_1,\dots,x_d$ gerçel sayısından oluşan sıralı bir listedir:

$$\mathbf{x}=\begin{pmatrix}x_1\\\vdots\\x_d\end{pmatrix}.$$

$x_j$ sayısına $\mathbf{x}$ vektörünün $j$-inci __bileşeni__ denir. $d$ bileşenli bütün vektörlerin kümesine $\mathbb{R}^d$ denir. İki vektörün bileşen sayıları aynıysa ve aynı yerdeki bileşenlerinin hepsi birbirine eşitse bu iki vektör eşittir.
:::

Vektörler kalın ve küçük harfle, bileşenleri ise ince harfle yazılır. Tek bir gerçel sayıya, vektörden ayırmak için __skaler__ denir.

**Sütun ve satır.** Bu seride bir vektör her zaman bir sütundur. Metin içinde bir sütun çok yer kaplar. Bu yüzden sayılar yan yana yazılır ve arkalarına üst simge olarak bir $\top$ konur: $(x_1,\dots,x_d)^{\top}$, aynı sayıların sütun olarak yazılışı demektir. İşaret __devrik__ diye okunur. Bir satırı sütuna, bir sütunu satıra çevirir. Tersine, $\mathbf{x}^{\top}=(x_1,\,\dots,\,x_d)$, satır olarak yazılmış $\mathbf{x}$ vektörüdür. Bir vektör ondalık sayılar içeriyorsa, ondalık virgül ayırıcı virgülle karıştırılmasın diye bileşenler noktalı virgülle ayrılır: $(0{,}2;\ 0{,}25;\ 0{,}3)^{\top}$ vektörünün üç bileşeni vardır.

**Bir veri kümesinin örnekleri.** $i$ numaralı örnek $\mathbf{x}_i\in\mathbb{R}^d$ vektörüdür. Bir örneğin vektörüne onun __öznitelik vektörü__ de denir. Bileşenleri iki indis alır: $x_{ij}$, $i$ numaralı örnekte $j$ numaralı özniteliğin değeridir. Yani tek indisli kalın bir harf, bir vektör listesinden alınmış bütün bir vektördür; iki indisli ince bir harf ise tek bir sayıdır.

::::beispiel [Sayısal örnek]
Daire 1, $\mathbf{x}_1=(60,\,2,\,3)^{\top}\in\mathbb{R}^3$ vektörüdür. Bu vektörün ikinci bileşeni $x_{12}=2$ sayısıdır. $(2,\,60,\,3)^{\top}$ vektörü aynı sayıları içerir, ama başka bir vektördür: Artık ilk yerde $2$ sayısı durur ve bu sayı alan olarak okunurdu.
::::

⁠**Kısacası:** Vektör, nokta ya da ok olarak çizilebilen sıralı bir sayı listesidir; $d$ öznitelikli bir örnek $\mathbb{R}^d$ uzayında bir vektördür.

:::hintergrund Vektör aslında nedir?
Hesaplarda kullanılan vektör bir sayı listesidir. Matematikte kavram daha geniştir: Vektör, nesnenin türünün dışına çıkmadan toplanabilen ve bir sayıyla çarpılabilen her şeydir. Düzlemdeki oklar buna dahildir, ama ses kayıtları da. Bir ses kaydı, eşit ve çok kısa aralıklarla hava basıncının o anda durgun değerinden ne kadar saptığını kaydeder. Bu türden $n$ tane $x[0],\dots,x[n-1]$ değeriyle ses kaydı $\mathbb{R}^n$ uzayında bir vektördür. İki kaydı toplamak onları karıştırmak, bir kaydı bir sayıyla çarpmak da sesini yükseltmek ya da alçaltmak demektir; ikisi de yine aynı uzunlukta bir ses kaydı verir.

Bir görüntü de bir vektördür. $28\times28$ pikselli gri tonlamalı bir görüntü $784$ parlaklık değerinden oluşur. Bunlar satır satır arka arkaya okunursa görüntü $\mathbb{R}^{784}$ uzayında bir nokta olur. Bu canlandırma artık çizilemez, ama onunla tıpkı iki ya da üç bileşenli vektörlerle olduğu gibi hesap yapılır.
:::

### Toplama ve katlar

<span class="anker" id="stufe-1-4"></span>

Ölçüm değeri listeleriyle hesap yapmak istenir: iki dairenin elektrik tüketimini toplamak, kilovatsaati megavatsaate çevirmek ya da iki dairenin birbirinden ne kadar farklı olduğuna bakmak. Bunların hepsi bileşen bileşen yapılır.

Oklar resminde toplama şu demektir: İkinci ok birincinin ucuna eklenir. Orijinden yeni uca giden ok toplamdır (Şekil [4](#abb-4), sol). Bir sayıyla çarpmak oku uzatmak ya da kısaltmak demektir; negatif bir çarpan oku ayrıca ters çevirir (Şekil [4](#abb-4), sağ).

:::abbildung ml/k1addition 4
Sol: $\mathbf{u}=(3,\,1)^{\top}$ artı $\mathbf{v}=(1,\,2)^{\top}$. $\mathbf{v}$ oku $\mathbf{u}$ okunun ucuna eklenirse (ya da $\mathbf{u}$ oku $\mathbf{v}$ okunun ucuna, kesikli) varış noktası $\mathbf{u}+\mathbf{v}=(4,\,3)^{\top}$ olur. Sağ: $\mathbf{u}=(2,\,1)^{\top}$, iki katı $2\mathbf{u}=(4,\,2)^{\top}$ (gri) ve $-\mathbf{u}=(-2,\,-1)^{\top}$.
:::

:::definition Tanım 1.3 (Toplama ve kat)
<span class="anker" id="satz-1-3"></span>

$\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ vektörleri ve bir $c$ skaleri için $\mathbf{u}+\mathbf{v}$ __toplamı__ ve $c\,\mathbf{u}$ __katı__, bileşenleri şunlar olan vektörlerdir:

<span class="anker" id="gl-1-3"></span>
$$(\mathbf{u}+\mathbf{v})_j=u_j+v_j ,\qquad (c\,\mathbf{u})_j=c\,u_j ,\qquad j=1,\dots,d. \tag{1.3}$$

Bütün bileşenleri sıfır olan vektöre __sıfır vektörü__ $\mathbf{0}$ denir. $(-1)\,\mathbf{u}$ yerine $-\mathbf{u}$, $\mathbf{u}+(-\mathbf{v})$ yerine $\mathbf{u}-\mathbf{v}$ yazılır.
:::

Yalnızca bileşen sayıları aynı olan vektörler toplanabilir. Toplama ayrıca ancak aynı yerde aynı büyüklük duruyorsa anlamlıdır: kilovatsaate kilovatsaat, metrekareye oda değil.

Her bileşen kendi başına sayılarla yapılan sıradan bir hesap olduğundan bilinen kurallar geçerlidir: $\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u}$, $(\mathbf{u}+\mathbf{v})+\mathbf{q}=\mathbf{u}+(\mathbf{v}+\mathbf{q})$, $c\,(\mathbf{u}+\mathbf{v})=c\,\mathbf{u}+c\,\mathbf{v}$, $(c+c')\,\mathbf{u}=c\,\mathbf{u}+c'\,\mathbf{u}$ ve $\mathbf{u}+\mathbf{0}=\mathbf{u}$; bu, bütün $\mathbf{u},\mathbf{v},\mathbf{q}\in\mathbb{R}^d$ vektörleri ve $c,c'$ skalerleri için böyledir.

$\mathbf{u}-\mathbf{v}$ farkının kendine özgü bir canlandırması vardır. Bu fark, $\mathbf{v}$ vektörünün ucundan $\mathbf{u}$ vektörünün ucuna giden oktur, çünkü $\mathbf{v}+(\mathbf{u}-\mathbf{v})=\mathbf{u}$. İki örnek söz konusuysa fark, her öznitelikte bunların birbirinden ne kadar ayrıldığını gösterir.

::::beispiel [Sayısal örnek]
Daire 1 ocak, şubat ve mart aylarında $\mathbf{u}=(200,\,250,\,300)^{\top}$ kilovatsaat elektrik tüketmiştir, aynı binadaki Daire 2 ise $\mathbf{v}=(150,\,100,\,120)^{\top}$. İkisi birlikte şu kadar tüketir:

$$\mathbf{u}+\mathbf{v}=(350,\,350,\,420)^{\top}\ \text{kWh}.$$

Daire 1'in tüketimini megavatsaat cinsinden $0{,}001\,\mathbf{u}=(0{,}2;\ 0{,}25;\ 0{,}3)^{\top}$ katı verir. $\mathbf{u}-\mathbf{v}=(50,\,150,\,180)^{\top}$ farkı, Daire 1'in her ay Daire 2'den kaç kilovatsaat fazla tükettiğini söyler. Daire veri kümesinde $\mathbf{x}_3-\mathbf{x}_1=(30,\,2,\,3)^{\top}$ olur: Daire 3, Daire 1'den $30\,\mathrm m^2$ daha büyüktür, iki odası daha fazladır ve $3$ km daha dışarıdadır.
::::

⁠**Kısacası:** Vektörler bileşen bileşen toplanır ve bir sayıyla bileşen bileşen çarpılır.

### Doğrusal bileşimler

<span class="anker" id="stufe-1-5"></span>

Bu bölümdeki hesapların neredeyse hepsi birkaç vektör alır, her birini kendine ait bir sayıyla çarpar ve sonuçları toplar. Bir ortalama böyle bir hesaptır, bir karışım da.

Oklar resminde: $c_1$ kez $\mathbf{v}_1$ yolu, sonra $c_2$ kez $\mathbf{v}_2$ yolu gidilir ve bu böyle sürer. Varılan yer sonuçtur.

:::definition Tanım 1.4 (Doğrusal bileşim)
<span class="anker" id="satz-1-4"></span>

$\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^d$ vektörleri ve $c_1,\dots,c_k$ skalerleri için

<span class="anker" id="gl-1-4"></span>
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k=\sum_{l=1}^{k}c_l\,\mathbf{v}_l \tag{1.4}$$

ifadesine $\mathbf{v}_1,\dots,\mathbf{v}_k$ vektörlerinin bir __doğrusal bileşimi__ denir. $c_l$ sayılarına bileşimin __katsayıları__ denir.
:::

Okurken dikkat: $\mathbf{v}_l$ kalındır, yani listenin $l$-inci vektörüdür, bir vektörün $l$-inci bileşeni değil.

::::beispiel [Sayısal örnek 1]
$(1,\,2)^{\top}+3\,(0,\,1)^{\top}=(1,\,2)^{\top}+(0,\,3)^{\top}=(1,\,5)^{\top}$.
::::

::::beispiel [Sayısal örnek 2] orta nokta
Daire 1 ile Daire 2'nin $\tfrac12\mathbf{x}_1+\tfrac12\mathbf{x}_2$ doğrusal bileşimi şudur:

$$\tfrac12\,(60,\,2,\,3)^{\top}+\tfrac12\,(40,\,1,\,1)^{\top}=(50;\ 1{,}5;\ 2)^{\top}.$$

Bu, her öznitelikte tam ikisinin ortasında duran hayali bir dairedir. Nokta, iki noktayı birleştiren doğru parçasının ortasında yer alır.
::::

Bu bölümde bir doğrusal bileşime özellikle sık ihtiyaç duyulur. Bütün $N$ örnek $1/N$ katsayısıyla alınırsa __örneklerin ortalaması__ ortaya çıkar:

<span class="anker" id="gl-1-5"></span>
$$\bar{\mathbf{x}}=\frac1N\sum_{i=1}^{N}\mathbf{x}_i . \tag{1.5}$$

Bu, her öznitelikte bütün örneklerin ortalamasına sahip hayali bir örnektir: $j$ numaralı bileşeni, $j$ numaralı özniteliklerin ortalamasıdır.

::::beispiel [Sayısal örnek 3] örneklerin ortalaması
Daire veri kümesi için $\bar{\mathbf{x}}=(65;\ 2{,}5;\ 3)^{\top}$ bulunur (Şekil [5](#abb-5)), yani “ortalama daire”: ortalamada $65\,\mathrm m^2$, $2{,}5$ oda ve merkeze $3$ km uzaklık.

:::abbildung ml/k1rmittelvektor 5
Dört dairenin ortalaması: Vektörlerin toplamı bileşen bileşen oluşturulur, sonra $4$'e bölünür; $5/2=2{,}5$.
:::
::::

⁠**Kısacası:** Bir doğrusal bileşim her vektörü kendine ait bir sayıyla çarpar ve hepsini toplar.

:::hintergrund İki noktanın karışımları nerede bulunur?
İki $\mathbf{x}_1,\mathbf{x}_2$ vektörü için katsayılar toplamları $1$ olacak biçimde seçilirse, yani bir $t$ sayısıyla $(1-t)\,\mathbf{x}_1+t\,\mathbf{x}_2$ alınırsa, sonuç her zaman iki noktadan geçen doğru üzerinde bulunur. Çünkü bu ifade şöyle yazılabilir:

$$(1-t)\,\mathbf{x}_1+t\,\mathbf{x}_2=\mathbf{x}_1+t\,(\mathbf{x}_2-\mathbf{x}_1) .$$

Bu şu demektir: $\mathbf{x}_1$ noktasından başlayarak $\mathbf{x}_2-\mathbf{x}_1$ bağlantı okunun $t$ katı kadar gitmek. $t=0$ için $\mathbf{x}_1$ noktasında, $t=1$ için $\mathbf{x}_2$ noktasında, $t=\tfrac12$ için ortada bulunulur. $0$ ile $1$ arasındaki bütün $t$ değerleri, iki noktayı birleştiren doğru parçasının noktalarını verir. Bu tür karışımlara, iki veri noktası arasında ara değerler oluşturmak gerektiğinde her zaman ihtiyaç duyulur.
:::

### Birim vektörler

<span class="anker" id="stufe-1-6"></span>

En basit vektörlerde tek bir bileşen $1$, geri kalan bileşenlerin hepsi sıfırdır. Bir örnekte bu şu anlama gelirdi: Yalnızca bir öznitelik “açıktır”, hem de $1$ değeriyle. Düzlemde bunlar eksenler boyunca uzanan, $1$ uzunluğundaki iki oktur.

:::definition Tanım 1.5 (Birim vektör)
<span class="anker" id="satz-1-5"></span>

$j$-inci __birim vektör__ $\mathbf{e}_j\in\mathbb{R}^d$ vektörünün $j$ numaralı yerinde $1$, öteki bütün yerlerinde $0$ bulunur.
:::

$\mathbb{R}^2$ uzayında $\mathbf{e}_1=(1,\,0)^{\top}$ ve $\mathbf{e}_2=(0,\,1)^{\top}$ olur. Her vektör birim vektörlerin bir doğrusal bileşimidir ve katsayılar tam olarak onun bileşenleridir:

<span class="anker" id="gl-1-6"></span>
$$\mathbf{x}=x_1\mathbf{e}_1+x_2\mathbf{e}_2+\dots+x_d\mathbf{e}_d=\sum_{j=1}^d x_j\,\mathbf{e}_j . \tag{1.6}$$

Bunu görmek için sağ taraf bileşen bileşen hesaplanır: $j$ numaralı yere yalnızca $x_j\mathbf{e}_j$ terimi bir katkı yapar, o da $x_j\cdot1$ kadardır. Başka katsayılar mümkün değildir, çünkü bunlar bir yerde başka bir sayı verirdi.

::::beispiel [Sayısal örnek]
$\mathbf{x}_1=(60,\,2,\,3)^{\top}=60\,\mathbf{e}_1+2\,\mathbf{e}_2+3\,\mathbf{e}_3$, yani $60$ kez “bir metrekare” artı $2$ kez “bir oda” artı $3$ kez “bir kilometre”.
::::

⁠**Kısacası:** $\mathbf{e}_j$ birim vektörünün yalnızca $j$ numaralı bileşeni bire, öteki bütün bileşenleri sıfıra eşittir; her vektör $\sum_jx_j\mathbf{e}_j$ toplamıdır.

:::aufgabe Alıştırma 1 ★ Toplamları okumak ve yazmak
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

$\sum_{i=1}^{5}(2i-1)$ ve $\sum_{i=1}^{2}\sum_{j=1}^{3}i\,j$ toplamlarını hesaplayın.

</li>

<li>

$3+6+9+12$ toplamını bir toplam sembolüyle yazın.

</li>

<li>

$a_i$, $i$ numaralı dairenin alanı olsun (Tablo [1](#tab-1)). $\sum_{i=1}^4a_i$ ve $\frac14\sum_{i=1}^4a_i$ ne anlama gelir ve hangi sayılar çıkar?

</li>

</ol>

:::loesung
(a) $i$ toplam indisi $1$'den $5$'e kadar değerler alır; toplanan terimler $1,3,5,7,9$ tek sayılarıdır:

$$\sum_{i=1}^{5}(2i-1)=1+3+5+7+9=25 .$$

Çift toplamda her sabit $i$ için iç toplam $\sum_{j=1}^3i\,j=i\,(1+2+3)=6i$ olur; $i$ çarpanı $j$ indisine bağlı değildir ve [(1.2)](#gl-1-2) uyarınca iç toplamın önüne alınabilir. Ardından $\sum_{i=1}^2 6i=6+12=18$ olur.

(b) Toplanan terimler $3$'ün katlarıdır: $3+6+9+12=\sum_{i=1}^43i$. Ortak çarpan kuralı uyarınca $3\sum_{i=1}^4i$ yazmak da aynı ölçüde doğrudur.

(c) $\sum_{i=1}^4a_i=60+40+90+70=260$, dört dairenin hepsinin $\mathrm m^2$ cinsinden toplam alanıdır; $\frac14\sum_{i=1}^4a_i=65$ ise bir dairenin ortalama alanıdır.
:::
:::

:::aufgabe Alıştırma 2 ★ Vektörlerle hesap
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

$\mathbf{u}=(1,\,-1,\,0)^{\top}$ ve $\mathbf{v}=(0,\,1,\,2)^{\top}$ için $2\mathbf{u}-3\mathbf{v}$ vektörünü hesaplayın.

</li>

<li>

$(4,\,-1,\,2)^{\top}$ vektörünü $\mathbb{R}^3$ uzayının birim vektörlerinin doğrusal bileşimi olarak yazın.

</li>

<li>

$c_1(1,\,2)^{\top}+c_2(2,\,1)^{\top}=(3,\,3)^{\top}$ eşitliğini sağlayan $c_1,c_2$ sayılarını bulun. Çözümü oklarla çizin.

</li>

<li>

Daire veri kümesi için $\mathbf{x}_3-\mathbf{x}_2$ vektörünü hesaplayın ve bu vektörün ne söylediğini sözcüklerle anlatın.

</li>

</ol>

:::loesung
(a) Bileşen bileşen: $2\mathbf{u}=(2,\,-2,\,0)^{\top}$ ve $3\mathbf{v}=(0,\,3,\,6)^{\top}$, dolayısıyla $2\mathbf{u}-3\mathbf{v}=(2,\,-5,\,-6)^{\top}$.

(b) [(1.6)](#gl-1-6) uyarınca katsayılar bileşenlerin kendisidir: $(4,\,-1,\,2)^{\top}=4\,\mathbf{e}_1-\mathbf{e}_2+2\,\mathbf{e}_3$.

(c) Bileşen bileşen yazılınca koşul $c_1+2c_2=3$ ve $2c_1+c_2=3$ olur. Birinci denklem ikinci denklemden iki kez çıkarılınca $-3c_2=-3$ kalır; dolayısıyla $c_2=1$, ardından da $c_1=1$ bulunur. Sağlama: $(1,\,2)^{\top}+(2,\,1)^{\top}=(3,\,3)^{\top}$. Çizimde $(2,\,1)^{\top}$ oku $(1,\,2)^{\top}$ okunun ucuna eklenir ve $(3,\,3)^{\top}$ noktasına varılır.

(d) $\mathbf{x}_3-\mathbf{x}_2=(90-40,\ 4-1,\ 6-1)^{\top}=(50,\,3,\,5)^{\top}$: Daire 3, Daire 2'den $50\,\mathrm m^2$ daha büyüktür, üç odası daha fazladır ve merkeze $5$ km daha uzaktır. Vektör, $\mathbf{x}_2$ noktasından $\mathbf{x}_3$ noktasına giden oktur.
:::
:::

:::aufgabe Alıştırma 3 ★ Kendi veri kümeniz
<span class="anker" id="aufg-3"></span>

Gündelik hayatınızdan dört nesne seçin, örneğin yiyecekler, bisikletler ya da şarkılar, ve her nesne için sayıyla verebileceğiniz üç özellik belirleyin. Değerleri ölçün ya da araştırın.

<ol class="al">

<li>

Tabloyu oluşturun. $N$ ve $d$ nedir? İkinci örneği $\mathbf{x}_2$ vektörü olarak yazın.

</li>

<li>

Sizi de ilgilendirecek ama sayı olmayan hangi özellik var? Bu özellik sayılara nasıl çevrilebilir?

</li>

<li>

Örneklerin ortalaması olan $\bar{\mathbf{x}}$ vektörünü hesaplayın. Tam olarak böyle görünen bir nesne var mı?

</li>

</ol>

:::loesung
Olası bir çözüm: öznitelikleri g cinsinden kütle, cm cinsinden çap ve sent cinsinden fiyat olan dört elma.

(a) Tablonun satırları $(180;\ 7{,}5;\ 45)$, $(150;\ 7{,}0;\ 40)$, $(210;\ 8{,}0;\ 55)$ ve $(165;\ 7{,}2;\ 40)$ olsun. O zaman $N=4$, $d=3$ ve $\mathbf{x}_2=(150;\ 7{,}0;\ 40)^{\top}$ olur. Önemli olan yalnızca her nesnenin aynı üç öznitelikle ve aynı sırayla tanımlanmasıdır.

(b) Elmanın çeşidi bir addır, sayı değildir. Her çeşit için ayrı bir öznitelik tanımlanarak sayılara çevrilebilir: Elma o çeşittense bu öznitelik $1$, değilse $0$ olur. Buna karşılık çeşitleri sırayla numaralandırmak çoğu zaman iyi bir fikir değildir: Numaralar, çeşitler arasında aslında olmayan bir sıra ve uzaklıklar varmış izlenimi verir.

(c) Örneklerin ortalaması bileşen bileşen alınan ortalamadır, burada $\bar{\mathbf{x}}=(176{,}25;\ 7{,}425;\ 45)^{\top}$. Tabloda tam olarak bu değerlere sahip bir elma yoktur. Ortalama ölçülmüş değil, düşünülmüş bir örnektir; oda sayısı gibi bir özellikte gerçek hiçbir nesnenin alamayacağı bir değer bile olabilir, örneğin $2{,}5$ oda.
:::
:::
