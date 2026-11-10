---
title: En iyi yaklaşık çözüm
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Bölüm 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15220400
summary: Bilinmeyenden çok denklemi olan bir denklem sisteminin çoğunlukla çözümü yoktur.
tags: artık, en iyi yaklaşık çözümü, normal denklemler, en küçük kareler doğrusu
lang: tr
---

<span class="anker" id="stufe-3"></span>

:::zweck
Bilinmeyenden çok denklemi olan bir denklem sisteminin çoğunlukla çözümü yoktur. Bu kesim bunun yerine sistemi olabildiğince iyi sağlayan bilinmeyenleri arıyor. Bunlar daha küçük ve her zaman çözülebilen bir denklem sisteminden çıkar; bunun nedeni de yine bir dik açıdır.
:::

### Geriye bakış: bilinmeyenden çok denklem

<span class="anker" id="stufe-3-1"></span>

[Bölüm 1, Kesim 12.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-gleichungssysteme.html#stufe-12-5)'te alan için bir $w_1$ ağırlığı ve oda sayısı için bir $w_2$ ağırlığı dairelerin fiyatlarını tam olarak tutturmalıydı. Dört dairenin hepsi alındığında bu, $\mathbf{A}\mathbf{w}=\mathbf{y}$ sistemidir; burada

$$\mathbf{A}=\begin{pmatrix}60&2\\40&1\\90&4\\70&3\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}200\\130\\290\\240\end{pmatrix}\ \text{bin avro}.$$

Sistemin çözümü yoktur. Sütun bakışıyla bu şu demektir: $\mathbf{A}$ matrisinin sütunları $\mathbb{R}^4$ uzayında bir düzlemi, yani sütun uzayını gerer ve $\mathbf{y}$ fiyat vektörü bu düzlemde değildir. $\mathbf{w}$ ne seçilirse seçilsin, geriye bir kalan artar.

:::definition Tanım 3.1 (Artık)
<span class="anker" id="satz-3-1"></span>

Bir $\mathbf{A}\mathbf{x}=\mathbf{y}$ denklem sistemi ve herhangi bir $\mathbf{x}$ vektörü için

<span class="anker" id="gl-3-1"></span>
$$\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x} \tag{3.1}$$

vektörüne $\mathbf{x}$ için __artık__ denir.
:::

Türkçe sözcük tam da “geriye kalan” demektir; uluslararası terim (*residual*) de Latincede “kalan” anlamına gelen sözcükten türemiştir. Artık vektörü ancak ve ancak $\mathbf{x}$ sistemi çözüyorsa sıfırdır. [Bölüm 1, Kesim 3.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3-5)'teki hata vektörünün ters işaretlisidir; uzunluğu aynıdır.

::::beispiel [Sayısal örnek]
[Bölüm 1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html)'deki $\mathbf{w}=(3,\,10)^{\top}$ ağırlıklarıyla $\mathbf{A}\mathbf{w}=(200,\,130,\,310,\,240)^{\top}$ olur ve artık $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{w}=(0,\,0,\,-20,\,0)^{\top}$, uzunluğu $20$. Üç fiyat tam olarak tutturulur, biri $20$ bin avro ıskalanır.
::::

⁠**Kısacası:** $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ artığı, bir $\mathbf{x}$ vektörünün $\mathbf{A}\mathbf{x}=\mathbf{y}$ sistemini çözerken geride bıraktığı kalandır.

### En iyi yaklaşık çözüm

<span class="anker" id="stufe-3-2"></span>

Artık vektörü sıfır olamıyorsa hiç değilse olabildiğince küçük olmalıdır. Bunun ölçüsü artığın Öklid uzunluğudur.

Problem geometrik olarak düşünülebilir. $\mathbf{x}$ bütün vektörleri dolaşırken $\mathbf{A}\mathbf{x}$, [Bölüm 1, Kesim 7.4](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-4)'e göre $\mathbf{A}$ matrisinin sütun uzayını dolaşır. $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert$ uzaklığı, $\mathbf{y}$ noktasının sütun uzayındaki $\mathbf{A}\mathbf{x}$ noktasına uzaklığıdır. Demek ki aranan, sütun uzayının $\mathbf{y}$ noktasına en yakın noktasıdır (Şekil [6](#abb-6)). Önceki kesimde sütun uzayı bir doğruydu; şimdi bir düzlem ya da daha yüksek boyutlu bir gerilen alt uzay olabilir.

:::definition Tanım 3.2 (En iyi yaklaşık çözüm)
<span class="anker" id="satz-3-2"></span>

Bir $\hat{\mathbf{x}}$ vektörü şu koşulu sağlıyorsa $\mathbf{A}\mathbf{x}=\mathbf{y}$ sisteminin __en iyi yaklaşık çözümü__ olarak adlandırılır:

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert\le\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\qquad\text{her }\mathbf{x}\text{ için} . \tag{3.2}$$
:::

