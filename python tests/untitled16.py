sayi = int(input("lütfen bir sayi giriniz"))
sonuc = 1

for x in range(1,sayi+1):
    sonuc = sonuc*x
    
print(sonuc)    #sadece sonucu verir




sayi = int(input("lütfen bir sayi giriniz"))
sonuc = 1

for x in range(1,sayi+1):
    sonuc = sonuc*x
    
    print(sonuc)    #5 e kadar olan tüm faktöriyeli verir 
    
while sayi > 0:
    sonuc = sonuc*sayi
    sayi = sayi-1
    print(sonuc)







