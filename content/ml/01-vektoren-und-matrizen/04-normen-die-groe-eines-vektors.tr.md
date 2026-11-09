---
title: Normlar: bir vektörün büyüklüğü
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
knoten: Temeller 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15210400
summary: Bir vektör ne kadar büyüktür?
tags: Öklid normu, uzunluğu, normlanmış, normlamak, mutlak değerler toplamı normu, maksimum normu, norm, üçgen eşitsizliği
lang: tr
---

<span class="anker" id="stufe-3"></span>

:::zweck
Bir vektör ne kadar büyüktür? Bu sorunun birden çok doğru cevabı vardır. Bu kesim en önemli üç cevabı tanıtıyor, bunların ortak yanını açıklıyor ve ne işe yaradıklarını gösteriyor: bir hatanın ne kadar büyük olduğunu ölçmeye.
:::

### Öklid normu

<span class="anker" id="stufe-3-1"></span>

Bir okun akla ilk gelen büyüklüğü uzunluğudur. Düzlemde uzunluğu Pisagor teoremi verir: $(3,\,-4)^{\top}$ oku, dik kenarları $3$ ve $4$ olan bir dik üçgenin hipotenüsüdür, dolayısıyla uzunluğu $\sqrt{3^2+4^2}=5$ olur. Uzayda Pisagor teoremi iki kez uygulanır ve üç karenin toplamının karekökü elde edilir. Aynı formül her boyutta kullanılır.

:::definition Tanım 3.1 (Öklid normu)
<span class="anker" id="satz-3-1"></span>

Bir $\mathbf{x}\in\mathbb{R}^d$ vektörünün __Öklid normu__ şudur:

<span class="anker" id="gl-3-1"></span>
$$\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}=\sqrt{x_1^2+x_2^2+\dots+x_d^2} . \tag{3.1}$$

Bu seride indissiz $\lVert\mathbf{x}\rVert$ her zaman Öklid normu anlamına gelir.
:::

Bu norma vektörün __uzunluğu__ ya da karelerden dolayı $L_2$-normu da denir. Uzunluğu $1$ olan bir vektöre __normlanmış__ vektör denir. Bir $\mathbf{x}\ne\mathbf{0}$ vektörü uzunluğuna bölünürse $\mathbf{x}/\lVert\mathbf{x}\rVert$ normlanmıştır ve aynı yönü gösterir. Bu adıma __normlamak__ denir.

