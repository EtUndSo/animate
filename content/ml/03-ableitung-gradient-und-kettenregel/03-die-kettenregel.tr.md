---
title: Zincir kuralı
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15230300
summary: Birçok fonksiyon, bir fonksiyonun başka bir fonksiyonun içine yerleştirilmesiyle ortaya çıkar.
tags: bileşkesi, lojistik fonksiyon
lang: tr
---

<span class="anker" id="stufe-2"></span>

:::zweck
Birçok fonksiyon, bir fonksiyonun başka bir fonksiyonun içine yerleştirilmesiyle ortaya çıkar. Zincir kuralı, böyle bir bileşkenin türevinin parçaların türevlerinden nasıl elde edildiğini söyler: Tek tek aşamaların çarpanları çarpılır. Bu, istenildiği kadar çok halkadan oluşan zincirler için de geçerlidir. Sonda, türevi fonksiyonun kendisiyle ifade edilebilen lojistik fonksiyon yer alıyor.
:::

### Bileşke

<span class="anker" id="stufe-2-1"></span>

$(3x+1)^2$ fonksiyonu iki adımda hesaplanır: önce $u=3x+1$, sonra $u^2$. Birçok formül böyle, basit adımların art arda uygulanması olarak kuruludur. Bu yapıyı tanıyan, türevi adımların türevlerinden bir araya getirebilir.

:::definition Tanım 2.1 (Bileşke)
<span class="anker" id="satz-2-1"></span>

$g$ ve $f$ fonksiyonsa ve her $g(x)$ değeri $f$ fonksiyonunun tanımlı olduğu yerdeyse

$$(f\circ g)(x)=f\bigl(g(x)\bigr)$$

fonksiyonuna $f$ ile $g$ fonksiyonlarının __bileşkesi__ denir ve “$f$ bileşke $g$” diye okunur. Önce uygulanan $g$ fonksiyonuna iç fonksiyon, $f$ fonksiyonuna dış fonksiyon denir.
:::

::::beispiel [Sayısal örnek]
$F(x)=(3x+1)^2$ için iç fonksiyon $g(x)=3x+1$, dış fonksiyon $f(u)=u^2$ olur, yani $F=f\circ g$. $1$ noktasında $g(1)=4$ ve $F(1)=f(4)=16$ olur. Sıra önemlidir: $(g\circ f)(x)=g(f(x))=3x^2+1$ başka bir fonksiyondur ve $1$ noktasındaki değeri $4$ olur.
::::

⁠**Kısacası:** $f\circ g$ bileşkesi önce $g$ fonksiyonunu, sonra $f$ fonksiyonunu uygular; sıra değiştirilemez.

### Zincir kuralı

<span class="anker" id="stufe-2-2"></span>

