---
title: Eleman eleman hesap ve tensörler
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Bölüm 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15211600
summary: Vektörler ve matrislerle yapılan her hesap bir matris çarpımı değildir.
tags: Hadamard çarpımı, eleman eleman, tensör, eksen, şekli
lang: tr
---

<span class="anker" id="stufe-15"></span>

:::zweck
Vektörler ve matrislerle yapılan her hesap bir matris çarpımı değildir. Bu kesim, eleman eleman çalışan hesapları tanıtıyor ve vektörleri ile matrisleri, görüntüler için gereken türden ikiden fazla indisli sayı dizilerine genişletiyor.
:::

### Hadamard çarpımı

<span class="anker" id="stufe-15-1"></span>

Bir satıcının elinde satılan miktarların listesi ve birim fiyatların listesi var. Her ürün için satış tutarını, yani miktar çarpı fiyatı bulmak istiyor, ama henüz toplamı değil. Bu, eleman eleman alınan bir çarpımdır.

:::definition Tanım 15.1 (Hadamard çarpımı)
<span class="anker" id="satz-15-1"></span>

Aynı tipteki iki vektör ya da iki matris için $\mathbf{A}\odot\mathbf{B}$ __Hadamard çarpımı__, eleman eleman alınan çarpımdır:

<span class="anker" id="gl-15-1"></span>
$$(\mathbf{A}\odot\mathbf{B})_{ij}=a_{ij}\,b_{ij} . \tag{15.1}$$
:::

Hadamard çarpımı matris çarpımı *değildir*. Matris çarpımı satırlardan ve sütunlardan iç çarpımlar oluşturur; Hadamard çarpımı yalnızca aynı yerdeki elemanları çarpar. Bilinen kavramlarla iki bağlantı: İki vektörün Hadamard çarpımının bileşenleri toplanırsa iç çarpımları elde edilir, $\mathbf 1^{\top}(\mathbf{u}\odot\mathbf{v})=\mathbf{u}^{\top}\mathbf{v}$. Sabit bir vektörle Hadamard çarpımı da bir köşegen matrisle çarpmadır: $\mathbf{v}\odot\mathbf{x}=\operatorname{diag}(\mathbf{v})\,\mathbf{x}$.

::::beispiel [Sayısal örnek]
$(1,\,2,\,3)^{\top}\odot(4,\,5,\,6)^{\top}=(4,\,10,\,18)^{\top}$ olur ve $4+10+18=32$ iç çarpımdır. Matrisler için şu bulunur:

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}\odot\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&2\\3&0\end{pmatrix},\qquad\text{ama}\qquad \begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}2&1\\4&3\end{pmatrix}.$$

Sıfırlardan ve birlerden oluşan bir vektörle öznitelikler gizlenebilir: $(1,\,0,\,1)^{\top}\odot\mathbf{x}_1=(60,\,0,\,3)^{\top}$, Daire 1 için oda sayısını dışarıda bırakır.
::::

⁠**Kısacası:** $\odot$ Hadamard çarpımı eleman eleman çarpar; matris çarpımı değildir.

### Eleman eleman uygulanan fonksiyonlar

<span class="anker" id="stufe-15-2"></span>

Çoğu zaman aynı fonksiyon bir vektörün her elemanına uygulanır: bütün hataların karesi alınır, hepsinin mutlak değeri alınır ya da bütün değerler yuvarlanır.

:::definition Tanım 15.2 (Eleman eleman uygulanan fonksiyon)
<span class="anker" id="satz-15-2"></span>

Bir $f\colon\mathbb{R}\to\mathbb{R}$ fonksiyonu ve bir $\mathbf{x}\in\mathbb{R}^d$ vektörü için __eleman eleman__ uygulanan $f$, $\bigl(f(x_1),\dots,f(x_d)\bigr)^{\top}$ vektörüdür. Matrisler için de aynısı eleman eleman geçerlidir.
:::

Birçok norm bu biçimde yazılabilir: Mutlak değerler toplamı normu, eleman eleman alınan mutlak değerlerin toplamıdır, $\lVert\mathbf{x}\rVert_1=\mathbf 1^{\top}|\mathbf{x}|$; Öklid normunun karesi de eleman eleman alınan karelerin toplamıdır. Eleman eleman uygulanan bir fonksiyon genel olarak doğrusal değildir: Eleman eleman kare alma, $2\mathbf{x}$ vektöründen elemanları $2x_j^2$ değil, $4x_j^2$ olan vektörü üretir.

