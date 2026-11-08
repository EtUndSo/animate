---
title: Kuadratik formlar
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
knoten: Temeller 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15220600
summary: Doğrusal fonksiyonlardan sonra çok değişkenli fonksiyonların en basitleri kuadratik olanlardır.
tags: kuadratik formu
lang: tr
---

<span class="anker" id="stufe-5"></span>

:::zweck
Doğrusal fonksiyonlardan sonra çok değişkenli fonksiyonların en basitleri kuadratik olanlardır. Enerjileri, hata karelerini ve eğri yüzeyleri betimlerler. Bu kesim onları bir matrisle yazıyor, üç temel biçimi, yani çanak, oluk ve eyeri gösteriyor ve karma terimler olmadığı sürece hangi biçimin söz konusu olduğunun matristen nasıl anlaşıldığını açıklıyor.
:::

### Kuadratik formlar

<span class="anker" id="stufe-5-1"></span>

Temeller 1, Kesim 8.4'te tek çıkışlı her doğrusal fonksiyon, bileşenlerin bir $\mathbf{w}^{\top}\mathbf{x}$ ağırlıklı toplamıydı. Basitlikte bundan sonra gelen fonksiyon türü, bileşenlerin ikişerli çarpımlarını toplar: $x_1^2$ gibi kareleri ve $x_1x_2$ gibi karma terimleri. Elektrik mühendisliğinden bir örnek, endüktansları $L_1$, $L_2$ ve karşılıklı endüktansı $M$ olan, içlerinden $i_1$ ve $i_2$ akımları geçen iki kuplajlı bobinin manyetik enerjisidir:

$$W=\tfrac12L_1i_1^2+M\,i_1i_2+\tfrac12L_2i_2^2 .$$

Böyle toplamlar ortada bir matris bulunacak biçimde yazılabilir.

:::definition Tanım 5.1 (Kuadratik form)
<span class="anker" id="satz-5-1"></span>

Bir $\mathbf{A}\in\mathbb{R}^{n\times n}$ kare matrisi için

<span class="anker" id="gl-5-1"></span>
$$f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^na_{il}\,x_ix_l \tag{5.1}$$

fonksiyonuna $\mathbf{A}$ matrisinin __kuadratik formu__ denir.
:::

Sonuç bir sayıdır: $\mathbf{A}\mathbf{x}$ bir vektördür ve $\mathbf{x}^{\top}(\mathbf{A}\mathbf{x})$, $\mathbf{x}$ ile bu vektörün iç çarpımıdır. $n=2$ için açık yazılınca şu elde edilir:

$$\mathbf{x}^{\top}\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}\mathbf{x}=a_{11}x_1^2+(a_{12}+a_{21})\,x_1x_2+a_{22}x_2^2 .$$

