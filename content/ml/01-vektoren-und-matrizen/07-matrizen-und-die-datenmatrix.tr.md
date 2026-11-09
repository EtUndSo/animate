---
title: Matrisler ve veri matrisi
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
knoten: Temeller 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15210700
summary: Bir veri kümesi, bileşen sayıları aynı olan birçok vektörden oluşur.
tags: matrisi, elemanı, tipi, kare, köşegenini, köşegen matris, sıfır matris, veri matrisi
lang: tr
---

<span class="anker" id="stufe-6"></span>

:::zweck
Bir veri kümesi, bileşen sayıları aynı olan birçok vektörden oluşur. Bu kesim bu vektörleri tek bir sayı tablosunda, yani bir matriste bir araya getiriyor ve matrislerin nasıl yazıldığını ve onlarla nasıl hesap yapıldığını belirliyor.
:::

### Matrisler

<span class="anker" id="stufe-6-1"></span>

Daire tablosu dört ayrı vektörden fazlasıdır: Bütün olarak onunla hesap yapılmak istenen bir nesnedir. Gri tonlamalı bir görüntü de bir tablodur, yani satırlar ve sütunlar hâlinde dizilmiş parlaklık değerlerinin tablosu. Böyle dikdörtgen bir sayı düzenine matris denir.

:::definition Tanım 6.1 (Matris)
<span class="anker" id="satz-6-1"></span>

Bir $\mathbf{A}\in\mathbb{R}^{m\times n}$ __matrisi__, $m$ satır ve $n$ sütun hâlinde dikdörtgen biçiminde dizilmiş $m\cdot n$ tane gerçel sayıdır:

$$\mathbf{A}=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix}.$$

$i$ numaralı satırda ve $j$ numaralı sütunda duran $a_{ij}$ sayısına matrisin bir __elemanı__ denir. $m\times n$ çiftine matrisin __tipi__ denir.
:::

Matrisler kalın ve büyük harfle yazılır, elemanları ise küçük harfle ve iki indisle: önce satır, sonra sütun. $\mathbf{A}$ matrisinin $j$-inci sütunu $m$ bileşenli bir vektördür; ona $\mathbf{a}_j$ denir. Matris bu durumda sütunlarının bir dizisi olarak da yazılır: $\mathbf{A}=\begin{pmatrix}\mathbf{a}_1&\cdots&\mathbf{a}_n\end{pmatrix}$. $d$ bileşenli bir vektör $d\times1$ tipinde bir matris, $d$ sayıdan oluşan bir satır da $1\times d$ tipinde bir matristir.

İki matris aynı tipteyse ve her yerde aynı elemana sahipse eşittir. Aynı tipteki matrisler, tıpkı vektörler gibi eleman eleman toplanır ve bir sayıyla eleman eleman çarpılır: $(\mathbf{A}+\mathbf{B})_{ij}=a_{ij}+b_{ij}$ ve $(c\,\mathbf{A})_{ij}=c\,a_{ij}$.

⁠**Sayısal örnek:** Şu matris

$$\mathbf{A}=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\in\mathbb{R}^{2\times3}$$

$2\times3$ tipindedir; elemanlarından ikisi $a_{12}=2$ ve $a_{21}=4$, ikinci sütunu da $\mathbf{a}_2=(2,\,5)^{\top}$ vektörüdür. Koyu zemin üzerinde açık renkli bir artı işareti gösteren $3\times3$ pikselli gri tonlamalı bir görüntü, satırları $(0,1,0)$, $(1,1,1)$ ve $(0,1,0)$ olan matristir. Ayrıca şu geçerlidir:

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}+\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}1&3\\4&4\end{pmatrix},\qquad 2\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}2&4\\6&8\end{pmatrix}.$$

⁠**Kısacası:** Matris, $m$ satırlı ve $n$ sütunlu dikdörtgen bir sayı tablosudur; $a_{ij}$ elemanı $i$ numaralı satırda ve $j$ numaralı sütunda durur.

