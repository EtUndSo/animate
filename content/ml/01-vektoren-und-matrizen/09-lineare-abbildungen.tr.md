---
title: Doğrusal dönüşümler
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Bölüm 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15210900
summary: Bir matris yalnızca bir tablo değil, aynı zamanda bir vektörden başka bir vektör üreten bir hesap kuralıdır.
tags: dönüşüm, doğrusal, dönme, germe, kayma, afin, eksen kesişimi
lang: tr
---

<span class="anker" id="stufe-8"></span>

:::zweck
Bir matris yalnızca bir tablo değil, aynı zamanda bir vektörden başka bir vektör üreten bir hesap kuralıdır. Bu kesim, bu biçimde yazılabilen kuralların tam olarak doğrusal kurallar olduğunu ve bir matrisin uzayı geometrik olarak nasıl değiştirdiğini gösteriyor.
:::

### Doğrusal dönüşümler

<span class="anker" id="stufe-8-1"></span>

Birçok hesap bir sayı listesinden başka bir liste üretir. Bir dairenin özniteliklerinden satış fiyatı ve kirası tahmin edilir; bir su sayacının sayaç değerlerinden her ayın tüketimi elde edilir. Böyle bir $f\colon\mathbb{R}^n\to\mathbb{R}^m$ kuralına __dönüşüm__ denir: Her $\mathbf{x}\in\mathbb{R}^n$ vektörüne bir $f(\mathbf{x})\in\mathbb{R}^m$ vektörü karşılık getirir.

