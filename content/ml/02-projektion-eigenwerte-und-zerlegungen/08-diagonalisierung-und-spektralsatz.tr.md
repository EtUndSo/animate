---
title: Köşegenleştirme ve spektral teorem
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
knoten: Temeller 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15220800
summary: Bir matris kendi özvektörlerinden oluşan bir tabanda betimlenirse köşegen olur: Her koordinat yalnızca kendi özdeğeriyle çarpılır ve birbirine bağlı hesaplar tek tek hesaplara ayrılır.
tags: taban değişimi, köşegenleştirilebilir, asal eksenleri
lang: tr
---

<span class="anker" id="stufe-7"></span>

:::zweck
Bir matris kendi özvektörlerinden oluşan bir tabanda betimlenirse köşegen olur: Her koordinat yalnızca kendi özdeğeriyle çarpılır ve birbirine bağlı hesaplar tek tek hesaplara ayrılır. Bu kesim bunun ne zaman mümkün olduğunu gösteriyor ve simetrik matrislerde her zaman, hem de bir ortonormal tabanla mümkün olduğunu kanıtlıyor.
:::

### Taban değişimi

<span class="anker" id="stufe-7-1"></span>

Aynı okun farklı tabanlarda farklı koordinatları vardır. Aynı şekilde aynı doğrusal dönüşümün farklı koordinatlarda farklı matrisleri vardır. Bazı tabanlar matrisi özellikle basit kılar.

$\mathbf s_1,\dots,\mathbf s_n$, $\mathbb{R}^n$ uzayının bir tabanı, $\mathbf{S}$ de sütunları bu vektörler olan matris olsun. [Temeller 1, Kesim 13.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5)'e göre bu matris tersinirdir. $\mathbf{x}$ vektörünün bu tabandaki koordinatları $\mathbf{c}$ ise $\mathbf{x}=\sum_ic_i\mathbf s_i=\mathbf{S}\mathbf{c}$ olur, tersine de $\mathbf{c}=\mathbf{S}^{-1}\mathbf{x}$. $\mathbf{x}$ vektörüne $\mathbf{A}$ uygulanırsa $\mathbf{A}\mathbf{x}$ görüntüsünün koordinatları $\mathbf{S}^{-1}\mathbf{A}\mathbf{x}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}\,\mathbf{c}$ olur. Demek ki yeni koordinatlarda dönüşüm $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ matrisiyle etki eder: Önce eski koordinatlara çevrilir, sonra dönüşüm uygulanır, sonra geri çevrilir.

:::definition Tanım 7.1 (Taban değişimi)
<span class="anker" id="satz-7-1"></span>

$\mathbf{S}$ tersinir ise $\mathbf{B}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ matrisine $\mathbf{A}$ dönüşümünün, $\mathbf{S}$ matrisinin sütunlarından oluşan tabandaki matrisi denir. $\mathbf{A}$ matrisinden $\mathbf{B}$ matrisine geçişe __taban değişimi__ denir.
:::

Birbiriyle bu şekilde ilişkili iki matrise benzer matrisler denir. Aynı dönüşümü betimlerler, yalnızca farklı koordinatlarda.

:::satz Teorem 7.2 (Taban değişiminin değiştirmedikleri)
<span class="anker" id="satz-7-2"></span>

$\mathbf{A}$ ve $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ matrislerinin karakteristik polinomu aynıdır; dolayısıyla özdeğerleri, izleri ve determinantları da aynıdır.
:::

:::beweis Taban değişimi
$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}-\lambda\mathbf{I}=\mathbf{S}^{-1}(\mathbf{A}-\lambda\mathbf{I})\mathbf{S}$ olur. [Temeller 1, Kesim 14.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5)'teki hesap kurallarına göre bunun determinantı $\det\mathbf{S}^{-1}\cdot\det(\mathbf{A}-\lambda\mathbf{I})\cdot\det\mathbf{S}=\det(\mathbf{A}-\lambda\mathbf{I})$ olur. İz ve determinant [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5) uyarınca özdeğerlerden belirlenir.
:::

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ ve [Temeller 1, Kesim 13.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3)'teki $(1,\,0)^{\top}$, $(1,\,1)^{\top}$ tabanı için $\mathbf{S}=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ ve $\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}1&-1\\0&1\end{smallmatrix}\bigr)$ olur. O zaman şu bulunur:

$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}4&5\\2&5\end{pmatrix}=\begin{pmatrix}2&0\\2&5\end{pmatrix}.$$

İz yine $7$, determinant yine $10$; özdeğerler de şimdi bir üçgen matrisin köşegeninde durur: $2$ ve $5$.
::::

⁠**Kısacası:** $\mathbf{S}$ matrisinin sütunlarından oluşan tabanda $\mathbf{A}$ dönüşümünün matrisi $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ olur; özdeğerler, iz ve determinant bu sırada değişmez.

### Köşegenleştirme

<span class="anker" id="stufe-7-2"></span>

Mümkün olan en basit matris köşegen matristir: Her koordinatı, koordinatları birbirine karıştırmadan kendine ait bir sayıyla çarpar. Taban olarak özvektörler alınırsa her taban vektörü yalnızca kendi özdeğeriyle çarpılır. Demek ki bu tabanda matris köşegendir.

:::satz Teorem 7.3 (Köşegenleştirme)
<span class="anker" id="satz-7-3"></span>

