---
title: Jacobi matrisi
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15230600
summary: Birçok hesap adımı tek bir sayı değil, birkaç sayı verir: Bir matris-vektör çarpımı bir vektörden başka bir vektör yapar.
tags: vektör değerli, Jacobi matrisi
lang: tr
---

<span class="anker" id="stufe-5"></span>

:::zweck
Birçok hesap adımı tek bir sayı değil, birkaç sayı verir: Bir matris-vektör çarpımı bir vektörden başka bir vektör yapar. Bu tür fonksiyonlar için Jacobi matrisi bütün çıktıların bütün girdilere göre kısmi türevlerini bir araya toplar. Jacobi matrisi doğrusal yaklaşımın matrisidir ve en sık kullanılan iki yapı taşı, doğrusal dönüşümler ve eleman eleman uygulanan fonksiyonlar için özellikle basit bir biçime sahiptir.
:::

### Çok çıktılı fonksiyonlar

<span class="anker" id="stufe-5-1"></span>

[Bölüm 1, Kesim 8](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8)'de bir $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ doğrusal dönüşümü $\mathbb{R}^n$ uzayının vektörlerini $\mathbb{R}^m$ uzayının vektörlerine gönderiyordu, [Bölüm 1, Kesim 15.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/elementweise-rechnen-und-tensoren.html#stufe-15-2)'de ise bir fonksiyon bir vektörün her bileşenine ayrı ayrı uygulanıyordu. İki durumda da bir vektörden birkaç sayı çıkar. Bunların her biri kendi başına çok değişkenli bir fonksiyondur.

:::definition Tanım 5.1 (Vektör değerli fonksiyon)
<span class="anker" id="satz-5-1"></span>

Bir $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ fonksiyonu her $\mathbf{x}\in\mathbb{R}^n$ vektörüne bir

$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}g_1(\mathbf{x})\\ \vdots\\ g_m(\mathbf{x})\end{pmatrix}\in\mathbb{R}^m$$

vektörü karşılık getirir; buna __vektör değerli__ fonksiyon denir. $g_1,\dots,g_m:\mathbb{R}^n\to\mathbb{R}$ fonksiyonlarına onun bileşenleri denir.
:::

Bu bölüm vektör değerli fonksiyonları vektörler gibi kalın, değeri bir sayı olan fonksiyonları normal yazıyla yazar.

::::beispiel [Sayısal örnek]
Kesim [5](#stufe-5) ve [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6) boyunca bize şu $\mathbf{g}:\mathbb{R}^2\to\mathbb{R}^2$ fonksiyonu eşlik ediyor:

<span class="anker" id="gl-5-1"></span>
$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}x_1x_2\\ 2x_1+x_2^2\end{pmatrix},\qquad \mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix}. \tag{5.1}$$

Bileşenleri $g_1(\mathbf{x})=x_1x_2$ ve $g_2(\mathbf{x})=2x_1+x_2^2$ olur.
::::

⁠**Kısacası:** Bir $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ vektör değerli fonksiyonu, her çıktı için bir tane olmak üzere $n$ değişkenli $m$ fonksiyondan oluşur.

### Jacobi matrisi

<span class="anker" id="stufe-5-2"></span>

Her $g_i$ bileşeninin, her girdiye göre bir tane olmak üzere $n$ kısmi türevi vardır. Hepsi birlikte $m\cdot n$ sayı eder. Bunlar her çıktı için bir satır ve her girdi için bir sütun olan bir tabloya yerleştirilir.

:::definition Tanım 5.2 (Jacobi matrisi)
<span class="anker" id="satz-5-2"></span>

$\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ fonksiyonunun bileşenlerinin bütün kısmi türevleri $\mathbf{x}$ noktasında varsa

<span class="anker" id="gl-5-2"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}\dfrac{\partial g_1}{\partial x_1}&\cdots&\dfrac{\partial g_1}{\partial x_n}\\ \vdots&&\vdots\\ \dfrac{\partial g_m}{\partial x_1}&\cdots&\dfrac{\partial g_m}{\partial x_n}\end{pmatrix},\qquad \bigl(\mathbf{J}_{\mathbf{g}}(\mathbf{x})\bigr)_{ij}=\frac{\partial g_i}{\partial x_j}(\mathbf{x}), \tag{5.2}$$

$m\times n$ tipindeki matrise $\mathbf{g}$ fonksiyonunun $\mathbf{x}$ noktasındaki __Jacobi matrisi__ denir.
:::