Uzunluk, karesinin en küçük olduğu yerde en küçüktür; kare de artığın bileşenlerinin karelerinin toplamıdır. Bu yüzden *en küçük kareler yöntemine* göre çözümden de söz edilir. Sistemin tam bir çözümü varsa o aynı zamanda en iyi yaklaşık çözümdür, çünkü artığının uzunluğu sıfırdır.

:::abbildung ml/k2ebene 6
$\mathbb{R}^3$ uzayında bir düzlem üzerine izdüşüm. $\mathbf{a}_1=(1,0,1)^{\top}$ ve $\mathbf{a}_2=(0,1,1)^{\top}$ sütunları $x_3=x_1+x_2$ düzlemini (mavi) gerer. $\mathbf{y}=(1,1,1)^{\top}$ noktası bu düzlemde değildir. Düzlemin en yakın noktası $\hat{\mathbf{y}}=(\tfrac23,\tfrac23,\tfrac43)^{\top}$ noktasıdır; $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(\tfrac13,\tfrac13,-\tfrac13)^{\top}$ artığı düzleme diktir.
:::

::::beispiel [Sayısal örnek]
[Bölüm 1, Kesim 7.4](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-4)'teki $\mathbf{H}$ matrisinin sütunları $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ ve $\mathbf{a}_2=(0,\,1,\,1)^{\top}$ vektörleridir. Sütun uzayı, üçüncü bileşeni ilk ikisinin toplamı olan bütün vektörlerin oluşturduğu düzlemdir. $\mathbf{y}=(1,\,1,\,1)^{\top}$ vektörü bu düzlemde değildir, dolayısıyla $\mathbf{H}\mathbf{x}=\mathbf{y}$ sisteminin çözümü yoktur. $\mathbf{x}=(1,\,0)^{\top}$ ile artık $(0,\,1,\,0)^{\top}$ olur ve uzunluğu $1$; $\mathbf{x}=(1,\,1)^{\top}$ ile artık $(0,\,0,\,-1)^{\top}$ olur, uzunluğu yine $1$. Daha iyisinin mümkün olup olmadığını sonraki alt kesim cevaplıyor.
::::

⁠**Kısacası:** En iyi yaklaşık çözüm artığı olabildiğince kısa yapar; geometrik olarak, sütun uzayının $\mathbf{y}$ noktasına en yakın noktasını arar.

### Normal denklemler

<span class="anker" id="stufe-3-3"></span>

Doğru durumunda en yakın nokta dikme ayağıydı: Artık vektörü doğruya dikti. Bir sütun uzayı için de aynı koşul akla yatkındır: Artık vektörü sütun uzayının her vektörüne dik olmalıdır. Bu bir denklem sistemi olarak yazılabilir.

:::herleitung Normal denklemler
Sütun uzayının her vektörü, sütunların bir $\sum_jz_j\mathbf{a}_j$ doğrusal bileşimidir. $\mathbf{r}$ her sütuna dikse böyle her doğrusal bileşime de diktir, çünkü $\bigl(\sum_jz_j\mathbf{a}_j\bigr)^{\top}\mathbf{r}=\sum_jz_j\,\mathbf{a}_j^{\top}\mathbf{r}$. Demek ki her sütun için şunu istemek yeterlidir:

$$\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=0\qquad j=1,\dots,n\text{ için} .$$

$\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$ sayıları $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$ vektörünün bileşenleridir, çünkü $\mathbf{A}^{\top}$ matrisinin satırları $\mathbf{A}$ matrisinin sütunlarıdır. $n$ koşul birlikte yani $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=\mathbf{0}$ olur; çarpım açılınca $\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$.
:::

:::definition Tanım 3.3 (Normal denklemler)
<span class="anker" id="satz-3-3"></span>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ olmak üzere $\mathbf{A}\mathbf{x}=\mathbf{y}$ sistemine ait __normal denklemler__ şunlardır:

<span class="anker" id="gl-3-3"></span>
$$\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y} . \tag{3.3}$$
:::

Buradaki “normal” sözcüğü, bir düzlemin normal vektöründe olduğu gibi “dik” anlamına gelir: Denklemler artığın sütun uzayına dik olmasını ister. $\mathbf{A}^{\top}\mathbf{A}$ matrisi, sütunların [Bölüm 1, Kesim 10.4](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-4)'teki Gram matrisidir; kare bir matristir ve bilinmeyen sayısı kadar satırı vardır. $m$ denklemli büyük ve çözümsüz bir sistemden $n$ denklemli küçük bir sistem elde edilir. Tek bir $\mathbf{a}$ sütunu için burada $\mathbf{a}^{\top}\mathbf{a}\,\hat x=\mathbf{a}^{\top}\mathbf{y}$ durur, yani önceki kesimdeki formül.

