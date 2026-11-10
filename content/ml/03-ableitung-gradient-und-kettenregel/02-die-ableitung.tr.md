---
title: Türev
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15230200
summary: Türev, tek değişkenli bir fonksiyonun girdisindeki küçük bir değişime ne kadar güçlü tepki verdiğini ölçer.
tags: kesen, fark bölümü, limiti, türevlenebilir, türevi, teğeti, köşe noktası, doğrusal yaklaşımı
lang: tr
---

<span class="anker" id="stufe-1"></span>

:::zweck
Türev, tek değişkenli bir fonksiyonun girdisindeki küçük bir değişime ne kadar güçlü tepki verdiğini ölçer. Bu kesim türevi eğimlerin limiti olarak tanıtıyor, onu eğriye en iyi yaslanan doğrunun eğimi olarak yorumluyor ve her seferinde limit almadan türev hesaplamayı sağlayan hesap kurallarını hazırlıyor. Sonda, eğimin kendisinin nasıl değiştiğini betimleyen ikinci türev yer alıyor.
:::

### Değişim hızı ve fark bölümü

<span class="anker" id="stufe-1-1"></span>

Bir $f$ fonksiyonu her $x$ sayısına bir $f(x)$ sayısı karşılık getirir. $x$ küçük bir $h$ parçası kadar büyütülürse genellikle değer de değişir, hem de $f(x+h)-f(x)$ kadar. Bunun çok mu az mı olduğunu ancak $h$ ile karşılaştırma gösterir: Değerdeki $0{,}1$'lik bir değişim, $x$ yalnızca $0{,}001$ arttıysa büyük, $x$, $100$ arttıysa küçüktür. Bu yüzden iki değişim birbirine bölünür.

Grafiğin resminde bu bir eğimdir. Grafiğin $(x,\,f(x))$ ve $(x+h,\,f(x+h))$ noktalarından bir doğru geçirilir. Bir eğrinin iki noktasından geçen böyle bir doğruya __kesen__ denir. Kesenin eğimi, iki nokta arasındaki yükseklik farkının yatay uzaklıklarına bölümüdür. Grafiğin iki nokta arasında ortalama olarak ne kadar dik yükseldiğini gösterir.

:::definition Tanım 1.1 (Fark bölümü)
<span class="anker" id="satz-1-1"></span>

Bir $f$ fonksiyonu, bir $x$ noktası ve bir $h\ne0$ sayısı için

<span class="anker" id="gl-1-1"></span>
$$\frac{f(x+h)-f(x)}{h} \tag{1.1}$$

ifadesine $f$ fonksiyonunun $x$ noktasında $h$ adım büyüklüğüne göre __fark bölümü__ denir. Bu, $(x,\,f(x))$ ve $(x+h,\,f(x+h))$ noktalarından geçen kesenin eğimidir.
:::

$h$ adım büyüklüğü negatif de olabilir; o zaman ikinci nokta $x$'in solunda kalır. $h=0$ için bölüm tanımlı değildir, çünkü sıfıra bölünemez.

::::beispiel [Sayısal örnek]
$f(x)=x^3$ ve $x=2$ olsun, yani $f(2)=8$. Üç adım büyüklüğü için şunlar bulunur:

$$\frac{3^3-8}{1}=19,\qquad \frac{2{,}5^3-8}{0{,}5}=\frac{15{,}625-8}{0{,}5}=15{,}25,\qquad \frac{2{,}1^3-8}{0{,}1}=\frac{9{,}261-8}{0{,}1}=12{,}61 .$$

