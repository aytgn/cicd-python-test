def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        raise ValueError("Bölen sıfır olamaz.")
    return a / b

if __name__ == '__main__':
    print("--- Gelişmiş Hesap Makinesi Uygulaması ---")
    try:
        islem = input("İşlem seçin (+, -, *, /): ")
        s1 = float(input("1. Sayı: "))
        s2 = float(input("2. Sayı: "))

        if islem == '+':
            print(f"Sonuç: {topla(s1, s2)}")
        elif islem == '-':
            print(f"Sonuç: {cikar(s1, s2)}")
        elif islem == '*':
            print(f"Sonuç: {carp(s1, s2)}")
        elif islem == '/':
            print(f"Sonuç: {bol(s1, s2)}")
        else:
            print("Geçersiz işlem!")
    except ValueError as e:
        print(f"Hata: {e}")