$\mathbf{A}\in\mathbb{R}^{n\times n}$ matrisinin $\lambda_1,\dots,\lambda_n$ özdeğerlerine ait $n$ tane doğrusal bağımsız $\mathbf s_1,\dots,\mathbf s_n$ özvektörü varsa ve $\mathbf{S}$ sütunları bu özvektörler olan matrisse şu geçerlidir:

<span class="anker" id="gl-7-1"></span>
$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\qquad\text{yani}\qquad \mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1} . \tag{7.1}$$

Tersine: $\mathbf{A}$ bu biçimde yazılabiliyorsa $\mathbf{S}$ matrisinin sütunları özvektörlerdir.
:::

:::beweis Köşegenleştirme
[Temeller 1, Kesim 9.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-2)'ye göre $\mathbf{A}\mathbf{S}$ matrisinin $i$ numaralı sütunu $\mathbf{A}\mathbf s_i=\lambda_i\mathbf s_i$ çarpımıdır; $\mathbf{S}\boldsymbol{\Lambda}$ matrisinin $i$ numaralı sütunu da $\lambda_i\mathbf s_i$ olur. Dolayısıyla $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$. $\mathbf{S}$ matrisinin sütunları bağımsızdır, dolayısıyla $\mathbf{S}$ tersinirdir ve soldan $\mathbf{S}^{-1}$ ile çarpma [(7.1)](#gl-7-1) bağıntısını verir. Aynı $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$ denklemi tersten okunursa ters önerme çıkar.
:::

Bu biçimde yazılabilen bir matrise __köşegenleştirilebilir__ denir. Kesim [6.8](eigenwerte-und-eigenvektoren.html#stufe-6-8)'deki teoreme göre bu, örneğin $n$ özdeğerin hepsi farklı olduğunda her zaman böyledir. Kayma köşegenleştirilemez, çünkü bir özvektörü eksiktir. $90^\circ$'lik dönme de gerçel sayılarla köşegenleştirilemez, yalnızca karmaşık sayılarla. İkisi de yine de tersinirdir: Tersinirlik ve köşegenleştirilebilirlik iki ayrı özelliktir.

::::beispiel [Sayısal örnek]
Özvektörleri $(1,\,1)^{\top}$ ve $(1,\,-2)^{\top}$ olan $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ için şu bulunur:

$$\mathbf{S}=\begin{pmatrix}1&1\\1&-2\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix},\qquad \mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix}\begin{pmatrix}5&2\\5&-4\end{pmatrix}=\begin{pmatrix}5&0\\0&2\end{pmatrix}.$$
::::

⁠**Kısacası:** $n$ bağımsız özvektörü olan bir matris, bu özvektörlerin tabanında köşegendir: $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$.

### Ayrıştırma: kuvvetler ve diziler

<span class="anker" id="stufe-7-3"></span>

Bunun ne işe yaradığını, tekrar tekrar uygulanan bir matris gösterir. A ve B adlı iki yerleşim yeri her yıl birbiriyle nüfus alışverişi yapar: A'da oturanların $20\,\%$'si B'ye, B'de oturanların $30\,\%$'u A'ya taşınır, geri kalan herkes yerinde kalır. $\mathbf{x}_k$ vektörü $k$ yılındaki nüfusları gösteriyorsa şu geçerlidir:

$$\mathbf{x}_{k+1}=\mathbf M\mathbf{x}_k\qquad\text{burada}\qquad \mathbf M=\begin{pmatrix}0{,}8&0{,}3\\0{,}2&0{,}7\end{pmatrix}.$$

İki nüfus birbirine bağlıdır: Her yeni değer, eski değerlerin ikisinden de etkilenir. $k$ yıl sonra $\mathbf{x}_k=\mathbf M^k\mathbf{x}_0$ olur. $\mathbf M^k$ kuvvetini doğrudan hesaplamak zahmetlidir ve uzun vadede ne olacağını göstermez. Öz tabanda ise iş basittir.

:::satz Teorem 7.4 (Öz tabanda kuvvetler ve diziler)
<span class="anker" id="satz-7-4"></span>

$\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ ise $\boldsymbol{\Lambda}^k=\operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k)$ olmak üzere $\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$ olur. $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_k$ dizisi için şu geçerlidir:

<span class="anker" id="gl-7-2"></span>
$$\mathbf{x}_k=\sum_{i=1}^nc_i\,\lambda_i^k\,\mathbf s_i\qquad\text{burada}\qquad \mathbf{c}=\mathbf{S}^{-1}\mathbf{x}_0 . \tag{7.2}$$
:::

:::beweis Kuvvetler
$\mathbf{A}^2=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\mathbf{S}\boldsymbol{\Lambda}^2\mathbf{S}^{-1}$, çünkü ortadaki $\mathbf{S}^{-1}\mathbf{S}=\mathbf{I}$ düşer; her kuvvet için de aynısı geçerlidir. $\mathbf{x}_0=\sum_ic_i\mathbf s_i$ biçiminde özvektörlere ayrılırsa $\mathbf{A}$ matrisinin her uygulanışı her payı yalnızca kendi özdeğeriyle çarpar.
:::