::::beispiel [Sayısal örnek]
$\mathbf{H}$ ve $\mathbf{y}=(1,\,1,\,1)^{\top}$ için şu bulunur:

$$\mathbf{H}^{\top}\mathbf{H}=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad \mathbf{H}^{\top}\mathbf{y}=\begin{pmatrix}2\\2\end{pmatrix}.$$

Her eleman iki sütunun ya da bir sütunla $\mathbf{y}$ vektörünün iç çarpımıdır (Şekil [7](#abb-7)).

:::abbildung ml/k2rnormal 7
Normal denklemlerin iki elemanı iç çarpım olarak: $\mathbf{H}^{\top}\mathbf{H}$ matrisinin $(1,2)$ elemanı $\mathbf{a}_1^{\top}\mathbf{a}_2$, $\mathbf{H}^{\top}\mathbf{y}$ vektörünün birinci bileşeni $\mathbf{a}_1^{\top}\mathbf{y}$ iç çarpımıdır.
:::

$2\hat x_1+\hat x_2=2$ ve $\hat x_1+2\hat x_2=2$ normal denklemlerinin çözümü $\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$ olur. Böylece $\hat{\mathbf{y}}=\mathbf{H}\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}$ ve artık $\mathbf{r}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$ bulunur. Sağlama: $\mathbf{a}_1^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$ ve $\mathbf{a}_2^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$. Artığın uzunluğu $\sqrt{3/9}\approx0{,}577$; önceki alt kesimdeki iki denemeden daha kısa.
::::

⁠**Kısacası:** $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ normal denklemleri, artığın bütün sütunlara dik olmasını ister.

### Normal denklemler neden en iyi çözümü verir

<span class="anker" id="stufe-3-4"></span>

Dik bir artığın en yakın noktaya ait olması, doğru durumunda Pisagor teoreminden çıkmıştı. Aynı gerekçe burada da işler: Pisagor teoremi hatayı, $\mathbf{x}$ seçimiyle etkilenebilen bir kısma ve etkilenemeyen bir kısma ayırır.

:::satz Teorem 3.4 (Normal denklemler en iyi yaklaşık çözümü verir)
<span class="anker" id="satz-3-4"></span>

$\hat{\mathbf{x}}$ normal denklemleri çözüyorsa her $\mathbf{x}$ vektörü için şu geçerlidir:

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert^2+\lVert\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})\rVert^2 . \tag{3.4}$$

Dolayısıyla $\hat{\mathbf{x}}$ bir en iyi yaklaşık çözümdür. Tersine, her en iyi yaklaşık çözüm normal denklemleri çözer ve bütün en iyi yaklaşık çözümler aynı $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}$ noktasını verir.
:::

