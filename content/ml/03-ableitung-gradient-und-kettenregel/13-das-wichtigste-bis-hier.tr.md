---
title: Buraya kadarki temel noktalar
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15231300
summary: Bir sayı girdilerine nasıl tepki verir: teğetten ters moda
tags: 
lang: tr
---

:::kern Buraya kadarki temel noktalar
<ul>

<li>

Türev: $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$; $x$ yakınında $f(x+h)\approx f(x)+f'(x)h$ olur, hata $h$'den hızlı sıfıra gider. İkinci türevle: $f(x+h)\approx f(x)+f'(x)h+\tfrac12f''(x)h^2$.

</li>

<li>

Zincir kuralı: $(f\circ g)'(x)=f'(g(x))\,g'(x)$; uzun zincirlerde bütün çarpanların çarpımı. Lojistik fonksiyon: $\sigma'=\sigma(1-\sigma)\le\tfrac14$.

</li>

<li>

Sütun olarak $\nabla f\in\mathbb{R}^d$ gradyanı; $f$ türevlenebilirse $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$; yalnızca kısmi türevler yetmez.

</li>

<li>

Yönlü türev $D_{\mathbf{u}}f=\nabla f^{\top}\mathbf{u}$; en dik çıkış $\nabla f$ doğrultusunda, eğimi $\lVert\nabla f\rVert$ (Cauchy-Schwarz); $\nabla f$ eş yükselti eğrilerine diktir; $-\nabla f$ yalnızca yuvarlak eş yükselti eğrilerinde en alçak noktayı gösterir.

</li>

<li>

Jacobi matrisi $\mathbf{J}_{\mathbf{g}}\in\mathbb{R}^{m\times n}$, her çıktı için bir satır: $\mathbf{g}(\mathbf{x}+\mathbf{h})\approx\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}\mathbf{h}$; $\mathbf{A}\mathbf{x}+\mathbf{b}$ için $\mathbf{A}$ olur, eleman eleman uygulanan fonksiyonlar için köşegendir.

</li>

<li>

Zincir kuralı: $\mathbf{J}_{\mathbf f\circ\mathbf{g}}=\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}$, bileşen bileşen bütün yollar üzerinden toplam; $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$.

</li>

<li>

$\nabla(\mathbf{a}^{\top}\mathbf{x})=\mathbf{a}$, $\nabla(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$, $\nabla\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$, $\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}$; $F=f(\mathbf{A}\mathbf{x})$ ile $\mathbf{y}=\mathbf{A}\mathbf{x}$ boyunca geriye doğru: $\nabla_{\mathbf{A}}F=\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$, $\nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\nabla f(\mathbf{y})$.

</li>

<li>

Hesse matrisi $\mathbf{H}_f$, Schwarz'a göre simetrik; $f(\mathbf{x}+\mathbf{h})\approx f+\nabla f^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$; $\mathbf{u}$ doğrultusundaki eğrilik $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$, en küçük ve en büyük özdeğer arasında.

</li>

<li>

Hesaplama grafiği: temel işlemler, saklanan değerlerle ileri hesaplama, kenarlarda yerel türevler.

</li>

<li>

İleri mod: teğet değerleri, her doğrultu için bir geçiş ($\mathbf{J}\dot{\mathbf{x}}$). Ters mod: $\bar f=1$'den başlayarak $\bar a=\sum\bar b\,\partial b/\partial a$ eşlenikleri, gradyanın tamamı için bir geçiş, maliyet bir değerlendirmenin küçük bir katı, bedeli: bellek.

</li>

<li>

