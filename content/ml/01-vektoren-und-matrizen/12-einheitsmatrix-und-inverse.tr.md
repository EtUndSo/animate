---
title: Birim matris ve ters matris
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
knoten: Temeller 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15211200
summary: Bazı doğrusal dönüşümler geri alınabilir, bazıları alınamaz.
tags: birim matrisi, tersinir, tersi, tekil
lang: tr
---

<span class="anker" id="stufe-11"></span>

:::zweck
Bazı doğrusal dönüşümler geri alınabilir, bazıları alınamaz. Bu kesim, hiçbir şeyi değiştirmeyen matrisi ve bir dönüşümü tersine çeviren ters matrisi tanıtıyor ve ters matrisin ne zaman var olduğunu açıklığa kavuşturuyor.
:::

### Birim matris

<span class="anker" id="stufe-11-1"></span>

Bütün doğrusal dönüşümler arasında hiçbir şey yapmayan bir dönüşüm vardır: Her vektörü kendisine götürür. [(8.2)](lineare-abbildungen.html#gl-8-2) uyarınca bu dönüşümün matrisinin sütunları birim vektörlerin görüntüleri, yani birim vektörlerin kendileridir.

:::definition Tanım 11.1 (Birim matris)
<span class="anker" id="satz-11-1"></span>

$\mathbf{I}_n\in\mathbb{R}^{n\times n}$ __birim matrisi__, köşegeninde yalnızca birler bulunan köşegen matristir. Sütunları $\mathbf{e}_1,\dots,\mathbf{e}_n$ vektörleridir.
:::

Tip açıksa kısaca $\mathbf{I}$ yazılır. Her $\mathbf{x}\in\mathbb{R}^n$ vektörü için $\mathbf{I}\mathbf{x}=\mathbf{x}$, her $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisi için de $\mathbf{A}\mathbf{I}_n=\mathbf{A}$ ve $\mathbf{I}_m\mathbf{A}=\mathbf{A}$ olur. Birim matris, matris çarpımında $1$ sayısının rolünü oynar.

::::beispiel [Sayısal örnek]
$$\mathbf{I}_3=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\qquad \mathbf{I}_3\begin{pmatrix}60\\2\\3\end{pmatrix}=\begin{pmatrix}60\\2\\3\end{pmatrix}.$$
::::

⁠**Kısacası:** Birim matrisin köşegeninde birler, başka her yerde sıfırlar vardır; bir dönüşüm olarak her vektörü değiştirmeden bırakır.

### Ters matris

<span class="anker" id="stufe-11-2"></span>

$90^\circ$ kadar bir dönme, $90^\circ$ geri döndürülerek geri alınır. İki katına germe, yarıya sıkıştırılarak geri alınır. İki durumda da birinciyi ortadan kaldıran ikinci bir dönüşüm vardır: Art arda uygulandıklarında ikisi birlikte hiçbir şey yapmaz.

:::definition Tanım 11.2 (Ters matris)
<span class="anker" id="satz-11-2"></span>

Şu eşitliği sağlayan bir $\mathbf{A}^{-1}\in\mathbb{R}^{n\times n}$ matrisi varsa $\mathbf{A}\in\mathbb{R}^{n\times n}$ kare matrisine __tersinir__ denir:

<span class="anker" id="gl-11-1"></span>
$$\mathbf{A}\mathbf{A}^{-1}=\mathbf{A}^{-1}\mathbf{A}=\mathbf{I} . \tag{11.1}$$

$\mathbf{A}^{-1}$ matrisine $\mathbf{A}$ matrisinin __tersi__ denir.
:::

Böyle en çok bir matris vardır. Gerçekten de $\mathbf{B}$ ve $\mathbf{C}$ ikisi de $\mathbf{A}$ matrisinin tersiyse $\mathbf{B}=\mathbf{B}\mathbf{I}=\mathbf{B}(\mathbf{A}\mathbf{C})=(\mathbf{B}\mathbf{A})\mathbf{C}=\mathbf{I}\mathbf{C}=\mathbf{C}$ olur. Bu yüzden *tek* bir tersten söz edilebilir. Ters bilinirse her $\mathbf{y}=\mathbf{A}\mathbf{x}$ sonucundan geriye doğru hesap yapılabilir: $\mathbf{A}^{-1}\mathbf{y}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{x}$.

::::beispiel [Sayısal örnek]
$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\begin{pmatrix}2-1&-2+2\\1-1&-1+2\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix},$$

