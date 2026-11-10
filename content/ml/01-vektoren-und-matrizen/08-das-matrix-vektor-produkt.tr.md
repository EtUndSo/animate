---
title: Matris-vektör çarpımı
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Bölüm 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15210800
summary: Aynı ağırlıklı toplam bir veri kümesinin bütün örnekleri için hesaplanmak isteniyor.
tags: matris-vektör çarpımı, sütun uzayı
lang: tr
---

<span class="anker" id="stufe-7"></span>

:::zweck
Aynı ağırlıklı toplam bir veri kümesinin bütün örnekleri için hesaplanmak isteniyor. Bu kesim bunun için matris ile vektörün çarpımını tanıtıyor ve bu çarpımı okumanın iki yolunu gösteriyor: satır satır ya da sütun sütun.
:::

### Matris çarpı vektör

<span class="anker" id="stufe-7-1"></span>

Emlakçı (alt kesim [2.2](das-skalarprodukt.html#stufe-2-2)) her daireyi aynı ağırlıklı toplamla tahmin eder. Dört daire için dört kez $\mathbf{w}^{\top}\mathbf{x}_i$ hesaplar. Daireler bir matrisin satırları olarak yazılırsa dört hesabın hepsi tek adımda ifade edilebilir: Matrisin her satırı aynı vektörle çarpılır.

:::definition Tanım 7.1 (Matris-vektör çarpımı)
<span class="anker" id="satz-7-1"></span>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ ve $\mathbf{x}\in\mathbb{R}^n$ için $\mathbf{A}\mathbf{x}$ __matris-vektör çarpımı__, bileşenleri şunlar olan $\mathbb{R}^m$ uzayındaki vektördür:

<span class="anker" id="gl-7-1"></span>
$$(\mathbf{A}\mathbf{x})_i=\sum_{j=1}^{n}a_{ij}\,x_j=a_{i1}x_1+a_{i2}x_2+\dots+a_{in}x_n ,\qquad i=1,\dots,m . \tag{7.1}$$
:::

Çarpım ancak $\mathbf{x}$ vektörünün bileşen sayısı $\mathbf{A}$ matrisinin sütun sayısına eşitse tanımlıdır. Sonucun bileşen sayısı $\mathbf{A}$ matrisinin satır sayısına eşittir. Toplamlar için hesap kurallarından şu çıkar: $\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ ve $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$.

::::beispiel [Sayısal örnek]
$$\mathbf{A}=\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\quad\text{ve}\quad \mathbf{x}=\begin{pmatrix}2\\1\end{pmatrix}\qquad\text{için}\qquad \mathbf{A}\mathbf{x}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$

Her bileşen [(7.1)](#gl-7-1) uyarınca bir toplamdır (Şekil [28](#abb-28)). $3\times2$ tipinde bir matris çarpı $2$ bileşenli bir vektör, $3$ bileşenli bir vektör verir.

:::abbildung ml/k1rmv 28
Bileşen bileşen matris-vektör çarpımı: Her $i$ satırı için $a_{ij}$ elemanları karşılık gelen $x_j$ bileşenleriyle çarpılır ve toplanır.
:::
::::

⁠**Kısacası:** $\mathbf{A}\mathbf{x}$ çarpımı, $i$ numaralı bileşeni $\sum_ja_{ij}x_j$ toplamı olan vektördür; $m\times n$ tipinde bir matris $\mathbb{R}^n$ uzayındaki bir vektörü $\mathbb{R}^m$ uzayındaki bir vektöre dönüştürür.

### Satır bakışı: birçok iç çarpım

<span class="anker" id="stufe-7-2"></span>

[(7.1)](#gl-7-1) formülü her bileşen için şunu söyler: Matrisin $i$ numaralı satırı eleman eleman $\mathbf{x}$ ile çarpılır ve toplanır. Bu, $i$ numaralı satırın $\mathbf{x}$ ile iç çarpımıdır (Şekil [30](#abb-30), sol).

:::satz Teorem 7.2 (Satır bakışı)
<span class="anker" id="satz-7-2"></span>

$\mathbf{A}\mathbf{x}$ vektörünün $i$ numaralı bileşeni, $\mathbf{A}$ matrisinin $i$-inci satırının $\mathbf{x}$ ile iç çarpımıdır. Satırları $\mathbf{x}_i^{\top}$ olan bir $\mathbf{X}$ veri matrisi ve bir $\mathbf{w}$ ağırlık vektörü için bu şu demektir:

<span class="anker" id="gl-7-2"></span>
$$\mathbf{X}\mathbf{w}=\begin{pmatrix}\mathbf{x}_1^{\top}\mathbf{w}\\\vdots\\\mathbf{x}_N^{\top}\mathbf{w}\end{pmatrix}. \tag{7.2}$$
:::

Yani matris-vektör çarpımı, $\mathbf{w}$ ağırlıklarıyla ağırlıklı toplamı bütün örneklere aynı anda uygular ve bütün tahminlerin vektörünü verir. Örüntü karşılaştırması resminde: Her örnek aynı $\mathbf{w}$ örüntüsüyle karşılaştırılır.

::::beispiel [Sayısal örnek]
Daire veri kümesi ve $\mathbf{w}=(3,\,10,\,-4)^{\top}$ için şu bulunur:

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3\\10\\-4\end{pmatrix}=\begin{pmatrix}188\\126\\286\\232\end{pmatrix},$$

yani emlakçının bin avro cinsinden dört tahmini. Her bileşen bir satırın $\mathbf{w}$ ile iç çarpımıdır (Şekil [29](#abb-29)).

:::abbildung ml/k1rzeilen 29
Emlakçı için satır bakışı: her daire, yani $\mathbf{X}$ matrisinin her satırı, çarpı $\mathbf{w}$ ağırlıkları.
:::
::::

⁠**Kısacası:** Satır bakışında $\mathbf{A}\mathbf{x}$, her satır için bir tane olmak üzere bir iç çarpımlar listesidir; $\mathbf{X}\mathbf{w}$ bütün örnekler için tahminlerdir.

:::hintergrund Bir matris-vektör çarpımı ne kadar hesap gerektirir?
$m$ bileşenin her biri $n$ çarpma ve $n-1$ toplama gerektirir. Bunlar toplam $m(2n-1)$, yani yaklaşık $2mn$ temel aritmetik işlem eder. Üç öznitelikli dört daire için bu sayı $4\cdot5=20$ olur. Bir milyon örnekli ve yüz öznitelikli bir veri kümesi için yaklaşık $2\cdot10^8$ olur. Bugünkü bir işlemci saniyede birkaç milyar böyle işlem yapar; demek ki bu büyüklükte tek bir matris-vektör çarpımı çabucak biter. Ama bu tür sayımlar hesap süresinin yalnızca büyüklük mertebesini verir, çünkü bir bilgisayarın gerçekte ne kadar hızlı olduğu, sayıları bellekten ne kadar hızlı alabildiğine de bağlıdır.
:::

### Sütun bakışı: sütunların bir doğrusal bileşimi

<span class="anker" id="stufe-7-3"></span>

Aynı toplam başka biçimde de düzenlenebilir. Satır satır ilerlemek yerine önce $x_1$ ile ilgili bütün katkılar, sonra $x_2$ ile ilgili bütün katkılar toplanır ve bu böyle sürer. $x_j$ ile ilgili katkıların hepsi matrisin $j$ numaralı sütununda durur. Böylece çarpım sütunların bir doğrusal bileşimine dönüşür (Şekil [30](#abb-30), sağ).

:::abbildung ml/k1zeilenspalten 30
$\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ ve $\mathbf{x}=(2,\,1)^{\top}$ için $\mathbf{A}\mathbf{x}$ çarpımını okumanın iki yolu. Solda satır bakışı: Sonucun $1$ numaralı bileşeni birinci satırın $\mathbf{x}$ ile iç çarpımıdır. Sağda sütun bakışı: $\mathbf{A}\mathbf{x}$ çarpımı, $2$ kez birinci sütun $\mathbf{a}_1=(2,1)^{\top}$ artı $1$ kez ikinci sütun $\mathbf{a}_2=(1,1)^{\top}$ olur.
:::

:::satz Teorem 7.3 (Sütun bakışı)
<span class="anker" id="satz-7-3"></span>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisinin sütunları $\mathbf{a}_1,\dots,\mathbf{a}_n$ ise şu geçerlidir:

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+x_2\mathbf{a}_2+\dots+x_n\mathbf{a}_n=\sum_{j=1}^nx_j\,\mathbf{a}_j . \tag{7.3}$$

Matris-vektör çarpımı, $\mathbf{A}$ matrisinin sütunlarının, katsayıları $\mathbf{x}$ vektörünün bileşenleri olan doğrusal bileşimidir.
:::

:::beweis Sütun bakışı
Sağ tarafın $i$ numaralı bileşeni $\sum_jx_j\,(\mathbf{a}_j)_i=\sum_jx_j\,a_{ij}$ olur, çünkü $\mathbf{a}_j$ sütununun $i$-inci bileşeni $a_{ij}$ elemanıdır. Bu, [(7.1)](#gl-7-1) uyarınca tam olarak $\mathbf{A}\mathbf{x}$ vektörünün $i$ numaralı bileşenidir.
:::

::::beispiel [Sayısal örnek 1]
Daha önceki $\mathbf{A}\mathbf{x}$ çarpımı (alt kesim [7.1](#stufe-7-1)) için şu bulunur:

$$\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\begin{pmatrix}2\\1\end{pmatrix}=2\begin{pmatrix}1\\0\\3\end{pmatrix}+1\begin{pmatrix}2\\-1\\1\end{pmatrix}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$
::::

::::beispiel [Sayısal örnek 2]
Emlakçının tahminleri, $3$ kez alanların sütunu artı $10$ kez odaların sütunu artı $(-4)$ kez uzaklıkların sütunudur (Şekil [31](#abb-31)). Burada $\mathbf{X}$ matrisinin sütunlarına, daha önce olduğu gibi (alt kesim [6.1](matrizen-und-die-datenmatrix.html#stufe-6-1)), $\mathbf{a}_1$, $\mathbf{a}_2$, $\mathbf{a}_3$ denir. Bu biçimde her tahminin hangi kısmının hangi öznitelikten geldiği görülür: Birinci terim alanın katkılarını, ikincisi odalarınkini, üçüncüsü uzaklığınkini içerir.

:::abbildung ml/k1rspalten 31
Emlakçı için sütun bakışı: $\mathbf{X}$ matrisinin her $\mathbf{a}_j$ sütunu kendi $w_j$ ağırlığıyla çarpılır, sonra üç vektör toplanır.
:::
::::

⁠**Kısacası:** Sütun bakışında $\mathbf{A}\mathbf{x}$ çarpımı, $\mathbf{A}$ matrisinin sütunlarının bir doğrusal bileşimidir; $\mathbf{x}$ vektörünün bileşenleri her sütundan ne kadar alınacağını söyler.

:::hintergrund Aynı hesaba neden iki bakış var?
İki bakış da aynı $m\cdot n$ tane $a_{ij}x_j$ çarpımını hesaplar ve toplar. Satır bakışı bunları önce satır satır, sütun bakışı önce sütun sütun bir araya getirir; terim sayısı sonlu olduğunda sıra önemsizdir, tıpkı çift toplamda olduğu gibi (alt kesim [1.1](vektoren-daten-als-zahlenlisten.html#stufe-1-1)). Ama her bakış başka bir soruya cevap verir. Satır bakışı şunu sorar: $i$ numaralı bileşende ne çıkar? Sütun bakışı şunu sorar: $\mathbf{x}$ serbestçe seçilirse matris hangi sonuçları verebilir? İkinci soru doğrudan bir sonraki kavrama götürür.
:::

### Sütun uzayı

<span class="anker" id="stufe-7-4"></span>

$\mathbf{x}$ vektörü $\mathbb{R}^n$ uzayının bütün vektörlerini dolaşırsa, sütun bakışına göre $\mathbf{A}\mathbf{x}$ çarpımı da sütunların bütün doğrusal bileşimlerini dolaşır. Bunlar genel olarak $\mathbb{R}^m$ uzayının bütün vektörleri değildir.

:::definition Tanım 7.4 (Sütun uzayı)
<span class="anker" id="satz-7-4"></span>

Bir $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisinin __sütun uzayı__, $\mathbf{x}\in\mathbb{R}^n$ olmak üzere bütün $\mathbf{A}\mathbf{x}$ vektörlerinin kümesidir, yani $\mathbf{A}$ matrisinin sütunlarının bütün doğrusal bileşimlerinin kümesidir.
:::

::::beispiel [Sayısal örnek 1]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ matrisinin sütunları $(1,\,2)^{\top}$ ve $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$ olur. Her doğrusal bileşim $(1,\,2)^{\top}$ vektörünün bir katıdır. Demek ki sonuçların iki bileşeni olmasına rağmen sütun uzayı yalnızca orijinden geçen ve $(1,\,2)^{\top}$ yönünde uzanan doğrudur. $(3,\,6)^{\top}$ vektörü bu doğru üzerindedir, $(1,\,1)^{\top}$ vektörü değildir.
::::

::::beispiel [Sayısal örnek 2]
$\mathbf{H}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ matrisi $\mathbf{H}\mathbf{x}=(x_1,\,x_2,\,x_1+x_2)^{\top}$ verir. Sütun uzayı, $\mathbb{R}^3$ uzayının üçüncü bileşeni ilk iki bileşenin toplamı olan vektörlerinden oluşur; bu, uzayda bir düzlemdir. $(1,\,2,\,3)^{\top}=\mathbf{H}\,(1,\,2)^{\top}$ vektörü bu düzlemdedir, $(1,\,1,\,1)^{\top}$ değildir, çünkü $1+1\ne1$.
::::

Bir veri matrisi için bu şu demektir: $\mathbf{X}\mathbf{w}$ tahminleri, hangi ağırlıklar seçilirse seçilsin, her zaman $\mathbf{X}$ matrisinin sütun uzayındadır. Bu özniteliklerle ancak çok belirli tahmin listeleri üretilebilir.

⁠**Kısacası:** Bir matrisin sütun uzayı bütün $\mathbf{A}\mathbf{x}$ vektörlerinin kümesidir, yani matrisin sütunlarından doğrusal bileşimle elde edilebilen her şeydir.

:::aufgabe Alıştırma 16 ★ Bir çarpıma iki bakış
<span class="anker" id="aufg-16"></span>

<ol class="al">

<li>

$\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ ve $\mathbf{x}=(1,\,3,\,-1)^{\top}$ için $\mathbf{B}\mathbf{x}$ çarpımını bir kez satır bakışıyla, bir kez sütun bakışıyla hesaplayın.

</li>

<li>

$\mathbf{B}\,(1,\,2)^{\top}$ tanımlı mıdır? Ya $\mathbf{B}\,(1,\,2,\,3)^{\top}$? Tiplerle gerekçelendirin ve tanımlıysa sonucun kaç bileşeni olduğunu belirtin.

</li>

<li>

$(2,\,0,\,2)^{\top}$ vektörü $\mathbf{H}$ matrisinin sütun uzayında mıdır (alt kesim [7.4](#stufe-7-4))? Ya $(2,\,1,\,2)^{\top}$?

</li>

</ol>

:::loesung
(a) Satır bakışı: $(1\cdot1+0\cdot3+2\cdot(-1),\ 2\cdot1+1\cdot3+0\cdot(-1))^{\top}=(-1,\,5)^{\top}$. Sütun bakışı: $1\,(1,\,2)^{\top}+3\,(0,\,1)^{\top}-1\,(2,\,0)^{\top}=(1+0-2,\ 2+3-0)^{\top}=(-1,\,5)^{\top}$.

(b) $\mathbf{B}$ matrisinin üç sütunu vardır. $\mathbf{B}\,(1,\,2)^{\top}$ tanımlı değildir, çünkü vektörün yalnızca iki bileşeni vardır. $\mathbf{B}\,(1,\,2,\,3)^{\top}$ tanımlıdır ve bileşen sayısı $\mathbf{B}$ matrisinin satır sayısına, yani ikiye eşittir: $(1+0+6,\ 2+2+0)^{\top}=(7,\,4)^{\top}$.

(c) $\mathbf{H}$ matrisinin sütun uzayı, üçüncü bileşeni ilk iki bileşenin toplamı olan vektörlerden oluşur. $(2,\,0,\,2)^{\top}$ için $2+0=2$: Evet, bu vektör $\mathbf{H}\,(2,\,0)^{\top}$ çarpımına eşittir. $(2,\,1,\,2)^{\top}$ için $2+1=3\ne2$: Hayır.
:::
:::

:::aufgabe Alıştırma 17 ★★ Aylık kira
<span class="anker" id="aufg-17"></span>

Bir kira endeksi, bir dairenin aylık kirasını metrekare, oda ve kilometre başına avro cinsinden $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$ ağırlıklarıyla tahmin ediyor.

<ol class="al">

<li>

Dört dairenin hepsi için tahmini kiraları $\mathbf{X}\mathbf{w}_{\mathrm M}$ olarak, bir kez satır bakışıyla, bir kez sütun bakışıyla hesaplayın.

</li>

<li>

Kaç çarpma ve kaç toplama yapmanız gerekti? $20$ öznitelikli $10\,000$ daire için bu kaç olurdu?

</li>

</ol>

:::loesung
(a) Satır bakışı, Daire 1 için: $12\cdot60+30\cdot2-8\cdot3=720+60-24=756$; aynı biçimde $502$, $1152$ ve $914$ avro. Sütun bakışı:

$$12\begin{pmatrix}60\\40\\90\\70\end{pmatrix}+30\begin{pmatrix}2\\1\\4\\3\end{pmatrix}-8\begin{pmatrix}3\\1\\6\\2\end{pmatrix}=\begin{pmatrix}720\\480\\1080\\840\end{pmatrix}+\begin{pmatrix}60\\30\\120\\90\end{pmatrix}-\begin{pmatrix}24\\8\\48\\16\end{pmatrix}=\begin{pmatrix}756\\502\\1152\\914\end{pmatrix}.$$

(b) Dört bileşenin her biri $3$ çarpma ve $2$ toplama gerektirir, hepsi birlikte $12+8=20$ işlem. $20$ öznitelikli $10\,000$ daire için $10\,000\cdot20=200\,000$ çarpma ve $10\,000\cdot19=190\,000$ toplama gerekir; $m=10\,000$, $n=20$ ile hepsi birlikte $390\,000\approx2mn$ işlem.
:::
:::
