---
title: Otomatik türev alma
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15231100
summary: Hesaplama grafiğiyle türevler, formülleri dönüştürmeden ve temel işlemlerin yuvarlaması dışında tam olarak, mekanik biçimde hesaplanabilir.
tags: Otomatik türev alma, İleri mod, teğet değeri, eşleniği, Ters mod
lang: tr
---

<span class="anker" id="stufe-10"></span>

:::zweck
Hesaplama grafiğiyle türevler, formülleri dönüştürmeden ve temel işlemlerin yuvarlaması dışında tam olarak, mekanik biçimde hesaplanabilir. Buna otomatik türev alma denir. Yerel türevleri birleştirmenin iki yolu vardır: ileri doğru, hesapla aynı adımda, ya da geriye doğru, sonuçtan girdilere. Ters mod bir sayının bütün girdilerine göre türevini tek bir geçişte verir ve bu kesim bunun neden bu kadar az maliyetli olduğunu gösteriyor.
:::

### Otomatik türev alma nedir

<span class="anker" id="stufe-10-1"></span>

Bir hesabın türevini elde etmenin üç yolu vardır. Formül kurallarla dönüştürülebilir; buna sembolik türev alma denir ve Kesim [9.1](rechengraphen.html#stufe-9-1)'e göre formüller bu sırada çabucak büyür. Fonksiyon birbirine yakın iki noktada hesaplanıp bir fark bölümü oluşturulabilir; buna sayısal türev alma denir, yalnızca yaklaşık olarak doğrudur ve Kesim [11](numerische-ableitung-und-gradientenprufung.html#stufe-11) onun hatasını inceler. Üçüncü yol, diğer ikisinin üstünlüklerini birleştirir.

:::definition Tanım 10.1 (Otomatik türev alma)
<span class="anker" id="satz-10-1"></span>

__Otomatik türev alma__, bir hesabın türevlerini, zincir kuralını onun hesaplama grafiğine uygulayarak hesaplar: Yerel türevleri hesabın sayılarıyla hesaplar ve onları yollar üzerinden toplama göre birleştirir.
:::

Otomatik türev alma formüllerle değil, sayılarla hesap yapar ve bu yüzden hiçbir ifade şişmez. Hiçbir şeyi yaklaşık olarak hesaplamaz: Sonuç tam türevdir, yalnızca tek tek hesap adımlarının yuvarlamasıyla bozulur. Ve temel işlemlerden oluşan her program için, döngüler ve dallanmalar içerse bile çalışır, çünkü program verilen girdiler için bir hesaplama grafiği verir. Kesim [9.1](rechengraphen.html#stufe-9-1)'deki örnekte yapılan adım adım hesap zaten otomatik türev almaydı.

::::beispiel [Sayısal örnek]
[(9.1)](rechengraphen.html#gl-9-1) için önceki kesim $5$, $8$ ve $3$ türevlerini, $f$ formülünü açmadan ya da türevini almadan, yerel türevlerden bir araya getirdi. Bu, hesabın sırası için henüz sabit bir yöntem olmasa da otomatik türev almaydı. Sonraki iki alt kesim bu sırayı veriyor.
::::

⁠**Kısacası:** Otomatik türev alma zincir kuralını sayılarla hesaplama grafiğine uygular; yuvarlama dışında tamdır ve formüle ihtiyaç duymaz.

### İleri mod

<span class="anker" id="stufe-10-2"></span>

Birinci olanak hesabın kendisini izler. Girdilerin hangi doğrultuda değiştirileceği belirlenir ve her düğümde, değerinin yanında, bu değişimde düğümün ne kadar hızlı değiştiği de taşınır.

:::definition Tanım 10.2 (İleri mod)
<span class="anker" id="satz-10-2"></span>

__İleri mod__da girdiler için bir $\dot{\mathbf{x}}\in\mathbb{R}^n$ doğrultusu seçilir ve her $b$ düğümü için değerinin yanında

<span class="anker" id="gl-10-1"></span>
$$\dot b=\sum_{a\text{: }b\text{'nin öncülü}}\frac{\partial b}{\partial a}\,\dot a , \tag{10.1}$$

sayısı, değerlerle aynı sırayla hesaplanır. Bu sayıya $b$'nin __teğet değeri__ denir; girdi düğümleri teğet değerleri olarak $\dot{\mathbf{x}}$ vektörünün bileşenlerini alır.
:::

Ad, Kesim [1.2](die-ableitung.html#stufe-1-2)'deki teğeti hatırlatır, ama bir sayıdır: $\dot b$ teğet değeri, girdiler $\mathbf{x}+t\,\dot{\mathbf{x}}$ doğrusu boyunca kaydırıldığında $b$ düğümünün değişim hızıdır. [(10.1)](#gl-10-1) formülü, bu eğri boyunca zincir kuralının, yani [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4) bağıntısının tek bir düğüm için yazılmış hâlidir. Bir geçişten sonra sonuçta $\dot f=\nabla f(\mathbf{x})^{\top}\dot{\mathbf{x}}$ durur. Hesabın birden çok çıktısı varsa orada Jacobi matrisi ile doğrultunun $\mathbf{J}\,\dot{\mathbf{x}}$ çarpımı durur. $\dot{\mathbf{x}}=\mathbf{e}_j$ ile bir geçiş $x_j$'ye göre kısmi türevi, birden çok çıktıda Jacobi matrisinin $j$ sütununu verir. $n$ değişkenli bir fonksiyonun gradyanının tamamı için ileri mod dolayısıyla $n$ geçiş gerektirir.

::::beispiel [Sayısal örnek]
[(9.1)](rechengraphen.html#gl-9-1) için $(1,\,2,\,3)$ noktasında $\dot{\mathbf{x}}=\mathbf{e}_2=(0,\,1,\,0)^{\top}$ doğrultusuyla Tablo [5](#tab-5) ortaya çıkar. Sonuçta $\dot f=8=\partial f/\partial x_2$ durur. $\partial f/\partial x_1$ ve $\partial f/\partial x_3$ için $\mathbf{e}_1$ ve $\mathbf{e}_3$ ile iki geçiş daha gerekir.

<span class="anker" id="tab-5"></span>

**Tablo 5:** $(1,\,2,\,3)$ noktasında $\dot{\mathbf{x}}=\mathbf{e}_2$ doğrultusunda $f=(x_1+x_2)\,(x_2+x_3)$ için ileri mod.

| Düğüm | Hesap | Değer | Teğet değeri |  |
|---|---|---|---|---|
| $x_1$ | girdi | $1$ | $\dot x_1$ | $0$ |
| $x_2$ | girdi | $2$ | $\dot x_2$ | $1$ |
| $x_3$ | girdi | $3$ | $\dot x_3$ | $0$ |
| $v_1$ | $x_1+x_2$ | $3$ | $\dot v_1=\dot x_1+\dot x_2$ | $1$ |
| $v_2$ | $x_2+x_3$ | $5$ | $\dot v_2=\dot x_2+\dot x_3$ | $1$ |
| $f$ | $v_1\cdot v_2$ | $15$ | $\dot f=v_2\,\dot v_1+v_1\,\dot v_2$ | $5+3=8$ |
::::

⁠**Kısacası:** İleri mod her değerle birlikte onun teğet değerini taşır; bir geçiş bir doğrultudaki türevi, yani Jacobi matrisinin bir sütununu verir.

:::hintergrund Dual sayılarla ileri mod
İleri mod, genişletilmiş sayılarla hesap yapmak olarak da görülebilir. $\varepsilon$, tek kuralı $\varepsilon^2=0$ olan yeni bir sembol olmak üzere $a+\dot a\,\varepsilon$ çiftleriyle hesap yapılır; böyle sayılara dual sayılar denir. Toplama ve çarpma alışıldığı gibi yapılır: $(a+\dot a\varepsilon)+(b+\dot b\varepsilon)=(a+b)+(\dot a+\dot b)\varepsilon$ ve $(a+\dot a\varepsilon)(b+\dot b\varepsilon)=ab+(a\dot b+\dot ab)\varepsilon$, çünkü $\dot a\dot b\varepsilon^2$ terimi düşer. Demek ki $\varepsilon$ önündeki çarpan tam olarak toplam ve çarpım kuralını izler. [(9.1)](rechengraphen.html#gl-9-1) için $x_1=1$, $x_2=2+\varepsilon$, $x_3=3$ konur ve $(3+\varepsilon)(5+\varepsilon)=15+8\varepsilon+\varepsilon^2=15+8\varepsilon$ elde edilir: Değer ve $x_2$'ye göre türev tek bir hesapta. Tek değişkenli bir $\varphi$ fonksiyonu için $\varphi(a+\dot a\varepsilon)=\varphi(a)+\varphi'(a)\,\dot a\,\varepsilon$ konur; bu, küçük terimin karesinin rol oynamadığı doğrusal yaklaşıma karşılık gelir. Dual sayıları William Kingdon Clifford 1873'te, herhangi bir bilgisayardan çok önce tanıtmıştır.
:::

### Ters mod

<span class="anker" id="stufe-10-3"></span>

İleri mod bir girdi için her düğümün ona ne kadar güçlü bağlı olduğunu sorar. Ters mod tersi soruyu sorar: Sonuç her düğüme ne kadar güçlü bağlıdır? Bu soru sonuçtan başlayarak geriye doğru cevaplanabilir ve sonunda cevap bütün girdiler için aynı anda bilinir.

:::definition Tanım 10.3 (Ters mod)
<span class="anker" id="satz-10-3"></span>

Bir $a$ düğümünün __eşleniği__ (adjoint) $\bar a=\partial f/\partial a$, yani düğüm hesabın geri kalanının bir girdisi olarak görüldüğünde sonucun bu düğüme göre türevidir. __Ters mod__da önce ileri hesaplama yapılır ve bütün değerler saklanır. Sonra $\bar f=1$ konur ve düğümler ters sırayla hesaplanır:

<span class="anker" id="gl-10-2"></span>
$$\bar a=\sum_{b\text{: }a\text{'nın ardılı}}\bar b\,\frac{\partial b}{\partial a}. \tag{10.2}$$

Girdi düğümlerinin eşlenikleri $\nabla f(\mathbf{x})$ gradyanını oluşturur.
:::

Ters sıra gereklidir, çünkü her düğüm ardıllarının eşleniklerine ihtiyaç duyar ve ardıllar hesapta ondan sonra gelir. Her eşlenik kendi düğümüyle aynı şekle sahiptir; bir düğüm bir vektör ya da bir matrisse eşleniği de bir vektör ya da bir matristir, Kesim [7.6](ableiten-nach-vektoren-und-matrizen.html#stufe-7-6)'daki matris çarpımının geri kuralında olduğu gibi.

:::satz Teorem 10.4 (Ters mod gradyanı verir)
<span class="anker" id="satz-10-4"></span>

Her $a$ düğümü için [(10.2)](#gl-10-2) uyarınca hesaplanan $\bar a$ sayısı, $a$'dan sonuca giden bütün yollar üzerinden toplamdır; her yol boyunca yerel türevler çarpılır. Girdi düğümleri için bu, Kesim [9.4](rechengraphen.html#stufe-9-4)'e göre $f$ fonksiyonunun kısmi türevidir.
:::

:::beweis Ters mod gradyanı verir
$a$'dan sonuca giden bütün yollar ilk kenarlarına göre gruplanır. Her yol bir $b$ ardılına giden bir kenarla başlar ve sonra $b$'den sonuca giden bir yol olarak devam eder. Bu yüzden $b$ üzerinden geçen yollar birlikte $\frac{\partial b}{\partial a}$ çarpı $b$'den sonuca giden bütün yollar üzerinden toplam kadar katkıda bulunur. Bu toplam bütün ardıllar için zaten doğru hesaplanmışsa, yani $\bar b$'ye eşitse, $a$ için toplam tam olarak [(10.2)](#gl-10-2) olur. Sonucun kendisi için önerme, boş yola karşılık gelen $\bar f=1$ ile doğrudur. Geriye doğru hesaplandığından ardıllar her zaman $a$'dan önce sıraya gelir ve önerme düğüm düğüm girdilere kadar aktarılır.
:::

::::beispiel [Sayısal örnek]
[(9.1)](rechengraphen.html#gl-9-1) için $(1,\,2,\,3)$ noktasında Tablo [6](#tab-6) ve Şekil [19](#abb-19) ortaya çıkar. Tek bir geri geçiş, ileri modun ancak üç geçişle elde ettiği $(5,\,8,\,3)$ kısmi türevlerinin üçünü birden verir.

<span class="anker" id="tab-6"></span>

**Tablo 6:** $(1,\,2,\,3)$ noktasında $f=(x_1+x_2)\,(x_2+x_3)$ için ters mod; değerler Tablo [3](rechengraphen.html#tab-3) içinden alınmıştır.

| Düğüm | [(10.2)](#gl-10-2) uyarınca hesap | Eşlenik |
|---|---|---|
| $f$ | başlangıç | $\bar f=1$ |
| $v_2$ | $\bar f\cdot\partial f/\partial v_2=1\cdot v_1$ | $\bar v_2=3$ |
| $v_1$ | $\bar f\cdot\partial f/\partial v_1=1\cdot v_2$ | $\bar v_1=5$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=3$ |
| $x_2$ | $\bar v_1\cdot1+\bar v_2\cdot1$ | $\bar x_2=5+3=8$ |
| $x_1$ | $\bar v_1\cdot1$ | $\bar x_1=5$ |

:::abbildung ml/k3rueckwaerts 19
$(1,\,2,\,3)$ noktasında $f=(x_1+x_2)\,(x_2+x_3)$ hesaplama grafiğinde ileri ve geri değerler: yeşille ileri hesaplamanın değerleri, kırmızıyla eşlenikler, kenarlarda griyle yerel türevler. Geriye doğru hesaplanırken her eşlenik ok yönünün tersine ilerler ve kenarın yerel türeviyle çarpılır; $x_2$'de olduğu gibi bir düğümden iki kenar çıkıyorsa katkılar toplanır.
:::
::::

⁠**Kısacası:** Ters mod önce ileri hesaplar ve bütün değerleri saklar, sonra geriye doğru $\bar a=\sum\bar b\,\partial b/\partial a$ eşleniklerini hesaplar; bir geri geçiş gradyanın tamamını verir.

### Geri akıştaki kalıplar

<span class="anker" id="stufe-10-4"></span>

Tablo [4](rechengraphen.html#tab-4) uyarınca temel işlemler geriye doğru hesapta basit, tekrar eden biçimlerde davranır. Bu kalıpları bilen kişi eşlenikleri neredeyse hiç hesap yapmadan yazabilir ve türetmelerdeki hataları hızla fark edebilir.

:::satz Teorem 10.5 (Temel işlemlerin kalıpları)
<span class="anker" id="satz-10-5"></span>

<ol class="al">

<li>

Bir *toplama* eşleniğini değiştirmeden her girdiye iletir.

</li>

<li>

Bir *çarpma* her girdiye kendi eşleniği çarpı *diğer* girdinin değerini iletir.

</li>

<li>

Bir *maksimum* eşleniğini tamamen büyük girdiye iletir, küçük girdi $0$ alır.

</li>

<li>

Tek değişkenli bir fonksiyon eşleniği kendi yerel türeviyle çarpar, lojistik fonksiyonda yani $b\,(1-b)$ ile.

</li>

<li>

Bir düğüm birden çok kez kullanılıyorsa bütün ardıllarının katkıları *toplanır*.

</li>

</ol>
:::

Her önerme, Tablo [4](rechengraphen.html#tab-4) içindeki yerel türevlerle yazılmış [(10.2)](#gl-10-2) bağıntısıdır. (b)'den yararlı bir gözlem çıkar: Bir çarpan diğerinin bin katı büyüklükteyse küçük çarpanın eşleniği büyüğünkünün bin katıdır. Girdilerin büyüklük mertebelerindeki büyük farklar bu yüzden kısmi türevlerde de aynı büyüklükte farklara yol açar.

::::beispiel [Sayısal örnek]
Tablo [6](#tab-6) içinde çarpma değerleri çaprazlamıştır: $v_1$, $v_2=5$ değerini aldı, $v_2$ ise $v_1=3$ değerini aldı. Toplamalar bu değerleri değiştirmeden iletti ve $x_2$, iki ardılı olan bir düğüm olarak $5+3=8$ topladı. Maksimumlu bir örnek: $(1,\,2,\,3)$ noktasında $f=\max(x_1,x_2)\cdot x_3$ için $v=\max(1,2)=2$ ve $f=6$ olur. Geriye doğru $\bar v=x_3=3$ ve $\bar x_3=v=2$ olur; maksimum $\bar v$ değerini büyük girdi olan $x_2$'ye iletir, yani $\bar x_2=3$ ve $\bar x_1=0$ olur. Gerçekten de $x_1<x_2$ kaldığı sürece $x_1$'deki küçük bir değişim sonucu değiştirmez.
::::

⁠**Kısacası:** Toplama dağıtır, çarpma çaprazlar, maksimum yönlendirir ve dallanmalarda toplanır.

### Maliyet

<span class="anker" id="stufe-10-5"></span>

Ters mod neden bu kadar önemlidir? Çünkü çok sayıda girdisi olan bir fonksiyonun gradyanını neredeyse fonksiyon değerinin kendisi kadar ucuza verir. Yöntemlerin karşılaştırılması bunu açıkça gösterir.

İleri mod, $n$ değişkenli bir fonksiyonun gradyanı için her girdi doğrultusu başına bir tane olmak üzere $n$ geçiş gerektirir. Bir geçiş, $f$ fonksiyonunun bir değerlendirmesinin küçük bir katına mal olur, çünkü her temel işleme onun teğet değeri eklenir. Fark bölümleri ise $n+1$ ya da $2n$ değerlendirme bile gerektirir. Ters mod buna karşılık, $n$ ne kadar büyük olursa olsun, her zaman tam olarak bir ileri hesaplama ve bir geri geçiş gerektirir. Geri geçişte her kenar, bir çarpma ve bir toplamayla, tam olarak bir kez kullanılır. Dolayısıyla geri geçiş de ileri hesaplamanın yalnızca küçük bir katına mal olur.

:::satz Teorem 10.6 (İleri ve ters modun maliyeti)
<span class="anker" id="satz-10-6"></span>

$\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$, temel işlemlerden oluşan bir hesaplama grafiğiyle verilmiş olsun ve bir değerlendirme $T$ süresine mal olsun. O zaman Jacobi matrisinin tamamı ileri modda yaklaşık $c\cdot n\cdot T$, ters modda yaklaşık $c\cdot m\cdot T$ süreye mal olur. $c$ sayısı $n$ ve $m$'ye bağlı değildir. Her temel aritmetik işlem bir adım olarak sayılırsa, fonksiyon değeri ile gradyanın birlikte, fonksiyon değerinin tek başına gerektirdiğinin en fazla dört katı adım gerektirdiği gösterilebilir; bellek erişimleri de hesaba katılırsa $c$, $6$'nın altında kalır ve pratikte çoğu zaman $2$ ile $3$ arasındadır. Bir sayı için ($m=1$) gradyanın tamamı ters modda dolayısıyla bir değerlendirmenin yalnızca sabit küçük bir katına mal olur.
:::

Teorem, her temel işlem için onun geri adımının kendisine oranla kaç hesap adımı gerektirdiği sayılarak ispatlanır. Buradan pratik bir kural çıkar: Milyonlarca ayar düğmesine bağlı bir sayıda olduğu gibi çok girdi ve bir çıktı, ters modu gerektirir. Az girdi ve çok çıktı ileri modu gerektirir. Çok girdili ve çok çıktılı bir fonksiyonun Jacobi matrisinin tamamı için böyle bir hile yoktur; orada her yöntem çok sayıda geçişe mal olur.

Ters modun bir bedeli vardır: bellek. Geri geçiş ileri hesaplamanın bütün değerlerine ihtiyaç duyar, çünkü yerel türevler onlarla hesaplanır. Dolayısıyla her ara değer, geri geçiş onun yanından geçene kadar saklanmalıdır. Uzun hesaplarda bu bellek çoğu zaman asıl sınırdır.

::::beispiel [Sayısal örnek]
Bir fonksiyonun $n=10^6$ girdisi olsun ve bir değerlendirme bir saniye sürsün. İleri mod gradyan için $10^6$ geçiş, yani en az $10^6$ saniye, $11$ günden biraz fazla gerektirir. Merkezi fark bölümleri $2\cdot10^6$ değerlendirme, $23$ günden biraz fazla gerektirir ve sonunda yalnızca yaklaşık olarak doğrudur. Ters mod bir ileri hesaplama ve bir geri geçiş gerektirir, $c\approx3$ ile yani birkaç saniye.
::::

⁠**Kısacası:** Ters mod bir sayının $n$ kısmi türevinin hepsini, $n$'den bağımsız olarak, bir değerlendirmenin küçük sabit bir katına verir; bunun bedelini bütün ara değerler için bellekle öder.

:::hintergrund Ters mod neden bu kadar ucuzdur ve nereden gelir
Bütün yollar üzerinden toplamın çok sayıda terimi olabilir. Her biri öncülünü iki kez kullanan on hesap adımı art arda bağlanırsa, örneğin $v_{k+1}=v_k\cdot v_k$, girdi ile sonuç arasında $2^{10}=1024$ yol vardır, $50$ adımda $10^{15}$'ten fazla. Ters mod bu yolları asla tek tek saymaz. Aynı düğümden geçen bütün yolları o düğümün eşleniğinde toplar ve bu ara toplamı bütün öncüller için yeniden kullanır. Bu, Kesim [9.1](rechengraphen.html#stufe-9-1)'deki adım adım çarpım kuralıyla aynı fikirdir: Bir ara sonuç bir kez hesaplanır ve sonra çok kez kullanılır. Böylece her kenar bir çarpma ve bir toplamaya mal olur ve maliyet yolların sayısıyla değil, kenarların sayısıyla büyür. Bellek ihtiyacı, yalnızca bazı ara değerler saklanıp geri kalanlar geri geçişte yeniden hesaplanarak azaltılabilir; akıllıca dağıtıldığında bellek ve hesap süresinin basit bir değerlendirmenin süresini aştığı çarpan, hesabın uzunluğuyla yalnızca logaritmik olarak büyür.

İleri mod 1964'te bir bilgisayar programı olarak betimlendi. Ters modu Seppo Linnainmaa 1970'te Helsinki Üniversitesi'ndeki yüksek lisans tezinde, bütün hesap adımlarının yuvarlama hatalarının sonucu nasıl etkilediğini kestirmek için geliştirdi; sonucun her ara adıma duyarlılığı tam olarak o adımın eşleniğidir. Ters modu herhangi bir hesap için otomatik olarak üreten bir program 1980'de geldi.
:::

### Parantezleme: vektör çarpı Jacobi matrisi

<span class="anker" id="stufe-10-6"></span>

İki mod arasındaki fark matrislerle de betimlenebilir. $\mathbf{g}_1,\dots,\mathbf{g}_L$ aşamalarından oluşan ve bir sayıyla biten bir hesabın Jacobi matrisi [(6.1)](die-kettenregel-fur-mehrere-variablen.html#gl-6-1) uyarınca şudur:

$$\mathbf{J}=\mathbf{J}_L\,\mathbf{J}_{L-1}\cdots\mathbf{J}_1 ,$$

burada $\mathbf{J}_L$ bir satırdır, çünkü son aşamanın yalnızca bir çıktısı vardır. Çarpım nasıl parantezlenirse parantezlensin aynıdır; ama [Bölüm 1, Kesim 9.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-3)'e göre maliyet çok farklıdır. Ters mod soldan parantezler: $\bigl((\mathbf{J}_L\mathbf{J}_{L-1})\,\mathbf{J}_{L-2}\bigr)\cdots$. Her adım bir satırı bir matrisle çarpar ve yine bir satır, yani ilgili aşamanın devrik eşleniğini verir. İleri mod sağdan parantezler: $\mathbf{J}_L\bigl(\cdots(\mathbf{J}_2\,(\mathbf{J}_1\dot{\mathbf{x}}))\bigr)$. Tek bir $\dot{\mathbf{x}}$ vektörü için bu da ucuzdur; ama gradyanın tamamı için böyle $n$ vektör gerekir ve bu, $\mathbf{J}_2\mathbf{J}_1$, $\mathbf{J}_3\mathbf{J}_2\mathbf{J}_1,\dots$ matrislerini tamamen çarpmak kadar pahalıdır.

Buna ikinci bir nokta eklenir: Jacobi matrisleri hiçbir zaman oluşturulmaz. Her geri adım, temel işlemlerin kurallarıyla, eşlenik ile Jacobi matrisinin çarpımını doğrudan hesaplar. Bir $\mathbf{y}=\mathbf{A}\mathbf{x}$ matris-vektör çarpımı için bu, [(7.6)](ableiten-nach-vektoren-und-matrizen.html#gl-7-6) uyarınca başka bir matris olmadan $\bar{\mathbf{x}}=\mathbf{A}^{\top}\bar{\mathbf{y}}$ olur; eleman eleman uygulanan bir fonksiyon için [(5.4)](die-jacobi-matrix.html#gl-5-4) uyarınca, bir köşegen matris kurulmadan, türevlerle bileşen bileşen çarpımdır. Bu gereklidir de: Bir aşamanın $10^5$ girdisi ve $10^5$ çıktısı varsa Jacobi matrisinin $10^{10}$ elemanı vardır, sayı başına sekiz baytla yani $80$ gigabayt.

::::beispiel [Sayısal örnek]
Bir hesap üç $\mathbb{R}^{1000}\to\mathbb{R}^{1000}$ aşamasından ve bir son $\mathbb{R}^{1000}\to\mathbb{R}$ aşamasından oluşsun. Bir satır ile $1000\times1000$ tipinde bir matrisin çarpımı [Bölüm 1, Kesim 9.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-3)'e göre yaklaşık $2\cdot10^6$ temel aritmetik işleme, bu türden iki matrisin çarpımı yaklaşık $2\cdot10^9$ işleme mal olur. Soldan parantezlendiğinde satır ile matrisin üç çarpımı söz konusudur, toplam yaklaşık $6\cdot10^6$. Sağdan parantezlendiğinde iki matris çarpımı ve bir satır-matris çarpımı söz konusudur, toplam yaklaşık $4\cdot10^9$, aşağı yukarı $670$ kat fazla.
::::

⁠**Kısacası:** Ters mod Jacobi matrislerinin zincirini soldan bir satırla, ileri mod sağdan bir sütunla çarpar; Jacobi matrislerinin kendileri hiçbir zaman oluşturulmaz.

:::aufgabe Alıştırma 35 ★ Bir kare boyunca geriye doğru
<span class="anker" id="aufg-35"></span>

$f=(x_1x_2+x_3)^2$, Alıştırma [32](rechengraphen.html#aufg-32)'deki gibi olsun.

<ol class="al">

<li>

$(1,\,2,\,3)$ noktasında bütün eşlenikleri ters modda hesaplayın ve Tablo [6](#tab-6) gibi bir tabloda gösterin.

</li>

<li>

İleri mod aynı gradyan için kaç geçiş gerektirirdi? $\dot{\mathbf{x}}=\mathbf{e}_1$ için geçişi yapın.

</li>

</ol>

:::loesung
(a) Alıştırma [32](rechengraphen.html#aufg-32)'deki değerlerle:

| Düğüm | Hesap | Eşlenik |
|---|---|---|
| $f$ | başlangıç | $\bar f=1$ |
| $v_2$ | $\bar f\cdot2v_2$ | $\bar v_2=10$ |
| $v_1$ | $\bar v_2\cdot1$ | $\bar v_1=10$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=10$ |
| $x_2$ | $\bar v_1\cdot x_1$ | $\bar x_2=10$ |
| $x_1$ | $\bar v_1\cdot x_2$ | $\bar x_1=20$ |

(b) Her girdi için bir tane olmak üzere üç geçiş. $\dot{\mathbf{x}}=\mathbf{e}_1$ ile: $\dot v_1=x_2\dot x_1+x_1\dot x_2=2$, $\dot v_2=\dot v_1+\dot x_3=2$, $\dot f=2v_2\,\dot v_2=10\cdot2=20=\partial f/\partial x_1$.
:::
:::

:::aufgabe Alıştırma 36 ★★ Grafikte lojistik fonksiyon
<span class="anker" id="aufg-36"></span>

$\sigma$ lojistik fonksiyon olmak üzere $f(x_1,x_2)=\sigma(2x_1-x_2)$ olsun.

<ol class="al">

<li>

$v_1=2x_1$, $v_2=v_1-x_2$, $f=\sigma(v_2)$ ile grafiği çizin ve $(1,\,1)$ noktasında ileri doğru hesaplayın.

</li>

<li>

Bütün eşlenikleri hesaplayın. $\sigma$ düğümü yerel türevi için hangi saklanmış sayıya ihtiyaç duyar?

</li>

<li>

Hesaplayarak doğrulayın: $\nabla f(\mathbf{x})=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$.

</li>

</ol>

:::loesung
(a) Grafiğin kenarları $x_1\to v_1$, $v_1\to v_2$, $x_2\to v_2$ ve $v_2\to f$ olur. $(1,\,1)$ noktasında ileri hesap: $v_1=2$, $v_2=1$, $f=\sigma(1)\approx0{,}7311$.

(b) $\bar f=1$; $\bar v_2=\bar f\cdot f\,(1-f)\approx0{,}7311\cdot0{,}2689\approx0{,}1966$; $\bar v_1=\bar v_2\cdot1\approx0{,}1966$; $\bar x_2=\bar v_2\cdot(-1)\approx-0{,}1966$; $\bar x_1=\bar v_1\cdot2\approx0{,}3932$. Tablo [4](rechengraphen.html#tab-4) uyarınca $\sigma$ düğümü yerel türevi için yalnızca kendi saklanan çıktısı $f$'ye ihtiyaç duyar.

(c) Zincir kuralı uyarınca $\nabla f=\sigma'(2x_1-x_2)\,\nabla(2x_1-x_2)=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$, dolayısıyla $(1,\,1)$ noktasında $0{,}1966\cdot(2,\,-1)^{\top}=(0{,}3932;\ -0{,}1966)^{\top}$.
:::
:::

:::aufgabe Alıştırma 37 ★★ Dual sayılar
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

$p(x)=(x+1)(x+2)(x+3)(x+4)$ ifadesini $x=0+1\varepsilon$ dual sayısıyla hesaplayın ve $p(0)$ ile $p'(0)$ değerlerini okuyun.

</li>

<li>

Aynı biçimde $(x^2+1)^3$ ifadesini $x=1+\varepsilon$ noktasında hesaplayın ve zincir kuralıyla karşılaştırın.

</li>

</ol>

:::loesung
(a) $x=\varepsilon$ ile:

$$(1+\varepsilon)(2+\varepsilon)=2+3\varepsilon,\quad (2+3\varepsilon)(3+\varepsilon)=6+11\varepsilon,\quad (6+11\varepsilon)(4+\varepsilon)=24+50\varepsilon .$$

Dolayısıyla $p(0)=24$ ve $p'(0)=50$; $\varepsilon$ önündeki katsayılar tam olarak Kesim [9.1](rechengraphen.html#stufe-9-1)'deki sayısal örnekteki $p_k'$ değerleridir.

(b) $(1+\varepsilon)^2=1+2\varepsilon$, buna $1$ eklenince $2+2\varepsilon$ olur; $(2+2\varepsilon)^2=4+8\varepsilon$ ve $(4+8\varepsilon)(2+2\varepsilon)=8+24\varepsilon$. Zincir kuralı $1$ noktasında $3\,(x^2+1)^2\cdot2x=3\cdot4\cdot2=24$ verir.
:::
:::

:::aufgabe Alıştırma 38 ★★★ Hangi mod?
<span class="anker" id="aufg-38"></span>

<ol class="al">

<li>

Bir hesabın $3$ girdisi ve $1000$ çıktısı, başka bir hesabın $1000$ girdisi ve $3$ çıktısı var. İleri ve ters mod, Jacobi matrisinin tamamı için her birinde kaç geçiş gerektirir?

</li>

<li>

Tam dolu bir $\mathbf{B}\in\mathbb{R}^{n\times n}$ matrisiyle $f(\mathbf{x})=\mathbf{c}^{\top}\mathbf{B}\mathbf{x}$ olsun; hesap, $\mathbf{y}=\mathbf{B}\mathbf{x}$ ve $f=\mathbf{c}^{\top}\mathbf{y}$ olmak üzere iki aşamada yapılsın. Bir ileri geçiş $\mathbf{c}^{\top}(\mathbf{B}\dot{\mathbf{x}})$, bir geri geçiş $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$ hesaplar. Bir matris-vektör çarpımı yaklaşık $2n^2$, bir iç çarpım yaklaşık $2n$ işleme mal oluyorsa, iki yol için gradyanın tamamının kaç temel aritmetik işleme mal olduğunu sayın.

</li>

<li>

Ters mod neden ileri moddan fazla bellek gerektirir? İleri mod hangi değerleri hemen unutabilir?

</li>

</ol>

:::loesung
(a) $3$ girdi ve $1000$ çıktıyla ileri mod $3$ geçiş, ters mod $1000$ geçiş gerektirir; ileri mod seçilir. $1000$ girdi ve $3$ çıktıyla durum tersinedir: $1000$ ileri geçişe karşı $3$ geri geçiş.

(b) İleri modda gradyan, $\dot{\mathbf{x}}=\mathbf{e}_1,\dots,\mathbf{e}_n$ ile $n$ geçiş gerektirir; her geçişte bir $\mathbf{B}\dot{\mathbf{x}}$ matris-vektör çarpımı ve bir iç çarpım vardır, toplam yaklaşık $n\,(2n^2+2n)\approx2n^3$ temel aritmetik işlem. Ters modda $\bar{\mathbf{y}}=\mathbf{c}$ olur ve $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$ bir matris-vektör çarpımına, yaklaşık $2n^2$ işleme mal olur; buna yaklaşık $2n^2+2n$ işlemli ileri hesaplama eklenir. Demek ki ters mod yaklaşık $n/2$ kat hızlıdır.

(c) Geri geçiş, yerel türevleri hesaplamak için ileri hesaplamanın değerlerine ihtiyaç duyar ve ancak ileri hesaplama bittikten sonra başlar. Bu yüzden bütün ara değerler o zamana kadar saklanmalıdır. İleri modda değer ve teğet değeri birlikte ileri doğru ilerler; düğümün bütün ardılları hesaplanır hesaplanmaz ikisine de artık ihtiyaç kalmaz ve unutulabilirler.
:::
:::