$F=f\circ g$, $x$ değerindeki küçük bir değişime nasıl tepki verir? Değişim iki aşama boyunca izlenir. Birinci aşama küçük bir $\Delta x$ değişimini, doğrusal yaklaşıma göre yaklaşık $\Delta u\approx g'(x)\,\Delta x$ olarak iletir. İkinci aşama bu değişimi $\Delta y\approx f'(u)\,\Delta u$ olarak iletir. Toplamda $\Delta y\approx f'(u)\,g'(x)\,\Delta x$ olur. İki dişli kademesinden oluşan bir dişli takımında olduğu gibi aşamaların çarpanları çarpılır (Şekil [4](#abb-4)).

:::abbildung ml/k3getriebe 4
$y=(3x+1)^2$ için $1$ noktasında dişli takımı olarak zincir kuralı. Üç sayı doğrusunun da ölçeği aynıdır. $\Delta x=0{,}01$ parçası (mavi) birinci aşamada üç katına, $\Delta u=0{,}03$ (turuncu), ikinci aşamada bunun yaklaşık sekiz katına, $\Delta y=0{,}2409\approx0{,}24$ (kırmızı) uzatılır.
:::

:::satz Teorem 2.2 (Zincir kuralı)
<span class="anker" id="satz-2-2"></span>

$g$, $x$ noktasında ve $f$, $g(x)$ noktasında türevlenebilirse $f\circ g$, $x$ noktasında türevlenebilirdir ve şu geçerlidir:

<span class="anker" id="gl-2-1"></span>
$$(f\circ g)'(x)=f'\bigl(g(x)\bigr)\cdot g'(x). \tag{2.1}$$
:::

Türevlerin nerede hesaplandığı önemlidir: $g'$, $x$ noktasında, $f'$ ise $u=g(x)$ noktasında, yani dış fonksiyonun gerçekten çalıştığı yerde. $u=g(x)$ ve $y=f(u)$ ile kural çoğu zaman $\frac{\mathrm{d} y}{\mathrm{d} x}=\frac{\mathrm{d} y}{\mathrm{d} u}\cdot\frac{\mathrm{d} u}{\mathrm{d} x}$ diye yazılır. Bu, sanki $\mathrm{d} u$ sadeleşiyormuş gibi görünür. Akılda tutma yolu olarak işe yarar, gerekçe olarak değil; çünkü bu simgeler kesir değil, limittir.

:::beweis Zincir kuralı
$u=g(x)$ olsun. Doğrusal yaklaşım [(1.4)](die-ableitung.html#gl-1-4) uyarınca $r_g(h)/h\to0$ olmak üzere $g(x+h)=u+g'(x)\,h+r_g(h)$ ve $r_f(k)/k\to0$ olmak üzere $f(u+k)=f(u)+f'(u)\,k+r_f(k)$ olur; burada $r_f(0)=0$ alınsın. $k=g(x+h)-u=g'(x)\,h+r_g(h)$ konur. O zaman şu elde edilir:

$$f\bigl(g(x+h)\bigr)-f(u)=f'(u)\,k+r_f(k)=f'(u)\,g'(x)\,h+f'(u)\,r_g(h)+r_f(k).$$

$h$'ye bölündükten sonra ortadaki terim $0$'a gider. Sonuncusu için, $k\ne0$ olduğu sürece $r_f(k)/h=\bigl(r_f(k)/k\bigr)\cdot(k/h)$ yazılır; ilk çarpan $0$'a gider, çünkü $h$ ile birlikte $k$ da $0$'a gider, ikincisi ise $g'(x)$'e gider. $k=0$ ise terim zaten $0$ olur. Geriye $f'(u)\,g'(x)$ kalır.
:::

::::beispiel [Sayısal örnek]
$F(x)=(3x+1)^2$ için $g'(x)=3$ ve $f'(u)=2u$ olur. $1$ noktasında $u=g(1)=4$, dolayısıyla

$$F'(1)=f'(4)\cdot g'(1)=8\cdot3=24 .$$

Sağlama: Açılınca $F(x)=9x^2+6x+1$, dolayısıyla $F'(x)=18x+6$ ve $F'(1)=24$ olur. Şekil [4](#abb-4) aynı şeyi sayılarla gösteriyor: $F(1{,}01)=4{,}03^2=16{,}2409$; doğrusal yaklaşım ise $16+24\cdot0{,}01=16{,}24$ öngörür.
::::

⁠**Kısacası:** Bir bileşkede aşamaların türevleri çarpılır; her biri, kendi aşamasının çalıştığı noktada hesaplanır: $(f\circ g)'(x)=f'(g(x))\,g'(x)$.

### Çok halkalı zincirler

<span class="anker" id="stufe-2-3"></span>

Hesapların çoğu ikiden fazla adımdan oluşur. Zincir kuralı tekrar tekrar uygulanabilir: Üç aşamada $f_3\circ f_2\circ f_1=f_3\circ(f_2\circ f_1)$ olur ve [(2.1)](#gl-2-1) iki kez uygulandığında üç çarpanlı bir çarpım verir. İstenildiği kadar çok aşama için de aynısı geçerlidir.

:::satz Teorem 2.3 (Çok halkalı zincirler için zincir kuralı)
<span class="anker" id="satz-2-3"></span>

$u_0=x$ ve $k=1,\dots,L$ için $u_k=f_k(u_{k-1})$ olsun ve her $f_k$ fonksiyonu $u_{k-1}$ noktasında türevlenebilir olsun. O zaman şu geçerlidir:

<span class="anker" id="gl-2-2"></span>
$$\frac{\mathrm{d} u_L}{\mathrm{d} x}=f_L'(u_{L-1})\cdot f_{L-1}'(u_{L-2})\cdots f_1'(u_0). \tag{2.2}$$
:::

Hesap için buradan bir sıra çıkar. Her çarpan, kendi aşamasının çalıştığı değere ihtiyaç duyar. Bu yüzden önce, sıradan hesaplamada olduğu gibi $u_1,u_2,\dots$ ara değerleri, ancak ondan sonra çarpanlar hesaplanır. Çarpanların ardından hangi sırayla çarpıldığı, sayılarda fark etmez.

::::beispiel [Sayısal örnek]
$x=1$ noktasında $y=\dfrac1{(x^2+1)^3}$ olsun. Zincirin üç halkası vardır:

$$u_1=x^2+1=2,\qquad u_2=u_1^3=8,\qquad y=\frac1{u_2}=\frac18 .$$

Çarpanlar $\frac{\mathrm{d} u_1}{\mathrm{d} x}=2x=2$, $\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=3u_1^2=12$ ve $\frac{\mathrm{d} y}{\mathrm{d} u_2}=-\frac1{u_2^2}=-\frac1{64}$ olur, dolayısıyla

$$\frac{\mathrm{d} y}{\mathrm{d} x}=2\cdot12\cdot\Bigl(-\frac1{64}\Bigr)=-\frac{24}{64}=-0{,}375 .$$

Sağlama: $y=(x^2+1)^{-3}$ fonksiyonunun kuvvet ve zincir kuralına göre türevi $-3\,(x^2+1)^{-4}\cdot2x$, $1$ noktasında yani $-6/16=-0{,}375$ olur.
::::

⁠**Kısacası:** Uzun bir zincirde türev, bütün halkaların türevlerinin çarpımıdır; önce ara değerler, sonra çarpanlar hesaplanır.

### Lojistik fonksiyon

<span class="anker" id="stufe-2-4"></span>

Bazı büyüklükler iki sınır arasında düzgünce kalmalıdır, örneğin $0$ ile $1$ arasındaki bir oran. Her gerçel sayıyı sıçramadan, köşe noktası olmadan ve hep artarak bu aralığa gönderen bir fonksiyon lojistik fonksiyondur. Doygunluklu büyümeyi de betimler: Bir büyüklük önce neredeyse üstel olarak büyür, sonra bir üst sınıra yaklaşır. Türevi, zincir kuralı için güzel bir örnektir ve dikkat çekici bir biçime sahiptir.

:::definition Tanım 2.4 (Lojistik fonksiyon)
<span class="anker" id="satz-2-4"></span>

Aşağıdaki

<span class="anker" id="gl-2-3"></span>
$$\sigma(x)=\frac1{1+\mathrm{e}^{-x}} \tag{2.3}$$

fonksiyonuna __lojistik fonksiyon__ denir.
:::

Büyük pozitif $x$ için $\mathrm{e}^{-x}$ neredeyse $0$, $\sigma(x)$ ise neredeyse $1$ olur. Büyük negatif $x$ için $\mathrm{e}^{-x}$ çok büyüktür ve $\sigma(x)$ neredeyse $0$ olur. $0$ noktasında $\sigma(0)=\tfrac12$ olur. Ayrıca $\sigma(-x)=1-\sigma(x)$ geçerlidir, çünkü $\frac1{1+\mathrm{e}^{x}}=\frac{\mathrm{e}^{-x}}{\mathrm{e}^{-x}+1}=1-\frac1{1+\mathrm{e}^{-x}}$; grafik dolayısıyla $(0,\,\tfrac12)$ noktasına göre simetriktir (Şekil [5](#abb-5)).

:::satz Teorem 2.5 (Lojistik fonksiyonun türevi)
<span class="anker" id="satz-2-5"></span>

Şu geçerlidir:

<span class="anker" id="gl-2-4"></span>
$$\sigma'(x)=\sigma(x)\,\bigl(1-\sigma(x)\bigr). \tag{2.4}$$

Türev her yerde pozitiftir ve en fazla $\tfrac14$ olur; en büyük değeri olan $\tfrac14$ değerini $0$ noktasında alır.
:::

:::herleitung Lojistik fonksiyonun türevi
Fonksiyon üç halkalı bir zincirdir: $u_1=-x$, $u_2=1+\mathrm{e}^{u_1}$, $\sigma=1/u_2$. Çarpanlar $-1$, $\mathrm{e}^{u_1}=\mathrm{e}^{-x}$ ve $-1/u_2^2$ olur. [(2.2)](#gl-2-2) uyarınca

$$\sigma'(x)=-\frac1{(1+\mathrm{e}^{-x})^2}\cdot\mathrm{e}^{-x}\cdot(-1)=\frac{\mathrm{e}^{-x}}{(1+\mathrm{e}^{-x})^2}=\frac1{1+\mathrm{e}^{-x}}\cdot\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}} .$$

İlk çarpan $\sigma(x)$ olur. İkincisi $\frac{(1+\mathrm{e}^{-x})-1}{1+\mathrm{e}^{-x}}=1-\sigma(x)$ olur. $\sigma(x)$, $0$ ile $1$ arasında olduğundan iki çarpan da pozitiftir. $0$ ile $1$ arasındaki bir $p$ sayısı için $p\,(1-p)=\tfrac14-(p-\tfrac12)^2\le\tfrac14$ olur; eşitlik tam olarak $p=\tfrac12$ için, yani $x=0$ için sağlanır.
:::

:::abbildung ml/k3logistisch 5
Lojistik fonksiyon $\sigma$ (mavi) $0$'dan $1$'e yükselir, en dik olarak $0$ noktasında. Türevi (kırmızı) orada en büyük değerine, $\tfrac14$ değerine ulaşır ve iki yana doğru hızla küçülür. Sayısal örnekteki $0$ ve $2$ noktalarındaki değerler işaretlenmiştir.
:::

::::beispiel [Sayısal örnek]
$2$ noktasında $\mathrm{e}^{-2}\approx0{,}1353$, dolayısıyla $\sigma(2)\approx1/1{,}1353\approx0{,}8808$ ve

$$\sigma'(2)=\sigma(2)\,\bigl(1-\sigma(2)\bigr)\approx0{,}8808\cdot0{,}1192\approx0{,}1050 .$$

$\sigma(2)$ bir kez hesaplandıktan sonra türev yalnızca bir çıkarma ve bir çarpmaya mal olur, ek bir üstel fonksiyon hesabı gerekmez. $10$ noktasında $\sigma(10)\approx0{,}99995$ ve $\sigma'(10)\approx0{,}0000454$ olur: Çok dışarıda fonksiyon neredeyse yataydır, girdideki küçük değişimler çıktıya neredeyse hiç ulaşmaz.
::::

⁠**Kısacası:** $\sigma(x)=1/(1+\mathrm{e}^{-x})$ lojistik fonksiyonu her sayıyı düzgünce $0$ ile $1$ arasındaki aralığa gönderir; türevi $\sigma(1-\sigma)$, en fazla $\tfrac14$ olur ve yalnızca fonksiyon değerinden hesaplanabilir.

:::aufgabe Alıştırma 5 ★ Çan eğrisi
<span class="anker" id="aufg-5"></span>

$f(x)=\mathrm{e}^{-x^2}$ olsun.

<ol class="al">

<li>

İç ve dış fonksiyonu belirleyin ve $f'(x)$ türevini hesaplayın.

</li>

<li>

$f'(0)$, $f'(1)$ ve $f'(-1)$ değerlerini hesaplayın ve işaretleri grafik üzerinde yorumlayın.

</li>

</ol>

:::loesung
(a) İç fonksiyon $u=-x^2$, türevi $u'=-2x$; dış fonksiyon $\mathrm{e}^u$, türevi $\mathrm{e}^u$. Zincir kuralı uyarınca $f'(x)=\mathrm{e}^{-x^2}\cdot(-2x)=-2x\,\mathrm{e}^{-x^2}$ olur.

(b) $f'(0)=0$: Grafiğin $0$ noktasında yatay bir teğeti vardır, tepesi oradadır. $f'(1)=-2/\mathrm{e}\approx-0{,}7358$: Tepenin sağında grafik iner. $f'(-1)=2/\mathrm{e}\approx0{,}7358$: Tepenin solunda grafik yükselir. $f(-x)=f(x)$ olduğundan $\pm1$ noktalarındaki eğimler aynı büyüklükte ve zıt işaretlidir.
:::
:::

:::aufgabe Alıştırma 6 ★★ Üç halkalı bir zincir
<span class="anker" id="aufg-6"></span>

$y=\sqrt{1+x^4}$ olsun.

<ol class="al">

<li>

Fonksiyonu $u_1$, $u_2$, $y$ olmak üzere üç halkaya ayırın ve $x=1$ noktasında önce bütün ara değerleri, sonra bütün çarpanları hesaplayın.

</li>

<li>

$1$ noktasında $\frac{\mathrm{d} y}{\mathrm{d} x}$ türevini çarpanların çarpımı olarak hesaplayın ve zincir kuralını tek adımda uygulayarak sağlamasını yapın.

</li>

</ol>

:::loesung
(a) Halkalar: $u_1=x^4$, $u_2=1+u_1$ ve $y=\sqrt{u_2}$. $1$ noktasında ara değerler $u_1=1$, $u_2=2$ ve $y=\sqrt2\approx1{,}4142$ olur. Çarpanlar ise $\frac{\mathrm{d} u_1}{\mathrm{d} x}=4x^3=4$, $\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=1$ ve $\frac{\mathrm{d} y}{\mathrm{d} u_2}=\frac1{2\sqrt{u_2}}=\frac1{2\sqrt2}\approx0{,}3536$ olur.

(b) Çarpım $4\cdot1\cdot\frac1{2\sqrt2}=\frac2{\sqrt2}=\sqrt2\approx1{,}4142$ olur. Tek adımda: $y'=\frac1{2\sqrt{1+x^4}}\cdot4x^3$, dolayısıyla $1$ noktasında $\frac4{2\sqrt2}=\sqrt2$.
:::
:::

:::aufgabe Alıştırma 7 ★★ Lojistik fonksiyonun özellikleri
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

[(2.4)](#gl-2-4) ve $\sigma(-x)=1-\sigma(x)$ yardımıyla $\sigma'(-x)=\sigma'(x)$ olduğunu gösterin. Bu, $\sigma'$ grafiği için ne anlama gelir?

</li>

<li>

$\sigma(1)$ ve $\sigma'(1)$ değerlerini dört basamakla hesaplayın.

</li>

<li>

$\sigma''$ ikinci türevini $\sigma$ cinsinden hesaplayın ve işaretini $x>0$ ve $x<0$ için belirleyin. Bu, $\sigma$ grafiğinin eğriliği hakkında ne söyler?

</li>

</ol>

:::loesung
(a) $\sigma(-x)=1-\sigma(x)$ ile $\sigma'(-x)=\sigma(-x)\,\bigl(1-\sigma(-x)\bigr)=\bigl(1-\sigma(x)\bigr)\,\sigma(x)=\sigma'(x)$ olur. Şekil [5](#abb-5) içinde de görüldüğü gibi $\sigma'$ grafiği düşey eksene göre simetriktir.

(b) $\mathrm{e}^{-1}\approx0{,}3679$, dolayısıyla $\sigma(1)=1/1{,}3679\approx0{,}7311$ ve $\sigma'(1)\approx0{,}7311\cdot0{,}2689\approx0{,}1966$.

(c) Çarpım ve zincir kuralıyla: $\sigma''=(\sigma-\sigma^2)'=\sigma'-2\sigma\sigma'=\sigma'\,(1-2\sigma)=\sigma(1-\sigma)(1-2\sigma)$. $x>0$ için $\sigma>\tfrac12$, dolayısıyla $1-2\sigma<0$ ve $\sigma''<0$ olur: Grafik orada aşağı doğru bükülür. $x<0$ için $\sigma''>0$ olur ve grafik yukarı doğru bükülür. $0$ noktasında eğrilik işaret değiştirir; eğim en büyük değerini orada alır.
:::
:::

:::aufgabe Alıştırma 8 ★★★ Bir ters fonksiyonun türevi
<span class="anker" id="aufg-8"></span>

$x>0$ için $\mathrm{e}^{\ln x}=x$ geçerlidir.

<ol class="al">

<li>

$\ln$ fonksiyonunun türevlenebilir olduğunu varsayarak iki tarafın da zincir kuralıyla $x$'e göre türevini alın ve $(\ln x)'=1/x$ sonucunu çıkarın.

</li>

<li>

Aynısını $(\sqrt x)^2=x$ ile yapın ve kuvvet kuralıyla karşılaştırın.

</li>

<li>

$0<p<1$ için lojistik fonksiyonun ters fonksiyonu $\ell(p)=\ln\frac{p}{1-p}$ olur. $\ell(\sigma(x))=x$ eşitliğini doğrulayın ve $\ell'(p)$ türevini bir kez doğrudan, bir kez de $\sigma'$ üzerinden hesaplayın.

</li>

</ol>

:::loesung
(a) Sol taraf, iç fonksiyonu $\ln x$, dış fonksiyonu $\mathrm{e}^u$ olan bir bileşkedir. Zincir kuralı uyarınca türevi $\mathrm{e}^{\ln x}\cdot(\ln x)'=x\cdot(\ln x)'$ olur. Sağ tarafın türevi $1$'dir. Dolayısıyla $x\,(\ln x)'=1$ ve $(\ln x)'=1/x$.

(b) $(\sqrt x)^2=x$ eşitliğinden $2\sqrt x\cdot(\sqrt x)'=1$, dolayısıyla $(\sqrt x)'=\frac1{2\sqrt x}=\tfrac12x^{-1/2}$ çıkar; bu, tam olarak $n=\tfrac12$ için kuvvet kuralıdır.

(c) $1-\sigma(x)=\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}}$ olur, dolayısıyla $\frac{\sigma(x)}{1-\sigma(x)}=\frac1{\mathrm{e}^{-x}}=\mathrm{e}^x$ ve $\ell(\sigma(x))=\ln\mathrm{e}^x=x$. Doğrudan hesapla $\ell(p)=\ln p-\ln(1-p)$ ve

$$\ell'(p)=\frac1p+\frac1{1-p}=\frac{1}{p\,(1-p)} .$$

$\sigma'$ üzerinden: $\ell(\sigma(x))=x$ eşitliğinin türevi alınınca $\ell'(\sigma(x))\cdot\sigma'(x)=1$, dolayısıyla $p=\sigma(x)$ ile $\ell'(p)=\frac1{\sigma'(x)}=\frac1{p(1-p)}$ bulunur. $\sigma$ nerede yatıksa ters fonksiyonu orada diktir.
:::
:::
