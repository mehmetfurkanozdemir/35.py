# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:30:33 2021

@author: Pc
"""

while True:
    sayi=input("Bir sayı giriniz: ")
    try :
        sayi=1/float(sayi)
    except  ValueError:
        print("Geçersiz bir sayı girdiniz, tekrar deneyin")
        continue
    except ZeroDivisionError:
        continue
    except Exception:
        print("Sistem yöneticinize başvurun")
   
    finally :
        print("sonuc :",sayi)
        print("islem bitti!!!")
    
    break   #break koyma sebebi valuerror ve zerodivisionerror olursa kırmızı yazılı hata vermesin ve uyarsın ,break sayesinde hata aldığımızda sonsuz döngü sona erer.



