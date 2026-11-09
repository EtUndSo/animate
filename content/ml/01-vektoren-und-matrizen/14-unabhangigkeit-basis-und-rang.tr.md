---
title: Bağımsızlık, taban ve rank
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
knoten: Temeller 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15211400
summary: Bir listedeki bazı vektörler yeni bir şey getirmez, çünkü ötekilerden oluşturulabilirler.
tags: gerilen alt uzay, doğrusal bağımsız, doğrusal bağımlı, tabanı, boyutu, standart tabanı, rankı, tam ranklı
lang: tr
---

<span class="anker" id="stufe-13"></span>

:::zweck
Bir listedeki bazı vektörler yeni bir şey getirmez, çünkü ötekilerden oluşturulabilirler. Bu kesim, bir matriste gerçekten kaç farklı doğrultu bulunduğunu ölçüyor ve öznitelikler aynı bilgiyi iki kez taşıdığında bunun veriler için ne anlama geldiğini gösteriyor.
:::

### Gerilen alt uzay

<span class="anker" id="stufe-13-1"></span>

Bir matrisin sütun uzayı, sütunlarının bütün doğrusal bileşimlerinin kümesidir. Aynı yapı her vektör listesi için bir küme verir ve bu kümeye ayrı bir ad verilir (Şekil [39](#abb-39)).

:::abbildung ml/k1spann 39
Düzlemdeki üç vektör listesinin gerdiği alt uzay (mavi), $1:2$ ölçeğinde. (a) Bir vektör orijinden geçen bir doğru gerer. (b) Aynı doğru üzerindeki ikinci bir vektör hiçbir şeyi değiştirmez. (c) Farklı doğrultulardaki iki vektör bütün düzlemi gerer.
:::

:::definition Tanım 13.1 (Gerilen alt uzay)
<span class="anker" id="satz-13-1"></span>

$\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^d$ vektörleri tarafından __gerilen alt uzay__ (*span*), bu vektörlerin bütün doğrusal bileşimlerinin kümesidir:

<span class="anker" id="gl-13-1"></span>
$$\operatorname{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}=\Bigl\{\sum_{l=1}^kc_l\,\mathbf{v}_l\ :\ c_1,\dots,c_k\in\mathbb{R}\Bigr\}. \tag{13.1}$$
:::

Demek ki bir matrisin sütun uzayı, sütunlarının gerdiği alt uzaydır. Gerilen alt uzayda iki vektör varsa onların her doğrusal bileşimi de oradadır; toplayarak ve bir sayıyla çarparak bu alt uzaydan hiçbir zaman çıkılmaz.

⁠**Sayısal örnek:** $\operatorname{span}\{(1,\,2)^{\top}\}$, bütün $c\,(1,\,2)^{\top}$ katlarından oluşan doğrudur. $(1,\,2)^{\top}$ ve $(2,\,4)^{\top}$ vektörlerinin gerdiği alt uzay aynı doğrudur, çünkü $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$. $(1,\,0)^{\top}$ ve $(1,\,1)^{\top}$ vektörlerinin gerdiği alt uzay bütün düzlemdir: Her $(y_1,\,y_2)^{\top}$ vektörü $(y_1-y_2)\,(1,\,0)^{\top}+y_2\,(1,\,1)^{\top}$ olarak yazılır. $\mathbb{R}^3$ uzayında $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$, $x_3=0$ olan bütün vektörlerin oluşturduğu düzlemdir.

⁠**Kısacası:** Bir vektör listesinin gerdiği alt uzay, bu vektörlerden doğrusal bileşimle elde edilebilen her şeydir.

### Doğrusal bağımsızlık

<span class="anker" id="stufe-13-2"></span>

Şekil [39](#abb-39) (b) durumunda ikinci vektör yeni bir şey getirmez: Birincinin gerdiği alt uzayda zaten bulunur. Bir veri kümesi de aynı zayıflığa sahip olabilir. Veri kümesi yatak odası sayısını, oturma odası sayısını ve bütün odaların sayısını içeriyorsa üçüncü sütun ilk ikisinin toplamıdır ve kendine ait bir bilgi taşımaz. Bir vektör listesinde hiçbir şeyin fazla olmadığını anlatan bir sözcüğe ihtiyaç vardır.

:::definition Tanım 13.2 (Doğrusal bağımsızlık)
<span class="anker" id="satz-13-2"></span>

$\mathbf{v}_1,\dots,\mathbf{v}_k$ vektörleri için

<span class="anker" id="gl-13-2"></span>
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k=\mathbf{0} \tag{13.2}$$

eşitliği yalnızca $c_1=c_2=\dots=c_k=0$ için sağlanıyorsa bu vektörlere __doğrusal bağımsız__ denir. Aksi hâlde __doğrusal bağımlı__ denir.
:::

Doğrusal bağımlı olmak şuna denktir: Vektörlerden en az biri ötekilerin bir doğrusal bileşimidir. Çünkü [(13.2)](#gl-13-2) eşitliği bir $c_l\ne0$ katsayısıyla sağlanıyorsa eşitlik $\mathbf{v}_l$ için çözülebilir: $\mathbf{v}_l=-\sum_{l'\ne l}(c_{l'}/c_l)\,\mathbf{v}_{l'}$. Tersine, böyle bir gösterim hemen $\mathbf{v}_l$ önünde $-1$ katsayısı bulunan bir bileşim verir.

⁠**Sayısal örnek:** $(1,\,2)^{\top}$ ve $(2,\,4)^{\top}$ doğrusal bağımlıdır: $2\,(1,\,2)^{\top}-(2,\,4)^{\top}=\mathbf{0}$. $(1,\,0)^{\top}$ ve $(1,\,1)^{\top}$ vektörleri doğrusal bağımsızdır: $c_1(1,\,0)^{\top}+c_2(1,\,1)^{\top}=(c_1+c_2,\ c_2)^{\top}=\mathbf{0}$ eşitliğinden önce $c_2=0$, sonra $c_1=0$ çıkar. $(1,\,0,\,1)^{\top}$, $(0,\,1,\,1)^{\top}$ ve $(1,\,1,\,2)^{\top}$ vektörleri doğrusal bağımlıdır, çünkü üçüncüsü ilk ikisinin toplamıdır.

⁠**Kısacası:** Doğrusal bağımsız şu demektir: Vektörlerin hiçbiri ötekilerden bileşim olarak elde edilemez, gereksiz tekrar yoktur.

### Taban ve boyut

<span class="anker" id="stufe-13-3"></span>

Gerilen bir alt uzay olabildiğince kısa betimlenmek istenirse gerektiği kadar az, ama her şeye ulaşmaya yetecek kadar vektör alınır. Böyle bir liste bir koordinat sistemi gibidir: O zaman alt uzaydaki her vektörün bu liste cinsinden tam olarak bir gösterimi vardır.

:::definition Tanım 13.3 (Taban, boyut)
<span class="anker" id="satz-13-3"></span>

Gerdiği alt uzay bir $\mathcal S$ kümesi olan, doğrusal bağımsız vektörlerden oluşan bir listeye $\mathcal S$ kümesinin bir __tabanı__ denir. Bir tabandaki vektörlerin sayısına $\mathcal S$ kümesinin __boyutu__ denir ve $\dim\mathcal S$ diye yazılır.
:::

Bir $\mathcal S$ kümesinin birçok farklı tabanı vardır, ama hepsi aynı sayıda vektörden oluşur; bu, boyut tanımının dayandığı bir doğrusal cebir teoremidir. $\mathbf{e}_1,\dots,\mathbf{e}_d$ birim vektörleri $\mathbb{R}^d$ uzayının bir tabanını, __standart tabanı__ oluşturur; bu yüzden $\dim\mathbb{R}^d=d$ olur.

:::satz Teorem 13.4 (Tek türlü belirli koordinatlar)
<span class="anker" id="satz-13-4"></span>

$\mathbf{v}_1,\dots,\mathbf{v}_k$, $\mathcal S$ kümesinin bir tabanıysa her $\mathbf{x}\in\mathcal S$ vektörünün tam olarak bir $\mathbf{x}=\sum_lc_l\mathbf{v}_l$ gösterimi vardır.
:::

:::beweis Tek türlü belirli koordinatlar
En az bir gösterim vardır, çünkü taban $\mathcal S$ kümesini gerer. İki gösterim olsaydı, $\sum_lc_l\mathbf{v}_l=\sum_lc_l'\mathbf{v}_l$, bunların farkı $\sum_l(c_l-c_l')\mathbf{v}_l=\mathbf{0}$ olurdu. Doğrusal bağımsızlık yüzünden o zaman bütün $c_l-c_l'=0$ olur.
:::

⁠**Sayısal örnek:** $(1,\,0)^{\top}$ ve $(1,\,1)^{\top}$, $\mathbb{R}^2$ uzayının bir tabanını oluşturur: Doğrusal bağımsızdırlar ve düzlemi gererler. $(3,\,2)^{\top}$ vektörünün bu tabandaki koordinatları $1$ ve $2$ olur, çünkü $(3,\,2)^{\top}=1\cdot(1,\,0)^{\top}+2\cdot(1,\,1)^{\top}$. $\operatorname{span}\{(0,\,1)^{\top}\}$ doğrusunun vektörlerinin iki bileşeni olmasına rağmen bu doğrunun boyutu $1$ olur.

⁠**Kısacası:** Bir taban, her şeyi geren bağımsız vektörlerden oluşan bir listedir; listenin uzunluğu boyuttur.

### Bir matrisin rankı

<span class="anker" id="stufe-13-4"></span>

$n$ sütunlu bir matris, gerçekten farklı $n$ taneden az doğrultu içerebilir. Fazla olan her şey atıldığında geriye kalan doğrultuların sayısı, bir matrisin gerçekte ne kadar iş gördüğünü söyler.

:::definition Tanım 13.5 (Rank)
<span class="anker" id="satz-13-5"></span>

Bir $\mathbf{A}$ matrisinin $\operatorname{rank}\mathbf{A}$ __rankı__, $\mathbf{A}$ matrisinin doğrusal bağımsız sütunlarının en büyük sayısıdır. Rank, matrisin sütun uzayının boyutuna eşittir.
:::

:::satz Teorem 13.6 (Sütun rankı eşittir satır rankı)
<span class="anker" id="satz-13-6"></span>

Bir matrisin doğrusal bağımsız sütunlarının en büyük sayısı, doğrusal bağımsız satırlarının en büyük sayısına eşittir. Özellikle $\mathbf{A}\in\mathbb{R}^{m\times n}$ için $\operatorname{rank}\mathbf{A}=\operatorname{rank}\mathbf{A}^{\top}\le\min(m,n)$ olur.
:::

$\operatorname{rank}\mathbf{A}=\min(m,n)$ ise $\mathbf{A}$ matrisine __tam ranklı__ denir. Uygulamada rank Gauss eleme yöntemiyle belirlenir: Satır işlemleri rankı değiştirmez ve satır basamak biçiminde rank, tamamı sıfırlardan oluşmayan satırların sayısıdır.

⁠**Sayısal örnek:** $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ matrisinin rankı $1$ olur: İkinci sütun birincinin iki katıdır, aynı biçimde ikinci satır da birincinin iki katıdır.

$$\mathbf K=\begin{pmatrix}1&0&1\\0&1&1\\1&1&2\end{pmatrix}$$

matrisinde birinci ve ikinci satır üçüncü satırdan çıkarılırsa $(1,0,1)$, $(0,1,1)$, $(0,0,0)$ satırları elde edilir. İki satır sıfır değildir, dolayısıyla $\operatorname{rank}\mathbf K=2$ olur; gerçekten de üçüncü sütun ilk ikisinin toplamıdır. Dairelerin veri matrisi tam ranklıdır, rankı $3$ olur.

⁠**Kısacası:** Rank, bir matrisin sütunlarında gerçekten kaç farklı doğrultu bulunduğunu sayar ve bu sayı satırlarındakiyle aynıdır.

:::hintergrund Neden bağımsız sütun sayısı kadar bağımsız satır vardır?
Bu apaçık değildir: $3\times5$ tipinde bir matrisin satırları ve sütunları bambaşka uzaylarda yaşar. Kısa bir gerekçe şöyledir. $\mathbf{A}$ matrisinin $r$ sütunu doğrusal bağımsız olsun ve öbür her sütun bunların bir doğrusal bileşimi olsun. Bu $r$ sütun bir $\mathbf G\in\mathbb{R}^{m\times r}$ matrisi oluşturur. O zaman $\mathbf{A}$ matrisinin her $\mathbf{a}_j$ sütunu, $\mathbf G$ çarpı $r$ bileşenli bir katsayı vektörüdür. Bu katsayı vektörleri bir $\mathbf F\in\mathbb{R}^{r\times n}$ matrisinin sütunları olarak yazılırsa [(9.2)](das-matrixprodukt.html#gl-9-2) uyarınca $\mathbf{A}=\mathbf G\mathbf F$ olur. Şimdi aynı çarpım satır satır okunur: $\mathbf{A}$ matrisinin $i$ numaralı satırı, $\mathbf G$ matrisinin $i$ numaralı satırı çarpı $\mathbf F$, yani $\mathbf F$ matrisinin $r$ satırının bir doğrusal bileşimidir. Demek ki $\mathbf{A}$ matrisinin bütün satırları, $\mathbf F$ matrisinin $r$ satırının gerdiği alt uzayda, yani boyutu en çok $r$ olan bir kümede bulunur; bu yüzden bu satırlardan $r$ taneden fazlası doğrusal bağımsız olamaz. Demek ki satırlarda en çok sütunlardaki kadar bağımsız doğrultu vardır. Aynı gerekçe, sütunları $\mathbf{A}$ matrisinin satırları olan $\mathbf{A}^{\top}$ matrisine uygulanırsa ters eşitsizlik çıkar. Demek ki iki sayı eşittir.
:::

### Çekirdek ve rank-sıfırlık teoremi

<span class="anker" id="stufe-13-5"></span>

$n$ sütunlu bir matris $n$ doğrultudan gelen vektörleri alır. Bu doğrultuların bir kısmı sonuca ulaşır, geri kalanı sıfır vektörüne gider ve kaybolur. Kaybolan doğrultular ayrı bir küme oluşturur.

:::definition Tanım 13.7 (Çekirdek)
<span class="anker" id="satz-13-7"></span>

Bir $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisinin __çekirdeği__, $\mathbf{A}$ matrisinin sıfır vektörüne götürdüğü bütün vektörlerin kümesidir:

<span class="anker" id="gl-13-3"></span>
$$\ker\mathbf{A}=\{\mathbf{x}\in\mathbb{R}^n:\ \mathbf{A}\mathbf{x}=\mathbf{0}\} . \tag{13.3}$$
:::

Çekirdek, homojen sistemin çözüm kümesidir (alt kesim [12.4](lineare-gleichungssysteme.html#stufe-12-4)). Her zaman sıfır vektörünü içerir ve iki vektörü içeriyorsa onların her doğrusal bileşimini de içerir; dolayısıyla çekirdeğin boyutundan söz edilebilir.

:::satz Teorem 13.8 (Rank-sıfırlık teoremi)
<span class="anker" id="satz-13-8"></span>

Her $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisi için şu geçerlidir:

<span class="anker" id="gl-13-4"></span>
$$\dim\ker\mathbf{A}+\operatorname{rank}\mathbf{A}=n . \tag{13.4}$$
:::

Girişin $n$ doğrultusu paylaşılır: Sonuca ulaşmayan, çekirdeğe düşer. Gauss eleme yönteminde bu şöyle görülür: Satır basamak biçiminde $\operatorname{rank}\mathbf{A}$ tane pivot vardır. Geri kalan $n-\operatorname{rank}\mathbf{A}$ bilinmeyenin kendi pivotu yoktur ve bunlar homojen sistemde serbestçe seçilebilir. Bunların her biri çekirdeğin bir doğrultusunu verir.

:::satz Teorem 13.9 (Bir kare matris ne zaman tersinirdir?)
<span class="anker" id="satz-13-9"></span>

$\mathbf{A}\in\mathbb{R}^{n\times n}$ için şunlar denktir: (i) $\mathbf{A}$ tersinirdir; (ii) $\ker\mathbf{A}=\{\mathbf{0}\}$; (iii) $\operatorname{rank}\mathbf{A}=n$; (iv) $\mathbf{A}$ matrisinin sütunları doğrusal bağımsızdır.
:::

:::beweis Tersinirlik
(i) koşulundan (ii) çıkar (alt kesim [11.5](einheitsmatrix-und-inverse.html#stufe-11-5)). (ii), (iii) ve (iv), rank-sıfırlık teoremi ve rankın tanımı uyarınca denktir. Geriye şu kalır: (iii) ve (ii) koşullarından (i) çıkar. $\operatorname{rank}\mathbf{A}=n$ ise sütun uzayı, $\mathbb{R}^n$ içinde boyutu $n$ olan bir uzay, yani bütün $\mathbb{R}^n$ uzayıdır. Bu yüzden her $\mathbf{A}\mathbf{c}_j=\mathbf{e}_j$ sistemi çözülebilir ve çözümler, $\mathbf{A}\mathbf{C}=\mathbf{I}$ olan bir $\mathbf{C}$ matrisinin sütunlarını oluşturur. Ayrıca $\mathbf{A}(\mathbf{C}\mathbf{A}-\mathbf{I})=\mathbf{A}\mathbf{C}\mathbf{A}-\mathbf{A}=\mathbf 0$ olur. Demek ki $\mathbf{C}\mathbf{A}-\mathbf{I}$ matrisinin her sütunu, (ii) uyarınca yalnızca sıfır vektörünü içeren çekirdektedir. Dolayısıyla $\mathbf{C}\mathbf{A}=\mathbf{I}$ de geçerlidir ve $\mathbf{C}=\mathbf{A}^{-1}$ olur.
:::

⁠**Sayısal örnek:** $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ matrisinin çekirdeği boyutu $1$ olan $\operatorname{span}\{(2,\,-1)^{\top}\}$, rankı da $1$ olur: $1+1=2$. Yukarıdaki $\mathbf K$ matrisinin çekirdeği $\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$ olur, çünkü üçüncü sütunu ilk ikisinin toplamıdır; $\operatorname{rank}\mathbf K=2$ ile $1+2=3$ bulunur.

**Rank ve çözülebilirlik.** Rank ve çekirdek sayesinde doğrusal denklem sistemleriyle ilgili sorular (Kesim [12](lineare-gleichungssysteme.html#stufe-12)), kare olmayan matrisler için bile sayılardan okunabilir. Bir çözüm var mı? Tek mi? Her sağ taraf için bir çözüm var mı?

:::satz Teorem 13.10 (Çözülebilirlik ve rank)
<span class="anker" id="satz-13-10"></span>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ ve $\mathbf{y}\in\mathbb{R}^m$ için şunlar geçerlidir:

<ol class="rm">

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ ancak ve ancak $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=\operatorname{rank}\mathbf{A}$ ise çözülebilir;

</li>

<li>

sistem çözülebiliyorsa çözüm ancak ve ancak $\operatorname{rank}\mathbf{A}=n$ ise tektir;

</li>

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ ancak ve ancak $\operatorname{rank}\mathbf{A}=m$ ise her $\mathbf{y}\in\mathbb{R}^m$ için çözülebilir.

</li>

</ol>
:::

:::beweis Çözülebilirlik ve rank
(i) Alt kesim [12.2](lineare-gleichungssysteme.html#stufe-12-2) uyarınca sistem ancak ve ancak $\mathbf{y}$ vektörü $\mathbf{A}$ matrisinin sütun uzayındaysa çözülebilir. $\mathbf{y}$ bu uzaydaysa ek sütun yeni bir doğrultu getirmez: $(\mathbf{A}\,|\,\mathbf{y})$ matrisinin sütunları $\mathbf{A}$ matrisinin sütunlarıyla aynı uzayı gerer ve iki rank da bu uzayın boyutudur. $\mathbf{y}$ bu uzayda değilse $\mathbf{A}$ matrisinin $r=\operatorname{rank}\mathbf{A}$ tane doğrusal bağımsız $\mathbf g_1,\dots,\mathbf g_r$ sütunu ve bunlara ek olarak $\mathbf{y}$ alınır. $c_1\mathbf g_1+\dots+c_r\mathbf g_r+c\,\mathbf{y}=\mathbf{0}$ eşitliğinden $c=0$ çıkar, çünkü aksi hâlde $\mathbf{y}$, $\mathbf g_l$ sütunlarının bir doğrusal bileşimi olur ve sütun uzayında bulunurdu; o zaman bütün $c_l=0$ da olur. Demek ki $(\mathbf{A}\,|\,\mathbf{y})$ matrisinin en az $r+1$ doğrusal bağımsız sütunu vardır ve $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})>\operatorname{rank}\mathbf{A}$ olur.

(ii) Alt kesim [12.4](lineare-gleichungssysteme.html#stufe-12-4) uyarınca bütün çözümler, bir çözüm artı çekirdeğin vektörleridir. Demek ki çözüm ancak ve ancak $\ker\mathbf{A}=\{\mathbf{0}\}$ ise tektir ve rank-sıfırlık teoremine göre bu, $\operatorname{rank}\mathbf{A}=n$ demektir.

(iii) Her $\mathbf{y}$ ancak ve ancak sütun uzayı bütün $\mathbb{R}^m$ uzayıysa sütun uzayında bulunur. Bu, ancak ve ancak sütun uzayının boyutu $m$ ise, yani $\operatorname{rank}\mathbf{A}=m$ ise böyledir.
:::

$\operatorname{rank}\mathbf{A}=n=m$ olan bir kare matris için (ii) ve (iii) bir araya gelir: her sağ taraf için tam olarak bir çözüm; bu, tersinirlik teoremiyle uyumludur.

⁠**Sayısal örnek:** $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ için $\operatorname{rank}\mathbf{A}=1$ olur. $\mathbf{y}=(1,\,1)^{\top}$ ile genişletilmiş matrisin satırları $(1,\,2\,|\,1)$ ve $(2,\,4\,|\,1)$ olur; birincisi ikincisinden iki kez çıkarılırsa geriye $(0,\,0\,|\,-1)$ kalır, bu bir sıfır satırı değildir. Demek ki $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=2\ne1$ olur ve sistem, tıpkı alt kesim [12.2](lineare-gleichungssysteme.html#stufe-12-2) içindeki gibi çözülemez. $\mathbf{y}=(3,\,6)^{\top}$ ile ise geriye $(0,\,0\,|\,0)$ kalır, ranklar eşittir ve sistem çözülebilir. $\operatorname{rank}\mathbf{A}=1<2=n$ olduğundan çözüm tek değildir: Bütün çözümler $(1,\,1)^{\top}+t\,(2,\,-1)^{\top}$ biçimindedir. $\operatorname{rank}\mathbf{A}=1<2=m$ olduğundan da çözümü olmayan sağ taraflar vardır. Aşırı belirlenmiş sistemde (alt kesim [12.5](lineare-gleichungssysteme.html#stufe-12-5)) $\operatorname{rank}\mathbf{A}=2=n$ olur: Bir çözüm olsaydı tek olurdu. Ama çözüm yoktur, dolayısıyla orada (i) uyarınca $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=3$ olur.

⁠**Kısacası:** Çekirdek, bir matrisin sıfıra götürdüğü doğrultuları toplar; çekirdek ve rank, $n$ giriş doğrultusunu aralarında paylaşır. Bir $\mathbf{A}\mathbf{x}=\mathbf{y}$ sistemi ancak ve ancak sağ taraf rankı artırmıyorsa çözülebilir ve çözüm ancak ve ancak çekirdek yalnızca sıfır vektörünü içeriyorsa tektir.

### Bağımlı öznitelikler

<span class="anker" id="stufe-13-6"></span>

Gerçek veri kümelerinde öznitelikler bazen aynı bilgiyi iki kez taşır. Bir anket vücut ağırlığını kilogram olarak, başka bir değerlendirme için de bir kez daha libre olarak kaydeder. Bir ev tanımında zemin katın alanı, üst katın alanı ve toplam alan verilir. Veri matrisi için bu şu demektir: Sütunları doğrusal bağımlıdır ve rankı öznitelik sayısından küçüktür.

⁠**Sayısal örnek: zemin kat, üst kat, toplam alan.** Dört ev:

$$\mathbf{X}=\begin{pmatrix}50&40&90\\60&0&60\\45&45&90\\70&30&100\end{pmatrix}\qquad(\text{alanlar, birim: }\mathrm m^2).$$

Üçüncü sütun ilk ikisinin toplamıdır. Demek ki $\operatorname{rank}\mathbf{X}=2<3$ olur ve çekirdek $\mathbf k=(1,\,1,\,-1)^{\top}$ vektörünü içerir, çünkü $\mathbf{X}\mathbf k=\mathbf{0}$. Bundan iki sonuç çıkar.

<ul>

<li>

⁠**Ağırlıklar tek türlü belirli değildir.** Her $t$ sayısı için $\mathbf{w}$ ve $\mathbf{w}+t\,\mathbf k$ aynı tahminleri verir, çünkü $\mathbf{X}(\mathbf{w}+t\,\mathbf k)=\mathbf{X}\mathbf{w}+t\,\mathbf{X}\mathbf k=\mathbf{X}\mathbf{w}$. “Zemin katın ve üst katın metrekaresi başına $3$” anlamına gelen $(3,\,3,\,0)^{\top}$ ağırlıkları ile “toplam alanın metrekaresi başına $3$” anlamına gelen $(0,\,0,\,3)^{\top}$ ağırlıklarının ikisi de $(270,\,180,\,270,\,300)^{\top}$ verir. Yalnızca tahminlerden hangi ağırlıkların kastedildiği okunamaz ve bu ağırlıklardan tek birini yorumlamak anlamsızdır.

</li>

<li>

⁠**Özniteliklerin Gram matrisi tekildir.** $\mathbf{X}\mathbf k=\mathbf{0}$ eşitliğinden, $\mathbf k\ne\mathbf{0}$ ile $\mathbf{X}^{\top}\mathbf{X}\mathbf k=\mathbf{X}^{\top}\mathbf{0}=\mathbf{0}$ çıkar. O zaman $\mathbf{X}^{\top}\mathbf{X}$ matrisinin tersi yoktur (alt kesim [11.5](einheitsmatrix-und-inverse.html#stufe-11-5)).

</li>

</ul>

⁠**Sayısal örnek: kilogram ve libre.** Bir libre tam olarak $0{,}45359237$ kg eder; dolayısıyla libre cinsinden bir kütle, aynı kütlenin kilogram cinsinden değerinin $c=1/0{,}45359237\approx2{,}20462$ katıdır. Boyu (cm), kütlesi (kg) ve kütlesi (libre) verilmiş üç kişi:

$$\mathbf{X}=\begin{pmatrix}170&70&70\,c\\182&85&85\,c\\165&60&60\,c\end{pmatrix}\approx\begin{pmatrix}170&70&154{,}3\\182&85&187{,}4\\165&60&132{,}3\end{pmatrix}.$$

Üçüncü sütun ikincinin $c$ katıdır, dolayısıyla $\operatorname{rank}\mathbf{X}=2$ olur ve $(0,\,c,\,-1)^{\top}$ çekirdekte bulunur. Libre sütunu yeni bir bilgi getirmez, yalnızca var olan bir bilgiyi ikinci kez taşır.

⁠**Kısacası:** Öznitelikler aynı bilgiyi iki kez taşıyorsa veri matrisinin sütunları doğrusal bağımlıdır; o zaman rank $d$ değerinden küçüktür, farklı ağırlıklar aynı tahminleri verir ve $\mathbf{X}^{\top}\mathbf{X}$ tersinir değildir.

:::aufgabe Alıştırma 31 ★★ Rank ve çekirdek
<span class="anker" id="aufg-31"></span>

Şu matrislerin rankını ve çekirdeğini belirleyin:

$$\mathbf{A}_1=\begin{pmatrix}1&2&3\\2&4&6\\1&0&1\end{pmatrix}\qquad\text{ve}\qquad \mathbf{A}_2=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}$$

ve her biri için rank-sıfırlık teoremini kontrol edin. İki matristen hangisi tersinirdir?

:::loesung
$\mathbf{A}_1$: İkinci satır birincinin iki katıdır. Birinci satırın iki katı ikinci satırdan, birinci satır da üçüncü satırdan çıkarılınca $(1,2,3)$, $(0,0,0)$, $(0,-2,-2)$ satırları kalır; alttaki iki satırın yeri değiştirilince bu, iki pivotlu bir basamak biçimidir, dolayısıyla $\operatorname{rank}\mathbf{A}_1=2$. Çekirdeği $x_1+2x_2+3x_3=0$ ve $-2x_2-2x_3=0$ denklemleri verir: $x_3=t$ ile $x_2=-t$ ve $x_1=-2(-t)-3t=-t$, dolayısıyla $\ker\mathbf{A}_1=\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$. Sağlama: İlk iki sütunun toplamı $(3,\,6,\,1)^{\top}$, üçüncü sütun da $(3,\,6,\,1)^{\top}$. Rank-sıfırlık teoremi: $1+2=3$. $\mathbf{A}_1$ tersinir değildir.

$\mathbf{A}_2$: Birinci satır üçüncü satırdan çıkarılınca $(0,\,-1,\,1)$ oluşur; buna ikinci satır eklenince $(0,\,0,\,2)$ oluşur. Üç pivot vardır, dolayısıyla $\operatorname{rank}\mathbf{A}_2=3$ ve $\ker\mathbf{A}_2=\{\mathbf{0}\}$. Rank-sıfırlık teoremi: $0+3=3$. $\mathbf{A}_2$ tersinirdir; determinantı $1\cdot(1-0)-1\cdot(0-1)+0=2\ne0$ olur.
:::
:::

:::aufgabe Alıştırma 32 ★★ Kilogram ve libre
<span class="anker" id="aufg-32"></span>

Kişilerin veri matrisini kullanın (alt kesim [13.6](#stufe-13-6)).

<ol class="al">

<li>

Üç kişinin hepsi için aynı tahminleri veren iki farklı ağırlık vektörü verin; biri yalnızca kilogram sütununu, öteki yalnızca libre sütununu kullansın.

</li>

<li>

Tablo libre değerlerini virgülden sonra bir basamağa yuvarlanmış olarak veriyor. Yuvarlanmış tablonun sütunları hâlâ tam olarak doğrusal bağımlı mıdır? Bu, yuvarlanmış verilerden hesaplanan rank hakkında ne söyler?

</li>

</ol>

:::loesung
(a) $(0,\,1,\,0)^{\top}$ ağırlıkları her kişi için kilogram cinsinden kütlesini, yani $(70,\,85,\,60)^{\top}$ değerlerini tahmin eder. Yalnızca libre sütununu kullanan $(0,\,0,\,1/c)^{\top}\approx(0;\ 0;\ 0{,}4536)^{\top}$ ağırlıkları da aynı tahminleri verir, çünkü $\frac1c\cdot c\,x=x$. İki ağırlık vektörü arasındaki fark $\frac1c\,(0,\,c,\,-1)^{\top}$, yani çekirdekten bir vektördür.

(b) Yuvarlanmış libre değerlerinin kilogram değerlerine oranları $154{,}3/70\approx2{,}20429$, $187{,}4/85\approx2{,}20471$ ve $132{,}3/60=2{,}205$ olur; tam olarak eşit değildir. Demek ki yuvarlanmış sütunlar artık tam olarak orantılı değildir ve yuvarlanmış tablo hesap bakımından tam ranka, yani $3$ rankına sahiptir. İçerik bakımından hiçbir şey değişmemiştir: Libre sütunu hâlâ neredeyse yalnızca kilogram sütununun bilgisini taşır. Rank, küçücük yuvarlamalar yüzünden $2$ değerinden $3$ değerine sıçrar. Bu yüzden ölçülmüş ya da yuvarlanmış verilerde rank tek başına, iki özniteliğin pratikte aynı bilgiyi taşıyıp taşımadığını söylemez.
:::
:::

:::aufgabe Alıştırma 33 ★★ Sayı olarak bir semt
<span class="anker" id="aufg-33"></span>

Daireler ya kuzeyde ya da güneydedir. Bu, iki özniteliğe çevrilir: “Kuzey”, kuzeydeki daireler için $1$, öbürleri için $0$ olur; “Güney” de aynı biçimde güney için tanımlanır. Bir taban fiyat için ayrıca bir birler sütunu eklenir (alt kesim [8.5](lineare-abbildungen.html#stufe-8-5)). Biri kuzeyde, biri güneyde olmak üzere sıralanmış dört daire şunu verir:

$$\mathbf{X}=\begin{pmatrix}1&1&0\\1&0&1\\1&1&0\\1&0&1\end{pmatrix}\qquad(\text{sütunlar: birler, kuzey, güney}).$$

<ol class="al">

<li>

$\mathbf{X}$ matrisinin rankını ve çekirdekte bir $\mathbf k\ne\mathbf{0}$ vektörü belirleyin. Bunun arkasında sütunlar arasındaki hangi ilişki yatıyor?

</li>

<li>

$(100,\,20,\,0)^{\top}$ ve $(80,\,40,\,20)^{\top}$ ağırlıklarının aynı tahminleri verdiğini gösterin. Bilgi kaybetmeden bu bağımlılık nasıl giderilir?

</li>

</ol>

:::loesung
(a) Her daire ya kuzeyde ya da güneydedir; dolayısıyla “Kuzey” sütunu ile “Güney” sütununun toplamı her satırda $1$, yani birler sütununa eşittir. Sütunlar doğrusal bağımlıdır ve $\mathbf k=(1,\,-1,\,-1)^{\top}$ çekirdektedir: $\mathbf{X}\mathbf k=\mathbf{0}$. Birinci ve ikinci sütun doğrusal bağımsızdır, dolayısıyla $\operatorname{rank}\mathbf{X}=2$ olur.

(b) $\mathbf{X}\,(100,\,20,\,0)^{\top}=(120,\,100,\,120,\,100)^{\top}$ ve $\mathbf{X}\,(80,\,40,\,20)^{\top}=(120,\,100,\,120,\,100)^{\top}$. İki ağırlık vektörü arasındaki fark $(20,\,-20,\,-20)^{\top}=20\,\mathbf k$ olur. Bağımlılık, “Kuzey” ve “Güney” sütunlarından biri, örneğin “Güney” çıkarılarak giderilir. O zaman taban fiyat güneydeki fiyattır, “Kuzey” sütununun ağırlığı da kuzey için fiyata eklenen tutardır. Bilgi kaybolmaz, çünkü “Güney” her zaman $1-\text{Kuzey}$ olur ve her an geri hesaplanabilir.
:::
:::
