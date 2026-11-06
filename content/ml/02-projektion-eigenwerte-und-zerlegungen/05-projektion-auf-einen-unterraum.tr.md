---
title: Bir alt uzay üzerine izdüşüm
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / İzdüşüm, Özdeğerler ve Ayrışımlar
order: 6220500
summary: Önceki kesim bir sütun uzayının en yakın noktasını buldu.
tags: alt uzayı, izdüşüm matrisi, ortogonal tümleyeni, Gram-Schmidt yöntemi, QR ayrışımı
lang: tr
---

<span class="anker" id="stufe-4"></span>

:::zweck
Önceki kesim bir sütun uzayının en yakın noktasını buldu. Bu kesim sonucu bir matris olarak ifade ediyor, sütunlar ortonormal olduğunda her şeyin özellikle basitleştiğini gösteriyor ve herhangi bağımsız sütunlardan ortonormal sütunlar elde eden bir yöntem tanıtıyor. Böylece en iyi yaklaşık çözüm, $\mathbf{A}^{\top}\mathbf{A}$ matrisi oluşturulmadan hesaplanabilir.
:::

### Alt uzaylar

<span class="anker" id="stufe-4-1"></span>

Orijinden geçen doğruların ve düzlemlerin, sütun uzaylarının ve çekirdeklerin ortak bir özelliği vardır: İki vektörü içeriyorlarsa bu ikisinin her doğrusal bileşimini de içerirler. Toplama ve katla çarpma ile bunların dışına hiç çıkılmaz. Böyle kümeler için ayrı bir sözcük vardır.

:::definition Tanım 4.1 (Alt uzay)
<span class="anker" id="satz-4-1"></span>

Bir $\mathcal U\subseteq\mathbb{R}^n$ kümesi sonlu sayıda vektörün gerdiği küme (span) ise, ona $\mathbb{R}^n$ uzayının bir __alt uzayı__ denir.
:::

Denk olarak: $\mathcal U$ sıfır vektörünü içerir ve içerdiği her $\mathbf{u},\mathbf{v}$ vektör çifti için $\mathcal U$ kümesi $\mathbf{u}+\mathbf{v}$ toplamını ve her $c\,\mathbf{u}$ katını da içerir. Her alt uzayın bir tabanı ve dolayısıyla Kısım 1, Kesim 13.3'e göre bir boyutu vardır.

⁠**Sayısal örnek:** $\mathbb{R}^3$ uzayında şunlar alt uzaydır: boyutu $0$ olan, tek başına orijin; boyutu $1$ olan, orijinden geçen her doğru; boyutu $2$ olan, orijinden geçen her düzlem, örneğin önceki kesimdeki $\mathbf{H}$ matrisinin sütun uzayı; ve $\mathbb{R}^3$ uzayının tamamı. Bir matrisin çekirdeği bir alt uzaydır, sütun uzayı da öyle. Orijinden geçmeyen bir doğru alt uzay değildir, çünkü sıfır vektörünü içermez.

⁠**Kısacası:** Alt uzay, birtakım vektörlerin gerdiği kümedir; toplama ve katla çarpma ile onun dışına çıkılmaz.

### Bir sütun uzayının izdüşüm matrisi

<span class="anker" id="stufe-4-2"></span>

Sütunlar doğrusal bağımsızsa [(3.5)](die-beste-naherungslosung.html#gl-3-5) en yakın noktayı verir: $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$. $\mathbf{y}$ vektörünün önündeki matris yalnızca $\mathbf{A}$ matrisine bağlıdır. Bu matris sütun uzayı için, $\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ matrisinin bir doğru için yaptığını yapar.

:::definition Tanım 4.2 (Bir sütun uzayının izdüşüm matrisi)
<span class="anker" id="satz-4-2"></span>

$\mathbf{A}$ matrisinin sütunları doğrusal bağımsızsa

<span class="anker" id="gl-4-1"></span>
$$\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{4.1}$$

matrisine $\mathbf{A}$ matrisinin sütun uzayı üzerine __izdüşüm matrisi__ denir.
:::

:::satz Teorem 4.3 (Özellikler)
<span class="anker" id="satz-4-3"></span>

$\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$, $\mathbf{P}^{\top}=\mathbf{P}$, $\mathbf{P}^2=\mathbf{P}$ ve $\mathbf{P}\mathbf{A}=\mathbf{A}$ geçerlidir. Dolayısıyla $\mathbf{P}$, sütun uzayı üzerine dik izdüşümdür.
:::

:::beweis Özellikler
Birinci denklem yukarıdaki türetmedir. Kısım 1, Kesim 10.1 ve 11.4'teki hesap kurallarıyla $\mathbf{P}^{\top}=\mathbf{A}\bigl((\mathbf{A}^{\top}\mathbf{A})^{-1}\bigr)^{\top}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$ olur, çünkü $\mathbf{A}^{\top}\mathbf{A}$ simetriktir, dolayısıyla tersi de simetriktir. Ayrıca $\mathbf{P}\mathbf{A}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}(\mathbf{A}^{\top}\mathbf{A})=\mathbf{A}$ ve buradan $\mathbf{P}^2=\mathbf{P}\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$. Kesim [2.4](projektion-auf-eine-gerade.html#stufe-2-4)'teki teoreme göre simetrik bir izdüşüm diktir.
:::

$\mathbf{P}\mathbf{A}=\mathbf{A}$ denklemi şunu söyler: Her sütun, dolayısıyla sütun uzayının her vektörü, izdüşümde yerinde kalır.

⁠**Sayısal örnek:** $\mathbf{H}$ için şu bulunur:

$$\mathbf{P}=\mathbf{H}\cdot\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\mathbf{H}^{\top}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix}.$$

