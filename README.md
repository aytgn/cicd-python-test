# Otonom Matematik Botu
Bu proje, GitHub Issue'ları üzerinden çalışan, tamamen sunucusuz (serverless) bir hesap makinesi platformudur.

## (CI/CD) Süreci
Sistemdeki tüm CI/CD süreci, yerel bilgisayarınızda yaptığınız kod değişikliklerini terminalden sırasıyla `git add .`, `git commit -m "mesajınız"` ve `git push` komutlarıyla GitHub'a göndermenizle otomatik olarak tetiklenir ve şu adımları izler:

* **Kalite Kontrol:** `main` dalına gelen bu yeni kodlar, CI iş akışını (yaml) otomatik olarak tetikleyerek bağımsız bir sunucuda test edilir. Testi geçemeyen hatalı kodların ileri gitmesi engellenir.
* **Otomatik Dağıtım:** Sadece testleri başarıyla geçen sağlam kodlar CD iş akışını tetikler. Bu otomasyon, hiçbir insan müdahalesine gerek kalmadan `main` dalındaki o taze kodları alır ve canlı ortamı temsil eden `stable` dalına otomatik olarak birleştirir (`merge`).
* **Kesintisiz Hizmet:** Bot veya canlı uygulama, geliştirme aşamasındaki riskli kodlara asla bulaşmaz; çalışırken her zaman en son test edilmiş ve onaylanmış olan `stable` dalındaki kodu (`ref: stable` parametresiyle) referans alarak kullanır.

Git Actions sayfasından geçmiş ve güncel aksiyonlar takip edilebilir.

## Nasıl Kullanılır?

1. Deponun **Issues** sekmesine gidilir.
2. **New Issue** butonuna tıklanır.
3. Başlık (Title) kısmına şu formatta komut yazılır: `işlem: sayı1, sayı2`.
4. Bot saniyeler içinde hesaplamayı yapıp sonucu yorum olarak yazacak ve issue kapanacaktır.

## Desteklenen Komutlar
Aşağıdaki formatları kullanarak işlem yapabilirsiniz:
* **Toplama:** `topla: 10, 20`
* **Çıkarma:** `cikar: 50, 10`
* **Çarpma:** `carp: 5, 4`
* **Bölme:** `bol: 100, 2`