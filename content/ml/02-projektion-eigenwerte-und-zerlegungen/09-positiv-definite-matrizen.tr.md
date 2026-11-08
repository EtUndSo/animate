---
title: Pozitif tanımlı matrisler
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
knoten: Temeller 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15220900
summary: Bir kuadratik form, orijin dışında her yerde pozitifse bir çanaktır.
tags: pozitif tanımlı, pozitif yarı tanımlı, belirsiz, Rayleigh bölümü
lang: tr
---

<span class="anker" id="stufe-8"></span>

:::zweck
Bir kuadratik form, orijin dışında her yerde pozitifse bir çanaktır. Bu kesim bu özelliğe bir ad veriyor ve onu sınamaya yarayan testleri tanıtıyor: özdeğerler, pivotlar ve determinantlar üzerinden. Buna iki sonuç eklenir: bir formun birim çember üzerindeki en büyük ve en küçük değeri ve yalnızca çanakların sahip olduğu bir ayrışım.
:::

### Pozitif tanımlı ve pozitif yarı tanımlı

<span class="anker" id="stufe-8-1"></span>

Kesim [5.3](quadratische-formen.html#stufe-5-3)'teki çanak ile oluk bir noktada ayrılır: Çanak orijin dışında her yerde pozitiftir, oluk ise yalnızca negatif değildir. Bu iki özelliğin yerleşik adları vardır.

:::definition Tanım 8.1 (Pozitif tanımlı, pozitif yarı tanımlı)
<span class="anker" id="satz-8-1"></span>

Simetrik bir $\mathbf{A}\in\mathbb{R}^{n\times n}$ matrisi için

<span class="anker" id="gl-8-1"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}>0\qquad\text{her}\ \mathbf{x}\ne\mathbf{0}\ \text{için} , \tag{8.1}$$

geçerliyse bu matrise __pozitif tanımlı__, her $\mathbf{x}$ için $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}\ge0$ geçerliyse __pozitif yarı tanımlı__ denir.
:::

