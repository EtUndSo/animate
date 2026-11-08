---
title: Sözde ters
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
knoten: Temeller 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15221200
summary: Temeller 1'de yalnızca bağımsız sütunlu bir kare matrisin tersi vardı.
tags: sol tersi, sağ tersi, sözde tersi
lang: tr
---

<span class="anker" id="stufe-11"></span>

:::zweck
Temeller 1'de yalnızca bağımsız sütunlu bir kare matrisin tersi vardı. Bu kesim her matrise bir tür ters veriyor: bilinmeyenlerden çok denklem varken soldan tersine çeviren bir ters, daha az denklem varken sağdan tersine çeviren bir ters ve her durum için bir ters, yani sözde ters. Sözde ters her zaman en iyi yaklaşık çözümü, birden çok varsa da en kısasını verir.
:::

### Sol ters

<span class="anker" id="stufe-11-1"></span>

$m>n$ olan uzun bir $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisinin tersi yoktur; kare bile değildir. Ama bir ters matrisin özelliğinin yarısına sahip olabilir.

:::definition Tanım 11.1 (Sol ters)
<span class="anker" id="satz-11-1"></span>

$\mathbf F\mathbf{A}=\mathbf{I}_n$ eşitliğini sağlayan bir $\mathbf F\in\mathbb{R}^{n\times m}$ matrisine $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisinin __sol tersi__ denir.
:::

:::satz Teorem 11.2 (Sol ters)
<span class="anker" id="satz-11-2"></span>

$\mathbf{A}$ matrisinin ancak ve ancak sütunları doğrusal bağımsızsa bir sol tersi vardır. O zaman

<span class="anker" id="gl-11-1"></span>
$$\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{11.1}$$

bir sol terstir ve $\mathbf F\mathbf{y}$, $\mathbf{A}\mathbf{x}=\mathbf{y}$ sisteminin en iyi yaklaşık çözümüdür.
:::

