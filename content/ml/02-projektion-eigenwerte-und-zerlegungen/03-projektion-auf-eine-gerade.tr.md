---
title: Bir doğru üzerine izdüşüm
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / İzdüşüm, Özdeğerler ve Ayrışımlar
order: 6220300
summary: Bir nokta bir doğrunun yanında duruyor.
tags: dik izdüşümü, izdüşüm matrisi, izdüşüm
lang: tr
---

<span class="anker" id="stufe-2"></span>

:::zweck
Bir nokta bir doğrunun yanında duruyor. Doğrunun hangi noktası ona en yakındır? Bu kesim soruyu orijinden geçen doğrular için, her boyutta cevaplıyor. Cevap dikme ayağıdır ve bunun nedeni Pisagor teoremidir.
:::

### Dikme ayağı

<span class="anker" id="stufe-2-1"></span>

Orijinden geçen bir doğru, bir $\mathbf{a}\ne\mathbf{0}$ doğrultu vektörünün bütün $t\,\mathbf{a}$ katlarından oluşur. Doğru üzerinde olması gerekmeyen bir $\mathbf{y}$ noktası veriliyor. Aranan, doğrunun $\mathbf{y}$ noktasına en yakın noktasıdır.

Kısım 1, Kesim 5.5'te bir ok, ışık dik geldiğinde bir doğru üzerine gölge düşürüyordu. Gölgenin uç noktası, $\mathbf{y}$ noktasından doğruya inilen dikmenin doğruyla buluştuğu noktadır, yani *dikme ayağı*. Bu noktadan $\mathbf{y}$ noktasına giden bağlantı doğruya diktir (Şekil [4](#abb-4)). Bu noktanın en yakın nokta olduğunu sonraki alt kesim gösteriyor. Burada önce nokta hesaplanıyor, hem de $\mathbf{a}$ birim uzunlukta olmasa bile.

:::herleitung Dikme ayağı
Aranan nokta doğru üzerindedir, yani henüz bilinmeyen bir $\hat x$ sayısıyla $\hat x\,\mathbf{a}$ biçimindedir. $\mathbf{y}-\hat x\,\mathbf{a}$ bağlantısı $\mathbf{a}$ vektörüne dik olmalıdır:

$$\mathbf{a}^{\top}(\mathbf{y}-\hat x\,\mathbf{a})=0\qquad\Longleftrightarrow\qquad \mathbf{a}^{\top}\mathbf{y}-\hat x\,\mathbf{a}^{\top}\mathbf{a}=0\qquad\Longleftrightarrow\qquad \hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} .$$

$\mathbf{a}\ne\mathbf{0}$ olduğundan $\mathbf{a}^{\top}\mathbf{a}=\lVert\mathbf{a}\rVert^2>0$ olur; yani bölme yapılabilir ve böyle tam bir tane $\hat x$ vardır.
:::

:::definition Tanım 2.1 (Bir doğru üzerine izdüşüm)
<span class="anker" id="satz-2-1"></span>

$\mathbf{a}\in\mathbb{R}^n$, $\mathbf{a}\ne\mathbf{0}$ olsun. $\mathbf{y}\in\mathbb{R}^n$ vektörünün, orijinden geçen ve $\mathbf{a}$ doğrultusunda olan doğru üzerine __dik izdüşümü__ şu noktadır:

<span class="anker" id="gl-2-1"></span>
$$\hat{\mathbf{y}}=\hat x\,\mathbf{a}\qquad\text{burada}\qquad\hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} . \tag{2.1}$$
:::

$\hat{\mathbf{y}}$ noktası $\mathbb{R}^n$ uzayında bir vektördür; $\hat x$ sayısı ise onun $\mathbf{a}$ boyunca koordinatıdır. İkisi birbirine karıştırılmamalıdır. $\mathbf{a}$ birim uzunluktaysa $\mathbf{a}^{\top}\mathbf{a}=1$ ve $\hat{\mathbf{y}}=(\mathbf{a}^{\top}\mathbf{y})\,\mathbf{a}$ olur; bu tam olarak Kısım 1'deki gölge noktasıdır.

