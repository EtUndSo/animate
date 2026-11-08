---
title: Tekil değer ayrışımı
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
knoten: Temeller 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15221000
summary: Özvektörler yalnızca kare matrislerde vardır ve yalnızca simetrik matrislerde birbirine diktir.
tags: tekil değerleri, sağ tekil vektörleri, sol tekil vektör, spektral normu
lang: tr
---

<span class="anker" id="stufe-9"></span>

:::zweck
Özvektörler yalnızca kare matrislerde vardır ve yalnızca simetrik matrislerde birbirine diktir. Bu kesim, dikdörtgen olanlar dahil her matrisin bir çift dik eksen takımı olduğunu gösteriyor: biri girişlerin uzayında, biri çıkışların uzayında. Matris birinin her eksenini öbürünün bir ekseninin bir katına götürür. Buradan her matrisin dönme, germe ve dönmeye ayrışımı çıkar.
:::

### Dik kalan dik doğrultular

<span class="anker" id="stufe-9-1"></span>

$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ matrisinin, bir üçgen matris olarak, çift katlı $2$ özdeğeri vardır, ama tek bir öz doğrultusu bulunur: $(\mathbf{A}-2\mathbf{I})\mathbf{v}=\mathbf{0}$ demek $3v_2=0$ demektir, dolayısıyla yalnızca $\mathbf{e}_1$ vektörünün katları söz konusu olabilir (Alıştırma [19](eigenwerte-und-eigenvektoren.html#aufg-19)). Kesim [7.2](diagonalisierung-und-spektralsatz.html#stufe-7-2)'ye göre bu matris köşegenleştirilemez. Yine de birim çemberi bir elipse dönüştürür (Şekil [23](#abb-23)) ve bir elipsin birbirine dik iki ekseni vardır. Çemberin hangi okları bu eksenlerin üzerine düşer?

Burada bir özvektörden daha azı aranıyor: Bir ok doğrultusunu değiştirebilir. Aranan, $\mathbf{A}\mathbf{v}_1$ ve $\mathbf{A}\mathbf{v}_2$ görüntüleri yine birbirine dik olan, birbirine dik iki $\mathbf{v}_1$, $\mathbf{v}_2$ birim vektörüdür. İki görüntünün birbirine dik olup olmadığını iç çarpımları söyler:

$$(\mathbf{A}\mathbf{v}_1)^{\top}(\mathbf{A}\mathbf{v}_2)=\mathbf{v}_1^{\top}\,\mathbf{A}^{\top}\mathbf{A}\,\mathbf{v}_2 .$$

Burada $\mathbf{A}^{\top}\mathbf{A}$ Gram matrisi ortaya çıkar. $\mathbf{A}$ simetrik olmasa bile bu matris simetriktir ve spektral teoreme göre özvektörlerden oluşan bir ortonormal tabanı vardır. $\mathbf{v}_2$, $\mathbf{A}^{\top}\mathbf{A}$ matrisinin $\lambda_2$ özdeğerine ait bir özvektörse ve $\mathbf{v}_1$, $\mathbf{v}_2$ vektörüne dikse iç çarpım $\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$ olur. Demek ki $\mathbf{A}^{\top}\mathbf{A}$ matrisinin özvektörleri isteneni sağlar. Aynı hesap $\mathbf{v}_1=\mathbf{v}_2$ ile görüntülerin uzunluklarını verir: $\lVert\mathbf{A}\mathbf{v}_i\rVert^2=\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_i=\lambda_i$.

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ için $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}4&6\\6&13\end{smallmatrix}\bigr)$ olur; izi $17$, determinantı $52-36=16$. $\lambda^2-17\lambda+16=(\lambda-16)(\lambda-1)$ karakteristik polinomunun kökleri $16$ ve $1$. Normlanmış özvektörler $16$ için $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$ ve $1$ için $\mathbf{v}_2=(-2,\,1)^{\top}/\sqrt5$ olur. Bunların

$$\mathbf{A}\mathbf{v}_1=\frac1{\sqrt5}\begin{pmatrix}8\\4\end{pmatrix},\qquad \mathbf{A}\mathbf{v}_2=\frac1{\sqrt5}\begin{pmatrix}-1\\2\end{pmatrix}$$