:::beweis En iyi yaklaşık çözüm
$\mathbf{y}-\mathbf{A}\mathbf{x}=(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})+\mathbf{A}(\hat{\mathbf{x}}-\mathbf{x})$ biçiminde ayrılır. Birinci terim $\hat{\mathbf{x}}$ için $\mathbf{r}$ artığıdır, ikincisi sütun uzayındadır. Normal denklemlere göre $\mathbf{r}$ sütun uzayına diktir ve Pisagor teoremi [(3.4)](#gl-3-4) bağıntısını verir. Sağdaki ikinci terim hiçbir zaman negatif değildir, dolayısıyla her $\mathbf{x}$ için $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\ge\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert$ olur.

$\mathbf{x}$ de bir en iyi yaklaşık çözümse iki uzunluk eşittir ve [(3.4)](#gl-3-4) bağıntısı $\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})=\mathbf{0}$ olmasını zorunlu kılar. O zaman $\mathbf{A}\mathbf{x}=\mathbf{A}\hat{\mathbf{x}}$ olur; yani ikisi aynı noktayı ve aynı artığı verir ve $\mathbf{x}$ de normal denklemleri sağlar.
:::

::::beispiel [Sayısal örnek]
$\mathbf{H}$, $\mathbf{y}=(1,\,1,\,1)^{\top}$ ve $\mathbf{x}=(1,\,0)^{\top}$ için $\lVert\mathbf{y}-\mathbf{H}\mathbf{x}\rVert^2=1$ olur. [(3.4)](#gl-3-4) bağıntısının sağ tarafı $\lVert\mathbf{r}\rVert^2=\tfrac13$ artı $\lVert\mathbf{H}(\tfrac13,\,-\tfrac23)^{\top}\rVert^2=\lVert(\tfrac13,\,-\tfrac23,\,-\tfrac13)^{\top}\rVert^2=\tfrac69$, toplam $\tfrac13+\tfrac23=1$.
::::

⁠**Kısacası:** Pisagor teoremi hatanın karesini, hiçbir $\mathbf{x}$ seçiminin küçültemeyeceği dik artığa ve sütun uzayında bulunan, $\hat{\mathbf{x}}$ için sıfırlanan bir kısma ayırır.

:::hintergrund Neyin etkilenebildiği, neyin etkilenemediği
[(3.4)](#gl-3-4) formülü, doğru koşulun neden tam da dik konum olduğunu açıklar. Her $\mathbf{A}\mathbf{x}$ adayı sütun uzayındadır. $\mathbf{y}$ noktasına olan uzaklık birbirine dik iki parçadan oluşur: sütun uzayında $\mathbf{A}\mathbf{x}$ noktasından $\hat{\mathbf{y}}$ noktasına giden bir parça ve buna dik olan, $\hat{\mathbf{y}}$ noktasından $\mathbf{y}$ noktasına giden $\mathbf{r}$ parçası. Birinci parça $\mathbf{x}$ seçimiyle istenildiği gibi değiştirilebilir, özellikle sıfıra indirilebilir. İkincisi $\mathbf{x}$ vektörüne hiç bağlı değildir: $\mathbf{y}$ vektörünün, sütunların hiçbir doğrusal bileşimle ulaşamadığı kısmıdır. En iyi yaklaşık çözüm, tam olarak etkilenebilen parçayı sıfır yapan çözümdür. İki parçanın Pisagor teoremine göre toplanması ve birbirini dengeleyememesi aralarındaki dik açıdan kaynaklanır.
:::

### En iyi yaklaşık çözüm ne zaman tektir

<span class="anker" id="stufe-3-5"></span>

Normal denklemler kare bir sistemdir. Tam olarak bir çözümü olup olmadığı, $\mathbf{A}^{\top}\mathbf{A}$ matrisinin tersinir olup olmamasına bağlıdır. Bunu da $\mathbf{A}$ matrisinin sütunları belirler.

:::satz Teorem 3.5 ($\mathbf{A}^{\top}\mathbf{A}$ matrisinin tersinirliği)
<span class="anker" id="satz-3-5"></span>

$\mathbf{A}^{\top}\mathbf{A}$ matrisi ancak ve ancak $\mathbf{A}$ matrisinin sütunları doğrusal bağımsızsa tersinirdir. O zaman en iyi yaklaşık çözüm tektir:

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y} . \tag{3.5}$$
:::

:::beweis Tersinirlik
[Bölüm 1, Kesim 13.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5)'e göre $\mathbf{A}^{\top}\mathbf{A}$ kare matrisi ancak ve ancak çekirdeği yalnızca sıfır vektörünü içeriyorsa tersinirdir. $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$ olsun. O zaman $\mathbf{z}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=0$, yani $\lVert\mathbf{A}\mathbf{z}\rVert^2=0$ ve $\mathbf{A}\mathbf{z}=\mathbf{0}$ olur. Tersine, $\mathbf{A}\mathbf{z}=\mathbf{0}$ ise hemen $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$ çıkar. Demek ki iki çekirdek aynıdır. $\mathbf{A}$ matrisinin çekirdeği ise ancak ve ancak $\mathbf{A}$ matrisinin sütunları doğrusal bağımsızsa yalnızca sıfır vektörünü içerir.
:::

Sütunlar doğrusal bağımlıysa sonsuz sayıda en iyi yaklaşık çözüm vardır. Bunlardan birine, $\mathbf{A}\hat{\mathbf{x}}$ değişmeden, $\mathbf{A}$ matrisinin çekirdeğinden herhangi bir vektör eklenebilir. Önceki alt kesimdeki teoremin gösterdiği gibi, en yakın $\hat{\mathbf{y}}$ noktası yine de tektir. Bu, [Bölüm 1, Kesim 13.6](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-6) ile uyumludur: Bağımlı öznitelikler ağırlıkları belirsiz kılar, tahminleri değil.

::::beispiel [Sayısal örnek 1]
$\mathbf{H}$ matrisinin sütunları doğrusal bağımsızdır ve $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ matrisinin tersi $\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$ olur. [(3.5)](#gl-3-5) ile $\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(2,\,2)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$ bulunur, yukarıdakiyle aynı.
::::

::::beispiel [Sayısal örnek 2]
$\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ ve $\mathbf{y}=(1,\,1)^{\top}$ için sütunlar bağımlıdır. Normal denklemler $\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)\hat{\mathbf{x}}=(3,\,6)^{\top}$ olur, yani iki kez aynı $\hat x_1+2\hat x_2=\tfrac35$ denklemi. Bu doğrunun her noktası bir en iyi yaklaşık çözümdür, örneğin $(\tfrac35,\,0)^{\top}$ ya da $(0,\,\tfrac3{10})^{\top}$. Hepsi aynı $\hat{\mathbf{y}}=(\tfrac35,\,\tfrac65)^{\top}$ noktasını verir: $\mathbf{y}$ vektörünün $(1,\,2)^{\top}$ doğrultusundaki doğru üzerine izdüşümünü.
::::

⁠**Kısacası:** Sütunlar doğrusal bağımsızsa $\mathbf{A}^{\top}\mathbf{A}$ tersinirdir ve $\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$ en iyi yaklaşık çözümü tektir; aksi halde sonsuz sayıda en iyi yaklaşık çözüm vardır ve hepsi aynı en yakın noktayı verir.

### Üç noktadan geçen bir doğru

<span class="anker" id="stufe-3-6"></span>

Kuram şimdi tamamlanmıştır ve gündelik bir probleme uygulanabilir. $(t,\,y)=(0,\,1)$, $(1,\,2)$ ve $(2,\,4)$ ölçüm noktaları bir $y=x_1+x_2\,t$ doğrusuyla betimlenmek isteniyor. Üç nokta ortak bir doğru üzerinde değildir. En iyi uyan $x_1$ eksen kesişimi ve $x_2$ eğimi aranıyor.

Her ölçüm noktası bir $x_1+x_2\,t_i=y_i$ denklemi verir. [Bölüm 1, Kesim 8.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-5)'teki gibi eksen kesişimi için bir birler sütunu eklenince bu, şu sistemdir:

$$\mathbf{A}\mathbf{x}=\mathbf{y}\qquad\text{burada}\qquad \mathbf{A}=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}1\\2\\4\end{pmatrix}.$$

Artığın bileşenleri, ölçüm noktalarının doğruya $y$ doğrultusunda ölçülen düşey uzaklıklarıdır (Şekil [8](#abb-8)). En iyi yaklaşık çözüm bunların karelerinin toplamını olabildiğince küçük yapar. Böyle bir doğruya __en küçük kareler doğrusu__ denir.

:::abbildung ml/k2ausgleich 8
$(0,1)$, $(1,2)$ ve $(2,4)$ ölçüm noktalarına uydurulan en küçük kareler doğrusu. Kırmızı parçalar artığın bileşenleri, yani noktaların doğruya $y$ doğrultusundaki düşey uzaklıklarıdır. Doğru bunların karelerinin toplamını olabildiğince küçük yapar; burada bu toplam $\tfrac1{36}+\tfrac19+\tfrac1{36}=\tfrac16$.
:::

::::beispiel [Sayısal örnek]
Burada

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&3\\3&5\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}7\\10\end{pmatrix},\qquad (\mathbf{A}^{\top}\mathbf{A})^{-1}=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix},$$

dolayısıyla $\hat{\mathbf{x}}=\tfrac16(35-30,\ -21+30)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$. $\mathbf{A}^{\top}\mathbf{A}$ ve $\mathbf{A}^{\top}\mathbf{y}$ elemanları ölçüm noktaları üzerinden alınan toplamlardır; bunlardan ikisini Şekil [9](#abb-9) gösteriyor. En küçük kareler doğrusu $y=\tfrac56+\tfrac32\,t$ olur. Doğrunun ölçüm yerlerindeki değerleri $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\,\tfrac73,\,\tfrac{23}6)^{\top}$, artık $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$ ve karelerinin toplamı $\tfrac16$. Sağlama: $\mathbf{A}^{\top}\mathbf{r}=(\tfrac16-\tfrac13+\tfrac16,\ 0-\tfrac13+\tfrac13)^{\top}=(0,\,0)^{\top}$.

Sağlamanın birinci bileşeninin ayrı bir anlamı vardır. $\mathbf{A}$ matrisinin birinci sütunu birler sütunudur ve $\mathbf{1}^{\top}\mathbf{r}=0$ şu demektir: Artıkların toplamı sıfırdır. Doğru ortalamada ne fazla yukarıda ne fazla aşağıdadır. Denk olarak, ölçüm noktalarının ağırlık merkezinden geçer; burada bu merkez $(\bar t,\,\bar y)=(1,\,\tfrac73)$: $\tfrac56+\tfrac32\cdot1=\tfrac73$.

:::abbildung ml/k2rausgleich 9
En küçük kareler doğrusunun normal denklemlerinden iki eleman, $(t_i,\,y_i)=(0,1)$, $(1,2)$, $(2,4)$ üç ölçüm noktası üzerinden alınan toplamlar olarak.
:::
::::

⁠**Kısacası:** En küçük kareler doğrusu, bütün ölçüm noktalarının doğru üzerinde olmasını isteyen sistemin en iyi yaklaşık çözümüdür; birler sütunu varsa artıkların toplamı sıfırdır.

:::hintergrund Bir diziyi başka bir diziden olabildiğince iyi taklit etmek
Aynı hesapla sayı dizileri için tahmin kuralları kurulur. Bir açık yüzme havuzu, $n$ günündeki $d[n]$ dondurma satışını, $n$ günündeki ve ondan önceki günlerdeki $x[n]$ ziyaretçi sayısından, $\sum_kh_k\,x[n-k]$ kuralı ve $h_0,\dots,h_{K-1}$ ağırlıklarıyla olabildiğince iyi taklit etmek istiyor. Her $n$ günü için bu, $K$ tane $h_k$ bilinmeyeni için bir denklemdir; çok sayıda gün için de aşırı belirli bir $\mathbf{X}\mathbf h=\mathbf d$ sistemi. $\mathbf{X}$ matrisinin $n$ numaralı satırı $x[n],x[n-1],\dots,x[n-K+1]$ değerlerini içerir. $\mathbf{X}^{\top}\mathbf{X}\mathbf h=\mathbf{X}^{\top}\mathbf d$ normal denklemlerinde $\mathbf{X}^{\top}\mathbf{X}$ matrisinin $(k,l)$ elemanı $\sum_nx[n-k]\,x[n-l]$ toplamıdır; bu, dizinin başındaki ve sonundaki kenar etkileri dışında $x$ dizisinin $l-k$ kaymasında kendisiyle çapraz ilintisi, yani özilintisidir. $\mathbf{X}^{\top}\mathbf d$ vektöründe $d$ ile $x$ dizilerinin çapraz ilintisi bulunur. Bunlar tam olarak [Bölüm 1, Kesim 2.4](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-4)'teki kaydırılmış dizilerin iç çarpımlarıdır. En iyi kuralın $d[n]-\sum_kh_k\,x[n-k]$ artığı, [(3.3)](#gl-3-3) uyarınca kaydırılmış her ziyaretçi dizisine diktir: Kuralın taklit edemediği şeyin, tahminini oluştururken kullandığı dizilerin hiçbiriyle ortak bir yanı yoktur.
:::

### Daireler: Bölüm 1'in açık bıraktığı soru

<span class="anker" id="stufe-3-7"></span>

Şimdi kesimin başındaki soru cevaplanabilir. Aranan, dört fiyatı olabildiğince iyi tutturan alan ve oda sayısı ağırlıklarıdır.

::::beispiel [Sayısal örnek]
İlk alt kesimdeki $\mathbf{A}\mathbf{w}=\mathbf{y}$ sistemi için şu bulunur:

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}18\,200&730\\730&30\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}60\,100\\2\,410\end{pmatrix}.$$

Elemanlardan ikisinin hesabını Şekil [10](#abb-10) gösteriyor.

:::abbildung ml/k2rwohnungen 10
Dairelerin normal denklemlerinden iki eleman iç çarpım olarak: $\mathbf{a}_1=(60,40,90,70)^{\top}$ alan sütunu, $\mathbf{a}_2=(2,1,4,3)^{\top}$ oda sütunu, $\mathbf{y}=(200,130,290,240)^{\top}$ fiyat vektörüdür.
:::

İki sütun doğrusal bağımsızdır; determinant $18\,200\cdot30-730^2=13\,100$. [Bölüm 1, Kesim 11.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-3)'teki ters matrisle şu bulunur:

$$\hat{\mathbf{w}}=\frac1{13\,100}\begin{pmatrix}30&-730\\-730&18\,200\end{pmatrix}\begin{pmatrix}60\,100\\2\,410\end{pmatrix}=\frac1{13\,100}\begin{pmatrix}43\,700\\-11\,000\end{pmatrix}=\begin{pmatrix}437/131\\-110/131\end{pmatrix}\approx\begin{pmatrix}3{,}336\\-0{,}840\end{pmatrix}.$$

Tahmin edilen fiyatlar $\mathbf{A}\hat{\mathbf{w}}\approx(198{,}47;\ 132{,}60;\ 296{,}87;\ 230{,}99)^{\top}$, artık ise

$$\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{w}}=\frac{20}{131}\,(10,\,-17,\,-45,\,59)^{\top}\approx(1{,}53;\ -2{,}60;\ -6{,}87;\ 9{,}01)^{\top}$$

olur ve uzunluğu $\lVert\mathbf{r}\rVert\approx11{,}72$. [Bölüm 1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html)'deki $(3,\,10)^{\top}$ ağırlıkları üç fiyatı tam olarak tutturuyordu, ama uzunluğu $20$ olan bir artık bırakıyordu. En iyi yaklaşık çözüm hiçbir fiyatı tam olarak tutturmaz, ama toplamda belirgin biçimde daha az sapar. Sağlama: $\mathbf{A}^{\top}\mathbf{r}=\frac{20}{131}(600-680-4050+4130,\ 20-17-180+177)^{\top}=\mathbf{0}$.
::::

⁠**Kısacası:** Daireler için en iyi yaklaşık çözüm $\hat{\mathbf{w}}\approx(3{,}336;\ -0{,}840)^{\top}$ ağırlıklarıdır; bunların artığı, $11{,}72$ uzunluğuyla, üç fiyatı tam olarak tutturan her artıktan belirgin biçimde kısadır.

:::hintergrund Oda ağırlığı neden negatif
Oda sayısı için negatif bir ağırlık ilk bakışta yanlış görünür: Daha çok oda fiyatı düşürmemelidir. Hesap yine de doğrudur ve nedeni verilerdedir. Bu dört dairede alan ve oda sayısı birlikte büyür: Daire ne kadar büyükse o kadar çok odası vardır. Bu yüzden $\mathbf{A}$ matrisinin iki sütunu neredeyse aynı doğrultuyu gösterir; [Bölüm 1, Kesim 5.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-2)'ye göre aralarındaki açının kosinüsü $730/\sqrt{18\,200\cdot30}\approx0{,}988$, açı yani yalnızca yaklaşık $8{,}9^\circ$. En iyi bileşim alan sütunundan çok alır ve dairelerin bu ortak orandan sapmalarını dengelemek için oda sütunundan biraz geri çıkarır. Aynı alanda daha çok oda burada daha küçük odalar demektir ve bu, bir fiyatı gerçekten düşürebilir; bunun doğru olup olmadığını ise dört daire gösteremez. [Bölüm 1, Kesim 13.6](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-6)'daki gibi şu geçerlidir: Öznitelikler neredeyse aynı bilgiyi taşıyorsa tek tek ağırlıklar az şey söyler, tahminler ise çok şey.
:::

:::aufgabe Alıştırma 7 ★ Elle normal denklemler
<span class="anker" id="aufg-7"></span>

$x_1=1$, $x_2=2$, $x_1+x_2=6$ sisteminin çözümü yoktur.

<ol class="al">

<li>

Sistemi $\mathbf{A}\mathbf{x}=\mathbf{y}$ biçiminde yazın, normal denklemleri kurun ve çözün.

</li>

<li>

Artığı hesaplayın ve iki sütuna da dik olduğunu doğrulayın. En iyi yaklaşık çözüm üç denklemin her birini ne kadar ıskalıyor?

</li>

</ol>

:::loesung
(a) $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ ve $\mathbf{y}=(1,\,2,\,6)^{\top}$ ile $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ ve $\mathbf{A}^{\top}\mathbf{y}=(1+6,\ 2+6)^{\top}=(7,\,8)^{\top}$ olur. $2\hat x_1+\hat x_2=7$, $\hat x_1+2\hat x_2=8$ normal denklemlerinin çözümü şudur:

$$\hat{\mathbf{x}}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}7\\8\end{pmatrix}=\frac13\begin{pmatrix}6\\9\end{pmatrix}=\begin{pmatrix}2\\3\end{pmatrix}.$$

