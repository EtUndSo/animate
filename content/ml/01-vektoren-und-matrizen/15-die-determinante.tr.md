---
title: Determinant
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Bölüm 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15211500
summary: Doğrusal bir dönüşüm düzlemin ızgarasının biçimini değiştirir ve bu sırada alanlar büyür ya da küçülür.
tags: determinantı, yönelim, Laplace açılımı
lang: tr
---

<span class="anker" id="stufe-14"></span>

:::zweck
Doğrusal bir dönüşüm düzlemin ızgarasının biçimini değiştirir ve bu sırada alanlar büyür ya da küçülür. Bu kesim, alanların hangi çarpanla değiştiğini belirliyor. Bu çarpan tek bir sayıdır, determinanttır; bir matrisin tersinir olup olmadığı da ondan anlaşılır.
:::

### $2\times2$ tipinde bir matrisin determinantı

<span class="anker" id="stufe-14-1"></span>

Birim karenin alanı $1$ olur. Bir $\mathbf{A}$ matrisi birim kareyi, matrisin iki sütununun gerdiği paralelkenara götürür (alt kesim [8.3](lineare-abbildungen.html#stufe-8-3)). Bu paralelkenarın alanı ne kadardır? Şekil [40](#abb-40) bunu $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ için gösteriyor.

:::abbildung ml/k1det 40
Solda alanı $1$ olan birim kare, sağda onun $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ altındaki görüntüsü: $\mathbf{a}_1$ ve $\mathbf{a}_2$ sütunlarından oluşan paralelkenar. Bu paralelkenarın alanı $5=3\cdot2-1\cdot1$ olur. Kesikli çizgiyle, alanın hesaplanmasını sağlayan çevreleyen dikdörtgen.
:::

:::herleitung Paralelkenarın alanı
Sütunlar, hepsi pozitif sayılarla $\mathbf{a}_1=(a,\,c)^{\top}$ ve $\mathbf{a}_2=(b,\,d)^{\top}$ olsun ve $\mathbf{a}_2$, Şekil [40](#abb-40) içindeki gibi $\mathbf{a}_1$ vektörünün sol üstünde bulunsun. Köşeleri $\mathbf{0}$, $\mathbf{a}_1$, $\mathbf{a}_1+\mathbf{a}_2$, $\mathbf{a}_2$ olan paralelkenar, kenarları $a+b$ ve $c+d$ olan dikdörtgenin içine sığar. Geriye yalnızca paralelkenarın kalması için dikdörtgenden dik kenarları $a$ ve $c$ olan iki üçgen, dik kenarları $b$ ve $d$ olan iki üçgen ve kenarları $b$ ve $c$ olan iki dikdörtgen kesilip çıkarılır:

$$(a+b)(c+d)-2\cdot\tfrac12ac-2\cdot\tfrac12bd-2\,bc=ac+ad+bc+bd-ac-bd-2bc=ad-bc .$$

$\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ için: $4\cdot3-3-2-2=5$.
:::

:::definition Tanım 14.1 ($2\times2$ tipinde bir matrisin determinantı)
<span class="anker" id="satz-14-1"></span>

$\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ matrisinin __determinantı__ şu sayıdır:

<span class="anker" id="gl-14-1"></span>
$$\det\mathbf{A}=ad-bc . \tag{14.1}$$
:::

Determinantın mutlak değeri, sütunların gerdiği paralelkenarın alanı, yani $\mathbf{A}$ matrisinin birim karenin alanını değiştirdiği çarpandır. Bu, [(11.2)](einheitsmatrix-und-inverse.html#gl-11-2) formülündeki tersin paydasında duran sayının ta kendisidir.

::::beispiel [Sayısal örnek]
$\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=6-1=5$, $\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=2-1=1$, $\det\operatorname{diag}(2;\,0{,}5)=1$ ve $\det\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=0$. Germe, karenin biçimini değiştirir, ama alanını değiştirmez: Eni ne kadar uzatıyorsa boyu o kadar kısaltır.
::::

⁠**Kısacası:** $2\times2$ tipinde bir matrisin $ad-bc$ determinantı, mutlak değerce, dönüşümün birim karenin alanını değiştirdiği çarpandır.

### Determinantın işareti

<span class="anker" id="stufe-14-2"></span>

Bir alan hiçbir zaman negatif değildir, determinant ise negatif olabilir. İşaret ek bir bilgi taşır: dönüşümün düzlemi yansıtıp yansıtmadığını.

Birim karede $\mathbf{e}_2$, $\mathbf{e}_1$ vektöründen bakıldığında saat yönünün tersinde bulunur. Görüntülerde de bu böyle kalıyorsa, yani $\mathbf{a}_2$ de $\mathbf{a}_1$ vektöründen bakıldığında saat yönünün tersinde bulunuyorsa $\det\mathbf{A}>0$ olur. $\mathbf{a}_2$, $\mathbf{a}_1$ vektöründen bakıldığında saat yönündeyse düzlem yansıtılmıştır ve $\det\mathbf{A}<0$ olur. Bu niteliğe __yönelim__ denir: Pozitif bir determinant yönelimi korur, negatif bir determinant onu tersine çevirir.

::::beispiel [Sayısal örnek]
$x_1$ eksenine göre yansımanın, yani $\operatorname{diag}(1;\,-1)$ matrisinin determinantı $-1$ olur: Alan aynı kalır, yönelim tersine döner. Bir matrisin sütunlarının yeri değiştirilirse determinant işaret değiştirir: $\det\bigl(\begin{smallmatrix}1&3\\2&1\end{smallmatrix}\bigr)=1-6=-5$. $90^\circ$ kadar dönme için $\det=0\cdot0-(-1)\cdot1=1$, kayma için $\det=1\cdot1-1\cdot0=1$ olur; $\operatorname{diag}(1;\,0)$ yassılaştırmasının determinantı ise $0$ olur.
::::

⁠**Kısacası:** Determinantın mutlak değeri alan çarpanıdır; işareti, dönüşümün yansıtıp yansıtmadığını söyler.

### Alan çarpanı her şekil için geçerlidir

<span class="anker" id="stufe-14-3"></span>

Şimdiye kadar söz konusu olan birim kareydi. Ama doğrusal bir dönüşüm düzlemin her yerine aynı biçimde davranır ve bu yüzden her geometrik şeklin alanını aynı çarpanla değiştirir.

:::satz Teorem 14.2 (Alan çarpanı)
<span class="anker" id="satz-14-2"></span>

$\mathbf{A}\in\mathbb{R}^{2\times2}$ matrisi, alanı $F$ olan bir şekli dönüştürürse görüntünün alanı $|\det\mathbf{A}|\cdot F$ olur.
:::

:::herleitung Alan çarpanı
Şeklin üzerine, kenar uzunluğu $h$ olan küçük karelerden oluşan ince bir ızgara konur. Bir köşesi $\mathbf{q}$ olan bir karenin köşeleri $\mathbf{q}$, $\mathbf{q}+h\mathbf{e}_1$, $\mathbf{q}+h\mathbf{e}_1+h\mathbf{e}_2$ ve $\mathbf{q}+h\mathbf{e}_2$ olur. Görüntüsünün köşeleri $\mathbf{A}\mathbf{q}$, $\mathbf{A}\mathbf{q}+h\mathbf{a}_1$, $\mathbf{A}\mathbf{q}+h\mathbf{a}_1+h\mathbf{a}_2$ ve $\mathbf{A}\mathbf{q}+h\mathbf{a}_2$ olur: Bu, $h\mathbf{a}_1$ ve $h\mathbf{a}_2$ vektörlerinden oluşan ve $\mathbf{A}\mathbf{q}$ noktasına kaydırılmış paralelkenardır. Alanı, karenin nerede bulunduğundan bağımsız olarak $h^2\,|\det\mathbf{A}|$ olur. Demek ki her küçük kare aynı $|\det\mathbf{A}|$ çarpanıyla büyür ya da küçülür. Söz konusu şekil yaklaşık olarak bu tür karelerden oluşur ve ızgara ne kadar inceyse yaklaşım o kadar iyidir. Bu yüzden çarpan bütün şekil için geçerlidir.
:::

::::beispiel [Sayısal örnek]
Yarıçapı $1$ olan çemberin çevrelediği alan $\pi$ olur. $\operatorname{diag}(3;\,2)$ germesi bunu yarı eksenleri $3$ ve $2$ olan bir elipse dönüştürür. Elipsin alanı $\pi\cdot3\cdot2=6\pi$, yani çemberin çevrelediği alanın tam $|\det\mathbf{A}|=6$ katıdır. Köşeleri $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_2$ olan üçgenin alanı $\tfrac12$ olur; bu üçgen $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ altında köşeleri $\mathbf{0}$, $(3,1)^{\top}$, $(1,2)^{\top}$ olan ve alanı $\tfrac52$ olan üçgene dönüşür.
::::

⁠**Kısacası:** Doğrusal bir dönüşüm her şeklin alanını aynı $|\det\mathbf{A}|$ çarpanıyla değiştirir, çünkü ızgaranın her küçük karesine aynı biçimde davranır.

### Daha büyük matrislerin determinantları

<span class="anker" id="stufe-14-4"></span>

Uzayda birim küp, matrisin üç sütununun gerdiği paralelyüze, yani eğik biçimde çarpılmış bir dikdörtgenler prizmasına dönüşür. Paralelyüzün hacmi, dönüşümün hacimleri değiştirdiği çarpandır. Daha büyük matrisler için de böyle bir sayı vardır. Bu sayı, daha küçük matrislerin determinantlarına indirgenerek hesaplanır.

:::definition Tanım 14.3 (Determinant)
<span class="anker" id="satz-14-3"></span>

$\mathbf{A}\in\mathbb{R}^{1\times1}$ için $\det\mathbf{A}=a_{11}$ olur. $n\ge2$ olmak üzere $\mathbf{A}\in\mathbb{R}^{n\times n}$ için şu geçerlidir:

<span class="anker" id="gl-14-2"></span>
$$\det\mathbf{A}=\sum_{j=1}^n(-1)^{1+j}\,a_{1j}\,\det\mathbf{A}_{1j} , \tag{14.2}$$

burada $\mathbf{A}_{1j}$, $\mathbf{A}$ matrisinin birinci satırı ve $j$ numaralı sütunu silinerek elde edilen $(n-1)\times(n-1)$ tipindeki matristir. Bu hesap kuralına birinci satıra göre __Laplace açılımı__ denir.
:::

$n=2$ için [(14.2)](#gl-14-2) yine $a_{11}a_{22}-a_{12}a_{21}$ verir. Açılım, $a_{ij}$ elemanı için $(-1)^{i+j}$ işaretiyle, başka herhangi bir satıra ya da sütuna göre de yapılabilir; sonuç hep aynıdır. $n=3$ için $|\det\mathbf{A}|$ üç sütundan oluşan paralelyüzün hacmidir; işaret ise sütunların $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ ile aynı dönme yönünde mi (sağ el kuralı) yoksa yansıtılmış olarak mı dizildiğini söyler.

::::beispiel [Sayısal örnek]
Gauss eleme yöntemindeki katsayı matrisi (alt kesim [12.3](lineare-gleichungssysteme.html#stufe-12-3)) için,

$$\mathbf{A}=\begin{pmatrix}1&2&1\\2&1&1\\1&1&2\end{pmatrix},$$

birinci satıra göre Laplace açılımı $\det\mathbf{A}=-4$ verir (Şekil [41](#abb-41)).

:::abbildung ml/k1rlaplace 41
Birinci satıra göre Laplace açılımı: Birinci satırın her elemanı çarpı, o elemanın satırı ve sütunu çıkarılınca kalan matrisin determinantı; işaretler sırayla değişir.
:::
::::

Köşegeninin altında yalnızca sıfırlar bulunan bir üst üçgen matriste açılım tekrar tekrar birinci sütuna göre yapılır ve köşegen elemanlarının çarpımı elde edilir; örneğin $\det\Bigl(\begin{smallmatrix}2&1&3\\0&3&1\\0&0&4\end{smallmatrix}\Bigr)=2\cdot3\cdot4=24$.

⁠**Kısacası:** $n\times n$ tipinde bir matrisin determinantı Laplace açılımıyla daha küçük determinantlara indirgenir; mutlak değeri, dönüşümün hacimleri değiştirdiği çarpandır.

### Determinantlar için hesap kuralları

<span class="anker" id="stufe-14-5"></span>

En önemli kural doğrudan sezgiden çıkar. İki dönüşüm art arda uygulanırsa birincisi hacmi kendi çarpanıyla, ikincisi de sonucu bir kez daha kendi çarpanıyla değiştirir. Çarpanlar birbiriyle çarpılır.

:::satz Teorem 14.4 (Determinantın hesap kuralları)
<span class="anker" id="satz-14-4"></span>

$\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ ve bir $c$ sayısı için şunlar geçerlidir:

<ol class="rm">

<li>

$\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\cdot\det\mathbf{B}$;

</li>

<li>

$\det\mathbf{A}^{\top}=\det\mathbf{A}$;

</li>

<li>

$\mathbf{A}$ tersinirse $\det\mathbf{A}^{-1}=1/\det\mathbf{A}$;

</li>

<li>

$\det(c\,\mathbf{A})=c^n\det\mathbf{A}$;

</li>

<li>

Bir satırın bir katı başka bir satıra eklenirse determinant değişmez; iki satırın yeri değiştirilirse determinant işaret değiştirir; bir satır $c$ ile çarpılırsa determinant da $c$ ile çarpılır.

</li>

</ol>
:::

(iii) kuralı, $\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$ ve $\det\mathbf{I}=1$ ile (i) kuralından çıkar. (iv) kuralı şunu söyler: Birim küpün $n$ kenarının hepsi $c$ katına gerilirse hacmi $c^n$ katına çıkar. (v) kuralı, Gauss eleme yöntemini determinant hesaplamanın pratik yolu yapar: Matris satır basamak biçimine getirilir, yer değiştirmelerin sayısı akılda tutulur ve köşegen elemanları çarpılır.

::::beispiel [Sayısal örnek 1]
$\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=1$ ve $\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=5$ olduğundan $\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$ çarpımının determinantı $5$ olmalıdır: $21-16=5$.
::::

::::beispiel [Sayısal örnek 2]
Gauss eleme yönteminin uygulamasında (alt kesim [12.3](lineare-gleichungssysteme.html#stufe-12-3)) katsayı matrisi, katların eklenmesi ve bir yer değiştirmeyle köşegeni $1$, $-1$, $-4$ olan basamak biçimine getirilmişti. Demek ki determinantı, Laplace açılımında olduğu gibi $(-1)\cdot\bigl(1\cdot(-1)\cdot(-4)\bigr)=-4$ olur.
::::

⁠**Kısacası:** Bir çarpımın determinantı determinantların çarpımıdır, çünkü hacim çarpanları art arda çarpılır; uygulamada determinant Gauss eleme yöntemiyle hesaplanır.

:::hintergrund Satır işlemleri determinantı neden tam da böyle değiştirir?
(ii) kuralına göre satırlar yerine sütunlar da aynı biçimde dönüştürülebilir ve paralelkenarı ya da paralelyüzü geren sütunlardır. Bir sütuna başka bir sütunun bir katı eklenirse, örneğin $\mathbf{a}_2\to\mathbf{a}_2+t\,\mathbf{a}_1$, $\mathbf{a}_1$ kenarının karşısındaki kenar $\mathbf{a}_1$ vektörüne paralel olarak kayar. Paralelkenar, yana doğru itilen bir iskambil destesi gibi kaydırılır. Bu sırada taban ve yükseklik aynı kalır, dolayısıyla alan da aynı kalır. Uzayda aynı şey paralelyüz için geçerlidir: Tabana paralel her kesit yalnızca kaydırılır, değiştirilmez ve her yükseklikte eşit büyüklükte kesitleri olan cisimlerin hacmi aynıdır (Cavalieri ilkesi). İki sütunun yeri değiştirilirse alan aynı kalır, ama birinci sütundan ikinciye dönme yönü tersine döner ve onunla birlikte işaret de. Bir sütun $c$ ile çarpılırsa bir kenar $c$ kat uzar ve hacim $c$ kat büyür. $2\times2$ tipindeki matrisler için $ad-bc$ formülü bunu doğrudan doğrular, örneğin kayma için: $a\,(d+t\,c)-(b+t\,a)\,c=ad-bc$.

Tersine, determinantı yalnızca üç nitelik tamamen belirler: $\det\mathbf{I}=1$; iki satırın yeri değiştirilirse işaret değişir; bir satır dışındaki bütün satırlar sabit tutulursa determinant bu tek satırda doğrusaldır. Matrisin bu üç niteliğe sahip her fonksiyonu determinantın kendisidir. Nedeni Gauss eleme yöntemidir: Bu yöntem her kare matrisi satır işlemleriyle $\mathbf{I}$ matrisine ya da bir sıfır satırı olan bir matrise indirger ve her işlemin etkisi bu üç nitelikle belirlenmiştir. Bu yüzden birçok ders kitabı determinantı bu niteliklerle tanımlar ve Laplace açılımını onlardan türetir.
:::

:::hintergrund Determinantlar neden Laplace açılımıyla hesaplanmaz?
$n\times n$ tipinde bir matrisin Laplace açılımı $n-1$ büyüklüğünde $n$ determinant çağırır, bunların her biri $n-2$ büyüklüğünde $n-1$ determinant çağırır ve bu böyle sürer. Açık yazıldığında $n!$ çarpım ortaya çıkar. $n=20$ için bu sayı $2\cdot10^{18}$ değerinden fazladır; bir bilgisayar için karşılanamayacak kadar pahalıdır. Gauss eleme yöntemi ise yalnızca yaklaşık $\tfrac23n^3$ temel aritmetik işlem gerektirir, yani $n=20$ için birkaç bin. Bu yüzden Laplace açılımı bir tanım ve küçük matrisler ile türetmeler için bir araçtır, bir hesap yöntemi değildir.
:::

### Determinant ve tersinirlik

<span class="anker" id="stufe-14-6"></span>

Determinant sıfırsa birim kare alanı olmayan bir şekle, yani bir doğru parçasına ya da bir noktaya dönüşür. Dönüşüm düzlemi yassılaştırır ve yassılaştırılmış olan yeniden kurulamaz.

:::satz Teorem 14.5 (Determinant ve tersinirlik)
<span class="anker" id="satz-14-5"></span>

Bir $\mathbf{A}$ kare matrisi ancak ve ancak $\det\mathbf{A}\ne0$ ise tersinirdir.
:::

:::beweis Determinant ve tersinirlik
$\mathbf{A}$ tersinirse (i) kuralına göre $\det\mathbf{A}\cdot\det\mathbf{A}^{-1}=\det\mathbf{I}=1$, dolayısıyla $\det\mathbf{A}\ne0$ olur. Tersine $\det\mathbf{A}\ne0$ ise $\mathbf{A}$ Gauss eleme yöntemiyle satır basamak biçimine getirilir. (v) kuralına göre determinant bu sırada en fazla sıfırdan farklı çarpanlarla değişir; dolayısıyla basamak biçiminin determinantı da sıfır değildir. Bu determinant köşegen elemanlarının çarpımıdır, dolayısıyla bunların hiçbiri sıfır değildir ve $n$ pivot vardır. Böylece $\operatorname{rank}\mathbf{A}=n$ olur ve alt kesim [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5) içindeki teoreme göre $\mathbf{A}$ tersinirdir.
:::

Demek ki alt kesim [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5) içindeki teoremle birlikte bir kare matris için şunlar denktir: $\det\mathbf{A}\ne0$, $\mathbf{A}$ tersinir, $\operatorname{rank}\mathbf{A}=n$, $\ker\mathbf{A}=\{\mathbf{0}\}$, sütunlar doğrusal bağımsız.

::::beispiel [Sayısal örnek]
$\mathbf K$ matrisi (alt kesim [13.4](unabhangigkeit-basis-und-rang.html#stufe-13-4)) için $\det\mathbf K=1\cdot(2-1)-0+1\cdot(0-1)=0$ olur; bu, $\operatorname{rank}\mathbf K=2$ ile uyumludur. Gauss eleme yöntemiyle çözülen sistemin katsayı matrisi için $\det=-4\ne0$ olur ve bu matris tersinirdir; bu yüzden sistemin tam olarak bir çözümü vardı.
::::

⁠**Kısacası:** Bir kare matris ancak ve ancak determinantı sıfır değilse, yani uzayı yassılaştırmıyorsa tersinirdir.

:::hintergrund Küçük bir determinant “neredeyse tersinir değil” demek değildir
Çok küçük determinantlı bir matrisin neredeyse tekil olduğu düşünülebilir. Bu doğru değildir. $0{,}1\,\mathbf{I}_{10}$ matrisinin determinantı $0{,}1^{10}=10^{-10}$ olur, ama matris son derece rahat tersine çevrilebilir: Tersi $10\,\mathbf{I}_{10}$ olur ve matris bütün uzunlukları onda birine kısaltmaktan başka bir şey yapmaz. Minicik determinant yalnızca $0{,}1$ çarpanının on doğrultuda birbiriyle çarpılmasından gelir. Tersine, $\operatorname{diag}(1000;\,0{,}001)$ matrisi düzlemi bir doğrultuda neredeyse yassılaştırmasına rağmen determinantı $1$ olur. Determinant hacmi ölçer ve hacim ölçeğe bağlıdır. Bir matrisin bilgiyi “neredeyse” yok edip etmediği determinantından güvenilir biçimde anlaşılamaz.
:::

:::aufgabe Alıştırma 34 ★ Determinant hesaplamak
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

$\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)$ ve $\Bigl(\begin{smallmatrix}1&2&0\\3&1&2\\0&1&1\end{smallmatrix}\Bigr)$ matrislerinin determinantlarını hesaplayın. İki matristen hangisi tersinirdir?

</li>

<li>

Köşeleri $(0,\,0)$, $(3,\,1)$ ve $(1,\,2)$ olan üçgenin alanı nedir?

</li>

<li>

$(1,\,0,\,0)^{\top}$, $(1,\,2,\,0)^{\top}$ ve $(0,\,1,\,3)^{\top}$ vektörlerinden oluşan paralelyüzün hacmi nedir?

</li>

</ol>

:::loesung
(a) $\det\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)=4-4=0$: tersinir değil, ikinci sütun birincinin iki katıdır. $3\times3$ tipindeki matris için birinci satıra göre açılım:

$$1\cdot\det\begin{pmatrix}1&2\\1&1\end{pmatrix}-2\cdot\det\begin{pmatrix}3&2\\0&1\end{pmatrix}+0=1\cdot(1-2)-2\cdot3=-7 .$$

Bu matris tersinirdir.

(b) Üçgen, $(3,1)^{\top}$ ve $(1,2)^{\top}$ vektörlerinin gerdiği, alanı $|\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)|=5$ olan paralelkenarın yarısıdır; dolayısıyla alanı $2{,}5$ olur. Aynı sonuç alan çarpanından da çıkar: Köşeleri $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_2$ olan ve alanı $\tfrac12$ olan üçgen bu üçgene gönderilir.

(c) Vektörler sütun olarak yazılınca $\Bigl(\begin{smallmatrix}1&1&0\\0&2&1\\0&0&3\end{smallmatrix}\Bigr)$ elde edilir; bu, determinantı $1\cdot2\cdot3=6$ olan bir üst üçgen matristir. Hacim $6$ olur.
:::
:::

:::aufgabe Alıştırma 35 ★★ Hesap kurallarını doğrulamak
<span class="anker" id="aufg-35"></span>

<ol class="al">

<li>

$\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ ve $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$ için $\det(\mathbf{C}\mathbf{D})=\det\mathbf{C}\cdot\det\mathbf{D}$ eşitliğini kontrol edin ve $\det(3\,\mathbf{C})$ değerini hesaplayın.

</li>

<li>

Her $\mathbf R_\alpha$ dönme matrisinin determinantının $1$ olduğunu gösterin. Bu geometrik olarak ne anlama gelir?

</li>

<li>

İki sütunu aynı olan bir matrisin determinantının neden $0$ olduğunu hesap yapmadan gerekçelendirin.

</li>

</ol>

:::loesung
(a) $\det\mathbf{C}=4-6=-2$, $\det\mathbf{D}=0-1=-1$ ve $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$ için $\det=14-12=2=(-2)\cdot(-1)$. Ayrıca $3\mathbf{C}=\bigl(\begin{smallmatrix}3&6\\9&12\end{smallmatrix}\bigr)$ için $\det=36-54=-18=3^2\cdot(-2)$; (iv) kuralı da $n=2$ için bunu söyler.

(b) $\det\mathbf R_\alpha=\cos\alpha\cdot\cos\alpha-(-\sin\alpha)\cdot\sin\alpha=\cos^2\alpha+\sin^2\alpha=1$. Bir dönme hiçbir alanı değiştirmez ve yansıtmaz.

(c) Aynı olan iki sütun doğrusal bağımlıdır. Sütunların gerdiği paralelkenar ya da paralelyüz yassıdır ve alanı ya da hacmi sıfırdır. Aynı sonuç, $\det\mathbf{A}^{\top}=\det\mathbf{A}$ ile sütunlara aktarılan (v) kuralından da çıkar: Aynı olan iki sütunun yeri değiştirilirse matris aynı kalır, ama determinantın işaret değiştirmesi gerekirdi. Demek ki $\det\mathbf{A}=-\det\mathbf{A}$, dolayısıyla $\det\mathbf{A}=0$.
:::
:::