görüntülerinin iç çarpımı $\tfrac15(-8+8)=0$, uzunlukları da $\sqrt{80/5}=4=\sqrt{16}$ ve $1=\sqrt1$ olur (Şekil [22](#abb-22)).

:::abbildung ml/k2rsvdidee 22
$\mathbf{A}\mathbf{v}_1=(8,4)^{\top}/\sqrt5$ ve $\mathbf{A}\mathbf{v}_2=(-1,2)^{\top}/\sqrt5$ görüntüleri birbirine diktir ve uzunluklarının kareleri, $\mathbf{A}^{\top}\mathbf{A}$ matrisinin özdeğerleri olan $16$ ve $1$ sayılarıdır.
:::

⁠**Kısacası:** Simetrik $\mathbf{A}^{\top}\mathbf{A}$ matrisinin özvektörleri, $\mathbf{A}$ altındaki görüntüleri yine birbirine dik olan dik doğrultulardır; görüntülerin uzunlukları $\sqrt{\lambda_i}$ olur.

### Tekil değerler

<span class="anker" id="stufe-9-2"></span>

Görüntülerin uzunlukları bir matrisin en önemli göstergeleridir: Matrisin ana doğrultularında ne kadar uzattığını söylerler. Kesim [8.4](positiv-definite-matrizen.html#stufe-8-4)'e göre $\mathbf{A}^{\top}\mathbf{A}$ pozitif yarı tanımlıdır; dolayısıyla özdeğerleri negatif değildir ve karekökleri alınabilir.

:::definition Tanım 9.1 (Tekil değerler)
<span class="anker" id="satz-9-1"></span>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ olsun ve $\lambda_1\ge\lambda_2\ge\dots\ge\lambda_n\ge0$, $\mathbf{A}^{\top}\mathbf{A}$ matrisinin büyükten küçüğe sıralanmış, katlı olanları katlılıkları kadar sayılmış özdeğerleri olsun.

<span class="anker" id="gl-9-1"></span>
$$d_j=\sqrt{\lambda_j},\qquad d_1\ge d_2\ge\dots\ge d_n\ge0 , \tag{9.1}$$

sayılarına $\mathbf{A}$ matrisinin __tekil değerleri__ denir.
:::

Birçok kitap $d_j$ yerine $\sigma_j$ yazar. Tekil değerler burada her zaman bir indis taşır; Temeller 1'deki indissiz $d$, yani öznitelik sayısı, başka bir şeydir.

:::satz Teorem 9.2 (Tekil değerler ve rank)
<span class="anker" id="satz-9-2"></span>

Sıfırdan farklı tekil değerlerin sayısı $\mathbf{A}$ matrisinin rankıdır.
:::

:::beweis Tekil değerler ve rank
$\mathbf{v}_1,\dots,\mathbf{v}_n$, $\mathbf{A}^{\top}\mathbf{A}$ matrisinin $\lambda_1,\dots,\lambda_n$ özdeğerlerine ait ortonormal özvektörleri olsun. Her vektör $\mathbf{x}=\sum_jc_j\mathbf{v}_j$ biçimindedir, dolayısıyla $\mathbf{A}\mathbf{x}=\sum_jc_j\,\mathbf{A}\mathbf{v}_j$ olur: Sütun uzayını $\mathbf{A}\mathbf{v}_1,\dots,\mathbf{A}\mathbf{v}_n$ görüntüleri gerer. Önceki alt kesime göre bu görüntüler ikişer ikişer birbirine diktir ve uzunlukları $d_j$ olur. $d_j=0$ olan görüntüler sıfır vektörüdür ve hiçbir katkı yapmaz. Geri kalanlar birbirine diktir ve sıfır değildir; uzunluklarına bölününce ortonormal olurlar ve Kesim [1.1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-1)'deki teoreme göre doğrusal bağımsızdırlar. Sütun uzayının bir tabanını oluştururlar ve sayıları ranktır.
:::

Bundan sonra bir matrisin rankı $r$ ile gösterilir. $d_1\ge\dots\ge d_r>0$ ve $d_{r+1}=\dots=d_n=0$ olur.

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ matrisinin tekil değerleri $d_1=4$ ve $d_2=1$, rankı $2$ olur. Özdeğerleri $2$ ve $2$: Tekil değerler ve özdeğerler genel olarak farklı sayılardır. $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ matrisi için $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$ olur; özdeğerleri $25$ ve $0$, dolayısıyla tekil değerleri $5$ ve $0$, rankı da $1$ olur.

⁠**Kısacası:** $d_j$ tekil değerleri $\mathbf{A}^{\top}\mathbf{A}$ matrisinin özdeğerlerinin karekökleridir; $\mathbf{A}$ matrisinin ana doğrultularında ne kadar uzattığını ölçerler ve pozitif olanların sayısı ranktır.

### Tekil vektörler

<span class="anker" id="stufe-9-3"></span>

Her pozitif tekil değere iki doğrultu karşılık gelir: bir $\mathbf{v}_j$ giriş doğrultusu ve onun görüntüsünün doğrultusu.

:::definition Tanım 9.3 (Tekil vektörler)
<span class="anker" id="satz-9-3"></span>

$\mathbf{A}^{\top}\mathbf{A}$ matrisinin $d_1^2,\dots,d_n^2$ özdeğerlerine ait $\mathbf{v}_1,\dots,\mathbf{v}_n$ ortonormal özvektörlerine $\mathbf{A}$ matrisinin __sağ tekil vektörleri__ denir. $d_j>0$ için

<span class="anker" id="gl-9-2"></span>
$$\mathbf{u}_j=\frac{\mathbf{A}\mathbf{v}_j}{d_j},\qquad\text{yani}\qquad \mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j , \tag{9.2}$$

vektörüne buna ait __sol tekil vektör__ denir.
:::

Adlar, vektörlerin sonraki alt kesimdeki ayrışımda durduğu yerden gelir. Sol tekil vektörler de ortonormaldir, çünkü

$$\mathbf{u}_i^{\top}\mathbf{u}_j=\frac{\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_id_j}=\frac{d_j^2\,\mathbf{v}_i^{\top}\mathbf{v}_j}{d_id_j},$$

ve bu ifade $i=j$ için $1$, aksi halde $0$ olur. Bunlar $\mathbf{A}\mathbf{A}^{\top}$ matrisinin özvektörleridir ve ters yöndeki denklem de geçerlidir:

$$\mathbf{A}^{\top}\mathbf{u}_j=\frac{\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_j}=d_j\mathbf{v}_j,\qquad \mathbf{A}\mathbf{A}^{\top}\mathbf{u}_j=d_j\,\mathbf{A}\mathbf{v}_j=d_j^2\,\mathbf{u}_j .$$

$\mathbf{A}$, $\mathbf{v}_j$ vektörünü $d_j\mathbf{u}_j$ vektörüne, $\mathbf{A}^{\top}$ de $\mathbf{u}_j$ vektörünü $d_j\mathbf{v}_j$ vektörüne götürür.

:::warnung İşaretler birlikte gider
Bir özvektör ancak işaret farkıyla belirlidir. $\mathbf{v}_j$ vektörleri $\mathbf{A}^{\top}\mathbf{A}$ matrisinin, bundan ayrı olarak da $\mathbf{u}_j$ vektörleri $\mathbf{A}\mathbf{A}^{\top}$ matrisinin özvektörleri olarak hesaplanırsa bir $\mathbf{u}_j$ yanlış işaret alabilir ve o zaman $\mathbf{A}\mathbf{v}_j=-d_j\mathbf{u}_j$ olur. Güvenli yol [(9.2)](#gl-9-2) üzerinden gider: önce $\mathbf{v}_j$ seçilir, sonra $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$ hesaplanır. $\mathbf{v}_j$ ve $\mathbf{u}_j$ birlikte ters çevrilirse her şey doğru kalır.
:::

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ için $\mathbf{u}_1=\mathbf{A}\mathbf{v}_1/4=(2,\,1)^{\top}/\sqrt5$ ve $\mathbf{u}_2=\mathbf{A}\mathbf{v}_2/1=(-1,\,2)^{\top}/\sqrt5$ olur. Sağlama: $\mathbf{A}\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}13&6\\6&4\end{smallmatrix}\bigr)$ matrisi $(2,\,1)^{\top}$ vektörünü $(32,\,16)^{\top}=16\,(2,\,1)^{\top}$ vektörüne götürür. $(-2,\,-1)^{\top}/\sqrt5$ vektörü de $\mathbf{A}\mathbf{A}^{\top}$ matrisinin $16$ özdeğerine ait normlanmış bir özvektörü olurdu, ama onunla $\mathbf{A}\mathbf{v}_1=-4\,\mathbf{u}_1$ olurdu.

⁠**Kısacası:** $\mathbf{v}_j$ sağ tekil vektörleri $\mathbf{A}^{\top}\mathbf{A}$ matrisinin özvektörleridir, sol tekil vektörler ise $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$ olur; iki küme de ortonormaldir ve $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$ geçerlidir.

### Ayrışım

<span class="anker" id="stufe-9-4"></span>

$\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$ denklemleri bütün $j$ değerleri için yan yana yazılırsa matrisin tamamının bir ayrışımı ortaya çıkar.

:::satz Teorem 9.4 (Tekil değer ayrışımı)
<span class="anker" id="satz-9-4"></span>

Rankı $r$ olan her $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisi

<span class="anker" id="gl-9-3"></span>
$$\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top} \tag{9.3}$$

biçiminde yazılabilir; burada $\mathbf{U}\in\mathbb{R}^{m\times m}$ ve $\mathbf{V}\in\mathbb{R}^{n\times n}$ ortogonal matrisler, $\mathbf{D}\in\mathbb{R}^{m\times n}$ ise köşegeninde $d_1\ge\dots\ge d_r>0$ tekil değerlerini taşıyan, geri kalan elemanları sıfır olan bir matristir. $\mathbf{V}$ matrisinin sütunları sağ tekil vektörler, $\mathbf{U}$ matrisinin ilk $r$ sütunu da bunlara ait sol tekil vektörlerdir. Buna denk olan kompakt biçim şudur:

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}=\sum_{j=1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} . \tag{9.4}$$
:::

