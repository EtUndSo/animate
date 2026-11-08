---
title: Koşul sayısı
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
knoten: Temeller 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15221300
summary: Ölçüm verileri hiçbir zaman kesin değildir ve bir bilgisayar her adımda yuvarlar.
tags: koşul sayısı
lang: tr
---

<span class="anker" id="stufe-12"></span>

:::zweck
Ölçüm verileri hiçbir zaman kesin değildir ve bir bilgisayar her adımda yuvarlar. Sağ taraf biraz yanlışsa bir denklem sisteminin çözümü ne kadar değişir? Bu kesim, tekil değerlerden elde edilen tek bir sayının cevabı verdiğini ve bunun normal denklemler için ne anlama geldiğini gösteriyor.
:::

### Hassas bir denklem sistemi

<span class="anker" id="stufe-12-1"></span>

Aşağıdaki denklem sisteminin

$$x_1+x_2=2,\qquad x_1+1{,}01\,x_2=2{,}01$$

çözümü $\mathbf{x}=(1,\,1)^{\top}$ olur. İkinci denklemin sağ tarafı $0{,}01$ kadar değiştirilip $2{,}02$ yapılırsa denklemlerin farkı $0{,}01\,x_2=0{,}02$ verir, dolayısıyla $x_2=2$ ve $x_1=0$ olur. Verilerin üçüncü basamağındaki bir değişiklik çözümü kendi büyüklüğü kadar kaydırır.

Geometrik olarak iki denklem, çözüm noktasında kesişen iki doğrudur. Burada neredeyse paraleldirler; yalnızca yaklaşık $0{,}29^\circ$'lik bir açıyla kesişirler. Biri biraz kaydırılırsa kesişim noktası öbürü boyunca uzun bir yol alır (Şekil [28](#abb-28)). Doğrular birbirine dikse kesişim noktası yalnızca doğrunun kaydırıldığı kadar kayar.

:::abbildung ml/k2kondition 28
Kırmızı doğru iki kez aynı biçimde, $0{,}2$ uzaklık kadar kaydırılıyor (kesikli). Solda kırmızı doğru mavi doğruyu dik keser ve kesişim noktası $0{,}2$ kayar. Sağda doğrular $8^\circ$'lik bir açıyla kesişir ve kesişim noktası $0{,}2/\sin8^\circ\approx1{,}44$ kayar. Kesişim açısı ne kadar küçükse çözüm verilerdeki değişikliklere o kadar hassas tepki verir.
:::