(b) $\mathbf{A}\hat{\mathbf{x}}=(2,\,3,\,5)^{\top}$ ve $\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}=(-1,\,-1,\,1)^{\top}$ olur. Sağlama: $\mathbf{a}_1^{\top}\mathbf{r}=-1+0+1=0$ ve $\mathbf{a}_2^{\top}\mathbf{r}=0-1+1=0$. Üç denklemin her biri tam olarak $1$ kadar ıskalanır: $1$ yerine $\hat x_1=2$, $2$ yerine $\hat x_2=3$, $6$ yerine $\hat x_1+\hat x_2=5$. En iyi yaklaşık çözüm çelişkiyi eşit olarak dağıtır; $\lVert\mathbf{r}\rVert^2=3$.
:::
:::

:::aufgabe Alıştırma 8 ★★ Bir en küçük kareler doğrusu
<span class="anker" id="aufg-8"></span>

$(1,\,2)$, $(2,\,3)$ ve $(3,\,5)$ noktalarına uyan $y=x_1+x_2\,t$ en küçük kareler doğrusunu bulun. Artığı hesaplayın, $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ eşitliğini doğrulayın ve doğrunun üç noktanın ağırlık merkezinden geçtiğini gösterin.

:::loesung
$\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&2\\1&3\end{smallmatrix}\Bigr)$ ve $\mathbf{y}=(2,\,3,\,5)^{\top}$ ile şu bulunur:

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&6\\6&14\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}10\\23\end{pmatrix},\qquad \hat{\mathbf{x}}=\frac16\begin{pmatrix}14&-6\\-6&3\end{pmatrix}\begin{pmatrix}10\\23\end{pmatrix}=\frac16\begin{pmatrix}2\\9\end{pmatrix}=\begin{pmatrix}1/3\\3/2\end{pmatrix}.$$