:::hintergrund Matris ve vektör olarak bir görüntü
Bir görüntü satır satır okunur ve satırlar arka arkaya eklenirse matris uzun bir vektöre dönüşür: $3\times3$ pikselli artı işaretinden $(0,1,0,1,1,1,0,1,0)^{\top}\in\mathbb{R}^9$ vektörü, $28\times28$ pikselli bir görüntüden $\mathbb{R}^{784}$ uzayında bir vektör. Sayılar aynı kalır, ama bu yazılışta bir bilgi kaybolur: hangi piksellerin komşu olduğu. Bir pikselin hemen altındaki piksel uzun vektörde $28$ yer daha geride durur. Her özniteliği ayrı ayrı ağırlıklandıran hesaplar için bunun bir önemi yoktur. Komşuluklardan yararlanmak isteyen hesaplar için matris biçimi daha doğaldır.
:::

### Kare matrisler ve köşegen matrisler

<span class="anker" id="stufe-6-2"></span>

Bazı matrislere o kadar sık rastlanır ki kendi adları vardır. Üçünde de tablonun biçimi özellikle basittir.

Satır sayısı sütun sayısına eşit olan bir matrise __kare__ matris denir. Bir kare matrisin $a_{11},a_{22},\dots,a_{nn}$ elemanları, sol üstten sağ alta uzanan __köşegenini__ oluşturur.

:::definition Tanım 6.2 (Köşegen matris, sıfır matris)
<span class="anker" id="satz-6-2"></span>

Köşegen dışındaki elemanlarının hepsi sıfır olan bir kare matrise __köşegen matris__ denir. Bir $\mathbf{v}\in\mathbb{R}^n$ vektörü için $\operatorname{diag}(\mathbf{v})$, köşegen elemanları $v_1,\dots,v_n$ olan köşegen matristir.

Bütün elemanları sıfır olan matrise __sıfır matris__ denir ve $\mathbf 0$ diye yazılır.
:::

⁠**Sayısal örnek:**

$$\operatorname{diag}\bigl((2;\ 0{,}5)^{\top}\bigr)=\begin{pmatrix}2&0\\0&0{,}5\end{pmatrix},\qquad \operatorname{diag}\bigl((1,\,0,\,3)^{\top}\bigr)=\begin{pmatrix}1&0&0\\0&0&0\\0&0&3\end{pmatrix}.$$

İkinci matrisin bir köşegen elemanı sıfırdır ve yine de bir köşegen matristir; istenen yalnızca köşegen dışında sıfırların bulunmasıdır. $\operatorname{diag}\bigl((2;\ 0{,}5)^{\top}\bigr)$ yerine kısaca $\operatorname{diag}(2;\,0{,}5)$ yazılır.

⁠**Kısacası:** Kare matrisin satır sayısı sütun sayısına eşittir; köşegen matrisin sıfırdan farklı elemanları yalnızca köşegende bulunur.

### Veri matrisi

<span class="anker" id="stufe-6-3"></span>