:::beweis Sol ters
Sütunlar bağımsızsa Kesim [3.5](die-beste-naherungslosung.html#stufe-3-5)'e göre $\mathbf{A}^{\top}\mathbf{A}$ tersinirdir ve $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$ olur. [(3.5)](die-beste-naherungslosung.html#gl-3-5) uyarınca $\mathbf F\mathbf{y}=\hat{\mathbf{x}}$ olur. Tersine: $\mathbf{A}$ matrisinin bir sol tersi varsa ve $\mathbf{A}\mathbf{x}=\mathbf{0}$ ise $\mathbf{x}=\mathbf F\mathbf{A}\mathbf{x}=\mathbf F\mathbf{0}=\mathbf{0}$ olur; demek ki çekirdek $\{\mathbf{0}\}$ kümesidir ve sütunlar bağımsızdır.
:::

$\mathbf F$ sağdan bir ters değildir. [(4.1)](projektion-auf-einen-unterraum.html#gl-4-1) uyarınca $\mathbf{A}\mathbf F=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ çarpımı sütun uzayı üzerine izdüşümdür ve $m>n$ için bu $\mathbf{I}_m$ değildir. Ayrıca uzun bir matrisin pek çok sol tersi vardır; [(11.1)](#gl-11-1), dik izdüşüme ait olanıdır.

⁠**Sayısal örnek:** Sütunları $(1,\,0,\,1)^{\top}$ ve $(0,\,1,\,1)^{\top}$ olan $\mathbf{H}$ için $(\mathbf{H}^{\top}\mathbf{H})^{-1}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$ olur ve şu bulunur:

$$\mathbf F=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\end{pmatrix}.$$

$\mathbf F\mathbf{H}=\tfrac13\bigl(\begin{smallmatrix}2+1&-1+1\\-1+1&2+1\end{smallmatrix}\bigr)=\mathbf{I}_2$ olur ve $\mathbf F(1,\,1,\,1)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$, Kesim [3.3](die-beste-naherungslosung.html#stufe-3-3)'teki en iyi yaklaşık çözümdür. $\mathbf{H}\mathbf F$, Kesim [4.2](projektion-auf-einen-unterraum.html#stufe-4-2)'deki $\tfrac13\Bigl(\begin{smallmatrix}2&-1&1\\-1&2&1\\1&1&2\end{smallmatrix}\Bigr)$ izdüşüm matrisidir. Başka bir sol ters $\bigl(\begin{smallmatrix}1&0&0\\0&1&0\end{smallmatrix}\bigr)$ matrisidir, çünkü $\mathbf{H}$ matrisinin ilk iki satırı birim matrisi oluşturur; ama bu sol ters $(1,\,1,\,1)^{\top}$ için en iyi yaklaşık çözümü değil, $(1,\,1)^{\top}$ vektörünü verir.

⁠**Kısacası:** Sütunları bağımsız olan bir matrisin sol tersi $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ olur; bu ters $\mathbf{y}$ vektörünü en iyi yaklaşık çözüme götürür.

### Sağ ters

<span class="anker" id="stufe-11-2"></span>

$m<n$ olan geniş bir matriste bilinmeyenlerden daha az denklem vardır. Sistem çözülebiliyorsa sonsuz sayıda çözümü vardır. Bir sağ ters bunlardan birini seçer, hem de özel birini.

:::definition Tanım 11.3 (Sağ ters)
<span class="anker" id="satz-11-3"></span>

$\mathbf{A}\mathbf G=\mathbf{I}_m$ eşitliğini sağlayan bir $\mathbf G\in\mathbb{R}^{n\times m}$ matrisine $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisinin __sağ tersi__ denir.
:::

:::satz Teorem 11.4 (Sağ ters ve en kısa çözüm)
<span class="anker" id="satz-11-4"></span>

$\mathbf{A}$ matrisinin satırları doğrusal bağımsızsa

<span class="anker" id="gl-11-2"></span>
$$\mathbf G=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1} \tag{11.2}$$

bir sağ terstir. $\mathbf{x}=\mathbf G\mathbf{y}$ her $\mathbf{y}$ için $\mathbf{A}\mathbf{x}=\mathbf{y}$ sistemini çözer ve bütün çözümler arasında uzunluğu en küçük olandır.
:::

:::beweis Sağ ters
$\mathbf{A}$ matrisinin satırları $\mathbf{A}^{\top}$ matrisinin sütunlarıdır; Kesim [3.5](die-beste-naherungslosung.html#stufe-3-5) $\mathbf{A}^{\top}$ için uygulanınca $\mathbf{A}\mathbf{A}^{\top}$ matrisinin tersinir olduğu çıkar. O zaman $\mathbf{A}\mathbf G=\mathbf{A}\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}=\mathbf{I}$ ve $\mathbf{A}\mathbf G\mathbf{y}=\mathbf{y}$ olur. $\mathbf{x}$ herhangi bir çözümse $\mathbf{A}(\mathbf{x}-\mathbf G\mathbf{y})=\mathbf{0}$ olur, dolayısıyla $\mathbf{z}=\mathbf{x}-\mathbf G\mathbf{y}$ çekirdektedir. $\mathbf{w}=(\mathbf{A}\mathbf{A}^{\top})^{-1}\mathbf{y}$ olmak üzere $\mathbf G\mathbf{y}=\mathbf{A}^{\top}\mathbf{w}$ vektörü çekirdeğin her vektörüne diktir, çünkü $(\mathbf{A}^{\top}\mathbf{w})^{\top}\mathbf{z}=\mathbf{w}^{\top}\mathbf{A}\mathbf{z}=0$. Pisagor teoremine göre şu bulunur:

$$\lVert\mathbf{x}\rVert^2=\lVert\mathbf G\mathbf{y}+\mathbf{z}\rVert^2=\lVert\mathbf G\mathbf{y}\rVert^2+\lVert\mathbf{z}\rVert^2\ge\lVert\mathbf G\mathbf{y}\rVert^2 ,$$

eşitlik yalnızca $\mathbf{z}=\mathbf{0}$ için sağlanır.
:::

Geometrik olarak çözüm kümesi orijinden geçmeyen bir doğru ya da düzlemdir ve $\mathbf G\mathbf{y}$ bu kümenin orijine en yakın noktasıdır: orijinden inilen dikmenin ayağı.

⁠**Sayısal örnek:** Tek bir $x_1+2x_2=5$ denklemi için $\mathbf{A}=(1\ \ 2)$ ve $\mathbf{A}\mathbf{A}^{\top}=5$ olur. Dolayısıyla $\mathbf G=\tfrac15(1,\,2)^{\top}$ ve $\mathbf G\cdot5=(1,\,2)^{\top}$. Bütün çözümler $(1,\,2)^{\top}+t\,(2,\,-1)^{\top}$ biçimindedir ve uzunluklarının karesi $(1+2t)^2+(2-t)^2=5+5t^2$ olur; en kısa çözüm $t=0$ için elde edilir. $(1,\,2)^{\top}$ vektörü, doğrultusu $(2,\,-1)^{\top}$ olan çözüm doğrusuna diktir.

⁠**Kısacası:** Satırları bağımsız olan bir matrisin sağ tersi $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$ olur; bu ters en kısa çözümü verir.

### Sözde ters

<span class="anker" id="stufe-11-3"></span>

$\mathbf{A}$ matrisinin ne sütunları ne de satırları bağımsızsa iki formül de işe yaramaz. Bir örnek Kesim [3.5](die-beste-naherungslosung.html#stufe-3-5)'teki $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ matrisidir: $\mathbf{y}=(1,\,1)^{\top}$ için $x_1+2x_2=\tfrac35$ doğrusunun bütün noktaları en iyi yaklaşık çözümdür. Tekil değer ayrışımı her matris için bir formül verir.

:::definition Tanım 11.5 (Sözde ters)
<span class="anker" id="satz-11-5"></span>

$\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ ve rank $r$ olsun. $\mathbf{D}^+\in\mathbb{R}^{n\times m}$ matrisi, $\mathbf{D}^{\top}$ matrisinde her $d_j>0$ değeri $1/d_j$ ile değiştirilerek elde edilir; sıfırlar kalır. $\mathbf{A}$ matrisinin __sözde tersi__ şudur:

<span class="anker" id="gl-11-3"></span>
$$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\sum_{j=1}^r\frac1{d_j}\,\mathbf{v}_j\mathbf{u}_j^{\top} . \tag{11.3}$$
:::

Her yapı taşı $\mathbf{A}$ matrisinin bir yapı taşını tersine çevirir: $\mathbf{A}$, $\mathbf{v}_j$ vektörünü $d_j\mathbf{u}_j$ vektörüne, $\mathbf{A}^+$ de $\mathbf{u}_j$ vektörünü $\mathbf{v}_j/d_j$ vektörüne götürür. $\mathbf{A}$ matrisinin ulaşamadığı, $j>r$ olan $\mathbf{u}_j$ doğrultularını $\mathbf{A}^+$ sıfıra bölmek yerine sıfıra götürür. $\mathbf{A}$ tersinirse $\mathbf{A}^+=\mathbf{A}^{-1}$ olur, çünkü o zaman $\mathbf{A}^{-1}=(\mathbf{V}^{\top})^{-1}\mathbf{D}^{-1}\mathbf{U}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$.

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ simetrik ve pozitif yarı tanımlıdır; $\mathbf{q}=(1,\,2)^{\top}/\sqrt5$ vektörüne ait özdeğeri $5$, öbür özdeğeri $0$ olur. Kesim [9.7](die-singularwertzerlegung.html#stufe-9-7)'ye göre kompakt ayrışımı, $d_1=5$ ve $\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$ ile $\mathbf{A}=5\,\mathbf{q}\mathbf{q}^{\top}$ olur. Dolayısıyla şu bulunur:

$$\mathbf{A}^+=\frac15\,\mathbf{q}\mathbf{q}^{\top}=\frac1{25}\begin{pmatrix}1&2\\2&4\end{pmatrix}.$$

⁠**Kısacası:** $\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ sözde tersi, $d_j>0$ olan her $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ yapı taşını tersine çevirir ve $0$ tekil değerine ait doğrultuları sıfıra götürür.

### En kısa en iyi yaklaşık çözüm

<span class="anker" id="stufe-11-4"></span>

$\mathbf{A}^+\mathbf{y}$ ne sağlar? Önceki iki alt kesimi birleştirir.

:::satz Teorem 11.6 (Sözde ters ve en küçük kareler)
<span class="anker" id="satz-11-6"></span>

Her $\mathbf{A}$ matrisi ve her $\mathbf{y}$ vektörü için $\mathbf{x}^+=\mathbf{A}^+\mathbf{y}$, $\mathbf{A}\mathbf{x}=\mathbf{y}$ sisteminin bir en iyi yaklaşık çözümüdür ve bütün en iyi yaklaşık çözümler arasında uzunluğu en küçük olandır. Özellikle şu geçerlidir:

$$\begin{gathered} \mathbf{A}^+=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\quad\text{bağımsız sütunlarda},\\ \mathbf{A}^+=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}\quad\text{bağımsız satırlarda}. \end{gathered}$$
:::

:::beweis Sözde ters
Hesap tekil vektörlerin koordinatlarında yapılır: $\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$ ve $\boldsymbol\beta=\mathbf{U}^{\top}\mathbf{y}$. $\mathbf{U}^{\top}$ uzunlukları koruduğundan şu geçerlidir:

$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{U}^{\top}\mathbf{y}-\mathbf{D}\mathbf{V}^{\top}\mathbf{x}\rVert^2=\lVert\boldsymbol\beta-\mathbf{D}\mathbf{c}\rVert^2=\sum_{j=1}^r(\beta_j-d_jc_j)^2+\sum_{j=r+1}^m\beta_j^2 .$$

İkinci toplam $\mathbf{x}$ vektörüne bağlı değildir. Birincisi ancak ve ancak bütün $j\le r$ için $c_j=\beta_j/d_j$ ise sıfırdır, yani olabildiğince küçüktür; $j>r$ olan $c_j$ değerleri hiç yer almaz. Demek ki en iyi yaklaşık çözümler tam olarak, $j\le r$ için $c_j=\beta_j/d_j$ olan ve $c_{r+1},\dots,c_n$ değerleri keyfi olan $\mathbf{x}=\mathbf{V}\mathbf{c}$ vektörleridir. Uzunlukları $\lVert\mathbf{x}\rVert^2=\lVert\mathbf{c}\rVert^2=\sum_{j\le r}(\beta_j/d_j)^2+\sum_{j>r}c_j^2$ olur ve $j>r$ için $c_j=0$ alındığında en küçüktür. Bu $\mathbf{c}$ vektörü $\mathbf{D}^+\boldsymbol\beta$ olur, dolayısıyla $\mathbf{x}=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}\mathbf{y}=\mathbf{A}^+\mathbf{y}$.

Sütunlar bağımsızsa Kesim [3.5](die-beste-naherungslosung.html#stufe-3-5)'e göre yalnızca bir en iyi yaklaşık çözüm vardır: $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$; bu çözüm $\mathbf{A}^+\mathbf{y}$ ile, hem de her $\mathbf{y}$ için aynı olmalıdır. Satırlar bağımsızsa Temeller 1, Kesim 13.4'e göre rank $m$ olur, yani sütun uzayı $\mathbb{R}^m$ uzayının tamamıdır ve sistem her $\mathbf{y}$ için çözülebilir; en iyi yaklaşık çözümler sistemin çözümleridir ve Kesim [11.2](#stufe-11-2)'ye göre en kısası $\mathbf G\mathbf{y}$ olur.
:::

⁠**Sayısal örnek 1:** $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ ve $\mathbf{y}=(1,\,1)^{\top}$ için $\mathbf{x}^+=\tfrac1{25}(1+2,\ 2+4)^{\top}=(0{,}12;\ 0{,}24)^{\top}$ olur. Bu vektör en iyi yaklaşık çözümlerin doğrusu üzerindedir, çünkü $0{,}12+2\cdot0{,}24=0{,}6=\tfrac35$; ayrıca $(1,\,2)^{\top}$ doğrultusunu, yani doğruya dik doğrultuyu gösterir: Doğrunun orijine en yakın noktasıdır.

⁠**Sayısal örnek 2:** Aynı büyüklük üç kez ölçülüyor; sonuçlar $4$, $5$ ve $9$. “$x=4$, $x=5$, $x=9$” sisteminin matrisi, birlerden oluşan bir sütun olan $\mathbf{1}\in\mathbb{R}^{3\times1}$ olur. Bu matrisin bağımsız bir sütunu vardır, dolayısıyla $\mathbf{1}^+=(\mathbf{1}^{\top}\mathbf{1})^{-1}\mathbf{1}^{\top}=\tfrac13(1,\,1,\,1)$ ve şu bulunur:

$$x^+=\tfrac13\,\mathbf{1}^{\top}\mathbf{y}=\tfrac13\,(4+5+9)=6 ,$$

yani ortalama (Şekil [27](#abb-27)). Birkaç ölçümün ortalaması, her ölçümü tam doğru sayan sistemin en iyi yaklaşık çözümüdür.

:::abbildung ml/k2rmittel 27
Birler sütununun sözde tersi $\mathbf{y}=(4,5,9)^{\top}$ ölçüm değerlerine uygulanınca: $\mathbf{1}$ ile iç çarpım ölçüm değerlerinin toplamıdır; $\mathbf{1}^{\top}\mathbf{1}=3$ sayısına bölününce ortalama elde edilir.
:::

⁠**Kısacası:** $\mathbf{A}^+\mathbf{y}$ her matris için bir en iyi yaklaşık çözümdür, birden çok varsa en kısasıdır; sütunlar ya da satırlar bağımsızsa $\mathbf{A}^+$ sol ya da sağ terstir.

:::hintergrund Sözde ters neden sıfıra bölmez
Sözde ters, $d_j=0$ olan yerlerde $1/d_j$ yerine $0$ koyar. Bu keyfi görünür, ama bir limitten çıkar. $\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I}$ matrisi her $\delta\ne0$ için tersinirdir, çünkü özdeğerleri $d_j^2+\delta^2>0$ olur. Tekil vektörlerin koordinatlarında $(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$ matrisi $j$ numaralı koordinatı şu sayıyla çarpar:

$$\frac{d_j}{d_j^2+\delta^2}\ \xrightarrow{\ \delta\to0\ }\ \begin{cases}1/d_j&d_j>0\text{ için},\\0&d_j=0\text{ için}.\end{cases}$$

Dolayısıyla her matris için $\mathbf{A}^+=\lim_{\delta\to0}(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$ olur. Bu limit bir tehlikeyi de gösterir: Sözde ters matrise sürekli olarak bağlı değildir. Küçük bir $\varepsilon>0$ ile $\operatorname{diag}(1;\,\varepsilon)$ matrisinin sözde tersi $\operatorname{diag}(1;\,1/\varepsilon)$ olur, yani devasadır; $\varepsilon=0$ için ise $\operatorname{diag}(1;\,0)$ olur. Yalnızca ölçüm hataları ya da yuvarlama yüzünden sıfır olmayan çok küçük bir tekil değer, $\mathbf{A}^+$ tarafından muazzam biçimde büyütülür. Bu yüzden sayısal hesap yazılımları küçük bir eşiğin altındaki tekil değerleri sıfır sayar. Küçük tekil değerlerin hataları ne kadar büyüttüğünü sonraki kesim ölçüyor.
:::

:::aufgabe Alıştırma 33 ★ Bir sol ters
<span class="anker" id="aufg-33"></span>

Kesim [3.6](die-beste-naherungslosung.html#stufe-3-6)'daki en küçük kareler doğrusu $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$ matrisine aittir.

<ol class="al">

<li>

$\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ sol tersini hesaplayın ve $\mathbf F\mathbf{A}=\mathbf{I}$ eşitliğini doğrulayın.

</li>

<li>

$\mathbf F$ matrisini $\mathbf{y}=(1,\,2,\,4)^{\top}$ vektörüne uygulayın ve Kesim [3.6](die-beste-naherungslosung.html#stufe-3-6)'daki sonuçla karşılaştırın.

</li>

<li>

Herhangi $y_1,y_2,y_3$ ölçüm değerleri için en küçük kareler doğrusunun eksen kesişiminin ve eğiminin nasıl oluştuğunu $\mathbf F$ matrisinin satırlarından okuyun.

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&3\\3&5\end{smallmatrix}\bigr)$ olur, tersi $\tfrac16\bigl(\begin{smallmatrix}5&-3\\-3&3\end{smallmatrix}\bigr)$, dolayısıyla

$$\mathbf F=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix}\begin{pmatrix}1&1&1\\0&1&2\end{pmatrix}=\frac16\begin{pmatrix}5&2&-1\\-3&0&3\end{pmatrix},\qquad \mathbf F\mathbf{A}=\frac16\begin{pmatrix}5+2-1&2-2\\-3+3&6\end{pmatrix}=\mathbf{I} .$$

(b) $\mathbf F(1,\,2,\,4)^{\top}=\tfrac16(5+4-4,\ -3+12)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$ olur; bu, Kesim [3.6](die-beste-naherungslosung.html#stufe-3-6)'daki en küçük kareler doğrusudur.

(c) Herhangi ölçüm değerleri için eksen kesişimi $\hat x_1=\tfrac16(5y_1+2y_2-y_3)$, eğim de $\hat x_2=\tfrac12(y_3-y_1)$ olur. Eksen kesişiminin ağırlıklarının toplamı $1$ eder: Bütün ölçüm değerleri eşitse eksen kesişimi bu değerdir. Aralarındaki uzaklıklar eşit olan üç ölçüm yerinde eğim yalnızca dıştaki iki noktaya bağlıdır; ortadaki nokta yalnızca doğrunun yüksekliğini etkiler.
:::
:::

:::aufgabe Alıştırma 34 ★★ En kısa çözümler
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

$\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ matrisinin sözde tersini ve $\mathbf{y}=(1,\,3)^{\top}$ için $\mathbf{x}^+$ vektörünü bulun. $\mathbf{x}^+$ vektörünün bir en iyi yaklaşık çözüm olduğunu ve daha kısa bir en iyi yaklaşık çözüm bulunmadığını doğrulayın.

</li>

<li>

$x_1+2x_2+2x_3=9$ denkleminin en kısa çözümünü bulun. Uzunluğunu $(9,\,0,\,0)^{\top}$ çözümünün uzunluğuyla karşılaştırın.

</li>

</ol>

:::loesung
(a) $\mathbf{q}=(1,\,1)^{\top}/\sqrt2$ ile $\mathbf{A}=2\,\mathbf{q}\mathbf{q}^{\top}$ olur. Matris simetrik ve pozitif yarı tanımlıdır; dolayısıyla bu, $d_1=2$ ve $\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$ ile kompakt ayrışımdır. Böylece $\mathbf{A}^+=\tfrac12\mathbf{q}\mathbf{q}^{\top}=\tfrac14\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ ve $\mathbf{x}^+=\tfrac14(4,\,4)^{\top}=(1,\,1)^{\top}$ olur. $\mathbf{A}\mathbf{x}^+=(2,\,2)^{\top}$ olur; bu, $(1,\,3)^{\top}$ vektörünün $(1,\,1)^{\top}$ doğrultusundaki doğru üzerine izdüşümüdür, çünkü $\tfrac{1+3}2(1,\,1)^{\top}=(2,\,2)^{\top}$. En iyi yaklaşık çözümler $x_1+x_2=2$ olan bütün $\mathbf{x}$ vektörleridir, yani uzunluklarının karesi $2+2s^2$ olan $(1+s,\ 1-s)^{\top}$ vektörleri. En kısası $s=0$ için elde edilen çözümdür ve bu da $\mathbf{x}^+$ vektörüdür.

(b) $\mathbf{A}=(1\ \ 2\ \ 2)$ için $\mathbf{A}\mathbf{A}^{\top}=9$ olur, dolayısıyla $\mathbf G=\tfrac19(1,\,2,\,2)^{\top}$ ve en kısa çözüm, uzunluğu $3$ olan $\mathbf G\cdot9=(1,\,2,\,2)^{\top}$ olur. $(9,\,0,\,0)^{\top}$ çözümünün uzunluğu $9$. En kısa çözüm, çözüm düzleminin $(1,\,2,\,2)^{\top}$ normal vektörünün doğrultusunu gösterir.
:::
:::

:::aufgabe Alıştırma 35 ★★★ Sözde ters neyin üzerine izdüşürür
<span class="anker" id="aufg-35"></span>

$\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ ve rank $r$ olsun; $\mathbf{U}_r$ ve $\mathbf{V}_r$, $\mathbf{U}$ ve $\mathbf{V}$ matrislerinin ilk $r$ sütununu içersin.

<ol class="al">

<li>

$\mathbf{A}\mathbf{A}^+=\mathbf{U}_r\mathbf{U}_r^{\top}$ ve $\mathbf{A}^+\mathbf{A}=\mathbf{V}_r\mathbf{V}_r^{\top}$ olduğunu gösterin. Bu matrisler hangi uzayların üzerine izdüşürür?

</li>

<li>

Buradan $\mathbf{A}\mathbf{A}^+\mathbf{A}=\mathbf{A}$ ve $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=\mathbf{A}^+$ sonuçlarını çıkarın.

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{A}^+=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^+\mathbf{U}^{\top}$ olur. $m\times m$ boyutlu $\mathbf{D}\mathbf{D}^+$ matrisinin ilk $r$ köşegen yerinde $d_j\cdot\tfrac1{d_j}=1$, geri kalan yerlerde sıfır bulunur. Dolayısıyla $\mathbf{A}\mathbf{A}^+=\sum_{j\le r}\mathbf{u}_j\mathbf{u}_j^{\top}=\mathbf{U}_r\mathbf{U}_r^{\top}$ olur; bu, [(4.2)](projektion-auf-einen-unterraum.html#gl-4-2) uyarınca $\mathbf{u}_1,\dots,\mathbf{u}_r$ vektörlerinin gerdiği alt uzay, yani $\mathbf{A}$ matrisinin sütun uzayı üzerine dik izdüşümdür. Aynı şekilde $\mathbf{A}^+\mathbf{A}=\mathbf{V}\mathbf{D}^+\mathbf{D}\mathbf{V}^{\top}=\mathbf{V}_r\mathbf{V}_r^{\top}$ olur; bu, $\mathbf{v}_1,\dots,\mathbf{v}_r$ vektörlerinin gerdiği alt uzay, yani $\mathbf{A}^{\top}$ matrisinin sütun uzayı üzerine izdüşümdür; bu uzay çekirdeğin ortogonal tümleyenidir.

(b) $\mathbf{A}$ matrisinin her sütunu sütun uzayındadır ve bu uzay üzerine izdüşüm onu yerinde bırakır: $\mathbf{A}\mathbf{A}^+\mathbf{A}=(\mathbf{U}_r\mathbf{U}_r^{\top})\mathbf{A}=\mathbf{A}$. Aynı şekilde $\mathbf{A}^+=\sum_{j\le r}\tfrac1{d_j}\mathbf{v}_j\mathbf{u}_j^{\top}$ matrisinin her sütunu $\mathbf{v}_1,\dots,\mathbf{v}_r$ vektörlerinin gerdiği alt uzaydadır, dolayısıyla $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=(\mathbf{V}_r\mathbf{V}_r^{\top})\mathbf{A}^+=\mathbf{A}^+$ olur.
:::
:::