İkinci nokta $(2,\,8)$ noktasına yaklaştıkça kesenler yatıklaşır (Şekil [1](#abb-1)). Herhangi bir $h$ için $(2+h)^3=8+12h+6h^2+h^3$ ile hesaplanır:

<span class="anker" id="gl-1-2"></span>
$$\frac{(2+h)^3-8}{h}=\frac{12h+6h^2+h^3}{h}=12+6h+h^2 . \tag{1.2}$$

$h=1$, $h=0{,}5$ ve $h=0{,}1$ için bu formül yine $19$, $15{,}25$ ve $12{,}61$ verir. $h=0{,}01$ için $12{,}0601$, $h=-0{,}1$ için $12-0{,}6+0{,}01=11{,}41$ verir.

:::abbildung ml/k3sekante 1
$f(x)=x^3$ grafiğinin $(2,\,8)$ noktasından geçen kesenleri; eğimleri $h=1$ için $19$ (kırmızı), $h=0{,}5$ için $15{,}25$ (turuncu). $h$ adım büyüklüğü küçüldükçe ikinci nokta yaklaşır, kesen yatıklaşır ve eğimi $12+6h+h^2$, teğetin (kesikli) $12$ eğimine yaklaşır.
:::
::::

⁠**Kısacası:** Fark bölümü, fonksiyon değerindeki değişimin girdideki değişime bölümüdür; grafiğin iki noktası arasındaki ortalama eğimdir.

### Türev

<span class="anker" id="stufe-1-2"></span>

Sayısal örnekte $|h|$ ne kadar küçükse kesen eğimleri $12$'ye o kadar yakındır, hem de iki taraftan: $h=0{,}1$ için $12{,}61$, $h=-0{,}1$ için $11{,}41$. $12$ değerinin kendisine hiçbir $h\ne0$ için ulaşmazlar, ama ona istenildiği kadar yaklaşırlar. Bu yüzden $12$ sayısına kesen eğimlerinin limiti denir. Genel olarak $h$'ye bağlı bir büyüklük, $h$ yeterince $0$'a yakın ve $0$'dan farklı olduğunda $c$'ye istenildiği kadar yakın oluyorsa, bu büyüklüğün $h\to0$ için __limiti__ $c$'dir. Burada pozitif ve negatif $h$ değerleri eşit ölçüde sayılır.

:::definition Tanım 1.2 (Türev)
<span class="anker" id="satz-1-2"></span>

Fark bölümünün $h\to0$ için bir limiti varsa $f$ fonksiyonuna $x$ noktasında __türevlenebilir__ denir. Bu limit

<span class="anker" id="gl-1-3"></span>
$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h} \tag{1.3}$$

$f$ fonksiyonunun $x$ noktasındaki __türevi__ olarak adlandırılır. $\frac{\mathrm{d} f}{\mathrm{d} x}(x)$ diye de yazılır. $(x,\,f(x))$ noktasından geçen ve eğimi $f'(x)$ olan doğruya grafiğin __teğeti__ denir.
:::

$f$ her noktada türevlenebilirse $f'$ yine bir fonksiyondur: Her $x$ değerine grafiğin o noktadaki eğimini karşılık getirir. Buna türev fonksiyonu ya da kısaca yine türev denir. $\frac{\mathrm{d} f}{\mathrm{d} x}$ yazılışı [(1.1)](#gl-1-1) bağıntısındaki bölümü hatırlatır, ama kendisi bir kesir değil, limitin simgesidir.

::::beispiel [Sayısal örnek 1]
[(1.2)](#gl-1-2) uyarınca $f(x)=x^3$ fonksiyonunun $2$ noktasındaki fark bölümü $12+6h+h^2$ olur. $h\to0$ için $6h$ ve $h^2$ istenildiği kadar küçülür, yani $f'(2)=12$ olur. Herhangi bir $x$ noktasında aynı hesap, $(x+h)^3=x^3+3x^2h+3xh^2+h^3$ ile $3x^2+3xh+h^2$ bölümünü ve dolayısıyla $f'(x)=3x^2$ sonucunu verir.
::::

Her fonksiyon her yerde türevlenebilir değildir. Bunun tipik bir istisnası __köşe noktası__ denen yerdir: grafiğin sıçramadan devam ettiği, ama sol tarafta sağ taraftakinden farklı bir eğime sahip olduğu bir nokta. Orada $h>0$ olan kesen eğimleri sağdaki eğime, $h<0$ olanlar soldaki eğime yaklaşır. İkisi farklı olduğundan ortak bir limit, dolayısıyla türev yoktur; hiçbir doğru iki tarafa birden yaslanmaz. En bilinen örnek, $0$ noktasındaki $|x|$ mutlak değer fonksiyonudur.

::::beispiel [Sayısal örnek 2]
$f(x)=|x|$ mutlak değer fonksiyonunun $0$ noktasında türevi yoktur. Fark bölümü $|h|/h$, yani her $h>0$ için $1$ ve her $h<0$ için $-1$ olur. Bu bölümün iki taraftan da yaklaştığı bir sayı yoktur. Grafiğin $0$'da bir köşe noktası vardır: Solda eğimi $-1$, sağda $+1$'dir. $|x|$ başka her noktada türevlenebilir; türevi $x>0$ için $1$, $x<0$ için $-1$ olur.
::::

⁠**Kısacası:** $f'(x)$ türevi kesen eğimlerinin limitidir, yani teğetin eğimidir; bir köşe noktasında türev yoktur.

### Doğrusal yaklaşım

<span class="anker" id="stufe-1-3"></span>

Teğet ne işe yarar? Düzgün bir grafiğe gittikçe güçlenen bir büyüteçle bakılırsa üzerinde gittikçe daha az eğrilik görülür. Güçlü bir büyüteç altında eğriden yalnızca düz bir parça kalır ve bu parça teğetin üzerindedir (Şekil [2](#abb-2)). Bu yüzden $x$ noktasının yakınında fonksiyonun yerine teğeti konabilir. Bir doğruyla hesap yapmak, fonksiyonun kendisiyle hesap yapmaktan çok daha kolaydır.

:::abbildung ml/k3lupe 2
Büyüteç: $f(x)=x^3$ grafiği (mavi) ve $2$ noktasındaki $8+12\,(x-2)$ teğeti (kırmızı kesikli), her biri bir öncekinden on kat dar olan üç pencerede. Son pencerede eğri ile teğet artık ayırt edilemez.
:::

:::satz Teorem 1.3 (Doğrusal yaklaşım)
<span class="anker" id="satz-1-3"></span>

$f$, $x$ noktasında türevlenebilirse şu eşitlik geçerlidir:

<span class="anker" id="gl-1-4"></span>
$$f(x+h)=f(x)+f'(x)\,h+r(h)\qquad\text{burada}\qquad \lim_{h\to0}\frac{r(h)}{h}=0 . \tag{1.4}$$

$f(x)+f'(x)\,h$ ifadesine $f$ fonksiyonunun $x$ noktasındaki __doğrusal yaklaşımı__ denir ve $r(h)$ onun hatasıdır.
:::

:::beweis Doğrusal yaklaşım
$r(h)=f(x+h)-f(x)-f'(x)\,h$ konur; o zaman soldaki eşitlik yapısı gereği sağlanır. $h\ne0$ için

$$\frac{r(h)}{h}=\frac{f(x+h)-f(x)}{h}-f'(x),$$

olur ve [(1.3)](#gl-1-3) uyarınca ilk terim $f'(x)$'e, fark da dolayısıyla $0$'a gider.
:::

$r(h)/h\to0$ koşulu, hatanın küçüldüğünden fazlasını söyler. $h$'nin kendisi de küçülür; belirleyici olan, hatanın $h$'den daha hızlı sıfıra gitmesidir. $h$ yarıya indirilirse $f'(x)\,h$ değişimi yarıya iner, hata ise yarısından belirgin biçimde daha küçük olur. Büyütecin tam anlamı budur.

[(1.4)](#gl-1-4) eşitliği türevin en anlaşılır yorumunu da verir. Girdideki küçük bir $h$ değişimi çıktıya yaklaşık $f'(x)\,h$ olarak ulaşır. Yani türev, fonksiyonun küçük değişimleri ilettiği *çarpan*dır, onun $x$ noktasındaki duyarlılığıdır. Büyük bir $|f'(x)|$, girdideki küçük değişimlerin bile değeri çok değiştirdiği anlamına gelir; negatif bir $f'(x)$ ise girdi arttığında değerin azaldığı anlamına gelir.

::::beispiel [Sayısal örnek]
$f(x)=x^3$ için $2$ noktasında ve $h=0{,}01$ ile doğrusal yaklaşım şunu verir:

$$f(2{,}01)\approx8+12\cdot0{,}01=8{,}12 .$$

Tam değer $f(2{,}01)=2{,}01^3=8{,}120601$ olur. Hata $r(0{,}01)=0{,}000601$, [(1.2)](#gl-1-2) ile ilgili hesaba göre genel olarak $r(h)=6h^2+h^3$ olur. $r(h)/h=6h+h^2$ bölümü $h=0{,}01$ için $0{,}0601$, $h=0{,}001$ için $0{,}006001$ olur: Teoremin gerektirdiği gibi sıfıra gider.
::::

⁠**Kısacası:** $x$ yakınında $f(x+h)\approx f(x)+f'(x)\,h$ olur; türev küçük değişimlerin iletildiği çarpandır ve hata $h$'den daha hızlı sıfıra gider.

:::hintergrund Neden en iyi doğru tam da teğettir
$(x,\,f(x))$ noktasından geçen her doğru, bir $m$ eğimiyle $f(x+h)\approx f(x)+m\,h$ yaklaşımını verir. Bu yaklaşımın hatası $f(x+h)-f(x)-m\,h$ olur. Hata $h$'ye bölünürse fark bölümü eksi $m$ elde edilir ve bu, $h\to0$ için $f'(x)-m$'ye gider. Bu limit yalnızca $m=f'(x)$ için sıfırdır. Başka her eğim için hata kalıcı olarak yaklaşık $|f'(x)-m|\cdot|h|$ büyüklüğünde kalır, yani ancak $h$'nin kendisi kadar hızlı küçülür. Dolayısıyla teğet, o noktadan geçen ve hatası $h$'den hızlı sıfıra giden tek doğrudur. Bu anlamda en iyi doğrusal yaklaşımdır ve türev tam olarak böyle de tanımlanabilir: $f(x+h)-f(x)-m\,h$ ifadesini $h$'den hızlı sıfıra götüren tek $m$ sayısı olarak. Tanımın bu biçiminin avantajı, çok girdili fonksiyonlara değişmeden aktarılabilmesidir; orada artık bir bölüm yoktur, çünkü bir vektöre bölünemez. Kesim [3](partielle-ableitungen-und-der-gradient.html#stufe-3) bundan yararlanır.
:::

### Türev kuralları

<span class="anker" id="stufe-1-4"></span>

Her türevi limit üzerinden hesaplamak zahmetlidir. Neyse ki temel aritmetik işlemlerden ve bilinen fonksiyonlardan oluşturulmuş hemen her formülün türevini almak için birkaç temel türev ve dört kural yeter. Tablo [1](#tab-1), bu bölümün kullandığı temel türevleri bir araya getiriyor.

<span class="anker" id="tab-1"></span>

**Tablo 1:** Temel türevler. Kuvvet kuralı her gerçel $n$ üssü için geçerlidir, tam sayı olmayan $n$ için yalnızca $x>0$ olduğunda. $\sin$ ve $\cos$ içindeki açılar radyan cinsinden ölçülür.

| Fonksiyon $f(x)$ | Türev $f'(x)$ | Örnek |
|---|---|---|
| $c$ (sabit) | $0$ | $f(x)=7$: $f'(x)=0$ |
| $x^n$ | $n\,x^{n-1}$ | $x^3\mapsto3x^2$, $\ \tfrac1x=x^{-1}\mapsto-\tfrac1{x^2}$, $\ \sqrt x=x^{1/2}\mapsto\tfrac1{2\sqrt x}$ |
| $\mathrm{e}^x$ | $\mathrm{e}^x$ | $0$ noktasında: eğim $1$ |
| $\ln x$ ($x>0$) | $\tfrac1x$ | $1$ noktasında: eğim $1$ |
| $\sin x$ | $\cos x$ | $0$ noktasında: eğim $1$ |
| $\cos x$ | $-\sin x$ | $0$ noktasında: eğim $0$ |

:::satz Teorem 1.4 (Türev kuralları)
<span class="anker" id="satz-1-4"></span>

$u$ ve $v$, $x$ noktasında türevlenebilirse ve $c$ bir sayıysa orada şunlar geçerlidir:

<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} (u+v)'&=u'+v' &&\text{(toplam kuralı)}\\ (c\,u)'&=c\,u' &&\text{(sabit çarpan kuralı)}\\ (u\,v)'&=u'\,v+u\,v' &&\text{(çarpım kuralı)}\\ \Bigl(\frac uv\Bigr)'&=\frac{u'\,v-u\,v'}{v^2}\quad v(x)\ne0\text{ ise} &&\text{(bölüm kuralı)} \end{aligned} \tag{1.5}$$
:::

İlk iki kural doğrudan tanımdan çıkar, çünkü toplamların ve katların fark bölümleri de aynı biçimde ayrışır. Çarpım kuralı daha az belirgindir. Bir resim onu açıklığa kavuşturur: $u\,v$, kenarları $u$ ve $v$ olan bir dikdörtgenin alanı olarak düşünülsün. Kenarlar $\Delta u$ ve $\Delta v$ kadar büyürse üç şerit eklenir: $u\,\Delta v$, $v\,\Delta u$ ve küçük köşe parçası $\Delta u\,\Delta v$. Küçük değişimlerde köşe parçası iki küçük büyüklüğün çarpımıdır ve iki şeritten daha hızlı sıfıra gider. Geriye $\Delta(uv)\approx v\,\Delta u+u\,\Delta v$ kalır ve $h$'ye bölmek çarpım kuralını verir.

:::beweis Çarpım kuralı ve kuvvet kuralı
$\Delta u=u(x+h)-u(x)$ ve $\Delta v=v(x+h)-v(x)$ ile tam olarak şu eşitlik geçerlidir:

$$u(x+h)\,v(x+h)-u(x)\,v(x)=v(x)\,\Delta u+u(x)\,\Delta v+\Delta u\,\Delta v .$$

$h$'ye bölündüğünde $\Delta u/h$, $u'(x)$'e ve $\Delta v/h$, $v'(x)$'e gider. Son terim $(\Delta u/h)\cdot\Delta v$ olur; ilk çarpanı $u'(x)$'e, ikincisi $0$'a gider, çünkü türevlenebilir bir fonksiyon küçük $h$ için çok az değişir. Dolayısıyla bölümün tamamı $u'(x)\,v(x)+u(x)\,v'(x)$'e gider.

Bir $n$ doğal sayısıyla kuvvet kuralı için $(x+h)^n$ açılır. Binom teoremine göre

$$(x+h)^n=x^n+n\,x^{n-1}h+(h^2,h^3,\dots,h^n\text{ içeren terimler}),$$

yani fark bölümü $n\,x^{n-1}$ artı hâlâ en az bir $h$ içeren terimlerdir. $h\to0$ için geriye $n\,x^{n-1}$ kalır. Bölüm kuralı, $u=(u/v)\cdot v$ eşitliğine uygulanan çarpım kuralından çıkar.
:::

::::beispiel [Sayısal örnek]
$f(x)=(x^2+1)(x-3)$ olsun ve $f'(2)$ aranıyor olsun. $u=x^2+1$, $u'=2x$, $v=x-3$, $v'=1$ ile çarpım kuralı şunu verir:

$$f'(x)=2x\,(x-3)+(x^2+1)\cdot1,\qquad f'(2)=4\cdot(-1)+5\cdot1=1 .$$

Sağlama: Çarpım açılınca $f(x)=x^3-3x^2+x-3$, dolayısıyla $f'(x)=3x^2-6x+1$ ve $f'(2)=12-12+1=1$ olur.
::::

⁠**Kısacası:** Tablodaki temel türevler ve toplam, kat, çarpım ve bölüm kurallarıyla, limit almadan bileşik formüllerin türevi alınır.

:::hintergrund Üstel fonksiyon neden kendi türevidir
Her $a>0$ tabanı için $a^{x+h}-a^x=a^x\,(a^h-1)$ olur. Bu yüzden $a^x$ fonksiyonunun fark bölümü, $a^x$ çarpı $a^x$ fonksiyonunun $0$ noktasındaki fark bölümüdür, yani $a^x\cdot\frac{a^h-1}{h}$: Her noktadaki eğim, fonksiyon değeri çarpı $0$ noktasındaki eğimdir. $a=2$ için $0$ noktasındaki bu eğim yaklaşık $0{,}693$, $a=3$ için yaklaşık $1{,}099$ olur. Arada bu eğimin $1$ olduğu tam olarak bir taban vardır ve bu taban Euler sayısı $\mathrm{e}\approx2{,}718$ olur. Bu taban için eğim her yerde fonksiyon değerine eşittir. $\ln x$ fonksiyonunun türevi buradan çıkar, çünkü logaritma üstel fonksiyonu geri alır: $y=\ln x$ ise $x=\mathrm{e}^y$ olur ve $y$'deki küçük bir değişim $x$'i, bu değişimin $\mathrm{e}^y=x$ katı kadar değiştirir. Tersine, $x$'teki küçük bir değişim de $y$'yi, bu değişimin $1/x$ katı kadar değiştirir.
:::

### İkinci türev ve ikinci dereceden yaklaşım

<span class="anker" id="stufe-1-5"></span>

Teğet grafiğin doğrultusunu verir, ama grafiğin ondan nasıl bükülerek uzaklaştığını vermez. Eğrinin teğetten yukarı mı aşağı mı ve ne kadar saptığı, eğimin kendisinin nasıl değiştiğine bağlıdır. Bu değişim yine bir türevle ölçülür, yani türevin türeviyle.

:::definition Tanım 1.5 (Yüksek mertebeden türevler)
<span class="anker" id="satz-1-5"></span>

$f'$ türev fonksiyonu $x$ noktasında türevlenebilirse $f''(x)=(f')'(x)$ ifadesine $f$ fonksiyonunun $x$ noktasındaki __ikinci türevi__ denir. Aynı şekilde $f'''=(f'')'$ üçüncü türevdir ve genel olarak $k$. türev için $f^{(k)}$ yazılır.
:::

$f''(x)>0$ ise eğim $x$ civarında artar; grafik teğetten yukarı doğru bükülerek uzaklaşır ve $x$'in yakınında teğetin üstünde kalır. $f''(x)<0$ ise aşağı doğru bükülür. Yani ikinci türev grafiğin __eğriliğini__ ölçer, daha doğrusu: eğiminin ne kadar hızlı değiştiğini.

İkinci türevle yaklaşım daha kesin olur. Teğetin yerine, $x$ noktasında $f$ ile aynı değere, aynı eğime ve aynı ikinci türeve sahip parabol konur. $p(h)=a+b\,h+c\,h^2$ parabolü için $p(0)=a$, $p'(0)=b$ ve $p''(0)=2c$ olur. Bu üç sayının $f(x)$, $f'(x)$ ve $f''(x)$ ile uyuşması için $a=f(x)$, $b=f'(x)$ ve $c=\tfrac12f''(x)$ olmalıdır. $\tfrac12$ çarpanı buradan gelir.

:::satz Teorem 1.6 (İkinci dereceden yaklaşım)
<span class="anker" id="satz-1-6"></span>

$f$, $x$ yakınında iki kez türevlenebilirse ve $f''$, $x$ noktasında sürekliyse şu eşitlik geçerlidir:

<span class="anker" id="gl-1-6"></span>
$$f(x+h)=f(x)+f'(x)\,h+\tfrac12f''(x)\,h^2+r_2(h)\qquad\text{burada}\qquad\lim_{h\to0}\frac{r_2(h)}{h^2}=0 . \tag{1.6}$$
:::

Burada sürekli, noktadaki küçük değişimlerde $f''$ fonksiyonunun sıçramadan, yalnızca az değişmesi demektir. İspat doğrusal yaklaşımdakine benzer biçimde, bir adım fazlasıyla yapılır; bu önermeye Taylor teoremi denir. $r_2(h)$ hatası artık $h^2$'den daha hızlı sıfıra gider, yani küçük $h$ için doğrusal yaklaşımın hatasından çok daha hızlı.

::::beispiel [Sayısal örnek]
$f(x)=x^3$ için $f'(x)=3x^2$, $f''(x)=6x$ ve $f'''(x)=6$ olur. $2$ noktasında $f''(2)=12>0$ olur: Grafik teğetten yukarı doğru bükülerek uzaklaşır (Şekil [2](#abb-2), sol panel). $h=0{,}01$ için ikinci dereceden yaklaşım şudur:

$$f(2{,}01)\approx8+12\cdot0{,}01+\tfrac12\cdot12\cdot0{,}01^2=8+0{,}12+0{,}0006=8{,}1206 .$$

Tam değer $8{,}120601$, hata ise yalnızca $0{,}000001=h^3$ olur. Şekil [3](#abb-3) üç terimin toplamını gösteriyor.

:::abbildung ml/k3rtaylor1 3
$f(x)=x^3$ fonksiyonunun $2$ noktasında $h=0{,}01$ için ikinci dereceden yaklaşımı; değer, eğim terimi ve eğrilik teriminin toplamı olarak.
:::
::::

⁠**Kısacası:** İkinci türev eğimin ne kadar hızlı değiştiğini, yani eğriliği ölçer; onunla yaklaşım $f(x+h)\approx f(x)+f'(x)\,h+\tfrac12f''(x)\,h^2$ olur.

:::hintergrund Yüksek mertebeden Taylor polinomları
Daha ileri gidilip üçüncü ve sonraki bütün türevler de eşleştirilebilir. Aşağıdaki

$$f(x)+f'(x)\,h+\frac{f''(x)}{2}\,h^2+\frac{f'''(x)}{6}\,h^3+\dots+\frac{f^{(k)}(x)}{k!}\,h^k$$

polinomuna $k$. mertebeden Taylor polinomu denir; burada $k!=1\cdot2\cdots k$ olur. $k!$ paydaları da $\tfrac12$ çarpanı gibi, $h^k$ ifadesinin $k$. türevinin $k!$ olmasından gelir. $f(x)=x^3$ için üçüncü mertebeden Taylor polinomu zaten tamdır: $8+12h+6h^2+h^3$ tam olarak $(2+h)^3$ eder. Çoğu fonksiyon için yaklaşım, $h$ yeterince küçük olduğu sürece her mertebede daha iyi olur. Bu bölüm için birinci ve ikinci mertebe yeterlidir.
:::

:::aufgabe Alıştırma 1 ★ Kesenler ve teğet
<span class="anker" id="aufg-1"></span>

$f(x)=x^2$ olsun.

<ol class="al">

<li>

$3$ noktasında $h=1$, $h=0{,}1$ ve $h=-0{,}1$ için fark bölümünü hesaplayın.

</li>

<li>

$3$ noktasındaki fark bölümünün $6+h$ olduğunu gösterin ve $f'(3)$ türevini belirleyin.

</li>

<li>

$3$ noktasındaki teğeti verin ve onunla $3{,}02^2$ için bir yaklaşık değer hesaplayın. Hata ne kadardır?

</li>

</ol>

:::loesung
(a) $f(3)=9$ olduğundan fark bölümleri şunlardır:

$$\frac{4^2-9}{1}=7,\qquad \frac{3{,}1^2-9}{0{,}1}=\frac{9{,}61-9}{0{,}1}=6{,}1,\qquad \frac{2{,}9^2-9}{-0{,}1}=\frac{8{,}41-9}{-0{,}1}=5{,}9 .$$

Sağa doğru çizilen kesen teğetten daha dik, sola doğru çizilen ise daha yatıktır, çünkü parabolün grafiği yukarı doğru bükülür.

(b) $(3+h)^2=9+6h+h^2$, dolayısıyla fark bölümü $\frac{6h+h^2}{h}=6+h$ olur. $h\to0$ için iki taraftan da $6$'ya gider; $(x^2)'=2x$ kuralına uygun olarak $f'(3)=6$ bulunur.

(c) Teğet $t(x)=9+6\,(x-3)$ olur. Bu teğet $3{,}02^2\approx9+6\cdot0{,}02=9{,}12$ verir. Tam değer $3{,}02^2=9{,}1204$ olur. $0{,}0004=0{,}02^2$ hatası tam olarak $h^2$ kadardır, çünkü $f(3+h)-9-6h=h^2$. Hata, doğrusal yaklaşımın vaat ettiği gibi $h$'den daha hızlı sıfıra gider.
:::
:::

:::aufgabe Alıştırma 2 ★ Kurallarla türev alma
<span class="anker" id="aufg-2"></span>

Türevi alın ve verilen noktada hesaplayın.

<ol class="al">

<li>

$1$ noktasında $f(x)=4x^3-2x+7$;

</li>

<li>

$0$ ve $1$ noktalarında $f(x)=x^2\,\mathrm{e}^x$;

</li>

<li>

$0$ ve $1$ noktalarında $f(x)=\dfrac{x}{1+x^2}$. $1$ noktasındaki sonuç grafik için ne anlama gelir?

</li>

</ol>

:::loesung
(a) Toplam ve sabit çarpan kuralı, kuvvet kuralıyla birlikte: $f'(x)=12x^2-2$, dolayısıyla $f'(1)=10$.

(b) $u=x^2$, $v=\mathrm{e}^x$ ile çarpım kuralı: $f'(x)=2x\,\mathrm{e}^x+x^2\,\mathrm{e}^x=(2x+x^2)\,\mathrm{e}^x$. Dolayısıyla $f'(0)=0$ ve $f'(1)=3\mathrm{e}\approx8{,}155$.

(c) $u=x$, $u'=1$, $v=1+x^2$, $v'=2x$ ile bölüm kuralı:

$$f'(x)=\frac{1\cdot(1+x^2)-x\cdot2x}{(1+x^2)^2}=\frac{1-x^2}{(1+x^2)^2},\qquad f'(0)=1,\qquad f'(1)=0 .$$

Grafiğin $1$ noktasında yatay bir teğeti vardır. En yüksek noktası da oradadır: Her $x$ için $\frac{x}{1+x^2}\le\frac12$ olur, çünkü $1+x^2-2x=(x-1)^2\ge0$; ayrıca $f(1)=\tfrac12$.
:::
:::

:::aufgabe Alıştırma 3 ★★ Büyüteçle kökler
<span class="anker" id="aufg-3"></span>

$f(x)=\sqrt x$ olsun.

<ol class="al">

<li>

Kuvvet kuralıyla $f'(x)$ ve $f''(x)$ türevlerini hesaplayın.

</li>

<li>

$4$ noktasındaki doğrusal ve ikinci dereceden yaklaşımla $\sqrt{4{,}1}$ için birer yaklaşık değer hesaplayın. İkisini hesap makinesinin verdiği değerle karşılaştırın.

</li>

<li>

Teğet grafiğin üstünde mi altında mı kalır? $f''(4)$ değerinin işaretiyle gerekçelendirin.

</li>

</ol>

:::loesung
(a) $\sqrt x=x^{1/2}$ ile $f'(x)=\tfrac12x^{-1/2}=\frac1{2\sqrt x}$ ve $f''(x)=-\tfrac14x^{-3/2}$ olur.

(b) $4$ noktasında $f(4)=2$, $f'(4)=\tfrac14$ ve $f''(4)=-\tfrac14\cdot\tfrac18=-\tfrac1{32}$ olur. $h=0{,}1$ ile:

$$\text{doğrusal: }2+\tfrac14\cdot0{,}1=2{,}025,\quad \text{kuadratik: }2{,}025-\tfrac12\cdot\tfrac1{32}\cdot0{,}01=2{,}025-0{,}00015625=2{,}02484375 .$$

Hesap makinesi $\sqrt{4{,}1}\approx2{,}0248457$ verir. Doğrusal yaklaşımın hatası yaklaşık $1{,}5\cdot10^{-4}$, ikinci dereceden yaklaşımınki ise yalnızca yaklaşık $1{,}9\cdot10^{-6}$ olur.

(c) $f''(4)<0$ olduğundan grafik teğetten aşağı doğru bükülür; teğet grafiğin üstünde kalır. Bu yüzden $2{,}025$ doğrusal yaklaşımı fazla büyüktür.
:::
:::

:::aufgabe Alıştırma 4 ★★ Köşe noktası var mı, yok mu?
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

$g(x)=x\,|x|$ fonksiyonunun $0$ noktasında türevlenebilir olduğunu fark bölümüyle gösterin ve $g'(0)$ değerini belirleyin.

</li>

<li>

$x>0$ ve $x<0$ için $g'(x)$ türevini belirleyin. $g'$ fonksiyonunun kendisinin $0$ noktasında türevi var mıdır?

</li>

<li>

$m(x)=\max(x,\,0)$ fonksiyonu $x$ pozitifse $x$ değerini, değilse $0$ döndürür. Bu fonksiyon nerede türevlenebilirdir ve türevi oralarda hangi değerleri alır?

</li>

</ol>

:::loesung
(a) $g(0)=0$ ve $\frac{g(h)-g(0)}{h}=\frac{h\,|h|}{h}=|h|$ olur. Bu ifade iki taraftan da $0$'a gider, dolayısıyla $g'(0)=0$. Mutlak değerin tek başına bir köşe noktası vardır, ama $x$ çarpanı iki kolu orijinde yassılaştırır.

(b) $x>0$ için $g(x)=x^2$ ve $g'(x)=2x$; $x<0$ için $g(x)=-x^2$ ve $g'(x)=-2x$ olur. (a) ile birlikte her $x$ için $g'(x)=2|x|$ bulunur. Bu fonksiyonun $0$'da bir köşe noktası vardır; fark bölümü $2|h|/h$ ise $\pm2$ olur. Dolayısıyla $g$ bir kez türevlenebilir, ama iki kez türevlenebilir değildir.

(c) $x>0$ için $m(x)=x$ ve $m'(x)=1$, $x<0$ için $m(x)=0$ ve $m'(x)=0$ olur. $0$ noktasında fark bölümü $h>0$ için $1$, $h<0$ için $0$ olur; orada türev yoktur. Grafiğin $0$'da bir köşe noktası vardır.
:::
:::