$i$ satırı $g_i$ çıktısına aittir; satır olarak yazılmış gradyanıdır: $\nabla g_i(\mathbf{x})^{\top}$. $j$ sütunu $x_j$ girdisine aittir; yalnızca $x_j$ değiştirildiğinde bütün çıktıların aynı anda nasıl tepki verdiğini söyler. Tek bir çıktısı olan bir $f:\mathbb{R}^n\to\mathbb{R}$ fonksiyonu için Jacobi matrisi $1\times n$ tipinde bir matristir, yani satır olarak yazılmış gradyan: $\mathbf{J}_f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}$. Matris adını matematikçi Carl Gustav Jacob Jacobi'den alır.

::::beispiel [Sayısal örnek]
[(5.1)](#gl-5-1) bağıntısındaki $\mathbf{g}$ için şunlar bulunur:

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}x_2&x_1\\2&2x_2\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}.$$

İlk sütun $(2,\,2)^{\top}$ şunu söyler: $x_1$ küçük bir $h$ kadar artarsa iki çıktı da yaklaşık $2h$ kadar artar. İkinci sütun $(1,\,4)^{\top}$ şunu söyler: $x_2$ artarsa ikinci çıktı birincisinin dört katı güçlü tepki verir.
::::

⁠**Kısacası:** Jacobi matrisinin her çıktı için bir satırı ve her girdi için bir sütunu vardır; $(i,j)$ elemanı $\partial g_i/\partial x_j$ olur.

### Jacobi matrisiyle doğrusal yaklaşım

<span class="anker" id="stufe-5-3"></span>

Her bileşenin [(3.4)](partielle-ableitungen-und-der-gradient.html#gl-3-4) biçiminde bir doğrusal yaklaşımı vardır. $m$ yaklaşımın hepsi alt alta yazılırsa solda $\mathbf{g}(\mathbf{x}+\mathbf{h})$ vektörünün bileşenleri, sağda Jacobi matrisinin satırları çarpı $\mathbf{h}$ durur. Bu, [Bölüm 1, Kesim 7.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-2)'deki satır bakışına göre bir matris-vektör çarpımıdır.

:::satz Teorem 5.3 (Vektör değerli bir fonksiyonun doğrusal yaklaşımı)
<span class="anker" id="satz-5-3"></span>

$\mathbf{g}$ fonksiyonunun her bileşeni $\mathbf{x}$ noktasında türevlenebilirse şu geçerlidir:

<span class="anker" id="gl-5-3"></span>
$$\mathbf{g}(\mathbf{x}+\mathbf{h})=\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}+\mathbf{r}(\mathbf{h})\qquad\text{burada}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{\lVert\mathbf{r}(\mathbf{h})\rVert}{\lVert\mathbf{h}\rVert}=0 . \tag{5.3}$$
:::

