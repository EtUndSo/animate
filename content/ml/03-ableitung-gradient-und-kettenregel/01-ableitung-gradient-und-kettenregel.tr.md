---
title: Genel Bakış: Türev, Gradyan ve Zincir Kuralı
kurz: Genel Bakış
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15230100
summary: Bir sayı girdilerine nasıl tepki verir: teğetten ters moda
tags: 
lang: tr
---

## Konunun özü

Bir sayı çoğu zaman başka birçok sayıya bağlıdır. [Bölüm 1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html)'deki ağırlıklı toplamın bir daire için tahmin ettiği fiyat, her ağırlığa ve her özniteliğe bağlıdır. Bir hata vektörünün uzunluğu, onun her bileşenine bağlıdır. Uzun bir hesabın sonucu, hesabın başladığı her değere bağlıdır. Bu bölüm şunu soruyor: Girdilerinden biri biraz değiştirildiğinde böyle bir sayı ne kadar ve hangi yönde değişir? Peki girdiler binlerce ise: Sayının en hızlı artması ya da en hızlı azalması için hepsi aynı anda hangi yönde kaydırılmalıdır?

Buna pratik bir soru eklenir. Sayı çoğu zaman basit hesap adımlarından oluşan uzun bir zincirle ortaya çıkar. Her girdi tek tek biraz değiştirilip sonunda ne çıktığına bakılabilirdi. Bir milyon girdide bu, bütün hesabı bir milyon kez tekrarlamak demek olurdu. Daha hızlısı var mı? Ve bu duyarlılıklar için kendi türettiğiniz ya da programladığınız bir formülün gerçekten doğru olup olmadığını nasıl denetlersiniz?

Yararı şu: Bu cevaplarla bir sonucun en çok hangi ayar düğmelerine bağlı olduğu ve girdilerdeki küçük ölçüm hatalarının sonuca nasıl yansıdığı bilinir. Karmaşık bir fonksiyon bir noktanın yakınında çok daha basit bir fonksiyonla değiştirilebilir ve bu sırada yapılan hatanın ne kadar büyük olduğu kestirilebilir. Ayrıca sayı, çok sayıda girdisi olan çok uzun bir hesaptan çıksa bile duyarlılıklar hesaplanabilir. Verilerden öğrenen yöntemlerin neredeyse hepsi bu araçlara ihtiyaç duyar.

**Bu bölümle nasıl çalışılır?** Konular birbirinin üzerine kurulur ve her yeni kavramın örnek içeren kendi alt başlığı vardır. Açılır kutular arka plan bilgisini (bir yöntemin neden işe yaradığını ve nereden geldiğini), türetmeleri ve ispatları içerir; okumaya devam etmek için bunlara gerek yoktur. Alıştırmaları (★ ile ★★★ arası) önce kendiniz çözmeye çalışın ve programları gerçekten çalıştırın; çözümü her alıştırmanın hemen altında açabilirsiniz.
