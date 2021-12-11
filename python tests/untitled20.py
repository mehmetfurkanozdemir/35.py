def faktoriyel(sayi):
    sonuc =1
    for i in range(1,sayi+1):
        sonuc = sonuc*i
    return sonuc


    



sayi = int(input("Lütfen bir sayı giriniz :"))
fak_sonuc = faktoriyel(sayi)
print(pow(fak_sonuc,2))




