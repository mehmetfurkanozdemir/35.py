sayi = int(input("lütfen bir sayi giriniz"))
sonuc = 1

for x in range(sayi+1):
    if x==0 :
        continue
    sonuc = sonuc*x
    
print(sonuc)    #sadece sonucu verir


