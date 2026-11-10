---
title: Özdeğerler ve özvektörler
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Bölüm 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15220700
summary: Bir matris çoğu vektörü aynı anda hem döndürür hem uzatır.
tags: karmaşık eşleniği, özvektörü, özdeğer, karakteristik polinomu, özuzayı, izi, cebirsel katlılığı, geometrik katlılığı
lang: tr
---

<span class="anker" id="stufe-6"></span>

:::zweck
Bir matris çoğu vektörü aynı anda hem döndürür hem uzatır. Ama bazı doğrultuları döndürmez: Böyle bir doğrultudaki bir ok yalnızca uzar, kısalır ya da ters döner. Bu kesim bu doğrultuları ve onlara ait uzama çarpanlarını buluyor. Bunlar bir matrisin doğal eksenleridir.
:::

:::::vorwissen Bunun için gerekenler: karmaşık sayılar

<span class="anker" id="stufe-6-1"></span>

Uzama çarpanları aranırken polinom denklemleri ortaya çıkar ve bunların hepsinin gerçel çözümü yoktur. Bu alt kesim, bu bölümün karmaşık sayılar hakkında kullandıklarını bir araya getiriyor.

**Karmaşık sayılar.** Bir $z=x+\mathrm j\,y$ karmaşık sayısı iki gerçel sayıdan, $x$ gerçel kısmından ve $y$ sanal kısmından oluşur. Sanal birim için $\mathrm j^2=-1$ geçerlidir. Birçok matematik kitabı onu $\mathrm i$ ile gösterir; bu bölüm Python gibi dik bir $\mathrm j$ yazar, çünkü Python $3+4\,\mathrm j$ sayısını `3+4j` olarak yazar ve $i$ indis olarak serbest kalır.

**Eşlenik ve mutlak değer.** $z$ sayısının __karmaşık eşleniği__ $z^*=x-\mathrm j\,y$ sayısıdır. $z\,z^*=x^2+y^2=|z|^2$ olur; bu, mutlak değerin karesidir, yani yalnızca $z=0$ için sıfır olan bir gerçel sayı. Bir sayı ancak ve ancak $z=z^*$ ise gerçeldir. Eşlenik alma toplam ve çarpımla uyumludur: $(z+w)^*=z^*+w^*$ ve $(zw)^*=z^*w^*$. Bileşenleri karmaşık olan bir $\mathbf{v}$ vektörü için bu bölümde $\mathbf{v}^*$, bileşenlerin eşleniklerinden oluşan vektörü gösterir; devrik alınmaz. Bu durumda şu geçerlidir:

$$(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0\qquad\mathbf{v}\ne\mathbf{0}\text{ için} .$$

**Euler formülü.** Her gerçel $\alpha$ sayısı için $\mathrm e^{\mathrm j\alpha}=\cos\alpha+\mathrm j\sin\alpha$ olur; bu, karmaşık düzlemin birim çemberi üzerinde, mutlak değeri $1$ olan bir noktadır.

**Polinomların kökleri.** Katsayıları gerçel ya da karmaşık olan ve derecesi $n\ge1$ olan her polinomun, katlı kökler katlılıkları kadar sayılırsa tam $n$ karmaşık kökü vardır ve polinom $n$ doğrusal çarpana ayrılır. Polinomun katsayıları gerçelse $z$ ile birlikte $z^*$ de bir köktür: Gerçel olmayan kökler çiftler halinde gelir.

::::beispiel [Sayısal örnek]
$\lambda^2-1{,}2\lambda+1=0$ denkleminin kökleri, ikinci dereceden denklemin kök formülüne göre $\lambda=0{,}6\pm\sqrt{0{,}36-1}=0{,}6\pm\mathrm j\,0{,}8$ olur; bu, mutlak değeri $\sqrt{0{,}36+0{,}64}=1$ olan eşlenik bir çifttir. $\mathbf{v}=(1,\,-\mathrm j)^{\top}$ için $\mathbf{v}^*=(1,\,\mathrm j)^{\top}$ ve $(\mathbf{v}^*)^{\top}\mathbf{v}=1\cdot1+\mathrm j\cdot(-\mathrm j)=1+1=2$ olur (Şekil [16](#abb-16)).

:::abbildung ml/k2rkomplex 16
$\mathbf{v}=(1,-\mathrm j)^{\top}$ için $(\mathbf{v}^*)^{\top}\mathbf{v}$ iç çarpımı: Her terim $v_i^*v_i=|v_i|^2$ olur, çünkü $\mathrm j\cdot(-\mathrm j)=-\mathrm j^2=1$.
:::
::::

⁠**Kısacası:** $\mathrm j^2=-1$ olmak üzere $x+\mathrm jy$ karmaşık sayıları her polinom denklemini çözer; eşlenik alma sanal kısmın işaretini değiştirir ve $zz^*=|z|^2$ gerçeldir.

:::::

### Özvektörler ve özdeğerler

<span class="anker" id="stufe-6-2"></span>

[Bölüm 1, Kesim 8.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3)'te düzlemin ızgarası matrislerle döndürülmüş, uzatılmış ve kaydırılmıştı. Bu sırada okların çoğu doğrultusunu değiştirir. Ama bazı matrislerde, bir okun orijinden geçen kendi doğrusu üzerinde kaldığı doğrultular vardır: Ok yalnızca uzar, kısalır ya da ters döner (Şekil [17](#abb-17)).

:::abbildung ml/k2eigen 17
$\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ matrisi birim çemberi (gri) bir elipse (mavi) dönüştürür. $\mathbf{v}_1=(1,1)^{\top}/\sqrt2$ oku (kırmızı) kendi doğrusu üzerinde kalır ve beş katına uzar, $\mathbf{v}_2=(1,-2)^{\top}/\sqrt5$ oku (yeşil) ise iki katına; görüntüleri açık renkle çizilmiştir. Gri doğrular iki öz doğrultudur. Buna karşılık $\mathbf{e}_1$ birim vektörü $(4,2)^{\top}$ vektörüne gider (kesikli) ve doğrultusunu değiştirir.
:::

:::definition Tanım 6.1 (Özvektör, özdeğer)
<span class="anker" id="satz-6-1"></span>

$\mathbf{A}\in\mathbb{R}^{n\times n}$ olsun. Bir $\mathbf{v}\ne\mathbf{0}$ vektörü için şu eşitliği sağlayan bir $\lambda$ sayısı varsa, bu vektöre $\mathbf{A}$ matrisinin bir __özvektörü__ denir:

<span class="anker" id="gl-6-1"></span>
$$\mathbf{A}\mathbf{v}=\lambda\,\mathbf{v} . \tag{6.1}$$

$\lambda$ sayısına da bu özvektöre ait __özdeğer__ denir.
:::

Sıfır vektörü dışarıda bırakılır, çünkü $\mathbf{A}\mathbf{0}=\lambda\mathbf{0}$ her $\lambda$ sayısı için geçerlidir ve hiçbir şey söylemez. Özdeğer ise sıfır olabilir: O zaman özvektör $\mathbf{0}$ vektörüne gider. Negatif bir özdeğer oku ters çevirir. Bu bölümde özdeğerler $\lambda$ ya da $\lambda_i$ ile gösterilir. Terim Almancadan gelir (*eigen* “öz, kendine ait” demektir) ve İngilizcede de kullanılır: *eigenvalue*, *eigenvector*.

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ için şu bulunur:

$$\mathbf{A}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}5\\5\end{pmatrix}=5\begin{pmatrix}1\\1\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\-2\end{pmatrix}=\begin{pmatrix}2\\-4\end{pmatrix}=2\begin{pmatrix}1\\-2\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}4\\2\end{pmatrix}.$$

Dolayısıyla $(1,\,1)^{\top}$, $5$ özdeğerine ait bir özvektördür; $(1,\,-2)^{\top}$ de $2$ özdeğerine ait bir özvektördür. $(1,\,0)^{\top}$ vektörü özvektör değildir, çünkü $(4,\,2)^{\top}$ onun bir katı değildir.
::::

⁠**Kısacası:** Bir özvektör matris tarafından döndürülmez, yalnızca bir sayıyla çarpılır; bu sayı özdeğerdir.

:::hintergrund Sonsuz uzunluktaki diziler için aynı fikir: bileşik faiz
$100$ avroluk bir bakiye yılda $5$ % faizle $100$, $105$, $110{,}25$, … avroya, genel olarak $n$ yıl sonra $a_n=100\cdot1{,}05^n$ değerine büyür. “Her değeri bir sonraki yılın değeriyle değiştir” kuralı bir $(a_0,a_1,a_2,\dots)$ dizisini $(a_1,a_2,a_3,\dots)$ dizisine dönüştürür. Bu kural doğrusaldır: İki dizinin toplamı kaydırılırsa kaydırılmış dizilerin toplamı elde edilir; katlar için de aynısı geçerlidir. Bakiye için şunu verir:

$$(105;\ 110{,}25;\ \dots)=1{,}05\cdot(100;\ 105;\ \dots) .$$

Dizinin biçimi korunur, yalnızca bir sayı çarpanı eklenir: $a_n=100\cdot1{,}05^n$ dizisi kaydırmanın bir özvektörüdür ve özdeğer $1{,}05$ faiz çarpanıdır. [(6.1)](#gl-6-1) denklemi bir matris için aynı şeyi söyler. Kaydırmanın bu tür dizilerden başka özvektörü de yoktur: Bütün $n$ değerleri için $a_{n+1}=\lambda\,a_n$ ise $a_n=a_0\,\lambda^n$ olur. İki durumda da, diziler için de vektörler için de, doğrusal kuralın yalnızca bir sayıyla çarptığı şeyler vardır.
:::

### Karakteristik polinom

<span class="anker" id="stufe-6-3"></span>

Özdeğerler tahmin yürütmeden nasıl bulunur? [(6.1)](#gl-6-1) denklemi, her şey bir tarafta olacak biçimde yeniden yazılır: $\mathbf{A}\mathbf{v}-\lambda\mathbf{v}=\mathbf{0}$, yani $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$. Aranan, bu homojen sistemin bir $\mathbf{v}\ne\mathbf{0}$ çözümünün bulunduğu bir $\lambda$ değeridir. [Bölüm 1, Kesim 11.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-5)'e göre bu şu demektir: $\mathbf{A}-\lambda\mathbf{I}$ matrisi tersinir değildir. [Bölüm 1, Kesim 14.6](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-6)'ya göre bu, ancak ve ancak determinantı sıfırsa böyledir.

:::definition Tanım 6.2 (Karakteristik polinom)
<span class="anker" id="satz-6-2"></span>

$\mathbf{A}\in\mathbb{R}^{n\times n}$ için

<span class="anker" id="gl-6-2"></span>
$$p(\lambda)=\det(\mathbf{A}-\lambda\mathbf{I}) \tag{6.2}$$

polinomuna $\mathbf{A}$ matrisinin __karakteristik polinomu__ denir.
:::

:::satz Teorem 6.3 (Özdeğerler köklerdir)
<span class="anker" id="satz-6-3"></span>

Bir $\lambda$ sayısı ancak ve ancak $p(\lambda)=0$ ise $\mathbf{A}$ matrisinin bir özdeğeridir.
:::

Karakteristik polinomun derecesi $n$ olur. $2\times2$ boyutlu bir matris için karakteristik polinom şudur:

<span class="anker" id="gl-6-3"></span>
$$\det\begin{pmatrix}a-\lambda&b\\c&d-\lambda\end{pmatrix}=(a-\lambda)(d-\lambda)-bc=\lambda^2-(a+d)\,\lambda+(ad-bc) . \tag{6.3}$$

Karmaşık sayılarla ilgili alt kesime göre bu polinomun, katlılıklarıyla sayıldığında tam $n$ karmaşık kökü vardır. Demek ki karmaşık özdeğerlere izin verilir ve katlı olanlar katlılıkları kadar sayılırsa, $n\times n$ boyutlu bir matrisin $n$ özdeğeri vardır.

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ için $p(\lambda)=\lambda^2-7\lambda+(12-2)=\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2)$ olur. Özdeğerler, önceki alt kesimdeki gibi $5$ ve $2$. $\operatorname{diag}(3;\,-1)$ köşegen matrisi için $p(\lambda)=(3-\lambda)(-1-\lambda)$ olur, kökleri $3$ ve $-1$: Bir köşegen matrisin özdeğerleri köşegenindedir, özvektörleri de birim vektörlerdir.
::::

⁠**Kısacası:** Özdeğerler $\det(\mathbf{A}-\lambda\mathbf{I})$ karakteristik polinomunun kökleridir; $n\times n$ boyutlu bir matrisin, katlılık ve karmaşık olanlar sayılınca $n$ özdeğeri vardır.

### Özvektörlerin hesaplanması

<span class="anker" id="stufe-6-4"></span>

Bir $\lambda$ özdeğeri biliniyorsa ona ait özvektörler, $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ homojen sisteminin $\mathbf{v}\ne\mathbf{0}$ çözümleridir. Bunlar Gauss eleme yöntemiyle bulunur. $\mathbf{v}$ ile birlikte $c\ne0$ olan her $c\,\mathbf{v}$ katı da bir özvektördür, çünkü $\mathbf{A}(c\mathbf{v})=c\lambda\mathbf{v}=\lambda(c\mathbf{v})$. Demek ki bir özvektör hiçbir zaman tek değildir, yalnızca doğrultusu tektir, bazen o bile değildir.

:::definition Tanım 6.4 (Özuzay)
<span class="anker" id="satz-6-4"></span>

$\mathbf{A}-\lambda\mathbf{I}$ matrisinin çekirdeğine $\mathbf{A}$ matrisinin $\lambda$ özdeğerine ait __özuzayı__ denir.
:::

Özuzay $\lambda$ özdeğerine ait bütün özvektörleri ve sıfır vektörünü içerir. Bir çekirdek olarak, Kesim [4.1](projektion-auf-einen-unterraum.html#stufe-4-1)'deki anlamda bir alt uzaydır.

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ ve $\lambda=5$ için şu bulunur:

$$\mathbf{A}-5\mathbf{I}=\begin{pmatrix}-1&1\\2&-2\end{pmatrix}.$$

İki satır da aynı şeyi ister: $-v_1+v_2=0$. Özuzay, $(1,\,1)^{\top}$ vektörünün bütün katlarından oluşan doğrudur. $\lambda=2$ için $\mathbf{A}-2\mathbf{I}=\bigl(\begin{smallmatrix}2&1\\2&1\end{smallmatrix}\bigr)$ olur ve koşul $2v_1+v_2=0$; özuzay $(1,\,-2)^{\top}$ doğrultusundaki doğrudur. Normlanmış özvektörler, Şekil [17](#abb-17) içindeki gibi $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ ve $\mathbf{v}_2=(1,\,-2)^{\top}/\sqrt5$ olur. Birbirlerine dik değildirler: $(1,\,1)(1,\,-2)^{\top}=-1\ne0$.
::::

⁠**Kısacası:** $\lambda$ özdeğerine ait özvektörler, $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ sisteminin $\mathbf{v}\ne\mathbf{0}$ çözümleridir; sıfır vektörüyle birlikte özuzayı oluştururlar.

### İz ve determinant

<span class="anker" id="stufe-6-5"></span>

[(6.3)](#gl-6-3) içinde, matrise bakınca hemen görülen iki sayı vardır: $ad-bc$ determinanttır, $a+d$ ise köşegen elemanlarının toplamıdır. Bu toplamın ayrı bir adı vardır. İki sayı da özdeğerlerle basit bir biçimde ilişkilidir ve bu yüzden sağlama için elverişlidir.

:::definition Tanım 6.5 (İz)
<span class="anker" id="satz-6-5"></span>

Bir $\mathbf{A}\in\mathbb{R}^{n\times n}$ kare matrisinin __izi__, köşegen elemanlarının toplamıdır:

<span class="anker" id="gl-6-4"></span>
$$\operatorname{iz}\mathbf{A}=a_{11}+a_{22}+\dots+a_{nn}=\sum_{i=1}^na_{ii} . \tag{6.4}$$
:::

:::satz Teorem 6.6 (Özdeğerlerden iz ve determinant)
<span class="anker" id="satz-6-6"></span>

$\lambda_1,\dots,\lambda_n$, katlılık ve karmaşık olanlar sayılarak $\mathbf{A}$ matrisinin özdeğerleriyse şunlar geçerlidir:

<span class="anker" id="gl-6-5"></span>
$$\operatorname{iz}\mathbf{A}=\lambda_1+\lambda_2+\dots+\lambda_n,\qquad \det\mathbf{A}=\lambda_1\cdot\lambda_2\cdots\lambda_n . \tag{6.5}$$

Ayrıca $\mathbf{A}\in\mathbb{R}^{m\times n}$ ve $\mathbf{B}\in\mathbb{R}^{n\times m}$ için $\operatorname{iz}(\mathbf{A}\mathbf{B})=\operatorname{iz}(\mathbf{B}\mathbf{A})$ olur.
:::

:::herleitung İz ve determinant
$n=2$ için: $\lambda^2-(a+d)\lambda+(ad-bc)$ polinomu $(\lambda-\lambda_1)(\lambda-\lambda_2)=\lambda^2-(\lambda_1+\lambda_2)\lambda+\lambda_1\lambda_2$ biçiminde çarpanlarına ayrılır. Katsayılar karşılaştırılırsa $a+d=\lambda_1+\lambda_2$ ve $ad-bc=\lambda_1\lambda_2$ çıkar.

Herhangi bir $n$ için $p(\lambda)$ aynı şekilde $(\lambda_1-\lambda)(\lambda_2-\lambda)\cdots(\lambda_n-\lambda)$ çarpanlarına ayrılır; işaret doğrudur, çünkü $\det(\mathbf{A}-\lambda\mathbf{I})$ içinde $(-\lambda)^n$ terimi bulunur. $\lambda=0$ konursa solda $\det\mathbf{A}$, sağda $\lambda_1\cdots\lambda_n$ kalır. İz için $\lambda^{n-1}$ teriminin katsayıları karşılaştırılır. Sağda bu katsayı $(-1)^{n-1}(\lambda_1+\dots+\lambda_n)$ olur. Solda Laplace açılımında $\lambda$ değişkeninin bu kadar yüksek bir kuvvetini yalnızca köşegen elemanlarının $(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$ çarpımı verir, hem de $(-1)^{n-1}(a_{11}+\dots+a_{nn})$ katsayısıyla.

Son önerme için: $\operatorname{iz}(\mathbf{A}\mathbf{B})=\sum_i(\mathbf{A}\mathbf{B})_{ii}=\sum_i\sum_la_{il}b_{li}$ ve $\operatorname{iz}(\mathbf{B}\mathbf{A})=\sum_l\sum_ib_{li}a_{il}$. Bu, yalnızca farklı sıralanmış olan aynı çift toplamdır.
:::

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ için $\operatorname{iz}\mathbf{A}=7=5+2$ (Şekil [18](#abb-18)) ve $\det\mathbf{A}=10=5\cdot2$ olur. $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ için $\operatorname{iz}=7$ ve $\det=6$; özdeğerler yani $\lambda^2-7\lambda+6=0$ denkleminin çözümleridir: $6$ ve $1$. Satırları $(1,0,2)$, $(0,1,1)$ olan $\mathbf{A}\in\mathbb{R}^{2\times3}$ ve $\mathbf{B}=\mathbf{A}^{\top}$ için $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ olur, izi $7$; $\mathbf{B}\mathbf{A}$ ise köşegen elemanları $1$, $1$ ve $5$ olan $3\times3$ boyutlu bir matristir, onun izi de $7$.

:::abbildung ml/k2rspur 18
$\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ matrisinin izi, köşegen elemanlarının toplamı olarak; bu iz, $5$ ve $2$ özdeğerlerinin toplamına eşittir.
:::
::::

⁠**Kısacası:** İz, köşegen elemanlarının toplamıdır ve aynı zamanda özdeğerlerin toplamıdır; determinant özdeğerlerin çarpımıdır.

### Karmaşık özdeğerler

<span class="anker" id="stufe-6-6"></span>

$90^\circ$'lik bir dönme hiçbir oku kendi doğrusu üzerinde bırakmaz: Her ok bir dik açı kadar döndürülür. Dolayısıyla bu dönmenin gerçel bir özvektörü olamaz. Bunun yerine ne olduğunu karakteristik polinom gösterir.

::::beispiel [Sayısal örnek 1]
$\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ dönmesi için $p(\lambda)=\lambda^2+1$ olur, kökleri $\lambda=\mathrm j$ ve $\lambda=-\mathrm j$. Özdeğerler saf sanaldır. $\lambda=\mathrm j$ özdeğerine $(1,\,-\mathrm j)^{\top}$ karmaşık özvektörü aittir, çünkü $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)(1,\,-\mathrm j)^{\top}=(\mathrm j,\,1)^{\top}=\mathrm j\,(1,\,-\mathrm j)^{\top}$.
::::

::::beispiel [Sayısal örnek 2]
Kesim [1.4](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-4)'teki $\mathbf{Q}=\bigl(\begin{smallmatrix}0{,}6&-0{,}8\\0{,}8&0{,}6\end{smallmatrix}\bigr)$ dönmesi için $p(\lambda)=\lambda^2-1{,}2\lambda+1$ olur ve karmaşık sayılarla ilgili sayısal örneğe göre özdeğerleri $0{,}6\pm\mathrm j\,0{,}8=\cos\alpha\pm\mathrm j\sin\alpha=\mathrm e^{\pm\mathrm j\alpha}$, burada $\alpha\approx53{,}13^\circ$. Genel olarak $\alpha$ açısı kadar dönmenin özdeğerleri $\mathrm e^{\pm\mathrm j\alpha}$ olur.
::::

Demek ki gerçel bir matrisin karmaşık özdeğerleri olabilir. Karakteristik polinomunun katsayıları gerçel olduğundan bunlar eşlenik çiftler halinde ortaya çıkar. Gerçel bir özvektör yalnızca gerçel bir özdeğere ait olabilir: $\mathbf{v}$ gerçel ve $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ olsaydı, $\lambda\mathbf{v}$ gerçel bir vektörün görüntüsü olarak gerçel olurdu, dolayısıyla $\lambda$ da. Karmaşık özdeğerler matrisin bir düzlemde döndürdüğünü gösterir.

⁠**Kısacası:** Gerçel bir matrisin karmaşık özdeğerleri olabilir, her zaman eşlenik çiftler halinde; $\alpha$ kadar bir dönmenin özdeğerleri $\mathrm e^{\pm\mathrm j\alpha}$ olur.

:::hintergrund Döndürmek $\mathrm e^{\mathrm j\alpha}$ ile çarpmak demektir
Karmaşık sayılarla sonuç doğrudan görülür. $(x_1,\,x_2)^{\top}$ oku $z=x_1+\mathrm jx_2$ karmaşık sayısıyla, yani karmaşık düzlemin bir noktasıyla özdeşleştirilir. O zaman $\alpha$ kadar bir dönme $\mathrm e^{\mathrm j\alpha}$ ile çarpmaktır: $\mathrm e^{\mathrm j\alpha}z=(x_1\cos\alpha-x_2\sin\alpha)+\mathrm j\,(x_1\sin\alpha+x_2\cos\alpha)$; bunlar [Bölüm 1, Kesim 8.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3)'teki dönme matrisi için $\mathbf{Q}\mathbf{x}$ vektörünün tam olarak iki bileşenidir. Karmaşık gösterimde dönme yani bir sayıyla çarpmadır ve bu sayı bir özdeğerdir. İkinci $\mathrm e^{-\mathrm j\alpha}$ özdeğeri, ters yönde dönen $z^*$ eşlenik gösterimine aittir.
:::

### Katlı özdeğerler

<span class="anker" id="stufe-6-7"></span>

Karakteristik polinomun çift katlı bir kökü olabilir. O zaman $n$ özdeğerden ikisi çakışır. Bir özdeğerin kaç kez yer aldığı ayrı bir sayıdır.

:::definition Tanım 6.7 (Cebirsel katlılık)
<span class="anker" id="satz-6-7"></span>

Bir $\lambda$ özdeğerinin __cebirsel katlılığı__, $\lambda$ sayısının karakteristik polinomun kökü olarak katlılığıdır.
:::

::::beispiel [Sayısal örnek]
$2\mathbf{I}=\operatorname{diag}(2;\,2)$ matrisi için $p(\lambda)=(2-\lambda)^2$: $2$ özdeğerinin cebirsel katlılığı $2$. [Bölüm 1, Kesim 8.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3)'teki $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ kayması için $p(\lambda)=(1-\lambda)^2$: $1$ özdeğerinin cebirsel katlılığı da $2$. $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ matrisinin iki farklı özdeğeri vardır, her birinin cebirsel katlılığı $1$.
::::

⁠**Kısacası:** Cebirsel katlılık, bir özdeğerin karakteristik polinomun kökü olarak kaç kez yer aldığını sayar.

### Kaç özvektör vardır

<span class="anker" id="stufe-6-8"></span>

Çift katlı özdeğerli iki örnek bambaşka davranır. $2\mathbf{I}$ matrisi her oku iki katına uzatır; $\ne\mathbf{0}$ olan her vektör bir özvektördür, özuzay düzlemin tamamıdır. Kayma her noktayı yüksekliği kadar sağa iter; yalnızca $x_1$ ekseni üzerindeki oklar kendi doğruları üzerinde kalır. Kaymanın özuzayı $\ker\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$, yani $(1,\,0)^{\top}$ doğrultusundaki doğrudur. Fark özuzayın boyutundadır.

:::definition Tanım 6.8 (Geometrik katlılık)
<span class="anker" id="satz-6-8"></span>

Bir özdeğerin __geometrik katlılığı__, özuzayının boyutudur.
:::

Geometrik katlılık en az $1$ olur, çünkü her özdeğere ait bir özvektör vardır; en fazla da cebirsel katlılık kadardır; bu ikinci önermeyi bölüm kanıtlamıyor. $2\mathbf{I}$ için iki katlılık da $2$, kaymada ise cebirsel katlılık $2$, geometrik katlılık $1$: Kaymanın bir özvektörü eksiktir.

:::satz Teorem 6.9 (Farklı özdeğerler, bağımsız özvektörler)
<span class="anker" id="satz-6-9"></span>

İkişer ikişer farklı $\lambda_1,\dots,\lambda_k$ özdeğerlerine ait $\mathbf{v}_1,\dots,\mathbf{v}_k$ özvektörleri doğrusal bağımsızdır. $n\times n$ boyutlu bir matrisin $n$ farklı özdeğeri varsa özvektörleri bir taban oluşturur.
:::

:::beweis Bağımsız özvektörler
İki özvektör için: $c_1\mathbf{v}_1+c_2\mathbf{v}_2=\mathbf{0}$ olsun. $\mathbf{A}$ uygulanırsa $c_1\lambda_1\mathbf{v}_1+c_2\lambda_2\mathbf{v}_2=\mathbf{0}$ çıkar. Bundan birinci denklemin $\lambda_2$ katı çıkarılırsa geriye $c_1(\lambda_1-\lambda_2)\mathbf{v}_1=\mathbf{0}$ kalır. $\lambda_1\ne\lambda_2$ ve $\mathbf{v}_1\ne\mathbf{0}$ olduğundan $c_1=0$, sonra da $c_2=0$ olur. Daha çok özvektör için de aynı yol izlenir: Bir bağımlılık olsaydı, sıfırdan farklı katsayıları olabildiğince az olan bir bağımlılık alınırdı. $\mathbf{A}$ uygulanır ve sonuçtan bağımlılığın, içinde yer alan özdeğerlerden birine eşit $\lambda$ katı çıkarılırsa, sıfırdan farklı katsayıları daha da az olan bir bağımlılık elde edilirdi; bu bir çelişkidir.
:::

::::beispiel [Sayısal örnek]
$\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ matrisinin $(1,\,1)^{\top}$ ve $(1,\,-2)^{\top}$ özvektörleri, farklı olan $5$ ve $2$ özdeğerlerine aittir; doğrusal bağımsızdırlar, çünkü $\det\bigl(\begin{smallmatrix}1&1\\1&-2\end{smallmatrix}\bigr)=-3\ne0$. Kaymanın ise yalnızca $(1,\,0)^{\top}$ öz doğrultusu vardır; iki bağımsız özvektörü yoktur.
::::

⁠**Kısacası:** Geometrik katlılık, bir özdeğere ait bağımsız özvektörleri sayar; cebirsel katlılıktan küçük olabilir, ama farklı özdeğerlerin özvektörleri her zaman bağımsızdır.

### Özdeğerler için hesap kuralları

<span class="anker" id="stufe-6-9"></span>

Bir matrisin özvektörlerini bilen, ondan kurulan birçok matrisin özvektörlerini de bilir. Kuralların hepsi doğrudan [(6.1)](#gl-6-1) denkleminden çıkar.

:::satz Teorem 6.10 (Hesap kuralları)
<span class="anker" id="satz-6-10"></span>

$\mathbf{v}\ne\mathbf{0}$ olmak üzere $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ olsun. O zaman şunlar geçerlidir:

<ol class="rm">

<li>

her $k$ doğal sayısı için $\mathbf{A}^k\mathbf{v}=\lambda^k\mathbf{v}$;

</li>

<li>

her $\beta$ sayısı için $(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=(\lambda+\beta)\mathbf{v}$;

</li>

<li>

$\mathbf{A}$ ancak ve ancak hiçbir özdeğeri sıfır değilse tersinirdir ve o zaman $\mathbf{A}^{-1}\mathbf{v}=\frac1\lambda\mathbf{v}$ olur;

</li>

<li>

$\mathbf{A}^{\top}$ matrisinin özdeğerleri $\mathbf{A}$ matrisininkilerle aynıdır, ama özvektörleri genel olarak farklıdır.

</li>

</ol>
:::

:::beweis Hesap kuralları
(i) $\mathbf{A}^2\mathbf{v}=\mathbf{A}(\lambda\mathbf{v})=\lambda\mathbf{A}\mathbf{v}=\lambda^2\mathbf{v}$ ve bu böyle sürer. (ii) $(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=\lambda\mathbf{v}+\beta\mathbf{v}$. (iii) [(6.5)](#gl-6-5) uyarınca $\det\mathbf{A}$ özdeğerlerin çarpımıdır, dolayısıyla ancak ve ancak hiçbir özdeğer sıfır değilse sıfırdan farklıdır. $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ eşitliği $\mathbf{A}^{-1}$ ile çarpılırsa $\mathbf{v}=\lambda\mathbf{A}^{-1}\mathbf{v}$ çıkar. (iv) [Bölüm 1, Kesim 14.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5)'e göre $\det(\mathbf{A}^{\top}-\lambda\mathbf{I})=\det\bigl((\mathbf{A}-\lambda\mathbf{I})^{\top}\bigr)=\det(\mathbf{A}-\lambda\mathbf{I})$; iki matrisin karakteristik polinomu aynıdır.
:::

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ için $\mathbf{A}^2=\bigl(\begin{smallmatrix}18&7\\14&11\end{smallmatrix}\bigr)$ matrisinin özdeğerleri $25$ ve $4$ olur: $\mathbf{A}^2(1,\,1)^{\top}=(25,\,25)^{\top}$. $\mathbf{A}-5\mathbf{I}$ matrisinin özdeğerleri $0$ ve $-3$ olur ve bu matris tersinir değildir. $\mathbf{A}^{-1}=\tfrac1{10}\bigl(\begin{smallmatrix}3&-1\\-2&4\end{smallmatrix}\bigr)$ tersinin özdeğerleri $\tfrac15$ ve $\tfrac12$ olur: $\mathbf{A}^{-1}(1,\,-2)^{\top}=\tfrac1{10}(5,\,-10)^{\top}=\tfrac12(1,\,-2)^{\top}$. $\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&2\\1&3\end{smallmatrix}\bigr)$ devriğinin özdeğerleri de $5$ ve $2$ olur, ama $\mathbf{A}^{\top}(1,\,1)^{\top}=(6,\,4)^{\top}$: Devriğin özvektörleri $(2,\,1)^{\top}$ ve $(1,\,-1)^{\top}$ olur.
::::

⁠**Kısacası:** Kuvvetler, $\beta\mathbf{I}$ kadar kaydırmalar ve ters matris özvektörleri korur ve özdeğerleri aynı biçimde değiştirir; devrik yalnızca özdeğerleri korur.

:::aufgabe Alıştırma 17 ★ Özdeğerler ve özvektörler
<span class="anker" id="aufg-17"></span>

Şu matrislerin özdeğerlerini ve özuzaylarını bulun:

$$\mathbf{A}_1=\begin{pmatrix}2&2\\1&3\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}3&0\\0&3\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&1\end{pmatrix}.$$

Her birinde izi ve determinantı kontrol edin. Hangi matriste özvektörler birbirine diktir?

:::loesung
$\mathbf{A}_1$: iz $5$, determinant $6-2=4$, dolayısıyla $\lambda^2-5\lambda+4=(\lambda-4)(\lambda-1)$. $\lambda=4$ için: $\mathbf{A}_1-4\mathbf{I}=\bigl(\begin{smallmatrix}-2&2\\1&-1\end{smallmatrix}\bigr)$, özuzay $(1,\,1)^{\top}$ doğrultusunda. $\lambda=1$ için: $\mathbf{A}_1-\mathbf{I}=\bigl(\begin{smallmatrix}1&2\\1&2\end{smallmatrix}\bigr)$, özuzay $(2,\,-1)^{\top}$ doğrultusunda. Sağlama: $4+1=5$, $4\cdot1=4$. Özvektörler birbirine dik değildir: $(1,\,1)(2,\,-1)^{\top}=1$.

$\mathbf{A}_2=3\mathbf{I}$: $p(\lambda)=(3-\lambda)^2$, $3$ özdeğeri çift katlı; özuzay düzlemin tamamıdır. Sağlama: $3+3=6$, $3\cdot3=9$. Birbirine dik iki özvektör seçilebilir, örneğin $\mathbf{e}_1$ ve $\mathbf{e}_2$, ama birbirine eğik iki özvektör de seçilebilir.

$\mathbf{A}_3$: iz $2$, determinant $1-9=-8$, dolayısıyla $\lambda^2-2\lambda-8=(\lambda-4)(\lambda+2)$. Özvektörler: $4$ için $(1,\,1)^{\top}$, $-2$ için $(1,\,-1)^{\top}$. Sağlama: $4-2=2$, $4\cdot(-2)=-8$. Birbirlerine diktirler; $\mathbf{A}_3$ simetriktir ve Kesim [7.5](diagonalisierung-und-spektralsatz.html#stufe-7-5) bunun bir rastlantı olmadığını gösteriyor.
:::
:::

:::aufgabe Alıştırma 18 ★ Üçgen matrisler
<span class="anker" id="aufg-18"></span>

Bir üst üçgen matrisin özdeğerlerinin köşegen elemanları olduğunu gösterin. $\Bigl(\begin{smallmatrix}2&1&0\\0&3&1\\0&0&5\end{smallmatrix}\Bigr)$ matrisinin özdeğerlerini ve özvektörlerini bulun.

:::loesung
Bir üst üçgen matris için $\mathbf{A}-\lambda\mathbf{I}$ da köşegen elemanları $a_{ii}-\lambda$ olan bir üst üçgen matristir. [Bölüm 1, Kesim 14.4](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-4)'e göre bu matrisin determinantı köşegen elemanlarının çarpımıdır: $p(\lambda)=(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$. Kökler köşegen elemanlarıdır.

Verilen matrisin özdeğerleri dolayısıyla $2$, $3$ ve $5$ olur. $2$ için: $\mathbf{A}-2\mathbf{I}=\Bigl(\begin{smallmatrix}0&1&0\\0&1&1\\0&0&3\end{smallmatrix}\Bigr)$ matrisi $v_3=0$ ve $v_2=0$ koşullarını verir, özvektör $(1,\,0,\,0)^{\top}$. $3$ için: $\Bigl(\begin{smallmatrix}-1&1&0\\0&0&1\\0&0&2\end{smallmatrix}\Bigr)$ matrisi $v_3=0$ ve $v_2=v_1$ koşullarını verir, özvektör $(1,\,1,\,0)^{\top}$. $5$ için: $\Bigl(\begin{smallmatrix}-3&1&0\\0&-2&1\\0&0&0\end{smallmatrix}\Bigr)$ matrisi $v_2=3v_1$ ve $v_3=2v_2$ koşullarını verir, özvektör $(1,\,3,\,6)^{\top}$. Sağlama: $\mathbf{A}(1,\,3,\,6)^{\top}=(2+3,\ 9+6,\ 30)^{\top}=5\,(1,\,3,\,6)^{\top}$.
:::
:::

:::aufgabe Alıştırma 19 ★★ Katlılıklar
<span class="anker" id="aufg-19"></span>

$\mathbf{B}_1=\bigl(\begin{smallmatrix}2&0\\0&2\end{smallmatrix}\bigr)$, $\mathbf{B}_2=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ ve $\mathbf{B}_3=\Bigl(\begin{smallmatrix}1&0&0\\0&1&1\\0&0&1\end{smallmatrix}\Bigr)$ için bütün özdeğerleri, cebirsel ve geometrik katlılıklarıyla birlikte bulun.

:::loesung
$\mathbf{B}_1=2\mathbf{I}$: özdeğer $2$, cebirsel katlılık $2$, özuzay düzlemin tamamı, geometrik katlılık $2$.

$\mathbf{B}_2$: üçgen matris, cebirsel katlılığı $2$ olan $2$ özdeğeri. $\mathbf{B}_2-2\mathbf{I}=\bigl(\begin{smallmatrix}0&3\\0&0\end{smallmatrix}\bigr)$ matrisi $v_2=0$ koşulunu verir; özuzay $x_1$ eksenidir, geometrik katlılık $1$. Kaymada olduğu gibi $\mathbf{B}_2$ matrisinin de bir özvektörü eksiktir.

$\mathbf{B}_3$: üçgen matris, cebirsel katlılığı $3$ olan $1$ özdeğeri. $\mathbf{B}_3-\mathbf{I}=\Bigl(\begin{smallmatrix}0&0&0\\0&0&1\\0&0&0\end{smallmatrix}\Bigr)$ matrisi yalnızca $v_3=0$ koşulunu verir; özuzay $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ olur, geometrik katlılık $2$. Burada geometrik katlılık $1$ ile cebirsel katlılık arasındadır.
:::
:::

:::aufgabe Alıştırma 20 ★★ Bir dönme ve bir yansıma
<span class="anker" id="aufg-20"></span>

<ol class="al">

<li>

$30^\circ$ kadar dönmenin özdeğerlerini hesaplayın ve $\mathrm e^{\pm\mathrm j\alpha}$ biçiminde yazın.

</li>

<li>

Kesim [1.5](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-5)'teki $\bigl(\begin{smallmatrix}0{,}6&0{,}8\\0{,}8&-0{,}6\end{smallmatrix}\bigr)$ yansıması da ortogonaldir. Özdeğerlerini ve özvektörlerini bulun ve bunları geometrik olarak yorumlayın.

</li>

<li>

Ortogonal bir matrisin her gerçel özdeğerinin $1$ ya da $-1$ olduğunu gösterin.

</li>

</ol>

:::loesung
(a) $30^\circ$ kadar dönme $\bigl(\begin{smallmatrix}\sqrt3/2&-1/2\\1/2&\sqrt3/2\end{smallmatrix}\bigr)$ matrisidir; izi $\sqrt3$, determinantı $1$. Dolayısıyla $p(\lambda)=\lambda^2-\sqrt3\,\lambda+1$ ve

$$\lambda=\frac{\sqrt3\pm\sqrt{3-4}}2=\frac{\sqrt3}2\pm\mathrm j\,\frac12=\cos30^\circ\pm\mathrm j\sin30^\circ=\mathrm e^{\pm\mathrm j\,30^\circ} .$$

(b) İz $0$, determinant $-0{,}36-0{,}64=-1$, dolayısıyla $p(\lambda)=\lambda^2-1$ ve özdeğerler $1$ ile $-1$. $1$ için: $\bigl(\begin{smallmatrix}-0{,}4&0{,}8\\0{,}8&-1{,}6\end{smallmatrix}\bigr)$, özvektör $(2,\,1)^{\top}$. $-1$ için: $\bigl(\begin{smallmatrix}1{,}6&0{,}8\\0{,}8&0{,}4\end{smallmatrix}\bigr)$, özvektör $(1,\,-2)^{\top}$. Geometrik olarak: $(2,\,1)^{\top}$ doğrultusundaki yansıma ekseninin noktaları yerinde kalır, özdeğer $1$; buna dik doğrultu ters çevrilir, özdeğer $-1$. İki özvektör birbirine diktir, çünkü matris simetriktir.

(c) Gerçel $\lambda$ ve gerçel $\mathbf{v}\ne\mathbf{0}$ ile $\mathbf{Q}\mathbf{v}=\lambda\mathbf{v}$ olsun. [(1.3)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-3) uyarınca $\lVert\mathbf{v}\rVert=\lVert\mathbf{Q}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$ olur, dolayısıyla $|\lambda|=1$ ve $\lambda=\pm1$. Rijit bir hareket, bir oku kendi doğrusu üzerinde ancak yerinde bırakabilir ya da ters çevirebilir; uzatamaz.
:::
:::