:::abbildung ml/k2lot 4
$\mathbf{y}=(4,3)^{\top}$ vektörünün $\mathbf{a}=(1,2)^{\top}$ doğrultusundaki doğru üzerine izdüşümü. Dikme ayağı $\hat{\mathbf{y}}=2\mathbf{a}=(2,4)^{\top}$ noktasıdır; $\mathbf{r}=(2,-1)^{\top}$ bağlantısı (mavi) doğruya diktir. Doğrunun başka bir noktası, örneğin $(1,2)^{\top}$, $\mathbf{y}$ noktasına daha uzaktır (kesikli): $\mathbf{y}$, $\hat{\mathbf{y}}$ ve $(1,2)^{\top}$ noktalarının oluşturduğu üçgenin $\hat{\mathbf{y}}$ köşesinde bir dik açı vardır ve kesikli kenar bu üçgenin hipotenüsüdür.
:::

⁠**Sayısal örnek 1:** $\mathbf{a}=(1,\,2)^{\top}$ ve $\mathbf{y}=(4,\,3)^{\top}$ için $\mathbf{a}^{\top}\mathbf{y}=4+6=10$ ve $\mathbf{a}^{\top}\mathbf{a}=5$ olur (Şekil [5](#abb-5)); dolayısıyla $\hat x=2$ ve $\hat{\mathbf{y}}=(2,\,4)^{\top}$. $\mathbf{y}-\hat{\mathbf{y}}=(2,\,-1)^{\top}$ bağlantısı $\mathbf{a}$ vektörüne diktir: $2-2=0$.

:::abbildung ml/k2rproj 5
İzdüşümün iki iç çarpımı adım adım: $\hat x$ kesrinin payında $\mathbf{a}^{\top}\mathbf{y}=10$, paydasında $\mathbf{a}^{\top}\mathbf{a}=5$.
:::

⁠**Sayısal örnek 2:** $\mathbf{a}=(3,\,4)^{\top}$ ve $\mathbf{y}=(3,\,1)^{\top}$ için $\hat x=(9+4)/25=0{,}52$ ve $\hat{\mathbf{y}}=0{,}52\,(3,\,4)^{\top}=(1{,}56;\ 2{,}08)^{\top}$ olur; bu, Kısım 1'de $(0{,}6;\ 0{,}8)^{\top}=\mathbf{a}/5$ birim vektörüyle bulunan gölge noktasının aynısıdır. Doğrultu vektörünün uzunluğu hiçbir rol oynamaz: $\mathbf{a}$ yerine $c\ne0$ olmak üzere $c\,\mathbf{a}$ alınırsa $\hat x$ değeri $\hat x/c$ olur ve $\hat{\mathbf{y}}$ değişmez. Buna karşılık $\mathbf{y}$ iki katına çıkarılırsa $\hat{\mathbf{y}}$ de iki katına çıkar.

⁠**Kısacası:** $\mathbf{y}$ vektörünün $\mathbf{a}$ doğrultusundaki doğru üzerine izdüşümü dikme ayağıdır: $\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$.

### Dikme ayağı en yakın noktadır

<span class="anker" id="stufe-2-2"></span>

Şimdiye kadar yalnızca dikme ayağına giden bağlantının dik olduğu gösterildi. Dikme ayağının aynı zamanda en yakın nokta olduğu Pisagor teoreminden çıkar: Doğru üzerinde dikme ayağından uzaklaşmak, dik bağlantıya doğru boyunca uzanan bir parça eklemek demektir ve bu, uzaklığı yalnızca büyütebilir.

:::satz Teorem 2.2 (Dikme ayağı en yakın noktadır)
<span class="anker" id="satz-2-2"></span>

$\hat{\mathbf{y}}=\hat x\,\mathbf{a}$, $\mathbf{y}$ vektörünün $\mathbf{a}$ doğrultusundaki doğru üzerine izdüşümü olsun. Her $t$ sayısı için şu geçerlidir:

<span class="anker" id="gl-2-2"></span>
$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2=\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2+(t-\hat x)^2\,\lVert\mathbf{a}\rVert^2 . \tag{2.2}$$

Özellikle $\hat{\mathbf{y}}$, doğrunun $\mathbf{y}$ noktasına uzaklığı en küçük olan tek noktasıdır.
:::

:::beweis En yakın nokta
$t\,\mathbf{a}$ noktasından $\mathbf{y}$ noktasına giden bağlantı iki okun toplamı olarak yazılır:

$$\mathbf{y}-t\,\mathbf{a}=(\mathbf{y}-\hat{\mathbf{y}})+(\hat x-t)\,\mathbf{a} .$$

Birinci terim türetmeye göre $\mathbf{a}$ vektörüne diktir, dolayısıyla ikinci terime de diktir. Kısım 1, Kesim 5.3'teki Pisagor teoremine göre toplamın uzunluğunun karesi, uzunlukların karelerinin toplamıdır; bu da [(2.2)](#gl-2-2) bağıntısıdır. Sağ taraftaki ikinci terim hiçbir zaman negatif değildir ve yalnızca $t=\hat x$ için sıfırdır. Dolayısıyla uzaklık tam olarak $t=\hat x$ için en küçüktür.
:::

Dikme ayağının uzunluğu için $\lVert\hat{\mathbf{y}}\rVert=|\hat x|\,\lVert\mathbf{a}\rVert=|\mathbf{a}^{\top}\mathbf{y}|/\lVert\mathbf{a}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$ geçerlidir; burada $\varphi$, $\mathbf{a}$ ile $\mathbf{y}$ arasındaki açıdır. Bu, hipotenüsü $\mathbf{y}$ olan dik üçgendeki komşu dik kenardır.

⁠**Sayısal örnek:** Önceki alt kesimin ilk sayısal örneğinde $\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2=\lVert(2,\,-1)^{\top}\rVert^2=5$ olur. $t=1$ noktası, yani $(1,\,2)^{\top}$ için [(2.2)](#gl-2-2) bağıntısı $5+1\cdot5=10$ uzaklık karesini öngörür ve gerçekten de $\lVert(3,\,1)^{\top}\rVert^2=10$. $t=3$, yani $(3,\,6)^{\top}$ için de bu değer $5+1\cdot5=10=\lVert(1,\,-3)^{\top}\rVert^2$ olur. İki nokta dikme ayağına eşit uzaklıktadır, ama farklı taraflarda.

⁠**Kısacası:** Bir doğrunun en yakın noktası dikme ayağıdır, çünkü doğru boyunca atılan her adım Pisagor teoremine göre uzaklığın karesini büyütür.

:::hintergrund Neden tam bir tane en yakın nokta vardır ve bu neden Öklid normuna bağlıdır
İspat Pisagor teoremini kullanır; bu teorem de yalnızca bir iç çarpımdan türeyen normlar için geçerlidir. Kısım 1, Kesim 3.4'te mutlak değerler toplamı normunun (1-normunun) böyle bir norm olmadığı ortaya çıkmıştı. Bu normla teklik gerçekten de kaybolur. Örnek: $\mathbf{a}=(1,\,1)^{\top}$ doğrultusundaki doğru ve $\mathbf{y}=(1,\,0)^{\top}$ noktası. $0\le t\le1$ için

$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert_1=|1-t|+|0-t|=(1-t)+t=1 ,$$

yani bu uzaklık $\mathbf{0}$ ile $\mathbf{a}$ arasındaki bütün noktalar için aynı büyüklüktedir; bu doğru parçasının dışında uzaklık daha büyüktür. Bu normda en yakın noktalardan oluşan koca bir doğru parçası vardır. Öklid normunda ise tam bir tane vardır: $\hat x=\tfrac12$, yani $(\tfrac12,\,\tfrac12)^{\top}$ noktası. Tek olan ve basit bir formülle hesaplanabilen izdüşüm, pek çok yöntemin Öklid uzaklığını kullanmasının nedenlerinden biridir.
:::

### İzdüşüm matrisi

<span class="anker" id="stufe-2-3"></span>

$\mathbf{y}\mapsto\hat{\mathbf{y}}$ kuralı doğrusaldır: İki noktanın toplamı izdüşümlerinin toplamına, bir katı ise izdüşümünün aynı katına gider. Dolayısıyla Kısım 1, Kesim 8.2'ye göre bir matrisi vardır. $\mathbf{a}^{\top}\mathbf{y}$ sayısı $\mathbf{a}$ vektörünün öbür yanına yazılıp matris çarpımı yeniden parantezlenirse matris doğrudan okunur:

$$\hat{\mathbf{y}}=\mathbf{a}\,\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{y} .$$

Kesrin payında Kısım 1, Kesim 9.5'teki dış çarpım durur.

:::definition Tanım 2.3 (Bir doğrunun izdüşüm matrisi)
<span class="anker" id="satz-2-3"></span>

$\mathbf{a}\ne\mathbf{0}$ için

<span class="anker" id="gl-2-3"></span>
$$\mathbf{P}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}} \tag{2.3}$$

matrisine $\mathbf{a}$ doğrultusundaki doğru üzerine __izdüşüm matrisi__ denir. $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$ olur.
:::

:::satz Teorem 2.4 (Bir doğrunun izdüşüm matrisinin özellikleri)
<span class="anker" id="satz-2-4"></span>

$\mathbf{P}^{\top}=\mathbf{P}$ ve $\mathbf{P}^2=\mathbf{P}$ geçerlidir. Doğrunun noktaları yerinde kalır: $\mathbf{P}\mathbf{a}=\mathbf{a}$. $\mathbf{a}$ vektörüne dik vektörler $\mathbf{0}$ vektörüne gider. $\mathbf{P}$ matrisinin rankı $1$ olur.
:::

:::beweis Özellikler
$(\mathbf{a}\mathbf{a}^{\top})^{\top}=\mathbf{a}\mathbf{a}^{\top}$, dolayısıyla $\mathbf{P}$ simetriktir. Ayrıca $\mathbf{a}^{\top}\mathbf{a}$ bir sayı olduğundan $\mathbf{P}^2=\mathbf{a}(\mathbf{a}^{\top}\mathbf{a})\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})^2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{P}$ olur. $\mathbf{P}\mathbf{a}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{a})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{a}$. $\mathbf{a}^{\top}\mathbf{z}=0$ ise $\mathbf{P}\mathbf{z}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{z})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{0}$ olur. $\mathbf{P}$ matrisinin her sütunu $\mathbf{a}$ vektörünün bir katıdır, dolayısıyla rank $1$ olur.
:::

