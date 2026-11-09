---
title: Uzaklıklar ve birimler
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
knoten: Temeller 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15210500
summary: İki örneğin vektörleri birbirine yakınsa bu örnekler birbirine benzer.
tags: uzaklığı, öznitelik sütunu, merkezlenmiş, standart sapması, standartlaştırılır
lang: tr
---

<span class="anker" id="stufe-4"></span>

:::zweck
İki örneğin vektörleri birbirine yakınsa bu örnekler birbirine benzer. Bu kesim uzaklıkları ölçüyor, sonucun seçilen birimlere bağlı olduğunu gösteriyor ve öznitelikleri karşılaştırılabilir kılan bir yöntem tanıtıyor.
:::

### İki veri noktasının uzaklığı

<span class="anker" id="stufe-4-1"></span>

İki daire bütün özniteliklerde birbirinden yalnızca biraz farklıysa birbirine benzer. Farklar, bir noktadan ötekine giden ok olan $\mathbf{u}-\mathbf{v}$ fark vektöründe durur. Bu okun ne kadar büyük olduğunu bir norm söyler.

:::definition Tanım 4.1 (Uzaklık)
<span class="anker" id="satz-4-1"></span>

İki $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ vektörünün bir norma göre __uzaklığı__, farklarının normudur: $\lVert\mathbf{u}-\mathbf{v}\rVert$. Başka bir şey belirtilmemişse Öklid uzaklığı kastedilir.
:::

Bir uzaklıktan beklenen özellikler normun özelliklerinden çıkar: Uzaklık hiçbir zaman negatif değildir ve yalnızca aynı noktalar için sıfırdır; $\mathbf{v}-\mathbf{u}=-(\mathbf{u}-\mathbf{v})$ olduğundan $\mathbf{u}$ noktasından $\mathbf{v}$ noktasına olan uzaklık, $\mathbf{v}$ noktasından $\mathbf{u}$ noktasına olan uzaklıkla aynıdır; ve üçüncü bir $\mathbf{q}$ noktası üzerinden giden yol hiçbir zaman daha kısa değildir, $\lVert\mathbf{u}-\mathbf{v}\rVert\le\lVert\mathbf{u}-\mathbf{q}\rVert+\lVert\mathbf{q}-\mathbf{v}\rVert$. Bu, $\mathbf{u}-\mathbf{v}=(\mathbf{u}-\mathbf{q})+(\mathbf{q}-\mathbf{v})$ eşitliğine uygulanan (N3) üçgen eşitsizliğidir.

**Uzaklık ve iç çarpım.** Öklid uzaklığının karesi iç çarpımın hesap kurallarıyla açılırsa şu elde edilir:

<span class="anker" id="gl-4-1"></span>
$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=(\mathbf{u}-\mathbf{v})^{\top}(\mathbf{u}-\mathbf{v})=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v} . \tag{4.1}$$

Demek ki uzunluklar sabitken iç çarpım ne kadar büyükse uzaklık o kadar küçüktür. İkisi de benzerliği ölçer, yalnızca ters yönde.