Etki, büyüklüklerin kendisiyle kıyaslandığında ne kadardır? $\mathbf{y}=(2;\ 2{,}01)^{\top}$ sağ tarafının uzunluğu $\sqrt{4+4{,}0401}\approx2{,}8355$ (Şekil [29](#abb-29)), $\Delta\mathbf{y}=(0;\ 0{,}01)^{\top}$ değişikliğinin uzunluğu $0{,}01$ olur. Demek ki sağ taraf göreli olarak $0{,}01/2{,}8355\approx0{,}35\,\%$ değişir. Çözüm $\Delta\mathbf{x}=(-1,\,1)^{\top}$ kadar, göreli olarak $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt2/\sqrt2=100\,\%$ değişir. Göreli hata yaklaşık $284$ kat büyütülür.

:::abbildung ml/k2rnormy 29
Sağ tarafın uzunluğunun karesi $\mathbf{y}^{\top}\mathbf{y}$ iç çarpımı olarak; uzunluk $\sqrt{8{,}0401}\approx2{,}8355$ olur.
:::

⁠**Kısacası:** Bir denklem sisteminin doğruları neredeyse paralel kesişiyorsa verilerdeki küçük değişiklikler çözümü çok kaydırır.

### Koşul sayısı

<span class="anker" id="stufe-12-2"></span>

Bu çarpan nereden geliyor? Tekil değer ayrışımıyla büyütme için kesin bir sınır verilebilir.

:::definition Tanım 12.1 (Koşul sayısı)
<span class="anker" id="satz-12-1"></span>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisinin sütunları doğrusal bağımsız, yani $d_n>0$ olsun. $\mathbf{A}$ matrisinin __koşul sayısı__

<span class="anker" id="gl-12-1"></span>
$$\kappa(\mathbf{A})=\frac{d_1}{d_n}, \tag{12.1}$$

yani en büyük uzatmanın en küçük uzatmaya oranıdır.
:::

Her zaman $\kappa(\mathbf{A})\ge1$ olur. Ortogonal bir matriste $\kappa=1$ olur, çünkü bütün tekil değerleri $1$ olur. Koşul sayısı büyük olan bir matrise kötü koşullu denir.

:::satz Teorem 12.2 (Hatanın büyütülmesi)
<span class="anker" id="satz-12-2"></span>

$\mathbf{A}\in\mathbb{R}^{n\times n}$ tersinir, $\mathbf{y}\ne\mathbf{0}$ olmak üzere $\mathbf{A}\mathbf{x}=\mathbf{y}$ ve $\mathbf{A}(\mathbf{x}+\Delta\mathbf{x})=\mathbf{y}+\Delta\mathbf{y}$ olsun. O zaman şu geçerlidir:

<span class="anker" id="gl-12-2"></span>
$$\frac{\lVert\Delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert}\le\kappa(\mathbf{A})\,\frac{\lVert\Delta\mathbf{y}\rVert}{\lVert\mathbf{y}\rVert} . \tag{12.2}$$

Eşitlik, $\mathbf{y}$ vektörü $\mathbf{u}_1$ doğrultusunu, $\Delta\mathbf{y}$ de $\mathbf{u}_n$ doğrultusunu gösterdiğinde sağlanır.
:::

:::beweis Hatanın büyütülmesi
İki denklemden $\mathbf{A}\Delta\mathbf{x}=\Delta\mathbf{y}$ çıkar. [(9.5)](die-singularwertzerlegung.html#gl-9-5) uyarınca $\lVert\mathbf{y}\rVert=\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\lVert\mathbf{x}\rVert$, dolayısıyla $1/\lVert\mathbf{x}\rVert\le d_1/\lVert\mathbf{y}\rVert$ olur; ayrıca $\lVert\Delta\mathbf{y}\rVert=\lVert\mathbf{A}\Delta\mathbf{x}\rVert\ge d_n\lVert\Delta\mathbf{x}\rVert$, dolayısıyla $\lVert\Delta\mathbf{x}\rVert\le\lVert\Delta\mathbf{y}\rVert/d_n$ olur. Bunlar çarpılınca [(12.2)](#gl-12-2) çıkar. $\mathbf{y}$, $\mathbf{u}_1$ doğrultusunu gösteriyorsa $\mathbf{x}$, $\mathbf{v}_1$ vektörünün bir katıdır ve birinci eşitsizlik bir eşitliktir; $\Delta\mathbf{y}$, $\mathbf{u}_n$ doğrultusunu gösteriyorsa $\Delta\mathbf{x}$, $\mathbf{v}_n$ vektörünün bir katıdır ve ikinci eşitsizlik bir eşitliktir.
:::

Demek ki en kötü durum şudur: Çözüm $\mathbf{A}$ matrisinin en çok uzattığı doğrultudadır, böylece $\mathbf{y}$, $\mathbf{x}$ vektörüne göre büyüktür; hata ise $\mathbf{A}$ matrisinin en az uzattığı doğrultudadır, böylece geri hesaplama onu $1/d_n$ katına büyütür.

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1{,}01\end{smallmatrix}\bigr)$ simetriktir; izi $2{,}01$, determinantı $0{,}01$ olur. Özdeğerleri şunlardır:

$$\lambda_{1,2}=\frac{2{,}01\pm\sqrt{2{,}01^2-0{,}04}}2=\frac{2{,}01\pm\sqrt{4{,}0001}}2\approx\frac{2{,}01\pm2{,}000025}2,$$

yani $\lambda_1\approx2{,}005012$ ve $\lambda_2\approx0{,}004988$; ikisi de pozitiftir. Kesim [9.7](die-singularwertzerlegung.html#stufe-9-7)'ye göre bunlar aynı zamanda tekil değerlerdir ve $\kappa(\mathbf{A})\approx402$ olur. Gözlenen $284$ büyütme bunun altındadır. Sınıra tam ulaşmaz, çünkü $\Delta\mathbf{y}=(0;\ 0{,}01)^{\top}$ tam olarak $\mathbf{u}_2\approx(1,\,-1)^{\top}/\sqrt2$ doğrultusunu göstermez. $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ için $\kappa=4/1=4$ olur: Göreli hatalar en fazla dört katına çıkar.

⁠**Kısacası:** $\kappa(\mathbf{A})=d_1/d_n$ koşul sayısı, $\mathbf{A}^{-1}$ matrisinin verilerdeki göreli bir hatayı çözümde büyütebileceği en büyük çarpandır.

### Koşul sayısı ve determinant

<span class="anker" id="stufe-12-3"></span>

Temeller 1, Kesim 14.6'daki arka plan kutusunda bir uyarı vardı: Küçük bir determinant, bir matrisin neredeyse tekil olduğu anlamına gelmez. Koşul sayısı orada kastedileni ölçer.

:::satz Teorem 12.3 (En yakın tekil matrise uzaklık)
<span class="anker" id="satz-12-3"></span>

Tersinir bir $\mathbf{A}\in\mathbb{R}^{n\times n}$ matrisi için tekil bir $\mathbf{B}$ matrisine olan en küçük $\lVert\mathbf{A}-\mathbf{B}\rVert_2$ uzaklığı $d_n$ olur. $\lVert\mathbf{A}\rVert_2=d_1$ büyüklüğüne göre bu uzaklık şudur:

<span class="anker" id="gl-12-3"></span>
$$\min_{\mathbf{B}\ \text{tekil}}\frac{\lVert\mathbf{A}-\mathbf{B}\rVert_2}{\lVert\mathbf{A}\rVert_2}=\frac1{\kappa(\mathbf{A})} . \tag{12.3}$$
:::

:::beweis Uzaklık
Tekil bir matrisin rankı en fazla $n-1$ olur. $k=n-1$ ile Eckart-Young teoremine göre $\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_n$ olur ve tekil $\mathbf{A}_{n-1}$ matrisinin uzaklığı tam olarak $d_n$ olur.
:::

Demek ki büyük bir koşul sayısı şu anlama gelir: Görece küçük bir değişiklik matrisi tekil yapar. Determinant başka bir şey ölçer. Alıştırma [29](die-singularwertzerlegung.html#aufg-29)'a göre $|\det\mathbf{A}|=d_1\cdots d_n$, yani bütün uzatmaların çarpımıdır; matrisin büyüklüğüne bağlıdır. Koşul sayısı bir orandır ve $\mathbf{A}$ bir sayıyla çarpıldığında değişmez: $c\ne0$ için $\kappa(c\mathbf{A})=\kappa(\mathbf{A})$. Yalnızca $\mathbf{A}$ matrisinin birim çemberi dönüştürdüğü elipsin ne kadar basık olduğunu ölçer.

⁠**Sayısal örnek:** Temeller 1, Kesim 14.6'daki iki matris: $0{,}1\cdot\mathbf{I}_{10}$ matrisinin determinantı $10^{-10}$, ama bütün tekil değerleri $0{,}1$ ve $\kappa=1$ olur; olabildiğince iyi koşulludur. $\operatorname{diag}(1000;\ 0{,}001)$ matrisinin determinantı $1$, ama $\kappa=1000/0{,}001=10^6$ olur. $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1{,}01\end{smallmatrix}\bigr)$ için en yakın tekil matrise uzaklık $d_2\approx0{,}005$ olur: Elemanları birkaç binde bir kadar değiştirmek matrisi tekil yapar. Tekil $\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ matrisinin uzaklığı $\lVert\bigl(\begin{smallmatrix}0&0\\0&0{,}01\end{smallmatrix}\bigr)\rVert_2=0{,}01$, yani en küçük değerden biraz fazladır.

⁠**Kısacası:** $1/\kappa(\mathbf{A})$, en yakın tekil matrise olan göreli uzaklıktır; determinant bu konuda hiçbir şey söylemez, çünkü matrisin büyüklüğüne bağlıdır.

### Normal denklemler koşul sayısının karesini alır

<span class="anker" id="stufe-12-4"></span>

En iyi yaklaşık çözüm $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ normal denklemleri üzerinden ya da QR ayrışımı, yani $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ üzerinden hesaplanabilir. Matematiksel olarak ikisi de aynı sonucu verir. Yuvarlanmış sayılarla vermez ve nedeni koşul sayısıdır.

:::satz Teorem 12.4 (Gram matrisinin koşul sayısı)
<span class="anker" id="satz-12-4"></span>

$\mathbf{A}$ matrisinin sütunları doğrusal bağımsızsa şu geçerlidir:

<span class="anker" id="gl-12-4"></span>
$$\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2 . \tag{12.4}$$

Buna karşılık $\mathbf{A}=\mathbf{Q}\mathbf{R}$ QR ayrışımı için $\kappa(\mathbf{R})=\kappa(\mathbf{A})$ olur.
:::

:::beweis Gram matrisi
$\mathbf{A}^{\top}\mathbf{A}$ simetrik ve pozitif tanımlıdır, özdeğerleri $d_j^2$ olur; Kesim [9.7](die-singularwertzerlegung.html#stufe-9-7)'ye göre bunlar aynı zamanda tekil değerleridir ve oranları $d_1^2/d_n^2$ olur. $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ olduğundan $\mathbf{R}^{\top}\mathbf{R}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{A}^{\top}\mathbf{A}$ olur; dolayısıyla $\mathbf{R}$ matrisinin tekil değerleri $\mathbf{A}$ matrisininkilerle aynıdır.
:::

⁠**Sayısal örnek:** Kesim [3.7](die-beste-naherungslosung.html#stufe-3-7)'deki, alan ve oda sayısından oluşan daire matrisinin tekil değerleri $d_1\approx135{,}02$ ve $d_2\approx0{,}848$, dolayısıyla $\kappa(\mathbf{A})\approx159{,}3$ ve $\kappa(\mathbf{A}^{\top}\mathbf{A})\approx25\,367$ olur. $\kappa(\mathbf{A})$ değerini iki neden büyütür. Birincisi birimlerdir: Alanlar $65$ dolayında, oda sayıları $2{,}5$ dolayında sayılardır. Alan $10\,\mathrm m^2$ birimiyle ölçülürse koşul sayısı yaklaşık $18{,}5$ değerine iner. İkincisi, iki sütun neredeyse aynı doğrultuyu gösterir; aralarında yalnızca yaklaşık $8{,}9^\circ$'lik bir açı vardır. Bu yüzden iki sütun da $1$ uzunluğuna getirilse bile $\kappa\approx12{,}8$ kalır. Birimlerin dönüştürülmesi uydurulan $\hat{\mathbf{y}}$ değerlerini değiştirmez: Bir sütun $10$ ile bölünürse ona ait ağırlık $10$ katına çıkar ve çarpımlar aynı kalır.

⁠**Kısacası:** Normal denklemler $\kappa(\mathbf{A})^2$ ile, QR ayrışımı $\kappa(\mathbf{A})$ ile çalışır; iyi seçilmiş birimler koşul sayısını düşürür.

:::hintergrund Bilgisayar koşul sayısıyla ne yapar
Bir bilgisayar sayıları genellikle yaklaşık $16$ anlamlı ondalık basamakla saklar ve her işlemden sonra yuvarlar. İyi bir yöntem, verileri yalnızca bu yuvarlama mertebesinde değiştirilmiş bir problemin tam çözümünü verir; böyle yöntemlere geriye doğru kararlı denir. [(12.2)](#gl-12-2) uyarınca sonucun göreli hatası o zaman en fazla yaklaşık $\kappa\cdot10^{-16}$ olur: $16$ basamaktan yaklaşık $\log_{10}\kappa$ tanesi kaybolur.

QR ayrışımı (ve tekil değer ayrışımı) üzerinden giden yol geriye doğru kararlıdır; artık vektörü küçükse hatası yaklaşık $\kappa(\mathbf{A})$ gibi büyür. Normal denklemler üzerinden giden yol öyle değildir: $\mathbf{A}^{\top}\mathbf{A}$ matrisiyle çalışır ve hatası, artık vektörü küçük olsa bile her zaman $\kappa(\mathbf{A})^2$ gibi büyür. $\kappa(\mathbf{A})=10^6$ olduğunda bu yolda $16$ basamaktan yaklaşık $12$ tanesi kaybolur, QR ile yaklaşık $6$ tanesi. $\kappa(\mathbf{A})^2\approx2{,}5\cdot10^4$ olan dairelerde bu henüz zararsızdır; neredeyse bağımlı öznitelikler içeren büyük veri kümelerinde değildir. Bu yüzden iyi programlar en iyi yaklaşık çözümü normal denklemler üzerinden değil, QR ya da tekil değer ayrışımı üzerinden hesaplar; oysa kuramı en kısa yoldan betimleyen normal denklemlerdir.
:::

:::aufgabe Alıştırma 36 ★ Koşul sayılarını okumak
<span class="anker" id="aufg-36"></span>

Şunların koşul sayısını bulun:

<ol class="al">

<li>

$\operatorname{diag}(2;\ 0{,}5)$ ve $\operatorname{diag}(-3;\ 3)$;

</li>

<li>

$30^\circ$ kadar dönmenin matrisi;

</li>

<li>

$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ için $5\mathbf{A}$. $\mathbf{A}$ ile $5\mathbf{A}$ matrislerinin determinantlarını karşılaştırın.

</li>

</ol>

:::loesung
(a) $\operatorname{diag}(2;\,0{,}5)$ matrisinin tekil değerleri $2$ ve $0{,}5$ olur, dolayısıyla $\kappa=4$. Kesim [9.7](die-singularwertzerlegung.html#stufe-9-7)'ye göre $\operatorname{diag}(-3;\,3)$ matrisinin tekil değerleri $3$ ve $3$ olur, dolayısıyla özdeğerlerin işaretleri farklı olsa da $\kappa=1$.

(b) Bir dönme matrisi ortogonaldir, bütün tekil değerleri $1$ olur: $\kappa=1$.

(c) $5\mathbf{A}$ matrisinin tekil değerleri $20$ ve $5$ olur, dolayısıyla yine $\kappa=4$. Determinant ise $4$ değerinden $\det(5\mathbf{A})=25\cdot4=100$ değerine çıkar.
:::
:::

:::aufgabe Alıştırma 37 ★★ Determinant 1, yine de kötü koşullu
<span class="anker" id="aufg-37"></span>

$\mathbf{A}=\bigl(\begin{smallmatrix}10&7\\7&5\end{smallmatrix}\bigr)$ olsun.

<ol class="al">

<li>

$\det\mathbf{A}$ değerini ve $\mathbf{A}^{-1}$ matrisini hesaplayın. $\mathbf{A}\mathbf{x}=(17,\,12)^{\top}$ ve $\mathbf{A}\mathbf{x}=(17;\ 12{,}1)^{\top}$ sistemlerini çözün.

</li>

<li>

$\mathbf{y}$ ve $\mathbf{x}$ vektörlerinin göreli değişimlerini ve bunların oranını hesaplayın.

</li>

<li>

$\kappa(\mathbf{A})$ değerini hesaplayın ve [(12.2)](#gl-12-2) eşitsizliğini doğrulayın. $\mathbf{A}$ en yakın tekil matristen ne kadar uzaktır?

</li>

</ol>

:::loesung
(a) $\det\mathbf{A}=50-49=1$ ve $\mathbf{A}^{-1}=\bigl(\begin{smallmatrix}5&-7\\-7&10\end{smallmatrix}\bigr)$ olur. Böylece $\mathbf{A}^{-1}(17,\,12)^{\top}=(85-84,\ -119+120)^{\top}=(1,\,1)^{\top}$ ve $\mathbf{A}^{-1}(17;\ 12{,}1)^{\top}=(85-84{,}7;\ -119+121)^{\top}=(0{,}3;\ 2)^{\top}$ bulunur.

(b) $\lVert\Delta\mathbf{y}\rVert/\lVert\mathbf{y}\rVert=0{,}1/\sqrt{433}\approx0{,}1/20{,}809\approx0{,}48\,\%$. $\Delta\mathbf{x}=(-0{,}7;\ 1)^{\top}$ olur, dolayısıyla $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt{1{,}49}/\sqrt2\approx1{,}2207/1{,}4142\approx86{,}3\,\%$. Oran yaklaşık $180$ olur.

(c) $\mathbf{A}$ simetriktir; izi $15$, determinantı $1$, dolayısıyla $\lambda=\tfrac{15\pm\sqrt{221}}2\approx14{,}933$ ve $0{,}0670$, ikisi de pozitif. Kesim [9.7](die-singularwertzerlegung.html#stufe-9-7)'ye göre bunlar tekil değerlerdir ve $\kappa(\mathbf{A})\approx14{,}933/0{,}0670\approx223$ olur. [(12.2)](#gl-12-2) sınırı sağlanır: $86{,}3\,\%\le223\cdot0{,}48\,\%\approx107\,\%$. En yakın tekil matrise uzaklık $d_2\approx0{,}067$, göreli olarak $1/223$ olur. Determinantın $1$ olması bu konuda hiçbir şey söylemez.
:::
:::

:::aufgabe Alıştırma 38 ★★★ Koşul sayısı için hesap kuralları
<span class="anker" id="aufg-38"></span>

$\mathbf{A}\in\mathbb{R}^{n\times n}$ tersinir ve $\mathbf{Q}$ ortogonal olsun. Gösterin:

<ol class="al">

<li>

$\kappa(\mathbf{Q}\mathbf{A})=\kappa(\mathbf{A})$ ve $\kappa(\mathbf{A}^{-1})=\kappa(\mathbf{A})$;

</li>

<li>

$\mathbf{A}$ matrisinin bütün $\lambda$ ve $\mu$ özdeğerleri için $|\lambda|/|\mu|\le\kappa(\mathbf{A})$;

</li>

<li>

simetrik $\mathbf{A}$ için $\kappa(\mathbf{A})=|\lambda|_{\max}/|\lambda|_{\min}$, yani mutlak değerce en büyük özdeğerin mutlak değerce en küçük özdeğere oranı.

</li>

</ol>

:::loesung
(a) Alıştırma [29](die-singularwertzerlegung.html#aufg-29)'a göre $\mathbf{Q}\mathbf{A}$ matrisinin tekil değerleri $\mathbf{A}$ matrisininkilerle aynıdır, dolayısıyla koşul sayısı da aynıdır. $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ eşitliğinden $\mathbf{A}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$ çıkar; bu, tekil değerleri $1/d_j$ olan bir tekil değer ayrışımıdır. En büyüğü $1/d_n$, en küçüğü $1/d_1$ olur, dolayısıyla $\kappa(\mathbf{A}^{-1})=\tfrac{1/d_n}{1/d_1}=\tfrac{d_1}{d_n}=\kappa(\mathbf{A})$.

(b) $\lambda$ özdeğerine ait bir $\mathbf{v}$ özvektörü için [(9.5)](die-singularwertzerlegung.html#gl-9-5) uyarınca $d_n\lVert\mathbf{v}\rVert\le\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert\le d_1\lVert\mathbf{v}\rVert$ olur, dolayısıyla $d_n\le|\lambda|\le d_1$; Kesim [9.8](die-singularwertzerlegung.html#stufe-9-8)'de gösterildiği gibi bu, karmaşık özvektörler için de geçerlidir. Aynı sınırlar $\mu$ için de geçerlidir. Dolayısıyla $|\lambda|/|\mu|\le d_1/d_n$ olur.

(c) Simetrik $\mathbf{A}$ için Kesim [9.7](die-singularwertzerlegung.html#stufe-9-7)'ye göre tekil değerler $|\lambda_i|$ mutlak değerleridir. Dolayısıyla en büyük tekil değer $|\lambda|_{\max}$, en küçüğü $|\lambda|_{\min}$ olur.
:::
:::