$\mathbf{x}$ iki katına çıkarılırsa $f$ dört katına çıkar: $f(c\,\mathbf{x})=c^2f(\mathbf{x})$. Adı buradan gelir.

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ için $f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$ olur. $\mathbf{x}=(1,\,-1)^{\top}$ noktasında $f=5-4+2=3$; sağlama olarak $\mathbf{A}\mathbf{x}=(3,\,0)^{\top}$ ve $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=3$. Şekil [14](#abb-14), [(5.1)](#gl-5-1) çift toplamını bu noktada terim terim hesaplıyor. $(1,\,1)^{\top}$ noktasında $f=11$, orijinde $f=0$. İki bobinin enerjisi $\mathbf i=(i_1,\,i_2)^{\top}$ akım vektörüyle $W=\tfrac12\,\mathbf i^{\top}\bigl(\begin{smallmatrix}L_1&M\\M&L_2\end{smallmatrix}\bigr)\,\mathbf i$ olur; bu matrise endüktans matrisi denir.

:::abbildung ml/k2rqf 14
$\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ matrisinin kuadratik formu $\mathbf{x}=(1,-1)^{\top}$ noktasında çift toplam olarak: $\mathbf{A}$ matrisinin her elemanı için bir tane olmak üzere dört terim.
:::

⁠**Kısacası:** Bir $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ kuadratik formu, bileşenlerin karelerinden ve karma çarpımlarından oluşan, ağırlıkları $\mathbf{A}$ matrisinin elemanları olan bir toplamdır.

### Yalnızca simetrik kısım önemlidir

<span class="anker" id="stufe-5-2"></span>

$n=2$ için yazılan ifadede $a_{12}$ ve $a_{21}$ yalnızca toplam olarak yer alır. Bu yüzden $\bigl(\begin{smallmatrix}5&4\\0&2\end{smallmatrix}\bigr)$ ve $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ matrislerinin kuadratik formu aynıdır. Her zaman simetrik olan seçilebilir.

:::satz Teorem 5.2 (Simetrik kısım)
<span class="anker" id="satz-5-2"></span>

Her $\mathbf{A}$ kare matrisi ve her $\mathbf{x}$ için şu geçerlidir:

<span class="anker" id="gl-5-2"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\Bigl(\frac{\mathbf{A}+\mathbf{A}^{\top}}2\Bigr)\mathbf{x} . \tag{5.2}$$
:::

:::beweis Simetrik kısım
$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ sayısı kendi devriğine eşittir, yani $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})^{\top}=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{x}$. İki ifadenin ortalaması $\mathbf{x}^{\top}\frac{\mathbf{A}+\mathbf{A}^{\top}}2\mathbf{x}$ olur.
:::

$\frac12(\mathbf{A}+\mathbf{A}^{\top})$ matrisi simetriktir. Bu yüzden bu bölümde bir kuadratik formun matrisi her zaman simetriktir. Bu matris şöyle okunur: Köşegende karelerin katsayıları, köşegen dışında ise her seferinde karma terimin katsayısının yarısı durur.

⁠**Sayısal örnek:** $3x_1^2-6x_1x_2+x_2^2$ formunun simetrik matrisi $\bigl(\begin{smallmatrix}3&-3\\-3&1\end{smallmatrix}\bigr)$ olur. $\mathbb{R}^3$ uzayındaki $x_1^2+2x_2^2+4x_3^2+2x_1x_3$ formunun matrisi $\Bigl(\begin{smallmatrix}1&0&1\\0&2&0\\1&0&4\end{smallmatrix}\Bigr)$ olur; $2x_1x_3$ karma terimi $(1,3)$ ve $(3,1)$ elemanlarına paylaştırılır.

⁠**Kısacası:** Bir kuadratik form matrisinin yalnızca simetrik kısmını görür; bu yüzden her zaman simetrik bir matrisle yazılır.

### Çanak, oluk ve eyer

<span class="anker" id="stufe-5-3"></span>

