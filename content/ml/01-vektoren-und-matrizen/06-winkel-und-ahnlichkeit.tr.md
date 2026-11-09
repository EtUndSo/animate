---
title: Açılar ve benzerlik
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
knoten: Temeller 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15210600
summary: İki vektör farklı uzunlukta olsalar bile benzer yönleri gösterebilir.
tags: açısı, ortogonal, kosinüs benzerliği
lang: tr
---

<span class="anker" id="stufe-5"></span>

:::zweck
İki vektör farklı uzunlukta olsalar bile benzer yönleri gösterebilir. Bu kesim aralarındaki açıyı ölçüyor. Temelde bir eşitsizlik vardır; bu eşitsizlik ayrıca bir örüntü karşılaştırmasının ne zaman en güçlü tepkiyi verdiğini de tam olarak söyler.
:::

### Cauchy-Schwarz eşitsizliği

<span class="anker" id="stufe-5-1"></span>

Uzunlukları belli olan iki vektörün iç çarpımı ne kadar büyük olabilir? Bir deneme: $\mathbf{u}=(1,\,2,\,2)^{\top}$ vektörünün uzunluğu $3$, $\mathbf{v}=(2,\,0,\,1)^{\top}$ vektörününki $\sqrt5\approx2{,}24$. İç çarpımları $2+0+2=4$ olur; bu, uzunlukların çarpımı olan $3\cdot2{,}24\approx6{,}71$ değerinden belirgin biçimde azdır. Bunun yerine aynı yönde ve uzunluğu $6$ olan $\mathbf{v}=2\mathbf{u}$ vektörü alınırsa $\mathbf{u}^{\top}(2\mathbf{u})=2\cdot9=18=3\cdot6$ olur: tam olarak uzunlukların çarpımı. Bundan fazlası olmaz.

:::satz Teorem 5.1 (Cauchy-Schwarz eşitsizliği)
<span class="anker" id="satz-5-1"></span>

Bütün $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ için şu geçerlidir:

<span class="anker" id="gl-5-1"></span>
$$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert . \tag{5.1}$$

Eşitlik ancak ve ancak iki vektörden biri ötekinin bir katıysa geçerlidir.
:::

:::beweis Cauchy-Schwarz eşitsizliği
$\mathbf{v}=\mathbf{0}$ ise iki taraf da sıfırdır. Aksi hâlde herhangi bir $t$ sayısı için $\mathbf{u}-t\,\mathbf{v}$ vektörü ele alınır. Bu vektörün uzunluğunun karesi hiçbir zaman negatif değildir ve iç çarpımın hesap kurallarına göre şu olur:

$$0\le\lVert\mathbf{u}-t\,\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2t\,\mathbf{u}^{\top}\mathbf{v}+t^2\lVert\mathbf{v}\rVert^2 .$$

Bu her $t$ için geçerlidir, dolayısıyla sağ tarafın $t$ değişkenine göre bir parabol olarak en küçük olduğu $t=\mathbf{u}^{\top}\mathbf{v}/\lVert\mathbf{v}\rVert^2$ noktası için de. Yerine konursa:

$$0\le\lVert\mathbf{u}\rVert^2-2\,\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}+\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}=\lVert\mathbf{u}\rVert^2-\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}.$$

