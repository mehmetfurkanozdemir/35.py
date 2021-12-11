#try :                       # girdileri kontrol etmek için kullanılır hepsi
    
    
#except:


#except:


#finally    

while True:
    sayi=input("Bir sayı giriniz: ")
    try :
        sayidegeri=float(sayi)
    except  ValueError:
        print("Geçersiz bir sayı girdiniz, tekrar deneyin")
        continue
    print("SAYİNİN KARESİ :",pow(sayidegeri,2))
    
    break