:::beweis Vektör değerli bir fonksiyonun doğrusal yaklaşımı
$\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$ vektörünün $i$ bileşeni $\nabla g_i(\mathbf{x})^{\top}\mathbf{h}$ olur. Türevlenebilirliğin tanımı [(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5) uyarınca her $i$ için $r_i(\mathbf{h})/\lVert\mathbf{h}\rVert$ bölümü $0$'a gider. $\lVert\mathbf{r}\rVert\le|r_1|+\dots+|r_m|$ olduğundan $\lVert\mathbf{r}(\mathbf{h})\rVert/\lVert\mathbf{h}\rVert$ de $0$'a gider.
:::

Yani $\mathbf{x}$ yakınında $\mathbf{g}$, $\mathbf{h}\mapsto\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$ doğrusal dönüşümü gibi davranır ve [Bölüm 1, Kesim 8.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-2)'ye göre her doğrusal dönüşüme tam olarak bir matris karşılık gelir. Jacobi matrisi bu matristir. Büyüteç altında $\mathbf{g}$, $\mathbf{x}$ çevresindeki küçük bir ızgarayı, $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ matrisinin birim ızgarayı biçimlendirdiği gibi biçimlendirir: Izgara döner, gerilir ya da kaymaya uğrar, ama düz çizgiler neredeyse düz kalır.

::::beispiel [Sayısal örnek]
[(5.1)](#gl-5-1) bağıntısındaki $\mathbf{g}$ için $(1,\,2)$ noktasında ve $\mathbf{h}=(0{,}1;\ -0{,}1)^{\top}$ ile şunlar bulunur:

$$\mathbf{J}_{\mathbf{g}}(1,2)\,\mathbf{h}=\begin{pmatrix}2\cdot0{,}1+1\cdot(-0{,}1)\\2\cdot0{,}1+4\cdot(-0{,}1)\end{pmatrix}=\begin{pmatrix}0{,}1\\-0{,}2\end{pmatrix}, \qquad \mathbf{g}(1{,}1;\ 1{,}9)\approx\begin{pmatrix}2{,}1\\5{,}8\end{pmatrix}.$$

Tam değer $\mathbf{g}(1{,}1;\ 1{,}9)=(2{,}09;\ 5{,}81)^{\top}$ olur. Şekil [10](#abb-10) çarpımı satır satır gösteriyor.

:::abbildung ml/k3rjacobi 10
$\mathbf{g}$ fonksiyonunun $\mathbf{x}=(1,\,2)^{\top}$ noktasındaki doğrusal yaklaşımında değişim, bir matris-vektör çarpımı olarak: Her satır, bir çıktının gradyanı ile yer değiştirmenin iç çarpımıdır.
:::
::::

⁠**Kısacası:** $\mathbf{x}$ yakınında $\mathbf{g}(\mathbf{x}+\mathbf{h})\approx\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$ olur; $\mathbf{g}$ küçük ölçekte bir doğrusal dönüşüm gibi davranır ve Jacobi matrisi bu dönüşümün matrisidir.

### İki önemli Jacobi matrisi

<span class="anker" id="stufe-5-4"></span>

Verilerle yapılan hesaplarda iki yapı taşı sürekli karşımıza çıkar: matris-vektör çarpımı ve her bileşene ayrı ayrı uygulanan fonksiyonlar. Bunların Jacobi matrislerine tekrar tekrar ihtiyaç duyulur ve ikisi de hesap yapmadan verilebilir.

:::satz Teorem 5.4 (Yapı taşlarının Jacobi matrisleri)
<span class="anker" id="satz-5-4"></span>

<ol class="al">

<li>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ ve $\mathbf{b}\in\mathbb{R}^m$ olmak üzere $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$ için her noktada $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\mathbf{A}$ olur.

</li>

<li>

$\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^n$, tek değişkenli türevlenebilir bir $\varphi$ fonksiyonunu her bileşene uyguluyorsa, $g_i(\mathbf{x})=\varphi(x_i)$, şu geçerlidir:

<span class="anker" id="gl-5-4"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\operatorname{diag}\bigl(\varphi'(x_1),\,\dots,\,\varphi'(x_n)\bigr). \tag{5.4}$$

</li>

</ol>
:::

:::beweis Yapı taşlarının Jacobi matrisleri
(a) $i$ bileşeni $g_i(\mathbf{x})=\sum_ka_{ik}x_k+b_i$ olur. $x_j$ değişkenine göre türev alınınca yalnızca $k=j$ olan terim kalır, yani $\partial g_i/\partial x_j=a_{ij}$. (b) $g_i=\varphi(x_i)$ bileşeni yalnızca $x_i$ değişkenine bağlıdır. Bu yüzden $x_j$ değişkenine göre türevi $j\ne i$ için $0$, $j=i$ için $\varphi'(x_i)$ olur.
:::

İki sonucun da basit bir nedeni vardır. Afin bir dönüşüm, $\mathbf{b}$ ötelemesi dışında zaten doğrusaldır; en iyi doğrusal yaklaşımı, $\mathbf{b}$ olmadan kendisidir. Eleman eleman uygulanan bir fonksiyonda her girdi yalnızca kendi çıktısına etki eder; köşegen dışındaki bütün elemanlar sıfırdır, çünkü farklı bileşenler arasında bağlantı yoktur.

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\bigr)$ için $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ dönüşümünün Jacobi matrisi her yerde $\mathbf{A}$ matrisinin kendisidir. Her bileşenin karesi alınırsa, $\varphi(t)=t^2$, $\mathbf{x}=(1,\,-2,\,3)^{\top}$ noktasında Jacobi matrisi $\operatorname{diag}(2;\,-4;\,6)$ olur. Lojistik fonksiyon $\mathbf{x}=(0,\,2)^{\top}$ vektörünün her bileşenine uygulanırsa Jacobi matrisi [(2.4)](die-kettenregel.html#gl-2-4) uyarınca $\operatorname{diag}\bigl(\sigma'(0);\,\sigma'(2)\bigr)\approx\operatorname{diag}(0{,}25;\ 0{,}105)$ olur.
::::

⁠**Kısacası:** $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}+\mathbf{b}$ dönüşümünün Jacobi matrisi $\mathbf{A}$ olur; eleman eleman uygulanan bir fonksiyonunki ise tek tek türevlerden oluşan köşegen matristir.

:::hintergrund Alan çarpanı olarak Jacobi matrisinin determinantı
[Bölüm 1, Kesim 14.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-3)'e göre doğrusal bir dönüşüm her şeklin alanını aynı $|\det\mathbf{A}|$ çarpanıyla çarpar. $\mathbf{g}$ küçük ölçekte $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ gibi davrandığından bu, $\mathbf{g}$ için de yaklaşık olarak geçerlidir: $\mathbf{x}$ çevresinde alanı $F$ olan küçük bir kare, alanı $|\det\mathbf{J}_{\mathbf{g}}(\mathbf{x})|\cdot F$ olan ve neredeyse paralelkenar olan bir şekle dönüşür. [(5.1)](#gl-5-1) bağıntısındaki $\mathbf{g}$ için $\det\mathbf{J}_{\mathbf{g}}(1,2)=2\cdot4-1\cdot2=6$ olur: $(1,\,2)$ yakınında $\mathbf{g}$ alanları yaklaşık altı katına büyütür. Bilinen bir örnek kutupsal koordinatlardır, $\mathbf{g}(r,\varphi)=(r\cos\varphi,\ r\sin\varphi)^{\top}$. Bu dönüşümün Jacobi matrisinin sütunları $(\cos\varphi,\,\sin\varphi)^{\top}$ ve $(-r\sin\varphi,\,r\cos\varphi)^{\top}$, determinantı ise $r\cos^2\varphi+r\sin^2\varphi=r$ olur. Kenarları $\Delta r$ ve $\Delta\varphi$ olan küçük bir dikdörtgen, alanı yaklaşık $r\,\Delta r\,\Delta\varphi$ olan bir halka parçasına dönüşür, çünkü $r$ uzaklığında $\Delta\varphi$ açısına ait yayın uzunluğu $r\,\Delta\varphi$ olur.
:::

:::aufgabe Alıştırma 17 ★ Jacobi matrislerini hesaplamak
<span class="anker" id="aufg-17"></span>

Verilen noktada Jacobi matrisini hesaplayın.

<ol class="al">

<li>

$(3,\,1)$ noktasında $\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1-x_2,\ x_1x_2)^{\top}$;

</li>

<li>

$(0,\,1,\,-1)$ noktasında $\mathbf{g}(\mathbf{x})=(\mathrm{e}^{x_1},\,\mathrm{e}^{x_2},\,\mathrm{e}^{x_3})^{\top}$;

</li>

<li>

$(1,\,2)$ noktasında [(3.1)](partielle-ableitungen-und-der-gradient.html#gl-3-1) bağıntısındaki $f(\mathbf{x})=x_1^2x_2+x_2^2$. Matrisin şekli nedir ve bu matris nedir?

</li>

</ol>

:::loesung
(a) Jacobi matrisinin üç satırı ve iki sütunu vardır:

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}1&1\\1&-1\\x_2&x_1\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(3,1)=\begin{pmatrix}1&1\\1&-1\\1&3\end{pmatrix}.$$

(b) Fonksiyon eleman eleman işler; [(5.4)](#gl-5-4) uyarınca $\mathbf{J}=\operatorname{diag}(\mathrm{e}^0;\,\mathrm{e}^1;\,\mathrm{e}^{-1})\approx\operatorname{diag}(1;\ 2{,}718;\ 0{,}368)$.

(c) Tek çıktılı bir fonksiyonun Jacobi matrisi $1\times2$ tipindedir; bu, satır olarak yazılmış gradyandır: $\mathbf{J}_f(1,2)=(4\ \ 5)=\nabla f(1,2)^{\top}$.
:::
:::

:::aufgabe Alıştırma 18 ★★ Düzlemin bir dönüşümünün doğrusal yaklaşımı
<span class="anker" id="aufg-18"></span>

$\mathbf{g}(\mathbf{x})=(x_1^2-x_2,\ x_1x_2)^{\top}$ olsun.

<ol class="al">

<li>

$\mathbf{J}_{\mathbf{g}}(2,1)$ matrisini ve onunla $\mathbf{g}(2{,}05;\ 0{,}9)$ için bir yaklaşık değer hesaplayın. Tam değerle karşılaştırın.

</li>

<li>

Birinci çıktının değişmesi, ikincisinin ise doğrusal yaklaşımda hiç değişmemesi için girdiler nasıl kaydırılmalıdır? Böyle bir $\mathbf{h}$ yer değiştirmesi verin.

</li>

</ol>

:::loesung
(a) $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}2x_1&-1\\x_2&x_1\end{smallmatrix}\bigr)$, dolayısıyla $\mathbf{J}_{\mathbf{g}}(2,1)=\bigl(\begin{smallmatrix}4&-1\\1&2\end{smallmatrix}\bigr)$ ve $\mathbf{g}(2,1)=(3,\,2)^{\top}$ olur. $\mathbf{h}=(0{,}05;\ -0{,}1)^{\top}$ ile

