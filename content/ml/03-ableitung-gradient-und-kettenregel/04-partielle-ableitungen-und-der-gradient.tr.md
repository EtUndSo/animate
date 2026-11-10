---
title: Kısmi türevler ve gradyan
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15230400
summary: Bir sayı birçok girdiye bağlıysa her girdi tek başına biraz değiştirilip diğerleri sabit tutulabilir.
tags: d değişkenli fonksiyon, düzey kümesi, eş yükselti eğrisi, kesit eğrisi, kısmi türevi, gradyanı, teğet düzlem, türevlenebilir
lang: tr
---

<span class="anker" id="stufe-3"></span>

:::zweck
Bir sayı birçok girdiye bağlıysa her girdi tek başına biraz değiştirilip diğerleri sabit tutulabilir. Bu sırada bulunan eğimlere kısmi türevler denir. Birlikte bir vektör, gradyanı oluştururlar ve gradyanla Kesim [1](die-ableitung.html#stufe-1)'deki doğrusal yaklaşım, bir düzlemle yapılan bir yaklaşıma dönüşür. Sonda kesim, bu yaklaşımın gerçekten ne zaman geçerli olduğunu açıklığa kavuşturuyor.
:::

### Çok değişkenli fonksiyonlar

<span class="anker" id="stufe-3-1"></span>

[Bölüm 1, Kesim 2.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-2)'de bir daire için tahmin, özniteliklerin $\hat y=\mathbf{w}^{\top}\mathbf{x}$ ağırlıklı toplamıydı. Öznitelikler sabit tutulup tahminin ağırlıklara nasıl bağlı olduğu sorulursa $\hat y$, $d$ tane $w_1,\dots,w_d$ sayısına bağlı bir sayıdır. Aynı şekilde [Bölüm 2, Kesim 5.1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1)'deki $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ kuadratik formu $\mathbf{x}$ vektörünün bütün bileşenlerine bağlıdır. Bu tür eşlemeler için ayrı bir kavram gerekir.

:::definition Tanım 3.1 (Çok değişkenli fonksiyon, eş yükselti eğrisi)
<span class="anker" id="satz-3-1"></span>

Bir $f:\mathbb{R}^d\to\mathbb{R}$ fonksiyonu her $\mathbf{x}\in\mathbb{R}^d$ vektörüne bir $f(\mathbf{x})=f(x_1,\dots,x_d)$ sayısı karşılık getirir; buna __$d$ değişkenli fonksiyon__ denir. Bir $c$ sayısı için $f(\mathbf{x})=c$ olan bütün $\mathbf{x}$ noktalarının kümesine $f$ fonksiyonunun $c$ değerine ait __düzey kümesi__ denir. $d=2$ için bu küme çoğunlukla bir eğridir ve o zaman __eş yükselti eğrisi__ adını alır.
:::

İki değişken için bir arazi resmi yardımcı olur. $\mathbf{x}=(x_1,\,x_2)^{\top}$ vektörü bir harita üzerindeki bir konumdur, $f(\mathbf{x})$ de arazi yüzeyinin bu konumdaki yüksekliğidir. $f$ fonksiyonunun grafiği, yani uzaydaki $(x_1,\,x_2,\,f(x_1,x_2))$ noktalarının kümesi, arazinin yüzeyidir. Eş yükselti eğrileri, bir yürüyüş haritasında olduğu gibi aynı yükseklikteki bütün konumları birleştirir. Sık durdukları yerde arazi diktir; birbirinden uzak durdukları yerde düzdür. İkiden fazla değişkende resim ortadan kalkar, ama hesaplar aynı kalır.

::::beispiel [Sayısal örnek]
Kesim [3](#stufe-3) ile [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8) arasında bize şu fonksiyon eşlik ediyor:

<span class="anker" id="gl-3-1"></span>
$$f(\mathbf{x})=x_1^2\,x_2+x_2^2 . \tag{3.1}$$

$\mathbf{x}=(1,\,2)^{\top}$ noktasında $f(1,2)=1\cdot2+4=6$ olur. $f=6$ eş yükselti eğrisine $x_1^2x_2+x_2^2=6$ olan bütün noktalar aittir. $x_1=0$ için bu $x_2^2=6$ demektir, yani $(0;\ \sqrt6)^{\top}\approx(0;\ 2{,}449)^{\top}$ noktası eğrinin üzerindedir. Genel olarak denklem her sabit $x_1$ için $x_2$ değişkenine göre ikinci derecedendir ve pozitif çözümü $x_2=\tfrac12\bigl(\sqrt{x_1^4+24}-x_1^2\bigr)$, eş yükselti eğrisinin $x_1$ ekseninin üstündeki bütün kısmını betimler; $x_1=1$ için $\tfrac12(5-1)=2$ verir. Şekil [6](#abb-6) birkaç eş yükselti eğrisini gösteriyor.
::::

⁠**Kısacası:** $d$ değişkenli bir fonksiyon her vektöre bir sayı karşılık getirir; iki değişkende bir arazi olarak canlandırılır, eş yükselti eğrileri de aynı yükseklikteki konumları birleştirir.

### Kısmi türevler

<span class="anker" id="stufe-3-2"></span>

Yalnızca bir girdi değiştirildiğinde $f$ ne kadar güçlü tepki verir? Diğer bütün girdiler sabit tutulur ve $f$ tek değişkenli sıradan bir fonksiyona dönüşür. Arazi resminde arazi yüzeyi, eksenlerden birine paralel bir doğru boyunca kesilir. Kesit yüzeyinin kenarında bir eğri belirir, __kesit eğrisi__; bu eğrinin eğimi aranan duyarlılıktır.

:::definition Tanım 3.2 (Kısmi türev)
<span class="anker" id="satz-3-2"></span>

$f:\mathbb{R}^d\to\mathbb{R}$ fonksiyonunun $\mathbf{x}$ noktasında $x_j$ değişkenine göre __kısmi türevi__, limit var olduğu sürece şudur:

<span class="anker" id="gl-3-2"></span>
$$\frac{\partial f}{\partial x_j}(\mathbf{x})=\lim_{h\to0}\frac{f(\mathbf{x}+h\,\mathbf{e}_j)-f(\mathbf{x})}{h}, \tag{3.2}$$

burada $\mathbf{e}_j$, [Bölüm 1, Kesim 1.6](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-daten-als-zahlenlisten.html#stufe-1-6)'daki $j$-inci birim vektördür. Kısaca $\partial_jf(\mathbf{x})$ diye de yazılır.
:::

$\mathbf{x}+h\,\mathbf{e}_j$ vektörü $\mathbf{x}$ vektöründen yalnızca $j$-inci bileşende ayrılır, hem de $h$ kadar. Yani tanım, Kesim [1.2](die-ableitung.html#stufe-1-2)'deki sıradan türevin, $x_j$ dışındaki bütün değişkenler sabit tutulunca elde edilen fonksiyona uygulanmasıdır. Hesap kuralı buradan çıkar: $x_j$ değişkenine göre türev alınır ve diğer bütün değişkenlere sabitmiş gibi davranılır. $\partial$ simgesi kıvrık bir d'dir ve değişkenlerin yalnızca bir kısmının hareket ettiğini hatırlatır.

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=x_1^2x_2+x_2^2$ için $x_1$ değişkenine göre türev alırken $x_2$ değişkenine sabit gibi davranılır, tersi de geçerlidir:

$$\frac{\partial f}{\partial x_1}=2x_1\,x_2,\qquad \frac{\partial f}{\partial x_2}=x_1^2+2x_2 .$$

$(1,\,2)$ noktasında bu $4$ ve $5$ verir. Kesit eğrileriyle de aynısı görülür (Şekil [6](#abb-6)): $x_2=2$ sabit tutulursa geriye $x_1=1$ noktasında eğimi $4x_1=4$ olan $f(x_1,2)=2x_1^2+4$ kalır. $x_1=1$ sabit tutulursa geriye $x_2=2$ noktasında eğimi $1+2x_2=5$ olan $f(1,x_2)=x_2+x_2^2$ kalır.

:::abbildung ml/k3schnitt 6
$f(\mathbf{x})=x_1^2x_2+x_2^2$ için $(1,\,2)$ noktasında kesit eğrilerinin eğimleri olarak kısmi türevler. (a) $2$, $4$, $6$ (siyah), $8$ ve $10$ değerlerine ait eş yükselti eğrileri ile $(1,\,2)$ noktasından geçen iki kesit doğrusu. (b) Mavi $x_2=2$ doğrusu boyunca arazi $2x_1^2+4$ gibi uzanır; $x_1=1$ noktasındaki eğim $4$ olur. (c) Kırmızı $x_1=1$ doğrusu boyunca arazi $x_2+x_2^2$ gibi uzanır; $x_2=2$ noktasındaki eğim $5$ olur.
:::
::::

⁠**Kısacası:** $\partial f/\partial x_j$ kısmi türevi $x_j$ ekseni doğrultusundaki eğimdir: $x_j$ değişkenine göre türev alınır ve diğer bütün değişkenler sabit tutulur.

### Gradyan

<span class="anker" id="stufe-3-3"></span>

$d$ değişkenli bir fonksiyonun her noktada $d$ tane kısmi türevi vardır. Bunlarla $\mathbf{x}$ vektörünün kendisiyle olduğu gibi hesap yapabilmek için kısmi türevler bir vektörde bir araya getirilir.

:::definition Tanım 3.3 (Gradyan)
<span class="anker" id="satz-3-3"></span>

$f:\mathbb{R}^d\to\mathbb{R}$ fonksiyonunun $\mathbf{x}$ noktasında bütün kısmi türevleri varsa

<span class="anker" id="gl-3-3"></span>
$$\nabla f(\mathbf{x})=\begin{pmatrix}\partial_1f(\mathbf{x})\\ \vdots\\ \partial_df(\mathbf{x})\end{pmatrix}\in\mathbb{R}^d \tag{3.3}$$

sütun vektörüne $f$ fonksiyonunun $\mathbf{x}$ noktasındaki __gradyanı__ denir. $\nabla$ simgesi “nabla” diye okunur.
:::

Gradyan $\mathbf{x}$ ile aynı şekle sahiptir: her değişken için bir eleman, sütun olarak yazılmış. Bu uzlaşım bölümün tamamında geçerlidir; Kesim [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7) bu konuya geri döner, çünkü her kitap aynı uzlaşımı benimsemez. Her $\mathbf{x}$ noktasına gradyanı karşılık getirilirse bir ok alanı oluşur: haritanın her konumunda bir ok. Bu okların nereyi gösterdiğini Kesim [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) açıklar.

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=x_1^2x_2+x_2^2$ için şunlar bulunur:

$$\nabla f(\mathbf{x})=\begin{pmatrix}2x_1x_2\\ x_1^2+2x_2\end{pmatrix},\qquad \nabla f(1,2)=\begin{pmatrix}4\\5\end{pmatrix},\qquad \nabla f(0,1)=\begin{pmatrix}0\\2\end{pmatrix} .$$

$f(\mathbf{x})=x_1^2+x_2^2+x_3^2$ kareler toplamı için $\nabla f(\mathbf{x})=(2x_1,\,2x_2,\,2x_3)^{\top}=2\mathbf{x}$ olur.
::::

⁠**Kısacası:** Gradyan, bütün kısmi türevlerden oluşan ve $\mathbf{x}$ ile aynı şekle sahip sütun vektörüdür.

### Uzayda doğrusal yaklaşım

<span class="anker" id="stufe-3-4"></span>

Tek değişkende teğet, fonksiyonun bir nokta yakınındaki yerini alır. İki değişkende onun yerini bir düzlem alır. Büyüteç altında düzgün bir arazi bir noktanın yakınında eğik konmuş bir levha gibi görünür: Bu, __teğet düzlem__dir. $(\mathbf{x},\,f(\mathbf{x}))$ noktasından geçen bir düzlem $f(\mathbf{x})+m_1h_1+m_2h_2$ biçimindedir; burada $\mathbf{h}=(h_1,\,h_2)^{\top}$ harita üzerindeki yer değiştirme, $m_1$ ve $m_2$ de levhanın iki eksen doğrultusundaki eğiklikleridir. Düzlemin araziye yaslanması için eksenler boyunca eğikliklerinin kesit eğrilerinin eğimleriyle uyuşması gerekir, yani $m_j=\partial_jf(\mathbf{x})$.

Buradan çok değişken için doğrusal yaklaşım çıkar:

<span class="anker" id="gl-3-4"></span>
$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=f(\mathbf{x})+\sum_{j=1}^d\partial_jf(\mathbf{x})\,h_j . \tag{3.4}$$

Formül dikkat çekici bir şey söylüyor: Birkaç girdi aynı anda küçük miktarlarla değiştirilirse *etkileri toplanır*. Her değişken, yalnız o değiştirilmiş gibi $\partial_jf\cdot h_j$ katkısını yapar. Büyük değişimlerde bu artık doğru değildir, çünkü o zaman değişkenler, $x_1^2x_2$ örneğinde olduğu gibi birbirlerinin etkisini değiştirir. Küçük değişimlerde bu etkileşimler küçük büyüklüklerin çarpımlarıdır ve tek tek etkilerden daha hızlı sıfıra gider, tıpkı çarpım kuralındaki köşe parçası gibi.

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=x_1^2x_2+x_2^2$ için $\mathbf{x}=(1,\,2)^{\top}$ noktasında ve $\mathbf{h}=(0{,}01;\ 0{,}02)^{\top}$ yer değiştirmesi için şu bulunur:

$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=6+4\cdot0{,}01+5\cdot0{,}02=6+0{,}14=6{,}14 .$$

Tam değer $f(1{,}01;\ 2{,}02)=1{,}0201\cdot2{,}02+2{,}02^2=2{,}060602+4{,}0804=6{,}141002$ olur. $0{,}001002$ hatası, $0{,}14$ değişiminin kendisinden çok daha küçüktür. Şekil [7](#abb-7) iç çarpımı adım adım gösteriyor.

:::abbildung ml/k3rlinear 7
Doğrusal yaklaşımdaki değişim, gradyan ile yer değiştirmenin iç çarpımı olarak: Her değişken kendi kısmi türevi çarpı kendi değişimi kadar katkı yapar.
:::
::::

⁠**Kısacası:** $\mathbf{x}$ yakınında $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$ olur: Küçük değişimlerde tek tek değişkenlerin etkileri toplanır.

### Türevlenebilirlik

<span class="anker" id="stufe-3-5"></span>

[(3.4)](#gl-3-4) yaklaşımı şimdiye kadar yalnızca akla yatkın kılındı. Tek değişkende türevin varlığından çıkıyordu. Birden çok değişkende ise, aşağıdaki karşı örneğin gösterdiği gibi, kısmi türevlerin varlığı bunun için yetmez. Bu yüzden yaklaşımın kendisi şart koşulur: Yaklaşımın hatası yer değiştirmeden daha hızlı sıfıra gitmelidir, tıpkı [(1.4)](die-ableitung.html#gl-1-4) bağıntısındaki $r(h)$ hatasının $h$'den daha hızlı sıfıra gitmesi gibi. Bir vektöre bölünemez; bu yüzden $h$ yerine [Bölüm 1, Kesim 3.1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3-1)'deki $\lVert\mathbf{h}\rVert$ uzunluğuna bölünür.

:::definition Tanım 3.4 (Türevlenebilirlik)
<span class="anker" id="satz-3-4"></span>

Bir $f:\mathbb{R}^d\to\mathbb{R}$ fonksiyonuna, şu koşulu sağlayan bir $\mathbf{g}\in\mathbb{R}^d$ vektörü varsa $\mathbf{x}$ noktasında __türevlenebilir__ denir:

<span class="anker" id="gl-3-5"></span>
$$\lim_{\mathbf{h}\to\mathbf{0}}\frac{f(\mathbf{x}+\mathbf{h})-f(\mathbf{x})-\mathbf{g}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=0 . \tag{3.5}$$

$\mathbf{h}\to\mathbf{0}$ limiti şu anlama gelir: $\lVert\mathbf{h}\rVert$ yeterince küçük ve $\mathbf{h}\ne\mathbf{0}$ olduğu sürece, $\mathbf{h}$ hangi doğrultudan yaklaşırsa yaklaşsın bölüm $0$'a istenildiği kadar yakındır.
:::

:::satz Teorem 3.5 (Türevlenebilir demek: gradyan ve doğrusal yaklaşım)
<span class="anker" id="satz-3-5"></span>

$f$, $\mathbf{x}$ noktasında türevlenebilirse orada bütün kısmi türevler vardır ve [(3.5)](#gl-3-5) içindeki vektör gradyandır: $\mathbf{g}=\nabla f(\mathbf{x})$. Tersine, bütün kısmi türevler $\mathbf{x}$ yakınında varsa ve $\mathbf{x}$ noktasında sürekliyse $f$, $\mathbf{x}$ noktasında türevlenebilirdir.
:::

:::beweis Vektör gradyandır
[(3.5)](#gl-3-5) içinde özel olarak, $t\ne0$ bir sayı olmak üzere $\mathbf{h}=t\,\mathbf{e}_j$ seçilir; o zaman $\lVert\mathbf{h}\rVert=|t|$ ve $\mathbf{g}^{\top}\mathbf{h}=t\,g_j$ olur. Bölüm $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})-t\,g_j}{|t|}$ biçimini alır ve $0$'a gider. O zaman $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})}{t}-g_j$ de $0$'a gider, çünkü bu sayının mutlak değeri öncekiyle aynıdır. Dolayısıyla $x_j$ değişkenine göre kısmi türev vardır ve $g_j$ değerine eşittir. Bu her $j$ için geçerlidir.
:::

Uygulama için ikinci önerme önemlidir. Polinomlar, üstel fonksiyon, lojistik fonksiyon ve bunlardan temel aritmetik işlemler ve bileşkeyle kurulan her şey, tanımlı oldukları her yerde sürekli kısmi türevlere sahiptir. Yani bu tür fonksiyonlar türevlenebilirdir ve onlar için [(3.4)](#gl-3-4) geçerlidir. Bu bölümdeki istisnalar, $|x|$ ya da $\max(x,\,0)$ örneğindeki gibi köşe noktalarıdır.

:::warnung Kısmi türevler tek başına yetmez
$f(0,0)=0$ olmak üzere $f(x_1,x_2)=\dfrac{x_1x_2}{x_1^2+x_2^2}$ fonksiyonu iki eksen üzerinde de sıfırdır, çünkü orada $x_1x_2=0$ olur. Dolayısıyla orijinden geçen ve eksenler boyunca uzanan kesit eğrileri yataydır: $\partial_1f(0,0)=\partial_2f(0,0)=0$, orijindeki gradyan $\mathbf{0}$ olur. Bu yüzden doğrusal yaklaşım, $f$ fonksiyonunun orijin yakınında neredeyse $0$ olduğunu öngörür. Oysa $t\ne0$ olmak üzere $x_1=x_2=t$ köşegeni üzerinde, $t$ ne kadar küçük olursa olsun $f(t,t)=t^2/(2t^2)=\tfrac12$ olur. Fonksiyon orijinde sıçrar ve hiçbir düzlem ona yaslanmaz. İki kısmi türev de var olduğu hâlde fonksiyon orada türevlenebilir değildir. Gradyanın varlığından doğrusal yaklaşımı çıkaran kişi bu yüzden türevlenebilirliğe ihtiyaç duyar, örneğin sürekli kısmi türevler yoluyla.
:::

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=x_1^2x_2+x_2^2$ için $2x_1x_2$ ve $x_1^2+2x_2$ kısmi türevleri polinomdur, yani her yerde süreklidir; dolayısıyla $f$ her yerde türevlenebilir. [(3.4)](#gl-3-4) ile ilgili sayısal örnekte hata, $\lVert\mathbf{h}\rVert=\sqrt{0{,}0001+0{,}0004}\approx0{,}0224$ için $0{,}001002$ idi; [(3.5)](#gl-3-5) içindeki bölüm yani yaklaşık $0{,}045$ olur. $\mathbf{h}$ yarıya indirilip $(0{,}005;\ 0{,}01)^{\top}$ yapılırsa hata $f(1{,}005;\ 2{,}01)-6-0{,}07=0{,}000250\ldots$, bölüm ise yaklaşık $0{,}022$ olur: Bölüm $\mathbf{h}$ ile birlikte yarıya iner ve $0$'a gider.
::::

⁠**Kısacası:** Türevlenebilir demek, gradyanla yapılan doğrusal yaklaşımın hatasının $\lVert\mathbf{h}\rVert$'den daha hızlı sıfıra gitmesi demektir; sürekli kısmi türevler bunu garanti eder, yalnızca var olmaları etmez.

:::hintergrund Sürekli kısmi türevler neden yeterlidir
$\mathbf{x}$ noktasından $\mathbf{x}+\mathbf{h}$ noktasına eğik olarak değil, eksenlere paralel iki etapta gidilir: önce $x_1$ doğrultusunda $h_1$ kadar, sonra $x_2$ doğrultusunda $h_2$ kadar. Her etapta yalnızca bir değişken değişir ve tek değişkenli ortalama değer teoremine göre değişim, etabın bir ara noktasında hesaplanmış $\partial_jf\cdot h_j$ değerine tam olarak eşittir. Kısmi türevler sürekliyse ara noktalardaki değerleri $\mathbf{x}$ noktasındaki değerlere yakındır ve iki etabın toplamı $\nabla f(\mathbf{x})^{\top}\mathbf{h}$ ifadesinden ancak $\lVert\mathbf{h}\rVert$'den hızlı sıfıra giden bir miktar kadar farklıdır. Karşı örnekte tam olarak bu adım çöker: Kısmi türevleri orijin dışında var olsa da sürekli değildir. Örneğin $x_1=0$ ekseni üzerinde $\partial_1f(0,x_2)=1/x_2$ olur ve bu, değerin $0$ olduğu orijine yaklaştıkça istenildiği kadar büyür.
:::

:::aufgabe Alıştırma 9 ★ Kısmi türevler ve gradyanlar
<span class="anker" id="aufg-9"></span>

Verilen noktada kısmi türevleri ve gradyanı hesaplayın.

<ol class="al">

<li>

$(4,\,-1)$ noktasında $f(\mathbf{x})=3x_1-2x_2+5$;

</li>

<li>

$(2,\,0)$ ve $(1,\,1)$ noktalarında $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$;

</li>

<li>

$(1,\,2,\,3)$ noktasında $f(\mathbf{x})=x_1x_2+x_2x_3+x_3x_1$.

</li>

</ol>

:::loesung
(a) $\partial_1f=3$, $\partial_2f=-2$, dolayısıyla her noktada $\nabla f=(3,\,-2)^{\top}$.

(b) $\partial_1f=\mathrm{e}^{x_2}$ ve $\partial_2f=x_1\mathrm{e}^{x_2}$. $(2,\,0)$ noktasında $\nabla f=(1,\,2)^{\top}$, $(1,\,1)$ noktasında $\nabla f=(\mathrm{e},\,\mathrm{e})^{\top}\approx(2{,}718;\ 2{,}718)^{\top}$ olur.

(c) $\partial_1f=x_2+x_3$, $\partial_2f=x_1+x_3$, $\partial_3f=x_1+x_2$; dolayısıyla $(1,\,2,\,3)$ noktasında $\nabla f=(5,\,4,\,3)^{\top}$.
:::
:::

:::aufgabe Alıştırma 10 ★★ İki değişkenle doğrusal yaklaşım
<span class="anker" id="aufg-10"></span>

$f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$ olsun.

<ol class="al">

<li>

$(2,\,0)$ noktasındaki doğrusal yaklaşımla $f(2{,}1;\ -0{,}05)$ için bir yaklaşık değer hesaplayın ve tam değerle karşılaştırın.

</li>

<li>

İki değişimden hangisi $f$ fonksiyonunun değişimine daha çok katkı yapar? Bu iki değişim doğrusal yaklaşımda neden tam olarak birbirini götürür de tam değerde götürmez?

</li>

</ol>

:::loesung
(a) $f(2,0)=2$ ve Alıştırma [9](#aufg-9)'a göre $\nabla f(2,0)=(1,\,2)^{\top}$ olur. $\mathbf{h}=(0{,}1;\ -0{,}05)^{\top}$ ile:

$$f(2{,}1;\ -0{,}05)\approx2+1\cdot0{,}1+2\cdot(-0{,}05)=2+0{,}1-0{,}1=2{,}0 .$$

Tam değer $2{,}1\,\mathrm{e}^{-0{,}05}\approx2{,}1\cdot0{,}951229\approx1{,}99758$ olur. Hata yaklaşık $0{,}0024$ kadardır.

(b) İki değişim de aynı ölçüde katkı yapar, $+0{,}1$ ve $-0{,}1$, ve doğrusal yaklaşımda birbirini götürür. Tam değerde ise değişkenler birbirini etkiler: $x_1$ büyüdükçe $f$, $x_2$'ye daha güçlü tepki verir, çünkü $\partial_2f=x_1\mathrm{e}^{x_2}$ türevi $x_1$ ile birlikte büyür. Bu yüzden $x_2$'nin küçülmesi, doğrusal yaklaşımın varsaydığından biraz daha güçlü etki eder. Böyle etkileşimler iki değişimin çarpımlarıdır, burada örneğin $0{,}1\cdot(-0{,}05)=-0{,}005$; doğrusal yaklaşımın dışarıda bıraktığı ikinci mertebe terimlere aittirler. Kesim [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8) bunları hesaplar (Alıştırma [29](die-hesse-matrix-und-die-quadratische-naherung.html#aufg-29)).
:::
:::

:::aufgabe Alıştırma 11 ★★ Eş yükselti eğrileri ve kesit eğrileri
<span class="anker" id="aufg-11"></span>

$f(\mathbf{x})=x_1^2x_2+x_2^2$, [(3.1)](#gl-3-1) bağıntısındaki gibi olsun.

<ol class="al">

<li>

$f$ fonksiyonunun $(2,\,1)$ noktasındaki değeri nedir? Aynı eş yükselti eğrisi üzerinde $x_1=0$ olan başka bir nokta verin.

</li>

<li>

$\nabla f(2,1)$ gradyanını ve $(2,\,1)$ noktasından geçen iki kesit eğrisinin denklemlerini hesaplayın. Eğimlerini kontrol edin.

</li>

</ol>

:::loesung
(a) $f(2,1)=4\cdot1+1=5$. $x_1=0$ olduğunda eş yükselti eğrisi $x_2^2=5$ koşulunu gerektirir; dolayısıyla örneğin $(0;\ \sqrt5)\approx(0;\ 2{,}236)$ noktası bu eğri üzerindedir.

(b) $\nabla f(2,1)=(2\cdot2\cdot1,\ 4+2\cdot1)^{\top}=(4,\,6)^{\top}$. $x_2=1$ boyunca kesit eğrisi $f(x_1,1)=x_1^2+1$ olur; eğimi $x_1=2$ noktasında $2x_1=4$ olur. $x_1=2$ boyunca kesit eğrisi $f(2,x_2)=4x_2+x_2^2$ olur; eğimi $x_2=1$ noktasında $4+2x_2=6$ olur. İki eğim de gradyanın bileşenleriyle örtüşür.
:::
:::

:::aufgabe Alıştırma 12 ★★★ Sürekli ama türevlenebilir değil
<span class="anker" id="aufg-12"></span>

$f(x_1,x_2)=\sqrt{|x_1x_2|}$ olsun.

<ol class="al">

<li>

İki kısmi türevin de orijinde var olduğunu ve $0$ olduğunu gösterin.

</li>

<li>

$\mathbf{h}=(t,\,t)^{\top}$ ile, $\mathbf{g}=\mathbf{0}$ için [(3.5)](#gl-3-5) içindeki bölümün $0$'a gitmediğini gösterin. $f$ orada sürekli olduğu hâlde, bundan neden $f$ fonksiyonunun orijinde türevlenebilir olmadığı sonucu çıkar?

</li>

</ol>

:::loesung
(a) İki eksen üzerinde de $x_1x_2=0$, dolayısıyla $f=0$ olur. Böylece her $h\ne0$ için $\frac{f(h,0)-f(0,0)}{h}=0$ olur; ikinci değişken için de aynısı geçerlidir. Orijindeki iki kısmi türev de $0$'dır.

(b) $f$ orijinde türevlenebilir olsaydı, Kesim [3.5](#stufe-3-5)'teki teoreme göre [(3.5)](#gl-3-5) içindeki vektör $\mathbf{0}$ gradyanı olmak zorunda kalırdı. Oysa $\mathbf{h}=(t,\,t)^{\top}$ ile $f(\mathbf{h})=\sqrt{t^2}=|t|$ ve $\lVert\mathbf{h}\rVert=\sqrt2\,|t|$ olur, dolayısıyla

$$\frac{f(\mathbf{h})-f(\mathbf{0})-\mathbf{0}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=\frac{|t|}{\sqrt2\,|t|}=\frac1{\sqrt2}\approx0{,}707 ,$$

ve bu, $t\ne0$ ne kadar küçük olursa olsun geçerlidir. Bölüm $0$'a gitmez, dolayısıyla $f$ türevlenebilir değildir. Yine de $f$ süreklidir, çünkü $\mathbf{x}$, $\mathbf{0}$ vektörüne giderken $|f(\mathbf{x})|=\sqrt{|x_1|\,|x_2|}\le\max(|x_1|,|x_2|)\le\lVert\mathbf{x}\rVert$ de $0$'a gider. Arazi yüzeyinde orijinde bir boşluk yoktur, ama köşegen boyunca hiçbir düzlemin yaslanmadığı bir kıvrım vardır.
:::
:::
