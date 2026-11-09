---
title: Doğrusal denklem sistemleri
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
knoten: Temeller 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15211300
summary: Şimdiye kadar x girişi verilmişti ve Ax çıkışı aranıyordu.
tags: doğrusal denklem sistemi, katsayı matrisi, sağ taraf, çözüm, genişletilmiş katsayı matrisi, Gauss eleme yöntemi, satır basamak biçimi, homojen
lang: tr
---

<span class="anker" id="stufe-12"></span>

:::zweck
Şimdiye kadar $\mathbf{x}$ girişi verilmişti ve $\mathbf{A}\mathbf{x}$ çıkışı aranıyordu. Bu kesim ters soruyu soruyor: Hangi giriş, önceden verilmiş bir çıkışı üretir? Bu bir doğrusal denklem sistemidir. Kesim, böyle bir sistemin nasıl çözüldüğünü ve ne zaman hiç çözümü olmadığını, tam olarak bir çözümü ya da sonsuz sayıda çözümü olduğunu gösteriyor.
:::

### Matris biçiminde denklem sistemleri

<span class="anker" id="stufe-12-1"></span>

Okuldan şu türden sorular bilinir: İki sayı, $x_1$ ve $x_2$, $2x_1+x_2=5$ ve $x_1+x_2=3$ eşitliklerini sağlıyor; bu sayılar nedir? Sol taraflar bir matris-vektör çarpımının bileşenleridir. Demek ki soru şudur: $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ matrisi hangi $\mathbf{x}$ vektörünü $(5,\,3)^{\top}$ vektörüne götürür?

:::definition Tanım 12.1 (Doğrusal denklem sistemi)
<span class="anker" id="satz-12-1"></span>

Bir $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisi ve bir $\mathbf{y}\in\mathbb{R}^m$ vektörü için

<span class="anker" id="gl-12-1"></span>
$$\mathbf{A}\mathbf{x}=\mathbf{y} \tag{12.1}$$

eşitliğine $m$ denklemli ve $x_1,\dots,x_n$ olmak üzere $n$ bilinmeyenli bir __doğrusal denklem sistemi__ denir. $\mathbf{A}$ matrisine __katsayı matrisi__, $\mathbf{y}$ vektörüne __sağ taraf__ denir. [(12.1)](#gl-12-1) eşitliğini sağlayan her $\mathbf{x}\in\mathbb{R}^n$ vektörüne bir __çözüm__ denir.
:::

Açık yazıldığında $i$ numaralı satırda $a_{i1}x_1+\dots+a_{in}x_n=y_i$ denklemi durur.

::::beispiel [Sayısal örnek]
$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}5\\3\end{pmatrix}$$