Öz tabanın $\mathbf{c}$ koordinatlarında her adım, her koordinatın kendi sayısıyla çarpılmasıdır: $c_i\mapsto\lambda_ic_i$. $n$ bilinmeyenli, birbirine bağlı bir hesaptan, her biri tek bilinmeyenli $n$ ayrı hesap çıkar. Bu koordinatlar ayrışmıştır, yani birbirinden bağımsızdır. Uzun vadede mutlak değerce en büyük özdeğere ait pay baskın çıkar.

::::beispiel [Sayısal örnek]
$\mathbf M$ matrisinin izi $1{,}5$, determinantı $0{,}56-0{,}06=0{,}5$, dolayısıyla özdeğerleri $1$ ve $0{,}5$ olur. $1$ özdeğerine ait bir özvektör $\mathbf s_1=(3,\,2)^{\top}$ olur, çünkü $\mathbf M\mathbf s_1=(2{,}4+0{,}6;\ 0{,}6+1{,}4)^{\top}=\mathbf s_1$; $0{,}5$ özdeğerine ait bir özvektör de $\mathbf s_2=(1,\,-1)^{\top}$. Başlangıçta A'da $1000$ kişi oturuyor, B'de kimse oturmuyorsa $\mathbf{x}_0=(1000,\,0)^{\top}=200\,\mathbf s_1+400\,\mathbf s_2$ olur ve [(7.2)](#gl-7-2) uyarınca şu bulunur:

$$\mathbf{x}_k=200\begin{pmatrix}3\\2\end{pmatrix}+400\cdot0{,}5^k\begin{pmatrix}1\\-1\end{pmatrix}=\begin{pmatrix}600+400\cdot0{,}5^k\\400-400\cdot0{,}5^k\end{pmatrix}.$$

Bir yıl sonra $(800,\,200)^{\top}$, iki yıl sonra $(700,\,300)^{\top}$ olur ve uzun vadede $(600,\,400)^{\top}$ dengesi kurulur. $0{,}5$ özdeğerine ait pay her yıl yarıya iner, $1$ özdeğerine ait pay ise kalır.
::::

⁠**Kısacası:** Öz tabanda matrisin her kuvveti özdeğerlerin kuvvetlerine dönüşür; birbirine bağlı diziler, her özvektör için bir tane olmak üzere ayrı dizilere ayrışır.

:::hintergrund LTI sistemlerindeki ve Fourier dönüşümündeki ilkenin aynısı
Zaman bölgesinde bir LTI sistemi bir evrişimdir: Her çıkış değeri bütün giriş değerlerinden etkilenir, her şey birbirine bağlıdır. Giriş sinyali $\mathrm e^{pt}$ üstel fonksiyonlarına ayrılırsa her biri yalnızca kendi $H(p)$ özdeğeriyle çarpılır ve bu bağ ortadan kalkar. Laplace ve Fourier dönüşümleri sinyaller için, $\mathbf{S}^{-1}$ taban değişiminin vektörler için yaptığını yapar: Özfonksiyonların koordinatlarına çevirirler.

Örneklenmiş sinyallerde bu benzerlik kelimenin tam anlamıyla bir köşegenleştirmedir. Bir $y_k=\sum_lh_{(k-l)\bmod n}\,x_l$ dairesel evrişimi, birinci sütunu $(h_0,\dots,h_{n-1})^{\top}$ dürtü yanıtı, öbür sütunları da bu yanıtın dairesel kaydırmaları olan bir matristir. Bu matrisin özvektörleri, örneklenmiş $\mathbf f_m=\bigl(1,\ \mathrm e^{\mathrm j2\pi m/n},\ \mathrm e^{\mathrm j2\pi\cdot2m/n},\dots\bigr)^{\top}$ karmaşık salınımlarıdır ve $\mathbf f_m$ vektörüne ait özdeğer, dürtü yanıtının ayrık Fourier dönüşümünün $H[m]=\sum_qh_q\,\mathrm e^{-\mathrm j2\pi mq/n}$ değeridir. Demek ki ayrık Fourier dönüşümünün matrisi, $1/n$ çarpanı dışında, her dairesel evrişimi köşegenleştiren $\mathbf{S}^{-1}$ matrisidir, hem de bütün dürtü yanıtları için aynı anda. $n=3$ ve $h=(1;\,0{,}5;\,0)$ ile bir örnek: $\Bigl(\begin{smallmatrix}1&0&0{,}5\\0{,}5&1&0\\0&0{,}5&1\end{smallmatrix}\Bigr)$ matrisi $\mathbf f_0=(1,1,1)^{\top}$ vektörünü $1{,}5\,\mathbf f_0$ vektörüne götürür ve $1{,}5=H[0]=h_0+h_1+h_2$.
:::

### Simetrik matrislerin özdeğerleri gerçeldir

<span class="anker" id="stufe-7-4"></span>

Simetrik matrislerde pek çok şey özellikle basittir. Birincisi: Özdeğerleri her zaman gerçeldir. Demek ki simetrik bir matris, Kesim [6.6](eigenwerte-und-eigenvektoren.html#stufe-6-6)'daki dönmeler gibi bir düzlemi kendi içinde döndürmez.

:::satz Teorem 7.5 (Gerçel özdeğerler)
<span class="anker" id="satz-7-5"></span>

Gerçel simetrik bir matrisin her özdeğeri gerçeldir.
:::

:::beweis Gerçel özdeğerler
$\mathbf{v}\ne\mathbf{0}$ olmak üzere $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ olsun; burada $\lambda$ ve $\mathbf{v}$ şimdilik karmaşık olabilir. İki tarafın eşleniği alınırsa $\mathbf{A}$ gerçel olduğu için değişmez: $\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$. $(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}$ sayısı iki yoldan hesaplanır. Bir kez $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ ile:

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=\lambda\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

Bir kez de $\mathbf{A}=\mathbf{A}^{\top}$ ve $\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$ ile:

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=(\mathbf{A}^{\top}\mathbf{v}^*)^{\top}\mathbf{v}=(\mathbf{A}\mathbf{v}^*)^{\top}\mathbf{v}=\lambda^*\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

Dolayısıyla $(\lambda-\lambda^*)\,(\mathbf{v}^*)^{\top}\mathbf{v}=0$ olur. Kesim [6.1](eigenwerte-und-eigenvektoren.html#stufe-6-1)'e göre $(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0$, dolayısıyla $\lambda=\lambda^*$ ve $\lambda$ gerçeldir.
:::

Gerçel bir özdeğere ait gerçel özvektörler de vardır, çünkü $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ gerçel bir denklem sistemidir.

::::beispiel [Sayısal örnek]
$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ matrisinin karakteristik polinomu $\lambda^2-7\lambda+6$, diskriminantı $49-24=25>0$, gerçel özdeğerleri de $6$ ve $1$ olur. Herhangi bir simetrik $2\times2$ matris $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$ için diskriminant $(a+c)^2-4(ac-b^2)=(a-c)^2+4b^2\ge0$ olur; teoremin söylediği gibi özdeğerler her zaman gerçeldir.
::::

⁠**Kısacası:** Simetrik bir matrisin yalnızca gerçel özdeğerleri ve gerçel özvektörleri vardır.

### Simetrik matrislerin özvektörleri birbirine diktir

<span class="anker" id="stufe-7-5"></span>

$\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ matrisinin özvektörleri birbirine eğikti. Simetrik matrislerde bu olamaz.

:::satz Teorem 7.6 (Ortogonal özvektörler)
<span class="anker" id="satz-7-6"></span>

Simetrik bir matrisin farklı özdeğerlere ait özvektörleri birbirine diktir.
:::

:::beweis Ortogonal özvektörler
$\lambda_1\ne\lambda_2$ olmak üzere $\mathbf{A}\mathbf{v}_1=\lambda_1\mathbf{v}_1$ ve $\mathbf{A}\mathbf{v}_2=\lambda_2\mathbf{v}_2$ olsun. $\mathbf{v}_1^{\top}\mathbf{A}\mathbf{v}_2$ iki yoldan hesaplanır: $\mathbf{v}_1^{\top}(\lambda_2\mathbf{v}_2)=\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2$ olarak ve $\mathbf{A}^{\top}=\mathbf{A}$ kullanılarak $(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\lambda_1\,\mathbf{v}_1^{\top}\mathbf{v}_2$ olarak. Dolayısıyla $(\lambda_1-\lambda_2)\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$ olur ve $\lambda_1\ne\lambda_2$ olduğundan $\mathbf{v}_1^{\top}\mathbf{v}_2=0$.
:::

::::beispiel [Sayısal örnek]
$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ matrisinin $6$ özdeğerine ait özvektörü $(2,\,1)^{\top}$ olur, çünkü $(10+2,\ 4+2)^{\top}=6\,(2,\,1)^{\top}$; $1$ özdeğerine ait özvektörü de $(1,\,-2)^{\top}$ olur, çünkü $(5-4,\ 2-4)^{\top}=(1,\,-2)^{\top}$. İç çarpımları $2-2=0$ (Şekil [19](#abb-19)).

:::abbildung ml/k2rsenkrecht 19
Simetrik $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ matrisinin $6$ özdeğerine ait $(2,1)^{\top}$ ve $1$ özdeğerine ait $(1,-2)^{\top}$ özvektörlerinin iç çarpımı: Bu özvektörler birbirine diktir.
:::
::::

⁠**Kısacası:** Simetrik bir matriste farklı özdeğerlere ait özvektörler birbirine diktir.

:::hintergrund Öz doğrultuları neden tam da simetri dik kılar
İspat simetriyi yalnızca tek bir yerde kullanır: $(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\mathbf{v}_1^{\top}(\mathbf{A}\mathbf{v}_2)$. Simetrik bir matris için bu eşitlik bütün vektörlerde geçerlidir; $\mathbf{A}$ iç çarpımın bir yanından öbür yanına kaydırılabilir. İç çarpım, $\mathbf{v}_2$ vektörünün ne kadarının $\mathbf{v}_1$ doğrultusunu gösterdiğini ölçer. $\mathbf{A}$ doğrultulardan birini $\lambda_1$, öbürünü $\lambda_2$ katına uzatıyorsa bu pay solda $\lambda_1$ ile, sağda $\lambda_2$ ile çarpılır. İki taraf ancak çarpılacak bir şey yoksa, yani pay sıfırsa eşit olabilir. Simetrik olmayan bir matriste bu kaydırma kuralı geçerli değildir ve eğik öz doğrultular mümkündür.

Buradan ikinci önemli bir özellik çıkar. $\mathbf{q}$ bir özvektörse ve $\mathbf{z}$, $\mathbf{q}$ vektörüne dikse $\mathbf{A}\mathbf{z}$ de $\mathbf{q}$ vektörüne diktir: $(\mathbf{A}\mathbf{z})^{\top}\mathbf{q}=\mathbf{z}^{\top}\mathbf{A}\mathbf{q}=\lambda\,\mathbf{z}^{\top}\mathbf{q}=0$. Demek ki simetrik bir matris bir özvektörün ortogonal tümleyenini yine kendi içine götürür. Bir sonraki özvektör orada aranabilir ve bu böyle sürer. Sonraki alt kesimdeki ispat tam olarak böyle işler.
:::

### Spektral teorem

<span class="anker" id="stufe-7-6"></span>

Önceki iki teorem, her simetrik matrisin özvektörlerden oluşan bir ortonormal tabanda köşegen olduğunu düşündürür. Özdeğerler katlı olduğunda da bu doğrudur. Bir matrisin özdeğerlerinin kümesine onun spektrumu denir; teoremin adı buradan gelir.

:::satz Teorem 7.7 (Spektral teorem)
<span class="anker" id="satz-7-7"></span>

Her simetrik $\mathbf{A}\in\mathbb{R}^{n\times n}$ matrisi için, gerçel $\lambda_1,\dots,\lambda_n$ özdeğerlerine ait özvektörlerden oluşan bir $\mathbf{q}_1,\dots,\mathbf{q}_n$ ortonormal tabanı vardır. $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$ ortogonal matrisi ve $\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ ile şu geçerlidir:

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}=\sum_{i=1}^n\lambda_i\,\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{7.3}$$
:::

:::beweis Spektral teorem
Adım adım ilerlenir. Kesim [6.3](eigenwerte-und-eigenvektoren.html#stufe-6-3)'e göre $\mathbf{A}$ matrisinin en az bir $\lambda_1$ özdeğeri vardır; Kesim [7.4](#stufe-7-4)'e göre bu özdeğer gerçeldir ve gerçel bir özvektörü vardır; bu özvektör normlanınca $\mathbf{q}_1$ olur. $\mathbf{q}_1$, $\mathbb{R}^n$ uzayının bir ortonormal tabanına tamamlanır; örneğin Gram-Schmidt yöntemi $\mathbf{q}_1,\mathbf{e}_1,\dots,\mathbf{e}_n$ vektörlerine uygulanır ve bu sırada $\tilde{\mathbf{q}}=\mathbf{0}$ veren vektörler atlanır. Geri kalan taban vektörleri bir $\mathbf{W}\in\mathbb{R}^{n\times(n-1)}$ matrisinin sütunlarını oluşturur ve $\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1&\mathbf{W}\end{pmatrix}$ ortogonaldir. O zaman şu bulunur:

$$\mathbf{Q}_1^{\top}\mathbf{A}\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{q}_1^{\top}\mathbf{A}\mathbf{W}\\\mathbf{W}^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{W}^{\top}\mathbf{A}\mathbf{W}\end{pmatrix}=\begin{pmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{B}\end{pmatrix}$$

burada $\mathbf{B}=\mathbf{W}^{\top}\mathbf{A}\mathbf{W}$, $(n-1)\times(n-1)$ boyutlu simetrik bir matristir. Sıfırlar, $\mathbf{A}\mathbf{q}_1=\lambda_1\mathbf{q}_1$ vektörü $\mathbf{W}$ matrisinin sütunlarına dik olduğu için ortaya çıkar; sağ üstte de aynı şekilde, çünkü $\mathbf{A}$ simetriktir. $\mathbf{B}$ için aynı işlem, geriye $1\times1$ boyutlu bir matris kalana kadar tekrarlanır. $\mathbf{B}$ için böylece $\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B$ çarpımını köşegen yapan bir $\mathbf{Q}_B$ ortogonal matrisi bulunduysa $\mathbf{Q}=\mathbf{Q}_1\bigl(\begin{smallmatrix}1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B\end{smallmatrix}\bigr)$, ortogonal matrislerin çarpımı olarak ortogonaldir ve $\mathbf{Q}^{\top}\mathbf{A}\mathbf{Q}=\bigl(\begin{smallmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B\end{smallmatrix}\bigr)=\boldsymbol{\Lambda}$ köşegendir. $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$ olduğundan $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ çıkar. Toplam biçimi [Temeller 1, Kesim 9.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5)'ten çıkar, çünkü $\mathbf{Q}\boldsymbol{\Lambda}$ matrisinin sütunları $\lambda_i\mathbf{q}_i$ vektörleridir.
:::

Kesim [2.3](projektion-auf-eine-gerade.html#stufe-2-3)'e göre her $\mathbf{q}_i\mathbf{q}_i^{\top}$ terimi, $\mathbf{q}_i$ doğrultusundaki doğru üzerine izdüşümdür. Demek ki simetrik bir matris, her biri kendi özdeğeriyle ağırlıklandırılmış, birbirine dik eksenler üzerine izdüşümlerin toplamıdır. Katlı bir özdeğerde $\mathbf{q}_i$ vektörleri onun özuzayında serbestçe seçilebilir: Özuzayın her ortonormal tabanı uygundur. Her $\mathbf{q}_i$ vektörünün işareti de serbesttir. Bazı kitaplar özdeğerleri büyükten küçüğe sıralar, bazıları sıralamaz.

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ için $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$ ve $\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$, $6$ ve $1$ özdeğerlerine ait normlanmış özvektörlerdir. O zaman şu bulunur:

$$6\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}+1\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\frac15\begin{pmatrix}25&10\\10&10\end{pmatrix}=\begin{pmatrix}5&2\\2&2\end{pmatrix}.$$
::::

⁠**Kısacası:** Her simetrik matris $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ biçimindedir: uygun biçimde döndürülmüş bir eksen takımında köşegendir, birbirine dik eksenler üzerine izdüşümlerin ağırlıklı bir toplamıdır.

:::hintergrund Simetrik matrisler nereden gelir
Simetrik matrisler, bir matrisin sıraya bağlı olmayan ikili ilişkileri betimlediği her yerde ortaya çıkar. [Temeller 1, Kesim 10](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10)'daki $\mathbf{X}^{\top}\mathbf{X}$ ve $\mathbf{X}\mathbf{X}^{\top}$ Gram matrisleri iç çarpımlar içerir ve $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$. Kesim [5.2](quadratische-formen.html#stufe-5-2)'ye göre bir kuadratik formun matrisi her zaman simetrik seçilebilir. Kuplajlı bobinlerin endüktans matrisi simetriktir, çünkü bobin 1'den bobin 2'ye olan karşılıklı endüktans, ters yöndekiyle aynıdır. Spektral teorem bütün bu matrisler için gerçel özdeğerleri ve birbirine dik öz doğrultuları güvence altına alır.
:::

### Asal eksenler

<span class="anker" id="stufe-7-7"></span>

Kesim [5.3](quadratische-formen.html#stufe-5-3)'te bir kuadratik formun biçimi, matrisi köşegen olduğu sürece kolayca anlaşılıyordu. Spektral teorem, koordinatlar uygun biçimde döndürülürse her simetrik matrisi köşegen yapar. Böylece karma terimler ortadan kalkar.

:::satz Teorem 7.8 (Bir kuadratik formun asal eksenleri)
<span class="anker" id="satz-7-8"></span>

$\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ ise ve $c_i=\mathbf{q}_i^{\top}\mathbf{x}$, $\mathbf{x}$ vektörünün öz tabandaki koordinatlarıysa şu geçerlidir:

<span class="anker" id="gl-7-4"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_1c_1^2+\lambda_2c_2^2+\dots+\lambda_nc_n^2 . \tag{7.4}$$
:::

:::beweis Asal eksenler
$\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$ ile $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}\mathbf{x}=\mathbf{c}^{\top}\boldsymbol{\Lambda}\mathbf{c}=\sum_i\lambda_ic_i^2$ olur.
:::

Bu yüzden özvektörlerin doğrultularına kuadratik formun __asal eksenleri__ denir. Bütün özdeğerler pozitifse $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=1$ eş yükselti eğrisi bir elipstir, $\mathbb{R}^3$ uzayında bir elipsoit. Eksenleri $\mathbf{q}_i$ doğrultularındadır ve $\mathbf{q}_i$ doğrultusundaki yarı eksenin uzunluğu $1/\sqrt{\lambda_i}$ olur, çünkü $\mathbf{x}=t\,\mathbf{q}_i$ için $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_it^2=1$ eşitliği tam olarak $t=\pm1/\sqrt{\lambda_i}$ için sağlanır. Büyük bir özdeğer, formun hızla yükseldiği bir doğrultuya ve kısa bir yarı eksene karşılık gelir.

:::abbildung ml/k2ellipse 20
$5x_1^2+4x_1x_2+2x_2^2=1$ (mavi) ve $=\tfrac14$ (açık mavi) eş yükselti eğrileri elipslerdir. Eksenleri (gri), $6$ özdeğerine ait $\mathbf{q}_1=(2,1)^{\top}/\sqrt5$ ve $1$ özdeğerine ait $\mathbf{q}_2=(1,-2)^{\top}/\sqrt5$ özvektörlerinin doğrultularındadır. Dıştaki elipsin yarı eksenleri $1/\sqrt6\approx0{,}41$ (kırmızı) ve $1/\sqrt1=1$ (yeşil) olur: Büyük özdeğerin doğrultusunda form en hızlı yükselir ve elips orada en dardır.
:::

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$ için öz tabandaki koordinatlar $c_1=(2x_1+x_2)/\sqrt5$ ve $c_2=(x_1-2x_2)/\sqrt5$ olur ve şu geçerlidir:

$$5x_1^2+4x_1x_2+2x_2^2=6\,c_1^2+c_2^2=\tfrac65(2x_1+x_2)^2+\tfrac15(x_1-2x_2)^2 .$$

Sağ taraf açılınca $\tfrac15\bigl(24x_1^2+24x_1x_2+6x_2^2+x_1^2-4x_1x_2+4x_2^2\bigr)=5x_1^2+4x_1x_2+2x_2^2$ elde edilir. $f=1$ eş yükselti eğrisi, Şekil [20](#abb-20) içindeki, yarı eksenleri $1/\sqrt6\approx0{,}408$ ve $1$ olan elipstir.
::::

⁠**Kısacası:** Öz tabanda her kuadratik form karma terimsiz bir $\sum_i\lambda_ic_i^2$ toplamına dönüşür; özvektörler formun elipslerinin asal eksenleridir, yarı eksenler de $1/\sqrt{\lambda_i}$ olur.

:::hintergrund Tam kareye tamamlamanın iki yolu
Aynı form Kesim [5.4](quadratische-formen.html#stufe-5-4)'te $5(x_1+0{,}4x_2)^2+1{,}2x_2^2$ biçiminde de yazılabilmişti. Oradaki $5$ ve $1{,}2$ katsayıları, buradaki $6$ ve $1$ özdeğerlerinden farklı sayılardır. İki ayrışım da doğrudur, ama yeni koordinatlar farklıdır: Tam kareye tamamlamada $x_1+0{,}4x_2$ ve $x_2$ eğik koordinatlardır, spektral teoremde ise $c_1,c_2$ döndürülmüş dik bir eksen takımındaki koordinatlardır. Elipsin eksenlerini yalnızca ikinci ayrışım gösterir. İkisinin ortak yanı başkadır: Pozitif, negatif ve sıfır olan katsayıların sayısı aynıdır. Bu, bir kuadratik formun bağımsız koordinatların karelerinin toplamı olarak her yazılışı için geçerlidir; bu önermeye Sylvester eylemsizlik yasası denir. Bu yüzden tam kareye tamamlama ile özdeğerler, bir formun çanak mı, oluk mu, yoksa eyer mi olduğu konusunda her zaman aynı yargıya varır.
:::

:::aufgabe Alıştırma 21 ★ Köşegenleştirme
<span class="anker" id="aufg-21"></span>

$\mathbf{A}=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$, Alıştırma [17](eigenwerte-und-eigenvektoren.html#aufg-17)'deki matris olsun.

<ol class="al">

<li>

$\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ eşitliğini sağlayan $\mathbf{S}$ ve $\boldsymbol{\Lambda}$ matrislerini yazın ve eşitliği doğrulayın.

</li>

<li>

$\mathbf{A}^3$ matrisini bir kez doğrudan, bir kez de $\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}$ olarak hesaplayın.

</li>

</ol>

:::loesung
(a) Alıştırma [17](eigenwerte-und-eigenvektoren.html#aufg-17)'den: $(1,\,1)^{\top}$ ve $(2,\,-1)^{\top}$ özvektörleriyle $4$ ve $1$ özdeğerleri. Dolayısıyla

$$\mathbf{S}=\begin{pmatrix}1&2\\1&-1\end{pmatrix},\qquad \boldsymbol{\Lambda}=\begin{pmatrix}4&0\\0&1\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}1&2\\1&-1\end{pmatrix},$$

çünkü $\det\mathbf{S}=-3$. Sağlama: $\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}4&2\\4&-1\end{smallmatrix}\bigr)\cdot\tfrac13\bigl(\begin{smallmatrix}1&2\\1&-1\end{smallmatrix}\bigr)=\tfrac13\bigl(\begin{smallmatrix}6&6\\3&9\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$.

(b) Doğrudan: $\mathbf{A}^2=\bigl(\begin{smallmatrix}6&10\\5&11\end{smallmatrix}\bigr)$ ve $\mathbf{A}^3=\mathbf{A}^2\mathbf{A}=\bigl(\begin{smallmatrix}12+10&12+30\\10+11&10+33\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}22&42\\21&43\end{smallmatrix}\bigr)$. Öz taban üzerinden: $\boldsymbol{\Lambda}^3=\operatorname{diag}(64;\,1)$, $\mathbf{S}\boldsymbol{\Lambda}^3=\bigl(\begin{smallmatrix}64&2\\64&-1\end{smallmatrix}\bigr)$ ve

$$\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}=\frac13\begin{pmatrix}64+2&128-2\\64-1&128+1\end{pmatrix}=\begin{pmatrix}22&42\\21&43\end{pmatrix}.$$

Büyük kuvvetlerde ikinci yol çok daha kısadır: Yalnızca özdeğerlerin kuvveti alınır.
:::
:::

:::aufgabe Alıştırma 22 ★★ Bir diziyi ayrıştırmak
<span class="anker" id="aufg-22"></span>

$0,1,1,2,3,5,\dots$ Fibonacci sayıları $F_{k+2}=F_{k+1}+F_k$ bağıntısını sağlar. $\mathbf{x}_k=(F_{k+1},\,F_k)^{\top}$ ile $\mathbf{x}_{k+1}=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\mathbf{x}_k$ olur.

<ol class="al">

<li>

Matrisin özdeğerlerini ve özvektörlerini bulun.

</li>

<li>

[(7.2)](#gl-7-2) ile $F_k$ için bir formül türetin ve formülü $k=5$ için doğrulayın.

</li>

<li>

Büyük $k$ değerleri için $F_{k+1}/F_k$ nasıl davranır ve neden?

</li>

</ol>

:::loesung
(a) $p(\lambda)=\lambda^2-\lambda-1$ olur, kökleri $\varphi=\tfrac{1+\sqrt5}2\approx1{,}618$ ve $\psi=\tfrac{1-\sqrt5}2\approx-0{,}618$. $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ sisteminin birinci satırı $(1-\lambda)v_1+v_2=0$ olur; ikinci satır olan $v_1-\lambda v_2=0$, $p(\lambda)=0$ olduğundan buna denktir. Özvektörler $\mathbf s_1=(\varphi,\,1)^{\top}$ ve $\mathbf s_2=(\psi,\,1)^{\top}$ olur.

(b) $\mathbf{x}_0=(F_1,\,F_0)^{\top}=(1,\,0)^{\top}=c_1\mathbf s_1+c_2\mathbf s_2$ eşitliği $c_1+c_2=0$ ve $c_1\varphi+c_2\psi=1$ koşullarını verir, dolayısıyla $c_1=1/(\varphi-\psi)=1/\sqrt5$ ve $c_2=-1/\sqrt5$. [(7.2)](#gl-7-2) uyarınca $\mathbf{x}_k=\tfrac1{\sqrt5}(\varphi^k\mathbf s_1-\psi^k\mathbf s_2)$ olur; ikinci bileşen şudur:

$$F_k=\frac{\varphi^k-\psi^k}{\sqrt5} .$$

$k=5$ için: $\varphi^5=\tfrac{11+5\sqrt5}2$ ve $\psi^5=\tfrac{11-5\sqrt5}2$, dolayısıyla $F_5=\tfrac{5\sqrt5}{\sqrt5}=5$. Sayısal olarak: $\varphi^5\approx11{,}090$, $\psi^5\approx-0{,}090$, $(11{,}090+0{,}090)/2{,}236\approx5{,}000$.

(c) $|\psi|<1$ olduğundan $\psi^k$ sıfıra gider ve $F_{k+1}/F_k$ oranı, altın oran olan $\varphi\approx1{,}618$ değerine gider. Kesim [7.3](#stufe-7-3)'te olduğu gibi mutlak değerce en büyük özdeğere ait pay baskın çıkar; sonraki her adım bu payı $\varphi$ ile çarpar.
:::
:::

:::aufgabe Alıştırma 23 ★★ Spektral ayrışım
<span class="anker" id="aufg-23"></span>

<ol class="al">

<li>

$\mathbf{A}=\bigl(\begin{smallmatrix}3&4\\4&-3\end{smallmatrix}\bigr)$ matrisini $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ biçiminde ve $\lambda_1\mathbf{q}_1\mathbf{q}_1^{\top}+\lambda_2\mathbf{q}_2\mathbf{q}_2^{\top}$ toplamı olarak yazın.

</li>

<li>

$3x_1^2+8x_1x_2-3x_2^2$ formunun asal eksenlerini bulun ve formu $\lambda_1c_1^2+\lambda_2c_2^2$ biçiminde yazın. Kesim [5.3](quadratische-formen.html#stufe-5-3)'teki temel biçimlerden hangisi söz konusudur?

</li>

<li>

$\Bigl(\begin{smallmatrix}2&0&0\\0&3&1\\0&1&3\end{smallmatrix}\Bigr)$ matrisinin $2$ özdeğeri çift katlıdır. Özvektörlerden oluşan bir ortonormal taban verin. Bu taban tek midir?

</li>

</ol>

:::loesung
(a) İz $0$, determinant $-9-16=-25$, dolayısıyla $\lambda^2-25=0$ ve $\lambda=\pm5$. $5$ için: $\bigl(\begin{smallmatrix}-2&4\\4&-8\end{smallmatrix}\bigr)$, $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$. $-5$ için: $\bigl(\begin{smallmatrix}8&4\\4&2\end{smallmatrix}\bigr)$, $\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$. $\mathbf{Q}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\bigr)$ ve $\boldsymbol{\Lambda}=\operatorname{diag}(5;\,-5)$ ile $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ olur ve

$$5\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}-5\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\begin{pmatrix}3&4\\4&-3\end{pmatrix}.$$

(b) Formun matrisi tam olarak bu matristir. $c_1=(2x_1+x_2)/\sqrt5$ ve $c_2=(x_1-2x_2)/\sqrt5$ ile şu bulunur:

$$3x_1^2+8x_1x_2-3x_2^2=5c_1^2-5c_2^2=(2x_1+x_2)^2-(x_1-2x_2)^2 ,$$

çarpımlar açılınca $4x_1^2+4x_1x_2+x_2^2-x_1^2+4x_1x_2-4x_2^2$ elde edilir. Asal eksenler $(2,\,1)^{\top}$ ve $(1,\,-2)^{\top}$ doğrultularındadır. Bir özdeğer pozitif, biri negatif: eksenleri koordinat eksenlerine göre döndürülmüş bir eyer.

(c) $\mathbf{e}_1$, $2$ özdeğerine ait bir özvektördür. Alttaki $\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ bloğunun özdeğerleri $(1,\,1)^{\top}$ ile $4$ ve $(1,\,-1)^{\top}$ ile $2$ olur. Dolayısıyla özvektörlerden oluşan bir ortonormal taban şudur:

$$\mathbf{e}_1,\qquad \tfrac1{\sqrt2}(0,\,1,\,-1)^{\top}\quad\text{özdeğer }2,\qquad \tfrac1{\sqrt2}(0,\,1,\,1)^{\top}\quad\text{özdeğer }4 .$$

Bu taban tek değildir. $2$ özdeğerine ait özuzay, $\mathbf{e}_1$ ve $(0,\,1,\,-1)^{\top}$ vektörlerinin gerdiği düzlemdir ve bu düzlemin her ortonormal tabanı uygundur, örneğin $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1+\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$ ve $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1-\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$. Yalnızca tek katlı $4$ özdeğerine ait özvektör, işareti dışında, tek olarak belirlidir.
:::
:::