Daire tablosu (alt kesim [1.2](vektoren-daten-als-zahlenlisten.html#stufe-1-2)) bir matristir: her daire için bir tane olmak üzere dört satır ve her öznitelik için bir tane olmak üzere üç sütun. Satır başına bir örnek içeren bu düzen, bir veri kümesinin standart biçimidir (Şekil [27](#abb-27)).

:::abbildung ml/k1datenmatrix 27
Daire veri kümesinin $\mathbf{X}$ veri matrisi. Her satır bir örnektir, satır olarak yazılmış $\mathbf{x}_i^{\top}$ vektörüdür (mavi: Daire 2). Her sütun, bir özniteliğin bütün örnekler üzerindeki öznitelik sütunudur (turuncu: alanlar). $x_{21}=40$ elemanı ikisinde de bulunur.
:::

:::definition Tanım 6.3 (Veri matrisi)
<span class="anker" id="satz-6-3"></span>

Örnekleri $\mathbf{x}_1,\dots,\mathbf{x}_N\in\mathbb{R}^d$ olan bir veri kümesinin __veri matrisi__, $i$ numaralı satırı satır olarak yazılmış $\mathbf{x}_i$ örneği olan $\mathbf{X}\in\mathbb{R}^{N\times d}$ matrisidir:

<span class="anker" id="gl-6-1"></span>
$$\mathbf{X}=\begin{pmatrix}\mathbf{x}_1^{\top}\\\mathbf{x}_2^{\top}\\\vdots\\\mathbf{x}_N^{\top}\end{pmatrix}=\begin{pmatrix}x_{11}&\cdots&x_{1d}\\\vdots&&\vdots\\x_{N1}&\cdots&x_{Nd}\end{pmatrix}. \tag{6.1}$$
:::

$x_{ij}$ elemanı, tıpkı daha önce kararlaştırıldığı gibi (alt kesim [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3)), $i$ numaralı örnekte $j$ numaralı özniteliğin değeridir. $\mathbf{X}$ matrisinin $j$ numaralı sütunu, $j$ özniteliğinin öznitelik sütunudur (alt kesim [4.3](abstande-und-einheiten.html#stufe-4-3)): bu özniteliğin bütün örneklerdeki bütün değerleri. Yani satırlar örneklere, sütunlar özniteliklere aittir. Örneklerin ortalaması olan $\bar{\mathbf{x}}$ vektörünün $j$ numaralı bileşeni, $j$ numaralı sütunun ortalamasıdır.

⁠**Sayısal örnek:** Daire veri kümesi için şu bulunur:

$$\mathbf{X}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\in\mathbb{R}^{4\times3}.$$

$x_{32}=4$ elemanı Daire 3'ün oda sayısıdır, birinci sütun $(60,\,40,\,90,\,70)^{\top}$ bütün alanları içerir ve bu sütunun ortalaması olan $65$, $\bar{\mathbf{x}}=(65;\ 2{,}5;\ 3)^{\top}$ vektörünün birinci bileşenidir.

⁠**Kısacası:** $\mathbf{X}\in\mathbb{R}^{N\times d}$ veri matrisi her satırda bir örnek, her sütunda bir öznitelik içerir.

:::hintergrund Örnekler satır olarak mı, sütun olarak mı?
Bu seri örnekleri, bir elektronik tabloda ve bugünkü ders kitaplarının ve program kütüphanelerinin çoğunda olduğu gibi satır olarak yazar. Bazı metinler bunun tersini yapar ve örnekleri sütun olarak yan yana koyar; o zaman veri matrisleri $d\times N$ tipinde olur. Harfler de değişebilir: Örnek sayısına çoğu zaman $m$, öznitelik sayısına $n$ denir ve $i$ numaralı örnek, indis üstte parantez içinde olmak üzere $\mathbf{x}^{(i)}$ diye yazılır. İçerik olarak hiçbir şey değişmez. Bu yüzden başka bir metni okuyan kişi önce orada neyin satır, neyin sütun olduğunu kontrol eder.
:::

:::aufgabe Alıştırma 15 ★ Matris okumak ve kurmak
<span class="anker" id="aufg-15"></span>

<ol class="al">

<li>

$\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ matrisi hangi tiptedir? $b_{13}$, $b_{21}$ elemanlarını ve $\mathbf{B}$ matrisinin üçüncü sütununu verin.

</li>

<li>

Üç metnin veri matrisini kurun (alt kesim [5.4](winkel-und-ahnlichkeit.html#stufe-5-4)). $N$, $d$ ve $x_{23}$ elemanı ne anlama gelir?

</li>

<li>

$4\times4$ pikselli gri tonlamalı bir görüntü açık renkli bir “L” gösteriyor: Birinci sütun ve en alttaki satır açıktır ($1$), geri kalan her şey koyudur ($0$). Matrisi yazın ve onu satır satır okuyarak bir vektöre dönüştürün. Bu vektörün kaç bileşeni vardır?

</li>

</ol>

:::loesung
(a) $\mathbf{B}$ matrisi $2\times3$ tipindedir. $b_{13}=2$ (satır 1, sütun 3) ve $b_{21}=2$ (satır 2, sütun 1) olur; üçüncü sütun $(2,\,0)^{\top}$ olur.

(b) $\mathbf{X}=\Bigl(\begin{smallmatrix}3&2&0\\6&4&0\\0&1&3\end{smallmatrix}\Bigr)$; $N=3$ metin ve $d=3$ sözcük vardır. $x_{23}=0$ elemanı şunu söyler: Üçüncü sözcük, “seçim”, ikinci metinde geçmez.

(c) Matrisin satırları $(1,0,0,0)$, $(1,0,0,0)$, $(1,0,0,0)$ ve $(1,1,1,1)$ olur. Satır satır okununca şu vektörü verir:

$$(1,0,0,0,\ 1,0,0,0,\ 1,0,0,0,\ 1,1,1,1)^{\top}\in\mathbb{R}^{16}$$

Bu vektörün $4\cdot4=16$ bileşeni vardır.
:::
:::