İki değişkende kuadratik form, $f(\mathbf{x})$ yükseklik olarak alınıp düzlemin üzerinde bir yüzey olarak çizilebilir; bir haritadaki gibi eş yükselti eğrileri, yani aynı yükseklikteki noktaları birleştiren eğriler de çizilebilir. En basit durum, matrisin bir köşegen matris olduğu durumdur. O zaman karma terim yoktur ve $f(\mathbf{x})=a_{11}x_1^2+a_{22}x_2^2$ olur. İki elemanın işaretlerine göre üç temel biçim ortaya çıkar (Şekil [15](#abb-15)).

:::abbildung ml/k2formen 15
Üstte $|x_1|,|x_2|\le1$ karesi üzerinde $x_1^2+2x_2^2$ (çanak), $x_1^2$ (oluk) ve $x_1^2-x_2^2$ (eyer) kuadratik formlarının grafikleri, altta eş yükselti eğrileri. Çanakta bunlar elipslerdir ($f=\tfrac14,\tfrac12,1$), olukta paralel doğru çiftleridir; kesikli çizgi, oluğun yüksekliğinin sıfır olduğu $x_1=0$ doğrusudur. Eyerde hiperbollerdir: $f=\tfrac14,\tfrac12$ için koyu, $f=-\tfrac14,-\tfrac12$ için soluk renkte; kesikli çizgiler $f=0$ olan iki doğrudur.
:::

<ul>

<li>

⁠**Çanak:** İki köşegen elemanı da pozitiftir, örneğin $f=x_1^2+2x_2^2$. O zaman her $\mathbf{x}\ne\mathbf{0}$ için $f(\mathbf{x})>0$ olur ve yalnızca orijinde $f=0$. Eş yükselti eğrileri, orijin çevresinde, yarı eksenleri koordinat eksenleri üzerinde olan elipslerdir.

</li>

<li>

⁠**Oluk:** Bir eleman pozitif, öbürü sıfırdır, örneğin $f=x_1^2$. O zaman $f\ge0$ olur, ama $x_1=0$ doğrusunun tamamında $f=0$: Yüzeyin orada düz bir vadi tabanı vardır. Eş yükselti eğrileri paralel doğru çiftleridir.

</li>

<li>

⁠**Eyer:** Elemanların işaretleri farklıdır, örneğin $f=x_1^2-x_2^2$. $x_1$ ekseni boyunca yüzey iki yana doğru yükselir, $x_2$ ekseni boyunca iki yana doğru alçalır. Eş yükselti eğrileri hiperbollerdir.

</li>

</ul>

İki eleman da negatifse çanak baş aşağı durur; bu bir kubbedir. Negatif bir eleman ve sıfır olan bir eleman ters dönmüş bir oluk, yani bir sırt verir. İkiden fazla değişkende de aynısı geçerlidir: Biçime köşegen elemanlarının işaretleri karar verir.

⁠**Sayısal örnek:** $f=x_1^2+2x_2^2$ çanağında $f=1$ eş yükselti eğrisi, yarı eksenleri $x_1$ ekseninde $1$ ve $x_2$ ekseninde $1/\sqrt2\approx0{,}707$ olan elipstir: $(1,\,0)^{\top}$ ve $(0,\,1/\sqrt2)^{\top}$ noktalarında $f=1$. $f=x_1^2-x_2^2$ eyerinde $f(1,\,0)=1$, $f(0,\,1)=-1$ ve $f(1,\,1)=0$.

⁠**Kısacası:** Karma terim yoksa biçim köşegenin işaretlerinden okunur: hepsi pozitifse bir çanak, pozitif ve sıfırsa bir oluk, karışık işaretliyse bir eyer.

### Tam kareye tamamlama

<span class="anker" id="stufe-5-4"></span>

Karma terimler varsa biçim hemen görülemez. $5x_1^2+4x_1x_2+2x_2^2$ bir çanak mıdır? Karma terim negatif olabilir. Okuldan, karma terimleri ortadan kaldıran bir araç bilinir: tam kareye tamamlama. Bu araç formu karelerin toplamı olarak yazar; biçim de karelerin önündeki katsayılardan, önceki alt kesimdeki gibi okunur.

:::herleitung İki değişkende tam kareye tamamlama
$a\ne0$ olsun. $x_1$ içeren terimlerden $a$ paranteze alınır ve bir kareye tamamlanır:

$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1^2+\frac{2b}ax_1x_2\Bigr)+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2-\frac{b^2}ax_2^2+cx_2^2 .$$

Dolayısıyla şu bulunur:

<span class="anker" id="gl-5-3"></span>
$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2+\Bigl(c-\frac{b^2}a\Bigr)x_2^2 . \tag{5.3}$$
:::

Sağ tarafta iki karenin toplamı vardır. $\mathbf{x}$ düzlemi dolaşırken $z_1=x_1+\frac bax_2$ ve $z_2=x_2$ yeni değişkenleri her sayı çiftini alır. Demek ki $z_1,z_2$ değişkenlerinde yazılan formda karma terim kalmaz ve çanak, oluk ya da eyer olduğuna $a$ ile $c-b^2/a$ katsayılarının işaretleri karar verir.

⁠**Sayısal örnek 1:** $5x_1^2+4x_1x_2+2x_2^2$ için $a=5$, $b=2$, $c=2$:

$$5x_1^2+4x_1x_2+2x_2^2=5\,(x_1+0{,}4\,x_2)^2+1{,}2\,x_2^2 .$$

İki katsayı da pozitiftir: Form bir çanaktır. $\mathbf{x}=(1,\,-1)^{\top}$ noktasında sağlama: $5\cdot0{,}36+1{,}2=3$.

⁠**Sayısal örnek 2:** $x_1^2+6x_1x_2+x_2^2=(x_1+3x_2)^2-8x_2^2$. Katsayıların işaretleri farklıdır: bir eyer. Gerçekten de $f(1,\,0)=1>0$ ve $f(1,\,-1)=1-6+1=-4<0$.

⁠**Kısacası:** Tam kareye tamamlama bir kuadratik formu karelerin toplamı olarak yazar; karelerin önündeki katsayıların işaretleri, formun bir çanak mı, bir oluk mu, yoksa bir eyer mi olduğunu gösterir.

:::hintergrund Tam kareye tamamlama Gauss eleme yöntemidir
[(5.3)](#gl-5-3) içindeki sayılar, Temeller 1, Kesim 12.3'teki Gauss eleme yöntemi $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$ simetrik matrisine uygulandığında çıkan sayılarla aynıdır. Köşegenin altında bir sıfır elde etmek için birinci satırın $\frac ba$ katı ikinci satırdan çıkarılır ve $\bigl(\begin{smallmatrix}a&b\\0&c-b^2/a\end{smallmatrix}\bigr)$ elde edilir. Bu basamak biçiminin köşegen elemanları, yani pivotlar, tam olarak karelerin önündeki katsayılardır; $\frac ba$ eleme çarpanı da birinci parantezde durur. $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ matrisi için: çarpan $0{,}4$, pivotlar $5$ ve $1{,}2$. $n$ değişkende aynı işlem sürdürülür: Her eleme adımı bir değişkeni bir kareye tamamlar. Form ancak ve ancak bütün pivotlar pozitifse bir çanaktır. Temeller 1, Kesim 14.5'teki hesap kurallarına göre pivotların çarpımı determinanttır, burada $5\cdot1{,}2=6=5\cdot2-2\cdot2$.
:::

:::aufgabe Alıştırma 14 ★ Formlar ve matrisler
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

$2x_1^2-2x_1x_2+3x_2^2$ ve $x_1x_2$ formlarının simetrik matrisini yazın.

</li>

<li>

$\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)$ matrisinin formunu ve simetrik matrisini hesaplayın.

</li>

<li>

$3x_1^2+x_2^2$, $-x_1^2$ ve $2x_1^2-x_2^2+x_3^2$ formlarının her birinin bir çanak mı, bir oluk mu, bir eyer mi, yoksa başka bir şey mi olduğunu hesap yapmadan belirleyin.

</li>

</ol>

:::loesung
(a) Köşegene karelerin katsayıları, köşegen dışına karma terimin katsayısının yarısı yazılır: $2x_1^2-2x_1x_2+3x_2^2$ formunun matrisi $\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$, $x_1x_2$ formununki ise $\bigl(\begin{smallmatrix}0&1/2\\1/2&0\end{smallmatrix}\bigr)$ olur.

(b) $\mathbf{x}^{\top}\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)\mathbf{x}=x_1^2+(3-1)\,x_1x_2+2x_2^2=x_1^2+2x_1x_2+2x_2^2$ olur. Simetrik matris $\tfrac12(\mathbf{A}+\mathbf{A}^{\top})=\bigl(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\bigr)$ olur.