$\mathbf{P}^2=\mathbf{P}$ denkleminin basit bir anlamı vardır: Zaten doğru üzerinde duran, ikinci izdüşümde yerinde kalır.

⁠**Sayısal örnek:** $\mathbf{a}=(1,\,2)^{\top}$ için şu bulunur:

$$\mathbf{P}=\frac15\begin{pmatrix}1&2\\2&4\end{pmatrix},\qquad \mathbf{P}\begin{pmatrix}4\\3\end{pmatrix}=\frac15\begin{pmatrix}4+6\\8+12\end{pmatrix}=\begin{pmatrix}2\\4\end{pmatrix}.$$

$\mathbf{P}^2=\mathbf{P}$ için sağlama: $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)^2=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)=5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, dolayısıyla $\mathbf{P}^2=\frac1{25}\cdot5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=\mathbf{P}$. $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ matrisi Kısım 1, Kesim 11.5'te tersi olmayan bir matris örneğiydi. Şimdi ne yaptığı açık: Bir izdüşümün beş katıdır ve düzlemi $(1,\,2)^{\top}$ doğrultusundaki doğrunun üzerine ezer.

⁠**Kısacası:** Bir doğru üzerine izdüşüm, $\mathbf{P}=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ ile yapılan matris-vektör çarpımıdır; bu matris simetriktir ve $\mathbf{P}^2=\mathbf{P}$ koşulunu sağlar.

