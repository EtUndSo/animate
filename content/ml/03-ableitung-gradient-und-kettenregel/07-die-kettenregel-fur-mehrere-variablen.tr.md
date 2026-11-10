---
title: Çok değişkenli zincir kuralı
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15230700
summary: Çok değişkenli hesaplar, çok girdili ve çok çıktılı fonksiyonlardan oluşan zincirlerdir.
tags: eğri, hız vektörü
lang: tr
---

<span class="anker" id="stufe-6"></span>

:::zweck
Çok değişkenli hesaplar, çok girdili ve çok çıktılı fonksiyonlardan oluşan zincirlerdir. Zincir kuralı bunlara da aktarılır: Aşamaların Jacobi matrisleri çarpılır. Bileşen bileşen bu, bir değişimin bir girdiden çıktıya ulaştığı bütün yollar üzerinden toplama yapmak demektir. Bir sayının gradyanı için burada devrik Jacobi matrisi ortaya çıkar.
:::

### Matris çarpımı olarak zincir kuralı

<span class="anker" id="stufe-6-1"></span>

İki aşama art arda bağlanmış olsun: $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$, $\mathbf{x}$ vektöründen $\mathbf{u}=\mathbf{g}(\mathbf{x})$ ara vektörünü, $\mathbf f:\mathbb{R}^m\to\mathbb{R}^p$ de bundan $\mathbf{y}=\mathbf f(\mathbf{u})$ vektörünü yapar. Küçük bir $\Delta\mathbf{x}$ değişimi Kesim [2.2](die-kettenregel.html#stufe-2-2)'deki gibi izlenir. Birinci aşama onu [(5.3)](die-jacobi-matrix.html#gl-5-3) uyarınca $\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$ olarak, ikincisi $\Delta\mathbf{y}\approx\mathbf{J}_{\mathbf f}\,\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$ olarak iletir. İki sayının çarpımı, iki matrisin çarpımına dönüşür. Bu, [Bölüm 1, Kesim 9.4](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-4) ile uyumludur: Art arda iki doğrusal aşama, matrisi iki matrisin çarpımı olan tek bir doğrusal aşamadır.

:::satz Teorem 6.1 (Çok değişkenli zincir kuralı)
<span class="anker" id="satz-6-1"></span>

$\mathbf{g}$, $\mathbf{x}$ noktasında ve $\mathbf f$, $\mathbf{g}(\mathbf{x})$ noktasında türevlenebilirse $\mathbf f\circ\mathbf{g}$, $\mathbf{x}$ noktasında türevlenebilirdir ve şu geçerlidir:

<span class="anker" id="gl-6-1"></span>
$$\mathbf{J}_{\mathbf f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_{\mathbf f}\bigl(\mathbf{g}(\mathbf{x})\bigr)\,\mathbf{J}_{\mathbf{g}}(\mathbf{x}). \tag{6.1}$$
:::

Şekiller birbirine uyar: Solda $p\times n$ tipinde bir matris, sağda $p\times m$ tipinde bir matris çarpı $m\times n$ tipinde bir matris durur. Ortak $m$ sayısı ara değişkenlerin sayısıdır. Tek değişkende olduğu gibi her Jacobi matrisi, kendi aşamasının çalıştığı yerde hesaplanır; yani $\mathbf{J}_{\mathbf f}$, $\mathbf{u}=\mathbf{g}(\mathbf{x})$ ara değerinde. $\mathbf f_L\circ\dots\circ\mathbf f_1$ gibi daha uzun zincirlerde Jacobi matrisi $\mathbf{J}_{\mathbf f_L}\cdots\mathbf{J}_{\mathbf f_1}$ çarpımıdır; en son uygulanan aşama en soldadır. Sayılardan farklı olarak çarpanların yeri değiştirilemez.

:::beweis Çok değişkenli zincir kuralı
İspat, Kesim [2.2](die-kettenregel.html#stufe-2-2)'deki gibi, mutlak değerler yerine uzunluklarla yapılır. $\mathbf{u}=\mathbf{g}(\mathbf{x})$ ve $\mathbf{k}=\mathbf{g}(\mathbf{x}+\mathbf{h})-\mathbf{u}=\mathbf{J}_{\mathbf{g}}\mathbf{h}+\mathbf{r}_{\mathbf{g}}(\mathbf{h})$ ile şu elde edilir:

$$\mathbf f\bigl(\mathbf{g}(\mathbf{x}+\mathbf{h})\bigr)-\mathbf f(\mathbf{u})=\mathbf{J}_{\mathbf f}\,\mathbf{k}+\mathbf{r}_{\mathbf f}(\mathbf{k})=\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}\,\mathbf{h}+\mathbf{J}_{\mathbf f}\,\mathbf{r}_{\mathbf{g}}(\mathbf{h})+\mathbf{r}_{\mathbf f}(\mathbf{k}).$$

Ortadaki hata $\lVert\mathbf{h}\rVert$'den hızlı sıfıra gider, çünkü $\mathbf{r}_{\mathbf{g}}$ de böyledir ve sabit bir matrisle çarpmak uzunlukları en fazla sabit bir çarpan kadar büyütür. Sonuncusu $\lVert\mathbf{k}\rVert$'den hızlı sıfıra gider ve $\mathbf{h}$ küçük olduğu sürece $\lVert\mathbf{k}\rVert$ en fazla $\lVert\mathbf{h}\rVert$ uzunluğunun sabit bir katıdır. Dolayısıyla $\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}$, $\mathbf f\circ\mathbf{g}$ fonksiyonunun doğrusal yaklaşımının matrisidir.
:::

::::beispiel [Sayısal örnek]
$\mathbf{g}$, [(5.1)](die-jacobi-matrix.html#gl-5-1) bağıntısındaki gibi olsun ve $f(\mathbf{u})=u_1^2+3u_2$, tek çıktılı bir fonksiyon ($p=1$) olsun. Bileşkeleri $F(\mathbf{x})=f(\mathbf{g}(\mathbf{x}))=x_1^2x_2^2+6x_1+3x_2^2$ olur. $\mathbf{x}=(1,\,2)^{\top}$ noktasında $\mathbf{u}=\mathbf{g}(\mathbf{x})=(2,\,6)^{\top}$ ve $\mathbf{J}_f(\mathbf{u})=(2u_1\ \ 3)=(4\ \ 3)$ olur. [(6.1)](#gl-6-1) uyarınca şu bulunur:

$$\mathbf{J}_F(1,2)=\begin{pmatrix}4&3\end{pmatrix}\begin{pmatrix}2&1\\2&4\end{pmatrix}=\begin{pmatrix}4\cdot2+3\cdot2&\ 4\cdot1+3\cdot4\end{pmatrix}=\begin{pmatrix}14&16\end{pmatrix}.$$

Açık yazılmış fonksiyonla sağlama: $\partial_1F=2x_1x_2^2+6=8+6=14$ ve $\partial_2F=2x_1^2x_2+6x_2=4+12=16$.
::::

⁠**Kısacası:** Bir bileşkenin Jacobi matrisi, aşamaların Jacobi matrislerinin çarpımıdır, en son uygulanan aşama solda: $\mathbf{J}_{\mathbf f\circ\mathbf{g}}=\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}$.

### Tüm yollar üzerinden toplam

<span class="anker" id="stufe-6-2"></span>

[(6.1)](#gl-6-1) matris çarpımı tek bir eleman için açık yazılırsa orada ara değişkenler üzerinden bir toplam durur. Tek çıktılı bir $F=f\circ\mathbf{g}$ fonksiyonu için şu geçerlidir:

<span class="anker" id="gl-6-2"></span>
$$\frac{\partial F}{\partial x_j}(\mathbf{x})=\sum_{i=1}^m\frac{\partial f}{\partial u_i}(\mathbf{u})\,\frac{\partial u_i}{\partial x_j}(\mathbf{x}),\qquad \mathbf{u}=\mathbf{g}(\mathbf{x}). \tag{6.2}$$

Bu toplamın anlaşılır bir anlamı vardır. $x_j$ değişkenindeki bir değişim $F$'ye doğrudan değil, $u_1,\dots,u_m$ ara değişkenleri üzerinden ulaşır. Her ara değişken bir yoldur: $u_i$ üzerinden geçen yolda değişim önce $\partial u_i/\partial x_j$ ile, sonra $\partial f/\partial u_i$ ile çarpılır. Çıktıda bütün yolların katkıları buluşur ve toplanır (Şekil [11](#abb-11)). Zincir kuralı bu yüzden çoğu zaman şöyle özetlenir: Bir yol boyunca çarp, bütün yollar üzerinden topla.

:::abbildung ml/k3wege 11
$(1,\,2)$ noktasında $F=f\circ\mathbf{g}$ için bir yol ağı olarak zincir kuralı. Her kenarda, hedefin kenarın başlangıç noktasına göre yerel türevi yazılıdır. $x_1$'den $F$'ye iki yol gider, $u_1$ üzerinden (mavi) ve $u_2$ üzerinden (turuncu). Her yol boyunca çarpanlar çarpılır, iki katkı toplanır. İçinden akan miktarı her borunun kendi çarpanıyla çoğalttığı ve akışların hedefte birleştiği bir boru ağı düşünülebilir.
:::

::::beispiel [Sayısal örnek 1]
Önceki alt kesimdeki $F=f\circ\mathbf{g}$ için $(1,\,2)$ noktasında kenar çarpanları şunlardır:

$$\frac{\partial u_1}{\partial x_1}=x_2=2,\quad \frac{\partial u_1}{\partial x_2}=x_1=1,\quad \frac{\partial u_2}{\partial x_1}=2,\quad \frac{\partial u_2}{\partial x_2}=2x_2=4,\quad \frac{\partial f}{\partial u_1}=2u_1=4,\quad \frac{\partial f}{\partial u_2}=3 .$$

İki yol üzerinden toplandığında bu, matris çarpımındaki gibi $14$ ve $16$ elemanlarını verir (Şekil [12](#abb-12)).

:::abbildung ml/k3rwege 12
$F=f\circ\mathbf{g}$ fonksiyonunun $(1,\,2)$ noktasındaki kısmi türevleri, $u_1$ ve $u_2$ üzerinden geçen iki yol üzerinden toplamlar olarak.
:::
::::

::::beispiel [Sayısal örnek 2]
Bir girdi, iki yol. $g_1(x)=x^2$ ve $g_2(x)=3x$ olmak üzere $F(x)=g_1(x)\,g_2(x)$ olsun, yani $f(\mathbf{u})=u_1u_2$. $u_1$ ve $u_2$ üzerinden geçen yollar şunu verir:

$$\frac{\mathrm{d} F}{\mathrm{d} x}=\frac{\partial f}{\partial u_1}\,g_1'(x)+\frac{\partial f}{\partial u_2}\,g_2'(x)=u_2\cdot2x+u_1\cdot3=3x\cdot2x+x^2\cdot3=9x^2 .$$

Sağlama: $F(x)=3x^3$ fonksiyonunun türevi $9x^2$ olur. Bir yolu unutan $6x^2$ ya da $3x^2$ bulur. Bu arada bu, tam olarak [(1.5)](die-ableitung.html#gl-1-5) çarpım kuralıdır: Çarpım kuralı, iki yol için zincir kuralıdır.
::::

⁠**Kısacası:** Bileşen bileşen zincir kuralı, girdiden çıktıya giden bütün yollar üzerinden bir toplamdır; her yol boyunca yerel türevler çarpılır.

:::hintergrund Yollar üzerinden neden toplanır
Nedeni Kesim [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4)'teki gözlemdir: Küçük değişimlerde etkiler toplanır. $x_j$, $\Delta x_j$ kadar değiştirilirse bütün ara değişkenler aynı anda, her biri yaklaşık $\frac{\partial u_i}{\partial x_j}\Delta x_j$ kadar değişir. Bu eş zamanlı değişimlerin $f$ üzerinde nasıl etki ettiğini $f$ fonksiyonunun $u_1,\dots,u_m$ değişkenlerindeki doğrusal yaklaşımı söyler: Her biri $\frac{\partial f}{\partial u_i}\Delta u_i$ katkısını yapar ve katkılar, her ara değişken tek başına değişmiş gibi toplanır. Yollar üzerinden toplam, yani bu tek tek katkıların toplamıdır. Daha uzun zincirlerde bu devam eder: Bir yol o zaman art arda birkaç ara değişkenden geçer, yol boyunca bütün kenar çarpanları çarpılır ve sonunda girdiden çıktıya giden bütün yollar üzerinden toplanır. Yolların sayısı bu sırada çok hızlı büyüyebilir; onların akıllıca nasıl bir araya getirileceğini Kesim [10](automatische-differentiation.html#stufe-10) gösterir.
:::

### Bir bileşkenin gradyanı

<span class="anker" id="stufe-6-3"></span>

Tek çıktılı bir $F=f\circ\mathbf{g}$ fonksiyonu için Jacobi matrisi satır olarak yazılmış gradyandır. Gradyan, bu bölümün uzlaştığı gibi sütun olarak istenirse zincir kuralının devriği alınmalıdır.

:::satz Teorem 6.2 (Bir bileşkenin gradyanı)
<span class="anker" id="satz-6-2"></span>

$\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$, $\mathbf{x}$ noktasında ve $f:\mathbb{R}^m\to\mathbb{R}$, $\mathbf{u}=\mathbf{g}(\mathbf{x})$ noktasında türevlenebilirse şu geçerlidir:

<span class="anker" id="gl-6-3"></span>
$$\nabla(f\circ\mathbf{g})(\mathbf{x})=\mathbf{J}_{\mathbf{g}}(\mathbf{x})^{\top}\,\nabla f(\mathbf{u}). \tag{6.3}$$
:::

:::beweis Bir bileşkenin gradyanı
[(6.1)](#gl-6-1) uyarınca $\nabla(f\circ\mathbf{g})(\mathbf{x})^{\top}=\mathbf{J}_{f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_f(\mathbf{u})\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\nabla f(\mathbf{u})^{\top}\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ olur. İki tarafın da [Bölüm 1, Kesim 10.1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1)'deki $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ kuralıyla devriği alınırsa iddia çıkar.
:::

Devrik yalnızca bir muhasebe meselesidir: Gradyan sütun olarak yazıldığı hâlde Jacobi matrisinin satırları çıktılara ait olduğu için ortaya çıkar. İçerik olarak [(6.3)](#gl-6-3) bağıntısı [(6.2)](#gl-6-2) ile aynı şeyi söyler: $\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ vektörünün $j$ bileşeni, $\mathbf{J}_{\mathbf{g}}$ matrisinin $j$ sütunu çarpı $\nabla f$, yani $x_j$'den başlayan yollar üzerinden toplamdır. İç fonksiyon doğrusalsa, $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}$, Kesim [5.4](die-jacobi-matrix.html#stufe-5-4)'e göre buradan $\nabla_{\mathbf{x}}f(\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\,\nabla f(\mathbf{A}\mathbf{x})$ kuralı çıkar. Nabladaki $\mathbf{x}$ indisi, gradyanın hangi değişkene göre alındığını söyler.

::::beispiel [Sayısal örnek]
[(6.1)](#gl-6-1) ile ilgili örnekteki $\mathbf{J}_{\mathbf{g}}(1,2)$ ve $\nabla f(\mathbf{u})=(4,\,3)^{\top}$ ile şu elde edilir:

$$\nabla F(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}^{\top}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}2&2\\1&4\end{pmatrix}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}8+6\\4+12\end{pmatrix}=\begin{pmatrix}14\\16\end{pmatrix}.$$

Devrik alınmasaydı $\mathbf{J}_{\mathbf{g}}\,\nabla f=(8+3;\ 8+12)^{\top}=(11,\,20)^{\top}$ bulunurdu ve bu yanlıştır.
::::

:::warnung Devriği unutmayın
İç fonksiyonun Jacobi matrisi simetrikse unutulan bir devrik fark edilmez. Bu yüzden kendi türettiğiniz bir gradyan formülünü, Jacobi matrisi simetrik olmayan bir örnekte kontrol edin. $\mathbf{J}_{\mathbf{g}}$ matrisinin satır ve sütun sayısı aynı değilse şekillere bir bakış hatayı hemen ele verir: $\nabla f$ vektörünün $m$ elemanı vardır, $\mathbf{J}_{\mathbf{g}}^{\top}$ matrisinin $m$ sütunu vardır ve yalnızca $\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ çarpımı $n$ elemanlı bir vektör verir.
:::

⁠**Kısacası:** Bir bileşkenin gradyanı, iç fonksiyonun devrik Jacobi matrisi çarpı dış fonksiyonun gradyanıdır: $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$.

### Bir eğri boyunca türev

<span class="anker" id="stufe-6-4"></span>

Harita üzerinde bir yürüyüş bir eğridir: Her $t$ anında insan bir $\boldsymbol{\gamma}(t)\in\mathbb{R}^d$ konumundadır. Yol boyunca $f(\boldsymbol{\gamma}(t))$ yüksekliği ne kadar hızlı değişir? Bu, tek bir $t$ girdi değişkeni olan zincir kuralının özel bir durumudur.

:::definition Tanım 6.3 (Eğri ve hız)
<span class="anker" id="satz-6-3"></span>

Bir __eğri__, bir $\boldsymbol{\gamma}:\mathbb{R}\to\mathbb{R}^d$, $t\mapsto\boldsymbol{\gamma}(t)=(\gamma_1(t),\dots,\gamma_d(t))^{\top}$ fonksiyonudur. Türevi olan $\boldsymbol{\gamma}'(t)=(\gamma_1'(t),\dots,\gamma_d'(t))^{\top}$ vektörüne __hız vektörü__ denir.
:::

Hız vektörü $\boldsymbol{\gamma}$ fonksiyonunun Jacobi matrisidir, $d\times1$ tipinde bir matris. O anda hareket edilen doğrultuyu gösterir ve uzunluğu sürattir. $n=1$ ile [(6.1)](#gl-6-1) uyarınca türevlenebilir bir $f$ için şu geçerlidir:

<span class="anker" id="gl-6-4"></span>
$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)=\nabla f\bigl(\boldsymbol{\gamma}(t)\bigr)^{\top}\boldsymbol{\gamma}'(t). \tag{6.4}$$

Bir $\boldsymbol{\gamma}(t)=\mathbf{x}+t\,\mathbf{h}$ doğrusu için $\boldsymbol{\gamma}'=\mathbf{h}$ ve değişim hızı $\nabla f(\mathbf{x})^{\top}\mathbf{h}$ olur; $\mathbf{h}$ vektörünün uzunluğu $1$ ise bu, Kesim [4.1](richtungsableitung-und-steilster-anstieg.html#stufe-4-1)'deki yönlü türevdir. Bir eğri tamamen bir eş yükselti eğrisi üzerinde uzanıyorsa $f(\boldsymbol{\gamma}(t))$ sabittir, sol taraf yani sıfırdır: Gradyan, eş yükselti eğrisindeki her hız vektörüne diktir. Bu, Kesim [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3)'teki teoremdir, şimdi zincir kuralıyla gerekçelendirilmiş olarak.

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=x_1^2x_2+x_2^2$ olsun ve $\boldsymbol{\gamma}(t)=(1+t,\ 2+2t)^{\top}$, $(1,\,2)$ noktasından geçen ve $\boldsymbol{\gamma}'(t)=(1,\,2)^{\top}$ olan bir doğru olsun. $t=0$ için şu bulunur:

$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)\Big|_{t=0}=\begin{pmatrix}4&5\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix}=4+10=14 .$$

Sağlama: $f(\boldsymbol{\gamma}(t))=(1+t)^2(2+2t)+(2+2t)^2=2\,(1+t)^3+4\,(1+t)^2$ fonksiyonunun $t=0$ noktasındaki türevi $6+8=14$ olur.
::::

⁠**Kısacası:** Bir eğri boyunca $f$, $\nabla f^{\top}\boldsymbol{\gamma}'$ hızıyla değişir; bir eş yükselti eğrisi üzerinde bu hız sıfırdır.

:::aufgabe Alıştırma 20 ★ Jacobi matrisleriyle zincir kuralı
<span class="anker" id="aufg-20"></span>

$\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1x_2)^{\top}$ ve $f(\mathbf{u})=u_1^2-u_2$ olsun.

<ol class="al">

<li>

$\mathbf{x}=(1,\,3)^{\top}$ noktasında $\mathbf{u}$ ara değerini, $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ Jacobi matrisini ve $\nabla f(\mathbf{u})$ gradyanını hesaplayın.

</li>

<li>

$\nabla(f\circ\mathbf{g})(\mathbf{x})$ gradyanını [(6.3)](#gl-6-3) ile hesaplayın ve açık yazılmış fonksiyonla sağlamasını yapın. Devrik alınmasaydı ne çıkardı?

</li>

</ol>

:::loesung
(a) $\mathbf{u}=\mathbf{g}(1,3)=(4,\,3)^{\top}$. Jacobi matrisi $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}1&1\\x_2&x_1\end{smallmatrix}\bigr)$, dolayısıyla $(1,\,3)$ noktasında $\bigl(\begin{smallmatrix}1&1\\3&1\end{smallmatrix}\bigr)$ olur. Dış fonksiyonun gradyanı $\nabla f(\mathbf{u})=(2u_1,\,-1)^{\top}=(8,\,-1)^{\top}$ olur.

(b) [(6.3)](#gl-6-3) uyarınca:

$$\nabla(f\circ\mathbf{g})(1,3)=\begin{pmatrix}1&3\\1&1\end{pmatrix}\begin{pmatrix}8\\-1\end{pmatrix}=\begin{pmatrix}8-3\\8-1\end{pmatrix}=\begin{pmatrix}5\\7\end{pmatrix}.$$

Sağlama: $F(\mathbf{x})=(x_1+x_2)^2-x_1x_2=x_1^2+x_1x_2+x_2^2$ fonksiyonunun kısmi türevleri $2x_1+x_2=5$ ve $x_1+2x_2=7$ olur. Devrik alınmasaydı $\mathbf{J}_{\mathbf{g}}\nabla f=(8-1;\ 24-1)^{\top}=(7,\,23)^{\top}$, yani yanlış bir sonuç elde edilirdi.
:::
:::

:::aufgabe Alıştırma 21 ★★ Üç yol
<span class="anker" id="aufg-21"></span>

$g_1(x)=x$, $g_2(x)=x^2$ ve $g_3(x)=x^3$ olmak üzere $F(x)=g_1(x)\,g_2(x)\,g_3(x)$ olsun.

<ol class="al">

<li>

$x$'ten $u_1,u_2,u_3$ üzerinden $F=u_1u_2u_3$ çıktısına giden yol ağını çizin ve her kenara çarpanını yazın.

</li>

<li>

$F'(x)$ türevini üç yol üzerinden toplam olarak hesaplayın ve $x^6$ fonksiyonunun türeviyle karşılaştırın.

</li>

</ol>

:::loesung
(a) $x$'ten $u_1$, $u_2$, $u_3$ düğümlerine, çarpanları $1$, $2x$ ve $3x^2$ olan üç kenar gider. Her $u_i$'den $F=u_1u_2u_3$ düğümüne birer kenar gider; bu kenarın çarpanı diğer ikisinin çarpımıdır: $u_2u_3=x^5$, $u_1u_3=x^4$ ve $u_1u_2=x^3$.

(b) Üç yol üzerinden toplanınca:

$$F'(x)=x^5\cdot1+x^4\cdot2x+x^3\cdot3x^2=x^5+2x^5+3x^5=6x^5 .$$

Bu, $F(x)=x^6$ fonksiyonunun türevidir. $u_k$ üzerinden geçen yol $k\,x^5$ katkı yapar, çünkü $g_k=x^k$ fonksiyonunun türevi $k\,x^{k-1}$ olur ve diğer iki çarpan birlikte $x^{6-k}$ verir. Demek ki üç çarpan için çarpım kuralı, üç yol üzerinden bir toplamdır.
:::
:::

:::aufgabe Alıştırma 22 ★★ Eş yükselti eğrisi üzerindeki eğri
<span class="anker" id="aufg-22"></span>

$f(\mathbf{x})=x_1^2+4x_2^2$ ve $\boldsymbol{\gamma}(t)=\bigl(\sqrt5\cos t,\ \tfrac{\sqrt5}2\sin t\bigr)^{\top}$ olsun.

<ol class="al">

<li>

$\boldsymbol{\gamma}$ eğrisinin tamamen $f=5$ eş yükselti eğrisi üzerinde uzandığını gösterin.

</li>

<li>

$\boldsymbol{\gamma}(t)=(1,\,1)^{\top}$ olan $t$ değerini belirleyin, orada $\boldsymbol{\gamma}'(t)$ vektörünü hesaplayın ve $\nabla f^{\top}\boldsymbol{\gamma}'=0$ olduğunu kontrol edin. Doğrultuyu Kesim [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3)'teki $\mathbf{t}$ vektörüyle karşılaştırın.

</li>

<li>

[(6.4)](#gl-6-4) ile genel olarak gerekçelendirin: Türevlenebilir bir eğri $f$ fonksiyonunun bir düzey kümesi üzerinde uzanıyorsa $\nabla f$, eğrinin hız vektörüne diktir.

</li>

</ol>

:::loesung
(a) Her $t$ için $f(\boldsymbol{\gamma}(t))=5\cos^2t+4\cdot\tfrac54\sin^2t=5\,(\cos^2t+\sin^2t)=5$.

(b) $\sqrt5\cos t=1$ ve $\tfrac{\sqrt5}2\sin t=1$ eşitliklerinden $\cos t=1/\sqrt5$ ve $\sin t=2/\sqrt5$, dolayısıyla $t\approx1{,}107$ çıkar. Bu noktada şunlar bulunur:

$$\boldsymbol{\gamma}'(t)=\bigl(-\sqrt5\sin t,\ \tfrac{\sqrt5}2\cos t\bigr)^{\top}=\bigl(-2,\ \tfrac12\bigr)^{\top},\qquad \nabla f(1,1)^{\top}\boldsymbol{\gamma}'=2\cdot(-2)+8\cdot\tfrac12=0 .$$

Hız vektörü $-\tfrac12\,(4,\,-1)^{\top}$ olur; yani Kesim [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3)'teki $\mathbf{t}$ vektörüne paraleldir.

(c) $\boldsymbol{\gamma}$, $c$ değerine ait düzey kümesi üzerinde uzanıyorsa her $t$ için $f(\boldsymbol{\gamma}(t))=c$ olur ve $t$'ye göre türev sıfırdır. [(6.4)](#gl-6-4) uyarınca bu türev $\nabla f(\boldsymbol{\gamma}(t))^{\top}\boldsymbol{\gamma}'(t)$ olur. Dolayısıyla gradyan, düzey kümesi üzerindeki bir eğrinin her hız vektörüne diktir.
:::
:::

:::aufgabe Alıştırma 23 ★★★ Üç aşamalı bir zincir
<span class="anker" id="aufg-23"></span>

$\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ olmak üzere $F(\mathbf{x})=\sum_{i=1}^2(\mathbf{A}\mathbf{x})_i^2$ olsun. Hesap üç aşamadan oluşur: $\mathbf{u}=\mathbf{A}\mathbf{x}$, sonra her bileşen için $v_i=u_i^2$, sonra $F=v_1+v_2$.

<ol class="al">

<li>

$\mathbf{x}=(2,\,1)^{\top}$ noktasında üç Jacobi matrisini verin ve $\mathbf{J}_F$ matrisini bunların çarpımı olarak hesaplayın.

</li>

<li>

Genel olarak $\nabla F(\mathbf{x})=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$ olduğunu gösterin ve (a)'daki sonucu kontrol edin.

</li>

<li>

(a)'daki çarpımı bir kez soldan, bir kez sağdan hesaplayın. $\mathbf{A}$ bir $n\times n$ tipinde matris ise hangi sıra daha az çarpma gerektirir?

</li>

</ol>

:::loesung
(a) $(2,\,1)$ noktasında $\mathbf{u}=\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$, $\mathbf{v}=(16,\,1)^{\top}$ ve $F=17$ olur. Jacobi matrisleri $\mathbf{J}_1=\mathbf{A}$, $\mathbf{J}_2=\operatorname{diag}(2u_1;\,2u_2)=\operatorname{diag}(8;\,2)$ ve $\mathbf{J}_3=(1\ \ 1)$ olur. Çarpımları:

$$\mathbf{J}_F=(1\ \ 1)\,\operatorname{diag}(8;\,2)\,\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 2)\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 18).$$

(b) Devrik alınınca $\nabla F=\mathbf{A}^{\top}\,\operatorname{diag}(2\mathbf{u})\,\mathbf{1}=\mathbf{A}^{\top}\,2\mathbf{u}=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$ olur. $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&5\end{smallmatrix}\bigr)$ ile $2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=2\,(4,\,9)^{\top}=(8,\,18)^{\top}$ bulunur, (a)'daki gibi. Sağlama: $F=(x_1+2x_2)^2+x_2^2$ fonksiyonunun kısmi türevleri $2\cdot4=8$ ve $4\cdot4+2=18$ olur.

(c) Soldan: $(1\ \ 1)\,\operatorname{diag}(8;2)$ bir satırdır ve bunun için $n$ çarpma gerekir; satır çarpı $\mathbf{A}$ ise $n^2$ çarpma gerektirir. Sağdan: $\operatorname{diag}(8;2)\,\mathbf{A}$ için $n^2$ çarpma, satır çarpı bu sonuç için bir kez daha $n^2$ çarpma gerekir. Demek ki soldan yaklaşık $n^2$, sağdan yaklaşık $2n^2$ çarpma yapılır. Ortadaki matris köşegen değil de tam dolu olsaydı, sağdan yapılan matris çarpımı yaklaşık $n^3$ çarpmaya bile mal olurdu. Soldan, yani sonuçtan başlanınca, her zaman yalnızca satırlar ortaya çıkar.
:::
:::