::::beispiel [Sayısal örnek]
Daire 1 ile Daire 2 arasındaki fark $\mathbf{x}_1-\mathbf{x}_2=(20,\,1,\,2)^{\top}$ vektörüdür. Aralarındaki Öklid uzaklığı $\sqrt{405}\approx20{,}12$ (Şekil [18](#abb-18)), mutlak değerler toplamı normuna göre uzaklık $20+1+2=23$, maksimum normuna göre $20$ olur.

:::abbildung ml/k1rabstand 18
Daire 1 ile Daire 2 arasındaki Öklid uzaklığı: önce fark, sonra bu farkın uzunluğu.
:::

[(4.1)](#gl-4-1) eşitliğinin sağlaması için $\mathbf{u}=(1,\,2,\,2)^{\top}$ ve $\mathbf{v}=(2,\,0,\,1)^{\top}$ alınsın: Sol taraf $\lVert(-1,\,2,\,1)^{\top}\rVert^2=6$, sağ taraf $9+5-2\cdot4=6$ olur.
::::

⁠**Kısacası:** İki veri noktasının uzaklığı farklarının normudur; birbirine yakın olmak benzer olmak demektir.

### Uzaklıklar birimlere bağlıdır

<span class="anker" id="stufe-4-2"></span>

Az önceki sayısal örnekte $20{,}12$ uzaklığı, $20\,\mathrm m^2$ olan alan farkına neredeyse tam olarak eşittir. Uzaklığın karesindeki $405$ değerinin $400$ kadarı alandan gelir. Bir odalık ve iki kilometrelik fark pratikte hiç rol oynamaz, hem de yalnızca metrekare cinsinden alanlar büyük sayılar olduğu için.

Bunun sonucunu başka üç daire gösteriyor. Soru şu: B ve C dairelerinden hangisi A dairesine daha çok benzer?

$$\text{A}=(60,\,2)^{\top},\qquad \text{B}=(63,\,4)^{\top},\qquad \text{C}=(54,\,2)^{\top}\qquad(\text{alan: m}^2,\ \text{oda}).$$

Metrekare cinsinden $\lVert\text{A}-\text{B}\rVert=\sqrt{9+4}\approx3{,}61$ ve $\lVert\text{A}-\text{C}\rVert=\sqrt{36+0}=6$ olur: B daha yakındır. Alan $10\,\mathrm m^2$ büyüklüğündeki birimlerle ölçülürse $\text{A}=(6,\,2)^{\top}$, $\text{B}=(6{,}3;\ 4)^{\top}$, $\text{C}=(5{,}4;\ 2)^{\top}$ ve $\lVert\text{A}-\text{B}\rVert=\sqrt{0{,}09+4}\approx2{,}02$, $\lVert\text{A}-\text{C}\rVert=0{,}6$ olur: Şimdi C daha yakındır. Şekil [19](#abb-19) iki resmi de gösteriyor.

:::abbildung ml/k1einheiten 19
Aynı üç daire, solda alan $\mathrm m^2$ cinsinden, sağda $10\,\mathrm m^2$ büyüklüğündeki birimlerle. Bir resmin iki ekseni aynı ölçekte olduğundan bir doğru parçasının uzunluğu Öklid uzaklığıdır. Solda B, A noktasına daha yakındır (kesikli çizgi: merkezi A olan ve B noktasından geçen çember), sağda C.
:::

Mekanizma basittir. Uzaklığın karesinde her öznitelik için farkın karesi bulunur. Bir öznitelik başka bir birimle ölçülürse sayıları bir $c$ çarpanıyla çarpılır ve uzaklığın karesine katkısı $c^2$ ile çarpılır. Öteki özniteliklerin katkıları aynı kalır. Sayıları büyük olan bir öznitelik uzaklığı neredeyse tek başına belirler, sayıları küçük olan bir öznitelik ise neredeyse kaybolur.

⁠**Kısacası:** Örnekler arasındaki uzaklıklar özniteliklerin birimlerine bağlıdır; bir örneğe en çok hangi örneğin benzediği bir birim değişikliğiyle değişebilir.

:::hintergrund Birimlerin her seçimi bir ağırlıklandırmadır
Öklid uzaklığı metrekarelerin, odaların ve kilometrelerin karelerini toplar. Hesap olarak bu yapılabilir, çünkü bilgisayar yalnızca sayıları görür. Fiziksel olarak ise bu, farklı türden büyüklüklerin toplamıdır ve her birinin ne kadar sayılacağına birimler karar verir. Alanı $\mathrm m^2$ cinsinden veren, farkında olmadan $1\,\mathrm m^2$ farkın bir odalık fark kadar sayılmasına karar vermiştir. Doğanın önceden belirlediği doğru bir seçim yoktur. Seçimi bilinçli yapmak gerekir; bir sonraki yöntem de böyle bilinçli bir seçimdir.
:::

### Ortalamadan sapmalar

<span class="anker" id="stufe-4-3"></span>

Öznitelikleri karşılaştırılabilir kılmak için her öznitelik bütün örnekler boyunca kendi başına ele alınır. Daire tablosunda (Tablo [1](vektoren-daten-als-zahlenlisten.html#tab-1)) bunlar sütunlardır: Bütün dairelerin alanları $\mathbf{v}=(60,\,40,\,90,\,70)^{\top}\in\mathbb{R}^4$ vektörünü oluşturur. Böyle bir vektör bir özniteliğe aittir ve örnek sayısı kadar bileşeni vardır. Burada ona __öznitelik sütunu__ denir.

Karşılaştırma için alanların ne kadar büyük olduğu değil, birbirinden ne kadar farklı oldukları önemlidir. Bu yüzden her alan ortalamadan sapma olarak ölçülür. Elektrik mühendisliğinde bu adımın adı şudur: sabit (DC) bileşeni çıkarmak ve yalnızca değişken (AC) bileşeni tutmak.

:::definition Tanım 4.2 (Merkezlenmiş vektör)
<span class="anker" id="satz-4-2"></span>

Ortalaması $\bar v$ olan bir $\mathbf{v}\in\mathbb{R}^N$ için

<span class="anker" id="gl-4-2"></span>
$$\tilde{\mathbf{v}}=\mathbf{v}-\bar v\,\mathbf 1=(v_1-\bar v,\,\dots,\,v_N-\bar v)^{\top} \tag{4.2}$$

vektörüne __merkezlenmiş__ vektör denir. Bileşenleri ortalamadan sapmalardır.
:::

Sapmalar her zaman birbirini götürür: $\mathbf 1^{\top}\tilde{\mathbf{v}}=\mathbf 1^{\top}\mathbf{v}-\bar v\,\mathbf 1^{\top}\mathbf 1=N\bar v-\bar v\,N=0$. Yani merkezlenmiş vektörün ortalaması sıfırdır.

::::beispiel [Sayısal örnek]
$\mathbf{v}=(60,\,40,\,90,\,70)^{\top}$ alanlarının ortalaması $\bar v=65$ olur. Merkezlenmiş hâli $\tilde{\mathbf{v}}=(-5,\,-25,\,25,\,5)^{\top}$ vektörüdür ve sapmaların toplamı gerçekten sıfırdır (Şekil [20](#abb-20)). $(2,\,1,\,4,\,3)^{\top}$ oda sayılarının ortalaması $2{,}5$, merkezlenmiş hâli $(-0{,}5;\ -1{,}5;\ 1{,}5;\ 0{,}5)^{\top}$; $(3,\,1,\,6,\,2)^{\top}$ uzaklıklarının ortalaması $3$, merkezlenmiş hâli $(0,\,-2,\,3,\,-1)^{\top}$ olur.

:::abbildung ml/k1rzentriert 20
Alanların ortalaması ve ortalamadan sapmaların toplamı, $\mathrm m^2$ cinsinden.
:::
::::

⁠**Kısacası:** Merkezleme her bileşenden ortalamayı çıkarır; geriye toplamı sıfır olan sapmalar kalır.

### Standart sapma

<span class="anker" id="stufe-4-4"></span>

Bir özniteliğin ne kadar dalgalandığı sapmalarının büyüklüğünden görülür. Bir bileşenin tipik mutlak değeri etkin değerdir (alt kesim [3.6](normen-die-groe-eines-vektors.html#stufe-3-6)). Etkin değer merkezlenmiş vektöre uygulanınca ortalamadan tipik sapmayı verir. Elektrik mühendisliğinin diliyle: değişken (AC) bileşenin etkin değeri.

:::definition Tanım 4.3 (Standart sapma)
<span class="anker" id="satz-4-3"></span>

Bir $\mathbf{v}\in\mathbb{R}^N$ vektörünün __standart sapması__, merkezlenmiş vektörünün etkin değeridir:

<span class="anker" id="gl-4-3"></span>
$$\operatorname{std}(\mathbf{v})=\operatorname{rms}(\tilde{\mathbf{v}})=\frac{\lVert\mathbf{v}-\bar v\,\mathbf 1\rVert}{\sqrt N}=\sqrt{\frac1N\sum_{i=1}^N(v_i-\bar v)^2} . \tag{4.3}$$
:::

Standart sapmanın birimi özniteliğin birimiyle aynıdır. Standart sapma ancak ve ancak bütün bileşenler eşitse sıfırdır. Birçok metin [(4.3)](#gl-4-3) içinde $N$ yerine $N-1$ ile böler. Örnek sayısı büyükse fark küçüktür. Bu seri $N$ ile böler ve bir yerde farklı yapılması gerekirse bunu ayrıca belirtir.

::::beispiel [Sayısal örnek]
$(-5,\,-25,\,25,\,5)^{\top}$ merkezlenmiş alanlarının kareleri toplamı $1\,300$, dolayısıyla $\operatorname{std}(\mathbf{v})=\sqrt{325}\approx18{,}03\,\mathrm m^2$ olur (Şekil [21](#abb-21)). Aynı biçimde odalar için $\sqrt{5/4}\approx1{,}118$, uzaklıklar için $\sqrt{14/4}\approx1{,}871$ km bulunur.

:::abbildung ml/k1rstd 21
Alanların standart sapması: Sapmaların karesi alınır, ortalamaları alınır, karekök alınır. $\sqrt{325}\approx18{,}03$ sonucunun birimi $\mathrm m^2$ olur.
:::
::::

⁠**Kısacası:** Standart sapma ortalamadan sapmaların etkin değeridir, yani bir özniteliğin tipik dalgalanmasıdır.

:::hintergrund Sabit bileşen ile değişken bileşen gücü paylaşır
Bir vektör, $\bar v\,\mathbf 1$ sabit bileşeni ile $\tilde{\mathbf{v}}$ değişken bileşeninin toplamıdır. Uzunluğun karesi için iç çarpımın hesap kurallarına göre şu geçerlidir:

$$\lVert\bar v\,\mathbf 1+\tilde{\mathbf{v}}\rVert^2=\bar v^2\,\mathbf 1^{\top}\mathbf 1+2\,\bar v\,\mathbf 1^{\top}\tilde{\mathbf{v}}+\lVert\tilde{\mathbf{v}}\rVert^2=N\bar v^2+0+\lVert\tilde{\mathbf{v}}\rVert^2 ,$$

çünkü sapmaların toplamı sıfırdır. $N$ ile bölününce bu, $\operatorname{rms}(\mathbf{v})^2=\bar v^2+\operatorname{std}(\mathbf{v})^2$ olur. Bu, bir karma akımdaki paylaşımın aynısıdır: Karma akımın bir dirençteki gücü, sabit bileşenin gücü ile değişken bileşenin gücünün toplamıdır. Alanlar için: $\operatorname{rms}^2=(3600+1600+8100+4900)/4=4550=65^2+325$.
:::

### Standartlaştırma

<span class="anker" id="stufe-4-5"></span>

Artık her öznitelik kendi tipik dalgalanmasıyla ölçülebilir. “Ortalamanın $25\,\mathrm m^2$ üstünde” yerine “ortalamanın $1{,}39$ standart sapma üstünde” denir. Bu dilde her öznitelik, başlangıçta hangi birimle ölçülmüş olursa olsun, aynı büyüklük mertebesindedir.

:::definition Tanım 4.4 (Standartlaştırma)
<span class="anker" id="satz-4-4"></span>

Öznitelik sütununun ortalaması $\bar x_j$ ve standart sapması $s_j>0$ olan bir $j$ özniteliği, her değerin yerine

<span class="anker" id="gl-4-4"></span>
$$z_{ij}=\frac{x_{ij}-\bar x_j}{s_j},\qquad i=1,\dots,N, \tag{4.4}$$

konarak __standartlaştırılır__. $z_{ij}$ sayılarına standartlaştırılmış değerler denir.
:::

Standartlaştırılmış öznitelik sütununun ortalaması $0$, standart sapması $1$ olur, çünkü merkezleme ortalamayı sıfır yapar, $s_j$ ile bölme de tipik sapmayı bir yapar. Değerlerin artık birimi yoktur.

::::beispiel [Sayısal örnek 1] daire veri kümesi
$65$, $2{,}5$, $3$ ortalamaları ve $18{,}03$, $1{,}118$, $1{,}871$ standart sapmalarıyla dört daire şunlara dönüşür:

$$\begin{aligned} \mathbf{z}_1&\approx(-0{,}28;\ -0{,}45;\ 0)^{\top}, & \mathbf{z}_2&\approx(-1{,}39;\ -1{,}34;\ -1{,}07)^{\top},\\ \mathbf{z}_3&\approx(1{,}39;\ 1{,}34;\ 1{,}60)^{\top}, & \mathbf{z}_4&\approx(0{,}28;\ 0{,}45;\ -0{,}53)^{\top}. \end{aligned}$$

Üç özniteliğin hepsi artık aynı sayı aralığında hareket ediyor.
::::

::::beispiel [Sayısal örnek 2] A, B ve C
Üç dairenin (alt kesim [4.2](#stufe-4-2)) ortalama alanı $59\,\mathrm m^2$, standart sapması $\sqrt{14}\approx3{,}74\,\mathrm m^2$; ortalama oda sayısı $8/3$, standart sapması $\sqrt{8/9}\approx0{,}943$ olur. Standartlaştırmadan sonra $\lVert\text A-\text B\rVert\approx2{,}27$ ve $\lVert\text A-\text C\rVert\approx1{,}60$ bulunur. Demek ki A'ya en çok C benzer ve bu hüküm artık alanın birimine bağlı değildir.
::::

Birimin hesaptan düşmesi genel olarak geçerlidir:

:::satz Teorem 4.5 (Standartlaştırılmış değerler birime bağlı değildir)
<span class="anker" id="satz-4-5"></span>

Bir öznitelik başka bir birime çevrilirse, yani $\alpha>0$ ve $\beta$ sayılarıyla bütün $i$ için $v_i'=\alpha\,v_i+\beta$ olursa, standartlaştırılmış değerleri aynı kalır.
:::

:::beweis Birimden bağımsızlık
Ortalama $\bar v'=\frac1N\sum_i(\alpha\,v_i+\beta)=\alpha\,\bar v+\beta$ olur, sapmalar da $v_i'-\bar v'=\alpha\,(v_i-\bar v)$. [(4.3)](#gl-4-3) uyarınca bu durumda $\operatorname{std}(\mathbf{v}')=|\alpha|\operatorname{std}(\mathbf{v})=\alpha\operatorname{std}(\mathbf{v})$ olur. [(4.4)](#gl-4-4) kesrinde $\alpha$ sadeleşir, $\beta$ ise merkezlemede zaten kaybolmuştur.
:::

$\beta$ terimi, sıfır noktası kaydırılmış dönüşümleri de kapsar, örneğin Celsius dereceden Fahrenheit dereceye.

⁠**Kısacası:** Standartlaştırma her özniteliği ortalamadan sapma olarak, kendi standart sapmasının katları cinsinden ölçer; bundan sonra uzaklıklar artık birimlere bağlı değildir.

:::hintergrund Ölçek olarak neden tam da standart sapma?
Her öznitelik için, birim değiştiğinde değerler arasındaki farklarla aynı çarpan kadar değişen bir ölçeğe ihtiyaç vardır. O zaman bu ölçek hesaptan sadeleşir. Özniteliğin değerleri arasındaki farklardan hesaplanan ve özniteliğin birimini taşıyan her büyüklük bunu sağlar: standart sapma, ama en küçük değerden en büyük değere kadar olan değişim aralığı da. Standart sapmanın olağan seçim olmasının nedeni, yalnızca en uçtaki iki değeri değil, bütün değerleri hesaba katmasıdır.

Standartlaştırmanın bir uzaklığa ne yaptığı, standartlaştırılmış iki $\mathbf{z}_a$ ve $\mathbf{z}_b$ örneği birbirinden çıkarılınca görülür. Ortalama düşer, $z_{aj}-z_{bj}=(x_{aj}-x_{bj})/s_j$, ve geriye şu kalır:

$$\lVert\mathbf{z}_a-\mathbf{z}_b\rVert^2=\sum_{j=1}^d\frac{(x_{aj}-x_{bj})^2}{s_j^2} .$$

Yani standartlaştırılmış değerlerin uzaklığı, $j$ özniteliğindeki farkın karesinin $1/s_j^2$ ağırlığıyla sayıldığı sıradan uzaklıktır. A ve B daireleri için bu $3^2/14+2^2/(8/9)=9/14+9/2\approx5{,}14$, karekökü de yukarıdaki gibi $2{,}27$ olur.

Ama standartlaştırmanın kendisi de bir karardır. Uzaklıkta her özniteliğe aynı ağırlığı verir, soruyla hiç ilgisi olmayan bir özniteliğe bile. Ayrıca bütün örneklerde aynı değeri alan bir özniteliğin standart sapması sıfırdır ve bu öznitelik standartlaştırılamaz; ama böyle bir öznitelik örnekleri birbirinden ayırt da etmez ve hiçbir uzaklığa katkı yapmaz.
:::

:::aufgabe Alıştırma 9 ★ Sabit bileşen ve değişken bileşen
<span class="anker" id="aufg-9"></span>

Bir sinyalin örnek değerleri $\mathbf{x}=(1,\,3,\,1,\,-1)^{\top}$ olsun. Ortalamayı, merkezlenmiş vektörü, standart sapmayı ve etkin değeri hesaplayın. $\operatorname{rms}(\mathbf{x})^2=\bar x^2+\operatorname{std}(\mathbf{x})^2$ eşitliğini doğrulayın.

:::loesung
Ortalama $\bar x=(1+3+1-1)/4=1$, merkezlenmiş vektör $\tilde{\mathbf{x}}=(0,\,2,\,0,\,-2)^{\top}$ olur. Standart sapma $\sqrt{(0+4+0+4)/4}=\sqrt2\approx1{,}414$, etkin değer $\sqrt{(1+9+1+1)/4}=\sqrt3\approx1{,}732$ olur. Sağlama: $\operatorname{rms}^2=3=1^2+(\sqrt2)^2=\bar x^2+\operatorname{std}^2$. Sabit bileşen ile değişken bileşen, $3$ büyüklüğündeki “gücü” $1:2$ oranında paylaşır.
:::
:::

:::aufgabe Alıştırma 10 ★★ Daire 1'e en çok hangisi benzer?
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Daire 1'in Daire 2, 3 ve 4'e Öklid uzaklıklarını tablodaki değerlerle hesaplayın (Tablo [1](vektoren-daten-als-zahlenlisten.html#tab-1)). Daire 2'ye olan uzaklığın karesinin ne kadarlık bir payı alandan gelir?

</li>

<li>

Aynı uzaklıkları standartlaştırılmış değerlerle hesaplayın (alt kesim [4.5](#stufe-4-5)). Daire 2'ye olan uzaklığın karesinin ne kadarlık bir payı şimdi alandan gelir?

</li>

<li>

Her iki durumda Daire 1'e en çok hangi daire benzer? Cevabı değilse, standartlaştırma burada neyi değiştirmiştir?

</li>

</ol>

:::loesung
(a) Tablodaki değerlerle:

$$\begin{aligned} \lVert\mathbf{x}_1-\mathbf{x}_2\rVert&=\sqrt{20^2+1^2+2^2}=\sqrt{405}\approx20{,}12,\\ \lVert\mathbf{x}_1-\mathbf{x}_3\rVert&=\sqrt{30^2+2^2+3^2}=\sqrt{913}\approx30{,}22,\\ \lVert\mathbf{x}_1-\mathbf{x}_4\rVert&=\sqrt{10^2+1^2+1^2}=\sqrt{102}\approx10{,}10 . \end{aligned}$$

Daire 2'ye olan uzaklığın karesindeki $405$'in $400$'ü alandan gelir, yani $98{,}8$ %.

(b) Standartlaştırılmış vektörlerle (alt kesim [4.5](#stufe-4-5)) $\mathbf{z}_1-\mathbf{z}_2\approx(1{,}109;\ 0{,}894;\ 1{,}069)^{\top}$ olur; bileşenlerin kareleri $1{,}231$, $0{,}800$ ve $1{,}143$. Uzaklık $\sqrt{3{,}174}\approx1{,}78$ olur. Aynı biçimde $\lVert\mathbf{z}_1-\mathbf{z}_3\rVert\approx2{,}92$ ve $\lVert\mathbf{z}_1-\mathbf{z}_4\rVert\approx1{,}18$ bulunur. Alanın, Daire 2'ye olan uzaklığın karesindeki payı artık $1{,}231/3{,}174\approx38{,}8$ % olur.

(c) Her iki durumda da Daire 1'e en çok Daire 4 benzer; onu Daire 2 ve Daire 3 izler. Sıra burada değişmez, çünkü bu küçük veri kümesinde büyük dairelerin odaları da daha fazladır ve bu daireler merkezden daha uzaktadır; üç özniteliğin hepsi aşağı yukarı aynı hikâyeyi anlatır. Değişen, Daire 4'ün *neden* en çok benzediğidir: Ham değerlerde neredeyse yalnızca alan belirleyicidir, standartlaştırılmış değerlerde ise üç özniteliğin hepsi aşağı yukarı eşit katkı yapar. Cevabın yine de aynı kalması bu verilere özgü bir rastlantıdır; A, B ve C dairelerinde (alt kesim [4.2](#stufe-4-2)) cevap değişmişti.
:::
:::

:::aufgabe Alıştırma 11 ★★ Celsius mu, Fahrenheit mi?
<span class="anker" id="aufg-11"></span>

Dört gün boyunca öğlen $10$, $20$, $15$ ve $25$ $^\circ$C ölçülmüştür.

<ol class="al">

<li>

Değerleri Fahrenheit dereceye çevirin ($F=1{,}8\,C+32$). Her iki birimde ortalamayı ve standart sapmayı hesaplayın.

</li>

<li>

Her iki birimde standartlaştırılmış değerleri hesaplayın ve karşılaştırın.

</li>

<li>

Bir öznitelik negatif bir çarpanla, örneğin $v_i'=-v_i$ ile dönüştürülürse standartlaştırılmış değerlere ne olur?

</li>

</ol>

:::loesung
(a) Fahrenheit cinsinden değerler $1{,}8\cdot10+32=50$, $68$, $59$ ve $77$ olur. Celsius cinsinden ortalama $17{,}5$, standart sapma $\sqrt{(56{,}25+6{,}25+6{,}25+56{,}25)/4}=\sqrt{31{,}25}\approx5{,}590$ olur; Fahrenheit cinsinden ortalama $63{,}5=1{,}8\cdot17{,}5+32$, standart sapma $\approx10{,}062=1{,}8\cdot5{,}590$ olur. Eklenen $32$ terimi yalnızca ortalamayı kaydırır, $1{,}8$ çarpanı ise standart sapmayı da gerer.

(b) Her iki birimde de standartlaştırılmış değerler $\approx(-1{,}342;\ 0{,}447;\ -0{,}447;\ 1{,}342)$ olur. Alt kesim [4.5](#stufe-4-5) içindeki teorem de bunu gerektirir: Eklenen terim merkezlemede düşer, çarpan standart sapmayla sadeleşir.

(c) $v_i'=-v_i$ ile ortalamadan bütün sapmalar $-1$ ile çarpılır, standart sapma ise $|-1|=1$ ile. Demek ki standartlaştırılmış değerler işaret değiştirir. Örnekler arasındaki uzaklıklar için bunun bir önemi yoktur, çünkü $\lVert-\mathbf{u}\rVert=\lVert\mathbf{u}\rVert$; veri kümesi yalnızca yansıtılır.
:::
:::