### Genel olarak izdüşümler

<span class="anker" id="stufe-2-4"></span>

Işık eğik geldiğinde de gölge oluşur. O zaman bir noktanın doğru üzerindeki gölgesi dikme ayağı olmaz, ama yine doğru üzerindedir; doğru üzerinde zaten bulunan bir nokta da kendi kendisinin gölgesidir. Demek ki $\mathbf{P}^2=\mathbf{P}$ özelliği korunur, simetri korunmaz.

:::definition Tanım 2.5 (İzdüşüm)
<span class="anker" id="satz-2-5"></span>

$\mathbf{P}^2=\mathbf{P}$ olan bir $\mathbf{P}$ kare matrisine __izdüşüm__ denir. Ayrıca her $\mathbf{y}$ için $\mathbf{y}-\mathbf{P}\mathbf{y}$ bağlantısı bütün $\mathbf{P}\mathbf{z}$ görüntülerine dikse bu izdüşüme dik izdüşüm denir.
:::

:::satz Teorem 2.6 (Dik demek simetrik demektir)
<span class="anker" id="satz-2-6"></span>

Bir $\mathbf{P}$ izdüşümü ancak ve ancak $\mathbf{P}^{\top}=\mathbf{P}$ ise dik izdüşümdür.
:::

:::beweis Dik demek simetrik demektir
Bütün $\mathbf{y},\mathbf{z}$ için $(\mathbf{y}-\mathbf{P}\mathbf{y})^{\top}\mathbf{P}\mathbf{z}=\mathbf{y}^{\top}(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}\mathbf{z}$ olur. $\mathbf{P}^{\top}=\mathbf{P}$ ise $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}=\mathbf{P}-\mathbf{P}^2=\mathbf 0$ olur ve ifade sıfırdır. Tersine, ifade bütün $\mathbf{y},\mathbf{z}$ için sıfırsa $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}$ matrisi sıfır matristir; çünkü $\mathbf{y}=\mathbf{e}_i$ ve $\mathbf{z}=\mathbf{e}_l$ seçilince ifade bu matrisin $(i,l)$ elemanını verir. O zaman $\mathbf{P}=\mathbf{P}^{\top}\mathbf{P}$ olur ve Kısım 1, Kesim 10.2'ye göre $\mathbf{P}^{\top}\mathbf{P}$ simetriktir.
:::