$$\mathbf{J}_{\mathbf{g}}\mathbf{h}=\begin{pmatrix}0{,}2+0{,}1\\0{,}05-0{,}2\end{pmatrix}=\begin{pmatrix}0{,}3\\-0{,}15\end{pmatrix},\qquad \mathbf{g}(2{,}05;\ 0{,}9)\approx\begin{pmatrix}3{,}3\\1{,}85\end{pmatrix}.$$

Tam değer $\mathbf{g}(2{,}05;\ 0{,}9)=(4{,}2025-0{,}9;\ 1{,}845)^{\top}=(3{,}3025;\ 1{,}845)^{\top}$ olur.

(b) İkinci çıktı doğrusal yaklaşımda $h_1+2h_2$ kadar değişir; bu, $(2,\,-1)^{\top}$ doğrultusundaki $\mathbf{h}$ için sıfırdır. Tam bu vektör kadarlık bir adımda birinci çıktı $4\cdot2-1\cdot(-1)=9$ kadar değişir. Demek ki iki girdi de değişmelidir: $x_1$ artar, $x_2$ yarısı kadar azalır; örneğin $\mathbf{h}=(0{,}02;\ -0{,}01)^{\top}$, etkisi $(0{,}09;\ 0)^{\top}$ olur.
:::
:::

