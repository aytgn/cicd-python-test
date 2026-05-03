# CI/CD Python Hesap Makinesi 🚀

Bu proje, modern DevOps süreçlerini (CI/CD) anlamak ve uygulamak için geliştirilmiş, Docker tabanlı bir hesap makinesi uygulamasıdır.

## Özellikler 🛠️
* **4 İşlem Desteği:** Toplama, çıkarma, çarpma ve bölme işlemlerini başarıyla gerçekleştirir.[cite: 1]
* **Otomatik Test:** Her kod güncellemesinde `unittest` ile tüm fonksiyonlar kontrol edilir.[cite: 2]
* **Dockerize:** Uygulama, her ortamda çalışabilmesi için Docker ile paketlenmiştir.
* **Tam Otomasyon:** GitHub Actions ile CI/CD boru hattı (pipeline) kurulmuştur.

## Nasıl Çalıştırılır? 🐳
Herhangi bir kurulum yapmadan, Docker yüklü her terminalde şu komutu çalıştırarak uygulamaya erişebilirsiniz:

```bash
docker run -it --rm aytgn/hesap-makinem:latest