$\lVert\mathbf{v}\rVert^2>0$ ile çarpılınca bu, $(\mathbf{u}^{\top}\mathbf{v})^2\le\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$ demektir; bunun karekökü [(5.1)](#gl-5-1) eşitsizliğidir.

Eşitlik ancak ve ancak bu $t$ için $\lVert\mathbf{u}-t\,\mathbf{v}\rVert=0$, yani $\mathbf{u}=t\,\mathbf{v}$ ise geçerlidir. Tersine, $\mathbf{u}=c\,\mathbf{v}$ için gerçekten $|\mathbf{u}^{\top}\mathbf{v}|=|c|\,\lVert\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$ olur.
:::

::::beispiel [Sayısal örnek]
$\mathbf{u}=(1,\,2,\,2)^{\top}$ ve $\mathbf{v}=(2,\,0,\,1)^{\top}$ için $|\mathbf{u}^{\top}\mathbf{v}|=4\le3\cdot\sqrt5\approx6{,}71$ olur. Burada eşitlik yoktur, çünkü $\mathbf{v}$ vektörü $\mathbf{u}$ vektörünün bir katı değildir.
::::

Bu eşitsizlikle, daha önce yalnızca sezgisel olarak gerekçelendirilen şey (alt kesim [3.4](normen-die-groe-eines-vektors.html#stufe-3-4)) sonradan kanıtlanabilir: Öklid normunun üçgen eşitsizliği. Şu geçerlidir:

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2\le\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2=\bigl(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert\bigr)^2 ,$$

ve bunun karekökü (N3) eşitsizliğidir.

⁠**Kısacası:** İç çarpımın mutlak değeri en fazla uzunlukların çarpımı kadardır ve ancak ve ancak vektörler orijinden geçen bir doğru üzerindeyse bu çarpıma eşittir.

:::hintergrund İç çarpım örüntüleri neden tanır: kesin ifade
Örüntü karşılaştırması daha önce (alt kesim [2.4](das-skalarprodukt.html#stufe-2-4)) sezgisel bir resimdi: Sinyal örüntüyü izliyorsa $\mathbf{w}^{\top}\mathbf{x}$ iç çarpımı büyüktür. Cauchy-Schwarz eşitsizliği bundan kesin bir ifade çıkarır. Yalnızca aynı $\lVert\mathbf{x}\rVert$ uzunluğundaki sinyaller karşılaştırılırsa $\mathbf{w}^{\top}\mathbf{x}$ her zaman $-\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$ ile $+\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$ arasında kalır. En büyük değere tam olarak örüntünün pozitif bir katı olan sinyal ulaşır, en küçük değere negatif katı. Yani aynı enerjiye sahip bütün sinyaller arasında karşılaştırma en güçlü tepkiyi örüntünün kendisinde verir.

⁠**Sayısal örnek:** İşaret değiştiren örüntü $\mathbf{w}=(1,-1,1,-1)^{\top}$ vektörünün uzunluğu $2$ olur. Uzunluğu $2$ olan bütün sinyaller arasında $\mathbf{x}=\mathbf{w}$ en büyük değeri, yani $4=2\cdot2$ değerini verir; $(2,0,0,0)^{\top}$ sinyali yalnızca $2$ verir, $\mathbf{x}=-\mathbf{w}$ ise en küçük değeri, yani $-4$ değerini verir.

İletişim tekniğinde bu, korelasyon alıcısının ve uyumlu süzgecin (*matched filter*) temelidir. Böyle bir süzgecin dürtü yanıtı, gönderilen sinyalin zamanda ters çevrilmiş hâlidir; bu sayede örnekleme anında alınan sinyal ile gönderilen sinyalin iç çarpımını tam olarak hesaplar. Bu süzgecin sinyal-gürültü oranını mümkün olan en büyük değere çıkardığı da tam bu eşitsizlikle kanıtlanır.
:::

### İki vektör arasındaki açı

<span class="anker" id="stufe-5-2"></span>

Orijinden çıkan iki ok bir açı oluşturur. Bu açı, okların uzunluğundan bağımsız olarak yönlerinin ne kadar benzer olduğunu söyler. Düzlemde bu açı iletkiyle ölçülebilir. Çok bileşenli vektörler için bir formül gerekir; bu formülü de iç çarpım verir.

:::herleitung Düzlemde iç çarpım
$\mathbf{u}$ ve $\mathbf{v}$ okları ile bunların $\mathbf{u}-\mathbf{v}$ bağlantı oku bir üçgen oluşturur. $\mathbf{u}$ ile $\mathbf{v}$ arasındaki açı $\varphi$ ise okul geometrisinden bilinen kosinüs teoremi şunu söyler:

$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

[(4.1)](abstande-und-einheiten.html#gl-4-1) uyarınca aynı sol taraf $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}$ ifadesine eşittir. İki satır karşılaştırılınca şu kalır:

$$\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

Demek ki düzlemde ve uzayda iç çarpım, uzunlukların çarpımı çarpı aradaki açının kosinüsüdür.
:::

Daha yüksek boyutlarda iletki yoktur. Bu yüzden türetme tersine çevrilir ve formül tanım olarak kullanılır.

:::definition Tanım 5.2 (Açı)
<span class="anker" id="satz-5-2"></span>

İkisi de $\mathbf{0}$ vektöründen farklı olan $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ için $\mathbf{u}$ ile $\mathbf{v}$ arasındaki $\varphi$ __açısı__, şu eşitliği sağlayan $\varphi\in[0^\circ,180^\circ]$ sayısıdır:

<span class="anker" id="gl-5-2"></span>
$$\cos\varphi=\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert} . \tag{5.2}$$
:::

Bu tanım ancak, sağ taraf Cauchy-Schwarz eşitsizliğine göre her zaman $-1$ ile $1$ arasında kaldığı için mümkündür. Böyle her sayıya $0^\circ$ ile $180^\circ$ arasında tam olarak bir açı karşılık gelir. İç çarpımın işaretinden açının dar ($\mathbf{u}^{\top}\mathbf{v}>0$), dik ($\mathbf{u}^{\top}\mathbf{v}=0$) ya da geniş ($\mathbf{u}^{\top}\mathbf{v}<0$) olduğu görülür.

::::beispiel [Sayısal örnek]
$(1,\,0)^{\top}$ ve $(1,\,1)^{\top}$ için $\cos\varphi=1/\sqrt2$, yani $\varphi=45^\circ$ olur. $(1,\,0,\,1)^{\top}$ ve $(1,\,1,\,0)^{\top}$ için $\cos\varphi=\tfrac12$, yani $\varphi=60^\circ$ olur (Şekil [22](#abb-22)). $\mathbf{u}=(1,\,2,\,2)^{\top}$ ve $\mathbf{v}=(2,\,0,\,1)^{\top}$ için $\cos\varphi=4/(3\sqrt5)\approx0{,}596$, yani $\varphi\approx53{,}4^\circ$ olur.

:::abbildung ml/k1rwinkel 22
$(1,\,0,\,1)^{\top}$ ile $(1,\,1,\,0)^{\top}$ arasındaki açı: kesrin payında iç çarpım, paydasında iki uzunluk.
:::
::::

⁠**Kısacası:** İki vektör arasındaki açının kosinüsü, iç çarpımlarının uzunluklarının çarpımına bölümüdür.

### Ortogonal vektörler

<span class="anker" id="stufe-5-3"></span>

İki vektörün iç çarpımı sıfırsa hiçbiri ötekinin yönüne bir katkı yapmaz. Düzlemde oklar bu durumda birbirine diktir. Bu durum o kadar önemlidir ki kendine ait bir adı vardır.

:::definition Tanım 5.3 (Ortogonal)
<span class="anker" id="satz-5-3"></span>

$\mathbf{u}^{\top}\mathbf{v}=0$ ise iki $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ vektörüne __ortogonal__ denir.
:::

İki vektör de $\mathbf{0}$ vektöründen farklıysa aralarındaki açı [(5.2)](#gl-5-2) uyarınca tam olarak $90^\circ$ olur. Sıfır vektörü her vektöre ortogonaldir.

:::satz Teorem 5.4 (Pisagor teoremi)
<span class="anker" id="satz-5-4"></span>

$\mathbf{u}$ ve $\mathbf{v}$ ortogonalse $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2$ olur.
:::

Bu, $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$ eşitliğinden hemen çıkar, çünkü ortadaki terim sıfırdır.

::::beispiel [Sayısal örnek 1]
$(1,\,2,\,2)^{\top}$ ve $(2,\,0,\,-1)^{\top}$ ortogonaldir, çünkü $2+0-2=0$. Toplamları olan $(3,\,2,\,1)^{\top}$ vektörünün uzunluğunun karesi $14=9+5$ olur.
::::

::::beispiel [Sayısal örnek 2] birbirini bozmayan iki örüntü
Sabit örüntü $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ ile işaret değiştiren örüntü $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$ (alt kesim [2.4](das-skalarprodukt.html#stufe-2-4)) ortogonaldir, $\mathbf 1^{\top}\mathbf{w}=0$. $2$ kez sabit örüntüden ve $1$ kez işaret değiştiren örüntüden oluşan bir sinyal $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}=(3,\,1,\,3,\,1)^{\top}$ olur. Sabit örüntüyle karşılaştırma $\mathbf 1^{\top}\mathbf{x}=8=2\cdot4$, işaret değiştiren örüntüyle karşılaştırma $\mathbf{w}^{\top}\mathbf{x}=4=1\cdot4$ verir (Şekil [23](#abb-23)). Her karşılaştırma tam olarak kendi payını, $\lVert\mathbf 1\rVert^2=\lVert\mathbf{w}\rVert^2=4$ ile çarpılmış olarak bulur; öteki pay onu bozmaz.

:::abbildung ml/k1rortho 23
İki örüntü ortogonaldir (üstte). $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}$ sinyalinin her örüntüyle karşılaştırılması, o örüntünün payının $4$ katını verir.
:::
::::

⁠**Kısacası:** Ortogonal, iç çarpımın sıfır olması demektir; ortogonal oklar birbirine diktir ve onlar için Pisagor teoremi geçerlidir.

:::hintergrund Ortogonal örüntüler neden birbirini bozmaz ve bunun Fourier katsayılarıyla ilgisi ne?
Bir sinyal iki ortogonal örüntünün $\mathbf{x}=\alpha\,\mathbf 1+\beta\,\mathbf{w}$ doğrusal bileşimiyse hesap kurallarına göre şu olur:

$$\mathbf 1^{\top}\mathbf{x}=\alpha\,\mathbf 1^{\top}\mathbf 1+\beta\,\mathbf 1^{\top}\mathbf{w}=\alpha\,\lVert\mathbf 1\rVert^2+0 ,\qquad\text{yani}\qquad \alpha=\frac{\mathbf 1^{\top}\mathbf{x}}{\lVert\mathbf 1\rVert^2} .$$

Yani bir örüntüyle karşılaştırma yalnızca o örüntünün kendi payını ölçer, çünkü öteki örüntünün katkısı $\mathbf 1^{\top}\mathbf{w}=0$ çarpanıyla kaybolur. Örüntüler ortogonal olmasaydı her karşılaştırma öteki payın bir parçasını da sayardı.

Bir Fourier serisinin katsayıları da tam olarak böyle kurulmuştur. Periyodu $T$ olan bir $s(t)$ sinyali ve $\omega_0=2\pi/T$ için şu geçerlidir:

$$a_k=\frac{2}{T}\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t=\frac{\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t}{\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t}\qquad(k\ge1),$$

çünkü $\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t=T/2$. İki fonksiyonun çarpımı üzerinden alınan integral iç çarpım rolünü oynar ve farklı frekanslardaki kosinüs ve sinüs fonksiyonları bu anlamda ortogonaldir: Çarpımlarının bir periyot üzerinden integrali sıfırdır. Bu yüzden her Fourier katsayısı, ötekiler bilinmeden kendi başına hesaplanabilir.
:::

### Kosinüs benzerliği

<span class="anker" id="stufe-5-4"></span>

Bazen bir vektörün uzunluğu ikinci plandadır. Bir metin, $j$ bileşeni sabit bir sözcük listesindeki $j$ sözcüğünün metinde kaç kez geçtiğini sayan bir vektörle betimlenebilir. Bir futbol maçı hakkındaki ayrıntılı bir haber “gol” ve “top” sözcüklerini aynı maç hakkındaki kısa bir duyurudan daha sık içerir, ama aynı oranda. İki vektörün uzunlukları farklıdır, ama aynı yönü gösterirler. İçerik için önemli olan yöndür.

:::definition Tanım 5.5 (Kosinüs benzerliği)
<span class="anker" id="satz-5-5"></span>

$\mathbf{u},\mathbf{v}\ne\mathbf{0}$ vektörlerinin __kosinüs benzerliği__ şu sayıdır:

<span class="anker" id="gl-5-3"></span>
$$\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert}\in[-1,\,1] , \tag{5.3}$$

yani aralarındaki açının kosinüsü.
:::

Vektörler aynı yönü gösteriyorsa kosinüs benzerliği $1$, ortogonalseler $0$, ters yönleri gösteriyorsa $-1$ olur. Vektörlerden biri pozitif bir sayıyla çarpılırsa kosinüs benzerliği değişmez, çünkü sayı sadeleşir.

::::beispiel [Sayısal örnek]
Üç metin ve bu metinlerde “gol”, “top” ve “seçim” sözcüklerinin sayıları:

$$\mathbf{x}_1=(3,\,2,\,0)^{\top},\qquad \mathbf{x}_2=(6,\,4,\,0)^{\top},\qquad \mathbf{x}_3=(0,\,1,\,3)^{\top} .$$

Metin 2 aynı maç hakkında iki kat uzun bir haberdir, Metin 3 ise ağırlıklı olarak bir seçimle ilgilidir. Metin 1 ile Metin 2'nin kosinüs benzerliği $1$, Metin 1 ile Metin 3'ünkü $2/\sqrt{130}\approx0{,}175$ olur (Şekil [24](#abb-24)). Aynı biçimde Metin 2 ile Metin 3'ünkü $4/(\sqrt{52}\,\sqrt{10})=4/\sqrt{520}\approx0{,}175$ olur.

:::abbildung ml/k1rkosinus 24
Sözcük sayımlarının iki kosinüs benzerliği: Her birinde kesrin payında bir iç çarpım, paydasında iki uzunluk vardır.
:::

Uzaklıklar ise $\lVert\mathbf{x}_1-\mathbf{x}_2\rVert=\sqrt{13}\approx3{,}61$, $\lVert\mathbf{x}_1-\mathbf{x}_3\rVert=\sqrt{19}\approx4{,}36$ ve $\lVert\mathbf{x}_2-\mathbf{x}_3\rVert=\sqrt{54}\approx7{,}35$ olur. Uzaklığa göre Metin 1'in Metin 3'e uzaklığı, Metin 2'ye uzaklığından pek fazla değildir; oysa Metin 2 tam olarak aynı konuyu işler. Kosinüs benzerliği bunu hemen fark eder: Metin 2 ile benzerlik $1$ olur, Metin 3 ile açı ise yaklaşık $79{,}9^\circ$, yani neredeyse diktir.
::::

⁠**Kısacası:** Kosinüs benzerliği iki vektörün yalnızca yönlerini karşılaştırır, uzunluklarını göz ardı eder.

:::hintergrund Kosinüs benzerliği korelasyonla aynı şey değildir
Bileşen sayıları aynı olan iki vektör önce merkezlenirse (alt kesim [4.3](abstande-und-einheiten.html#stufe-4-3)), aralarındaki açının kosinüsü bileşenlerin birlikte kendi ortalamalarının üstünde ve altında olup olmadığını ölçer. Bu sayıya korelasyon katsayısı denir. Merkezleme yapılmazsa çoğu zaman bambaşka bir şey çıkar. Örnek: $\mathbf{a}=(1,2,3)^{\top}$, $\mathbf{b}=(3,4,5)^{\top}$ ve $\mathbf{c}=(3,2,1)^{\top}$. $\mathbf{a}$ ile $\mathbf{b}$ vektörlerinin kosinüs benzerliği yaklaşık $0{,}983$, $\mathbf{a}$ ile $\mathbf{c}$ vektörlerininki de hatırı sayılır bir değer olan $0{,}714$; ikisi de açıkça pozitiftir. Merkezlenmiş hâlleri $\tilde{\mathbf{a}}=(-1,0,1)^{\top}$, $\tilde{\mathbf{b}}=(-1,0,1)^{\top}$ ve $\tilde{\mathbf{c}}=(1,0,-1)^{\top}$ olur: $\mathbf{a}$ ile $\mathbf{b}$ vektörlerinin korelasyon katsayısı $1$, $\mathbf{a}$ ile $\mathbf{c}$ vektörlerininki ise $-1$ olur, çünkü $\mathbf{c}$ tam olarak $\mathbf{a}$ vektörünün arttığı yerde azalır. Merkezlenmemiş kosinüs benzerliği yalnızca bütün sayılar pozitif olduğu ve bu yüzden üç vektör de aşağı yukarı aynı yönü gösterdiği için pozitif çıkmıştı.
:::

### Gölge uzunluğu olarak iç çarpım

<span class="anker" id="stufe-5-5"></span>

Normlanmış bir vektörle iç çarpımın basit bir geometrik anlamı vardır. Orijinden geçen ve normlanmış $\mathbf{u}$ vektörünün yönünde uzanan bir doğru düşünün ve bu doğruya ışığın dik olarak düştüğünü varsayın. $\mathbf{x}$ oku bu durumda doğru üzerine bir gölge düşürür (Şekil [25](#abb-25)). Bu gölge ne kadar uzundur?

:::abbildung ml/k1schatten 25
$\mathbf{x}=(3,1)^{\top}$ okunun, normlanmış $\mathbf{u}=(0{,}6;\,0{,}8)^{\top}$ vektörünün yönündeki doğru üzerine düşen gölgesi. Işık doğruya dik olarak düşer (kesikli). Gölgenin (açık mavi) uzunluğu $\mathbf{u}^{\top}\mathbf{x}=\lVert\mathbf{x}\rVert\cos\varphi=2{,}6$ olur ve gölge $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}=(1{,}56;\,2{,}08)^{\top}$ noktasında biter.
:::

:::satz Teorem 5.6 (Gölge uzunluğu)
<span class="anker" id="satz-5-6"></span>

$\mathbf{u}\in\mathbb{R}^d$ normlanmış olsun, yani $\lVert\mathbf{u}\rVert=1$. Bu durumda $\mathbf{x}$ vektörünün $\mathbf{u}$ yönündeki doğru üzerine düşen gölgesinin işaretli uzunluğu $\mathbf{u}^{\top}\mathbf{x}$ olur: Gölge $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ noktasında biter ve $\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ bağlantı oku $\mathbf{u}$ vektörüne ortogonaldir.
:::

:::beweis Gölge uzunluğu
$\mathbf{u}^{\top}\mathbf{u}=\lVert\mathbf{u}\rVert^2=1$ olduğundan $\mathbf{u}^{\top}\bigl(\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}\bigr)=\mathbf{u}^{\top}\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}^{\top}\mathbf{u}=0$ olur. Yani bağlantı oku doğruya diktir; bu da tam olarak ışığın geldiği yöndür. $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ gölge noktası orijinden $|\mathbf{u}^{\top}\mathbf{x}|$ uzaklıktadır, çünkü $\mathbf{u}$ vektörünün uzunluğu $1$. Bu nokta $\mathbf{u}^{\top}\mathbf{x}>0$ ise $\mathbf{u}$ yönünde, $\mathbf{u}^{\top}\mathbf{x}<0$ ise ters yönde bulunur. $\mathbf{x}$, gölge ve bağlantı okundan oluşan dik üçgende $\mathbf{x}$ hipotenüstür; bu yüzden gölge uzunluğu $\lVert\mathbf{x}\rVert\cos\varphi$ olarak da yazılabilir.
:::

$\mathbf{u}$ normlanmış değilse, $\mathbf{u}^{\top}\mathbf{x}$ iç çarpımı $\mathbf{x}$ vektörünün $\mathbf{u}$ yönündeki gölge uzunluğunun $\lVert\mathbf{u}\rVert$ katıdır.

::::beispiel [Sayısal örnek]
$\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$ normlanmıştır, çünkü $0{,}36+0{,}64=1$. $\mathbf{x}=(3,\,1)^{\top}$ için gölge uzunluğu $\mathbf{u}^{\top}\mathbf{x}=2{,}6$ (Şekil [26](#abb-26)), gölge noktası $2{,}6\,\mathbf{u}=(1{,}56;\ 2{,}08)^{\top}$ ve bağlantı oku $\mathbf{x}-2{,}6\,\mathbf{u}=(1{,}44;\ -1{,}08)^{\top}$ olur. Bağlantı oku $\mathbf{u}$ vektörüne ortogonaldir: $0{,}6\cdot1{,}44-0{,}8\cdot1{,}08=0$. $\lVert\mathbf{x}\rVert=\sqrt{10}\approx3{,}162$ ile $\cos\varphi=2{,}6/3{,}162\approx0{,}822$, yani $\varphi\approx34{,}7^\circ$ bulunur.

:::abbildung ml/k1rschatten 26
Normlanmış $\mathbf{u}$ vektörünün yönünde $\mathbf{x}$ vektörünün gölge uzunluğu, iç çarpım olarak.
:::
::::

Ağırlıklı bir toplam için bu şu anlama gelir: Ağırlıklar normlanmışsa $\mathbf{x}$ örneğinin $\mathbf{w}$ yönünde ne kadar uzandığını $\mathbf{w}^{\top}\mathbf{x}$ verir. Aynı $\mathbf{w}^{\top}\mathbf{x}$ değerini veren bütün noktalar aynı gölgeyi düşürür. Bu yüzden düzlemde $\mathbf{w}$ vektörüne dik bir doğru üzerinde, uzayda $\mathbf{w}$ vektörüne dik bir düzlem üzerinde bulunurlar.

⁠**Kısacası:** Normlanmış bir $\mathbf{u}$ vektörü için $\mathbf{x}$ vektörünün $\mathbf{u}$ yönündeki doğru üzerine düşürdüğü gölgenin uzunluğu $\mathbf{u}^{\top}\mathbf{x}$ olur.

:::aufgabe Alıştırma 12 ★ Açı ve ortogonallik
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

$(2,\,1,\,2)^{\top}$ ile $(1,\,0,\,1)^{\top}$ arasındaki açıyı hesaplayın ve Cauchy-Schwarz eşitsizliğini doğrulayın.

</li>

<li>

$(1,\,1,\,0)^{\top}$ ve $(1,\,-1,\,3)^{\top}$ ortogonal midir?

</li>

<li>

$\mathbf{u}=(1,\,2)^{\top}$ vektörüne ortogonal olan bir $\mathbf{v}\ne\mathbf{0}$ vektörü bulun ve $\mathbf{u}$ ile $\mathbf{v}$ için Pisagor teoremini doğrulayın.

</li>

</ol>

:::loesung
(a) İç çarpım $2+0+2=4$, uzunluklar $3$ ve $\sqrt2$ olur. Dolayısıyla $\cos\varphi=4/(3\sqrt2)\approx0{,}943$ ve $\varphi\approx19{,}5^\circ$. Cauchy-Schwarz: $4\le3\sqrt2\approx4{,}243$.

(b) $1\cdot1+1\cdot(-1)+0\cdot3=0$: Evet, ortogonaldirler.

(c) $\mathbf{v}=(v_1,v_2)^{\top}$ için koşul $v_1+2v_2=0$ olur. Bir çözüm $\mathbf{v}=(2,\,-1)^{\top}$ olur; onun sıfırdan farklı her katı da bir çözümdür. Pisagor sağlaması: $\mathbf{u}+\mathbf{v}=(3,\,1)^{\top}$ vektörünün uzunluğunun karesi $10$ olur ve $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2=5+5=10$.
:::
:::

:::aufgabe Alıştırma 13 ★★ Hangi metin benzer?
<span class="anker" id="aufg-13"></span>

Dört metin; yine “gol”, “top” ve “seçim” sözcükleri sayılmıştır: $\mathbf{x}_a=(2,\,0,\,1)^{\top}$, $\mathbf{x}_b=(0,\,3,\,0)^{\top}$, $\mathbf{x}_c=(4,\,0,\,2)^{\top}$ ve $\mathbf{x}_d=(1,\,1,\,1)^{\top}$.

<ol class="al">

<li>

Metin $a$ ile öteki üç metin arasındaki kosinüs benzerliğini ve Öklid uzaklığını hesaplayın.

</li>

<li>

Uzaklığa göre ve kosinüs benzerliğine göre Metin $a$'ya en çok hangi metin benzer? Farkı açıklayın.

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{x}_a\rVert=\sqrt5$, $\lVert\mathbf{x}_b\rVert=3$, $\lVert\mathbf{x}_c\rVert=\sqrt{20}$ ve $\lVert\mathbf{x}_d\rVert=\sqrt3$ ile:

<ul>

<li>

Metin $b$ ile: $\mathbf{x}_a^{\top}\mathbf{x}_b=0$, kosinüs benzerliği $0$; uzaklık $\sqrt{4+9+1}=\sqrt{14}\approx3{,}74$;

</li>

<li>

Metin $c$ ile: $\mathbf{x}_a^{\top}\mathbf{x}_c=8+0+2=10$, kosinüs benzerliği $10/(\sqrt5\sqrt{20})=1$; uzaklık $\sqrt{4+0+1}=\sqrt5\approx2{,}24$;

</li>

<li>

Metin $d$ ile: $\mathbf{x}_a^{\top}\mathbf{x}_d=3$, kosinüs benzerliği $3/(\sqrt5\sqrt3)\approx0{,}775$; uzaklık $\sqrt{1+1+0}=\sqrt2\approx1{,}41$.

</li>

</ul>

(b) Uzaklığa göre en yakın metin Metin $d$, kosinüs benzerliğine göre Metin $c$ olur. Metin $c$ için $\mathbf{x}_c=2\mathbf{x}_a$ olur: Sözcük dağılımı aynıdır, metin yalnızca iki kat uzundur; yani içerik bakımından konu aynıdır. Uzaklık daha büyük uzunluğu cezalandırır, kosinüs benzerliği ise yalnızca yönü görür. Metin $d$ kısadır ve bu yüzden ortak bir konusu olmasa bile her kısa metne yakındır. İçerikleri karşılaştırmak için burada uygun ölçü kosinüs benzerliğidir; Metin $b$ ile Metin $a$ arasında ise hiçbir ortaklık yoktur.
:::
:::

:::aufgabe Alıştırma 14 ★★★ Normlanmış vektörlerin uzaklığı ve açısı
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Aralarındaki açı $\varphi$ olan normlanmış $\mathbf{u},\mathbf{v}$ vektörleri için $\lVert\mathbf{u}-\mathbf{v}\rVert^2=2-2\cos\varphi$ olduğunu gösterin. Bütün örnekler önceden normlanırsa, bundan “uzaklığa göre benzer” ve “kosinüs benzerliğine göre benzer” sıralamaları için ne çıkar?

</li>

<li>

Formülü $\mathbf{x}_1$ ve $\mathbf{x}_3$ metinlerinin normlanmış hâlleri üzerinde doğrulayın (alt kesim [5.4](#stufe-5-4)).

</li>

<li>

$\lVert\mathbf{u}+\mathbf{v}\rVert=\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ eşitliğinin ancak ve ancak $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$ ise geçerli olduğunu gösterin. Bu ne zaman olur?

</li>

</ol>

:::loesung
(a) [(4.1)](abstande-und-einheiten.html#gl-4-1) uyarınca $\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}=1+1-2\cos\varphi$ olur, çünkü normlanmış vektörler için $\mathbf{u}^{\top}\mathbf{v}=\cos\varphi$. Demek ki uzaklık, kosinüs benzerliğinin azalan bir fonksiyonudur: Kosinüs ne kadar büyükse uzaklık o kadar küçüktür. Bu yüzden bütün örnekler önceden normlanırsa uzaklık ve kosinüs benzerliği örnekleri tam olarak aynı biçimde sıralar.

(b) Normlanmış metinler $\mathbf{x}_1/\sqrt{13}$ ve $\mathbf{x}_3/\sqrt{10}$ olur; aralarındaki kosinüs $0{,}1754$. Formül $2-2\cdot0{,}1754\approx1{,}649$ verir. Doğrudan: $\mathbf{x}_1/\sqrt{13}-\mathbf{x}_3/\sqrt{10}\approx(0{,}832;\ 0{,}238;\ -0{,}949)^{\top}$, uzunluğunun karesi $0{,}692+0{,}057+0{,}900\approx1{,}649$.

(c) İki taraf da negatif değildir, dolayısıyla kareler karşılaştırılabilir. $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$ ve $(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert)^2=\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2$ olur. İkisi ancak ve ancak $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$ ise eşittir. Cauchy-Schwarz eşitsizliğine ve onun eşitlik durumuna göre bu, ancak ve ancak vektörlerden biri ötekinin bir katıysa olur, hem de $\ge0$ bir çarpanla, çünkü aksi hâlde iç çarpım negatif olurdu. Sezgisel olarak: Üçgen eşitsizliği yalnızca üçgen yassıysa ve iki ok aynı yönü gösteriyorsa eşitliğe dönüşür.
:::
:::