::::beispiel [Sayısal örnek]
$\mathbf{x}=(3,\,-4)^{\top}$ vektörünün uzunluğu $\lVert\mathbf{x}\rVert_2=5$ olur (Şekil [12](#abb-12)). Normlanmış hâli $\mathbf{x}/5=(0{,}6;\ -0{,}8)^{\top}$ vektörüdür. Uzayda $\lVert(1,\,2,\,2)^{\top}\rVert=\sqrt{1+4+4}=3$ bulunur.

:::abbildung ml/k1rl2 12
$(3,\,-4)^{\top}$ vektörünün Öklid normu: Bileşenlerin karesi alınır, kareler toplanır, karekök alınır. Eksi işareti kare alınırken kaybolur.
:::
::::

⁠**Kısacası:** Öklid normu okun uzunluğudur, yani bileşenlerin kareleri toplamının kareköküdür.

### Mutlak değerler toplamı normu

<span class="anker" id="stufe-3-2"></span>

Sokakları dik açılarla kesişen bir şehirde taksi bina bloklarının arasından çapraz geçemez. Orijinden $(3,\,-4)^{\top}$ noktasına gitmek için bir yönde $3$, öteki yönde $4$ blok, toplam $7$ blok yol alır. Bu uzunluğu mutlak değerler toplamı normu ölçer.

:::definition Tanım 3.2 (Mutlak değerler toplamı normu)
<span class="anker" id="satz-3-2"></span>

Bir $\mathbf{x}\in\mathbb{R}^d$ vektörünün __mutlak değerler toplamı normu__ şudur:

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{x}\rVert_1=|x_1|+|x_2|+\dots+|x_d|=\sum_{j=1}^d|x_j| . \tag{3.2}$$
:::

Bu norma $L_1$-normu ya da Manhattan'ın sokak ağından dolayı Manhattan normu da denir.

::::beispiel [Sayısal örnek]
$\mathbf{x}=(3,\,-4)^{\top}$ için $\lVert\mathbf{x}\rVert_1=7$ (Şekil [13](#abb-13)) ve $\lVert(1,\,2,\,2)^{\top}\rVert_1=1+2+2=5$ olur.

:::abbildung ml/k1rl1 13
$\mathbf{x}=(3,\,-4)^{\top}$ vektörünün mutlak değerler toplamı normu: Bileşenlerin mutlak değerleri toplanır.
:::

Mutlak değerler toplamı normu burada Öklid uzunluğundan büyüktür, çünkü sokaklar üzerinden dolambaçlı yol kuş uçuşu mesafeden uzundur.
::::

⁠**Kısacası:** Mutlak değerler toplamı normu bileşenlerin mutlak değerlerini toplar; dik açılı bir sokak ağında alınan yoldur.

### Maksimum normu

<span class="anker" id="stufe-3-3"></span>

Bir kalite denetiminde çoğu zaman yalnızca en kötü sapma önemlidir. Bir parçanın üç ölçüsü vardır ve her biri nominal değerden en çok $0{,}1$ mm sapabilir. Parçanın uygun olup olmadığına yalnızca üç sapmanın en büyüğü karar verir.

:::definition Tanım 3.3 (Maksimum normu)
<span class="anker" id="satz-3-3"></span>

Bir $\mathbf{x}\in\mathbb{R}^d$ vektörünün __maksimum normu__, bileşenlerin mutlak değerlerinin en büyüğüdür:

<span class="anker" id="gl-3-3"></span>
$$\lVert\mathbf{x}\rVert_\infty=\max_{j=1,\dots,d}|x_j| . \tag{3.3}$$
:::

Bu norma $L_\infty$-normu da denir. Sonsuzluk işaretinin nedeni bir sonraki alt kesimde açıklanıyor.

::::beispiel [Sayısal örnek]
$\lVert(3,\,-4)^{\top}\rVert_\infty=4$ olur ve $\lVert(1,\,2,\,2)^{\top}\rVert_\infty=2$. Bir parçanın sapmaları $(0{,}05;\ -0{,}08;\ 0{,}02)$ mm ise bunların maksimum normu $0{,}08$ mm olur ve parça uygundur.
::::

⁠**Kısacası:** Maksimum normu bileşenlerin mutlak değerlerinin en büyüğü, yani en kötü tek sapmadır.

### Bir normu norm yapan nedir?

<span class="anker" id="stufe-3-4"></span>

Üç norm farklı ölçer, ama her büyüklük ölçüsünden beklenen üç özellik hepsinde ortaktır. Yalnızca sıfır vektörünün büyüklüğü sıfırdır. İki kat uzun bir vektör iki kat büyüktür. Ve dolambaçlı bir yol hiçbir zaman doğrudan yoldan kısa değildir.

:::definition Tanım 3.4 (Norm)
<span class="anker" id="satz-3-4"></span>

$\mathbb{R}^d$ üzerinde bir __norm__, her $\mathbf{x}$ vektörüne bir $\lVert\mathbf{x}\rVert$ gerçel sayısını öyle karşılık getirir ki bütün $\mathbf{u},\mathbf{v},\mathbf{x}\in\mathbb{R}^d$ vektörleri ve bütün $c$ skalerleri için şunlar geçerlidir:

<ol>

<li>

$\lVert\mathbf{x}\rVert\ge0$ ve $\lVert\mathbf{x}\rVert=0$ yalnızca $\mathbf{x}=\mathbf{0}$ için;

</li>

<li>

$\lVert c\,\mathbf{x}\rVert=|c|\,\lVert\mathbf{x}\rVert$;

</li>

<li>

$\lVert\mathbf{u}+\mathbf{v}\rVert\le\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ (__üçgen eşitsizliği__).

</li>

</ol>
:::

Üçgen eşitsizliği adını $\mathbf{u}$, $\mathbf{v}$ ve $\mathbf{u}+\mathbf{v}$ oklarından oluşan bir üçgenden alır: $\mathbf{u}+\mathbf{v}$ kenarı hiçbir zaman öteki iki kenarın toplamından uzun değildir.

**$p$-normları.** Mutlak değerler toplamı normu ile Öklid normu, bütün bir ailenin iki üyesidir. Her $p\ge1$ sayısı için __$p$-normu__ şudur:

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{x}\rVert_p=\Bigl(\sum_{j=1}^d|x_j|^p\Bigr)^{1/p} . \tag{3.4}$$

$p=1$ için bu mutlak değerler toplamı normu, $p=2$ için Öklid normudur. $p$ ne kadar büyükse toplamda en büyük bileşen o kadar ağır basar. $p\to\infty$ için yalnızca o kalır; maksimum normunun $\lVert\cdot\rVert_\infty$ diye yazılmasının nedeni budur.

**Birim küre.** Bir normun nasıl ölçtüğü, büyüklüğü $1$ olan bütün vektörlerin kümesinde görülür. Bu kümeye, bir küre olmak zorunda olmasa da normun __birim küresi__ denir (Şekil [14](#abb-14)). Öklid normu için bu küme düzlemde yarıçapı $1$ olan çemberdir. Mutlak değerler toplamı normu için $|x_1|+|x_2|=1$ eşkenar dörtgenidir: Her çeyrek düzlemde bu bir doğru parçasıdır, örneğin $x_1,x_2\ge0$ için $x_1+x_2=1$. Maksimum normu için köşeleri $(\pm1,\,\pm1)$ olan karedir, çünkü orada iki bileşenden mutlak değerce büyük olanı tam olarak $1$ olur.

:::abbildung ml/k1einheitskugeln 14
Düzlemde üç normun birim küreleri: mutlak değerler toplamı normunun eşkenar dörtgeni (solda, turuncu), Öklid normunun çemberi (ortada, mavi) ve maksimum normunun karesi (sağda, yeşil); karşılaştırma için her birinde öteki ikisi gri. Üçü de $(\pm1,\,0)$ ve $(0,\,\pm1)$ noktalarından geçer.
:::

::::beispiel [Sayısal örnek]
$\mathbf{x}=(3,\,-4)^{\top}$ için $\lVert\mathbf{x}\rVert_1=7$, $\lVert\mathbf{x}\rVert_2=5$, $\lVert\mathbf{x}\rVert_3=91^{1/3}\approx4{,}498$, $\lVert\mathbf{x}\rVert_{10}=1\,107\,625^{1/10}\approx4{,}022$ (Şekil [15](#abb-15)) ve $\lVert\mathbf{x}\rVert_\infty=4$ bulunur. $p$ büyüdükçe $p$-normu bileşenlerin mutlak değerlerinin en büyüğüne, burada $4$ sayısına yaklaşır. Nedeni toplamda zaten görülür: $p=10$ iken $4^{10}$ sayısı $3^{10}$ sayısının neredeyse on sekiz katıdır ve toplamın kökü, yalnızca $4^{10}$ sayısının kökünden pek büyük değildir.

:::abbildung ml/k1rlp 15
$\mathbf{x}=(3,\,-4)^{\top}$ vektörünün $p=3$ ve $p=10$ için iki $p$-normu. $p$ ne kadar büyükse en büyük bileşenin terimi o kadar ağır basar.
:::
::::

Mutlak değerler toplamı normunun (N1)–(N3) koşullarını sağladığı doğrudan hesapla görülür: (N1) ve (N2) geçerlidir, çünkü $|x_j|\ge0$ ve $|c\,x_j|=|c|\,|x_j|$ olur. (N3), sayılar için üçgen eşitsizliğinin, $|u_j+v_j|\le|u_j|+|v_j|$, bütün $j$ üzerinden toplanmasından çıkar. Maksimum normu için de aynı biçimde gösterilir. Öklid normu için üçgen eşitsizliği sezgisel olarak açıktır, çünkü iki nokta arasındaki doğrudan yol, üçüncü bir noktadan geçen dolambaçlı bir yoldan hiçbir zaman uzun değildir.

⁠**Kısacası:** Bir norm bir vektörün büyüklüğünü öyle ölçer ki yalnızca sıfır vektörünün büyüklüğü sıfırdır, katlar orantılı olarak büyür ve üçgen eşitsizliği geçerlidir; $p$-normları, $L_1$, $L_2$ ve $L_\infty$ normlarının da ait olduğu bir aile oluşturur.

:::hintergrund Neden $p\ge1$ olmalı ve “sıfır normu” neden bir norm değildir?
$p<1$ için [(3.4)](#gl-3-4) formülü üçgen eşitsizliğini bozar. $p=\tfrac12$ ile $\lVert(1,0)^{\top}\rVert_{1/2}=1$ ve $\lVert(0,1)^{\top}\rVert_{1/2}=1$ olur, ama $\lVert(1,1)^{\top}\rVert_{1/2}=(1+1)^2=4>1+1$. Bu formülün “birim küresi” içeri doğru göçüktür, bir yıldız biçimindedir.

Sık sık “$L_0$-normu” diye bir şeyle karşılaşılır: sıfırdan farklı bileşenlerin sayısı. Bu, bir vektörün kaç özniteliği gerçekten kullandığı için yararlı bir ölçüdür. Yine de bir norm değildir, çünkü (N2) koşulunu bozar: $2\mathbf{x}$ vektörünün sıfırdan farklı bileşenlerinin sayısı $\mathbf{x}$ vektörününkiyle aynıdır, iki katı değil.
:::

:::hintergrund Her norm bir iç çarpımdan gelmez
Öklid normu iç çarpımdan kurulmuştur, $\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$. Buradan paralelkenar özdeşliği denen bir eşitlik çıkar. İç çarpımın hesap kurallarıyla çarpımlar açılırsa şu bulunur:

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,\qquad \lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,$$

ve iki satır toplanınca $\lVert\mathbf{u}+\mathbf{v}\rVert^2+\lVert\mathbf{u}-\mathbf{v}\rVert^2=2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2$ çıkar: Bir paralelkenarda iki köşegenin karelerinin toplamı dört kenarın karelerinin toplamına eşittir. Bir iç çarpımdan gelen her norm bu eşitliği sağlamak zorundadır. Mutlak değerler toplamı normu sağlamaz: $\mathbf{u}=\mathbf{e}_1$ ve $\mathbf{v}=\mathbf{e}_2$ ile sol taraf $\lVert(1,1)^{\top}\rVert_1^2+\lVert(1,-1)^{\top}\rVert_1^2=4+4=8$, sağ taraf ise $2+2=4$ olur. Demek ki uzunluğu mutlak değerler toplamı normu olan bir iç çarpım yoktur. Bu yüzden bu normla, iç çarpımın verdiği türden açılar ölçülemez.
:::

### Hata vektörü ve büyüklüğü

<span class="anker" id="stufe-3-5"></span>

Bir model tahminler üretir ve bir noktada gerçek değerler öğrenilir. O zaman tahminlerin ne kadar iyi olduğu bilinmek istenir. Her örnek için bir sapma vardır ve bu sapmalar bir vektör oluşturur. Bu vektörün normu, hatanın toplam büyüklüğü için bir ölçüdür.

:::definition Tanım 3.5 (Hata vektörü)
<span class="anker" id="satz-3-5"></span>

$\hat y_1,\dots,\hat y_N$ bir modelin $N$ örnek için tahminleri, $y_1,\dots,y_N$ de gerçek değerler ise

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{y}}-\mathbf{y}=(\hat y_1-y_1,\,\dots,\,\hat y_N-y_N)^{\top} \tag{3.5}$$

vektörüne __hata vektörü__ denir. Burada $\hat{\mathbf{y}}=(\hat y_1,\dots,\hat y_N)^{\top}$ tahminlerin vektörü, $\mathbf{y}=(y_1,\dots,y_N)^{\top}$ de gerçek değerlerin vektörüdür.
:::

Hata vektörüne hangi normun uygulanacağı, en çok hangi hatalardan kaçınıldığına dair bir karardır. İşaret burada rol oynamaz, çünkü her norm $\mathbf{y}-\hat{\mathbf{y}}$ vektörüne $\hat{\mathbf{y}}-\mathbf{y}$ vektörüyle aynı büyüklüğü verir.

::::beispiel [Sayısal örnek]
Dört daire satılmış, gerçek fiyatlar $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$ bin avro olmuştur. İki eksper, A ve B, önceden şu tahminleri yapmıştı:

$$\hat{\mathbf{y}}_{\mathrm A}=(210,\,120,\,300,\,230)^{\top},\qquad \hat{\mathbf{y}}_{\mathrm B}=(200,\,130,\,290,\,280)^{\top}.$$

Hata vektörleri $\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}=(10,\,-10,\,10,\,-10)^{\top}$ ve $\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}=(0,\,0,\,0,\,40)^{\top}$ olur. Eksper A her seferinde biraz yanılmış, eksper B ise üç kez tam tutturmuş, bir kez de çok yanılmış. Üç norm farklı hükümler verir (Tablo [2](#tab-2)). Öklid normlarının hesabını Şekil [16](#abb-16) gösteriyor.

:::abbildung ml/k1rfehler 16
İki hata vektörünün bin avro cinsinden Öklid normları. B'nin tek büyük hatası kareler toplamına $1\,600$ katkı yapar; bu, A'nın dört küçük hatasının toplam katkısının dört katıdır.
:::

<span class="anker" id="tab-2"></span>

**Tablo 2:** İki eksperin hata vektörlerinin normları, bin avro cinsinden.

|  | $\lVert\cdot\rVert_1$ | $\lVert\cdot\rVert_2$ | $\lVert\cdot\rVert_\infty$ |
|---|---|---|---|
| Eksper A, $\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}$ | $40$ | $\sqrt{4\cdot100}=20$ | $10$ |
| Eksper B, $\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}$ | $40$ | $\sqrt{1600}=40$ | $40$ |

Mutlak değerler toplamı normuna göre ikisi de aynı derecede iyidir: İkisi de toplamda $40$ bin avro yanılmıştır. Öklid normuna göre A iki kat, maksimum normuna göre dört kat daha iyidir. Hangi dairede olursa olsun her bin avroluk sapmayı aynı derecede kötü bulan, $L_1$ ile ölçer. Büyük bir aykırı değeri birçok küçük hatadan daha kötü bulan, $L_2$ ile ölçer. Yalnızca en kötü durumdan çekinen, $L_\infty$ ile ölçer.
::::

⁠**Kısacası:** Hata vektörü bütün tahminlerin sapmalarını bir araya toplar; normu hatanın büyüklüğünü ölçer ve normun seçimi hangi hataların özellikle önemli sayılacağını belirler.

:::hintergrund Kareler toplamı neden büyük hataları cezalandırır da küçükleri neredeyse görmez?
Öklid normunda her sapma karesiyle girer. $0{,}1$ büyüklüğünde bir sapma $0{,}01$ katkı yapar, $10$ büyüklüğünde bir sapma ise $100$. Kare almak küçük sayıları küçültür, büyük sayıları büyütür. Bu yüzden $40$ büyüklüğündeki tek bir büyük hata $1600$ katkı yapar; bu, her biri $10$ olan dört hatanın toplam katkısının dört katıdır. Mutlak değerler toplamı normu ise her yerde aynı hızla büyür: Sapmanın her birimi, ister küçük ister büyük bir hataya ait olsun, aynı ölçüde hesaba katılır. Bu yüzden bu norm “tam olarak sıfır” ile “biraz sapmış” arasında da belirgin bir ayrım yapar, kareler toplamı ise bu ikisi arasında neredeyse hiç fark gözetmez. Hangi özelliğin istendiği göreve bağlıdır; birden çok normun bulunmasının nedeni de tam olarak budur.
:::

### Etkin değer

<span class="anker" id="stufe-3-6"></span>

Öklid normu bileşen sayısıyla birlikte büyür. Bir eksper dört daire, bir başkası dört yüz daire üzerinden değerlendirilirse, ikincisi daire başına aynı iyilikte tahmin yapsa bile çok daha uzun bir hata vektörüne sahip olur. Hatalar örnek başına karşılaştırılmak isteniyorsa bileşen sayısının etkisi hesaptan çıkarılmalıdır.

:::definition Tanım 3.6 (Etkin değer)
<span class="anker" id="satz-3-6"></span>

Bir $\mathbf{x}\in\mathbb{R}^n$ vektörünün __etkin değeri__ şudur:

<span class="anker" id="gl-3-6"></span>
$$\operatorname{rms}(\mathbf{x})=\frac{\lVert\mathbf{x}\rVert}{\sqrt n}=\sqrt{\frac1n\sum_{i=1}^nx_i^2} . \tag{3.6}$$
:::

rms kısaltması *root mean square* anlamına gelir: karelerin ortalamasının karekökü. Etkin değer bir bileşenin tipik mutlak değeridir. Bütün bileşenlerin mutlak değeri aynı $a$ sayısıysa etkin değer tam olarak $a$ olur.

Bu ad elektrik mühendisliğinden bilinir: Bir alternatif gerilimin etkin değeri, karesinin zaman ortalamasının kareköküdür. Örneklenmiş bir sinyal için [(3.6)](#gl-3-6), integral yerine örnek değerlerle yapılan aynı hesaptır. Bir sinüs tam bir periyot boyunca $n\ge3$ eşit aralıklı noktada örneklenirse, sinüsün $1/\sqrt2$ etkin değeri bile tam olarak elde edilir.

::::beispiel [Sayısal örnek]
Önceki alt kesimdeki eksperlerin hata vektörlerinin etkin değerleri $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y})=20/\sqrt4=10$ ve $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y})=40/\sqrt4=20$ bin avrodur: A tipik olarak $10$ bin avro yanılmıştır. Genliği $1$ olan ve bir periyot içinde eşit aralıklı dört noktada örneklenen bir sinüsün örnek değerleri $\mathbf{x}=(0,\,1,\,0,\,-1)^{\top}$, etkin değeri $1/\sqrt2\approx0{,}707$ olur (Şekil [17](#abb-17)).

:::abbildung ml/k1rrms 17
Örneklenmiş bir sinüsün etkin değeri: Kareler toplanır, bileşen sayısına bölünür, karekök alınır.
:::
::::

⁠**Kısacası:** $\lVert\mathbf{x}\rVert/\sqrt n$ etkin değeri bir bileşenin tipik mutlak değeridir ve bileşen sayıları farklı olan vektörleri karşılaştırılabilir kılar.

:::hintergrund Kaç bileşen büyük olabilir?
Etkin değer, kaç bileşenin büyük bir mutlak değere sahip olabileceğini sınırlar. $n$ bileşenden $k$ tanesinin mutlak değeri en az $a>0$ ise, yalnızca bu $k$ bileşen kareler toplamına en az $k\,a^2$ katkı yapar. Kareler toplamının tamamı $n\operatorname{rms}(\mathbf{x})^2$ olduğundan $k\,a^2\le n\operatorname{rms}(\mathbf{x})^2$, yani

$$\frac kn\le\Bigl(\frac{\operatorname{rms}(\mathbf{x})}{a}\Bigr)^2 .$$

Demek ki bileşenlerin en fazla $(\operatorname{rms}/a)^2$ kadarlık bir payı en az $a$ büyüklüğünde olabilir. Bileşenlerin en fazla dörtte biri etkin değerin iki katına, en fazla yüzde biri on katına ulaşabilir. $\operatorname{rms}=20$ olan eksper B'de hataların en fazla $(20/30)^2=4/9\approx44$ % kadarı $30$ ya da daha büyük olabilir; gerçekte dört hatadan biri, yani $25$ % bu kadar büyüktür. Bu sınıra Çebişev eşitsizliği denir.
:::

:::aufgabe Alıştırma 7 ★ Norm hesaplamak
<span class="anker" id="aufg-7"></span>

$\mathbf{x}=(2,\,-1,\,0,\,2)^{\top}$ olsun.

<ol class="al">

<li>

$\lVert\mathbf{x}\rVert_1$, $\lVert\mathbf{x}\rVert_2$, $\lVert\mathbf{x}\rVert_3$ ve $\lVert\mathbf{x}\rVert_\infty$ normlarını ve $\mathbf{x}/\lVert\mathbf{x}\rVert$ normlanmış vektörünü hesaplayın.

</li>

<li>

$\lVert\mathbf{x}\rVert_\infty\le\lVert\mathbf{x}\rVert_2\le\lVert\mathbf{x}\rVert_1$ sıralamasını doğrulayın. Bu sıralamanın neden her vektör için geçerli olduğunu gerekçelendirin.

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{x}\rVert_1=2+1+0+2=5$, $\lVert\mathbf{x}\rVert_2=\sqrt{4+1+0+4}=3$, $\lVert\mathbf{x}\rVert_3=(8+1+0+8)^{1/3}=17^{1/3}\approx2{,}571$ ve $\lVert\mathbf{x}\rVert_\infty=2$. Normlanmış vektör $\mathbf{x}/3=(\tfrac23,\,-\tfrac13,\,0,\,\tfrac23)^{\top}$ olur; uzunluğu $\sqrt{(4+1+4)/9}=1$.

(b) $2\le3\le5$ olur; $2{,}571$ değeriyle $\lVert\mathbf{x}\rVert_3$ de arada kalır. Genel olarak: $|x_k|$ en büyük bileşen ise $\lVert\mathbf{x}\rVert_\infty^2=x_k^2\le\sum_jx_j^2=\lVert\mathbf{x}\rVert_2^2$ olur, çünkü toplam $x_k^2$ terimini ve onun yanında yalnızca negatif olmayan başka terimler içerir. Ayrıca $\lVert\mathbf{x}\rVert_1^2=\bigl(\sum_j|x_j|\bigr)^2=\sum_jx_j^2+\sum_{j\ne l}|x_j|\,|x_l|\ge\lVert\mathbf{x}\rVert_2^2$ olur, çünkü karma çarpımlar negatif değildir. Sezgisel olarak: Kuş uçuşu mesafe hiçbir zaman sokak ağı üzerinden giden yoldan uzun, en uzun tek parçadan da kısa değildir.
:::
:::

:::aufgabe Alıştırma 8 ★★ Emlakçı ne kadar iyi tahmin ediyor?
<span class="anker" id="aufg-8"></span>

Emlakçının tahminleri $\hat{\mathbf{y}}=(188,\,126,\,286,\,232)^{\top}$ idi (alt kesim [2.2](das-skalarprodukt.html#stufe-2-2)); gerçek fiyatlar $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$ bin avro olmuştur.

<ol class="al">

<li>

Hata vektörünü, onun üç normunu ve etkin değerini hesaplayın. Emlakçı en çok hangi dairede yanılmıştır?

</li>

<li>

İşaretlerde ne dikkat çekiyor? Emlakçı bundan sonra her tahmine $7$ bin avro ekliyor. Yeni hata vektörünü ve normlarını hesaplayın. Emlakçı üç normun hepsine göre daha iyi hâle gelmiş midir?

</li>

</ol>

:::loesung
(a) Hata vektörü $\hat{\mathbf{y}}-\mathbf{y}=(188-200,\ 126-130,\ 286-290,\ 232-240)^{\top}=(-12,\,-4,\,-4,\,-8)^{\top}$ olur. Normları: $\lVert\cdot\rVert_1=28$, $\lVert\cdot\rVert_2=\sqrt{144+16+16+64}=\sqrt{240}\approx15{,}49$, $\lVert\cdot\rVert_\infty=12$; etkin değer $\sqrt{240}/2\approx7{,}75$ bin avro. Emlakçı en çok Daire 1'de, $12$ bin avro yanılmıştır.

(b) Hataların hepsi negatiftir: Emlakçı her seferinde düşük tahmin ediyor; hatasının bir sabit bileşeni vardır. Tahminlere $7$ bin avro eklenince hata vektörü $(-5,\,3,\,3,\,-1)^{\top}$ olur; $\lVert\cdot\rVert_1=12$, $\lVert\cdot\rVert_2=\sqrt{25+9+9+1}=\sqrt{44}\approx6{,}63$, $\lVert\cdot\rVert_\infty=5$ ve etkin değer $\sqrt{44}/2\approx3{,}32$. Emlakçı üç normun hepsine göre daha iyi hâle gelmiştir. Eklenen $7$, tam olarak hataların mutlak değerlerinin ortalamasıdır, $(12+4+4+8)/4=7$: Hatanın sabit bileşenini çıkarır ve geriye yalnızca değişken bileşeni bırakır.
:::
:::