En küçük kareler doğrusu $y=\tfrac13+\tfrac32\,t$ olur; ölçüm yerlerindeki değerleri $\tfrac{11}6$, $\tfrac{10}3$, $\tfrac{29}6$. Artık $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$ olur ve $\mathbf{A}^{\top}\mathbf{r}=\bigl(\tfrac16-\tfrac13+\tfrac16,\ \tfrac16-\tfrac23+\tfrac12\bigr)^{\top}=(0,\,0)^{\top}$. Ağırlık merkezi $(\bar t,\,\bar y)=(2,\,\tfrac{10}3)$ ve $\tfrac13+\tfrac32\cdot2=\tfrac{10}3$: Doğru ağırlık merkezinden geçer. Bu, $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ eşitliğinin birinci bileşeninden çıkar: Artıkların toplamı sıfırdır, dolayısıyla $\bar y=\hat x_1+\hat x_2\,\bar t$ olur.
:::
:::

:::aufgabe Alıştırma 9 ★★ Taban fiyat ve metrekare fiyatı
<span class="anker" id="aufg-9"></span>

Dört dairenin fiyatı yalnızca alanlarına göre, bir taban fiyatla birlikte tahmin edilmek isteniyor: $y\approx x_1+x_2\cdot\text{alan}$.

<ol class="al">