⁠**Sayısal örnek:** $\mathbf{P}=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$ matrisi $(x_1,\,x_2)^{\top}$ vektörünü $(x_1+x_2,\,0)^{\top}$ vektörüne götürür. $\mathbf{P}^2=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$ olduğundan $\mathbf{P}$, $x_1$ ekseni üzerine bir izdüşümdür. Simetrik değildir, dolayısıyla dik değildir: $(0,\,1)^{\top}$ noktası $(1,\,0)^{\top}$ noktasına gider, $(-1,\,1)^{\top}$ bağlantısı eksene eğiktir. Işık burada $(1,\,-1)^{\top}$ doğrultusunda gelir. $x_1$ ekseninin en yakın noktasını, yani $(0,\,0)^{\top}$ noktasını bu izdüşüm vermez.

⁠**Kısacası:** İzdüşüm, $\mathbf{P}^2=\mathbf{P}$ olan bir matristir; ancak ve ancak simetrikse diktir, yani dikme ayağını verir.

:::aufgabe Alıştırma 4 ★ Elle bir izdüşüm
<span class="anker" id="aufg-4"></span>

$\mathbf{y}=(3,\,3,\,0)^{\top}$ vektörünün $\mathbf{a}=(2,\,1,\,2)^{\top}$ doğrultusundaki doğru üzerine izdüşümünü bulun.