:::aufgabe Alıştırma 19 ★★★ $\mathbf{g}$ alanları ne kadar büyütür
<span class="anker" id="aufg-19"></span>

$\mathbf{g}$, [(5.1)](#gl-5-1) bağıntısındaki gibi olsun.

<ol class="al">

<li>

Köşeleri $(1,\,2)$, $(1{,}1;\ 2)$, $(1{,}1;\ 2{,}1)$ ve $(1;\ 2{,}1)$ olan karenin dört köşesinin görüntülerini hesaplayın.

</li>

<li>

Görüntüler neredeyse bir paralelkenar oluşturur. Bu paralelkenarın alanını $\mathbf{g}(1,2)$ noktasından çıkan iki kenarın görüntüleriyle kestirin ve $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0{,}01$ ile karşılaştırın.

</li>

</ol>

:::loesung
(a) $\mathbf{g}(\mathbf{x})=(x_1x_2,\ 2x_1+x_2^2)^{\top}$ ile:

$$\mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix},\quad \mathbf{g}(1{,}1;\,2)=\begin{pmatrix}2{,}2\\6{,}2\end{pmatrix},\quad \mathbf{g}(1{,}1;\,2{,}1)=\begin{pmatrix}2{,}31\\6{,}61\end{pmatrix},\quad \mathbf{g}(1;\,2{,}1)=\begin{pmatrix}2{,}1\\6{,}41\end{pmatrix}.$$

(b) $\mathbf{g}(1,2)$ noktasından çıkan iki kenarın görüntüleri $(0{,}2;\ 0{,}2)^{\top}$ ve $(0{,}1;\ 0{,}41)^{\top}$ olur. Bu iki vektörün gerdiği paralelkenarın alanı, [Bölüm 1, Kesim 14.1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-1)'e göre $|0{,}2\cdot0{,}41-0{,}1\cdot0{,}2|=0{,}062$ olur. Jacobi matrisi $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0{,}01=6\cdot0{,}01=0{,}06$ öngörür. Fark, karenin istenildiği kadar küçük olmamasından kaynaklanır; dördüncü köşe de $(2{,}31;\ 6{,}61)$ noktasındadır, yani gerçek bir paralelkenarın dördüncü köşesinin bulunacağı $(2{,}3;\ 6{,}61)$ noktasına yalnızca çok yakındır.
:::
:::