:::beweis Tekil değer ayrışımı
$j\le r$ için $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$ olur. $j>r$ için $d_j=0$, dolayısıyla $\lVert\mathbf{A}\mathbf{v}_j\rVert=0$ ve $\mathbf{A}\mathbf{v}_j=\mathbf{0}$ olur. $r<m$ ise $\mathbf{u}_1,\dots,\mathbf{u}_r$, örneğin spektral teoremin ispatındaki gibi Gram-Schmidt yöntemiyle, $\mathbb{R}^m$ uzayının bir ortonormal tabanına tamamlanır. Temeller 1, Kesim 9.2'ye göre $\mathbf{A}\mathbf{V}$ matrisinin $j$ numaralı sütunu $\mathbf{A}\mathbf{v}_j$ vektörüdür; $\mathbf{U}\mathbf{D}$ matrisinin $j$ numaralı sütunu ise $j\le r$ için $d_j\mathbf{u}_j$, aksi halde sıfır vektörüdür. Dolayısıyla $\mathbf{A}\mathbf{V}=\mathbf{U}\mathbf{D}$ olur. $\mathbf{V}$ ortogonal olduğundan $\mathbf{V}\mathbf{V}^{\top}=\mathbf{I}$ olur ve sağdan $\mathbf{V}^{\top}$ ile çarpma $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ verir. Kompakt biçim Temeller 1, Kesim 9.5'ten çıkar: $\mathbf{U}\mathbf{D}$ matrisinin $j$ numaralı sütunu çarpı $\mathbf{V}^{\top}$ matrisinin $j$ numaralı satırı, $j$ üzerinden toplanır; yalnızca $j\le r$ olan terimler sıfır değildir.
:::

$\mathbf{D}$ matrisinin biçimi $\mathbf{A}$ matrisinin biçimine göre belirlenir. Örneğin $m=3$ ve $n=2$ için $\mathbf{D}=\Bigl(\begin{smallmatrix}d_1&0\\0&d_2\\0&0\end{smallmatrix}\Bigr)$ olur. Yaygın kısaltma SVD'dir; İngilizce adı olan *singular value decomposition* sözcüklerinin baş harflerinden gelir.

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ için şu geçerlidir:

$$\mathbf{A}=\underbrace{\frac1{\sqrt5}\begin{pmatrix}2&-1\\1&2\end{pmatrix}}_{\mathbf{U}}\underbrace{\begin{pmatrix}4&0\\0&1\end{pmatrix}}_{\mathbf{D}}\underbrace{\frac1{\sqrt5}\begin{pmatrix}1&2\\-2&1\end{pmatrix}}_{\mathbf{V}^{\top}},$$