ve öbür sırada da aynısı çıkar; dolayısıyla $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$ olur. Germenin tersi $\operatorname{diag}(2;\,0{,}5)^{-1}=\operatorname{diag}(0{,}5;\,2)$, $90^\circ$ kadar dönmenin tersi de $-90^\circ$ kadar dönmedir, $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$.
::::

⁠**Kısacası:** $\mathbf{A}^{-1}$ tersi, $\mathbf{A}$ dönüşümünü geri alır: $\mathbf{A}^{-1}\mathbf{A}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$.

:::hintergrund Bir köşegen matrisin tersi
Bir $\operatorname{diag}(\mathbf{v})$ köşegen matrisi her bileşeni kendi $v_j$ çarpanıyla çarpar. Bu işlem, her bileşen kendi çarpanına bölünerek geri alınır: $\operatorname{diag}(\mathbf{v})^{-1}=\operatorname{diag}(1/v_1,\dots,1/v_n)$. Bu ancak ve ancak hiçbir çarpan sıfır değilse mümkündür. $v_j=0$ çarpanı $j$ numaralı bileşeni siler ve silineni hiçbir hesap geri getiremez.
:::

### $2\times2$ tipinde bir matrisin tersi

<span class="anker" id="stufe-11-3"></span>

$2\times2$ tipindeki matrisler için basit bir formül vardır. İki köşegen elemanının yeri değiştirilir, öbür iki elemanın önüne eksi işareti konur ve dört elemanın hepsinden oluşturulan bir sayıya bölünür.

:::satz Teorem 11.3 ($2\times2$ tipinde bir matrisin tersi)
<span class="anker" id="satz-11-3"></span>

$\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ matrisi ancak ve ancak $ad-bc\ne0$ ise tersinirdir ve o zaman tersi şudur:

<span class="anker" id="gl-11-2"></span>
$$\mathbf{A}^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}. \tag{11.2}$$
:::

:::herleitung $2\times2$ tipinde bir matrisin tersi
Çarpım açık açık yazılırsa şu bulunur:

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}=\begin{pmatrix}ad-bc&-ab+ba\\cd-dc&-cb+da\end{pmatrix}=(ad-bc)\,\mathbf{I} ,$$

