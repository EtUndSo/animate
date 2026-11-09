---
title: İç çarpım
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
knoten: Temeller 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15210300
summary: Bileşen sayısı aynı olan iki vektörün bileşenleri ikişer ikişer çarpılıp toplanırsa tek bir sayı elde edilir.
tags: iç çarpımı, ağırlığı, ağırlıklı toplam, model, tahmini, Birler vektörü, ortalaması
lang: tr
---

<span class="anker" id="stufe-2"></span>

:::zweck
Bileşen sayısı aynı olan iki vektörün bileşenleri ikişer ikişer çarpılıp toplanırsa tek bir sayı elde edilir. Bu hesap bütün makine öğrenmesinde en sık yapılan hesaptır: Ölçüm değerlerinden bir tahmin üretir ve verileri bir örüntüyle karşılaştırır.
:::

### İki vektörün iç çarpımı

<span class="anker" id="stufe-2-1"></span>

Bir alışveriş hesabı şöyle yapılır: Her ürün için miktar çarpı fiyat, sonra hepsi toplanır. Herhangi iki vektörle yapılan aynı hesaba iç çarpım denir.

Bu hesap bir satırla bir sütunun karşılaşması olarak düşünülebilir. Birinci vektör satır olarak, ikincisi onun yanına sütun olarak yazılır. Sonra satırın birinci elemanı sütunun birinci elemanıyla, ikincisi ikincisiyle çarpılır, bu böyle sürer ve hepsi toplanır:

$$\begin{pmatrix}1&2&3\end{pmatrix}\begin{pmatrix}4\\-1\\2\end{pmatrix}=1\cdot4+2\cdot(-1)+3\cdot2=8 .$$

:::definition Tanım 2.1 (İç çarpım)
<span class="anker" id="satz-2-1"></span>

İki $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ vektörünün __iç çarpımı__ şu sayıdır:

<span class="anker" id="gl-2-1"></span>
$$\mathbf{u}^{\top}\mathbf{v}=\sum_{j=1}^{d}u_j\,v_j=u_1v_1+u_2v_2+\dots+u_dv_d . \tag{2.1}$$
:::

$\mathbf{u}^{\top}\mathbf{v}$ yazılışı ne olduğunu tam olarak söyler: $\mathbf{u}^{\top}$, satır olarak yazılmış $\mathbf{u}$ vektörüdür ve bu satır $\mathbf{v}$ sütunuyla karşılaşır. Sonuç bir skalerdir; bu yüzden iç çarpıma skaler çarpım da denir.

:::satz Teorem 2.2 (İç çarpımın hesap kuralları)
<span class="anker" id="satz-2-2"></span>

Bütün $\mathbf{u},\mathbf{v},\mathbf{q}\in\mathbb{R}^d$ vektörleri ve her $c$ skaleri için şunlar geçerlidir:

<ol class="rm">

<li>

$\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$ (simetrik);

</li>

<li>

$(c\,\mathbf{u})^{\top}\mathbf{v}=c\,(\mathbf{u}^{\top}\mathbf{v})$ ve $(\mathbf{u}+\mathbf{q})^{\top}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}+\mathbf{q}^{\top}\mathbf{v}$ (doğrusal, ikinci vektörde de aynı biçimde);

</li>

<li>

$\mathbf{u}^{\top}\mathbf{u}=\sum_ju_j^2\ge0$ ve $\mathbf{u}^{\top}\mathbf{u}=0$ yalnızca $\mathbf{u}=\mathbf{0}$ için.

</li>

</ol>
:::

