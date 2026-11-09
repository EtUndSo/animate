---
title: Matris çarpımı
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
knoten: Temeller 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15211000
summary: Art arda uygulanan iki doğrusal dönüşüm yine bir doğrusal dönüşüm, yani bir matris verir.
tags: matris çarpımı, dış çarpımı
lang: tr
---

<span class="anker" id="stufe-9"></span>

:::zweck
Art arda uygulanan iki doğrusal dönüşüm yine bir doğrusal dönüşüm, yani bir matris verir. Bu kesim o matrisi belirliyor. Sonuç matris çarpımıdır ve tanımı zorunlu olarak bu sorudan çıkar.
:::

### Matris çarpımı

<span class="anker" id="stufe-9-1"></span>

Önce bir $\mathbf{x}\in\mathbb{R}^k$ vektörü bir $\mathbf{B}\in\mathbb{R}^{n\times k}$ matrisiyle dönüştürülür, sonra $\mathbf{B}\mathbf{x}\in\mathbb{R}^n$ sonucu bir $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisiyle (Şekil [33](#abb-33)). $\mathbf{x}\mapsto\mathbf{A}(\mathbf{B}\mathbf{x})$ bileşkesi doğrusaldır, çünkü iki aşamanın her biri toplamları ve katları korur. Demek ki alt kesim [8.2](lineare-abbildungen.html#stufe-8-2) içindeki teoreme göre bir matrisi vardır. Bu matrisin $l$ numaralı sütunu $\mathbf{e}_l$ vektörünün görüntüsüdür: Birinci aşama bundan $\mathbf{B}$ matrisinin $\mathbf{B}\mathbf{e}_l$ sütununu yapar, ikinci aşama bu sütunu $\mathbf{A}$ ile çarpar.

:::abbildung ml/k1hinter 33
Üstte art arda iki doğrusal dönüşüm: önce $\mathbf{B}$, sonra $\mathbf{A}$. Altta aynı dönüşüm tek adımda, tek bir $\mathbf{A}\mathbf{B}$ matrisiyle. Matris çarpımı tam olarak iki yolun aynı sonucu vereceği biçimde tanımlanmıştır.
:::

:::definition Tanım 9.1 (Matris çarpımı)
<span class="anker" id="satz-9-1"></span>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ ve $\mathbf{B}\in\mathbb{R}^{n\times k}$ için $\mathbf{A}\mathbf{B}\in\mathbb{R}^{m\times k}$ __matris çarpımı__, elemanları şunlar olan matristir:

<span class="anker" id="gl-9-1"></span>
$$(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^{n}a_{ij}\,b_{jl},\qquad i=1,\dots,m,\quad l=1,\dots,k . \tag{9.1}$$
:::

$(i,l)$ elemanı, $\mathbf{A}$ matrisinin $i$ numaralı satırının $\mathbf{B}$ matrisinin $l$ numaralı sütunuyla iç çarpımıdır. Çarpım ancak $\mathbf{A}$ matrisinin sütun sayısı $\mathbf{B}$ matrisinin satır sayısına eşitse tanımlıdır: Tiplerin “iç” sayıları uyuşmalıdır, $(m\times n)\cdot(n\times k)$, ve sonuç, “dış” sayılardan oluşan $m\times k$ tipindedir.

:::satz Teorem 9.2 (Çarpım bileşkedir)
<span class="anker" id="satz-9-2"></span>

Bütün $\mathbf{x}\in\mathbb{R}^k$ vektörleri için $(\mathbf{A}\mathbf{B})\,\mathbf{x}=\mathbf{A}\,(\mathbf{B}\mathbf{x})$ geçerlidir.
:::

:::herleitung Bileşke
[(7.1)](das-matrix-vektor-produkt.html#gl-7-1) ve [(9.1)](#gl-9-1) uyarınca sol tarafın $i$ numaralı bileşeni şudur:

$$\sum_{l=1}^k(\mathbf{A}\mathbf{B})_{il}\,x_l=\sum_{l=1}^k\sum_{j=1}^na_{ij}\,b_{jl}\,x_l=\sum_{j=1}^na_{ij}\Bigl(\sum_{l=1}^kb_{jl}\,x_l\Bigr)=\sum_{j=1}^na_{ij}\,(\mathbf{B}\mathbf{x})_j ,$$

ve bu, $\mathbf{A}(\mathbf{B}\mathbf{x})$ vektörünün $i$ numaralı bileşenidir. Ortadaki adımda iki toplamın yeri değiştirildi ve $a_{ij}$ içteki toplamın önüne alındı.
:::

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ ve $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ için şu bulunur:

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&1\\1&0\end{pmatrix}.$$

Dört elemanın her biri [(9.1)](#gl-9-1) uyarınca bir toplamdır (Şekil [34](#abb-34)).

:::abbildung ml/k1rprodukt 34
Eleman eleman matris çarpımı: $(i,l)$ elemanı, $\mathbf{A}$ matrisinin $i$ numaralı satırı çarpı $\mathbf{B}$ matrisinin $l$ numaralı sütunudur.
:::

$\mathbf{x}=(1,\,2)^{\top}$ ile kontrol: $\mathbf{B}\mathbf{x}=(2,\,1)^{\top}$, sonra $\mathbf{A}(\mathbf{B}\mathbf{x})=(4,\,1)^{\top}$; doğrudan da $(\mathbf{A}\mathbf{B})\mathbf{x}=(2+2,\ 1+0)^{\top}=(4,\,1)^{\top}$.
::::

⁠**Kısacası:** $\mathbf{A}\mathbf{B}$ matris çarpımı, “önce $\mathbf{B}$, sonra $\mathbf{A}$” dönüşümünün matrisidir; $(i,l)$ elemanı, $\mathbf{A}$ matrisinin $i$ numaralı satırı çarpı $\mathbf{B}$ matrisinin $l$ numaralı sütunudur.

:::hintergrund Matris çarpımı neden tam olarak böyle tanımlanır?
[(9.1)](#gl-9-1) formülü ilk bakışta keyfî görünür. Matrisleri eleman eleman çarpmak daha akla yakın gelirdi. Ama matris çarpımı serbestçe uydurulmuş bir şey değildir, bir istekle belirlenmiştir: Bileşkenin matrisi olmalıdır. Bu matris alt kesim [8.2](lineare-abbildungen.html#stufe-8-2) içindeki teoreme göre tektir ve $l$ numaralı sütunu, $\mathbf{e}_l$ vektörünün iki dönüşüm altındaki görüntüsü, yani $\mathbf{A}$ çarpı $\mathbf{B}$ matrisinin $l$ numaralı sütunu olmak zorundadır. Bu koşul bileşen bileşen yazılınca tam olarak [(9.1)](#gl-9-1) ortaya çıkar. Eleman eleman alınan bir çarpımın böyle bir anlamı olmazdı: İki dönüşümün bileşkesini betimlemez.
:::

### Birçok vektör aynı anda

<span class="anker" id="stufe-9-2"></span>

Çarpımın türetilişine göre $\mathbf{A}\mathbf{B}$ matrisinin $l$ numaralı sütunu, $\mathbf{A}$ çarpı $\mathbf{B}$ matrisinin $l$ numaralı sütunudur. Demek ki bir matris çarpımı, yan yana duran birkaç matris-vektör çarpımı olarak okunabilir:

<span class="anker" id="gl-9-2"></span>
$$\mathbf{A}\begin{pmatrix}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{B}\mathbf{e}_k\end{pmatrix}=\begin{pmatrix}\mathbf{A}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{A}\mathbf{B}\mathbf{e}_k\end{pmatrix}. \tag{9.2}$$

Aynı biçimde $\mathbf{A}\mathbf{B}$ matrisinin $i$ numaralı satırı, $\mathbf{A}$ matrisinin $\mathbf{B}$ ile çarpılmış $i$ numaralı satırıdır.

Veriler için bu şu demektir: Birkaç ağırlıklı toplam bütün örneklere uygulanmak istenirse ağırlık vektörleri bir $\mathbf{W}$ matrisinin sütunları olarak yan yana yazılır. O zaman $\mathbf{X}\mathbf{W}$ çarpımının $l$ numaralı sütunu, $l$-inci ağırlık vektörüyle yapılan tahminleri içerir.

::::beispiel [Sayısal örnek]
$\mathbf{w}=(3,\,10,\,-4)^{\top}$ (bin avro) ile tahmin edilen satış fiyatının yanında $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$ (avro) ağırlıklarıyla aylık kira da tahmin edilmek isteniyor. $\mathbf{W}=\begin{pmatrix}\mathbf{w}&\mathbf{w}_{\mathrm M}\end{pmatrix}\in\mathbb{R}^{3\times2}$ ile şu bulunur:

$$\mathbf{X}\mathbf{W}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3&12\\10&30\\-4&-8\end{pmatrix}=\begin{pmatrix}188&756\\126&502\\286&1152\\232&914\end{pmatrix}.$$

$i$ numaralı satır, $i$ numaralı daire için iki tahmini de içerir; $1$ numaralı sütun bütün satış fiyatlarını, $2$ numaralı sütun bütün kiraları içerir.
::::

⁠**Kısacası:** $\mathbf{A}\mathbf{B}$ matrisinin sütunları, $\mathbf{A}$ çarpı $\mathbf{B}$ matrisinin sütunlarıdır; $\mathbf{X}\mathbf{W}$ birkaç ağırlıklı toplamı bütün örneklere aynı anda uygular.

### Hesap kuralları: Sıra önemlidir

<span class="anker" id="stufe-9-3"></span>

Sayılar için $2\cdot3=3\cdot2$ olur. Matrisler için bu geçerli değildir ve nedeni gözle görülebilir: Önce döndürüp sonra germek, önce gerip sonra döndürmekten farklı bir şeydir (Şekil [35](#abb-35)).

:::abbildung ml/k1reihenfolge 35
$\mathbf{e}_1$ (kırmızı) ve $\mathbf{e}_2$ (yeşil) ile birim kare, yanında $\mathbf{S}\mathbf R$ ve $\mathbf R\mathbf{S}$ altındaki görüntüleri. Burada $\mathbf R$, $90^\circ$ kadar dönme, $\mathbf{S}=\operatorname{diag}(2;\,0{,}5)$ ise germedir. Dikdörtgenin yatay mı yoksa dikey mi uzun olacağına sıra karar verir.
:::

:::satz Teorem 9.3 (Matris çarpımının hesap kuralları)
<span class="anker" id="satz-9-3"></span>

Tipleri uygun matrisler ve $c$ skalerleri için şunlar geçerlidir:

<ol class="rm">

<li>

$(\mathbf{A}\mathbf{B})\mathbf{C}=\mathbf{A}(\mathbf{B}\mathbf{C})$ (birleşme özelliği);

</li>

<li>

$\mathbf{A}(\mathbf{B}+\mathbf{C})=\mathbf{A}\mathbf{B}+\mathbf{A}\mathbf{C}$ ve $(\mathbf{A}+\mathbf{B})\mathbf{C}=\mathbf{A}\mathbf{C}+\mathbf{B}\mathbf{C}$ (dağılma özelliği);

</li>

<li>

$c\,(\mathbf{A}\mathbf{B})=(c\,\mathbf{A})\mathbf{B}=\mathbf{A}(c\,\mathbf{B})$.

</li>

</ol>

Ama genel olarak $\mathbf{A}\mathbf{B}\ne\mathbf{B}\mathbf{A}$ olur: Matris çarpımının değişme özelliği *yoktur*.
:::

(i) kuralı anlamdan çıkar: İki taraf da “önce $\mathbf{C}$, sonra $\mathbf{B}$, sonra $\mathbf{A}$” dönüşümünün matrisidir, çünkü her $\mathbf{x}$ için $(\mathbf{A}\mathbf{B})(\mathbf{C}\mathbf{x})=\mathbf{A}(\mathbf{B}(\mathbf{C}\mathbf{x}))=\mathbf{A}((\mathbf{B}\mathbf{C})\mathbf{x})$ olur. (ii) ve (iii) kuralları [(9.1)](#gl-9-1) ve toplam kurallarıyla eleman eleman doğrulanır.

::::beispiel [Sayısal örnek 1]
$\mathbf R=\mathbf R_{90^\circ}=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ dönmesi ve $\mathbf{S}=\operatorname{diag}(2;\,0{,}5)$ germesiyle şu bulunur:

$$\mathbf{S}\mathbf R=\begin{pmatrix}0&-2\\0{,}5&0\end{pmatrix},\qquad \mathbf R\mathbf{S}=\begin{pmatrix}0&-0{,}5\\2&0\end{pmatrix}.$$

Önce döndürüp sonra germek $\mathbf{e}_1$ vektörünü $(0;\,0{,}5)^{\top}$ vektörüne, önce gerip sonra döndürmek ise $(0,\,2)^{\top}$ vektörüne götürür.
::::

::::beispiel [Sayısal örnek 2]
Daha önceki matrisler için (alt kesim [9.1](#stufe-9-1)) $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\bigr)$, ama $\mathbf{B}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$ olur. Tipler farklıysa bu daha da belirgindir: $\mathbf{A}\in\mathbb{R}^{2\times3}$ ve $\mathbf{B}\in\mathbb{R}^{3\times2}$ için $\mathbf{A}\mathbf{B}$ çarpımı $2\times2$ tipinde, $\mathbf{B}\mathbf{A}$ çarpımı ise $3\times3$ tipinde bir matristir.
::::

⁠**Kısacası:** Matris çarpımında parantezlerin yeri değiştirilebilir ve parantezler açılabilir, ama çarpanların sırası değiştirilemez.

:::hintergrund Parantezleme neden hesap süresi kazandırır?
(i) kuralına göre $(\mathbf{A}\mathbf{B})\mathbf{x}=\mathbf{A}(\mathbf{B}\mathbf{x})$ olur. Sonuç aynıdır, harcanan emek aynı değildir. $n\times n$ tipindeki iki matris için $\mathbf{A}\mathbf{B}$ çarpımı, $n^2$ elemanın her biri için $n$ çarpma ve $n-1$ toplama, toplam yaklaşık $2n^3$ temel aritmetik işlem gerektirir; ardından $(\mathbf{A}\mathbf{B})\mathbf{x}$ yaklaşık $2n^2$ işlem daha tutar. $\mathbf{A}(\mathbf{B}\mathbf{x})$ yolu, her biri yaklaşık $2n^2$ işlem tutan iki matris-vektör çarpımından oluşur. $n=1000$ için bu, yaklaşık $2\cdot10^9$ işleme karşı $4\cdot10^6$ temel aritmetik işlem, yani $500$ katlık bir farktır. Bu yüzden uzun bir matris zincirini bir vektöre uygulayan kişi sağdan sola doğru hesaplar ve çarpım matrisini hiç oluşturmaz.
:::

### İki doğrusal aşama tek bir aşamadır

<span class="anker" id="stufe-9-4"></span>

Birkaç doğrusal hesap aşaması art arda bağlanırsa yeni türden bir dönüşüm ortaya çıkmaz. Bu, matris çarpımından (alt kesim [9.1](#stufe-9-1)) sonra açıktır, ama doğrusal kuralların sınırlarını belirlediği için ayrı bir teoremi hak eder.

:::satz Teorem 9.4 (Art arda bağlanmış doğrusal dönüşümler)
<span class="anker" id="satz-9-4"></span>

$f(\mathbf{x})=\mathbf{B}\mathbf{x}$ ve $g(\mathbf{u})=\mathbf{A}\mathbf{u}$ doğrusalsa $\mathbf{x}\mapsto g(f(\mathbf{x}))$ bileşkesi de doğrusaldır, hem de tek bir $\mathbf{A}\mathbf{B}$ matrisiyle. Aynı şey, doğrusal aşamalardan oluşan sonlu her zincir için geçerlidir.
:::

Kaç doğrusal aşama art arda bağlanırsa bağlansın, sonuç her zaman tek bir matrisle tek adımda hesaplanabilir. Demek ki doğrusal aşamalardan oluşan bir zincirin yapabildiğini tek bir matris de yapabilir. Sinyaller ve sistemler alanından aynı şey bilinir: Zincir hâlinde bağlanmış iki doğrusal sistem birlikte yine doğrusal bir sistem oluşturur.

::::beispiel [Sayısal örnek]
Birinci aşama üç sayıdan iki sayı üretir, $\mathbf{B}=\bigl(\begin{smallmatrix}1&2&0\\0&1&-1\end{smallmatrix}\bigr)$; ikinci aşama iki sayıdan yine üç sayı üretir, $\mathbf{A}=\Bigl(\begin{smallmatrix}2&1\\1&-1\\0&3\end{smallmatrix}\Bigr)$. Birlikte bunlar tek bir matristir:

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&5&-1\\1&1&1\\0&3&-3\end{pmatrix}.$$

$\mathbf{x}=(1,\,1,\,1)^{\top}$ ile kontrol: $\mathbf{B}\mathbf{x}=(3,\,0)^{\top}$ ve $\mathbf{A}(3,\,0)^{\top}=(6,\,3,\,0)^{\top}$; aynı biçimde $(\mathbf{A}\mathbf{B})\mathbf{x}=(2+5-1,\ 1+1+1,\ 0+3-3)^{\top}=(6,\,3,\,0)^{\top}$.
::::

⁠**Kısacası:** Art arda doğrusal aşamalar birlikte tek bir doğrusal dönüşümdür; bu dönüşümün matrisi tek tek matrislerin çarpımıdır.

### Dış çarpım

<span class="anker" id="stufe-9-5"></span>

$\mathbf{u}^{\top}\mathbf{v}$ iç çarpımı “satır çarpı sütun” biçimindedir ve bir sayı verir. Sıra tersine çevrilirse, yani “sütun çarpı satır” alınırsa, [(9.1)](#gl-9-1) uyarınca koca bir matris ortaya çıkar: bir vektörün her bileşeninin öteki vektörün her bileşeniyle çarpımlarından oluşan tablo, tıpkı bir çarpım tablosu gibi.

:::definition Tanım 9.5 (Dış çarpım)
<span class="anker" id="satz-9-5"></span>

$\mathbf{u}\in\mathbb{R}^m$ ve $\mathbf{v}\in\mathbb{R}^n$ için $\mathbf{u}\mathbf{v}^{\top}\in\mathbb{R}^{m\times n}$ __dış çarpımı__, elemanları şunlar olan matristir:

<span class="anker" id="gl-9-3"></span>
$$(\mathbf{u}\mathbf{v}^{\top})_{ij}=u_i\,v_j . \tag{9.3}$$
:::

Bu, $m\times1$ tipinde bir matris ile $1\times n$ tipinde bir matrisin matris çarpımıdır. Her sütun $\mathbf{u}$ vektörünün bir katıdır, yani $v_j\,\mathbf{u}$; her satır da $\mathbf{v}^{\top}$ satırının bir katıdır.

::::beispiel [Sayısal örnek]
$$\begin{pmatrix}1\\2\\3\end{pmatrix}\begin{pmatrix}4&5\end{pmatrix}=\begin{pmatrix}4&5\\8&10\\12&15\end{pmatrix}.$$
::::

Dış çarpımla her matris çarpımı bir toplam olarak yazılabilir: “$\mathbf{A}$ matrisinin $j$ numaralı sütunu çarpı $\mathbf{B}$ matrisinin $j$ numaralı satırı”, $j$ üzerinden toplanmış olarak:

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}\mathbf{B}=\sum_{j=1}^n\mathbf{a}_j\,\bigl(\mathbf{B}\text{ matrisinin $j$ numaralı satırı}\bigr) . \tag{9.4}$$

Sağ tarafın $(i,l)$ elemanı, tıpkı [(9.1)](#gl-9-1) formülündeki gibi $\sum_ja_{ij}\,b_{jl}$ olur. Daha önceki $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ ve $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ matrisleri için (alt kesim [9.1](#stufe-9-1)) iki dış çarpımın toplamı yine $\mathbf{A}\mathbf{B}$ çarpımını verir (Şekil [36](#abb-36)).

:::abbildung ml/k1raeusser 36
Dış çarpımların toplamı olarak matris çarpımı: $\mathbf{A}$ matrisinin $j$ numaralı sütunu çarpı $\mathbf{B}$ matrisinin $j$ numaralı satırı, $j=1,2$ üzerinden toplanmış.
:::

⁠**Kısacası:** $\mathbf{u}\mathbf{v}^{\top}$ dış çarpımı bütün $u_iv_j$ çarpımlarının tablosudur; her matris çarpımı bu tür tabloların bir toplamıdır.

:::aufgabe Alıştırma 21 ★ Çarpımlar ve tipler
<span class="anker" id="aufg-21"></span>

<ol class="al">

<li>

$\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ ve $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$ için $\mathbf{C}\mathbf{D}$ ve $\mathbf{D}\mathbf{C}$ çarpımlarını hesaplayın.

</li>

<li>

$\mathbf{A}\in\mathbb{R}^{2\times3}$, $\mathbf{B}\in\mathbb{R}^{3\times4}$ ve $\mathbf{x}\in\mathbb{R}^4$ olsun. $\mathbf{A}\mathbf{B}$, $\mathbf{B}\mathbf{A}$, $\mathbf{A}\mathbf{B}\mathbf{x}$, $\mathbf{B}\mathbf{x}\mathbf{A}$ ifadelerinden hangileri tanımlıdır ve sonuç hangi tiptedir?

</li>

<li>

$(1,\,-1)^{\top}(2,\,0,\,3)$ dış çarpımını hesaplayın ve her satırın $(2,\,0,\,3)$ satırının bir katı olduğunu kontrol edin.

</li>

</ol>

:::loesung
(a) $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}1\cdot0+2\cdot1&1\cdot1+2\cdot1\\3\cdot0+4\cdot1&3\cdot1+4\cdot1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$ ve $\mathbf{D}\mathbf{C}=\bigl(\begin{smallmatrix}0+3&0+4\\1+3&2+4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$. İkisi farklıdır.

(b) $\mathbf{A}\mathbf{B}$: $(2\times3)\cdot(3\times4)$ uyar, tip $2\times4$. $\mathbf{B}\mathbf{A}$: $(3\times4)\cdot(2\times3)$, içteki sayılar $4\ne2$, tanımlı değil. $\mathbf{A}\mathbf{B}\mathbf{x}$: $(2\times4)\cdot(4\times1)$ uyar, sonuç $\mathbb{R}^2$ uzayında bir vektör. $\mathbf{B}\mathbf{x}\mathbf{A}$: $\mathbf{B}\mathbf{x}$ çarpımının tipi $3\times1$ olur ve $(3\times1)\cdot(2\times3)$ uymaz, içteki sayılar $1\ne2$; tanımlı değil.

(c) $(1,\,-1)^{\top}(2,\,0,\,3)=\bigl(\begin{smallmatrix}2&0&3\\-2&0&-3\end{smallmatrix}\bigr)$. Birinci satır $1\cdot(2,0,3)$, ikincisi $-1\cdot(2,0,3)$ olur.
:::
:::

:::aufgabe Alıştırma 22 ★★ İki dönme
<span class="anker" id="aufg-22"></span>

<ol class="al">

<li>

[(8.3)](lineare-abbildungen.html#gl-8-3) ile $\mathbf R_\alpha\mathbf R_\beta$ çarpımını hesaplayın. Bu hangi dönmedir? Bu arada trigonometrinin hangi iki formülünü elde edersiniz?

</li>

<li>

$\mathbf R_{90^\circ}^2=\mathbf R_{90^\circ}\mathbf R_{90^\circ}$ ve $\mathbf R_{90^\circ}^4$ matrislerini hesaplayın ve sonuçları geometrik olarak yorumlayın.

</li>

<li>

$\mathbf R_\alpha\mathbf R_\beta=\mathbf R_\beta\mathbf R_\alpha$ eşitliği geçerli midir? Bu, matrislerin çarpımda yer değiştiremeyeceği kuralıyla neden çelişmez?

</li>

</ol>

:::loesung
(a) Çarpım açılınca şu bulunur:

$$\mathbf R_\alpha\mathbf R_\beta=\begin{pmatrix}\cos\alpha\cos\beta-\sin\alpha\sin\beta&-(\cos\alpha\sin\beta+\sin\alpha\cos\beta)\\\sin\alpha\cos\beta+\cos\alpha\sin\beta&\cos\alpha\cos\beta-\sin\alpha\sin\beta\end{pmatrix}.$$

Geometrik olarak bu “önce $\beta$ kadar döndür, sonra $\alpha$ kadar” demektir, yani $\alpha+\beta$ kadar dönmedir; bu dönmenin matrisi [(8.3)](lineare-abbildungen.html#gl-8-3) uyarınca $\mathbf R_{\alpha+\beta}$ olur. Elemanlar karşılaştırılınca trigonometrinin toplam formülleri elde edilir: $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$ ve $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$. Matris çarpımı bu formülleri, ezberlemeye gerek bırakmadan verir.

(b) $\mathbf R_{90^\circ}^2=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-1&0\\0&-1\end{smallmatrix}\bigr)=-\mathbf{I}$: İki kez $90^\circ$ yarım dönmedir; her nokta orijine göre simetriğine geçer. $\mathbf R_{90^\circ}^4=(-\mathbf{I})(-\mathbf{I})=\mathbf{I}$: Dört çeyrek dönme tam bir dönmedir.

(c) Evet: İki çarpım da $\mathbf R_{\alpha+\beta}=\mathbf R_{\beta+\alpha}$ olur, çünkü düzlemde aynı nokta etrafındaki dönmeler herhangi bir sırayla yapılabilir. “Değişme özelliği yoktur” yalnızca $\mathbf{A}\mathbf{B}=\mathbf{B}\mathbf{A}$ eşitliğinin *her zaman geçerli olmadığı* anlamına gelir. Belirli çiftler için, örneğin düzlemin iki dönmesi ya da iki köşegen matris için, bu eşitlik yine de geçerli olabilir.
:::
:::

:::aufgabe Alıştırma 23 ★★ Doğru parantez
<span class="anker" id="aufg-23"></span>

$\mathbf{A}\in\mathbb{R}^{100\times1000}$, $\mathbf{B}\in\mathbb{R}^{1000\times1000}$ ve $\mathbf{x}\in\mathbb{R}^{1000}$ olsun. $(\mathbf{A}\mathbf{B})\mathbf{x}$ ve $\mathbf{A}(\mathbf{B}\mathbf{x})$ için temel aritmetik işlem sayısını kestirin. Bunu yaparken $m\times n$ tipinde bir matrisin $n\times k$ tipinde bir matrisle çarpımı için yaklaşık $2mnk$ işlem sayın.

:::loesung
$(\mathbf{A}\mathbf{B})\mathbf{x}$: $100\times1000$ tipindeki bir matrisin $1000\times1000$ tipindeki bir matrisle çarpımı olan $\mathbf{A}\mathbf{B}$ yaklaşık $2\cdot100\cdot1000\cdot1000=2\cdot10^8$ işlem gerektirir, ardından $(\mathbf{A}\mathbf{B})\mathbf{x}$ yaklaşık $2\cdot100\cdot1000=2\cdot10^5$ işlem daha; hepsi birlikte yaklaşık $200{,}2$ milyon. $\mathbf{A}(\mathbf{B}\mathbf{x})$: $\mathbf{B}\mathbf{x}$ yaklaşık $2\cdot1000\cdot1000=2\cdot10^6$ işlem gerektirir, ardından $\mathbf{A}(\mathbf{B}\mathbf{x})$ yaklaşık $2\cdot10^5$; hepsi birlikte yaklaşık $2{,}2$ milyon. İkinci yol aynı sonucu verir ve yaklaşık $91$ kat daha hızlıdır.
:::
:::