ve öbür sırada da aynısı çıkar. $ad-bc\ne0$ ise bu sayıya bölünür ve [(11.1)](#gl-11-1) elde edilir. $ad-bc=0$ ise $\mathbf{A}$ matrisi $(d,\,-c)^{\top}$ vektörünü $(ad-bc,\ cd-dc)^{\top}=\mathbf{0}$ vektörüne, aynı biçimde $(b,\,-a)^{\top}$ vektörünü de $\mathbf{0}$ vektörüne götürür. Dört elemanın hepsi sıfır olmadıkça bu iki vektörden en az biri sıfır vektörü değildir; dördü de sıfırsa $\mathbf{A}$ zaten sıfır matristir. Ama bir $\mathbf{x}\ne\mathbf{0}$ vektörünü $\mathbf{0}$ vektörüne götüren bir matrisin tersi yoktur: Olsaydı $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$ olurdu.
:::

::::beispiel [Sayısal örnek]
$\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ için $ad-bc=2-1=1$ olur, dolayısıyla tersi, yukarıdaki gibi $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$ matrisidir. $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ için $ad-bc=5$, tersi de $\tfrac15\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$ olur.
::::

⁠**Kısacası:** $2\times2$ tipinde bir matris ancak ve ancak $ad-bc\ne0$ ise tersinirdir; tersi $\frac{1}{ad-bc}\bigl(\begin{smallmatrix}d&-b\\-c&a\end{smallmatrix}\bigr)$ olur.

### Ters matrisler için hesap kuralları

<span class="anker" id="stufe-11-4"></span>

İki dönüşümü art arda uygulayıp bunu geri almak isteyen kişi önce ikincisini ortadan kaldırmalıdır. Bu yüzden bir çarpımın tersi alınırken sıra tersine döner.

:::satz Teorem 11.4 (Ters matrisler için hesap kuralları)
<span class="anker" id="satz-11-4"></span>

$\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ tersinir ve $c\ne0$ ise $\mathbf{A}\mathbf{B}$, $\mathbf{A}^{\top}$, $\mathbf{A}^{-1}$ ve $c\,\mathbf{A}$ da tersinirdir ve şunlar geçerlidir:

$$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1},\qquad(\mathbf{A}^{\top})^{-1}=(\mathbf{A}^{-1})^{\top},\qquad(\mathbf{A}^{-1})^{-1}=\mathbf{A},\qquad(c\,\mathbf{A})^{-1}=\tfrac1c\,\mathbf{A}^{-1}.$$
:::