:::beweis İç çarpımın hesap kuralları
(i) her bileşen için $u_jv_j=v_ju_j$ olmasından çıkar. (ii) [(1.2)](vektoren-daten-als-zahlenlisten.html#gl-1-2) toplam kuralıdır: $\sum_j(c\,u_j)v_j=c\sum_ju_jv_j$ ve $\sum_j(u_j+q_j)v_j=\sum_ju_jv_j+\sum_jq_jv_j$. (iii) Her $u_j^2$ terimi negatif değildir. Toplam ancak her terim sıfırsa, yani her $u_j=0$ ise sıfırdır.
:::

⁠**Sayısal örnek:** $\mathbf{u}=(1,\,2,\,3)^{\top}$ ve $\mathbf{v}=(4,\,-1,\,2)^{\top}$ için $\mathbf{u}^{\top}\mathbf{v}=8$ ve $\mathbf{u}^{\top}\mathbf{u}=14$ bulunur (Şekil [6](#abb-6)). Ters sırada da aynı sayı çıkar, $\mathbf{v}^{\top}\mathbf{u}=4\cdot1+(-1)\cdot2+2\cdot3=8$; simetri de bunu gerektirir.

:::abbildung ml/k1rskp 6
Adım adım iki iç çarpım: bileşen çarpı bileşen, sonra çarpımların toplamı. Bir vektörün kendisiyle iç çarpımı, bileşenlerinin karelerinin toplamıdır.
:::

⁠**Kısacası:** İç çarpım iki vektörü bileşen bileşen çarpar ve çarpımları toplar; sonuç bir sayıdır.

:::hintergrund Aynı şey için başka yazılışlar
Birçok kitapta $\mathbf{u}^{\top}\mathbf{v}$ yerine $\mathbf{u}\cdot\mathbf{v}$ ya da $\langle\mathbf{u},\mathbf{v}\rangle$ yazılır; İngilizcede buna *dot product* ya da *inner product* denir. Kastedilen aynı sayıdır. Bu seri $\mathbf{u}^{\top}\mathbf{v}$ yazar, çünkü bu yazılışta bir satırın bir sütunla karşılaştığı görülür. Bu, sayı tabloları devreye girer girmez işe yarar.
:::

### Ağırlıklar ve ağırlıklı toplamlar

<span class="anker" id="stufe-2-2"></span>

Bir emlakçı bir dairenin fiyatını kafasından aşağı yukarı şöyle tahmin eder: Her metrekare yaklaşık $3$ bin avro eder, her oda $10$ bin avro daha katar ve merkezden uzaklığın her kilometresi $4$ bin avro düşürür. Yani her özniteliği kendine ait bir çarpanla alır ve hepsini toplar.

Bir özniteliğin böyle bir hesaba girdiği sayıya o özniteliğin __ağırlığı__ denir. Büyük pozitif bir ağırlık şu demektir: Bu özniteliğin her birimi sonucu çok artırır. Negatif bir ağırlık şu demektir: Öznitelik sonucu düşürür.

:::definition Tanım 2.3 (Ağırlıklı toplam)
<span class="anker" id="satz-2-3"></span>

Bir $\mathbf{w}=(w_1,\dots,w_d)^{\top}$ ağırlık vektörü ve bir $\mathbf{x}\in\mathbb{R}^d$ örneği için __ağırlıklı toplam__ şudur:

<span class="anker" id="gl-2-2"></span>
$$\hat y=\mathbf{w}^{\top}\mathbf{x}=\sum_{j=1}^{d}w_j\,x_j . \tag{2.2}$$
:::

Bir örneğin özniteliklerinden bir sayı hesaplayan sabit bir hesap kuralına __model__ denir. Modelin bir örnek için verdiği sayıya onun __tahmini__ denir. $\hat y$ içinde $y$ harfinin üstündeki şapka, bunun ölçülmüş bir değer değil, hesaplanmış bir tahmin değeri olduğunu gösterir. Bu bölümde ağırlıklar her zaman verilmiştir; iyi ağırlıkların nereden geldiği ayrı bir sorudur.

⁠**Sayısal örnek:** Emlakçı metrekare, oda ve kilometre başına bin avro cinsinden $\mathbf{w}=(3,\,10,\,-4)^{\top}$ ağırlıklarını kullanır. Daire 1 için $\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$ bulunur (Şekil [7](#abb-7)), yani $188$ bin avro.

:::abbildung ml/k1rgewicht 7
Emlakçının Daire 1 için tahmini: her öznitelik çarpı ağırlığı, sonra toplam. Üç özniteliğin katkıları $180$, $20$ ve $-12$ bin avrodur.
:::

Öteki daireler için de aynı biçimde $\hat y_2=126$, $\hat y_3=286$ ve $\hat y_4=232$ bulunur. Her $w_jx_j$ çarpımının birimi bin avrodur, çünkü özniteliğin birimi ağırlığın paydasındaki birimle sadeleşir. Üç çarpım ancak bu yüzden toplanabilir.

⁠**Kısacası:** Ağırlıklı toplam, ağırlıklarla özniteliklerin $\mathbf{w}^{\top}\mathbf{x}$ iç çarpımıdır; özniteliklerden bir tahmin üreten en basit modeldir.

:::hintergrund Büyük bir ağırlık, özniteliğin önemli olduğu anlamına gelmez
Emlakçının modelinde odaların ağırlığı ($10$), alanın ağırlığının ($3$) üç katından fazladır. Yine de Daire 1'de alan $180$ bin avro katkı yapar, oda sayısı ise yalnızca $20$. Nedeni şu: Ağırlık özniteliğin birimi başına geçerlidir ve alanın birimi çoktur. Alan $10\,\mathrm m^2$ büyüklüğündeki birimlerle ölçülürse Daire 1 yalnızca $6$ birim büyüklüğündedir ve aynı model $10\,\mathrm m^2$ başına $30$ bin avroluk bir ağırlık gerektirir. Tahmin aynı kalır, yalnızca ağırlık on katına çıkmıştır. Demek ki bir ağırlığın ne kadar büyük olduğu seçilen birime bağlıdır. Bir özniteliğin tahmine ne kadar katkı yaptığını bilmek isteyen, yalnızca ağırlığa değil, $w_jx_j$ çarpımına bakmalıdır.
:::

### İç çarpım olarak toplam ve ortalama

<span class="anker" id="stufe-2-3"></span>

Gündelik hesapların çoğu, ikinci vektörü özellikle basit olan iç çarpımlardır. En sık gerekenler bütün bileşenlerin toplamı ve ortalamasıdır.

__Birler vektörü__ $\mathbf 1\in\mathbb{R}^n$ vektörünün bütün bileşenleri birdir. Onunla iç çarpım bütün bileşenleri basitçe toplar: $\mathbf 1^{\top}\mathbf{v}=v_1+\dots+v_n$.

:::definition Tanım 2.4 (Ortalama)
<span class="anker" id="satz-2-4"></span>

Bir $\mathbf{v}\in\mathbb{R}^n$ vektörünün bileşenlerinin __ortalaması__ şudur:

<span class="anker" id="gl-2-3"></span>
$$\bar v=\frac1n\sum_{i=1}^nv_i=\frac1n\,\mathbf 1^{\top}\mathbf{v} . \tag{2.3}$$
:::

Bu türden başka hesaplar: Bir birim vektörle iç çarpım bir bileşeni seçer, $\mathbf{e}_j^{\top}\mathbf{v}=v_j$, çünkü öteki bütün çarpımlar bir sıfır içerir. Bir vektörün kendisiyle iç çarpımı karelerin toplamıdır, $\mathbf{v}^{\top}\mathbf{v}=\sum_iv_i^2$. Miktarlar çarpı fiyatlar toplanınca fatura tutarını verir. Ve bir $p(t)=c_1+c_2t+\dots+c_nt^{n-1}$ polinomunu bir $t$ noktasında hesaplamak, $\mathbf{c}^{\top}\mathbf{z}$ iç çarpımını almak demektir; burada $\mathbf{c}=(c_1,\dots,c_n)^{\top}$ polinomun katsayılarını, $\mathbf{z}=(1,\,t,\,t^2,\dots,t^{n-1})^{\top}$ ise kuvvetleri içerir. $p(t)=1+2t+3t^2$ için $t=2$ noktasında bu, $(1,\,2,\,3)\,(1,\,2,\,4)^{\top}=1+4+12=17$ olur.

⁠**Sayısal örnek:** Daire 1 ocak, şubat ve mart aylarında $\mathbf{u}=(200,\,250,\,300)^{\top}$ kWh elektrik tüketmiştir (alt kesim [1.4](vektoren-daten-als-zahlenlisten.html#stufe-1-4)). Toplam tüketim $\mathbf 1^{\top}\mathbf{u}=750$ kWh, aylık ortalama $\bar u=250$ kWh olur (Şekil [8](#abb-8)). Şubat ayındaki tüketim $\mathbf{e}_2^{\top}\mathbf{u}=250$ kWh olur.

:::abbildung ml/k1rmittel 8
Elektrik tüketiminin toplamı ve ortalaması, birler vektörüyle iç çarpım olarak, kWh cinsinden.
:::

Kilovatsaatin fiyatı üç ayda $\mathbf{p}=(0{,}32;\ 0{,}34;\ 0{,}28)^{\top}$ avro ise elektrik faturası fiyatlarla miktarların iç çarpımıdır: $\mathbf{p}^{\top}\mathbf{u}=233$ avro (Şekil [9](#abb-9)). Her $p_ju_j$ çarpımı bir ayın tutarıdır; birimi kWh başına avro çarpı kWh, yani avrodur.

:::abbildung ml/k1rstrom 9
İç çarpım olarak elektrik faturası: her ay için fiyat çarpı miktar, sonra toplam, avro cinsinden.
:::

⁠**Kısacası:** Toplam, ortalama, bir bileşenin seçilmesi ve kareler toplamı; $\mathbf 1$, $\tfrac1n\mathbf 1$, $\mathbf{e}_j$ ve vektörün kendisiyle alınan iç çarpımlardır.

### Örüntü karşılaştırması olarak iç çarpım

<span class="anker" id="stufe-2-4"></span>

Bir ölçüm sinyalinin bir örnek değerden ötekine ileri geri sıçrayıp sıçramadığı denetlenmek isteniyor. Bunun için aranan örüntü bir vektör olarak yazılır, burada $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$, ve sinyalle iç çarpımı alınır.

Bu sırada ne olduğunu Şekil [10](#abb-10) gösteriyor. Her örnek değer, aynı yerdeki örüntü değeriyle çarpılır. Sinyalin bir yerdeki işareti örüntününkiyle aynıysa çarpım pozitiftir; ters işaretliyse negatiftir. Sinyal her yerde örüntüyü izliyorsa yalnızca pozitif katkılar birikir ve büyük bir toplam oluşur. Sinyalin örüntüyle bir ilgisi yoksa pozitif ve negatif katkılar birbirini götürür.

:::abbildung ml/k1muster 10
İç çarpımla örüntü karşılaştırması. Üstte $\mathbf{w}=(1,-1,1,-1)^{\top}$ örüntüsü, ortada iki sinyal, altta her $j$ yerindeki $w_j\,x_j$ çarpımları. Solda $\mathbf{x}=(2,-1,3,-2)^{\top}$ sinyali örüntüyle aynı tempoda sıçrar: Bütün çarpımlar pozitiftir, toplam $8$ olur. Sağda $\mathbf{x}'=(2,2,3,3)^{\top}$ düzgün biçimde artar: Çarpımlar birbirini götürür, toplam $0$ olur.
:::

Kesin söylemek gerekirse: $j$ yerinin $\mathbf{w}^{\top}\mathbf{x}$ iç çarpımına katkısı $w_jx_j$ çarpımıdır. $w_j$ ile $x_j$ aynı işaretliyse bu katkı pozitif, ters işaretliyse negatiftir. İşaretlerin uyuştuğu yerlerdeki mutlak değerler ne kadar büyükse iç çarpım da o kadar büyüktür.

Bu hesap sinyal işlemeden korelasyon olarak bilinir. İki gerçel $x[n]$ ve $y[n]$ dizisinin sıfır kaydırmadaki çapraz ilintisi $\sum_nx[n]\,y[n]$ toplamıdır. Sonlu uzunluktaki iki sinyalin örnek değerleri $\mathbf{x}$ ve $\mathbf{y}$ vektörleri olarak yazılırsa bu tam olarak $\mathbf{x}^{\top}\mathbf{y}$ iç çarpımıdır. Bir sinyalin enerjisi, $\sum_nx[n]^2$, aynı biçimde $\mathbf{x}^{\top}\mathbf{x}$ olur. Yani örüntü karşılaştırması yeni bir araç değildir; bir korelatörün bir sinyalde bilinen bir örüntüyü ararken kullandığı araçla aynıdır.

⁠**Sayısal örnek:** İşaret değiştiren örüntü $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$ ile $\mathbf{x}=(2,\,-1,\,3,\,-2)^{\top}$ için $\mathbf{w}^{\top}\mathbf{x}=8$, $\mathbf{x}'=(2,\,2,\,3,\,3)^{\top}$ için $\mathbf{w}^{\top}\mathbf{x}'=0$ bulunur (Şekil [11](#abb-11)). Sabit örüntü $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ ile durum tersinedir: $\mathbf 1^{\top}\mathbf{x}=2$, ama $\mathbf 1^{\top}\mathbf{x}'=10$. Yani $\mathbf{x}$ büyük ölçüde işaret değiştiren, $\mathbf{x}'$ ise büyük ölçüde sabit kalan bir sinyaldir.

:::abbildung ml/k1rmuster 11
İşaret değiştiren örüntü $\mathbf{w}$ ve iki sinyal. Üstte $\mathbf{x}$ örüntüyü izler: Dört çarpımın hepsi pozitiftir. Altta $\mathbf{x}'$ düzgün biçimde artar: Çarpımlar ikişer ikişer birbirini götürür.
:::

Emlakçının ağırlıklı toplamı da bir örüntü karşılaştırmasıdır. Onun $\mathbf{w}=(3,\,10,\,-4)^{\top}$ örüntüsü bir daireyi neyin değerli kıldığını betimler: çok alan, çok oda, az uzaklık. Bir daire bu örüntüye ne kadar iyi uyarsa tahmini de o kadar yüksek olur.

⁠**Kısacası:** $\mathbf{w}^{\top}\mathbf{x}$ iç çarpımı, $\mathbf{w}$ örüntüsünün aynı işaretle büyük değerler taşıdığı yerlerde $\mathbf{x}$ de büyük değerler taşıyorsa büyüktür; iç çarpım sıfır kaydırmadaki korelasyondur.

:::hintergrund Korelasyon fonksiyonu baştan sona iç çarpımlardan oluşur
Çapraz ilinti bir sinyali bir örüntüyle yalnızca tek bir konumda değil, olası her kaydırma için karşılaştırır. Her $k$ kaydırması için değeri bir iç çarpımdır: sinyal ile $k$ adım kaydırılmış örüntünün iç çarpımı. Yani korelasyon fonksiyonunun tamamı, her kaydırma için bir tane olmak üzere bir dizi iç çarpımdır. Örüntünün sinyalde bulunduğu yerde pozitif katkılar birikir ve korelasyon fonksiyonu orada en büyük değerini alır. Bir radar alıcısı kendi darbesinin yankısını, bir radyo alıcısı da bilinen bir veri çerçevesinin başlangıcını böyle bulur. Makine öğrenmesinde kaydırma çoğunlukla sıfırda sabit kalır: Bir örnek bütün olarak bir örüntüyle karşılaştırılır.
:::

:::aufgabe Alıştırma 4 ★ Hesap kurallarını doğrulamak
<span class="anker" id="aufg-4"></span>

$\mathbf{u}=(1,\,0,\,2)^{\top}$, $\mathbf{v}=(3,\,-1,\,1)^{\top}$ ve $\mathbf{q}=(0,\,2,\,1)^{\top}$ olsun. $\mathbf{u}^{\top}\mathbf{v}$, $\mathbf{v}^{\top}\mathbf{u}$, $\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})$, $\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}$, $(3\mathbf{u})^{\top}\mathbf{v}$ ve $\mathbf{u}^{\top}\mathbf{u}$ değerlerini hesaplayın. Her karşılaştırma hangi hesap kuralını gösteriyor?

:::loesung
$\mathbf{u}^{\top}\mathbf{v}=3+0+2=5$ ve $\mathbf{v}^{\top}\mathbf{u}=3+0+2=5$ olur: İç çarpım simetriktir, (i) kuralı. $\mathbf{v}+\mathbf{q}=(3,\,1,\,2)^{\top}$ ile $\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})=3+0+4=7$ ve $\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}=5+(0+0+2)=7$ olur: ikinci vektörde doğrusallık, (ii) kuralı. Ayrıca $(3\mathbf{u})^{\top}\mathbf{v}=(3,0,6)\,(3,-1,1)^{\top}=9+0+6=15=3\cdot5$; bu da (ii) kuralıdır. Son olarak $\mathbf{u}^{\top}\mathbf{u}=1+0+4=5>0$ olur; (iii) kuralı da $\mathbf{u}\ne\mathbf{0}$ için bunu gerektirir.
:::
:::

:::aufgabe Alıştırma 5 ★★ Emlakçının tahmini
<span class="anker" id="aufg-5"></span>

$\mathbf{w}=(3,\,10,\,-4)^{\top}$ ağırlıklarını kullanın (alt kesim [2.2](#stufe-2-2)).

<ol class="al">

<li>

Dört dairenin hepsi için tahminleri hesaplayın. Tahminlerin birimi nedir?

</li>

<li>

Daire 2'ye bir duvar örülüyor; daire bundan sonra aynı alanda iki odalı oluyor. Tahmin nasıl değişir ve bu değişiklik neden alana bağlı değildir?

</li>

<li>

Bir meslektaşınız şöyle diyor: “Emlakçıda en çok odalar önemli, en büyük ağırlık onlarda.” Bu iddiayı Daire 1 üzerinde, üç $w_jx_{1j}$ katkısını karşılaştırarak sınayın.

</li>

</ol>

:::loesung
(a) Tıpkı alt kesim [2.2](#stufe-2-2) içindeki gibi: $188$, $126$, $286$ ve $232$, her biri bin avro cinsinden. Birim bin avrodur, çünkü her ağırlığın birimi “özniteliğin birimi başına bin avro” olur ve özniteliğin birimi çarpımda sadeleşir.

(b) Daire 2 artık $(40,\,2,\,1)^{\top}$ olur. Tahmin $126$ değerinden $120+20-4=136$ değerine, yani $10$ artar. Genel olarak ikinci öznitelikteki bir $\Delta x_2$ değişikliği ağırlıklı toplamı $w_2\,\Delta x_2$ kadar değiştirir, çünkü $\mathbf{w}^{\top}(\mathbf{x}+\Delta x_2\,\mathbf{e}_2)=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,\mathbf{w}^{\top}\mathbf{e}_2=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,w_2$. Öteki özniteliklerin bunda hiçbir rolü yoktur. Bu, iç çarpımın doğrusallığıdır: Her öznitelik ötekilerle etkileşmeden, kendi başına katkıda bulunur.

(c) Daire 1'deki katkılar $w_1x_{11}=180$, $w_2x_{12}=20$ ve $w_3x_{13}=-12$ olur. Açık ara en büyük katkı, ağırlığı mutlak değerce en küçük olduğu hâlde alandan gelir. Meslektaşınızın iddiası birim başına ağırlığı tahmine yapılan katkıyla karıştırıyor; alan çok sayıda birim içerir.
:::
:::

:::aufgabe Alıştırma 6 ★★ Artan sinyaller için bir örüntü
<span class="anker" id="aufg-6"></span>

Dört örnek değerli bir sinyalin artıp artmadığı denetlenmek isteniyor. Örüntü olarak $\mathbf{w}=(-3,\,-1,\,1,\,3)^{\top}$ öneriliyor.

<ol class="al">

<li>

$\mathbf{x}=(1,2,3,4)^{\top}$, $(4,3,2,1)^{\top}$, $(5,5,5,5)^{\top}$ ve $(1,3,2,4)^{\top}$ için $\mathbf{w}^{\top}\mathbf{x}$ değerini hesaplayın ve sonuçları yorumlayın.

</li>

<li>

Neden her sabit $c\,\mathbf1$ sinyali tam olarak sıfır verir? $\mathbf 1^{\top}\mathbf{w}$ çarpımını kullanın.

</li>

</ol>

:::loesung
(a) $\mathbf{w}^{\top}(1,2,3,4)^{\top}=-3-2+3+12=10$: Sinyal artıyor, sonuç açıkça pozitif. $\mathbf{w}^{\top}(4,3,2,1)^{\top}=-12-3+2+3=-10$: Sinyal azalıyor, sonuç aynı ölçüde açıkça negatif. $\mathbf{w}^{\top}(5,5,5,5)^{\top}=-15-5+5+15=0$: sabit, artış yok. $\mathbf{w}^{\top}(1,3,2,4)^{\top}=-3-3+2+12=8$: Sinyal ortada bir kez geri düşse de genel olarak artıyor ve sonuç düzgün artıştakinden biraz küçük. Örüntü erken değerleri negatif, geç değerleri pozitif ağırlıklandırır; yani geç değerlerin erken değerlerden büyük olup olmadığına tepki verir.

(b) $\mathbf 1^{\top}\mathbf{w}=-3-1+1+3=0$. Bu yüzden sabit bir sinyal için $\mathbf{w}^{\top}(c\,\mathbf 1)=c\,\mathbf{w}^{\top}\mathbf 1=c\cdot0=0$ olur. Ağırlıkların toplamı sıfır olduğundan örüntü ortak bir sabit bileşeni tamamen yok sayar: Yalnızca örnek değerler arasındaki farkları ölçer.
:::
:::