Sayısal: ileri farkın hatası $\approx\tfrac12f''h$, merkezi farkınki $\approx\tfrac16f'''h^2$; yuvarlama $\varepsilon_{\mathrm M}/h$ gibi büyür, V eğrisi buradan gelir; bağıl hatayla gradyan kontrolü, $10^{-2}$'nin üzeri yanlış, $10^{-7}$'nin altı iyi.

</li>

</ul>
:::

:::merke Üç cümlede cevap
<ol>

<li>

Bir sayının girdilerindeki küçük değişimlere nasıl tepki verdiğini doğrusal yaklaşımı söyler: Her girdi kendi kısmi türevi çarpı kendi değişimi kadar katkıda bulunur ve katkılar toplanarak gradyanla iç çarpımı verir.

</li>

<li>

Cauchy-Schwarz eşitsizliğine göre bu iç çarpım, sabit uzunluktaki adımlarda gradyan doğrultusunda en büyüktür; gradyan bu yüzden en dik biçimde yokuş yukarıyı gösterir ve eş yükselti eğrilerine diktir.

</li>

<li>

Sayı uzun bir hesap adımları zinciriyle ortaya çıkıyorsa türevi Jacobi matrislerinin bir çarpımı, yani bütün yollar üzerinden bir toplamdır; ters mod bu çarpımı sayıdan başlayarak satır vektörleriyle hesaplar ve böylece bütün türevleri, tek bir değerlendirmenin maliyetinin küçük bir katına, bir kerede verir.

</li>

</ol>
:::

**Tüm sonuçların ardındaki tek ilke.** Bu bölümdeki neredeyse her şey tek bir ilkeden çıkar: Bir noktaya yeterince yakında her türevlenebilir fonksiyon doğrusaldır. Türev, gradyan ve Jacobi matrisi bu doğrusal yaklaşımdır; zincir kuralı doğrusal yaklaşımları art arda bağlar ve bu sırada matrislerini çarpar; ileri ve ters mod da bu çarpımı parantezlemenin iki yoludur.

| Sonuç | Nereden geliyor |
|---|---|
| Türev ve teğet | hatası $h$'den hızlı sıfıra giden tek doğru (Kesim [1](die-ableitung.html#stufe-1)) |
| Çarpım kuralı | $\Delta u\,\Delta v$ köşe parçası ikinci mertebeden küçüktür (Kesim [1.4](die-ableitung.html#stufe-1-4)) |
| Tek değişkenli zincir kuralı | her aşama küçük değişimleri kendi çarpanıyla iletir (Kesim [2](die-kettenregel.html#stufe-2)) |
| Gradyan ve teğet düzlem | küçük değişimlerin etkileri toplanır (Kesim [3](partielle-ableitungen-und-der-gradient.html#stufe-3)) |
| En dik çıkış | $\nabla f^{\top}\mathbf{u}$ için Cauchy-Schwarz (Kesim [4](richtungsableitung-und-steilster-anstieg.html#stufe-4)) |
| Gradyan eş yükselti eğrisine dik | eş yükselti eğrisi boyunca eğim sıfırdır (Kesim [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) ve [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6)) |
| Jacobi matrisi | vektör değerli bir fonksiyonun doğrusal yaklaşımının matrisi (Kesim [5](die-jacobi-matrix.html#stufe-5)) |
| Matris çarpımı olarak zincir kuralı, yollar üzerinden toplam | art arda bağlanmış doğrusal yaklaşımlar (Kesim [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6)) |
| Matris özdeşlikleri, geri kuralı | sabit bir düzen kuralıyla bileşen bileşen zincir kuralı (Kesim [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7)) |
| Hesse matrisi ve eğrilik | bir doğru boyunca ikinci türev, bir kuadratik formun özdeğerleri (Kesim [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8)) |
| Ters mod | yolları ilk kenarlarına göre gruplamak, ara toplamları yeniden kullanmak; soldan parantezleme (Kesim [9](rechengraphen.html#stufe-9) ve [10](automatische-differentiation.html#stufe-10)) |
| Merkezi fark, V eğrisi | çift dereceli Taylor terimleri sadeleşir; yuvarlama hataları $1/h$ gibi büyür (Kesim [11](numerische-ableitung-und-gradientenprufung.html#stufe-11)) |