Sağlama: $\mathbf{P}(1,\,1,\,1)^{\top}=\tfrac13(2,\,2,\,4)^{\top}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}=\hat{\mathbf{y}}$ ve $\mathbf{P}\mathbf{a}_1=\tfrac13(2+1,\ -1+1,\ 1+2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_1$.

⁠**Kısacası:** $\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ izdüşüm matrisi her vektörü sütun uzayının en yakın noktasına götürür; simetriktir ve $\mathbf{P}^2=\mathbf{P}$ koşulunu sağlar.

### Ortonormal sütunlar

<span class="anker" id="stufe-4-3"></span>

[(4.1)](#gl-4-1) formülü bir ters matris içerir. Sütunlar ortonormal olduğunda bu ters matris ortadan kalkar, çünkü o zaman $\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$ olur. Bu yüzden ortonormal sütunlu bir $\mathbf{Q}$ matrisi için en iyi yaklaşık çözüm basitçe $\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ olur: Bileşenleri $\mathbf{q}_i^{\top}\mathbf{y}$ gölge uzunluklarıdır.

:::satz Teorem 4.4 (Ortonormal sütunlarda izdüşüm)
<span class="anker" id="satz-4-4"></span>

$\mathbf{Q}\in\mathbb{R}^{n\times k}$ matrisinin $\mathbf{q}_1,\dots,\mathbf{q}_k$ sütunları ortonormalse, sütun uzayı üzerine izdüşüm matrisi şudur:

<span class="anker" id="gl-4-2"></span>
$$\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}=\sum_{i=1}^k\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{4.2}$$
:::

Toplam biçimi Kısım 1, Kesim 9.5'ten çıkar: Bir matris çarpımı, sütunların ve satırların dış çarpımlarının toplamıdır. Her $\mathbf{q}_i\mathbf{q}_i^{\top}$ terimi, $\mathbf{q}_i$ doğrultusundaki doğru üzerine izdüşüm matrisidir. Demek ki ortonormal sütunlarda sütun uzayı üzerine izdüşüm, tek tek eksenler üzerine izdüşümlerin toplamıdır. Bu, Kesim [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1)'in son alt kesimini sonradan açıklar: $\mathbf{Q}\mathbf{Q}^{\top}$ birim matris değil, $\mathbf{Q}$ matrisinin sütun uzayı üzerine izdüşümdür. Bu uzaya dik olanı atar.

⁠**Sayısal örnek:** $\mathbf{q}_1=\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}$ ve $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$ vektörleri ortonormaldir: $\lVert\mathbf{q}_1\rVert^2=\tfrac22$, $\lVert\mathbf{q}_2\rVert^2=\tfrac66$, $\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac{-1+0+1}{\sqrt{12}}=0$. İkisinde de üçüncü bileşen ilk ikisinin toplamıdır; $\mathbf{H}$ düzleminin bir ortonormal tabanını oluştururlar. İzdüşüm matrisi şöyle bulunur:

$$\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}=\frac12\begin{pmatrix}1&0&1\\0&0&0\\1&0&1\end{pmatrix}+\frac16\begin{pmatrix}1&-2&-1\\-2&4&2\\-1&2&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix},$$

yani önceki alt kesimdeki matrisin aynısı, bu kez ters matris olmadan.

⁠**Kısacası:** Ortonormal sütunlarda $\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ ve $\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}$ olur; bu izdüşüm matrisi, tek tek sütunlar üzerine izdüşümlerin toplamıdır.

### Ortogonal tümleyen

<span class="anker" id="stufe-4-4"></span>

$\mathbf{y}$ bir alt uzay üzerine izdüşürülürse geriye $\mathbf{y}-\mathbf{P}\mathbf{y}$ artığı kalır. Bu artık vektörü alt uzayın tamamına diktir. Bu özelliğe sahip bütün vektörler kendileri de bir alt uzay oluşturur ve $\mathbf{y}$, biri birinci alt uzayda, öbürü ikincide olan iki parçaya ayrılır.

:::definition Tanım 4.5 (Ortogonal tümleyen)
<span class="anker" id="satz-4-5"></span>

Bir $\mathcal U\subseteq\mathbb{R}^n$ alt uzayının __ortogonal tümleyeni__ şu kümedir:

<span class="anker" id="gl-4-3"></span>
$$\mathcal U^\perp=\{\mathbf{z}\in\mathbb{R}^n:\ \mathbf{z}^{\top}\mathbf{u}=0\ \text{her}\ \mathbf{u}\in\mathcal U\ \text{için}\} . \tag{4.3}$$
:::

$\mathcal U^\perp$ ifadesi “$\mathcal U$ dik” diye okunur. $\mathcal U$, $\mathbf{A}$ matrisinin sütun uzayıysa $\mathbf{z}$ ancak ve ancak $\mathbf{A}^{\top}\mathbf{z}=\mathbf{0}$ ise $\mathcal U$ alt uzayına diktir; yani ortogonal tümleyen $\mathbf{A}^{\top}$ matrisinin çekirdeğidir.

:::satz Teorem 4.6 (İki dik parçaya ayrışım)
<span class="anker" id="satz-4-6"></span>

$\mathbf{P}$, $\mathbb{R}^n$ uzayının bir $\mathcal U$ alt uzayı üzerine dik izdüşümse şunlar geçerlidir:

<ol class="rm">

<li>

Her $\mathbf{y}$ vektörü, $\mathbf{u}\in\mathcal U$ ve $\mathbf{z}\in\mathcal U^\perp$ olmak üzere tek bir biçimde $\mathbf{y}=\mathbf{u}+\mathbf{z}$ toplamı olarak yazılır; bu parçalar $\mathbf{u}=\mathbf{P}\mathbf{y}$ ve $\mathbf{z}=(\mathbf{I}-\mathbf{P})\mathbf{y}$ vektörleridir.

</li>

<li>

$\mathbf{I}-\mathbf{P}$, $\mathcal U^\perp$ üzerine dik izdüşümdür.

</li>

<li>

$\dim\mathcal U^\perp=n-\dim\mathcal U$.

</li>

</ol>
:::

:::beweis Ayrışım
(i) $\mathbf{P}\mathbf{y}$ vektörünün $\mathcal U$ içinde olması ve $\mathbf{y}-\mathbf{P}\mathbf{y}$ vektörünün $\mathcal U$ alt uzayına dik olması, dik izdüşümün tanımıdır. İkinci bir $\mathbf{y}=\mathbf{u}'+\mathbf{z}'$ ayrışımı olsaydı $\mathbf{u}-\mathbf{u}'=\mathbf{z}'-\mathbf{z}$ hem $\mathcal U$ içinde bulunan hem de $\mathcal U$ alt uzayına dik olan, yani kendine dik olan bir vektör olurdu. O zaman uzunluğunun karesi sıfırdır, yani bu vektör sıfır vektörüdür. (ii) $\mathbf{I}-\mathbf{P}$ simetriktir ve $(\mathbf{I}-\mathbf{P})^2=\mathbf{I}-2\mathbf{P}+\mathbf{P}^2=\mathbf{I}-\mathbf{P}$. (i) şıkkına göre görüntüsü $\mathcal U^\perp$ içindedir. Her $\mathbf{z}\in\mathcal U^\perp$ yerinde kalır: $\mathbf{P}\mathbf{z}$, $\mathcal U$ içindedir ve aynı zamanda $\mathcal U$ alt uzayına dik iki vektörün $\mathbf{z}-(\mathbf{z}-\mathbf{P}\mathbf{z})$ farkıdır; dolayısıyla $\mathbf{P}\mathbf{z}$ kendine diktir ve $\mathbf{0}$ vektörüdür. (iii) $\mathcal U$ için bir taban seçilip bir $\mathbf{A}$ matrisinin sütunları olarak yazılırsa $\mathcal U^\perp$, $\mathbf{A}^{\top}$ matrisinin çekirdeği olur. Kısım 1, Kesim 13.5'teki rank-sıfırlık teoremine göre bu çekirdeğin boyutu $n-\operatorname{rank}\mathbf{A}^{\top}=n-\operatorname{rank}\mathbf{A}=n-\dim\mathcal U$ olur.
:::

⁠**Sayısal örnek:** $\mathbf{H}$ düzleminin boyutu $2$, dolayısıyla $\mathbb{R}^3$ uzayındaki ortogonal tümleyeninin boyutu $1$: $\mathbf{k}=(1,\,1,\,-1)^{\top}$ normal vektörü doğrultusundaki doğru. Gerçekten de $\mathbf{H}^{\top}\mathbf{k}=(1-1,\ 1-1)^{\top}=\mathbf{0}$. Ayrıca

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&1&-1\\1&1&-1\\-1&-1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}},$$

bu da söz konusu doğru üzerine izdüşümdür. $\mathbf{y}=(1,\,1,\,1)^{\top}$ için $(\mathbf{I}-\mathbf{P})\mathbf{y}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$ olur, yani önceki kesimdeki artık.