Simetri tanımın bir parçasıdır. Kuadratik form için bu bir kısıtlama değildir; Kesim [5.2](quadratische-formen.html#stufe-5-2)'ye göre zaten yalnızca simetrik kısım önemlidir. Ama sonraki alt kesimdeki testlerin geçerli olması için simetri gereklidir. Her pozitif tanımlı matris aynı zamanda pozitif yarı tanımlıdır.

⁠**Sayısal örnek:** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ pozitif tanımlıdır, çünkü Kesim [5.4](quadratische-formen.html#stufe-5-4)'e göre $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=5(x_1+0{,}4x_2)^2+1{,}2x_2^2$ olur ve bu ifade yalnızca $x_2=0$ ve dolayısıyla $x_1=0$ ise sıfırdır. $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ matrisinin formu $x_1^2+4x_1x_2+4x_2^2=(x_1+2x_2)^2\ge0$ olur; bu matris pozitif yarı tanımlıdır, ama pozitif tanımlı değildir, çünkü $\mathbf{x}=(2,\,-1)^{\top}$ için form sıfırdır. Grafiği, vadi tabanı $(2,\,-1)^{\top}$ doğrultusunda olan bir oluktur.

⁠**Kısacası:** Pozitif tanımlı demek, kuadratik formun orijin dışında pozitif, yani bir çanak olması demektir; pozitif yarı tanımlı demek, hiçbir yerde negatif olmaması demektir.

### Özdeğer testi

<span class="anker" id="stufe-8-2"></span>

[(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4) asal eksen biçimi soruyu hemen cevaplar: Bir $\sum_i\lambda_ic_i^2$ toplamı, bütün $\lambda_i$ pozitifse koordinatların her seçimi için pozitiftir, aksi halde değildir.

:::satz Teorem 8.2 (Özdeğer testi)
<span class="anker" id="satz-8-2"></span>

Simetrik bir matris ancak ve ancak bütün özdeğerleri pozitifse pozitif tanımlıdır ve ancak ve ancak hiçbir özdeğeri negatif değilse pozitif yarı tanımlıdır.
:::

:::beweis Özdeğer testi
Bütün $\lambda_i>0$ ve $\mathbf{x}\ne\mathbf{0}$ ise $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}\ne\mathbf{0}$ olur, çünkü $\mathbf{Q}$ tersinirdir; o zaman [(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4) uyarınca $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2>0$. Tersine, bir $\lambda_i\le0$ özdeğeri varsa $\mathbf{x}=\mathbf{q}_i$ özvektörü için form $\mathbf{q}_i^{\top}\mathbf{A}\mathbf{q}_i=\lambda_i\le0$ olur ve $\mathbf{A}$ pozitif tanımlı değildir. Yarı tanımlılık için aynı yol, $>$ yerine $\ge$ ile izlenir.
:::

Simetrik bir matrisin hem pozitif hem negatif özdeğerleri varsa formu bazı doğrultularda pozitif, bazılarında negatiftir: bir eyer. Böyle bir matrise __belirsiz__ denir. Buna karşılık bütün özdeğerleri negatif olan bir matrise negatif tanımlı denir; formu bir kubbedir.

⁠**Sayısal örnek:** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ matrisinin özdeğerleri $6$ ve $1$: pozitif tanımlı. $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ matrisinin özdeğerleri $5$ ve $0$: pozitif yarı tanımlı. $\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ matrisinin bütün elemanları pozitiftir, ama özdeğerleri $4$ ve $-2$: belirsiz, çünkü $\mathbf{x}=(1,\,-1)^{\top}$ için form $1-6+1=-4$ olur. Demek ki elemanların pozitif olması tanımlılık hakkında hiçbir şey söylemez.

⁠**Kısacası:** Simetrik bir matris ancak ve ancak bütün özdeğerleri pozitifse pozitif tanımlıdır; pozitif ve negatif özdeğerler bir arada bir eyer verir.

:::hintergrund Simetri neden tanımın parçasıdır
Bazı kitaplar pozitif tanımlılığı kuadratik form üzerinden, bazıları özdeğerler üzerinden tanımlar. Simetrik matrislerde bu, teoreme göre aynı şeydir; simetrik olmayanlarda değildir. $\bigl(\begin{smallmatrix}2&-5\\0&2\end{smallmatrix}\bigr)$ matrisinin, bir üçgen matris olarak, $2$ ve $2$ özdeğerleri vardır; ikisi de pozitiftir. Ama kuadratik formu $2x_1^2-5x_1x_2+2x_2^2$ olur ve $\mathbf{x}=(1,\,1)^{\top}$ için değeri $2-5+2=-1$. Nedeni şudur: Form yalnızca, özdeğerleri $4{,}5$ ve $-0{,}5$ olan $\bigl(\begin{smallmatrix}2&-2{,}5\\-2{,}5&2\end{smallmatrix}\bigr)$ simetrik kısmını görür; özdeğerler ise matrisin tamamına aittir. Bu yüzden kavramı simetri olmadan kullanan, hangi tanımı kastettiğini her zaman söylemelidir.
:::

### Özdeğer gerektirmeyen testler

<span class="anker" id="stufe-8-3"></span>

Büyük matrislerde özdeğerleri hesaplamak zahmetlidir. Kesim [5.4](quadratische-formen.html#stufe-5-4)'teki tam kareye tamamlama özdeğer gerektirmeyen bir test verir; ondan da determinantlarla çalışan ikinci bir test çıkar.

:::satz Teorem 8.3 (Pozitif tanımlılık için testler)
<span class="anker" id="satz-8-3"></span>

Simetrik bir $\mathbf{A}\in\mathbb{R}^{n\times n}$ matrisi için şunlar denktir:

<ol class="rm">

<li>

$\mathbf{A}$ pozitif tanımlıdır;

</li>

<li>

satır değişimi yapılmadan uygulanan Gauss eleme yöntemi $n$ pozitif pivot verir;

</li>

<li>

bütün baş asal minörler pozitiftir: Sol üstteki $k\times k$ alt matrislerin determinantları $k=1,\dots,n$ için sıfırdan büyüktür.

</li>

</ol>

$n=2$ ve $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$ için bu şu demektir: $a>0$ ve $ac-b^2>0$.
:::

$n=2$ için bu [(5.3)](quadratische-formen.html#gl-5-3) bağıntısıdır: Pivotlar $a$ ve $c-b^2/a$ olur, form ancak ve ancak ikisi de pozitifse bir çanaktır ve $a>0$ iken $c-b^2/a>0$ koşulu $ac-b^2>0$ koşuluna denktir. Daha büyük $n$ için her eleme adımı, Kesim [5.4](quadratische-formen.html#stufe-5-4)'teki arka plan kutusunda olduğu gibi bir değişkeni bir kareye tamamlar. Sol üstteki $k\times k$ alt matrisin determinantı ilk $k$ pivotun çarpımıdır; bu yüzden pivotların hepsi ancak ve ancak baş asal minörlerin hepsi pozitifse pozitiftir. Determinant testine Sylvester ölçütü de denir.

İki uyarı. Birincisi, tek başına $\det\mathbf{A}>0$ yetmez: $\operatorname{diag}(-1;\,-3)$ matrisinin determinantı $3$, ama matris negatif tanımlıdır. İkincisi, test yarı tanımlılığa doğrudan aktarılamaz: $\operatorname{diag}(0;\,-1)$ matrisinin baş asal minörleri $0$ ve $0$, ikisi de negatif değildir; matris yine de pozitif yarı tanımlı değildir.

⁠**Sayısal örnek:**

$$\mathbf{A}=\begin{pmatrix}2&1&0\\1&2&1\\0&1&2\end{pmatrix}$$

matrisinin baş asal minörleri $2$, $\det\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)=3$ ve $\det\mathbf{A}=2\cdot3-1\cdot2=4$ olur; hepsi pozitiftir: $\mathbf{A}$ pozitif tanımlıdır. Pivotlar $2$, $\tfrac32$ ve $\tfrac43$, yani ardışık minörlerin bölümleridir. Sağlama: Özdeğerler $2-\sqrt2$, $2$ ve $2+\sqrt2$ olur, hepsi pozitiftir ve çarpımları $(4-2)\cdot2=4$.

⁠**Kısacası:** Simetrik bir matris ancak ve ancak bütün pivotları ya da bütün baş asal minörleri pozitifse pozitif tanımlıdır; $2\times2$ için bu $a>0$ ve $ac-b^2>0$ demektir.

### Gram matrisleri pozitif yarı tanımlıdır

<span class="anker" id="stufe-8-4"></span>

Temeller 1, Kesim 10'da $\mathbf{X}^{\top}\mathbf{X}$ ve $\mathbf{X}\mathbf{X}^{\top}$ Gram matrisleri, bu bölümde da normal denklemlerdeki $\mathbf{A}^{\top}\mathbf{A}$ ortaya çıktı. Bunlar her zaman pozitif yarı tanımlıdır ve nedeni basittir: Kuadratik formları bir uzunluk karesidir.

:::satz Teorem 8.4 (Gram matrisleri)
<span class="anker" id="satz-8-4"></span>

Her $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisi için $\mathbf{A}^{\top}\mathbf{A}$ pozitif yarı tanımlıdır. Bu matris ancak ve ancak $\mathbf{A}$ matrisinin sütunları doğrusal bağımsızsa pozitif tanımlıdır.
:::

:::beweis Gram matrisleri
$\mathbf{A}^{\top}\mathbf{A}$ simetriktir ve $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}\mathbf{x})^{\top}(\mathbf{A}\mathbf{x})=\lVert\mathbf{A}\mathbf{x}\rVert^2\ge0$ olur. Bu ifade ancak ve ancak $\mathbf{A}\mathbf{x}=\mathbf{0}$ ise sıfırdır. Sütunlar bağımsızsa bu yalnızca $\mathbf{x}=\mathbf{0}$ için olur.
:::

Aynısı, sütunlar yerine satırlarla $\mathbf{A}\mathbf{A}^{\top}$ için de geçerlidir. Teorem Kesim [3.5](die-beste-naherungslosung.html#stufe-3-5)'i sonradan açıklar: Sütunlar bağımsızsa $\mathbf{A}^{\top}\mathbf{A}$ pozitif tanımlıdır, yani bütün özdeğerleri pozitiftir ve tersinirdir.

⁠**Sayısal örnek:** $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ matrisinin özdeğerleri $3$ ve $1$: pozitif tanımlı; bu, $\mathbf{H}$ matrisinin bağımsız sütunlarıyla uyumludur. $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ için $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$ olur; determinantı $0$, özdeğerleri $25$ ve $0$: pozitif yarı tanımlı, pozitif tanımlı değil.

⁠**Kısacası:** $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf{A}\mathbf{x}\rVert^2$ olduğundan $\mathbf{A}^{\top}\mathbf{A}$ her zaman pozitif yarı tanımlıdır; sütunlar bağımsızsa pozitif tanımlıdır.

### Birim çember üzerinde en büyük ve en küçük değer

<span class="anker" id="stufe-8-5"></span>

Bir kuadratik form $\mathbf{x}$ vektörünün uzunluğunun karesiyle büyür. Farklı doğrultularda ne kadar hızlı büyüdüğü, yalnızca $1$ uzunluğundaki vektörler yerine konduğunda görülür. Form hangi doğrultuda en büyüktür?

:::satz Teorem 8.5 (Bir kuadratik formun uç değerleri)
<span class="anker" id="satz-8-5"></span>

$\mathbf{A}$, en küçük özdeğeri $\lambda_{\min}$ ve en büyük özdeğeri $\lambda_{\max}$ olan simetrik bir matris olsun. Her $\mathbf{x}\ne\mathbf{0}$ vektörü için şu geçerlidir:

<span class="anker" id="gl-8-2"></span>
$$\lambda_{\min}\le\frac{\mathbf{x}^{\top}\mathbf{A}\mathbf{x}}{\mathbf{x}^{\top}\mathbf{x}}\le\lambda_{\max} . \tag{8.2}$$

En büyük değer $\lambda_{\max}$ özdeğerine ait bir özvektörde, en küçük değer $\lambda_{\min}$ özdeğerine ait bir özvektörde alınır.
:::

:::beweis Uç değerler
$\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$ ile, $\mathbf{Q}$ uzunlukları koruduğu için $\mathbf{x}^{\top}\mathbf{x}=\mathbf{c}^{\top}\mathbf{c}=\sum_ic_i^2$ ve ayrıca $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2$ olur. Demek ki bölüm şudur:

$$\frac{\sum_i\lambda_ic_i^2}{\sum_ic_i^2}=\sum_i\lambda_i\,g_i\qquad\text{burada}\qquad g_i=\frac{c_i^2}{\sum_lc_l^2}\ge0,\quad \sum_ig_i=1 .$$

Bu, özdeğerlerin ağırlıklı bir ortalamasıdır ve bir ortalama her zaman ortalaması alınan değerlerin en küçüğü ile en büyüğü arasındadır. $\mathbf{x}=\mathbf{q}_i$ için ağırlıklardan yalnızca $g_i=1$ kalır ve bölüm $\lambda_i$ olur.
:::

[(8.2)](#gl-8-2) içindeki bölüme __Rayleigh bölümü__ denir. $\lVert\mathbf{x}\rVert=1$ için bu bölüm kuadratik formun kendisidir: Birim çember üzerinde form, en küçük ile en büyük özdeğer arasında kalır.

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ için Rayleigh bölümü $\mathbf{e}_1$ noktasında $5$, $\mathbf{e}_2$ noktasında $2$, $(1,\,1)^{\top}/\sqrt2$ noktasında $\tfrac{5+4+2}2=5{,}5$ ve $(1,\,-1)^{\top}/\sqrt2$ noktasında $\tfrac{5-4+2}2=1{,}5$ olur. Bütün değerler $1$ ile $6$ arasındadır. $6$ değerine $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$ noktasında ulaşılır: $\tfrac15(20+8+2)=6$. Bölüm $\mathbf{x}$ vektörünün uzunluğuna bağlı değildir; Şekil [21](#abb-21) onu $\mathbf{x}=(1,\,1)^{\top}$ için köklü ifadeler olmadan hesaplıyor.

:::abbildung ml/k2rrayleigh 21
$\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ matrisinin $\mathbf{x}=(1,1)^{\top}$ noktasındaki Rayleigh bölümü: Pay ve payda toplam olarak; $\tfrac{11}2=5{,}5$ bölümü $1$ ve $6$ özdeğerleri arasındadır.
:::

⁠**Kısacası:** Birim çember üzerinde bir kuadratik form en küçük ile en büyük özdeğer arasında kalır ve bu uç değerler öz doğrultularda alınır.

### Cholesky ayrışımı

<span class="anker" id="stufe-8-6"></span>

Tam kareye tamamlama, pozitif tanımlı bir formu karelerin toplamı olarak yazar. Karelerin içindeki ifadeler bir vektörde toplanırsa form bu vektörün uzunluğunun karesi olur. Buradan matrisin bir ayrışımı çıkar.

:::satz Teorem 8.6 (Cholesky ayrışımı)
<span class="anker" id="satz-8-6"></span>

Simetrik bir $\mathbf{A}$ matrisi ancak ve ancak, köşegen elemanları pozitif olan bir $\mathbf L$ alt üçgen matrisiyle şöyle yazılabiliyorsa pozitif tanımlıdır:

<span class="anker" id="gl-8-3"></span>
$$\mathbf{A}=\mathbf L\mathbf L^{\top} . \tag{8.3}$$

Bu $\mathbf L$ matrisi tektir ve $\mathbf{A}$ matrisinin Cholesky çarpanı olarak adlandırılır.
:::

$\mathbf{A}=\mathbf L\mathbf L^{\top}$ ise $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf L^{\top}\mathbf{x}\rVert^2$ olur; bu bir kareler toplamıdır ve $\mathbf L$ tersinir olduğundan yalnızca $\mathbf{x}=\mathbf{0}$ için sıfırdır. Bu, yönlerden biridir. Öbür yön, yani her pozitif tanımlı matrisin böyle bir çarpanı olduğu, tam kareye tamamlamadır: $n=2$ için çarpan [(5.3)](quadratische-formen.html#gl-5-3) bağıntısından okunur,

$$\mathbf L=\begin{pmatrix}\sqrt a&0\\b/\sqrt a&\sqrt{c-b^2/a}\end{pmatrix},$$

daha büyük $n$ için de tamamlama değişken değişken sürdürülür. Temeller 1, Kesim 14.5'e göre $\det\mathbf{A}=\det\mathbf L\cdot\det\mathbf L^{\top}=(l_{11}\cdots l_{nn})^2$ olur.

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$ için $a=4$, $b=2$, $c=5$, dolayısıyla $l_{11}=2$, $l_{21}=1$ ve $l_{22}=\sqrt{5-1}=2$ olur:

$$\mathbf L=\begin{pmatrix}2&0\\1&2\end{pmatrix},\qquad \mathbf L\mathbf L^{\top}=\begin{pmatrix}4&2\\2&1+4\end{pmatrix}=\mathbf{A} .$$

Form $4x_1^2+4x_1x_2+5x_2^2=(2x_1+x_2)^2+(2x_2)^2$ olur; karelerin içindeki iki ifade $\mathbf L^{\top}\mathbf{x}$ vektörünün bileşenleridir. Determinant $20-4=16=(2\cdot2)^2$.

⁠**Kısacası:** Her pozitif tanımlı matris, $\mathbf L$ bir alt üçgen matris olmak üzere $\mathbf L\mathbf L^{\top}$ biçimindedir; bu ayrışım, matris biçiminde tam kareye tamamlamadır.

:::aufgabe Alıştırma 24 ★ Tanımlılığı sınamak
<span class="anker" id="aufg-24"></span>

Matrislerin pozitif tanımlı mı, pozitif yarı tanımlı mı, negatif tanımlı mı, yoksa belirsiz mi olduğuna iki farklı testle karar verin:

$$\mathbf{A}_1=\begin{pmatrix}3&1\\1&2\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}2&6\\6&18\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&2\end{pmatrix},\qquad \mathbf{A}_4=\begin{pmatrix}-2&1\\1&-1\end{pmatrix}.$$

:::loesung
<ul>

<li>

$\mathbf{A}_1$: $a=3>0$ ve $ac-b^2=6-1=5>0$: pozitif tanımlı. Özdeğerler: iz $5$, determinant $5$, $\lambda=\tfrac{5\pm\sqrt5}2\approx3{,}62$ ve $1{,}38$, ikisi de pozitif.

</li>

<li>

$\mathbf{A}_2$: $a=2>0$, ama $ac-b^2=36-36=0$. Özdeğerler $20$ ve $0$: pozitif yarı tanımlı, tanımlı değil. Tam kareye tamamlanınca: $2(x_1+3x_2)^2$, bir oluk.

</li>

<li>

$\mathbf{A}_3$: $ac-b^2=2-9=-7<0$; özdeğerlerin çarpımı $-7$, dolayısıyla işaretleri farklıdır: belirsiz. Özdeğerler $\tfrac{3\pm\sqrt{37}}2\approx4{,}54$ ve $-1{,}54$ olur.

</li>

<li>

$\mathbf{A}_4$: $a=-2<0$, pozitif tanımlı değil. $-\mathbf{A}_4=\bigl(\begin{smallmatrix}2&-1\\-1&1\end{smallmatrix}\bigr)$ için $a=2>0$ ve $ac-b^2=1>0$ olur, dolayısıyla $-\mathbf{A}_4$ pozitif tanımlı, $\mathbf{A}_4$ ise negatif tanımlıdır. $\mathbf{A}_4$ matrisinin özdeğerleri: iz $-3$, determinant $1$, $\lambda=\tfrac{-3\pm\sqrt5}2\approx-0{,}38$ ve $-2{,}62$, ikisi de negatif: bir kubbe.

</li>

</ul>
:::
:::

:::aufgabe Alıştırma 25 ★★ Bir tuzak
<span class="anker" id="aufg-25"></span>

<ol class="al">

<li>

$\bigl(\begin{smallmatrix}1&-4\\0&1\end{smallmatrix}\bigr)$ matrisinin yalnızca pozitif özdeğerleri vardır. Kuadratik formu pozitif midir? Bunun tersini gösteren bir vektör bulun ve çelişkiyi açıklayın.

</li>

<li>

$t$ sayısının hangi değerleri için $\bigl(\begin{smallmatrix}1&t\\t&4\end{smallmatrix}\bigr)$ pozitif tanımlıdır? Hangileri için pozitif yarı tanımlıdır?

</li>

</ol>

:::loesung
(a) Özdeğerler $1$ ve $1$ olur, ama $x_1^2-4x_1x_2+x_2^2$ formunun $\mathbf{x}=(1,\,1)^{\top}$ noktasındaki değeri $1-4+1=-2<0$. Bu bir çelişki değildir: Özdeğer testi yalnızca simetrik matrisler için geçerlidir. Form yalnızca $\bigl(\begin{smallmatrix}1&-2\\-2&1\end{smallmatrix}\bigr)$ simetrik kısmını görür ve bu kısmın özdeğerleri $3$ ve $-1$ olur; form belirsizdir.

(b) $2\times2$ testiyle: $a=1>0$ ve $ac-b^2=4-t^2>0$ koşulu tam olarak $|t|<2$ için sağlanır. Pozitif yarı tanımlılık için özdeğerlerin $\ge0$ olması gerekir. Toplamları iz olan $5>0$, çarpımları determinant olan $4-t^2$ değeridir; iki özdeğer de ancak ve ancak $4-t^2\ge0$ ise, yani $|t|\le2$ için $\ge0$ olur. $t=\pm2$ için matris pozitif yarı tanımlıdır, ama tanımlı değildir, özdeğerleri $5$ ve $0$ olur; $|t|>2$ için belirsizdir.
:::
:::

:::aufgabe Alıştırma 26 ★★ Rayleigh bölümü ve Cholesky
<span class="anker" id="aufg-26"></span>

$\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$ olsun.

<ol class="al">

<li>

Özdeğerleri ve $\mathbf{e}_1$, $\mathbf{e}_2$ ve $(1,\,1)^{\top}$ noktalarındaki Rayleigh bölümünü hesaplayın. [(8.2)](#gl-8-2) eşitsizliğini doğrulayın.

</li>

<li>

$\mathbf{A}\mathbf{x}=(2,\,9)^{\top}$ sistemini Cholesky çarpanıyla çözün: önce $\mathbf L\mathbf{z}=(2,\,9)^{\top}$ sistemini yukarıdan aşağıya, sonra $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$ sistemini aşağıdan yukarıya.

</li>

</ol>

:::loesung
(a) İz $9$, determinant $16$: $\lambda=\tfrac{9\pm\sqrt{81-64}}2=\tfrac{9\pm\sqrt{17}}2\approx6{,}56$ ve $2{,}44$. Rayleigh bölümü $\mathbf{e}_1$ noktasında $4$, $\mathbf{e}_2$ noktasında $5$, $(1,\,1)^{\top}$ noktasında $\tfrac{4+2+2+5}2=\tfrac{13}2=6{,}5$ olur. Üçü de $2{,}44$ ile $6{,}56$ arasındadır; üçüncüsü en büyük değere yakındır, çünkü $(1,\,1)^{\top}$ neredeyse büyük özdeğere ait özvektörün doğrultusunu gösterir.

(b) Kesim [8.6](#stufe-8-6)'dan: $\mathbf L=\bigl(\begin{smallmatrix}2&0\\1&2\end{smallmatrix}\bigr)$. Yukarıdan aşağıya: $2z_1=2$, dolayısıyla $z_1=1$; $z_1+2z_2=9$, dolayısıyla $z_2=4$. Sonra $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$ aşağıdan yukarıya: $2x_2=4$, dolayısıyla $x_2=2$; $2x_1+x_2=1$, dolayısıyla $x_1=-\tfrac12$. Sağlama: $\mathbf{A}(-\tfrac12,\,2)^{\top}=(-2+4,\ -1+10)^{\top}=(2,\,9)^{\top}$. İki üçgen sistem, genel bir denklem sisteminin yerini alır.
:::
:::