sisteminin çözümü $\mathbf{x}=(2,\,1)^{\top}$ olur: $2\cdot2+1=5$ ve $2+1=3$. Katsayı matrisi, tersi $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$ olan matris olarak daha önceden bilinir (alt kesim [11.2](einheitsmatrix-und-inverse.html#stufe-11-2)). Sistem soldan bu tersle çarpılırsa çözüm hemen ortaya çıkar: $\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}=(5-3,\ -5+6)^{\top}=(2,\,1)^{\top}$.
::::

⁠**Kısacası:** $\mathbf{A}\mathbf{x}=\mathbf{y}$ doğrusal denklem sistemi, hangi $\mathbf{x}$ girişinin $\mathbf{y}$ çıkışını verdiğini sorar.

### Satır resmi ve sütun resmi

<span class="anker" id="stufe-12-2"></span>

Matris-vektör çarpımında olduğu gibi bir denklem sistemini okumanın da iki yolu vardır.

**Satır resmi.** Her denklem tek başına bir noktalar kümesini betimler. İki bilinmeyen varsa $2x_1+x_2=5$ düzlemde bir doğrudur, $x_1+x_2=3$ de öyle. Bir çözüm iki denklemi de sağlamak, yani iki doğrunun da üzerinde bulunmak zorundadır: Doğruların kesişim noktasıdır (Şekil [38](#abb-38), sol). Üç bilinmeyen varsa her denklem uzayda bir düzlemdir.

**Sütun resmi.** [(7.3)](das-matrix-vektor-produkt.html#gl-7-3) sütun bakışına göre $\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+\dots+x_n\mathbf{a}_n$ olur. Demek ki denklem şunu sorar: Sütunların doğrusal bileşimi hangi katsayılarla sağ tarafı verir? Yukarıdaki sistemde: $x_1\,(2,\,1)^{\top}+x_2\,(1,\,1)^{\top}=(5,\,3)^{\top}$; çözüm $x_1=2$ ve $x_2=1$ olur. Şekil [30](das-matrix-vektor-produkt.html#abb-30) içinde sağda görülen resim tam olarak budur.

:::abbildung ml/k1lgs 38
İki bilinmeyenli üç denklem sisteminin satır resmi. Her denklem bir doğrudur, bir çözüm bütün doğruların üzerinde bulunur. (a) Doğrular bir noktada kesişir. (b) Doğrular paraleldir ve ortak noktaları yoktur. (c) İki denklem aynı doğruyu betimler ve bu doğrunun her noktası bir çözümdür.
:::

Sütun resmi, ne zaman bir çözümün var olduğu sorusunu hemen cevaplar. $\mathbf{A}\mathbf{x}$ vektörleri sütun uzayını oluşturur (alt kesim [7.4](das-matrix-vektor-produkt.html#stufe-7-4)).

:::satz Teorem 12.2 (Çözülebilirlik)
<span class="anker" id="satz-12-2"></span>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ sisteminin ancak ve ancak $\mathbf{y}$ vektörü $\mathbf{A}$ matrisinin sütun uzayındaysa bir çözümü vardır.
:::

::::beispiel [Sayısal örnek]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)\mathbf{x}=\mathbf{y}$ sistemi $\mathbf{y}=(3,\,6)^{\top}$ için çözülebilir, örneğin $\mathbf{x}=(1,\,1)^{\top}$ ile; ama $\mathbf{y}=(1,\,1)^{\top}$ için çözülemez: Sütun uzayı yalnızca $(1,\,2)^{\top}$ doğrultusundaki doğrudur (alt kesim [7.4](das-matrix-vektor-produkt.html#stufe-7-4)).
::::

⁠**Kısacası:** Satır resminde bir çözüm bütün denklemlerin ortak bir noktasıdır, sütun resminde ise sütunların sağ tarafı vermesini sağlayan katsayı seçimidir.

### Gauss eleme yöntemi

<span class="anker" id="stufe-12-3"></span>

İki bilinmeyende çözüm bakarak bulunabilir. Üç ya da daha fazla bilinmeyende her zaman işe yarayan bir yönteme ihtiyaç vardır. Fikir okuldakiyle aynıdır: Bir denklemin bir katı başka bir denklemden çıkarılır, böylece bir bilinmeyen yok olur. Bu, son denklem yalnızca tek bir bilinmeyen içerene kadar tekrarlanır.

Bunun için yalnızca sayılar yazılır: katsayı matrisi ve bir çizgiyle ayrılmış olarak sağ taraf. Bu tabloya __genişletilmiş katsayı matrisi__ $(\mathbf{A}\,|\,\mathbf{y})$ denir.

:::definition Tanım 12.3 (Gauss eleme yöntemi)
<span class="anker" id="satz-12-3"></span>

__Gauss eleme yöntemi__, genişletilmiş katsayı matrisini üç satır işlemiyle dönüştürür:

<ol>

<li>

bir satırın bir katını başka bir satıra eklemek;

</li>

<li>

iki satırın yerini değiştirmek;

</li>

<li>

bir satırı sıfırdan farklı bir sayıyla çarpmak.

</li>

</ol>

Amaç, __satır basamak biçimi__ denen biçime ulaşmaktır: Her satırda sıfırdan farklı ilk elemanın önünde, üstteki satırdakinden en az bir fazla sıfır bulunur. Ardından bilinmeyenler aşağıdan yukarıya doğru belirlenir (geriye doğru yerine koyma).
:::

:::satz Teorem 12.4 (Satır işlemleri çözümleri değiştirmez)
<span class="anker" id="satz-12-4"></span>

Bir sistem ile ondan satır işlemleriyle elde edilen sistemin çözümleri aynıdır.
:::

:::beweis Satır işlemleri
Eski sistemin her çözümü yeni denklemleri de sağlar, çünkü yeni denklemler eskilerin toplamları ve katlarıdır. Ama üç işlemin her biri geri de alınabilir: eklenen kat yeniden çıkarılır, satırların yeri yeniden değiştirilir, sayıya bölünür. Demek ki tersine, yeni sistemin her çözümü eskisini de sağlar.
:::

::::beispiel [Sayısal örnek]
$$\begin{aligned} x_1+2x_2+x_3&=8\\ 2x_1+x_2+x_3&=7\\ x_1+x_2+2x_3&=9 \end{aligned} \qquad\text{sisteminin genişletilmiş katsayı matrisi şudur:}\qquad \left(\begin{array}{ccc|c}1&2&1&8\\2&1&1&7\\1&1&2&9\end{array}\right).$$

Birinci satır ikinci satırdan iki kez, üçüncü satırdan bir kez çıkarılırsa $x_1$ ikisinden de yok olur. Ardından yeni ikinci ve üçüncü satırların yeri değiştirilir ve yeni ikinci satır üçüncüden üç kez çıkarılırsa $x_2$ de son satırdan yok olur:

$$\left(\begin{array}{ccc|c}1&2&1&8\\0&-3&-1&-9\\0&-1&1&1\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&-3&-1&-9\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&0&-4&-12\end{array}\right).$$

Aşağıdan yukarıya: $-4x_3=-12$, dolayısıyla $x_3=3$; sonra $-x_2+3=1$, dolayısıyla $x_2=2$; sonra $x_1+4+3=8$, dolayısıyla $x_1=1$. Çözüm $\mathbf{x}=(1,\,2,\,3)^{\top}$ olur; üç denklemin hepsinde yerine koymak bunu doğrular.
::::

⁠**Kısacası:** Gauss eleme yöntemi, çözümleri değiştirmeyen satır işlemleriyle bilinmeyenleri adım adım yok eder ve sonra aşağıdan yukarıya doğru yerine koyar.

:::hintergrund Çözmek için neden ters matris hesaplanmaz?
$\mathbf{A}$ tersinirse çözüm $\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}$ olur. Bu, akıl yürütmek için yararlıdır, ama bir hesap yolu olarak elverişsizdir. Gauss eleme yöntemi $n$ denklemli ve $n$ bilinmeyenli bir sistem için yaklaşık $\tfrac23n^3$ temel aritmetik işlem gerektirir; tersi hesaplamak yaklaşık $2n^3$, yani üç katı tutar ve ardından bir de $\mathbf{A}^{-1}\mathbf{y}$ çarpımı eklenir. Ayrıca bir bilgisayar sonlu sayıda basamakla hesap yapar. O zaman ters ancak yuvarlanmış olarak gösterilebilir ve doğrudan eleme genellikle daha doğru sonuçlar verir. Bu yüzden ters matris her şeyden önce düşünmek ve türetmek için bir araçtır, hesaplamak için değil.
:::

### Çözüm yok, bir çözüm ya da sonsuz sayıda çözüm

<span class="anker" id="stufe-12-4"></span>

Düzlemdeki iki doğru ya bir noktada kesişir, ya paraleldir ya da çakışır (Şekil [38](#abb-38)). Tam olarak iki kesişim noktası olamaz. Aynı şey, ne kadar büyük olursa olsun her doğrusal denklem sistemi için geçerlidir.

:::satz Teorem 12.5 (Çözüm sayısı)
<span class="anker" id="satz-12-5"></span>

Bir doğrusal denklem sisteminin ya hiç çözümü yoktur, ya tam olarak bir çözümü ya da sonsuz sayıda çözümü vardır.
:::

:::beweis Çözüm sayısı
Şunu göstermek yeter: Sistemin iki farklı $\mathbf{x}\ne\mathbf{x}'$ çözümü varsa sonsuz sayıda çözümü vardır. Her $t$ sayısı için şu geçerlidir:

$$\mathbf{A}\bigl(\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})\bigr)=\mathbf{A}\mathbf{x}+t\,(\mathbf{A}\mathbf{x}'-\mathbf{A}\mathbf{x})=\mathbf{y}+t\,(\mathbf{y}-\mathbf{y})=\mathbf{y} ,$$

dolayısıyla $\mathbf{x}$ ve $\mathbf{x}'$ noktalarından geçen doğrunun her $\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})$ noktası bir çözümdür ve farklı $t$ değerleri farklı noktalar verir.
:::

Sağ tarafı sıfır olan $\mathbf{A}\mathbf{x}=\mathbf{0}$ sistemine __homojen__ denir. Bu sistemin her zaman $\mathbf{x}=\mathbf{0}$ çözümü vardır. $\mathbf{A}\mathbf{x}=\mathbf{y}$ sisteminin tek bir $\mathbf{x}_{\mathrm s}$ çözümü biliniyorsa öbür bütün çözümler, buna homojen sistemin çözümleri eklenerek elde edilir: $\mathbf{A}\mathbf{x}=\mathbf{y}$ ancak ve ancak $\mathbf{A}(\mathbf{x}-\mathbf{x}_{\mathrm s})=\mathbf{y}-\mathbf{y}=\mathbf{0}$ ise geçerlidir.

::::beispiel [Sayısal örnek]
Şekildeki üç sistem (Şekil [38](#abb-38)):

<ol class="al">

<li>

$2x_1+x_2=5$, $x_1+x_2=3$: tam olarak bir çözüm, $(2,\,1)^{\top}$.

</li>

<li>

$x_1+x_2=3$, $x_1+x_2=1$: çözüm yok, çünkü aynı toplam aynı anda hem $3$ hem $1$ olamaz.

</li>

<li>

$x_1+x_2=3$, $2x_1+2x_2=6$: İkinci denklem birincinin iki katıdır. Bir çözüm $\mathbf{x}_{\mathrm s}=(3,\,0)^{\top}$ olur ve $x_1+x_2=0$ homojen sistemini $(-1,\,1)^{\top}$ vektörünün bütün katları çözer. Demek ki bütün çözümler, $t$ herhangi bir sayı olmak üzere $\mathbf{x}=(3,\,0)^{\top}+t\,(-1,\,1)^{\top}$ biçimindedir.

</li>

</ol>
::::

⁠**Kısacası:** Bir doğrusal denklem sisteminin ya hiç çözümü yoktur, ya tam olarak bir ya da sonsuz sayıda çözümü vardır; bütün çözümler, bir çözüm artı homojen sistemin çözümleridir.

### Bilinmeyenlerden fazla denklem

<span class="anker" id="stufe-12-5"></span>

Verilerde denklemler ile bilinmeyenler çoğu zaman eşit sayıda değildir. Diyelim ki alan için bir $w_1$ ağırlığı ve odalar için bir $w_2$ ağırlığı aranıyor; ağırlıklı toplam üç dairede gerçek fiyatı tam olarak tutturmalı. Bunlar iki bilinmeyen için üç denklemdir.

:::definition Tanım 12.6 (Aşırı belirlenmiş, eksik belirlenmiş)
<span class="anker" id="satz-12-6"></span>

Denklem sayısı bilinmeyen sayısından fazla olan ($m>n$) bir doğrusal denklem sistemine __aşırı belirlenmiş__, az olana ($m<n$) __eksik belirlenmiş__ denir.
:::

Aşırı belirlenmiş bir sistemin çoğunlukla çözümü yoktur: İki denklem iki bilinmeyeni zaten belirler ve üçüncü denklemin de rastlantı sonucu sağlanması gerekirdi. Sütun resminde: $\mathbb{R}^m$ uzayındaki $n$ sütunun sütun uzayı, $n<m$ için $\mathbb{R}^m$ uzayının yalnızca küçük bir parçasıdır ve sağ taraf neredeyse hiçbir zaman onun içinde bulunmaz. Eksik belirlenmiş bir sistemin ise, çözülebiliyorsa, sonsuz sayıda çözümü vardır: Satır basamak biçiminde en az bir bilinmeyenin kendi pivotu olmaz ve bu bilinmeyen serbestçe seçilebilir.

::::beispiel [Sayısal örnek]
Fiyatları $200$, $130$ ve $290$ bin avro olan 1, 2 ve 3 numaralı daireler için sistem şudur:

$$60\,w_1+2\,w_2=200,\qquad 40\,w_1+w_2=130,\qquad 90\,w_1+4\,w_2=290 .$$

İlk iki denklemden $w_1=3$ ve $w_2=10$ çıkar: İkinci denklem birinciden iki kez çıkarılırsa $-20\,w_1=-60$ kalır. Ama üçüncü denklemde yerine konunca bu, $270+40=310\ne290$ verir. Sistemin çözümü yoktur. Hiçbir ağırlık çifti üç fiyatın üçünü de tam olarak tutturamaz. Böyle bir durumda bunun yerine ne arandığı ayrı bir sorudur.
::::

⁠**Kısacası:** Aşırı belirlenmiş bir sistemde bilinmeyenlerden fazla denklem vardır ve sistem çoğunlukla çözülemez; eksik belirlenmiş bir sistemde daha az denklem vardır ve sistem çözülebiliyorsa sonsuz sayıda çözümü vardır.

:::aufgabe Alıştırma 28 ★★ Gauss eleme yöntemi
<span class="anker" id="aufg-28"></span>

Gauss eleme yöntemiyle çözün ve sonucu kontrol edin:

$$x_1+x_2+x_3=6,\qquad 2x_1+3x_2+x_3=11,\qquad x_1-x_2+2x_3=5 .$$

:::loesung
Genişletilmiş katsayı matrisi $\Bigl(\begin{smallmatrix}1&1&1&|&6\\2&3&1&|&11\\1&-1&2&|&5\end{smallmatrix}\Bigr)$ olur. Birinci satır ikinci satırdan iki kez, üçüncü satırdan bir kez çıkarılınca $(0,\,1,\,-1\,|\,-1)$ ve $(0,\,-2,\,1\,|\,-1)$ satırları oluşur. Ardından yeni ikinci satır üçüncü satıra iki kez eklenince üçüncü satır $(0,\,0,\,-1\,|\,-3)$ olur. Basamak biçimi şudur:

$$x_1+x_2+x_3=6,\qquad x_2-x_3=-1,\qquad -x_3=-3 .$$

Aşağıdan yukarıya: $x_3=3$, $x_2=-1+3=2$, $x_1=6-2-3=1$. Sağlama: $1+2+3=6$, $2+6+3=11$, $1-2+6=5$. Çözüm $\mathbf{x}=(1,\,2,\,3)^{\top}$ olur.
:::
:::

:::aufgabe Alıştırma 29 ★★ Kaç çözüm var?
<span class="anker" id="aufg-29"></span>

Her sistem için çözüm kümesini belirleyin ve satır resmini çizin:

<ol class="al">

<li>

$x_1+2x_2=3$, $2x_1+4x_2=6$;

</li>

<li>

$x_1+2x_2=3$, $2x_1+4x_2=5$;

</li>

<li>

$x_1+2x_2=3$, $x_1-x_2=0$.

</li>

</ol>

:::loesung
(a) İkinci denklem birincinin iki katıdır; ikisi de aynı doğruyu tanımlar. Sonsuz sayıda çözüm: $x_2=t$ ile $x_1=3-2t$, dolayısıyla $\mathbf{x}=(3,\,0)^{\top}+t\,(-2,\,1)^{\top}$.

(b) Birinci denklem iki ile çarpılınca $2x_1+4x_2=6$ elde edilir; bu, $2x_1+4x_2=5$ ile çelişir. Doğrular paraleldir; çözüm yoktur.

(c) İkinci denklemden $x_1=x_2$ çıkar; birinci denklemde yerine konunca $3x_2=3$. Tek bir çözüm vardır: $\mathbf{x}=(1,\,1)^{\top}$, paralel olmayan iki doğrunun kesişim noktası.
:::
:::

:::aufgabe Alıştırma 30 ★★ Uyan ağırlıklar
<span class="anker" id="aufg-30"></span>

Aşırı belirlenmiş sisteme (alt kesim [12.5](#stufe-12-5)) fiyatı $240$ bin avro olan Daire 4'ü de ekleyin.

<ol class="al">

<li>

$w_1=3$, $w_2=10$ ile dört daireden hangilerinin fiyatı tam olarak tutturulur?

</li>

<li>

Dört denklemli sistemi $\mathbf{A}\mathbf{w}=\mathbf{y}$ biçiminde yazın. $\mathbf{A}$, $\mathbf{w}$ ve $\mathbf{y}$ hangi tiptedir? “Çözüm yok” sütun resminde ne anlama gelir?

</li>

</ol>

:::loesung
(a) $w_1=3$, $w_2=10$ ile: Daire 1: $180+20=200$ (tutturuldu), Daire 2: $120+10=130$ (tutturuldu), Daire 3: $290$ yerine $270+40=310$ (tutturulamadı), Daire 4: $210+30=240$ (tutturuldu). Dört fiyattan üçü tutuyor, ama hepsi değil.

(b) $\mathbf{A}=\Biggl(\begin{smallmatrix}60&2\\40&1\\90&4\\70&3\end{smallmatrix}\Biggr)\in\mathbb{R}^{4\times2}$, $\mathbf{w}\in\mathbb{R}^2$, $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}\in\mathbb{R}^4$. $\mathbf{A}$ matrisinin sütun uzayı, alan sütunu ile oda sütununun bütün $w_1\mathbf{a}_1+w_2\mathbf{a}_2$ bileşimlerinden oluşur; $\mathbb{R}^4$ uzayında orijinden geçen bir düzlemdir. “Çözüm yok” şu demektir: $\mathbf{y}$ fiyat vektörü bu düzlemde değildir. İki ağırlığın hiçbir seçimi tam olarak bu dört fiyatı üretmez.
:::
:::