:::herleitung Ters matrisler için hesap kuralları
Her seferinde adayla çarpımın birim matrisi verdiği kontrol edilir. Çarpım için: $(\mathbf{A}\mathbf{B})(\mathbf{B}^{-1}\mathbf{A}^{-1})=\mathbf{A}(\mathbf{B}\mathbf{B}^{-1})\mathbf{A}^{-1}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$, aynı biçimde $(\mathbf{B}^{-1}\mathbf{A}^{-1})(\mathbf{A}\mathbf{B})=\mathbf{I}$. Devrik için: $\mathbf{A}^{\top}(\mathbf{A}^{-1})^{\top}=(\mathbf{A}^{-1}\mathbf{A})^{\top}=\mathbf{I}^{\top}=\mathbf{I}$; öbür sırada da aynısı geçerlidir. Son iki kural doğrudan [(11.1)](#gl-11-1) eşitliğinden çıkar.
:::

İnsanın olmasını isteyeceği bir kural ise geçerli değildir: $(\mathbf{A}+\mathbf{B})^{-1}$ genel olarak $\mathbf{A}^{-1}+\mathbf{B}^{-1}$ değildir. Sayılar için bile $\frac{1}{2+4}=\frac16$, ama $\frac12+\frac14=\frac34$ olur.

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ ve $\mathbf{B}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ için $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$ ve $ad-bc=21-16=5$ olur, dolayısıyla $(\mathbf{A}\mathbf{B})^{-1}=\tfrac15\bigl(\begin{smallmatrix}3&-4\\-4&7\end{smallmatrix}\bigr)$. Aynı sonucu şu da verir:

$$\mathbf{B}^{-1}\mathbf{A}^{-1}=\tfrac15\begin{pmatrix}2&-1\\-1&3\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\tfrac15\begin{pmatrix}3&-4\\-4&7\end{pmatrix}.$$
::::

⁠**Kısacası:** Bir çarpımın tersi, terslerin ters sırayla alınmış çarpımıdır, $(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$.

:::hintergrund Ters sıra için bir resim
Sabah önce kazak, sonra ceket giyen kişi akşam önce ceketi, sonra kazağı çıkarır. Geri alma, adımları sondan başa doğru izler. $\mathbf{A}\mathbf{B}$ dönüşümü “önce $\mathbf{B}$, sonra $\mathbf{A}$” demektir; onu ortadan kaldırmak için önce $\mathbf{A}$, sonra $\mathbf{B}$ ortadan kaldırılmalıdır, yani önce $\mathbf{A}^{-1}$, sonra $\mathbf{B}^{-1}$ uygulanmalıdır. İlk uygulanan sağda olacak biçimde matris olarak yazılınca bu, $\mathbf{B}^{-1}\mathbf{A}^{-1}$ olur. Bu resim yalnızca sıra söz konusu olduğu ölçüde geçerlidir; bir tersin neden var olduğunu açıklamaz.
:::

### Ters matrisin olmadığı durum

<span class="anker" id="stufe-11-5"></span>

$\operatorname{diag}(1;\,0)$ matrisi düzlemi $x_1$ ekseni üzerine yassılaştırır (Şekil [32](lineare-abbildungen.html#abb-32)). $(1,\,5)^{\top}$ ve $(1,\,-2)^{\top}$ noktalarının ikisi de $(1,\,0)^{\top}$ noktasına gelir. Yalnızca $(1,\,0)^{\top}$ sonucunu gören kişi bu sonucun hangi noktadan geldiğini bilemez. İkinci bileşen kaybolmuştur ve hiçbir hesap onu geri getiremez.

:::satz Teorem 11.5 (Tersi olmayan matris)
<span class="anker" id="satz-11-5"></span>

$\mathbf{A}\mathbf{x}=\mathbf{0}$ olan bir $\mathbf{x}\ne\mathbf{0}$ vektörü varsa $\mathbf{A}$ tersinir değildir.
:::

:::beweis Tersi olmayan matris
Bir ters olsaydı $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$ olurdu; bu, $\mathbf{x}\ne\mathbf{0}$ ile çelişir.
:::

Sezgisel olarak: $\mathbf{A}\mathbf{x}=\mathbf{0}$ ise her $\mathbf{u}$ için birbirinden farklı $\mathbf{u}$ ve $\mathbf{u}+\mathbf{x}$ vektörleri aynı yere gelir, çünkü $\mathbf{A}(\mathbf{u}+\mathbf{x})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{x}=\mathbf{A}\mathbf{u}$. Çıkışı aynı olan iki giriş birbirinden ayırt edilemez. Tersinir olmayan bir kare matrise __tekil__ denir.

::::beispiel [Sayısal örnek]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ için $ad-bc=4-4=0$ olur. Gerçekten de $\mathbf{x}=(2,\,-1)^{\top}$ vektörü $(2-2,\ 4-4)^{\top}=\mathbf{0}$ vektörüne gider ve birbirinden farklı $(1,\,1)^{\top}$ ve $(3,\,0)^{\top}$ vektörlerinin ikisi de $(3,\,6)^{\top}$ vektörüne gelir.
::::

Veriler için bu şu demektir: Örneğin yatak odaları ile oturma odalarından yalnızca oda toplamını oluşturan bir hesap, iki sayıyı artık birbirinden ayıramaz. $2\times2$ tipindeki matrislerde bu, tam olarak $ad-bc=0$ durumudur (alt kesim [11.3](#stufe-11-3)).

⁠**Kısacası:** Bir matris bir $\mathbf{x}\ne\mathbf{0}$ vektörünü $\mathbf{0}$ vektörüne götürüyorsa bilgi kaybeder ve tersi yoktur; o zaman ona tekil denir.

:::aufgabe Alıştırma 26 ★ Ters matris hesaplamak
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

$\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$ ve $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ matrislerinin terslerini hesaplayın ve her birini kontrol edin.

</li>

<li>

Hangi $t$ sayısı için $\bigl(\begin{smallmatrix}2&t\\4&6\end{smallmatrix}\bigr)$ tersinir değildir? Bu durum için $\mathbf{A}\mathbf{x}=\mathbf{0}$ olan bir $\mathbf{x}\ne\mathbf{0}$ vektörü verin.

</li>

<li>

$\operatorname{diag}(4;\,-1;\,0{,}5)$ matrisinin tersini verin.

</li>

</ol>

:::loesung
(a) $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$ için $ad-bc=4-3=1$ olur, tersi $\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)$. Sağlama: $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4-3&-12+12\\1-1&-3+4\end{smallmatrix}\bigr)=\mathbf{I}$. $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ için $ad-bc=4-6=-2$ olur, tersi $-\tfrac12\bigl(\begin{smallmatrix}4&-2\\-3&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)$. Sağlama: $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2+3&1-1\\-6+6&3-2\end{smallmatrix}\bigr)=\mathbf{I}$.

(b) $t=3$ için $ad-bc=12-4t=0$ olur. Bu durumda matris $\bigl(\begin{smallmatrix}2&3\\4&6\end{smallmatrix}\bigr)$ olur; ikinci satırı birincinin iki katıdır. $(3,\,-2)^{\top}$ vektörü $(6-6,\ 12-12)^{\top}=\mathbf{0}$ vektörüne gönderilir.

(c) $\operatorname{diag}(4;\,-1;\,0{,}5)^{-1}=\operatorname{diag}(0{,}25;\,-1;\,2)$: Her köşegen elemanının yerine çarpmaya göre tersi konur.
:::
:::

:::aufgabe Alıştırma 27 ★★ Ters matrislerle akıl yürütmek
<span class="anker" id="aufg-27"></span>

<ol class="al">

<li>

$\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ için $(\mathbf{C}^{\top})^{-1}=(\mathbf{C}^{-1})^{\top}$ eşitliğini kontrol edin.

</li>

<li>

$\mathbf{A}$ tersinir ve $\mathbf{A}\mathbf{B}=\mathbf 0$ olsun. O zaman $\mathbf{B}=\mathbf 0$ olduğunu gösterin.

</li>

<li>

Sayılarda $ab=0$ eşitliğinden $a=0$ ya da $b=0$ çıkar. $\mathbf{A}=\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$ ile bunun matrisler için geçerli olmadığını gösterin. Bu neden (b) ile çelişmez?

</li>

</ol>

:::loesung
(a) Önceki alıştırmadan $\mathbf{C}^{-1}=\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)$, dolayısıyla $(\mathbf{C}^{-1})^{\top}=\bigl(\begin{smallmatrix}-2&1{,}5\\1&-0{,}5\end{smallmatrix}\bigr)$ olur. Öte yandan $\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)$ için $ad-bc=-2$, dolayısıyla $(\mathbf{C}^{\top})^{-1}=-\tfrac12\bigl(\begin{smallmatrix}4&-3\\-2&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1{,}5\\1&-0{,}5\end{smallmatrix}\bigr)$ olur. İkisi aynıdır.

(b) $\mathbf{A}\mathbf{B}=\mathbf 0$ eşitliği soldan $\mathbf{A}^{-1}$ ile çarpılır: $\mathbf{B}=\mathbf{I}\mathbf{B}=\mathbf{A}^{-1}\mathbf{A}\mathbf{B}=\mathbf{A}^{-1}\mathbf 0=\mathbf 0$.

(c) $\mathbf{A}\ne\mathbf 0$ olduğu hâlde $\mathbf{A}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}0\cdot0+1\cdot0&0\cdot1+1\cdot0\\0&0\end{smallmatrix}\bigr)=\mathbf 0$. Geometrik olarak $\mathbf{A}$, $\mathbf{e}_2$ vektörünü $\mathbf{e}_1$ vektörüne, $\mathbf{e}_1$ vektörünü de $\mathbf{0}$ vektörüne gönderir; iki kez uygulanınca her şey sıfır vektörüne varır. Bu, (b) ile çelişmez, çünkü $\mathbf{A}$ tersinir değildir: $ad-bc=0$. (b) şıkkındaki çıkarım ters matrise dayanır.
:::
:::