(c) $3x_1^2+x_2^2$: iki katsayı da pozitif, bir çanak. $-x_1^2$: bir negatif ve bir sıfır katsayı, dolayısıyla ters dönmüş bir oluk, yani $x_2$ ekseni boyunca uzanan bir sırt. $2x_1^2-x_2^2+x_3^2$: karışık işaretler, bir eyer; form $x_1$ ve $x_3$ doğrultularında yükselir, $x_2$ doğrultusunda alçalır.
:::
:::

:::aufgabe Alıştırma 15 ★★ Tam kareye tamamlama
<span class="anker" id="aufg-15"></span>

Tam kareye tamamlayın ve biçim hakkında karar verin:

$$f_1=2x_1^2+8x_1x_2+11x_2^2,\qquad f_2=x_1^2+4x_1x_2+4x_2^2,\qquad f_3=x_1^2+4x_1x_2+x_2^2 .$$

Oluk için $f=0$ olan doğruyu, eyer için de $f<0$ olan bir noktayı verin.

:::loesung
[(5.3)](#gl-5-3) ile:

<ul>

<li>

$f_1$: $a=2$, $b=4$, $c=11$, dolayısıyla $f_1=2(x_1+2x_2)^2+(11-8)\,x_2^2=2(x_1+2x_2)^2+3x_2^2$. İki katsayı da pozitif: bir çanak.

</li>

<li>

$f_2=(x_1+2x_2)^2+0\cdot x_2^2$: bir oluk. $x_1+2x_2=0$ doğrusu üzerinde, yani $(2,\,-1)^{\top}$ doğrultusunda sıfırdır.

</li>

<li>

$f_3=(x_1+2x_2)^2-3x_2^2$: farklı işaretler, bir eyer. $x_2=1$ ve $x_1=-2$ seçilirse birinci kare sıfır olur: $f_3(-2,\,1)=4-8+1=-3<0$.

</li>

</ul>
:::
:::

:::aufgabe Alıştırma 16 ★★ Kuplajlı bobinler
<span class="anker" id="aufg-16"></span>

İki kuplajlı bobin için $L_1=4\,\mathrm{mH}$ ve $L_2=1\,\mathrm{mH}$ veriliyor.

<ol class="al">

<li>

$W=\tfrac12L_1i_1^2+M\,i_1i_2+\tfrac12L_2i_2^2$ enerjisini tam kareye tamamlayın.

</li>

<li>

$M$ hangi değerleri aldığında bütün $(i_1,\,i_2)\ne(0,\,0)$ akımları için $W>0$ olur? Bundan $k=M/\sqrt{L_1L_2}$ kuplaj katsayısı için ne çıkar?

</li>

</ol>

:::loesung
(a) [(5.3)](#gl-5-3) bağıntısında $a=\tfrac12L_1$, $2b=M$ ve $c=\tfrac12L_2$ olur, dolayısıyla $b/a=M/L_1$ ve $b^2/a=M^2/(2L_1)$:

$$W=\tfrac12L_1\Bigl(i_1+\frac M{L_1}\,i_2\Bigr)^2+\tfrac12\Bigl(L_2-\frac{M^2}{L_1}\Bigr)i_2^2=2\,\mathrm{mH}\,\Bigl(i_1+\frac M{4\,\mathrm{mH}}\,i_2\Bigr)^2+\Bigl(\frac12\,\mathrm{mH}-\frac{M^2}{8\,\mathrm{mH}}\Bigr)i_2^2 .$$

(b) Birinci katsayı pozitiftir. $\ne(0,\,0)$ olan bütün akımlar için $W>0$ koşulu ancak ve ancak ikinci katsayı da pozitifse sağlanır: $L_2-M^2/L_1>0$, yani $M^2<L_1L_2=4\,(\mathrm{mH})^2$ ve $|M|<2\,\mathrm{mH}$. Kuplaj katsayısı için bu, $|k|=|M|/\sqrt{L_1L_2}<1$ demektir. İdeal sıkı kuplaj olan $|k|=1$ durumunda form yalnızca bir oluk olurdu: Uygun $i_1=-\tfrac M{L_1}\,i_2$ akım oranında depolanan enerji sıfır olurdu. Demek ki bir manyetik alanın enerjisinin hiçbir zaman negatif olmaması $|k|\le1$ koşulunu zorunlu kılar.
:::
:::