<ol class="al">

<li>

$\hat x$, $\hat{\mathbf{y}}$ ve $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}$ bağlantısını hesaplayın. $\mathbf{a}^{\top}\mathbf{r}=0$ eşitliğini doğrulayın. $\mathbf{y}$ noktası doğruya ne kadar uzaktır?

</li>

<li>

$\mathbf{P}$ izdüşüm matrisini kurun ve $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$ ile $\mathbf{P}\mathbf{a}=\mathbf{a}$ eşitliklerini doğrulayın.

</li>

</ol>

:::loesung
(a) $\mathbf{a}^{\top}\mathbf{y}=6+3+0=9$ ve $\mathbf{a}^{\top}\mathbf{a}=4+1+4=9$ olur, dolayısıyla $\hat x=1$ ve $\hat{\mathbf{y}}=\mathbf{a}=(2,\,1,\,2)^{\top}$. Bağlantı $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(1,\,2,\,-2)^{\top}$ olur ve $\mathbf{a}^{\top}\mathbf{r}=2+2-4=0$: Bağlantı doğruya diktir. $\mathbf{y}$ noktasının doğruya uzaklığı $\lVert\mathbf{r}\rVert=\sqrt{1+4+4}=3$ olur; Kesim [2.2](#stufe-2-2)'deki teoreme göre doğrunun hiçbir noktası daha yakın değildir.

(b)

$$\mathbf{P}=\frac{\mathbf{a}\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}=\frac19\begin{pmatrix}4&2&4\\2&1&2\\4&2&4\end{pmatrix},\qquad \mathbf{P}\mathbf{y}=\frac19\begin{pmatrix}12+6\\6+3\\12+6\end{pmatrix}=\begin{pmatrix}2\\1\\2\end{pmatrix},\qquad \mathbf{P}\mathbf{a}=\frac19\begin{pmatrix}8+2+8\\4+1+4\\8+2+8\end{pmatrix}=\mathbf{a} .$$
:::
:::

:::aufgabe Alıştırma 5 ★★ Doğru üzerinde Pisagor
<span class="anker" id="aufg-5"></span>

$\mathbf{a}=(1,\,2)^{\top}$ ve $\mathbf{y}=(4,\,3)^{\top}$, sayısal örnekteki gibi olsun.

<ol class="al">

<li>

$t=0$, $1$, $2$, $3$ ve $4$ için $\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2$ değerini doğrudan ve [(2.2)](#gl-2-2) ile hesaplayın.

</li>

<li>

$\mathbf{a}$ ile $\mathbf{y}$ arasındaki $\varphi$ açısını hesaplayın ve $\lVert\hat{\mathbf{y}}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$ eşitliğini doğrulayın.

</li>

</ol>

:::loesung
(a) Doğrudan: $t=0$: $\lVert(4,\,3)^{\top}\rVert^2=25$; $t=1$: $\lVert(3,\,1)^{\top}\rVert^2=10$; $t=2$: $\lVert(2,\,-1)^{\top}\rVert^2=5$; $t=3$: $\lVert(1,\,-3)^{\top}\rVert^2=10$; $t=4$: $\lVert(0,\,-5)^{\top}\rVert^2=25$. [(2.2)](#gl-2-2) ile, $\hat x=2$, $\lVert\mathbf{r}\rVert^2=5$ ve $\lVert\mathbf{a}\rVert^2=5$ alınarak: $5+5(t-2)^2$ ifadesi $25$, $10$, $5$, $10$, $25$ verir. Değerler $t=2$ dikme ayağının çevresinde simetriktir, çünkü uzaklık karesi, doğru boyunca alınan uzaklığın karesiyle artar.

(b) $\cos\varphi=\mathbf{a}^{\top}\mathbf{y}/(\lVert\mathbf{a}\rVert\,\lVert\mathbf{y}\rVert)=10/(\sqrt5\cdot5)=2/\sqrt5\approx0{,}894$, dolayısıyla $\varphi\approx26{,}57^\circ$. $\lVert\hat{\mathbf{y}}\rVert=\lVert(2,\,4)^{\top}\rVert=\sqrt{20}=2\sqrt5$ ve $|\cos\varphi|\,\lVert\mathbf{y}\rVert=\tfrac2{\sqrt5}\cdot5=2\sqrt5$ olur.
:::
:::

:::aufgabe Alıştırma 6 ★★ Hangi matrisler izdüşümdür?
<span class="anker" id="aufg-6"></span>

Her matris için bir izdüşüm olup olmadığını ve dik izdüşüm olup olmadığını inceleyin. İzdüşüm olanlarda neyin üzerine izdüşüm yapıldığını açıklayın.

$$\mathbf{P}_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad \mathbf{P}_2=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad \mathbf{P}_3=\begin{pmatrix}1&0\\1&0\end{pmatrix},\quad \mathbf{P}_4=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad \mathbf{P}_5=\mathbf{I},\quad \mathbf{P}_6=\mathbf 0 .$$

:::loesung
Her matris için önce $\mathbf{P}^2=\mathbf{P}$, sonra $\mathbf{P}^{\top}=\mathbf{P}$ koşulu denetlenir.

<ul>

<li>

$\mathbf{P}_1$: $\mathbf{P}_1^2=\mathbf{P}_1$ ve simetrik, dolayısıyla $x_1$ ekseni üzerine dik izdüşüm.

</li>

<li>

$\mathbf{P}_2$: $\mathbf{P}_2^2=\tfrac14\bigl(\begin{smallmatrix}2&2\\2&2\end{smallmatrix}\bigr)=\mathbf{P}_2$ ve simetrik: $(1,\,1)^{\top}$ doğrultusundaki doğru üzerine dik izdüşüm; $\mathbf{a}=(1,\,1)^{\top}$ ile $\mathbf{P}_2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ olur.

</li>

<li>

$\mathbf{P}_3$: $\mathbf{P}_3^2=\bigl(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\bigr)=\mathbf{P}_3$, ama simetrik değil. Eğik bir izdüşüm: $(x_1,\,x_2)^{\top}$ vektörünü $x_1\,(1,\,1)^{\top}$ vektörüne, yani $(1,\,1)^{\top}$ doğrultusundaki doğrunun üzerine götürür; $(0,\,1)^{\top}$ vektörünü ise sıfıra götürür. Işık doğruya dik olarak değil, $(0,\,1)^{\top}$ doğrultusunda gelir.

</li>

<li>

$\mathbf{P}_4$: $\mathbf{P}_4^2=\bigl(\begin{smallmatrix}1&4\\0&1\end{smallmatrix}\bigr)\ne\mathbf{P}_4$. Bir izdüşüm değil, bir kaymadır; iki kez uygulanınca iki katı kadar kaydırır.

</li>

<li>

$\mathbf{P}_5=\mathbf{I}$: $\mathbf{I}^2=\mathbf{I}$, simetrik. Düzlemin tamamı üzerine dik izdüşüm; her şeyi olduğu yerde bırakır.

</li>

<li>

$\mathbf{P}_6=\mathbf 0$: $\mathbf 0^2=\mathbf 0$, simetrik. Orijin üzerine dik izdüşüm.

</li>

</ul>
:::
:::