::::beispiel [Sayısal örnek]
Emlakçının hata vektörü $(-12,\,-4,\,-4,\,-8)^{\top}$ idi. Eleman eleman mutlak değerler $(12,\,4,\,4,\,8)^{\top}$ verir; bunların toplamı $28$, yani mutlak değerler toplamı normudur. Eksper A için (alt kesim [3.5](normen-die-groe-eines-vektors.html#stufe-3-5)) eleman eleman kareler $(100,\,100,\,100,\,100)^{\top}$ verir; toplamları $400=20^2$ olur.
::::

⁠**Kısacası:** Eleman eleman uygulanan bir fonksiyon her elemana ayrı ayrı etki eder; genel olarak doğrusal değildir.

### Her satıra bir vektör eklemek

<span class="anker" id="stufe-15-3"></span>

Bütün bir veri kümesini merkezlemek için veri matrisinin her satırından aynı vektör, yani örneklerin ortalaması çıkarılır. Aynı biçimde afin tahmin de her bileşene aynı eksen kesişimini ekler. Bu tür hesaplar için bir yazılışa ihtiyaç vardır.

Örneklerin ortalamasını bir matris-vektör çarpımı verir: $\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$, çünkü bu vektörün $j$ numaralı bileşeni, $j$ numaralı sütunun ortalaması olan $\frac1N\sum_ix_{ij}$ değeridir. Bütün satırları $\bar{\mathbf{x}}^{\top}$ satırına eşit olan matris $\mathbf 1\,\bar{\mathbf{x}}^{\top}$ dış çarpımıdır. Böylece merkezlenmiş veri matrisi şudur:

<span class="anker" id="gl-15-2"></span>
$$\tilde{\mathbf{X}}=\mathbf{X}-\mathbf 1\,\bar{\mathbf{x}}^{\top} , \tag{15.2}$$

ve bu matrisin $i$ numaralı satırı $(\mathbf{x}_i-\bar{\mathbf{x}})^{\top}$ vektörüdür. Birçok kaynak bunun yerine kısaca $\mathbf{X}-\bar{\mathbf{x}}^{\top}$ yazar ve bununla şunu kasteder: satır vektörünü her satırdan çıkarmak. Kesin konuşmak gerekirse $N\times d$ tipinde bir matris ile $1\times d$ tipinde bir matrisin farkı tanımlı değildir; kısa yazılış her zaman [(15.2)](#gl-15-2) anlamına gelir.

::::beispiel [Sayısal örnek]
Daireler için $\bar{\mathbf{x}}=\tfrac14\mathbf{X}^{\top}\mathbf 1=(65;\ 2{,}5;\ 3)^{\top}$ ve şu bulunur:

$$\tilde{\mathbf{X}}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}-\begin{pmatrix}65&2{,}5&3\\65&2{,}5&3\\65&2{,}5&3\\65&2{,}5&3\end{pmatrix}=\begin{pmatrix}-5&-0{,}5&0\\-25&-1{,}5&-2\\25&1{,}5&3\\5&0{,}5&-1\end{pmatrix}.$$

Her sütun merkezlenmiş öznitelik sütunudur (alt kesim [4.3](abstande-und-einheiten.html#stufe-4-3)) ve toplamı sıfırdır.
::::

⁠**Kısacası:** Bir $\mathbf{A}$ matrisinin her satırına bir $\mathbf{q}$ vektörü eklemek $\mathbf{A}+\mathbf 1\,\mathbf{q}^{\top}$ demektir; yaygın kısa yazılış $\mathbf{A}+\mathbf{q}^{\top}$ tam olarak bunu kasteder.

### Tensörler

<span class="anker" id="stufe-15-4"></span>

Bir skaler tek bir sayıdır, bir vektör tek indisli bir liste, bir matris iki indisli bir tablo. Renkli bir görüntü üç indis gerektirir: satır, sütun ve renk kanalı. Renkli görüntülerden oluşan bir yığın dört indis gerektirir. Bütün bu sayı dizileri tek bir ad altında toplanır.

:::definition Tanım 15.3 (Tensör, şekil)
<span class="anker" id="satz-15-3"></span>

Makine öğrenmesinde __tensör__, elemanları $k$ indisle numaralanan bir sayı dizisidir. Her indis bir __eksen__ boyunca ilerler. Eksen uzunluklarının listesine tensörün __şekli__ denir.
:::

Bir skaler $0$ eksenli bir tensördür, $\mathbb{R}^d$ uzayındaki bir vektör uzunluğu $d$ olan tek eksenli bir tensör, $\mathbb{R}^{m\times n}$ içindeki bir matris de şekli $m\times n$ olan bir tensördür. Şekli $n_1\times n_2\times\dots\times n_k$ olan bir tensörün $n_1\cdot n_2\cdots n_k$ elemanı vardır. Şekil [42](#abb-42) ilk basamakları gösteriyor.

:::abbildung ml/k1tensor 42
$0$ ile $4$ arası eksenli tensörler: bir skaler, $4$ elemanlı bir vektör, $4\times4$ tipinde bir matris (örneğin gri tonlamalı bir görüntü), kırmızı, yeşil ve mavi için $4\times4$ tipindeki üç kanaldan oluşan renkli bir görüntü ve bu türden $N$ renkli görüntüden oluşan bir yığın (üç görüntüyle gösterilmiştir).
:::

::::beispiel [Sayısal örnek]
$4\times4$ pikselli ve üç renk kanallı renkli bir görüntü, şekli $3\times4\times4$ olan ve $48$ elemanı bulunan bir tensördür. İndisleri $(1,2,3)$ olan eleman, $2$ numaralı satır ile $3$ numaralı sütundaki pikselde birinci kanalın, yani kırmızının parlaklığıdır.
::::

⁠**Kısacası:** Bir tensör, eksen sayısı istenildiği kadar olabilen bir sayı dizisidir; skaler, vektör ve matris $0$, $1$ ve $2$ eksenli durumlardır.

:::hintergrund Fizikteki tensör başka bir şeydir
Fizikte bir tensör, örneğin bir cismi her eksen etrafında döndürmenin ne kadar zor olduğunu belirten eylemsizlik tensörü ya da yük altındaki bir kirişin her doğrultuda ne kadar çekildiğini veya bastırıldığını betimleyen tensör, bir sayı dizisinden fazlasıdır. Orada tensöre, koordinat sistemi döndürüldüğünde elemanlarının nasıl değiştiğini söyleyen bir kural da dahildir; tensörü yalnızca elemanları oluşturmaz. Makine öğrenmesinde bu kural yoktur: Orada bir tensör yalnızca çok boyutlu bir sayı dizisidir. Sözcük aynıdır, kavram farklıdır.
:::

### Tensör olarak görüntüler

<span class="anker" id="stufe-15-5"></span>

Görüntü verileri, ikiden fazla eksenli tensörlerin en önemli kullanım alanıdır. Şekilleri, bir veri kümesinin kaç sayı içerdiğini hemen gösterir.

$28\times28$ pikselli gri tonlamalı bir görüntü bir matristir, yani şekli $28\times28$ olan ve $784$ elemanı bulunan bir tensördür. $32\times32$ pikselli renkli bir görüntünün üç kanalı vardır; şekli $3\times32\times32$, dolayısıyla eleman sayısı $3072$ olur. Bu türden $100$ renkli görüntüden oluşan bir yığının şekli $100\times3\times32\times32$, eleman sayısı $307\,200$ olur. Burada birinci eksen, tıpkı veri matrisinin satırları gibi örnekleri sayar: Veri matrisi, şekli $N\times d$ olan bir vektör yığınının özel durumudur.

Eksenlerin sırası bir uzlaşımdır. Bazı programlar renk kanalını başa ($3\times32\times32$), bazıları sona ($32\times32\times3$) koyar. Sayılar aynıdır, yalnızca dizilişleri farklıdır; her hesaptan önce hangi eksenin ne anlama geldiği açık olmalıdır.

::::beispiel [Sayısal örnek]
$28\times28$ pikselli $60\,000$ gri tonlamalı görüntüden oluşan bir veri kümesi, şekli $60\,000\times28\times28$ olan ve $47\,040\,000$ elemanı bulunan bir tensördür. Her görüntü okunarak $\mathbb{R}^{784}$ uzayında bir vektöre dönüştürülürse aynı elemanlara sahip, $\mathbb{R}^{60\,000\times784}$ içinde bir veri matrisi ortaya çıkar.
::::

⁠**Kısacası:** Bir görüntü iki ya da üç eksenli bir tensördür, bir görüntü yığını ise bir eksen daha fazlasına sahip bir tensördür; birinci eksen örnekleri sayar.

:::aufgabe Alıştırma 36 ★ Eleman eleman mı, değil mi?
<span class="anker" id="aufg-36"></span>

<ol class="al">

<li>

$\mathbf{u}=(2,\,-1,\,3)^{\top}$ ve $\mathbf{v}=(1,\,4,\,2)^{\top}$ için $\mathbf{u}\odot\mathbf{v}$ ve $\mathbf{u}^{\top}\mathbf{v}$ değerlerini hesaplayın.

</li>

<li>

$\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\odot\bigl(\begin{smallmatrix}2&0\\1&3\end{smallmatrix}\bigr)$ çarpımını ve aynı matrislerin matris çarpımını hesaplayın.

</li>

<li>

Renk kanalı başta olmak üzere, $224\times224$ pikselli $64$ renkli görüntüden oluşan bir yığının şekli nedir ve kaç elemanı vardır?

</li>

</ol>

:::loesung
(a) $\mathbf{u}\odot\mathbf{v}=(2,\,-4,\,6)^{\top}$ ve $\mathbf{u}^{\top}\mathbf{v}=2-4+6=4$; iç çarpım, Hadamard çarpımının elemanlarının toplamıdır.

(b) Hadamard: $\bigl(\begin{smallmatrix}1\cdot2&2\cdot0\\3\cdot1&4\cdot3\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&0\\3&12\end{smallmatrix}\bigr)$. Matris çarpımı: $\bigl(\begin{smallmatrix}2+2&0+6\\6+4&0+12\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4&6\\10&12\end{smallmatrix}\bigr)$. Yalnızca sağ alttaki eleman rastlantı eseri aynıdır.

(c) Şekil $64\times3\times224\times224$ olur; eleman sayısı $64\cdot3\cdot224\cdot224=9\,633\,792$.
:::
:::

:::aufgabe Alıştırma 37 ★★ Bir veri kümesini merkezlemek
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

Gösterin: [(15.2)](#gl-15-2) merkezlenmiş veri matrisinin sütunlarının toplamı sıfırdır, yani $\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf{0}^{\top}$. $\mathbf 1^{\top}\mathbf 1=N$ eşitliğini kullanın.

</li>

<li>

Üç metnin veri matrisini merkezleyin (alt kesim [5.4](winkel-und-ahnlichkeit.html#stufe-5-4)).

</li>

</ol>

:::loesung
(a) $\bar{\mathbf{x}}^{\top}=\frac1N\mathbf 1^{\top}\mathbf{X}$ olur; bu, $\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$ vektörünün devriğidir. Böylece:

$$\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf 1^{\top}\mathbf{X}-(\mathbf 1^{\top}\mathbf 1)\,\bar{\mathbf{x}}^{\top}=\mathbf 1^{\top}\mathbf{X}-N\cdot\tfrac1N\,\mathbf 1^{\top}\mathbf{X}=\mathbf{0}^{\top} .$$

Her sütun merkezlenmiş bir vektördür ve bileşenlerinin toplamı, tıpkı alt kesim [4.3](abstande-und-einheiten.html#stufe-4-3) içindeki gibi, sıfırdır.

(b) Metinlerin ortalaması $\bar{\mathbf{x}}=\tfrac13\bigl((3,2,0)^{\top}+(6,4,0)^{\top}+(0,1,3)^{\top}\bigr)=(3,\,\tfrac73,\,1)^{\top}$ olur. Merkezlenmiş hâli:

$$\tilde{\mathbf{X}}=\begin{pmatrix}0&-\frac13&-1\\3&\frac53&-1\\-3&-\frac43&2\end{pmatrix}.$$

Her sütunun toplamı sıfırdır: $0+3-3=0$, $-\tfrac13+\tfrac53-\tfrac43=0$, $-1-1+2=0$.
:::
:::