çünkü $\mathbf{U}\mathbf{D}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}8&-1\\4&2\end{smallmatrix}\bigr)$ ve $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\tfrac15\bigl(\begin{smallmatrix}8+2&16-1\\4-4&8+2\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ olur. Kompakt biçimde:

$$4\cdot\frac15\begin{pmatrix}2&4\\1&2\end{pmatrix}+1\cdot\frac15\begin{pmatrix}2&-1\\-4&2\end{pmatrix}=\begin{pmatrix}1{,}6&3{,}2\\0{,}8&1{,}6\end{pmatrix}+\begin{pmatrix}0{,}4&-0{,}2\\-0{,}8&0{,}4\end{pmatrix}=\begin{pmatrix}2&3\\0&2\end{pmatrix}.$$

⁠**Kısacası:** Her matris, iki ortogonal matris ve $\mathbf{D}$ matrisinin köşegenindeki tekil değerlerle $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ biçimindedir; buna denk olarak bir $\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$ toplamıdır.

:::hintergrund Ayrışım neden her matris için vardır
Özvektörleri olmayan matrisler vardır ve bir matrisin özvektörleri her zaman birbirine dik değildir. Tekil değer ayrışımı iki engeli de bir hileyle aşar: $\mathbf{A}$ matrisinin özvektörlerini değil, $\mathbf{A}^{\top}\mathbf{A}$ matrisininkileri kullanır. Bu matris her $\mathbf{A}$ için simetrik ve pozitif yarı tanımlıdır; spektral teorem de onun için, özdeğerleri $\ge0$ olan özvektörlerden oluşan bir ortonormal tabanı güvence altına alır. Bedeli şudur: Bir yerine iki taban gerekir, biri girişler, biri çıkışlar için.

Tekil vektörler $\mathbf{A}^{\top}\mathbf{A}$ olmadan da betimlenebilir. [(8.2)](positiv-definite-matrizen.html#gl-8-2) eşitsizliği $\mathbf{A}^{\top}\mathbf{A}$ matrisine uygulanırsa birim vektörler için $\lVert\mathbf{A}\mathbf{v}\rVert^2=\mathbf{v}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}\le\lambda_1=d_1^2$ olur; eşitlik $\mathbf{v}_1$ için sağlanır. Demek ki $\mathbf{v}_1$, $\mathbf{A}$ matrisinin en çok uzattığı doğrultudur ve $d_1$ bu en büyük uzatmadır. $\mathbf{v}_1$ vektörüne dik bütün birim vektörler arasında en çok uzatılan $\mathbf{v}_2$ olur ve bu böyle sürer; bunu, [(8.2)](positiv-definite-matrizen.html#gl-8-2) bağıntısının ispatındaki ortalama hesabının aynısı $c_1=0$ ile gösterir. Demek ki ayrışım doğrultuları en güçlü uzatmadan en zayıfına doğru sırayla sayar.

Tek türlü belirli olan, tekil değerlerdir. Bütün $d_j$ farklı ve pozitifse her $\mathbf{v}_j,\mathbf{u}_j$ çifti, ortak bir işaret dışında belirlidir. Eşit tekil değerlerde daha fazla serbestlik vardır: Ortogonal bir $\mathbf{Q}$ matrisinin bütün tekil değerleri $1$ olur ve her $\mathbf{V}$ ortogonal matrisi için $\mathbf{Q}=(\mathbf{Q}\mathbf{V})\,\mathbf{I}\,\mathbf{V}^{\top}$ bir tekil değer ayrışımıdır.
:::

### Dönme, germe, dönme

<span class="anker" id="stufe-9-5"></span>

$\mathbf{A}\mathbf{x}=\mathbf{U}\bigl(\mathbf{D}(\mathbf{V}^{\top}\mathbf{x})\bigr)$ sağdan sola okunursa her matris üç adımda etki eder (Şekil [23](#abb-23)):

<ol>

<li>

$\mathbf{V}^{\top}\mathbf{x}$, [(1.2)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-2) uyarınca $\mathbf{x}$ vektörünün $\mathbf{v}_j$ tabanındaki $c_j=\mathbf{v}_j^{\top}\mathbf{x}$ koordinatlarını hesaplar. Geometrik olarak bu, $\mathbf{v}_j$ vektörünü $\mathbf{e}_j$ vektörünün üzerine getiren bir dönme ya da yansımadır.

</li>

<li>

$\mathbf{D}$ her $c_j$ koordinatını $d_j$ ile çarpar. $m>n$ ise $\mathbf{D}$ sıfırlar ekler, $m<n$ ise $\mathbf{D}$ son koordinatları atar. Birim çember, eksenleri koordinat eksenleri üzerinde olan bir elipse dönüşür.

</li>

<li>

$\mathbf{U}$, $\mathbf{e}_j$ vektörünü $\mathbf{u}_j$ vektörünün üzerine getirir; bu da yine bir dönme ya da yansımadır.

</li>

</ol>

Demek ki her doğrusal dönüşüm, yansımalar bir yana bırakılırsa, bir dönme, eksenler boyunca bir germe ve bir dönme daha demektir. Birim çemberi bir elipse, birim küreyi bir elipsoide dönüştürür; yarı eksenler $d_j\mathbf{u}_j$ olur. $\det\mathbf{A}<0$ ise en az bir yansıma işin içindedir, çünkü Temeller 1, Kesim 14.5'e göre $\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$ ve $\det\mathbf{D}\ge0$ olur.

:::abbildung ml/k2svd 23
$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ matrisi dönme, germe, dönme olarak. Sol üstte $\mathbf{v}_1=(1,2)^{\top}/\sqrt5$ (kırmızı) ve $\mathbf{v}_2=(-2,1)^{\top}/\sqrt5$ (yeşil) ile birim çember. $\mathbf{V}^{\top}$ matrisi $-63{,}4^\circ$ kadar döndürür ve $\mathbf{v}_1$ vektörünü $\mathbf{e}_1$, $\mathbf{v}_2$ vektörünü $\mathbf{e}_2$ üzerine getirir (sol alt). $\mathbf{D}$ birinci ekseni $d_1=4$, ikinciyi $d_2=1$ katına uzatır (sağ alt). $\mathbf{U}$ matrisi $26{,}6^\circ$ kadar döndürür ve eksenleri $\mathbf{u}_1=(2,1)^{\top}/\sqrt5$ ve $\mathbf{u}_2=(-1,2)^{\top}/\sqrt5$ üzerine getirir (sağ üst). Siyah $\mathbf{x}=\mathbf{e}_2$ noktası her yoldan $\mathbf{A}\mathbf{x}=(3,2)^{\top}$ noktasına varır. Üstteki doğrudan yol $\mathbf{A}$ matrisinin kendisidir: Birim çember, yarı eksenleri $4\,\mathbf{u}_1$ ve $1\cdot\mathbf{u}_2$ olan elipse dönüşür.
:::

⁠**Sayısal örnek:** $\mathbf{x}=\mathbf{e}_2$ ve $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ için koordinatlar $\mathbf{V}^{\top}\mathbf{x}=(2,\,1)^{\top}/\sqrt5$ olur. Germe $\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=(8,\,1)^{\top}/\sqrt5$ verir, döndürme de şunu:

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=\frac15\begin{pmatrix}2&-1\\1&2\end{pmatrix}\begin{pmatrix}8\\1\end{pmatrix}=\frac15\begin{pmatrix}15\\10\end{pmatrix}=\begin{pmatrix}3\\2\end{pmatrix}=\mathbf{A}\mathbf{e}_2 .$$

$\mathbf{V}$ matrisinin sütunları, $\cos\theta=1/\sqrt5$ olmak üzere $(\cos\theta,\,\sin\theta)^{\top}$ ve $(-\sin\theta,\,\cos\theta)^{\top}$ olur; yani bu matris $\theta\approx63{,}4^\circ$ kadar dönmedir ve $\mathbf{V}^{\top}$ matrisi $-63{,}4^\circ$ kadar geri döndürür. $\mathbf{U}$, $26{,}6^\circ$ kadar dönmedir, çünkü $\cos26{,}6^\circ\approx2/\sqrt5$.

⁠**Kısacası:** Her matris, yansımalar bir yana, döndürür, eksenler boyunca gerer ve yeniden döndürür; birim çember, yarı eksenleri $d_j\mathbf{u}_j$ olan bir elipse dönüşür.

### Rankı 1 olan yapı taşları ve bir matrisin uzayları

<span class="anker" id="stufe-9-6"></span>

[(9.4)](#gl-9-4) kompakt biçimindeki her $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ teriminin rankı $1$ olur, çünkü bütün sütunları $\mathbf{u}_j$ vektörünün katlarıdır. Bu terim bir vektöre şöyle etki eder:

$$d_j\mathbf{u}_j\mathbf{v}_j^{\top}\mathbf{x}=d_j\,(\mathbf{v}_j^{\top}\mathbf{x})\,\mathbf{u}_j .$$

$\mathbf{x}$ vektörünün $\mathbf{v}_j$ boyunca koordinatını okur, onu $d_j$ ile çarpar ve sonucu $\mathbf{u}_j$ doğrultusunda verir. Matris, $d_j$ büyüklüklerine göre sıralanmış böyle $r$ yapı taşının toplamıdır. Ayrışım, yan ürün olarak bir matrise ait alt uzaylar için ortonormal tabanlar da verir.

:::satz Teorem 9.5 (Tekil vektörlerin gerdikleri)
<span class="anker" id="satz-9-5"></span>

$\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ ve rank $r$ olsun. O zaman şunlar geçerlidir:

<ol class="rm">

<li>

$\mathbf{u}_1,\dots,\mathbf{u}_r$, $\mathbf{A}$ matrisinin sütun uzayının bir ortonormal tabanıdır; $\mathbf{u}_{r+1},\dots,\mathbf{u}_m$ de bu uzayın ortogonal tümleyeninin bir ortonormal tabanıdır;

</li>

<li>

$\mathbf{v}_{r+1},\dots,\mathbf{v}_n$, $\mathbf{A}$ matrisinin çekirdeğinin bir ortonormal tabanıdır; $\mathbf{v}_1,\dots,\mathbf{v}_r$ de $\mathbf{A}^{\top}$ matrisinin sütun uzayının bir ortonormal tabanıdır.

</li>

</ol>
:::

:::beweis Uzaylar
(i) Her $\mathbf{A}\mathbf{x}=\sum_{j\le r}d_j(\mathbf{v}_j^{\top}\mathbf{x})\mathbf{u}_j$ vektörü $\mathbf{u}_1,\dots,\mathbf{u}_r$ vektörlerinin gerdiği alt uzaydadır; tersine $\mathbf{u}_j=\mathbf{A}(\mathbf{v}_j/d_j)$ bir görüntüdür. $\mathbf{U}$ matrisinin geri kalan sütunları bunlara diktir, dolayısıyla Kesim [4.4](projektion-auf-einen-unterraum.html#stufe-4-4)'e göre ortogonal tümleyeni gerer. (ii) $\mathbf{u}_j$ vektörleri bağımsız ve $d_j$ sayıları pozitif olduğundan $\mathbf{A}\mathbf{x}=\mathbf{0}$ eşitliği ancak ve ancak bütün $j\le r$ için $\mathbf{v}_j^{\top}\mathbf{x}=0$ ise, yani $\mathbf{x}$ vektörünün yalnızca $\mathbf{v}_{r+1},\dots,\mathbf{v}_n$ boyunca koordinatları varsa sağlanır. Son olarak $\mathbf{A}^{\top}=\mathbf{V}\mathbf{D}^{\top}\mathbf{U}^{\top}$, $\mathbf{A}^{\top}$ matrisinin bir tekil değer ayrışımıdır ve bu ayrışımda $\mathbf{U}$ ile $\mathbf{V}$ rollerini değiş tokuş eder; (i) şıkkı $\mathbf{A}^{\top}$ için uygulanınca geri kalanı verir.
:::

Sayılar Temeller 1, Kesim 13.5'teki rank-sıfırlık teoremiyle uyumludur: Çekirdeğin boyutu $n-r$ olur.

⁠**Sayısal örnek:** Kesim [3.2](die-beste-naherungslosung.html#stufe-3-2)'deki, sütunları $(1,\,0,\,1)^{\top}$ ve $(0,\,1,\,1)^{\top}$ olan $\mathbf{H}$ matrisi için $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ olur; özdeğerleri $3$ ve $1$, dolayısıyla tekil değerleri $d_1=\sqrt3$ ve $d_2=1$, sağ tekil vektörleri de $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$, $\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$ olur. Sol tekil vektörler şunlardır:

$$\mathbf{u}_1=\frac{\mathbf{H}\mathbf{v}_1}{\sqrt3}=\frac1{\sqrt6}\begin{pmatrix}1\\1\\2\end{pmatrix},\qquad \mathbf{u}_2=\frac{\mathbf{H}\mathbf{v}_2}{1}=\frac1{\sqrt2}\begin{pmatrix}1\\-1\\0\end{pmatrix}.$$

Bunlar $x_3=x_1+x_2$ düzleminin, Kesim [4.3](projektion-auf-einen-unterraum.html#stufe-4-3)'tekinden farklı bir ortonormal tabanını oluşturur. Bu taban, Kesim [4.4](projektion-auf-einen-unterraum.html#stufe-4-4)'teki normlanmış normal vektör olan $\mathbf{u}_3=(1,\,1,\,-1)^{\top}/\sqrt3$ ile tamamlanır. Tam ayrışımda $\mathbf{D}=\Bigl(\begin{smallmatrix}\sqrt3&0\\0&1\\0&0\end{smallmatrix}\Bigr)$ olur. Çekirdek yalnızca sıfır vektöründen oluşur, çünkü $r=n=2$.

⁠**Kısacası:** Bir matris, rankı $1$ olan $r$ tane $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ yapı taşının toplamıdır; $d_j>0$ olan $\mathbf{u}_j$ vektörleri sütun uzayını, $d_j=0$ olan $\mathbf{v}_j$ vektörleri çekirdeği gerer.

### Simetrik matrisler

<span class="anker" id="stufe-9-7"></span>

Simetrik bir matrisin zaten bir ortonormal tabanla bir ayrışımı vardır: $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$. Bu ayrışımın tekil değer ayrışımıyla ilişkisi nedir?

:::satz Teorem 9.6 (Simetrik matrislerin tekil değerleri)
<span class="anker" id="satz-9-6"></span>

Simetrik bir matrisin tekil değerleri, özdeğerlerinin $|\lambda_i|$ mutlak değerleridir. $\mathbf{q}_i$, $\lambda_i\ne0$ özdeğerine ait normlanmış bir özvektörse $\mathbf{v}=\mathbf{q}_i$ bir sağ tekil vektör, $\mathbf{u}=\operatorname{sign}(\lambda_i)\,\mathbf{q}_i$ de buna ait sol tekil vektördür.
:::

:::beweis Simetrik matrisler
$\mathbf{A}^{\top}\mathbf{A}=\mathbf{A}^2=\mathbf{Q}\boldsymbol{\Lambda}^2\mathbf{Q}^{\top}$ olur; dolayısıyla $\mathbf{A}^{\top}\mathbf{A}$ matrisinin özvektörleri $\mathbf{q}_i$, özdeğerleri $\lambda_i^2$ olur ve tekil değerler $\sqrt{\lambda_i^2}=|\lambda_i|$ çıkar. [(9.2)](#gl-9-2) uyarınca $\mathbf{u}=\mathbf{A}\mathbf{q}_i/|\lambda_i|=(\lambda_i/|\lambda_i|)\,\mathbf{q}_i$ olur.
:::

$\mathbf{A}$ pozitif yarı tanımlıysa spektral ayrışım ile tekil değer ayrışımı, $\mathbf{U}=\mathbf{V}=\mathbf{Q}$ olmak üzere aynı ayrışımdır. Negatif özdeğerlerde işaret $\mathbf{U}$ matrisine geçer. Simetrik olmayan matrislerde özdeğerlerle tekil değerlerin genel olarak birbiriyle bir ilgisi yoktur; bunu özdeğerleri $2,2$, tekil değerleri $4,1$ olan $\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ matrisi gösterir. Yine de her zaman bir bağlantı vardır: Her özdeğerin mutlak değeri en fazla $d_1$ olur; bu, sonraki alt kesimden çıkar.

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ matrisinin özdeğerleri, $\mathbf{q}_1=(1,\,1)^{\top}/\sqrt2$ özvektörüyle $4$ ve $\mathbf{q}_2=(1,\,-1)^{\top}/\sqrt2$ özvektörüyle $-2$ olur. Tekil değerler $4$ ve $2$. $\mathbf{v}_2=\mathbf{q}_2$ ile $\mathbf{A}\mathbf{v}_2=(-2,\,2)^{\top}/\sqrt2=2\cdot(-1,\,1)^{\top}/\sqrt2$, dolayısıyla $\mathbf{u}_2=-\mathbf{q}_2$ olur.

⁠**Kısacası:** Simetrik matrislerde tekil değerler özdeğerlerin mutlak değerleridir; pozitif yarı tanımlı olanlarda tekil değer ayrışımı spektral ayrışımın kendisidir.

### Spektral norm

<span class="anker" id="stufe-9-8"></span>

Bir matris bir vektörü en fazla ne kadar uzatabilir? Vektörlerde büyüklüğü norm ölçer. Bir matris için doğal bir büyüklük, en güçlü uzatma çarpanıdır.

:::definition Tanım 9.7 (Spektral norm)
<span class="anker" id="satz-9-7"></span>

Bir $\mathbf{A}$ matrisinin __spektral normu__ şudur:

$$\lVert\mathbf{A}\rVert_2=\max_{\mathbf{x}\ne\mathbf{0}}\frac{\lVert\mathbf{A}\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert} .$$
:::

:::satz Teorem 9.8 (En büyük ve en küçük uzatma)
<span class="anker" id="satz-9-8"></span>

Tekil değerleri $d_1\ge\dots\ge d_n$ olan her $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisi ve her $\mathbf{x}\in\mathbb{R}^n$ vektörü için şu geçerlidir:

<span class="anker" id="gl-9-5"></span>
$$d_n\,\lVert\mathbf{x}\rVert\le\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\,\lVert\mathbf{x}\rVert . \tag{9.5}$$

Sınırlara $\mathbf{x}=\mathbf{v}_1$ ve $\mathbf{x}=\mathbf{v}_n$ için ulaşılır. Özellikle $\lVert\mathbf{A}\rVert_2=d_1$ olur.
:::

:::beweis En büyük ve en küçük uzatma
$\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$ ile $\lVert\mathbf{c}\rVert=\lVert\mathbf{x}\rVert$ ve $\lVert\mathbf{A}\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\sum_jd_j^2c_j^2$ olur. Bu, $d_n^2\sum_jc_j^2$ ile $d_1^2\sum_jc_j^2$ arasındadır. Bu ifade, $\mathbf{A}^{\top}\mathbf{A}$ matrisinin $\lVert\mathbf{x}\rVert^2$ ile çarpılmış [(8.2)](positiv-definite-matrizen.html#gl-8-2) Rayleigh bölümüdür.
:::

İki sonuç. Birincisi, $\lVert\mathbf{A}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{x}\rVert$, dolayısıyla $\lVert\mathbf{A}\mathbf{B}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2\lVert\mathbf{x}\rVert$, yani $\lVert\mathbf{A}\mathbf{B}\rVert_2\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2$ olur: Matrisler art arda uygulandığında en büyük uzatma çarpanları en fazla birbiriyle çarpılır. İkincisi, bir özvektör için $\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$ olur; dolayısıyla bir kare matrisin her özdeğeri için $|\lambda|\le d_1$. Gerçel $\mathbf{a},\mathbf{b}$ olmak üzere karmaşık bir $\mathbf{v}=\mathbf{a}+\mathrm j\mathbf{b}$ özvektörü için de, $\lVert\mathbf{v}\rVert^2=(\mathbf{v}^*)^{\top}\mathbf{v}=\lVert\mathbf{a}\rVert^2+\lVert\mathbf{b}\rVert^2$ alınırsa aynısı geçerlidir, çünkü $\lVert\mathbf{A}\mathbf{v}\rVert^2=\lVert\mathbf{A}\mathbf{a}\rVert^2+\lVert\mathbf{A}\mathbf{b}\rVert^2$ ifadesi [(9.5)](#gl-9-5) uyarınca $d_n^2\lVert\mathbf{v}\rVert^2$ ile $d_1^2\lVert\mathbf{v}\rVert^2$ arasındadır; demek ki kare bir $\mathbf{A}$ için ayrıca $|\lambda|\ge d_n$ olur.

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ için $\lVert\mathbf{A}\rVert_2=4$ olur. Birim vektörler daha az uzatılır: $\lVert\mathbf{A}\mathbf{e}_1\rVert=\lVert(2,\,0)^{\top}\rVert=2$ ve $\lVert\mathbf{A}\mathbf{e}_2\rVert=\lVert(3,\,2)^{\top}\rVert=\sqrt{13}\approx3{,}61$. $4$ çarpanına yalnızca $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$ için, en küçük çarpan olan $1$ değerine de $\mathbf{v}_2$ için ulaşılır. $2$ özdeğeri $1$ ile $4$ arasındadır.

⁠**Kısacası:** $\lVert\mathbf{A}\rVert_2=d_1$ spektral normu, $\mathbf{A}$ matrisinin bir vektörü uzattığı en büyük çarpandır; en küçüğü $d_n$ olur.

:::hintergrund Birden çok anten: tekil değer ayrışımından paralel kanallar
Birden çok verici ve alıcı anteni olan bir telsiz sisteme MIMO sistemi denir. Her alıcı anten bütün verici sinyallerinin bir karışımını alır. Basit bir modelde alınan vektör $\mathbf{y}=\mathbf{K}\mathbf{x}+\boldsymbol\nu$ olur: $\mathbf{x}$ antenlerin gönderdiği sinyalleri içerir, $\mathbf{K}$ kanal matrisi her verici antenin her alıcı antene ne kadar güçlü ulaştığını betimler, $\boldsymbol\nu$ ise gürültüdür.

Verici ve alıcı $\mathbf{K}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ ayrışımını biliyorsa verici $\mathbf{x}=\mathbf{V}\tilde{\mathbf{x}}$ gönderir, alıcı da $\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{y}$ hesaplar. O zaman şu bulunur:

$$\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\tilde{\mathbf{x}}+\mathbf{U}^{\top}\boldsymbol\nu=\mathbf{D}\tilde{\mathbf{x}}+\tilde{\boldsymbol\nu} .$$

Karışık kanaldan $r$ ayrı kanal oluşmuştur: $\tilde y_j=d_j\tilde x_j+\tilde\nu_j$. Her biri kendi veri akışını $d_j$ kazanç çarpanıyla iletir. Gürültü bu sırada yalnızca döndürülür, uzunluğu aynı kalır, çünkü $\mathbf{U}^{\top}$ ortogonaldir. Kullanılabilir paralel kanalların sayısı kanal matrisinin rankıdır; her kanalın ne kadar iyi olduğunu da tekil değeri söyler. Bu, uygulamada dönme, germe, dönmedir: Verici önceden döndürür, kanal gerer, alıcı geri döndürür.
:::

:::aufgabe Alıştırma 27 ★★ Elle bir ayrışım
<span class="anker" id="aufg-27"></span>

$\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$ olsun.

<ol class="al">

<li>

$\mathbf{A}^{\top}\mathbf{A}$ matrisini, özdeğerlerini ve $\mathbf{A}$ matrisinin tekil değerlerini hesaplayın.

</li>

<li>

$\mathbf{v}_1,\mathbf{v}_2$ vektörlerini ve bunlardan [(9.2)](#gl-9-2) ile $\mathbf{u}_1,\mathbf{u}_2$ vektörlerini bulun. $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ eşitliğini doğrulayın.

</li>

<li>

Tekil değerleri $\mathbf{A}$ matrisinin özdeğerleriyle karşılaştırın. Ne uyuşuyor, ne uyuşmuyor?

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}9+16&20\\20&25\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}25&20\\20&25\end{smallmatrix}\bigr)$ olur; izi $50$, determinantı $625-400=225$, dolayısıyla $\lambda^2-50\lambda+225=(\lambda-45)(\lambda-5)$. Tekil değerler $d_1=\sqrt{45}=3\sqrt5\approx6{,}708$ ve $d_2=\sqrt5\approx2{,}236$ olur.

(b) $\mathbf{A}^{\top}\mathbf{A}$ matrisinin özvektörleri: $45$ için $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ ve $5$ için $\mathbf{v}_2=(-1,\,1)^{\top}/\sqrt2$. Sonra şu bulunur:

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}{d_1}=\frac{(3,\,9)^{\top}}{\sqrt2\cdot3\sqrt5}=\frac{(1,\,3)^{\top}}{\sqrt{10}},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{d_2}=\frac{(-3,\,1)^{\top}}{\sqrt2\cdot\sqrt5}=\frac{(-3,\,1)^{\top}}{\sqrt{10}} .$$

Sağlama: $\mathbf{U}\mathbf{D}=\tfrac1{\sqrt{10}}\bigl(\begin{smallmatrix}3\sqrt5&-3\sqrt5\\9\sqrt5&\sqrt5\end{smallmatrix}\bigr)=\tfrac1{\sqrt2}\bigl(\begin{smallmatrix}3&-3\\9&1\end{smallmatrix}\bigr)$ ve

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\frac1{\sqrt2}\begin{pmatrix}3&-3\\9&1\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\frac12\begin{pmatrix}6&0\\8&10\end{pmatrix}=\begin{pmatrix}3&0\\4&5\end{pmatrix}.$$

(c) Üçgen matrisin özdeğerleri $3$ ve $5$ olur. Çarpımlar uyuşur: $3\cdot5=15=3\sqrt5\cdot\sqrt5=|\det\mathbf{A}|$. Toplamlar uyuşmaz: $8$ ile $4\sqrt5\approx8{,}94$. Özdeğerlerin mutlak değerleri $d_2$ ile $d_1$ arasındadır: $2{,}236\le3$ ve $5\le6{,}708$.
:::
:::

:::aufgabe Alıştırma 28 ★★ Dikdörtgen bir matris
<span class="anker" id="aufg-28"></span>

$\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$ olsun.

<ol class="al">

<li>

Tekil değerleri ve $\mathbf{v}_1,\mathbf{v}_2,\mathbf{u}_1,\mathbf{u}_2$ tekil vektörlerini bulun.

</li>

<li>

$\mathbf{u}_3$ vektörünü ekleyin ve $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ tam ayrışımını yazın.

</li>

<li>

Sütun uzayının ve onun ortogonal tümleyeninin ortonormal tabanlarını verin.

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ matrisinin özdeğerleri $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ ile $4$ ve $\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$ ile $2$ olur. Dolayısıyla $d_1=2$, $d_2=\sqrt2$ ve

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}2=\frac{(2,\,2,\,0)^{\top}}{2\sqrt2}=\frac{(1,\,1,\,0)^{\top}}{\sqrt2},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{\sqrt2}=\frac{(0,\,0,\,2)^{\top}}{\sqrt2\cdot\sqrt2}=(0,\,0,\,1)^{\top} .$$

(b) $\mathbf{u}_3$ ikisine de diktir: $\mathbf{u}_3=(1,\,-1,\,0)^{\top}/\sqrt2$. Tam ayrışım şudur:

$$\mathbf{A}=\begin{pmatrix}1/\sqrt2&0&1/\sqrt2\\1/\sqrt2&0&-1/\sqrt2\\0&1&0\end{pmatrix}\begin{pmatrix}2&0\\0&\sqrt2\\0&0\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$

(c) Kesim [9.6](#stufe-9-6)'daki teoreme göre $\mathbf{u}_1,\mathbf{u}_2$ sütun uzayının bir ortonormal tabanıdır, $\mathbf{u}_3$ de ortogonal tümleyeninin bir ortonormal tabanıdır. Sağlama: $(1,\,1,\,1)^{\top}=\sqrt2\,\mathbf{u}_1+\mathbf{u}_2$ ve $(1,\,1,\,-1)^{\top}=\sqrt2\,\mathbf{u}_1-\mathbf{u}_2$ sütunları $\mathbf{u}_1,\mathbf{u}_2$ vektörlerinin gerdiği alt uzaydadır ve ikisi de $\mathbf{u}_3$ vektörüne diktir.
:::
:::

:::aufgabe Alıştırma 29 ★★★ Tekil değerlerin özellikleri
<span class="anker" id="aufg-29"></span>

<ol class="al">

<li>

Gösterin: Bir kare matris için $|\det\mathbf{A}|=d_1d_2\cdots d_n$ olur.

</li>

<li>

Gösterin: $\mathbf{A}$ ile $\mathbf{A}^{\top}$ matrislerinin pozitif tekil değerleri aynıdır.

</li>

<li>

Gösterin: $\mathbf{u}\ne\mathbf{0}$ ve $\mathbf{v}\ne\mathbf{0}$ için $\mathbf{u}\mathbf{v}^{\top}$ dış çarpımının tam olarak bir pozitif tekil değeri vardır, o da $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$ değeridir.

</li>

<li>

Gösterin: $\mathbf{Q}$ ortogonal ise $\mathbf{Q}\mathbf{A}$ ile $\mathbf{A}$ matrislerinin tekil değerleri aynıdır.

</li>

</ol>

:::loesung
(a) Temeller 1, Kesim 14.5'e göre $\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$ olur. İki ortogonal matrisin determinantı $\pm1$ olur, $\mathbf{D}$ ise determinantı $d_1\cdots d_n$ olan bir köşegen matristir. Dolayısıyla $|\det\mathbf{A}|=d_1\cdots d_n$.

(b) $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ eşitliğinden $\mathbf{A}^{\top}\mathbf{A}=\mathbf{V}\mathbf{D}^{\top}\mathbf{D}\mathbf{V}^{\top}$ ve $\mathbf{A}\mathbf{A}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^{\top}\mathbf{U}^{\top}$ çıkar. $\mathbf{D}^{\top}\mathbf{D}$ ve $\mathbf{D}\mathbf{D}^{\top}$ köşegen matrislerinin köşegeninde aynı $d_j^2>0$ elemanları bulunur, yalnızca sıfırların sayısı farklıdır. $\mathbf{A}^{\top}$ matrisinin tekil değerleri $(\mathbf{A}^{\top})^{\top}\mathbf{A}^{\top}=\mathbf{A}\mathbf{A}^{\top}$ matrisinin özdeğerlerinin karekökleridir, yani yine $d_j$ değerleri ve bunlara eklenen sıfırlar.

(c) $(\mathbf{u}\mathbf{v}^{\top})^{\top}(\mathbf{u}\mathbf{v}^{\top})=\mathbf{v}\,\mathbf{u}^{\top}\mathbf{u}\,\mathbf{v}^{\top}=\lVert\mathbf{u}\rVert^2\,\mathbf{v}\mathbf{v}^{\top}$ olur. Bu matris $\mathbf{v}$ vektörünü $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2\,\mathbf{v}$ vektörüne, $\mathbf{v}$ vektörüne dik her vektörü de sıfıra götürür. Dolayısıyla özdeğerleri $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$ ve geri kalanlar için $0$ olur; tek pozitif tekil değer de $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$ olur.

(d) $(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$ olur. İki matrisin Gram matrisi aynıdır, dolayısıyla tekil değerleri de aynıdır. Sezgisel olarak: $\mathbf{A}$ matrisinden sonra uygulanan bir dönme ya da yansıma elipsin biçimini değiştirmez, yalnızca konumunu değiştirir.
:::
:::