⁠**Kısacası:** $\mathcal U^\perp$ ortogonal tümleyeni, $\mathcal U$ alt uzayına dik bütün vektörleri içerir; her vektör tek bir biçimde $\mathcal U$ içindeki ve $\mathcal U^\perp$ içindeki birer parçaya ayrılır ve boyutların toplamı $n$ olur.

### Gram-Schmidt yöntemi

<span class="anker" id="stufe-4-5"></span>

Ortonormal sütunlar her şeyi basitleştirir, ama elde çoğunlukla herhangi sütunlar vardır. Gram-Schmidt yöntemi, doğrusal bağımsız $\mathbf{a}_1,\dots,\mathbf{a}_k$ vektörlerinden aynı alt uzayı geren ortonormal $\mathbf{q}_1,\dots,\mathbf{q}_k$ vektörleri kurar.

Fikri iki vektör için Şekil [11](#abb-11) gösteriyor. Birinci vektör normlanır. İkinciden, birinci üzerine düşen gölgesi, yani izdüşümü çıkarılır. Geriye kalan birinciye diktir ve normlanır. Üçüncü vektörden, bulunmuş olan iki vektör üzerine düşen gölgeleri çıkarılır ve böyle devam edilir.

:::abbildung ml/k2gramschmidt 11
$\mathbf{a}_1=(2,1)^{\top}$ ve $\mathbf{a}_2=(1,2)^{\top}$ için Gram-Schmidt yöntemi. Önce $\mathbf{a}_1$ normlanır: $\mathbf{q}_1=\mathbf{a}_1/\sqrt5$. İkinci vektörden $(\mathbf{q}_1^{\top}\mathbf{a}_2)\,\mathbf{q}_1=(1{,}6;\,0{,}8)^{\top}$ gölgesi (mavi) çıkarılır. Kalan $\tilde{\mathbf{q}}_2=(-0{,}6;\,1{,}2)^{\top}$ (turuncu, kesikli dikme çizgisine paralel) $\mathbf{q}_1$ vektörüne diktir; normlanınca $\mathbf{q}_2=(-1,2)^{\top}/\sqrt5$ olur.
:::

:::definition Tanım 4.7 (Gram-Schmidt yöntemi)
<span class="anker" id="satz-4-7"></span>

Doğrusal bağımsız $\mathbf{a}_1,\dots,\mathbf{a}_k\in\mathbb{R}^n$ vektörleri veriliyor. __Gram-Schmidt yöntemi__ $i=1,\dots,k$ için sırayla şunları hesaplar:

<span class="anker" id="gl-4-4"></span>
$$\tilde{\mathbf{q}}_i=\mathbf{a}_i-\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l,\qquad \mathbf{q}_i=\frac{\tilde{\mathbf{q}}_i}{\lVert\tilde{\mathbf{q}}_i\rVert} . \tag{4.4}$$
:::

$i=1$ için toplam boştur, yani $\tilde{\mathbf{q}}_1=\mathbf{a}_1$. Toplam, [(4.2)](#gl-4-2) uyarınca $\mathbf{a}_i$ vektörünün şimdiye kadar bulunan vektörlerin gerdiği alt uzay üzerine izdüşümüdür; $\tilde{\mathbf{q}}_i$ bu izdüşümün artığıdır.

:::satz Teorem 4.8 (Gram-Schmidt yönteminin verdiği sonuç)
<span class="anker" id="satz-4-8"></span>

$\mathbf{q}_1,\dots,\mathbf{q}_k$ vektörleri ortonormaldir ve her $i$ için $\mathbf{q}_1,\dots,\mathbf{q}_i$ vektörleri, $\mathbf{a}_1,\dots,\mathbf{a}_i$ vektörleriyle aynı alt uzayı gerer.
:::

:::beweis Gram-Schmidt
Adım adım ilerlenir. $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ vektörlerinin zaten ortonormal olduğunu ve $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$ vektörleriyle aynı alt uzayı gerdiğini varsayalım. O zaman $\tilde{\mathbf{q}}_i$, $\mathbf{a}_i$ vektörünün bu alt uzay üzerine izdüşümünün artığıdır ve bu yüzden $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ vektörlerine diktir; doğrudan hesaplanırsa $\mathbf{q}_l^{\top}\tilde{\mathbf{q}}_i=\mathbf{q}_l^{\top}\mathbf{a}_i-\mathbf{q}_l^{\top}\mathbf{a}_i=0$ olur. $\tilde{\mathbf{q}}_i\ne\mathbf{0}$ olur, çünkü aksi halde $\mathbf{a}_i$, $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ vektörlerinin ve dolayısıyla $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$ vektörlerinin bir doğrusal bileşimi olurdu; bu da bağımsızlıkla çelişir. Demek ki normlama yapılabilir. Son olarak $\mathbf{a}_i=\tilde{\mathbf{q}}_i+\sum_l(\mathbf{q}_l^{\top}\mathbf{a}_i)\mathbf{q}_l$, $\mathbf{q}_1,\dots,\mathbf{q}_i$ vektörlerinin bir doğrusal bileşimidir; tersine $\mathbf{q}_i$ de $\mathbf{a}_i$ ile $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ vektörlerinin bir doğrusal bileşimidir. Demek ki iki liste aynı alt uzayı gerer.
:::

Verilen vektörler yine de bağımlıysa yöntem bunu kendisi fark eder: Bir noktada $\tilde{\mathbf{q}}_i=\mathbf{0}$ olur ve normlama yapılamaz.

⁠**Sayısal örnek:** $\mathbf{H}$ matrisinin $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ ve $\mathbf{a}_2=(0,\,1,\,1)^{\top}$ sütunları için $\mathbf{q}_1=\mathbf{a}_1/\sqrt2$ olur. O zaman $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$ olur ve şu bulunur:

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\frac1{\sqrt2}\,\mathbf{q}_1=(0,\,1,\,1)^{\top}-\tfrac12(1,\,0,\,1)^{\top}=\bigl(-\tfrac12,\,1,\,\tfrac12\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{\tfrac14+1+\tfrac14}=\sqrt{\tfrac32} .$$

Normlanınca $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$ olur; bu tam olarak [(4.2)](#gl-4-2) bağıntısına ait sayısal örnekteki ortonormal tabandır. Bu sayısal örnekteki iki toplamı Şekil [12](#abb-12) gösteriyor.

:::abbildung ml/k2rgs 12
$\mathbf{H}$ matrisinin sütunları için Gram-Schmidt: $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$ ile $\mathbf{a}_2=(0,1,1)^{\top}$ vektörlerinin, gölgenin uzunluğunu veren $\mathbf{q}_1^{\top}\mathbf{a}_2$ iç çarpımı ve $\tilde{\mathbf{q}}_2=(-\tfrac12,1,\tfrac12)^{\top}$ kalanının uzunluğunun karesi.
:::

⁠**Kısacası:** Gram-Schmidt her vektörden, şimdiye kadar bulunanlar üzerine izdüşümünü çıkarır ve kalanı normlar; böylece aynı alt uzayın bir ortonormal tabanı oluşur.

:::hintergrund İşlem yükü ve yuvarlama hataları
Her biri $n$ bileşenli $k$ vektör için yöntem yaklaşık $2nk^2$ temel aritmetik işlem gerektirir: $i$ numaralı adımda $i-1$ iç çarpım hesaplanır ve aynı sayıda kat çıkarılır; bunların her biri yaklaşık $2n$ işleme mal olur ve $i$ üzerinden toplam $k^2$ gibi büyür. Yuvarlanmış sayılarla [(4.4)](#gl-4-4) biçimi hassastır: Verilen vektörlerden ikisi neredeyse paralelse $\tilde{\mathbf{q}}_i$ büyük sayıların küçük bir farkıdır ve hesaplanan $\mathbf{q}_i$ vektörleri o zaman tam olarak ortogonal olmaz. Hesap adımlarının biraz değiştirilmiş bir sırası, yani değiştirilmiş Gram-Schmidt yöntemi, gölgelerin hepsini ilk $\mathbf{a}_i$ vektöründen çıkarmak yerine onları tek tek, zaten küçülmüş kalandan çıkarır. Kesin sayılarla aynı sonucu verir, yuvarlanmış sayılarla belirgin biçimde daha doğrudur. Yazılım kütüphaneleri çoğunlukla yansımalarla, yani ortogonal matrislerle çalışan başka yöntemler kullanır.
:::

### QR ayrışımı

<span class="anker" id="stufe-4-6"></span>

Gram-Schmidt yöntemi bir matris ayrışımı olarak yazılabilir. Yukarıdaki ispata göre her $\mathbf{a}_i$ vektörü $\mathbf{q}_1,\dots,\mathbf{q}_i$ vektörlerinin bir doğrusal bileşimidir, şöyle ki:

$$\mathbf{a}_i=\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l+\lVert\tilde{\mathbf{q}}_i\rVert\,\mathbf{q}_i .$$

Bu bileşimde $\mathbf{q}_l$ vektörlerinin yalnızca ilk $i$ tanesi yer alır, sonrakiler yer almaz. Bu yüzden katsayılar bir matrisin sütunları olarak yazılınca bir üçgen matris ortaya çıkar.

:::definition Tanım 4.9 (QR ayrışımı)
<span class="anker" id="satz-4-9"></span>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisinin sütunları doğrusal bağımsızsa __QR ayrışımı__ şu gösterimdir:

<span class="anker" id="gl-4-5"></span>
$$\mathbf{A}=\mathbf{Q}\mathbf{R} \tag{4.5}$$

burada $\mathbf{Q}\in\mathbb{R}^{m\times n}$ ortonormal sütunlu bir matris, $\mathbf{R}\in\mathbb{R}^{n\times n}$ ise köşegen elemanları pozitif olan bir üst üçgen matristir. Bu sırada $l<i$ için $r_{li}=\mathbf{q}_l^{\top}\mathbf{a}_i$ ve $r_{ii}=\lVert\tilde{\mathbf{q}}_i\rVert$ olur.
:::

Bir üst üçgen matrisin köşegeninin altında yalnızca sıfırlar vardır. Sütun bakışına göre $\mathbf{Q}\mathbf{R}$ matrisinin $i$ numaralı sütunu $\sum_lr_{li}\mathbf{q}_l$, yani tam olarak yukarıdaki $\mathbf{a}_i$ gösterimidir. $\mathbf{Q}$ matrisinin sütunlarını Gram-Schmidt yöntemi verir, $\mathbf{R}$ matrisinin elemanları da bu sırada yan ürün olarak çıkar. $\mathbf{Q}$ ortonormal sütunlu olduğundan ayrıca $\mathbf{R}=\mathbf{Q}^{\top}\mathbf{A}$ olur.

⁠**Sayısal örnek:** $\mathbf{H}$ için şu bulunur:

$$\mathbf{Q}=\begin{pmatrix}\tfrac1{\sqrt2}&-\tfrac1{\sqrt6}\\0&\tfrac2{\sqrt6}\\\tfrac1{\sqrt2}&\tfrac1{\sqrt6}\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&\tfrac1{\sqrt2}\\0&\sqrt{\tfrac32}\end{pmatrix}\approx\begin{pmatrix}1{,}414&0{,}707\\0&1{,}225\end{pmatrix}.$$

İkinci sütunun sağlaması: $\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}+\sqrt{\tfrac32}\cdot\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}=\tfrac12(1,\,0,\,1)^{\top}+\tfrac12(-1,\,2,\,1)^{\top}=(0,\,1,\,1)^{\top}=\mathbf{a}_2$.

⁠**Kısacası:** $\mathbf{A}=\mathbf{Q}\mathbf{R}$ QR ayrışımı, Gram-Schmidt yöntemini bir matris çarpımı olarak yazar: $\mathbf{Q}$ ortonormal sütunludur, $\mathbf{R}$ bir üst üçgen matristir.

### QR ile en iyi yaklaşık çözüm

<span class="anker" id="stufe-4-7"></span>

QR ayrışımıyla normal denklemler, $\mathbf{A}^{\top}\mathbf{A}$ hesaplanmadan çözülebilir. $\mathbf{A}=\mathbf{Q}\mathbf{R}$ yerine konur ve $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ kullanılır.

:::satz Teorem 4.10 (QR ile en iyi yaklaşık çözüm)
<span class="anker" id="satz-4-10"></span>

$\mathbf{A}=\mathbf{Q}\mathbf{R}$ QR ayrışımıysa $\mathbf{A}\mathbf{x}=\mathbf{y}$ sisteminin en iyi yaklaşık çözümü şu sistemin çözümüdür:

<span class="anker" id="gl-4-6"></span>
$$\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y} . \tag{4.6}$$
:::

:::beweis QR ile çözüm
$\mathbf{A}^{\top}\mathbf{A}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{R}^{\top}\mathbf{R}$ ve $\mathbf{A}^{\top}\mathbf{y}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$ olur. Normal denklemler yani $\mathbf{R}^{\top}\mathbf{R}\hat{\mathbf{x}}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$ biçimini alır. $\mathbf{R}$ üçgen matrisinin köşegen elemanları pozitiftir; dolayısıyla Kısım 1, Kesim 14.4'e göre determinantı sıfırdan farklıdır, yani tersinirdir; $\mathbf{R}^{\top}$ de öyle. Soldan $(\mathbf{R}^{\top})^{-1}$ ile çarpılınca geriye [(4.6)](#gl-4-6) kalır.
:::

[(4.6)](#gl-4-6) sistemi üçgen biçimlidir ve Kısım 1, Kesim 12.3'teki Gauss eleme yönteminin sonunda yapılan geriye doğru yerine koymada olduğu gibi aşağıdan yukarıya doğru çözülür. $m\times n$ boyutlu bir matris için yolun tamamı yaklaşık $2mn^2$ temel aritmetik işleme mal olur; bunun neredeyse tamamı QR ayrışımına gider.

⁠**Sayısal örnek:** $\mathbf{H}$ ve $\mathbf{y}=(1,\,1,\,1)^{\top}$ için $\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac2{\sqrt2},\ \tfrac{-1+2+1}{\sqrt6}\bigr)^{\top}=\bigl(\sqrt2,\ \tfrac2{\sqrt6}\bigr)^{\top}$ olur. [(4.6)](#gl-4-6) sisteminin alt satırı $\sqrt{\tfrac32}\,\hat x_2=\tfrac2{\sqrt6}$, dolayısıyla $\hat x_2=\tfrac2{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac23$. Üst satırı $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac23=\sqrt2$, dolayısıyla $\hat x_1=1-\tfrac13=\tfrac23$. Bu, normal denklemlerle bulunan çözümün aynısıdır. $\mathbf{Q}^{\top}\mathbf{y}$ vektörünün bileşenleri iç çarpımlardır (Şekil [13](#abb-13)).

:::abbildung ml/k2rqr 13
$\mathbf{y}=(1,1,1)^{\top}$ için üçgen sistemin $\mathbf{Q}^{\top}\mathbf{y}$ sağ tarafı; $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$ ve $\mathbf{q}_2=(-1,2,1)^{\top}/\sqrt6$ ile.
:::

⁠**Kısacası:** $\mathbf{A}=\mathbf{Q}\mathbf{R}$ ile normal denklemlerden $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ üçgen sistemi elde edilir; $\mathbf{A}^{\top}\mathbf{A}$ matrisi bu sırada hiç oluşturulmaz.

:::aufgabe Alıştırma 11 ★ Gram-Schmidt ve izdüşüm
<span class="anker" id="aufg-11"></span>

$\mathbf{a}_1=(1,\,1,\,0)^{\top}$ ve $\mathbf{a}_2=(1,\,0,\,1)^{\top}$ veriliyor.

<ol class="al">

<li>

Gram-Schmidt yöntemini uygulayın ve $\mathbf{q}_1,\mathbf{q}_2$ vektörlerinin ortonormal olduğunu doğrulayın.

</li>

<li>

$\mathbf{a}_1$ ve $\mathbf{a}_2$ vektörlerinin gerdiği düzlem üzerine $\mathbf{P}=\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}$ izdüşüm matrisini hesaplayın ve $\mathbf{y}=(1,\,2,\,3)^{\top}$ vektörünün izdüşümünü bulun.

</li>

<li>

Düzlemin ortogonal tümleyenini geren bir vektör bulun ve $\mathbf{I}-\mathbf{P}=\mathbf{k}\mathbf{k}^{\top}/(\mathbf{k}^{\top}\mathbf{k})$ eşitliğini doğrulayın.

</li>

</ol>

:::loesung
(a) $\mathbf{q}_1=\mathbf{a}_1/\sqrt2=(1,\,1,\,0)^{\top}/\sqrt2$ olur. Sonra $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$ ve

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\tfrac1{\sqrt2}\,\mathbf{q}_1=(1,\,0,\,1)^{\top}-\tfrac12(1,\,1,\,0)^{\top}=\bigl(\tfrac12,\,-\tfrac12,\,1\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert^2=\tfrac14+\tfrac14+1=\tfrac32 ,$$

dolayısıyla $\mathbf{q}_2=\tilde{\mathbf{q}}_2/\sqrt{3/2}=(1,\,-1,\,2)^{\top}/\sqrt6$ olur. Sağlama: $\mathbf{q}_1^{\top}\mathbf{q}_2=(1-1+0)/\sqrt{12}=0$, $\lVert\mathbf{q}_2\rVert^2=\tfrac{1+1+4}6=1$.

(b)

$$\mathbf{P}=\frac12\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix}+\frac16\begin{pmatrix}1&-1&2\\-1&1&-2\\2&-2&4\end{pmatrix}=\frac13\begin{pmatrix}2&1&1\\1&2&-1\\1&-1&2\end{pmatrix},$$

$$\mathbf{P}\mathbf{y}=\frac13\begin{pmatrix}2+2+3\\1+4-3\\1-2+6\end{pmatrix}=\begin{pmatrix}7/3\\2/3\\5/3\end{pmatrix}.$$

(c) $\mathbf{a}_1^{\top}\mathbf{k}=k_1+k_2=0$ ve $\mathbf{a}_2^{\top}\mathbf{k}=k_1+k_3=0$ koşullarını sağlayan bir $\mathbf{k}$ aranıyor; bu da $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ ya da onun bir katıdır. $\mathbf{k}^{\top}\mathbf{k}=3$ olur ve

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&-1&-1\\-1&1&1\\-1&1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}} .$$