Matris-vektör çarpımının iki özel niteliği vardır (alt kesim [7.1](das-matrix-vektor-produkt.html#stufe-7-1)): $\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ ve $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$. Önce toplamak ya da önce dönüştürmek fark etmez; önce bir sayıyla çarpmak ya da önce dönüştürmek de fark etmez. Düzlemde bu nitelikler bir ızgara üzerinde görülür: Böyle bir dönüşüm doğruları yine doğrulara ya da tek tek noktalara dönüştürür, orijini yerinde bırakır ve paralel, eşit aralıklı ızgara çizgilerini yine paralel, eşit aralıklı çizgilere ya da noktalara dönüştürür.

:::definition Tanım 8.1 (Doğrusal dönüşüm)
<span class="anker" id="satz-8-1"></span>

Bütün $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$ vektörleri ve bütün $c$ skalerleri için şu sağlanıyorsa bir $f\colon\mathbb{R}^n\to\mathbb{R}^m$ dönüşümüne __doğrusal__ denir:

<span class="anker" id="gl-8-1"></span>
$$f(\mathbf{u}+\mathbf{v})=f(\mathbf{u})+f(\mathbf{v})\qquad\text{ve}\qquad f(c\,\mathbf{u})=c\,f(\mathbf{u}) . \tag{8.1}$$
:::

İki koşul birlikte şunu söyler: $f$ doğrusal bileşimleri korur, $f(c_1\mathbf{u}+c_2\mathbf{v})=c_1f(\mathbf{u})+c_2f(\mathbf{v})$. Her doğrusal dönüşüm sıfır vektörünü sıfır vektörüne götürür, çünkü $f(\mathbf{0})=f(0\cdot\mathbf{u})=0\cdot f(\mathbf{u})=\mathbf{0}$.

::::beispiel [Sayısal örnek]
$\mathbb{R}^2$ uzayından $\mathbb{R}^2$ uzayına giden $f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$ dönüşümü doğrusaldır. İki bileşen de $x_j$ bileşenlerinin katlarının toplamıdır ve bu tür toplamlar için [(8.1)](#gl-8-1) koşulları sağlanır; örneğin $f(\mathbf{u}+\mathbf{v})=(u_1+v_1+u_2+v_2,\ 2u_1+2v_1)^{\top}=f(\mathbf{u})+f(\mathbf{v})$ olur. $g(\mathbf{x})=x_1x_2$ ise doğrusal değildir, çünkü $x_1x_2\ne0$ olduğunda $g(2\mathbf{x})=4x_1x_2\ne2\,g(\mathbf{x})$ olur. $h(\mathbf{x})=\mathbf{x}+\mathbf 1$ de doğrusal değildir, çünkü $h(\mathbf{0})=\mathbf 1\ne\mathbf{0}$.
::::

⁠**Kısacası:** Bir dönüşüm toplamları ve katları koruyorsa doğrusaldır; o zaman doğrusal bileşimleri doğrusal bileşimlere götürür.

:::hintergrund Süpermarket kasasında doğrusallık
Bir süpermarketin kasası doğrusal hesap yapar. Satın alınan miktarların listesinden ödenecek tutarı çıkarır; iki alışveriş birlikte banda konursa iki tutarın toplamı ödenir; her şeyden iki kat alınırsa iki katı ödenir. Bunlar tam olarak [(8.1)](#gl-8-1) koşullarıdır. Miktar indirimli bir tarife, yani iki katın iki kat fiyattan daha ucuza geldiği bir tarife doğrusal olmazdı; sabit ücretli bir tarife de doğrusal olmazdı: Orada boş bir alışveriş bile bir şeye mal olur ve bu, $f(\mathbf{0})=\mathbf{0}$ koşulunu bozar. Bir ses kaydı da (alt kesim [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3)) çoğu zaman doğrusal biçimde işlenir: İki kaydı önce karıştırıp sonra sesini alçaltan kişi, her birinin sesini ayrı ayrı alçaltıp sonra karıştıran kişiyle aynı sonucu elde eder.
:::

### Her doğrusal dönüşüm bir matristir

<span class="anker" id="stufe-8-2"></span>

Her matris bir $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ doğrusal dönüşümü verir. Tersi de doğru mudur? Evet, ve nedeni basittir: Her vektör birim vektörlerin bir doğrusal bileşimidir ve doğrusal bir dönüşüm doğrusal bileşimleri korur. Bu yüzden $n$ birim vektörün nereye gittiğini bilen, her vektörün nereye gittiğini de bilir.

:::satz Teorem 8.2 (Bir doğrusal dönüşümün matrisi)
<span class="anker" id="satz-8-2"></span>

Her $f\colon\mathbb{R}^n\to\mathbb{R}^m$ doğrusal dönüşümü için bütün $\mathbf{x}\in\mathbb{R}^n$ vektörlerinde $f(\mathbf{x})=\mathbf{A}\mathbf{x}$ olan tam olarak bir $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisi vardır. Bu matrisin sütunları birim vektörlerin görüntüleridir:

<span class="anker" id="gl-8-2"></span>
$$\mathbf{a}_j=f(\mathbf{e}_j),\qquad j=1,\dots,n . \tag{8.2}$$
:::

:::beweis Bir doğrusal dönüşümün matrisi
[(1.6)](vektoren-daten-als-zahlenlisten.html#gl-1-6) uyarınca $\mathbf{x}=\sum_jx_j\mathbf{e}_j$ olur. $f$ doğrusal olduğundan şu çıkar:

$$f(\mathbf{x})=f\Bigl(\sum_{j=1}^nx_j\mathbf{e}_j\Bigr)=\sum_{j=1}^nx_j\,f(\mathbf{e}_j)=\sum_{j=1}^nx_j\,\mathbf{a}_j=\mathbf{A}\mathbf{x} ,$$

burada son adım [(7.3)](das-matrix-vektor-produkt.html#gl-7-3) sütun bakışından gelir. Bütün $\mathbf{x}$ vektörleri için $\mathbf{B}\mathbf{x}=f(\mathbf{x})$ eşitliğini sağlayan ikinci bir $\mathbf{B}$ matrisi olsaydı, $\mathbf{x}=\mathbf{e}_j$ alındığında $\mathbf{B}$ matrisinin $j$ numaralı sütunu her $j$ için $f(\mathbf{e}_j)=\mathbf{a}_j$ olurdu. Demek ki $\mathbf{B}=\mathbf{A}$.
:::

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$ için $f(\mathbf{e}_1)=(1,\,2)^{\top}$ ve $f(\mathbf{e}_2)=(1,\,0)^{\top}$ olur. Demek ki

$$\mathbf{A}=\begin{pmatrix}1&1\\2&0\end{pmatrix},\qquad\text{ve kontrol için}\qquad \mathbf{A}\begin{pmatrix}3\\-1\end{pmatrix}=\begin{pmatrix}2\\6\end{pmatrix}=f\bigl((3,\,-1)^{\top}\bigr).$$
::::

⁠**Kısacası:** Doğrusal dönüşümler ile matrisler aynı şeydir; matrisin $j$ numaralı sütunu $\mathbf{e}_j$ birim vektörünün görüntüsüdür.

:::hintergrund Matris olarak bir artçı etki: Sütunlar kaydırılmış yanıtlardır
Bir odun sobasında bir odun, yandığı saat içinde ısısının tamamını, sonraki saatte ise kor sayesinde yarısını daha verir; bu, büyük ölçüde basitleştirilmiş bir resimdir. $n$ numaralı saatte tam olarak $x[n]$ odun eklenirse bu saatteki ısı, odun cinsinden ölçülürse, $y[n]=x[n]+0{,}5\,x[n-1]$ olur. Üç saat ele alınıyor; ilk saatten önce hiçbir şey yanmıyordu. Bu hesap doğrusaldır, dolayısıyla bir matrisi vardır. [(8.2)](#gl-8-2) uyarınca bu matrisin $j$ numaralı sütunu, $\mathbf{e}_j$ birim vektörüne, yani $j$ numaralı saatteki tek bir oduna verilen yanıttır. Bu yanıt, $j-1$ saat kaydırılmış $(1;\,0{,}5)$ yanıtıdır:

$$\mathbf{A}=\begin{pmatrix}1&0&0\\0{,}5&1&0\\0&0{,}5&1\end{pmatrix}.$$

Üçüncü sütunda yalnızca $1$ kalır, çünkü ele alınan süre üç saatten sonra biter. $\mathbf{x}=(2,\,4,\,6)^{\top}$ için matris $(2,\,5,\,8)^{\top}$ verir; formül de aynısını verir. Matematikte evrişim adı verilen, sabit ağırlıklı her böyle artçı etki bu şekilde bir matris-vektör çarpımıdır ve yukarıdaki teorem bunun nedenini açıklar: Tek tek her oduna verilen yanıt bilinirse her odun dizisine verilen yanıt da bilinir.
:::

:::hintergrund Veri mi, dönüşüm mü? Aynı tablonun iki rolü
Bir matris, $\mathbf{X}$ veri matrisi gibi bir veri topluluğu ya da bir önceki kutudaki odun sobasının matrisi gibi bir dönüşüm olabilir. Biçimsel olarak ikisi aynı şeydir ve bazen aynı matris iki rolü birden üstlenir: Veri matrisi aynı zamanda ağırlıklardan tahminler üreten $\mathbf{w}\mapsto\mathbf{X}\mathbf{w}$ dönüşümüdür. Ağırlıkların $\mathbb{R}^d$ uzayını tahmin listelerinin $\mathbb{R}^N$ uzayına götürür. Bu yüzden bir formül okunurken bir matrisin o anda hangi rolde ortaya çıktığını sormak işe yarar.
:::

### Düzlemin doğrusal dönüşümleri

<span class="anker" id="stufe-8-3"></span>

Düzlemde bir matrisin ne yaptığı görülebilir. Köşeleri $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_1+\mathbf{e}_2$ ve $\mathbf{e}_2$ olan birim kare ve onun görüntüsü çizilir. Dönüşüm doğrusal bileşimleri koruduğu için kare, köşeleri $\mathbf{0}$, $\mathbf{a}_1$, $\mathbf{a}_1+\mathbf{a}_2$ ve $\mathbf{a}_2$ olan paralelkenara dönüşür. Bu paralelkenarın orijindeki iki kenarı matrisin sütunlarıdır (Şekil [32](#abb-32)). Düzlemin bütün ızgarası da aynı biçimde şekil değiştirir: Her küçük kare bu paralelkenarın kaydırılmış bir kopyasına dönüşür.

:::abbildung ml/k1ebene 32
Düzlemin dört doğrusal dönüşümü. Gri kesikli çizgiyle birim kare, mavi ile onun görüntüsü. Kırmızı ok $\mathbf{e}_1$ vektörünün $\mathbf{a}_1$ görüntüsü, yeşil ok $\mathbf{e}_2$ vektörünün $\mathbf{a}_2$ görüntüsüdür; bunlar matrisin iki sütunudur. Yassılaştırmada $\mathbf{a}_2=\mathbf{0}$ olur ve kare, $\mathbf{0}$ ile $\mathbf{e}_1$ arasındaki doğru parçasına dönüşür.
:::

<ul>

<li>

Saat yönünün tersine $90^\circ$ kadar __dönme__, $\mathbf{e}_1$ vektörünü $(0,\,1)^{\top}$ vektörüne, $\mathbf{e}_2$ vektörünü $(-1,\,0)^{\top}$ vektörüne götürür; bunlar matrisin sütunlarıdır.

</li>

<li>

$\operatorname{diag}(2;\,0{,}5)$ ile verilen __germe__, düzlemi yatay doğrultuda iki katına çeker ve dikey doğrultuda yarıya sıkıştırır.

</li>

<li>

$\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ ile verilen __kayma__, $\mathbf{e}_1$ vektörünü yerinde bırakır ve $\mathbf{e}_2$ vektörünü sağa iter: Her nokta, yüksekliği kadar sağa kaydırılır.

</li>

<li>

$\operatorname{diag}(1;\,0)$ matrisi birinci bileşeni korur ve ikincisini sıfır yapar. Bütün düzlemi $x_1$ ekseni üzerine yassılaştırır.

</li>

</ul>

::::beispiel [Sayısal örnek] herhangi bir açı kadar dönme
Saat yönünün tersine $\alpha$ açısı kadar döndürüldüğünde $\mathbf{e}_1$ vektörü birim çember üzerindeki $(\cos\alpha,\,\sin\alpha)^{\top}$ noktasına, ondan $90^\circ$ ileride bulunan $\mathbf{e}_2$ vektörü ise $(-\sin\alpha,\,\cos\alpha)^{\top}$ noktasına gelir. Bu yüzden [(8.2)](#gl-8-2) uyarınca dönme matrisi şudur:

<span class="anker" id="gl-8-3"></span>
$$\mathbf R_\alpha=\begin{pmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{pmatrix}. \tag{8.3}$$

$\alpha=90^\circ$ için yukarıdaki dönme matrisi çıkar (Şekil [32](#abb-32)). Bu matris $(1,\,1)^{\top}$ noktasını $(-1,\,1)^{\top}$ noktasına döndürür; germe onu $(2;\ 0{,}5)^{\top}$ noktasına, kayma $(2,\,1)^{\top}$ noktasına, yassılaştırma da $(1,\,0)^{\top}$ noktasına götürür.
::::

⁠**Kısacası:** $2\times2$ tipinde bir matris düzlemin ızgarasının biçimini değiştirir; birim kare, matrisin iki sütununun gerdiği paralelkenara dönüşür.

### Tek çıkışlı doğrusal fonksiyonlar

<span class="anker" id="stufe-8-4"></span>

Bir örneğin özniteliklerinden tek bir sayı üreten bir model, $\mathbb{R}^d$ uzayından $\mathbb{R}$ kümesine giden bir dönüşümdür. Bu dönüşüm doğrusalsa matrisi, $d$ elemanlı tek bir satırdır (alt kesim [8.2](#stufe-8-2) içindeki teorem).

:::satz Teorem 8.3 (Doğrusal fonksiyonlar ağırlıklı toplamlardır)
<span class="anker" id="satz-8-3"></span>

Her $f\colon\mathbb{R}^d\to\mathbb{R}$ doğrusal dönüşümü, $w_j=f(\mathbf{e}_j)$ ağırlıklarıyla $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}$ biçimindedir.
:::

Bu, $m=1$ için alt kesim [8.2](#stufe-8-2) içindeki teoremdir: $1\times d$ tipindeki matris $\mathbf{w}^{\top}$ satırıdır ve bu satırın $\mathbf{x}$ ile çarpımı iç çarpımdır. Demek ki ağırlıklı toplam (alt kesim [2.2](das-skalarprodukt.html#stufe-2-2)) sıradan bir özel durum değil, tek çıkışlı en genel doğrusal kuraldır.

::::beispiel [Sayısal örnek]
Emlakçının kuralı $f(\mathbf{x})=3x_1+10x_2-4x_3$ olur. $f(\mathbf{e}_1)=3$, $f(\mathbf{e}_2)=10$, $f(\mathbf{e}_3)=-4$, dolayısıyla $\mathbf{w}=(3,\,10,\,-4)^{\top}$ bulunur. $w_j=f(\mathbf{e}_j)$ ağırlığı, kuralın, $j$ özniteliğinden yalnızca bir birimi olan ve başka hiçbir şeyi olmayan hayalî bir örnek için verdiği değerdir: Bu özniteliğin bir biriminin ne kadar katkı yaptığını söyler.
::::

⁠**Kısacası:** Tek çıkışlı her doğrusal dönüşüm bir $\mathbf{w}^{\top}\mathbf{x}$ ağırlıklı toplamıdır ve $w_j$ ağırlığı, dönüşümün $\mathbf{e}_j$ noktasındaki değeridir.

### Afin dönüşümler

<span class="anker" id="stufe-8-5"></span>

Emlakçı, tahminlerinin hep çok düşük kaldığını fark eder. Bu yüzden her ağırlıklı toplama $20$ bin avroluk bir taban tutar ekler. Bu yeni kural artık doğrusal değildir: Hayalî bir $\mathbf{x}=\mathbf{0}$ dairesine $0$ değil, $20$ değerini karşılık getirir. Bu kural, ardından bir kaydırma gelen bir doğrusal dönüşümdür.

:::definition Tanım 8.4 (Afin dönüşüm)
<span class="anker" id="satz-8-4"></span>

Bir $f\colon\mathbb{R}^n\to\mathbb{R}^m$ dönüşümü, bir $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisi ve sabit bir $\mathbf{b}\in\mathbb{R}^m$ vektörüyle

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b} \tag{8.4}$$

biçiminde yazılabiliyorsa bu dönüşüme __afin__ denir. Tek bir çıkış ($m=1$) için $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}+b$ yazılır ve $b$ sayısına __eksen kesişimi__ (sabit terim) denir.
:::

$\mathbf{b}\ne\mathbf{0}$ için afin bir dönüşüm doğrusal değildir, çünkü $f(\mathbf{0})=\mathbf{b}\ne\mathbf{0}$. Izgara resminde düzlem önce biçim değiştirir, sonra bir bütün olarak $\mathbf{b}$ kadar kaydırılır; orijin $\mathbf{b}$ noktasına gelir. Gündelik dilde afin kurallara da çoğu zaman “doğrusal” denir. Bu seride yalnızca $\mathbf{b}=\mathbf{0}$ olan bir dönüşüme doğrusal denir.

Bütün örnekler için afin tahmin, $\mathbf 1\in\mathbb{R}^N$ birler vektörüyle aynı anda şöyle yazılır:

<span class="anker" id="gl-8-5"></span>
$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+b\,\mathbf 1 . \tag{8.5}$$

$b\,\mathbf 1$ terimi her tahmine aynı $b$ tutarını ekler.

::::beispiel [Sayısal örnek]
$\mathbf{w}=(3,\,10,\,-4)^{\top}$ ve $b=20$ ile $(188,\,126,\,286,\,232)^{\top}$ tahminleri şu tahminlere dönüşür:

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+20\cdot\mathbf 1=(208,\,146,\,306,\,252)^{\top}\ \text{bin avro}.$$
::::

⁠**Kısacası:** Afin bir dönüşüm, bir doğrusal dönüşüm artı sabit bir kaydırmadır, $\mathbf{A}\mathbf{x}+\mathbf{b}$; tek çıkışta bu kaydırmaya eksen kesişimi denir.

:::hintergrund Sona eklenen 1 hilesi
Her örneğe sabit değeri $1$ olan bir bileşen eklenirse afin bir fonksiyon doğrusal bir fonksiyon olarak yazılabilir:

$$\mathbf{w}^{\top}\mathbf{x}+b=\begin{pmatrix}w_1&\cdots&w_d&b\end{pmatrix}\begin{pmatrix}x_1\\\vdots\\x_d\\1\end{pmatrix}.$$

Böylece eksen kesişimi, değeri her zaman $1$ olan bir özniteliğin ağırlığına dönüşür. Bütün veri kümesi için veri matrisine bir birler sütunu eklenir: $\begin{pmatrix}\mathbf{X}&\mathbf 1\end{pmatrix}\begin{pmatrix}\mathbf{w}\\b\end{pmatrix}=\mathbf{X}\mathbf{w}+b\,\mathbf 1$. Daireler için genişletilmiş veri matrisinin satırları $(60,2,3,1)$, $(40,1,1,1)$, $(90,4,6,1)$, $(70,3,2,1)$ olur ve $(3,\,10,\,-4,\,20)^{\top}$ vektörüyle yine $(208,\,146,\,306,\,252)^{\top}$ çıkar. Bu hile sayesinde afin kurallar için ayrı bir kurama gerek kalmaz: Doğrusal dönüşümler için geçerli olan her şey, boyutu bir fazla olan uzayda afin kurallar için de geçerlidir.
:::

:::aufgabe Alıştırma 18 ★ Doğrusal mı, değil mi?
<span class="anker" id="aufg-18"></span>

Aşağıdaki dönüşümlerden hangilerinin doğrusal olduğunu kontrol edin ve doğrusal olanların matrisini verin:

$$\begin{gathered} f_1(\mathbf{x})=(2x_1,\ x_1-x_2)^{\top},\qquad f_2(\mathbf{x})=x_1^2,\qquad f_3(\mathbf{x})=(x_2,\ x_1)^{\top},\\ f_4(x)=2x+3,\qquad f_5(\mathbf{x})=(0,\ 0)^{\top} \end{gathered}$$

Burada $\mathbf{x}\in\mathbb{R}^2$, $f_4$ için ise $x\in\mathbb{R}$ olsun.

:::loesung
<ul>

<li>

$f_1$ doğrusaldır; iki bileşen de $x_j$ değişkenlerinin katlarının toplamıdır. Sütunlar $f_1(\mathbf{e}_1)=(2,\,1)^{\top}$ ve $f_1(\mathbf{e}_2)=(0,\,-1)^{\top}$, dolayısıyla matris $\bigl(\begin{smallmatrix}2&0\\1&-1\end{smallmatrix}\bigr)$ olur.

</li>

<li>

$f_2$ doğrusal değildir: $x_1\ne0$ olduğu anda $f_2(2\mathbf{x})=4x_1^2\ne2f_2(\mathbf{x})$.

</li>

<li>

$f_3$ doğrusaldır, matrisi $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ olur; bileşenlerin yerini değiştirir.

</li>

<li>

$f_4$ doğrusal değildir, çünkü $f_4(0)=3\ne0$. Afindir, eksen kesişimi $3$ olur.

</li>

<li>

$f_5$ doğrusaldır, matrisi sıfır matristir; iki koşul da $\mathbf{0}+\mathbf{0}=\mathbf{0}$ ve $c\,\mathbf{0}=\mathbf{0}$ olduğu için sağlanır.

</li>

</ul>
:::
:::

:::aufgabe Alıştırma 19 ★★ Birim vektörlerin görüntülerinden matrisler
<span class="anker" id="aufg-19"></span>

<ol class="al">

<li>

$30^\circ$ kadar dönmenin matrisini verin ve $(2,\,0)^{\top}$ vektörünün görüntüsünü hesaplayın.

</li>

<li>

$x_1=x_2$ açıortayına göre yansıma iki bileşenin yerini değiştirir. Bu yansımanın matrisini ve $(3,\,1)^{\top}$ vektörünün görüntüsünü verin.

</li>

<li>

Doğrusal bir dönüşüm $f\bigl((1,\,1)^{\top}\bigr)=(1,\,4)^{\top}$ ve $f\bigl((2,\,-1)^{\top}\bigr)=(5,\,-1)^{\top}$ koşullarını sağlıyor. Matrisini bulun. İpucu: İki koşulu $\mathbf{a}_1,\mathbf{a}_2$ sütunlarıyla yazın.

</li>

</ol>

:::loesung
(a) $\cos30^\circ=\sqrt3/2\approx0{,}866$ ve $\sin30^\circ=\tfrac12$ ile [(8.3)](#gl-8-3) uyarınca:

$$\mathbf R_{30^\circ}=\begin{pmatrix}0{,}866&-0{,}5\\0{,}5&0{,}866\end{pmatrix},\qquad \mathbf R_{30^\circ}\begin{pmatrix}2\\0\end{pmatrix}=\begin{pmatrix}\sqrt3\\1\end{pmatrix}\approx\begin{pmatrix}1{,}732\\1\end{pmatrix}.$$

Görüntü birinci sütunun iki katıdır: $30^\circ$ doğrultusundaki, uzunluğu $2$ olan bir ok.

(b) $\mathbf{e}_1$ vektörü $\mathbf{e}_2$ vektörüne, $\mathbf{e}_2$ de $\mathbf{e}_1$ vektörüne gider; dolayısıyla matris $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ olur ve $(3,\,1)^{\top}$ vektörü $(1,\,3)^{\top}$ vektörüne gider.

(c) Doğrusallık nedeniyle $f\bigl((1,1)^{\top}\bigr)=\mathbf{a}_1+\mathbf{a}_2=(1,\,4)^{\top}$ ve $f\bigl((2,-1)^{\top}\bigr)=2\mathbf{a}_1-\mathbf{a}_2=(5,\,-1)^{\top}$ olur. İki denklem toplanınca $3\mathbf{a}_1=(6,\,3)^{\top}$ çıkar; dolayısıyla $\mathbf{a}_1=(2,\,1)^{\top}$ ve $\mathbf{a}_2=(1,4)^{\top}-(2,1)^{\top}=(-1,\,3)^{\top}$. Matris $\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)$ olur. Sağlama: $\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)(2,\,-1)^{\top}=(5,\,-1)^{\top}$.
:::
:::

:::aufgabe Alıştırma 20 ★★ Matris olarak sayaç değerlerinden tüketim
<span class="anker" id="aufg-20"></span>

Yeni bir su sayacı dört ayın sonunda metreküp cinsinden $x[1],\dots,x[4]$ sayaç değerlerini gösteriyor; ilk aydan önce $x[0]=0$ değerindeydi. $n$ numaralı aydaki tüketim $y[n]=x[n]-x[n-1]$ farkıdır, $n=1,\dots,4$.

<ol class="al">

<li>

Bu hesap neden doğrusaldır? Dört birim vektöre verilen yanıtları hesaplayarak hesabın $4\times4$ tipindeki matrisini kurun.

</li>

<li>

$\mathbf{x}=(1,\,2,\,4,\,7)^{\top}$ sayaç değerlerine karşılık gelen tüketimi matrisle ve formülle hesaplayın.

</li>

</ol>

:::loesung
(a) Sonucun her $y[n]=x[n]-x[n-1]$ bileşeni, $\mathbf{x}$ bileşenlerinin katlarının sabit bir toplamıdır; dolayısıyla hesap doğrusaldır. $1$ konumundaki tek $1$ değerine, yani $\mathbf{x}=\mathbf{e}_1=(1,0,0,0)^{\top}$ vektörüne verilen yanıt $(1,\,-1,\,0,\,0)^{\top}$ olur: Sayaç değeri önce $1$ değerine çıkar, sonra yeniden $0$ değerine iner. Aynı biçimde hesap $\mathbf{e}_2$ vektörüne $(0,\,1,\,-1,\,0)^{\top}$, $\mathbf{e}_3$ vektörüne $(0,\,0,\,1,\,-1)^{\top}$, $\mathbf{e}_4$ vektörüne de $(0,\,0,\,0,\,1)^{\top}$ yanıtını verir; bu son $1$ değerinde dört ay, sayaç değeri yeniden düşmeden önce biter. Bu yanıtlar matrisin sütunlarıdır:

$$\mathbf{A}=\begin{pmatrix}1&0&0&0\\-1&1&0&0\\0&-1&1&0\\0&0&-1&1\end{pmatrix}.$$

(b) Matrisle: $\mathbf{A}\,(1,2,4,7)^{\top}=(1,\ -1+2,\ -2+4,\ -4+7)^{\top}=(1,\,1,\,2,\,3)^{\top}$. Formülle: $y[1]=1-0=1$, $y[2]=2-1=1$, $y[3]=4-2=2$, $y[4]=7-4=3$. Demek ki dört ayda sırasıyla $1$, $1$, $2$ ve $3$ metreküp su tüketilmiştir.
:::
:::
