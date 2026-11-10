---
title: Hesaplama grafikleri
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15231000
summary: Bir bilgisayar uzun formülleri adım adım hesaplar ve her adım, türevi bilinen basit bir işlemdir.
tags: hesaplama grafiği, ileri hesaplaması, yerel türevi
lang: tr
---

<span class="anker" id="stufe-9"></span>

:::zweck
Bir bilgisayar uzun formülleri adım adım hesaplar ve her adım, türevi bilinen basit bir işlemdir. Bir hesaplama grafiği bu adımları ve aralarındaki bağımlılıkları görünür kılar. Bu kesim böyle bir grafik çiziyor, onu bir tablo olarak ileri doğru hesaplıyor ve her kenara yerel türevini yazıyor. Böylece sonucun bütün girdilere göre türevlerini mekanik olarak hesaplamak için her şey hazır olur.
:::

### Ara sonuçlar

<span class="anker" id="stufe-9-1"></span>

Kesim [1.4](die-ableitung.html#stufe-1-4)'teki kurallarla, temel aritmetik işlemlerden ve bilinen fonksiyonlardan oluşan her formülün türevi alınabilir. Ama sonuç formül olarak açık yazılırsa çoğu zaman fonksiyonun kendisinden çok daha uzun olur. $n$ çarpanlı bir çarpımın türevi, çarpım kuralına göre her biri $n$ çarpanlı $n$ terimden oluşur; yani fonksiyonun yalnızca $n$ çarpanı varken formül $n^2$ ile büyür. Ara sonuçlarla ise hesap küçük kalır. Her adımdan sonra o ana kadarki değer ve o ana kadarki türev akılda tutulur ve hesaba formüllerle değil, sayılarla devam edilir.

::::beispiel [Sayısal örnek]
$p(x)=(x+1)(x+2)(x+3)(x+4)$ olsun ve $p'(0)$ aransın. Açık yazılmış çarpım kuralı, her birinde bir çarpanın yerine türevi olan $1$ konmuş dört terim verir:

$$p'(0)=2\cdot3\cdot4+1\cdot3\cdot4+1\cdot2\cdot4+1\cdot2\cdot3=24+12+8+6=50$$

(Şekil [17](#abb-17)). Adım adım, $p_1=x+1$, $p_k=p_{k-1}\cdot(x+k)$ kısmi çarpımları ve $p_k'=p_{k-1}'\cdot(x+k)+p_{k-1}\cdot1$ çarpım kuralıyla şöyle ilerlenir:

$$\begin{gathered} p_1=1,\quad p_1'=1;\qquad p_2=1\cdot2=2,\quad p_2'=1\cdot2+1\cdot1=3;\\ p_3=2\cdot3=6,\quad p_3'=3\cdot3+2\cdot1=11;\qquad p_4=6\cdot4=24,\quad p_4'=11\cdot4+6\cdot1=50 . \end{gathered}$$

Her adım, kaç çarpanın işlenmiş olduğundan bağımsız olarak iki çarpma ve bir toplamaya mal olur.

:::abbildung ml/k3rvierfaktoren 17
$0$ noktasında $p(x)=(x+1)(x+2)(x+3)(x+4)$ için açık yazılmış çarpım kuralı: $k$ teriminde $x+k$ çarpanının yerine türevi olan $1$ konmuştur.
:::
::::

⁠**Kısacası:** Açık yazılmış türev formülleri çabucak fonksiyondan çok daha uzun olur; sayı olarak saklanan ara sonuçlarla adım başına maliyet küçük kalır.

### Hesaplama grafiği

<span class="anker" id="stufe-9-2"></span>

Bir hesabın hangi ara sonuçları olduğunu ve her birinin neye bağlı olduğunu en açık biçimde düğümlerden ve oklardan oluşan bir resim gösterir. Bir $a$ düğümünden bir $b$ düğümüne giden bir ok şu anlama gelir: $b$'yi hesaplamak için $a$ gerekir.

:::definition Tanım 9.1 (Hesaplama grafiği)
<span class="anker" id="satz-9-1"></span>

Bir __hesaplama grafiği__ düğümlerden ve yönlü kenarlardan, yani düğümler arasındaki oklardan oluşur. Her düğüm bir sayıyı ya da daha büyük hesaplarda bütün bir vektörü veya matrisi temsil eder. Girdi düğümleri hesabın girdileridir; diğer her $v$ düğümü, $v$'ye bir kenar giden düğümlerden bir temel işlemle oluşur. Bu düğümlere $v$'nin öncülleri, $v$'ye de onların ardılı denir. Kenarlar izlendiğinde daha önce bulunulan bir düğüme asla geri dönülmez; böyle bir grafiğe döngüsüz denir. Özel olarak belirlenmiş bir düğüm sonuçtur.
:::

Temel işlemler, temel aritmetik işlemler ile kare, üstel fonksiyon ya da lojistik fonksiyon gibi tek değişkenli fonksiyonlardır. Grafik döngüsüz olduğundan düğümler her zaman, her düğüm öncüllerinden sonra gelecek biçimde sıralanabilir; hesap bu sırayla yapılır. Döngüler ve dallanmalar içeren bir hesaplama programı da belirli girdi değerleri için böyle bir grafik verir: Üç kez çalıştırılan bir döngü, aynı düğümleri art arda üç kez üretir.

::::beispiel [Sayısal örnek]
Bu ve sonraki kesimin örneği

<span class="anker" id="gl-9-1"></span>
$$f(x_1,x_2,x_3)=(x_1+x_2)\,(x_2+x_3) \tag{9.1}$$

fonksiyonudur; ara sonuçları $v_1=x_1+x_2$ ve $v_2=x_2+x_3$, sonucu $f=v_1\cdot v_2$ olur. Grafikte üç girdi düğümü, iki toplama düğümü ve bir çarpma düğümü vardır; bunlar altı kenarla birbirine bağlıdır (Şekil [18](#abb-18)). $x_2$ girdisinin iki ardılı vardır; grafik orada dallanır.

:::abbildung ml/k3graph 18
$f=(x_1+x_2)\,(x_2+x_3)$ fonksiyonunun hesaplama grafiği. Oklar hesap yönünü gösterir, daireler temel işlemi içerir. Yeşil renkle $(1,\,2,\,3)$ noktasındaki ileri hesaplamanın değerleri yazılıdır.
:::
::::

⁠**Kısacası:** Bir hesaplama grafiği bir hesabı temel işlemlere ayırır; kenarları hangi değerin hangi başka değere girdiğini gösterir ve grafik döngüsüz olduğundan onu hesaplamanın her zaman bir sırası vardır.

### İleri hesaplama

<span class="anker" id="stufe-9-3"></span>

Bir hesaplama grafiğini değerlendirmek, düğümleri her düğümün öncüllerinden sonra geldiği bir sırayla hesaplamak demektir. Adımlar alt alta yazılırsa türevler için de gereken bir tablo ortaya çıkar: Yalnızca sonuç değil, bütün değerler saklanır.

:::definition Tanım 9.2 (İleri hesaplama)
<span class="anker" id="satz-9-2"></span>

Bir hesaplama grafiğinin __ileri hesaplaması__, bütün düğümleri her düğümün öncüllerinden sonra geldiği bir sırayla hesaplar ve her değeri saklar.
:::

::::beispiel [Sayısal örnek]
[(9.1)](#gl-9-1) için $(1,\,2,\,3)$ noktasında Tablo [3](#tab-3) ortaya çıkar.

<span class="anker" id="tab-3"></span>

**Tablo 3:** $(1,\,2,\,3)$ noktasında $f=(x_1+x_2)\,(x_2+x_3)$ için ileri hesaplama.

| Düğüm | Hesap | Değer |
|---|---|---|
| $x_1$ | girdi | $1$ |
| $x_2$ | girdi | $2$ |
| $x_3$ | girdi | $3$ |
| $v_1$ | $x_1+x_2$ | $3$ |
| $v_2$ | $x_2+x_3$ | $5$ |
| $f$ | $v_1\cdot v_2$ | $15$ |
::::

⁠**Kısacası:** İleri hesaplama, grafiği düğüm düğüm değerlendirir ve her ara değeri saklar.

### Yerel türevler

<span class="anker" id="stufe-9-4"></span>

Her kenar bir düğümü, ondan bir temel işlemle oluşan bir ardılla bağlar. Ardılın bu tek öncüldeki küçük bir değişime ne kadar güçlü tepki verdiği, temel işlemin sıradan bir kısmi türevidir.

:::definition Tanım 9.3 (Yerel türev)
<span class="anker" id="satz-9-3"></span>

$a$'dan $b$'ye giden bir kenar için, $b$'yi hesaplayan temel işlemin $a$ girdisine göre $\partial b/\partial a$ kısmi türevine kenarın __yerel türevi__ denir. Yerel türev, ileri hesaplamanın saklanan değerleriyle hesaplanır.
:::

Temel işlemler için yerel türevler basittir (Tablo [4](#tab-4)). Dikkat çekici olan, ne kadar az şeye ihtiyaç duydukları: Üstel fonksiyonda ve lojistik fonksiyonda ardılın kendi saklanan değeri yeter. Maksimum düğümünün, iki girdi eşit olduğunda bir köşe noktası vardır; orada iki tek taraflı değerden biri kullanılır.

<span class="anker" id="tab-4"></span>

**Tablo 4:** Saklanan değerlerle ifade edilmiş, temel işlemlerin yerel türevleri.

| İşlem | yerel türevler | gereken değerler |
|---|---|---|
| $b=a_1+a_2$ | $\partial b/\partial a_1=1$, $\ \partial b/\partial a_2=1$ | yok |
| $b=a_1\cdot a_2$ | $\partial b/\partial a_1=a_2$, $\ \partial b/\partial a_2=a_1$ | girdiler |
| $b=a^2$ | $\partial b/\partial a=2a$ | girdi |
| $b=\mathrm{e}^a$ | $\partial b/\partial a=\mathrm{e}^a=b$ | çıktı |
| $b=\sigma(a)$ | $\partial b/\partial a=b\,(1-b)$ | çıktı |
| $b=\max(a_1,a_2)$ | büyük girdi için $1$, diğeri için $0$ | hangisinin büyük olduğu |

Yerel türevlerle, Kesim [6.2](die-kettenregel-fur-mehrere-variablen.html#stufe-6-2)'deki zincir kuralı tamamen bir sayma işidir: Sonucun bir girdiye göre türevi, girdiden sonuca giden bütün yollar üzerinden toplamdır ve her yol boyunca kenarlarının yerel türevleri çarpılır.

::::beispiel [Sayısal örnek]
Şekil [18](#abb-18) içindeki grafikte girdilerden toplama düğümlerine giden dört kenarın yerel türevi $1$ olur. $v_1$'den sonuca giden kenarın yerel türevi $\partial f/\partial v_1=v_2=5$, $v_2$'den gidenin $\partial f/\partial v_2=v_1=3$ olur. $x_1$'den sonuca bir yol gider, $x_3$'ten de; $x_2$'den iki yol gider. Dolayısıyla şu bulunur:

$$\frac{\partial f}{\partial x_1}=1\cdot5=5,\qquad \frac{\partial f}{\partial x_2}=1\cdot5+1\cdot3=8,\qquad \frac{\partial f}{\partial x_3}=1\cdot3=3 .$$

Sağlama: Çarpım açılınca $f=x_1x_2+x_1x_3+x_2^2+x_2x_3$ olur; kısmi türevleri $x_2+x_3=5$, $x_1+2x_2+x_3=8$ ve $x_1+x_2=3$ olur.
::::

⁠**Kısacası:** Her kenar, saklanan değerlerle hesaplanmış olarak, temel işleminin yerel türevini taşır; sonucun türevi, bu sayıların çarpımlarının bütün yollar üzerinden toplamıdır.

:::aufgabe Alıştırma 32 ★ Kare içeren bir grafik
<span class="anker" id="aufg-32"></span>

$f(x_1,x_2,x_3)=(x_1x_2+x_3)^2$ olsun.

<ol class="al">

<li>

$v_1=x_1x_2$, $v_2=v_1+x_3$ ve $f=v_2^2$ ara sonuçlarıyla hesaplama grafiğini çizin.

</li>

<li>

$(1,\,2,\,3)$ noktasında ileri hesaplamanın tablosunu oluşturun ve her kenara yerel türevini yazın.

</li>

<li>

Üç kısmi türevin hepsini yollar üzerinden toplamlar olarak hesaplayın ve sağlamasını yapın.

</li>

</ol>

:::loesung
(a) Girdiler $x_1,x_2,x_3$; $x_1$ ve $x_2$'den kenar alan bir $v_1$ çarpma düğümü; $v_1$ ve $x_3$'ten kenar alan bir $v_2$ toplama düğümü; $v_2$'den bir kenar alan bir $f$ kare düğümü.

(b) İleri: $x_1=1$, $x_2=2$, $x_3=3$, $v_1=2$, $v_2=5$, $f=25$. Yerel türevler: $\partial v_1/\partial x_1=x_2=2$, $\partial v_1/\partial x_2=x_1=1$, $\partial v_2/\partial v_1=1$, $\partial v_2/\partial x_3=1$, $\partial f/\partial v_2=2v_2=10$.

(c) Her girdiden sonuca tam olarak bir yol gider:

$$\frac{\partial f}{\partial x_1}=2\cdot1\cdot10=20,\qquad \frac{\partial f}{\partial x_2}=1\cdot1\cdot10=10,\qquad \frac{\partial f}{\partial x_3}=1\cdot10=10 .$$

Sağlama: $\partial_1f=2\,(x_1x_2+x_3)\,x_2=20$, $\partial_2f=2\,(x_1x_2+x_3)\,x_1=10$, $\partial_3f=2\,(x_1x_2+x_3)=10$.
:::
:::

:::aufgabe Alıştırma 33 ★★ Beş çarpan
<span class="anker" id="aufg-33"></span>

$p(x)=(x+1)(x+2)(x+3)(x+4)(x+5)$ olsun.

<ol class="al">

<li>

$p'(1)$ türevini, Kesim [9.1](#stufe-9-1)'deki sayısal örnekte olduğu gibi kısmi çarpımlarla adım adım hesaplayın.

</li>

<li>

Açık yazılmış çarpım kuralı kaç çarpma gerektirir, adım adım hesap kaç çarpma gerektirir? İkisi $n$ çarpan sayısıyla nasıl büyür?

</li>

</ol>

:::loesung
(a) $1$ noktasında çarpanlar $2,3,4,5,6$ olur. Adım adım:

$$\begin{aligned} p_1&=2, & p_1'&=1,\\ p_2&=2\cdot3=6, & p_2'&=1\cdot3+2\cdot1=5,\\ p_3&=6\cdot4=24, & p_3'&=5\cdot4+6\cdot1=26,\\ p_4&=24\cdot5=120, & p_4'&=26\cdot5+24\cdot1=154,\\ p_5&=120\cdot6=720, & p_5'&=154\cdot6+120\cdot1=1044 . \end{aligned}$$

Dolayısıyla $p'(1)=1044$. Sağlama: $p'(1)=p(1)\bigl(\tfrac12+\tfrac13+\tfrac14+\tfrac15+\tfrac16\bigr)=720\cdot\tfrac{87}{60}=1044$.

(b) Açık yazılmış çarpım kuralının her biri $n-1$ çarpanlı $n$ terimi vardır, dolayısıyla $n\,(n-2)$ çarpma gerekir; $n=5$ için bu $15$ eder. Adım adım hesapta $n-1$ adımın her biri iki çarpma gerektirir, yani $n=5$ için $8$. Açık yazılmış formül $n^2$ ile, adım adım hesap $n$ ile büyür.
:::
:::

:::aufgabe Alıştırma 34 ★★ Grafik olarak bir döngü
<span class="anker" id="aufg-34"></span>

Bir program $y=x$ atar ve sonra $y$'nin art arda üç kez karesini alır.

<ol class="al">

<li>

Hesaplama grafiğini çizin ve $y(x)$ fonksiyonunu verin.

</li>

<li>

$x=2$ noktasında bütün ara değerleri ve yerel türevleri, bunlardan da $y'(2)$ türevini hesaplayın. (a)'daki formülün türeviyle karşılaştırın.

</li>

</ol>

:::loesung
(a) Grafik, üç kare düğümünden oluşan bir $x\to y_1\to y_2\to y_3$ zinciridir, $y_k=y_{k-1}^2$. Buradan $y=((x^2)^2)^2=x^8$ olur.

(b) $2$ noktasında: $y_1=4$, $y_2=16$, $y_3=256$. Yerel türevler $2\cdot2=4$, $2\cdot4=8$ ve $2\cdot16=32$, çarpımları $4\cdot8\cdot32=1024$ olur. Formül $8x^7=8\cdot128=1024$ verir.
:::
:::