<li>

$\mathbf{A}$ matrisini birler sütunuyla kurun ve normal denklemleri çözün.

</li>

<li>

Artığı ve uzunluğunu hesaplayın. Son alt kesimdeki sonuçla karşılaştırın.

</li>

</ol>

:::loesung
(a) Matrisin sütunları birler sütunu ile alan sütunudur:

$$\mathbf{A}=\begin{pmatrix}1&60\\1&40\\1&90\\1&70\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}4&260\\260&18\,200\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}860\\60\,100\end{pmatrix}.$$

Determinant $4\cdot18\,200-260^2=72\,800-67\,600=5\,200$ olur ve şu bulunur:

$$\hat{\mathbf{x}}=\frac1{5\,200}\begin{pmatrix}18\,200&-260\\-260&4\end{pmatrix}\begin{pmatrix}860\\60\,100\end{pmatrix}=\frac1{5\,200}\begin{pmatrix}26\,000\\16\,800\end{pmatrix}=\begin{pmatrix}5\\42/13\end{pmatrix}\approx\begin{pmatrix}5\\3{,}231\end{pmatrix}.$$

Taban fiyat $5$ bin avrodur; buna metrekare başına yaklaşık $3{,}23$ bin avro eklenir.

(b) Tahmin edilen fiyatlar $5+\tfrac{42}{13}\cdot\text{alan}$ olur; artık ise şudur:

$$\mathbf{r}=\tfrac1{13}\,(15,\,-55,\,-75,\,115)^{\top}\approx(1{,}15;\ -4{,}23;\ -5{,}77;\ 8{,}85)^{\top},\qquad \lVert\mathbf{r}\rVert=\tfrac1{13}\sqrt{22\,100}\approx11{,}44 .$$

Artıkların toplamı, birler sütununun gerektirdiği gibi sıfırdır. Alan ve oda sayısıyla $\lVert\mathbf{r}\rVert\approx11{,}72$ bulunmuştu; demek ki taban fiyat ve alan, yine iki bilinmeyenle, biraz daha iyi uyar. Hangi iki sütunun seçildiği sütun uzayını, dolayısıyla en yakın noktayı değiştirir.
:::
:::

:::aufgabe Alıştırma 10 ★★★ Birler sütunu olmadan artıklar
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Gösterin: $\mathbf{A}$ matrisinin sütun uzayı $\mathbf{1}$ birler vektörünü içeriyorsa en iyi yaklaşık çözümün artığının bileşenlerinin toplamı sıfırdır.

</li>

<li>

Son alt kesimdeki dairelerin artığı üzerinde, birler sütunu olmadan artıkların toplamının genel olarak sıfır olmadığını doğrulayın.

</li>

</ol>

:::loesung
(a) $\mathbf{1}$ sütun uzayındaysa en iyi yaklaşık çözümün artığı, normal denklemlere göre $\mathbf{1}$ vektörüne diktir, çünkü sütun uzayının tamamına diktir. Dolayısıyla $\mathbf{1}^{\top}\mathbf{r}=\sum_ir_i=0$ olur.

(b) Dairelerin artığı $\tfrac{20}{131}(10,\,-17,\,-45,\,59)^{\top}$ olur, bileşenlerinin toplamı $\tfrac{20}{131}(10-17-45+59)=\tfrac{140}{131}\approx1{,}07\ne0$. Birler sütunu olmadığında $\mathbf{1}$ burada sütun uzayında değildir ve artıkların birbirini dengelemesi gerekmez.
:::
:::