Düzlemin ortogonal tümleyeni, boyutu $3-2=1$ olan, $\mathbf{k}$ doğrultusundaki doğrudur. Sağlama: $\mathbf{y}-\mathbf{P}\mathbf{y}=(-\tfrac43,\,\tfrac43,\,\tfrac43)^{\top}=-\tfrac43\mathbf{k}$ bu doğru üzerindedir.
:::
:::

:::aufgabe Alıştırma 12 ★★ QR ile çözüm
<span class="anker" id="aufg-12"></span>

Sütunları Alıştırma [11](#aufg-11)'deki $\mathbf{a}_1$ ve $\mathbf{a}_2$ vektörleri olan $\mathbf{A}$ matrisini kullanın.

<ol class="al">

<li>

QR ayrışımını yazın ve $\mathbf{Q}\mathbf{R}=\mathbf{A}$ eşitliğini doğrulayın.

</li>

<li>

$\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$ sistemini en küçük kareler anlamında [(4.6)](#gl-4-6) ile ve sağlama için normal denklemlerle çözün.

</li>

</ol>

:::loesung
(a) Alıştırma [11](#aufg-11)'den: $\mathbf{q}_1=(1,\,1,\,0)^{\top}/\sqrt2$, $\mathbf{q}_2=(1,\,-1,\,2)^{\top}/\sqrt6$, $r_{11}=\lVert\mathbf{a}_1\rVert=\sqrt2$, $r_{12}=\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$, $r_{22}=\lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{3/2}$. Böylece:

$$\mathbf{Q}=\begin{pmatrix}1/\sqrt2&1/\sqrt6\\1/\sqrt2&-1/\sqrt6\\0&2/\sqrt6\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&1/\sqrt2\\0&\sqrt{3/2}\end{pmatrix}.$$

Sağlama: $\mathbf{Q}\mathbf{R}$ matrisinin birinci sütunu $\sqrt2\,\mathbf{q}_1=\mathbf{a}_1$ olur; ikinci sütunu $\tfrac1{\sqrt2}\mathbf{q}_1+\sqrt{\tfrac32}\,\mathbf{q}_2=\tfrac12(1,\,1,\,0)^{\top}+\tfrac12(1,\,-1,\,2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_2$ olur, çünkü $\sqrt{3/2}/\sqrt6=\tfrac12$.

(b) $\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac3{\sqrt2},\ \tfrac{1-2+6}{\sqrt6}\bigr)^{\top}=\bigl(\tfrac3{\sqrt2},\ \tfrac5{\sqrt6}\bigr)^{\top}$ olur. $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ sisteminin alt satırı $\hat x_2=\tfrac5{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac53$ verir; üst satırı $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac53=\tfrac3{\sqrt2}$ verir, bu da $\sqrt2$ ile çarpılınca $2\hat x_1+\tfrac53=3$, yani $\hat x_1=\tfrac23$ olur. Normal denklemlerle sağlama: $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$, $\mathbf{A}^{\top}\mathbf{y}=(3,\,4)^{\top}$, $\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(3,\,4)^{\top}=(\tfrac23,\,\tfrac53)^{\top}$. Ayrıca $\mathbf{A}\hat{\mathbf{x}}=(\tfrac73,\,\tfrac23,\,\tfrac53)^{\top}=\mathbf{P}\mathbf{y}$ olur; bu, Alıştırma [11](#aufg-11)'deki izdüşümdür.
:::
:::

:::aufgabe Alıştırma 13 ★★ Tümleyenler
<span class="anker" id="aufg-13"></span>

<ol class="al">

<li>

$\mathbb{R}^3$ uzayında orijinden geçen bir doğrunun ortogonal tümleyeni kaç boyutludur? $\mathbb{R}^5$ uzayındaki bir doğrununki kaç boyutludur?

</li>

<li>

$(\mathcal U^\perp)^\perp=\mathcal U$ olduğunu gösterin. İpucu: Önce $\mathcal U$ içindeki her vektörün $(\mathcal U^\perp)^\perp$ içinde olduğunu gösterin. Sonra bir $\mathbf{y}\in(\mathcal U^\perp)^\perp$ vektörünü Kesim [4.4](#stufe-4-4)'teki teoremde olduğu gibi ayrıştırın ve onun $\mathcal U^\perp$ içindeki parçasıyla iç çarpımını alın.

</li>

</ol>

:::loesung
(a) Kesim [4.4](#stufe-4-4)'teki teoreme göre $\dim\mathcal U^\perp=n-\dim\mathcal U$ olur: $\mathbb{R}^3$ uzayında bu $3-1=2$, yani bir düzlemdir; $\mathbb{R}^5$ uzayında $5-1=4$ olur.

(b) Birinci adım: $\mathbf{u}\in\mathcal U$ ise $\mathcal U^\perp$ tanımı gereği her $\mathbf{z}\in\mathcal U^\perp$ için $\mathbf{u}^{\top}\mathbf{z}=0$ olur. Dolayısıyla $\mathbf{u}$, $\mathcal U^\perp$ alt uzayının tamamına diktir ve $(\mathcal U^\perp)^\perp$ içindedir. İkinci adım: $\mathbf{y}\in(\mathcal U^\perp)^\perp$ olsun. Teoreme göre, $\mathbf{u}\in\mathcal U$ ve $\mathbf{z}\in\mathcal U^\perp$ olmak üzere $\mathbf{y}=\mathbf{u}+\mathbf{z}$ ayrışımı yapılır. O zaman $\mathbf{z}^{\top}\mathbf{y}=0$ olur, çünkü $\mathbf{y}$, $\mathcal U^\perp$ alt uzayına diktir; ayrıca $\mathbf{z}^{\top}\mathbf{u}=0$ olur, çünkü $\mathbf{z}$, $\mathcal U$ alt uzayına diktir. Dolayısıyla $\mathbf{z}^{\top}\mathbf{z}=\mathbf{z}^{\top}\mathbf{y}-\mathbf{z}^{\top}\mathbf{u}=0$ ve $\mathbf{z}=\mathbf{0}$ olur. Böylece $\mathbf{y}=\mathbf{u}\in\mathcal U$. İki küme birbirini içerir, yani eşittir.
:::
:::
