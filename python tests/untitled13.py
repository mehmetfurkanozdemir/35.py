mevcut = int(input("Sınıf Mevcudunu Giriniz :"))


for x in range(mevcut):
    
    vize= int(input("Vize Notunu Giriniz :"))
    final = int(input("Final Notunu Giriniz :"))
    ort = ((vize)*40/100+(final)*60/100)
    if ort>=70:
        print("geçtiniz",ort)
    else :
        print("kaldınız",ort)


