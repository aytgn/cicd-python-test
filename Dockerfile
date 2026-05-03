# 1. TEMEL: Bize içinde hazır Python 3.10 olan ufak, temiz bir işletim sistemi ver
FROM python:3.10-slim

# 2. ALAN: Kutunun içinde 'app' adında bir çalışma klasörü oluştur ve oraya gir
WORKDIR /app

# 3. KOPYALA: Bilgisayarımızdaki (veya GitHub'daki) tüm kodları kutunun içindeki bu klasöre kopyala
COPY . /app

# 4. ÇALIŞTIR: Kutu canlı sunucuda açıldığı anda varsayılan olarak bu komutu ateşle
CMD ["python", "calculator.py"]